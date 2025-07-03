from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
import random
app = Flask(__name__)

secret='17c2914e2381b70e4c697614728db454'
token='8uYnUXVel0cqNllw+ORRj0q16HepXCUmc3+zpMTqPxyMnU8csqgf0Lft+35XU8mL6fLsmIYUVyL/kVyExJLL2/3KjGqQ+vt4rd440e/cf51k11nmjKeGrYuHbLobyRx53Z5Va0t9RikDriQIVXnlnQdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(token)
line_handler = WebhookHandler(secret)


@app.route('/')
def home():
    return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


reply_arr=[
    TextMessage(text='hello123'),
    ImageSendMessage(
        original_content_url= "https://cms.rhinoshield.app/public/images/small_ip_page_shinchan_powerrangers_icon_8f457372c0.webp",
        preview_image_url= "https://cms.rhinoshield.app/public/images/small_ip_page_shinchan_powerrangers_icon_8f457372c0.webp"),
    TextMessage(text='hello345')

]


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text
    if getA =='123':
        line_bot_api.reply_message(event.reply_token, reply_arr)
    elif getA =='456':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到456了'))
    elif getA =='789':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到789了'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()