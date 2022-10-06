# Copyright 2020
#
# Created by nguyenvantam at 06/10/2022
# Modified by nguyenvantam
#
# -*- coding: utf-8 -*-

import json
import time

import requests

from config import config
from user import User


class GraphApi:
    def __int__(self):
        pass

    @staticmethod
    def call_subscriptions_api(custom_fields=None):
        print(f"Setting app {config.app_id} callback url to {config.webhook_url()}")
        fields = (
            "messages, messaging_postbacks, messaging_optins, "
            + "message_deliveries, messaging_referrals"
        )
        if custom_fields:
            fields = fields + ", " + custom_fields

        url = f"{config.api_url()}/{config.app_id}/subscriptions"
        data = {
            "access_token": f"{config.app_id}|{config.app_secret}",
            "object": "page",
            "callback_url": config.webhook_url(),
            "verify_token": config.verify_token,
            "fields": fields,
            "include_values": "true",
        }

        res = requests.post(url, json=data)
        if res.status_code == 200:
            print("Request subscriptions sent")
        else:
            print("Unable to call_subscriptions_api", res.content)

    @staticmethod
    def call_subcribed_app(custom_fields=None):
        print(f"Subscribing app {config.app_id} to page {config.page_id}")
        fields = (
            "messages, messaging_postbacks, messaging_optins, "
            + "message_deliveries, messaging_referrals"
        )
        if custom_fields:
            fields = fields + ", " + custom_fields

        url = f"{config.api_url()}/{config.page_id}/subscribed_apps"
        data = {"access_token": config.page_access_token, "subscribed_fields": fields}

        res = requests.post(url, json=data)
        if res.status_code == 200:
            print("Request subscriptions sent")
        else:
            print("Unable to call_subcribed_app", res.content)

    @staticmethod
    def call_messenger_profile(body):
        print(f"Setting Messenger Profile for app {config.app_id}")
        url = f"{config.api_url()}/me/messenger_profile"
        params = {
            "access_token": config.page_access_token,
        }
        res = requests.post(url, params=params, json=body)
        if res.status_code == 200:
            print("Request messenger_profile sent")
        else:
            print("Unable to call_messenger_profile", res.content)

    @staticmethod
    def get_user_profile(sender_igsid):
        url = f"{config.api_url()}/{sender_igsid}"
        params = {
            "access_token": config.page_access_token,
            "fields": "first_name, last_name, gender, locale, timezone",
        }
        res = requests.get(url, params=params)
        if res.status_code == 200:
            print("Request get user profile sent")
            data = res.json()
            print("---> data", data)
            return User()
        else:
            print("Unable to get user profile", res.content)
            return None

    @staticmethod
    def call_send_api(body, delay):
        time.sleep(delay)
        url = f"{config.api_url()}/me/messages"
        params = {"access_token": config.page_access_token}
        res = requests.post(url, params=params, json=body)
        print("--->> ", res.status_code, res.content)
        if res.status_code != 200:
            print("Could not send the message")
