class example_class:
    class_list = []
    class_counter = 0
    def counter():
        class_counter += 1
        return class_counter
    def class_push():
        class_list.append(class_counter)
    def class_pop():
        return class_list.pop()
