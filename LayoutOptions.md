# Layout Options

PlantUML uses [Graphviz](https://www.graphviz.org/) for its graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

For this reason, C4-PlantUML also comes with some layout options.

## LAYOUT_TOP_DOWN() or LAYOUT_LEFT_RIGHT()

With the two macros `LAYOUT_TOP_DOWN()` and `LAYOUT_LEFT_RIGHT()` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN()` is the default.

```csharp
@startuml LAYOUT_TOP_DOWN Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_TOP_DOWN Sample](https://www.plantuml.com/plantuml/png/NP1DJyCm38Rl-HLc7DP9ezKG9quh0y5X7nNhc3XLQUknI6aI9IxLXFZlkDhO454aI_Rhruyz3IGzjOs6UVg-skH5ligAnzLs2MlPE8tYIfbAjpN2diY5-oJniei_5EtRiWteAsi83SMLRH9PUoNDfsvTcypkRZ8j3MqMyqHBma2SAcQibigWZnsF528Pmj8I6CGQQoYnakm9j5S1-DCUeSQTR3N1C17_0AEH41dwO4qawqQPCGpIFgf0NfBrWv5O7m9XKppOrjJI7w9gCeRXSQ_X2Bu4y3iZHHsMXNIEVRPOGkgSLfKaPSs0KxFhCQJhB5u-vTpY4MxZ2IpUPdqjrTfs0VfpCBG5leMJB6aONF4io3j5X1v8DQXvLc2sxnDTHCSY-vnaN1Ilg7-tkc1j0dToVCdpRCsgNdIkNcoUaHYZmpxil6t-japHr7pv7m00 "LAYOUT_TOP_DOWN Sample")


Using `LAYOUT_LEFT_RIGHT()`

```csharp
@startuml LAYOUT_LEFT_RIGHT Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](https://www.plantuml.com/plantuml/png/PL1DIyD05BplhrZheIdKX8edJusXjaAhfKaLJs6RFEt2Vh7xrb34_-uBhLPmBmDlvhsPsMb0uJ5gnPVvwzEsgfUp-whUFCmN5I-5TWhOXJIDYYtmFQ8BjrdcHPU-Izp7NGpW6siG3AQDrPbelHJcGqKNi-BcQgs4mUrgcIc14916TK5g8Gtur94fO_zSan5ZQ_31caIqMfen7-Gzoe1UeFM34IiF0K7NTpQQLlX3qap6V7WCEnpnJyRf_Vea7UnguHpTUO4TpvrJiX4ehHdGgBWSyxnSfu-pYbOyyEjqmbVFHS_bIjakyBvZu6Wv5NI293egbEJ5gquYWkSeDIZo2fJjwvGkmID9Tquo8ja6r4-hSwnje4t2HLMjIrBreb_sV6OEI34wwE7DM_rtPGgcfU_y1W00 "LAYOUT_LEFT_RIGHT Sample")


## LAYOUT_WITH_LEGEND() or SHOW_LEGEND(?hideStereotype)

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```csharp
@startuml LAYOUT_WITH_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](https://www.plantuml.com/plantuml/png/PL1DJy905BplhrZnG4cm3SQJ9sebO0BOs2Bnr2pjKpRPh-o-sX3ZV_Sr89YubqdUp7ipizE0mcEh5L-cRy-Rije-bOjgEPlFre-y4DefO5VIrAfjWEyHNRXF4Y-w-4FYljsr0Nnj3OB1kBOw4OsNmdogrhL9TdUJAs5mirecIY04f56LaLf80pvsvChOVzjen5WEFbWJYKPBC-Q3j4SPq0kqVZ1YnI4WwEh1jgOH_X3Lap4V7jCEH_oBSNfdewY3NIMSepjRsF7KEILhWTAQ0Osowp5FYpnUpqfQyS1lumbVlMOzbofbky3xae6ZvTJG2PBeLg4aBrvs4X4yHwb1aLUWRD-dT14UIRfpaX79Na3zjhh4sWJQ95oKPLwGgXUTsSkPEI35wA27Ts_rtvKfc8R-ymS0 "LAYOUT_WITH_LEGEND Sample")

Instead of a static legend (activated with `LAYOUT_WITH_LEGEND()`) a calculated legend can be activated with `SHOW_LEGEND(?hideStereotype)`.

The calculated legend has following differences:
* only relevant elements are listed
* custom tags/styles are supported
* stereotypes can remain visible (with `SHOW_LEGEND(false)`)
* **`SHOW_LEGEND()` has to be last call in the diagram**

```csharp
@startuml SHOW_LEGEND Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![SHOW_LEGEND Sample](https://www.plantuml.com/plantuml/png/JL5Dgzf05DtFhxYr2oDeWgMhhfgceWkreObr6IR9RHsOZs7cXY3b_VTtWpurcqlEn-4Svdia6MWm6ghThtEptsmtnvzGIUCrYa_ATdhe4Iv4FdxBiY37z9-Yoz0E4KFdBA6bj7CcyrhQAMOLgTUgpOglgtA2JeTzPcGa30mr1JkaiXXIpreXIWpHsKJsHjabpFBfgaX1aWkpXQYkR3JD3pVONePhqgsNCBzrco_Wlm3-7f79Y6qZlUUSCxQGUwzL9qavEsEe-Bo4l2hJuwPcIq3uagxXyAUOk5nhDqQO9aKW1xp7IvQOGPFo6g4U5H4686LGAukHkxtTsoLq8pddBcDI_4RziUfPwnJPoNTNrsN5gadqO9ynMwJ8lpYTly6PLujuUQLa8Tu1 "SHOW_LEGEND Sample")

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
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](https://www.plantuml.com/plantuml/png/NL1DIyD05BplhrZheIdKX8edJusXMB3LO5B5KzWcJxkmN-o-DHJnl_j2QolkPU3Dl3SpEmyeF4Qj-2f_UzhKJLurrSEYBfQy4jefO1VIj2fsm7U8BjnccHTz-Y5n5xSnW6-jGJ2OjbPdelDIc4yLNSoAcwjI2OERzIfJ0Y4WZPg2r48QyAaZJyR-coOJnahmmPf4T5gQAH_b0yg0Ng3remchzW51DtSscaxuVTBEfdnyo3gUy2_6wPriaXwsZN2Exhp2bkVEATaAbDQCQ5HSJdbUbUdZegOL3_mwdV7rIp5mkLAs3toe63XQJlsS88cE2YLvyRgNYE0vIWsAl09b-pwcI_10qfsZZ4Zs3EgtrJdM9j0cuRAkoufKW-Z4di_S0rAC7WPuzrR_NPc3wUWtVm00 "LAYOUT_AS_SKETCH Sample")


## HIDE_STEREOTYPE()

To enable a layout without `<<stereotypes>>` and legend.
This can be enabled with `HIDE_STEREOTYPE()`.

```csharp
@startuml HIDE_STEREOTYPE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![HIDE_STEREOTYPE Sample](https://www.plantuml.com/plantuml/png/NL1DIyD05BplhrZheIdKX8edJuqrMC5gQ5B5KzWcJxkmN-o-DHJnl_j2gnNtCl1ctfkPdGSK7gDMV7b_MpHLNQoBf_grB7Wbj5F0pgHfLUo0xn1TkCuoB_hqNU8kRcC0trg3O31jhSv4vwKm7ogwc2skBaeb36vM3vaI205fr2n8BQG1dpgoPEoVPp9Xh0GVh4b4fwMPyb4-e0pe1Le_ch1g7n1qSsEZwOJV9-rioiU7gEC9_sIStgzBqiEs4SxHdHVOyjmv9Lk1qfeHZHRdKvvNPVfOrBJYWL-cCxvwNWnShfJj0nyQ1ewMKpqdIAAZGabUlEub8dYEKeCYhq3Plexf4ZoGTESe8vAjGVsqEiNQ1DeaNDPrMP5g4FsofpDtW1IZXm7UlDL_L-PWElhCRm00 "HIDE_STEREOTYPE Sample")


## HIDE_PERSON_SPRITE() or SHOW_PERSON_SPRITE(?sprite)

With the macros `HIDE_PERSON_SPRITE()` and `SHOW_PERSON_SPRITE()` it is possible to change the person related default sprite. `SHOW_PERSON_SPRITE()` is the default.

- **HIDE_PERSON_SPRITE()**: deactivates the default sprite
- **SHOW_PERSON_SPRITE()**: activates the default sprite "person"
- **SHOW_PERSON_SPRITE($sprite)**: activates a specific sprite as default sprite

"person" and "person2" are predefined sprites which can be used as default sprite too.

```csharp
@startuml predefined sprites Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(userA, "User A", "with predefined sprite person", "person")
Person(userB, "User B", "with predefined sprite person2", "person2")
@enduml
```

![Predefined sprites Sample](https://www.plantuml.com/plantuml/png/XOxDIiKm48NtUOfuLrxmDY2kNFLdgr2GhYLjHXj89c5cGb_VH2m8BbpDOVZupkbPB4c9GMS21nyUmMdEv0LOlzcO0wWxZrie3lGkaldP6B97z-bbBsjXe2sX04gtfMXoiDXiDnON_6gcfzlSNilhYucM1QY-tgU4OciJTRcoIir0dF2-oOO7VLdgrSEbfgEM_1scypVVW9zq_QqOJyNuh-An4MUygXxGrK5V "Predefined sprites Sample")


**Using HIDE_PERSON_SPRITE()**

```csharp
@startuml HIDE_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![HIDE_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL1TgzD047tVNp7MXvj2Ry8LdtowCGPRi3KqgJw6JJBQXVrOTYU48lvtPsbj1VCoPCwPyx6laMIWsMZOxZxLVLCVsw-7lcsEkww6LXglKRnHTjJpX70cyl53KGIvv3yLdUTXZXX6PmajvQCpXTVI9hNdI9DMGr6zVsxIwhJ_KXWP2GEl-eelfB8OSizS8VwtpjP2D1YYivcSZB8RM9LfgaX1aWkhjMWlaT3q7zri9naksVYoWQThugSr_1B0tzqeMt3efVUiynq7ABtNQfIad5tngdgxWR9jyaFTyKb0U9U_mFvRbR1IQxT4I4KZa0DkwILJpAn9iHTqYoB20AGCQlQAdEttBLr6Lv1rRZG6nH7rtrQFMAU8CVbjkwvfcPL8T_GXynafyY-cyICuy-_9AzeflUSV "HIDE_PERSON_SPRITE Sample")

**Using SHOW_PERSON_SPRITE()**

```csharp
@startuml SHOW_PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

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

![SHOW_PERSON_SPRITE Sample](https://www.plantuml.com/plantuml/png/PL5DQzmm4BthLqpTWxsmiKdfgQUuPcaApSQidUPeP6lI5UX3I6DCAFtl7JLfjb1V1i-yz-QzqKqY6Mcr1eRR-yUfFvo6--CqzAUlum46QOD1yKwxnQmAuKmKqgUcYNAhVsWwh_EQC2xU4Jgg5s-ROAJBQbU9bD5pqtsywdFhuUvROsKYZDoQEcP8xJ3MWR52D2KSFO53LAXWnaMoBj1P9z29AuB29xaQWestGWfH4q8HC2Rl2YWRyR_vQYT4_mTGIMMrsqFHvgeJHKa-5ZinFBCXEttsgrCoFbVBzHxAbypb3duAuE_DQhNXFCaGMESHPsX3C7gHfDa0jxhtUsY7lZuUHgP4X0_rDTnzx_AiDSPl2VAf4f07lbEG3B4SIFCk63aLOGJI5WtlIkpjrwkxYbw6hFCAuw4ueVcRwcBh8J6Jw-quzWEZCkXjUf7vWfJu5tDvYjx-Ixb1f_AB_0O0 "SHOW_PERSON_SPRITE Sample")

**Using SHOW_PERSON_SPRITE(sprite)**

```csharp
@startuml SHOW_PERSON_SPRITE(sprite) Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml
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

![SHOW_PERSON_SPRITE(sprite) Sample](https://www.plantuml.com/plantuml/png/ZL1DQzj04BthLspTGnIm9H9wwYckC4sXIOGbDqUnbYRnmduiCxCOK_hVEzieTkcfkYmpx-EzqHsnHaxE5X-C7ssQG1sO8tskQzJ7wjNm8UqJ0Ox1CtYknk3gQBNFcXNnPCs-RZwjshpQFNoldIO6bDNGY48R3rZ5F_uJlCYa0kbMvl-8QL3J0IPd_5I_-wz214ym9ZHyqZWU3CF82U5sPKHBS_xbcZckRe9pmSzL_WLtabnhQz_Wehj_UXxQpRPxUXowTlkjtvGBeGwvuF2A07uuHo-kYw85fE1BdQikrMATNqECcWCAtfs8mGrVGlAJnbCvtYpLLQTTj71rhNuMIhxppogFi1zqZEBp37krZj6QKRC9VY6hvkDIhRksUjpq8a5GjzMDUlZHP6njRJYIoYL9SL1ZS54BnINBHh9KVpJCW8gD0ojP9Dr-pUrAVWF5PwRbmxPWtw-wrDeHKCwxx_ks4rOcdT6BpLTWaX7oyuB1_Isv0pybPty3 "SHOW_PERSON_SPRITE(sprite)")

