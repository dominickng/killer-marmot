# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This file defines the metadata for each app (used by the templating system).
"""

import copy
import os.path

# HTML defaults.
DEFAULT_VIEWPORT = 'width=device-width, initial-scale=1'

# Manifest defaults.
DEFAULT_NAME = 'Killer Marmot'
DEFAULT_SHORT_NAME = 'Marmot'
DEFAULT_START_URL = 'index.html'
DEFAULT_DISPLAY = 'standalone'
RELATED_APP_PLAY = {
    'platform': 'play',
    'id': 'com.sbg.crappybird',
}
RELATED_APP_PLAY_REAL = {
    'platform': 'play',
    'id': 'io.github.benfredwells.killermarmot',
}
RELATED_APP_PLAY_REFERRER = {
    'platform': 'play',
    'url': 'https://play.google.com/store/apps/details?id=com.sbg.crappybird&'
           'referrer=utm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_term%3D'
           'podcast%252Bapps%26utm_content%3DdisplayAd1%26utm_campaign%3D'
           'podcast%252Bgeneralkeywords',
    'id': 'com.sbg.crappybird',
}
RELATED_APP_PLAY_NON_GOOGLE_REFERRER = {
    'platform': 'play',
    'url': 'http://a.localytics.com/android?id=com.google.samples.apps.iosched&'
           'referrer=utm_source%3Dother_app_banners_local%26utm_campaign%3D'
           'AppBanners%2520Local',
    'id': 'com.google.samples.apps.iosched',
}
RELATED_APP_IOS = {
    'platform': 'ios',
    'id': 'basdfasdf',
}


def make_icons(name='marmot'):
  """Makes the icons dict."""
  icons = []
  for size in (None, 48, 96, 128, 200, 480):
    s = '' if size is None else '_%d' % size
    # TODO(mgiuca): Make icon dicts collections.OrderedDict to avoid random
    # output.
    icon_dict = {
        'src': '../%s%s.png' % (name, s),
        'sizes': 'any' if size is None else '%dx%d' % (size, size),
        'type': 'image/png',
        'density': 1,
    }
    icons.append(icon_dict)
  return icons


DEFAULT_ICONS = make_icons()


# Each app is represented by a dictionary with the following optional fields:
# - description: String description of the app.
# - index_js: Boolean; whether to load index.js.
# - manifest_json: Boolean; whether to link to manifest.json.
# - viewport: String value for the viewport meta tag. If omitted, no tag. Can
#   use DEFAULT_VIEWPORT.
# - referrer: Boolean; whether to include a referrer meta tag.
# - web_stuff: Boolean; whether to include name, short_name, icons, display and
#   start_url. Can be overridden by other fields.
# - icons: List of dicts; manifest member.
# - display: String; display field for manifest. None for no display.
# - prefer_related_applications: Boolean; manifest member.
# - related_applications: List of dicts; manifest member.
APPS = {
    'ios_and_play': {
        'description': 'Site with a related iOS and play app in the manifest.',
        'manifest_json': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_IOS, RELATED_APP_PLAY],
    },

    'ios_and_web': {
        'description': 'Site which is a valid web app, but has a preferred iOS app '
                       'in its manifest.',
        'index_js': True,
        'manifest_json': True,
        'web_stuff': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_IOS],
    },

    'ios': {
        'description': 'Site with a related iOS app in the manifest.',
        'manifest_json': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_IOS],
    },

    'none': {
        'description': 'Site with no manifest.',
        'index_js': True,
    },

    'play_and_ios': {
        'description': 'Site with a related play app, and iOS app, in its '
                       'manifest.',
        'manifest_json': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_PLAY, RELATED_APP_IOS],
    },

    'play_and_web': {
        'description': 'Site which is a valid web app, but has a preferred play '
                       'app in its manifest.',
        'index_js': True,
        'manifest_json': True,
        'web_stuff': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_PLAY],
    },

    'play': {
        'description': 'Site with a related play app in the manifest.',
        'manifest_json': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_PLAY],
    },

    'play_non_google_link_referrer': {
        'description': 'Site with a related play app (non-Play-Store referrer) '
                       'in the manifest.',
        'manifest_json': True,
        'referrer': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_PLAY_NON_GOOGLE_REFERRER],
    },

    'play_referrer': {
        'description': 'Site with a related play app (Play Store referrer) in '
                       'the manifest.',
        'manifest_json': True,
        'referrer': True,
        'prefer_related_applications': True,
        'related_applications': [RELATED_APP_PLAY_REFERRER],
    },

    'web': {
        'description': 'Site which is a valid web app.',
        'index_js': True,
        'manifest_json': True,
        'viewport': DEFAULT_VIEWPORT,
        'web_stuff': True,
    },

    'web_and_ios': {
        'description': 'Site which is a valid web app, and also with a '
                       'non-preferred iOS app in its manifest.',
        'index_js': True,
        'manifest_json': True,
        'viewport': DEFAULT_VIEWPORT,
        'web_stuff': True,
        'related_applications': [RELATED_APP_IOS],
    },

    'web_and_play': {
        'description': 'Site which is a valid web, and also with a non-preferred '
                       'play app in its manifest.',
        'index_js': True,
        'manifest_json': True,
        'viewport': DEFAULT_VIEWPORT,
        'web_stuff': True,
        'related_applications': [RELATED_APP_PLAY, RELATED_APP_PLAY_REAL],
    },

    'web_broken': {
        'description': 'Site which is a broken web app.',
        'index_js': True,
        'manifest_json': True,
        'viewport': 'minimum-scale=0.6, maximum-scale=5.0, '
                    'user-scalable=fixed, INITIAL-SCALE=1.0, '
                    'width=device-width',
        'web_stuff': True,
        'icons': make_icons(name='missing'),
        'display': None,
    },

    'web_no_meta_viewport': {
        'description': 'Site which is missing a viewport.',
        'index_js': True,
        'manifest_json': True,
        'web_stuff': True,
    },

    'web_redispatch': {
        'description': 'Site which is a valid web app.',
        'index_js': True,
        'manifest_json': True,
        'viewport': DEFAULT_VIEWPORT,
        'web_stuff': True,
    },
}
