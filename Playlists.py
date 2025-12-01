class Playlists:
    def __init__(self):
        self.all_play_list=[]
    def add_to_playlists(self,playlist):
        self.all_play_list.append(playlist)
    def show(self):
        for i in self.all_play_list:
            print(i.id,i.name)
    def search_by_id(self,id):
        for i in self.all_play_list:
            if i.id==id:
                return i
        return None