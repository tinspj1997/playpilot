import asyncio
from playwright.async_api import async_playwright

async def fetch_page_source(url: str, output_file: str = "page_source.txt") -> str:
    """
    Simplified fully-rendered HTML fetcher.
    Uses Playwright's native idle detection to handle JS frameworks.
    """
    async with async_playwright() as pw:
        # Launch browser
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        try:
            print(f"🌐 Navigating to: {url}")
            
            # 1. Navigate and wait for network to be idle (covers most API calls)
            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # 2. Ensure the 'load' event has fired
            await page.wait_for_load_state("load")

            # 3. Handle Lazy Loading: Scroll to the bottom of the page
            # This is the most reliable way to trigger lazy-loaded images/components
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # 4. Short settle time for animations/final rendering
            await page.wait_for_timeout(2000)

            # 5. Capture the rendered HTML
            html = await page.content()

            # 6. Save to file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html)

            print(f"✅ Success! Saved {len(html)} chars to {output_file}")
            return html

        except Exception as e:
            print(f"❌ Error: {e}")
            return ""
        finally:
            await browser.close()

if __name__ == "__main__":
    target = "https://studio4.gnie.ai:7062/"
    asyncio.run(fetch_page_source(target))