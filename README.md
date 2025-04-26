# inkscape-extensions

This repo holds some inkscape extensions I've made.

The extension tutorials are nice, but you'll sometimes have to inspect how other extensions do things to learn.

Here's where you can find them [extensions](https://gitlab.com/inkscape/extensions/-/tree/master) , you'll need a GitLab account.

I'll try to have a section on what each extension does and what references I used to figure it out.

Since inkscape handles extensions in folders, feel free to clone this and copy the folder for the appropriate to your extensions folder.

## BatchPNGExport

This extension exports PNGs in many square sizes (16x16, 32x32) etc, from the current document. It was built to produce [icons](https://www.foundations.unity.com/fundamentals/iconography#Single-Size-Icons) for the Unity Editor.

Finding how to export stuff took a bit, and I used the [Guillotine](https://gitlab.com/inkscape/extensions/-/blob/master/guillotine.py) extension as a reference.

One tricky thing I had for this was that only `export_area="0:0:100:100"` seemed to work, using `page` or `drawing` as an argument didn't work for me.

The export uses the `inkscape` command, instead of spining up a shell. You can find info about the command [here](https://inkscape.gitlab.io/extensions/documentation/source/inkex.command.html#inkex.command.inkscape)
