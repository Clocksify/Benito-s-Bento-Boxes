import json

with open('Benito-s-Bento-Boxes/NRSE/EQ_to_EQR_dict.json','r') as f:
    dic = json.load(f)

open('Benito-s-Bento-Boxes/NRSE/Response.txt',"w").close()

with open("Benito-s-Bento-Boxes/NRSE/Encrypted_query.txt", "r") as j:
    Encrypted_query = j.readlines()
    for line in Encrypted_query:
        encrypted_attr = line.strip()
        Response = dic[encrypted_attr]
        for lines in Response:
            Response1 = lines.strip()
            open('Benito-s-Bento-Boxes/NRSE/Response.txt',"a").write((Response1))
            open('Benito-s-Bento-Boxes/NRSE/Response.txt',"a").write('\n')

