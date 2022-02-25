MINIMUM_WAGE = 2324 # 2020
TIP = 2324/2

def take_number(min):
    number = int(input())
    while number < min:
        number = int(input("Hatalı giriş ! Lütfen tekrar giriniz: "))
    return number

def consultantEmployeeCounter():
    employeeCount = int(input("Lütfen acenteye bağlı olarak çalışan emlak danışmanı sayısını giriniz: "))
    while employeeCount < 0:
        employeeCount = int(input("Hatalı giriş ! Lütfen tekrar giriniz: "))
    return employeeCount

def check():
    check = input("Lütfen başka değer girmek isteyip istemediğinizi giriniz: ")
    while check not in ["e","E","h","H"]:
        check = input("Hatalı giriş ! Lütfen tekrar giriniz: ")
    return check

def for_Each_Estate(name_surname,saleCount,rentCount,totalPriceHouseSale,totalPriceHouseRent,totalPriceOfficeSale,totalPriceOfficeRent,totalPricePlotSale,totalPricePlotRent,priceChecker,maxSalePrice,maxSaleName,maxSaleType,maxRentHousePrice,maxRentHouseName,minWageRentCount):
    estate = input("Lütfen o an sattığınız ya da kiraladığınız emlak tipini giriniz [Konut, İş yeri, Arsa(K/k/İ/i/A/a)]: ")
    while estate not in ["k", "K", "İ", "i", "A", "a"]:
        estate = input("Hatalı giriş ! Lütfen tekrar giriniz: ")
    processType = input("Lütfen satış mı kiralama mı yaptığınızı giriniz:(S/s/K/k): ")
    while processType not in ["S", "s", "K", "k"]:
        processType = input("Hatalı giriş ! Lütfen tekrar giriniz: ")

    if processType =="s" or processType =="S":
        saleCount += 1
    else:
        rentCount += 1
    print("Lütfen satış/kira bedelini giriniz: ",end="")
    price = take_number(0)

    if processType == "k" and price > priceChecker or processType == "K" and price > priceChecker:
        priceChecker = price

    if estate == "k" and processType == "s" or estate == "k" and processType =="S" or estate == "K" and processType == "s" or estate == "K" and processType =="S":
        totalPriceHouseSale+= price
        if(maxSalePrice < price):
            maxSalePrice = price
            maxSaleType = "Konut"
            maxSaleName = name_surname
    if estate == "i" and processType == "s" or estate == "i" and processType =="S" or estate == "İ" and processType == "s" or estate == "İ" and processType =="S":
        totalPriceOfficeSale+= price
        if (maxSalePrice < price):
            maxSalePrice = price
            maxSaleType = "İş Yeri"
            maxSaleName = name_surname
    if estate == "a" and processType == "s" or estate == "a" and processType =="S" or estate == "A" and processType == "s" or estate == "A" and processType =="S":
        totalPricePlotSale+= price
        if (maxSalePrice < price):
            maxSalePrice = price
            maxSaleType = "Arsa"
            maxSaleName = name_surname
    if estate == "k" and processType == "k" or estate == "k" and processType =="K" or estate == "K" and processType == "k" or estate == "K" and processType =="K":
        totalPriceHouseRent+= price
        if (maxRentHousePrice < price):
            maxRentHousePrice = price
            maxRentHouseName = name_surname
        if(price > MINIMUM_WAGE):
            minWageRentCount += 1
    if estate == "i" and processType == "k" or estate == "i" and processType == "K" or estate == "i" and processType == "k" or estate == "İ" and processType == "K":
        totalPriceOfficeRent+= price
    if estate == "a" and processType == "k" or estate == "a" and processType == "K" or estate == "A" and processType == "k" or estate == "A" and processType == "K":
        totalPricePlotRent+= price
    return name_surname,saleCount,rentCount,totalPriceHouseSale,totalPriceHouseRent,totalPriceOfficeSale,totalPriceOfficeRent,totalPricePlotSale,totalPricePlotRent,priceChecker,maxSalePrice,maxSaleName,maxSaleType,maxRentHousePrice,maxRentHouseName,minWageRentCount

