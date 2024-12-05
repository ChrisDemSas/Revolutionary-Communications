# Project Overview

The main purpose of creating RevCom.ai is to provide a comfortable space for local communities to criticize the practices of tour companies and for tour companies to save time brainstorming for solutions using LLMs. We wanted a way for tour companies to efficiently analyze feedback from local communities to sustainably improve their tour packages. We also wanted companies to measure the impact their practices have on local communities, and then start the brainstorming of how to address these complaints by leveraging Solar LLM. For local communities, we wanted a way to provide easy and anonymized feedback to tour companies. 

Note, that for the purpose of the Upstage Hackathon, only 1 community is available: Haenyeo and 1 company: Company1.

### Feedback Form

The main part for the locals, who use RevCom.ai is the anonymized feedback form. Locals can pick the company name, community name and the category of feedback (Miscellaneous, Economic, Treatment, Environmental, Cultural). Then, the locals can input their feedback in the textbox before clicking the submit button. Finally, the feedback is analyzed using a finetuned version of Solar LLM which is finetuned for sentiment analysis. A sentiment rating between 1 and 10 is given, whereby 1 is the most negative, and 10 is the most positive feedback. The feedback data is then stored in feedback.db for use in dashboards.

### Dashboard

The data from the feedback is ingested and shown on a dashboard. Here, we have a variety of charts which include sentiment rating over time, average sentiment for each category, total number of feedback etc. We also have a comments table at the very bottom of the dashboard to show when the feedback was sent, sentiment rating, the feedback itself etc. The dashboard is where companies can observe trends of what impacts they have on local communities.

### Brainstorming Page

Sometimes, it is not enough to see the data in a dashboard and companies may wish to get a headstart in brainstorming. We use Solar LLM here to do a brainstorming session. The prompts can be seen in main.py and solar.py.

### Chat and Finetune Ideas

Finally, companies may find the ideas too generic. In order to adapt the ideas to the reality of the companies' budget, we can use the Solar API to finetune the ideas. 

### Important Links:

Video, Project Information: https://drive.google.com/drive/u/0/folders/1PLdXby7QD4tGoKwdfjDTkZYyGGuYqUuT

# Upstage API Usage

The Upstage API was used three times. During the creation of the dashboard by analyzing sentiment from feedback, to brainstorming and chatting with Solar API.

### Sentiment Analysis (Dashboard)

We finetuned using Predibase in order to make Solar LLM better at sentiment analysis. We generated 200 comments from ChatGPT to simulate feedback for each of the five categories (Environment, Economic, Treatment, Cultural, Miscellaneous). We then assigned a sentiment rating for each comment and used Predibase for fine-tuning (Epoch = 3, Rank = 16). We saw a win rate of 67% when we used the finetuned model. This model was used to analyze the sentiment and show the results on a dashboard. The data can be found in 'solar_finetuning.ipynb' under the 'llm' folder.

### Brainstorming

We have a default prompt, where we pretended that Solar LLM was an experienced consultant for a tour company and the most recent feedback from 7 days, to generate 10 solutions. The default prompt can be seen in main.py, and is recorded here:

"""

    You are a consultant for a medium sized tour company. You are to come up with actionable solutions to address the following complaints from the local community:

       {comments}

    What are 10 detailed solutions can you suggest to the tour company to resolve these complaints to make their tour packages more sustainable and appease the local community? 
    Make sure the solutions deal primarily with the tour company and tourists, and not the local community. 
"""

Where {comments} indicate the comments from locals from the last 7 days. This prompt is used as a way to generate 10 ideas, with the system prompt: "You are a consultant to a tour company".

### Chat and Finetuning

Similarly to before, we have a default prompt "You are a consultant to a tour company". We added the previous prompt to the chat history, which allows the user to chat with Solar API while keeping this in mind.

# Installation

## NOTE: THIS CODE WILL NOT RUN WITHOUT keys.py WHICH THE AUTHOR OF THE CODE HAS. CONTACT THE AUTHOR FOR THE FILE keys.py BY EMAIL: christopher.sastropranoto@gmail.com.

### USERNAME: Company1
### PASSWORD: password

1) Install Python (https://www.python.org/downloads/)
2) Download the source code by clicking the 'Code' button on Github and select 'Download ZIP'.
2) Install everything in the 'requirements.text' by opening Terminal and running !pip install -r path/to/requirements.txt
    Replace path/to by the actual file path to where requirements.txt is.
3) Put keys.py inside the same file as main.py file.
4) Install an IDE such as VSCode or Wing.
5) Open and run main.py
6) Open your web browser and type in: http://127.0.0.1:8000 or http://192.168.18.4:8000 at the top.

## NOTE: WHEN YOU GIVE FEEDBACK ON THE FEEDBACK FORM, YOU HAVE TO RESTART THE APP FOR THE FEEDBACK TO BE ANALYZED IN THE DASHBOARD.
## NOTE: YOU HAVE TO USE THE CORRECT USERNAME AND PASSWORD OR ELSE THE PROGRAM WILL CRASH.

# Future Plans

Add a QR code feature which would be accessible to only members of the community, to reduce impersonation risk.
Add Retrieval Augmented Generation (RAG) feature for the chatting and brainstorming features so that companies can further finetune the responses of Solar LLM.
Make the dashboards public to promote transparency and accountability to other tourists and tour communities. 
Implement a way for local communities to give suggestions or plans, instead of completely relying on the AI.
Implement an incentives for companies and local communities for better co-operation.
Redo the fine tuning using comments from surveying local communities instead of relying on ChatGPT.

# Tech Stack
Front-End: CSS, HTML, Basic Javascript
Back-End: Flask, Python, API (Predibase and OpenAI), Dash, Pandas, Sqlite Databases
