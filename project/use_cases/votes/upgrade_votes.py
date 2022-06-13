"""Upgrade Votes UseCase."""
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

from project import repositories
from project.models.vote import Vote


def upgrade_votes(db: Session, user_id: int, candidate_id: int, veredict: bool = None) -> str:
    """Get candidates with their votes."""
    vote = repositories.votes.get_vote_by_user_id_and_candidate_id(db, user_id=user_id, candidate_id=candidate_id)
    veredict_to_historical = {
        'veredict': veredict_to_tinyint(veredict),
        'datetime': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    if vote:
        vote.veredict = veredict
        vote.historical_veredicts.append(veredict_to_historical)
        flag_modified(vote, "historical_veredicts")
        repositories.votes.update(db, vote=vote)
        return f"Your vote has successfully been updated."
    else:
        vote = Vote(user_id=user_id,
                    candidate_id=candidate_id,
                    veredict=veredict,
                    historical_veredicts=[veredict_to_historical])
        repositories.votes.create(db, vote=vote)
        return f"Your vote has successfully been registered."


def veredict_to_tinyint(veredict: Optional[bool]):
    if veredict is None:
        return None
    return 1 if veredict else 0


