def readcurrency(filename):
    with open(filename,'r') as file:
        currency = file.read().splitlines()
    listofdics = []
    dic = {}
    print (currency)
    for lines in currency:
        print (lines)
        dic['symbol'] = lines.split()[0]
        dic['rate'] = lines.split()[1]
        listofdics.append(dic)
    print (listofdics)
readcurrency('currency.txt')
