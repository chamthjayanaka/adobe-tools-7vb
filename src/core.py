import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Union


@dataclass
class AdobeReaderForWindowsProject:
    """Represents a project/file in Adobe Reader for Windows."""
    file_path: Path
    title: str
    author: str
    content: str

    def __post_init__(self):
        """Post-initialization to validate the file path."""
        if not self.file_path.exists() or not self.file_path.is_file():
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")


class AdobeReaderForWindowsParser:
    """Parser for Adobe Reader for Windows files."""

    @staticmethod
    def parse(file_path: Path) -> AdobeReaderForWindowsProject:
        """Parse an Adobe Reader for Windows file and return a project object.

        Args:
            file_path (Path): The path to the Adobe Reader file.

        Returns:
            AdobeReaderForWindowsProject: The parsed project.

        Raises:
            ValueError: If the file format is invalid or cannot be parsed.
        """
        if not file_path.suffix == '.pdf':
            raise ValueError("Invalid file format. Only .pdf files are supported.")

        # Simulating file reading and parsing
        try:
            with open(file_path, 'rb') as file:
                # Simplified parsing logic
                content = file.read(100).decode('utf-8', errors='ignore')
                title = "Sample Title"
                author = "Sample Author"
                return AdobeReaderForWindowsProject(file_path=file_path, title=title, author=author, content=content)
        except Exception as e:
            raise ValueError(f"Failed to parse the file {file_path}: {e}")


class AdobeReaderForWindowsExporter:
    """Exporter for Adobe Reader for Windows project data."""

    @staticmethod
    def export_to_json(project: AdobeReaderForWindowsProject, output_path: Path) -> None:
        """Export project data to a JSON file.

        Args:
            project (AdobeReaderForWindowsProject): The project to export.
            output_path (Path): The path where the JSON file will be saved.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(output_path, 'w') as json_file:
                json.dump(asdict(project), json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to {output_path}: {e}") from e


def main(file_path: str, output_path: str) -> None:
    """Main function to parse a PDF file and export its data to JSON.

    Args:
        file_path (str): The path to the input PDF file.
        output_path (str): The path to the output JSON file.
    """
    try:
        parser = AdobeReaderForWindowsParser()
        project = parser.parse(Path(file_path))
        exporter = AdobeReaderForWindowsExporter()
        exporter.export_to_json(project, Path(output_path))
        print(f"Successfully exported {project.title} to {output_path}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Adobe Reader for Windows Toolkit')
    parser.add_argument('file_path', type=str, help='Path to the Adobe Reader PDF file')
    parser.add_argument('output_path', type=str, help='Path to the output JSON file')
    args = parser.parse_args()

    main(args.file_path, args.output_path)
