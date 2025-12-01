class Playlist:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.musics=[]
    def add_music(self,music):
        self.musics.append(music)
    def search_music(self,id):
        for i in self.musics:
            if(id==i.id):
                return True
        return False
    def delete_music(self,id):
        for i in self.musics:
            if(id==i.id):
                self.musics.remove(i)
                return True
        return False
    def show_playlist_sorted(self):
        sort_musics=[]
        for i in self.musics:
            sort_musics.append(i)