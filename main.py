from BrainFuckCompiler import Compiler

DEBUG = True

def main():
    with open("code.txt", "r") as f:
        code = f.read()
    
        comp = Compiler(code)
        compiled_code = comp.evaluate()

if __name__ == "__main__":
    main()
