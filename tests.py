import unittest
from bem_syntax_analyzer import analyze

class TestBEMAnalyzerMethods(unittest.TestCase):

    def test_valide_syntax(self):
        data = """
            <article class="article">
                <h5 class="article__title">Lorem ipsum dolor.</h5>
                <div class="article__body">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi omnis dolorum, obcaecati minima quisquam, consectetur quibusdam, animi fugiat pariatur debitis quis quidem quos corporis odit porro cum modi beatae assumenda amet at eligendi inventore quia. Harum eligendi impedit quidem omnis ullam ipsum, delectus voluptates laudantium totam repellendus inventore iste hic.
                    <a href="#" class="[ article__link  article__link--heavy ]  link">Lorem ipsum dolor sit amet, consectetur.</a>
                </div>
                <div class="article__tags">
                    <ul class="tag-list">
                        <li class="tag-list__item  tag-list__item--first">lorem</li>
                        <li class="tag-list__item">ipsum</li>
                        <li class="tag-list__item">dolor</li>
                    </ul>
                </div>
            </article>
        """

        items = analyze(data)

        self.assertEqual(len(items), 0)

    def test_unvalide_syntax(self):
        data = """
            <article class="article">
                <h5 class="article__title--h5">Lorem ipsum dolor.</h5>
                <div class="article__body">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi omnis dolorum, obcaecati minima quisquam, consectetur quibusdam, animi fugiat pariatur debitis quis quidem quos corporis odit porro cum modi beatae assumenda amet at eligendi inventore quia. Harum eligendi impedit quidem omnis ullam ipsum, delectus voluptates laudantium totam repellendus inventore iste hic.
                    <a href="#" class="article__body__link--heavy  link">Lorem ipsum dolor sit amet, consectetur.</a>
                </div>
                <div class="article--tags">
                    <ul class="tag-list">
                        <li class="tag-list__item--first">lorem</li>
                        <li class="tag-list__item">ipsum</li>
                        <li class="tag-list__item">dolor</li>
                    </ul>
                </div>
            </article>
        """

        items = analyze(data)

        self.assertEqual(len(items), 5)

if __name__ == '__main__':
    unittest.main()
