# AppMan
AppMan is a free, open source package manager for AppImages, making it easier to install, upgrade, and remove AppImages systemwide or locally.

## Features
- [x] Easy installation
- [x] Lightweight

## Installation
AppMan is available on all GNU/Linux distributions. They can be found in their respective official repositories. If you wish to download from source then do the following in the directory you wish to download the source to:
```
git clone --depth=1 https://github.com/AppImage/AppMan.git
cd AppMan
python3 setup.py install
```

Alternatively you could clone the repository and then create a directory called `bin_scripts` and create a file called `appman` with the following contents:
```
#!/bin/bash
venv_python=[[PATH]]
$venv_python appman.py "$@"
```
Note that you should create a virtual environment for appman.

After creating this you can symlink the `bin_scripts/appman` to `$HOME/.local/bin`, make sure to give it executable permissions.

## Uninstallation
You can uninstall AppMan with your package manager. If you installed it through the source, then uninstall it with:
```
python3 setup.py uninstall
```

Uninstalling AppMan using the `bin_scripts` requires the following steps:
- Remove the virtual environment
- Remove the `bin_scripts/appman` file

## Usage

## [Liscense](./LICENSE)
```
AppMan is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License

Pacstall is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pacstall. If not, see <https://www.gnu.org/licenses/>.
```
