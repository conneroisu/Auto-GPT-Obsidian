"""For Type Checking and Lists"""
from typing import TYPE_CHECKING, List

"""Obsidian Note Object for operating representing markdown files in the vault""" 
from obsidian import obsidianNote

"""Import the guidance llm python library for LLM prompting"""
import guidance

"""Operating System operations allowing for operating system integation"""
import os

"""Github Operations allowing for control of Git Operations for the Obsidian Vault"""
from git.repo import Repo

class obsidianVault: 
    """
    Vault Object allowing for interactions with markdown notes specifically with the syntax 
    of Obsidian Markdown for the AutoGPT plugin, AutoGPT-Obsidian.

    This metaphorical obsidian vault class has a few native components on itself: 
          `markdown content` : The Markdown Files in the vault.  
          `vault path`       : The path of the vault within the file system.
          `vault name`       : The name of the vault. 
          `git url`          : The git url of the vault. 
          `git api key`      : The git api key of the vault. 
          `git username`     : The git username of the vault.
    """
    def __init__(self) -> None:
        """Initializes the Obsidian Vault Object"""
        # Retrieve the environment variables for the obsidian plugin
        self.initialize_environment_variables()
        self.sync_vault()
        self.vault_directory = os.sep.join([ os.path.expanduser("~"), "autogpt", "auto_gpt_workspace", self.vault_name ])
        self.content = self.get_vault_content()

        
    def initialize_environment_variables(self) -> Exception|None:
        """Initializes the Environment Variables for the Obsidian Plugin"""
        if os.getenv("OBSIDIAN_GITHUB_API_KEY"):
            self.git_api_key = os.getenv("OBSIDIAN_GITHUB_API_KEY")
        else: 
            return Exception("Please set the OBSIDIAN_GITHUB_API_KEY environment variable in the .env file.")

        if os.getenv("OBSIDIAN_VAULT_GIT_URL"):
            self.git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        else: 
            return Exception("Please set the OBSIDIAN_VAULT_GIT_URL environment variable in the .env file.")

        if os.getenv("OBSIDIAN_GITHUB_USERNAME"):
            self.git_username = os.getenv("OBSIDIAN_GIT_USERNAME")
        else: 
            return Exception("Please set the OBSIDIAN_GIT_USERNAME environment variable in the .env file.")

        if os.getenv("OBSIDIAN_VAULT_NAME"): 
            self.vault_name = str(os.getenv("OBSIDIAN_VAULT_NAME"))
        else:
            return Exception("Please set the OBSIDIAN_VAULT_NAME environment variable in the .env file.")

        if os.getenv("OBSIDIAN_VAULT_PATH"): 
            self.vault_path = str(os.getenv("OBSIDIAN_VAULT_PATH")) 
        else:
            return Exception("Please set the OBSIDIAN_VAULT_PATH environment variable in the .env file.")

        if os.getenv("OBSIDIAN_GITHUB_API_KEY"): 
            self.git_api_key = os.getenv("OBSIDIAN_GITHUB_API_KEY")
        else: 
            return Exception("Please set the OBSIDIAN_GITHUB_API_KEY environment variable in the .env file.")

        if os.getenv("OBSIDIAN_FLASHCARD_DIRECTORY"): 
            self.flashcard_directory = os.getenv("OBSIDIAN_FLASHCARD_DIRECTORY")
            return None
        else: 
            return Exception("Please set the OBSIDIAN_FLASHCARD_DIRECTORY environment variable in the .env file.")

    def clone_vault(self) -> Exception|None:
        """Clones the Vault from the Vaults Git Url into the Workspace"""
        # Create the working directory
        working_directory = os.path.join(os.path.expanduser("~"), "autogpt"+ os.sep  +  "auto_gpt_workspace" + os.sep +  self.vault_name)
        os.makedirs(working_directory, exist_ok=True)
        try: 
            Repo.clone_from(self.git_url, working_directory)
            return None
        except Exception as e:
            return e

    def search_vault_title(self, title: str) -> obsidianNote:
        """ 
        Searches the Obsidian Vault's content for an Obsidian_Note with a given title

        Parameters: 
              title: the Title to `Search` for inside the Vault.
        """
        # For each file with a `.md` extension as target:
        # for ob_note in self.markdown_content: 
        # List result = 
        for note in self.content:
            if note.title == title: 
                return note

        return None

    def sync_vault(self) -> Exception|None: 
        """ 
        Sync the Obsidian Vault within the workspace with the remote Git repository.
        If there is a vault in the workspace, then it syncs the vault with the remote 
        Git repository. If not, then it clones the remote Git repository into the workspace.

        Returns: 
            Exception or None for an exception thrown or successful operation
        """
        git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        git_api_key = os.getenv("OBSIDIAN-GITHUB_API_KEY")
        git_username = os.getenv("OBSIDIAN-GITHUB_USERNAME")
        if self.git_url is None:
            return Exception("2319 - No Git URL provided.") 
        split_url = self.git_url.split("//")
        auth_repo_url = f"//{git_username}:{git_api_key}@".join(split_url)

        repo = Repo(self.vault_directory)
        origin = repo.create_remote("origin", repo.remotes.origin.url)
        assert origin.exists()
        assert origin == repo.remotes.origin == repo.remotes["origin"]
        # There are changes in the remote repository, then pull the latest changes from the remote repository.
        if repo.head.commit != repo.remotes.origin.fetch()[0].commit: 
            repo.git.pull()
            try:
                repo.git.add(update=True) 
                repo.git.commit("-m", "Auto-commit from AutoGPT") 
                origin = repo.remote(name="origin")
                origin.push() 
                return None 
            except Exception as e: 
                return e

        # If there are changes in repo
        elif repo.is_dirty():
            repo.git.add(update=True) 
            repo.git.commit("-m", "Auto-commit from AutoGPT") 
            origin = repo.remote(name="origin")
            try:
                origin.push()
                print(f"""Pushed changes to {git_url}""")
                return None 
                
            except Exception as e: 
                return e

    def get_valid_tags(self) -> list: 
        """ 
        Retrieves a list of valid tags from the vault. 

        Returns: a list of valid tags used within the vault.
        """ 
        # Set guidance's OpenAI Model to "text-davinci-004"
        guidance.llm = guidance.llms.OpenAI("gpt4")

        # Sync the vault to most recent changes
        self.sync_vault()

        # Create a list of valid tags from the vault
        valid_tags = []

        # Iterate through the vault to find all tags
        for root, [], files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as f:
                        for line in f.readlines():
                            if line.startswith("tags:"):
                                for tag in line.split(":")[0].split(","):
                                    valid_tags.append(tag.strip())

        # Additionally, Obsidian allows for tags to be defined as #tags, so we will add those to the list of valid tags.
        for root, [], files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as f:
                        for line in f.readlines():
                            for word in line.split(" "):
                                if word.startswith("#"):
                                    valid_tags.append(word.strip())
        return valid_tags

    # A function to get the content of the vault returning a list Obsidian_Note objects 
    def get_vault_content(self) -> list:
            """A Basic Method to get the Content of the Vault returning a list Obsidian_Note Objects"""
            notes = []

            for root , [] , files in os.walk(self.vault_path):
                for file in files:
                    if file.endswith(".md"):
                        with open(os.path.join(root, file), "r"):
                            # Create a new Obsidian_Note object with a reference to the Obsidian_Vault object
                            note = obsidianNote(self, note_path=os.path.join(root, file))
                            notes.append(note)
            return notes

    def smart_seach(self, topic: str):
        pass

    def find_by_title(self, title:str) -> obsidianNote:
        """Finds an Obsidian_Note by its Title"""
        notez = None
        for note in self.content:
            if (note.title == title):
                notez = note
                return notez
        return None  

    def create_note(self, title: str, content: str = "") -> obsidianNote:
        """Creates a new Obsidian_Note in the Vault"""
        note = obsidianNote(self, note_path )
        return note
