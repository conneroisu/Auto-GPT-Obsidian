import os

from obsidian_vault import Obsidian_Vault
from obsidian_note import Obsidian_Note
from obsidian_vault import Obsidian_Vault

import guidance
import datetime 

class Obsidian:
    def __init__(self):
        self.vault = Obsidian_Vault()
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
        # Sync the vault to most recent changes
        self.vault.sync_vault()
        
        # Set guidance's OpenAI Model to "text-davinci-003"
        guidance.llm = guidance.llms.OpenAI("text-davinci-003")

        #geneal path ~/
        if self.vault.git_url is None:
            return Exception("Vault is not a git repository. Please make sure that the vault is a git repository.")

        self.vault.git_url.split("/")[-1]

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

        note = open(os.path.join(self.vault.vault_path, title), "w") 

        current_date = datetime.datetime.now()
        # Create a valid tags list file in the workspace
        valid_tags_file = self.vault.get_valid_tags()



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
            valid_tags = self.vault.get_valid_tags(),
            current_date = current_date
            vault_path = self.vault.path
        )

    def _create_markdown_file(title: str, content: str) -> str: 
        return ""

    def _sync_vault(self) -> str: 
        try:
            self.vault.sync_vault()
            return "Vault synced successfully." 
        except Exception as e:
            return "Vault failed to sync because of the following error: " + str(e)



    def _create_note_flashcards(self, title: str) -> Exception | None:
        self._sync_vault()
        if title is None:
            return Exception("Title cannot be None.")
        note = self._find_note_by_title(title)
        if note is not None:
            if note.content is not None:
                return  Exception("Note with title " + title + " exists in the vault.")
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
