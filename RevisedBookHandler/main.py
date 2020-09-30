import pandas as pd;
import im_exportData as imex;

def obtainInfo():
    info = {};
    #general-info 1
    gI = imex.createDictionaryFromFile('generalInfo.txt')
    gI1 = (gI[0],pd.DataFrame(gI[1]));
    info['generalInfo'] = gI1;
    #contributor
    gC = imex.createDictionaryFromFile('contributors.txt')
    gC1 = (gC[0],pd.DataFrame(gC[1]));
    info['contributors'] = gC1;
    return info;

def run():
    print("Loading...")
    dbs = obtainInfo();
    print("Welcome to the Book Handler Interface.")
    print (dbs)







if __name__ == '__main__':
    run();
