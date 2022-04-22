from enum import Enum


class PlaylistStatus(str, Enum):
    transitioning = "transitioning"
    playing = "playing"
    stopped = "stopped"
    pause = "pause"
