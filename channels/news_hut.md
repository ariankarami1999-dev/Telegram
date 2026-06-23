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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 00:41:14</div>
<hr>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=Tn7ylaltwuJWk3NFPirEk8IX8NnwFH3XBq7Bc76bqMmUZ13nurOujzteifi3JOsBr0M90PxKA2zN9FnD2fEQOrEa3hw-whUd1xcUEpYnWV-G8Jp8XAoEWt3E6Nnc2IpGowT0XkZbd4SCF7puXF4nXmuilOqF808ZtwsWxdeuBOEli08cektP-si0O6dKp1BHps9zIsRR-bOcsyAJpg6DNFq6xKzGgGdOlbl1yFCUTr38e0J513vK2dfMW5slBNpk48ClwqIeXE8kuMm-Qx64Ct8QjyhoEsNTIm8PDM7sGjV_DTSR1_Qc8yL1wK2Cf8rpsEhVUT8xcgxWlMgAT-ecAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=sa3SZwnGxFsgucLJpb45c86AcBiuC18TRHF6WD8nk3noLF_pJcy2OR-NXyFkH4sPqvIUpJOAC1EXD3_un1z54QvKDz2DJlDe-lX3OgzeFjxmAfKhpZ4AeLLvGAbKMtdWa8QW0vz4gVUKolIG5wPVzk0Yh9y0YQpJDfWhXZe8aZT25QkNbQKdnR5soKXhTbF2gGwb8fd5Qf9ma5zsyB7H_rRlyCxY3NdPd3miWTTlfr5x6BH3ODuUFTUVmALmq_NaknE-JCShGPeDRT4_fFqt4wKPm5r_T78ncKcF9LljeySDm8drkbzgUIVdiBGlsOwieGqhuBYjlxoW0r3X9bXUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=gC-Q1_op8B-TKcwdGx7Hz0uTx593IQDQ01_qWnhm0dCJeyITi6bqLP0HwEjZUYztg95AU0amrb46XrsoID-Sy2vgxd-wBmksXJMFq4j1Gre0NLdtzMJ663oXQHg6EaLPlL_MmYjiGgcQXeFJ4cVRXmyLMylC3ML_9lfUcVC7k9Hrmm5ZzAXUU2GrOEqX9qbQGFazIxiihiN7JyQ_qgmlPk61GzLkGwTq2qp6OkMCzxSWHFSMXlthlEHytX71cEVgr_0gm9Dwbw7cIMwaTsPKI1RP6KhRFeffHwWXP2jNW1d-ZaU-XilcvNPOrL0TtB7Yd2obYaIhr2KyIN8u6ma1bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve7P93zhgyCbzKLF-KHp3jc6kto9hMd9H-eEqTku5rmrhVQm9CiBkgmbkvIF_UJJB2yJLXEpo3HfZfi8_7qALz60J27Kv8arP7mjbYCZBBWnAQR9o41TaefH9_AhJ1M6Z6U77p6k9AYJBVs5pdYF-YyuRGb62-5WYdJTQ9zC9Q7KNaFR5NUg772oynKPbgU37kIYY9b60mEPy43_CBZwV7SmPLUvtzsCOkEsZ2fvHPQ1lPxGjNz7ClMTJdSRbWp-q2pgSpULr4CqTtkAee-0XJdygfsDy65oOSM8wepkkBd0vqblHK47ghK0FcMrR7aSlr2lYGwgrLOr5erZRMWkiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMzliEQINyK0rc6nS_kzPQlNY1f3JZ3HoxNWll-vU__F6j-5Bjh3WSKmbIyccxHriJd3KhOVXs8tGRmxD6_cdtqEbdXDUP6TADNKOPf_jsflt6marIi3Kmaj3gVzbSUPsXqtFp2wjZjFFpLyBG1xnukATwkZo9s6pWjgTwJu41IHvQppt5WZauYX7HRmnM0hpsFAR03_x1dLUdm5zDL7CK5QC_XGvoCvxIunMqekzfMMIAFARUrPFsoynW497643ZbaTtqjk56GkOO6rK1EE-wkeGyiTsxJtU7_gvaRnzz-Ov1EqrHuRbot7mbFp0ijOOSeRKanD6YezeyAQCaoFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCjAD2IkWHJ2rOzGRvoIoeNCwl1Ty9rAee4S7qxGxfSBQQf4B3h9hAiFQLHzWy7FTY8JXkJ-xVwMPatLVfpe5FGKQQsmdEhqkGolpiZS5QBqKnjOqqcKnbCLuXwXGnvYSdA69BoAqNAPMnGl-6mc5IYISk9CmWSB-ciabch28SAULLX-ypIgnA_TtRelmOczVCRl8F8064tN6f2sdceBY_Wth_MhHzE6VkK9Uizr9gKi01SZ7dF0XygoIDbtW5m6zqm2J-n5XZPKD5NhHisRki9Ad7TyWGodJD_IbGtkS8gj15MqQz13kI7hMHPrR3-laOxxzAcUtbuWlALb_oOOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=dmhMIv4Y183I5Jurb7prd_KXHW8QGTvvqJ3ryE2w61eed9ce03MkYMTbYPm7hGvy2b4e1iOpFAU1Oqk-h2N4P9Ua8xSTmsNsymM_R9iDsyBpiiu0pdUvC045sNVZ_l2_rCVWs4odm7Mtm7vLfmYrP8sTeg19dNdb3BlpG7fUn9whBPyY825hb2TsG2tqyy-7AquDiOVNJGN1q8DGlzjFip_r1zyMIa1Uf1RHuS5LRtaQueuJxZUih-hPh3a6hqxMt0PD0ndV8JNnE8OLKghriRaRqd5nDfn7g2jg0suIYGq9gFor3oCiQ7Qlc1KgdRRqvb9I5adxrLjce_uoTCbJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=dmhMIv4Y183I5Jurb7prd_KXHW8QGTvvqJ3ryE2w61eed9ce03MkYMTbYPm7hGvy2b4e1iOpFAU1Oqk-h2N4P9Ua8xSTmsNsymM_R9iDsyBpiiu0pdUvC045sNVZ_l2_rCVWs4odm7Mtm7vLfmYrP8sTeg19dNdb3BlpG7fUn9whBPyY825hb2TsG2tqyy-7AquDiOVNJGN1q8DGlzjFip_r1zyMIa1Uf1RHuS5LRtaQueuJxZUih-hPh3a6hqxMt0PD0ndV8JNnE8OLKghriRaRqd5nDfn7g2jg0suIYGq9gFor3oCiQ7Qlc1KgdRRqvb9I5adxrLjce_uoTCbJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cliyiQtJeDtrvxNodcO9ojJCC0huLxON1ikWOmOOlr2SC_rLwAsrl4GI0Heli_oHUQSv5pU7F4hpBseP-R_pudeJYAvOcAUDFE1pRtFOwu08DMcVzY6WV-L_f2C9CFSulul0kb7ULtddmp_QQ-w8vrlYpiX6iIIcj0tFhOBIts_H18LYsB3wvInzBJlmrGMdd0VSH2N7Yon3KYAWRhMVuNm-tad8Y_V9dfPvrXeNYOB3QQ1LGWRMuPI0wa8tYhnWWk7E061NkVeGHF4A1wLDBW_NrWB_v47xiZvQSsPUtvLrBMoCd2v4QqvRtobMLhm1r9tfYLnSLIy66X5W14SDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HjBN8Vjdtfv6OSk5UVlvcZ3wAA1YIRFUgB6EDECbgu27S-aEDIt8oCe9nPtWbHvrFBVl5tRDDSnFSIDVIZ4hic0yE_1M7LwT3-MMj6ANxZx0yErEIpUMyRqrzH2EhB5b6E3NTK1l2Q8DyVAPZsktzuj8ZHJ3yKsa1m2wPBLhGTtHCwswTmREcY8A0EcMQjsNOvDdsI3juA-spMkJ9MBCGRS8Wzriqlk8CGUcQkE-rpFnCFI5HMHaNbyLzGH3mXJt2R2cJnZVkeKs1NY8CB_NxlKRN_jOjVuv33rTV68d5epZ83JUgqBizxNR5TuR-GXdTBROjt_HPUn_aoIfgSRrvR2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HjBN8Vjdtfv6OSk5UVlvcZ3wAA1YIRFUgB6EDECbgu27S-aEDIt8oCe9nPtWbHvrFBVl5tRDDSnFSIDVIZ4hic0yE_1M7LwT3-MMj6ANxZx0yErEIpUMyRqrzH2EhB5b6E3NTK1l2Q8DyVAPZsktzuj8ZHJ3yKsa1m2wPBLhGTtHCwswTmREcY8A0EcMQjsNOvDdsI3juA-spMkJ9MBCGRS8Wzriqlk8CGUcQkE-rpFnCFI5HMHaNbyLzGH3mXJt2R2cJnZVkeKs1NY8CB_NxlKRN_jOjVuv33rTV68d5epZ83JUgqBizxNR5TuR-GXdTBROjt_HPUn_aoIfgSRrvR2xIYCRP3nrgugEsga8RgqD-jbUNZEWWuK8ewpjSw55iDFLno9jAoxC59f1H2iKfGOPB00dMAM39uRMzj1SHzugq3UJy3Drbw5Tj819WVK01yqh0Eh7h6FS5h3NfLCK-qfu9BPpi6Y4MxCVnxyeBK-lTnGJZAcp_L0V_dHiV2d2cI26RxGIJzXG0YzedsM9sD9y5IjmCpEDXaXij9eXOLOyyauLyCQpDPG6SXpK2RF7tsI48n7s9vnGCJ_tbn2YDyYkL_5mj0hrIaxcm8fq_2B7j7HS4ZtEehnZitdUPUxLe75Km2HcGm9Ky6ujpXigFcGVx3oCFztSV3-In0GbY78" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=e-r-sP5vNkoIKhFrq54oADfN2SEfucOQZEmjm0hcp3XEQT-QarsseDOKg69DWnoSj7raakKn90XaLTPURMUSWwabkMZLk-bGep2BJCDmS8qEwV5Nxq_Kz_E3Kwf--3JzeGG3ntJb5l9vt0B4DKoi3SRPWYYOovZjGahp49n0yuY644bdLrbSnuF5_lGqGYgjusxfz-y6m29l1nck9UEWIgiFiTQfRGBjelek1lKMO3iV78ijQ2s47D1iYiW6YnKYpqHe4oczFLrO17EJJEe1K5NroBiyegnHrMFq2BVakauhDddV89EwRaaCsP_pdO_uGOFAH75TXwUrLAGPGhmwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=e-r-sP5vNkoIKhFrq54oADfN2SEfucOQZEmjm0hcp3XEQT-QarsseDOKg69DWnoSj7raakKn90XaLTPURMUSWwabkMZLk-bGep2BJCDmS8qEwV5Nxq_Kz_E3Kwf--3JzeGG3ntJb5l9vt0B4DKoi3SRPWYYOovZjGahp49n0yuY644bdLrbSnuF5_lGqGYgjusxfz-y6m29l1nck9UEWIgiFiTQfRGBjelek1lKMO3iV78ijQ2s47D1iYiW6YnKYpqHe4oczFLrO17EJJEe1K5NroBiyegnHrMFq2BVakauhDddV89EwRaaCsP_pdO_uGOFAH75TXwUrLAGPGhmwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=Dku5zEvnHh-SSikZHc-pH5hjzleO34EFKybUqVSchFi0c_OuerZdqDo6hf-5DhIVSSFBId_zQel8XDQ7JLbxQ8ZjD670NY17fF5LUqkeoHf7NbkgWin-GHyiO5CNK7YMIvHFxjeU-N7EKrKGzhuZ3NYr3CF5BgLZVx_qjlY7SGy6Fm2MLyU9e1nd_o1azS4VG-5di9QErDlhX4NQFgB0IXvVlwjZcccBm3j-xoIr9-KFZ6xrN389bLcxZtYSZnFMqNI4F91rHMWZfn7tAqgnvIoSlVvz-XthdUngUCe5KOnOKj7AsnfqU-wlByPpFZJkr7wK2I2Kk3r9EwWIN-qJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=Dku5zEvnHh-SSikZHc-pH5hjzleO34EFKybUqVSchFi0c_OuerZdqDo6hf-5DhIVSSFBId_zQel8XDQ7JLbxQ8ZjD670NY17fF5LUqkeoHf7NbkgWin-GHyiO5CNK7YMIvHFxjeU-N7EKrKGzhuZ3NYr3CF5BgLZVx_qjlY7SGy6Fm2MLyU9e1nd_o1azS4VG-5di9QErDlhX4NQFgB0IXvVlwjZcccBm3j-xoIr9-KFZ6xrN389bLcxZtYSZnFMqNI4F91rHMWZfn7tAqgnvIoSlVvz-XthdUngUCe5KOnOKj7AsnfqU-wlByPpFZJkr7wK2I2Kk3r9EwWIN-qJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=owK-i10cAEN09HkSvJpkxiRah9d5KorI-o938Vg3ZAyWWIbq-wEJv5o-djzBAkaB8y19D_RP81o0WzxBwqTaiAWiErLH3DmFTnSHmhNypjqmD4GyQxYL55-Al7OuI6jI3mWYTsSQNu-UtxHBkHCCpiahFZ-0p4NkqQLwffUd_EAd3InCUVd1PGUuh_fC06FL5Hb7eFvuJDqWwebtdhVai8oXplV6bhdLgCeQDhjjH7bEDhYyqQrTh4ciEPKiituLhg2x9BIEM_dpZ7BoEdlQ67srOFAzqOZJTZ_MfpDEI7KwbF7yIymwEgaGpryDhxiZ3oVd2b5JcG84_dSDXV9C8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d36c0712.mp4?token=owK-i10cAEN09HkSvJpkxiRah9d5KorI-o938Vg3ZAyWWIbq-wEJv5o-djzBAkaB8y19D_RP81o0WzxBwqTaiAWiErLH3DmFTnSHmhNypjqmD4GyQxYL55-Al7OuI6jI3mWYTsSQNu-UtxHBkHCCpiahFZ-0p4NkqQLwffUd_EAd3InCUVd1PGUuh_fC06FL5Hb7eFvuJDqWwebtdhVai8oXplV6bhdLgCeQDhjjH7bEDhYyqQrTh4ciEPKiituLhg2x9BIEM_dpZ7BoEdlQ67srOFAzqOZJTZ_MfpDEI7KwbF7yIymwEgaGpryDhxiZ3oVd2b5JcG84_dSDXV9C8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور سر زده ناپلئون بناپارت و درگیری شدید با شیر تعزیه
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66713" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OCdz6OWQkOMf03om0_PqD3zO39G5ff9mMFeuiu0Qg75EoyyHtBjXk-eHOrJkE0C4BeZosNAutViB1xDcW3-LlesXT9gejMPuarQfAxjLuT2zitKN-CgpB6o8A-G7-F94Z4WdoI50FdMPY4DJiVrKIuFylJKXjSMhNma9QVI7cligl7chE3Pizp-a8igBzfkodfg-IpKqc8u-f1KS2ASqVxVcbymT9fHxzhOgXJJXR5C_IUZ-VwlSREjrohakRVMmq0UP9TNshGDGnNbDBMlwQQUSVEUku8qnT2lBcrExAr6ghhnKkQacYFBHnrJHmVjhOarDaXMO9acehDHAw-4OtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312bd6815a.mp4?token=OCdz6OWQkOMf03om0_PqD3zO39G5ff9mMFeuiu0Qg75EoyyHtBjXk-eHOrJkE0C4BeZosNAutViB1xDcW3-LlesXT9gejMPuarQfAxjLuT2zitKN-CgpB6o8A-G7-F94Z4WdoI50FdMPY4DJiVrKIuFylJKXjSMhNma9QVI7cligl7chE3Pizp-a8igBzfkodfg-IpKqc8u-f1KS2ASqVxVcbymT9fHxzhOgXJJXR5C_IUZ-VwlSREjrohakRVMmq0UP9TNshGDGnNbDBMlwQQUSVEUku8qnT2lBcrExAr6ghhnKkQacYFBHnrJHmVjhOarDaXMO9acehDHAw-4OtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66712" target="_blank">📅 10:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=L8tUlGBz1BBaJRFncf_b71SCNbiWsb9dYfx4b1hEhsZhk6mi6F0M6pfuExSgkMKnPjYrTH852gWAHRmsD7UnkY_06gG4_Z39jaPsC8ei_raV7ubGmXcc-7VQsW-UhCzannx63dmCjThcEvV3WD4H93lEJqebL6o4VP6t4Vc7aBU1aIwul_bvbD249xEEzM3B4WWVEmHYysORfPwCHDh0VKDocuJgJZYui-Wz_2Fui4pAHNk6bCX49pRL_MZZfMmxEKtmNpGUrWgpnwZM1_H8LS5LvJf6Iff687KrNgDRbvvSN6SO3lS6vkyCCQZlls1-nP0YDxsQ9_beM8My2et6MVs2Oj0hYER0gvlQZbSgKbmt96pXMqY4QqXGWqeQBQwNARWZ7TBHaua6ShwvX33L4JEPY__MCrcGkCjQGsnN16AFx1wMG1X5izk1U5zM7GWAXyilIOPrILxMf_K-fItBBEpX24ZfONJnSrfo6BBTHBwDxx4u2R0jZd0X4z9XHt4cTdNn2x71UkF2yJGxiyeaCwvpY8y2higrEZRgwQ3R60yO2n7u0Sa7HydARAiNn0HJCDRCnyXX30Jnkt-fcThwIwCONIpkak0gKzf5wbbe1q2kLfGb0s7bpmZuPuRekkQ3EmoQHjaZnWbVXtig3e11odxoj0pSF4Z_5A4xBBg_XpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0082fda5e1.mp4?token=L8tUlGBz1BBaJRFncf_b71SCNbiWsb9dYfx4b1hEhsZhk6mi6F0M6pfuExSgkMKnPjYrTH852gWAHRmsD7UnkY_06gG4_Z39jaPsC8ei_raV7ubGmXcc-7VQsW-UhCzannx63dmCjThcEvV3WD4H93lEJqebL6o4VP6t4Vc7aBU1aIwul_bvbD249xEEzM3B4WWVEmHYysORfPwCHDh0VKDocuJgJZYui-Wz_2Fui4pAHNk6bCX49pRL_MZZfMmxEKtmNpGUrWgpnwZM1_H8LS5LvJf6Iff687KrNgDRbvvSN6SO3lS6vkyCCQZlls1-nP0YDxsQ9_beM8My2et6MVs2Oj0hYER0gvlQZbSgKbmt96pXMqY4QqXGWqeQBQwNARWZ7TBHaua6ShwvX33L4JEPY__MCrcGkCjQGsnN16AFx1wMG1X5izk1U5zM7GWAXyilIOPrILxMf_K-fItBBEpX24ZfONJnSrfo6BBTHBwDxx4u2R0jZd0X4z9XHt4cTdNn2x71UkF2yJGxiyeaCwvpY8y2higrEZRgwQ3R60yO2n7u0Sa7HydARAiNn0HJCDRCnyXX30Jnkt-fcThwIwCONIpkak0gKzf5wbbe1q2kLfGb0s7bpmZuPuRekkQ3EmoQHjaZnWbVXtig3e11odxoj0pSF4Z_5A4xBBg_XpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
دیروز یه لحظه بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما هم دست ندادید و بعدش رفت. آیا احساس کردید که به شما بی‌احترامی شده؟
🔴
جی دی ونس :
نه... باور کن، من چند ماه اخیر رو خیلی با ایرانی‌ها سر و کار داشتم. بعضی وقت‌ها واقعا برام گیج‌کننده‌ان به عنوان مذاکره‌کننده
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66711" target="_blank">📅 10:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66710">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66710" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66709">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66709" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66708" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZPkT5iOH0T9QD6Gtn6_IcM42sNGScCfy32HSx2Hx5vZDG9a_KrFL6aUF_zxQtrO_voeLIkj6vnCoFvpIllpJ5K8GdINBgV5ZNQLcU05BM4osrmibdaV1moNk4dWhgNUPdPQPQAHtAL4nrtJnQqYCKx-Pn1UNbD2oq9jvisYNk-lfRcR_rjvo8Kxzu5dlruTzXBHUjZkoZmLfWz5sFMXnSjy8PEO5rLeglzys9kvSw5I1nnQoo8a7K1vVO_y5fJGwwpsRRx9sae6wLiVls5f3auhcwu62GF2tq_UVBrYfZcu78immAFoqWOY0PCbsPtMUVU5WDTK5zqXCz_pIrf7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66707" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=kYJUvk1l82bHBGE-PMsxbN_x86P6rzKlKoKUeMzxAnxYBEs2IblMafnFZmoX-qCZfcGPguZsTXRejj2qWnKAeSSa7vu9GC9v_9wr9K-EQZ0jzTakfT0ZuFEPADOr_NU8ZhGpRBCkHqoCioGceK2IvnRLjbn2R_HQIyrSqrNmmmYDC2l6cW46BcJhXQYoGijwUkLpjAEYNkDW7ZxeZCsJfMlwfEXKr9Yz9jzNvdMeUkqQ9uFLEWjEM6cCC5zMwXFXtU-nJod5X0cOQd-T-fz-9Z8yS4gJPkK973ah9UcXE80wvTCh8yTUG1ImEIOyQuDSCnqyJspyh-wF8AHGC3so3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299b9a2567.mp4?token=kYJUvk1l82bHBGE-PMsxbN_x86P6rzKlKoKUeMzxAnxYBEs2IblMafnFZmoX-qCZfcGPguZsTXRejj2qWnKAeSSa7vu9GC9v_9wr9K-EQZ0jzTakfT0ZuFEPADOr_NU8ZhGpRBCkHqoCioGceK2IvnRLjbn2R_HQIyrSqrNmmmYDC2l6cW46BcJhXQYoGijwUkLpjAEYNkDW7ZxeZCsJfMlwfEXKr9Yz9jzNvdMeUkqQ9uFLEWjEM6cCC5zMwXFXtU-nJod5X0cOQd-T-fz-9Z8yS4gJPkK973ah9UcXE80wvTCh8yTUG1ImEIOyQuDSCnqyJspyh-wF8AHGC3so3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت‏ترامپ:
پولی که از حالت مسدود خارج می‌شود برای خرید غذا استفاده خواهد شد و غذا منحصراً از طریق ایالات متحده از کشاورزان ما خریداری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66706" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66705">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66705" target="_blank">📅 01:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-XoIS_pbsgGs6ASTn1IjBpe-KxjXseeODIGeeGb5JZZq2VhVSUGCC1W-ZwxgF2xeteVF3_5UKrynzbivP_GD_LwegVzNybNHhThKVhiIjlmjp5PXZ6NgV05Qf3Ca4c7kE6XXKpCWr4pOVfd2jQe_Ema63QYhK7HIgpnZ6nQbWuFF9jdbcnF_5x3FEHeJ5JGdXnY3w6jDiCkioViKjx6rQWOy87Z3ansifr1r9vSPjqXxNv69YTabikv9NFZ86vDB2-Qd3MJLl7_Kc5S5mMkEjzW9Ta7qm-OzYJx8cGNuhdy2J8K3T7rCJFrivhOmrFyy_lOaMNm_D67rC9mm5GXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
قالیباف: اگر به سوئیس نمی‌رفتیم خون بیشتری از شیعیان لبنان ریخته می‌شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66704" target="_blank">📅 00:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=tVqfs_He1vDDAKNcAhsQ8pwkrfq8cwKy0hRlICj7OMvwtkLC7nTANpzeBY8b2mD9qzIbb4DyxNU6mQLGKbs2TX85lwLzymZcGT3-B7tg7lv_iLov60FZj6RTNuGcOfTprMCfnIZucg_tP9rL9jddV_cUDwfMujAgS_Hdlt4XEaZ_rk9pi4wDitxy_0_en5hDh2bxVRk5jI6VeskGMS0RyI6y2LcLLlQlJQtTQKT8l33Cn7XNPTxm-WOfdOCQ-hM9-yFVqaH3vjMKyafDJj7Si82AAQVt6D39lYWdtoF4jAksh4Y2OlhUIar4Ulj64b9bfnuaQG66xbvOF_tUP1Oajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=tVqfs_He1vDDAKNcAhsQ8pwkrfq8cwKy0hRlICj7OMvwtkLC7nTANpzeBY8b2mD9qzIbb4DyxNU6mQLGKbs2TX85lwLzymZcGT3-B7tg7lv_iLov60FZj6RTNuGcOfTprMCfnIZucg_tP9rL9jddV_cUDwfMujAgS_Hdlt4XEaZ_rk9pi4wDitxy_0_en5hDh2bxVRk5jI6VeskGMS0RyI6y2LcLLlQlJQtTQKT8l33Cn7XNPTxm-WOfdOCQ-hM9-yFVqaH3vjMKyafDJj7Si82AAQVt6D39lYWdtoF4jAksh4Y2OlhUIar4Ulj64b9bfnuaQG66xbvOF_tUP1Oajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=pQyMimbQGKgOc7GKGGh34GX_98N0gwQFcCkxHl-09Tqo0QZcfqgX7mcAD9VhuZJAoPjgLVOzpoPuNa1FbMv0YZ8ekuLSWFK9R23wfbMwqzypgRrU-1uF2tuwIvIVB1pl5fDiUMMClMEVPLyZi95E5ZVqPt7D60GB4C2F2-JUpzsuTyQzos5n2xQ0KNRYPjMDePQse56zOBZ5WQzzr588HhN6td3cqFFPu8hEcFS70-TkHTSZ2L2R2r1JVDVYPiOe5AAZ3SReUT_qwWygvT9cJci2prUnoMNUXbw4T26OjPNLHvDYoN4ceaT5dUubcSmZbCxdBgrJi3KVKMNUPveRvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=pQyMimbQGKgOc7GKGGh34GX_98N0gwQFcCkxHl-09Tqo0QZcfqgX7mcAD9VhuZJAoPjgLVOzpoPuNa1FbMv0YZ8ekuLSWFK9R23wfbMwqzypgRrU-1uF2tuwIvIVB1pl5fDiUMMClMEVPLyZi95E5ZVqPt7D60GB4C2F2-JUpzsuTyQzos5n2xQ0KNRYPjMDePQse56zOBZ5WQzzr588HhN6td3cqFFPu8hEcFS70-TkHTSZ2L2R2r1JVDVYPiOe5AAZ3SReUT_qwWygvT9cJci2prUnoMNUXbw4T26OjPNLHvDYoN4ceaT5dUubcSmZbCxdBgrJi3KVKMNUPveRvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=P_lSPUvS_5bI5sDx7RuZECOznUI11T6TrnUVvqM0SF_b2kDHxWWHIam86L9sqKga9YqHJzePcX1LF8NCpoQX9yvIcYoGuCQLcB0CpPCykVlRkJAE51gxh2vLdvFp8t2VRnneC18xFwlg2klbh0oKrR4xkVNPu_fx7Lpy_dwvg8lBLK13qG6hl6G7jZWybaydPTqpjJK3vEO8AP1wDkZY3Do11QQmBtbfLHK1LGmnRmRpmUepb9t58JNgg3prLldxcj99g3IP0Efb8IsBAOdqiBTqIzwVwwnKXbmajkAyZPnQVSnqX3oOnAUHy7DARH9CfjJcExQRZaQfphGcy3DNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=P_lSPUvS_5bI5sDx7RuZECOznUI11T6TrnUVvqM0SF_b2kDHxWWHIam86L9sqKga9YqHJzePcX1LF8NCpoQX9yvIcYoGuCQLcB0CpPCykVlRkJAE51gxh2vLdvFp8t2VRnneC18xFwlg2klbh0oKrR4xkVNPu_fx7Lpy_dwvg8lBLK13qG6hl6G7jZWybaydPTqpjJK3vEO8AP1wDkZY3Do11QQmBtbfLHK1LGmnRmRpmUepb9t58JNgg3prLldxcj99g3IP0Efb8IsBAOdqiBTqIzwVwwnKXbmajkAyZPnQVSnqX3oOnAUHy7DARH9CfjJcExQRZaQfphGcy3DNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMzH4pEmJJ7IaPKbhUuawGI2tlT--BQ-Bkq_JRLZNIy21y5DxHMTY2oyjkYPqJMzbSZILMxtrqEEREZAyyEfls020U8lmfAVrUASY4yi2RCmvtFXX6GndzpzKx3Qw6NIoM_glLti8pDGooGWRZtELWe7Zk3KIcnY0bC1QEBzLcg_NGbj2cwKjeFTq8bNJ0QTfRssFWuy90OB4xLNSjBKabQWRe7bD9vLizvvoh8Ty7s2slwNtF-VzLrW_MbM5-amqzAB6a-VCfInEUKnEEHeH2gV7PfL3edeXPioenBnfcdSRb_QdxPqeyae7TnXhGOKb8zgPU4BUGiVFXK3UtL0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bejt-0JnXnUR8zfRCWZKawhqfqfv4gp9o5d7nVu2S3LLNIkuaPAKM2K04I0HCt9JvHqVFjMCAdSHKMKQ4Nyv7tb9ffAyvj0F-WIBKbwSG98wGfgfZDzCrcnsXbsTeghgBlmD5qAQPkL4w25a_K5rpRnT4aLZcWkql272QV6NMOE2admyhn7dMfVzfiksS0AAMEcYqjciQYdu_6w-5EXfed2RMClfldop-fKo2CwpX2uMu2YXBzbNIv8pGU_wnqhL4jhPj6hs11qqehgiwwxqWAkMuLSll4rb0S6oquAZ0KYh4EJqeHmOYEG9tUJvDQlhnOK1t2btbg9aO09MtSgOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTneGQJjlP_GxBSR6FBgiOFOamAvgbDVSYwVcINEzKkt5iX-sLM4N9ZQOKkplbLhrWdmCWMDgj7kicwRx3ocTyde1ssiS997zG4dlsNreayG8UkOhFcjOn4-r0j_Js56Xar5u87jA5uWBpN4Sc6JEHiSN401Q3wZVHouwDxEbcwiyjz2lMdScQ-EoTRpjQn5i_fH75BuSfCARQN0RsDZvZNC7QqHEu1N1aUObR3iY2r7qlwMgVBf8AcE_KtE57KROhq-prmy2-99T4rDitt3UKv85WTwkAeMedZBVtiYLIcrS1O5UXNGIFHLT1dSmvOlbiHkQ0OfOiD_y_yzXsDRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAFeDIb0a7MYz4_A82jgbK4-bR6dx2arN3yigWBGQErVZlqIjzy_vHha4LiLdrVsU-CVL1vNECVJf9vi8ZAqEFYWGG4ZJiEYnJpVJThkcb_xx-UrsFODO3_JCvQZeHpq2mXnl-VO_mXsRqAT4XtFprAm2TIwmOz_F3InRi0qwxRx86vmIMk1K0svNrWYXhRiHRqrfY2lgDCRA6YsAVkWJdqmGLYp5LzR29AQSuvAj8Hh-HXpszp-JWh_XOVsWtP20FxcEyiNoyIGQRQOqHjFSDRPz2lLSFAeabWwPk6HkDhBa1KD7wdX4R65jwIpgg3_g_rGYuwRlpcncEkuRvO4yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkrn-ttymHHzmakJKWeTGe22V6O9EPw5mLbjbmOOvVSCWc4cbtRAaMxPy35TDbYOwiL6I4xUrBlVPQQoQp5-NsjYwAxQVDcuXVE92VfVELHjXEuf55nfJ-U7DD1kHCuM4lnjY2eusZ9IY3retEy6g_2lNLM-eASeyvIo3vPIZPDTryuK50K9HGqvEHjSxIbhPTZTYdqpS1Spff3As1m1O4tQnUSRD2lH_UMUg7HxnMpRmng2fpkXnoU1UpcIAoXKivj1MLPYgIPcy9Fw7hgMy2t9pKb3ICyT5WmHIhSolKAzhzxlYQNG0Ooe_ypqUKdCyTQogKIeG0nXdwU3RaDR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLHfnxIm4hLr3-DY-7EeybH9t6arXr4PIGKBcEV5JLVNldkKi36aYriS_r0zfJbAT8VIMy-ABzJtjBuXVIWO7aSmYeYDNVwHjWkplcXu5HvF_5NeDyfwDSxYSEp4A0aRPaK86Yc5mPi4fZea3yegHlG9hJq-Lbs6t4SOpRMVKfNMfQkGW3Z8bLniaEtNp9m2dJR7oN-SbZM6FFmG_ezkogdNVgXuu3HQn1Kay3CYFsW15OoSuwrNlExDJeJUzz-dK5mfIbmxnMieO6G5_jGBDx317dQe6FPw26BGj3-q2eCdN9e8pu8QWDk3OSqwDvt7-CsIb_WAYLcnnwZdhvk8VeQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLHfnxIm4hLr3-DY-7EeybH9t6arXr4PIGKBcEV5JLVNldkKi36aYriS_r0zfJbAT8VIMy-ABzJtjBuXVIWO7aSmYeYDNVwHjWkplcXu5HvF_5NeDyfwDSxYSEp4A0aRPaK86Yc5mPi4fZea3yegHlG9hJq-Lbs6t4SOpRMVKfNMfQkGW3Z8bLniaEtNp9m2dJR7oN-SbZM6FFmG_ezkogdNVgXuu3HQn1Kay3CYFsW15OoSuwrNlExDJeJUzz-dK5mfIbmxnMieO6G5_jGBDx317dQe6FPw26BGj3-q2eCdN9e8pu8QWDk3OSqwDvt7-CsIb_WAYLcnnwZdhvk8VeQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=mBGyF8r767U71eDpVBBNuaLNPi_1kwI5LKM2eQortzHrB4d_h_Zdl-9VK3F6BaA3zevvzKpMcBlhlXruEw5SLJaH90UYicUytv9uCqB25y98UX0pb0btzNR2bsoAPQkDZmp8l3TvFLQVobZu-pbj48Lq7Ce-gxa4jemt5Flr93NMkWKcRHmg8eulv7fWEQXYOYObVmExx2c-UO1AAtwUqKTc-kkIRvjUmR7E-HYaJiSc4gtKXaB-HhH_wXYixc_ishQ3GgHJW2BhrI0UKZiA10yhrXmKSh4J0ggtlrJ4ldS3CIEROblg7EQK2jpHMbRogfAaIi1ArT7pEJHP-vKnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=mBGyF8r767U71eDpVBBNuaLNPi_1kwI5LKM2eQortzHrB4d_h_Zdl-9VK3F6BaA3zevvzKpMcBlhlXruEw5SLJaH90UYicUytv9uCqB25y98UX0pb0btzNR2bsoAPQkDZmp8l3TvFLQVobZu-pbj48Lq7Ce-gxa4jemt5Flr93NMkWKcRHmg8eulv7fWEQXYOYObVmExx2c-UO1AAtwUqKTc-kkIRvjUmR7E-HYaJiSc4gtKXaB-HhH_wXYixc_ishQ3GgHJW2BhrI0UKZiA10yhrXmKSh4J0ggtlrJ4ldS3CIEROblg7EQK2jpHMbRogfAaIi1ArT7pEJHP-vKnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=Rhu1RGuFM8JUAivWeZoslz6YXRblnoP_j4NRE_u44lYAuzwfyht1Bvr7iV2INRgpnvXX3kQn6IerVvEHpdutG2rSoZfgKfaI464d1Sox-NS3i8ax04s0M5lSv54ANo9Dw25aESG0vRieEOYBxWkkJqRz9rJ_xAp2qKszyJJYZueQN4VtJjBStCh5nwezcClzy_QyIm6hZYFFWygkx27Y20k68b2YMHsGuBHWAuc2UjjRc-Qz1ly0XB93KCcFFOHLaH-w9kYmAORLYrrSy6SuroDRCm-L-Vl-ltPbKZ2_2yK-y6gCQI00ke3tSYhn12a5_WkkyBdFBTo2y8dxH4MDIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=Rhu1RGuFM8JUAivWeZoslz6YXRblnoP_j4NRE_u44lYAuzwfyht1Bvr7iV2INRgpnvXX3kQn6IerVvEHpdutG2rSoZfgKfaI464d1Sox-NS3i8ax04s0M5lSv54ANo9Dw25aESG0vRieEOYBxWkkJqRz9rJ_xAp2qKszyJJYZueQN4VtJjBStCh5nwezcClzy_QyIm6hZYFFWygkx27Y20k68b2YMHsGuBHWAuc2UjjRc-Qz1ly0XB93KCcFFOHLaH-w9kYmAORLYrrSy6SuroDRCm-L-Vl-ltPbKZ2_2yK-y6gCQI00ke3tSYhn12a5_WkkyBdFBTo2y8dxH4MDIjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=hx8mhVt2kqLMwI8zvsKRuU7l7CR3-UYQ5O46IqrXwAkcTYqB9exK7BhDbGEhFGZ4mR0zuuf5T9raqrYmFabxlZjLE1eERRoWGoTL2tXq6mnp6MfHX9a5onRnlFuimKt_h-suJ7o0MEYk1n1h7kRpMdL4D3YppMbk2ynKjPa0eAHLR9fejIvfRt29YWhynyNbrHJWh6v_XSq5_arPdHJGmCMFyhD8HU3fohAhHT1XnE24swU9UMh92tjAc0jdsqMBnlGmHc235rGwkuVVDzCiOrZkZyIUI9VZ4ThWzicQj585ogM3cc5VogFD4oBp-93-0IelpqIGs7RRIpmMCEpbBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=hx8mhVt2kqLMwI8zvsKRuU7l7CR3-UYQ5O46IqrXwAkcTYqB9exK7BhDbGEhFGZ4mR0zuuf5T9raqrYmFabxlZjLE1eERRoWGoTL2tXq6mnp6MfHX9a5onRnlFuimKt_h-suJ7o0MEYk1n1h7kRpMdL4D3YppMbk2ynKjPa0eAHLR9fejIvfRt29YWhynyNbrHJWh6v_XSq5_arPdHJGmCMFyhD8HU3fohAhHT1XnE24swU9UMh92tjAc0jdsqMBnlGmHc235rGwkuVVDzCiOrZkZyIUI9VZ4ThWzicQj585ogM3cc5VogFD4oBp-93-0IelpqIGs7RRIpmMCEpbBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtfDruXgtR-HmxWlxoKm4eEY4sQYVTR9OCXXZfU_pW8TgY_GapUtDb5PEK7JyuCVPG-KRl95VaLS2IMpmtdO-8n2O-_NYgwO4EBp5GuVhzLL9Smm9kHIgcj1MNvxlPmIiAv16qiOmBughsxwzAKSwzqpuuDjuxdzwXzycIYA19PCdCvx88IQFf1HvY9nqVKZZYsbkOaPmWW1-aI3mrEFBOFnlo-QOwOhQFuUqlbHrTJeG5JHjID5j7A7_saUHFrbrvg0A0T7RNjr--hsV19-1M1hAzp3h4xW8K5NhdeyVWtRxkP8h5VStNH_gsw61KuxRQJUTk-W_y4F0Sgt9h07LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=btdq8ipNJbJ3rV86ZosmkoEdyVUnxouPN3pyK02bP7pbYHSTbneVhvh4v11nmxbn1YIAlvj5wIMJkNEO807hQgRKSIXmcSKgDYSZ-IpEWo35Mpg3-CE2ZVx2YZPgE64UpHoCsWtRkM77ipBzS29Xwvs_PsPSf2vEeU-iSC9AnhZUA_i7C-UPMcEQwidxgjypoTS6EVTnjv-cstjMWQF3i9xG4_tcNgrA4xbCEMNgSei0XH_9MJgfV7CfFB2csGxL5R0PrlHHPkBAvE8ojVq5R-dFsgTRh_1gJk21byS74rgVGqrOhTGiGfsUyczP8wX29uZUatHBurYPR5StBVRlyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=btdq8ipNJbJ3rV86ZosmkoEdyVUnxouPN3pyK02bP7pbYHSTbneVhvh4v11nmxbn1YIAlvj5wIMJkNEO807hQgRKSIXmcSKgDYSZ-IpEWo35Mpg3-CE2ZVx2YZPgE64UpHoCsWtRkM77ipBzS29Xwvs_PsPSf2vEeU-iSC9AnhZUA_i7C-UPMcEQwidxgjypoTS6EVTnjv-cstjMWQF3i9xG4_tcNgrA4xbCEMNgSei0XH_9MJgfV7CfFB2csGxL5R0PrlHHPkBAvE8ojVq5R-dFsgTRh_1gJk21byS74rgVGqrOhTGiGfsUyczP8wX29uZUatHBurYPR5StBVRlyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=lFIW243Dkbtu18hu1YrrhIQ_Tu6BlQf3qF9CDwoZkVr5f0F3AsZ4f5RXsKX9x_jJIEjVl5MuD6bZHs2z8HbUgDGGM_3YgNJR2cfmelg3jAigcQY5KC972z_pr69Br5nSH7SAyCR159zRFuDzMG0YsgutOIxWjM5tYi4qB9CIA4uu4-WMpnNi_RL6tYJx7ZlxFTgwlhHoU-9InPkWeOSa-nstCI57IrT96h6LLTZzwWh2O62xj8e71k5uNjw-lpkVI4ExVeh-5GIKieKCcaZJjwsIzpogzxcpt2N_Ga78Bb83aOmJpgwcIjnZ2z4Tl9Xg1eFKOuErJt9AvGq7JxlyCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=lFIW243Dkbtu18hu1YrrhIQ_Tu6BlQf3qF9CDwoZkVr5f0F3AsZ4f5RXsKX9x_jJIEjVl5MuD6bZHs2z8HbUgDGGM_3YgNJR2cfmelg3jAigcQY5KC972z_pr69Br5nSH7SAyCR159zRFuDzMG0YsgutOIxWjM5tYi4qB9CIA4uu4-WMpnNi_RL6tYJx7ZlxFTgwlhHoU-9InPkWeOSa-nstCI57IrT96h6LLTZzwWh2O62xj8e71k5uNjw-lpkVI4ExVeh-5GIKieKCcaZJjwsIzpogzxcpt2N_Ga78Bb83aOmJpgwcIjnZ2z4Tl9Xg1eFKOuErJt9AvGq7JxlyCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=JZ41p1cmEI3laipcLOthIRVMJO7pdyv_PstMY5CKnmFw2QLbiK4-eUf9sWeYcVFvPRRHQFjno3Nob41YcpCDzbOCHw1srlDY4Z2QaM_9LajKHl0YMl7EeQ9vro5SmW3-u19_Vl0A2-3dtHsKQw1QIDoCbUIKmrnid_-6BVtUBldFrrgR5LZHLlYjOMv0ZNqUH8ClW8BZ44WYsiAw38663gSBrrOHaEEG-PZ0JSpe1IGa-RGBwHCTEiXFtcpHRLXRzF1fsNjYPaU-eu0nV5hE-fkJqIPfiqjSzVT22QhLy7NcwctfiAMHqr7pejPdI9qeZNZnHEoUGaOiapya1hq8wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=JZ41p1cmEI3laipcLOthIRVMJO7pdyv_PstMY5CKnmFw2QLbiK4-eUf9sWeYcVFvPRRHQFjno3Nob41YcpCDzbOCHw1srlDY4Z2QaM_9LajKHl0YMl7EeQ9vro5SmW3-u19_Vl0A2-3dtHsKQw1QIDoCbUIKmrnid_-6BVtUBldFrrgR5LZHLlYjOMv0ZNqUH8ClW8BZ44WYsiAw38663gSBrrOHaEEG-PZ0JSpe1IGa-RGBwHCTEiXFtcpHRLXRzF1fsNjYPaU-eu0nV5hE-fkJqIPfiqjSzVT22QhLy7NcwctfiAMHqr7pejPdI9qeZNZnHEoUGaOiapya1hq8wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=JbDha_PC2NHHVr9Eb476eSCeuQ2gEI6oAz2hUQTLatHNIaLyjhlf91O3P8QLwP2miyxD3KsNKz3dbLAjT0Yk0ZNHNMT2ZAa_XDsHAWbV_INQ61EhFcMp7ClWiw3k-_Z9hbNH3OJp4paM0LxfL_B34X1mA-wEhf2lNJZMHdLy6jeb5HBpOsYaJvldI7lX7De_Hc7JXWAFA8pbdnycj1C7xfwiqE2qfJCWcvxUu3dewjtKrzd01cEYYQUklTSVa2viUG3xLsAnM3VFRXtjkX6h1Y6V5uqxhHU6UJeZEeHd4GIwW_aSARPzulx2ymIO2pOybqhFW79BPHvpAdjmJ0n3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=JbDha_PC2NHHVr9Eb476eSCeuQ2gEI6oAz2hUQTLatHNIaLyjhlf91O3P8QLwP2miyxD3KsNKz3dbLAjT0Yk0ZNHNMT2ZAa_XDsHAWbV_INQ61EhFcMp7ClWiw3k-_Z9hbNH3OJp4paM0LxfL_B34X1mA-wEhf2lNJZMHdLy6jeb5HBpOsYaJvldI7lX7De_Hc7JXWAFA8pbdnycj1C7xfwiqE2qfJCWcvxUu3dewjtKrzd01cEYYQUklTSVa2viUG3xLsAnM3VFRXtjkX6h1Y6V5uqxhHU6UJeZEeHd4GIwW_aSARPzulx2ymIO2pOybqhFW79BPHvpAdjmJ0n3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=rdFl_wv0sS4oerm_wiHJZLXvAXzYLw5_aGvYIw5VVX3PlxUW3xwFHQSMbzYkAHvrxHJHsjveLqnn-93Jwfaqb0zlkfzv1VW6IQrRdZCktA9cYgDcUAHJvPgY2GyEp1qUvLNnQS66WTxZy2DkhI2AYp-QMZO9Cd7J-lBtcGgJgP2EeMuD068hbCBglupun8RmLlkU6uQlCJHbXHUpKjOWsrofd5CjZhSr-RbgUlzzrga2wuVqv4QqYUVqLpFfV9GrvDHzfciwrVyMZBbV49qJ4_Eyz-5oqh3KBZhm2bmciDukbJfQOWwu-LfpJjEz9zWPOudJV-puQBsKTx1RTrPjCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=rdFl_wv0sS4oerm_wiHJZLXvAXzYLw5_aGvYIw5VVX3PlxUW3xwFHQSMbzYkAHvrxHJHsjveLqnn-93Jwfaqb0zlkfzv1VW6IQrRdZCktA9cYgDcUAHJvPgY2GyEp1qUvLNnQS66WTxZy2DkhI2AYp-QMZO9Cd7J-lBtcGgJgP2EeMuD068hbCBglupun8RmLlkU6uQlCJHbXHUpKjOWsrofd5CjZhSr-RbgUlzzrga2wuVqv4QqYUVqLpFfV9GrvDHzfciwrVyMZBbV49qJ4_Eyz-5oqh3KBZhm2bmciDukbJfQOWwu-LfpJjEz9zWPOudJV-puQBsKTx1RTrPjCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=f3tvv8ii-2HSLsXucbcVNMZGRiP9Jg_IDJhUgj2mUlLk8JPMFWCnIOJSKppucmPkJmdQvIYo1x8o2nw4MI_wRJSVbMK95zO_DGCBVtt6CPmoSgWWcO6SJaCOWmIaC_kXLSU8jj6bFjRoR5byUJyB1B1X_vFN1bybs6E6nJA88tQyyiAdDqaFoYrT9IKFoRAia_xLag1MwVomJF5USapOk7pDO3hfw2C-HrlvFu5qBdFb_a_32qWrq7dhmOFfhlAsrlmzpdCAMKC2beQEtry7J7-g-QjVbie0fy0b81EUElakDyH3CYSNjAxfw4aImBaZAjBpEFKaXHDBF2vLVrCzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=f3tvv8ii-2HSLsXucbcVNMZGRiP9Jg_IDJhUgj2mUlLk8JPMFWCnIOJSKppucmPkJmdQvIYo1x8o2nw4MI_wRJSVbMK95zO_DGCBVtt6CPmoSgWWcO6SJaCOWmIaC_kXLSU8jj6bFjRoR5byUJyB1B1X_vFN1bybs6E6nJA88tQyyiAdDqaFoYrT9IKFoRAia_xLag1MwVomJF5USapOk7pDO3hfw2C-HrlvFu5qBdFb_a_32qWrq7dhmOFfhlAsrlmzpdCAMKC2beQEtry7J7-g-QjVbie0fy0b81EUElakDyH3CYSNjAxfw4aImBaZAjBpEFKaXHDBF2vLVrCzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=ePa5fqZ2Erh1haBstSRMnRW4R0FytsN_69BTguABX1MLQl3l37TY9MW9SoNBgWM54An-Za9CzVSYDsZ2GX6OJrpBjniayik6FL38MhABdcui6x317XY9tuMdbGtdva_qmw2WxmawUL8PLAGpd_LsV6lhFWgePoosYsK5sFe8ash6p4-jwDYO08go_pvr6F9_tAirggQK9HiiVQ_QKOAacOFQwcwXdOb_9aX4fdqHO4uvITuNya27utHL30qZy5_QH5sylO9_jMPHmIR7T2K73WjSpQ1CY3tVsFj3qDd0xV8pkgquJoA3hEPZPXeW9h0Wge7HMccxQvDY9-jLzCm1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=ePa5fqZ2Erh1haBstSRMnRW4R0FytsN_69BTguABX1MLQl3l37TY9MW9SoNBgWM54An-Za9CzVSYDsZ2GX6OJrpBjniayik6FL38MhABdcui6x317XY9tuMdbGtdva_qmw2WxmawUL8PLAGpd_LsV6lhFWgePoosYsK5sFe8ash6p4-jwDYO08go_pvr6F9_tAirggQK9HiiVQ_QKOAacOFQwcwXdOb_9aX4fdqHO4uvITuNya27utHL30qZy5_QH5sylO9_jMPHmIR7T2K73WjSpQ1CY3tVsFj3qDd0xV8pkgquJoA3hEPZPXeW9h0Wge7HMccxQvDY9-jLzCm1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=Vy5PgcDxKcQbhor15NFbQyDO-_Rw-C2UWLOY4__fnJil7EFZf-Ylk5gtCbxlcdML_Qb3qb6EdGZnFCUflyGNw9VKx7XQgBCPEUwneK9ll_HBccJbJwxxXeZMi3gCEHLC6s1JWw6JFp2PKs_CsVCDxc9ZTYxIMmi7DBaOyi0PAeDoBOv4DgDgqx7uL9abQCMocpsLyvn-ubGRiC_p7XsIxGlQ7CRa6m9di41xdcK1XgiIrY3p0yhHrLWlgKUhv3oTzDpQxrEIHVxxCcyk754tpfPdcoOkg70Px4D5iQxhssxV3JfCmQFWdVIe-2zV7bk2OQKFADJnfZCI8799I1XgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=Vy5PgcDxKcQbhor15NFbQyDO-_Rw-C2UWLOY4__fnJil7EFZf-Ylk5gtCbxlcdML_Qb3qb6EdGZnFCUflyGNw9VKx7XQgBCPEUwneK9ll_HBccJbJwxxXeZMi3gCEHLC6s1JWw6JFp2PKs_CsVCDxc9ZTYxIMmi7DBaOyi0PAeDoBOv4DgDgqx7uL9abQCMocpsLyvn-ubGRiC_p7XsIxGlQ7CRa6m9di41xdcK1XgiIrY3p0yhHrLWlgKUhv3oTzDpQxrEIHVxxCcyk754tpfPdcoOkg70Px4D5iQxhssxV3JfCmQFWdVIe-2zV7bk2OQKFADJnfZCI8799I1XgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=SzOVmQ5sBlTGBzUUjKnz6PqZUwjXA8t6kRdEXQhZiScP8olomYUj14lbaCg1h3--aGlxVm--HBNXTNlFQPGp8-6WwXjNd3xallutN5ZyUGOmazgvEcMmegGpg9U5DfsIlHpTEQLEp5aVtKDbZWKVOTtolr51XCa2S6hU4QdDI5UYTwq1ogZuOuqlGi7v_SDUpY-wT1jUfz0fqfJI5p1Z16EBf6zWXYQbPYKncY-awqfg2kU5fNdXC-IWgu7px0VkfmjYfFr1OuZ2Jt0EWeVEco84FJGLxTj6IMG_aeJrz04y1VrBpu6kFpAf5beMd0qVx0TIKqevu2RFDVTA7UiaTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=SzOVmQ5sBlTGBzUUjKnz6PqZUwjXA8t6kRdEXQhZiScP8olomYUj14lbaCg1h3--aGlxVm--HBNXTNlFQPGp8-6WwXjNd3xallutN5ZyUGOmazgvEcMmegGpg9U5DfsIlHpTEQLEp5aVtKDbZWKVOTtolr51XCa2S6hU4QdDI5UYTwq1ogZuOuqlGi7v_SDUpY-wT1jUfz0fqfJI5p1Z16EBf6zWXYQbPYKncY-awqfg2kU5fNdXC-IWgu7px0VkfmjYfFr1OuZ2Jt0EWeVEco84FJGLxTj6IMG_aeJrz04y1VrBpu6kFpAf5beMd0qVx0TIKqevu2RFDVTA7UiaTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=WEMh2sVwsJnrZOgVujQCg-XkpXEyaJ2RJVuNZlp-b8Ao80yyMsOeNPwOEZXcgDNlSVRJldTh5RYzr-RrXrIpa2PNlv79LKmkgwSw7wysESOM8YUPshTiiuZbFpQ_ohEMVK0KyyGF4h-X6YzNSFrwj0opbOGsbftnmUip9HHhPxNA-P54L_qDjNXBU46PUZjV3DfD6Zi8qefPECHCLkETn9XSIyyujtDZCNLWlicIat4yVDiIupfWwP9ly12Nso5pZ5mqxhIrxeM8LbCTpoZxUiekcX_2lDUzAfYF6VstueTeTqDCR7m1rOnuzitJhAA7Xs-xlBeDsY2vvAnLbqOqiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=WEMh2sVwsJnrZOgVujQCg-XkpXEyaJ2RJVuNZlp-b8Ao80yyMsOeNPwOEZXcgDNlSVRJldTh5RYzr-RrXrIpa2PNlv79LKmkgwSw7wysESOM8YUPshTiiuZbFpQ_ohEMVK0KyyGF4h-X6YzNSFrwj0opbOGsbftnmUip9HHhPxNA-P54L_qDjNXBU46PUZjV3DfD6Zi8qefPECHCLkETn9XSIyyujtDZCNLWlicIat4yVDiIupfWwP9ly12Nso5pZ5mqxhIrxeM8LbCTpoZxUiekcX_2lDUzAfYF6VstueTeTqDCR7m1rOnuzitJhAA7Xs-xlBeDsY2vvAnLbqOqiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=gv1ZiUBwrUecyu7fi5ROs1K1y27XP9D_zKyGt9WBLU_bsxEy4senNqUeR6tNbB4_SKmX0y7DQ8CIZ3fUJqpd1nv_Vg_ZC_RcpiEZafy9-DN1q-_Kzi1FRTUoJMgWiJJ-vwkHAaLF2jJeBw8JpN1Jeh1YWNv1nhWROXREZw7Yggs4DKvXQl2DI-W06TBVQynaasn9_Q05j3M7Fz8M74Le1tPP4nU5zA31nQvHR-SUW2il7dj5mekERW9kUIvrDgDGbDBR5PPYB-LU_GkFun0JAb8SD3q6TxtNDUrmo61LotCNGJvK4qkyee_uM3Oamrg2Ox_iWpylB-W3-sIzb2o2Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=gv1ZiUBwrUecyu7fi5ROs1K1y27XP9D_zKyGt9WBLU_bsxEy4senNqUeR6tNbB4_SKmX0y7DQ8CIZ3fUJqpd1nv_Vg_ZC_RcpiEZafy9-DN1q-_Kzi1FRTUoJMgWiJJ-vwkHAaLF2jJeBw8JpN1Jeh1YWNv1nhWROXREZw7Yggs4DKvXQl2DI-W06TBVQynaasn9_Q05j3M7Fz8M74Le1tPP4nU5zA31nQvHR-SUW2il7dj5mekERW9kUIvrDgDGbDBR5PPYB-LU_GkFun0JAb8SD3q6TxtNDUrmo61LotCNGJvK4qkyee_uM3Oamrg2Ox_iWpylB-W3-sIzb2o2Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFESUGDUUnxSLvtXqp2vo5N8gKkIKjJSLLD1C1KuelPiM5HqQX-QgQIaZdTIp9JLNy_aITSHwBVkczDCbc6yUEJTmwdAGy9x9U9fDm9A5ISp_9qp4YciO3UaGA7wmOhHK-SNI11lFP4qzO2Kyl02drHZR7dgGPt0XUjLOuU4sEyMDrsrGPba3-PpEyL3v_G13JknhYzfQHZ02gOnom-myeFhgHF7hK7EAzO_O1_k2X1ymNA1f-vk71ZZw5_d0syOf7WIRQPx8RAElqmZv7w-bToemSMQYmn2jHLDGzudRd18lNy1slizTOLmQb-8wkEK_4NZXuujdxhfxVXxX62Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phpEQOUFwF1QdDugarVuIbMSz6NYxj4I64iAXfgQn4l5IJvIX5v5G_YwiiFiHd2PmTiMGNL7s-8MCxWhBDLNkw_B8AxoPGbhY2vFvE-o3JXtiOvbf_a5QfNmBMcMDEGIWAA7mK6hVJjGEsMzr_sobFYRkINbIQo3_P6s4-x04fC8-AfDXXHxD2sRjLXOMHvKMDAr1nyP_F07lUYkqqpQN6NFpFUor2_je5l6m82cUccii5-am1ggdCNJFGOx3lpVV4etlEy_CL3aCnvq9q_FinvWiGog28vKLWwp9UBuP-bd8pDczim_SLalJa45oSnLr8wCEuk7UlYk74lhIEN_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_kjFCdsZkp7PoNSl_5xow92p5Uah5qL2EPY63vxjHnrfXhu62uuybDyp4OD-hlANnI1osMW4fOdel_oTcO7FKr2dSpFg__qPmO9040l4mxgpQgsruP14-XDf3eXJIeivhBb2Ii96dsEYa9nuJ5rbuFUuLPvyG7DyV5bPk9UQxwFd1G3miWzywkRvibx08JWjfrLGepHAAucNGBtYBebxmQimOTDp-cMDVUjHibmCuidIV8WSmHNup7GNRH0tJsYsBaUkXiPX8EGp1lPOLDGsuqprcey2tRsteK8PdDLN01MkBKyxIm8Crem68q0cO28x7HvXTwLYdHnRW2k9wRA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMJreTqwh7jdU2AlLV66HpUovjeex-pilMPhzsMzSnHYDv12NO8o5A7xhe60PEWWQY2rhnQsNwftO_iq3UEXr1hk8nFBeVqmeXLlABrlAdQgA4SYjJ2r4P6un5cFjWl8j1nnRXuUhjnTlTR5R40N5sQf3q6lHDSNdSam9q0Scd90Bs7wNO16obW-k9soQC_NpkFXN0h4CJffs7gPRvQAG9J1YWE38umaClSlSpXqPOjCT420LmFUEqw4fn_Q6UhEXF1yqYna3kyoQHTYqWFOgATl3fBI3yUiQuWOmBY2CG-B5U4rLCjrM_llchiudX40qLBpqNCRR0P_q9EdwWYetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpAJxkw6Az9BAeKSuOb82RVMnWF_H99iRsknvXVanA68Yb9w4UfIqHn5oWJKNgYlYvWK15kTamGNFDZNxEfgnT_OmAEzZLpXIJ8AXaS1EiMbTrNRVT2Cae3Wdk-VvLdPYJEdAT21oFqpj5Tt1SG6ir6oH72ELD7ndN13nbp1_onmSxbujXyOYs5zJSa4RvtNJTgyyPJuQ62L9oX7gp9-vix_6X94go6MvE1K_SGd8faigukSzilEbZ_Xuk6b-c9Vaa7E3_irv9Ix_HLKflGyZa-5eA9raQqExqte1202JJJY_BBujkiLb1KotwDOjtAWsETxkRcPwPwUL58A2LLPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUCKGn-3dqAKrw32VLfoNKF9sotXmGZ1NEntAHK0Q7Bo6gLozK7vqXAcM2FZyelarA4xqkuvIT-T77JH0rPQoUILDTLKsslZznYiCxBMGoYN9aLZxAsmEouivysZ6CZMjn6GwL8DFeJsKynbyoKgW6GU6yiIGgYNw5MZw7_cbsoxa1f7MxQPit5OBGg5etLynDwfg82x8RtF-Z6g9A-77FGiyj5jSW2Y6ibVX-PitTvoI010WCzm4woQYHWvQQrDnHtWNvKiXp_A5YCFu-8oSIckKSU-69vcMuJ6KZQW505fPcZtmM_dyy-9cj_y_3wPTfuRmDMyixeB97NEsh-U0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=RWpqQ6-36iydUGn3EXiU6e_wCsMLv__l06ydhcTpb1PG2M9xHDz0yu6Qdf2mfD-w5KlmnpMlUZ0RKz7ZKr-N1JgLGiKrWsHRgSUVRh_UG9gxsAKbvCGNXPZ1bPny65d0ttAQiuOF_TUQzhFsEjlelm0lWnF3AvEZpMXNpU2uFynQ-QrTx-xaKHeXtvlWhtlzapq2Xw0W0z4yktUcOE3DU3w1Zyv-CgDk89XpvY8BV9AvqQCh8vn9fr5RtFephqnRxafQiMJL3TK2UV8_C2dTSmZZJ0mOHGu8QLc2RyXZ0VFa_iOAlUDEolMjkUZ97G35OMpeCo_JpN5JB8qgP37SEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=RWpqQ6-36iydUGn3EXiU6e_wCsMLv__l06ydhcTpb1PG2M9xHDz0yu6Qdf2mfD-w5KlmnpMlUZ0RKz7ZKr-N1JgLGiKrWsHRgSUVRh_UG9gxsAKbvCGNXPZ1bPny65d0ttAQiuOF_TUQzhFsEjlelm0lWnF3AvEZpMXNpU2uFynQ-QrTx-xaKHeXtvlWhtlzapq2Xw0W0z4yktUcOE3DU3w1Zyv-CgDk89XpvY8BV9AvqQCh8vn9fr5RtFephqnRxafQiMJL3TK2UV8_C2dTSmZZJ0mOHGu8QLc2RyXZ0VFa_iOAlUDEolMjkUZ97G35OMpeCo_JpN5JB8qgP37SEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otWrweG43X7OcAlIzAvmLXMoeLkhOdIdwi7TAusYSWfWpvjtzXk9H770NcA-R_LEVjWB_Z4VYA_6MogS2l55W1w7XjEc2K-BNSF-H-zhqbIFIZtJTUx5YY465sX1wGziQZQxXr1NO52eoISDnkkCLcD7uVNH7ABr0UspRylfwiPlAq-jF44mGMbe8pg9xte-JpLdJ03HzvBSplGG2m8zt5patylTBddSGU2Bx39zOhZzjZr2a0x4ktX5x2u0-060q7YPFMsTQ-JqIRzSlqOWPkUPP6d9v-hWCriAFn6UDe4chF2HoTZ1XPfA9pTGr_4ytv17cxU6fNFCtfhtzo_USA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRdE-1PmiOHTEkSiEkOOVXIaNNPDFzOI_E6PdUSznaJpefTSdx4_F9EdTwaI7K66e62AUirbxziedCca35er05a6cz2cqdzPWsrCSJ_lP-okVI0Opg1imfb-Nidgu29P6DRZtEZfVLdNeV6KdWX1jex3sw1KcCDwe30k7Z2e1UF05vijYz71Hual9Vl0DCTHzdx9hCqM9MC7lsqTY6AI4q9ByomPHW1cxe1mN4CxfqXanpaBjIxGI5iwkpSJluAokevrNO8pT75AMp__4hpODVD0Iz3eKibuvZGuAucpQ19wdnkSUjpGdpEUOdjBeJrMPdGM_dOw9319daqfneGF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxsY_Z6agC3txfB2rqxEOp4bUmmpQQPEq1PB8-T0hipKmFXoa1mWVtn9lS0S8EzJts7xRZLfiVI7fr82DazX-Y1Gc60UotQbAGDvqB0TTaPmwyz8VbsI2XYqGT6cqidlyBP8dyhqjVJ9fqOn7aLt-fkNLs2HozieXfWdKUgW23Kovj4WX2oNkStFKlrXjnWWI1Vf4dtdrHQueNJGRQfAld46kV0sQSvfgitHvS7Hxsh81xiEZe2KcwooxB-_6Mtzwr1vACq5ROuicnmbjicscpCHNWavq1F6jAiQtPYNoebrD9SNtCls_hUfM2zDWtJ3k6IIFtkmXL0d60y0WuCF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipex8MskJNxI_0Ljpc2bllCxfkc0IifeQMZQIo1k6XpTs37p4cP1Vo7ry_LreYTE3P39fNUuKSkOXdKCrURsRTkYmW0NVrxry6v6o7_kx8vHzGmAX6CPJUpigwWJC3Xzv8QwbrtYBzzXXGZg1rxpftLxIVSXsIajewNB-YXR5fKwnEf1RfL-MEdc9fB835CawHRcIO6CWKVd8aNbQdk3XR8GRLooJG635zRHdqD9h1mFZzrCuSpGqmIJVaGhhF-O5pgPCR6Ic-1CGcCmTkivAz5KBKz8eqxf5ToZns0iDUiZlFsass0L8IBwvOxMP51S8_XofYZrAgujsHYbywTXaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIDAbDgRFwiJyYE_UA94WkuSJHAbnURvE15KqOraMqYATQdYErOh2OAWrqsvtxUDnhWW_GbntQfULmFX72pfWxcDa_4Cz8_VXcZaubYARTe5YRTZHiHju4DSY_cjfr-vm7xzDDs5sRGUY5J7vfllgJuRghr_rxnKPTIP0qjzODtyErXRQ0pcZFrz0itSaGobleHr2xcD4RV-u1dBVNs9QmOShNt1mIDZJ01TsOX5F0eYiuPoDC3G2-M169tscx-1WxZqA1snl21VEL2GGyt0SA5gCXroYEa8I6DUk9mvmfQXMdOybqTUuB5mIkaRvRIiNYj37jogm1Uj1tE744KdpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg3Rb2-w7WewhU4NSatYYLqRrVpbM7ECc-iEZx2CaJhtBPYJq7h4dSl-b06YgR5Y9LlMINHssFzhrewAwSNZu5XQZqbPSeWmSRK0FblOS-LTPXMvqaYzx3TI-DiURIPcN2C5HU6bgEGjwjMikFF3TwUuuls2aztKFPYoyIOEvQS8eFV10gPMp7kLpdd2RTLYoEiR93TYJIDtPoNExt84fw3zGqj1y31uz_eOZ3ts4QXQur7Z1uLPHMpQaj_0TaMBOVnnLerClipY3_EV5Jz0Mno57JtuJ7jqS7z4Ab_aTciuNerRCF3dR87YQV7UANvhZX7nVlWVLX2GIIE8KwDbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
