# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

import pyinstaller_versionfile


def get_version():
    """Get the version from the pyproject.toml file."""
    try:
        from toml import load
    except ImportError:
        print("Please install 'toml' package to read version from pyproject.toml")
        sys.exit(1)

    toml_path = Path("./pyproject.toml")
    if not toml_path.exists():
        print(f"pyproject.toml not found at {toml_path}")
        sys.exit(1)

    with open(toml_path, "r", encoding="utf-8") as f:
        data = load(f)
    version = data["project"]["version"]
    return version


company_name = "Spoonforge"
general_name = "Spoony Waves"
file_description = general_name
internal_name = general_name
legal_copyright = "© Spoonforge. All rights reserved."
application_name = general_name.replace(" ", "")
exe_name = f"{application_name}.exe"
product_name = general_name

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=get_version(),
    company_name=company_name,
    file_description=file_description,
    internal_name=internal_name,
    legal_copyright=legal_copyright,
    original_filename=exe_name,
    product_name=product_name,
)

# Get the current directory where this spec file is located
current_dir = Path(SPECPATH)

a = Analysis(
    ["spoonywaves_cli.py"],
    pathex=[str(current_dir)],
    binaries=[],
    datas=[],
    hiddenimports=[
        "ffmpeg",
        "src.wavyfier",
        "src.main",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="SpoonyWaves",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="spoonywaves.ico",
    version="versionfile.txt",
)
