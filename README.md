# Obsidian AutoGPT Plugin

<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br/>
<div align="center">
      <img src="docs/assets/logoautogptobsidian.png" alt="Logo" width="80" height="80">
<h3 align="center">Auto-GPT-Obsidian</h3>

  <p align="center">
    Power Auto-GPT with Your Obsidian Vault and Vise Versa!
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#use-cases">Use Cases</a> </li>
    <li><a href="#commands">Commands</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Introduction 
This plugin for [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) allows for robust interactions with Obsidian Markdown Elements/Sytax. Also, this plugin povides toolings for [Auto-GPT Agents](https://github.com/Significant-Gravitas/Auto-GPT) to create flashcards and featured notes programmatically. Additionally, povides various interfaces of the corresponding data elements from notes. 



## Features


#### Enable AutoGPT with guided generate ai to create automatically flashcards for studying. (similar to the [arcana plugin](https://github.com/evanaze/obsidian-asana-plugin), but automatically generated from your notes).
#### Automate the filling out of boing but potentially impotant metadata in notes in the vault.
#### Enable AutoGPT with commands to find and integrate unlinked or lost notes from your Obsidian Vault 
#### Enable AutoGPT with commands to house attached media files into a Folder Note similar to [Consistent Names](https://github.com/)
#### Provides various features that coinside with Obsidian Vault makdown standards and features 
#### Expand on or leave footnotes in you notes progrrammatically as autogpt or as commands from autogpt to futher discover an topic. 
#### Create notes in Obsidian with Auto-GPT automatically 
#### Create flashcards in Obsidian with Auto-GPT automatically with the [Spaced Repetition Plugin](https://github.com/st3v3nmw/obsidian-spaced-repetition) for [Obsidian MD](https://obsidian.md/). 
#### Use an (soon to be) Community Accepted Plugins for aiding in the syncing of your vault to this plugin, [git-gpt-sync](https://github.com/conneroisu/git-gpt-sync).  
#### Create notes in styled/templated markdown with Auto-GPT commands that feature guided generative ai programs. 


## Prerequisites

1. Install [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT), **checkout the [latest release v0.3.0](https://github.com/Significant-Gravitas/Auto-GPT/releases/tag/v0.3.0) which adds plugin support**, and make sure you can run it successfully.
2. Install extra dependencies for this plugin.

```terminal
pip install obsidiantools python-dotenv auto_gpt_plugin_template
```

## Getting Started

To download it directly from your Auto-GPT directory (Once finished and accepted), you can run this command on Linux or MacOS:

```bash
curl -L -o ./plugins/Auto-GPT-Obsidian.zip https://github.com/conneroisu/Auto-GPT-Obsidian/archive/refs/heads/master.zip
```

In PowerShell:
```pwsh
Invoke-WebRequest -Uri "https://github.com/conneroisu/Auto-GPT-Obsidian/archive/refs/heads/master.zip"     -OutFile "./plugins/Auto-GPT-Obsidian.zip"
```

#### Github Source Code Install

Either navigate to https://github.com/conneroisu/Auto-GPT-Obsidian/archive/refs/heads/master.zip or use the link below, and download the source code. Place the **ZIP** file under the `Auto-GPT/plugins/` directory inside of your working directory of `Auto-GPT`. More specifically, place the zip files into the directoy containing `__PUT_PLUGIN_ZIPS_HERE__`.

[Click Here](https://github.com/conneroisu/Auto-GPT-Obsidian/archive/refs/heads/master.zip) to download the source code as **ZIP**, and place the **ZIP** file under `Auto-GPT/plugins/`.

### Edit Environment

`Auto-GPT/.env`

1. Add this plugin to the `ALLOWLISTED_PLUGINS` variable in the `.env` file for Auto-GPT. More specifically, append `AutoGPTObsidian` to `ALLOWLISTED_PLUGINS` in the `.env` file.

```.env
ALLOWLISTED_PLUGINS=AutoGPTObsidian
```

2. Add the path to your Obsidian vault create a public or private github repository for your vault variable in the `.env` file for Auto-GPT. More specifically, append the path to your Obsidian vault to `OBSIDIAN_VAULT_PATH` in the `.env` file.

```.env
################################################################################
### Obsidian
################################################################################

## OBSIDIAN_VAULT_NAME - the name of the obsidian vault
## OBSIDIAN_VAULT_GIT_URL - the repository url (without .git) of the vault.
## OBSIDIAN_FLASHCARD_SUBDIRECTORY - the subdirectory in which to create flashcards with spaced repition format/syntax.
## OBSIDIAN_GITHUB_API_KEY - the API KEY to which responsibilities inside of the github repository ahave been allowed
## OBSIDIAN_GITHUB_USERNAME - the username of the account housing the github repository and key. 

OBSIDIAN_VAULT_NAME=Auto-GPT-Obsidian-Example-Vault
OBSIDIAN_VAULT_GIT_URL=https://github.com/conneroisu/Auto-GPT-Obsidian-Example-Vault
OBSIDIAN_FLASHCARD_SUBDIRECTORY=/internal/vault/path/
OBSIDIAN_GITHUB_API_KEY=<github_api_key/token>
OBSIDIAN_GITHUB_USERNAME=<github_username>
```

Run Auto-GPT and enjoy integrations of Auto-GPT with Obsidian!

### FAQ

If you encounter problems or have any ideas, feel free to open an issue or pull request.

- [Issues](https://github.com/conneroisu/Auto-GPT-Obsidian/issues)
- [Pull Requests](https://github.com/conneroisu/Auto-GPT-Obsidian/pulls)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contribution

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Run Tests

```terminal
pytest -vs
```

Contributors will be featured here with a link to their GitHub profile with accompanying social image.

[Conner Ohnesorge](https://connerohnesorge.mixa.site)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Commands (Working)

All of the commands below are operational as plugin commands meaning that an AutoGPT instance can call them when both AutoGPT and Obsidian plugin are installed correctly. The commands below are the commands that are currently implemented. More commands will be added in the future. If you have a suggestion for a command, please open an issue with the tag "enhancement". Additionally, if you have an issue with a command, please open an issue with the tag "bug". 

### create_note(title, aliases, tags, summary, content)

This command creates a note inside the vault with a title, content, tags, and a summary.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgements

- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) - The main project that this plugin is for
- [obsidian-tools](https://github.com/mfarragher/obsidiantools) - The python library that this plugin uses to interact with Obsidian Vaults.
- [Microsoft Guidance](https://github.com/microsoft/guidance) - Microsoft Python llm inferencing markup library. 
- [Arcana  Plugin for Obsidian](https://github.com/evanaze/obsidian-asana-plugin) - Inspiation to make flashcard system. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/conneroisu/Auto-GPT-Obsidian.svg?style=for-the-badge
[contributors-url]: https://github.com/conneroisu/Auto-GPT-Obsidian/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/conneroisu/Auto-GPT-Obsidian.svg?style=for-the-badge
[forks-url]: https://github.com/conneroisu/Auto-GPT-Obsidian/network/members
[stars-shield]: https://img.shields.io/github/stars/conneroisu/Auto-GPT-Obsidian.svg?style=for-the-badge
[stars-url]: https://github.com/conneroisu/Auto-GPT-Obsidian/stargazers
[issues-shield]: https://img.shields.io/github/issues/conneroisu/Auto-GPT-Obsidian.svg?style=for-the-badge
[issues-url]: https://github.com/conneroisu/Auto-GPT-Obsidian/issues
[license-shield]: https://img.shields.io/github/license/conneroisu/Auto-GPT-Obsidian.svg?style=for-the-badge
[license-url]: https://github.com/conneroisu/Auto-GPT-Obsidian/blob/master/LICENSE
