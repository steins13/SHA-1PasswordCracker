import hashlib

def crack_sha1_hash(hash, use_salts=None):

  #open and read text files
  passwords = open("top-10000-passwords.txt")
  salts = open("known-salts.txt")
  allPasswords = passwords.readlines()
  allSalts = salts.readlines()
  #close
  passwords.close()
  salts.close()

  #function if no salt
  def noSalt(hash):
    for password in allPasswords:
      password = password.strip()
      hashPass = hashlib.sha1(password.encode()).hexdigest()
      
      if hashPass == hash:
        return password
    return "PASSWORD NOT IN DATABASE"

  #function if salt
  def withSalt(hash):
    for password in allPasswords:
      for salt in allSalts:
        password = password.strip()
        salt = salt.strip()

        appendSalt = password + salt
        hashPass = hashlib.sha1(appendSalt.encode()).hexdigest()
        if hashPass == hash:
          return password

        prependSalt = salt + password
        hashPass = hashlib.sha1(prependSalt.encode()).hexdigest()
        if hashPass == hash:
          return password
    return "PASSWORD NOT IN DATABASE"

  #returns
  if use_salts == True:
    return withSalt(hash)
  
  return noSalt(hash)
  