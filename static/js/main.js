$("document").ready(function () {
    AOS.init();
    
    $('.toast').toast('show');
    
    /*
    $(".image-product-1").on("click", function () {
        $(this).addClass("testjs");
    });    */


    /*On click scroll to top*/
    $('#scroll-top-button').on("click", function() {
        window.scrollTo(0,0)
    })
});



