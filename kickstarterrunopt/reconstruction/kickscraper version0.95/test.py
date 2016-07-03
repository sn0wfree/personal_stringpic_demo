def re(file):
    with open(file,'r') as f:
        f_collected=f.readlines()
    return f_collected



for i in xrange(0,9):
    locals()['collected%s'%i]=re(locals()['collected%s.txt'%i])
    type(locals()['collected%s'%i])
