"""Synology AudioStation API wrapper."""
from typing import List, Optional

from .api import AudioStationApi
from src.synology_dsm.api.audio_station.models.audio_station_info import AudioStationInfo
from .models.library_share_type import LibraryShareType
from .models.player import Player
from .models.player_list import PlayerList
from .models.playlist import Playlist
from .models.remote_player_action import RemotePlayerAction
from .models.remote_player_status import RemotePlayerStatus

from .models.repeat_mode import RepeatMode
from .models.shuffle_mode import ShuffleMode
from .models.song_sort_mode import SongSortMode
from .remote_player_info import RemotePlayerInfo


class SynoAudioStation:
    """An implementation of a Synology AudioStation."""

    def __init__(self, dsm):
        """Initialize Audio Station."""
        self._api = AudioStationApi(dsm)
        self._remote_players: Optional[List[RemotePlayerInfo]] = None
        self._info = None

    def update(self):
        self._info = self._api.get_info()
        self._remote_players = self.__get_players()

    @property
    def info(self) -> AudioStationInfo:
        return self._info

    @property
    def remote_players(self) -> List[RemotePlayerInfo]:
        return self._remote_players

    def get_remote_player(self, player_id: str) -> Optional[RemotePlayerInfo]:
        for player in self._remote_players:
            if player.player.id == player_id:
                return player
        return None

    def __add_status_to_player(self, player: Player):
        player = RemotePlayerInfo(self._api, player)
        player.update()
        return player

    def __get_players(self) -> List[RemotePlayerInfo]:
        players = self._api.remote_player_get_players()
        return list(map(self.__add_status_to_player, players))
