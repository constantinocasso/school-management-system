from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=200, unique=True)  # Apenas uma escola por instância
    endereco = models.CharField(max_length=200)
    diretor = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Escola"
        verbose_name_plural = "Escolas"

class AnoLetivo(models.Model):
    ano = models.CharField(max_length=20, unique=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ano

    class Meta:
        verbose_name = "Ano Letivo"
        verbose_name_plural = "Anos Letivos"

class Classe(models.Model):
    descricao = models.CharField(max_length=100)
    tipo_classe = models.CharField(max_length=50)
    exame_combinado = models.BooleanField(default=False)
    nota_maxima = models.FloatField(default=20)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    ano_letivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE)
    sala = models.ForeignKey('SalaAula', on_delete=models.SET_NULL, null=True)
    turno = models.CharField(max_length=20, choices=[('Manha', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')])
    numero_alunos = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.curso}"

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class SalaAula(models.Model):
    descricao = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Sala de Aula"
        verbose_name_plural = "Salas de Aula"

class Disciplina(models.Model):
    descricao = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Prova(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, blank=True)
    peso = models.FloatField(default=0)
    formula = models.CharField(max_length=200, blank=True)
    dia = models.IntegerField(default=1)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Prova"
        verbose_name_plural = "Provas"

class Professor(models.Model):
    nome_completo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', blank=True)
    contato = models.CharField(max_length=100, blank=True)
    morada = models.CharField(max_length=200, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"

class ProfessorTurma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.professor} - {self.disciplina}"

    class Meta:
        verbose_name = "Professor-Turma"
        verbose_name_plural = "Professores-Turmas"

class Encarregado(models.Model):
    nome_completo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', blank=True)
    relacionamento = models.CharField(max_length=50)
    contato = models.CharField(max_length=100, blank=True)
    morada = models.CharField(max_length=200, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Encarregado"
        verbose_name_plural = "Encarregados"

class Aluno(models.Model):
    nome_completo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', blank=True)
    nome_pai = models.CharField(max_length=100, blank=True)
    nome_mae = models.CharField(max_length=100, blank=True)
    encarregado = models.ForeignKey(Encarregado, on_delete=models.SET_NULL, null=True)
    hablitacoes = models.CharField(max_length=100, blank=True)
    profissao = models.CharField(max_length=100, blank=True)
    nacionalidade = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=20, choices=[('Cedula', 'Cédula'), ('BI', 'Bilhete de Identidade')])
    numero_documento = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    estado_civil = models.CharField(max_length=20, choices=[('Solteiro', 'Solteiro'), ('Casado', 'Casado'), ('Outro', 'Outro')], blank=True)
    curso = models.CharField(max_length=100)
    classe_nivel = models.ForeignKey(Classe, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    contato = models.CharField(max_length=100, blank=True)
    morada = models.CharField(max_length=200, blank=True)
    data_inscricao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo'), ('Transferido', 'Transferido')], default='Ativo')
    risco_reprovacao = models.CharField(max_length=20, choices=[('Baixo', 'Baixo'), ('Médio', 'Médio'), ('Alto', 'Alto')], default='Baixo')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    valor = models.FloatField()
    modalidade = models.CharField(max_length=20, choices=[('Interna', 'Interna'), ('Externa', 'Externa'), ('Nacional', 'Nacional')])
    trimestre = models.CharField(max_length=20, choices=[('1º Trimestre', '1º Trimestre'), ('2º Trimestre', '2º Trimestre'), ('3º Trimestre', '3º Trimestre')])
    reapreciacao = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} - {self.valor}"

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

class EscolaTransferencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    classe_nivel = models.ForeignKey(Classe, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    escola_destino = models.CharField(max_length=200)  # Nome da escola de destino para transferência
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.escola_destino}"

    class Meta:
        verbose_name = "Escola de Transferência"
        verbose_name_plural = "Escolas de Transferência"

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    perfil = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Professor', 'Professor'), ('Aluno', 'Aluno'), ('Encarregado', 'Encarregado')])
    senha = models.CharField(max_length=128)
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class CriterioAvaliacao(models.Model):
    nome = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    aprovacao_reprovacao = models.CharField(max_length=100)
    nota_minima = models.FloatField(default=0)
    nota_maxima = models.FloatField(default=20)
    nota_positiva_aprovacao = models.FloatField(default=10)
    incluir_exame = models.BooleanField(default=False)
    sistema_recursos = models.BooleanField(default=False)
    formula = models.CharField(max_length=200, blank=True)
    percentagem_trimestre1 = models.FloatField(default=33.33)
    percentagem_trimestre2 = models.FloatField(default=33.33)
    percentagem_trimestre3 = models.FloatField(default=33.33)
    percentagem_prova_final = models.FloatField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Critério de Avaliação"
        verbose_name_plural = "Critérios de Avaliação"

class Material(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='materiais/')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiais"

class Mensagem(models.Model):
    remetente = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remetente} para {self.destinatario}"

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

class PlanoPedagogico(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plano para {self.aluno}"

    class Meta:
        verbose_name = "Plano Pedagógico"
        verbose_name_plural = "Planos Pedagógicos"

class ExameEspecial(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=[('Recurso', 'Recurso'), ('Extraordinario', 'Extraordinário'), ('Equivalencia', 'Equivalência'), ('Melhoria', 'Melhoria')])
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.FloatField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.tipo} - {self.disciplina}"

    class Meta:
        verbose_name = "Exame Especial"
        verbose_name_plural = "Exames Especiais"