import Stack
class Singer:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.musics=Stack.Stack()
    def add_own_music(self,music):
        self.musics.push(music)
    def find_music_by_id(self,id):
        new_stack=Stack.Stack()
        found=False
        for _ in range(self.musics.size()):
            current=self.musics.peek()
            if(current.id==int(id)):
                found=True
                return current
            new_stack.push(self.musics.pop())
        while not new_stack.isEmpty():
            self.musics.push(new_stack.pop())
        if(not found):
            return None
        
    def find_music_by_id_bool(self,id):
        new_stack=Stack.Stack()
        found=False
        for _ in range(self.musics.size()):
            current=self.musics.peek()
            if(current.id==int(id)):
                found=True
                return True
            new_stack.push(self.musics.pop())
        while not new_stack.isEmpty():
            self.musics.push(new_stack.pop())
        if(not found):
            return False
        
        
    def remove_own_music(self, id):
        new_stack=Stack.Stack()
        for _ in range(self.musics.size()):
            current2=self.musics.peek()
            if(current2.id==int(id)):
                self.musics.pop()
                break
            new_stack.push(self.musics.pop())
        while not new_stack.isEmpty():
            self.musics.push(new_stack.pop())            
        
    
        
    def __str__(self):
        return f"Singer => name: {self.name} | id: {self.id} | musics: \n{self.musics}"
    
    def __repr__(self):
        return self.__str__()
        