db = db.getSiblingDB('proyectobst'); // base de datos que vas a usar

db.createUser({
  user: 'nataly-33',
  pwd: 'passWord63',
  roles: [
    {
      role: 'readWrite',
      db: 'proyectobst',
    },
  ],
});
