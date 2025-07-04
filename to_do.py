import streamlit as st
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
def add_task(task, status):
    st.session_state.tasks.append({'task': task, 'status': status})
def edit_task(index, new_task, new_status):
    st.session_state.tasks[index]['task'] = new_task
    st.session_state.tasks[index]['status'] = new_status
def delete_task(index):
    st.session_state.tasks.pop(index)
def toggle_completion(index):
    if st.session_state.tasks[index]['status'] != 'Completed':
        st.session_state.tasks[index]['status'] = 'Completed'
    else:
        st.session_state.tasks[index]['status'] = 'Not Started'
st.title("✅ To-do App with Status and Completion")
with st.form(key='add_task_form'):
    new_task = st.text_input('Add Task')
    new_status = st.selectbox('Status', ['Not Started', 'In Progress', 'Completed'])
    add_task_button = st.form_submit_button('Add Task')
    if add_task_button and new_task:
        add_task(new_task, new_status)
        st.success(f'Task "{new_task}" added with status "{new_status}"!')
if st.session_state.tasks:
    st.write("### Your Tasks")
    for i, task in enumerate(st.session_state.tasks):
        cols = st.columns([0.1, 0.6, 0.2, 0.1])
        completed_checkbox = cols[0].checkbox(
            "",
            value=(task['status'] == 'Completed'),
            key=f"checkbox_{i}",
            on_change=toggle_completion,
            args=(i,)
        )
        if task['status'] == 'Completed':
            cols[1].markdown(f"~~{task['task']}~~")
        else:
            cols[1].markdown(task['task'])
        cols[2].markdown(f"**Status:** {task['status']}")
        if cols[3].button("🗑️", key=f"delete_{i}"):
            delete_task(i)
            st.experimental_rerun()
    task_number = st.number_input(
        'Select Task Number to Edit',
        min_value=1,
        max_value=len(st.session_state.tasks),
        step=1,
        key='task_number'
    )
    with st.form(key='edit_task_form'):
        edit_task_input = st.text_input(
            'Edit Task Description',
            value=st.session_state.tasks[task_number - 1]['task'],
            key='edit_task_input'
        )
        edit_status_input = st.selectbox(
            'Edit Status',
            ['Not Started', 'In Progress', 'Completed'],
            index=['Not Started', 'In Progress', 'Completed'].index(
                st.session_state.tasks[task_number - 1]['status']
            ),
            key='edit_status_input'
        )
        edit_button = st.form_submit_button('Update Task')
        if edit_button and edit_task_input:
            edit_task(task_number - 1, edit_task_input, edit_status_input)
            st.success(f'Task {task_number} updated!')
            st.rerun()
else:
    st.write("No tasks yet. Add some!")







