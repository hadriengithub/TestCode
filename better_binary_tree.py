class Node():
	def __init__(self,key,left_child=None,right_child=None):
		self.key=key
		self.left_child=left_child
		self.right_child=right_child
	def __repr__(self):
		return f"Noeud('{self.key}')"
	def is_leaf(self):
		if self.left_child==None and self.right_child==None:
			return True
		return False
	def size(self):
		if self.key==None:
			return 0
		if self.left_child==None:
			left_size=0
		else:
			left_size=self.left_child.size()
		if self.right_child==None:
			right_size=0
		else:
			right_size=self.right_child.size()
		return 1+left_size+right_size
	def height(self):
		if self.key==None:
			return -1
		left_height=(-1)
		right_height=(-1)
		if self.left_child!=None:
			left_height=self.left_child.height()
		if self.right_child!=None:
			right_height=self.right_child.height()
		return 1+max(left_height,right_height)

class Binary_Tree():
	def __init__(self, root=None):
		self.root=root
	def __repr__(self):
		return f"Arbre binaire(Racine = {self.root})"

	

F=Node("F")
E=Node("E")
D=Node("D",E,F)
C=Node("C",None,D)
I=Node("I")
H=Node("H")
G=Node("G",None,H)
B=Node("B",G,I)
A=Node("A",B,C)
my_tree=Binary_Tree(A)

print(A.height())
