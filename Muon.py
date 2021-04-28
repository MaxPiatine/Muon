def output():
    """
    Arranges files to it can then be separated into two different files
    """
    file = open("21-01-29-15-12.txt","r")
    output = open("1st_column.txt","w")
    lines= file.readlines()
    for i in (lines):
        for j in i:
            if j.isdigit():
                output.write(j)
            if j.isspace():
                output.write("\n")
                file.readline()
    file.close()
    output.close()

def columns():
    """
    Puts The lifetimes of the muons incident on the scintillator as column1.txt and the rest as column 2.
    """
    file = open("1st_column.txt", "r")
    column1= open("column1.txt","w")
    column2= open("column2.txt","w")
    lines = file.readlines()
    for i in range(len(lines)):
        if i%2==0:
            column1.write(lines[i])
        else:
            column2.write(lines[i])


def mean4MuonLifetime():
    """
    Function goes through the list of data of "The lifetimes of the muons incident on the scintillator"
    and provides the mean of the lifetimes of muons. It takes all the data below 40000ns since data above this
    value is less than the cut off time.
    >>> data = [123,40000,39999,7389] #Let this be in the file
    >>> mean4MuonLifetime()
    The mean lifetimes of the muons incident on the scintillator is: 15837
    """
    with open('column1.txt','r') as fin:
        data = fin.read().split('\n')
        data.remove('')
        length = 0
        mean = 0
        sd = 0
        for i in data:
            if isinstance(int(i),int)==True and (0<=int(i)<40000):
                mean += int(i)
                length += 1
            else:
                pass
        lifetime=mean/length
        for j in data:
            if isinstance(int(j),int)==True and (0<=int(j)<40000):
                sd += ((float(j)-lifetime)**2)
            else:
                pass
        sd = (sd/(length))**(1/2)
        print("The mean lifetimes of the muons incident on the scintillator is: " +str(lifetime)+" +/- "+str(sd))

def NumberofOccurences():
    """
    Takes all of the lifetimes and sets the amount of occurences for each lifetimes.
    >>> data = [123,40000,39999,7389,7389,7389,123] #Let this be in a file
    >>> NumberofOccurences
    123 2
    7389 3
    39999 1
    """
    column3 = open("column3.txt","w")
    with open('column1.txt','r') as fin:
        data = fin.read().split('\n')
        data.remove('')
        for i in data:
            count = 0
            for j in data:
                if int(i)==int(j):
                    count += 1
                    data.remove(str(j))
                else:
                    pass
            column3.write(i+"  "+str( count )+'\n' )

if __name__=="__main__":
    output()
    columns()
    mean4MuonLifetime()
    NumberofOccurences()