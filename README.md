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

Finally, companies may find the ideas too generic. In order to adapt the ideas to the reality of the companies' budget, we can use the Solar API to finetune the ideas. We take advantage of Solar's ability for groundedness checks and Korean background to serve Korean communities in Jeju Island (in this demo).

### Important Links:

# Upstage API Usage

The Upstage API was used three times. During the creation of the dashboard, to 

### Dashboard
### Brainstorming


### Chat and Finetuning



# Installation