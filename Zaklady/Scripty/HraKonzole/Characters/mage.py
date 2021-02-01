from .character import *

class mage(character):
    def __init__(self,hp=65,energy=100,damage=110):
        self.type=3
        self.hp=hp
        self.energy=energy
        self.damage=damage

    def sleep(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Během spánku jsi byl přepaden. \nNezískal jsi žádnou energii")
               

        elif hod==2:
                print("Sotva jsi zamhouřil oči, okolní rámus tvému spánku rozhodně nedopřál!\nZískáváš 30 energie")
                self.energy=30
        elif hod==3:
            print("V průběhu spánku ses několikrát probudil kvůli nočním můrám !\nZískáváš 60 energie")
            self.energy=60

        elif hod==4 or hod==5:
            print("Po několika hodinách se probouzíš, ale spaní na tvrdé podložce nebylo to pravé!\nZískáváš 90 energie")
            self.energy=90

        elif hod==6:
           print("Bylo ti nabídnuto lůžko v blízkém hostinci, takhle dobře ses už dlouho nevyspal!\nZískáváš 120 energie")
           self.energy=120

    def heal(self):  
        hod=hodKostkou(1,8)
        print("\nHodil jsi: " + str(hod) + "\n")   

        if hod==1:
            print("Asi jsi trochu mimo, použil jsi lektvar na špatnou část těla.") 

        elif hod==2:
                print("Vypadá to, že tenhle lektvar je prošlý.\nZískáváš 30 hp.")
                self.hp=hp+30

        elif hod==3 or hod==5:
            print("Tvé léčení bylo úspěšné.\nZískáváš 45 hp.")
            self.hp=hp+45

        elif hod==4 or hod==6:
            print("Tvé léčení by snad oživilo i mrtvého.\nZískáváš 65 hp.")
            self.hp=hp+65