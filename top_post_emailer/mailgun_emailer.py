#!/usr/bin/env python3

import os
import configparser
import requests
from requests.exceptions import HTTPError

def send_email(html):
    '''Given HTML template, sends Reddit Top Post Digest email using MailGun's API

    Arg:
        html - HTML to send via email

    Returns:
        None
    '''
    ## api params (using configparser)
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'settings.cfg'))
    key = config.get('MailGun', 'api')
    domain = config.get('MailGun', 'domain')

    ## set requests params
    request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(domain)
    payload = {
        'from': 'alysivji@gmail.com',
        'to': 'alysivji@gmail.com',
        'subject': 'Reddit Top Post Digest',
        'html': html,
    }

    try:
        r = requests.post(request_url, auth=('api', key), data=payload)
        r.raise_for_status()
        print('Success!')
    except HTTPError as e:
        print('Error {}'.format(e.response.status_code))
