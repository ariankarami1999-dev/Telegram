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
<img src="https://cdn4.telesco.pe/file/W3ciE8AV0pkbirl9eXVsxWBWZUYrlKYbzvSXY8BN7gA6vvKXo1_7qz0Iptan7W2rIWA4Ml5MlP1OclZJlbEc2k5Twkg9me-6N-id8Uds314pf7Ga3SPxhul9-YYvbZ9Yuf5o33lGwlcs__rnTJo5JVNSm3E8RRR4hucBdKo1_LwRhJGIUzx3w3TuDjsoXG__p62I7qzdDw7Pq-wgHenCvfUjmZHUZKAuX8iYYuDsjfDJxB2h6ErpPzUZ9sqpVPVPoxouNqdPZXvZjPTSUPCwM7T49xlLao4KwWb6d_RJMUVS9NWWS_KJi1lI05dOrHExTRSYMZ7guKfqWLUCDkc4Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 115K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 06:08:05</div>
<hr>

<div class="tg-post" id="msg-70776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omV3GI9ZIjtikfuWNHWXGsFTHrwBTnARDxs98zHk1Ty9FvzTYDzzFJMbFliGuLDJ5DLQuZVfMZ-ex5xMHFGLA4ez3F00QOdSfNahWNsDdZ4g5Z2O0YlxMWJy4wHMDNqSgqyQJ1e1OJthCunIHHW9gyfsl0uiKojRvXoqPvs7Gjokyfs0s_h39bcJBomQfsU7YM8SGlwYOtHMya6Nt-4xNShcWUwdX5ZlAAyhZs-lN9T9UZalySBLAbVVsPhbhj065kvjzjwOOxabAKW_tkkiHVAIOdB3tvFpG6duGfGwOgaPpKnIHUJti0kahleqOVJo2B2XaHvIfwYorYfjd9eghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/news_hut/70776" target="_blank">📅 01:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26b389410.mp4?token=mnuw4metfeUqQ119oe68fzVYJQsW3rz0idYFdlgf18DVhdJiFutR_Q7cDJ_IvKQH0afg9BQ9zKLn7KgsgSld9cip4mXUT9Sdf-B6w0yar5pHQdJLpbEphW3S13iigij9_yqkudDlbzIjezJ3iv45m-dS-MF21uXv5KhSLn3phH-zpCZv7y44dG0aPQUt9IICuTA1gl0OR0W5OaKQlZxCL_4EhQFZU_C2YmSKv62SgIzDusNFz9BETz8yBqJOa91vCSJqvud_-oYb0GApmtbMMNPDrNSlpdcwon3UoLlriQIjVmkKXMPKXLZYFrJzz9fGejymzXEa8wqIR7CNBNg6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26b389410.mp4?token=mnuw4metfeUqQ119oe68fzVYJQsW3rz0idYFdlgf18DVhdJiFutR_Q7cDJ_IvKQH0afg9BQ9zKLn7KgsgSld9cip4mXUT9Sdf-B6w0yar5pHQdJLpbEphW3S13iigij9_yqkudDlbzIjezJ3iv45m-dS-MF21uXv5KhSLn3phH-zpCZv7y44dG0aPQUt9IICuTA1gl0OR0W5OaKQlZxCL_4EhQFZU_C2YmSKv62SgIzDusNFz9BETz8yBqJOa91vCSJqvud_-oYb0GApmtbMMNPDrNSlpdcwon3UoLlriQIjVmkKXMPKXLZYFrJzz9fGejymzXEa8wqIR7CNBNg6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپِ هوش مصنوعی، تابلوی «دریاچه انتاریو» را با تابلوی «دریاچه آمریکا» جایگزین می‌کند و سپس با آهنگ «YMCA» شروع به رقصیدن می‌کند
😟
@News_Hut</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/news_hut/70775" target="_blank">📅 01:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6d62ZQw0XC4RAjUlwqA9OdmWLwsPS-8vYuW8a0c70jnlrqXuwoA3fyuy4fKFuxn09YLEYf1IrlVNwyHntu2FiDAG4Itv0oYpPh6KMgx8XF4LTivteAu3JH6E-PxmlBs9tKYRiXvLhHPP6wQ35XajwJEvv2QovS6iIflkjkcFy8TQiQINHXc6qpPYgSJpiXtk68tyWtW7NcWNaAfgBwoYqmquY12frz-XqW4nyXMj9ptij2Bwbvd_UibMu1gILs1-wJUHfqDa_UavGcTHeVinu6wFyWnrDK4VGIayEk3Pe_HhfKmG4zoEtRFiu6Wdg_zapv3-LV9XFG2KldVe9h_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
باراک راوید:
دو مقام اسرائیلی می‌گویند که تصمیم به بستن تنگه هرمز توسط فرمانده وقت نیروی دریایی سپاه پاسداران انقلاب اسلامی، سردار علیرضا تنگسیری، اتخاذ شد.
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه را می‌بندد و هشدار داد که به نفت‌کش‌هایی که قصد عبور از آن را داشته باشند، حمله خواهد کرد.
اما به گفته مقامات اسرائیلی و آمریکایی، تنگسیری در پشت پرده دستوری صادر کرد که تنش را به‌شدت تشدید کرد: استقرار مین‌های دریایی در «طرح تفکیک ترافیک» (TSS) که مسیر اصلی کشتیرانی بین‌المللی در این تنگه محسوب می‌شود.
تنگسیری سه هفته بعد در جریان یک حمله هوایی اسرائیل در بندرعباس کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70774" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=t_l4dJIDLpz7yEz3N2jEndvsW9dwexBBtMosIDCL7ZSqfH9cUN3FTxXt28p7gP6Bonott0G05pGQH_NKRHxlFXIffxEXUMNtvG-Q3RJgDznHSSJNXGnubfupmceAVjWGC83_tK1yJaPp6-IsEJfcJ1Ok1VyUIdO7uBisiWpLj-8_tp_9y4gEnWx_lyr30bPvzdzz9CDdBWEZTatEqbhOE4jNecXBzPS7POMobJjjfTaT-WYtdf4PuhA_gUeya8nDQnGUz0fe_UOMxa0HL4c8RuFCvg1q3M6_pZkZqhPNvv-kjDFcc9ceY-4CP_mQxEueXjQemwm3hqqIJJWQpXG75w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d12414fa.mp4?token=t_l4dJIDLpz7yEz3N2jEndvsW9dwexBBtMosIDCL7ZSqfH9cUN3FTxXt28p7gP6Bonott0G05pGQH_NKRHxlFXIffxEXUMNtvG-Q3RJgDznHSSJNXGnubfupmceAVjWGC83_tK1yJaPp6-IsEJfcJ1Ok1VyUIdO7uBisiWpLj-8_tp_9y4gEnWx_lyr30bPvzdzz9CDdBWEZTatEqbhOE4jNecXBzPS7POMobJjjfTaT-WYtdf4PuhA_gUeya8nDQnGUz0fe_UOMxa0HL4c8RuFCvg1q3M6_pZkZqhPNvv-kjDFcc9ceY-4CP_mQxEueXjQemwm3hqqIJJWQpXG75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارتی شوگر مامی ها توی ولنجک تهران
😐
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/70773" target="_blank">📅 00:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051d44837a.mp4?token=Td5O2-2Iyz29vQK7MGuTELfiF8uYHg9okUWD-zT0aw9jOjIdQkivAdp-F4zMN6BEJwnYNA9d8Ao_LP87WSAzCN2a7oI2tDWakicm4PyLc4PR1OWgZ07WA2JKyM3XWYTd0lsEneOAnPu5MJwWsC3irYZw43yMY7ujgB_AysyLaW6HqFiJ4lRsoXnV9kbCBqJQQHUj6RzxbVzlYJ0oUrb3QfVBdOC1XbRaMirb_iVj2RwUJf3v18McO6gRKd3PpnXtx9jw-WYlmg8eP4EiK7cqnUZfeXqgkvL1jgoMSboKmUIqEnOlrLaDeiruTkwu6WrdbdLVNsIIz9cDtwe7Ij_4jgp1OmfC77qcpEUvBUKgveqPr04Rv7n3KUBlMdWEgRtRFh_o2zP2nL1AMru3lbcnItlBVtVmy5yGlJ23O8LW6XuCeHXcwjobjfH7uFVgCLc3XZSDD9h7dSYo0qhGm-nEsEXTBIXNyT4gSJkrWvvwEKDDQN6_FPMP6b0j2KeZdeT6O489dAYcEs0bdoXPrgkDEc7cfeNyYqReRhbGk1UYOE9Pg7lJHnSJ9hWyXjVF7bNAePSOnE06OEdqIp3DxYIJR8U8fcuAL4IN4WpA1H0nVWZVKCxLA2S2CEtIIT9Hl_1uS_hpiJrfE9UP6RelPpCo6cgS3EXFtbk71QkCo1fR-DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051d44837a.mp4?token=Td5O2-2Iyz29vQK7MGuTELfiF8uYHg9okUWD-zT0aw9jOjIdQkivAdp-F4zMN6BEJwnYNA9d8Ao_LP87WSAzCN2a7oI2tDWakicm4PyLc4PR1OWgZ07WA2JKyM3XWYTd0lsEneOAnPu5MJwWsC3irYZw43yMY7ujgB_AysyLaW6HqFiJ4lRsoXnV9kbCBqJQQHUj6RzxbVzlYJ0oUrb3QfVBdOC1XbRaMirb_iVj2RwUJf3v18McO6gRKd3PpnXtx9jw-WYlmg8eP4EiK7cqnUZfeXqgkvL1jgoMSboKmUIqEnOlrLaDeiruTkwu6WrdbdLVNsIIz9cDtwe7Ij_4jgp1OmfC77qcpEUvBUKgveqPr04Rv7n3KUBlMdWEgRtRFh_o2zP2nL1AMru3lbcnItlBVtVmy5yGlJ23O8LW6XuCeHXcwjobjfH7uFVgCLc3XZSDD9h7dSYo0qhGm-nEsEXTBIXNyT4gSJkrWvvwEKDDQN6_FPMP6b0j2KeZdeT6O489dAYcEs0bdoXPrgkDEc7cfeNyYqReRhbGk1UYOE9Pg7lJHnSJ9hWyXjVF7bNAePSOnE06OEdqIp3DxYIJR8U8fcuAL4IN4WpA1H0nVWZVKCxLA2S2CEtIIT9Hl_1uS_hpiJrfE9UP6RelPpCo6cgS3EXFtbk71QkCo1fR-DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصویری که صداوسیما و رسانه های داخلی از آمریکا نشون میدن:
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70772" target="_blank">📅 23:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=oLGr8mhesmHElgWMqF5t0p3sOenRIRnGfoR0WyRRokur24qu0cUeXR-QvUdfZHdSqNcK8T3XgvOcO3H4462H4Ejd6A5DnbAoDdBVK9yhK4ofhLmuT3Ib6BH-VkRPtSaChRxzpH2iIM3ufV2AXJLkw3TC5yzUWOQ1MNlL491EKR9_FzpQU0hktlGUQN8Z3JtZNHXa5zM3twHW1Fs6BVPrE37WNkmRf_WhLwAfV6XHOF7VNOcJalEslESriWie5wCZj8qYlTfnjXGLz1h2lsOYy4frp2FUBSxIqBhewICc808yGh_40w7vMVcPKatPKStp278L_4RgdJTNVFhd6VYq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006e88a7ee.mp4?token=oLGr8mhesmHElgWMqF5t0p3sOenRIRnGfoR0WyRRokur24qu0cUeXR-QvUdfZHdSqNcK8T3XgvOcO3H4462H4Ejd6A5DnbAoDdBVK9yhK4ofhLmuT3Ib6BH-VkRPtSaChRxzpH2iIM3ufV2AXJLkw3TC5yzUWOQ1MNlL491EKR9_FzpQU0hktlGUQN8Z3JtZNHXa5zM3twHW1Fs6BVPrE37WNkmRf_WhLwAfV6XHOF7VNOcJalEslESriWie5wCZj8qYlTfnjXGLz1h2lsOYy4frp2FUBSxIqBhewICc808yGh_40w7vMVcPKatPKStp278L_4RgdJTNVFhd6VYq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
«میزان، رأی ملت است»؛ اما ظاهراً نه همیشه!
🎙
روح‌الله خمینی در سال ۱۳۵۸:
«میزان، رأی ملت است» و حتی اگر اکثریت مردم اشتباه کنند، باید به رأی آنان احترام گذاشت.
اما چندی بعد، در سال ۱۳۶۰:
«میزان، آرای ملت است»؛ «البته مسائل اگر مسائل اسلامی باشد، اگر در رای هم مخالف باشید، باید تو سرتان زد!»
🇮🇷
🎙
سال ها بعد علی خامنه‌ای در پاسخ به پیشنهاد رفراندوم در ایران گفت:
«این چه حرف بی‌خودی است؟ مگر همه مردم قدرت تحلیل مسائل سیاسی را دارند؟»
⁉️
اما همین رفراندوم را برای فلسطین و دیگر کشورها تجویز می‌کند تا خواست مردم مشخص شود!
پس چگونه است که مردم دیگر کشورها قدرت تحلیل مسائل سیاسی دارند، اما مردم ایران ندارند؟
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70771" target="_blank">📅 23:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=dExJF8HobVewYiMaGluERn3zjE0BuWsQKLQsoBYNg4CIxR_fXlOSPANkP171-f4EKHNfELWrnORaqrwBkkq1AHfJFlBx1yKCrTKz4nwzekvz4HFNBl9Vw4wPrpHG9t_2b53mxuB95ShMoiVJc44s2jK6UUd0x5xHErttdwYW00okvfvDXAOdj31Dek050Xwkzqwh1vnxhfsE-L2b5uAlm_mHBIvlTBbrB61iRgOeISF-eerD748M0nHN8D0QEZtS0xLTq6Rk-lXGlvzfGJkD0oeFlXtSma45dKTQFa5ks5D7aQMoXbyU3JB_Q0L9OYnivUh4784yPbQ1a8KtZzIqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5c66fd58.mp4?token=dExJF8HobVewYiMaGluERn3zjE0BuWsQKLQsoBYNg4CIxR_fXlOSPANkP171-f4EKHNfELWrnORaqrwBkkq1AHfJFlBx1yKCrTKz4nwzekvz4HFNBl9Vw4wPrpHG9t_2b53mxuB95ShMoiVJc44s2jK6UUd0x5xHErttdwYW00okvfvDXAOdj31Dek050Xwkzqwh1vnxhfsE-L2b5uAlm_mHBIvlTBbrB61iRgOeISF-eerD748M0nHN8D0QEZtS0xLTq6Rk-lXGlvzfGJkD0oeFlXtSma45dKTQFa5ks5D7aQMoXbyU3JB_Q0L9OYnivUh4784yPbQ1a8KtZzIqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر رفته دکتر و میگه وسواس شدید دارم و نمیتونم برم دستشویی چون چندشم میشه!
برای همین دستمال کاغذی برمیدارم، تو اتاقم لای دستمال کاغذی پی‌پی میکنم و بعد از یه هفته که جمع شد، میندازم سطل آشغال
😳
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70770" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=hZjYkdn0aMVgqUk8n2x4DsgZACcMtsuXX_j4x7RjvdDKDmxz3DhOtZ_tMm2MpLG163is7U_-5z6DEaN8Obk435kKRblvKIdcQr-TuwqGRDXG9s1ljJksYWYOtoxPgJCoWU28mDm-qkQF8zQWqMCcd-f9r0rxZp7kEKDzDn4AuAQfre-bd5RuDd33GpkDYhymnaZw0tKn2rCbEwYlBU49YyCywOMQ6lsZOuezuPlu4Ilgm8leJg018h7WgxFOmZ6T0dd-h6xo6UM2tHCSgflAvN4BmlUuP59E6tbnNMaFdF7ilnJQDU0gCUBkg6WVY_7VXDjLvlLcSqFpyGPzmMkzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fdedcf94.mp4?token=hZjYkdn0aMVgqUk8n2x4DsgZACcMtsuXX_j4x7RjvdDKDmxz3DhOtZ_tMm2MpLG163is7U_-5z6DEaN8Obk435kKRblvKIdcQr-TuwqGRDXG9s1ljJksYWYOtoxPgJCoWU28mDm-qkQF8zQWqMCcd-f9r0rxZp7kEKDzDn4AuAQfre-bd5RuDd33GpkDYhymnaZw0tKn2rCbEwYlBU49YyCywOMQ6lsZOuezuPlu4Ilgm8leJg018h7WgxFOmZ6T0dd-h6xo6UM2tHCSgflAvN4BmlUuP59E6tbnNMaFdF7ilnJQDU0gCUBkg6WVY_7VXDjLvlLcSqFpyGPzmMkzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سخنرانی یه اخوند در خیابونای قم برای در و دیوار.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70769" target="_blank">📅 21:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=iqTDFKqlmegLPIZtC9WI2BCx5dZB4H1-WcdeucyFpuGEbczMwayFhi36F47h2MuTZCLCmDG2Sd8Ltyhn6ywXErHG1_0RGoHrcGk6lFrMPdoPyPNIJc823HUbECCsXov9YaNcDhaGOsLpR0IUnwGwbFi3g-ccCegGjAQ-PCZQEmEZbeWeFpXIqqRDDyU52i-N-2hp-o0t78wgFouAZFVMof3sXNs7GiTVjL8bmXG3N_4fu62sNmKigFW7UuQ_TyTy29KFQKxMqG-rdqqIdmV84qobLm91PBqbGpRUPiaHQlvPBUCf3yPHswcBS30FdwOJPrcOGZM0bAszLXARESdiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ada238f9.mp4?token=iqTDFKqlmegLPIZtC9WI2BCx5dZB4H1-WcdeucyFpuGEbczMwayFhi36F47h2MuTZCLCmDG2Sd8Ltyhn6ywXErHG1_0RGoHrcGk6lFrMPdoPyPNIJc823HUbECCsXov9YaNcDhaGOsLpR0IUnwGwbFi3g-ccCegGjAQ-PCZQEmEZbeWeFpXIqqRDDyU52i-N-2hp-o0t78wgFouAZFVMof3sXNs7GiTVjL8bmXG3N_4fu62sNmKigFW7UuQ_TyTy29KFQKxMqG-rdqqIdmV84qobLm91PBqbGpRUPiaHQlvPBUCf3yPHswcBS30FdwOJPrcOGZM0bAszLXARESdiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صدا و سیما:
تو رو به خدا تورو به ۱۲۴ هزار پیغمبرتورو به همه اهل بیت باور کنیم که ما تو جنگ پیروز شدیم
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70768" target="_blank">📅 21:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBj865gsflqa4IqXDbyRlwXmzQCEVf4Otd1hUVFf-b5_fAKw_CBo0avl0HXgtmiPckdvPlJ6Ic21Qz94pvY9nzKaXEaVDfcKqnV4OnqbLMLwrjlSyjn-nrOCDUhqV83Rf1duzBFnQ4ykm0Zr1sre0YD4tmr-heMbM_qiJMvrgtMrd2VmADgeFauiluCFFNc3TkG8m7mq8XpkKMxEvKKjeHPi9gcFKbypSwTUfWSle15B88AFSJ5XwN2xl9pcWc3i8JAuCchIWO5dOOvKXwqPjDYeYx1KLU0e2UenOUzDAd9bhrD7i4F0YT6Uagx3OSr1RhNxcCwgyGlsYD74JF6k7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
دیس قالیباف به بسنت:
دروغگو، دروغگو، شلوارش آتش گرفته.
برای ۱۳۰ دلار واقعی، به کارمندتان بگویید که آمار مودیز را که ۱۳۰+ میلیارد دلار هزینه جنگ را نشان می‌دهد، بکشد
از دیگری بپرسید که خیابان جین چقدر از ۱۳۰ میلیون دلار فروش استقراضی نفت را فقط در یک دور معاملات آتی برای شما سوزانده است.
دروغگو، دروغگو، بازده (اوراق خزانه‌داری آمریکا)آتش گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70767" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=AINPyO9M5vh2O0qT6MzdhAlfVyfWuvqaZHAMITDJyTeWJ3u7T9xRpvCynm6thXlRWUWidYfw3rwOMNG-9x7Aqxr2XYk3_b2BE76c8QXH285PDp_pqxuolgc_8A42vzjCtIXhGlWmy_SnqMqh8AHv_fySBLMGYzqjB9Bx7yfyPy76agt2dAWTqOukEh5MJPzl-WLffA5G5_wAc3bIjj_89y9IgZkAwk56QSmT8rYaPStiF7IOL763DAHUN4ZiKWOUjGSuK0BitpM55GZD4dnDWJiacXteL7j6gzA2EMI13ecAiot7vNe9m1AfQXzSr5TD7423yaPs_1gS4BmiEvcwL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379eb81ec.mp4?token=AINPyO9M5vh2O0qT6MzdhAlfVyfWuvqaZHAMITDJyTeWJ3u7T9xRpvCynm6thXlRWUWidYfw3rwOMNG-9x7Aqxr2XYk3_b2BE76c8QXH285PDp_pqxuolgc_8A42vzjCtIXhGlWmy_SnqMqh8AHv_fySBLMGYzqjB9Bx7yfyPy76agt2dAWTqOukEh5MJPzl-WLffA5G5_wAc3bIjj_89y9IgZkAwk56QSmT8rYaPStiF7IOL763DAHUN4ZiKWOUjGSuK0BitpM55GZD4dnDWJiacXteL7j6gzA2EMI13ecAiot7vNe9m1AfQXzSr5TD7423yaPs_1gS4BmiEvcwL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
دریاچه آمریکا توسط «اردک های دونالد» محافظت می‌شود
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70766" target="_blank">📅 19:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
صف ترسناک و طولانی ده کیلومتری یه پمپ بنزین توی سیستان و بلوچستان!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70765" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70764" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txCAKV6km2C7FyJYB-5OpAvje1MmPScIX69vIQwsnx05xxTklcUCLdALUK2T2e55JIQHOsugGUhSRfc-Rohj7fyIeLLO1oXU2gjYcmNWP7sSDqVHW7xhHgs7KLU4nj-fhGCi2ksudLmkh5OzW8YKKvzhC-C6MjJupqtvL2xWglAA6p5l360Icx8PTYN4Q3rFC6jmBCyhbtp2Z-dRdDUmq3-98XqfsUrDZuc2cA0oRLjDq_zUCkFmtKyjA4LLoqmt1qmJAAud2Dm4eSO9KXRW0gh_uPsQOUPKB_d4_X2X-TkXdTnjAjIDu5jmWcy64Gm8o0wZ6r2CjV77RNT14__A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70763" target="_blank">📅 19:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308edc2c2b.mp4?token=qd3rjQzHL8ILc79x3Tq5mzfth2qOsJDr3riasFjQWbYGDV_XVLBGUcVaanG927Q-ycNwdsgZPNX78NVOZIaNnY3BlHo9OKzi0hxwEc5NASM2MW-kcJINA4wx-pZwO3vfNEafXRrYjtwnlEd8BXPirzwMkY13pzHCqEi9zdzrEptMwH2PUrxfc6Q0dvSCcO4Rf2fBvpX7E30WGcWBFlsh9gfAL2F2Lz2yM8fdkkVEf5-D04_hrfj8YL0XeiMsJbrWnquzSmDBtRphNIZshRp5ZGO5J0OSU5g1OTzGa-A2UDzVMMgv2i5QsHMnKx8PGmPiZxll8BDR7Pus7PM1eGddfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنفرانس خبری علیرضا منصوریان در عراق که سوژه رسانه ها شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70762" target="_blank">📅 19:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddfb592e3.mp4?token=Xuzx1jg4Un8jeK-JLWY-C3MvJpM_kiqpeRiy54MhpaZ3rWmlPWHIAVBlYzRn4YdjTxIQu7l-veELtgQ67roxYiQVUp2ms6xbFnRbVjHZmVrT7NlYBM-_rzthbMmbJSH-17FgfhvCjiahXjt3R_ld30WZqdg56xTW9XHeuCto005jlVTRLSQt1iFof2TkUGGqyqwFBnS2-1j7ZifvwyrNUdGDbPnKDkjVeK4mdNgFezUthYLOMsmoAWL0u6UKR33XfMp6wsgjqJZNdXN6bUzwZgBaYXkY_uVjeP1tuTxqdgyFEowmfduyjd-Q935gbr2GSOAlJjH_2Ng-wto3yqUW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
رقص ایرانیان در شهر وان ترکیه؛
هزاران ایرانی برای خرید، دسترسی به مشروبات الکلی و تجربه تفریحات شبانه مختلط — که در کشور خودشان امکان‌پذیر نیست — به شهر وان در شرق ترکیه سفر می‌کنند؛ شهری که تنها یک‌ونیم ساعت با مرز فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70761" target="_blank">📅 18:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=jPCMN5HQXkJeU2ffscTcXYNgMIGZ4ExJwK93tdCbMuowYEPZT1pMgtVV3S0K3j3XilMt3dKu0SMr0S3kDyZfwCc2i61JFXQKQZt6jYf3Dv_1xJLYgf-Vb8XM6Tn8tlXyz0vcrloUls4CyanXfdAAEJeu2kmAspwaVeLNHRBNlfeZ4vCXGq6TrK-19TCJmjR8ISy6dQft1VYOXy-tWwGyENtqeFd1vlcdb6aH56A8ezFlkTg9Lx4Q42IT6jvIkczkPttijh9yNZxYY89EyH8NoVAxchgaYIWLhkogg01W6Lxg3um37ZKlBeVDGuuF-T36xH8pb4b92FlV-V-avQsg0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9054a10ac0.mp4?token=jPCMN5HQXkJeU2ffscTcXYNgMIGZ4ExJwK93tdCbMuowYEPZT1pMgtVV3S0K3j3XilMt3dKu0SMr0S3kDyZfwCc2i61JFXQKQZt6jYf3Dv_1xJLYgf-Vb8XM6Tn8tlXyz0vcrloUls4CyanXfdAAEJeu2kmAspwaVeLNHRBNlfeZ4vCXGq6TrK-19TCJmjR8ISy6dQft1VYOXy-tWwGyENtqeFd1vlcdb6aH56A8ezFlkTg9Lx4Q42IT6jvIkczkPttijh9yNZxYY89EyH8NoVAxchgaYIWLhkogg01W6Lxg3um37ZKlBeVDGuuF-T36xH8pb4b92FlV-V-avQsg0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر داشت چالش ضبط می‌کرد که دو نفری باهم برن غذا بخورن، تا اینکه یه خانم دکتر خورد به تورش و آخرش این شکلی با دعوا تموم شد:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70759" target="_blank">📅 17:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=voKdxmvm6P9WF-jG34ETypmB7fPXBXvejGPa2IcVT7MKXG_ChIRcz-8n9NOfhNNVRYkJHTU0RjrOlzsJ2tKzi8sc6SjWPlYKXxtyL1ATBE13IOLHTZ79fZXsIQxSArF5wRWY_UcFnbuVWJ8kzklOv9WTDETQ4hmfmjZ3-JyHBHhwNsXyQ5egn4oEbczmZKbxwHddfoEp3LwQIyzziCExJQ5fd1491aJoM6C4DnK5ElQ4XelIpVwclr66kN94oLfAez9g0toPDIaLL1ds8QMcBUrl_Gvu9l5itSZULbe1cWxaNoua5amLBZR6vww8j122vwFVr7Sv9HwBbaetfVc2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8867b7b84.mp4?token=voKdxmvm6P9WF-jG34ETypmB7fPXBXvejGPa2IcVT7MKXG_ChIRcz-8n9NOfhNNVRYkJHTU0RjrOlzsJ2tKzi8sc6SjWPlYKXxtyL1ATBE13IOLHTZ79fZXsIQxSArF5wRWY_UcFnbuVWJ8kzklOv9WTDETQ4hmfmjZ3-JyHBHhwNsXyQ5egn4oEbczmZKbxwHddfoEp3LwQIyzziCExJQ5fd1491aJoM6C4DnK5ElQ4XelIpVwclr66kN94oLfAez9g0toPDIaLL1ds8QMcBUrl_Gvu9l5itSZULbe1cWxaNoua5amLBZR6vww8j122vwFVr7Sv9HwBbaetfVc2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:
ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود.
امروز همان پوشک ۸۶۵ هزار تومان است.
باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70758" target="_blank">📅 17:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=kDBEpDBzK0krA-dgyIO4utT8r9NrKV8q9z3kMO6M6H_BfvXXjC430FBSCzwBykM6OrrR47fhdThmH4OAERF9eNsYdtlQoQF8HVdBky4zPMqCkvFpuZ8i1vMD3U-WfO_3qgZ3K0UCoeSZxvfZbQAKLj_UKL9o89-P01vsgpmTv4xZboz_aX4iDeq87ioYTHGLYWgK-n1tsV-0gavCwHdOM4RvUyfULCIhOmJUeak3-6UnJSA0JKcRXG_27ybbrGQi4nDzDGgKJkPWKHK5_1vZPHMHkd4fWu1WUtl8-CWz6-DYRHM7GPayj_I4OAP0IUB6A1Bn9nB2EOE42Nmehoz2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e620180d.mp4?token=kDBEpDBzK0krA-dgyIO4utT8r9NrKV8q9z3kMO6M6H_BfvXXjC430FBSCzwBykM6OrrR47fhdThmH4OAERF9eNsYdtlQoQF8HVdBky4zPMqCkvFpuZ8i1vMD3U-WfO_3qgZ3K0UCoeSZxvfZbQAKLj_UKL9o89-P01vsgpmTv4xZboz_aX4iDeq87ioYTHGLYWgK-n1tsV-0gavCwHdOM4RvUyfULCIhOmJUeak3-6UnJSA0JKcRXG_27ybbrGQi4nDzDGgKJkPWKHK5_1vZPHMHkd4fWu1WUtl8-CWz6-DYRHM7GPayj_I4OAP0IUB6A1Bn9nB2EOE42Nmehoz2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💀
این ویدیو از سرعت تایپ مسی شدیدا داره تو رسانه ها وایرال میشه
حالا جدا از سرعت تایپش فکرشو بکن لیونل مسی با ثروت تخمینی 1.1 میلیارد دلاری گوشی ای که دستشه آیفون15 هستش
بعد یه‌سری جوونای ایرانی با هزارتا قسط و قرض و بدبختی میرن آیفون17 میخرن و تو چشم همدیگه میکنن
از یه طرف هم بعضی دخترا میان میگن پسری که آیفون17 نداره کنسله و ...
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70757" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=L-Lmx4IjOzY50qZ30vvESnmg9UouaDMM5JmSJv1ypv17k0xfkZ92W2I5x9q5ivnncM8N8Od97OQl4LJ8jWLn2AjINOuqvwwwSenLFogrvrLp-GMDmaUegluUYyJI23jDQTF_mrieNpUSJ59ul5lTqoJ4fW8nY5YhvVT9UlIq5ziMPLOp1GRlIIetcGrlpqxbR26eFHoOqnkI7gPDNxUw3DbeQQATnLqsWdyjqU81wrulOcKwhRJ9iAoEgslHmGiRbBHNyCgGNsmJFLowLo-jcBxiwWdMtKA6x91-zwapFnzKGlM8-psZi_0pFXbGiJJa8QBtYwhNMze0MJamDuwqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d16a7d2dd.mp4?token=L-Lmx4IjOzY50qZ30vvESnmg9UouaDMM5JmSJv1ypv17k0xfkZ92W2I5x9q5ivnncM8N8Od97OQl4LJ8jWLn2AjINOuqvwwwSenLFogrvrLp-GMDmaUegluUYyJI23jDQTF_mrieNpUSJ59ul5lTqoJ4fW8nY5YhvVT9UlIq5ziMPLOp1GRlIIetcGrlpqxbR26eFHoOqnkI7gPDNxUw3DbeQQATnLqsWdyjqU81wrulOcKwhRJ9iAoEgslHmGiRbBHNyCgGNsmJFLowLo-jcBxiwWdMtKA6x91-zwapFnzKGlM8-psZi_0pFXbGiJJa8QBtYwhNMze0MJamDuwqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار در گفتگو با شاهنشاه آریامهر:
آمریکا و بریتانیا نیز، که احساس می‌کنند رژیم شما غیردموکراتیک است. شما چگونه به آن پاسخ می‌دهید؟
❤️
شاهنشاه آریامهر:
خب، من به آن پاسخ می‌دهم و می‌گویم که رژیم شما دموکراتیک‌تر از ما نیست، زیرا به نام دموکراسی، شما کارهایی را انجام می‌دهید که ما از آن‌ها وحشت داریم.
هیچ برابری بین مردم شما وجود ندارد.
تفاوت بیشتری در سطح زندگی و ثروت بین مردم شما نسبت به مردم ما وجود دارد.
🎙
خبرنگار:
آیا اینطور است؟
❤️
محمدرضا شاه:
فقط ببینید چند میلیاردر دارید و چند فقیر.
در اینجا، ثروت کشور، حداقل ما پنج قلم مواد غذایی را یارانه می‌دهیم
تمام آموزش رایگان است.
در سراسر دانشگاه، ما حتی به دانشجویان پول توجیبی می‌دهیم.
🎙
خبرنگار:
خب، اجازه دهید به شما بگویم که آقای کالاهان (نخست‌وزیر بریتانیا) مانند شما در یک دفتر کار نمی‌کند. شما چگونه به آن پاسخ می‌دهید؟
❤️
محمدرضا شاه:
آقای کالاهان نخست وزیر است.
من شاه شاهان کشوری هستم که دو هزار و پانصد سال سلطنت دارد، اما این کاخ را نمی‌توان با کاخ باکینگهام مقایسه کرد.
قیمت کاخ باکینگهام صد برابر بیشتر از قیمت این یکی است.
در گذشته، شما، بریتانیایی‌ها و دیگران که در اینجا نفوذ داشتید، می‌توانستید نخست وزیران را به دلخواه خود تغییر دهید و در امور داخلی ما دخالت کنید.
آیا برای آن زمان از دست رفته متاسف هستید؟ آیا همان چیز را می‌خواهید، دخالت در امور داخلی ما؟
ما به شما اجازه نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70756" target="_blank">📅 15:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuA_RttHOxXhFgjgOFTkIWonaPDuzIWYsNTTGp0vaokGpzyBV5gpNUbqinaXR9h7ExK48mYkpKZ28C50B9LgL3bwH3PLE-oPJ9ICIXnXA2qLIF6Qb_7CHQoo_tTE0sRm7Cz-Q-crDWuuvgU010PK-1fZi9phGir4wO9eu-iKDUk0SWYJhQWYGf4aQGLSjUUpIsmKISspuJ4W6dpzSbHYw4zkI3np-z5AceoMAjwvvz8IlQFnAaAv8v3UAp6F-C4uKReXVQb2pK09Wthv-VzBzLmVN4uDLJxJuVG9BZZf0ey24o3PjoiDdMPTzu0kTf173W6rHKcEH50cYg4I8FHxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی:
اطلاعات ما حاکی از تلاش‌های گسترده برای دستکاری بازارهای انرژی است.
عناصری در دولت آمریکا با بهره‌گیری از رسانه‌های ساده‌لوح، سعی دارند برای منافع شخصی بر قیمت‌ها تأثیر بگذارند و رئیس‌جمهور آمریکا را همچنان درگیر جنگی بازنده نگه دارند.
بازیگران همسو با اسرائیل نیز با ارائه ارزیابی‌های خوش‌بینانه، بر طبل جنگ می‌کوبند.
این مصرف‌کنندگان آمریکایی هستند که پیامدهای واقعی این وضعیت را با تمام وجود حس می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70755" target="_blank">📅 15:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQRsskEewdixh2mf0cEe1lGxHrzlc2tiZXlPLMK9dcv9DDxbpTPc_S0uWL9AhsHm8QhmXhEFk3-0e9JilsgAN9oUIOnI8JtxgtpVxZ4CLsj5r_3vq9g0_V58NiL8R6QI2kuGAupjQA_95-jXm0Hp5jDnc8zl6UEx54MfqH9oKwIFxpMWCRD7PojLjRmsECE1orgvYvatYYd9TjWHler2hW9tNpjblzeylTbbnBVP2O3wYaxms66CWKPfpM6SuLUqbcFdarZwgCrcvkbZ-rtu-SFwZowuDZglRi2FIxiUbgEni4zsSBEDL5z8IlDsCF4e5PypCYBiIHlzg1MaOrjJOGCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e307c52db.mp4?token=esR-m3Si9W2KIT784au45d2ZcU-VyPuTMo48bVrsluJ7HWgxru79isELDt8fB34y2GUD9uCHusNP18AxNg4dyNyRg561cIPeACICsw9gQzubjMOnlKFJIkSF36gu44FIrR0s_cOX-fq9FE27nfg3kssh7HDM1bu5GzIK51h89e0CkDen2zvuf3OvBQg_Q_J6C3k2k2pqbQ7LPXLjyhR_ctcmy-KzKQp8vkmJHIEmwPPBgmJOSaMfwypc7ffNIxYIAtOuQJR5doBgoi_QsjGyohaU3lYhN_33R_ho8Bi7MvOtDmPcdkumZIfFDxHKD-NJZ6JuhgAa4P5VK51exZ1iQRsskEewdixh2mf0cEe1lGxHrzlc2tiZXlPLMK9dcv9DDxbpTPc_S0uWL9AhsHm8QhmXhEFk3-0e9JilsgAN9oUIOnI8JtxgtpVxZ4CLsj5r_3vq9g0_V58NiL8R6QI2kuGAupjQA_95-jXm0Hp5jDnc8zl6UEx54MfqH9oKwIFxpMWCRD7PojLjRmsECE1orgvYvatYYd9TjWHler2hW9tNpjblzeylTbbnBVP2O3wYaxms66CWKPfpM6SuLUqbcFdarZwgCrcvkbZ-rtu-SFwZowuDZglRi2FIxiUbgEni4zsSBEDL5z8IlDsCF4e5PypCYBiIHlzg1MaOrjJOGCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
مراد ویسی:
۱۵ هزار میلیارد برای شیر مدارس «نبود» — ۱۵۰ هزار میلیارد برای خانه‌سازی حزب‌الله لبنان «بود».
بودجه شیر مدارس بچه‌های ایرانی قطع شد. عددش ۱۵ هزار میلیارد تومان بود؛ گفتند نداریم.
در همان حال، ده برابر آن — ۱۵۰ هزار میلیارد تومان — برای ساختن خانه برای اعضای حزب‌الله لبنان پرداخت شد.
وقتی می‌گوییم اینها ایرانی نیستند، عرق ایرانی ندارند، بعضی‌ها معترض می‌شوند. اما ایرانی بودن به این نیست که در مشهد و تهران و کرمانشاه و اهواز و کرمان به دنیا آمده باشی.
وقتی پول شیر مدرسه را نمی‌دهی و ده برابرش را به بیرون از مرز می‌فرستی، معلوم است که منافع ایران برایت مهم نیست.
بازنشسته معوقه‌اش را نمی‌گیرد.
گندم‌کار طلبش را نمی‌گیرد.
پرستار اضافه‌کارش را نمی‌گیرد.
بچه مدرسه‌ای شیرش را نمی‌گیرد.
اما بودجه هزار حوزه علمیه سر جایش است.
اینها حکومت نکرده‌اند؛ منصب حکومت را اشغال کرده‌اند. اشغالگرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70754" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4724327ae9.mp4?token=LrqgDbIBzJqPSy1xLbftRhLIs4obl5mBj30IENv11-8TsFelhozrLplYnZ2pcDgWSTAMPJAgayMoO0I39vkdP55pfbs3xuZY2ZudnQsrLBKrbjWFXCM6h3L61I0fjWmFQ7LVKq-KDSkCVlT8YpJw1lCcgaF4rcm-1FGsIuuHnSNzOHTp_AUY2ltXwoZKDcDzpH8zqq1_t2tvqT9mtpSyFaJ11n3MNzZmugbOwap-v70HD-fA4cnLzsoS3ZGLO1qFv1xCj4109YRT2q9QnscdG3n-3ELOVoxyIl2ni_G0IRBJrnITTfTeRShyiuJZywadJxguoOqs_swqc8BBFf-8PV4uDFYayLLsZWoU9lbzTicqh7bbIJgD_cXZdcw8V3FQxGo0RRRoGQumlrmtMEi7p-5SKK5sY-gHSD-ZXhzZqct6sc2YG4eUCvWMixPw-YgJSmPfNEdtRv1lS3SenmEYUG-NrVRtvrFnL4lvP-DZvqixBSpK9zS6WkiYEoq-rxXdvafzpKvfb5llN_tA4GQoIrTh3QYHnTKHbtc6eQC54woB_R8nEqPOlRy5MpUrj6gYNqhomIS_wZyqD3TTd844K-n9LJW-kcKOg4Yv2NJXl1lU0pQzIEvbGFSXR5-IhUHPW4lgYtL7DvZMK6-alOQSwgqYPNL31yFDJXxGbYIeMAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از شیرجه زدن تو استخر یه پیرزن دزفولی 85 ساله در بانمک ترین شکل ممکن
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70753" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDl7C-LJkbnvGt-r4FiAWmycU3aoOxHuoQjHHUCpl24hFvNCAeB_Y0oF1d24fzEnm5G98U2_2oCGArbfqqJJ0MO-UvQ453_C9aUtb6fQFy_P_9pqzc-T7kFNg5cPPLUHImmr9g9Gbbc_Py39Mm3eG5SbrnZdC6ZeGrif9UK0riueeVqU9vRTtnyEnj1CGJW3zn8S0JYuOC1jFpM_Tvoyfcxlpa9T08TNm00-J4La3x-OEZUOH4W5cuZk2tXiYVEyxYDJRGC43AhQlerRkNp8JmXM6K1kMSx2-q8U5ok6RTXz182Cw61Sptwjc85BORPwGSlIiODq6TSn8b1TXUXjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بنر یک عرزشی در تجمعات شبانه:
آمدیم امام زمان را بیاوریم
مجتبی خامنه ای رهبرمان را هم به غیبت بردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70752" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0b023677.mp4?token=azm1_wid_fXnrvrVQA_1jDVquKbmQkSvtPMZrHX95P-vGrbGkibK0wxSDMmQatTvh0eBpeBRXfz2wsSGDvEY3VUl8ckakLxSVVqvzNuXiJXLZdfXsulrIUHx1GgfOMuJbaTJL5B1timA_j0UbpcYwvQd4uzStYhSf_ybO0ew10yESbI0ettRKJtrrINzY7zb0_9AtbKOPjpRlUFBIox8WiW4Uc3Kw3YcEGZq82V1IFH8dKtYQgAYSJ8TI96-1Zl7ruxZ6Wib8AS1WVH9p9CZFrNW4B3ydzOpWMpE0aQrdaZiWzcbVNr8XvRZuBJyuwFlJwrvDhgd6sMqOYQnj-jFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مجتبی خامنه‌ای:‌
به طور جدی اعلام می‌کنیم که هر چیزی که به همبستگی مردم ضربه بزنه، ممنوعه؛ مسئولان هم باید حواسشون باشه حرفی نزنن که روحیه مردم رو تضعیف کنه یا باعث دودستگی و اختلاف الکی تو جامعه بشه.
🇮🇷
پزشکیان بعد اینکه مجتبی خامنه‌ای گفت "دولت نباید ضعف‌ها رو علنی کنه" :
واقعیت اینه که ما پول نداریم، درآمدمون کمتر و مشکلات‌مون بیشتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70751" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXhG_4bmQI130SoVlqIokrNj0sSmDpQG6yOxQ3C44PMpsB9jVpXW92bUe7wLlun3bh061nIq2bAq5HO8snf1836ZpGJmjIL8uBYd4vo1ctZeeKBPwwRbnBI5s-vjNoy4KfpAdHK022prQEJUWVDSWaYOqIjZuaqiJ-XJ-PaiVcdttC0HzE6SJLHA0WF8oqK0w6JK5ojgXWdqyRLKPjObugR9M0BoEeCkBNYZS09NpRrdUIBX0d35k5VSQkD1FyiePbEX4ssZ-ZPt0w2aaKGD8S_NIDb7eeOy32ZWbSUyYDiGBMPKwte6ymMcSx5jpTVbfJwOPE6hSeGdhsZvVJQ-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
گلدمن ساکس:
صادرات نفت خلیج فارس به سطح ۱۵ تا ۱۶ میلیون بشکه در روز بازگشته است که حدود دو‌سومِ میزانِ پیش از جنگ محسوب می‌شود.
نفتکش‌ها به‌طور فزاینده‌ای با خاموش کردن سیستم‌های ردیابی («رفتن به حالت نامرئی») و استفاده از روش انتقال نفت از کشتی به کشتی، سعی در دور زدن اختلالات دارند؛ اقدامی که به کاهش قیمت نفت از بیش از ۱۲۰ دلار در ماه آوریل به حدود ۸۹ دلار کمک کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70750" target="_blank">📅 12:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70748">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ed6f2f55.mp4?token=hsNYY2iVP0J6eJCuQtDi8Qsq6J9dqT_fvQtzLeYbfMkKCcGCSB4m0odltWm2UA-JviYqecNgm_soZVtyyOuCrCxRJUAS7GDwPPknW9oKNaotstyKh295rO38Wfn_crQk4OXYmwjbCklFD7EwYTgGBovzY1G-t-77lcSeT7rivndhaCKGMFfTuFa7L3EMPdg1Wqmo1M1TU1cSf-hv6EkQspHa99anRRe6BAfPGP8dbntYAzIcRi9-NNok0xrYsXw6h4CEZEtE50v3asV03ossvUGNRgL-zk8OqDIjlpLEmFiSINsABXOK15wwNUj-tCc6GB9Co8hb6bNCNi7JeHYW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روزی هست که اکسپلور تحت سیطره این بانوی بلوند ایرانیه؛
و خیلی‌ها از ایشون با عنوان "قرمه سبزی جاافتاده" یاد کردن...
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70748" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70747">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70747" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70746">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9FbQzYNwPvLp6hdzYk0kBbR5zYtNlNsyTI8j0wyGB2KDmZzUdOhibqb519xnwcjNc2yLDyDNvPGL6vgQHuvetkR2CNz9zqxwLvHy8KIDcWiRaNBJKtsEf8MZOcUJkbc-CX1o7HghQHEh7tcL6f8bRXjJNeLPUXp_n-x2L8jvhQxE552lKw_EiXH_cMVXqTM_wloS7RdJtcCjkhcjFzw4XLb-gO6ipFfiejzHuaEXAzxZepbBbmvbAz4hGJ0mPZAvlkSVNc5nbc4_d-nHSjwTOKBS2EPCchajnsY3Iws7sLTLltvX2NGIGGzIr0NGjprSHXSnISI5Y8nTpoOKGa2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70746" target="_blank">📅 12:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70745">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b5d02791.mp4?token=buWAoLNT6-I6M_N8o7ZC7HcNJ37mg4xo5doPzudUac0-01fuaBPiBn6e7xfXNAluQAph3oEFbZFJSQtIjsaQ89C4ox9cqN6paXMNgeLM5TvkqnMsMOMx4T1Td5mJeesdKcZ-A3YXNQPNa4ZFylmc91bSlv8YAuPa_MserTIGJXxcLDT-RKNn7TDrWm-kST2CSFu9cXwytQntK2QGLVtdshvRUSTRxnyaiLIootphcPNftE9jpLT5Y87Kpou3fzXSiBCk62Bj6x6Wo7Eeiff8DhNXLvS1agMGS75D_Hqfi7pUgwBggcTzoaF4euUKRJRiRaqi9KaxQ2zGpmDVspqu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شعرخوانی محسن نامجو درباره علی خامنه‌ای و جمهوری اسلامی، شهریور ۱۴۰۱:
یک روز مار صدسرتان می‌رود به گا
آئین خوک‌پرورتان می‌رود به گا
سیدعلی اصغرتان می‌رود به گا
سیخ و سنگ سرورتان می‌رود به گا
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70745" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALuhG7RHUsoUUxnkdVMNU-5rmfn99FYMAn2AXFYWfJKWnvEcmSVE-c6HcJP4BUdQp4nibvdjB0HLKj9cIBm9dFuMC13ajzoF5i3GUJhREAbOCEVMjSFh-59D7Et_DcNSmAMJX5zAnLn-ymEHkRADJbjYZDjPfJv1mU5GQ_KdrX3aGlyu-onMloRIewr2Kjcs8QMrb9wZ7uw6PzpZcSUvb16YhL1lISO63NLCTf3bz9wZch_YuIbRw33mWAAgjF-lq1zDMCk0ca0MD6meAvMr7cCy6gYlQL_z4iiAIPOSqvtP4AsaFAtkSZQ5_8r9S4wHhLa293TZC5fLBEnjVSfs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:
به گفته مقامات آمریکایی، ایالات متحده مقادیر زیادی موشک و سامانه دفاع هوایی را برای جنگ با ایران به خاورمیانه منتقل کرده و برخی از ذخایر خود در اروپا و آسیا را در سطح بسیار پایینی نگه داشته است.
به گفته مقامات آمریکایی، پاتریوت، ATACMS و سایر سلاح‌های دقیق به شدت تخلیه شده‌اند، در حالی که رهگیرهای THAAD و سیستم‌های ضد پهپاد نیز به منطقه منتقل شده‌اند. تکمیل موجودی انبارها می‌تواند سال‌ها طول بکشد.
این کمبودها، فرماندهان آمریکایی را مجبور به تنظیم برنامه‌های احتمالی کرده و نگرانی‌هایی را در مورد توانایی واشنگتن برای پاسخ همزمان به حمله احتمالی چین به تایوان یا تهدید روسیه علیه ناتو ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70744" target="_blank">📅 11:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cb56543e.mp4?token=Ao_n1vzSQktOH9mwLMUBG06XkpqGlaCQuWCvdbgD_XoMLfBMFmOERpVvEI14nJkoWIgI59mUrfCuPKMFclH2syiYZFPiUzmWy5b7EqE_3hUjcdDXGv_ByALvxrzQ6OSATYvV-hd7yoDTzjJMUydIY3rFI-Ntl6GaOquqJL1ggKwqnXLbEjn7Wp98s7-9mz7VAr7QVqpDSNCIN2i26azyzIGhOMvyAzc2GDMRt0VtrS_AECtyc7KQ5K_nTXV6xckYHnrYzT6-jNDYLxs4KgITnrBKdqQjGK6enW9Leiz2ZnkRKniVWUf66g8iSytqnFVqe8pk069LaHuXzLduPp9Lgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک دختر ۱۶ساله رفته تست بارداری گرفته و تستش مثبت شده:
فقط لرزش پاهاشو ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70743" target="_blank">📅 11:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1927e9cdc.mp4?token=N3OTNUmcfTYoooauDFOiMVpuMvzIP3YMIe4mpVX4T18Ls9mBQZJifyIzocbvGF4J2tZcaK_M1dCanMc344ZS7R4bdBTgYG7QNirF_mp_mEW_vWMO2XwgZHf3EKzYl-aYdoUglY16zF6eCAMrrMhfcyz03YAapJ1XP6OU7EZvLLXySkB7jhemQFMo6lW_5UPxrznk9ynUkgiduXAkJrmZ_qbNkoDrVIcLI-I0_j8bb14zWxOB3I6DDt0-FFQ_zCBw_FpHGpcUhk8FtK_tbjSq77JWLnte8faapb05WLICG-i1A6a8jlbj0D1gAxsb0gauns02blOmFd_sgJQkOZMCVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آیسان اسلامی درباره شاهزاده رضا پهلوی:
طرف میاد میگه این که نمیتونه تو ایران نبوده د آخه خارکصه برای مسافرت که نرفته پدرشو کشتید
میخاید برگرده ایران بکنن زندان مثل تتلو عکس بزنیم آزادش کنید؟
سیاست مدار نباید مهربون باشه که انقد حرف بهش بگن
خارکصه ها خامنه‌ای رو دیدید؟؟ کسی خایه نمیکرد بهش پخ بگه بعد میاین انتقاد میکنید؟
خامنه ای خار روحانی خاتمی احمدی نژاد رفسنجانی (پدرنظام رو گایید)
خب دیدین که با رای دادن نمیتونین جلو اینا باشین چرا پس ۵۰ هزار کشته دادیم ما
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70742" target="_blank">📅 10:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ccdcc3bb.mp4?token=owA4J1FMm_W60Xjinkt2nYEAX8ORVUtv0ZNYZY6TCH7ECasKm_TVT_ZNA74bqELdakCvWq4cGzx-JFpVeREPHCQiHdRVWgyD8aJjV__0ziQW4_yMgl551kzapXEH774VNnwc1T3GwmlcFGTJfNUQt60fWPAVyH6WHP7uX4yv05VfxXRMYTTRGro1OYip_tejU2A86ftoKAMDlTWhdmMJ7zKStzx-tPa3kC-L4-iP9iAicSBg_Ij1yFV6jxNbz7Z0wVpK2HaebyP_jqXQOZb9ycEbgK78LcVk49CZTkyCd7_DWYRfHcy8gjraoYBQDToCCHA3mcTn8ZExyp6SPiVJm2bgobIP3HNeAqgIgCoDokpaDS9RNHi4pEEmWm5XAKd48M3FzxdbbbwxB0N9275_3eMe-gI36NZ75GWidr4P5G3epnDLbrrF8LRC4CET-3SmKKOik7HpmwGkINQJmngWMUCikZg3yrQc82vLLpWc3B2nWxTIcN6pnxA9Af0cl6i3xmPMlHvsOb5WBHWF9w8CoRAWbl8OkJnwBPw1m7rIc9MNr2IoofceCtLIlCqbiyiH46wKTViIVCCx165FoSWy6GxilZXCvdj1zqd1VOjTsbkgS_tr-yMrN2_TeQVhDcbW3UlZs5Y2O20lGayi3zOYqmw6iNlV91m_Gxqi9-30XDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
این ویدیو تو اینستاگرام فارسی از شدت طبیعی بودنش شمارو وارد طبیعت میکنه و یادتون میره که این فقط یه کلیپ:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70741" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2bd8e631.mp4?token=R7jlCDusNnw3g6UGRz5SoVsHDcV3YsR6t6vCGraMtvuF7S3JuYtOQAOwOoFfvecOfi0CbKyv_R6ZdyqzjJyEeQYHwTaeQow8DLL_Ee7HsMfZx972exDf3MH1gQAnwAKX4i8lUKkptLr7kDWwaa0Bbu7mMmViH-iE8uraBEXwNNzVIl9ekaILUuzpE7vYTEJQll5q0gggeQOlf0Y0OCQ1t-KR4NQScJoe0WdzjaZmotr74xM4wlF3Vn0v2qOL9zTzPYlagPj8kjJUHDpGT6fEjLg7nN1H71Un58mDZoUhOSEOgYpSbF2COpuIw0fatG2TzpnoSz7-KjsMI9tBl5XZ7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال‌ شده از گلایه‌های مالی یه ستوان سومِ نیروی انتظامی:
تا صبح میرم گشت‌زنی و حقوق خالص من 21 تومنه!
با این حقوق حتی غذای خانواده هم نمی‌تونم تا آخرماه تأمین کنم.
به هرکی هم می‌گیم جواب میده که دست ما نیست.
من نه ضد نظامم نه هیچی، آقا به فکر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70740" target="_blank">📅 09:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8l84jHhem2V1LgwWIUWmgrPZZbV4megoqusE5tfb4Zi8IGms9VaYYyAs3TDvxuedGM8gB2veqOs-dtOP_caUwvBaopZ8W_IP4H6NjlbMbOEaQMz-7V4WkGUuOdb6bayjsKJy2cPihHFFW49aUHmqeo-vyrF_Boytstz81qlbq2c5KxwqGQOenPEtJ3zUtW9xqDbqfvcd5fCaCz4rlwoZMR0EJZa7k8vObyoMMKklvT5a0vH4sb5CajdeoVmvKNl3Hn0jF5m4WfkDQ62gKpy_w8q6AteQm0VDAvWIOSG7GBEPvpqDz1yqBl3VshgMYhgUjGtZue7bbD5mQQ200OFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
باراک راوید:
بیش از ۲۰۰ شیء شبیه به مین از مسیر اصلی این تنگه پاکسازی شده است.
مقامات آمریکایی می‌گویند تنها ۱۱ مورد از آن‌ها مین واقعی بودند و تعداد اندکی نیز به شکل اصولی کار گذاشته شده بودند.
تنگه هرمز باز است و آمریکا در «نبرد هرمز»دست بالاتر را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70739" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNO5hdDg9T5AdRqPbRkUzWxqH0eWcMBPIeMIFi5SFzxOCnhRzryylvqKDYGlM5aW0gHo7hhtNCEBrcmv8hWJnhNYzrOOONCpjzeNJQiGB92AgqZd79KuzGziiIacQQr1j6Ff4a5oX3pvJ9eQr8PA1NKN5HadwWW0gwdsKb6vwOPMb2Qh-NAjHkq-I9ySdT3rCiqxEZp75B3r07XTSJHaxvcihwvQAuer5vLEn4PVRedJ-Y9dySdsxS56R2DcEgp_Da4kASuMK_JKP3UCJKua7cxJyX8rVtr2NLg4rQ8cMIwxdTp5iikQBth1YSsx32BkeR9dq4acBm32p3v3CaMqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUkCvDTXl0hgrmXxCOlMkZBV0ayQt5R1e2jl5sL-Q1BTd1n2Oswns7eJsccFeEhHaTihS9SEJipG4h4OyuUss6II2xvUa4ZSzaTypUHU6ydrV7GsGjSi3VFwdaG-cNeTqpJJzGUWi8-FI1ZBcc_CZmvQGJZQtp4I2l0qNFQfeRQmfnaFIaprRhWc8Z0vsp__Rah0qCZXCXcBmIpz96-XKRwOXnZPOEjNnzBvJa3quoYf8ZNjNlSGm7GBktKRV4DGWMcKAGZl8BUbJM-fq_8jtJoZ6yJeAVdL-iqglTvWsINqQd9xKgyKd2NvDwUWD0btPLe--e4PXKd0l9xei-YumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مجری:
غیر از قرآن و نهج‌البلاغه، کتاب دیگری هم مطالعه می‌کنید؟
🇮🇷
پزشکیان
تا دلتان بخواهد. فکر می‌کنید همه حرف‌هایی که می‌زنم، فقط از همین منابع است؟
🎙
مجری:
آخرین کتابی که مطالعه کردید، چه بود؟
🇮🇷
پزشکیان:
آخرین کتابی که خواندم «فراجامعه» نویسنده آمریکایی بود.مگر می‌شود کتاب نخواند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70735" target="_blank">📅 01:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=jfMpbQCdDtbKhXoEDHxLZKznUnXuCdsBje1tPyzJX46EGIi3FvZk0C97duD2f5vzpr1DuKscUZiv2X5ZQ34Wb8wQ_uzZDJic1KI9yQtsDdARXQqieoKTLeZzdh4r6bojBYfvOeLAFxwvg65Miiy3JRHBvC_tuP8GZ_Azf8upbTqh_ZuAQd7XcmlEBqnvZl5AONf_3Dq4_3DG0j-yR9zuNWwyPn1OpcSMFDXaBP1PA5Q4k7CdhorUXtjHZGNvxzPuFsvHP-g6J0g4iiREULxpzyt8FaQ9Su5yEdiWGQ5fgtolhD3t38y6kDCD2luWqfCiegVSnvVyuk28RUfFd2ObMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=jfMpbQCdDtbKhXoEDHxLZKznUnXuCdsBje1tPyzJX46EGIi3FvZk0C97duD2f5vzpr1DuKscUZiv2X5ZQ34Wb8wQ_uzZDJic1KI9yQtsDdARXQqieoKTLeZzdh4r6bojBYfvOeLAFxwvg65Miiy3JRHBvC_tuP8GZ_Azf8upbTqh_ZuAQd7XcmlEBqnvZl5AONf_3Dq4_3DG0j-yR9zuNWwyPn1OpcSMFDXaBP1PA5Q4k7CdhorUXtjHZGNvxzPuFsvHP-g6J0g4iiREULxpzyt8FaQ9Su5yEdiWGQ5fgtolhD3t38y6kDCD2luWqfCiegVSnvVyuk28RUfFd2ObMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مسعود پزشکیان:
«زمانی که حتی پیش از وقوع هرگونه درگیری، با کسری بودجه ۱۵۰۰ هزار میلیارد ریالی مواجه بودیم... آیا این صرفاً ناشی از سوءمدیریت است؟ آیا این بدان معناست که مردم تورم را احساس نمی‌کنند؟»
«بدیهی است که ما در زمینه معیشت مردم مشکلاتی داریم. روشن است که... باید تا کنون میزان طرح کالابرگ الکترونیک را افزایش می‌دادیم. ما در برابر مردم شرمنده‌ایم.»
🇮🇷
پزشکیان:
«در این شرایط جنگ‌گونه و در این وضعیت اقتصادی
بگذارید بگویند
:
"من می‌توانم با همین شرایط و محدودیت‌ها مشکل را حل کنم"؛ آنگاه من دستشان را می‌بوسم.»
«نه اینکه به من بگویند "پول و منابع در اختیارم بگذار تا مشکل را حل کنم"
خب، اگر من پول داشتم که خودم حل میکردم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70734" target="_blank">📅 00:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tS_LyXge7nsPJiCWP0SxUIn_xW7UJiUHOC4BTneFN04UrHOVUzlfTB3wKu8phvWL9B8HBitxK9qLuuMjqazXba4UmagwIJ9vzyAz_pi7ZGLASDLvgsZsdIKaf5kB7YFypvs0THEUCBxBHbpdBuAwVwddi8HK3YbFN155VB8VsCJft_39VKAQ9eqyAZfPyFu-KUG5DuBG1_PVmGDUtt9iKAi7LWMa0Ho6r2gXOG-TDD9xwA2RHOn5quhsicYCoQ9oMLA4TxIFgkp9gGgu8IJxzSL0oAlmvfFFb40qmC7QyAQxJvazsvJl8XQZa4Kfyh-DTxHs-Xntl7DASPlAsKtYdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇫
برای اولین بار تور افغانستان گردی برای مردم ایران موجود شد.
قیمت تور ۷ روزه‌، ناقابل ۵۰ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70733" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=AQAtFF4g7DsMZ6-k-nqu05EOlmTBYRGBSw9FmbvBY3_Ldmx_IwuvUiUERJS1fxjLC_9X_dKkh62eaqERvLFwc6f_tZdd-DDvAswgMaFuQRhxJkitPFESS_Em3IxZnIvWyvW20MX-AdDrgo8WbYSBmwg4RB4s8mfnAAXmRtnuqvmq206grjqom-ToLpU_1X5bD-tkSdI7g1bZbmo6W62Euj2mJuzEmUGzWKntE9vpXnAcFd-TzgIKxdEQGwIVvXb9iU8L966yhdwAVb0l6C6f5RJrtEe0HWY1fqcpeyb5XNvAqewTqaJ1Pk6Uj288BSKesFYRwae-PFAUPy5FYvhEbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=AQAtFF4g7DsMZ6-k-nqu05EOlmTBYRGBSw9FmbvBY3_Ldmx_IwuvUiUERJS1fxjLC_9X_dKkh62eaqERvLFwc6f_tZdd-DDvAswgMaFuQRhxJkitPFESS_Em3IxZnIvWyvW20MX-AdDrgo8WbYSBmwg4RB4s8mfnAAXmRtnuqvmq206grjqom-ToLpU_1X5bD-tkSdI7g1bZbmo6W62Euj2mJuzEmUGzWKntE9vpXnAcFd-TzgIKxdEQGwIVvXb9iU8L966yhdwAVb0l6C6f5RJrtEe0HWY1fqcpeyb5XNvAqewTqaJ1Pk6Uj288BSKesFYRwae-PFAUPy5FYvhEbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
بنزین لیتری ۱۰ هزار تومان !
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70732" target="_blank">📅 23:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=j_DAFzUR8KE-jVZqtmK92iIzuWp0Hwu1xvtIUE-C1_KdaaCaewg5VYM6b6maOWVATZIqhDXun8NAj-SfDp2FdHyozTyoZ1JWYAPLcf2oCNYJAD5obrBV9zcEdVfamVpbh69lypoYJTJgv7oqgAJfR5gKugm2bH0ejRvB2q-CFXJC7i6uKaxtgG8BYhik7aj_V_hx4R-jUMqNC8HVpDxFZUBtE2DMjOrVSF3YB6pJt3SG6lWqjNaMhl6Pa4iabqg8GLKW_9wqu8V9LsWlbLa8X3mrorIGQYZ64vNI_8wnt6MoD-hmArkIvTCIVsoKFJi3FPNxFSIiXQTTVurLzHQzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=j_DAFzUR8KE-jVZqtmK92iIzuWp0Hwu1xvtIUE-C1_KdaaCaewg5VYM6b6maOWVATZIqhDXun8NAj-SfDp2FdHyozTyoZ1JWYAPLcf2oCNYJAD5obrBV9zcEdVfamVpbh69lypoYJTJgv7oqgAJfR5gKugm2bH0ejRvB2q-CFXJC7i6uKaxtgG8BYhik7aj_V_hx4R-jUMqNC8HVpDxFZUBtE2DMjOrVSF3YB6pJt3SG6lWqjNaMhl6Pa4iabqg8GLKW_9wqu8V9LsWlbLa8X3mrorIGQYZ64vNI_8wnt6MoD-hmArkIvTCIVsoKFJi3FPNxFSIiXQTTVurLzHQzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای انتحاری اوکراینی از نوع «شاهد» به پایگاه هوایی «انگلس-۲» در روسیه حمله کردند؛ پایگاهی که میزبان بمب‌افکن‌های راهبردی نیروی هوافضای روسیه (VKS) است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70730" target="_blank">📅 23:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=rrisaKTk2NDKxUIeamDQZhFNBJHpAdfKi01XO1842XmewdmuxAhsmqMcnzk6PJlDNBh0nwJ-iM-SJ6oXvsfBiwmNqOldEsh9vxh0Kbtq5Y0uBLjQ6wBw5iE7cQ_FU0VToeK7uwMyd1kzjbC-ULoZt3x_m142fr1sTZcrvQREPMxAOWn5E0QCEplW5qTaF08ww6I5jsCfX5FHnjHBhl4WrXzVW-l04Hs2360Vxf01Dk80Mb35GFYwWtHXIF4M5pS-QZBHYTONk77u4QPJJg-byXZnmHA1W4oHi2tW2SJSzVoFmUnVnHXoSV682FGqQ4Rcx-f53Azo6ZCu-I5MQ2cU8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=rrisaKTk2NDKxUIeamDQZhFNBJHpAdfKi01XO1842XmewdmuxAhsmqMcnzk6PJlDNBh0nwJ-iM-SJ6oXvsfBiwmNqOldEsh9vxh0Kbtq5Y0uBLjQ6wBw5iE7cQ_FU0VToeK7uwMyd1kzjbC-ULoZt3x_m142fr1sTZcrvQREPMxAOWn5E0QCEplW5qTaF08ww6I5jsCfX5FHnjHBhl4WrXzVW-l04Hs2360Vxf01Dk80Mb35GFYwWtHXIF4M5pS-QZBHYTONk77u4QPJJg-byXZnmHA1W4oHi2tW2SJSzVoFmUnVnHXoSV682FGqQ4Rcx-f53Azo6ZCu-I5MQ2cU8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبتای یه مداح؛
روزی بود یه میلیون حسابم داشتم رفتم ده میلیون چیز میز خریدم تازه پونصد هم حسابم موند
خاک تو سر مسئولی که چوب میندازه لای چرخ اداره این مملکت
اصلا دلار بشه یه میلیارد رزق ما دست خداس نه دلار
دلار ۲۰۰ تومنی هزار تومنی ۱۰۰ تومنی همش یه عدده مهم نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70729" target="_blank">📅 22:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇮🇷
چندین موشک ضد کشتی از سیریک به طرف تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70728" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=IiSkqiOQgUA0JvarnWKSuL7iWgxKXLVTNFlG0l1yl00R3JGGXZi7OWD7HVzW94yN4awsuhHRZnn0HPQxwzXeFbazoSfBNB3L5ojNSR_Q72I4cLi51r6LyNWBKXKRH97Z1cDkKbx1KLRu0f65-jsSuFG80fs3AyQertMrbAtF7e2SzazpSmUsN8yk_TE3iCUtsckzPoi74FJADAGdPKTid0o2ghf_X5FWfAnfFJHBWUF1G3CjuPlapKIbM4Q4ot5an88Q7ewYdZf7wwu3hyV63Ar0jqh5YBdCxoophchYqhfGSWzNEfynU4avpynXlxQ32llUkO_-0myvYaJCsDcTTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=IiSkqiOQgUA0JvarnWKSuL7iWgxKXLVTNFlG0l1yl00R3JGGXZi7OWD7HVzW94yN4awsuhHRZnn0HPQxwzXeFbazoSfBNB3L5ojNSR_Q72I4cLi51r6LyNWBKXKRH97Z1cDkKbx1KLRu0f65-jsSuFG80fs3AyQertMrbAtF7e2SzazpSmUsN8yk_TE3iCUtsckzPoi74FJADAGdPKTid0o2ghf_X5FWfAnfFJHBWUF1G3CjuPlapKIbM4Q4ot5an88Q7ewYdZf7wwu3hyV63Ar0jqh5YBdCxoophchYqhfGSWzNEfynU4avpynXlxQ32llUkO_-0myvYaJCsDcTTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجید شریفی:
جایگاه کره‌شمالی با جایگاه ایران اصلاً قابل مقایسه نیست
اگر ایران سمت سلاح اتمی برود، همین چین هم شما را تحریم خواهد کرد
مطمئن باشید به اندازه‌ای که روس ها مخالف اتمی شدن ایران هستند، آمریکایی ها مخالف نیستند؛ این را مطمئن باشید
بازی مناسبات قدرت است، بحث دوستی و اینجور چیزها نیست
به محض اینکه اعلام کنید سلاح هسته‌ای داشته باشیم، مطمئن باشید با تمام قوا حمله خواهند کرد، هیچ حد و مرز اخلاقی را رعایت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70727" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209278afcc.mp4?token=UV0TnEDO4W-FMLO-oiLGcAetroF0d5pRWFryoggNAzIuK_e8OLLiN9dW3Lx-K6jikyiZjI3DO7ZR06eYdIFjdkrE6G-yeEnXNS4hBUl2YZNObTOf3Go9KhXvtw24VReXmBO1cYljDCVYCkbvRKbM_ely2WNUjk4gmYBbpx8fam2o_B2UkO-3-sEEGLgokbtq5jxNT0PsPF1Jfb8UxXrdMzB_j-D08ZixpapCURT-FpleZbITlaJP87melAsCFhtap80lBEyM-Rv8FXFHen5x6LAmzNeCthq4syUIW4WOR8gztKhEVLoFNkgoniMY0KDkfI52bO1lCTdvlDOIqwtQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209278afcc.mp4?token=UV0TnEDO4W-FMLO-oiLGcAetroF0d5pRWFryoggNAzIuK_e8OLLiN9dW3Lx-K6jikyiZjI3DO7ZR06eYdIFjdkrE6G-yeEnXNS4hBUl2YZNObTOf3Go9KhXvtw24VReXmBO1cYljDCVYCkbvRKbM_ely2WNUjk4gmYBbpx8fam2o_B2UkO-3-sEEGLgokbtq5jxNT0PsPF1Jfb8UxXrdMzB_j-D08ZixpapCURT-FpleZbITlaJP87melAsCFhtap80lBEyM-Rv8FXFHen5x6LAmzNeCthq4syUIW4WOR8gztKhEVLoFNkgoniMY0KDkfI52bO1lCTdvlDOIqwtQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بعد از حذف شدن سوریه از کشورهای حامیِ تروریسم؛
احمد الشرع، رئیس‌جمهور سوریه، به یکی از فروشگاه‌های دمشق رفت و اولین تراکنش پرداخت با ویزاکارت(کارت بین‌المللی )رو انجام‌ داد...
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70726" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=f22JUw4uP34zt0FXY6Zep9lAy-fVB2pVHKHH--P8jKO3oVw0ue2VcjzoZ9zXilbQmUu2FjEPT7fbZ6M8g7c7MSRGnFBa6D1aa8FsR9gzhKXYfVZ5_8Z1NT-NOK4XOfwWJ2BANa7hmDK5tMztHEKJdSXD_ZA2Oj_Itcv_pVbpeZm3ZMXY_pm-8mlwkk-ZuQTBL8fAYH0xM2dtN9D7EAiLWPj9pHaJuBRA3NV3FBhi96aaB8iMqthANk5Bgf1USa-kMXZPZgZiM7RabqK4w-WsEJqi84n4plZ0ZdeCiUZPJ-rwAiAGONZZas38mSbVUXiocQ-uTUwxclcywW8AVgRh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=f22JUw4uP34zt0FXY6Zep9lAy-fVB2pVHKHH--P8jKO3oVw0ue2VcjzoZ9zXilbQmUu2FjEPT7fbZ6M8g7c7MSRGnFBa6D1aa8FsR9gzhKXYfVZ5_8Z1NT-NOK4XOfwWJ2BANa7hmDK5tMztHEKJdSXD_ZA2Oj_Itcv_pVbpeZm3ZMXY_pm-8mlwkk-ZuQTBL8fAYH0xM2dtN9D7EAiLWPj9pHaJuBRA3NV3FBhi96aaB8iMqthANk5Bgf1USa-kMXZPZgZiM7RabqK4w-WsEJqi84n4plZ0ZdeCiUZPJ-rwAiAGONZZas38mSbVUXiocQ-uTUwxclcywW8AVgRh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇵
ویدیویی دیگر از آنچه در نپال رخ داد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70725" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-taLyKPEQ8j0qGxlwYAzMSx5oPbdHLjTR53Yy2uos00SYJEG-0Cek6F5UPC8JwyWew8ml4OSZw_Xo-mlj1A8YQXI_dX7_8dqw9jMAYdrIivoM-_vvKbVvwiezxnL8jWNsXvYrEkOn2-xxvdDtOwjhLimQC6lbVJV9OTrzaFRve_EWMgWGo6mETahTQh-042XVrKfodz9rRTSZKRr1WjtOx4gPa-AVu8sx0G9yoIMNq4tvGcwsk7VUx5lpbLRItUHzm0P-VYd5gn2r2jGnQ2cmUxAVV_7KVrYfgdln_jCV8csuBYn8U5341QcCi_w8PLTwjl9-80wjQ-W8tKe6MFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داد که تمامی شریان‌های حیاتی اقتصادی باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید ناشی از رژیم ایران پایان دهد.
ما همچنین هشدار دادیم که حامیان و تسهیل‌کنندگان فعالیت‌های ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی بهره‌مند باشند.
بانک «مصر» (Banque Misr) در امارات تصمیم گرفت این واقعیت را به بهایی گزاف و از طریق تجربه‌ای دشوار دریابد؛ و امروز، ما نخستین گام را برای پاسخگو کردن این بانک در قبال حمایت‌های مستمر و فاحش آن از رژیم ایران برمی‌داریم.
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای جرایم مالی وزارت خزانه‌داری آمریکا (FinCEN) مقرراتی را پیشنهاد کرد که دسترسی «بانک مصر» (شعبه امارات) به خدمات بانکداری کارگزاری با مؤسسات مالی ایالات متحده را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری، «رضا محمد تأیدی» — مدیر شعبه دبی بانک ملی — و همچنین یک شرکت پوششی مستقر در هنگ‌کنگ را که در پولشویی وجوه برای یک صرافی ایرانیِ تحت تحریم نقش داشته است، تحریم کرد.
🔴
«عملیات طرد اقتصادی» در حال قطع آخرین شریان‌های حیاتی مالی است که رژیم ایران را سرپا نگه داشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70724" target="_blank">📅 19:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_mtyOh0k-31ldDcpRLDIE-9bLX-JUnAA59ncO-EcPBNW5mei35BzxYYqh9xal0nBFJ4hAQT59nCUWYAzxSH-BG4ymNWrsJLLZ70R9MNVv6Vk9t5G_ddRjWOAonLkJ8npoZ4_nvZ7akQOuij_8KLJ_jX_jdU26HRNSW9bpCeDd5HDTDVlVW05A6pI7xDfw8lYWwDYpL8f3e_1hQ3i-o4n90u7-I4fUYOtYDNg2G9h7SjHmA-g_y0VBwZBtTtHfA01p7XF3_9rphQl7Mrh3YKrpKFADgWslyvbO1nHvPA1sDrlYMIds26FdGNwUyLhQUApeYWGsmEH72j-NqiF-sO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ: دیگر خبری از آن آدمِ مهربان نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70723" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=N5Dh-Dc02sVT1b4K-4ksT6y697F7IulNspb2P_MvIXKc9tj91BUwDrVqq5MTl-m53rIZNx-7aXamU4U9F0fvwei96Dqc937Imn_ebW4H1qgG8DETaZ_wP5qu-q_O_JQA7ba8mPMaj4HiVv0qIvpVrBZtYqp22eUd-V3C8HOTIBwyMxvBZRpDOtajWYHR5IiPWsz_oeSJYL1LlwC-SMboFcJK3yxqxDd1fIvR6HbE5rWeoR3wtiWbOR7lNBcCM6T6dLXHZuFk8iPvOq_UgCV03Nz31T3Ul5G_PeUWbfXgxMI3tFApXjEVEfHFjfJUGBbaTe7dp3OUx23DvGzTQ4LhoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=N5Dh-Dc02sVT1b4K-4ksT6y697F7IulNspb2P_MvIXKc9tj91BUwDrVqq5MTl-m53rIZNx-7aXamU4U9F0fvwei96Dqc937Imn_ebW4H1qgG8DETaZ_wP5qu-q_O_JQA7ba8mPMaj4HiVv0qIvpVrBZtYqp22eUd-V3C8HOTIBwyMxvBZRpDOtajWYHR5IiPWsz_oeSJYL1LlwC-SMboFcJK3yxqxDd1fIvR6HbE5rWeoR3wtiWbOR7lNBcCM6T6dLXHZuFk8iPvOq_UgCV03Nz31T3Ul5G_PeUWbfXgxMI3tFApXjEVEfHFjfJUGBbaTe7dp3OUx23DvGzTQ4LhoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دوربین مخفی ضبط میکنن از رفتار جامعه با دخترها و پسرها؛
وقتی دختره بنزین میخاد صدنفر برا کمک بهش می ایستن
ولی وقتی پسره درخواست بنزین میکنه حتی یه نفرم حاضر به کمک نمیشه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70722" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70721" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0IcVBGAolk43GmeV1m4k4zvqV2qp7vdW52kCaTDmZR_fYboW2IQ5hNZ9u6Eo1dPkHu3H8B4IqPWEXoOeI68DSc7U3rk2B6-Iswet06HyFKT4ZlBzh63PpiZgsfWXb-nI1EMGsyV1x30k4R8J9hLkOUToiYMtVt5AYJtRHsbAL8lA42b-7di9_n_Inm-VRjnLIJXtghaA8HjS4QyFc7F3TMTib97Gwh4_rnfIXPLo3JQpHYSrJ2jXxrSZ56T1bhsQsyKk-jCYXzqWX5Y9QzpPmGC3Oihx-f2Qck_qTWFblvAhsZPzA3eEqKrKee_A3Ip6lQPQK-s4PbrUmG-ZJ6vCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70720" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=pCLemE3aGYWgHGfoJmAcvDgTwCL7IIdLwKfMlb4xVJw10RnofdvifJy7saq1z1qWpxwkJfy_jQuji9kSZVRhly8p-jRjicvNOQ8rwE1SHAgxxvvRbVf-ZgCu6LTfbfgsddbMoQwKpjX0lDRg4k-aWkfU1C4Nahv6YJQ7Ndti-Oc4PeA1pn90OZBkauF3rUzO81dILBqcCkhe384L10ZM-U6PGDkZ4yFbq5RkCe_Z4vtCVGD99ZFybl2_h945oJUT5jvcc8eTaPF9zgmdbUp-kVqGNWsJFgznluUQ1aCgx0fkozBwvI7DT54OSz_ogTFElb8xVM5sXs0P14OppORYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=pCLemE3aGYWgHGfoJmAcvDgTwCL7IIdLwKfMlb4xVJw10RnofdvifJy7saq1z1qWpxwkJfy_jQuji9kSZVRhly8p-jRjicvNOQ8rwE1SHAgxxvvRbVf-ZgCu6LTfbfgsddbMoQwKpjX0lDRg4k-aWkfU1C4Nahv6YJQ7Ndti-Oc4PeA1pn90OZBkauF3rUzO81dILBqcCkhe384L10ZM-U6PGDkZ4yFbq5RkCe_Z4vtCVGD99ZFybl2_h945oJUT5jvcc8eTaPF9zgmdbUp-kVqGNWsJFgznluUQ1aCgx0fkozBwvI7DT54OSz_ogTFElb8xVM5sXs0P14OppORYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری خطاب به آخوند:
یه چیزی بگم باورتون میشه؟وقت تموم شد.
🙁
واکنش آخوند:
خوووبه؛اگه اینجوریه که من دیگه اصلا نمیام اینجا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70718" target="_blank">📅 18:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55129dd199.mp4?token=dZqxe3b4dU8rGFXsG_p4VOJ6n45P8HRcb4TnDisuccy669sMUI-Z8jlVxmM8XuRd2tAIN0ejBoIHrRF6Nvtk3IRULKIa4RGqVKoC3oYEL2rn7CArkmxaSy__MPTpI6TTIayK8OtRRvSgwZU7HcgrPj-cOfRwLPEFV8ewC7ET271Tigkm8mDKFjcbR-3P9IAlXZMTdDPrNS9S3q9Vm0bej2BZAzSsYP9QMD9coiZyhlNvqf8Pb6a79jC2E38Hu3LfxCkPDAqe_MB_Rocmk87N8e3WGP9awVOvvjyetKR-BxumoRm8pyZvlvjuVTEsQFtqF6FrRTtmzeqmCXZq9YcXNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55129dd199.mp4?token=dZqxe3b4dU8rGFXsG_p4VOJ6n45P8HRcb4TnDisuccy669sMUI-Z8jlVxmM8XuRd2tAIN0ejBoIHrRF6Nvtk3IRULKIa4RGqVKoC3oYEL2rn7CArkmxaSy__MPTpI6TTIayK8OtRRvSgwZU7HcgrPj-cOfRwLPEFV8ewC7ET271Tigkm8mDKFjcbR-3P9IAlXZMTdDPrNS9S3q9Vm0bej2BZAzSsYP9QMD9coiZyhlNvqf8Pb6a79jC2E38Hu3LfxCkPDAqe_MB_Rocmk87N8e3WGP9awVOvvjyetKR-BxumoRm8pyZvlvjuVTEsQFtqF6FrRTtmzeqmCXZq9YcXNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چرا یهودیان بهترین بی‌سیم‌ها و شرکت های اینتل و راکال رو دارن؟
⏺
مهدی طائب؛ کارشناس مذهبی: چون حضرت موسی یادشون داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70717" target="_blank">📅 18:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508daa856a.mp4?token=BbYxZI9OsglSXQV16fSzsnoqGKE9tJLdzCdp5Y6FRLJynvsCKedI-R0FdzXo-79d3_6jcbLyq4FCGaKVaBkJdYuIuKYdnWWlY5tYuZGC_sv2ASgE_QORnrb9nopGMbYLxU9LxQiA60aYUK6RY5_Ildir1v4wp8RZ5CbPbQgTmKeeNDKNAoJwCt7sMqVw0M_1gX5Zw9Z92tpcDM34-mmXd_qnIiQYJqSiZK9uRlls-U929zYbonNKD2xJCWoLtWUF0xhw3SG1IOjGvQM91Uv8mYcz0615c_kchXvkYNhylQWkIeJWKHHKFcM61UI1aWWpm_JhriUKh-mAdZh6UGausA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508daa856a.mp4?token=BbYxZI9OsglSXQV16fSzsnoqGKE9tJLdzCdp5Y6FRLJynvsCKedI-R0FdzXo-79d3_6jcbLyq4FCGaKVaBkJdYuIuKYdnWWlY5tYuZGC_sv2ASgE_QORnrb9nopGMbYLxU9LxQiA60aYUK6RY5_Ildir1v4wp8RZ5CbPbQgTmKeeNDKNAoJwCt7sMqVw0M_1gX5Zw9Z92tpcDM34-mmXd_qnIiQYJqSiZK9uRlls-U929zYbonNKD2xJCWoLtWUF0xhw3SG1IOjGvQM91Uv8mYcz0615c_kchXvkYNhylQWkIeJWKHHKFcM61UI1aWWpm_JhriUKh-mAdZh6UGausA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشماتون بریزه؛ یه پسری داشت توی خیابون قدم میزد که یه پیرزن رندوم برگشت بهش گفت: تا حالا کون کردی؟ دوس دارم منو از کون دار بزنی، حشرم بدجوری زده بالا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70716" target="_blank">📅 17:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=euIQvjCCILz6WxHQj82N6ZBimUM0RRBlZDL2O1NOMeoStLtUxNgp941wDoqOLTja5kIKFiUrB7hNdkTzYD3SSqe8kKz6M2CQoy9DrHiHwAiKKyiNuBp65403nU8x4vQ09ttYrfKZ8kUU0l2V99IKUDdP9ROCO6t0XGWHU9QjN4AdCoN4yASBLrKR1rQ4wLDnqtTa8HK-9zxAtTng8c7qcdETeUoxa1xjIR69JroheKtSph2wPCII25XuSPpRCBuypEzrT776fNzF6SmdfaMTw8le6m4U4vFfjzxv4pZyhC1FlX8TSNH90tgMCKs3DcakFytgi0woUwljPS0ZQgqAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=euIQvjCCILz6WxHQj82N6ZBimUM0RRBlZDL2O1NOMeoStLtUxNgp941wDoqOLTja5kIKFiUrB7hNdkTzYD3SSqe8kKz6M2CQoy9DrHiHwAiKKyiNuBp65403nU8x4vQ09ttYrfKZ8kUU0l2V99IKUDdP9ROCO6t0XGWHU9QjN4AdCoN4yASBLrKR1rQ4wLDnqtTa8HK-9zxAtTng8c7qcdETeUoxa1xjIR69JroheKtSph2wPCII25XuSPpRCBuypEzrT776fNzF6SmdfaMTw8le6m4U4vFfjzxv4pZyhC1FlX8TSNH90tgMCKs3DcakFytgi0woUwljPS0ZQgqAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=cPDe3vSv_F0nwN0WyPYTmm9MAn25Nwe-2f17_fsWmoiiA_4GKmTl4CSIQuwE2hnUPaznl6UzJTCek4NNcmlrIC4EJvImfyIfpKVzhWtpxQ8eUrpFyTPB8bqIesYJ6FiYb-SkMzpFEEEpbptUw0CIGIm7b1ksdlfAP74U28EsaD3gHtLAqHGZGf_hgps4MgrDfQ49Q908O9PwxUoRO2OBL23YAfTeczdFlYHP_AhfJ3uI8qGHVkP21lDwBhRWps-IOxX5ln7apUhkpLiMUZ7wvlBOqO2skQ5OQihomP04wSrMd8XnSgr0OsJltwT-fSWkUOgDpJLJw7CPhrpM52CeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=cPDe3vSv_F0nwN0WyPYTmm9MAn25Nwe-2f17_fsWmoiiA_4GKmTl4CSIQuwE2hnUPaznl6UzJTCek4NNcmlrIC4EJvImfyIfpKVzhWtpxQ8eUrpFyTPB8bqIesYJ6FiYb-SkMzpFEEEpbptUw0CIGIm7b1ksdlfAP74U28EsaD3gHtLAqHGZGf_hgps4MgrDfQ49Q908O9PwxUoRO2OBL23YAfTeczdFlYHP_AhfJ3uI8qGHVkP21lDwBhRWps-IOxX5ln7apUhkpLiMUZ7wvlBOqO2skQ5OQihomP04wSrMd8XnSgr0OsJltwT-fSWkUOgDpJLJw7CPhrpM52CeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1FekU7ZemZvMYMDKZBICZZqA1A0QQXgpVxpP9TgDa5BKlAhdPSdj0iV6bBV2S0j3OBAzi8d5_WCbDiLeTrNLmdCxytA8FO_EjV8McLPGY-bTqpTmHuRhcXVruWK2JszZ7CNXg7ZqIgX4n4kM10iob0otrlSAEem5Q66CAKkLQV78z0RvdJi2j6itFryTJfLkXPzmelzuob9grTRU656S8CkpjrOh9ccC5AzAe73mB-u4crL9VZ1JGNlKrIxftAlD27MEqltayjxkjbMlq6mqja_ZMcCw9ZsIV4joj3YWaGjM_9ykSSRnXl0cYN-oQYMD7ni0jyiTsPGpEf6LVM_ngFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1FekU7ZemZvMYMDKZBICZZqA1A0QQXgpVxpP9TgDa5BKlAhdPSdj0iV6bBV2S0j3OBAzi8d5_WCbDiLeTrNLmdCxytA8FO_EjV8McLPGY-bTqpTmHuRhcXVruWK2JszZ7CNXg7ZqIgX4n4kM10iob0otrlSAEem5Q66CAKkLQV78z0RvdJi2j6itFryTJfLkXPzmelzuob9grTRU656S8CkpjrOh9ccC5AzAe73mB-u4crL9VZ1JGNlKrIxftAlD27MEqltayjxkjbMlq6mqja_ZMcCw9ZsIV4joj3YWaGjM_9ykSSRnXl0cYN-oQYMD7ni0jyiTsPGpEf6LVM_ngFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=PMurR7nYl_L_KiycYY71rAD5CjdsVgXtSNswpdANlzGSJxsoXgf_AeDUBTOVSRV19l4hEJLET-5TYcnw3qzVYHA8OTC4eku8QfyT9H1l32vEeONL64etL3TrDbPVgqxw8_T8G6eRPewIkncCleKrrDpKqwaXo7Xs-wgJj4yHvjTviIjD4Vcfsf3T1yXZOZi8VcXF9_XzmaUz4z_bbDoKQhWymnAEjcSg57xKUMs4an91rYaYiRGRhDKGhwXetMz8c7JU_lauyFnG6sCKxWeZoS9i-Vj0RJSEGB1mEHqc8abC6JLdAceFHylcdJh4dBLOKbfQO7tRUjba2vkjyfOdxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=PMurR7nYl_L_KiycYY71rAD5CjdsVgXtSNswpdANlzGSJxsoXgf_AeDUBTOVSRV19l4hEJLET-5TYcnw3qzVYHA8OTC4eku8QfyT9H1l32vEeONL64etL3TrDbPVgqxw8_T8G6eRPewIkncCleKrrDpKqwaXo7Xs-wgJj4yHvjTviIjD4Vcfsf3T1yXZOZi8VcXF9_XzmaUz4z_bbDoKQhWymnAEjcSg57xKUMs4an91rYaYiRGRhDKGhwXetMz8c7JU_lauyFnG6sCKxWeZoS9i-Vj0RJSEGB1mEHqc8abC6JLdAceFHylcdJh4dBLOKbfQO7tRUjba2vkjyfOdxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=q6iB-0yl5REJFVaBHhqymLDDftDAIROpt6R09fBobmTDNYDNpsezFt7GV1lYKfw3daX3qPl-LPKKakKrwxeDzW13iUTVLkmwzwgCeA7ffUpDO8oEzCmydpFtAyZ1-bRqgJhWNpS3dKyO5qBmr83lCdVH0YSdhDvKGcXnin2Njtm99BLGX79WX64NGIo2IH_x3ZIV5aEVHXB5qRrBwGL6LxIHqQ3CPsLp6umEqOm8CQT_q-_5Hi7NpPTL27-QHbqlrmnThvJTUD7TuU7iEByxXece3L5EDOoqYvORPKwwNTb_1ZCoKdyiR2j4yp-PXM2UR4lKnrg45Ekd14dbCJGByw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=q6iB-0yl5REJFVaBHhqymLDDftDAIROpt6R09fBobmTDNYDNpsezFt7GV1lYKfw3daX3qPl-LPKKakKrwxeDzW13iUTVLkmwzwgCeA7ffUpDO8oEzCmydpFtAyZ1-bRqgJhWNpS3dKyO5qBmr83lCdVH0YSdhDvKGcXnin2Njtm99BLGX79WX64NGIo2IH_x3ZIV5aEVHXB5qRrBwGL6LxIHqQ3CPsLp6umEqOm8CQT_q-_5Hi7NpPTL27-QHbqlrmnThvJTUD7TuU7iEByxXece3L5EDOoqYvORPKwwNTb_1ZCoKdyiR2j4yp-PXM2UR4lKnrg45Ekd14dbCJGByw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3-SH2z3n1zNk_1V4AFaoZP7r1vplH8-I2kAw8Th_7_lRf3QCpVqVFJdB2Yw4geeEDZV7iWcsrX1Az8Lv_sfoD3QfRbJBoMEBKyGc-Bg0KVZ5ZG53E3W62rzFFGWLxzgsTT389_k1yH3rdQhlzGJScE0PltBMyXgnmqXgtfUZDINwfvmEHzDC6vHdhXeycvaNLv4OiwjhfwjiRjefOFyiH19K4fYnhEWoneqGJg03v11J2et0-PeIdmeptxJLSeXqnx-vhOuFlR1xg-2EGuLZR5Wu6aE0Wd4QmNpeZfIdN5LrcJavLcR5IiyaX84V_UWRu4IAz18uKtEWcBhuaFJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=CaemG9vFKGou2nCseOgxL90yd_jAlRNkPYBxs53o1QqVwmWuH8U8Joed1u_WL9YrgqxtsBsS3Nn3ypNIaagRyq9mdjyaJ4lZjO4SPrL8Ne427G55rLdkMgGQmpLdDVAPQZviN9kvvEpz97H3bHSikC57s82v2fFbwgpEwzDKfRZPqDQhMHedRjN4MIEuJ5foG3qc7VyflLaqT9ssgwIHNTR1XR1oeUJM3CidMIjrcZM7EQc4a2UVK_PR8RvkzLd4sgLv8Vd4_NWxnEIooaEKuFfsOcyE_sbGbYwJEQ2To5KwUFOS4nUJHfRy-TCT2-yKq7yNo9FZMj-LRfojsI0ZRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=CaemG9vFKGou2nCseOgxL90yd_jAlRNkPYBxs53o1QqVwmWuH8U8Joed1u_WL9YrgqxtsBsS3Nn3ypNIaagRyq9mdjyaJ4lZjO4SPrL8Ne427G55rLdkMgGQmpLdDVAPQZviN9kvvEpz97H3bHSikC57s82v2fFbwgpEwzDKfRZPqDQhMHedRjN4MIEuJ5foG3qc7VyflLaqT9ssgwIHNTR1XR1oeUJM3CidMIjrcZM7EQc4a2UVK_PR8RvkzLd4sgLv8Vd4_NWxnEIooaEKuFfsOcyE_sbGbYwJEQ2To5KwUFOS4nUJHfRy-TCT2-yKq7yNo9FZMj-LRfojsI0ZRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BByDQjrI54MCxJMtGEtOlidWYTt2mrrnYXvB6AhxENiEgSIVZxjrXayCr2XroUFix9H-p2s4bm6MPsF02jQgPylVMBAPj0fhtqcPytA17-cdRQ8mz459KSY_hALfmUYfiHIl2X6ZfLD62uE4EZ3OrsJX0zTeDINf1Aw0LFIGJ_l1IPn2gX2IGQHmBKgnpXA-v6p88m-ZJjY9GavRs88GU_P1ySHs5YCbDSlIEK9a8ANuJN1lX-PVWJc7to7i1DD6OBK8PdQHXFDBZKC-uNC1Z57y_gMSoy__jgZ9YsY30hecbTLtScibuuPswShEj_hHnt2XgbCLUHFdVTvv889kIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4vhqnEFEzPpsnrF8G6Mki29NiqZjvGMJwuIAvt4CKlZxepPyT7fSSrGHb0DN1xUCcytz7FYOQWxFIBqEZoKaHiHpqKl-pBLb16ImHsHfxtFDzWQzf3kXOFlRUqY6BkiVCsgHne2IVywiqDn893NPMS9f0n0CDkT2-b5sHTINTl43n1M1n6F4vykDa4_okXKpQhFqlCoRUfGMyYsCjvOe6Fkj2VH2cExxe-Z8zC5Ee1ixC6QGLafJUHtgQ0NbRucbhtoGDnfD8F0Ki2JkeCV6JM3sW7v2vV5GzD4JH4PJDVIJJOge1QFtY5snDGM8BIb-cfqf2hfbMG0JXPpZWMlLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oN1sOsCZER9OnUAp3r0tFdXC9EN3isKyKOPRBfF_vNJKBPaMC0MxOjjeJ__0DImQUHhLSLrBT8d_Bhdt23WfxHTRBrIHuQ4lxrgCSFqlVT-1h09ffisXWmd17uvnwe5-FBnR77diryJxUp9lWbQp1AplkQmMJBqkrkdbJmGJLs24ipXXrityXfazL7pUxwpr5AoPAF9F2mnUcHf9ZSirGk1uSMTKwCaeKrx_mZmMUOrWB3rCjh-a3whR5e1AOAq4lwFY_TLZZ5yKgjvBo7d0QVlZP9eg0S0Z31yyzcsq4-dTf7BJlgzF0-0PaFUEAvnuEp7Q66tA3rL8wUTBaN-1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wkw8yTKEX23CGXCMT5KMfacyOmTM3k1sxOKs0fGAuc72yP-3AfnS5hncLDX98PYkIOgTtKkQiknM2Fxch92UO0NSb0CJVW9DCHu_ejE1x6K3Pz96MJ93QQukEgdaKeeZpw6FVywd9AVN7iWwn0Q7wN7lpdTF6RL2TnvpKjIo4YHsi_VSEtd7BsxAniQJkwVqpkCCbRPSfor-lTNJdeyxWspcS5SUa0zRrUQJgqQCL_wzW9RdisO1FeU4ok2IOvVlN2jDvMFEkoEzR9JciomqWsgGJdjJYcd_ms4RTGuPCZYrdfCU1Z_cyqOQNFKausCNgtTImBumspHKLkEGOe9dLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hIOb8Oe1VNxdRQaFIVksHevuAZ54jmQGJYyjNVYDdMN_Hvfim-qtCDgIjKpEHTMC3VR7bDPckwSVe0oXGIdEEStYjjZ4rVx9dSeO-vfgex-e2l5xy-B6h9KFzGQCOCOCrek9R6LoYs-EqxQGi9JRalLoa4hEiwZreT3p-_xxXfArEIZsAhVb9qFCjJLmrhh3eH-xnmdGaXJlEXEVeVkjIBE4eKCPYf8G-Fr8eLLTkzGWXZiIWk_V5-hq_Q6VeYattuEkIAMq76dQGOuSxe0BlmhTSxujsj_HAZ2Fnt9AG8V60hiSDOxkeMMRzAuOo805Ap8cfGdBB_0yqvs1sWkaSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgNilpCgLOJGUXasjXaQfaJZqS9J44qE06pd4-Lwqi5yeptZrYiWWMuzRihtix1BUcxj19H5FB5odr9RbwK7mUKVvFl9ogLSHQVEgorfV2QRrJwVIy3_Urxr_HbxmS76Je8v-qKfxQ36hbfWdB8ljm0R0wA7siPinNkPqct2X5r7BSPz7pnNHVC7j6yKUhTIZ5caT5SjrMlZVEJNVSeCGLp3KjtRAJ4ektByWvpQD4t9WI5XGmsAkgvbpX5fGd2ZqPNvyCHsvDYRa1dOdZjk8lIv0NjuHoTi_w7Yju_ta7A4T5U1us-JoGQngkAswCQCS15mOCNGYE7-n_nZPqobxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=ltQLfKZpIVLwXA2d6G5hcAwvIm6UHgn2fVmHJu5X3vv0eX0t8l1EnstR9KdP6FSMOS1lhj7p-P_i-KVmIyIvs5KXc1mnWr6vrKLEEt6EVzelJ_owgCDQd-jns_zxUdw5M_Beoz1kcP-r690xN4FJcd42QA3CTY6fOlnViefGI0lyjP-qW0gdbCciX2uTNQ1a6bKIy1OjCQHInfBwn4Y_vawphc5rKafv4AeJ9TwY9QUKJNrjm1AXW83jzO3gXrsVhgoogqKzq8fIXyXylhRSsEdgQOyG2MlJWNrNh_M4vhZpER_6q0eGH1-H83pYQiYxuUw2d6MNrpoxGHLf916NRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=ltQLfKZpIVLwXA2d6G5hcAwvIm6UHgn2fVmHJu5X3vv0eX0t8l1EnstR9KdP6FSMOS1lhj7p-P_i-KVmIyIvs5KXc1mnWr6vrKLEEt6EVzelJ_owgCDQd-jns_zxUdw5M_Beoz1kcP-r690xN4FJcd42QA3CTY6fOlnViefGI0lyjP-qW0gdbCciX2uTNQ1a6bKIy1OjCQHInfBwn4Y_vawphc5rKafv4AeJ9TwY9QUKJNrjm1AXW83jzO3gXrsVhgoogqKzq8fIXyXylhRSsEdgQOyG2MlJWNrNh_M4vhZpER_6q0eGH1-H83pYQiYxuUw2d6MNrpoxGHLf916NRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=nNRHbuE7fRQK8ULVYLqz7KZ58rUfLLjAiB0HwmDbEa-ilAYu5c5qXOJQf2bdujduNMRQxbFFSaKnNoy0Wo3lXg145q_duFdbAVjnfZ5Sw302Daoa8VSF8N1aphpft-BKURXITdXupg9IvBKnsT5cnF7P7H2tsCZWAZ4rgwo8aCtjrTHrEg9EBrJ5vkDCAgNZsqCzUpKAVwKHobfDxJfZub9DWJovoRWIWwqSl6_1oLtShzFhFgjhXblvgHVWCCmogKU35IdprIZmZga6-Fup7fb3k5AL3jzgOqSm0wN6I4cIMumckzqWk6zg1x9ubyijBc-T1Q-TdXRlBTDFvnGkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=nNRHbuE7fRQK8ULVYLqz7KZ58rUfLLjAiB0HwmDbEa-ilAYu5c5qXOJQf2bdujduNMRQxbFFSaKnNoy0Wo3lXg145q_duFdbAVjnfZ5Sw302Daoa8VSF8N1aphpft-BKURXITdXupg9IvBKnsT5cnF7P7H2tsCZWAZ4rgwo8aCtjrTHrEg9EBrJ5vkDCAgNZsqCzUpKAVwKHobfDxJfZub9DWJovoRWIWwqSl6_1oLtShzFhFgjhXblvgHVWCCmogKU35IdprIZmZga6-Fup7fb3k5AL3jzgOqSm0wN6I4cIMumckzqWk6zg1x9ubyijBc-T1Q-TdXRlBTDFvnGkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRHVRDNJDPYvR_YnNu3WSUbRA-oYZ8Z8h-glrhAXXFcKJrnEpi2MD5x1vGhoPQ8rPdcmBCwTRXEaZZfxy2bmKX9rt0aUtG0uPZI7a6wojh2kkMbO-iiuudPbPGZy-HvRrcS-xPy0Wsu_3XTziUH5gJ-Ebst-pfAHv3-FjRmjsnNHVO5rMDmqQKurVds_Yc0ydhEZUb6BTXoGHc2biGDK1pUs8LTrnvoAHaUvziSbNii3GiuO4eL3OlHuFFgie4y9n_bcm1CrnXqz_G3lQntvhowS6FeWJZYShvxLJct4gH_Hso9w47I7gW_qzhx3yNZwDDaoddjqOMTODe2IlbcE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=UZvMBgpbPdBefNjFDTk_V5f5a4duQDgsMdqozKBxuJuz0HOa8y_ZA--h7xihxoWvwrvkLKrAtyDpXNKi-O5HPbip-JArDagAQPqD9N1jCgiI7GoVkyA1SDQN5JwCtYIEhqf9_XxP-khjej13_t8fhaB-wfE9aC0ocLwJWVeBgGhIzrjBTPNit64KGbzUIrSWiNahYJb7vhns-UJcdfitHwbKA2EzoYIjFdhat2GeWQCWRpkcYw2v8rsm0x3t5t07XjyBoKO2iQxxCxSIPq5hyPuyll4aviwZLeveJVTVpl4CQqvD04YKw8wpuM2Eb9SBbRsymgzwhytx-xT0XKxIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=F7JuiyhC3q4Gwk-5SgAsfk0k_PYa2ixWiZ5q8dSL5v81afugutt41RmxS747giaDLjKFUEpUNmbDYNU2-c45KdbYIeSW5DjTtN4T6sLvLAyfJz4zV_qDO-agbwcxMhggM1nAODq1xiM4vp1C5yqv0HyV1LBWEL-2ZrH4dtSaN2gJSx3ptpArlFFhZG083eWda-byzMLZKNT5vWVX81RFyaYXEph1rA--Ld1PUAx56bk0k1bqoruhz6a-nvw3EWJZ6ZWaUClWCNXAQNKuouERpB7UPQxLob0vv3JzqMu97sEBc7O33-Tl4519fVZUTaQ5Af-H673HLNGXPKY2OWJUBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=F7JuiyhC3q4Gwk-5SgAsfk0k_PYa2ixWiZ5q8dSL5v81afugutt41RmxS747giaDLjKFUEpUNmbDYNU2-c45KdbYIeSW5DjTtN4T6sLvLAyfJz4zV_qDO-agbwcxMhggM1nAODq1xiM4vp1C5yqv0HyV1LBWEL-2ZrH4dtSaN2gJSx3ptpArlFFhZG083eWda-byzMLZKNT5vWVX81RFyaYXEph1rA--Ld1PUAx56bk0k1bqoruhz6a-nvw3EWJZ6ZWaUClWCNXAQNKuouERpB7UPQxLob0vv3JzqMu97sEBc7O33-Tl4519fVZUTaQ5Af-H673HLNGXPKY2OWJUBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7PgVNswqTD7mlDW5khQtTPeKH2xY4M1Ll6xHr82ubhMnkZb9IJfD-x6fWmkcMZS9doFxqieR90X56mbR5KcNSuaUmxLIFzZbj_q0XrR58vxXNkmlNJ_CsyKZBSbsf58mxqUZktZ6HcFtFUIo0MwqTAwE5Oz4ne67xB7sE03GkIpjf0J8OLfTgCJDwzX-pqmv2yXYtWWiHU6FO6hqeEhnkyexEuX5SdVnieTqojrXwSg-gfsmH5S5C3At64BWCMe_sNg0ImJX5SKe-3rjUDxHC6ofvMLEPZSrBMmoxYne9iZOYM5bn4n2zecNLZqlTYaL2y4noKqqEjW5YqK6h3SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsubXNPVtDKG8tH5GfUwDPk8PePr7MHf5QP4FRzFuu9zuvUm2wTngn_dUo9Bp31YkOZufM96ggAPSC5r8lgVdEsxUXIz5gy7dtZT6CzzfO74lkYrAPjR6JtnqkzByQnaf7MVQWFbtbxPD3pAJa9TmG2QfgSirF5ISZl4tOTl1nYfnz-I4ONeJYtGOzcrlxaDlOkM4kMGPL1KWoBRPL4Vgoindn764-InkqHnSI6l3bpHu-cQIIZug2jZqkM8lASnhiWUIl5J_vfRe7217w-6X3yqfnVBKG6ewafiTwm8HRcoYKWvsYPvV-z5q7Zs9uCZ3QIQilIwtiS-yAX7YOtM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeEHR9qzZJrzppRwKM4aqkC0k3_C2v6uw9Q-egnWVSTOhDDoeR3qhXTBnjGWXEasfrTyxgVNZvy5cIbt3iWa7-bykqf3WYVDhfffSoGXgpa-yfmYkew8ojwRcOvvnL2czzl_kvZGuQHlSakKddN-V4wiGVUwPfaev32zkYTHpZM87bhagk3qt2BzenP8xYaP-zS1bKI9TpV4wczXvGRi-9ltYeXUhjEZoMRfdnBk08dBN9rUo-LO-CjyB2WFh0o7dA1GTqPd6HhFS_CeDreS7SsEijExqe-Xl1dHgDKSiBgfY_Z_0Gl6bwqTgmxpLG4sJRA_KXbj4XIaaVCWyM0y9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nElrKoE_tpQ-PqLsSkiufpbJDQ1P1vKb3b_-jBtCzKQHjVJUffY2ztkcYBNuYkY0dg7nc3KyBfF-Aupk-TWm_9p0lQQn1-Ppv7UZiUetztvxRyTBEtxub0wLIDbe-9sRv9zNaIic4H6G3GCD6v_emRvuAAugTDPOxqP6SagiOVFHCYnEDOYc4I3_hMVg8cLMLQ2SR6b8lXTGrQZ5KcY72oZ8wr6-EfKou9axsOd8WHT9ff9UneaVfy2yR1CxAzRMhLgUlWhYDsRkzT9If8ejqGMTDIvQPdbliNgzggR65Emwmfo-7QWUsdfAItwMnjv-l7G-e_Kratxhg8gtdzDnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnoZ7seP71U-eQIwXsQI2wSJ_a88-Q7Go6EOMYOfz-uRaevkA55qT6y3tkZuWWdW1PxERi0PRMypFM_1TO-tEP4akTiR8XY3nK3xODNmFVJ7OIpwA_V72ybL7vAHSfMHAcQgON3fwXGVoR-eG7rXd0ncfi5xTJ5eavQooYrQz5zRiDVu0ngIAvx9WgTT3-saZKd_g5wkw1r0utOG4SdpkQdBU2lp-3MHLmKRiwZk3bojde5CTlm3NImoV8QOmLvH46So2lSA1pLfU2ej3hLSKmBN2Yf9s61iaeyaD096bM1QRv4zE-6Oqj_dAsIp3F5NxVExVHyBAOsIsqNxdYaR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=lLqgbQEvbFTzyrzX29NC2VrPQGR9dmrm-pb1y3-qw8Y1_kFU756ZGOEmX2pv2B_f-jKNf9Uu6p_XEVVhvctcPFQMs5PTLEaAoY472dlvkDy_gZyThzSpe-TbyJsrzeisA0VMST0aZrbha1NDrW3elh6fmMKMje589m_a-NfhgXWDc-f_ud28fPm7V2zC22fAtnCkD5gVDLuNu2g1CSa_rCsNBFilrV4o_GfuHZmm2XstbPQr96RskEaPxKuttCVlZbcMNg-uivavn8xysto5YCnlN8vG_xyOuRhLDvtlM2d7-au3XsjfpkGOz4RDq5GyxTpPn6z_y4BQflvq4Wx8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=lLqgbQEvbFTzyrzX29NC2VrPQGR9dmrm-pb1y3-qw8Y1_kFU756ZGOEmX2pv2B_f-jKNf9Uu6p_XEVVhvctcPFQMs5PTLEaAoY472dlvkDy_gZyThzSpe-TbyJsrzeisA0VMST0aZrbha1NDrW3elh6fmMKMje589m_a-NfhgXWDc-f_ud28fPm7V2zC22fAtnCkD5gVDLuNu2g1CSa_rCsNBFilrV4o_GfuHZmm2XstbPQr96RskEaPxKuttCVlZbcMNg-uivavn8xysto5YCnlN8vG_xyOuRhLDvtlM2d7-au3XsjfpkGOz4RDq5GyxTpPn6z_y4BQflvq4Wx8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=jRYpYiNHliUPFFVf8DGMV8MFQ_8S08h_2e2dWaijM-z45hYVUj74eb_GLt8MBCOGk0cmWDnJna84nylQ81TI1ud7Z6cXR56KQw-fLUYS4gMNmTu7cbqycUt-evCmYu-orhCMWfFqLPARew85_P8a5kKy9FZR9rJMV9A-3SWhu0ojieolSd0HwINvWerKCFuFMYcVquBA649vw5h6ko5rAfa7hBynEmtxPQLUYYZ1I4dHzYsom30z5ktifvPBT2KH_lqaw0SVSoY9oJy1r0z8dAnxOyd3TEntAeL-gpfyDG89-2wQ30hdfn_ZIMeC0_TrwJdnfRe0TI3n3tgg-Gfqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=jRYpYiNHliUPFFVf8DGMV8MFQ_8S08h_2e2dWaijM-z45hYVUj74eb_GLt8MBCOGk0cmWDnJna84nylQ81TI1ud7Z6cXR56KQw-fLUYS4gMNmTu7cbqycUt-evCmYu-orhCMWfFqLPARew85_P8a5kKy9FZR9rJMV9A-3SWhu0ojieolSd0HwINvWerKCFuFMYcVquBA649vw5h6ko5rAfa7hBynEmtxPQLUYYZ1I4dHzYsom30z5ktifvPBT2KH_lqaw0SVSoY9oJy1r0z8dAnxOyd3TEntAeL-gpfyDG89-2wQ30hdfn_ZIMeC0_TrwJdnfRe0TI3n3tgg-Gfqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=HlSbmd3v333dmMPhb5yHhqlwgdI66MBi387JiuhseIMdHBAWd_yO4uprKCSXSoQwy2tuWwmdQsQBbElMqvPXvdoJWduxqkVsYrbmkYAqY4cCCWfYVb9xGcq5C3-cCu--udFNHx0q6iwPx0KmUegi7YuO7r-bYJ0nTEaFmAOK8JhLaYQQJHJ4j4g_4S0GFItZ-1wUFXYtKyOTb2PqDld5zXWu6vUD0W3jKlwuXVceG8pYeBALD6s5OKRdXLgH619kTEbR6OWclzcGYCfIzNbLx8L-QtExRvA4PbROMil2y2x5bFV3O3SEtydgrxaCYJBFThSibVs66UZtQ1BTY1jnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=HlSbmd3v333dmMPhb5yHhqlwgdI66MBi387JiuhseIMdHBAWd_yO4uprKCSXSoQwy2tuWwmdQsQBbElMqvPXvdoJWduxqkVsYrbmkYAqY4cCCWfYVb9xGcq5C3-cCu--udFNHx0q6iwPx0KmUegi7YuO7r-bYJ0nTEaFmAOK8JhLaYQQJHJ4j4g_4S0GFItZ-1wUFXYtKyOTb2PqDld5zXWu6vUD0W3jKlwuXVceG8pYeBALD6s5OKRdXLgH619kTEbR6OWclzcGYCfIzNbLx8L-QtExRvA4PbROMil2y2x5bFV3O3SEtydgrxaCYJBFThSibVs66UZtQ1BTY1jnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=AdfFvRje-IGjykvjkzJ-2NpagqVTFSdB1D-l6FPIKM0hem_QYncrd_3qP0AEAXEK06NlJqA66cqBjK_fRKBhgG3gQ65QG6FKBlSZ1aeg9ccDaFHM3bOl121wr6MpqL8fdmR4RioqIrAJD7msn60X-t-ljHndm3sLuKqH4VNb5YDk3OWL7cZwLFDVCjYh_-JPETqF3gJbXgtofqPxCotexkF8UzOH4i1P5OqQR-JUOJSDy3y9urjwpTO6xyb9AxHa-FOYec27XSQIz4iqAyVO2gr4XsXifP43WZuI6SzBYFmRaSMP6fodjTsneSVIYQ0BHhHFZejBJ5sXTROaegGEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=AdfFvRje-IGjykvjkzJ-2NpagqVTFSdB1D-l6FPIKM0hem_QYncrd_3qP0AEAXEK06NlJqA66cqBjK_fRKBhgG3gQ65QG6FKBlSZ1aeg9ccDaFHM3bOl121wr6MpqL8fdmR4RioqIrAJD7msn60X-t-ljHndm3sLuKqH4VNb5YDk3OWL7cZwLFDVCjYh_-JPETqF3gJbXgtofqPxCotexkF8UzOH4i1P5OqQR-JUOJSDy3y9urjwpTO6xyb9AxHa-FOYec27XSQIz4iqAyVO2gr4XsXifP43WZuI6SzBYFmRaSMP6fodjTsneSVIYQ0BHhHFZejBJ5sXTROaegGEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=fvmVjm62gStXmwCRm-mR-NThhcCvmdRBDoa3RrbieZpH8DYENk7iDkBdW-nFGM86hPiN0TOdk04zlKf-FnpE1uaDd6D8u9pwhceqh43VYj42IIBl9Q2bPHLAc2tQYIJMHPmbD7SHbbvPGSQ8db_Frq3ftACp8Ip9D3IREBd4SA572eADm4egctphPTrapIflmgJguEhw3lGnp_UOGE1_AigkjtmOOdqOjk7rjHPbiXY_w1CBXlegwCx9A0pM7o4Zp8vAb9Pb1Ab_zgR6oDedbJtB7lmjAU37SzRzUeeZvKqqc-1VDUEIWnkepqcVgdd1vWWIk9WTiq-8EGzBL0zjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=fvmVjm62gStXmwCRm-mR-NThhcCvmdRBDoa3RrbieZpH8DYENk7iDkBdW-nFGM86hPiN0TOdk04zlKf-FnpE1uaDd6D8u9pwhceqh43VYj42IIBl9Q2bPHLAc2tQYIJMHPmbD7SHbbvPGSQ8db_Frq3ftACp8Ip9D3IREBd4SA572eADm4egctphPTrapIflmgJguEhw3lGnp_UOGE1_AigkjtmOOdqOjk7rjHPbiXY_w1CBXlegwCx9A0pM7o4Zp8vAb9Pb1Ab_zgR6oDedbJtB7lmjAU37SzRzUeeZvKqqc-1VDUEIWnkepqcVgdd1vWWIk9WTiq-8EGzBL0zjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_myzak1SBPDpwyTqRJK2PX1N2oVdLOVAZo2XZc4L7A_GZgCMqUZV3sj0U1wRllCZZQGRmIcvkgmmlBcckwryTh9MSaYM6YZcjGcw2crOjBjd9qT89kdxYvfBjHSNodd5zJKEuD_P8dLEojYSRoWgFVxmKAKESvbaVaeLdWz_alpJM-AMugf5_PLHOG-XrEorxqM1GX08mrOMIj_TCj-MFtG9bOybmdMSYlF6azZMq7d2EPLeGa9mgDkjwQH2SpOAEm8agdeoqoNxkfFh-wOuePrhDe4Qd7b1Dvp9NxfYBGbwbjts73QgyRF4sGUSYKmYiqU1riP_g8V3OLDGnS22M4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_myzak1SBPDpwyTqRJK2PX1N2oVdLOVAZo2XZc4L7A_GZgCMqUZV3sj0U1wRllCZZQGRmIcvkgmmlBcckwryTh9MSaYM6YZcjGcw2crOjBjd9qT89kdxYvfBjHSNodd5zJKEuD_P8dLEojYSRoWgFVxmKAKESvbaVaeLdWz_alpJM-AMugf5_PLHOG-XrEorxqM1GX08mrOMIj_TCj-MFtG9bOybmdMSYlF6azZMq7d2EPLeGa9mgDkjwQH2SpOAEm8agdeoqoNxkfFh-wOuePrhDe4Qd7b1Dvp9NxfYBGbwbjts73QgyRF4sGUSYKmYiqU1riP_g8V3OLDGnS22M4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=XKcTuAjdWHK7Gni3hFdEdr3fbsPdyg66MBNHn1I02_vp_amBsDc1y7EseLQDNkASmxxATKz-Twmh_qOZGcLjaRJZ2p24MGTN3jnqQG7rPaaYkk-lpxa50o55R--WtChNGYWDi98eQQ5xXNyAFiwMMtfMgbn_xgiNRA8Eyc-3RvotKTIIFy6ud07878MHNqWjR_d-_n9tWh0LyCJwSdj0lZwrYhGGl8-i5KkMChkiVaY2y_JcJuznYGcG-GoGldTaW37-GfpVBMsuClsobs4Rlw7JKdPKjcHkfJzKXcKCluH2TknxC9LkNLdgL5cKo-DAIVFI0v88qJjnwWlf0jrMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=XKcTuAjdWHK7Gni3hFdEdr3fbsPdyg66MBNHn1I02_vp_amBsDc1y7EseLQDNkASmxxATKz-Twmh_qOZGcLjaRJZ2p24MGTN3jnqQG7rPaaYkk-lpxa50o55R--WtChNGYWDi98eQQ5xXNyAFiwMMtfMgbn_xgiNRA8Eyc-3RvotKTIIFy6ud07878MHNqWjR_d-_n9tWh0LyCJwSdj0lZwrYhGGl8-i5KkMChkiVaY2y_JcJuznYGcG-GoGldTaW37-GfpVBMsuClsobs4Rlw7JKdPKjcHkfJzKXcKCluH2TknxC9LkNLdgL5cKo-DAIVFI0v88qJjnwWlf0jrMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH5v_AQcPuudytD6uaiscTFkrDoaupO7ENg3XqqBTOpbqjTyFJZrAvDnc6zoLztDyv7CXz2oHbinu8GPTk318qTBoWCP33J-nDWyjK00B9iw5IvEvM5i5nBOc9Sw5KlIqcHjNFta75v7qJiJELqLGo1DCVBAkvVucND3ls6nXmaIZt9ZPRtjAgrVscW1mxr0tu2nuiRr9Jz16SOCasZiIGl_dCBTM8gMel3QuBsqa9OK8RluQM_yY6adLmFvrzTc4Q1D5QhzGRi1WKTcgdOmDPZZewCDn_mbIVnB5EGKg4uxgIzndOlVbUtnS30fUexGZh75KmQkreU67wkRY3ID7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8QalDQgIKVYQSryLVDOYC2B2jvGy9Xq4-rK_8exr_3rWJgAgqv1sCnaRsbs6zsa0yfHm2MQ6M5i9kMCzkHRDCdJ0aVro_TdYsqdGMPhQ7DPWS-MEH6jXj355K8mN--A93UOncDfqq7TXHfhUf-ncyQCo0XA5hT162zeEXvg2vKW85zawRcyNS8C73k13VtoLGlv0hh5DqfRAa_AS4VU0oirshGVDrEh13yX7IbFMaZgIfSUM1HdqSQzIhuEqHW5EMwoZ8Le6SYG1KtY9qXeBP5EXdBQ_bDfAXSSMUJGFXTWgPE4wBoF6edDIRRawzDcnnnWtWF8grLvGGbBBFeXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=HfpNLqEHwCglal_bo-dHo45sbOTjWawdRd9BzEjqxK1KtmY05nkQeialosoptF_nuvc3Hjtb0wS2sMbgIoF2w2Y-KuVNKZUyXx9CIJ3uBuLoqka5fhw8VWTQJvBAyZBZ61iyZab5MDbVHqZVEjkydh7VvyNZ_Co4IE_D9T6q4oh3SPEYA0OikBSvel-0dtm-kSOzw4jsYcYvEjwFzv6e6JmbqppWVQWwOkzXfAOf-rLuHBjtRR6VYv860VmEzPRbrDp5NsgkFuuL-gftWn1px5vFQJtfabE4ju2mwJn9kSjsQP493MQqD9GY0ScGgT5ALgCIoVTtBcuokLY-6xXKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=HfpNLqEHwCglal_bo-dHo45sbOTjWawdRd9BzEjqxK1KtmY05nkQeialosoptF_nuvc3Hjtb0wS2sMbgIoF2w2Y-KuVNKZUyXx9CIJ3uBuLoqka5fhw8VWTQJvBAyZBZ61iyZab5MDbVHqZVEjkydh7VvyNZ_Co4IE_D9T6q4oh3SPEYA0OikBSvel-0dtm-kSOzw4jsYcYvEjwFzv6e6JmbqppWVQWwOkzXfAOf-rLuHBjtRR6VYv860VmEzPRbrDp5NsgkFuuL-gftWn1px5vFQJtfabE4ju2mwJn9kSjsQP493MQqD9GY0ScGgT5ALgCIoVTtBcuokLY-6xXKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IspNS1fLRUPYVdSYWhXZRN7mHoYThERzvda_WLUPT6oYYXjpeEDgohR34OfxRySq0fv3LAUZMbU80HQrGpC4S8uw_lsUBtFgXwbcpiZiHH70_GZdp0leKKFxx8TJyl1TVkR3SvO8QuFLYUETgi2xOXr6xllZlbycSTufS4wLco0V9WGG9kxXI9UVXgqR1C8j-DN1npxvtNFbJBvkFwouNaiagKJMkKFTzYxbWsNAwW2fagueYsVeHtZVRcSXagcaHSRY2lW9b6s9dLX-Uyk0ylbXTRVy_2vwTCDPo6_zBUMbeeiFDx6jFnvmSk3ZPeSfNurykdsI1SRC2iMNOhw6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=NOdGvtCXpY2RCW0KYSO1_cJSK4VIlNUu4eH4-YA0iWjbleVZkyX4dzf-EPO1z0vlxSUOPXg-oGwT-5LUYgh1cO-ETKjZ_0on5DeWszdmS6yKcNSdcH4bth0MCNvtYhp_DCbBOOE8T1m3zgIVjuAJ45Zf07s_KoIPPJxvBFB3w4GxPtQANDg5CoPgvZSrziDgjG3buGEiQrJsWHe74liFXGOkTGvavSO3rpjBync3kqMkQcPf03l56ws8QWHzn-4jnJnpl7eB46TUHs9z46-JBJnmvITqrXkdo4ixAIVXJM5eA8fx17V01zNJggPycRo9jmrwlfjVDqbSUu8LJPvr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=NOdGvtCXpY2RCW0KYSO1_cJSK4VIlNUu4eH4-YA0iWjbleVZkyX4dzf-EPO1z0vlxSUOPXg-oGwT-5LUYgh1cO-ETKjZ_0on5DeWszdmS6yKcNSdcH4bth0MCNvtYhp_DCbBOOE8T1m3zgIVjuAJ45Zf07s_KoIPPJxvBFB3w4GxPtQANDg5CoPgvZSrziDgjG3buGEiQrJsWHe74liFXGOkTGvavSO3rpjBync3kqMkQcPf03l56ws8QWHzn-4jnJnpl7eB46TUHs9z46-JBJnmvITqrXkdo4ixAIVXJM5eA8fx17V01zNJggPycRo9jmrwlfjVDqbSUu8LJPvr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=rggpR0hAL1D8RD13F57Kwu9ptCBgbqFgwpKYEKL2luFLToZi43CDD8UUmSMTp5b1RKBw8tuEhhWqUlBNpe4-E0W-VY5daSLrABhyNxftw77LU_wW-zp8yXp0JKNR0E-uXjG3ppfy9moX_n0EhxZErHAuGE2B7zw4BIJF-VsXv5OY6kwB4RIcADne0NfcFMVjw7Nl6RrXCJH2pIryFQTRwjW1C_6sqw4oWCC2u3MvVWvxYy9SZM4nQrCuDpeU6KzWp7H04Dd8IP59gnRUPlkMfG62FWEJQGqkkU2N2ubmlOODNb7bhyCTH3FHp0kvyYdfO7Z2p0SOkzRdqZezi9V_vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=rggpR0hAL1D8RD13F57Kwu9ptCBgbqFgwpKYEKL2luFLToZi43CDD8UUmSMTp5b1RKBw8tuEhhWqUlBNpe4-E0W-VY5daSLrABhyNxftw77LU_wW-zp8yXp0JKNR0E-uXjG3ppfy9moX_n0EhxZErHAuGE2B7zw4BIJF-VsXv5OY6kwB4RIcADne0NfcFMVjw7Nl6RrXCJH2pIryFQTRwjW1C_6sqw4oWCC2u3MvVWvxYy9SZM4nQrCuDpeU6KzWp7H04Dd8IP59gnRUPlkMfG62FWEJQGqkkU2N2ubmlOODNb7bhyCTH3FHp0kvyYdfO7Z2p0SOkzRdqZezi9V_vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkZfaB8Tk95IYjKmaAKj6GiOsc2-MWTZzAcvg2xkqeupwsl9BELBssvH_4DDncEGD3dQM-3wv7plWsJtakxS5O2aofXr9NGqFdLduoAvqchKEJRwTJYQYvSvckCsg4bG6d4uQiipwy2aQLniB2ck_bE1zV8XwZyiPdoI89G2_nNgO9i8lDjnKOPXVqOfo2p-2FmkSNeelzHknYRDMjgy40wZxcAMBUws2LCdeNqi0xs6spyl8OmQZiFQ3ifLnpHutRnQQkjARFRUepTpMlIPtt_hZpVhhmDvOVhauGDHxoBhzxwkVKWAsVALRK0DPVxLF6e6XdTXZppz-a2PqOTBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=i4QICn2vQlVhIWtziw5_HbctT6ixiIRX1yXwcst1i_Wm3Tp4k02_JsXpWSFLGxsN-tyT9A7XX9kzyTvduO1Y6NhsW8ozV7-0d7DyQeYsRHno0G03QndJ8OP4dO55tEJEDT5XjopXQzr-vpRbIzqllTyqq17gG3NKm6q3iu-9B9UH_J2dLSyzdym_-OLwHB7CL9fh7rjWHXs-ZI2laKTzSEm09d8go1evpKsxUV4lDED0QOOdBSnDf63YNJdcagr32zild6IQEyp-jy-X54lah0hoPqzZ-2sayWzVjiTx_QHiPM9pEK6iH1RfMPbfrmcI865uXy3OVA5OnpLfcTLi8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=i4QICn2vQlVhIWtziw5_HbctT6ixiIRX1yXwcst1i_Wm3Tp4k02_JsXpWSFLGxsN-tyT9A7XX9kzyTvduO1Y6NhsW8ozV7-0d7DyQeYsRHno0G03QndJ8OP4dO55tEJEDT5XjopXQzr-vpRbIzqllTyqq17gG3NKm6q3iu-9B9UH_J2dLSyzdym_-OLwHB7CL9fh7rjWHXs-ZI2laKTzSEm09d8go1evpKsxUV4lDED0QOOdBSnDf63YNJdcagr32zild6IQEyp-jy-X54lah0hoPqzZ-2sayWzVjiTx_QHiPM9pEK6iH1RfMPbfrmcI865uXy3OVA5OnpLfcTLi8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=Yu-vCoOhzRjP4qatODSgdDlKCm0iVb6LJ34YrpSmbFt1dc6KMM2LM2450pf3B_LSU2bcROKC4V9t60lz9lFll6D2sm8ggRJ2q7GqITfWYgIq17PoRVutJSaikY0jgZJ3f8mXTJI-gv9_eI5v5HU2IUyPruun9jDwL4UZxuhjz6gbgRdxsDRUtvCeGGMjv2pu2DV8nG-Vvk9LI-2yT2ZLY1lR-Inqk4hfsQv9Eepw0LBEjNMi2r4x4UKUblQ9JmDX4hNYqMgGkrY-xZT53QlTp-kGfOA56krWqKEr4PJFzfIpik1NhV0nd-b8-MCMOXHKndRrbuJVLXeyZD_g-Rl68g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=Yu-vCoOhzRjP4qatODSgdDlKCm0iVb6LJ34YrpSmbFt1dc6KMM2LM2450pf3B_LSU2bcROKC4V9t60lz9lFll6D2sm8ggRJ2q7GqITfWYgIq17PoRVutJSaikY0jgZJ3f8mXTJI-gv9_eI5v5HU2IUyPruun9jDwL4UZxuhjz6gbgRdxsDRUtvCeGGMjv2pu2DV8nG-Vvk9LI-2yT2ZLY1lR-Inqk4hfsQv9Eepw0LBEjNMi2r4x4UKUblQ9JmDX4hNYqMgGkrY-xZT53QlTp-kGfOA56krWqKEr4PJFzfIpik1NhV0nd-b8-MCMOXHKndRrbuJVLXeyZD_g-Rl68g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX9GnG32fb61g5_fqdGh8aGIFV1jGdlvnbQqCDWv821Tqn8VQfQnJHom3i_jRqa-HDpnkxk_eI_jM9l3RFLvv2l--IpbzAF5YvYF3oypwuk7fPU27HQ0wpHKLuUG9LIzaoYlu_xbOBl6lXHCbpExgwapWzVkASz4F62bhGfoDGNSo_wCyneF-NaHEXjt6T8TcXSlmQy8YicaLLwnE_NUQuLz07ArTIJTpNV16eCAfF2eIcBcZiUjas_SLYXJi0SrBZBRTz5LZ2MG8PPMOKwK1SzQxq-JJkf1uubZkvejlb1dh_fKFVuR94WFuZIPxbynQzjmkAHWeSNZ_0RMI3bTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
