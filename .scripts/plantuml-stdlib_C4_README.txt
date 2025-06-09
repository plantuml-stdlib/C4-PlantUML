---
name: C4
display_name: C4 (C4-PlantUML)
description: The C4 library enables a simple way of describing and communicate software architectures with an intuitive language.
author: Ricardo Niepel, kirchsth and contributors
version: {release version without v}
release: https://github.com/plantuml-stdlib/C4-PlantUML/tree/release/v{release version without v}
license: MIT
source: https://github.com/plantuml-stdlib/C4-PlantUML
origin: https://c4model.com
---
**C4 specific stdlib properties:**  
![name: C4](https://img.shields.io/badge/name-C4-black)
![display_name: C4 (C4-PlantUML)](https://img.shields.io/badge/display__name-C4_(C4--PlantUML)-black)  
![version: {release version without v}](https://img.shields.io/badge/version-{release version without v}-black)
[![release: https://github.com/plantuml-stdlib/C4-PlantUML/tree/release/v{release version without v}][Release Badge]][Release Link]  
![description: The C4 library enables a simple way of describing and communicate software architectures with an intuitive language.](https://img.shields.io/badge/description-The_C4_library_enables_a_simple_way_of_describing_and_communicate_software_architectures_with_an_intuitive_language.-black)  
[![license: MIT][License Badge]][License Link]
![author: Ricardo Niepel, kirchsth and contributors](https://img.shields.io/badge/author-Ricardo_Niepel,_kirchsth_and_contributors-black)  
[![source: https://github.com/plantuml-stdlib/C4-PlantUML][Source Badge]][Source Link]
[![origin: https://c4model.com][Origin Badge]][Origin Link]  

[Release Badge]: https://img.shields.io/badge/release-https://github.com/plantuml--stdlib/C4--PlantUML/tree/release/v{release version without v}-blue
[Release Link]: https://github.com/plantuml-stdlib/C4-PlantUML/tree/release/v{release version without v}
[License Badge]: https://img.shields.io/badge/license-MIT-green
[License Link]: https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/LICENSE
[Source Badge]: https://img.shields.io/badge/source-https://github.com/plantuml--stdlib/C4--PlantUML-blue
[Source Link]: https://github.com/plantuml-stdlib/C4-PlantUML
[Origin Badge]: https://img.shields.io/badge/origin-https://c4model.com-blue
[Origin Link]: https://c4model.com

**Support and community:**  
[![issues: C4][Issues Badge]][Issues Link]
[![open master commits][Open Badge]][Open Link]  
[![discussions: C4][Discussions Badge]][Discussions Link]  

[Issues Badge]: https://img.shields.io/badge/issues-https://github.com/plantuml--stdlib/C4--PlantUML/issues-orange
[Issues Link]: https://github.com/plantuml-stdlib/C4-PlantUML/issues
[Open Badge]: https://img.shields.io/github/commits-difference/plantuml-stdlib/C4-PlantUML?base=release%2Fv{release version without v}&head=master&label=Open%20master%20commits&color=orange
[Open Link]: https://github.com/plantuml-stdlib/C4-PlantUML/compare/v{release version without v}...master
[Discussions Badge]: https://img.shields.io/badge/discussions-https://github.com/plantuml--stdlib/C4--PlantUML/discussions-orange
[Discussions Link]: https://github.com/plantuml-stdlib/C4-PlantUML/discussions

# C4 library (C4-PlantUML) [C4]

The C4 library enables a simple way of describing and communicate software architectures with an intuitive language.

It is the PlantUML integrated version of [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) and has the big advantage that it can be used without additional external includes.
(E.g. container diagrams can be drawn with `!include <C4/C4_Container>` and no `!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml` is required.)

## Example of usage:

```plantuml
@startuml
!include <C4/C4_Container>
LAYOUT_LEFT_RIGHT()

Person(admin, "Administrator")
System_Boundary(c1, "Sample System") {
    Container(web_app, "Web Application", "C#, ASP.NET Core 2.1 MVC", "Allows users to compare multiple Twitter timelines")
}
System(twitter, "Twitter")

Rel(admin, web_app, "Uses", "HTTPS")
Rel(web_app, twitter, "Gets tweets from", "HTTPS")

SHOW_LEGEND()
@enduml
```

<br/>

**renders following image:**

[![Example](https://www.plantuml.com/plantuml/png/JL1TQy9047o_Nx5DNn8GYyN7KanJgmMhOivAdyAPRE7WFiBT1f7I_zvDjTfxMUvcPcTk9f5KeCuQSQDTRRe6uQ4OtnNZgl2Eb7OO7iKY_rXjPRMOliXgypgRopGJOeqXUfUgncetW2JlfuuK5FcGPA8yHa9RFVdEDIeSqth4f5BPrY2Si2I3Bm5yBaxf0VULQbjcxd0FUTiQNIlItYNyLDmE82_Nm-LKiYGWt0z7yFPUz5XkZ3z4w2A62EIXzhPLJB6T8TrRoeCcmW2aBHhsYXpn-nmofHF8Uyuq1iK6pT_dhh6saPKyvrAkooJx9LtGwvePKkGhzkCpUFjV8ihvQiTTpgRBP-vnWgxX-dy0)](https://www.plantuml.com/plantuml/uml/JL1TQy9047o_Nx5DNn8GYyN7KanJgmMhOivAdyAPRE7WFiBT1f7I_zvDjTfxMUvcPcTk9f5KeCuQSQDTRRe6uQ4OtnNZgl2Eb7OO7iKY_rXjPRMOliXgypgRopGJOeqXUfUgncetW2JlfuuK5FcGPA8yHa9RFVdEDIeSqth4f5BPrY2Si2I3Bm5yBaxf0VULQbjcxd0FUTiQNIlItYNyLDmE82_Nm-LKiYGWt0z7yFPUz5XkZ3z4w2A62EIXzhPLJB6T8TrRoeCcmW2aBHhsYXpn-nmofHF8Uyuq1iK6pT_dhh6saPKyvrAkooJx9LtGwvePKkGhzkCpUFjV8ihvQiTTpgRBP-vnWgxX-dy0)
