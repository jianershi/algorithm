class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        # write your code here

        map = '0123456789bcdefghjkmnpqrstuvwxyz'
        char_to_index = {map[i]:i for i in range(len(map))}

        precision = len(geohash)

        geo_hash_decimal_index = []
        for i in geohash:
            geo_hash_decimal_index.append(char_to_index[i])

        #this steps convert geohash to a long binary string
        geohash_to_binary = ""
        for dec_char in geo_hash_decimal_index:
            #convert decimal to 5 digit binary.
            binary_char = "" #end in lowest big in the front
            while dec_char > 0:
                binary_char += str(dec_char % 2)
                dec_char = dec_char // 2
            #append 0 (to the highest big, but this is still reversed, so append it)
            num_0_to_append = 5 - len(binary_char)
            for _ in range(num_0_to_append):
                binary_char += '0'
            #reverse the binary string to the correct orer and append to the big binary string
            geohash_to_binary += binary_char[::-1]

        # this part break it to 2 strings, 1 for longtitude, 1 for latitude
        longitude_binary = ""
        latitude_binary = ""
        append_longitude = True
        for bin in geohash_to_binary:
            if append_longitude:
                longitude_binary += bin
            else:
                latitude_binary += bin
            append_longitude = not append_longitude

        longitude = self.binary_search(-180, 180, longitude_binary)
        latitude = self.binary_search(-90, 90, latitude_binary)

        return (latitude, longitude)

    def binary_search(self, start, end, binary_string):
        for c_i in binary_string:
            mid = (start + end) / 2.0
            if int(c_i) == 1:
                start = mid
            else:
                end = mid
        return (start + end) / 2.0

s = GeoHash()
print(s.decode("wx4g0s8q3jf9"))
