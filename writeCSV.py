import csv
import json

with open('data.json') as f:
    data = json.load(f)

def getFromData(current, section, index):
    try:
        ret = current[section][index]
    except IndexError:
        ret = None

    return ret

with open("data.csv", 'w', newline='') as f:
    csvWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csvWriter.writerow([
        "name", 
        "index", 
        "partner", 
        "move", 
        "moveFrequency", 
        "ability", 
        "abilityFrequency",
        "nature",
        "natureFrequency",
        "item",
        "itemFrequency"
    ])

    for x in data:
        name = x["name"]
        
        for i in range(0, 10):
            row = []

            row.append(name)

            row.append(i+1)

            row.append(getFromData(x, "partners", i))

            move = getFromData(x, "moves", i)
            if move is not None:
                for key in move:
                    row.append(key)
                    row.append(move[key])
            else:
                row.append(None)
                row.append(None)
            
            ability = getFromData(x, "ability", i)
            if ability is not None:
                for key in ability:
                    row.append(key)
                    row.append(ability[key])
            else:
                row.append(None)
                row.append(None)
                
            nature = getFromData(x, "nature", i)
            if nature is not None:
                for key in nature:
                    row.append(key)
                    row.append(nature[key])
            else:
                row.append(None)
                row.append(None)

            item = getFromData(x, "item", i)
            if item is not None:
                for key in item:
                    row.append(key)
                    row.append(item[key])
            else:
                row.append(None)
                row.append(None)

            csvWriter.writerow(row)
        