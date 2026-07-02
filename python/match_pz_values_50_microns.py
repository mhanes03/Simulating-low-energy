import numpy as np 

Event_id_100, Pz_100 = np.loadtxt('pz_before_and_after_210.txt',  unpack=True)
Event_id_120, Pz_120 = np.loadtxt('test.txt',  unpack=True)

#open('pz_before_and_After.txt', 'x')

f = open('pz_before_and_After_50.txt', 'a' )

for event_id in range (1, 10001, 1):

  if event_id != Event_id_120[event_id-1] :
    print('event not equal to array', event_id, Event_id_120[event_id-1])
    if event_id-1 == Event_id_120[event_id-1]:
      print('duplicate event id', event_id-1)

      Event_id_120 = np.delete(Event_id_120, event_id-1)
      Pz_120 = np.delete(Pz_120, event_id-1)

      if event_id-1 != Event_id_120[event_id-1] :
        print('insert', event_id, Event_id_120[event_id-1])
        Event_id_120 = np.insert(Event_id_120, event_id-1, event_id)
        Pz_120 = np.insert(Pz_120, event_id-1, 0)

      elif event_id-1 == Event_id_120[event_id-1]:
        print('duplicate event id', event_id-1)

        Event_id_120 = np.delete(Event_id_120, event_id-1)
        Pz_120 = np.delete(Pz_120, event_id-1)

        if event_id != Event_id_120[event_id-1] :
          print('insert', event_id, Event_id_120[event_id-1])
          Event_id_120 = np.insert(Event_id_120, event_id-1, event_id)
          Pz_120 = np.insert(Pz_120, event_id-1, 0)

        elif event_id == Event_id_120[event_id-1] :
          print(Event_id_120[event_id-1], Pz_120[event_id-1],  'match')

      elif event_id == Event_id_120[event_id-1] :
        print(Event_id_120[event_id-1], Pz_120[event_id-1],  'match')


    else :
      missing_positions = int(Event_id_120[event_id-1]) - event_id

      for insert in range (event_id, missing_positions+event_id, 1):
        print('insert',insert, event_id)
        Event_id_120 = np.insert(Event_id_120, insert-1, insert)
        Pz_120 = np.insert(Pz_120, insert-1, 0)

       # print(Event_id_120[insert-1], Pz_120[insert-1])
        #print(Event_id_120[0:insert+4])

  else :
    print(Event_id_120[event_id-1], Pz_120[event_id-1],  'match')
   # print(Event_id_120[0:event_id])


for event_id in range (1, 10001, 1):

  if event_id != Event_id_100[event_id-1] :
    print('event not equal to array', event_id, Event_id_100[event_id-1])
    if event_id-1 == Event_id_100[event_id-1]:
      print('duplicate event id', event_id-1)
      Event_id_100 = np.delete(Event_id_100, event_id-1)

      Pz_100 = np.delete(Pz_100, event_id-1)

      if event_id != Event_id_100[event_id-1] :
        print('insert', event_id, Event_id_100[event_id-1])
        Event_id_100 = np.insert(Event_id_100, event_id-1, event_id)
        Pz_100 = np.insert(Pz_100, event_id-1, 0)
      elif event_id == Event_id_100[event_id-1] :
        print(Event_id_100[event_id-1], Pz_100[event_id-1],  'match')

    else :
      missing_positions = int(Event_id_100[event_id-1]) - event_id

      for insert in range (event_id, missing_positions+event_id, 1):
        print('insert',insert, event_id)
        Event_id_100 = np.insert(Event_id_100, insert-1, insert)
        Pz_100 = np.insert(Pz_100, insert-1, 0)

       # print(Event_id_120[insert-1], Pz_120[insert-1])
        #print(Event_id_120[0:insert+4])

  else :
    print(Event_id_100[event_id-1], Pz_100[event_id-1],  'match')

for event_id in range (1, 10001, 1):
  f.write(str(event_id) + ' ' + str(Pz_100[event_id-1])+ ' ' + str(event_id) +' ' + str(Pz_120[event_id-1]) + '\n')


f.close()