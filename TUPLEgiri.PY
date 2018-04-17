def ge():
    print ("modul tuple giri")
tupa=(1, 2, 3, 4) #Menampilkan empat bilangan bulat positif pertama

tupb=(5, 6, 7, 8)#Menampilkan empat bilangan bulat positif berikutnya

tupc=tupa + tupb#Menggabungkan tupA dan tupB

tupd=tupc*2#tupD salinan dari tupC

print '\nMenampilkan Tuple D :',tupd

print '\nCetak Element ke-3 Tuple D :',tupd[3]

print '\nCetak 3 Element Terakhir Tuple D :',tupd[-3:]

print '\nCetak Panjang Tuple D :',len(tupd)
