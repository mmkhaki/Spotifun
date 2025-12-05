import Stack
class Playlist:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.musics=Stack.Stack()
    def add_music(self,music):
        self.musics.push(music)
    #checked ok
    def search_music(self,id):
        new_stack=Stack.Stack()
        found=False
        for _ in range(self.musics.size()):
            current=self.musics.peek()
            if(current.id==int(id)):
                while not new_stack.isEmpty():
                    self.musics.push(new_stack.pop())
                return current
            new_stack.push(self.musics.pop())
        while not new_stack.isEmpty():
            self.musics.push(new_stack.pop())
        if(not found):
            return print("We dont have music with name ",id)
        
    def delete_music(self,id):
        for i in self.musics:
            if(int(id)==i.id):
                self.musics.remove(i)
                return True
        return False

    def show_playlist(self):
        for i in self.musics.stack:
            print(i.name,i.text)
        
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
    
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])     
        right = self.merge_sort(arr[mid:])    
    
        return self.merge(left, right)


    def merge(self,left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i].year <= right[j].year:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
    def sort_playlist(self):
        newarr=self.merge_sort(self.musics)
        for i in newarr:
            print(i.name,i.text)
            