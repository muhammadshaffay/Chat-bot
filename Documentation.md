# ChatBot Documentation

### Installation Requirements
```python
pip install tensorflow==2.12.0
pip install transformers
pip install openfabric_pysdk==0.1.11
```

### Working
The main.py file includes 2 functions i.e. config and execute. The `config` function is responsible for loading the configuration settings required for the application to run properly. The `execute` function loads a pre-trained tokenizer and model for the Blenderbot chatbot. It processes each text input by encoding it, generating an answer using the model, and decoding the generated response. The answers are stored in the output list. If any errors occur, an error message is printed and an error response is added to the output. The function returns a SimpleText object containing the generated answers.

### About the Model
Blenderbot is an open-source chatbot developed by Facebook. It is trained on the _blended-skill-talk_ dataset and has a specific version called `facebook/blenderbot-400M-distill`.

Blenderbot is a powerful conversational AI model with 400 million parameters, allowing it to generate contextually relevant responses. The _distill_ in `facebook/blenderbot-400M-distill` refers to a refined version of the model. This distilled version aims to capture the knowledge and performance of the larger model while being more memory and computationally-efficient.

Reason for Choice <br>
The decision to use Blenderbot for this application is based on several factors. Firstly, the model's large parameter size gives it a rich understanding of conversations and generates high-quality responses. Additionally, the "distill" version balances model size and performance, making it suitable for various conversational applications. The choice of Blenderbot ensures that the chatbot can provide engaging and contextually appropriate responses to users.

### Execution Guidelines
1. Open your terminal and run the following command: python ./ignite.py
2. Open your web browser and navigate to http://localhost:5000/
3. Click on `swagger-ui` to access the Swagger user interface.
4. In the Swagger UI, navigate to `Execution` > `Post` > `Try it out`.
5. In the `Post`, add the messages to `string`: {"text": ["string"]}

### Execution Time
* Model Initialization: 15 minutes (First run)
* Response Generation: 40 seconds (Approximately)

### Conversation
| Question                                      | Answer                                       |
| --------------------------------------------- | -------------------------------------------- |
| What is Earth?            | It is our planet located in the middle of the Solar System |
| What is the primary source of light during the day?  | I think it's the sunlight, but I'm not really sure.  I know that the sun is the main source of the energy. |


### References
* https://huggingface.co/facebook/blenderbot-400M-distill
* https://arxiv.org/abs/2004.13637