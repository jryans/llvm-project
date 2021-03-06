#!/usr/bin/env python
#===----------------------------------------------------------------------===##
#
# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
#===----------------------------------------------------------------------===##

"""
Generate a linker script that links libc++ to the proper ABI library.
An example script for c++abi would look like "INPUT(libc++.so.1 -lc++abi)".
"""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dryrun", help="Don't write any output",
                        action="store_true", default=False)
    parser.add_argument("--rename", action="store_true", default=False,
                        help="Rename the output as input so we can replace it")
    parser.add_argument("--input", help="Path to libc++ library", required=True)
    parser.add_argument("--output", help="Path to libc++ linker script", required=True)
    parser.add_argument("libraries", nargs="+",
                        help="List of libraries libc++ depends on")
    args = parser.parse_args()

    # Prepare the list of public libraries to link.
    public_libs = ['-l%s' % l for l in args.libraries]

    # Generate the linker script contents.
    contents = "INPUT(%s)" % ' '.join([args.input] + public_libs)
    print("GENERATING SCRIPT: '%s' as file %s" % (contents, args.output))

    if args.dryrun:
        return 0

    # Remove the existing libc++ symlink if it exists.
    if os.path.islink(args.output):
        os.unlink(args.output)

    # Replace it with the linker script.
    with open(args.output, 'w') as f:
        f.write(contents + "\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
