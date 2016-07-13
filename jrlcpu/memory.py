import array

BYTE_LIMIT = 2**8
WORD_LIMIT = 2**16

# Class: Memory
#  Class representing a CPUs memory. Provides methods to read and writes
#  bytes/words to/from memory. Methods are not thread-safe. 
class Memory:

  # Function: __init__
  #  Creates a new Memory instance. Memory is used by the Executor
  #  when executing instructions. The Memory instance may be shared
  #  among multiple executors but assume that access is not thread-safe.
  #  Neither the set nor get functions are atomic. Executors may also
  #  each use their own instance of Memory.
  #
  # Parameters:
  #  self - implicit
  #  size - Size of the memory in bytes (default: 4MiB)
  #
  # Returns:
  #  Instance of Memory.
  def __init__(self, size = 4*1024*1024):
    self.mem = array.array('B', [0] * size)
    self.size = size
    
  # Function: getb
  #  Read one byte from memory at the specified address.
  #
  # Parameters:
  #  self - implicit
  #  addr - Address
  #
  # Returns:
  #  Byte at target address.
  #
  # Contract:
  #  : addr >= 0
  #  : addr < self.size
  def getb(self, addr):
    assert addr >= 0
    assert addr < self.size
  
    return self.mem[addr]
    
    
  # Function: setb
  #  Write one byte to memory at the specified address.
  #
  # Parameters:
  #  self - implicit
  #  addr - Address
  #
  # Returns:
  #  None
  #
  # Contract:
  #  : addr >= 0
  #  : addr < self.size
  #  : value >= 0 and value < BYTE_LIMIT
  def setb(self, addr, value):
    assert addr >= 0
    assert addr < self.size
    assert value >= 0 and value < BYTE_LIMIT
  
    self.mem[addr] = value
    
  # Function: getw
  #  Read one word from memory at the specified address.
  #  Note: little endian.
  #
  # Parameters:
  #  self - implicit
  #  addr - Address
  #
  # Returns:
  #  Word at target address.
  #
  # Contract:
  #  : addr >= 0
  #  : addr < size
  def getw(self, addr):
    assert addr >= 0
    assert addr < size
  
    return (self.mem[addr+1] << 8) | (self.mem[addr])
   
  # Function: setw
  #  Write one word to memory at the specified address.
  #  Note: little endian.
  #
  # Parameters:
  #  self - implicit
  #  addr - Address
  #
  # Returns:
  #  None.
  #
  # Contract:
  #  : addr >= 0
  #  : addr < self.size
  #  : value >= 0 and value < WORD_LIMIT
  def setw(self, addr, value):
    assert addr >= 0
    assert addr < self.size
    assert value >= 0 and value < WORD_LIMIT
  
    self.mem[addr+1] = (value >> 8) & 255
    self.mem[addr] = value & 255