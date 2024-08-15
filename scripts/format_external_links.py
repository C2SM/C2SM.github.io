import os
import re
import argparse

def modify_link(line):
    # Define patterns for general and download links
    general_pattern = r'\[([^\]]+)\]\((http[s]?://[^\s\)]+)\)'
    download_pattern = r'\[([^\]]+)\]\((https://polybox\.ethz\.ch/index\.php/s/[^\s\)]+)\)'

    # Define replacements for general and download links
    icon_external_link = ':material-open-in-new:'
    icon_download = ':material-download:'
    open_new_tab = '{:target="_blank"}'
    general_replacement = r'[\1 ' + icon_external_link + r'](\2)'
    download_replacement = r'[\1 ' + icon_download + r'](\2)'

    # Check if the line was already modified or doesn't need modification
    if icon_external_link in line and open_new_tab in line:
        return line, False
    if icon_download in line and open_new_tab in line:
        return line, False

    # Check for link icon
    if icon_external_link not in line and icon_download not in line:
        if re.search(download_pattern, line):
            line = re.sub(download_pattern, download_replacement, line)
        else:
            line = re.sub(general_pattern, general_replacement, line)
        return line, True

    # Check for new tab attribute
    if open_new_tab not in line:
        line = re.sub(r'(\[.*?\]\(.*?\))', r'\1' + open_new_tab, line)
        return line, True

    # Apply the appropriate replacement based on the URL pattern
    if re.search(download_pattern, line):
        modified_line, num_subs = re.subn(download_pattern, download_replacement, line)
    else:
        modified_line, num_subs = re.subn(general_pattern, general_replacement, line)

    return modified_line, num_subs > 0


def process_markdown_file(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        modified = False
        for i, line in enumerate(lines):
            new_line, changed = modify_link(line)
            if changed:
                modified = True
                lines[i] = new_line
        if modified:
            file.seek(0)
            file.writelines(lines)
            file.truncate()
            print(f"Modified: {file_path}")


def main(start_path):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.md'):
                process_markdown_file(os.path.join(root, file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check markdown links in files.')
    parser.add_argument('-p', '--path', default=os.getcwd(), help='Base path to search for markdown files. Defaults to current working directory.')
    args = parser.parse_args()

    main(args.path) 
