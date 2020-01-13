#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/01/13 16:01:18
# Contact: androllen#hotmail.com

import random
import os
import json
from app.config import Config


def soul():
    data_file_path = os.path.join(Config.APP_ROOT, 'static/json/soul.json')
    with open(data_file_path, 'r', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        temp_data_list = random.sample(data, 1)
        temp_data = temp_data_list[0]
        message = str(temp_data)

    return message
