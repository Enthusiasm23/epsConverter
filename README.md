# EPS Converter Script

A versatile script for converting EPS files to various image formats using Ghostscript.

## Getting Started

### Prerequisites

- [Python](https://www.python.org)
- [Ghostscript](https://www.ghostscript.com)

### Installing Ghostscript

#### Windows

1. Download Ghostscript from [Ghostscript downloads page](https://www.ghostscript.com/download/gsdnld.html).
2. Install Ghostscript, and note the installation directory.
3. Add Ghostscript to your system's PATH:
   - Right-click on 'This PC' or 'My Computer'.
   - Click 'Properties' -> 'Advanced system settings'.
   - Click 'Environment Variables'.
   - Under 'System variables', find and select 'PATH', then click 'Edit'.
   - Click 'New' and add the path to the Ghostscript `bin` folder (e.g., `C:\Program Files\gs\gs10.02.1\bin`).
   - Click 'OK' to close all dialogs.

#### Linux

Typically, you can install Ghostscript using your distribution's package manager, for example:

- On `Ubuntu` or other `Debian` based systems, use the following command to install Ghostscript:

```bash
sudo apt-get install ghostscript
```

- On `CentOS` or other `Red Hat` based systems, use the following command to install Ghostscript:
```bash
sudo yum install ghostscript
```

Alternatively, you can download the latest version of Ghostscript from the official [GitHub releases page](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases).

### Script Installation

Clone the repository or download the script file directly from the GitHub repository.

- To clone the [`epsConverter`](https://github.com/Enthusiasm23/epsConverter.git) repository, use:

```bash
git clone https://github.com/Enthusiasm23/epsConverter.git
```

- Alternatively, to directly download the [`eps_converter.py`](./eps_converter.py), use:

```bash
wget https://raw.githubusercontent.com/Enthusiasm23/epsConverter/master/eps_converter.py
```

## Usage
Run the script from the command line, specifying the input EPS file, the output file with its desired format, and optionally the resolution and Ghostscript device type.

```bash
python eps_converter.py input.eps output.png -r 300 -d png
```

Alternatively, you can use Ghostscript directly for more complex operations.

```bash
gs -dNOPAUSE -dBATCH -sDEVICE=jpeg -r300 -sOutputFile=output.jpg input.eps
```
For more detailed usage and parameter adjustments, please refer to the [Ghostscript documentation](https://ghostscript.readthedocs.io/en/latest).

## Acknowledgements

This repository's script is a Python implementation of some functionalities provided by Ghostscript. 
It serves as a convenient interface, simplifying certain operations that Ghostscript enables. 
We express our heartfelt gratitude to [Ghostscript](https://www.ghostscript.com) for their robust and versatile software, which has been instrumental in the development of this script. 
Their work and dedication to the open-source community are greatly appreciated.

## License
[epsConverter](https://github.com/Enthusiasm23/epsConverter.git) is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
