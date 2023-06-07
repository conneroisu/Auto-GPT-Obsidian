import os


class Frontmatter: 
    def __init__(self, note_title: str) -> None:
        # Self.values is a dictionary of key-value pairs
        self.values = {} 
        self.content = self.get_content(note_title)
        for line in content: 
            key, value = line.split(":")
            self.values[key] = value
    self.title = self.values["title"]
    def add(self, key, value):
        self.values[key] = value 



    def get_content(self, note_path):        
        """ 
        Returns the content of the frontmatter.  
        """
        with open(note_path, "r")as file:
            for line in file:
                count = 0
                if line.startswith("---"):
                    count += 1
                    if count == 2: 
                        return content              
                    else:
                        continue
                content += line

        return content 
        
