# Layout Options

PlantUML uses [Graphviz](https://www.graphviz.org/) for its graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

For this reason, C4-PlantUML also comes with some layout options.

## LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT()

With the two macros `LAYOUT_TOP_DOWN()` and `LAYOUT_LEFT_RIGHT()` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN()` is the default.

```csharp
@startuml LAYOUT_TOP_DOWN Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

/' Not needed because this is the default '/
LAYOUT_TOP_DOWN()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/NP1F3vD04CNl-od6Ue0c5LBZoPE8HW_zGuJQU28BJ6NZ_jdi3i76-DqTqjeQkRomxysRt-wxI3BGP3JiYc_7KzCsnwhzS3mVe9R6QnGlbEtrD22CH3w-pVCWv-oxed7gfeYXTvRGKjOxa_zGeHyZZNdvvbMbfQNJVfVZJ_O77FYmBJaibSMGUTueH9x0mH5OH0v0XxtaIg1HHL2H5M70YvmqGPAB__ZIjH0LXkXiAWUZx0PMnQ8gKf3amcejwciaDErxDzb1XclQRpUGtAwLhE6N0FuUIEcCNIkzvvupTb1uhrKlIJcxugFovGQAkieE7niU2GYliotilvQBLsZjvWYC7XZQ0J-5bnmn3Avu5pIp8i80f0ngtXMPxVUTBgMRoJtt69lY2-g_jtfYdI9Fidvkcghcr19wkC-QJqYHVt6HIt3cdv4_ "LAYOUT_TOP_DOWN Sample")


Using `LAYOUT_LEFT_RIGHT()`

```csharp
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

LAYOUT_LEFT_RIGHT()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/PL1DhzCm4BpxLopbq5GgYOeuSMg8IelKGjIa84wHcop4mX-MlL6e4F_zRTI-zadFbvLtPdTcTXr91XgCXdt-yzkfRlQRptLp_BBTrL19upMADygsUkWGUY8VFsPPa6FwMr4_d8U8eNMMq5BQEfFzKQ7j8_LPyU5TgQMbqs6VuL_6E-ousHHCbifYI3rh2l5AD5a8KMA8pYQoCyekOPPFLKKAaboOBKHrYOIc-UG6sybmIThL4kPNh_C5_1F0xwwJZ7XkfFUyvmUU8VTUgrQISdR6hUBj4lAgJBzkQXu92E_J5Ho-5nEMQ-t625F42EI0ytd953DeKgm5zQY8C00fWvgr8dlxVtENq1NaFJSQW-A8-ZdLmzOfyYJNNLsN5RCcqXrzhDaYHVxYL7u5PrwEhFc-VCud "LAYOUT_LEFT_RIGHT Sample")


## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```csharp
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

LAYOUT_WITH_LEGEND()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/PL1Fxz904BtlfnZnG4cm3SQJ9sebO0BOs2Bnr2pjQ3VkdytkD9KOlxlJW63osyjavxsPzzwi8yb0Wz6mpxzzFjND-LEzQ_QRxURu4Iffl4RnIjbM3nr2J-JZ-omBSan_AEg7on0njCuIMafRPxAVAhHzf3uhthqfjRHqEkmp_CLuXnqtcuB9KbaCgMTH8Lwg9WiXIWpHsKHsHjabpFAfgaX1aWkpXQYkaT0q7znWEnckIRjQmlncThw0tmBuFOII4I-Dz9xtdF42kVTQjPAKipDk5Q-Na5TbUjpKF18GtgOhE7mj9YpNseqHfemHo047z98fPj2aM0lgKH5X0586DMj5zlRdxYwX6yXxxZG6nHVK_r8zRPqYJtBTrNLPCMiYFT3dcYrIv2zEvNjmvl-HDH-Ox_aN "LAYOUT_WITH_LEGEND Sample")

