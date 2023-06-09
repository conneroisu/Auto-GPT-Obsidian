"""Import the OS module to operate using operating system of the operating computer."""
import os
import frontmatter 

from obsidian.obsidian_vault import Obsidian_Vault

class Obsidian_Note():
    def __init__(self, vault: Obsidian_Vault, note_path) -> None: 
        self.vault_name = os.getenv("OBSIDIAN_VAULT_NAME") 
        self.vault = vault
        self.path = vault.vault_directory + note_path
        self.title = os.path.basename(self.path).replace(".md", "")  
        with open(os.path.join(vault.vault_directory, note_path))as f:
            self.frontmatter = frontmatter.load(f)
            self.update_note_attributes(f.read())
        

    def reload(self) -> None: 
        with open(self.path, "r") as f: 
            self.content = f.read()
        if self.content is None: 
            self.content = ""
        self.update_note_attributes(self.content)

    def update_note_attributes(self, context:str) -> None: 
        self.tags = self.get_tags(context)
        with open(self.path, "r") as file: 
            self.content = file.read()

    def get_tags(self, content) -> list: 
        """
        Retreives the tags of the note defined in Frontmatter syntax, obsidian content syntax, and dataview syntax.

        Returns: 
            A list of tags for the note. 
        """
        tags = []
        for line in content.split("\n"): 
            for word in line.split(" "): 
                if word.startswith("#"): 
                    tags.append(word.replace("#", ""))
        for line in content.split("\n"): 
            if line.startswith("tags::"): 
                tags += line.replace("tags::", "").strip().split(" ")
        return tags

