
# super class
class Super:
	
	var1 = None #public: accessible from entire program.
	_var2 = None #protected: accessible from all derived classes.
	__var3 = None #private: only accessible from class.
	
	def __init__(self, var1, var2, var3): 
		self.var1 = var1
		self._var2 = var2 #can be accessed from child class.
		self.__var3 = var3
	
	def displayPublicMembers(self):
		print("Public Data Member: ", self.var1)
		
	def _displayProtectedMembers(self):#method can be called from derived class. 
		print("Protected Data Member: ", self._var2)
		 
	def __displayPrivateMembers(self):
		return 'private Data Member: ' + self.__var3
		#functions as the getter method. A setter can be added. 
	def accessPrivateMembers(self):#public method to make private attribute accessible. 
		return self.__displayPrivateMembers()

# derived class
class Sub(Super):

	# constructor 
	def __init__(self, var1, var2, var3): 
				Super.__init__(self, var1, var2, var3)
		
	# public member function 
	def accessProtectedMembers(self):
				return self._displayProtectedMembers()
	

# creating objects of the derived class	 
obj = Sub("Geeks", 4, "Geeks !") 

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
print(obj.accessPrivateMembers()) 

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
#print(obj.__var3)
