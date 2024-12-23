class Farteh:
    def __init__(self, name):
        self.name = name
    def __masarapnafood(self):
        print(f"Sfpesyal na foodVY: {self.name}")
    def NocheBuenas(self):
        print("Lechon Manok, Lumpia, Bibingka")
        self.__masarapnafood()
    def MediasNoche(self):
        print("Carbonara, Pork Belly, Pizza")
        self.__masarapnafood()

kare2x = Farteh("Kare-kare")
kare2x.NocheBuenas()
sisig = Farteh("Sisig")
sisig.MediasNoche()