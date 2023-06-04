"""Git operatiuons for the Obsidian Vault Object"""
from typing import TYPE_CHECKING, List

from obsidian.obsidian_note import Obsidian_Note

"""
Import the OS module to operate using operating system of the operating computer.
"""
import os

from git.repo import Repo

import obsidian

class Obsidian_Vault: 
    """ 
    Vault Object allowing for interacttions with markdown notes with the syntax of Obsidian Makdown fo the AutoGPT plugin, AutoGPT-Obsidian.

    Vault Path - the path of the obsidian vault folder. When running inside of a docker container, the vault path is running on a Debian Linux OS. 
    """
    def __init__(self) -> None:
        git_url = os.getenv("OBSIDIAN_VAULT_GIT_URL") 
        current_working_directory = os.getcwd() 
        self.path = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])

    
    def get_tags(self) -> List:

    def search_vault_title(title: str) -> Obsidian_Note[]:
        """ 
        Searches the Obsidian Vault for a note with a given title.
        
        Parameters: 
            - title: the title to search for inside of the vault.
        """
        # For each file with a `.md` extension  as target:
            pass
        
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

        current_working_directory = os.getcwd() 
        working_directory = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])
       
        # if there is no vault in the workspace (checked usinging os.path.exists() with end of git url), then create one with git clone.
        if not os.path.exists(working_directory):
            try:
                Repo.clone_from(auth_repo_url, os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace"))
                return True
            except Exception as e: 
                print(e)
                return False
        else:
            # Create a repo object for the vault directory.
            repo = git.Repo(working_directory)

            def add_all_commit_push() -> Exception|None:
                try:
                    repo.git.add(update=True) 
                    repo.git.commit("-m", "Auto-commit from AutoGPT") 
                    origin = repo.remote(name="origin")
                    origin.push() 
                    return
                except Exception as e: 
                    return e

            # There are changes in the remote repository, then pull the latest changes from the remote repository.
            if repo.head.commit != origin.fetch()[0].commit: 
                repo.git.pull() 
                if not add_all_commit_push() as exception:
                    return f"""Exception while pushing changes to {git_url}: {exception}"""
                else:
                    return f"""Pulled latest changes from {git_url} to {working_directory} and pushed changes"""  

            # If there are changes in repo
            if repo.is_dirty():
                
                if not add_all_commit_push() as exception:
                    return f"""Exception while pushing changes to {git_url}: {exception}"""
                else:
                    return f"""Pushed changes to {git_url}"""
