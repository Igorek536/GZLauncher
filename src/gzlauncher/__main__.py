import logging
import argparse
import os
import sys

import gzconfig
import launcher


def main():
    logfile = "latest.log"
    _init_logger(log_file=logfile)
    log = logging.getLogger("Main")
    cfg = gzconfig.GZConfig()
    parser = argparse.ArgumentParser(
        formatter_class=gzconfig.GZFormatter,
        description="Simple launcher for GZDoom",
        epilog="Good luck, Doomer!")

    parser.add_argument("-g", "--game",
                        action="store",
                        nargs=1,
                        choices=cfg.get_games(),
                        help=f"R|{cfg.get_help()}",
                        metavar="")
    parser.add_argument("-c", "--clear", action="store_true",
                        help="Clear all configs and logs")
    args = parser.parse_args()
    if args.clear == True:
        os.remove(logfile)
        os.remove(cfg.get_config_file())
        return
    if args.game is not None:
        try:
            launcher.execute(
                cfg.get_args(args.game[0]),
                lambda o: log.info(o.strip().decode(sys.stdout.encoding)),
                lambda e: log.error(e.strip().decode(sys.stderr.encoding)))
        except KeyboardInterrupt:
            log.info("Program stopped by user!")
            exit(0)
    else:
        parser.print_help()


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
