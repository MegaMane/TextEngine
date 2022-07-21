import inspect
from game_object import  GameObject
from game_controller import Controller

#print(inspect.getsource(lexer.check_direction))

def action_room201_couch(controller: Controller, target) ->bool:
    tokens = controller.tokens
    couch = target
    if tokens.verb == "sit":
        couch.current_description = couch.descriptions["Sitting"]
        controller.response = "You sit on the couch."
        controller.response += controller.player.go_to(couch.key_value)
        return True
    elif tokens.verb in ["stand","get off", "get up"]:
        couch.current_description = couch.descriptions["Main"]
        controller.response = "You get off the couch."
        controller.response += controller.player.go_to(couch.location_key)
        return True
    return False