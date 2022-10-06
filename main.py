import os
import threading
from profile import Profile

from flask import Flask, request

from config import config
from const import *
from graph_api import GraphApi

app = Flask(__name__)

users: dict = {}


def handle_postback(messaging, user_id):
    print("handle_postback", messaging)
    payload = messaging["postback"]["payload"]
    if payload.upper() == "GET_STARTED":
        GraphApi.call_send_api(
            {
                "recipient": {"id": user_id},
                "message": {
                    "text": "Thanks for using our product. Could you spend little time for rating our service from 1 to 10 stars?"
                },
            },
            1,
        )


def handle_text(messaging, user_id):
    text = messaging["message"]["text"]
    GraphApi.call_send_api(
        {"recipient": {"id": user_id}, "message": {"text": "Thank you very much."}}, 1
    )


def handle_message(message):
    for entry in message.get("entry", []):
        for messaging in entry.get("messaging", []):
            sender_psid = messaging["sender"]["id"]
            user = GraphApi.get_user_profile(sender_psid)
            if not user:
                continue
            if sender_psid not in users.keys():
                users[sender_psid] = user
            print("messaging ", messaging)
            if "postback" in messaging:
                handle_postback(messaging, sender_psid)
            elif "message" in messaging:
                handle_text(messaging, sender_psid)


def webhook_post(req):
    body = req.get_json()
    if body.get("object") == "page":

        thread = threading.Thread(target=handle_message, kwargs={"message": body})
        thread.start()

        return "RECEIVED", 200
    else:
        return "Not found", 404


def webhook_get(req):
    mode = req.args.get("hub.mode")
    token = req.args.get("hub.verify_token")
    challenge = req.args.get("hub.challenge")
    if mode and token:
        if mode == "subscribe" and token == config.verify_token:
            return challenge, 200
        else:
            return "Forbidden", 403
    else:
        return "Forbidden", 403


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "POST":
        return webhook_post(request)
    else:
        return webhook_get(request)


@app.route("/", methods=["GET"])
def home():
    return "Start Review", 200


@app.route("/profile", methods=["GET"])
def profile():
    token = request.args.get("verify_token")
    if not config.webhook_url().startswith("https://"):
        return "ERROR - Need a proper API_URL in the .env file", 200
    if not token or token != config.verify_token:
        return "Forbidden", 403

    try:
        Profile.set_webhook()
        Profile.set_thread()
        Profile.set_whitelisted_domains()
    except Exception as e:
        return str(e), 500

    return "Set profile", 200
