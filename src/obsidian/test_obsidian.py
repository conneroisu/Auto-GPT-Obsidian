from unittest import TestCase, main
from obsidian import Obsidian
import json 
import random 

import pytest 
import os 

from functools import partial
from unittest.mock import mock_open, patch
import unittest

class Test_Obsidian(unittest.TestCase):

    @patch.dict( 
        os.environ, 
        { 
            "OBSIDIAN_FLASHCARD_DIRECTORY": "/flashcards",
        }
    )

    class Test_Obsidian_Vault(unittest.TestCase):
        """Test the Obsidian vault class."""

    def setUp(self):
        self.obsidian = Obsidian()

        
    def test_find_note_by_title(self):
        note = self.obsidian._find_note_by_title("My Note")
        self.assertIsNotNone(note)
        if note is None:
            return
        self.assertEqual(note.title, "My Note")

    def test_create_note(self):
        title = "New Note"
        content = "This is a new note."
        result = self.obsidian._create_note(title, content)
        self.assertIsNone(result)
        note = self.obsidian._find_note_by_title(title)
        self.assertIsNotNone(note)
        self.assertEqual(note.title, title)
        self.assertEqual(note.content, content)

    # Add more tests for other methods

if __name__ == '__main__':
    unittest.main()
