import argparse
import os
from shutil import copy2, copytree

parser = argparse.ArgumentParser(description='Prepare Standalone Build.')

parser.add_argument('--ifa-install', help='ifa_install directory path')
parser.add_argument('--fw', help='framework directory path')
parser.add_argument('--gfx-prod', help='graphics product directory path')
parser.add_argument('--config', help='tracer config directory path')
parser.add_argument('--libs', help='libs dependencies file path')
parser.add_argument('--bins', help='binary dependencies file path')

args = parser.parse_args()
fw_lib_path = os.path.join(args.fw, 'lib')
fw_bin_path = os.path.join(args.fw, 'bin')
gfx_lib_path = os.path.join(args.gfx_prod, 'lib')
gfx_bin_path = os.path.join(args.gfx_prod, 'bin')
libs = []
bins = []


with open(args.libs, 'r') as f:
    libs = [line.strip() for line in f.readlines()]
with open(args.bins, 'r') as f:
    bins = [line.strip() for line in f.readlines()]

print(args)
for file_name in libs:
    if os.path.exists(os.path.join(fw_lib_path, file_name)):
        copy2(os.path.join(fw_lib_path, file_name), os.path.join(args.ifa_install, 'lib'))
    elif os.path.exists(os.path.join(gfx_lib_path, file_name)):
        copy2(os.path.join(gfx_lib_path, file_name), os.path.join(args.ifa_install, 'lib'))
    else:
        print('could not find library {}'.format(file_name))
        print('library is ignored')

for file_name in bins:
    if os.path.exists(os.path.join(fw_bin_path, file_name)):
        copy2(os.path.join(fw_bin_path, file_name), os.path.join(args.ifa_install, 'bin'))
    elif os.path.exists(os.path.join(gfx_bin_path, file_name)):
        copy2(os.path.join(gfx_bin_path, file_name), os.path.join(args.ifa_install, 'bin'))
    else:
        print('could not find binary {}'.format(file_name))
        print('binary is ignored')

if os.path.exists(args.config):
    copytree(args.config, os.path.join(args.ifa_install, 'config'))
else:
    print('could not add the config directory to the build')

print(libs)
print(bins)