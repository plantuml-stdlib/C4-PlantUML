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


## LAYOUT_WITH_LEGEND()

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


## PERSON_SPRITE_NONE(), PERSON_SPRITE_ACTIVE(), PERSON_SPRITE_C4(), PERSON_SPRITE_3D() or PERSON_SPRITE($person) 

With the macros `PERSON_SPRITE_NONE()`, `PERSON_SPRITE_ACTIVE()`, `PERSON_SPRITE_C4()`, `PERSON_SPRITE_3D()` and `PERSON_SPRITE($person)` it is possible to easily change the person related default sprite. `PERSON_SPRITE_ACTIVE()` is the default.

- **PERSON_SPRITE_NONE()**: deactivates the default sprite
- **PERSON_SPRITE_ACTIVE()**: (re-)activates the default sprite
- **PERSON_SPRITE_C4()**, **PERSON_SPRITE_3D()**: activates one of the other prepared sprites
- **PERSON_SPRITE($person)**: activates a customer specific sprite as default sprite

**Using PERSON_SPRITE_ACTIVE()**

```csharp
@startuml PERSON_SPRITE_ACTIVE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

/' Not needed because this is the default '/
PERSON_SPRITE_ACTIVE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![PERSON_SPRITE_ACTIVE Sample](http://www.plantuml.com/plantuml/png/RL1DYzim4BthLqpJWnt8scpfgQTrZMaNkgc9lTkZaQr98z27aCQOKFhVEoPfqaDzUNZUnppDKo8PQRO6skRGVTyFNNjuxfkXglldjmOwQOD1yKwxoSmAuKGKqgUoZ78fVcewpUESC4xU4Jeg9c_BOAHRynuIAQF7ilxuqAwZrvTlfPM9CF9egDaXjSDO1DOAKMQmzmGEKQ624IV9kK0ddK0dHWI5HpaRWgmK_skQRuLeCIRlSgciTZlOL2lgH56IZvkjwCwytGwV_UoKZETyUjn1TdbWjeLV0lYxzSeN70SP0kVym16g48oU96dlDZogt--WwjfYt_HiYGWVYaTuUQjNhZB6BmdMkt1p3toK85bYkRtcNT0lcWWZaBPeU5VYRh-lxNAwa9npbJ4f3cZ-lkfUwpMna_5htxSTgrRHZRt7V45A_8ih7AEt_rgUq2a-_ny0 "PERSON_SPRITE_ACTIVE Sample")


**Using PERSON_SPRITE_NONE()**

```csharp
@startuml PERSON_SPRITE_NONE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

