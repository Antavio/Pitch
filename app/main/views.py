from flask import render_template,redirect,url_for,request,abort,flash
from . import main
from ..models import User,Pitch
from .forms import UpdateProfile,PitchForm
from flask_login import login_required,current_user
from .. import db,photos

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitches', methods = ['GET', 'POST'])
@login_required
def pitches_list():
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.pitch_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.pitches_list'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Pitches Page'    
    return render_template('pitches.html', title = title, pitch_form = pitch_form, pitches = all_pitches)