import random
import string

from fastapi import APIRouter 

from app.models.player import Player, PlayerBase
from app.game_logic.user import User

router = APIRouter()

users = {}

@router.post('/player',  response_model=Player)
def create_new_player(player: PlayerBase):
    player_id = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
    while player_id in users:
        player_id = ''.join(random.choice(string.ascii_uppercase) for i in range(4)) # generate new game ids until a new id is found

    users[player_id] = User(player.name, player_id)
    
    return users[player_id].to_json()

@router.get('/player', response_model=Player)
def get_player(player: PlayerBase):
    return users[player.uid]