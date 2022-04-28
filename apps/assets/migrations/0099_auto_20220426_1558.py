# Generated by Django 3.1.14 on 2022-04-26 07:58
import uuid

from django.db import migrations

failed_apps = []


def create_app_platform(apps, *args):
    platform_model = apps.get_model('assets', 'Platform')
    platforms = [
        # DB
        {'name': 'MySQL', 'category': 'database', 'type': 'mysql'},
        {'name': 'MariaDB', 'category': 'database', 'type': 'mariadb'},
        {'name': 'PostgreSQL', 'category': 'database', 'type': 'postgresql'},
        {'name': 'Oracle', 'category': 'database', 'type': 'oracle'},
        {'name': 'SQLServer', 'category': 'database', 'type': 'sqlserver'},
        {'name': 'MongoDB', 'category': 'database', 'type': 'mongodb'},
        {'name': 'Redis', 'category': 'database', 'type': 'redis'},
        {'name': 'Chrome', 'category': 'remote_app', 'type': 'chrome'},
        {'name': 'vSphereClient', 'category': 'remote_app', 'type': 'vmware_client'},
        {'name': 'MySQLWorkbench', 'category': 'remote_app', 'type': 'mysql_workbench'},
        {'name': 'GeneralRemoteApp', 'category': 'remote_app', 'type': 'general_remote_app'},
        {'name': 'Kubernetes', 'category': 'cloud', 'type': 'k8s'},
    ]

    for platform in platforms:
        platform['internal'] = True
        print("Create platform: {}".format(platform['name']))
        platform_model.objects.update_or_create(defaults=platform, name=platform['name'])


def get_prop_name_id(apps, app, category):
    asset_model = apps.get_model('assets', 'Asset')
    _id = app.id
    id_exists = asset_model.objects.filter(id=_id).exists()
    if (id_exists):
        _id = uuid.uuid4()
    name = app.name
    name_exists = asset_model.objects.filter(hostname=name).exists()
    if name_exists:
        name = category + '-' + app.name
    return _id, name


def migrate_database_to_asset(apps, *args):
    app_model = apps.get_model('applications', 'Application')
    db_model = apps.get_model('assets', 'Database')
    platform_model = apps.get_model('assets', 'Platform')

    applications = app_model.objects.filter(category='db')
    platforms = platform_model.objects.all()
    platforms_map = {p.type: p for p in platforms}

    for app in applications:
        attrs = {'host': '', 'port': 0, 'database': ''}
        _attrs = app.attrs or {}
        attrs.update(_attrs)

        db = db_model(
            id=app.id, hostname=app.name, ip=attrs['host'],
            protocols='{}/{}'.format(app.type, attrs['port']),
            category='database', type=app.type,
            db_name=attrs['database'] or '',
            platform=platforms_map[app.type],
            org_id=app.org_id
        )
        try:
            print("Create database: ", app.name)
            db.save()
        except:
            failed_apps.append(app)
            pass
                # db.hostname = 'DB-' + db.hostname


def migrate_remote_app_to_asset(apps, *args):
    app_model = apps.get_model('applications', 'Application')
    remote_app_model = apps.get_model('assets', 'RemoteApp')
    host_model = apps.get_model('assets', 'Host')
    platform_model = apps.get_model('assets', 'Platform')
    applications = app_model.objects.filter(category='remote_app')
    platforms = platform_model.objects.filter(category='remote_app')
    platforms_map = {p.type: p for p in platforms}

    connect_host_map = {}

    for app in applications:
        attrs = app.attrs
        connect_host = attrs.pop('asset')
        if connect_host:
            connect_host = host_model.objects.filter(asset_ptr_id=connect_host).first()
            connect_host_map[app.id] = connect_host

    for app in applications:
        tp = app.type
        app_path = attrs.pop('path', '')
        if tp == 'custom':
            tp = 'general_remote_app'

        print("Create remote app: {}".format(app.name))
        remote_app = remote_app_model(
            id=app.id, hostname=app.name, ip='',
            protocols='',
            category='remote_app', type=tp,
            platform=platforms_map[tp],
            org_id=app.org_id,

            app_path=app_path,
            connect_host=connect_host_map.get(app.id),
            attrs=attrs,
        )
        try:
            remote_app.save()
        except Exception as e:
            print("Error: ", e)
            # remote_app.hostname = 'RemoteApp-' + remote_app.hostname


def migrate_cloud_to_asset(apps, *args):
    app_model = apps.get_model('applications', 'Application')
    cloud_model = apps.get_model('assets', 'Cloud')
    platform_model = apps.get_model('assets', 'Platform')

    applications = app_model.objects.filter(category='cloud')
    platform = platform_model.objects.filter(type='k8s').first()

    for app in applications:
        attrs = app.attrs
        print("Create cloud: {}".format(app.name))
        cloud = cloud_model(
            id=app.id, hostname=app.name, ip='',
            category='remote_app', type='k8s',
            protocols='',
            platform=platform,
            org_id=app.org_id,
            cluster=attrs.get('cluster', '')
        )

        try:
            cloud.save()
        except Exception as e:
            failed_apps.append(cloud)
            print("Error: ", e)


def create_app_nodes(apps, org_id):
    node_model = apps.get_model('assets', 'Node')

    child_pattern = r'^[0-9]+:[0-9]+$'
    node_keys = node_model.objects.filter(org_id=org_id) \
        .filter(key__regex=child_pattern) \
        .values_list('key', flat=True)
    if not node_keys:
        return
    node_key_split = [key.split(':') for key in node_keys]
    next_value = int(max([k[1] for k in node_key_split])) + 1
    parent_key = node_key_split[0][0]
    parent = node_model.objects.get(key=parent_key)
    next_key = '{}:{}'.format(node_key_split[0][0], next_value)
    name = 'Apps'
    full_value = parent.full_value + '/' + name
    defaults = {
        'key': next_key, 'value': name, 'parent_key': parent_key,
        'full_value': full_value, 'org_id': org_id
    }
    node, created = node_model.objects.get_or_create(
        defaults=defaults, value=name, org_id=org_id,
    )
    node.parent = parent
    return node


def migrate_to_nodes(apps, *args):
    org_model = apps.get_model('orgs', 'Organization')
    asset_model = apps.get_model('assets', 'Asset')
    orgs = org_model.objects.all()

    for org in orgs:
        node = create_app_nodes(apps, org.id)
        assets = asset_model.objects.filter(
            category__in=['remote_app', 'database', 'cloud'],
            org_id=org.id
        )
        print("Set node asset: ", node)
        if node:
            node.assets_amount = len(assets)
            node.save()
            node.assets.set(assets)
            parent = node.parent
            parent.assets_amount += len(assets)
            parent.save()


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0098_auto_20220426_1550'),
        ('applications', '0020_auto_20220316_2028')
    ]

    operations = [
        migrations.RunPython(create_app_platform),
        migrations.RunPython(migrate_database_to_asset),
        migrations.RunPython(migrate_remote_app_to_asset),
        migrations.RunPython(migrate_cloud_to_asset),
        migrations.RunPython(migrate_to_nodes)
    ]
