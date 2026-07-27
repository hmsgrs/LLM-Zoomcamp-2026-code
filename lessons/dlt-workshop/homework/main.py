import argparse

import logfire

from dotenv import load_dotenv

load_dotenv()

logfire.configure()
logfire.instrument_pydantic_ai()

from agent import faq_agent, SearchDeps
from ingest import build_index, load_faq_data


def main():
    parser = argparse.ArgumentParser(description='Ask the course FAQ agent a question.')
    parser.add_argument(
        '--question',
        default='How do I run Ollama locally?',
        help='Question to send to the FAQ agent.',
    )
    args = parser.parse_args()

    # Download the FAQ and build the search index
    documents = load_faq_data()
    index = build_index(documents)

    # Inject the index into the agent via the dependency container
    deps = SearchDeps(index=index)

    # Ask a question. run_sync blocks until the agent is done;
    # the agent may call search multiple times before answering.
    result = faq_agent.run_sync(args.question, deps=deps)

    print(result.output)


if __name__ == '__main__':
    main()
