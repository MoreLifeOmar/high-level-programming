#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hid = dir(hidden_4)
    for i in range(0, len(hid)):
        if (hid[i][0] != '_'):
            print(hid[i])
