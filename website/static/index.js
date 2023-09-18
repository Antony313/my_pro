function deleteNote(noteId) {
  console.log("Deleting note with ID:", noteId);
  fetch(`/delete-note/${noteId}`, {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
    headers: {
      'Content-Type': 'application/json'
    }
  }).then((_res) => {
    console.log("Note deleted.");
    window.location.href = "/";
  });
}
