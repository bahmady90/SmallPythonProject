import json
with open("questions.json", "r") as file:
  content = file.read()


data = json.loads(content)


for question in data:
  print(question["question_text"])
  for index, alternative in enumerate(question["alternatives"]):
    print(index + 1, "-", alternative)
  user_choice = int(input("Enter your answer: "))
  correct_answer = question["correct_answer"]
  question["user_choice"] = user_choice

print(data)
score = 0

for index, question in enumerate(data):
  if question["user_choice"] == question["correct_answer"]:
    score = score + 1
    result = "Right answer"
  else:
    result = "Wrong answer"
  message = f"{index + 1} - Your answer: {question["user_choice"]}, " \
            f"Correct answer: {question["correct_answer"]}"
  print(message)


print(score, "/", len(data))


