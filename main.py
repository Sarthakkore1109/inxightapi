import json

import requests
from requests.structures import CaseInsensitiveDict

inXightCount = 18841
num = 0
startRange = 0
#num = 16910
#startRange = 1961
url = f"https://drugs.ncats.io/api/v1/structures?skip={num}"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

for i in range(startRange, inXightCount):
    resp = requests.get(url, headers=headers)
    results = resp.json()
    with open(f"data/{num}.txt", "w") as output:
        #output.writelines(results['content'])
        dict = results['content']
        json_object = json.dumps(dict, indent=4)
        output.write(json_object)
        print("entries" + str(num))

    num += 10

print('done')
