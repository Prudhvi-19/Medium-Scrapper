#importing required code files
from Scrape import *

#MAIN Takes input from file and gives url to scrape function which scrapes and stores it in Database
def main():
    myfile = open("test_cases.txt","r")
    try:
        for i in myfile:
            if i == '':
                exit
            link = i
            scrape(i)
    except EOFError:
        return 0
    print ("Scraping Completed hurray!")

if __name__ == "__main__":
    main()

