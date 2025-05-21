// Vertex Shader
#version 140

in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;

out vec2 texcoord;

uniform mat4 p3d_ModelViewProjectionMatrix;

void main() {
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
    texcoord = p3d_MultiTexCoord0;
}

// Fragment Shader
#version 140

in vec2 texcoord;
out vec4 fragColor;

uniform sampler2D p3d_Texture0;

void main() {
    // Отразить текстуру для создания зеркального эффекта
    vec2 flipped_texcoord = vec2(texcoord.x, 1.0 - texcoord.y);
    fragColor = texture(p3d_Texture0, flipped_texcoord);
}