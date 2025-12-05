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
            
    def delete_music_by_id(self,id):
        new_stack1=Stack.Stack()
        for _ in range(self.musics.size()):
            current_music=self.musics.peek()
            new_stack1.push(self.musics.pop())
            if(current_music.id==int(id)):
                new_stack1.pop()
                break
        while not new_stack1.isEmpty():
             self.musics.push(new_stack1.pop())
    def show(self):
        for i in self.musics.stack:
            print(i.__str__())
            