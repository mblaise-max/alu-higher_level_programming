#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    count = len(argv) - 1
    print("{} argument{}{}".format(count, "" if count == 1 else "s",
                                   ":" if count else "."))
    for i in range(1, count + 1):
        print("{}: {}".format(i, argv[i]))
