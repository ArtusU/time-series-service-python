import uuid
from datetime import datetime

from models import DataPoint, Device, User

datastore = {
    "bd365184-6df6-42b5-b5fc-29cbbef3136c_d566b66d-9f73-43a2-9912-a679ba9df6d9_9d3f8ea8-5f01-49c4-a6ef-9de0ddf4265d": DataPoint(
        timestamp=datetime(2023, 8, 12, 17, 16, 13, 670541),
        value=30.0,
        device=Device(
            id=uuid.UUID("d566b66d-9f73-43a2-9912-a679ba9df6d9"), name="oven"
        ),
        user=User(id=uuid.UUID("bd365184-6df6-42b5-b5fc-29cbbef3136c"), name="Mike"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_75b662e3-972c-4611-a9b4-7450dc2b718f": DataPoint(
        timestamp=datetime(2023, 8, 12, 17, 40, 28, 237504),
        value=100.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_91e0015e-153c-489f-b088-1077f50be858": DataPoint(
        timestamp=datetime(2023, 8, 12, 17, 40, 29, 865331),
        value=200.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c001e": DataPoint(
        timestamp=datetime(2023, 8, 12, 17, 41, 23, 357955),
        value=300.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0011": DataPoint(
        timestamp=datetime(2023, 8, 13, 9, 41, 23, 357955),
        value=400.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0012": DataPoint(
        timestamp=datetime(2023, 8, 13, 9, 42, 23, 357955),
        value=500.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0013": DataPoint(
        timestamp=datetime(2023, 8, 13, 9, 43, 23, 357955),
        value=600.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0014": DataPoint(
        timestamp=datetime(2023, 8, 13, 10, 43, 23, 357955),
        value=700.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0015": DataPoint(
        timestamp=datetime(2023, 8, 13, 10, 45, 23, 357955),
        value=800.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0016": DataPoint(
        timestamp=datetime(2023, 8, 13, 10, 46, 23, 357955),
        value=900.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
    "ed620724-30f2-4b9c-9fa7-636cc7d2d24e_58a1f904-df84-4b64-89ab-eecd511c0df0_4de8b7ba-43b4-422a-bb5f-7fe78a2c0017": DataPoint(
        timestamp=datetime(2023, 8, 13, 10, 56, 23, 357955),
        value=1000.0,
        device=Device(
            id=uuid.UUID("58a1f904-df84-4b64-89ab-eecd511c0df0"), name="socket"
        ),
        user=User(id=uuid.UUID("ed620724-30f2-4b9c-9fa7-636cc7d2d24e"), name="Mia"),
    ),
}
