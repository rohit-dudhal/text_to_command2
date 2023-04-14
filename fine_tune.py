import os
import openai
openai.api_key = "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"

# openai.api_key = os.getenv("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")
# file_created = openai.File.create(
#   file=open("text_json_prepared.jsonl", "rb"),
#   purpose='fine-tune'
# )
# print(file_created)
# # openai.File.delete("file-HsSXf0vsQ7cn7L8syAZ9SLr4")


# file_list = openai.File.list()
# print(file_list)

# fine_tune = openai.FineTune.create(training_file="file-9iYt9kis4lA07izJtdubLLie", model="davinci")
# print(fine_tune)

fine_tune_list = openai.FineTune.list()
print(fine_tune_list)