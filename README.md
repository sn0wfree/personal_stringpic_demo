# Kickstarterscrapy
=====================
This python file is just for collecting kickstarter crowdfunding platform data!!
and the aim is for help myself to access the crowdfunding field what may i need.
# Menu

---------------
1. Included materials
2. Files
3. Codes

------------------------

## 1. included materials
>In those code files, those may include some useless materials for other people who want to read.Here,i just show the important materials if you want to use mine code.These have three folders which may include a lots of .py files

if you are intersted in this project, first two folders which are **downloadurl** and **kickstarterforcollectingdata** should be focus on.

### **downloadurl**
- this folder is for search all possible project urls. it can be split into 2 parts.
  - 1st part:
     - generating all category-based urls for hunman-read urls from [kickstarter corwdfunding platform!](www.kickstarter.com)
  - 2nd part:
     - throught requesting each category-based url, the bot can crawl and download the links which appear at the category page (16 projects each page).
after that, you can access all estblished or live projects (included canceled, failed,live,successful and suspended projects).

### **kickstarterforcollectingdata**
- this folder include main spider program
- my version format is **name**+**version**.py
- in the **kickstarterforcollectingdata** folder, you can find a **reconstruction** folder. 
- any things you want all saving in this folder
- and what you may interst is the plan2.3.3.py or the version bigger than 2.3.3
	- sometime i may add more information follwoing veriong number for .py file,like add fortxt or forcsv.

## 2.files
- you may found a lot of txt files and csv or xlsx files, that may somedata what data i have collected until 4 July 2016. 
- i will clean up those useless files when i finish my dissertation finally

## 3. codes
- i use python 2.7 code  
- and when you run the code, you may find some number or path ask for, you should type full path into two parts.
- one is public path for what dir/folder you want save the data. the dir/folder must include 4 csv files and one txt file.(those must be named as follow)


```		
collected.txt
project_data.csv
rewards_backers_distribution.csv
rewards_pledge_limit.csv
rewards_pledged_amount.csv 				
```
- and a csv file which must include the target urls as column


___________________________I'm a line____________________________

Wirtten by sn0wfree at 15 July 2016

	
	
	
	
