from src.controller.appController import AppController


class AppView:
    _controller = AppController()

    def run(self):
        init_path_args = ("src//app_data", "data.json")
        disk_data = self._controller.load_disk_data(*init_path_args)
        url, coins = disk_data["url"], disk_data["coins"]
        links = [url + "/currencies/" + item for item in coins]
        output = self._controller.scrape_web(links)

        for item in output:
            print(item)

