class Phone:
    def __init__(self,ram,memory):
        self.ram = ram
        self.memory = memory
        
    def capacity(self):
        c = self._helper_capacity()
        print("Capacity: ",c)
        
    def _helper_capacity(self):
        return self.ram*self.memory
        
Phone_A = Phone(3,5)
Phone_A.capacity()
