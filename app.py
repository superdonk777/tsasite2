import sqlite3

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_random_secret_key'  # Required for using session

# Sample "database" of recipes
ALL_RECIPES = [
    {
        "id": 1,
        "title": "Chili",
        "description": "A hearty and flavorful chili perfect for any occasion.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["comfort food"],
        "ingredients": [
            "ground beef",
            "onion",
            "garlic",
            "canned tomatoes",
            "kidney beans",
            "chili powder",
            "cumin",
            "paprika",
            "salt",
            "pepper"
        ],
        "instructions": [
            "1. Sauté onion and garlic until softened.",
            "2. Add ground beef and cook until browned.",
            "3. Stir in tomatoes, beans, chili powder, cumin, paprika, salt, and pepper.",
            "4. Simmer for 20–30 minutes. Serve warm."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2014/06/28/14/14/chili-con-carne-378952_1280.jpg"
    },
    {
        "id": 2,
        "title": "Chicken Noodle Soup",
        "description": "A classic, comforting soup perfect for cold days.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["comfort food"],
        "ingredients": [
            "chicken breast",
            "carrots",
            "celery",
            "onion",
            "chicken broth",
            "egg noodles",
            "thyme",
            "salt",
            "pepper"
        ],
        "instructions": [
            "1. Sauté carrots, celery, and onion until soft.",
            "2. Add broth and bring to a boil.",
            "3. Stir in noodles and chicken; cook until noodles are tender.",
            "4. Add thyme, salt, and pepper. Simmer 5 minutes."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2016/07/07/19/51/soup-1503117_1280.jpg"
    },
    {
        "id": 3,
        "title": "Cobb Salad",
        "description": "A hearty salad with chicken, bacon, avocado, and blue cheese.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["salad"],
        "ingredients": [
            "lettuce",
            "hard-boiled egg",
            "avocado",
            "cherry tomatoes",
            "bacon",
            "blue cheese",
            "grilled chicken"
        ],
        "instructions": [
            "1. Arrange lettuce on a plate.",
            "2. Top with egg, avocado, tomatoes, bacon, blue cheese, and chicken.",
            "3. Drizzle with dressing and serve."
        ],
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPrABQAGqQDFeWrDftAdM90W_pTMc4pMsxFA&s"
    },
    {
        "id": 4,
        "title": "Caesar Salad",
        "description": "A classic Caesar salad with romaine, croutons, and Parmesan.",
        "cuisine": "Italian",
        "dietary": "None",
        "tags": ["salad"],
        "ingredients": [
            "romaine lettuce",
            "croutons",
            "Parmesan cheese",
            "Caesar dressing"
        ],
        "instructions": [
            "1. Toss lettuce, croutons, and Parmesan in a bowl.",
            "2. Drizzle Caesar dressing and mix gently."
        ],
        "image_url": "https://img.taste.com.au/J6WbLwTn/w720-h480-cfill-q80/taste/2016/11/caesar-salad-29418-1.jpeg"
    },
    {
        "id": 5,
        "title": "Fried Rice",
        "description": "A quick and versatile fried rice dish.",
        "cuisine": "Asian",
        "dietary": "None",
        "tags": ["easy"],
        "ingredients": [
            "rice",
            "mixed vegetables",
            "eggs",
            "soy sauce",
            "sesame oil"
        ],
        "instructions": [
            "1. Heat sesame oil in a pan. Add vegetables and sauté.",
            "2. Push veggies aside, cook eggs, and mix with veggies.",
            "3. Stir in rice and soy sauce. Cook for 5 minutes."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2023/01/09/23/23/fried-rice-7708486_1280.jpg"
    },
    {
        "id": 6,
        "title": "Sushi",
        "description": "Simple and delicious sushi rolls.",
        "cuisine": "Japanese",
        "dietary": "None",
        "tags": ["popular"],
        "ingredients": [
            "sushi rice",
            "nori sheet",
            "cucumber",
            "avocado",
            "cooked shrimp",
            "soy sauce"
        ],
        "instructions": [
            "1. Spread rice evenly on nori.",
            "2. Add fillings in a line near one edge.",
            "3. Roll tightly, slice into pieces, and serve with soy sauce."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2018/08/03/08/33/food-3581341_1280.jpg"
    },
    {
        "id": 7,
        "title": "Butter Chicken",
        "description": "A creamy, spiced chicken curry.",
        "cuisine": "Indian",
        "dietary": "None",
        "tags": ["comfort food"],
        "ingredients": [
            "chicken",
            "tomato sauce",
            "heavy cream",
            "butter",
            "garam masala",
            "turmeric",
            "garlic"
        ],
        "instructions": [
            "1. Cook chicken in butter until browned.",
            "2. Stir in tomato sauce, cream, garlic, and spices.",
            "3. Simmer for 15 minutes. Serve with rice."
        ],
        "image_url": "https://www.shutterstock.com/image-photo/top-view-butter-chicken-rice-600nw-2364473377.jpg"
    },
    {
        "id": 8,
        "title": "Cheeseburger",
        "description": "A classic cheeseburger with all the fixings.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["popular", "grilling"],
        "ingredients": [
            "ground beef",
            "cheese slices",
            "burger buns",
            "lettuce",
            "tomato",
            "ketchup",
            "mustard"
        ],
        "instructions": [
            "1. Form ground beef into patties and season with salt and pepper.",
            "2. Grill or pan-fry patties until cooked through; add cheese slices to melt.",
            "3. Assemble with buns and toppings of your choice."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2019/04/22/08/37/burger-4145977_1280.jpg"
    },
    {
        "id": 9,
        "title": "Omelette",
        "description": "A quick and easy omelet with your favorite fillings.",
        "cuisine": "French",
        "dietary": "None",
        "tags": ["breakfast"],
        "ingredients": [
            "eggs",
            "cheese",
            "ham",
            "vegetables",
            "butter"
        ],
        "instructions": [
            "1. Heat butter in a pan.",
            "2. Pour in whisked eggs; let set slightly.",
            "3. Add filling to one side, fold, and cook 1 more minute."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2015/05/20/16/11/kitchen-775746_1280.jpg"
    },
    {
        "id": 10,
        "title": "Waffles",
        "description": "Crispy, golden waffles perfect for breakfast.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["breakfast"],
        "ingredients": [
            "flour",
            "baking powder",
            "egg",
            "milk",
            "butter"
        ],
        "instructions": [
            "1. Mix flour, baking powder, egg, milk, and butter into batter.",
            "2. Pour into a waffle iron and cook until golden."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2022/07/26/22/48/waffle-7346835_1280.jpg"
    },
    {
        "id": 11,
        "title": "Gluten-Free Cookies",
        "description": "Soft and chewy gluten-free cookies perfect for dessert.",
        "cuisine": "American",
        "dietary": "Gluten-Free",
        "tags": ["dessert", "gluten-free"],
        "ingredients": [
            "almond flour",
            "butter",
            "sugar",
            "egg",
            "baking powder",
            "chocolate chips"
        ],
        "instructions": [
            "1. Preheat oven to 350°F (175°C).",
            "2. Mix almond flour, butter, sugar, and egg together.",
            "3. Add baking powder and chocolate chips to form dough.",
            "4. Scoop onto a baking sheet and bake for 10-12 minutes."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2023/06/22/22/29/cookies-8082386_1280.jpg"
    },
    {
        "id": 12,
        "title": "Gluten-Free Pizza",
        "description": "Delicious gluten-free pizza with your favorite toppings.",
        "cuisine": "Italian",
        "dietary": "Gluten-Free",
        "tags": ["pizza", "gluten-free"],
        "ingredients": [
            "gluten-free pizza crust",
            "pizza sauce",
            "mozzarella cheese",
            "pepperoni",
            "vegetables"
        ],
        "instructions": [
            "1. Preheat oven to 425°F (220°C).",
            "2. Spread pizza sauce over the gluten-free crust.",
            "3. Add cheese and your favorite toppings.",
            "4. Bake for 10-15 minutes until golden and bubbly."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2017/12/10/14/47/pizza-3010062_1280.jpg"
    },
    {
        "id": 13,
        "title": "Gluten-Free Bread",
        "description": "A quick and easy gluten-free bread recipe.",
        "cuisine": "American",
        "dietary": "Gluten-Free",
        "tags": ["bread", "gluten-free"],
        "ingredients": [
            "gluten-free flour",
            "baking powder",
            "milk",
            "egg",
            "butter",
            "sugar"
        ],
        "instructions": [
            "1. Mix dry ingredients together in a bowl.",
            "2. Add milk, egg, and melted butter to form a batter.",
            "3. Pour into a greased loaf pan.",
            "4. Bake at 350°F (175°C) for 25-30 minutes."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2016/07/11/17/31/bread-1510155_1280.jpg"
    },
    {
        "id": 14,
        "title": "Gluten-Free Pancakes",
        "description": "Fluffy and delicious gluten-free pancakes for breakfast.",
        "cuisine": "American",
        "dietary": "Gluten-Free",
        "tags": ["breakfast", "gluten-free"],
        "ingredients": [
            "gluten-free flour",
            "baking powder",
            "milk",
            "egg",
            "butter",
            "sugar"
        ],
        "instructions": [
            "1. Mix flour, baking powder, sugar, and milk together.",
            "2. Whisk in egg and melted butter until smooth.",
            "3. Pour batter onto a hot griddle and cook until bubbles form.",
            "4. Flip and cook until golden brown."
        ],
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxNlwfRdVK6A2KZIWAjpElMEZ5YXmGdh7d2Q&s"
    },
    {
        "id": 15,
        "title": "Squash Soup",
        "description": "A creamy and comforting soup made with roasted squash.",
        "cuisine": "American",
        "dietary": "Vegetarian",
        "tags": ["soup", "comfort food"],
        "ingredients": [
            "butternut squash",
            "vegetable broth",
            "onion",
            "garlic",
            "cream",
            "salt",
            "pepper"
        ],
        "instructions": [
            "1. Roast butternut squash until tender.",
            "2. Sauté onion and garlic in a pot.",
            "3. Add squash, broth, and seasonings. Simmer for 20 minutes.",
            "4. Blend until smooth and stir in cream. Serve warm."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2019/09/27/09/59/pumpkin-soup-4508015_1280.jpg"
    },
    {
        "id": 16,
        "title": "Pumpkin Pancakes",
        "description": "Fluffy and spiced pumpkin pancakes for a festive breakfast.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["breakfast", "seasonal"],
        "ingredients": [
            "flour",
            "baking powder",
            "pumpkin puree",
            "milk",
            "egg",
            "spices (cinnamon, nutmeg)"
        ],
        "instructions": [
            "1. Mix flour, baking powder, spices, and pumpkin puree in a bowl.",
            "2. Add milk and egg; stir until smooth.",
            "3. Cook pancakes on a hot griddle until bubbles form.",
            "4. Flip and cook until golden brown."
        ],
        "image_url": "https://t4.ftcdn.net/jpg/09/70/52/95/360_F_970529582_UHU7XN9o9lnKOFqf5MhhQXwzVApsx7Vv.jpg"
    },
    {
        "id": 17,
        "title": "Apple Cider Doughnuts",
        "description": "Soft and spiced apple cider doughnuts perfect for fall.",
        "cuisine": "American",
        "dietary": "None",
        "tags": ["dessert", "seasonal"],
        "ingredients": [
            "flour",
            "apple cider",
            "sugar",
            "eggs",
            "spices (cinnamon, nutmeg)",
            "baking powder",
            "oil"
        ],
        "instructions": [
            "1. Mix dry ingredients together in one bowl.",
            "2. Combine wet ingredients with dry to form a dough.",
            "3. Shape into doughnuts and fry in hot oil until golden.",
            "4. Toss in cinnamon sugar and serve."
        ],
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFIN4Q3tV2WMNlzuISbIr-ckS1v0n3Et2ToQ&s"
    },
    {
        "id": 18,
        "title": "Vegan Pesto Pasta",
        "description": "A creamy and delicious vegan pesto pasta.",
        "cuisine": "Italian",
        "dietary": "Vegan",
        "tags": ["pasta", "vegan"],
        "ingredients": [
            "pasta",
            "basil",
            "olive oil",
            "garlic",
            "pine nuts",
            "salt"
        ],
        "instructions": [
            "1. Cook pasta according to package instructions.",
            "2. Blend basil, olive oil, garlic, pine nuts, and salt into a pesto.",
            "3. Toss cooked pasta with pesto and serve."
        ],
        "image_url": "https://cdn.pixabay.com/photo/2018/10/27/22/11/pasta-3777541_1280.jpg"
    },
    {
        "id": 19,
        "title": "Vegan Cauliflower Steaks",
        "description": "Roasted cauliflower steaks with flavorful spices.",
        "cuisine": "American",
        "dietary": "Vegan",
        "tags": ["vegan", "vegetables"],
        "ingredients": [
            "cauliflower",
            "olive oil",
            "spices (paprika, cumin, salt, pepper)"
        ],
        "instructions": [
            "1. Slice cauliflower into thick steaks.",
            "2. Brush with olive oil and sprinkle with spices.",
            "3. Roast at 400°F (200°C) for 20-25 minutes.",
            "4. Serve warm as a main or side dish."
        ],
        "image_url": "https://www.shutterstock.com/image-photo/tasty-cauliflower-steaks-baking-dish-260nw-2519682423.jpg"
    },
    {
        "id": 20,
        "title": "Vegan Lasagna",
        "description": "A hearty vegan lasagna layered with vegetables and cashew cream.",
        "cuisine": "Italian",
        "dietary": "Vegan",
        "tags": ["vegan", "pasta"],
        "ingredients": [
            "lasagna noodles",
            "vegetables (zucchini, spinach, mushrooms)",
            "tomato sauce",
            "cashew cream"
        ],
        "instructions": [
            "1. Cook lasagna noodles according to package instructions.",
            "2. Layer noodles, vegetables, tomato sauce, and cashew cream in a baking dish.",
            "3. Bake at 375°F (190°C) for 30-35 minutes.",
            "4. Let cool slightly before serving."
        ],
        "image_url": "https://media02.stockfood.com/largepreviews/Mzg4MjgwMjM5/12525169-Half-Eaten-Portion-of-Vegetarian-Lasagna-on-a-Plate.jpg"
    },
    {
        "id":21,
        "title": "Generate your own recipe with AI",
        "description": "Ask ai to generate you a recipe with your favorite ingredients",
        "cuisine":"AI",
        "dietary": "AI",
        "tags": ["AI", "generate"],
        "ingredients": ["your favorite ingredients"],
        "instructions": ["Ask AI to generate a recipe with your favorite ingredients"],
        "image_url": "https://cdn.discordapp.com/attachments/1331418016805818480/1334636343250386954/1708232269853.png?ex=679d4074&is=679beef4&hm=729db2ce688d0272f87f463e00d1964718e6bcd42b5b9af970321ae07e7505ca&"
    }
]



def validate_recipes():
    required_keys = {"id", "title", "description", "cuisine", "dietary", "ingredients", "instructions"}
    for recipe in ALL_RECIPES:
        missing = required_keys - recipe.keys()
        if missing:
            print(f"Recipe ID {recipe.get('id', 'Unknown')} is missing keys: {', '.join(missing)}")

def recommend_recipes(favorite_cuisine, dietary_restrictions, favorite_food, least_favorite_food, ingredients_on_hand):
    recommended = []

    for recipe in ALL_RECIPES:
        # Safely get ingredients, defaulting to empty list if missing
        recipe_ingredients = recipe.get('ingredients', [])
        
        # Skip recipes without 'ingredients'
        if not recipe_ingredients:
            continue

        # 1) Cuisine check
        if favorite_cuisine and recipe['cuisine'].lower() != favorite_cuisine.lower():
            continue
        
        # 2) Dietary restrictions check
        if dietary_restrictions and dietary_restrictions.lower() != "none":
            if dietary_restrictions.lower() == "vegetarian":
                if recipe['dietary'].lower() not in ["vegetarian", "vegan"]:
                    continue
            elif dietary_restrictions.lower() == "vegan":
                if recipe['dietary'].lower() != "vegan":
                    continue
        
        # 3) Least favorite food check
        if least_favorite_food and least_favorite_food.lower() in recipe['title'].lower():
            continue
        
        # 4) Ingredients check (user must have all the recipe's ingredients)
        recipe_ingredients_lower = set(ing.lower() for ing in recipe_ingredients)
        user_ingredients_lower = set(ingredients_on_hand)
        
        if not recipe_ingredients_lower.issubset(user_ingredients_lower):
            continue

        recommended.append(recipe)

    # Fallback if no recipes matched
    if not recommended:
        return ALL_RECIPES
    return recommended

@app.context_processor
def inject_recipes():
    popular_recipes = [recipe for recipe in ALL_RECIPES if "popular" in recipe.get("tags", [])]
    return dict(all_recipes=ALL_RECIPES, popular_recipes=popular_recipes)




@app.route('/')
def home():
    # Select "popular" recipes for the sidebar
    popular_recipes = [recipe for recipe in ALL_RECIPES if "popular" in recipe.get("tags", [])]

    # Filter seasonal recipes
    seasonal_recipes = [recipe for recipe in ALL_RECIPES if "seasonal" in recipe.get("tags", [])]

    return render_template('home.html', popular_recipes=popular_recipes, seasonal_recipes=seasonal_recipes)


@app.route('/survey', methods=['GET', 'POST'])
def survey():
    """
    Handles the survey page for collecting user preferences.
    Saves the data to the database and session.
    """
    if request.method == 'POST':
        # Capture survey data
        name = request.form.get('name')
        favorite_cuisine = request.form.get('favorite_cuisine')
        dietary_restrictions = request.form.get('dietary_restrictions')
        favorite_food = request.form.get('favorite_food')
        least_favorite_food = request.form.get('least_favorite_food')
        ingredients_str = request.form.get('ingredients_on_hand', '')

        # Save survey responses to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO survey_responses (name, favorite_cuisine, dietary_restrictions, favorite_food, least_favorite_food, ingredients_on_hand)
        VALUES (?, ?, ?, ?, ?, ?)''', (name, favorite_cuisine, dietary_restrictions, favorite_food, least_favorite_food, ingredients_str))
        conn.commit()
        conn.close()

        # Store in session for use in /recipes
        session.update({
            'name': name,
            'favorite_cuisine': favorite_cuisine,
            'dietary_restrictions': dietary_restrictions,
            'favorite_food': favorite_food,
            'least_favorite_food': least_favorite_food,
            'ingredients_on_hand': [ingredient.strip().lower() for ingredient in ingredients_str.split(',')]
        })

        return redirect(url_for('recipes'))

    return render_template('survey.html')

@app.route('/survey-results')
def survey_results():
    """
    Displays all survey responses in a table format.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM survey_responses')
    survey_responses = cursor.fetchall()
    conn.close()

    column_names = ["ID", "Name", "Favorite Cuisine", "Dietary Restrictions", "Favorite Food", "Least Favorite Food", "Ingredients On Hand", "Timestamp"]
    return render_template('survey_results.html', survey_responses=survey_responses, column_names=column_names)


@app.route('/recipes')
def recipes():
    """
    Recommend recipes based on the session data from the survey.
    """
    favorite_cuisine = session.get('favorite_cuisine')
    dietary_restrictions = session.get('dietary_restrictions')
    favorite_food = session.get('favorite_food')
    least_favorite_food = session.get('least_favorite_food')
    ingredients_on_hand = session.get('ingredients_on_hand', [])  # Default to empty list

    recommended = recommend_recipes(
        favorite_cuisine,
        dietary_restrictions,
        favorite_food,
        least_favorite_food,
        ingredients_on_hand
    )

    return render_template('recipes.html', recipes=recommended)

@app.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    # Find the recipe by ID
    recipe = next((r for r in ALL_RECIPES if r["id"] == recipe_id), None)
    if not recipe:
        return render_template('404.html'), 404
    return render_template('recipe_detail.html', recipe=recipe)


@app.route('/search')
def search():
    """
    Handles recipe search functionality.
    Filters recipes based on title or description matching the search query.
    """
    query = request.args.get('query', '').lower()
    if not query:
        # Redirect to recipes page if no query is provided
        return redirect(url_for('recipes'))

    # Filter recipes based on the search query
    matched_recipes = [
        recipe for recipe in ALL_RECIPES
        if query in recipe['title'].lower() or query in recipe['description'].lower()
    ]

    return render_template('recipes.html', recipes=matched_recipes, search_query=query)

#DEEPSEEK AI INTEGRATION MXRCEL
import requests
import re
# Set the API URL
# Set the API URL
DEEPSEEK_API_URL = "http://127.0.0.1:11434/api/generate"  # Correct endpoint for Ollama

def filter_recipe(response_text):
    """
    Filter out unwanted text like </think> from the recipe.
    """
    # Remove <think> tags and other unwanted content
    filtered_text = re.sub(r'<think>.*?</think>', '', response_text, flags=re.DOTALL)
    return filtered_text.strip()

@app.route('/ai', methods=['GET', 'POST'])
def ai_gen_recipe():
    if request.method == "POST":
        user_input = request.form.get("ingredients")
        
        try:
            # Prepare the data to send to the Ollama server
            data = {
                "model": "deepseek-r1:1.5b",  # Use the correct model name
                "prompt": f"Generate a recipe using these ingredients: {user_input}.",
                "stream": False
            }
            
            # Send POST request to the Ollama server
            response = requests.post(DEEPSEEK_API_URL, json=data)
            
            if response.status_code == 200:
                # Extract the recipe from the response and filter it
                response_data = response.json()
                recipe = filter_recipe(response_data.get("response", "No recipe found."))
            else:
                # Handle errors
                recipe = f"Error: Received status code {response.status_code}. Response: {response.text}"
        except requests.exceptions.RequestException as e:
            # Handle connection or request issues
            recipe = f"Error: {str(e)}"
        
        # Pass the generated recipe to the template for display
        return render_template("_ai.html", recipe=recipe)
    
    return render_template("_ai.html")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    validate_recipes()  # Validate recipes on startup
    app.run(debug=True)

