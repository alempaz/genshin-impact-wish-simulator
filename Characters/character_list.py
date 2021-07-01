import characters as c

# 5 Star Characters ------------------------------------------------------
diluc = c.SwordUser(name='Diluc', rarity='5 Star', element='Pyro', gender='Male', nation='Mondstadt', weapon='Sword',
                    description='As the wealthiest gentleman in Mondstadt, the ever-dapper Diluc always presents '
                                'himself as the epitome of perfection. But behind the courteous visage burns '
                                'a zealous soul that has sworn to protect Mondstadt at all costs, allowing him '
                                'to mercilessly vanquish all who threaten his city.', in_game=True, char_type='perma')

jean = c.SwordUser(name='Jean', rarity='5 Star', element='Anemo', gender='Female', nation='Mondstadt', weapon='Sword',
                   description='As the Acting Grand Master of the Knights, Jean has always been devoted to her duties '
                               'and maintaining peace in Mondstadt. She had taken precautions long before the onset of '
                               'Stormterror\'s assault, and she will guard Mondstadt with her life as always.',
                   in_game=True, char_type='perma')

keqing = c.SwordUser(name='Keqing', rarity='5 Star', element='Electro', gender='Female', nation='Mondstadt',
                     weapon='Sword', in_game=True, char_type='perma',
                     description='The Yuheng of the Liyue Qixing. Keqing has much to say about Rex Lapis\' unilateral '
                                 'approach to policymaking in Liyue — but in truth, gods admire skeptics such as her '
                                 'quite a lot. She firmly believes that humanity\'s future should be determined by '
                                 'humans themselves, and that they can even do better than the archons and adepti have '
                                 'done for them. In order to prove this, she works harder than anyone else.')

mona = c.CatalystUser(name='Mona', rarity='5 Star', element='Hydro', gender='Female', nation='Mondstadt',
                      weapon='Catalyst', in_game=True, char_type='perma',
                      description='A mysterious young astrologer who proclaims herself to be "Astrologist Mona Megistus'
                                  '," and who possesses abilities to match the title. Erudite, but prideful. Though '
                                  'she is often strapped for cash and lives a life of thrift, she is resolved to never '
                                  'use astrology for profit... It is this very resolution that has caused '
                                  'her to constantly fret about money.')

qiqi = c.SwordUser(name='Qiqi', rarity='5 Star', element='Cryo', gender='Female', nation='Mondstadt', weapon='Sword',
                   description='An apprentice and herb gatherer at Bubu Pharmacy. "Blessed" by the adepti with a body '
                               'that cannot die, this petite zombie cannot do anything without first giving herself '
                               'orders to do it. Qiqi\'s memory is like a sieve. Out of necessity, she always carries '
                               'around a notebook in which she writes anything important that she is sure to forget '
                               'later. But on her worst days, she even forgets to look at her notebook...',
                   in_game=True, char_type='perma')

# 5 Star Promotional Characters ------------------------------------------
albedo = c.SwordUser(name='Albedo', rarity='5 Star', element='Geo', gender='Male', nation='Liyue', weapon='Sword',
                     description='An alchemist based in Mondstadt, in the service of the Knights of Favonius.'
                                 '"Genius," "Kreideprinz," or "Captain of the Investigation Team"... Such titles and '
                                 'honors are of no consequence to him when there is so much more research to conduct.',
                     in_game=True, char_type='promo')

ganyu = c.BowUser(name='Ganyu', rarity='5 Star', element='Cryo', gender='Female', nation='Liyue', weapon='Bow',
                  description='The secretary to the Liyue Qixing. The blood of both human and illuminated beast flows '
                              'within her veins. Graceful and quiet by nature, yet the gentle disposition of qilin '
                              'sees not even the slightest conflict with even the most arduous of workloads.',
                  in_game=True, char_type='promo')

hu_tao = c.PolearmUser(name='Hu Tao', rarity='5 Star', element='Pyro', gender='Female', nation='Liyue',
                       weapon='Polearm', char_type='promo',
                       description='Hu Tao is the 77th Director of the Wangsheng Funeral Parlor, a person vital to '
                                   'managing Liyue\'s funerary affairs. She does her utmost to flawlessly carry out a '
                                   'person\'s last rites and preserve the world\'s balance of yin and yang. Aside from '
                                   'this, she is also a talented poet whose many "masterpieces" have passed around '
                                   'Liyue\'s populace by word of mouth.', in_game=True)

