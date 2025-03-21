# Note Popup Example


::: details Click me to toggle the code {open}
```js
console.log('Hello, VitePress!')
```
:::



Attaches event [^31](/kinhtrungbo/nanamoli-bodhi-en/outro/notes/001#_31){.note}  [ꜛ](/kinhtrungbo/nanamoli-bodhi-en/outro/notes/001#_31){target="_blank"} nhwng van de




This is an example of how the note popup works. Hover over these links:

# Using custom anchors {#my-anchor}

*i want [all of this](/link){target="_blank"} to be italics*


# header {.style-me}
paragraph {data-toggle=modal}

paragraph *style me*{.red} more text

- Here is a [pop11](/kinhtrungbo/nanamoli-bodhi-en/outro/notes/001#_31){.red}

- Here is a [pop](/kinhtrungbo/nanamoli-bodhi-en/outro/notes/001#_31){target="_blank"}  <a href="/kinhtrungbo/nanamoli-bodhi-en/outro/notes/001x#_31">link </a> that will show a popup when hovered.
- You can also <a href="/kinhtrungbo/nanamoli-bodhi-vi/001-the-root-of-all-things.md" class="note">hover over this link</a> to see another example.

The popup should appear below the link, displaying the content from the linked URL.

## Implementation Details

The `NotePopup` component:

1. Attaches event listeners to track mouseover events on elements with the `.note` class
2. Fetches the HTML content from the linked URL when hovering
3. Displays a popup with the fetched content
4. Positions the popup near the hovered element
5. Handles loading states and errors

To use this component, simply:

1. The component is registered globally in the VitePress theme
2. Add it to your page: `<NotePopup />`
3. Add class="note" to any links that should trigger the popup
