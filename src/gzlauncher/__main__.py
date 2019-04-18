import logging

def main():
    pass

def _init_logger(log_file="latest.log", log_level=logging.INFO):
    root = logging.getLogger()
    fmt_file = logging.Formatter(
        fmt="{asctime:15s} | {levelname:8s} | {name} : {message}",
        datefmt="%d-%m-%Y %H:%M:%S",
        style="{")
    fmt_stream = logging.Formatter(
        fmt="{asctime:8s} | {levelname:8s} | {name} : {message}",
        datefmt="%H:%M:%S",
        style="{")
    if log_file is not None:
        handler_file = logging.FileHandler(log_file)
        handler_file.setFormatter(fmt_file)
        root.addHandler(handler_file)
    handler_stream = logging.StreamHandler()
    handler_stream.setFormatter(fmt_stream)
    root.addHandler(handler_stream)
    root.setLevel(log_level)
    return log_file

if __name__ == "__main__":
    main()