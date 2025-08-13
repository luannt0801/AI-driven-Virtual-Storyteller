
<!-- 
echo "# -AI-driven-Virtual-Storyteller" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/luannt0801/-AI-driven-Virtual-Storyteller.git
git push -u origin main -->


# Project Title: AI-driven Virtual Storyteller | Code: 242B1MDCP01 
Generate narrated stories with matching visuals and background music.

---

Requirements
- NLP module for story scripts 
- Text-to-speech with emotion 
- Visual scene generator (GANs or procedural) 
- API for story/visual input
Expected 
- End-to-end storytelling player 
- API for content creation 
- Demo stories


```
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

---

aidriven-storyteller/
├── frontend/               # UI React (Next.js + Tailwind + shadcn/ui)
│   ├── app/                # App Router (nếu dùng Next.js 13+)
│   │   ├── page.tsx        # Trang chính chứa UI
│   │   ├── globals.css     # CSS chung
│   │   └── layout.tsx      # Layout app
│   ├── components/         # Các component UI tách riêng
│   │   ├── StoryConfig.tsx # Form nhập prompt & config
│   │   ├── StepProgress.tsx# Hiển thị tiến trình từng bước
│   │   └── OutputPanel.tsx # Khu vực Story, Audio, Video
│   ├── lib/                # Hàm tiện ích frontend
│   │   ├── api.ts          # Gọi API tới backend
│   │   └── types.ts        # Khai báo TypeScript type chung
│   ├── public/             # Ảnh/logo tĩnh
│   ├── package.json
│   └── ...
│
└── backend/                # Server chạy mô hình AI + API
    ├── app/
    │   ├── __init__.py
    │   ├── main.py         # FastAPI entrypoint
    │   ├── routes/         # Tách route API theo nhóm
    │   │   ├── gpt2.py     # Route tạo story từ GPT-2
    │   │   ├── bark.py     # Route TTS với suno/bark-small
    │   │   ├── sd.py       # Route Stable Diffusion v1-5
    │   │   └── assemble.py # Route ghép audio + video
    │   ├── services/       # Logic gọi model, xử lý dữ liệu
    │   │   ├── gpt2_service.py
    │   │   ├── bark_service.py
    │   │   ├── sd_service.py
    │   │   └── assemble_service.py
    │   ├── workers/        # Nếu có background job queue
    │   │   ├── worker.py
    │   │   └── tasks.py
    │   ├── utils/          # Hàm tiện ích backend (ffmpeg, đọc/ghi file)
    │   │   ├── ffmpeg_utils.py
    │   │   └── file_utils.py
    │   ├── models/         # (tuỳ) Dataclass / Pydantic models
    │   └── config.py       # Cấu hình app (path model, key API,...)
    ├── requirements.txt    # Python dependencies
    └── README.md
