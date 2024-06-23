from flask import Blueprint, redirect, render_template, request

#           bluepring name
bp = Blueprint("pages", __name__)

todo_list = [
    "wash cloths today.",
    "clean room on sunday",
    "wake up early",
    "go to barber",
    "do testing on dev.",
]


@bp.route("/", methods=['GET','POST'])
def default():
    if request.method == 'POST':
        text = request.form['text']
        if text.strip() != '':
            todo_list.append(text) # add logic to add in database
    print(todo_list)
    return render_template("home.html",  all_todos=todo_list)


@bp.route("/delete", methods=['POST'])
def delete_todo():
    text = request.form['todo_to_delete']
    todo_list.remove(text) # add logic to delete from database
    return redirect("/")

