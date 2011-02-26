import tpt
import sys
import code
import ctypes
import traceback
from threading import Thread
print "console module loaded."
"""#redirect stdout like this:
class logger:
    def write(self,txt):
        txt=txt[:254]
        tpt.log(txt)
sys.stdout=logger()"""

element={"none":0,"dust":1,"watr":2,"oil":3,"fire":4,"stne":5,"lava":6,"gunp":7,
    "nitr":8,"clne":9,"gas":10,"plex":11,"goo":12,"icei":13,"metl":14,"sprk":15,
    "snow":16,"wood":17,"neut":18,"plut":19,"plnt":20,"acid":21,"void":22,
    "wtrv":23,"cnct":24,"dstw":25,"salt":26,"sltw":27,"dmnd":28,"bmtl":29,
    "brmt":30,"phot":31,"uran":32,"wax":33,"mwax":34,"pscn":35,"nscn":36,
    "lntg":37,"insl":38,"bhol":39,"whol":40,"rbdm":41,"lrbd":42,"ntct":43,
    "sand":44,"glas":45,"ptct":46,"bgla":47,"thdr":48,"plsm":49,"etrd":50,
    "nice":51,"nble":52,"btry":53,"lcry":54,"stkm":55,"swch":56,"smke":57,
    "desl":58,"coal":59,"lo2":60,"o2":61,"inwr":62,"yest":63,"dyst":64,
    "thrm":65,"glow":66,"brck":67,"hflm":68,"firw":69,"fuse":70,"fsep":71,
    "amtr":72,"bcol":73,"pcln":74,"hswc":75,"iron":76,"mort":77,"gol":78,
    "hlif":79,"asim":80,"2x2":81,"dani":82,"amoe":83,"move":84,"pgol":85,
    "dmoe":86,"34":87,"llif":88,"stan":89,"spng":90,"rime":91,"fog":92,
    "bcln":93,"love":94,"deut":95,"warp":96,"pump":97,"fwrk":98,"pipe":99,
    "frzz":100,"frzw":101,"grav":102,"bizr":103,"bizrg":104,"bizrs":105,
    "inst":106,"isoz":107,"iszs":108,"prti":109,"prto":110,"pste":111,
    "psts":112,"anar":113,"vine":114,"invis":115,"equalvel":116,"spawn2":117,
    "spawn":118,"shld1":119,"shld2":120,"shld3":121,"shld4":122,"lolz":123,
    "wifi":124,"filt":125,"aray":126,"bray":127,"stkm2":128,"bomb":129,
    "c5":130,"sing":131,"qrtz":132,"pqrt":133,"seed":134,"maze":135,
    "coag":136,"wall":137,"gnar":138,"repl":139,"myst":140,"boyl":141,
    "lote":142,"frg2":143,"star":144,"frog":145,"bran":146,"wind":147,
    "num":148}

def _async_raise(tid, exctype):
    '''Raises an exception in the threads with id tid'''
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble, 
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

class _fork(Thread):
    def __init__ (self,func):
        Thread.__init__(self)
        self.func=func
    def run(self):
        self.func(self)
def fork(func):
    try:
        a=fork.threads
    except:
        fork.threads={}
        fork.i=0
    tmp=_fork(func)
    fork.threads[fork.i]=tmp
    fork.i+=1
    tmp.start()
    tpt.log("Thread #%d started"%(fork.i-1))
def fork_status():
    count=0
    remove=[]
    for key in fork.threads:
        if(fork.threads[key].is_alive()):
            count+=1
        else:
            remove.append[key]
    for item in remove:
        del fork.threads[item]
    tpt.log("%d threads alive. %d threads stopped since last status."%(count,len(remove)))
def fork_unblock():
    pass#i need to implement this some day.
def error(ex):
    name,_,_=repr(ex).partition("(")
    tpt.log("%s: %s"%(name,str(ex)))

def clean():
    #add any functions that must be reachable here.
    copy=["__builtins__","__name__","__doc__","__package__",'tpt','clean',
        'element','fork','_fork','fork_status','fork_unblock']
    handle.glob={}
    for item in copy:
        handle.glob[item]=globals()[item]

def handle(txt):
    try:
        a=handle.glob
    except:
        clean()
    try:
        _handle(txt)
    except Exception as ex:
        error(ex)
        print "### -------------------- trace"
        traceback.print_exc()
        
def _handle(txt):
    print "handling '%s'"%txt
    tpt.console_less()
    try:
        #tmp=code.compile_command('\n'.join(handle.txt))
        tmp=code.compile_command(txt)
    except Exception as ex:
        #tpt.log("Invalid code. see stdout for more info.")
        error(ex)
        print "### -------------------- trace"
        traceback.print_exc()
        return
    if(tmp==None):
        tpt.console_more()
    else:
        try:
            #print "executing"
            exec tmp in handle.glob
        except Exception as ex:
            #tpt.log("Invalid code. see stdout for more info.")
            error(ex)
            print "### -------------------- trace"
            traceback.print_exc()
    
    