# Greycraft News Automation System  
灰匠新聞自動化系統

---

## 📘 繁體中文說明

**Greycraft News Automation System** 是由 **Greycraft Automation（灰匠自動化）** 開發的  
「Yahoo 奇摩新聞自動化擷取與報表工具」。

主要功能：

- 每次執行時，自動連線到 Yahoo 奇摩新聞（台灣）首頁  
- 擷取最新新聞標題與連結  
- 輸出為帶有時間戳記檔名的 CSV 檔案  
- 可選擇搭配 `email_reporter.py`，透過 Gmail SMTP 自動寄送最新報表

適合對象：

- 想每天快速掌握新聞重點的老闆、主管  
- 需要將新聞做成資料、再進一步分析的分析師／研究人員  
- 每天要整理新聞、貼連結給主管的行政人員或小編

專案檔案簡介：

- `yahoo_news_titles.py`：主程式，負責連線 Yahoo 新聞並產生 CSV 報表  
- `email_reporter.py`：自動尋找最新 CSV，並透過 Gmail SMTP 寄出 Email  
- `project_yahoo_news.md`：中文專案說明與商業應用情境文件  

執行方式（簡要）：

1. 安裝套件：`pip install requests beautifulsoup4 pandas`  
2. 產生 CSV 報表：`python yahoo_news_titles.py`  
3. （選用）設定 `email_reporter.py` 內的 Gmail 帳號與 App Password，然後執行：  
   `python email_reporter.py` 便可寄出最新報表

如需針對自家產業客製化新聞情資 / 自動化系統，歡迎聯絡：

- Email：`jasonaiflow.dev@gmail.com`  
- LINE 官方帳號：灰匠自動化 Greycraft（ID：`@177yaqsm`）  
- GitHub：<https://github.com/greycraft-automation>

---

## 📗 English Version

### Overview

**Greycraft News Automation System** is an enterprise-grade  
news & intelligence automation tool,  
built with Python for daily Yahoo News collection, CSV export, and email reporting.  

Created by **Greycraft Automation（灰匠自動化）**.

---

## What this project does

This tool automatically:

1. Connects to the Yahoo News (Taiwan) homepage  
2. Extracts the latest headlines and links  
3. Stores them in a structured, timestamped CSV file  
4. (Optional) Sends the latest report to a specified inbox via Gmail SMTP

Designed for:

- Founders and executives who need a quick daily news snapshot  
- Analysts who need structured news data for further processing  
- Teams who want to reduce repetitive copy–paste work  

---

## Tech stack

- Python 3  
- `requests` – HTTP requests  
- `beautifulsoup4` – HTML parsing  
- `pandas` – data structuring & CSV export  
- `smtplib` – Gmail SMTP email sending (Python standard library)  

---

## Files

- `yahoo_news_titles.py`  
  Core scraper that fetches Yahoo News Taiwan headlines and URLs,  
  then exports a timestamped CSV file.

- `email_reporter.py`  
  Utility script that finds the latest CSV report and sends it via Gmail SMTP.

- `project_yahoo_news.md`  
  Chinese project description & business use case documentation.

---

## How to run

### 1. Install dependencies

```bash
pip install requests beautifulsoup4 pandas
```
### 2. Run the scraper (generate CSV)

```bash
python yahoo_news_titles.py
```
This will:    
- Connect to Yahoo News (Taiwan) homepage  
- Collect the latest headlines and URLs  
- Save them into a timestamped CSV file  
  
Example filename：
```text
yahoo_news_pro_20251118_090000.csv
```

### 3. (Optional) Configure and run the email reporter
First, set your Gmail and app password inside `email_reporter.py`:  

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # e.g. Gmail App Password
RECEIVER_EMAIL = "target_inbox@example.com"
```
>🔐 Security note｜安全提醒：  
>- For Gmail, use an App Password instead of your main password.  
>- Do NOT commit real credentials into the repository.
>   
>  使用 Gmail 時建議設定「應用程式專用密碼」，不要直接填入主帳號密碼。  
>  請勿將真實帳密提交到版本控制或公開儲存庫。  

Then execute:  

```bash
python email_reporter.py
```

---

### About Greycraft Automation

Greycraft Automation（灰匠自動化） focuses on:  
- Python + AI automation tooling for businesses  
- Data collection, cleaning, and report automation  
- Designing reusable automation workflows for SMEs  

Contact  

- Email：jasonaiflow.dev@gmail.com
- LINE Official：灰匠自動化 Greycraft（ID：@177yaqsm）
- GitHub：https://github.com/greycraft-automation
