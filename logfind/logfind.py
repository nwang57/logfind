#build a logfind class skeleton
import os

class Logfind(object):

  def __init__(self, operator = "and"):
    self.filenames = os.path.join(os.getcwd(),'README.md')
    self.operator = operator

  def search(self, words):
    search_file = open(self.filenames,'r').read()
    if self.operator == "and":
      for word in words:
        if word not in search_file:
          return False
      return True
    else:
      return False

def main():
  test = Logfind()
  print(test.search(['logfind','project']))




if __name__ == '__main__': main()
