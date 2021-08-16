def flat(l):
    t_l = [] #t_l bizim transform list'imiz olacak ondan boş olarak oluşturduk
    for i in l: #açtığımız for bloğu ile input olarak verilmiş l listesi üzerinde geziyoruz
        if isinstance(i, list): #isinstance sayesinde verilen listedeki elemanların çok katmanlı olup olmadığını kontrol edebiliyoruz
            t_l.extend(flat(i)) #true dönerse recrussive call oluyor yani fonksiyon kendi kendini çağrıyor
        else:
            t_l.append(i) #false dönerse zaten t_l listesinin sonuna ekleniyor.
    return t_l

l =  [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flat(l))

#geliştirilmesi gerekenler; kullanıcıdan listeyi input almak, denemelerim oldu fakat çok katmanlı örneklerde dönüşüm doğru olmuyor.
