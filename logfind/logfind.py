#build a logfind class skeleton
import os
import argparse

class Logfind(object):

  def __init__(self):
    #init the files to be searched
    self.filenames = 'README.md'
    self.filenamepath = os.path.join(os.getcwd(), self.filenames)
    self.operator = ""
  #set the logic
  def set_operator(self, operator):
    self.operator = operator

  def search_file(self, filename, words):
    search_file = open(filename,'r').read()
    if self.operator == "and":
      for word in words:
        if word not in search_file:
          return False
      return True

    elif self.operator == "or":
      for word in words:
        if word in search_file:
          return True
      return False

    else:
      raise Logfind.OperatorError("Operator is not specified! Plz use set_operator(and/or)")
      return False

  def search(self, words):
    if self.search_file(self.filenamepath, words):
      return self.filenames

  class OperatorError(Exception):

    def __init__(self, value):
      self.value = value

    def __str__(self):
      return repr(self.value)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-o', nargs='+')
  parser.add_argument('words', nargs='+')

  args = parser.parse_args()

  test = Logfind()
  if (args.o is not None) and (args.words is None):
    test.set_operator("or")
  elif (args.o is None) and (args.words is not None):
    test.set_operator("and")
  else:
    raise ValueError("Invalid Argument")

  print("first arg ",args.words)
  print("second arg",args.o)




if __name__ == '__main__': main()
