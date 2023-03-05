{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6aab03da",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. Why are functions advantageous to have in your programs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66311b82",
   "metadata": {},
   "outputs": [],
   "source": [
    "#We can avoid rewriting the same logic again in a program."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a89b2ce2",
   "metadata": {},
   "outputs": [],
   "source": [
    "2. When does the code in a function run: when it is specified or when it is called?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c48489a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The code in a function run when it is called."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8031e54a",
   "metadata": {},
   "outputs": [],
   "source": [
    "3. What statement creates a function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a663bc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#def keyword followed by name. \n",
    "def name():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48509552",
   "metadata": {},
   "outputs": [],
   "source": [
    "4. What is the difference between a function and a function call?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e3b4e90",
   "metadata": {},
   "outputs": [],
   "source": [
    "#A function is a block of code that does a particular operation and returns a result.\n",
    "#A function call is a code used to pass control to a function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f71d8a73",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. How many global scopes are there in a Python program? How many local scopes?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45f3b26a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4 global scopes and 2 local scopes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bb2e3a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "6. What happens to variables in a local scope when the function call returns?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c4c0d7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The values will be stored in the function's local variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c84b099",
   "metadata": {},
   "outputs": [],
   "source": [
    "7. What is the concept of a return value? Is it possible to have a return value in an expression?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b688eef3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# return value concept is, it returns the value when the called funcion executes. Yes it is possible to have return with expressions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "507d3def",
   "metadata": {},
   "outputs": [],
   "source": [
    "8. If a function does not have a return statement, what is the return value of a call to that function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e288da47",
   "metadata": {},
   "outputs": [],
   "source": [
    "# It returns default value i.e. None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b16dff0",
   "metadata": {},
   "outputs": [],
   "source": [
    "9. How do you make a function variable refer to the global variable?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b73b209",
   "metadata": {},
   "outputs": [],
   "source": [
    "# local variable can be used only inside that function. By writing global keyword inside function, it can be possible."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe322ff0",
   "metadata": {},
   "outputs": [],
   "source": [
    "10. What is the data type of None?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "33e928f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "NoneType"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f02aa6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "11. What does the sentence import areallyourpetsnamederic do?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4ef04e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#When called import areallyourpetsnamederic, it will import module named areallyourpetsnamederic."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29ea3592",
   "metadata": {},
   "outputs": [],
   "source": [
    "12. If you had a bacon() feature in a spam module, what would you call it after importing spam?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb598794",
   "metadata": {},
   "outputs": [],
   "source": [
    "#from spam import bacon."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a932bfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "13. What can you do to save a programme from crashing if it encounters an error?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c17d92c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we should use error handling concept."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa282518",
   "metadata": {},
   "outputs": [],
   "source": [
    "14. What is the purpose of the try clause? What is the purpose of the except clause?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63a283ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The try block lets you test a block of code for errors. The except block lets you handle the error."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
