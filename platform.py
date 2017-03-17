#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-03-08 19:30:18
# ---------------------------------------


import random


WINDOWS_VERSIONS = [5.1, 5.2, 6.0, 6.1, 6.2, 6.3, 10.0]

LINUX_VERSIONS = ['Ubuntu', 'Fedora', 'OpenSUSE', 'Mint', 'ElementaryOS', 'PCLinuxOS']

MAC_VERSIONS = [
    '10.8.0', '10.8.1', '10.8.2', '10.8.3', '10.9.0', '10.9.1', '10.9.2', '10.9.3',
    '10.9.4', '10.10.0', '10.10.1', '10.10.2', '10.10.3', '10.10.4', '10.10.5',
    '10.11.0', '10.11.1', '10.11.2', '10.11.3', '10.11.4', '10.11.5', '10.11.6',
    '10.12.0', '10.12.1', '10.12.2', '10.12.3', '10.12.4', '10.12.5', '10.12.6'
]

# list of android versions, see more 'https://source.android.com/source/build-numbers?hl=zh-cn'
#
ANDROID_VERSIONS = {
    '4.0.1':    'Build/ITL41F',
    '4.0.2':    'Build/ICL53F',
    '4.0.3':    'Build/IML74K',
    '4.0.4':    'Build/IMM76',
    '4.1.1':    'Build/JRO03C',
    '4.1.2':    'Build/JZO54K',
    '4.2':      'Build/JOP40C',
    '4.2.1':    'Build/JOP40D',
    '4.2.2':    'Build/JDQ39',
    '4.3':      'Build/JWR66V',
    '4.3.1':    'Build/JLS36I',
    '4.4':      'Build/KRT16M',
    '4.4.1':    'Build/KOT49E',
    '4.4.2':    'Build/KOT49H',
    '4.4.3':    'Build/KTU84L',
    '4.4.4':    'Build/KTU84P',
    '5.0':      'Build/LRX21L',
    '5.0.1':    'Build/LRX22C',
    '5.0.2':    'Build/LRX22G',
    '5.1':      'Build/LMY47D',
    '5.1.1':    'Build/LMY47V',
    '6.0':      'Build/MRA58K',
    '6.0.1':    'Build/MMB29K',
    '7.0':      'Build/NRD90M',
    '7.1':      'Build/NDE63L',
    '7.1.1':    'Build/NMF26F'
}

# http://api.ineal.me/tss/status
IOS_VERSIONS = {
    '8_1':      '12B410',
    '8_1_1':    '12B436',
    '8_1_2':    '12B440',
    '8_1_3':    '12B466',
    '8_2':      '12D508',
    '8_3':      '12F69',
    '8_4':      '12H143',
    '8_4_1':    '12H321',
    '9_0':      '13A344',
    '9_0_1':    '13A404',
    '9_0_2':    '13A452',
    '9_1':      '13B143',
    '9_2':      '13C75',
    '9_2_1':    '13D15',
    '9_3':      '13E233',
    '9_3_1':    '13E238',
    '9_3_2':    '13F69',
    '9_3_3':    '13G34',
    '9_3_4':    '13G35',
    '9_3_5':    '13G36',
    '10_0_1':   '14A403',
    '10_0_2':   '14A456',
    '10_1':     '14B72',
    '10_1_1':   '14B100',
    '10_2':     '14C92',
    '10_2_1':   '14D27',
    '10_3':     '14E277',
    '10_3_1':   '14E304',
    '10_3_2':   '14F89',
    '10_3_3':   '14G60',
    '11_0':     '15A372',
    '11_0_1':   '15A402',
    '11_0_2':   '15A421',
    '11_0_3':   '15A432'
}

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
        'X11; U; Linux i686',
        'X11; U; Linux x86_64',
        'X11; U; Linux i686 on x86_64',
        'X11; {version}; Linux i686',
        'X11; {version}; Linux x86_64',
        'X11; {version}; Linux i686 on x86_64',
    ],
    'android': [
        'Android {version}'
    ],
    'ios': [
        'CPU iPhone OS {version} like Mac OS X'
    ]
}


def get_all_versions(name):
    if name == 'android':
        return list(ANDROID_VERSIONS.copy().keys())
    elif name == 'windows':
        return WINDOWS_VERSIONS.copy()
    elif name == 'mac':
        return MAC_VERSIONS.copy()
    elif name == 'linux':
        return LINUX_VERSIONS.copy()
    elif name == 'ios':
        return list(IOS_VERSIONS.copy().keys())
    else:
        names = ['android', 'windows', 'mac', 'linux', 'ios']
        raise ValueError('name must be one of {}'.format(names))


def random_platform_token(platforms=None):
    if platforms is None:
        name = random.choice(list(PLATFORM_TOKEN_MAP.keys()))
    else:
        name = random.choice(list(platforms))

    token = random.choice(PLATFORM_TOKEN_MAP[name])
    if '{version}' in token:
        version = random.choice(get_all_versions(name))
        token = token.format(version=version)
    return name, token


def get_platform_tokens(name=None):
    names = ['windows', 'mac', 'linux', 'android', 'ios']
    if name not in names:
        raise ValueError('name must be one of {}'.format(names))

    tokens = []
    for x in PLATFORM_TOKEN_MAP[name]:
        tokens.extend(
            [(name, x.format(version=version)) for version in get_all_versions(name)]
        )
    return tokens
