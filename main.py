import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# الحصول على التوكن من المتغيرات البيئية
TOKEN = os.getenv("TOKEN")

# تهيئة نظام تسجيل الأخطاء
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# دالة بدء التشغيل
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👑 أهلاً بك، أنا عبد ميليوداس! استخدم /القائمة لرؤية الأوامر المتاحة.")

# دالة عرض قائمة الأوامر
async def commands(update: Update, context: CallbackContext):
    commands_list = """
    ✅ /games - 🎮 ألعاب ممتعة
    ✅ /anime_info - 🏮 معلومات عن أنمي
    ✅ /download - 📥 تحميل من مواقع التواصل
    ✅ /convert - 🎨 تحويل صورة/فيديو
    ✅ /marriage - 💍 زواج عشوائي
    ✅ /admin - ⚡ أوامر المشرفين
    ✅ /owner - 🔥 أوامر المالك فقط
    """
    await update.message.reply_text(commands_list)

# إنشاء التطبيق وإضافة الأوامر
def main():
    print(f"Using Token: {TOKEN}")  
    app = Application.builder().token(TOKEN.strip()).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("commands", commands))

    # تشغيل البوت
    logger.info("✅ البوت يعمل الآن!")
    app.run_polling()

if __name__ == "__main__":
    main()
