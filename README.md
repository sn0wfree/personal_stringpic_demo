

# Kickstarterscrapy
-------------------------------------------------
```
This python file is just for collecting kickstarter crowdfunding platform data!!
and the aim is for help myself to access the crowdfunding field what may i need.
```
# Menu
------------------------------------------------
1. Included materials
2. Files
3. Codes
4. update
5. upgrade

-----------------------------------------------

## 1. included materials
>In those code files, those may include some useless materials for other people who want to read.Here,i just show the important materials if you want to use mine code.These have three folders which may include a lots of .py files

if you are intersted in this project, first two folders which are **downloadurl** and **kickstarterforcollectingdata** should be focus on.

### **downloadurl**
- this folder is for search all possible project urls. what it included may involve 2 parts of information.
  - 1st part:
     - generating all category-based urls for hunman-read urls from [kickstarter corwdfunding platform!](www.kickstarter.com)
  - 2nd part:
     - throught requesting each category-based url, the bot can crawl and download the links which appear at the category page (16 projects each page).
after that, you can access almost estblished or live projects (included canceled, failed,live,successful and suspended projects).

### **kickstarterforcollectingdata**
- this folder include main spider program
- my version format is **name**+**version**.py
- in the **kickstarterforcollectingdata** folder, you can find a folder named **reconstruction** . 
- any things you want all saving in this folder
- and what you may interst is the plan2.3.3.py or the version bigger than 2.3.3
	- sometime i may add more information after version number in the .py file,like add fortxt or forcsv.

## 2.files
- you may find a lot of txt files and csv or xlsx files, that are some data what i have collected until 4 July 2016. 
-PS: i will clean up those useless files when i finish my dissertation finally

## 3. codes
- I use python 2.7 to code  
- and when you run the code, you may find some number or path be required to type in, you should type full path into two parts.
	- one is public path for what dir/folder you want save the data. the dir/folder must include 4 csv files and one txt file.
	- another is the full name of target file(csv format) 
	- (those must be named as follow)
```
targetfile.csv
collected.txt
project_data.csv
rewards_backers_distribution.csv
rewards_pledge_limit.csv
rewards_pledged_amount.csv 				
```
	
-**the target file**  must include the target urls
## 4. update
- i know there still some bug i have not fixed, but anyway it work, that is it. i do not promise to fix it,but i will try my best to fix it and update it.
 

## 5.upgrade
- for now, i still try to upgrade my code, untill i finish my disseration.
- now i'm work on covering the projects which  cannnot be searched from category pages






___________________________I'm a line____________________________

Wirtten by sn0wfree at 15 July 2016 Cardiff, UK

	
	
	
	
