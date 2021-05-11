const titreSpans = document.querySelectorAll('centre')

window.addEventListener('load' , () =>{

    const TL = gsap.timeline({paused: true});

    TL.staggerFrom(titreSpans, 1, {top: -50, opacity: 0, ease: "power2.out"}, 0.3)

    TL.play();
})