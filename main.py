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
        inputs = list(file.split(" "))
        

    if DEBUG: print(bfcode, mode, inputs, code)

    comp = Compiler(code, mode, inputs)
    compiled_code = comp.evaluate()

if __name__ == "__main__":
    main()
