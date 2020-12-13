                          Frekvence slov v textu
==============================================================================
Program vypo��t� frekvenci v�skytu ka�d�ho platn�ho slova v souboru data.txt

Vstup:
- program p�ij�m� vlajku -min - pokud je po�et znak� dan�ho slova vy��� nebo roven hodnot� p�edan� vlajce min - program
  slovo p�id� do datab�ze - slova s men��m po�tem znak�, ne� je min jsou ignorov�na
- syntaxe: "WordFrequency.py -min 3" ignoruje v�echna slova, kter� maj� m�n� znak� ne� 3
- program ur�uje d�lku slova a� po odstran�n� znak� obsa�en�ch v listu remove - tzn. slovo "don't" po odstran�n� apostrofu
  obsahuje 4 znaky

Popis funkce:
- Program nahraje obsah souboru data.txt do pam�ti a rozd�l� text na jednotliv� slova (podle mezer a konc� ��dku)
- Z ka�d�ho slova odebere ne��douc� znaky (list remove) a p�evede v�e na mal� p�smena
- Vytvo�� se datab�ze unik�tn�ch slov a ke ka�d�mu slovu se p�i�azuje jeho v�skyt - program
  proch�z� v�echna upraven� slova a porovn�v� je se svoj� datab�z�, pokud slovo najde, p�i�te si 1 k jeho v�skytu
  pokud slovo v datab�zi nenajde - p�id� si ho do datab�ze a nastav� mu v�skyt 1
- program p�ij�m� jako vstup vlajku -min kter� definuje, kolik mus� m�t slovo minim�ln� znak�, aby bylo
  pova�ov�no za platn� a p�idalo se do datab�ze programu - je takto mo�n� odfiltrovat kr�tk� slova
- datab�ze m� charakter dvourozm�rn�ho pole (vno�en� listy do listu) 
  p�. database = [["ahoj", 2], ["pes", 3]] - slovo ahoj m� v�skyt 2, slovo pes m� v�skyt 3
  p��stup k prvk�m: database[1][0] vrac� pes, database[1][1] vrac� 3 