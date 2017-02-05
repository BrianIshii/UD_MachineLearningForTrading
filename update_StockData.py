#This program will update CSV files in StockData Folder
import webbrowser
import datetime
import os 
import time

def update_data(folder):
    """
    this should do all the steps by calling this function
    """
    symbols = get_current_symbols(folder)
    for symbol in symbols:
        download_data(symbol,folder)
def add_data():
    pass
def get_current_symbols(folder):
    """
    get file names so we can find what symbols we need
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
    print"Downloading {}.csv. . . .".format(symbol),
    while os.path.isfile(src_file) is False:
        continue
    time.sleep(0.25)
    if os.path.isfile(src_file) is True:
        os.rename(src_file,dst_file)
        print"Done"
    else:
        print"Error"
def download_custom_data(symbols,data_type=[]):
    data = ""
    for i in range(len(data_type)):
        data +=data_type[i]
        url = "http://finance.yahoo.com/d/quotes.csv?s=" + symbols + "&f=" + data + ""
    print url
    #webbrowser.open(url,new=2)

update_data("StockData")