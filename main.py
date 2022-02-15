import remi
import remi.gui as gui

class ChatApp(remi.App):

    def __init__(self, request, client_address, server, **app_args):
        super().__init__(request, client_address, server, **app_args)
     
    def main(self):
        container = gui.VBox(width=500, height=200)
        self.label = gui.Label("Hello")
        self.textbox = gui.TextInput()
        self.bt = gui.Button("Click")
        self.bt.onclick.do(self.on_button_click)

        container.append(self.label)
        container.append(self.textbox)
        container.append(self.bt)
        return container

    def on_button_click(self, w):
        self.label.set_text(self.textbox.get_text())

    def on_close(self):
        return super().on_close()

remi.start(ChatApp, port=8080)