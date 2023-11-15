import streamlit as st
import functions
import time

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()
    if not todo:
        st.warning('Nothing to add.', icon="⚠️")
        return

    if todo+"\n" not in todos:
        todos.append(todo+"\n")
        functions.write_todos(todos)
    else:
        st.error(f'"{todo}" is already on the To-Do list', icon="❌")

    st.session_state["new_todo"] = None


st.title("My To-Do App")
st.write("*Helping you Manage your To-Do list* :sunglasses:")
now = time.strftime("%b %d, %Y %H:%M:%S")
st.caption(now)
st.info('To complete a pending To-Do: ☑ (select the check box)', icon="ℹ️")

checkbox = False

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)

    if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.session_state["new_todo"] = None
            st.rerun()

st.text_input(label="To-Do:", placeholder="Add new todo...",
                  on_change=add_todo, key='new_todo')
