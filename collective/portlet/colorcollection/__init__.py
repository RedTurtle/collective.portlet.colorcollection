# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.portlet.colorcollection')
logger = logging.getLogger('collective.portlet.colorcollection')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
