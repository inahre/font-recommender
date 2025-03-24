Google Fonts Recommender (Tkinter GUI):

A simple Python application that recommends Google Fonts based on your desired font variants, subsets, and category. The app uses the Google Fonts API and a Tkinter-based GUI for user interaction.

Features:

- Fetches the most popular fonts from the Google Fonts API.

- GUI for filtering fonts based on:

  1. Variants (e.g., regular, italic, 700)

  2. Subsets (e.g., latin, cyrillic, greek)

  3. Category (e.g., sans-serif, serif, display, handwriting, monospace)

- Displays up to 10 font recommendations based on your input.

Installation:

  1. Clone this repository or copy the script:

     git clone https://github.com/your-username/font-recommender.git

  2. Install required Python libraries.

  3. Replace the placeholder API key with your own in the script:

     api_token = "YOUR_GOOGLE_FONTS_API_KEY"

How it works:

- The app pulls font metadata from the Google Fonts API, sorted by popularity.

- The user enters optional filters:

  1. Variants (e.g., regular, italic, 700italic)

  2. Subsets (e.g., latin, greek-ext)

  3. Category (e.g., sans-serif, display)

- It then matches fonts that include all given parameters.

- The top 10 popular matching fonts are displayed in the GUI.

