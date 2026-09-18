import urllib.request
import json
import html
import random
import ast

def fetch_questions(amount):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    return data.get("results", [])

print("Fetching questions...")
results = fetch_questions(50)
import time
time.sleep(6)
results += fetch_questions(20)

new_questions = []
for item in results:
    question = html.unescape(item["question"])
    correct = html.unescape(item["correct_answer"])
    incorrect = [html.unescape(ans) for ans in item["incorrect_answers"]]
    
    all_options = incorrect + [correct]
    random.shuffle(all_options)
    
    labels = ["A", "B", "C", "D"]
    formatted_options = []
    answer_label = ""
    
    for i, opt in enumerate(all_options):
        formatted_options.append(f"{labels[i]}) {opt}")
        if opt == correct:
            answer_label = labels[i]
            
    new_questions.append({
        "question": question,
        "options": formatted_options,
        "answer": answer_label
    })

print(f"Fetched {len(new_questions)} questions.")

file_path = "miniKBC.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to find the end of the questions list.
# Let's use string manipulation: find the first occurrence of `]\n` or similar after the questions list,
# but it's safer to find the line with `lifelines = {` and insert before it.
# Actually, the questions list ends with `    }\n]`
# Let's just find the closing bracket of the questions list.

# Using AST to find the line number of the end of the questions list.
tree = ast.parse(content)
questions_node = next(n for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == 'questions')
last_element = questions_node.value.elts[-1]
end_lineno = last_element.end_lineno

lines = content.splitlines()

# The elements are up to end_lineno. The closing bracket is likely on the next line or same line.
# Let's find the closing bracket line:
bracket_line = end_lineno
while bracket_line < len(lines):
    if "]" in lines[bracket_line]:
        break
    bracket_line += 1

# Generate the string for new questions
questions_str = ",\n".join("    {\n        \"question\": " + json.dumps(q["question"]) + ",\n        \"options\": " + json.dumps(q["options"]) + ",\n        \"answer\": " + json.dumps(q["answer"]) + "\n    }" for q in new_questions)

# Insert it before the bracket
# we need to add a comma to the last existing element!
# find the last element's closing brace
last_brace_line = end_lineno - 1
while last_brace_line >= 0:
    if "}" in lines[last_brace_line]:
        lines[last_brace_line] = lines[last_brace_line].replace("}", "},")
        break
    last_brace_line -= 1

# Now insert the new questions string
lines.insert(bracket_line, questions_str)

with open(file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Questions successfully added to miniKBC.py")
