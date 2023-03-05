{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba74b765",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. Why are functions advantageous to have in your programs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a76646ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "#We can avoid rewriting the same logic again in a program."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b086f14c",
   "metadata": {},
   "outputs": [],
   "source": [
    "2. When does the code in a function run: when it is specified or when it is called?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "152a7ca8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The code in a function run when it is called."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c29799a",
   "metadata": {},
   "outputs": [],
   "source": [
    "3. What statement creates a function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78c66a16",
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
   "id": "a595de94",
   "metadata": {},
   "outputs": [],
   "source": [
    "4. What is the difference between a function and a function call?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "083491d0",
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
   "id": "8aa10f60",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. How many global scopes are there in a Python program? How many local scopes?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cfd2d6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4 global scopes and 2 local scopes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51954f6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "6. What happens to variables in a local scope when the function call returns?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cbcdc94",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The values will be stored in the function's local variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a85db1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "7. What is the concept of a return value? Is it possible to have a return value in an expression?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "762c267a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# return value concept is, it returns the value when the called funcion executes. Yes it is possible to have return with expressions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6106eb98",
   "metadata": {},
   "outputs": [],
   "source": [
    "8. If a function does not have a return statement, what is the return value of a call to that function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f63eccf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# It returns default value i.e. None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bec6775c",
   "metadata": {},
   "outputs": [],
   "source": [
    "9. How do you make a function variable refer to the global variable?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aba7a164",
   "metadata": {},
   "outputs": [],
   "source": [
    "# local variable can be used only inside that function. By writing global keyword inside function, it can be possible."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9ab374d",
   "metadata": {},
   "outputs": [],
   "source": [
    "10. What is the data type of None?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5f5a9ac0",
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
   "id": "4b624a44",
   "metadata": {},
   "outputs": [],
   "source": [
    "11. What does the sentence import areallyourpetsnamederic do?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a1e09c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#When called import areallyourpetsnamederic, it will import module named areallyourpetsnamederic."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00517f03",
   "metadata": {},
   "outputs": [],
   "source": [
    "12. If you had a bacon() feature in a spam module, what would you call it after importing spam?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "735e0c5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#from spam import bacon."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "143ab5dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "13. What can you do to save a programme from crashing if it encounters an error?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d71f36d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#we should use error handling concept."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6732eebe",
   "metadata": {},
   "outputs": [],
   "source": [
    "14. What is the purpose of the try clause? What is the purpose of the except clause?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76b4e8d5",
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
