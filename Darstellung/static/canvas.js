function handleSearch(e) {
  const term = e.target.value.toLowerCase().trim();
  const items = document.querySelectorAll("ul li");

  if (!term) {
    items.forEach((li) => li.classList.remove("is-hidden"));
    return;
  }

  items.forEach((li) => {
    const parts = li.textContent.split(" +++ ");
    const title = (parts.length > 1 ? parts.slice(1).join(" +++ ") : li.textContent).toLowerCase();

    const match = title.includes(term);
    li.classList.toggle("is-hidden", !match);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const searchBar = document.getElementById("search-bar");
  if (!searchBar) return;

  searchBar.addEventListener("input", handleSearch);

  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      searchBar.focus();
    }
  });
});
