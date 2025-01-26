# RestaurantNameGenerator

A Python project that generates creative restaurant names and menu items based on a given cuisine. This project uses LangChain for chaining together language models to generate restaurant names and their respective menu items.

## Features

- **Restaurant Name Generator**: Given a cuisine, the model generates a creative name for a restaurant.
- **Menu Items Generator**: For a given restaurant name, the model generates a list of menu items.
- **Easy Setup**: The project uses LangChain and OpenAI to make it easy to generate restaurant-related content.

## Usage

1. **Run the Program**:
   To generate a restaurant name and menu items, run the `main.py` file. For example, to generate content for an Italian restaurant:
   ```bash
   python main.py
   ```

   Example usage within the script:
   ```python
   from LangchainHelper import generate_restaurantname_and_items
   print(generate_restaurantname_and_items("Italian"))
   ```

   This will output a restaurant name and some menu items for an Italian cuisine restaurant.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Customizing the Generator
You can easily modify the prompt templates in `LangchainHelper.py` to generate restaurant names and menu items for different cuisines. Just update the templates and add more chains if you want additional features!

---

This should give anyone who clones the repository enough information to set up and use the project. You can customize it further based on any additional features or instructions. Let me know if you need more changes or have any questions! 😊
