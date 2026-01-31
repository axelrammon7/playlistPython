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
  
  def registry_song_success(self, response: dict) -> None:
    self.__clear()
    message = ''' 
      Música cadastrada com sucesso!

      * Título: {}
      * Quantidade: {} 
    '''.format(
      response["attributes"]["title"],
      response["count"]
    )

    print(message)

  def registry_song_fail(self, response: dict) -> None:
    self.__clear()
    message = ''' 
      Falha ao registrar música

      * Erro: {} 
    '''.format(
      response["error"]
    )
    print(message)

  def __clear(self):
    os.system("cls||clear")