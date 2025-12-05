import Stack
class Playlists:
    def __init__(self):
        self.all_play_list=Stack.Stack()
    def add_to_playlists(self,playlist):
        self.all_play_list.push(playlist)
    def show(self):
        for i in self.all_play_list.stack:
            print(i.id,i.name)
    def search_by_id(self,id):
        for i in self.all_play_list.stack:
            if i.id==id:
                return i
        return None