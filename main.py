import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import time
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot Token from BotFather
TOKEN = "8181288340:AAG8JEa2GXGstmgt1yzCrBJzhCkEweiBtl0"

# Initialize the bot
bot = telegram.Bot(token=TOKEN)

# Handler for start command
def start(update, context):
    update.message.reply_text('Hello! I am IQsmart bot 🤖. Send me PRNG numbers (e.g., 6 3 2 8) to get predictions 🔮.')

# Handler for handling PRNG numbers
def handle_prng(update, context):
    prng_input = update.message.text
    prng_numbers = [int(x) for x in prng_input.split() if x.isdigit()]
    
    # Run the prediction system and send the output
    prediction = run_prediction(prng_numbers)
    update.message.reply_text(f"Prediction: {prediction} ⚡")

def run_prediction(prng_numbers):
    # Sample logic for Big/Small and Red/Green prediction
    big_small = ['Big' if x > 4 else 'Small' for x in prng_numbers]
    red_green = ['Red' if x % 2 == 0 else 'Green' for x in prng_numbers]
    
    # Simulated prediction result
    accuracy = random.randint(70, 95)  # Sample accuracy between 70% to 95%
    prediction = f"Big/Small: {big_small}, Red/Green: {red_green}, Accuracy: {accuracy}%"
    
    # Return the prediction
    return prediction

# Handler for feedback (positive/negative)
def feedback(update, context):
    feedback_text = update.message.text
    update.message.reply_text("Feedback received 👍. Thank you for your response!")
    
    # Logic for feedback integration (this can be improved to make the bot learn over time)
    # E.g., Adjust prediction logic based on feedback

def main():
    # Create an updater and pass the bot token
    updater = Updater(TOKEN, use_context=True)
    
    # Register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_prng))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, feedback))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
