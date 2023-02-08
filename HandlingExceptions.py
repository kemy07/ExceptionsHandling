def main ():
    # try:
    #     list = [30 , 20 , 54]
    #     print(list[3])
    # except:
    #     print("List is 3 Element only")
    try:
        file = open("sataurday.txt" , 'r')
    except:
        print("File is not Existed")
if __name__ == '__main__':
    main()