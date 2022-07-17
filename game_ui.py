import tkinter as tk


class UI:


    def __init__(self, controller):
        #https://blog.teclado.com/tkinters-grid-geometry-manager/
        self.history_index = 0
        self.current_turn = 0
        self.turn_history = []
        self.root = tk.Tk()
        self.root.geometry("1000x800")
        self.root.resizable(False, False)
        self.root.title("Texticular")
        self.controller = controller


        self.dialogue = tk.StringVar()
        self.dialogue.set("Main Game Dialogue")
        self.statistics = tk.StringVar()
        self.statistics.set("Game Statistics Here")

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=1)

        self.root.rowconfigure(0, weight=5)
        self.root.rowconfigure(1, weight=1)

        self.main_dialogue = tk.Label(self.root, wraplength=600, bg="#000", textvariable=self.dialogue, justify="left", anchor="nw", padx=10, pady=10, font="sans 14", fg="white")
        self.main_dialogue.grid(column=0, row=0, ipadx=10, ipady=10, sticky="NSEW")

        self.game_sats = tk.Label(self.root, textvariable=self.statistics, bg="grey", fg="white", borderwidth=5, relief="raised")
        self.game_sats.grid(column=1, row=0, ipadx=10, ipady=10, sticky="NSEW")

        self.player_input = tk.Entry(self.root, bg="#222324", fg="yellow", font="sans 12", borderwidth=3, relief="flat", insertbackground="white")
        self.player_input.grid(column=0, row=1, columnspan=2, ipadx=10, ipady=10, sticky="NSEW")
        self.input_prompt = 'Enter Command>> '
        self.player_input .insert(0, self.input_prompt)
        self.player_input.focus_set()

        self.root.bind('<Return>', self.refresh_ui)
        self.root.bind('<Left>', self.dialogue_history_back)
        self.root.bind('<Right>', self.dialogue_history_forward)
        self.dialogue.set("Something new appears in the main dialogue")





    def refresh_ui(self, key):

        # performing these three actions manually instead of calling controller.render()
        # because we are no longer getting input from the command line
        player_input = self.player_input.get().replace(self.input_prompt,'')
        self.controller.response = ''
        self.controller.user_input = player_input.lower().strip()

        current_label_val = self.dialogue.get()
        game_response = self.controller.update()

        self.current_turn += 1
        result = "-" * 100 + "\n\n"
        result += f"Move {self.current_turn}: {player_input}\n\n"
        result += "-" * 100 + "\n\n"
        result += f"{game_response}"

        #print(result)
        self.turn_history.append(result)

        self.history_index = self.current_turn
        self.dialogue.set(result)
        self.player_input.delete(0, len(self.player_input.get()))
        self.player_input.insert(0, self.input_prompt)

    def dialogue_history_back(self, key):
        self.history_index -= 1
        self.player_input.delete(0, len(self.player_input.get()))
        self.player_input.insert(0, self.input_prompt)
        try:
            self.dialogue.set(self.turn_history[self.history_index])
        except IndexError:
            self.history_index = -1
            self.dialogue.set(self.turn_history[self.history_index])

    def dialogue_history_forward(self, key):
        self.history_index += 1
        self.player_input.delete(0, len(self.player_input.get()))
        self.player_input.insert(0, self.input_prompt)
        try:
            self.dialogue.set(self.turn_history[self.history_index])
        except IndexError:
            self.history_index = 0
            self.dialogue.set(self.turn_history[self.history_index])

















