from HTree import *

class AVLTree(HTree):
  
  def search(self, v):
    if self.isempty():
      return False
    if self.value == v:
      return True
    if self.value < v:
      return self.right.search(v)
    else:
      return self.left.search(v)

  def insert(self,v):
    if self.isempty():
      self.value = v
      self.left = AVLTree()
      self.right = AVLTree()
      self.height = 1
    if self.value == v:
      return 
    if self.value < v:
      self.right.insert(v)
    else:
      self.left.insert(v)
    self.fixheight()
    self.rebalance()
    return

  def deletemax(self):
    if self.isempty():
      return None
    if self.right.isempty(): # This node is the maximum
      v = self.value
      tmp = self.left
      self.value, self.left,self.right = tmp.value,tmp.left,tmp.right
      self.height = tmp.height
      # The two lines below are not needed for correctness
      tmp.value, tmp.left,tmp.right = None,None,None
      tmp = None
      return v
    else:
      v = self.right.deletemax()
      self.fixheight()
      return(v)

  def delete(self,v):
    if self.isempty():
      return
    if self.value < v:
      self.right.delete(v)
      self.fixheight()
    elif self.value > v:
      self.left.delete(v)
      self.fixheight()
    else: # v sits in the current node
      if self.left.isempty():
        tmp = self.right
        self.left,self.right = tmp.left,tmp.right
        self.value,self.height = tmp.value,tmp.height
        # Next lines not needed for correctness
        tmp.value,tmp.left,tmp.right,tmp.height = None, None, None, None
        tmp = None
      else:
        self.value = self.left.deletemax()
        self.fixheight()



 

  
