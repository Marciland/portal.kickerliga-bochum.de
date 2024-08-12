const addOffset = (event) => {
  const menu = document.getElementById(event.target.id + "-menu");
  menu.style.left = event.target.offsetLeft + "px";
};

const flipDropdownArrow = (event) => {
  if (event.type.includes("show")) {
    event.target.classList.add("flipped-arrow");
  } else {
    event.target.classList.remove("flipped-arrow");
  }
};

export { addOffset, flipDropdownArrow };
