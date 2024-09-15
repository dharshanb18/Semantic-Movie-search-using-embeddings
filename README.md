This project has an objective to give context to the llm, By giving it the relavent content from a database(also we can scrape for it via a thread)
I have used vector search rather than a simple keyword search to understand the meaning of the query and return similar content with sematic meaning
I have 3 inputs a) Query 2)K value(top k value) 3) Threshold value for the similarity score
When user enters these values , we will get the k results based on their query
It is almost like a part of RAG

Here is a step by step demonstartion
1)Run app.py

![image](https://github.com/user-attachments/assets/686fc5af-e2d4-45e6-b892-9f42c4a8561a)

2)enter the the local host port 5000

![image](https://github.com/user-attachments/assets/f237ffda-bc8f-4b88-b010-e72373691824)

3)enter the values and see the result

![image](https://github.com/user-attachments/assets/7019d5b8-18a4-472e-83e4-a4f27b4e31ca)


My database setup:
I used MongoDB and their database for this purpose and then I use vector search using an embedding which I will tell later
![Screenshot 2024-08-08 104149](https://github.com/user-attachments/assets/94efc79b-5d47-4585-a20a-bbc5f5872c68)

For my embedding I used Hugging face transformer to generate embedding vector for a sentence

![image](https://github.com/user-attachments/assets/6129070c-9095-4e58-8be0-431d5aacd6c7)


Then I have used this pipeline to predict these matches based on similarity score, can use cosine score or manhatten score whichever we choose to , I have use cosine score



