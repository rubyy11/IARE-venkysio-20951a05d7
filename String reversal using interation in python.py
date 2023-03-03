import timeit

def string_reversal(l):
    stg=''
    start = timeit.default_timer()      
    for i in l[::-1]:
        char = char_reversal(i)
        stg += char
        stg += " "
    end = timeit.default_timer()
    result = "Reversed String : " + stg + 'and Time taken : ' + str(end-start)
    return result
def char_reversal(string):
    return string[::-1]
print("Enter the String")
l=list(map(str,input().split()))
print(string_reversal(l))
