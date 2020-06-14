# FileSystem object will be instantiated and called as following:
# fs = FileSystem()
# files = obj.ls(path) // list "files" in path
# obj.mkdir(path) // make directory with "path"
# obj.addContentToFile(filePath,content) // addContent to file 
# content = obj.readContentFromFile(filePath) // read content from specified "filePath"

class Node:
    def __init__(self, name, isFile=False, content=None):
        self.name = name
        self.isFile = isFile
        self.children = {}
        self.content = content


class FileSystem:
    def __init__(self):
        self.root = Node("/")

    def ls(self, path: str) -> List[str]:
        fs = path[1:].split('/')
        trav = self.root
        
        if path != "/":
            for f in fs:
                if f not in trav.children:
                    return []
                trav = trav.children[f]
        
        if trav.isFile == True:
            return [trav.name]
        
        names = []
        for k in trav.children:
            names.append(k)
        names.sort()
        return names

    def mkdir(self, path: str) -> None:
        fs = path[1:].split('/')
        trav = self.root

        for f in fs:
            if f not in trav.children:
                trav.children[f] = Node(f)
            trav = trav.children[f]

        return None

    def addContentToFile(self, filePath: str, content: str) -> None:
        fs = filePath[1:].split('/')
        trav = self.root

        for f in fs:
            if f not in trav.children:
                trav.children[f] = Node(f)
            trav = trav.children[f]

        trav.isFile = True
        if trav.content is None:
            trav.content = content
        else:
            trav.content = trav.content + content

    def readContentFromFile(self, filePath: str) -> str:
        fs = filePath[1:].split('/')
        trav = self.root

        for f in fs:
            if f not in trav.children:
                return None
            trav = trav.children[f]

        return trav.content
