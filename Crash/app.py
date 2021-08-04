import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon")

# print(response.json())

# res names
# map len()

# res = json.loads(dict(response.json()))
# print(res)

d = response.json()
# print(d["results"])

results = d["results"]

maped = map(lambda x: len(x["name"]), results)
# print(list(maped))

# cnt = 0
# for n in list(maped):
#     cnt += n

# print(cnt)

# print(len(results))


print("Results: {0}\nTotal {1} pokemons\nCount: {2}".format(
    results, len(results), d["count"]))

dict = {}
# for n in range(1, 20):
#     dict[n] = 0

for pok in results:
    if dict.get(len(pok["name"])) is None:
        dict[len(pok["name"])] = 1
    else:
        dict[len(pok["name"])] = dict[len(pok["name"])] + 1

    print(
        "Pokeman - name: {0}; name length: {1}; name count: {2}".format(pok["name"], len(pok["name"]), dict[len(pok["name"])]))


#[6, 7, 8, 9, 10]
print(dict)

# filtered = filter(lambda x: len(x["name"]) == 9, results)
# print(list(filtered))

# filtered = filter(lambda x: dict[x] > 0, dict)
# print(list(filtered))

# list of names


# sort by name length

# print(results.sort())

poks = []
for pok in results:
    # print(pok)
    pok["namelen"] = len(pok["name"])
    poks.append(pok)

print("poks:\n", poks)


# def getNameLen(el):
#     return len(el["name"])


print(poks.sort(key=namelen))

# print(poks.sort())
