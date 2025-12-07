import Singers
import Singer
import Musics
import Music
import Playlists
import Playlist
import History
import Stack
singers = Singers.Singers(100)
musics = Musics.Musics()
playlists = Playlists.Playlists()
history = History.History()
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

def start():
    request = input()
    arr = request.strip().split()
    func = arr[0]
    i = 0
    while True:
        if (i != 0):
            request = input()
            arr = request.strip().split()
            func = arr[0]
        i = 1
        #checked
        if func == "adds":
            if(int(arr[1])>100):
                print("Invalid id (Should be smaller than 100)")
                continue
            
            singer = Singer.Singer(arr[2], int(arr[1]))
            singers.add(singer)

        #checked
        elif func == "dels":
            id = int(arr[1])
            singers.remove(id)

        #checked
        elif func == "finds":
            id = int(arr[1])
            singers.finds(id)
        
        #checked
        elif func == "prints":
            singers.prints()

        #checked
        elif func == "cls":
            singers.cls()
            musics.cls()
            playlists.cls()
            history.cls()

        #checked
        elif func == "findms":
            target_name = arr[1]
            musics.search_music(target_name)

        #checked
        elif func == "addms":
            music_name = arr[1]
            singer_name = input()
            music_year = input()
            music_score = input()
            music_text = input()
            text = []
            while music_text != "$end":
                start = music_text.find('"') + 1
                end = music_text.find('"', start)
                result = music_text[start:end]
                text.append(result)
                music_text = input()
            music_text = " ".join(text)
            target_singer = singers.find_by_name(singer_name)
            if(target_singer is not None):
                target_music = musics.add_music(music_name, singer_name, musics.allmusics.size(
                ), music_year, music_score, music_text)
                target_singer.add_own_music(target_music)
                print(f"Saved successfully {music_name}")
            else:
                print(f"Please Try again we dont have singer with name {singer_name}")

        elif func == "delms":
            singer_id = arr[1]
            musics_id = arr[2]
            musics.delete_music(musics_id)
            target_singer = singers.find_by_id(singer_id)
            target_singer.remove_own_music(musics_id)
            # delete from playlists
            new_stack = Stack.Stack()
            counter = playlists.all_play_list.size()
            for _ in range(counter):
                current_playlist = playlists.all_play_list.peek()
                current_playlist.delete_music(musics_id)
                new_stack.push(playlists.all_play_list.pop())
            while not new_stack.isEmpty():
                playlists.all_play_list.push(new_stack.pop())
            history.delete_music_by_id(musics_id)

        elif func == "searchw":
            singer_id6=arr[1]
            music_id6=arr[2]
            word=arr[3]
            target_singer6=singers.find_by_id(singer_id6)
            target_music6=target_singer6.find_music_by_id(music_id6)
            text=target_music6.text
            for i in range(len(text)):
                if text[i] == word[0]:
                    y =text[i:i+len(word)]
                    if y == word:
                        print(f"{i} to {i+len(word)-1}")
                        break
        
        #checked
        elif func == "countw":
            singer_id4 = arr[1]
            music_id4 = arr[2]
            word = arr[3]
            singer_target = singers.find_by_id(singer_id4)
            music_target = singer_target.find_music_by_id(music_id4)
            text=music_target.text
            count=0
            for i in range(len(text)):
                if text[i] == word[0]:
                    y =text[i:i+len(word)]
                    if y == word:
                        count+=1
            print(count)

        #checked
        elif func == "addp":
            playlist_id = arr[1]
            playlist_name = arr[2]
            playlist = Playlist.Playlist(playlist_id, playlist_name)
            playlists.add_to_playlists(playlist)
            playlists.show()

        #checked
        elif func == "addmp":
            music_id = arr[1]
            playlist_id = arr[2]
            target_playlist = playlists.search_by_id(playlist_id)
            target_music = musics.search_music_by_id(music_id)
            if(target_music is None):
                print(f"we dont have music with id {music_id}")
                continue
            if(target_playlist is None):
                print(f"We dont have playlist with id {playlist_id}")
                continue
            target_playlist.add_music(target_music)
            target_playlist.show_playlist()  # edit

        #checked
        elif func == "searchp":
            playlist_id = arr[1]
            target_playlist1 = playlists.search_by_id(playlist_id)
            target_playlist1.show_playlist()

        elif func == "searchmp":
            playlist_id2 = arr[1]
            music_id2 = arr[2]
            target_playlist2 = playlists.search_by_id(playlist_id2)
            if (target_playlist2 is None):
                print(f"No playlist with id {playlist_id2}")
                continue
            target_music2 = target_playlist2.search_music(music_id2)
            if (target_music2 is None):
                print(f"No music with id {music_id2}")
                continue
            print(target_music2.name)

        elif func == "delmp":
            playlist_id3 = arr[1]
            music_id3 = arr[2]
            target_playlist3 = playlists.search_by_id(playlist_id3)
            target_music3 = target_playlist3.delete_music(music_id3)
            if (target_music3 is None):
                print(f"No music with id {music_id2}")
                continue
            print(target_music3)

        elif func == "showp":
            playlist_id4 = arr[1]
            target_playlist4 = playlists.search_by_id(playlist_id4)
            if(target_playlist4 is not None):
                target_playlist4.sort_playlist()
            else:
                print("Playlist is Empty")


        elif func == "playm":
            singer_id5 = arr[1]
            music_id5 = arr[2]
            target_music5 = musics.search_music_by_id(music_id5)
            target_singer5 = singers.find_by_id(singer_id5)
            if (target_music5 is None):
                print(f"No music with id {music_id5}")
                continue
            if (target_singer5 is None):
                print(f"No singer with id {singer_id5}")
                continue
            if (target_singer5.find_music_by_id_bool(music_id5)):
                history.play_music(target_music5)
            else:
                print(
                    f"No music with id {music_id5} for singer {target_singer5.name}")
                continue

        elif func == "undo_playm":
            history.undo()

        elif func == "get_max_rated":
            musics.max_rated()

        elif func == "get_min_rated":
            musics.low_rated()

        elif func == "quit":
            print("Goodbye")
            break

        else:
            print("Invalid request")

start()
# while True:
#     try:
#         start()
#     except:
#         print("Please try again your request was invalid")


