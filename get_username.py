def get_tiktok_username(page):
    try:
        profile_btn = page.locator('[data-e2e="nav-profile-avatar"]')
        profile_btn.click()
        page.wait_for_timeout(3000)
        
        username_element = page.locator('a[href*="/@"]')
        username_url = username_element.get_attribute("href")
        if username_url and "/@" in username_url:
            return username_url.split("/@")[1]
    except:
        pass
    return "unknown_user"
