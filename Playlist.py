class Playlist:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.musics=[]
    def add_music(self,music):
        self.musics.append(music)
    def search_music(self,id):
        for i in self.musics:
            if(int(id)==i.id):
                return i
        return None
    def delete_music(self,id):
        for i in self.musics:
            if(int(id)==i.id):
                self.musics.remove(i)
                return True
        return False

    def show_playlist(self):
        for i in self.musics:
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
            