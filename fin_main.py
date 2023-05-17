# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 02:40:05 2022

@author: k0eov
"""

# this file might be replaced by GUI app with wxpython.
import fin_analysis
import glob
import json
import sys


JSON_path=glob.glob("*data_json.json")[0]

print("options")
print("1. make memo & show another memo similar to the memo")
print("2. overwrite the memo & show another memo similar to the memo")
print("3. analyze the memo & show another memo similar to the memo")
print("4. show all memo's name")
print("5. show the content of the memo")
print("6. update the system file (update JSON file) ")


# input option

while True:
    opt=input("enter number of above options : ")
    if opt in {"1","2","3","4","5","6"}:
        opt=int(opt)
        break
    else:
        print("invalid input!")


#load filename
filenames=set(glob.glob("*.txt"))


# opt finctions
def make_memo():
    while True:
        
        #filename
        memoname=input("enter the name of the memo :")
        if memoname in filenames:
            print("the file already exist")
            yn=input("stop this option? (y/n)")
            if yn=="y":
                return "@![]{}"
        else:
            break
        
    #file content
    print("enter the content of the memo (entering 'EOF' will stop the input)")
    memo_content=""
    while True:
        line=input(">>")
        if line == "EOF":
            memo_content.rsplit()
            break
        else:
            memo_content += line+"\n"
    
    #make .txt file
    memoname+=".txt"
    with open(memoname, mode="w", encoding="utf-8") as f:
        f.write(memo_content)
        
    return memoname


# the result of analysis
def result_of_analysis(filename, JSON_path):
    result=fin_analysis.similar(filename, JSON_path)
    
    result=sorted(result.items(), key = lambda k : k[1][1], reverse=True)
    #print(result)
    print("degree of similarity\tfilename\tpoints of similarity")
    
    for i in result:
        compared_filename = i[0]
        print(i[1][1],"\t",compared_filename,"\t",i[1][0])
        
   
    

def overwrite_memo(memoname):
    print("the previous content:")
    with open(memoname, encoding="utf-8") as f:
        txt=f.read()
        print(txt)
    memo_content=""
    while True:
        line=input(">>")
        if line == "EOF":
            memo_content.rsplit()
            break
        else:
            memo_content += line+"\n"
        with open(memoname, mode="w", encoding="utf-8") as f:
            f.write(memo_content)
        
    
# exec option

if opt == 1:
    tmp=make_memo()
    if tmp=="@![]{}":
        pass
    else:
        fin_analysis.analyze(tmp, tmp, JSON_path)
        
        
        result_of_analysis(tmp, JSON_path)
        
if opt==2:
    while True:
        fn=input("which memo do you overwrite? :")
        fn2=fn+".txt"
        if fn in filenames or fn2 in filenames:
            break
        else:
            print("such file doesn't exist")
            yn=input("stop this option? (y/n)")
            if yn=="y":
                sys.exit()
    if fn[-3:]!="txt":
        
        fn=fn2
    overwrite_memo(fn)
    fin_analysis.analyze(fn, fn, JSON_path)
    result_of_analysis(fn, JSON_path)
    
if opt==3:
    while True:
        fn=input("which memo do you analyze? :")
        fn2=fn+".txt"
        if fn in filenames or fn2 in filenames:
            break
        else:
            print("such file doesn't exist")
            yn=input("stop this option? (y/n)")
            if yn=="y":
                sys.exit()
    if fn[-3:]!="txt":
        fn=fn2
    fin_analysis.analyze(fn, fn, JSON_path)
    result_of_analysis(fn, JSON_path)
    
    
    
    
if opt==4:
    for i in filenames:
        print(i)
        
if opt==5:
    while True:
        fn=input("which memo do you want to know about? :")
        fn2=fn+".txt"
        if fn in filenames or fn2 in filenames:
            break
        else:
            print("such file doesn't exist")
            yn=input("stop this option? (y/n)")
            if yn=="y":
                sys.exit()
    if fn[-3:]!="txt":
        fn=fn2
    with open(fn, encoding="utf-8") as f:
        txt=f.read()
        print(txt)

if opt==6:
    datam={}
    for i in filenames:
        
        datam[i]=fin_analysis.for_overwiteJSON(i, i, JSON_path)
    with open(JSON_path, mode="w", encoding="utf-8") as f:
        datam=json.dumps(datam,ensure_ascii=False)
    
        f.write(datam)


"""

file_path=glob.glob("*sumple1.txt")[0]
json_path=glob.glob("*data_json.json")[0]

with open(json_path, mode="r", encoding="utf-8") as f:
        Jr=json.load(f)
print(Jr)

fin_analysis.analyze(file_path,file_path,json_path)

fin_analysis.similar(file_path, json_path)
"""