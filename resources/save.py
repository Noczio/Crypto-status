import json
import os


def save(final_path: str, data: dict):
    if not os.path.exists(final_path):
        with open(final_path, 'w', encoding="utf-8") as file:
            new_data = [data]
            json.dump(new_data, file, indent=2)
    else:
        with open(final_path, 'r', encoding="utf-8") as file:
            new_data = json.load(file)
            new_data.append(data)
            with open(final_path, 'w', encoding="utf-8") as file_again:
                json.dump(new_data, file_again, indent=2)


def save_to_disk(path: str, file_name: str, data: dict) -> None:
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        final_path = path + "\\" + file_name + ".json"
        save(final_path, data)

    except FileNotFoundError:
        raise FileNotFoundError("Path to JSON file was not found")
    except ValueError:
        raise ValueError("Data does not meet requirements to be considered a json file")
    except OSError:
        raise OSError("Invalid file. It needs a text extension")
    except Exception as e:
        raise Exception(str(e))
