import brookie
brookie.auto_run = True
brookie.model = "gpt-3.5-turbo"
brookie.temperature = 0


def test_hello_world():
    brookie.reset()
    messages = brookie.chat("""Please reply with just the words "Hello, World!" and nothing else. Do not run code.""", return_messages=True)
    assert messages == [{'role': 'user', 'content': 'Please reply with just the words "Hello, World!" and nothing else. Do not run code.'}, {'role': 'assistant', 'content': 'Hello, World!'}]

def test_math():
    brookie.reset()
    messages = brookie.chat("""Please perform the calculation 27073*7397 then reply with just the integer answer with no commas or anything, nothing else.""", return_messages=True)
    assert "200258981" in messages[-1]["content"]

def test_delayed_exec():
    brookie.reset()
    brookie.chat("""Can you write a single block of code and run_code it that prints something, then delays 1 second, then prints something else? No talk just code. Thanks!""", return_messages=True)

def test_nested_loops_and_multiple_newlines():
    brookie.reset()
    brookie.chat("""Can you write a nested for loop in python and shell and run them? Also put 1-3 newlines between each line in the code. Thanks!""", return_messages=True)

def test_markdown():
    brookie.reset()
    brookie.chat("""Hi, can you test out a bunch of markdown features? Try writing a fenced code block, a table, headers, everything. DO NOT write the markdown inside a markdown code block, just write it raw.""")
