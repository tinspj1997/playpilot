from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://app.bookeep.space/")
    page.wait_for_load_state("networkidle")

    # Click GitHub and wait for navigation
    with page.expect_navigation():
        page.get_by_role("button", name="GitHub").click()

    # Now you're on GitHub page
    print("Title:", page.title())
    print("URL:", page.url)

    # keep open for inspection
    page.wait_for_timeout(10000)

    browser.close()