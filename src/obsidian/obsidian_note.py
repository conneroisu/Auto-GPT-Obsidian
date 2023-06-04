""" 
Import the OS module to operate using operating system of the operating computer.
"""
import os
import obsidian

class Obsidian_Note:
    """
    Note object allowing for inteactions with markdown notes with the syntax of Obsidian for the AutoGPT plugin, AutoGPTObsidian.
    Note Title - the title of the file/note defined by the path of the note/file. Additively, the title of the note without the file extension aka `.md`.
    Note Content - the entire content of the file/note including the frontmatter. 
    Note Frontmatter - the content of an Obsidian Note inside of "---"s at the front of a note or defined with dataview syntax
    Note Meta data - the metadata fields and their corresponding values of the note/file 
    """
    def __init__(self, note_path: str) -> None: 
        """
        Initialize the Obsidian_Note object with the given parameters.

        Args:
            path: The path of the note with respect to the vault_working_directory. 
        """
        git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        current_working_directory = os.getcwd() 
        vault_working_directory = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])
        self.tags = None
        self.incoming_links = None
        self.outgoing_links = None

        with open(note_path, "r") as file: 
            self.content = file.read()

        self.frontmatter = None
        self.dataview_metadata = None

    def get_frontmatter(self) -> dict|None:
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
                    self.frontmatter.value = data
        return self.frontmatter

    def get_value_in_frontmatter(self, value):
        """
        Get the predefined value in the frontmatter of the note.

        Parameters:
            value: The value to get from the frontmatter.

        Returns:
            The value in the frontmatter. If the value is not in the frontmatter, returns None.
        """
        self.get_frontmatter()
        return frontmatter.value

    def is_value_in_content_as_dataview(self, value):
        """
        Determines whether the value is in the content of the note as a dataview.

        Parameters:
            value: The value to check for in the content in dataview syntax.

        Returns:
            True if the value is in the content, False otherwise.
        """
        value += "::"
        for line in content:
            if line.startswith(value):
                value = line.split("::")[0]
                data = line.split("::")[1]
                self.dataview_metadata.value = data


    def add_tags(self, tags) -> str:
        """
        Add tags to the note.

        Args:
            tags: The tags to add to the note.
        """
        if self.get_tags() is not None:
            self.tags += tags
        else:
            self.tags = tags


    def add_aliases(self, aliases) -> str:
        """
        Add aliases to the note.

        Args:
            aliases: The aliases to add to the note.
        """
        if self.get_aliases() is not None:
            self.aliases += aliases
            update_note(self)
            return "Aliases added to note."

    def set_summary(self, new_summary) -> str:
        """
        Change the summary of the note. Changes the frontmatter.summary value to the given summary, and changes note's summary value to the given summary.

        Args:
            summary: The new summary of the note.
        """
        self.frontmatter.summary = summary

        # Replace the old summary from the note's content with the new summary
        self.content = self.content.replace(self.summary, new_summary)))
        
        # Do the same to the file 
        with open(self.path, "w") as f:
            f.write(self.content)
            return "Summary changed successfully."
       return "Summary change failed. The current path is " + self.path + " and the current summary is " + self.summary + " and the new summary is " + new_summary + "." 

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
