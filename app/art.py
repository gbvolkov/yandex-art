from flask import Blueprint, render_template, url_for, flash, redirect, request, session
from app.forms import PostGeneratorForm
#from config import OPENAI_API_KEY
from datetime import datetime, timedelta

art = Blueprint('art', __name__)


from generators.image_gen import ImageGenerator as ImagePostGenerator

@art.route("/post_generator", methods=['GET', 'POST'])
def post_generator():
    form = PostGeneratorForm()
    image_url = session.get('image_url')

    if form.validate_on_submit():
        tone = form.tone.data
        topic = form.topic.data
        shape = form.shape.data

        image_generator = ImagePostGenerator()
        image_base64 = image_generator.generate_image(topic, tone, shape)
        image_url = f"data:image/png;base64,{image_base64}"

        #session['image_url'] = image_url

    return render_template('post_generator.html', title='Post Generator', form=form, image_url=image_url)

@art.route("/new_post", methods=['GET'])
def new_post():
    session.pop('post_text', None)
    session.pop('image_url', None)
    return redirect(url_for('art.post_generator'))