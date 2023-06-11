"""Python Wrapper-like application interface for autogpt for Obsidian.md"""

"""Operating System Operations for Working with Files and Directories within the Operating System"""
import os

"""Guidance Library for Prompt LLM Models with a more Predictable, Definable Output"""
import guidance

"""Obsidian Note meta-object library to imitate the Operations and Attributes of notes inside of an Obsidian_Vault Object"""
from obsidianNote import ObsidianNote
from obsidianNote import obsidianNote

"""Obsidian Vault meta-object to imitate the operations of the Obsidian Vault"""
import obsidianVault

"""Import the datetime Module for Accurate Time"""
import datetime


class Obsidian:
    def __init__(self):
        """Initializes an Obsidian object with a vault."""
        self.vault = obsidianVault
        self.vault_path = os.path.join(
            os.path.expanduser("~"),
            f"autogpt{os.sep}auto_gpt_workspace{os.sep}{self.vault.vault_name}",
        )

    def _find_note_by_title(self, title: str) -> obsidianNote | None:
        return self.vault.find_by_title(title)

    def _create_note(self, title: str, content: str) -> Exception | None:
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

        guidance.llm = guidance.llms.OpenAI("text-davinci-003")

        # geneal path ~/
        if self.vault.git_url is None:
            return Exception(
                "Vault is not a git repository. Please make sure that the vault is a git repository."
            )

        self.vault.git_url.split("/")[-1]

        note = self._find_note_by_title(title)
        if note is not None and note.title == title:
            return Exception(f"Note with title {title} exists in the vault.")

        note = self._find_note_by_title(title)

        if title.endswith(".md"):
            title = title[:-3]
            title = f"{title}.md"

        note = open(os.path.join(self.vault.vault_path, title), "w")
        note = open(os.path.join(self.vault.vault_path, title), "w")

        note = open(os.path.join(self.vault.vault_path, title), "w")

        current_date = datetime.datetime.now()
        valid_tags_file = open(
            os.path.join(self.vault.vault_path, "valid_tags.txt"), "w"
        )
        create_note_program = guidance(
            """
            {{#system~}}
            You are a writer. You are writing a note. The note is about {title}. The note is about {gen 'type'}.
            The note has the following {{content}} a parameter to this function. The current_date is {{current_date}}.
            The note is in the vault {{vault_path}}.
            You must create a summary, classify the note by type, and choose from valid tags found to be within the vault already.
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
        """
        )
        executed_create_program = create_note_program(
            content=content,
            valid_tags=self.vault.get_valid_tags(),
            current_date=current_date,
            vault_path=self.vault.path,
            title=title,
        )

    def _create_markdown_file(self, note_path: str, content: str) -> Exception | None:
        """
        Creats a markdown file and Obsidian Note housed inside the obsidian vault and the Obsidian_Vault object respectively.

        Parrameters:
        - note_path : name of the file to crerate and the title of the note to create within the obsidian vault

        """
        if not note_path.endswith(".md"):
            note_path += ".md"
        try:
            self._sync_vault()
            note = obsidianNote(self.vault, note_path)
        except Exception as e:
            return e

        return None

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
            return f"Vault failed to sync because of the following error: {str(e)}"

    def _create_note_flashcards(self, title: str) -> Exception | None:
        """
        Create Spaced-Repetition Styled Flashcards inside the vault with title,
        content, tags, and summary. The title of the note from which flashcards
        are being generated + "Flashcards" + number of flashcards for that note
        in the vault that were found to be in the vault to avoid name collisions.

        Parameters:
            - title : the title of the note to create inside of the obsidian vault
        """

        self._sync_vault()

        if title is None:
            return Exception("Title cannot be None.")
        note = self._find_note_by_title(title)
        if note is not None and note.content is not None:
            return Exception("Note with title " + title + " exists in the vault.")
        executed_flashcards_program = guidance(
            """
                A conversation with an AI for use in Obsidian.
                You are an AI that is helping write flashcards for the purpose of spaced repetition.
                Flashcards should have the following format:
                '<question>
                ?
                <answer>'.

                Here is an example flashcard:
                ${exampleFlashcard}
                Do NOT number the flashcards. Make sure each question you state is atomic, so that it only asks one thing, i.e. avoids the use of 'and'. You do not need to write flashcards on everything in the document, just start with the most important. You will be a writing it on the subject matter of:'${title}.
            """
        )
        self._create_note(title, executed_flashcards_program)
