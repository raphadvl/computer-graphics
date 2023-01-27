#version 400

layout (location=0) in vec3 position;
layout (location=1) in vec2 textureCoord;
layout (location=2) in vec3 normal;
uniform mat4 MVP;
out float intensity;

void main(void) 
{   
    vec3 lightDir = normalize(vec3(10.0,0.0,0.0));
    intensity = dot(lightDir,normalize(normal));
    gl_Position = MVP * vec4(position,1.0);
}