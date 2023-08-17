import random

st=input("Enter you message: ")
words=st.split(" ")

coding= input("1 for Coding and 0 for Decoding")
coding= True if (coding=="1") else False
print(coding)

if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))+ word[1:]+word[0]+ ''.join(random.choices('abcdefghijklmnopqrstuvwxyz',k=3))
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew= word[3:-3]
            stnew= stnew[-1]+ stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
