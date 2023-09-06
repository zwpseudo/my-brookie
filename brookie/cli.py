import argparse
import inquirer

def cli(brookie):
  """
  Takes an instance of brookie.
  Modifies it according to command line flags, then runs chat.
  """

  # Setup CLI
  parser = argparse.ArgumentParser(description='Chat with My Brookie.')
  
  parser.add_argument('-y',
                      '--yes',
                      action='store_true',
                      help='execute code without user confirmation')
  parser.add_argument('-f',
                      '--fast',
                      action='store_true',
                      help='use gpt-3.5-turbo instead of gpt-4')
  parser.add_argument('-l',
                      '--local',
                      action='store_true',
                      help='run fully local with code-llama')
  parser.add_argument('-d',
                      '--debug',
                      action='store_true',
                      help='prints extra information')
  args = parser.parse_args()

  # Modify brookie according to command line flags
  if args.yes:
    brookie.auto_run = True
  if args.fast:
    brookie.model = "gpt-3.5-turbo"
  if args.local:
    brookie.local = True
  if args.debug:
    brookie.debug_mode = True

  # Run the chat method
  brookie.chat()
