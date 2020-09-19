#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import re
import datetime
import bs4
import tools
from bs4 import BeautifulSoup
import urllib

root = pathlib.Path(__file__).parent.resolve()


class Source (object):

    def __init__(self):
        self.T = tools.Tools()

    def getSource(self):
        img = ''

        url = 'http://www.zuidazy5.com'
        req = [
            'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36',
        ]
        res = self.T.getPage(url, req)
        if res['code'] == 200:
            soup = BeautifulSoup(res['body'], 'html.parser')
            img = soup.find(name='div',attrs={"class":"xing_vb"})
            print(img)
            return img


if __name__ == '__main__':
    obj = Source()
