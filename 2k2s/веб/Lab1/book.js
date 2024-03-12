const modal = document.getElementById("modal");
const greens = document.getElementsByClassName(
    "text-center h-12 w-12 flex items-center justify-center py-2 bg-green-500 text-white rounded cursor-pointer hover:bg-green-700"
);

const accBtn = document.querySelector(".accept-button");
const cnclBtn = document.querySelector(".cancel-button");

accBtn.addEventListener("click", () => {
    toggleModal();
    setTimeout(() => {
        alert("You booked a room");
    }, 500);
});

cnclBtn.addEventListener("click", toggleModal);

[...greens].forEach((item) => {
    item.addEventListener("click", toggleModal);
});

modal.addEventListener("click", (e) => {
    if (e.target == modal) {
        toggleModal();
    }
});

function toggleModal() {
    modal.classList.toggle("hidden");
    document.body.classList.toggle("overflow-hidden");
}