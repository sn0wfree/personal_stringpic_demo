# coding=utf-8

import os
import platform
import sys
import gc
import time
from PIL import Image
import pandas as pd
import numpy as np
import multiprocessing as mp


def get_terminal_bound():
    rows, columns = os.popen('stty size', 'r').read().split()
    width = int(columns)
    height = int(rows)
    return (int(rows), int(columns))


class TestPlatform:

    def __init__(self):
        self.python_version = platform.python_version()  # Python version
        # programme structure('32bit', 'WindowsPE')
        self.platform_architecture = platform.architecture()
        self.node = platform.node()  # name
        # capture operator system's core version
        self.platform_version = platform.version()
        # capture operator system,Windows-7-6.1.7601-SP1
        self.platform_name_version = platform.platform()
        # computer processor info,'Intel64 Family 6 Model 42 Stepping 7,
        # GenuineIntel'
        self.processor = platform.processor()
        self.python_compiler = platform.python_compiler()
        self.otherinfo = platform.uname()  # other
        self.platform_system = platform.system()  # system

    def UsePlatform(self, returnornot=False):
        sysstr = self.platform_system
        if returnornot:
            return sysstr
        else:
            pass
        # if(sysstr =="Windows"):
        #    return ("Call Windows tasks")
        # elif(sysstr == "Linux"):
        #    print ("Call Linux tasks")
        # elif(sysstr == "Darwin"):
        #     print ("Call Darwin or Mac tasks")
        # else:
        #    print ("Other System tasks")

    # print

    # print platform.system_alias()

    # print

        # return (rows,columns)
    # def get_terminal_width_resize():
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

    # def get_terminal_height():
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
        self.name = 'show_bound_process'
        rows, columns = os.popen('stty size', 'r').read().split()
        #self.width = 20
        #self.height = 50
        self.width = int(columns)
        self.height = int(rows)
        self.system = platform.system()  # system


class pic2symboltext:

    def __init__(self):
        self.name = 'pic2text process'
        rows, columns = os.popen('stty size', 'r').read().split()
        self.width = int(columns)
        self.height = int(rows)
        self.system = platform.system()  # system
        self.symboldataset = None
        self.resize = (0, 0)

    def preprocess(self, img_name):
        img = Image.open(img_name)
        img_w, img_h = img.size
        #img_m = max(img.size)
        windows_w = float(self.width)
        windows_h = float(self.height)
        #img = img.convert('L')
        'resize picture process'
        # resize_num=windows_h/img_h
        scaleX = windows_w / img_w
        scaleY = windows_h / img_h
        scale = min(scaleY, scaleX)
        resize_w = scale * img_w
        resize_h = scale * img_h
        resize = (int(resize_w * 2.6), int(resize_h))
        # if img_h >= windows_h:
        #    resize_h=windows_h
        # print img_h,windows_h
        #    resize_w=resize_h*4/3
        # print resize_w
        #    if resize_w <= windows_w:
        #        resize=(int(resize_w),int(resize_h))
        #    elif resize_w > windows_w:
        #        resize_new_w=windows_w
        #        resize_new_h=resize_new_w*3/4
        #        resize=(int(resize_new_w),int(resize_new_h))
        # elif img_h < windows_h:
        #    resize_h=img_h
        #    if img_w <= windows_w:
        #        resize_w=img_w
        #        resize=(int(resize_w),int(resize_h))
        #    elif img_w > windows_w:
        #        resize_new_w = windows_w
        #        resize_new_h=resize_h*3/4
        #        resize=(int(resize_new_w),int(resize_new_h))
        # print resize
        img = img.resize(resize, Image.ANTIALIAS)
        self.resize = resize

        return img

    def pandalizationfortest(self, img_name):
        character_image = self.preprocess(img_name)
        pix = character_image.load()
        self.symboldataset = np.zeros(
            (character_image.size[1], character_image.size[0]))
        data = self.scan_rep(pix, character_image)
        dataset = pd.DataFrame(data)
        # print datas
        self.symboldataset = dataset
        return dataset

        # data[0][1]=1
    def scan_rep(self, pix, character_image):
        data = self.symboldataset
        for i in xrange(character_image.size[0]):
            for j in xrange(character_image.size[1]):
                data[j, i] = pix[i, j][0]
                if 242 <= data[j, i] <= 255:
                    data[j, i] = 5
                    # 5'%'
                elif 230 <= data[j, i] < 242:
                    data[j, i] = 4
                    # 4'@'
                elif 150 <= data[j, i] < 230:
                    data[j, i] = 3
                    # 3'#'
                elif 94 <= data[j, i] < 150:
                    data[j, i] = 2
                    # 2'*'
                elif 38 <= data[j, i] < 94:
                    data[j, i] = 1
                    # 1'.'
                elif 0 <= data[j, i] < 38:
                    data[j, i] = 0
                    # 0' '
        return data

    def printdash(self):
        length = self.width
        h = self.height
        for x in xrange(h):
            sys.stdout.write('*' * length)
            sys.stdout.flush()


