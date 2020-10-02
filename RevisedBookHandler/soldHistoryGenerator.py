#range from 1 to 7 inclusive

import random

def produceRandomDate():
    month = str(random.randrange(1,13));
    if (len(month) < 2):
        month = '0' + month;
    year = "20";
    year2 = str(random.randrange(0,100));
    if (len(year2) < 2):
        year = year + '0' + year2;
    else:
        year = year + year2;
    number = 0;
    if (month == '02' and int(year)%4==0):
        number = random.randrange(1,30);
    elif (month == '02'):
        number = random.randrange(1,29);
    elif (month in ['01','03','05','07','08','10','12']):
        number = random.randrange(1,32);
    else:
        number = random.randrange(1,31);
    day = "";
    if (number < 10):
        day = str(0) + str(number);
    else:
        day = str(number);
    #print(day + '/' + month + '/' + year);
    return day + '/' + month + '/' + year

if __name__ == "__main__":
    #print (random.randrange(100))
    #print (round(random.uniform(5, 30),3))
    filename = "databases/soldhistory.txt";
    file = open(filename,'w');
    file.write("dbNumber, versionNumber, soldAt, dateSold\n\n")
    for i in range(1,1001):
        file.write("\n");
        superstring = str(random.randrange(1,8)) + "\n1\n" + str(round(random.uniform(5, 30),2)) + "\n" + produceRandomDate() + "\n\n";
        file.write(superstring);
    file.close();
