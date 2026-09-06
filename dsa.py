# import ctypes

# # n=146
# # float=n/10
# # int=n//10
# # mod=n%10
# # mod=1%10
# # print(float)
# # print(int)
# # print(mod)



# # making a O(logn) TC program 

# # Q1: so the task is to convert an integer into a string
# # CODE 

# # def int_to_str(int):
# #     nums="0123456789"
# #     result=""
# #     if int==0:
# #        return print("0")
# #     else:
# #         while int>0:
# #            result=nums[int%10]+result
# #            int=int//10  # KEEP IN MIND MOSTLY  WHEN WE ARE DEVIDING THE LOOPS CHRACTER IN THS CASE INT WITH ANYTHING IT WOULD MOSTLY BE A logN case of TC 
# #     return result


# # str=int_to_str(124)

# # print(str)
# # print(type(str))




# # Q2: fiding TC 

# # CODE 
# # n=1000
# # j=2
# # i=n/2
# # k=0

# # while i<=n: # this loop will have time compllexity of n/2 as i=n/2 
# #    while j<=n: # this inner loop will have Tc OF LOGN BECAUSE THE J IS INCREASNG WITH A MULTIPLE OF 2 MEANNG 2^J EVEN IN 9 ITRATIONS IT WILL REACH 512 AND WONT RUN AGAIN 
# #       k=k+n/2
# #       j=j*2

# #    i+=i


# # SO N/2 *logn = O(nlogn)


# # Q3: reverse an array

# # CODE 

# # l=[1,2,3,4,5,33]
# # for i in range(0,len(l)//2):
# #     other=len(l)-i-1
# #     temp=l[i]
# #     l[i]=l[other]
# #     l[other]=temp

# # print(l)

# # Q: make a reursive function for a factorial
# # fctorial = 
# #    1!=1,
# #    2!=2x1=2
# #    3!=3x2x1=6
# #    4!=4x3x2x1=24

# # CODE 
# # def factorial(n):
# #     if n==1:
# #       return 1
# #     return n*factorial(n-1)

# # print(factorial(5))



# # makin a fbonci series 
# # Q: very number is the sum of the revious 2 numbers 

# # F.series 0,1,1,2,3,5,8,13,21
  
# # TC of EXPONENTIAL O(n^n) 

# # def fibonaci(n):
    
# #     if n==0 or n==1:
# #       return 1
    
# #     return (fibonaci((n-1))+fibonaci((n-2)))

# # print(fibonaci(6))







# # making an ARRAY DATA STRUCTURE OF MY OWN IN ORDER TO UNDERSTAND THE WOKING OF THE DYNAMIC AND REFRANTIAL ARRAYS AND THE OOPS
# # tasks

# # Dynamic array 
# # Creating the array 
# # len()
# # append()
# # print()
# # indexing
# # pop
# # clear
# # find uses index() function
# # insert
# # delete
# # remove

# class MyList:
#     def __init__(self):
#         self.size=1
#         self.n=0
#         self.A=self.__make_list__(self.size)


#     def __make_list__(self,capacity):
#         # this  special function will be called everytme a class is created
#         return (capacity*ctypes.py_object)()

#     # all the methods with __ in them like __len__ are called the magic functions and can be used like len(L) rater then L.len()
    
#     def __len__(self):
#         return self.n
    
#     def __getitem__(self,index):
#         if 0<=index<self.n:

#          return self.A[index]
#         return "IndexError--- Index out of  range"


#     def pop(self):
#         if self.n==0:
#          return "Error--list empty"
#         print(self.A[self.n-1])
#         self.n = self.n - 1
    
#     def append(self,new_element):
#         if self.size == self.n:
#             # resize by making a new array
#            self.__resize(self.size*2)
#         #if there is empty space then copy then add the new eleement to the existing array
#         self.A[self.n]=new_element
#         self.n=self.n+1

#     def clear(self):
#        self.n=0
#        self.size=1
          
