import time

def upload_to_tiktok(video_path, title_text):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.tiktok.com/upload?lang=en")

        print("⚠️ Please log in manually (if not already). Then press ENTER")
        input()

        page.locator('input[type="file"]').set_input_files(video_path)
        time.sleep(10)

        page.locator('[data-e2e="upload-caption"]').fill(title_text)
        page.locator('[data-e2e="publish-button"]').click()
        time.sleep(5)
        browser.close()
