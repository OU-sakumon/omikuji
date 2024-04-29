def count_content_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    start = lines.index("\\begin{document}\n") + 1
    end = lines.index("\\end{document}\n")

    content_lines = lines[start:end]

    # Remove empty lines and comment lines
    content_lines = [line for line in content_lines if line.strip() and not line.strip().startswith('%')]

    return len(content_lines)

filename = 'ex.tex'  # replace with your filename
line_count = count_content_lines(filename)

if line_count < 7:
    print(f"{line_count}行あります。")
else:
    print(f"The content is not less than 7 lines. It has {line_count} lines.")
