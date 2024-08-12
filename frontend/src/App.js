const resizeMain = () => {
  const header = document.querySelector("header");
  const footer = document.querySelector("footer");

  if (header && footer) {
    document.documentElement.style.setProperty(
      "--header-height",
      `${header.offsetHeight}px`
    );
    document.documentElement.style.setProperty(
      "--footer-height",
      `${footer.offsetHeight}px`
    );
  }
};

export { resizeMain };
