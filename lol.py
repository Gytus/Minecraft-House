import math
from colorama import Fore

#Requesting Users input
x, z, y = int(input("Enter the value of x: ")), int(input("Enter the value of z: ")), int(input("Enter the value of y: "))

#Ar nori tokiu paciu namu
Same_House = str(input("Ar nori daugiau negu vieno namo? (True/False): "))
if Same_House == "True":
    Kiekis = int(input("How many houses do you want?")) 
                                                       
#substracting 2 from every
x1 = x - 2
z1 = z - 2
y1 = y - 2

#devisioning for roof
roof_z = z / 2 
roof_y = y / 2

#checks if you need one door or two doors and substract them form kubas
door = x % 2 
if x == 0:
    door =  2
else:
    door = 4

#Calculate corners
corners = y * 4
corner = corners / 2

#Calculate roof and floor and substract corners
base1 = (z * x ) * 2
base = base1 - corner

#calculate Sides
sides3 = ((x * y1) + (x1 * y1)) * 2
sides2 = sides3 - door
sides = sides2 - corner

#calculating diagonal
roof_diagonal = math.pow(roof_y, 2) + math.pow(roof_z, 2)
roof_diagonal1 = math.sqrt(roof_diagonal)
roof_diagonal2 = int(roof_diagonal1)

#calculating full roof
z_base = z + 2
full_roof_side = roof_diagonal2 * z_base
roof_one_side = z_base * 2
roof = (full_roof_side * 2) + roof_one_side

#calculating triangle in roof
trikampis1 = 0.5 * (x -2) * y
trikampis = trikampis1 * 2

#no float
pagrindas0 = int(base)
sides0 = int(sides)
trikampis0 = int(trikampis)
corners0 = int(corners)
stogas0 = int(roof)

#one time loop
if Same_House == "False":
    print(Fore.BLUE + "You will need these blocks:")
    print(Fore.RED + "Cobblestone: ", Fore.GREEN + str(pagrindas0))
    print(Fore.RED + "Wood planks: ", Fore.GREEN + str(sides0 + trikampis0))
    print(Fore.RED + "Wood logs: ", Fore.GREEN + str(corners0))
    print(Fore.RED + "Wood stairs: ", Fore.GREEN + str(stogas0))
    
#multiple time loop   
if Same_House == "True":
    print(Fore.BLUE + "You will need these blocks:")
    print(Fore.RED + "Cobblestone: ", Fore.GREEN + str(pagrindas0 * Kiekis))
    print(Fore.RED + "Wood planks: ", Fore.GREEN + str((sides0 + trikampis0) * Kiekis))
    print(Fore.RED + "Wood logs: ", Fore.GREEN + str(corners0 * Kiekis))
    print(Fore.RED + "Wood stairs: ", Fore.GREEN + str(stogas0 * Kiekis))