def consultantEmployeeInformation(employeeCount):
    saleCount_total = 0
    rentCount_total = 0
    houseSale_total = 0
    houseRent_total = 0
    officeSale_total = 0
    officeRent_total = 0
    plotSale_total = 0
    plotRent_total = 0

    maxSalePrice = 0
    maxSaleType = ""
    maxSaleName = ""

    maxRentHousePrice = 0
    maxRentHouseName = ""

    minWageRentCount = 0
    while employeeCount > 0:
        saleCount = 0
        rentCount = 0
        totalPriceHouseSale = 0
        totalPriceHouseRent = 0
        totalPriceOfficeSale = 0
        totalPriceOfficeRent = 0
        totalPricePlotSale = 0
        totalPricePlotRent = 0
        priceChecker = 0
        condition = "Doldurdu !"
        name_surname = input("Lütfen çalışan ad soyadını giriniz: ")
        print("Lütfen maaşınızı giriniz: ", end="")
        salary = take_number(2070)
        print("Lütfen kotayı giriniz: ",end="")
        quota = take_number(salary*10)
        checkInfo = "e"
        while checkInfo == "e" or checkInfo == "E":
            name_surname,saleCount,rentCount,totalPriceHouseSale,totalPriceHouseRent,totalPriceOfficeSale,totalPriceOfficeRent,totalPricePlotSale,totalPricePlotRent,priceChecker,maxSalePrice,maxSaleName,maxSaleType,maxRentHousePrice,maxRentHouseName,minWageRentCount = for_Each_Estate(name_surname,saleCount,rentCount,totalPriceHouseSale,totalPriceHouseRent,totalPriceOfficeSale,totalPriceOfficeRent,totalPricePlotSale,totalPricePlotRent,priceChecker,maxSalePrice,maxSaleName,maxSaleType,maxRentHousePrice,maxRentHouseName,minWageRentCount)

            checkInfo = check()

        saleCount_total += saleCount
        rentCount_total += rentCount
        houseSale_total += totalPriceHouseSale
        houseRent_total += totalPriceHouseRent
        officeSale_total += totalPriceOfficeSale
        officeRent_total += totalPriceOfficeRent
        plotSale_total += totalPricePlotSale
        plotRent_total += totalPricePlotRent

        if (totalPricePlotSale+totalPriceOfficeSale+totalPriceHouseSale+totalPricePlotRent+totalPriceOfficeRent+totalPriceHouseRent) < quota:
            condition = "Dolduramadı !"


        print("\nAd Soyad:", name_surname,
              "\nO ay sattığı emlak adedi: ", saleCount, "\nKiraladığı emlak adedi: ", rentCount, "\nOranları: %",format(saleCount / (rentCount + saleCount) * 100, ".2f"),
              "\nO ay Konut emlak tipi için toplam sattığı bedel: ",format(totalPriceHouseSale,".2f"),"TL",
              "\nO ay İş yeri emlak tipi için toplam sattığı bedel: ",format(totalPriceOfficeSale,".2f"),"TL",
              "\nO ay Arsa emlak tipi için toplam sattığı bedel: ",format(totalPricePlotSale,".2f"),"TL",
              "\nO ay kiraladığı emlakların ortalama kiralama bedeli: ",format((totalPriceHouseRent+totalPriceOfficeRent+totalPricePlotRent)/rentCount,".2f"),"TL",
              "\nO ay en yüksek bedelle kiraladığı konutun kira bedeli: ",format(priceChecker,".2f"),"TL",
              "\nO ay maaşı: ",format(salary,".2f"),"TL",
              "\nO ay kotası: ",format(quota,".2f"),"TL",
              "\nO ay acenteye kazandırdığı toplam komisyon bedeli: ",format((totalPricePlotSale+totalPriceOfficeSale+totalPriceHouseSale)*4/100+totalPriceHouseRent+totalPriceOfficeRent+totalPricePlotRent,".2f"),"TL",
              "\nO ay kotasını doldurup doldurmadığı: ",condition,
              "\nO ay kotasını doldurduysa alacağı ikramiye : ",format(TIP,".2f"),"TL",
              "\nO ay alacağı toplam ücret: ",format((salary+TIP),".2f"),"TL")

        employeeCount-=1
    print("\nToplam satılan emlak adedi: ",saleCount_total, "\nToplam kiralanan emlak adedi: ", rentCount_total, "\nSatılma oranları: %",format(saleCount_total / (rentCount_total+saleCount_total) *100,".2f"),
          "\nKonut emlak tipi için toplam satış bedeli: ",houseSale_total,"TL",
          "\nİş yeri emlak tipi için toplam satış bedeli: ",officeSale_total,"TL",
          "\nArsa emlak tipi için toplam satış bedeli: ",plotSale_total,"TL",
          "\nOrtalaması: ",format((houseSale_total + officeSale_total + plotSale_total) / 3,".2f"),"TL",
          "\nO ay en yüksek bedelle satılan emlağın tipi: ",maxSaleType , "\nSatış bedeli: ",maxSalePrice,"TL" , "\nSatışı yapan danışmanın adı-soyadı: ",maxSaleName,
          "\nO ay en yüksek bedelle kiralanan konutun kira bedeli: ", maxRentHousePrice,"TL", "\nSatışı yapan danışmanın adı-soyadı: ", maxRentHouseName,
          "\nO ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı: ", minWageRentCount, "\nKiralanan konutlar içindeki oranı: %",format(minWageRentCount / rentCount_total * 100,".2f"))

def main():

    employeeCount=consultantEmployeeCounter()
    consultantEmployeeInformation(employeeCount)

main()