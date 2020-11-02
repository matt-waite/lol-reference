const http = require('http');
const MongoClient = require('mongodb').MongoClient;

const hostname = '127.0.0.1';
const port = 3000;
const mongourl = 'mongodb://localhost:27017';
const dbname = 'game-data';
const client = new MongoClient(mongourl);

async function getPlayerGames(db, playerName) {
  let games = [];
  try {
    const collection = db.collection("PlayerGames");
    const query = { player: playerName };

    games = await collection.find(query).toArray();
  } finally {
    return games;
  }
}

async function main() {
  await client.connect();
  const database = client.db(dbname);

  let player1 = getPlayerGames(database, "WildTurtle");
  let player2 = getPlayerGames(database, "Sneaky");
  Promise.all([player1, player2]).then(retVal => console.log(`${retVal[0].length} - ${retVal[1].length}`));

  await client.close();
}

main();

/*
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
*/