from flask import request
from . import api
from app.models import Post


@api.route('/')
def index():
    return 'Hello this is the API'

# Endpoint to get all of the posts
@api.route('/posts', methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return [post.to_dict() for post in posts]

# Endpoint to get a single post by ID
@api.route('/posts/<int:post_id>')
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return {'error': f'Post with the ID of {post_id} does not exist.'}, 404
    return post.to_dict()

# Endpoint to create a new post
@api.route('/posts', methods=["POST"])
def create_post():
    # Check to see that the request body is JSON aka application/json content-type
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ['title', 'body', 'user_id']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            # If the field is not in the request body, add that to missing fields list
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400

    # Get the data from the request body
    title = data.get('title')
    body = data.get('body')
    image_url = data.get('image_url')
    user_id = data.get('user_id')

    # Create a new Post instance with the data from the request
    new_post = Post(title=title, body=body, image_url=image_url, user_id=user_id)

    # Return the new post as a JSON response
    return new_post.to_dict(), 201
