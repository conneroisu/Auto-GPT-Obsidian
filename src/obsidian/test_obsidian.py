"""
Import the `os` module to access the environment variables from the `.env` file.
"""
import os

from git.repo import Repo
import pytest
import unittest

def ObsidianVaultTest(unittest.TestCase): 
    """ 
    Testing Class for obsidian_vault.py
    """
    def test_construction_empty(self):  
        # Constructing a Vault using public empty vault example should have 0 items as cotnents
        empty_vault_url = "https://github.com/conneroisu/Empty-Obsidian-Vault-AutoGPT"   
        empty_vault = ObsidianVault(empty_vault_url)         
        assert len(empty_vault.contents) == 0

    def test_clone_empty(self):
        # Constructing a Vault using public empty vault example should have 0 items as cotnents
        empty_vault_url = "https://github.com/conneroisu/Empty-Obsidian-Vault-AutoGPT"

        # The vault should be cloned into the workspace of autoGPT 
        empty_vault = ObsidianVault(empty_vault_url)
        #
        # Assert that the vault is cloned into the workspace as Empty-Obsidian-Vault-AutoGPT
        assert os.path.exists("Empty-Obsidian-Vault-AutoGPT")
    def arbitrary_test(self): 
        assert 1==1

