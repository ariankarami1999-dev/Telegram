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
<img src="https://cdn4.telesco.pe/file/NLRxiNNJBocQNzHtAzunIrEE9LkykRZvy2Sl_ZdG-VO4V0edKexSBP7ls4IWFEuEKtCMUTYMHZZuvJoWOke0OSaiXDKRRTdF386sTuZS6qN4DeWWdkpQGm5UuZozkXd7AuFTvHXt3d6sVqHKzBSlIwryPoBW-Ni6I3iXlEkZl6DQGyzAx4Pe0VfxLplOrInh9Z1b8gMjHEMEc0cYBLpoLk7ivneQg-AmazSElzDYbFd0b05trXfhbybkNl3HpZ2K1ffIZvo0knLt11C4LXniCcA_cOs4u6jKaBU6fQUeEH1sVzb7ntoU7MMMWwWyzx3X6cBS_SjfUCnpS9c0X7unhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.87M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-460870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس بسیج اساتید: علاج کشور در هتل‌های وین و اتریش نیست
🔹
میرسامان پیشوایی: دروازه‌های نظامی و اقتصادی کشور از طریق علم و فناوری گشوده می‌شود و علاج کشور در هتل‌های وین و اتریش و این موارد نیست؛ بنابراین نباید علاج کشور را آنجا جست‌وجو کنیم.
🔹
علاج کشور در…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/farsna/460870" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQnlbzr_4JCGGPQVM0VNIw1sucuuezPirnreg4L9io9qLLgGoo3S_zF_AcZy5LGIpT4L0KXHyAme1F0oGjAaWKBzTLksuTGjLasw1caf3A2gbSi1SiszkvfDg0FlU6J_tHCOl8Fp1aYI0gkEcPrBCSufSbyUHh6KS8HxWi-4zGdVK9RBLdpzqWTVvkgOTViKoa7VYEGKTojdXRsRr7Q17PpKe8gpoY59Qq4nvB8fAg6BVgzjxTXXekLzr-OTxX5IEy9GP3CYH9dEfw967kAzolSD7eUlCXimR5Zo5eu9YO1iU2SyFBK8WFdBStRg9KRH9LgkbzMnM9maHic3sV9mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بسیج: ان‌شاء‌الله امسال ورود ما به دانشگاه با جشن پیروزی مقابل آمریکا و اسرائیل باشد.  @Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/460869" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4zxCszgeCTTHUPmNVnAMPegqKcueElLLj00MIRvOGjGvbpGOM73Pk_LXOnNGFDiHLP99pLbwjz83bSuxHHbThz1I7o1dDvRFyCHqmh7jg0SecwuJ0tYSzcdZGSXyjuSgAWUMx6NUOcgHOHEKB7j2sdZnv73oiQoN449Dv9nlVuOYxlHFXCSGHuZ2JVFBU_9959FqVz4LpjNGhzatMTseqXhyeXQubguAbTPJhpoMxYP72H2cXthB_EmohemUReiNv5xEMk1MYi0JS9nUH3dfAXEvNxhTz2Hg-KFnfJkJx4sCE-mNWLcHQiKzOGn4hHX2I5Zflm8o25bUejerAy57w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در تماس با همتای ژاپنی: وضعیت منطقه به‌دلیل نقض‌عهد آمریکاست
🔹
وزیر خارجهٔ ایران در تماس با وزیر خارجهٔ ژاپن مسئولیت وضعیت تنش کنونی در منطقه را متوجه نقض تأسف‌بار تعهدات آمریکا در چهارچوب تفاهم‌نامهٔ اسلام‌آباد دانست و گفت: «راه‌حل ساده است؛ بازگشت و پایبندی طرف آمریکایی به تعهدات و امضای خود در تفاهم‌نامه زمینه را برای بازگشت به وضعیت عادی فراهم خواهد کرد».
🔹
عراقچی همچنین با تشریح آخرین وضعیت مذاکرات ایران و عمان دربارهٔ تنگهٔ هرمز از پیشرفت قابل‌توجه گفت‌وگوهای دو کشور برای تعیین یک مسیر موقت تردد در تنگه خبر داد.
🔹
موتگی، وزیر خارجهٔ ژاپن هم با ابراز نگرانی از تشدید تنش‌ها در منطقه، بر ضرورت تداوم رایزنی‌ها و هماهنگی‌های دیپلماتیک میان کشورهای منطقه و کشورهای ذی‌نفع با هدف برقراری امنیت در منطقه و تردد آزاد و ایمن در تنگهٔ هرمز تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/farsna/460868" target="_blank">📅 13:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40c83147e.mp4?token=lcX2-93C2sd8kmP62UpwDr78UyApZN2P8DrHH_va2HgACDDa-NBhvxACN-7T967EZfH5_lUa2x8by1RwqHi1eea1zrd1Qb4zjenh6-Q-l6DZeYC0tR4A5PAweKWSRFx52V7W82LB1ZeifEsDDNkKaRVx8rnBmglqYLlgZnhvDlddxdTNsk6EexIUMr1HdV760d-F5Llh2NZvPxbUKMMPipa22w81nAvWYs0AmZrslsHsnqau50rEFHIxRJThtDmrFZe-UtHF-_NqcWJXX6pMZfN85XoyWsiMA8juwp20iMQ0wjNZfpACuqs2Hg96s2nzGS5-XW4CSXS7ub31qY_ivg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40c83147e.mp4?token=lcX2-93C2sd8kmP62UpwDr78UyApZN2P8DrHH_va2HgACDDa-NBhvxACN-7T967EZfH5_lUa2x8by1RwqHi1eea1zrd1Qb4zjenh6-Q-l6DZeYC0tR4A5PAweKWSRFx52V7W82LB1ZeifEsDDNkKaRVx8rnBmglqYLlgZnhvDlddxdTNsk6EexIUMr1HdV760d-F5Llh2NZvPxbUKMMPipa22w81nAvWYs0AmZrslsHsnqau50rEFHIxRJThtDmrFZe-UtHF-_NqcWJXX6pMZfN85XoyWsiMA8juwp20iMQ0wjNZfpACuqs2Hg96s2nzGS5-XW4CSXS7ub31qY_ivg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طائب: هر استاد یک بسیجی و هر کارمند یک بسیجی را باید شکل بدهیم.  @Farsna</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/460867" target="_blank">📅 13:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVQxFBL5a6TxBSAVVW81bdDAauzWXGOjA2suJXnv7w5nfUAK4cRFhn_8cX3A5yjD9u_tuPtcxonYeZKbTi5WmoMi3NxjY3jfXS6BPcnbbjrkhWo7DSusUbIqV7tXqIAJxgNL8Z6PCh2-P-kBqDdJe-y4u_y_4hDHdsijbSHDhP48QCgzOLjCOBz76jFj8n2fetymqpfnA7gby0vIEpukW85X8e7ZNDI6ogFpw4IjK0Dp2wpRFTm45Zgyb--uET6BUADIEmsVAlser9vpUPDum_m2aAeZ7y98pyZvnCKWI7_UFEToSjTKMzGLJcOoVjC439IzBIwpKsdY5RpfBlwB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ایران تا پشیمانی کامل متجاوزان، با قوت به مقاومت ادامه خواهد داد
.
@Farsna</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/460866" target="_blank">📅 13:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31884a3da2.mp4?token=N87CvP-GTTYxDl7BRG_mm-utGonxEsKWvw0JhNu7-vkxBMMjgSCqlwfxQQja_4ePRhORA-bz0XuWH9hvp8eJfX_bAxSxSJimcw1Xp7d4rTzFug6J2AcCibd9YS9fmGhV_RlVPnBTQRc16VTNlycHpuJAZpYclONiqKXtlwBn4LF4oO-EbRRzYsjzZQsGaMnqkhFWKDpa_qpndfxPKHe8SUrpiZqqrJhHuxwXd0gYTZgwkrq_HtcSpkrKiwfGFLQAQNZH2vwM-k_PaaqY2yvtC36e8QVQabzGtfvd8iTI6MyUYjn9jNkRuTE3civP8DId4Uc0dju-zJI6bw4BrM1vMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31884a3da2.mp4?token=N87CvP-GTTYxDl7BRG_mm-utGonxEsKWvw0JhNu7-vkxBMMjgSCqlwfxQQja_4ePRhORA-bz0XuWH9hvp8eJfX_bAxSxSJimcw1Xp7d4rTzFug6J2AcCibd9YS9fmGhV_RlVPnBTQRc16VTNlycHpuJAZpYclONiqKXtlwBn4LF4oO-EbRRzYsjzZQsGaMnqkhFWKDpa_qpndfxPKHe8SUrpiZqqrJhHuxwXd0gYTZgwkrq_HtcSpkrKiwfGFLQAQNZH2vwM-k_PaaqY2yvtC36e8QVQabzGtfvd8iTI6MyUYjn9jNkRuTE3civP8DId4Uc0dju-zJI6bw4BrM1vMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بسیج خطاب به ترامپ: اگر نیروی دریایی ایران را از بین بردی، چرا هنوز در تنگۀ هرمز می‌جنگی؟
🔹
طائب: دولت آمریکا باید به مردم خود بابت راه‌اندازی جنگ با ایران پاسخ دهد.
🔹
طبق نظرسنجی‌های صورت‌گرفته در آمریکا، ۶۰ درصد مردم معتقدند راه‌اندازی این…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/farsna/460865" target="_blank">📅 12:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460864">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7010c9344f.mp4?token=gqP71Xj1HZHKrxI63lqxyH2erZ6jwb9IxinLj1qEO5fhgvNTTYQ_pYv1caG4dRkYjB-MZuFz6-Er7Hn26PzAAK-1jZzlQQZ-530heJ84Vyg0x2w_eULZtIqan0qBTEk5ACHIjHzL2Ik5v-Hprs6Gx8cZK6wjHMvaAiheSyzO6dZpNyP8d1yR_Zv3d68X7krDcYrRzTqIFNDN0qTWPZZSdYkZ14porPPcm_7Gu_EfAjn68YUdS9IG_rpQMpj9e9WJ0VcsdWGVSYQAoXvNM3vumWFeLFvaXuiZhdfKIAcrdYPXyiXxtJW0jKPkM8kBYSgIdeCj-yWfBr25uEV_petWEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7010c9344f.mp4?token=gqP71Xj1HZHKrxI63lqxyH2erZ6jwb9IxinLj1qEO5fhgvNTTYQ_pYv1caG4dRkYjB-MZuFz6-Er7Hn26PzAAK-1jZzlQQZ-530heJ84Vyg0x2w_eULZtIqan0qBTEk5ACHIjHzL2Ik5v-Hprs6Gx8cZK6wjHMvaAiheSyzO6dZpNyP8d1yR_Zv3d68X7krDcYrRzTqIFNDN0qTWPZZSdYkZ14porPPcm_7Gu_EfAjn68YUdS9IG_rpQMpj9e9WJ0VcsdWGVSYQAoXvNM3vumWFeLFvaXuiZhdfKIAcrdYPXyiXxtJW0jKPkM8kBYSgIdeCj-yWfBr25uEV_petWEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بسیج خطاب به ترامپ: اگر نیروی دریایی ایران را از بین بردی، چرا هنوز در تنگۀ هرمز می‌جنگی؟
🔹
طائب: دولت آمریکا باید به مردم خود بابت راه‌اندازی جنگ با ایران پاسخ دهد.
🔹
طبق نظرسنجی‌های صورت‌گرفته در آمریکا، ۶۰ درصد مردم معتقدند راه‌اندازی این جنگ ارزشی نداشت.
@Farsna</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/460864" target="_blank">📅 12:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460863">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8ZFWDX2boJP4I6mGwEvLz-VpA9xR9OvUJ6IXOdswuGQk66lr_e_hLKcVctdR32jGioDaUz8sTSNXQLPtryUao-1qAOKKb5kqCr4dvX9dbFxpb2iIxxsUdXiMf54h7w8pJY-Hf5hevCxtNmpTalL2pzrK-QNne3jYFo3xvp97bBdHq5fxjcbBq5BRytSMSWU-rHCJVRMq4K1uPWoV8l-29F5pBX0KfrlVvs3pTlfumAK_qCe3sjlLLpIVmdYNbgNgARUGSxo5ewD5Y7LF2A3cYIfc9LsZB6HxGqsV48K4WgQiB44yN2jfkgV-tLuuhaXvOIx-X6Kt5aZ-tKSQsrCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس امروز را ۷ میلیونی تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با افزایش ۱۶۷ هزار واحدی به ۷ میلیون و ۷۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/460863" target="_blank">📅 12:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc7b914dd.mp4?token=ecu86_GkuzxAV_yax-OgX3tGT7MelLZI1RbSwCB-Z_XQFGQsZnbhe1A7knurV1nddJ27oDAGN6FZNMWOpLbAwrNHv_363hE9lrBg7s9etJ0B_0JAx_DGfp0ezHP9cipV2uR3aOFOMrDlsPSUWbteewrDV7SzCPT15vgZAl8crZYJli6DMXPY7R_uLgU0ZlcUKH0pErz7gZ5WofpxaXWtgoPNu8DkTwIznx-lgrkhf5fZDrG9KNuBnSdo5xGUtiO9zevMqd6D_p1ujB1YtfShmWfHn9OeS3ZuZ-fyeECFvZYgWuYgD75CWXfegHXrrnEWEROxv0JF82OipDxklc5Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc7b914dd.mp4?token=ecu86_GkuzxAV_yax-OgX3tGT7MelLZI1RbSwCB-Z_XQFGQsZnbhe1A7knurV1nddJ27oDAGN6FZNMWOpLbAwrNHv_363hE9lrBg7s9etJ0B_0JAx_DGfp0ezHP9cipV2uR3aOFOMrDlsPSUWbteewrDV7SzCPT15vgZAl8crZYJli6DMXPY7R_uLgU0ZlcUKH0pErz7gZ5WofpxaXWtgoPNu8DkTwIznx-lgrkhf5fZDrG9KNuBnSdo5xGUtiO9zevMqd6D_p1ujB1YtfShmWfHn9OeS3ZuZ-fyeECFvZYgWuYgD75CWXfegHXrrnEWEROxv0JF82OipDxklc5Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاده هراز پس از ریزش سنگین کوه در محدودۀ آب‌اسک بازگشایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/460861" target="_blank">📅 12:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291f3357ba.mp4?token=F3ghmF-NkVmsYvt_ulkl1u8fGJ7u2nSjGlRglXF0rfWxfLJ27y7CUum2YJT102_ArIJzjV-ny157zE43x3QG2bX6bG6pA0PTVMskzbutME7GySc9hkhk2sdX_9fqwweASdD4UEGvxg46LZgi2dKxhajGIbuU0TW09Cu_Ad9wk5ztYWKfxooV-2sirbWd_i211EGRYLQYQsG4mk6fQ5G6UNPSWF4AGMGdXhV_nMj3DoR7Ut3jkp0J1NMqcPR5Y3phPioalzwaz8Zz1jSdhGtyLJiyq7zhNeTndEha7jNKy433vhyMemC4di8GL0t2UmHFc1b4ntjungEKkgmKHFB79w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291f3357ba.mp4?token=F3ghmF-NkVmsYvt_ulkl1u8fGJ7u2nSjGlRglXF0rfWxfLJ27y7CUum2YJT102_ArIJzjV-ny157zE43x3QG2bX6bG6pA0PTVMskzbutME7GySc9hkhk2sdX_9fqwweASdD4UEGvxg46LZgi2dKxhajGIbuU0TW09Cu_Ad9wk5ztYWKfxooV-2sirbWd_i211EGRYLQYQsG4mk6fQ5G6UNPSWF4AGMGdXhV_nMj3DoR7Ut3jkp0J1NMqcPR5Y3phPioalzwaz8Zz1jSdhGtyLJiyq7zhNeTndEha7jNKy433vhyMemC4di8GL0t2UmHFc1b4ntjungEKkgmKHFB79w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای اولین بار قرارگاه مشترک مبارزه با گران‌فروشی و احتکار در سطح ملی و استان‌ها شکل گرفته و با این موارد قاطعانه برخورد می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/460860" target="_blank">📅 11:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfb970427.mp4?token=najBNT0rANKxuDfHUZPDZL3XqXiXLUCksjjhVtRneb5CC5cudQHIlN6Ylhql2BFRhRV_zU0QUoRGxL7KfBnLYmznofzKMmUAo_aWz4r6-ID59UOtWtK5sS48Su-ciAFO52FZMVQ5x0QF8xTvoRpKPZOWHxqIvg4bQXO1sBx53rd2PT91xmlfa7bM1bKuou_8iOGPyUuRdcVUbu_j4i0ikzPQ9t0eQXrty2UF4iSQYAPnEBabhscUTxwbW4G_4vpb8dZMW6LDTUkz3XOJgAvFG_mGY3rmT67b63k5M3BE17QG_19ulwy8PlOtW0nN546zqCiZ_S7LTklBPeTmo1DSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfb970427.mp4?token=najBNT0rANKxuDfHUZPDZL3XqXiXLUCksjjhVtRneb5CC5cudQHIlN6Ylhql2BFRhRV_zU0QUoRGxL7KfBnLYmznofzKMmUAo_aWz4r6-ID59UOtWtK5sS48Su-ciAFO52FZMVQ5x0QF8xTvoRpKPZOWHxqIvg4bQXO1sBx53rd2PT91xmlfa7bM1bKuou_8iOGPyUuRdcVUbu_j4i0ikzPQ9t0eQXrty2UF4iSQYAPnEBabhscUTxwbW4G_4vpb8dZMW6LDTUkz3XOJgAvFG_mGY3rmT67b63k5M3BE17QG_19ulwy8PlOtW0nN546zqCiZ_S7LTklBPeTmo1DSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: در رسیدگی به پرونده‌های دی‌ماه تمام حقوق متهم رعایت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/460859" target="_blank">📅 11:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee10be90c9.mp4?token=ezwtflkqY7wz8EF98ZK8BARcMsxksUtL0u0oIECeYoyc-mnMo4IqB6k03BRc6arS1m86fTl_-jpmllX0iCCwiKDAmMrvb_oVwa80FybOHYjaFcWnsce5Bx1221wiMpz2aS7aNWXE3RMGcVo1Ikzl8k1aZ0X9vBRDhoXMpSmLRMLX-Nlldw7Htzqv0bbXo2BvjTpf13Y3IAJ6B6cvP4aQKB12_N9o5Hv9WHLalsqoqk3WCL5s0hHeg4Zb8-zMfVnPlwlJEewtLzyIUU58AkdL4akszBBWHTL_98rSJuAYPclfIDdtcPfStDSoKaZxW5hFbBOpfSnbJZ_-JBKJKvT7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee10be90c9.mp4?token=ezwtflkqY7wz8EF98ZK8BARcMsxksUtL0u0oIECeYoyc-mnMo4IqB6k03BRc6arS1m86fTl_-jpmllX0iCCwiKDAmMrvb_oVwa80FybOHYjaFcWnsce5Bx1221wiMpz2aS7aNWXE3RMGcVo1Ikzl8k1aZ0X9vBRDhoXMpSmLRMLX-Nlldw7Htzqv0bbXo2BvjTpf13Y3IAJ6B6cvP4aQKB12_N9o5Hv9WHLalsqoqk3WCL5s0hHeg4Zb8-zMfVnPlwlJEewtLzyIUU58AkdL4akszBBWHTL_98rSJuAYPclfIDdtcPfStDSoKaZxW5hFbBOpfSnbJZ_-JBKJKvT7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: پروندهٔ فرداموتور ۹ هزار خودروی تحویل‌نشده دارد که بخشی از آن در حال ترخیص است.  @Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/460858" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c66a69a8.mp4?token=I_Jslu0LKyGyopSuNLlHsAilIdYMMka0YQ-YV5oVSmagzQ-qF3ubfmcpF5h8F95pNTk9ppIWgEKHHO075_ZqDD_iglE7u1KuzNNes0NGrhwMrh3nXldi4thbOWLVZFdyFIpMM928WfDinVMlTGjFOdLR8yxp4eo3j3A1Zqf1istysfgbnhQnW1Tr_4ID2yvCo6-h9F9-GZZocT2EvvkPx9bSEcv1sQSRmsXokHwIBZGAfaDMvn5uLvnBGG1gfDXIIvMIluhG0ZNBvi6JuYkd7Q_mf70Gz4q6QEGxJwzuBkOUjYL-UcVu2yNTfIk0JW509QMHr_t95p-2W-ZK-XHSBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c66a69a8.mp4?token=I_Jslu0LKyGyopSuNLlHsAilIdYMMka0YQ-YV5oVSmagzQ-qF3ubfmcpF5h8F95pNTk9ppIWgEKHHO075_ZqDD_iglE7u1KuzNNes0NGrhwMrh3nXldi4thbOWLVZFdyFIpMM928WfDinVMlTGjFOdLR8yxp4eo3j3A1Zqf1istysfgbnhQnW1Tr_4ID2yvCo6-h9F9-GZZocT2EvvkPx9bSEcv1sQSRmsXokHwIBZGAfaDMvn5uLvnBGG1gfDXIIvMIluhG0ZNBvi6JuYkd7Q_mf70Gz4q6QEGxJwzuBkOUjYL-UcVu2yNTfIk0JW509QMHr_t95p-2W-ZK-XHSBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: محمدباقر خرازی در بازداشت است و پرونده‌اش هنوز به مرحلهٔ صدور کیفرخواست و حکم نرسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/460857" target="_blank">📅 11:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6253d754.mp4?token=baL-u5c-a9bk36oskyLgvj7HXg9-TQRIwdec2q-bbiEsacriUWRFELCrM5SW2mVIcTpkXzcecWyrRLbcPqq56wH34ncLRLf2CVxFqCKS4A4s2xMWGYHKCeyU0c3zj339jm9Y9ZQCqUtyLuOvQHD1v2YynaqmBJqiuJcRTx1Cu1pm01UFILoD_LPXA-vMh5BnGHQmFT7WURn4Nx7OGDHQM7QAECFgmMOZEcO6rTalvREDwtmng37EfowWPjNsWbaVf6tez8i9PYvw-7J-4kVSOgBJYTojnsB0DBXRai825aTqDOEF5X1pqeYMC-SbDzB8Qnv1VVy0tfcH8Sr7RnAS1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6253d754.mp4?token=baL-u5c-a9bk36oskyLgvj7HXg9-TQRIwdec2q-bbiEsacriUWRFELCrM5SW2mVIcTpkXzcecWyrRLbcPqq56wH34ncLRLf2CVxFqCKS4A4s2xMWGYHKCeyU0c3zj339jm9Y9ZQCqUtyLuOvQHD1v2YynaqmBJqiuJcRTx1Cu1pm01UFILoD_LPXA-vMh5BnGHQmFT7WURn4Nx7OGDHQM7QAECFgmMOZEcO6rTalvREDwtmng37EfowWPjNsWbaVf6tez8i9PYvw-7J-4kVSOgBJYTojnsB0DBXRai825aTqDOEF5X1pqeYMC-SbDzB8Qnv1VVy0tfcH8Sr7RnAS1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای مقابلهٔ هوشمند با فرار از دِین، سامانهٔ سهام طراحی شده و تاریخچهٔ نقل‌وانتقالات مشخص است.  @Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/460856" target="_blank">📅 11:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e3d77ad5.mp4?token=dWR1OgO07btQSwf6EbE0B4AW7sOkUoFAh42qpgB3ZCIPoWd7PQH4ISnl26WfQwFo8AtOczHJiabjZPlDZsRQ1l3LcbxgWrZi8YqGn9iUM-mpVFoj-bBxCB9sQ3i-j5MsnFJpiz6eS5ZGBlV-_t2J_NTOgMe1YgtqolzBU2RXE45zsnM-yqJpDvdBUHjsjY6RyVKwH4hAOvUGxbutmgeT8j_ouKyeZfF2PsVtXTebDVJE093qUbCI3ml1p862U8scCMfZ-AqS9XU24j94Y5HyWITZ1XJ04S9zgktNtF85muIJqPcjeD7VHLQwMdXQgwCrn72wvscQQc2JzELqJLNfoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e3d77ad5.mp4?token=dWR1OgO07btQSwf6EbE0B4AW7sOkUoFAh42qpgB3ZCIPoWd7PQH4ISnl26WfQwFo8AtOczHJiabjZPlDZsRQ1l3LcbxgWrZi8YqGn9iUM-mpVFoj-bBxCB9sQ3i-j5MsnFJpiz6eS5ZGBlV-_t2J_NTOgMe1YgtqolzBU2RXE45zsnM-yqJpDvdBUHjsjY6RyVKwH4hAOvUGxbutmgeT8j_ouKyeZfF2PsVtXTebDVJE093qUbCI3ml1p862U8scCMfZ-AqS9XU24j94Y5HyWITZ1XJ04S9zgktNtF85muIJqPcjeD7VHLQwMdXQgwCrn72wvscQQc2JzELqJLNfoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تلاش می‌کنیم با رویکرد صلح و نگاه مددکاری به حل‌وفصل پرونده‌های مالی کمک کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/460855" target="_blank">📅 11:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a6d40fc.mp4?token=LsY8bdTQqJZsBzS6YYbuIUNufixnUw1xpN6kyOI2S3SPZGEjRV9ZH_EFVhM9Kd4W9MO7ET7eZGremYxmo5edR2XxBuAyUaeYBxUt_oSStnQB7kkza3a9gIXHjfUwaqlNWUNTXk9lhvIFqqQms7QrJOFM39OU5VzRFWbctkMpiNIs1F0rEVUJrjBqUn-lfmBgGnWwVj0E7Cfwbh9YrZ_aDKn4n54X9ohk9DyUCR96BjXHvk3CGdqMKlVE62dznj_-XgWVzUMrDml2wPp4eSrUrNuP49zx_6ecaHSJC9MwDKIs2aNWLAfjGX4j0zVS4fVtBkRUaXySYc-3jBANlBnK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a6d40fc.mp4?token=LsY8bdTQqJZsBzS6YYbuIUNufixnUw1xpN6kyOI2S3SPZGEjRV9ZH_EFVhM9Kd4W9MO7ET7eZGremYxmo5edR2XxBuAyUaeYBxUt_oSStnQB7kkza3a9gIXHjfUwaqlNWUNTXk9lhvIFqqQms7QrJOFM39OU5VzRFWbctkMpiNIs1F0rEVUJrjBqUn-lfmBgGnWwVj0E7Cfwbh9YrZ_aDKn4n54X9ohk9DyUCR96BjXHvk3CGdqMKlVE62dznj_-XgWVzUMrDml2wPp4eSrUrNuP49zx_6ecaHSJC9MwDKIs2aNWLAfjGX4j0zVS4fVtBkRUaXySYc-3jBANlBnK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: در قانون آیین دادرسی کیفری ماده‌ای پیشنهاد شده که رؤسای دادگستری‌ها هم بتوانند بر وضعیت زندانی‌ها نظارت کنند.  @Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/460854" target="_blank">📅 11:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSz8PKA-XqdG5-ESsTJCl3SFG72Rz5kj9RiAqSlWEenjLOU1Ikz1U5rSvxZSAPgs6xXHJVLsRQqtYCNd_8851lVrZIOiHhytas9PVkvNK3a3RRVN3ZBB6eP3O92GNL2r5KZV8Wa3YKwRVjXx2M4rQFoWqV1purb6V3YxGulI9OfU7GxNRJtt6fHsrTopDQePiUyY6hDEUlY1w5MIzj7jxFjBZ4QzncNkJMbpC5Txt9MWzDmn7wbPQ1DbpnuAnfvUEZTIuk_VuRbD5zD1PQvh31QrwQwFo4oPr91rDgNYB-TS79tuprgvQ4XZsHFvBuRU7XUMQvGgjOsZh82uReJSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملات یمن آرامکو را به تعطیلی کشاند
🔹
وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
🔹
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/460853" target="_blank">📅 11:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfb4550f.mp4?token=bkAVV_EM7MHh1F-Ec_W0Bfk53QlR7eXmURhkfgt1Bp8h7ar0TUvRGYWZzr_dmQlmSnZtCCZiWuc7Udpom66vsAIzUKzdS871yJgWbR95WQTmIbzyAqp_s4Weu4LThvodcP6-KZ5O69hXzJMwiEBGG2m_V68fPtkhEcqUTxELj1EUTx9bMOKmnPAEo0J7uDXT1L1l_lLMOAHbm7D7tXhcIOV1RH8dry7XJ8PQlEmsp82Rn-nXu0S9aVQhalNB0kEddrffLMGWPpmI2OM56-vl44Vv5bD6ZiWQ7CYU1k1ORKYbk6zmRHi5zmqybAfRIeS0MJiyGXDFKaOPS6GxJVTB5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfb4550f.mp4?token=bkAVV_EM7MHh1F-Ec_W0Bfk53QlR7eXmURhkfgt1Bp8h7ar0TUvRGYWZzr_dmQlmSnZtCCZiWuc7Udpom66vsAIzUKzdS871yJgWbR95WQTmIbzyAqp_s4Weu4LThvodcP6-KZ5O69hXzJMwiEBGG2m_V68fPtkhEcqUTxELj1EUTx9bMOKmnPAEo0J7uDXT1L1l_lLMOAHbm7D7tXhcIOV1RH8dry7XJ8PQlEmsp82Rn-nXu0S9aVQhalNB0kEddrffLMGWPpmI2OM56-vl44Vv5bD6ZiWQ7CYU1k1ORKYbk6zmRHi5zmqybAfRIeS0MJiyGXDFKaOPS6GxJVTB5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای وطن‌فروشان پروندهٔ قضایی تشکیل شده و برای بعضی کیفرخواست و حکم هم صادر شده
🔹
حجم اموال این حوزه بسیار زیاد است و تجمیع آن طول می‌کشد. @Farsna</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/460852" target="_blank">📅 11:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1738a6d5.mp4?token=HMwJuVUp43G4xpxmpbRCrO9wgW2sJWPIrmmeQSMcSnUPmT_CFvI_R8NDHTaXzFldTljejth7QW8iXDah2Sojsu-5wBouQKRquh4fMOJIXD_IJ9dXjK_xBnZn91HetxuGv7HP0evS4Qve_to-PsY8YukVPDdQK0swh7pr1NqLIGdZ8Phez9bEGjPHLM_NYC7nJjQ_So7uRQQxaBiqWeKH2e25pJ-8UGOFS5jXPkazwFOUhht4Y9d1xmkOaP_h5T8PDCcrnL38C7__FLTMtlHWEMbmyDOuzwhifAzBHZLBs-QP6QzxIAa7GMyFzdPsO0AZB2GwSMjG4WIyr7oqnO1yBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1738a6d5.mp4?token=HMwJuVUp43G4xpxmpbRCrO9wgW2sJWPIrmmeQSMcSnUPmT_CFvI_R8NDHTaXzFldTljejth7QW8iXDah2Sojsu-5wBouQKRquh4fMOJIXD_IJ9dXjK_xBnZn91HetxuGv7HP0evS4Qve_to-PsY8YukVPDdQK0swh7pr1NqLIGdZ8Phez9bEGjPHLM_NYC7nJjQ_So7uRQQxaBiqWeKH2e25pJ-8UGOFS5jXPkazwFOUhht4Y9d1xmkOaP_h5T8PDCcrnL38C7__FLTMtlHWEMbmyDOuzwhifAzBHZLBs-QP6QzxIAa7GMyFzdPsO0AZB2GwSMjG4WIyr7oqnO1yBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای وطن‌فروشان پروندهٔ قضایی تشکیل شده و برای بعضی کیفرخواست و حکم هم صادر شده
🔹
حجم اموال این حوزه بسیار زیاد است و تجمیع آن طول می‌کشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/460851" target="_blank">📅 10:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf30da4a1.mp4?token=f5u3-vCAwJbVQTBmuzXKw7nqc8otYjnKSHu1WWk_VEKo57n-XuC7yt_qRgvqUzyVR__9zfEpcf6gDSimFcgOjxVyhRKc-nHU4LBYQeXse1cGpgcHZUYZbBlOLdw9yEv1RLxXU_c1SF5iKv6t0DfX2wNkytBzmAsMJktxvpDy5gIkolPrwpnQntSQx5BslO5REf-n6MnU_uw1cL9mpm-9bQMGWcgVW49nKA5RsvOnzSYo3karK6XEsinHdGKXr1ud7dTXGKrcd6Qjk3KQXAPBP6O7n_oEQPQF817HLBOGpMrdiL15mjK7Ci9nlPhHHuuPGeZ-C6qEbXA1-M46YdcdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf30da4a1.mp4?token=f5u3-vCAwJbVQTBmuzXKw7nqc8otYjnKSHu1WWk_VEKo57n-XuC7yt_qRgvqUzyVR__9zfEpcf6gDSimFcgOjxVyhRKc-nHU4LBYQeXse1cGpgcHZUYZbBlOLdw9yEv1RLxXU_c1SF5iKv6t0DfX2wNkytBzmAsMJktxvpDy5gIkolPrwpnQntSQx5BslO5REf-n6MnU_uw1cL9mpm-9bQMGWcgVW49nKA5RsvOnzSYo3karK6XEsinHdGKXr1ud7dTXGKrcd6Qjk3KQXAPBP6O7n_oEQPQF817HLBOGpMrdiL15mjK7Ci9nlPhHHuuPGeZ-C6qEbXA1-M46YdcdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: مذاکره گره‌گشای همۀ مشکلات نیست
🔹
فیروزآبادی: دیدگاه و نظریۀ بعضی از دوستان این است که ظاهراً همۀ مشکلات را می‌شود با گفت‌وگو و مذاکره حل کرد.
🔹
اینکه همیشه فکر کنیم همه‌چیز در هر حالی می‌تواند این‌گونه حل شود و با این روش عمل کرد، از قدیم در روابط بین‌الملل مورد نقد بوده و الان هم مورد نقد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/460850" target="_blank">📅 10:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyM7KQDVeE-_DlC9ReyDlFA6doCfo9HxaMm0oATApRuGvQwJLOtJcD8ZlnQ9jEu2qBNt2VlR8zisjjbQ5uqpem0jPMxr2N-bG2AwSdobrx1fCh6dH3ijzy3V6w6A3EcdTI8aNC1J7toVEnCYexijirw1lKybWFO6SR2WMdRjW-BcQ6dnbEnA6tbjWXtF_AzvwYEtyp5TSNQHDfY9dr53T2PhbVIa1I2-69kpnWwfgw52s_onG0cjKfKwS2yHm8Q6Sh55ax1T60gT7Kv20f700dY7eah3M_Kh7ZuGvCWZYiSiMuIRkKWB7q_eDjp4bM6tgiqgTMEx58RHYeOyUxK5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده به مجلس بازگشت
🔹
در نشست صبح امروز مجلس به ریاست نیکزاد، برای نخستین‌بار پس از جنگ رمضان، جلسه به‌صورت زنده از رادیو فرهنگ پخش ‌شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/460849" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b357690a.mp4?token=Qw2MoYN3e7A89aopzySRD6tn7-2EalcDMACB5L1TMRmYr0HYqAOyg8Xf9_Ft3RnZBtQW8eN6aeys7yv_mjWe9bcRMTR9KTiqmOQe2oryoTi-WYhPrivWedL8PllyeZR9iABDXQONaiUkJIYSab2liPsSB8Q8ONN_K-cXe84YemKARk_7KYNvzKh0NZBIKJdUCluUj9BkESylqwHWiM2AxW5BZqrlp_tR8RhC865kNnMF-nhNe5KLpxbWZo34OJTuMxE0n3_QRQJX0DFplxRjnA-BMU9AYgMxqKUvs3CpJiZCkIBDn58vEDqtRKUjLQRN-_M0YMyi4jTLozkCToYgRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b357690a.mp4?token=Qw2MoYN3e7A89aopzySRD6tn7-2EalcDMACB5L1TMRmYr0HYqAOyg8Xf9_Ft3RnZBtQW8eN6aeys7yv_mjWe9bcRMTR9KTiqmOQe2oryoTi-WYhPrivWedL8PllyeZR9iABDXQONaiUkJIYSab2liPsSB8Q8ONN_K-cXe84YemKARk_7KYNvzKh0NZBIKJdUCluUj9BkESylqwHWiM2AxW5BZqrlp_tR8RhC865kNnMF-nhNe5KLpxbWZo34OJTuMxE0n3_QRQJX0DFplxRjnA-BMU9AYgMxqKUvs3CpJiZCkIBDn58vEDqtRKUjLQRN-_M0YMyi4jTLozkCToYgRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رویکرد جدید نفت ایران در برابر دولت ترامپ
🔹
معاون تلفیقی شرکت ملی نفت: در مواجهه با رویکرد خصمانۀ دولت آمریکا و شرایط خاص حاکم بر کشور، افزایش تاب‌آوری در بخش‌های تولید، توزیع داخلی و صادرات به اولویت نخست شرکت ملی نفت تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/460848" target="_blank">📅 10:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiJu0tNLS2Q9fUtXUlTdLQDMtk1l31zVjc5qAE9bFMQEslJMBD5-6zozmGnKa7-l3DR5_YitJ7ictgxGeakIqLk1nyQYrvo7iC6eFdyIbpGOgxJ_DXc1WHSf_nuHFpMYQzRT5w9dUGTIOW34OZQsRy7K0Kbg0fbWS6K2WiZJE0TZ6GKj2SotuVvWIE95mb888GTTMAYjcSRBTEM57nTSwrbYpl4b7PiMD6TDwpQkkNpD5avVnWXxh71TUkkZwLA87a6C3_bw2QlDoV70C13j7YtRPB9dOrJ_D0pKQIKaqQb0j8GhmKCtPot0AkkELYOVijc-E6_bN5vowtg31jNXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت زرد مجلس به وزیر ارتباطات
🔹
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح شد که نمایندگان از پاسخ ستار هاشمی قانع نشدند و به او کارت زرد دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/460847" target="_blank">📅 10:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460845">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251a5a71b3.mp4?token=FWGSv_5Fs5RMJA1Usa58f7yw6849JQhLS8wBngGxMWISm-oTHyDzROnyUaVFsSAvJze9oCL45VzU8D9Q_qplqKIPjh538Vg50YkqCL4ohV8nffPt4hZoSWuSGG8fD-QEKxGWcefgb-_WzuDU2BIO0Fy9i-IeLJvFTZ7kvnySHgYVNKqZeo7sJUrtR2Qkqb1iSv2G98mt9rUykEI_Xp3dKLSjJcLin4r71HZgXUVljju0rQ1m3TBa2ukw6VycVP7N2u_t7LUvQBNZpXmGSaQ1fGALAAP8MeDNySc3uM3a-ejfWGdv1ZjbV40qk1jy_1it9kpBApEgl9W0ZNp6OIC27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251a5a71b3.mp4?token=FWGSv_5Fs5RMJA1Usa58f7yw6849JQhLS8wBngGxMWISm-oTHyDzROnyUaVFsSAvJze9oCL45VzU8D9Q_qplqKIPjh538Vg50YkqCL4ohV8nffPt4hZoSWuSGG8fD-QEKxGWcefgb-_WzuDU2BIO0Fy9i-IeLJvFTZ7kvnySHgYVNKqZeo7sJUrtR2Qkqb1iSv2G98mt9rUykEI_Xp3dKLSjJcLin4r71HZgXUVljju0rQ1m3TBa2ukw6VycVP7N2u_t7LUvQBNZpXmGSaQ1fGALAAP8MeDNySc3uM3a-ejfWGdv1ZjbV40qk1jy_1it9kpBApEgl9W0ZNp6OIC27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات یمن آرامکو را به تعطیلی کشاند
🔹
وزارت انرژی عربستان اعلام کرد حملات بامداد امروز یمن به تأسیسات انرژی در جنوب این کشور، موجب آتش‌سوزی و توقف موقت فعالیت برخی تأسیسات شده است.
🔹
در این حملات، پالایشگاه آرامکو در ابها هدف قرار گرفت و همزمان گزارش‌هایی از اصابت به فرودگاه ابها و شنیده‌شدن انفجار در مناطق جنوبی عربستان منتشر شد.
🔸
این حمله سومین حمله به تأسیسات نفتی عربستان در کمتر از ۴۸ ساعت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/460845" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460844">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/efa5317854.mp4?token=R5AaikFeSJVByyQutVfAOcfIVe0J8F7uS3Ni1PL4b6R-cq-rcXSNt55wUzd46gLT6L8_4KUUV2uMaRs8FEQTQq3zYKJgZ9uvJUhJaXvS79AxLT9zQgcmCY9II2YWJ1tf4lmJaO9y_LoQvnpZtan556np8FzaPUe13ylu02hFARn_7m33mXnPzUVE8wYFIsYBuLIZVUGf13L8uoH5kAJrJ3V1Y6717CKKV2ilO0O-NsZxPvl-Bc37IigmHtmjvwR2tzI_EGF719IoTn1WHI3GBJjSz4PbhecgwbTB7HYiYVorTw7ZwRVpoQi0wzd4c7oB2ixIjzcttwfLK7pb0tMqWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/efa5317854.mp4?token=R5AaikFeSJVByyQutVfAOcfIVe0J8F7uS3Ni1PL4b6R-cq-rcXSNt55wUzd46gLT6L8_4KUUV2uMaRs8FEQTQq3zYKJgZ9uvJUhJaXvS79AxLT9zQgcmCY9II2YWJ1tf4lmJaO9y_LoQvnpZtan556np8FzaPUe13ylu02hFARn_7m33mXnPzUVE8wYFIsYBuLIZVUGf13L8uoH5kAJrJ3V1Y6717CKKV2ilO0O-NsZxPvl-Bc37IigmHtmjvwR2tzI_EGF719IoTn1WHI3GBJjSz4PbhecgwbTB7HYiYVorTw7ZwRVpoQi0wzd4c7oB2ixIjzcttwfLK7pb0tMqWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست جالب بهروز رهبری‌فرد از همسرش در «پانتولیگ»؛ «می‌خوای بری خرید، کارت منو با خودت نبر!»
@Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/460844" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460843">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">📊
🙏
یکه‌تازی «وتجارت» در بازار کارمزدها ادامه دارد
✅
بانک تجارت در پنج‌ماهه نخست سال ۱۴۰۵ با عبور هوشمندانه از الگوی سنتی درآمدزایی و ثبت جهش‌های معنادار آماری نسبت به مدت مشابه سال قبل، فصل نوینی از استقرار بانکداری مدرن را رقم زد:
🟢
رشد ۵۷ درصدی درآمدهای عملیاتی
🟢
افزایش ۷۰ درصدی درآمدهای کارمزدی
🟢
رشد ۶۰ درصدی خالص درآمد عملیاتی
🟢
افزایش ۶۴ درصدی منابع
🟢
رشد ۶۱ درصدی تسهیلات
🟢
جهش ۱۹۸ درصدی سپرده‌های ارزی
🟢
افزایش ۱۴۲ درصدی تسهیلات ارزی
رشد درآمدهای کارمزدی، توسعه فعالیت‌های ارزی، افزایش منابع جاری و تنوع‌بخشی به سبد درآمدی، نشان می‌دهد بانک تجارت در حال حرکت از الگوی سنتی درآمدزایی به سمت بانکداری خدمات‌محور و مدرن است؛ مدلی که در آن، رابطه مؤثر با مشتری و ارائه خدمات متنوع، به موتور جدید خلق ارزش و سودآوری تبدیل می‌شود.
📌
بانکداری به نفع همه؛ به سبک تجارت
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/460843" target="_blank">📅 10:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460842">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/460842" target="_blank">📅 10:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460841">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8Q3feZVWYeb2_gcsowhXuIIexKglc4AqngKB244fTepcU5zBLnbnUnNp-N9hl0Myf-Y_4v6SEgihCxVGOrxYUotLWtStVV5YLHDNfSUbuDJh7I7WIGXMD__fjoqKqvY-4EY-m5b7P0HOSrENcDsR_YXLxdbDHwvQAyIZiyNuW-tKDhAKGrmIcSkhw1zS2BG3ED9wx7rdclMnYYyI-WY15kWM1D2HpgfS4rE0P3CiLYrTRp3izOnBTHBcSM_ki5gau_x28AHid0pBjUuv2U_q5kC03BZbEfoyPD_KEa5CUEqKQ9AlpBJmg1a11_kN0EwjCAKL4t27KhLxHmwXBY0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تصویب یک فوریت بررسی لایحهٔ تداوم حمل‌ونقل عمومی رایگان در تهران
🔹
یک فوریت لایحهٔ تداوم رایگان‌بودن حمل‌ونقل عمومی در تهران، امروز با حداکثر آرای موافق اعضای شورای شهر تصویب شد.
🔹
رئیس شورای شهر با اشاره به اینکه «تصویب یک فوریت لایحه می‌تواند زمینهٔ ادامهٔ…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/460841" target="_blank">📅 09:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460840">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMwRneig66eTA2QJZPQbzZTYcQgrmZSq0cLmR9ALEruUqfmkkKxX6vHd5dIrkjZ4mx14AZ_YuHlAFTEQU0qsiGREdPdTBdInoegwnOBPisTqKq80m7ufmrVwjKA0ZaV8UN-b-XFzW9X4w60HiYHqnlQRmjUzKD0YhWirll693Gocx5UujjTVJFI_C40CHBYu4IuHHCIPqn0QTrdLgncQVVaijIRCI7RXsDrk_GyRUD6PJfYrcmOqP9_EM7KyKLHL-wMPhZoMMo9Ner8sfpLCJNDdV1Yex4xVGQ3rd9RXNHD8FosA1HONtzPM6xgyOyESzeGSYqOdARIinhdwp1oMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/460840" target="_blank">📅 09:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460839">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LInDRTKVGDDP1jFtVD-GUC3JMoEmpCQrjfYceunghI5XBGDAu6jZ36dXG5k3PwcPSdRdd6oyJsAZXoSoudxPQE6Mq7MPhvVl8UQXilCEoNsUpTwm5p4hVRP7mKMGFvSWj0W0zPsZIB_gThU6jEtjBoMLnZCBY_7qCz7iQzisrp-D3vPD7O5i_BDicMiiNXKXbPgIPUiOOOWsG_K0_DSDhHz-6aySKCxH1oBv8-WeRHYheE2KkMt3NcOd89UoUTsn10etkuANwXXwSx2JPyr3YFqydMdgR1VQXMryKpXkgxUe-vehpYJhKQ4lmPgHiEYoZmK2m23FSBS1UANxK8pMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای «بانک» مخصوص جنگنده‌ها
🔹
«بانک زدن» یعنی
خواباندن جنگنده روی یک بال برای تغییر مسیر و گردش
؛ مانوری که در پرواز ارتفاع پایین، مهارت و دقت بالایی می‌طلبد.
🔹
«بانک زدن» یعنی
خواباندن جنگنده روی یک بال برای تغییر مسیر و گردش
؛ مانوری که اجرای آن در ارتفاع پایین به مهارت و دقت بالای خلبان نیاز دارد.
🔹
در
جنگ ۴۰ روزه
خلبانان ایرانی نیز در مأموریت‌های رزمی از این تکنیک استفاده کردند؛ از جمله خلبانان F-5 که در عملیات حمله به کمپ بوهرینگ، بخش‌هایی از مسیر را در ارتفاع بسیار پایین طی کردند.
🔹
اهمیت «بانک» زمانی بیشتر می‌شود که جنگنده در ارتفاع پایین پرواز می‌کند؛ جایی که خلبان باید در زمانی کوتاه مسیر جنگنده را تغییر دهد و همزمان فاصله خود با زمین را کنترل کند.
«بانک زدن» چگونه انجام می‌شود و چه نقشی در پرواز رزمی دارد؟
🔗
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/460839" target="_blank">📅 09:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460838">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPJRCB3wH4EcdFnkzkkoYlAxpjgUqE6ZEU1dQ37Y3Q_UghhLEvMliXPpck9wgx82tXLwIidumj3FrKG808hHHRn4wX3Et-7N5nGxXxFd_xtKopSk1evGlWHj2wr8Jb8J6rMpvzV2mohbddY4S3JQXDwSyL7smJM2USakcktMg3FMgX1mW7_ancBlj3iQ4KUok6wjazdaJl9oE8bKr4FPNsb0sXzD0Oyyi8ybSkU8SDsXrgOL5BZrOKHouq3lBMJgeBv3d177UMdm63yM9ghK1rs3HfhIShcoKhGRm4j6P4BNKSkztWo8oDExmQ7Q6D-fRT6LSsdmSEyeuS5x--sAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۷ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با جهش ۱۷۶ هزار واحدی به رکورد تاریخی ۷ میلیون و ۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/460838" target="_blank">📅 09:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460837">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5QI90z2s92eRFvcuNjyHv3UgEX1mAqRQzcdjCzOeoAuyv7rHmApF9bSXzNdja9tQ5zLjzunwKv0A1TET8R2gVA_t7AA4oe9YdSpKDz8Zry1zH95GOddSYAx_DTKJdi5c2w9XCII3D2VXzmofsOdQoO0i1610YUTEcNQIw4nqtAC5SYbad9wohn_L6OsifBSohyN6O-nk1gfQVfzvlQL0QxTGG2qSj2Y9iAcyypmqxeLHNntIWG7_rsSZJYs4EfK1JtbmZU6O44DUCUzPLNHOLNM8Vhvj7pOaoeyRSzko28zsB3bM-liTRQNMSxOWa9f5Z1t9H6Bh4ZgnuVUGnWRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به ترامپ: مستعمره کسی نیستیم
🔹
اقدام رئیس‌جمهور آمریکا در انتشار یک تصویر جعلی با موضوع تعلق بخش‌ زیادی از مکزیک به ایالات متحده، پاسخ رئیس‌جمهور مکزیک را درپی داشت.
🔹
شینباوم در رد این تصویر منتشر شده توسط دونالد ترامپ گفت که مکزیک، مستعمره هیچ کشور خارجی نیست.
🔹
رئیس‌جمهور مکزیک در شبکه ایکس نوشت: «در ماه سرزمین مادری‌مان، بار دیگر تأکید می‌کنیم که مکزیک مستعمره یا تحت‌الحمایۀ هیچ کشور خارجی نیست و نخواهد بود. با افتخار، ما یک کشور آزاد، مستقل و مستقل هستیم.»
🔸
در تصویر ترامپ، آمریکا، مکزیک و کانادا را با رنگ‌ پرچم آمریکا نشان می‌داد، در حالی که سایر سرزمین‌ها نیز زیر پرچم ایالات متحده به تصویر کشیده شده بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/460837" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460836">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49b3dc7c6.mp4?token=OBlmn4O1EqemWQM0NAiurnOzGCL-pM0vfkcu8OIKcNXqY3D_OkY59-pSvOCYT2_5m35HKtbYZcl23dAdacObRS3b5aSly76wHcwANsOwPU317VWRiuuZpvpA7RVKEGOBLZDeIFwFkv4gQb1Rlk2mpio2fl28V2MbKQQ6q_-5TZ5QwsvKSxuAd1-Ref2W2GpPUyI_vBgYJFmG5paO2M0MC7DIiGWkKgWJbhbE_UCRYBVsRZzOG23l2peuz9SQyQ8ODvAH7HdEYft4TbaLzjDE-vorf3AszRubf01TmrY0WgaWB3sOBTSggKyU5uUeqt30UXmVmFMirUKI5Ecz4K1AAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49b3dc7c6.mp4?token=OBlmn4O1EqemWQM0NAiurnOzGCL-pM0vfkcu8OIKcNXqY3D_OkY59-pSvOCYT2_5m35HKtbYZcl23dAdacObRS3b5aSly76wHcwANsOwPU317VWRiuuZpvpA7RVKEGOBLZDeIFwFkv4gQb1Rlk2mpio2fl28V2MbKQQ6q_-5TZ5QwsvKSxuAd1-Ref2W2GpPUyI_vBgYJFmG5paO2M0MC7DIiGWkKgWJbhbE_UCRYBVsRZzOG23l2peuz9SQyQ8ODvAH7HdEYft4TbaLzjDE-vorf3AszRubf01TmrY0WgaWB3sOBTSggKyU5uUeqt30UXmVmFMirUKI5Ecz4K1AAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ بانک‌های مازندران هم امروز تعطیل شدند
🔹
معاون استانداری مازندران: با توجه به آب‌گرفتگی شدید در اکثر شعب بانک‌ها، تمامی بانک‌های استان امروز تعطیل هستند. @Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/460836" target="_blank">📅 08:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460829">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsWCm1NLZUaMMJ6YpCyQ3mSe6P0CiRQiS2a3KLnxO8g4_m3VQOdKawgMTqGovssl6J9eNrDOlDyeEQuFvGpg_1eymkifIvrl7RayRo8KXWV6lN5lFfcBgscOvp8VhBjKjfhn6kd1q_7i6yJU_XjTgJ-3mw-K2sf2GrPcnjjdx0q13CaMneg5bKdlBfNoaHq3dID8TQuOBsds-vXWc0q9JzfjT03fr59iuMQygIk-LA7MG2MpJcxAOJOcQ4se5KIkDXjEAuErjI8c_VXDL4t6L61IVJPlVoU0nbw697fOovbjLr-Le3zTF8zCwGRPzyIu61WlyedfMknUmS30FFqa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaKMpNbAPIIgqV01vVASUXYM8nQB6ODoNLMXcGsLc02OnlWj8AHv010_uZi4N7fUbzpMsApUIi6tpDNMjOS2u71nJqLJVmDjD7MK1W-QVAlUuXoJ4tn4NgbQNF1PIc_VcTDij2dvTYZqb_fRKuWt-Dz0cxBPThYPaUlRGxQoar0qAXl4uYDps-Evrwh2zkaSFrHZMaFtN8q0gPoYCHSofGcAgdkG28kmWAVgPCxP1APLZLDpsH0HHlSuThRzvZiyKbG_RHIL7wwX57W7yiZyIDKJcHTrHHnK7C6OXL2hAVA6lr_qothxlIXJyhCKiGpsQOHRoTletoed88f1LcI9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6bqnUdP-A6auXYaDJNiyVE-gnakIrbJOSSRNvhKHbCcumi40QPnEQ7Tc5pkboD4y96ZXXC-f-VvtginQvEcsgiaqNyUviW_H8-KzWk-EPGDsnp7LcfE2jxxZRiO1rPAoKEYpMu6Wm9aN7TnTVjE6UbwPdvEQLWPy70LGGQLOs6yewxEWZNUB3xzMoMqcVuowxnTQdQwMw0bPKpLtH0-361UQL8MOOgNclSxalDP9hdxmVMFa5-jtev3_P6iTuEdnEuQVmkwBrIlIuocFdMPah5Y182vtOeb4nl_h-IWZG_0AYZbEr3l1d94wP5yq6tMqFDH85f9ll6zhTa1UEYGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9NTG4I3F59E-0JxADFL4yY7I6U-BBYMUnO4UzFQJYx58rcS5oqvvhJu3tUtyvxyzuD9uAHL9ctzBPwYraGls_qEqwWvJ2hhy1lFxyv-tAcqTCTRzOOfTFLEq9dn-NX6w3pfybX0BJn0AtQtgjF5y_x0oy_FEfVI8dVVZTpkIqv3M2v0QnGyD16JoPmsTHzYQzkwK6CpD2-5FgtJZe6jBRgnfiksRGOqDEyuqGgEg2Lnls4-7_T4ipUncMhpjHwnCk9tZoBpOYCVFwOvKolE4slS0ZdRkXa10u40my8wyJYgrjraDF4mOjrtJq_L7h4Z7qsw7iXgB-6QzmY632pF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pL8ToRKaI49zizr8HG3W0BHAiEbblFmBtfCQx5qCGyY5OGltlAKSZJgn6O7dYuizPVazLR2RNiPIulU0BMW700hFGPBlJE2MMbzEKQE5SAtDn2UI9QozI0UKrBXlXKyG-BSscfWaBH8CmlEeRjJGRkiox2n4ctZmRoH7xebbraPbqKBLzKVzk2_hhwjlP-Rvrej0TCJEwzu22yRds8j2jgcI7kzZYPJXZ5KGzE3g4Z6g-YiVsFbRLHnvVzWb2Z8Vke6CM74aAOAEpUeCnRNJ5JvVogewNqVJrnnNCaHGng6xnqNTd3g2QtEo_m90dhvJ6V_jpUR7ZxSAL3kQw8P2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxr-tDmYZ70ZdJLSvjBc7KubXbTA_epTYneKeHP48FE0gzh3VKkTtH9KbJ93NWYLTDT5FnTX-0jY6sG8QPL4othPJrwQWeu-ZxpnjYAhXVP3z80h0M7XL7nh9yhTT3NNlthZKKwkgJfMZf0KTaqFFMK0vO2zzDNWPhO6_sSv0YBLjFpM3sf4PEFZptQkEILbLcOkyyZjDK_jqwCxxLX62QDxOhAldc9qbOc4uKSD9rsOiyncusjQgiJzgBKY4wddSE7XtpNuEK1NtL_GE8hPVakrpl3sloBCmSur82lu8lohg-I54QL8VxxpKtWxHyzgNPD9tLX-TNeXo8c1KG10LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8PDWcAXVTRgU5R-X-h0fdzPzrYzhqMxaXWWHMKTOqIIpvfPZNg_IueE0o28MVQXvNBcZLDZs3SBtLubrPrnrkudScvQKoAdypJDGO33D7Tn1kCKGZJMuKepQV7gCUCdNMeXTLMwFB_8o5Z6htSaT-N_66-D8thlW0REthcDzvMLlBaKO96UMreNxXWWXWHZu9FWAD9JeJxqFJdEVvHngchq9_BywMRYqnXMDNzTLZmx83QBG42H-G7hu0yjMnglD9shRIXfp9XJtGuttqeKYI4nQy-Q02fzAu9rblFirk-A-zeXEPx3jBVvEbLc-ZBCDnGgVX4hp5kbOcePltRXCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قالیباف در حرم عبدالعظیم حسنی (ع)
🔹
رئیس‌مجلس شامگاه دیشب با حضور در حرم عبدالعظیم حسنی (ع) ضمن زیارت این مضجع شریف، با تعدادی از زائران دیدار و گفت‌وگو کرد.
🔹
او همچنین با حضور بر سر مزار شهید سلامی، شهید امیرعبداللهیان، شهید علیرضا بیات، شهید طهرانچی به مقام رفیع این شهیدان ادای احترام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/460829" target="_blank">📅 08:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460828">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MibG0KNANJeVfhrRHmNajw6ZR5X26mCEkgVLWbJo1uXjfB2-ql_U8sJBYMRLZde5CfKpPYh687ZT1RRQEsbvbO2s7MmxXG6Y0gAKGkY6vvXRthWxgIspfvGWuQzVT54Jw-U6I2fKjWmGFDwsotLbWfrb8BjhYuJBl1j0wmCF5LzEsSeDhmNe5tjoCYG5V4AuLp4_jfD7pKUOuZFIUJ_yYxagbseLWHB1IYAW400I8unMiH8WTibNgm9Wf5FajWdgPEMERlSA8T6DHkfcmqZypzvRJUcEjd9rvrjvzhMWFKNEiHiUWmADzowzRVIlcu8QNPS9S3E0xfKuGRpgq1ESZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نرخ سوم بنزین رسما ۱۰ هزار تومان شد
🔸
از راس ساعت ۰۰:۰۰ بامداد ۱۷ شهریور، نرخ سوخت سهمیۀ جایگاه‌ها از ۵ هزار تومان به ۱۰ هزار تومان افزایش یافت.
🔹
نرخ ۱۵۰۰ تومانی سهمیۀ اول و ۳۰۰۰ تومانی سهمیۀ دوم تغییر نکرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/460828" target="_blank">📅 08:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dzpz9eMdOa1GCwz0kkS6bsXRcfLsgOTUlkDC2RU0UAbon_E3ZQnZflBzHBMQNbQh90P0iY6wwgSGDGjFJ1ds2pw0Bogx1r4YBT7RKCVOfK5PxiGQVLgdjZRC6kgjpNlMi1_8OjfCKK0FwIWJRdt4RU3VLaYtyKv62eUZ_iGYNfK2c-nsln4q6rmnb4DjTz1QMalqLIQOI8aTCg6mZPMP9XIzMD69YMmrXr83lyULgaOd_NucGnN-dAc2dTJoVUe8fW5NT8KSBzntspwxMpZUNA2cn_oxH03rtKFgxGidhGmsr8z7bcwNfClYZMfKDyURGCsrM99qCvjhBf8JrJLF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط سنگین گرا برای جدایی از پرسپولیس
🔹
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از دنیل گرا در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
🔹
در این‌ بین، گرا برای جدایی از پرسپولیس خواهان دریافت ۶۰ درصد از مبلغ قرارداد خود شده که پرداخت این رقم برای باشگاه پرسپولیس، سنگین است. به‌همین دلیل و باوجود مطرح‌شدن بحث جدایی این بازیکن، فعلاً تصمیم نهایی دربارۀ آیندۀ او گرفته نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/460827" target="_blank">📅 08:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/460826" target="_blank">📅 08:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌ هشدار پلیس‌راه مازندران دربارۀ تردد در محورهای استان
🔹
با توجه به فعالیت سامانۀ بارشی شدید و احتمال آبگرفتگی، سیلاب، ریزش سنگ و رانش زمین، از رانندگان درخواست می‌شود از سفرهای غیرضروری خودداری، و هنگام تردد در محورهای استان احتیاط کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/460825" target="_blank">📅 07:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e27328e6.mp4?token=tWNNygP4XuYQtsBCV4bvp4PNPy6wetaBEBUNEz9xYTmkOHfXsYmT1ygMKXh8SrmDooh-I9uljN7ZC1IUgjWfZn4SAzMiWqwGs9ZDKhRDfrvG6Jp34_YHw734kQ9QMq6bWhjD2zlc1fekOXMhO4t6XQsuujwun553n3pHh9_zAawTVKbF5qqHUTV1LWGQx4lLpoxLJbrfid8e3gbRJ_FSP71hZE8vb3a97AIAwl70yX3wG1QoMh-BeOyJ8r9bVx11b9ZCO8-V1jNwRk_KqheoMgCsTFD4jEciXtVbYu8FcKLBycDZj_yMoGRyg9uxsZPv4uMqfbQ9OUtXi2D2MNDpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e27328e6.mp4?token=tWNNygP4XuYQtsBCV4bvp4PNPy6wetaBEBUNEz9xYTmkOHfXsYmT1ygMKXh8SrmDooh-I9uljN7ZC1IUgjWfZn4SAzMiWqwGs9ZDKhRDfrvG6Jp34_YHw734kQ9QMq6bWhjD2zlc1fekOXMhO4t6XQsuujwun553n3pHh9_zAawTVKbF5qqHUTV1LWGQx4lLpoxLJbrfid8e3gbRJ_FSP71hZE8vb3a97AIAwl70yX3wG1QoMh-BeOyJ8r9bVx11b9ZCO8-V1jNwRk_KqheoMgCsTFD4jEciXtVbYu8FcKLBycDZj_yMoGRyg9uxsZPv4uMqfbQ9OUtXi2D2MNDpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش‌های سیل‌آسا در شهرهای شمالی کشور  @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/460824" target="_blank">📅 07:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b236108324.mp4?token=royfZsmEXJFK8Ch6NyI-XFzTwn4io1JtUUWaKD0Y33N_FC5x4tzj62xcOXAzbiRch6bfmLUS0odTDAF8L9OCXDj9p-SbYmK1BMstO9dSp7LArNrcWTJT-vVaeJlqOWBIusj270PQhaBXlld8Ibya_uzwd9UP8cAkWZt60W94pN6WtflWHsML1caRFH5TT0R2QClefhO6A3jvtGthh4koylc-SaRDW4Gec5_RrMnMnwZCYa9751bmvQCNgt7SHlzzBrastoaGWz3GH3SolnAiH8FTITZr8czMwcZxTL4vwMUbW4hBYzM57HS631sYtOJVoJOI422eJkE8NYzbYASA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b236108324.mp4?token=royfZsmEXJFK8Ch6NyI-XFzTwn4io1JtUUWaKD0Y33N_FC5x4tzj62xcOXAzbiRch6bfmLUS0odTDAF8L9OCXDj9p-SbYmK1BMstO9dSp7LArNrcWTJT-vVaeJlqOWBIusj270PQhaBXlld8Ibya_uzwd9UP8cAkWZt60W94pN6WtflWHsML1caRFH5TT0R2QClefhO6A3jvtGthh4koylc-SaRDW4Gec5_RrMnMnwZCYa9751bmvQCNgt7SHlzzBrastoaGWz3GH3SolnAiH8FTITZr8czMwcZxTL4vwMUbW4hBYzM57HS631sYtOJVoJOI422eJkE8NYzbYASA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران @Farsna - Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/460823" target="_blank">📅 07:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_z25Z6fyWrn9tEULHVxcgjQd2ND2y-4Femd4NNyInIvoNIGR02FZJktMB_TlAa2p5NTcHw61JcPgBA-2tgvSs0NCs6bHvIhuBynYRkJPuOhigXSjJ2-eEWVKN6zPpfMIx-GWOX2bHHgjI7WCeICamfBZxNB7cfKeJVbLy4Zg2oBsxZxWfyXDWhmKgpTUaV9Ngc5j3kB7CPrzbBkIy3rakqFk-HGL6GpBvJPR_JPrpmIQQD_eZrsmjlDjc5OwWeudmM-_UEHELlPOVMVdgqchfD69OKCQUz3fnRq74YDmfelE9NN1CB3xzG3cTIpk93v0fv6Ycs-YI9ZMjV3wwFNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای مهیب کی‌یف را لرزاند
🔹
رسانه‌های اوکراینی می‌گویند که ارتش روسیه با ترکیبی از موشک‌های بالستیک «اسکندر-ام»، ابرفراصوت «زیرکان» و کروز، پایتخت این کشور را هدف قرار داده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/460822" target="_blank">📅 07:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70365c549f.mp4?token=vLB_vWqQchN3kxNk1BZFWkmI9Rs3W8YAIyUv0vFQ0WZHMy7ei0Hs9IAnfQDGV67dqLbSrzxgrfTAqmlbEBjSVwZYCMCuu1K2nat3PJr4HCMIdoGNJq0AJMNBTt7lww1_LTunkjzLKWR3UMbYXqTcijd6pSzn2clRZoOSovs4GI1z01PxV_iTvI8DyBwtvr9ZERiL_AVxuNZitVA3sC-wc02ZgqRyMBP5o3TlKkyqTQM72bdeaVL-um2d9Ez1OsbbhIv7VlfhPkFbkVN4mHiNfy6sUOi6CC65vGtl67mrodnlyUNkow5gkh7kI6KiKtVL_b71ndc7txPOk5NPq7Vjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70365c549f.mp4?token=vLB_vWqQchN3kxNk1BZFWkmI9Rs3W8YAIyUv0vFQ0WZHMy7ei0Hs9IAnfQDGV67dqLbSrzxgrfTAqmlbEBjSVwZYCMCuu1K2nat3PJr4HCMIdoGNJq0AJMNBTt7lww1_LTunkjzLKWR3UMbYXqTcijd6pSzn2clRZoOSovs4GI1z01PxV_iTvI8DyBwtvr9ZERiL_AVxuNZitVA3sC-wc02ZgqRyMBP5o3TlKkyqTQM72bdeaVL-um2d9Ez1OsbbhIv7VlfhPkFbkVN4mHiNfy6sUOi6CC65vGtl67mrodnlyUNkow5gkh7kI6KiKtVL_b71ndc7txPOk5NPq7Vjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ هشدار پلیس‌راه مازندران دربارۀ تردد در محورهای استان
🔹
با توجه به فعالیت سامانۀ بارشی شدید و احتمال آبگرفتگی، سیلاب، ریزش سنگ و رانش زمین، از رانندگان درخواست می‌شود از سفرهای غیرضروری خودداری، و هنگام تردد در محورهای استان احتیاط کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/460821" target="_blank">📅 07:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌ برق برخی مناطق مازندران به‌دلیل آب‌گرفتگی قطع شد
🔹
بارش شدید و سیل‌آسای باران که از شب گذشته آغاز شده، علاوه بر آب‌گرفتگی معابر و اختلال در تردد، موجب قطع برق در برخی شهرهای استان و بروز خسارت در نقاط مختلف شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/460820" target="_blank">📅 07:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
بارش سیل‌آسای باران، طوفان و رعدوبرق در مازندران، در بامداد امروز
🔸
در پی بارندگی شدید و طوفان، کلیۀ ادارات استان مازندران امروز تعطیل هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/460819" target="_blank">📅 07:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c763e8ae68.mp4?token=i4qNiJhxJvK_X-WEQ5_u1UWE9MIk2Zn-1T6T512rYS2jtQfKVcQnamYbfHc4BTf31kgHBMzdxPPZ8hmHhAG1_3Wi51prOTiC5MGvUD9O2kDBLPFdH0i8Ep92uFyT3LINrMTgxUu1RwBO-Xa_uZZ_EKeRrOuxln82x6ywOIMYDA04IFHwILfpj0y_MXFA6c95NRUtwNARsPSu05vKutP4yvAzJx9bdEBGFXiLZgI-XMgnugEOyLsrkYb0MzaFzByVokKB1ACvNoIrrWnACNXMdl7AWZI6YYKrmudYCKa5QS8C32rN4WDX68bt81AMMHfCTcnC043atpe4TtYY_C_BBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c763e8ae68.mp4?token=i4qNiJhxJvK_X-WEQ5_u1UWE9MIk2Zn-1T6T512rYS2jtQfKVcQnamYbfHc4BTf31kgHBMzdxPPZ8hmHhAG1_3Wi51prOTiC5MGvUD9O2kDBLPFdH0i8Ep92uFyT3LINrMTgxUu1RwBO-Xa_uZZ_EKeRrOuxln82x6ywOIMYDA04IFHwILfpj0y_MXFA6c95NRUtwNARsPSu05vKutP4yvAzJx9bdEBGFXiLZgI-XMgnugEOyLsrkYb0MzaFzByVokKB1ACvNoIrrWnACNXMdl7AWZI6YYKrmudYCKa5QS8C32rN4WDX68bt81AMMHfCTcnC043atpe4TtYY_C_BBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/460818" target="_blank">📅 07:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460816">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253c13e9c9.mp4?token=IHdYnmV_6RaD4TDgwDc9OQaIZWYl_6hR8U4ZstsrFZFf5-7WEWfcvKeJAZTX5DHFb3T9c1gIP00ED-Dt3Hb4Hj9TifbSf79S_wn1e1_af0YAu3w9x9S78_fbRIQr0xotcyJQ-g_C2O4WOgE3sxyayQxYav97cQjjX1MCnO1lbHwRkuBV-d1Pz2iDRkm93VBvB_WigYo2hEnfDR2CBkJz2tmg_WEh_o458ceibzb2EIQrNGRUxsAD4nSlQlL7PJuoa4x2qopsLkCY5zUvS7NwGIK9Q9GsUKfyheWQwt_hCnYOd-EO38_cut05zo1cXL-JRneYhUqXMR204IzC19hp6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253c13e9c9.mp4?token=IHdYnmV_6RaD4TDgwDc9OQaIZWYl_6hR8U4ZstsrFZFf5-7WEWfcvKeJAZTX5DHFb3T9c1gIP00ED-Dt3Hb4Hj9TifbSf79S_wn1e1_af0YAu3w9x9S78_fbRIQr0xotcyJQ-g_C2O4WOgE3sxyayQxYav97cQjjX1MCnO1lbHwRkuBV-d1Pz2iDRkm93VBvB_WigYo2hEnfDR2CBkJz2tmg_WEh_o458ceibzb2EIQrNGRUxsAD4nSlQlL7PJuoa4x2qopsLkCY5zUvS7NwGIK9Q9GsUKfyheWQwt_hCnYOd-EO38_cut05zo1cXL-JRneYhUqXMR204IzC19hp6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/460816" target="_blank">📅 07:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460815">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
تعطیلی ادارات مازندران در پی بارندگی شدید و طوفان
🔹
در پی تشدید بارندگی، وزش‌باد شدید و طوفان، و با توجه به آبگرفتگی معابر و اختلال در تردد، فعالیت کلیۀ ادارات استان مازندران امروز ۱۷ شهریورماه تعطیل اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/460815" target="_blank">📅 06:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5qtKI8iobiSPhtA_l35vr6DawiKMv7FHoQ8kHk3qa1uprp41WdG61lEdPF3PBAtAKC-sqwuW_OekjMNoq_MYbOYAH5TZi0hS04B520smO5jY2y3t6-mxz-iwy0o-Gzz4QlPflLQnodsn_1MKDc9-iaiW8ILeS49MvzRx00E8xJ1AyFoWfib0SDdaFc2kWSK4zStHsuKmdtCF3iXYQ7nBSRKTiCbackCySAItmp4m3FF6QaFF_Qs6BsD8gtgFtrTPzc8nfLgQBlbdFHo22U-3syud4_MZdeaXyXAOaOWU1LQOaH5uDcvoeXxsPKpfLF-PbfNgC9EAlC7tRvtqVCnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ct2LyK0886BowicFtxLDrgMtJMQHOZ2-HkFMUGQNWJP7HRWFypxFGPxZeQFM2AMiaQrZw2J7h6dZamVZk2V1gfQx6_sxgSGAuOpr8FvQdVI6_wFRs0IMLJ4MwZH4iyiI5I4KF8WbuvQPa-0TzmbQTijlvK2SfKqdes_8lMAo_nlpTcJJFOvYzS8BjzkPk9ExV21ROjeK3KZN9yVrOBbcYLKK2e2FBFhMTBzE11fRjtj4RrYsYss5Tpw6kMroCv2_3YPBki2yF4Sgd16zYulOmDOUVpG0pLWvz7SwADir_Tmc2QmtiQRyTuPZmJ476RbMzb7GCkefKrTYzWboLHDkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUnwNExslssZufYD1b8PKteRVjxrvamnOvzChVlTKejL0CmMozejO_UsQv000U0grN5sZHR7le9xKw0o7oCgzLWzjTgPMBEmtQDcEd_-uUKDcqhzSSea4J1kCdWytc5R1dLL5QcToL0Ne2_s92jga_dtEYs3146m6QQM7jnBGg0xVbH7xRp455a3ALEF-pWv6Vv1CahzRPUMtQX2YFfYjYBUaoh8yz7XS7w9bqpMVkJVuiBW_5fKmzRQfy6au6nmVRURxrKDmm-z-l13av8FGEwBpGfheINOsj62PYSwId1_rcIHnBNh-icdChwYAHfn4yud7Ei-3v52T6C-dw7qDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست کمیسیون امنیت ملی و سیاست خارجی مجلس، عصر دیروز با حضور سید عباس عراقچی وزیر امور خارجۀ کشورمان برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/460812" target="_blank">📅 06:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اروپا برای اوکراین موشک پاتریوت می‌خرد
🔹
باوجود هشدارهای مکرر روسیه دربارۀ ارسال تسلیحات توسط کشورهای غربی به اوکراین و مشارکت مستقیم در جنگ، اروپا تصمیم دارد برای اوکراین موشک پاتریوت خریداری کند.
🔹
منابع مطلع اعلام کردند کمیسیون اروپا درخواست اوکراین برای دریافت موشک‌های رهگیر سامانۀ پدافندی پاتریوت با استفاده از وام ۹۰ میلیارد یورویی اتحادیۀ اروپا را تأیید کرده است.
🔹
بر اساس گزارش‌ها، کی‌یف باید قبل از تصمیم‌گیری درمورد پرداخت‌های واقعی، قراردادهای خرید را برای بررسی به نهاد اجرایی اتحادیۀ اروپا ارائه دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/460811" target="_blank">📅 06:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حملات رژیم صهیونیستی به نوار غزه
🔹
المیادین: تانک‌ها و خودروهای زرهی رژیم صهیونیستی به سمت مرکز و جنوب نوار غزه، و شناورهای جنگی این رژیم نیز به سمت غرب این باریکه آتش گشودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/460810" target="_blank">📅 06:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7FxBxbNygtJDcN2BCxUvOkAbG3_u4fKzl27_BZqGKXc0UvznJorvRw0-5D1074XDT19ciBXuTYJvUcSRxMrobZW8HXvuwlVuEDdMmLHjgH43nZgvgijvXJcD4yO5LK0UaHKyj4TX7g0w3UL-t0ScPSjKRgS6rfQqcF_F-3R-bgKVOnlvVLD6pFHtx-nMyyf7D71RCZ7x0_76vU4OweagBZ1ucbnBIex__rhKDLgbIToQqJ7rPZ0Wli2jxreIeLY9sJ9_hldbGl1U_YbwuZGBy_5rHevvoajiaPXsxTOE_GIVsghM4tDcoPG3UVdDPTtr6I--ZPobXWWwXx6dAZlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای مهیب کی‌یف را لرزاند
🔹
رسانه‌های اوکراینی می‌گویند که ارتش روسیه با ترکیبی از موشک‌های بالستیک «اسکندر-ام»، ابرفراصوت «زیرکان» و کروز، پایتخت این کشور را هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/460809" target="_blank">📅 05:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bff62194.mp4?token=PUMkzMJO4-hTLnWKN1qhLAPKGL-TrGFrw-jcqh2nNSVyFTruWbwppfyzCI4J5FqjBiy-5PsUIxAvp0AmsHhZD9zFY-mzfLFmD2jR0M0GDj59UIhZJ-AJ9pZnDUbZPYT3u1cjvSc91sgDt5wRGzyclQPGrszzDNM7Gb_QybZGL1Yd8UPONNuMO_DCRh2AcsQQ8zBNvz-RRC3MxviPQpm_1kGlfC3Gr9St91nFoxJny6KKeMkNHT3Lt7XLK_0giqJEmZbIw3X8_HJuiCfFdvsMuHXQS2U6oz72KiTsxYju6v-VooiuizBgTcNVkGt9pcl2bCzSnkanVNwt4F8msVhgvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bff62194.mp4?token=PUMkzMJO4-hTLnWKN1qhLAPKGL-TrGFrw-jcqh2nNSVyFTruWbwppfyzCI4J5FqjBiy-5PsUIxAvp0AmsHhZD9zFY-mzfLFmD2jR0M0GDj59UIhZJ-AJ9pZnDUbZPYT3u1cjvSc91sgDt5wRGzyclQPGrszzDNM7Gb_QybZGL1Yd8UPONNuMO_DCRh2AcsQQ8zBNvz-RRC3MxviPQpm_1kGlfC3Gr9St91nFoxJny6KKeMkNHT3Lt7XLK_0giqJEmZbIw3X8_HJuiCfFdvsMuHXQS2U6oz72KiTsxYju6v-VooiuizBgTcNVkGt9pcl2bCzSnkanVNwt4F8msVhgvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار سنتی ماهی و میگو محلۀ پاشهر بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/460808" target="_blank">📅 05:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFQFt-LatKsPSxpjzyJQYyPAQ4q2OmksSI-HapcE0QkHxKXAQ7Rj4acD9XmHJIvZzLS_XzBU7Wl-B-mhb9YakyYnInQaySdp-9wIcNpzTZ5wFu7k63F7Y8Qz4lUREcqcK3oqopfRe61Mxm9YhpTUxE0XxrudP1acEx8EKy60vgXISPoyuf61FJMiJc-eHJJRfrKE37ClLj8PxltJVNP1YLiUBTdLjeWioWJOFxDL9nOdlZD8fyAjbfceVUeIVZnCJ5C5aLcTpYXldjDiGpn9u7D5H4kPxfQtBboBLyoz6XmfWn-ZRZTFe_JX0Paequ0g03qkz-gPlLE4YZRhsR7orw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش ماکرون برای ممنوعیت شبکه‌های اجتماعی برای کودکان از طریق اتحادیۀ اروپا
🔹
رئیس‌جمهور فرانسه در نامه‌ای به رئیس کمیسیون اروپا خواست که دسترسی افراد زیر ۱۵ سال به شبکه‌های اجتماعی در اتحادیۀ اروپا، به‌صورت قانونی ممنوع شود.
🔹
وی با بیان اینکه وضعیت کنونی نیازمند اقدام فوری است، پیشنهاد داد که در قوانین آیندۀ اروپا ویژگی‌های اعتیادآور رسانه‌های اجتماعی را تعریف و تنظیم کنند. همچنین از همان ابتدا استانداردهای ایمنی، از جمله محدودیت‌های زمانی برای استفاده از پلتفرم را معرفی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460807" target="_blank">📅 05:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127c8d7ef0.mp4?token=Cr1CHcZHrQG9bkxGnA0RoaFsPlTmmpvra-rjGzk45NoCqwNJbibAU6yAVWGCvA84TDiA2eILtU7ceYJ7NNLjg3mVxhaptg7JPMvzbCEEgOsgRNhiV9bYSy2oXRo2L_NcOFtIFvzHToZTbUwrcEWj2x2jg7lvPe3x0VuJ631hUfzS5wKZY8ay7yhsHGZbmZ_bL_AwLJHapRNQAasjeZatlemOKHdPWKbbJPHF-wSmHtY5k_l-8xuELWsph4p9kLY17FvynjDyUGs_THaMuUknpQfcLPVkesTt2jLEgPAJ-tuBPc8Mjt-zVwBdBEYmgdADJKUW1FpxjYws0v8WUuDCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127c8d7ef0.mp4?token=Cr1CHcZHrQG9bkxGnA0RoaFsPlTmmpvra-rjGzk45NoCqwNJbibAU6yAVWGCvA84TDiA2eILtU7ceYJ7NNLjg3mVxhaptg7JPMvzbCEEgOsgRNhiV9bYSy2oXRo2L_NcOFtIFvzHToZTbUwrcEWj2x2jg7lvPe3x0VuJ631hUfzS5wKZY8ay7yhsHGZbmZ_bL_AwLJHapRNQAasjeZatlemOKHdPWKbbJPHF-wSmHtY5k_l-8xuELWsph4p9kLY17FvynjDyUGs_THaMuUknpQfcLPVkesTt2jLEgPAJ-tuBPc8Mjt-zVwBdBEYmgdADJKUW1FpxjYws0v8WUuDCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افکارت را کنترل کن
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/460806" target="_blank">📅 04:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">مسکو: ایران، اولویت دستورکار سیاسی بریکس است
🔹
«سرگئی ریابکوف» معاون وزیر خارجه روسیه در مصاحبه با خبرگزاری «تاس» گفت که تنش‌زایی‌های آمریکا علیه ایران، مبرم‌ترین مسئله در دستورکار سیاسی سازمان «بریکس» در اجلاس دهلی‌نو است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460805" target="_blank">📅 04:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460803">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSIrsVmAuj2u_RIwsUqs7bZt5aNApyGCKsKj-LGPGsUC2NDXaymuFf9gDlzjcwOA_8UhNnEQjsij50wCtQ1rpUNd8BGVgiQ1xl6Nv0hngAqZIw_E2mOdzNnLclXBtk03nE1itJqfkuDSWp2COEyACadzFIqGo9HPDrKSsHsTAukyusfn3F9MMoND0INN_ha9oC8JYEaFqfkSR8p8KDkC-eWebntvFXRPc7J14cTe_n9pzN51Qgisb6myEEuJ8X2k_bKau3pd-ZmRtfMD30aIjHJ6yYQI7huAKvCK_UM1zZzT4e-C4MDxWLhUNbDrgRLwDLDbUBh7gYUzXJoc-JHP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bu_0FhsBO3wZS-zecPovFbddXFXAcEz0U4RoztxGe347HKSCrD00h7HHAZT9YJcMFpP-AYQvCPNKjXk0PIIiLwtofQ5pvN5eT-j9oBrdDrz_Sx1nIeb1gMpcp-yYYMTfr4amJW_HS1W39YmCIIgTOCXnVnMa9J7Dyo-Z6Nj2f8FEosLR7RGGuQlMUR-OOKjdhx1TZEDrPg9fM6KE0UnPQNv0Q55AK_XKYfmdDq2o7VW3DxZje2L00jEgmAMcG6c6Q6hfYZkkjrfSnmWtyJzWvhiSFyysVJbtrTACpg3H7JLdFUegDxkEpvKXEhsoUAdGT_ktpc1sndgablo1rqNXKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ گزارش‌های تاییدنشده از حمله به پالایشگاه «جیزان»
🔹
رسانۀ عربی «صابرین نیوز» نوشت گزارش‌هایی مبنی بر برخاستن دود از پالایشگاه نفت جیزان در جنوب غربی سعودی دریافت کرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460803" target="_blank">📅 03:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460802">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Starp4piAGNpbZFmn379_X70LuiXkzJo8LPfEnaSReKP5ypd4GZgNLXWb89xxD9b2DyeK038xb9zLj1DgLUvHlORfiL_DRmO80Cjj3vIw5zfiSod6r9OED_6fwEOeqsl6ackLbnqmMMN2nAlRpwzDnxEnwizKIedBi3SLstTODq9GvOwH-fb0p3x5qLvFj8aPvbeHdgchMkCyx7Q7F-0oOy73Hi2GT6wCTP9ZB6XhMs8d8qWLwfANdUamroCuwTrYEARum8h2Lvm_IAeUaSMtE3-v_B1YVG5bv-bvmMFpSWKQdTeMVb_XqBIo_OHLupnUDrkGLf1btoyAnXQLC6fQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش دوبارۀ ترامپ برای گفتاردرمانی قیمت نفت
🔹
همزمان با نزدیک‌شدن بهای جهانی نفت به بشکه‌ای ۱۰۰ دلار، رئیس‌جمهور تروریست آمریکا بار دیگر به گفتاردرمانی برای پایین آوردن قیمت آن روی آورد.
🔹
ترامپ مدعی شد وقتی در جنگ با ایران پیروز شویم، قیمت نفت به سرعت کاهش خواهد یافت، همانطور که هر چیز دیگری در حال کاهش است (اما بیشتر!).
🔹
وی با نوشتن آرزوهای خود، ادعا کرد: سه دلار برای هر گالن، اما در نهایت، زیر دو دلار برای هر گالن خواهد شد. همۀ این‌ها به سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔸
عصر دوشنبه بود که خبرگزاری رویترز نوشت قیمت نفت برنت به بیش از ۹۷ دلار برای هر بشکه افزایش یافته است.
🔸
بلومبرگ نیز هشدار داد که در صورت تشدید حملات به کشتی‌ها در تنگۀ هرمز، قیمت نفت ممکن است به ۱۲۰ دلار در هر بشکه برسد و اختلال در عرضۀ جهانی نفت را به‌دنبال داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460802" target="_blank">📅 03:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460801">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
پرواز موشک یمنی در آسمان سعودی
🔹
گفته می‌شود که در حملۀ هوایی ارتش یمن به خمیس مشیط، پایگاه هوایی «ملک خالد» هدف قرار گرفته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460801" target="_blank">📅 03:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb721b9567.mp4?token=tvHsQb8uAuX54Gst79Si2zDvYmI9sSUnz88px5-CdJXZbHhvzTZ0TVp3Dqe524QYEUsbN5_TKiSwEmMgZzDwmIJZ8hUuSwJUrlqhW4_0nISekrLLNHwQVDWfKXSiQChH8ToA1tiWGeZn6g2yAUsd-iFxMlGn86zS0U7jNVaz4GqPn7AnVe4LUg_YKV6xLK99CMD3v6HHt8ox0gQomeVJmO2uGMJFStSkMkWwBj5vYiooIUP1pFFb158jV-c31FRPuU27tdjTKH5_5sa4Di8NzU7zxEb_T86Cb4tycj4Zws0GvuPvTrgKhlips9Bh-yD0Gc3oo3EQP9kWgRXvvExMTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb721b9567.mp4?token=tvHsQb8uAuX54Gst79Si2zDvYmI9sSUnz88px5-CdJXZbHhvzTZ0TVp3Dqe524QYEUsbN5_TKiSwEmMgZzDwmIJZ8hUuSwJUrlqhW4_0nISekrLLNHwQVDWfKXSiQChH8ToA1tiWGeZn6g2yAUsd-iFxMlGn86zS0U7jNVaz4GqPn7AnVe4LUg_YKV6xLK99CMD3v6HHt8ox0gQomeVJmO2uGMJFStSkMkWwBj5vYiooIUP1pFFb158jV-c31FRPuU27tdjTKH5_5sa4Di8NzU7zxEb_T86Cb4tycj4Zws0GvuPvTrgKhlips9Bh-yD0Gc3oo3EQP9kWgRXvvExMTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادامۀ حملات یمن به سعودی
🔹
رسانه‌های عربی: با تداوم حملات موشکی و پهپادی نیروهای مسلح یمن، صدای انفجارها به شهرهای مختلفی در جنوب سعودی گسترش یافته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/460800" target="_blank">📅 02:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460798">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0682df0b.mp4?token=D39qmd_dLq1K5_Rzb-BNtZQOqoSNClVqWXGLb8FT2UeZNk-75lvOFHkB3WoG-8T4QHRFZIYhClIaCUK2S_e4Fmo6_oAVUVeQPGqghwS7xqsX8AJWCMLa7hYQODwBzPD2AjTMZsq7W8_R6zelUjqBMlF2oUtteMS770FUTXCY7IQvOUV2kP_QKVfakOnzGGTYyfQRrYrJBbDbquc9HygR39gpVZkdf4oHDMqNXm0WLbNLLbFMu6Tyw5tyLF-0JLqVNPcJq9o75DMF7WTGzS6QwvCpwtj74qcmzuvarcuJfpMEU6am6OO3V1kGiRw3qAEZ6tBoofJ1Yz1ggZH5b2KdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0682df0b.mp4?token=D39qmd_dLq1K5_Rzb-BNtZQOqoSNClVqWXGLb8FT2UeZNk-75lvOFHkB3WoG-8T4QHRFZIYhClIaCUK2S_e4Fmo6_oAVUVeQPGqghwS7xqsX8AJWCMLa7hYQODwBzPD2AjTMZsq7W8_R6zelUjqBMlF2oUtteMS770FUTXCY7IQvOUV2kP_QKVfakOnzGGTYyfQRrYrJBbDbquc9HygR39gpVZkdf4oHDMqNXm0WLbNLLbFMu6Tyw5tyLF-0JLqVNPcJq9o75DMF7WTGzS6QwvCpwtj74qcmzuvarcuJfpMEU6am6OO3V1kGiRw3qAEZ6tBoofJ1Yz1ggZH5b2KdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش‌ها از وقوع چند انفجار در جنوب غربی سعودی
🔹
منابع محلی از شلیک چندین موشک بالستیک یمنی به شهر «خميس مشيط» در استان «عسیر» خبر دادند.
🔹
صابرین‌نیوز هم نوشت که در پی حملات پهپادی یمن،‌ انفجارهایی در فرودگاه «أبها» در استان عسیر رخ داده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460798" target="_blank">📅 02:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460792">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_nQ_Kafdngh6Sw17perPOV6aRv82OJlasiJ7LR5wL_qEATKVJ8Z8fYg_tjCNmZVjCEu7sHUYXI2zM3RWoxkdcyZo809uunRz_KAQCdwK0PijFQJYwek104lyHIWFt7cLCNtcgflbGfHyRRBB6hz8ik_WmPmjSa8gC8GPEqUI5GbJHZ2KzUda-3yY0DLX2jIl_4LjfSxnEZP7jmMX6d9UBBuDQ2litKd3DNjkJFKXL46Ot3F8LbbgIhAhQS8pFwyoO4zh75fmYKrR83873MfeXpON7A-agtS7cvSaPbE-2OzgLysuibr3OUFpX5tBOSJi6Z1E1x0EArEHNetak7E2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQ8vzfioO7fNfFwe-1h-71kdXvsRzzqg-BXC89DWAAkutjgP8xTrHV9y1ueUomiL1_jefbVlUPK-plsxItyzcT4efJWbt4rAkLbzmT6i_a8sWIWQGZZ8ISrVtfAYJw5mLiqVnKNEOGaYxNu8saLNmKR-uArKE2a4VBnlyzZGUGqEueQK2ZkHbOvv3pi7vh-by1tpvZo8DfCGNBK38otEqVvAHXrNI-PDHXPa4gNf67M6y496IpMOzvswRPbTBfyqL2QQizW5RxNu7hZpJjOrH0jnChQb1xG_7m8embDRyzEgtHRk1IJpIbsqKBWbTBhqQCFs8L9w0bjx1-WkUjdfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhPJqW-MxWSGs74SY_YU305gXBJ3xM9pAvacANaCvmne1sMtoUrjVwFvUpGe6lHw5bmvant5IXVk14iBw97wJrx15V-Qkh93l9kXV39s372MZIcO7hWA08qs-Mu7PjjVkKGzwYosQj_JOMWDKCBteubyszJpjoyWHMtDpdMWGx0QJkER0LC2oSuf0uf00NPFL2DCDaXyvYdSoHHlFqSpkN7g1SV8ugtMy_5UrNp1OVwT6CuK5vvjTByleuPJThV6KCxHV0VHD4BFdvMM130Zy-JLMguFE8mVEJq0jhdfiBICMPNaTkIlSNAhPTaEb461SrSNHoyUYuFp4Y-OHtGFFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpkZd6vvJBfuOin2kbkKE_7fmiT0flKYuh3nOHMFXgt5-98ZtNNE3MZPJSIFyaibexUq9ZDvgIx8tQxCoh0kfI6PAhzXHJNImM3tU3nYVLZfYn6MOsIXA4JNRinw3RKBoHbKr8Pl18lOyH-Faw4EHR_ZSIi9hTvTxzXRirPEQJ2Kd-0qIGxUIZzgxHqAgsd89yLi-OZO3agQU34Hk2cu-X-7j2YtkDWXR8LzsuWVaGCokD80IEMHulPnUwhQJFMoLq8qLhLqYI3Ah7J0zjmHNXTooRCyh87wPd8qG-BwIqngFd6o6OR-KhqZ_aQ8aVkov4P7mLziUJsG8fqnQTnaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nywRlr55aG9v41ZbmF6726Iv5ukkI3YcBmIOzKiA9hY_5yuWkiDnOkPjXY-7jIfV5nW8LPVoEyXjZRlcsFV4l4eATm3OM8UZA9WZUbGz5aConUWt7u_sLOWx_GiyrPPQW3iXHg_XdfogA0imk6_VuwWvq5ROfJvX3epfx1YoDP2T5XSwOQVynLZ0_jsB2yotx3pxNcI2hg3l8qLZossC-KLdowQpP466sbhY2kJ5Q3bNUNc38BvYBUZVzEnitaJhg8WvHx2avjB4gm0wr1vOc9jefWvX8I-vqZZ7CnSuh7hxh7MLIFCW32eXM-4AU-u1s5WMDQOoIJU8EcC9AwbXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYW27jlO-swUfBFUCPORIogYVs4Bp3Le1AMp9-WRIGD8Sk2SVKg01WdYxPiOJ8HVgmBCsUR0uVMgMsvlKQU3hqm8LXPWRswk2sMMloI_lAH0FlZExT3HOwLCVPj-yS_UTVYFHGz0e3Ivk00V7zp0ZWquWGTuMRjBRReERTCJxe_sy612P2Aq5sUFrb0StLeyzfJ-qpuQsom-cfKUcqiVo5Q_ZrPQdBnAOMmc8whT15tNW1BwMTC1Ztovq_8-Ig3fR845jIXrd7YdouSwc-0CHSjS-BFWHeRz96XwdHFebXBSdhxfq-h67XiohIXxFHYPQdbU1pgPuntxxBugvpjA4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۷ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460792" target="_blank">📅 02:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460782">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Evry_tCKFhOUbkD1x6Zl8xnHxKhex2-Pe7A-boC2Q7jI52JGMJVG4EzfWQ5wbWg5sD0V_qlzdxEfTT0tCnw7oUv2dEKmowXbzkCbiNBKihyoAXLPuiDYY999kmO5OrfkbHOsbXelvJ5EjXW9oXcRcshRguVr1s4TpQVxhaHZ2H1GjCDUHuMgvIYeRN-zsf7VsjOgLgwNa6P_5GrypsNnqBCgJ4iecgjBkoqsOt0_Y_DzQTrmfuR0Au3zABaHyI1_2QLuuvxkIKS-JifnV_qWRO3kbhrLFWUVmNlVdOeFvkQ-vkdzvx0dhzXSUtcJ2CSXwMGOpF3PqouPI9mA-VLYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uH_UvHkeL9zBKiib9orLZMq-3gu0L50v4Y0il7grVpZjl9IqH7XR-gVOgydcbEoyc6PRygiUUV_EHKosCe7aaVvSFJkSTy1U-YZAp7sPQGbjYLtDm17mHg8HGS0PnmR9Wz6haiPMiVz3F_OTZV99ixPO_uwF-3cYy529JXfJRdZ0xz2wKg2XLl0g7ICYsxDyNLg8dvj2Lt_8pT9phZnPLM2vPh_g1wSeNA0Yl5GrBmBhya_iEnBraOcY2wgJGbET0QWkzvMZRfKnFTynSxp5g7ht3FBKZWKVAtFoS3gSVTo3MLbqlIXNbdFIjH0eGN8wE1wKdLNgBJiDmsn3e59TXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSaRW8fu6NOnXqpLM-FgsqVdbGHWfGFqQmDqJBwPW0f8C933VG14aB0w0RdwXnzdJ16rya0nF5V7iACizrs2x_9L4D-yNE0BCz3Ec4dqGs0-BHxVgWd7vqGgyLepcy1VRTjsmBQnIzz1Wt7RWZPuOQ4CDGTIbuIlEoynYO6_APDjgmrLmzT2hg4OGp4IzXCquAu-gEJ2ArEjAwa_CQlRoHUFVrSVOxG2fstKgMmv8bw88XuxI2J30eW2s1tfCQimKC-PKaLwKgM3553s4xlVC_5X4JOsJJbmsgy5dLzW-7UAVr0NRB9ww0HRmFmWFaYKukNNwcinRC9GmTSsBqGlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdsbqvl0bHqCGh74MRqJ4bm2W7GRHjdQAhmX8NHjqe8REeFyarTBghZq8hoTpBYRVCZrJEFjdIbNQX-XNS_QavuGkr_nO7uE7n6gBS0vKGcz3BsgeGaDrRRdlTcVt-Tuhb6o_s-a4_iKZGk3Erhpgsz7olXmI67lqNe3CoQ_us-iwRh41ReNU0nTHGT9vEnTav5YztiZ_a3XgiBNP9KIQomUrzXoWI3F7ZQCua0ON62vxpVGkYNtEUUY2Hq0iKlVwXxLiDP64TpXo49nyVc-vWHM1x7NceOp1v05aKlpTk6cREQaJ904bHqJfF2OlEZk7jpQA38tzHIPd_b9ED3bQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SesZeH3sJ_P76yFcDd0TJfOhYZ0DDSR_M3IkHj9Ik-DDTSoV2K9he_wgJXPHKsezGqfriMUQi-FUqlh31Z7s9ut-yXPypNwQYS3jyOl7y75uwmzfSR3ugLzhxHelEx8_Hh7n7NaNGQ0fj9oR-y2YMBWtJfFibzab33_-HhlfXt09KBdWsnws9vV7Ar7TKEC2oPFxU78ZlHP9JvESB72JdNqYxrbw4Q4GlLRhUsOq8Ms0v8FEuI0UBbl6c1jLwcdSIrOffBP9mZndnVouDcE-_Tp0GbazD5BtX3Tes0Egp-U50iajRUsuufxXi56Lj6-FBEeLGB87TSTtxjvVdXsHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWtyBxDYE6i7YLhCDfGEzqTkGmexl_SiRyeb6OVFoVJEtPMiHVKXcwpFEEqFl-nBiZRIFGPAftgRnaf3f5z2AKBCLEjl0BNT6GXBfbbVYVvkDlky9zZ7bPXBs83oxduTNnUUK3yAuQl07fSkcNHQFOXaGG_GuDo5EG3VqU-bCFZx_Ka04BnTnxGuIyaqfGeqh6siDUqAwdmPH9yMiD_bmnUId7Bhbzb4B0egR3Thi63eOatFXB6TTvDgdyOxtSeBuZl-M5VUopAAzaLBZ7t1ZAZOfDUETlFaP7KfN1P1kePwEagt4SLdtMBn9GBd7snglmWU8W0o1uaok4n8i0QhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txjesPwApvU5fKAx5-SeHZiW3TPcp27hLBoHRQkXiDatbIgekdqLDh1kUgUkCHGAOjaPWI1odeYNWGwdWQYUx2eL94VbwHF3nA9OeUv7umioUjY2_oQl6QqXbpEAz6S00TQmqDxGiBaFATqtlBTaMkx7OZETQbuwbTGGG6vZec9D_PafseRZ1UdesLEqgAXrXD84rEn--Lj8soOW2qXFF6ODF1eNwX1lamkbFrlJhzuZ9BWq_yh81HUzFfXK6gOsqI4X4vTYrA5Rf3JpE_C8u8-REstRC2rASkTBhCx2vaYdgHSl8kecxx-S5SOlcHzbjWbXVhlD21CQxA34Y-fy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4IR2oq19w6_MN2aD1nPd7DqXnu4NhdvBeQca4LT-SDlEmmSMgKt0ABhrrlLHNMpk1Y5Zu86UCX_YIUiHSeS0KejCVyRqQq5MQ06Zm23Z9l40GYE-0DQ4dA23ZAA8RT6tDjyfMO9MWYAkRxb78ZJ8YfafbWZ6zy8IEasKVFz0pn77Hk1W6mUtw0Wget60JCd1xIyTnnPh83rY7W-4XI0txBPY63djUL_Bwq46FXSHqTdTjFo9x3DtP5Ef_oZuYYiV3Cmc-yUlHFK2wluotmlssiUY0MHZRUU3hqCsORvpdvG2j8qW7driNo0Yqo6k-VPHPq5OIuLbe-Vr_sKvQxcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUgT5tu7mnxPG1hjOO6lSzw_VKC9M5b7xZ4qmc3Chydjk1RNbamZhg8NZcdmva7Vxxudi0lLzqYRrAaVTPqOOhTEi0YSPzwsE1TGsuJPsNq1sSnedRs1yhY8vTDwZs9CJ8evpTY51S-zw3SUf1zSxGFRDrHP5j4Cu6_ru7auf9FqX9THZzztQPzud3Lel_z1SfEdVZkgxyNDwYFEq0xN91gX5lHqudDwFendtrbiQrtnhraiAJhmPpu2_QslAoGGtI0__cw5XVo_uwalReQQ-r5-4Vj-t1z_Q4srldIdou0JHbRrw5vHAaWTIkeYy4mpES68WXX638RMrqFQxMWJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRbqBkAAvdOFiK1mbFNxSxzQAVDYnWIPKKub9b--h-Y9Dy6lnioTblgRe4U9cbwO9bC5uDp7hTr0ki5t-WT15SS6hzc2hkGHPe-MBGxEasD5UA5ulk38y7qb_7UWem9Q5YA3Y3X99DgyxLiK0dbnj5dseIcMZfc5sUXHngt_Ns24tz-HtCozG0dmmdkEzqydjNuw-SLVSI5k4ZT5bAIswuW8yXwmcBZI5fLu-AfwUbULGQalokRtrgbJ5hdga-8Sje4VuwntYPEWOlrkUKOB3n8xxZknOW7B2AiXEY9T2aBg3GrG0J0ySAnsxxkltSapwu3mBydIa68oQujBVk_j7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/460782" target="_blank">📅 02:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460781">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش‌ها از وقوع چند انفجار در جنوب غربی سعودی
🔹
منابع محلی از شلیک چندین موشک بالستیک یمنی به شهر «خميس مشيط» در استان «عسیر» خبر دادند.
🔹
صابرین‌نیوز هم نوشت که در پی حملات پهپادی یمن،‌ انفجارهایی در فرودگاه «أبها» در استان عسیر رخ داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460781" target="_blank">📅 01:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460780">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef62f58031.mp4?token=vn848j7XmA5mF6TpEABG0aEIg050EkPrMFwtmXl3SrBcBAyWMRQMqxiQ6DfIdgCK63pJT7Xy7kK-Oikw-YZPZdw1tAwMPntIUlbBZ95WEeu4Mmi_ROexcPJx-xHAql6S16eET97QPlShW8ny6nVhVWxiV2AD1UZ3VF3itJY1eEECxS6YPFvu4oDqnXdAlUq48orCcLmdhUIrhcl876j77vdcPbhn_wRw3fk9YwUAbDk3Qz5qryT9HkgyOvHoSbdoZ_bDzsh1voIfog8LvorCC2penVgiM_p6F3OZZbPzQRWoshGP7gx2wKRa0Kf-N3c1G-rIeKOGGRlNfAhItPlZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef62f58031.mp4?token=vn848j7XmA5mF6TpEABG0aEIg050EkPrMFwtmXl3SrBcBAyWMRQMqxiQ6DfIdgCK63pJT7Xy7kK-Oikw-YZPZdw1tAwMPntIUlbBZ95WEeu4Mmi_ROexcPJx-xHAql6S16eET97QPlShW8ny6nVhVWxiV2AD1UZ3VF3itJY1eEECxS6YPFvu4oDqnXdAlUq48orCcLmdhUIrhcl876j77vdcPbhn_wRw3fk9YwUAbDk3Qz5qryT9HkgyOvHoSbdoZ_bDzsh1voIfog8LvorCC2penVgiM_p6F3OZZbPzQRWoshGP7gx2wKRa0Kf-N3c1G-rIeKOGGRlNfAhItPlZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل گل‌گهر منکر شد: هیچ فحاشی‌ای از سمت عالیشاه نبود @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460780" target="_blank">📅 01:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460779">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca35906779.mp4?token=Yfz6BREP8Yo_iRkU84erE9OIKg5VRDQCuAmEdxUCnxNeFkLmJFDSm-J3S5A2y4LLKRmGuwYaZ3O0Y1nf4lPZH0vDw3DMDHc4Me9A6eN_Dc5Guk0sbn8mcMuVaFkPb_9SKcIR6d4iZ_348M9_KXRJsZZsDM3qFIp6iX7OUGRFhM9jgzpPoTThXcIFH_qhhf0dQrpkQr3v-s6B_ViVvEOwsaej-t9Zt--bwLcT9ubfNvBIx8VLmQwdVfOI7rKH0H26Lr-mP357SU9o52JYfTlzysNi_DlIJSCWyS26JL-N_93fDjsQPb84cVk__EpbOMMSaNRVAnxYZFV9qvT7jIHEoB3pdR6kHacIcs_hNSZTVWGL3AlokmyKT2SnmYtIRvxQWd__g0zk44rWgpfS_uqksKqQmUQM2tTlj1k7w7_Um64aq4TjkbJtHhbnxh6YVasQ5vMJiwaWV15kOdsvzQGD6qGPKdcW20eUO-vhoN4iZfNcDiDTXAMcNx89JL9fiw9G3sPb5hGiqPBCGMR5moY--YGXCIkdqylTBqhIp1EPQPVEBIOfEcq11j7NErPWiUKWDjuuIgeLXa5FWOfhRW_z1GzNyjUYB4faR8fdGc1Oo1UfJ_rjK3oNEhQtJXYSk1l6CeqT3RxkGiC1g5PoDq9FBhmDhUPXPq7WgHFfjQqyDQo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca35906779.mp4?token=Yfz6BREP8Yo_iRkU84erE9OIKg5VRDQCuAmEdxUCnxNeFkLmJFDSm-J3S5A2y4LLKRmGuwYaZ3O0Y1nf4lPZH0vDw3DMDHc4Me9A6eN_Dc5Guk0sbn8mcMuVaFkPb_9SKcIR6d4iZ_348M9_KXRJsZZsDM3qFIp6iX7OUGRFhM9jgzpPoTThXcIFH_qhhf0dQrpkQr3v-s6B_ViVvEOwsaej-t9Zt--bwLcT9ubfNvBIx8VLmQwdVfOI7rKH0H26Lr-mP357SU9o52JYfTlzysNi_DlIJSCWyS26JL-N_93fDjsQPb84cVk__EpbOMMSaNRVAnxYZFV9qvT7jIHEoB3pdR6kHacIcs_hNSZTVWGL3AlokmyKT2SnmYtIRvxQWd__g0zk44rWgpfS_uqksKqQmUQM2tTlj1k7w7_Um64aq4TjkbJtHhbnxh6YVasQ5vMJiwaWV15kOdsvzQGD6qGPKdcW20eUO-vhoN4iZfNcDiDTXAMcNx89JL9fiw9G3sPb5hGiqPBCGMR5moY--YGXCIkdqylTBqhIp1EPQPVEBIOfEcq11j7NErPWiUKWDjuuIgeLXa5FWOfhRW_z1GzNyjUYB4faR8fdGc1Oo1UfJ_rjK3oNEhQtJXYSk1l6CeqT3RxkGiC1g5PoDq9FBhmDhUPXPq7WgHFfjQqyDQo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌های مداوم شبکۀ تهاجمی دشمن، چگونه کور شدند؟
🔹
هربار که یک پهپاد پیشرفتۀ دشمن در آسمان ایران از بین می‌رفت، مسئله تنها نابودی یک وسیلۀ چند میلیون دلاری نبود؛ بخشی از زنجیرۀ شناسایی و هدف‌یابی دشمن بود که از کار می‌افتاد!
📝
برشی از برنامۀ تلویزیونی «عملیات…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460779" target="_blank">📅 01:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460778">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP0YZbkZgDM0IcEY-nnDJpUdrtENQj-niBV3rLbAThf8GsskUGn3-N8zTqKLeSOAeL3kPjVFSzSg_tyiUBZlaWmrbbnUPp8raOZ2cG8kgzih09BRBQNXvXbyxKt-zj9j1KX9DsyDiAvwSkodWRn_1GEMgYNBoCvL0OZS5dwG7iPEUbhQILKvp1xbDuJ6IU5LnYGf7o9QaQdHgfrBQBTrvCl7O51XmoOtX1tX_9RIfk3cs4i9WMzPGL046Q4lDygZt0wkBnzCtNE7y2lYnJ5wPu4u7OhOdx0PC_NE78dTGC6PLnd_9EPGeUMfTqxb6G1SdRD-pZzkSVYxzSwhfwsOqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای عالی امنیت ملی: جنگ اقتصادی با ایجاد منطقۀ ممنوعۀ دریایی در سراسر خلیج فارس تا محدودۀ محاصره پاسخ داده خواهد شد
🔹
سرلشکر محسن رضایی: در روزهای اخیر، واشنگتن از موشک‌های جدید ایران هشدار واضحی دریافت کرده است.
🔹
موضع عملیاتی علیه کشتی‌ها و پایگاه‌های نظامی آمریکا، مورد بازنگری اساسی قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460778" target="_blank">📅 01:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460777">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161ec79cf3.mp4?token=ox7YoHrsc2vhtewO-p4GZCCGNchi7lK1xN-gB6V7OH-dKbitbcZ1zipwqmdmFjyZtRTztlvxv14Sdq5mzjYVza8laXvkTGD5oVgI7uoMSO4LyttiRKinEue7rx1JHQkt1aq1wWJ89YsLdMauitFste9xdn22eQXGvw2YUhgEJ-2f28molrSAuAJ-o6n0gbckC3Z27YEUEstBwenqfELVOuCOxYx3mXDlleyAnnDSWERLb7AZNPSICb7VpLDnTs9FhB3-3At5aGFVd5HCOlLjixXq_pt3whO5wRx4aDIlUMrka1PzAIzOY23ucvjCbYyvmmw67dnSVn9eMyaKc8gOcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161ec79cf3.mp4?token=ox7YoHrsc2vhtewO-p4GZCCGNchi7lK1xN-gB6V7OH-dKbitbcZ1zipwqmdmFjyZtRTztlvxv14Sdq5mzjYVza8laXvkTGD5oVgI7uoMSO4LyttiRKinEue7rx1JHQkt1aq1wWJ89YsLdMauitFste9xdn22eQXGvw2YUhgEJ-2f28molrSAuAJ-o6n0gbckC3Z27YEUEstBwenqfELVOuCOxYx3mXDlleyAnnDSWERLb7AZNPSICb7VpLDnTs9FhB3-3At5aGFVd5HCOlLjixXq_pt3whO5wRx4aDIlUMrka1PzAIzOY23ucvjCbYyvmmw67dnSVn9eMyaKc8gOcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل گل‌گهر: چه کسی گفته نباید ویس خداداد پخش می‌شد؟ اصلا چرا [چنین حرف‌هایی] باید گفته می‌شد؟ فرار رو به جلو نکنید.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460777" target="_blank">📅 01:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460776">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارتش رژیم صهیونیستی از آغاز عملیات گسترده در اردوگاه شعفاط و شهرک عناتا واقع در شرق قدس اشغالی خبر داد.
🔸
دقایقی پیش، برخی منابع از حملۀ وحشیانه اشغالگران صهیونیست به این دو منطقه خبر داده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460776" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460775">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
تصاویری از حملۀ هوایی عربستان به یک زندان در استان الجوف یمن
🔹
به گفتۀ منابع یمنی ۳۵ زندانی همچنان زیر آوار هستند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460775" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460774">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b379af196d.mp4?token=umqEE10qSgyc_8e0_9pU1fbz3xHtU0i-h193AvUP1BxfCYwOdDLgxndR7hwRp76qSJUqKrXyp4a4L4kbaQ1wxK9yJF_ul1vmMFYgfjRSYxBcv0IQtjbx7KreL9oQwFdm4azfX76ITPwEZ3rVVuNFVL5OL80w6eZMSOmgVSut54N-_RDKSpN8wtRT23Hd5S-StyIoP2k99uAHd0gjZck_t7Jc8PR5J-_dS2NKexeU-1Z2u5dW_4tC_OvMeNNRqnlTGIHAlclP6aj0z8USCbezm8i6hzxsPZ9VMKvrpZht6-MZjTQYIYMloNr-cOwHi6nDtFYNWgSYGBNnu8ddiqEYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b379af196d.mp4?token=umqEE10qSgyc_8e0_9pU1fbz3xHtU0i-h193AvUP1BxfCYwOdDLgxndR7hwRp76qSJUqKrXyp4a4L4kbaQ1wxK9yJF_ul1vmMFYgfjRSYxBcv0IQtjbx7KreL9oQwFdm4azfX76ITPwEZ3rVVuNFVL5OL80w6eZMSOmgVSut54N-_RDKSpN8wtRT23Hd5S-StyIoP2k99uAHd0gjZck_t7Jc8PR5J-_dS2NKexeU-1Z2u5dW_4tC_OvMeNNRqnlTGIHAlclP6aj0z8USCbezm8i6hzxsPZ9VMKvrpZht6-MZjTQYIYMloNr-cOwHi6nDtFYNWgSYGBNnu8ddiqEYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل تراکتور: کسی حق نداشت ویس خداداد را ضبط و پخش کند. ویس را دادند به شبکه‌های معاند، اول آنها پخش کردند  @Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460774" target="_blank">📅 01:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460773">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvsP3GDN8VPZxkYvebgqHcRMI_b68O4hIuXiCRt6Vnm21oUvVHp0PHefttKobQgvbFqd58OtgUitXqZakrosbwyqO22rPmqq7Z8oHimxLxDXRU89ESAd9yI-8uYEqysWEzaT0Mqi9LaySiGsWyTQR6Lrx7NevH7GgDHN7-ysz5h4diX_P0GPqX1_GYxHVJeMJA8tZoz55IWeMtuJUqDKmzWhPaIT-Kof6dWmKlQsISGtlVPWw7XLbEwTl19qNuRxiZnV3zRPW3NN-DNbU12-PBW_XNvkvhrVFY9NiE6NXfDusU3V4UTdz-EpAr1OJbduaP_0SZRae-FcH1Tp9hexOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تاجرنیا دربارۀ اعلام قهرمان فصل گذشته لیگ برتر: برای احقاق حق استقلال نه کوتاه می‌آییم نه خسته می‌شویم. از مسئولان سازمان لیگ و فدراسیون می‌خواهیم به حق عمل کنند.
🔸
پیش‌‌از‌این، سخنگوی سازمان لیگ از بررسی مجدد درخواست استقلال برای دریافت جام قهرمانی فصل گذشتۀ لیگ برتر در هیئت‌رئیسه فدراسیون خبر داده بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460773" target="_blank">📅 01:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fec0611a6.mp4?token=XXU3UFyJv6EcckHfXL3RjhejOCjgSD1PZqpgfQZbqRDSMkZ1vmWwS1Rugig3Bn0b3IIkiejTDCkIQcBz-RXiURKCvnMvK5_oujQP-rMDw0RI2DgSj_JT53Fd8_Wa4AXahpOkDqiM89rC0AFHtcWU-bWxMa-sWxwD7jPUzOtVw9bPNPB-ClAG8ikHttMKS8PLUnnl66rrFNCxHguvLC9Dkwpqtwbx56_nil9zVThrUDhb7Oc18k7tYsqA-CU-IWfDKMWwkZMiUphX_gEmx_ydf_X8iJvTrVy-t9i5ks2540wGj8s1KAF8ZBkDz9kylL3vzosjmQk4qSRwHDAizIyJegsOtLvXnZaMo4hrSTaMQEynoL_zeWS7fK3JxmfRM6u1-QI6HLgcOEkPBELysjI7sOHeN-bEzKbd-UOr2wGw0EoUlhF1SY_JvbG75BS1hclnLKfqQdmbdjThWb4X8YgLjdHpUOenfYxIGHVPVTUHape0lIHv3Mo8KFLowtLYC-FXZ6yFFymGKuzSvk7qSYCvQjGvAiEQVNM47FgDlbEiYQfDH-UTxz4FDiVK7D2DSOr93RG80v7FtHS_tn54Qt1jr9MCkyk32qFSufArB1jgFtG5oINbgTlJVzbmP8IsZvLSJ8VB8zX_6G3YLipzJThXv9crSR9kMZM0BqE_YNDhIHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fec0611a6.mp4?token=XXU3UFyJv6EcckHfXL3RjhejOCjgSD1PZqpgfQZbqRDSMkZ1vmWwS1Rugig3Bn0b3IIkiejTDCkIQcBz-RXiURKCvnMvK5_oujQP-rMDw0RI2DgSj_JT53Fd8_Wa4AXahpOkDqiM89rC0AFHtcWU-bWxMa-sWxwD7jPUzOtVw9bPNPB-ClAG8ikHttMKS8PLUnnl66rrFNCxHguvLC9Dkwpqtwbx56_nil9zVThrUDhb7Oc18k7tYsqA-CU-IWfDKMWwkZMiUphX_gEmx_ydf_X8iJvTrVy-t9i5ks2540wGj8s1KAF8ZBkDz9kylL3vzosjmQk4qSRwHDAizIyJegsOtLvXnZaMo4hrSTaMQEynoL_zeWS7fK3JxmfRM6u1-QI6HLgcOEkPBELysjI7sOHeN-bEzKbd-UOr2wGw0EoUlhF1SY_JvbG75BS1hclnLKfqQdmbdjThWb4X8YgLjdHpUOenfYxIGHVPVTUHape0lIHv3Mo8KFLowtLYC-FXZ6yFFymGKuzSvk7qSYCvQjGvAiEQVNM47FgDlbEiYQfDH-UTxz4FDiVK7D2DSOr93RG80v7FtHS_tn54Qt1jr9MCkyk32qFSufArB1jgFtG5oINbgTlJVzbmP8IsZvLSJ8VB8zX_6G3YLipzJThXv9crSR9kMZM0BqE_YNDhIHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارزانترین پرندۀ ایرانی، گرانترین هواپیمای آمریکایی را نابود کرد
🔹
انهدام آواکس ای‌۳ تنها یک موفقیت تاکتیکی نبود، بلکه نقطهۀ عطفی در معادلات دفاع هوایی منطقه به شمار می‌رود.
📝
برشی از برنامۀ تلویزیونی «عملیات شکار چشم عقاب»  @Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/460772" target="_blank">📅 01:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiZJR-RSskvzi5K-jDWRCXYtrmqQH_DyGIL7f5keZNyktNqUlsAlwLW8ZRMIyAzLks31irDw4Wkif7Zgvd1TXPstVsy4D8F5BWxUuQw7sT4BQTaDI8k4cc9KGx3AK4QYmEo6Mxckt3jAb2rgJJR81IejPrJIuehUK4LJVyPfcbefbBGyumG6pKRClNkvSRznLKE_hl0S--sYXAPAdqouW61jfRcb0k8fwX8E8n1rc39pXeNWEiRjTWlLje_MFC9deXvc-wNEOQHxV8g_YmXJBgmEN3BZGy8nzQbOFt2py86mjZL53klbnJ2KSQ-Gig-zw8gJFOV9sRTOGqF8DHG2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت مقاومت عراق از عملیات‌های یمن علیه سعودی
🔹
کتائب حزب‌الله در بیانیه‌ای گفت: پس از تجاوز فجیع به مقر نیروهای الحشدالشعبی در عراق، خاندان حاکم بر شبه‌جزیرۀ عربستان به جنایات خود علیه مردم یمن ادامه می‌دهد و به سلسله جنایات صهیونیستی-آمریکایی علیه ملت‌های مخالف سلطۀ آمریکا در منطقه می‌افزاید.
🔹
این اقدامات وحشیانه تنها عزم مردم یمن را برای ادامۀ مسیر مقاومت، عزم آنها برای بازپس‌گیری حقوق خود و ارادۀ تزلزل‌ناپذیر آنها برای شکستن محاصرۀ ناعادلانۀ سعودی‌ها افزایش می‌دهد.
🔹
کتائب حزب‌الله ضمن تاکید بر همبستگی کامل با مردم یمن در دفاع مشروع از سرزمینشان تصریح کرد، پایداری آنها که در خطوط مقدم رویارویی و عزت علیه رژیم سعودی و مزدوران آن مستقر هستند، ستایش می‌کنیم.
🔹
فرزندانی که به جهانیان ثابت کرده‌اند ارادۀ مردم از هواپیماها و موشک‌ها قوی‌تر است و عدالت، هر چقدر هم که مدت‌ها در انتظار باشد، به یاری خدا ناگزیر پیروز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/460771" target="_blank">📅 00:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460770">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🎥
مدیرعامل تراکتور: کسی حق نداشت ویس خداداد را ضبط و پخش کند. ویس را دادند به شبکه‌های معاند، اول آنها پخش کردند
@Sportfars</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/460770" target="_blank">📅 00:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460769">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b452ef8b35.mp4?token=tkaa6CDBl4V1SHOngDCgnemf2wQuErHie2ZXN0S3-NBh2qW9yZmMSy4GI0F1q3WgkUS8KirIaMTd23cQlQYnvOFOWPWLjv1sZ12U5-gwYub5SNBwIoZ9oKQ0vfLbSqxG68Rzxy3XAu4khSCdrnRhIVb63Ke5Dz1oP6hs4IWFVj-a_RqGXm-z2G1gaCphXJvaduA2uOkfRwWI4HUBsiuXsEc_9MKpKUvWjKoPO5kc5h0UyOYYAZAKzZzfdqHIZknKE9f1oZOa9RVpOXqs3YZZB9k9PKbU3K9jb74EQFiy6NfWYRcEqvevTf29u0-RtKF8-k1Z52TAm_Ld92MOEL2fZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b452ef8b35.mp4?token=tkaa6CDBl4V1SHOngDCgnemf2wQuErHie2ZXN0S3-NBh2qW9yZmMSy4GI0F1q3WgkUS8KirIaMTd23cQlQYnvOFOWPWLjv1sZ12U5-gwYub5SNBwIoZ9oKQ0vfLbSqxG68Rzxy3XAu4khSCdrnRhIVb63Ke5Dz1oP6hs4IWFVj-a_RqGXm-z2G1gaCphXJvaduA2uOkfRwWI4HUBsiuXsEc_9MKpKUvWjKoPO5kc5h0UyOYYAZAKzZzfdqHIZknKE9f1oZOa9RVpOXqs3YZZB9k9PKbU3K9jb74EQFiy6NfWYRcEqvevTf29u0-RtKF8-k1Z52TAm_Ld92MOEL2fZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارزانترین پرندۀ ایرانی، گرانترین هواپیمای آمریکایی را نابود کرد
🔹
انهدام آواکس ای‌۳ تنها یک موفقیت تاکتیکی نبود، بلکه نقطهۀ عطفی در معادلات دفاع هوایی منطقه به شمار می‌رود.
📝
برشی از برنامۀ تلویزیونی «عملیات شکار چشم عقاب»
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/460769" target="_blank">📅 00:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fno5x9qwCExRUeHVUIjXEEKkqrVZaWjaTb9xysaPD_rJ-Sk5AlA5rqHVXryY2VoA2jowqWMNIkzeHtKjXnyXtj2ThIGD4wlnKMzGFnYb-FprKC2AUrRbqDx3AL1TQwJiyHAC7Jp1MAnNQyqTK-iaKwdi12SDdidbjU3_TxCwnetLPEIkklJZ7OdUbHC78J6EckHOrgmIslZ6iVqzFu0NK6OAfRrYGYvWDIcbCZQn478XUyMxFxmjKUnOuMfYigbGhlNXxZKQVY1H6rO85V0jXUJ2Rl59vPK2Yndi-2AZ5h4d-b1T80Fp31d_D80z-CctQQXISZUQbdFV8NIBC6uvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۵ خبر خوب از ایران؛ از بازگشت پروازها تا جهش صادرات و درمان
🔹
همه خبرهای خوب قرار نیست در تیترهای بزرگ دیده شوند؛ گاهی یک پرواز که دوباره برقرار می‌شود، روستایی که به آب پایدار می‌رسد یا بیماری که با یک فناوری تازه درمان می‌شود، بخشی از تصویری بزرگ‌تر از…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/460768" target="_blank">📅 00:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA_pwtflcCEYJcbp1hRDQzhwjvgQMW2C2HpcLBkEDaTCpYQX1DQdWrpewWZV3lv1_T15kfkg9CyOl8NYzQMZZKO_KBgRDW-CKr5QFvkDiI-WzNmvGqCtIq6nN3koKtMZGRP3-KKr7j0aAuert8lJ8JBC0TVRPG7yt7BJTOERRBU93nkISZTe34xuW6yX6ILYiYo4BnLi91SoyaI1dagKRjsJi4DPmSDq79knrJlR7_6HxBeCbQAW0KtOje7A1_gVvi6DMiBRfRwelVEJgVJDnbIwoQYDbxbGOU6nTKAxjrdeqRoWzXdmYLdBUUuq8ZdhWO8FGo9ud3MdRFd0VogBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: بیانیۀ وزرای خارجه و دارایی کانادا در حمایت از جنگ اقتصادی آمريکا علیه ایران، همدستی در قانون‌شکنی و تحریف واقعیت‌ها است
🔸
سخنگوی وزارت خارجه کشورمان به بیانیۀ مشترک وزرای امور خارجه و دارایی کانادا در همراهی با اقدامات مداخله‌جویانه و جنگ اقتصادی آمریکا علیه ایران واکنش نشان داد.
🔹
اسماعیل بقائی نوشت: درست در همان روزی که رئیس‌جمهور آمریکا با بی‌حرمتی به حاکمیت و استقلال کانادا، کل این کشور را به‌عنوان بخشی از قلمروی آمریکا نقاشی کرد، وزرای امور خارجه و دارایی کانادا تصمیم می‌گیرند باز هم در مسیر باج‌دهی به همسایه قلدر قدم بردارند؛ این بار از طریق لگدپراکنی به سمت ایران از طریق صدور بیانیه‌ای که سراسر تحریف واقعیت‌ها است.
🔹
اما کانادا باید متوجه باشد که نمی‌تواند هم خود را منادی «صلح و امنیت»، «آزادی کشتیرانی» و «حقوق بین‌الملل» معرفی کند و هم از تجاوز نظامی آمریکا و اقدامات غیرقانونی و مداخله‌جویانه آن در منطقه ما حمایت کند.
🔹
اگر مسئله واقعاً آزادی کشتیرانی است، چرا کانادا، که خود طعم بدعهدی آمریکا را چشیده و می‌داند امضاهای آمریکا با مداد انجام می‌شوند، به جای مطالبه توقف جنگ و رفع عوامل تشدیدکننده بحران، از تجاوز نظامی و تروریسم اقتصادی آمریکا حمایت می‌کند؟
🔹
این، نه دیپلماسی است و نه نشانه حکمرانی مسئولانه، بلکه نشانه سردرگمی راهبردی و تسلیم در برابر قلدری است؛ انتخابی که حتی خود کانادا را هم بیشتر در معرض تعرض‌ها و باج‌خواهی‌های آمریکا قرار خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460767" target="_blank">📅 00:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
اصلاح قیمت بنزین از ساعت ۲۴ امشب
🔹
مدیرعامل پخش فرآورده‌های نفتی: در نرخ‌های اول و دوم بنزین هیچ تغییری نداریم.
🔹
تنها نرخ سوم بنزین که کارت جایگاه است از ۵ هزار به ۱۰ هزار تومان تغییر می‌کند.
🔹
سهمیه‌های اول و دوم ۸۵ درصد نیاز خودروهای شخصی و موتورسیکلت‌ها…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460766" target="_blank">📅 00:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe3d013a2.mp4?token=UWfWo11p3k-3SD73xauPMzfVwUShCY_zXy4RtxmHAxcRU0jyogReQuQ--tmwnyDDn1kdo-mS9HOem_TdP7EoB949yRd2P_KBImgFi-K-CfuG9A0F63QXeOhtZcQ6fvr_uzYK4-Ug8PR_tSXfogP4OOBbfZ2A2lHcG5-RovNcEitptk1mdr80sOD4a3EKSCout-f3-DWhNhF726iym-WwquRd5q-_SEMnUSB1xyOFgwjglFeQ90PCC8L7LI0Eyf4HZMz_HsHhOcibfr8e1IWb8xniLJCQSQoa7OXgiBCkj1pYWV4ujgM9NkuXrISkpc1LGSeKc5oe2AewV0mj-WEkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe3d013a2.mp4?token=UWfWo11p3k-3SD73xauPMzfVwUShCY_zXy4RtxmHAxcRU0jyogReQuQ--tmwnyDDn1kdo-mS9HOem_TdP7EoB949yRd2P_KBImgFi-K-CfuG9A0F63QXeOhtZcQ6fvr_uzYK4-Ug8PR_tSXfogP4OOBbfZ2A2lHcG5-RovNcEitptk1mdr80sOD4a3EKSCout-f3-DWhNhF726iym-WwquRd5q-_SEMnUSB1xyOFgwjglFeQ90PCC8L7LI0Eyf4HZMz_HsHhOcibfr8e1IWb8xniLJCQSQoa7OXgiBCkj1pYWV4ujgM9NkuXrISkpc1LGSeKc5oe2AewV0mj-WEkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان شهدا میزبان اولین شب گرامیداشت شهدای ۱۷ شهریور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460765" target="_blank">📅 00:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyEgEPiDbyOMnNnNqGc0KCP4-i6vgEBYHTFTve79Ax9Ql_qLDdf0lca-0XXibm8fX-TMS1xYxrBWH1bQ55GAWsUPOfGnJWNFZ8Jq3xNdAzSU3OgIUk5Rcbim4MZxejqF81Oq9-E4h1hpldamt9tddSPDW522w-uDjlAVp6YZWmYhhv1vUMYx-lYjQr8_yxALM9TNcb0tYPWla-tFJUsxOcE2VuR1HaeqQwpGwcQEouZyxc8nR7l6xO78292R0M47ZecOUF8a9O5w-eGDADfpr9RdCGpCoX9slwi932jaFu5NTXFtHxL9yyZaymiL4JNRIXatkej-SWkSLSzb2XtmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سازمان ملل نسبت به طرح اسرائیل برای آواربرداری در غزه
🔹
گزارشگر ویژه سازمان ملل هشدار داد که هرگونه عملیات آواربرداری در نوار غزه ممکن است به نابودی شواهدی منجر شود که می‌توانند برای تحقیق درباره جنایت‌های فجیع اسرائیل ارزشمند باشند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460764" target="_blank">📅 23:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f51c78457.mp4?token=f29h4qbxvsLyi7mMhKTsUS2NSLBrqPdOUuaKtQ_si09fpbd3NyGjy1w6f7_6PuTL6VkyZqEV87mqLWLHafyNWyn6XD5MxGXplFzDcY_apqtQO95gwnZVZVMGveCV4astuVQ8MSgXDb5hMpQdZrh3QZI5pSKtAQItt4PRDyEjZQvlUU7ICYksNgWVjcHIa2TXAlSmTXLNvIkZ-TuwXwl2r_wOxR1vqXTkb5644_rrVtXpQWTvl6ZiQimyvBN4kKXR5mdj1ZkyNBT8Dm8AT5hcMZawyfS5irGxYOKDfrDyg7dQgDO7SNLP4B12gymwgm_RTzVzl0pp08YMDElle2riWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f51c78457.mp4?token=f29h4qbxvsLyi7mMhKTsUS2NSLBrqPdOUuaKtQ_si09fpbd3NyGjy1w6f7_6PuTL6VkyZqEV87mqLWLHafyNWyn6XD5MxGXplFzDcY_apqtQO95gwnZVZVMGveCV4astuVQ8MSgXDb5hMpQdZrh3QZI5pSKtAQItt4PRDyEjZQvlUU7ICYksNgWVjcHIa2TXAlSmTXLNvIkZ-TuwXwl2r_wOxR1vqXTkb5644_rrVtXpQWTvl6ZiQimyvBN4kKXR5mdj1ZkyNBT8Dm8AT5hcMZawyfS5irGxYOKDfrDyg7dQgDO7SNLP4B12gymwgm_RTzVzl0pp08YMDElle2riWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار ابن‌الرضا: توان زدن ناوهای محاصره‌کنندهٔ آمریکایی را داریم
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460763" target="_blank">📅 23:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/613b4cd993.mp4?token=oHkNEo7F8EhhoTmrwRso0Mndm2aqc3-OHcWwQR19D1oVPUqvRMm_QcLU0-W1mMBaWj-SOii-Z6-hhynQBgtIgl01lhfECO6PZnqiW7D1rYoVTY7Mu4LMFgMQ3rsVRbtomEYw9yAy5c1L_humGj9iTxIBPJ13ghyqmEoMfULOfa5J_49jRkIZL8FkOADYCZ4o03A7-QfRy7XP-1MDBMa-hjKOentcqWXEdrNivHadt7Lv5ep9YDD_6K7na7ggplBlFGxot9lhZlvAe-5qemugDVDmOnCusFUJz9sqqRXVetlsS8AUO197KHw_yz5q3hfS7bvHVixDuZ--PekX3y9eOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/613b4cd993.mp4?token=oHkNEo7F8EhhoTmrwRso0Mndm2aqc3-OHcWwQR19D1oVPUqvRMm_QcLU0-W1mMBaWj-SOii-Z6-hhynQBgtIgl01lhfECO6PZnqiW7D1rYoVTY7Mu4LMFgMQ3rsVRbtomEYw9yAy5c1L_humGj9iTxIBPJ13ghyqmEoMfULOfa5J_49jRkIZL8FkOADYCZ4o03A7-QfRy7XP-1MDBMa-hjKOentcqWXEdrNivHadt7Lv5ep9YDD_6K7na7ggplBlFGxot9lhZlvAe-5qemugDVDmOnCusFUJz9sqqRXVetlsS8AUO197KHw_yz5q3hfS7bvHVixDuZ--PekX3y9eOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران میهمان امشب حماسهٔ مردم رشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460762" target="_blank">📅 23:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bde5b1eb7.mp4?token=QxPUlv9N7EbkO4y_19_LKThrXdmguWS2jrAcjSstboQ-0Tqsm5Y7qjoanc_7_7G-AOQ9YcvTYEPJbP2V_Xn_GFx2bUvPGfSkY3CqLZuuDDMiC8HEL8t_RuIOt8UI-3YDV0rGLvp0O41SvKzj2swDKksb3pI1KC-eSWXNEyd_WiiLlNcEQL8aQFDFxo28_I9vjp_QfNQavF0KwcAkP734QUi25gbL3pVay0hGPmVart1eR8oalpqcvrJXISaAaAXJ8BWPG4gC90z0ehiV9W6ecLVPJS6e1mP1Qa1jaKZ-tec2RUTJgTA2k_GgkKBp5RsJyKkOOxxugms1yqecQiLRyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bde5b1eb7.mp4?token=QxPUlv9N7EbkO4y_19_LKThrXdmguWS2jrAcjSstboQ-0Tqsm5Y7qjoanc_7_7G-AOQ9YcvTYEPJbP2V_Xn_GFx2bUvPGfSkY3CqLZuuDDMiC8HEL8t_RuIOt8UI-3YDV0rGLvp0O41SvKzj2swDKksb3pI1KC-eSWXNEyd_WiiLlNcEQL8aQFDFxo28_I9vjp_QfNQavF0KwcAkP734QUi25gbL3pVay0hGPmVart1eR8oalpqcvrJXISaAaAXJ8BWPG4gC90z0ehiV9W6ecLVPJS6e1mP1Qa1jaKZ-tec2RUTJgTA2k_GgkKBp5RsJyKkOOxxugms1yqecQiLRyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سارق حرفه‌ای موتورسیکلت در دام پلیس بروجرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460761" target="_blank">📅 23:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گردهمایی مجلس باحضور همۀ نمایندگان
🔹
سخنگوی هیئت‌رئیسۀ مجلس: گردهمایی حضوری نمایندگان مجلس با حضور بیش از ۲۰۰ نفر از نمایندگان برگزار شد.
🔹
در این نشست، حدود ۱۰ نماینده به قید قرعه انتخاب شدند و دیدگاه‌ها و مسائل موردنظر خود را مطرح کردند.
🔹
قالیباف نیز در ادامه درباره مسائل مهم ملی و منطقه‌ای نکاتی را مطرح و تبیین کرد.
🔹
مسائل روز کشور در حوزه‌های ملی، منطقه‌ای، بین‌المللی و معیشتی از محورهای این نشست بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460760" target="_blank">📅 22:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309854c321.mp4?token=h3BiXkni0pL3JzyXLBdqJGlF0soANJkMMc_mIAdG_6S_h19hfa7ZdWsBDk9V7cRFFVTaljITtX_HKhHpb56A1l8BeTYFNRNzgEe7jTc4ORVNLs68Pe59naUOv199aAeWwFeq5fh1QIHBG4P3wGzF35Dr_G6ogxR7CCv3qJxGQBqGPXba9Lz5lKJS98gz44UrVpmxpsIJRbOQN6swmImLiSrW_eFJVOIpRkpMSkqfT0ZKhP-Pc_olWff2u_tUdDZ8P2zul71lDhvV7MBSzCfmvT3-3ZYAiw23_FzAqGaDuV5Ce2H9c0lS6CcJIOVXqMuY42KJjbyWQBVn6XiTBURdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309854c321.mp4?token=h3BiXkni0pL3JzyXLBdqJGlF0soANJkMMc_mIAdG_6S_h19hfa7ZdWsBDk9V7cRFFVTaljITtX_HKhHpb56A1l8BeTYFNRNzgEe7jTc4ORVNLs68Pe59naUOv199aAeWwFeq5fh1QIHBG4P3wGzF35Dr_G6ogxR7CCv3qJxGQBqGPXba9Lz5lKJS98gz44UrVpmxpsIJRbOQN6swmImLiSrW_eFJVOIpRkpMSkqfT0ZKhP-Pc_olWff2u_tUdDZ8P2zul71lDhvV7MBSzCfmvT3-3ZYAiw23_FzAqGaDuV5Ce2H9c0lS6CcJIOVXqMuY42KJjbyWQBVn6XiTBURdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانهٔ مردم بیارجمندِ سمنان به ایستگاه ۱۹۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460759" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460758">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2a24bc0a.mp4?token=CSbO_xuVjD4LPHZ5AvaY90xwv_1h4zdC6_U3sSZTNbml_QmQY7d-NrLlABrqDb-mZzjm7dgGt_Vwyss0yWE16AEMxUoEmNSsNM9l5m0RWlXNtTnwymn_CwDIIvdSMRaTCIsgfPC_keyPAtnk6K_wTWCOKHEBU4zHdVZDcA76EhxP4EshEUWSdAAWWkjDGRZn5u_qO1WAQiXrJIAKkOQoR3rGCaT1LXamLd8YBjZkraIWjq2nOwhr52d07AR_x7Jh-eiSZwx46KfX4ZcYCN2JYWdttG4xhK6duuZLZtI6A8ItUZlaqV_m5bxkRo-LFLdDlWlUNB5RzFLcECbbS5Vdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2a24bc0a.mp4?token=CSbO_xuVjD4LPHZ5AvaY90xwv_1h4zdC6_U3sSZTNbml_QmQY7d-NrLlABrqDb-mZzjm7dgGt_Vwyss0yWE16AEMxUoEmNSsNM9l5m0RWlXNtTnwymn_CwDIIvdSMRaTCIsgfPC_keyPAtnk6K_wTWCOKHEBU4zHdVZDcA76EhxP4EshEUWSdAAWWkjDGRZn5u_qO1WAQiXrJIAKkOQoR3rGCaT1LXamLd8YBjZkraIWjq2nOwhr52d07AR_x7Jh-eiSZwx46KfX4ZcYCN2JYWdttG4xhK6duuZLZtI6A8ItUZlaqV_m5bxkRo-LFLdDlWlUNB5RzFLcECbbS5Vdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترویج دموکراسی به سبک ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460758" target="_blank">📅 22:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc-GTrYqz2Qdt4qJea3bHlhQzKDCI5FGiRuFC5vJ8MxmOyhnHhTAfr5WWq9z3u2IqZwzTtZRs119Dvc8BXxIW5QExQv1Og_bGUb6MtT9h33xDRULz1H5Mbi436ZmNen8l3BXowrFokijS-7GvHJMjE7o2lPYbM4GVDcaoMzi-hsIWAQjHNeuz7t3AZfxXxBqaB8yjgVjpHGfAVaSr5JnzS1-px21USwAz2jmT7rifkXM9r0eDAPQghiRvNjipIn58mxeIMP-tOGn73aEVE2CxjN5YynN7OIL2o-0cRMLc11MWLuBPdV-bILQJ-A5SozULJETWuZZ3WnVDqYBnNKIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460757" target="_blank">📅 22:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWW06DQfv2X8PuAu7FsBq4deTl-1CWD73m9gWVuQr3NPxMOHVuW6IV8VvloBETQSsWtvGZXZbQbENtxYVihnLAFgpEvhRNfOJo3V94CuIdqC12t5PFLNWp_YrVyuIKjALYNe_GJbxIXLl7r1jGmw8BIq6Rwc8o4lfrqqcfvovk1BDQYgiXby_Ivfpw-XjEndBGktyyt-0eZ_z66DRrIaPHGqLkqY1NtIbmvpSzQIrJh-QCjcyCg_-VJnqN4xIQhh83K2BQzoZDHMvLdbKjLcWlW74F2aM5FctiWcJZvVenT2gJenBtIAAHend4mJLzRZnAHheKxlUyjkqub_nlqhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دبیرکل نجبای عراق به آمریکا: بعد از ۳۰ سپتامبر، سربازانتان سالم برنمی‌گردند
🔹
شیخ اکرم الکعبی: اگر یک سرباز آمریکایی بعد از  ۳۰ سپتامبر در عراق باقی بماند، اجازه نخواهیم داد سالم به خانه بازگردد و تنها اجساد آن‌ها از عراق خارج می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460756" target="_blank">📅 22:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460755">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a73c92806.mp4?token=iv_5e2R4uENj_XscKIYqlMP-I8f-EmiXdynBN9LRS_3f55_RHsTcK3yGbfaQOY43bx0iZDRFKmIyJcOUWkBfyF6S2esXWS8iTnbe5rb3e4dogGcqsDSgIrP6Gs6e16c2RAL4UB8KAoscnmfUJXcN5aemYKrQ_o5gWMnKMZA6OZqe0ylqJ8mMPcCUol-XvNphxKtNogHIAu-Sr8V31ixkAwfC7tVseuxB169TTR2EWTSEBeOp_ntzZZ2RuR-oa6zxCkm-pyve6-l790Rsoo78o_TyjfIxMRdjjKt1hPiaiQy7bFYHjW61lnSnMzKVp8uHdbBWFep1-mNh35Y0y2WZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a73c92806.mp4?token=iv_5e2R4uENj_XscKIYqlMP-I8f-EmiXdynBN9LRS_3f55_RHsTcK3yGbfaQOY43bx0iZDRFKmIyJcOUWkBfyF6S2esXWS8iTnbe5rb3e4dogGcqsDSgIrP6Gs6e16c2RAL4UB8KAoscnmfUJXcN5aemYKrQ_o5gWMnKMZA6OZqe0ylqJ8mMPcCUol-XvNphxKtNogHIAu-Sr8V31ixkAwfC7tVseuxB169TTR2EWTSEBeOp_ntzZZ2RuR-oa6zxCkm-pyve6-l790Rsoo78o_TyjfIxMRdjjKt1hPiaiQy7bFYHjW61lnSnMzKVp8uHdbBWFep1-mNh35Y0y2WZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب‌های ایستادگی مراغه به ۱۹۱ رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/460755" target="_blank">📅 22:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5p36dzdVBnvhCQH-GJuiacYzpSpDK8jkRA8gphPG1V1o8MUNu1H4OMJuqOiGGxpkGqmG7UE6eLIuPbfnyhvLB4goWY7zfARPrgBLN3nYTPkNkJDxQPSpOP-_gofixRfmxEVSAmKo2b4Wcxu72aWXHQpRM0iAHM2QIXrjuE4eUrdZxrHK-u6bVVk_I4QHmibxso1fsotJ6OiKGULcIJ7BURacTtiAt2vsL5gBkiCYgi1T1pCk_ELBYr1EMkvQlWw3ktjYf_0_F8UAMmTZ7O-egA_uaU7P6g-0mfN1axRW3vOJnsqq3VdRtb99gqhlLHuHkAat_j-KPtsKIpH7mKufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ابزار قرار است کارهای روزانه‌تان را پیگیری کند
🔹
دیجیتال‌ترندز: متا درحال توسعهٔ نسلی از دستیارهای هوش مصنوعی است که قرار نیست فقط به پرسش‌های کاربران پاسخ دهند.
🔹
بلکه می‌توانند هدفی را دریافت کنند، مراحل لازم برای رسیدن به آن را تشخیص دهند و بخشی از کار را به‌صورت خودکار انجام دهند.
🔹
پروژهٔ «میوز» یکی از مهم‌ترین تلاش‌های متا در همین مسیر است؛ مسیری که می‌تواند نحوهٔ استفاده روزمره از دستیارهای هوشمند را تغییر دهد.
🔹
تصور کنید صبح، به‌جای این‌که فهرستی طولانی از کارهای روزانه را یکی‌یکی بررسی کنید، فقط به دستیار هوش مصنوعی بگویید امروز چه کارهایی باید انجام شوند.
🔹
در مدل موردنظر متا، هوش مصنوعی می‌تواند این درخواست را به چند وظیفه کوچک‌تر تقسیم کند، اطلاعات موردنیاز را جمع‌آوری کند و برای اجرای مراحل مختلف از ابزارهای دیجیتال کمک بگیرد.
🔹
در چنین شرایطی، دستیار از یک چت‌بات پاسخ‌گو به یک «عامل هوش مصنوعی» تبدیل می‌شود که هدف را دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460753" target="_blank">📅 22:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2d3dcac7.mp4?token=A3TlT0sSUr2d3KfHI_zTBIBwpma5tTeaWYIRvCWIXo2Y9mGfSxE5k4uEVbq7O2bb6KGYT19oaj9IY0F2goMrrPquB36FRG0W5gUk-oveucTm1_zJ2BOIPuHCyDb-Dh2KaOTCdcajYdhoXq4pNZGZft7XLzsN78Q1DAVemhoP9LYq3jOhpY6WwtgrZpgSVPLgPYULcfVU4MBb6_OrrtFrjz1GTHFqZBj3JOSjAr5isOSEmotE4wL9CbppjRCyjfxBeYwYo4Q8Gdje6NihcFeldMJjYCTenfwrp1Oh1u74oI8frvJ1ESFZ9kntayIIC13xyedAqHAngY_mnWaptERZkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2d3dcac7.mp4?token=A3TlT0sSUr2d3KfHI_zTBIBwpma5tTeaWYIRvCWIXo2Y9mGfSxE5k4uEVbq7O2bb6KGYT19oaj9IY0F2goMrrPquB36FRG0W5gUk-oveucTm1_zJ2BOIPuHCyDb-Dh2KaOTCdcajYdhoXq4pNZGZft7XLzsN78Q1DAVemhoP9LYq3jOhpY6WwtgrZpgSVPLgPYULcfVU4MBb6_OrrtFrjz1GTHFqZBj3JOSjAr5isOSEmotE4wL9CbppjRCyjfxBeYwYo4Q8Gdje6NihcFeldMJjYCTenfwrp1Oh1u74oI8frvJ1ESFZ9kntayIIC13xyedAqHAngY_mnWaptERZkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ هم نتوانست تولید دارو را متوقف کند
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/460752" target="_blank">📅 22:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnSD3jtg-z8nVXYBnp3nbAjyKdeJggzL2AZRKLEmwZi4ofV39O9nr2lhCfwY6aY-Xv2Q88hAJHFG3CqODoPvTPlfzaoRChLCLWDDyTC4zObvY9FXxwMLcmBnNjO5ut5IwfBlvaI9nBnY33GNXkv_8MrrpUptxq18aGqWLQB1V8thaBfqEBFXsHTLzy3c_DLmdA__LbZwjEnf5dtxM2gKVPhA8q6gmclrfUeZIIneg1H-l6R10bFNKAH_16Iagw6nO0rj5UBSkh4yQDhGlOuqGiR2exfmrkMcgPn9NcxvfqOvoUL85mmyR45dVtoWthoLdVpTrHGqvKmz8ArMZK9w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان ارز‌بری خودروهای داخلی اعلام شد
🔹
تولید هر خودرو در ایران‌خودرو حداقل سه‌هزار دلار و در سایپا دست‌کم ۲۵۰۰ دلار ارزبری دارد.یعنی برای تولید هر خودروی داخلی، حداقل ۵۰۰ میلیون تومان منابع ارزی مصرف می‌شود.
🔹
در سال‌های گذشته وابستگی به واردات قطعات های‌تک پاشنه‌آشیل خودروسازی بوده است.
🔹
بازوی کارشناسی مجلس می‌گوید تا زمانی که زنجیره ارزش قطعه‌سازی تکمیل نشود، شعار تعمیق ساخت داخل روی کاغذ می‌ماند و جهش ارز مستقیماً قیمت کارخانه را بالا می‌کشد.
🔹
حالا بررسی جزئیات آماری نشان می‌دهد تارا اتوماتیک ۴۵۰۰ دلار، شاهین پلاس ۵ هزار دلار و ری‌را ۶ هزار دلار ارز می‌بلعند.
🔹
این ارزبری در محصولی مونتاژی مانند هایما X7 به بیش از ۱۶ هزار دلار می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460751" target="_blank">📅 22:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رفع مشکل اپلیکیشن خبرگزاری فارس
🔹
مشکل دسترسی به اپلیکیشن فارس که در روزهای گذشته به دلیل تحریم‌های جدید آمریکا ایجاد شده بود، با تلاش تیم فنی برطرف شد.
🔸
هم‌اکنون کاربران می‌توانند با به‌روزرسانی آخرین نسخهٔ اپلیکیشن از طریق
سایت رسمی فارس
یا
کافه‌بازار
و
مایکت
، به صورت پایدار از خدمات آن استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460750" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d2bcce6b.mp4?token=KenISqO6fpEfKWn48JqPshew8q_F1wi1DRCQxgGDtEx3_sVkT_pfJWgSzzBTKwqB-1NK4Eq8XFWehogLgQdDZLpZ31yr2hiiOWUbo2ytojGTVN1RLHgpdUhOGprDvrMekjd0rov8RzAKViJg_ksvGFXGyxQnSpkAnIaPMaM0pjbWlAnHKEYPlfgIpqQ1DYfdcJCB4tXz3LZw0xyTDzeGp9MuhEV7Vun1xnrcpWJ5ErbQdavv1ZeaZFN5BYMlA6TA3bCqciZH5hGQ0XKZaUx5fE23s2APCRTx2PNWo-Y66TUffv3P0LV3PKY64UEMNOON4ZjdSXVEx5IqyEzXc9j2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d2bcce6b.mp4?token=KenISqO6fpEfKWn48JqPshew8q_F1wi1DRCQxgGDtEx3_sVkT_pfJWgSzzBTKwqB-1NK4Eq8XFWehogLgQdDZLpZ31yr2hiiOWUbo2ytojGTVN1RLHgpdUhOGprDvrMekjd0rov8RzAKViJg_ksvGFXGyxQnSpkAnIaPMaM0pjbWlAnHKEYPlfgIpqQ1DYfdcJCB4tXz3LZw0xyTDzeGp9MuhEV7Vun1xnrcpWJ5ErbQdavv1ZeaZFN5BYMlA6TA3bCqciZH5hGQ0XKZaUx5fE23s2APCRTx2PNWo-Y66TUffv3P0LV3PKY64UEMNOON4ZjdSXVEx5IqyEzXc9j2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ جانباز؛ از میدان جنگ تا امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460749" target="_blank">📅 21:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a89db0851.mp4?token=ejVJ06BHYuQfGY1zT-9RNb1w57SSBQ4FWfLSmRxR22VvRS4DPYbQEEL1SVXGfS8PGGlvj1R2C6VU1qVQ3EHt6H5uyubkHCIZIE5F_gxLoNnCAnEK0N-oqLplJvZxIhGjPLaL2RDbhuFrh1On5VhP0pPf3XXahZqVw5_SPM9at6jyDHtwmxunqWjVFRajjMs94cGUHLJLZZITdfHbtDGuwMaSqrTFAfpDUlpxsTc2WsH_T02aPSj5_I8F5WHHqDwkiEl0NU5Ox-Jal0_u6c11bK36zTxqpNGthllLm0O0PQ2QKm8EL43PRlwr7lVLemPXDFEa9t31LNHvcM4ZoTN-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a89db0851.mp4?token=ejVJ06BHYuQfGY1zT-9RNb1w57SSBQ4FWfLSmRxR22VvRS4DPYbQEEL1SVXGfS8PGGlvj1R2C6VU1qVQ3EHt6H5uyubkHCIZIE5F_gxLoNnCAnEK0N-oqLplJvZxIhGjPLaL2RDbhuFrh1On5VhP0pPf3XXahZqVw5_SPM9at6jyDHtwmxunqWjVFRajjMs94cGUHLJLZZITdfHbtDGuwMaSqrTFAfpDUlpxsTc2WsH_T02aPSj5_I8F5WHHqDwkiEl0NU5Ox-Jal0_u6c11bK36zTxqpNGthllLm0O0PQ2QKm8EL43PRlwr7lVLemPXDFEa9t31LNHvcM4ZoTN-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار متناقض ترامپ از نفت عبوری از تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460748" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb2f7c881.mp4?token=Ez_2MIg4W5mVeeUPrTizT-jwbrEJczAD0lgQ4P-xobnNSOWohN-ToAdEwsFUnY9AeUQgyFEmwIaZBoCO44dbgBX2N3MC0DkyYUaOf-zUt_LKPY4YaXdaI9zh86cmNnR4F_rX_F0_yUwXZ8VVn1zE7bv4WsqQWW70b-J1leSbwplzSI0T9HrcTktAZR1FflDP5egs869EI9CVwTkhNfkV3y6KY_f9jgCohbSEfm3y5Be2AUaAVXJl9wKxwCLk4dc89_Hh5JM43-R1sPZuwT-no2RiQ6TBSrh_bkeiK24civ3Z_wCOP7Q8aZK1pcQaMHNbj-M7BUtp7S6uTzc1CP2jxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb2f7c881.mp4?token=Ez_2MIg4W5mVeeUPrTizT-jwbrEJczAD0lgQ4P-xobnNSOWohN-ToAdEwsFUnY9AeUQgyFEmwIaZBoCO44dbgBX2N3MC0DkyYUaOf-zUt_LKPY4YaXdaI9zh86cmNnR4F_rX_F0_yUwXZ8VVn1zE7bv4WsqQWW70b-J1leSbwplzSI0T9HrcTktAZR1FflDP5egs869EI9CVwTkhNfkV3y6KY_f9jgCohbSEfm3y5Be2AUaAVXJl9wKxwCLk4dc89_Hh5JM43-R1sPZuwT-no2RiQ6TBSrh_bkeiK24civ3Z_wCOP7Q8aZK1pcQaMHNbj-M7BUtp7S6uTzc1CP2jxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف دولت از افزایش نرخ سوم بنزین چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460747" target="_blank">📅 21:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ff4bcd6c.mp4?token=T0LmTMGzA1DtFy_8SwOobIlGkpJ54uJIHXTOZmklNZk_cMMVmYq2bPfAUNbcRzGSaShM5M5cTsIGG1i48TxGUgPJMAhO2JqHB2zCYD4OLNMLWnEjnCvkx5cELljZyb1uwqdN9ow91r1tbtujl04vDiQ3_RVKHnaQvurClquwhFaq14k6WIxYHqtA44wM6V4yRRyXD9JzzJEKhgtkfW_rr6BX4ckbZTREMNeCJsC4Ue5y10sZ7qKz9fflvIW7TOxxXeU66lasyELVnbHKT0g6WVbHv-7pBXXwA8UlSKx7PX-2wXCjtv8it6b_W7kjWvO0Ne7qs1TEf9nV7HDfAZVfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ff4bcd6c.mp4?token=T0LmTMGzA1DtFy_8SwOobIlGkpJ54uJIHXTOZmklNZk_cMMVmYq2bPfAUNbcRzGSaShM5M5cTsIGG1i48TxGUgPJMAhO2JqHB2zCYD4OLNMLWnEjnCvkx5cELljZyb1uwqdN9ow91r1tbtujl04vDiQ3_RVKHnaQvurClquwhFaq14k6WIxYHqtA44wM6V4yRRyXD9JzzJEKhgtkfW_rr6BX4ckbZTREMNeCJsC4Ue5y10sZ7qKz9fflvIW7TOxxXeU66lasyELVnbHKT0g6WVbHv-7pBXXwA8UlSKx7PX-2wXCjtv8it6b_W7kjWvO0Ne7qs1TEf9nV7HDfAZVfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام مسکن تهران یک میلیارد تومان شد
🔹
با اعلام مدیرعامل بانک مسکن، مبلغ وام مسکن به‌ازای هر نفر افزایش پیدا کرد.
🔹
تهران:  یک میلیارد تومان به‌ازای هر نفر
🔹
شهرهای بالای ۲۰۰ هزار نفر: ۸۰۰ میلیون تومان
🔹
سایر شهرها: ۶۰۰ میلیون تومان
🔸
یعنی زوجین در تهران مجموعا ۲ میلیارد تومان برای خرید مسکن دریافت می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/460745" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248b05fa76.mp4?token=smIN83xv-ps3pE_BXLzmWTDkEbdw4P0sNwmog1CNbStNfowGMxynyIWTxOaUrKhw1v5dWcxKodvzWenG4ku0L3D_hR1bDoWvL2Sz5JK13YN_TkfQ8YhcD2puvh-MCA2hcM6NVTDTr_HL-DUxqqJMnvgf-34MLOZmE6iRuSAmB9_t42Cn1xV53fn-mXM93F4_qk-K33RuDY46Qytn1rAf7W954tCpoT3fzHNlh0DbU33eF5vOMUmYFdST4ReNB950ZfAyqY0iIYZy88AIw8SwMGxn1PRL9IrRIECEeNGE5Ts6vp68-U82Xf-MoR-kyCc6l1w4Qkg-jA88Z9t5W4Po6WxCVK96uw_H2JmTk5qSjk8126QuIhxNTINXgK1lDZvj8EJ6rPzl9hoXb8X3tvSoQggT0PGd7XCnXYXlmtwoBVntU_yHMAYdWiOupgzFBXClseXJ-mgvCdZ6furUhGYxUtteqvj8-CaBlNk8nbmjUHTM2tI1I0thVAY68IdYipDW2C6HLQINxWOFX2vkYYABRy6MMW3yOrjHgSiCkYtU4233fEK03yEb_4JkniLDyiTUESjOQvC_GwNzm4grIvePtVhtxmB7genJD-CxR2Ws-4Ix1A1zT37XzNH9FVwArH3MKYh92DU6LA2X9fiMpzUMCP9GcPiPO9jMkbhCR6TZ87U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248b05fa76.mp4?token=smIN83xv-ps3pE_BXLzmWTDkEbdw4P0sNwmog1CNbStNfowGMxynyIWTxOaUrKhw1v5dWcxKodvzWenG4ku0L3D_hR1bDoWvL2Sz5JK13YN_TkfQ8YhcD2puvh-MCA2hcM6NVTDTr_HL-DUxqqJMnvgf-34MLOZmE6iRuSAmB9_t42Cn1xV53fn-mXM93F4_qk-K33RuDY46Qytn1rAf7W954tCpoT3fzHNlh0DbU33eF5vOMUmYFdST4ReNB950ZfAyqY0iIYZy88AIw8SwMGxn1PRL9IrRIECEeNGE5Ts6vp68-U82Xf-MoR-kyCc6l1w4Qkg-jA88Z9t5W4Po6WxCVK96uw_H2JmTk5qSjk8126QuIhxNTINXgK1lDZvj8EJ6rPzl9hoXb8X3tvSoQggT0PGd7XCnXYXlmtwoBVntU_yHMAYdWiOupgzFBXClseXJ-mgvCdZ6furUhGYxUtteqvj8-CaBlNk8nbmjUHTM2tI1I0thVAY68IdYipDW2C6HLQINxWOFX2vkYYABRy6MMW3yOrjHgSiCkYtU4233fEK03yEb_4JkniLDyiTUESjOQvC_GwNzm4grIvePtVhtxmB7genJD-CxR2Ws-4Ix1A1zT37XzNH9FVwArH3MKYh92DU6LA2X9fiMpzUMCP9GcPiPO9jMkbhCR6TZ87U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا ۱۹۰ خسته می‌شویم از شمردن؛ اما از حضور هرگز
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460744" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrwKtOiFY_QSQZOT_3tQyaDaLBn35jmZGHTuetf545UPptIPpzujH5L2aPG6xxmgBR1vaJysBUE8y0IQPa7MTg9wjXhORc4B-vou8CvQWoAtB0c-ZySpOmKOy0_IeDM1Rte8WMgt2ZjX23xwfPUlgUE5S7dV8jqR5bwS8cEzJi2Z5KSEI65LzLswYUM1qcXAPIGNGeWk5fIM-iYJQJRpOn_BLSaWE0zuRlBhg2ZN3WvU0Vq8CpjFcdSShBYHcDOMgtnMzYIFH0-T_VOa6FiRFgvNGBIR2nLUZDkPhlrljxLZfEixEggqFIT0jbkz2rXZeH7sZQhlgwBC0MFKzQJD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور پیشین لبنان: مقاومت تنها راه مقابله با اسرائیل است
🔹
امیل لحود در پیام تسلیتی خطاب به خانواده‌های شهدای جنوب لبنان نوشت: تاسف‌بار است که تقریباً هر هفته ناچاریم همین سخنان را تکرار کنیم، در حالی که غرب نظاره‌گر است؛ به‌ ویژه آمریکا که قرار است ضامن آتش‌بس باشد، اما این توافق‌ها همچنان روی کاغذ باقی مانده‌اند.
🔹
از زمانی که پای میز مذاکره با این دشمن نشستیم، آنها همچنان به تجاوزات خود ادامه داده‌اند؛ تجاوزاتی که علاوه بر حملات علیه غیرنظامیان، شامل سوزاندن زمین‌ها و تخریب و با خاک یکسان کردن روستاها بوده است.
🔹
این دشمن به توسعه‌طلبی خود پایان نداده و نخواهد داد، زیرا جز منطق قدرت را باور ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460743" target="_blank">📅 21:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4addf5a73b.mp4?token=BAkgSDyC1_pD8q65aLpwJKqXUagDuWbiVZRwlmVKiLPDTAhk4zkNPkfK6GWUN5oZzTMKJPC_e8IpjQjDcl-GwrBkp3o4XnEM5dHVblCTRq8cEZIaoeDT_yjmgwrETywjalhPTGd2_WoGPMyyR9kTjgnBU5fX946-wO50lOofdIiUKzav4WZTHWsYvP137VCJnZMF8fVxIfbY1Jz2sI9gH-sfu3fC7737smVQ69_hVLC1ZrSxh7iTEYqR-HQWXQu3owSEkTmzYgPdruDoV0smnhPU36cN9z-ly0rNDowmZQ-_QnWKF4c-ErAuJAa-4dA9hQ7YylDkiJq3_xWMlHqcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4addf5a73b.mp4?token=BAkgSDyC1_pD8q65aLpwJKqXUagDuWbiVZRwlmVKiLPDTAhk4zkNPkfK6GWUN5oZzTMKJPC_e8IpjQjDcl-GwrBkp3o4XnEM5dHVblCTRq8cEZIaoeDT_yjmgwrETywjalhPTGd2_WoGPMyyR9kTjgnBU5fX946-wO50lOofdIiUKzav4WZTHWsYvP137VCJnZMF8fVxIfbY1Jz2sI9gH-sfu3fC7737smVQ69_hVLC1ZrSxh7iTEYqR-HQWXQu3owSEkTmzYgPdruDoV0smnhPU36cN9z-ly0rNDowmZQ-_QnWKF4c-ErAuJAa-4dA9hQ7YylDkiJq3_xWMlHqcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرسپولیس ذوب‌آهن را از پیش‌رو برداشت
⚽️
پرسپولیس ۲ - ۰ ذوب‌آهن @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460742" target="_blank">📅 21:06 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
