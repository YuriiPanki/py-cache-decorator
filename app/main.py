from typing import Callable, Any


def cache(func: Callable) -> Callable:
    save_list = []
    def wrraper(*args: Any, **kwargs: Any) -> Any:
        for item in save_list:
            if args == item[0]:
                print("Getting from cache")
                return item[1]
        result = func(*args, **kwargs)
        save_list.append([args, result])
        print("Calculating new result")
        return result

    return wrraper