klee = c.CatalystUser(name='Klee', rarity='5 Star', element='Pyro', gender='Female', nation='Mondstadt',
                      weapon='Catalyst', in_game=True, char_type='promo',
                      description='Knights of Favonius Spark Knight! Forever with a bang and a flash! —And then '
                                  'disappearing from the stern gaze of Acting Grand Master Jean. Sure, time in '
                                  'solitary confinement gives lots of time to think about new gunpowder formulas...'
                                  'But it\'d still be better to not be in solitary in the first place.')

tartaglia = c.BowUser(name='Tartaglia', rarity='5 Star', element='Hydro', gender='Male', nation='Snezhnaya', weapon='',
                      description='Meet Tartaglia — the cunning Snezhnayan whose unpredictable personality keeps '
                                  'people guessing his every move. Don\'t be under any illusion as to what he might be '
                                  'thinking or what his intentions are. Just remember this: Behind that innocent, '
                                  'childlike exterior lies a finely honed instrument of war.',
                      in_game=True, char_type='promo')

venti = c.BowUser(name='Venti', rarity='5 Star', element='Anemo', gender='Male', nation='Mondstadt', weapon='Bow',
                  description='A bard that seems to have arrived on some unknown wind - sometimes sings songs as old '
                              'as the hills, and other times sings poems fresh and new. Likes apples and lively places '
                              'but is not a fan of cheese or anything sticky. When using his Anemo power to control '
                              'the wind, it often appears as feathers, as he\'s fond of that which appears '
                              'light and breezy.', in_game=True, char_type='promo')

xiao = c.PolearmUser(name='Xiao', rarity='5 Star', element='Anemo', gender='Male', nation='Liyue', weapon='Polearm',
                     description='One of the "Mighty and Illuminated Adepti" guarding Liyue, also heralded as the '
                                 '"Guardian Yaksha." Despite his appearance as a young man, occasional legends '
                                 'about him have been documented in ancient books. He is especially fond of '
                                 'Wangshu Inn\'s Almond Tofu. The reason is that the dish tastes just like the '
                                 '"dreams" he used to devour.', in_game=True, char_type='promo')

zhongli = c.PolearmUser(name='Zhongli', rarity='5 Star', element='Geo', gender='Male', nation='Liyue', weapon='Polearm',
                        description='Wangsheng Funeral Parlor\'s mysterious consultant. Handsome, elegant, and '
                                    'surpassingly learned.Though no one knows where Zhongli is from, he is a master of '
                                    'courtesy and rules. From his seat at Wangsheng Funeral Parlor, he performs all '
                                    'manner of rituals.', in_game=True, char_type='promo')


eula = c.ClaymoreUser(name='Eula', rarity='5 Star', element='Cryo', gender='Female', nation='Mondstadt',
                      weapon='Claymore',
                      description='The Spindrift Knight, a scion of the old aristocracy, and the Captain of the '
                                  'Knights of Favonius Reconnaissance Company. The reason for which a '
                                  'descendant of the ancient nobles might join the Knights remains a great '
                                  'mystery in Mondstadt to this very day.', in_game=True, char_type='promo')

kazuha = c.SwordUser(name='Kaedehara Kazuha', rarity='5 Star', element='Anemo', gender='Male', nation='Inazuma',
                      weapon='Sword',
                      description='A wandering samurai from Inazuma who is currently with Liyue\'s Crux Fleet. '
                                  'A gentle and carefree soul whose heart hides a great many burdens from the past.'
                     , in_game=True, char_type='promo')

# Upcoming Characters
ayaka = c.SwordUser(name='Kamisato Ayaka', rarity='5 Star', element='Cryo', gender='Female', nation='Inazuma',
                    weapon='Sword',
                    description='The princess of the Kamisato House. She occasionally practices '
                                'swordsmanship so that she can pass time by slicing every falling '
                                'snowflake floating around her on a snowy day.', in_game=False, char_type='promo')

yoimiya = c.BowUser(name='Yoimiya', rarity='5 Star', element='Pyro', gender='Female', nation='Inazuma',
                        weapon='Bow', description='Owner of Naganohara Fireworks. Known as "Queen of the '
                        'Summer Festival, she excels in her craft of creating fireworks that symbolize people\'s '
                        'hopes and dreams.', in_game=False, char_type='promo',)

# 4 Star Characters -----------------------------------------------------
amber = c.BowUser(name='Amber', rarity='4 Star', element='Pyro', gender='Female', nation='Mondstadt', weapon='Bow',
                  description='A perky, straightforward girl, who is also the only Outrider of the Knights of '
                              'Favonius. Her amazing mastery of the glider has made her a three-time winner of the '
                              'Gliding Championship in Mondstadt. As a rising star within the Knights of Favonius, '
                              'Amber is always ready for any challenging tasks.', in_game=True, char_type='perma')

