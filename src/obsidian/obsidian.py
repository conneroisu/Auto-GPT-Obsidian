"""
Import the `os` module to access the environment variables from the `.env` file.
"""
import os
from obsidian_note import Obsidian_Note
from obsidian_vault import Obsidian_Vault

"""
Import the `guidance` module to access microsoft guidance's python libraries allowing for more ways to inference language models.
"""
import guidance

"""
Import the datetime module for accurate date and time
"""
import datetime 

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

    # Sync the vault to most recent changes
    _sync_vault()
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

def _create_note(title: str, content: str) -> str:
    """
    Create a note inside the vault with a title, content, tags, type,  and a summary within the frontmatter of said note following the Obsidian format
    Parameters:
        - title: The title of the note. In other words, the title is the name of the note. The title is also the name of the file to be produced.

        - content: the content of the note to be written in Markdown. In other words, the content of a note is the text to be placed in the main body of the note excluding the frontmatter. 
    Returns:
        - the created note content.

    """
    # Sync the vault to most recent changes

    _sync_vault()
    
    # Set guidance's OpenAI Model to "text-davinci-003"
    guidance.llm = guidance.llms.OpenAI("text-davinci-003")

    vault_path = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])

    ## Handle Collisions  
    ## TODO Need to finish the Collisions Code here to 
    note = _find_note_by_title(title) 
    if not note is None: 
        # Handle Collision
        HandleCollision(note, title, content)
        
        
    
    if title.endswith(".md"): 
        title = title[:-3]
        title = title + ".md"

    # Create a new note with the title and content
    note = open(os.path.join(vault_path, title), "w") 


    current_date = datetime.datetime.now()
    # Create a valid tags list file in the workspace
    valid_tags_file = open(os.path.join(current_working_directory, "valid_tags.txt"), "w")

    valid_tags  = [_get_valid_tags()]

    create_note_program = guidance('''
    {{#system~}}
    You are a writer. You are writing a note. The note is about {title}. The note is about {gen 'type'}. 
    The note has the following {{content}} a parameter to this function. The note was created on {{current_date}}. 
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
        valid_tags = _get_valid_tags(),
        current_date = current_date
    } 

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
    executed_program = program(



     )
    vault_path = os.path.join(current_working_directory, "autogpt", "auto_gpt_workspace", git_url.split("/")[-1])

    // Get the document text 
    documentText = await _get_note_by_title(documentPath)



    return 


