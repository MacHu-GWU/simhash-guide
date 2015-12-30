from __future__ import print_function
from simhash import Simhash, SimhashIndex
from angora.dataIO import load_pk, safe_dump_pk
import random, string
import time

def rand_str(n=8):
    return "".join(random.sample(string.ascii_lowercase, n))

datafile = "data.pickle"
indexfile = "index.pickle"

def create_test_data():
    """For 1 million records, it takes 5 minutes.
    """
    complexity = 1000**2
    print("creat data ...")
    data = [rand_str(8) for i in range(complexity)]
    print("calculate simhash ...")
    objs = [(i, Simhash(item)) for i, item in enumerate(data)]
    print("creat index ...")
    index = SimhashIndex(objs, k=3)
    safe_dump_pk(data, datafile)
    safe_dump_pk(index, indexfile)

# create_test_data()

def search_duplicate():
    data = load_pk(datafile)
    index = load_pk(indexfile)
    
    begin, middle, end = data[1000], data[500000], data[-1000]
    print("1,000th is %r, 500,000th is %r, -1,000th is %r." % (
        begin, middle, end))
         
    st = time.clock()
    ind = data.index(begin)
    print("list.index(item) method for begin takes %.6f sec" % (time.clock() - st,))

    st = time.clock()
    res = index.get_near_dups(Simhash(begin))
    print("simhash index method for begin takes %.6f sec" % (time.clock() - st,))
    
    st = time.clock()
    ind = data.index(middle)
    print("list.index(item) method for middle takes %.6f sec" % (time.clock() - st,))

    st = time.clock()
    res = index.get_near_dups(Simhash(middle))
    print("simhash index method for middle takes %.6f sec" % (time.clock() - st,))
    
    st = time.clock()
    ind = data.index(end)
    print("list.index(item) method for end takes %.6f sec" % (time.clock() - st,))
    
    st = time.clock()
    res = index.get_near_dups(Simhash(end))
    print("simhash index method for end takes %.6f sec" % (time.clock() - st,))
    
search_duplicate()