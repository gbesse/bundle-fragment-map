import hashlib
from .common import integer,identifier

def run(data):
 total=integer(data['total_bytes'],0,100000);fragments=data['fragments']
 if len(fragments)>1000:raise ValueError('fragments')
 values=[None]*total;owners=[set()for _ in range(total)];conflicts=set();overlap=0
 for f in fragments:
  name=identifier(f['id']);raw=bytes.fromhex(f['hex']);offset=integer(f['offset'],0,total)
  if offset+len(raw)>total:raise ValueError('fragment_range')
  for i,value in enumerate(raw,offset):
   if values[i] is not None:
    overlap+=1
    if values[i]!=value:conflicts.add(i)
   else:values[i]=value
   owners[i].add(name)
 gaps=[];i=0
 while i<total:
  if values[i]is not None:i+=1;continue
  start=i
  while i<total and values[i]is None:i+=1
  gaps.append([start,i])
 complete=not gaps and not conflicts
 return {'total_bytes':total,'covered_bytes':sum(x is not None for x in values),'overlapping_byte_observations':overlap,'missing_ranges':gaps,'conflicts':[{'offset':i,'fragment_ids':sorted(owners[i])}for i in sorted(conflicts)],'complete_unambiguous':complete,'payload_sha256':hashlib.sha256(bytes(values)).hexdigest()if complete else None,'model':'one_declared_payload_byte_ranges_not_bp7_decoder'}
