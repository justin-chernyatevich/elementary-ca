import sys
import random
import shutil

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def frul(array):
    result = []
    if len(array) == 2:
        if isint(array[1]) and (int(array[1]) >= 0 and int(array[1]) <= 255):
            template = {"111":"0", "110":"0",
                        "101":"0", "100":"0",
                        "011":"0", "010":"0",
                        "001":"0", "000":"0"}
            t_num = list(bin(int(array[1]))[2:].rjust(8).replace(" ", "0"))
            count = 0
            for i in template:
                if count < len(t_num):
                    template[i] = t_num[count]
                    count += 1
            result.append(template)
            return result
        elif not isint(array[1]):
            sys.stderr.write("The argument must be a number. Try again.\n")
            return "Error"
        else:
            sys.stderr.write("The number cannot be less than 0 and more than 255. Try again.\n")
            return "Error"
    return result

def play_ca(size=100, rules={"111":"0", "110":"1", "101":"0", "100":"1", "011":"1", "010":"0", "001":"1", "000":"0"}, steps=35):
    l = [random.randint(0, 1) for i in range(size)]
    l2 = l.copy()
    l[len(l) // 2] = 1
    ffi = lambda x : ((len(l) + x) % len(l))

    def print_l():
        print("\n".join(["".join([str(i)+"*" for i in l])]).\
              replace("1*", "\x1b[41m\x1b[31m \x1b[0m").replace("0*", "\x1b[47m \x1b[0m"))
    print_l()
    for i in range(steps):
        for j in range(len(l)):
            cursor = j
            left = ffi(cursor - 1)
            right = ffi(cursor + 1)
            sp_str = str(l[left]) + str(l[cursor]) + str(l[right])
            l2[cursor] = int(rules[sp_str])
        l = l2.copy()
        print_l()

if __name__ == "__main__":
    sp_value = frul(sys.argv)
    cols, rows = shutil.get_terminal_size()
    if type(sp_value) != str:
        print("\033[2J", end="")
        print("\033[0;0H", end="")
        if len(sp_value) == 1:
            play_ca(size=cols, steps=rows - 2, rules=sp_value[0])
        else:
            play_ca(size=cols, steps=rows - 2)
