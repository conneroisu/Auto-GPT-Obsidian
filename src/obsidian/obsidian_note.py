"""perate using operating system of the docker container"""
import os

from obsidian.example_avl import avl_Node

"""the library `python-frontmatter` for working with frontmatters of files"""
import frontmatter

"""Obsidian Vault Meta Object for working for files inside of the obsidian vault"""
from obsidian_vault import Obsidian_Vault

class Obsidian_Note(avl_Node):
    """Note object allowing for inteactions with markdown notes with the syntax of Obsidian for the AutoGPT plugin, AutoGPTObsidian"""

    def __init__(self, vault: Obsidian_Vault, note_path) -> None: 
        """
        Initialize the Obsidian_Note object with the given vault_path inside of the AutoGPT Workspace.

        Args:
            path: The path of the note with respect to the vault_working_directory. (Not including the vault_directory)
        """
        # Vault : The `Obsidian_Vault` object assigned with the Note Object.
        self.vault = vault # Vault provides access to the notes in the vault.
        # Note Title : The Title of the file/note defined by the path of the note/file. 
        self.path = os.path.join(vault.vault_directory, note_path)
        # Note Title : the Title of the Obsidian_Note
        self.title = os.path.basename(self.path).replace(".md", "")  

        with open(os.path.join(vault.vault_directory, note_path)) as f:
            self.frontmatter = frontmatter.load(f)
            self.update_note_attributes(f.read())
        

    def reload(self) -> None: 
        """Reloads the note content from the file at the given path"""
        with open(self.path, "r") as f: 
            self.content = f.read()
        if self.content is None: 
            self.content = ""
        self.update_note_attributes(self.content)

    def update_note_attributes(self, context:str) -> None: 
        """
        Updates the attributes of the Obsidian_Note object based on the content of the note give as context, a string.
        Updates the following attributes: tags, incoming_links, outgoing_links, frontmatter, dataview_metadata, and dataview_metadata_fields 

        Parameters: 
            context : string representing the the content of the note to update the ntoe attributes on 
        """
        self.tags = self.get_tags(context)
        
        with open(self.path, "r") as file: 
            self.content = file.read()


    def get_tags(self, content) -> list: 
        """
        Retreives the tags of the note defined in Frontmatter syntax, obsidian content syntax, and dataview syntax. It first checks the frontmatter, then the content, then for tags defined in the dataview syntax.

        Returns: 
            list : A list of tags marked with the note for this Obsidian_Vault Object
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

