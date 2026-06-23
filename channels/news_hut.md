<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/gGswR75z_nlH8Ri1Y0wd-o0k0yXvb5PTubho-RQISzmWvPLviyTtBBb0m2OrpMZBgt7DShVwajmQRJC8qrQ-6piwouLvVKOQ1GndH4P96b6dUh3xbmpjJxTHwuTofDaSrrDzA-QONZk-QC4DgZ92o-LB2476E4rYocH_zHo0E1U-uVZg9103qiYpC90E4QKjhThR5fFGp2IplOGN6PeVA_g0jI3itPa1CUxW5wdckzLn-3kUxlaYzcodss7edF-X7KlRKlimdWVxRRyPlF9_1XxQ34RR3mbpMNj1uB2mNoU5pJe4kfs2ElhvSrl7KGXp0Z27Kvvlh9TsEVomYRREbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 22:53:04</div>
<hr>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=cUM10HB9biCFz8OktSb3MKhfsCidu56cLYUUarQ1_Msv7uLc1M8n1BsEeOKJjjo2eQrMXNLpgubpFYLjI_C4eO3IFj16XFlCn5WzBFng6yBHTX7a_K6IIvK2PeP7x4DM_9nr8LYGDXRnjxc60Ioq4nOm1uClivgLclO0BIY9QMoDzYUDcNG2AEL3tDM91Wvx1Rpze0htNU8bUuOPMMZi2f4rywzR3ldkge5pdFKl3uGYje9ptYU0g5PYtfzfUYoFGP8RcTAMJPRnM9kdhb6Trn1JUhmI5K5EHgEPJNUokyXJcaahdxLrYZZ-vFJq0rioE83IhllXC0KnvIqSqvi6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=IeGlJKTgWpVihaegopP9rKzRdXEt7KWHglT4ZqNwlgJ96Gltm1lRiLrtYFBh8XwUtVWbfAiHU-OEX55oDyPr-waGk3P1kMA6dro5EU74rncpnGD6LtliyCjhA2GUd1IfgsKleMu38uSowsKiQC_dAWOmyS9VOi2YfddVf_KsNGl1YAUe2mYHByOzEAYwJPVFCMcQu1O64hEJYHeTG0lm93u1Ab-7j_LB66GwRojmsm3_aqN-EkdFklj13avlgs2OjRxeO-WaHOI5FJhIkRQBeS2TZHATywCwUSJ62vtefhO257zam7gJ5E6EvFnAgboWNmIMfmP-wUuZ-wwQWA7Knw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=IeGlJKTgWpVihaegopP9rKzRdXEt7KWHglT4ZqNwlgJ96Gltm1lRiLrtYFBh8XwUtVWbfAiHU-OEX55oDyPr-waGk3P1kMA6dro5EU74rncpnGD6LtliyCjhA2GUd1IfgsKleMu38uSowsKiQC_dAWOmyS9VOi2YfddVf_KsNGl1YAUe2mYHByOzEAYwJPVFCMcQu1O64hEJYHeTG0lm93u1Ab-7j_LB66GwRojmsm3_aqN-EkdFklj13avlgs2OjRxeO-WaHOI5FJhIkRQBeS2TZHATywCwUSJ62vtefhO257zam7gJ5E6EvFnAgboWNmIMfmP-wUuZ-wwQWA7Knw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=ORDwtdeHSLgJBitX-noRS3wk64avsWQkDyXj3hV4OEWlSLlDmBLqf_tiFgEqJclXQqh43gqBlCWXF02n7Ch4n6LDkN21NwrJRTx5vN3_oRKZFTEwP8dVTkcdjxRrFuJEQfBFUPFRg1PnIt_atZ4KNQhCFTx8oBgn3M9wO8xqIbKc0ThtPhQ9fU9AstcqFSQQmtdeDpeuG885gNpZk3nD7mn37oVvkixHA0ajtx-tUSt_y59oCBsoCx4-xuiFqmGiQDTQ8Zk5LrjILU3qpl3OXZyz89Ir0XOpkM6BAvKez7Y5k7v4-VMwOypf6vbD3-zz83F3nFUqqtanP-6VkuV-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=ORDwtdeHSLgJBitX-noRS3wk64avsWQkDyXj3hV4OEWlSLlDmBLqf_tiFgEqJclXQqh43gqBlCWXF02n7Ch4n6LDkN21NwrJRTx5vN3_oRKZFTEwP8dVTkcdjxRrFuJEQfBFUPFRg1PnIt_atZ4KNQhCFTx8oBgn3M9wO8xqIbKc0ThtPhQ9fU9AstcqFSQQmtdeDpeuG885gNpZk3nD7mn37oVvkixHA0ajtx-tUSt_y59oCBsoCx4-xuiFqmGiQDTQ8Zk5LrjILU3qpl3OXZyz89Ir0XOpkM6BAvKez7Y5k7v4-VMwOypf6vbD3-zz83F3nFUqqtanP-6VkuV-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=ioKdt1gFn-q1ysj0HHzhBxulOO8VFcMStzIIM433e6Ryh-KU5OB-hAlYlmdzzgPwvOhdtGc4mzN77BmF_w8PDqXJ_Q9GNfPGkJ3OEIzCNc8rAnc-JJJDNlIAqW922AQZ4C09OGpZeavmqqbaQANvIh18KcGCRoqdXMfQ5ZL9sgVBdI6Y5wMTDuq71VtvWljYGwFsWfTCbMhZ3f7EVxZaTnC31i3LN1kOy7fuqVqS5iVOSSBDsOXXXLRdg4wrpfgiHlv7MPr9OgCMTFBJfm4-Hl7o3Bh37lTKvxt2udzL8gff0rwz49QlYynFhYlQ-GYpNUq3KD2J1plKEyzoKhc28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=ioKdt1gFn-q1ysj0HHzhBxulOO8VFcMStzIIM433e6Ryh-KU5OB-hAlYlmdzzgPwvOhdtGc4mzN77BmF_w8PDqXJ_Q9GNfPGkJ3OEIzCNc8rAnc-JJJDNlIAqW922AQZ4C09OGpZeavmqqbaQANvIh18KcGCRoqdXMfQ5ZL9sgVBdI6Y5wMTDuq71VtvWljYGwFsWfTCbMhZ3f7EVxZaTnC31i3LN1kOy7fuqVqS5iVOSSBDsOXXXLRdg4wrpfgiHlv7MPr9OgCMTFBJfm4-Hl7o3Bh37lTKvxt2udzL8gff0rwz49QlYynFhYlQ-GYpNUq3KD2J1plKEyzoKhc28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=GChVAy2aN3Ao9j-DWCqfQ85HdG04nplVV8HrHUP8qlZA4okm0ig__61ZJqfS6nNYPCrOGAqUd3s5G7ekG3an3sdDafx6akt24eh5i5EEX9S40bghQbUyC45ukfrUT6lyxFvowk495RNqq607Vo0gqTIfI_6E8geZAYVYG9NT1WTRlePyo13ZYa9lQIJAa7Wl2oSk7286f0zigkCG0DYWdyhxWXC2oW6kPLYKztdLju-QWe2OlwZKG-CLu54wwrfMXU0EazytJJNWEqAeLjKCclRthOM1khw8IHzw-9AQ5yA2dMWDTV5vxu7MRPSWC8SD4rL1l68RiE9KWMkMcOvpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=M154quwvTeYLFg_OaCdL7heXOitg6TNs0vpjk-yU3gzYWumPIYZzIvfTQ97QpYTOer2zVqd1dH4j9L5-YiinK1Ty59uxVHK9n8G9ELD9KbtGdnDzFuR-QkvbI59dPaEDk2J0Mvp_3zT9kO-WH3mArMvGxlMLu74EskPImcNqACkDNAFNgqDWNVp-kKTziksEpAVSw00E_LQbI41D12GHejpi_JAKVC4tCewYAziZgftB03fTkkIqRN8LgelWggIhk9gdoFGtHvSNWr8ssj2J5JsCRwnb3a2wueaGsKHbHI5PSJXBrjdAex5KvHNnHuiALSzRMkjP7LUet_20O-Bmxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve7P93zhgyCbzKLF-KHp3jc6kto9hMd9H-eEqTku5rmrhVQm9CiBkgmbkvIF_UJJB2yJLXEpo3HfZfi8_7qALz60J27Kv8arP7mjbYCZBBWnAQR9o41TaefH9_AhJ1M6Z6U77p6k9AYJBVs5pdYF-YyuRGb62-5WYdJTQ9zC9Q7KNaFR5NUg772oynKPbgU37kIYY9b60mEPy43_CBZwV7SmPLUvtzsCOkEsZ2fvHPQ1lPxGjNz7ClMTJdSRbWp-q2pgSpULr4CqTtkAee-0XJdygfsDy65oOSM8wepkkBd0vqblHK47ghK0FcMrR7aSlr2lYGwgrLOr5erZRMWkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYYPR0TGhNcDHvHunkwLlaS294kiOgkRyBiAfEuHeuE4Aw39OrIIMa19exNWnrozECeAMv1hLJg4CpnmI3GJ6pFR7EfykWeZXl9lPNYv8GL38gzQWSpZ_ZRtXqe55LitXcnfKbt0SQMg0-jtMKivfGwniwQEP7s9lCA_gCddVZsYT3Wz_7ZQb6Ow8wgyoge0NiDHuHT0Bmw8DwVgS-xrkdI4ijW9UDEFRKtdoZa7F2y33CdY9hMpABcCTwXqTyYa4-3JmsAnv07knGt6VGGtYxAilY3s30FtVPo05a_vGHS6CVql9dYe6xxirUP3739ODpTXVVmYBPKuyCG9PS4c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=MGCssVA7nPEgvEe0DZIeXKOiItnZuhH5uJubAv3xg97jlelK_0TCAGHbaOoXHKXdPwfEs29wm9C55hTDONHw0e01B7AwaZKGLZJW9iJX0X4Mal5yWTiE1VOY4GbXENxnF-XMIl-dsC4olNkiR5G0ZU8mdgn9QyaEeC7FCUgoJS5-IUIg3lruiIQyMPJ05O8igSDl-ybpcHpF1aMclkfzlI2Yt_BmQfwwOqh1qQo1UlBTr8etCg9hADxwHvz8YSUc3B7BPfPOTuMK8DHjRcTCGn24JBPCDYbALwV_0CXT_dnBHh8kyf-Ufs-rDi7UDOXUHgK3sYVO0tuU16XJkPfTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=nALPpqNIOWkll96fKwOfvgnro5A_UGj5ysqmBQ4_5TF17tQJ0xuUOOMZzPjAclS9Gae2p7ug6v-4MR9SUrHhDbvjnMqaU1cd4HLwP9rTecAulcWmhm-sfWD2iM95pb2l0M9lCTAqRDkLZ2Fp0hCAaTnr2EOJFqD6uqdvPZy2bniEoBfOs1A_ZZ_Htjh4qeLm9fdGFmIs1y8WoAgX5iYWh2pOIggKKZt9Jyp47SQ-_rtTyGBFL9Eh32ujsRpdkOryCNDR6pRIi873b91KOjIQhg0y_99i6q0IM1awS2grVvwtYQ4xgjW0u_13tzwYMwMVwjkhGXq66Gzz1bt1dmtjQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=oTqigYBw3LkRmnkGqM3kUl-n3eBzdML7Nx970_iM1qa4KcCsuZ84xD_C8UEtnKhGNg0gyt465bINdkKOq3qe9kIU4j83pu-LUDF0VmiiHHByuROrd-y1S3kn4YkTPsvNpTtrAaWu6ciBHz2OglzDt8zDbNN4kkMQ-HZEDIHDZlmgpHMpzjBbXyi0WCjJGrVdI0ysd3YydNyKr3dC5E3jfXT-Zd8MtjRXZ7A9P3e4BJCUN-FG_HYz1mAr6GGxuTJrDhFAFi2oGGdt-gqZvWGVXUOS59je71-izIR-dadQMgh1jdo53YBd0Nh_KS21uwGxIUOs3cLs_-9sCo0Ca3ftKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=F3gbZhg_dc08_CykpL8rFmYEBLofWASd40blwy9Shz5AguALFoBId_mXJilQi9m-tP17vsD_M9mywJGbDB4-JEDYj8-sSLVV4Qiopw6OCFcOvJmRXfjtMdQfPsDiAo1uUjNxYYy1ZuCGYqBM8l6WH91z9SZZDk4cBNaltmuBX3t3OIM8erAiol3lh8M-fgnuueNhy6lBF6FHFOdAfuq6CjyjGxWGIdqzl2F2XKL8hw6QOyQt5m2A1tp2uDqcbZRc3C05LXH2BYvlzO1hEGiUBi79ATy3ivGC7ieir33XEMSJlTmhyo0PMHGLIwdyS8CwOWqG_129SV3ckpJb-fqBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzliEQINyK0rc6nS_kzPQlNY1f3JZ3HoxNWll-vU__F6j-5Bjh3WSKmbIyccxHriJd3KhOVXs8tGRmxD6_cdtqEbdXDUP6TADNKOPf_jsflt6marIi3Kmaj3gVzbSUPsXqtFp2wjZjFFpLyBG1xnukATwkZo9s6pWjgTwJu41IHvQppt5WZauYX7HRmnM0hpsFAR03_x1dLUdm5zDL7CK5QC_XGvoCvxIunMqekzfMMIAFARUrPFsoynW497643ZbaTtqjk56GkOO6rK1EE-wkeGyiTsxJtU7_gvaRnzz-Ov1EqrHuRbot7mbFp0ijOOSeRKanD6YezeyAQCaoFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCjAD2IkWHJ2rOzGRvoIoeNCwl1Ty9rAee4S7qxGxfSBQQf4B3h9hAiFQLHzWy7FTY8JXkJ-xVwMPatLVfpe5FGKQQsmdEhqkGolpiZS5QBqKnjOqqcKnbCLuXwXGnvYSdA69BoAqNAPMnGl-6mc5IYISk9CmWSB-ciabch28SAULLX-ypIgnA_TtRelmOczVCRl8F8064tN6f2sdceBY_Wth_MhHzE6VkK9Uizr9gKi01SZ7dF0XygoIDbtW5m6zqm2J-n5XZPKD5NhHisRki9Ad7TyWGodJD_IbGtkS8gj15MqQz13kI7hMHPrR3-laOxxzAcUtbuWlALb_oOOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2n6OjDDP_cAqS76SYdXkYjTJ4T7HchDXQX43WTwvBQyW_A5-GCm2F8qQZngpZz-Q9LbbRRH8uJ-Dq3EecZrt4uIDLFOeSSRCCCj7L90Ob_1hJLtJfP8BVNwznIuyxYWfDIkPQHW9sPs7D3FnWpxGazc5-7pvsQRsD8AheYq1-uVlMl9weBKiBPFrRvjDsH23KZpPRDt_7P-G7z8OV84oV6lUlFmDfR0PNcvCWAecdn7AdswN5xsq5NlvV2gAgbDlgO_RDN-Te9zwn167Ki2Fvq-I9ZraKE4KWnVr3WepL_MhN9yY701umwlJMvFyD_ClxmvLRw1-AATdGLFVIkOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=QRdbyjgDTyxEClYnl6oJcmzS-L8uUkms2x4YyGiGGcF7w7QY8H35WENr-0-xmbMKzmehhI47F5gExKuxqQlq41689I_qmPI6NvA0HW3D2XrOwyiv9pjZjjN3tzJTbGfp6R70z3DtN5pl4lP3Vx9CAuNSxZSS_FX6RSj43U4HPEtt-mAWUEjMVgzICVBLtUI7-PejoL2IruUzmWK6sf6sZqMFBeC5tSLHKWaOVIxmA0umEoR07nb9ZjlYehaBjqEztI94-7rWr-MXFU5SlyEzULhdjlpcPnzk9UpsYYFxiNS07FjRX6v5Roq5oW5CyrmOkcjcN1vJIh7V5kgUKH_xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=P3RvcWwCmr4B1din1mLe8uHjiggBp7I6JnYBQ_wsiE5eY4wKMKtge9-gSxKZL9EBH-t5YFF-lkkjmMdOLLZTgkp_ab8ljMHcsdsPrDC14quuh99uq_R6xtIfwCFujr5bTqzQYjKcSiF2INnJj0S_-CDoK0Hw5so66B1rMak-UxF1-z5SuWOs49YyJXMvlOJMFlEbQrdcOE5y3-Ej_VVCtVCaG6djP49Nz0GV5gC91OLVeNfiXX5iZyLX_FKqoC9prhsTdosUOty965BSqxVfQD_KJMF8oAxf35Eu8-RQg8DwCe--nBwN3B0U3ITM4qUdc_P59KmcuRg8EcLv9Myybw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=P3RvcWwCmr4B1din1mLe8uHjiggBp7I6JnYBQ_wsiE5eY4wKMKtge9-gSxKZL9EBH-t5YFF-lkkjmMdOLLZTgkp_ab8ljMHcsdsPrDC14quuh99uq_R6xtIfwCFujr5bTqzQYjKcSiF2INnJj0S_-CDoK0Hw5so66B1rMak-UxF1-z5SuWOs49YyJXMvlOJMFlEbQrdcOE5y3-Ej_VVCtVCaG6djP49Nz0GV5gC91OLVeNfiXX5iZyLX_FKqoC9prhsTdosUOty965BSqxVfQD_KJMF8oAxf35Eu8-RQg8DwCe--nBwN3B0U3ITM4qUdc_P59KmcuRg8EcLv9Myybw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHp2-wGNjnv8nQVJhJjgWs2wHaTuFb7HMsfYJxK9OGSCRzD97VjrfaP9zVcj1FtIozoItn05ilBgf20HDJquF5-ElNDx5JON0ik1xg8vftPqoBVrZS6W-RIeaeSLZxrhCoQw8Wag3Z9s6gmiFPsTAMF-TJqIh5t22nxNIgjor7FZYQsqcuTSXXMu3_mzkNDv8llbPcK3rBjh2gGp3beoqYMInr71_Jbd1bvseXDHL1Q8GGi6MWEuW2rbYpY6NTwQu1xHbEcM5NSDC2KDX0qbPEkwoLU7cH5vRMK5FmqSUsZDilZkiKkCKW5nSairaqoZRepnPTwa7XkOPLeE_WPFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=J5mzAiA7No8_fnqQLUJSo457VbzYjeCFSOmZBuDZQumyK8z4FWeR4LIgk4JtSHNNQxJ3HuWANMia8SOO2I-iMqG9ZH96aVMITWm3Wx1UsbJnEcKE_bgSzO4Opc30klpwihWAoe50SaP2-u5wzj1WgrWRRGFGYi9G3Yo5MAzeWdOhZBUAEcb0MFS_0yzf6PluxQ_6oySEjkWWxkEXre6dW93Cq8fHueAE1Wq2eDV65wMNVuzr8srBEfCreWcPsad4TgbwvODhh0ZsuKxj4iQmxZhcHBAQvqToiJlQ3Lpvq75EFEubO3EM2VsAS8DB3cVP8rUtGavyxYjqlLiaBw8ImECseGHmVFhZ-3czZzhraKPsdebMMjYUWEKSEVMjUpwqJxT8a7a3Ygnt_Mb7YLfVF7ih7XK0LOdNM6Mtfdt4WNBlJP6JRrpVE_XLUf3LdlxIgw1K0oaUQ1kttyoE0URDMW5hl2CPbD_-jmJj8klhdXB3nF12pydvvdFdWP5RY0BkBMUuTHjMhzzIYBigBvlxofB2G5SEGAG-U6oHrBQj2jfJnfHDx3gkWgCoY1xoqlSkFsoXLW0tBsr_H6s52HOk1mitU6libp49pafxKhR1GldFrop4rnB-jbc_rCku8-7hnd_gGmKAYxY9HFXfr9vFAf8V8rT_ra6gJZZ6ExnZ6Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=J5mzAiA7No8_fnqQLUJSo457VbzYjeCFSOmZBuDZQumyK8z4FWeR4LIgk4JtSHNNQxJ3HuWANMia8SOO2I-iMqG9ZH96aVMITWm3Wx1UsbJnEcKE_bgSzO4Opc30klpwihWAoe50SaP2-u5wzj1WgrWRRGFGYi9G3Yo5MAzeWdOhZBUAEcb0MFS_0yzf6PluxQ_6oySEjkWWxkEXre6dW93Cq8fHueAE1Wq2eDV65wMNVuzr8srBEfCreWcPsad4TgbwvODhh0ZsuKxj4iQmxZhcHBAQvqToiJlQ3Lpvq75EFEubO3EM2VsAS8DB3cVP8rUtGavyxYjqlLiaBw8ImECseGHmVFhZ-3czZzhraKPsdebMMjYUWEKSEVMjUpwqJxT8a7a3Ygnt_Mb7YLfVF7ih7XK0LOdNM6Mtfdt4WNBlJP6JRrpVE_XLUf3LdlxIgw1K0oaUQ1kttyoE0URDMW5hl2CPbD_-jmJj8klhdXB3nF12pydvvdFdWP5RY0BkBMUuTHjMhzzIYBigBvlxofB2G5SEGAG-U6oHrBQj2jfJnfHDx3gkWgCoY1xoqlSkFsoXLW0tBsr_H6s52HOk1mitU6libp49pafxKhR1GldFrop4rnB-jbc_rCku8-7hnd_gGmKAYxY9HFXfr9vFAf8V8rT_ra6gJZZ6ExnZ6Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=qyOPrM3GO3TWzX-xkdMK0IATCl2p-u21mf5xGh1JZk27d1VqPa2Ys46SkWQz4Zj4C7ejXO4R5-dhNMKY5DEmIYdgm7LJv18uR-bJlLfGsxf36OHth74J1eKRTS_LTJRr44oJb6pCnqtxprEq2I-tD_jKdN_yxSnBYKjO6_bTTqzgVAoMWjjShoeYcjqJLBuFGIiBHorUB_ooC_mDs0AZJxV5uxNCUE4sjNUu3hmWz8uYy7SVqgewfrxQxmyNKnKDS_yFTIq6t4Uw-IxnJMUsI9Bo1y-cySy2NsoZ2WanyrhmX4MVwji9YtAjESXhfrs82wZoaZo1SrOGMqoEbPwtng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=qyOPrM3GO3TWzX-xkdMK0IATCl2p-u21mf5xGh1JZk27d1VqPa2Ys46SkWQz4Zj4C7ejXO4R5-dhNMKY5DEmIYdgm7LJv18uR-bJlLfGsxf36OHth74J1eKRTS_LTJRr44oJb6pCnqtxprEq2I-tD_jKdN_yxSnBYKjO6_bTTqzgVAoMWjjShoeYcjqJLBuFGIiBHorUB_ooC_mDs0AZJxV5uxNCUE4sjNUu3hmWz8uYy7SVqgewfrxQxmyNKnKDS_yFTIq6t4Uw-IxnJMUsI9Bo1y-cySy2NsoZ2WanyrhmX4MVwji9YtAjESXhfrs82wZoaZo1SrOGMqoEbPwtng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=HXGUyu_EPKo6iVRw423Hz2uZC6qdKYvlmisuSFuo8zkZyo6ajMykQIxqjWMjGGXAKuwKQ90_duffd6vStxzMFF3B_eNKsWN0uJQyEnwr0Rii4uY59uDxAICJyMk_gfPp-zVjswGQfpPAc-la9yU-ZW-x2fEjEvSBpTv6Gif-IDC1ppcZGVt2KWe2KQxF9XndVxQQpWZgwZOtvAW89ywlv_GdKRSBZZ0xfzGtLjetbfD1tEP7usncvgRemjhy4eKZoOSaJUqDG22EZiRwraViycgdCJYnTRQ0EZmyCKcskmaOoqHW7LJd2rze9G7P032mhvMNHOTpDp6QpC_m9o5fRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=HXGUyu_EPKo6iVRw423Hz2uZC6qdKYvlmisuSFuo8zkZyo6ajMykQIxqjWMjGGXAKuwKQ90_duffd6vStxzMFF3B_eNKsWN0uJQyEnwr0Rii4uY59uDxAICJyMk_gfPp-zVjswGQfpPAc-la9yU-ZW-x2fEjEvSBpTv6Gif-IDC1ppcZGVt2KWe2KQxF9XndVxQQpWZgwZOtvAW89ywlv_GdKRSBZZ0xfzGtLjetbfD1tEP7usncvgRemjhy4eKZoOSaJUqDG22EZiRwraViycgdCJYnTRQ0EZmyCKcskmaOoqHW7LJd2rze9G7P032mhvMNHOTpDp6QpC_m9o5fRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=P0zxPvWG1C-fokqoonGlEp9dBh1sseOmx0kMsh1gCW9NmKqOabNRnzMEtTWhfi_VfLTqK3DJM-ttIq_DVFXx2rD0l-nWP7UaVuml6zFTkHGVHSSZKqyAQz9dF337V8ua78uYZT2Gc7eThc3ZA-ZorkuusqdVHLFyJo0-tdjYmdFxQjmJH3V5SwBkP3pW_C0P15mJ9gFke-7OPTZAG1foEV1VskTz9VGA5Oo4j1p1Qv8e58G2vkyfMmlgM_nsSGXWpTUjiBclTu4h5DXjCrmQL56Fe7N_EnbAbY3HD8R3T3filFh290ydFzRMUTfS9KnvOht5dYyv127r-Aqn7ekr4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=P0zxPvWG1C-fokqoonGlEp9dBh1sseOmx0kMsh1gCW9NmKqOabNRnzMEtTWhfi_VfLTqK3DJM-ttIq_DVFXx2rD0l-nWP7UaVuml6zFTkHGVHSSZKqyAQz9dF337V8ua78uYZT2Gc7eThc3ZA-ZorkuusqdVHLFyJo0-tdjYmdFxQjmJH3V5SwBkP3pW_C0P15mJ9gFke-7OPTZAG1foEV1VskTz9VGA5Oo4j1p1Qv8e58G2vkyfMmlgM_nsSGXWpTUjiBclTu4h5DXjCrmQL56Fe7N_EnbAbY3HD8R3T3filFh290ydFzRMUTfS9KnvOht5dYyv127r-Aqn7ekr4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=gl-Zb9OD1yZa0MB6b6-Ux3fS6bs2B_Cat_vA3i9nel76nOznNSFle0pL6cg3ZZ9TFdThmGLuUkBvV1QU2eQWD5bxQEHHDtGDHKDj0Mx1Gtdel1akOqEhVQYmi3eeHAyUYGvnlgQJZjJVXMfGfKDdEZzyknUhazUW2UASuIiM3I4pnGqxFfES5QiRKYQOxFtRloaUqSMWxnVycZfAePaRDtel8YT3l8evzbkv9yoY4BD5ahrdiAH0iuNw7erj6zYK7QS8IE_ogrUpQtEemOLhAGV6Ilk6YNWu1XfC7YoZe1ZW6qMR8q4zbDUJgfMQYpE2B4KmvqGWPLiwx2e5hb22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=gl-Zb9OD1yZa0MB6b6-Ux3fS6bs2B_Cat_vA3i9nel76nOznNSFle0pL6cg3ZZ9TFdThmGLuUkBvV1QU2eQWD5bxQEHHDtGDHKDj0Mx1Gtdel1akOqEhVQYmi3eeHAyUYGvnlgQJZjJVXMfGfKDdEZzyknUhazUW2UASuIiM3I4pnGqxFfES5QiRKYQOxFtRloaUqSMWxnVycZfAePaRDtel8YT3l8evzbkv9yoY4BD5ahrdiAH0iuNw7erj6zYK7QS8IE_ogrUpQtEemOLhAGV6Ilk6YNWu1XfC7YoZe1ZW6qMR8q4zbDUJgfMQYpE2B4KmvqGWPLiwx2e5hb22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کریس رایت وزیر انرژی آمریکا: آلبرت اینشتن ۱۲۰ سال پیش مقاله ای منتشر کرد که...
🔴
ترامپ: برای هیچ کس اهمیت نداره
😂
🔴
کریس رایت: به نکته خوبی اشاره کردین قربان
.
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=d8Z6JOhf3cPwszXuE1-pOmP4gxgHPKhhdQpspCro3sjQFiadx7TNkToFLEfh0JupCYg705yevol5jrZqkzuc_cVscJTN_JFUT74cbSO9Izc0m29fgP2ySwkWMKfmLemXxYWeNkgSlTF8wmjNszf9uEx4_S7wu_M259X4rccDd5aBs6iK5ro8Y4LAHFz-izkhy0_XvuRYN0l-I_rZXIjWuNj8GIIdZYXlrK7wUUjg7KdTNUDnbGyEwiSwPX4EiJ-dIv3PufqaxOdw-OJ6CSHemkWWxr-tQ2H_cxVzbPXTKg3XhuaHhJgTwekigr7493T1zqV1FjDNPX7WDJvBP0hUhrjigW83xpOszoxCp9gCA4JXBn66nFnK8uNEK076YRlUPYTh_kWxGGJyeMf2f6YxdcQRUJ1G6Wd4yJ2rThAhIPG_K5gHKT0JcytEb6k5J3pJU9dk-m35BxaHlTB4g030cXXSTO39qurtRGzovBmLcCc8kmhFoU_K7n6s_EL0TQr6kwLclvmR0zkl83vwhr2FNANlCcCW3DbOITBez6ArFREN6zOV7QYiob4YYmEQqe7yWAI01WKubQPnJelPD53UsC-Ei2ergESKrH3AzJTTcnAqlAp1OWv0EbjVqtnmS8GjQYty6qbSSQFUvzT0I0XUyD-0xCMliv85omHGjjsKfTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=d8Z6JOhf3cPwszXuE1-pOmP4gxgHPKhhdQpspCro3sjQFiadx7TNkToFLEfh0JupCYg705yevol5jrZqkzuc_cVscJTN_JFUT74cbSO9Izc0m29fgP2ySwkWMKfmLemXxYWeNkgSlTF8wmjNszf9uEx4_S7wu_M259X4rccDd5aBs6iK5ro8Y4LAHFz-izkhy0_XvuRYN0l-I_rZXIjWuNj8GIIdZYXlrK7wUUjg7KdTNUDnbGyEwiSwPX4EiJ-dIv3PufqaxOdw-OJ6CSHemkWWxr-tQ2H_cxVzbPXTKg3XhuaHhJgTwekigr7493T1zqV1FjDNPX7WDJvBP0hUhrjigW83xpOszoxCp9gCA4JXBn66nFnK8uNEK076YRlUPYTh_kWxGGJyeMf2f6YxdcQRUJ1G6Wd4yJ2rThAhIPG_K5gHKT0JcytEb6k5J3pJU9dk-m35BxaHlTB4g030cXXSTO39qurtRGzovBmLcCc8kmhFoU_K7n6s_EL0TQr6kwLclvmR0zkl83vwhr2FNANlCcCW3DbOITBez6ArFREN6zOV7QYiob4YYmEQqe7yWAI01WKubQPnJelPD53UsC-Ei2ergESKrH3AzJTTcnAqlAp1OWv0EbjVqtnmS8GjQYty6qbSSQFUvzT0I0XUyD-0xCMliv85omHGjjsKfTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=mVGU1be6QjWiGPuXKiOkMuNHaKuuBJYFMz0uqGtoOexy-aWcLoHgzP7mYfu2IsIlqIgEzQzc4hChYEmiuMBhUEnhqshus3TbqOtIIBaUmoxzO5W9ooPHsCa3e5tmQMo_DqcOIuBod1FuXRdLQTzo1Yfx_dXdqHEpbGCSN7CC_0_96p6KaqAa8Q58qE098x5ymcee8fMWr1kQYv2eC8ZgmR_e6uqGj4vNa9w8V2Abi9sUMvbvXcfNHUImHOAPmSWwplG8UPlOHgwqr1FXxxoYGB26cDTggAfHdsWce-LFl7ph6EP25ML8dSLWmXQ8XhED8FeIS_Z4gF9P3cbbTB2bXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a355cf81.mp4?token=mVGU1be6QjWiGPuXKiOkMuNHaKuuBJYFMz0uqGtoOexy-aWcLoHgzP7mYfu2IsIlqIgEzQzc4hChYEmiuMBhUEnhqshus3TbqOtIIBaUmoxzO5W9ooPHsCa3e5tmQMo_DqcOIuBod1FuXRdLQTzo1Yfx_dXdqHEpbGCSN7CC_0_96p6KaqAa8Q58qE098x5ymcee8fMWr1kQYv2eC8ZgmR_e6uqGj4vNa9w8V2Abi9sUMvbvXcfNHUImHOAPmSWwplG8UPlOHgwqr1FXxxoYGB26cDTggAfHdsWce-LFl7ph6EP25ML8dSLWmXQ8XhED8FeIS_Z4gF9P3cbbTB2bXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شهبازی، مجری مفعول صداوسیما:
طبق تفاهم جمهوری اسلامی و آمریکا؛ از این به بعد شعار «مرگ بر آمریکا» ممنوعه و اگر کسی اینکار رو بکنه دستگیر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=aIiufz0RrkQQGSVZqip94a0co999J42rUTX_CZmCj8WjQbMo8G3R2DEshlqDxrvgVfz2zVQBsPqBlW5u18dIlpvxLpDyYYQ-yEDHbWWYUFfHzdOUgGKgPChNyWXKB11nRjp7RD19tMfPiUCR6b2r-49ujsfdoWWUrDlNeApvsDSB6nUk9pBtjl6BeYIWJDG3t0-uYxs19NceNbOHWCou8coOcRxBCTMi2Mu6kHT_onQD5sGHWCarl7j7jjeFW8q05wAzKeYgVAvq0GoWwR1G94KGjKpD6fFZFQ73-8FGc1Cn99eZCZIiWJZXEACejOG-3iNJwnElvZnVpyWJNxSSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ce9206e1d.mp4?token=aIiufz0RrkQQGSVZqip94a0co999J42rUTX_CZmCj8WjQbMo8G3R2DEshlqDxrvgVfz2zVQBsPqBlW5u18dIlpvxLpDyYYQ-yEDHbWWYUFfHzdOUgGKgPChNyWXKB11nRjp7RD19tMfPiUCR6b2r-49ujsfdoWWUrDlNeApvsDSB6nUk9pBtjl6BeYIWJDG3t0-uYxs19NceNbOHWCou8coOcRxBCTMi2Mu6kHT_onQD5sGHWCarl7j7jjeFW8q05wAzKeYgVAvq0GoWwR1G94KGjKpD6fFZFQ73-8FGc1Cn99eZCZIiWJZXEACejOG-3iNJwnElvZnVpyWJNxSSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
ما هرگز نمی‌خواهیم با آمریکایی‌ها در یک قاب باشیم
میانجی‌ها خیلی اصرار داشتند و ماهم گفتیم در آن قاب حاضر نمی‌شویم و ما فقط برای مذاکره می‌آییم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ornw1rgHu0n0UTymlpzrsPJQY-LiDGh7QQ9tt9f9l9qyQv_jOaDdWJPhDuPI9kZjbusDX4WiBwWkyhxi15_PVKZiUFMhZSKr_cALvm38Sn65dNdyDc-ijnb5Vqfp-tVn7OIPksAlLfDfUyhy_LuB7gaUWsLPIE2up7gMrVhAlLrNtu24W2FZ4Co6Iz9uoDxtXADACcQe70-5KYVTOB4utlqn5gTeOAIdFJ09_FrCVyOGdfShdCqKlec5Xh7lBz4xi6CBObH8bz5GM5mT6bS0065OgFLjdMeuHAqsUFiTTTDnWKP6ZJr1bbfsp4bWJEPFCECrznANNDVXcJreif7rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=Ij79hN8uue7NI4zX4AycypaqTIG0fg_q54-2MDNac_zgD5OFP7NLsjK4MQNaXgIOKeVVgZVIofFX2GCvDXVwhbsCj4_NS687XjLEGBPhIQcn1MQQaMAuN56MisHDL3fZGdxvBJ0wlQncS4VEt79JQ8ODtdAe_SNDNDEetuUeRijgv6j23XjaHfefcSowHgpljCB4sYaHx9u68E1Gi2DGoLLQRJGuDLyb16J8083a_no38yRCnW0uLzc8ykQrgCfkT8U2cVe91vGlMTFSdOmlqPD_nREmyUjW4n8KxU9zzMoAN7KrP8wiX9-vemXtOjhSPKCqoSOZ0dMbdBC3Xw7BcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=Ij79hN8uue7NI4zX4AycypaqTIG0fg_q54-2MDNac_zgD5OFP7NLsjK4MQNaXgIOKeVVgZVIofFX2GCvDXVwhbsCj4_NS687XjLEGBPhIQcn1MQQaMAuN56MisHDL3fZGdxvBJ0wlQncS4VEt79JQ8ODtdAe_SNDNDEetuUeRijgv6j23XjaHfefcSowHgpljCB4sYaHx9u68E1Gi2DGoLLQRJGuDLyb16J8083a_no38yRCnW0uLzc8ykQrgCfkT8U2cVe91vGlMTFSdOmlqPD_nREmyUjW4n8KxU9zzMoAN7KrP8wiX9-vemXtOjhSPKCqoSOZ0dMbdBC3Xw7BcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91eda4547b.mp4?token=DhkFCvfD7h0I07Tfa5vi4kut-KwA-1OpL9L1d5fA9ApfPKzaug_8qDOFa8Vy1QYTOmYNKex7EBi_NCS-Sg9TKbboYK4P3ETORuMu7ZF0uClHcw9CzS6JJGaQGcNkEqZ-Q3lK9s84dFZbzNYsh7sg-mKjNUchG80mnUXm4cz1dHI7w50eGcmmHdMlansJb99MVo_dGiqiMWXmQm3iGPZUdkqVLWhcvI59YKiQeBG9pUY8CyQF0sa3tFYI2d2aXhzrXl8Psi7rJprJTAnIqDks_uuU3j1oio6gheOLLM0fqQbtzUFfUag9BVCegYzDM189RoJWJzX9L0MHLOeKujSBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: وزارت خزانه‌داری امروز تحریم‌های نفتی ایران را لغو کرد؟
ترامپ: خب، من باید دقیقاً وضعیت را بفهمم. تمام آن پول به صورت خرید مواد غذایی برمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند که نمی‌توانند آنها را سیر کنند.
خبرنگار: مطمئنی ایرانی‌ها از سود حاصل از فروش نفت برای بازسازی ارتش خود استفاده نمی‌کنند؟
ترامپ: قرار نیست آنها این کار را انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-XoIS_pbsgGs6ASTn1IjBpe-KxjXseeODIGeeGb5JZZq2VhVSUGCC1W-ZwxgF2xeteVF3_5UKrynzbivP_GD_LwegVzNybNHhThKVhiIjlmjp5PXZ6NgV05Qf3Ca4c7kE6XXKpCWr4pOVfd2jQe_Ema63QYhK7HIgpnZ6nQbWuFF9jdbcnF_5x3FEHeJ5JGdXnY3w6jDiCkioViKjx6rQWOy87Z3ansifr1r9vSPjqXxNv69YTabikv9NFZ86vDB2-Qd3MJLl7_Kc5S5mMkEjzW9Ta7qm-OzYJx8cGNuhdy2J8K3T7rCJFrivhOmrFyy_lOaMNm_D67rC9mm5GXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=pFjwqxgyFIJWzmyL3Q0dsu9GFXHYJy0v_N9TxyYIxbMOy322HFurmK5yG2n5XXHW5HOHoK4r8pEwcc7lzDecXNEGB1lHZWitsrC4Cm66Gcc9tbbj_t9eYOrY_BJdrflApx7otS5v0BS8BChWAiBPDf4DwWu-_HOcX3l1mipVhME1Klm9MTLYWKQQha7UklUrnWlOl1T58RMhWj948buwpAZw8JponCgsRc8mbjIU2R8qX7nwEZUvFLxNLycPRABJJCjjzXl7f5Z2ABQcRT7mH1txYEW12TWtaPujtuzt0MbRvqhfdsXyaLGsearDk_ZktYvOH133d_sU9-Vv-51uWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=pFjwqxgyFIJWzmyL3Q0dsu9GFXHYJy0v_N9TxyYIxbMOy322HFurmK5yG2n5XXHW5HOHoK4r8pEwcc7lzDecXNEGB1lHZWitsrC4Cm66Gcc9tbbj_t9eYOrY_BJdrflApx7otS5v0BS8BChWAiBPDf4DwWu-_HOcX3l1mipVhME1Klm9MTLYWKQQha7UklUrnWlOl1T58RMhWj948buwpAZw8JponCgsRc8mbjIU2R8qX7nwEZUvFLxNLycPRABJJCjjzXl7f5Z2ABQcRT7mH1txYEW12TWtaPujtuzt0MbRvqhfdsXyaLGsearDk_ZktYvOH133d_sU9-Vv-51uWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=fBqj0RRJj_xZpcsLKUy6jaQbz2aSFgy980zzO7xs8ZSwwR1Kdq2FEtetkWnkg7rgCwspk0_ZivKlp8ZSNhQio-7qOdhoWQaAezb0wkkK5ZG8vSLnHw4Gk1vycxPDy1ixfFph_c4GOAXxEUGwQbXogXTpaZzejuYPdWKB4FmKn_JFvYkNYMVuYnQyTaMNUS386a_lff2fSCwpjDhE72yDRIof0SfWiIZ6upuIfzklRITO5ktOa_ZcjuwxOHJVEUeMHgqPMZ1J2CfNiizBoE23NpRN2uro6CKf4tVHC5-73qTOv9B6IDpEHK0wbDv8VkdEaZJCaPnRxCbVvTU0zyb5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=fBqj0RRJj_xZpcsLKUy6jaQbz2aSFgy980zzO7xs8ZSwwR1Kdq2FEtetkWnkg7rgCwspk0_ZivKlp8ZSNhQio-7qOdhoWQaAezb0wkkK5ZG8vSLnHw4Gk1vycxPDy1ixfFph_c4GOAXxEUGwQbXogXTpaZzejuYPdWKB4FmKn_JFvYkNYMVuYnQyTaMNUS386a_lff2fSCwpjDhE72yDRIof0SfWiIZ6upuIfzklRITO5ktOa_ZcjuwxOHJVEUeMHgqPMZ1J2CfNiizBoE23NpRN2uro6CKf4tVHC5-73qTOv9B6IDpEHK0wbDv8VkdEaZJCaPnRxCbVvTU0zyb5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=BXnx8JHXvcS5JIy5XwwvL1bFziLbW-sdh1KQ1sDp_b1xhGAb1xnYHPZbpTEzLBDiGYOsC-zv2inoBM9qI10ZILr3IeZNHT_9IIIJ51DXwXMsX-zUrfTkfa-H2Trte2_Aj7Fwi1MI_JjLEb-onT-igKlFWnQ1pF-GMXUa0r2u0IoSEzec3JZszZ9IKfQ3NVzK4Z71m3FZzIEIjr3-Xtj5PptBg4HwKmFrX3d-cZcVz3BvTiQ6YUKck2uo0Pt4Q6gJD9YYx5oBWJoNtrGbKVGH3Vv-BC5N_1BaFztI-EpRdmWwdL647JufQGu1X8CY7UoNPolP_cCnT8M1Dw8DynjslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=BXnx8JHXvcS5JIy5XwwvL1bFziLbW-sdh1KQ1sDp_b1xhGAb1xnYHPZbpTEzLBDiGYOsC-zv2inoBM9qI10ZILr3IeZNHT_9IIIJ51DXwXMsX-zUrfTkfa-H2Trte2_Aj7Fwi1MI_JjLEb-onT-igKlFWnQ1pF-GMXUa0r2u0IoSEzec3JZszZ9IKfQ3NVzK4Z71m3FZzIEIjr3-Xtj5PptBg4HwKmFrX3d-cZcVz3BvTiQ6YUKck2uo0Pt4Q6gJD9YYx5oBWJoNtrGbKVGH3Vv-BC5N_1BaFztI-EpRdmWwdL647JufQGu1X8CY7UoNPolP_cCnT8M1Dw8DynjslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=XxoiaJkN0HSOfouzdUZS4vuYJPkQXgPcZqzQoxy1J2VEN9g36XQfecs51rrk3fNSWG3LhT-LdWZLujNntkxEMsXeA-hTISGXIZyxz_qfvu-nuIoveb7CVmyaVBrexK7Kvv0Ue5891jRf0gSi7Ksr9sbyh3hF7v15mfTBuPt-nrBmCVN8eBiwbE7hldtkFM2kH03f_UTnxHE8MKhFZ9FN40AtDAsf7Zg-nxUlABxPAbb1AlgC94X65ayWIhWMlB6OLkPpQXjPPnkOsJO6ib-lUYkTqHOQSbARDZ3wgr3TpEh2rlIIHykceAo8tGZTshyowMSSWhDFiYJDPvHw7f7kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=XxoiaJkN0HSOfouzdUZS4vuYJPkQXgPcZqzQoxy1J2VEN9g36XQfecs51rrk3fNSWG3LhT-LdWZLujNntkxEMsXeA-hTISGXIZyxz_qfvu-nuIoveb7CVmyaVBrexK7Kvv0Ue5891jRf0gSi7Ksr9sbyh3hF7v15mfTBuPt-nrBmCVN8eBiwbE7hldtkFM2kH03f_UTnxHE8MKhFZ9FN40AtDAsf7Zg-nxUlABxPAbb1AlgC94X65ayWIhWMlB6OLkPpQXjPPnkOsJO6ib-lUYkTqHOQSbARDZ3wgr3TpEh2rlIIHykceAo8tGZTshyowMSSWhDFiYJDPvHw7f7kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=MBubMD4y1o9cKBGfxypH9uCSKC2vm-iglRDCzzCJCiUiW9XF_1q_NPYeeQNvI91JrPUDPtb-_PXn8Ffyd6DpIBTDIPFa8R-1YmiL9ntNchqakm8U_-fLNx2e-2gHPgiZrYvDjEbQ4o5PlPNb75Z1IZqfIZcjAjynKNXq7BHg13iuwtXc5o5CL2u1UafOVKkWM7hkFgV9mlEPxrE7IDRq6aH80SzOHG24ju6yYV0jMGCenyPCdGqrdep5zAx8FvwPN4Nk40Py355vOne0q8MbeQEe8BFRXlX2owHzOuHtFHCbo7Z-hgZknJxIKFw2-jOvKQy4Ge-dTJbrI3TInWO2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=MBubMD4y1o9cKBGfxypH9uCSKC2vm-iglRDCzzCJCiUiW9XF_1q_NPYeeQNvI91JrPUDPtb-_PXn8Ffyd6DpIBTDIPFa8R-1YmiL9ntNchqakm8U_-fLNx2e-2gHPgiZrYvDjEbQ4o5PlPNb75Z1IZqfIZcjAjynKNXq7BHg13iuwtXc5o5CL2u1UafOVKkWM7hkFgV9mlEPxrE7IDRq6aH80SzOHG24ju6yYV0jMGCenyPCdGqrdep5zAx8FvwPN4Nk40Py355vOne0q8MbeQEe8BFRXlX2owHzOuHtFHCbo7Z-hgZknJxIKFw2-jOvKQy4Ge-dTJbrI3TInWO2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMzH4pEmJJ7IaPKbhUuawGI2tlT--BQ-Bkq_JRLZNIy21y5DxHMTY2oyjkYPqJMzbSZILMxtrqEEREZAyyEfls020U8lmfAVrUASY4yi2RCmvtFXX6GndzpzKx3Qw6NIoM_glLti8pDGooGWRZtELWe7Zk3KIcnY0bC1QEBzLcg_NGbj2cwKjeFTq8bNJ0QTfRssFWuy90OB4xLNSjBKabQWRe7bD9vLizvvoh8Ty7s2slwNtF-VzLrW_MbM5-amqzAB6a-VCfInEUKnEEHeH2gV7PfL3edeXPioenBnfcdSRb_QdxPqeyae7TnXhGOKb8zgPU4BUGiVFXK3UtL0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLucRNRccTGSlZL3rnnFUebf9lWm20otu2arTJaYkhdDKK9ZxxG7DV5DmmeE34tgTGDFVGPUKclVUkY6AQL7D1VzS-y9U6hEOAK6FTnmmPtkQQWjbkSkt-gAf6EcsrBsGBGwpMRt3swtiSZdqOdf3T0pXuPnyG7ZCfMnu_nubvXgQl3Rh0h09ZbAsDxTM5tqBa_jTXNWXmoRJPBpuODJGwtrcvBC-XjTls_v6XRura_0KLdZ1U1Em92cOquTKK14VyUzG5ZYAT_y7h_OwXsdh85WX9Picip6K5kSTEFkAST3kfozMW89NS3OUAokBWNw0pgcxeEPDnEh-QF1gDgU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpgRfHD5JUtxy41aDt0HY_ii9WJQ5ZxIox48BJEpwQpg7EVc_-Kt7jqzgQbf4Ft5Cf8lS6hezkEyIozxpL-djUxzjmrSC1VYyHAMS6aLbtQ--_qo9_VEa9DY5nRYpndn30JFYWFEzvqx9W6h5WaE2Fbtn3ERuU6t6fGgdls1OFd8_j_3cZm34cCxqFC08aPruDizm9mmuOTngnOTklNJSYIITWdPYPBJgGvLqJo83xDKFTibttU498vvxA_iqrnK8r1CtGwsVXbI7U5AbqB5iQconitjC6M1ZLeiMuiZpaY0lCYgA51wfwkiIyA6neLfwRGVI_gqWt0ukM9zlC-xEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXsZcGKDm0NQBGLSJBEiXi1kLQ7ZlR3lY2Sj7xg0iUYtLl1n4nCi7dPOI5qqxyuKXBc_m5aHA1gKiRvfV4QHEJzrZ2SqILTHYuoQttKBHNt8mvnqQObXk3XJ0gW0vgWL-R15VSjCP8kHZ7p9ceFXcURwuzkJOZxI7tLW0RffmyGoEdjSyCxMinJ3Qp3nRkJUucx45KKFnq1osaEDFdvZgsRE_jPjtE2BWBs3_XL_BKiAgEb_5_p_5OUWrl7Wi3XGCbl8UEEWiVwx6yctHGjfAzzO-bJ2ylmVOooVOXTtbx_5k5WlGTKJCOJzwhUsBIijxD3bVRfNECNIVR_Todk8Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkrn-ttymHHzmakJKWeTGe22V6O9EPw5mLbjbmOOvVSCWc4cbtRAaMxPy35TDbYOwiL6I4xUrBlVPQQoQp5-NsjYwAxQVDcuXVE92VfVELHjXEuf55nfJ-U7DD1kHCuM4lnjY2eusZ9IY3retEy6g_2lNLM-eASeyvIo3vPIZPDTryuK50K9HGqvEHjSxIbhPTZTYdqpS1Spff3As1m1O4tQnUSRD2lH_UMUg7HxnMpRmng2fpkXnoU1UpcIAoXKivj1MLPYgIPcy9Fw7hgMy2t9pKb3ICyT5WmHIhSolKAzhzxlYQNG0Ooe_ypqUKdCyTQogKIeG0nXdwU3RaDR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMltY5Ok3gGXsY_Q810TtZo7hSTpTNmdaf7rNqG8J4pzroEuKRbmN6y__Y586MfDrwCyfQcghkcja80Euw13XZnZdDr8jehJs5NMpBqLkSwP3VLFfYzvf8idDEGCK3-gi5Fymp1zWSkqN4IxxoCzIeUy1TUHqXn7hAkkFbkRWfyW7f5lcn2T5a793jwVkrVJJEFFtNIFltLxTraebRx0KO97te3oQfJFkne1NwECjAp0vhcuYJkGHXo_zW0aYCRDr17d6NV7EuFQK5tgR65rMPfDFAU0kpdUdsDSp9BTyzdSU0hOR0eFR92aQOAThxAaIo3yg7i9UAKU7zq9sQlZ5EOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=gVTg9KOPF0V3ZK08J6r9qD-uljwxSBMUOsOC9Xeo5tewLfEA2y-O80zowdjCaqIwceVQ3LZcF5kwIcGd6TPD3pvlnCmMb858OznZ4CoqG5TBQQt25J6jcCotNRNbRG9e0MvzxQHuTecJaP-UO-O0ysUDzRCNd1K62K4OUT5oVs4c_8Mme3LjECarwTbyRUIeu_RQ9AFNC6TOjO9oK_GPeYCztEeZ3qwJ2tu-rjNs0LMyyhJLz5KmlnbVaLQ4HKXudxXdeTswGfnNxnd9hEzTZBvFT_Kgs6EigIpVFWrJ8b9xa7XWTi3eso5p7nuYltCp05TYlymWhXtg7ZIzmy7zMltY5Ok3gGXsY_Q810TtZo7hSTpTNmdaf7rNqG8J4pzroEuKRbmN6y__Y586MfDrwCyfQcghkcja80Euw13XZnZdDr8jehJs5NMpBqLkSwP3VLFfYzvf8idDEGCK3-gi5Fymp1zWSkqN4IxxoCzIeUy1TUHqXn7hAkkFbkRWfyW7f5lcn2T5a793jwVkrVJJEFFtNIFltLxTraebRx0KO97te3oQfJFkne1NwECjAp0vhcuYJkGHXo_zW0aYCRDr17d6NV7EuFQK5tgR65rMPfDFAU0kpdUdsDSp9BTyzdSU0hOR0eFR92aQOAThxAaIo3yg7i9UAKU7zq9sQlZ5EOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=MkQjoEFhMdgqvYUjprvpC37oQolzpfVViJQi1tz_6RA8lvdgY4DonbSx-wTXOGWhzPiEcC9I2TTi0uLNHXlbulucArkuG7JQdJfcPUJYv5KwD-IkTlx8lbgCvo0ygnnEb-dvecLnuJlbcTz1WJwWLLxpxPktMU2g9yjsc1w16Nw5tQ8jzXdYY-GzNTMIa4mEKn5yxrQHDwEIjMWj_fJypEXag4aXTo-wPbl6WKj5YzqA4JHcUE-HAiqPuepypwmtWKsq00WmK-6vgCl7_D70ZPFKbtGcQ9eIF3VXyj0bjm3ZxMne5TMMlIF1QiuzW6CrtnrWOR8vmYBiZvR-BFKJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=MkQjoEFhMdgqvYUjprvpC37oQolzpfVViJQi1tz_6RA8lvdgY4DonbSx-wTXOGWhzPiEcC9I2TTi0uLNHXlbulucArkuG7JQdJfcPUJYv5KwD-IkTlx8lbgCvo0ygnnEb-dvecLnuJlbcTz1WJwWLLxpxPktMU2g9yjsc1w16Nw5tQ8jzXdYY-GzNTMIa4mEKn5yxrQHDwEIjMWj_fJypEXag4aXTo-wPbl6WKj5YzqA4JHcUE-HAiqPuepypwmtWKsq00WmK-6vgCl7_D70ZPFKbtGcQ9eIF3VXyj0bjm3ZxMne5TMMlIF1QiuzW6CrtnrWOR8vmYBiZvR-BFKJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=HfekTwzoQhtU-7QPBuA9U7Y9so3e2fIcQXqjMVOyRF6sh2DuX2M8UQFp3ezijjL90nmnhluPbCsMPr910-CZKWF2HSDmzhvshuDZrlS8wkFkmVjbvykvFNTiqdNQ7Rcu_6H7IU_-JSMhe9GeM5u4TrsZtY6jZj43s0kusFf_pd5tuyGk6ZcGqpX9VFYxUrJ6ZmNx_14lwoHcb3oXu5Bdp42NbitUOy531VYEeukmc1bICY8-6pxI3WSUCpnGGOPE-7BTJQXHsaFczky-udnRdcVY4ZQf7iDhdQvhQnrNeEj5PX_wo76hm9jh4UAR1lUExhlG5cF5uwmOvAsbXUQZ7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=HfekTwzoQhtU-7QPBuA9U7Y9so3e2fIcQXqjMVOyRF6sh2DuX2M8UQFp3ezijjL90nmnhluPbCsMPr910-CZKWF2HSDmzhvshuDZrlS8wkFkmVjbvykvFNTiqdNQ7Rcu_6H7IU_-JSMhe9GeM5u4TrsZtY6jZj43s0kusFf_pd5tuyGk6ZcGqpX9VFYxUrJ6ZmNx_14lwoHcb3oXu5Bdp42NbitUOy531VYEeukmc1bICY8-6pxI3WSUCpnGGOPE-7BTJQXHsaFczky-udnRdcVY4ZQf7iDhdQvhQnrNeEj5PX_wo76hm9jh4UAR1lUExhlG5cF5uwmOvAsbXUQZ7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=Tl5I3STSkX-xH4zCt12JEqYyFZMimI0PhV_6KZX3GxqrHJvpMp5VYB2g4W1BNUJZxYSPJiUmfzRr-RYCGKQGO7le3G4rrXedYpOW9_RLrvObTx2iOQpNUI4fdQNUIca3wKl2aynAdCXzuEy8-zIYwM58guc95lHMkodXPhM69yZawnp6qi7_8REWwwWqMV0OmrrmP30kVHZDKuMynYziLRp3eoq5ati-ge2tRa8flNePl51WfDm3ulGVaAzJZu0m8soAlJZdXag_HHeDW0pIWTbh3PZV5xlKYIKRR_gZYwt8I_WPbfkQPrWaIH_dOsR0HEQznIqC5O0OK4ulzyuALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=Tl5I3STSkX-xH4zCt12JEqYyFZMimI0PhV_6KZX3GxqrHJvpMp5VYB2g4W1BNUJZxYSPJiUmfzRr-RYCGKQGO7le3G4rrXedYpOW9_RLrvObTx2iOQpNUI4fdQNUIca3wKl2aynAdCXzuEy8-zIYwM58guc95lHMkodXPhM69yZawnp6qi7_8REWwwWqMV0OmrrmP30kVHZDKuMynYziLRp3eoq5ati-ge2tRa8flNePl51WfDm3ulGVaAzJZu0m8soAlJZdXag_HHeDW0pIWTbh3PZV5xlKYIKRR_gZYwt8I_WPbfkQPrWaIH_dOsR0HEQznIqC5O0OK4ulzyuALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amXvqzDogj5w22V_SQ2UQA9S_lgTcdBS6QyfR2oWjSNq2gFeie0N7Tmb5OWf0OIg7-g968CJI5Gm-9Snddv89LJdq4jwjs3oBLFhIVgV_JkAtnfEu_imM5B930LUCF1SJNCfqdJcXRfTdPTo-Cv1kGn18_1A8zuGfUPafAiAbRGv7oPnWOLQbLUQOJtfCBOloy_A49DkEsQCnOyKYngXZ9XenAJKBCw-L8jCD8Iikx3p6umYP450y4MIZ_1oxLPxMkat-QzqP5hZZ3eM7t4iNojpQTNMrgOeskcycMtloY7rzxkuvur8miL9L-6WEJmTVW9EazpGqtSvc20tGOqZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=UKXZeBXUuC9p2LtIkNcGs0AAS2iddlYGntnqsjYJiHT6spnLdimlN4VVaadX9TFqPvsEaa4BGdIH6g0Pq5rOk2ZUHnosJLjocYlEjZKOP6SNPPs3_tj6dbgSTEEJMeWrWz2Fb3f6Jo2YHfsYTQBr80xS9Tm1SeUTPTMcyM4I3GK9O2Qo_OcuYjY8wxQYR_fLOCCp4eJKVdaqSDm3wsMkhyRBlwJcPRE2S7biiq6nN3na90zxXGFlNkiXD39JGuF6Jwcnh_9Jf9K8R5NhtXZ0kO1qKydajwoJtmHHXzzVhymGAGHiK3KiCQA9eAmhDm60_UlGbQJdVWDmB6Lh0wqt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=UKXZeBXUuC9p2LtIkNcGs0AAS2iddlYGntnqsjYJiHT6spnLdimlN4VVaadX9TFqPvsEaa4BGdIH6g0Pq5rOk2ZUHnosJLjocYlEjZKOP6SNPPs3_tj6dbgSTEEJMeWrWz2Fb3f6Jo2YHfsYTQBr80xS9Tm1SeUTPTMcyM4I3GK9O2Qo_OcuYjY8wxQYR_fLOCCp4eJKVdaqSDm3wsMkhyRBlwJcPRE2S7biiq6nN3na90zxXGFlNkiXD39JGuF6Jwcnh_9Jf9K8R5NhtXZ0kO1qKydajwoJtmHHXzzVhymGAGHiK3KiCQA9eAmhDm60_UlGbQJdVWDmB6Lh0wqt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=F9ztgwjX7VjgSepMIQCJFwlN4LfSmOKNBhpTceGs8OQQM7Pwnjuf8BpJqiutooBYlXlnlLHjzcoykRzBT4ytO2FvqsqcegmaI_TEsL6UQJRV-4ewfSSZ81UO8KWy3SQW8MDVMKdjpX2DQDR-dhcwQsN0h8HmJSC77LqpTo3BXHwm-8w15gC0huW2fCDuS4z_HRA4TecZl-eL-aHTC40tgv5JSAbnROuwRbgnAfYTo0AZR3L1BnNWGGw3MkfbAl7gddOgWuudUPp_fDX_J5IRCvSjJpCsi5UWTkjIsfFykenUxkdbFBq6hiIt4jOnly1qUWAtnkUfMCHEf9cAW3o9Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=F9ztgwjX7VjgSepMIQCJFwlN4LfSmOKNBhpTceGs8OQQM7Pwnjuf8BpJqiutooBYlXlnlLHjzcoykRzBT4ytO2FvqsqcegmaI_TEsL6UQJRV-4ewfSSZ81UO8KWy3SQW8MDVMKdjpX2DQDR-dhcwQsN0h8HmJSC77LqpTo3BXHwm-8w15gC0huW2fCDuS4z_HRA4TecZl-eL-aHTC40tgv5JSAbnROuwRbgnAfYTo0AZR3L1BnNWGGw3MkfbAl7gddOgWuudUPp_fDX_J5IRCvSjJpCsi5UWTkjIsfFykenUxkdbFBq6hiIt4jOnly1qUWAtnkUfMCHEf9cAW3o9Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=a3Vv7lKlLuutdCRdRVOCjInaFs0Gnuoq85cX_Jr6GnIvqxT0LzvkdHSI7ZbNuuX-T0h-tvQXwC77rRuzeEKNhRd-MsC2vR5cVyhbvSR15supH083Z_8QHorIIPYrPlkNZg6c1GtVyVXb2X2zEFMc1epwhaTVfpbF1HLRQ8EqbRWDdqJGK3bAyBkyVGlg94kv4HziifKjg9Lb0tg76jQQMRxbIhGZzPTdnVoKtAn6_H63SrFkuoxmQGR6iOfWWS_flIYOV6MHSuM_At8RtUJjtCElh0PpGDS4AqxjKg5KjMmPf2sBD6LIFgnv-vxJzAV2mOO-uD8AlGoTcpGkDz2O5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=a3Vv7lKlLuutdCRdRVOCjInaFs0Gnuoq85cX_Jr6GnIvqxT0LzvkdHSI7ZbNuuX-T0h-tvQXwC77rRuzeEKNhRd-MsC2vR5cVyhbvSR15supH083Z_8QHorIIPYrPlkNZg6c1GtVyVXb2X2zEFMc1epwhaTVfpbF1HLRQ8EqbRWDdqJGK3bAyBkyVGlg94kv4HziifKjg9Lb0tg76jQQMRxbIhGZzPTdnVoKtAn6_H63SrFkuoxmQGR6iOfWWS_flIYOV6MHSuM_At8RtUJjtCElh0PpGDS4AqxjKg5KjMmPf2sBD6LIFgnv-vxJzAV2mOO-uD8AlGoTcpGkDz2O5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=LQVoqYqVchJZ0QV-ao7L4p-hmi5VZr6r40VDBZDwQpDnLwOAsMu_VtO0PKoUtr-QK5UWHrLI_WiBKajd2RDNkPMyshTdrUXkl1dHbhXPKhJVOB-ZhplzOv4PR2GpAblY39BSf3iKN4Ko6h-Fd8pnnlbHP8jNZ66SkfaFgs1iUXgMaBRCMU-9--kOrccC-N245xnOY0Wu5gVn1PJhdeTZY9_DoLOJqRIKxKT1l0dmJA1yGQPkLt3l0SrXXEGWsbwbaCpEFVdqS1o_enOLJ9P4ssOkPgsG-1wYrNxqDucsLjVC7d636hnMnSDkrMD0k2ys_ICfbMoNkI7vZ40R4uW6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=LQVoqYqVchJZ0QV-ao7L4p-hmi5VZr6r40VDBZDwQpDnLwOAsMu_VtO0PKoUtr-QK5UWHrLI_WiBKajd2RDNkPMyshTdrUXkl1dHbhXPKhJVOB-ZhplzOv4PR2GpAblY39BSf3iKN4Ko6h-Fd8pnnlbHP8jNZ66SkfaFgs1iUXgMaBRCMU-9--kOrccC-N245xnOY0Wu5gVn1PJhdeTZY9_DoLOJqRIKxKT1l0dmJA1yGQPkLt3l0SrXXEGWsbwbaCpEFVdqS1o_enOLJ9P4ssOkPgsG-1wYrNxqDucsLjVC7d636hnMnSDkrMD0k2ys_ICfbMoNkI7vZ40R4uW6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=E1T40nRWlm8fJSYQpVaU6dmSj4Wod1lA7fvE0bXFylz01khd7RR61CiibGgBaa5TlEqZPV56mbpEB2PpySnjCiP_MKB-Uaz2EyoX7PAYoBWTZN1yL-0H0C7EVXKWBclpsZXImmJtFwkzVgFCNE52rZND8TR-cJ2aMN1AS_dp2t5-XFSJFTYcYI9h08z2qUevx5rEU5t2WWCh8NmSbxw-awDv4obql30WYeWCyIF14irTf8EMS1T5TX0QaR6g3oYYUJx7KNw453KWsfkvn9Ird6HoJ8OXrV6r7qhzCZ2bQl8Pm4QQSC3XM1U5wSD2HmOjRDy9Urxc0Vw1Htq-GqFL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=E1T40nRWlm8fJSYQpVaU6dmSj4Wod1lA7fvE0bXFylz01khd7RR61CiibGgBaa5TlEqZPV56mbpEB2PpySnjCiP_MKB-Uaz2EyoX7PAYoBWTZN1yL-0H0C7EVXKWBclpsZXImmJtFwkzVgFCNE52rZND8TR-cJ2aMN1AS_dp2t5-XFSJFTYcYI9h08z2qUevx5rEU5t2WWCh8NmSbxw-awDv4obql30WYeWCyIF14irTf8EMS1T5TX0QaR6g3oYYUJx7KNw453KWsfkvn9Ird6HoJ8OXrV6r7qhzCZ2bQl8Pm4QQSC3XM1U5wSD2HmOjRDy9Urxc0Vw1Htq-GqFL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=TbuTYh8USvE12OSGdk6T3LWbghDVOfRILSv-HUgqwsjEU-hEXOGUwY6VYeifbCe-h7isnobLMw7UIl6Wro_6hZiD0yneZouVcbKNTM8T09Ax2Jvfmkqlm7MIicGwh5al7HjpYIv5OLe_592NQYNTsEtTAeZGoMzP_NRGJqGth2WJP88QALTuOe_Ji84VsYc1p3bkQItRPTHVGg_BXkJLWGwhS_jsz9YFsiymMSN7_z5hJrGWGpXbT4UTg1mw7pfjZ9TWpSXfvmKhBy6w7j5HRhh3ycIiFVypUW5jp47oVQYYbT_Q01M9sQUPS8ylwGiN9aHjzxe_VN69m8ZXt-wnWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=TbuTYh8USvE12OSGdk6T3LWbghDVOfRILSv-HUgqwsjEU-hEXOGUwY6VYeifbCe-h7isnobLMw7UIl6Wro_6hZiD0yneZouVcbKNTM8T09Ax2Jvfmkqlm7MIicGwh5al7HjpYIv5OLe_592NQYNTsEtTAeZGoMzP_NRGJqGth2WJP88QALTuOe_Ji84VsYc1p3bkQItRPTHVGg_BXkJLWGwhS_jsz9YFsiymMSN7_z5hJrGWGpXbT4UTg1mw7pfjZ9TWpSXfvmKhBy6w7j5HRhh3ycIiFVypUW5jp47oVQYYbT_Q01M9sQUPS8ylwGiN9aHjzxe_VN69m8ZXt-wnWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=Q4MqsdaLBcN8avBXTwo92Q_FqcDlHrgkIsbZk8L33XWE_NWKWpT0eDi_ywVWrihDdcOE5lHIOA2IyqDC36zOn6ug3E9cZgRcFfwv0tLqwfAxqhArNZ8xY__qAxqFmObnzTW1qLIdnIO6PR6ihhXknqoAIyzlhHCoA9CdAeFX4GUcwfkbeJlNhG7IV1M__WjFZUpB21YeqpZBLBWPJSlnDStWiYByqqVjV9cm01_-yNCypO0Nfjk5kVoln4G8k24tiRRAy6MpViqXQwS_cFhPnPCcU1dAewA75IJi7vIsrz7BIZXbo4CoFy4X4V5XXzyPgf0AC6UZhrHrWRcdfuaj2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=Q4MqsdaLBcN8avBXTwo92Q_FqcDlHrgkIsbZk8L33XWE_NWKWpT0eDi_ywVWrihDdcOE5lHIOA2IyqDC36zOn6ug3E9cZgRcFfwv0tLqwfAxqhArNZ8xY__qAxqFmObnzTW1qLIdnIO6PR6ihhXknqoAIyzlhHCoA9CdAeFX4GUcwfkbeJlNhG7IV1M__WjFZUpB21YeqpZBLBWPJSlnDStWiYByqqVjV9cm01_-yNCypO0Nfjk5kVoln4G8k24tiRRAy6MpViqXQwS_cFhPnPCcU1dAewA75IJi7vIsrz7BIZXbo4CoFy4X4V5XXzyPgf0AC6UZhrHrWRcdfuaj2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=D7jsDt4a4ykyBVWvGOTAQlwjKMsm8hvbddEXq32wtYn85LpXSsaoyLfm82XF7uIHZpLJ1Pui63bEJyszquCnww8drMdhama3wVnwnHIbv9VP17Q4pLSXyalBVyGQkWvnMA5FzHpSxD165xWqq4lK3604YmR7tcdvMLv36JepQ2__mnNUzyJxArK43Z8crWNiXLTpbBLDEmKgJgXcXXZdtqKytqVsmF0csg_9wujetZpG36ODUAF8vKpGH58QQf9_rJotHaXxO1MbWeasTyphu5JOL3FQZGjPIhCK4UvR8WeRvfRk0c_hTJW-wlRZ24vQrmex2p84QvAfg3c_ctgp5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=D7jsDt4a4ykyBVWvGOTAQlwjKMsm8hvbddEXq32wtYn85LpXSsaoyLfm82XF7uIHZpLJ1Pui63bEJyszquCnww8drMdhama3wVnwnHIbv9VP17Q4pLSXyalBVyGQkWvnMA5FzHpSxD165xWqq4lK3604YmR7tcdvMLv36JepQ2__mnNUzyJxArK43Z8crWNiXLTpbBLDEmKgJgXcXXZdtqKytqVsmF0csg_9wujetZpG36ODUAF8vKpGH58QQf9_rJotHaXxO1MbWeasTyphu5JOL3FQZGjPIhCK4UvR8WeRvfRk0c_hTJW-wlRZ24vQrmex2p84QvAfg3c_ctgp5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=hkCiABZdDslmr1e0mf7zfc2NF2z1n8Ul97SbPJ2qRFY8JwCU6fUumyE4DKramROZGV3xVJQ0RClMOQ93mnRU6yOuuQM1wK3DHDRRZryTc73DI5oNGAM_2ef-sItCITnHsitVyMd9eChRgFq4AcWhFv-9dX3xltZLz0Q88BoihRa9Wh5D5F0614EQR1G4jrm_VXwSq7MlFezrJgtv-rFjGZM2KGeTuO-UZ7Als-dLmsMSGFyOoS3k1Gio9y1e7w5Op0-c2UdI3SYLNgC0jtiShFCwab1fen4emZX48NUD4qNscbN8OhD10HMI2nayPIMdvstKiTdBgDwF5wagzl47uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=hkCiABZdDslmr1e0mf7zfc2NF2z1n8Ul97SbPJ2qRFY8JwCU6fUumyE4DKramROZGV3xVJQ0RClMOQ93mnRU6yOuuQM1wK3DHDRRZryTc73DI5oNGAM_2ef-sItCITnHsitVyMd9eChRgFq4AcWhFv-9dX3xltZLz0Q88BoihRa9Wh5D5F0614EQR1G4jrm_VXwSq7MlFezrJgtv-rFjGZM2KGeTuO-UZ7Als-dLmsMSGFyOoS3k1Gio9y1e7w5Op0-c2UdI3SYLNgC0jtiShFCwab1fen4emZX48NUD4qNscbN8OhD10HMI2nayPIMdvstKiTdBgDwF5wagzl47uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=DJrOHCDHEM1XEPK5zSE6kb481wIIOfEWGaDEWyZeVAq4fg4TC7tkomabA68p3EWUIqVj0uGD_RP5IXfeT5FbOaowy4L6_jNvPh9QatD0GnxuhpaB4nrYWjHhkso66legPhGxRnOzEtGgEoF19lUGwg6P-zb_7T-Qt-VM054VNPzRgOuK4u7IUflVcUGgpsu5U2JR-mHlFNhSD-0VyGPPo-_QFDPbnalNA8IIHmbSWDWhg06zsayGGZvjevmCbQdNo3l3I6F6Qb5eFPKCawON2BmUZpIhQw9QyY4Kox_8bm5yEsWGvGIl2emEd3IBXQUK0KihU1g77eoifWEsxsmnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=DJrOHCDHEM1XEPK5zSE6kb481wIIOfEWGaDEWyZeVAq4fg4TC7tkomabA68p3EWUIqVj0uGD_RP5IXfeT5FbOaowy4L6_jNvPh9QatD0GnxuhpaB4nrYWjHhkso66legPhGxRnOzEtGgEoF19lUGwg6P-zb_7T-Qt-VM054VNPzRgOuK4u7IUflVcUGgpsu5U2JR-mHlFNhSD-0VyGPPo-_QFDPbnalNA8IIHmbSWDWhg06zsayGGZvjevmCbQdNo3l3I6F6Qb5eFPKCawON2BmUZpIhQw9QyY4Kox_8bm5yEsWGvGIl2emEd3IBXQUK0KihU1g77eoifWEsxsmnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=XvaaVoVWlPOyNXyMjBoHCqnHeQdcomxeKSxgZy-JFmwqzarozBQk6vZLh25zq9thwL9OxQTRUEhADDYBQ_lY5x5nXG0uaES_GU5_hOrfcESwJlZBJAxBW5aAHMnGJkAhyG6yChX5SQwq3V8080VAZxhk4Bto6AM0OEDv1TpWsbNkmzzhLVLM6eoxifz7xwNgY1QsQ-sj3T6VBdguWnyU84yCaWJyJuhgTj0-B8Sxn8fTefR6oPSlf6J2JwsS1SAPEpLTlVR5OFm76cI5FNzflF0S196Kbpwyl7Bm6MEbi2vLnOmFBI21SuC2hVMBki_P9ssb718jWvsXRzQZkWdbkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=XvaaVoVWlPOyNXyMjBoHCqnHeQdcomxeKSxgZy-JFmwqzarozBQk6vZLh25zq9thwL9OxQTRUEhADDYBQ_lY5x5nXG0uaES_GU5_hOrfcESwJlZBJAxBW5aAHMnGJkAhyG6yChX5SQwq3V8080VAZxhk4Bto6AM0OEDv1TpWsbNkmzzhLVLM6eoxifz7xwNgY1QsQ-sj3T6VBdguWnyU84yCaWJyJuhgTj0-B8Sxn8fTefR6oPSlf6J2JwsS1SAPEpLTlVR5OFm76cI5FNzflF0S196Kbpwyl7Bm6MEbi2vLnOmFBI21SuC2hVMBki_P9ssb718jWvsXRzQZkWdbkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFESUGDUUnxSLvtXqp2vo5N8gKkIKjJSLLD1C1KuelPiM5HqQX-QgQIaZdTIp9JLNy_aITSHwBVkczDCbc6yUEJTmwdAGy9x9U9fDm9A5ISp_9qp4YciO3UaGA7wmOhHK-SNI11lFP4qzO2Kyl02drHZR7dgGPt0XUjLOuU4sEyMDrsrGPba3-PpEyL3v_G13JknhYzfQHZ02gOnom-myeFhgHF7hK7EAzO_O1_k2X1ymNA1f-vk71ZZw5_d0syOf7WIRQPx8RAElqmZv7w-bToemSMQYmn2jHLDGzudRd18lNy1slizTOLmQb-8wkEK_4NZXuujdxhfxVXxX62Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=apPBGoxOALbij4hCqqzdED3WtKAYRFCTMbdwhYVcZcFzZU8KC7tnPpDYfcgeGtF0KyrxLyA-syYGnYXIYkhhojvylnWMQrKhOtalOk3MQV1k3fFp5N3J0D0-597xTGAvVpSWpgfHrvV7b7-Ro5vZWB84KcEwSGNUZzLLlzBZquSanI3uBK7Qb5trVo-4NNBeIGCXp2P4mmPrPtfqMnE7iocjrfGG9ROlDVdDGqMJKCdXe_ls_XcM7S4HYNVHxf-tjW4FcFanqUQTCzKX2RINTvC1PBWCt6bEd7ZO_k6xRUxUi6hTshiN3qI32axR90Orm2dzP2ARc-AYJWFUbyiMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=apPBGoxOALbij4hCqqzdED3WtKAYRFCTMbdwhYVcZcFzZU8KC7tnPpDYfcgeGtF0KyrxLyA-syYGnYXIYkhhojvylnWMQrKhOtalOk3MQV1k3fFp5N3J0D0-597xTGAvVpSWpgfHrvV7b7-Ro5vZWB84KcEwSGNUZzLLlzBZquSanI3uBK7Qb5trVo-4NNBeIGCXp2P4mmPrPtfqMnE7iocjrfGG9ROlDVdDGqMJKCdXe_ls_XcM7S4HYNVHxf-tjW4FcFanqUQTCzKX2RINTvC1PBWCt6bEd7ZO_k6xRUxUi6hTshiN3qI32axR90Orm2dzP2ARc-AYJWFUbyiMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=CWBuTYrBxLK9_sXjY8dICwWJPprTmlnJ7x5bewIk098JXdsVdGOMDkgPKtL2T_2ebJ_SI2gdO2Cyqv4PHMPoL_IgMrDaeEHk9miFk1241X2e1gc0fSXte3PaUfswQKOMjpYqRAPy9GyWqy7VRZ2HUOLx_FM_zDfmiK63aPCqyPjUoypJ9JP-T0k3n_o19zmEyKhV0cauuW8uwQhtRbeZcLYOUGNSGYLrcmDCa2n10JwGRCrS_3hjAXPrd6ZOVw-UwMhIgh3FGHFUs4qZsB4nUVKQvtk9B0sbhq4JNSNoaiwqiKl0WMUaIVg5Uat1LyFWPd-nur5onr_NTjItW_PsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=CWBuTYrBxLK9_sXjY8dICwWJPprTmlnJ7x5bewIk098JXdsVdGOMDkgPKtL2T_2ebJ_SI2gdO2Cyqv4PHMPoL_IgMrDaeEHk9miFk1241X2e1gc0fSXte3PaUfswQKOMjpYqRAPy9GyWqy7VRZ2HUOLx_FM_zDfmiK63aPCqyPjUoypJ9JP-T0k3n_o19zmEyKhV0cauuW8uwQhtRbeZcLYOUGNSGYLrcmDCa2n10JwGRCrS_3hjAXPrd6ZOVw-UwMhIgh3FGHFUs4qZsB4nUVKQvtk9B0sbhq4JNSNoaiwqiKl0WMUaIVg5Uat1LyFWPd-nur5onr_NTjItW_PsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=uTRHU4MHJw6zeddE4ekBHBfvoNl2ILYkhHTnMi1uSWc4oYhQr50duThzvHzYEIbtKJV6h5FCn0Zy2tA19GR4Af22EqYqMhPfku-kvi9PULa3W7eQz_C05sv9TkyzIjQ6iyvvZxtTdjoDaPs-wZNqy8VFg0IkKeF6JgLwdb52yVs_cVcbjajP6utNDNxZghhu09aK2SX-MWoQcRHT_NIL2GP9M6QHVmMufZieIZbtOEHLfV80yam-bGTPIoqTr-hc3l9Eo5GqNKT5KdD5PpoNsSAdgbDff4XCi8gfvF1qyo9N9kZNyEBL0tC9JvA8J9uJ-O7r2I0gylcvG5oMNpXH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=uTRHU4MHJw6zeddE4ekBHBfvoNl2ILYkhHTnMi1uSWc4oYhQr50duThzvHzYEIbtKJV6h5FCn0Zy2tA19GR4Af22EqYqMhPfku-kvi9PULa3W7eQz_C05sv9TkyzIjQ6iyvvZxtTdjoDaPs-wZNqy8VFg0IkKeF6JgLwdb52yVs_cVcbjajP6utNDNxZghhu09aK2SX-MWoQcRHT_NIL2GP9M6QHVmMufZieIZbtOEHLfV80yam-bGTPIoqTr-hc3l9Eo5GqNKT5KdD5PpoNsSAdgbDff4XCi8gfvF1qyo9N9kZNyEBL0tC9JvA8J9uJ-O7r2I0gylcvG5oMNpXH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phpEQOUFwF1QdDugarVuIbMSz6NYxj4I64iAXfgQn4l5IJvIX5v5G_YwiiFiHd2PmTiMGNL7s-8MCxWhBDLNkw_B8AxoPGbhY2vFvE-o3JXtiOvbf_a5QfNmBMcMDEGIWAA7mK6hVJjGEsMzr_sobFYRkINbIQo3_P6s4-x04fC8-AfDXXHxD2sRjLXOMHvKMDAr1nyP_F07lUYkqqpQN6NFpFUor2_je5l6m82cUccii5-am1ggdCNJFGOx3lpVV4etlEy_CL3aCnvq9q_FinvWiGog28vKLWwp9UBuP-bd8pDczim_SLalJa45oSnLr8wCEuk7UlYk74lhIEN_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=ucFW_CG8tbaMbJdaY32iHkKHjDZ2Y8qV0KrPakIZlqA1JsZCalSGT6OBvf7DXWosx0RUKcWnrr1F-oKoYQhxg10_S4WCJ9zoIzlp2VfZY8qjFX6dLdRxQuAtsj64fYEDTrs0cjsOb2tPjf8F3Qy7Jpw4ltd4XtJi1Tt5vAEf8sgf6M3jheGh9HDlAgKthkmg_iWnhMgw2yh8w4bJhRAoDAKFA0N5iD4zCiEMMilNlr5ZxABtSNs35_eEADKiVMmW1gzSJ5NkvILoiN_uZATOhGQNa1wOS-5G2wIbN2QVDZMw2AFGWOCKr6ytsfv3WRE3zbdvFx8kVywukJQm0OCjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=ucFW_CG8tbaMbJdaY32iHkKHjDZ2Y8qV0KrPakIZlqA1JsZCalSGT6OBvf7DXWosx0RUKcWnrr1F-oKoYQhxg10_S4WCJ9zoIzlp2VfZY8qjFX6dLdRxQuAtsj64fYEDTrs0cjsOb2tPjf8F3Qy7Jpw4ltd4XtJi1Tt5vAEf8sgf6M3jheGh9HDlAgKthkmg_iWnhMgw2yh8w4bJhRAoDAKFA0N5iD4zCiEMMilNlr5ZxABtSNs35_eEADKiVMmW1gzSJ5NkvILoiN_uZATOhGQNa1wOS-5G2wIbN2QVDZMw2AFGWOCKr6ytsfv3WRE3zbdvFx8kVywukJQm0OCjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_kjFCdsZkp7PoNSl_5xow92p5Uah5qL2EPY63vxjHnrfXhu62uuybDyp4OD-hlANnI1osMW4fOdel_oTcO7FKr2dSpFg__qPmO9040l4mxgpQgsruP14-XDf3eXJIeivhBb2Ii96dsEYa9nuJ5rbuFUuLPvyG7DyV5bPk9UQxwFd1G3miWzywkRvibx08JWjfrLGepHAAucNGBtYBebxmQimOTDp-cMDVUjHibmCuidIV8WSmHNup7GNRH0tJsYsBaUkXiPX8EGp1lPOLDGsuqprcey2tRsteK8PdDLN01MkBKyxIm8Crem68q0cO28x7HvXTwLYdHnRW2k9wRA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMJreTqwh7jdU2AlLV66HpUovjeex-pilMPhzsMzSnHYDv12NO8o5A7xhe60PEWWQY2rhnQsNwftO_iq3UEXr1hk8nFBeVqmeXLlABrlAdQgA4SYjJ2r4P6un5cFjWl8j1nnRXuUhjnTlTR5R40N5sQf3q6lHDSNdSam9q0Scd90Bs7wNO16obW-k9soQC_NpkFXN0h4CJffs7gPRvQAG9J1YWE38umaClSlSpXqPOjCT420LmFUEqw4fn_Q6UhEXF1yqYna3kyoQHTYqWFOgATl3fBI3yUiQuWOmBY2CG-B5U4rLCjrM_llchiudX40qLBpqNCRR0P_q9EdwWYetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdAFsg8Rle4ZYaT9EhJDOqDy_-iZ3oma6xCGgdW-RNxhFb5jYFYcHg1p__r2KKMpMZzRO9O1vq8Y_gt5KrtLfSNPdqzocXkcMInkQEbFf8QyTRoN8bzgEmtLatpXO0dL8tOPo3bXv4wr2g0bC9vurCxMEVvOnf5TpxzEj0OjLnz2m8ET8zUI1VNjHBsnYeYCD5nZyF0i5wcHhoP4HVvYgaMBNNahi0Zq8sV1paXO_Fgq_6kc9e_wa9r1V1uYFRu12lNJ5EcAhmhtW_22XzNFZ9E6XDeXHaCHMnFB-mHxHJazyb39udeIkHpvWickhwpYiKEf6lVeOsSQN0T_VbFm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpAJxkw6Az9BAeKSuOb82RVMnWF_H99iRsknvXVanA68Yb9w4UfIqHn5oWJKNgYlYvWK15kTamGNFDZNxEfgnT_OmAEzZLpXIJ8AXaS1EiMbTrNRVT2Cae3Wdk-VvLdPYJEdAT21oFqpj5Tt1SG6ir6oH72ELD7ndN13nbp1_onmSxbujXyOYs5zJSa4RvtNJTgyyPJuQ62L9oX7gp9-vix_6X94go6MvE1K_SGd8faigukSzilEbZ_Xuk6b-c9Vaa7E3_irv9Ix_HLKflGyZa-5eA9raQqExqte1202JJJY_BBujkiLb1KotwDOjtAWsETxkRcPwPwUL58A2LLPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUCKGn-3dqAKrw32VLfoNKF9sotXmGZ1NEntAHK0Q7Bo6gLozK7vqXAcM2FZyelarA4xqkuvIT-T77JH0rPQoUILDTLKsslZznYiCxBMGoYN9aLZxAsmEouivysZ6CZMjn6GwL8DFeJsKynbyoKgW6GU6yiIGgYNw5MZw7_cbsoxa1f7MxQPit5OBGg5etLynDwfg82x8RtF-Z6g9A-77FGiyj5jSW2Y6ibVX-PitTvoI010WCzm4woQYHWvQQrDnHtWNvKiXp_A5YCFu-8oSIckKSU-69vcMuJ6KZQW505fPcZtmM_dyy-9cj_y_3wPTfuRmDMyixeB97NEsh-U0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=RWpqQ6-36iydUGn3EXiU6e_wCsMLv__l06ydhcTpb1PG2M9xHDz0yu6Qdf2mfD-w5KlmnpMlUZ0RKz7ZKr-N1JgLGiKrWsHRgSUVRh_UG9gxsAKbvCGNXPZ1bPny65d0ttAQiuOF_TUQzhFsEjlelm0lWnF3AvEZpMXNpU2uFynQ-QrTx-xaKHeXtvlWhtlzapq2Xw0W0z4yktUcOE3DU3w1Zyv-CgDk89XpvY8BV9AvqQCh8vn9fr5RtFephqnRxafQiMJL3TK2UV8_C2dTSmZZJ0mOHGu8QLc2RyXZ0VFa_iOAlUDEolMjkUZ97G35OMpeCo_JpN5JB8qgP37SEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=RWpqQ6-36iydUGn3EXiU6e_wCsMLv__l06ydhcTpb1PG2M9xHDz0yu6Qdf2mfD-w5KlmnpMlUZ0RKz7ZKr-N1JgLGiKrWsHRgSUVRh_UG9gxsAKbvCGNXPZ1bPny65d0ttAQiuOF_TUQzhFsEjlelm0lWnF3AvEZpMXNpU2uFynQ-QrTx-xaKHeXtvlWhtlzapq2Xw0W0z4yktUcOE3DU3w1Zyv-CgDk89XpvY8BV9AvqQCh8vn9fr5RtFephqnRxafQiMJL3TK2UV8_C2dTSmZZJ0mOHGu8QLc2RyXZ0VFa_iOAlUDEolMjkUZ97G35OMpeCo_JpN5JB8qgP37SEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otWrweG43X7OcAlIzAvmLXMoeLkhOdIdwi7TAusYSWfWpvjtzXk9H770NcA-R_LEVjWB_Z4VYA_6MogS2l55W1w7XjEc2K-BNSF-H-zhqbIFIZtJTUx5YY465sX1wGziQZQxXr1NO52eoISDnkkCLcD7uVNH7ABr0UspRylfwiPlAq-jF44mGMbe8pg9xte-JpLdJ03HzvBSplGG2m8zt5patylTBddSGU2Bx39zOhZzjZr2a0x4ktX5x2u0-060q7YPFMsTQ-JqIRzSlqOWPkUPP6d9v-hWCriAFn6UDe4chF2HoTZ1XPfA9pTGr_4ytv17cxU6fNFCtfhtzo_USA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRdE-1PmiOHTEkSiEkOOVXIaNNPDFzOI_E6PdUSznaJpefTSdx4_F9EdTwaI7K66e62AUirbxziedCca35er05a6cz2cqdzPWsrCSJ_lP-okVI0Opg1imfb-Nidgu29P6DRZtEZfVLdNeV6KdWX1jex3sw1KcCDwe30k7Z2e1UF05vijYz71Hual9Vl0DCTHzdx9hCqM9MC7lsqTY6AI4q9ByomPHW1cxe1mN4CxfqXanpaBjIxGI5iwkpSJluAokevrNO8pT75AMp__4hpODVD0Iz3eKibuvZGuAucpQ19wdnkSUjpGdpEUOdjBeJrMPdGM_dOw9319daqfneGF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=Ta6GWvTsM59KP0k7WGozGrr2pllmSt-xLjO6qEpRqYlkc7J2egHZbcQWMq2wk1edNn_ObVC2PcnqHOdvX5ErdZkB2kk-FY9M_6Z4vJ7KrofdKXwxWYXJiNlviXgWRtU2hWoGCc6fxUAgUiM17vUjY1nSvZsEP-M6c_VyYXYKtKD2Dbn34wOpi3aB3vo6d84VgF0CQvKg2Fy1ygv0R7zWDvH7kDdb-COY-dB1mvdFx6AQgqeYXw8uPVNGfIcFGupb43SLteI_QFn1ZOSEmj8Mx_b_Kn3R1gbCVJRxquitbdfknMP8exnYVVurpEv8_Wl77cl1xurELAthRXILh9LWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=Ta6GWvTsM59KP0k7WGozGrr2pllmSt-xLjO6qEpRqYlkc7J2egHZbcQWMq2wk1edNn_ObVC2PcnqHOdvX5ErdZkB2kk-FY9M_6Z4vJ7KrofdKXwxWYXJiNlviXgWRtU2hWoGCc6fxUAgUiM17vUjY1nSvZsEP-M6c_VyYXYKtKD2Dbn34wOpi3aB3vo6d84VgF0CQvKg2Fy1ygv0R7zWDvH7kDdb-COY-dB1mvdFx6AQgqeYXw8uPVNGfIcFGupb43SLteI_QFn1ZOSEmj8Mx_b_Kn3R1gbCVJRxquitbdfknMP8exnYVVurpEv8_Wl77cl1xurELAthRXILh9LWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=FsSCavzx8UbP0BIaiibPoylSv_NlKKXHljXP3gSUZ8eY1sD45VtDRiubtmOuXQQ7Shq3fojzeln5n8uOwM7FiK-JtJpI75nX_OarEwG1WKF6kUlA4N_DeRgFfswCxSzYg6oCHV9-0rUlnmXrTf9SuDlY6cQJ32LbJZHXlapX6asAP3axjNDfzGB_JxNbETF6Pc0Joasn5JbkLzSvzkEkch1AF4r5GUMGOhqVDooOnwNUMsgBPQQL2PfljQAlcQo5iOtARu76yr2th-vvxQK45DTgww6ak492UNtNm9JxMkuMLgBGTMrRG2e84P5JCp_Cqd31WLrlVu57iu0WfI47Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=FsSCavzx8UbP0BIaiibPoylSv_NlKKXHljXP3gSUZ8eY1sD45VtDRiubtmOuXQQ7Shq3fojzeln5n8uOwM7FiK-JtJpI75nX_OarEwG1WKF6kUlA4N_DeRgFfswCxSzYg6oCHV9-0rUlnmXrTf9SuDlY6cQJ32LbJZHXlapX6asAP3axjNDfzGB_JxNbETF6Pc0Joasn5JbkLzSvzkEkch1AF4r5GUMGOhqVDooOnwNUMsgBPQQL2PfljQAlcQo5iOtARu76yr2th-vvxQK45DTgww6ak492UNtNm9JxMkuMLgBGTMrRG2e84P5JCp_Cqd31WLrlVu57iu0WfI47Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6-La2DMqiSNaUZAyu1tJ2zTHlxBsaAdTuKZW9_9ZUFwEsgtxYa5NnJwtRUA5Ny_UywvZ9ZtZb7hISqJEgyZOpsJO6F7_i2FRa0Taj5NLVZHIF3z0DWaPLExcfVVDnht8cVxk--m5h0cehtkDq1wzSbcVxVvENdECth-ietyO1oSooEPuzmysmYbRitb14qcrmWV0C_w5unADDnqla9qTV21tx_yHa1bJfa_KBgFDu4emI-zgHZZrOFVXBToFamXd5ZAVxqbMapyUoZiGA85JvEk1M8GdKFR6M0rbVLWZFtwwKP1gGTEheL3QDAoiW59yBLDoLYbWOLMd6J8NzVG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxsY_Z6agC3txfB2rqxEOp4bUmmpQQPEq1PB8-T0hipKmFXoa1mWVtn9lS0S8EzJts7xRZLfiVI7fr82DazX-Y1Gc60UotQbAGDvqB0TTaPmwyz8VbsI2XYqGT6cqidlyBP8dyhqjVJ9fqOn7aLt-fkNLs2HozieXfWdKUgW23Kovj4WX2oNkStFKlrXjnWWI1Vf4dtdrHQueNJGRQfAld46kV0sQSvfgitHvS7Hxsh81xiEZe2KcwooxB-_6Mtzwr1vACq5ROuicnmbjicscpCHNWavq1F6jAiQtPYNoebrD9SNtCls_hUfM2zDWtJ3k6IIFtkmXL0d60y0WuCF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipex8MskJNxI_0Ljpc2bllCxfkc0IifeQMZQIo1k6XpTs37p4cP1Vo7ry_LreYTE3P39fNUuKSkOXdKCrURsRTkYmW0NVrxry6v6o7_kx8vHzGmAX6CPJUpigwWJC3Xzv8QwbrtYBzzXXGZg1rxpftLxIVSXsIajewNB-YXR5fKwnEf1RfL-MEdc9fB835CawHRcIO6CWKVd8aNbQdk3XR8GRLooJG635zRHdqD9h1mFZzrCuSpGqmIJVaGhhF-O5pgPCR6Ic-1CGcCmTkivAz5KBKz8eqxf5ToZns0iDUiZlFsass0L8IBwvOxMP51S8_XofYZrAgujsHYbywTXaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okygH2i-NYkUo_lppXxOPET2rrgpoYgoml0HuDtsoI7niTknxBTNP7widh_UVQu1AkSZ9pKcbLcHUbhm_059zFrepxI6F2MDsVQMtv-E1N8905DWgrT8RhkfnCmHG_nr_95Sk9ox4kOjG-QZH5w5BsUjkJCxj_oKFoMin1_sQpre22lI0tw5C1T-Ms4Qq8GrsHK4tqBMS-CA2-gs71HmQqUEmfkEC28dHVy5eS1ugSioLasVBSMOiBI7n5ASTE6IskxwOU77uwk869Oy4SMZhWv2GYDNR3gk4xTxp57inOaFQXDCBId7D8hRgPfNkPTflr41vXJd5x6iiVYTVqh1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg3Rb2-w7WewhU4NSatYYLqRrVpbM7ECc-iEZx2CaJhtBPYJq7h4dSl-b06YgR5Y9LlMINHssFzhrewAwSNZu5XQZqbPSeWmSRK0FblOS-LTPXMvqaYzx3TI-DiURIPcN2C5HU6bgEGjwjMikFF3TwUuuls2aztKFPYoyIOEvQS8eFV10gPMp7kLpdd2RTLYoEiR93TYJIDtPoNExt84fw3zGqj1y31uz_eOZ3ts4QXQur7Z1uLPHMpQaj_0TaMBOVnnLerClipY3_EV5Jz0Mno57JtuJ7jqS7z4Ab_aTciuNerRCF3dR87YQV7UANvhZX7nVlWVLX2GIIE8KwDbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtSllvOoGxYtEcRY62OlD9LT7zT85rSkIvdP2QKW7aMhiVqKp17v7x6DrJp1ccqobWQb65K7j-BsRb_47xm9V5WMJX8OUvAzJzFEfcZ7JT0GMTI_HT3wuocpjmKMuYqrDG2Y4ixwsKQdCGR_15xq605IBp9lLaMZSmC0Jgw_Qqa7YYDu9grLIS1zWbs-2Nsngd9a12ogS4FRU_KPyTOcSb7ZNi55Bpu1i9O8GhiL_zoLw4I0kbNUjaPGB4d5eAXVptY7ateuBfNFj50EUBdn3BHiBkHxZTJ7O71t-tCyquQQJpUOgQ75hyxMwB2NwGaYb7gGZThc0wLLjZZKgR3U1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfgmD2WSLbHL5A6y6SmHJyleZvpwPjwTy5PlBxe8OPLXt6_9aDQbqXzJTEpPQTILsTFxZNO_SIceRmz3RMPEnblRJrqsXNu2erOM565cVctrLmAgJplb2dVqCHp6pOObb0apes1ihxlgFDypT2jlbHoTxeq4wX5VcPxqVAJ0LDjqEBXpEWlQiTZ-bQ0HmmrHfdKYeQyA8xUbsNYcjPOMzEG2XwYbIeL5OmBMGoygnTV3i5U_zwc8kNfdbAiqhvaYGeRED2Kz255XG-RIWWrdeKdJWhaGs_rz5uSNHPUj0p3LgQ-vY4HE-O7nMRaHhxQEruGNldy4RTH44S-EA8QOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t15GjUxhnim0XhPnY7VX2Z3WGsP9UPIQWhzulEB2qi9vauKwu34iEkrHHu6Vy5M5HPvEb0I6PfypOtnOHNNA2b4LZVGT5hePwgp14MuV4Of6HmkID5ys0j60G_c5a76_VATwUIuJJ6oKoiqIDiE_x5cFrPXppmM1O-F5VL4VmU-NfVaP1BlpxNkbR8YQfJKMMnZqPKQj_4Strl1ePdLlxtaq-8EV4x7XxJ0ZqBLgUEWJPVfdyZWIPv9sg_Oj-8vA__TfuZOPCg4qTQCE_ZRpUDeYi_0A7l12MbBNos9pPiMat_7p9k-rQKGob86nxO9pqje5RZ-fKvYUk6Ow6NsRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlx0BK9dSHBhOOHk5qAjss9HJ0CBibtiewTFYPQ_FUrg34ro3Rhv_kAlXeV-P_Irr5yMd26fyAT3OeRtoMyOBsDmFKTK_-WrCP6VreEox1LecvCJZuPN5XTkzb81oWKIp82l-WrQVoEnCMdPU___5G0p3rx4KvryIptINFAdzFAqjcWmQVm-BYO_sBKUP7kz8uvF1-An7mp2IQLvZnwM94EYuxC7erx6Fz-ChGisjYhxoJSIyk9Sc7zs7DEClZ2rNNGxqfu1e7Ssg_qWFuk-HFFKIcGrl92ha04MIFUfttL9loY6W8if4Cf0ZbxSHOhBUXXD23Ls6sfaZNliaiq5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8wgrYKtP0kpglqXs2kwBWcQrchFpiF74RNV6jQXqelHrWskj4lxczsLXX9gER7cGztrzAFa9veCQJW4bJFs7WCtn1RqY2PRqxqZ42l9H9wSBO3tBGaSQpo0uz7q3GnbOvSJ0slC5oSf6jYfuEcd7ysPRGE-35_7EVQh6YaVTP3r6QyD1mmwtUra14PoCQPrzfFl384RXDtebiC33hw9ibdiJOx_G2SW39oxLSjCEX5VqhXblmEyf5FoMqKT79g_3HQqvNRgUmu_LJHbWZI4ddJkHl17deFfMcH7cR2ImwlY0diEwyzV4tcQRXaQsDR_7bV0XDIuyVqzmeju6i9bMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
