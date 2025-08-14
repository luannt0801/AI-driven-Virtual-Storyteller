# Media utilities
from moviepy import ImageClip, concatenate_videoclips, AudioFileClip
from typing import List
import os

# from moviepy.video.VideoClip import ImageClip
# from moviepy.video.compositing.concatenate import concatenate_videoclips
# from moviepy.audio.io.AudioFileClip import AudioFileClip

# def build_video_from_assets(
#     image_paths: List[str],
#     audio_path: str,
#     out_path: str = "story_video.mp4",
#     fps: int = 24,
#     min_sec_per_image: float = 2.5,
#     max_sec_per_image: float = 8.0
# ) -> str:
#     """
#     Compose a slideshow video from image_paths and a narration audio file.
#     Durations are automatically balanced to fit the audio length.
#     """
#     if not image_paths:
#         raise ValueError("No image paths provided.")
#     if not os.path.exists(audio_path):
#         raise FileNotFoundError(f"Audio not found: {audio_path}")

#     # Load audio to get exact duration
#     audio_clip = AudioFileClip(audio_path)
#     audio_duration = audio_clip.duration  # in seconds

#     # Decide durations for each image
#     n = len(image_paths)
#     base_dur = max(min_sec_per_image, audio_duration / max(1, n))
#     base_dur = min(base_dur, max_sec_per_image)

#     # Build image clips
#     img_clips = []
#     for p in image_paths:
#         clip = ImageClip(p).with_duration(base_dur)
#         img_clips.append(clip)

#     # Concatenate and set audio
#     video = concatenate_videoclips(img_clips, method="compose")
#     video = video.with_audio(audio_clip)

#     # If total video is longer than audio, trim to audio; if shorter, extend last frame
#     if video.duration > audio_duration:
#         video = video.subclipped(0, audio_duration)
#     elif video.duration < audio_duration:
#         last = ImageClip(image_paths[-1]).with_duration(audio_duration - video.duration)
#         video = concatenate_videoclips([video, last], method="compose")
#         video = video.with_audio(audio_clip)

#     # Write file
#     video.write_videofile(out_path, fps=fps, codec="libx264", audio_codec="aac")
#     audio_clip.close()
#     return out_path


def build_video_from_assets(
    image_paths: List[str],
    audio_path: str,
    out_path: str = "story_video.mp4",
    fps: int = 24,
    min_sec_per_image: float = 2.5,
    max_sec_per_image: float = 8.0
) -> str:
    if not image_paths:
        raise ValueError("No image paths provided.")
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio not found: {audio_path}")

    # Load audio (không đóng cho tới khi render xong)
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration

    n = len(image_paths)
    base_dur = max(min_sec_per_image, audio_duration / max(1, n))
    base_dur = min(base_dur, max_sec_per_image)

    img_clips = [ImageClip(p).with_duration(base_dur) for p in image_paths]
    video = concatenate_videoclips(img_clips, method="compose")

    # Trim hoặc extend để khớp audio
    if video.duration > audio_duration:
        video = video.subclipped(0, audio_duration)
    elif video.duration < audio_duration:
        last = ImageClip(image_paths[-1]).with_duration(audio_duration - video.duration)
        video = concatenate_videoclips([video, last], method="compose")

    # Gắn audio và render
    final_video = video.with_audio(audio_clip)
    final_video.write_videofile(out_path, fps=fps, codec="libx264", audio_codec="aac")

    audio_clip.close()  # đóng sau khi render
    return out_path
