{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b7c52c3d",
   "metadata": {},
   "source": [
    "Task 2: Restaurant Performance Analyser (Pandas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "541293ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a2b0c658",
   "metadata": {},
   "outputs": [],
   "source": [
    "np.random.seed(42)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "00b5353c",
   "metadata": {},
   "outputs": [],
   "source": [
    "restaurant = np.random.choice(\n",
    "    ['Food Hub', 'Pizza Corner', 'Spice Garden',\n",
    "     'Chinese Wok', 'Sweet Treats'], 50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9b6a6321",
   "metadata": {},
   "outputs": [],
   "source": [
    "city = np.random.choice(['Ahmedabad', 'Mumbai', 'Delhi'], 50)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0e01d28c",
   "metadata": {},
   "outputs": [],
   "source": [
    "order_value = np.random.randint(200, 1000, 50)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "db280786",
   "metadata": {},
   "outputs": [],
   "source": [
    "delivery_time = np.random.randint(20, 45, 50)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7804b094",
   "metadata": {},
   "outputs": [],
   "source": [
    "rating = np.round(np.random.uniform(4.1, 5.0, 50), 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0681eacc",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "cuisine = np.random.choice(\n",
    "    ['Indian', 'Chinese', 'Fast Food'], 50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "84e2dc58",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({\n",
    "    'restaurant_name': restaurant,\n",
    "    'city': city,\n",
    "    'order_value': order_value,\n",
    "    'delivery_time_mins': delivery_time,\n",
    "    'rating': rating,\n",
    "    'cuisine_type': cuisine\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "171e3946",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = df.groupby('restaurant_name').agg({\n",
    "    'order_value': 'mean',\n",
    "    'delivery_time_mins': 'mean',\n",
    "    'rating': 'mean'\n",
    "}).reset_index()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "98ce223c",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = result[\n",
    "    (result['rating'] > 4.0) &\n",
    "    (result['delivery_time_mins'] < 35)\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "15b29ca3",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = result.sort_values(\n",
    "    'order_value', ascending=False\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "09572ae1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Restaurant Performance Summary:\n",
      "Empty DataFrame\n",
      "Columns: [restaurant_name, order_value, delivery_time_mins, rating]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "print(\"Restaurant Performance Summary:\")\n",
    "print(result.to_string(index=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9f88da9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
