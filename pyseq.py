from sequencer.sequencer import Sequencer
from gui.sequencer_gui import Sequencer_GUI

def main():
    sequencer = Sequencer()
    sequencer_gui = Sequencer_GUI(sequencer)

if __name__ == "__main__":
    main()