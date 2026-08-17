import telebot
from pprint import pprint
from google import genai

bot=telebot.TeleBot("API TELEGRAM")

client=genai.Client(api_key="API GOOGLE")



Model="gemini-2.5-flash"


chat=client.chats.create(model=Model,config={"system_instruction":"خیلی کوتاه ساده جواب بده زیاد طولانی نکن پیام رو"})



@bot.message_handler(commands=["start"])

def start(message):
    bot.reply_to(message,"سلام به بات من خوش اومدی😘 میتونی هر سوالی داری بپرسی ")

@bot.message_handler(commands=["about"])
def about(about):
    bot.reply_to(about,"این یک چت بات با استفاده از مدل ساده gemini-2.5-flashهست شما میتونید سوالاتون رو از من بپرسید 👾🤖👽😎😘")

@bot.message_handler(content_types=["text"])

def give_message(give):
    response=chat.send_message(give.text)
    text=response.text
    bot.reply_to(give,text)


if __name__=="__main__":
    pprint("Bot is Runnig...")
    bot.infinity_polling()