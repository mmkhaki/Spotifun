import Stack
import Queue
class Playlist:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.musics=Queue.Queue()
    
    #checked ok
    #edited to queue
    def add_music(self,music):
        self.musics.enqueue(music)
    #checked ok
    #edited to queue
    
    def search_music(self,id):
        new_queue=Queue.Queue()
        found_item=None
        while not self.musics.is_empty():
            item=self.musics.dequeue()
            if(item.id==int(id)):
               found_item=item
            new_queue.enqueue(item)
        self.musics=new_queue
        return found_item

        # for _ in range(self.musics.size()):
        #     if(not found):
        #         current=self.musics.peek()
        #     if(current.id==int(id)):
        #         found=True
        #     new_queue.enqueue(self.musics.dequeue())
        # self.musics=new_queue
        # if(not found):
        #     return None
        # else:
        #     return current
        
    #checked ok
    #edited to queue
      
    def delete_music(self,id):
        new_queue=Queue.Queue()
        found=False
        while not self.musics.is_empty():
            item=self.musics.dequeue()
            if item.id==int(id):
                found=True
                continue
            new_queue.enqueue(item)
        self.musics=new_queue
        return found

    #checked ok
    #edited to queue
    
    def show_playlist(self):
        new_queue=Queue.Queue()
        for _ in range(self.musics.size()):
            current=self.musics.peek()
            print(current.name,current.singer)
            new_queue.enqueue(self.musics.dequeue())
        self.musics=new_queue
                
    #checked ok
    #edited to queue 
     
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
    
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])     
        right = self.merge_sort(arr[mid:])    
    
        return self.merge(left, right)

    #checked ok
    #edited to queue 
     
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
    
    #checked ok
    #edited to queue 
     
    def sort_playlist(self):
        newarr=self.merge_sort(self.musics.queue)
        for i in newarr:
            print(i.name,i.text)
            