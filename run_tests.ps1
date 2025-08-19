# ---------------------------------------------
# run_tests.ps1
# Windows PowerShell script to run test_app.py
# ---------------------------------------------

# 1️⃣ Activate the virtual environment
# Adjust path if your venv folder is somewhere else
$venvPath = "..\venv\Scripts\Activate.ps1"
if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..."
    . $venvPath
} else {
    Write-Host "Virtual environment not found at $venvPath"
    exit 1
}

# 2️⃣ Run the test suite
Write-Host "Running tests..."
pytest tests/test_app.py -v --disable-warnings

# 3️⃣ Capture exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ All tests passed!"
    exit 0
} else {
    Write-Host "❌ Some tests failed."
    exit 1
}


