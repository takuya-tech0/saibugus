from fastapi import FastAPI, Request, HTTPException
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    FollowEvent, FlexMessage, FlexSendMessage
)
import os
from starlette.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return PlainTextResponse("LINE Bot is running!")
