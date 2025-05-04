# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

**Reflection on IST356 Assignment 03**  

This assignment helped me learn how to use Streamlit to create interactive web applications with Python. At first, I found it challenging to understand how Streamlit works because it runs differently from regular Python scripts. The program reloads every time you interact with it, which was confusing at first. However, after working through the three parts, I started to see how useful Streamlit can be for building simple interfaces quickly.  

The first part, `one_package.py`, was the easiest because it only required processing a single input. I learned how to use `st.text_input()` and display results properly. The second part, `process_file.py`, was harder because I had to handle file uploads and process multiple lines of data. Converting the file content into readable text and saving it as JSON took some trial and error. The third part, `process_files.py`, was the most difficult because I had to track data between sessions using `st.session_state`. At first, I didn’t realize I needed this to keep count across multiple file uploads, but once I figured it out, it made sense.  

Overall, this assignment improved my understanding of Streamlit and how to structure interactive programs. I also got better at debugging when things didn’t work as expected. The most important lesson was learning how to persist data in a web app, which will be useful for future projects. Next time, I’d like to add error handling to make the programs more user-friendly. This assignment showed me that even when coding feels frustrating, working through problems helps me learn the most.