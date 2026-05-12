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
<img src="https://cdn4.telesco.pe/file/eWbh0tQNhOmKOotNE6VmJ-0-XglviR1C-GHuiiUNbAxq0uDJhzCb6U0qmBH9_NpI6BhNKRXJTpmsOqFZ3KxF0R9ShybFsL9az7YC5T2OCNsd6JRLdhjJcTgaWO4LSr11RiaOUCwjaXdrdTga2l2k3Kfxe7gmiNmX3caSoiZQ3s0OxjJmefTPkoKqgvKS8ESF10Z43qVrlByxGFRFwDMFjRaxWtrcWm_xto0qEbqSt2xntdCUi6cZmUPmqIPoEtNyC06cLWcL3wZ_w-uiH6GSFlhxwC8j_aNqwBjPiPULFbMmd2tOedRNOFQ7YAKcKegZwiB7g9o6Oq6kZK12IBGLHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 60.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 21:28:40</div>
<hr>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-YI17qibGupoAmWmJgbCv2lvDR2yxsKNeITXmoyV6ldokWF08k_3bk_KBSVZ0ksRA831RUYl_6WMnlTKTnTddEi3k-Afc5JebiyGUP5gbxeU993FbQT7DEiqyBH-8cyJ2IbOl7uwC_DjS-EnqblXE_goCgDEz-4zdgcphdn9H9X2QyPOxkYW7nZEG12-g0T9sPZMKEpG9856-UxlBF7WX75LjSprVUXtdl_zu9s5QO-K87cb2Gqu00Q1jkulQ9U08Qyr1sIeKBIfs-il24XyQUC2XTu5dYvpoL5P7Jt_bLBukqe9Lfm7gvUBjDW21aJeu1i-GlA6ZPsgnk6VT1wZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSnGiVVT_TSvVKpIGYFwzSDK5vZgv0G2X-vD8_vKOD3RgG8Ux3N8XrMslwat0seYBfWy2IGROVfmVjTeeysctenjZneLnoC8ybGJ_CcoKB6T9g54Ad9Zek__x9IyqZ6drlsAQ_HOODlhglFiUjLYyYKSsDs4FgS4tr7bXfjAjR3FSB-8ayvXe8H_YbtXrltsRd6dHvqIHZ2t-xmxYYCkB5QeBqeP0ISGhwhRYaPWt-vqXjDnPhRProbXt55zCBdqSJnNs9BFx6nCZkZXgjx9Ur_wrjgZHMzyPzD_hfZez7TwtEWThYu6bqOvqt_gBy1or5mjZb7mZORhU-g9Lk1HiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfId6hOwL6O1Oj1QYlVXwGQSiDirdWr9w77D_tcM8GqPoE97IQ9GhYITms4cyf5Hn9aevyc_0ZusR9A9Wk4W9oT4viPgNhMi1fUI5rU5czYwrLH3fRkiMMPghgry5maMg5uL01IopSAW817tAi43_upqEC14wzagkQk6OLm66Vg2C1xZfU_L01lBfD-qLBqObgBOZkytbAzhYjUd4Z0Ro4BDfltrptXi8DODRsCt86bWvvw6O5F3dOu8JmMq5qEqnlsczMt09nVS8opCNu9iXwRQ8nRicInlLTTlqRdDuVnwDH_UXf5EJqPuoUCSgu8obUlLpjElORWJQUN-Ucx5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm_lhC3KUc9f6Z1C_bIGzej-gxF9as82zNgBv-Fqj45ywrg_rzRWrVYekLcX5pYNgBjC3QzqVjTveEHEfkojLLmsQGGKJxg-uOuKFp0qKVeIFNBLKbj52lTytb22gbZMrhkhrKP2729eqtsGusJlVaixOHxhhHHujPlCmvc5t04Rbm8hQhWewLtqiTfrhP6TgIc9RO23S8ug9vpAh80wIOy1h95QcWFw1GfKrAzj7BixYilerY-LdnES5yewLW25Q1Ahy135y3ykzzwZEATS3Ga5nVWMQGyWRrWj24JaINWtFGQDKHYmqU9MCfsUgxmSAkScU8sahkeAqP0c1OsuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=B2yBDq_vBTbo1VEX0zDQsXAJhQJYE7W8xUfM8TzhXcN6rSedGugOhUAHBTum5K6LjB98id-T_1Yl_f1QMXZYdwY7vt84SrYLUThxuX9ohUqEXGhMPyI1_mD3IJ6uKCy4rv2aW1leZLenhOu95gLz3lcWGlLFvQWEWUncKn5O65sDEqc3z2nU6KIssv42vEvGi6jjiuegzlzj-yDq1UL9EjbgF_uIOxBDzsDm0UHF-gvDGZ2zGtPD63dKjaqOyJW9itOEGI1-mItpQvSZCpn0yZUN6Ia0eMOTatXzLyjYjuPsjT9X5QGjEtc7VuOf8rigoljFLwsxVVg1bd9ujl_XZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=B2yBDq_vBTbo1VEX0zDQsXAJhQJYE7W8xUfM8TzhXcN6rSedGugOhUAHBTum5K6LjB98id-T_1Yl_f1QMXZYdwY7vt84SrYLUThxuX9ohUqEXGhMPyI1_mD3IJ6uKCy4rv2aW1leZLenhOu95gLz3lcWGlLFvQWEWUncKn5O65sDEqc3z2nU6KIssv42vEvGi6jjiuegzlzj-yDq1UL9EjbgF_uIOxBDzsDm0UHF-gvDGZ2zGtPD63dKjaqOyJW9itOEGI1-mItpQvSZCpn0yZUN6Ia0eMOTatXzLyjYjuPsjT9X5QGjEtc7VuOf8rigoljFLwsxVVg1bd9ujl_XZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj4Gwb6nVMM0pAWc5h0CyM5pdgLUduCx690xp9x-seOD8_5FroI_OF-CXkbUOtcH8ND6ZvC1N1VqRdPZs-CSUmd4LFkZaMv2sfis7Gkh863-k2WTOqwnQ1kIbGWJ-lrVBzWDqPVxfbw9lYPObF1TAQimIVKK-kl-OkdP1fGi0_jcIhSV906qVnyiP-gnOG7k_WmyzXFA4eHuo6nRoe7TVOq4M3zs6BxTx5O2Gnb_u00j3H-eIQ5MKRZ8iy8WUenBhl9GsdSjfyFJ2MUl5toSN_RW-MhnIbhZ5TJJXCuuzonhcG23Bs0C5uThDs6-5GVa6ZDnLzpg6TRN2EDO9uCYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwEgQmHuEJ6lFE3RRyBu1dZL95-pe36yfFv7ztIadQDzBgM-GfHrutfWAfgjZK5LDhv4HgnUJ06fQdgBzPaV2EOIUQ8oRaRBB-rggorlTVfxRyt7P_NsWayPYh5g6WpQihRS-5ufwrqfxDi7zuguGd314_Fd0pKv0cU07-fxN3utKR6sjePpMxXTfSKnQhUhyLKg4bRR-M7JadPHUysoCcjiSNqbYwX6hTx2DqAltS1QjHICq00E0YbGRdpbMVYfV2jtl0_XCt-6z-UWJtQRhkPAUATaRRPsUexz8w72x_Sh-adYja86n5f-ZGkMJ7_HapT4JR782udiIi0IeJPqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpUP6V90yomMQhME74ueuebPIR0unZpQiM0rg75s1hQnHaW7AMogaAyv-vQVG8AXF03Vieh8nQTVR0a2jePlU5CiLcda9f2Kwy7dlJwNRt5gOBujt6j9vNSC3ZzKOF4IEE3FlqCLQ852BGQjLaCxc967dZl7XKEm-G_oycMMP4Vjb-r6rVVTlOOcT7CP8rvFYEebqsuc-ap2nsgAccx8V4FUb5i4BygvH4eBJcU2cPEB6IzwLo2fWTZyHy0hdisVsjJPTDzyr6HDr3Tf75UdtLFY4HnJmUiTi0TrjD0E0QLzl3cmQnDMWHR0cdhGm7_dyerFl664ekjgHiwB7z-6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ5Kdq1zan39xFl5hleFM1rPS0oU3dVhCMAXbPrGfKe8g1Y0cqY03nhUnLgQFHmrbAU0uI6uL0bwTvh12CpSzRnkesppJoPR07OHCsICW2SQBedJMQse6ks8AgIbD4qD8thumslUNgpOGwvVNzIaLG5yF5WCyTLSoNsrOaX4s8Sx5LQnHc9lTJq2txP7H0yl22JBtfclkwXlM-MgT8WQUm1okiiMl7n-Cr_tP7aEQZe791pbHjdn9xF8hZ4E0G1tl8eIFLGBrWJlc8n1Oma64rAUZ9v2AO0Dv1Ua8rQGOqBZDhoWv7S0gmjbDF71ldd18PpMo4i6S0b-raix33FpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUo9O3vC0f_NuV9jzc6l9MKYlL_SEmDjJNc7tzFKO3lAxBfNFwQ9SmbKKv-2n4gu3cKy02vzcIz2n-_hD4h3Paz-zhCb7ffiOhguESjehe9UAjOFhmx_SUlxfeRYM1hQ0IrBJxnM-SXVmXBJdOiHH0oWwTb9mO81ANBu7Y4fI5nAYFMd4sV2m_rPx4a1_EYB4ZXX6jJJKEcOhOyudgqbBF_6lHfU5CbDnUuA0qKfyU4inIjM3MpcK3fAhTFbU-1dclbeWCmIHmuqP1j-RUZtuEy9v_78yb265SzijP27vJO4zy_W0i4ngqZWR4lH0QjHm6FO36e-gJNT68B8ZZok_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsNr56xyzZsDaPUOCVMN403ECk4hTzePq8ifBiVO470A2fgRIdBV2wTse53aEd8WtZMWoOS72lEY_LzQy0fSMmdrbVWIG61v4QExaw-Ap9-o8uU8lEDlwLoluR6Umae-AFBUvwPLlbAMKUYZZwSbU0lydBP4ewXYoa4q352AFO3affhytUXum0VWkTVoD9ez-v8pGj9FB9xTJvwszni_SUZSZZ8UJEWct_6b3SduorABOtuf19qGj2n7YlNo0PtsxsP8lL5drrs858KNjeiXsGlCaZ8MF-THAWALg625o9FkHNAwDjybYJswmfFjIWQEs5Xxg9VvxbPR2JxKGdpHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwxzeUw6k80sjBVUOkc8krzz_WA6sGTucXjPmlokOz-aFm_cZKj9qsDW0zdfwvySigYT_WZs1CLB0nNBvHAepUGwkKJsrbQd1LguL9bJwfKHlL7DcJkCI1PpWpTZUhSV13w_TIiD8laUB1C3x0fdlgqF7YOSyF_woc81u1_CCgGetNagnXuGWUFyfWNViDNzYZy24JQcMcgrIyGdLpxnZuwlBVT60Z1ggpHoNeNBIQ37D-BsnCzoPtK-GyBPJOATC-DfI9SXQSDAlsRaWzkJydab_IigC39kv8-HQJPBHNAfbMolenWstGjhd5N0HCZQXO6pvhHPh9k7A8_LZFW8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pg_xnKTWcgdKXADLW_yMclp56QnNcj6kK9X1DIRznUvcm6WeBDxBk58BGQAIFbsf1d7DWt2nM3jJ09TcrMQMLPpZzkprUIifZP6Wr9iLSiALHx1RtxI8jjq0QkexO3Pp8mUnlw72mRiLHGmFUWTvzRHo02D2PqTQFMU2GC9tp7Re00xqIF0jybWyCDs5oVIy_c2FWSW03JV0VlGz4HpzMsuoorlS4gOSTmvUnUtcwYGF8OHEtLDRBiNFvCBduEn55Shwd-kAkMsOw5OODVrlMdgOVS7Tvp2qhjqP26SOeCSasKoXaut2-p5drEKShC_UqzGUPW_I2ZuxDwsujyg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در تروث سوشال:
«
ایران ۴۷ سال است که با ایالات متحده و بقیه جهان بازی می‌کند؛ فقط وقت‌کشی، وقت‌کشی، وقت‌کشی!
و در نهایت وقتی به “گنج” رسید که باراک حسین اوباما رئیس‌جمهور شد.
او نه تنها با آنها خوب بود، بلکه فوق‌العاده با آنها رفتار کرد؛ عملاً به سمت ایران رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار پول، و همچنین ۱.۷ میلیارد دلار پول نقد سبز، با هواپیما به تهران فرستاده شد و مثل هدیه‌ای آماده تقدیم آنها شد. تمام بانک‌های واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند!
آن‌قدر پول زیاد بود که وقتی رسید، اراذل و اوباش ایرانی اصلاً نمی‌دانستند با آن چه کار کنند. آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید.
این پول‌ها داخل چمدان‌ها و کیف‌ها از هواپیما خارج شد و ایرانی‌ها باورشان نمی‌شد چنین شانسی آورده‌اند. آنها بالاخره بزرگ‌ترین ساده‌لوح ممکن را پیدا کردند؛ در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی.
او برای رهبری کشور ما یک فاجعه بود، البته نه به بدی جو خواب‌آلود بایدن!
ایرانی‌ها ۴۷ سال است که ما را معطل نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً هم ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند، و به کشوری که حالا دوباره عظمتش را به دست آورده می‌خندیدند.
اما دیگر نخواهند خندید!
»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh1q1d5fbfRp0eGC8m-4iCBJy9JRkrGuRTXxKPcMmelQmLb_044EsXGkGhB_BxzA1O9YO7O7xLi7aEFbceBc-ZZRzjk2kycFgD7q_M3PxUromeMfz18U90PlKGxk0wLUhAV9rSswEhb7R1_Jq1NtQfbmChmRJzDaBH606mD_6LYqwrNqb0mtmCg_Ao5RWbeA8qVRDy-B0haXdjdkx5XPBo9yrIXwjEKTNBJl-1Nc1fY8RNS5M-q1v2BOaGhjEL7x04n8zsh4IFTj18bGWBk8exjcm0jyl3K0ybKGhem2iAzc8MJjv32vx-H_o4Gllqz4RyOWmzboxCrhyLxGhk357g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه چرا کمونیست‌های ایتالیایی نخست وزیر ایتالیا  - الدو مورو - رو در می ۱۹۷۹ کشتن!
چون گفته بود : «باید قدرت رو با چپ‌ها تقسیم کرد!  اونها هم ایتالیایی هستند! نباید مانع شد که وارد دولت بشن!  دولت ائتلافی ایجاد کنیم اونها هم باشن!»  کشتنش!
کمونیست‌های افراطی کشتنش و
گفتن : برنامه داشت تا ما کمونیست‌ها
رو از مسیر اصلی که مبارزه بی‌امان
با لیبرالیسم و سرمایه‌‌‌‌‌‌داری است منحرف کنه و ما رو به فساد بکشونه! در حالی که وظیفه  ما «انقلاب کمونیستی» است !
و نه سازش و شراکت با سرمایه‌دارها!
و‌ همین چپ‌های افراطی (در ایتالیا، آلمان و فرانسه)  که به خاطر مبارزه با سرمایه‌ داری به کشور خودشون رحم نمیکردن و دست به بمب گذاری و قتل و.. میزدن، بزرگ‌ترین حامیان فلسطین شدند (چون اسرائیل طرف آمریکا بود)
چپ‌های افراطی آلمان حتی می‌رفتند اردوگاه‌های فلسطینی
کار با اسلحه و مبارزه رو یاد بگیرن!
کاری که چپ‌های ایرانی هم انجام می‌دادند!
خلاصه ریشه این داستان‌ها و… خیلی طولانیه!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=t6GddzlbC37KcJjQtwgTYEEsgSJbBcMNkWrsOifVtc_3ltb-BhSaTeQFcl24oZsF84TQIn6pO61OW_oaHQVuZ7UIHOcRGZusG256QP87r7bh7wnSzrhs8xiBH5pYx7DBXa6-BD7nI08eiyVbxVSRdky-yw16itoSyWNB64fprhMRC6Ku4l7MvV2TVRyNmK0qv5hbeQAtKEaUKo9fXxsALTchsiUocaurrgFMQCX04Of9YhAzKMbWkQilZJg4aomWNFFAOQKw8hyb7zLWZoAn-6hA6S3167zdAEn_YQPNDG2BOtAf-L0mLAFbbNTyaFoDqlhs3anMmSmXMH9s-qrYsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736c3c8edd.mp4?token=t6GddzlbC37KcJjQtwgTYEEsgSJbBcMNkWrsOifVtc_3ltb-BhSaTeQFcl24oZsF84TQIn6pO61OW_oaHQVuZ7UIHOcRGZusG256QP87r7bh7wnSzrhs8xiBH5pYx7DBXa6-BD7nI08eiyVbxVSRdky-yw16itoSyWNB64fprhMRC6Ku4l7MvV2TVRyNmK0qv5hbeQAtKEaUKo9fXxsALTchsiUocaurrgFMQCX04Of9YhAzKMbWkQilZJg4aomWNFFAOQKw8hyb7zLWZoAn-6hA6S3167zdAEn_YQPNDG2BOtAf-L0mLAFbbNTyaFoDqlhs3anMmSmXMH9s-qrYsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به مارکو روبیو در وزارت خارجه ایتالیا
سند و شجره نامه خانوادگی‌اش اهدا شد.
خانواده مادری او ایتالیایی است
(از منطقه پیه‌مونته - تورین)
و خانواده پدری او از اسپانیاست (سویل)
او کوبایی است.
در این مراسم گفت : از طریق یک اپلیکیشن ایتالیایی تمرین میکردم. همه رو متوجه میشم! (به خاطر اینکه زبان‌ خودش اسپانیایی است، متوجه میشه
و نه فقط ا‌پلیکیشن و تمرین ایتالیایی)
هر چی وزیر خارجه (ایتالیا ) میگه متوجه میشم.
اصلا نیازی به هدفون و ترجمه نیست.
دفعه بعد که اومدم ایتالیا، سعی میکنم که بتونم
به ایتالیایی هم پاسخ بدم و صحبت کنم.
باید اپلیکیشن زبانم رو هم تمدید کنم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jfi9cCpVdpdjqM1mH4FnraKBQtdYvN3NmflUR4Q1kZPVSutpHWhZ2ieH2-YADdpAvtXKk-nhCoQ9R9jtqOccpq3nyRXDkMkW1GWFJPiMB5RNTYCBOceYuB8-waNHEL5bZvajp-zoiAAbNUKboAt4bskWVqPpZVZAigVmtVTSLsYZ-pKpidcE2yRfv8U7A0RMulkNQtT-ehvWKv1Oszs7b_JJlpvxc97IZAlrTz6a62c_6jJeKRc5ciYXzz3pybmCBp7cBdyvJSOcryxVeF86JAugZy8F2PwqhsS4tlYrH1U4GwZ1do2lSCK7O9LZweP7uVhZt43fBxrkBg6qUSNQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5PBVGiCWxT1NZ603E-lWiHvR7zCWaVnFhyN0srRCe8O0032Vo8zC09LOdhVnG4kA5ctNfW30324p63FGVcIbaYl2TOXNYKN2bY_dmyc37keH9VgiGY4p6Ea7s5L2oddCqvTTbpkCr2sM3Ie-gPsFNr0uQpnlWmcWXHBNZv5389kLN77ciJVq3IAD0g_v26F2CsLUE99MKk_gmuv7JwBageEHYd4I-aHICnNsBib7cJSPXKmlyT5SSo_Q50vrjP9DFNaubJ6wxrmciTkT9KfG5FnARXKNNy4PFMDEQLrPyEnHwPNT9D3KnmY-oKueqPBItwF00voxLEvfXLTARPjOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=p4ljMuSK4cfpjxHAqgxqtWcSOu_ArvSgQzzlzJtkFq30fFyWsoVpeIPrCSrqET2tHeHyBEbDioIr3LPq66m1kQ1nicWsFYmtWGzf3SxUyMSJDqe38EcFw_jlif2x0l6RDz3Dlkgd3nVZEasd0FlMJp7BUprVGHM-YKFl4yr2QEZiGVYOnBUVRAsigfop6Jg4kBKkBeHZbjqrisuNF94Wv55nzfQ4Eadw_QXLIgGC6WbSoESF3MVDcAVN5q2zegltlFpqUtC24gGu5X7i4FcQ0T-VqwsA5TogySY2yagSJ1tsoM60Z_FGFjIz-ELs4Sjw9g0cF3NXShFJQ6JLOV7a3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=p4ljMuSK4cfpjxHAqgxqtWcSOu_ArvSgQzzlzJtkFq30fFyWsoVpeIPrCSrqET2tHeHyBEbDioIr3LPq66m1kQ1nicWsFYmtWGzf3SxUyMSJDqe38EcFw_jlif2x0l6RDz3Dlkgd3nVZEasd0FlMJp7BUprVGHM-YKFl4yr2QEZiGVYOnBUVRAsigfop6Jg4kBKkBeHZbjqrisuNF94Wv55nzfQ4Eadw_QXLIgGC6WbSoESF3MVDcAVN5q2zegltlFpqUtC24gGu5X7i4FcQ0T-VqwsA5TogySY2yagSJ1tsoM60Z_FGFjIz-ELs4Sjw9g0cF3NXShFJQ6JLOV7a3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-rfdyEaczPbP7wja8oFc8G4mfb71RMWrV10pWo654S2RrTrkuwEg2qRJr0S3Dv-41zxcPcn_hoCT4yi8Pys6_jIDZ4T1gPBxKxXXq2IuJtJcthoyzvRIVh2LFDA_bmdjpBvktZbbC0P2v1aMS06dsegug_Jo7b32aTxe46L2yGYlIOm1gkxbJf_C5P6QD6eCx9ECp_vVqxT4vjDufmBC2KlX47oD5VhQcXhC6g7Ro09kKyM3m9Om66ngZ6pD78PQ3Sg_aCcv42eIq6QeT4Oc2ld1BDoajpJCoIDdvDOFD3LFLc6Pi90uS8F-JYsggwWRd3hu7WBtl9k1f36PGQmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8lmXRl3sYfTU_ibf6KnFV1xHPuEU0-UN1lQ-fQ-M6-eAAHy2D943qWk36WRUssynJzpc1YkDoH_LjhI7Httz8Uh-B8O51bYUIHfK_VTq8TfHkfRRXG3FMG0iC4m7H6Owi70sSViEL71pe2A_XOTuUuPEL0F9VxiX3vZtdbR5zAF7EeejYDZ49Ay_jsDxTA3asnx8KPcPYAO7pvSJM6iKzZy8uGHPAdniT_NF27MPyB899mK0Fmu43pI4dz44MbwvNpLJd9VhgBi7pK8mDJ_FntKw66KjUmxYZJKK3fwvPnqgImvEch_oGEvy8caM9jL6yg0XZOdfYIC4ybrXd-h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ سال پیش در ۱۹۳۶و در آستانه برگزاری بازی‌های المپیک برلین در آلمان نازی دستورهای خاصی صادر شد.
مثلا گفتن که دامن زنان در این مدت
می‌تونه ۵ سانتیمتر کوتاه‌تر باشه،
گفتن یهود ستیزی باید کاملا متوقف بشه
که وقتی خارجی‌ها و خبرنگارها میان،
بهشون بگیم این حرف‌ها، فقط تبلیغات
دروغین خارجی علیه آلمانه و واقعیت نداره.
یا مثلا دستور دادن، بخش زیادی از نظامی‌ها و پلیس،
با لباس مردم عادی توی خیابون باشن تا جو پلیسی و نظامی به نظر نیاد و عادی باشه و نشون بدیم آلمان نازی اصلا با تبلیغاتی که بیرون آلمان میگن واقعیت نداره.
حالا توی جمهوری اسلامی این چند روز
زنان بی‌حجاب رو ویترین کردن! و طوری وانمود میکنن انگار ما اینها و سوابق شون و دستهای خو‌نین‌شون
رو نمی‌شناسیم.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvBhT2IxUVGvoF0NZBtcALo9ZGiefT4rZok9TBSNmjunZMAYW_tQ1OuinAIUKO4fnwXXNuABwWHKp1h8NsM5B6vbUbF0IK9i1MGopw9iVQd7jlVxeI8sRTKoPs8MUzBf7ZBiWxl52KV4Wkj0ts6GT_QAk8LpQRu9LzTn0V-uF7z0Jnp6BGuZOtpMQfUOWQ2CcSm5laePL1KR5JBdt-joFdUFfURyBeinyQPRBn2KikcvoghaiSWrXfKXcZVwg-seVPcBoWSdJn4pOhwiqElXCW-SuyN0sWyFwh1iEw8-DeMlhAynvpp2c3pQw3uwEvJSSsr5r84dvSMd2BobWYEkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AChuH90xUDsTDGm5c55IMap2XofuZGLBngO0-2l2b43szNSGY1gwtD2WPOEvapIUYcu9xysLooXOoWMb4kIcIXSnZwp2MjToMBOwa7LQx2_KAxK0sObEXl-lolWaSsyBlh327h2gwcDndJHxLMOl86nUo8Ltb7Of1S6Ir70O40yfRn62KHlNCVwhSBQDn7I0SNpFID5oaelNxKd1ZORH2sGSLnzaNLm4oUTlhqbAwsIRSN-PHr4Sr8CgyIl6Dk1MSq3SI6urE79Q3i-5aZGxWF4gFKclTzVE1A4cM0nVyyUQAayGqI_wsmrsx9mYmN_JJUBAZf_RV24in-X-LZvQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFHn8qHfAWBZuRhO8-BOcPyaKWtIHd3Rk1p4grT5_CZRoblMiiogmVbJJVmuv-BBz2q20UpO2BFjOGOntC1C9YMmbBGhcKI0K81X4MoedlbP56Gzawilj_skV_dysx8LgFwHGMkHCMG1I7YKcxK9FJEdV86b_2pe-Hw6syWK_IJLnuxycV6p8wuBjIgjhqvEQXoVA1QbtNPyhiPOLmNRU1pJkuWPLlgHUf7nvAuaQaL8DWFXJNZkTXXvGJM0wnCvymUqCeDLeMyXEtw-O-4nm_vmy1W0dl71q4-wmrgazyfeJb6j-yIpygvRkGTKolD0dnZG1JvK6YjMdeoyH4w-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ‌دست به اخراج گروهی از شیعیان پاکستانی مقیم امارات زده که برای جمهوری اسلامی تبلیغ میکنن.
🔺
امارات چند سال پیش یک وام ۳.۵ میلیارد دلاری
هم به پاکستان داده بود، که چون پاکستان
آه در بساط نداشت، هی تمدید می‌کرد،
که بعد از خودشیرینی‌های پاکستان برای جوش دادن معامله بین جمهوری اسلامی و ترامپ، امارات بهش گفت سریعا این بدهی‌ات رو پرداخت کن!
که یک شوک عظیم روی اقتصاد پاکستان ایجاد کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/4880" target="_blank">📅 12:23 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiuiabuTfxYWC0OFlBGCP4HFoZKq_cS910u4kEqeRYFZBqIalVBRH2UdMqOHTwo0Ha4taWKEqrWDA2_w3nbmgVHaslNxzaMhWLtty2T0qkqENi5Xvw1kU2Xp-I8C0jM9j4rkP_mWWRONdAUSCwfQUtaNDyngQT7q7NELIvRNrBP57KlWNSPmVrz042AvkO5BUORrK650I-61eBO3MHItdRm29hqe9p5zYrq-x-mEbfjytmqoGDYy_AXUbwlSPgCn1upTg9NKrDVCVB6vqHohDPJ0skOZIAo8M1oPIXhxW0Fy9VNdsBm_Kr0NsDWZ0ZsghY-EmGmdp5nGlBMJZjEeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت «مبعوث» شده :))
این هندونه رو  این چند هفته حاکمان
جمهوری اسلامی زیر بغل عمله‌هاشون میگذارن!
که منظورشون چیه؟ مبعوث/ برگزیده شده برای مبارزه با آمریکا و اسرائیل!
«قوم برگزیده» لقب معروف و شاخص قوم یهوده! برگزیدگی هم از سوی خدا بوده!
اینو فقط تورات میگه؟
نه! قرآن هم اشاره داره بهش:
سوره بقره، آیه ۴۷:
يَا بَنِي إِسْرَائِيلَ اذْكُرُوا نِعْمَتِيَ الَّتِي أَنْعَمْتُ عَلَيْكُمْ  وَأَنِّي فَضَّلْتُكُمْ عَلَى الْعَالَمِينَ
«ای بنی‌اسرائیل، نعمت مرا که به شما عطا کردم به یاد آورید، و اینکه شما را بر جهانیان برتری دادم.»  بخش بزرگی از کینه مسلمانان به یهودیان از  شدت «حسادت» میاد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/4878" target="_blank">📅 18:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgxjeX1ne5mRjgl9Pjq_HfKazeE4TNcotXIDzT5L8T5t-vurO8gpov8wl_PTRHpKv0H2dkoKnv7tSqxORGU82TOsG0pYBL1Frl846A4_Tyud7-_8tbFRrxjtW6lPLr6tq03UirjPbTEEXjNqGYKP7gPV3D33dVDm1-ymA6bFeE1lLEjMGbFOZ_NYy1gfb1wdeo2vfwKifRNxZ0lyzIDu0nC4g4VICvbttHmgQ-uR6wq7gSLZZauI3i0T_2fJnDeRjah7jTYiBDsUTJhMDAmGImR7MgZlwPhrWxLKIczWliLN5t2bjPtfsTrfOqr2DP8L5qi93orRoIikwwQGe_zOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط واسه اینکه
روزنه‌ای متفاوت داشته باشید :
در قرآن بیش از ۴۰ بار واژه «اسرائیل» ذکر شده! اما یکبار هم اسم فلسطین نیومده! حتی به روایت صریح قرآن (یعنی
آیه ۲۱ سوره مائده
)
موسی که به‌ دستور خدا رفته بود قوم بنی‌اسرائیل رو از مصر خارج کرده بود و آورده بود تا «سرزمین وعده داده شده» (فلسطین) رو بهشون بده، میگه : « ای قوم من! وارد سرزمین مقدسی شوید که خدا برای شما مقرر کرده است، و به عقب بازنگردید، که زیانکار خواهید شد.» !
يَا قَوْمِ ادْخُلُوا الْأَرْضَ الْمُقَدَّسَةَ الَّتِي كَتَبَ اللَّهُ لَكُمْ وَلَا تَرْتَدُّوا عَلَىٰ أَدْبَارِكُمْ فَتَنقَلِبُوا خَاسِرِينَ
بله! پیامبر خدا، موسی، به روایت صریح قرآن ، به قوم یهود گفته وارد این سرزمین «
مقرر شده
» «
از سوی خدا
» شوید
و خارج هم نشوید
!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1pnwgQB21uvW8Oy73oujEOvdtuka8UrCPEQeHoKbnTYLf6Nd0c6Zxny1lj58yKeCZH3LNWUAZBZGue2wZ04Z045n9-QQmH4AxfLiiucIE3yBlb3h8aBrq92obG5xLZzED47TGVj9koTq8KPX3HmTPQ0tVAqwdis3q-jJPb2-5F9BESlshzpw4hD_VOJ14z7wzllCFw_K3BoPiSfg9NDZBbo0ddQNL8mdqOzK6dga8T7ZvggyU2UIZXYtBJfUuM3fvG10cSFpVhyC-6lTVG--_Pkht4b_10pdU31CG87P6TdtbIv6yPdN-NXDCdBDAr7_3TjDRCWyp0HLit8Z3AXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4jxdndJseGOLhncRJR9AEKT4fSDMX2EWw-weGuCSeSYLK7Af_IJgs5g-nKyLTm6S0Vw_umwrD9Q_tkP2sQbULK7VUhgCdT7CMV_kJuGq3_I9VcSIFI8gJAicmTKe9A6f0yRsFHmHNeOfnOzwBgPx8fQFAHpcqeI53YvyN3ZNIHI1uc0Cw4ftCOkFpKgZXYHN54YkdbHrhGNMXrAkM0ivTIrmi373x0K3KtJ2cab_pFI-RAxQlZ9sqm_wBxzFooEszzvQlKRXUgTgJt8Sp2I-G4PGXN1zKkCMCb8OeRJ8kWtOrX-xqKTBZiCei0SUk1oa-8aX2Cdn4AC2ud2MTFc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXP2CLngKewVK5xHGUUbEex6M1YAyaxgaHFEXsx8RQGTTO3rNJeBnQ-YRN6OuCDmwvMxeNUOVq2QIrgxhbDpmZbqDcj2WMmau_9HR5vxYoJ9mf9FMvGTgn8sl_-Ry-B6SGBgbbzqGuRWxFGzcOaYPCHbyMHH4p4aj7RbkcaEMAhz-dGQmipEBspqPiixeW8CYxKPNYEbWIRsWt3kW0UC3j6mOGfgGGZ0q0rmYe4qjpcsdCLVZT05VtHU5KeHaWWgeBJYY_-cM_HaeomRJtTyxfpsrxEvWPtGxQ9fPkK6mCMrSqjHBB9Mos0HKUcUU4mfxlk8Gv3s2Fwx9vb1XH8sVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex4Lk3qDaZUsJfWAdJPO1DrWBoH8hF_-QKIb83InoPFfksyAMkWWBlylPxBJuRgXWUCHCRV9DUjwrgacT270HWuIR4FD_DjJHEaGuXZHNh1lWxiw339KJ1TedQnQN18zo7nWFUlamFdGqgunlFWX6VS2Lgtukx_nbQtmm_4SzRMbc6diNxkWdlQ7zA9EJhjt-nLacB6v1AbbHs39Qgb8c2FAjiAwTu5Jcc-xc63W9E5Thh_m6fSbo6ZWNoNTtennvFspS5_Az4SroDOoZJ4lSp1yCjprm6vz6RmNgToZ77-n2QhM-wXo1s7b5dp-7lVqzel4OoZ5xdtsWJZDjqkZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gycVQ78HtYlfxDOG2Q6r3Kvu_HqRGD-vYVbbHb2R1J42Z4Hzlxljcb9ToMi08C8_KYn4ceVlh-manYZbSJlTt8wPBRT3PCrQqnlTrYsnvsZJwSdfNaMeH-jpDMGSq60OljpAuKgGVrY2d8tCzi-Qkd3cUVn1PC52yJE-NWFYTLiyHa24z6DmJKBJuo0BIvnv98haW_3m-cFBOuIKYes870vbxm-4px7UyofTQNLZmITMzE_c6N4FbmtuW7pnZMYAqJ1flR_NibpzwE4nCKfGGVbZOKnjKz83jjy1YtpLuVNEzFLE_4riCBATliD9ICe2f-XHIyP1FLUKEjyHA8LNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-s4acn0MzgN0gXnFyGcg2AYcdEVWElycXkDDNEoIN9Qheul-u_QE6nocECMJEvH97t6bA504ORSj-4BHCxcYUZUEriteyrWPYGZ9RAfB5k-xZyCbEm_7FtXrUwhKBQN2ShA-7vzzPsDtU_Bo_7cSb2D679b-Xr-ewZWShy9EaM71GSt7Zw4AgkuFX8Q1IPqY_rlb_ZM3RuDNXgIyyAqfpFppRwlaHaaE3tvFH2O7_pSB1mkbnF9DV0HooqaOpY7KZp-SMbBLN1qD7FvhDtOmu9knMUMiHVEw8A7F7IwwM0NOA4M4ty-fv4R_p7LSEXJPqLOk5G-rFOl1-MzBje7Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=MLiWrqbdshD4RzFUn5M5z7Hw__E2vKQ39m0UpLODDMMzkPoGp-gyItYcGmaib_ZJpBmLrxpgGP-OwBaHfA4Z0juihVPab6Epg60uYe6x-FzjFPo2hJLezqKlIf9vgET_tZ6rjVDWUDvugOxxwjaHyLw978i3gPTlBgV-Jq4EDI3QKwKJL4XyE9Mv20KQB9lkJu-9qC2F0Gd_PPbHcjrWuluZ9HBna6ysUS2-C8Jkd80I8w9ZeVJ-WgN0hLcO_TSEVP524CBWhyaEoGyjZK3A0x_-I71hQKQC7jQ2VvZeMgdJwq93dZFlXQhmVrJUJuUBnFCEBw2SxFJ-uIt0Ckl6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=MLiWrqbdshD4RzFUn5M5z7Hw__E2vKQ39m0UpLODDMMzkPoGp-gyItYcGmaib_ZJpBmLrxpgGP-OwBaHfA4Z0juihVPab6Epg60uYe6x-FzjFPo2hJLezqKlIf9vgET_tZ6rjVDWUDvugOxxwjaHyLw978i3gPTlBgV-Jq4EDI3QKwKJL4XyE9Mv20KQB9lkJu-9qC2F0Gd_PPbHcjrWuluZ9HBna6ysUS2-C8Jkd80I8w9ZeVJ-WgN0hLcO_TSEVP524CBWhyaEoGyjZK3A0x_-I71hQKQC7jQ2VvZeMgdJwq93dZFlXQhmVrJUJuUBnFCEBw2SxFJ-uIt0Ckl6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،
یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت
از امارات در این کشور مستقر کرد
(همراه با خلبانان مصری).
رئیس جمهور مصر گفت :
«هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر قرار می‌دهد.
ما از امنیت و ثبات امارات حمایت می‌کنیم و تجاوزات ایران را رد می‌کنیم.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBrKt6szp0UiGZzs_Gq-ofOWD6gemczU2RW2FpmDi3G4aeoqxNDGPuFy2huMEAcl2WMZLfqaD75F5MA-Hd5GSnDHK3qwL901yUm_XBss-nUbhe6bwabofQqQq2w9cZtW7Z2WUQlynAigG-OlKFpX2lJH94kc8AUn6Hq9zffm99svhmpc8Yl_raafNV9DVrPXB0xaRqJE7qC91bQNpXNXykEgsdQ9ok5YBqAmDBs6E7DoBcdZn3l6LH0Bl9kIbme2H_75kAUpKfsBOJBlb4LjKizGt7ZdNRtQ8Swyy5TtdFarzV9dMUnSSfwvKL_OwMmnovZBFWiHdLKJ-zR6bSRqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXWCQ4UBkN8PqMt08Ol8YGO1Sj9VXfLct53wRyPshQWXZ4C1XP-6IlPt1c-0luAzC5LCo8cmzyqo9Hs6ZzSjfpOyQUnSQ7jEvmYbohBuiC6Jmrg8n4rCRixWty-zq_FyhEeK1qaKixY1lUfBB9dVWJBVNoOEo9A04zDgphUj6yd7BbR_a6MjjfHX12DYiPGdbJ0l-dn8PWgqB_dPwlHb_dgJhbuqdwtvpedpiVQGYr1OEDBxem6o4eSrOtDllOOv_by7hJ-yoF0DbpB4-86P1LMsopfyL1jsK20Q_NikaW44EDBANOH1aQqpWF6srcTAfkjTyq2f16e934QrnkN37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lo0m2H2TMEdq6UOIlV9jW_O-tF8MlewGNaPfpyHe-8RC-Sp9ttdK7Oio-5_gCnlgKFLMwy35Ssl3vdTdtCfjjRn8lb5dYPJ7Yi56yaC9hiF-6ouZC4hYVDTAMbs2x2M8ECeTKPvKw7G-6N7mSgDIBQYI1wmFEif6I9zKlWt-Og-iKEBkkSzuzKlRPr3eGjFr0uDd0-ObVzio5koqy9fPBnI_W3YDN_cr2eqACGj1kaAfNeFbwlba22Dh8rH-HGhM4P0WQAXiTBFXQiWLSQUA0MC6j9I-5Rs1mdE-OMhy9JH10NnsqJdvYQfdrfPZHSV0k0ylL54aXrtir61z3wZu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzqoRhPU2yYcuM-kpL5ps9rJmhxp9O7YDvCtT2kWwNnAPDxy4KCRZ2BcWPv-DiVGjN4QZviBFUThYoMtn4kPbE9YzJDZ8YMBsRQWbOvgXfG4NWKrvUlDAocoJahPjN61gLLqOm95-EYUwCbNBELCg5jhL7osmT6AqVz-_esf62UMvKsrN5YLJNWgbGDDeGcP9hyVbe4S8uU2lDNbRdw6kpzrkiKZjiKtB19ZQwFjJX6MdcxJDJOS0kKXPPrWZAyi_RkodTAXeTvgifSFn610PQEhFaGPzg3o10HxKEQOM3IvHT9A6nIm6-8B08M1YnA4hiQVZDAyJVluh5vB5Nq4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvNPG3wtmCVqr4LiNqFaoB5omH1b0S0XTQ5ma8ILOzi4dahLY9I0OGrNOFvdYgZXo6QqaP4YqGCSzSJMMdsj2pe69agMkFyAspqpjNiV755_C8q9Rd5SDUo80wUo8A8QuacPRhUK6_vj-ZjGvodwyL4kLX1wcv_8SxchyOe4-HH1LOj6Bh-T9mavjij-wPtKO34fQDFMpOovOwCDlhDA-itPvpb_T2o2nyUJmmYViVh28qyPpcJRrsN_Lsci1SzJ6Ns_5V67ndsc0uZcmAmTB9OEqHBZGLwEFBes06JauUVB3zjJnmkLOXBOiOCQZyTLWeBP0r1NK7q6UrgtIZz3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKgApH_0xHb7QIgz11ikmNurmVN4ziQWZmoT_uLmC5HiRSBSFG84XODxfdP1X-FnvwNpwhZZv14LMZsyQpYf46-1wkBakwtK_Aylf-uMk3VhlLtub7tQYJvb8PzHmMMfQa4OdRZuPcYcjL5qRI_niPgkCsRryWvHoP-EwNqiN451nF_n9ycnNJt0CFDWb_HQ90PVTeYECnWotcGMo5Dz9TgdBErJq0RJy0iHo4WjDpwMY4wLXeMpng6_9K7rLDb7TBOqynWMOg_pJ_Rqc3RbNJAzpV3rqQKDIRXJSSAt0peKmRoYN73wdUYUfvAqWLOMS5hLB9a3RMmpw18SDe45eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd3udN-2Oi-bvWDTy-d9rbZSBnn8MygbkjRUpONdTAIiWnouXK8LB-dL66mZrn2cccbibaXyrQNmwBfPy_zHIQwRuyKA8VVMRUPAF2-u4Eu179r6fLYLEpUkG6FwFuvz60fEm0PEVNXruWrXnA-VcWs0TgWiImEEp05wWtEW6u4NRjMV8DPlEvvFsFrYr__bRGvGgpPjuSymPOo1VxgtTtKGCv8fYZzcqW7tk3YdJhbmAtEm3mTomyKwqjxFW7rLTf-9ctPFx1mOck-PcvjlHrO_lYCRiOyW59tF1PqPveZOy2QAaRYxLNvF9CtrNUUGo5AQsRjnH7zW76SGpxqHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
🔺
سه ناوشکن آمریکایی درجه یک جهان همین الان با موفقیت زیاد از تنگه هرمز عبور کردند در حالی که زیر آتش بودند. به این سه ناوشکن هیچ آسیبی نرسید،
🔺
اما به مهاجمان ایرانی خسارت عظیمی وارد شد.آنها به طور کامل همراه با قایق‌های کوچک متعدد که برای جایگزینی نیروی دریایی کاملاً سرکوب شده‌شان استفاده می‌شوند، نابود شدند.
🔺
این قایق‌ها به سرعت و به طور مؤثر به ته دریا رفتند. به ناوشکن‌های ما موشک شلیک شد که به راحتی سرنگون شدند. همچنین پهپادهایی آمدند که در هوا سوختند. آنها به زیبایی در اقیانوس سقوط کردند، مثل پروانه‌ای که به قبرش فرود می‌آید!
🔺
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند،
اما ایران کشور عادی نیست. آنها توسط دیوانگان اداره می‌شوند و اگر فرصتی برای استفاده از سلاح هسته‌ای داشتند، بدون تردید این کار را می‌کردند اما هرگز چنین فرصتی نخواهند داشت و همانطور که امروز دوباره آنها را شکست دادیم، در آینده بسیار سخت‌تر و بی‌رحمانه‌تر شکستشان خواهیم داد اگر سریعاً توافق خود را امضا نکنند
!
🔺
سه ناوشکن ما با خدمه‌های شگفت‌انگیزشان اکنون به محاصره دریایی ما می‌پیوندند که واقعاً «دیوار فولادی» است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4859" target="_blank">📅 09:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia2X5IFnrD5pBpfgo1a9f9UyEA235zVGl5EE1YsqcJEYzuLdG8B3ZPtP2lw9gJO-oJbw5oYFLtw4WwVcp_DfrvyLU_c5dsBibAIpe4UD0lCiVh8XD0f4ln50rStf_o5BTLbY7HCDnyk1_2bPI_sHnGNCA2ez3BUME17TlPOlKL_XSplGssas62mKGDWGnRgh8539x8DeatE4tEmIx71Tn1A2qJMqAToCBQfVhJeSLBKfRY9fAW17Yb_ZBoNLT7NRN3KAQN00WRjQ5xU7aulbcZh9OgpuNt5vPCyu7n4NUCdt0CmLZbADRdDZxiU0IfTWghMiK2I0dwJuoc7HasTh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu-98lkFIZthrJJcUYQ1gRt_37yOfKUl4tuO4okGVvuiKQbFESsZ07Dj_WOhT7mgL5hmgJs-M3ZNNKKugrlO0pypvaCtsBRS-mojKSPYfyR4j7_dzGjS9cI9E7pkatEM8rGtk5IJqJBUEdJdkvxjbx3ZFJ0zXVU8XTwwE4Ud3aYbYoxFSaRdoyXPgjTT-Z59HjF3QVaaDiFwGnMrgdcTwdkzLLZPRukt7hy3zNQLfMjGRIDwilhrs_2I6QiXpHkmItKIos1AyJGwR0VoZl3OQNYFP19LU3YCJimFRX3dq0TwQFHaYW8OrgxQmLMp9WkWDbZRQrsXTzYzoO--S9Fksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
تداوم درگیری های نظامی
🔺
گزارش‌هایی از حمله به بوشهر
🔺
گزارش‌هایی از فعال شدن پدافند در شیراز
🚨
حمله آمریکا به میناب</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4856" target="_blank">📅 00:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXyyjyqIs-p80aIUl4RO1uCcy7eLER8E2x166wB3_PR2U9-KVJPhCtrbwdfKHZ3SKJVYZtn4kRL387i_QqVQLh3yuDB73vWWDlr5PHTDjPLzDbr19O1iN3C1IEKmjNH6wxlR0RXjw4GSdf9h9b2kLD07SvX82nSAAi9Gb6XgCH9A_CFJ-HyeCtRE1-7nkE2ukFyaXqmZMZ3xOgz_XjrV4XCcgaLF7LJrNF-ye5EBkKJe0BcMTbc7rMxu53py1r3FMUPzdShA2H425KmuO_CKFx222-G5MmC_iQW_PluV3yUQnjkQ_E_P_ORMHNHAcaJnX7qqdy6HuaJgOW4VUrbq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی  به نقل از منبع مطلع نظامی: «
حملات نیروی دریایی ایران به ناوشکن‌های آمریکایی در دریای عمان ادامه دارد.
ماجراهای امشب از تعرض ارتش آمریکا به یک نفتکش ایرانی آغاز شد و پس از آن شناورهای نظامی آمریکا هدف حملات موشکی و پهپادی نیروی دریایی قرار گرفتند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4853" target="_blank">📅 00:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
تسنیم: «۳ ناوشکن آمریکایی
در نزدیکی تنگه هرمز هدف حمله نیروی دریایی جمهوری اسلامی قرار گرفت»
🚨
خبرهایی از شنیده شدن صدای انفجار در ابوظبی و‌ دوبی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4852" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
فاکس نیوز:‏ ایالات متحده حملاتی
را به بندر قشم و بندرعباس ایران انجام داده است، اما یک مقام ارشد آمریکایی می‌گوید این به معنای
از سرگیری جنگ نیست.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4851" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در حالی که خبر فعالیت پدافند در تهران منتشر میشه، جمهوری اسلامی هنوز دقیقا نمی‌دونه کی امشب بهش در قشم و بندرعباس و‌ تهران حمله کرده!
فعلا میگه اماراته، اما نمی‌دونه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4850" target="_blank">📅 00:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=SK5iDZJVeKOtUU3oUpe3kHyQwT1C-6-LkS3HGD0mwbrZ9wSMI2E-6vJwAgRJtxNqx0aygxZNJc74q11ENqCuAAnWc_VoNZWHlkyewYDCP1Iew05jDrICRKR_5yvRuOYV2lV65WRPwSRaGqfGHnXrC-icABVKZZUW4rOXx8IxtQdBYGHtOeiSZJdPc2jI2P-LhrV3AkeozLwi67ZBKcmQUx1DW64ckEYtY3q-r1-Lu2v5_Fp8iRCISeF4qGjZavCzn16FWcXt7ctK-aqW8I8bEw48Bs99heHRa6dm_OAoFM6fPia37nlBrmDX5K9WsCfB-lR2umf4FPwgVJH3L2QGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=SK5iDZJVeKOtUU3oUpe3kHyQwT1C-6-LkS3HGD0mwbrZ9wSMI2E-6vJwAgRJtxNqx0aygxZNJc74q11ENqCuAAnWc_VoNZWHlkyewYDCP1Iew05jDrICRKR_5yvRuOYV2lV65WRPwSRaGqfGHnXrC-icABVKZZUW4rOXx8IxtQdBYGHtOeiSZJdPc2jI2P-LhrV3AkeozLwi67ZBKcmQUx1DW64ckEYtY3q-r1-Lu2v5_Fp8iRCISeF4qGjZavCzn16FWcXt7ctK-aqW8I8bEw48Bs99heHRa6dm_OAoFM6fPia37nlBrmDX5K9WsCfB-lR2umf4FPwgVJH3L2QGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش صدا و‌سیما
از درگیری نظامی رخ داده بین ارتش
آمریکا و نیروهای نظامی جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4849" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4848" target="_blank">📅 23:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
پایگاه هوایی بندر عباس، کشتی سازی قشم، اسکله بندر قشم و چند ساختمان اداری اسکله قشم ، امشب مورد حمله قرار گرفتند.
🚨
رسانه‌های اسرائیلی به نقل از منابع آگاه وقوع درگیری نظامی امشب میان ارتش آمریکا و جمهوری اسلامی را تایید کردند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4847" target="_blank">📅 23:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏صدا و سیما به نقل از یک مقام آگاه نظامی:  «به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی یگان های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
🔺
برخی رسانه‌ها از شریک  ۷-۸ موشک خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4846" target="_blank">📅 23:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
منابع اسرائیلی : در حملات امشب به جنوب ایران، اسرائیل نقشی نداشت.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4845" target="_blank">📅 23:05 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های تایید شده از انفجار  در بندرعباس و قشم خبر می‌دهند،  و گزارش‌های هنوز تایید نشده  از شنیده شدن صدای انفجارها  در میناب،  بندر خمیر و سیریک خبر می‌دهند.
🚨
برخی رسانه‌ها از احتمال  حمله امارات به بنادر جنوبی خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4844" target="_blank">📅 23:03 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرگزاری‌های داخلی از حمله «دشمن» خبر داده‌اند، اما مشخص نیست منظور کدوم کشوره، آمریکا؟ امارات؟؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4843" target="_blank">📅 23:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4842" target="_blank">📅 22:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imudq9jrsvXx0VoFkfpuxrl97ci8XhzN0uZidzWtT155P9s1ami1acUowXamNhDZ5f-4bgGemTu3LDWyridNI8Iul6Mbt5JOM56YFr-oCVUaqGpN-CZfpFSEuWHsRgvSf-Fbkjh7Dp74C1nRwEfvD5fLgtgLSmi45uQfK7Y9EHRQ4-ebc4dpY9EY32Jl5fNPI09YwoPU1n90dttgMxN6o59D5fsfGLpPr95Mq7ewq27bFOVy5jS29W0rvkPO3Ybe1bWtinaKLzEJBgrJ0ayml3oXs3hOHt86cyMzQHZdRNdRFynWtSsMHxj8CAFgj2rDAwxpwoIHayJMTm4GfSjxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم
خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4841" target="_blank">📅 22:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
روزنامه وال‌استریت ژورنال به نقل از مقامات آمریکایی و سعودی نوشته عربستان سعودی و کویت محدودیت‌هایی را که برای استفاده ارتش ایالات متحده از پایگاه‌ها و حریم هوایی این کشورها وضع کرده بودند، لغو کردند.
روزنامه آمریکایی نوشته لغو این تصمیمات، مانع بزرگی را که پیش روی تلاش‌های ترامپ برای عبور کشتی‌ها از این آبراه حیاتی قرار داشت، از میان برمی‌دارد و مسیر را برای ازسرگیری عملیات «پروژه آزادی» در روزهای آینده هموار می‌کند.
مقامات آمریکایی اعلام کردند که دولت ترامپ اکنون به دنبال ازسرگیری عملیات هدایت کشتی‌های تجاری با پشتیبانی دریایی و هوایی است؛ عملیاتی که پیش‌تر در این هفته، تنها 36 ساعت پس از آغاز، متوقف شده بود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4840" target="_blank">📅 22:08 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtN05ioF169fRxoiKYz-rvKswB4fLaHDdoy-_jk-wf_8CaTlL2DiKrXAoxK6myF38WeYxUHCoe4c6ieZd3HAsoTm6sWGuXnZhTw0EWQ49pznp-K8rAnorOeDXPbMPIrbMm-s7aVN_alPVHU-aBZYRY-bSAKgEZgOKbTU1PFFq4fGW2B4S1G7Xq9vMh4m6QkZq0HbaHWqGzci43b581rG-rqtVRo8wBMwXLWsy_tADc7qttH0Iv5FPYF3RsYTW7UhXUJoAOxhy8zAOtX6hAXB85QHPWsV7BZ1M42AOyXVXxmTOrZy-mkEyV709OBtrT4NLAIzxoSsJNnXWhIRl7uwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی
منبع شرارته! محصولی جز تولید
نکبت و سرکوب و عقب‌ماندگی نداره !</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4839" target="_blank">📅 16:24 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3gl4pWGGCBJ7GuSJTmtpVkDqx0OC6v2Ku6rl3akZ9kaGprA4XU9HMLWUkl-SpA9ahXaC4IU5zZOaci1W32o6mGS6Rn8q-g3JdW5O32tgVRMU8npCbjGZSCklnFiFhwqhN0Sz4zABkX_anS6d9JbNCh_qC9EzPsRV5mUgxHFNpFQoquWl6w-BSDOzplim2rpqHFgvoM-U9tQ_eiGGiBZUFD2mHHQZMvfSlvzPo4ntytuz6Dtfrl5YTarUZDsnaJMjFGKNGpT7UJqbdPQC82H68Bq-9a6c3nDgmU8iqxAj78Qstd3vDWuZm5pSyRcjgR8U39fJl6-lz5n_6lTqtPmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری چندین شهر و روستا در استان نبطیه در جنوب لبنان را صادر کرد.
با اینکه اسما هنوز آتش‌بس میان حزب‌الله و اسرائیل برقرار است، از دو روز پیش درگیری نظامی میان ارتش اسرائیل و گروه تروریستی حزب‌الله لبنان افزایش یافته.
دیروز ارتش اسرائیل در حمله‌ای به جنوب بیروت، فرمانده نیروهای نخبه حزب الله موسوم به «تیپ رضوان» را همراه با چند نیروی ارشد نظامی حزب الله کشت.
طبق گفتگوی آمریکا و اسرائیل، قرار بود اسرائیل به بیروت حمله نکند اما فرصت را برای حذف چند عضو ارشد نظامی حزب‌الله از دست نداد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4838" target="_blank">📅 13:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG252eoI8JfcdrUOhc0jWz_4Xvo86HYgRFvKJ6DkuX6FuA8Eaa-HmoxU3gRqLf758EqVSuAPWvOaajfQyGPalqPGSHlJE_24e1BEwGBmiZLw9cTZhomAWynn4bfX4ZJnUlpZuCKwdVd6midvdcGWQHXEDCZLJQsj0ebr7roP65-CfyEFdsTqURMJsZPlVpCJWQfhTiZRpCmFZMAUpV2Q-BKOSgvGUp2xM1J6TVahL50tuTLsznv0_o4c3PrOskSHtUG8T8nUanvqDJTrfe9wq25QTEfEEkZsZGLS8wMQxEMFDzGPNNIfUDPVaOdsauxL0pvkGk2NipbGIo-yyw-vKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه امروز وزارت خارجه پاکستان
و زبان اردو :))
بهتر understanding
سفارت کاری یعنی dialogue and diplomacy</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4837" target="_blank">📅 12:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSooriLand</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=r7MyKiZhWmIY_qgAiUVS3iYE2z6x4wpEijfCyefYiXJgok0SYdS1j_ETiI4SjhQXpQn0phkILgy8vX2xcDCON8kTLLxlJDcfOaGCoTAXnP34fs7qi2Fc5KofrDL3SooLDts65In-Qiq9gqVYd5Nr4ioQJ19JthFYOfl7zAonKObDx4QO-7xu-3D1ESw_h7MOP64hB2b3An0aZ1fJlAetGaA8Fdvligtf9UxHBTxG8-Qg_tWftqBj9haCmGMaAIqxw8tvUbf2TTxZuk3THjKvhLnmIHDf8hhyO06lcOh0qHEKbG0dvG2-gYUDlG28Lr7oaAdNB2QpRe-U9xiT14mqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=r7MyKiZhWmIY_qgAiUVS3iYE2z6x4wpEijfCyefYiXJgok0SYdS1j_ETiI4SjhQXpQn0phkILgy8vX2xcDCON8kTLLxlJDcfOaGCoTAXnP34fs7qi2Fc5KofrDL3SooLDts65In-Qiq9gqVYd5Nr4ioQJ19JthFYOfl7zAonKObDx4QO-7xu-3D1ESw_h7MOP64hB2b3An0aZ1fJlAetGaA8Fdvligtf9UxHBTxG8-Qg_tWftqBj9haCmGMaAIqxw8tvUbf2TTxZuk3THjKvhLnmIHDf8hhyO06lcOh0qHEKbG0dvG2-gYUDlG28Lr7oaAdNB2QpRe-U9xiT14mqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
@sooriland
@sooriland
..
..
لینک یوتیوب سوریلند:
https://www.youtube.com/@SooriLand
https://www.youtube.com/@SooriLand</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4836" target="_blank">📅 11:13 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDluuCSVgD-PaDrbuYlV6UZC1QaKO-ProDwoR0YhK2VGhfXfQANlq7n8qwAC-_w_wUEgpLZ-jNMgcckW7bTDe239axs3_OYujOnxnJOYb7eCx_69V7gKBTi8xoXZSZe_FQJC9XcvQD2TdBbsoBmwGas3K4d9AcgXpeZxgVokWPNrRb_h2vqInne6q08fZskU5WJWk3OAq-D-CgBJE2dvVIUZDmIwouWqj6HeBDBMeeBlIXcEparkPzaRJn6Hva2hsGhKQ7GieDEMZI-lDjeIoLtqWF3vTjNAZbKGqyA5sh5gu68dB6_65VlxBjIHB_xfPnIXiInUDA_PAIZhvmLbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuFppSCMb0CpbIGFCQtqShNomWT5Be8sQv0pW8BIVlwiT02yLC8_eGEYwMMXhiUudJkeOYUZtadKmaYX9trrF55Ar6MUm7TVc6QgZVUCAFVpNVihlIKhqLcYK2EDFvIdO3MAGpoNIfOZBlhdzBFi173wR0jRIV1iDr9PU9EZS5JGVbIbsHf-fwspRp0xVndag548mpI6SRbiPIS6FOF3pI04fPU-XNJHMJNVvmNLzMK-AXirdrCCKvjdlNIxntGpN80LYY0-jO2A2kYBr7-pECdUxItv6dX-BVwTIjavLBwop-J6z_Or7RRaUdA03OdLOqnrjmFdFb752w11YZIv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pk7kQgigN32A3p30bRKA_te-NEe8Zq9I38tkesyENkdd42aBI3V434fEtZaEQnrjXkFTDEbRRP_RoICn0kEDYDPUnx5ngBV9xJNHXlddmGMnpCUglkyZMiyUf6HjC6ezsKtEP5G8nFxeND1Gv6wsQlsqV6e_nuQXh1oGFsTUvW0FIaCexgBpjWSkqkBmaBtfwax8WbrGwpNnJkAwtay7uEHKEVyaqSl5rdR7Sk5iRbda8-aqVf4KJYtEbzlDK-Wm1YWGM1megLxKx7_cFdkrB-bRIPfL4f6ZvlSKSMR93jaUDUEkZqmpmRsOgP-MT74I_dZVZ1INCCenz_-2RDJHIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پاکستان بمب اتم ساخت، کسی کاریش نداشت!
ترکیه موشک با برد ۶ هزار کیلومتری ساخت کسی کاریش نداره!
امارات در عرض چند سال ۴ نیروگاه بزرگ اتمی راه انداخت کسی کارش نداره!
جمهوری اسلامی اما از بس گفت و نوشت
و هزینه کرد که آمریکا رو نابود می‌کنیم،
اسرائیل رو نابود می‌کنیم
میخوایم عربستان رو بگیریم بقیع رو آباد کنیم!
دنیا علیه‌اش شد و ۳۰ سال تحریم
و رنج به مردم ایران تحمیل کرد!
اساسا این طول دادن مذاکرات، که ۲۰ ساله روی هسته‌ای و….. انجام میشه، برای جمهوری اسلامی یک برنده! یک مسیریه که عمدا انتخاب کرده که به حامیانش و به دنیا بگه : ببینید من چقدر مهم هستم آمریکا ده‌ها ساله با من مذاکره میکنه و ما حتی حاضر به دیدار رو در رو نیستیم!
و ثمره این سیاست تحمیل انواع تحریم و انزوا و فقر و فساد در کشور و سرکوب و جنگ و نابودی ایران شده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4833" target="_blank">📅 10:52 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUJQy3S0VP03KCe0sKTL0WPIC_odVl4YMZdiyYQnC9SCvalqeNOv3gnntgq5gaVw6yuyYiLAp_oQDGMRNBybE2hWuuHBqegs3OU9tblF3eWPp5-zRiBJkRYCyXpbmQBr6jLSeb1PNGkS0AWja6_W-hc5Ex4I2bUNhORFS0f0ndN92U3OUiHJc55hcFhKqbtXGv1bmLnEV0wmcAxhXR5kqXQorKVLxbFGYXrouaGZ_Ofe30X2MGHRO_y7X9INpw3WsiFazX8ssUA6a-Mc61UEKjgfCX0ZPSCzKtyVWns8U_0OBrh1kBBMeOysQ0Rz1zIV0zdmd5X_4yxMt1RzTeAFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
ادعای اکسیوس : کاخ سفید معتقد است که به توافقی با ایران درباره یک یادداشت تفاهم یک صفحه‌ای برای پایان دادن به جنگ و تعیین چارچوبی برای مذاکرات دقیق‌تر هسته‌ای نزدیک شده است.   ‏در ۴۸ ساعت آینده، آمریکا انتظار دارد پاسخ ایران را در مورد چندین نکته کلیدی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4832" target="_blank">📅 09:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
اسرائیل : تمام اورانیوم غنی شده باید از ایران خارج شود.
🚨
امارات : هرگونه مذاکره‌ با جمهوری اسلامی باید شامل رفتارهای بی‌ثبات کننده جمهوری اسلامی در منطقه و فعالیت‌های موشکی آن نیز باشد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4831" target="_blank">📅 23:42 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivsQWkjVz0ZY7m3osNU66v6lO0OeAEr_3fGuEAWBmKM7qF7WpBzt-Iozc5DFgeWBhT-sKBJX3Jy-zGLBBPM2HF7vdqN5_v2_DSmt4rvEnJZQ2e80mQf-FFzkkG5xmLVEtXmn6JOB7-qPE-vA3CR7u0MOYdZqIhz8k1rE8qVl9zAHNOinsylDf7EaL2Z1Pw-wBT-Pe-WSgG6M-sxlZfRvkwMPmXUQ5P3rJemufWYbe_MBOzyCD18rcIFt9FT1W1HZ5DTVbsWyjOIp3f_1sClP3Ols2KB8yVlDMs0_JWF6LLNFvJs26ioJggjHtpMEm3-D5lgGUb4Tillx3eMxd8atWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
در حمله اسرائیل :  عزام الحلیه پسر خلیل الحلیه، از سران ارشد گروه تروریستی حماس در غزه کشته شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4830" target="_blank">📅 22:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQH9RABnKsRYvxaxf0rX1-RpMupqrbY69p8sGfUwPGiI-HgVgINe-tbi2zjn3jaZKrTVT35uAkEUb_StraVwHjeIOPHK6Y8xuQJ5RRQGEwUEpiXlq0eqeKPjVHgdCH3lHOOmIXW6P45uRGLpaEw5tiLVa7W8lq0ifUAMbJ25A35FQvIdySuGBRtyzi54KI3v1rTeJt8n-fO97lN4PZiBi8B-ZmocC8Hc4UanUxOXg9YNXGjlmCVoR2ogxbSUVRO8gvfoW3PMIt1rpqfFKSOLpvDMqSEeh3HCFQuzkj3D_tYMb3A3ENhTvEnecxdC_PTdURGqU7-AVOXMoVacX7nEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ql5-zYC6srLNMOvRsB3G69gfwx5h2x-Q5t4f7rHNTjrABtc6Ui6AUREg2G5JhUzbGTe5qs4XaPXKlK40olMInSx3loN1AkJYi6_QXlOTWB1WCynmbbqw4agu6MDsVjTq_gqL_HX9gGiq-LjzWzo16tBePBwSqyJMWL_wtap0gUOeYOc83Y64LChLqmMMMWe9PIjsQ8CXh_VAGxK3mkBxGxrnX_PHUdEe_pYRz7VJVqqAfQclH_Zidi4d-PacOgkGIw5AIQ-ausHTwPNhwFpoiTEnby3tkxINGRMsYVrDr3VrRA87eT1SyIkgc18cZ_Tm-Gnl1GYxD_3gZUD4tg5t7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
در حمله اسرائیل :
عزام الحلیه پسر خلیل الحلیه، از سران ارشد گروه تروریستی حماس در غزه کشته شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4828" target="_blank">📅 22:44 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT1Tgl8-mpFNhV0rL9FjiO4aGdJHI6k36uvpqDRR7HtkGfZhPmx1U324K6563j95eGs8Qv11R--xIXwSEvijIw6Ek8cbDJNk54QL3jQoDOtRhFUk14Qlwz8Czo0ngjPMluDhXK8Px3Dx_LUzzcVkadXl8giqO7_EUFbtJnIaE9pjGjCY3gyUlpexly6iJr73_60hPW6QweBxLjGPdsA3GvaiwKc9cksyFukp-jkcKFgcZcRE-6paxgYKfMjK-McyCqCY1KeGbxi_hgehI6NhGUqyo6LsjtRqyflZyg6SkduOMdswrWvv8SdQSmJSyPnR4vYu_aCHgCECdMzth8mW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
درگیری شدید نیروهای حزب‌ ‌الله و ارتش اسرائیل در حاشیه رود لیتانی،
جنگنده‌های اسرائیلی نیز دست به
حملات هوایی پیاپی در این منطقه زده‌اند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4827" target="_blank">📅 21:47 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNatiACbYIDA4d5pt-hfhrk8xfqE-YqOUOvSxfowdCSL_hev9J1KFvagCEhHOk0BM_FVy4vnZGY-dfuInwN3zjhmqQYsMUaOCbD3_ftia6V2zNvBxt6jJieXw0ydcdvI80XZ37ec1mb7Mhg3rYMkFWcBcI198k0MNKNy8fA0xnhLPPWgxP0KLtBPYzorA2MEMrMB182kBiGX84JoVz8SaC8MevArhpgSo4iwikR2CLQz-7TXH1_NV91wem1Jv02hVTAsnjVSg1Oeg9KwuW7u5g9qMVKwpFf8osTNRxflBORBRm7tmhRRbBBWn0dleMAFMjzL5irMtAnrgpYFsLR5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm8d9kMGmZNvKW5DZY-4CUsCGGnOMZtInBzFoRYvyMBF3AAhTiPD8pNPuatWe2x4rkhp3af8411nBsJqN413YPwlfi4VWMc62iGFtDwj48HjJAM39ixMEAyL3J5A4bLGNck7l6V9q9AbxAUzkpo_jJAHQWGbC-A8e8rsp2jC4osTNkJRXubEG1_uVpqsrUcQjn3dHtKwqN5PKKrgDoAog66tIINq3SnqdR_uKwHp2BZZUD2_C3PJJJsIBELaqRQmTaLvNUI8fr8ieBrIkWjyQy147uS9d40IfOw7_b5rdbYV61wCiqh18_30fSpqWTtqdhRjF-J-AGW7javx2RUqEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
در جریان حمله دقایقی پیش اسرائیل به ضاحیه بیروت [بخش شیعه نشین بیروت]  «مالک بلوط» فرمانده «تیپ رضوان» گروه تروریستی حزب‌الله به همراه معاونش  و گروهی از چهره‌های نظامی ارشد  این تیپ کشته شدند.
🔺
تیپ رضوان، تیپ نخبه و قدرتمندترین بخش نیروهای نظامی حزب‌الله…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4825" target="_blank">📅 21:31 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pErM9koGVksDnurWljfhy-jyRdGzx0btFDF-qSeKYNftiZ1RkgC3v5vmrHGWpP4a9buDvhl2rO5SzahOMxBVuXqpfDoShQc4CheCFohScE1lqKs3aacomdZirnrwpSR7RdBkEk0Fgvp7Fv-cYcTZcoh4a4scmcE_wkRCZiY_nasRQkL_AJsEzN156rNgZaZfJ-509tA1vrphbBiEjCiE4YKmrNY7uN_MgnDiN-4R2JLHHID8UoyZqOv6J8wfZuZOLFIxnrXLF0F4esM7UgQheaHLBB51drbXj5tXHYgrnU5pOlOv6-U3CdPiK51rbiIKN0JSgFra73ux3uc8RgxK8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله آمریکا به یک کشتی ایرانی
در خلیج عمان
سنتکام : جنگنده آمریکایی
در خلیج عمان یک نفتکش با پرچم ایران
را که قصد شکستن محاصره دریایی
را  داشت، با شلیک چندین گلوله
به سکان کشتی متوقف کرد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4824" target="_blank">📅 21:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعد از جنگ ۱۲ روزه نوشتم بازهم یادآوری میکنم  جمهوری اسلامی در نهایت بتونه  - که بسیار بعیده - با آمریکا به یک توافق برسه،
با اسرائیل چی کار می‌خواد کنه؟
اصلا شما مگه نمیگید که اسرائیل بود
که آمریکا را به جنگ کشاند؟
تونست؟ بازهم می‌تونه!
جنگ ۱۲ روزه تنهایی اومد! ۲۵۰ روز نگذشت که دوباره اومد سراغتون!
اسرائیل «چمن زنی» خواهد کرد!
به شماها اجازه نخواهد داد قد علم کنید!
شما اصل مشکل‌تون با اسرائیله،
رفتید اسرائیل رو نابود کنید،
ولی اسرائیل داره شما رو نابود میکنه!
این مسیری که جمهوری اسلامی و اسرائیل از جنگ ۱۲ روزه وارد اون شدن،
که رویارویی مستقیم نظامی است،
این به این سادگی‌ها
به پایان نخواهد رسید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4823" target="_blank">📅 21:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJc8LlxQ7SKN-MfI5wSB4-r8JV4i8UQLxDujVsuxpjMdVT5hPA5a766ynZlqBpZCuele00vHI2PbowaYI9UTntYsCrsenoOgN38BH-WKLw7_41Q3UXU_snqjnYtEHIhLJj0Xjmji-RZcHNV8I8Ifs0B1gHCMDKOe4UQLKsFq99xJ39jo3-aocsLkaUVkgN8JKaYarUkTggjdpQrGT7s60S-sPTLeSMfy9Vam7HPi9GDasL-bzJbQQtTxMB4Yg9wKUzMfyyNGqP82e7C9CG2nmNeeOoaelHK02S3pU-8pyBYJnK7AHDUu69IKC2nsA6wBmcHxqqJC_lvVSERs0taHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
در جریان حمله دقایقی پیش اسرائیل
به ضاحیه بیروت [بخش شیعه نشین بیروت]
«مالک بلوط» فرمانده «تیپ رضوان»
گروه تروریستی حزب‌الله به همراه معاونش
و گروهی از چهره‌های نظامی ارشد
این تیپ کشته شدند.
🔺
تیپ رضوان، تیپ نخبه و قدرتمندترین بخش نیروهای نظامی حزب‌الله لبنان است.
🔺
نتانیاهو به سرعت پیامی صادر کرد
و گفت که اسرائیل دشمنانش را هر جا که باشند
پیدا و مجازات می‌کند.
🔺
از هفت اکتبر، این سومین بار است که اسرائیل فرمانده این تیپ را ترور می‌کند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4822" target="_blank">📅 21:08 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUwlCVQTjg0J594yoGYAeHnvZc7ZAjInPig1nQb5sF_--CBWyV--AV9_itKnDseqhX736HkJ9c6eRorgisO1UmnOMaBrJpju4fCOaI-K_D2DvkpU3f9OsdwcklLT1hTbrzliEfMNVwmQ7N8Pxv6oQeES6ll6iZwzHKNHdFoZQ1E8qNSlpSAjvK3FlLNQ6u1D_Ylz0zIeWi_Wi_wrSr8dlAu0Cn337Ho3987CV7eKEez6bhY7hM5dPYabxRcRVjjHCWcc5CSrHaDCEq1etl8MwZREK5wNOQbJ4HpNovrGLzWNcH6P6BLlTNM_uIYEOJ9tBULUcuo1gDIrnsuPVF7B-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «پیام صوتی» می‌فرسته :))</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4821" target="_blank">📅 19:40 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
یک مقام اسرائیلی به رویترز : از رسیدن توافق بین ترامپ و جمهوری اسلامی بی‌اطلاعیم!
خود را برای تشدید نبرد آماده می‌کنیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4820" target="_blank">📅 17:28 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2_iUua3N9b63rrUJ4dQFebvZmUvk9Vb69l6jPCFjVY0Nd1UqxXACGEIuXIBS9s6Jib7iJqcLQaqIX0QH_ahMvSAhYoxl-FfwXpsGqeRmHqTMMhU-q3OCtPNV680tIL9RnmH7_GiX85HFcRz35CsFHe-yEgbR-XP_PX3fusQe3pvxmQLkFKpFYdLKXqiKNjttCj5pbcplZeOpnjrj0-bo8Q7cxGnpBs3EwrAdIwIl8HxeotC2QIcNJZqwNMzmNnxA72BHyBmeiu_36IXA9k0q8pBEjCmVM3-_4ENKKrV9NepI9XZGAtkMIGYBDWb_UyU7ETE7B201brU7aBgdqYQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر پروپاگاندای کره شمالی
گل و گندم در دست زنان و دختران،
تفنگ در دست سرباز
و پرچم مقدس و کتاب آموزه‌های کمونیستی
در دست دو مرد. لبخند شادی و رضایت!
بگراند هم آب و برق و سد و زیر ساخت و پیشرفت و…..!  می‌دونید توی تبلیغات تلویزیون کره شمالی میگن دنیا با ما دشمنه چون نسبت به پیشرفت‌های ما حساب میکنن،
می‌دونید هنوز خبر کشته شدن خامنه‌ای منتشر نشده، فقط گفتن پسرش جانشین پر شد
(نگفتن با عیان شدن «دست خدا» )</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4819" target="_blank">📅 15:56 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kosGRKnxO09Y9u_-Bf-dAN6mRGEksOnk9OFamgOMZCEPgPNSG62Zm4XeWc0enJeEzg51c7fYFgRqgRc07154brGdCIEb0lpk8o1QrtVoJELxqm-bPy69n77Y8cfOdM6d2TThhBQoZAu3mUxkHBBojGCwieNFjnSQePf3KwQXACKgVGD7jtZ8gSBltd_vgoTqxNARJt7RWiM3MTIjL4gv0Pse3v5cw2YwfhVkKvn80lJIuIqYlIzHazBD8nVDmArEG68se5EdJZmkRRbGtSLgJDbgu8vigXr0nVNOOpybGKqHjXcZOpeoddGNcSJO9c4y6vXLULAG0WnJhpsxpnL7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lI_mhjO8R0-5vs7dcPpKURObDySkCWqnRGK8Nn5IM1KjrpNprt2M9KifNWvk990sIi_H__61Me_nOT2m1lGtiGiHr5n9yqP7mQRfMQrwJAPQyzpgSD1eC3E5hi2CBXak-awb4hzPTby0aNTpwkeb3XkQSbKCBxQu2KDT5MfeWqiyhRByEkDcIDHueaL20MEl-i0ljggSKRvJyYrYvg3xeKkRpoKwQDVX1toJUZxqvebtHoteijwGbW7dtvMPY_o-t5hHvPh3wDTnbgowH_jkwWCtV3Ie2mBPwPNVKa9QE8-w9pO-m1BbM-4ObX5ZVvHNDOxRkpVkxD_quf0t3WPP7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سخنان رهبر عزیز و  عظیم‌شان کره شمالی خطاب به ۳۰ میلیون گرسنهِ زندانی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4817" target="_blank">📅 15:50 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2mbo8ba9Xpg7mQMuXaedzyGmLfcZhZawWMVMMjmUPi5dkSe-vF0TZKotD-i39zLcpqR0QiqDJgGkGyFmQyiCs7BNvFUSCDfoyuoJVhRUT4WWH-ayS6T9ZpP-5HES4cwLJm1yLhgDL2QuYhno3y9TXpvpWplj5N7vi3MqZC1jOgSQtYdHXklnyKY75m7pAcvzS41ZN-xKVM9PBsJ5K3qbr3bMRdmw07v0iVw0RJ2jG-_34tVlpRbZYtm_zH94PZcl5wT1oVWHcjh3nd3yw0V3HxXfl5I-ePkjXzJ9SpESqeY9Mia-3iM3gJCWzIs-2jHMWnRqiR_at5Xxg_Qx5a2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ : یا توافق یا بمباران شدید
«اگر ایران بپذیرد آنچه را که بر سرش توافق شده ارائه دهد عملیات «خشم حماسی»
به پایان خواهد رسید
و محاصره تنگه هرمز نیز پایان خواهد یافت.
اما اگر موافقت نکنند، بمباران‌ها آغاز خواهد شد؛ و متأسفانه این بار در سطح
و شدتی بسیار بالاتر از قبل خواهد بود.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4816" target="_blank">📅 15:35 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgV4QbgGVIs8mwAX56A2pDbeaSTzCtQUzsEa1v7WPdNYgB7PHkmFHBIp5XxQjqzK4hpiVo1vxDfZyeBh7Me2xhN94c4zg1PLWHeibXX3nyxvRyrxjyorrpJ5Xgfy-X9pSCwLlea9F0gTzjjaZ7f2t3qc1b8ZmsTmwQLPKRm-pd4Kltr03U5CotxzJRqWfbpeMJDKEQn2IjQ6-x-l8MPm7LC5CSVcn0qctP4NNQD-kJ7uiESnzIEIVzwbPAGTWfbl1_PyQWdh3U3Nu_bqXCtFUAAlUJScClzppalsQU79ZFAQIbd7OqjtLEwzDibVzewv-zz4Nt--sZVf--2oLcE60w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سقوط ۱۲ درصدی قیمت نفت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4815" target="_blank">📅 14:29 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3_-5byseTo3dbVS9LLpkD1CCUdKIYiCfBPRRCAyDXZlQS7NvwUApfvvFCXrPydrhfGj6rgN9ghZiv5eBQdwQDR0TttZaAU_8xcjXfooVUX7d8BSGXqiktnu6AKxBtiZRlbG2Kp3IqHWga5pzCSMddgknO5Ns1xgq33twEEuZQpNtIyoLwK3ylrCsPKHPy3_ujAWRsD6v4IIy07d55qa16yiAaPHNNIc2iEZZ0QO84qWQGeQn3yIhmV__T-VRxcn3IlmuVLxyrhh2ogQNqetUU37vXOKVU1n7qIcjRsOboO11_CFlf8IhlRryXSRUiVKRZKUj2cRvdqMV49kjEzngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4814" target="_blank">📅 13:56 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRpSJHS095sjSobOKirzGYGKrqUC8_CHof0JDK0Awi-IxBa8mrKeY9bLSGLfQaglem1WC0Zv2SCp470WABRjmF9-LnoJ5_2ozyiFJio4MnnpuUjYjpxrQ7onV0pZc8FPNEPyuUo419lnNYHiRGcjiZqVUxW2oBzisyFqIBM800F9Hk-SH4eeEYKVZJ6DbxMC-VdiqEKphAvfrejA70YQObZLDHrQgi83ICFn6CYkynFVJsSA7q3hnvPUcL5M5mIbR-4gDSusJmN06EjdYK0OTO96tMK2X3kNltLxU5BUzn973PmcGi9ZocWY2K1L7a-Eg8fMplildXed0i4VlzZ-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4813" target="_blank">📅 13:51 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
