#!/usr/bin/python3

import argparse
from resources.Check import Check, CheckSerialize, CheckDeserialize

parser = argparse.ArgumentParser(
  description='Serialize/Desirialize.',
  formatter_class=argparse.RawDescriptionHelpFormatter,
  prog="serializator",
  usage= "serializator [options] ./paths_to_obj [./path_to_file]")

parser.add_argument("-s", "--serialize", action="store_const", 
  const=CheckSerialize, default=CheckDeserialize, 
  help="serialize(without deserialize).")
parser.add_argument("-f", "--file", action="store_const", 
  const=True, default=False,
  help="write in the file.")

parser.add_argument("path_to_obj", type=str, 
  help="path to python object file")
parser.add_argument("path_to_file", type=str, nargs="?",
  help="path to file .json, .yaml, .toml or .pickle")

args = parser.parse_args()
# print(args)
Check(args)