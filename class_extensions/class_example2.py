class InfoFormatter:

    def show_dimension(self):
        print('I am {} from dimension {}'.format(self.name, self.dimension))

class Rick(InfoFormatter):
    name = 'Rick'
    dimension = 'c137'

    def wubulubudubdub(self):
        print('I am not okay')

class Morty(InfoFormatter):
    name = 'Morty'
    dimension = 'c137'

    def awwwww_geeez(self):
        print('Geeeezz Rick!')

if __name__ == '__main__':
    Rick().show_dimension()
    Morty().show_dimension()