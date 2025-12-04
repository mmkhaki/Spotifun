class Music:
    def __init__(self,name,singer,id,year,score,text):
        self.name=name
        self.singer=singer
        self.id=id
        self.year=year
        self.score=score
        self.text=text
    
    def count_word(self,text, word):
        count = 0
        current = ""  # کلمه‌ای که داریم می‌سازیم
        for ch in text:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                current += ch
            else:
                if current == word:
                    count += 1
                current = ""  
                
        if current == word:
            count += 1

        return count
    def __str__(self):
        return f"Music => name: {self.name} | singer: {self.singer} | id: {self.id} | year: {self.year} | score: {self.score} | text: {self.text}"

    def __repr__(self):
        return self.__str__()