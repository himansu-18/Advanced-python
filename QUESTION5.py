s=input("enter a string")
freq={}

for ch in s:
     if ch in freq:
         freq[ch]+=1
     else:
         freq[ch]=1

print("character frequencies")
 for ch,count in freq.item():
     print(ch,":",count)
            