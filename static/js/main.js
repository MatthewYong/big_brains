$("document").ready(function () {
    AOS.init();


    //Show toast messages throughout the website
    $('.toast').toast('show');


    //Show and hide contact popup when link is clicked
    $('#show-contact-form').click(function() {
        $(".contact-form").css("display", "block");
        return false;
    });

    $('#hide-contact-form').click(function() {
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
        autoplay:true,
        autoplaySpeed:2000,
        autoplayTimeout:4000,
        autoplayHoverPause:true,
        center:true,
        margin:5,
        nav:false,
        dots:true,
        animateOut: 'fadeOut',
        responsive:{
            0:{
                items:1,
                loop:false
            },
            600:{
                items:3,
                loop:true
            },
            1000:{
                items:3,
                dotsEach:10,                
                loop:true
            }
        }
    });


//Owl carousel for blogs
    $('#blog-carousel').owlCarousel({
        items:1,
        center:true,
        margin:50,
        nav:true,
        dots:false,
        loop:true,
        autoWidth:true,
    });




    //Glidejs carousel for blogs
    var carouselConfig = {
    type: 'carousel',
    perView: 3,
    focusAt: 'center',
    autoplay: 3000,
    gap: 50,
    }

    new Glide('.glide', carouselConfig).mount();

});







