class Binary_Tree():
	def __init__(self, key, left_child=None, right_child=None):
		self.key=key
		self.left_child=left_child
		self.right_child=right_child

	def __repr__(self):
		return f"This is a binary tree whose root is {self.key}"

	def size(self,size=0):
		if self.key==None:
			return 0
		else:
			if self.left_child==None:
				left_tree=0
			else:
				left_tree=self.left_child.size()
			if self.right_child==None:
				right_tree=0
			else:
				right_tree=self.right_child.size()
		return 1+left_tree+right_tree

	def height(self,height=0):
		if self.key==None:
			return -1
		left_height=(-1)
		right_height=(-1)
		if self.left_child!=None:
			left_height=self.left_child.height()
		if self.right_child!=None:
			right_height=self.right_child.height()
		return 1+max(left_height,right_height)

	def new_size(self,size=0):
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

	def new_height(self):
		if self.key==None:
			return -1
		if self.left_child!=None:
			left_height=self.left_child.height()
		if self.right_child!=None:
			right_height=self.right_child.height()
		return 1+max(left_height,right_height)


print("hello world !")
H=Binary_Tree("H")
I=Binary_Tree("I")
E=Binary_Tree("E")
F=Binary_Tree("F")
G=Binary_Tree("G",None,H)
D=Binary_Tree("D",E,F)
C=Binary_Tree("C",None,D)
B=Binary_Tree("B",G,I)
A=Binary_Tree("A",B,C)

print(A.size())
print(A.height())
print(A.new_size())
print(A.new_height())
