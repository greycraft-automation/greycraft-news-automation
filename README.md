# Greycraft News Automation System

Enterprise-grade news & intelligence automation tool,  
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

### 3. (Optional) Configure and run the email reporter
First, set your Gmail and app password inside email_reporter.py:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # e.g. Gmail App Password
RECEIVER_EMAIL = "target_inbox@example.com"
```
Then execute:

```bash
python email_reporter.py
```
---

### About Greycraft Automation

Greycraft Automation（灰匠自動化）專注於：
- Python + AI 自動化工具開發
- 資料蒐集、整理與報表自動化
- 幫中小企業減少重複性人工操作，建立可複用的自動化流程

Contact:

- Email：jasonaiflow.dev@gmail.com  
- LINE Official：灰匠自動化 Greycraft（ID：@177yaqsm）
