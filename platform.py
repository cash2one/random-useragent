#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-03-08 19:30:18
# ---------------------------------------


import random


WINDOWS_VERSIONS = [5.1, 5.2, 6.0, 6.1, 6.2, 6.3, 10.0]
MAC_VERSIONS = [10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.11, 10.12, 10.13]
ANDROID_VERSIONS = [4.0, 4.1, 4.3, 4.4, 5.0, 5.1, 6.0, 7.0, 7.1, 8.0]
LINUX_VERSIONS = ['Ubuntu', 'U']


PLATFORM_TOKEN_MAP = {
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
        'X11; {version}; Linux i686',
        'X11; {version}; Linux x86_64',
        'X11; {version}; Linux i686 on x86_64',
    ],
    'android': [
        'Android {version}; Mobile',
        'Android {version}; Tablet'
    ]
}


PLATFORM_VERSION_MAP = {
    'windows': WINDOWS_VERSIONS,
    'mac': MAC_VERSIONS,
    'android': ANDROID_VERSIONS,
    'linux': LINUX_VERSIONS
}


def random_platform_token(name=None):
    if name not in ['windows', 'mac', 'linux', 'android']:
        name = random.choice(list(PLATFORM_TOKEN_MAP.keys()))

    token = random.choice(PLATFORM_TOKEN_MAP[name])

    if '{version}' in token:
        token = token.format(
            version=random.choice(PLATFORM_VERSION_MAP[name])
        )
    return name, token


def get_platform_tokens(name=None):
    names = ['windows', 'mac', 'linux', 'android']
    if name not in names:
        raise ValueError('name must be one of {}'.format(names))

    tokens = []
    for x in PLATFORM_TOKEN_MAP[name]:
        tokens.extend([x.format(version=version) for version in PLATFORM_VERSION_MAP[name]])
    return tokens
