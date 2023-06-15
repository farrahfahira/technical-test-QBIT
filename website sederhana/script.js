// menu slider

function scrollCarousel(direction) {
  const carouselWrapper = document.querySelector(".carousel-wrapper");
  const carouselWidth = carouselWrapper.offsetWidth;
  const itemWidth = carouselWidth / 3;

  if (direction === "prev") {
    carouselWrapper.style.transform = `translateX(${itemWidth}px)`;
    carouselWrapper.appendChild(carouselWrapper.firstElementChild);
  } else if (direction === "next") {
    carouselWrapper.style.transform = `translateX(-${itemWidth}px)`;
    carouselWrapper.prepend(carouselWrapper.lastElementChild);
  }
}

// accordion FAQ

const accordionItems = document.querySelectorAll(".accordion-item");

accordionItems.forEach((item) => {
  const header = item.querySelector(".accordion-header");

  header.addEventListener("click", () => {
    item.classList.toggle("accordion-open");

    if (item.classList.contains("accordion-open")) {
      closeOtherItems(item);
    }
  });
});

function closeOtherItems(currentItem) {
  accordionItems.forEach((item) => {
    if (item !== currentItem && item.classList.contains("accordion-open")) {
      item.classList.remove("accordion-open");
    }
  });
}
