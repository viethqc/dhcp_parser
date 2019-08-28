import os

CONFIG_FILE = "dhcp.conf"

with open(CONFIG_FILE) as f:
    line = f.readline()
    cnt = 1
    stack = []
    block = ""

    while line:
        line = line.strip()
        
        if len(line) == 0:
            line = f.readline()
            continue

        if line[0] == "#":
            line = f.readline()
            continue



        if line [len(line) - 1] == ";":
            if len(stack) == 0:
                print line + ": line config"
            else:
                block += line
        elif line [len(line) - 1] == "{":
            block += line
            stack.append("{")
        elif line [len(line) - 1] == "}":
            block += line
            data = stack.pop()

            if len(stack) == 0:
                print block + ": block config"

        line = f.readline()
        cnt += 1

class Config(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

class BlockConfig(object):
    def __init__(self, title):
        self.__title = title
        self.__line_config = []
        self.__block_config = []
        pass

    def add_line_config(self, line):
        if line in self.__line_config:
            return True
        
        self.__line_config.append(line)
        return True

    def add_block_config(self, block_config):
        self.__block_config.append(block_config)
        pass

    def remove_line_config(self, line):
        pass

    def remove_block_config(self, block_config):
        pass

    def __str__(self):
        block = ""
        block += self.__title + " {" + "\n"
        for line in self.__line_config:
            block += "\t" + line + "\n"

        for single_block in self.__block_config:
            block += str(single_block)
        block += "{" + "\n"
        return block

block = BlockConfig("host fantasia")
block.add_line_config("hardware ethernet 08:00:07:26:c0:a5;")
block.add_line_config("fixed-address fantasia.example.com;")

a = BlockConfig("subnet 10.5.5.0 netmask 255.255.255.224")
a.add_line_config("range 10.5.5.26 10.5.5.30;")


print block

a.add_block_config(block)
print a