barbara = c.CatalystUser(name='Barbara', rarity='4 Star', element='Hydro', gender='Female', nation='Mondstadt',
                         description='The Deaconess of the Favonius Church and a shining starlet '
                                     'adored by all. Although the concept of a starlet is rather novel in a city of '
                                     'bards, the people of Mondstadt love Barbara nonetheless. "I owe everything to '
                                     'the city\'s spirit of freedom" — Barbara, regarding her popularity.',
                         weapon='Catalyst', in_game=True, char_type='perma')

beidou = c.ClaymoreUser(name='Beidou', rarity='4 Star', element='Hydro', gender='Female', nation='Liyue',
                        weapon='Claymore', in_game=True, char_type='perma',
                        description='Captain of the Crux, with quite the reputation in Liyue. There are those who say '
                                    'she can split mountains and part the sea. Others say she draws lightning through '
                                    'her sword. Some say that even the mightiest of sea beasts are no match for her.')

bennet = c.SwordUser(name='Bennet', rarity='4 Star', element='Pyro', gender='Male', nation='Mondstadt',
                     weapon='Sword', in_game=True, char_type='perma',
                     description='The few young adventurers that the Mondstadt Adventurers\' Guild has always found '
                                 'themselves tangled up in baffling bouts of bad luck. He is the only active member of '
                                 'his own adventure group, known as "Benny\'s Adventure Team," after all the other '
                                 'members decided to "take leave" following a series of unfortunate incidents. '
                                 'As a result, the team is currently on the verge of being dissolved.')

chongyun = c.ClaymoreUser(name='Chongyun', rarity='4 Star', element='Cryo', gender='Male', nation='Liyue',
                          weapon='Claymore', in_game=True, char_type='perma',
                          description='An exorcist who roams the land with Liyue as his base of operations, evil '
                                      'spirits fleeing wherever he goes. As the heir to a clan of exorcists, he has '
                                      'always possessed abilities superior to most. However, these abilities are not '
                                      'the result of training, but of an inborn trait - a pure yang spirit.')

diona = c.BowUser(name='Diona', rarity='4 Star', element='Cryo', gender='Female', nation='Mondstadt', weapon='Bow',
                  description='The incredibly popular bartender of the Cat\'s Tail tavern, rising star of Mondstadt\'s '
                              'wine industry, and the greatest challenger to its traditional powerhouses. A feisty '
                              'feline young lady from Springvale, any drink mixed by Diona\'s hand tastes delicious '
                              'beyond belief. Yet given her extreme distaste for alcohol, is her talent a blessing or '
                              'a curse?', in_game=True, char_type='perma')

fischl = c.BowUser(name='Fischl', rarity='4 Star', element='Electro', gender='Female', nation='Mondstadt', weapon='Bow',
                   description='A mysterious girl who calls herself "Prinzessin der Verurteilung" and travels with a '
                               'night raven named Oz. Currently serves as an investigator in the Adventurers\' Guild. '
                               'Through her unique abilities, eccentric character, and (while she would never admit it '
                               'herself) hard work, Fischl has become a rising star among the Adventurers\' Guild\'s '
                               'investigators, earning the recognition of all.', in_game=True, char_type='perma')

kaeya = c.SwordUser(name='Kaeya', rarity='4 Star', element='Cryo', gender='Male', nation='Mondstadt', weapon='Sword',
                    description='In the Knights of Favonius, Kaeya is the most trusted aide for the Acting Grand '
                                'Master Jean. You can always count on him to solve any intractable problems. '
                                'Everyone in Mondstadt loves Kaeya, but no one knows what secrets this witty, '
                                'charming knight has...', in_game=True, char_type='perma')

lisa = c.CatalystUser(name='Lisa', rarity='4 Star', element='Electro', gender='Female', nation='Mondstadt',
                      weapon='Catalyst', in_game=True, char_type='perma',
                      description='She is an intellectual witch who can never get enough naps. As the Librarian of the '
                                  'Knights of Favonius, Lisa is smart in that she always knows exactly what to do with '
                                  'whatever troubles her. As much as she loves her sleep, she still manages to keep '
                                  'everything under control in a calm, composed manner.')

ningguang = c.CatalystUser(name='Ningguang', rarity='4 Star', element='Geo', gender='Female', nation='Liyue',
                           weapon='Catalyst', in_game=True, char_type='perma',
                           description='Owner of the Jade Chamber in the skies above Liyue, there are stories abound '
                                       'about Ningguang, with her elegance and mysterious smile. As a Tianquan of the '
                                       'Liyue Qixing, not only does she embody law and order, she also represents '
                                       'fortune and wit.')

