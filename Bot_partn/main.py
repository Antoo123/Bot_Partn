import telebot
from telebot import *
import time
# token='5787182783:AAFd-6QHoBcjiia5oWokUSPoSPfeYf0yHBo'
token='5683172971:AAHQogr_WETGAiZpw_PZA9y2PmfE72Jv9SA'
Chat1='-1001851240625'
bot=telebot.TeleBot(token)
# button1=types.KeyboardButton('Получить ссылку')
# button2=types.KeyboardButton('Я подписался')
s=[]
af=[]
@bot.message_handler(commands=["start"],content_types=['text'])


		
def start_command_handler(message):
	
	if " " in message.text:
		print('1')
		referrer_candidate = message.text.split()[1]
		b=str(referrer_candidate)
		
		
		# but_start=types.ReplyKeyboardMarkup()
		# but_start.add(button2)
		bot.send_message(message.chat.id,text='Здравствуйте',)
		
		keyboard = types.InlineKeyboardMarkup()
		url_button = types.InlineKeyboardButton(text="Ссылка на канал", url="https://t.me/+iCtctspUgVEyY2U5")
		keyboard.add(url_button)
		bot.send_message(message.chat.id, "Подпишитесь на наш канал:", reply_markup=keyboard)
		
		s.append(referrer_candidate)	
		# bot.send_message(message.chat.id,text='Ваша реферальная ссылка: https://t.me/gadsdgasdgbot?start='+message.from_user.username)
		but_start=types.ReplyKeyboardMarkup()
		f=open('txt.txt')
		a=f.read()
		if str(referrer_candidate) in a:

			
			# range: количество проверок time.sleep-время в секундах 
			for i in range(5):
				user_status=str(bot.get_chat_member(chat_id=Chat1, user_id=message.from_user.id).status)
				print('123')
				time.sleep(10)
				if user_status in 'member':
					print('1111111')			
					file=open('txt.txt', 'r')
					a=file.read()
					b=a
					b=b.split()
					

					for i in range(len(b)):
						
						if b[i]==str(referrer_candidate):
							int1=int(b[i+1])
							int1+=1
							b[i+1]=int1
							
					c=open('txt.txt','w')
					print(b)		
					for i in range(len(b)):
						
						c.write(str(b[i])+' ')
					
					break	
					
		else:
			print('321')
			f=open('txt.txt','a')
			f.write(str(referrer_candidate+' '+'0'+'\n'))

	else:

		bot.send_message(message.chat.id,text='Ваша реферальная ссылка:https://t.me/gadsdgasdgbot?start='+message.from_user.username)
		


	
	

bot.polling(none_stop=True, interval=0)