from telegram.ext import Updater, MessageHandler, Filters
import smtplib
from email.message import EmailMessage
import os

def voye_imel_admin(username, mesaj):
    msg = EmailMessage()
    msg.set_content(f"""
📬 ALÈT: Gen yon itilizatè sou bot la ki bezwen ou!

👤 Telegram Username: @{username}
📝 Mesaj li ekri:
{mesaj}
""")

    msg['Subject'] = '🚨 URGENCE - Itilizatè bezwen èd sou bot Crypto2MonCash'
    msg['From'] = "crypto2moncashbot@gmail.com"
    msg['To'] = "tondreaulordhands@gmail.com"

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "crypto2moncashbot@gmail.com"
    smtp_password = os.getenv("MODPAS_APLIKASYON")

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

def reponn_otomatik(update, context):
    user = update.message.from_user
    mesaj = update.message.text

    voye_imel_admin(user.username, mesaj)

    update.message.reply_text(
        "👋 Bonjou!\n\n🙏 Mèsi dèske w kontakte nou. Admin lan pa anliy kounye a pou kounye a.\n\n📌 Pa enkyete w — nou fenk voye yon alèt bay administratè prensipal la pou l vin ede w vit vit!\n\n📲 Ou ka tou kontakte li dirèkteman sou Telegram: @CryptomoncashAdmin\n\n⏳ Tanpri rete konekte. N ap reponn ou dèke nou tounen anliy.\n\n💎 Mèsi pou pasyans ou ak konfyans ou."
    )

if __name__ == "__main__":
    token = os.getenv("TOKEN_BOT_OU")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reponn_otomatik))
    updater.start_polling()
    updater.idle()
