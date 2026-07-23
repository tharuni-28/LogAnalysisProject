from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------- FILE UPLOAD & ANALYSIS ----------------
@app.route('/upload', methods=['POST'])
def upload():
    # 1. Get uploaded file
    file = request.files.get('logfile')
    if file is None or file.filename == '':
        return "No file selected"

    # 2. Read file content once
    content = file.read().decode('utf-8')
    lines = content.splitlines()

    total_lines = len(lines)

    # 3. Counters
    error_count = 0
    warning_count = 0
    info_count = 0

    # 4. Store log lines
    log_lines = []
    error_messages = []

    # 5. Process each line
    for line in lines:
        line_lower = line.lower()

        if 'error' in line_lower:
            error_count += 1
            error_messages.append(line.strip())
            log_lines.append({"type": "ERROR", "text": line})

        elif 'warning' in line_lower:
            warning_count += 1
            log_lines.append({"type": "WARNING", "text": line})

        else:
            info_count += 1
            log_lines.append({"type": "INFO", "text": line})

    # 6. Most common error
    most_common_error = "None"
    if error_messages:
        counter = Counter(error_messages)
        most_common_error = counter.most_common(1)[0][0]

    # 7. Error percentage
    error_percentage = 0
    if total_lines > 0:
        error_percentage = round((error_count / total_lines) * 100, 2)

    # 8. Send everything to result page
    return render_template(
        'result.html',
        total_lines=total_lines,
        error_count=error_count,
        warning_count=warning_count,
        info_count=info_count,
        error_percentage=error_percentage,
        most_common_error=most_common_error,
        log_lines=log_lines
    )

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
