# This class keeps variables synced between modules, because otherwise the interpreter has a seperate instance in each module
class ModuleVariable:
    def __init__(self, val):
        self.value = val;
    # Use this when setting the value, otherwise it will not work properly.
    def set(self, val):
        self.value = val;
    # Use this when getting the value, otherwise it will not work properly.
    def get(self):
        return self.value;

# The functions added to this 
loop_callback_list = ModuleVariable([]);
