/**
* Template Name: Moderna - v4.1.0
* Template URL: https://bootstrapmade.com/free-bootstrap-template-corporate-moderna/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  });

})()

function upDate(previewPic)
{
	 var element=document.getElementById("image");
	 element.style.background="url(" + previewPic.src + ")";
	 element.style.backgroundSize="100% 100%";
}
function upDates(previewPic)
{
	 var element=document.getElementById("images");
	 element.style.background="url(" + previewPic.src + ")";
	 element.style.backgroundSize="100% 100%";
}
