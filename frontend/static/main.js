const toggleSnippet = (list, titleAsClass) => {
  list
    .filter((element) => element.pk !== titleAsClass)
    .map((element) => {
      const otherElements = document.getElementById(element.pk);
      if (otherElements.style.display === "block") {
        otherElements.style.display = "none";
      }
    });

  const clickedElement = document.getElementById(titleAsClass);

  if (clickedElement.style.display === "none") {
    clickedElement.style.display = "block";
  } else {
    clickedElement.style.display = "none";
  }
};
