# Spotify-Time-Machine

This project automates the creation of a Spotify playlist based on the Billboard Hot 100 songs for a specific date using the Spotify and Billboard charts APIs. The playlist can be created either publicly or privately on your Spotify account, pulling song data from Billboard's Hot 100 chart for any date you choose.

## Features

- Fetch Billboard Hot 100 song data for a specified date.
- Search for songs on Spotify.
- Create a new Spotify playlist with those songs.
- Automatically adds the songs to your playlist.

## Project Structure

- `main.py`: The main script that handles Spotify authorization, song search, playlist creation, and adding songs to the playlist.
- `billboard.py`: A module that scrapes Billboard's Hot 100 chart for song data based on the date provided by the user.

## Prerequisites

To run this project, you need the following:

- Python 3.12
- A [Spotify Developer account](https://developer.spotify.com/dashboard/applications) to get your `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI`.
- A Spotify account with permissions to create playlists.
- Environment variables (`CLIENT_ID`, `CLIENT_SECRET`, `ID`) set in a `.env` file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/spotify-billboard-playlist.git
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory:
   ```bash
   touch .env
   ```

4. **Add your Spotify credentials** to the `.env` file:
   ```
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   ID=your_spotify_user_id
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. You will be prompted to enter a date in the format `YYYY-MM-DD`. This will be the date for which you want to fetch the Billboard Hot 100 chart.

3. The script will:
   - Fetch the Billboard Hot 100 songs for that date.
   - Search for those songs on Spotify.
   - Create a new Spotify playlist named after the Billboard chart for that date.
   - Add the songs to the playlist.

4. You can then view the playlist in your Spotify account.

## Example

When you run the script and enter `2020-09-19`, a new playlist named `2020-09-19 Billboard 100` will be created in your Spotify account, containing the top 100 songs from that Billboard chart.

## Technologies Used

- **Python**
- **Spotipy**: A Python library for the Spotify Web API.
- **BeautifulSoup**: For scraping the Billboard Hot 100 chart.
- **requests**: For making HTTP requests.

## License

This project is licensed under the MIT License.

Feel free to contribute by submitting issues or pull requests!
