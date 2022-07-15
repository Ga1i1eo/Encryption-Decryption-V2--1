while True:


  print("1-Encrypt")
  print("2-Decrypt")

  task=input("Enter number: ")
  
  if task=="1":

    message=input("Enter your message: ")
    crypt=""

    for a in message:
      ascode=ord(a)
      ent=ascode-+9
      en=ent/7
      # print (a,"",ascode,chr(en))
      crypt=crypt+chr(en)

    print ("The encrypted message is: %s" %(crypt))

  if task=="2":

    message=input("Enter your message to decrypt: ")
    crypt=""
  
    for a in message:
      ascode=ord(a)
      ent=a+9
      en=ent*7
     
      # print (a,"",ascot,chr(en))
      crypt=crypt+chr(en)

    print ("The decrypted message is: %s" %(crypt))

