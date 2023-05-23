
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br/>
<div align="center">
      <img src="docs/logoautogptobsidian.png" alt="Logo" width="80" height="80">
<h3 align="center">Auto-GPT-Obsidian</h3>

  <p align="center">
    Power Auto-GPT with Obsidian!
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li> <a href="#getting-started">Getting Started</a> </li>
    <li><a href="#use-cases">Use Cases</a> </li>
    <li><a href="#commands">Commands</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# Features

- Create notes in Obsidian with Auto-GPT automatically (Fully Implemented)
- Create flashcards in Obsidian with Auto-GPT automatically 
- Create notes in styled/templated markdown with Auto-GPT automatically 

## Prerequisites

1. Install [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT), **checkout the [latest release v0.3.0](https://github.com/Significant-Gravitas/Auto-GPT/releases/tag/v0.3.0) which adds plugin support**, and make sure you can run it successfully.
2. Install extra dependencies for this plugin.

```terminal
pip install obsidiantools python-dotenv auto_gpt_plugin_template
```

## Getting Started

Make sure that you have completed the [prerequisites](#prerequisites) before continuing. Additionally, the RESTRICT_TO_WORKSPACE variable in the .env file for Auto-GPT must be set to False as seen below.

```
RESTRICT_TO_WORKSPACE=False
```

## Download

Thanks for considering to download the Auto-GPT-Obsidian Plugin. The best/recommended way to install is via the terminal, but below there are a few other ways to install the plugin. 

#### Terminal (Recommended)

To download it directly from your Auto-GPT directory, you can run this command on Linux or MacOS:

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

```
ALLOWLISTED_PLUGINS=AutoGPTObsidian
```

2. Add the path to your Obsidian vault to the `OBSIDIAN_VAULT_PATH` variable in the `.env` file for Auto-GPT. More specifically, append the path to your Obsidian vault to `OBSIDIAN_VAULT_PATH` in the `.env` file.

```
################################################################################
### Obsidian
################################################################################

OBSIDIAN_VAULT_PATH=/path/to/your/obsidian/vault
```

Run Auto-GPT and enjoy integrations of Auto-GPT with Obsidian!

### FAQ

If you encounter problems or have any ideas, feel free to open an issue or pull request.

- [issues](https://github.com/conneroisu/Auto-GPT-Obsidian/issues)
- [pull requests](https://github.com/conneroisu/Auto-GPT-Obsidian/pulls)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Use Cases

Ask Autogpt to create flashcards for studying automatically.

# Contribution

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Run Tests

```terminal
pytest -vs
```

Contributors will be featured here with a link to their GitHub profile with accompanying social image.

[Conner Ohnesorge](connerohnesorge.mixa.site)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Commands (Working)

All of the commands below are operational as plugin commands meaning that an AutoGPT instance can call them when both AutoGPT and Obsidian plugin are installed correctly. The commands below are the commands that are currently implemented. More commands will be added in the future. If you have a suggestion for a command, please open an issue with the tag "enhancement". Additionally, if you have an issue with a command, please open an issue with the tag "bug". 

### create_note(title, aliases, tags, summary, content)

This command creates a note inside the vault with a title, content, tags, and a summary.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgements

[Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) - The main project that this plugin is for
[obsidian-tools](https://github.com/mfarragher/obsidiantools) - The python library that this plugin uses to interact with Obsidian Vaults.

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
