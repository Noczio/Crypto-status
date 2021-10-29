from src.controller.scrape import scrape_web


def run() -> None:
    arguments = ("src//app_data", "data.json")
    scrape_web(*arguments)

