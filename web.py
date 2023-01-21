import streamlit as st
import functions

# Note: To fix OSError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions
# I have to add to streamlit command line the argument --server.port <4+ digit port no>. I suspect that streamlit is
# to use a port too low or that is already in use by another application. This is the only workaround I've found that
# solves this problem.
todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is intended to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter new todos here ...",
              on_change=add_todo, key="new_todo")
