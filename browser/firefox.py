#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-03-06 20:14:18
# ---------------------------------------

#
# see more 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent/Firefox'
#


import random
from platform import random_platform_token


FIREFOX_VERSIONS = [float(i) for i in range(41, 57)]


def get_firefox_version(min_version=41, max_version=56):
    if min is 41 and max is 56:
        return random.choice(FIREFOX_VERSIONS)
    else:
        if (not 41 <= min_version <= 56) or (not 41 <= max_version <= 56):
            raise ValueError('value must be between 41 and 56')

        versions = [float(x) for x in range(min_version, max_version + 1)]
        return random.choice(versions)


def get_user_agent():
    name, platform = random_platform_token()
    firefox_version = get_firefox_version()
    gecko_trail = '20100101' if name in ['windows', 'mac', 'linux'] else firefox_version

    ua = 'Mozilla/5.0 ({platform}; rv:{firefox_version}) Gecko/{gecko_trail} Firefox/{firefox_version}'.format(
        platform=platform,
        gecko_trail=gecko_trail,
        firefox_version=firefox_version
    )
    return ua
