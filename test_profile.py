# Copyright 2020
#
# Created by nguyenvantam at 06/10/2022
# Modified by nguyenvantam
#
# -*- coding: utf-8 -*-

from profile import Profile


def test_set_webhook():
    try:
        Profile.set_webhook()
        assert True
    except:
        assert False
