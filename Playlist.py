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
                found=True
                break
            new_stack.push(self.musics.pop())
        while not new_stack.isEmpty():
            self.musics.push(new_stack.pop())
        if(not found):
            return None
        else:
            return current
        
    def delete_music(self,id):
        new_stack=Stack.Stack()
        found=False
        for _ in range(self.musics.size()):
            current=self.musics.peek()
            if(int(id)==current.id):
                self.musics.pop()
                found=True
                break
            new_stack.push(self.musics.pop())
        while not new_stack.isEmpty():
            self.musics.push(new_stack.pop())
        if(found):
            return found
        return False

    def show_playlist(self):
        for i in self.musics.stack:
            if(i is not None):
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
        newarr=self.merge_sort(self.musics.stack)
        for i in newarr:
            print(i.name,i.text)
            