import os
import json
import csv
from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass
import datetime


@dataclass
class FileInfo:
    name: str
    size: int
    modified_time: datetime.datetime


def scan_files(directory: str, extensions: List[str]) -> List[Path]:
    """Scan the given directory for files with specified extensions.

    Args:
        directory (str): The directory to scan.
        extensions (List[str]): A list of file extensions to look for.

    Returns:
        List[Path]: A list of Path objects for the found files.
    """
    try:
        dir_path = Path(directory)
        if not dir_path.is_dir():
            raise ValueError(f"The provided directory '{directory}' is not valid.")

        files = []
        for ext in extensions:
            files.extend(dir_path.glob(f"*.{ext}"))
        return files
    except Exception as e:
        print(f"Error scanning files: {e}")
        return []


def format_size(bytes: int) -> str:
    """Convert bytes to a human-readable format.

    Args:
        bytes (int): Size in bytes.

    Returns:
        str: Formatted size string.
    """
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024**2:
        return f"{bytes / 1024:.2f} KB"
    elif bytes < 1024**3:
        return f"{bytes / 1024**2:.2f} MB"
    else:
        return f"{bytes / 1024**3:.2f} GB"


def format_duration(seconds: int) -> str:
    """Format a duration in seconds to a human-readable string.

    Args:
        seconds (int): Duration in seconds.

    Returns:
        str: Formatted duration string.
    """
    if seconds < 60:
        return f"{seconds} seconds"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} minutes"
    else:
        hours = seconds // 3600
        return f"{hours} hours"


def export_json(data: Any, path: str) -> None:
    """Export data to a JSON file.

    Args:
        data (Any): Data to export.
        path (str): Path to the output JSON file.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error exporting to JSON: {e}")


def export_csv(data: List[Dict[str, Any]], path: str) -> None:
    """Export data to a CSV file.

    Args:
        data (List[Dict[str, Any]]): List of dictionaries to export.
        path (str): Path to the output CSV file.

    Raises:
        IOError: If the file cannot be written.
    """
    if not data:
        print("No data to export.")
        return

    try:
        with open(path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except IOError as e:
        print(f"Error exporting to CSV: {e}")


def get_file_info(path: str) -> FileInfo:
    """Get metadata information for a file.

    Args:
        path (str): Path to the file.

    Returns:
        FileInfo: A dataclass instance containing file metadata.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"The file '{path}' does not exist.")

        return FileInfo(
            name=file_path.name,
            size=file_path.stat().st_size,
            modified_time=datetime.datetime.fromtimestamp(file_path.stat().st_mtime)
        )
    except Exception as e:
        print(f"Error getting file info: {e}")
        raise
