{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "57eca9b4-4e91-4c7f-a211-59d3eb484e78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to the Python Quiz!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "What's your name?  Ramya\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi Ramya, let's begin!\n",
      "\n",
      "Q1. What is the output of 2 + 2?\n",
      "A. 22\n",
      "B. 4\n",
      "C. 2\n",
      "D. None\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer (A/B/C/D):  B\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct!\n",
      "\n",
      "Q2. What data type is the value: 3.14?\n",
      "A. Integer\n",
      "B. String\n",
      "C. Float\n",
      "D. Boolean\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer (A/B/C/D):  C\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct!\n",
      "\n",
      "Q3. Which keyword is used for a function in Python?\n",
      "A. fun\n",
      "B. def\n",
      "C. function\n",
      "D. define\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer (A/B/C/D):  B\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct!\n",
      "\n",
      "Q4. What is the output of: print(3 * '7')?\n",
      "A. 21\n",
      "B. 777\n",
      "C. 73\n",
      "D. Error\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer (A/B/C/D):  B\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct!\n",
      "\n",
      "Q5. Which loop repeats a block of code a known number of times?\n",
      "A. for\n",
      "B. while\n",
      "C. loop\n",
      "D. repeat\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer (A/B/C/D):  A\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correct!\n",
      "\n",
      "Your final score is: 5 out of 5\n",
      "Great job, Ramya!\n"
     ]
    }
   ],
   "source": [
    "def greet_user():\n",
    "    print(\"Welcome to the Python Quiz!\")\n",
    "    name = input(\"What's your name? \")\n",
    "    print(f\"Hi {name}, let's begin!\\n\")\n",
    "    return name\n",
    "\n",
    "def ask_question(question, options, correct_answer):\n",
    "    print(question)\n",
    "    for option in options:\n",
    "        print(option)\n",
    "    answer = input(\"Your answer (A/B/C/D): \").strip().upper()\n",
    "    \n",
    "    if answer == correct_answer:\n",
    "        print(\"Correct!\\n\")\n",
    "        return True\n",
    "    else:\n",
    "        print(f\"Wrong! The correct answer was {correct_answer}.\\n\")\n",
    "        return False\n",
    "\n",
    "def main():\n",
    "    name = greet_user()\n",
    "    score = 0\n",
    "\n",
    "    questions = [\n",
    "        {\n",
    "            \"question\": \"Q1. What is the output of 2 + 2?\",\n",
    "            \"options\": [\"A. 22\", \"B. 4\", \"C. 2\", \"D. None\"],\n",
    "            \"answer\": \"B\"\n",
    "        },\n",
    "        {\n",
    "            \"question\": \"Q2. What data type is the value: 3.14?\",\n",
    "            \"options\": [\"A. Integer\", \"B. String\", \"C. Float\", \"D. Boolean\"],\n",
    "            \"answer\": \"C\"\n",
    "        },\n",
    "        {\n",
    "            \"question\": \"Q3. Which keyword is used for a function in Python?\",\n",
    "            \"options\": [\"A. fun\", \"B. def\", \"C. function\", \"D. define\"],\n",
    "            \"answer\": \"B\"\n",
    "        },\n",
    "        {\n",
    "            \"question\": \"Q4. What is the output of: print(3 * '7')?\",\n",
    "            \"options\": [\"A. 21\", \"B. 777\", \"C. 73\", \"D. Error\"],\n",
    "            \"answer\": \"B\"\n",
    "        },\n",
    "        {\n",
    "            \"question\": \"Q5. Which loop repeats a block of code a known number of times?\",\n",
    "            \"options\": [\"A. for\", \"B. while\", \"C. loop\", \"D. repeat\"],\n",
    "            \"answer\": \"A\"\n",
    "        }\n",
    "    ]\n",
    "\n",
    "    for q in questions:\n",
    "        if ask_question(q[\"question\"], q[\"options\"], q[\"answer\"]):\n",
    "            score += 1\n",
    "\n",
    "    print(f\"Your final score is: {score} out of {len(questions)}\")\n",
    "    print(f\"Great job, {name}!\" if score >= 3 else f\"Keep practicing, {name}!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fe9b53b-c498-4eed-bce9-3bbf6af31462",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
