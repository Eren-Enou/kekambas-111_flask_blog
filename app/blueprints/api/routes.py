from . import api
from app.models import Post


@api.route('/')
def index():
    return 'Hello this is the API'

# Endpoint to get all of the posts
@api.route('/posts')
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
