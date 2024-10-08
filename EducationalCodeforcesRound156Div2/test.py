from collections import namedtuple


# Enter your code here. Read input from STDIN. Print output to STDOUT
def my_function(a, b, *args):
    print(a, b, args)
    print(args)


if __name__ == "__main__":
    my_function(1, 2, 3)  # Kết quả: a=1, b=2, args=(3, 4, 5)
