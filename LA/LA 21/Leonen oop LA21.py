class AdobongPorkandChicken:
    def __init__(self, pork, chicken, toyo, suka):
        self.__pork = pork
        self.__chicken = chicken
        self.__toyo = toyo
        self.__suka = suka
    def __str__(self):
        return f"adobo ko may {self.__pork}, {self.__chicken}, {self.__toyo} at {self.__suka}"
    def may_pork_ba(self, religion):
        if religion >= "Muslim":
            return self.__pork
        else:
            return "Meron"
    def i_set_to(self,baguhin):
        self.__pork = baguhin
ForkandChimkenadobo = AdobongPorkandChicken("babuy", "chiken", "tuyu", "soka")
ForkandChimkenadobo.i_set_to("beep")
print(ForkandChimkenadobo.may_pork_ba("Muslim"))