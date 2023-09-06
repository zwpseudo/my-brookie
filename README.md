<h1 align="center">● My Brookie</h1>


```shell
pip install my-brookie
```

```shell
brookie
```

<br>

**My Brookie** lets LLMs run code (Python, Javascript, Shell, and more) locally. You can chat with My Brookie through an interface in your terminal by running `$ brookie` after installing.

This provides a natural-language interface to your computer's general-purpose capabilities:

- Create and edit photos, videos, PDFs, etc.
- Control a Chrome browser to perform research
- Plot, clean, and analyze large datasets
- ...etc.

**⚠️ Note: You'll be asked to approve code before it's run.**

<br>

## Quick Start

```shell
pip install my-brookie
```

### Terminal

After installation, simply run `brookie`:

```shell
brookie
```

### Python

```python
import brookie

brookie.chat("Plot APPL and META's normalized stock prices") # Executes a single command
brookie.chat() # Starts an interactive chat
```


My Brookie overcomes limitations by running on your local environment. It has full access to the internet, isn't restricted by time or file size, and can utilize any package or library.

This combines the power of GPT-4's Code Interpreter with the flexibility of your local development environment.

## Commands

#### Interactive Chat

To start an interactive chat in your terminal, either run `brookie` from the command line:

```shell
brookie
```

Or `brookie.chat()` from a .py file:

```python
brookie.chat()
```

#### Programmatic Chat

For more precise control, you can pass messages directly to `.chat(message)`:

```python
brookie.chat("Add subtitles to all videos in /videos.")

# ... Streams output to your terminal, completes task ...

brookie.chat("These look great but can you make the subtitles bigger?")

# ...
```

#### Start a New Chat

In Python, My Brookie remembers conversation history. If you want to start fresh, you can reset it:

```python
brookie.reset()
```

#### Save and Restore Chats

`brookie.chat()` returns a List of messages when return_messages=True, which can be used to resume a conversation with `brookie.load(messages)`:

```python
messages = brookie.chat("My name is zwpseudo.", return_messages=True) # Save messages to 'messages'
brookie.reset() # Reset brookie ("zwpseudo" will be forgotten)

brookie.load(messages) # Resume chat from 'messages' ("zwpseudo" will be remembered)
```

#### Customize System Message

You can inspect and configure My Brookie's system message to extend its functionality, modify permissions, or give it more context.

```python
brookie.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""
print(brookie.system_message)
```

#### Change the Model

You can run `brookie` in local mode from the command line to use `Code Llama`:

```shell
brookie --local
```

For `gpt-3.5-turbo`, use fast mode:

```shell
brookie --fast
```

Or, in Python, set the model manually:

```python
brookie.model = "gpt-3.5-turbo"
```

## Safety Notice

Since generated code is executed in your local environment, it can interact with your files and system settings, potentially leading to unexpected outcomes like data loss or security risks.

**⚠️ My Brookie will ask for user confirmation before executing code.**

You can run `brookie -y` or set `brookie.auto_run = True` to bypass this confirmation, in which case:

- Be cautious when requesting commands that modify files or system settings.
- Watch My Brookie like a self-driving car, and be prepared to end the process by closing your terminal.
- Consider running My Brookie in a restricted environment like Google Colab or Replit. These environments are more isolated, reducing the risks associated with executing arbitrary code.

## How Does it Work?

My Brookie equips a [function-calling language model](https://platform.openai.com/docs/guides/gpt/function-calling) with an `exec()` function, which accepts a `language` (like "python" or "javascript") and `code` to run.

We then stream the model's messages, code, and your system's outputs to the terminal as Markdown.


**Note**: This software is not affiliated with OpenAI.
