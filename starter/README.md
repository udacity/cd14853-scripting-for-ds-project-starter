# Automating Data Cleaning with Shell and Python

## Project Description

In this project, you will build a **multi-stage data automation pipeline** using the Unix shell and Python.

You will take a folder of messy JSON files, organize them, validate their contents, clean and normalize the data, and finally merge everything into a single dataset ready for analysis or machine learning.

This project mirrors real-world data engineering workflows where automation, validation, and traceability are critical.

---

## Getting Started

These instructions will help you run the project locally using the provided starter files.

### Prerequisites

You should already be comfortable with:
- Basic Python programming
- Running commands in a Unix shell (Linux or macOS)

> ⚠️ This project is designed for **Unix-based shells** (Linux/macOS).  
> Windows Command Prompt and PowerShell are not supported.

---

### Dependencies

Python 3.8+
pandas

Shell scripts rely only on standard Unix utilities.

### Installation

1.	Clone or download the project starter repository.
2.	Open a terminal and navigate into the project directory.
3.	Install Python dependencies: `pip3 install pandas` (**Only if the pandas is not already installed on the env**)
4.  Make shell scripts executable: `chmod +x *.sh`

## Testing

This project does not include automated unit tests.

Instead, correctness is verified by running the pipeline and inspecting the outputs produced at each stage.

### Break Down Tests

You should manually verify that:

- Files are moved from json_dump/ to raw/ with cleaned filenames
-	Invalid JSON files are routed to the invalid/ folder
-	Cleaned JSON files are written to the clean/ folder
-	Original processed files are moved to the archive/ folder from clean/ folder after processing
-	A final CSV dataset is created in the dataset/ folder
-	Log files are written to the logs/ folder with filename as current date

These checks reflect how many real-world data pipelines are validated in practice.

## Project Instructions

You are expected to complete the following deliverables:

1.	Filename Organization
    -   Implement logic in organize_files.sh to normalize filenames and move files into the raw/ folder.
2.	Validation and Routing
    -	Implement validate_json.py to determine whether a JSON file is valid.
    -	Implement validate_and_route.sh to:
    -	Validate files in raw/
    -	Move invalid files to invalid/
    -	Track valid files in valid_files.txt
3.	Data Cleaning
    -	Implement process_jsons.py to:
    -	Normalize different JSON structures into a consistent format
    -	Write cleaned JSON files to the clean/ folder
    -	Archive original files after successful processing
4.	Dataset Creation
    -	Implement merge_to_dataset.py to:
    -	Read all cleaned JSON files
    -	Merge them into a single CSV dataset using pandas
    -	Save the dataset to the dataset/ folder
5.	Pipeline Execution
    -	Implement run_pipeline.sh so the entire pipeline can be executed with a single command.

⚠️ Do not manually move files between folders.
All file movement must be done through scripts.


## Project Folder Structure and Pipeline Phases

-	json_dump/ — Phase 0: Incoming data
Raw input files as received. Filenames and data may be inconsistent.
-	raw/ — Phase 1: Organized files
Files after filename normalization. Contents are unchanged.
-	invalid/ — Phase 2: Rejected data
Files that failed validation and are excluded from processing.
-	clean/ — Phase 3: Normalized data
Files with standardized and consistent structure.
-	archive/ — Phase 4: Archived originals
Original files that were successfully processed and archived.
-	dataset/ — Phase 5: Final dataset
Aggregated dataset ready for analysis or machine learning.
-	logs/ — Cross-cutting: Pipeline logs
Execution logs for all pipeline steps.

## Built With

-	Python￼ – Core scripting language for validation and processing
-	pandas￼ – Used to merge cleaned data into a final dataset
-	Bash￼ – Used for file automation and orchestration
-	Unix shell utilities – Standard tools for file navigation and scripting

Include all items used to build project.

## License

[License](../LICENSE.txt)
