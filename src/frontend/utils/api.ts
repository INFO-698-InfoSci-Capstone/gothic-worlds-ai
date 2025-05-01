import axios from 'axios';
import DEMO_CHARACTERS from '../data/demoCharacters';
import dotenv from 'dotenv';

// Load environment variables from .env (located at the project root)
dotenv.config({ path: '../../.env', override: true });

const BACKEND_PORT = parseInt(process.env.BACKEND_PORT || '5000', 10);

export const fetchCharacters = async (
  setCharacters: (characters: any[]) => void,
  setIsLoading: (isLoading: boolean) => void
) => {
  try {
    setIsLoading(true);
    const response = await axios.get(`http://localhost:${BACKEND_PORT}/api/characters`);
    console.log("API Response:", response.data);
    if (response.data && response.data.length > 0) {
      setCharacters(response.data);
    } else {
      console.log("No characters returned from API, using demo data");
      setCharacters(DEMO_CHARACTERS);
    }
  } catch (error) {
    console.error("Error fetching characters:", error);
    console.log("Error fetching characters, using demo data");
    setCharacters(DEMO_CHARACTERS);
  } finally {
    setIsLoading(false);
  }
};
