from typing import TYPE_CHECKING, List

from obsidian.obsidian_note import Obsidian_Note

"""Used to operate using operating system of the operating computer."""
import os

"""Provides Git Operations for the Obsidian Vault Object"""
from git.repo import Repo

class Obsidian_Vault: 
    """
    Vault Object allowing for interactions with markdown notes specifically with the syntax 
    of Obsidian Markdown for the AutoGPT plugin, AutoGPT-Obsidian.

    This metaphorical obsidian vault class has a few native components on itself: 
        - `markdown content` - The Markdown Files in the vault.  
        - `vault path`       - The path of the vault within the file system.
        - `vault name`       - The name of the vault. 
        - `git url`          - The git url of the vault. 
        - `git api key`      - The git api key of the vault. 
        - `git username`     - The git username of the vault.
    """
    def __init__(self) -> None:
        """Initializes the Obsidian Vault Object."""
        # Retreive the env vars fo the obsidian plugin
        self.init_env_vars()
        self.sync_vault()
        self.path = None
        self.tags = None  
        self.vault_directory = os.sep.join([ os.path.expanduser("~"), "autogpt", "auto_gpt_workspace", self.vault_name ])

        
    def init_env_vars(self) -> None:
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
        else:
            self.vault_name = "autogpt-vault-unspecified vault name"
            assert False, "Please set the OBSIDIAN_VAULT_NAME environment variable in the .env file."

        if os.getenv("OBSIDIAN_GITHUB_API_KEY"): 
            # Initialize the Vault Object with the Git API Key used to house the vault.
            self.git_api_key = os.getenv("OBSIDIAN_GITHUB_API_KEY")
        else: 
            assert False, "Please set the OBSIDIAN_GITHUB_API_KEY environment variable in the .env file."

    def clone_vault(self) -> str:
        """Clones the vault from the git url into the workspace."""
        # Create the working directory
        working_directory = os.path.join(os.path.expanduser("~"), "autogpt"+ os.sep  +  "auto_gpt_workspace" + os.sep +  self.vault_name)
        os.makedirs(working_directory, exist_ok=True)
        try: 
            Repo.clone_from(self.git_url, working_directory)
            return f"""Cloned {self.git_url} to {working_directory}"""
        except Exception as e: 
            return f"Error: {str(e)}"

    def search_vault_title(self, title: str):
        """ 
        Searches the Obsidian Vault for a note with a given title.
        
        Parameters: 
            - title: the title to search for inside of the vault.
        """
        pass 
        # For each file with a `.md` extension  as target:
        # for ob_note in self.markdown_content: 
        # List result = 
        for note in content:

    def sync_vault(self) -> bool: 
        """ 
        Sync the Obsidian Vault within the workspace with the remote Git repository.
        If there is a vault in the workspace, then it syncs the vault with the remote 
        Git repository. If not, then it clones the remote Git repository into the workspace.

        Returns: 
            - the result of the sync operation.
        """
        git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        git_api_key = os.getenv("OBSIDIAN-GITHUB_API_KEY")
        git_username = os.getenv("OBSIDIAN-GITHUB_USERNAME")
        split_url = git_url.split("//")
        auth_repo_url = f"//{git_username}:{git_api_key}@".join(split_url)
        # Create a repo object for the vault directory.
        repo = Repo(self.vault_directory))

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
            if(add_all_commit_push()): 
                
                print( f"""Exception while pushing changes to {git_url}: {exception}""")
                return False 
            else:
                print(f"""Pushed changes to {git_url}""")
                return True 
