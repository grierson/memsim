#!/usr/bin/env python3
""" TEST Process Panel """
from unittest import TestCase
from source.process import Process


class TestProcess(TestCase):
    """ Test Process """
    def setUp(self):
        """ Create Process """
        self.process = Process("Firefox", 200, 0)

    def test_should_store_name(self):
        """ test name """
        self.assertEqual(self.process.name, "Firefox")

    def test_should_store_size(self):
        """ test size """
        self.assertEqual(self.process.size, 200)

    def test_should_store_address(self):
        """ test address """
        self.assertEqual(self.process.address, 0)
