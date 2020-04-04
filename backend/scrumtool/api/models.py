""" This file contains database definitions
"""
from django.db import models


class Project(models.Model):
    """Model definition for Project."""
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    class Meta:
        """Meta definition for Project."""

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        """Unicode representation of Project."""
        pass


class Board(models.Model):
    """Model definition for Board."""

    board = models.ForeignKey(
        to='Project',
        on_delete=models.CASCADE,
        related_name='boards')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=2)
    display_lane_horizontal = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Board."""

        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

    def __str__(self):
        """Unicode representation of Board."""
        pass


BOARD_TYPE = (
    ('PB', 'Product Backlog Board'),
    ('SP', 'Sprint Backlog Board '),
    ('AB', 'Archiv Board'),
)


class Lane(models.Model):
    """Model definition for Lane. """

    board = models.ForeignKey(
        to='Board',
        on_delete=models.CASCADE,
        related_name='lanes')
    name = models.CharField(max_length=256)
    numbering = models.IntegerField(default=0)

    class Meta:
        """Meta definition for Lane."""

        verbose_name = 'Lane'
        verbose_name_plural = 'Lanes'

    def __str__(self):
        """Unicode representation of Lane."""
        pass


class Card(models.Model):
    """A Card contains all information concerning a task.
    Including the Steplist
    """
    lane = models.ForeignKey(
        to='Lane',
        on_delete=models.CASCADE,
        related_name='cards')
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    numbering = models.IntegerField(default=0)
    storypoints = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=2)

    class Meta:
        """Meta definition for Card."""

        verbose_name = 'Card'
        verbose_name_plural = 'Card'
        abstract = True

    def __str__(self):
        return "{0} ({1}) {2}".format(
            self.name,
            self.description,
            self.storypoints)


STATUS = (
    ('ns', 'not started'),
    ('do', 'done'),
    ('ip', 'in progress'),
)


class Label(models.Model):
    """Model definition for Label."""
    card = models.ForeignKey(
        to='Card',
        on_delete=models.CASCADE,
        related_name='labels'
    )
    title = models.CharField(max_length=256)

    class Meta:
        """Meta definition for Label."""

        verbose_name = 'Label'
        verbose_name_plural = 'Labels'

    def __str__(self):
        """Unicode representation of Label."""
        pass


class Epic(Card):
    """Model definition for Epic."""

    class Meta:
        """Meta definition for Epic."""

        verbose_name = 'Epic(Card)'
        verbose_name_plural = 'Epics(Card)'

    def __str__(self):
        """Unicode representation of Epic."""
        pass


class Feature(Card):
    """A Feature describes a part of an Epic."""
    epic = models.ForeignKey(
        to='Epic',
        on_delete=models.CASCADE,
        related_name='features')

    class Meta:
        """Meta definition for Feature."""
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        """Unicode representation of Feature."""
        pass


class Task(Card):
    """Model definition for Task."""
    feature = models.ForeignKey(
        to='Feature',
        on_delete=models.CASCADE,
        related_name='tasks')

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """Unicode representation of Task."""
        pass


class Steplist(models.Model):
    """ A Steplist contains all elements of a Steplist
    """
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    class Meta:
        """Meta definition for Steplist."""

        verbose_name = 'Steplist'
        verbose_name_plural = 'Steplist'

    def __str__(self):
        return "{0} ".format(self.name)


class SteplistItem(models.Model):
    """ A SteplistItem describes a Task that has to be done
    """
    steplist = models.ForeignKey(
        to='Steplist',
        on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    checked = models.BooleanField(default=False)
    numbering = models.IntegerField(default=0, unique=False)

    class Meta:
        """Meta definition for Step."""

        verbose_name = 'Step'
        verbose_name_plural = 'Step'

    def __str__(self):
        return "{0}: {1}({2}): {3} ".format(self.numbering, self.text,
                                            self.steplist,
                                            self.checked,
                                            )
