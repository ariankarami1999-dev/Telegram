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
<img src="https://cdn4.telesco.pe/file/Ryqj8MYsapvntTZpREfyy1ymTA70YeBMOZsBIgYH3ffSzlHmY8Ixo-wpTDE8EEmhiEo3kaxJLotocpdUs8o-NTNV05hTehGPSeSxeWMsS0YAocoqd5AHomTXkElPrykZeXi_PBMMBFdgstZQEZGdhBax1E9PeDdgYU4cOe9N894XFI7ZthQGCOG2XrHD-_n8nXHn4p1ahs7mrkn44ef199l9PJ0GSPciKtOuhFy3NyP492J9ZBiNTGYQD5CR0TBd4fdLCEm5HT6Fxw9rePBZnVG7dioBeJGdCfejNYIOId4Vw6RIsogm6KYYum2kxgSrApMBrRbBg7ZaULV2A00UMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 184K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 18:01:13</div>
<hr>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YafPWvLQQkHhYyJOnS0N9LkQzkYydtXwjq9T4ZKXJvjoO9KQrmZtRYSiAbuRm8cRzJqB7X0juwNAuXWW5tR68aHcgpwNk_aQUL8mcqJSy2CEFyOtyCfxSZV8u-qNmqhAOT7aEJ4AToWos-p7Q1NYTlG9OWIDOPATqus34VHHhk8Hr85DjimWwRZOJVTDEP4LFjBSVGxglxpJP05FpXVqh-XzRbvwQnefOP-w0-74OlQDLZDzEknrB_nUfmGtVRGY60vxB4eASD764Pgc88bQv4IFP-DlMwrgZU3aE1jF1Z_xYLeUzys3Z2Gd3J590by1BUhiuBHR3tv3ITUgAVcMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skdqExMqG85JDy7UowC9Z7jyEKY0XpfLJBsHSnSXPW4CSKsMauwcDkUQ9u9MvNXeCzwheHnMA-U9Egw6xoqxRYCAIvi2oeXj_RNfcUEnRitsU4B9h6tmocIcbRNpnDLS6QAUZtkqWv7hY4zBC8af71Wph_AW5MMkn00QlDhI8tcluvVojOZ4AubuKf0qrfeVrPuQ6_Q7y5ny10lCFI6-eVYwyL7cp9kPv7IwQmAFsU-HtfdJOvkGjt9qsyjFrRJL9jl3qq2TmWYiUGsHaltYuOZP4pfNEZ2vzuUthNwu94B5u576tL3NO0Mmd6hDbhIwxFP_1TdNewUBJeOMr2yRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyyrXZdDUPTxikXX-bF56HUVjtpTLv_aGuOESmm8NGpDyK1f4xQd1lapEnPQX_9aoKbqqF6ycB6aWgoWZZNC4KtQ7fgvWkDu7gd0QUOn_XEXCafh0dFvTe_tGuxEnd-BIo-SN1HUNrgLvaazHGdJkzBmHisaNumIHpCApG4nk7QzJlQXR62BCNJ00z84fqW1jDQQUr87EOzdvfkakliamHWwIhAozDEGC6-J4WVWkBKBjyX6H9PVIPG-3KK_4CCO4mBnH_3YAVswVx2gjFueyfy2o7BqsCNPAYD90ObD8dSMTRwzxYSFoVdWYGrgz7y25hGPtPMfXljXk4bSJLQ4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRapht_DQXRs1wQ06i065QIltxaSOnFFA0oUjX1rzDTXZ9lzUNciIFzSGGjrqu-wzlVBe6U6p0bPoS9TzU2ZAqo5Zjttqscoksxz6SbtuwC0mTKxa4fg2F0wNJcCSjw9Xk86T-DtmLl_UQHzPa0BkeFWxMJc6qeUBJktMIBrPbgatnuRfnl3ZIolrNrpSCge-FKThvgTFFRVNrpP_ZCfq1fHA1aJR_n98hn5b-j63hYF5hHn7pe7aNhMhewz2IzCnonSDWd3H0aUdApqetBnbkQlFWQe42ShSGOfBDepSkEMP7bxnuvWUUUPKuDrYOCT3vhO_GMfQ-mFQPs4RA8V1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=wBF5tJdVf0cOv9j5lU58fk_57Xp-OUMYeLAVjueyDP8BAlFhHKXTXqqQ9GcVM78AIOGCLzu9-f3Xkho7xHHpCfu89CrohT4PklW5id8sul7wIEwriWSYdIpocsCpkD0UnChF_WxGs8tSvofPGl_ZzQ_I7IS2fXMCyHi-Tj0R--QAc88BNPYcAwca0zR5tX8DN-ZM4evb32fwEYWyFywozsEx6Qm00eLgp2JyWZh3W7rRXpWlJ-As_Ue6ul7rHuGBYIQGtMuJrF0h1tL7TjpP-paVqcV5ZaN4Hs-eO4mAeTXVsv25Q0kiNKeRJtcJ8bOJEvm1MJP_zEQSdr06Zrq0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=CnIqAPJeYjE1jf29xUHlA4bjdMB5d2GNSwU4zpDaqk4qi88OmaWVHi2zEjtyTTeB0zRhEzY9zkQKslUp3WFut9oKMVa2imjzZoSJ3Z0Y5acNI3ZE9LcFpJf83wwm5ROaWjgNjvO2TpF-usvryRwqG_hVqqiAb3V4cJ-aywmOhKJjbDX1YWaK0nIjDocq8Lkyyo3iI5jgHTEaleAHKce2H3-oMob-DmA9XjM1ac6QzzOJ5wpYpsaYduFFpQVxbbVoU_q3PSK6zRk-bv7ZjFdnL0PHPGMdwJyGRzGHevX6i5hVPb0P0mVUfPjwkNHBVbIWrszHuysHckI8-FSaNmLkHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qygIZNdq3sYN73f19X5NsftNMfHhYSU3PUYHjYTdRAk6vacMNxzwR4KxPns-6-vRzYlbjptAaze6rr5ZmzymfyV7-Ww2XYTQN2szqFh_IAfABSAaTAGXWoYZax4NUfmJxheE4jZyqptSXcPWbI2LwEABF_boMXk9Ztp0qm39q_2UkzmeGbpb9RI6Ri-Lhyux4SX_RHTyVHA0LMJXv5qTnSfEp3y-JmfwLMEmztiec6gZY7PmwyW7XUQ8ZKFht7T8SDSBx4Ua4NP7CXZQxx90B_YsrUC9j2hGam63yEJFZ0AsmKkAKE5GF--Iw_PsGhFUsFKKLr8x8MR2RvIDb8pWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC3IP1eMveuH-L4FkdaPjI_EO4XV1NpW0RBC-JlvLPukfXccsJSCiMi2lNcC_jrfShNXhqqrJrk6kH1hkXLjWZwy5H02191hABd-8LB6kdW9t9OwugV4IAB64sqVVGaH7eSjiOAfrl6FjMRmu5pTpRl8z2_a6lZusS7VB2BRc42imwQ5-9QBpoLHhH8RzLQY4ZBtnuNNLdMzytTbM98h_0m2cj5PbyQ7-OiLC_f__l1li1tn9Vj8kCEcpI9HEJs-owbIP4jMdxIxIbp5iDr8u8IY8BUhPntcEF2iDHWb24n_7CjcVkASc08odwtEcs1Ccdh4r7Uq2BYT5qtcwRrTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtWnV6AIKzVpJv6n2TDy77jwvB-Qem1rJYFjdGVesKNi42wFuBJJfYdk3r1yTfYdP49IKsarjTpUMjAfXfUqg3gsrnAceQ3zAFVt-hn9chiehzXT6sI-RzuAGDGha5pvMVYrziGsveNGX5mUv7uw96EfCpaW9cWRFwH99WHzcs8lutd5_J9VfQFuU_3brnnNsdw7E6VUedCrNDLjo4S5AOqAY8oj5Tgj4DYaGhYlnvSNJKF6e5BdzIC71GmCkNGEs4oL1uRuT7tTsIWR2fw1R1nuYVUhzxrM-yyelEa2CZOzaTQEfPauxjP-HtGcUnmJUd_5dhz3-QtBOSD3Gn6SCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBTqIzJAcFn76Vq_CabmqpyY81yEOXjJ0bGxdfbgb8ddmm_iZJqDOtQaqpEbPVC-67ukX1ApINcb-iQIVZsyfbnt94iielA3IxZkmgU1PUk38AZuVQAmRUXDKhKgXi-VHmkZqwMjHrbL_PjxcINxwqbmFMF7UyIX0QHiHMbxXdX7uIP7tn7PGOpzrz2XwxV9M3-2Vc3SZ7LFRX0VvMQCsp4sGXqp4NG0sDU2y7qTUOWHOddbEC1V27vYGDZFAsBlOJU9qH3yI3yqOC_RA6tejS6lp6DQohznkWykpYkWGpmTwUUNrKsYVky0RJQTY2mVp_1lRBwDyU6UJyO_PmZ6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Minxp1xQw3nyIxcTXVN2yzO1W36tCm2p4nw4FyYpnQKa7WG7iwboQk550b90URJ9heYNu_YJeQwV1VYRoe7B2IRgYACNG9snJjb5U_NobxCKFCK275LIjIJ_ridsheprd8ndIS80M54zOeGHUBXB8Uju0V-Lga-xnpG2RT06o2wRY3TqL0l9lDCQVlpx5KhMST-CWFopgvjbZIbivx7I6-3QJKIYJaZslNvz1mUiroW8wdS-2SAbs7DwsdKV7ofDrbAPruwlsfNt0vYR29fyyGX8SSma8wD9jT8i9ZexReTsOdBDabE5w8gPIwPABCtqj0oqIx7gtPLVqMhY1LTv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6q5J1cCWgCyNklCEgwOid28xn9nhiWegCcZkwFvqA2KOAGK3ZNvezWGuqD4l2FDwZzTva0VoRxM4C2IA8VdYhPQ46umBCg3ZsQordyIO0HyMBcyvX1aVQ9uDDaTcKPDPnAInMp67ilcsmQ-8JqP-OP6-JUg5qxlXVksYE61uB2FwvpSyHa6JtFGI1-kXXs_bjdeLnXV7-GcHRyVwVhKKAsi8kWb-DPwf3ZrB1hxiR2T4CIg8lrG3Po_--EZuzDq5iweKDgnsigz6yNDNmDMDgtpvd0jt1B28GSS0e1VRSk7Jh6S3aAeJ-1dMNfwnB5XxD2rijtKVCGaNSMqw7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنهاسایتیکه باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/22378" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LnTn1RGo-AxOyhUFfgARLefoUJbGzaflxwgRgFkxOgv4jo6RH1B11UOOVLr2odHtvzsvkuIikDH29TncQ_Uxb4OWHebc_6uHXCiAGwhP1wq8lH8GTjQWkT3WqyV6Qa66HxbTEMMgZCj3LXQum_ma4sP3DBbgzJ-Fd0MqxDvyf4hlmn9B9OVTQcxSXlMbwIaO5FRnwYGQkuHz8n07BDz_vHx1ankUDPbuJlNAkLIDJ4OErVkLwFtxg3rPSRSKZNnbYO8YMrwkRduAZGm_NqUJmFM-EnaOyz7okvg7pgwgDf_vuSfteNs6Q4ZPdRhRKI0vWCCtkHWocBhqrWur2OgW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LnTn1RGo-AxOyhUFfgARLefoUJbGzaflxwgRgFkxOgv4jo6RH1B11UOOVLr2odHtvzsvkuIikDH29TncQ_Uxb4OWHebc_6uHXCiAGwhP1wq8lH8GTjQWkT3WqyV6Qa66HxbTEMMgZCj3LXQum_ma4sP3DBbgzJ-Fd0MqxDvyf4hlmn9B9OVTQcxSXlMbwIaO5FRnwYGQkuHz8n07BDz_vHx1ankUDPbuJlNAkLIDJ4OErVkLwFtxg3rPSRSKZNnbYO8YMrwkRduAZGm_NqUJmFM-EnaOyz7okvg7pgwgDf_vuSfteNs6Q4ZPdRhRKI0vWCCtkHWocBhqrWur2OgW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qujpee2BTT0paG-YbFPH9M7mPpjPLy2ER-bsUn6UWtVglPCa3vMYcgnletWqvhbV9u9MaGsfSG8NOztxR6ukYHdRUOyZ28CnHBIT9Pb8MI4WnAj9YG6NYUXaTY-4smiueZLkx6CUwwds7yR9nCIG_VtbAM6IneCZH1jHe-zredlW0wa95GRSPsHmLZ1_asxKRq3DMXuGlCYPpgiHuj5sFJE0rFqsOCF1-B2K5X2ueQyvd99JxUJYJXnHhtFZUq1_7P7uNWbalncP3W6PxTvPCo3KQHkbzvfduDh8cSQnFXQWG_5yWJ_X2gp4bgyvM5_FnmnCm6exPDKNPydDpj9inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6MBLnnUevNHt1JJIOb1s0YSo3KAY9Bak3hp9SE4qLim2iH5GT9wC9zgmytJYqTBfYkvPofFsaMCTB51ttXyDGzcSkHZNiE6DJR_o6e6AhHzr-XWQ1aeZHbq6ryHpBHe1pALGqOVrCZasTbBv-DiOEDE4zh9Nqo4L0paVLVoXM87BT4KVhY63rNX0Tm48n1zsMvq-r5AP4LrsKloJjgEpwDiezOZwwxG8CSFC-fgQqJvjimszFlNRkQNtt0lXcd0_6I9lOCdXCjBn_9-LgB9zAwRfYp26517RSeS0PExmGOspBC509rCMVHRWWpsOw41Hp-C5ej6q8W2N24uvBzL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAXrXdn9yQPqxpbNTmarBBvdl68iCSe4G1yHBJuiCOUqrQSJuVtFcOQ1LYI9N_Oe10cuz8wnXK3B3qqNr54bXo2bajlQhTgJ-shmDsuVcOAUBFUbN7pmXE02Kb4NAqVoPHO7v6FkbPA6r8d2srLMSUt7hwpW6TuFOhW07vGIyy0wg4KGCqZS08SeTthLkHrxUtVZxunCGxx0c8GwYte9NuvPTwsi-6p4QQTPd9PGqFq5iK2GQDLOBobDNfq5TwTJ8tT31ZqBKjwb69_ZGTijpXrZVd9EbQOZ4N8WcKrA8f7dv8rClaEPpedQIbO9jGHNZmC7gWYbpyJmCu_gVZ6bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUl07PLynFV6ZQiLW54i7ttZNGXmXwGJKYe7eR9ZHVa4nFlsP1Xcg8Xdg33uU9Xo_M_3PPdHbn9A5ZkKj61OVEdo4ocshlD9hEsyq67snoPBzB7YrawAneGl0TmEzgcELdfuPl0zkwnDubcjoer1L7QaSTVxKXnIO83xpc43kUfXfoIdP0R54pqjISzCFdaYhu_FEoD7aweDoYb3or1n8FhTlFiRSNCR5R6j4eG9ErPvzHaNRxbCVbhkzwrCPVcRbYNAmWzZmQUXmRGzWsF8mXDaqr1pq2ADlSjWhU0YkUEsEEsNmfXDWGK7qLfROZ2b-gJppTFYy6X5YBd3ZSbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=c6eEGrctUQFPSvsc3g9fN4-P8OAT0IBKCAcLqR0RnY_zJNneksTuKzkmuvkda6YcWLWTyhDNuMqkDHjRQvFmOoThdQLDIzIoVDF67esyc6NNPeLFnDZ3HTDr5i8jnag4kKfGduTRnVCEl2zSqeCmcUt5MGtUXqH-mTe2RTi7E0wac1cw3Ew0HU5ONxnkMX45ZCm2ZZX-L01obdJ1If0vpdTR7-85RjBvCH98DZAiXMYR0QQAmLLWwmiqroKtNUK8c5i096s6WDMYHxzeYPEPqPkFgykIuZSKi5gCsw1LPFPQm_tYfq1NtEMZCrTjC-e-AYeAPW06RlwA7Db1mFIsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=c6eEGrctUQFPSvsc3g9fN4-P8OAT0IBKCAcLqR0RnY_zJNneksTuKzkmuvkda6YcWLWTyhDNuMqkDHjRQvFmOoThdQLDIzIoVDF67esyc6NNPeLFnDZ3HTDr5i8jnag4kKfGduTRnVCEl2zSqeCmcUt5MGtUXqH-mTe2RTi7E0wac1cw3Ew0HU5ONxnkMX45ZCm2ZZX-L01obdJ1If0vpdTR7-85RjBvCH98DZAiXMYR0QQAmLLWwmiqroKtNUK8c5i096s6WDMYHxzeYPEPqPkFgykIuZSKi5gCsw1LPFPQm_tYfq1NtEMZCrTjC-e-AYeAPW06RlwA7Db1mFIsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbC3f2WrFQo0EwfqRE6y5nrVy-soXSYL0Xt0EzJMZ7TTfTrwXJfC3xpEQywdhWZh_snOOTquMp0yYJImBsOqttCRINpMnWJKEzZoYMHMUYwl6u-spc1ZFfaKjRHqZGlk_mPf06Aape-7pTu00Ifpv4Elbn3n9ktrMrVVwiwf5D1mFLN6bgpm3QBUR-ruit-OTd7bdPCCFxjwqFuoQZFHAAcV3nm1RjNxkfftk9wtU9Pn3DM4S74zdj_47S6rNtmdaQBrZnpjlv-t-rTpnxZUW0a8jGAmGjrd5UiMKOkpEcECsVhs4L0aaU-5E-nXzul6mWiULX7p2y7OPlw9mVJ5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IygrrdbWIaKnnZpU7SmIkfW7ZAfQCis2tvYU-q2jMjW5hy4jsoIhLSWjG2fCHZgV2G-a5fQ0gVrk3XQmLLVZ3K5p0B7IiBnhZz2qZWqwIA6NTNAyOm6ymT1h2-H2qM6AjFE8lZopo3otTqR3UfUKT-qD5DAHzt9DU_-cPu5JZ8GaFB-n5dZFVM0Q1yEIzL9_WoiqRLwXkXWNsG9Gkw1mKuqt9ODgM_3dD9PHur71yBMTV_xlb3i84KkTXqlNuA5FXwrnXmJ9Qhacc69c-1XJ9bMYouqOkffykyk3fs-N9Ghoso5HwSMZqkDMQbFsVwu8JvGECOmgAUBoHvKqL7QWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Guw-6r_dZWUsVgp9rE_NdZShdF9GVvZn4rbSUFZYOt1e92e8vJgkf8UEI-uPaCHfw1JJ-H-cueAiAX2k0g4JXBngVY21kD1Hb1R9v3GQViNIieHXZmFhf2upzxPIH7QEy0eWK3B7CxJ67FJ_yqWdvuFrmidtKNoBhDhBGPDBANvKn_fWE_ZAQu4-DMhSYq6qPuoCJHtlaz7fR_R6s_UzB_m1MpP5jC1c-dwO7KdmTFkRAezuBI3c5O8m3iv5znx5Y1oDPIe9LYuGp5LgY8naoFXIrk2k4w49ZpclDaIaSybPEG4Mf0PIdBhI6XYn6nQ2wcDTYnXuOtsJcL7SaePYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=Li5SnV8WfkLUNdiBHndQPbKbw38p13AbEzbgo8gUXFkqMJ_HfzOXrHFS4mImG5gC0OFf9ee5rCztONZAzaccyU-jHiLn0EV8XNFLuXewhq4itQy7YPI2f8GZQHVU62E3ImBDU7i0BWplWTKzZKsAPYGFdOpK-1iB6uzIBIwAkoHWNICFkMWvZd-SimEIt3BwmB5tHqbBdixkgY5NAyKIKdmwrJDwjn3q0QcTxZkBmo1Z_H2fG9goc77oV5BJyB9v_xaJfKreOqQe-8UMzY4nI3N2XHRXpw2Ufna5jjYjksHjY1nZeiAoEoZz56Cq1dR-lGt2gQxM0L_DCOXb8LFbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=Li5SnV8WfkLUNdiBHndQPbKbw38p13AbEzbgo8gUXFkqMJ_HfzOXrHFS4mImG5gC0OFf9ee5rCztONZAzaccyU-jHiLn0EV8XNFLuXewhq4itQy7YPI2f8GZQHVU62E3ImBDU7i0BWplWTKzZKsAPYGFdOpK-1iB6uzIBIwAkoHWNICFkMWvZd-SimEIt3BwmB5tHqbBdixkgY5NAyKIKdmwrJDwjn3q0QcTxZkBmo1Z_H2fG9goc77oV5BJyB9v_xaJfKreOqQe-8UMzY4nI3N2XHRXpw2Ufna5jjYjksHjY1nZeiAoEoZz56Cq1dR-lGt2gQxM0L_DCOXb8LFbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjzE_qm6Uw-sR7yZFeN6qeQVCbzkFj2rvYWHQP3SZ_88EBExhN5QfmOlL-nyFCG6K6CAiJKeCA9DRA6yEfunxYw0IP_XEP4bPlqYwc-53KWkhV1ZogVPOGprU6Yys_YODvmcWoXpCb2alBpsxIiweTyasrvAO-2RqTgl1zAdqmCEW3FUG6x250I_2vEBXYEauVrl06_IGiSQpSiMKdFH9GWjcRrF6_8-vr8HBqnXKVfRQ5sKbanCFI3jhoqY8rPCv2bxy3RY1SAdnpRXfGkI37ebPdIO-4g_n899tpDeQkER8nZmQGb1PqbUh9G3utYvl08A3w3SqL4OGBRf_N2_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaOOLu4deUK7xI70VlpiNDyGIGIhtZz1WGjRvZCjtvLEyndBn04lMT8eW7lH3goKz6OTbEBfNqaeX1tZuas14yTf9S0AABKfOKKPjw_0Ns9P_m9v_0JCUdvkyaXGNFkYitngfs5-8IT2344I64RXj6osBSEGx5NO1GNiVr9xlygRaPZgw3ZpOP8R0OmRo5uVR8Jy8LpmfOQGFBJC5rQdV2XZQHms39ot7L4LZX0Kb_-lBdGTUpU5Ymllys0jojTE3co3MNkDfYDLnLJIDYPKexVWtnLq-yisYBxL6M6IsfqbRQjUnWgomock03Ncsi9Ggqv4zEOKmc3zq8QwistYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMO4wD59kY9TzJZuyNrQ7ptEMpSfBqsCvTI-olHyYhMO1bOkzGhAuAzoCE67IAxDq2X_EktMFSJ-LA6bbBa6asY0I0NzlHlIFXdzVjy9v-2WAFGw7MZ4vLd92aevTul0ypJfs6l53IkpqyYEvknvveAqLsSTH2N6-vo7sWJ-32UGU4miNT7mODvEUR8m4fyu7GaBBVbISyEBkgIHqACjy-PAdS3wOiC8k0r1MYSWkjrSYO4oCxyAJn8Q6oaMjNyHoZ8HsABAXJDfeIlCKMVwKxLz3NH-dS8Oub2FizGIVXDK7hbXmsJEj94k_P00GKkREwYIwSO9X3MDLR4w6GvY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owB7IhEE_7KlXugIvpl5eDTXy1e8lYLBwxK3OOg7RCyyq-STVTUEvIw8zXrn2Pr16t07I0JhRix_8nrCdg-FJhvvB9X5V-jHkYjQfmxR1YhWYWJqdBlRSV4_ijrI0X_YzgX5gDwioLdM4pftAILIHkaQuMvuNehrOk_ZqivZUGQMuEqW3-lCYLTJLaWfElpKaADOmPS6gztq73g42nLx8i_IPMfpXZ9eQAJ-sqaxtsl1onjjxGrZbJiXv7hZs8NX89c9hHT3uj2NMggJ1bOioGcsuGX4sR2RRvvf574DZZUj4SVS1ujynOHfDNANRarqcupy_jO6joZT0Ip9_qKMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=ahXlF8rZJ9mGGfzu1ET7Va1d0ChcUJHwH4JDVG2_yMBE3F0H7ewhNDk6oQE65y_1iZ0dhscY8T5m19HuQe2LGHAjU77HAf9IYc31Fx6X4-Z5FXUFLBJDyGxbxJv8HRHaYcajQY75-7yBT9y2Cm3n5vQBc4hlnsKG5AJAFSJRwuRnW1TsgkLJGINtcmpp4SschWIXGV7uoiRWX43_KiJMlUMCSaHhdt32sMOpg2Jy9L4WL7svw5OkWf4rSVwUG4vgpOr2zV43EAbgGkvHyJoMdgmYFJb3POZoEUpg9xl0nvIQ2vFsCdyFqzC2C3XmTAMOMQaRBjdIXWA_5MYual9YFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=ahXlF8rZJ9mGGfzu1ET7Va1d0ChcUJHwH4JDVG2_yMBE3F0H7ewhNDk6oQE65y_1iZ0dhscY8T5m19HuQe2LGHAjU77HAf9IYc31Fx6X4-Z5FXUFLBJDyGxbxJv8HRHaYcajQY75-7yBT9y2Cm3n5vQBc4hlnsKG5AJAFSJRwuRnW1TsgkLJGINtcmpp4SschWIXGV7uoiRWX43_KiJMlUMCSaHhdt32sMOpg2Jy9L4WL7svw5OkWf4rSVwUG4vgpOr2zV43EAbgGkvHyJoMdgmYFJb3POZoEUpg9xl0nvIQ2vFsCdyFqzC2C3XmTAMOMQaRBjdIXWA_5MYual9YFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk2UL8ZxuJ8OwCHRuOgoXkK9LKwGTuV8KDGKGNrpmlLJiG0IIJZ6gfnsRtcwZrtef5yjm40ZxvB114YfA8Uu3y2wIk8Mc7B4JS7fQ3ZetRecuSfmKvzXi2h_8zsDs1TQI4tH4mzySrXPCYFLis-rNEOikSMc7KnmYO4gDByUn7W6MCN1b_o-iAiNJX6yRmvtZ5aSpol16ga5azf0t83Yk4B_RGTbBmgRkIAfb3zbfzLz8Hnf8DFFhu5nIKTaOOGP8XzXjwLUcJn_-LuIoTLplWRr8sz-Zg3XTaME4DaaydIlALCaVLLEP03F4X9M0-tGx21_10Vq4H9W9WiV33H1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=uZLW5G-kD6CJ0f7SMVPjEvOZU1V4uKo6oF8ymz0Jo65apK6KgggYvTIg-Y-ghxmNQ2H27pLLWLkIq22BzsMEubcnFmsT-_6WfdSbgxChGKHeWlawRvknANkCC2uDT38enmadzCRTBG6U_t0-RCp_AwPk16O27RSdYuLRzExCgKBQDoEdkralRqRPV12a8o0C4QtapuDQWisXLRKJ5HyvYi7tnUn_dp1ZaLJNUXqNqrS315AlglKCQto8Tar53yMtSef2DZrCpfj_MOApszV9fdE1l1RW8_bA7sWDCS3CsbZh_mkuzBQRGUN8lbG6-ktZuRCKppS8bvfdEyNcBznoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=uZLW5G-kD6CJ0f7SMVPjEvOZU1V4uKo6oF8ymz0Jo65apK6KgggYvTIg-Y-ghxmNQ2H27pLLWLkIq22BzsMEubcnFmsT-_6WfdSbgxChGKHeWlawRvknANkCC2uDT38enmadzCRTBG6U_t0-RCp_AwPk16O27RSdYuLRzExCgKBQDoEdkralRqRPV12a8o0C4QtapuDQWisXLRKJ5HyvYi7tnUn_dp1ZaLJNUXqNqrS315AlglKCQto8Tar53yMtSef2DZrCpfj_MOApszV9fdE1l1RW8_bA7sWDCS3CsbZh_mkuzBQRGUN8lbG6-ktZuRCKppS8bvfdEyNcBznoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZBQH-I-4kpG_YQmC_XdvpUVOyAGCK8B4SgVwV4twHYbKOZZc6drkJWNS2OueXVzU3A2UBv_QC95A6f82UR526W6NqNHjNwDpcQbe5Tgy6dr60j60fFwjtZN5oHKkPr6R0TRwCNH0GO6rSITx3DNWpeqY4UE8fDXjpz7kuVY6LVyXkFoGJmjoll_5I3apYpj13ffVausSwsA2KvR5jdpyO1NSo6js1xvjL-FThh3YYV-I4AH3s77e2f0dEXbwlw1RVEs6mkcCXFdmCJkKe4YSETtX2WiMmwbJ6iKWtr2cAjDeRNRuvMuv6Wg751fJ-Hf3BTLPLD-xUNKM1iKdKJPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zwc_JiQWbeAMICcd3l-1aZYvAVAqoU2et2GG00aPrPEzV0tUkccgn3LXL85xXVaGZqqcyXHDc7hR4LRk6foMPnlvtglTKLnq5of0qzgcQzpeg5ImE9qvG96npwag2T5Cv-uiAHBpuzmXl126dg-qk5d4g42V7ACpcPw9wm02j_pIEN_QOzjOo9fhKw5OuiCtENEwk8Mn-unohh5ykiFpaGg2oUzRJwZTRYmS0mN4Y1hwF_WDv6HQAQOnGoTYwgEX3LRPXUR0oUlBTitP4EAbgavC7f7_VPLiI9WgKwi-1rgKp-4Lp2FI4e9CgjovwpaCip81NPkJIyDnrIzCeOpdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJPVUuvTpaBbKpofPrJGPSgNUn46UlhPQBFwIplhf-FLexDRBUWy2Chus49ymYy74O0Yqpom2h9igeiyfYx-9LnyxxCpqr4oTqloojUC0WhLzlmY4mk5znlzE7UKxLijpftkW8zNTeZ37AOL7lI4LJ_J1RyWZJ2HGUsZgsFwGJcoX7-OWnZk3yyfkqT9ItY3S107kSNcgwiS0lGLJPnR20iorneaw5VQ3ZUvOv185S6myfPe2XV3Kjw1rPVtTYkPtOlNCNAxGqwyXWb6ukMGlcvlfbcv-LKg8CxaIep2uXKe9s6lvk2rG4d6FpjAHgA70Yubo26DJchEaXi6681JYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObS-jBpLPACx_-_M7qBMbAQPwoFkbG26HCBkBZPcYT18XBxr8W09FvqwkxU96velbdcnNQ0hxUerVYlGdmgtptidkFijeFA5HuPR4eEkJ5GVXnGP1LdttJNg9o1BvoYGemx8sOw4SXMJOC7D2uB8a9TzTjxZuPdednjzjUNBkjdvK_WwD7KZ0bqVOlLOzY1pbh9Alp6SnoW7Hhr1qS80OvEkSlf3B7FVmqCNmMooVB7kqSF4AXGaUSnIibAy2BxgtM90tzIM-Up4APgMwUI0LlYhjpQgl-Qsx3CS4LIA4jSMFNeqAeVeeEL3Ehl9yUXK4tvfYcwyVu12xYv4oExk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoPcLlGzCF24_1c90MIuxfDlxdaPqKoUE4xJmg0o00JlAMuDG-H7vsCEy_W6rRkCZGNHSjGj4WhOLgZP-2b4TyD87jhnKsd_0Txtrnr9RrEqV3o3drdnN7AEA8uOUjPrURCYSEB1iciUJ6smyzj-2fjctVKQbreNYlIb5JbzQY_f6lKq79_jvJkLyd0FLUnc4tPIMIDH5M0EQDEiWy3c3z1hwbvXkfwzyWMCiIBPRREKmXQnCjXjwucbbHhrNLw7gvJ00wCJerdaADi87PiFwx7kQdVUCx7Bo90rUmp7ewHi5qFWvu5x9-UfTDNwakc9cfzxcqAWmL12DQFQkbQtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=IPl0M09PGiTu4Z1PjloPCTsIr58h8WOhJuMqzECVMaAdi4uGALm8ou-uit0gYntzeumT2CFSAQkTfbctlsBfPdvVdPF2mNi1ipO4RRxzDofI0tKquHgIS90H9XJWkuZmlE2JhEbfW4jw4elSbLpodQA8s0xA4SApJ7KoQXvThHFx6cYitBAb3xiR5dshAZqEb1K9B4ylpvtY8PprLm1ZffjLDZkJjb3MFlRr9lhRFX2pDoi-pWox4y-khWqWUulhQw0F8ctPrPL3CGlBW7nPJaMvvbgjeYInQ3VZAQ_CwpvyvG0_-lSZ3-KdqPOI_ttqyzDDL4n48TixVqBametOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=IPl0M09PGiTu4Z1PjloPCTsIr58h8WOhJuMqzECVMaAdi4uGALm8ou-uit0gYntzeumT2CFSAQkTfbctlsBfPdvVdPF2mNi1ipO4RRxzDofI0tKquHgIS90H9XJWkuZmlE2JhEbfW4jw4elSbLpodQA8s0xA4SApJ7KoQXvThHFx6cYitBAb3xiR5dshAZqEb1K9B4ylpvtY8PprLm1ZffjLDZkJjb3MFlRr9lhRFX2pDoi-pWox4y-khWqWUulhQw0F8ctPrPL3CGlBW7nPJaMvvbgjeYInQ3VZAQ_CwpvyvG0_-lSZ3-KdqPOI_ttqyzDDL4n48TixVqBametOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnDVxoNQukIDoHnzGOlX4UxfqQDQtwXkmLoPeahUIZVlKsPZavT1HhrZm1wjkhMMhowIrFWPIDwkhn9jWHR4fx7W_Jg-8PyYwG71RPKnxyslVAnPGHoR5V9lK63UlftLOoRO1cc5lJqvFtMDQJBXQ1dARk_jYW1KpbMMVU7DxAG2-tk86C_xOzFWRkxjryLXRo22ZjZMlw5To8NVvKS_vP2kjQzn6Cc-IKf1f1pjz9hME8faZ3HCaRUpXISINwzEcTr6i7nr_GwjRHD4BUDnceL6JTrKGpisYdUlIEpxb45pOIkeX_qT6jtcfAiO6DZBMojXCOyhW3bdEOV99q1TCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtpiLLlhUi2vReYgtuHQiNy_e-TjPdxjxu8kcScO9Kt4vgAFYzcMB1MJFhlBRJdwo62YCpJrHSwRlZJPrXiYzn2OUSP_gpkewhx6bZ9yDTdzjI1Jyq9Fv7kGtWOrMFtV3mFRgCWSOc1B1OpIhs7xI03UAcoKUo6V2FJD3Eeue8MJQqd2iXnXZ-9ZZFFo4HjzM4P-kiUtsX_LuNIuygXYJHliCOws-HsMdIcISkjzTzTEeJobeeSKvYu_-2hyty_7wYqMgpOQD7PyBsHggI4IiLFlR3AUmBjwIcOwQ6sgmaAJ-BGeDRI14vLHEcJ6vWxnMev9-8UapmlxYofFb7IaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=rNKpVgmazwiLVzuXuGi3jYW2YJazBbgF_GsDzl17RHFGDY4eszwqtQij_ybdUVhDO7MGA1gWE1dC9snKPwDQynshWn2kIzMLWZPmHoBw6-HslboPeu9qAK88VWq6akVV8I5ROVARL_TwKbARldMepFOj8yl8cxE6hw24EDf1usLp3FWlw1qqxRGvjZpKW77bd7jBNo1HjbNHpfYL8J5HbRTG-OIlBFX7iOEd-6rSbpWRmlgbI2qzjbUSrsFiYdxj33BCg363nlup-6leTRTEi8FK6Tz0y2ZcgrSm0oVXGoO98eao_DOON_hXs7NvOJMtWl1V13efsbTJOW7OMH9aUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=rNKpVgmazwiLVzuXuGi3jYW2YJazBbgF_GsDzl17RHFGDY4eszwqtQij_ybdUVhDO7MGA1gWE1dC9snKPwDQynshWn2kIzMLWZPmHoBw6-HslboPeu9qAK88VWq6akVV8I5ROVARL_TwKbARldMepFOj8yl8cxE6hw24EDf1usLp3FWlw1qqxRGvjZpKW77bd7jBNo1HjbNHpfYL8J5HbRTG-OIlBFX7iOEd-6rSbpWRmlgbI2qzjbUSrsFiYdxj33BCg363nlup-6leTRTEi8FK6Tz0y2ZcgrSm0oVXGoO98eao_DOON_hXs7NvOJMtWl1V13efsbTJOW7OMH9aUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiRb_Bx2fHpbpyOIXzhRXDdhPiajdNYV6YL0MtOH3W-UdyEDDk5UeNiUf-HsFbYKCROtMTHWsp9UWqQKABIAo_i79MOHOzStW0HUcxLqYItb4DDtQTVKd_hH9TE2JLW6g-HSNi389YfoFMu35Yl1yC7UpL1bPjknDKpkw2HhC3KUL3YXZ9pGDyc6p3VolyjGBnH0qKJNu47igBBF-9b8E24ZgR4fNNka_NMsEjoncqM6gHkg03dFaA4ZgTqzpO0x2Fgzl1yfrd_IUntx-gnP0AJYGUyTiXMrD6b-fS6xuj6FGYePnVotufQqXXhJK_8Ntsh9lD4dHRtdhHE1Mtbgrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp-lSPD4lneiT4O5URdJYRrso0ZiMiwMahz4OZ-_Fp8BL0gJH_iKk72r6N6QCVl6b1lpdqpdm3HpqkE59V85gBpzkg_cItulsh5hnVpJZSlLu2lcCLptOSXKRgnn-oDSORM6gS-HqFheiYMMiuzEYLu-K8mgo95ssTYB2ofM9aFP5xqsXUP3ZMpKHZ7jlT0LLRVrAEGi3s8arWCMjogfqaZvf-9fpKPADoGnuLZCGG5omTqKxBy97-1laCeKubvtWxLuBJT5lJuHz_X6hhp1-8mpRXRKHDR1o5WwXSFVnXeBJfUIbsStbAMNYP1mHkVnPZXhoYa3I-6noUw4IZHmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UegofG1rG-7iifG7HtqZiEy45ihi1WzO8hbtgUKFgGLVxaoc0wkJlCXqPV02kA2iCjbCnOXU9mBw_unt-Hc8va9zOTJ0pVEa4IS6mQ9SRh-f5UK0qCvdHh-FuQTG4VijssRCfEZYt7vNC4GE1g-ORh1PIyaVOAM2iLF05uaKODsiM9HLZZ3hI14F6GI-lOLGihsVlCxFQPSjy0t07XNV-xDP3tc24GcwShZBK3zP9HdD2hnUr514UyiJIR2CwS1EC2ewZOzLHw54nYGHgN4cr0qEXjeCET50Usx_FFjde3_emuo57PDe-G4IoxQAlJe51QJ-wNWC2Y8LkJ5LpYcpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxkvKnPWTJe1GNqzphK9wkjeChC8ue45XHOYHU-vqoY2CIWyw61geQnWHkezPMc1VtVZ9VLSP6vEhtKQHS0Pls51W12E3UoZdMNVBYo1jNtZvSS5GuKF6obOIoRRWF-kjf8R_3x1Yl0TrLLe15h_-lGlL58A7VOQuwLmYZrAi93a07r_BJ51O1atUD-FInnm-FiIvPQ4I9TkRDQU1jl9zKxVbbpK3TvyfOt1GNAlppu-ShfPOGTjC5wyQdzmAL08MkPyNPTU-Xsob1q4w0Y4yYnjAfqhNpRsvaZvJV9vyhoRQAK0cD4mkKin6biPd40aewZKIAmbs4pfMr_yuO2VLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJwWNLD3Y5FI3vqWSYdokReGx1BfvhySyPfokAZqGKGghcIEU-56lOP074KIA3MSimguB7KU5DD38Vn6DYEmffS0RAiv8Q7LWFdF2iira94g09IEWDZIfBqpL9qL0Ifnxqqob4fHghLNn3YyYDDon84W22Kf-cf0_Dgomt2b45kj5mMh5BOwHuUSxCjzqR3M31VJcYiHazqRZZyeOIlchmVP3IpuGvYyg23TB_Lfw5PtbFJjI8CpXCM33PXIr82sZvrFT1DPzvipJnPLxNGebO4XYc_wKD-_TG-MxGGmRtQmhPymkd_iCbG4ccdQvO3vVfd-vIavjZM4r1ezG0h5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAs-nPt3BFuoYwhwivq5a1pjfjBbxRQ3207SVoiF-G4talSLj6PrTj1zP4VHs8nfwVDFQQiDzXDwrrIiCM7qGB_GwmdwAif2VkrNRnpt9N7iw3a_0NpFMfisb0Qw5xxA7miXA4iqWgkBzQS-0dOsLAzZzKxzO8V3GqBUaHijOagFqd_37KYLwcWnS0NMa2wImQ7IrqqXe12k8iT7TOQ5xytB6eMVQ2gY2phMCfHcqGM84WWizULqFKlxuMq2G889Cz_sfi4sCz1t8FO9qNjAaJOdk02AcYITqE5BuYjQUZNlQdOmIsPg2mDl7eqMr71_5hGmTps4f4l8BwxHZ-FFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFRhKuA0Uqf5AsPZaXjIgZOBFZFWJo4H1Gjl1jD8ic-BsOEMuYWwxjkcluzijThUSwgrQkpvCkamSDcE_plorUg0bLvioRtUQYY9QH70F6mKcNer1dNLBlpRyOnS_WOWp9TzdZ9fur1WcgDZJtZYP2fgTzyNwWRjuRlp2QcKu3VeE3Y3HOYEks-a5lTXS4oKAxL4qQW74_VMARcfpvljPNk_TG107G-ISOUC_u0khUd2bxDHAn78WiQm5c71TrnpmkDmcHS1qDe4qt__---d-omeGOaDZQgnNsdZxGXEhlZkNiIPIu7JL9bmAutNSEY6Br5TACUt0h1eECCW0MpCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcLHB_IqTVB0rHjWsQOFKddH5DEnQ97YkxZollASPOM_qiGb4O48p8wbqeG-Mt_IbaaVziv0CU43LvGzQIhODmc_17kNoMiAf9vda5-lziCkH0MSOpi-4vJwc7OSLktmGapshrYi2W8pZoia4vzwq3W5WGQxAQwpF6HdiyKx2xjn8SXYAIg5KZajtmWCKwEo0HgMf1so3JZNEGIL9OnTgbQDaflLdiEiIJ37oTkOn3E80sPErQGtOxiHgJY1bwSBMI4HXKwO1qrx6PwzG-kd66c2EkMatM9JMSopLZLL3gfOfBbPJVb4121M4nrdcN5Uekoqn1O9CfTe5z_zLB7_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4PDYmvR15EJNfbtPSl_xD8oHpmQnaxj3crGIZTQk2nG2ZSQLOSyXmOwo1Oi_5FbMrZX5Xs_FEqSdglyIxkPDsfv55EI0b5jTYulmSphD4zbNmWgcTJcAbGK3PSK_aWf7I5V5pWa-tmPwscJHpNWLwDu4TdPYhIvJViAWE8qRCxjIFkmSGehxVKW5QbdSK4zmaoM0Wnfpe4Ua-Y5ECdAF7b7EZjsl-iEuu5S8YCUqOzOo0Jfh6i-vVzm76Pa1GVP2E4vQcNVjMFmmXw0Mb_wCnjjspUnFEPNMSw7o3Vk8f3LUfuW-YKU2RU5dO135LPPmWBDAAkEdzLx5BFIt-f-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tttgdmtXO3PWsu4YuEii1s-2_wB7t9rS6ph42C2Neto99iownmY_dqu__2JggOweba8aokvIoYaH4nv75aFMsZIldKvIU-UHB2QfA6vIzZKi6yBNf7VVBf2Ul4FTDu9yROTzGXdaT4G1p8soEwKpsYDTuTRNkKjUiI9NmUq8SGoFyfAwhMATV6jBdW7tsRjrI2O8Lom6tar5tRHPmoLhkdeIj21xfB8LQTqIiCflVjr00YkTn2dLXu499rHBwCk6IUZTooI30U6ZQASO8MX-72yJDm6JrtyCWMOJ5Y9qnHFahryeS4RAiN_qraPMuqC66rP-QYyf5KS1d4CU29S3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=VaArecR3EHT3XCanVeSSBN0MGVFbnJGmIFqo2QOUAS6vjU87XMzHvBYNqJ7X9qPLhGAvOEWQZ8P1xobMq1mOpSXR6to8bt2rYUxT_KW0I9nCO_ouvMq9l6aM6KGxwbJjsiIxiWSWQWiOHjOsZWIuKQdigqcsRdBs8WwQCGtiIBz9Xd-Q_o-AqcWClQJCip6yhB2UA4AiQl8PqPt8JP20wWMfeWBmYUahqBOPBqi1JrCWlFkSeMPLmhyXEHKys4WAYjSfmcUj21QcIOFLHAx4FoiOlPFfC7Vy2dJYKcl7L2ZjYEOPPbgHIKMX2lwIr9M5kfvahz0bzbg_vBX3j4OxdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=VaArecR3EHT3XCanVeSSBN0MGVFbnJGmIFqo2QOUAS6vjU87XMzHvBYNqJ7X9qPLhGAvOEWQZ8P1xobMq1mOpSXR6to8bt2rYUxT_KW0I9nCO_ouvMq9l6aM6KGxwbJjsiIxiWSWQWiOHjOsZWIuKQdigqcsRdBs8WwQCGtiIBz9Xd-Q_o-AqcWClQJCip6yhB2UA4AiQl8PqPt8JP20wWMfeWBmYUahqBOPBqi1JrCWlFkSeMPLmhyXEHKys4WAYjSfmcUj21QcIOFLHAx4FoiOlPFfC7Vy2dJYKcl7L2ZjYEOPPbgHIKMX2lwIr9M5kfvahz0bzbg_vBX3j4OxdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBW8H0KGxs-3_Z_XeM0gI4w9rNYobaH-POl9Y-07sDD5tp1GIXZv_GMOlTz0qgEAOOk9od0w17H8nVN20HHWYDz3gYCK4jjtOi7Jtk3Dwawp2gWOxUJYssyaStSC7o3WGMvOFAdawOr1fBwB4sA5P2SMmb75FVjBC_ZU3xsbpA-Fu1_EYD7A_do39RT4XvtqVy7oFEGJc0195MI1Y4tZawWTv_uPWk21JzwdNFaQbmdbTaqILKTg8Bpi4_I0gN8XsAnYDh0v0ZLiomyGx3ZSGogiJQCtlqBFZameOjUwXWvaAGz7pod86FLXCopG10oT9yXIb5ZcBUkFtXFo1Oz6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZqm9ZZBu4ojexlAbLZqTj_6KqxAuOZHARXYLMNWWz1WBN8dW53x5arqFjUFyCJazQzd7sneaNDx_yVs7z_8OsPp-uyX1fBpKJoY1hHgXx--U0-tMvpLSp8ycFgEfqNtn6mt9Rh2AsKNLp6VJfw4PH3RO7r2GxY65Vba4F6D61XmfOu0D9eEOzLKzfD385KZHBh-FD_YKyFXmAlz0mHnL_6HEDwv1edBLmqeQnWWkpq13zdEJf4J35U1snbKauTydHpWer4tlKHY3CMnjwHmLnhKBSLPJ_2QY_Zf6KGrbsu31bx6dEOJLhZdJ-g9alykckE7eCU7k5Lvscx4sNrFiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q11MK4T1ik0g8i9XfrQ1pMdcWsbtW7ry8BRSj2tvAhscxLILfCJ1we9TEsy3kW2aetOvtLBc8inmcCym7rgFGoNtPCRWe_4-KF9x_eylEg06V89EH66IHqOyJFDFVdUvKGUShIQSQBaw9QRoHdf87ejIn61Vwm-Bm8TMI198P_D47BYhWWPsc8Go_DDNOm-qUe_6mrau1kxpLPe4s-upnao5gJNb5WPKujhg32nSpPp-xU3jfM9wWErrRiIYPs31bagLkzScpBqDeCiOrV7YbrJe3HabmX-yAJwGh4oB7lufrvE8Wf90mGedqv01ludCzvqOMcaWoy1UJRIbwB93cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dt8BqK79liCgypU6k5zOiaeJMw9p6KvQ_Cnm_Rc9Om1KdrQA5YvUwr10s0nZ8baj4uADL4OhVoGJX2FHtdAokwk-xjfv-DeZkhkTKr0rUGIgFd1u9mFTt37dwYBGbhMTIwqFugwm3Thqe8YCYIEdj3vpGQ4OxNFnUskEVQ4p_vKAjXRFvT72F4LIFDN0WBGESdtCc3qke0jjtc-TRmtBvVHtU1EXnJQBkI8LTnleFEwKR4fWay8Pmm7aeJACVANdzDRajKDYg6bDINyb5SQQYJGCxUCXwqO1rOVAR7C8DvFlJlGZednBh7ZNmeghXM1WmXJVB5WNX2QI9_8u4yBRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCiPVlp1x0EEPyGD4hZNdMvGfb0wvWX0aCXQnELUw6ZjHwD2AeVyD4OyLLZ_x-lr16IpLuDJDhH-svo7BWSoC_7l9bl3DiG-L3RxS7RYGc5y7wu1O81qVperPXgSDdAnxDe3WQgjuKGjClm-n-6Urxp3hTO0gzFzUoAF7ZVjw19DKQ_UKJuHg_jxvsYz9XhULbCgWhFM4XsVHurhj4E9yk_L9NMRr4iMFkYfrcafbzyoHfqVX_EMVfYmXCMoUIdVT692kdbTWxxvRa6xPanEZtEOYqorfpTd6CEw-qvfLNA1YSznYbtwQEDPeF5JpDv4qvL8PqHjQPNnEypk7KQokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgotP94FU2es5NuScyeaG0PSs_5VpqTHnrESJn7LQ9_JdwT8k7svxwu8VpcewHES7bgGCSujC7YREoSW4i6Iq6zSxFQYtJVfj_xPcdgrvZrBYIhVJHQqdXT4VhoJGBMGNDpIBbZClVJvbWO1VmQWLPEAf_1_ceMO4yQYab6IUWbZEbeTSGI0VUj_gtz1phBWCl3JZ3hZVsAv4l5meIEi-cPSGEBO5LIqTOxsZ0QtT4mGtqdNkQOtheZ4Jbh4UcLPEF0qIMzdgRn_XDEnQlo-mrQWBMW37wc4sfQZMuBkRVL38Hk0Ru6CLGoXPt6i6Ch1fxr8JRqHRh3WvIKlVIibSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1sM7mUPT-8tdL9EteftmvH0beN82pLhDVqMA1tU2fbF97rg-cxgwRGlpq8kApJxzxM3nuia-qzYjyGZsUSUw47NU_hJKuW6zWnATLPl4i2kzDesNgbaQa1YxFIv1W7nRU7Kocbj_IgFCyWJRxfcAp3oLrniP9GRrbwWW8Cs2YfuESl8sWyhYcvl0bGWXHT7v3J9PYXgytoXus4Kk3yaJ0eGfhPhHzUZsGdOasMcfynnN-j8KWJvFMHaAOFl3iMZ8q946HYUB6_Q2NvaxO6rKDbHxH5G5BQ84m-7jWU_0rFgK4qq0-igW4DI3-pWuPSXT3Q5dvbDOXsk2ohxhqxRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=bBdNveu9r0HxNkXutUtVeGQ_aWioAGmNvoSOGHdQtk8IfnrMeZj3UvAKkLefDiBbvf0xu3bJESWO-CO8wunuOznEXEPR_22JH4lZ9xnNwFiM7NxfGREjaTzt-HBq3ojqWUO7CeNcMlrHFZBWj6bDSpytXPSBCHTYklKgCbhccgZCCdxK2d_3k56ECj9pd2vkXgqIFUA1DsK5Sw5bfdeNR8fij81eHO6zuT2_VdQt8w5i4WvWcBrpZ51hv7TlMak1GH_P5-vM9H_4jw77EjbfD21c90yO4gXClZeKP0ykpub6N6WgvRnmeKpLPJukJ1rdCrKuV13x7ihYDWuP3dV7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=bBdNveu9r0HxNkXutUtVeGQ_aWioAGmNvoSOGHdQtk8IfnrMeZj3UvAKkLefDiBbvf0xu3bJESWO-CO8wunuOznEXEPR_22JH4lZ9xnNwFiM7NxfGREjaTzt-HBq3ojqWUO7CeNcMlrHFZBWj6bDSpytXPSBCHTYklKgCbhccgZCCdxK2d_3k56ECj9pd2vkXgqIFUA1DsK5Sw5bfdeNR8fij81eHO6zuT2_VdQt8w5i4WvWcBrpZ51hv7TlMak1GH_P5-vM9H_4jw77EjbfD21c90yO4gXClZeKP0ykpub6N6WgvRnmeKpLPJukJ1rdCrKuV13x7ihYDWuP3dV7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPsZcAMf9XdUAJ9DC5bcQnRdE3BV_WJX12eQJAP5voZLbX5yam3VtqpzFnZCvyXchLP0rHjFR-iWDCsANtwrmY_zAaAf0nquEx6ZMFMIXm1FuzVHxOzx1uCCDFKmSgmEoc4kOJ0IXYf637d8L82frKpzTXQu0wzzNGe9zpzRX5iDYaJ0wkVWl9z_YdsARUqs5PLSEgwQtQoa9-20SyetCDhP0xVKPnabi3m51n0-OHWJV1lQuepvLo8JDKXRjx76dk95xBluz2uyLDtbpSZu2wkajRev-mnHbF5XciPTG2l5BekNGrXfWPHJCaP_DjMpVPwffwgI_K7emnhHy3_IgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxuPL5untuVThV4fEkErYnPa2qQeNHpQbEBK3VJYFU-rUGTlGput2VvzFLd0T3hq4semDeA-hv2NQjJyrBBA7MwBW3TtHX51Jke3NAZMfMqEieKLkyeKPfqaCacKq8EdwQ5cWTS6dwNjRyoKapPfdU5ZEKCWk9UL7JL2BnDfs96Vb2fQ0gN4QWDCuBkkabtRzNbTKMaaArLVRQJoDytegFGLWhBWQe0hhuhE1NVExEQoAoxbKA6uQj2XeHMrHi8NOT0LlytKmcUteMcBXguji0XZ4dba5MLk49xCa_NZnFR4lnGClcMe4uhydKjxZI4oTxGjI0kJ-rGqoQYdvukkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=T7s2EJmd2DOshiyyk1nCs6uzx1a2E4ys93aaF6hhM48_olyhSjMwjTdQQXFaXs2kAnx8SuHdL4h9VHrF6BYzx8EktuQYJ1rtA8RE-oi2503aJIAF1zRNPWhPe7yg3_7Uqpwrtf43dMoUaR7O9Q4zxFQPFwk1_3hgIk_5i4_GTZzXqTQWhZTUKVo68uYCX4h4IY47z77DmUPYyXkk_z0rhUyEGDwSb7KnMrTM9DME1qkVmacaqGLYJ9wMaouMApfF7YOUfX2IGs-_bV7pCqHqiyrRX_Yo42lJA7R4YgfN435PR9_dTsvmP2wnNAYKVYuJABchyjrOXEaVxDEoYyiFPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=T7s2EJmd2DOshiyyk1nCs6uzx1a2E4ys93aaF6hhM48_olyhSjMwjTdQQXFaXs2kAnx8SuHdL4h9VHrF6BYzx8EktuQYJ1rtA8RE-oi2503aJIAF1zRNPWhPe7yg3_7Uqpwrtf43dMoUaR7O9Q4zxFQPFwk1_3hgIk_5i4_GTZzXqTQWhZTUKVo68uYCX4h4IY47z77DmUPYyXkk_z0rhUyEGDwSb7KnMrTM9DME1qkVmacaqGLYJ9wMaouMApfF7YOUfX2IGs-_bV7pCqHqiyrRX_Yo42lJA7R4YgfN435PR9_dTsvmP2wnNAYKVYuJABchyjrOXEaVxDEoYyiFPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiJQ67EuJqasRjnxXwQMiSNbMiCeYE9xrr-qEPWKNqm4gU_57IgIMsJNXPeuDtvZuBmGbIF5vPeeu46bUa-sFKnWtQytWmU7ckKpT8p9oOrXuD4Z85EDunIsCwO8OMnBzlOuEo0NRgoynG2ZnnCYj9lELXympvrKkvxhV0gPyg8y54_8QMLon0CxD-C2R-lCtucsmi2NXHUsTedhcFs9MjW2nNcC6oGT5ANG3cBSztc21YOHmfIciXWB6Shbi43kVg3OBVuxndn9-6X2_vLCOKqxoImkZiTKe7NmKW38e3XsVR3jfEkEwmetcNkeSR69dbLe5aYX3wv-xDkTCdFN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxAzXM809IC0hNDnBF-XhjChE9TGeQUxqUQZ0T-VOKwjtmZqXgktn7jZVkXKhgeSJaIzw-YuwYLQzbNay4-7NTHLb7F2m2TSHbPSfuKemf7GtgIQ8iKoThOUFi0gg6_zpp7agy1xB9bH0_d0HWEvU0GW4LqWNI9H5M1QMPT7W9gbvXTvtOqu3Td0K7nlh3lVLzPIyq-P4SSxi3dsWEVBhABPHzjVP-IcBMOm9ioIV1A-AZN-LdJpixmG_2Byl0ZzqgsOljZjGTcOxdmDkbGwzO7IPspZ1pEKSvv2ZKZKJSLJaNvuX9zN-7AA9FIgNWseIjM1LAa-s5qerAkFKEHa7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohni981XojYPHYjdgQfGdz1xPCdI72ypRkYu-zp7EJMxRqsQiBbZPapxYMGdTDI_qjs6wJk1C0en11sB-fLWD4NzJgKVI_THogxsHPWfvQ48JbkyFfsPi-GyC1WY1_D_dRO1n3tVKw-zFtNIu2shfSztkmuOss9tPv299AqoVQhDaAI3uwlZTi2SP1MSgmBxWKCt10u9eoDWMpUIpkDo82gn8o7VHJaiKmtn88AXIeQKqAIeZOHsUzOv041ig82o0OB4sn_FSVHwYkgeRic7zLmt99Ie6zfntxXTIXNF6wmaOM6TPpifQAa89oYRYdIA7PrIw_j3v8-tz_CmKMDXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1gmCGBoGreG9nPzffzJVTISpBIWtwxRfF8z1Chy_gkyvuCAtKLtNTIAfLfXH0Qv5j9SEfKsEQ6QPiMpPCsLYVZSNZZ5FSIc31NnCT807hR9HqsAj3sed80cFGT10yQAEbTS9xDpaq7yxkC2Qy7_lAi_yY6BMPbQw0eo5575QtyC8zer0MFaij0b69REQtXWkN7zZqTAZrk79xB0rp23i9qJJouvuzp-3-MH6JIBodr2zHSI4ArYVLJwhAyXK46yhu7c8gTdu34P7aQa1os-5Wz8ayWNXP5HGnhaOvtblVQUZBW27vRR-NPj0XQm5XJmDcadaBGjLg21nKP580M0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=EE-odF1JO7kCNyqaBroH10gT3NJ_EJBTxGT73xKQLcuyFzxOuQ9X04IhImI1kcPeZULyI6VMDwtcopEF2EmwgZxwFQnttZHKH_m6tSK6h2K4TPMFgx-oDEKnZEy3rl0euKWxaSTK0bYkcobe--mOQct67ZSgZmMLuw5Gnr4JY1eFKtqN6qA9fUmy_BbrFO2STGDtACxYy7H8rRq4QOoEtYxUZZnh-tqF_4_oNLncr7LIkel1dzzAlXSxa1pAgpPhF_Mw0b8Oz139ph7CHZXynXijKcIyhNbdySxrXOsFzvSW3xR9p-iYpoSG-Uk25NofsKDXE2sWjSOfFpgUzvMCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=EE-odF1JO7kCNyqaBroH10gT3NJ_EJBTxGT73xKQLcuyFzxOuQ9X04IhImI1kcPeZULyI6VMDwtcopEF2EmwgZxwFQnttZHKH_m6tSK6h2K4TPMFgx-oDEKnZEy3rl0euKWxaSTK0bYkcobe--mOQct67ZSgZmMLuw5Gnr4JY1eFKtqN6qA9fUmy_BbrFO2STGDtACxYy7H8rRq4QOoEtYxUZZnh-tqF_4_oNLncr7LIkel1dzzAlXSxa1pAgpPhF_Mw0b8Oz139ph7CHZXynXijKcIyhNbdySxrXOsFzvSW3xR9p-iYpoSG-Uk25NofsKDXE2sWjSOfFpgUzvMCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ota94n19RMgnX9aZSVhPWz15ejENlMzfDf6Y2KIWQ2ZALll_pCAAwb3mAeprAIqCZd5dxUMNcRyGsy-A-VB1qMobcJK_nEwjvROvUeqiQkrkQ49nVXv2aKF9cMTTLVA9PEeK2V7Ok4Yy68cg_d_vyqs9MP0wMFtcHS5fIcfxXsvHm6koSUKg1Ol9cz6apYrJx6Oh1iRxHsnGbih-ww1w7ZnLXKdD-HKjFpUN3SQxg2w7aJMW0AGZup7-FrghMBcXvJJaiKXR8f4zI1SRlTwDwWbeWvPGdTi1OJvw5mI2HjLmgFUMunrKQDJkjQIqR38l0Av-HR5EHXw0YMmfhzdqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8nAaeZtB9S6DwgL5FqKg-AIg39dwhUvuVLJRFUcs44wezlQ8m2jHsdDiBN6vygEd7olfjWCkjJlh6XRq_M2tQvTei7NZ8yDq-IYk5HomrwSZFCG1oUc45ZSxg849d0NTZP_ZIyUJPxE5sD8jz692rZhZvZ1mwY9nRfsPHBSb3JJIm3i00Oid5e3WsXDJ3Y57ccqlRwY7HDVZl-DP1DNuCKDH5JXD43cR03uqRiXsG8tghLnhazhbmEAQgj9SUyQ8ziVAkmtJEZobthuQVQO-KrIZfpGVa5ozcjYijRdx6epkx0WmRftWxQmTeiQsRFTaIngN0wQZmcn1fQ45wsFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prfYsq8owWwHD5zJAvNoRPXeC8_vBAvqVoOS6hiWc8_bAd-06hMdisyu8fYM7qyTDG5u2ckQdnkUtrV1x0-xA4s5wZ9pasTW8Xc_XARZNkOWgOZ3r3AZ7jpNSbr8gOY8G4TenXqPM4T8ETmuCdYeORqxj8_6vilDsHeSfe8lrPE_iULXEuqcPGf7LM_6KvO8KB06ai0o7wbAA6siaS3j8YaooAOmBRVuHN6rwkpSHf0uB1tzP3RPk859zJKSHJ5qZ4j-8XRRxN6QoOtbZhQiSOLFP2mLuWvkazEayyBlJhblQsBwySPzqPs0_NCzwrwyUZVEHPX-VoxDbaaWNH7ZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdxhoiP7UJbQWRTDwKN2GE_YDw5isWbu3dWEn0HTSxRN1GQPxf4E0bT-ftfx_0DYF3KsJ5Cru8_qDrb13AgeN5jreBs9_eHnnk4iOcRqgWxbGed2s4Z13rhBU3RX7TGx1ZKJ4dM5gnV1FbtPvwVgsU_lfAON2kpTzN2tPRnt3khph8zlv0mhTx4J6KuV5cxXr1H-6oYajUqwpWuPY-mln6TCRcJLeOHb7WstpLdINvb1X4x72bm6qW4qbK60xjoM_dNQbuaWos_VcqXh0tWSevBO2zYVkMhnuR7LZIPbOC2lpKPc_ks4N4qy1pJiNyUWmoiMAai5M9GoSqxcUfeT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulya4GifgWHXpXJCOqf5ayDV6EalekUUd88NL7ckS-CiBQYGqQoZv4IW_ol72i8OaxsVzxqshu2X1pKYZe4ze8k8YNVTs827ueN7XevyrRWGFah30T9IxOIsUi80m7vZfDSXlzCwo4gxVZXJ9sutoErfmp20VtrXmb03XhYg7Ez9R7NFlQ6xiG3NsQjrGmPcPeNymaX6tObtex8SvLyoYcD64ji4Xn9I2px75Xk91CRyAExvNhFStHBufjZ3OdUpJXKZrwW3Vj4LP-UaY_CA8YikAt056K13PY59t5QNdIO6sN1p5jK8FsZQcGrPxrEpE3CWS_5PcFD1ZEalRUFWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNDimZBJlaRAJEkl7xKpwntjLH_pzuZYCl-PrMFDvuf6kqqjmaMddqdas5jmn-Vyn6HCgfzRFfeQQkuXSi0zg8n5UkwVjHMS8bNAkacsdyWvN26XpVJEqYilUF0M7b-aY5-lE7Xan6BM4uqj04vLK1E-wotccyJVGJ2BHJRoLrzeoYuFjyZQTdipCjzxSOzB3A-4q6-WrAvvaTdcnujizwhlb0Fi4fYgz8Q9lg6d9YwISkdimTpVXrQ0LvqAhGDhVRZF-Sla8DE8_KIX9UAGXz0Mmmu3MOjNcZWKfxPvQ2Si7YcbQnjpx9cIo0N1-b0ARwmRVoMUB2stNlyO2OYC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF7XJBYZJPhZfcptto4Lt4lqov9Df845gsHyVry8ZAXNwlo71qL69I807Rx61iccfdXxj3DEGW0ibhI6GoAHsyCuKCXYchivjJOX2ZP6r44ukNOxTNzh5kCvNiryAB6dQ75Ck3XAirzuqTRlV980-4e-jSjHx9GV6QC0htaDj1En-NH4bmJvezhhWkN2CiXaIUgv113Bn4_JBWrORuSzTa51AteJ84CIQ0i6y7AvkLpui9ufSDmFfWJa79PL-gjdbRMXpU-MY_j0YRb8J4x3IS6ZWP_M_UZv3u2XFjaMxAf9z7ryR8wAgXNQs8_xcXGv-gSdkz4FA3pFywvmRtBqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niGyUbpZNNW7l4Lh1Akjk0EplycUznwYYrkXCUGxjpyN-h0FPPVmnsPAiwhNYnwgIOHPHgvvue5zVbce_POVSk9r7m0KRkQjUe1CLI74oNxZzVJJpg4oj8SIYEEy0SDImoalYJFR9K7xQS-8sMstpXK_RPdXy9r4DBQCDEj2e5dvMFO8oaZwfNY-52gcAU_ZCrsBWqSOBWnv_kqGa-F4oHtis0r45lXDd7l6ecw7IjdT71fISOYZk3kET41jQemJFLnI5lsuwAvp5dUEwI2SKnBUteXQAGUBGqHDiOdUpIWmqY9GZgvzs1OyGnVqW17Dpx_RJ9EzYJAXJcVH1Poe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDONJdeqe6nG8FrO5hzRQCH8wvpUPffXHj0vAITW65wvUws7U8LWRWbfHRZtzer1tVU-UdFXbWUCjWgR8s5W_ryK2hZtxe8mkdcqNxqLqlLfxn0N-xUlN_DCSbSVLm6HvR6W0oHzdALxaLX0wgOFYj4aQb6rdG6V871pzxH-eCPyOYIoFrlC5PBmm9afA3o5QEGK6ZHnvblT2l33ic4_seBc498x9kn6zGKnREVgNL-LnMlifQ_3aPCcQJDWS6uL3DQcZMpjE47yklShjI2Ppt7rT-UNvANPNqU3UlHWheylFVe_6IXHJkpmNtRpM9o9MMuXIEj34aSdRHTlIFxApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG_FUuXVYrn4zdrJMxGACdzXYnkaYdmKIWmL3TYuAPQRbPJsylvMNvoSi_DtSUgDX-bny9_s_frkDCt93a5N96ZEHQiQfY41zDiMbToYEukoXhHQybwVCLchUSjqGWz9fYhDgpzOzTaEioaOLtHcKfIeMbBkyO_Sr0hJTAO92IdfLGu1NpzV8Oigxw_h1bqOx6Jx59YijFLXV8N4vrwVCk8p3_HJjHiC2pjSGwASDae0B6laS-nyyh3Wh1KSMN4tGVmffwr9m35xzReA-8OEE-fZXNeMyRWTSpEsojb4lzaTzzHsZwA_6j1aiz1VSUauIqhW343tvbp537HZmSvqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scXgZ-sBm4OU6DBoIw683uy_LG2U2D28dZLmnrht46QZkWAHRbJNMURhG7O-AM7gh_Ib3DVHGz8S50yHSfsFoiOjizx6bCgS0tPYWbswp3IqqkrB4mlcCE_pq_N37ZLUD2WMl1XLIs-iOvJgtV7eYKV_lO-mlMcXTMDGvsGckYw6Ol81EGnfcXCvfY6-DcGjj4YLjBTcX64QMdLtWZPD9ghvEFQYhUtyzgbFxaworO9VViJM4xbv3Cd3HC5bk6q4zi0Ebq_VMm7oLqzYyzHaWBMK9_H0opjYORQTPhDv3yiGvkvAJPhl26SVhPM8jlgoFM15ZqBRvHyK-vCIFlh0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjygX8AEia4NbDCqPhHml-KHdMAR1RpIN3Bvb8YcfKDXtYH-x20cOFoYl4URVOnImw0MhFDL_t65WmbuKHX6sefyzddp4ei7GCxHrmScZP24E2gIe4hbGJNhbNRsIkJCQWmIOWpR5i78pgGG3g6MfrRXBo4Kh_Vt39gvXQk9EefZxK_55_Wt63kJNOga2G4FTjaFX0kLhjVhjNhnrRbPrF7GZthqvtvwhCdeSd1J8GgfPqzhCT6A7TYjrHksqufyO8V39do57__DO6wI7z5a-vD1D8707tXg6POW4AguOZQZ2xFR5iOLvilEyz4K9LwKPObW_8kK8UxvW4cc_53u2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1wR-DkPB4QbJhB09KvMGnsx-90tKwer0g30ZhezCwaTj3s5pJZLsnxJhCKYOFQ50K2405bK6riFL14-jxOF4ydtEyn3o_W1uPo-MVyH8UEL3fjKLZ9T0GgcFRpHz0Q1FpGkdwaRyUxnQrqUqIOghFmM6ZQUxYs_At72bwUlBEu0KYOtSqabadaQDng1Hs-r_nOWi0ejmF7Ctt4lDOwDdPa97eC2yDSED_2XOPapPWqlD5R8HXcS1gf5JFPVnfBz1nb-YlYsG3af77T2JiJT7HOoNsrG3d2BJqDImV4Dyyp5Z-ZfGzZ28niXoX5EztfdZFnyv5_Ky7Rj9hZSwuVMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrAhS7f92LYjzCd3Zca_1NVLlucV6KLAa3nlU2o-G4JNstTAKdwbUYK-aMpSbwKd9BR6gJ-PAfZJtNzHlkDHXuIK08d8DqntWAy4wVUZVFo7C9rtl4q4kDw2fO5geLyj0T-TD9pW0QYvmrDs1rywFarSM8BUNtmEtBVNphsRdcUN0pqGmAfHIiWg5sKOe_nU0MAXqL7LztDLuTtpHlb4dJ2fGCBYIRsMK84KKijD_SlBjbi16bcFCTOvuV3TbNgyvq8elLe_4KkoLuHYMH98Pp9HDxJ4ZKNLJjWGrQMJV802yg1q2RbHJFF-lXDYvlwqRKhe4xpYPhWUhE9ZemwyBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euVK3pdFsxOGx84Q05vGDKSvisVEKMrUJi3K3CfxG2XuU5Rkb-2tdLfhh7l8oRg8y_RljxRzcViBi5SGmS3RrhPlC-CVGcKSGiZDVA8Xek1eO7G7Dpvmpo7aXZKrFTMNXObwnOwVmMjaF9BjlvNBYGfM31S_ZfERaoHE80rlUdTNoF7pCRNtLib6WnhwC_-A5_YqcbcBAROFBg6B9zxWb1hvBTb3ZrSfvp80MxZznVsZgU7gXQr-5MjXPOA3r0ScZQJSWdZNQdHm4OL936aeDTalKHoDTQeDBb9uL6XRj6oWes4c3xC-Tk030C0Lxlwv7AfELh7N1HdOnwnmgVyyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS6e3TjXNH0NR6OOgBrbxPZvVgnmmoCKb8sKE2pateLEs30lv66xHd0vLWeyPyuZVCqKgwOY_jXI472khl-Q98XS9i0EpCYjYCXlSeNz6hTPu3ARRNzQUqWjuOVkFNt0ecgUTky-vlwZm01M5CmEhE5h0cjyGrwWsf2dCXO6kXl8GuZJ_7qbjsVK65beeJubj6LMgrKVRUBBbUCuiExFu-o7RapyF9YVSziMpVGL0DGpWAqJ04m62K9WYMVa8HKlXdZx3NXYff_yo3vDdCRlaUxbMLnrukx8azTkPH4uu4d_IJtyW3AMd-9tkNFt3CHePbUkuuX4CMd4WN7hsCiGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-rXWm4yJuKcuSrBYzbWGPGAlJOshaboEwtioJL2Ejf4x34re5o2Fsov_y-OFiHF-VQkw941vyJaGwnupFbJLas-1JeSYMUlvt_7TOnd3m1t58g4CflE_WUlX7LVuZ4U5ifRDArorWPUCZm6qmHJ7ZoSUj-i4qJg6X4Xr0r_o2ABpq8N38EbiBT8m56hGMQjw0vk-PdQVl3dyvHNfkDnlmuWPpMnPhuUTwz1L-suJk7ogyrxVRrSMMtKF77zbRHutMyKSRqWX0WYVgCc0Swh1XkzPZiwKxIQZ7tMyAZM-n0wRjBW2BcQqu79woxNEjvSPrfJpkwJxdfnDra7aeE9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuuZl3uSwm7LU3L40O8IIOgLxP8oQ9Vd23AIM0taJWab5rahPieHytC2QrI6B6ftZQ-z0NijGEwA0fUj41eEJidBcsMdHv9p_Z6cx3O09e7Yl5pQLkp1dylkMmZ6ymIZPn-C2-rUsufI4N-Y3zZpGTK2rQNJIpuHKjGC6zLfg6bt-gpDS20dy_J0xLf7wSOazzIBOzO1IhgLolFk2FuAAmbe9XxCJ4Vc-KbagUAIODWeyxQbcJho5bYh1mqXZDqhfxJNSnAiqwX6YQTw9_WAL45AGsg6KvJgz9l6y_10sUEEudTNviYACVRV8uKPbDPLysNLqucUkSW-uRTliCyq-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpIcniau9e0aOerrEKioCuZMnUBpLiyxVj-2D0jiqY2aTI1QrHuejeXJRx7RRI0zyEyp0KfuC2sTYjReeYVnYQyCtlxncrhMQulAYweOZjbF-mA_QXIqf2S1QARPIY-oKUXe3RAx18ABUmaFyT2oiev4sDur7Y7Pn5gaf8pnleWXY1C1djszSH19pRsfFJM61i9CqUBm5t9GRJ2InXWBwn1xtcUhOKgFJ90Vp2BE2w_i-5atKUfkERd5729SotuQZattgHwg34ORvrlZr1VLXHS6Vqt9zg6CzqWXIHjOTJ08LAx2Lvfm3CnUpI2i4VXHzx16QD_VS9i1zACz0WkwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKuG8xWOhc3hu_se9DKC0ihW4b9AAw9o-RpAjLWkYx6bWENnrxEjk5PpX5sz9YgUjjHLKxSM2l8c9KIYdPs8Fbvjq8uVMyu2UaWyWZIFDDcbH6gpBqgRhhSR5OtF91SgcKIzihuI97MSg8vdimDvTU9CkUlpmxKaWVIL0aAGXPqaID-1Eo2GvsN6m2QyGI3-m9ojTCccSEqfsEb_UfhJv490Wx3UY5BemewJLiPxOh4Lxid5EPL6jZ9Zf6uC6rfPaBZAEHOfPsoRdTQjh7nd_iazDsN4r_c2A-6ZrGJ-57FaxtY-Ape2ojX37X0O72wjLh9TshNKLE941-j1rPxvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALgjVwR6XYcoDYQjFJeTaOVh7atZuygl7aRji1u6RflCOfcA8MpzSgdc96g4oqaMBz-2HcdFOnBOXrfDW0aCQl0ABpTEBnA_uJVpriFat0xTTG9znK3U3BH9iKuLrJN2cOIKgKyONQtjcx0bL__JF3FXfugp7A35clSbxgFFu-4w4huOuYF9Wh1cmnhEGmEEdR9vAmr28SNp3GbcZRpcwgo7yzKGugB77PAPNAZBp4ZRD9ZZlSiS2WvX-PKckiS21awo4EA0uM-RD-ct2j1zXw5L2ot5F6OUr1rna3VDbTnKdTK6dRyAV9t6O72PsJFhg5ZqpFY53jugYIBqFgX9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2ScmUNm1CLvGYNDXOEhwCTZg_cou8QHFdagFSqnYbgjf5oIeWjB5hl728921bh_aVwfsJA7qyJknLuU-Wpfuuc1McN1Mge591hQ0SRx4kpIQB-mcluyOPCTV22o9R8wEUYvo2E0YmqCtUktMwct-swbmv9URW2ptmPqE6WAl1gwJE0xWybAPUeLvUQpIguc_NQC82n6cGrmYWd77avrGtZPUgzM1AUmuZZotZE1C6JatW9vyH2K6fiu2NL8bNBh27ZwZF-hoyxQSlTnvaNvT_sFE1CXOXxy_pCKUTSU7RocZHUQXpZWg7BumLj63h0NibzD0oFLXF8DhYm2_3L2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Few2JfYL82owBSCP9NRv1QY4OV7k-6q9iYi_YCVamC4xJsbaoNSWHmavmgViZnEKNe4KGll9TfODMdkKYF5hNJmTsFouUAJKv6oE0VRmrvdlE70rJ31T0VZXzqEaSxSRWMluAOAgbDL2Kt2RegoR54n2WztXsCys1BtA3bBo06UeRG9wSLzjr6O1NZJ9776WCX5BiQ3qBxmUcsxkNMg2BAGrtrQBp2pzePo8tX37FYXMUb5TawZPHh7CRlT5ehWjMreNNhA8WRZpHMhaj8_58EqAvM1GgXj79WfFfuBSLR3UJl3FLWt1BcBu7A9RTuaHB1WGAGzv7qfPNRky1Wb6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XApNhol6WO4o37sbsAgLYpE6Nmp5mbv9u0jZ8tMOvPCjDsts5JzDsvS9fG9dSE4s0WaZSZ7HNGuUC7pfuDxq39fU9iLf9B_2VENC7HZQd76E3uw-9MpaewS4Ggt7PClNS_eNKZwK1_ce5mPtA5httPyuBg2AvgGZPd5FOYXGD1XgrnbGaX8rqpmT8yDC4mrp44-u_1XVToS9m6re8O1f7m2Bh7jLmm-yukZIKsYH0mCzrAd7B9Ad-72UCwzoukC1i6c9OQyX_fFXp82jbCfWdK-g4Tw-k5MP2JfAwzrkkLvISLVKbSC0lDKU0_VUJ1lwdaq6jgkcIbII3acTo0H2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Km8wfzEvMiqjsnDpgYi5H-243xOuTkY3bOiovCi6bquGDP4h6liNJMStzvjMoKPwvbnMLje8pMKmehEU8y75Toi2vs3757lMveQKHih613qf59dwNDpCkVn0NVAWL3hJeFrq5Ax-i8U1OQqQi7Q7TKfIYUdGWE06cX2aBZgGvRwTibKHJhvaAZ7GOhlfdl_ccELaRgV8ehH8Puwd2oH-f0LK-znu1C-4AyW7480nams7FDt_67hZB2rqFTTbYArS4urXBBM0yB3SXDWFYhLVzlYMdABO5AAfjtuXtXji1omy-zmMeks6D_Xho46QxUp3u2B_FrfgV02GTMTP0_bHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOfd-pZlcR1J9_b2IdRHBIG_P1kh7KI9UomYHe30qFxzBW_oESpfbaFDpbaE7qfIke2ZE-aloQDFOBptB9J3GagBkMTVvn_xIAF3vX091u5te704TdU2FSVOLoFcipXr5dAZRMG0kObuUwtYRIu2fcybMQVGFaAmOXyIuv_v9it5FwO42_Zx8U2ME5ZWzG17P_SoG74l_tL2_KmpZaArGAgSQalySrfL6zgaM71qBjnw3bTLFTMl_9_JbrkQ3q87cCyldZR882l5WWhZXYKULMWEQHfH3Jt_V6jrPqYUSa9r0JHz7n1v3ce-_LiiSJthZAkSgquVOifZ_I4fboy6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7OQ-mNs6qgF09HxaJXwCRovBrKFzcMAbJOb0bK5nWW49O9qxpErqrRRnotcdaEdN7A3ZMoT4-_T4PScvhCDYPOUdDOj0nshoZD01hXnBkLcpR9XdcPhkyjPIp5G3_6a5iEfToCnhnL9bBOKBruAFcRsvP3oofe_4ecudA8sgAec2Mskf612Dt27V_hFw3BwBzds5-orlqRelNYxrdpuobypGwlzHUuoI7Cq0-oBxtoFaK5LOQ1HbiZ_YicMA28iN3Uen_g3cDH12-kxgi_Rp0q_ReuHbI82yrawTuhPrvoaBMSMnY0Opki1tBNFd-bcAN_mSDUnkGC5iTY-kq7BfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuBIR4hZO42U9rekSXjsN6iBkAEa-01lKcG2Mc3s83WLnZXddcHKUsw5AkBmLw29uvie3xc-N3v-sR3ejLqOur_yCSbepHwT7hJi1-IohgJdTmfo0Hd7qDgsfyUzTjSK4BQiG5hIgiIZgSU6nNJwyET_NPLyqXU0A31KtaA5kI8MSKwAlDUvx2b26zkKsRU_a2x9xXzs2a7fhq539hBODsz8AGMBUZVpsFh-UIC9YA2ftIeC-G86Q8wKxPVCAvlbW2pSvFB8_6_g8Q8ZCr9gg1IR7Ta7rY2QEau9eZgxuZ3TO1t7E4nGXBNBu_ppPNPvBz9JUZcP_5HznIvOz5Uu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJFoF4iL8BVG8zuxJr36j7skpqGHX34L99SCd0eDEK911uD1Kv9PG-RwJ2t4j-Q3sH-BDL-J7BuTDVAVHIhpFg0GnkrRSNESIAzrgVA5ap4ywZPE9Uiq-TFK2df4yvS6O2C50Wgl5ZW4Yh7xsD899ZJV1i2bzxjBIGQAhfMKHC_n_2MvlAO9vi_P3jF9ojYeKh2C0SBit07pZemBRtUOMMoFzhdDAmtoNFCjznWhofZRyS9HbL0kf2o7cMLJEq3R4QAIivl9YOQsVasBcR8bRz5f0K2vVSOVMYus7URsUHU5w2GwtU12lCu1SZLMRy1YqDCcC9dmuHtQEofqxwnc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv-6ohnINhieAshhsv-OLwmoNY8CxxjIR4rCuWNyzxU_Ukeb02vZ_BIF5M23G3pKGKm0GM3lRmCYEImCx7Yxd562BGwxwxLwdMydHYi-TBNdiKPj9RrJT90IEB_tV9Go1BzE2jOSvCKkXRl5YnJI5Y7dxXUa11BwSc9CVQPrNvBdP_rm5cJATWacPmnF1032v9gZr_Su95av-VHpg_P9_NoejkpTEHW-OWjilvvf8ednkVNtcIaAV0rxMBQHCnge1XkyFIHMUt3jKFsN6Euhfbh-hEptsEv0k9xG9qTF3JnYMDcdEkJ4-_2_qDEh_x6TLc5sncExjypOEZVRmUesng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e20TazoOHMFKbbkVJQQXfj-U9Ap9tw6lao3VoZ7vCU25ggBeigHb6eUMBU30NJEi1sNcCpiTyCYQPFQqBYk5smzFDHWXyPHTXPz32faNB-6wQZGYtObS2R0YC3xVZRlaFcOjh6OnGc5cwytS21dMreP7i5fHnDk7F3XGSjgNI45LkjfZK4itYRcuCryNY4lMnqoeT9tSwjQoJc7d0z5R4MZfE0ibcKJd7pDSkCBtvQZEQN_KfOIUMcdnWDfOIVhIWWmqqC9oGfwi7K1v68ee_-oaB1Hso_anASxCtGxkK5OuAy8ixyf4vj-IAK-2wN5WjteBqvtv2ODnvik8W1R0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/le778lZNg0EV1IS2ksOLetUQwrM3sOXC9csCGsuOoosO9JyV9tfSxggL6U-JduP6tuQ-f1XrwX_GeDcOvVPjCDeciBpMDPnPDnrg5_F3dNFdqpfQymyawSeTjmCYD9tGdLXFW97k_5czV3Jfd5PP63xxj7LfG_I8n4yfyXh-ra3b_IZ4jE2ZFQtqNDlIV9pdvmPYN-GGolMjL_zJyKNsUdHZPq6kD-C0p8ynFZ6dzRUVw29tRwZLQc6hVipIgLM9TjsOTVojBgXT5kB1DaDtVkLVzKFtoANoib7xal44bRP7ln5-tTjXoOOONxcrMsxOGCQeU9wEYnBki7XbKa-LXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-CGHOfA1mWd8F2x2OMTCboVsV1hroCBQgzQO3QbYhC4XNME5gA1t0xg2iduZtrHYtc3vDZNguxL0M44Rr8pnKLlvmBWOIEQUToU37V3HPZWDlNOFFU_uzjepUXOdq8rua44p9e3kAHiOsVvCYgu6kUbCAzme5BvmEulql7hC8wZXZmeNWoI8BYHk8iO_TshROFp6kA4MGgvCmYQiC5MZfi7WqtRkVxkgrt6U0DZUJ-s80J7raWtIa_rLlsLexxLL9ULsaBUHEU_fe5mEqlwz1wssmpGZVukEGfkngdavY7MfYDBqDncZMdZb2EBtN5wBVHOQGqoFWoJIj4ZhJ-p6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbolyIV7qFtc_1pY-OFIgST2L0Fh2CJ3trdhRRt3GCLzYF121kT4TBxF3hXkX50MNWqr9D6pIQuGXiMlbADZ6qiHDSDEXK2ArqNZYpUQwbwSBWUo5-vCTNG0piCQRSKfbgyPX1ktt_r_j7-nMOozvHqKVgmJCRYFRGJN2ttyHAU7V_bnoq1ln8764bQGjnJ3fvOJEzdb2kSg2W7N4sszhJOD8KYTZ60tUSpIKCb9YfHokYesWOVhf-GlolyHhBMsX6Jlvog2tDgFq6NDszNQbS9mpAoKqPNZ7ia6gMj8wdsMsH4pcgKx0ygZpQ7nGJn-UeWgyQh8EwTSZFOiLjBR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jyi56Zk1GWkFJykWWqpK-WQN7MpCrON2gU9oEM92vMNdKzUfXlYRsN-W3HPU9UW4i2tJliYhQzQ9MzoM7U64P2woso33gEFszxaQEp2PZvXHQg1Jvhql6_8eYEfFC4PHXlbooAkALvtXNvKuC0XIjY0VSOnh47NpHPu3piY-YeSkMbkuI7W6XfP2B4id0kQlRbvygtHyU-anttlfWAqjfRPnonu_ZkAWUCkiaJDdmnT7lyGzu2E86Id2PPmRMgduSh9UUVoycSpS2UStha_S8xunN8InA0aUhNH-PGe5p8hBji8mrvjD1hWcL4LFHGS0G-OWaF7rOzqYQeBCedD0IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj_ECaK01CafdPrdL2bBRs_vLxQL_k-2xDU4Rzg8oxQsi9BCSKIWUW5qGAXMWfpySYlfCfnaHy8GKUt4eHjLbV9iewRhNUhTLx67MXqNWT7GBL2Zy9cMisTdoBLVmfSIpSH3qdTeXwnobL9aX9FhpU0L2m889PX_rq1cKeY83fo8qK636eT9LTYtfJVkNhI8KzAeI8BpSp3hBRWZFw8RDtrh0naXQwLNpM5nWSkP7caACnNh9J2ZbbaPqX2gbPHJlTRJf-Vbsd7hpaX8HqP_DC7eaLrRRYsWLqcrEVWyM0fR_2b7pBDtX9alsRU3nQwsOeE5zPmCc4F0unIWhoKSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr_gwqF8_A6eZVwi9J9n9Cb03YfPLSPQwEBTkjXh-BpxCAJ4hZnH34klFaQfsCexFL-YFbapGaaSD-MTSFOc1QwoCBN-6bK2O7QGTZZxG1n_pdseBKu6IyQbNZ9A1wf-5X1xIM9YiQZ5ioEGBdA-RM9hMXuvMieuCOL7WaLZHc9VXy9mVExEQHgs08J6_2k16MFtkIFoIsYLeEzm6mhwf5IPnBv2SgBppO67n8v1F7-ZqjnmocTPDPCUAsiHQGV3tluw-3aIlkDnFngopoC1JIx6UJ8MxtFSjqCaokzusr-pth1pYSqtuUCYmigUvH_Sxry3v4fuCM3JJ2pAoIQj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz5_6aDBlOAkeyk3_CHLMQDsQr0NS2WLALRKrn20rheWS4D7Rw2tMjZWYseSzeXIFIdydNqyaMmRD4fr14LW8ddmjyvx6MpKigCc9uUzSf5h-9vRzRfgJqZgEODffkJnBb4KBs_WvxwEjhXKERt32vnjU7MgUDjGx0uJGC0Gl-YNvY6iVFRdF-Y-RE483UMggBqyfgXINPhb4NUfpikS871xkFg9nedeqXBIxKUsdJkSndlLB9pakEx6DkuT_g03CXYZPjFCnWhv9obbuUAK7ljHUenn0yg_zAql7xCThbQzMfEs5RIinzdooD6u85xKx6C8x_aO0SAnh0aD075zzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
