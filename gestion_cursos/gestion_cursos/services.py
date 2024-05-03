from .models import Estudiante, Profesor, Curso, Direccion

def crear_curso(nombre, codigo, version, profesor_id):
    curso = Curso.objects.create(nombre=nombre, codigo=codigo, version=version)
    if profesor_id:
        profesor = Profesor.objects.get(rut=profesor_id)
        curso.profesor = profesor
        curso.save()
    return curso

def crear_profesor(rut, nombre, apellido, activo=False, creado_por=None):
    return Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)

def crear_estudiante(rut, nombre, apellido, fecha_nac, activo=False, creado_por=None):
    return Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)

def crear_direccion(estudiante_id, calle, numero, comuna, ciudad, region, dpto=None):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    return Direccion.objects.create(estudiante=estudiante, calle=calle, numero=numero, comuna=comuna, ciudad=ciudad, region=region, dpto=dpto)

def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def agrega_profesor_a_curso(curso_codigo, profesor_rut):
    curso = Curso.objects.get(codigo=curso_codigo)
    profesor = Profesor.objects.get(rut=profesor_rut)
    curso.profesor = profesor
    curso.save()

def agrega_cursos_a_estudiante(estudiante_rut, curso_codigos):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = Curso.objects.filter(codigo__in=curso_codigos)
    estudiante.cursos.add(*cursos)

def imprime_estudiante_cursos(estudiante_rut):
    estudiante = Estudiante.objects.get(rut=estudiante_rut)
    cursos = estudiante.cursos.all()
    cursos_nombres = [curso.nombre for curso in cursos]
    return cursos_nombres