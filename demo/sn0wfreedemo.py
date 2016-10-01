#coding=utf-8
import os,platform,sys
from PIL import Image
import pandas as pd
import numpy as np
import multiprocessing as mp




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




class pic2symboltext:
    def __init__(self):
        self.name='pic2text process'
        rows,columns=os.popen('stty size', 'r').read().split()
        self.width = int(columns)
        self.height = int(rows)
        self.system= platform.system()#system
        self.symboldataset=None


    def preprocess(self,img_name):

        img = Image.open(img_name)
        img_w, img_h = img.size
        #img_m = max(img.size)
        windows_w=self.width
        windows_h=self.height
        img = img.resize((w,h))
        #img = img.convert('L')
        '接下来写图片调整大小调整程序'


        return img

    def pandalizationfortest(self,character_image):
        pix=character_image.load()
        self.symboldataset=np.zeros((character_image.size[1],character_image.size[0]))
        data=self.scan_rep(pix,character_image)
        dataset=pd.DataFrame(data)
        #print datas
        self.symboldataset=dataset
        return dataset

        #data[0][1]=1
    def scan_rep(self,pix,character_image):
        data=self.symboldataset
        for i in xrange(character_image.size[0]):
            for j in xrange(character_image.size[1]):
                data[j,i]=pix[i,j][0]
                #if data[i][j]<10:
                #    data[i][j]=0
                #else:
                #    data[i][j]=1



        return data


    #def create_symbol_text(img):
    #    """ 将已经预处理好的图片根据color生成字符字符串，存放到 pic_str 变量中 """
    #    pix = img.load()
    #    pic_str = ''
    #    width, height = img.size
    #    pandalizationfortest（img）



                    #pic_str += color[int(pix[w,h]) * 14 /255]
                #pic_str += '\n'
        return pic_str



    def printdash(self):
        length= self.width
        h=self.height
        for x in xrange(h):
            sys.stdout.write ('*'*length)
            sys.stdout.flush()




def bmp2png(bmp_img_name):
    name,ext = os.path.splitext(bmp_img_name)
    if ext.lower() == '.bmp':
        target= name +'.png'
    Image.open(bmp_img_name).save(target)

    pass



def getDirList( p ):
        p = str( p )
        if p=="":
              return [ ]
        #p = p.replace( "/","/")
        if p[-1] != "/":
             p = p+"/"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isdir( p + x ) ]
        return b

def scanfolderprocess(rdir):
    fo=os.walk(rdir)
    f=[]
    for root,subfolder,files in fo:
        #print root
        num=root.lstrip(rdir)
        #print num,type(num)

    return f


#def multi_scan(img):
#    pool = mp.Pool()
    #for rdir in rdirs:
#    yv=pool.map




if __name__=='__main__':
    img_name='/Users/sn0wfree/Documents/python_projects/personal_terminal_demo/demo/test/0052.bmp'
    img=Image.open(img_name)
    s=pic2symboltext().pandalizationfortest(img)
    test='/Users/sn0wfree/Documents/python_projects/personal_terminal_demo/demo'
    fo=os.walk(test)
    files_full_infos=[]
    for (root,subfolder,file_a) in fo:
        files_full_infos.append((root,subfolder,file_a))

    print getDirList(test)
    for files_full_info in files_full_infos:
        print files_full_info,'\n'








    #a=TestPlatform()
    #print a.platform_system
    #v.printdash()
    #print g.height