Instead of a static legend (activated with `LAYOUT_WITH_LEGEND()`) a calculated legend can be activated with `SHOW_LEGEND(?hideStereotype)`.

The calculated legend has following differences:
* only relevant elements are listed
* custom tags/styles are supported
* stereotypes can remain visible (with `SHOW_LEGEND(false)`)
* **`SHOW_LEGEND()` has to be last call in the diagram**

```csharp
@startuml SHOW_LEGEND Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")

SHOW_LEGEND()
@enduml
```

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JKzDR-8m4BtdLyoo1uB49cArfpsHfWWEGACcb6DaacbZrH-MFL6AglxtJbGAzUN9ypxqtZAGyDHh5VsIfb5zYz0HkV0_JRqOaXT9NN_g0_h66a93IMDr-YfzqmNgqlpVdq89GuVTDiKtvbji-LZdB1RIe4_S61qLw8CriMYrD7EOP2FAG5wGzPDPL9u3eQxlR6zQuSznivZ3j1JQAPpEu3q2VjV8UC1JBPpZd2EU87DEoKQGj6R2f_pt7BAoIFQhYYqUuM-oWDrJFdAPKdO8CAu9G1PuYXCiqRqYwHH2DKWYz41Iev860tVxkBIBwOlad8kCoUWHrVUgMwr3O2VZfggAabMZwChUOjP8WRyumhEt-gSbAZSFntgxMg_sz_4iMg9fUwq-0G00 "SHOW_LEGEND Sample")

## LAYOUT_AS_SKETCH()

C4-PlantUML can be especially helpful during up-front design sessions.
One thing which is often ignored is the fact, that these software architecture sketches are just sketches.

Without any proof

* if they are technically possible
* if they can fulfill all requirements
* if they keep what they promise

More often these sketches are used by many people as facts and are manifested into their documentations.
With `LAYOUT_AS_SKETCH()` you can make a difference.

```csharp
@startuml LAYOUT_AS_SKETCH Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

LAYOUT_AS_SKETCH()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1DQzj04BtlhvYw1ylWIhZqr9DLOMgetOfARib9hAL9j6G_bjqHYWdvxnbXnmxPox3ptinxRzQHPA31QDZbTtyETPDNJVLhKnTRgAJn6iKdPLizT0WzaO_Viop8CNrGr0_78M9edIMqbBREP8ygj7saFYk-VIcrj7JOxp9yOhp3ZfjDmMIfB8RKiwGG7pMJXH0bXkXi8ZkZx19c-LHLf239XTb2LAT8Q9eVRh2T3AUaNIrXVhOwNy2p07vNcMJ4OoEzvpt_yGYvzrgrafIpCsuLdvUGLsNwUrFpI43ucgvW_w-Oi5nhDqQO4aOW1npFIwQOGPDYBQX7HOG1I1dKh1NPsyl5NK9daFTSQ0oAlwZVKjri7I9FSjtMTLanQo9TqTkQdqYHlpYL--3C-v4rdvUl-Ge0 "LAYOUT_AS_SKETCH Sample")


## HIDE_STEREOTYPE()

To enable a layout without `<<stereotypes>>` and legend.
This can be enabled with `HIDE_STEREOTYPE()`.

```csharp
@startuml HIDE_STEREOTYPE Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

HIDE_STEREOTYPE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/NL1DJ-j03Bplh_3hEpIL-XBrYHEdXX1H90fHau8uHTl4a1NxiTfr52h4VsUZbXPnikmPpuozzCGTzKh2wlOwhyigt-GFrNEHGycLbSZ-2Dt8laNeYAo_J1B7X_XLKDVlUe-kCPfGKzmObRm9rtIUkYIx-5T8hccxlalmFU0jjc5OPu7CXKONs-38s2_BQCPOWSuR7V5M2Js7IJfMuSbnCcuoO-NU4whwolIwvMuVDOivJ0z9fpFuO0009vTem5tDhGqwJxY3r5ef6ax2w4aOPN_da9P5V9zNOSKX_8yNi7xCHYoLqWmUnWCza876ACi3HVMIX9K8rI28q049XL9ez27Rvp5TH0Smw1nf0MGRbDzNdMDjFVhHRrLLHHbO8-c4dcLka7neSImlpgYVAylmtV6PNm00 "HIDE_STEREOTYPE Sample")


