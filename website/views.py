from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from database import get_db 
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user=current_user)
            new_note.save()
            flash('Note added!', category='success')

    notes = Note.objects(user=current_user)
    return render_template("home.html", user=current_user, notes=notes)

@views.route('/delete-note/<string:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    try:
        note_to_delete = Note.objects.get(id=note_id, user=current_user)
        note_to_delete.delete()
        flash('Note deleted!', category='success')
        return jsonify({'status': 'success'})
    except Note.DoesNotExist:
        flash('Note not found or you do not have permission to delete it.', category='error')
        return jsonify({'status': 'error'})
    except Exception as e:
        flash('An error occurred while deleting the note.', category='error')
        return jsonify({'status': 'error', 'message': str(e)})

@views.app_errorhandler(404)  # Handle 404 errors
def page_not_found(e):
    print("404 Error. Requested URL:", request.url)
    return 'Page not found', 404

@views.route('/')
def index():
    # Example usage: Retrieve data from MongoDB
    db = get_db()
    notes_collection = db['notes']
    notes = notes_collection.find()  # Retrieve all notes from the 'notes' collection
    return render_template('index.html', notes=notes)
