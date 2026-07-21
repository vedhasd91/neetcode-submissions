class FileSystem:
    class File:
        def __init__(self):
            self.is_file = False
            self.files = {}
            self.content = ""

    def __init__(self):
        self.root = self.File()
        

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.files.keys())

        dirs = path.split("/")[1:]

        cur = self.root
        for dir_ in dirs:
            if dir_ in cur.files:
                cur = cur.files[dir_]

        if cur.is_file:
            return [dirs[-1]]

        
        return sorted(cur.files.keys())
        

    def mkdir(self, path: str) -> None:
        dirs = path.split("/")[1:]

        cur = self.root
        for dir_ in dirs:
            if dir_ not in cur.files:
                cur.files[dir_] = self.File()
            cur = cur.files[dir_]
            

    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split("/")[1:]
        file = dirs[-1]

        cur = self.root
        for dir_ in dirs[:-1]:
            if dir_ in cur.files:
                cur = cur.files[dir_]
                
        print(cur.files, content)
        if file not in cur.files:
            cur.files[file] = self.File()
            cur.files[file].is_file = True

        cur.files[file].content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split("/")[1:]
        file = dirs[-1]
        cur = self.root
        for dir_ in dirs[:-1]:
            if dir_ in cur.files:
                cur = cur.files[dir_]
        
        return cur.files[file].content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
