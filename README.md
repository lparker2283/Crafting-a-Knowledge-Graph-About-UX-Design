# Crafting-a-Knowledge-Graph-About-UX-Design

**Goal**: Build a knowledge graph based on several scraped articles searched using the keyword "UX Design Interview" using the REBEL model for knowledge graph construction. This is a prototype for a pre-interview project idea that I had for instructional design; to scrape high-quality articles about interview prep for certain roles to construct a graph of the required skills, interview rounds, and strategies for success. My thouht was that knowledge graph construction based on large volumes of text data could help IDs at interview prep companies get a big-picture sense of what interviewees are being told in terms of what to expect and how to ace interviews. IDs can use this info to begin to construct course outlines, and share their findings with subject matter experts who can validate the knowledge graph - and point out critical pieces that are missing. Armed with this knowledge, IDs can build better curriculum, and marketers/biz office workers will know what keywords to target / how to position new courses to demonstrate maximum value to job seekers.

Read the paper on the REBEL model [here](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf) - it's simple, robust, and it utilizes end-to-end relation extraction; eliminating the need to tackle entity recognition and relation classification separately. I used Fabiano Chuisano's excellent [tutorial](https://medium.com/nlplanet/building-a-knowledge-base-from-texts-a-full-practical-example-8dbbffb912fa) and made minor changes. 

**Results**: My knowledge graph comprises information from the following articles:
- [Mastering UX/CX Design: Privacy Meets Omnichannel Harmony](https://www.cmswire.com/customer-experience/mastering-uxcx-design-privacy-meets-omnichannel-harmony/)
- [Interview with a Leading UX Designer Agency in San Francisco](https://southernafrican.news/2023/04/26/interview-with-a-leading-ux-designer-agency-in-san-francisco/)
- [In Conversation with Aayushi Bhotica, Lead Designer, Wadhwani AI, on the use of Design for Social Impact](https://www.cxotoday.com/interviews/in-conversation-with-ayushi-bhotica-lead-designer-wadhwani-ai-on-the-use-of-design-for-social-impact/)
- [A Designer’s Survival Guide to Economic Uncertainty](https://builtin.com/design-ux/recession-proof-designer)
- [Big Impact on a Small Budget: 6 Cost-Effective UX Research Techniques for Early-Stage Founders](https://entrepreneurshandbook.co/big-impact-on-a-small-budget-6-cost-effective-ux-research-techniques-for-early-stage-founders-e69c27878ba0)

The resultant graph correctly identified that UX design is: 
- closely related to principles of design and user experience, which affect to customers' quality of life
- related (operationally) to product management and customer experience
- makes use of tools/methods like user research, wireframing, and problem solving

However, few articles went into this knowledge graph, they were of mixed length (one promising looking article exceeded the length limit set by REBEL) and quality. I suspect better results could be achieved by curating a list of input articles on the frontend rather than relying on recently articles Google News has access to that contain a given keyword. 
