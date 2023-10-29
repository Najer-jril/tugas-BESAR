import json

json_file = open("db.json")
json_data = json.load(json_file)

n = int(input("absen:")) - 1
print(json_data[n])

json_file.close()