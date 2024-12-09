#Alannah Steck
#U4L2
#A simple reverse 
#૮꒰ ˶• ༝ •˶꒱ა  Good Luck Bunny
from StackClass import ArrayStack

def main():
  original = "Sphinx of black quartz, judge my vow"
  new = ""
  print(f"original : {original}")
  theStack = ArrayStack()
  for item in original:
    theStack.push(item)
  for item in range(len(theStack)):
    addThis = theStack.pop()
    new += addThis
  print(f"reversed : {new}")
    

if __name__ == "__main__":
  main()
