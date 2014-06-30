#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FIXME: По уму эту жесть надо убирать, но пока и так сойдет
import sys
sys.path.append ('/home/rus/work/home/regnupg')
import pgpxmlrpc


import unittest
import os.path as osp


if int (sys.version [0]) >= 3:
    import xmlrpc.client as xmlrpclib
else:
    import xmlrpclib


print (sys.version)

SERVICE_KEY = '00970D7538ABB8435BF8E6CEE040C8BCA068662E'
CLIENT_KEY = '5CDD1A70201C2844823AEF81BEFD3D1DB2B51C31'
CLIENT_PWD = '123321'
GPG_HOMEDIR = osp.join (osp.dirname (osp.abspath (__file__)), '__keyring__')


class Test (unittest.TestCase):

    @classmethod
    def setUpClass (cls):
        cls.service = pgpxmlrpc.Service (
            'http://testapi.cherrybase:8080/pgpxmlrpc',
            SERVICE_KEY,
            GPG_HOMEDIR,
            CLIENT_KEY,
            CLIENT_PWD
        )
        cls.meta = xmlrpclib.Server ('http://testapi.cherrybase:8080/pgpxmlrpc/meta', encoding = 'utf-8', allow_none = True)

    def test_sum (self):
        self.assertEqual (self.service.test.sum (10, 200), 210)
        self.assertEqual (self.service.test.sum ('А', 'Б'), u'АБ')

    def test_hello (self):
        self.assertEqual (self.service.test.hello ('tester'), 'Hello tester')

    def test_restypes (self):
        self.assertIsInstance (self.service.test.restypes (), list)

    def test_system (self):
        self.assertIn ('test.hello', self.service.system.listMethods ())

    def test_meta (self):
        self.assertEqual (self.meta.meta.info ()['code'], 'testapi')


if __name__ == "__main__":
    unittest.main ()
