import sys
import json
from tqdm import tqdm

unprocessed_data_path=sys.argv[1]
with open(unprocessed_data_path,'r',encoding='utf-8') as f:
    unprocessed_data=json.load(f)

may_repeated=[]
for dic in tqdm(unprocessed_data):
    for value in dic.values():
        flag=False
        value=value.replace(" ","")
        for i in range(1,len(value)//3+1):
            for j in range(len(value)-i*3+1):
                if(value[j:j+i]==value[j+i:j+2*i]==value[j+2*i:j+3*i]):
                    flag=True
                    break        
            if(flag):
                break
        if(flag):
            may_repeated.append(dic)
            break
for i in may_repeated:
    unprocessed_data.remove(i)

with open('data_without_repeated.json','w',encoding='utf-8') as f:
    json.dump(unprocessed_data,f,ensure_ascii=False,indent=4)