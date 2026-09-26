function openEdit(id, name, age, branch, address, email) {
  document.getElementById('edit_id').value = id;
  document.getElementById('edit_name').value = name;
  document.getElementById('edit_age').value = age;
  document.getElementById('edit_branch').value = branch;
  document.getElementById('edit_address').value = address;
  document.getElementById('edit_email').value = email;

  const modalElement = document.getElementById('editModal');
  const editModal = new bootstrap.Modal(modalElement);
  editModal.show();
}