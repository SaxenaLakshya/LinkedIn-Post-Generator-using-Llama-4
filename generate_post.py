from llm_helper import llm
from few_shot import FewShotPosts


fs = FewShotPosts()
def get_length_str(length):
    if length == "Short":
        return "1 to 14 lines"
    if length == "Medium":
        return "14 to 24 lines"
    if length == "Long":
        return "24 to 30 lines"

def get_prompt(length, language, topic):
    length_str = get_length_str(length)
    prompt = f'''
        Generate a LinkedIn post using the below information. No preamble.
        1) Topic: {topic}
        2) Length: {length}
        3) Language: {language}
    '''
    examples = fs.get_filtered_post(length, language, topic)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\n Example {i + 1}: \n\n {post_text}"
            if i == 1:
                break
    prompt += "\n\nMake sure to add some emojies as well to make the post attractive."
    return prompt

def generate_post(length, language, topic):
    prompt = get_prompt(length, language, topic)
    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    post = generate_post("Short", "English", "ai")
    print(post)