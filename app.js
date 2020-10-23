const http = require('http');
const MongoClient = require('mongodb').MongoClient;

const hostname = '127.0.0.1';
const port = 3000;
const mongourl = 'mongodb://localhost:27017';
const dbname = 'game-data';
const client = new MongoClient(mongourl);

async function run() {
  let games = [];
  try {
    await client.connect();

    const database = client.db(dbname);
    const collection = database.collection("PlayerGames");

    const query = { player: 'Zorozero'};

    games = await collection.find(query).toArray();
    //console.log(games);
  } finally {
    await client.close();
    return games;
  }
}

var games = run();
games.then(retVal => console.log(retVal));

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