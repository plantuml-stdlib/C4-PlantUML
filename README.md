# C4-PlantUML

![Container diagram for Internet Banking System](https://www.plantuml.com/plantuml/png/hLPlZzh64txFfvYGH0690_sKNzvKEYaSkCr5S4Snb_GT6di7UvNrhhkxvWvL_UwTDJO-k5IfrBu1x-pEypmxVyR-w3nQNnMgzmvIe_TaFKWFZzBdW498Bur6nLj5WLg0afe0RLOLf3rSpTVHOhgv_H9jR-zcYuTvTDqVzy4Rg1o1CYagTUYzaZjukqShCL6qfIVfl1lqBptxmnx0AwbJLGc2yMGydip-lvqPxP4vxRWC6b-HSlJyNEvzwNwQJ2m-ZZFMN2NCR5FsOdrZLZqf5UfmloldXP89WrwjWkbXkPWKw3pPx_9e8NUzNlpf_kjs5QtZ-xlj_SDcSNiN3OOSgGrc3bnLbiPwq0PSYIava1fyJg2n81Waw4Y0EPegBSXoyAJE872IyOUIt0WUSvdc88n-vrl05WtreJ2MXcDWnjlToMm9BFrU4UE8bb9Hnf97pJzuUcfoM3j1ZYva9I4Gj9EQH6ygHAGeP97lCkWdc7vZnrCO-YDui-F5p2XZhzz4YsWPtMssFz_pp-n-SR_c_IGxxlPVlt__OJxz47nSZYLTHpBBVIm5YJYi1qFUEIhRiB3hbWtIbWu655p01PzXVnZahKdLqj0TT1gm-LAjdkbwpObfXOIY_DkDs1yKNS_HvIGMKhEOC_G0FlblA8pt7KNFIwy8JW458J6pMC3EMBZLdgmc3pUeluMIY0_EKz7hhSWwemTfvRmfo8vWTdhgJw4rWzdLIK_OUtHCSraxegfjW6bgAkrTdtKSeRStR11e3uFqVunrAQ0_X3zw0D3f7JnIiiMovCDVAO5fMIgPOfW6VJPznZsE82vj4B_yCWksEIcvPncrDEVvR0fD8m9gKPjFl4bxyTMKHPupkn8PBkPjHLShp2YmjwnnQcNfHp3LMQNG1lFAchqKeJEK-ZxBhjBfSP19Vm1lE99r81ti9GONQO7l2uarZuxi2qM5IQIY9XpBi3XfchqUmMzO84VYN0ieMSZGeQvA77dEsJ_Mvbw8Eme0GNkPqgMyUJ8Gw37Ccv26vZ6eYNzTmDdQ6qiEmeW4IvbqtjOf1QcvB8lwUGHvtIk0bSyXjIH8UudAZK9PaNEWJCOBykduHQ2QnkP8oL2ngzll5yxSy37R-Pr5xWSH2a5XuBfRCNFNBqONY_hpLFRHanzGWL9jNMrWekXgoUkcvGBp9YUGDIagMChK6cTs7gAdD4UT4Hmz6VOPPgEjGsLClRDOq4LFTs4FvTbMGSg6zdxFWm-OcCft9J0wjV88l4Nji8v45_xUcjIpST4rxOCZ5xW_RJQhc0-UdtCb_l1CK_GTN4EtlGkpEZ7TYAZXkW7G8DN6yu9e2UjvEuBF_5gTrEHTDkkj1g5JyE-0jZVitCdkckKST4qe7EoiAUfvzMYb9mVU1AA6PtupOyWJvhDeNHHPpB0Ew2fOQunEo7azdccuzAiSrqT77oytAmOwoy6P-qLLTd7gtd8yhPQBorXrsmn__EXPHBz4T_F1iBSpnfC5OV5H7zyrxUSJxCVmDYHS6ZqOrZ7hFgx2BY-_jDkzZwooAjHV "Container diagram for Internet Banking System")

C4-PlantUML combines the benefits of [PlantUML](https://plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures – especially during up-front design sessions – with an intuitive language using open source and platform independent tools.

C4-PlantUML includes macros, stereotypes, and other goodies (like VSCode Snippets) for creating C4 diagrams with PlantUML.

- [C4-PlantUML](#c4-plantuml)
  - [Getting Started](#getting-started)
  - [Supported Diagram Types](#supported-diagram-types)
  - [Relationship Types](#relationship-types)
  - [Layout (arrange) elements (without relationships)](#layout-arrange-elements-without-relationships)
  - [Global Layout Options](#global-layout-options)
  - [Sprites and other images](#sprites-and-other-images)
  - [Custom tags/stereotypes support and skinparam updates](#custom-tagsstereotypes-support-and-skinparam-updates)
  - [Element and Relationship properties](#element-and-relationship-properties)
  - [Version information](#version-information)
  - [Snippets for Visual Studio Code](#snippets-for-visual-studio-code)
  - [Live Templates for IntelliJ](#live-templates-for-intellij)
  - [Advanced Samples](#advanced-samples)
  - [Background](#background)
  - [License](#license)

## Getting Started

At the top of your C4 PlantUML `.puml` file, you need to include the `C4_Context.puml`, `C4_Container.puml` or `C4_Component.puml` file found in the `root` of this repo.

To be independent of any internet connectivity, you can also download the files found in the `root` and activate the local conversion with additional command line argument `-DRELATIVE_INCLUDE="."` (that the local files are included)

```plantuml
java -jar plantuml.jar -DRELATIVE_INCLUDE="."  ...
```

If you want to use the always up-to-date version in this repo, use the following:

```plantuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
```

Now let's create a C4 Container diagram:

\(If you don't want run PlantUML locally you can use e.g. the [PlantUML Web Server](https://www.plantuml.com/plantuml/uml/ZOxDIWGn48JlUOeufn5qSjcJfvNHsugBFsV99iqcsEc4T0VTjpSCE2AYUAeAgVwgjYosIakevytBBK824bPdaHms3pg85BuofjgtwHWbj4DZg2wJzDpaSZAliRh04ioykToZ9Nc-snbux_yUlEdGkOTj9AXJwJLAxQ5ofh4iSetHyeKUTlO0E7HpNoHcigXlW5sDosiuLojaT9_kn-aJk40Py_7q1-Znn09fv4N-swuU0ByFNbVyZlYQqmbR8DyIVW00) too.)

After you have included `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `Person_Ext`, `System`, `System_Ext`, `Container`, `Relationship`, `Boundary`, and `System_Boundary`

```plantuml
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

Take a look at the following sample of a C4 Container Diagram:

```plantuml
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

Entities can also be decorated with icons/sprites using the $sprite parameter, for example:

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define DEVICONS https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/devicons
!define FONTAWESOME https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/font-awesome-5
!include DEVICONS/angular.puml
!include DEVICONS/java.puml
!include DEVICONS/msql_server.puml
!include FONTAWESOME/users.puml

LAYOUT_WITH_LEGEND()

Person(user, "Customer", "People that need products", $sprite="users")
Container(spa, "SPA", "angular", "The main interface that the customer interacts with", $sprite="angular")
Container(api, "API", "java", "Handles all business logic", $sprite="java")
ContainerDb(db, "Database", "Microsoft SQL", "Holds product, order and invoice information", $sprite="msql_server")

Rel(user, spa, "Uses", "https")
Rel(spa, api, "Uses", "https")
Rel_R(api, db, "Reads/Writes")
@enduml
```

![Sprites/Icons](https://www.plantuml.com/plantuml/png/hP9BZzem4CVl-HHUr0ChBPj3sqkbIek0Tf5uK1v5FQ59F05NZfrw9l3rEmvXD-f3wg4dE_EV-VyyCtaYXi1rQPCxut9RQrGdvee-f6c0o-FHyAdEQiAGUyVe-37tPLfPSB5cGAojoTBHky4gXdRpMLe2CGO97KPI0SPXUAoYVtAdiP1FDPvydOwMYyq_WBYkG8Uthq0Zwg2GZ05LmJ3IZQVn73LweNnQBhR3_MIpd4_-AwY9mGN9bpXu_pgrMrSfk6DjeMtwT_axdE5lMaa_x84mdF7NyautQNmxjJET3RyjTzl3VhfzFimcdoUBSVy-ILQIu5q_9ZwetgWczYM6djnNw2kBYa_0oY5gLGMlwvn9n3VNJZ_s6a3lFdbPO9ygaEBDQXWzsWRZTNj2LKgACeun592trYpnlCLUDH26kiZikw2RKnS5bH7ZuMeQ_UEmulaCJbia1TOgsPqa4YdhZoRlsiNihjSuw-jCgiV0a05XT9gRF7Zo1QlDbrbZxQscsnWUb0yQWnASFFliJOvo5ZwKmCQxBgopAs4cQxJjlA-psX5Ij6z-FKc8UgD8Vt-M3-jhxysJrmYQqdr4HVa9dPPz_mG0 "Sprites/Icons")

Similar to icons/sprites is it possible to add links to all elements and relationships:

```plantuml
@startuml Basic Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(admin, "Administrator", $sprite="person2", $link="https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/LayoutOptions.md#hide_person_sprite-or-show_person_spritesprite")
System_Boundary(c1, "Sample System", $link="https://github.com/plantuml-stdlib/C4-PlantUML") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", $descr="Allows users to compare multiple Twitter timelines", $link="https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/LayoutOptions.md")
}
System(twitter, "Twitter", $link="https://github.com/plantuml-stdlib/C4-PlantUML")

Rel(admin, web_app, "Uses", "HTTPS", $link="https://plantuml.com/link")
Rel(web_app, twitter, "Gets tweets from", "HTTPS", $link="https://plantuml.com/link")
@enduml
```

> `png` itself supports no links, therefore the following image is generated as `svg` image.
> Github does not support `svg` links in README.md.
> If you click on the image a new window is opened and there you can use the links.

![Click on the image that the links are working](https://www.plantuml.com/plantuml/svg/jP9FYzH04CNl-HHjhuTPc4dOnPCmiECWUjZLOB9w39rqQHhxJrDL8GpYTxTxizb5F8W3vf0chrBl_NZ93R52dfmjNXW_s4c369aZlQugL7FvpV0uzHC13i4pU2w7uAfebSyxEs9jJLyTN-tgBDtVtLPE4GCcgJkc3MKyO1cpVr43Kl0RfPtnMo4F-JJ4g3YWt8gN5D4mx6LyUEywIzRuxtkv0YqmVoNeRUXNZ5jr2XD_Z6o2fzBfYz5ew9Q4RWdS1TpH6ERVrUKkBulcb8nSzoPCNYiyROQhnDue5os8PNOkgBmKFmgHhgUYDZFqdOen9No1NXnYj6PGcLqcwNYn5OUcBZ-yRTCAWhWkhyJTvsFErq03xkN1sZ2JoD-B10UH2A9246woR39nEnjcGC76GM86-Yyjfzf-FXQtuIKnyJzcdrzNKNm2k_u_prNT4r3kvttRrisVxglbWtyU9QFiysJmJFWEcD8ZvECh1lUFhZVWTP9-0G00 "Click on the image that the links are working")

Elements and relationships can be decorated with tags and explained via a calculated legend, for example:

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("v1.0", $borderColor="#d73027")
AddElementTag("v1.1", $fontColor="#d73027")
AddElementTag("backup", $fontColor="orange")

AddRelTag("backup", $textColor="orange", $lineColor="orange", $lineStyle = DashedLine())

Person(user, "Customer", "People that need products")
Person(admin, "Administrator", "People that administrates the products via the new v1.1 components", $tags="v1.1")
Container(spa, "SPA", "angular", "The main interface that the customer interacts with via v1.0", $tags="v1.0")
Container(spaAdmin, "Admin SPA", "angular", "The administrator interface that the customer interacts with via new v1.1", $tags="v1.1")
Container(api, "API", "java", "Handles all business logic (incl. new v1.1 extensions)", $tags="v1.0+v1.1")
ContainerDb(db, "Database", "Microsoft SQL", "Holds product, order and invoice information")
Container(archive, "Archive", "Audit logging", "Stores 5 years", $tags="backup")

Rel(user, spa, "Uses", "https")
Rel(spa, api, "Uses", "https")
Rel_R(api, db, "Reads/Writes")
Rel(admin, spaAdmin, "Uses", "https")
Rel(spaAdmin, api, "Uses", "https")
Rel_L(api, archive, "Writes", "messages", $tags="backup")

SHOW_LEGEND()
@enduml
```

![tags](https://www.plantuml.com/plantuml/png/bLJTRjfC4BtFK-pdhnT6JN3I7qMgX1G4gAb4MWg9Sed6ti5ikzwrTjRGl7rdrn08jLBrQj7CcJbppeov8G_EDvK--q-PGZSInThxcZvbcODjlrH-tUGDeIkiyMXylx1LLcimeUQ2lDGgpqOVBcOXz70tpIeWZuv3on5NW3Be-dNeVpQKSgAnuYRtKAR9vgf_cPoBDxbr4jt8Qki6oV_o-ltbk-karu6-2kWLD_qRDeVYPrEVeAq3KoA30tgE-WJfyTS9aeEQf-yCBloJHZ4GOw0roYb7qXvtdg4ZQz9Wrxb8HWrvMw7ZecI6jkOAlmOl3A8KjREoAJmblNqLo4ePXWx3gyWxyFQFMZWaaJY4put4Ha4C6DoAu9RWJTNMi2aK1K99WsWZKpwl9gKQc68n6mOcbjXeYAJttAbYY536erj1qGuG6OgTi3O7WNpBTn8dY5izfhiyfHiUwnJTp73imR-Ei3VW5TLGgp31x4iW_04R2Eyj6AcH16Wj-EGPI2IqBLKXql1jz0_Myh6W8MKDzLwAVNjADSvJcNFpCNZ8WJ0GtQd2MR8hBnRVfv7PQadxJPwB-448deRLRQmgaD-LTHLuPdofmnLhjS6WfVsLX9-DL3uCNYfJXi22JMHT7yKJWZiSm_xw-N3dg7TNszx30o65olXNm82GZnashZkzdBUcHh5p14dPerCUT-dzTH_jlvkZJRz6D6s93j9RdW2ha0XAx9IukFtsk9nEFa--ZjFUsGqQsLJwDm00 "tags")

## Supported Diagram Types

> * `arg`.. argument required (e.g. `alias`)
> * `?arg`.. argument optional  (e.g. `?descr`)

* System Context & System Landscape diagrams
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml`
  * Macros: 
    * `Person(alias, label, ?descr, ?sprite, ?tags, $link)`
    * `Person_Ext`
    * `System(alias, label, ?descr, ?sprite, ?tags, $link)`
    * `SystemDb`
    * `SystemQueue`
    * `System_Ext`
    * `SystemDb_Ext`
    * `SystemQueue_Ext`
    * `Boundary(alias, label, ?type, ?tags, $link)`
    * `Enterprise_Boundary(alias, label, ?tags, $link)`
    * `System_Boundary` 

* Container diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml`
  * Additional Macros: 
    * `Container(alias, label, ?techn, ?descr, ?sprite, ?tags, $link)`
    * `ContainerDb`
    * `ContainerQueue`
    * `Container_Ext`
    * `ContainerDb_Ext`
    * `ContainerQueue_Ext`
    * `Container_Boundary(alias, label, ?tags, $link)`

* Component diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml`
  * Additional Macros: 
    * `Component(alias, label, ?techn, ?descr, ?sprite, ?tags, $link)`
    * `ComponentDb`
    * `ComponentQueue`
    * `Component_Ext`
    * `ComponentDb_Ext`
    * `ComponentQueue_Ext`

* Dynamic diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Dynamic.puml`
  * Additional Macros: 
    * `RelIndex(index, from, to, label, ?tags, $link)`
    * (lowercase) `increment($offset=1)`: increase current index (procedure which has no direct output)
    * (lowercase) `setIndex($new_index)`: set the new index (procedure which has no direct output)
    * `LastIndex()`: return the last used index (function which can be used as argument)

    following 2 macros requires V1.2020.24Beta4 (can be already tested with https://www.plantuml.com/plantuml/)
    * `Index($offset=1)`: returns current index and calculates next index (function which can be used as argument)
    * `SetIndex($new_index)`: returns new set index and calculates next index (function which can be used as argument)

* Deployment diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Deployment.puml`
  * Additional Macros: 
    * `Deployment_Node(alias, label, ?type, ?descr, ?sprite, ?tags, $link)`
    * `Node(alias, label, ?type, ?descr, ?sprite, ?tags, $link)`: short name of Deployment_Node()
    * `Node_L(alias, label, ?type, ?descr, ?sprite, ?tags, $link)`: left aligned Node()
    * `Node_R(alias, label, ?type, ?descr, ?sprite, ?tags, $link)`: right aligned Node()

Take a look at each of the [C4 Model Diagram Samples](samples/C4CoreDiagrams.md).

## Relationship Types

* `Rel(from, to, label, ?techn, ?descr, ?sprite, ?tags, $link)`
* `BiRel` (bidirectional relationship)

You can force the direction of a relationship by using:

* `Rel_U`, `Rel_Up`
* `Rel_D`, `Rel_Down`
* `Rel_L`, `Rel_Left`
* `Rel_R`, `Rel_Right`

In following sample a person uses different systems, and a group of persons which have bidirectional relationships

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
HIDE_STEREOTYPE()

Person(a, "A")
Person(b, "B")
Person(c, "C")
Person(d, "D")
Person(e, "E")

BiRel_U(a, b, "talk with")
BiRel_R(a, c, "talk with")
BiRel_D(a, d, "talk with")
BiRel_L(a, e, "talk with")

Person(x, "X")
System(s1, "S1")
System(s2, "S2")
System(s3, "S3")
System(s4, "S4")

Rel_U(x, s1, "uses")
Rel_R(x, s2, "uses")
Rel_D(x, s3, "uses")
Rel_L(x, s4, "uses")
@enduml
```

![(unidirectional) relationship versus bidirectional relationship](https://www.plantuml.com/plantuml/png/RP11QuD044Rl_eeq9mED4lNKKneLMh1KD87s9AiEZNHTPNSaxR_lZ59KoF6zntuCUpGeD0wjj1uQLScXXiqLiJTFhgl5pVbgy3gKWm5TTGf1eLDrhTjBeVZDtc0jcz8DWttAwlAMkAqm29fK4T8BqIZGJi_xBwzHNEJdE8lVpvzfREyiAmLjEcMBnytsURlxnvBmD6D56CvO4qOp0c5CQ9sQ36HnuJ4UG26_DpUwdjgKCaxLtHHngk-cX1Eiqdpu3_aFulpN8BIsEH3dXuNmM7WBuRFm5o9W4V3cT3vDZZE30KDsEfobjvRHAFsrJ4OPpF88ggQ__mC0 "(unidirectional) relationship versus bidirectional relationship")

## Layout (arrange) elements (without relationships)

In rare cases, you can force the layout of elements which have no relationships by using:

* `Lay_U(from, to)`, `Lay_Up(from, to)`
* `Lay_D(from, to)`, `Lay_Down(from, to)`
* `Lay_L(from, to)`, `Lay_Left(from, to)`
* `Lay_R(from, to)`, `Lay_Right(from, to)`

In following sample a person uses different systems, and a group of persons which have no relationships

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
HIDE_STEREOTYPE()

Person(a, "A")
Person(b, "B")
Person(c, "C")
Person(d, "D")
Person(e, "E")

Lay_U(a, b)
Lay_R(a, c)
Lay_D(a, d)
Lay_L(a, e)

Person(x, "X")
System(s1, "S1")
System(s2, "S2")
System(s3, "S3")
System(s4, "S4")

Rel_U(x, s1, "uses")
Rel_R(x, s2, "uses")
Rel_D(x, s3, "uses")
Rel_L(x, s4, "uses")
@enduml
```

![Relationship versus Layout](https://www.plantuml.com/plantuml/png/LSt1QeD04CRnkq-HvgJGA55FFQLLeGLBHIEq9rbrQ8HrbTrPshnzPmn5Svl_3_RRaq6XqOxIUHXK9sqFkmlYR9w2G8iV_tl0Yssj0TrD2a6XtqrZC4kX-Ct1O2-7DaZYGy5Kl-V1A0o29ceIUY461TgVUV_rBSsQwfoLsSVvgyXSpt4Aq6PIhdZSxP_ttd-sb2zhTfJ9cZrbkYPGPfHEBgvDpLEjjzmbtztjJldkRtVEDwoV_zB09mrKLuCmkkP8NHqt43A46uWOeWt43361Ku9iQfvSPgm1GyfOBXZUOxfWT8_vWl6A9r2z7UKV "Relationship versus Layout")

(In combination with [SHOW_FLOATING_LEGEND()](LayoutOptions.md#show_floating_legend)) a greater distance between an element and the
e.g. floating legend could be required that all e.g. corners of the drawing area can be reached.

* `Lay_Distance(from, to, ?distance)`: Sets the distance between `from` and `to` with down alignment (Lay_Distance(from,to,0) equals Lay_D(from, to)). The default alias of the floating legend is LEGEND().

In following sample the floating legend should be in the left bottom corner of the drawing are.
(The normal SHOW_LEGEND() call requires no extra Lay_Distance() call and the legend is automatically drawn below the diagram on the right side)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define DEVICONS https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/devicons
!define FONTAWESOME https://raw.githubusercontent.com/tupadr3/plantuml-icon-font-sprites/master/font-awesome-5
!include DEVICONS/angular.puml
!include DEVICONS/java.puml
!include DEVICONS/msql_server.puml
!include FONTAWESOME/users.puml

Person(user, "Customer", "People that need products", $sprite="users")
Container(spa, "SPA", "angular", "The main interface that the customer interacts with", $sprite="angular")
Container(api, "API", "java", "Handles all business logic", $sprite="java")
ContainerDb(db, "Database", "Microsoft SQL", "Holds product, order and invoice information", $sprite="msql_server")

Rel(user, spa, "Uses")
Rel(spa, api, "Uses")
Rel_R(api, db, "Reads/Writes")

SHOW_FLOATING_LEGEND()
Lay_Distance(LEGEND(), db, 1)
@enduml
```

![db below legend, 1 unit distance](https://www.plantuml.com/plantuml/png/hL5DZzem4BtdLtXH3o0jH5NRIwLAYu3THUA30bkEqH0FuCgnKyy4r7_VCIIxKQjAFVGKvptFUtvl7eWXS5NOvCwut5OQrOcvfCzf6k0oE1e-LVkACEJUCJeUvBv8ImikplI9jJNxTFInluhGotoM5a2CGQ1i91DW78P16VMJEuq7-LNZoRVfQBdO_8CHLoNeyE7Dq0ZRFyYDFfN1C5BZf_4SENfrULmkjiFTPBESJ_whqHM32v8liF-fQUqjLGhkM5ceG_z9VuSp_8qhw8VD2CCPVnjlfqdZswdkT2L7xxeHkbUTKKNi2mmTEQ_GbnOLdu2LGzIg35vNEPEGxswPldIkKfrUyhggBfKWmvlLC6hKKU9nUq9Lo1Lb76CuG5vBi-1vRNlZG3pKHLfk6pLARIieZGWFLzEe7sk9tsTmsY8fi5R9bkGYaRB-QFAsNBpTrXhlktelqsDWs0DXL9gRF7Zo1rQRhxEhjBUQcXhkbGyQWn8xUVRPcnpbU_2X03RUjSrQMn7FP8ssxllMrGiX2HxXAn1ZjT5iVKjwVU0QGLEwYyAHJZRFortsE5iEjzF5KpQRF4qMusulcS7FR6o8mUNORT2RnFjUye1Eo_P_0G00 "db below legend, 1 unit distance")

## Global Layout Options

C4-PlantUML also comes with some layout options to make it easy and reusable to create nice and useful diagrams:

* [LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT() or LAYOUT_LANDSCAPE()](LayoutOptions.md#layout_top_down-or-layout_left_right-or-layout_landscape)
* [LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype)](LayoutOptions.md#layout_with_legend-or-show_legend)
* [SHOW_FLOATING_LEGEND(?alias, ?hideStereotype) and LEGEND()](LayoutOptions.md#show_floating_legendalias-hidestereotype-and-legend)
* [LAYOUT_AS_SKETCH() and SET_SKETCH_STYLE(?bgColor, ?fontColor, ?warningColor, ?fontName, ?footerWarning, ?footerText)](LayoutOptions.md#layout_as_sketch)
* [HIDE_STEREOTYPE()](LayoutOptions.md#hide_stereotype)

C4-PlantUML also comes with some person sprite/portrait options:

* [HIDE_PERSON_SPRITE()](LayoutOptions.md#hide_person_sprite)
* [SHOW_PERSON_SPRITE(?sprite)](LayoutOptions.md#show_person_sprite)
* [SHOW_PERSON_PORTRAIT()](LayoutOptions.md#show_person_portrait)
* [SHOW_PERSON_OUTLINE()](LayoutOptions.md#show_person_outline) (requires PlantUML version >= 1.2021.4)

## Sprites and other images

`$sprite` (images) can be defined with following PlantUML supported options:

* included (standard library) sprites via their `{SpriteName}`; details see [sprites](https://plantuml.com/sprite)
* images via `img:{File or Url}`
* OpenIconic via `&{OpenIconicName}`; details see [openiconic](https://plantuml.com/openiconic)

Size of the displayed images can be changed with `,scale={factor}`.
Color of the displayed images can be changed with `,color={color}   `.

(If sprites are defined via $tags then the calculated legend is updated too)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

'stdlib users.puml defines sprite "users"
!include <office/users/users.puml>


AddRelTag("plantuml", $textColor="$ARROW_COLOR", $lineColor="$ARROW_COLOR", $sprite="img:http://plantuml.com/logo3.png{scale=0.3}", $legendSprite="img:http://plantuml.com/logo3.png{scale=0.1}", $legendText="console triggered")

Person(user, "user group displayed with a sprite", $sprite="users")


Container(container, "Container with scaled and colored OpenIconic", $sprite="&folder,scale=5.0,color=gray")

System(system, "System with an image", $sprite="img:http://plantuml.com/logo3.png")

Rel(user, system, "Rel with image (via tags)", $tags="plantuml")
Rel(user, container, "Rel with OpenIconinc", $sprite="&folder")

SHOW_LEGEND()
@enduml
```

![Sprite, image and OpenIconic](https://www.plantuml.com/plantuml/png/bP91RzGm48Nl_XL3L45MsYP5XSkAe5PB1KWBMwL572itddKjENPaEvGLuhypjfTi3d3OKvonvvltddtb0tTXx3LxeKodHu7m5CBWLtNj-7CbLNWQ7qUFhhCce0bLP_jwqDp4ddCVX5QFzVhD-MqiVVkogNlk0pegFQofWok3hXeYdxtAfo7IVAg1m1qTyE07fm92aRQAevHtThTJ7TQfNXyRtpF6heLeKTzpMHP_zHHBE0luCwojjgufpgxRTllzORtTRDkufMdMVxQoWAPGlLn5_wjwCfaSQoljPJKO-SjtN6DpKLt-JaYKQCJToTslPzttfBWfA5zlDK9mIafqA8e5OxTas9eo6b_cT40wEmuWbAS9UnJmJ3S4_93Wt4hEaY1ikeYoowj4cwePaPG9u4P05pEYzNP0yvbQL3VdljnPBOYGhRojBfRfV2CTtyTnTtiVi2zz-j2S_7_GQK3rNE99aKTeY_gGmiIbKe9c8fG_58V0fLz4U5mqntUnc06c3EQCoQhvbzTawnEzbytDnvkl7ye5kq8Z2Fm7 "Sprite, image and OpenIconic")

Relationship specific sprites are typically smaller and therefore following options are possible:
* use smaller icons (like the $triangle in the following sample)
* use an additional scale factor (direct as part of the argument, or via a variable)
* if sprite argument starts with `&` an OpenIconic name can be used too (details see https://useiconic.com/open)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(user, "User")
Person(user1, "User 1")
Person(user2, "User 2")
Person(user3, "User 3")

System(system, "System")

' normal sprites are too big 
Rel_L(user, user2, "informs", "courier", "normal sprites are too big", $sprite="person2")

' scaled sprites are ok
Rel_R(user, user3, "informs", "courier", "scaled sprites are OK", $sprite="person2,scale=0.5")

' combine sprite and scale to a new sprite
!$combinedSprite="person2,scale=0.5"
Rel_R(user, user3, "informs", "courier", "combined sprites are OK", $sprite=$combinedSprite)

' special smaller sprites can be used
sprite $triangle {
    00000000000
    00000F00000
    0000FBF0000
    0000FBF0000
    000F999F000
    000F999F000
    00F66666F00
    00F66666F00
    0F3333333F0
    0F3333333F0
    0FFFFFFFFF0
    00000000000
}
Rel_R(user1, system, "orders", "http", "small sprites, like the small triangle", $sprite="triangle")

' if sprite starts with &, sprite defines a OpenIconic, details see https://useiconic.com/open/
Rel_D(user, user1, "requests", "async message", "if sprite starts with &, it defines a OpenIconic like &envelope-closed", $sprite = "&envelope-closed")
@enduml
```

![Relationship with sprite or OpenIconic](https://www.plantuml.com/plantuml/png/bLJVQnin37w_lq8DeMiXoQN9DiWWKDPnCDRHqjBdujXAOkgpRvPlMHdxt-SVSPEikK7rujCdIzyd8TybEMPTMwlYH6gkMe6mTgwXJsLfsMQqacxTBbf2oursgDs8cxfi5DCXPqXEABaehzuFRmFqyFswh1avj1vwl0ePlzoe2TMBMxHaz5aeDO3UWpzwv_lWnHQ5YqDyal798JxD-DJZnVspPwtFA1u-almGUGVQs9efeCPAXmJC8ZXZO25NKDoXUhpUYifiKYzz1lNy9pUjbMZ3PtSL7-qdUDvhei198YRE58g35FCKAU_sAAUTb4VoRxuTOHl4Y_Fnw4FYvQPUI8tRH61Q92bUC33GkDb6YfF-zgguxwpu1hsvMBVYV_YysZ2c1haCe_NpLMXViZdJiC30AOg4GTzPoVHA8VmkmDjuPpk_ElIhpzN__6escrNTVlKnMDNbLzDaLPUVRVnAxvyysRJyBwjhh40RHniUOZZZOF9O1g3a4u9R8oGyZsH_CJAMza4kyoh4nqwmaMuDfuEC2bnAZGGCRXhKNxdHaWyywfXK18IxNuBNAcCu_WQClrt6BhxizYC-P8i_MYGNks3qh3dKICHM681EET8TbP8QFaNz4vMd779b2CMkNPX3xrNqlBX4BTfQ_GK0 "Relationship with sprite or OpenIconic")

## Custom tags/stereotypes support and skinparam updates

Additional tags/stereotypes can be added to the existing element stereotypes (component, ...) and highlight,... specific aspects:

* `AddElementTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?techn, ?legendText, ?legendSprite)`:
  Introduces a new element tag. The styles of the tagged elements are updated and the tag is displayed in the calculated legend.
* `AddRelTag(tagStereo, ?textColor, ?lineColor, ?lineStyle, ?sprite, ?techn, ?legendText, ?legendSprite)`:
  Introduces a new Relationship tag. The styles of the tagged relationships are updated and the tag is displayed in the calculated legend.
* `UpdateElementStyle(elementName, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?techn, ?legendText, ?legendSprite)`:
  This call updates the default style of the elements (component, ...) and creates no additional legend entry.
* `UpdateRelStyle(textColor, lineColor)`:
  This call updates the default relationship colors and creates no additional legend entry.
* `RoundedBoxShape()`: This call returns the name of the rounded box shape and can be used as ?shape argument.
* `EightSidedShape()`: This call returns the name of the eight sided shape and can be used as ?shape argument.
* `DashedLine()`: This call returns the name of the dashed line and can be used as ?lineStyle argument.
* `DottedLine()`: This call returns the name of the dotted line and can be used as ?lineStyle argument.
* `BoldLine()`: This call returns the name of the bold line and can be used as ?lineStyle argument.

Each element can be extended with one or multiple custom tags via the keyword argument `$tags="..."`, like `Container(spaAdmin, "Admin SPA", $tags="v1.1")`.
Multiple tags can be combined with `+`, like `Container(api, "API", $tags="v1.0+v1.1")`.

**Element specific tag definitions**

Sometimes an added element tag is element specific and all element specific colors should be used, e.g. a specific user role should be defined as element tag with the specific colors `...PERSON_...` like
```plantuml
AddElementTag("admin", $fontColor=$ELEMENT_FONT_COLOR, $bgColor=$PERSON_BG_COLOR, $borderColor=$PERSON_BORDER_COLOR, $sprite="osa_user_audit", $legendText="administration user")
```
Therefore element Add...Tag() shortcuts are added which use the specific colors as default values and the call can be simplified like
```plantuml
AddPersonTag("admin", $sprite="osa_user_audit", $legendText="administration user")
```

Following calls introduces new element tags with element specific default colors:
* `AddPersonTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?legendText, ?legendSprite)`
* `AddExternalPersonTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?legendText, ?legendSprite)`
* `AddSystemTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?legendText, ?legendSprite)`
* `AddExternalSystemTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?legendText, ?legendSprite)`
* `AddComponentTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?techn, ?legendText, ?legendSprite)`
* `AddExternalComponentTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?techn, ?legendText, ?legendSprite)`
* `AddContainerTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?techn, ?legendText, ?legendSprite)`
* `AddExternalContainerTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?techn, ?sprite, ?legendText, ?legendSprite)`
* `AddNodeTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing, ?shape, ?sprite, ?techn, ?legendText, ?legendSprite)`
  (node specific: $type reuses $techn definition of $tags)

**Comments**

* `SHOW_LEGEND()` supports the customized stereotypes
      (`LAYOUT_WITH_LEGEND()` cannot be used, if the custom tags/stereotypes should be displayed in the legend).
* `SHOW_LEGEND()` has to be last line in diagram.
* Don't use space between `$tags` and `=` (PlantUML does not support it).
* Don't use `,` as part of the tag names (PlantUML does not support it in combination with keyword arguments).
* If 2 tags define the same skinparam, the first definition is used.
* If specific skinparams have to be merged (e.g. 2 tags change the font color) an additional combined tag has to be defined. Use `&` as part of combined tag names.

* Colors of relationship tags cannot be automatically merged (PlantUML does not support it).
  If one tag modifies the line color and the other the text color, an additional combined tag has to be defined and used.

**Sample with different tag combinations**

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

UpdateElementStyle(person, $fontColor="green")
AddElementTag("v1.0", $fontColor="#d73027", $borderColor="#d73027")
AddElementTag("v1.1", $fontColor="#ffffbf", $borderColor="#ffffbf")
AddElementTag("v1.0&v1.1", $fontColor="#fdae61", $borderColor="#fdae61")
AddElementTag("fallback", $bgColor="#444444")

' If spaces are requested in the legend, legend text with space has to be defined (incl. all other additional details)
AddElementTag("microService", $shape=EightSidedShape(), $legendText="micro service (eight sided) (no text, no back color)")
' If no special tag names should be displayed in legend, no explicit legend text definition is required (all additional details are automatically calculated) 
AddElementTag("storage", $shape=RoundedBoxShape())

UpdateRelStyle(black, black)
AddRelTag("service1", $textColor="red")
AddRelTag("service2", $lineColor="red")
AddRelTag("service1&service2", $textColor="red", $lineColor="red")

Container(spa, "SPA", "angular", "The main interface that the customer interacts with via v1.0", $tags="v1.0")
Container(spaAdmin, "Admin SPA", "angular", "The administrator interface that the customer interacts with via new v1.1", $tags="v1.1")
Container(api, "API", "java", "Handles all business logic (incl. new v1.1 extensions)", $tags="v1.0&v1.1+v1.0+v1.1")
Container(spa2, "SPA2", "angular", "The main interface that the customer interacts with via v1.0", $tags="v1.0+fallback")
Container(spaAdmin2, "Admin SPA2", "angular", "The administrator interface that the customer interacts with via new v1.1", $tags="fallback+v1.1")

Container(services, "Services", "techn", $tags="microService")
Container(fileStorage, "File storage", "techn", $tags="storage")

Rel(spa, api, "Uses", "https")
Rel(spaAdmin, api, "Uses", "https")
Rel_L(spa, spa2, "Updates", "https")
Rel_R(spaAdmin, spaAdmin2, "Updates", "https")

Rel_D(api, services, "uses service1 via this call", $tags="service1")
Rel_D(api, services, "uses service2 via this call", $tags="service2")
Rel_D(services, fileStorage, "both services stores via this call", $tags="service1&service2+service1+service2")

SHOW_LEGEND(false)
@enduml
```

![merged tags](https://www.plantuml.com/plantuml/png/jLLHRzis47xthxXvGsV1hbrxnGeC2D0ipTO2sHR42VOOdCIpn8qYDVBa9Fz-Hz4AvCfRq8Vw8PJ8xxxxxjCTypumUcvhC_b6syAqYg1YRi9FgvN7XsMfkMhpDf0ld6Mol2nSlMeCsXZpEh0oEbzTl7rz7RVkVhjQrHYOl6pTNqW4Qaj-sKJ-oLsZaEdIK2qyMtuoD6l81sSNyDrEi1VEE7ysBJsHdMQJSwKEs5iiPzFzUlbcUepyLhtxuStcNTpDdLVaZ_TFSgm_vzZ9Bz-DETB-QHslJX8ff1_NOwAqFoRQeJ4v5dzt4MMFVjlz13tv7Zxj83HOK03q19x-QIamAT0Mk28mL99LYyCAJ8yC3vgh50GL1c07EO6YdROIDujVU0cI5vmGU42bD6jdqGY6KPimKbdhmhij-RqkA2eD5JPqTgdBYhTQaTh6zrac9qd6hQWuIr4GKXZCAC8XH7m6C-iwhGkGXsW05B7sR9gbacKtD5HeDC1OWiMQ0eJAjKPrnUZG67nADlGMI0mzDaONceTsfCgx4a67pa7jen5YmRZuP3Esx6faNGZc2UHlqHhaAFnpQm8xZ-N0bHlNMYdnP_TuS2Nhc_w6J6hut4Z12-YMpcivIMJ9gwv_H7hVLQ9sUWgtYJYZBRs0Mx_g0yR49oacprCx2mqkOBgzFf_AWhOK7tnylAq8Qe60jan-5tkDA-Ik9uisY7taqnaM759BxZL2Fy6CPJXByvmTfpjNjRQIeLlXT6QCPpgmHx7_IoLOUe0qkmCPwoCPsEYeuFfJJFWNxZ6k7z4gGw4RdRmD0Wm1Z2jrqGzLpmnYCTcWdGtPKPPqQSpZqtoKL6hV9AytNytiUN_Xd7HzCxHzy_LzxyNqNWmbfOuDqP33OnJ1L5JscU3uOXfMjDE6jcaq9UeNUOD-KiSi_Oa8aCb9BPywu2wajDr_GpbFnyci_y7SNoMImnTDupy2tGoe-gV_W7Vu3waj1ywqahf_NtSUSwK3n5jhK5qwZ_w-pB9vWMNJimm-qB7NkUFgcRqpNPRJfEFxQTxlp0Vv9jkFV_nvVtNvw-Nl7sRICe6ooNkoggtDlm00 "merged tags")

**Sample with tag dependent sprites and custom legend text**

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define osaPuml https://raw.githubusercontent.com/Crashedmind/PlantUML-opensecurityarchitecture2-icons/master
!include osaPuml/Common.puml
!include osaPuml/User/all.puml

!include <office/Servers/database_server>
!include <office/Servers/file_server>
!include <office/Servers/application_server>
!include <office/Concepts/service_application>
!include <office/Concepts/firewall>

AddExternalPersonTag("anonymous_ext", $sprite="osa_user_black_hat", $legendText="anonymous user")
AddPersonTag("customer", $sprite="osa_user_large_group", $legendText="aggregated user")
AddPersonTag("admin", $sprite="osa_user_audit,color=red", $legendSprite="osa_user_audit,scale=0.25,color=red", $legendText="administration user")

AddContainerTag("webApp", $sprite="application_server", $legendText="web app container")
AddContainerTag("db", $sprite="database_server", $legendText="database container")
AddContainerTag("files", $sprite="file_server", $legendText="file server container")
AddContainerTag("conApp", $sprite="service_application", $legendText="console app container")

AddRelTag("firewall", $textColor="$ARROW_COLOR", $lineColor="$ARROW_COLOR", $sprite="firewall,scale=0.3,color=red", $legendText="firewall")

Person_Ext(anonymous_user, "Bob", $tags="anonymous_ext")
Person(aggregated_user, "Sam, Ivone", $tags="customer")
Person(administration_user, "Bernd", $tags="admin")

System_Boundary(c1, "techtribes.js"){
    Container(web_app, "Web Application", "Java, Spring MVC, Tomcat 7.x", $tags="webApp")
    ContainerDb(rel_db, "Relational Database", "MySQL 5.5.x", $tags="db")
    Container(filesystem, "File System", "FAT32", $tags="files")
    ContainerDb(nosql, "NoSQL Data Store", "MongoDB 2.2.x", $tags="db")
    Container(updater, "Updater", "Java 7 Console App", $tags="conApp")
}

Rel(anonymous_user, web_app, "Uses", "HTTPS", $tags="firewall")
Rel(aggregated_user, web_app, "Uses", "HTTPS", $tags="firewall")
Rel(administration_user, web_app, "Uses", "HTTPS", $tags="firewall")

Rel(web_app, rel_db, "Reads from and writes to", "SQL/JDBC, port 3306")
Rel(web_app, filesystem, "Reads from")
Rel(web_app, nosql, "Reads from", "MongoDB wire protocol, port 27017")

Rel_U(updater, rel_db, "Reads from and writes data to", "SQL/JDBC, port 3306")
Rel_U(updater, filesystem, "Writes to")
Rel_U(updater, nosql, "Reads from and writes to", "MongoDB wire protocol, port 27017")

Lay_R(rel_db, filesystem)

SHOW_LEGEND()
@enduml
```

![tags with sprites and custom legend](https://www.plantuml.com/plantuml/png/dLJTRkCs4xttKt2DlN00nyewNxu0HRDOnqwxNJYRr3_DfJ0Inx9QYbH9AevHzDqxf6tHiPMVDbSHvvmpXpE7_c8iQ5iLelKXbwceEBAbjQNv8Oeqh7fPRfTLKXdKgP8MfUsbgeXA0T9nJetb8a-YuVzExztH_7OS5M0iQZgAXyI0NABkbKw_zO7ZWZwPCd1F1-_eCzHWbiYBNF9er-1KbIWDffNExHfqkimjfhRIs3_DYMks1i9rjksYeIeA9RsNu-BSa6SGObCEzH_LOf6d64rHFw8s4GSB2HYCZJ_u_39oaOjteA0iHPw2pPLy6Ko3JB6q9d88EeZtMA_15xd65GZnkTKQS7xpP55B4FVKLyaPP9qsI2NNXQfCZ4-stMKVJKbJnQksCX2xPSI9WFIFU0c-AZ13oMU4lGfKvd3j4zTXJpcjZ5K5waPH0Jh3EDEgAezaiqnZ1XPviowuC3IAGiLpsqsLKFfA8m_2qsQaIK7WrLclVn58HsvSjznOxKUzS-GirTdshbQO3CfotzRnNW-rYSC8nTAT4YaV2VDaNpI4hq4nb5-NTBaq-whke5dHbzYczBee5Gy6q13LGtKY6INmQ0fEVeB22-yYxBYMM4E_glR7mMHozn0FxyPt4ozBrAPIC5GhrOi_Vsdl0UlCRC8Nq-lfr9dtEUgozhLAl378pDN1OphP4ZiXqJlM58ek--LHIGpa-hq4thFirHrHInve7kHSJjV6OX5VgqfoqEjE-ed05jEbrNc2flUxQP_yrMBqLo-kGmbqwo7W0sLny6nHxM_m25tctexCsErlmowRgOBAxBBt5FflWt_oN7cKT3IAc2UaGulqcY3OQ9jF9t-xdluwPXUzYtqrdXmgTNnQ_Ts8z9EBu-QcRVSvc9tt0zj36wn8PVuK1F-kN4jdWasjqXiRIcPgTCtwlVuRHggIW_Khc6_-sms9NJgK3x8RHTYeaflH_DrgqH2EmXEcFpTedDhNsUn-6WH223q_vEY_2Xm6wj-AU9MQiBTXu8Ojj2eOICvMxhaPPfKJeub7tqRNb9vIQSlEpy_-lt4JTCA6dsaTmdPR38Zz_Qt89IkriYfLOjkiVtdswN9hEvw71RvXd53mbliWT-3_eRxy4IvSe7bSxxxE6DRnf7vWeJsLfb_fbszyy_FDzr7dfFK59QyAyGy0 "tags with sprites and custom legend")

**Custom schema definition**

If the custom (color) schema is defined via `UpdateElementStyle()` then the legend of existing elements is updated too.

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

!$COLOR_A_5 = "#7f3b08"
!$COLOR_A_4 = "#b35806"
!$COLOR_A_3 = "#e08214"
!$COLOR_A_2 = "#fdb863"
!$COLOR_A_1 = "#fee0b6"
!$COLOR_NEUTRAL = "#f7f7f7"
!$COLOR_B_1 = "#d8daeb"
!$COLOR_B_2 = "#b2abd2"
!$COLOR_B_3 = "#8073ac"
!$COLOR_B_4 = "#542788"
!$COLOR_B_5 = "#2d004b"
!$COLOR_REL_LINE = "#8073ac"
!$COLOR_REL_TEXT = "#8073ac"

UpdateElementStyle("person", $bgColor=$COLOR_A_5, $fontColor=$COLOR_NEUTRAL, $borderColor=$COLOR_A_1, $shadowing="true")
UpdateElementStyle("external_person", $bgColor=$COLOR_B_5, $fontColor=$COLOR_NEUTRAL, $borderColor=$COLOR_B_1)
UpdateElementStyle("system", $bgColor=$COLOR_A_4, $fontColor=$COLOR_NEUTRAL, $borderColor=$COLOR_A_2)
UpdateElementStyle("external_system", $bgColor=$COLOR_B_4, $fontColor=$COLOR_NEUTRAL, $borderColor=$COLOR_B_2)
UpdateRelStyle($lineColor=$COLOR_REL_LINE, $textColor=$COLOR_REL_TEXT)

Person(customer, "Personal Banking Customer")
System(banking_system, "Internet Banking System")

System_Ext(mail_system, "E-mail system")
System_Ext(mainframe, "Mainframe Banking System")

Rel(customer, banking_system, "Uses")
Rel_Back(customer, mail_system, "Sends e-mails to")
Rel_Neighbor(banking_system, mail_system, "Sends e-mails")
Rel(banking_system, mainframe, "Uses")

SHOW_LEGEND()
@enduml
```

![custom schema](https://www.plantuml.com/plantuml/png/dPHVRzem5CNVyodI34qWyIU4KA99I6rOj5LAeUAFjhV8YIyGrN6GxQZqsy-9iyMqwIeXNk1tpxdt7jlYZWl4H94HuoQb2Iamc4SXJlpRQCJGo_2GYcCH5nnOabC1L0oJF1kT2AAbPy059cayMhY3fnBj7iDHXhW09b6qA1rdCJoLtOsRpc8LhjRHVJGrvwRrPRQVnBPdQTojU3oPUlQjpYSL1zjpngxEdOhlSUpTJdG-LXp0ZhK-os2tNT-7gZOhFqtDhptOmmXYdQiPiODYxEXSxUJPimbATAuoJ5rdvdawLvaTRDkkrdyTX57ui0nQcgdYDlYzlIWQknD60W826L2n4Qy4kjO96C-frJSxyM6HavpDcxEMS9zJeV3bKPJwd65WRpnZMU17XFENb1xcbc05MBtMmN0Mm2WYqOSR-5Ti86-ZVHn_vGAorfpk5JcTJq9zECw_OfpVZ5i3KQCw9AMWgPe7qJU_2ZXhxRNtq3ECf-gukqd1HPu1wvkM8eYOFgBFyjhCHLsJDxUfSdHZLQbZISy3BOE2-ETHGkceBL5m5jqCfQJn18FojybhvHiXtJEKWPGz_ltUqbl6rpP_jzME0vSogOfyb3nhqijDDa0nDw7QXviYhprBI0z7UVxlulx7hQnj3XMYsShO_5pzYiBWHx3ytkqPTx9B-UVs1m00 "custom schema")

## Element and Relationship properties

A model can be extended with (a table of) properties that concrete deployments or more detailed concepts can be documented:

* `SetPropertyHeader(col1Name, col2Name, ?col3Name, ?col4Name)`
  The properties table can have up to 4 columns. The default header uses the column names "Name", "Description".
* `WithoutPropertyHeader()`
  If no header is used, then the second column is bold.
* `AddProperty(col1, col2, ?col3, ?col4)`
  (All columns of) a property which will be added to the next element.

Following sample uses all 3 different property definitions (and the aligned deployment node).

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Deployment.puml

' default header Property, Value
AddProperty("Name", "Flash")
AddProperty("Organization", "Zootopia")
AddProperty("Tool", "Internet Explorer 7.0")
Person(personAlias, "Label", "Optional Description (with default property header)")

SetPropertyHeader("Property","Value", "Description")
AddProperty("Prop1", "Value1", "Details1")
AddProperty("Prop2", "Value2", "Details2")
Deployment_Node_L(nodeAlias, "Label", "Optional Type", "Optional Description (with custom property header)") {

  WithoutPropertyHeader()
  AddProperty("PropC1", "ValueC1")
  AddProperty("PropC2", "ValueC2")
  Container(containerAlias, "Label", "Technology", "Optional Description (without property header)")
}

System(systemAlias, "Label", "Optional Description (without properties)")

' starting with v.2.5.0 relationships support properties too
WithoutPropertyHeader()
AddProperty("PropC1", "ValueC1")
AddProperty("PropC2", "ValueC2")
Rel(personAlias, containerAlias, "Label", "Optional Technology", "Optional Description")
@enduml
```

![properties sample](https://www.plantuml.com/plantuml/png/XP9HRzCm4CVVyobCNfPANR9L82IUDdKWaCfMGG69b-gQ78qbnsVPPqP0V7TiQrsxBYLFFfz_T_R_Vxvo39Pzfx8NKjVADoXQPkFUL9M5-t8hkVKRxz3Mf1arbpLrbL6WOysvuqR9JJL_URwCgIyV5rK7Zj66rFe6ZQA-YqKcNf2TYGP_W5SiMeG6hLXQCcYvdugle3ncrqspInNvBNIOJqN-Je5hyydJmpkx1Ir_0qlI4VfEn6Ga77Ch8XNFFsX6gv75srz6aKKhNfSN0LwYTQGBavPh9S45U04RJ5Lt9lO79MxGrLQcdIZkWoUFIip3LG-I9g5dzXbvzuBtALlaktq-pQFK9EoWwV6pOtGPcGJ7AD0CKhdB8NJsYCuEq5b0zpDOtrA3wqMXmt9QwAetEAAyzewf6n0k_cIP4Dy2G_xOW4auUVRi-LvY28UHlRGGHcHEEgZJeMUzYvx9MM7TQbAqxV-lXVpW0F-64VQEiIjSMeRi6kyeqQNVS2OSGzZghKZ-_IndvQloGbXK40kTSDuOieU5WecoKqwE-ZZguYTKJx_yaPL3KiSz3OslK3U-K_y0 "properties sample")

## Version information

C4-PlantUML offers version information like PlantUML with its `%version()` call.

* `C4Version()`: Current C4-PlantUML version (e.g. `2.4.0beta1`).
* `C4VersionDetails()`: (Floating) version details with the current PlantUML and C4-PlantUML version. (It can be referenced via the alias `C4VersionDetailsArea`.)

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

' existing plantuml version as text
%version()

' new C4-Plantuml version as text 
C4Version()

' new C4-Plantuml version details (incl. PlantUML version) as table
C4VersionDetails()

' version functions used in e.g. footer
footer drawn with PlantUML v. %version() and C4-PlantUML v. C4Version()
@enduml
```

![version sample](https://www.plantuml.com/plantuml/png/ZOynJyCm48Nt_8fZGBH3dQKJKwKmWiG2Axh4r-GavnBvpgG_dvXWjGjIfqJltllytaaDewKnL0yiNKYUO32RzRck8owkPnjIcvHYDucHcEkciPu3IiuSr7pWjcwEX_SiVRozrYEgKLobhsPD80j5DsT-zGHqOJMM7We0lYagJmAeO7Inwl5FsEspNsY1pFx73LLp_Bp7xycGWy8kJtHGkfRx_XU8RQ0hy6MBRDp2EIVfRFrHI4eUM81Sx-0yJKQnsZxW8ou22zjmyv23wp90yQLckTuEEP7ujVqF "version sample")

## Snippets for Visual Studio Code

Because the PlantUML support inside of Visual Studio Code is excellent with the [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), you can also find VS Code snippets for C4-PlantUML at [.vscode/C4.code-snippets](.vscode/C4.code-snippets).

Project level snippets are now supported in [VSCode 1.28](https://code.visualstudio.com/updates/v1_28#_project-level-snippets).
Just include the `C4.code-snippets` file in the `.vscode` folder of your project.

It is possible to save them directly inside VS Code: [Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_creating-your-own-snippets).

![C4-PlantUML Snippets Video](images/vscode_c4plantuml_snippets.gif)

## Live Templates for IntelliJ

**Prerequisites**

[Graphviz download](https://graphviz.gitlab.io/download/)  
[PlantUML Integration](https://plugins.jetbrains.com/plugin/7017-plantuml-integration)

**Install**

1. Download [IntelliJ live template](intellij/c4_live_template.zip).  
2. Select `File | Manage IDE Settings | Import Settings` from the IntelliJ IDEA menu.
3. Specify the path to the downloaded ZIP file: `c4_live_template.zip`.
4. In the Import Settings dialog, select the Live templates checkbox and click OK.
5. Restart IntelliJ.

**Usage**

* Create new PlantUML file (.puml).
* Type `c4_` for displaying artifacts templates for C4-PlantUML
* Live template create correct C4 model artifact with stubbed arguments. 
  * E.g. alias, label, type, technology, description
* Replace stubbed arguments with desired values.

![C4-PlantUML Snippets Video](images/intellij_c4plantum_live_template1.gif)
![C4-PlantUML Snippets Video](images/intellij_c4plantum_live_template2.gif)

## Advanced Samples

The following advanced samples are reproductions with C4-PlantUML from official [C4 model samples](https://c4model.com/#examples) created by [Simon Brown](https://simonbrown.je/).

The core diagram samples from [c4model.com](https://c4model.com/#coreDiagrams) are available [here](samples/C4CoreDiagrams.md).

**techtribes.js**

Source: [C4_Container Diagram Sample - techtribesjs.puml](samples/C4_Container%20Diagram%20Sample%20-%20techtribesjs.puml)

![techtribesjs](https://www.plantuml.com/plantuml/png/ZLHDR-Cs4BthLqnzMGVGshj9jm5wMYTEazqw7uta1Zq9b3YMcLAaIb9nZAB_lKDAaQsuWEk39G_V3D-RUUElrZ7Zcah2o66nTaRaQ9_jAFf1g48s767jN6r_dauDsqnAuTPDtbWqXLOEbPiKkfhMaYbVugDrN8fyUldZnmSVMjukfXMp3Ws5ialAO4AXcTI4ZJv0eoYveYBWrWWhBQNU25M2910mnM5mB8obDmrqEKXTC2ctLADdUNX1j9ZzSRzCi_J-8PlVFzsDJw8FNMYMPCclL-db3SMwqDEtz2PRN5rVtSqf64KFQAnMsTMh6pEbrRRIZSsyy1X6ixS0B2amEkd0OrQM1alcaFV8Fl8UoYkXX7M6EQ5L3nz4trAYP6iTLjc5RXHdPZikFiVxqvhGk4x-Ze0-uQllmtY3USRgcj1FcCEihgKeGkaHXRwp5nP3KXlVyzlVBsD8TKN7S3vvzUSpFmyBdfhrZNyHk84QTIqnXlRc63eRn80lzA30iyxf6rqnWPNH5Ssk6nTumZ5mGHvYCiptMmeM2wUzo27pUJusA3EU4uz7b84p9SsPOpcpwEdTRfFV5l1bygLbcr0Pj0VymXCgh79IiHOrHPZyqxxdcpDUUlYrS3TD3WPhtQaue3PU2OasJ8Ik_OL-G3kVaVyvIyzEz-XOPAPOWr0SNz7-bqobxL-I4kuqoGa28UG6YLgLUdu1fvFJWSZGsCSacSuSlQmGkOLnBdK9HDlPaz1Sjq5qzf1-KtFcWjkMxTkR5-3SewoMw9qowW4MQgE3wBWhEknJkAtp0MW536onHjv8v4334fx3Fxs9_KAvZN0jXRHz8yJUSVidGwVjBSD3BzFIsGKzWxg8_76meZlZqmvPh-KcJHyImXDwkAV7uSDTFPeISlhZFHiptetEDsnZX6-jqpwLHZ_zFh-W5QorSN1szkadAZIeitFTeDPxMB3J4B5df8qmwAVfTA5bTzdf-QVFvntjRDdRunXnGh4Zx0Vb1loVUl47k23WIBl-hvnTrPtZhj7rXWQXLjfKOQoxdUdRrazqK6hdJe8EA-IwSL0tkHG559fZkn_2QIFmIDNErg5elqoD5QhqYnx8zSi-BEMrBjWsU-p_CNUjfgElg7XJoNy1 "techtribesjs")

**Message Bus and Microservices**

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](https://www.plantuml.com/plantuml/png/ZLNVRzis47xtNt7p1am6d1WTzZGWGFt3M5iuYMlPwADn4iyIKOeaICgfD-n_7odPAjqegFEGaCUxx_lkFb9vRnqQLrTYy0kNkQWPGUcSjdzD9WPVxWlkoZghBPbSIKVItUUgccY1CjJSMSS4poRpF-_M8RHxN4qgj8wC3-tdlWAv97El0_xlK4jVN7aGS2N1GGcXNhWiGFWaGCdWwfWRwrSAF3a8bQCG9u_HgNnDC9WojXGK4BPO9CEAvqQbP8uyf-4OVhCbQdfOyg9qAMV4qh1FHluaA-PAAFCmd2iZ3ruLcPcecwA3vpWVlfJSDJ511KcsfM_keIK1sx90GW4TR80V3KS_Ah9E6ImYCHjLIvywKzzwn8X6wTVJMr8y_Y3zyFnblrvkqkUd_VDkk_huj4nyU4t6AfdajMUio8nXtgs6KxY46u2JTLJjPq48cbEIl_CfbspuA0_ALEYuaiCH_3i0_zDDFK6ju-IfreBdRRAFVy8ZsjnmxSOmbKKjq8JmDBXkEmqsM5oXn8A2xTo0Dkh0HUZkckrIiJyFEwRkN6vfnv1g4sxMJ2aNWjkIG2ik7QW3O9wJjU0xwrG0ZnhretPOM7Y0-0gz5bHv52zxdzNMKposEvZLDZ1kCCkuU_pSi1kKLYlZ6awVpcKGG4UIphw2DHHIlVgeqSqb5dUwgRDJ-3itX8uioD21u9OOC7JOa7LWe6kZbILxStjOC-uY3TEmZ_ddlqxkdvRRi5mRTUICB2XJeEIs6UJTYmz10nC4733dmYzlbx38lflEijZl1JhCq3OodWtcWk3T7tdOfKuPiZyrjds9VOpTn09bFFcOy_6KVbv5T7WP_Z_4u4Z6UhhcgWdH-VtT56HGghp7crw5_RRuqyYKi0jobaUItRPJ5yq0C5ErEryzS2KwAF58_fVM98drA_XlCDYGs2-Y3qhxzdUjwE67xNQT-iHpMdFOyrvtcg5xmnq8Ooe26DgJpCVmoN_J9bV0k-GrPgiZ9SbirvKAA5yeIrN-bPolVgiuUi4TIAUjRiH6e0rE3qfqHxkPjsRpzaEucCtFBIHNZ7ql_JOHCKpxmcw7k4ZfOUz2lQsqr3-mnTUngsYvsfh12a_xJH_R5TBbVzbg-VVoQP6C1kzz5tKb_WS0 "messagebus")

## Background

[PlantUML](https://plantuml.com/) is an open source project that allows you to create UML diagrams.
Diagrams are defined using a simple and intuitive language.
Images can be generated in PNG, in SVG or in LaTeX format.

PlantUML was created to allow the drawing of UML diagrams, using a simple and human readable text description.
Because it does not prevent you from drawing inconsistent diagrams, it is a drawing tool and not a modeling tool.
It is the most used text-based diagram drawing tool with [extensive support into wikis and forums, text editors and IDEs, use by different programming languages and documentation generators](https://plantuml.com/running).

The [C4 model](https://c4model.com/) for software architecture is an "abstraction-first" approach to diagramming, based upon abstractions that reflect how software architects and developers think about and build software.
The small set of abstractions and diagram types makes the C4 model easy to learn and use.
C4 stands for context, containers, components, and code — a set of hierarchical diagrams that you can use to describe your software architecture at different zoom levels, each useful for different audiences.

The C4 model was created as a way to help software development teams describe and communicate software architecture, both during up-front design sessions and when retrospectively documenting an existing codebase.

More information can be found here:

* [The C4 model for software architecture](https://c4model.com/)
* [REAL WORLD PlantUML - Sample Gallery](https://real-world-plantuml.com/)
* [Visualising and documenting software architecture cheat sheets](https://www.codingthearchitecture.com/2017/04/27/visualising_and_documenting_software_architecture_cheat_sheets.html)
* [PlantUML and Structurizr - Create models not diagrams](https://www.codingthearchitecture.com/2016/12/08/plantuml_and_structurizr.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
