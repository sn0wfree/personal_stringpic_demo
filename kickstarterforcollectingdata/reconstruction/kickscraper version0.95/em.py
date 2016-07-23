import random,sys




#class testforem():
for x in xrange(0,1000):
    dash_r='/'*random.randint(1,100)
    star_r='*'*random.randint(1,100)
    wave_r='~'*random.randint(1,100)
    point_r='.'*random.randint(1,100)
    bracks_r='()'*random.randint(1,100)
    A_r='A'*random.randint(1,100)
    question_r='?'*random.randint(1,100)
    strrr=dash_r+star_r+wave_r+point_r+bracks_r+A_r+question_r
    symbol=list(strrr)[random.randint(1,len(strrr)-1)]
    for j in xrange(0,1000):
        symbol+=list(strrr)[random.randint(1,len(strrr)-1)]
    sys.stdout.write('/r %s'%symbol)
    sys.stdout.flush()
