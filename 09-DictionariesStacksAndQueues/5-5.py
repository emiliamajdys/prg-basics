paragraph = "cat dog mouse cat rat cat mouse"

words=paragraph.split()

count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1

for word, county in count.items():
    print(f'{word}:{county}')