import smtplib
from email.mime.text import MIMEText
from utils import get_env

def send_email(subject, body_html, to_email):

    email = get_env("GMAIL_EMAIL")
    app_password = get_env("GMAIL_APP_PASSWORD")

    msg = MIMEText(body_html, "html")
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, app_password)
        server.sendmail(email, to_email, msg.as_string())

    print("Email sent successfully!")

def render_newsletter_html(articles, date_str, template="templates/newsletter_template.html"):
    from jinja2 import Template
    with open(template, "r", encoding="utf-8") as f:
        tpl = Template(f.read())
    return tpl.render(articles=articles, date=date_str)
