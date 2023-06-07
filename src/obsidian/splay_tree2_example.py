class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class SplayTree:
    def __init__(self):
        self.root=None

        
    #------------------Insertion--------------------
    def Insert(self,value):
        newnode=Node(value)
        if self.root==None:
            self.root=newnode
        else:
            self.__InsertSplay(value)
            if value< self.root.value:
                newnode.left=self.root.left
                self.root.left = None
                newnode.right=self.root
                self.root=newnode
            elif value > self.root.value:
                newnode.right=self.root.right
                self.root.right = None
                newnode.left=self.root
                self.root=newnode

                
    #--Splaying-only-for-Insertion-----
    def __InsertSplay(self,value):
        while True:
            if self.root.left == None or self.root.left.value < value:
                break
            else:
                if value < self.root.left.value:
                    
                    y=self.root.left
                    self.root.left=None
                    y.right=self.root
                    self.root=y
            if self.root.right == None:
                break
            else:
                if value> self.root.right.value:

                    y=self.root.right
                    self.root.right=None
    #---------------------------------Deletion------------------     

    #------Delete--Case-1----Bottom-Up----
    def BottomUpDelete(self, value):
        Root=self.root
        parent = None
        while (Root.value) !=value:
            if Root.value < value and Root.right is not None:
                parent = Root
                Root= Root.right
            elif Root.value > value and Root.left is not None:
                parent = Root
                Root= Root.left
            else:
                break
        self.__delete(value)
        self.__newsplay(parent.value)


        
    #-----Delete--Case-2-----Top-Down---
    def TopDownDelete(self,value):
        self.__newsplay(value)
        #self.__delete(value)
        self.root.left.right = self.root.right
        self.root = self.root.left


        
    #---Wrapper-for-Deletion    
    def __delete(self, value):
        self.root = self.__deleteNode(self.root, value)

    def __minValueNode(self, node): 
        current = node 
      
        while(current.left is not None): 
            current = current.left  
      
        return current  
    def __deleteNode(self,root, value): 
  
        if root is None: 
            return root  
  

        if value < root.value: 
            root.left = self.__deleteNode(root.left, value) 
      

        elif(value > root.value): 
            root.right = self.__deleteNode(root.right, value) 
      
        else: 
              

            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  
                  
            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 
      
            temp = self.__minValueNode(root.right) 
      
            root.value = temp.value 
      

            root.right = self.__deleteNode(root.right , temp.value) 
      
      
        return root  

    #-------------------------Searching---------------
    def __newsplay(self,value):
       self.__delete(value)
       self.Insert(value)
        
    def Search(self,value):
        self.__newsplay(value)
        if value==self.root.value:
            print("value found")
            return self.root.value
        else:
            print("value not found")


    #-------BST---Pre-Order------ 
    def PreOrder(self):
        return self.__PreOrder(self.root)
    def __PreOrder(self,x):
        if x:
            print(x.value)
            self.__PreOrder(x.left)
            self.__PreOrder(x.right)



#------------Driver-Code--------------
a = SplayTree()
#---Insertion----
#a.Insert(23)
#a.Insert(30)
#a.Insert(45)
#a.Insert(1)
#a.Insert(5)
#----Searching----
#a.Search(5)
#----Deletion-----
#a.BottomUpDelete(23)
#a.TopDownDelete(23)
#---Pre-Order----
#a.PreOrder()
