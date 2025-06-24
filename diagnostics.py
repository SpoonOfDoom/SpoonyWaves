# SpoonyWaves Error Handler and System Check
# Checks system requirements and common issues

import os
import shutil
import subprocess
import sys
from pathlib import Path


def check_ffmpeg():
    """Check if FFmpeg is available"""
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return True, "FFmpeg is available"
        else:
            return False, "FFmpeg command failed"
    except FileNotFoundError:
        return False, "FFmpeg not found in PATH"
    except subprocess.TimeoutExpired:
        return False, "FFmpeg command timed out"
    except Exception as e:
        return False, f"Error checking FFmpeg: {e}"


def check_audio_file(file_path):
    """Check if audio file exists and is readable"""
    try:
        path = Path(file_path)
        if not path.exists():
            return False, f"File does not exist: {file_path}"

        if not path.is_file():
            return False, f"Path is not a file: {file_path}"

        # Check file size
        size = path.stat().st_size
        if size == 0:
            return False, f"File is empty: {file_path}"

        # Check if file is readable
        try:
            with open(file_path, "rb") as f:
                f.read(1024)  # Try to read first 1KB
            return True, f"File is accessible: {file_path}"
        except PermissionError:
            return False, f"Permission denied reading file: {file_path}"
        except Exception as e:
            return False, f"Error reading file: {e}"

    except Exception as e:
        return False, f"Error checking file: {e}"


def check_output_directory(file_path):
    """Check if output directory is writable"""
    try:
        output_dir = Path(file_path).parent

        # Check if directory exists
        if not output_dir.exists():
            return False, f"Output directory does not exist: {output_dir}"

        # Check if directory is writable
        test_file = output_dir / "test_write_permission.tmp"
        try:
            test_file.touch()
            test_file.unlink()
            return True, f"Output directory is writable: {output_dir}"
        except PermissionError:
            return False, f"No write permission to output directory: {output_dir}"
        except Exception as e:
            return False, f"Error testing output directory: {e}"

    except Exception as e:
        return False, f"Error checking output directory: {e}"


def system_diagnostics():
    """Run complete system diagnostics"""
    print("SpoonyWaves System Diagnostics")
    print("=" * 40)
    print()

    # Check Python version
    print(f"Python Version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print()

    # Check FFmpeg
    ffmpeg_ok, ffmpeg_msg = check_ffmpeg()
    print(f"FFmpeg Status: {'✓' if ffmpeg_ok else '✗'} {ffmpeg_msg}")

    if not ffmpeg_ok:
        print("  Possible solutions:")
        print("  - Install FFmpeg from https://ffmpeg.org/")
        print("  - Add FFmpeg to your system PATH")
        print("  - Use the standalone executable which bundles FFmpeg")

    print()

    # Check current directory permissions
    current_dir = Path.cwd()
    dir_ok, dir_msg = check_output_directory(current_dir / "test.tmp")
    print(f"Current Directory: {'✓' if dir_ok else '✗'} {dir_msg}")

    print()
    print("Diagnostics complete.")

    if not ffmpeg_ok:
        print("\nWARNING: FFmpeg issues detected. SpoonyWaves may not work properly.")
        return False

    return True


def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"Checking file: {file_path}")
        print()

        # Check the specific file
        file_ok, file_msg = check_audio_file(file_path)
        print(f"Input File: {'✓' if file_ok else '✗'} {file_msg}")

        if file_ok:
            dir_ok, dir_msg = check_output_directory(file_path)
            print(f"Output Directory: {'✓' if dir_ok else '✗'} {dir_msg}")

        print()

    # Run system diagnostics
    system_ok = system_diagnostics()

    if len(sys.argv) > 1 and system_ok:
        print("\nFile and system checks passed. SpoonyWaves should work with this file.")

    return 0 if system_ok else 1


if __name__ == "__main__":
    exit(main())
