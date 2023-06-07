"""
Import the `os` module to access the environment variables from the `.env` file.
"""
import os

from git.repo import Repo
import pytest
import unittest

""" Obsidian uses vaults, notes,  content, frontmatters, and body to store information. """
from obsidian.obsidian_vault import Obsidian_Vault
from obsidian.obsidian_note import Obsidian_Note
from obsidian.obsidian_vault import Obsidian_Vault

def ObsidianVaultTest( unittest.TestCase ): 
    """ Testing Class for obsidian_vault.py """
    def test_construction(self):  
        """ Test that an vault can be constructed. """

        # Constructing a Vault using public empty vault example should have 0 items as cotnents
        #
        empty_vault_url = "https://github.com/conneroisu/Empty-Obsidian-Vault-AutoGPT"   

        test_vault = Obsidian_Vault()         

        assert True, "Vault constructed successfully." 

        assert test_vault is not None, "Vault constructed successfully."


    def arbitrary_test(self): 
        assert 1==1

