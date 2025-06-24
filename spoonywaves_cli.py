#!/usr/bin/env python3
"""
SpoonyWaves CLI Entry Point
Standalone entry point for the SpoonyWaves executable with enhanced error handling
"""

import os
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        # Check if an input file was provided
        if len(sys.argv) < 2:
            print("Usage: SpoonyWaves.exe <input_file>")
            print("       SpoonyWaves.exe --diagnostics")
            print()
            print("SpoonyWaves - Audio Waveform Generator")
            print("=====================================")
            print()
            print("Generates waveform visualizations from audio files.")
            print()
            print("Supported formats: MP3, WAV, FLAC, M4A, AAC")
            print()
            print("Examples:")
            print('  SpoonyWaves.exe "C:\\Music\\song.mp3"')
            print('  SpoonyWaves.exe "audio_file.wav"')
            print("  SpoonyWaves.exe --diagnostics        # Run system diagnostics")
            print()
            print("The waveform video will be created in the same directory as the input file.")
            return 1

        # Handle special commands
        if sys.argv[1] in ["--diagnostics", "-d", "--help", "-h", "/?"]:
            if sys.argv[1] in ["--diagnostics", "-d"]:
                # Run diagnostics
                try:
                    import diagnostics

                    return diagnostics.main()
                except ImportError:
                    print("❌ Diagnostics module not available")
                    return 1
            else:
                # Show help (already shown above for no args)
                return 0

        input_file = sys.argv[1]

        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"ERROR: Input file not found: {input_file}")
            return 1

        # Import and call the main function
        from src.main import main as spoonywaves_main

        return spoonywaves_main()

    except ImportError as e:
        print(f"ERROR: Failed to import SpoonyWaves modules: {e}")
        print("This might be a packaging issue with the executable.")
        return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return 1
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        print("Please check that:")
        print("1. The input file is a valid audio file")
        print("2. You have write permissions to the output directory")
        print("3. FFmpeg is working properly")
        return 1


if __name__ == "__main__":
    sys.exit(main())
