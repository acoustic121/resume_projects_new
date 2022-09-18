import pandas as pd
data1=pd.read_excel("jan_alerts.xlsx")
s=data1["Message"]
message_list=list(s)
sentence_split_list=[]
for x in message_list:
    sentence_split_list.append(x.split())
filtered_list=[]
for x in sentence_split_list:
    if "REALERT" not in x and "New,ticket" not in x:
        filtered_list.append(x)
data2=pd.read_excel("client_ids_new.xls")
d=data2["client_id"]
client_list=list(d)

for i in client_list:
    for j in filtered_list:  
        if i in j:
            string3= '*'+i
            j.append(string3)
            #print(j) 
final_list=[]
for x in filtered_list:
    final_list.append(','.join(x))
#print(final_list[:10])   

df = pd.DataFrame(final_list)
writer = pd.ExcelWriter('aug_list_new.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()
            
