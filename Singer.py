class Singer:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.musics=[]
    def add_own_music(self,music):
        self.musics.append(music)
    
        
        