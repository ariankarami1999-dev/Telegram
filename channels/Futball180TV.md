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
<img src="https://cdn5.telesco.pe/file/EnJBuxfszWoaL-HsYuzSU6FxouckcfnR32clTw_UVdRzcM484bijDWNd2ZDEaZp2RJDQQhVWs5ZfgXOyLQVMzoTUc37SJNRE5iaqIxaqny37-6HSCL8ff_McrZedigrzlwErL1nTS72WFuP1rA1oKn3cmDYQt_5WKQo1819cxEMCyF-enUOxtiK7bglya_EgJKub8oKsfcaKaZOMv5vebAHrUcEX-6HWLoFA-8qQuLYm2yxJmStgT62An13BSy2KurbqFBveMQtdepEqHvuPJGuyFHVliG4O3pmJI5BoYz0AFvVJtyUYPcvf-54wckA-tExxpjOt-XAGCDlR4I7Q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 710K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-95155">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFtNUBRmcPmY2yRuB3jkbf4hvo6aQziwiD430OjAW7os_4by4EoXH65LntqRzBGRB6nAqJ6ngg8FZgQb142xbv-ZptKLD7tJWey3oiFYAqaQbVhZoyidDlU5vThs0uWUoB4OL4281HB0V6M_pGAcpTl-HbM2sxxEnW8D8z9fMKwA8BJNO-vM-WwOsY1ZeTFuzEb2pLC7bXOMLzcN-iuNAtvjz5-4iS_8maIOrLVx-slgUqpKbxtJ8BzkAbsGMDxyVdQ8aTXOck5i3PY8bel5WY8_ZvvyPo516FbVqCncykgCUR_bJzhN--PGrmVm-pgg2Bl8MxsBLqxWZZScfCG9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
تاتنهام در حال آماده سازی پیشنهادی 100 میلیون یورویی برای ساندرو تونالی است
منچسترسیتی، آرسنال و منچستریونایتد نیز برای جذب هافبک ایتالیایی در رقابت هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/95155" target="_blank">📅 10:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95154">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f33346775.mp4?token=Ohg5cBCYFS1Qh7NcCxMmod9nmhNqfOZHm8J785xRqyZGLXVHJwHQ65SUc7_kmOGrdpETlhCHkh9lQPxzE0wt4CXRk_eZJftyi__rzOYRPHfK-59O0h64TOyULSbJ2dO8JgiQ9g3QWiNc5biQNKEm8yQ0_H3aSYDTE0cD8wE7ljKLImQCUN9sMr2J9c8zukASb9JKadHjimfokdA9e9OdMUmFryhSPhn7lg1fMo57LKxT9L1-9o_fL_3lLPgKPlWUS1Ghhuq1FAAtssBiX7n1LDXylDcPekf66LS8cacgFZ2ueJj-foyipYJT2QXJBu-22cmT-fn913a75zuvd-dsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f33346775.mp4?token=Ohg5cBCYFS1Qh7NcCxMmod9nmhNqfOZHm8J785xRqyZGLXVHJwHQ65SUc7_kmOGrdpETlhCHkh9lQPxzE0wt4CXRk_eZJftyi__rzOYRPHfK-59O0h64TOyULSbJ2dO8JgiQ9g3QWiNc5biQNKEm8yQ0_H3aSYDTE0cD8wE7ljKLImQCUN9sMr2J9c8zukASb9JKadHjimfokdA9e9OdMUmFryhSPhn7lg1fMo57LKxT9L1-9o_fL_3lLPgKPlWUS1Ghhuq1FAAtssBiX7n1LDXylDcPekf66LS8cacgFZ2ueJj-foyipYJT2QXJBu-22cmT-fn913a75zuvd-dsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
امباپه:
«از وقتی فوتبال رو شروع کردم، هر دوره بهمون می‌گفتن باید از یه روشی کپی‌برداری کنیم؛ یه زمان بازی مالکانه بارسلونا، یه زمان خط حمله سه نفره رئال مادرید، یه دوره هم شدت و قدرت بازی بایرن مونیخ، و حالا هم ازمون می‌خوان مثل پرس شدید پاریس سن ژرمن بازی کنیم، پس تیمی که میبره، همیشه الگوی واسه کل دنیای فوتبال میشه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/95154" target="_blank">📅 10:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95153">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8977a43dd2.mp4?token=FNJq0nIBbp4c5oKlK_b2pBA1rjyFh-T5DGoaTlUsaqYJch-3r6qVyxxctl2QLd5cZrajhF9zYZ0myLwyWtdfFJXzgBmxmSOxjA1W62RtykjP4B3gTvEV56knuiP9g20KUwtBOWjFOyt8lIq0lsrtqGw4VobHIGPs3wdpsWFwoDoq9xT3DLhgKy_YyfwEBvcSMO2-5-mBPJvIeWYHdJrtnGH5M2Bhg7rGUpHDvikuux-e3NAjE1RxglBbcXfcVu09WPToKiS3l3jDOAUGFWc8kCgY5rkHjS1TTlqrzagWtEih4Jj29vS3AGYiVnBEmPd4KyDORbO5tcuvPD8xp6M0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8977a43dd2.mp4?token=FNJq0nIBbp4c5oKlK_b2pBA1rjyFh-T5DGoaTlUsaqYJch-3r6qVyxxctl2QLd5cZrajhF9zYZ0myLwyWtdfFJXzgBmxmSOxjA1W62RtykjP4B3gTvEV56knuiP9g20KUwtBOWjFOyt8lIq0lsrtqGw4VobHIGPs3wdpsWFwoDoq9xT3DLhgKy_YyfwEBvcSMO2-5-mBPJvIeWYHdJrtnGH5M2Bhg7rGUpHDvikuux-e3NAjE1RxglBbcXfcVu09WPToKiS3l3jDOAUGFWc8kCgY5rkHjS1TTlqrzagWtEih4Jj29vS3AGYiVnBEmPd4KyDORbO5tcuvPD8xp6M0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
شوخی‌های جنسی دو مجری خانوم با نیمار در ویژه برنامه جام‌جهانی یکی از پلتفرم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/95153" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f153f9102b.mp4?token=g4Wf5ne0hDe9c5Fm-bJyCHG6UxiLARsLqvBYv64B95KBqlMy8za8ujd-Y5KTeF9zzgEh63vFHFCaVlCl4cS7j3jswOoCXrMiGdYaujwMsjN7NV8N2tujshwrS5HncRwWAMs7ngOcfYBfQ0YaOvsUb6PLQZmrwYBgc1NgncTUeudJHK9W_GDXPZqW1oGBQpaf087emJsskXeFotqRU-iJTIuHfAha7_V53-CrRWb2Jbd3_J10Dx4XHccUC4AeoaHkCe2x7sGsGzkTnBGyUYj-YBzU7U1Ap4X0qqyq4C7GvIPuKqUYMZ7Q5yq86nzlzMJBbuoMI0z1lZAFbsvQaIk2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f153f9102b.mp4?token=g4Wf5ne0hDe9c5Fm-bJyCHG6UxiLARsLqvBYv64B95KBqlMy8za8ujd-Y5KTeF9zzgEh63vFHFCaVlCl4cS7j3jswOoCXrMiGdYaujwMsjN7NV8N2tujshwrS5HncRwWAMs7ngOcfYBfQ0YaOvsUb6PLQZmrwYBgc1NgncTUeudJHK9W_GDXPZqW1oGBQpaf087emJsskXeFotqRU-iJTIuHfAha7_V53-CrRWb2Jbd3_J10Dx4XHccUC4AeoaHkCe2x7sGsGzkTnBGyUYj-YBzU7U1Ap4X0qqyq4C7GvIPuKqUYMZ7Q5yq86nzlzMJBbuoMI0z1lZAFbsvQaIk2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇲🇽
مکزیکی‌ها دیگه خیلی تو جام‌جهانی راحت شدن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/95152" target="_blank">📅 10:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226f9c8160.mp4?token=mvojblzs_5wvlAL7y2t5EZlamd_0nROdxexY8Brk6gD8Lat6MMtuKXIdGQOlpbDfE6s-UaZ83rAT8AdunPzybsT_nqXfhQhz-5FY-iw91TpM74XkLmM5qnxTEf0y1d2KsXc24QJiY5Jepep6q8Lp5BXnMZofU4NAcYlmIdbRXPh0cIsDaY2khXxyrtPGaNUv6FUizzUzFMqCJV-7E-qolaMpjEB2yT9-lnGlTSDeM2RyUWD16wfwPcMNkrvkL8UbZ6MdS4exuUNom_tS_njYVnk93Mm8zyWKMwQw-O1mTRZUySOHM_8p0CGZ14rMpugrMsXpzayRucsk-zf1X6moDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226f9c8160.mp4?token=mvojblzs_5wvlAL7y2t5EZlamd_0nROdxexY8Brk6gD8Lat6MMtuKXIdGQOlpbDfE6s-UaZ83rAT8AdunPzybsT_nqXfhQhz-5FY-iw91TpM74XkLmM5qnxTEf0y1d2KsXc24QJiY5Jepep6q8Lp5BXnMZofU4NAcYlmIdbRXPh0cIsDaY2khXxyrtPGaNUv6FUizzUzFMqCJV-7E-qolaMpjEB2yT9-lnGlTSDeM2RyUWD16wfwPcMNkrvkL8UbZ6MdS4exuUNom_tS_njYVnk93Mm8zyWKMwQw-O1mTRZUySOHM_8p0CGZ14rMpugrMsXpzayRucsk-zf1X6moDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🏆
هوادار ژاپنی بعد گلبارون تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/95151" target="_blank">📅 09:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpNuZMaiNJO-Lt_ym3YyGaQ6ot4VolpCBygZtF8tgPbWYBCv0fQq5ZCZcHF1-tDVTofcLZtbdoW2VZvrKdnA7p5BghUrTRZK0jvBRQVrY4dgfqegQm5NSNv60t_JbMp-dhVyITWomoYYAgcmO7Wspz5fxyK8qes9DcZZr6oWV4Zjb_PEhpOdQOVNGQl5xM4H-ofx1e7x7jmFQWgl7aDNv5kpcBqpeNagWEZhd0xdBzi85u1U2WEeg1EtZ4380a3vKdMUIXTbjE-YkzN3_IFgkMJbbNrAaDSZm8Vap_wlzOtNfGeSL9umnXg45Iwcp0ZNzcXBp8Rt_Yg91PIOneyt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
پیمان‌معادی دیشب در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/95150" target="_blank">📅 09:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95148">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqtNT5CB90Mstxl0P9JF5Uf68H296Zt_0cRk3aBAOIXBy_xag2EXTzFLxP3BwmaqpUkqJyUZEv0hl7RROQD6PYEk-emSvJNTLcEI6i54ZnkAUBalEyBSD-q1vv4MPf1UyJY_9_63YiA8WY4WQFYWwEw4dVHEagz5hH06QEwtcBRLB5OUedGk9ooKxzANw8LPjBg8JZL_BLLZXaAXOU_OrFkj6PPVD_Hjh0H_tgC_O4xi1FqueImpRvTwkur-RhTjiuzU2wWEyStKjHNUb-BODnJxUqWU93AMvmgXR8W7i1TWqYRd1ZHBfsu7sjyKzEBhAswX4RmWdVTBfUCBRc8EZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👻
به امید صعود تیم مردمی سوئد
🔥
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95148" target="_blank">📅 09:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95147">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3243a4ebbc.mp4?token=J3GiaS-Vqp3vH-veZMik16ldpaImVI60xaMBJJ4LHGMpYboDlK4slU8K0mZKQ_svBejLCHlPpwQUuMgKaoWxhZcpd8gj7hIQeIVMZblUwmIN1Pp_QaoKZp3RndjrfeLRjw2p7m55D5qiBHgv8YZbL8U4CYpJIu2A26Ex21f22AlxtvycVyaoi1J-duPNZHwoo_fvu0zhWx_FvAEXuzfmn45QTh9TPUBM05-IntDQTIQ7rl1IxRpom8uC_67C-iBoAzkXUh9vjjGKHRzKJYz10xZYJu3DHhxDBZCBEO04V4oVgmqWO4Lke18xjgy-eN1YG2TdrszFtyOZ_5EKEUmVpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3243a4ebbc.mp4?token=J3GiaS-Vqp3vH-veZMik16ldpaImVI60xaMBJJ4LHGMpYboDlK4slU8K0mZKQ_svBejLCHlPpwQUuMgKaoWxhZcpd8gj7hIQeIVMZblUwmIN1Pp_QaoKZp3RndjrfeLRjw2p7m55D5qiBHgv8YZbL8U4CYpJIu2A26Ex21f22AlxtvycVyaoi1J-duPNZHwoo_fvu0zhWx_FvAEXuzfmn45QTh9TPUBM05-IntDQTIQ7rl1IxRpom8uC_67C-iBoAzkXUh9vjjGKHRzKJYz10xZYJu3DHhxDBZCBEO04V4oVgmqWO4Lke18xjgy-eN1YG2TdrszFtyOZ_5EKEUmVpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
واکنش صادقانه یه هوادار به بازی دیشب:
❌
❌
❌
❌
❌
صدا کمممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95147" target="_blank">📅 08:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU0IUhZz_dgOhPhB0rTERInTkxMQYrA-SLVxSUwOTIchvSAhG72HImVwyZwHIT6dM5C6Fh0dbxq-PYDG9QZpNGIApqdcJzZiN9Vspkk69gIHWjIIBQ38SRflmtzDdANZMTgDQTvMPmOstFtnDnia2jO8d3vpeK7rWpjms1NGjm-mQQc7REMudPKcTUwAvgVVXTDXtaT1-IIoA-34Qq0qIe6avrDGNWIhMzClAqGMUweZ8HttAdPFD4ftclhwtnCBcHNjMLfZxBVDu7YXnGJE8EC2RwplHhKqIf0o3BnZiYaMbzbSy53N5DtwxjKv4PE_qFfnScEfjiBk9w5IOzNK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇳🇿
🏆
🇪🇬
اسطوره‌صلاح بهترین بازیکن دیدار مصر و نیوزیلند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95146" target="_blank">📅 06:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSK3-_9nXgdV13ewn5q7tCRbtzdzUJTALpFJEVr-bk_rE27JvoPqYWqMVJZxnkLQjTx3DVvFbP4wlUUABYRqxYm6SXnJUBdPembn8gfskqDxizBOWnHEzkDfelsiJgYh2VPjzy3Zb9G2Zks7z55iAI5_8m9DSAVJ6BZrx_HD7W28W8QVKlRYgtYdUhxzVOM-505TgNhKqhQYbU4oP-dbA7ElL1dPk8f9a1BrnAOmSi3IQWue0qu4yqmfNiff32cinVYqY_BLB__iStb1wqGTXQk7pB4BLKrIRPV4-QY8uZUy1iQGPbkaLeJvbpI1HvZ7i9nW6pETcPsRv4qB2WQ_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه G جام‌جهانی با صدرنشینی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95144" target="_blank">📅 06:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03ce4f787.mp4?token=JU--7rPWHytOFEfzzDKHxfun3aota707-Q9o8G8RfRzTZmJdXAd8PIiAgK5PTegE3xLXGfvhm1uzojVwfJhVE7FqcbB4Z74qy8gbNxBKktsALA_ni1Ewqsrr-w2g7HgrmNzdeUheHwvw74zcPSdQrvl3YKqvXNca9f-MnhOUfb3TEAFnTSL-1h706UNQjhIJ2YIxFXVzz3-r2UseRYN-odE9KzPjHfXa8Ml07GNhRsqQVUWS4NUowMPWfFtmKRihr6erfyJVU5nHGcfLOuXOTk94i5wWx7dTY0E2JWZ-SyvoZ_fFnluJu6VtcDJ2Qt1LZbXeEq52oqo7Kv80b7L9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03ce4f787.mp4?token=JU--7rPWHytOFEfzzDKHxfun3aota707-Q9o8G8RfRzTZmJdXAd8PIiAgK5PTegE3xLXGfvhm1uzojVwfJhVE7FqcbB4Z74qy8gbNxBKktsALA_ni1Ewqsrr-w2g7HgrmNzdeUheHwvw74zcPSdQrvl3YKqvXNca9f-MnhOUfb3TEAFnTSL-1h706UNQjhIJ2YIxFXVzz3-r2UseRYN-odE9KzPjHfXa8Ml07GNhRsqQVUWS4NUowMPWfFtmKRihr6erfyJVU5nHGcfLOuXOTk94i5wWx7dTY0E2JWZ-SyvoZ_fFnluJu6VtcDJ2Qt1LZbXeEq52oqo7Kv80b7L9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇿
👀
گل دوم و کامبک مصر مقابل نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95143" target="_blank">📅 06:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b497a60b9.mp4?token=MEjJ7B9eWMtH6bCpVapMeIjKOJ44SPH1M5I-65vnV648gWIS-Vi-w-qLafzPZD0LTUg1eEvRGgEVdEnd_5lT3SwrDEMu8x1AE4_pJZzxjVPjH59pY8FxiNpJE25tE5dSXweAd6xb6pTppiGcOM67ZWwAyCzH0Bk4SVngh6aCiaeaNOQh9OezfV6P1CIwZtiOO-ovuhAf7moIUEJL46GBCKoUnULRRV2QrmphFC5d7sGZK4tCXbDEPXvDWl3No8g3H5FTJ3v8g8wb9O3g9aSNkEfU_rdEa3yDdSrAcZg935wMR2sTsbYHH9slF9ipchI3wDUM9MiAUeEwGDDOA4D5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b497a60b9.mp4?token=MEjJ7B9eWMtH6bCpVapMeIjKOJ44SPH1M5I-65vnV648gWIS-Vi-w-qLafzPZD0LTUg1eEvRGgEVdEnd_5lT3SwrDEMu8x1AE4_pJZzxjVPjH59pY8FxiNpJE25tE5dSXweAd6xb6pTppiGcOM67ZWwAyCzH0Bk4SVngh6aCiaeaNOQh9OezfV6P1CIwZtiOO-ovuhAf7moIUEJL46GBCKoUnULRRV2QrmphFC5d7sGZK4tCXbDEPXvDWl3No8g3H5FTJ3v8g8wb9O3g9aSNkEfU_rdEa3yDdSrAcZg935wMR2sTsbYHH9slF9ipchI3wDUM9MiAUeEwGDDOA4D5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇬
گل اول مصر به نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95142" target="_blank">📅 06:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95141" target="_blank">📅 05:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH-UwkCuaWcBvtihFSN2vN_-MQ-v7ksXRrZbk9RLObnxPd7qMhoktlGfxOQcxR5YVHnYu30WB11iHnHvesHcaiOozXS6HOcwTIBz-kmYtzCa54yx66Idos97T84Wgc66xCKSfFT_m5g72CbUFYneuGHMp1-xrVvs2rKFBBqS3y0RaLnD-yJoB4cQXmhRw-0xTrC-e0YEebeVbIxXcI7A2Q3QeT9OZC4vY5yxiB8EPwZZO3GZwMmbhxeYyWNvWFafM5Fj-Q79Vk24m88wIGjnPbSZyFw5iZXZXdpx7RLLS2FKZGk1razQzugBpCdOs5su7hsqxfBvm1m3dUz54bapwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
#فکت
؛
تعداد فالوورای تیم پین دفاع تیم ملی نیوزیلند از جمعیت کشور نیوزیلند که حدود 5.3 میلیون نفره بیشتر شده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95140" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhADNPIBCvIyJRckuMZqlacqGlunrUP9duNSLcrlxive7liZHmqJgF68m942iWtTE2tm-VPeIpFsVQKpZeKopgpMLA-KV7Njc8CYcOHalyRmRoZ8ySVSUyQcWJ5lARGpbhGf5CukjQk9WDnlWgKEiOy850c55Iui6iXXoMr4NsbgyEXWkrj8dj7aYkoC9it82qU1kPTORRTqXqt_wncWqbprNQPpL9JCpL5OT74qHLpF3jQlqXoeR0RuULtG8zRNrjAQY12qzN_x8lu25VwUfkad6fGsii3rdsUXhFKr_xp-1abU9jkHSKvc-Jme4BFw1Bzx0tP_K4r6ErcuIOnd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو محتوای خوابامم همچین چیزیو نمیتونم تصور کنم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95138" target="_blank">📅 04:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95137">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac61dfc9d.mp4?token=mkRQvnANrh_hqrWP3PdK4hSkpDx5ezdum2WT32vEWbD1Kj44vSM8IfEa95tX0xAq2_Dg1jKlEeQu4UoGmgT2maBTyEGXYC-DpPjyzlHbWqWM7FsNCOoxaxTro2OAzxCyai7rLUCMq0BsWR6Ua2Lrz5CSwUY4ozS8EIiHqDJTr2Kv8uIw4b6jYrr5fBRv4gihhCymiXOK6RduTIqDlfgnQXOAAHV3qmD2323qX9VNpjIjQKjT4yoUDpMaKx8XKEjd9ZhmnM8bY4-qeKEq6TNbw32NfFWf_DU56P10fSeNqhvYBh1gCm1HVrhZSV6R18F70CX05wR_770n_Fql3p7zWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac61dfc9d.mp4?token=mkRQvnANrh_hqrWP3PdK4hSkpDx5ezdum2WT32vEWbD1Kj44vSM8IfEa95tX0xAq2_Dg1jKlEeQu4UoGmgT2maBTyEGXYC-DpPjyzlHbWqWM7FsNCOoxaxTro2OAzxCyai7rLUCMq0BsWR6Ua2Lrz5CSwUY4ozS8EIiHqDJTr2Kv8uIw4b6jYrr5fBRv4gihhCymiXOK6RduTIqDlfgnQXOAAHV3qmD2323qX9VNpjIjQKjT4yoUDpMaKx8XKEjd9ZhmnM8bY4-qeKEq6TNbw32NfFWf_DU56P10fSeNqhvYBh1gCm1HVrhZSV6R18F70CX05wR_770n_Fql3p7zWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇿
گل اول نیوزیلند به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95137" target="_blank">📅 04:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95136">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پشمام نیوزیلند زد
😐
😐</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95136" target="_blank">📅 04:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95135">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95135" target="_blank">📅 04:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بریم برا شروع بازی مصر - نیوزیلند</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95134" target="_blank">📅 04:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffe5f74c8.mp4?token=EWfavBedVhQjM7DPaSfHTE8pLWByTDtI3trr5tN6C4oRxImcny29_9UV-UYQ4tl6Uu5sWa5ev5dGxKm-UTwI8QasyrsHx4OIshQupwh0ralbndKlHjftv_sqKFIE1zt72eQJ4O-lNvCwtWOQ_e13ylo_eahcBVsguDyzy3HQDcVD3cy5lH2LvajTFEtgLIqTf5d6cqUact27fogXb7ncxsy-s0ZiOHpPpvn6cOTnCbV8hdJOXP2hPe_R73VMUi0M2nLuz09YwjCOq7sjFVVc0Vu1Rv1GH_e3XwP6dAYGRQHuXqsijx9U2pvyWR8m0oYEoUc5p1OnnoS_X-ka02Vxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffe5f74c8.mp4?token=EWfavBedVhQjM7DPaSfHTE8pLWByTDtI3trr5tN6C4oRxImcny29_9UV-UYQ4tl6Uu5sWa5ev5dGxKm-UTwI8QasyrsHx4OIshQupwh0ralbndKlHjftv_sqKFIE1zt72eQJ4O-lNvCwtWOQ_e13ylo_eahcBVsguDyzy3HQDcVD3cy5lH2LvajTFEtgLIqTf5d6cqUact27fogXb7ncxsy-s0ZiOHpPpvn6cOTnCbV8hdJOXP2hPe_R73VMUi0M2nLuz09YwjCOq7sjFVVc0Vu1Rv1GH_e3XwP6dAYGRQHuXqsijx9U2pvyWR8m0oYEoUc5p1OnnoS_X-ka02Vxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
واکنش کنعانی به گل آفساید طارمی: اینقدرت تو آفساید بود
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95133" target="_blank">📅 04:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWFLHLY06BcfWh27dXosvBAPEeDnbF1Gu2Gcy77ZR8E-jW-G9sPEBAy4SZ459Uh9Ro67TbQVEZRdMDhZMSGPwafIngQZC9f8XFpSzOiWylHjPKluR5bb3hyMTLI20WQ5NuX6et9UjsVdrPpq94c8l4Z_c0iqF4hKQOBEduDoEpHj9VFEUyvb0BlXU_g7zss5dTqfKFqzjYDXcLiamocdCAlkF6WORHkDO_MEGUj_PHvY549qWOymZ0Nu5EFBShGTy9yWyzrDOeUGkIHk335lGoKWWTHtB1RIsKuoon9t_wPhwT8lEUNh57ThONZdcENr8qRpx4HlxsvTqUYCsEc2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
‏ بیشترین مشارکت در گلزنی در جام جهانی ۲۰۲۶ تاکنون:
🇩🇪
دنیز اونداو — ۵ مشارکت.
🇸🇪
الکساندر ایساک — ۴ مشارکت.
🇦🇷
لیونل مسی — ۳ مشارکت.
🇨🇦
جاناتان دیوید — ۳ مشارکت.
😀
وینیسیوس جونیور — ۳ مشارکت.
🇳🇱
خاکپو — ۳ مشارکت.
🇳🇱
سامرفیل — ۳ مشارکت.
🇯🇵
اویدا — ۳ مشارکت.
🇪🇸
اویارزابال — ۳ مشارکت.
🇺🇾
آرائوخو — ۳ مشارکت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95132" target="_blank">📅 03:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vaupam8xHpDQdcbXB4bQQNRyT-M0PerGlreL-ktVLwNKGo2A7LhAayG526F4w7MPnsxv6I2MsCJRwawa5LjjBXmDvkCU4AbMdTiFE6dNmXiVkBlhH0s-A9zfCxjkJPg2gHXicJMvBCs2ZTtXavHkFSDQtR5UYopuM2yEtkqcmF3AZiGB_QrJF-rEckXeQQ0Gdl4UlBZ31W2_Fzehr0bKC9wytJXacea2841w3R3Wm6x7yuTYCeVT333p80ekOD6b7zmQaPJeTe0MjYkfZNQ4VyYw91FOlkdt2nCnIVrKpVLmwMJlWDfKCtd1DP-sH_zaTvHyryhQO3DDmHOq6VWauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وضعیت جدول رده‌بندی گروه H جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95131" target="_blank">📅 03:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krrEdqVguL0dU-k74-mCWaQ-MEsZEsrIOZX8O1iZnK9ZsYgfwn_zRIecK0G8VsLAKrzMhhvRCqVniHSCfNzAaS2oJLzE5WPQz84ZTvNjXhPzByx75lFihNTF0hD6Nny06JorGDLAvSPzzCZKriu94nGrdZQRlF6qWNSSAxCiy0Aem2RcWraQMvCRdi4gKWhjXD6Uu2_hHW_7JMxoEVPGIu6D8WqCjsDHW9mZ1V65BqVOztGg2OR4ds2R3PhFru3Cn3IrVxg0rJavPtQxg5OAybclRm0_x2NZrbOIL1R0LlU4CnyJeGcwO1Wmeev6FQViHysV4cW0Xi8c9tbe0Evlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شگفتی ساز جام همچنان قربانی میگیرد
🇺🇾
اروگوئه 2 -
🇨🇻
کیپ ورد 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95130" target="_blank">📅 03:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNxZ6E6I5GfHCUE9WECUfrcI4RAiaOVixT3oWSOjLjuoWGDNzYKgySiw6y4q0D3Fhhr2jp50Pk86rJuOAd3qGuIjxI1eyHLJ8kyjxvqXP3XFONEw67HtiRtoIA4YagERtqZ7TdklbTVsFN9LuJtXvnd209Xm0LV25uhmbVOHRQj00VBvuJ4fx5Aqqjac8kUDNeR1m5cuHWaZqrEWNY6zbrB5AFGnXc_y1kzxtm-9qk3iQ2UvQvhemT4lzPeGiZ24lgDVOAtbPUmBe3jlDSaDJaoxrpHa5Ln-DzRdVOOr3uFNgKaFel_-TZ4gkxbGwTpE3xDKGTQ00XU5WpufVJYjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
ترکیب مصر مقابل نیوزلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95129" target="_blank">📅 03:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAs-jvWSWWMdKjxO0SUeTg7RcarUsjNTigO5_xcz7LVcwnJ9eu-jkCcLGHiQYTsh076HHy0cdQ6MSDRfFXDb4CV6yQG22bLrWOEA_uZGo2db_EmwgLUUp6xHhU0MVZbEgbM9gPi_Ps6UjgStz9OAUPk6t0z0IQYe7hI99xPttkLsmGUCX_mTmrv9HI39mH7y56AeyXeN6hH7CwoLVaGl32ke_qCg9vL_5bz6jX92PTcuDv3kYBduZz1TfpSpoIQGcOEuvXv0dHx2hPh0GcI7Ke55EJ0WXo7g2IShn7RMkHmFGnEMHrlIaBZeZu7SVGAm7dlFPa_HPtbcXstroIRBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lkb8_Lfkj31JYFKH1viVdPibtVyOQ_mT4SYRdQ25DYuhkOGDe7P1s3u11vB5iEL5ZZMtBT7qHzm0E96ctzHYAVuOHDznAL14ogB-nT1eS3B-NZjVkwamvPzShp3LwR5EEYycQwVADs6A-32S5KuyogVm0BLMR6ZlK2KEpsSni4bSCPAuUg55x_k346ORSJtQts9t2SPbEImZYiPQ8E1ZfKskek5KjhZ8ENd18s66xPGmuEKpf4s9IafatEdQcFD2SJ2eGUB2exNiIKZLPeeB0EOaD6PM2jqgmxm68eL4NLmky2s_Pv5WniwUwVSWwxQFiARcnc1HwHzP6jyg3QXmdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازیکن اروگوئه اینجوری داشت به بازیکن کیپ ورد کمک می‌کرد که دید دارن ضد حمله میزنن ول کرد رفت
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95127" target="_blank">📅 03:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95126">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چیو نزد اروگوئه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95126" target="_blank">📅 03:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95125">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اروگوئه سومی زد ولی مردود شد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95125" target="_blank">📅 03:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95124">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46dacb2641.mp4?token=KS0Kf0rppTYxA5nzoytuN9cECEJ3JzVEDpmdCV6gQ06aLv-5_rNBhcpiROpxFLL5XtjFp416d6cXTP50U_Mx-uA1CUjkkqoQEHZ-gfg1PbpMBS8KA-HSWprJ5o7MgyWmsMFQL-AVLUu8FVzOvgJCF2qCtPWkTs8NEGrJwza5OCfmE0uqZcyip1WgQXwsuAfN2u6R5Cy83Yo9QqF7J9UpImUT0M3bNp8SykyRGjhDkAsM3OAEE-osls8JebbYYwzQKv9T3z0rx0J4KH7EbKWimyr9vaqSsA2U7BcPYGqh_67IP1oKJGN-S8krN1QWG-60kACnpAWwrZv3q7lp9kj431N6QVY7pUpPqlu2vSkg5oTkHrcEMIaCVPjcHFv92btNSQfioWXRkKSwexY_qFquFtc3mEqKkbygPo7qKQysqbTMKS5ANZeO3YF00qkPe7mvPa2P-ZpLCYFHrks_F1IcTm8f4m9kJVBvO78Vg0ncyoiEuzsBw0ZscBa4JHvTDjwZHPyLgbAeQHCHr3SauumJh_t2GOKNcBIU-5hNla77y2_UvRaLvjjjVgQOG7Ym9xw98XsEsu1iSlJEQu6APaJu2-pSDYsjlx3ba9-oAeYwLyL-44RWLahXZC40VmAfqxjeYLyeKVAt9fCyy5YjnciEtwTB1xuctM3gTUw2ObGzHBY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46dacb2641.mp4?token=KS0Kf0rppTYxA5nzoytuN9cECEJ3JzVEDpmdCV6gQ06aLv-5_rNBhcpiROpxFLL5XtjFp416d6cXTP50U_Mx-uA1CUjkkqoQEHZ-gfg1PbpMBS8KA-HSWprJ5o7MgyWmsMFQL-AVLUu8FVzOvgJCF2qCtPWkTs8NEGrJwza5OCfmE0uqZcyip1WgQXwsuAfN2u6R5Cy83Yo9QqF7J9UpImUT0M3bNp8SykyRGjhDkAsM3OAEE-osls8JebbYYwzQKv9T3z0rx0J4KH7EbKWimyr9vaqSsA2U7BcPYGqh_67IP1oKJGN-S8krN1QWG-60kACnpAWwrZv3q7lp9kj431N6QVY7pUpPqlu2vSkg5oTkHrcEMIaCVPjcHFv92btNSQfioWXRkKSwexY_qFquFtc3mEqKkbygPo7qKQysqbTMKS5ANZeO3YF00qkPe7mvPa2P-ZpLCYFHrks_F1IcTm8f4m9kJVBvO78Vg0ncyoiEuzsBw0ZscBa4JHvTDjwZHPyLgbAeQHCHr3SauumJh_t2GOKNcBIU-5hNla77y2_UvRaLvjjjVgQOG7Ym9xw98XsEsu1iSlJEQu6APaJu2-pSDYsjlx3ba9-oAeYwLyL-44RWLahXZC40VmAfqxjeYLyeKVAt9fCyy5YjnciEtwTB1xuctM3gTUw2ObGzHBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم کیپ ورد به اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95124" target="_blank">📅 02:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95122">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کیپ ورد زد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95122" target="_blank">📅 02:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95121">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95121" target="_blank">📅 02:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He-Fpl8AokMGaXHC-r8q5LwUclOj1oh3QAH9eqMNM2Os-jP6qwz72cmIlvS3GOxsIQri-c2hga84PksC1E7zuNlhG8plZa9zxg10ZOUaZ7NvjYEzl5d2OuTM2CLlx_5AdItSbQ-XUKKxXx_HW3Or2YO21XWeCU2mbLe_dBat6CkQ-NQUBIXzF4-O7k3SxDRxyvyFNp90nY7dWfbisTkl9pkPDNb__AyiyclJDjDrrsUJR91JpUrAfYKYM2wsnJl0nzHXEYlHUCWwvd8BqbOtEFL5-h5v-ntjocj0YNzSdNqqFMVx6pl6NiPTwQxqtvfgkSvWeSoMB22VoIq-koLShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گلر کصخل کیپ‌ورد 1.3 میلیون فالوور میخواد تا به تعداد فالوورای نویر که 20 ساله داره کون خودشو تو فوتبال پاره میکنه برسه
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95120" target="_blank">📅 02:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0B-A0-h-gPKu06rbJYXxUSEvCqCTHI6bZ2uTTeT9dgs4uyXlWx4zLsqMXtgfK6ikl5vGZTCBhAeEclcY6xyGhHAHpxKjefjXKc3YgocxbHFzfdnDB1S8U8iUlXIl8X1FJmazDI4ySGIy65ER-h8ooZXlWqmpsNZp5OarCpzt0DA4Xvdswd7Wc3Fkf4VKwAElFuMDGNal2Fth9QKO4K_NDGYV30k0fLU0_q5DcDcf3gtKe-tuEp7scTHd_OUFvBwAwdr0cZnTdqx6_777Cd2LnDNpsFR1MZ29T5CyBejn8ulXAuEYmChtYrzks4lw3Kyl8xNz-eESq7LIgh0_UULug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
ترکیب مصر مقابل نیوزلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95119" target="_blank">📅 02:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95118">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7BQC2xmbb0Ottb1UPTiDUSiLfmJhFZDphWEdfuwx50UE5s-MSIS545vPaxOA8ywbY6loqqBhOyaLdZQ3fBRiB5VZcfFXRzszZvG46VwjWRjrEWLGsu_Fnv64x85YJZvxxL4FZ8lkw6oPS3cEfyyA-BhIHSoYgwH1P_2FCoO0LEw700aFWVQLIiU_DP1c5HpgOTaWc5hfn9QqJsLY3nZdu-KnrHNsOmNXcDsgrJofNpAsgm44eUK467OCI7RnHRIS1Pf1CmLAGyNTH9HaZatb4y2TfXIEqQHD4xY5LboAvc2AkAPas3jLC4OKhIWnR-db4zIuG1ej_eKwb9B_uqa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار اروگوئه چه سمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95118" target="_blank">📅 02:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95117">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیمه دوم بازی شروع شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95117" target="_blank">📅 02:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95116">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK9Y2fRIFwHkjBFE4SXUw_KEqSp1d_9_GbuMSK_0fxSqeTiwHbrwWhhQ6D-jdGpCMyFbhT8f6MUE1df5ayOXLVLEw3Of5yFwoilX9c3ZfuCYZwWZrONGrECCk34KVTq93gRwcvlQq1JSK2isTyrbuPvtbIMMt-6dYmAgu-eBNdJNQ4IPsXZKW0Y3KwY4-MACNcTvV5_xhaDIFxKmRxuE3CJWQZnikqA-XM-96pDQdrItGEFKz2OtKLEjnULxJrXxdhvsk0dOudHZzTm30O4NAiBxSVf0nUWtsQbR0sK96qSiGylb8Li6Ifl43MGzZgeDEk3y7XxnNtpHIguzG47dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید جورجینا خانوم کریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95116" target="_blank">📅 02:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پایان نیمه اول
🇺🇾
اروگوئه 2 -
🇨🇻
کیپ ورد 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95115" target="_blank">📅 02:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508a2a45bd.mp4?token=jvYU6yZw_7DFFvyqYpgu9g2EzcNp12aco_pMA8lh77RsyfporqTwYmOMIajl0Mpmzpo7RssLSq_f_asI4zBehztq6RmjK4iVJNS1FJTNON47WkGgvF0RTmMjLEw71Xx9Wn5tRDfEgQBLYHm767c_Ot0z71HNHoY7ZTz7HxEhcBLgY5doJ5L_6rocm0usTYvHCFbTPts5qt0hOe-HlaurrdUuJwkngfSuIgz95DM8c_FlH-oEe_zcHngw6V_qnsSqKgBfHJkDQnYKF0kONdxxgDFSzj16mF4ESv2oDbn-LCUVeplDrPgWCekbjuyC1f_tCmnpevQx4Yws-Z1fF87irg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508a2a45bd.mp4?token=jvYU6yZw_7DFFvyqYpgu9g2EzcNp12aco_pMA8lh77RsyfporqTwYmOMIajl0Mpmzpo7RssLSq_f_asI4zBehztq6RmjK4iVJNS1FJTNON47WkGgvF0RTmMjLEw71Xx9Wn5tRDfEgQBLYHm767c_Ot0z71HNHoY7ZTz7HxEhcBLgY5doJ5L_6rocm0usTYvHCFbTPts5qt0hOe-HlaurrdUuJwkngfSuIgz95DM8c_FlH-oEe_zcHngw6V_qnsSqKgBfHJkDQnYKF0kONdxxgDFSzj16mF4ESv2oDbn-LCUVeplDrPgWCekbjuyC1f_tCmnpevQx4Yws-Z1fF87irg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇾
گل دوم اروگوئه به کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95114" target="_blank">📅 02:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اروگوئه دومی هم زد</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95113" target="_blank">📅 02:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95112">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95112" target="_blank">📅 02:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95111">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cdc8088ef7.mp4?token=lRj8wWAiCSmEmduQuzFpoNHYoTVM7m5rCvcJxRhcf1KgVVWioDXyJ3UT6qwbsns4Fh6H-bZOnV9WyKxcZrvZ6Ij4SLRfSbAr8XiMufOUMSqsSz4_Z-gUPeWu0wh3lJhrSxmdovyWCBLULj2JqBgJ6OBMhclwVLiBbvdtMm2NA6Ry5Hdh7erfgxdVbJUXI6IBHNiBU2atYTN86mKMuWK91PeXQEg6mCrw-VKk--XMX6T4oIbIRV4RIePTV913QbHR9UiVra2AskKnJFjcvNJkzfmvv516Xw2fBXUYcRiQMtfJ94iVWeDyNnaZlAND2YSAv9qkkkV61600hgx90959lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cdc8088ef7.mp4?token=lRj8wWAiCSmEmduQuzFpoNHYoTVM7m5rCvcJxRhcf1KgVVWioDXyJ3UT6qwbsns4Fh6H-bZOnV9WyKxcZrvZ6Ij4SLRfSbAr8XiMufOUMSqsSz4_Z-gUPeWu0wh3lJhrSxmdovyWCBLULj2JqBgJ6OBMhclwVLiBbvdtMm2NA6Ry5Hdh7erfgxdVbJUXI6IBHNiBU2atYTN86mKMuWK91PeXQEg6mCrw-VKk--XMX6T4oIbIRV4RIePTV913QbHR9UiVra2AskKnJFjcvNJkzfmvv516Xw2fBXUYcRiQMtfJ94iVWeDyNnaZlAND2YSAv9qkkkV61600hgx90959lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇾
گل اول اروگوئه به کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95111" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95110">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اروگوئه گل مساوی رو زد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95110" target="_blank">📅 02:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95109">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
قلعه‌نویی: معادلات گروه را بهم زده ایم و به دنبال صعود به عنوان صدرنشین هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95109" target="_blank">📅 02:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95108">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb-MI_mU90jsY3Ka7uEVr7mDNWufq2eSUPgOoE7ruZ3SYX1OmJUEhJi3me4_Pr--qWO-vCPmhMTs89vlyALyNZAsmO1u650--R601bR7rYWV7ztsNrdKMroiZKVOO50Jy5sv_eNKREGq9QTbYIiAyT2d2WlbEyQ3o-lfhHh8B-_50oUDArx7xH0Pt8_rONGkoBjrEJO_SBvHAvPJGKWgtgLH9RdkIZQWkVMYnFy-tFzunBIMl9on6XKDyEQn-XkIvx_-tjyrHVGoOlW7kptnA_LVh4jbHhk3YwjfRG2iPJV6sEskGAoa991iHTJ1MvnSrGr83WOfR2yKDQxTYUAszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کنسیسائو : وقتی صحبت از توانایی گلزنی میشه هیچ کس بهتر از رونالدو نیست ، هیچ اجبار یا ضرورتی نداریم که همیشه توپ رو به کریستیانو پاس بدیم، من توپ رو به هر کسی که تو موقعیت بهتری باشه پاس میدم، رونالدو هم اینجاست تا مثل هر بازیکن دیگه ای به تیم ملی کمک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95108" target="_blank">📅 02:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95105">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca2c51a18c.mp4?token=KOpAoPflID9C-tw62x-73SWB6ChBhKaS2j4nXEPD0kWnR5N8Cdlqt5AaJ3UlyH204ptd8KK5gzUE0IdxrSTgDMTx2G2j6YSA3Ni4DcxPSZyGeaxaS7VoSgGfB0OdyrfGsVj26DF2bQNBLQySagi8The-f084APZ2cVPpzQjuJd5A7aumxjUzEHDmv-eLZT0pJgblzXuMAxR1Xi8VFamT2sMt9rW6wNhTTYFH_m9TStiK7YtHYxEbe0NnJdqGeIrp1la7y7vGVoSk2ZKKAW05gMQ4MICe-WM8VHu0va2KXgLKzIxG6C8bXntmKPkoX5ANPo84X-b8N7hLIYojtmbFVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca2c51a18c.mp4?token=KOpAoPflID9C-tw62x-73SWB6ChBhKaS2j4nXEPD0kWnR5N8Cdlqt5AaJ3UlyH204ptd8KK5gzUE0IdxrSTgDMTx2G2j6YSA3Ni4DcxPSZyGeaxaS7VoSgGfB0OdyrfGsVj26DF2bQNBLQySagi8The-f084APZ2cVPpzQjuJd5A7aumxjUzEHDmv-eLZT0pJgblzXuMAxR1Xi8VFamT2sMt9rW6wNhTTYFH_m9TStiK7YtHYxEbe0NnJdqGeIrp1la7y7vGVoSk2ZKKAW05gMQ4MICe-WM8VHu0va2KXgLKzIxG6C8bXntmKPkoX5ANPo84X-b8N7hLIYojtmbFVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول کیپ ورد به اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95105" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95104">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چه سوپرگلی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95104" target="_blank">📅 01:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کیپ ورد زدددد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95103" target="_blank">📅 01:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95101" target="_blank">📅 01:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJTdnISWDjq0f0ykgwWwQS7KKE8FgvYk4sJs2OQF0t8sZy1wBAu2_RjwblXjMu5hIWTQKCbzLJm4OzCWy9g7EK0QD6O3ySDZtZhkJ9mK5hMgysH9K2eoIljirAjCKMFADTuYkUWaT_ZXUUov0P4dJJca_7fVtpJJ9npawcwXrZrgY8_VyorLh_6tYVidaF2gfc41_WilGZZCBeHXivqlByCeuhx_Pe39eK9_gZCKk0t0R1bJGsKUj97AgzNiJoPv1W2N0mK4y_QuWMZ9OTERNLKaRM_V4Qcw4_WLl5kfJi7v9QsEVSphWEw3ThLSZx9c4XruDosfQqtpjct_Q9op3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوارز تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/95100" target="_blank">📅 01:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4516eab25c.mp4?token=HMteqNFq3X_rsg8ie0Zfz60gPGYkX_9QauHWS5nlUp54jTj7-NNdcRCUnjJjSMp9tUNEGjbD9GmWoryj0NHoVgbx80wbHtIR8TIKYyVu5iJXnLKB7DK1kzJY65sdiBolwjJmPTo8s9vJG7MObNIv3ZVber4WKZizxaZsHhxnn-uxr_a3F9JHQJ1WjgyLqA3-VR_1xb_M2UOkjzZMq8RHkktFIhUSy4V47wd_XF6Ls8Daqj9yfYmvSZ9RO70SnAjk596Dj0JcpXS8KIJi2PsYvkMSNvtxzKQdvFKmjfBHWVYl5bmbpmNzMywpqQe3PGzpIUpIAcnyi1cMn23s4wiQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4516eab25c.mp4?token=HMteqNFq3X_rsg8ie0Zfz60gPGYkX_9QauHWS5nlUp54jTj7-NNdcRCUnjJjSMp9tUNEGjbD9GmWoryj0NHoVgbx80wbHtIR8TIKYyVu5iJXnLKB7DK1kzJY65sdiBolwjJmPTo8s9vJG7MObNIv3ZVber4WKZizxaZsHhxnn-uxr_a3F9JHQJ1WjgyLqA3-VR_1xb_M2UOkjzZMq8RHkktFIhUSy4V47wd_XF6Ls8Daqj9yfYmvSZ9RO70SnAjk596Dj0JcpXS8KIJi2PsYvkMSNvtxzKQdvFKmjfBHWVYl5bmbpmNzMywpqQe3PGzpIUpIAcnyi1cMn23s4wiQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
💥
دلیل موفقیت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/95099" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fya9C4NsYJzU0wYwJc5akFYyTJliHgdAQhxlxpA8nMGw8hQkofTFe-353O7CE9rQP4RQ-n3m6h1fexGsYALxWENel4tL3Zn-P0Ni82q9XZVUTpeRHIQwSTQYcaIWT0nfmbA0A1tR8fucMVNiQzCo3-axB5xlYK7MJ8ClsUNFxCMVaUGYHb7aq4hC6aySL9v0YsOHusvk3cQXhd18UM1KS5uB5LSZ47YyxsNcvFYSPrllHYWjq16zxoFlwo5H_eXWB3DuyA34zlPoTbjp-l6P92Yn_kam26AixoXKRwrUYTfFiWNQPUc-dpc8LhP1-QUMvnOQQGr_TcrCkG6olLTH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
با تساوی مقابل منتخب ایران، بلژیک در رنکینگ فیفا به رده دهم سقوط کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/95098" target="_blank">📅 01:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95097">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0036204705.mp4?token=VOrY0Al3HkrFKi1FyHDsN2Xr1Xu5gXWykZ-965sRchTI3uTnghTfGJvaK_VpRkBA0upOIoFHTZQeGt6bmFzbM_ng6-Hcu0nYhAWjnRB2Rn0YATlWxJ2oP7KrU0JmeCfdHLyk9ZzHV2R08kj8Pzy43JrHzswe9DfHsJ4t1pSLO35SKEANaldYeo8QuReNXJxQwG5g_J5JVYHciiOLcTtrdXNkYiQQVq870Mk54JoMVPdBY1-YwylzKV1e9gL4OwONs9-fghAlssBvwsbZH1D19bDCIp48hkZLygfGK5-PNfXO-p9_k43No8kvPZgx9kR1DsQ2gQ2SMdIEEJ3kSiOvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0036204705.mp4?token=VOrY0Al3HkrFKi1FyHDsN2Xr1Xu5gXWykZ-965sRchTI3uTnghTfGJvaK_VpRkBA0upOIoFHTZQeGt6bmFzbM_ng6-Hcu0nYhAWjnRB2Rn0YATlWxJ2oP7KrU0JmeCfdHLyk9ZzHV2R08kj8Pzy43JrHzswe9DfHsJ4t1pSLO35SKEANaldYeo8QuReNXJxQwG5g_J5JVYHciiOLcTtrdXNkYiQQVq870Mk54JoMVPdBY1-YwylzKV1e9gL4OwONs9-fghAlssBvwsbZH1D19bDCIp48hkZLygfGK5-PNfXO-p9_k43No8kvPZgx9kR1DsQ2gQ2SMdIEEJ3kSiOvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ریدممممم حرکات دست قلعه‌نوییوووو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/95097" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95096">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssZzmC1yCsFlKOZ_DcrixSxPEntzuN6w4TA9lcsJ7i9x1ZRAHCb5LQOLgAnM2wqVa_-tSBCqnm9p4EL3WZv7fbNgTHFCrBzXpzFMmbg6m9nujx820t6HxaSjRsfhd3zmTCxchXuarhr1Sv8fG0u2vXJVe2mwH9PO5FzI8t3FmpXgB4pVH4r5g7G7QdipVojKFBp9SM0Jt0vsAaOFLfMzmwWX6KpVgnYiXkaXXU_nW5WCcpigVu6E4yBnAQSK4NcyPBjOuYdlm3oqpqKB5-IJIY5Ex7iYQ8A9BJZfSpR4LISFkH1gUuggbNyOhxh0UTZtVbxn09s_gDlWF0kkObj0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
آمار پشم ریزون؛
دروازبان‌هایی که تو تاریخ جام جهانی نمره کامل 10 رو گرفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/95096" target="_blank">📅 01:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95095">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17l29I9HVQpEjlBtvHYwE_tw1LoSzD7Wlq8TyB4fLHxbgdDuRnTu2-FeqvSzFUl-OPhiWpg2zOlMhq1BBT_X02qALneed_gayXeAOBT0w9oQsnpBAwKj2svvaG9BwSSuni4cvr1Q1crh4obZ1-6zyagcUi54hUdtac-gdwTxGTCNlYFkIodk95fRJpwdDfvhqkKXVBWmKWgwreb8HUnss6dvAHKamXCuVklBFP-Ti10ScuuikEgNsJ2unm5VnvE-saF7vQO29uxTVS0K2pu3AMn_hy_Szm1eqTBtRBac_it1Ve9bnqXAjOmVLS1unDrT1TU6Fg-1moLUSqZRgDyBt8uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c180e5c8f.mp4?token=q5n_-J1CvcWt2Lzi9cYdko1nT6JX-K91ykSvtD0Fc6jEHWnlyj0HPc_6mZW5rQefwIUqUfkopDaL6RslqvJoabYpcg2NuAzEcRKN20IOVAY6KqIs92Jb0tBO6WIk31Jm6_gW2v_Fjw89fqIGaW11lOASfAUFLK6g3kcDR_MDjwGcscEZifdxJi7-9WNvysB0BtrMATHi21-3akp3Qn8J_RK7RzkqHW3Gb2trNpWc5jd_0BddPDU6Dh0dnWL81JB2bm-Cquwmqo3goT7iY6ylxBXOTPqm9Pwq3O4jgjqLZT4fhqiO8xVbGvdUUPAWEe462GJHMCEWREU99BKo8cw17l29I9HVQpEjlBtvHYwE_tw1LoSzD7Wlq8TyB4fLHxbgdDuRnTu2-FeqvSzFUl-OPhiWpg2zOlMhq1BBT_X02qALneed_gayXeAOBT0w9oQsnpBAwKj2svvaG9BwSSuni4cvr1Q1crh4obZ1-6zyagcUi54hUdtac-gdwTxGTCNlYFkIodk95fRJpwdDfvhqkKXVBWmKWgwreb8HUnss6dvAHKamXCuVklBFP-Ti10ScuuikEgNsJ2unm5VnvE-saF7vQO29uxTVS0K2pu3AMn_hy_Szm1eqTBtRBac_it1Ve9bnqXAjOmVLS1unDrT1TU6Fg-1moLUSqZRgDyBt8uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
👀
سیو خایه‌افکن بیرانوند از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/95095" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95094">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=VckpsSJF6i6aJdyVX_MgEi8M6_GZuY6NrNsbJ-PmlDThb7UUMFurxJASKzRnO4eZVEj8I8LXXmi6t-Prc-P0dzOLKP64BIWIhy5nLgdlmzQrN0ceoA99bzlBTdx1VThHXA-fXFJLzFpBvP2KAEWj9PoSsla9CoKmL_KqEiLY3WXVbAk5sFUguuCC-T7XhbgV_x8RN4lJvp3E10UQy6wa5WzctnLV7uH1FeAv62O-JdFvbPBsifPy20Izyx2K4ljr9Y1Y-LN_DS74fAxh_95w4NSJK-d-RbMy8_zkjNzKcj5Q5SFEe0tzcYbTP4Z3ktmGMseyfP_kiTDgzk9PFJ7O9ii1wGE3Tve7rOYMJiAFUlaz38zMqCzXnHIj1C1FhLLCBPxu6fPop13Z5mIrpntoFHfUgX4sCBKwtPRAbwUkxZ7WApX2ARpj4n8tg8I574QZbKX5SeU1AiRnDWecMWnljNB-4KBefoQ5bn388fB9ONXFsfolMKD22nAzvqrZBAq0KnskEk6fil2ufUs33HGScaNQ7Oa261SK1aWA7kDRiU-7QbaVxZYAkU14O1NGOLvAb32_KRFyqJ8EqpUwITbKu4jHakRzdG9JoUlMdX-AewA64nl-eSPFo6HPAX1YK2QgLTyNXcRh4K4_yR9N4cKN5tlBNLdlFRvjCtrz7J65YDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccbcf146d.mp4?token=VckpsSJF6i6aJdyVX_MgEi8M6_GZuY6NrNsbJ-PmlDThb7UUMFurxJASKzRnO4eZVEj8I8LXXmi6t-Prc-P0dzOLKP64BIWIhy5nLgdlmzQrN0ceoA99bzlBTdx1VThHXA-fXFJLzFpBvP2KAEWj9PoSsla9CoKmL_KqEiLY3WXVbAk5sFUguuCC-T7XhbgV_x8RN4lJvp3E10UQy6wa5WzctnLV7uH1FeAv62O-JdFvbPBsifPy20Izyx2K4ljr9Y1Y-LN_DS74fAxh_95w4NSJK-d-RbMy8_zkjNzKcj5Q5SFEe0tzcYbTP4Z3ktmGMseyfP_kiTDgzk9PFJ7O9ii1wGE3Tve7rOYMJiAFUlaz38zMqCzXnHIj1C1FhLLCBPxu6fPop13Z5mIrpntoFHfUgX4sCBKwtPRAbwUkxZ7WApX2ARpj4n8tg8I574QZbKX5SeU1AiRnDWecMWnljNB-4KBefoQ5bn388fB9ONXFsfolMKD22nAzvqrZBAq0KnskEk6fil2ufUs33HGScaNQ7Oa261SK1aWA7kDRiU-7QbaVxZYAkU14O1NGOLvAb32_KRFyqJ8EqpUwITbKu4jHakRzdG9JoUlMdX-AewA64nl-eSPFo6HPAX1YK2QgLTyNXcRh4K4_yR9N4cKN5tlBNLdlFRvjCtrz7J65YDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امید نورافکن: بازی با بلژیک، بازی تاریخی برای ما بود/از لحاظ بدنی در مقابل مصر، تیم آماده تر به زمین خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/95094" target="_blank">📅 01:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95093">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=oMO9ymQ5Mb1ykNflMH85GxDo-3w10Xw6jFOf0vUlloRZ8XmemfDrpNdiswM56cT8G8h3xZG8_8rAgFD2Jag4swIpk0LyZ6D5fzG5JA1W-8e7AqNmksXXCvqRqhy1-2FieCpXd-4zL8DsFgEywHfgkxdLdFwkVmXeycT4Sn_Sk2_roP3SNBqh5EGYNRp9_Qdl7TiIbf8dyTyprd48jVpqnhImMrs_HHcYApeEJ_p1M8ZTi4JnChLtF32fAAWO0ZE1vHOOW_lhyvXoIXtof7oDnY6YS-671rSF-WJ4yCQFpw7AWNNhu96sek_qhN8Gqo9kNP1QciuwNpy1r_sA5me3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d8e1f59.mp4?token=oMO9ymQ5Mb1ykNflMH85GxDo-3w10Xw6jFOf0vUlloRZ8XmemfDrpNdiswM56cT8G8h3xZG8_8rAgFD2Jag4swIpk0LyZ6D5fzG5JA1W-8e7AqNmksXXCvqRqhy1-2FieCpXd-4zL8DsFgEywHfgkxdLdFwkVmXeycT4Sn_Sk2_roP3SNBqh5EGYNRp9_Qdl7TiIbf8dyTyprd48jVpqnhImMrs_HHcYApeEJ_p1M8ZTi4JnChLtF32fAAWO0ZE1vHOOW_lhyvXoIXtof7oDnY6YS-671rSF-WJ4yCQFpw7AWNNhu96sek_qhN8Gqo9kNP1QciuwNpy1r_sA5me3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استراتژی امشب قلعه‌نویی که عالی بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/95093" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95092">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/95092" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95091">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vTSCCCCsIm2uGCfGJmTbCLrt-63vpnu4z5p8Ef4n3lJghxgpjxsi3w5Jym18uJlXiI5Ti05ZAtaGU7uK_Nn-onYa1JP7FQXqM-1UUOCG_BdXFZZgui4drR-lu52_onz779t7yzw5yxdz1ZzQD2f6SKTigiVlCN4SmDE6XFiDkoc760EeVqbjZpVXzUQ9o7SckZ71P4P73-W-QT7UTSxpRr8y1K5gtPRTTR9Qs7FGAFNrLzf2cM1ilrQ5nj2KDaNyUlUJd2l8CcRe75-bJnxznwVhKLqrUngCVqcQbcipqX-msCrxwSwlL40jVvIpAxIlCSalwN4NqUKfL6-jmLAZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/95091" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو   بیرانوند به رئال مادرید  here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/95090" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RkkzD1Yqmp37DMnFhjFKeedduhtCdU40uPMm8VCLdqCpw9UjCHs4dTeJv58nVa9E3SMQMwbMNqYo_aAJAWLDcntHJkUMlSp72xYP6Y34VrJCGk3JvQSDsUYCNPoa9Xq6UGiiQPqXYNRfinHyiJ7C5IpVE7ZrGvoSBN0oJXvNeuXA9wh16XSWkARZC3PKVtP45ac2qDOSt3n_Vdugf8esyIFgBusgla45SK7kisZc1gw6QzRfCBXeGXli91LqgOaQoUKNgF1FJornhD5itBuPScm7lgVbxIMCk0ko6ZYDxyzhL6pINjr1t4DKyJU4yx33-K586dI-dOZerxciV2Ai5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از رومانو
بیرانوند به رئال مادرید
here we goooooooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/95089" target="_blank">📅 00:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csUhcNeVNfxP1-4Z_7FuNRJRVSjp1v7QHNZBhx-dwlHrLNJpXJiF3GEezNqvig8lOhxHFOdscOMdoURZO_wqtaxf8GEmhk7cYb8wqIXwGqyAkE6CrDDoPH_iumowtvlllpd0q6paIqIcMKGi02fHIBtE1PxVPuuhOWDTVTUdeSbEgHUioSMZC0ugEGkpt6EjbuBHf0sykUU_1k5sN5odEnazTdgGbl2kcQcUU5dATtnmrtoaXNvOgy8UNp0rFOqLKXf9yYKuUBsuKE1_0JM2gSBC6vNX3Mk3RNtiJIx6LkUky17956WRW-gPm6fpGB_I6hG-wYcsx_rTfzONMFfOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیرانوند و جایزه‌اش بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/95088" target="_blank">📅 00:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=LNRpI5qAeh1lc8wHnM8gRnnl4HcJOc5uhNKOl-Zi_Ch_uUpz92GzB4GwHNpRO2o-rChNmC6K4orq4hC56Q8DJExPlrGqt3ltO-pOvR1mK6G2GPjpYR3EsLStLCnuIkRdptMuYvOgyoHCkXeeMQBkxUnhaeVfPHHM8wvOTFgiKjax5satkjLosr5hUec9zR_jskBpmFyMXd-rPmiNxj6pY9W7yC5xe1f6N-rimbXZGDN-R8xvzZgz5nLsoV27pRx91EtrEmuTEg-TGoVblgop903SPBfTphr43kX-DYgb_PhfqG9Mnlx1rMyA0W9qfjCYUPh2ooPfvR_CmfGDDxnfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a4d65e8d.mp4?token=LNRpI5qAeh1lc8wHnM8gRnnl4HcJOc5uhNKOl-Zi_Ch_uUpz92GzB4GwHNpRO2o-rChNmC6K4orq4hC56Q8DJExPlrGqt3ltO-pOvR1mK6G2GPjpYR3EsLStLCnuIkRdptMuYvOgyoHCkXeeMQBkxUnhaeVfPHHM8wvOTFgiKjax5satkjLosr5hUec9zR_jskBpmFyMXd-rPmiNxj6pY9W7yC5xe1f6N-rimbXZGDN-R8xvzZgz5nLsoV27pRx91EtrEmuTEg-TGoVblgop903SPBfTphr43kX-DYgb_PhfqG9Mnlx1rMyA0W9qfjCYUPh2ooPfvR_CmfGDDxnfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
💥
واکنش فیروز کریمی به سیو بیرانوند: خدایی خیلی تنگ بود
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/95087" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjS-BPLyROQy2duslJBTsd3kvoc3KlNQ44uMvxed1zGTJetRZ6Tt1zMBunjdRdAdl08K9-_KHBbwWZSZUfXJbZ-iNpEH19e2Ez8R_L1K686y84rF94nBs4pzD1hJ1mu_VB_KlLFKLYZ_nLbhbwrINB3lCuqWgUgd797MmO0qaIRByT-YU04N__zI5ZZF2Jo1poO7J0HGtW4rvK-sKfu4cfR4kM4MFHJxcAmm94vYomjwo_UxRytRNeSm38fsbdgKMZJKr3CgvbQ4reZyWHTR4q71B354FbdpMRf1NC-efVlsQyUDmRfmmmIBPfegWmjIC1Kd6hStCkxgCZ1hbfciiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🇮🇷
زلاتان ابراهیموویچ: در نیمه اول خواب‌آلود بودم و در نیمه دوم چرت زدم، بدترین بازی‌ای که چشمم دیده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/95086" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD8TmTUqp5Vua_sSrw8t7vLLRz3vezAsGOICmEYMxhHEs587-dbXSOjwhPBd0E77FaEvzXBJ-hB41mqf8gXTNk9qxBVj6KPPukD13b77iEPKCgIGwwREFuRHBIJSaGXJbckCmYyCUGs8hPmNpLpW9MNweJIwghBZZ1fmR855AnvklG9SsWsfi9WFbQlU612aoD7QYPcH6uOhqxnT6uSdLjfUvttnQYOFuuA58v_GlaDpkJ3TdoQlKrseZuzpwWbl9yT4veKssrdAqjI5UNiu-nNr0kYc3N572JXAPN2ZGUzft1eN1GhCch3nMhhjwhEOClKEtxYqAAGvwHhI0jrr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تا اینجای جام جهانی کلا سه تا بازیکن نمره کامل 10 گرفتن که یکیش مسیه یکیش بیرانوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/95085" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-5v7t1aq08ZvKp2_EZxZ8xyLPavCVewZ7cdi1v--t6vHzCn5PExduglusEwaaYkG7oyAlKuskbRAVG_VhLAMNfIrpfjzo78OCU-dUydCNnCVQJQ1XGOmYAkjqlRwGLB9Z-OraLjFyn3pO1QlfDLDtxS0QsD6FtXNDOdrcso-xTQM1rdB6VltwuNa-xmsY3cjoI0rHknQ0E-dZapfTUyqp5tXHZyDlxBGYOkojL7nHE3RLqWYeNdT-5A2voglEik303pv2bicAAstv0VwhTCb_eTlk6ftTqczxmWHgIiMdxn_4AYHl2zx82ijxpkrsfU4wnkpk0xRVGOhhMo11UBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو محرم وسط خاک امریکا در حالی که داغدار رهبر شهیدمون هستیم رقص بندری میرید؟ ما ملت ایران خواهان اعدام تک تک این بی‌غیرت‌ها هستیم که داخل ایام عزیز محرم بندری میرقصن
😆
😆
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/95084" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/95083" target="_blank">📅 00:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95082">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evYcWf0zJxhITQprB02JL9iQ12iYAX3EcuWBTp9_I-r59yYFQn9I9uO3aAUaYDMd4yIVI59Fdfu2EsM419PSNqgQPrnZ-EOZ6p9coz9T-Vl6cx3Hffj1uWng_ENw7aPtjV9N8mkU0Z5-Q_HOSGBfezM9fw3qVo9krx0jvOjnq9bHVL2Eq0S8AAtcRAS4HiiYJ0YnZYne-B4GIFFsGMYetFiQ1BtI8IXqB2ffMQoPGfhySOUvkugzXdT20JeqJjfrPFsOoZ7rjx3kpoxQx9eGTz_SlUG6KSQHDo_wrjsa7otnjvDaiA0I0rJ44gSmSIEwlHJRw9EMAXqjzlwoUIhCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🙂
استوری سردار آزمون بعد تساوی منتخب ایران مقابل بلژیک ده‌نفره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/Futball180TV/95082" target="_blank">📅 00:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95081">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پرزدینت پزشکیان شییییره</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/95081" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVZppffQVzSptH-SBznow6armIX-FQgC5NLmNM0Nl96DqupUAVJClIUozDuF1El6RJ03Vr_n0wuS4_RIU3pn07w4MCHY9iyqPmqRkRJgNzhw1rRYuAnJm6_cXwyU9G2klswwZ5oIMgJAF1Qtg2jWDZBCyCa6Qg6vt_C3HL9x_SptXKFdc58AnF31I_vF5JF2Rw3sA_YGlgRuyoPO9vt1k-tnZaEJ1STbVfF-9n8-c7MbKM_hxsO7iSCPrqScEKdO1veT-3UI_kGMOLGIbZ15RuNFXXJJ9aReQ6qhKoXDsoDb8ADJ02b7ijelJlMiImIuEeynduMBx67xuO71x4PFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آمار روملو لوکاکو مقابل ایران:
- دریافت کارت زرد
- 0 شوت به سمت دروازه
- 0 فرار موفق
- 10 بار توپ را از دست داد
- او تمام درگیری های زمینی را از دست داد
- بدترین امتیاز (5.7)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/Futball180TV/95080" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/95079" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/95078" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d7eb4f82.mp4?token=tXfqL32P1OCKO6mfrWpCEWWQ3G_0j-fgYlzSCHBvcyjhS2AVhkBhv9-nxz0tY3ttcUhuqPp9AJx3bx8ahzvbeKy_S5AepbIYkDIqcdzWBW6lY1MB_WxKwpDcqCchVHlF3Q1LUpiuaRYHMjdC1TvFKVE_rUOijCn-n2U4uCAzp_dN0hRUXtxDC8CDnaUM62yclpTWzVjDLxHJ01eVhnOSOw-pfd7hLu0B4enT4hnbcXPEykz2nbNlyndwN2tFJ8Pd-flzS4AJzKjXUeo_B8IzebqCU1TdJnVb6W8O2BZXPquhYY30nRU_rujX1U4wfInxE1Un080caY9m2XDdWgbLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d7eb4f82.mp4?token=tXfqL32P1OCKO6mfrWpCEWWQ3G_0j-fgYlzSCHBvcyjhS2AVhkBhv9-nxz0tY3ttcUhuqPp9AJx3bx8ahzvbeKy_S5AepbIYkDIqcdzWBW6lY1MB_WxKwpDcqCchVHlF3Q1LUpiuaRYHMjdC1TvFKVE_rUOijCn-n2U4uCAzp_dN0hRUXtxDC8CDnaUM62yclpTWzVjDLxHJ01eVhnOSOw-pfd7hLu0B4enT4hnbcXPEykz2nbNlyndwN2tFJ8Pd-flzS4AJzKjXUeo_B8IzebqCU1TdJnVb6W8O2BZXPquhYY30nRU_rujX1U4wfInxE1Un080caY9m2XDdWgbLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
😆
😆
کل و هوراااا در پخش زنده شبکه سه پس از تساوی ایران مقابل بلژیک
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/Futball180TV/95077" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ دشت یک‌امتیازی منتخب ایران مقابل بلژیک سردرگم و بی‌دقت؛ قلعه‌نویی با بلژیک ده نفره هم موفق به گلزنی نشد
🇧🇪
بلژیک
😏
😏
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/Futball180TV/95076" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95075">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب کم کم بریم برا پلی سالار عقیلی تو تلویزیون برا مساوی</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/Futball180TV/95075" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95074">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q67j-J-6uVMUu9ZnS32eWTB0TF6GdbbGqAi648pvb6SJ7LFxlL27nR-9lNcRQG3SHlGtJrI4-EJHvDhr1vJ90qXRChplEi83YbXGHo_32JrpBBLk-RF4MV7dcsX_R7q26bz9ZlMp-vyxQ8UKYjHX-zwIKPcguMWni7CkkSsrXwRNt5VCMquGYpJhbCf2SBrg2MuOcMGaNDnJ3VHOrZzNYvuGLKZvgMbWsyqsuKjgb2YffK-LZszXMCwriWjo2ioiGSNXqcp15aZE118u_xX_VnYRdi1FWfV6Le4HfuBVQQti_xAzxA0qh0yCeDQ9rcSpmpte6t0isYt_YYIWgHBwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ دشت یک‌امتیازی منتخب ایران مقابل بلژیک سردرگم و بی‌دقت؛ قلعه‌نویی با بلژیک ده نفره هم موفق به گلزنی نشد
🇧🇪
بلژیک
😏
😏
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/Futball180TV/95074" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95073">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قلعه‌نویی از کوووون آوردددد</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/Futball180TV/95073" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95072">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/95072" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/95071" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">علی نعمتی واقعا کسمغزه</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/95070" target="_blank">📅 00:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/Futball180TV/95069" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چرا دفاع میکنه تیم قلعه‌نویی
😐
😐
😂</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/95068" target="_blank">📅 00:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترابی جقی نزدددد</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/95067" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95066">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/Futball180TV/95066" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دیبروینه هم کشید بیرون</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/95065" target="_blank">📅 00:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">از کون آورد قلعه‌نویی</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/95064" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95063">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیرانوند چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/95063" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95062">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/95062" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95061">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/95061" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95060">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قایدی رو واسه دکوری برده اصلا بازی نمیده</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/95060" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95059">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عزت‌اللهی رفت بیرون
حسین زاده اومد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/95059" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95058">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">موقعیت بلژیکککک از دست رفت</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/95058" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95057">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/95057" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95056">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کورتوااااا چی گرفتتتتتت</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/95056" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95055">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95055" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95054">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بلژیک تو دفاعه کامل</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/95054" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95053">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فردیناند هم تو ورزشگاهه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/95053" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95052">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سناریو صدرنشینی تیم قلعه‌نویی عذابم ميده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/95052" target="_blank">📅 00:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95051">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECOck7h-vNJHgA1auy-ZieWIQQcdG76iy1_fNRPEDSWVdtPALAVX8mBA0Wm0bAiMYramfYPotzj4sDPo0o_q91P4yxoBZeMIFY327FgLsioVQj68h1BdWRaVqhTc3jw_ahhIkHk2aDaG77GIxQLqD6J8F5fJfYQJF2OUzTGrGEbMRdgajJcyXwa_dJJGj5EXExCbqwJ9x_m6yO1bze3P0LWyl1utRliVNQLeW7YKDHjraDI4qKvIUwQZw-pC44zyCAioPRRjsfcfOBTPh8YIT-ffsuWddUwOctBSFAqSD64uHGESDfpOgj1UJl9ovvg13rS9KB5QHpV35WK9NMeIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🏆
🇺🇾
ترکیب اروگوئه و کیپ‌ورد؛ ۰۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95051" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95050">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فقط و چوب بهتر از بازیکنای بلژیک بازی کردن
😂</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95050" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95049">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">لوکاکو تعویض شد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95049" target="_blank">📅 00:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95048">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr7-RrTar-SFrpRpWTil2pBm6PjiQ5S4KLgMz94tWezxZpo0WWpC5FskTDOFOVlTzP6SYN1Ob-V22QAd_sKQM1SHFQMxDBAqE1Z6H_8RBmc4nfbae6d4u6iSGteXTIF7oOSv18exiwpAgu3wBKf9CEBa7UKxyoUUDbCU1OR9crbQecR8A3yLxGB2Kbf1qUdpqfx3_tXN56DK94akRqGQ9xHCcFkYyyK0Vi1VVq5dEHQspeIXBDpPUUXoy-iKMe9duhHMPFZI7kRkuINuGczCwcM9yYKODiWkywo8CQRlOkQeweX4P1FOMkEQ3fq6LIKLunYs3fsR4g7YOotu4jZ7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفاع بلژیککککککک اخراج شدددددددد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/95048" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
