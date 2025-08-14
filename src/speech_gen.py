import re
import numpy as np
import torch
import scipy
from transformers import BarkModel, AutoProcessor

class BarkTTS:
    def __init__(self, model_path="../models/suno_bark_small", device=None):
        """
        Initialize Bark TTS model and processor.
        - model_path: local directory to store/load Bark model.
        - device: 'cuda' or 'cpu' (auto-detect if None).
        """
        self.model_path = model_path
        self.device = device or ("cuda:0" if torch.cuda.is_available() else "cpu")

        # Load model & processor (offline if available, otherwise download)
        # if os.path.exists(os.path.join(model_path, "config.json")) and \
        #    os.path.exists(os.path.join(model_path, "preprocessor_config.json")):
        #     print("Loading Bark model & processor from local storage...")
        #     self.model = BarkModel.from_pretrained(model_path, trust_remote_code=True).to(self.device)
        #     self.processor = AutoProcessor.from_pretrained(model_path, local_files_only=True)
        # else:
        #     print("Downloading Bark model & processor from Hugging Face...")
        #     self.model = BarkModel.from_pretrained(
        #         "suno/bark-small",
        #         trust_remote_code=True,
        #         cache_dir=model_path
        #     ).to(self.device)
        #     self.processor = AutoProcessor.from_pretrained(
        #         "suno/bark-small",
        #         cache_dir=model_path
        #     )
        #     # Save locally for offline usage
        #     self.model.save_pretrained(model_path)
        #     self.processor.save_pretrained(model_path)

        self.model = BarkModel.from_pretrained(self.model_path, trust_remote_code=True).to(self.device)
        self.processor = AutoProcessor.from_pretrained(model_path, local_files_only=True)

        print(f"Loading Bark TTS model from local path: {self.model_path}")
        self.model = BarkModel.from_pretrained(
            model_path,
            trust_remote_code=True,
            local_files_only=True  
        ).to(self.device)

        self.processor = AutoProcessor.from_pretrained(
            model_path,
            local_files_only=True 
        )

        # Ensure pad token is set
        if self.processor.tokenizer.pad_token is None:
            self.processor.tokenizer.pad_token = self.processor.tokenizer.eos_token

        self.sampling_rate = self.model.generation_config.sample_rate

    def generate_all_speech(self, text, voice_preset=None, output_wav="bark_out.wav",
                        num_beams=None, temperature=None, semantic_temperature=None):
        """
        Generate speech from text.
        - text: input text prompt
        - voice_preset: optional voice preset string (e.g., "v2/en_speaker_6")
        - output_wav: path to save generated .wav file
        - num_beams, temperature, semantic_temperature: optional generation settings
        Returns: path to saved wav file
        """
        # Prepare inputs
        if voice_preset:
            inputs = self.processor(text, voice_preset=voice_preset)
        else:
            inputs = self.processor(text)

        # Move inputs to target device
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # Generation arguments
        gen_kwargs = {}
        if num_beams is not None:
            gen_kwargs["num_beams"] = num_beams
        if temperature is not None:
            gen_kwargs["temperature"] = temperature
        if semantic_temperature is not None:
            gen_kwargs["semantic_temperature"] = semantic_temperature

        # Generate speech
        with torch.no_grad():
            speech_output = self.model.generate(**inputs, **gen_kwargs)

        # Save to wav file
        scipy.io.wavfile.write(output_wav, rate=self.sampling_rate, data=speech_output[0].cpu().numpy())
        print(f"Speech saved to: {output_wav}")

        return output_wav
    

    def generate_speech(self, text, voice_preset=None, output_wav="bark_out.wav",
                        num_beams=None, temperature=None, semantic_temperature=None):
        """
        Generate speech from text, sentence-by-sentence, and merge into one WAV.
        """
        sentences = re.split(r'(?<=[\.\!\?])\s+', text.strip())
        sentences = [s.strip() for s in sentences if s.strip()]

        all_audio = []

        for idx, sentence in enumerate(sentences, 1):
            print(f"[Bark] Generating speech for sentence {idx}/{len(sentences)}: {sentence}")

            if voice_preset:
                inputs = self.processor(sentence, voice_preset=voice_preset)
            else:
                inputs = self.processor(sentence)

            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            gen_kwargs = {}
            if num_beams is not None:
                gen_kwargs["num_beams"] = num_beams
            if temperature is not None:
                gen_kwargs["temperature"] = temperature
            if semantic_temperature is not None:
                gen_kwargs["semantic_temperature"] = semantic_temperature

            with torch.no_grad():
                speech_output = self.model.generate(**inputs, **gen_kwargs)

            # Ghép audio
            audio_np = speech_output[0].cpu().numpy()
            all_audio.append(audio_np)

        merged_audio = np.concatenate(all_audio, axis=0)

        scipy.io.wavfile.write(output_wav, rate=self.sampling_rate, data=merged_audio)
        print(f"[Bark] Full speech saved to: {output_wav}")

        return output_wav


# # ===== Example usage =====
# if __name__ == "__main__":
#     tts = BarkTTS()

#     # Generate English speech
#     tts.generate_speech(
#         text="Hello, I am an AI-generated voice speaking from Bark!",
#         voice_preset="v2/en_speaker_6",
#         output_wav="english_voice.wav"
#     )

#     # Generate French speech
#     tts.generate_speech(
#         text="Je peux générer du son facilement avec ce modèle.",
#         voice_preset="fr_speaker_3",
#         output_wav="french_voice.wav"
#     )
