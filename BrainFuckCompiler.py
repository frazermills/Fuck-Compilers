DEBUG = True

class Compiler:
    def __init__(self, bfcode, mode=1):
        self.code = bfcode
        self.mode = mode

    def evaluate(self):
        if DEBUG: print(self.code)

        arr = [0]
        x = 0
        index = 0
        while_loop = []
        
        while x < len(self.code):

            if self.code[x] == "+":
                arr[index] += 1
                if arr[index] == 256:
                    arr[index] = 0

            elif self.code[x] == "-":
                arr[index] -= 1
                if arr[index] == -1:
                    arr[index] = 255

            elif self.code[x] == ">":
                index += 1
                if index == len(arr):
                    arr.append(0)
                    
            elif self.code[x] == "<":
                index -= 1
                if index < 0:
                    arr.insert(0, 0)
                    index += 1
                    
            elif self.code[x] == ".":
                print(chr(arr[index]),end="")

            elif self.code[x] == ",":
                arr[index] = ord(input(">>> "))

            elif self.code[x] == "[":
                while_loop.append(x)

            elif self.code[x] == "]":
                if arr[index] != 0:
                    x = while_loop[-1]
                else:
                    del while_loop[-1]
            x += 1