## HIDE_PERSON_SPRITE(), SHOW_PERSON_SPRITE(?sprite), SHOW_PERSON_PORTRAIT()

With the macros `HIDE_PERSON_SPRITE()`, `SHOW_PERSON_SPRITE()` and `SHOW_PERSON_PORTRAIT()` it is possible to change the person related default sprite or person layout itself. `SHOW_PERSON_SPRITE()` is the default.

- **HIDE_PERSON_SPRITE()**: deactivates the default sprite
- **SHOW_PERSON_SPRITE()**: activates the default sprite "person"
- **SHOW_PERSON_SPRITE($sprite)**: activates a specific sprite as default sprite
- **SHOW_PERSON_PORTRAIT()**: activates portrait outline instead of a rectangle

"person" and "person2" are predefined sprites which can be used as default sprite too.

```csharp
@startuml predefined sprites Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XSvFYy8m40NmUpz5jgTTs6sWx6bF_NDTeI0zIqn64qpJC9bGFxvJKHGyUCeG7h_tcaGAAKzUH0G31nV0Y1JH4IInLLFqK7oue7qs82nHJ7zIebggeoERzpa1wZaG1AhqFCcJGsqJMTd__WnU1Het_nBE1C60uSzTps759LX5BYsA0J3DuNDrsczHZloAjkHhOVzrauZN_1guNL_FH7SdkhT4_J1gHXfUo8Ck "Predefined sprites Sample")


**Using HIDE_PERSON_SPRITE()**

```csharp
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

HIDE_PERSON_SPRITE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL1Fxz904BtlfnZnG4cm3SQJ9sfjX4ImeKMFpTAETkF-sUnEKudnkpiD22Q_NYQTz-RzsMqa6MWq6dRxZsLRbQVwox6jgzE-AQ6MnciKhvJjzDWZ34G-li-o8AVqXw9Xl8mHG-SieQMqSoRxgK8tH1goujsRIajBvyFd37yntcFFoxPWibGMG-hPL8YNhibAY0f3T3QHlL5s3OjydYfIaEJ2OYNgQoGqxGStsbw6Qz9jrh2yXLskuBS0_Xv6oOINLdhFEj_m0hdtMdMIbBCBNXMlrv3NLNei6pu926_J3Ho-5ZEMQ-sc27F72EI02th953DgKkm5pQI8C00fWvgz8cVxSq-Nq0radJkDGN52_Q_LCzOvyYNFNTDKDRDcqWDzodn2YloBy_WUdFd_P8ksv_Vy2m00 "HIDE_PERSON_SPRITE Sample")

**Using SHOW_PERSON_SPRITE()**

```csharp
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

/' Not needed because this is the default with sprite "person" '/
SHOW_PERSON_SPRITE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5DZvH04BtthoZn09ECa3MUF2sIYMlYpfA1TO-aQMgbOtzqkelWnlZVBPpHCP5BXNgltaVwDf6Cj5W3tTt3qz0UJjt3SUZQqwV-09sqmQ1ufPqoouGm4uNqlggYNCklckPbN196vHsXer9vMttJKSs9vgfvzwOrqj7Z_USAlpC-uSJBeM6or0vZ6TXKY2g7eoTmY4o04PLaIQ1P9z299yA4pt8n12iRGWfH4q8MC2RlCiWhyN_kOYT4-vjGoCbgjuUitgPE52NvcEr4zv88xV31BswIyQLGDtl8ptNp7VmGmD_VgCMAuo13O9qd7A4EmMWbINC0NZMlzr1tRNayz7mI4TwMDt3_fTcmsXY_9k1ACG5vKDu6oHJBXJHxGS-j22EGjcZOAt6sdvTq1Pr1rhdG61GdD7zQNMCz9hxaUTVtRSSi9br3NsK-8YN-nMqyHs__FRb5DsqlyWi0 "SHOW_PERSON_SPRITE Sample")

**Using SHOW_PERSON_SPRITE(sprite)**

```csharp
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml
!define osaPuml https://raw.githubusercontent.com/Crashedmind/PlantUML-opensecurityarchitecture2-icons/master
!include osaPuml/Common.puml
!include osaPuml/User/all.puml

