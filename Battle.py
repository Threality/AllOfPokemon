class GameEvent:
    ON_SWITCH_IN = "onSwitchIn"
    BEFORE_TURN = "beforeTurn"
    ON_MOVE_USE = "onMoveUse"
    ON_MOVE_HIT = "onMoveHit"
    ON_DAMAGE = "onDamage"
    ON_KO = "onKO"
    END_TURN = "endTurn"
    TERRAIN_CHANGE = "terrainChange"
    WEATHER_CHANGE = "weatherChange"
    STATUS_GAINED = "statusGained"
    ON_STAT_CALC = "onStatCalc"
    ON_MEGA_EVOLVE = "onMegaEvolve"

class Battle:
    def __init__(self, team1, team2, battleType):
        self._team1 = team1
        self._team2 = team2
        self._battleType = battleType
        self._weather = None
        self._weatherDuration = 0
        self._terrain = None
        self._terrainDuration = 0

    def SetTerrain(self, terrain, pokemon):
        self._terrain = terrain
        self._terrainDuration = 5
        pokemon._item.HandleEvent("terrainChange", pokemon, self, terrain=terrain) # checks if extra duration needs to be added

    def SetWeather(self, weather, pokemon):
        self._weather = weather
        self._weatherDuration = weather._duration
        pokemon._item.HandleEvent("weatherChange", pokemon, self, weather=weather) # checks if extra duration needs to be added

    class Turn:
        pass