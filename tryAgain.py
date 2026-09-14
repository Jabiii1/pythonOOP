class pc:
    def __init__(self, name, cpu, gpu):
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.powerOn = False
        self.playTime  = 0

    def PowerONPc(self):
        if self.powerOn:
            print(f"the{self.name} is already Power On!")
        else:
            self.powerOn = True
            print(f"the {self.name} is now powered on!")

    def powerOFFPc(self):
        if not self.powerOn:
            print(f"the {self.name} is already off.")
        else:
            self.powerOn = False
            print("Power Off!")

    def playgame(self,NumOfGamesPlayed):
        if not self.powerOn:
            print(f"the {self.name} is not On! Click the power button first!")
        else:
            self.playTime += NumOfGamesPlayed
            print(f"playtime {self.playTime}hr. total games played {NumOfGamesPlayed}games.")


pc1 = pc("pc1", "amd", "rtx5090")
pc2 = pc("pc2", "intel", "rtx4090")

pc2.powerOFFPc()
pc2.PowerONPc()
pc2.playgame(3)

