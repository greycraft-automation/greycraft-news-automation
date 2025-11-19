import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
import glob

# =====================================================
# Gmail Report Sender - Enterprise Utility
# Author: Jason (Automation Workflow Architect)
#
# 功能說明：
#   - 自動尋找資料夾中最新的 yahoo_news_pro_*.csv
#   - 以 Gmail 寄出報表（先寄給自己）
#   - 採企業級 Log 風格，方便日後整合排程與監控
# =====================================================

# === 基本設定（依照你自己的需求修改） ===
GMAIL_ADDRESS = "your_email"   # 你的真實信箱
RECIPIENTS = [
    "target_inbox@example.com",
    # 未來可以在這裡加上老闆或客戶的 Email
]

# ⚠️ 這裡要填上你剛剛建立的「應用程式密碼」
#    看起來會像：abcd efgh ijkl mnop（貼進來時可以不留空格）
APP_PASSWORD = "your_app_password" # 你的密碼


def find_latest_report(pattern: str = "yahoo_news_pro_*.csv") -> str:
    """
    尋找目前資料夾中最新的 CSV 報表檔案。
    若找不到則回傳空字串。
    """
    files = glob.glob(pattern)
    if not files:
        return ""
    latest_file = max(files, key=os.path.getmtime)
    return latest_file


def build_email(subject: str, body: str, attachment_path: str) -> EmailMessage:
    """
    建立含附件的 Email 物件。
    """
    msg = EmailMessage()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject
    msg.set_content(body)

    # 加入附件
    with open(attachment_path, "rb") as f:
        file_data = f.read()
        filename = os.path.basename(attachment_path)

    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="csv",
        filename=filename,
    )

    return msg


def send_email(msg: EmailMessage):
    """
    使用 Gmail SMTP 寄出 Email。
    """
    print("[INFO] Connecting to Gmail SMTP...")
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(GMAIL_ADDRESS, APP_PASSWORD)
        smtp.send_message(msg)
    print("[INFO] Email sent successfully.")


def main():
    print("====================================================")
    print(" Gmail Automated Report Sender - Enterprise Utility")
    print("====================================================\n")

    # 1. 找最新報表檔案
    latest_report = find_latest_report()

    if not latest_report:
        print("[ERROR] No report file found (yahoo_news_pro_*.csv).")
        print("        Please run the scraper first to generate a report.")
        return

    print(f"[INFO] Latest report detected: {latest_report}")

    # 2. 建立主旨與內文
    today_str = datetime.now().strftime("%Y-%m-%d")
    subject = f"Daily Yahoo News Report - {today_str}"
    body = (
        "這是一封由自動化系統寄出的每日 Yahoo 新聞報表。\n\n"
        "說明：\n"
        " - 附件為最新產出的 yahoo_news_pro_*.csv\n"
        " - 可用於市場情資、新聞監控、決策支援\n\n"
        "Jason 自動化流程系統\n"
    )

    # 3. 建立 Email 物件
    msg = build_email(subject, body, latest_report)

    # 4. 寄出
    try:
        send_email(msg)
        print("[INFO] Process completed.")
    except Exception as e:
        print(f"[FATAL] Failed to send email: {e}")


if __name__ == "__main__":
    main()