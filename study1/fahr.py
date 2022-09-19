
if __name__ == "__main__":

    fahr = True
    print("Exit : input 0 ")
    while fahr :
        fahr = input()
        if fahr.isdigit():
            fahr = int(fahr)
            celsius = 5 / 9 * (fahr - 32)
            print("celsius: %.2f" % celsius)
        else:
            print("error")
