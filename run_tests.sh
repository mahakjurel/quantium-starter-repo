#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate  # Windows (Git Bash/WSL)


# Run the test suite
pytest tests/test_app.py -v --disable-warnings

# Capture exit code
EXIT_CODE=$?

# Exit with 0 if tests passed, 1 if failed
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi

