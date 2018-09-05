# C4-PlantUML

C4-PlantUML combines the benefits of [PlantUML](http://en.plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures - especially during up-front design sessions - with an intuitive language using open source and platform independent tools.

C4-PlantUML includes macros, stereotypes, and other goodies (like VSCode Snippets) for creating C4 diagrams with PlantUML.

## Background

[PlantUML](http://en.plantuml.com/) is an open source project that allows you to create UML diagrams.
Diagrams are defined using a simple and intuitive language.
Images can be generated in PNG, in SVG or in LaTeX format.

PlantUML was created to allow the drawing of UML diagrams, using a simple and human readable text description.
Because it does not prevent you from drawing inconsistent diagrams, it is a drawing tool and not a modeling tool.
It is the most used text-based diagram drawing tool with [extensive support into wikis and forums, text editors and IDEs, use by different programming languages and documentation generators](http://en.plantuml.com/running).

The [C4 model](https://c4model.com/) for software architecture is an "abstraction-first" approach to diagramming, based upon abstractions that reflect how software architects and developers think about and build software.
The small set of abstractions and diagram types makes the C4 model easy to learn and use.
C4 stands for context, containers, components, and code — a set of hierarchical diagrams that you can use to describe your software architecture at different zoom levels, each useful for different audiences.

The C4 model was created as a way to help software development teams describe and communicate software architecture, both during up-front design sessions and when retrospectively documenting an existing codebase.

More information can be found here:

* [The C4 model for software architecture](https://c4model.com/)
* [REAL WORLD PlantUML - Sample Gallery](https://real-world-plantuml.com/)
* [Visualising and documenting software architecture cheat sheets](http://www.codingthearchitecture.com/2017/04/27/visualising_and_documenting_software_architecture_cheat_sheets.html)
* [PlantUML and Structurizr - Create models not diagrams](http://www.codingthearchitecture.com/2016/12/08/plantuml_and_structurizr.html)

## Getting Started

At the top of your C4 PlantUML `.puml` file, you need to include the `C4_Container.puml` file found in the `root` of this repo.

To be independent of any internet connectifity, you can also download `C4_Container.puml` and reference it locally with

```plantuml
!include path/to/C4_Container.puml
```

If you want to use the always up-to-date version in this repo, use the following:

```plantuml
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml
```

After you have inlcluded `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `System`, `Container`, `Relationship`.

```plantuml
@startuml Basic Sample
!include C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

In addition to this, it is also possible to define a system boundary.

Take a look a look at the following sample of a C4 Container Diagram:

```plantuml
@startuml Basic Sample
!include C4_Container.puml

Person(admin, "Administrator")
package "Sample System" <<boundary>> as c1 {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

## Snipptes for Visual Studio Code

Lorem

https://medium.com/hack-visual-studio-code/share-snippets-with-your-team-in-vs-code-817801e853fb

## Layout Options

PlantUML uses [Graphviz](https://www.graphviz.org/) for his graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

For this reason, C4-PlantUML also comes with some layout options.

### LAYOUT_TOP_DOWN or LAYOUT_LEFT_RIGHT

With the two macros `LAYOUT_TOP_DOWN` and `LAYOUT_LEFT_RIGHT` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN` is the default.

```plantuml
@startuml Basic Sample
!include C4_Container.puml

' Not needed because this is the default
LAYOUT_TOP_DOWN

Person(admin, "Administrator")
package "Sample System" <<boundary>> as c1 {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

Using `LAYOUT_LEFT_RIGHT`

```plantuml
@startuml Basic Sample
!include C4_Container.puml

LAYOUT_LEFT_RIGHT

Person(admin, "Administrator")
package "Sample System" <<boundary>> as c1 {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

### LAYOUT_WITH_LEGEND

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.


## Advanced Samples

