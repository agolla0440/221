from my_first_module.file_with_function import add_strings

def main():
    """
    this is the main method which prints few lines and calls add_strings method from a file called
      my_first_module.file_with_function
    :return:
    """
    print("line 1")
    print("line 2")
    print("line 3")
    print("line 4")
    name = add_strings("ajay", "gollapalli")
    print(name)


def test():
    print("line 1 of test")


if __name__ == "__main__":
    test()
    print("Before calling the main function")
    main()

