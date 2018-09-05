# C4-PlantUML

![bigbankplc](http://www.plantuml.com/plantuml/png/bLLHRzis47uNeFzmSn-Q0NAC0dqQWg2kxJLfxKIBvALx4auKRHEbI86ax0R3_lkEicHPgO5kVZ34qzrttzrzHtsm3eshImcZN6npLDygoKPXy8jGJDO5hus4dNEL_MqoCNYutWgtg_FQSiEqSbovQwRBoPDWQ0hz87Z5vMJsVXnBL6wzMavAj8uRCcKpyaUXkBckA5qOXC5o-jVZEitInpYRFpu_XC7RrZ9DikJB8ftTdNoUxzExRBduj7YO-yWmYBcnMbsnsZfTSXF1xFGqca9d1hq1j-FWwuhWGDoXQW9HDZP0ndIjd1tzwa4hPDzmos5qJwKPnHry92UXjf2yK1db26vkSl8lqBpStW9QOE_WRny9z3iLU7NWUOPLHLIUUGxJgfBK7oUq6f7fC-unWgGo7dVrvypRvboAFH5hoD94d63GzXTG5Otvn2dlECNJ8-rXSbiH_2WX3yd7iI-727I94sP4vIAOgcqjqNXpRFHU5Dm2IdavqQPMpBD7ATmBE4tjRRfhOI_GXmW3L3BaHXz869T8bJeNahTDMJM7ZjRiJGHViKJgnv0EI54AnmkmTMw9JZlB_qBF_i3lI00AlXUCNsAOq-ovAeYYy1AAxo_FRQx9pVHn0ye_eURP4F2bx0KwpD5ohuNsqICdVonXS7RQK1w_Vc3uLbXdaE11g8qsPKCrWXqv5u0rYPqPNf2614eRUQrpQq7gBHsuOzUUo3-Uor7TLxn48JFR72ZPOhoYSoTzCgJKVT6KIEkp4inegpSE5j_P3XNfx1ZfKLl0jWqz906gZS6IlrwilZQlmdRIZ0odLfwL24XBwFenHwSrZe0QeYmsJJ-hCWoUk3oxBFe5NLjkVVQxD8qJxpfqF2xJJvm6ucvykvJPKtyN7A6wJUzPDVQX-hfyQ5yKY-1pylWmEUK-Hftd_B_1sNAezZFnFN4iB6oCBfjxvs1e0UbMqXwmnPj_dBKjeEe6E3-CkwFY8oSjdw_qKJZlOxOUWhmIOK8lBF2njthX4txF9LcbST-IOMG_dbSOL4mJOZXpw2z9e19T69o7mtWTZs_R5_uVnil5xocPEjWmsD7AjnvXy85Iq5VjNm00 "bigbankplc")

C4-PlantUML combines the benefits of [PlantUML](http://en.plantuml.com/) and the [C4 model](https://c4model.com/) for providing a simple way of describing and communicate software architectures - especially during up-front design sessions - with an intuitive language using open source and platform independent tools.

C4-PlantUML includes macros, stereotypes, and other goodies (like VSCode Snippets) for creating C4 diagrams with PlantUML.

* [Getting Started](#getting-started)
* [Snippets for Visual Studio Code](#snipptes-for-visual-studio-code)
* [Layout Options](#layout-options)
  * [LAYOUT_TOP_DOWN or LAYOUT_LEFT_RIGHT](#layout_top_down-or-layout_left_right)
  * [LAYOUT_WITH_LEGEND](#layout_with_legend)
  * [LAYOUT_AS_SKETCH](#layout_as_sketch)
* [Advanced Samples](#advanced-samples)
* [Background](#background)

## Getting Started

At the top of your C4 PlantUML `.puml` file, you need to include the `C4_Container.puml` file found in the `root` of this repo.

To be independent of any internet connectifity, you can also download `C4_Container.puml` and reference it locally with

```c#
!include path/to/C4_Container.puml
```

If you want to use the always up-to-date version in this repo, use the following:

```c#
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml
```

After you have inlcluded `C4_Container.puml` you can use the defined macro definitions for the C4 elements: `Person`, `System`, `Container`, `Relationship`.

```csharp
@startuml C4_Elements
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

Person(personAlias, "Label", "Optional Description")
Container(containerAlias, "Label", "Technology", "Optional Description")
System(systemAlias, "Label", "Optional Description")

Rel(personAlias, containerAlias, "Label", "Optional Technology")
@enduml
```

![C4_Elements](http://www.plantuml.com/plantuml/png/ZL31IWCn4Bq7yW_hdbQecqjFdYhRtgejLSybpGxTm6GICXDA_zwmO554yVJU36_UUyoAnMOf0PjXUTmW121XhUuyEImZb8pD99BuqPXiB_tPorHEXI6xI5ArlOl17BopUOml7XAW6POFUxGaxyzR4omBvBew3bLlFK7kKqtJIgizP8xKfHcUq5jUDEtMdW3RIdP9V2IBpHhOPJzFxRrMDv_EVR8Vjs_W9eeOpzU_d5wljLleU8P_vsjr0FnU-lSYDvClZQh72cYiJ_W0 "C4_Elements")

In addition to this, it is also possible to define a system boundary.

Take a look a look at the following sample of a C4 Container Diagram:

```csharp
@startuml Basic Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

Person(admin, "Administrator")
package "Sample System" <<boundary>> as c1 {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![Basic Sample](http://www.plantuml.com/plantuml/png/LL1DIyD04Bq7yX_6UAbG4ogUf9J687gmfJIf7iis6Tl5_M9tGYZYVtUMQejx6PZtvdtiF93mr6i5ZoB85cgXdS8qkPAcLNs7lLTm87BXeIYy6FAzf4E_wmFwrXf2GtbhTR6MhV2TNKfqg8hg_dQbXA7DuhNG8X1wNcqhvWjfqEUExT8aJLReWpKZqMbfnf2LSSf0Nf3rsKsQED5-YZr2TWe5zP6rT0RJwSxsfXF-E9k12D1Eu2jDWD_POpJWRYkSOzbtt47fdEA89At9U5LTZw6iL_dogU4JZt2NJs3nLaMiLCeE0MB306I1wpd15DqhaZ55CqZYIa1IesAl4AD-fyaftOXEC2lz4YES9cjKVqKlqJQ1htc-DCsgZhp8EiCNfMSapZ9W71_UwdytSpGTV-WF "Basic Sample")

## Snippets for Visual Studio Code

Because the PlantUML support inside of Visual Studio Code is excellend with the [PlantUML extension](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml), you can also find VS Code snippets for C4-PlantUML at [.vscode/snippets/diagram.json](.vscode/snippets/diagram.json).

It is possible to save them directly inside VS Code: [Creating your own snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_creating-your-own-snippets).

Or you can use the [Project Snippets extension](https://marketplace.visualstudio.com/items?itemName=rebornix.project-snippets).
Now it is possible to have workspace/project level code snippets.

![C4-PlantUML Snippets Video](images/vscode_c4plantuml_snippets.gif)

## Layout Options

PlantUML uses [Graphviz](https://www.graphviz.org/) for his graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

For this reason, C4-PlantUML also comes with some layout options.

### LAYOUT_TOP_DOWN or LAYOUT_LEFT_RIGHT

With the two macros `LAYOUT_TOP_DOWN` and `LAYOUT_LEFT_RIGHT` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN` is the default.

```csharp
@startuml LAYOUT_TOP_DOWN Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

/' Not needed because this is the default '/
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

![LAYOUT_TOP_DOWN Sample](http://www.plantuml.com/plantuml/png/NL5TQzj047mNw3zib8Swa4gaz2cO4E66zY6nHImtzCcifBLzvBwuMo5Cw7_l7cuIakDWuMPsTcRlDZ867es6-_hFQjDksrMp_R5wMi8QZTUKPsVAzdeSQ0mQ3im-NbTLmAdSApwCtHWfzCuoMIvxPwf7rMCOt5AH9rqjldzjD5hUFDnN1YDJaAVjGlYeB8NIo-0yoxCli7GCbcYW0JhgKMI13og2N3uG3BJ3KNEUVNAPcXiAqTaP3aRPIoZgL5NaWEn2SP5d7ljdt1CKfqImFeeHKy1ythdH3XYEDpU04VehUCapaFDcS3PHjqNlHVQ9EgYzrvAFbRE5F2tEBw5UD-NohfMMGF2jl8A7tuk4rLgxAK9QZoHm8BlnA1GZALHoqKwAPH_0of2MMJ5P_Pjd9tSpFi6Yz9-Ou3nx9FqQzDtQ9agtr5zjswmJBx7Uu7UbdyJYPQ9KTi6P3pstP0VvZNy0 "LAYOUT_TOP_DOWN Sample")

Using `LAYOUT_LEFT_RIGHT`

```csharp
@startuml LAYOUT_LEFT_RIGHT Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_LEFT_RIGHT Sample](http://www.plantuml.com/plantuml/png/PL1TIyD047mFv3-iyQL2JQZu94KCeNv0rTAcYa_bagnwU5_SRGX5_E_kKMqHxsLWPtPdvgu22K-zLZ0lNnxNzMO-kwutoxkRsnfMGZk5QN8aJQlw3dklu9t8XOkYy6B8toIzzqqVqBVM41hAMwkBfMo5x-o3H8UggCvF5qeOMj_F2oq2eUVHfcAza0PzxjWwJTBadtiSBj07QqQYqzAC8IiZoa1UaFNPIPeuqNw8DuHibnHMMpRG6KodZUrD9_psyX94W7O2dsa2_FR6em6RZN2EppvZ0wLpYdEJj2RZKNKyXdAro1zcDQzuXBDy0lTFLUHAfUmG8DOEG1QuinCiqRqY6LFKWoJk2IGrAlOACUfNckpIZMX7ywKVOQJJP8dgj-WXsZhmDkDjNIzMKHTLU_fmwGQ9immOuTLR_MVd2at7l_mD "LAYOUT_LEFT_RIGHT Sample")

### LAYOUT_WITH_LEGEND

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND`.

```csharp
@startuml LAYOUT_WITH_LEGEND Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

LAYOUT_WITH_LEGEND

Person(admin, "Administrator")
package "Sample System" <<boundary>> as c1 {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_WITH_LEGEND Sample](http://www.plantuml.com/plantuml/png/PL1TIyD047mFv3-iyQL2JQZu94KCjLYXrj2aYa_bcgpryBwusn14_E_kKJyGxsLWPtPdvgu22K-zLh0id-utpVRnjbbib_ER-UeQQg6TmZGvagPLVOUzL_12vC95KNWnv7j9B_sk3-XRQmWDvQtLnLgsmdTs9T6XAcRdfvKIXZPtoqABGEXvj9snNaY3FdVidIPfyjy-JYlqmPgHwBGqOyZAY3AG5sHzTf8cJhIlOe-G7Q92_SOEEeFfT6Txqmd_Tda98a0xWVSq0Nu_pgC1TrlX79zzn1sKpYaEJjAQZ4Upup6KTPMlvWslU8IpV09t3xF8bKhP8K3i7O0iS6adMA9xHJAcQ0P9N1H8QbJi5MBKZpGvf1lHWUPBNy98fyaQrNVHtsYRmDkCYwQfwgYBgX_wzz8D4cSPCCApj_hFpXMQZh_v4m00 "LAYOUT_WITH_LEGEND Sample")

### LAYOUT_AS_SKETCH

C4-PlantUML can be especially helpful during up-front design sessions.
One thing which is often ignored is the fact, that these software architecture sketches are just sketches.

Without any proof

* if they are technically possible
* if they can fullfil all requirements
* if they keep what they promise

More often these sketches are used by many people as facts and are manifested into their documentations.
With `LAYOUT_AS_SKETCH` you can make a difference.

```csharp
@startuml LAYOUT_AS_SKETCH Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

LAYOUT_AS_SKETCH

Person(admin, "Administrator")
package "Sample System" <<boundary>> as c1 {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_AS_SKETCH Sample](http://www.plantuml.com/plantuml/png/NL1DIyD04Bq7yX_6UAbG4nHFKaf340MhbYPLF8LjCkhYVh4x8OZutvsbsg9x6PZtvdti8f3mD6W5o_BvOTEqPTtMjrTDTGErq4vXcXn9qwcXny4hU2DouR8el1ZpLqblmtO8w3jh20tbdTN5MdR2z_PUeaDLL1UdAoKCRUwMXHQ1qFEghPWlf46VEtPEapJvRnvtA_J1cedejJHJoCeuPI0loFhi94sSwDx5AqAs2mhr1-lh36QphHrCB_p7V0uYG7S6dsa2_FQ-an6thN2EPPzm2wLpYcEJj2RZLNKyXR9UvVTN3PzuXFFy3EuUguYLIjanG6mTW2nmPIUOeWT5CgPeHabS4qXgLEmLOjIlDDcbcz0EPgKVOeJJP8tgj-WXsYRmDS-RfbdLaHTPU_YWT8t4MKQCuyLR_UTcWQRdJ_u6 "LAYOUT_AS_SKETCH Sample")

## Advanced Samples

The following advanced samples are reproductions with C4-PlantUML from official [C4 model samples](https://c4model.com/#examples) created by [Simon Brown](http://simonbrown.je/).

### techtribes.js

Source: [C4_Container Diagram Sample - techtribesjs.puml](samples/C4_Container%20Diagram%20Sample%20-%20techtribesjs.puml)

![techtribesjs](http://www.plantuml.com/plantuml/png/ZLLTJzim57slrFzmbvU1rBKCnf2cQQ9GniVAnqWwjAV8YI-fXsDdjaEfflttNITjqgveZ0UIsEVUUyxrkUwXTSouCfSG929Bc7eeP1fqEw-4IcN9iJGIfiuLziDWODYidmatBPFIeacrSgXSFzNvu5Qap71z9R10EJX-z-P6CkKcb-D1pgn3GqlnCU6PK6Zw1PNhThgTyV3xzIIAe-kRU7HzTzNjl5wi3CCu_78I7PyrcBlpw2mUdvoUN8ryPBTpWyPgjSMKLlDSbpRsb7eG39SBCA65OBj5Pfd1Z3da3RHPsS3oN2XXdM5EQDNWrrQRc6wdOEa3on02X-dK6P6WxV-m0NpycEXISMRcdpu1iv2-XLyU3_JNT6DhXadCYe8At642mwAGr4nV8Q2b2_R8UX0MHgWCBhyTzo3IEMt3GV_9xm-br3CBdg45f-5Hu0mAr8N47jHKUh0ugHxW8preuOTEw3-wj0_tHkVWfWXIfqo2Lz03BkYOwOif3kSHM4oTNcXTvsvGnZmX7hSeAyuKD6AE9SoYftSv3x-EOR-_NxCDAGtQ3NxL4tBC4r8n5TGAAlvW_-QRC9vv-AbmPsK21WkzKF4SjNiXqSx9V3aL_amV45PVdiVdORItkqB88ZFf58JY-8JskMnAsv-I0gwq5-GbGXLRYTGgqwCZsEtlhiciMdiRXeEXevTxH6vXAv4w0oBkx7RLNZT3TC-MB0jEtlJ6czHlIp_0WKTPJPB8BK43eCOQNSdkBTAkzwggj_02a84Ps7IAl9Gq07HWecBnsnEfExNbPiBL3ABwpGCMU_KzG5jrXPKThv0g1qV-MGlhTiWV6xFQ6fz6oNeTPr5q4_gG2lxtmBw4Vsve_n5JHpM05IiplZWytx2P4RwrJbSd-tKyk1WTqHZw8uIzlPtto_9DeZNZjSasS4jBhK1Mp3GJ1lrvEfrgwSiP1xi7EsyF6khnfBN82-Ivz-jB2bRphMcuQpgm2TmKiTcq_vVKvcsjTqe-NXgR9lHUcxo-VzlfQPgtveScLsjLZrrBGVUpWw9CwCgboU1O3ugW-HNuKjgbpwkiox4ghR-eQUWhUYk3lvghrZjcy_YskK7RZbURXwWu_Kh-0G00 "techtribesjs")

### Message Bus and Microservices

Source: [C4_Container Diagram Sample - message bus.puml](samples/C4_Container%20Diagram%20Sample%20-%20message%20bus.puml)

![bigbankplc](http://www.plantuml.com/plantuml/png/bLN1Rjf04BqZyGzJUcWhqT14FLLHL0AeQKg0OgAe9pHUBx3AUdUrkuRIgl_UMTiOGtr8EM1xFFlUcpSpyDbvj3vB9NHYiOvHFHl9EktMAw6Op1AUMGaRxutxrEjPt5siXTzaSUQuPLfvhlm5qsblBXZQH4y4Drps1X_VpoGg__WmxgNeFBSKMWue7uNYzi8GNRlLRhbdeGnQJ65dqJo9n6_WwiE7-eiKVpvmvt3D8_6B5s_RhN7_n_HniLnCPylXz6dIRhqf8_re6NqRBGPtLSxJryNTSZpwCfeCmybsQyQjq-ejovpNARTT65HtdJuSmfrt8TSWUoPgw1nouAjQQPkY5rf1jAVIqWvSNySwKmdQ_SqDe0Ds2R_3QQ1FLVHRDAPR0-eR8ycq0DIX-3rkqJ4hZEz2NwqpYJQ4-rBgdQjKEV2QB551azzmOS5OlHAI5t9F2G-7bjIhhM2ypXuLeGDp5o9ZXLh3hTO-11SR3aOBvK6l01cZ5W0LNWa1SVIXYJijUhQaGI6qieDmcxa0FiSu5lxXUqvaKJcZhS_XAPsE4nVVqcIv9cJBGpPfhPKrFyJgTSspU1-k0ylHSmSgw9N2yGGIz9ZpLM1WCckquusKc2N2r-ZwuRbEDNZTkvYC5k5sPlLM94IdxHgLSBb3xtSKWXmcSAsG2KctpMnLsvAuth4XQOxHvNnJYqnokBnYuIdosdBtujOS3Sm9ZjxL6HxsqVTn3HmFzlqY-xOqY67-msX8UMnQPIiciD7i_zmDF4TlmrEW7uKvE3wMQceL0jBk-N9UQ2VGmmQtdBwCuOedWV5F89rpMTlvOXaVWoIwtYqMiwZGHcdBUR6h3VlpQ99ybfgyXc33Ei2XsolMXVjeEkcTGOyRjhBG4d6LkAeE7N2UU1nfzinzE5y8-_VqwQOLA9MyBDTRGtrtQiGHvdJgIf_pXehYzsbuEwZAE5tlferyeOuJdFCrUm56WT8Wu6p8p-efsSy8JmUnF5BIYNALnhYdBZGGdc3bgPz9FltF_GK0 "bigbankplc")

### Big Bank plc

Source: [C4_Container Diagram Sample - bigbankplc.puml](samples/C4_Container%20Diagram%20Sample%20-%20bigbankplc.puml)

![bigbankplc](http://www.plantuml.com/plantuml/png/bLLHRzis47uNeFzmSn-Q0NAC0dqQWg2kxJLfxKIBvALx4auKRHEbI86ax0R3_lkEicHPgO5kVZ34qzrttzrzHtsm3eshImcZN6npLDygoKPXy8jGJDO5hus4dNEL_MqoCNYutWgtg_FQSiEqSbovQwRBoPDWQ0hz87Z5vMJsVXnBL6wzMavAj8uRCcKpyaUXkBckA5qOXC5o-jVZEitInpYRFpu_XC7RrZ9DikJB8ftTdNoUxzExRBduj7YO-yWmYBcnMbsnsZfTSXF1xFGqca9d1hq1j-FWwuhWGDoXQW9HDZP0ndIjd1tzwa4hPDzmos5qJwKPnHry92UXjf2yK1db26vkSl8lqBpStW9QOE_WRny9z3iLU7NWUOPLHLIUUGxJgfBK7oUq6f7fC-unWgGo7dVrvypRvboAFH5hoD94d63GzXTG5Otvn2dlECNJ8-rXSbiH_2WX3yd7iI-727I94sP4vIAOgcqjqNXpRFHU5Dm2IdavqQPMpBD7ATmBE4tjRRfhOI_GXmW3L3BaHXz869T8bJeNahTDMJM7ZjRiJGHViKJgnv0EI54AnmkmTMw9JZlB_qBF_i3lI00AlXUCNsAOq-ovAeYYy1AAxo_FRQx9pVHn0ye_eURP4F2bx0KwpD5ohuNsqICdVonXS7RQK1w_Vc3uLbXdaE11g8qsPKCrWXqv5u0rYPqPNf2614eRUQrpQq7gBHsuOzUUo3-Uor7TLxn48JFR72ZPOhoYSoTzCgJKVT6KIEkp4inegpSE5j_P3XNfx1ZfKLl0jWqz906gZS6IlrwilZQlmdRIZ0odLfwL24XBwFenHwSrZe0QeYmsJJ-hCWoUk3oxBFe5NLjkVVQxD8qJxpfqF2xJJvm6ucvykvJPKtyN7A6wJUzPDVQX-hfyQ5yKY-1pylWmEUK-Hftd_B_1sNAezZFnFN4iB6oCBfjxvs1e0UbMqXwmnPj_dBKjeEe6E3-CkwFY8oSjdw_qKJZlOxOUWhmIOK8lBF2njthX4txF9LcbST-IOMG_dbSOL4mJOZXpw2z9e19T69o7mtWTZs_R5_uVnil5xocPEjWmsD7AjnvXy85Iq5VjNm00 "bigbankplc")

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