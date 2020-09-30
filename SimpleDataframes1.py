# https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm

import pandas

def emptyFrame():
    f = pandas.DataFrame();
    return f;

def lolFrame():
    lol = [['Ace','Clubs'],['4','Hearts'],['6','Diamonds'],['2','Clubs'],['5','Hearts'],['2','Spades']]
    f = pandas.DataFrame(lol,columns=['Name','Suit'])
    print(f);

def dlFrame():
    dic = {'Name':['2','5','Ace','6',],'Suit':['Hearts','Diamonds','Clubs','Spades']};
    f = pandas.DataFrame(dic);
    print(f);

def ldFrame():
    lod = [{'Name':'2','Suit':'Diamonds'},{'Name':'3','Suit':'Hearts'},{'Name':'4','Suit':'Spades'}]
    f = pandas.DataFrame(lod);
    print(f);


    

if __name__ == "__main__":
    print(emptyFrame());
    lolFrame();
    dlFrame();
    ldFrame();
