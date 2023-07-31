import first_file

def print_name_second_file():
    print("Second file name =",__name__)

def main():
    first_file.print_name_first_file()
    print_name_second_file()
    
if (__name__ == "__main__"):
    main()
