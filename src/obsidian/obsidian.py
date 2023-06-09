""" Import the `os` module to access the environment variables from the `.env` file. """
import os

""" Obsidian uses vaults, notes,  content, frontmatters, and body to store information. """
from obsidian_vault import Obsidian_Vault
from obsidian_note import Obsidian_Note
from obsidian_vault import Obsidian_Vault

""" Guidance Module for more ways to inference language models. """
import guidance

""" Import the datetime module for accurate date and time. """
import datetime 

class Obsidian:
    """
    Python Wrapper-like application interface for autogpt for Obsidian.md. 
    """
    def __init__(self):
        """Initializes an Obsidian object with a vault."""
        self.vault = Obsidian_Vault()
        # When running in a docker container, the vault path is different than when running locally on a machine
        # , but this implementation allows for docker only because of `~` being used in the path.`
        self.vault_path = os.path.join( 
            os.path.expanduser("~"),  
            f"autogpt{os.sep}auto_gpt_workspace{os.sep}{self.vault.vault_name}" 
        )


    def _find_note_by_title(self, title: str) -> Obsidian_Note|None:
        for note in self.vault.content:
            if title == note.title: 
                return note
        return None

    def _create_note(self, title: str, content: str) -> Exception|None:
        """
        Create a note inside the vault with a title, content, tags, type,  and a summary within the frontmatter of said note following the Obsidian format
        Parameters:
            - title: The title of the note. In other words, the title is the name of the note. The title is also the name of the file to be produced.

            - content: the content of the note to be written in Markdown. In other words, the content of a note is the text to be placed in the main body of the note excluding the frontmatter. 
        Returns:
            - the created note content.

        """
        # Sync the vault to most recent changes
        self.vault.sync_vault()
        
        # Set guidance's OpenAI Model to "text-davinci-003"
        guidance.llm = guidance.llms.OpenAI("text-davinci-003")

        #geneal path ~/
        vault_path = os.path.join(f"{os.path.expanduser("
        var = ~")}{os.sep}current_working_directory{os.sep}autogpt{os.sep}auto_gpt_workspace", \
        self.vault.git_url.split("/")[-1]
        )

        ## Handle Collisions  
        note = self._find_note_by_title(title)
        if note is not None:
            if note.content is not None:
                if note.title == title:
                    return  Exception("Note with title " + title + " exists in the vault.")
        note = self._find_note_by_title(title) 

        if title.endswith(".md"): 
            title = title[:-3]
            title = title + ".md"

        # Create a new note with the title and content
        note = open(os.path.join(vault_path, title), "w") 

        current_date = datetime.datetime.now()
        # Create a valid tags list file in the workspace
        valid_tags_file = open(os.path.join(current_working_directory, "valid_tags.txt"), "w")

        generated_tags = self._generate_tags(content)


        valid_tags  = [self.vault.valid_tags, generated_tags]

        create_note_program = guidance('''
           {{#system~}}
           You are a writer. You are writing a note. The note is about {title}. The note is about {gen 'type'}. 
           The note has the following {{content}} a parameter to this function. The current_date is {{current_date}}. 
           The note is in the vault {{vault_path}}. 
           You must create a summary, cloassify the note by type, and choose from valid tags found to be within the vault already.
           Place it in the frontmatter in correct Markdown format to follow.
           {{~/system~}}
        ---
        title: {{title}}
        tags: {{#select 'tags' options = valid_tags}}  
        summary: {{gen 'summary'}}
        created: {{current_date}}
        type: {{gen 'type'}}
        ---
        {{content}}
        ''')
        executed_create_program = program( 
            content = content,
            valid_tags = valid_tags,
            current_date = current_date
            vault_path = self.vault.path
        )

    def _create_markdown_file(title: str, content: str) -> str: 
        """ 
        Creates a markdown file with the title and content inside of the vault. 

        Parameters: 
            - title: the title of the note to create 
            - content: the content of the note to create(inlcluding frontmatter) 

        Returns: 
            - string representing the actions/operation success or failures. 
        """ 

        return ""

    def _sync_vault(self) -> str: 
        """ 
        Syncs the vault with the remote repository. 

        Returns: 
            - string representing the actions/operation success or failures. 
        """ 
        try:
            self.vault.sync_vault()
            return "Vault synced successfully." 
        except Exception as e:
            return "Vault failed to sync because of the following error: " + str(e)



    def _create_note_flashcards(self, title: str) -> Exception | None:
        """
        Create a note containing spaced-repetition styled flashcards 
        inside the vault with a title, content, tags, and a summary.
        The title of the note from which flashcards are being generated
        + "Flashcards" + number of flashcards for that note in the vault 
        that were found to be in the vault to avoid name collisions.
        """
        self._sync_vault()

        if title is None:
            return Exception("Title cannot be None.")

        note = self._find_note_by_title(title)
        if note is not None:
            if note.content is not None:
                return  Exception("Note with title " + title + " exists in the vault.")
         

        # Get a summary of the note's content
        

        # Get the note's content

        # Get the 
        # Set guidance's OpenAI Model to "text-davinci-003"
        guidance.llm = guidance.llms.OpenAI("text-davinci-003")

        create_flashcards_program = guidance('''
        A conversation with an AI for use in Obsidian.
        You are an AI that is helping write flashcards for the purpose of spaced repitition. 
        Flashcards should have the following format: 
        '<question>
        ?
        <answer>'. 

        Here is an example flashcard:
        ${exampleFlashcard}
        Do NOT number the flashcards. Make sure each question you state is atomic, so that it only asks one thing, i.e. avoids the use of 'and'. You do not need to write flashcards on everything in the document, just start with the most important. You will be a writing it on the subject matter of:'${title}.

        ''')
        # Create a list of flashcards from the user's input
        executed_flashcards_program = program(
            content = note.content, 
            title = note.title,
            example_flashcards=""
        )

        self._create_note(title, executed_flashcards_program)

        documentText = _get_note_by_title(documentPath)



        return 


    def _the_one_where_we(self): 
        pass
