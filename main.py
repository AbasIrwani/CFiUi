from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Your Telegram Bot Token
BOT_TOKEN = "7905964403:AAFRfDSpAsyyt6I17Xzen4xBfV7ZdrZF494"

# Define your start command function
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Check Price", callback_data='check_price')],
        [InlineKeyboardButton("Help", callback_data='help')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome to the Crypto Bot!", reply_markup=reply_markup)

# Callback function for buttons
def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'check_price':
        query.edit_message_text(text="Fetching the latest price...")
        # Call your API to get crypto price (fake value here)
        query.edit_message_text(text="Price: $50,000")  # Replace with actual API response

    elif query.data == 'help':
        query.edit_message_text(text="Use the 'Check Price' button to get the latest price!")

# Main function to set up the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))  # Handle '/start' command
    dp.add_handler(CallbackQueryHandler(button))   # Handle button clicks
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
