class SongRegisterController:
  def insert(self, new_song_informations: dict) -> dict:
    self.verify_songs_infos()
    self.verify_if_song_already_registered()
    self.insert_song()
    self.format_response()
    pass

  def __verify_if_song_already_registered(new_song_informations: dict) -> None:
    pass

  def __verify_songs_infos(new_song_informations: dict) -> None:
    pass

  def __insert_song() -> None:
    pass

  def __format_response() -> None:
    pass
