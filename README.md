# Medium-Scrapper
Python Bot for Scrapping Medium Articles and Storing in DataBase

/*Prerequisites*/

/*Setting Up*/
1. Python 3 Compiler

To Install in Ubuntu type following command in your Terminal

sudo apt-get install python3

2.mysql-server 

To install in ubuntu type following command 

sudo apt install mysql-server

3. Some Libraries also needed to install them 

sudo apt-get install python3-bs4

sudo apt-get install python3-pip

sudo pip3 install mysql-connector-python

If you get any problems refer youtube.com and search for your problem



/*Installing and Using*/

1.Download the repository in to your desired location

2.Open terminal in repository

3.Type : mysql -u username -p

4.It will ask your password enter it.

5.You will go into mysql interface

  Type: CREATE DATABASE MEDS; 

  You can use any name instead of MEDS i used MEDS as my name. If you are new to these things remain it as MEDS.
  
6.Now Importing Table Schema and Some Articles I Scraped in to your newly Created Database

  Type : mysql -u username -p MEDS < Download_location/Medium Scrapper/schema.sql
  
  Here Download location is location where you downloaded and extracted the repo
  
7. You can view the articles Scraped by me by typing the command in mysql interface

  1. USE MEDS;
  2. SELECT * from Article;


/*Using the Scraper Bot*/

1. Just Copy and Paste the links of your needed articles in test_cases.txt(One link in a line and Last line should not be empty it will generate you error after completion)

2.After copying all the desired links in test_cases.txt

3.Open the terminal and Navigate to Medium Scrapper Folder and Type following Command:

  python3 main.py
  
  On Successful completion you will a "hurray!" Message at the end
  
  If you get any errors let me know they may be due to not setting up correctly or you are trying to scrape non medium        articles and many reasons may be feel free to ask.
  
 4. On running it done you got all your articles in your database Voila`!
 
 5. To view the articles go to your database . Run following Commands in your Terminal
 
    1. mysql -u username -p
    2. Your Password
    3. USE MEDS;
    4. select * from Article;
    
  6. Thats it in a magic time you will see your articles in well formatted table form
  
7. To Update your DB with new contents of same article . Follow steps from point one of /*Using Scraper Bot*/

That's it if you have any doubts or problems feel free to ask!

Thank You!

Happy Scraping!
  
