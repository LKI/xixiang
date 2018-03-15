# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import six


class Model(object):
    def __repr__(self):
        return six.text_type(self)
