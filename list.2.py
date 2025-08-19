{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d6970efe",
   "metadata": {},
   "outputs": [],
   "source": [
    "product_data = {\n",
    "    \"store\": \"TechNova\",\n",
    "    \"location\": {\n",
    "        \"city\": \"San Francisco\",\n",
    "        \"country\": \"USA\"\n",
    "    },\n",
    "    \"products\": [\n",
    "        {\n",
    "            \"id\": \"P1001\",\n",
    "            \"name\": \"Wireless Mouse\",\n",
    "            \"brand\": \"LogiTech\",\n",
    "            \"price\": 29.99,\n",
    "            \"currency\": \"USD\",\n",
    "            \"stock\": 134,\n",
    "            \"specs\": {\n",
    "                \"color\": \"Black\",\n",
    "                \"connectivity\": \"Bluetooth\",\n",
    "                \"battery_life\": \"12 months\"\n",
    "            },\n",
    "            \"ratings\": {\n",
    "                \"average\": 4.5,\n",
    "                \"count\": 240\n",
    "            }\n",
    "        },\n",
    "        {\n",
    "            \"id\": \"P1002\",\n",
    "            \"name\": \"Mechanical Keyboard\",\n",
    "            \"brand\": \"KeyChron\",\n",
    "            \"price\": 79.99,\n",
    "            \"currency\": \"USD\",\n",
    "            \"stock\": 57,\n",
    "            \"specs\": {\n",
    "                \"color\": \"White\",\n",
    "                \"switch_type\": \"Gateron Brown\",\n",
    "                \"backlight\": \"RGB\"\n",
    "            },\n",
    "            \"ratings\": {\n",
    "                \"average\": 4.7,\n",
    "                \"count\": 145\n",
    "            }\n",
    "        },\n",
    "        {\n",
    "            \"id\": \"P1003\",\n",
    "            \"name\": \"Sony Wireless Noise-Canceling Headphones\",\n",
    "            \"brand\": \"Sony\",\n",
    "            \"price\": 199.99,\n",
    "            \"currency\": \"USD\",\n",
    "            \"stock\": 23,\n",
    "            \"specs\": {\n",
    "                \"color\": \"Black\",\n",
    "                \"connectivity\": \"Bluetooth\",\n",
    "                \"noise_cancellation\": \"Active\",\n",
    "                \"battery_life\": \"30 hours\"\n",
    "            },\n",
    "            \"ratings\": {\n",
    "                \"average\": 4.8,\n",
    "                \"count\": 529\n",
    "            }\n",
    "        }\n",
    "    ]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1e64bea1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Task 3: Create a List of All Unique Brands\n",
    "# Loop through the product data and store all unique brands in a list. Then print the final list.\n",
    "# Example Output:\n",
    "#  Available brands: ['LogiTech', 'KeyChron', 'Sony']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e9e5028a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Available brands: ['LogiTech', 'KeyChron', 'Sony']\n"
     ]
    }
   ],
   "source": [
    "list_of_brands = []\n",
    "for i in range(0,3):\n",
    "    if product_data['products'][i]['brand'] not in list_of_brands:\n",
    "        list_of_brands.append(product_data['products'][i]['brand'])\n",
    "print(f'Available brands: {list_of_brands}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31f403b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "py311env",
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
   "version": "3.12.3"
  }
 }


list_of_brands = []
for i in range(0,3):
    if product_data['products'][i]['brand'] not in list_of_brands:
        list_of_brands.append(product_data['products'][i]['brand'])
print(f'Available brands: {list_of_brands}')
