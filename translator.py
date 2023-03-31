import sys
import json
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,pipeline

model_name=sys.argv[1]
source_data_path=sys.argv[2]

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator=pipeline("translation",model=model,tokenizer=tokenizer)



def translate(scentence):
    scentences=scentence.split('\n')
    result=''
    for i in range(len(scentences)):
        if(len(scentences[i])!=0):
            result+=translator(scentences[i])[0]['translation_text']
        if(i!=len(scentences)-1):
            result+='\n'
    return result



with open(source_data_path) as f:
    source_data=json.load(f)



translated_data=[]
for dic in tqdm(source_data):
    temp={}
    for key,value in dic.items():
        if(len(value)==0):    
            temp[key]=value
            continue
        temp[key]=translate(value)
    translated_data.append(temp)



with open('translated_data.json','w') as f:
    json.dump(translated_data,f,ensure_ascii=False,indent=4)
