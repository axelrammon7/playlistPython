import os

class SongRegisterView:
  def register_song_initial(self) -> dict:
    self.__clear()
    print("Implementar nova música \n\n")

    title = input("Nome da música: ")
    year = input("Ano de publicação: ")
    artist = input("Nome do artista: ")

    new_song_informations = {
      "title": title,
      "artist": artist,
      "year": year
    }

    return new_song_informations
  
  def __clear(self):
    os.system("cls||clear")