

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
    u_gradient_bottom (1.3, 1.0, 0.8, 1.0)


label testDaGradiants:

    scene clearDayTime at fullFit , duskMorningGradient
    "hehe"
    show secondSubversionBaseRuins at fullFit , duskLights
    "the testicles lolololololol"
    return