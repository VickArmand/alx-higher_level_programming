#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    import sys
    operator = ['+', '-', '*', '/']
    func = [add, sub, mul, div]
    argc = len(sys.argv) - 1
    if (argc != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (sys.argv[2] not in operator):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        for i in range(4):
            if (op == operator[i]):
                print(f"{a} {op} {b} = {func[i](a, b)}")
