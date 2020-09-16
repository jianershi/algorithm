class GeoHash:
    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        # write your code here

        map = '0123456789bcdefghjkmnpqrstuvwxyz'

        #convert precision to steps allowed on binary search for longitude and latitude
        steps_long = (precision % 2) * 3 + (precision // 2) * 5
        steps_lat = (precision % 2) * 2 + (precision // 2) * 5

        long_binary = self.binary_search(-180, 180, longitude, steps_long)
        lat_binary = self.binary_search(-90, 90, latitude, steps_lat)

        print ("".join([str(x) for x in long_binary]))

        result_index = [0] * precision

        long_i = 0
        lat_i = 0
        append_longitude = True #flipping a switch to know which array to append

        for i in range(precision):
            current_precision = []
            for _ in range(5): #process 5 digits at a time, so that i can convert to decimal index
                if append_longitude:
                    current_precision.append(long_binary[long_i])
                    long_i += 1
                else:
                    current_precision.append(lat_binary[lat_i])
                    lat_i += 1
                append_longitude = not append_longitude
            for j in range(5): #convert binary to decimal
                result_index[i] += current_precision[4 - j] * 2**j
                # result_index[i] = result_index[i] << 1 | current_precision[j] #bitwise or and shift to left, both will work

        #using result_index to find the char in the map
        result_string = ""
        for k in range(len(result_index)):
            result_string += map[result_index[k]]
        return result_string

    """
    binary_search
    @param: start, end, target, steps allwowed
    @return: an list of binary [1, 0, 1, 0, 1, 0]
    """
    def binary_search(self, start, end, target, steps):
        result = []
        for _ in range(steps):
            mid = (start + end) / 2.0
            if mid < target:
                start = mid
                result.append(1)
            else:
                end = mid
                result.append(0)
        return result

s = GeoHash()
print(s.encode(39.92816697, 116.38954991, 12))
