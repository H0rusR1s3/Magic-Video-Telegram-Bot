import requests
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

def start(update, context):
    # Present the user with the option of "Video"
    buttons = [['Video']]
    update.message.reply_text('Please select an option:', reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    return 'SELECTION'

def handle_selection(update, context):
    # Get the user's selection
    selection = update.message.text
    if selection == 'Video':
        # Ask the user for a URL
        update.message.reply_text('Please enter a URL:')
        return 'HANDLE_URL'

def handle_url(update, context):
    # Download the video from the URL and send it to the user
    video_url = update.message.text
    video_response = requests.get(video_url)
    video_content = video_response.content
    update.message.reply_video(video_content)
    # Ask the user if they want to download another video
    buttons = [['Yes'], ['No']]
    update.message.reply_text('Do you want to download another video?', reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
    return 'ANOTHER_VIDEO'

def handle_another_video(update, context):
    # Get the user's response
    response = update.message.text
    if response == 'Yes':
        # Ask the user for a URL
        update.message.reply_text('Please enter a URL:')
        return 'HANDLE_URL'
    elif response == 'No':
        # Go back to the start
        return start(update, context)

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token=5865686892:AAHx2kxlPL_RD6ZJ83Ldd5aqoA1R5JGsO_4, use_context=True)