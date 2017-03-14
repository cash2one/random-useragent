#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-03-08 19:30:18
# ---------------------------------------


import random


WINDOWS_VERSIONS = [5.1, 5.2, 6.0, 6.1, 6.2, 6.3, 10.0]

LINUX_VERSIONS = ['Ubuntu', 'U', 'Fedora']

MAC_VERSIONS = [
    '10.8.0', '10.8.1', '10.8.2', '10.8.3', '10.9.0', '10.9.1', '10.9.2', '10.9.3',
    '10.9.4', '10.10.0', '10.10.1', '10.10.2', '10.10.3', '10.10.4', '10.10.5',
    '10.11.0', '10.11.1', '10.11.2', '10.11.3', '10.11.4', '10.11.5', '10.11.6',
    '10.12.0', '10.12.1', '10.12.2', '10.12.3', '10.12.4', '10.12.5', '10.12.6'
]

ANDROID_VERSIONS = [
    '4.0.1', '4.0.2', '4.0.3', '4.0.4', '4.1.1', '4.1.2', '4.2.1', '4.2.2',
    '4.3.0', '4.3.1', '4.4.0', '4.4.1', '4.4.2', '4.4.3', '4.4.4', '5.0.0',
    '5.0.1', '5.0.2', '5.1.0', '5.1.1', '6.0.0', '6.0.1', '7.0.0', '7.1.0',
    '7.1.1'
]

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
        'Android {version}'
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
        tokens.extend(
            [(name, x.format(version=version)) for version in PLATFORM_VERSION_MAP[name]]
        )
    return tokens
