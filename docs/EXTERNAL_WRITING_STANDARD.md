# External Writing Standard

Public writing has one job: help a smart, busy person understand the product in one read.

## What readers should understand

Within the first 90 seconds, a reader should be able to explain:

1. What problem this project solves.
2. What changes for the founder who uses it.
3. How it works at a useful level.
4. What has actually been built and tested.
5. What remains unproved.

## Writing rules

- Lead with the human outcome, not the architecture.
- Use short sentences and plain words.
- Keep one main idea in each sentence.
- Explain a technical term when it first becomes necessary.
- Move implementation detail into the technical document.
- Preserve important reasoning. Plain language is not shallow language.
- State proof limits directly.

## What does not count as proof

The line `Style check: external style applied.` is an internal review cue. It must never appear in published copy. Its presence does not show that the writing is clear.

A narrative audit also does not prove readability. It can confirm that the right ideas are present while the writing still forces readers to decode internal language.

## Release rule

Every public release must pass three separate checks:

1. **Claim check:** the statements are accurate and supported.
2. **Reader check:** the public front door is clear in one read.
3. **Technical check:** setup, links, tests and safety controls work.

The release stops when any one of these checks fails.

## Proof rule

This standard is implemented when the release gate can reject the old failure and accept a clear alternative. It is proved only after later public artifacts pass without the founder having to identify the same problem again.
