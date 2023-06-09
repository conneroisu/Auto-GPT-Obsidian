from typing import TYPE_CHECKING, List

from obsidian.obsidian_note import Obsidian_Note
import guidance

import os

from git.repo import Repo

class Obsidian_Vault: 
    def __init__(self) -> None:
        self.initialize_environment_variables()
        self.sync_vault()
        self.path = None
        self.tags = None  
        self.vault_directory = os.sep.join([ os.path.expanduser("~"), "autogpt", "auto_gpt_workspace", self.vault_name ])
        self.content = self.get_vault_content()

        
    def initialize_environment_variables(self) -> Exception|None:
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
        working_directory = os.path.join(os.path.expanduser("~"), "autogpt"+ os.sep  +  "auto_gpt_workspace" + os.sep +  self.vault_name)
        os.makedirs(working_directory, exist_ok=True)
        try: 
            Repo.clone_from(self.git_url, working_directory)
            return None
        except Exception as e:
            return e

    def search_vault_title(self, title: str) -> Obsidian_Note|None:
        pass 
        for note in self.content:
            if note.title == title: 
                return note

        return None

    def sync_vault(self) -> Exception|None: 
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
        guidance.llm = guidance.llms.OpenAI("gpt4")

        self.sync_vault()

        valid_tags = []

        for root, [], files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as f:
                        for line in f.readlines():
                            if line.startswith("tags:"):
                                for tag in line.split(":")[0].split(","):
                                    valid_tags.append(tag.strip())

        for root, [], files in os.walk(self.vault_path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r") as f:
                        for line in f.readlines():
                            for word in line.split(" "):
                                if word.startswith("#"):
                                    valid_tags.append(word.strip())
        return valid_tags

    def get_vault_content(self) -> list:
            notes = []

            for root , [] , files in os.walk(self.vault_path):
                for file in files:
                    if file.endswith(".md"):
                        with open(os.path.join(root, file), "r"):
                            note = Obsidian_Note(self, note_path=os.path.join(root, file))
                            notes.append(note)
            return notes


