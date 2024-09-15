This project has an objective to give context to the llm, By giving it the relavent content from a database(also we can scrape for it via a thread)
I have used vector search rather than a simple keyword search to understand the meaning of the query and return similar content with sematic meaning
I have 3 inputs a) Query 2)K value(top k value) 3) Threshold value for the similarity score
When user enters these values , we will get the k results based on their query
It is almost like a part of RAG

Here is a step by step demonstartion
1)Run app.py

![image](https://github.com/user-attachments/assets/686fc5af-e2d4-45e6-b892-9f42c4a8561a)

2)enter the the local host port 5000
