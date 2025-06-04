{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cc2af38f-f80e-49f7-a9fa-ed62b8342762",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum: 15\n",
      "Sum: 8\n",
      "Product: 30\n"
     ]
    }
   ],
   "source": [
    "def custom_function(a, b=10, c=None):\n",
    "    if c is None:\n",
    "        print(\"Sum:\", a + b)\n",
    "    else:\n",
    "        print(\"Product:\", a * b * c)\n",
    "\n",
    "# Example calls\n",
    "custom_function(5)            # Sum: 15\n",
    "custom_function(5, b=3)       # Sum: 8\n",
    "custom_function(5, b=3, c=2)  # Product: 30\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cfd52e0a-348a-4175-9940-6d0404c82aab",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'grape']\n"
     ]
    }
   ],
   "source": [
    "def filter_long_strings(string_list):\n",
    "    return [s for s in string_list if len(s) >= 5]\n",
    "\n",
    "# Example\n",
    "words = [\"apple\", \"cat\", \"banana\", \"dog\", \"grape\"]\n",
    "print(filter_long_strings(words))  # Output: ['apple', 'banana', 'grape']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb69573e-4a06-48ca-b55a-efedb61f56ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 17\n"
     ]
    }
   ],
   "source": [
    "expression = \"3 * 5 + 2\"\n",
    "result = eval(expression)\n",
    "print(\"Result:\", result)  # Output: Result: 17\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ff824b87-f11e-4293-be65-64a7430f7e64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Primes: [2, 3, 5, 7, 11]\n"
     ]
    }
   ],
   "source": [
    "def is_prime(n):\n",
    "    if n <= 1:\n",
    "        return False\n",
    "    for i in range(2, int(n**0.5)+1):\n",
    "        if n % i == 0:\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]\n",
    "prime_numbers = list(filter(is_prime, numbers))\n",
    "print(\"Primes:\", prime_numbers)  # Output: [2, 3, 5, 7, 11]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d782baa0-9288-48d5-bf99-c8de3221d5a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Uppercase: ['HELLO', 'WORLD', 'PYTHON', 'MAP']\n"
     ]
    }
   ],
   "source": [
    "words = [\"hello\", \"world\", \"python\", \"map\"]\n",
    "uppercase_words = list(map(str.upper, words))\n",
    "print(\"Uppercase:\", uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON', 'MAP']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c8bd955-86fd-4bfc-a881-357e1638244c",
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
