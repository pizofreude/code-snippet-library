// @maintainer: Pizofreude
// ---------------------------------------------------------------------
// Reads from MQTT topic, saves the messages in database and direct to API endpoint.

// --- Imports
// Importing MQTT library used to connect to Streamr broker.
const mqtt = require('mqtt');

// Importing express library used to create the API Rest.
const app = require('express')()

// Importing Sequelize library to connect and manage database.
const { Sequelize, DataTypes } = require("sequelize");



// --- Environment variables.
// Address of the MQTT broker
const STREAMRADDRESS = process.env.STREAMRADDRESS;

// Port of the MQTT broker
const STREAMRPORT = Number(process.env.STREAMRPORT);
const STREAMRUSER = process.env.STREAMRUSER;
const STREAMRAPIKEY = process.env.STREAMRAPIKEY;
const STREAMRTOPIC = process.env.STREAMRTOPIC;

// Database credentials and table name
const DBADDRESS = process.env.DBADDRESS;
const DBPORT = Number(process.env.DBPORT);
const DBNAME = process.env.DBNAME;
const DBUSER = process.env.DBUSER;
const DBPASSWORD = process.env.DBPASSWORD;



// --- Main
// Connect to the MQTT Streamr broker
// The connection string syntax is as follows: protocol://username:address@host:port
const client = mqtt.connect(`mqtt://${STREAMRUSER}:${STREAMRAPIKEY}@${STREAMRADDRESS}:${STREAMRPORT}`);
console.log("Connecting to MQTT broker...");

// Create a database client with the address and credentials.
// The connection string syntax is as follows: protocol://username:address@host:port/database
const sequelize = new Sequelize(`postgres://${DBUSER}:${DBPASSWORD}@${DBADDRESS}:${DBPORT}/${DBNAME}`, { logging: false });
console.log("Connecting to PostgreSQL database...");



// --- Database Model
const Messages = sequelize.define("Messages", {

  // Sender of the message
  sender: {
    type: DataTypes.STRING,
    allowNull: false
  },

  // Text of the message
  text: {
    type: DataTypes.STRING,
    allowNull: false
  },

  // Date of the message
  date: {
    type: DataTypes.STRING,
    allowNull: false
  },
});



// --- Event handlers
client.on('connect', async () => {

  // Subscribe to topic
  console.log("Connected to MQTT broker!")
  client.subscribe(STREAMRTOPIC);

  // Database Logic...
  try {
    // Authenticate the database.
    await sequelize.authenticate();
    console.log("Connected to PostgreSQL database server!");

    // Sync the Messages table
    await Messages.sync();
    console.log("Created Messages table in database:", DBNAME);

    // Start the API Rest listening on port 8888.
    app.listen(8888, () => {
      console.log("API listening on port 8888");
    });

  } catch (error) {
    throw error;
  }
});

// Client receives message from topic...
client.on('message', async (topic, payload) => {

  // The payload will be a JSON string
  const { message } = JSON.parse(payload);

  // Create a new message in the database.
  const dbmessage = await Messages.create(message);

  // Console log the message now stored in the db.
  console.log(dbmessage.dataValues);
});

// Create API Endpoint
app.get('/messages/:sender', async (req, res) => {

  // Get sender from request parameters
  const { sender } = req.params;

  // Find all the messages in database that have the same sender as the one specified in the request.
  const messages = await Messages.findAll({ where: { sender } });

  // Send the messages as a response.
  res.json(messages);
});