
from operator import itemgetter
import sys
sotial=dict()
keys = []
# c=1
for line in sys.stdin:
	# line = line.strip()
	# person,friends = line.split('\t',1)
    person = line.split('\t')[0]
    friends = line.split('\t')[1].strip('[]\n').split(',')
    dict1={person:friends}
    sotial.update(dict1)
    keys.append(person)
    # c=c+1
    # if c==3:
    #     break
    
def common_member(a, b):   
    a_set = set(a)
    b_set = set(b)
     
    # check length
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set)) 
    else:
        return("no common elements")
for i in range(len(keys)-1):
    common =common_member(sotial[keys[i]], sotial[keys[i+1]])
    print ('%s\t%s' % (f"{keys[i]} {keys[i+1]}", common))
