# Spoony Waves

A wrapper around FFmpeg to create waveform visualizations from audio files with GPU acceleration support.
This serves a very specific personal use case, but may be useful for others as well.

## Features

- Generate 1080p waveform visualizations at 60fps
- GPU acceleration (CUDA) support for faster processing
- Windows context menu integration for easy access
- Command-line interface with enhanced error handling
- Standalone executable with bundled dependencies

## Requirements

### For Development

- Python 3.12 or higher
- FFmpeg with CUDA support (for GPU acceleration) or standard FFmpeg
- [UV](https://docs.astral.sh/uv/) package manager

### For End Users (Standalone Executable)

- Windows 7 or later
- NVIDIA GPU with CUDA support (optional, for faster processing)
- No additional software required (FFmpeg is bundled)

## Installation

### For Developers

1. Clone the repository
2. Install dependencies using UV:

```bash
uv sync
```

### For End Users

#### Option 1: Inno Setup Installer (Recommended)

1. Download `SpoonyWavesSetup.exe` from releases
2. Run the installer (may require administrator privileges)
3. Choose installation path and context menu integration options
4. Right-click any audio file and select "Generate Waveform with Spoony Waves"

#### Option 2: Portable Executable

1. Download `SpoonyWaves.exe` from releases
2. Place it in a permanent location
3. Use command line or create your own shortcuts

## Usage

### GUI Method (Recommended)

After installing with context menu integration:

1. Right-click any supported audio file
2. Select "Generate Waveform with Spoony Waves"
3. The waveform video will be created in the same directory

### Command Line

```bash
# Using UV to run the script (Development)
uv run python src/main.py <input_audio_file>

# Or using the console script entry point (Development)
uv run spoonywaves <input_audio_file>

# Using the standalone executable
SpoonyWaves.exe "path\to\audio\file.mp3"

# Run diagnostics to check system configuration
SpoonyWaves.exe --diagnostics
```

### Output

The waveform video is generated with the following specifications:

- **Resolution**: 1080p (1920x1080)
- **Frame Rate**: 60fps
- **Format**: MP4 with H.264 encoding
- **Waveform Style**: Peak-to-peak mode with white color
- **Audio**: Original audio is preserved in the output

## Building and Distribution

### Complete Build Process

```bash
# Build executable and create Inno Setup installer
build_all.bat
```

This script will:

1. Build the standalone executable using PyInstaller
2. Create an Inno Setup installer with context menu integration
3. Output `SpoonyWavesSetup.exe` in the `installer/Output/` directory

### Individual Build Steps

#### Executable Only

```bash
# Build the standalone executable
uv run pyinstaller spoonywaves.spec
```

The executable will be created in the `dist/` directory.

### Prerequisites for Building

- **PyInstaller**: Included in dependencies
- **Inno Setup**: Download from [jrsoftware.org](https://jrsoftware.org/isinfo.php)
- **FFmpeg**: Must be available in PATH for development

## System Diagnostics

The application includes built-in diagnostics to help troubleshoot issues:

```bash
# Run system diagnostics
SpoonyWaves.exe --diagnostics
```

This will check:

- FFmpeg availability and version
- CUDA support status
- Python environment (development mode)
- File permissions
- System requirements

## Examples

```bash
# Process an MP3 file
uv run spoonywaves "C:\Music\song.mp3"
# Creates: C:\Music\song.mp4

# Using the standalone executable
SpoonyWaves.exe "audio_file.wav"
# Creates: audio_file.mp4

# Check system configuration
SpoonyWaves.exe --diagnostics
```

## Development

### Running Tests

```bash
uv run pytest
```

### Adding Dependencies

```bash
# Add a runtime dependency
uv add <package_name>

# Add a development dependency
uv add --dev <package_name>
```

### Code Formatting

This project uses Ruff for code formatting and linting:

```bash
# Check code style
uv run ruff check

# Format code
uv run ruff format
```

## Technical Details

### Waveform Generation

The application uses FFmpeg with the following settings:

- **Mode**: Peak-to-peak (`p2p`) for maximum visual impact
- **Colors**: White waveform on transparent background
- **Draw Mode**: Full sample rendering for accuracy
- **Hardware Acceleration**: CUDA support when available (falls back to CPU)

### Dependencies

- **ffmpeg-python**: FFmpeg integration
- **PyInstaller**: Executable creation
- **toml**: Project file parsing

## Troubleshooting

### Common Issues

1. **"FFmpeg not found"**: Ensure FFmpeg is installed and in your PATH
2. **CUDA errors**: Update NVIDIA drivers or disable GPU acceleration
3. **Permission errors**: Run as administrator or check file permissions
4. **Large file processing**: Ensure sufficient disk space for output

### Getting Help

1. Run diagnostics: `SpoonyWaves.exe --diagnostics`
2. Check the console output for detailed error messages
3. Verify input file format is supported
4. Ensure write permissions to the output directory
