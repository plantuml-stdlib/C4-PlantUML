# Layout Options

PlantUML uses [Graphviz](https://www.graphviz.org/) for his graph visualization. Thus the rendering itself is done automatically for you - that it one of the biggest advantages of using PlantUML.

...and also sometimes one of the biggest disadvantages, if the rendering is not what the user intended.

For this reason, C4-PlantUML also comes with some layout options.

## LAYOUT_TOP_DOWN or LAYOUT_LEFT_RIGHT

With the two macros `LAYOUT_TOP_DOWN` and `LAYOUT_LEFT_RIGHT` it is possible to easily change the flow visualization of the diagram. `LAYOUT_TOP_DOWN` is the default.

```csharp
@startuml LAYOUT_TOP_DOWN Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

/' Not needed because this is the default '/
LAYOUT_TOP_DOWN

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_TOP_DOWN Sample](http://www.plantuml.com/plantuml/png/xLXhRziw4ltkNy7hV6W3E8sJFfhDEaRzK1vOnmaiPRDtsy9Wf74iN9aKIBgkTzl_laD9PcGpMa7sRJvT1aWKSURCcI5r-FWa5HLgFejghqYFHrn8VDWhRRNQRm5CGWR46JZNpj0Rdz_WhzxDu6P4ziwJLaCaLosZa3rMnFIStkKmHNIl_ksGe-DQJVuHifWAEYDeHEUHyk2xwaJX8vi1KyJ7No3oPWj1u_imK5Dot6pcti_ezskGaZw26_u7oD7xPjvBWAyeUuo0_BT6iBc82bmjOpZdJAKUnqcFdDA0Bp0vCg6HXDhFF4n72Bx889AoahqFIKlUQ2ZxRJx0psSvjLeFVCu2AfRjzehV1ei2paqhmWQFTqbBtdQv240KlTSZ2YIWSWg1flcA3EYIprMr8OuuCXvqVh-vyyOTT-p-m_5wbxcK7wZ_nwFGoMOy7CVfzdivYobbmKA4IW4ZIip1dY0wko6T0Qdt-2pqYKkP9DTklPRE5JBXNFzfJT2E-3hCcO2WVKy5mtgUjWvrHvlq15050PeB4eJIdqiPSjOW322GH77o0EGRZS90MzL-0nOyfMZoNUNgtToE-pVtG_IB4r-k59yXhXvZXDsq7pZdtdXqTN7faGWcIhk8y76gSXvO-6uwAqAe-l5cZilNCCOCg6mG64Vq0QBzt8TGFplBtjR9sWoaacH-vO3wGS_8vu79vxJtQt44p6m44TKfosaOLqmKNSShJaUD5UZn6ZrJqhDwVP-iZFCTne-SQlAcB9N2AF2dRATuNzZXOKlYTtow8PJjpndyrzQXxcyV7jRNQe3S9eBF6cZ6SsETqRQx6gH-SD2kxvTYcCHiCDl6eAxLhOkV_EkLW_Qs2Tfzcc7hu40pB8UoUPOO6V0rz27W5_Z0nJR5nAoBi7OlwlCrDJ6sB2vYba7kNkHDulrjYgk5rQfmV_VI5cFp1IiWMXow7C9cM9h6HldkjYdVtQsLuDtknIj2Zeie5jCl1R2vtLKgss2Rikabsafli7lXYh5XeWg85eSkW2XXEAXKlj4svTER6pl7qUxr-p_WA5w55IpEenp39bcUoTCEcbn254Fb0nWw6tL8OFb-fhNauFCq309WN_i7ISUQprs9pzqpFgCIdz4pFeCIdq7canmNVHx3AUaG6IOxHCadQa45FYobWjaRDBaLuOoA9O48zC5FdX9lQXcIa16fiRI7EuzZBXGYvfnkWSSOWB9WqrTcU-jeINpE63v1G1GdgYJC5LF00hIbyo04vcCUpZSGomSUB1jwepyboOY7FesIk8opWwStSKAeWP0o359YVAwIPpvP3nx0DuXuh3D1I8fbsVRmVkkCt9lXk7knEhatJzuTV-oQVkTVdZCQTWPZo_33YVunXkxlhkTSv_gFZZwSTFisa6NujwHLlIieE1xhpuUpTji-l9kJhdrVaPYM6dGtJgGR5R5FpisFRxiVpWjFyl0ToJ4QZL-Ginc5Kl8d7VrJI3wT_Y_2sKoO8gflUn_FUytoEhyWPtksbzTvztkK-ollSZnmBfnXlpRLkY5DYhK87e45wTr1xSSPMMluluT6v4VjHsjZPhGp2vBEqiJ4P5TakofvtccZ4crjcAdeEgWnB08rJfXGafPzwVAAE9dGLzN3X725sv0qmxMRYZ8m_H20zCNpg5_O5xQoA8YmoNViV5SLEEUKnuQsaNTBe2ISYUScereX2_Cvs-GDs6x4hGWstsqhNqv-vygNXDlXsj1Gh7XxI3wdViMNVDll0NkSAOhKX2IBK4r3HjJBxGfz4xnW7-XjxFAssUJz7Pty226Hi36Ymf-62id8nie1MQIu-9JUbXxAD5KY5PrCjjyizd3HwrmDdL5kz_RkxKc___vFshsPEhx88ctIATzR_BKyLr-UqScgS8PhnldNBE962spzDATkMw2gtgkJ_7pDYrWL7aRGToUq8VuskTrbtoHKNVcDQqNnDraKoVuivam_vsNVE9KBVcxTU5s-SC0-YQEv9F5souGXMx1CkBQiwnWvPTz5lAzlRuOeYpdnFddVxPut_oJnDjdj9jvxpQGLABR9eL2nF-9vgd_oonJxByL6ApCEbbKs1NwLhcVmlrhNJHv5kfvrlxok5vF3bfqtQJ0BaK2ze_-6KWcgkC0RyCrDkt-4HYwTQILB--hxwPURMxaMy32cSOoMz_10Ed4SXNwogwpZgzvUWtJSspT3nqCN0UJupH6v_cTFztMYY2yacKiafGLGqwPeCfj7AjGXFPHR1OAeS0OHnf98yMT6yhLAEn4dCyFEsWYYLN9FjEuaI1tlqlDkNRJIHgRt2UO2bCH_GV_Hryzvbq_0Wlai-Xy0 "LAYOUT_TOP_DOWN Sample")

Using `LAYOUT_LEFT_RIGHT`

```csharp
@startuml LAYOUT_LEFT_RIGHT Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

LAYOUT_LEFT_RIGHT

Person(admin, "Administrator")
System_Boundary(c1, 'Sample') {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")
@enduml
```

![LAYOUT_LEFT_RIGHT Sample](http://www.plantuml.com/plantuml/png/xLfjRziu4lwkNy5rFgG1dCP9NvhD9SRwHMc2Svp0KYwtrnO6ROrZOMLI8Ecwlcl_-mrbcP7D28BaDfzM1c9Pd7dccI7ry0NvGoegr7mMEVkamoCk9Dxi5LwEyri0av01SNlkZTltXvUt-ATpsxiTaBtBv78GoLFBA6IF9J5zjtFLNo5wr_znoV69uyY_GXPJGMS4ZUWyKZvyKwqeV6GpO8gCyG-8hDb2qFWX3DIKd3GQcUSp-kq6fAIFu8N_1NByhf7r4Z1Mb3r6GFxd4BmyH0MkbZ5SSgPM7YT9YvpIW2ymEJAXaGJdHnQc9GHVf119MSdU--HAdcWe-sasm8zdEPsVZ_YS1LGicyqrloqMEPmRLeGj7c-JAtdQvY80aVTSzoYGWCef19hcFkdH9P-hSbqSSMJSQ_rvU-yFMzxG-wVhTwuoAO_e-Az7ePDDURYks-vsCXPJoeA529K2HfIOWpr0T7PzEWDIw_1PE2OUPPBSU3LdDLR8X7FzTJxXUlpeC1S2WkO35GphUNP-f1kQf2E0AWZGN90WbEEvb25dTS800aaK9oCWNsaK1jhA-GrOy9IYoNUTgtzxD-pUFlJHBqvykL8S6OUwZn5ssxxdNlh3mVN7Avz4C57QHOIFKvNnmCAtLwCYXB8lR-guV0L3p83AEe5XH4SG7MHUXDh5HVgqHZP689KazIi6r3TwH3uFJ3wjMh_aHy3C1X1HdRASXd79HD5rkEPqN5-3dcpGCoMzgDKEoDeuss3yo9acRyfIAeo2yPJj5EypEpewb_WUdsq9PVDJ2l_b_4YtDu-EQXirG6uJmMTrDEEPlavfsqrrKZiyRDOE2Z5COZQORMDGD-hMnbV-LUgGUDi4xJRDyFpmK3CiXh9v5XWPy0tqFk0REEAYIZ4nwsAioaLzjgOcHiNY8cOnvAv5tYRUhL9SBQnMXRkxbpOVcozOFj6Sq3P48SFYDBRATr-bVFTtLeBtknSl3pdEevXFtmOev7PVgcozAcNJKxILNc_tmkLZmqJb4yq9NG2Hmx1Ngdo3AkNJYnixny7FgLyEE8fNVWLpyx0nYaaMP_AqWYPN4CLGUWE6paOT4bX-a6ejEVmq3OC0s9VkOTAmuNDVu7F_ZC-Wm6VmZ4-lmAUN-YJRnJ6FuOoqY0oJ5QBa4xMW0c-MKi7iDPhSYN16nP9017hZ9y-8FxKCISY8r5ZQmvl7CHSA4JDETy1Z341PiEqhqxLrj2HZpXZUGK0K9weWp3LJm0AqfVCW13R6FDol89OZ7YphUg4_9KcFXsCQ9N4PPuTFJ-A4K1qXPHYiYF6vIkxvP3Du05yXuh7E124fbgNgvltE7NYt_M7xuthdtZXzU_AXRThTV_lkeD_g3It3zwVwOmozFptVlScq7n-_FsrtRI3ByFVaAdjMaBCzrgyFPysclNatErtxl28nBJHeR-r8jofYxvmR7zwqtr_cxkJX6v9ZD1g-86VJ2uNaJrlwaqj-DVnVXBCPC7bKttG-N7OQnNL-GSxsQ2-ky-xdA0_N_jMmvtvq-rrdgdL3cXIT21w11Qkp0-Vx1TcuyBUFHkIxy_ryQsGqKmko6gM9YSakptPTygpJLYMQsZ1LqKrGOvW7QfmmeIGj-z1bdxYfq9VLmuHmYTEGLOQR9nK5OFec03aMpwD-Pf_PsY8dmZRVeVjDbU1iAuzDtaQkb41XE1FFItgrH1OoSR39ss1LYTiHBBvLArzCVjVA5uQhVcneA9OyFIIVLdxvXtpLru0TpXH5QaAIHQYc8IFgvLQ5OnCyPnteRwtogYpo_e5EumWXaR0nec8y3HMIaVMr0x98SFNTwhJqIAvI9LBHoQJwOh63arxhkkyECgktjszEkzrtFsdrPkhu8fEqIQTuRL5-UlvxUaOdgy8fhkddNpE96osmzTFikcs1AdkkJhBZDIjYPNZOWbwPqBRuM-IgoxwLK7dbDwubnTzaaIVxivWpVP-LVUDKAFZPUUDLySG11oIEvfB4rQO9GpPdcl1iMTSnCig-YtZVtDtsKHOpudtwhjs-RFmayJRPxIRUUutaob5iaqEkOd_0_LJtz9Sfzj-AZLPMFnYhT0ZyAbrFuN-rhfiyB5stUBoyhkUGSwn_672ST0DAWrc8Z6ej_HrA9QZY0e_4jrVnu-CwsVVeB8vW_s3r3cVci0MCXZIE4US1HgGLnr4uJjQNDNpKsQkJbdVtkk_ww2A0dBm-9ZV_wkYsLXJnXIHpYMoq5Ee4jCZDvf4AjOpwABmA157X32AC9P7RZvJTAxLgH9pK31kT0KJhh9vetKkGEjwLxzzvQAMDJEiJp4TG4d-2_j87qLcNFu05yrdqVm00 "LAYOUT_LEFT_RIGHT Sample")

## LAYOUT_WITH_LEGEND

Colors can help to add additional information or simply to make the diagram more aesthetically pleasing.
It can also help to save some space.

All of that is the reason, C4-PlantUML uses colors and prefer also to enable a layout without `<<stereotypes>>` and with a legend.
This can be enabled with `LAYOUT_WITH_LEGEND()`.

```csharp
@startuml LAYOUT_WITH_LEGEND Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_WITH_LEGEND Sample](http://www.plantuml.com/plantuml/png/PKzDozD04BxlhnZhuKsX9hpYoLDZBAtGrj2a5azXcunsOJ-MtLb24V-x4rfRmRqCEyyppySoaWoKZ8Pj-VthiUrENzfDjrsjL_lFq4ZZDOetolOw3PY2XWkHZn-B8iWn_wdeaiufOkYT9RIKzyuK1zNBCBYzGe-wg3wygxMqTDnj2oCZOU1LLp5VAeiXzsmjnF_UsLo86aDqDfE3KNO1itAQAbAGvC9iBfehovdkaqjsaE6QzQyBUBb5Vfd3Bm7y7aRPYETEUiyw9pn3wRtcdAISdV6gUhk0igdp_Qhbau3mFd-5tRTgmagjtHXXgXc17717BvbYaYR5Nj2EYWW3a3AesIjojj_tT1dTGDQvqnWK1zH_MprZ7IDVyjoqRTqmQo8zqAVC6Ydo5wVn8pZpxyaIxP2C_WC0 "LAYOUT_WITH_LEGEND Sample")

## LAYOUT_AS_SKETCH

C4-PlantUML can be especially helpful during up-front design sessions.
One thing which is often ignored is the fact, that these software architecture sketches are just sketches.

Without any proof

* if they are technically possible
* if they can fullfil all requirements
* if they keep what they promise

More often these sketches are used by many people as facts and are manifested into their documentations.
With `LAYOUT_AS_SKETCH()` you can make a difference.

```csharp
@startuml LAYOUT_AS_SKETCH Sample
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml

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

![LAYOUT_AS_SKETCH Sample](http://www.plantuml.com/plantuml/png/NL1DQzj04BtlhvYw1ylWIhZqr9DLOMgexGfBJiX9hAL9lB0Vo-u8OKB-UqROiKDq6JJlpVlOPIGPg3SQDldJ_qFTv5LJ_LlLnHegQRn6yKtPLlSTza73YSZ7traMv92-A3hrnpvYQ9qbj9IspcHxrShGkPr2ZpehVlqejRHqs6uo8oDXu5LJC5ygYo7rR2p4L-Ta9aI98JgRoCueEuT9FauLAKXoOJ8JrPd5JFF7zRQJuPoqYpbCBu6dCtWLmD_D9Xdms4ZlMUSHZv1xhpabAMSdl2g-po6lodItglaa8FnC5x1zA4OirzeD4SQI4SW1D_IIAQRNfDWBwa4HOG1I1ZLxHSxsTasNq0LadIkDGR57_T7g7kiG-PBdkgxBYbaZwORUPVuYHVx5SJm7PpwVBD5susk-0m00 "LAYOUT_AS_SKETCH Sample")
