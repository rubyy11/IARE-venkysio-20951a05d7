import threading
# import timeit

def wordReversal(string, i):
    string[i] = string[i][::-1]

def stringReversal(string):
    for i in range(len(string)):
        threads = threading.Thread(target=wordReversal, args=(string, i))
        threads.start()
    print("Reversed String : " , *string)
    exit()

print("Enter the String : ")
stringList = list(map(str,input().split()))
reversedString = stringReversal(stringList[::-1])





