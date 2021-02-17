DEBUG = True

class Compiler:
    def __init__(self, bfcode, mode, inputs):
        self.code = bfcode
        self.mode = mode
        self.inputs = inputs

    def evaluate(self):

        arr = [0 for i in range(50)]
        input_index = int(0)                        # index of the inputs
        p = 0                                       # pointer location
        arr_index = 0                               # index of array
        while_loop = []
        
        while p < len(self.code):

            if self.code[p] == "+":
                arr[arr_index] += 1
                if arr[arr_index] == 256:
                    arr[arr_index] = 0

            elif self.code[p] == "-":
                arr[arr_index] -= 1
                if arr[arr_index] == -1:
                    arr[arr_index] = 255

            elif self.code[p] == ">":
                arr_index += 1
                if arr_index == len(arr):
                    arr.append(0)
                    
            elif self.code[p] == "<":
                arr_index -= 1
                if arr_index < 0:
                    arr.insert(0, 0)
                    arr_index += 1
                    
            elif self.code[p] == ".":
                if self.mode == "char":
                    print(chr(arr[arr_index]), end="")
                elif self.mode == "int":
                    print(chr(arr[arr_index]), end=" ")
                else:
                    print(arr[arr_index])

            elif self.code[p] == ",":
                num = self.inputs[input_index] + 48
                arr[arr_index] = num
                input_index += 1

            elif self.code[p] == "[":
                while_loop.append(p)

            elif self.code[p] == "]":
                if arr[arr_index] != 0:
                    p = while_loop[-1]
                else:
                    del while_loop[-1]
            p += 1
            
