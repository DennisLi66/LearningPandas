import pandas as pd;
import im_exportData as imex;

def retrieveDBfromTitle(title):
    db = 0;
    #search generalInfo database for db
    #using dictionary info
    toPull = "";
    return db;


class dbHandler:
    def __init__(self):
        self.info = {};
        #general-info 1
        gI = imex.createDictionaryFromFile('generalInfo.txt')
        gI1 = {gI[0]:pd.DataFrame(gI[1])};
        self.info['generalInfo'] = gI1;
        #contributor
        gC = imex.createDictionaryFromFile('contributors.txt')
        gC1 = {gC[0]:pd.DataFrame(gC[1])};
        self.info['contributors'] = gC1;
    def getSpecificDataFrame(self,name):
        return self.info[name][name];
    def getDBfromTitle(self,title):
        db = 0;
        frame = self.getSpecificDataFrame('generalInfo');
        print(frame);
        return db;

def run():
    print("Loading...")
    db = dbHandler();
    print("Welcome to the Book Handler Interface.")
    # print (db.getSpecificDataFrame('generalInfo'))
    print(db.getDBfromTitle('Other Gibberish'))







if __name__ == '__main__':
    run();
