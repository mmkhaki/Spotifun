class Singer:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.musics=[]
    def add_own_music(self,music):
        self.musics.append(music)
    def find_music_by_id(self,id):
        for i in self.musics:
            if(i.id==int(id)):
                return i
        return None
    def remove_own_music(self,id):
        music=self.find_music_by_id(id)
        self.musics.remove(music)
        
    
        
    def __str__(self):
        return f"Singer => name: {self.name} | id: {self.id} | musics: \n{self.musics}"
    
    def __repr__(self):
        return self.__str__()
        