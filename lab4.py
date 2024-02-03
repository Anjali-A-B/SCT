#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 4. Write a program to implement De-Morgan’s Law in Fuzzy sets.

Z = {}

def union(A, B):
    Z = {}
    for x in A and B:
        Z[x] = max(A[x],B[x])
    return Z

def complement(X):
    Z = {}
    for x in X:
        Z[x] = round(1 - X[x], 2)
    return Z

def intersection(A, B):
    for x in A and B:
        Z[x] = min(A[x], B[x])
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

# Applying De Morgan's law
LHS = complement(union(A, B))
RHS = intersection(complement(A), complement(B))

print("\nFuzzy Set A : ", A)
print("\nFuzzy Set B : ", B)
print("\nLHS (A U B)':", LHS)
print("\nRHS (A' ∩ B') : ", RHS)

if LHS == RHS:
    print("\nDe Morgan's law is proved \n Since {} = {}".format(LHS, RHS))
else:
    print("De Morgan's law is not proved")


# In[ ]:




