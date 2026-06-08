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
<img src="https://cdn4.telesco.pe/file/QpcFfaDThY3BvG0_KwCOuHz9pZtTikXOiYxM-puMw20t6md_vRPfnobrcl-M5z1_MYzllKTKz6sAkzkn9PQ6ORlIaXBxscpZEubJDqiSp_6Q-28PEAzeOoCGpdsL_a4T_uApOu-DOmzXqBOwGck8QtPQ2TSqJHPTKlZ7VaOyskyXZC0KWagLESW5BfOWWC6u1fdoxH9w30jeCFE74CTnuJwPkPmuw6IN4eLCYRwe2EfQOz1sePf-MA000DiQLeJvhg5AwySM0QU1Whoa55pJBKdhemf_u3fkKOBwsi2AinWlw6Kq9zUWOfXW6MbuZgF5UXOAbg3fEomt1ljXgnLaPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=BqZpLQSc7RXoRM4UPa37SDwtABfH2g5Yekxii2DTWiUaf8AQy5WNgGE3Ax5dE_GJX-yFBTAhQTQFNwxA1N2adGsPQh1eBkntkH4tX2PcKb0rC1o5eRoHX7-oruPGqtdNjazn8gYzCZ9mWfj8v_x67l0Jk11givUYYG3aqy_LQOXh5L886c56ISOPMI9FnAuvPM-0fRTLVIY65LPQQ6UL0SIXV9akPsQyiNWyckHSDQzsmtK2ZhlJ2UW-mvtWwAdxXZNkKfQx0JSF-agFm5v1jL9MfbZeEgBpsyQeBHVPDmXaCLl9F9j-8yA_2LfzqTC2fUN9zHxPO_6DyFPeDEaxnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=BqZpLQSc7RXoRM4UPa37SDwtABfH2g5Yekxii2DTWiUaf8AQy5WNgGE3Ax5dE_GJX-yFBTAhQTQFNwxA1N2adGsPQh1eBkntkH4tX2PcKb0rC1o5eRoHX7-oruPGqtdNjazn8gYzCZ9mWfj8v_x67l0Jk11givUYYG3aqy_LQOXh5L886c56ISOPMI9FnAuvPM-0fRTLVIY65LPQQ6UL0SIXV9akPsQyiNWyckHSDQzsmtK2ZhlJ2UW-mvtWwAdxXZNkKfQx0JSF-agFm5v1jL9MfbZeEgBpsyQeBHVPDmXaCLl9F9j-8yA_2LfzqTC2fUN9zHxPO_6DyFPeDEaxnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=Mrwaq9NC3oKcfMPDl564BXqM6PL_hzcT0CEsTyASwmQzKIRNjsxJwyI6oTP1K0ul2UJT9JaZ8ZAGiDjA30Uoa_IVH7Rvs1eTJSBKVzzjUe5Qe25g0pSHDHA2T7aE0OOkWBrQjr8swM_6bqjqrCCToV8LtYZOVjwOhP8Htmgu9_M94Ov9zrBZ0GIv80riSNfBhL5A74LLh_At5Qi_iGRaoLSN9kkgbJ_nc8CJbU4y-JYKzQPVulfM0g_8akiYLKtV3umqUSWnyZMkA7Lqbwi9sCjoPszwg-3Aeq7b5fFywpFpaeXL83UOODuJ4rL830DarkNyI6FhENvBSSi756u0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=Mrwaq9NC3oKcfMPDl564BXqM6PL_hzcT0CEsTyASwmQzKIRNjsxJwyI6oTP1K0ul2UJT9JaZ8ZAGiDjA30Uoa_IVH7Rvs1eTJSBKVzzjUe5Qe25g0pSHDHA2T7aE0OOkWBrQjr8swM_6bqjqrCCToV8LtYZOVjwOhP8Htmgu9_M94Ov9zrBZ0GIv80riSNfBhL5A74LLh_At5Qi_iGRaoLSN9kkgbJ_nc8CJbU4y-JYKzQPVulfM0g_8akiYLKtV3umqUSWnyZMkA7Lqbwi9sCjoPszwg-3Aeq7b5fFywpFpaeXL83UOODuJ4rL830DarkNyI6FhENvBSSi756u0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGVoNrcxDxw6T71Flue5sGNepXGRDRDKV3oAPse4YAbdLyHz7WwwZDSIRrEDHgUsg1Us0AHLN5SEz4MW2uxaVPsZuuS3U2JvAWvTbQrHlg1nWRfoLota2fK_DAfUGqf45VAT6_yt9KFb_Pq-VXsEZezut0l389qWGF8XFs2FoOBlKyXNiAEMqrYTxPh6DM9IgRS-PXXWyEaA7ySswZ0_qGJ5RifQOQK5XkI1eL5HW2EDBT2wmhjFggSdgOMAN8iVxuJEO8fDspPt8hDgEAIEseePGqS3p7xJbmU6CMUC-DOxW1pygy2CNxCvMuNJv5gkuCV8jQ8EECYHpopjPakA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBNMHpTtmPxcyXN5Nz_S2zXOEMynSLJcg4Hv4PQuIPUFnRyQ1jp5BpAxiLRo6SZ5fklpUQpINW76oGiLdN-BOjJlAFMPFv7EQoyHbb3xaYYBoJoTbPFhCH_rhyglE5rMihxJDZq7bjc8ESZ0AJf79iNk-8F1rCj4M30lLSkQCFnnxxnScvEGVg4kVXzMt8-rR0LG3iPJ9xayQ8uQcFhEwEzsMvzMHylncHGXcPFN2mIffQXZNqn-CkqhQcsBjmuFFOY6U6taQp0kMQHctgil-K6mEiTDgH9C5gMD7XfDz2nLmD3imyEDWRZ94ycUJNC3hb_Kp4Bdtp2IXp_RsG4tDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O687kfXCDyKIY1EZANFUFsQVcUroLcam_YWhXyjRv3BggUuxWev62JT0nDmrBSJc8k81pIwXDj18_7wTbC4stvJC2brJoACCYUY5OXJynjZvwIev8od5bMSpbi9J-yHv-NBTk5Y7w0B-wfUyWiw3aiMYfoKlvA_QmvYEgaN8sAZowTnvgYp7XcOj_Rgg87IAug23TCFC1954lREAEKz6FEviJkn9olOcKqGsZ_2J0pa5OBH_5aozyiJxqlrVwQpR3BPQGrNcYKruMQyXL9wDB6uPS9I4SnR8rbW5PnxNKKVXzv1gZt1rIsvZejWalbHXr2cY8X8S9B-1ZNmP09ff4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpkjHFFL2jwlOQug4T9GrARuwGVZf0ZcOFm57RktN0rHNg3SBJgXliDZ7lnOy71FfjfG2d82phun5R40Rn7For-ULw-D-b9BHauUNc6f-01XbxrahLS4Ulzjlbvg9wWGv-AdjRQpasKtukdsooGG4-9KCahGQGKlnl5_YEUEjr5-LDeMfgZFJRNzsXjsHKjMbiqrVTvizrNSwBaib5H5g4YzP6UpDucXqwq9quq95nCGjlS62IFvSrW7Efaq-lyOzdqidvKb0NdufY2TvhP16hWxBvoNXkTHArk6UPKPQLX8vbw5_MTxUnUNRdxwaXMZTLDTg0PFPLGO3l8CS9-mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDrmIfXuzTi2Hz9E1Ee_xTCtxV0DgDfeawml1s5Nes_9I4wSVLJSru3-i3--_CbCq3CaRTQjEsn1yOpk4OyUbe26lQIZ5cOfvsJIa2FqhnE_0rr72z6ohXvhBF7K_tB2N73BIeww_skWwX5I4Q685Rpp_3qbZGWzBHrJkDk-pn14gciulx1D-Mxq5xeF3_XqWdRwoxi0RuQSxA2Vx-q3z4krW1S7oZtQC50qlE5OROWSI9hXtBCJ8hIDQSjia7e5i-D09yb8kBJxmQzSOZ72F5ROy2_hRd0PGCGUs4KMvBM6kjWqUHS5-8k6sPNbq5wD8Sh79Pks3ar_GbBcpNrx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiiMXvXkRe8VgTrYXjP_Z42DFCxQ9CGqpbL6d0C2GPh9ULhU-QIfKU4FcH8Mo8Sqff_7iBwJFkwmYFt7RytM35jhfjPS-cbv0EU4-8sDrTr9zOejBXbOZvaT19M2xmK9Sdn70S0WyVEB8jQhXjWNqaZ-kNv-DzhTRH_I0qBpZ8kT1kCnbRRqrpMu_qPY8vYvbUk3eZcUitr0kzpyFPOccnaLvHB8foi0jTSgnYQB5133lyKNPIm1LITXf4QqVIjcCjNmHkRosHSayeh6RPLA9Rz-OgXNjDZoI0XZ5dmuR4K8jAIxo43j_QqhvXO4n6RlUd2e0udOfKWtmOCfJvExqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2gUP3GvmDBERO69NqnUjHIO0_05g6MZ65Xd1C0NzwzbMMrIGaBGxxAgOeVUR1eUdKeBQdH1lhgJWSNTFjvY0JaqEuGH_qdPJBRPHsF-0JDp0CTQjqPO6uuYR3iGH1PqBlAhqOj6F2hbxewPHUK7TE1oQDHxnbh1DfDUb2d9K2iNgOXGaleDvOoO1ERIpbx95heQRgL8GCb2kZg70RBuL48UHQzQpQooy8GD11lqPsTbqZ9NXFk-3xtbxJM50WvFNiZY8_V8WYnHsCNbTj0TUCjW5swamCx21QU8Q1sD4kD2OSnHh3dd5swN9iymfXdDUCxuUApMKMkjfvngsALeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8D6xoVzq6om_kzaBAPJOjFiSt6SsLtMo7qEujscJ3E6-ZtICWfKjZ4aSKCGm7XbWBId7elHZwqaYv-DvNsN3XlBbac_IZKL0AOmr-R5NNrab3PEQk0s_nIxuF0TRb54fILxeMeoqAe2EbxUXvLglOJOiygdwvh1ssBLkP0ffzKk5odXzPaDuUj43TtJZOhltLZRoHCqqRu7J4WXNh0RV7lhtD_N3_nYlC8t-0gM_EKBlQaBj71sBNEYFq0_DjxQW3Fc5-f0ubWPzil_d-k2jkapEyixVixI_mysPwM1YN18K6sNORfkKX5G5IlPpYWYZXcTnM5V7V43EZGDGG3EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiRnqu1cVmBqqz91wq2H0uZCZ7-hyb6mrY_2f7tWufd7bXR3p-MEReAOcEblA8TsQkEe3AHRdaN6un-miWyahoRswXvNHj__Rkm7UIijGHj9kXmQkCxfsZA74ify_hnXMtdg9BSfUK_jYDE4PH1vbLkzCAmv8W8ZpULZ28eSKOlWMM3jV4HdioMmto61QZ0iA5-aJpLChEd0mKhzqqVqRu-67UGlbCW5bNQswCvhewyqUR-KSPB4mAKkXqiG3IITOlu1FsmVHM1jr7uzviaeatpS8useQIw3kiouv6Yyw0R0Wi6ACf4ALY8Dx4wLyNAyGb4jvtyfMy1_EqFcBtOLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=rFMSfBiP0o8UCRXXcfRabEDH_4_saLKoi__E6hrCGCOZg6ZdEtgJzHe5spy6aTBhFegqzv0-qMsp4jA2vpF2CIrxVNBAkzY3My5ZP1dK2I1txHHSDEqZo3sprXfhGDArS3-ffMzKOYANVyNQeXAvYVGcERcJ--UzWROYbFXhPnijo8hQb-G2KOaYgglOrWAj54Fv-_75eSuKMN461Zg4TKQyofFbiSiacm5q7a-IP36fAh5DnJ9MtkBK_R3G-lrHs5bMoiDMIidoIy2zpzVROKsbiwEGoYacSyZ7Ulq6t_Of8ppc-5xc7uyKv6kAL56ejXS2IY3mN2YAMVbQWjzoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=MfWm5GgC-BJBZHsovqW5CU8-vYZ0l438QYMwcnHBbddf4-YpRagC7mr0wQHI86afd5kVMZ5uq2OjmHU1IkssRr6S-sWJ_VodLNcnV9aW-Yqo_3AkmHpxeH_VUgtnmyn5wEjymiD1LUiljkvB5Iic8GQD3gag213iaPwKxIooLl_zAJfyvRM6zDqz6YxMBLNnFP4jQJkLE6XAG3upQhykTeiZxWTAUQ_kZXKuqEpZNgASjCJNL7HNRSK_8pE2Ux50nWPJd_Bzf9s5sirKlV-iW-NxCa2JavuqmyX3OOtV3uA_6X6nWgSFJNs-1nnmBVBtRwyR61rar8ro34V-1F_bPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=MfWm5GgC-BJBZHsovqW5CU8-vYZ0l438QYMwcnHBbddf4-YpRagC7mr0wQHI86afd5kVMZ5uq2OjmHU1IkssRr6S-sWJ_VodLNcnV9aW-Yqo_3AkmHpxeH_VUgtnmyn5wEjymiD1LUiljkvB5Iic8GQD3gag213iaPwKxIooLl_zAJfyvRM6zDqz6YxMBLNnFP4jQJkLE6XAG3upQhykTeiZxWTAUQ_kZXKuqEpZNgASjCJNL7HNRSK_8pE2Ux50nWPJd_Bzf9s5sirKlV-iW-NxCa2JavuqmyX3OOtV3uA_6X6nWgSFJNs-1nnmBVBtRwyR61rar8ro34V-1F_bPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=E2omNYCWWNVvdvzx930ZXfESi18XeCrDJgnTCPKDMsP4Z9MWUaiMjAElP1bruxkttRDNqcxrPj9bzgh89IJiXDZE7EQlwdh9dB3sY_lZw_kFZVeE8H4QeAEbjeYNunEmbnLsehsZWgOuKadXD3cbNfh3TXG44wA6eTXibJ-SI-uJm2xHUXSZOzsxPUEq2lnpH4CxAJw0vUIhQNhCOHOnJ6c8YYznlIbiEN1hMxmO2RUk0BBlXR9mmn3tOzai5DWGn7V4GDfDTbR8bngSR7BLPvTUSmGaOmzGoVgEZh-PfcAdoRVmWuC6T6AqqFO9BzuqNdFFMoXkTqw8cAIkn_ot-jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co3k8KY8kGJvAP2AAndTAuIcDP096hiOqHTX4vN__zSrCUG0XWofcZCTx22ov7tmWhSiTc-vF74teZiqGYAFjm1a6DQH801ylGKPGAdqcqOaW6wViYyrTtuOfzifaUmsM0RwwoyV8VKlihrrsyyJpm9f2BD31PYqOQpRtWvIrhxh_Lde-QQMSYONGi7tQt-G9FBVZmySHCZcKOLvhHTdUNu3_NZRaLZeH7F7h5Vn6ufiMYQb7fokh-SNt3LlIBCawziVsp_q95a1wCExGQp_ayPotx57smXhxGaLlpPzT5FPSdrZvIbWTaNpDp-SkTt7fdVRt1PMBIh0ZmVKn11t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwsBSRMMsea8Rh-Jk6A36yJIVd2Vh3LgTWw11UH8i3TDitHOnAV7q4iH_7z9w0o2FB1l23z5s9UJCcy1DnMe_JwKFIBhS0IAlMEL2HnSPJSSEIDTTpD41poQ3z9xA4rR7FqE7zH03J3vxG6FsOTiJ_myZtzB5f2tdMZKCX5fLB2z6_84jpBkG7RrMfHoQW55-ajzkvQQdVX4kIkSlpkHTEY41Zy0yN9AFJbRo_WSGsim13CLiwBJhh8DrtrGjellCD6HETb9tuIdrzSPDD-YBRrN_OUV_huG0ScsuRwh2aMU1kOBD4qovMYzuEVwyEqkcXYtAwi1LWvSCxuJ28ilKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5B1U-f_dQsLmmpLcETGsIu39382AVVDd22o3urhQKYfFbolArAfSipdJCYK_0YALtCgjSZo74PoCJr6eoH00isjOGBaITYq3Gz3V79bLIt1Z4YCqBRYk1L174KqhHdoGbbam4qxjEq7Up41qiel6mOO3EgWFR3OyxQbsHZemJ_NZlRAYyy4G3OF7rsGy1WvgkUUfoeV_BF5krlzJ4fa5iSRB9C2jYTguOJUx6zmZWalZ6-oU72cVQWbtoBE6-0YBhtjXf1eBk-QgVHuESng_soYDaBDYm9rUReLm4WVHj8MYzLzmZ-Hiz5yMM4oVDz1-YDTFaXvYpjYeGJRz7ij1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH-TDJFiLwSZfxXhmGFmzgjx6sSzBk0dJcJSTuUDz8tTebxm7WvpJwFnLxiUHg7JSlQdnkNx3tHTJQxhFWnb2w4MotN8vHu3ytaWQa_ns3FH2EOu9XsxnhPfEE31BJDra_Im15bOn0aSTDrBEJjg15sK6lDWfD3tXnr4CGszGWTh24LICPSIx_7grO6qs4wviPZLFN8fw2N4MArrr4CWZsedyRQZif8mPNV6FaZ8-qEZ_isul69iFd-sps9FNqn3i19n_eY7iRfRiZr4BgrayG6a-MZtaWw0Tub9kLGJVrCOBzgPBnGE9vkq79_VES-nMdlU5Aof66hfqZuLUs4Big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPQ4dTLrH_lwhLcdIi2wzSOoD9sWJWvnWg7-6crTablLAntXKXt9Ac02oh6605rWNogdBQqMl3VRzAq-aW5uIPDFr7fTOsnPTIxEgmLdqDEMMeuqO4wijAVDjdgXRlylo9mL7-1nVYMu61bUio87DOL-XmTsIwPda_MxTMSvRS9CWV8N_8KWMuJXYlpcDtBQGxSjRdgfJx7_da8Qz9vAS77wAsAkn0Q1KjeeIHzpWFHKMqyX1_kb2AoGPUHG7W_ZyXqKV59WPuITqIzaC-33MGf7x_mhpePFzkHfZ-3v5E2kqIWgCJA2qE5DC8Ke_9bWpD_OvCPbsqReElb9-NQWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpHT70J-04suE8JJgLWc6xJq9NtJPIcSNriN54N1dd2abhTNf4HtWJ0k3Rv8lDYVaS-yOZCpMNLbqjFkLDtHu082zKMS5pYsjO6IeFcdHkrvfwqrgtq_11YI2xo9_SEojT2MBoVsnjPib9oOOOOa211Z8Dqn6WAndvGFaHEWMU0Sd4U9usZzozta4Tr2Kuo_ac_NUwxkDYxeWiybKBsEwkOjMRa1xJQ17CNvJQrWX-zlcWMs1TkpC3x9WDFCvZf6I-czGldMNfO6FwB1D0X0cstqACazVnfaFXP_LUnieu-V2YbwDK-zMZckq14nAJ8R0TGPkOrHP18m66MBX25zJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I248XGk3T3ARVhLyWgTbl0WhKnceCxpiz3sSYOI-utWDaSl2Y3-wzDGvwUW9regAB8mABet69Oamet-Zz7o3vGQLdhEcXU7qYhLfadJ2t3PxbN2Xp1CN1udhl0J6nO6pbOMwZyobDc93J_CXD35vueNWsv6Wjl6HiDrbFJo3T7UX1txQLRr_i1hEavjQmIPfKDqmShIUn-xsER913vv6WCXqlIOgJJlXFs7NMsy4WhdOMYVi0ch_c9KOgTZJV6WkTbp7ZOPYPqe4xkg5P7Q4LYtWZiPY9UcF_ZtMT8kUJDAX18MNdQit2gWckouKKNa8t-F3YCT32uXqsFVTiOW4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ajWt008KskkSB4PaNuuflTZKFMvHhz0myL6Vgm3u2KVmMOPK80vVUFwbJ7FAJYX0dEOFJhBZ5kUzu2KmpNVMn0ZcezsYnSC4GTVLk5EG8VdP-OZOfUoDyf_TpGgmrmNMvEvUz_lpR_Z4hy-DGvuNbOtDtQ8qSxM1hH-ZY03JzbDCnUunHHucxWj3TfwLooRdHMSFe-pP4EB6kTbbzej8KoeGm6jmk935hMnrAXSSTuCHNMy__VbWPaI-GDyb_3Gw3wXJZipl4M5KmYqugc0XmeFo6xRG4CrtfreXCpeyRoM8p2P3bC2-0Hqe1ZZtYkFkb2ob0VQ_-5cq_5lxIg5kEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4QEcS3xjni5SEku-2iaq67tOSDaTgNo-Ih2OM8i-rVly9gCm05hn_Vr6aYB9BE2htzUZgkwYwNSg4B_m6ZSZzeDzeCiMoP-pNt55EJSqG1L4MIbw7YeTqhXkw6iSI1pQpthOm8fM2yVoWZR_R6_AuvSAbaoDfGBseT8g1taGppzjPntwFgIL4pSh7XVj-sNkKoFPEgcyO_tp6qg2f39m_RBCe4zBoGck2yINP9Q7oq4rWSHuTE3loI4q4wtcdwEfVSSrdalq2iU6N-cwihbt9zz7Yx9lQ3iGaOHzu3htNbCz6Ne3QNJueCDOT9fH_XylwIe6KwQXNe2J7PGPP562A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=XAp3Uzq9Kxiw3kko_DHBrM7SIOOdKTc2ykxnIwDu-rKAaAbFu6g2PJ_-I2jnjTm-hOsxUz3ZUpeMOeFad8ZXIjHuUi4iWEodftvZdvRVVVZWDXiyWSFEQCFV7cSFf6knxcZneijnmrVlXE_sOaOMELlUHf4pNxTdvkADI3B4JMjPNWV_KKRGLkVzjkZchDebQ5bOA1TuxEVMm_7OjYygOqNBhvyLVg4pY5Ib4YsZFv4fyh5-_oy81ww0qP3n9rwbeA_Z1cHxZWOZacLGVEBa9Ijr0vWOgRIdsbjylHRqFxT456vNBpjHAFCuFREyChBuC-kS-be7tP05ANoDhhEPeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=XAp3Uzq9Kxiw3kko_DHBrM7SIOOdKTc2ykxnIwDu-rKAaAbFu6g2PJ_-I2jnjTm-hOsxUz3ZUpeMOeFad8ZXIjHuUi4iWEodftvZdvRVVVZWDXiyWSFEQCFV7cSFf6knxcZneijnmrVlXE_sOaOMELlUHf4pNxTdvkADI3B4JMjPNWV_KKRGLkVzjkZchDebQ5bOA1TuxEVMm_7OjYygOqNBhvyLVg4pY5Ib4YsZFv4fyh5-_oy81ww0qP3n9rwbeA_Z1cHxZWOZacLGVEBa9Ijr0vWOgRIdsbjylHRqFxT456vNBpjHAFCuFREyChBuC-kS-be7tP05ANoDhhEPeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8XyJ9yS5CJZDwf39RxVVNyu8VgtFpTcIU8Iw23qexvtfGFDX3yZvdU4fLbxD00SCgN_P3m55Ngp9qCGKUBTNztrzOj5SQz4rYsO7KOYLHVVgJAUD148Y425lMk9EstZPRBKoqq5dGuVzHhW542jj-seByG6CN1ZpfiDkK_t-jp9N3sw-NPmy7H1OJcamkHYChjCYK6rNOvBDQ3g_f1uopM-sk09DDXyh-FdKOJpOs0WKgQz_aCWDs-eMtYn42SavK3ny4PUS2e95i-SVMcNZdnMebCRxwel2GlV0Z6otTUkUoWxDbSjELZvKF5Vhz8-nCpG7deSQ9kYc2iTMvv3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m87PKaE14XwE7F2B7pmHMR5pibwA00AaZelhj-1fgwAl6uLWbhYpRmobNkb_0iQcV3h-woYoy_Dkzs4VnKNq2098guClQWVHgAIawNp2AXMy93PRadfL2viivn0GxPhJSTun6tFAp5v2VPSyO38ss6UvWRCZD3po2smnCOVsXuE43HAhQUbABECuFFpaupw0TgxT0x4IapglMyTlWHwbpB3ILZc1uIMsPo-WwmTuGOLwpB8y-vDZWcl7bTDfKV1HNexDx86sSR-ndiNhhGmhKOZgrBNEngtNW0hf-ldlWPoJoEv03ZYgFEf4NoPxsjaHoLgsx3J-JEuNFe6hyIOocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYM7b-wDek81aTwfxPtAH0y1_NrJZsFsasJR09QXf6lCpPPj0LKdOcIKRKKQu7x5FTrYpAbtT-2uutRNnyNdEmjUR5eQBSck3kFVpB9VlsxrhFbHPWkmX-Gqp3fXxQ0ZBu0L5YTgJjKmuD_Ry9ocWHKTW-trydG3mqHw7VQHDOM7Jc9axM7YlVc0q442KDMv4cdkQL5TgoG1XbobRdkWK4UxPYnQ-vz8w3fme8lWhzs7LQNSyvmQYP3z4JK8MuqM0dWzdzUPxPSqo10sf6xxeZHn11DykLEe_p3lFHt4B3ij3p7OE24bnA_mOOP3GknUiuCgdAfW-5qUEUc7aXrurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DN21MB5m0AALIXsl9z-jJ3xznLPIlCxxDb39JKfABWbH6COs4kgeNfvJQJxNM6FJaKe-pYL8GBSDUq4A9eyiimpGkdbdYM3n1GNjqNPH0q9bYKFKjRjDCN_tM1CIMHLDgyp4ItZQxGa5fc0qrjut1Q6pL8bH-pqJJCAOlAYk7gTkft-Gc2vhM9SFkBKs51fehh5thbtXTbhwB2DdFuKJEr_6QGEW01yPQxNHX8IRIALEh7CBnoaLDGvfm6ARPr8ja6PxADq_VLbrULEKzCZGv9SyiCf4Ff8dGgw9xqE9wpgz99KI02jXeWaK8i2ppIcF57fKnx4keVgJM-dMxPN1Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=GDpcqSfDhtPvvRuPDArMzWY0XKUkFc3lQAwQQs5KFTSl4H8qPsFve8mZ05Ivhpkqo_YH7GzTwTfeklDVJz_-8VhBNwkyeXijjGIH6mdmjYMniBqWittHFIgARd4eqGpDm40lL3pJP6ZyT4jcDiMKvMQXGuhXiTj9BqpTLZ2KP88FDmlqHem_p8K1fHl8YwCtSxZTvmiDBrp7fq2QVQDn__-J3xxuc2D78CWtTOA1_4JEYqY9WyBKoxWOTiYqU0ZvMvgQf80htvvtM1UiOu4NFfA4pkGVnMLV8rOOJz6aJNbLETsrXlJQlPqWwl6uwP2DQjN7-7TB8PUZJ_FFR0gUjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=GDpcqSfDhtPvvRuPDArMzWY0XKUkFc3lQAwQQs5KFTSl4H8qPsFve8mZ05Ivhpkqo_YH7GzTwTfeklDVJz_-8VhBNwkyeXijjGIH6mdmjYMniBqWittHFIgARd4eqGpDm40lL3pJP6ZyT4jcDiMKvMQXGuhXiTj9BqpTLZ2KP88FDmlqHem_p8K1fHl8YwCtSxZTvmiDBrp7fq2QVQDn__-J3xxuc2D78CWtTOA1_4JEYqY9WyBKoxWOTiYqU0ZvMvgQf80htvvtM1UiOu4NFfA4pkGVnMLV8rOOJz6aJNbLETsrXlJQlPqWwl6uwP2DQjN7-7TB8PUZJ_FFR0gUjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QediBx1Q29dxgML7rMtXkLfkgNsmqfKW_lPtZgI7YpIPIarxl4llfRgy6sKKUmWl37bZ_eJhE0EWgtaLvkeYuwJxFbzMk1O1JdIzdc2PK_uFgJKHeknKqFDRiEqqTE6590aJ_MtDiC-HDL8mvue1mjydtaUBUI8h9cbDZWF4mG28jGD7hKkFo6SogQjVDvSdtdwdHHsm32HwNj-FL68mtWNhzTuyx80RSCczPmUeofbG-RwgyAXTaWt-5kGF6_9s8gKv6O1897gWEz__6stKqt4sXFj8r7ii9LRujnysEzVwPHGofiBmlCXTsyg0-33apIPMIY-N2cqp6XRtyVbF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=bf6G4K-TEomHDDPwACrhoeB_1ce_ztF7xYXd-GJ0ViWoWKvBA0vu8h01QvSoOi_sYbR6hEkh0ymPg-hOt4dnEgzK6dgr4hn5GQGfT0C16_YWCA4_VtqRpo5EeKCWDS9Z2IorRwu4FNFG5ITpvIetZGBU_s-qHVmcwFji2ZNd1aY-CjKTS62yLj7Or8wZH6O6kTDWCKGKDyvuFDMTOHsLpcu4odY05aN08to30bU7z6GmWitRgaYAPCaI6wzh-vf-6nPyiG5bgq0_xLmH9Eq0f4KHnuBYyE_jf2hniwmojDveUPzJ_A_t4SjqFUOgoNNgW7h-1M7dv6FY6TewhJeEKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=bf6G4K-TEomHDDPwACrhoeB_1ce_ztF7xYXd-GJ0ViWoWKvBA0vu8h01QvSoOi_sYbR6hEkh0ymPg-hOt4dnEgzK6dgr4hn5GQGfT0C16_YWCA4_VtqRpo5EeKCWDS9Z2IorRwu4FNFG5ITpvIetZGBU_s-qHVmcwFji2ZNd1aY-CjKTS62yLj7Or8wZH6O6kTDWCKGKDyvuFDMTOHsLpcu4odY05aN08to30bU7z6GmWitRgaYAPCaI6wzh-vf-6nPyiG5bgq0_xLmH9Eq0f4KHnuBYyE_jf2hniwmojDveUPzJ_A_t4SjqFUOgoNNgW7h-1M7dv6FY6TewhJeEKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiRn3x9bYIM1gG_dr82pAQXytBZxq3Ewv4pK3S8QOFXftMXkAitf-5EnPeRHXIIqnYhiVqoruKBTqDmQ1AeBQSHVv5LZaKpPqyhnlwDskhlFKC5m82H4kQtztNA9jezV278B5mMM-8qSY_UM8x1IAI4QkkrzwO_zRPUWKwy8dlXSdIyA1djXSD1SWa3DVWhhZ34omcY5Q8vcdjs1iVZt__YOLfyuYQ30QHAXaPvYquGVceGJ6AdMb8jVry-5be1YxS-UN0kY14Pzd-XuYp286BJwar6_kDuEuk2cffiGg5nOIVo-TFbnXdukkYe2Xveoe8xRqZFHC9CFHeSvXwlbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA_NhYlRQSCcNVOalYdQClskeXzD5IOLz_NeKwOE6FJ_Zvj2i9yBjG6GhJW5AbFtSYB4gxpQXAZW-5VFehkWV86kHiucgzFgGlX23ggLcpIXmqNkhuFZZye3tQ80AHYLq2jlxvTgEvosXdhJ54IfL2ujLKtdHeDL_vXdWJex1v6QTwis0aUy48W7txe05NbjuU1gCOCNGcKfs9g3gSuPpBCZ_8Oggb5jTRxOojnBr5dkoNM61RiNY2BY2r1d35ZRlauP-V1aREffImdcHpPGbG-aCCyOUyfkmZDxEsl6-Sh6lbBVEXkyqRDzVhEI6Rd2WoB4zkzm0MyhD5Jm9Bc-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=PR2REoLhPZzCzBplNK7Wq18cNTdtV1uUSkP166tG8e5cG5e_tBEG-j_BrjDEMQ-M3g9eKESOgRB5QxVe_D-3A0dyqWoVNM308iSoIMeUMTbkKK-lmdheVFEs0b8M95-sxyd76XG6ZgFAJ4KuFHnKGquO1yYY90z99xEa530qQOhoGKsP5iHgPHOkPL0uJPNDaDK_RV91IF6E4quY-G8sA5zgPo66IeR9W3-k56frvtD5rRgDB18G2Wcdr6KSde24C2rYi39L_AdhGIywF2U6WzkkOC6OlrVcT6I765oyBJ7w43ObnYj4e7q1ctsE9m8i3XHiEx0eckB8p5b-R3f94Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=PR2REoLhPZzCzBplNK7Wq18cNTdtV1uUSkP166tG8e5cG5e_tBEG-j_BrjDEMQ-M3g9eKESOgRB5QxVe_D-3A0dyqWoVNM308iSoIMeUMTbkKK-lmdheVFEs0b8M95-sxyd76XG6ZgFAJ4KuFHnKGquO1yYY90z99xEa530qQOhoGKsP5iHgPHOkPL0uJPNDaDK_RV91IF6E4quY-G8sA5zgPo66IeR9W3-k56frvtD5rRgDB18G2Wcdr6KSde24C2rYi39L_AdhGIywF2U6WzkkOC6OlrVcT6I765oyBJ7w43ObnYj4e7q1ctsE9m8i3XHiEx0eckB8p5b-R3f94Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op6Pt54eBGCm_59Z0LySqPYn1JgEzf-gaYDtAPN7ssdL8sjJvyp44sVCQRSrTytPfWK4cFMb6-F6eyzfzCtJDUKJWyqRtTKxVL-Vpcd33UCQcI-hv-QBaTHMMvSFc5xqihqoBfIF4U58k57n9pgG9DnIzpDzcIxufPlv2hpKgyD49Ze0xAqbuJKqKiU3sVAPcxMelhmKdnkv7SdG7pVNIhV0FD8BvMhSl3e-rSPU8wyiPViY0w1_iQ67ruTGjd3bJwm-5GQS_xpQLFZf3gOHwY78a1MVvJkSin55bL0cMtcG98gGHudy1KSxnr-JjY_8zhHbqfulTiEmiq74p7BZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=O74EBrTkMXS7C0ifsCQXzJZzGmEZtRc4uUjWsCDaMVLBPK4rYxR2j2mxErkKmyQYs2xBDFVM4ABaA-fVC7PH8UuVrmdgmkHq9LTG-3zZT18cMT0S38SXOwO9zAOpVobV-hO84NqwjqX7Ms1zFDEZLKH8lUcaKPGvKL63bdihN9mloH1zitmQQKaqnkCEfCOe1mPOJmBpZFtWy7e_kNl3o9qH4XumgO5whKxlzVY4PeASszu7WZexnmo6hQF3DQCmHVm6MMG1yv1i8_TuVZcLXFTd6dxQmdjaC20wrmgE8YyQ-1HdnSFXO0wOBBwPbxKKbg47uVwMP8yN9NcOTXdumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=O74EBrTkMXS7C0ifsCQXzJZzGmEZtRc4uUjWsCDaMVLBPK4rYxR2j2mxErkKmyQYs2xBDFVM4ABaA-fVC7PH8UuVrmdgmkHq9LTG-3zZT18cMT0S38SXOwO9zAOpVobV-hO84NqwjqX7Ms1zFDEZLKH8lUcaKPGvKL63bdihN9mloH1zitmQQKaqnkCEfCOe1mPOJmBpZFtWy7e_kNl3o9qH4XumgO5whKxlzVY4PeASszu7WZexnmo6hQF3DQCmHVm6MMG1yv1i8_TuVZcLXFTd6dxQmdjaC20wrmgE8YyQ-1HdnSFXO0wOBBwPbxKKbg47uVwMP8yN9NcOTXdumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2YYCJOA-LXaJxmHNqvCh3m_6pUwwH6y8mgX4AV5lvvbiX3FnElCVa6h9QLb2LXnj-4GHcDyTpDpVhHOHjeb8N45fLvfvR7AWyKLWWSXoE8xeiyHah-apZn_JJzp9bIEXFLVbRTzxvJfI5gUIP35geKt6UcDzC4deWCR2KQjL-DHxsNyIQCBIh0BnS_hiiQm0rmUqD7D38o9RBj6IMVCpktNFVfw8NUsEFj-QYGK79624jjwN5LFliyUHXdm9VwiCvkBLxHAGGp_XF5AAGcrAQaF4j3JUyXd2RolG8mjF4K24STJjsUb5RbII6KR60lsjxq-jclnE7On4hVN4JoFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWISCwIhci2FiyB7EIbc2GyuXQKN3pn-xbxqlKIv3dboSCfNDpa7TB-5LhywMPYCc1sOgNCZ1rCK-72MkwlOFFn8g6_pjeGLiZ9jVktU94lLYocOmxKjG5lVolY8XrLFIlV1mi2VXTY6CQltO7SBJ4KX0WuDPPuINH9qjIWWE8fdShVClzOXsj8V0ZKNlV3KCZiz9PRkAJELo7MCG0EWaJ6oUdG65_WCS2h-SwEvuFW0BpA7lGoe6hv0gIwzFaSES6wYWm2L-0KR743O3nbfVT14MMtmu2QcBGNwI5W7yXDRFj_VudkGmUf978O9Ye4PelhgbB5Jz-b2JcPnANSpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev_JZfTiZtGFp8aeBXo5YSyXtOCyXS8kqxQzlf9OrKYTnx2X30q05P3oBFa0xyZOcdvf-yf2e4nW8hiqpDnwA5eRgWZZQu_xT05lX-_qViXyBdpc6sVE9sRw4M5fOtmW4n1RmgVdcsSVZC4Dl4wapI37uLfgW-s8mqtCUtsawNcdgPBXGeiznB6Qgu_jX82vWAUU5pXph-ebvcfDPw6YDiS21AlgdwOUKP2HioMgVJlADE86iewGpUxP07JuHuHHAprVz0G1-8nm3Igxf40PqZvDvtIymuY5eHCnE3iuAztg4QH3D99ablrRaKTSRRfp1HlR_7lKh3N3NCoDsWiw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=lglm0IQlz0ShpR0BooOBH8-Undvz5gDLJ1i0VsJjx-XbacJojgiV40eCYNbRuXGPx74W2x-lU3H_0AGlXlyWGQLrjKzXOif90V4nAeWOAzUKWgZMfe9lGsU1FkuCRQM-6YseklbMS1B-qD55zmaGvtmoKjdE1-Ig8O087d1FRATkjPZYAmv8Ij-6mCVPMyTJTtaR4QZ_CEJpxVl3iYnrHhnnVVTzQDzs_JwMlZGCO-PNwyFeLxPNNodYZRBIq6hJa66L4bCqj7RSdS8lCix1IRXx8Jmnp9YAC35CoQ8073oT0HZ4TjGbJzuSwMxzaTfWKgp579-90C0-Kz-kHL3IJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=lglm0IQlz0ShpR0BooOBH8-Undvz5gDLJ1i0VsJjx-XbacJojgiV40eCYNbRuXGPx74W2x-lU3H_0AGlXlyWGQLrjKzXOif90V4nAeWOAzUKWgZMfe9lGsU1FkuCRQM-6YseklbMS1B-qD55zmaGvtmoKjdE1-Ig8O087d1FRATkjPZYAmv8Ij-6mCVPMyTJTtaR4QZ_CEJpxVl3iYnrHhnnVVTzQDzs_JwMlZGCO-PNwyFeLxPNNodYZRBIq6hJa66L4bCqj7RSdS8lCix1IRXx8Jmnp9YAC35CoQ8073oT0HZ4TjGbJzuSwMxzaTfWKgp579-90C0-Kz-kHL3IJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=llTwZDMskEQBRMDCdFw6ZVUEnYOfQehtejQ792eryxJwR_fXglcsiMPL3R3_Md6tMamAGq_tPn5SXZJnHbcVbFOJtFPfB4cXiWhMEneYA0Kf-8hNsDlW3Yn3NJrZIZakLNBjtwBzQnD1xSRKTJ9z8h70nrPKNSclNMSmJj4X1jSMeTDRM25_xvmWiYEHEfR50IXCH6dgpl9XUfw2lM6U4_pkUCXhmAScdHNI8fDOr7Ty6pkrY__CvGWyaZLknkASad7nYjJdmssH_WZjgRdt01A-gTgDKNBe42pd7t8r--cJkpT2vzmDmQWm-qmzSyJPcXGbXDnaiMBekKoKjyR7SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=llTwZDMskEQBRMDCdFw6ZVUEnYOfQehtejQ792eryxJwR_fXglcsiMPL3R3_Md6tMamAGq_tPn5SXZJnHbcVbFOJtFPfB4cXiWhMEneYA0Kf-8hNsDlW3Yn3NJrZIZakLNBjtwBzQnD1xSRKTJ9z8h70nrPKNSclNMSmJj4X1jSMeTDRM25_xvmWiYEHEfR50IXCH6dgpl9XUfw2lM6U4_pkUCXhmAScdHNI8fDOr7Ty6pkrY__CvGWyaZLknkASad7nYjJdmssH_WZjgRdt01A-gTgDKNBe42pd7t8r--cJkpT2vzmDmQWm-qmzSyJPcXGbXDnaiMBekKoKjyR7SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=jVFvQ-Pk6a5V0oVdFvqf85uAH-Hl0yxrNWPC9qZ_nGjJ9j_tsIV92yrsz7cSrEsrv6-PfPQpn_A4G8foD9ke1XnLuqBiBFAg0AUgCuOwX9GQ-Txv7KmzPAx0A2rctD35VMH3BXaM9S6xMF0JbDfrmACmpQZS6JXN_EAtdNfw1YGSm34ShE3UlatfgX0Y9DwJIrP_9848_9dREHaAdY-h0Lzax6rWtvjDHD0NQcUPBEHtIxrbzmnLKEoLU5xEyb38goEhRMtahbb1Xn1-bi8ZXYH0HuRJV4VxaGCiOezuqsbMcDKxxoHar-9owBgNYgIOAGugLSR3mnCoLZB6dSaaeWYmf_4Yjnjm7of8dW72cY9CCUZ809RbG3zIyjtydUFwed9CBWYD7FfPCPePKNQM7akrQE5Lz1QwnNTk-E893P7AQXPedybxR_tiMh2WfnTavr1wSXVdjeFKSOe5CDFBASw_jRKMr4Ds8FiQPT_xuSv09c-5_PG0sAJOz5HOfK2SLNp0oBwVXnohGMLur24qf5xgrK0BjDZwrY6PI41TIZ4Lf_-xpFAqtP1NyS0_9XqXSFUGJbsd42aZVRqdwNBhxDDeJrA7DIInxBVJr_sk5H_UnqAIIrhx7zLAgIToIeL-QKOBPgR6QOW42KuIALNiJ4pVPiUe4VmB_qoDdp214-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=jVFvQ-Pk6a5V0oVdFvqf85uAH-Hl0yxrNWPC9qZ_nGjJ9j_tsIV92yrsz7cSrEsrv6-PfPQpn_A4G8foD9ke1XnLuqBiBFAg0AUgCuOwX9GQ-Txv7KmzPAx0A2rctD35VMH3BXaM9S6xMF0JbDfrmACmpQZS6JXN_EAtdNfw1YGSm34ShE3UlatfgX0Y9DwJIrP_9848_9dREHaAdY-h0Lzax6rWtvjDHD0NQcUPBEHtIxrbzmnLKEoLU5xEyb38goEhRMtahbb1Xn1-bi8ZXYH0HuRJV4VxaGCiOezuqsbMcDKxxoHar-9owBgNYgIOAGugLSR3mnCoLZB6dSaaeWYmf_4Yjnjm7of8dW72cY9CCUZ809RbG3zIyjtydUFwed9CBWYD7FfPCPePKNQM7akrQE5Lz1QwnNTk-E893P7AQXPedybxR_tiMh2WfnTavr1wSXVdjeFKSOe5CDFBASw_jRKMr4Ds8FiQPT_xuSv09c-5_PG0sAJOz5HOfK2SLNp0oBwVXnohGMLur24qf5xgrK0BjDZwrY6PI41TIZ4Lf_-xpFAqtP1NyS0_9XqXSFUGJbsd42aZVRqdwNBhxDDeJrA7DIInxBVJr_sk5H_UnqAIIrhx7zLAgIToIeL-QKOBPgR6QOW42KuIALNiJ4pVPiUe4VmB_qoDdp214-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6bYORpG_zB1vMV-75aTpZNMIHUrnng8PSKmTvcXqoT2rCR3SDW5E4DA7TtL8ZFVYWRvaP9l1AM_NKxSKzMv3FBlUKRXOFhHIQhmlikC1eGXxuKLm6i9kMDtn4zBjJWHdxP4Ilch66zL07x61VRwcXUiqzO11vot9Hs4O0tif0tSD2Wk3zzfSqccA00ivY3vYi4lrN50UdKDE7X0UYY1bpz2fdSvmsmDXnUpkt0_5yzl6A2Do6_OZa52Hc-jfD2dHDNcQtr9VG_XKYNbBSsDTj7KdJ8HahIRlw8ijMmuoY7uFWD2DBfKDEv0eIVGUnFCdLBLWqxpJgcBLsPVd0rJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-S7ieg_6wVMfv1_GR9NkXbmq5y915ZJ0aEjjhQhdFOKi4lDeklsLun9qwWu7WHHxOKhZT6WUhQO8sMbcxmwADQrT_fGW6Lnsw1pkF-nmUj_jR3X0fVL4zRb9fVt5kFN1Ywf1FhqDvKNccL90dnZjLGEfduszsRPXUS_HTFt7RJnUn2X233IQkHmu455aZ1_yYEuO40T4MHceiasJY5PWDcZvS7jlIPC2wfd5i11AuLMBLcjh4M0oshp1nLcgGqLlEt7_zz6a0BAZpv0WYjlhh1NudTlwvqK0NuS3eSzt8ewDS1Zg-wktlwgrLH38pzkgR_0kYbj_XnOxKVRTrca5TzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-S7ieg_6wVMfv1_GR9NkXbmq5y915ZJ0aEjjhQhdFOKi4lDeklsLun9qwWu7WHHxOKhZT6WUhQO8sMbcxmwADQrT_fGW6Lnsw1pkF-nmUj_jR3X0fVL4zRb9fVt5kFN1Ywf1FhqDvKNccL90dnZjLGEfduszsRPXUS_HTFt7RJnUn2X233IQkHmu455aZ1_yYEuO40T4MHceiasJY5PWDcZvS7jlIPC2wfd5i11AuLMBLcjh4M0oshp1nLcgGqLlEt7_zz6a0BAZpv0WYjlhh1NudTlwvqK0NuS3eSzt8ewDS1Zg-wktlwgrLH38pzkgR_0kYbj_XnOxKVRTrca5TzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5bEufSZb61YeeZl9e8X_iLZDiG1xNWSTU1l18gkX7EbCdjkvIiawQo7ed7-CDU3JsD3sngyaoAuKLXJJMno-0wcgIVlg2TGvHYZ00snmA2ZvkS5TShsiEII_gbO9WwghLVcME-8Slmx7ua4yiCIyusjoC-ijTd97dpVw_PzxKeHZVSwVYEjVb24gNLX73B4y3z7MyUCaTI_Y4QQvfl8s8mjGvrBa8iiC2iOBmJCgjW4KL45r78RgbTLUa_88bbSI49GxllJ7XZ3zA4nBv7Qw3eXwkewxmBy4H8gOgYpm5rGU_RSHDGKDHdM1_7icW5_IegSHkZ2PHqq8ZT0MBtkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZH-mODpNahUol03My4IC81LiKrxzTqOTB0KlE-8VddzWbOfcSmQbQienifgZsCaBmdQybh8zmTv9_KtNZs6ggL6qmi9pr3eyVBKQCmoANCgmOE-RzxA--eOT_E6UQVmtF-qs2ghT3rqCYgPbYDldssvOwXhLn2E04lrKAPHVwfjiTr-39BRVZV1yAvNWxqWQvDWrNybFI-uuC4HePsNQi-mubQ0qk7mejtod-ftv_1ldsgZtteL01lywHlchgVFV4QeJu-X6kJdT9bRcF6lbHmN_BP-b2EAXajdVs3AJz38Ug5foWXaqxrD6e3RLjhz1M8H9AmDRpocM0tXNIzTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQFrLRGiSOFZlXka92NArytNodcdDF5ZaTWBWHh1FOZ5MkhFqf2ok3WXJwfD0IoaxlQUhfLgXLAUszifAaUfbsIDeyrVIH-lz7FaQkx3fkFu7h5lOHim6OTzLusLj11n5zHev5FRazumz6b22Qhej0JUeM3Uz5cZR7YOt59Hpe9_qwTSu0grZGpG7sga6D0FJdwb2BUIfiqMokAw5Hi57BVChXQuC1moZtR1e3GCnMSvxw5MFZGYtZ0le7pWZdWEMg3Zk-dLEL5NsQDDXY-Or4DX_9LPy9Bd-S95FZGpezB9TcrYIAMAGZB5XGlqq5bju0C9Dh97UW_UCq7__P1siA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGbPcU7982A5HAfOya9Gr2kLIM_HE-rB-E9S62XfpSPm5N_uxCPCKWycx_CPBSGhAsOlOLa_ZtePOEYi2aS8YjcuIeMA9k4xPnho4xzf9WYmoZAG5a0N1_Hc4F6DneNfJRbmj3jeFAGMzKvNB6mBgpT9WNJ8uVCsx23tLqtsiPG-hJE3Q5-KUtILSi7GXmKvFsN9HmcR7yLTlRFMWU9K_gZbm9dloO7qiwpGtLE8MhADeU3T6w0zx0Zd6KdKjVwucB_3Pz1bT9YbBBQc1fRJHdA_40z__2eCmtztHETVYJfLSIUMElxImPGwXE7CWGJ6FtjDiHwQ2f0ckBSd-SjR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8RCdvUqWB36GNjcXi73a9kFPJLs5M2iEnJThEH4YQS4WwV3H0XkByj9uJHApv9lYNhrLREBhMqY6h-6jTShwK_kWDH2gBYdIUCSQIrSqoRZUzEqDMWu5GaJIOlNqpQqeE4X9kWtWvQ7V77MDN6tcUratkWqWbNZ6J-ZuxqeoCdxUoiX1VG7LswJ6eiAo5916XShy927B6E8NG4_bz9xsmRf5HI19O7DJk5_OFyBl4KDh-A5EbN_i7Wyg0whE39dDW5Svwe7bhzyw20l4lHdDedgOeAQWqV-yYDZDd_VTZRhQobxwrCuYaCYplDx2PV8rfvssOsqW69Mj-ycTumdjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVpN_2CH_JPh3pZ5iZFS5p9XAvNZ4eXFOCJkfKGXR1XyZQqWou6Vq9CMyNmFf_nQV-LVGcE0z7ggakxd3_W4erR5tFonCAB2ArgU8yvJ7BTNjPfbmRQ4AwKHCdubLwRxmJTbl2kyG97cSpG_Kxqdun3uzYOr1-kRmLP345KsmIyo100s7z7F3iLl5MBKZHUghb9JsWHplSf9SETHMBTPyxBV1GW2XAPk6kcEgsdxwEHtxHnALxaA4GPPiciFhKuRiE_kxvASv1jjC8U1KRagbOaxvb837F5QECt7TADXRLw9q3gXV5B7Ft2qQQwE6vU6bZImhaHy20eKjZddmM2_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=aWi0vTGlQL_BhlSNUaKr-TL6DZcMGXbxvPdguwZl8Ljw2nPSECJOxDqjKHhMLxUF2-tFZB5PjZHtFAMC9Hd1stodOe6rkqG9yh_izpjLUHtaVV35nm0zpBYKIsS7TTzpwNnsKV4GFI2RE0QZGDGLSh-Tu2Le_ux_rDVzIhGr4FDooXyZQCERuDQXz0qDeVeb092sKLfTCP_uUjL5hyRxqfmVxQ9vmNuAVypda1H4_3KoSk2zbgIn3xVwATQO83NRk6uq5sct1IebZbVmizo8yoaWBGxe9QavAD-vLZ1KG_fK8wqYf9MHpc-eYSGcxV__ZQZTWdQwLCDJc1wzgW2wRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=aWi0vTGlQL_BhlSNUaKr-TL6DZcMGXbxvPdguwZl8Ljw2nPSECJOxDqjKHhMLxUF2-tFZB5PjZHtFAMC9Hd1stodOe6rkqG9yh_izpjLUHtaVV35nm0zpBYKIsS7TTzpwNnsKV4GFI2RE0QZGDGLSh-Tu2Le_ux_rDVzIhGr4FDooXyZQCERuDQXz0qDeVeb092sKLfTCP_uUjL5hyRxqfmVxQ9vmNuAVypda1H4_3KoSk2zbgIn3xVwATQO83NRk6uq5sct1IebZbVmizo8yoaWBGxe9QavAD-vLZ1KG_fK8wqYf9MHpc-eYSGcxV__ZQZTWdQwLCDJc1wzgW2wRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqqiC48vum70vWzsh-0V_yrE71bXAnKcmFIZROImMuTddA-9eFiZG4ZyD87CQiSWekV5L9umdNKq0bIHHUXy1GFfcw9-67lmbZyn7ZuUIb7YKXxqBzam7Wpk8kMssV-zSSxOpv22SegpFWC7cyREkCc9AFwPpTb8PeAZ6SMweuX3amb8NYWgSgMNirMdhyF-x9FKEUapeJjsMV0ct5B0qTYOpuDdNFGvinI3UrvmXOlSX4Pi0jqmotLNFBfNtrj6b2HHWx67oIzpd_Oy-l_OXdzNUvx1JTfsNCk05N_SUjYwt2wGFlY5C4Y0_v3sfDA1pkfg67lWrU29x1I9uequaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnVkshfnHxwRAN6-ltu1N92C7uZeQ--AaWZ1-ujhC-YgKkD1g_Bj0xXi5quHqfydCicgG7-RqbRdYQ2q5msgnHfE4DFfhE00nTt8Yy7Nt_VjfJKrDkqe1bVSufq_B0HxFm3ZnUWD8xbzjSDN2thOkpCIHbFmfim--F7-Cb51HgNteaeeZNOWCopJ9fKiXCuHfQYxhD8k6HRs1ui1rJ0eCBvHRt03egxCoW8xMTRp1FPfXzIhxG1TzLisCPr2NxU025scu07KcfmWbMNPGqqYc1MMTkcOr2h16lYD-yTXMXaV_u9zTA4GYdFIZMtHyXWyqlHfJ_AOBiRvZmZQ27HBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kj7UMU_a1sXlHRxzymDJahCSxYpTJyMKPgSX2SUk0JMXenAl1EY8tTaIPRuzqH--9qrN3FyQRQd-Ma5OsHSEDOmfYfpPGKaWI55e3basMmvF1L6_8bG_PrvF5H0ov2SKd5NzIjXvmBWfObL3ik6sPr2_Gi1i0J_8XbO_h_uhUlRpn8jrbMkk4gi_oLTEgZbdhdtUHD2t5gO6msBRAtthCxPz6bF9jCMUlgEnlK3EKSdzMPqpYw702E59Is48genpRW-WfPxxRCp9PHgHISpTBF1K0aKxSeLMK_Om3QAQwrP4em1G0ciWesvjAsnwutwcY8loRarZVYM3DGHDCz9oOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=nS_jCMXHl0vvB3JrSHr7pj-DS9Az4LN8r-mTDioghUR-OCjAggOTOBF9-IyGkKjCg-4Y5kyVR6StHiPGT4pKnxcwBvVWMBE6-oUVwVcYYDIvRp-eOqJTD046y31ymdIu3WghVvLATXj6-jUxgLx50UQxSOylJ88W4YlNmnKHx5neCOA-v_UAGqgIeT-ceNvQKh6aMbmYFB5FOJlnJkslpjbLK8N7qsoYhoBugC_EAbZns1i_gJdqi5gHYTMHhGx6w9TDXr9ry7pQLwAbkyXo82xnfsK_MxLoQxqYL9sm1KjlhBvp4FZigF2oGL-2_OGBfhNM4mVqEmtGB5T4hsTh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=nS_jCMXHl0vvB3JrSHr7pj-DS9Az4LN8r-mTDioghUR-OCjAggOTOBF9-IyGkKjCg-4Y5kyVR6StHiPGT4pKnxcwBvVWMBE6-oUVwVcYYDIvRp-eOqJTD046y31ymdIu3WghVvLATXj6-jUxgLx50UQxSOylJ88W4YlNmnKHx5neCOA-v_UAGqgIeT-ceNvQKh6aMbmYFB5FOJlnJkslpjbLK8N7qsoYhoBugC_EAbZns1i_gJdqi5gHYTMHhGx6w9TDXr9ry7pQLwAbkyXo82xnfsK_MxLoQxqYL9sm1KjlhBvp4FZigF2oGL-2_OGBfhNM4mVqEmtGB5T4hsTh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=oE1QDwhpv6uP8UGWQmyDd383NU-u1oAQdUbiJPm2sHdtKFBCnZk1FzlJ6dWTzRe2kLdSGHuakP_N0-VCj6uGLDtLLTRe_jvSk_HoeZkx5fM8D7ljhxH6nLiJ5IxNnkFdQVOgreJTSsgMGZvHxgsovpGB9Ax9JdXWLroHG4X4yZ2udNakHVi5tH6r6a2qXAQE5geVKV75R4-haumnnKFwahZ8QrTgwh1cgQICLVq4yFctZ2z8EgwFir3S3I8bjMX8oB-wu2M6YKo_DoHimiuBVXTrrHiCvsS9oa4o4PKDhO1s-12C6duXbW8NbQlQd_XZYR_LAtW0dZRxOC8c5IvyCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=oE1QDwhpv6uP8UGWQmyDd383NU-u1oAQdUbiJPm2sHdtKFBCnZk1FzlJ6dWTzRe2kLdSGHuakP_N0-VCj6uGLDtLLTRe_jvSk_HoeZkx5fM8D7ljhxH6nLiJ5IxNnkFdQVOgreJTSsgMGZvHxgsovpGB9Ax9JdXWLroHG4X4yZ2udNakHVi5tH6r6a2qXAQE5geVKV75R4-haumnnKFwahZ8QrTgwh1cgQICLVq4yFctZ2z8EgwFir3S3I8bjMX8oB-wu2M6YKo_DoHimiuBVXTrrHiCvsS9oa4o4PKDhO1s-12C6duXbW8NbQlQd_XZYR_LAtW0dZRxOC8c5IvyCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxDvNejkbVbdYpLZgwXSSKf95gk_T6CRKE-TlLj4Qn-3_vHQpwXtRxvKRgXqQis7z8ztxADS6t4wEqiKaV83iQtM6mrhyOWITA-JIs1OyG3HT0gUg8eGFUtASGXcMB3WVHrRgWyaFK-QZrYBLjCtigQx3dQ_9YIlZQkTsLtqsPaPjeUMv5u4xevnAb3f-BbD4gY3BINvn-8llTC0ZObvWeFrQEyKuhuNr7L2SadzyzS_IOc-t6-YdNLjwY7KY8ZPCgddM1F_cryOxvfWmWa4QMO9dUq6tU90sDJUMIdeEL0PR7acaK0IWzPFRpDrWA0F8-1teICFQExeeJwmujyfczjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxDvNejkbVbdYpLZgwXSSKf95gk_T6CRKE-TlLj4Qn-3_vHQpwXtRxvKRgXqQis7z8ztxADS6t4wEqiKaV83iQtM6mrhyOWITA-JIs1OyG3HT0gUg8eGFUtASGXcMB3WVHrRgWyaFK-QZrYBLjCtigQx3dQ_9YIlZQkTsLtqsPaPjeUMv5u4xevnAb3f-BbD4gY3BINvn-8llTC0ZObvWeFrQEyKuhuNr7L2SadzyzS_IOc-t6-YdNLjwY7KY8ZPCgddM1F_cryOxvfWmWa4QMO9dUq6tU90sDJUMIdeEL0PR7acaK0IWzPFRpDrWA0F8-1teICFQExeeJwmujyfczjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWQjMas-UA4_p-zgyxMZ5C8wuMHf9QltNXFylNfLM6yCO1x1mzAMJyWNu_r3NF-jLAAO7wRIbJJgeDy9kj50-B3p0G4QDsp9iIjxtWNK0IE34h1An1f8zEzhRDp7zDzJTIxanKKIOfMdKB5hxWCvH0SZAW3vlGVqR0jqm1WkTGVSrBmry2ByY5W3SkKf8DsMhqI66c5ZhRXRXZwZwvgH5eMU9HiRWHzAhmKGvG8NR0E8swtH83qRaDxHHMjfs6TzWZ8uiy5t3djCi7fUiVy8_0BcD7AYgv7HINWkOUhGXMGeC9zmFrXGbE7CO0561B_PacfUsWHPsFsnUgceD0RWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
