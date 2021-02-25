$("document").ready(function () {
    AOS.init();


    //Show toast messages throughout the website
    $('.toast').toast('show');

    //When scrolled make button visible after 300px
    //Within 300px button will be hide
    window.onscroll = function () { scrollButtonVisible() };
    function scrollButtonVisible() {
        if ($('body,html').scrollTop() < 300) {
            $("#scroll-top-button").css("display", "none");
        } else {
            if ($('body,html').scrollTop() > 300) {
                $("#scroll-top-button").css("display", "block");
            }
        }
    }


    //When clicked, window will scroll to the top page
    $('#scroll-top-button').on("click", function () {
        window.scrollTo(0, 0);
    })


    //Test owl carousel
    $('.owl-carousel').owlCarousel({
        items:3,
        loop:true,
        margin:5,
        nav:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });

});





