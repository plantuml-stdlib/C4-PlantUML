# C4-PlantUML

![Container diagram for Internet Banking System](https://www.plantuml.com/plantuml/png/bLLDZzis4BtxLqoTGnr0kqQ0ddgArpQwcwntrSZRJK_2Y1hRH2XI82axHj7_tg6i3yiEajGdQJJpvl7D6_gzysXzLQZHBr8BLUK4E-zBz_jqQl5mkvL-LsML8okCzgJzhJ3557ChKUzLLLRJ-MytiKBjNrQFKuMUdETGEkTib9hiRHcmVuLASs710E1t11kZb3b8lGN5IO0wXy5dQHq_6U36e8n0fOwCqJ6yRi1V7sT_Fx-iq_Lpd2wUNvycR_lOB4cJZylr_9w3JUZrONsVFYx_M3ujE3ZoqYl6RK4XbxYrM31H2mzySAl9mntgBu5pSdIUYj4e9kkCdeZAULEGZM3UFOrdq8R1REf3PLmTmO45XR8kH5N708KmbVPkp3nEqEaT1tAqnubunrYN1CPluPyHyA_ZEpbGbc9PSl8hPJ0hIoK5Ucdqc4CVS8yH9AKDv5T_pKDiGKhkcKPDZJtWfO1cnFKuGhZhcxK7ZsTCSjZPbOmzJlYpefiOjnIwjrqJOMNf8vZfRQNGXd1ipLxcv827-kqk6_PAe8vA-cDmWQXg8Hti9OOIQO7F2var1pRc5QF2P59H8yUgVcavpTz4y1aBP2M6NDY7XVIKWwionroQcVqCDtT5xaG0SjfBGPVq5jaaHuyPEWfZQ1u3c-JFHnYyUsEPMrW-iBILpblarY0rkxAefnl1ZfDpm8fT9IpbF3w9oaN1LEGSBy-MNyYBsokPCXHVIEUiamn-ZH--RPk5uJJRrmrq-u4-GH86vjR_TjPUVlKJAb2grDK1XblUhFYzMQk0lsRfPGtDExAImXfdDXwMNyKEDJliLCcmPvWDWnwLCVM6TvWkzlPCsc31PjA20zqfpXG6p4pb-p57tRf6mFFG3klpzYAFFf4wknBwnNnnv4Bl-_KwJZXnc7TQe-_d38nTfvxQfKyajxlCd5q39xXsoHkaEZWSUziGtL6B23uapq_Jy-RdBVzNPNh7sJsntl93b4-4kOEDDKLzwnmiBo7VIIOWDy2Bktbxpe1vfiU5ZHA6TK0t8LfZz4Gk73VaCAohNBXXk_R9QXqtGDrX1kLNlck52VNJHftF_EVOYlEUI_alwpy0 "Container diagram for Internet Banking System")

C4-PlantUML combines the benefits of [PlantUML](http://en.plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures – especially during up-front design sessions – with an intuitive language using open source and platform independent tools.

C4-PlantUML includes macros, stereotypes, and other goodies (like VSCode Snippets) for creating C4 diagrams with PlantUML.

* [Getting Started](#getting-started)
* [Supported Diagram Types](#supported-diagram-types)
* [Snippets for Visual Studio Code](#snippets-for-visual-studio-code)
* [Layout Options](#layout-options)
* [Samples](#advanced-samples)
* [Background](#background)
* [License](#license)

## Getting Started

At the top of your C4 PlantUML `.puml` file, you need to include the `C4_Context.puml`, `C4_Container.puml` or `C4_Component.puml` file found in the `root` of this repo.

To be independent of any internet connectivity, you can also download the files found in the `root` and reference it locally with

```c#
!include path/to/C4.puml
!include path/to/C4_Context.puml
!include path/to/C4_Container.puml
!include path/to/C4_Component.puml
```

Just remember to change the `!include` statements at the top of the files.

If you want to use the always up-to-date version in this repo, use the following:

```c#
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
```

Now let's create a C4 Container diagram:

After you have included `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `Person_Ext`, `System`, `System_Ext`, `Container`, `Relationship`, `Boundary`, and `System_Boundary`

```csharp
@startuml C4_Elements
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

![test](https://www.plantuml.com/plantuml/png/ZOz1Yy9038NlyojgJnNSpiNJdbpqwAAuUfOu3NOWpGoJZEA_trfGLaJPqti9oPUNcIWapHsPaMT7kS6YLOtoQMs2SttqskP35amki29hxK9deKaU-4GvPZkVVgm9M7VVIqkWADgtzlD-6ZnZgkELRTQO970L1_aY3p8foYKSaChUhABwm4350iKbFrJbsDmXbRkvfzKjkfO3XUFb3UZd8efT9OFyzxhP83q6VftYZlWJPsnco4t__Iy0 "test")

In addition to this, it is also possible to define a system or component boundary.

Take a look a look at the following sample of a C4 Container Diagram:

```csharp
@startuml Basic Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, "Sample System") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![Basic Sample](https://www.plantuml.com/plantuml/png/JP1FIyD04CNl-HHZlAHG4ogUF3KDeWShmQHwBDDaj0lxZzs9eOZVtGcjhNiPcFURUMzs6Ha33qR32gFge47ZDILNodPww0dsp3xU5qN0CVzKl1zsGwJGESjaEU-SAR0F2ksN7lnGL7StjKRBc_LpeP4fihIsbT2eB8NSYr6Ir1IYindsHjavfELKLUI0x48wIvf3P3BRbHjiZ-6GTGk1ZhdWgAKp-4v0tdbpDj9kYzuB-KuxABtNgaDMpgRIggxdK3Pr_lBGoaWWkCqNi7wh9gtKseqHfgiYi0CvoQCWPj2i9ijsLCmKW9KXBLvH8lwSGcPy56NF2HCnUINzTzmbrYRAfDIdjgqReIReh5xMF19BZ96cyX6S-J-o9DlB1_u2 "Basic Sample")

Entities can also be decorated with icons using the last parameter, for example:

```cs
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define DEVICONS https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/devicons
!define FONTAWESOME https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/font-awesome-5
!include DEVICONS/angular.puml
!include DEVICONS/java.puml
!include DEVICONS/msql_server.puml
!include FONTAWESOME/users.puml

LAYOUT_WITH_LEGEND()

Person(user, "Customer", "People that need products", "users")
Container(spa, "SPA", "angular", "The main interface that the customer interacts with", "angular")
Container(api, "API", "java", "Handles all business logic", "java")
ContainerDb(db, "Database", "Microsoft SQL", "Holds product, order and invoice information", "msql_server")

Rel(user, spa, "Uses", "https")
Rel(spa, api, "Uses", "https")
Rel_R(api, db, "Reads/Writes")
@enduml
```

![test](https://www.plantuml.com/plantuml/png/hL9DZzCm4BtdLtXxeIjjwmDmuRHLMzXA_Q8VL9ogQJnfZHmxUEnM_7l6QRORM90uS8erx-NDl9dtI05yYAN9xhJDJLGeJY5Kz45A3vV-KOTJF4H2dpiRq8P-xae9ockmPnEhA8VlUai3DcndKsaW80KkxOVC1ctHzwka_KP4op-MB2322KNXZ74NRO_2C4c0LU8NM7lYbnFSM1YNWp4_MECsuUi6sPt28acDnbycmyLy_GykGgpOo5jPfV5PfASPxHNCw57bDLkH9L10BnMU4qQtBXyNyyrWDrulPkF_sgYkmGN9bTXx_tAIPrSIx34QQ4o_Xh_16Vw6bVJTx7coC_x-UykDJBDJizFfuEjYkzdl9fkd_NJyQJmVTU-pRCa4Pxk9-20wmqY1X_KTVY_HLGRvWX24HLIYyax5F502Q-7EVNOxN9SguFfwEKXmOomzDvo0aYb2ymfz0NaZcPAHD-sk6B2skF3Esmhj5b1fHWRBIIAavQJl4yVD80bEbU1RCP68KtRK-OtLqXWTkkh0zH44E01XuinqxXsv8eZrvsajwOoYPxiFmdd58wPKQtjscWreMpXVGj3E9dxh5jmhMw5fzddToPQmtbaTBIOal4QkVlu0xrTNh_MeAmH5SbSdY-57j8hl-HC0 "test")


## Supported Diagram Types

Diagram types 

* System Context & System Landscape diagrams
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml`
  * Macros: 
    * `Person(alias, label, ?description, ?sprite)`
    * `Person_Ext`
    * `System(alias, label, ?description, ?sprite)`
    * `System_Ext`
    * `Boundary(alias, label, ?type)` 
    * `Enterprise_Boundary(alias, label)`
    * `System_Boundary` 
* Container diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml`
  * Additional Macros: 
    * `Container(alias, label, technology, ?description, ?sprite)`
    * `ContainerDb`
    * `ContainerQueue`
    * `Container_Ext`
    * `ContainerDb_Ext`
    * `ContainerQueue_Ext`
    * `Container_Boundary(alias, label)`
* Component diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml`
  * Additional Macros: 
    * `Component(alias, label, technology, ?description, ?sprite)`
    * `ComponentDb`
    * `ComponentQueue`
    * `Component_Ext`
    * `ComponentDb_Ext`
    * `ComponentQueue_Ext`
* Dynamic diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Dynamic.puml`
  * Additional Macros: 
    * `RelIndex(index, from, to, label)`
    * `increment()`
    * `setIndex(number)`
* Deployment diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Deployment.puml`
  * Additional Macros: 
    * `Deployment_Node(alias, label, ?type)`

Take a look at each of the [C4 Model Diagram Samples](samples/C4CoreDiagrams.md).

## Relationship Types

* `Rel(from, to, label, ?technology)`
* `BiRel` (bidirectional relationship)

You can force the direction of a relationship by using:

* `Rel_U`, `Rel_Up`
* `Rel_D`, `Rel_Down`
* `Rel_L`, `Rel_Left`
* `Rel_R`, `Rel_Right`

In rare cases, you can force the layout using hidden relationships, `Lay_U`, `Lay_D`, `Lay_L`, `Lay_R`.

## Layout Options

C4-PlantUML also comes with some layout options to make it easy and reuseable to create nice and useful diagrams:

* [LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT()](LayoutOptions.md#layout_top_down-or-layout_left_right)
* [LAYOUT_WITH_LEGEND()](LayoutOptions.md#layout_with_legend)
* [LAYOUT_AS_SKETCH()](LayoutOptions.md#layout_as_sketch)
* [HIDE_STEREOTYPE()](LayoutOptions.md#hide_stereotype)

## Snippets for Visual Studio Code

Because the PlantUML support inside of Visual Studio Code is excellent with the [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), you can also find VS Code snippets for C4-PlantUML at [.vscode/C4.code-snippets](.vscode/C4.code-snippets).

Project level snippets are now supported in [VSCode 1.28](https://code.visualstudio.com/updates/v1_28#_project-level-snippets).
Just include the `C4.code-snippets` file in the `.vscode` folder of your project.

It is possible to save them directly inside VS Code: [Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_creating-your-own-snippets).

![C4-PlantUML Snippets Video](images/vscode_c4plantuml_snippets.gif)

## Advanced Samples

The following advanced samples are reproductions with C4-PlantUML from official [C4 model samples](https://c4model.com/#examples) created by [Simon Brown](http://simonbrown.je/).

The core diagram samples from [c4model.com](https://c4model.com/#coreDiagrams) are available [here](samples/C4CoreDiagrams.md).

### techtribes.js

Source: [C4_Container Diagram Sample - techtribesjs.puml](samples/C4_Container%20Diagram%20Sample%20-%20techtribesjs.puml)

![techtribesjs](https://www.plantuml.com/plantuml/png/ZLLDSziu3BthLs1zgJAZjTkatSpigKwS9csTZqRoPdhIK19iiwL8BKd5yNJwtmjIiYp5tSdwO54W2Bm7F53lZMNQrgM0aSLyRJNFq7mpe-0FBdDH5mXhQolpzsIYsMQyudPTPxL1dIjfKTfnhie9ApHdyb7KLJqvV_lddM3IBgxd4y4i6akcz9oy6PUennMb2bv1BUbWIG70hX6MIWYruN85Wfo0oG86srmRMYcWn21KpeJOKemEuM62O3xzUhj8qkJsBftTFjo4Hy6hrZIDq_ZpHN9-HRRMzF0nkKhd5vSNDpCo1i4TQgDaUl5aGoQLt9QgDgaZ7S5ekZF0WWoZezOvPAkLnXKHBZhFplBSjIYvvCPgPZcbsRaFhBiZGRmr5ilqJDMoO7eRvc-YVgV6rAgZ7m7Gp_zrTGWtcAMigiZx0JEOLfNWkGyz8jCdziWYY2ljQdxzpta4YIff6qx7Jsv_wlfXNBsrSOL_vBY12bKbC88cSmIj12B0HtgGuPlAw1zjFeQbLgNldMyNEC0H59pqGs-klnyJC9XRvKaEaC-oKAD8YunmtAFmcEdGZ5cMCOCEtlKs_ZA7T-Dt3TgOmg0vmEUVK6AP4Oirfr9Gyk_cETwC5IldVidjLPs1nagrB0wWXKikqFYEKDeFz09DVnoA3zFavBW7no3J-HguBF09pUzeIcN-5NJWHZawZY3uivwYaYirEuFZyV60f2_iVHnFffOMIyJ2G9W9jGA2RSsHBwxT8Dh3b65T5QH7fxP5izff0KwTbr54Y9GowXoeg5fvqb4RT5YdTbIz3e1Koy3aQongGQAdPd67uMSdOZTGTiDj0o5fLkJHssuk6DfjiWmt7Kq2C3fpJySk87qSZEXU-3H3nd6vIfAxcFozz_CvVS7zTxFwtqVycMwx9sDMjArp1TjexafhbU_hb_daq-oCHh1IsiB9oUk_sjnTd87gzh6Uk-tarFFe2Md3DRfkMfKhqIOxFdtzvhI5dIxsydW1UE6K-WBwVhW1_eUE_87V8O73SlrVElkeUyLTadvtWgQvN2fTDfVjVcQwilL5q8NQgzEv3Y9aghPGrHdTiZGGz57oyy5fQ3c-47KdQnzqDqorSLSp3Re7rnlsVYZ7TSwswNrtO-vBJLllKHRqDVm5 "techtribesjs")


### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](https://www.plantuml.com/plantuml/png/bLN1Sjem4BtxAxRqa6Gc2Msdfvv2W6dQaa0mcKnFdhKiG1DPqaWoAUdqtxkoZR49CqsvOArNxxrzkmjNpgFrHIwXbtFdSCNJmlMYTq8nMMGSrjuRzwNVj_XykH9-NT1hRfbMdYj_oNJUnymAL1jPcA8__7mnawZym-saBz5pvocK32aRXUBsqX1HT0A5eeiv0O1VSrXgAVMpK2kGb0IeCkYy5jRHamOY1gaPIhabZ4RXQuB8FGbbq68EpnRDeyZy6Zvz-D2Av_ZhjYet5Y-yV1bD1Z-d3ujaCPqbe-dZtUbPT5A71d4I_nWlXZSKgqEFtnOtoMJyTNmtec0KpRXrMfsomdcTStiEm-QfDu1Tk4UfyTPvdYVNkb0Pskqf-qWfkspuffRQvkY5Lhqp-1r5G9-clbCqffqzC4OALcLJ_3jkq34hZ3-7WLeL4cq83uA_hX7XWfavAYe-62mi6AkNGlAWhaktkv9GppU2yJPtN8LslESG6nkQUAsr3y45zSveGLtKIq36o6vgjMraW6YNUiXS3sD2uqPOTQ_WccQJZdDCK-5lxqiQYyePRNq9JkbqdPZuXkR7lSQrFEIIpbP9yrsiNTEyIBVXUsXv66HGGQiKZcUGeSUIhG43KrYZ7Jz2Y4KcV8ji4Cvjek7x_kNTU14UPrPlH4PasgvG2LTwS_5C8IXX0jCIcP3qU8HhbEuRbgNjNer8SOgkv9jQP9B3nqyid6AlBNTlQmhXx-qh2VREjHbkj_7zf0MEE_DUoBmD3I21bqCXvRvXZQcOmLgp__4siEoT3QT0FWuJi3_MMbhr0QQwyFMaq2QWXpLkw2UFbemhdX7VdoYQSzdQwch_7e8Q-hvPB6Pna4L9oRnQpYChys2oSeIEcGoX_bK0GxTLx1o-nzExVWTuScGDAnqnLvbh2j01vP6diMPFtDFjIjNhoztTga0QRKKfjWLwrh5WZz8TjThUiekY-Z4QNG_h4hhRV6m5toQY0tEuMF-6A36Ei1yCzK4f5VK1MtVowXirLtadck2Mp3_2ra6Yn2lIJVzQVm40 "messagebus")


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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
