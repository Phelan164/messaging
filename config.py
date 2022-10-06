# Copyright 2020
#
# Created by nguyenvantam at 06/10/2022
# Modified by nguyenvantam
#
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

from singleton import Singleton

load_dotenv()


class Config(metaclass=Singleton):
    api_domain = "https://graph.facebook.com"
    api_version = "v11.0"

    app_id = os.getenv("APP_ID")
    app_secret = os.getenv("APP_SECRET")
    app_url = os.getenv("APP_URL")
    verify_token = os.getenv("VERIFY_TOKEN")
    page_id = os.getenv("PAGE_ID")
    page_access_token = os.getenv("PAGE_ACCESS_TOKEN")

    def api_url(self):
        return f"{self.api_domain}/{self.api_version}"

    def webhook_url(self):
        return f"{self.app_url}/webhook"

    def get_whitelisted_domains(self):
        return [self.api_url()]


config = Config()
