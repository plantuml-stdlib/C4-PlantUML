# Contributing guidelines

Welcome! If you would like to contribute to [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML/), you have come to the right place!

There are different ways you can contribute:

- Ask questions (or answer them)
- Give feedback (or discuss feedback given by others)
- Report issues (or resolve them)
- Request new feature (or build them)
- Help create a release

## Questions

When you have a question about something related to C4-PlantUML, first [search the issue](https://github.com/plantuml-stdlib/C4-PlantUML/issues?q=) to see if a similar question has already been answered.
If no issue is found that answers your question, [open a new issue](https://github.com/plantuml-stdlib/C4-PlantUML/issues/new?title=[Question]&labels=question) and ask.

Provide as much context and detail as needed. The higher the quality of the issue, the easier it is to get an answer.
Don't worry about this too much, though, if anything is unclear, or more information is needed, you'll be asked to provide specifics.

Your question could be of interest to other users, in which case it might even be added to the project documentation!

Sometimes, the answer might be that either we don't know, or the question is not really about this project, but more about C4 or PlantUML (or other tools and techniques).
Maintainers and contributors will try to answer any question as best they can, but please be respectful if your question remains unaswered or you are directed elsewhere.

To keep things organised, if an issue with a question is inactive for a longer period of time, it will be marked as "stale". Shortly thereafter, the issue will be closed, regardless of the answer.

## Feedback

To keep things organised, if an issue with feedback is inactive for a longer period of time, it will be marked as "stale". Shortly thereafter, the issue will be closed, regardless of the answer.

## Issues

To keep things organised, if an issue is inactive for a longer period of time, it will be marked as "stale". Shortly thereafter, the issue will be closed, regardless of the answer.

## Features

To keep things organised, if an issue with a feature request is inactive for a longer period of time, it will be marked as "stale". Shortly thereafter, the issue will be closed, regardless of the answer.

Merge requests are not marked as stale nor automatically closed.

## Release

When creating a release, the following needs to happen:

- [ ] Resolve all open issues related to [the upcoming milestone](https://github.com/plantuml-stdlib/C4-PlantUML/milestones/)<br>
      <sup>_So all desired features are present in the planned release_
- [ ] Update the `!include` paths to point to the new release URL<br>
  <sup>_So users that include `https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/vX.X.X/C4_Component.puml` actually get the related files instead of files from the main branch._
- [ ] Update the version in [`C4.puml`](https://github.com/plantuml-stdlib/C4-PlantUML/blob/master/C4.puml#L6)<br>
  <sup>_So user can debug/output the version they are using_ 
- [ ] Check if anything else that needs changing. Copyright year? Any contrib files? URLS?<br>
  <sup>_Making everything is in order before the release, so we do not have to make minor releases afterwards_
- [ ] Open an MR to incorporate the changes needed for version release into the `main` branch.<br>
  <sup>_So there is a fixed/traceable moment in time that marks the change_
- [ ] Create [a new release](https://github.com/plantuml-stdlib/C4-PlantUML/releases/new?title=Release%202.X.X&tag=v2.X.X&release-notes=true) of the latest changes (using "Generate Release Notes").<br>
  <sup>_So there is a fixed/traceable moment in time that marks the change_
- [ ] Create a merge-request for the release at [PlantUML-stdlib](https://github.com/plantuml/plantuml-stdlib/)<br>
  <sup>_So PlantUML users also have access to the latest greatest C4-PlantUML_

The easest way to track these tasks, and let others know how a release is progressing, copy/paste the above list into a new issue.
