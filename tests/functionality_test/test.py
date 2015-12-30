from __future__ import print_function, unicode_literals
from simhash import Simhash, SimhashIndex
import re

def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r"[^\w]+", "", s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

# --- View simhash value ---
def view_simhash_value():
    print("%x" % Simhash(get_features("How are you? I am fine. Thanks.")).value)
    print("%x" % Simhash(get_features("How are u? I am fine.     Thanks.")).value)
    print("%x" % Simhash(get_features("How r you?I    am fine. Thanks.")).value)

# view_simhash_value()

# --- Get distance of two simhash ---
def get_distance_of_two_simhash():
    print(Simhash("aa").distance(Simhash("bb")))
    print(Simhash("aa").distance(Simhash("aa")))

# get_distance_of_two_simhash()

# --- Use the SimhashIndex to query near duplicates objects in a very efficient way ---
def use_simhash_index():
    data = {
        1: "How are you? I Am fine. blar blar blar blar blar Thanks.",
        2: "How are you i am fine. blar blar blar blar blar than",
        3: "This is simhash test.",
    }
    objs = [(str(k), Simhash(get_features(v))) for k, v in data.items()]
    index = SimhashIndex(objs, k=3)
    
    print(index.bucket_size())
    
    s1 = Simhash(get_features(u"How are you i am fine. blar blar blar blar blar thank"))
    print(index.get_near_dups(s1))
    
    index.add("4", s1)
    print(index.get_near_dups(s1))
    
use_simhash_index()