function dragstartHandler(ev) {
  try
  {
    ev.dataTransfer.setData("zettel", ev.target.id);
  }
  catch (error)
  {
    console.error(error);
  }
}

function dragoverHandler(ev) {
  ev.preventDefault();
}

function dropHandler(ev) {
    const data = ev.dataTransfer.getData("zettel");
    const element = document.getElementById(data);

    if (!element) {
      console.warn("Kein Element für ID gefunden:", data);
      return;
    }
    ev.target.appendChild(element);
}

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
