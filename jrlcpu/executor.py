
class Executor:

  def __init__(self, memory, cpu):
    self.memory = memory
    self.cpu = cpu
    
    self.instructions = {
      0 : self.ins_rst,
      1 : self.ins_add
    }
    
  def step(self):
    op = self.memory.getb(self.cpu.ip)
    regs = self.memory.getb(self.cpu.ip + 1)
    
    self.cpu.ip += 2
    
    self.instructions[op](regs)
    
  def ins_rst(self, regs):
    self.cpu.ip = 0
    
  def ins_add(self, regs):
    self.cpu.c += 1