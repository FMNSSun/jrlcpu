import jrlcpu
import time

m = jrlcpu.Memory()

m.setb(0, 1)
m.setb(1, 1)
m.setb(2, 0)
m.setb(3, 5)

cpu = jrlcpu.CPU()
e = jrlcpu.Executor(m, cpu)

i = 0

start = time.time()*1000

while i < 1000*1000:
  e.step()
  i += 1
  
stop = time.time()*1000
  
print ('MIPS: %f' % ((1000*1000) / ((stop - start)*1000)))