let activeCategory = "all";
let activeNamespace = "all";

// Called after changing either the category or the namespace
function applyFilters() {
  const items = document.getElementsByClassName("filterDiv");
  for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const itemClasses = item.className.split(" ");

    // Check category
    const matchesCategory =
      activeCategory === "all" || itemClasses.includes(activeCategory);
    // Check namespace
    const matchesNamespace =
      activeNamespace === "all" || itemClasses.includes(activeNamespace);

    // Show item only if it matches both
    if (matchesCategory && matchesNamespace) {
      item.classList.add("show");
    } else {
      item.classList.remove("show");
    }
  }
}

function initFilters() {
  // Category button clicks
  const catBtnContainer = document.getElementById("cmapCategoryButtons");
  if (catBtnContainer) {
    const catBtns = catBtnContainer.getElementsByClassName("btn");
    for (let btn of catBtns) {
      btn.addEventListener("click", function() {
        // Remove 'active' from existing
        for (let b of catBtns) {
          b.classList.remove("active");
        }
        // Set 'active' on the clicked button
        this.classList.add("active");
        // Update the filter
        activeCategory = this.getAttribute("data-filter-cat");
        applyFilters();
      });
    }
  }

  // Namespace button clicks
  const nsBtnContainer = document.getElementById("cmapNamespaceButtons");
  if (nsBtnContainer) {
    const nsBtns = nsBtnContainer.getElementsByClassName("btn");
    for (let btn of nsBtns) {
      btn.addEventListener("click", function() {
        // Remove 'active' from existing
        for (let b of nsBtns) {
          b.classList.remove("active");
        }
        // Set 'active' on the clicked button
        this.classList.add("active");
        // Update the filter
        activeNamespace = this.getAttribute("data-filter-ns");
        applyFilters();
      });
    }
  }

  // Initialize on load
  applyFilters();
}

document.addEventListener("DOMContentLoaded", initFilters);