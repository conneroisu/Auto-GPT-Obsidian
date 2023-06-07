"""Import typing for type checking and List"""
from typing import TYPE_CHECKING, List

"""Import Obsidian Objects for Dealing with Files Used By Obsidian"""
from obsidian.obsidian_note import Obsidian_Note
from obsidian.obsidian_frontmatter import Obsidian_Frontmatter

"""Used to operate using operating system of the operating computer, debian, in the case of the auto_gpt docker."""
import os

"""Provides Git Operations for Obsidian and AutoGPT-Obsidian"""
from git.repo import Repo

class Obsidian_Vault: 
    """
    Vault Object allowing for interactions with markdown notes specifically with the syntax 
    of Obsidian Markdown for the AutoGPT plugin, AutoGPT-Obsidian.

    This metaphorical Obsidian Vault class has a few native components on itself: 
        - `markdown content` - The Markdown Files in the vault.  
        - `vault path`       - path of the vault within the file system.
        - `vault name`       - name of the vault within the file system.
        - `git url`          - Git Url of the Vault.
        - `git api key`      - Git Api Key of the Vault. 
        - `git username`     - The git username of the vault.
    """
    def __init__(self) -> None:
        """Initializes the Obsidian Vault Object with no aguments."""

        self.initialize_environment_variables()
        self.sync_vault()
        self.content = self.get_content()
        self.tags = self.get_tags()

        
    def get_tags(self) -> list: 
        """ Returns a list of tags from the vault present in all of the notes. """
        tags = []
        for note in self.content: 
            tags.extend(note.tags)
        return tags

    def initialize_environment_variables(self) -> None:
        """Initializes the environment variables for the Obsidian Vault Object."""

        if os.getenv("OBSIDIAN_GITHUB_API_KEY"):
            self.git_api_key = os.getenv("OBSIDIAN_GITHUB_API_KEY")
        else: 
            assert False, "Please set the OBSIDIAN_GITHUB_API_KEY environment variable in the .env file."
        if os.getenv("OBSIDIAN_VAULT_GIT_URL"):
            # Initialize the Vault Object with the a Git URL used to house the vault.
            self.git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        else: 
            assert False, "Please set the OBSIDIAN_VAULT_GIT_URL environment variable in the .env file." 
        if os.getenv("OBSIDIAN_GITHUB_USERNAME"):
            # Initialize the Vault Object with the Git Username used by the repository owner to house the vault. 
            self.git_username = os.getenv("OBSIDIAN_GIT_USERNAME")
        else: 
            assert False, "Please set the OBSIDIAN_GIT_USERNAME environment variable in the .env file." 
        if os.getenv("OBSIDIAN_VAULT_NAME"): 
            # Initialize the Vault Object with the name of the vault. 
            self.vault_name = os.getenv("OBSIDIAN_VAULT_NAME") 
            self.vault_directory = f"{os.path.expanduser('~')}autogpt{os.path.sep}auto_gpt_workspace{os.path.sep}{self.vault_name}"
        else:
            self.vault_name = "autogpt-vault-unspecified vault name"
            assert False, "Please set the OBSIDIAN_VAULT_NAME environment variable in the .env file."
        if os.getenv("OBSIDIAN_GITHUB_API_KEY"): 
            # Initialize the Vault Object with the Git API Key used to house the vault.
            self.git_api_key = os.getenv("OBSIDIAN_GITHUB_API_KEY")
        else: 
            assert False, "Please set the OBSIDIAN_GITHUB_API_KEY environment variable in the .env file."

    def clone_vault(self) -> str:
        """ Clones the vault from the git url into the workspace. """
        os.makedirs(self.vault_directory , exist_ok=True)
        try:
            Repo.clone_from(self.git_url, working_directory)
            return f"""Cloned {self.git_url} to {working_directory}"""
        except Exception as e: 
            return f"Error: {str(e)}"

    def search_vault_title(self, title: str) -> dict:
        """ 
        Searches the Obsidian Vault for a note with a given title.
        
        Parameters: 
            - title: the title to search for inside of the vault.
        """

    def get_content(self):
        """
        Reteives the Obsidian Objects pesent within the vault
        """
        dir = self.vault_directory
        # Get all of the files in the vault directory. 
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        notes = []
        for file in files: 
            if file.endswith(".md"):
                file_path = os.path.join(dir, file)
                file_path = file_path.replace(self.vault_directory, "") 
                notes.extend( Obsidian_Note( os.path.join(self.vault_directory, file_path) ) )
            return notes

    def sync_vault(self) -> bool: 
        """ 
        Sync the Obsidian Vault within the workspace with the remote Git repository.
        If there is a vault in the workspace, then it syncs the vault with the remote 
        Git repository. If not, then it clones the remote Git repository into the workspace.

        Returns: 
            - boolean as the result of the sync operation.
        """
        git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        git_api_key = os.getenv("OBSIDIAN-GITHUB_API_KEY")
        git_username = os.getenv("OBSIDIAN-GITHUB_USERNAME")
        split_url = git_url.split("//")
        auth_repo_url = f"//{git_username}:{git_api_key}@".join(split_url)
        # Create a repo object for the vault directory.
        repo = Repo(self.vault_directory)

        def add_all_commit_push() ->bool:
            try:
                repo.git.add(update=True) 
                repo.git.commit("-m", "Auto-commit from AutoGPT") 
                origin = repo.remote(name="origin")
                origin.push() 
                
                return True 
            except Exception as e: 
                print(e)
                return False

        # There are changes in the remote repository, then pull the latest changes from the remote repository.
        if repo.head.commit != origin.fetch()[0].commit: 
            repo.git.pull()
            add_all_commit_push()

        # If there are changes in repo
        if repo.is_dirty():
            try:
                add_all_commit_push()
                print(f""" Pushed changes to {git_url} """)
                return True 
                
            except Exception as exception:
                print( f""" Exception while pushing changes to {git_url}: {exception} """)
                return False 

    def create_note(note_path: str) -> Obsidian_Note: 
        """ 
        Creates a note at the given path. 
        """
        note = Obsidian_Note(note_path)
        return note
        
    def get_tags_generalability(self) -> int:
        """
        Returns the number of propotion of tags that are generalizable. 
        """


