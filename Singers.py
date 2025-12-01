class Singers:
    def __init__(self, max_value):
        self.sparse = [-1] * (max_value + 1)
        self.dense = []
        self.max_value=max_value
    
    def contains(self, x):
        idx = self.sparse[x]
        return idx != -1 and self.dense[idx].id == x

    def add(self, x):
        if not self.contains(x.id):
            self.sparse[x.id] = len(self.dense)
            self.dense.append(x)
        else:
            print("We have a singer with id ",x.id)

    def remove(self, x):
        if not self.contains(x):
            print("We dont have a singer with id ",x)
            return
        idx = self.sparse[x]          # محل x در dense
        last = self.dense[-1]         # آخرین عنصر
        self.dense[idx] = last        # جابجایی
        self.sparse[last.id] = idx       # آپدیت sparse
        self.dense.pop()              # حذف آخر
        self.sparse[x] = -1           # علامت حذف

    def __iter__(self):
        return iter(self.dense)

    def finds(self,x):
        if self.contains(x):
            singer=self.dense[self.sparse[x]]
            printSinger(singer)
            print_singer_music(singer)
            
        else:
            print("We dont have a singer with id ",x)
    def find_by_name(self,name):
        for i in self.dense:
            if(i.name==name):
                return i
        return None
    def find_by_id(self,id):
        singer_indx=self.sparse[int(id)]
        singer_target=self.dense[int(singer_indx)]
        return singer_target
    def prints(self):
        printSingers(self.dense)
                
        
    def cls(self):
        self.sparse = [-1] * (self.max_value + 1)
        self.dense=[]
        





def printSingers(singers):
    if len(singers)==0:
        print("No singer")
        return
    for i in singers:
        print(f"Singer_id:{i.id} Singer_name:{i.name}")
def printSinger(singer):
        print(f"id:{singer.id} name:{singer.name}")
def print_singer_music(singer):
        for i in singer.musics:
            print(f"music name:{i.name} music singer:{i.singer} music id:{i.id} music year:{i.year} music score:{i.score} music text:{i.text}")
    