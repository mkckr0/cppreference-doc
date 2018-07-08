#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Copyright (C) 2018  Monika Kairaityte <monika@kibit.lt>
#
#   This file is part of cppreference-doc
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see http://www.gnu.org/licenses/.

from commands.preprocess import *
import unittest
from lxml import etree

class TestConvertLoaderName(unittest.TestCase):
    def test_convert_loader_name(self):
        url = 'http://en.cppreference.com/mwiki/load.php?debug=false&lang=en&\
modules=site&only=scripts&skin=cppreference2&*'
        self.assertEqual('site_scripts.js', convert_loader_name(url))

        url = 'http://en.cppreference.com/mwiki/load.php?debug=false&lang=en&\
modules=site&only=styles&skin=cppreference2&*'
        self.assertEqual('site_modules.css', convert_loader_name(url))

        url = 'http://en.cppreference.com/mwiki/load.php?debug=false&lang=en&\
modules=skins.cppreference2&only=scripts&skin=cppreference2&*'
        self.assertEqual('skin_scripts.js', convert_loader_name(url))

        url = 'http://en.cppreference.com/mwiki/load.php?debug=false&lang=en&\
modules=startup&only=scripts&skin=cppreference2&*'
        self.assertEqual('startup_scripts.js', convert_loader_name(url))

        url = 'http://en.cppreference.com/mwiki/load.php?debug=false&lang=en&\
modules=ext.gadget.ColiruCompiler%2CMathJax%7Cext.rtlcite%7Cmediawiki.\
legacy.commonPrint%2Cshared%7Cskins.cppreference2&only=styles&skin=\
cppreference2&*'
        self.assertEqual('ext.css', convert_loader_name(url))

        with self.assertRaises(Exception):
            convert_loader_name('')

class TestHasClass(unittest.TestCase):
    def test_has_class(self):
        el = etree.Element('tag')
        self.assertEqual(False, has_class(el, []))
        self.assertEqual(False, has_class(el, ['']))
        self.assertEqual(False, has_class(el, ['a']))
        self.assertEqual(False, has_class(el, ['tag']))

        el.set('class', '')
        self.assertEqual(False, has_class(el, []))
        self.assertEqual(False, has_class(el, ['']))
        self.assertEqual(False, has_class(el, ['a']))
        self.assertEqual(False, has_class(el, ['tag']))

        el.set('class', 'a')
        self.assertEqual(False, has_class(el, []))
        self.assertEqual(False, has_class(el, ['']))
        self.assertEqual(True, has_class(el, ['a']))
        self.assertEqual(False, has_class(el, ['b']))
        self.assertEqual(False, has_class(el, ['tag']))
        self.assertEqual(True, has_class(el, ['a', 'b']))
        self.assertEqual(True, has_class(el, ['b', 'a']))
        self.assertEqual(False, has_class(el, ['b', 'c']))

        el.set('class', 'a b')
        self.assertEqual(False, has_class(el, []))
        self.assertEqual(False, has_class(el, ['']))
        self.assertEqual(True, has_class(el, ['a']))
        self.assertEqual(True, has_class(el, ['b']))
        self.assertEqual(False, has_class(el, ['tag']))
        self.assertEqual(True, has_class(el, ['a', 'b']))
        self.assertEqual(True, has_class(el, ['b', 'a']))
        self.assertEqual(True, has_class(el, ['b', 'c']))

        el.set('class', 'a  b')
        self.assertEqual(False, has_class(el, []))
        self.assertEqual(False, has_class(el, ['']))
        self.assertEqual(True, has_class(el, ['a']))
        self.assertEqual(True, has_class(el, ['b']))
        self.assertEqual(False, has_class(el, ['tag']))
        self.assertEqual(True, has_class(el, ['a', 'b']))
        self.assertEqual(True, has_class(el, ['b', 'a']))
        self.assertEqual(True, has_class(el, ['b', 'c']))

class TestIsExternalLink(unittest.TestCase):
    def test_is_external_link(self):
        self.assertEqual(True, is_external_link('http://a'))
        self.assertEqual(True, is_external_link('https://a'))
        self.assertEqual(True, is_external_link('ftp://a'))
        self.assertEqual(False, is_external_link('ahttp://a'))
        self.assertEqual(False, is_external_link(' http://a'))


