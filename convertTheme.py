import click
import json
import os


@click.command()
@click.argument('theme')
@click.option('--output_dir', default="output/", prompt='Output Directory', help='Where should the output be written to?')
@click.option('--contrast', default="normal", help='Contrast scheme to use, can be normal, medium, or high')
def convert(theme, output_dir, contrast="normal"):
    """Converts a theme exported from https://material-foundation.github.io/material-theme-builder/ to SwiftUI color sets."""
    with open(theme) as f:
        theme = json.load(f)
        light = theme['schemes'].get('light').items()
        dark = theme['schemes'].get('dark').items()
        for l,d in zip(light, dark):
            # create folder if not exist
            folder = output_dir + l[0][0].upper() + l[0][1:] + 'Color.colorset'
            if not os.path.exists(folder):
                os.makedirs(folder)

            # create content of color json
            c = color.copy()
            l_comp = c['colors'][0]['color']['components']
            l_comp['red'] = '0x' + l[1][1:3]
            l_comp['green'] = '0x' + l[1][3:5]
            l_comp['blue'] = '0x' + l[1][5:7]

            d_comp = c['colors'][1]['color']['components']
            d_comp['red'] = '0x' + d[1][1:3]
            d_comp['green'] = '0x' + d[1][3:5]
            d_comp['blue'] = '0x' + d[1][5:7]
            with open(folder + '/Contents.json', 'w') as color_file:
                json.dump(c, color_file)

color = {
  "colors" : [
    {
      "color" : {
        "color-space" : "display-p3",
        "components" : {
          "alpha" : "1.000"
        }
      },
      "idiom" : "universal"
    },
    {
      "appearances" : [
        {
          "appearance" : "luminosity",
          "value" : "dark"
        }
      ],
      "color" : {
        "color-space" : "display-p3",
        "components" : {
          "alpha" : "1.000"
        }
      },
      "idiom" : "universal"
    }
  ],
  "info" : {
    "author" : "xcode",
    "version" : 1
  }
}
  

if __name__ == '__main__':
    convert()