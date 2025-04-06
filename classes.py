from stat_gambling import stat_array, normalized_number_str


class adnd_class:
    def __init__(self, stats:stat_array):
        self.stats:stat_array=stats
        self.level:int=1
        self.abilities:str=""
        self.name:str="class"

        self.spell_slots:list[int]=[0,0,0,0,0,0,0,0,0,0]
    
    def __str__(self)->str:
        stat_line:str="Str, Int, Wis, Dex, Con, Chr\n"+str(self.stats)
        class_abilities:str=self.name+" abilities"+"/n"+self.abilities
        return stat_line+"/n/n"+class_abilities

class cleric(adnd_class):

    name="Cleric"

    def __init__(self, stats:stat_array):

        super().__init__(stats)

        self.abilities="""- Turn undead (PHB 20)\n- 2 weapon proficiencies (else -2 penalty)\n- One 1st lvl spell\n"""

        self.spell_slots[1]+=1

        self.name="Cleric"

        if self.stats.WIS > 15:
            self.abilities+="- +10% XP gain\n"

class Druid(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.abilities="""- Turn undead (PHB 20)\n- 2 weapon proficiencies (else -2 penalty)\n- One 1st lvl spell\n"""

        self.name="Druid"

        if self.stats.WIS > 15 and self.stats.CHR > 15:
            self.abilities+="- +10% XP gain\n"

class Fighter(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Fighter"

class Paladin(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Paladin"

class Ranger(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Ranger"

class Magic_user(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Magic-User"

class Illusionist(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Illusionist"

class Thief(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Thief"

class Assassin(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Assassin"

class Monk(adnd_class):
    def __init__(self, stats:stat_array):
        super().__init__(stats)

        self.name="Monk"
