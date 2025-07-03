from flask import Flask, request


from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

import json
app = Flask(__name__)



@app.route("/")
def home():
  line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
  try:
    msg = request.args.get('msg')
    #https://XXXXX.app/?msg=123
    if msg != None:
        line_bot_api.push_message('User ID', TextSendMessage(text=msg))
        return msg
    else:
        return 'OK'
  except:
    print('error')

if __name__ == "__main__":
    app.run()
