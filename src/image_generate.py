import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class StoryImageGenerator:
    def __init__(self, model_path="../models/stable-diffusion-v1-5",
                 model_id="runwayml/stable-diffusion-v1-5", device=None):
        """
        Initialize Stable Diffusion pipeline.
        - model_path: local path to save/load model
        - model_id: Hugging Face model ID (only used if download is needed)
        - device: 'cuda' or 'cpu' (auto-detect if None)
        """
        self.model_path = model_path
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

        # Load model locally if exists, otherwise download
        if os.path.exists(os.path.join(model_path, "model_index.json")):
            print("Loading Stable Diffusion from local storage...")
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_path,
                torch_dtype=torch.float16 if self.device.startswith("cuda") else torch.float32
            ).to(self.device)
        else:
            print("⬇ Downloading Stable Diffusion model...")
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float16 if self.device.startswith("cuda") else torch.float32
            )
            self.pipe.save_pretrained(model_path)  # Save for offline use
            self.pipe = self.pipe.to(self.device)

    def generate_images_from_story(self, story_text, output_dir="story_images", 
                                   image_per_sentence=True, guidance_scale=7.5):
        """
        Generate multiple images from a story text.
        - story_text: full story (string)
        - output_dir: folder to save generated images
        - image_per_sentence: if True, split by sentences; else split by paragraphs
        - guidance_scale: prompt guidance for diffusion
        Returns: list of saved image file paths
        """
        os.makedirs(output_dir, exist_ok=True)

        # Split story into parts
        if image_per_sentence:
            parts = [s.strip() for s in story_text.split('.') if s.strip()]
        else:
            parts = [p.strip() for p in story_text.split('\n') if p.strip()]

        saved_paths = []
        for idx, part in enumerate(parts, start=1):
            print(f"Generating image {idx} for: {part[:50]}...")
            image = self.pipe(part, guidance_scale=guidance_scale).images[0]
            file_path = os.path.join(output_dir, f"story_part_{idx}.png")
            image.save(file_path)
            saved_paths.append(file_path)

        print(f"Generated {len(saved_paths)} images.")
        return saved_paths


# # ===== Example usage =====
# if __name__ == "__main__":
#     generator = StoryImageGenerator()

#     story = """
#     Once upon a time, there was a brave princess who lived in a shining castle.
#     One day, she encountered a fierce dragon in the forest.
#     With courage and kindness, she befriended the dragon and they protected the kingdom together.
#     """

#     generator.generate_images_from_story(story, output_dir="princess_dragon_images")
