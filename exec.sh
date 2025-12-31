#!/bin/bash
initial_setup="${initial_setup:-true}"
echo "Running initial setup..."
python3 -c "import readchar" 2>/dev/null 
if [[ "$?" -gt 0 ]]; then
  command -v pip >/dev/null 
  if [[ "$?" -gt 0 ]]; then
    echo "pip package manager is a prerequisite for bubbley.py. Install pip or set up python virtual environment with 'python3 -m venv venv' then 'source venv/bin/activate' (assuming unix-based OS), then re-run exec.sh"
  else
    pip install readchar
  fi
fi
echo "Initial setup complete ✅"
echo

echo "Running bubbley.py..."
python3 bubbley.py
