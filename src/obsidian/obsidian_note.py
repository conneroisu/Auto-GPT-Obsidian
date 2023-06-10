"""Import the OS module to operate using operating system of the operating computer."""
import os

import frontmatter
from obsidian_vault import Obsidian_Vault

class Obsidian_Note():
    """
    Note object allowing for inteactions with markdown notes with the syntax of Obsidian for the AutoGPT plugin, AutoGPTObsidian.
    Attributes:  | Description:
    Note Title - the title of the file/note defined by the path of the note/file. 
    Note Content - the entire content of the file/note including the frontmatter. 
    Note Body - the content of the note without the frontmatter.
    Note Frontmatter - the content of an Obsidian Note inside of "---"s at the front of a note 
    Note Meta data - the metadata fields and their corresponding values of the note/file 
    """
    def __init__(self, vault: Obsidian_Vault, note_path) -> None: 
        """
        Initialize the Obsidian_Note object with the given parameters.

        Args:
            path: The path of the note with respect to the vault_working_directory. (Not including the vault_directory)
        """
        self.vault_name = os.getenv("OBSIDIAN_VAULT_NAME") 
        self.vault = vault
        self.path = vault.vault_directory + note_path
        self.title = os.path.basename(self.path).replace(".md", "")  
        with open(os.path.join(vault.vault_directory, note_path))as f:
            self.frontmatter = frontmatter.load(f)
            self.update_note_attributes(f.read())
        

    def reload(self) -> None: 
        """
        Reloads the note content from the file at the given path. 
        """
        with open(self.path, "r") as f: 
            self.content = f.read()
        if self.content is None: 
            self.content = ""
        self.update_note_attributes(self.content)

    def update_note_attributes(self, context:str) -> None: 
        """
        Updates the attributes of the Obsidian_Note object based on the content of the note give as context, a string.
        Updates the following attributes: tags, incoming_links, outgoing_links, frontmatter, dataview_metadata, and dataview_metadata_fields 
        """
        self.tags = self.get_tags(context)
        with open(self.path, "r") as file: 
            self.content = file.read()

    def get_tags(self, content) -> list: 
        """
        Retreives the tags of the note defined in Frontmatter syntax, obsidian content syntax, and dataview syntax.

        Returns: 
            A list of tags for the note. 
        """
        ### FRONTMATTER ###
        tags = []
        ### CONTENT ###
        for line in content.split("\n"): 
            # split around spaces
            for word in line.split(" "): 
                if word.startswith("#"): 
                    tags.append(word.replace("#", ""))
        ### DATAVIEW ### 
        for line in content.split("\n"): 
            if line.startswith("tags::"): 
                tags += line.replace("tags::", "").strip().split(" ")
        return tags

