import Singers
import Singer
import Musics
import Music
singers=Singers.Singers(100)
musics=Musics.Musics()
# singer1=Singer.Singer("Tataloo",1)
# music2=Music.Music("Delbar","Tataloo",1,2000,4,"Man bahat ghahram vali22 ...")
# singer1.add_own_music(music2)
# print(singer1.musics[0].name
# )
# music22=singer1.find_music_by_id(1)
# print(music22.name)
# singer2=Singer.Singer("chavoshi",2)
# singer3=Singer.Singer("chavoshi",4)
# music1=Music.Music("Manbahat",1,1998,5,"Man bahat ghahram vali ...")
# singer1.add_own_music(music1)
# music3=Music.Music("Salam",3,2020,1,"Man bahat ghahram vali33 ...")
# musics.add_music(music1)
# musics.add_music(music2)
# musics.add_music(music3)
# musics.search_music("Salam")
# print(musics.delete_music(3))
# musics.search_music("Salam")
request=input()
arr=request.strip().split()
func=arr[0]
i=0
while True:
    if(i!=0):
        request=input()
        arr=request.strip().split()
        func=arr[0]
    i=1
    if func=="adds":
        singer=Singer.Singer(arr[2],int(arr[1]))
        singers.add(singer)
        
    elif func=="dels":
        id=int(arr[1])
        singers.remove(id)
        
    elif func=="finds":
        id=int(arr[1])
        singers.finds(id)
        
    elif func=="prints":
        singers.prints()
        
    elif func=="cls":
        singers.cls()
    
    elif func=="findms":
        target_name=arr[1]
        musics.search_music(target_name)
    elif func=="addms":
        music_name=arr[1]
        singer_name=input()
        music_year=input()
        music_score=input()
        music_text=input()
        text=[]
        while music_text!="$end":
            start = music_text.find('"') + 1
            end = music_text.find('"', start)
            result = music_text[start:end]
            text.append(result)
            music_text=input()
        music_text=" ".join(text)
        target_music=musics.add_music(music_name,singer_name,11,music_year,music_score,music_text)
        print("Target music name:",target_music.name)
        target_singer=singers.find_by_name(singer_name)
        print("Target singer name:",target_singer.name)
        target_singer.add_own_music(target_music)
        print(f"Saved successfully {music_name}")
    elif func=="delms":
        singer_id=arr[1]
        musics_id=arr[2]
        musics.delete_music(musics_id)
        target_singer=singers.find_by_id(singer_id)
        target_singer.remove_own_music(musics_id)
        
    elif func=="searchw":
        print("searchw")
    elif func=="countw":
        print("countw")
    elif func=="dels":
        print("dels")
    elif func=="addp":
        print("addp")
    elif func=="addmp":
        print("addmp")
    elif func=="searchp":
        print("searchp")
    elif func=="searchmp":
        print("searchmp")
    elif func=="delmp":
        print("delmp")
    elif func=="showp":
        print("showp")
    elif func=="playm":
        print("playm")
    elif func=="undo_playm":
        print("undo_playm")
    elif func=="quit":
        print("Goodbye")
        break
    else:
        print("Invalid request")
 
    
    
    