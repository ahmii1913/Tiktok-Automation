# ✨ **_TikTok Auto Upload Bot_** ✨

Automate TikTok video creation and upload with AI-generated titles, hashtags, mentions, and optional AI face videos.

---

## 🚀 **Features**

- 🔥 Batch upload **5–50 videos** per run  
- ⚽ Smart trending football topic generator (**English / Urdu / Hindi**)  
- 📝 Auto title, hashtags, and mentions generation  
- 💧 Dynamic TikTok username **watermark** on videos  
- 🤖 Optional AI face video generation via **D-ID API**  
- 🤹‍♂️ Upload automation using **Playwright**  
- 🖥️ User-friendly **GUI app** for easy use  
- 💻 Windows `.exe` support with **PyInstaller**  
- 📊 Upload logs and retry mechanism  
- ⏰ Scheduling support (manual)

---

## 🛠️ **Setup Instructions**

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/tiktok-auto-bot.git
   cd tiktok-auto-bot
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

3. **Add your D-ID API key** (optional) in `did_video_generator.py`

4. **Run the CLI bot:**

   ```bash
   python main.py
   ```

5. **Or launch the GUI app:**

   ```bash
   python gui_app.py
   ```

---

## ⚠️ **Notes**

- You **must log in manually** to TikTok once in the browser window that opens.  
- The bot will detect your logged-in **TikTok username** and add it as a watermark automatically.  
- Adjust **batch size** and **language settings** inside `main.py` or via GUI controls.  
- To build a Windows executable, use **PyInstaller**:

  ```bash
  pyinstaller --onefile --noconsole main.py
  ```

---

## 📜 **License**

This project is licensed under the **MIT License** — feel free to use and customize it!  

---

Made with ❤️ by **@yourusername**

---

💬 **Questions or feedback?** Open an issue or contact me directly!
