from src.controller.appController import AppController


class AppView:

    def run(self):
        controller = AppController(path="src//app_data", file="data.json")
        controller.scrape_web()


