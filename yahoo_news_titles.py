import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random

# =====================================================
# Yahoo News Automated Scraper - Enterprise Edition
# Author: Jason (Automation Workflow Architect)
#
# 中英混合註解：
# 這份程式展示企業級自動化架構：
# - Retry 機制
# - 清晰 Log
# - Yahoo 新版結構 fallback selector
# - 安全解析與版本化 CSV 輸出
# =====================================================


def fetch_page(url: str, retries: int = 3, delay: float = 2.0):
    """
    Fetch HTML with retry mechanism.
    具有重試機制，適合企業級自動排程環境。
    """
    for attempt in range(1, retries + 1):
        try:
            print(f"[INFO] Attempt {attempt}/{retries} - Connecting: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text

        except Exception as e:
            print(f"[WARN] Request failed: {e}")
            time.sleep(delay + random.random())

    raise Exception("[ERROR] All retry attempts failed. Terminating process.")


def parse_news(html: str):
    """
    Parse Yahoo News homepage.
    為因應 Yahoo 頻繁改版，採用多組 fallback selector。
    """

    soup = BeautifulSoup(html, "html.parser")

    selectors = [
        "h3 a",                # 新版 Yahoo 首選
        ".js-content-viewer a",  # 舊版 fallback
        ".mega-item a"          # 區塊型 fallback
    ]

    results = []

    for selector in selectors:
        items = soup.select(selector)
        if items:
            for n in items:
                title = n.get_text(strip=True)
                link = n.get("href")

                # 需要排除廣告或空值
                if not title or not link:
                    continue

                # 若連結不是完整URL，自動補齊
                if link.startswith("/"):
                    link = "https://tw.news.yahoo.com" + link

                results.append({"title": title, "url": link})

            # 已抓到資料，不用再試其他 selector
            if results:
                return results

    return results


def save_to_csv(data: list):
    """
    Save scraped data into a timestamped CSV.
    企業級自動化慣例：輸出具有版本化的時間戳文件。
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"yahoo_news_pro_{timestamp}.csv"

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig")

    print(f"[INFO] Output file generated: {filename}")
    return filename


def preview(data: list, n: int = 10):
    """
    Preview first N items.
    用於快速驗證爬蟲是否正常。
    """
    print("\n[PREVIEW] Top Headlines:")
    for i, item in enumerate(data[:n], 1):
        print(f"{i:02d}. {item['title']} ({item['url']})")
    print()


def main():
    url = "https://tw.news.yahoo.com/"

    print("====================================================")
    print(" Yahoo News Automation System - Enterprise Edition")
    print("====================================================\n")

    try:
        html = fetch_page(url)
        news = parse_news(html)

        if not news:
            print("[ERROR] No news extracted. Yahoo may have changed layout.")
            return

        print(f"[INFO] Total items extracted: {len(news)}")
        preview(news)

        output_file = save_to_csv(news)

        print("[INFO] Process completed successfully.")
        print("[INFO] This module can be attached to:")
        print("       - Daily automated reporting")
        print("       - Market intelligence monitoring")
        print("       - Enterprise dashboard pipelines\n")

    except Exception as e:
        print(f"\n[FATAL] Unhandled exception: {e}\n")


if __name__ == "__main__":
    main()
