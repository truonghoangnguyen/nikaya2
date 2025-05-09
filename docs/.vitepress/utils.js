// Converts a string to a slug suitable for anchor links
import slugify from '@sindresorhus/slugify';

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

export { slugAnchor };
