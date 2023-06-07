""" Import the operating system module to allow for operating system dependent functionality. """
import os

class Obsidian_Frontmatter: 
    def __init__(self, note_path: str) -> None:
        # The path to the note is the note_path
        self.note_path = note_path
        self.content = self.get_content()
        # Self.values is a dictionary of key-value pairs
        self.values = {}

        for line in self.content: 
            key, value = line.split(":")
            self.values[key] = value

    def add(self, key, value):
        self.values[key] = value 


    def get_content(self):        
        """ 
        Returns the content of the frontmatter.  
        """
        with open(self.note_path, "r")as file:
            for line in file:
                count = 0
                content = ""
                if line.startswith("---"):
                    count += 1
                    if count >= 2: 
                        return content
                    else:
                        content += line
                        continue
            return content
        return ""

        ################### TMEPALTRTEJ DCXOXWE 
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

