import EbayScraper
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

"""
Using: https://github.com/Shawey/Ebay-Scraper/blob/main/EbayScraper.py

"""
app = None
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

async def avg_price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = EbayScraper.Average("Macbook Pro", "us", "all")
    logger.debug(result)
    logger.info(update._effective_message.text)
    await update.message.reply_text(result)

async def get_sale(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(update._effective_message.text)
    result = EbayScraper.Items("Macbook Pro", "us")
    logger.info(result)
    for i in result:
        md_template = f"**Name**: {i['title']}\n\n**Price**: {i['price']}\n\n**Shipping**: {i['shipping']}\n\n**Sale time left**: {i['time-left']}\n\n**End date**: {i['time-end']}\n\n**Bid count: {i['bid-count']}\n\n **Reviews**: {i['reviews-count']}\n\n**Link**: [Go to link]({i['url']})"
        await update.message.reply_markdown(md_template)
        #await update.message.reply_text(i)

def setup_bot() -> None:
    global app
    app = ApplicationBuilder().token("").build()
    logger.info("Bot is running")
    app.add_handler(CommandHandler("avgprice", avg_price))
    app.add_handler(CommandHandler("getsale", get_sale))

def main():
    global app
    setup_bot()
    app.run_polling()
    pass

if __name__ == "__main__":
    main()