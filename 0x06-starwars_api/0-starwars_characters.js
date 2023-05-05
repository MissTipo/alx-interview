#!/usr/bin/node

import request from 'request-promise';

const printCharacters = async (movieId) => {
  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/${movieId}/';
  try {
    const movieData = await request.get(movieUr);
    const characterUrls = JSON.parse(movieData).characters

    const characterPromises = characterUrls.map((url) => request.get(url));
    const characterResponse = await Promise.all(characterPromises);

    const characters = characterResponses.map((response) => JSON.parse(response))
    characters.forEach((character) => console.log(character.name));
  } catch (error) {
    console.error('Error retrieving character data: ${error}');
  }
};

const movieId = process.argv[2];
printCharacters(movieId);


