


#def test(numbers):
#      parni_stack = []
#      nonparni_stack = []
#      for num in numbers: 
#         if num % 2 == 0:
#            parni_stack.append(num)
#         else:
#            nonparni_stack.append(num)
#      return parni_stack, nonparni_stack

#stack = []
#add = int(input("Amount: "))

#for i in range(add):
#        num =int(input("Numbers: "))
#        stack.append(num)
#def print_stack(stack_name, stack):
#        print(f"{stack_name} stack: {stack}") 

#parni, nonparni = test(stack)

#print_stack("Couples", parni) 
#print_stack("Not couples", nonparni) 

queue = [] 
ar = int(input("Amount: "))
for i in range(ar):
    num = int(input("Numbers: "))
    queue.append(num)
    
print("__________")
print("Initial queue")
print(queue)
  
print("\nElements dequeued from queue")
for i in range(ar):
   print(queue.pop(0))
   print(queue)
   print("__________")

print("queue after removing elements")
print(queue)
