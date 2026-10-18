document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".mobile-menu");
  const nav = document.querySelector(".nav-links");
  if (menuButton && nav) {
    menuButton.addEventListener("click", () => {
      const open = nav.classList.toggle("nav-open");
      menuButton.setAttribute("aria-expanded", String(open));
    });
  }

  document.querySelectorAll('input[type="number"]').forEach((input) => {
    input.addEventListener("change", () => {
      const min = Number(input.min || 0);
      const max = Number(input.max || 9999);
      let value = Number(input.value || min);
      if (!Number.isFinite(value)) value = min;
      input.value = String(Math.min(max, Math.max(min, value)));
    });
  });
});
