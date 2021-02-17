from BrainFuckCompiler import Compiler

def main():
    DEBUG = str(input("Enable debug mode? (True/False) "))
    bfcode = str(input("Enter file you want to compiler: "))
    mode = str(input("Enter mode: "))
    input_file = str(input("Enter inputs file: "))

    with open(f"{bfcode}.bf", "r") as f:
        code = f.read()

    with open(f"{input_file}.txt", "r") as f:
        file = f.read()
        str_inputs = list(file.split(" "))
        int_inputs = [int(i) for i in str_inputs]
        if DEBUG: print(type(int_inputs[0]))
        

    if DEBUG: print(bfcode, mode, int_inputs, code)

    comp = Compiler(code, mode, int_inputs)
    compiled_code = comp.evaluate()

if __name__ == "__main__":
    main()
