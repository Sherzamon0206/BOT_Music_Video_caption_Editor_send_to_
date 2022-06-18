from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from django.conf import settings
from  telegram import Bot
import time

from telegram.ext import Updater
from bot.models import *
class Command(BaseCommand):
    help='Bu django telegram bot'

    def handle(self,*args,**options):
        request=Request(
        )
        bot=Bot(
            request=request,
            token=settings.TOKEN,


        )

        print(bot.get_me())





from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

#
#
# a=str(input("yangi token kiritishni xoxlaysizmi y/n :  "))
# a=a.lower()
# if a=="y" or a=="yes":
#     TOKEN=str(input("Tokenni kiriting: "))
# elif a=="n" or a=="no":
#     TOKEN=settings.Token
# else:
#     TOKEN=settings.Token
#
button=ReplyKeyboardMarkup([["Qayta ishga tushirish"]], resize_keyboard=True)



updater = Updater(settings.TOKEN)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		f"""Assalomu aleykum  {update.effective_user.last_name}\n\n sizning id {update.effective_user.id}"""

	)
	id = update.effective_user.id
	f_name = update.effective_user.first_name
	l_name = update.effective_user.last_name
	username = update.effective_user.username

	try:
		profile = Profile.objects.get(exeterenal_id=id)
		profile.f_name = f_name
		profile.username = username
		profile.l_name = l_name
		profile.save()
	except:

		user, created = Profile.objects.get_or_create(exeterenal_id=id, username=username, f_name=f_name, l_name=l_name)
		update.message.reply_text(f"your ID:  {update._effective_user.id}\ncurrent chat ID:  {update.message.chat_id}",
							  reply_markup=button)


	time.sleep(1)

	return 'bot'
def voice(update: Update, context: CallbackContext):
	id = update.effective_user.id
	try:
		context.bot.send_voice(chat_id=-1001692468825,voice=update.message.voice,caption="""\n🔴🔈@music_online_2022💯\nlink -> https://t.me/music_online_2022""")
		time.sleep(1)
		return 'bot'
	except:
		context.bot.send_message(chat_id=-1001692468825, text="""
			🔴🔈@music_online_2022 🎥
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
		🖤 
		🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

		  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
		🖤
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
		 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
		       link->https://t.me/music_online_2022
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•""")

		time.sleep(1)
		return  'bot'
def music(update: Update, context: CallbackContext):
	id = update.effective_user.id
	try:
		context.bot.send_audio(chat_id=-1001692468825,audio=update.message.audio,caption="""🔴🔈@music_online_2022💯\n
🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
\n🔴yuqori sifatda💯🔈\nlink -> https://t.me/music_online_2022""")
		time.sleep(1)
		return 'bot'
	except:
		context.bot.send_message(chat_id=-1001692468825, text="""
			🔴🔈@music_online_2022 🎥
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
		🖤 
		🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

		  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
		🖤
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
		 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
		       link->https://t.me/music_online_2022
		•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•""")
		time.sleep(1)
		return  'bot'


def video(update: Update, context: CallbackContext):
	try:
		context.bot.send_video(chat_id=-1001692468825, video=update.message.video,caption="""
	🔴🔈@music_online_2022 🎥
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
🖤  𝐁𝐈𝐙 𝐁𝐈𝐋𝐀𝐍 𝐁𝐈𝐑𝐆𝐀 𝐁𝐎𝐋𝐈𝐍🖤
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
       link->https://t.me/music_online_2022
•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•""")
		time.sleep(1)
		return 'bot'
	except:
		context.bot.send_message(chat_id=-1001692468825, text="""
					🔴🔈@music_online_2022 🎥
				•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
				🖤 
				🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

				  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
				🖤
				•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
				 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
				•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
				       link->https://t.me/music_online_2022
				•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•""")
		time.sleep(1)
		return  'bot'



def other2(update: Update, context: CallbackContext):
	text = """
		🔴🔈@music_online_2022 🎥
	•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
	🖤 
	🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

	  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
	🖤
	•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈• 
	 ☞𝐃𝐎𝐒𝐓𝐋𝐀𝐑𝐆𝐀 𝐔𝐋𝐀𝐒𝐇𝐈𝐍𝐆☜
	•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•
	       link->https://t.me/music_online_2022
	•┈┈┈•• ✦🕊💔 🍃✦••┈┈┈•"""
	context.bot.forward_message(chat_id=-1001692468825,from_chat_id=update.effective_user.id,message_id=update.message.message_id)
	context.bot.send_message(chat_id=-1001692468825,text=text)

	time.sleep(1)

	return 'bot'
def other(update: Update, context: CallbackContext):
	context.bot.send_message(chat_id=-1001692468825,text="""
	🔴🔈@music_online_2022 🎥
🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █
  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻
link->https://t.me/music_online_2022""")
	time.sleep(1)

	return 'bot'

def users(update:Update,context:CallbackContext):
    count=Profile.objects.all().count()
    update.message.reply_text(f"foydalanuvchilar soni : {count}",reply_markup=button)


    return 'bot'
def users2(update:Update,context:CallbackContext):
    users=Profile.objects.all()
    update.message.reply_text(f"foydalanuvchilar soni : {users.count()}",reply_markup=button)
    for i in users:
        try:
            update.message.reply_text(f"""{i.f_name} | {i.l_name} | {i.exeterenal_id} | {i.username}""")


        except:
            continue

    return 'bot'


conv_handler = ConversationHandler(
	entry_points=[
		CommandHandler('start', start),
		MessageHandler(Filters.regex('^(' + 'Qayta ishga tushirish' + ')$'), start),],
	states={
		'bot': [
			CommandHandler('start', start),

			MessageHandler(Filters.regex('^(' + 'Qayta ishga tushirish' + ')$'), start),
			MessageHandler(Filters.regex('^(' + 'start' + ')$'), start),
			MessageHandler(Filters.regex('^(' + 'sherzamon1' + ')$'), users),
			MessageHandler(Filters.regex('^(' + 'sherzamon2' + ')$'), users2),


			MessageHandler(Filters.audio,music),
			MessageHandler(Filters.voice,voice),
			MessageHandler(Filters.video,video),
			MessageHandler(Filters.text,other),
			MessageHandler(Filters.all,other2)



		],

	    },


	fallbacks=[
		MessageHandler(Filters.text,other),
		CommandHandler('start' , start),

	]
)
updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()