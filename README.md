
<!-- 
echo "# -AI-driven-Virtual-Storyteller" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/luannt0801/-AI-driven-Virtual-Storyteller.git
git push -u origin main -->


[![transformers](https://img.shields.io/badge/transformer-4.55.0-blue)](https://huggingface.co/docs/transformers/installation)
[![torch](https://img.shields.io/badge/torch-2.2.1-green)](https://pytorch.org/get-started/locally/)
[![cuda](https://img.shields.io/badge/cuda-12.06-pink)](https://huggingface.co/docs/transformers/installation)
[![Python](https://img.shields.io/badge/Python-3.12-red)](https://www.python.org/downloads/release/python-3120)
[![Nodejs](https://img.shields.io/badge/Nodejs-24.5.0-orange)](https://nodejs.org/en)
[![Luan](https://img.shields.io/badge/Luan-8.1.2002-white)](https://github.com/luannt0801)

# StorieAlate

StorieAlate is an AI-powered virtual storyteller that generates immersive, narrated stories accompanied by dynamic visuals and background music. Combining cutting-edge NLP, text-to-speech synthesis, and procedural or GAN-based visual generation, StorieAlate brings stories to life in a fully interactive and multi-sensory experience.

![StorieAlate](/docs/imgs/StoryTeller.png)

---

## Architect

![Architecture](/docs/imgs/diagram_AIDST.png)


**GPT-2**

![imgs](/docs/imgs/gpt-2.png)

**Suno-bark**

![imgs](/docs/imgs/suno-bark.png)

**Stable-diffusion**

![imgs](/docs/imgs/stable-diffusion.png)

---

## Output

**Story**
```
"A long-haired blonde princess was trapped in a castle guarded by a dragon. The prince saved the princess. They lived happily together and ruled the kingdom. One night their long-lost friend, the dragon called Kreygasm, appeared and told him he had killed Kreygasm and had given him the key to the dragon's lair. It was only that time that he revealed to Kreygasm that he was possessed by his demonic self.

It was this dark, frightening reality that brought Kreygasm back to life for the first time. Soon, Kreygasm became a hero. It has ever since been taught that his demonic self is stronger than those who take it down.

- Chapter 47

[Previous Chapter] [Table of Contents] [Next Chapter]
```

**Audio output**
<audio controls="controls">
  <source type="audio/mp3" src="/outputs/narration.wav"></source>
  <source type="audio/ogg" src="filename.ogg"></source>
  <p>Your browser does not support the audio element.</p>
</audio>

**Video**
![](/outputs/story_video.mp4)

<video controls="controls">
  <source type="video/mp4" src="/outputs/story_video.mp4"></source>
  <source type="video/webm" src="filename.webm"></source>
  <p>Your browser does not support the video element.</p>
</video>

**Story Compose**

---

How to run this project

In client side
```html
run live-server index.html
```

Server side
```python
main.py
  --prompt "tell me a story about a princess and dragon" ^
  --gpt_model_path "%ROOT_PATH%/gpt2" ^
  --sd_model_path "%ROOT_PATH%/stable-diffusion-v1-5" ^
  --sd_model_id "runwayml/stable-diffusion-v1-5" ^
  --bark_model_path "%ROOT_PATH%/suno_bark_small" ^
  --voice_preset "v2/en_speaker_6" ^
  --split_mode sentence ^
  --max_images 8 ^
  --output_dir outputs ^
  --video_name story_video.mp4
```

```bat
run.bat
```
