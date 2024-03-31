import io
import psycopg2

from fastapi import FastAPI, Response
from PIL import Image
from dotenv import dotenv_values

env_vars = dotenv_values()

connection = psycopg2.connect(**env_vars)
connection.autocommit = True

app = FastAPI()

# Route to get image from id
@app.get("/image/{image_id}")
async def get_image(image_id: int):

    '''Func to get image from id'''

    try:

        with connection.cursor() as cursor:
            cursor.execute('''SELECT book_image 
                        FROM books_data 
                        WHERE id = %s''', (image_id,))
            
            image_data = cursor.fetchone()[0]

        image = Image.open(io.BytesIO(image_data))

        # Converting an image into bytes for sending via FastAPI
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format="PNG")
        img_byte_array = img_byte_array.getvalue()

        # Returning an image as a response
        return Response(content=img_byte_array, media_type="image/png")
    
    except:
        return {'message': 'something wrong!'}

# Route to get info from database
@app.get('/all_books')
async def get_all_books():

    '''Func to get info from database'''

    with connection.cursor() as cursor:
        cursor.execute('''SELECT id, author, book_name, book_link
                       FROM books_data
                       ORDER BY id
                       ''')
        
        data = cursor.fetchall()
        finally_data = [{'id': i[0], 'author': i[1], 'book_name': i[2], 'book_link': i[3]} for i in data]

        return {'result': finally_data}