# Antenna House Extension Properties: Multimedia Properties

<!-- Source: XSL-FO-Reference-74-MID.pdf pp.312–476 -->

Properties for embedding multimedia content (video, audio, Flash) in PDF output, controlling playback mode, volume, window dimensions, and skin appearance.

## axf:media-activation

Specifies when to activate / deactivate the rich media. Values are case insensitive; values other than the following are ignored:

- **ExplicitlyActivated** (abbrev. XA): Activates when the content is clicked.
- **PageOpen** (abbrev. PO): Activates when the page containing the content is opened.
- **PageVisible** (abbrev. PV): Activates when the page containing the content is displayed.
- **ExplicitlyDeactivated** (abbrev. XD): Deactivates when "Disable Content" is selected from the context menu.
- **PageClose** (abbrev. PC): Deactivates when the page containing the content is closed.
- **PageInvisible** (abbrev. PI): Deactivates when the page containing the content is not displayed.

If omitted, it is considered ExplicitlyActivated ExplicitlyDeactivated. This setting is effective when Rich media is activated.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | [ ExplicitlyActivated \| PageOpen \| PageVisible ]? [ ExplicitlyDeactivated \| PageClose \| PageInvisible ]? |
| **Initial** | empty |
| **Inherited** | no |

## axf:media-duration

Specifies the duration of a time period of the multimedia. Whether the setting is effective or not depends on the multimedia data, the viewer or the player. This setting is invalid with the rich media. Values have the following meanings:

- **intrinsic**: Plays the multimedia only the period of time that the resource has.
- **infinity**: Plays the multimedia indefinitely.
- **&lt;number&gt;**: Plays the multimedia only the specified period of time. The value is the number of seconds.

This setting is invalid when axf:media-play-mode="once" is specified.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | intrinsic \| infinity \| &lt;number&gt; |
| **Initial** | intrinsic |
| **Inherited** | no |

## axf:media-extraction-policy

Specifies whether the creation of temporary files is allowed or not when playing the multimedia. Whether the setting is effective or not depends on the multimedia data, the viewer or the player. This setting is invalid with the rich media. Values have the following meanings:

- **tempnever**: The creation of temporary files is not allowed.
- **tempextract**: Only when the "copy of the contents" is given to the user right to access PDF, the creation of temporary files is allowed.
- **tempaccess**: Only when the "content extraction for accessibility" is given to the user right to access PDF, the creation of temporary files is allowed.
- **tempalways**: The creation of temporary files is always allowed.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | tempnever \| tempextract \| tempaccess \| tempalways |
| **Initial** | tempaccess |
| **Inherited** | no |

## axf:media-flash-context-menu

Specifies whether to display the context menu of Flash when embedding Flash in the rich media. This setting is effective when embedding Flash in the Rich media.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | true \| false |
| **Initial** | true |
| **Inherited** | no |

## axf:media-flash-vars

Specifies the variable when embedding Flash in the rich media. This setting is effective when embedding Flash in the Rich media. Even if there are some errors in the described content, these are not detected and output to PDF as is.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | &lt;string&gt; |
| **Initial** | empty string |
| **Inherited** | no |

## axf:media-play-mode

Specifies the number of times to play the multimedia. Whether the setting is effective or not depends on the multimedia data, the viewer or the player. This setting is invalid with the rich media. Values have the following meanings:

- **once**: Plays the multimedia only one time.
- **continuously**: Plays the multimedia continuously.
- **&lt;number&gt;**: Plays the multimedia only the specified number of times.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | once \| continuously \| &lt;number&gt; |
| **Initial** | once |
| **Inherited** | no |

## axf:media-skin-auto-hide

Specifies whether to automatically hide Rich Media skins or not. This setting is effective when the Rich Media is activated.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | true \| false |
| **Initial** | true |
| **Inherited** | no |

## axf:media-skin-color

Specifies the skin color of the Rich Media. When the color does not contain the alpha value, the default alpha value is adopted. When alpha value is specified, that value is adopted. This setting is effective when the Rich media is activated.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | auto \| &lt;color&gt; |
| **Initial** | auto |
| **Inherited** | no |

