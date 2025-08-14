
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
[![Luan](https://img.shields.io/badge/Luan-8.1.2002-white)](https://github.com/luannt0801)

# StorieAlate

StorieAlate is an AI-powered virtual storyteller that generates immersive, narrated stories accompanied by dynamic visuals and background music. Combining cutting-edge NLP, text-to-speech synthesis, and procedural or GAN-based visual generation, StorieAlate brings stories to life in a fully interactive and multi-sensory experience.

![StorieAlate](/docs/imgs/StoryTeller.png)

---

## Architect


```bash
          +-------------------+
          |  User/API Client  |
          +--------+----------+
                   |
                   v
           +-------+--------+
           |   Orchestration | ← API Layer / Backend
           +-------+--------+
                   |
      +------------+-------------+------------+-------------+
      |                          |                          |
      v                          v                          v
+-------------+         +----------------+        +-----------------+
| Story Engine|         |   Visual Engine|        |  Audio Engine   |
|  (NLP Gen)  |         | (Image Gen /   |        | (TTS + Music)   |
+-------------+         |  Scene Builder)|        +-----------------+
       |                +----------------+                |
       v                       |                          v
 Story Script           Visual Frames             Narration + Music
       \_____________________|____________________/
                            |
                            v
                  +----------------------+
                  |   Story Composer     |
                  | (Video generator)    |
                  +----------------------+
                            |
                            v
                    +---------------+
                    |   Story Player|
                    +---------------+
```

### GPT-2

![gpt-2](/docs/imgs/gpt-2.png)

### Suno-bark

![gpt-2](/docs/imgs/suno-bark.png)

### Stable-diffusion

![gpt-2](/docs/imgs/stable-diffusion.png)