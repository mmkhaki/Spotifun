import Stack
import Singers
class History:
    def __init__(self):
        self.musics=Stack.Stack()
        self.count=0
    def play_music(self,music):
        self.musics.push(music)
        for i in self.musics.stack:
            print(i.__str__())
            
    def undo(self):
        if(self.count==0):
            print(self.musics.peek())
            self.count+=1
            return
        new_stack=Stack.Stack()
        for _ in range(self.count):
            new_stack.push(self.musics.pop())
        print(self.musics.peek())
        for _ in range(self.count):
            self.musics.push(new_stack.pop())
        self.count+=1
        
        
    
    def show(self):
        for i in self.musics.stack:
            print(i.__str__())