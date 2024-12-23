class AdobongPorkandChicken:
    def __init__(self, pork, chicken, toyo, suka):
        self.__pork = pork
        self.__chicken = chicken
        self.__toyo = toyo
        self.__suka = suka
    def __str__(self):
        return f"adobo ko may {self.__pork}, {self.__chicken}, {self.__toyo} at {self.__suka}"
       
ForkandChimkenadobo = AdobongPorkandChicken("babuy", "chiken", "tuyu", "soka")
print(ForkandChimkenadobo)