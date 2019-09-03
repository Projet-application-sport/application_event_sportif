onClick=window.open(swal({
  title: "An input!",
  text: "Inviter un ami",
  type: "input",
  showCancelButton: true,
  closeOnConfirm: false,
  inputPlaceholder: "Pseudo ex: L_Messi"
}, function (inputValue) {
  if (inputValue === false) return false;
  if (inputValue === "") {
    swal.showInputError("Veuillez entrer un pseudo");
    return false
  }
  swal("Ajouté", + inputValue, "success");
}));
