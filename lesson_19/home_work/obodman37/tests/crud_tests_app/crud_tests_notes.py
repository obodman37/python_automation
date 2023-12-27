def add_notes(notes_app, n):
    for i in range(n + 1):
        notes_app.add_note(f'Test note {i}')

def test_create_note(notes_app):
    number_of_notes = len(notes_app.get_all_notes())
    assert "Note added successfully" == notes_app.add_note("Test note content")
    assert len(notes_app.get_all_notes()) == number_of_notes + 1

def test_read_note(notes_app):
    add_notes(notes_app, 1)
    assert notes_app.get_note(0) == "Test note 0"

def test_update_note(notes_app):
    add_notes(notes_app, 1)
    notes_app.edit_note(0, "Updated note content")
    assert "Updated note content" == notes_app.get_note(0)