#     def index(self,value):
#       for i in range(self.n):
#         if self.A[i]==value:
#           return i
       
#       return "valueError value not found " 

#     def insert(self,index,value):
#         if self.size==self.n:
              
#             self.__resize(self.size*2)
#         for i in range(self.n,index,-1):
#             self.A[i]=self.A[i-1]
            
#         self.A[index]=value
#         self.n=self.n+1
       

#     def __delitem__(self,index):
#         if index>self.n:
#            return "IndexError--limit exceeded"
#         for i in range(index,self.n-1):
#            self.A[i]=self.A[i+1]
#         self.n=self.n-1
           
           
           
       

           
#     def __str__(self):

#         result=""
#         for i in range(self.n):
#             result=result+str(self.A[i])+"," 
#         return "["+result[:-1]+"]"

#     def __resize(self,new_capacity):
#         # make a new array
#         B=self.__make_list__(new_capacity)
#         # add the new size of the array
#         self.size=new_capacity
#         for i in range(self.n):
#             B[i]=self.A[i]

#         self.A=B






# L=MyList()
# L.__make_list__(4)
    

# L.append(2)
# L.append("hello")
# L.append(3.4)
# L.append(9)
# L.append(7)
# # L.append("world")

# # print(len(L))
# # L.__str__()

# # print(L)
# # print(L)

# # L.pop()
# print(L)

# # L.clear()

# # print(L.index("hello"))
# # print(L)


# # L.insert(2,"World")

# del L[10]
# # print(L.__delitem__(10)) this will print the error the above wont because 
# # print(L)









# LINKED LIST 
# tasks to preform
# NODE class
# LL class
# len function
# insert from head
# traversal
# insert from tail append
# insert from middle

# clear 
# delete from head 
# delete from tail (pop)
# delete by value (remove)
# delete by index -> del L[0]

# search by value (find) 
# search by index (indexing)



# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.n=0
#         self.head=None

#     def __len__(self):
#         return self.n

#     # insertions
#     def insert_head(self,value):
#         new_node=Node(value)
#         new_node.next=self.head    
#         self.head=new_node
#         self.n=self.n+1


#     def append(self,value):

#         new_node=Node(value)
#         if self.head==None:
#             self.head=new_node
#             self.n=self.n
#             return

#         curr =self.head
#         while curr.next!=None: #if you want to stop before none curr.next if you want to stop 2nd last node then curr.next.next and so on
#             curr=curr.next
#         curr.next=new_node
#         self.n=self.n+1

    
#     def insert_middle(self,after_value,value):
#         new_node=Node(value)
#         if self.head==None:
#           self.head=new_node
#           self.n=self.n+1
#           return
#         curr=self.head

#         while curr!=None:
#              if curr.data==after_value:
#                 # print("value not found")
#                 break
#              curr=curr.next
#         if curr!=None:
#             new_node.next=curr.next
#             curr.next=new_node
#             self.n=self.n+1
#         else:
#             print("Value not found")

    
        

#     def traverse(self):

#         if self.n==0:
#             return "IndexError Linked List empty"
#         curr=self.head
#         result=""
#         while curr !=None:  
#            result =result+str(curr.data)+"->"
#            curr=curr.next # the while loop needs  an increment always
#         return result[:-2]

#     # deletions
#     def clear(self):
#          self.head=None
#          self.n=0

#     def delete_head(self):
#         if self.head==None:
#             return "IndexError linked list is empty"

#         self.head=self.head.next
#         self.n=self.n-1

#     def pop(self):
#         if self.head==None:
#                     return "IndexError linked list is empty"
        
#         curr=self.head
#         while curr.next.next!=None:
#             curr=curr.next
#         curr.next=None
#         self.n=self.n-1
#     def delete_by_value(self,value):
#         if self.head==None:
#             return "IndexError Linked List is empty"

        
#         if self.head.data==value:
#             self.head=self.head.next
#             return 

