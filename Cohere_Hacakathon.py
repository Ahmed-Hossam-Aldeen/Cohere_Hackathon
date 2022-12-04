import cohere
import config

co = cohere.Client("6arOhVPDx9BLudwjrgLJrS7Y2cg43LTBm8DU3DEI")

def get_hashtag(input):
      
      output = [] 

      Hashtag_Model = co.generate(
            model='xlarge',
            max_tokens=10,
            num_generations = 2,
            temperature= 0.6,
            k=0,
            p=0.9,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods='NONE',

            prompt=f'''
                        Post: Why are there no country songs about software engineering
                        Hashtag: software-engineering
                        --
                        Post: Your soulmate is in the WeWork you decided not to go to
                        Hashtag: wework
                        --
                        Post: If shes talking to you once a day im sorry bro thats not flirting that standup
                        Hashtag: standup
                        --
                        Post: Going to unmute at the end of the Zoom meeting to say bye and realizing you were actually unmuted the whole call
                        Hashtag: zoom
                        --
                        Post: {input}
                        Hashtag:''', 

      )
      output.append(Hashtag_Model.generations[0].text)
      output.append(Hashtag_Model.generations[1].text)
      print(output)
      return output

def get_mention(input):

    Mention_Model = co.generate(
        model='xlarge',
        max_tokens=10,
        num_generations = 1,
        temperature= 0.6,
        k=0,
        p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE',

        prompt=f'''
                    interest: Footbal
                    mention: Messi
                    --
                    interest: tech
                    mention: Elon Musk
                    --
                    interest: Food
                    mention: Gordon Ramsy
                    --
                    interest: rap
                    mention: Snoop Dogg
                    --
                    interest: movies
                    mention: Netflix
                    --
                    interst: {input}
                    mention:''', 

        )
    output = Mention_Model.generations[0].text
    return(output)


def text_summary(input):
    

    Model_Summary = co.generate( 
        model='xlarge',
        max_tokens=100,
        return_likelihoods = 'GENERATION', 
        num_generations= 5,
        temperature=0.7,
        stop_sequences=["--"],
        prompt = f'''
                    Passage: Johannes Gutenberg (1398:1468) was a German goldsmith and publisher who introduced printing to Europe. His introduction of mechanical movable type printing to Europe started the Printing Revolution and is widely regarded as the most important event of the modern period. It played a key role in the scientific revolution and laid the basis for the modern knowledge-based economy and the spread of learning to the masses.
                    Gutenberg many contributions to printing are: the invention of a process for mass-producing movable type, the use of oil-based ink for printing books, adjustable molds, and the use of a wooden printing press. His truly epochal invention was the combination of these elements into a practical system that allowed the mass production of printed books and was economically viable for printers and readers alike.
                    In Renaissance Europe, the arrival of mechanical movable type printing introduced the era of mass communication which permanently altered the structure of society. The relatively unrestricted circulation of information—including revolutionary ideas—transcended borders, and captured the masses in the Reformation. The sharp increase in literacy broke the monopoly of the literate elite on education and learning and bolstered the emerging middle class.
                    Summary: The German Johannes Gutenberg introduced printing in Europe. His invention had a decisive contribution in spread of mass-learning and in building the basis of the modern society.
                    Gutenberg major invention was a practical system permitting the mass production of printed books. The printed books allowed open circulation of information, and prepared the evolution of society from to the contemporary knowledge-based economy.
                    --
                    Passage: The first questions we should ask ourselves or when starting a job in the institution we work for are “What is the problem we are trying to solve? / What is our goal? Or what will be the contribution of this work?” should be. These questions are invaluable whatever our job is data analytics, data science, application development or project management.These questions are very important both for us to choose the right technique and for us to make the right deductions and develop our competencies by owning the work. Also it is important in choosing the right technique because the method changes according to the purpose and goal of the work we will do. In this project, we actually experienced this. Using the same data, we brought solutions to two different problems/targets with two different techniques.
                    Summary: These questions are very important both for us to choose the right technique and for us to make the right deductions and develop our competencies by owning the work.
                    --
                    Passage: A long time ago, there lived a king in a faraway land. He was very weak and sick due to laziness. He consulted his doctor. The doctor was wiser than the king and knew that it was not medicine but healthy exercise that the king needed. The doctor, therefore, brought two heavy clubs of strange wood to the king and said that these clubs contained medicine to cure him. He asked the king to hold them by the handles and turn them until his hands were moist from the exercise. Moisture, the doctor said, would make the medicine work. He obeys the doctors advice and can be seen in the open air at certain times every day, working manually with his magic clubs. His muscles grow stronger, his health improves, and he appreciates the wonderful medicine of his club and the knowledge of his physician.
                    Summary: A king was suffering from weakness and illness due to his laziness. He consulted his doctor. The physician saw that the king needed healthy exercise, not medicine. He gave the king two heavy bundles of a strange wood and advised him to swing regularly in the open air until his body began to sweat. Raja followed the doctors advice. His health has improved. He appreciated the doctors treatment of his disease.
                    --
                    Passage: King Midas was fond of gold more than anything else in the world. He treasured his royal crown because it was made of that precious metal. If she loved anything good or half as good, it was a little girl who played around her father’s feet so happily. But the more Midas loved his daughter, the more he desired wealth.He thought the foolish man that he was, the best thing he could possibly do for his beloved child was to bestow upon him the great pile of yellow shiny coins that had been collected since the creation of the world. So he gave all his thoughts and all his time to this one cause. If ever he looked for a moment at the golden clouds of sunset, he wished they were gold and that they could be safely squeezed into his strong box.
                    Summary: King Midas loved gold more than earthly things. The royal crown was precious to him because it was made of gold. But he loved his daughter dearly and would have paid for her in gold. He wanted to give her all the gold in the world. He even wished the golden clouds of the sunset to be true gold so that he could hold them and store them in an iron safe.
                    --
                    Passage: {input}
                    Summary:''')

    # Get list of generations
    gens = []
    likelihoods = []
    for gen in Model_Summary.generations:
        gens.append(gen.text)
        sum_likelihood = 0
        for t in gen.token_likelihoods:
            sum_likelihood += t.likelihood
        # Get sum of likelihoods
        likelihoods.append(sum_likelihood)

    print(likelihoods)    
    max_likelihood = max(likelihoods)
    max_index = likelihoods.index(max_likelihood)
    print(max_index)

    summary = Model_Summary.generations[max_index].text
    print(summary)
    return summary
