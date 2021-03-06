from nose.tools import *
#from dir.script import class
from logfind.logfind import Logfind

def setup():
	print("SETUP!")

def teardown():
  print("TEAR DOWN!")

def test_or_logic():
  test1 = Logfind(".*\.md$")
  test1.set_operator("or")
  assert_equal(test1.search(["cool"]), None)

  test2 = Logfind(".*\.md$")
  test2.set_operator("or")
  assert_equal(test2.search(["logfind","cool"]), './README.md')
  pass

def test_and_logic():
  test1 = Logfind(".*\.md$")
  test1.set_operator("and")
  assert_equal(test1.search(["logfind"]), './README.md')

  test2 = Logfind(".*\.md$")
  test2.set_operator("and")
  assert_equal(test2.search(["logfind", "cool"]), None)

def test_operator():
  test = Logfind(".*\.md$")

  test.set_operator("and")
  assert_equal(test.operator, "and")

@raises(Logfind.OperatorError)
def test_operator_exception():
  test = Logfind(".*\.md$")
  test.search(["logfind"])
