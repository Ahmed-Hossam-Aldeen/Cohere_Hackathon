import cohere

def get_hashtag(input):
      co = cohere.Client('6arOhVPDx9BLudwjrgLJrS7Y2cg43LTBm8DU3DEI')
      output = [] 

      Hashtag_Model = co.generate(
            model='xlarge',
            max_tokens=10,
            num_generations = 3,
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
      output.append(Hashtag_Model.generations[2].text)
      print(output)
      return output

def get_mention(input):
    co = cohere.Client('6arOhVPDx9BLudwjrgLJrS7Y2cg43LTBm8DU3DEI')
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
                    interst: {input}
                    mention:''', 

        )
    output = Mention_Model.generations[0].text
    return(output)


def text_summary(input):
    
    co = cohere.Client('6arOhVPDx9BLudwjrgLJrS7Y2cg43LTBm8DU3DEI')

    Model_Summary = co.generate( 
        model='xlarge',
        max_tokens=100, 
        temperature=0.65,
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
                    Passage: {input}
                    Summary:''')

    summary = Model_Summary.generations[0].text
    print(summary)
    return summary