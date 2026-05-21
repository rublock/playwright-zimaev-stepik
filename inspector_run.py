from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://10.81.61.60')

    page.wait_for_selector('x-pw-glass', timeout=10000)
    page.evaluate("""
        const intervalId = setInterval(() => {
            const glass = document.querySelector('x-pw-glass');
            if (glass) {
                glass.style.visibility = 'hidden';
            }
        }, 100);
        """)

    # TODO: сделать так чтобы появлялся инспектор
    page.pause()

    input("Нажми Enter, чтобы закрыть браузер...")
    browser.close()
