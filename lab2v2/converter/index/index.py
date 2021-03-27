#!/usr/bin/python3

import argparse
import os

import sys
sys.path.append('..')

from createParser.createParcer import CreateSerializator, CreateDeserializator


def main():
  def check_ext(orig, conv):
    # print(conv)
    if orig == conv:
      exit()

    if conv == '.json':
      conv = 'JSON'
    elif conv == '.yaml' or \
      conv == '.yml':
      conv = 'YAML'
    elif conv == '.toml':
      conv = 'TOML'
    elif conv == '.pickle' or \
      conv == '.pcl':
      conv = 'PICKLE'
    else:
      parser.error(conv + ' unsupported extension')

    if orig == '.json':
      orig = 'JSON'
    elif orig == '.yaml' or \
      orig == '.yml':
      orig = 'YAML'
    elif orig == '.toml':
      orig = 'TOML'
    elif orig == '.pickle' or \
      orig == '.pcl':
      orig = 'PICKLE'
    else:
      parser.error(orig + ' unsupported extension')

    return (orig, conv)

  def prepare(args):
    serializer = CreateSerializator()
    deserializer = CreateDeserializator()

    if args.config is None:
      file1 = args.file[0]
      file2 = args.file[1]
      # print(file1, file2)

      if os.path.isfile(args.file[0]):
        name1 = os.path.basename(args.file[0])
        orig_ext = os.path.splitext(name1)[1]
        name1 = os.path.splitext(name1)[0]
        # print(orig_ext)

      else:
        parser.error(str(args.file[0]) + ' not exist')

      name2 = os.path.basename(args.file[1])
      conv_ext = os.path.splitext(name2)[1]

      if conv_ext == '':
        conv_ext = name2
        file2 = os.path.abspath(name1 + f'conv{conv_ext}')
        # print(file1, file2)

      orig_ext, conv_ext = check_ext(orig_ext, conv_ext)

      obj = deserializer.deserialize(file1, format=orig_ext, file_mode=True)

      print(obj)
      serializer.serialize(obj, format=conv_ext, file_path=file2)

    else:
      file = args.config[0]

      if os.path.isfile(file):
        name1 = os.path.basename(file)
        orig = os.path.splitext(name1)[1]

        if orig == '.json':
          orig = 'JSON'
        elif orig == '.yaml' or \
          orig == '.yml':
          orig = 'YAML'
        elif orig == '.toml':
          orig = 'TOML'
        elif orig == '.pickle' or \
          orig == '.pcl':
          orig = 'PICKLE'
        else:
          parser.error(orig + ' unsupported extension')

        obj = deserializer.deserialize(file, format=orig, file_mode=True)

        if 'orig' in obj.keys():
          file1 = obj['orig']

        else:
          parser.error(f"doesn't find field orig in {file}")

        if 'conv' in obj.keys():
          file2 = obj['conv']

        else:
          parser.error(f"doesn't find field conv in {file}")

        #

        if os.path.isfile(file1):
          name1 = os.path.basename(file1)
          orig_ext = os.path.splitext(name1)[1]
          name1 = os.path.splitext(name1)[0]
          # print(orig_ext)

        else:
          parser.error(str(file1) + ' not exist')

        name2 = os.path.basename(file2)
        conv_ext = os.path.splitext(name2)[1]

        if conv_ext == '':
          conv_ext = name2
          file2 = os.path.abspath(name1 + f'conv{conv_ext}')
          # print(file1, file2)

        orig_ext, conv_ext = check_ext(orig_ext, conv_ext)

        obj = deserializer.deserialize(file1, format=orig_ext, file_mode=True)

        print(obj)
        serializer.serialize(obj, format=conv_ext, file_path=file2)


        #
      else:
        parser.error(file + ' not exist')
    # print(args)

  parser = argparse.ArgumentParser(
    description='Convertator',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog="convertator")
    # usage= "convertator [options] ./path1 [./path2]")

  group = parser.add_mutually_exclusive_group(required=True)

  group.add_argument("-f", "--file",
    const=None,
    nargs=2,
    type=os.path.abspath,
    help="--file ./path/to/original ./path/for/convertetion")

  group.add_argument("-c", "--config",
    nargs=1,
    const=None,
    type=os.path.abspath,
    help="--config ./config")

  # parser.add_argument("path1", type=str, 
  #   nargs=1
  #   help="path to original file")
  # parser.add_argument("path2", type=str,
  #   help="path to file for convertetion", 
  #   nargs='?',
  #   const=None)

  args = parser.parse_args()

  prepare(args)

