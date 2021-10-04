# Author MB 09/30/2021

g = int(input("what was your grade this year"))

if g >= 93:
    print("you got A")
else:
    if g >= 90:
        print("you got A-")
    else:
        if g >= 87:
            print("you got B+")
        else:
            if g >= 83:
                print("you got B")
            else:
                if g >= 80:
                    print("you got B-")
                else:
                    if g >= 77:
                        print("you got C+")
                    else:
                        if g >= 73:
                            print("you got C")
                        else:
                            if g >= 70:
                                print("you got C-")
                            else:
                                if g >= 65:
                                    print("you got D+")
                                else:
                                    if g >= 60:
                                        print("you got D")
                                    else:
                                        print("you got F")
