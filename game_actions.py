import inspect


#print(inspect.getsource(lexer.check_direction))

def action_room201_couch(tokens, controller) ->bool:
    if tokens.verb == "sit":
        controller.response = "You sit on the couch"
        return True
    return False