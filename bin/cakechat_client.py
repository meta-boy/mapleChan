import tkinter as tk
import requests
import json
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time


class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.base_url = "http://localhost:8080/cakechat_api/v1/actions/get_response"
        self.data = []
        self.emotion = tk.StringVar(value="neutral")
        self.title("Maple - Chan")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        self.respond = ttk.Button(
            self, text='Get Response', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3, columnspan=4,)
        
        self.neutral = ttk.Radiobutton(
            self,
            text = "Neutral",
            variable = self.emotion,
            value = "neutral",
            
        )
        self.neutral.grid(column = 0, row  = 7, columnspan=1,)
        self.anger = ttk.Radiobutton(
            self,
            text = "Anger",
            
            variable = self.emotion,
            value = "anger",
            
        )
        self.anger.grid(column = 1, row  = 7, columnspan=1,)
        self.joy = ttk.Radiobutton(
            self,
            text = "Joy",
            variable = self.emotion,
            value = "joy",
            
        )
        self.joy.grid(column = 2, row  = 7, columnspan=1,)
        self.fear = ttk.Radiobutton(
            self,
            text = "Fear",
            variable = self.emotion,
            value = "fear",
            
        )
        self.fear.grid(column = 3, row  = 7, columnspan=1,)
        self.saddness = ttk.Radiobutton(
            self,
            text = "Saddness",
            variable = self.emotion,
            value = "saddness",
            
        )
        self.saddness.grid(column = 4, row  = 7, columnspan=1,)
        self.conversation_lbl = ttk.Label(
            self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(
            column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=8, columnspan=5,
                               sticky='nesw', padx=3, pady=3)

    def makeRequest(self):
        payload = {
            'context': self.data,
            'emotion': self.emotion.get()
        }
        print(payload)
        resp = requests.post(self.base_url, json = payload)
        print(resp.text, payload)
        j = json.loads(resp.text)["response"]
        print(j)
        return j

    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)
        self.data.append(user_input)
        response = self.makeRequest()
    
        self.data.append(response)
        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" +
            "Maple: " + str(response) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)


gui_example = TkinterGUIExample()
gui_example.mainloop()
