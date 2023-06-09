import os

from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict

from obsidian.obsidian_vault import Obsidian_Vault

from obsidian import _create_note

from auto_gpt_plugin_template import AutoGPTPluginTemplate

PromptGenerator = TypeVar("PromptGenerator")

class Message(TypedDict):
    role: str
    content: str


class AutoGPTObsidian(AutoGPTPluginTemplate):

    def __init__(self):
        super().__init__()
        self._name = "autogpt-obsidian"
        self._version = "0.1.0"
        self._description = "Obsidian Integrations for Auto-GPT using obsidiantools."
        self.vault = Obsidian_Vault() 
        if self.vault_path is None:
            print(
                "WARNING: The OBSIDIAN_VAULT_PATH environment variable is not set. Please set it to the path of the Obsidian vault wished to be interacted with."
            )

    def can_handle_on_response(self) -> bool:
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        pass

    def can_handle_post_prompt(self) -> bool:
        return True

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:

        prompt.add_command(
            "obsidian_create_note",
            "Create a new Obsidian note in the vault with a given title and content.",
            {
                "title": "<title>",
                "content": "<content>"
            },
            _create_note
        )
        prompt.add_command( 
            "obsidian_sync_vault", 
            "Sync the Obsidian Vault in the workspace with the remote vault.",
            {},
            _sync_vault
        )


        return prompt

    def can_handle_on_planning(self) -> bool:
        return False

    def on_planning(self, prompt: PromptGenerator, messages: List[Message]) -> Optional[str]:
        pass

    def can_handle_post_planning(self) -> bool:
        return False

    def post_planning(self, response: str) -> str:
        pass

    def can_handle_pre_instruction(self) -> bool:
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        pass

    def can_handle_on_instruction(self) -> bool:
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        pass

    def can_handle_post_instruction(self) -> bool:
        return False

    def post_instruction(self, response: str) -> str:
        pass

    def can_handle_pre_command(self) -> bool:
        return False

    def pre_command(
            self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        pass

    def can_handle_post_command(self) -> bool:
        return False

    def post_command(self, command_name: str, response: str) -> str:
        pass

    def can_handle_chat_completion(self, messages: Dict[Any, Any], model: str, temperature: float,
                                   max_tokens: int) -> bool:
        return False

    def handle_chat_completion(self, messages: List[Message], model: str, temperature: float, max_tokens: int) -> str:
        pass

    def can_handle_text_embedding(self, text: str) -> bool:
        return False

    def handle_text_embedding(self, text: str) -> list:
        pass

    def can_handle_user_input(self, user_input: str) -> bool:
        return False

    def user_input(self, user_input: str) -> str:
        pass

    def can_handle_report(self) -> bool:
        return False

    def report(self, message: str) -> None:
        pass
