from BrainFuckCompiler import Compiler

def main():
    DEBUG = str(input("Enable debug mode? (True/False) "))
    bfcode = str(input("Enter file you want to compiler: "))
    mode = str(input("Enter mode: "))
    num_of_inputs = int(input("How many inputs are there? "))
    inputs = [input("Input next number: ") for i in range(num_of_inputs)]

    if DEBUG: print(bfcode, mode, inputs)

    with open(f"{bfcode}.bf", "r") as f:
        code = f.read()

        comp = Compiler(code, inputs, mode)
        compiled_code = comp.evaluate()

if __name__ == "__main__":
    main()
