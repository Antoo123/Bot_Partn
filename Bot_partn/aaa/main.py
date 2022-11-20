import telebot
from telebot import *
token='5787182783:AAFd-6QHoBcjiia5oWokUSPoSPfeYf0yHBo'
Chat1='-1001851240625'
bot=telebot.TeleBot(token)
button1=types.KeyboardButton('Получить ссылку')
button2=types.KeyboardButton('Я подписался')


@bot.message_handler(commands=["start"])
def start_command_handler(message):
	# bot.send_message(message.chat.id,text='Здравствуйте, подпишитесь на наш канал:')
	but_start=types.ReplyKeyboardMarkup()
	but_start.add(button2)
	bot.send_message(message.chat.id,text='Здравствуйте',reply_markup=but_start)
	
	keyboard = types.InlineKeyboardMarkup()
	url_button = types.InlineKeyboardButton(text="Ссылка на канал", url="https://t.me/+iCtctspUgVEyY2U5")
	keyboard.add(url_button)
	bot.send_message(message.chat.id, "Подпишитесь на наш канал:", reply_markup=keyboard)
	if " " in message.text:
		referrer_candidate = message.text.split()[1]
		print(referrer_candidate)

		f=open('txt.txt')
		a=f.read()
		if str(referrer_candidate) in a:
			user_status=str(bot.get_chat_member(chat_id=Chat1, user_id=message.from_user.id).status)
			if user_status in 'creator':
				print('123')			
				file=open('txt.txt', 'r')
				a=file.read()
				b=a
				b=b.split()
				print('123')

				for i in range(len(b)):
					# print(b[i])
					if b[i]==str(referrer_candidate):
						int1=int(b[i+1])
						int1+=1
						b[i+1]=int1
						print(b)
				c=open('txt.txt','w')		
				for i in range(len(b)):
					print(b[i])
					c.write(str(b[i])+' ')
				
			
		else:
			f=open('txt.txt','a')
			f.write(str(referrer_candidate+' '+'0'+'\n'))
		
			
			
# Кнопка подписался
@bot.message_handler(content_types=['text'])
def mes1(message):
	if message.text=='Я подписался':
		bot.send_message(message.chat.id,text='Ваша реферальная ссылка: https://t.me/asgfwsgsbot?start='+message.from_user.username)
		but_start=types.ReplyKeyboardMarkup()
def foo(message):
	pass
bot.polling(none_stop=True, interval=0)
