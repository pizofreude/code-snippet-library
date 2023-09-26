// @author: Pizofreude
// ---------------------------------------------------------------------
// This is a service that reads from MQTT topic
//& saves the messages in a database as well as exposes API endpoint.

// --- Imports
// Import libraries
// Importing MQTT library used to connect to Streamr broker.
const mqtt = require('mqtt');

// Importing express library used to create the API Rest.
const app = require('express')()

// Importing Sequelize library used to connect and manage the database.
const { Sequelize, DataTypes } = require("sequelize");



// --- Configuration variables.
// Address of the MQTT broker
const STREAMRADDRESS = "localhost";

// Port of the MQTT broker
const STREAMRPORT = 1883;
const STREAMRUSER = "pizofreude";
const STREAMRAPIKEY = MY_STREAMR_NODE_API_KEY;
const STREAMRTOPIC = "MY_TOPIC/streamr_chat";

// Database credentials and table name
const DBADDRESS = "localhost";
const DBPORT = 5432;
const DBNAME = "chatdb";
const DBUSER = "root";
const DBPASSWORD = "root";



// --- Main
// Connect to the MQTT Streamr broker
// The connection string syntax is as follows: protocol://username:address@host:port
const client = mqtt.connect(`mqtt://${STREAMRUSER}:${STREAMRAPIKEY}@${STREAMRADDRESS}:${STREAMRPORT}`);
console.log("Sabr, connecting to MQTT broker...");

// Create a database client with the address & credentials.
// The connection string syntax is as follows: protocol://username:address@host:port/database
const sequelize = new Sequelize(`postgres://${DBUSER}:${DBPASSWORD}@${DBADDRESS}:${DBPORT}/${DBNAME}`, { logging: false });
console.log("Sabr, connecting to PostgreSQL database...");



// --- Database Model
const Messages = sequelize.define("Messages", {

  // Sender of the message
  sender: {
    type: DataTypes.STRING,
    allowNull: false
  },

  // Text message
  text: {
    type: DataTypes.STRING,
    allowNull: false
  },

  // Message Date
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
    // Authenticate to database.
    await sequelize.authenticate();
    console.log("Connected to PostgreSQL database server!");

    // Sync the Messages table
    //this will create the Messages table if it doesn't already exist in the database.
    await Messages.sync();
    console.log("Created Messages table in database:", DBNAME);

    // Start the API Rest listening on port 3000.
    app.listen(3000, () => {
      console.log("API listening on port 3000");
    });

  } catch (error) {
    throw error;
  }
});

// Client receives a message from the topic.
client.on('message', async (topic, payload) => {

  // The payload will be a JSON string.
  const { message } = JSON.parse(payload);

  // Create a new message in database.
  const dbmessage = await Messages.create(message);
   
  // Log message stored in db.
  console.log(dbmessage.dataValues);
});

// Create API Endpoint with a paramter for the sender of the messages.
app.get('/messages/:sender', async (req, res) => {

  // Get the sender from the request parameters.
  const { sender } = req.params;

  // Find all messages in database with similar sender as the one specified in request.
  const messages = await Messages.findAll({ where: { sender } });

  // Send the messages as a response.
  res.json(messages);
});