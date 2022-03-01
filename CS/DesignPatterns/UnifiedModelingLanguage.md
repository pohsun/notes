#CS/DesignPattern 

# Unified Modeling Language

Reference:
* [The UML language](https://www.uml-diagrams.org)
* [PlantUML](http://plantuml.com/zh/)
* [Tutorialspoint](https://www.tutorialspoint.com/uml/uml_overview.htm)
* [看懂UML建模語言](https://design-patterns.readthedocs.io/zh_CN/latest/read_uml.html)

UML, **Unified Modeling Language**, is a standard language for specifying, visualizing, constructing, and documenting the artifacts of software systems.

* UML is different from the other common programming languages such as C++, Java, COBOL, etc.

* UML is a pictorial language used to make software blueprints.

* UML can be described as a general purpose visual modeling language to visualize, specify, construct, and document software system.

* Although UML is generally used to model software systems, it is not limited within this boundary. It is also used to model non-software systems as well. For example, the process flow in a manufacturing unit, etc.

## The object-oriented world

Objects are the real-world entities that exist around us and the basic concepts as following, all can be represented using UML.

* **Objects** − Objects represent an entity and the basic building block.
* **Class** − Class is the blue print of an object.
* **Abstraction** − Abstraction represents the behavior of an real world entity.
* **Encapsulation** − Encapsulation is the mechanism of binding the data together and hiding them from the outside world.
* **Inheritance** − Inheritance is the mechanism of making new classes from existing ones.
* **Polymorphism** − It defines the mechanisp to exists in different forms.

UML is powerful enough to represent all the concepts that exist in object-oriented analysis and design.
UML diagrams are representation of object-oriented concepts only.
Thus, before learning UML, it becomes important to understand OO concept in detail.

The purpose of OO analysis and design can described as

* Identifying the objects of a system.
* Identifying their relationships.
* Making a design, which can be converted to executables using OO languages.

There are 3 steps to implement an OO design:

* OO analysis:

    Identify objects and describe them in a proper way.
    If these objects are identified efficiently, then the next job of design is easy.
    *The objects should be identified with responsibilities*.
    Responsibilities are the functions performed by the object.
    Each and every object has some type of responsibilities to be performed.
    When these responsibilities are collaborated, the purpose of the system is fulfilled.

* OO design:

    In this stage, the objects are *collaborated according to their intended association*. After the association is complete, the design is also complete.

* OO implementaion:

    Design is implemented using OO languages such as Java, C++, etc.

## UML modeling

For quick intro to each, reference to [UML official reference](https://www.uml-diagrams.org/class-reference.html). The commonly used diagrams are **Class diagram**, **Sequence diagram**, and sometimes **Use case diagram**.

* [Relationships](https://www.uml-diagrams.org/uml-core.html#relationship)

```plantuml
left to right direction

"Base" <|-- "(Abstract) Derived" : Generalization (Inheritance, is-A)
Class <|.. Instance : Realization
"Traffic jam" o-- Car : Aggregation, still have car even without traffic jam
Company *-- Department : Composition, no department if company collapse
"Gravity" <-- "General relativistics": Association
"Central Limit Theorem" <.. "Asymptotic approximation technics" : Dependency

hide methods
hide members
```

* [Diagrams](https://en.wikipedia.org/wiki/Unified_Modeling_Language)

```plantuml
left to right direction

package "UML Diagrams" as pkg_root {
    package "Structural" as pkg_structural {
        class "Classes, 類圖" as cls_classes
        class "Objects, 對象圖" as cls_objects
        class "Package, 套件圖" as cls_package
        class "Deployment, 部署圖" as cls_deployment
        class "Component, 組件圖" as cls_component
        class "Composite structure, 複合結構圖" as cls_compositeStructure
        class "Profile" as cls_profile
    }
    package "Behavioral" as pkg_behavioral {
        class "Activity, 活動圖" as cls_activity
        class "Use case, 用例圖 " as cls_usecase
        class "State Machine" as cls_stateMachine
        package "Interaction" as pkg_interaction {
            class "Sequence, 循序圖" as cls_sequence
            class "Timing" as cls_timing
            class "Communication" as cls_communication
            class "Interaction overview" as cls_interactionOverview
        }
    }
}

hide methods
hide members
```