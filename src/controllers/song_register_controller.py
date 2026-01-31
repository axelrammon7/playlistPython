class SongRegisterController:
  def insert(self, new_song_informations: dict) -> dict:
    try:
      self.verify_songs_infos()
      self.verify_if_song_already_registered()
      self.insert_song()
      return self.format_response()
    except Exception as exception:
      return self.__format_error_response(exception)

  def __verify_songs_infos(self, new_song_informations: dict) -> None:
    if len(new_song_informations["title"]) > 100:
      raise Exception("Título de música com mais de 100 caracteres")

    year = int(new_song_informations["year"])
    if year >= 2027:
      raise Exception("Ano de música inválido")
    
  def __verify_if_song_already_registered(self, new_song_informations: dict) -> None:
    pass

  def __insert_song(self, new_song_informations: dict) -> None:
    pass

  def __format_response(self, new_song_informations: dict) -> dict:
    return {
      "success": True,
      "count": 1,
      "attributes": {
        "title": new_song_informations["title"]
      }
    }

  def __format_error_response(self, err: Exception) -> dict:
    return {
        "success": False,
        "error": str(err)
      }   