SHOW_PERSON_SPRITE("osa_user_green_architect")

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZP1FQzj04CNl-XGRzn0PR8c4ddgAAqnJQ19XoSrHh5UJQEd-MNPcSKtfT-yiTknIUeWkOlQzcVURkKEIaP8rehj_UXxQzQPxUXowTlErNvSOeYQOYqxQOA2uqawPD8AOY09-gkiezzMhfYdj4a9KtX4ugfItzGyTrOGqrSt7PMkae-t3jnf-iZx2o8z3msQf7SGgS7XnDS8BLyAZRBb-Hq8J9KumMkt6-YrXwGCu19KO-o2PG1CeIX5kbvfxiROI2U9baLDStNXhlJkX_2jkERcMnXpbuZztch5ro833QmHmmpbwDY-A5Y9wLygCkX2pLVvhf2Z9HzQx0nBOuRDFRfJnKAgRXRW-7lnwBduLWh_piSezx0OP0izvXfrOXM2qagIzc_5Jys4XLbrRFQvxReaWRgiRyV2zoThA6Bz7aI5Ha1VAso3POfCXpLcYtsiYY8Aq1SDPo6o_JtGb7KMUSxBbnJPWthQwO6qHCEVTzttRiIkRpkfbp1SWv1BoxoLw-tVB7RWnMVC7 "SHOW_PERSON_SPRITE(sprite)")

**Using SHOW_PERSON_PORTRAIT()**

```csharp
@startuml SHOW_PERSON_PORTRAIT() Sample
!include https://raw.githubusercontent.com/kirchsth/C4-PlantUML/extended/C4_Container.puml

SHOW_PERSON_PORTRAIT()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

' if a person is combined with a sprite then the rectangle layout is used again
Person(person, "Person with sprite", $sprite="person2")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![SHOW_PERSON_PORTRAIT() Sample](https://www.plantuml.com/plantuml/png/RL3DQjmm4BxxAQRRmdfXQvFGKw4GTmbDeScQjTCSZTQUh4Nr8wGHxbBwxXrLJT93VB2acM--dxaA93n5hQ2xsJyCxVMXszyDxVxG7vglVRc1JcYdi7WZpQZYX30JkV2nhhrOgfEaEHvZG3zQGsYe6gskVqW_pe7cUlVXVQk4eVlRRpN-93GJJbmSTjQGa0PzvLYuA5vNBeeMVR2c59EMPWkh9fqoa1Ta_MfJTET0g8VFDff9-7CvNcnXdUskD_2h0FwUfSe5ZuDmZdaUy0YDSqgEWgGrAoxjtcwXwThgxhhd4OzmMLt0xVTTwZLAsIL0IXc0B8nMEy4G7HL9fn3wHHAX1v8Q5Mi5zlRxdxkISfDvCYmPBzOW7q60-viFP4YSHvwSW34pTuBpaX1eHfD-u74aOKuifiJPHaepCJ1Ud3ZTqw8o7qlbToRBL1paNRvzMcNOPJ9oGFMqtfVzt0SCAVXDtxSTenBekVkIvmjIu2Ucuz5R_V_85PefQlK7 "SHOW_PERSON_PORTRAIT()")
