#version 400

in float intensity;

void main(void) 
{   
    gl_FragColor = max(intensity,0.2) * vec4(0.0,0.0,0.7,0.0);
}