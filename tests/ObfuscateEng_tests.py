#!/usr/bin/env python
from nose.tools import *
import ObfuscateEng

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
