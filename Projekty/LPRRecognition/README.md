## Projekt pro rozpozn�v�n� SPZ v OpenCV

TODO:
1)	Sezn�men� se s jazykem Python a knihovnou OpenCV.
	-instalace OpenCV a propojen� s projektem.

2)	Inspirace podle projektu na Git : "https://github.com/MicrocontrollersAndMore/OpenCV_3_License_Plate_Recognition_Python?fbclid=IwAR1T5z2nZTCi4HFX0SVd_A_QxJEiinoNS_uQmzagPfS2m3M1_H_GmHAhSZ8"

3)	Vytvo�en� si podprogramu "strojov�ho u�en� �ten� znak�". Zvol�me vlastn� fonty, kter� se nej�ast�ji pou��vaj� na SPZ.
	-vygenerov�n� .txt souborou, kter� budou pou�ity k rozpozn�v�n� SPZ

4)	Samotn� program na rozezn�n� SPZ:
	Nalezen� zna�ky
	-P�evod obr�zku na �ernob�l�
	-Nalezen� mo�n�ch znak� v obr�zku
	-Vytvo�en� vektoru mo�n�ch znak�, kter� jsou u sebe a mohou tvo�it SPZ
	-Vyjmut� vektoru mo�n�ch znak� z obr�zku a ulo�en� do listu
	-Zv�t�en� a zam��en� se na listy kde se vyskytuj� znaky
	-Znovu p�evod obr�zku na �ernob�l�
	-Rozpozn�n� znak� na zna�ce
	-Vybr�n� zna�ky, kter� m� bu� nejv�ce mo�n�ch znak� nebo ur�it� standardizovan� po�et znak�
	-Vyjmut� t�to zna�ky z listu a porovn�n� se znaky
	-Pot� uk�z�n� v�sledku ve form� okna a znak� pod n�m napsan�ch + vypsan�

//*Mo�n� rozeps�n� krok� a p�ips�n� n�kter�ch chyb�j�c�ch, nebo v p��pad� nara�en� na dal�� probl�my, mo�nost rozepsat*//


Auto�i: des. Edita Bo�kov�, des. Daniel Popel��, des. Lubom�r Hork�
