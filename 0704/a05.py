from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageAction,ConfirmTemplate,PostbackAction,ImageCarouselColumn,ImageCarouselTemplate,MessageTemplateAction,ButtonsTemplate,TemplateSendMessage,MessageEvent, TextMessage, TextSendMessage
import random
app = Flask(__name__)


token='XXXX'
secret='XXXX'
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



@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text        

    if getA =='1' :
                line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackAction(
                label='postback',
                display_text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='message',
                text='message text'
            )
        ]
    )
 )

 )
       
    elif getA=='2':
        confirm_template_message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackAction(
                label='postback',
                display_text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='message',
                text='message text'
            )
        ]
    )
)

        line_bot_api.reply_message(event.reply_token, confirm_template_message)

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入1或2"))

if __name__ == "__main__":
    app.run()
