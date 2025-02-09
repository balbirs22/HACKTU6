import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load the emails and company names from CSV
csv_file = "src/emails.csv"  # Update path if needed
df = pd.read_csv(csv_file)

# Your email credentials
SENDER_EMAIL = "balbirs2204@gmail.com"  # Replace with your email
APP_PASSWORD = "ciqbyyrvvpjokwjv"     # Replace with the generated App Password

# SMTP setup
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(to_email, company_name):
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = f"Seeking Assistance for a Job Opportunity at {company_name}"

        # Email body (personalized)
        body = f"""
        Hi,

        I hope you're doing well! I'm very interested in opportunities at {company_name}, and I came across your contact information while researching the company. 

        I would really appreciate any guidance or insights you can provide about working at {company_name}. If you could share any job openings, referral opportunities, or general advice, it would mean a lot to me.

        Looking forward to hearing from you.

        Best regards,  
        Pave Guardians.
        """

        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure connection
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {to_email} for {company_name}")

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}. Error: {e}")

# Loop through each email and send personalized emails
for index, row in df.iterrows():
    email = row["Email"]
    company = row["Company"]
    send_email(email, company)