def getDirList(p):
    p = str(p)
    if p == "":
        return []
    #p = p.replace( "/","/")
    if p[-1] != "/":
        p = p + "/"
    a = os.listdir(p)
    b = [x for x in a if os.path.isdir(p + x)]
    return b

# def multi_scan(img):
#    pool = mp.Pool()
    # for rdir in rdirs:
#    yv=pool.map


def scan_all_pic_file_process(rdir):
    fo = os.walk(rdir)
    f = []
    for root, subfolder, files_a in fo:
        pass
    for file_a in files_a:
        full_path_for_each_bmp = (root, file_a)
        f.append(full_path_for_each_bmp)
        # print root
        # num=root.lstrip(rdir)
        # print num,type(num)
    return f


def showoutput(img_file_png, preload=True):

    p = pic2symboltext()
    # print 'terminal_bound:%s,%s' %(p.width,p.height)
    # p_img=p.preprocess(a)
    p_data = p.pandalizationfortest(img_file_png)
    # print p_data[44:45]
    if p.width - p.resize[0] >= 0:
        extra_symbol = (p.width - p.resize[0]) / 2
    else:
        extra_symbol = 0

    if preload == False:
        for x in xrange(len(p_data)):
            example = p_data[x:x + 1].values.tolist()[0]
            print_list = ' ' * extra_symbol
            for e in example:
                if e == 5:
                    print_list += '%'
                elif e == 4:
                    print_list += '@'
                elif e == 3:
                    print_list += '#'
                elif e == 2:
                    print_list += '*'
                elif e == 1:
                    print_list += '.'
                elif e == 0:
                    print_list += ' '
                else:
                    print_list += ' '

            print_list += ' ' * int(extra_symbol)
            print print_list
    elif preload == True:
        plist = []
        for x in xrange(len(p_data)):
            example = p_data[x:x + 1].values.tolist()[0]
            print_list = ' ' * int(extra_symbol)
            for e in example:
                if e == 5:
                    print_list += '%'
                elif e == 4:
                    print_list += '@'
                elif e == 3:
                    print_list += '#'
                elif e == 2:
                    print_list += '*'
                elif e == 1:
                    print_list += '.'
                elif e == 0:
                    print_list += ' '
                else:
                    print_list += ' '

            print_list += ' ' * int(extra_symbol)
            plist.append(print_list)
        return plist


if __name__ == '__main__':
    # img_name='/Users/admin/Documents/python/personal_terminal_demo/demo/test/0052.bmp'
    # img=Image.open(img_name)
    preload = raw_input('pre-load feature disable,should preload?(yes or no):')
    test = '/Users/sn0wfree/Documents/python_projects/personal_stringpic_demo/demo/video2picture/Capture_png30'
    # test2="./video2picture/capture_png30"
    ff = scan_all_pic_file_process(test)
    total_files = []
    gc.collect()
    for f in ff:
        total_file = f[0] + '/' + f[1]
        total_files.append(total_file)
    # a=total_files[2678]

    movie_orderd = []
    if preload == 'Disable' or preload == 'no':
        for img_file_png in total_files:
            showoutput(img_file_png, False)
    elif preload == 'yes' or preload == 'enable':
        pool = mp.Pool()
        # for rdir in rdirs:
        # pool.map(bmp2png,ff)

        # for img_file_png in total_files:
        plist = pool.map(showoutput, total_files)
        test = raw_input(
            "preload have already completed,should we start?(yes)")
        re_test = "0"

        while 1:
            p = 0

            if test == "yes":
                p = 1
            elif re_test == "yes":
                p = 1
            elif re_test == "no" and test == "done":
                break
            if p == 1:

                for ls in plist:
                    fff = time.time()
                    for l in ls:
                        print l
                    t = time.time() - fff
                    if t <= (1 / 25.0):
                        time.sleep(1 / 25.0 - t)
                    else:
                        pass

            re_test = raw_input(
                "preload have already completed,should we re-start?(yes)")
            if test == "yes":
                test = "done"
            else:
                pass

        # print plist
        # movie_orderd.append(plist)
        # for i in xrange(10):

            # print "time=%s"%round((i/30.0),5)
            # temp=raw_input("stop?")

        # print "%s\n"%l
            #
