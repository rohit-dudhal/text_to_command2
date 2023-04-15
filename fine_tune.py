import os
import openai
openai.api_key = "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"

# openai.api_key = os.getenv("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")
# file_created = openai.File.create(
#   file=open("prompt_update.jsonl", "rb"),
#   purpose='fine-tune'
# )
# print(file_created)
# # openai.File.delete("file-HsSXf0vsQ7cn7L8syAZ9SLr4")


# file_list = openai.File.list()
# print(file_list)

# fine_tune = openai.FineTune.create(training_file="file-tkcZqM2ibLtSiHOy0GgEncXd", model="davinci")
# print(fine_tune)

result = openai.FineTune.result("ft-8Zl58j2xtRP9ggPqFErNdyje")
print(result)

# fine_tune_list = openai.FineTune.list()
# print(fine_tune_list)