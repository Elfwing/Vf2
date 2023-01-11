/* This file is our "controller file" and is responsible for
handling all of our routes and rendering our views 
and rendering our views*/

const express = require("express");

const path = require("path");
require("colors");

const app = express();

//for body parser, leyfir req body
app.use(express.urlencoded({ extended: false }));

//server static files
app.use(express.static(path.join(_dirname, "public")));

//template engine
app.set("views", path.join(_dirname, "views"));
app.set("view engine", "ejs");

//routers
app.get("/", (req, res) => {
  res.render("index", { title: "home" });
});

app.get("/help", (req, res) => {
  res.render("help", { title: "help" });
});

//errors : page not found
app.use((req, res, next) => {
  const err = new Error("Page not found");
  err.status = 404;
  next(err);
});

//handling errors
app.use((err, req, res) => {
  res.status(err.status || 500);
  res.send(err.message);
});

//setting up the server
app.listen(3000, () => {
  console.log("Server is running on port 3000............".green);
});
