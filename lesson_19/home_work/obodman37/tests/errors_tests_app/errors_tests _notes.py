
def add_notes(notes_app, n):
    for i in range(n + 1):
        notes_app.add_note(f'Test note {i}')

def test_create_note(notes_app):
    number_of_notes = len(notes_app.get_all_notes())
    assert "Note added successfully" == notes_app.add_note("Test note content")
    assert len(notes_app.get_all_notes()) == number_of_notes + 1

def test_read_note_out_of_range(notes_app):
    result = notes_app.get_note(0)
    assert result == "Index out of range"

def test_update_note_out_of_range(notes_app):
    result = notes_app.edit_note(0, "Updated note content")
    assert result == "Index out of range"

def test_delete_note_out_of_range(notes_app):
    result = notes_app.delete_note(0)
    assert result == "Index out of range"