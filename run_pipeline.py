import subprocess
import sys
import os

# Đường dẫn python.exe của venv
venv_python = r"D:\2025\Master BKHN\Ky thuat lap trinh noi dung so\AI-driven-Virtual-Storyteller\luan\Scripts\python.exe"

# Lệnh chạy pipeline
cmd = [
    venv_python,
    "main_2.py",
    "--prompt", "tell me a story about a princess and dragon",
    "--gpt_model_path", "../models/gpt2",
    "--sd_model_path", "../models/stable-diffusion-v1-5",
    "--sd_model_id", "runwayml/stable-diffusion-v1-5",
    "--bark_model_path", "../models/suno_bark_small",
    "--voice_preset", "v2/en_speaker_6",
    "--split_mode", "sentence",
    "--max_images", "8",
    "--output_dir", "outputs",
    "--video_name", "story_video.mp4"
]

subprocess.run(cmd)