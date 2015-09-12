from thraxilsettings.shared import common

d = common(app='test')
locals().update(d)

print(DATABASES)
