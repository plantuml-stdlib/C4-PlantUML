# C4-PlantUML

![Container diagram for Internet Banking System](https://www.plantuml.com/plantuml/png/bLLDZzis4BtxLqoTGnr0kqQ0ddgArpQwcwntrSZRJK_2Y1hRH2XI82axHj7_tg6i3yiEajGdQJJpvl7D6_gzysXzLQZHBr8BLUK4E-zBz_jqQl5mkvL-LsML8okCzgJzhJ3557ChKUzLLLRJ-MytiKBjNrQFKuMUdETGEkTib9hiRHcmVuLASs710E1t11kZb3b8lGN5IO0wXy5dQHq_6U36e8n0fOwCqJ6yRi1V7sT_Fx-iq_Lpd2wUNvycR_lOB4cJZylr_9w3JUZrONsVFYx_M3ujE3ZoqYl6RK4XbxYrM31H2mzySAl9mntgBu5pSdIUYj4e9kkCdeZAULEGZM3UFOrdq8R1REf3PLmTmO45XR8kH5N708KmbVPkp3nEqEaT1tAqnubunrYN1CPluPyHyA_ZEpbGbc9PSl8hPJ0hIoK5Ucdqc4CVS8yH9AKDv5T_pKDiGKhkcKPDZJtWfO1cnFKuGhZhcxK7ZsTCSjZPbOmzJlYpefiOjnIwjrqJOMNf8vZfRQNGXd1ipLxcv827-kqk6_PAe8vA-cDmWQXg8Hti9OOIQO7F2var1pRc5QF2P59H8yUgVcavpTz4y1aBP2M6NDY7XVIKWwionroQcVqCDtT5xaG0SjfBGPVq5jaaHuyPEWfZQ1u3c-JFHnYyUsEPMrW-iBILpblarY0rkxAefnl1ZfDpm8fT9IpbF3w9oaN1LEGSBy-MNyYBsokPCXHVIEUiamn-ZH--RPk5uJJRrmrq-u4-GH86vjR_TjPUVlKJAb2grDK1XblUhFYzMQk0lsRfPGtDExAImXfdDXwMNyKEDJliLCcmPvWDWnwLCVM6TvWkzlPCsc31PjA20zqfpXG6p4pb-p57tRf6mFFG3klpzYAFFf4wknBwnNnnv4Bl-_KwJZXnc7TQe-_d38nTfvxQfKyajxlCd5q39xXsoHkaEZWSUziGtL6B23uapq_Jy-RdBVzNPNh7sJsntl93b4-4kOEDDKLzwnmiBo7VIIOWDy2Bktbxpe1vfiU5ZHA6TK0t8LfZz4Gk73VaCAohNBXXk_R9QXqtGDrX1kLNlck52VNJHftF_EVOYlEUI_alwpy0 "Container diagram for Internet Banking System")

C4-PlantUML combines the benefits of [PlantUML](https://plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures – especially during up-front design sessions – with an intuitive language using open source and platform independent tools.

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

To be independent of any internet connectivity, you can also download the files found in the `root` and activate the local conversion with additional command line argument `-DRELATIVE_INCLUDE="."` (that the local files are included)

```csharp
java -jar plantuml.jar -DRELATIVE_INCLUDE="."  ...
```

If you want to use the always up-to-date version in this repo, use the following:

```csharp
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
```

Now let's create a C4 Container diagram:

\(If you don't want run PlantUML locally you can use e.g. the [PlantUML Web Server](https://www.plantuml.com/plantuml/uml/ZOxDIWGn48JlUOeufn5qSjcJfvNHsugBFsV99iqcsEc4T0VTjpSCE2AYUAeAgVwgjYosIakevytBBK824bPdaHms3pg85BuofjgtwHWbj4DZg2wJzDpaSZAliRh04ioykToZ9Nc-snbux_yUlEdGkOTj9AXJwJLAxQ5ofh4iSetHyeKUTlO0E7HpNoHcigXlW5sDosiuLojaT9_kn-aJk40Py_7q1-Znn09fv4N-swuU0ByFNbVyZlYQqmbR8DyIVW00) too.)

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

Take a look at the following sample of a C4 Container Diagram:

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

Entities can also be decorated with icons/sprites using the $sprite parameter, for example:

```csharp
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

![Sprites/Icons](http://www.plantuml.com/plantuml/png/hP9BZzem4CVl-HHUr0ChBPj3sqkbIek0Tf5uK1v5FQ59F05NZfrw9l3rEmvXD-f3wg4dE_EV-VyyCtaYXi1rQPCxut9RQrGdvee-f6c0o-FHyAdEQiAGUyVe-37tPLfPSB5cGAojoTBHky4gXdRpMLe2CGO97KPI0SPXUAoYVtAdiP1FDPvydOwMYyq_WBYkG8Uthq0Zwg2GZ05LmJ3IZQVn73LweNnQBhR3_MIpd4_-AwY9mGN9bpXu_pgrMrSfk6DjeMtwT_axdE5lMaa_x84mdF7NyautQNmxjJET3RyjTzl3VhfzFimcdoUBSVy-ILQIu5q_9ZwetgWczYM6djnNw2kBYa_0oY5gLGMlwvn9n3VNJZ_s6a3lFdbPO9ygaEBDQXWzsWRZTNj2LKgACeun592trYpnlCLUDH26kiZikw2RKnS5bH7ZuMeQ_UEmulaCJbia1TOgsPqa4YdhZoRlsiNihjSuw-jCgiV0a05XT9gRF7Zo1QlDbrbZxQscsnWUb0yQWnASFFliJOvo5ZwKmCQxBgopAs4cQxJjlA-psX5Ij6z-FKc8UgD8Vt-M3-jhxysJrmYQqdr4HVa9dPPz_mG0 "Sprites/Icons")

Similar to icons/sprites is it possible to add links to all elements and relationships:

```csharp
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

![Click on the image that the links are working](http://www.plantuml.com/plantuml/svg/jP9FYzH04CNl-HHjhuTPc4dOnPCmiECWUjZLOB9w39rqQHhxJrDL8GpYTxTxizb5F8W3vf0chrBl_NZ93R52dfmjNXW_s4c369aZlQugL7FvpV0uzHC13i4pU2w7uAfebSyxEs9jJLyTN-tgBDtVtLPE4GCcgJkc3MKyO1cpVr43Kl0RfPtnMo4F-JJ4g3YWt8gN5D4mx6LyUEywIzRuxtkv0YqmVoNeRUXNZ5jr2XD_Z6o2fzBfYz5ew9Q4RWdS1TpH6ERVrUKkBulcb8nSzoPCNYiyROQhnDue5os8PNOkgBmKFmgHhgUYDZFqdOen9No1NXnYj6PGcLqcwNYn5OUcBZ-yRTCAWhWkhyJTvsFErq03xkN1sZ2JoD-B10UH2A9246woR39nEnjcGC76GM86-Yyjfzf-FXQtuIKnyJzcdrzNKNm2k_u_prNT4r3kvttRrisVxglbWtyU9QFiysJmJFWEcD8ZvECh1lUFhZVWTP9-0G00 "Click on the image that the links are working")

Elements and relations can be decorated with tags and explained via a calculated legend, for example:

```csharp
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

AddElementTag("v1.0", $borderColor="#d73027")
AddElementTag("v1.1", $fontColor="#d73027")
AddElementTag("backup", $fontColor="orange")

AddRelTag("backup", $textColor="orange", $lineColor="orange")

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

![tags](https://www.plantuml.com/plantuml/png/bLJTJjjC4BtdAVRprukWGWBz4L8b9AA0IgNGfWJ49Hfx9ywswrrhPnpQj--COs884LMlTZLpPiwSsMEV4KFYfl9x_xbG-CQYMJBNz6aqIl0mB1qlcxmXJ4KCZ867HQn6jOUWDOV4rhjyDFbmEDFGxTLqL04n9WdTJwG2NC0qhBN_tjZQ2uyL1hw1Sf2jZeT7sO5vayTaCKsYZ-aq-z-Ul3zwTvBjxq0VAteXJV-6pQ7usTHRw9WWb2XWHL-Ztq8o_jf2Ij2xW2_APvWeXe7kvC1aauOuLfW4diqmrXuDBu5DGBIcJj4s1PEKTLLWAnS4EjRJ4IVW-A8M-YIIX73JoAmSj8603qPNOkGvwXX4ERKgeAJJTbT2kTd_W6eGYlbih4oYe_7Gajv8fqeWnWN6j82Y6q0PYaxOEWTA_Y1cQ2VedgwdEzgc6p_LQNOpmzCT_EC8cmMyeXfgfnFClYZX3rY1dfSGh4SouBqHNmkGoFXOki8Cz0COzgiLHs0W5mFjFnVxTflgF1_ON9gV0qCEX4fqvOeKAIxOpBzFM-ReBJs-v85fNMyWM56tYgv0EHSnLS32-5n7AfPkXQfbVSlqsbZ7EdZfGgc1ESSakZwQtmYfDqDdSJMkcBvpxTeFjuIabUttBW3DjnbPtExq_VLwgQtOQmHBexla6Blqexlxzz_DqQLV8vgkYNhf7O_SAYI24dTAd5z-kxkVNdo--7e-sDyxms3rp_C7 "tags")


## Supported Diagram Types

Diagram types 

* System Context & System Landscape diagrams
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml`
  * Macros: 
    * `Person(alias, label, ?description, ?sprite, ?tags, $link)`
    * `Person_Ext`
    * `System(alias, label, ?description, ?sprite, ?tags, $link)`
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
    * `Container(alias, label, technology, ?description, ?sprite, ?tags, $link)`
    * `ContainerDb`
    * `ContainerQueue`
    * `Container_Ext`
    * `ContainerDb_Ext`
    * `ContainerQueue_Ext`
    * `Container_Boundary(alias, label, ?tags, $link)`
* Component diagram
  * Import: `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml`
  * Additional Macros: 
    * `Component(alias, label, technology, ?description, ?sprite, ?tags, $link)`
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
    * `Deployment_Node(alias, label, ?type, ?description, ?sprite, ?tags, $link)`
    * `Node(alias, label, ?type, ?description, ?sprite, ?tags, $link)`: short name of Deployment_Node()
    * `Node_L(alias, label, ?type, ?description, ?sprite, ?tags, $link)`: left aligned Node()
    * `Node_R(alias, label, ?type, ?description, ?sprite, ?tags, $link)`: right aligned Node()

Take a look at each of the [C4 Model Diagram Samples](samples/C4CoreDiagrams.md).

## Relationship Types

* `Rel(from, to, label, ?technology, ?description, ?sprite, ?tags, $link)`
* `BiRel` (bidirectional relationship)

You can force the direction of a relationship by using:

* `Rel_U`, `Rel_Up`
* `Rel_D`, `Rel_Down`
* `Rel_L`, `Rel_Left`
* `Rel_R`, `Rel_Right`

Relationship specific sprites are not down scaled, they requires typically smaller icons.
Therefore if sprite argument starts with `&` an OpenIconic name can be used too (details see https://useiconic.com/open)

```csharp
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Dynamic.puml

Person(user, "User1")
Person(user2, "User2")
System(system, "System")

' if sprite starts with &, sprite defines a OpenIconic, details see https://useiconic.com/open/
Rel_D(user, system, "requests", "async message", "if sprite starts with &, it defines a OpenIconic like &envelope-closed", $sprite = "&envelope-closed")

' normal sprites are too big 
Rel_R(user, user2, "informs", "courier", "normal sprites are too big", "person2")

' special smaller sprites have to be used
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
Rel(user, system, "orders", "http", "only small sprites looks ok, like the small triangle", "triangle")
@enduml
```

![Relation with sprite or OpenIconic](https://www.plantuml.com/plantuml/png/VL9XYnCn4Fs-ls8inta7RLUh21M4Gu-0e7YStESZpKxReTbapMJlAE9_Tv9DMoskyoLvRp9lNYQvuQX3x5jRlI1dRDyWR6Fi-7rT1_qytr3SzgkUCHZl8heuDxwjEwjTgfbnR2ojwazlPtU9UlZwfMurHmn2FTxkdMx9pBkaNjrXOE-kajGK9W-ol9vS_yak2hqG-ljUHDehpelm0vP4zH9e3Tm5YWZPEiEpU8JBwO5jS4qE6JHywz1z5jzafi96JPQ1yNH1wKevdI_bvNHTtQDzl2qkZ-q3_kYH8qzahtdl3BJ8h3UOY54_5F_f1Ipj42xHFQ6LdZDZFMCZIXT5vWDCphF3pPqFhRQbcuW6XEWzh6W3sVTzyNsO9hcrL6JNnlU1CAJjk4hATlb15aD3xj1GEYi55iEnPgkVf4XgCFLggcBy8WRIRcCHVbOWyUeK9wp-nkgZ-XzMo-LIZMFrBeKQm-hD46eCbn1yxlTNckZvF_2XmP3dcRvGMhsp-poUqq2jzpi6lviE3nstM0uSffFgZllhwWPTqxVsDm00 "Relation with sprite or OpenIconic")

In rare cases, you can force the layout of objects which have no relationships by using:

* `Lay_U`
* `Lay_D`
* `Lay_L`
* `Lay_R`

In following sample a person uses different systems, and group of persons which have no relations

```csharp
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

![Relation versus Layout](https://www.plantuml.com/plantuml/png/LSt1QeD04CRnkq-HvgJGA55FFQLLeGLBHIEq9rbrQ8HrbTrPshnzPmn5Svl_3_RRaq6XqOxIUHXK9sqFkmlYR9w2G8iV_tl0Yssj0TrD2a6XtqrZC4kX-Ct1O2-7DaZYGy5Kl-V1A0o29ceIUY461TgVUV_rBSsQwfoLsSVvgyXSpt4Aq6PIhdZSxP_ttd-sb2zhTfJ9cZrbkYPGPfHEBgvDpLEjjzmbtztjJldkRtVEDwoV_zB09mrKLuCmkkP8NHqt43A46uWOeWt43361Ku9iQfvSPgm1GyfOBXZUOxfWT8_vWl6A9r2z7UKV "Relation versus Layout")

## Layout Options

C4-PlantUML also comes with some layout options to make it easy and reusable to create nice and useful diagrams:

* [LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT()](LayoutOptions.md#layout_top_down-or-layout_left_right)
* [LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype)](LayoutOptions.md#layout_with_legend-or-SHOW_LEGEND)
* [LAYOUT_AS_SKETCH()](LayoutOptions.md#layout_as_sketch)
* [HIDE_STEREOTYPE()](LayoutOptions.md#hide_stereotype)

C4-PlantUML also comes with some default person sprite options:

* [HIDE_PERSON_SPRITE()](LayoutOptions.md#hide_person_sprite)
* [SHOW_PERSON_SPRITE(?sprite)](LayoutOptions.md#show_person_sprite)

## Custom tags/stereotypes support and skinparam updates

Additional tags/stereotypes can be added to the existing element stereotypes (component, ...) and highlight,... specific aspects:

* `AddElementTag(tagStereo, ?bgColor, ?fontColor, ?borderColor, ?shadowing)`:
  Introduces a new element tag. The styles of the tagged elements are updated and the tag is displayed in the calculated legend.
* `AddRelTag(tagStereo, ?textColor, ?lineColor)`:
  Introduces a new relation tag. The styles of the tagged relations are updated and the tag is displayed in the calculated legend.

* `UpdateElementStyle(elementName, ?bgColor, ?fontColor, ?borderColor, ?shadowing)`
  This call updates the default style of the elements (component, ...) and creates no additional legend entry.
* `UpdateRelStyle(textColor, lineColor)`
  This call updates the default relationship colors and creates no additional legend entry.

Each element can be extended with one or multiple custom tags via the keyword argument `$tags="..."`, like `Container(spaAdmin, "Admin SPA", $tags="v1.1")`.
Multiple tags can be combined with `+`, like `Container(api, "API", $tags="v1.0+v1.1")`.

**Comments**

* `SHOW_LEGEND()` supports the customized stereotypes
      (`LAYOUT_WITH_LEGEND()` cannot be used, if the custom tags/stereotypes should be displayed in the legend).
* `SHOW_LEGEND()` has to be last line in diagram.
* Don't use space between `$tags` and `=` (PlantUML does not support it).
* Don't use `,` as part of the tag names (PlantUML does not support it in combination with keyword arguments).
* If 2 tags defines the same skinparam, the first definition is used.
* If specific skinparams have to be merged (e.g. 2 tags change the font color) an additional combined tag has to be defined. Use `&` as part of combined tag names.

* Colors of relationship tags cannot be automatically merged (PlantUML does not support it).
  If one tag modifies the line color and the other the text color, an additional combined tag has to be defined and used.

```csharp
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

UpdateElementStyle(person, $fontColor="green")
AddElementTag("v1.0", $fontColor="#d73027", $borderColor="#d73027")
AddElementTag("v1.1", $fontColor="#ffffbf", $borderColor="#ffffbf")
AddElementTag("v1.0&v1.1", $fontColor="#fdae61", $borderColor="#fdae61")
AddElementTag("fallback", $bgColor="#444444")

UpdateRelStyle(black, black)
AddRelTag("service1", $textColor="red")
AddRelTag("service2", $lineColor="red")
AddRelTag("service1&service2", $textColor="red", $lineColor="red")

Container(spa, "SPA", "angular", "The main interface that the customer interacts with via v1.0", $tags="v1.0")
Container(spaAdmin, "Admin SPA", "angular", "The administrator interface that the customer interacts with via new v1.1", $tags="v1.1")
Container(api, "API", "java", "Handles all business logic (incl. new v1.1 extensions)", $tags="v1.0&v1.1+v1.0+v1.1")
Container(spa2, "SPA2", "angular", "The main interface that the customer interacts with via v1.0", $tags="v1.0+fallback")
Container(spaAdmin2, "Admin SPA2", "angular", "The administrator interface that the customer interacts with via new v1.1", $tags="fallback+v1.1")

Rel(spa, api, "Uses", "https")
Rel(spaAdmin, api, "Uses", "https")
Rel_L(spa, spa2, "Updates", "https")
Rel_R(spaAdmin, spaAdmin2, "Updates", "https")

Person(user, "A user")
System(system, "A system")

Rel_D(user, system, "uses service1 via this call", $tags="service1")
Rel_D(user, system, "uses service2 via this call", $tags="service2")
Rel_D(user, system, "uses both services via this call", $tags="service1&service2+service1+service2")

Lay_D(api, user)
SHOW_LEGEND(false)
@enduml
```

![merged tags](https://www.plantuml.com/plantuml/png/jLJVRzCm47xFNs4Acb9rQzSmCGbfqgPjOaW5glqGZzCbkIO6nubybuxzzzXENLeQLl6mlDYv-_nzf-_EFYS6mssbeZTIPwhDKPJC3NsSJ0myZGl9PPksX2QhDQFcSLPNaqQ1TcUEY7CbqydboT7SXHw-p2OL4AEneSTBUmAaHZDk77_qqEJ0UAsmiZnt_AmmRj1GhG_5kuN5NjQgDcU3mY3gmJ2woFCLzXwAUB2SZey7syYt-Udxu-JKHTFQv6YsuxqSqxyv5lPB5piS8TvRnq4lKGxuOTf3vEExH0jGAeNifpzH1FI9_onwPTSjgiwgL5dieV2Bvx8PpqDebZ93hypuAzHZC1_quHA7KrBZ7jpq81pe8UwZYDRzZgc1Gp6ucryCx0AwQ1KOjxqlKLGM8gHcD0l8K709BDZ6ivQuhj1qESYOn9FaKYmbYD1xXeBEkaaORijTv9NKLi6lebyPN4uI6-3Q_6y96fz4wFgwZEbM6T18Ly7yinFy0KjmwmteN249K4gaBLaWaL1r8JCHkmitNZCBQp5gahMcuOPA6BUHsursHAc1fFCwUJMpHs5KUrrFDcrFNj_tK4pm8hA3sqrSru07GdBI_XcpUPSEjRw0UPnr92j3_UtR1TrkK8NTF-3Ht3zkiNiydKN2RMpyxfaOgvZyuXFTrgQynDNgn1fWVqc4M-bDuLAIo42fFww4l6NPIvBi8KbU94bhBWCJxIjd_OYCGcIq8HBDuDcg-9uuAMlEpRVlZxFhJzTVhsBRQC9XT8uwRolr6m00 "merged tags")

**Custom schema definition**

If the custom (color) schema is defined via `UpdateElementStyle()` then the legend of existing elements is updated too.

```csharp
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
UpdateRelStyle($lineColor=$COLOR_REL_LINE, &textColor=$COLOR_REL_TEXT)

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

## Element properties

A model can be extended with (a table of) properties that concrete deployments or more detailed concepts can be documented:

* `SetPropertyHeader(col1Name, col2Name, ?col3Name, ?col4Name)`:
  The properties table can have up to 4 columns. The default header uses the column names "Name", "Description".
* `WithoutPropertyHeader()`
  If no header is used, then the second column is bold.
* `AddProperty(col1, col2, ?col3, `?col4)`
  (All columns of) a property which will be added to the next element.

Following sample uses all 3 different property definitions (and the aligned deployment node).

```csharp
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

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

![properties sample](https://www.plantuml.com/plantuml/png/ZP9HRzCm4CVVyobCNaYbhc4L4X9FcpeGI6Mhe834ItLDZiQIuxFiiqP0V7VEqRfiQO0z-NB--P_xnRa839vZQx9dsbOcrgWQPXTUbwM7syL1SnFtCQ2lo39QNbJKbiw0JMVE0jT6xylLoxDDQdt-i2vR28nUMhihT8QwDXrowGNPSrNZTuY6LODGerSRJmuzTtFr1Kp4xBAkZwqYluOMyxdAtne8JJvxl7dZ3s3rJs1DDa7VY9YSXZ6t9J9f_xrbz1PPlVaXGtdqwjNYXS0Rz85iuVhbqcW80gzXZ_sf6vVomQWh39NN_PCgRZKtzoRkxbLtIZF9p3uX7oTurtUB_FYSp_Easeiz21sFdQhpnFImL8bcq2QSJw7BUtJv05qAEjp1xffgtAqBAylVHRUTm_-OLp4mjHFYwbUMAVLL68hZ3p2JdPEnLuEYbDF8e2PbGbPanSvAPdMiJdIsM3MM31swVxjGdBp0ttA5NM1iYz0lu_od9MeC_T_m4StZ_sjgxb7k82095sZhs9e_ "properties sample")

## Snippets for Visual Studio Code

Because the PlantUML support inside of Visual Studio Code is excellent with the [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), you can also find VS Code snippets for C4-PlantUML at [.vscode/C4.code-snippets](.vscode/C4.code-snippets).

Project level snippets are now supported in [VSCode 1.28](https://code.visualstudio.com/updates/v1_28#_project-level-snippets).
Just include the `C4.code-snippets` file in the `.vscode` folder of your project.

It is possible to save them directly inside VS Code: [Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_creating-your-own-snippets).

![C4-PlantUML Snippets Video](images/vscode_c4plantuml_snippets.gif)

## Advanced Samples

The following advanced samples are reproductions with C4-PlantUML from official [C4 model samples](https://c4model.com/#examples) created by [Simon Brown](https://simonbrown.je/).

The core diagram samples from [c4model.com](https://c4model.com/#coreDiagrams) are available [here](samples/C4CoreDiagrams.md).

### techtribes.js

Source: [C4_Container Diagram Sample - techtribesjs.puml](samples/C4_Container%20Diagram%20Sample%20-%20techtribesjs.puml)

![techtribesjs](https://www.plantuml.com/plantuml/png/ZLHDR-Cs4BthLqnzMGVGshj9jm5wMYTEazqw7uta1Zq9b3YMcLAaIb9nZAB_lKDAaQsuWEk39G_V3D-RUUElrZ7Zcah2o66nTaRaQ9_jAFf1g48s767jN6r_dauDsqnAuTPDtbWqXLOEbPiKkfhMaYbVugDrN8fyUldZnmSVMjukfXMp3Ws5ialAO4AXcTI4ZJv0eoYveYBWrWWhBQNU25M2910mnM5mB8obDmrqEKXTC2ctLADdUNX1j9ZzSRzCi_J-8PlVFzsDJw8FNMYMPCclL-db3SMwqDEtz2PRN5rVtSqf64KFQAnMsTMh6pEbrRRIZSsyy1X6ixS0B2amEkd0OrQM1alcaFV8Fl8UoYkXX7M6EQ5L3nz4trAYP6iTLjc5RXHdPZikFiVxqvhGk4x-Ze0-uQllmtY3USRgcj1FcCEihgKeGkaHXRwp5nP3KXlVyzlVBsD8TKN7S3vvzUSpFmyBdfhrZNyHk84QTIqnXlRc63eRn80lzA30iyxf6rqnWPNH5Ssk6nTumZ5mGHvYCiptMmeM2wUzo27pUJusA3EU4uz7b84p9SsPOpcpwEdTRfFV5l1bygLbcr0Pj0VymXCgh79IiHOrHPZyqxxdcpDUUlYrS3TD3WPhtQaue3PU2OasJ8Ik_OL-G3kVaVyvIyzEz-XOPAPOWr0SNz7-bqobxL-I4kuqoGa28UG6YLgLUdu1fvFJWSZGsCSacSuSlQmGkOLnBdK9HDlPaz1Sjq5qzf1-KtFcWjkMxTkR5-3SewoMw9qowW4MQgE3wBWhEknJkAtp0MW536onHjv8v4334fx3Fxs9_KAvZN0jXRHz8yJUSVidGwVjBSD3BzFIsGKzWxg8_76meZlZqmvPh-KcJHyImXDwkAV7uSDTFPeISlhZFHiptetEDsnZX6-jqpwLHZ_zFh-W5QorSN1szkadAZIeitFTeDPxMB3J4B5df8qmwAVfTA5bTzdf-QVFvntjRDdRunXnGh4Zx0Vb1loVUl47k23WIBl-hvnTrPtZhj7rXWQXLjfKOQoxdUdRrazqK6hdJe8EA-IwSL0tkHG559fZkn_2QIFmIDNErg5elqoD5QhqYnx8zSi-BEMrBjWsU-p_CNUjfgElg7XJoNy1 "techtribesjs")


### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![messagebus](https://www.plantuml.com/plantuml/png/bLHVRzis47_NfxXb3qs196wBFUsfZcqixPpOjHm4Un9EqjacIf44IJbpXttt7IMReHSLQFCGYJyTVt-EF7zq7grl6maN3Jc7MofRTv7z8bGbsvfWvxrnluz65fzljiBlMlvCjjBAa_8tbMv6Hg8A1DVErrAKeyblryi0FTxFHmqwJvQXOi8xK2YoDuPhipVGAjxSC0du7S56IwcVXTg2v290LSFPPs4TlsbWSP2wGYaFp15TlXR8t5UX35fiuDcYUHArty67T-yIlC6_x_l8kVX6tSTiFlvhyRWkrejbCLqyFLo-pTuSeN5Uv7_ErfCxnexGqwVrNJ6V_J5xc3AOPKkoJglBgdLUDsIlO1BVBiPmWY-uD3yuJqrngrjLeprSLk-vv5GDdzH6smQzqEhYBVoJPS1_CTyb6fDMZusHekgh6V-CUtIL5SPVmLXjMuasmEFGNnTDkD3C1XM73mqM5epL6o69tPtBnJY58xiN5QNQUG-TTAyWDpOSugtMFe3h7O7HGddG6y2g8kU0iqKR89AehvIF5xBWAyTSnxE2szO5wXMMfV3tNpePYyePRNr7pkL21INQa_BkDQ-bKCi-aqYh4vPcMhNb8Jmdbj2J0nMyIk6eXXezTcgH34nhZNOq88XjBNmYDWxhL6Zow-ZcOROEhqkhzw9cCMstg8JhUdFzp11qD45fWvMG_3gWDIrV3gmkqxEQeiSINQUti5X9WlSVgh3AlRRaVknGc3yc3W9fvrA5-qF-PPwGuwbvtwY6FLd7vDsba38Us4jJiOQThdwcjwoIT3QiWlXiJoekevSa7s2fMt-yAU1tw667U-9_nf2YclN-pR8LoMIg-_bx36xuURTUBtCk2qN5gX_EWP5vD1pkEqs6a7yRoD0TL7K5d_F5m-YCU3umXhsFd5JjOW0TM9wep7NrbJplxbsztfpCLYI9tjhEx0jfppF0aborsDx-54N_OpIzdHmZd4_pm0Z-e8cKff-8dw7ehGoeHsWmIY_zFxNqviKTlLQ_9vlZeLWDgPqnSU57zjqsyZy0 "messagebus")


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
