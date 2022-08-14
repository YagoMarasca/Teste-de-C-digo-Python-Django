from rolepermissions.roles import AbstractUserRole


class Empresa(AbstractUserRole):
    available_permissions ={'criar_vagas': True, 'ver_vagas': True, 'relatorio_vagas': True}


class Candidato(AbstractUserRole):
    available_permissions = {'ver_vagas': True, 'candidatar_vagas': True}