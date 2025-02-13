from stat_gambling import stat_array

class adnd_class():
    def __init__(self, stats:stat_array):
        self.stats:stat_array=stats
        self.level:int=1
    
    def __str__(self)->str:
        return "Str, Int, Wis, Dex, Con, Chr\n"+str(self.stats)


class cleric(adnd_class):

    def __init__(self, stats:stat_array):
        super.__init__(stats)
        self.abilities="""
            - Turn undead (PHB 20)
            - 2 weapon proficiencies (else -2 penalty)
            - One 1st lvl spell\n
        """
    
    def cleric_bonus():
        if self.stats.WIS > 15:
            self.abilities+="+10% XP gain"