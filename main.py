from engine.core import Core
from dataclasses import dataclass
from mario.scenes import SCENES

# todo fazer isso dps um objeto com tipos staticos e etc
# game_data = {
#     "title": ,
#     "width": 256,
#     "height": 224,
#     "fps": 60,
#     "scenes": SCENES,
# }


@dataclass
class Mario:
    title: str
    width: int
    height: int
    fps: int
    scenes: dict


game_data = Mario(
    "Mario From Scratch",
    256,
    224,
    60,
    SCENES)

if __name__ == "__main__":
    game = Core(game_data)
    game.run()
