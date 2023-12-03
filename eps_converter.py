# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import subprocess
import platform
import shutil

__version__ = 'v1.0'
__doc__ = """
    Script Name: eps_converter.py
    Author: LiBao Feng
    Email: lbfeng23@gmail.com
    Description: This script converts EPS files to various formats using Ghostscript.
"""

# Device type mapping
devices = {
    'png': 'pngalpha',          # PNG format with transparency support
    'png16m': 'png16m',         # 16 million colors PNG format
    'pnggray': 'pnggray',       # Grayscale PNG format
    'pngmonod': 'pngmonod',     # Monochrome (black and white) PNG format
    'jpg': 'jpeg',              # JPEG format
    'jpeggray': 'jpeggray',     # Grayscale JPEG format
    'pdf': 'pdfwrite'           # PDF format
}


def find_ghostscript(custom_path: str = None):
    """
    Attempt to find the appropriate Ghostscript executable.
    If a custom path is provided, it uses that. Otherwise, it attempts to find
    'gswin64c', 'gswin32c' on Windows or 'gs' on other systems.

    :param custom_path: Optional custom path for the Ghostscript executable.
    :return: Path to the Ghostscript executable.
    :raises RuntimeError: If Ghostscript executable is not found.
    """
    if custom_path:
        return custom_path

    gs_names = ['gswin64c', 'gswin32c'] if platform.system() == 'Windows' else ['gs']
    for gs_name in gs_names:
        gs_path = shutil.which(gs_name)
        if gs_path:
            return gs_path
    raise RuntimeError('Ghostscript executable not found.')


def check_device_extension(output_file: str, device: str):
    """
    Check if the output file extension matches the device type.
    Validates whether the provided output file extension is compatible with the
    selected Ghostscript device type.

    :param output_file: The output file with extension.
    :param device: The selected device type.
    :raises ValueError: If the file extension doesn't match the device type.
    """
    output_ext = os.path.splitext(output_file)[1].lower()

    valid_extensions = {
        'png': ['.png'],
        'png16m': ['.png'],
        'pnggray': ['.png'],
        'pngmonod': ['.png'],
        'jpg': ['.jpg', '.jpeg'],
        'jpeggray': ['.jpg', '.jpeg'],
        'pdf': ['.pdf']
    }

    if device not in valid_extensions or output_ext not in valid_extensions[device]:
        raise ValueError(
            f"The output file extension '{output_ext}' does not match the selected device type '{device}'. "
            f"Expected extensions for device '{device}': {', '.join(valid_extensions[device])}.")


def convert_eps(input_eps: str, output_file: str, device_type: str, resolution: int, gs_path: str):
    """
    Convert an EPS file to another format using Ghostscript.
    The function constructs and executes a Ghostscript command based on the provided parameters.

    :param input_eps: Path to the input EPS file.
    :param output_file: Path for the output file, with desired extension.
    :param device_type: The Ghostscript device type for the output format.
    :param resolution: Resolution in DPI.
    :param gs_path: Path to the Ghostscript executable.
    :raises RuntimeError: If the Ghostscript command execution fails.
    """
    command = [
        gs_path,
        '-dNOPAUSE',
        '-dBATCH',
        f'-sDEVICE={device_type}',
        f'-r{resolution}',
        f'-sOutputFile={output_file}',
        input_eps
    ]

    try:
        subprocess.run(command, check=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8') if e.stderr else 'Unknown error'
        raise RuntimeError(f"Ghostscript failed with error: {error_msg}")


def main():
    """
    Main function to handle command line arguments and execute the EPS conversion process.
    Parses command line arguments, checks file extension compatibility, and performs the EPS conversion
    using the specified parameters.
    """
    parser = argparse.ArgumentParser(description='Convert EPS files to other formats using Ghostscript.',
                                     epilog='For more information and documentation, visit: https://github.com/Enthusiasm23')
    parser.add_argument('input_eps', type=str, help='The input EPS file.')
    parser.add_argument('output_file', type=str, help='The output file with extension (png, jpg, pdf).')
    parser.add_argument('-r', '--resolution', type=int, default=300, help='Resolution in DPI (default: 300).')
    parser.add_argument('-d', '--device', choices=devices.keys(), default='png',
                        help='Ghostscript device type. Choices are: ' + ', '.join(devices.keys()))
    parser.add_argument('--gs_path', type=str, help='Custom path to the Ghostscript executable.')
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args()

    gs_path = find_ghostscript(args.gs_path)
    check_device_extension(args.output_file, args.device)
    convert_eps(args.input_eps, args.output_file, devices[args.device], args.resolution, gs_path)


if __name__ == '__main__':
    main()
