def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams")
    else:
        print("The strings aren't anagrams")         
s1 =input("enter string1:")
s2 =input("enter string1:")
check(s1, s2)
