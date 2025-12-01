import Music
class Musics:
    def __init__(self):
        self.allmusics=[]
    def add_music(self,name,id,year,score,text):
        music=Music.Music(name,id,year,score,text)
        self.allmusics.append(music)
    def search_music(self,name):
        for i in self.allmusics:
            if(i.name==name):
                return printmusic(i)
        return print("We dont have music with name ",name)
    def delete_music(self,id):
        for i in self.allmusics:
            if(i.id==id):
                self.allmusics.remove(i)
                return True
        return False
    def max_rated(self):
        low_score=0
        target_music=None
        for i in self.allmusics:
            if(i.score>low_score):
                target_music=i
                low_score=i.score
        return target_music
    def low_rated(self):
        high_score=5
        target_music=None
        for i in self.allmusics:
            if(i.score<high_score):
                target_music=i
                high_score=i.score
        return target_music
            
        
def printmusic(music):
    print(f"name:{music.name} year:{music.year} rating:{music.score} text:{music.text}")