"""Tests for Adobe Reader for Windows toolkit"""
import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


class TestToolkit:
    """Basic tests"""
    
    def test_import(self):
        """Test module imports"""
        from src import __version__
        assert __version__ == "0.1.0"
    
    def test_scan_files(self):
        """Test file scanning"""
        from src.utils import scan_files
        # Should not raise
        result = scan_files(".", ["*.py"])
        assert isinstance(result, list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
