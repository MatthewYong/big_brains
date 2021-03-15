$("document").ready(function () {
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
