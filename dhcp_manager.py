from dhcp_config import BlockConfig
import os
import traceback

class DHCPManager(BlockConfig):
    def __init__(self, file_path):
        BlockConfig.__init__(self, "", is_root=True)
        self.__file_path = file_path
        pass

    def parse_string(self, string_raw_data):
        pass

    def sum(self, a, b):
        return a + b

    def parse_file(self):
        if os.path.exists(self.__file_path) is False:
            return False
    
        with open(self.__file_path) as f:
            line = f.readline()
            stack = []
            block = ""
            block_tmp = None

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
                        self.add_line_config(line)
                    else:
                        block_tmp.add_line_config(line)
                elif line [len(line) - 1] == "{":
                    title = line[0:len(line) - 1].strip()

                    block_tmp = None
                    block_tmp = BlockConfig(title)
                    stack.append("{")
                elif line [len(line) - 1] == "}":
                    data = stack.pop()

                    if len(stack) == 0:
                        self.add_block_config(block_tmp)
                        block = None

                line = f.readline()

        return True
    

    def save_config(self):
        try:
            hFile = open(self.__file_path, "w+")
            data = str(self)
            hFile.write(data)
            hFile.close

            return True
        except Exception as ex:
            traceback.print_exc()
            return False
        
        pass

    def stop(self):
        os.system("service isc-dhcp-server stop")
        pass

    def start(self):
        os.system("service isc-dhcp-server start")
        pass

    def restart(self):
        os.system("service isc-dhcp-server restart")
        pass


if __name__ == '__main__':
    kk = DHCPManager("dhcp.conf")
    kk.parse_file()

    kk.add_line_config("hello world;")
    kk.save_config()

    print kk

    kk.remove_line_config("hello world;")
    print kk