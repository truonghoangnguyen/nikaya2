import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-pro-exp-02-05"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="""[^1] 1. THUS HAVE I HEARD.[^1] On one occasion the
Blessed One was living in Ukkaṭṭhā in the Subhaga Grove at

"""
                ),
            ],
        ),


    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(
                text="""1. Translate texts from English to Vietnamese. The subject matter is Early Buddhism. Your translations should be easy to understand, using simple, everyday language. Maintain the original paragraph structure; do not add or remove any text. For key terms or concepts that require clarification, please provide the Vietnamese translation, followed by the original English word in quotation marks, and a brief explanation if necessary.
2. If content have --Annotation, that is footnote.
3. Place important-keyword/concept-keyword that at the end  as  `Từ ngữ`.
following format: - *Vietnamese term*/ pali term / English term / Brief explanation in Vietnamese
4. Remember do not add or remove any text"""
            ),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


generate()