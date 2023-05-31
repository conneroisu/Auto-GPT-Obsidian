""" 
Import the OS module to operate on the file system of the operating computer.
"""
import os


class Note:
    """
    Note object for the AutoGPT plugin, AutoGPTObsidian.
    A Note object is a representation of a note in the Obsidian vault.
    A Note object contains the path, title, content, frontmatter, and dataview_metadata of the note.
    """

    def __init__(self, path):
        """
        Initialize the note object with the given parameters.

        Args:
            path: The path of the note.
        """
        # Title  -  the title of the note without the file extension aka `.md`.
        # Content  -  the entire content of the note including the frontmatter.
        # Frontmatter  -  the frontmatter of the note inbetween the `---`s.
        # Dataview Metadata  -  the metadata of the note for the Dataview plugin.
        self.path = path
        self.title = get_title(path)
        self.content = None
        self.frontmatter = None
        self.dataview_metadata = None

    def get_frontmatter(self) -> dict:
        """
        Retreives the frontmatter metadata the defined in the frontmatter of the note.

        Returns:
            A frontmatter object for the note containing the metadata values of the note.
        """
        for line in content:
            if line.startswith("---") and line.endswith("\n"):
                beginning_line = line
                for sline in content:
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

    def get_summary(self):
        """
        Get the summary of the note defined in the frontmatter or in dataview syntax.
        """
        return frontmatter.summary

    def get_tags(self) -> list | None:
        """
        Get the tags of the note defined in the frontmatter or in dataview syntax.
        """
        return frontmatter.tags

    def get_title(self):
        """
        Get the title of the note.
        The title of the note is the final part of the path of the note.
        """
        separator = os.path.sep
        return self.path.split(separator)[-1]

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
        # TODO - this method needs tested
        if self.get_aliases() is not None:
            self.aliases += aliases
        else:
            self.aliases = aliases

    def change_summary(self, summary) -> str:
        """
        Change the summary of the note. Changes the frontmatter.summary value to the given summary, and changes note's summary value to the given summary.

        Args:
            summary: The new summary of the note.
        """
        # TODO - this method needs to change the note
        self.frontmatter.summary = summary

    def create_note_flashcards(self) -> str:
        """
        Create flashcards for the note.
        """
        # TODO - this method needs to be implemented
        # Needs a title not already in the vault
        # Needs to create a note with the title of the note + "Flashcards" + number of flashcards for that note in the vault.

        pass
