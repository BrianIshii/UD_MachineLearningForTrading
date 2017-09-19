#This program will update CSV files in StockData Folder
import webbrowser
import datetime
import os 
import time

def update_data(folder):
    """
    this should do all the steps by calling this function

    Arguments:
    folder -- (String) i.e. 'StockData'
    """
    symbols = get_current_symbols(folder)
    for symbol in symbols:
        download_data(symbol,folder)

def get_current_symbols(folder):
    """
    get file names so we can find what symbols we need

    Arguments:
    folder -- (String) i.e. 'StockData'

    """
    symbols = []
    path = os.path.abspath(folder)
    for file in os.listdir(path):
        if file.endswith(".csv"):
            symbols.append(file[:-4])
    return symbols
def download_data(symbol,folder):
    """
    download data from yahoo finance
    Note: make sure there is not a table.csv file in Downloads folder

    Arguments:
    symbol -- (String) i.e. 'AAPL'
    folder -- (String) i.e. 'StockData'

    """
    now = datetime.datetime.now()
    d = str(int(now.strftime("%m"))-1)
    e = str(int(now.strftime("%d")) - 1)
    f = now.strftime("%Y")
    url = "http://ichart.finance.yahoo.com/table.csv?s="+str(symbol)+"&a=00&b=01&c=1900&d="+d+"&e="+e+"&f="+f+"&g=d&ignore=.csv"
    webbrowser.open(url,new=2)
    if folder == "StockData":
        new_file = "table.csv"
    src_file = os.path.abspath("../../Downloads/"+new_file)
    dst_dir = os.path.abspath('StockData')
    dst_file = dst_dir +"/{}.csv".format(symbol)
    print "Downloading {}.csv. . . .".format(symbol),
    #print("Downloading {}.csv. . . .".format(symbol),end="") # for python3
    while os.path.isfile(src_file) is False:
        continue
    time.sleep(0.1)
    if os.path.isfile(src_file) is True:
        os.rename(src_file,dst_file)
        print("Done")
    else:
        print("Error")
def download_custom_data(symbols,data_type=[]):
    """
    download custom data from yahoo finance
    
    Arguments:
    symbols -- (List) i.e. ['AAPL','SPY']
    data_type -- (List) i.e. ['o','p']
    """
    symbol_string = ""
    data = ""
    if len(symbols) > 1:
        for i in symbols[:-1]:
            symbol_string += i
            symbol_string += ","
        symbol_string += symbols[-1]
    else:
        symbol_string = symbols[0]
    for i in range(len(data_type)):
        data +=data_type[i]
        url = "http://finance.yahoo.com/d/quotes.csv?s=" + symbol_string + "&f=" + data + ""
    print(url)
    webbrowser.open(url,new=2)
syms = ['GOOGL','AAPL']
types = ['y','d','r1','m5','m6','m7','m8','m3','m4']
#download_custom_data(syms,types)