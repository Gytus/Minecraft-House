import math
from colorama import Fore

#Requesting Users input
x, z, y = int(input("Enter the value of x: ")), int(input("Enter the value of z: ")), int(input("Enter the value of y: "))

#Ar nori tokiu paciu namu
Tokie_patys_namai = str(input("Ar nori daugiau negu vieno namo? (True/False): "))
if Tokie_patys_namai == "True":
    Kiekis = int(input("Kiek namu nori?")) 
                                                       
#substracting 2 from every
x1 = x - 2
z1 = z - 2
y1 = y - 2
#devisioning for roof
stogas_z = z / 2 
stogas_y = y / 2

#checks if you need one door or two doors and substract them form kubas
duris = x % 2 
if x == 0:
    durys =  2
else:
    durys = 4

#Calculate corners
corners = y * 4
corner = corners / 2

#Calculate roof and floor and substract corners
pagrindas1 = (z * x ) * 2
pagrindas = pagrindas1 - corner

#calculate Sides
sides3 = ((x * y1) + (x1 * y1)) * 2
sides2 = sides3 - durys
sides = sides2 - corner

#calculating diagonal
stogo_istrizaine = math.pow(stogas_y, 2) + math.pow(stogas_z, 2)
stogo_istrizaine1 = math.sqrt(stogo_istrizaine)
stogo_istrizaine2 = int(stogo_istrizaine1)

#calculating full roof
z_su_pag = z + 2
full_stogo_side = stogo_istrizaine2 * z_su_pag
roof_side = z_su_pag * 2
stogas = (full_stogo_side * 2) + roof_side

#calculating triangle in roof
trikampis1 = 0.5 * (x -2) * y
trikampis = trikampis1 * 2

#no float
pagrindas0 = int(pagrindas)
sides0 = int(sides)
trikampis0 = int(trikampis)
corners0 = int(corners)
stogas0 = int(stogas)

#one time loop
if Tokie_patys_namai == "False":
    print(Fore.BLUE + "You will need these blocks:")
    print(Fore.RED + "Cobblestone: ", Fore.GREEN + str(pagrindas0))
    print(Fore.RED + "Wood planks: ", Fore.GREEN + str(sides0 + trikampis0))
    print(Fore.RED + "Wood logs: ", Fore.GREEN + str(corners0))
    print(Fore.RED + "Wood stairs: ", Fore.GREEN + str(stogas0))
    
#multiple time loop   
if Tokie_patys_namai == "True":
    print(Fore.BLUE + "You will need these blocks:")
    print(Fore.RED + "Cobblestone: ", Fore.GREEN + str(pagrindas0 * Kiekis))
    print(Fore.RED + "Wood planks: ", Fore.GREEN + str((sides0 + trikampis0) * Kiekis))
    print(Fore.RED + "Wood logs: ", Fore.GREEN + str(corners0 * Kiekis))
    print(Fore.RED + "Wood stairs: ", Fore.GREEN + str(stogas0 * Kiekis))
