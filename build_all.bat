@echo off
REM Complete Build and Package Script for SpoonyWaves
REM Builds executable and creates Setup installer using InnoSetup

echo "SpoonyWaves Complete Build Process"
echo "=================================="
echo.

REM Check for required tools
echo "Checking build environment..."

REM Check Python and UV
where uv >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo "ERROR: UV package manager not found!"
    echo "Please install UV from: https://docs.astral.sh/uv/"
    pause
    exit /b 1
)

REM Check PyInstaller
uv run pyinstaller --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo "ERROR: PyInstaller not available!"
    echo "Please run: uv sync"
    pause
    exit /b 1
)

REM Check InnoSetup Compiler (ISCC)
where iscc >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo "ERROR: InnoSetup Compiler (ISCC) not found!"
    echo "Please install InnoSetup from: https://jrsoftware.org/isinfo.php"
    echo "Make sure ISCC.exe is in your PATH or install to default location"
    pause
    exit /b 1
)

echo.
echo "Step 1: Building executable..."
echo "=============================="

REM Clean previous builds
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"

REM Build the executable
uv run pyinstaller spoonywaves.spec
if %ERRORLEVEL% neq 0 (
    echo "ERROR: Executable build failed!"
    pause
    exit /b 1
)

echo "Executable built successfully!"

echo.
echo "Step 2: Building InnoSetup installer..."
echo "======================================="

REM Change to installer directory
cd installer

REM Compile the InnoSetup script
iscc InnoSetupScript.iss
if %ERRORLEVEL% neq 0 (
    echo "ERROR: InnoSetup compilation failed!"
    pause
    exit /b 1
)

cd ..

echo.
echo "Build Summary:"
echo "============="
if exist "dist\SpoonyWaves.exe" (
    echo "[OK] Executable: dist\SpoonyWaves.exe"
) else (
    echo "[FAIL] Executable not found"
)

if exist "installer\Output\SpoonyWavesSetup.exe" (
    echo "[OK] Setup installer: installer\Output\SpoonyWavesSetup.exe"
) else (
    echo "[FAIL] Setup installer not found"
)

echo.
echo "Installation:"
echo "Run installer\Output\SpoonyWavesSetup.exe to install SpoonyWaves"
echo.
echo "Build process complete!"
pause
