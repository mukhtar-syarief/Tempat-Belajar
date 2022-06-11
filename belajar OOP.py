class Kendaraan:
    roda = 4
    lampu = 1 
    def __init__(self):
        self.lampu = 3

    def santai(self):
        print(self.lampu)

    @classmethod
    def ngebut(cls):
        print(cls.roda)
        print(cls.lampu)

    @staticmethod
    def jalan():
        print ("Berjalan")

    


motor = Kendaraan()
motor.santai()
Kendaraan.jalan()
Kendaraan.ngebut()
