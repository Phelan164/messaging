# Copyright 2020
#
# Created by nguyenvantam at 06/10/2022
# Modified by nguyenvantam
#
# -*- coding: utf-8 -*-
from config import config
from const import *
from graph_api import GraphApi


class Profile:
    def __int__(self):
        pass

    @staticmethod
    def set_webhook():
        GraphApi.call_subscriptions_api()
        GraphApi.call_subcribed_app()

    @staticmethod
    def set_thread():
        profile_payload = {
            "get_started": {"payload": "GET_STARTED"},
            "greeting": greetings,
        }
        GraphApi.call_messenger_profile(profile_payload)

    @staticmethod
    def set_whitelisted_domains():
        whitelisted_domains = {"whitelisted_domains": config.get_whitelisted_domains()}
        GraphApi.call_messenger_profile(whitelisted_domains)
