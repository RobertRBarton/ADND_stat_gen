from random import randint

def gen_stat()->int:
    return randint(1,6)+randint(1,6)+randint(1,6)

def normalized_number_str(number:int)->int:
    if number>=10:
        return str(number)+",  "
    else:
        return str(number)+",   "

class stat_array:
    def __init__(self,array:list[int]=list()):
        self.array=array
        if not array:
            for _ in range(6):
                self.array.append(gen_stat())
        
        self.STR:int=self.array[0]
        self.INT:int=self.array[1]
        self.WIS:int=self.array[2]
        self.DEX:int=self.array[3]
        self.CON:int=self.array[4]
        self.CHR:int=self.array[5]
        self.SUM:int=sum(self.array)
        self.is_good:bool=self.SUM>70

    def __str__(self)->str:
        output:str=""

        for i in range(6):
            output+=normalized_number_str(self.array[i])
        
        return output


class char_array:

    def __init__(self):
        self.chars:list[stat_array]=list()
        for _ in range(12):
            self.chars.append(stat_array())

    def __str__(self)->str:
        output:str="#    Str, Int, Wis, Dex, Con, Chr, Sum\n"

        for i, char in enumerate(self.chars):
            output+=normalized_number_str(i+1)+str(char)

            output+=str(char.SUM)+","

            if char.is_good:
                output+=" good"

            output+="\n"

        return output

def test_generation():
    var=1000000000
    total=0
    for _ in range(var):
        total+=gen_stat()
    
    print(f"Averaged out to {total/var}")

if __name__=="__main__":
    print("LET'S GO GAMBLING!")
    print(char_array())