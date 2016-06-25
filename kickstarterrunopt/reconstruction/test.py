
import funcforkick
import time


start = time.time()

someurl = 'https://www.kickstarter.com/projects/elijahkavana/action-deck-to-spark-your-journey?ref=category_newest'
(a,b,c,d)=funcforkick.opt(someurl)
print a



end = time.time()
print end-start
