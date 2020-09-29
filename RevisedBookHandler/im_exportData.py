

def createDictionaryFromFile(filename):
    file = open(filename);
    dictQ = [];
    params = file.readline().strip().split(',');
    slots = {}
    counter = 0;
    for line in file.readlines():
        if line.strip() == "":
            continue;
        if counter == len(params):
            counter = 0;
            dictQ.insert(len(dictQ),slots);
            slots = {};
        line = line.strip();
        slots[params[counter]] = line;
        counter += 1;
    file.close();
    #print(dictQ);
    return (filename.split('.')[0],dictQ);


def saveToFile(t): #param is above tuple
    print(t);
    filename = t[0] + "1.txt";
    file = open(filename,'w');
    return;



if __name__ == '__main__':
    saveToFile(createDictionaryFromFile('generalInfo.txt'))
