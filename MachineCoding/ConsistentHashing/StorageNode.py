class StorageNode:
    def __init__(self, name=None, host=None):
        self.name = name
        self.host = host
        self.storage = []
        self.key = None
    
    def get_storage(self):
        return self.storage
        
    def __repr__(self) -> str:
        return f'{self.name} : {self.host} : {self.key} : {self.storage}'

    def fetch_file(self, path):
        for item in self.storage:
            if item[0] == path:
                print(f'FETCHED  : {self.host}:{self.name}:{path}')
                return 
        raise Exception(f'File {path} not in Node.{self.__repr__()}')
    
    def put_file(self, path):
        self.storage.append(path)
        print(f'PUTTING : {path} in {self.__repr__()}')