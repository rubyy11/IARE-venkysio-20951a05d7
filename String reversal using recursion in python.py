import timeit
string = input("Enter string : ")

def string_reversal(string):
    if  len(string)==0:
        return
    temp = string[0]
    string_reversal(string[1:])
    print(temp,end="")
start = timeit.default_timer()
print("Reversed string : ",end="")
string_reversal(string)
end = timeit.default_timer()
print()
print("Time taken : ",end-start)





