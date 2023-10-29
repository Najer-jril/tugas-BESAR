import json

inputnim = input("masukkan nim : ")
input = inputnim
prodi = input[0] + input[1]

with open("db.json", "r") as file:
    data = json.load(file)
    for i in data[prodi]:
        if i["NIM"] == input:
            print(i)