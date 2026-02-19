from flask import Flask, render_template, request, jsonify
import os
import pyodbc
from collections import Counter
from dotenv import load_dotenv

# Load local environment variables
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    connection_string = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.environ.get('DB_SERVER')};"
        f"DATABASE={os.environ.get('DB_NAME')};"
        f"UID={os.environ.get('DB_USER')};"
        f"PWD={os.environ.get('DB_PASSWORD')}"
    )
    return pyodbc.connect(connection_string)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/planner')
def planner():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Pulling data from your dbo.meals table
        cursor.execute("SELECT name, ingredient, calories, category FROM dbo.meals")
        rows = cursor.fetchall()
        
        meals_dict = {}
        for row in rows:
            meal_name = row[0]
            if meal_name not in meals_dict:
                meals_dict[meal_name] = {
                    'ingredients': [],
                    'calories': row[2],
                    'category': row[3]
                }
            meals_dict[meal_name]['ingredients'].append(row[1])
        
        return render_template('planner.html', meals=meals_dict)
    
    except Exception as e:
        print(f"Database Error: {e}")
        return f"Database Error: {str(e)}", 500
    
    finally:
        # This is the finally clause that was likely missing or incomplete
        if conn:
            conn.close()

@app.route('/shopping-list', methods=['POST'])
def shopping_list():
    selected_meals = request.json.get('meals', [])
    if not selected_meals:
        return jsonify({'error': 'No meals selected'}), 400

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        all_ingredients = []
        meal_details = []
        
        for meal in selected_meals:
            cursor.execute("SELECT ingredient FROM dbo.meals WHERE name = ?", (meal,))
            ingredients = [row[0] for row in cursor.fetchall()]
            
            if ingredients:
                meal_details.append({
                    'name': meal,
                    'ingredients': ingredients
                })
                all_ingredients.extend(ingredients)
        
        ingredient_counts = Counter(all_ingredients)
        
        return jsonify({
            'selected_meals': selected_meals,
            'meal_details': meal_details,
            'ingredients': dict(ingredient_counts)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        if conn:
            conn.close()

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000)
    