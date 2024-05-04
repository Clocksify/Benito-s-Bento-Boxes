import json

with open('Encrypted_data.json','r') as f:
    dic = json.load(f)

with open("Encrypted_query.txt", "r") as j:
    Encrypted_query = j.readlines()
    print(Encrypted_query)
    for line in Encrypted_query:
        For_real = line.strip()
        open("Response.txt","a").write(dic[For_real] + '\n')
