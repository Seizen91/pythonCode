# python3异常
import sys


def demo1():
    while True:
        try:
            x = int(input("Please enter a number:"))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again ")


def demo2():
    try:
        f = open('tmp/myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

#demo2()


def demo3():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
            print("hello")
        except IOError:
            print("cannot open", arg)
        # else子句必须放在所有except子句之后，它将在try没有发生任何异常时执行
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


# demo3()

def this_fails():
    x = 1/0


def demo4():
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)


#demo4()


def demo5():
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise


# demo5()


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
