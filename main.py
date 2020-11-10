from Classes.code import Code

def main():
    f = open("code.txt","r+").read()
    code = Code(f)
    code.split()
    code.splitKeywork()
    # TODO: Analyze By Line Not By Keyword
    result = code.analyze()
    print(result.functions)
    print(result.math_operations)
    print(result.assign_operations)
    print(result.line_indentation)
    print(result.lines_of_code)
    print(result.classes)
    
    

main()
