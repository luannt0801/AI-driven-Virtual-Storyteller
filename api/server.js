const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

app.post('/api/generate-story', (req, res) => {
  const { prompt } = req.body;

  const storyText = `Đây là câu chuyện về: ${prompt}\n\nMột ngày nọ, ${prompt} bắt đầu chuyến phiêu lưu kỳ thú...`;

  const imageUrl = `https://source.unsplash.com/800x400/?${encodeURIComponent(prompt)}`;

  const audioUrl = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3';

  const videoUrl = 'https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4';

  res.json({
    story_text: storyText,
    image_url: imageUrl,
    audio_url: audioUrl,
    video_url: videoUrl
  });
});

app.listen(port, () => {
  console.log(`Mock API running at http://localhost:${port}`);
});
