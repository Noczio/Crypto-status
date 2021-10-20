from src.controller.appController import AppController


class AppView:
    _controller = AppController()

    def run(self):
        disk_data = self._controller.load_disk_data(path="src//app_data", file="data.json")
        output = self._controller.scrape_web(disk_data["url"], disk_data["search"])
        last_pos = len(output) - 1

        for counter, item in enumerate(output):
            if counter < last_pos:
                print(item, end="\n")
            else:
                print(item)
