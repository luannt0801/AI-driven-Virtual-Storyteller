// // const express = require('express');
// // const cors = require('cors');
// // const fs = require('fs');
// // const path = require('path');
// // const { spawn } = require('child_process');
// // const app = express();
// // const port = 3000;

// // app.use(cors());
// // app.use(express.json());

// // app.post('/api/generate-story', (req, res) => {
// //   req.setTimeout(0);
// //   const { prompt } = req.body;

// //   // Đường dẫn python interpreter và main.py
// //   const pythonExe = 'D:\\2025\\Master BKHN\\Ky thuat lap trinh noi dung so\\AI-driven-Virtual-Storyteller\\luan\\Scripts\\python.exe';
// //   const mainPy = 'main.py';
// //   const rootPath = 'D:/2025/Master BKHN/Ky thuat lap trinh noi dung so/AI-driven-Virtual-Storyteller/models';

// //   // Tham số như trong run.bat
// //   const args = [
// //     mainPy,
// //     '--prompt', prompt,
// //     '--gpt_model_path', `${rootPath}/gpt2`,
// //     '--sd_model_path', `${rootPath}/stable-diffusion-v1-5`,
// //     '--sd_model_id', 'runwayml/stable-diffusion-v1-5',
// //     '--bark_model_path', `${rootPath}/suno_bark_small`,
// //     '--voice_preset', 'v2/en_speaker_6',
// //     '--split_mode', 'sentence',
// //     '--max_images', '8',
// //     '--output_dir', 'outputs',
// //     '--video_name', 'story_video.mp4'
// //   ];

// //   const py = spawn(pythonExe, args, { cwd: '..' }); // cwd: '..' để chạy ở thư mục cha (nơi có main.py)

// //   py.stdout.on('data', (data) => {
// //     console.log(`stdout: ${data}`);
// //   });
// //   py.stderr.on('data', (data) => {
// //     console.error(`stderr: ${data}`);
// //   });

// //   py.on('close', (code) => {
// //     if (code !== 0) {
// //       return res.status(500).json({ error: 'Python script failed' });
// //     }
// //     try {
// //       const storyText = fs.readFileSync('../outputs/story.txt', 'utf8');
// //       res.json({
// //         story_text: storyText,
// //         video_url: 'outputs/story_video.mp4',
// //         audio_url: 'outputs/narration.wav'
// //         // Thêm image_url nếu cần
// //       });
// //     } catch (err) {
// //       res.status(500).json({ error: 'Failed to read output files' });
// //     }
// //   });
// // });

// // //   py.stdout.on('data', (data) => {
// // //     console.log(`stdout: ${data}`);
// // //   });
// // //   py.stderr.on('data', (data) => {
// // //     console.error(`stderr: ${data}`);
// // //   });

// // //   py.on('close', (code) => {
// // //     if (code !== 0) {
// // //       return res.status(500).json({ error: 'Python script failed. Check server logs for details.' });
// // //     }
// // //     try {
// // //       const storyPath = path.join(__dirname, '..', 'outputs', 'story.txt');
// // //       const storyText = fs.readFileSync(storyPath, 'utf8');

// // //       // Đường dẫn video và audio
// // //       const videoPath = path.join(__dirname, '..', 'outputs', 'story_video.mp4');
// // //       const audioPath = path.join(__dirname, '..', 'outputs', 'narration.wav');

// // //       // Kiểm tra file tồn tại
// // //       const videoUrl = fs.existsSync(videoPath) ? '/outputs/story_video.mp4' : null;
// // //       const audioUrl = fs.existsSync(audioPath) ? '/outputs/narration.wav' : null;

// // //       res.json({
// // //         story_text: storyText,
// // //         video_url: videoUrl,
// // //         audio_url: audioUrl
// // //       });
// // //     } catch (err) {
// // //       console.error("Read output error:", err);
// // //       res.status(500).json({ error: 'Failed to read output files.' });
// // //     }
// // //   });
// // // });

// // app.listen(port, () => {
// //   console.log(`API running at http://localhost:${port}`);
// // });


// // try 1


// const express = require('express');
// const cors = require('cors');
// const fs = require('fs');
// const path = require('path');
// const { spawn } = require('child_process');
// const app = express();
// const port = 3000;

// app.use(cors());
// app.use(express.json());
// app.use('/outputs', express.static(path.join(__dirname, '..', 'outputs')));

// app.post('/api/generate-story', (req, res) => {
//   req.setTimeout(0);
//   const { prompt } = req.body;

