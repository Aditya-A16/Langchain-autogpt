from apikey import apikey  
import openai

# Replace 'apikey' with your actual API key (if required)

openai.api_key = apikey 

def run_gpt3_query(prompt):
    try:
        # Call the OpenAI GPT-3 API to generate a response to the prompt
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens= 500)
        
        # Extract the generated text from the response
        generated_text = response['choices'][0]['text']
        
        return generated_text
    except Exception as e:
        print(f"Error: {e}")
        return None
    
title = input('enter title for your blog post: ')
print('\n')

# Example usage
#chain1
prompt_template1 = f"Give me a creative title for my blog post which is about{title}"
generated_text1 = run_gpt3_query(prompt_template1)
print("Here's a Suitable title: ", generated_text1)
print('\n')

#chain 2
prompt2 = f'create content for my blog post titled:{generated_text1}'
generated_text2 = run_gpt3_query(prompt2)
print('content : \n',generated_text2)



