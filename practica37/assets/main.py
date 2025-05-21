import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros Iniciales ---

# Dimensiones de la imagen y parámetros de la esfera
img_size = 400
radius = 1.0
center = np.array([0.0, 0.0, 0.0]) # Asumiendo centro en el origen para simplificar normales

# Parámetros de iluminación
ambient_intensity = 0.2          # Componente ambiental global
kd = 0.7                         # Coeficiente difuso del material
ks = 0.5                         # Coeficiente especular del material
specular_exponent = 32           # Exponente para el brillo especular (shininess)

# Posición de la fuente de luz y del observador (cámara)
light_pos = np.array([2.0, 2.0, 2.0])
eye_pos = np.array([0.0, 0.0, 5.0]) # Observador en el eje Z positivo

# Color del objeto (AHORA AZUL) y del highlight especular (blanco)
object_color = np.array([0.0, 0.0, 1.0]) # <--- CAMBIO AQUÍ: Color Azul
specular_color = np.array([1.0, 1.0, 1.0]) # Ks implícito en este color

# --- Preparación de la Geometría y la Imagen ---

# Crear una cuadrícula 2D representando la proyección en el plano XY
x = np.linspace(-radius, radius, img_size)
y = np.linspace(-radius, radius, img_size)
X, Y = np.meshgrid(x, y)

# Inicializar la imagen (RGB)
image = np.zeros((img_size, img_size, 3))

# Calcular la coordenada z de la esfera
z_squared = radius**2 - X**2 - Y**2
Z = np.sqrt(np.maximum(0, z_squared))

# Crear una máscara para los puntos que pertenecen a la esfera
mask = X**2 + Y**2 <= radius**2

# Posición de cada punto en la superficie visible de la esfera
points = np.stack([X, Y, Z], axis=-1)

# --- Cálculo de Normales ---

# Normal en cada punto de la esfera (vector unitario)
normals = np.zeros_like(points)
# Calcular normales solo para los puntos dentro de la máscara
normals[mask] = points[mask] / radius

# --- Función Auxiliar ---

# Función para normalizar vectores
def normalize(v):
    norm = np.linalg.norm(v, axis=-1, keepdims=True)
    # Usar np.finfo para un epsilon pequeño y evitar división por cero
    norm = np.maximum(norm, np.finfo(float).eps)
    return v / norm

# --- Cálculos de Iluminación (Vectorizados donde sea posible) ---

# Calcular vectores de luz (L) y vista (V) para cada punto de la esfera
# Aplicar solo a los puntos válidos usando la máscara

# Vector de luz: desde el punto hasta la fuente de luz
L = light_pos - points[mask]
L = normalize(L)

# Vector de vista: desde el punto hasta la posición del observador
V = eye_pos - points[mask]
V = normalize(V)

# Acceder a las normales solo para los puntos válidos
N = normals[mask] # Ya están normalizadas

# Calcular la reflexión para el modelo Phong: R = 2*(N·L)*N - L
dot_NL = np.sum(N * L, axis=-1, keepdims=True)
# Clampear N·L >= 0 *antes* de calcular R para evitar reflejos extraños de luz "trasera"
dot_NL_clamped = np.maximum(0.0, dot_NL)
R = 2 * dot_NL_clamped * N - L
R = normalize(R)

# Calcular cada componente de la iluminación para los puntos en la máscara

# Componente ambiental
ambient = ambient_intensity

# Componente difusa (según Lambert)
# kd * max(0, N · L)
# Usamos el dot_NL_clamped calculado antes
diffuse_intensity = kd * dot_NL_clamped.squeeze() # .squeeze() para quitar la dimensión extra
diffuse = diffuse_intensity # Renombrado para claridad, ahora es escalar por punto

# Componente especular (modelo Phong)
# ks * max(0, R · V) ^ specular_exponent
dot_RV = np.sum(R * V, axis=-1) # R·V por punto
specular_intensity = ks * (np.maximum(0.0, dot_RV) ** specular_exponent)
specular = specular_intensity # Renombrado para claridad, ahora es escalar por punto

# --- Combinar Componentes y Asignar Colores ---

# Combinar componentes para obtener el color final por píxel
shading = np.zeros((mask.sum(), 3)) # Array para guardar el color calculado

# Para cada canal (R, G, B)
for c in range(3):
    # Color = Amb*ObjCol + Diff*ObjCol + Spec*SpecCol
    # Asegurarse que diffuse y specular tengan la forma correcta para broadcasting si es necesario
    # (aunque con squeeze y axis=-1 deberían ser 1D arrays de tamaño mask.sum())
    shading[:, c] = ambient * object_color[c] + diffuse * object_color[c] + specular * specular_color[c]

# Solo asignar color a los píxeles que pertenecen a la esfera
final_image = np.zeros_like(image) # Imagen final inicializada a negro
final_image[mask] = shading # Asignar los colores calculados a los píxeles de la máscara

# Asegurarse que los valores estén en el rango [0,1]
final_image = np.clip(final_image, 0, 1)

# --- Mostrar el resultado ---
plt.figure(figsize=(6, 6))
plt.imshow(final_image)
plt.axis('off')
plt.title('Iluminación Combinada: Ambiental, Difusa y Especular (Azul)')
plt.show()
