def getText():
    txt = open('fenci.txt','r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch,' ')
    return txt

txt = getText()
words = txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1   # 注意dict.get()用法
items = list(counts.items())  # 转换成列表类型
# print(items)
items.sort(key = lambda x:x[1], reverse = True)  # 对列表按value从大到小排序
for i in range(10):
    word, count = items[i]
    print(word,count)
