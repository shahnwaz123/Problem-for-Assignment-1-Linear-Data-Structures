# 1- Write a program to find all pairs of an integer array whose sum is equal to a given number?
class Pairs():
    def __init__(self, sum, n, arr ):

        self.sum = sum
        self.n = n
        self.arr = arr
        
    
    def find_pairs(self):
        
       
        for i in range(0, self.n):
            for j in range(i+1, self.n):
                if (self.arr[i] + self.arr[j] == self.sum):
                    
                    print("(", self.arr[i], ",", " ", self.arr[j], ")", sep = "")

def Main():
    sum = int(input("Enter the sum for array elements: "))
   
    arr = [1, 5, 7, -1, 5, 4, 6, 8]
   
    n = len(arr)
   
    obj_Pairs = Pairs(sum, n, arr)
    obj_Pairs.find_pairs()

if __name__ == "__main__":
    Main()

# 2-  Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverselist(A, start, end):
    while start<end:
        A[start], A[end] = A[end], A[start]
        start+=1
        end-=1
A = [1,2,3,4,5,6]
print(A)
reverselist(A, 0, 5)
print("Reverselist is")
print(A)

# 3-  Write a program to check if two strings are a rotation of each other?
def arerotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    if size1 != size2:
        return 0
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

# 4-Write a program to print the first non-repeated character from a string
N0_OF_CHARS = 256
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+=1
    return count

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k=0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k+=1
    return index
string = "edyoda"
index = firstNonRepeating(string)
if index == 1:
    print(" either all characters are repeating or string is empty")
else:
    print("first non repeating character is"+ string[index])

# 5-Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n==1:
        print("move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("move disk",n,"from_rod",from_rod,"to_rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
n=4
TowerOfHanoi(n,'A','C','B')

 # 6-Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
s = "*-A/BC-/AKL"
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
s = s[::-1]
for i in s:
    if i in operators:
        a = stack.pop()
        b = stack.pop()
        temp = a+b+i
        stack.append(temp)
    else:
        stack.append(i)
print(*stack)

# 7-Write a program to convert prefix expression to infix expression
def prefixToinfinix(prefix):
    stack = []
    i=len(prefix) - 1
    while i >=0:
        if not isOperator(prefix[i])
        stack.append(prefix[i])
        i-=1
    else:
        str = "("+ stack.pop() + prefix[i] + stack.pop() +")"

    return stack.pop()

def isOperator(c):
    if c == "*" or c== "+" or c =="-" or c = "/" or c = "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToinfinix(str))

# 8-Write a program to check if all the brackets are closed in a given code snippet.
def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")

# 9-Write a program to reverse a stack.
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
        def createStack():
    stack = []
    return stack

def isEmpty( stack ):
    return len(stack) == 0
def push( stack, item ):
    stack.append( item )
def pop( stack ):
    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()

stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)

# 10-Write a program to find the smallest number using a stack.
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)
     
    __repr__ = __str__
 
 
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
         
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))
         
    __repr__=__str__

    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
 
 
def isEmpty(self):
    if self.top == None:
            return True
        else:
        
            return False
 
def __len__(self):
    self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count
 
def peek(self):
     if self.top is None:
            print ("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
 
    
    
def push(self,value):
    if self.top is None:
            self.top = Node(value)
            self.minimum = value
        
    elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))     
    
 
def pop(self):
    if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print ("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))


