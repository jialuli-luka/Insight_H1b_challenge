#used to find top 10 job and states
from count import Counting
from minheap import MinHeap
import sys

#get the count for every job and state
count = Counting(sys.argv[1])
job_count, state_count, sum_count = count.count()

#find the top_10 jobs
job_heap = MinHeap(10)
job_fhandle = open(sys.argv[2],'w')
for key,value in job_count.items():
    job_heap.add(key,value)
job_fhandle.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
result = dict()
for i in range(min(10,len(job_count))):
    key,value = job_heap.extract()
    result[key.lstrip('""').rstrip('""')] = value
result = sorted(result.items(), key = lambda item:item[0])
result.sort(key = lambda x:x[1], reverse = True)
for item in result:
    key = item[0]
    value = item[1]
    p = round(value / sum_count * 100.0, 1)
    s = key + ';' + str(value) + ';' + str(p) + '%' + '\n'
    job_fhandle.write(s)

#find the top_10 states
state_heap = MinHeap(10)
state_fhandle = open(sys.argv[3],'w')
for key,value in state_count.items():
    state_heap.add(key,value)
state_fhandle.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
result = dict()
for i in range(min(10,len(state_count))):
    key,value = state_heap.extract()
    result[key.lstrip('""').rstrip('""')] = value
result = sorted(result.items(), key = lambda item:item[0])
result.sort(key = lambda x:x[1], reverse = True)
for item in result:
    key = item[0]
    value = item[1]
    p = round(value / sum_count * 100.0, 1)
    s = key + ';' + str(value) + ';' + str(p) + '%' + '\n'
    state_fhandle.write(s)
