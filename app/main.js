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