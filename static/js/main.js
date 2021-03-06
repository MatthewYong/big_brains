$("document").ready(function () {
    AOS.init();


    //Show toast messages throughout the website
    $('.toast').toast('show');


    //Show and hide contact popup when link is clicked
    $('#show-contact-form').click(function () {
        $(".contact-form").css("display", "block");
        return false;
    });

    $('#hide-contact-form').click(function () {
        $(".contact-form").css("display", "none");
        return false;
    });


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


    //Owl carousel for toy products
    $('#toy-carousel').owlCarousel({
        autoplay: true,
        autoplaySpeed: 2000,
        autoplayTimeout: 4000,
        autoplayHoverPause: true,
        center: true,
        margin: 5,
        nav: false,
        dots: true,
        animateOut: 'fadeOut',
        responsive: {
            0: {
                items: 1,
                loop: false
            },
            800: {
                items: 2,
                loop: true
            },
            1200: {
                items: 3,
                loop: true
            }
        }
    });


    //Owl carousel for blogs
    $('#blog-carousel').owlCarousel({
        items: 1,     
        center: true,
        nav: true,
        dots: false,
        loop: true,
        autoWidth: false,        
        responsive: {
            0: {
                items: 1,
            },
            800: {
                items: 1,              
            },
            1200: {
                autoWidth: true,
                autoplay: true,
                autoplaySpeed: 4000,
                autoplayTimeout: 6000,                  
            }
        }        
    });
});







