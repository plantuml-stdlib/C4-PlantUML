# Extended C4-PlantUML

This branch is basically https://github.com/plantuml-stdlib/C4-PlantUML/tree/master
extended with my open PRs.

**Old master branch**

The [old master branch](https://github.com/kirchsth/C4-PlantUML/blob/master/README.md) is still working. But it will not be updated anymore.

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

```csharp
!include path/to/C4.puml
!include path/to/C4_Context.puml
!include path/to/C4_Container.puml
!include path/to/C4_Component.puml
```

Just remember to change the `!include` statements at the top of the files.

If you want to use the always up-to-date version in this repo, use the following:

```csharp
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml
```

Now let's create a C4 Container diagram:

After you have included `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `Person_Ext`, `System`, `System_Ext`, `Container`, `Relationship`, `Boundary`, and `System_Boundary`

```csharp
@startuml C4_Elements
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

![test](http://www.plantuml.com/plantuml/png/ZOxDIWGn48JlUOeufn5qSjcJfvNHsugBFsV99iqcsEc4T0VTjpSCE2AYUAeAgVwgjYosIakevytBBK824bPdaHms3pg85BuofjgtwHWbj4DZg2wJzDpaSZAliRh04ioykToZ9Nc-snbux_yUlEdGkOTj9AXJwJLAxQ5ofh4iSetHyeKUTlO0E7HpNoHcigXlW5sDosiuLojaT9_kn-aJk40Py_7q1-Znn09fv4N-swuU0ByFNbVyZlYQqmbR8DyIVW00 "test")

In addition to this, it is also possible to define a system or component boundary.

Take a look a look at the following sample of a C4 Container Diagram:

```csharp
@startuml Basic Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, "Sample System") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![Basic Sample](http://www.plantuml.com/plantuml/png/JP3FJkD03CRlUGflzf9AtKHTxMbFJIC41ueYaiAncauC6J5_HZEEGeLuTpngQPcBDVv-jZzx7Ka4ceo6ZOXAGYUCrvZzKbRgQK0OYNpyNrL1pEMhed4wJ163T9RGKYcTgTvKa6EaiMh-_McriBJRtbVuplg00oVt3SD2MGobvpbPrcA8pXPYCCek8QzJL96281VoHTOT8w7PRzna1n6EXLmnTB859orVm4S6_2wTYnaFU-4zayzuWDfxhQGWvMpEgURt4kgkBHzkUYu927_B5MoVcgJLMhivGbeg0ZdWZRnWn4oQL1hPpue80v0og7bMP8kVPvC5dKJkSyPOp1vHVoztjRMBNCdnhk_RZga4NTHhcrkao5zCuIKuyxDapHTD1_m2 "Basic Sample")

Entities can also be decorated with icons using the last parameter, for example:

```csharp
@startuml
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

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

![test](http://www.plantuml.com/plantuml/png/hL9DZzem4BtdLtWviTA23sqlFIq2saNYW_9Hr1CQue6uTUpKCu7-_8v3Yb0_f1xsP6VUotlpPlnC397hqcKFrkUkDgWAvehUQntXqZzPBkf3JHZpu1azz_DGwcysvWLneOTlUqi7dhUpgSOVWXiqKjmFXGpMO-nNIJfxC7YKJpKQVvuC5_FrVtXmNO69RtILz4MaPmNj7ONHeofQHj8b46FK1iy9evlBXyLyCzYDrulP-5MDcXfSa4A9lNUtWTrIQV2dsa4R-a_uAvpXNrX9tzsUC9xnzz_lqkZKExKpdGw-BBQR_MwoUTbFnn_7yr7tCSkMGWY-cuXFgZEiYQNPs97x4aFbK741h3oYKLKCfiwP4jW8Tnwps-AwL87Kryj1WjjWwRefK9L2KTOpnYFahIHBFM_jhXY8jhh8pEyLxYsWie8CbfD4ICD9vmjuuv0KEATaLq8aKYwSR7vZtMcC3brpaFe860v0c3WpcyT0uSXg_MdQI0Pdw5VS9nMYaHR5Hjey1vkZdCSGIs0RVEBVxKAyiXMwTfxNcMm9AT6QfoM4X3U8vFaxl5zTipQjhX0CwLtpiWH-Hc_IFdy2 "test")


## Supported Diagram Types

Diagram types 

* System Context & System Landscape diagrams
  * Import: `!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Context.puml`
  * Macros: 
    * `Person(alias, label, ?description, ?sprite)`
    * `Person_Ext`
    * `System(alias, label, ?description, ?sprite)`
    * `System_Ext`
    * `Boundary(alias, label, ?type)` 
    * `Enterprise_Boundary(alias, label)`
    * `System_Boundary` 
* Container diagram
  * Import: `!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml`
  * Additional Macros: 
    * `Container(alias, label, technology, ?description, ?sprite)`
    * `ContainerDb`
    * `ContainerQueue`
    * `Container_Ext`
    * `ContainerDb_Ext`
    * `ContainerQueue_Ext`
    * `Container_Boundary(alias, label)`
* Component diagram
  * Import: `!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Component.puml`
  * Additional Macros: 
    * `Component(alias, label, technology, ?description, ?sprite)`
    * `ComponentDb`
    * `ComponentQueue`
    * `Component_Ext`
    * `ComponentDb_Ext`
    * `ComponentQueue_Ext`
* Dynamic diagram
  * Import: `!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Dynamic.puml`
  * Additional Macros: 
    * `RelIndex(index, from, to, label)`
    * (lowercase) `increment($offset=1)`: increase current index (procedure which has no direct output)
    * (lowercase) `setIndex($new_index)`: set the new index (procedure which has no direct output)
    * `LastIndex()`: return the last used index (function which can be used as argument)

    following 2 macros requires V1.2020.24Beta4 (can be already tested with http://www.plantuml.com/plantuml/)
    * `Index($offset=1)`: returns current index and calculates next index (function which can be used as argument)
    * `SetIndex($new_index)`: returns new set index and calculates next index (function which can be used as argument)

* Deployment diagram
  * Import: `!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Deployment.puml`
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

C4-PlantUML also comes with some layout options to make it easy and reusable to create nice and useful diagrams:

* [LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT()](LayoutOptions.md#layout_top_down-or-layout_left_right)
* [LAYOUT_WITH_LEGEND()](LayoutOptions.md#layout_with_legend)
* [LAYOUT_AS_SKETCH()](LayoutOptions.md#layout_as_sketch)
* [HIDE_STEREOTYPE()](LayoutOptions.md#hide_stereotype)

C4-PlantUML also comes with some default person sprite options:

* [HIDE_PERSON_SPRITE()](LayoutOptions.md#hide_person_sprite)
* [SHOW_PERSON_SPRITE_ACTIVE()](LayoutOptions.md#show_person_sprite)

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

![techtribesjs](http://www.plantuml.com/plantuml/png/ZLHDR-Cs4BthLqnzMGTGxTsasm0zhHEdoMwTZqPoWvu4IXpBt52aIb9nZAB_lKDAaQsuWEk39Syy3j-RUUClrZ7Zcah2o66nTaRaQB_RKVI3K8LiECBQkTh-CfqQjfcKmgsRlB5e2gqSAZSfT3Lz5gPOMxUUNlxquuDaoYrl5rDyfJn7Ji7iai1CA3IJccwAFa2Zw5n5vy6j4LPQIhqHgWH9862Amo0jZAKt3NGlI5qmARTKeoTuU46qcFrvlqopzFuXczy_tOrFeWzTQ9PaoMzNwUKDnRhGqzVq9bjSNL_TpIaOHGzeh5RPrQiRCwNLjjADpRpc64Qpjm0iAJ0wwS1ZLfO6I-QGzyW-yXxAAw64TOOveLKF7qJVZaJ9rZgiiWlTACxCTbnyYlS7DQ59dVmT0Nt2Lz-7yGRpZDKrePymXrbTIr64qYCAVMClB8QaDhxdjtzSnf3gYj9mFddr-PcVXmLFpVh6lmZSG8swbXX3UtCCdGDYm1TwKE2xpkaRNJ61bT4LpQuR5tZ2CN11zc4opFTh2XOBfxt88VDvFZOeCvuJZqUKWJCTcZF7ScRHqxlT9hyluFFaSyiseJ9e3_Y59rHOvQHYBMgACFbit_FD6Iyz_5gucoO7WxNkL1nG6w-4H1icGjV-IZ-WdS_8_vobPwTxT2mosWeGYkChsl-IgRJzIzA1EqroWa08PuD4hKezlu3JoUb0P6ZiOv9CPuvULeZSmZYNkWIYxUn9QAxR83fxIB-fENF1RSlsxSqBSEvHLalqJXdr00krqK5qt1KTzYdSrla0j086jbWZRoHoe649p-6VtiH-eTn6k9P2shuHOY_T_hzGjhrbcFGoBUKkw1dKHUIFWnNT6Pzso7ejDsdwa12UqCCzFGuVxkhH8-5CdzwpCUFTw7p3DaRurZhjZzBefz_c5xI2jJOEpiu-_ao51dLshXlKUWyBTXeYzeoq4GRzD9qkjEmkEpt_-EcyevqjUtiS8queTeJzeDo0_rCl_W0N11nfr_-LiwkwSzmrkjxG8DHAcogCTRSpVTlwYGvAxTn9q665N3SEwYQNee12SsptGpXj11wf6cpT5UsNgR52bNxH0xb-sOUblDO5ssQF_J_chjMK-eAADvNy5m00 "techtribesjs")


### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](http://www.plantuml.com/plantuml/png/bLHVRzis47_NfxXv3qs1D6wBFUsfZcsixPpOjHm4Un9EqjaYGf44IJbrXttt7MMRfLiDoF8GaSVZxyyTpn-SH-kxLiAe9UTmHsNdHjalGbMogmaQxutxVJos-7op4xxf-9XifPKdvMygtOwVXAqQvvlnzBStAudAFzmjnlILpskgELXCEHc58djZc2Tx1PtYUotV1zyGRBMK-bce7KXE0bGrN1mBwtYbWNb1wWgbF3165FWpGUQUX39eiOLdY-PHrBw1zs_V9l4MlzuTtURY6_M7sMBor_9XKsoMgsAsVBo_UfszEeKcUP7_ETzCFtBi57hyjFbOBEP_pEzd7Coo5LcdrLNLEQzRijSmZQlH1CxX4QVc1-UfBMvrfsgqXwlg7QUSi-6JschReXTQZLx3tra6_1VzNQ4nQVR462cgOpR7F-CUNMM5yTSmKRjEeWtXIQYlYo9SA6QBYis70WiBnkgjaCJgBkcYdSAHtOkAKkxy63hpNaDkR6ZYhTO-13SDWT52UT1RmAeYvu2zHHaWKgi_Cf_UOi6lZR5ElOBRpWNeDPQby7TVUXgBoXbjVG_EwK859jgJykvdN4iXbtKcbjRdMEfftPM7y9rQGayELD0gXQCQQlJOiqKmC9qrsj408NQry0dP9EnJekcluvlx-IOiLrRlHSraskvG2TVNviqpXw272KnRh8JavG3NhFpUiBfCUpL3ZoMwdczfiP84xzvNOPTxRSczh2cC7nq7WhHoASFT8V-oIC3nNBnlLCEUh6Fm_b586HlslQXOGwEh_rDRPaag6tQ1VBud5RTHI-8FiDITFxqKy0rwQ71F_CyOKbGptpzPjYQPJFLn_Xw26lv-t6nMEQU5f69z7Cw1aNamREu_YWp1_ow0eJkewXe-vylxyGNmOc0CZpfoKhMB1dH0UQGorzKJURxTgngudCnM18dQkbvi0jhZ3A2aJosMj--YEFuOpMwd9mkNqpmqWYyJSG4J1-l543t607iC3LavKV_0bhwyUEF4rT_95dWeraDi5qYS-85rTwty5m00 "messagebus")


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
