import logging
import configparser
import argparse
import launcher
import defaults


class GZConfig:
    def __init__(self, config_file="launcher.cfg"):
        self.__log = logging.getLogger("GZConfig")
        self.__config_file = config_file
        self.__config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation())
        try:
            with open(config_file, "r") as conf:
                self.__config.read_file(conf)
        except FileNotFoundError:
            try:
                with open(config_file, "w") as conf:
                    conf.write(defaults.GZCONFIG)
                    self.__config.read_string(defaults.GZCONFIG)
            except IOError:
                self.__log.error(
                    f"Can't create configuration file {config_file}")

    def get_config_file(self):
        return self.__config_file

    def get_games(self, non_game=["paths", ]):
        sections = self.__config.sections()
        return [s for s in sections if s not in non_game]

    def get_args(self, game):
        if game in self.get_games():
            args = []
            mods = self.__config.get(game, "mods").split(",")
            g = self.__config.get(game, "game").split(",")
            if len(g) > 1:
                args = g.copy()
                del args[0]
            args.extend(mods)
            arg_list = [["-file", a.strip()] for a in args if a is not ""]
            arg_list.insert(0, [
                self.__config.get(
                    "paths",
                    "engine.linux64"
                    if launcher.get_os() is launcher.System.Linux64 else
                    "engine.linux32"
                    if launcher.get_os() is launcher.System.Linux32 else
                    "engine.windows64"
                    if launcher.get_os() is launcher.System.Windows64 else
                    "engine.windows32"),
                "-iwad", g[0].strip(),
                "-config",
                self.__config.get("paths", "engine.config").strip(),
                "-savedir",
                self.__config.get("paths", "saves") + f"/{game}".strip(),
                "-stdout",
            ])
            return [inner for outer in arg_list for inner in outer]

    def get_description(self, game):
        if game in self.get_games():
            return self.__config.get(game, "description")

    def get_help(self):
        result = "Available games:\n"
        for g in self.get_games():
            result = "{}  {:<13} -- {}\n".format(
                result, g, self.get_description(g).strip())
        return result


class GZFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)
