# Permanent Banner by Default.
# Type help for instructions

from Wish import wishes


if __name__ == '__main__':
    n_help = wishes.Color.RED + 'help' + wishes.Color.END
    print('`~`' * 4, wishes.Color.CYAN + 'Genshin Impact Wish Simulator' + wishes.Color.END, '`~`' * 4)
    print('   ', '`~`' * 3, f'Type {n_help} for instructions', '`~`' * 3, '\n', ' ' * 10, '`~`' * 10)
    wishes.init()
