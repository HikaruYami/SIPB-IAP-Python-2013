class ExampleClass:
    def __init__(self):
        self.class_counter = 0
        self.class_list = []
        print "Initialized!"
    def counter(self):
        self.class_counter += 1
        return self.class_counter
    def class_push(self):
        self.class_list.append(self.class_counter)
    def class_pop(self):
        return self.class_list.pop()
