db = db.getSiblingDB('proyectobst'); 

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
