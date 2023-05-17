# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 02:50:24 2022

"""

# this file is for analyzing.
# fin_main.py is to import this file.

# this file make & load JSON file.
# fin_main.py will load the JSON file.

# fin_main.py might be replaced by GUI app with wxpython.

# this file is made with function.

########################################



# if __name__=="__main__":
import MeCab
import json


# load the file & analyze & make/overwrite JSON
def analyze(file_path, filename, JSON_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        text = f.read()
    
    
        # analyze
        mt = MeCab.Tagger()
                
        node = mt.parseToNode(text)
        
        ignorePOS={"助詞","連体詞","助動詞","副詞","接続詞","補助記号"}
        ignoreWords={"*","こと","事","ない","無い","する"}
        data={}
        
        while node:
            nf = node.feature.split(',')
            if nf[0] not in ignorePOS and nf[10] not in ignoreWords:
                if nf[10] in data:
                    data[nf[10]]+=1
                else:
                    data.setdefault(nf[10],1)
            node=node.next
        
        #print(data)
    # read JSON, to dict 
    with open(JSON_path, mode="r", encoding="utf-8") as f:
        Jr=json.load(f)

    
    # overwite JSON
    with open(JSON_path, mode="w", encoding="utf-8") as f:
        if filename in Jr:
            Jr[filename]=data
        else:
            Jr.setdefault(filename,data)
            
        Jr=json.dumps(Jr,ensure_ascii=False)
        
        f.write(Jr)
    

# defect the similar
def similar(filename, JSON_path):
    print("the result of analysis")
    with open(JSON_path, mode="r", encoding="utf-8") as f:
        Jr=json.load(f)
        obj_dict=Jr[filename] # dict of the file
        #print(obj_dict)
        dict_sim={}
        
        
        for i in Jr:
            if i != filename:
                compared = Jr[i]    #compared dict
                n_sim=0
                dict_sim[i]=[]
                dict_sim[i].append({})   
                
                # compare & make dict => {compared(i):[{sentence(a) : similar(cnt),,}, sum of sim(n_sim)]}
                
                for a in obj_dict:
                    if a in compared:
                        cnt = min(compared[a],obj_dict[a])
                        dict_sim[i][0][a]=cnt
                        n_sim+=cnt
                        
                dict_sim[i].append(n_sim)
                
                if n_sim==0:
                    del dict_sim[i]
        #print(dict_sim)
        return dict_sim
        

    
def for_overwiteJSON(file_path, filename,JSON_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        text = f.read()
    
    
        # analyze
        mt = MeCab.Tagger()
                
        node = mt.parseToNode(text)
        
        ignorePOS={"助詞","連体詞","助動詞","副詞","接続詞","補助記号"}
        ignoreWords={"*","こと","事","ない","無い","する"}
        data={}
        
        while node:
            nf = node.feature.split(',')
            if nf[0] not in ignorePOS and nf[10] not in ignoreWords:
                if nf[10] in data:
                    data[nf[10]]+=1
                else:
                    data.setdefault(nf[10],1)
            node=node.next
        
        #print(data)
        return data
    