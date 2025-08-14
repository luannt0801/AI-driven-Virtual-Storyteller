// // const btn = document.getElementById("generateBtn");
// // const storyOutput = document.getElementById("storyOutput");
// // const visualBox = document.getElementById("visual");

// // async function generateStory() {
// //   const prompt = document.getElementById("prompt").value.trim();
// //   if (!prompt) {
// //     alert("Please enter story request!");
// //     return;
// //   }

// //   btn.disabled = true;
// //   btn.textContent = "Creating...";

// //   try {
// //     // Gọi API mock local
// //     const res = await fetch("http://localhost:3000/api/generate-story", {
// //       method: "POST",
// //       headers: { "Content-Type": "application/json" },
// //       body: JSON.stringify({ prompt })
// //     });

// //     if (!res.ok) throw new Error("API error: " + res.status);

// //     const data = await res.json();

// //     // Hiển thị video nếu có, nếu không thì ảnh
// //     if (data.video_url) {
// //       visualBox.innerHTML = `<video controls autoplay muted loop src="${data.video_url}"></video>`;
// //     } else if (data.image_url) {
// //       visualBox.innerHTML = `<img src="${data.image_url}" alt="Story Visual"/>`;
// //     }

// //     // Hiển thị câu chuyện
// //     storyOutput.textContent = data.story_text;

// //     // Phát audio nếu có
// //     if (data.audio_url) {
// //       const audio = new Audio(data.audio_url);
// //       audio.play();
// //     }

// //   } catch (err) {
// //     console.error(err);
// //     alert("Lỗi khi gọi API!");
// //   }

// //   btn.disabled = false;
// //   btn.textContent = "Generate Story";
// // }

// // btn.addEventListener("click", generateStory);


// const btn = document.getElementById("generateBtn");
// const storyOutput = document.getElementById("storyOutput");
// const visualBox = document.getElementById("visual");

// let currentAudio = null; // Quản lý audio hiện tại

// async function generateStory() {
//   const prompt = document.getElementById("prompt").value.trim();
//   if (!prompt) {
//     alert("Please enter story request!");
//     return;
//   }

//   btn.disabled = true;
//   btn.textContent = "Creating...";
//   storyOutput.textContent = "";
//   visualBox.innerHTML = "";

//   // Dừng audio cũ nếu có
//   if (currentAudio) {
//     currentAudio.pause();
//     currentAudio.currentTime = 0;
//     currentAudio = null;
//   }

//   try {
//     // Gọi API mock local
//     const res = await fetch("http://localhost:3000/api/generate-story", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ prompt })
//     });

//     if (!res.ok) throw new Error("API error: " + res.status);

//     const data = await res.json();

//     // Hiển thị video nếu có
//     if (data.video_url) {
//       visualBox.innerHTML = `
//         <video id="storyVideo" controls autoplay muted loop style="max-width:100%;border-radius:10px;">
//           <source src="${data.video_url}" type="video/mp4">
//           Trình duyệt của bạn không hỗ trợ video.
//         </video>
//       `;
//     } else if (data.image_url) {
//       visualBox.innerHTML = `<img src="${data.image_url}" alt="Story Visual" style="max-width:100%;border-radius:10px;"/>`;
//     } else {
//       visualBox.innerHTML = "";
//     }

//     // Hiển thị câu chuyện
//     storyOutput.textContent = data.story_text || "";

//     // Phát audio nếu có
//     if (data.audio_url) {
//       currentAudio = new Audio(data.audio_url);
//       // Đảm bảo audio phát không bị trùng lặp
//       currentAudio.play().catch(() => {
//         // Nếu trình duyệt chặn tự động phát
//       });
//     }

//   } catch (err) {
//     console.error(err);
//     alert("Lỗi khi gọi API!");
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
    const res = await fetch("http://localhost:3000/api/generate-story", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    if (!res.ok) throw new Error("API error: " + res.status);

    const data = await res.json();
    console.log("API Response:", data);

    // Hiển thị video nếu có
    if (data.video_url) {
      visualBox.innerHTML = `<video controls autoplay muted loop src="${data.video_url}" style="width: 100%;"></video>`;
    } else {
      visualBox.innerHTML = `<p>No video available.</p>`;
    }

    // Hiển thị câu chuyện
    storyOutput.textContent = data.story_text || "No story generated.";

    // Phát audio nếu có
    if (data.audio_url) {
      const audio = new Audio(data.audio_url);
      audio.play();
    }

  } catch (err) {
    console.error(err);
    alert("Lỗi khi gọi API: " + err.message);
  }

  btn.disabled = false;
  btn.textContent = "Generate Story";
}

btn.addEventListener("click", generateStory);