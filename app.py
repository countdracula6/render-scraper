from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=chrome_options)

@app.route("/")
def home():
    return "<h1>Welcome to the Auto-Browse Scraper API</h1>"

@app.route("/scrape")
def scrape():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Missing ?url= parameter"}), 400
    
    driver = create_driver()
    driver.get(url)
    title = driver.title
    driver.quit()

    return jsonify({
        "url": url,
        "title": title
    })

@app.route("/browse")
def browse():
    # Example: simulate going through 3 pages
    driver = create_driver()
    log = []

    urls = [
        "https://example.com",
        "https://httpbin.org/html",
        "https://golove.ai"
    ]

    for url in urls:
        driver.get(url)
        log.append({
            "url": url,
            "title": driver.title
        })

    driver.quit()
    return jsonify(log)