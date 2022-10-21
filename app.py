"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_DATABASE_URI'] = (
  "postgresql://otherjoel:hello@13.57.9.123/otherjoel")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def pet_list():
    """ Shows all pets and renders html """
    pets = Pet.query.all()

    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def pet_add():
    """ Pet add form; handle adding """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data or None

        new_pet = Pet(
          name=name,
          species=species,
          photo_url=photo_url,
          age=age,
          notes=notes
        )

        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('pet_add_form.html', form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_display_edit(pet_id):
    """
    Display pet details

    Pet edit form; handle editing
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data or None
        pet.available = form.available.data

        db.session.commit()

        flash("Successfully edited")
        return redirect(f'/{pet_id}')

    else:
        return render_template('pet_details_edit_form.html', form=form, pet=pet)
