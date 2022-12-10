#version 400

in vec2 textureCoord;
out vec4 color;
uniform sampler2D textureSlot;

void main(void) 
{
    vec4 vermelho = vec4(1.0,0.0,0.0,1.0);
    color = vermelho*0.7 + 0.3*texture(textureSlot,textureCoord);
}
