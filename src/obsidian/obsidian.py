"""
Import the `os` module to access the environment variables from the `.env` file.
"""
import os

""" 
Import the TextIO type from the `typing` module to use as a type hint for the 
"""
from typing import TextIO

"""
Import the `guidance` module to access microsoft guidance a way to inference language models.
"""
import guidance

""" 
Import repo from GitPython for syncing the vault with the remote repository. 
""" 
from git import Repo

"""
Obsidian Integrations for Auto-GPT using custom API functions and obsidiantools.
"""
def _get_valid_tags() -> list: 
    """ 
    Retrieves a list of valid tags from the vault. 

    Returns: a list of valid tags used within the vault.
    """ 
    # Set guidance's OpenAI Model to "text-davinci-003"
    guidance.llm = guidance.llms.OpenAI("text-davinci-003")

    vault_path = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])

    # Create a list of valid tags from the vault
    valid_tags = []

    # Iterate through the vault to find all tags
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f.readlines():
                        if line.startswith("tags:"):
                            for tag in line.split(":")[1].split(","):
                                valid_tags.append(tag.strip())
    # Additionally, Obsidian allows for tags to be defined as #tags, so we will add those to the list of valid tags. 
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f.readlines():
                        for word in line.split(" "):
                            if word.startswith("#"):
                                valid_tags.append(word.strip())

    return valid_tags

def _create_notes(titles[]: str, contents[]: str) -> list:
    """
    Creates a list of notes inside the vault with titles, contents, tags, types,  and summaries using the _create_note function.

    Returns: a list of strings containing the result of each _create_note function call. 
    """
    responses = []

    for title in titles:
        for content in contents:
            responses += _create_note(title, content)
            
    return responses

def _create_note(title: str, content: str) -> str:
    """
    Create a note inside the vault with a title, content, tags, type,  and a summary.

    Parameters:
        - title: The title of the note. In other words, the title 
        is the name of the note. The title is also the name of the file to be produced.

        - content: the content of the note to be written in Markdown. In other words, the content of a note is the text to be placed in the main body of the note excluding the frontmatter. 
    Returns:
        - the created note content.

    """
    # Sync the vault to most recent changes

    _sync_vault()
    
    # Set guidance's OpenAI Model to "text-davinci-003"
    guidance.llm = guidance.llms.OpenAI("text-davinci-003")

    vault_path = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])

    # Create a new note with the title and content
    note = open(os.path.join(vault_path, title + ".md"), "w") 

    current_date = datetime.datetime.now()

    # Create a valid tags list file in the workspace
    valid_tags_file = open(os.path.join(current_working_directory, "valid_tags.txt"), "w")

    valid_tags  = [_get_valid_tags()]

    create_note_program = guidance('''
    {{#system~}}
    You are a writer. You are writing a note. The note is about {title}. The note is about {gen 'type'}. 
    The note has the following {content} a parameter to this function. The note was created on {date}. 
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

def _create_note_flashcards(title: str) -> str | None:
    """
    Create a note containing spaced-repetition styled flashcards 
    inside the vault with a title, content, tags, and a summary.
    The title of the note from which flashcards are being generated
    + "Flashcards" + number of flashcards for that note in the vault 
    that were found to be in the vault to avoid name collisions.
    """
    
    _sync_vault()
    
    # Set guidance's OpenAI Model to "text-davinci-003"
    guidance.llm = guidance.llms.OpenAI("text-davinci-003")

    create_flashcards = guidance('''

    A conversation with an AI for use in Obsidian. \n 

    You are an AI that is helping write flashcards for the purpose of spaced repitition. 
    Flashcards should have the following format: 
    '<question>
    ?
    <answer>'. 

    Here is an example flashcard:
    ${exampleFlashcard}
    Do NOT number the flashcards. Make sure each question you as is atomic, so that it only asks one thing, i.e. avoids the use of 'and'. You do not need to write flashcards on everything in the document, just start with the most important. You will be a writing it on the subject matter of:'${title}.''')

    # Create a list of flashcards from the user's input
    executed_program = program( 



     )
    vault_path = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])

    // Get the document text 
    documentText = await getDocumentText(documentPath);

     // Remove the front matter
    const cleanedText = removeFrontMatter(documentText);
    // Surround the text with markdown
    const markdownText = surroundWithMarkdown(cleanedText);


def _sync_vault() -> str:
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
            return f"""Cloned {git_url} to {working_directory}"""
        except Exception as e: 
            return f"""Error cloning {git_url} to {working_directory}: {e}"""
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
