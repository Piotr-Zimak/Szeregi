import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

def main():
    #data = pd.read_csv('D:\\Piotr\\Studia\\PK mgr\\sem II\\Szeregi czasowe\\Lab1\\MSFT.csv', sep= ',')
    data = pd.read_csv('Lab1\\MSFT.csv', sep= ',')
    #1
    x = data['Date']
    y = data['Close']
    plot.subplot(2,2,1)
    plot.plot(x,y)
    #plot.xticks(rotation=90)
    plot.title("Microsoft stock")
    #plot.show()

    #2
    plot.subplot(2,2,2)
    plot.plot(x,y)
    plot.title("Microsoft stock [log]")
    plot.yscale('log')
    #plot.show()

    #3
    differences = data.set_index('Date').diff()
    plot.subplot(2,2,3)
    plot.plot(differences['Close'])
    plot.title("Earnings")
    #plot.show()

    #4
    plot.subplot(2,2,4)
    plot.plot(differences['Close'])
    plot.title("Earnings [log]")
    plot.yscale('log')
    plot.show()
    

if __name__ == "__main__":
    main()