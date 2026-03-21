

#shaders.rpy

#this is for complicated shading and gradient tints

#activate the gl2 renderer
#define config.gl2 = True

#this is the two gradients
init python:
    # Registers a shader that tints from top to bottom
    renpy.register_shader("gradiants.vertical_gradient", variables="""
        uniform vec4 u_gradient_top;
        uniform vec4 u_gradient_bottom;
        uniform vec2 u_model_size;
        varying float v_gradient_progress;
        attribute vec4 a_position;
    """, vertex_300="""
        v_gradient_progress = a_position.y / u_model_size.y;
    """, fragment_300="""
        float gradient_done = v_gradient_progress;
        gl_FragColor *= mix(u_gradient_top, u_gradient_bottom, gradient_done);
    """)

#the example on the renpy documentation is of a horizonantal one
    renpy.register_shader("gradiants.gradient", variables="""
        uniform vec4 u_gradient_left;
        uniform vec4 u_gradient_right;
        uniform vec2 u_model_size;
        varying float v_gradient_done;
        attribute vec4 a_position;
    """, vertex_300="""
        v_gradient_done = a_position.x / u_model_size.x;
    """, fragment_300="""
        float gradient_done = v_gradient_done;
        gl_FragColor *= mix(u_gradient_left, u_gradient_right, gradient_done);
    """)

    renpy.register_shader("gradiants.two_thirds_gradient", variables="""
        uniform vec4 u_gradient_top;
        uniform vec4 u_gradient_bottom;
        uniform vec2 u_model_size;
        varying float v_gradient_progress;
        attribute vec4 a_position;
    """, vertex_300="""
        v_gradient_progress = a_position.y / u_model_size.y;
    """, fragment_300="""
        // Shift the transition so the bottom color starts appearing at 1/3rd height
        // and is fully solid by the time it hits the bottom 2/3rds.
        float transition = clamp((v_gradient_progress - 0.0) / 0.33, 0.0, 1.0);
        
        gl_FragColor *= mix(u_gradient_top, u_gradient_bottom, transition);
    """)

transform duskMorningGradient:
    shader "gradiants.two_thirds_gradient"
    # Red at the top (R=1.0, G=0.0, B=0.0, Alpha=1.0)
    u_gradient_top (-0.3, -0.3, 0.0, 1.0)
    # Blue at the bottom (R=0.0, G=0.0, B=1.0, Alpha=1.0)
    u_gradient_bottom (1.3, 0.95, 0.8, 1.0)

transform starReavalTopGradient:
    shader "gradiants.two_thirds_gradient"
    # yes stars
    u_gradient_top (0.5, 0.5, 0.5, 1.0)
    # no stars
    u_gradient_bottom (1.3, 0.95, 0.8, 0.0)

transform topShineGradient:
    shader "gradiants.two_thirds_gradient"
    # yes stars
    u_gradient_top (0.5, 0.5, 0.5, 1.0)
    # no stars
    u_gradient_bottom (1.3, 0.95, 0.8, 1.0)

transform darkShade:
    shader "gradiants.vertical_gradient"
    # Red at the top (R=1.0, G=0.0, B=0.0, Alpha=1.0)
    u_gradient_top (1.3, 0.95, 0.8, 1.0)
    # Blue at the bottom (R=0.0, G=0.0, B=1.0, Alpha=1.0)
    u_gradient_bottom (0.4, 0.3, 0.0, 1.0)


label testDaGradiants:

    scene clearDayTime at fullFit , duskMorningGradient with fade
    "hehe"
    show light at center:
        matrixcolor TintMatrix( "#97d6ff") * BrightnessMatrix( 0.6 )
        ypos 0.95
    show secondSubversionBaseRuins at fullFit , darkShade
    with dissolve
    "the testicles lolololololol"


    #delete or comment out when done testing images for webp issues caused by krita
    #up to the harem ladies 
    #mr malik
    #atazera
    scene xartabanaThoneRoom at center
    show atazeraImg at center , halfSize
    with fade
    "atazera"
    show atazeraImg item happy mean  
    "hehe"
    show atazeraImg point O
    "o"
    show atazeraImg greet closedEyes frown
    "dsds"
    show atazeraImg training mean angry
    "beat yo ass"
    show atazeraImg sadEyes
    "sadge"

    show atazeraImg armored neutral neutralHappy
    with fade
    "atazera with armor"
    show atazeraImg armoredItem mean happy
    "hehe"
    show atazeraImg armoredPoint O
    "o"
    show atazeraImg armoredGreet closedEyes frown
    "dsds"
    show atazeraImg armoredBattle mean angry
    "beat yo ass"
    show atazeraImg sadEyes
    "sadge"

    scene balatiusPalaceHaremGirlRoom at fullFit
    show muwaHarem at left, halfSize
    show orodianHaremLady at right , halfSize
    show balaAstartWhippaLady at center , halfSize
    with fade
    "harem girls"

    show muwaHarem greet happy
    hide orodianHaremLady
    show orodianHaremLadyItem at right , halfSize
    show balaAstartWhippaLady annoyed
    "talking"

    hide orodianHaremLadyItem with dissolve
    show muwaHarem inviting mean extraHappy
    show balaAstartWhippaLady armed angry
    "angry lady"

    show muwaHarem sad O
    "sad muwa"

    show muwaHarem horny blush
    show balaAstartWhippaLady base neutralHappy:
        linear 2 xpos 0.75
    "they have an idea."

    scene clearDayTime at duskMorningGradient with fade
    show astaJamesianBoarderModular at fullFit , darkShade , right 
    show atazeraImg schytedChariot at quatSize , center:
        matrixcolor TintMatrix("#ffdbb9")
    with fade
    "Atazera on her chaiort"
    show atazeraImg armoredBattle
    "with armor"

    return