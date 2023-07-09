import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time

# my imports
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # my code
    configuration.load()


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []

    # loading tokenizer and model
    tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
    model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

    for text in request.text:
        
        try:
            # answer generation (my code starts)

            # encode question
            inputs = tokenizer.encode_plus(text, padding=True, truncation=True, return_tensors="pt")                    # tokenize input

            # generate answer
            generated = model.generate(input_ids=inputs['input_ids'],
                                    attention_mask=inputs['attention_mask'], 
                                    num_beams=4,
                                    early_stopping=True,
                                    max_length=100,
                                    no_repeat_ngram_size=3,
                                    top_k=50,
                                    top_p=0.95,
                                    temperature=0.8)      
                       
            # decode answer
            response = tokenizer.decode(generated[0], skip_special_tokens=True) 

            # answer generation (my code ends)

            output.append(response)

        except Exception as e:
            # error handling
            print("ERROR : ", e)
            output.append("ERROR : Unable To Generate Answers!")

    return SimpleText(dict(text=output))