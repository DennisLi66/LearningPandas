#pip install pandas
# https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm
import pandas as pan
import numpy as np

def emptySeries():
    x = pan.Series([],dtype= pan.StringDtype());
    return x;

def numpyArraySeries():
    #make numpy array
    na = np.array([1,2,3,4,5])
    x = pan.Series(na,index=['a','b','c','d','e']);
    print(x['a'] + x['e']);
    return x;

def dictSeries():
    dd = {'a':1,'b':2,'c':3};
    x = pan.Series(dd);
    print(x['a']);
    

if __name__ == "__main__":
    print(emptySeries());
    print(numpyArraySeries());
    dictSeries();
