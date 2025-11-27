class Music:
    def __init__(self,name,singer,id,year,score,text):
        self.name=name
        self.singer=singer
        self.id=id
        self.year=year
        self.score=score
        self.text=text
        
    def __str__(self):
        return f"Music => name: {self.name} | singer: {self.singer} | id: {self.id} | year: {self.year} | score: {self.score} | text: {self.text}"

    def __repr__(self):
        return self.__str__()