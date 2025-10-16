import multitasking
from sentiment_analysis import score_paragraph



@multitasking.task
def score(chunk_data,index):
    out=score_paragraph(chunk_data)
    print("processing ==>" , index)
    return out

if __name__ == "__main__":
    with open("randomparas.txt") as f:
        huge_text = f.read()
        chunks = huge_text.split("\n")
        for i, chunk in enumerate(chunks):
            score(chunk,i)
    multitasking.wait_for_tasks()



# results = {}
#
# @multitasking.task
# def score(chunk_data, index):
#     out = score_paragraph(chunk_data)
#     results[index] = out
#     print(f"processing ===> {index} | score = {out}")
#
# if __name__ == "__main__":
#     with open("randomparas.txt", "r") as f:
#         huge_text = f.read()
#
#     chunks = huge_text.split("\n")
#
#     for i, chunk in enumerate(chunks):
#         score(chunk, i)
#
#     multitasking.wait_for_tasks()  # wait until all async tasks are done
#
#     # print("\nFinal Results:")
#     # for i in sorted(results):
#     #     print(f"Para {i}: {results[i]}")
