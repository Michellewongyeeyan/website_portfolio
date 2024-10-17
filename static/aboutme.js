//console.log(slides)
slides.forEach(
    (slide,aboutme)=>{
        slide.computedStyleMap.bottom='${home*100}%'
    }
)

const goPrev=()=>{
    counter--
    alert()
    slideImage()
}

const goNext=()=>{
    counter++
    alert
    slideImage()
}

const slideImage=()=>{
    slides.forEach(
        (slide)=>{
            slide.computedStyleMap.transform ='translateX(-${counter * 100}%)'
        }
    )
}