#         curr=self.head
        
#         while curr.next.data!= value:     
                  
#             curr=curr.next

#         curr.next=curr.next.next
#         self.n=self.n-1   


#     # def delete_by_index(self,index):


#     def __delitem__(self, key):
#         # print("exe 1")
#         curr=self.head
#         if self.head==None:
#             return "LinkedList empty"
#         if key==0:
#            self.head=self.head.next
#            return
#         index=0
#         while curr.next.next is not None:
            
#             if key-1==index:
#                curr.next=curr.next.next
#                print("exe 2")
#                return
            
#             curr=curr.next
#             index=index+1
        
#         print("exe 3")
#         curr.next=None
#         return "Limit Exceeded index not found"
        
         
#      #Searching 

#     def search_by_value(self,value):
#         curr=self.head
#         index=0
#         while curr is not None:
#             if curr.data ==value:
#                  return index
        
#             curr=curr.next
#             index=index+1
        
#     def search_by_index(self,index):
#         curr=self.head
#         iter=0

#         while curr is not None:
#             if iter==index:
#                 return curr.data
        
#             curr=curr.next
#             iter+=1

        
        

        






        
    



# a=LinkedList()

# a.insert_head(1)
# a.insert_head(2)
# a.insert_head(3)
# a.insert_head(4)
# a.insert_head(5)
# a.append(6)
# a.insert_middle(4,"hello")
# a.insert_middle("hello","world")

# # a.clear()
# # a.delete_head()
# # a.pop()
# # a.delete_by_value(5)


# # values 
# # print(a.search_by_value("hello"))
# # print(a.search_by_index(0))

# # print(len(a))
# print(a.traverse())
# # print(a)

# del a[0]
# print(a.traverse())



#  linked list test  question 
# Q1- write a python program to find the max value in a linked list adn replace it with the given value
# assume that the linked list is populated with whole numbers and there is only one maximum value in it 

# make a linked list 

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None


class LL:
    def __init__(self):
        self.head=None
        self.n=0


    def insert_head(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.n=self.n+1
            return
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
        


    def __len__(self):
        return self.n

    def traverse(self):
        if self.n==0:
            return "LL empty"
        curr=self.head
        result=""
        
        while curr!=None:
            
            result=result+str(curr.data)+"->"
            curr = curr.next
      
        return result[:-2]
    def Question1(self,value):
        if self.head==None:
            return "LL empty"
        curr=self.head
        new_node=Node(value)
        max=0
        for  i in range(self.n-1):
            if curr.next.data>=max:
                max=curr.next.data
                # print(curr.next)
                next_node=curr.next.next
                current_node_address=curr.next
                #inserting the node
                
            curr=curr.next
        
        new_curr=self.head
        # print("exe 1")
        # print(max)
        # print(next_node)
        # print(current_node_address)
        while new_curr!=None:

            if new_curr.next==current_node_address:
                # print(" if exe 1")
                new_curr.next=new_node
                # print(" if exe 2")
                new_node.next=next_node
                # print(" if exe 3")
                return

            new_curr=new_curr.next

    # Q2 make a function to return the sum of all the odd index values of LL
    def sum_odd(self):
        curr=self.head
        sum=0
        for i in range(self.n):
                if i % 2!=0:
                    sum=sum+curr.data
                curr=curr.next
        return sum
             
    def reverse(self):
        curr=self.head
        prev_node=None
        while curr!=None:
            next_node=curr.next
            curr.next=prev_node

            prev_node=curr
            curr=next_node
        self.head=prev_node





            
            



L=LL()

L.insert_head(5)
L.insert_head(2)
L.insert_head(6)
L.insert_head(4)
L.insert_head(7)
L.insert_head(3)
L.insert_head(1)
L.insert_head(0)

# L.traverse()
print(L.traverse())

# L.Question1(18)
# print(L.sum_odd())
L.reverse()

print(L.traverse())





