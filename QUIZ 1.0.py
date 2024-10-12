
import time


print("Ahoj, já jsem jednodochý kvíz :-)")
print("Tuto hru vytvořil NNW Developer")
print("Pravidla:")
print("Hra začíná výběrem A/N, pokud chcete hrát napište A pokud nechcete napište N, když napíšete N tak vám to napíše: Aha, tak nic :-(   Tak snad příště. Pro ukončení zavři hru křížkem.   V tuto chvíli opustíte hru zmáčknutím křížku. Pokud dáte A, tak se Vám spustí kvíz. Vždy máte na výběr ze tří otázek, do pole pak napíšete pouze číslo dané otázky bez tečky. To znamená, že když budu chtít odpovědět odpovědí č.3, tak napíšu pouze číslo 3 atd. Při zadání špatné odpovědi se hra automaticky po 15ti sekundách zavře, pokud nechcete čekat, zavřete ji sami a spusťte znova pro opravu Vaší odpovědi. Užijte si hru :-)")

print("Jsi připravený?  A/N")
promnena1= input()
if promnena1 == ("A"):print("Dobře, jdeme na to :-)")
if promnena1 == ("N"):print("Aha, tak nic :-(   Tak snad příště. Pro ukončení zavři hru křížkem.")



print("1. Kdo byl Václav Havel")



print("1. ","Budoucí manžel od Shopaholic Adel")
print("2. ","1. prezident České Republiky")
print("3. ","2. syn od Andreje Babiše")

x1 = input()
if x1 == ("2"):print("Ano, správně. Druhá otázka: Kdy vznikla samostatná Československá republika?")

print("1. ","1918")
print("2. ","2013")
print("3. ","1914")

x2 = input()
if x2 == ("1"):print("Ano správně, třetí otázka: Co to je Perl ?")

print("1. ","Mužská verze od mořské perly")
print("2. ","Označení hloupého velblouda")
print("3. ","Programovací jazyk")

x3 = input()
if x3 == ("3"):print("Ano správně, Dokončil jsi kvíz, pokud jsi byl spokojený, nebo tě napadají další otázky, které bych měl doplnit, tak mi napiš na https://nonamewebsite.neocities.org/formular.html")




time.sleep(15)