//   const pythonExe = 'D:\\2025\\Master BKHN\\Ky thuat lap trinh noi dung so\\AI-driven-Virtual-Storyteller\\luan\\Scripts\\python.exe';
//   const mainPy = 'main.py';
//   const rootPath = 'D:/2025/Master BKHN/Ky thuat lap trinh noi dung so/AI-driven-Virtual-Storyteller/models';

//   const args = [
//     mainPy,
//     '--prompt', prompt,
//     '--gpt_model_path', `${rootPath}/gpt2`,
//     '--sd_model_path', `${rootPath}/stable-diffusion-v1-5`,
//     '--sd_model_id', 'runwayml/stable-diffusion-v1-5',
//     '--bark_model_path', `${rootPath}/suno_bark_small`,
//     '--voice_preset', 'v2/en_speaker_6',
//     '--split_mode', 'sentence',
//     '--max_images', '8',
//     '--output_dir', 'outputs',
//     '--video_name', 'story_video.mp4'
//   ];

//   const py = spawn(pythonExe, args, { cwd: '..' });

//   py.stdout.on('data', (data) => {
//     console.log(`stdout: ${data}`);
//   });
//   py.stderr.on('data', (data) => {
//     console.error(`stderr: ${data}`);
//   });

//   py.on('close', (code) => {
//     if (code !== 0) {
//       return res.status(500).json({ error: 'Python script failed. Check server logs for details.' });
//     }
//     try {
//       const storyPath = path.join(__dirname, '..', 'outputs', 'story.txt');
//       const storyText = fs.readFileSync(storyPath, 'utf8');

//       const videoPath = path.join(__dirname, '..', 'outputs', 'story_video.mp4');
//       const audioPath = path.join(__dirname, '..', 'outputs', 'narration.wav');

//       // Kiểm tra file tồn tại
//       const videoUrl = fs.existsSync(videoPath) ? '/outputs/story_video.mp4' : null;
//       const audioUrl = fs.existsSync(audioPath) ? '/outputs/narration.wav' : null;

//       res.json({
//         story_text: storyText,
//         video_url: videoUrl,
//         audio_url: audioUrl // Trả về URL đầy đủ cho audio
//       });
//     } catch (err) {
//       console.error("Read output error:", err);
//       res.status(500).json({ error: 'Failed to read output files.' });
//     }
//   });
// });

// app.listen(port, () => {
//   console.log(`API running at http://localhost:${port}`);
// });


const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use('/outputs', express.static(path.join(__dirname, '..', 'outputs')));

app.post('/api/generate-story', (req, res) => {
  req.setTimeout(0);
  const { prompt } = req.body;

  const pythonExe = 'D:\\2025\\Master BKHN\\Ky thuat lap trinh noi dung so\\AI-driven-Virtual-Storyteller\\luan\\Scripts\\python.exe';
  const mainPy = 'main.py';
  const rootPath = 'D:/2025/Master BKHN/Ky thuat lap trinh noi dung so/AI-driven-Virtual-Storyteller/models';

  const args = [
    mainPy,
    '--prompt', prompt,
    '--gpt_model_path', `${rootPath}/gpt2`,
    '--sd_model_path', `${rootPath}/stable-diffusion-v1-5`,
    '--sd_model_id', 'runwayml/stable-diffusion-v1-5',
    '--bark_model_path', `${rootPath}/suno_bark_small`,
    '--voice_preset', 'v2/en_speaker_6',
    '--split_mode', 'sentence',
    '--max_images', '8',
    '--output_dir', 'outputs',
    '--video_name', 'story_video.mp4'
  ];

  const py = spawn(pythonExe, args, { cwd: '..' });

  py.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  py.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  py.on('close', (code) => {
    if (code !== 0) {
      return res.status(500).json({ error: 'Python script failed. Check server logs for details.' });
    }
    try {
      const storyPath = path.join(__dirname, '..', 'outputs', 'story.txt');
      const storyText = fs.readFileSync(storyPath, 'utf8');

      const videoPath = path.join(__dirname, '..', 'outputs', 'story_video.mp4');
      const audioPath = path.join(__dirname, '..', 'outputs', 'narration.wav');

      // Trả về URL đầy đủ cho video và audio
      const videoUrl = fs.existsSync(videoPath) ? `http://localhost:${port}/outputs/story_video.mp4` : null;
      const audioUrl = fs.existsSync(audioPath) ? `http://localhost:${port}/outputs/narration.wav` : null;

      res.json({
        story_text: storyText,
        video_url: videoUrl,
        audio_url: audioUrl
      });
    } catch (err) {
      console.error("Read output error:", err);
      res.status(500).json({ error: 'Failed to read output files.' });
    }
  });
});

app.listen(port, () => {
  console.log(`API running at http://localhost:${port}`);
});