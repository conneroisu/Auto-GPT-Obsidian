"""Import the OS module to operate using operating system of the operating computer."""
import os

"""Import Obsidian Objects for Dealing with Files Used By Obsidian MD."""
from obsidian.obsidian_frontmatter import Obsidian_Frontmatter
from obsidian.obsidian_vault import Obsidian_Vault

class Obsidian_Note():
    """
    Note Object allowing for better interactions with Obsidian Markdown, local files.
    Note Title - the title of the file/note defined by the path of the note/file. 
    Note Content - the content of the file including the fontmatter of the note.
    Note Body - the entire content of the file not including the frontmatter. 
    Note Frontmatter - the content of an Note inside of "---\n"s at the top. 
    """
    def __init__(self, note_path) -> None: 
        """
        Creates the Obsidian_Note Object with the given path.
        Args:
            path: The internal path of the note with respect 
            to the vault_working_directory. (Not including the vault_directory)
        """
        self.path = note_path
        self.title = self.get_title(note_path)
        self.frontmatter = self.get_frontmatter(note_path)
        self.content = self.get_content(note_path)
        self.body = self.get_body(note_path)
        self.update_note_attributes(self.content)

    def get_body(self, note_path) -> str: 
        """ 
        Get the Body of the content of the note without the frontmatter. 
        Args: 
            note_path: The path of the note to get the body of. 
        Returns: 
            body: The body of the note.
        """ 
        with open(note_path, "r") as note_file: 
            note_content = note_file.read()
        frontmatter = self.get_frontmatter(note_path)
        note_body = note_content.replace(frontmatter.content, "")
        return note_body

    def get_content(self, note_path) -> str: 
        """ 
        Returns the content of the note outside of the frontmatter. 
        Args: 
            note_path: The path of the note to get the body of. 
        Returns: 
            content: The content of the note.
        """
        with open(note_path, "r") as note_file: 
            note_content = note_file.read()
        return note_content


    def get_frontmatter(self, note_path) -> Obsidian_Frontmatter: 
        """
        Returns the frontmatter of the note. 
        Args:
            note_path: The path of the note. 
        Returns:
            The frontmatter of the note. 
        """
        return Obsidian_Frontmatter(note_path) 

    def get_title(self, note_path) -> str: 
        """
        Returns the title of the note. 

        Args:
            note_path: The path of the note. 

        Returns:
            The title of the note. 
        """
        return os.path.basename(note_path)

    def reload(self) -> None: 
        """
        Reloads the note content from the file at the note's path. 
        """
        self.title = self.get_title(self.path)
        self.frontmatter = self.get_frontmatter(self.path)
        self.content = self.get_content(self.path)
        self.body = self.get_body(self.path)
        self.update_note_attributes(self.content)

    def update_note_attributes(self, context:str) -> None: 
        """
        Updates the attributes of the Obsidian_Note object based on the content of the note give as context, a string.
        Updates the following attributes: tags, incoming_links, outgoing_links, frontmatter, dataview_metadata, and dataview_metadata_fields 
        """

        self.frontmatter = self.get_frontmatter(context)

        self.tags = self.get_tags(context)

        self.incoming_links = self.get_incoming_links(context)

        self.outgoing_links = self.get_outgoing_links(context)



    def get_frontmatter(self, note_path) -> Obsidian_Frontmatter: 
        """ 
        Retreives the frontmatter of the note defined in Frontmatter syntax. 
        Args: 
            note_path: The path of the note. 
        Returns: 
            An Obsidian_Frontmatter object.
        """
        return Obsidian_Frontmatter(note_path)

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


    def run_core_template(self) -> Exception|bool:
        """
        Similar to the templates core plugin for Obsidian, this function tries to emulate the evaluation of {{date}} and {{title}}
        """
        for line in self.content:  
                    if "{{date}}" in line: 
                        line = line.replace("{{date}}", datetime.now().strftime("%m/%d/%Y"))
                    if "{{title}}" in line: 
                        line = line.replace("{{title}}", self.title) 
                    # If the date and title come with javascript styled modifier  
                    

    def run_plugin_templater(self): 
        pass
