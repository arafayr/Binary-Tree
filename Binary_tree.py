#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Binary search tree

class Node:
    def __init__ (self,data,parent):
        
        self.data = data
        self.lefthcild = None
        self.righthcild = None
        self.parent = parent
        
class binarysearchtree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data, None)
            
        else:
            
            self.insert_node(data, self.root)
            
            
    def insert_node(self, data, root):
        
        if data < root.data:
            
            #agar to data less than hai bilkul to leaf node banega to ik na ik bar ye statement false honi hai
            if root.lefthcild is not None:
                self.insert_node(data, root.lefthcild)
                
            else:
                #asal me data ye store karega ku ke left most node banega data
                root.lefthcild = Node(data, root)
        else:
            if root.righthcild is not None:
                self.insert_node(data, root.righthcild)
                
            else:
                root.righthcild = Node(data, root)
                
                
                
                
    def traverse(self):
        if self.root is not None:
            
            self.traverse_lrR(self.root)
            
    def traverse_lrR(self,root):
        if root.lefthcild is not None:
            self.traverse_lrR(root.lefthcild)
            
        
        print(root.data)
        if root.righthcild is not None:
            self.traverse_lrR(root.righthcild)
            
           
        
    def maxvalue(self):
        if self.root is not None:
            #jo value function ke name me store huiwi hai us ko return kara dia
            return self.max_diff(self.root)
    
    
    def max_diff(self,root):
        
        if root.righthcild:
            
            #ye line har right child ki value return karwayegi 4,6,7,200 ese ye ja kar store hogi function ke name me
            #agar return na hota to bs function ko call jati actual return na hota
            return self.max_diff(root.righthcild)
        #pura if khattam hone ke bad jo sab se akhiri value root parameter me hogi wo pakar kar return kara di
        #wo function ke name me store hogi      
        #phir upper jao
        return root.data
    def max_easy(self,root):
        
        
        
        while root.righthcild:
                root = root.righthcild
        return root.data
                
        
        
    def remove(self,data):
        if self.root:
            self.remove_Node(data,self.root)
                
    def remove_Node(self,data,root):
        
        if root is None:
            return
        
        if data < root.data:
            self.remove_Node(data,root.lefthcild)
            #is me return karane ki zaroorat nahe cuz jese hi base case hit karega
            #if se bahar ajayega else par chala jayega waha min most value pakarli jayegi
        elif data > root.data:
            self.remove_Node(data,root.righthcild)
        else:
            #removing leaf Node
            if root.lefthcild is None and root.righthcild is None:
                #leaf Node ka parent
                parent = root.parent
                 
                if parent is not None and parent.lefthcild == root:
                    parent.lefthcild = None

                if parent is not None and parent.righthcild == root:
                    parent.righthcild = None
                    
                if parent is None:
                    self.root = None
                    
                #deleting the actual Node pura ka pura with left right parent
                del root
            elif root.lefthcild is None and root.righthcild is not None:
                parent = root.parent
                
                if parent is not None:
                    if parent.lefthcild == root:
                        parent.lefthcild = root.righthcild
                    if parent.righthcild == root:
                        parent.righthcild = root.righthcild
                else:
                    self.root =  root.righthcild
                #informing root.rightchild that its parent is what is stored in parent variable
                root.righthcild.parent = parent
                del root
            elif root.lefthcild is not None and root.righthcild is None:
                parent = root.parent
                
                if parent is not None:
                    if parent.lefthcild == root:
                        parent.lefthcild = root.lefthcild
                    if parent.righthcild == root:
                        parent.righthcild = root.lefthcild
                        
                else:
                    self.parent = root.lefthcild
                    
                root.lefthcild.parent = parent
                
            else:
                #we know we are removing a Node with two child
                
                alternate = self.getalternate(root.lefthcild)
                
                temp = alternate.data
                alternate.data = root.data
                root.data = temp
                
                self.remove_Node(data,alternate)
                
    #def test(self):
        #alternate = self.getalternate(self.root.lefthcild)        
        #print(alternate.data)
        
        
    def getalternate(self,root):
            if root.righthcild:
                self.getalternate(root.righthcild)
            return root
                
                    
    def compare_bst(self,bst1,bst2):
        
        if bst1 is None or bst2 is None:
            return bst1 == bst2
        
        if bst1.data is not bst2.data:
            return False
        
        return self.compare_bst(bst1.lefthcild,bst2.lefthcild) and self.compare_bst(bst1.righthcild,bst2.righthcild)
        
obj = binarysearchtree()




obj.insert(10)
obj.insert(11)
obj.insert(12)
obj.insert(16)
obj.insert(5)
obj.insert(2)
obj.insert(1)
obj.insert(3)
obj.insert(4)




obj.remove(1)
obj.remove(10)
obj.remove(4)

obj.traverse()

print("-------------------------------------------------------------------------------------")
obj1 = binarysearchtree()

obj1.insert(10)
obj1.insert(11)
obj1.insert(12)
obj1.insert(16)
obj1.insert(5)
obj1.insert(2)
obj1.insert(1)
obj1.insert(3)
obj1.insert(4)

obj2 = binarysearchtree()




obj2.insert(10)
obj2.insert(11)
obj2.insert(12)
obj2.insert(16)
obj2.insert(5)
obj2.insert(2)
obj2.insert(1)
obj2.insert(3)
obj2.insert(4)

comparator = binarysearchtree()
comparator.compare_bst(obj1.root,obj2.root)


# In[ ]:




