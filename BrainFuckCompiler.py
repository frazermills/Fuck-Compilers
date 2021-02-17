DEBUG = True

class Compiler:
    def __init__(self, bfcode, mode, inputs):
        self.code = bfcode
        self.mode = mode
        self.inputs = inputs
        if len(inputs) == 1:
            self.take_inputs = False
        else:
            self.take_inputs = True

    def evaluate(self):

        arr = [0 for i in range(25)]
        input_index = int(0)
        bfcode_index = 0
        arr_index = 0
        while_loop = []
        
        while bfcode_index < len(self.code):
            if DEBUG: print(bfcode_index, arr)

            if self.code[bfcode_index] == "+":
                arr[arr_index] += 1
                if arr[arr_index] == 256:
                    arr[arr_index] = 0

            elif self.code[bfcode_index] == "-":
                arr[arr_index] -= 1
                if arr[arr_index] == -1:
                    arr[arr_index] = 255

            elif self.code[bfcode_index] == ">":
                arr_index += 1
                if arr_index == len(arr):
                    print("out of range")
                    
            elif self.code[bfcode_index] == "<":
                arr_index -= 1
                if arr_index < 0:
                    arr.insert(0, 0)
                    arr_index += 1
                    
            elif self.code[bfcode_index] == ".":
                if self.mode == "char":
                    print(chr(arr[arr_index]), end="")
                elif self.mode == "int":
                    print(chr(arr[arr_index]), end=" ")
                else:
                    print(arr[arr_index])

            elif self.code[bfcode_index] == "," and self.take_inputs:
                
                if self.inputs[input_index] == "end":
                    self.take_inputs = False                    
                else:
                    num = self.inputs[input_index] + 48
                    arr[arr_index] = num
                    input_index += 1

            elif self.code[bfcode_index] == "[":
                while_loop.append(bfcode_index)

            elif self.code[bfcode_index] == "]":
                if arr[arr_index] != 0:
                    bfcode_index = while_loop[-1]
                else:
                    del while_loop[-1]
            
            bfcode_index += 1
            
