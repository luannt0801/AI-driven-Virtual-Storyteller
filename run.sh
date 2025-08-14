#!/bin/bash
# Run story-to-video pipeline on Ubuntu/Linux
python3 story_to_video.py \
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
