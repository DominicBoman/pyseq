from sequencer.sequencer import Sequencer
from gui.app_window import App_Window

def main():
    sequencer = Sequencer()
    app_window = App_Window(sequencer)

if __name__ == "__main__":
    main()