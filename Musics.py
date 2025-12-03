import Music
import Singers
import Stack
class Musics:
    def __init__(self):
        self.allmusics=Stack.Stack()
    def add_music(self,name,singer,id,year,score,text):
        music=Music.Music(name,singer,id,year,score,text)
        self.allmusics.push(music)
        return music#change
    def search_music(self,name):
        for i in self.allmusics.stack:
            if(i.name==name):
                return printmusic(i)
        return print("We dont have music with name ",name)
    def delete_music(self,id):
        new_stack=Stack.Stack()
        for _ in range(self.allmusics.size()):
            if(self.allmusics.size()==0):
                break
            current_id=self.allmusics.peek()
            if(current_id==id):
                self.allmusics.pop()
            new_stack.push(self.allmusics.pop())
        self.allmusics=new_stack
        
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
    def printt_musics(self):
        for i in self.allmusics:
            printmusic(i)
    def search_music_by_id(self,id):
        for i in self.allmusics:
            if i.id==int(id):
                return i
        return None   
    def max_rated(self):
        min_rated=0
        for i in self.allmusics:
            if(float(i.score)>=min_rated):
                target_music=i
                min_rated=float(i.score)
        return printmusic(target_music)        
    def min_rated(self):
        max_rated=5
        for i in self.allmusics:
            if(float(i.score)<=max_rated):
                target_music1=i
                max_rated=float(i.score)
        return printmusic(target_music1)
def printmusic(music):
    print(f"name:{music.name} singer:{music.singer} year:{music.year} rating:{music.score} text:{music.text}")