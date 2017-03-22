#!/usr/bin/env python3

import os
import jinja2

def render(filename, context):
    ''' Given jinja2 template, generate HTML
    Adapted from http://matthiaseisen.com/pp/patterns/p0198/

    Args:
        * filename - jinja2 template
        * context - dict of variables to pass in

    Returns:
        * rendered HTML from jinja2 templating engine
    '''
    path = os.path.dirname(os.path.abspath(__file__))
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)
