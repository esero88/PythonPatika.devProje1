def reverselist(x):
    result = []
    l = len(x)

    for i in range(l):
        j = -i-1    #Negatif sayılar için
        if type(x[j]) is list:  #Liste içinde liste var mı diye kontrol
            result.append(reverselist(x[j]))    #Eğer öyle ise reverselist(x) için alt listeyi döndür ve result listesine ekle
        else:
            result.append(x[j])     #Aksi halde result listesinin sonuna ekle
    return result

x = [[1, 2], [3, 4], [5, 6, 7]]
print(reverselist(x))
