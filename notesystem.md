Hi there, I've been accumulating a pile of notes/ideas for a while in Apple Notes, but I've been having trouble actually putting them to good use/viewing them, just because of crap structuring on my part.

Over time I've gotten what features of a note organization system would work for me, which I detail below as requirements for the system.

Of note, my profession is a software developer. I'm not particularly picky UIs, and in fact I would probably prefer if I could operate
the notes system from the terminal. I was originally planning on building/coding this notes system for myself, but I want to see
if a solution already exists.

OS independent [REQUIRED]

- I do not want to be tied to a specific OS, preferably support for both Windows and Linux

Notes should support hand writing [REQUIRED]

- none of my ideas are typed, they are handwritten with my Apple pencil, and sometimes I draw figures
- [IDEAL] (this is something I don't know), the notes should be saved in some "universal"/standardized file format that can support hand written figures
  - To my knowledge, the only file format that supports that is PDF, but if there's a better one let me know!

Notes can have tags [REQUIRED]

- and to be clear, a single note can have many tags

Notes can be queried [REQUIRED]

- example queries: (`Dog`), (`Dog` or `Cat`), (`Dog` and `Car`)
- [ideal]: The querying system is highly flexible, able to specify and filter by arbitary boolean formulas

Tags can be "namespaced"/sub-tagged [DESIRABLE]

- What I mean by this is that I can create regular tags like `Dog`

  - But the ``Dog` tag can also have subtags like

    - `Dog["brown", "white", "black"]`

  - and importantly, these sub-tags are different when under different parents

    - for example I should be able to also define
      `Car["white", "black", "red"]`, with no conflict between the "white" and "black" tags

- Querying by tags/subtags should be flexible like
  (`Dog`), (`Dog:brown`), (`Dog:brown` and `Car:brown`), (`Dog:brown` or `Car`)

Should be easily backup-able [REQUIRED]

- Some type of way to export/backup all my notes and metadata to either a different computer/drive/the Cloud
- [IDEAL] I would like is having all the data, notes and tag metadata, in a single folder. That way, I could version control it with Git and also back it up with a regular cloud Git service

After querying, I want at least 2 options [REQUIRED]

- see notes sorted by date created
- see notes sorted random shuffle, so I can see all the notes that satisfy my query in a random order
- [IDEAL] I would prefer if the query would just output the raw data paths to the files, so I could build my own infrastructure on top of it
