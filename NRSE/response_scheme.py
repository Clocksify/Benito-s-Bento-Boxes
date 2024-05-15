import json

with open('Benito-s-Bento-Boxes/NRSE/EQ_to_EQR_dict.json','r') as f:
    dic = json.load(f)

open('Benito-s-Bento-Boxes/NRSE/Response.txt',"w").close()

with open("Benito-s-Bento-Boxes/NRSE/Encrypted_query.txt", "r") as j:
    Encrypted_query = j.readlines()
    print(Encrypted_query)
    for line in Encrypted_query:
        For_real = line.strip()
        Response = dic[For_real]
        Response_list.append(Response)
        for lines in Response_list:
            Response1 = lines.strip()
            open('Benito-s-Bento-Boxes/NRSE/Response.txt',"a").write((Response1))
            open('Benito-s-Bento-Boxes/NRSE/Response.txt',"a").write('\n')

