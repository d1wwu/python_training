from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    app.session.logout()
