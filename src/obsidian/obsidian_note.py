"""Import the OS module to operate using operating system of the operating computer."""
import os
from obsidian.obsidian_frontmatter import Frontmatter

from obsidian.obsidian_vault import Obsidian_Vault

class Obsidian_Note():
    """
    Note object allowing for inteactions with markdown notes with the syntax of Obsidian for the AutoGPT plugin, AutoGPTObsidian.
    Attributes:  | Description:
    Note Title - the title of the file/note defined by the path of the note/file. Additively, the title of the note without the file extension aka `.md`.
    Note Content - the entire content of the file/note including the frontmatter. 
    Note Body - the content of the note without the frontmatter.
    Note Frontmatter - the content of an Obsidian Note inside of "---"s at the front of a note or defined with dataview syntax
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
        self.frontmatter: Frontmatter
        self.content = None
        self.body = None
        self.update_note_attributes(self.content)

#    def format_frontmatter(self) -> str:
        """ 
        Formats the frontmatter of the note to be in a standard format as chosen by AutoGPTObsidian.
        --- 
        tags: [tag1, tag2, tag3]
        aliases: [alias1, alias2, alias3]
        summary: [summary]
        ---

        """
#        self.reload()
        


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
        ######FRONTMATTER###### 
        self.frontmatter = self.get_frontmatter(context)
        ######TAGS######
        # Get the tags of the note
        self.tags = self.get_tags(context)
        ######CONTENT######
        with open(self.path, "r") as file: 
            self.content = file.read()


    def get_tags(self, content) -> list: 
        """
        Retreives the tags of the note defined in Frontmatter syntax, obsidian content syntax, and dataview syntax.

        Returns: 
            A list of tags for the note. 
        """
        tags = []
        ### FRONTMATTER ###
        for line in self.frontmatter.split("\n"): 
            if line.startswith("tags:"): 
                tags = line.replace("tags:", "").strip().split(" ")
        ### CONTENT ###
        for line in content.split("\n"): 
            # split around spaces
            for word in line.split(" "): 
                if word.startswith("#"): 
                    tags.append(word) 
        ### DATAVIEW ### 
        for line in content.split("\n"): 
            if line.startswith("tags::"): 
                tags += line.replace("tags::", "").strip().split(" ")


        return tags

    def get_frontmatter(self, context: str) -> dict|None:
        """
        Retreives the frontmatter metadata the defined in the frontmatter of the note.

        Returns:
            A frontmatter object for the note containing the metadata values of the note.
        """
        for line in self.content:
            if line.startswith("---") and line.endswith("\n"):
                beginning_line = line
                for sline in self.content:
                    if (
                        sline.startswith("---")
                        and sline.endswith("\n")
                        and sline != beginning_line
                    ):
                        end_line = sline
        # Now that we have the beginning and end of the frontmatter, we can check if the value is in the frontmatter.
        inside = False
        for line in content:
            if line == beginning_line:
                inside = True
            if line == end_line:
                inside = False
            if inside:
                # for each value in the frontmatter set frontmatter.value to said value.
                for char in line:
                    value = line.split(":")[0]
                    data = line.split(":")[1]
        return self.frontmatter


    def run_core_template(self):
        # TODO: Run the core template.
        pass
