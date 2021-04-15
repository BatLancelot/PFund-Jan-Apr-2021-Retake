todo_notes_list = []

while True:
    todo_note = input()
    if todo_note == 'End':
        break
    else:
        note_part = todo_note.split('-', maxsplit=1)
        priority = int(note_part[0])
        note = note_part[1]
        todo_notes_list.append((priority, note))

final_ordered_todo_list = []


def sort_by_priority_fn(todo_notes_list):
    return todo_notes_list[0]


for priority, note in sorted(todo_notes_list, key=sort_by_priority_fn):
    final_ordered_todo_list.append(note)

print(final_ordered_todo_list)
