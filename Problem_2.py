def reverselist(x):
    result = []
    l = len(x)

    for i in range(l):
        j = -i-1    #Negatif sayılar için
        if type(x[j]) is list:  #Liste mi diye kontrol
            result.append(reverselist(x[j]))    #Eğer öyle ise yeniden döndür
        else:
            result.append(x[j])     #Aksi halde listenin sonuna ekle
    return result

x = [[1, 2], [3, 4], [5, 6, 7]]
print(reverselist(x))
