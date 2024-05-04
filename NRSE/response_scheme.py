import json

with open('NRSE/Encrypted_data.json','r') as f:
    dic = json.load(f)

print (dic)

with open("NRSE/Encrypted_query.txt", "r") as j:
    Encrypted_query = j.readlines()
    print(Encrypted_query)
    print (type(Encrypted_query))
    for line in Encrypted_query:
        For_real = line.strip()
        open("Response.txt","w").write(dic[For_real] + '\n')
