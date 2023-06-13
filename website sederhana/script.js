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
