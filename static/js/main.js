$("document").ready(function () {
    AOS.init();
    
    $('.toast').toast('show');
    
    /*
    $(".image-product-1").on("click", function () {
        $(this).addClass("testjs");
    });    */


    //On click scroll to top
    window.onscroll = function() {visiblebutton()};
    function visiblebutton() {
        if ($('window').scrollTop() > 10) {
            $("#scroll-top-button").css("color", "black");
        }
    }
  

    //When clicked, window will scroll to the top page
    $('#scroll-top-button').on("click", function() {
        window.scrollTo(0,0)
    })
});





