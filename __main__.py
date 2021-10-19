from colorama import init

from src.view.appView import AppView

if __name__ == "__main__":
    init(autoreset=True)
    app = AppView()
    app.run()
