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
<img src="https://cdn4.telesco.pe/file/Mw51jRYg7_Ij66wchzLCKonqFMuLWzUkOdp-j4ijMrD036jxt2pzysbAu654XKR9DMQ18o815_P5LxpMeXcKv7ztWNoEItPF22WWUKQpD2Ob76yAIg0Xlkalwhqu7s-DstTr8BKhsc0OK3bJ76vzTL8HoXhCDlSpHMBB9Q2q3fg7y8Ey02OLY2jj4FTzDy8lL3pYreompPHv7zfmTgZSe5ExdAC7YgwHsxQnB2l9aXDKctbVBfCThOE7IRUT6OhDdS6URNysPwkuaPTatNxazQr1ulD1BkzZ_CTFiBTnpg9R2r2RDTGnh-tpeWTkNCu2zFht3PzYXs7nhe0E8hAx9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-686598">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا به فاکس نیوز: ما در حال حاضر تحریم‌های بی‌سابقه‌ای را علیه ایران اعمال می‌کنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/686598" target="_blank">📅 15:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686597">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6258e5b0c4.mp4?token=eV_cdInpSVEyQoXA3nNClFDUX4U9lBvNcU-iiSYAIaXx-J5Q6aQQ6-LuppTquFF6zw5uJYim2gS10eR6ekCli3WZCB5RXus102mZM8cxzJ9qf5CBI6ujCkcxE0sMygftBff4b14NpkFMP_RFOzVzCjcPmG9CRUQIshwKuxOhHHBcty4a_6fV22yGdxvPRLkOV07loayWPGZBPeom4wxA1IDnY5poT6VILmiMAdsExhNXk5oFe1wV4GkNY5QKC9ILEl_1vl7CIyQRMQb3vSpcHi1f8ZBSF0J0SmoEUUj7wbTDXTVaXnAVDeIUTr8BACyIFVKaj1XPEy0t5zRsoRQRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6258e5b0c4.mp4?token=eV_cdInpSVEyQoXA3nNClFDUX4U9lBvNcU-iiSYAIaXx-J5Q6aQQ6-LuppTquFF6zw5uJYim2gS10eR6ekCli3WZCB5RXus102mZM8cxzJ9qf5CBI6ujCkcxE0sMygftBff4b14NpkFMP_RFOzVzCjcPmG9CRUQIshwKuxOhHHBcty4a_6fV22yGdxvPRLkOV07loayWPGZBPeom4wxA1IDnY5poT6VILmiMAdsExhNXk5oFe1wV4GkNY5QKC9ILEl_1vl7CIyQRMQb3vSpcHi1f8ZBSF0J0SmoEUUj7wbTDXTVaXnAVDeIUTr8BACyIFVKaj1XPEy0t5zRsoRQRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به اندازه‌ای ۱درصد از تولید ناخالص روسیه به دلیل حملات دریایی سیاه آسیب وارده شده است
پوتین:
🔹
باید بگویم در حملات دشمن به کشتی‌های ما در دریای سیاه و آز‌وف آسیب کلانی به ما وارد شده است که حدود ۱درصد از تولید ناخالص داخلی کشور را تشکیل می‌دهد البته این یک آسیب بحرانی نیست اما با این حال، یک آسیب است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/686597" target="_blank">📅 15:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686596">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا به فاکس نیوز: ما در حال حاضر تحریم‌های بی‌سابقه‌ای را علیه ایران اعمال می‌کنیم
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/686596" target="_blank">📅 15:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686594">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ece111bc.mp4?token=oPilpzujjtwKN4orAnZxeGb159TvEmXaDb-VIAEdOegpQHjQPHeZ3Y9nhoV86p3J2rcyGBUBsrzu3_Q2HXQYNuMQASP0ojP1-Mye3P-Rd_a6igzwdcNR9ppCjxOHGIgnJXhrHCqcTkP2hrkmSbryZC0QFqMwFx5VNXfYFXm-DvXBWXgf20fgHMyFsJsyCm8yv5QS07T7CGcSncMA-k4jcOXHNW7Qnzw1SOXbnSI0esQJcVQRfaddc-6WUsFccFOYSHPHvXe9ThyjY1IWbaWU8AymssXZqAtguOw1r3XLWDaOHwsUTiTSODWsD7q7ZDTkk8X7oHMMGJ35mdor6Z5Ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ece111bc.mp4?token=oPilpzujjtwKN4orAnZxeGb159TvEmXaDb-VIAEdOegpQHjQPHeZ3Y9nhoV86p3J2rcyGBUBsrzu3_Q2HXQYNuMQASP0ojP1-Mye3P-Rd_a6igzwdcNR9ppCjxOHGIgnJXhrHCqcTkP2hrkmSbryZC0QFqMwFx5VNXfYFXm-DvXBWXgf20fgHMyFsJsyCm8yv5QS07T7CGcSncMA-k4jcOXHNW7Qnzw1SOXbnSI0esQJcVQRfaddc-6WUsFccFOYSHPHvXe9ThyjY1IWbaWU8AymssXZqAtguOw1r3XLWDaOHwsUTiTSODWsD7q7ZDTkk8X7oHMMGJ35mdor6Z5Ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعجاز خلقت را همین‌جا ببینید؛ جایی که مادر نهنگ، با ترکیبی شگفت‌انگیز شیر رو به دهان بچه پمپ‌ می‌کنه تا رشد روزانه ده‌ها کیلویی بچه‌نهنگ رو ممکن کنه! #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/686594" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686593">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajs8wcwVIJhlotA8irytqRqFtATDxJEdqFG7EDJv_GzeAq83q9Apn9SeEz_IpAq0Mbbj5WQJ37r6s9vFRp8ej0hFcKHooLMzosu6HO__95MH7sB8j_aH9EvfquwgJgzt_Y6mXyCZ1bvz6dojnzMnAVHW_XL32SQQyj6C-dieoHYYGOwvcA9LEUx652ImLK7lWoy2MZbILdZ4RTJOqAbUhdK0DqpDPOYS3a0818zVzj9OcNh13M9F2zbuB90jlOw46AWL9k30kxLv63FZhka3DrYhEJfVI12oM1aA4r9aodcuWDjuoiClm6xRd854-ATRPi4T0tifiqwN_-21R2XdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسری شدید مواد اولیه تولید کاندوم
🔹
با رسیدن قیمت دلار به محدوده ۲۰۰ هزار تومان، افزایش ۳۰۰ درصدی هزینه حمل‌ونقل به علت محاصره و افزایش قیمت ۲۰ درصدی لاتکس که ماده اولیه اصلی این کالا است، بازار این کالا را تحت تأثیر قرار داده است.
🔹
بر همین اساس، پیش‌بینی می‌شود قیمت کاندوم در آینده‌ی نزدیک، افزایش پیدا کند و این محصولات با قیمت‌های بالاتری در بازار عرضه شوند.
🔹
به گفته cnn، اثرات موجی جنگ آمریکا و اسرائیل با ایران، محاصره دریایی و افزایش  هزینه تأمین مواد اولیه، از مهم‌ترین عوامل احتمالی این افزایش قیمت در دنیا عنوان می‌شود و باتوجه به وارداتی بودن لاتکس‌، ایران نیز از این موضوع مستثنی نخواهد بود./ چندثانیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/686593" target="_blank">📅 15:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686592">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWiIEF9mH9rCqrE27uNXS_Yu2PVCc9BopONRaCclMdPJ7J5tiB-e0uiuBd_FZ99fMclE3amqFVv4MEpFAJL5EgAeoOltwWHynGIAjy0lrV-QG2zI_GxHjYsLZBDwV5yjSib4Z-CbQ4OmHtKnN6cDsirkQVaem_Zb6BFUhrPgFkChRcg6QdllC5GVYzRCKMR6BxmHFtmsbp5WEW3UYpv9wCYsgAP-CBGVzFqMQUQS1VIiHq9l8dwxCKsX3Zur8VT3QGbK1AYYX6FDtAR_-82WWjWpDw5yzz_x2IxhLbS53zHsY4045Kr9TRfcDetsCGnJLM9dFblZ58-QdOqNq8DFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به عروسی بعد از عقد و در زمان شام رخ داد  سیدعبدالکریم هاشمی نخل‌ابراهیمی، نماینده حوزه انتخابیه سیریک در #گفتگو با خبرفوری:
🔹
این حمله بعد از مراسم عقد و در زمان شام رخ داد که عمدتا خانم‌ها در مراسم حضور داشتند.  شهدا و مجروحان این حادثه از نزدیکان…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/686592" target="_blank">📅 15:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686591">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z519sB0rBCruTBNkMtuWkUA1lJFr3ZogSscmvah3AN2p17NIuGxuLL_F37P1csjkd9xZhY-1tfAQP7akJiFs4H3Qkiz1-yAlEjVJrEHBP0yq8xJNBgUxmLRn7OLXbnDWwa6DT5AzKMOJNHbzRQ5i2murQ9d2bK5e0qney4Lr-NhjyzhNVj_N4yIg1MVBkO29ehpIeNwkIiUocAg5NLikuSoDdSZEhzQ2BDlJvSXjw2oSEtPV6ILjIqBKUwShpS1OpIbUWJEtzLZV3mMiTaYNQ99MOpJH9YIlxdEYVKMTcTJ_pELkuvZWaRbNlSb6onxIUl2eBbwYcPk7fpVYeK9hHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: اگر غنی‌سازی نکنیم نمی‌میریم!
🔹
حیات ما به غنی‌سازی وابسته نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/686591" target="_blank">📅 15:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686590">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
گزارش USA TODAY: ایران نسل جدیدی از موشک‌های بالستیک را وارد میدان کرده که قادر به عبور از پدافند هوایی آمریکا هستند
🔹
تهران دسترسی به ۱۵ پایگاه آمریکا در خلیج فارس را برای همیشه قطع کرده و عبور حتی یک تا سه موشک خیبرشکن می‌تواند پیامدهایی بالقوه فاجعه‌بار داشته باشد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/686590" target="_blank">📅 14:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686589">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAyMBEViCYingBpFZBWhdxGPCPNXZnX4_bzzVdgePE4wTIW-0zrEU_JSCuYVKPeYXApdvREPay3W9JmS5VkB59_CjopjvOuFqlFRDCI56_LhkJjn0-fBDbmw7rd0yBuPc9HzachHSZ5kh_ETRW5QxKb4495rJZL8at-wTfloTI822IfddWtUO0JVLeD3xnGorK1Iqyhth3khLiYalITz5ZD4WVPBMhbObf_2nWBrUIgL9mDxr-bQkCPhieTW-3FtjGlxKyNsWEANHCJJXhuAGLRob-dl7uOkwQArAeALFqryamwQDWl99__veEx8jEL-6Arc9c5KwCwA9ancUjnKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: بنیان‌‌تان درهم خواهد شکست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/686589" target="_blank">📅 14:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686588">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkGNia1Z2GXZ8TwuGpC1DL54ihtuZli8Ghib4v9FyI3Y2gsQ56sHQp8Xx6Hkb3k4PLdFTKOY3KbxfRUXKfH1W1JGKyh6Tndqhmm28DhthOf2MBEMBry7UHhY7fkCYDbjUlnbttbhNPJbs9TH5yRGtx48SU14bze_CpmT3Tjpr9w9jl9XDwzr3mNqTjAXOFNkPB_PmibrrMHqEbnkdmqxKrQjLpENvYsHq8HUZEoFOIlCTVu0yGi5jydna9NNfDuKuJfUaXXrv3xa-wGesX2RzEuY1PXQsNHO6fm-oPaheSBsguC3H9kynz4CHlsqN8uPipZRq2gf7g2r_U1NqiysbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/686588" target="_blank">📅 14:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686587">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIC3rTzzvAIwT68Q-vZtT4BpmaoMS972PSaU1ThOK_bV9_vimCoHjO3wSMoDDEHw0FC88O9M7vC9bWtEdWTohzhn9dQnfLQNlPumkZzOs8ZgyAPz5kopV4tqIVUJvrDiLcMyv6xr5RtZqKFabtkuoY0xPg3myu9StoOQvrIXsggrUcOurYgwvRvgpZ7-ZGTmRE1yD2pXy6HADzuWFOx0ERvNImynnmEI5Gj_-MfIZDWJ_lfHYT3K9S-6JKUiGarbwMnyjKlI46fbRQ46Jjao3fd6MIcMP60GKCvCB_ZA_SCB2-vj33kcsEZ_9JLL_qJssyTAvlop9gyyuA4poOf2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سایپا ایران خودرو را پشت سر گذاشت. از روز واگذاری ایران خودرو به بخش خصوصی تا‌کنون، سایپا ۳۷ درصد بیشتر بازدهی داشته
🔹
بازدهی سهام از ۱۷ بهمن ۱۴۰۳:
سایپا ۱۰۵٪
ایران‌خودرو ۶۸٪
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/686587" target="_blank">📅 14:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f101f2f.mp4?token=JdricScShgblFSM0WVXsjt_0O_acZjSEMJTe9B5wpmDToovTghi10-G71h1nh2_WZywIkeQZcYlFY6pYDiY4wOWD_sOc75ZYHoV-ykKyPEuGWANrb5O0OD2OJpC2vdhewyL1NDr24nBmfU_XxCTUKiB6_exgeMesneLCuJ9fZDcz9w7bw7zaKbz1UP1cyqDRhZq_pVnCFcMU_MIGhcgLRUgRnqIf4ef4Gfge5FVdipCzPqedELxxAj5rEFqVKTozPkEBrhGkikrAkPiZRd2Rtps9UsgQioA6z8WInbVDDzWwTG2t78aXq1XOFdfTZTubxJUxeN5avs8OxLo3NJxBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f101f2f.mp4?token=JdricScShgblFSM0WVXsjt_0O_acZjSEMJTe9B5wpmDToovTghi10-G71h1nh2_WZywIkeQZcYlFY6pYDiY4wOWD_sOc75ZYHoV-ykKyPEuGWANrb5O0OD2OJpC2vdhewyL1NDr24nBmfU_XxCTUKiB6_exgeMesneLCuJ9fZDcz9w7bw7zaKbz1UP1cyqDRhZq_pVnCFcMU_MIGhcgLRUgRnqIf4ef4Gfge5FVdipCzPqedELxxAj5rEFqVKTozPkEBrhGkikrAkPiZRd2Rtps9UsgQioA6z8WInbVDDzWwTG2t78aXq1XOFdfTZTubxJUxeN5avs8OxLo3NJxBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در نیروگاه برق اربیل
🔹
برخی منابع عربی از وقوع آتش‌سوزی در نیروگاه برق خبات در استان اربیل واقع شمال عراق، خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/686585" target="_blank">📅 14:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شهید ۶ ساله عروسی سیریک
🔹
امیرمحمد کریمی، کودک ۶ ساله که توسط ارتش تروریستی آمریکا به شهادت رسید.
🔹
خواهر او نیز در این حمله تروریستی به شدت مجروح شده‌است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/686582" target="_blank">📅 14:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773878b9cf.mp4?token=USTT97Cf2cbDdhz6MYuB3FycWX9cXCSfpH1v83a7FCuC9N_nk3vapKWOufKgcrvrCf45xNtGVQKf0BuPQkEwq1Iy4GaAXjQUSGVReiv0GE55bmE9BWfB-JHXfZdtHYx6qiCZYeh1syo70TZCiWZhdi1SBwVvplEmgf7lU-jwIrT88gCuWxq5mFoSg_n3LEN9HcIzkqKpCsI1gbcTGC8y28m_sCVq3jH9moKj7EmoL1hg54yKx_TmwScb7JlVMngpEFxhopRCrzvNrRfdui0pv0N7z_sRkOqfei7fwslJlZ6vSVd2sCKCx8juE7Bs7xjiXRAZ8_uAbddjsdvaYz-A8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773878b9cf.mp4?token=USTT97Cf2cbDdhz6MYuB3FycWX9cXCSfpH1v83a7FCuC9N_nk3vapKWOufKgcrvrCf45xNtGVQKf0BuPQkEwq1Iy4GaAXjQUSGVReiv0GE55bmE9BWfB-JHXfZdtHYx6qiCZYeh1syo70TZCiWZhdi1SBwVvplEmgf7lU-jwIrT88gCuWxq5mFoSg_n3LEN9HcIzkqKpCsI1gbcTGC8y28m_sCVq3jH9moKj7EmoL1hg54yKx_TmwScb7JlVMngpEFxhopRCrzvNrRfdui0pv0N7z_sRkOqfei7fwslJlZ6vSVd2sCKCx8juE7Bs7xjiXRAZ8_uAbddjsdvaYz-A8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در الکامپ ۲۹ همراه شما هستیم؛ نمایشگاه بین المللی تهران؛ سالن ۶ غرفه ۳۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/686581" target="_blank">📅 14:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رویترز: نفت با تشدید دوباره درگیری آمریکا و ایران، به بالاترین سطح چند هفته اخیر رسید
🔹
نفت برنت در معاملات امروز تا ۹۷.۰۴ دلار و نفت آمریکا تا ۹۲.۲۹ دلار در هر بشکه صعود کرد.
🔹
تیم واترر، تحلیلگر ارشد بازار، به رویترز: اگر مرحله کنونی تشدید درگیری ادامه پیدا کند، بازگشت نفت به محدوده ۱۰۰ دلار را نمی‌توان منتفی دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/686580" target="_blank">📅 14:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698db1137a.mp4?token=dTx8serwNCAW3iLvZ9hYJ-soEU6n56MSOmBban4Ee9XL10Hvj9ZgIrjFdSV5zbs37ZDuZfrpWZjPytrvQ692mEUZZhBuxjj0IkJ1W-OwLhqJpiF1i8Snb9R3FQF3BleRJ5uPJgjvK0u9sd6ry7TFpYthubcOB76mCoLNHj4agmMW6BOLb6kh2iGsZEpv62-0eS_iDQCjCBHQNxX820WZRbetPLhj1osewAEGqIMNo2fQrSr2H4UuOEIU2Q-mhUswJL-yt_C5wPwyjudcNoEQLmFKm93Q7MUZCaNHnt__L4As3T4CdGGqlvK-bwvqJdVatU1iC0IzkDawi_R3L31hLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698db1137a.mp4?token=dTx8serwNCAW3iLvZ9hYJ-soEU6n56MSOmBban4Ee9XL10Hvj9ZgIrjFdSV5zbs37ZDuZfrpWZjPytrvQ692mEUZZhBuxjj0IkJ1W-OwLhqJpiF1i8Snb9R3FQF3BleRJ5uPJgjvK0u9sd6ry7TFpYthubcOB76mCoLNHj4agmMW6BOLb6kh2iGsZEpv62-0eS_iDQCjCBHQNxX820WZRbetPLhj1osewAEGqIMNo2fQrSr2H4UuOEIU2Q-mhUswJL-yt_C5wPwyjudcNoEQLmFKm93Q7MUZCaNHnt__L4As3T4CdGGqlvK-bwvqJdVatU1iC0IzkDawi_R3L31hLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیاتی از هدف قرار گرفتن پایگاه مهم تفنگداران امریکا در اردن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/686579" target="_blank">📅 14:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9UmcnL0UClXaNGtIfGbMnalmclucFkIdmlq1T6NQ2C3ZmwWMM4bwOom2lPCgWd3uBRnvHwlr6LVyhFfQEkEZq1uozGU5UMtQPPHSQMZo91aArHRPHEEgCw-B1sfOl14YUV5sx7Egh7jbk6moLCmZGvnicqfeiCoix8cKeaaq_yDDMioFkvDcRq3eC0QT8j0_2PZVrE5GlPRWCPaczCCl4j9lBQPBKEpUcwR8FGit0FP6u34hhz4b0SoPqzSuD5IKoghCSfcUtDm0q4sDZd4M-dRauFIFcJNWfCi0VpRILuRuYu6e5XAaHvFAm3crHfpjTGCHJeKmnUXFZNUS0NRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هر رنگ کت‌وشلوار باید چه کفشی پوشید؟ #استایل_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/686578" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhomgIaDmrPZKjGd-DcqETPa1aNp95v3XPC0y9t8sTwYwQupYINHOoose-divwiT8MS7fzwmJZz6Ie4us7A8w_49-78WXwAHGP9RpODfNM9yiK6zxzQneA7uqONvcgfSBH4gtgHP0fZp6St5SGHg6fxYxM4Bg2n30Ge7JrMA2JELVsaFuYw6y3xWwIiyQasGqjUNS-N-_dtaBJuJPeCaHEq089l382rfO-jL12U6JRJq1ISXfjPDXU-V07GenXwKGA0sZr_JlOEZQ8iqNiKoToQlAgm78v6-LYb-2mnhxptc1TZkIy9OGl4DgDp_lc0aP_RodoB1Pir0MzBFxnfUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO6jtfpQPYfKB_yYV-YO1X2ASvUyFAM8cLjw0sOg0ZkU5WV1nyfPSWmeqFRXammSmIihMbMkLLwqagUlSfkxs4X8IrGNR3DyvGRe7CvVOJVa1SFNJ9I46PYmUt-gVTBc0V0m0hfm1Q6U0XZrQSUqVIneS_yKhX_-lqwJlYAfIKX2RPq98JMYE9whiKnagm22azg-DwN_A16PRY8A-9sPCeNkuezBtNZ6vcz8LAkbAs-f5so-vToHiC-ZoWXEc2PJ5ygcUzc4eBzQJ4PxeymRIaqZA9GT_02ay1WUMQdjqWIvJRo60GteUO5HEDbIRD_iTrnNMqEbs9V5rNLUPA_Qww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شکارچیان خاموش زیر آب
شناخت مین‌های دریایی و روش‌های مقابله با آن‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/686576" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0718e5256a.mp4?token=s3sMU7MwK28U9FCf14C9zQD9mReMa2IjLnHfKk8MFlMuHJNF_b0NWS9m-lYXmfA8KdPLf6ZCa15FXtoxEJrRtegf5AQNE1wrN2-OyL4KprWIp3rBEqQQ_H5Yt-O2Dd0OyumAK6794zzs-709tYiO1o4wYuF6M62H4B6fLuK2TUh_fopgMqLjqiQy2de96RX0_KWRTwc_5HWnOW__jo9FOToEQx-5y-kVq2cBYVeRayPh3DpSDWnD8tG0nS8T-9Fy8Zov7zb9gRkt2fk7JkguHq3Oc9M0QGI3829tzP5NUmgFerVkzCV-lRaPSWl81uV-TuAFWWeStldY7XjQ1ac67Kcht8lRyjsLTQD8N3qXevsXbg9z-wG3QuZm2M4dAGy0NCmaOhVnfnI9vNcxvb4RIYskQlmmmv9KxOLqw-uEuvaDMV661yxdk6FHaoqDOsYtUkWwEgXCsPxjFbv379jBpgXSuVhQ6VYV3YebdChNP3_vT60eXA7SmCZ-niQpyzC2RNZVYQ6MsG6HpzCcE27-Ooaq7AShMee9n8FqY5rIXAshH64kONcoHkVMnCw9qa_Y1kRp2wXsErCZvQn1WkfC_-0xQ8JkYJR46ysHLp8JX5t2ncPmQAXjamYn-dZSccoWB489bd1MED2IcIDFQ2wRLp-fB-to82IGQtaovJNpEBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0718e5256a.mp4?token=s3sMU7MwK28U9FCf14C9zQD9mReMa2IjLnHfKk8MFlMuHJNF_b0NWS9m-lYXmfA8KdPLf6ZCa15FXtoxEJrRtegf5AQNE1wrN2-OyL4KprWIp3rBEqQQ_H5Yt-O2Dd0OyumAK6794zzs-709tYiO1o4wYuF6M62H4B6fLuK2TUh_fopgMqLjqiQy2de96RX0_KWRTwc_5HWnOW__jo9FOToEQx-5y-kVq2cBYVeRayPh3DpSDWnD8tG0nS8T-9Fy8Zov7zb9gRkt2fk7JkguHq3Oc9M0QGI3829tzP5NUmgFerVkzCV-lRaPSWl81uV-TuAFWWeStldY7XjQ1ac67Kcht8lRyjsLTQD8N3qXevsXbg9z-wG3QuZm2M4dAGy0NCmaOhVnfnI9vNcxvb4RIYskQlmmmv9KxOLqw-uEuvaDMV661yxdk6FHaoqDOsYtUkWwEgXCsPxjFbv379jBpgXSuVhQ6VYV3YebdChNP3_vT60eXA7SmCZ-niQpyzC2RNZVYQ6MsG6HpzCcE27-Ooaq7AShMee9n8FqY5rIXAshH64kONcoHkVMnCw9qa_Y1kRp2wXsErCZvQn1WkfC_-0xQ8JkYJR46ysHLp8JX5t2ncPmQAXjamYn-dZSccoWB489bd1MED2IcIDFQ2wRLp-fB-to82IGQtaovJNpEBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زود هنگام‌ترین گل‌های تاریخ شهرآورد تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/686575" target="_blank">📅 13:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزیر کار: ۸۷.۵ میلیون نفر ماهانه کالابرگ دریافت می‌کنند.
🔹
وزیر علوم احتمال غیرحضوری شدن دانشگاه‌های جنوب کشور را رد کرد.
🔹
پرو در اقدامی ضد ایرانی روابط دیپلماتیک خود را با تهران قطع کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/686574" target="_blank">📅 13:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
برخورد با خودروهای دودزا و فاقد معاینه فنی در تهران از ۱۴ شهریور
⁣
رئیس مرکز اطلاع‌رسانی پلیس راهور تهران بزرگ:
🔹
از روز شنبه ۱۴ شهریور، به مدت سه روز،  برخورد با خودروهای دودزا و فاقد معاینه فنی اجرا می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/686573" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038eafceec.mp4?token=EmYfPQFe_fV4rG2G4L1HOJuoGrOIYp-ba5ouJMOXXVAiSGll9mTye3OH2RcPILxZKxwaPJwWd8s2C9LGbdkpYXipCMWJ7o2QgfE5WKBXrEHJbLvdc68Vpdjy3pWa2JY7De3o0w8ViWGRlDH-RcUwbYJFh672hxoe1JFEFWuOeBdNPl89k4ieN8KT_WuC5HUnlHK5HnlnCz-6lNeFwZ1fBURpC_JyfRWlI_CfmoYzqZEQcAYXdW0aJCIzDLfdjgpPQBfVrJzAt5ZiOGnhnYpVk8f2mPHctNb1cMMOUw4JdbIGHg3CvAxjBbraaLVEt4wxvIegsIJazOkLxWHbvxWglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038eafceec.mp4?token=EmYfPQFe_fV4rG2G4L1HOJuoGrOIYp-ba5ouJMOXXVAiSGll9mTye3OH2RcPILxZKxwaPJwWd8s2C9LGbdkpYXipCMWJ7o2QgfE5WKBXrEHJbLvdc68Vpdjy3pWa2JY7De3o0w8ViWGRlDH-RcUwbYJFh672hxoe1JFEFWuOeBdNPl89k4ieN8KT_WuC5HUnlHK5HnlnCz-6lNeFwZ1fBURpC_JyfRWlI_CfmoYzqZEQcAYXdW0aJCIzDLfdjgpPQBfVrJzAt5ZiOGnhnYpVk8f2mPHctNb1cMMOUw4JdbIGHg3CvAxjBbraaLVEt4wxvIegsIJazOkLxWHbvxWglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پایگاه‌های آمریکا در اربیل عراق
🔹
نوع حمله: حمله تلفیقی موشکی و پهپادی
🔹
هدف: مرکز تعمیراتی، انبار تجهیزات فنی، سامانه هدایت بالن جاسوسی و مخازن سوخت
🔹
نتیجه: انهدام مرکز تعمیراتی، انبارها و سامانه بالن؛ آتش‌گرفتن مخازن سوخت؛ کشته‌شدن تعدادی از نیروها</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/686572" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حمله به عروسی بعد از عقد و در زمان شام رخ داد
سیدعبدالکریم هاشمی نخل‌ابراهیمی، نماینده حوزه انتخابیه سیریک در
#گفتگو
با خبرفوری:
🔹
این حمله بعد از مراسم عقد و در زمان شام رخ داد که عمدتا خانم‌ها در مراسم حضور داشتند.  شهدا و مجروحان این حادثه از نزدیکان عروس و داماد بودند.
🔹
در این حمله بیش از ۶۰ نفر زخمی شدند و تعداد شهدا تا الان به ۵ نفر رسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/686571" target="_blank">📅 13:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d242958f52.mp4?token=pcjVCbV1aqPt2fNHHr32-30svR9M3o3wnJNBheSCF1weM9_r-0k4j4tC4p9QoIKKtX4na_FG-_AXEbu98lP2fN9fHgrLA60EqL_9rGcPHWGdAjtlHFPO63TqKN9RnBuadx3ea7fVrb9GBVYWIE5AFSuHEcsOCDmyClZ511dpMGrzR1RGfCa8J1z45_rX06ftdffOzDB9ZCoroqr7I_SgJpft_GPcXU3bf0kF8SXXcEtCvgouiw0aM0VkjKOq98GQxgVWFGU0K5htNU3Y3xC1G1HZUpXzDtUn8zpKPh-MFI8tLp979ruHOyqIZglib54J074SRPsYGef6V3CvMeBFSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d242958f52.mp4?token=pcjVCbV1aqPt2fNHHr32-30svR9M3o3wnJNBheSCF1weM9_r-0k4j4tC4p9QoIKKtX4na_FG-_AXEbu98lP2fN9fHgrLA60EqL_9rGcPHWGdAjtlHFPO63TqKN9RnBuadx3ea7fVrb9GBVYWIE5AFSuHEcsOCDmyClZ511dpMGrzR1RGfCa8J1z45_rX06ftdffOzDB9ZCoroqr7I_SgJpft_GPcXU3bf0kF8SXXcEtCvgouiw0aM0VkjKOq98GQxgVWFGU0K5htNU3Y3xC1G1HZUpXzDtUn8zpKPh-MFI8tLp979ruHOyqIZglib54J074SRPsYGef6V3CvMeBFSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس جبهۀ مقاومت: مبارزۀ جوانان حزب‌الله در نبرد «علی‌الطاهر» گلچینی از مقاومت مهدی باکری در بدر، حسن باقری در خرمشهر، همت در خیبر و حاج قاسم سلیمانی در حلب است
🔹
حسین پاک: چند جوان عاشورایی شهادت طلب بیش از ۵ ماه است که در محاصره رژیم صهیونسیتی هستند و دشمن را متوقف کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/686570" target="_blank">📅 13:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686568">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B78gaAQWVdfFo1oAXNPM3lUthtU5YDfH56mryxY-fSA5VopxC3zfi-UzmZIaWKStep6YUoL1YfiF6i2heLi7pMgF34YqVRQZE9itM22u0fQemOfky2TF2e_VoGDIHF1maLYDhWF2fZUUBcwOuOGzWQS8RT4lvrhftdC0-pjbyKTH-AQjR93nKg5I304blCOO8YGYcUY0AJ-kmJMooW5KdveS5e_j00YMg7xYLvEy2YgRT8miwmsZ66dbkM60-YRyGMWQpowU96pWP42lDOLuBi3SaSAKgx2lc2ANoC1vb9arLN5v8Kvwx7Nh6wS5xlN29dnwvjQetUr5wHKGDVeWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کمپ تیتین چه می‌دانیم؟/ شاهکار سپاه در عمق مواضع آمریکا
🔹
آمریکا پس از افزایش آسیب‌پذیری پایگاه‌هایش در خلیج فارس، بخشی از آرایش نظامی خود را به سمت مناطق دورتر از تنگه هرمز سوق داد؛ اما حمله موشکی سپاه به کمپ تیتین در ساحل خلیج عقبه نشان داد که فاصله…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686568" target="_blank">📅 13:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686567">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPn2G2JjtZMi6S7L2yf6Uru8ut3XCtObt0RxfIozzbo-lkvL819PMF1jzs7opOi0VwCBUit-gnVFPudcQOR_amcSer6YYMpanttPee7hGoY7RfvwIsLMDruHOpxim9o-ZhsWvwpTl1KmRAd8_6q1YvbEsx_W7NrjSG8YZlh_RzeEF3nlYwrQALpiXirULptTtdWmyq_x98_YzAA1-HTN4K5hYXhK2GWEkyFSB4BT86abu2XYhjUwzlVgGVStu2z6zOU05mJhU1eImswZgRifNU18_o0JpuwgSJSRk0KW0nxfKEgixOr2C5cgXswlMqTL_3_9rDDy6qr9QyBCViIqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای حمله دشمن آمریکایی به مراسم عروسی در بندر کوهستک شهرستان سیریک
🔹
محمد ملاحی ۱۶ساله
🔹
زرخاتون طاهری ۵۰ ساله
🔹
کلثوم ملاحی نژند ۴۳ساله
🔹
امیر محمد کریمی ۶ساله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/686567" target="_blank">📅 13:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686566">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31ad7edabd.mp4?token=puagFR-uRcwmb1KjawJ7-rp9mMbX4H8--eIBqB6tZz4a36M4iirR6abMHR9o23iFN_FNJDjvQT7QXFMkOjAddCwClAtV_iQpYI2QIAQ7JOTgCRO73TyIwU0sFCN8haABUA6HR5ATluqHscz76SBp9QbYzDnC_dBm6oYYClJeJOzz6_4wDJAQGhx34bv0MCIz5ToTLEPVmC_POsyuonFM9qzXQC-wm9GJeVmtDVr9AExdP0inO-qJYfskaA3E_jNQI5uqrp__93kQvbIj9weuIPrkO1lK-IA6YMxB1Nqp1p3UrGXUVAZpgvVHeAfW4WWMrkSyMYNtaeOMkY3Gj4VGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31ad7edabd.mp4?token=puagFR-uRcwmb1KjawJ7-rp9mMbX4H8--eIBqB6tZz4a36M4iirR6abMHR9o23iFN_FNJDjvQT7QXFMkOjAddCwClAtV_iQpYI2QIAQ7JOTgCRO73TyIwU0sFCN8haABUA6HR5ATluqHscz76SBp9QbYzDnC_dBm6oYYClJeJOzz6_4wDJAQGhx34bv0MCIz5ToTLEPVmC_POsyuonFM9qzXQC-wm9GJeVmtDVr9AExdP0inO-qJYfskaA3E_jNQI5uqrp__93kQvbIj9weuIPrkO1lK-IA6YMxB1Nqp1p3UrGXUVAZpgvVHeAfW4WWMrkSyMYNtaeOMkY3Gj4VGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس جبهۀ مقاومت: خبر قطعی به دستم رسیده که در حملۀ دلاورانۀ سپاه به پایگاه آمریکایی در اردن، تعداد بالایی از سربازان دشمن مجروح و کشته شده‌اند
🔹
حسین پاک: بالگردهای آمریکایی مدام در حال انتقال مجروحین به بیمارستان‌های اسرائیل هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/686566" target="_blank">📅 13:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686565">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
‏خبرنگار صداوسیما: محل عروسی دیشب با سه موشک هدف قرار گرفت؛ در کف یکی از اتاق‌ها گودالی ۱.۵ متری ایجاد شده است، ۶۸ تن از مجروحین بستری و حال ۶ تن وخیم است و چهار نفر هم به شهادت رسیده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686565" target="_blank">📅 13:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0eO7pwCgJX3tCaWiE5xaijhK9j497CM0G1Z6ctE_jU_VLnN8uRG3CuNgXljnvcq_8ZDQtAeRkzCx4eNuZxWBLSWRVMB91qizWWegjjUY5_S8XcAX49NNwb_fS9AkXNBKHvd9tVHhuLvJDtTXsCE-rEh7I_KBBaCUEptkDSlTBuzF9-V00vs443IunVHycp_pBVwAzSKOOfDdSmCTZK3LQickFwhQwSGgsE19B1uKJHvEJHTVApNEF9c8-jpw4LrYEyFZqvFPY_S12Zs5zYtX3DiIVxaMC6jEpFI6RbCIgGlP6vK2L_yQ-FnDaXoVyf-Bg85d5Bp1d43ODtHMIrxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imK1otUHTKijOxxGtXJNL4T0GrBxC9oIE25WiXsVYl_5uRPEWqokbkCq2E6nVyRgde2RQR5UDWZzPAVqhRLp8q-uZDzdKRE-Ktp4KBVjtKSfsBjITw-vt-Dsg5mTJH_ry5P2eTQ2p4VlezTMRkz3OlCbMeERD5sk9NUdA-L-Y05qZGDqTlJ0O8txVQ52fnSCBQ6fDe7TDmHHyiOOe1UR2ahDUvsPeugCyWuL13OXNhYrO6bKCWSMP6kpey67SyIA14SAdfV5O8lIJDpA_9lK6ECf770fyWie6BkfgdhoSee4NuUMHLg2Jmq6_07ceBEkPyHgoEH9p9uzkKPNs9cH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ube7ClP4jo8Esj0yOwscR8ZT8iub_0_GwscmB-tPaLLaM_nUs6x836aUx9W_STAdY7peQxMSEBU9gEr4EHJhM8GyUFnmvzr59W6fSt3uMqR7OCnlw-GSrNnsh-xc1qyiyuaz2qfyWE3OHgpHwQhb2OyZCX9zQfCTnB16Q63SHKueowirXY8l-y1vlk55HwZcFliWWTw3zQOsriMoyf4KNJg5Q0QD3x6BvNB6vn8SnPAFmUf2C48mf6GpRDDO-uU1H83Ims24YdftD1TpSrLCWPknzfawiqCnWayUQAtFjwnWSt_OavzfjU9XZKqVoIL986JzICFxP0Z9QtwlpfBHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnCJleXeRWPnSnXSw1mZIZjUxL0eLcqnHRKN7jWYR6mOUrTjevFmN8zH7UMhUj0ykWCVt0UWZm2qb-uX1r8xgP8vJloHz2x_5W6n9IhPi1q4NkpLi3x16JbZHf7sBK_AdBcC0nNZlFjl6fEaOXaODi5yP4i_hkNHWkvBwFY8JrxbLpL5xy7cgLnhyBA8sXwceE915Ci9nkRgilo9mWK6aCRqj1WUlPjCzTiLVm9z-3MFy7SC3FLLCTLBxW9IBE0nIEjnHFLSeylvLbCu5xz4NB66fPrZnF1aAtrJWBGvLYZhpCEUBQrsaajVFikr6ZOOWaWBBVAhdgvw_lYizfknTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tcy_G82oH0gRMAarDkxMh3Tvql3CMrkIqvzk-6cTaFNWkk8YHLCvs2sGw6iTpED36rVGmEDoCFEIvpAroWNhtdF-FYiLGbgfP_f6MHs25B07nJZHt3uEVmF4-OLISWAlBLut1RLM5vuL1W6eAMMdpWhooReTLnkYS_PESokBRSJ2zmwi-3_-FM90punhhrmXgoIew3_KZhL_FhFEU7fYjPcnOd7TLcqzAMT9GoYwQaOrIxIsZI_NK838SMQs_6PBFywnZLUjtioUUIMRma6-WImAiZUa77yRLaOPTKz5hJdAQ5NlqNMrkuDT9zMLga7yyrSYWGXSVxFSGsk_2xAg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcyDLpj21E7xS98hFDbW2rYYBrPxmUwe27hLWpDsvlh5PkMVIv--0PRd1VV8dX5I6V36Zeh2rw5uNaS9lKp7iKdHPYY6rfBEWDtOIUZtL8bBSlhD6_jwVI6mvRweuTOTbID62Qxsbp4Sb3YhkMaQ99t6Qb74EqZWfMxEfIdDCrGoSTg5W_uXwgnSj2Mf7XPFWtk4f6ZiSuVoZ5yZvlTRnzZRbM7pEvDVuixtgZmfRtMNkmilGCbIuAejzSahwUUn81k-X_vnZVLQoVor59ZFw3CeoZQfGIXWDHPFRQ24655dU6R0i6SzMwH4XeqvlxHYfTdlfF7Oi-SEwXcncM-3oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
واکنش هنرمندان به تجاوز دشمن به مراسم عروسی سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/686559" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lliva41VQO0M2rtN8fproAIu4ZkrI-qqm7IJZ_EViJ6_ySwhc7PA16ZSQaMdmg7rXDjm7nqx-OcFhz-jYt-3n5N9CyD7RR5O-20ldtqAl7p9jExTEelK61TjdKrS2eXpW5YtONXZd11FS5JDGBUxxj3-T1TFZYLGOIO0vuBdAeUQVBFW-6Av1RkFruDMOJp8-XZA29ehUNpJMFVgqiyVvOV2rlXd7sTkF5JlxWV7VbhzUtmMOXJcroREmwU7VbVAGQjAkz3bh8yWo477bV0lKqpbRrGShHwuXnVoUz_r8GsmOQd75B7ws5CdE-D_Xew5kbnDJnxa6nYQsut41VGq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام ۲۰۰ میلیونی تارا؛ بدون نیاز به ضامن
🔹
تارا امکان دریافت وام فوری تا سقف ۲۰۰ میلیون تومان را بدون نیاز به معرفی ضامن فراهم کرده است.
🔹
متقاضیان برای دریافت این وام به یک برگ چک صیادی نیاز دارند و امکان بازپرداخت آن نیز تا ۲۴ ماه در نظر گرفته شده است.
🔹
کاربران از این وام می‌توانند برای خرید از ۲۳ هزار فروشگاه فعال در اپلیکیشن تارا استفاده کنند. از خرید طلا و وسایل خانه گرفته تا کالای دیجیتال.
▫️
دریافت وام
👇
https://tara360.org/tbl
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686558" target="_blank">📅 12:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686557">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
۷ شهید و ۸ مجروح در پی حملات آمریکا به خوزستان  استانداری خوزستان:
🔹
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686557" target="_blank">📅 12:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686556">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytpKt9rTK4IQARZAgb5xrsOzkkCElqKKSy8ofA2xWKHWVTmaUHZM5fSMo1K8fW_3A4EWTwBruyT6i5E9OPahlp-imw1fvKUsd41ax7CcGEh-ZW03KL2nL2ge1T2Q05D6i5AVuUp2LxhTAUJDsaQfgCmdymtsLdBomG6pNjmADu1gaKwNULzCkFJu5WhNkOYSomhegvk7CAhkXXXOrYbAV87aPAOlok0yyAYNcchc3hTJwZycwA3LfbwniIc_o_qY4T_uOERMixwF1sCRx1OWWM3yAy9uzDSdxDeatHSDt7rVZ5kfaJlCIqOXMFThp01H-VdfuHWVBR9V_M_LU59Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بورس
| کاهش ۷۹ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با کاهش ۷۹ هزار واحدی در پایان معاملات امروز به ۶ میلیون و ۵۰۳ هزار واحد رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/686556" target="_blank">📅 12:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd62eb16b.mp4?token=L7OyWQx1fQmHirfrDB-w-0e6v-EB2GzzKxiSvWNOVjZ-3nhQ5kkePKD_5pb22oAUOaOGj_VA-UTvUUaEYIMa1BrGKxWALXxKp9cZ7RCkGLMk9TPi9KXlHQxYaS0sCtNbk1vGvfUkuBH5QP5kfmilAQ480c_49MPNAOR8XkHIPhqhnqmaZuxH60SW2wQIvf49KzdAzauZsGLc8ppHBBYASH8dFSe0mUTe8EnOidXDF1SuoBa6bYf_gljiTGR94MXRWIaZsRY_GzyC7Ltt3LVIQPvemOt4ixT1ZK0dj7ffYj9WgF25wIIbqcEsa7dXWTa48jsKwg8Ld6bC_aKcuVKo5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd62eb16b.mp4?token=L7OyWQx1fQmHirfrDB-w-0e6v-EB2GzzKxiSvWNOVjZ-3nhQ5kkePKD_5pb22oAUOaOGj_VA-UTvUUaEYIMa1BrGKxWALXxKp9cZ7RCkGLMk9TPi9KXlHQxYaS0sCtNbk1vGvfUkuBH5QP5kfmilAQ480c_49MPNAOR8XkHIPhqhnqmaZuxH60SW2wQIvf49KzdAzauZsGLc8ppHBBYASH8dFSe0mUTe8EnOidXDF1SuoBa6bYf_gljiTGR94MXRWIaZsRY_GzyC7Ltt3LVIQPvemOt4ixT1ZK0dj7ffYj9WgF25wIIbqcEsa7dXWTa48jsKwg8Ld6bC_aKcuVKo5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از جنایت آمریکا در مراسم عروسی سیریک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/686555" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جلسه هیئت دولت امروز به ریاست پزشکیان برگزار شد
.
🔹
شمار جان‌باختگان سیل در نزدیکی مرز نپال با چین به ۱۱۱۴ نفر افزایش یافت.
🔹
قیمت گاز اروپا به نزدیکی ۷۴ یورو به ازای هر مگاوات‌ساعت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686554" target="_blank">📅 12:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6S6sBOaZMAziFj7eifcRPg9lQg3pXoc8LmbvKKNwq36eYVdm3AI_PcfOMdycQyeB8NfFpYPKyrxMmYR-DKI9nCgYG5lmq253MpSeV7mC7dCjEc0s5FFLnuNGcaRFdq5boTUmUBspvxCwwN8ZmR5Kwb6-GaRi1QF11C6dX-TBQGj7SO1Kmd2oOwTIXQoIJEeAxqq4fkyFhsSwotHoTU2eCnVcz1dd72cTcoMdEvvc6773ghHhSrWSDTh2dxt9KrgOywm2bq6SYaNGr6RZdui0wrZ7uCLVBy_VvEiyZOMzqPqMEI3yJ_6SNpt_NtnbD2yb3keH8rJuv944zpjkzPr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4wQSSJ7nE6MNizzAa8w16F0k9bZ4gyxvS6waeeq2HpCuMw6bYMJaKnL_DfMhZ-1NAN3rcI7j5m4Pii_CTITDg0j1KWsGF0mdC6CVhSVMVHUzx27Hc-sRQpnFmtg-rw3BF_uEHpRO9bjou1MX-2yQuKXpN9S-lJBjertfx2m7ZKC4scdLj9vUj7nw4kbtqnWX-xuEztBLKO6B400NVMGtIUA6tY4S4DE32tm45ZKSBr8JJm3orq_ezEGNo6pe3DqDsn_KbRxyXcIqYCg1xZRsNq6DSjsoh2hZ2SS9w455oyNCsHtFaY-rO2sutyyyzfhD_O6La91ImON9E4vPbggZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Heo8dgRwgtHD-2Vzcg6LUBqbkMNg20JJ39LAfR3SrPvu0CwKEZ7Luuxx_pGkB2ss_qf-A9toAMmWRgLnV7m7TvE_uIJ_CRgZTcdLel-LK5IHYgWABfeXvV3ot8fs71kmlKck61eWcomr-mU-c2zdefabsR6qYV-2UdFg-afhGR4sF1aRGIQ2ytVwScPufT02PZ1efLKLHhOn7SKK5qjTWJA7_Q9Dkk-M-9ot1LtPe1AHhZJXIs1z4L3bpp9kSlX0cb2G0XQST4D9ZPQziTVGAaa2xySff9fVMmUXaVIOxPpSb6Uc777CkqLSl1ePX7vZEe0bUp8naqskYHBzoRR6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7PROz6n7XuSqrBtrlx2T95AXtk2kBt6hbqNv0Kizzq3hGizQ60uycpji4c07tge3OfIO0bg6V26nqnl-wQD-ryt_cMoxSzRhfsi7tg0igYFQVX0gqrtDt1FEkXaPCoMWHiIHtVvN-St0RlcllGTR3UKY6Gn9PExMLAdh_n2p9cf25DfixuSRZjVH9-pN1yd1n6r9KQ_v-Ln4OGczhpVLDO_PW-eVguAZ4Cuvc1Wl60kk1arifM2pm9zFeB4EnJWI7cyt-5qykJ_lEI6ImqESgjklrenPPXcydixzzQJEkqDLaCtqcf0qXfQ02Bfvs8tqowewA-d9MBzc76URrL9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrtHv9VuXLyDWOSH2H6n7kqieEMpw7mCm7gnHKSxIZBFGnhMLdMfAkd0RQAj0akBoXNhhUrKiqbzLMSdLBSf7bWgVz-suLU3JZCPQRdIo2miS5eF2ONYSR8Fn1Ou2HGSqghjJJcE-v2qBe9QCYhF9g6rDHcuArs8aVBnu4jlb-xGNFuySOjYcRw6cVwH-GtHAklvO9jEuRuEDjqRv4vUkQbPMTNJd8Xaa30LvYp_AIf73IXt0RLii3uBQ94zvFp1QEcNI5NHPfGhBsThI8o4RcyQEjUJbuAECBgOYodZUPqgHU-hEM5YoPiXeDTLmfv39N5V7Mimp6akRcjjv96ETA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوشه‌ای از حال‌وهوای غرفه خبرفوری در سومین روز الکامپ۲۹
🔹
روز سوم الکامپ هم با حضور پررنگ بازدیدکنندگان و مهمانان در غرفه خبرفوری همراه شد؛ روزی پر از دیدار، گفت‌وگو و لحظه‌های تازه در قلب بزرگ‌ترین رویداد فناوری کشور.
📍
نمایشگاه بین‌المللی تهران | سالن ۶ | غرفه ۳۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/686549" target="_blank">📅 12:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAoTSMcd8pJP5GyM6wB7VRS5Yl7BahFN1egc7n-4ctFBEz1hUM-Stwo3eZs9AXHWu5fX8Z6Atd0qUjmPljt7M5BoA4cT16RKzSslcemssVUxCOEhlwMAAYjyIH7PgLL-Z6vgGxZDOzIbsmMwO1UqWCHo6aXDs4pyCeDgSmZSrqvs-dHyHibv1DiAdLvvWLrBhb073g99epOk56AsN8247dtvzc-wilKG-ncnrYFiKHtPokdKMxNqmm-O_Il4bUZBrySvbC_DGsRZXKt7NOBk2alKgsW16nzgc2ZceW3frB46qjaemj3-GnUTCGoSl31Z7HRlQ4V0HbhPKgbRoY6oDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYAn5b01cySDolwDkd1jcGSSQ5s_sfY3vZ8JGmwc6yPDmrIdbd8haB2PLt-JfHVQc86lHP6raJ4B1uerAtTHStZLApAGhCJfgg_XIZocn0Mnz7H_pR1YDzCaderF-5C6NwJNxGF24uffEg9VVUChIpFgXQUm98H-CTCYbLmVtBP4xwPYrrMEQ_7SYATrqnVbi1ieabDoY6qFx1U1NMHAjwkmlJQ2IbvXjMiYyEjM-uBBF1n8H-uxfOlRVQDY5Y2YC59f1bwE68G7VcsElMERJMM5sPU54WOHPIhWTNeEXs3xtfoLCSXl1UQ6rc5sQGujo7fLGLbmAcD0GisiFaAryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UvXtdUaJ54TMB-mlyvHEXdD-cql0DE75FtD2skq40-45R2ZMY8Vu7SV47tIM_kwFEZg04ace83J_upT2HqThzA-cN5sQVOprxK8qkFTixLqHkQYYWFKEvrCKoohwYlKdk_ia8yWNVyT9JOrH3AHloykhJE175hhonmgc3mTUyvgvvsoutfWThfa3HL_0mGCHwJ5ZUoarTjoj0CpZAfuAgheDb1RaKKbssKD18Lmrqmgj7UQOiQXAoKoc8IydQztxCT4_BqP4G_cwD1wHkZS4Y7fWXzuLeoq9zaTMYnHiG6KxDkr3qR0iOk_5VF3jl1HRAbAbqtNBh0QoTZrRI2n5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkndsozVsdipDIOigBqGbZhWwRElT2RVQUhiyhPDAOwiLuj20T8obvAryPUzsxDVBOSz0xVQdGbxoXEndwD7sM3lINhIXaQ9i-CsRj_UUQBoPNk74UfQQl3Dsg_kCVHFZgV0cudOLfyDZMNPDnHBInoHQvewaz446baGIuklaH7Y_kDpfasQnWNHumPY040neT-3mEE1OjQ-UiURubkQqRFmOVBL33IIB3dFnhKEfTcuXgnusMhdWFal6FV1iO5st6UxKoi8u7Qp1rOiotlkXT_hmRRT943r5042KWjfJopTrTX1lbKoW5ZIrc74i6Kk1MG6pHcVswqMiV0fni9YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2ctA8oY3QlFfJBaPjttWBF427Jtb_j2yWvcUz7VlpGXYNf1ImH-IE0ITvHC9YhArPuSvcYmLKjEXdu-Zl_ivmjM6uSJr-zZOYju44GuSdtwxLf84Nc0pqd30ifdtDdfiI5YW8mD1HEc4VI4_mVxYAxNt9GPlGbUc1eA-G7YOE-9kNFKeldqagm2mPLN5pfBUjllmFeYoGuT4UJzKX8E_ISi3x9mXRGjd7vki91QB7l2UxOCLFISPBwRZ-LEx9ezuPnlZ3vdyGbj465DjHTvymx74FSKjy1_KuvWQvgGHL_7MpPvvm7xvegOKMeqGHYF2kW3DClPe_2ftDUjweqtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnrIfKAadjZVUTh-43qVYbnNT2nNBUnqCIeVQxlGu6QCOCJeL3EV-PwpqRtwmM7WnehW-okp7g5dPV0VZCKNK7cItsvXZ0bO9fFH1ETkPnT-DsbTjG3Ui-D8FaD-_Zz8s5oWGXUIWzoNR6DP8TovVtTrW0Z7HHFowf1k1Dbcf6zXiPPyyHFpkjd1FlwV2R0tWLpRbhmoVFpcWnp8xtyU1KtpvepMe8-C0oQl-rOm2uFWVgXxk1X9oYIsEHl96TKpkFdxAlZj6Yx9XjVoiAeq6WACp0MSodUBMhGgVU2XFuTlj2zLelR9bmuTOS-8SpB-glnzE7Dbqh7YuCZQbOUyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNltlLH-qoj3bal5HJMNDoZrR9EJUyPqCpz2_DQ44MuoFCS5zQ3pnqlLzVCAVo-PdCABUR90iOYB87VDegvr4oStw5oNwpF4WthVoVrBia1giSFPvBCFpOhzUn7vxgtEWbT6YX_GIFKmtUmQMxt2vUFKVSQ0hxnTmEVQ6aVw-IguYILD9ETu9QHd8FXBrH34L_ClJpGQhIcTNqaimv1jP4_XmnVUGn6SSe3HB5344gvltCrOdKbPy8xKNXcI55LOyuUSun12d7ae3OvfQYyJnmO89td_uPAwgDtYgsJL6PNsYweu-LrEJ6FwfmJb1K6Qe9MMI_3TW41CqaytOSu5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6ppJQYIjirVoSsFjHf2JAKSZdeEDJwva8uv7babNYZAbr1s7OA8JY91me8aCU9bBhp48M_hekhw_iZ7kUGReO0Otgz4Dc4aNa98kngilsNcjBW8vYZF9vKpNTPYt7EfzDyyMyz_Yvv6nQWgVyCTndir4QSkskGEJ3EQWxkq9wxuLx9HpSB_ohBcXeCVartRqQjcvGpFZW4Q0t4JFPO4f-lKRA_Y_JB0z65S2rq5fHBGXVKCXNpOuYG1qClnw9y25z06bfkIvn7BRhCmrqNIIz1RMevV4FBoeQyqL5up5vDUwcyc-WkIuo70VNG_c-qrNRjnrvC0IwwCtymiSdDUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbOoIC5z3cFVOrkIOX8rHRgQs1qalETcolzw8iS-_pQ2Kk4vYPqg0Mw1e36h20PyIreYVM5Qw0nPuuRNaY9tDzhMZu0x_rjBRYk6ckbGL8zDH8PlWwnjFSSfWsxJ7GYkkiB3VuBTgyYXd_RZ-nCua46PWmuqrq32iFbsVkktQGOmq2Rkt4hD7jHphagIqODEkp4NtgqE27-3pCk4_1D6lUHUPIsKqeE0SbdthbTwVtzmrDFq-lqH2JT8JN8Of08wdtFwco18xxrA4cyUZBla0mL87bJQmBEyayQIPwgyEbAuT9wKQ7HR6QK1Y3HUwUtNUbRpcHv_CZ-JAkrx2M9xAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noFreoBi3MLhtGVn6DUNhghKkimp197acsFb3aC0Ns0WP9SSbtD4Q9JkvWJwmEpf17_tE4akKloCykvOZOjLr12n9VVMofi5yR3RdeAR4rAlzpICrWu853TpWJ-dbu4bfL-ogf9wDRTHRqbNCt-PsqyIbNXLm0SyLtJAXo41cklBoME4HeVD3poBqNnlFJoODmZUy6yUZr0iiW-T7dE-NmE_DzJhKAr3BmiOW9CcOZcmA1LCRkx9TIqQWiS3yxNY4u9wabXyP09LuXc_0bdugvtg-X8ZBAGagCBtYYb_XpjNV9VCRHOlgEh5BgAmGUv-UmvqieMTCsnXCNljiIN88A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
انعکاس مشکلات تهیه دارو از زبان شما؛ روایتی از مسیر سخت برای رسیدن به داروی بیمار.
🔸
روایت های خود را به آیدی زیر ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/686539" target="_blank">📅 12:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c58e3b120.mp4?token=kvTwmeRD9uaWxCp159a2rOsF3HHQDsf5iOeWG6FveVRkHbQfb4GdIURbcGAsSUUHWYFB3eLTjkoqt1kj3XiYWMC2sN1q_NrfsjV1A0Ep4L1gQRt2A8EuhotY5Z7vDm3lbduoZLKG-r9sZfsNZ2iOivBJ80SE2PfV4aYIFgOemqwogZmFYN6VsKdIQp3Rbsf_JPIBsQr6LJa3sLCSdeb8Apr7kiIPd4DgeV5Sbi2Nd6r6_mG40rOz9m2jvuHKiXY_s9F8Bm8fA8BYXLn2euzm4nnlk8q1A0EEYFJ0YH2q6f2xXpRrCTUY78Y7ZVVIc2sW0AeW7H7EtK9sm4uL_RwDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c58e3b120.mp4?token=kvTwmeRD9uaWxCp159a2rOsF3HHQDsf5iOeWG6FveVRkHbQfb4GdIURbcGAsSUUHWYFB3eLTjkoqt1kj3XiYWMC2sN1q_NrfsjV1A0Ep4L1gQRt2A8EuhotY5Z7vDm3lbduoZLKG-r9sZfsNZ2iOivBJ80SE2PfV4aYIFgOemqwogZmFYN6VsKdIQp3Rbsf_JPIBsQr6LJa3sLCSdeb8Apr7kiIPd4DgeV5Sbi2Nd6r6_mG40rOz9m2jvuHKiXY_s9F8Bm8fA8BYXLn2euzm4nnlk8q1A0EEYFJ0YH2q6f2xXpRrCTUY78Y7ZVVIc2sW0AeW7H7EtK9sm4uL_RwDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از جنایت آمریکا در مراسم عروسی سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/686538" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پلیس: تصادف خودرو با شهروندان مشهدی عمدی و امنیتی نبود  رئیس پلیس ترافیک شهری راهور:
🔹
حادثۀ بزرگراه وکیل‌آباد مشهد، براثر از دست رفتن توانایی کنترل خودرو ناشی از تشنج راننده رخ داده و منجر به فوت ۴ نفر و مجروح شدن ۱۱ نفر شده.
🔹
رانندۀ خودرو مردی حدود ۳۵ ساله…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/686537" target="_blank">📅 12:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_fuQsVLAtBz4xWijbx4wPeVy-ZxZTZ1-EjqFjLDhJVUbZa1Uhn3iSJPxFbF724k8NIbvGptZ16W304mNZEKfB8e_z1iHl-7xVRjI8cAxad718g-l2cuq7lZQqm3C3xdfF-Wol4Pj17k-gt61yLkOUze2mb8EDSR9ApMHzmIciYCQoj8O-X5ZGU3jjPRZawxmWSZfrx9qSWUpE2CvbQRMRndRwDOVr2pMl2Dm5awAW1VrLX3h7rnRg4paEFW2NKvqLJEID2bXbdqSyhbzbrJJfXO7f2MdEsTewxSaLBYjwUU8NVucTtoXGC7Cm1YfewjpSlhEss957ILCWFRPJHgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قصور واسطه‌ها رافع تکلیف وزارت نفت نبود/ توجیه تراستی‌ها پذیرفته نیست
دیوان محاسبات کشور:
🔹
واگذاری فروش نفت و نقل‌وانتقال وجوه به تراستی‌ها، تریدرها، شرکت‌های پوششی و کارگزاران، نافی مسئولیت قانونی مقامات مکلف در صیانت و وصول درآمدهای دولت نیست.
🔹
طبق «قانون وظایف و اختیارات وزارت نفت»، مسئولیت فروش نفت بر عهده وزیر نفت بوده و قصور یا عدم ایفای تعهدات واسطه‌ها، ضمن آنکه مستقلاً لازم به رسیدگی است، رافع تکلیف قانونی وزارت نفت در وصول و واریز کامل و به‌موقع درآمدهای نفتی نخواهد بود. بانک مرکزی نیز در حدود وظایف خود مکلف به اتخاذ تدابیر لازم برای کنترل جریان وجوه، صیانت از منابع ارزی و وصول مطالبات بوده و مشکلات تراستی‌ها نمی‌تواند مبنای توجیه تأخیر یا عدم وصول مطالبات دولت قرار گیرد.
🔹
بر اساس ماده (3) قانون دیوان محاسبات کشور و ماده (37) قانون محاسبات عمومی، موارد عدم وصول صحیح و به‌موقع درآمدهای نفتی به تفکیک سال، مستندسازی شده و در دستور کار دادسرای دیوان محاسبات قرار دارد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/686536" target="_blank">📅 12:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab8fd704c.mp4?token=BikdpvS4m6uPYSjWumcFbXd5kfv2KDgAu8GadNzkVlw6yWITjzd03JKyGFT6GbmXH7ovtIqniev8KjPhD8Kc0SxZltKMsbmtPuSVUqXGjbQYiptEzLGVaaUtx1HtI0CNvPYOOCCZhb1nymyl90FvqcALuvAOBgTpqW-3vAv--hT3H9xBEagWSbbv8XfErK3KLSCyp3focKTkNRIWP4L9dwu0A8T6R5tSdjCAm4b7NYVvI0MJub09cqwbuMwZtPZJKoR7HCard3BdHJaemHZ9PUni4ZgjFRsTR6AbRnu_6jD0BdF35-P582oxUQnxXHuOOd02gyvCoH1wL6qtJMR3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab8fd704c.mp4?token=BikdpvS4m6uPYSjWumcFbXd5kfv2KDgAu8GadNzkVlw6yWITjzd03JKyGFT6GbmXH7ovtIqniev8KjPhD8Kc0SxZltKMsbmtPuSVUqXGjbQYiptEzLGVaaUtx1HtI0CNvPYOOCCZhb1nymyl90FvqcALuvAOBgTpqW-3vAv--hT3H9xBEagWSbbv8XfErK3KLSCyp3focKTkNRIWP4L9dwu0A8T6R5tSdjCAm4b7NYVvI0MJub09cqwbuMwZtPZJKoR7HCard3BdHJaemHZ9PUni4ZgjFRsTR6AbRnu_6jD0BdF35-P582oxUQnxXHuOOd02gyvCoH1wL6qtJMR3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا دیدی یه مادر برای کمک به جنوب کشور اینطوری از بچه هاش بگذره؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686535" target="_blank">📅 12:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ3BS4J3qtROTb3Tt_LROsQbBnq-eq6I5cn4JOw0NXEjYz1qml3uYo0bTblTBmqMDyMdfPa2zZqTTprI9MrkszCgNDiAffJcJWC8PwpTiykGqPB4Fsoai7D8ALsU65tyK0sbbIaCCrwyCcdN2-2KwunBeG-keWI88TJEp9tc_5ZS4sVUX7g0ywvhWNQd7hi2DBc6eH9fEtmrfaxQX5l97IGGe1AN2_NrQ_FFDPJUN4Q5CE6VGcU4XOvkdIJUqNd8Yk3lQS4FNCjV_HEPp0TlWqqWpVuHKTGVHIy-RDfz2160klirEQK1o2KMWxXnHiew7MZuJUTzFVTo_HpCJ23kzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه خبرنگار WSJ به ترامپ: از «کمک در راه است» تا «چه زمانی مردم ایران قیام و مبارزه خواهند کرد؟»
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686534" target="_blank">📅 12:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2746fbcd68.mp4?token=FqGYHuvtKmqbKQLQJHkbPIicjsB-uHcGqhRSAy-zmMEio6NI31VwViCJPEIQZFpLda2gURcJBkUsPqmWmli8ofiOjkfy38FuhoEGq7ZMSoQ3Db9mq4MkPoejb2hurVCyxPSdjxHNFzJbVNa5is_z0xTD05J1eL_H9lKloSp_azTUg8ciqeijzbP7CiYeSVLiI7UUP9cZ9BgZUeSGfrvjdwI3x4QDV9fXL29yWJLOf_gJPP2XSK4uDOGzEpghSW4hoi5tEP6rIHVrVzwtl-JAGMoUMoQl1VLK6VyieRbr2Rqtpq6Bev8cq6i1H3GxgfV5-f5eEHnZnYAydiVcu1orAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2746fbcd68.mp4?token=FqGYHuvtKmqbKQLQJHkbPIicjsB-uHcGqhRSAy-zmMEio6NI31VwViCJPEIQZFpLda2gURcJBkUsPqmWmli8ofiOjkfy38FuhoEGq7ZMSoQ3Db9mq4MkPoejb2hurVCyxPSdjxHNFzJbVNa5is_z0xTD05J1eL_H9lKloSp_azTUg8ciqeijzbP7CiYeSVLiI7UUP9cZ9BgZUeSGfrvjdwI3x4QDV9fXL29yWJLOf_gJPP2XSK4uDOGzEpghSW4hoi5tEP6rIHVrVzwtl-JAGMoUMoQl1VLK6VyieRbr2Rqtpq6Bev8cq6i1H3GxgfV5-f5eEHnZnYAydiVcu1orAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند یک‌ثانیه‌ای آتش‌نشان‌ها برای باز کردن درهای قفل‌ شده
👨‍🚒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/686533" target="_blank">📅 12:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBCq_Vh8ifCWD6wlrlGZu5S3FkfLeDJCwBzvnUB-n4L_r5W9DQ4Sli8PcuaJXo3PID-8_RMVf8F9PTjkEDErQxGqz6BZEf73td10alWAHtjJVHX0rCnnRJb5p4Lw9SHi1v0RWfsRYtriabDIrLIH5OLIYl2maVWEPlwULUD_mhoLfHD9_PC-fFTJn7iHguP1QJXSDCmgiC019SQrHS2CUNpPqbEvxvcorI05p8Do-mVC2hsNRF7giujAq7D21yaxBQAEPNIZ_4-dTm9fcJ1wXpbmVBD1poIcGqqVNOLOEPwSkmvoZnRD2AXrbxcwmMpVFwCy4NYYpC3k20U8NJyMqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خرید طلا در روزهای پرنوسان از پلتفرم‌های آنلاین ؛ وقتی قیمت و هزینه‌ها شفاف است
🔹
در روزهایی که قیمت طلا مدام در حال تغییر است، یکی از مهم‌ترین مزیت‌های خرید آنلاین این است که کاربر قبل از معامله می‌داند با چه قیمتی طلا می‌خرد و در زمان فروش، قیمت معامله را هم به‌صورت شفاف مشاهده می‌کند. این موضوع کمک می‌کند تصمیم‌گیری برای خرید و فروش، به‌خصوص در روزهای پرنوسان، ساده‌تر باشد.
🔹
از طرف دیگر، وقتی هدف از خرید طلا پس‌انداز و حفظ ارزش پول است و قرار نیست طلا به شکل زیورآلات استفاده شود، خرید طلای سرمایه‌ای می‌تواند هزینه‌های مربوط به اجرت ساخت مصنوعات را نداشته باشد.
🔹
یکی دیگر از مزیت‌های خرید آنلاین، امکان مشاهده جزئیات معامله قبل از تأیید است. کاربر می‌تواند میزان طلای موردنظر، قیمت و هزینه‌های مرتبط با خرید را ببیند و بعد تصمیم بگیرد؛ یعنی به‌جای اینکه صرفاً در پایان فرآیند با یک عدد نهایی مواجه شود، از ابتدا تصویر روشن‌تری از معامله دارد.
🔹
به همین دلیل، پلتفرم‌های آنلاین طلا در سال‌های اخیر به یکی از روش‌های جدید دسترسی به بازار طلا تبدیل شده‌اند؛ روشی که برای افرادی که با هدف پس‌انداز طلا می‌خرند، شفافیت قیمت، مشخص بودن هزینه‌ها و دسترسی سریع به بازار را در کنار هم قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/686532" target="_blank">📅 12:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
خبرها از هدف قرار گرفتن یک کشتی دیگر در تنگه هرمز حکایت می‌کند
🔹
گزارشها نشان می دهد که یک نفتکش در نزدیکی سواحل عمان با شلیک سه موشک هدف قرار گرفته است.
🔹
منابع عربی مدعی شدند نفتکش مورد حمله، متعلق به عربستان سعودی است.
🌍
تازه‌ترین خبرهای ایران و جهان…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/686531" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9e369c4.mp4?token=u40Np99bDRo0EJaW-R_2Voaixu3bK0PahtsAGg015LEtLmEmWruVPVCXhTAYCm9_xpONlpixBnWu7b2KBaKh3bE2t54vcVyCGofxWIuU6ppDzw5AG4gAxaI1FiejHzQjco9bbjF4eKgVrN0nHPBv80jrtvN-DqoaYa1wOr_yWYaWyqoEY6Eja9xyOrjEfPpQsIJeBj6gkzfr9GvMS4REmMaQ59PevpoK91bc4PvGR7Yq3hHrTU8P0orWcBFA0EpuTdN5ipgolL0NCGjSHt3AXxmAXt0UAZz-rW4rwOAZWAL8ipC1r8_3yxFOkVrshth9gGvoGPwQjMyigSln-f-NLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9e369c4.mp4?token=u40Np99bDRo0EJaW-R_2Voaixu3bK0PahtsAGg015LEtLmEmWruVPVCXhTAYCm9_xpONlpixBnWu7b2KBaKh3bE2t54vcVyCGofxWIuU6ppDzw5AG4gAxaI1FiejHzQjco9bbjF4eKgVrN0nHPBv80jrtvN-DqoaYa1wOr_yWYaWyqoEY6Eja9xyOrjEfPpQsIJeBj6gkzfr9GvMS4REmMaQ59PevpoK91bc4PvGR7Yq3hHrTU8P0orWcBFA0EpuTdN5ipgolL0NCGjSHt3AXxmAXt0UAZz-rW4rwOAZWAL8ipC1r8_3yxFOkVrshth9gGvoGPwQjMyigSln-f-NLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۵۰ میلیارد مترمکعب بدهی به منابع زیر زمینی داریم
دکتر تابع جماعت معاون وزارت نیرو در
#گفتگوی
اختصاصی با خبرفوری:
🔹
ما در سال گذشته ۲۰ هزار مگاوات ناترازی برق داشتیم که امسال به کمتر از ۱۰ هزار مگاوات رسیده است.
🔹
شرایط آبی ما امسال نسبت به سال قبل کمی بهتر است، اما نسبت به درازمدت چنین نیست و همان کمبودها وجود دارد.
🔹
ما ۱۵۰ میلیارد مترمکعب بدهی به منابع آب زیرزمینی داریم که پرداخت آن سالیان زیادی طول می‌‌کشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/686530" target="_blank">📅 12:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
چین اجماع گروه ۲۰ بر سر بند تنگه هرمز را ناکام گذاشت
🔹
چین در نشست گروه ۲۰ در برابر فشارهای آمریکا ایستاد و با بند پیشنهادی واشنگتن درباره تنگه هرمز مخالفت کرد؛ مخالفتی که مانع دستیابی اعضای این گروه به اجماع بر سر بیانیه مشترک شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/686529" target="_blank">📅 12:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJspHxSu3b9xSIeOy-yd0ibQhzRlF52lN98pRuXbNfyTvdV3PaRSjk6r7KUuqyjODBkxdsw9blJXxWntkff-zUOU9rpVGpEA6JWmyUViV51P9nJv97EsVBbub_OLtmHkmn_s_H1_Vm3uggT_iyLesxAceiaa01IBiIkh7wwrYjd628-yf8w7ZxfkTnAFwMkxRCjmV7x74EaqDOXjnKdRt8CLjEa6ppohBl-D_11p8p8rh7RQ6_Aqs6E09-_wTRu0ik0jdhDzwR00iSq0z_bh0B7eEFsAJs8C0sl_O1Vyuif61thi72YJQ3aK4bK5sjuKDpNxOcOvCE_KYS7bVf18Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت دلار، طلا و سکه امروز چهارشنبه ۱۱ شهریور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/686528" target="_blank">📅 12:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfO3b3OxtkFRi3_CVRoAqcKcU7QqzCbyRR4Ntg94zMWnA4PwtFmqTj9PhyKK2KLYldNqApulJQwpo51BK3bwqMrQDOsZOKdOX689yFWYYUjlB1SqFuuWkFBiDaQ0Z7bwUmXfoTaTmXDfFWquYnDR98dZiTRQyeNaQyOaAceHrEM50dPV8QvABGo_g4fIK2A540leH-K0dhrNmK8b_-WNIH6Jw7vPhoop5C4YSVYN-2erK95XZ0NiORTq7Iseh9Vkc_Xe2SxatCRBkrg-osXUXohrJ_eo1_0ca1hIwPLkGUTroomupBiWCb92P_6GPskgfacR-2qXZz6tAivaOU7vHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686527" target="_blank">📅 12:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8SYTUGEgSMnakD3_9Ueg-0q4nSdkxWmtxqfAOyuiIFv8s0bqQBONQdQRFrxuFfjh4cyIpd2RXdYO1L4E4qI-6IYLcVAqClUAQc-uf5dHMoqZyM1dyNIEtL_6XDe-NI8a7ldsFM4yrCMpe_MEfvmQjLdPEjibmHu-O7ZiowagxSd7lGRkKF-A3VkCs1pRSH0IJy5ALVXb-K8ygFGdxFZtW91Iq-JFWFfZO_fd35Fwtf2yo_fOcB7cCOGlKpt9MHEqKNNcoPP2ef-JHoh4zwdJsqrzp4ek_MZXI3xF1tuTOByEwxyuQDubV922bxVZykjZ-e6TpTa6SwJb39GfIM2VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش بهنوش بختیاری به حمله ارتش تروریستی آمریکا به مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/686525" target="_blank">📅 12:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRS9Ut2Ne-FwCLPiUCTh1Wyg2ytEPzHNCVhYuayKFtRJwl-WsMPp0-lBp6Oq51aHExlTbV0ryz3HwN1XEG28q5YPlU8y-OQWuQsGfB7FHCbDtGxe3tzL6CRV2lKEsnsjyHxny_suUHldscslNJKf9jGmKn0OYgyIukUwipO4ET3bcGoCx3OpOoZIFjB2PL73ghPJozXN1GMlNeuBBXnENoyXQ_KW0w7pa7EJ7e5NeVFziGHZjMTlhFB7bGUbpyq0aVGV2Zz-MO8Z3CMHFVX5P8uml9edgjWAEVSSuqp3fHRGa_rhvZG2cGcTfFbVlzd3_UXL0qtN3iG4GN5p6f1ZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6TUhqDgIotrmvChED9iSatQOqpWyCvbQaeNjX20y7FKYYTxqaoltkQ9aS-VfxYmfuiKfeKrthr19rEwCNBUIYWhIRq7TSypbQF_MuBCLhmg-4l9myAv6OY_7CeWO5Q0DzPSfpm9DukYZaOf4pdl1iNFYtUQ7QpfWI2TXLL7Iq2TcrqdJ5tFva6jswcch7BCLOTbgy-jiMDVXrxCxvPOoX6WGrgakxfTJVyu3FiNIPnPDWk4nERTKlMkLpZWlBb7HnQuyVyja0eYKydyewkMYG9HopUc9MjP4br4Ud6BbxqCtobIlBOrsnIK0fVLhn23ZxhQb5muoBdxXo_ueCycqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پوستر باشگاه‌های استقلال و پرسپولیس برای شهرآورد
🔹
دیدار ۲ تیم ساعت ۱۹:۳۰ در اصفهان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/686523" target="_blank">📅 12:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768388c985.mp4?token=UiXwAxOE5jo6B3KfXagBzYXM7jgSY80yJ6wTAhGSOXbXM3QXblMBIutsvvWnQQ2r0bPR8Gcpr1FQ0iHEOlRNiChJm4pNNOz5nRC513mqzTAcDxs3l-cezwQe6buWKgJO1rU87BueN-XYKQJsd48HzBnO8j9bIpFGmXp6kHAltD9HK_d3sxzLjtkwlpciMUFgtQA5cyxt2vQtEOTUNjmXSZq2gdoZ3xeK9zmGI-Ndo6Z9Mtq_izpMuwVs9aFtMbKVPz_QaXEcdotMNk2QEQY9OAaweN02YQ5gEhk0zLE-2LkEYsJX3uFZp2QfOWqafv3jSvCQ2qu17wgAolYHTdQNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768388c985.mp4?token=UiXwAxOE5jo6B3KfXagBzYXM7jgSY80yJ6wTAhGSOXbXM3QXblMBIutsvvWnQQ2r0bPR8Gcpr1FQ0iHEOlRNiChJm4pNNOz5nRC513mqzTAcDxs3l-cezwQe6buWKgJO1rU87BueN-XYKQJsd48HzBnO8j9bIpFGmXp6kHAltD9HK_d3sxzLjtkwlpciMUFgtQA5cyxt2vQtEOTUNjmXSZq2gdoZ3xeK9zmGI-Ndo6Z9Mtq_izpMuwVs9aFtMbKVPz_QaXEcdotMNk2QEQY9OAaweN02YQ5gEhk0zLE-2LkEYsJX3uFZp2QfOWqafv3jSvCQ2qu17wgAolYHTdQNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا زندگی نزیسته‌ای همیشه زیباتر و جذاب‌تر به نظر می‌رسه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686522" target="_blank">📅 12:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686521">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7gA7-KFvsMY6q1jCd3-PUAK-3hnraNgYHgTZGQJUkHcHBJZwrhTer-W60eZ076H-7DgsfOwXfpyHqDvOOPQlNx-MmxyFrA-S2RYb89ln5e6b9K4UFjbN0tu5mZvOkhguP6jed5bUuP2vXCShE1IEYGh_B-2DERxoNcJkjQ1C5dx7SMUIfznhlDcvlZGZFrwduOrFGQ1HwludNqJKu7Wxg0UMbYNmn4_CT4QuDyteb_sQ6X4Lm8m-7z92k0GRz8VnBIAYqx3WAhGgD3zs6tyf2zBb0IhIgIhCVWshWPN-vJeF3lL36IiA-z5GyW5_efImCt8pTBzoVGB2Z8VEuTNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686521" target="_blank">📅 11:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686520">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRTSRPUc1PvtsWCCuFHX_q_yLRyuF2fZk1_zgE36ehuKsHKcpq430qQBaxrUG3G6LTltNW5yTaHt7WHiI8l3Xj_zn9ozM2oINdCkoMSFdL4lSxD9vukaJO7DPdQluVog4Agk3XHkNMRmezvwXs15_i1EduLh-Pn9yQM4ZoX3w-FvdTs7JZGK-yoFyQhhH9oJPHTopqo0fTwt2dqVEJfELXNsL6BcMwreLEQXKEYcwIo9Kis20htnZS-JBE_bX1505dgRIiT8Fb3vM0iU_CBRW5ari7lX7UD8pkycgIsuyU8JB21RV_nTuq2kGND-EFJk70xcSOCzsaulk-Lz9LjQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه خبرنگار WSJ به ترامپ: از «کمک در راه است» تا «چه زمانی مردم ایران قیام و مبارزه خواهند کرد؟»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686520" target="_blank">📅 11:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686519">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تکذیب ادعای شروط چین برای توسعه روابط با ایران
🔹
دفتر نماینده ویژه ایران در امور چین، ادعاها درباره مشروط شدن سفر و گسترش روابط تهران و پکن به شروطی از سوی چین را رد کرد.
🔹
این دفتر تأکید کرد روابط دو کشور بر پایه منافع مشترک و مشارکت راهبردی ادامه دارد و خواستار پرهیز از انتشار گمانه‌زنی‌های تأییدنشده درباره روابط خارجی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686519" target="_blank">📅 11:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f85b4a48.mp4?token=LvSRJsRf8WWEc7eVraDzE2ePfzZOgDzQK2T5MdPk1ewmhOvih2DHHJ7xYm70hzy7KDvccYDB7hW-IhLACozpVlFWabvjYdxd17jg0lNvm_BTredH3NqpaIEJUNYNBs2aRrfiO6JNpBQoNYR5eBjI-JtpqES34tyeuqEay6xT6hZF-0xFlPdrg5qRiVj4V9-0TAYy3arZZ9XANZiKgkGAudRqlDi1dyr6_ll5LgeyDQP5kdMYITVMEVxRS9xG4K4Clt5awREpHfG9TQeXI8VE6zrSVlpT_ilSsiQbYGwz2MVtLNEZG65nyfG6LKns3o0SAqczm2u-dySZNtm--nSnKjh8G-5v4yb4vfv2ZBCvsK0dCsYnH_D3rYL2EXSllfOZpzlgeXT0pDxuAAxmtVLUttoYEFw5mWaje_yLRQGdiZQZm3zSuRq7YBrJFuvi6SMs6dE4uWhm77Id_Aaimp4xzFPw_PkDl3timmqTRGPUc6KT6zAJHrt5B2xgNTxC9v63TDWHZC7LnAMJbBUbHhyCeKCwLGycVyKgoGhuBKUOTjsjswdEL1RZew7gOB4rZVrcH_wc709yFAZHg_MMgRSl99IiDdDtTm4G4J1jvfN3wVXkR4Dgd6B6wxaKgLrEzONKGqmUqor9sttcEFHum8c4ENsJ2e5vZVubCyPXVLFv900" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f85b4a48.mp4?token=LvSRJsRf8WWEc7eVraDzE2ePfzZOgDzQK2T5MdPk1ewmhOvih2DHHJ7xYm70hzy7KDvccYDB7hW-IhLACozpVlFWabvjYdxd17jg0lNvm_BTredH3NqpaIEJUNYNBs2aRrfiO6JNpBQoNYR5eBjI-JtpqES34tyeuqEay6xT6hZF-0xFlPdrg5qRiVj4V9-0TAYy3arZZ9XANZiKgkGAudRqlDi1dyr6_ll5LgeyDQP5kdMYITVMEVxRS9xG4K4Clt5awREpHfG9TQeXI8VE6zrSVlpT_ilSsiQbYGwz2MVtLNEZG65nyfG6LKns3o0SAqczm2u-dySZNtm--nSnKjh8G-5v4yb4vfv2ZBCvsK0dCsYnH_D3rYL2EXSllfOZpzlgeXT0pDxuAAxmtVLUttoYEFw5mWaje_yLRQGdiZQZm3zSuRq7YBrJFuvi6SMs6dE4uWhm77Id_Aaimp4xzFPw_PkDl3timmqTRGPUc6KT6zAJHrt5B2xgNTxC9v63TDWHZC7LnAMJbBUbHhyCeKCwLGycVyKgoGhuBKUOTjsjswdEL1RZew7gOB4rZVrcH_wc709yFAZHg_MMgRSl99IiDdDtTm4G4J1jvfN3wVXkR4Dgd6B6wxaKgLrEzONKGqmUqor9sttcEFHum8c4ENsJ2e5vZVubCyPXVLFv900" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واسم رخت عزا تن کن/ همین جا شمع روشن کن
🔹
به یاد عروسی سیریکی‌ها که عزا شد  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/686517" target="_blank">📅 11:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/686516" target="_blank">📅 11:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49960f924.mp4?token=pKJoN5hewcIzN-Ao4C1vTI73rqvCSzylL6sKUhyNNjBWDT9YVMnh8L1I2GFVdg9aruWJRXXaHyBX4Ipe1HPzlHxP9v4KW1l90PawEK-j4RLj10J2ZElvcodVZCWIzO3_DdLdIynxUw4Px4qgi-cEfNUkYz-uguO6qCRyG787rocnfNqettOOEovozJwOk51kyn93MoZqBayBbopWPGDx0aJ1F7iuL_oLrk9zmqQSeaslLTT6x_x81goJNmAxQblVdk6lHDLIFVumDUQt0uny6dWwUPVbiFF8LcMr7ka7-7MjI9FuV4UGY7xPJNirTC8kqV4VcJDcCTki3m8lPCqNBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49960f924.mp4?token=pKJoN5hewcIzN-Ao4C1vTI73rqvCSzylL6sKUhyNNjBWDT9YVMnh8L1I2GFVdg9aruWJRXXaHyBX4Ipe1HPzlHxP9v4KW1l90PawEK-j4RLj10J2ZElvcodVZCWIzO3_DdLdIynxUw4Px4qgi-cEfNUkYz-uguO6qCRyG787rocnfNqettOOEovozJwOk51kyn93MoZqBayBbopWPGDx0aJ1F7iuL_oLrk9zmqQSeaslLTT6x_x81goJNmAxQblVdk6lHDLIFVumDUQt0uny6dWwUPVbiFF8LcMr7ka7-7MjI9FuV4UGY7xPJNirTC8kqV4VcJDcCTki3m8lPCqNBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشر شده در فضای مجازی از حمله ربات به انسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/686515" target="_blank">📅 11:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بیانیه ۷ سپاه: انهدام محل اسکان فرماندهی ارتش آمریکا در پایگاه علی السالم کویت
🔹
هنوز از سرنوشت فرمانده پایگاه آمریکایی علی السالم خبری منتشر نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/686514" target="_blank">📅 11:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سندی از جنایت آمریکا در حمله به مناطق مسکونی
🔹
وسعت حمله ارتش آمریکا به مراسم عروسی در سیریک   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/686512" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
‏
خبرنگار صداوسیما: محل عروسی دیشب با سه موشک هدف قرار گرفت؛ در کف یکی از اتاق‌ها گودالی ۱.۵ متری ایجاد شده است، ۶۸ تن از مجروحین بستری و حال ۶ تن وخیم است و چهار نفر هم به شهادت رسیده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/686511" target="_blank">📅 11:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686509">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcdN-FccXV3HmBCwXvSZOdSpg8RRSVeKnvE9JAMUgH3CMZ0NhvzQLyT-YndLKi5wIorFbtJx7eXk2LY5GpnWQIVe15SrpTD0AV_-LGpf0ihjFRa20B9YjGO6D2pIitxXzt88_I7RpPBP-ApA_fp_JN_auAatpnax70F9Dd6-OcXxerZCmWBCp2VZCK4hhar9L-9dkVyMo5-5W6s8AEWKUmbixBwEfLKsRiI76Q9wD6PbjeR6SJP05knZmUVVC2XkINC4bptB5_Jp5rZuAcsCSEjdpcyg0LWx7O2HmsljskotyktvMT4vt2HAmmLXAN0PvgMGT_W4IXOgAYFUWiTzCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جیمی بانکیویچ، فعال سیاسی امریکایی: این جنایتکاران حتی به بمباران مدرسه دخترانه در ایران هم بسنده نکردند. حالا یک مراسم عروسی را هم به خاک و خون کشیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686509" target="_blank">📅 11:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJLvTdFo63L09Sv-OI8a8aMgx0Qa602YEfMT1l4Ziz7Cp_Uo5tLJzIGDT6fa3YdRGTFf7xrc7gha3HLf9cyc0k3xty8sulMtYBQa3g6IC4SocaQaZ-r4dc1rx9ZrTdiGndz5b3f_YsHZRMr_OsP25v0F137nHkivaH7PARtOweW9YmJSJkbHGPXUz063zuMcV-Fx60CbueWHb4pcyz1Jztn51HkwSN5abJuhIIHv_H3MDh0aFAmYpM8K65tdNBa07NVifqPYNod2xZfZ7IR7bKILsIx_LQE8I4N6X_ZFLF6m7gUn7DHELAY_-YOgf4eJm8026qZO1tm5UGlVdT5cFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hB2jbkJ7CzKShsjx6v8at9YYuI1DXXCgGsTZ8hABMjjWhC2e8rCBjLEi8ymgX704QyDvjq7bIEK16NadiWfzEuquwMGPFn9bu-w7fGrD6Hyd_0tnPPfeRmVdNQgcCRgP610hqMpj4hB_3tONPjXFxK7VnUynwry9ZCCHK2juCTS21wTXxaCo6wjRWNZW9WksVz9leWtGf-7fLt01Az1-yhmD5X0WyrgVjSqVEbmWnmafiBzxmec95Y4cIh5OwtLGvyjClzaWZdnIz4JYk6ViLqwB4KQzgYUTOtXc3DHwFm8QFMbAd6F65IvwT0A82DuStSa9PilFLhM1iiL6jG8eEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PhJkvEc3KLxAyeaQZ2euUm1XsRlsmFVAU_XIaxe34P34ImA6Eq47TEHbua6V8xv0UNdhSXnSli1lB-CDXOf90taUzPfnsnILoDoVxwEGjhHE_BaiSVbML-9W-QOxsZkPrEoBmZuyHWqxXxJe0bdNAVYiM6jvYH6V_NqRYfwZezI9Mqych7e1BuwZp4CQ17_foxqtuRQuxcTF6sqKAz5MswM4x8SCuoVkvyYd7GLDFM4KSHNUJq5oiNBb7RW0hCPsTXZTKVg0sWaOF2vM0BDj0W8Nm0ojSlGNLTsnIR2YyIbFh_hX-BjojPPLK6XVIXwxcFFwzZ0_FAqGXoA0L49o2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فاصله بین دکل مخابراتی و محل عروسی در کوهستک سیریک حدود ۱۳۶ متر (۴۴۵ فوت) است
🔹
سلاح‌های هدایت‌شونده رایج آمریکا در شرایط عادی خطای دایره‌ای محتمل حدود ۵ متر دارند. حتی در صورت اختلال GPS هم معمولاً تا حدود ۳۰ متر گزارش شده است.
🔹
این فاصله برای توضیح «خطای محاسباتی» در هدف‌گیری یک سلاح دقیق، زیاد محسوب می‌شود. با اطمینان بالا می‌توان گفت جنایت جنگی اتفاق افتاد./ خبرنگار CNN
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686506" target="_blank">📅 11:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سخنگوی سازمان لیگ: ۶ هزار زن، تماشاگر دربی ۱۰۷ خواهند بود/ درهای استادیوم نقش جهان ساعت ۱۲ باز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/686505" target="_blank">📅 11:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5daa76fecb.mp4?token=WRQT6_4GpEx8zT93t6AuX3xfC9EsW66-ltJnbFZvQftMq8Zp-JjoOrQkgAwa4C4whN1mCnBV-4J_XiW8HNe8-07W1diHZkMjpiF-Ncfbya4OqIuLm_8LYAaPiSRKC53slqMR3Jjzh0kOwq55jyIJrq-xNrXLikkObIG3wTznNcN8Al3SVPTNcox3qKH4YqQNsQLdoskk2iVlWcxEDSXj-6xA5_6gWaNRRzLWkJvM-xIgVAsUN_6tzq0gAodAdgqwnbx4d6G6iqpDQrlWN754C5vhP61uuP2EOIlQTof87HtDWnXOkENDNBu24QC9BzRr5n0qHVBdBJV6OiUk6Yqx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5daa76fecb.mp4?token=WRQT6_4GpEx8zT93t6AuX3xfC9EsW66-ltJnbFZvQftMq8Zp-JjoOrQkgAwa4C4whN1mCnBV-4J_XiW8HNe8-07W1diHZkMjpiF-Ncfbya4OqIuLm_8LYAaPiSRKC53slqMR3Jjzh0kOwq55jyIJrq-xNrXLikkObIG3wTznNcN8Al3SVPTNcox3qKH4YqQNsQLdoskk2iVlWcxEDSXj-6xA5_6gWaNRRzLWkJvM-xIgVAsUN_6tzq0gAodAdgqwnbx4d6G6iqpDQrlWN754C5vhP61uuP2EOIlQTof87HtDWnXOkENDNBu24QC9BzRr5n0qHVBdBJV6OiUk6Yqx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سندی از جنایت آمریکا در حمله به مناطق مسکونی
🔹
وسعت حمله ارتش آمریکا به مراسم عروسی در سیریک   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/686504" target="_blank">📅 11:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الکامپ امسال، یک تجربه متفاوت در غرفه بانک ملت؛
از «دیما» و خدمات دیجیتال تا صدور آنی کارت؛ فناوری را اینجا باید تجربه کرد، نه فقط دید.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/686503" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a47d746d.mp4?token=g2Py-lT7s5nO00ik5aHrDvHmCpXr1Pol6M22c2Gw0h2YJpFRlALBxGseFZIybEpL--Vkl8SJgo_3udTlH3ONwq1FWCe1Ci5KKQH6RcdoTcQ94f2JoYe_TH80WQdEvGaTAhtM8g6NGp9qJbyKXAA6_tkrA6YmaU7rZ4FMrucL4svFHc3ArFQQrGjgQueXbN58gYsAGrRPsm7FOXLgx-LUDmcZ4EeMIIiM8dYm2Wn8N4ndHcq4z5dzZZ4PUr9KigWk6VmCr1wRTtzFMIT1Np_KZnBXUz_bywX3xUinCqIQTaI5QnifYJ_4KChb0agZeF80XZxt8P8flFPW11lj5M2tkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a47d746d.mp4?token=g2Py-lT7s5nO00ik5aHrDvHmCpXr1Pol6M22c2Gw0h2YJpFRlALBxGseFZIybEpL--Vkl8SJgo_3udTlH3ONwq1FWCe1Ci5KKQH6RcdoTcQ94f2JoYe_TH80WQdEvGaTAhtM8g6NGp9qJbyKXAA6_tkrA6YmaU7rZ4FMrucL4svFHc3ArFQQrGjgQueXbN58gYsAGrRPsm7FOXLgx-LUDmcZ4EeMIIiM8dYm2Wn8N4ndHcq4z5dzZZ4PUr9KigWk6VmCr1wRTtzFMIT1Np_KZnBXUz_bywX3xUinCqIQTaI5QnifYJ_4KChb0agZeF80XZxt8P8flFPW11lj5M2tkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روز دوم حضور طلاسی در الکامپ ۱۴۰۵
🔹
در روز دوم نمایشگاه، بازدیدکنندگان از غرفه طلاسی دیدن کردند، با خدمات و محصولات این مجموعه آشنا شدند و در تجربه «یک ضربه طلایی» شرکت کردند.
🔹
طلاسی تا پنجشنبه در
سالن ۸ و ۹، غرفه ۵۴
حضور دارد.
#طلاسی
#الکامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/686502" target="_blank">📅 10:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzoaGaXUQQH47s9LMer38p21Ck9_somxHRlpTeSry44rSvLcFCryZrH07GFX144vBDbWKg-3fHEu22RbGAj0T5T_FF7Cyh3mCiCYcAqeJIuvqiAcQq_9jsi832J_2ornjQO4mpHsteX3x70RJbW3lGQgU5EpXJ3cTZPBmyadVZk1ljkXjj1f8YbJpeFoZyg_uCjGLHnN1vkA5ZqEy2ON3OQ5UhrQGZF_B8jeDeQutIP0yErLwwRYwuu-prXty9_4W0S0bekG_7Wi65O1ZmLldPf_V3J4wqYwFyv57cPud7c8uLtGMbFptMYqztSzh_aiOPEixISHZqaF0mZzg7zSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: تمام اقدامات آمریکا به تقلید از شیطان و خود آمریکا شیطان بزرگ است
🔹
مدرسه میناب: کودکان قتل‌عام شدند.
🔹
سالن ورزشی لامرد: بچه‌ها سلاخی شدند.
🔹
عروسی کوهستک: کودکان همراه با خانواده‌هایشان کشته شدند.
🔹
اگر قدرتی مثل شیطان عمل کند، مثل شیطان هدف انتخاب کند و مثل شیطان بکشد، آن قدرت شیطان است.
🔹
اگر همان قدرت، شیطانِ کوچک‌تری را که دقیقاً همین کارها را می‌کند حمایت و سپر کند، آن‌وقت خودش «شیطان بزرگ» است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/686501" target="_blank">📅 10:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ac3698c4.mp4?token=e2a8TCzL0i-wwKu2kTF7RFe59yC52I3ilsDuBHa0Zv75tGGkSOH-aK0wUYO9_VHK9n1Z4n-nWQj9pgbzak-H7Cc2Yink3HL4DLwtn3LgrTpZqcUnoX6yXRnPHBMCjWbuHlwj335p4zXrrsTErnkOm1r_XN_3nSYILEhiplBpnnVvjUtYzlx4hlEM9ELlHW6Uz4cSfAeQGUf3CPNycE7xK7gxrv7pYEoH1Rbm47qXDhMefXNC8fs9H2Q4h5OBIbHOdA4HlivM_OXtI07MPohNx8Hbrwc3u4fTbjb1O3FHBRl2lU55Ar3X2uuvhonaCW0hbiD9owhl2V9kCiB4bg9I7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ac3698c4.mp4?token=e2a8TCzL0i-wwKu2kTF7RFe59yC52I3ilsDuBHa0Zv75tGGkSOH-aK0wUYO9_VHK9n1Z4n-nWQj9pgbzak-H7Cc2Yink3HL4DLwtn3LgrTpZqcUnoX6yXRnPHBMCjWbuHlwj335p4zXrrsTErnkOm1r_XN_3nSYILEhiplBpnnVvjUtYzlx4hlEM9ELlHW6Uz4cSfAeQGUf3CPNycE7xK7gxrv7pYEoH1Rbm47qXDhMefXNC8fs9H2Q4h5OBIbHOdA4HlivM_OXtI07MPohNx8Hbrwc3u4fTbjb1O3FHBRl2lU55Ar3X2uuvhonaCW0hbiD9owhl2V9kCiB4bg9I7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سندی از جنایت آمریکا در حمله به مناطق مسکونی
🔹
وسعت حمله ارتش آمریکا به مراسم عروسی در سیریک   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/686500" target="_blank">📅 10:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تصادف عجیب در اتوبان ارتش، تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/686499" target="_blank">📅 10:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا شکیبا و شهید جعفر کهریزی.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/686497" target="_blank">📅 10:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyDJemRSpZtVxhtkO2ojoMi595lZxGfnwOjtfvhC9kNYR7Q-AiE7J-StV-ONbdkMEZCasRMtBF8Is1EO23p1Rqg0zXUR18T7sI4STIEVzNjxh5YLjJfynsf0jurZKTC0LvFoldyXHCoLrrAMHOv9gc2G2iP-o1-hXgCvDs01PNo3b8QCbMc6zPoithDvLtKfq6UapaDIXvZg0blD4zz8Kzlw6wuU4XKItbmBNdUUiPT3tpFJzG8_nrEgd4U4-jhKEtHOGrPHTz2HwnbTEcxjKRtQsQB5j6SSffCRQLM8OzzPnF2Qm3Jiu7ir6OtvGDKrCBc_Jywxi8OQrgbRK1Y8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری رضا صادقی در واکنش به حمله ارتش تروریستی آمریکا به مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686496" target="_blank">📅 10:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
۳ رزمنده بسیجی شهرستان دیر در جزیره لاوان به شهادت رسیدند
جانشین فرمانده سپاه سیدالشهدا(ع) شهرستان دیّر:
🔹
در این تهاجم ناجوانمردانه، شهیدان والامقام «مهدی بحرانی»، «حسین صالح‌نژاد» و «حسن مؤمنی» به فیض عظیم شهادت نائل آمده و تعدادی دیگر از نیروهای مدافع امنیت شهرستان دیّر نیز مجروح شدند.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/686495" target="_blank">📅 10:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19494596d8.mp4?token=kMw-oSYpFc0RkPI845haplHAaqZKLkqIkNSdFia9OOhfMvBf_rYm6SOnqBMh68MC9Ldr7eYl5LpOwsizIIPKHfEfkeUrWiuwpvOtq_6xQa74w2ig9442c8dxUtr51jf-yYs5wnfV-ShpQ7VHI2JqHAW4iSrwXivhNkRVh14yHVZ5E84rkhIsiSPYtx4O0qYB4lcrC_bCuextG1dZEL1tr91VadMqFJQ-G-oAO0CxrGzzxA8ykuEVHl0CmG5H9M1IZDTrxtT80rrhNDn7tdq-RIS6znhI3N8tEo44csaPoG-c0mCZ_UP_BFgwpSYRhUcwTSvWhPKTMq3h2K6px2Vlag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19494596d8.mp4?token=kMw-oSYpFc0RkPI845haplHAaqZKLkqIkNSdFia9OOhfMvBf_rYm6SOnqBMh68MC9Ldr7eYl5LpOwsizIIPKHfEfkeUrWiuwpvOtq_6xQa74w2ig9442c8dxUtr51jf-yYs5wnfV-ShpQ7VHI2JqHAW4iSrwXivhNkRVh14yHVZ5E84rkhIsiSPYtx4O0qYB4lcrC_bCuextG1dZEL1tr91VadMqFJQ-G-oAO0CxrGzzxA8ykuEVHl0CmG5H9M1IZDTrxtT80rrhNDn7tdq-RIS6znhI3N8tEo44csaPoG-c0mCZ_UP_BFgwpSYRhUcwTSvWhPKTMq3h2K6px2Vlag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس می‌گوید با فرا رسیدن آخرالزمان موافق است و اگر دجال در میان ما قدم بزند، شوکه نمی‌شود
معاون رئیس‌جمهور آمریکا:
🔹
در حال حاضر، سعی می‌کنم تا حد امکان بر انجام کار خدا تمرکز کنم و اگر این کار در نهایت به آخرالزمان منجر شود، اشکالی ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/686494" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رویترز: آمریکا جای چین و روسیه را در نفت ونزوئلا می‌گیرد
🔹
منابع خبری ترکیه: دو کشتی در دریای مرمره در سواحل استانبول با هم برخورد کردند و ۱۰ نفر مفقود شدند
🔹
سی‌بی‌اس نیوز: ذخایر نفت آمریکا به پایین‌ترین سطح در۴۴ سال گذشته رسید
🔹
استقرار گسترده نیروهای حشد شعبی در مناطق بیابانی غرب استان الانبار عراق برای مقابله با داعش
📲
⁣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/686493" target="_blank">📅 10:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaMxNy8K7OGYnzIAhD0sGIz3Zak_Ia12e2w2FFGH_wZx3KLZ6hjqaG7or2NP-lQVNqaLi5khivUz02EcVOmzhGTnSWSu7a9tkZH9dqgsqxCv6xdoB8axIL7ZWx4hFuqyqmGsEm6k9fsozLCrv-R3rQ8QvBi9jmmO8_a7s0KuSR-jQ3qjALQDGN58Gk2jYkhJRnqVKGW_Fk_2I3pVhLUamcLiRcBJvZGWTIs2pclFrNutBRxGKfr_hWmASe3KHugcabkwV0qctKqEtipHdyn7_lJr0koER_Vr91lq2LpdRoFYZy7ei8Q9ZOVQaqIMeqcBGROSh9n6TsygAVkeXPJFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکاور بهمئی در عملیات مقابله با پهپاد متجاوز به شهادت رسید
معاون فرهنگی بنیاد شهید کهگیلویه‌وبویراحمد:
🔹
سید مالک موسوی‌تبار، متولد ۱۳۷۰ و از اهالی روستای تنگ‌گر بخش ممبی شهرستان بهمئی، صبح چهارشنبه ۱۱ شهریورماه در جریان انجام مأموریت و عملیات مقابله با تحرکات پهپاد متجاوز به شهادت رسید.
#اخبار_کهگیلویه_و_بویراحمد
در فضای مجازی
👇
@akhbar_kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/686492" target="_blank">📅 10:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4265d064.mp4?token=vgG76nqQlLObtiSn6_uyrMN0q6bRPrHEUmGxhgwKP0M5Spip1key9MJ-ZMaa_6gl05LYLiEoK_Ckn3P9Rhycv8-r12i-SKaogima-zB3NFhYCDhdGZDgo6txEPUcGoPsC_P5e41WKhCP93IOnf9FOoLE9RlpXwkfE6welGWznqt8x6AzQWiPWxvbspcIkVhikKnL0bv2_KAIh7NNpLm3a6iHKnNEYqPTFtsm1ZNkTIxYYjgwVV-ArTEUxA5oP7_y-Wy9JflJSxvny3iDI4Ulco5NHK9gYSjLI-_J3lkI5fewJ6iwjN0EOby2Gwtqys5QGl1A15Ikk_dE-vCcRCkAxKgSF-4aV_fzRbvoe6tXOD3xZdtn7YAEhrJ9IoWSIzB5nQmetnrxUNtN7qyY1q2CYFcYRJHB1VXVyeHSz4IqUsRFpknH62DbGsjPMdug5Tqyb1-jo8yxa-scRksreqqZZG99GPkcrNJFF7IcSuioUSP9C2NPiRHTEZIruPq9zDDIkDChSMK8FbxaQXp4fj26lmgRGFrdqELUIFTXITd6E4VZfusP439uLbWE9OCNV8vlPld0vKgs3E3ryxpXXPvRkyPcTg6wVnWC5H_4eX2UtvSQfrWMRLpasOt8g7K51VhPw4vTGq7MNFpTqQhzduAkMZ2MInKdyfndB5-nHRarRXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4265d064.mp4?token=vgG76nqQlLObtiSn6_uyrMN0q6bRPrHEUmGxhgwKP0M5Spip1key9MJ-ZMaa_6gl05LYLiEoK_Ckn3P9Rhycv8-r12i-SKaogima-zB3NFhYCDhdGZDgo6txEPUcGoPsC_P5e41WKhCP93IOnf9FOoLE9RlpXwkfE6welGWznqt8x6AzQWiPWxvbspcIkVhikKnL0bv2_KAIh7NNpLm3a6iHKnNEYqPTFtsm1ZNkTIxYYjgwVV-ArTEUxA5oP7_y-Wy9JflJSxvny3iDI4Ulco5NHK9gYSjLI-_J3lkI5fewJ6iwjN0EOby2Gwtqys5QGl1A15Ikk_dE-vCcRCkAxKgSF-4aV_fzRbvoe6tXOD3xZdtn7YAEhrJ9IoWSIzB5nQmetnrxUNtN7qyY1q2CYFcYRJHB1VXVyeHSz4IqUsRFpknH62DbGsjPMdug5Tqyb1-jo8yxa-scRksreqqZZG99GPkcrNJFF7IcSuioUSP9C2NPiRHTEZIruPq9zDDIkDChSMK8FbxaQXp4fj26lmgRGFrdqELUIFTXITd6E4VZfusP439uLbWE9OCNV8vlPld0vKgs3E3ryxpXXPvRkyPcTg6wVnWC5H_4eX2UtvSQfrWMRLpasOt8g7K51VhPw4vTGq7MNFpTqQhzduAkMZ2MInKdyfndB5-nHRarRXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فقط نیم‌ساعت وقت داری این غذا برای خودته   مواد لازم:
🔹
پیاز
🔹
سینه یا ران مرغ تکه شده
🔹
فلفل دلمه‌ای
🔹
زرشک
🔹
رب ‌گوجه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/686489" target="_blank">📅 10:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند تاسیسات و چند بالگرد
🔹
پایگاه پرنس حسن در اردن
🔹
نوع حمله: حمله سنگین با موشک‌های بالستیک
🔹
هدف: آشیانه پهپادهای RQ-4 و MQ-9 و زیرساختهای فنی
🔹
نتیجه: انهدام پهپادهای آمریکایی؛ هلاکت تعدادی از خلبانان و خدمه فنی؛ آتش‌گرفتن زیرساخت‌های فنی
🔹
پایگاه‌های آمریکا در اربیل عراق
🔹
نوع حمله: حمله تلفیقی موشکی و پهپادی
🔹
هدف: مرکز تعمیراتی، انبار تجهیزات فنی، سامانه هدایت بالن جاسوسی و مخازن سوخت
🔹
نتیجه: انهدام مرکز تعمیراتی، انبارها و سامانه بالن؛ آتش‌گرفتن مخازن سوخت؛ کشته‌شدن تعدادی از نیروها
🔹
پایگاه علی‌السالم در کویت
🔹
نوع حمله: حمله تلفیقی موشکی و پهپادی
🔹
هدف: قرارگاه و محل اسکان فرمانده آمریکایی، آشیانه پهپادی و رمپ استقرار پهپادها
🔹
نتیجه: کشته‌شدن تعدادی از نیروهای آمریکایی؛ انهدام آشیانه و رمپ؛ انهدام تعدادی پهپاد
🔹
پایگاه نیروی دریایی آمریکا در بحرین
🔹
نوع حمله: تلفیقی موشکی-پهپادی
🔹
هدف: تاسیسات، تجهیزات و نیروهای آمریکایی
🔹
نتیجه: هنوز جزئیات کامل به صورت مجزا اطلاع رسانی نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/686488" target="_blank">📅 10:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57450f310.mp4?token=l-jpTY5G-jT4ll9pLTZg3xygvBevot67kj3ZtGmLA0cH2kjgOD24eJ9RjE88fPvzcpO4s-iBxElU5WBc_4aSJ3_1STxFwGPx6aBxltaeoTC8DL439-lryYirAc_tJho6vea_mpiWIdAL0R0mm0tyvnb3lmVHDoNJkV-yf8lrV37L4ECK-lyCyllCYylbbq8eL_lfbHfR1fvbWrlLTueukWDV2DlqfUTENSA4UwWgU7ldhYNfB5bLw_IAp9pW6cQk9aFZY43oCeZRwj0wY5lQ_4r3PFooapIvERhDJm-V6zgRzli-RBsTbeAWIol2i359sfuLwhe11BKsPUNSYGXLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57450f310.mp4?token=l-jpTY5G-jT4ll9pLTZg3xygvBevot67kj3ZtGmLA0cH2kjgOD24eJ9RjE88fPvzcpO4s-iBxElU5WBc_4aSJ3_1STxFwGPx6aBxltaeoTC8DL439-lryYirAc_tJho6vea_mpiWIdAL0R0mm0tyvnb3lmVHDoNJkV-yf8lrV37L4ECK-lyCyllCYylbbq8eL_lfbHfR1fvbWrlLTueukWDV2DlqfUTENSA4UwWgU7ldhYNfB5bLw_IAp9pW6cQk9aFZY43oCeZRwj0wY5lQ_4r3PFooapIvERhDJm-V6zgRzli-RBsTbeAWIol2i359sfuLwhe11BKsPUNSYGXLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اولیۀ حملۀ دشمن آمریکایی به محل برگزاری مراسم عروسی در بندر کوهستک سیریک
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/686485" target="_blank">📅 10:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c68a0f4c8.mp4?token=EDg0w_zbxDKGQB-1K2znJw53UrMHnq6riwZYxesg6QFdSXyeCnHR2GSze8_cGl2Hx3W04iTiYTRS0IqSkj_q_XtAp1tm5lTdkYOL5Rf5VJdyBjMlG6e7pjW-P5K9CO0R4ilUj8ncAku8SRwt4fwDpfxZQZwLs-xchiGGiss8VfoCN2TQN7GvzqYLMSyfW65zZ8Vu7PJQ3jFFRdYSiSiStCwywUiaZ8lda6CjkkBA4PenJdlbt93gZAF2Mt-7nMgmAb3y6GKymb8nfkFI1UFAwUnFWgkOojRxx2g8B3SCF3c4aDDXpph98gyAGJ3YEUwoUN5WFXki1IopNfgO3GptyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c68a0f4c8.mp4?token=EDg0w_zbxDKGQB-1K2znJw53UrMHnq6riwZYxesg6QFdSXyeCnHR2GSze8_cGl2Hx3W04iTiYTRS0IqSkj_q_XtAp1tm5lTdkYOL5Rf5VJdyBjMlG6e7pjW-P5K9CO0R4ilUj8ncAku8SRwt4fwDpfxZQZwLs-xchiGGiss8VfoCN2TQN7GvzqYLMSyfW65zZ8Vu7PJQ3jFFRdYSiSiStCwywUiaZ8lda6CjkkBA4PenJdlbt93gZAF2Mt-7nMgmAb3y6GKymb8nfkFI1UFAwUnFWgkOojRxx2g8B3SCF3c4aDDXpph98gyAGJ3YEUwoUN5WFXki1IopNfgO3GptyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسواک ۵۰۰ دلاری Dyson؛ هوش مصنوعی حالا داخل دهان‌تان را هم می‌بیند
🦷
🔹
این مسواک با دوربین ۱۰۰ هزار پیکسلی و هوش مصنوعی، داخل دهان را بررسی می‌کند، فاصله بین دندان‌ها را تشخیص می‌دهد و دهان‌شویه را دقیقاً همان‌جا می‌پاشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686484" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686483">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
جزئیاتی از حادثۀ خونین بلوار وکیل‌آباد مشهد  رئیس پلیس راهور خراسان‌رضوی:
🔹
این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
🔹
این خودرو با یک دستگاه خودروی چانگان که در مسیر…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/686483" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlMA_0YoVpPmzR7H1glzuBrM2kGjgalhkE7VqtgEc8Wtv7rspMDYfcxH2MBhJTU5ORVF8X6WUbWjtFYeCp7iQaJq4RSY6lIJJFKRrBX92sY3oLDMKn1_LWWfxJFk_C8VpyMd68Iq0ibKTKj0qGmJIul4fnxoTKZ2wXd8DK5s8-6ZX4lpCxrHpdsu7AqvadIKbda59VJtCFtmpHoQdSlmA9uoFXh7ROLj4Cn2e6DR2iga0BqVI9TMS__9Ds-_0AIjaDMENCSDMJM0arpc8ZQABGLcODTcKDuDZvq42RopLsT4mV97E_Ba-wY_geAUWJLfnjIQjEkAKX547ecvfRxkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک توسعه صادرات ایران؛ الگوی موفق در بانکداری اسلامی
🔹
بانک توسعه صادرات ایران بر اساس ارزیابی دبیرخانه شورای فقهی بانک مرکزی، در سی‌وششمین همایش بانکداری اسلامی به عنوان بانک پیشرو در اجرای بانکداری اسلامی در سال ۱۴۰۵ معرفی و مورد تقدیر قرار گرفت.
🔹
این تقدیر در پی عملکرد موفق بانک در رعایت موازین شرعی، تقویت سازوکارهای نظارت و تطبیق شرعی و اجرای صحیح عقود اسلامی در عملیات بانکی انجام شد.
🔹
لوح تقدیر با امضای رئیس کل بانک مرکزی و رئیس شورای فقهی این بانک به طور جداگانه به دکتر قاسمی سرپرست بانک توسعه صادرات ایران و رضا عبیدی مسئول نظارت و تطبیق شرعی بانک اهدا شد.
🔹
در این ارزیابی، شاخص‌هایی همچون نظارت بر رعایت مقررات شرعی، بررسی پرونده‌های تسهیلاتی، نظارت بر مصرف تسهیلات در چارچوب عقود اسلامی و آموزش بانکداری اسلامی مورد توجه قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/686482" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686481">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db35ef4a5.mp4?token=kawZpKvmMMW8-yt2P1JLf0hl-_vSHKaLMwy1P_AELoiXbWeGeBGak6Dpp8JIa5F9km3Ueuru5C4t9dFJTPnd0j079Q4fIPg50taq6dptOqJTpVmuuw_w0oqXKSvdY0T0YPi-k86d9NeXdN5x5ZtDPX7-7xjOa053TLaCNWGpi7au7Lueq_FQUerP5CFT1W2ICrjIdepOwekDh44JWkSQwVjUgNj88poKnPBbIYEeyPnopXp7nmoGZXifM9hq_FDSOFlMNI2IDCskpJTIn2fL1jb0iyVD66mM1wztsJqXAaNtRzdJDOyUZ14og2fCE6es_KOIuQE6z8QnMhi6NBPmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db35ef4a5.mp4?token=kawZpKvmMMW8-yt2P1JLf0hl-_vSHKaLMwy1P_AELoiXbWeGeBGak6Dpp8JIa5F9km3Ueuru5C4t9dFJTPnd0j079Q4fIPg50taq6dptOqJTpVmuuw_w0oqXKSvdY0T0YPi-k86d9NeXdN5x5ZtDPX7-7xjOa053TLaCNWGpi7au7Lueq_FQUerP5CFT1W2ICrjIdepOwekDh44JWkSQwVjUgNj88poKnPBbIYEeyPnopXp7nmoGZXifM9hq_FDSOFlMNI2IDCskpJTIn2fL1jb0iyVD66mM1wztsJqXAaNtRzdJDOyUZ14og2fCE6es_KOIuQE6z8QnMhi6NBPmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای تازه از اصابت موشک ایرانی به پایگاه هوایی آمریکایی الازرق اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/686481" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7195ceb1.mp4?token=t-yOjODlCPbuuPSCGA7owk27CoQn5V6RUHaynwrH-bmTBn8eZkSgG2V_QE2y-ACIISL1TPpDOD0eSCvPcrsOmIDOs2xgUhxWCS6GlbJMN20xMQRm1dGGtYwYrsN1lzuKyJh1SzT2kK3pDyYFXmXi_pMMqTYvHbUbTQdwHl-zY982JU-SPxATm8KaDEKz4h8Dn-RKgX0ynvjVsynQX8JdkK-Z92RIu-g1I28nNJcRTuLc6cyqK0c2FsshPweaAxOuYFGV7kgdpQbWQuEJyEwQx1DGd3EUew-C5DQIRW9l4Ua9chne_mtRoDWeb5ujYSQacLWoJWohxeKWXwYLaXhpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7195ceb1.mp4?token=t-yOjODlCPbuuPSCGA7owk27CoQn5V6RUHaynwrH-bmTBn8eZkSgG2V_QE2y-ACIISL1TPpDOD0eSCvPcrsOmIDOs2xgUhxWCS6GlbJMN20xMQRm1dGGtYwYrsN1lzuKyJh1SzT2kK3pDyYFXmXi_pMMqTYvHbUbTQdwHl-zY982JU-SPxATm8KaDEKz4h8Dn-RKgX0ynvjVsynQX8JdkK-Z92RIu-g1I28nNJcRTuLc6cyqK0c2FsshPweaAxOuYFGV7kgdpQbWQuEJyEwQx1DGd3EUew-C5DQIRW9l4Ua9chne_mtRoDWeb5ujYSQacLWoJWohxeKWXwYLaXhpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سندی از جنایت آمریکا در حمله به مناطق مسکونی
🔹
وسعت حمله ارتش آمریکا به مراسم عروسی در سیریک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/686480" target="_blank">📅 09:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686475">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lT68Lg-cmYR-tRZVOWVOJtmma4M9VQR5OZ3gDyp7Ko0dNxRglCoqi6JAzWYsyDcuEQVVi-o9UnxnBdBH7KSMwhNPkr8MiIwAML0lo6qVVC3enAG6jeGlbyIjPVLQBaBKk15wKD_kP9VEwEIXV1nbw-OKkkUJBOyuoQhIFwRq7qKjYZP_gS_ubr5ZmKuU-PNdLYPgFPu7DMzpuPm7TuImBBut1t8v-CllmWQkn2ZlXHph2kqXk4fXPQ_Mkonz8ZDnGQ_Pr0xNbTRvrbe4x-kCsE9zYtifE15qkjaEXTsz-ENyUETe3F1CzipKe_8W7BFpNmRghlrxeUTUKejOtNSw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdqTLXRrT76vJ5KpMk0jdpC1UI2J7L8vkdwv4u4WzfF4a8G9X-B-IoZTfK7M2h9_ZQK-fLDqjQjdmSfv7nlYmEhzqIyj02ttjs6ZcIMosBMunPaPPwJFLx4lKG9bqLWB8brglnbhQ-bUJw8bbph0wBmnjJ0PJpz7FJH5xugDCQEvNLMeL4CrqfUEEPI8WeRz4tLTVQ2x9LvkvRDE44jSwGKD6J-UJG1lsKuv4hfTykC7dXdudRHDp6HusRz_rwk57LLoRKT3CT6fX2ixVo_mNHUesxyU0nhigq130pwIe8_-x1O0f7TLQSdgoD7XXDAk715tZWJt-rZMQsyuGXXN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHKyZpz_Z-IOwytitjwT6aGrQNRDEzD8v6sAm-dkKXnYOTB3kxTEy3j0fu9Kk9Cd0MqB8QrIO4QxlLBwQ9KNycff9V60htX6lsRenzkvehAAxBkntu00seEhfhbzGRq4Nk2HYUoCGzt0-ynYJxU1vVXd2vDpg5VXzuxbNbfyaJxVZAl_v9OUUilBsWSollLiWtRLel1099PX6r2DNrt2c-AqiTvpC12dsPZ_fVIDPTDUnaBWLFVovTTR2R8eGGm6Xygl3fLcMlIzrPpSZtqajtW2KtmnwzRURaZnM7EpbHGWv9iFH1FyjDxhTHie6MtSWs2XiZkczzMdTmcFkRI0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcOe1_H_qOFpEFQyvOAQnIq_wIqGixvp3tvDrQHX1at35OwNonK6d_xJ2bspZCVa9fIPKIJnWBTyUi_3PgZFcdfBAm01BezknFx7RbIVTz6PyX9dukWbmeoaUUdmEmO8lX7daBn3NVRLAPQPDz3paTuHrphQUtHkBAGj_ZDxI_wjgS7-bKNyM7jX38A7T1HX30bVgp182bAb5X1VCz25xbQZisaV75RSPf4-75shExdCSxX1DUSFWJAVXnGQHerfz-Zcqiu6Bs0TES7Q0t6uMT1W8HMdxGgdF6rXSC1nPT2C-bAc46k6GMbGAPK4U4ahwvmSCU1Vv80004slzd2hnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCI6d6d71TC6RwwJineYRuU8bzpcHz8S4UOCcx-f25hQAcftUXUs3RJvriRQL_ef3hZjeXxk5asesqxRiJHPnlkZe__nzeCy9ysTncInvCVdIPps5sxbNLOSX0BaXfbKIbFD8jef1ze1UlUKXy-B21-2fp40Aq5vrk-OvRaLEQQrqSmY5l7bcVdCT0_nyOiBbA0pkkeVtfNf6sJqoAykEhqkkGmtPVNEr4NbPygT9JegWR2TKw3zG6kzho88CmZyDcVdZXdLjg-Orpz4Sk95vOCNkJXWfmD-zdjizV6ZulaRBWkXq-sYoV9IoAFCll7fIAkhTyn-upM9a8924yWjHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
موشکی که به مراسم عروسی در منطقه کوهستک در جنوب ایران اصابت کرد و منجر به شهادت ۵ غیرنظامی (از جمله یک کودک) و زخمی شدن ۵۰ نفر دیگر شد، یک موشک آمریکایی به نام "SLAM-ER" بود
🔹
شرکت بوئینگ، سازنده این موشک کروز، ادعا می‌کند که این دقیق‌ترین سلاح در کل ناوگان…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/686475" target="_blank">📅 09:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686474">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وضعیت مجروحان حادثه حمله آمریکا به جشن عروسی در بیمارستان میناب  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/686474" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس کمیسیون اجتماعی مجلس، از واگذاری اختیار تعطیلی پنجشنبه‌ها به دولت خبر داد.
🔹
یک کارشناس رسمی دادگستری اردبیل حین دریافت رشوه دستگیر شد.
🔹
رژیم صهیونیستی در جولان اشغالی رزمایش برگزار می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/686472" target="_blank">📅 09:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686471">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تکذیب حذف شارژ کالابرگ؛ زمان‌بندی جدید اعلام شد  معاون وزیر تعاون کار و رفاه اجتماعی:
🔹
زمانبندی شارژ کالابرگ از این پس به جای ۱۵، ۲۰ و ۲۵ هر ماه، در تاریخ‌های ۵، ۱۵ و ۲۵ ماه انجام می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/686471" target="_blank">📅 09:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4075e7990.mp4?token=JT3v7TaO6fM2k8EVWPgnHtETNMjwW02l5FuTAE3GVW7lUXU7b3MRSiyXLmMMQTBz0rXOOYU2kj_tElmnHgLiR0P08GxLwYV_2mutJifby5fDH07fapCkB3jDvUPC5lQzuBFe13T2_rF0Q_5NMe9H055ZGAFbnXKVShLPLRu97Ay_6ZB8SpjbItwaIxUCTzzIevmcxjkxvG0GgJMjXRFF_P38NgXyYoHfBiKi-l8boNlquQw5em_66GT8Cc5MAvkGn8SQudgkYLdOk5VIa4zXkHxGRaky5N_U9exYbs6U00__2SvhUyLh1huDAZP9wqAcaspQ_YJWrJalsVq5D4xuiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4075e7990.mp4?token=JT3v7TaO6fM2k8EVWPgnHtETNMjwW02l5FuTAE3GVW7lUXU7b3MRSiyXLmMMQTBz0rXOOYU2kj_tElmnHgLiR0P08GxLwYV_2mutJifby5fDH07fapCkB3jDvUPC5lQzuBFe13T2_rF0Q_5NMe9H055ZGAFbnXKVShLPLRu97Ay_6ZB8SpjbItwaIxUCTzzIevmcxjkxvG0GgJMjXRFF_P38NgXyYoHfBiKi-l8boNlquQw5em_66GT8Cc5MAvkGn8SQudgkYLdOk5VIa4zXkHxGRaky5N_U9exYbs6U00__2SvhUyLh1huDAZP9wqAcaspQ_YJWrJalsVq5D4xuiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکذیب حذف شارژ کالابرگ؛ زمان‌بندی جدید اعلام شد
معاون وزیر تعاون کار و رفاه اجتماعی:
🔹
زمانبندی شارژ کالابرگ از این پس به جای ۱۵، ۲۰ و ۲۵ هر ماه، در تاریخ‌های ۵، ۱۵ و ۲۵ ماه انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/686470" target="_blank">📅 09:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88e74c3ba.mp4?token=bMM6yDfeKdO6yKGAGxfuDuTtK9zwqhKG1n5hMueFi4_6Ku_6WAqD7jDo7_imK-u_S4W_DVvckST7FrqL43Ph4gVTEB-ZuWWA_zBK0hpm3wjoCLN75aE_Wt__V7QpLyLaOBOWN8NvhuDjachKgNwRMUDd8UOSzwe1IRplHFXcaE83YMsLkpm8n6UGc7Uq7-XT5FX8IGtppVqAjMxDWnxv39XW7OhGZy2JFOGIEbBEz7StBa_bhNRJ6Pj2fwbYTIO6tJmiasoAQS12xbnkUUil1nv2ZCJsn9kjioXpen3j2_4MbiMZicuq0CH6ZcBVrjamWHWQdkytkuRv3vGT_xvwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88e74c3ba.mp4?token=bMM6yDfeKdO6yKGAGxfuDuTtK9zwqhKG1n5hMueFi4_6Ku_6WAqD7jDo7_imK-u_S4W_DVvckST7FrqL43Ph4gVTEB-ZuWWA_zBK0hpm3wjoCLN75aE_Wt__V7QpLyLaOBOWN8NvhuDjachKgNwRMUDd8UOSzwe1IRplHFXcaE83YMsLkpm8n6UGc7Uq7-XT5FX8IGtppVqAjMxDWnxv39XW7OhGZy2JFOGIEbBEz7StBa_bhNRJ6Pj2fwbYTIO6tJmiasoAQS12xbnkUUil1nv2ZCJsn9kjioXpen3j2_4MbiMZicuq0CH6ZcBVrjamWHWQdkytkuRv3vGT_xvwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله سی‌ام عملیات صاعقه ارتش/ادامه حملات پهپادی ارتش به پایگاه‌های آمریکا در بحرین و امارات
روابط عمومی ارتش:
🔹
در سی‌امین مرحله از عملیات صاعقه و در پاسخ به هدف قرار دادن مردم بی‌گناه، از بامداد امروز، ده‌ها فروند پهپاد انهدامی ارتش، سامانه‌های راداری و محل‌ استقرار نیروهای آمریکا در پایگاه‌های الظفره و المنهاد امارات را مورد هدف قرار دادند.
🔹
همچنین، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین، مجددا مورد هدف حملات پر حجم پهپادهای انهدامی آرش قرار گرفت.
🔹
پایگاه الظفره یکی از مراکز مهم عملیاتی آمریکای جنایتکار در منطقه است و از آن برای عملیات هوایی، شناسایی، مراقبت  و پشتیبانی استفاده می‌کند.
🔹
حمله به مناطق مسکونی و هدف قرار دادن مراسم عروسی از سوی دشمن، مصداق بارز جنایت جنگی و  آشکار کننده ماهیّت پلید «حقوق بشر آمریکایی»است و قطعا پاسخ رزمندگان ارتش به این جنایات دامنه دار و گسترده خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/686469" target="_blank">📅 08:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
بیانیه شماره ۶ سپاه پاسداران: زمان پایان سلطه رژیم منفور و وحشی آمریکا فرا رسیده است   بسم الله قاصم الجبارین  و لکم فی القصاص حیاه یا اولی الالباب  مردم مسلمان و شریف کردستان عراق
🔹
ارتش کودک کش آمریکا که تجاوز خود به ایران را با جنایت و کودک کشی در میناب…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/686468" target="_blank">📅 08:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH8SZ7CBg1Ii0dA3VXKxQVNNMEi6BHZU8cTfmMXMeV4fCGIePh08PrjwdH4W9nO9PY1O7KcbQutbQGept8XN5I73Ejkk6Vc5IuGIMMy0WBkWO1ojDhttUvkECxMYv_FNDSsQ-MHYk93Mx5TwFNbGZrWtNEi-URC7D-z9_S6BTSpbzGVnr5m7j_iHd0eNueDcVC-xqwliM51sXAPxBKE0jvCpmWkjCxLzpl1XhsdlNrovoFpnfBFwos1zXCqvE4iUGRXpQ_Jx4uLSrTOvZo9F0etQdVuXkbAXHI7w6gc7_nH42p3H7dBcolMI-sxinxCfPNn9pST1yUl6YK-Y90A2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیش از ۲۰ مقام ارشد نظامی آمریکایی در طول دوره تصدی پیت هگست (وزیر جنگ آمریکا)، استعفا داده‌ یا اخراج شده‌اند
یک مقام آمریکایی:
🔹
"هگست تعداد بیشتری از ژنرال‌های آمریکایی را نسبت به ژنرال‌های ایرانی کنار گذاشته است"
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/686467" target="_blank">📅 08:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWMLaguUPJPCniO0dFytOy71OzspVImS-1yfjEX3ga1MOnBx3uArRJ1HcXZHoSog1RGFjWT2Loy3G8Hhos0pkE86FQDhjWJdbyPi4cPrfx_f60AKNNdjqhUU20DxIbivERqwRd2yKJQmvk-IIKzXWKn7KBF0Hbz4PiMwNccIf7gXKx-RQdXnpHVg6xCYlIpag929R2n_LLt4ih3iUXjl7d5JFrF7PlVUKuJ3aeIEM_N4hQAqiGkG6TKQwWhNfPowBjdiioyb_xKuJh8LxWnm8hJ0nUN9cDVa3Lf5bINCmK-Rzc6ALEcgx-l_Qi96auJtA3URDa9a8pP-zvugM7AaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس مدعی شد: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است؛ دو نفتکش هدف قرار گرفتند
یک مقام آمریکایی:
🔹
این اقدام بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» است که با هدف افزایش فشار و بازدارندگی در برابر حملات ایران به نفتکش‌های عبوری از تنگه هرمز تصویب شده است
🔹
آمریکا نفتکش‌های ایرانی را به عنوان اقدامی تلافی‌جویانه در برابر حملات ایران به کشتی‌ها در تنگه هرمز هدف قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/686466" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfP8QkblPMVJ2OmX6Xy-sFi0vya3pSTRNfMnvNKjbFA7-O-R5Ww0uxDMZJuKPB4TUvjOhUqFEx6mPYpI5giDmeOv8sDpJwSBI7OBVKI5G6uO4Ej_EGFjK2FmyLY2QkubohOAnui7p4_rCDTP8CMa7hu5dRGVkcfWDIuEouVBlFZO5bye2CUYuaT8rd08WSPyKjRA5vHiXGteNialyl6T4aUUbba9wMOGVzvXqmJ6v1bHitErrNJiuXRPZcc42LO3_kFx5dglGjEpcgsOy_5lmvNirYfppro-WVXKl-33K-IZKkwFrj_56BGKyk5RhQAYlnUD-x4VXRoGfNhIppJAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار تصاویر از قطعات موشک‌های اصابت‌کرده به مراسم عروسی در کوهستک سیریک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/686465" target="_blank">📅 08:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi0at9Tt2VuOZENADrn0rsMV0ih2BdZHmWcOGR-IGsjQC-IcIARz5B7XztP83vhQ8GDlAnS875kcqJxz5rojLh7kV35fU3DxIkvt6agWLbBoVYi0tsIt1u4PBm51cs3ZjlMCA20gRmU3TOP8iJr0RV-aIutzhKbSkqs2lo7vXGNXRhBlnQwhUbVMn1ejKc8Cb7MAxvXNqgkbCmKVK0IHZ_Bi0vJRgCAKZ9y-am6efGOJ2SVl5Rqir5cEpJExmeF0MWpiy7gvDOklA50f1fBzry9AGPeA65CCzH8VfzmGNwESbgXvq2KGaRsrifxxX3acKv7vC2j88sNtnW5AK_Vx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ساعتی قبل از ۹۶ دلار هم عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/686464" target="_blank">📅 08:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5534a77c.mp4?token=kHhYUxv1bEGCivze89F2oRq7nTzi1ZdOebmVnYK6nhSW89Xf4n5NTz4O3KmB-OupwvlLh7GX3EIFFWLUoHqvMbl9zJugKIlkroaxZJzEYGNffmg9phJeCzDKbKDt21jNpnp1FryfKhOXJfg0c2hT4l13giEwpValYHDQKdNGztJ_TbKfyqPazYzL4Jm_svod_gVSjGolb4Wx_cutLa-KuY-siO3ExOLSCKKUqleQWak7PjiR0kMSK6iRyd9SPXRxlT7s8eHx-KL2DX7x7kxmqhEluttTqRT9Sr-hAO-yKgHSYZE9xyoR01Wn2w3TvjMhhYtRZikMHi_L19Kh-5TloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5534a77c.mp4?token=kHhYUxv1bEGCivze89F2oRq7nTzi1ZdOebmVnYK6nhSW89Xf4n5NTz4O3KmB-OupwvlLh7GX3EIFFWLUoHqvMbl9zJugKIlkroaxZJzEYGNffmg9phJeCzDKbKDt21jNpnp1FryfKhOXJfg0c2hT4l13giEwpValYHDQKdNGztJ_TbKfyqPazYzL4Jm_svod_gVSjGolb4Wx_cutLa-KuY-siO3ExOLSCKKUqleQWak7PjiR0kMSK6iRyd9SPXRxlT7s8eHx-KL2DX7x7kxmqhEluttTqRT9Sr-hAO-yKgHSYZE9xyoR01Wn2w3TvjMhhYtRZikMHi_L19Kh-5TloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از حمله آمریکا به مدرسه میناب و ورزشگاه لامرد نوبت به عروسی در سیریک رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/686463" target="_blank">📅 08:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
هشدار دادستان تهران به افرادی که به تعهدات ارزی خود عمل نکرده‌اند
دادستان تهران:
🔹
کلیه اشخاصی که دارای تعهدات ارزی هستند در اسرع وقت نسبت به ایفا تعهدات خود اقدام کنند، در غیر این صورت مورد برخورد صریح، قاطع و قانونی دستگاه قضایی قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/686462" target="_blank">📅 08:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تیم‌های پرسپولیس و استقلال در صدوهفتمین شهرآورد از ساعت ۱۹:۳۰ به مصاف هم می‌روند.
🔹
پارلمان ونزوئلا قرارداد نفتی با آمریکا را تصویب کرد.
🔹
صدای انفجار کنترل شده در محدوده شهر میمه اصفهان شنیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/686461" target="_blank">📅 08:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سوءاستفاده از جایگاه شورای امنیت؛ فرانسه در پی برگزاری نشستی درباره ایران
🔹
سفیر فرانسه در سازمان ملل متحد که کشورش به تازگی ریاست دوره ای شورای امنیت را در ماه جاری میلادی(سپتامبر) برعهده گرفته است، با سوءاستفاده از موقعیت خود، در پی برگزاری نشستی درباره ایران پیش از آغاز نشست سالانه سران مجمع عمومی سازمان ملل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/686460" target="_blank">📅 08:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c623c5b1a8.mp4?token=fqqSKjQxdYfShm_boFC-hDPbtZ2aTq2336dG9Tj_ZeSbvb_X8NSvafSxr1x_1Od9PMwdxNPSfnHHbUozGyDycFNuX1uogSNGDuOevnZPFAUOqp778z13E0qmTCd12wNeMRYi7ODbck8p6Nueemp6LwAUMUMMX4w0oYMDn7HN6dmlCYnj3yGKjKxrbzbjv79kcJqg8ALvWbtm07ZlGLHKULKeDCAyni6KOlah84wVb8U80Tdar-iu5LvT3Kb2owYTUjTmuxECXWlttbQ7WccG_dKuwtyePjkTEYB-tsSIoLcaBygsVOB69jVObzu5IujNK1sxWcWG_6Wv4pavVyWemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c623c5b1a8.mp4?token=fqqSKjQxdYfShm_boFC-hDPbtZ2aTq2336dG9Tj_ZeSbvb_X8NSvafSxr1x_1Od9PMwdxNPSfnHHbUozGyDycFNuX1uogSNGDuOevnZPFAUOqp778z13E0qmTCd12wNeMRYi7ODbck8p6Nueemp6LwAUMUMMX4w0oYMDn7HN6dmlCYnj3yGKjKxrbzbjv79kcJqg8ALvWbtm07ZlGLHKULKeDCAyni6KOlah84wVb8U80Tdar-iu5LvT3Kb2owYTUjTmuxECXWlttbQ7WccG_dKuwtyePjkTEYB-tsSIoLcaBygsVOB69jVObzu5IujNK1sxWcWG_6Wv4pavVyWemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تمرینات برای افرادی است که می‌خواهند بدنشان را بدون وزنه قوی کنند! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/686459" target="_blank">📅 08:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f8589ea7.mp4?token=YUyQplbAFd-7vL19QeisqW0o7h-w5bdZLrpd5xw4DCNSVhiZBJLIZxz7FZqQuO7vFWM3f6qzNVstzALiC4Ast4QGhX_HdJCrwuIuNTAbpAgS9pV8rOHdkraAkzvQNCZZ5aV3WbC-cyjD88Csb6lF1aeK3I-8wXY_7SPBfqxurG9HP6NMWAvJnrU_tLfQXhtw_fpAc7WvJL3_SbCDOGXX1tfgONRAAvsoa6-pnGgB-aIBVZgeCxyzmI_HRqxZ5T5l-rfy7jBoFs9vvPjbAB6xedWyuMe5HquXxTbRaznezpCky0MsviBv6o2r8NbjM8iVmbMbkmf8gBhCRe7BdD329zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f8589ea7.mp4?token=YUyQplbAFd-7vL19QeisqW0o7h-w5bdZLrpd5xw4DCNSVhiZBJLIZxz7FZqQuO7vFWM3f6qzNVstzALiC4Ast4QGhX_HdJCrwuIuNTAbpAgS9pV8rOHdkraAkzvQNCZZ5aV3WbC-cyjD88Csb6lF1aeK3I-8wXY_7SPBfqxurG9HP6NMWAvJnrU_tLfQXhtw_fpAc7WvJL3_SbCDOGXX1tfgONRAAvsoa6-pnGgB-aIBVZgeCxyzmI_HRqxZ5T5l-rfy7jBoFs9vvPjbAB6xedWyuMe5HquXxTbRaznezpCky0MsviBv6o2r8NbjM8iVmbMbkmf8gBhCRe7BdD329zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرماندار شهرستان سیریک: ۵۰ نفر از ۶۳ نفر مجروح جنایت آمریکایی در کوهستک زن و کودک هستند
🔹
همه‌ی مجروحین به بیمارستان شهر میناب منتقل شدند و وضعیت مساعد دارند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/686458" target="_blank">📅 07:54 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
