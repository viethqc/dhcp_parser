import os


class Config(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

class BlockConfig(object):
    def __init__(self, title, is_root=False):
        self.__is_root = is_root
        self.__title = title.strip()
        self.__line_config = []
        self.__block_config = []
        self.__dict_block = {}
        pass

    def get_block_title(self):
        return self.__title

    def set_title(self, title):
        title = title.strip()
        self.__title = title

    def get_block_config(self, title):
        title = title.strip()

        if title in self.__dict_block:
            return self.__dict_block[title]

        return None

    def add_line_config(self, line):
        line = line.strip()

        if line in self.__line_config:
            return True
        
        self.__line_config.append(line)
        return True

    def add_block_config(self, block_config):
        self.__block_config.append(block_config)
        self.__dict_block[block_config.get_block_title()] = block_config

    def remove_block_config(self, block_title):

        print "remove block config"
        block_title = block_title.strip()

        if block_title in self.__dict_block:
            self.__dict_block.pop(block_title, None)

        print self.__dict_block

    def remove_line_config(self, line):
        line = line.strip()
        index = -1

        for i in range(0, len(self.__line_config)):
            line_tmp = self.__line_config[i].strip()
            if line == line_tmp:
                index = i
                break

        if index >= 0 and index <= (len(self.__line_config) - 1):
            del self.__line_config[index]

    def __str__(self):
        block = ""

        if self.__is_root is False:
            block += self.__title + " {" + "\n"
        
        for line in self.__line_config:
            block += line + "\n"

        
        for key in self.__dict_block:
            block += str(self.__dict_block[key])

        if self.__is_root is False:
            block += "}" + "\n"

        return block