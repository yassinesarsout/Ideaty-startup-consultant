
def create_prompt(business_domain):
    prompt = f'''generate 4 business ideas for this domain {business_domain}
generate the Business Name, Short Description, Target Audience and Potential Revenue Streams 
you should return a title like business ideas for said domain then the ideas devided with the format i gave you and nothing else 
'''
    return prompt

