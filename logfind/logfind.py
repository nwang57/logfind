#build a logfind class skeleton
import os
import argparse

class Logfind(object):

  def __init__(self):
    #init the files to be searched
    self.filenames = os.path.join(os.getcwd(),'README.md')
    self.operator = ""
  #set the logic
  def set_operator(self, operator):
    self.operator = operator

  def search(self, words):
    search_file = open(self.filenames,'r').read()
    if self.operator == "and":
      for word in words:
        if word not in search_file:
          return False
      return True
    else:
      #todo 'or' logic
      return False

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-o', nargs='+')
  parser.add_argument('words', nargs='+')

  args = parser.parse_args()

  test = Logfind()
  if args.o is not None:
    test.set_operator("or")
  else:
    test.set_operator("and")

  #test = Logfind()
  #print(test.search(['logfind','project']))
  print("first arg ",args.words)
  print("second arg",args.o)




if __name__ == '__main__': main()
