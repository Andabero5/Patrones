


# **Singleton**

*Singleton* es un patrón de diseño de creación que le permite asegurarse de que una clase solo tiene una instancia, al tiempo que proporciona un punto de acceso global a esta instancia.

  - [**Problema**](#problema)
  - [**Solución**](#solución)
  - [**Ejemplo**](#ejemplo)
  - [**Aplicaciones**](#aplicaciones)
  - [**Pros**](#pros)
  - [**Contras**](#contras)
  - [**Relaciones con otros patrones**](#relaciones-con-otros-patrones)
## **Problema**

El patrón *Singleton* resuelve dos problemas al mismo tiempo, violando el principio de responsabilidad única:

1. Una clase tiene una sola instancia. ¿Por qué alguien querría controlar cuántas instancias tiene una clase? La razón más común para esto es controlar el acceso a algún recurso compartido, por ejemplo, una base de datos o un archivo.

    Así es como funciona: imagina que creaste un objeto, pero después de un tiempo decidiste crear uno nuevo. En lugar de recibir un objeto nuevo, obtendrá el que ya se ha creado.

    Tenga en cuenta que este comportamiento es imposible de implementar con un constructor normal, ya que una llamada al constructor siempre debe devolver un nuevo objeto por diseño.

2. Punto de acceso global a esa instancia. Las variables globales usadas para almacenar algunos objetos esenciales, aunque son muy prácticas, también son muy inseguras, ya que cualquier código puede sobrescribir potencialmente el contenido de esas variables y bloquear la aplicación.

    Al igual que una variable global, el patrón *Singleton* le permite acceder a algún objeto desde cualquier lugar del programa. Sin embargo, también protege esa instancia de ser sobrescrita por otro código.

    Hay otro lado en este problema: no quieres que el código que resuelve el problema #1 se disperse por todo el programa. Es mucho mejor tenerlo dentro de una clase, especialmente si el resto del código ya depende de él.

Hoy en día, el patrón *Singleton* se ha vuelto tan popular que la gente puede llamar a algo un *singleton* incluso si resuelve sólo uno de los problemas enumerados.

## **Solución**

Todas las implementaciones del *Singleton* tienen estos dos pasos en común:

- El constructor predeterminado sera privado, para evitar que otros objetos usen el nuevo operador con la clase *Singleton*.

- Se creara un método de creación estático que actúe como constructor. Por debajo, este método llama al constructor privado para crear un objeto y lo guarda en un campo estático. Todas las llamadas siguientes a este método devuelven el objeto almacenado en caché.
  
Si el código tiene acceso a la clase *Singleton*  a continuación, es capaz de llamar al método estático *Singleton*. Por lo tanto, siempre que se llama a ese método, siempre se devuelve el mismo objeto.

## **Ejemplo**

En este ejemplo, la clase de conexión de base de datos actúa como *Singleton*. Esta clase no tiene un constructor público, por lo que la única manera de obtener su objeto es llamar al método *get_instance*. Este método almacena en caché el primer objeto creado y lo devuelve en todas las llamadas posteriores.

## **Aplicaciones**

- Se utiliza el patrón *Singleton* cuando una clase del programa debe tener una sola instancia disponible para todos los clientes; por ejemplo, un único objeto de base de datos compartido por diferentes partes del programa.

  - El patrón *Singleton* deshabilita todos los demás medios de creación de objetos de una clase, excepto el método de creación especial. Este método crea un nuevo objeto o devuelve uno existente si ya se ha creado.

- El patrón *Singleton* es usado cuando se necesite un control más estricto sobre las variables globales.

  - A diferencia de las variables globales, el patrón *Singleton* garantiza que solo hay una instancia de una clase. Nada, excepto la propia clase *Singleton*, puede reemplazar la instancia almacenada en caché.

  - Tenga en cuenta que siempre puede ajustar esta limitación y permitir la creación de cualquier número de instancias *Singleton*. El único fragmento de código que necesita cambiar es el cuerpo del método.

## **Pros**

- Puede estar seguro de que una clase solo tiene una instancia.
  
- Obtendrá un punto de acceso global a esa instancia.
  
- El objeto *singleton* se inicializa solo cuando se solicita por primera vez.

## **Contras**

- Viola el Principio de Responsabilidad Única. El patrón resuelve dos problemas en ese momento.

- El patrón *Singleton* puede enmascarar un mal diseño, por ejemplo, cuando los componentes del programa saben demasiado entre sí.

- El patrón requiere un tratamiento especial en un entorno multiproceso para que varios subprocesos no creen un objeto *singleton* varias veces.

- Puede ser difícil probar unitariamente el código de cliente de *Singleton* porque muchos marcos de pruebas dependen de la herencia al producir objetos ficticios. Dado que el constructor de la clase *singleton* es privado y reemplazar métodos estáticos es imposible en la mayoría de los lenguajes, tendrá que pensar en una forma creativa de simular el *singleton*.

## **Relaciones con otros patrones**

- Una clase Facade a menudo se puede transformar en un *Singleton* ya que un único objeto de facade es suficiente en la mayoría de los casos.

- Flyweight se parecería a *Singleton* si de alguna manera lograste reducir todos los estados compartidos de los objetos a un solo objeto flyweight. Pero hay dos diferencias fundamentales entre estos patrones:

  - Debe haber solo una instancia *singleton*, mientras que una clase Flyweight puede tener varias instancias con diferentes estados intrínsecos.

  - El objeto *Singleton* puede ser mutable. Los objetos Flyweight son inmutables.

- Las *Abstract Factories*, los *Builders* y los *Prototype* se pueden implementar como *Singletons*.