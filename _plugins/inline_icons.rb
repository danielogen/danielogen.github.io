# Replaces icon-font markup with inline SVG at build time, so pages don't download
# Font Awesome (~100 KB of CSS + font) or Academicons for a few dozen small icons.
#
# Templates keep the familiar syntax: <i class="fas fa-trophy"></i>. Each one becomes
#   <svg class="icon fa-trophy" viewBox="..." aria-hidden="true"><use href="#i-solid-trophy"/></svg>
# and the page gets one hidden <svg> holding a <symbol> for each icon it uses.
# Extra classes (fa-2x, mr-1, text-success, fa-sun, ...) are kept, so CSS still applies.
#
# Shapes come from _data/icons.json; run `python3 scripts/fetch_icons.py` to add new ones.
module InlineIcons
  SETS = {
    "fas" => "solid", "fa-solid" => "solid", "far" => "regular", "fa-regular" => "regular",
    "fab" => "brands", "fa-brands" => "brands", "ai" => "ai"
  }.freeze
  MODIFIERS = %w[fa-xs fa-sm fa-lg fa-2x fa-3x fa-fw].freeze
  TAG = %r{<i\s([^>]*?)class="([^"]*)"([^>]*)>\s*</i>}.freeze

  def self.process(doc)
    return unless doc.output_ext == ".html" && doc.output.include?("<i ")

    icons = doc.site.data["icons"] || {}
    used = {}
    doc.output = doc.output.gsub(TAG) do
      match = Regexp.last_match
      before, classes, after = match[1], match[2].split, match[3]
      set = classes.map { |c| SETS[c] }.compact.first
      name = classes.find { |c| c =~ /\A(fa|ai)-/ && !SETS.key?(c) && !MODIFIERS.include?(c) }
      next match[0] unless set && name

      key = "#{set}/#{name.sub(/\A(fa|ai)-/, '')}"
      icon = icons[key] or raise "Icon \"#{classes.join(' ')}\" (#{key}) in #{doc.relative_path} " \
                                 "is not in _data/icons.json. Run: python3 scripts/fetch_icons.py"
      used[key] = icon
      keep = classes.reject { |c| SETS.key?(c) }
      attrs = "#{before}#{after}".strip
      attrs = [attrs, ('aria-hidden="true"' unless attrs.include?("aria-")), 'focusable="false"'].compact.reject(&:empty?)
      %(<svg class="#{(['icon'] + keep).join(' ')}" viewBox="#{icon['viewBox']}" #{attrs.join(' ')}>) +
        %(<use href="#i-#{key.tr('/', '-')}"/></svg>)
    end
    return if used.empty?

    symbols = used.map do |key, icon|
      %(<symbol id="i-#{key.tr('/', '-')}" viewBox="#{icon['viewBox']}">#{icon['body']}</symbol>)
    end
    sprite = %(<svg xmlns="http://www.w3.org/2000/svg" class="icon-sprite" aria-hidden="true">) +
             "<!-- Icons: Font Awesome Free 6.5.1 (CC BY 4.0), Academicons 1.9.1 (SIL OFL 1.1) -->" +
             "#{symbols.join}</svg>"
    doc.output = doc.output.sub(/<body[^>]*>/) { |body| body + sprite }
  end
end

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  InlineIcons.process(doc)
end
