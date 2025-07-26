from playwright.sync_api import sync_playwright
from topic_generator import generate_topics
from video_generator import generate_simple_video
from did_video_generator import create_did_video
from tiktok_uploader import upload_to_tiktok
from get_username import get_tiktok_username

BATCH_SIZE = 5  # Set between 5-50
LANG = "en"     # 'en', 'ur', 'hi'
USE_AI_FACE = False  # Set True to use D-ID AI face videos

def run_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Open TikTok upload page and login manually.")
        page.goto("https://www.tiktok.com/upload?lang=en")
        input("Press Enter after login is complete...")

        username = get_tiktok_username(page)
        print(f"Using TikTok account: @{username}")

        topics = generate_topics(BATCH_SIZE, language=LANG)

        for i, topic in enumerate(topics):
            filename = f"video_{i+1}.mp4"
            print(f"Generating video [{i+1}] for topic: {topic}")
            if USE_AI_FACE:
                create_did_video(topic, filename)
            else:
                generate_simple_video(topic, filename, username)

            print(f"Uploading {filename}...")
            upload_to_tiktok(filename, topic)

        browser.close()

if __name__ == "__main__":
    run_bot()
