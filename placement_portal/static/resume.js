// select modal-btn,modal-overlay,close-btn
// listen for click events on modal-btn and close-btn
// when user clicks modal-btn add .open-modal to modal-overlay
// when user clicks close-btn remove .open-modal from modal-overlay

const mbtn = document.querySelector(".modal-btn");
const modaloverlay = document.querySelector(".modal-overlay");
const closebtn = document.querySelector(".close-btn");
mbtn.addEventListener("click", function () {
  modaloverlay.classList.add("open-modal");
});
closebtn.addEventListener("click", function () {
  modaloverlay.classList.remove("open-modal");
});
