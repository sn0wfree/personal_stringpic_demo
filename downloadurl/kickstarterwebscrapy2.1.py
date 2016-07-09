from urllib2 import Request, urlopen, URLError

from time import sleep
someurl = 'https://www.kickstarter.com/projects/mnbookarts/the-s-helmes-and-w-gaglione-rubber-stamp-archive?ref=category_featured'

req = Request(someurl)

try:
      response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    the_page = response.readlines()       # read each line of the html file
    for line in the_page:                 # iterate through the lines
        if 'twitter:text:time' in line:   # check for lines we want to find & print them
            days_left=line.split('"')[3]

        if 'data-goal' in line:
            words = line.split(" ")             # split line into 'words'
            for word in words:                  # iterate through 'words'
                if 'data-goal' in word:
                    target = word.split('"')    # split word at " character
                                                             # make 2nd element a float
                    print 'target: %.4f' % float(target[1])  # then truncate to 4 d.p.
                if 'data-percent-raised' in word:
                    percent = word.split('"')
                    print 'percentage raised: %.4f  ' % (float(percent[1]) )
                if 'data-pledged' in word:
                    amount_raised = word.split('"')
                    print 'Total so far: %.4f' % float(amount_raised[1])
            #print 'Time left: %s' % days_left
            print ' '                           # stick a blank line on the end
            break                               # break out of the loop once done
