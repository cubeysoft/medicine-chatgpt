# -*- coding: utf-8 -*-
"""
Created on Sat Sep 2 19:04:54 2023

@author: Nick Yan
"""


from langchain.chains import ConversationChain  
from langchain.memory import ConversationBufferMemory
  
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI()

#####################################################################
# Prompt Template load  
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate


template = """
You are a doctor with specialty in skin wellness. You have the following medical knowledge: Expertise in diagnosing and managing allergies and immunologic disorders. Knowledge of allergens and their effects on the body. Skill in administering and interpreting allergy tests. Ability to develop treatment plans, including immunotherapy if necessary.
Current conversation:
{history}
[Patient]: {input}
[Skin Wellness AI]:"""

PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)
conversation = ConversationChain(
    prompt=PROMPT,
    llm=chat,
    verbose=True,
    memory=ConversationBufferMemory(ai_prefix="[Skin Wellness AI]", memory_key="history"),
)

outText = conversation.run( "I have skin rash, can you help")
print(outText)
