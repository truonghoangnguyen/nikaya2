// Converts a string to a slug suitable for anchor links
import slugify from '@sindresorhus/slugify';
import MarkdownIt from 'markdown-it'

function slugAnchor(inputString) {
  // Regex breakdown:
  // ^           - Anchors the match to the beginning of the string.
  // AN          - Matches the literal characters "AN".
  // \s          - Matches a single whitespace character (the space after AN).
  // (           - Start of a capturing group.
  //   \d+       - Matches one or more digits (the part before the dot).
  //   \.        - Matches a literal dot (needs to be escaped).
  //   \d+       - Matches one or more digits (the part after the dot).
  // )           - End of the capturing group.
  // The rest of the string (e.g., "--10 text") is ignored by this regex.
  const regex = /^AN\s(\d+\.\d+)/;
  const match = inputString.match(regex);

  if (match && match[1]) {

    // match[0] is the full matched string (e.g., "AN 1.1")
    // match[1] is the content of the first capturing group (e.g., "1.1")
    return `AN${match[1]}`;
  } else {
    return slugify(inputString);
    // Handle cases where the pattern is not found
    // console.warn(`Pattern "AN <num>.<num>" not found in: "${inputString}"`);
    // return null; // Or return an empty string, or throw an error, depending on desired behavior
  }
}



// Xử lý `{#id}` cuối đoạn văn một cách độc lập với markdown-it-attrs.
// markdown-it-attrs có bug: nếu đoạn văn có markup (in nghiêng, in đậm...)
// trước {#id}, và phần text còn lại sau markup có MỘT dấu " lẻ (không cặp),
// logic tìm dấu { của nó bị "kẹt" ở trạng thái "đang trong giá trị có ngoặc
// kép" và không bao giờ tìm ra {, nên {#id} bị bỏ sót, in ra literal.
// Rule này chạy trước, tự strip {#id} bằng regex thuần, tránh hẳn bug đó.
function idAnchorFix(md) {
  const ID_RE = /[ \t]*\{#([A-Za-z0-9_\u00C0-\uFFFF-]+)\}[ \t]*$/

  function findOwningOpenToken(tokens, inlineIdx) {
    let idx = inlineIdx - 1
    let depth = 0
    let found = null
    for (; idx >= 0; idx--) {
      if (tokens[idx].nesting === -1) { depth++; continue }
      if (tokens[idx].nesting === 1) {
        if (depth === 0) { found = tokens[idx]; break }
        depth--
      }
    }
    if (!found) return null
    if (!found.hidden) return found
    // Token bao ngoài bị hidden (vd paragraph_open trong tight list item)
    // -> tiếp tục tìm ancestor hiển thị thật sự (vd list_item_open) để
    // gán id vào đó, nếu không id sẽ "biến mất" vì token không render ra tag.
    let outerIdx = idx - 1
    let outerDepth = 0
    for (; outerIdx >= 0; outerIdx--) {
      if (tokens[outerIdx].nesting === -1) { outerDepth++; continue }
      if (tokens[outerIdx].nesting === 1) {
        if (outerDepth === 0) return tokens[outerIdx]
        outerDepth--
      }
    }
    return found
  }

  md.core.ruler.before('linkify', 'trailing_id_attr', (state) => {
    const tokens = state.tokens
    for (let i = 0; i < tokens.length; i++) {
      const tok = tokens[i]
      if (tok.type !== 'inline' || !tok.children?.length) continue

      const children = tok.children
      const last = children[children.length - 1]
      if (last.type !== 'text') continue

      const match = ID_RE.exec(last.content)
      if (!match) continue

      last.content = last.content.slice(0, match.index)

      const openTok = findOwningOpenToken(tokens, i)
      if (!openTok) continue

      const idx = openTok.attrIndex('id')
      if (idx < 0) openTok.attrPush(['id', match[1]])
      else openTok.attrs[idx][1] = match[1]
    }
  })
}


export { slugAnchor, idAnchorFix };
