Introduction :
--------------
This section consists of a CPU accelerated text hasher and dictionary attack hash cracker.
These 2 programs use the "multiprocessing" library and spawn new processes for each hash generated/cracked.

Operating Systems Supported :
-----------------------------
MacOS, Linux & other UNIX based systems.

Work Done thus far :
--------------------
--> Made a base working model
--> Improved time complexity
--> Improved speed through CPU acceleration

Work that needs to be done :
----------------------------
--> Need to implement GPU acceleration using the CUDA/OpenCL libraries (Numba/PyOpenCL) for Python.

Usage :
-------

Just to clarify, you can get the usage options just by typing either "./CPU_accelerated_password_hasher.py" or
"./CPU_accelerated_dict_attack_hash_cracker.py" and pressing Enter/Return.

  (i) Password Hasher :
      -----------------
      ./CPU_accelerated_password_hasher.py --pass-list [PASSWORD LIST] --hash-type [HASH TYPE] --output-file [OUTPUT FILE]
      
  (ii) Dictionary Attack Hash Cracker :
       --------------------------------
       ./CPU_accelerated_dict_attack_hash_cracker.py --hash-list [HASH FILE] --hash-type [HASH TYPE] --dictionary [DICTIONARY]
