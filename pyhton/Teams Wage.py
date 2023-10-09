driver = ["Sebastian Vettel","Charles Leclerc","Kevin Magnussen","Lando Norris"]
wage = [21,17,3,5]
for driver, wage in zip(driver,wage):
    print(driver,wage)
Totalwage = 0
for counter in range(4):
    Totalwage = Totalwage + wage
    print(Totalwage)
