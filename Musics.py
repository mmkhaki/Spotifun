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
        new_stack=Stack.Stack()
        found=False
        for _ in range(self.allmusics.size()):
            current=self.allmusics.peek()
            if(current.name==name):
                printmusic(current)
                found=True
            new_stack.push(self.allmusics.pop())
        while not new_stack.isEmpty():
                self.allmusics.push(new_stack.pop())
        if(not found):
            return print("We dont have music with name ",name)
    def delete_music(self,id):
        new_stack=Stack.Stack()
        for _ in range(self.allmusics.size()):
            current=self.allmusics.peek()
            if(current.id==int(id)):
                self.allmusics.pop()
                break
            new_stack.push(self.allmusics.pop())
        while not new_stack.isEmpty():
            self.allmusics.push(new_stack.pop())
        
    def max_rated(self):
        if self.allmusics.isEmpty():
            return None
        max_music = None
        max_score = -1
        new_stack=Stack.Stack()
        for _ in range(self.allmusics.size()):  
            current=self.allmusics.peek()
            if float(current.score) > max_score:
                max_score = float(current.score)
                max_music = current
            new_stack.push(self.allmusics.pop())
        while not new_stack.isEmpty():
            self.allmusics.push(new_stack.pop())
        return printmusic(max_music)

    def low_rated(self):
        if self.allmusics.isEmpty():
            return print("No musics found!")

        min_music = None
        min_score = float('inf')

        for music in self.allmusics.stack:
            if float(music.score) < min_score:
                min_score = float(music.score)
                min_music = music

        return printmusic(min_music)

    def printt_musics(self):
        for i in self.allmusics:
            printmusic(i)
    def search_music_by_id(self,id):
        new_stack=Stack.Stack()
        found=False
        for _ in range(self.allmusics.size()):
            current=self.allmusics.peek()
            if(current.id==int(id)):
                found=True
                break
            new_stack.push(self.allmusics.pop())
        while not new_stack.isEmpty():
            self.allmusics.push(new_stack.pop()) 
        if(not found):
            return None
        else:
            return current
    # def max_rated(self):
    #     min_rated=0
    #     for i in self.allmusics:
    #         if(float(i.score)>=min_rated):
    #             target_music=i
    #             min_rated=float(i.score)
    #     return printmusic(target_music)        
    # def min_rated(self):
    #     max_rated=5
    #     for i in self.allmusics:
    #         if(float(i.score)<=max_rated):
    #             target_music1=i
    #             max_rated=float(i.score)
    #     return printmusic(target_music1)
def printmusic(music):
    print(f"name:{music.name} singer:{music.singer} year:{music.year} rating:{music.score} text:{music.text}")