noelle = c.ClaymoreUser(name='Noelle', rarity='4 Star', element='Geo', gender='Female', nation='Mondstadt',
                        weapon='Claymore', in_game=True, char_type='perma',
                        description='Like most of Mondstadt\'s young people, Noelle always dreamed of being a knight '
                                    'of Favonius when she grew up. She may not have what it takes to be a knight just '
                                    'yet, but she is learning. Working as a maid at the Knights\' headquarters, '
                                    'she is constantly taking notes on what constitutes knightly speech, knightly '
                                    'conduct, and knightly customs. She holds firm to her belief that one day she '
                                    'will join their ranks - she just needs to keep trying her hardest at everything '
                                    'she does.')

razor = c.ClaymoreUser(name='Razor', rarity='4 Star', element='Electro', gender='Male', nation='Mondstadt',
                       weapon='Claymore', in_game=True, char_type='perma',
                       description='Some say he is an orphan raised by wolves. Others say he is a wolf spirit in human '
                                   'form. He is most at home in the wild, fighting with claw and thunder. To this day '
                                   'the wolf boy can be found prowling the forest, where he and his wolf pack hunt to '
                                   'survive using nothing more than their animal instincts.')

rosaria = c.PolearmUser(name='Rosaria', rarity='4 Star', element='Cryo', gender='Female', nation='Mondstadt',
                        weapon='Polearm', in_game=True, char_type='promo',
                        description='Rosaria, a sister in Mondstadt\'s Church of Favonius. A sister of the church, '
                                    'though you wouldn\'t know it if it weren\'t for her attire. An unusual woman with '
                                    'sharp, piercing words and a cold manner. Her movements are unpredictable. She '
                                    'often leaves without notifying anyone. She acts with some kind of purpose, but '
                                    'others don\'t seem to know exactly what she stands for...')

sucrose = c.CatalystUser(name='Sucrose', rarity='4 Star', element='Anemo', gender='Female', nation='Mondstadt',
                         weapon='Catalyst', in_game=True, char_type='perma',
                         description='An alchemist with an insatiable curiosity towards the world and everything in '
                                     'it. Attached to the Knights of Favonius as an assistant to Albedo, her area of '
                                     'focus is "bio-alchemy." She strives to enrich the world by transforming living '
                                     'things with the power of alchemy. Granted, the products of her research '
                                     'sometimes prove to be more weird than wonderful — but on the whole, she has '
                                     'made monumental contributions to the field of bio-alchemy.')

xianglin = c.PolearmUser(name='Xianglin', rarity='4 Star', element='Pyro', gender='Female', nation='Liyue',
                         weapon='Polearm', in_game=True, char_type='perma',
                         description='The Head Chef at the Wanmin Restaurant and also a waitress there, Xiangling is '
                                     'extremely passionate about cooking and excels at her signature hot and spicy '
                                     'dishes. Though still young, Xiangling is a true master of the culinary arts '
                                     'with all the skills of a kitchen veteran. She enjoys a good reputation among '
                                     'the hearty eaters at Chihu Rock.')

xingqiu = c.SwordUser(name='Xingqiu', rarity='4 Star', element='Hydro', gender='Male', nation='Liyue', weapon='Sword',
                      description='The second son of the Feiyun Commerce Guild, Xingqiu has had a reputation for '
                                   'being studious and polite ever since he was a young child. But there is another '
                                   'side to the mild-mannered Xingqiu everyone knows. A daring, adventurous and '
                                   'much more mischievous side...', in_game=True, char_type='perma')

xinyan = c.ClaymoreUser(name='Xinyan', rarity='4 Star', element='Pyro', gender='Female', nation='Liyue',
                        weapon='Claymore', in_game=True, char_type='perma',
                        description='Rock \'n\' roll is an avant-garde art in Liyue Harbor and Xinyan is the pioneer '
                                    'in this field. She rebels against ossified prejudices, using her music and '
                                    'passionate singing to awaken dazed souls fatigued by worldly matters. If you '
                                    'get the chance, do not miss out on her next performance!')

yanfei = c.CatalystUser(name='Yanfei', rarity='4 Star', element='Pyro', gender='Female', nation='Liyue',
                        weapon='Catalyst', in_game=True, char_type='perma',
                        description='A well-known legal adviser active in Liyue Harbor. A briliant young lady '
                                    'in whose veins runs the blood of an illuminated beast.')

# Upcoming Characters
sayu = c.ClaymoreUser(name='Sayu', rarity='4 Star', element='Anemo', gender='Female', nation='Inazuma',
                        weapon='Claymore', in_game=False, char_type='perma',
                        description='A pint-sized ninja attached to the Shiyuumatsu-Ban, '
                                    'who always seems sleep-deprived.')


