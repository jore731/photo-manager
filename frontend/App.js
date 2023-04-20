import React from "react";
import {
  StyleSheet,
  Text,
  SafeAreaView,
  ScrollView,
  StatusBar,
  Image,
  FlatList,
} from "react-native";
import uuid from "react-native-uuid";

let DATA = [];

for (let index = 0; index < 1000; index++) {
  DATA.push({
    id: uuid.v4(),
    uri: "https://reactnative.dev/img/tiny_logo.png",
  });
}

const Item = ({ item_uri }) => (
  <Image style={styles.logo} source={{ uri: item_uri }} />
);

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        data={DATA}
        numColumns={2}
        renderItem={({ item }) => <Item item_uri={item.uri} />}
        keyExtractor={(item) => item.id}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: StatusBar.currentHeight,
  },
  scrollView: {
    backgroundColor: "#DDDDDD",
    marginHorizontal: 0,
  },
  text: {
    fontSize: 42,
  },
  logo: {
    width: "50%",
    height: undefined,
    aspectRatio: 1,
  },
});

export default App;
