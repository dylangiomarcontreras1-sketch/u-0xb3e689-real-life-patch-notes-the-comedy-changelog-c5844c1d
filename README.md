# Real-Life Patch Notes: The Comedy Changelog

[![make.fun competition](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![make.fun rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/dylangiomarcontreras1-sketch/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![make.fun reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/dylangiomarcontreras1-sketch/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

Entry for the make.fun bounty [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d).

## The entry

> v3.7.1: fixed a bug where the sneeze aborts at 90% and the eyes are billed for the cleanup.

91 characters, one line, UTF-8, ASCII only.

## Approach

The brief asks for a single line in the register of a real release note: a version
number, a terse engineering voice, and a fix stated as if it shipped. The judge weighs
five things in order: it must be a patch note about a real-life or human-biology bug and
read as comedy, the joke must rest on a real comedic idea, it must sound like an actual
changelog, it must name a specific bug the reader recognises, and every character must
work.

The line is built on an aborted operation. A sneeze that stops at ninety per cent is a
familiar, physically annoying failure: the body starts a job, cancels it late, and leaves
a cleanup handler running. The eyes pay for it. That is the joke, and it is also an
accurate description of what happens, which is why the engineering voice holds up.

The wording is tuned to the rubric rather than to length:

- A made-up patch version, `v3.7.1`, so the note reads as something that shipped.
- One specific, measurable detail, `90%`, instead of an adjective.
- The failure and its cost stated flatly, with no setup the punchline does not need.
- No address to the judge, no padding, and no dependence on the word "bug" to carry the
  humour.

## How it runs

The program is a single zero-dependency Python 3 file. It writes the text to
`/output/entry.txt` as UTF-8 with no trailing newline, creating the output directory if
it is missing.

```sh
python3 main.py
```

`render()` enforces the gate in code: the text must be between 1 and 160 characters and
must not be only white space. The output is a constant, so repeated runs are byte
identical.

## Verification

- Output length: 91 characters, 91 bytes, single line, no trailing newline.
- Determinism: five consecutive runs produce the same SHA-256,
  `45c1e3adf5476368757c0d0c55beb01973f25ca75179e63e45dff8e4dc2698f3`.
- Gate: 1 to 160 characters, UTF-8 text, not only white space.

## Links

- Bounty: https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
- make.fun: https://make.fun

## License

MIT. See [LICENSE](LICENSE).
