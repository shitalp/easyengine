"""EasyEngine site controller."""

from cement.core.controller import CementBaseController, expose

class EECleanController(CementBaseController):
    class Meta:
        label = 'clean'
        interface = controller.IController
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'clean command cleans different cache with following options'
            (['-f', '--foo'],
             dict(help='the notorious foo option', dest='foo', action='store',
                  metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        # Default action for ee clean command
        print ("Inside EECleanController.default().")

        # clean command Options and subcommand calls and definations to
        # mention here

        # If using an output handler such as 'mustache', you could also
        # render a data dictionary using a template.  For example:
        #
        #   data = dict(foo='bar')
        #   self.app.render(data, 'default.mustache')
        #
        #
        # The 'default.mustache' file would be loaded from
        # ``ee.cli.templates``, or ``/var/lib/ee/templates/``.
        #