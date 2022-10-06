# Copyright 2020
#
# Created by nguyenvantam at 06/10/2022
# Modified by nguyenvantam
#
# -*- coding: utf-8 -*-


class User:
    def __int__(self, user_id, first_name, last_name, gender, locale, timezone):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.locale = locale
        self.timezone = timezone
