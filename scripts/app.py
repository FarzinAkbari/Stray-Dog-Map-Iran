import pandas as pd
import folium

def load_data(file_path):
    return pd.read_csv(file_path)

def add_dog_location(data, latitude, longitude, description):
    new_entry = {'latitude': latitude, 'longitude': longitude, 'description': description}
    data = data.append(new_entry, ignore_index=True)
    return data

def save_data(data, file_path):
    data.to_csv(file_path, index=False)

def generate_map(data, map_file):
    map_ = folium.Map(location=[32.0, 53.0], zoom_start=5)
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['description']
        ).add_to(map_)
    map_.save(map_file)

if __name__ == "__main__":
    data_file = 'data/stray_dogs.csv'
    map_file = 'data/stray_dog_map.html'
    
    # Load existing data or create new DataFrame if no data exists
    try:
        data = load_data(data_file)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['latitude', 'longitude', 'description'])

    # Add a new dog location
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    description = input("Enter description: ")
    data = add_dog_location(data, latitude, longitude, description)

    # Save updated data
    save_data(data, data_file)
    
    # Generate map
    generate_map(data, map_file)
    print(f"Map has been generated: {map_file}")

