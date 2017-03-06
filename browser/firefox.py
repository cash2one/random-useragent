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


WINDOWS_VERSIONS = [5.1, 5.2, 6.0, 6.1, 6.2, 6.3, 10.0]
MAC_VERSIONS = [10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.11, 10.12, 10.13]
ANDROID_VERSIONS = [4.0, 4.1, 4.3, 4.4, 5.0, 5.1, 6.0, 7.0, 7.1, 8.0]
FIREFOX_VERSIONS = [float(i) for i in range(41, 57)]


PLATFORMS_MAP = {
    'windows': [
        'Windows NT {version}',
        'Windows NT {version}; Win64; x64',
        'Windows NT {version}; WOW64',
    ],
    'mac': [
        'Macintosh; Intel Mac OS X {version}',
        'Macintosh; PPC Mac OS X {version}'
    ],
    'linux': [
        'X11; Linux i686',
        'X11; Linux x86_64',
        'X11; Linux i686 on x86_64',
    ],
    'android': [
        'Android {version}; Mobile',
        'Android {version}; Tablet'
    ]
}


PLATFORM_VERSIONS_MAP = {
    'windows': WINDOWS_VERSIONS,
    'mac': MAC_VERSIONS,
    'android': ANDROID_VERSIONS
}


def get_platform_indicator(name=None):
    if name not in ['windows', 'mac', 'linux', 'android']:
        name = random.choice(list(PLATFORMS_MAP.keys()))

    platform = random.choice(PLATFORMS_MAP[name])

    if '{version}' in platform:
        platform = platform.format(
            version=random.choice(PLATFORM_VERSIONS_MAP[name])
        )
    return name, platform


def get_firefox_version(min_version=41, max_version=56):
    if min is 41 and max is 56:
        return random.choice(FIREFOX_VERSIONS)
    else:
        if (not 41 <= min_version <= 56) or (not 41 <= max_version <= 56):
            raise ValueError('value must be between 41 and 56')

        versions = [float(x) for x in range(min_version, max_version + 1)]
        return random.choice(versions)


def get_user_agent():
    name, platform = get_platform_indicator()
    firefox_version = get_firefox_version()

    gecko_trail = '20100101' if name in ['windows', 'mac', 'linux'] else firefox_version

    ua = 'Mozilla/5.0 ({platform}; rv:{firefox_version}) Gecko/{gecko_trail} Firefox/{firefox_version}'.format(
        platform=platform,
        gecko_trail=gecko_trail,
        firefox_version=firefox_version
    )
    return ua
