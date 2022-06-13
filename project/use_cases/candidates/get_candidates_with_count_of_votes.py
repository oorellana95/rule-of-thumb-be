"""Get Candidates with Votes UseCase."""
from typing import List, Optional
from sqlalchemy.orm import Session
from project.dtos import CandidatesFilterDto, VotesFilterDto
from project.schemas.candidates import GetCandidatesWithCounterOfVotesResponse
from project import repositories


def get_candidates_with_count_of_votes(db: Session, candidates_filter: CandidatesFilterDto) -> \
        List[GetCandidatesWithCounterOfVotesResponse]:
    """Get candidates with their votes."""
    candidates_itr = repositories.candidates.get_by_filter(db, candidates_filter)
    votes_itr = repositories.votes.get_votes_grouped_by_candidate_id_and_veredict(db, votes_filter=VotesFilterDto(
        veredict_types=[True, False]))

    response = []
    for candidate in candidates_itr:
        positive_votes = get_votes_by_candidate_id_and_veredict(votes=votes_itr,
                                                                candidate_id=candidate.id,
                                                                veredict=True)
        negative_votes = get_votes_by_candidate_id_and_veredict(votes=votes_itr,
                                                                candidate_id=candidate.id,
                                                                veredict=False)
        total_votes = positive_votes + negative_votes
        positive_votes_pct = round(positive_votes / total_votes, 3) if total_votes else 0
        negative_votes_pct = round(negative_votes / total_votes, 3) if total_votes else 0

        response.append(GetCandidatesWithCounterOfVotesResponse(**candidate,
                                                                positive_votes=positive_votes,
                                                                positive_votes_pct=positive_votes_pct,
                                                                negative_votes=negative_votes,
                                                                negative_votes_pct=negative_votes_pct,
                                                                total_votes=total_votes))

    return response


def get_votes_by_candidate_id_and_veredict(votes: list, candidate_id: int, veredict: Optional[bool]) -> int:
    if votes:
        filtered_vote = [vote for vote in votes if (vote.candidate_id is candidate_id and vote.veredict is veredict)]
        if filtered_vote:
            return filtered_vote[0].units
    return 0
