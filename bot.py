import telebot
import speedtest

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! How can I assist you today?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Here are the commands you can use:\n/start - Welcome message\n/help - List of commands\n/speedtest - Check internet speed")

@bot.message_handler(commands=['speedtest'])
def check_speed(message):
    st = speedtest.Speedtest()
    bot.reply_to(message, "Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    bot.reply_to(message, "Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    server_name = st.get_best_server()['sponsor']
    
    response = (f"Download speed: {download_speed:.2f} Mbps\n"
                f"Upload speed: {upload_speed:.2f} Mbps\n"
                f"Server: {server_name}")
    bot.reply_to(message, response)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "You said: " + message.text)

if __name__ == '__main__':
    print("Bot is polling...")
    bot.polling(none_stop=True)
