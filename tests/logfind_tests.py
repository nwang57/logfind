from nose.tools import *
#from dir.script import class
from logfind.logfind import Logfind

def setup():
	print("SETUP!")

def teardown():
  print("TEAR DOWN!")

def test_and_logic():
  test1 = Logfind()
  test1.set_operator("and")
  assert_equal(test1.search(["logfind"]), True)

  test2 = Logfind()
  test2.set_operator("and")
  assert_equal(test2.search(["logfind", "cool"]), False)

def test_operator():
  test = Logfind()

  test.set_operator("and")
  assert_equal(test.operator, "and")

@raises(Logfind.OperatorError)
def test_operator_exception():
  test = Logfind()
  test.search(["logfind"])
