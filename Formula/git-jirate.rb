class GitJirate < Formula
  include Language::Python::Virtualenv

  desc "A Python CLI installed from a wheel"
  homepage "https://github.com/aronobagnon/homebrew-git-jirate"
  url "https://github.com/AronoBagnon/homebrew-git-jirate/archive/refs/tags/0.0.1.tar.gz"
  sha256 "59b31cf2c588662ce8e4e0fdea292fbe4283ad2912c1aae24c1387653f6db1ae"

  depends_on "python@3.11"

  resource "git-jirate" do
    url "https://github.com/AronoBagnon/homebrew-git-jirate/releases/download/0.0.1/git_jirate-0.0.1-py3-none-any.whl"
    sha256 "68d7a068148941782397f1132f984018605dab37d5369e2225812837361d50c2"
  end

  def install
    virtualenv_install_with_resources
    bin.install_symlink libexec/"bin/git-jirate"
  end

  test do
    system "#{bin}/git-jirate", "--version"
  end
end

