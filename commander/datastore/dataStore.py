from flask.ext.cache import Cache

class DataStoreError(Exception):
    pass

class DataStore:
    def __init__(self, app):
        self.app = app
        self.cache = Cache(app, config{'CACHE_TYPE':'simple'})

    # generic methods

    def set(self, key, value):
        '''
        Sets value to a key
        '''
        self.cache.set(key, value)

    def add(self, listKey, value):
        '''
        Adds a item to a list
        '''
        aux = self.cache.get(listKey)
        aux.append(value)
        self.cache.set(listKey, aux)

    def get(self, key):
        '''
        Gets a value from it key
        '''
        return self.cache.get(key)

    def delete(self, key):
        '''
        Deletes a key-value pair
        '''
        self.cache.delete(key)


    def delete(self, listKey, element):
        '''
        Deletes a element in a list
        '''
        aux = self.cache.get(listKey)
        aux.remove(element)
        self.cache.set(listKey, aux)

    def checkIfExists(self, key):
        '''
        Checks if a key is defined
        '''
        if self.cache.get(key) == None:
            return False
        return True


    def checkIfExists(self, listKey, element):
        '''
        Checks if a element exists in a list
        '''
        aux = self.cache.get(listKey)
        return element in aux

    def raiseIfDifferent(self, a, b):
        if a != b:
            raise DataStoreError('Error: \'' + a + '\' and \'' + b + '\' are different.')

    def raiseIfNotExists(self, key):
        if self.checkIfExists(key) == False
            raise DataStoreError('Error: \'' + key + '\' does not exists.')


    # contexts methods

    def addContext(self, contextToken, context):
        '''
        Adds a context
        '''
        # check if the token provided is the same that in the context entity.
        self.raiseIfDifferent(contextToken, context['token'])
        # add token to the list of contexts
        self.add('contexts', contextToken)
        # add the context entity
        self.set(contextToken, context)

    def delContext(self, contextToken):
        '''
        Deletes a context
        '''
        # delete from list of tokens
        self.delete('contexts', contextToken)
        # delete entity
        self.delete(contextToken)

    def updateContext(self, contextToken, context):
        '''
        Updates a context with a new value
        '''
        # check if the token provided is the same that in the context entity.
        self.raiseIfDifferent(contextToken, context['token'])
        # set context entity
        self.set(contextToken, context)

    def getContext(self, contextToken):
        '''
        Gets the context entity
        '''
        self.get(contextToken)


    # images methods

    def addImage(self, imageToken, image, contextToken):
        '''
        Adds an image to a context
        '''
        # check if the token provided is the same that in the image entity.
        self.raiseIfDifferent(imageToken, image['token'])
        # get context
        context = self.getContext(contextToken)
        # add to the list of images in the context
        context['images'].append(imageToken)
        self.updateContext(context['token'], context)
        # add the image entity
        self.set(imageToken, image)

    def delImage(self, imageToken):
        '''
        Deletes an image
        '''
        # get image
        image = self.getImage(imageToken)
        # get context
        context = self.getContext(image['contextToken'])
        # remove reference to image in context
        context['images'].remove(imageToken)
        # remove image entity
        self.delete(imageToken)

    def updateImage(self, imageToken, image):
        '''
        Updates an image with a new value
        '''
        # check if the token provided is the same that in the image entity.
        self.raiseIfDifferent(imageToken, image['token'])
        # set entity
        self.raiseIfNotExists(imageToken)
        self.set(contextToken, context)

    def getImage(self, imageToken):
        '''
        Gets the image entity
        '''
        self.get(imageToken)


    # cluster methods

    def addCluster(self, clusterToken, cluster):
        '''
        Adds a cluster
        '''
        # check if the token provided is the same that in the cluster entity.
        self.raiseIfDifferent(clusterToken, cluster['token'])
        # add to the list of clusters
        self.add('clusters', clusterToken)
        # add the cluster entity
        self.set(clusterToken, cluster)

    def delCluster(self, clusterToken):
        '''
        Deletes a cluster
        '''
        # delete from list of clusters
        self.delete('clusters', clusterToken)
        # delete entity
        self.delete(clusterToken)

    def updateCluster(self, clusterToken, cluster):
        '''
        Updates a cluster with a new value
        '''
        # check if the token provided is the same that in the cluster entity.
        self.raiseIfDifferent(clusterToken, cluster['token'])
        # set cluster entity
        self.set(clusterToken, cluster)

    def getCluster(self, clusterToken):
        '''
        Gets the cluster entity
        '''
        self.get(clusterToken)


    # compositions methods

    def addComposition(self, compositionToken, composition):
        '''
        Adds a composition
        '''
        # check if the token provided is the same that in the composition entity.
        self.raiseIfDifferent(compositionToken, composition['token'])
        # add to the list of compositions
        self.add('compositions', compositionToken)
        # add the composition entity
        self.set(compositionToken, composition)

    def delComposition(self, compositionToken):
        '''
        Deletes a composition
        '''
        # delete from list of compositions
        self.delete('compositions', compositionToken)
        # delete entity
        self.delete(compositionToken)

    def updateComposition(self, compositionToken, composition):
        '''
        Updates a composition with a new value
        '''
        # check if the token provided is the same that in the composition entity.
        self.raiseIfDifferent(compositionToken, composition['token'])
        # set composition entity
        self.set(compositionToken, composition)

    def getComposition(self, compositionToken):
        '''
        Gets the composition entity
        '''
        self.get(compositionToken)
