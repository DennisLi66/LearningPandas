

def createDictionaryFromFile(filename):
    file = open(filename);
    dictQ = [];
    params = file.readline().strip().split(',');
    slots = {}
    counter = 0;
    for line in file.readlines():
        if line.strip() == "":
            continue;
        line = line.strip();
        slots[params[counter]] = line;
        counter += 1;
        if counter == len(params):
            counter = 0;
            dictQ.insert(len(dictQ),slots);
            slots = {};
    file.close();
    # print(dictQ);
    return (filename.split('.')[0],dictQ);


def saveToFile(t): #param is above tuple
    # print(t);
    filename = "databases/" + t[0] + ".txt";
    file = open(filename,'w');
    file.write(",".join(t[1][0].keys()) + "\n");
    # print(t);
    for d in t[1]:
        for v in d.values():
            file.write(v + "\n")
    file.close();
    return;



if __name__ == '__main__':
    saveToFile(createDictionaryFromFile('generalInfo.txt'))
