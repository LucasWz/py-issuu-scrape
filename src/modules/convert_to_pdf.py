import subprocess


def convert_img_to_pdf(pages_files_pattern: str, out_file_path: str) -> None:
    params = ["convert", pages_files_pattern, out_file_path]
    subprocess.run(params)
