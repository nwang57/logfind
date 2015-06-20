from nose.tools import *
#from dir.script import class
from logfind.logfind import Logfind

def setup():
	print("SETUP!")

def teardown():
  print("TEAR DOWN!")

def test_basic():
  test1 = Logfind()
  assert_equal(test1.search(["logfind"]), True)

  test2 = Logfind()
  assert_equal(test2.search(["logfind", "cool"]), False)


