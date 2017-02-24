import os,urllib2,time

jieguo=[]
def saveListToFile(file,list):
    """
        jieguo
    :return:
    """
    s = '\n'.join(list)
    with open(file,'a') as output:
        output.write(s)
def zhengli():
    fp=open("jieguo.txt", "r")
    alllines=fp.readlines()
    fp.close()
for eachline in alllines:
        eachline=eachline.strip('\n')
        eachline=eachline.strip(' ')
        http_url=eachline
        try:
            req=urllib2.Request(http_url)
            req.add_header('User-Agent','Mozilla/5.0')
            resp = urllib2.urlopen(req, timeout=10)
            qrcont=resp.read()
     
        except Exception,e:
            a = str(e)
            if 'HTTP Error 500' in a:
                print http_url
                jieguo.append(http_url)
            else:
                print 'not shell'
        
def main():
    zhengli()
    saveListToFile('shell.txt',jieguo)
  
if __name__ == '__main__':
    main()
        
