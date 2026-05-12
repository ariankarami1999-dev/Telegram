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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 14:59:35</div>
<hr>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfId6hOwL6O1Oj1QYlVXwGQSiDirdWr9w77D_tcM8GqPoE97IQ9GhYITms4cyf5Hn9aevyc_0ZusR9A9Wk4W9oT4viPgNhMi1fUI5rU5czYwrLH3fRkiMMPghgry5maMg5uL01IopSAW817tAi43_upqEC14wzagkQk6OLm66Vg2C1xZfU_L01lBfD-qLBqObgBOZkytbAzhYjUd4Z0Ro4BDfltrptXi8DODRsCt86bWvvw6O5F3dOu8JmMq5qEqnlsczMt09nVS8opCNu9iXwRQ8nRicInlLTTlqRdDuVnwDH_UXf5EJqPuoUCSgu8obUlLpjElORWJQUN-Ucx5Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj4Gwb6nVMM0pAWc5h0CyM5pdgLUduCx690xp9x-seOD8_5FroI_OF-CXkbUOtcH8ND6ZvC1N1VqRdPZs-CSUmd4LFkZaMv2sfis7Gkh863-k2WTOqwnQ1kIbGWJ-lrVBzWDqPVxfbw9lYPObF1TAQimIVKK-kl-OkdP1fGi0_jcIhSV906qVnyiP-gnOG7k_WmyzXFA4eHuo6nRoe7TVOq4M3zs6BxTx5O2Gnb_u00j3H-eIQ5MKRZ8iy8WUenBhl9GsdSjfyFJ2MUl5toSN_RW-MhnIbhZ5TJJXCuuzonhcG23Bs0C5uThDs6-5GVa6ZDnLzpg6TRN2EDO9uCYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwEgQmHuEJ6lFE3RRyBu1dZL95-pe36yfFv7ztIadQDzBgM-GfHrutfWAfgjZK5LDhv4HgnUJ06fQdgBzPaV2EOIUQ8oRaRBB-rggorlTVfxRyt7P_NsWayPYh5g6WpQihRS-5ufwrqfxDi7zuguGd314_Fd0pKv0cU07-fxN3utKR6sjePpMxXTfSKnQhUhyLKg4bRR-M7JadPHUysoCcjiSNqbYwX6hTx2DqAltS1QjHICq00E0YbGRdpbMVYfV2jtl0_XCt-6z-UWJtQRhkPAUATaRRPsUexz8w72x_Sh-adYja86n5f-ZGkMJ7_HapT4JR782udiIi0IeJPqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpUP6V90yomMQhME74ueuebPIR0unZpQiM0rg75s1hQnHaW7AMogaAyv-vQVG8AXF03Vieh8nQTVR0a2jePlU5CiLcda9f2Kwy7dlJwNRt5gOBujt6j9vNSC3ZzKOF4IEE3FlqCLQ852BGQjLaCxc967dZl7XKEm-G_oycMMP4Vjb-r6rVVTlOOcT7CP8rvFYEebqsuc-ap2nsgAccx8V4FUb5i4BygvH4eBJcU2cPEB6IzwLo2fWTZyHy0hdisVsjJPTDzyr6HDr3Tf75UdtLFY4HnJmUiTi0TrjD0E0QLzl3cmQnDMWHR0cdhGm7_dyerFl664ekjgHiwB7z-6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ5Kdq1zan39xFl5hleFM1rPS0oU3dVhCMAXbPrGfKe8g1Y0cqY03nhUnLgQFHmrbAU0uI6uL0bwTvh12CpSzRnkesppJoPR07OHCsICW2SQBedJMQse6ks8AgIbD4qD8thumslUNgpOGwvVNzIaLG5yF5WCyTLSoNsrOaX4s8Sx5LQnHc9lTJq2txP7H0yl22JBtfclkwXlM-MgT8WQUm1okiiMl7n-Cr_tP7aEQZe791pbHjdn9xF8hZ4E0G1tl8eIFLGBrWJlc8n1Oma64rAUZ9v2AO0Dv1Ua8rQGOqBZDhoWv7S0gmjbDF71ldd18PpMo4i6S0b-raix33FpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-QsSBOkCBK7uHleHPEC5T6859aKDfkqDvCyx1N0XDj_79OE2A0guMixF4UHVzU8t_N7BKzOMfc5DiTu5urS8FzNzoko90qOcgvCYwxfe0jRzdDdu3fyA5meetZJ5CkwxnLbBXx0jQvLDTOob4lb4jyMTgvjgGU_yNzBD4uCNruX-GAPL6hhY2_7KsDqDKH4K3-0nnQpxKdis7MH--jMi8J3p_FqIdZ27WZ5JSzK8Rde_kUaFHYIUmvJYD2TP9j-oYJemfN_UF4Msxjf2TJFS0DdoiIxMPaAr1NH3HdlF0L_ttjBCRGxTTizus8cgGs8TJHDw4afwinMpzA4ENMfzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_LEmggzaHLx0TNM5alPgflcG1Qf0BvdT6zAKECiPhNiLPneQ6okTDU82_0gEf_qumEN15_z7W1xHNXXxXWXwG-HK7QhOOR-R9injg6SsZ86LzHDUlx1GRHO503yKuR0UlUAMZstq97qPqRwktzcb7GgycGk9RS7dcSuimvjFP4dupXCXbPJY9Gnnd1Kts4cO2lAvemPyxgHRyd-_QTa-JrPcwPx3edRmjBR5Bk83T-aLnbFdjwvwPYi1cNOsvEj00LcN_H2RGTqjmctAq05xH08CPYVZfuRtaY9kHLHQqLz3O9hqzq8GBGnh0DkK8q6PeysZVTwHF1rkmZuQ4xwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXBdZWHZuR78_mK5ygaGxtsZRH0UCXmLDJeVXDJgDnB0et7EWFtfQ1APt8Z0yKfIHFkYjU75L7EWwmzb34lZpjY3rCm8Mb4dpc_IWFyZVFhU_e7P7Xu8-3AuP_o6iYrOIkF1X6ctzMkAQHRppF_8Cgp0NYk4r_eIspze9lm0nB3fX3rdU1yNmQV0LgSPrS9uCDC06sI9XkcPsgLdRwulPvibYaxcNNnJOJixCunViJsvect0Rkh3Gwtb4mFAtMZtjQzg1c0xt8fuDPk9MagUBQzYMaMXE7KfwWUnQJHwcaG5WyVfMCh6_mfYSJI2zOQi5OjEleKarM5MasV77_KLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اعدام «عرفان شکورزاده» با اتهام «همکاری با سازمان اطلاعات مرکزی آمریکا (سیا) و موساد» خبر داد؛ اعدامی که در ادامه موج فزاینده اجرای احکام مرگ در ایران پس از آغاز آتش‌بس میان جمهوری اسلامی، آمریکا و اسراییل انجام شده است.
لعنت به جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4904" target="_blank">📅 10:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk0dD6IFf2CCZI9Ra59_yh_H5UcVcvSQCHRUSnALKy2uWzDH_XZVpt-omgXq_6Z1G6LgPf4S80fClZHXUSiLwX6PDMJYokYnzE5zjI8u-_DUYy8ivhaokZi0lxI9DruWcDaJvGQHa7rw_7FBOmx63EG72wLhRaRQApHVELgVJ3R2GQPOVbexat6gHOzeKzccHkxNCVIrrHR4LLz6cPWUhwrc92gdDhsdC2QBXtDydkbkFDruBC852vWLgNbo3xy37mSa3T-RWhHd4t3asAcfemue7-P3lpoS-izeqHZ_-IQW7BbfyR7v5W--SP3Wl2qfAbkQRgkI9pPqFSMFCVZAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس :  پاسخ اخیر ج‌ا را دوست نداشتم. کافی نبود!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4903" target="_blank">📅 23:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پاکستانی‌ها ۴-۵ ساعت پیش طرح پیشنهادی جمهوری اسلامی رو تحویل آمریکا داده بودن.  مشخصه که ترامپ از طرح جمهوری اسلامی راضی نیست.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4902" target="_blank">📅 23:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پاکستان طرح را برای آمریکا ارسال کرد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4901" target="_blank">📅 21:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4900" target="_blank">📅 21:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX360knnIfCBrSG98xKWbgFdlWw6G1DIF9MvH--JhvaUJ0QMhrKcr3YtatlT40N0pqnTYDvyfhzkADoCNLWe1cTU4O7rkkFWv_1MZSXHFtTl_-z0XLPrF1HRjs1cXAAAaiz1A7Uu-IPEyQCDp-BZJPAcnpKYKVBTpf0JOrQwYgYK0m1_AXed82h0kYqeMXbs8TNEnL2gR-WfqY7TeayEhSHYBnxUfJCYh0qxEpLn58GlsJkGm9c7I662H0VDOrvnfo8CDizcudcHYwSOppAcTApSBY3WvYqEWAvrYIRCSCDOK-jUX5dhvLLxWBTpsuAPD1PfVy0WBRtz6U111D6dFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4899" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/4898" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jfi9cCpVdpdjqM1mH4FnraKBQtdYvN3NmflUR4Q1kZPVSutpHWhZ2ieH2-YADdpAvtXKk-nhCoQ9R9jtqOccpq3nyRXDkMkW1GWFJPiMB5RNTYCBOceYuB8-waNHEL5bZvajp-zoiAAbNUKboAt4bskWVqPpZVZAigVmtVTSLsYZ-pKpidcE2yRfv8U7A0RMulkNQtT-ehvWKv1Oszs7b_JJlpvxc97IZAlrTz6a62c_6jJeKRc5ciYXzz3pybmCBp7cBdyvJSOcryxVeF86JAugZy8F2PwqhsS4tlYrH1U4GwZ1do2lSCK7O9LZweP7uVhZt43fBxrkBg6qUSNQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5PBVGiCWxT1NZ603E-lWiHvR7zCWaVnFhyN0srRCe8O0032Vo8zC09LOdhVnG4kA5ctNfW30324p63FGVcIbaYl2TOXNYKN2bY_dmyc37keH9VgiGY4p6Ea7s5L2oddCqvTTbpkCr2sM3Ie-gPsFNr0uQpnlWmcWXHBNZv5389kLN77ciJVq3IAD0g_v26F2CsLUE99MKk_gmuv7JwBageEHYd4I-aHICnNsBib7cJSPXKmlyT5SSo_Q50vrjP9DFNaubJ6wxrmciTkT9KfG5FnARXKNNy4PFMDEQLrPyEnHwPNT9D3KnmY-oKueqPBItwF00voxLEvfXLTARPjOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی :
‏مقامات فرانسوی اعلام کردند که ناو اعزامی آنها ماموریت مین زدایی و اسکورت کشتی ها پس از بازگشت آرامش را برعهده دارد. به آنان متذکر می شویم که چه در زمان جنگ و چه در زمان صلح، صرفا جمهوری اسلامی ایران می تواند امنیت را در این تنگه برقرار کند و به هیچ کشوری اجازه نخواهد داد در این قبیل امور دخالت کند.
‏بر این اساس، خاطرنشان می شود حضور ناوهای فرانسوی و انگلیسی و یا هر کشور دیگری برای همراهی احتمالی با اقدامات غیرقانونی و خلاف حقوق بین الملل آمریکا در تنگه هرمز، با پاسخ قاطع و فوری نیروهای مسلح جمهوری اسلامی ایران مواجه خواهد  شد. از اینرو، به آن‌ها موکدا توصیه می شود اوضاع را پیچیده تر نکنند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4896" target="_blank">📅 18:37 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126410d252.mp4?token=bcum7zVG7XoPt2Or_RyFEpE8a5xRtvrln02Sz69eoFXAeVGp4duxsDjqh-JoFvyGz-FcP1zSnD2VIEBvxiZZhtH9XG9ZAmBASYzblklFQSk_wY8gYMY2atsZUnwAZieZ4wsYnyOwQsK46Wi8Ct8vB3a7SrPhVfQiPjtl7Hmig29AAFHAexJ0C3IfXgk0ZaztSQi1pdORRB1OGa4Ytlonsn4UwVrqU9rK86LJVq_FQizdmkDMGoYixUh-yryUTK3syHrRhlVKRHZj3qTyU5iN9-ISqbxCFCOrWwjB9KXEx2F_pU6-d0_T0-cBge4IJ26FuUA0h6y2sxmMs0y7Aj9q-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126410d252.mp4?token=bcum7zVG7XoPt2Or_RyFEpE8a5xRtvrln02Sz69eoFXAeVGp4duxsDjqh-JoFvyGz-FcP1zSnD2VIEBvxiZZhtH9XG9ZAmBASYzblklFQSk_wY8gYMY2atsZUnwAZieZ4wsYnyOwQsK46Wi8Ct8vB3a7SrPhVfQiPjtl7Hmig29AAFHAexJ0C3IfXgk0ZaztSQi1pdORRB1OGa4Ytlonsn4UwVrqU9rK86LJVq_FQizdmkDMGoYixUh-yryUTK3syHrRhlVKRHZj3qTyU5iN9-ISqbxCFCOrWwjB9KXEx2F_pU6-d0_T0-cBge4IJ26FuUA0h6y2sxmMs0y7Aj9q-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رهبران آنها رفته‌اند، تیم A رفته است، تیم B رفته است و احتمالاً تیم C هم رفته است.
‏ما با افرادی سر و کار داریم که قدرت خاصی دارند. خیلی جالبه
توافق می‌کنند و آن را زیر پا می‌گذارند
و دوباره توافق می‌کنن و زیر پا می‌گذارن.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/4895" target="_blank">📅 18:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
🚨
نتانیاهو در گفتگو با ۶۰ دقیقه :
جنگ با ایران تمام نشده است زیرا هنوز اورانیوم غنی‌شده‌ای وجود دارد که باید از ایران خارج شود.
هنوز سایت‌های غنی‌سازی وجود دارند که باید برچیده شوند. هنوز گروه‌های نیابتی مورد حمایت و موشک‌های بالستیکی وجود دارند که می‌خواهند تولید کنند.
ما مقدار زیادی از آن را تخریب کردیم، اما هنوز کارهایی برای انجام دادن وجود دارد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4894" target="_blank">📅 18:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
‏ترامپ: «ما هر سه رده رهبری در ایران را از بین برده‌ایم.
ما ممکن است دو هفته دیگر به اقدام نظامی علیه ایران ادامه دهیم و به هر یک از اهداف تعیین شده حمله کنیم.
ما اهداف خاصی داریم که قصد داشتیم در ایران به آنها دست یابیم و ممکن است تاکنون حدود ۷۰٪ از آنها را محقق کرده باشیم.»
‏ترامپ درباره اورانیوم غنی‌شده در ایران گفت: ما بالاخره به آن دست پیدا می‌کنیم، ما آنجا را تحت نظارت داریم. همه‌چیز تحت نظر است. اگر کسی به آن محل نزدیک شود، خبردار می‌شویم و نابودش می‌کنیم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4893" target="_blank">📅 18:09 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد  ایرنا :«بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.» [و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4892" target="_blank">📅 17:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
از طریق پاکستان: پاسخ جمهوری اسلامی به متن پیشنهادی آمریکا ارسال شد
ایرنا :«بر اساس طرح پیشنهادی،
در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود
.»
[و‌ نه هسته‌ای و اوانیوم و…]</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4891" target="_blank">📅 16:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZa5DOEm0UF1IVSwDI6Al1_lFPxf2bx8fHWTZF-N7lU41DNxeCWeq8XPsgDe4A428LFL9ogHLC3ZUUIcLgl5Qsl3490FrCtCjT9UePlRQxfSRnXRrSiG40ZEWtba98tHvxJ0MF8AmgZ-ibnZVsSL3kOE6yOeeYJorKBBDN_em41JNfA4I34hIPyh1rGptBdU8qvQB_aOgzZQQ0cHpnJxfIGrhnsXy0QIFSRcnKIGab4ow30OIXOLEYkMTIkXE18sUc00OsvD2SKImcb1gSCzQ6KCEvMFA_X8IP7HghNKo6pcgyyRaNxt-qJ4HXduByO-8omjNqwWGgakmnBE4Btn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4890" target="_blank">📅 15:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
وزارت دفاع امارات : حمله با دو پهپاد به امارات و دفع آنها</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4889" target="_blank">📅 14:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4888" target="_blank">📅 13:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‏وزارت دفاع قطر: یک کشتی باری در آب‌های سرزمینی این کشور در شمال شرقی بندر مسیعید، صبح امروز هدف حمله پهپادی قرار گرفت.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4887" target="_blank">📅 13:14 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bebsD2c09qWbpi9mKZEHntXhCY8dQOCDNolMMnSsl-T8kOH65eIjBub0nPOctuYuKgWJBexqYY2EPtE-nwlrB13A8YbU-e7gVKPWXp0quXSfBxW7Sp30LhtwM5myx59b7e9u3uxY-yMEgx_a_Y8905CatA1SzMwU1I5yCvRmOokB9ECbfOXnQUdBngqW6y56sH3zUf-uI2lw74DAzoaOdPcU6CXbLLC9wbkbcIsNsiFfkGv6P4UiOf-EJbBUZxaE31yzCMEL8RQWPcYzmoLkWlWEcO752tkPit8SPJITCpsyvdT7unCXJGK8CJ05xaSj3OCZq5pmk8YwlGPbkFdhVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4884" target="_blank">📅 10:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏ایسنا - فرمانده نیروی هوافضای سپاه: موشک‌ها و پهپادهای هوافضا بر دشمن قفل شده و منتظر فرمان شلیک هستیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4883" target="_blank">📅 23:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctQdlOJ7wd2K-F4bPT-_7HkIRn8Q2sboV1kNwNG_GQbJLETlvuwC0XHkOJTutIqI7Lk7rOtd4ofYSmtwxdF-QvpMMft9iH0tBxMCHVjfp-BcPaXk_18NCpt0uzUxpA9-erhIbjGsgyuIWyd_g_0QjSvYqy_V82CfAMpieeL5cfwprRQtZG7cKBgxRq6mId_03LziqW-FNfieot3JOCUvUL_fG6WOmXO4QnFdhELzghX5KSOSvUTF8Xg4pVePnRXGuBnWteJfNCYr237uUz7waOhkA9mCzQr2CTrLRW2chFIATpEWYbBkdZ-oPTwTYOfZe8ssLaKfgEePh1kAA_E_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/4882" target="_blank">📅 22:35 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmz9n87p4uT51cGBZ7m7i1qRqXD-aky4ZJEDLsfIYNUVKHYdH4xaP19HjrEZrE7Lnl9L0Zyg3IstSiUFGenGas00716_0rZjDRSjDu90EW_mz-2ZWKblQca8sX-sPMPIWO-YRJE4aQRnIpQFYWHYtyuhe3s7c4io_aVQJbkqA3ECst7jPvM6vSazT8y9vxAwGiupzm3VVhxCTjY0DR0LMxX5QE-f-cW5kIkllfwMWSdLEbjw8ye22i-hfdtIIa_Rb7f53rGNWBGYluQaUlA4m8y-zHK5dmdDiWzL0ucBbPZITI5EbqK_LdhBmJqt8U9p3z0hUWLXKTSGfQ23OreDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
https://iranintl.com/202605091828</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4881" target="_blank">📅 16:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Dj3QrlOrHXUbYLTiJjOKOzM7WZ9Ma040zt1FvbtEBNcWeQkOY9pVaHw7dXmVQCNxOcjIegqEE3smTdxWXKD3eBRwlnPpQcu08pOKBur-iz_Z7YjPDkCCdVX3BOGttNw3HsO8FIJXioSQ6TvvAQzd470WMCwI2488D4vQ_-utgvke5Ki9eTTqp34-zo3ywkzWLzzXd3H2v50ie488S8epqsrqN90yYN87SeMR0I0oueVJmkh8i4azPSeCUf0T4jfqBqNMWBzotQEQHemf7W3SzCwgmp6O-RJF6xqO1pKKHOF0vl_DmxbJX4CR3RBH5mTl6ehbnyGC-Dy1-E0qPGow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مارکو روبیو : ما در خصوص لبنان فقط با دولت لبنان مذاکره می‌کنیم. لبنان ربطی به جمهوری اسلامی نداره.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/4879" target="_blank">📅 19:12 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjPLuxiPhNwA1ZIiI-oN06ZbY6RVaJd8u2OmZ1JL7ctcR-eWKI4MXv2dMsky5dndjPIbIIdMLv2QpHsVcKgkwdNuCoAuOhmBuB9U4EWPdllxokJsLmGBG9yEuZ-D80FcMVey97AR64i8MzoTB8_8haV1tt05ARXVsQTYY9HeOh3ujguaUawJVhmqaajlwGZE5CSotzcQ70FejFwA0x3Jp8o127QCW8P53po3j-vwaMGoEE_N9T6ZBj7mT2hcje-JgpNbbKkisL3sRZtBN-NuRhq5BQ6rv_0lPOeIASmVzG5LTlOqm9VzkeCSyqRRddYNF11vHCdsE1wa0lxKjYchoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4877" target="_blank">📅 18:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
🚨
🚨
🚨
خبرگزاری فارس:
وقوع درگیری‌های پراکنده در تنگهٔ هرمز
‏از ساعتی پیش درگیری‌های پراکنده‌ای میان نیروهای مسلح جمهوری اسلامی و شناورهای آمریکایی‌ در محدودهٔ تنگهٔ هرمز در جریان است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4876" target="_blank">📅 17:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مارکو روبیو : «انتظار داریم که جمهوری اسلامی امروز پاسخ پیشنهاد توافق را بدهد و امیدوارم که جدی باشند.»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4875" target="_blank">📅 17:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1pnwgQB21uvW8Oy73oujEOvdtuka8UrCPEQeHoKbnTYLf6Nd0c6Zxny1lj58yKeCZH3LNWUAZBZGue2wZ04Z045n9-QQmH4AxfLiiucIE3yBlb3h8aBrq92obG5xLZzED47TGVj9koTq8KPX3HmTPQ0tVAqwdis3q-jJPb2-5F9BESlshzpw4hD_VOJ14z7wzllCFw_K3BoPiSfg9NDZBbo0ddQNL8mdqOzK6dga8T7ZvggyU2UIZXYtBJfUuM3fvG10cSFpVhyC-6lTVG--_Pkht4b_10pdU31CG87P6TdtbIv6yPdN-NXDCdBDAr7_3TjDRCWyp0HLit8Z3AXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یه هفته وقت داریم که بزنیم
زیر آتش‌بس و شهر رو بهم‌ بریزیم»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4874" target="_blank">📅 17:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2B8xzaLVOzZR81_jB4aiVzb7WEFH72ViG9Hq10uMwf93qRatYy2ZmeEAIMUd_D3SWI-X_qiS1IuTXmZ1migVXUSnxL06geCK98nMYaed50dbVr_0_sbG_VgTbXH7i0ufnn_fmLRbKN_6cfZtspFeV2XfujzWd_vPaBXQksIFcHCMIAoKAoqRRuHwrAEk97gFEPtZrckY3uo_X-9BWGeCP93xNbjeAV7xPUIDDkLLVdWwWPUTzPSKSfq87_Yon5X-hXLguhhomVwAAdFhSuicvpNTDpClFpshZyre4ODWV5ve4sBehkDdG8b1n2HtLyDSZ_n3QU8tlfFW3LLatj7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور ۱۳۶۱ !
در بحبوحه جنگ عراق :
وقتی می‌گوییم اسرائیل را میخواهیم نابود کنیم، خب آمریکا به ما سلاح نمی‌دهد!
جنگ با عراق، مقدمه جنگ با اسرائیله
و با تمام مستکبران عالم!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4873" target="_blank">📅 15:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_VfdaI3Ipbid0IMlMinxIjYBwS6ksUGf4-DMdoXM0xtLCxTbZroj4bQ-10o0AtOhY84_FVYvmIi7I9U-3-RZLNLMht52HBpIb4_7ryqIcv89zJmYEI7-XEkuo1au1FpHUYqKRyFPiDAHBRt2PjXQB8HYOSj1OFciQqBXzBsubvibz_2P7tZ7Ch1LpfK7tfjVtEAHtJnrYr2oKyCwmQxJ0NHT0tEoePFcFZBt9Tuv7NThpjj_piQuLKl2_ivE7zITN_mu6JLloso3rGXczdCKtbtTLY-g8ZWoaUOEjiMVjpOqcYqUlj7AJsGyhYbykFYWy1G0f_wWBAecBXMzC9S3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون ….. حمله با موشک و پهپاد
به امارات</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4872" target="_blank">📅 14:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWlq1X3q9AG_Gwhltr3LKTziCXzVUGut-uP1OzntHGOK7_LkoeBCmPANHquExrkzOJTcqGZxs-MIhETyi9CQHQgS_5wDshx1sHh-f3yLrQ3lxxa4EmEIyK8wXHaePtmB4OtlSLL8XniaQ3i7CU2yE5KTtMNhBWquiZ-pdE6ogx71NR8OvqCtUkyHcWdP_1bieLLYIwkx4YOvefT_wtjxLoOvZ1IQc-qifgHTbXlx01pE62fxpZk6KBFLyyoVjK12Flc9M-qMSI2uvYgafqB_Si9aD45Xi-w9BZLdxspXL7CvTXwAwXEiEViIX6UN312VA_mJVcaxm-4Xnt0X7nLc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروپاگاندای کره شمالی
برای بچه مدرسه ای‌ها،
این ور موشک، اون ور موشک.
بالا : «رهبر ما شماره یکه!»
می‌دونستید جمهوری اسلامی
ساخت موشک رو از کره شمالی یاد گرفت؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4871" target="_blank">📅 14:51 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
جمهوری اسلامی میگه یک نفتکش رو توقیف کرده.
احتمالا متعلق به کره‌جنوبی است.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4870" target="_blank">📅 14:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
رئیس جمهور مصر به امارات رفت،  یک اسکادران [ ۱۲ فروند] جنگنده پیشرفته رافال  نیروی هوایی مصر را برای حفاظت  از امارات در این کشور مستقر کرد  (همراه با خلبانان مصری).  رئیس جمهور مصر گفت :  «هر چیزی که امارات رو تحت تأثیر قرار بده، مصر را  هم تحت تأثیر…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4869" target="_blank">📅 12:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW9C0l1E53lNmSJz78KUZPEJv3xAY5V0RIazefwEncLwR0QW0QJmDeycTKRF4gZ2kf2LNUZEIaxkv0ltaYKp-W1mR4Dui9JbNYy1Uspsjj7WJPDU2UZq6i6dJ3E3TleSRC9Fh86phiO9-JXJKaZHiirOIWUOynL-linsQlkMKb-Km8Czk-nNAZY-CwUXEEXK2HDS_-tmLV4-5Jat96Zn5wdHxE9bma70wurjJK2nnemH9y2Hcn5WLqOCKp8rd1JiU28cYz_XLwlhFpKOkHP_ao60xDXVvqg42nevkXHqfiu_cr7NnPdHcnyOEOUQrtEIpC67-i4pHn8BUqqCOLlXXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMP6XOpC12YAUkRCINN2j033pcJbAq_RiQRWp2U9DX_D-PNF7b1u-POFf_pgiBcib2sIaP8snopR3Zj_HwLdcdSFSU6LvPph-F2xfDLqHHZuhdsmNPMyBDBP4GbQR_zl9aH76DDJslR35AHEZGn2aZ45u1Bjb2b_OoJtwg96k2v9RdVTsfLjW3qiLGGUrcqa99j40MP74nzo_TI04hwoaeT-zmhUnIfUsqqpcbWrG4JD53-VaRAxNJ1zVdq9pklU0Xal21ZKsDjsKmUtpcsDszI0YD72ENRioQbk96hP9Mb6EKlmWm_k1dMRrFm1MY5_kzCQrYwTqRHDSymzBlRgkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=AAyTj9qwDYyPETEzxbri0J6MTjs_TWpYyIYmgxq2w5Yngsq2aj12Hlepbm_i5F-FEHuMAUM1bf-phbbPMEv0BilHw86dW26xq22XCFOqz35EdyEAvlrCNlECa_S9T4s3aYrBPYNAhR8iGhKrVAoRRmZ5oCBbttKFw2Y8UioUsqSjGYupvQ55NpXWt-TXmLEfnyeIlTwV3lXCpiJPAgCQOYuYswV2lhRJYPYzNoWiJoOf_xueJs3yC-EyJvA_uhvuGNGtfZqeJf8VMFGMFqIp-inp5RHY0dTWpVON_vV6xOXe4SYOt1d4paxJbaD-JXmxTa0Q1xr_2gJsYWZbUlV4uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=AAyTj9qwDYyPETEzxbri0J6MTjs_TWpYyIYmgxq2w5Yngsq2aj12Hlepbm_i5F-FEHuMAUM1bf-phbbPMEv0BilHw86dW26xq22XCFOqz35EdyEAvlrCNlECa_S9T4s3aYrBPYNAhR8iGhKrVAoRRmZ5oCBbttKFw2Y8UioUsqSjGYupvQ55NpXWt-TXmLEfnyeIlTwV3lXCpiJPAgCQOYuYswV2lhRJYPYzNoWiJoOf_xueJs3yC-EyJvA_uhvuGNGtfZqeJf8VMFGMFqIp-inp5RHY0dTWpVON_vV6xOXe4SYOt1d4paxJbaD-JXmxTa0Q1xr_2gJsYWZbUlV4uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4866" target="_blank">📅 12:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqQqN2TUSIJiKOBGmhfupyPhN9qr6eyeIPK6JgEl1v6O5SAHZw2k63jXUmF_uOV7BjNpIQ-G-jdPrbJfdHJeEtVm2gKcoRv7U8oZ47BrmSdY8sHdFGqb8aG4Nnf6GlukkGpGikIUZ3QGnFqk_YRqAo_-wFRGJP9c6hxgRp5DTkjVJSVIdY_uKafkx0y5YF5wsZ3TJ53EEVFpUFA0RWmNtuXt88slK2fYDB0eJRLZWNjYxwYT0CQnywc6HrobdORZbaSE0kArfXpyh57tNzYz1gh3I3rBcI8iGmbR5slnIIcgHf_fkGxrKjYH-6ZvIx7oJupsISOiCFfSWrsmOaPmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KgAVoTvPxDTmc1sONy7Io8kxC2I_4MvRVKiSA-dLOWuYsuq_kBvubQ2dj2iaZFue9XyosVukLnkpNAC4ve3xdhXDIp5c-v0BK1QxqvE1O_rqU86D8QHxNPf7oy-ZAxfBtQ4pPuRbxnFDnZJrboMJ3Cbj2aoKTgRLqn3gCpuZ1j3M_UZPz2Ttnk7lTkHs3J9FoIBsEnH1ZsEcKQzYZ79le3kyBxXaQ3uo_-5dfycfUFJplzssxVKZXo-B_QYub7Le6KcejlQdVOMLhtJuipl15sZzSaJJa64Ho8BXJJ9wW-fTOUEe_RuCpCWNy_W3xQ8E7wbRy1XaGsSrWUbDOibC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMQBpaBE9jaWsd-JJPQVIhAhYlQ4Jk2RRgTs7nvQbYjGL475ggmsY72COC5ZUSuOtuS_p6EtD1mgCSPpBwKgTtIpeexszBFNFez51tgMr5vjYZvJmGLnaJOReNXoF859j_1SowXbFXL3Io7UAhKYzMcEqc8sIZOVJBUY8_Cxn5Tjf_MGNWQY22jzqB1hbkFvySajCmKjMVLM3djOQnoX0WAAu6_y-ia60LAZ5eWdryZyz5FhbPfzum_UlOmZWGtAlPDPjdYPRfqQKWVfeaHoA_lgw_wmhW3shwFolMwXEecGrgD-YsrRu3AdSM6XywPxaZVg3pxnm0hHFeBFDjYwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-z1xu0sdqM4Ny9xELh4eOThyGKokInS-d76JhHNHP44z4xgFD4yrcP0xNhg91d0TAoZzKFfhKa13sA9aN3h6fn0j6nRjqDc3tdb9HCDtQLGPKkmbijz8KlNH5u-qMopRm5GtvJaXC-mRvQlMAS3uR-lTfF-FwXXU69Jvxs778YeA1BgWgc9x1QeRxRfZxlhiALjziJJ34dZc5g-M0j_3qJMEX5JZyb38ruu_7zFyDSwEsxa4vOvOovGN6TSEQlQBwW-_nMdeCjANW3U4If2RTHMWHTE_uK_FlaGoedqMUF4NIcnJ4oJn19ZJ2wwMB6Yf8Cv4Kn4T-rFH3rfK5wiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKKqLgKBHybBFao_bx3PYkQkUqC34EHnlYaiJxfmrTRQZNpIquxZf4iFh_G-mMc6q3vGiL1WSJJu7PcvcPL7P3ElvLCkI3UoCPKDd2qUefllfEY2Qz-fh0ZhEp65r9FLfbmR0a2hZGIEnxr9h4CUl70e1R-bpn_tU0_XXFL_p75XOyOK6NhfmWNuvuDG__OoQ-X1Gz3s_6xcXeElzbBRNrl7dsiwTjXKttUPX5d2cArfdrAiE5o02VxeF8sZKfJG_hrEM-hxcV1NvQo4jNJmGR_y35hNQeAYHLoaey01t-_XfuL8to-qsPcBBkD_zckNc7JUMi4AJLK27GKviLQ4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSwimKwevzmkxvFgj0TpsM8VyriHNlu2xqXX-ns9GSHoB05eAZQi76Qak8qQL4huFpB4BruuiOPbg8NmdNAZ78CJzVW0j99sLyid_TMxCLuzir5FBR6YyFs8ZehRYMm8UkkmPLdSpNWQWAQBSKUmSnfJ48Zyj6nkACDVhttS4fYjUo1PB3Lg_F3_nOT1zr5LBMstuh0nUJ_BkJUmvz9Qa8wA6N2ansZNlkpKYCiUVGuW14LJ3KjgRnmeKpIr6BTRuvqxwpf-EAqDWbuxFY8K6g-hWyciO55tF1cGHKCNVxDhWao5wc6_Xv7nKDLVMyeTqLCc0BSfKznoR0reReHQwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">موج تبلیغات حکومتی‌ها علیه امارات
اینها از اسرائیل بدشون میاد، چون اسرائیل به کشورهای کوچیک همسایه اش حمله میکنه و به خاک اونها نظر داره.
اینها ندارن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4860" target="_blank">📅 12:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3HyFerFuCpDbcSneLjhquf7onLJ7-8qCZGrRm9H5FTlyrhURSkqWU889IqDpBv7CyKNKbMBOS9fIgaeV0bVLIbt-IsqUw5qQr7XVL4tuyR5-cqLWapcVbkuvrUGmRL4cS9BPU59-6l-tu_X-HWwO8SWc_lWrIpSVHfgf8quTIaNPJFaSdATheWf9I8Q1ri2LxWWUSE5C9NKsLKsy3zVXamK2XCUVVegEnkcw9YsT6hTEjSQ6B6e9PhyJ5nrxXLLIRJ_AVLQOZHT4u_16tOOEaLIU7tcn_aPiimA1VN6RlMqoiYKAJAfdaB3rSS9KnCCUg2WT1nuVITK6qhhogzzRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4859" target="_blank">📅 09:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlD5chY9Mm0ebDZp69X91ZdkYCv5Lk3pW9RIdnOKX_Es4Dl0nttsOeYpBLEcrTKv9g2_E2lGK_z9EoISi9t4IVK3staOmZaB5Xqg6UbKwQD-BtVBBU2DO-PCdDo6UfKbvGTXgl-DE_H6kG8bduPlxrAsxIo17cFOmnV0C8RmLnNClDO1QaLP6WC9t-ATOwEbJ--YcxKlR5xBQO13zLdvYP1Yd8HUqqnoRHROwwblFAXN86rSTuo0VWs9XEi2yy00n0sG5ogtarCbZxvu8iTPiQ8pJ573k5uRmu0rP3QN_Ejw-HZnP_z-sriagCpOQU05G_6ErlP1d7Yg_fTVfxtHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4858" target="_blank">📅 08:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYqRuphwufR_lIaRNfMrPMN_ESVidgUz7npXfQpO-Q1uNvDGKG9BzC4laSHN_ww8bkIkW9_aGUsoKBrrNqvqddQ9QoFHY5VwCn2VqoFz-F0hABleB61Nt6jg-A2L3L0UddOJNjK5O5n0CdMG4msTJITEBF3lyXWHsOxbwMnp_Kz2jYwt9mLzFm6pqdGQXBHWI_L1MQz5_bYZO95qya6yQGNI0EV8huWKE6bPFPJr0532P0e-1611NsFcLjHojmJKuaSE5mJvAIrcgyCEpxrp4ox8HL4fI9ZKuxEXZ5bFwYgquip-TlFLTSTblN0eYpZWO6KLokFh7ZDx8U4nw1_6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه سنتکام : سه ناوشکن آمریکایی در حال عبور از تنگه هرمز به سمت دریای عمان بودند که جمهوری اسلامی به آنها با موشک و پهپاد و قایق‌های تندرو حمله کرد و آنها نیز به حمله پاسخ دادند.
سنتکام در پیام خود افزوده که به محل پرتاب موشک‌ها و پهپادها و همچنین به مراکز فرماندهی و کنترل و مراکز اطلاعاتی، شناسایی حمله کرده است.
بیانیه تاکید می‌کند هیچ کدام یک از ناوهای آمریکایی مورد آسیب واقع نشده است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4857" target="_blank">📅 01:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZrruL-Wb0g85ZGwxIY8xKDXLyDfv87kj-NcOZv_YoiCOMsyH7-MzApxZrSH1Whe-L9xtfIlgYfIzjMtg-hS_t_a4G5fH-WtPsQQnztl5PhK5ZIxMzNDb0yrep_vdqgxKbN9N8ac6pCRy5HHHIZPNp29pp_StaGklrtm8p3snCowSM8dlmOfMIRJ5WuJRIQu60LHYtNeszppj3ybHcqAuPrX-c6vCd4clW6m93XJGgkUqXxIzLV4aKeAw1qKWjzMQGyrbbwDZ2yepxzwbCZMLAdhPN0Tk0-lgoH0ytJYDJ48JFuHOZT-Z8eUv05nJiYX0TryZRNHdWwjzOMhGmyDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: با تلاش شهدا قیمت نفت رو بردیم بالا و به یک دستاورد راهبردی رسیدیم،
ولی با یک خبر باراک راوید در آکسیوس [ که خبر توافق بین آمریکا و جمهوری اسلامی رو زده بود] قیمت نفت اومد زیر ۱۰۰ دلار</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4855" target="_blank">📅 00:49 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
‏سخنگوی قرارگاه خاتم‌الانبیا:
‏ارتش آمریکا با نقض آتش بس یک کشتی نفتکش ایرانی و در حال حرکت از آبهای ساحلی ایران در منطقه جاسک به سمت تنگه هرمز و همچنین یک کشتی دیگر در حال ورود به تنگه هرمز را روبروی بندر فجیره امارات مورد هدف قرار دادند
‏همزمان مناطق غیرنظامی را با همکاری برخی از کشورهای منطقه در سواحل بندر خمیر، سیریک و جزیره قشم مورد تعرض هوایی خود قرار دادند.
نیروهای مسلح جمهوری اسلامی نیز بلافاصله و در اقدامی متقابل شناورهای نظامی آمریکا در شرق تنگه هرمز و جنوب بندر چابهار را مورد هجوم قرار داده و خسارات قابل توجهی به‌ آنها وارد نمودند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4854" target="_blank">📅 00:37 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
رسانه‌های حکومتی  به نقل از منبع مطلع نظامی: «
حملات نیروی دریایی ایران به ناوشکن‌های آمریکایی در دریای عمان ادامه دارد.
ماجراهای امشب از تعرض ارتش آمریکا به یک نفتکش ایرانی آغاز شد و پس از آن شناورهای نظامی آمریکا هدف حملات موشکی و پهپادی نیروی دریایی قرار گرفتند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4853" target="_blank">📅 00:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
تسنیم: «۳ ناوشکن آمریکایی
در نزدیکی تنگه هرمز هدف حمله نیروی دریایی جمهوری اسلامی قرار گرفت»
🚨
خبرهایی از شنیده شدن صدای انفجار در ابوظبی و‌ دوبی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4852" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
فاکس نیوز:‏ ایالات متحده حملاتی
را به بندر قشم و بندرعباس ایران انجام داده است، اما یک مقام ارشد آمریکایی می‌گوید این به معنای
از سرگیری جنگ نیست.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4851" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">در حالی که خبر فعالیت پدافند در تهران منتشر میشه، جمهوری اسلامی هنوز دقیقا نمی‌دونه کی امشب بهش در قشم و بندرعباس و‌ تهران حمله کرده!
فعلا میگه اماراته، اما نمی‌دونه!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4850" target="_blank">📅 00:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=ezJlLZ3RPmTR6sJvH9N_y9m9aXgwCVXCcnYeTVb3Tmov6yX5aITkw73p4AaQ2L4VQQk-ZgLvSRoTRUlvXjCIUyrphX76n2ax5sblZi1Aiu51FNekgJOqrwoaIgSw5VTXZPRWILYy_SV-PUm0VrYlLpl4NevqmD61hChQOM1GlMv5Eq87Z0LcJyHF7fkTGgIcbWkp4EkraG-49udcHIroBX9A_UR5UHUQrbC5fe2y954aLafB5v_VFaPo2gqilmfV81Byv_jcZEhScWMc8V7twF_03Ih4GkONfwbaOb3IszvAE_Aj27b3NtF6J_46Jch6Tfo6SQoWdpTgeQdLl3xk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea8130ce7.mp4?token=ezJlLZ3RPmTR6sJvH9N_y9m9aXgwCVXCcnYeTVb3Tmov6yX5aITkw73p4AaQ2L4VQQk-ZgLvSRoTRUlvXjCIUyrphX76n2ax5sblZi1Aiu51FNekgJOqrwoaIgSw5VTXZPRWILYy_SV-PUm0VrYlLpl4NevqmD61hChQOM1GlMv5Eq87Z0LcJyHF7fkTGgIcbWkp4EkraG-49udcHIroBX9A_UR5UHUQrbC5fe2y954aLafB5v_VFaPo2gqilmfV81Byv_jcZEhScWMc8V7twF_03Ih4GkONfwbaOb3IszvAE_Aj27b3NtF6J_46Jch6Tfo6SQoWdpTgeQdLl3xk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش صدا و‌سیما
از درگیری نظامی رخ داده بین ارتش
آمریکا و نیروهای نظامی جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4849" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌ها از فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4848" target="_blank">📅 23:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
پایگاه هوایی بندر عباس، کشتی سازی قشم، اسکله بندر قشم و چند ساختمان اداری اسکله قشم ، امشب مورد حمله قرار گرفتند.
🚨
رسانه‌های اسرائیلی به نقل از منابع آگاه وقوع درگیری نظامی امشب میان ارتش آمریکا و جمهوری اسلامی را تایید کردند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4847" target="_blank">📅 23:50 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏صدا و سیما به نقل از یک مقام آگاه نظامی:  «به دنبال تعرض ارتش متجاوز آمریکا به یک نفت‌کش ایرانی یگان های متعرض دشمن در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت مجبور به فرار شدند.»
🔺
برخی رسانه‌ها از شریک  ۷-۸ موشک خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4846" target="_blank">📅 23:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
منابع اسرائیلی : در حملات امشب به جنوب ایران، اسرائیل نقشی نداشت.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4845" target="_blank">📅 23:05 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌های تایید شده از انفجار  در بندرعباس و قشم خبر می‌دهند،  و گزارش‌های هنوز تایید نشده  از شنیده شدن صدای انفجارها  در میناب،  بندر خمیر و سیریک خبر می‌دهند.
🚨
برخی رسانه‌ها از احتمال  حمله امارات به بنادر جنوبی خبر می‌دهند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4844" target="_blank">📅 23:03 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبرگزاری‌های داخلی از حمله «دشمن» خبر داده‌اند، اما مشخص نیست منظور کدوم کشوره، آمریکا؟ امارات؟؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4843" target="_blank">📅 23:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4842" target="_blank">📅 22:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6pmlrlrvrnn-OyADgmVqlt4o8NFWRKdquZ-C49XWUA5rrsNo0vnSDSKIUywgMjFsha5ubbcugqIpRG-rkZwQuDZQQHS6xbaHO_zugs2HWu1H7vXRVyFkTC2gz4_Vbv0WkoaUhw1k50dESX87Ow7gzkJ6IACV2m3_WEMDK1Uf_CS5jO9kHxYWFsvky2pRi5kD6E0-JjBctub37Fyg8AO53c8TDBCsG9dWrllTAnDb86NdwpBmORE-KWqpg5U0Jh3p-9QH9cB5Q2pRD68DiqCfu8uft3N72faPIxQEMDoFsbegyUrEySNy1MAUKlfFsJvh_Apr5jL-mBHKddzjL5waQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله به قشم
خبرگزاری فارس: در جریان تبادل آتش میان نیروهای مسلح ایران و دشمن بخش‌هایی تجاری اسکله بهمن قشم مورد هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4841" target="_blank">📅 22:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
روزنامه وال‌استریت ژورنال به نقل از مقامات آمریکایی و سعودی نوشته عربستان سعودی و کویت محدودیت‌هایی را که برای استفاده ارتش ایالات متحده از پایگاه‌ها و حریم هوایی این کشورها وضع کرده بودند، لغو کردند.
روزنامه آمریکایی نوشته لغو این تصمیمات، مانع بزرگی را که پیش روی تلاش‌های ترامپ برای عبور کشتی‌ها از این آبراه حیاتی قرار داشت، از میان برمی‌دارد و مسیر را برای ازسرگیری عملیات «پروژه آزادی» در روزهای آینده هموار می‌کند.
مقامات آمریکایی اعلام کردند که دولت ترامپ اکنون به دنبال ازسرگیری عملیات هدایت کشتی‌های تجاری با پشتیبانی دریایی و هوایی است؛ عملیاتی که پیش‌تر در این هفته، تنها 36 ساعت پس از آغاز، متوقف شده بود.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4840" target="_blank">📅 22:08 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0lQvKKLpezoHLEpVDQAjiq_WphK9EALxJ5g2M_dmXcAVIqW-8WJZc7Gz7WVfW83fVHXi_Fg-xx6BqycNcN7i9cD6zS-BUrbaH85AaX1tLoO_e-HENkRJoTdtcnmrCPZxwQwiaDi9_85MVx3gf_7YjLAcgOFYh62lg9Kb6_SwpTn4b_N-0GQgXTG2NKKwNa29IlsYPzMitTu_kYIZsSqPRvpyQ5HzVI4mI84KSmb8MSG4NsofuIyPV-uU2M4Z27JInUEroFrnYfgqsozlUo5ggLDEqYAseyNSJBK5pkWgcLyhSgOsvMTlJRKwJylMud-uWC91MAcVIIld8Ol1n9naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی
منبع شرارته! محصولی جز تولید
نکبت و سرکوب و عقب‌ماندگی نداره !</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4839" target="_blank">📅 16:24 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1t9l7fhCKu6hcdIar8Kx1kbGMs9Oqi5GKqvfy-1FE374upoPHlfT0hg81FqcFoTdK0chdSdwx1CXz4IODuWHBqCgs1rfiaP3g5KFObYJ8-JnM1F8Goluy58HyMCGdg57soaz_s5Aj8y47KdkHh6sGbPlQm87JTH3PzIObbi8iJ7N4A7Jiji1S9mIz6gWAyv_O0c3iAXhhFWBbwmzaMAvHQ2IBwfseWoGunM73TF336ODZgCSNnvlqtraEILkSiwdbPHdLezQhxdhKEo_HR8yeaISM4TLtvLv4pmYTUF_rwbcz1HGerOBQzAefmHfzClAVTuK4fBYEMbCfrEyjiXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری چندین شهر و روستا در استان نبطیه در جنوب لبنان را صادر کرد.
با اینکه اسما هنوز آتش‌بس میان حزب‌الله و اسرائیل برقرار است، از دو روز پیش درگیری نظامی میان ارتش اسرائیل و گروه تروریستی حزب‌الله لبنان افزایش یافته.
دیروز ارتش اسرائیل در حمله‌ای به جنوب بیروت، فرمانده نیروهای نخبه حزب الله موسوم به «تیپ رضوان» را همراه با چند نیروی ارشد نظامی حزب الله کشت.
طبق گفتگوی آمریکا و اسرائیل، قرار بود اسرائیل به بیروت حمله نکند اما فرصت را برای حذف چند عضو ارشد نظامی حزب‌الله از دست نداد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4838" target="_blank">📅 13:34 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmAIAdTJWLI6q1SIzZttIR-tKfl08bejJDj-3pP5YUAIXYGIQCP_xmotPkEfOYxkmQhYEJJAogaTTM8Dz75RqBw8YIWq9OSRUqHv8W8xh54DZ81hVXS7cZ6oiuMZu8LrG04d7JzHpJ02khLShSNzOxZnJ9VpyuJANAEUSM7jForcEPEh12P85EMSDmYcUVZFNBnBN3eWjXIDN84bdP3EucsP-KvCupE6XiCSigBlhkAafqxObimZdr-P2pXKB8bygBW4qi7n9Cnujwc_6vdSTGqqWGuXkZuDbk3YnMwXciri6j7A6tVaTm6GSUZvY5nfcx1fIe1SrxRmeEiN0BkyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه امروز وزارت خارجه پاکستان
و زبان اردو :))
بهتر understanding
سفارت کاری یعنی dialogue and diplomacy</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4837" target="_blank">📅 12:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSooriLand</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=J5F_L8X_gLzTjiH12Msp7Po-FR6GyfYvKCDvBaK_uZ4EfUKxhZz4gKw6IWSgI6iBf7TLnIH9g8kqZp6Qhz-lDtTPqzLqKQJ3pzGSxKm5h9cxhNRlPSLlz7i13BnRhBG771G0gsSNbIYW2Fd4NpIHeidlQuAvdza0aJJUeNmMDvt1l_nDcbKJ-qfi4Jj5O8Y9lfmmVTjVg0oqVkfpEZ9QAgCpCx0CpX0eBq2_JkCioot93-fISeO7wz97CdxVSYRvHqbt8Iux_PXfmmcTNXl6o4h4jC9RKCb6cAlKbdauzm7cdjiezoCdql0dnywE616o3KMDZzsSWFLcBSFi52Bk7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=J5F_L8X_gLzTjiH12Msp7Po-FR6GyfYvKCDvBaK_uZ4EfUKxhZz4gKw6IWSgI6iBf7TLnIH9g8kqZp6Qhz-lDtTPqzLqKQJ3pzGSxKm5h9cxhNRlPSLlz7i13BnRhBG771G0gsSNbIYW2Fd4NpIHeidlQuAvdza0aJJUeNmMDvt1l_nDcbKJ-qfi4Jj5O8Y9lfmmVTjVg0oqVkfpEZ9QAgCpCx0CpX0eBq2_JkCioot93-fISeO7wz97CdxVSYRvHqbt8Iux_PXfmmcTNXl6o4h4jC9RKCb6cAlKbdauzm7cdjiezoCdql0dnywE616o3KMDZzsSWFLcBSFi52Bk7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ls2k5Rh0HEJihsJegAS10sb9uIZ_6VsBQlCa9fMDgTdWZKHSXcYcAyQ1TfzY_euhfAj_t1sHZfivhyDxHbrDSQSVvgp2953E5yKqTHeAj-mUSM78FRBvAxMRZzatcosKAWDEZ0akvR1LuVKjYUqqWqQDKQEffsDK2nR63DmGuQxnFdvj0EzmyM9p1eoVnk_kPLULbj0mbDXZ66Fiq4ooEcs58eh6om0buH_YyyDSS2HQtezrN7JK9zzm022ecAzRH-stsQEFnYXWL0yLtqUe04UXyKSm4idWnd7wtMBS6tY1ovAx0if1Dguy5vGRD1LVzYCUBMi7Nx3ob8E5jcS6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hn3KQadKohVdv7J_I4DNSo8tdKZi3kLJaDfWA39V3aQLsRxT2tmdTBXatdNMlztLevpV1FZtZUGv7Fa0O3FfYvaTD-AJWmbCIPga1y_RjDAIGXyX5CkHkG2LAtJAiYexvUlCidsDgyGLXoMeVFPznwvkiwC2P1_tplzT-kicNpTgkNEjMWasgF1fpgqE9IUCLHrjFLL55_003ewjxjd53wG70SalazgdSB0mbzdD8sV3rOiHiDNp2WK6ogJL99YVYjv0gHYD8gv5HdAVeW_DIUKyOjyIq9O3fXI3PnSXUBd0Ovu4SQU8SrfVl0Rku2Rpzlj7-fnlw2xFCi9eoi7TUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTA9mSYjaMjzWmVYcAyGDq1O0GuvczvxRFY_t7S4x1ahhVXkJ21IyXMUzHlW2l2tQlaoElmTCq0y0zya9E9cP-dLrkJqeW_2IrEB_RudgessnUo23OD_ZL6aDwgn3co67Ql2NMaljhITwTV_WcjFd0aeQPffRbT7SfjSnfAmMejPQEi-qbVilvUWlicjQXWk-8jqGFJMOKr63Fvg8fy_z3u1FE2BVFfbWnm-FUr1pZRj9RD9V0-RITbkcHNsMwAj3Bq2TzXuVj8MT3dCd26RuobyvDBachOe-Wf-yETWv4p4lJssj3cA4iYD8MsFqzw9VWKupjRkDfigmJXnHjy4TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/4833" target="_blank">📅 10:52 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx9OT0kx7uHx530rT55HiN8qqj2EgoZaP3PensHeVIIx7OXlUPqMg7X-9tghL8VTEmZ6969wcSLQQj52azc0-s_VoM0TlJ85-36ZXJ3tImtqXylrK2kWuplIDmU_wsx1tkzfnLo-1ul3WhtTypDv7IGqSdXJcZqY-1i4zhC2ytXRTqPIth_DFvjdXmzEjzjse4fM0IHypYDOTaKzqc0XC5QM-_U7SevBsw4qxOEqLvqrnbZJmbj2sxMdkNgKc-RDuIEH-fxLnWE-XDCodkmTNv77ndZzNJGAChz5FvEWjWGqPDia-dDBU0qmFqA5M4lqjOir9Xm9JyvUHThiefRdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
ادعای اکسیوس : کاخ سفید معتقد است که به توافقی با ایران درباره یک یادداشت تفاهم یک صفحه‌ای برای پایان دادن به جنگ و تعیین چارچوبی برای مذاکرات دقیق‌تر هسته‌ای نزدیک شده است.   ‏در ۴۸ ساعت آینده، آمریکا انتظار دارد پاسخ ایران را در مورد چندین نکته کلیدی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4832" target="_blank">📅 09:53 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
اسرائیل : تمام اورانیوم غنی شده باید از ایران خارج شود.
🚨
امارات : هرگونه مذاکره‌ با جمهوری اسلامی باید شامل رفتارهای بی‌ثبات کننده جمهوری اسلامی در منطقه و فعالیت‌های موشکی آن نیز باشد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4831" target="_blank">📅 23:42 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3pdL1fzRDHQZVKUBAN_EhHT1Tqarv9A4FQxf_53fkK3N2zyKHI2ZOLNiny9Qni4c29xcA6OfFqlOUIG7-9m_e_V0Qou9ZV8QItI_edeXV__cG76qLNni00OtEVy3e7QILARQUpPI63pRDJUQ25DXG9_j_AsnxQMmjAYc0gGiQKZuPQwAf2YzPAR433r7EsbMruBL1bljThwL1TfqbnYuFhWRys_cqId1UXPxPZP1Oby4BV4ml-XapqfXpshetCAGQJ3Xq_f0O3o-qGpo9zTbgACDVfjeA0nnh_Yn8wYlJvfEwCePruytLi63oB0nvtarOsCVHDByMsQbI64a1ZKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
در حمله اسرائیل :  عزام الحلیه پسر خلیل الحلیه، از سران ارشد گروه تروریستی حماس در غزه کشته شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4830" target="_blank">📅 22:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4828">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGutM1Sl_Peg8gsaGXPEE7KK93ZJn1YQMdhHjHu9obHmQQjtd6C1zO1BVJ8kCPlUR1FtZucoD-uL5YPkHVGUD-s7AXq8oqsOxkEGFGbAC5CVuDoDCP1RfP5_uE81njbO3SWkM3XFaoxmrsGNEV_GA9z2TX9y-W7XiQscbx26Q14wubrCeVed-AAgO-ool-9stQIxg_YviXSSr2FtOVfKWyLRowkTLxak6QlpoVImg5JxZDiYO26VeTr9mWmfTmuf4SMt3EZbHakZB8V1WZdmhpRFHhqPHh0lAjLgCbz5vzV_PRUn17fdVG9iwPLbuQqCD4xE7evIjzOKz0h8KuePqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrh0wph5YMSY6iUXrQ-tL0w2U3nNofgWsZufFas0IyOvNf9NmDht5Lu5SMhS28eycFYj1AD2QPlx2ZcE9ZE5TdJFQN4B_Gf6xnSjIY7zJ_zPCClzSBQgfQWFXaXqKz41iE7We8bby7f5fUQaoei8XJb8XXA7rirJvQf_gt84gENA1V8deuho4f9SPnFVsimkcxPiG1bs_zJoWJFJ-CpN4EUBM1Q0WgBvEZQsQyP4mdOAifNhzp8KQ1g-7t4e2mGnJfg0jz419sDgz8UPOEgxE9M5qeFz2JsmWA7S_0TQkQhUq3KZyUzqdWa1MgvhzwOGP2RKkviAauBR2E20DVMDBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
در حمله اسرائیل :
عزام الحلیه پسر خلیل الحلیه، از سران ارشد گروه تروریستی حماس در غزه کشته شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4828" target="_blank">📅 22:44 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnGSDLr3jIJIda9qMJ-Z_0rfv7ZDoGbY2vDFxYFZEXcC4Azzv6SF0hzhO08MTWU_9WEvhbemOvOOzlh05U88xN7HtcetwHzxixIOXywgp2VPfn_d1Kkc8obuayJRV9Gp8q9sBdwy67YqX_2PmYK6axr-npYMHB2_1RKw2czaIXI3du5QHDUxjv3YyFoN3f_HAOIEejCFa5A2DAUxQSqevtUvPU9U7dp3Q3FbBZ9HACZHMwuYRC3Li_3ZSY_hRCUqOjS7TMbGtVn8shGSRMq8czeNz1z6VINuL_YhNL2oz_iQHgrpX90c37YaMgwdcOIFQD-UIWvImsUySFvi8dhbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
درگیری شدید نیروهای حزب‌ ‌الله و ارتش اسرائیل در حاشیه رود لیتانی،
جنگنده‌های اسرائیلی نیز دست به
حملات هوایی پیاپی در این منطقه زده‌اند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4827" target="_blank">📅 21:47 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6vOq4nDdj0xX7x7pTK8sx7DJosOXqTNHGjtmqNuZ-8fdE9FBHrV_rpoxY8_yyWs3mOe5Rswpsdv5kowd7SB3zBpXmpCdgcK8wQo_wpFhsI56k0PhQzd0jgK83R8o-rFEqshcozxBt5hMxx7Q5AfztUwG0EfII_oMiXF6rRqhoqld01l0quwGOXPIxVBVvWSxy5NL26KHZ5o5z96pLirrCsTiXsRGZUyeGmARUXpPl_EnFhyujDX_X4pzXKlu1AHh-v1nlm4PLR_fAy0to_PyRDIRHbJ_qX-TN8eog_JYWAQ5kzT3bpr3Hzy4eqe2hoM_xOXoz02Q2Jm6h0cEarR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7BVSiG4WlgNSEyvPX3zkzkUf0pbpx3w0r67lORWA758KXiix9tnMF-ublXiWRfTBM3bBvv0TR29BoO1L3FozJPdjGCU5sP3nCCrDtkf6M1oXQTG0xd1s1fPcUHQhuUauvDubPa1UaO18LXIIr0y2iAHIuWNVrALriyBPbFqKE6oV9Hg6n9ODXMOlemGAsJ9SS5C-Un6s0Q9cUwWXyfn2GKvHcUoTrhAz7WsTZ89sV9IEYfC1EQP_Pj2YgSdMDkNrWa0GJUtSOjzF0rk0i3C7XcwIsoPfSULJSTVL1q3HdjiHwEqiNs4fiSDm4gYJBV4SEZ6SBpsdA6J_zHrAeD_2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvdx1Lnlmfv7AbTZIZIBVAQFGHCntk80vqvJvXQXRrI02ZQ-39WoSyrJyL2lYkciUnhno_TcJdeZ8bJB0c16F3xWKazfR7unRlQruV_ZUloAtGut4_EBfD1nBtCQOIcGzEfrCEBir-hq-8vHQbyRQ9o1be6OkgTAPOcNIGKkTyjEyZ6iRUaE_qAW8W8ie-WJyu9doQc996qEFp97q7Dz4fwKEkcmyZwnAOZT9SiWNgGjBl4mgme7SBXE1xwPqUgusqEzpK3HLOgtisQVst0xnrcEzuc9-6GxbflNkk-sKt5Lihz3lT_tPCMwrxg7ETkFBKxSK3dEbMgX2EogZFhMZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4823" target="_blank">📅 21:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5vp4XOaa-5jGK4R1EHkD1Y3fWk8X5Rv6plTb_mmt_GaGdok4gPZafGgacz3iadSRJPoZgd4JNuAW4czyQU7K8hs0eBhb1NuoKfqHx6pnHU127GtjFePrW18iJ6lfjbVd09WIeV2k7-nnZc1BfLCvIACyZcwRGfXyuU-oyggeCSixQRkgkRGkVbyiXxhr_eejbQni5SxU9P6G55-CRmOP1N62paoK7weCc7BIEBgOghAZvfo7APs8WscK_ZIVF4XbtITMvH_8tAtovtsUiPzUlCjrifd2TMJ2WwYLGhDi-1k3-pOB9xl1PWoE6jSJLeg7LbHRhS6_q5z0YtuUtpfJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1eE79rtFwTduRrdMq4bilch7I-DVQeY0ce0_AIqqQQChYvLLEEIefBVXtPI4e76kCxoU2r3vySp9pbV8jlpjGKkxsROn5M23u1YsnsMco2AgJepTaTiyEeMeBGGBYlAq3ZnXTbAk_xl031gWjbaBF1zTExYOJz_MDy98YejiJ6I9tVsq2Ervr-Vpplkw9ya8_GOGdrwWXNrvMuPS98KAryPSpdgTyCcK8Hs2s4tKn4kiOiujd1teDmH5W5JYVwtVkg9Wkxeh942WBUSSC4lu2PnlAbg4y7VTDjvxnI_U6VjBtc_-5Yn6uQ5TbBg1S1uoRvK_uXSt_RWmygmUGentQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «پیام صوتی» می‌فرسته :))</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4821" target="_blank">📅 19:40 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
یک مقام اسرائیلی به رویترز : از رسیدن توافق بین ترامپ و جمهوری اسلامی بی‌اطلاعیم!
خود را برای تشدید نبرد آماده می‌کنیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4820" target="_blank">📅 17:28 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljGigD71z5GT1nPawl5cYcbb4RIgQxzXtT1qqw75xr-odOiM7-jkC2Cw-6wUK4PedsQUq_LP79Oas7ic3DQPWDf_W38M8sq9zof0MgTS69AD6Jt6waZNLDKe2ylBVPoPjSyT_iBZVytM4WE6tCDK6L_Z7jazhT3_y4I8M2WErCydUSaNVIl6z6vcAQXLDWdqbMKoAbKWLwy1P1aCbY7GJ29qm1vQ-12rCTDZKjpvyNQw0-cKdtNmhFzpN9hykULRM-_83cigKU_Hev9yWv5X-Gx2L94u8P_0z3wbCOu7M1uJ8vsPDLGMB9fHLcuyNrosgierTQbJQZV8o0onyWd69w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5__tGoOMbZakbzqysLz72uHT3H0FiA_Rn4Z3r3_B2Fkh2kBk5kcisIJk6HPz_WKYG8ddErxGkZhizfS6KT0zP_hcv5aBZYgE4eSLmIrqzyEvQVQe3Agsbp78x4pAaGLN9qVEoybTX_a1avxamXZTKN7n_p38GF1jfIS3INAC-SVu95lmiVVzaD26Vkm3FWbU1ejpgqiBWoTfyErQaviBy3D3SwwrhYSu1y1f3yXGU2JmHn4RcAmpGKRULiU8pHejGDlCPpOXkkvHh03XHb3CHWDQKeWCGMvpvb4UcEgyxROL8JpJ-5mdsq8fbxuGnjWhNyFSZjD7Fbo0d0PEAlHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWZSs3YpH6kzcJpJQUdApW_IPrCkJnpe6CfAogv8qehvOXiv0e6kH4n5wK0zFQx7FmIgXLdhsofHHT997vD1YSkuU01DJVqxzllmFbNiGBebQtlMb8Vg-0Su616ZRjLwI6PR2lBwablSD8TiTOL97Cy9EGnITfRpM5e1A--178aowBE_QxMERglhLHohJ1AbqGkCcmazqrKlFTiH5IvUYUdDqIMYEzdOQ89asOBT_cH_TAEmrUzT-nl0LfjNCLGWPkBPnvJiH9JBGEEaTtOJEvw6hW5VLo57WjROYEEko6gZFBxHyNRijkLotq4xnnBOBaPAN2tgYX-wQrYw_f3xsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سخنان رهبر عزیز و  عظیم‌شان کره شمالی خطاب به ۳۰ میلیون گرسنهِ زندانی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4817" target="_blank">📅 15:50 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0dgBHCl5NpaiAZvsLohUvkpuN_IzyAp7qq0oSQ2VMcbleoKv8J0bbpW7YSfzF0wD10VRRKaVUM0pUfIZ9xUdZDt5h4Twk04e8G5JoT9WVcHeXD1yXQISeQUe3fGs8PSmZVI8zbTuTnFfT2F0lyVgrGRb6bQhuT6_LklBfTah6m0xUVDwojj98ohUPcOJ4NqVIi5gVwe4jQ-hXJDvn2EajX7EWEpLFwSwmycM1clf-PTbxXBHGOZqVWOaWzOy77ACut5-4rocVrH9AIM60rGlBY3V0RLLtRLordEOnL1j6L1KVhRHf2AHfuYfaIbxbM-P3gh0o_4Ybe9xCclLnl5vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN_90Yl2Qx9pjjtLTwnF5IuM1URnzbRCVL_R0CsGNJ1hZNbevKK6tn0wh1CcgENKNQpQL7ICIj0FxnrWoZZATJdHTkr2npi1Q5g35Xrtu5-joPth4ztN2_lU0dx8DheEURE26gSpliWykVxu8gtuKKq5DHh1cdfQ1et-hE73aWeVloY9MXoF23RG1HFXjNQ_OvwB9W-4armdtBA8SXsZdQlTyK7-O8jVerqQaN308IDQA5uGFcLwRSEpJQj6c4VnG2GQdxgzVrsgfaUa4bKYE_JrxORUZ7E-cpC9ftb5y6AubfcDmyprxZL_PmlaKAykV2Z1JDWEgqy2qJTdVF8yBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سقوط ۱۲ درصدی قیمت نفت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4815" target="_blank">📅 14:29 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtFwh0QeoWtlSVPXYmuNWXpZJlX1P6_yt-lPkgJO21m3Bqu-flaJm9ubvtn1ZBpQSObep2axnLl8pjg-WNxgMRl4FW3gr6RrHwv0n67FOeTsFICzATbDjtTOkkJUF2nr_Le-9fZvh3c2JoMEHgRIiXhEh5fmkB0Er08qNKx9hA1HizyStapSGFrn4oRnPeWP9EqjFUPHVWap2rO1af5DFoJTK4x6jUZturErpX57LM3q4ysKvsRC4hW8GX1iwnYJxmiITBCnQ7bmNA4KekMxrAHG09wbrsWe-6WLLnyyzXQI0satFzFXgmgHiIFDYqmWG6oFcTnpUOpA_us6FSHFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4814" target="_blank">📅 13:56 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9vKaZX7dyQryH6qiZwk8MJYIqlYV-Vr7G6bGBbZXYSkjUyhETJYM1omx4nmWM-9jWqc55PfG8u9Pz-RFK0mBnv-_wKUiXw5LcBS0u8uGibajrSN0-orfUH42sFqnIzw_y4N4bV-w0Kt3rJYFpKnc20x1qD1BGxtwsjU4HAnmrEGKMRaDd4-2xi9TD_9_9xQbq-1Vo7gKUruBtYJ2fXYc6iRviDoVjpZ5HgN8xWBFH40Fqoebmp6Qst2-cZ0ISOv2tK6bXb8_nntYvl0UshSx1YFwvCvxZ82p0ysZfihbTCFQiEOqJ3oReVO-Nobo3Ec1W-VrGreIJe0rj_ZVys-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4813" target="_blank">📅 13:51 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJhCtD0wwc6R-Bh-Rmt1e24OJ3MV3Ft3RbW50MWRdcU6itxWAj-vemrkC_AYCIuVqKjAZSMfa3W56Lwzb9wowSXnKS_VutA23lECqLQ_c84h8CeVH8Oh-Ds09zzenG1aDRP27BIkyFGZkD93rQKsf4TXbHxibioeb1lFl61WsO0MqJ26bQR0nESvbF_EloPWvdKn6zt2DrbJTMsc9jiQdH7AphyDi0DCc2-AarZyD9dSAId1TB20XWSyguoupuv-qISTBTaitiDLw0eH_jgPIplTu7stO9v61DtFuS20IR0WcTJNiC5ytXW-XwumCLe5jK9yoQ8e_s8yH01ZG3qXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
ادعای اکسیوس : کاخ سفید معتقد است که به توافقی با ایران درباره یک یادداشت تفاهم یک صفحه‌ای برای پایان دادن به جنگ و تعیین چارچوبی برای مذاکرات دقیق‌تر هسته‌ای نزدیک شده است.
‏در ۴۸ ساعت آینده، آمریکا انتظار دارد پاسخ ایران را در مورد چندین نکته کلیدی دریافت کند. هنوز هیچی توافق نشده، اما منابع گفته‌اند که طرفین از زمان آغاز جنگ، هرگز به این اندازه به توافق نزدیک نشده بودند.
‏ایالات متحده انتظار دارد ظرف ۴۸ ساعت پاسخی از ایران در مورد چندین نکته کلیدی دریافت کند.
‏این توافق پیش‌بینی‌شده شامل تأیید آمریکا برای لغو تحریم‌هایش علیه ایران خواهد بود.
‏توافق مورد انتظار شامل تعهد ایران به تعلیق غنی‌سازی اورانیوم است.
‏این توافق پیش‌بینی‌شده شامل آزادسازی میلیاردها دلار از دارایی‌های مسدود شده ایران خواهد بود.
‏ایران موافقت کرده است که اورانیوم غنی‌شده با غنای بالا را خارج کند.
‏به ادعای اکسیوس: این یادداشت تفاهم، پایان جنگ در منطقه و آغاز دوره‌ای ۳۰ روزه برای مذاکره بر سر توافقی دقیق تر درباره بازگشایی تنگه، برنامه هسته‌ای و لغو تحریم‌های آمریکا را اعلام خواهد کرد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/4812" target="_blank">📅 13:25 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
