import os
import re
import argparse
from typing import List, Optional

# Core AI components
from src.story_gegnerate import StoryGenerator  # user's file
from src.image_generate import StoryImageGenerator  # user's file
from src.speech_gen import BarkTTS  # user's file

from src.utils.text_preprocess import *
from src.utils.video_summarization import *


def run_pipeline(
    prompt: str,
    gpt_model_path: str = f"../models/gpt2",
    sd_model_path: str = f"../models/stable-diffusion-v1-5",
    sd_model_id: str = "runwayml/stable-diffusion-v1-5",
    bark_model_path: str = "../models/suno_bark_small",
    voice_preset: Optional[str] = "v2/en_speaker_6",
    image_split_mode: str = "sentence",
    output_dir: str = "outputs",
    max_images: int = 8,
    guidance_scale: float = 7.5,
    video_fps: int = 24,
    video_path: str = "story_video.mp4"
) -> dict:
    """
    Full pipeline: prompt -> story -> images -> narration -> video.
    Returns dict with paths to artifacts.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Generate story
    storyteller = StoryGenerator(model_path=gpt_model_path)
    story_text = storyteller.generate_story(prompt, max_new_tokens=400)
    story_txt_path = os.path.join(output_dir, "story.txt")
    with open(story_txt_path, "w", encoding="utf-8") as f:
        f.write(story_text)

    # Generate images from story
    img_gen = StoryImageGenerator(model_path=sd_model_path, model_id=sd_model_id)
    parts = smart_split(story_text, mode=image_split_mode)[:max_images]
    # If parts becomes empty (very short text), fallback to prompt
    if not parts:
        parts = [prompt]
    image_dir = os.path.join(output_dir, "images")
    image_paths = []
    for idx, p in enumerate(parts, start=1):
        # Simple enhancement: append art-style tag for consistency
        enhanced_prompt = f"{p} -- cinematic, storybook illustration, soft lighting, highly detailed"
        paths = img_gen.generate_images_from_story(
            story_text=enhanced_prompt,
            output_dir=image_dir,
            image_per_sentence=False,  # already passing one prompt per call
            guidance_scale=guidance_scale
        )
        # generate_images_from_story returns a list; we expect one image because we passed a single 'story_text'
        if paths:
            # but method saves as story_part_1.png each time; rename to unique
            src = paths[0]
            dst = os.path.join(image_dir, f"frame_{idx:02d}.png")
            os.replace(src, dst)
            image_paths.append(dst)

    # Generate narration audio
    tts = BarkTTS(model_path=bark_model_path)
    audio_path = os.path.join(output_dir, "narration.wav")
    tts.generate_speech(text=story_text, voice_preset=voice_preset, output_wav=audio_path)

    # Build video
    video_out_path = os.path.join(output_dir, video_path)
    final_video = build_video_from_assets(
        image_paths=image_paths,
        audio_path=audio_path,
        out_path=video_out_path,
        fps=video_fps
    )

    return {
        "prompt": prompt,
        "story_path": story_txt_path,
        "image_paths": image_paths,
        "audio_path": audio_path,
        "video_path": final_video
    }


def main():
    parser = argparse.ArgumentParser(description="Story-to-Video pipeline")
    parser.add_argument("--prompt", type=str, required=True, help="Story prompt (e.g., 'tell me a story about a princess and dragon')")
    parser.add_argument("--gpt_model_path", type=str, default="../models/gpt2")
    parser.add_argument("--sd_model_path", type=str, default="../models/stable-diffusion-v1-5")
    parser.add_argument("--sd_model_id", type=str, default="runwayml/stable-diffusion-v1-5")
    parser.add_argument("--bark_model_path", type=str, default="../models/suno_bark_small")
    parser.add_argument("--voice_preset", type=str, default="v2/en_speaker_6")
    parser.add_argument("--split_mode", type=str, choices=["sentence", "paragraph"], default="sentence")
    parser.add_argument("--max_images", type=int, default=8)
    parser.add_argument("--guidance_scale", type=float, default=7.5)
    parser.add_argument("--output_dir", type=str, default="outputs")
    parser.add_argument("--video_fps", type=int, default=24)
    parser.add_argument("--video_name", type=str, default="story_video.mp4")

    args = parser.parse_args()

    result = run_pipeline(
        prompt=args.prompt,
        gpt_model_path=args.gpt_model_path,
        sd_model_path=args.sd_model_path,
        sd_model_id=args.sd_model_id,
        bark_model_path=args.bark_model_path,
        voice_preset=args.voice_preset,
        image_split_mode=args.split_mode,
        output_dir=args.output_dir,
        max_images=args.max_images,
        guidance_scale=args.guidance_scale,
        video_fps=args.video_fps,
        video_path=args.video_name
    )

    print("=== Pipeline Complete ===")
    for k, v in result.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()

"""
python main2.py \
  --prompt "tell me a story about a princess and dragon" \
  --gpt_model_path "../models/gpt2" \
  --sd_model_path "../models/stable-diffusion-v1-5" \
  --sd_model_id "runwayml/stable-diffusion-v1-5" \
  --bark_model_path "../models/suno_bark_small" \
  --voice_preset "v2/en_speaker_6" \
  --split_mode sentence \
  --max_images 8 \
  --output_dir outputs \
  --video_name story_video.mp4
"""
