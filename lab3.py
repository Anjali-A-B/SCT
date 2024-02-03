#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3. Write a Program to implement Union, Intersection and Complement operations in fuzzy set.

Z = {}

def union(A, B):
    for x in A and B:
        Z[x] = max(A[x], B[x])
    return Z

def intersection(A, B):
    for x in A and B:
        Z[x] = min(A[x], B[x])
    return Z

def complement(X):
    for x in X:
        Z[x] = round(1 - X[x],2)
    return Z

def get_membership_value(key):
    while True:
     
        value = float(input(f"Enter the Membership value (between 0 and 1) for {key}: "))
        if 0 <= value <= 1:
            return value
        else:
            print("Invalid input. Please enter a value between 0 and 1.")
                
A = {}
B = {}

no_items_A = int(input("Enter the number of elements for fuzzy set A: "))
for _ in range(no_items_A):
    key = input("Enter the crispy set elements for A: ")
    value = get_membership_value(key)
    A[key] = value

no_items_B = int(input("Enter the number of elements for fuzzy set B: "))
for _ in range(no_items_B):
    key = input("Enter the crispy set elements for B: ")
    value = get_membership_value(key)
    B[key] = value


print("\nResults:")
print("\nA : ",A)
print("\nB : ",B)
print(f"\nA UNION B: {union(A, B)}")
print(f"\nA INTERSECTION B: {intersection(A, B)}")
print(f"\nCOMPLIMENT OF A: {complement(A)}")
print(f"\nCOMPLIMENT OF B: {complement(B)}")


# In[ ]:




