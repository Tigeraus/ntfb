import sys 
sys.path.append('..')
from ntfb import NtbMark
from ntfb import NtfBot

@NtbMark
def add(x,y):
    return x+y

add(1,1)
nb = NtfBot()
nb('hello')