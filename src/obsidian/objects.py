import os 

class Note: 
    """
    Note object for the AutoGPT plugin, AutoGPTObsidian.
    """

    def __init__(self, path):
        """
        Initialize the note object with the given parameters.
        Args:
            path: The path of the note.
        """
        self.path = path
        self.title = get_title(path)
        self.aliases = None
        self.tags = None
        self.summary = None
        self.content = None
    def is_value_in_frontmatter(self, value):
        """
        Determines whether the value is in the frontmatter of the note as a metadata value.
        TODO - Need to implement and finish this method.
        """
        pass
    def is_value_in_content_as_dataview(self, value):
        """
        Determines whether the value is in the content of the note as a dataview.
        TODO - Need to implement dataview syntax
        """
        pass

    def get_summary(self):
        """
        Get the summary of the note defined in the frontmatter or in dataview syntax.
        TODO - Need to implement dataview syntax and finish this method.
        """
         pass
    def get_tags(self):
        """
        Get the tags of the note defined in the frontmatter or in dataview syntax.
        TODO - Need to implement dataview syntax and finish this method.
        """
    def get_aliases(self):
        """
        Get the aliases of the note defined in the frontmatter or in dataview syntax.
        TODO - Need to implement dataview syntax and finish this method.
        """
        aliases = None
        note = open(self.path, "r")
        # frontmatter check
        for line in note.readlines():
            if line == "---":
                inside = true
                break
            if inside:
                if line.startswith("aliases:"):
                    aliases = line.split(":")[1]
                    break
           pass
    def get_title(self):
        """
        Get the title of the note.
        The title of the note is the final part of the path of the note.
        """
        separator = os.path.sep
        return self.path.split(separator)[-1]

    def add_tags(self, tags):
        """
        Add tags to the note.

        Args:
            tags: The tags to add to the note.
        """

    def add_aliases(self, aliases):
        """
        Add aliases to the note.

        Args:
            aliases: The aliases to add to the note.
        TODO - this method is not implemented yet.
        """

        pass 


    def change_summary(self, summary):
        """
        Change the summary of the note.

        Args:
            summary: The new summary of the note.
        TODO - this method is not implemented yet.
        """
        pass 


    