## axf:media-skin-control

Specifies the skin control of the Rich Media. Values have the following meanings:

- **none**: No controls are displayed.
- **all**: All controls are displayed.
- **play**: The playback control is displayed.
- **stop**: The stop control is displayed.
- **forward**: The fast-forward control is displayed.
- **rewind**: The rewind control is displayed.
- **seek**: The seek control is displayed.
- **mute**: The mute control is displayed.
- **volume**: The volume control is displayed.

Other controls may be displayed automatically to display a certain control. This setting is effective when the Rich media is activated.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | none \| all \| [ play \|\| stop \|\| forward \|\| rewind \|\| seek \|\| mute \|\| volume ] |
| **Initial** | all |
| **Inherited** | no |

## axf:media-transparent-background

Specifies whether to make the background transparent when embedding Flash in the Rich Media.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | true \| false |
| **Initial** | true |
| **Inherited** | no |

## axf:media-volume

Specifies the volume of the sound when playing the multimedia. Whether the setting is effective or not depends on the multimedia data, the viewer or the player. It is effective also with the rich media, but when editing the multimedia with Acrobat, this setting seems to be canceled.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | &lt;percentage&gt; \| &lt;number&gt; \| auto |
| **Initial** | auto |
| **Inherited** | no |

## axf:media-window-height

Specifies the height of the window when axf:multimedia-treatment="richmedia-windowed" is specified. This setting is effective when the Rich media is activated.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | auto \| &lt;length&gt; |
| **Initial** | auto |
| **Inherited** | no |

## axf:media-window-width

Specifies the width of the window when axf:multimedia-treatment="richmedia-windowed" is specified. This setting is effective when the Rich media is activated.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | auto \| &lt;length&gt; |
| **Initial** | auto |
| **Inherited** | no |

## axf:multimedia-treatment

Specifies whether to embed Multimedia in PDF. Values have the following meanings:

- **auto**: The value specified by multimedia-treatment in the Option Setting File is adopted.
- **embed**: Embeds the multimedia objects in PDF. It is not recommended for PDF 2.0 or later.
- **absolute-link**: Links the multimedia objects in PDF, instead of embedding them. The linked multimedia objects are referred to as the absolute link. It is not recommended for PDF 2.0 or later.
- **relative-link**: Links the multimedia objects in PDF, instead of embedding them. The linked multimedia objects are referred to as the relative link from either XML or FO. It is not recommended for PDF 2.0 or later.
- **richmedia**: Embeds the multimedia as Rich media annotation. Effective with PDF1.7 or later.
- **richmedia-windowed**: Embeds the multimedia as Rich media annotation, but displayed in a separate window when playing. Effective with PDF1.7 or later.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | auto \| embed \| absolute-link \| relative-link \| richmedia \| richmedia-windowed |
| **Initial** | auto |
| **Inherited** | yes |

## axf:poster-content-type

Specifies the content type of the poster image for embedded multimedia. Values have the following meanings:

- **&lt;string&gt;**: Specifies the content type of the poster image.
- **auto**: Recognizes the content type from the poster image.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | &lt;string&gt; \| auto |
| **Initial** | auto |
| **Inherited** | no |

## axf:poster-image

Specifies the poster image for embedded multimedia. Values have the following meanings:

- **&lt;uri-specification&gt;**: Specifies the URL of the poster image. Multimedia, such as video or audio, cannot be specified.
- **none**: Specifies no poster images.
- **auto**: Uses the plain fallback image for the poster image.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | &lt;uri-specification&gt; \| none \| auto |
| **Initial** | auto |
| **Inherited** | no |

## axf:show-controls

Specifies whether to show the player control bar for multimedia. The control bar is shown under the playing multimedia object. To prevent overlapping the control bar with another object, it is necessary to make enough space below the multimedia object. Whether the control bar is shown or not depends on the multimedia data, the viewer or the player. This setting is invalid with the Rich Media.

| Attribute | Value |
|---|---|
| **Applies to** | `<fo:external-graphic>` |
| **Values** | true \| false |
| **Initial** | false |
| **Inherited** | no |
