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
        self.frontmatter = None
        self.dataviewmetadata = None

    def get_frontmatter(self):
        """
        Creates a frontmatter object for the note containing the metadata values of the note.

        Returns:
            A frontmatter object for the note containing the metadata values of the note.
        """
        for line in content:
            if line.startswith("---") and line.endswith("\n"):
                beginning_line = line
                for sline in content:
                    if sline.startswith("---") and sline.endswith(
                            "\n") and sline != beginning_line:
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
                self.dataviewmetadata.value = data
    def get_summary(self):
        """
        Get the summary of the note defined in the frontmatter or in dataview syntax.
        TODO - Need to implement dataview syntax and finish this method.
        """

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


def has_tags(title: str) -> bool:
    """
    Check if a note has tags. Returns true if so.

    Parameters:
        - title: The title of the note. In other words, the title is the name of the note. The title is also the name of the file to be produced.
    Returns:
        - True if the note has tags, False if not.
    """


def change_summary(self, summary):
    """
    Change the summary of the note.

    Args:
        summary: The new summary of the note.
    TODO - this method is not implemented yet.
    """
    pass