PERSON_SPRITE_NONE()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![PERSON_SPRITE_NONE Sample](http://www.plantuml.com/plantuml/png/PL1DYwD04BtxAsgpXnX8b2nxsbDSaTs5ZP5eTe_IQisaeJ-QxX89m_ptAKac6HWlXLNluxtU1HAUHgsWAexreMphwlYdAThoK1PG2-qKHb-awTKu89o9NFYHfbvCoREayzYD0Nrl3Q6XfBSwTKgOMMqJQ52oI_FlcsfUdVP_Koq2eUTLcpD3I8C-SOoDei_MyOgtw8CriHYqD6jOPFEKWRmWwnUhgBwmd6v_sj4Cmb_YVhk6vJNnSWKl4V1tDuedx5hX7ElynmuovvJi1Kbh5hpAlwuXgwkaB1gcU8HloHRs__BvbYbbfm1pqG1aWLiwmH0zAfBi1SqaYNi1IOsAlG9dUxsbY-bwP9qRZ8_H4TLxgqUiKs0cpzzDKzMCca7twqFc5rBWNvp7axVw8sM7Pk3tV0C0 "PERSON_SPRITE_NONE Sample")

**Using PERSON_SPRITE_C4()**

```csharp
@startuml PERSON_SPRITE_C4 Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

PERSON_SPRITE_C4()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![PERSON_SPRITE_C4 Sample](http://www.plantuml.com/plantuml/png/NL1DIyD04BtdLupnq0JQX4fFdXf3KS7MqAHw39jajGlxiUnE24NyxyvIjM8kGsRUntkxziWSZaf2jTdNpxkshlQFpQOjLr0pPIMFheJkvJXmE29QVvldZatPky3Zs8sUkzvev1gptgZSIgQ3riBZ84MNbwj55LQ7xLEkc4VkQDMMn612SvTPmaRHV-CafHrttkY43KheESH5cCAZOsXSd4RrYSHKUsT6FJ1tIlhb76RdlBCKFYAWxzSccNZNCcj9vvLtK5WhHSzG61tJghoUGr5NsMxJ4CLnkCcMi7qfmwsGqamUGaqFQ80wMaOGDKeKv0ND991Q0Gh59NbvolRvdIx1yv5qph0GFDfp-TFg4klWYKdpeMcgEau3w1Bw8dFFqTCl3-FD6VMNikPw2A_v1G00 "PERSON_SPRITE_C4 Sample")

**Using PERSON_SPRITE_3D()**

```csharp
@startuml PERSON_SPRITE_3D Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

PERSON_SPRITE_3D()

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![PERSON_SPRITE_3D Sample](http://www.plantuml.com/plantuml/png/NL1DRzf04BtxLqpf0IE1BTgUUi9rKLkfK0kRvcYjxKbOQJzMksDPACf_pwmW4CMNaUTzl3Ux2IGyZLf1jJtK__PjNHt-DDlswq-eXNOAaq_Iz6eS44v4BdpFSo-cx4dIQUp6WBwtXj1GrbkTEoLCz5e56fJiylBRgeghu-vlhaKWzBngIrO8QT1dZhb9yZ4uNV0EVR0c5OEMPWcp8auPo0koVhP8wZERwVQ77SqW_3djrqkON_hE5_2S07-tc7J2hXNEiSy3Tb0ufsGlI5epurNvUGb5NMNxRSCIZ_0bMyFkVncnGYax1OXd1Y0BVACJJD6Z8ibPq4oI23sGrAWuAt2tbskxb2uW-rnf32O7L6zNtMiT0ojv_cwQgcPM9DtGkyqlfC2_6CUZj_gzP8DcYA_v2W00 "PERSON_SPRITE_3D Sample")

**Using PERSON_SPRITE($person)**

```csharp
@startuml PERSON_SPRITE Sample
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

!define osaPuml https://raw.githubusercontent.com/Crashedmind/PlantUML-opensecurityarchitecture2-icons/master
!include osaPuml/Common.puml
!include osaPuml/User/all.puml

PERSON_SPRITE("osa_user_green_operations")

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![PERSON_SPRITE Sample](http://www.plantuml.com/plantuml/png/ZP1FRzD04CNl-HJJSAWh9RPQSU94i290eiMANJXQ6tlQhBH_LZDZHH7YkpDBt0R41L-idNapxpVlFOiXcRo3PhjhlpxqRRFxt6sXDJuvN5pPCBXfH3Y897vNLMIEvRELmxIV66c8GJ18EKHV9MT2NhHc6PtTL_NRTPDBZ_TVAczOaBJKrpfXR40gaseNYwiHd_G9aKsZXV_mgSdm0KTlmrYz6AnZmi0uJ6JbP6WuMC519iAxjTLPdW4kvynsLHszZ-7Cya_paPNPE3UZ_XLGiLHLdzdwPq8ClHAG4QjconlL8d4CXScOArXkyj-og2AIzjkJulZ-Gvp2QEXK3BShk3v7Vdq3FnQWtsjInH7tlKb9ztp7FMnISdRuRRNKKlrc1PksAH-sdOuGmbrv2_VVwjpRE1UF39cIGI9eVCcen4zEh7f1TxGYI23MerElpFvpfYlatDGziomVjaFtSjK5IuFYxFUfwvfMLLdqshsi-OZ2-iJyUwBe_npv1G00 "PERSON_SPRITE Sample")

