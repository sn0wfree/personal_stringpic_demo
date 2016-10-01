#coding=utf-8
import os,platform,sys
import Image





def get_terminal_bound():
    rows,columns=os.popen('stty size', 'r').read().split()
    width = int(columns)
    height = int(rows)
    return (int(rows),int(columns))

class TestPlatform:
    def __init__(self):
        self.python_version = platform.python_version() # Python version
        self.platform_architecture = platform.architecture()#programme structure(’32bit’, ‘WindowsPE’)
        self.node = platform.node() # name
        self.platform_version=platform.version()#  获取操作系统的core版本
        self.platform_name_version = platform.platform()#获取操作系统名称及版本号，Windows-7-6.1.7601-SP1
        self.processor = platform.processor()#计算机处理器信息，’Intel64 Family 6 Model 42 Stepping 7, GenuineIntel’
        self.python_compiler=platform.python_compiler()#  获取系统中python解释器的信息
        self.otherinfo=platform.uname()#  other
        self.platform_system=platform.system()#system
    def UsePlatform(self, returnornot=False):
        sysstr = self.platform_system
        if returnornot:
            return sysstr
        else:
            pass
        #if(sysstr =="Windows"):
        #    return ("Call Windows tasks")
        #elif(sysstr == "Linux"):
        #    print ("Call Linux tasks")
        #elif(sysstr == "Darwin"):
        #     print ("Call Darwin or Mac tasks")
        #else:
        #    print ("Other System tasks")




    #print

    #print platform.system_alias()

    #print












        #return (rows,columns)
    #def get_terminal_width_resize():
    #    c = commands.getoutput('resize').split('\n')
    #    c = [x for x in c if x.startswith('COLUMNS=')]
    #    if c:
    #        c = c[0]
    #        dummy, c = c.split('=', 1)
    #        if c[-1] == ';':
    #            c = c[:-1]
    #    if c:
    #        return int(c)
    #    else:
    #        return None

    #def get_terminal_height():
    #    c = commands.getoutput('resize').split('\n')
    #    c = [x for x in c if x.startswith('LINES=')]

    #    if c:
    #        c = c[0]
    #        dummy, c = c.split('=', 1)
    #        if c[-1] == ';':
    #            c = c[:-1]
    #    if c:
    #        return int(c)
    #    else:
    #        return None

class show_terminal_bound:
    def __init__(self):
        self.name='show_bound_process'
        rows,columns=os.popen('stty size', 'r').read().split()
        #self.width = 20
        #self.height = 50
        self.width = int(columns)
        self.height = int(rows)
        self.system= platform.system()#system


class pic2symboltext():
    def __init__(self):
        self.name='pic2text process'
        rows,columns=os.popen('stty size', 'r').read().split()
        self.width = int(columns)
        self.height = int(rows)
        self.system= platform.system()#system

    def preprocess(self,img_name):

        img = Image.open(img_name)
        img_w, img_h = img.size
        #img_m = max(img.size)
        #windows_w=self.width
        #windows_h=self.height
        #img = img.resize((w,h))
        img = img.convert('L')
        return img

    def create_symbol_text(img):
        """ 将已经预处理好的图片根据color生成字符字符串，存放到 pic_str 变量中 """
        pix = img.load()
        pic_str = ''
        width, height = img.size
        for h in xrange(height):
                for w in xrange(width):
                    if pix[w,h]==255:
                        

                    #pic_str += color[int(pix[w,h]) * 14 /255]
                pic_str += '\n'
        return pic_str



    def printdash(self):
        length= self.width
        h=self.height
        for x in xrange(h):
            sys.stdout.write ('*'*length)
            sys.stdout.flush()







if __name__=='__main__':

    a=TestPlatform()
    #print a.platform_system
    v.printdash()
    #print g.height
