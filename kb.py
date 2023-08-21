import wikipedia  # Add this line to import the wikipedia module

# Define a Knowledge Base class to store entities, relations, and sources
class KB():
    def __init__(self):
        # Initialize empty lists and dictionaries to store data
        self.relations = [] # List to store relation data
        self.entities = {} # Dictionary to store entity data
        self.sources = {}  # Dictionary to store source (article) data

    # Merge the data from another KB instance into this one
    def merge_with_kb(self, kb2):
        for r in kb2.relations:
            article_url = list(r["meta"].keys())[0]
            source_data = kb2.sources[article_url]
            self.add_relation(r, source_data["article_title"], source_data["article_publish_date"])

    # Check if 2 relations are equal
    def are_relations_equal(self, r1, r2):
        return all(r1[attr] == r2[attr] for attr in ["head", "type", "tail"])
    
    # Check if a relation already exists in the kb
    def exists_relation(self, r1):
        return any(self.are_relations_equal(r1, r2) for r2 in self.relations)

    # Merge relations with the same content but from different sources
    def merge_relations(self, r2):
        r1 = [r for r in self.relations
              if self.are_relations_equal(r2, r)][0]
        
        # if different article
        article_url = list(r2["meta"].keys())[0]
        if article_url not in r1["meta"]:
            r1["meta"][article_url] = r2["meta"][article_url]
        
        # if existing article
        else: 
            spans_to_add = [span for span in r2["meta"][article_url]["spans"]
                            if span not in r1["meta"][article_url]["spans"]]
            r1["meta"][article_url]["spans"] += spans_to_add

    # Fetch Wikipedia data for a candidate entity
    def get_wikipedia_data(self, candidate_entity):
        try:
            page = wikipedia.page(candidate_entity, auto_suggest=False)
            entity_data = {
                "title": page.title,
                "url": page.url,
                "summary": page.summary
            }
            return entity_data
        except:
            return None

    # Add an entity to the KB
    def add_entity(self, e):
        self.entities[e["title"]] = {k: v for k, v in e.items() if k != "title"}

     # Add a relation to the KB
    def add_relation(self, r, article_title, article_publish_date):
        candidate_entities = [r["head"], r["tail"]]
        entities = [self.get_wikipedia_data(ent) for ent in candidate_entities]

        # if one entity does not exist, stop
        if any(ent is None for ent in entities):
            return

        # manage new entities
        for e in entities:
            self.add_entity(e)

        # rename relation entities with their wikipedia titles
        r["head"] = entities[0]["title"]
        r["tail"] = entities[1]["title"]

        # add source if not in kb
        article_url = list(r["meta"].keys())[0]
        if article_url not in self.sources: 
            self.sources[article_url] = {
                "article_title": article_title,
                "article_publish_date": article_publish_date
            }

        # manage new relation
        if not self.exists_relation(r):
           self.relations.append(r)
        else:
           self.merge_relations(r)

    # Print the content of the KB
    def print(self):
        print("Entities:")
        for e in self.entities.items():
            print(f" {e}")
        print("Relations:")
        relation_count = len(self.relations)
        print(f"  Total Relations: {relation_count}")
        for r in self.relations:
            print(f"  {r}")
        print("Sources:")
        for s in self.sources.items():
            print(f" {s}")
    
    # Merge multiple knowledge bases for separate articles together
    def merge_with_kb(self, kb2):
        for r in kb2.relations:
            article_url = list(r["meta"].keys())[0]
            source_data = kb2.sources[article_url]
            self.add_relation(r, source_data["article_title"],
                              source_data["article_publish_date"])
