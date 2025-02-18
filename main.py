from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# استبدل هذا بالتوكن الخاص بك
TOKEN = "7975728007:AAGyHSOIr42qOA6BmXj_EQF30fX2jQpP0dA"

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# قائمة الأوامر
commands = {
    "games": "🎮 ألعاب ممتعة",
    "anime_info": "🏮 معلومات عن أنمي",
    "download": "📥 تحميل من مواقع التواصل",
    "convert": "🎨 تحويل صورة/فيديو",
    "marriage": "💍 زواج عشوائي",
    "admin": "⚡ أوامر المشرفين",
    "owner": "🔥 أوامر المالك فقط"
}

# صورة ميليوداس (يجب استضافتها على الإنترنت أو رفعها يدوياً)
meliodas_image_url = "https://i.imgur.com/MeliodasImage.jpg"

def start(update: Update, context: CallbackContext):
    message = "👑 أهلاً بك، أنا *عبد ميليوداس*! البوت الخاص بنقابة فلود.\n"
    message += "استخدم /القائمة لرؤية قائمة الأوامر المتاحة."
    update.message.reply_photo(photo=meliodas_image_url, caption=message, parse_mode="Markdown")

def commands_list(update: Update, context: CallbackContext):
    message = "📜 *قائمة الأوامر الخاصة بـ عبد ميليوداس:*\n\n"
    for cmd, desc in commands.items():
        message += f"✅ `/{cmd}` - {desc}\n"
    
    update.message.reply_photo(photo=meliodas_image_url, caption=message, parse_mode="Markdown")

# إضافة الأوامر إلى البوت
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("commands", commands_list))

# بدء تشغيل البوت
updater.start_polling()
updater.idle()
