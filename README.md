- [**Patrones creacionales**](#patrones-creacionales)
  - [**Abstract factory**](#abstract-factory)
    - [**Problema**](#problema)
    - [**Solución**](#solución)
    - [**Ejemplo**](#ejemplo)
    - [**Aplicaciones**](#aplicaciones)
    - [**Pros**](#pros)
    - [**Contras**](#contras)
    - [**Relaciones con otros patrones**](#relaciones-con-otros-patrones)
  - [**Builder**](#builder)
    - [**Problema**](#problema-1)
    - [**Solución**](#solución-1)
    - [**Clase director**](#clase-director)
    - [**Ejemplo**](#ejemplo-1)
    - [**Aplicaciones**](#aplicaciones-1)
    - [**Pros**](#pros-1)
    - [**Contras**](#contras-1)
    - [**Relaciones con otros patrones**](#relaciones-con-otros-patrones-1)
  - [**Singleton**](#singleton)
    - [**Problema**](#problema-2)
    - [**Solución**](#solución-2)
    - [**Ejemplo**](#ejemplo-2)
    - [**Aplicaciones**](#aplicaciones-2)
    - [**Pros**](#pros-2)
    - [**Contras**](#contras-2)
    - [**Relaciones con otros patrones**](#relaciones-con-otros-patrones-2)

# **Patrones creacionales**

## **Abstract factory**

Es un patrón de diseño creacional que permite producir familias de objetos relacionados sin especificar sus clases concretas.

### **Problema**

Imagina que estas creando un simulador de ceador de *drones*, El codigo consta de clases que representan:

1. Una familia de marcas relacionadas, por ejemplo: *DJI* y *Hubsand* 
2. Variantes de los componentes como lo pueden ser la camara, las helices y el chasis

Necesita una forma de crear objetos de *drones* individuales para que coincidan con otros objetos de la misma familia. Los clientes se enojan mucho cuando reciben piezas que no coinciden.

Además, no desea cambiar el código existente al agregar nuevos productos o familias de productos al programa. Los vendedores de *drones* actualizan sus catálogos muy a menudo, y no querrá cambiar el código principal cada vez que sucede.

### **Solución**

1. El patrón Abstract Factory sugiere declarar explícitamente interfaces para cada producto distinto de la familia de productos (por ejemplo, camara, chasis y helices). A continuación, puede hacer que todas las variantes de productos sigan esas interfaces. Por ejemplo, todas las variantes de camara pueden implementar la interfaz; todas las variantes de la chasis pueden implementar la interfaz, y así sucesivamente.

2. El siguiente paso es declarar la clase abstracta que es una interfaz con una lista de métodos de creación para todos los productos que forman parte de la familia de productos (por ejemplo,crear camara, crear chasis y crear helices). Estos métodos deben devolver tipos de productos abstractos representados por las interfaces que extrajimos anteriormente:helices, chasis, etc.

3. Ahora, ¿qué tal las variantes del producto? Para cada variante de una familia de productos, creamos una clase de fábrica independiente basada en la interfaz. Una fábrica es una clase que devuelve productos de un tipo determinado. Por ejemplo, *DJI* solo puede crear *ChassisDJI*, *CameraDJI* y *propellerDJI*.

El código de cliente tiene que trabajar con fábricas y productos a través de sus respectivas interfaces abstractas. Esto le permite cambiar el tipo de fábrica que se pasa al código de cliente, así como la variante de producto que recibe el código de cliente, sin interrumpir el código de cliente real.

Digamos que el cliente quiere una fábrica para producir una drone. El cliente no tiene que ser consciente de la clase de la fábrica, ni importa qué tipo de drone recibe. Ya sea un modelo DJI o una drone de *hubsand*, el cliente debe tratar todos los *drones* de la misma manera, utilizando la interfaz abstracta. Con este enfoque, lo único que el cliente sabe sobre el drone es que implementa el método de alguna manera. Además, cualquiera que sea la variante del drone que se devuelva, siempre coincidirá con el tipo de camara o chasis producido por el mismo objeto de fábrica.

Hay una cosa más que aclarar: si el cliente sólo está expuesto a las interfaces abstractas, ¿qué crea los objetos de fábrica reales? Normalmente, la aplicación crea un objeto de fábrica concreto en la etapa de inicialización. Justo antes de eso, la aplicación debe seleccionar el tipo de fábrica en función de la configuración o la configuración del entorno.

### **Ejemplo**

En este ejemplo se muestra cómo se puede usar el patrón de fábrica abstracta para crear elementos de *drones* sin acoplar el código de cliente a clases de interfaz de usuario concretas, manteniendo todos los elementos creados coherentes con un Drone seleccionado.

![UML Abstract Factory](AbstractFactory\Main.jpg)

Se espera que los mismos elementos de interfaz de usuario de un drone se comporten de forma similar, pero se vean un poco diferentes en diferentes marcas. Además, es su trabajo asegurarse de que los elementos de la interfaz de usuario coinciden con el estilo del drone actual. No querrás que el programa represente partes DJI cuando se ejecute en *Hubsand*.

La interfaz *Abstract Factory* declara un conjunto de métodos de creación que el código de cliente puede usar para generar diferentes tipos de elementos de interfaz de usuario. Las fábricas de concretas corresponden a partes específicas y crean los elementos de interfaz de usuario que coinciden con ese drone en particular.

Funciona así: cuando se inicia una aplicación, comprueba el tipo del drone actual. La aplicación utiliza esta información para crear un objeto de fábrica a partir de una clase que coincida con el drone. El resto del código usa este generador para crear elementos de interfaz de usuario. Esto evita que se creen los elementos incorrectos.

Con este enfoque, el código de cliente no depende de clases concretas de generadores y elementos de interfaz de usuario, siempre y cuando funcione con estos objetos a través de sus interfaces abstractas. Esto también permite que el código de cliente admita otros generadores o elementos de interfaz de usuario que podría agregar en el futuro.

Como resultado, no es necesario modificar el código de cliente cada vez que agregue una nueva variación de elementos de interfaz de usuario a la aplicación. Sólo tiene que crear una nueva clase de fábrica que produce estos elementos y modificar ligeramente el código de inicialización de la aplicación para que seleccione esa clase cuando corresponda.

### **Aplicaciones**

Utilice *Abstract Factory* cuando el código necesite trabajar con varias familias de productos relacionados, pero no desea que dependa de las clases concretas de esos productos, es posible que se desconozcan de antemano o que simplemente desee permitir la extensibilidad futura.

 *Abstract Factory* proporciona una interfaz para crear objetos de cada clase de la familia de productos. Siempre que el código cree objetos a través de esta interfaz, no tiene que preocuparse por crear la variante incorrecta de un producto que no coincide con los productos ya creados por la aplicación.

Considere la posibilidad de implementar *Abstract Factory* cuando tenga una clase con un conjunto de métodos de fábrica que difuminen su responsabilidad principal.

En un programa bien diseñado cada clase es responsable sólo de una cosa. Cuando una clase se ocupa de varios tipos de productos, puede valer la pena extraer sus métodos de fábrica en una clase de fábrica independiente o una implementación de fábrica abstracta completa.

### **Pros**

- Puede estar seguro de que los productos que obtiene de una fábrica son compatibles entre sí.
  
- Evita el acoplamiento estrecho entre las clases concretas y el código de cliente.
  
- Principio de responsabilidad única. Puede extraer el código de creación del producto en un solo lugar, lo que facilita la compatibilidad con el código.
  
- Principio abierto/cerrado. Puede introducir nuevas variantes de productos sin romper el código de cliente existente.

### **Contras**

- El código puede volverse más complicado de lo que debería ser, ya que se introducen muchas interfaces y clases nuevas junto con el patrón.

### **Relaciones con otros patrones**

- Muchos diseños comienzan usando El método Factory y evolucionan hacia *Abstract Factory*, *Prototype* o *Builder*.

- *Builder* se centra en la construcción de objetos complejos paso a paso. *Abstract Factory* se especializa en la creación de familias de objetos relacionados. *Abstract Factory* devuelve el producto inmediatamente, mientras que *Builder* le permite ejecutar algunos pasos de construcción adicionales antes de capturar el producto.

- *Abstract Factory* a menudo se basan en un conjunto de métodos de fábrica,pero también puede usar *Prototype* para componer los métodos de estas clases.

- Puede servir como alternativa a *Facade* cuando solo desea ocultar la forma en que se crean los objetos del subsistema desde el código de cliente.

- Puede utilizar *Abstract Factory* junto con *Bridge*. Este emparejamiento es útil cuando algunas abstracciones definidas por *Bridge* solo pueden funcionar con implementaciones específicas. En este caso, *Abstract Factory* puede encapsular estas relaciones y ocultar la complejidad del código de cliente.

- Las *Abstract Factories*, los *Builders* y los *Prototype* se pueden implementar como *Singletons*.


## **Builder**

*Builder* es un patrón de diseño creacional que permite construir objetos complejos paso a paso. El patrón permite producir diferentes tipos y representaciones de un objeto utilizando el mismo código de construcción.

### **Problema**

Imagine un objeto complejo que requiera una inicialización laboriosa paso a paso de muchos campos y objetos anidados. Este código de inicialización suele estar enterrado dentro de un *Builder* monstruoso con muchos parámetros. O peor aún: disperso por todo el código del cliente.

Por ejemplo, pensemos en cómo crear un objeto. Para construir una casa sencilla, es necesario construir cuatro paredes y un piso, instalar una puerta, encajar un par de ventanas y construir un techo. Pero, ¿qué pasa si quieres una casa más grande y brillante, con un patio trasero y otras cosas (como un sistema de calefacción, plomería y cableado eléctrico)?

La solución más sencilla es ampliar la clase base casa y crear un conjunto de subclases para cubrir todas las combinaciones de los parámetros. Pero con el tiempo terminarás con un número considerable de subclases. Cualquier parámetro nuevo, como el estilo de terraza, requerirá el crecimiento de esta jerarquía.

Hay otro enfoque que no implica la creación de subclases. Puede crear un *Builder* gigante directamente en la clase base casa con todos los parámetros posibles que controlan el objeto de casa. Si bien este enfoque elimina de hecho la necesidad de subclases, crea otro problema.

En la mayoría de los casos la mayoría de los parámetros no se utilizarán, por lo que el *Builder* estara bastante lleno. Por ejemplo, sólo una fracción de las casas tienen piscinas, por lo que los parámetros relacionados con las piscinas serán inútiles nueve de cada diez veces.

### **Solución**

El patrón *Builder* sugiere que extraiga el código de construcción del objeto de su propia clase y lo mueva a objetos independientes denominados contructores.

El patrón organiza la construcción de objetos en un conjunto de pasos (Puertas, Ventanas, etc.). Para crear un objeto, ejecute una serie de estos pasos en un objeto de generador. La parte importante es que no es necesario llamar a todos los pasos. Solo puede llamar a los pasos necesarios para producir una configuración determinada de un objeto.

Algunos de los pasos de construcción pueden requerir una implementación diferente cuando se necesitan para crear varias representaciones del producto. Por ejemplo, las paredes de una cabaña pueden estar construidas de madera, pero las paredes del castillo deben ser construidas con piedra.

En este caso, puede crear varias clases de generador diferentes que implementen el mismo conjunto de pasos de creación, pero de una manera diferente. A continuación, puede utilizar estos constructores en el proceso de construcción (es decir, un conjunto ordenado de llamadas a los pasos de construcción) para producir diferentes tipos de objetos.

Por ejemplo, imagine un *Builder* que construye todo a partir de madera y vidrio, un segundo que construye todo con piedra y hierro y un tercero que utiliza oro y diamantes. Al llamar al mismo conjunto de pasos, se obtiene una casa normal del primer *Builder*, un pequeño castillo del segundo y un palacio del tercero. Sin embargo, esto solo funcionaría si el código de cliente que llama a los pasos de creación puede interactuar con los generadores mediante una interfaz común.

### **Clase director**

Puede ir más allá y extraer una serie de llamadas a los pasos del generador que utiliza para construir un producto en una clase independiente denominada director. La clase director define el orden en el que se ejecutarán los pasos de creación, mientras que el generador proporciona la implementación de esos pasos.

Tener una clase de director en su programa no es estrictamente necesario. Siempre puede llamar a los pasos de creación en un orden específico directamente desde el código de cliente. Sin embargo, la clase director podría ser un buen lugar para poner varias rutinas de construcción para que pueda reutilizarlas en todo el programa.

Además, la clase director oculta completamente los detalles de la construcción del producto del código de cliente. El cliente sólo necesita asociar un *Builder* con un director, iniciar la construcción con el director y obtener el resultado del *Builder*.

### **Ejemplo**

En este ejemplo del patrón *Builder* se muestra cómo se puede reutilizar el mismo código de construcción de objetos al crear diferentes tipos de productos, como casas, y crear las piezas correspondientes para ellas.

Una casa es un objeto complejo que se puede construir de cientos de maneras diferentes. En lugar de hinchar la clase casa con un *Builder* enorme, extrajimos el código de ensamblaje de la casa en una clase  *Builder* de casas independientes. Esta clase tiene un conjunto de métodos para configurar varias partes de una casa.

Si el código de cliente necesita ensamblar un modelo especial y ajustado de una casa, puede trabajar directamente con el *Builder*. Por otro lado, el cliente puede delegar el ensamblado a la clase director, que sabe cómo utilizar un *Builder* para construir varios de los modelos más populares de casas.

### **Aplicaciones**

- Utilice el patrón *Builder* para deshacerse de un "constructor telescópico" (antipatron donde se dan muchas propiedades, que en casos no tienen ningun orden logico y caen en la creacion de un numero muy grande de constructores). 

  - Supongamos que tiene un constructor con diez parámetros opcionales. Llamar a tal bestia es muy inconveniente; por lo tanto, sobrecargar el constructor y crear varias versiones más cortas con menos parámetros. Estos constructores todavía hacen referencia al principal, pasando algunos valores predeterminados en los parámetros omitidos.

  - El patrón *Builder* le permite crear objetos paso a paso, utilizando solo los pasos que realmente necesita. Después de implementar el patrón, ya no tiene que incorporar docenas de parámetros en los constructores.

- Utilice el patrón *Builder* cuando desee que el código pueda crear diferentes representaciones de algún producto (por ejemplo, casas de piedra y madera).

  - El patrón *Builder* se puede aplicar cuando la construcción de varias representaciones del producto implica pasos similares que difieren sólo en los detalles.

  - La interfaz del generador base define todos los pasos de construcción posibles, y los constructores de hormigón implementan estos pasos para construir representaciones particulares del producto. Mientras tanto, la clase de director guía el orden de construcción.

- Utilice el Generador para construir árboles compuestos u otros objetos complejos.
  - El patrón *Builder* le permite construir productos paso a paso. Puede aplazar la ejecución de algunos pasos sin romper el producto final. Incluso puede llamar a pasos de forma recursiva, lo que es útil cuando necesita crear un árbol de objetos.

  - Un constructor no expone el producto inacabado mientras se ejecutan pasos de construcción. Esto impide que el código de cliente obtenga un resultado incompleto.

### **Pros**

- Puede construir objetos paso a paso, aplazar pasos de construcción o ejecutar pasos de forma recursiva.

- Puede reutilizar el mismo código de construcción al crear varias representaciones de productos.

- Principio de responsabilidad única. Puede aislar código de construcción complejo de la lógica empresarial del producto.

### **Contras**

- La complejidad general del código aumenta ya que el patrón requiere la creación de varias clases nuevas.

### **Relaciones con otros patrones**

- Muchos diseños comienzan usando El método Factory y evolucionan hacia Abstract Factory, Prototypeo *Builder* (más flexible, pero más complicado).

- *Builder* se centra en la construcción de objetos complejos paso a paso. Abstract Factory se especializa en la creación de familias de objetos relacionados. Abstract Factory devuelve el producto inmediatamente, mientras que *Builder* le permite ejecutar algunos pasos de construcción adicionales antes de capturar el producto.

- Puede utilizar *Builder* al crear árboles compuestos complejos porque puede programar sus pasos de construcción para que funcionen de forma recursiva.

- Puede combinar *Builder* con Bridge:la clase director desempeña el papel de la abstracción, mientras que los diferentes constructores actúan como implementaciones.

## **Singleton**

*Singleton* es un patrón de diseño de creación que le permite asegurarse de que una clase solo tiene una instancia, al tiempo que proporciona un punto de acceso global a esta instancia.

### **Problema**

El patrón *Singleton* resuelve dos problemas al mismo tiempo, violando el principio de responsabilidad única:

1. Una clase tiene una sola instancia. ¿Por qué alguien querría controlar cuántas instancias tiene una clase? La razón más común para esto es controlar el acceso a algún recurso compartido, por ejemplo, una base de datos o un archivo.

    Así es como funciona: imagina que creaste un objeto, pero después de un tiempo decidiste crear uno nuevo. En lugar de recibir un objeto nuevo, obtendrá el que ya se ha creado.

    Tenga en cuenta que este comportamiento es imposible de implementar con un constructor normal, ya que una llamada al constructor siempre debe devolver un nuevo objeto por diseño.

2. Punto de acceso global a esa instancia. Las variables globales usadas para almacenar algunos objetos esenciales, aunque son muy prácticas, también son muy inseguras, ya que cualquier código puede sobrescribir potencialmente el contenido de esas variables y bloquear la aplicación.

    Al igual que una variable global, el patrón *Singleton* le permite acceder a algún objeto desde cualquier lugar del programa. Sin embargo, también protege esa instancia de ser sobrescrita por otro código.

    Hay otro lado en este problema: no quieres que el código que resuelve el problema #1 se disperse por todo el programa. Es mucho mejor tenerlo dentro de una clase, especialmente si el resto del código ya depende de él.

Hoy en día, el patrón *Singleton* se ha vuelto tan popular que la gente puede llamar a algo un *singleton* incluso si resuelve sólo uno de los problemas enumerados.

### **Solución**

Todas las implementaciones del *Singleton* tienen estos dos pasos en común:

- El constructor predeterminado sera privado, para evitar que otros objetos usen el nuevo operador con la clase *Singleton*.

- Se creara un método de creación estático que actúe como constructor. Por debajo, este método llama al constructor privado para crear un objeto y lo guarda en un campo estático. Todas las llamadas siguientes a este método devuelven el objeto almacenado en caché.
  
Si el código tiene acceso a la clase *Singleton*  a continuación, es capaz de llamar al método estático *Singleton*. Por lo tanto, siempre que se llama a ese método, siempre se devuelve el mismo objeto.

### **Ejemplo**

En este ejemplo, la clase de conexión de base de datos actúa como *Singleton*. Esta clase no tiene un constructor público, por lo que la única manera de obtener su objeto es llamar al método *get_instance*. Este método almacena en caché el primer objeto creado y lo devuelve en todas las llamadas posteriores.

### **Aplicaciones**

- Se utiliza el patrón *Singleton* cuando una clase del programa debe tener una sola instancia disponible para todos los clientes; por ejemplo, un único objeto de base de datos compartido por diferentes partes del programa.

  - El patrón *Singleton* deshabilita todos los demás medios de creación de objetos de una clase, excepto el método de creación especial. Este método crea un nuevo objeto o devuelve uno existente si ya se ha creado.

- El patrón *Singleton* es usado cuando se necesite un control más estricto sobre las variables globales.

  - A diferencia de las variables globales, el patrón *Singleton* garantiza que solo hay una instancia de una clase. Nada, excepto la propia clase *Singleton*, puede reemplazar la instancia almacenada en caché.

  - Tenga en cuenta que siempre puede ajustar esta limitación y permitir la creación de cualquier número de instancias *Singleton*. El único fragmento de código que necesita cambiar es el cuerpo del método.

### **Pros**

- Puede estar seguro de que una clase solo tiene una instancia.
  
- Obtendrá un punto de acceso global a esa instancia.
  
- El objeto *singleton* se inicializa solo cuando se solicita por primera vez.

### **Contras**

- Viola el Principio de Responsabilidad Única. El patrón resuelve dos problemas en ese momento.

- El patrón *Singleton* puede enmascarar un mal diseño, por ejemplo, cuando los componentes del programa saben demasiado entre sí.

- El patrón requiere un tratamiento especial en un entorno multiproceso para que varios subprocesos no creen un objeto *singleton* varias veces.

- Puede ser difícil probar unitariamente el código de cliente de *Singleton* porque muchos marcos de pruebas dependen de la herencia al producir objetos ficticios. Dado que el constructor de la clase *singleton* es privado y reemplazar métodos estáticos es imposible en la mayoría de los lenguajes, tendrá que pensar en una forma creativa de simular el *singleton*.

### **Relaciones con otros patrones**

- Una clase Facade a menudo se puede transformar en un *Singleton* ya que un único objeto de facade es suficiente en la mayoría de los casos.

- Flyweight se parecería a *Singleton* si de alguna manera lograste reducir todos los estados compartidos de los objetos a un solo objeto flyweight. Pero hay dos diferencias fundamentales entre estos patrones:

  - Debe haber solo una instancia *singleton*, mientras que una clase Flyweight puede tener varias instancias con diferentes estados intrínsecos.

  - El objeto *Singleton* puede ser mutable. Los objetos Flyweight son inmutables.

- Las *Abstract Factories*, los *Builders* y los *Prototype* se pueden implementar como *Singletons*.