#!/usr/bin/env python3
"""
Test script to verify efinance-cli installation and basic functionality
"""

import subprocess
import sys

def run_command(cmd):
    """Run a command and return the result"""
    print(f"\n{'='*60}")
    print(f"Testing: {cmd}")
    print('='*60)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode == 0

def main():
    print("efinance-cli Installation and Functionality Test")
    print("="*60)

    # Test 1: Check if efinance-cli is installed
    success = run_command("efinance-cli --help")

    # Test 2: Show version
    success &= run_command("efinance-cli version")

    # Test 3: Stock commands
    print("\n" + "="*60)
    print("Testing Stock Commands")
    print("="*60)

    # Test stock history
    success &= run_command("efinance-cli stock history 600519 --limit 5")

    # Test stock realtime (limited output)
    success &= run_command("efinance-cli stock realtime --limit 5")

    # Test 4: Fund commands
    print("\n" + "="*60)
    print("Testing Fund Commands")
    print("="*60)

    # Test fund history
    success &= run_command("efinance-cli fund history 161725 --limit 5")

    # Test fund position
    success &= run_command("efinance-cli fund position 161725")

    # Test 5: Bond commands
    print("\n" + "="*60)
    print("Testing Bond Commands")
    print("="*60)

    # Test bond realtime
    success &= run_command("efinance-cli bond realtime --limit 5")

    # Test 6: Futures commands
    print("\n" + "="*60)
    print("Testing Futures Commands")
    print("="*60)

    # Test futures info
    success &= run_command("efinance-cli futures info --limit 5")

    # Final result
    print("\n" + "="*60)
    if success:
        print("✅ All tests passed!")
        print("="*60)
        return 0
    else:
        print("❌ Some tests failed!")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
