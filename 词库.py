from os import replace
from unicodedata import decimal
import pinyin

with open("symbol.txt", "a"):
    pass
with open("han.txt", "a"):
    pass

def read_dict():
    global pinyin_dict, han_dict
    pinyin_dict = {}
    han_dict={}
    with open("symbol.txt", "r") as text:
        pinyin_list_old = text.read().split('\n')
    while '' in pinyin_list_old:
        pinyin_list_old.remove('')
    for i in pinyin_list_old:
        pinyin_dict[i.split(' ')[0]] = i.split(' ')[1]

    with open("han.txt", "r") as text:
        han_list_old = text.read().split("\n")
    while '' in han_list_old:
        han_list_old.remove('')
    for i in pinyin_list_old:
        pinyin_dict[i.split(' ')[0]] = i.split(' ')[1]

def add(char_han,symbol,mode): #中文意思 符号 模式(1为全拼，2为首字母，或者直接输入缩写)
    global pinyin_dict,han_dict
    if mode=='1':
        pinyin_char=pinyin.get(char_han.split('-')[1],format='strip')
        pinyin_type=pinyin.get_initial(char_han.split('-')[0]).replace(" ",'')
        pinyin_dict['.'+pinyin_type+'-'+pinyin_char]=symbol
        han_dict[char_han+symbol] = '.'+pinyin_type+'-'+pinyin_char
    elif mode=='2':
        pinyin_char = pinyin.get_initial(char_han).replace(' ','')
        pinyin_dict['.'+pinyin_char] = symbol
        han_dict[char_han+symbol] ='.'+pinyin_char
    else:
        pinyin_type = pinyin.get_initial(char_han.split('-')[0]).replace(" ", '')
        pinyin_dict['.'+pinyin_type+'-'+mode] = symbol
        han_dict[char_han+symbol] ='.'+pinyin_type+'-'+mode

def write_dict():
    global pinyin_dict, han_dict
    with open("symbol.txt",'w') as f:
        # pinyin_dict=sorted(pinyin_dict)
        for i in pinyin_dict:
            f.write(i+' '+pinyin_dict[i]+'\n')
    with open("han.txt",'w') as f:
        # han_dict=sorted(han_dict)
        for i in han_dict:
            f.write(i+' '+han_dict[i]+'\n')

read_dict()
# add_item = input("请输入要添加的字符\n格式：类别-中文汉字 符号 模式(1为全拼，2为首字母，或者直接输入缩写)\n例子：方向-左 ← 1\n").split(' ')
# add(add_item[0],add_item[1],add_item[2])
with open("symbol_word.txt",'r') as f:
    a=f.read().split('\n')
for i in a:
    i=i.split(' ')
    for j in range(1,3):
        add(i[0],i[1],str(j))

write_dict()



