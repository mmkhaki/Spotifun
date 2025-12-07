import Stack
class Playlists:
    def __init__(self):
        self.all_play_list=Stack.Stack()
    def add_to_playlists(self,playlist):
        self.all_play_list.push(playlist)
    #تابع کمکی بلااستفاده است
    def show(self):
        for i in self.all_play_list.stack:
            print(i.id,i.name)
    def search_by_id(self,id):
        found=False
        new_stack=Stack.Stack()
        for _ in range(self.all_play_list.size()):
            current=self.all_play_list.peek()
            if current.id==id:
                found=True
                break
            new_stack.push(self.all_play_list.pop())
        while not new_stack.isEmpty():
            self.all_play_list.push(new_stack.pop())
        if(not found):
            return None
        else:
            return current
    def cls(self):
        self.all_play_list.stack=[]
    