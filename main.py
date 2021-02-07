from BrainFuckCompiler import Compiler

DEBUG = True

def main():
    bfcode = str(input("Enter file you want to compiler: "))
    with open(f"{bfcode}.txt", "r") as f:
        code = f.read()
    
        comp = Compiler(code)
        compiled_code = comp.evaluate()

if __name__ == "__main__":
    main()
