from typing import Optional, Any, List

from . import Playlist, SongSortMode, RemotePlayerAction, ShuffleMode, RepeatMode
from .api import AudioStationApi
from .models.player import Player
from .models.queue_mode import QueueMode
from .models.remote_player_status import RemotePlayerStatus


class RemotePlayerInfo:
    """Model used by library to store info about a remote player."""

    def __init__(self, api: AudioStationApi, player: Player):
        """Initialize RemotePlayerInfo."""
        self._api = api
        self._player = player
        self._status: Optional[RemotePlayerStatus] = None

    def update(self):
        self._status = self._api.remote_player_get_player_status(self._player.id)

    @property
    def player(self) -> Player:
        return self._player

    @property
    def status(self) -> RemotePlayerStatus:
        return self._status

    def get_current_playlist(self) -> Playlist:
        """Get current playlist"""
        return self._api.remote_player_get_current_playlist(self._player.id)

    def clear_playlist(self) -> bool:
        """Clear current playlist"""
        return self.__return_success_and_update(self._api.remote_player_clear_playlist(self._player.id))

    def play_songs(self, song_ids: List[str], playlist_playlist_queue_mode: QueueMode,
                   play_directly: bool = True) -> bool:
        """Play songs using their ids"""
        return self.__return_success_and_update(
            self._api.remote_player_play_songs(self._player.id, song_ids, playlist_playlist_queue_mode, play_directly))

    def play_artist(self, artist: str, sort: SongSortMode, playlist_queue_mode: QueueMode,
                    play_directly: bool = True) -> bool:
        """Play all song of an artist"""
        return self.__return_success_and_update(
            self._api.remote_player_play_artist(self._player.id, artist, sort, playlist_queue_mode, play_directly))

    def play_album(self, album_name: str, album_artist: str, sort: SongSortMode, playlist_queue_mode: QueueMode,
                   play_directly: bool = True) -> bool:
        """Play an album using album name and album artist"""
        return self.__return_success_and_update(
            self._api.remote_player_play_album(self._player.id, album_name, album_artist, sort, playlist_queue_mode,
                                               play_directly))

    def jump_to_song(self, position_in_playlist: int) -> bool:
        """Change player current song to index in playlist"""
        return self.__return_success_and_update(
            self._api.remote_player_jump_to_song(self._player.id, position_in_playlist))

    def control(self, action: RemotePlayerAction) -> bool:
        """Change player current playing status"""
        return self.__return_success_and_update(self._api.remote_player_control(self._player.id, action))

    def volume(self, volume: int) -> bool:
        """Change player current volume"""
        return self.__return_success_and_update(self._api.remote_player_volume(self._player.id, volume))

    def shuffle(self, shuffle: ShuffleMode) -> bool:
        """Change player current shuffle mode"""
        return self.__return_success_and_update(self._api.remote_player_volume(self._player.id, shuffle))

    def repeat(self, repeat: RepeatMode) -> bool:
        """Change player current repeat mode"""
        return self.__return_success_and_update(self._api.remote_player_repeat(self._player.id, repeat))

    def __return_success_and_update(self, success: bool):
        if success:
            self.update()
        return success
