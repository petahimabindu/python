s=input("enter a string:")
vowels="aeiouAEIOU"

v=sum(c in vowels for c in s)
c=sum(c.isalpha()and c not in vowels for c in s)

print("Vowels:",v)
print("Consonents:",c)
