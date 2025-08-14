// const btn = document.getElementById("generateBtn");
// const storyOutput = document.getElementById("storyOutput");
// const visualBox = document.getElementById("visual");

// async function generateStory() {
//   const prompt = document.getElementById("prompt").value.trim();
//   if (!prompt) {
//     alert("Please enter story request!");
//     return;
//   }

//   btn.disabled = true;
//   btn.textContent = "Creating...";

//   await new Promise(r => setTimeout(r, 800)); 

//   const story = `
// Chuyện về: ${prompt}

// 1. Mở đầu – ${prompt} bắt đầu chuyến phiêu lưu.
// 2. Khám phá – Những bí ẩn dần hé lộ.
// 3. Cao trào – Một tình huống bất ngờ xảy ra.
// 4. Kết thúc – Hành trình khép lại, để lại nhiều suy ngẫm.

// (Kết thúc câu chuyện)
//   `.trim();

//   const imageUrl = `https://source.unsplash.com/800x400/?${encodeURIComponent(prompt)}`;

//   visualBox.innerHTML = `<img src="${imageUrl}" alt="Story Visual"/>`;

//   storyOutput.textContent = story;

//   // Đọc giọng kể bằng Web Speech API
//   try {
//     const utter = new SpeechSynthesisUtterance(story);
//     utter.lang = "vi-VN";
//     window.speechSynthesis.speak(utter);
//   } catch (e) {
//     console.error("Không đọc được giọng kể:", e);
//   }

//   btn.disabled = false;
//   btn.textContent = "Generate Story";
// }

// btn.addEventListener("click", generateStory);


const btn = document.getElementById("generateBtn");
const storyOutput = document.getElementById("storyOutput");
const visualBox = document.getElementById("visual");

async function generateStory() {
  const prompt = document.getElementById("prompt").value.trim();
  if (!prompt) {
    alert("Please enter story request!");
    return;
  }

  btn.disabled = true;
  btn.textContent = "Creating...";

  try {
    // Gọi API mock local
    const res = await fetch("http://localhost:3000/api/generate-story", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    if (!res.ok) throw new Error("API error: " + res.status);

    const data = await res.json();

    // Hiển thị video nếu có, nếu không thì ảnh
    if (data.video_url) {
      visualBox.innerHTML = `<video controls autoplay muted loop src="${data.video_url}"></video>`;
    } else if (data.image_url) {
      visualBox.innerHTML = `<img src="${data.image_url}" alt="Story Visual"/>`;
    }

    // Hiển thị câu chuyện
    storyOutput.textContent = data.story_text;

    // Phát audio nếu có
    if (data.audio_url) {
      const audio = new Audio(data.audio_url);
      audio.play();
    }

  } catch (err) {
    console.error(err);
    alert("Lỗi khi gọi API!");
  }

  btn.disabled = false;
  btn.textContent = "Generate Story";
}

btn.addEventListener("click", generateStory);
