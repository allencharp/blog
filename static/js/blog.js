
/*
   Javascript Client FX
 */

function Comment(type, cid)
{
    this.prototype = Comment.prototype;

    /* property */
    this.type = type;
    this.cid = cid;

    /* method */
    if (typeof(this.prototype._init) == "undefined")
    {
        this.prototype._init = true;

        this.prototype.load = function(divId)
        {
            $("#" + divId).load("/comment/{0}/{1}".format(this.type, this.cid));
        };
    }
}

