import ctypes

# n=146
# float=n/10
# int=n//10
# mod=n%10
# mod=1%10
# print(float)
# print(int)
# print(mod)



# making a O(logn) TC program 

# Q1: so the task is to convert an integer into a string
# CODE 

# def int_to_str(int):
#     nums="0123456789"
#     result=""
#     if int==0:
#        return print("0")
#     else:
#         while int>0:
#            result=nums[int%10]+result
#            int=int//10  # KEEP IN MIND MOSTLY  WHEN WE ARE DEVIDING THE LOOPS CHRACTER IN THS CASE INT WITH ANYTHING IT WOULD MOSTLY BE A logN case of TC 
#     return result


# str=int_to_str(124)

# print(str)
# print(type(str))




# Q2: fiding TC 

# CODE 
# n=1000
# j=2
# i=n/2
# k=0

# while i<=n: # this loop will have time compllexity of n/2 as i=n/2 
#    while j<=n: # this inner loop will have Tc OF LOGN BECAUSE THE J IS INCREASNG WITH A MULTIPLE OF 2 MEANNG 2^J EVEN IN 9 ITRATIONS IT WILL REACH 512 AND WONT RUN AGAIN 
#       k=k+n/2
#       j=j*2

#    i+=i


# SO N/2 *logn = O(nlogn)


# Q3: reverse an array

# CODE 

# l=[1,2,3,4,5,33]
# for i in range(0,len(l)//2):
#     other=len(l)-i-1
#     temp=l[i]
#     l[i]=l[other]
#     l[other]=temp

# print(l)

# Q: make a reursive function for a factorial
# fctorial = 
#    1!=1,
#    2!=2x1=2
#    3!=3x2x1=6
#    4!=4x3x2x1=24

# CODE 
# def factorial(n):
#     if n==1:
#       return 1
#     return n*factorial(n-1)

# print(factorial(5))



# makin a fbonci series 
# Q: very number is the sum of the revious 2 numbers 

# F.series 0,1,1,2,3,5,8,13,21
  
# TC of EXPONENTIAL O(n^n) 

# def fibonaci(n):
    
#     if n==0 or n==1:
#       return 1
    
#     return (fibonaci((n-1))+fibonaci((n-2)))

# print(fibonaci(6))







# making an ARRAY DATA STRUCTURE OF MY OWN IN ORDER TO UNDERSTAND THE WOKING OF THE DYNAMIC AND REFRANTIAL ARRAYS AND THE OOPS
# tasks

# Dynamic array 
# Creating the array 
# len()
# append()
# print()
# indexing
# pop
# clear
# find uses index() function
# insert
# delete
# remove

class MyList:
    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_list__(self.size)


    def __make_list__(self,capacity):
        # this  special function will be called everytme a class is created
        return (capacity*ctypes.py_object)()

    # all the methods with __ in them like __len__ are called the magic functions and can be used like len(L) rater then L.len()
    
    def __len__(self):
        return self.n
    
    def __getitem__(self,index):
        if 0<=index<self.n:

         return self.A[index]
        return "IndexError--- Index out of  range"


    def pop(self):
        if self.n==0:
         return "Error--list empty"
        print(self.A[self.n-1])
        self.n = self.n - 1
    
    def append(self,new_element):
        if self.size == self.n:
            # resize by making a new array
           self.__resize(self.size*2)
        #if there is empty space then copy then add the new eleement to the existing array
        self.A[self.n]=new_element
        self.n=self.n+1

    def clear(self):
       self.n=0
       self.size=1
          
    def index(self,value):
      for i in range(self.n):
        if self.A[i]==value:
          return i
       
      return "valueError value not found " 

    def insert(self,index,value):
        if self.size==self.n:
              
            self.__resize(self.size*2)
        for i in range(self.n,index,-1):
            self.A[i]=self.A[i-1]
            
        self.A[index]=value
        self.n=self.n+1
       

    def __delitem__(self,index):
        if index>self.n:
           return "IndexError--limit exceeded"
        for i in range(index,self.n-1):
           self.A[i]=self.A[i+1]
        self.n=self.n-1
           
           
           
       

           
    def __str__(self):

        result=""
        for i in range(self.n):
            result=result+str(self.A[i])+"," 
        return "["+result[:-1]+"]"

    def __resize(self,new_capacity):
        # make a new array
        B=self.__make_list__(new_capacity)
        # add the new size of the array
        self.size=new_capacity
        for i in range(self.n):
            B[i]=self.A[i]

        self.A=B






L=MyList()
L.__make_list__(4)
    

L.append(2)
L.append("hello")
L.append(3.4)
L.append(9)
L.append(7)
# L.append("world")

# print(len(L))
# L.__str__()

# print(L)
# print(L)

# L.pop()
print(L)

# L.clear()

# print(L.index("hello"))
# print(L)


# L.insert(2,"World")

del L[10]
# print(L.__delitem__(10)) this will print the error the above wont because 
# print(L)


















