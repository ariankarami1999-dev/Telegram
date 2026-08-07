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
<img src="https://cdn4.telesco.pe/file/gWifMOeti4AiOPQU_FI4zCHOaAdgxrqeXbzynWSQUzlWwRcfBCYJjWQLBiTFbhnTA0dLHo39_FkghtME6cOEjBmunTvvIsTTFdmshRgxwbYIShUBuv43MKGn45qxcmb9-sexRQAzyp7FGXVU_YPlnglqMQoJvF7RSvCvsy0bgJdu0E89DghmXRVX-gHahk-9-9TeinoVcwtDJA-RzYD9w9pqDo5091w87TLKGzn1Isef0sko3QxWZnq944Z61xBKrB8WgGwRPrxpyAYY_P4kVCIbsFgjUjcK0LZI0iVcTTDRNr4OTtCJxm_MWkEQAZH_SSnjvlL_dkUgiFv1-C7rzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 20:12:26</div>
<hr>

<div class="tg-post" id="msg-679237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb0UzQhH2n3-7pQBztpa-oJuik7IQs4m_p48UWvGFJiN7SKsIPQkDQKlsGgnoov1s0svV1FU-8e4lba644TPJ42yCmKLfnii1HSU6imyX-c7K6E-CoVUqOOF90Brx0KltqObxRgYa5Yv5YT_hc3mAjAa6SkcRfVQKvlTQDLUkGkn84RFc5TU3ypZEvcRUvpSWodcZaAE1zUFo0mBw3Ko3asD0tF6dq36J5mJWcX7udfCi231JCDUb96PF90wFT_gZ7BtBIkS1LVVtdAOJzNMJGk23-9GXbQxPVVGokRJAD1Uraw6zwpMZb8YK3tHXg1MypmWXHn21xba2Mkc2zihag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/679237" target="_blank">📅 20:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFHI6kmQ18NMpKw_FmRuQFYWHiuzwfS4JQvDaD2rCNaiBKVNbCRyLvq18_GaWb69vXqm9_fsOiANV_8Vh9n39GduAtYDqea9GjoNbWATqs5Lz-DX1CjilMFGobfYyBS98v4JhROYCZdmEjgW-AXUnX5ypGsaSmj0y4OpAP4ngkLC-6uP6rlS4aQp5aLIz1ilxRWCNFYNitJUyvjOf7i5lgxY2OaqVsNVD_bl3GSEGC4FFxyHAAB_hn0RITP3cd7-IGZs63VNHvh2V7ajvSLpDEoSbwNLfwF7LPGL5_Rfy6yYLUdgZIacmuqm_iYEm1KPe0ebqvt_hVrzffJmTFdjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار ناامیدکننده اشتغال در آمریکا؛ ۲۳ هزار شغل از دست رفت
کلش ریپورت:
🔹
کارفرمایان آمریکایی در ماه ژوئیه ۲۰۲۶، ۲۳ هزار شغل را حذف کردند؛ آماری که برخلاف پیش‌بینی تحلیلگران بود، زیرا انتظار می‌رفت اقتصاد آمریکا تا ۱۰۰ هزار شغل جدید ایجاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/akhbarefori/679236" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
به تعویق افتادن پاسخ مقاومت عراق به تجاوز اخیر آمریکایی سعودی
🔹
مقاومت اسلامی عراق در بیانیه ای اعلام کرد که در پاسخ مثبت و همراهی با درخواست برادر مجاهد(هادی العامری) و همراهی با مواضع شرافتمندانه برخی رهبران سیاسی شریف، تصمیم گرفته شد پاسخی را که قرار بود امروز بیست و سوم صفر(علیه متجاوزان سعودی) صورت گیرد، به تعویق افتد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/679235" target="_blank">📅 20:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd4d4d968.mp4?token=TaQvjzTomaS0tk2ZAFIDP4M-vLgOQpk-m2q1-0DxsHoJgJWhJs9lr59sD5EkVaFD-lrbZZvDqKSQlrI737Y-JUb2JiDMe62TCps32JTi6ajR2TG5ZnAtE39922NgJFxh4dmt4GEJCGjbM9XwHCYneE4c2Xj7U4wWcS8mxHaiPoXKk07EO82Dn2RQsEUuUPvIVev2umRk8M6x7IqZaUbMRlxeK1yA27S7_AirJ9fNMhf_XFwgMyH_E9tzDpLyiLsySnm9AtObbW6DpShJuPaFzoSJzTZt9OCoQ_MnaQ5_7zQgQiHvFB2OirIAMAgw8FTEBf42-8ibvGu0vQt5Kd70pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd4d4d968.mp4?token=TaQvjzTomaS0tk2ZAFIDP4M-vLgOQpk-m2q1-0DxsHoJgJWhJs9lr59sD5EkVaFD-lrbZZvDqKSQlrI737Y-JUb2JiDMe62TCps32JTi6ajR2TG5ZnAtE39922NgJFxh4dmt4GEJCGjbM9XwHCYneE4c2Xj7U4wWcS8mxHaiPoXKk07EO82Dn2RQsEUuUPvIVev2umRk8M6x7IqZaUbMRlxeK1yA27S7_AirJ9fNMhf_XFwgMyH_E9tzDpLyiLsySnm9AtObbW6DpShJuPaFzoSJzTZt9OCoQ_MnaQ5_7zQgQiHvFB2OirIAMAgw8FTEBf42-8ibvGu0vQt5Kd70pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد نماینده کنگره آمریکا از وزیر جنگ: او دروغگوی حرفه‌ای و بی‌کفایت است
🔹
با کت‌وشلوار شیک پشت تریبون می‌ایستد و می‌گوید همه‌چیز خوب است
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/679234" target="_blank">📅 20:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وزارت خارجه آمریکا از وضع تحریم‌های جدید علیه ایران خبر داد
🔹
وزارت خارجه آمریکا در بیانیه‌ای اعلام کرد اقدامات جدیدی برای قطع مبادلات مالی با ایران انجام داده است.
🔹
در بیانیه وزارت خارجه آمریکا آمده است: «اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/679233" target="_blank">📅 19:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
واکنش امام جمعه اردبیل به سخنان باقر خرازی  آیت‌الله سید حسن عاملی:
🔹
از دستگاه قضایی سوالی داریم شخصی خبر دروغ به رهبری بسته و دفتر رهبری با صراحت آن را انکار کرده است آیا این جرم است یا خیر؟ قطعاً جرم بسیار بزرگی است چون علاوه بر ضربه به جایگاه رهبری هزینه…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/679232" target="_blank">📅 19:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گزارش به مردم| قسمت آخر
🔹
مشارکت داخلی، سیاست خارجی
🔹
قسمت آخر گفتگوی رئیس جمهور با مردم امشب بعد از خبر ساعت ۲۱ از شبکه های خبر و یک سیما پخش خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/679231" target="_blank">📅 19:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679230">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=vMIOrY3hf4Ru31-j7cKgSRom40co-7cRGShtPxpbt_Z6igCD5vW_iGpLSRTuc5KCSYjz2sqH0OHShK8IdQJcUIT2kBNUQ55LDPJuHie5fhvkDIxUrLgK900HBlNzO6h5hH4fyXAhB0RymTjXHNot1jULT7Z6EVToD3AOMWRJQ5tw673CgRprVEuGws2D_sSc2Comj49rpbIJ5_0IBkGzVavtvVMLTlZYmNngymSlxoPAJk_7gGz5L3Jlm02jP4cBOkwyoGMz8tnbrTRdkd_lMYh_J2d5etAK9-uQ28s-Ux-gCNRF2vm455RPMUHiCQ8Fb6CkJVgZCNJYRTGEFHvXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=vMIOrY3hf4Ru31-j7cKgSRom40co-7cRGShtPxpbt_Z6igCD5vW_iGpLSRTuc5KCSYjz2sqH0OHShK8IdQJcUIT2kBNUQ55LDPJuHie5fhvkDIxUrLgK900HBlNzO6h5hH4fyXAhB0RymTjXHNot1jULT7Z6EVToD3AOMWRJQ5tw673CgRprVEuGws2D_sSc2Comj49rpbIJ5_0IBkGzVavtvVMLTlZYmNngymSlxoPAJk_7gGz5L3Jlm02jP4cBOkwyoGMz8tnbrTRdkd_lMYh_J2d5etAK9-uQ28s-Ux-gCNRF2vm455RPMUHiCQ8Fb6CkJVgZCNJYRTGEFHvXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطریانفر:
پوست قالیباف به اندازه‌ای کلفت است که خیلی نگران اهانت تندروها به او بابت مذاکره و توافق نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/679230" target="_blank">📅 19:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679229">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: تنگه هرمز هرگز مثل قبل نخواهد شد
اسکات بسنت:
🔹
ما از نظر اقتصادی ایران را خفه می‌کنیم؛ آنها تورم ۱۵۰ تا ۱۸۰ درصدی دارند و نمی‌توانند حقوق ارتش خود را پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679229" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679228">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKj7McahBnKF_53uBU_8DkZbHLEJvrHqtgU4JKVtkABTkYyNnlpCgdixNKTN39EPd2LVhRgbRLFTe6bRjx9ewsjwZKKYO3vHs9tNXqZ1W_xY9ns6nuHUgqcdWCCFxeEsuPzVtDpykMdJzRESoYDCaZCLMmlW7NfB3RPNMvlusBj7qbugYpVkcZJL97BORd2PeRocS8RPCyHNwF1FzSbYXHCzfgvAgD_JhIcdJi0fe2BYIoiMN5bWSP0ZPDh-RLUVyH8uh0jMzqOQfZyJHkNGQeVk-a2v5I_a_MFs7QygTKNPa-GiZwqYoPTl86u7m6D5UZUqb0EWTfR3X3sBKHRoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین زمان تعویض لوازم مصرفی خودرو
🔸
بهترین زمان برای تعویض روغن موتور و فیلترها، هر ۵ هزار کیلومتر و برای فیلتر بنزین، هر ۱۰ هزار کیلومتر است.
🔸
لاستیک و لنت کاسه‌ای نیز بهتر است هر ۸۰ هزار کیلومتر تعویض شوند.
@amarfact</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679228" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679227">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e930289fa5.mp4?token=oaGG89CvfE5Kx59u3o2vPHvmNBXpPAaIK10KrF70JG0BTdl4R2ujdev8rOMsx-yRfg-96tsXOrQWR73VIZQFAlOchyNd8fhp4FGWBFN6PDLC2vjz9PMCDi9ttt-mtocd6Lv0056-_dpxSypbqU8XeYRvqZJZKV4iRZfjreXxzuqGrajeTFnqAcY7mWMnyOjt92pVQHFnToDpzJgqxyEHgFY2mCy3LV-xs4Rpo9CMnEBjC6PnlHDdZTexF6WRetw6Ofw-Jg0s4tSIYpoPQlMdM-F0MCWEWBhzPQKFp-tRR906FNCSQ8QqnszS0jpQAYgMjAYrUPYSIePeCzRbZxMIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e930289fa5.mp4?token=oaGG89CvfE5Kx59u3o2vPHvmNBXpPAaIK10KrF70JG0BTdl4R2ujdev8rOMsx-yRfg-96tsXOrQWR73VIZQFAlOchyNd8fhp4FGWBFN6PDLC2vjz9PMCDi9ttt-mtocd6Lv0056-_dpxSypbqU8XeYRvqZJZKV4iRZfjreXxzuqGrajeTFnqAcY7mWMnyOjt92pVQHFnToDpzJgqxyEHgFY2mCy3LV-xs4Rpo9CMnEBjC6PnlHDdZTexF6WRetw6Ofw-Jg0s4tSIYpoPQlMdM-F0MCWEWBhzPQKFp-tRR906FNCSQ8QqnszS0jpQAYgMjAYrUPYSIePeCzRbZxMIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخت بائوباب؛ غول آفریقا با توانایی ذخیره حجم عظیمی از آب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/679227" target="_blank">📅 19:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679226">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
المیادین به نقل از یک منبع در وزارت خارجه پاکستان:  به احتمال زیاد، عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه به پاکستان سفر خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/679226" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679225">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJCULMDbM9HOjG-Ah98jYlzMTB4numXzSwAdD5mvLbssimGcfAQDdvyNqqwEHKtJd0cTcCrfolJCdiC5iXgq3OnbkUWZzFuE-1Zlie845tn4qdBW77l7BKxH7TBrFalF6sRIXQZajKsnShfEqUgFKp_dSbLJdwqqvWTKK2aE95sAU0snToUDvPbVi3i1P7YA0_AuIg1HdIKff3MHkwyXDSgTlx5nMVQ7Xl0FOd-U4EEdgB-VLcSurRrpICuZjXBuhiuBk1W3cBkXapYUTbC_7vAM2w-2ih4nkTxfrU56t4IkA-FTK5hgkAV4xNbJjLsX8t1HZAD5jIo4Yse77ZySUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/679225" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679224">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج آزمون ورودی پایه هفتم مدارس استعدادهای درخشان (سمپاد) اعلام شد.
🔹
شرکت اماراتی آدنوک: ۱۵ شناور ما در جنگ علیه ایران آسیب دید.
🔹
پلیس راهور: مسیر جنوب به شمال کندوان و آزادراه تهران-شمال مسدود شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679224" target="_blank">📅 19:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679223">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
غریب‌آبادی: امنیت خلیج فارس باید به دست کشورهای منطقه تأمین شود
معاون وزارت امور خارجه:
🔹
تهران خواستار حل مسائل امنیتی منطقه بدون مداخله بیگانگان است و حملات از قلمرو برخی کشورهای همسایه را در شورای امنیت ثبت و مستندسازی کرده است.
🔹
او افزود زمینه برای ازسرگیری گفت‌وگوهای امنیتی میان کشورهای خلیج فارس فراهم است و گسترش درگیری را برای امنیت کشورهای منطقه خطرناک دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/679223" target="_blank">📅 19:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679222">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
رقم تاریخی اجاره کشتی برای انتقال نفت عراق
رویترز:
🔹
اجاره یک ابرنفتکش برای انتقال نفت عراق به ۲۳ تا ۲۵ میلیون دلار رسیده؛ در حالی که پیش از جنگ حدود ۲ میلیون دلار بود.
🔹
عراق همچنین نفت خود را با تخفیف ۲۵ تا ۳۰ دلار در هر بشکه عرضه می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679222" target="_blank">📅 19:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679221">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
گزارش‌ها از حمله موشکی نیروهای مسلح یمن به مواضع مزدوران عربستان در منطقه مأرب خبر می‌دهند/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/679221" target="_blank">📅 19:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679220">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1zc-fDI_nz3XK-TF9DpQLgzkEMRBt5_lBndxjRJy98r32pZNhpoN27I3F6jOuZuAiFllLqbxvzU9uN0KHLZtJrgRCbIlM4agtXNQ-3QUeBZUMwZID_ss7k5S5_4mc84rXQKdo9dXQORrb5oO-cRLxl_aMHqTLtpzAa6EsZSBxKcDAEf7ChXBOFxFvmrPgCKeb6Fp84b0zvGnfY4WMMF41iBhW-bhbLF2zqlsWofy4wLiFiaEzxDotdQ48OHB-lj-CTNNschl9c9nb6q53makQEincXUcus76aFQXN-gPloJs4lfZq_UNyKr0ct_MCRzNWokRtNtbNwF_R9LyF6pBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ائتلاف نظامی عربستان - ترکیه - پاکستان/ یک مثلث شوم برای محاصره ایران؟
🔹
برداشت ها در رابطه با سند مکه متفاوت است. برخی معتقدند این ائتلاف، آن هم در زمان جنگ و درگیری ایران و آمریکا، به ضرر ایران تمام می شود. برخی دیگر آن را معلول و پیامد جنگ ۳۹ روزه می دانند و معتقدند این سند واکنشی است که اتفاقات جاری و وضعیت سوق الجیشی منطقه را وارد مرحله جدیدی می کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236126</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/679220" target="_blank">📅 19:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679219">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پایگاه اینترنتی نیروی دریایی ترکیه: یک کشتی باری با پرچم ترکیه در سواحل بندر نووروسیسک روسیه هدف حمله پهپادی قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/679219" target="_blank">📅 19:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679218">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
گزافه‌گویی
ترامپ جنایتکار: قیمت نفت فقط در صورتی افزایش می‌یابد که مجبور به حمله دیگری به ایران شویم
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/679218" target="_blank">📅 18:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679216">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای العربیه: عربستان سعودی، ترکیه و پاکستان «توافق‌نامه دفاع مشترک مکه» را امضا کردند  توافق‌نامه دفاع مشترک مکه:
🔹
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔹
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/679216" target="_blank">📅 18:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679215">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آقایان مدعی! زخم تازه نسازید.../وحدت، سنگر این ملت است
🔹
کشور زخمی است؛ زخمی از سال‌هایی که بر شانه‌های این مردم، تحریم ناجونمردانه، گرانی، جنگ و هزار رنج دیگر سنگینی کرده است.
🔹
مردمی که هنوز ایستاده‌اند، نه از سر آسایش، بلکه از سر عشق به سرزمینی که خانه‌شان است. این مردم دیگر تاب زخم تازه ندارند.
🔹
اما گویا عده‌ای، رنج ملت را نه می‌بینند و نه می‌خواهند ببینند. آنان که هر صبح با کلماتشان بذر اختلاف می‌کارند و هر شب با شعله‌های تفرقه به خواب می‌روند، انگار از ویرانی وحدت این سرزمین ارتزاق می‌کنند.
برای آنان، آرامش مردم هیچ ارزشی ندارد، مهم آن است که آتش اختلاف خاموش نشود.
🔹
تریبون، امانت است، اما در دست اینان به سلاحی برای شکستن دل‌های یک ملت تبدیل شده است.
🔹
هر جمله‌ای که می‌گویند، خشت دیگری بر دیوار بی‌اعتمادی می‌گذارد و هر فریادی که می‌کشند، زخمی تازه بر پیکر جامعه می‌نشاند.
🔹
کسانی که خود را منتسب معرفی می‌کنند، اما حاصل حضورشان چیزی جز آلودن فضای عمومی به تعفن تفرقه نیست.
🔹
تریبون‌هایی که باید مأمن عقلانیت و همدلی باشند، به دست آنان به کارخانه تولید نفرت، بدبینی و شکاف تبدیل شده است.
🔹
آنان با افتخار از رفاقت‌های دیرینه سخن می‌گویند، اما در عمل، هر جمله و هر رفتارشان خلاف منش رفیق است و خنجری است بر پیکر وحدت ملی.
🔹
آنهایی که فتوا می‌دهند و دعوت به لشگر کشی می‌کنند گویی تمام همّ و غمشان آن است که مردم را در برابر یکدیگر قرار دهند و از دل التهاب و اختلاف، برای خود اعتباری دست‌وپا کنند.
🔹
اگر این افراد احمق نباشند، قطعا یا جاسوسند و یا خائن که در هر سه صورت باید نهادهای امنیتی و قضایی کشور به مقابله با آنان بپردازند.
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679215" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679214">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5c7b282f.mp4?token=IKVKDSWtz3TgjRfBvy92TfkSekpozCNN_TzQmF4U9lTrOEjQonaEwS17YTYYyJibAwHvA2Ab4iOxslbQdmLZ9865pG0SYfQQ8-DqLR7ipPDgTbPmm5lpHdg2AOIKk6cwlCxdF7sMSSKRvnKuNZjzornY1BZq_Il-7bzIIG7QftqQqCnkNRvOYZ1zDHxWJIMNad0J2B1gIX1fXa4FRwFNDr-i2e3WymefB2eGbgBlA5MeNUTIWGkVes6dmHChWiMLQdlMjf9oZDNJi72gUJpnSHe2_miC8JcQizgEqEQ7syeXW1WLjDDJbOPhVhQUQkT1dxHmNNoeQtm3ZB5HGlXUZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5c7b282f.mp4?token=IKVKDSWtz3TgjRfBvy92TfkSekpozCNN_TzQmF4U9lTrOEjQonaEwS17YTYYyJibAwHvA2Ab4iOxslbQdmLZ9865pG0SYfQQ8-DqLR7ipPDgTbPmm5lpHdg2AOIKk6cwlCxdF7sMSSKRvnKuNZjzornY1BZq_Il-7bzIIG7QftqQqCnkNRvOYZ1zDHxWJIMNad0J2B1gIX1fXa4FRwFNDr-i2e3WymefB2eGbgBlA5MeNUTIWGkVes6dmHChWiMLQdlMjf9oZDNJi72gUJpnSHe2_miC8JcQizgEqEQ7syeXW1WLjDDJbOPhVhQUQkT1dxHmNNoeQtm3ZB5HGlXUZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دستور انتشار اسناد موجودات فضایی را صادر کرد
🔹
در پی اظهارات جنجالی اخیر باراک اوباما درباره وجود موجودات فضایی، دونالد ترامپ به نهادهای فدرال دستور داده روند شناسایی و انتشار اسناد دولتی مرتبط با یوفوها و حیات فرازمینی را آغاز کنند.
🔹
ترامپ در این…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/679214" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679213">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb3d1485e.mp4?token=teu-kxp9CJNkzwJrSpgdIaxH6KYS4yptzB8dhsVAGMnj9GY6kAKKojnbAfFhPZGo6w5lsZWU4w1y_IKq91XJvQmE8a4Zn0MJK4VLfISkO9YSUG85Ic0ctdCrY-bZZMytmjU4xvA8LLyma3V3tkc-U20RCU39YJ2XXX1_m5fNbFoYj1o2qEgGQLTln43gn3WvQpNGkk1B4SDTClhDegVuZJs8TZ_HLIm3klQObI21WYRxxKOrGzyfDuZllTN7iFvN-mDIyxtABH3Cij8CC1KcozWP5fjmu9rej-n_xULitGWQb70QEuM-SOpaiMJmJBLShxm9BZ-ln-7n8YiSONmu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb3d1485e.mp4?token=teu-kxp9CJNkzwJrSpgdIaxH6KYS4yptzB8dhsVAGMnj9GY6kAKKojnbAfFhPZGo6w5lsZWU4w1y_IKq91XJvQmE8a4Zn0MJK4VLfISkO9YSUG85Ic0ctdCrY-bZZMytmjU4xvA8LLyma3V3tkc-U20RCU39YJ2XXX1_m5fNbFoYj1o2qEgGQLTln43gn3WvQpNGkk1B4SDTClhDegVuZJs8TZ_HLIm3klQObI21WYRxxKOrGzyfDuZllTN7iFvN-mDIyxtABH3Cij8CC1KcozWP5fjmu9rej-n_xULitGWQb70QEuM-SOpaiMJmJBLShxm9BZ-ln-7n8YiSONmu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قنات نبادان؛ منبع حیات سرو کهنسال ابرکوه
🔹
قنات نبادان در شهرستان ابرکوه یزد، منبع اصلی تأمین آب سرو کهنسال ابرکوه است.
#ایران_زیبا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679213" target="_blank">📅 18:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679212">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daff06e5cf.mp4?token=FnZQpc01PNGt1msfptBFeJRdmiCZcKiNFj-nxRuby0C4z-3V5IV6_-tSn7iPlCEa1bM9i8-PJjdppMwyk06ZgffKd0NDx7DH6XTklXDEz4psWKy1ryT7JK4KLBdZwEVkwB3xvFzXoFRYuFi9wlP24c2PIIUxmFPoBgo6XueSXILYyVuOldka1Y2gpRXNoIheu9M94Mpm6s39HSKJQvvsViBAbb-KcyBLUFgJCai5W3885Ej3jcnirNCjWOyWpM4JOUZESjhRf-kKsMHY3rgvt-i1_vYnHlPVOy9tt2AgeW9MELPvKJ9pHqkLM5Hu1ZwuaXe2XIAJ31iRPczcpnOFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daff06e5cf.mp4?token=FnZQpc01PNGt1msfptBFeJRdmiCZcKiNFj-nxRuby0C4z-3V5IV6_-tSn7iPlCEa1bM9i8-PJjdppMwyk06ZgffKd0NDx7DH6XTklXDEz4psWKy1ryT7JK4KLBdZwEVkwB3xvFzXoFRYuFi9wlP24c2PIIUxmFPoBgo6XueSXILYyVuOldka1Y2gpRXNoIheu9M94Mpm6s39HSKJQvvsViBAbb-KcyBLUFgJCai5W3885Ej3jcnirNCjWOyWpM4JOUZESjhRf-kKsMHY3rgvt-i1_vYnHlPVOy9tt2AgeW9MELPvKJ9pHqkLM5Hu1ZwuaXe2XIAJ31iRPczcpnOFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚿
✨
سردوش ماساژور و تقویت‌کننده فشار آب
رفع افت فشار
💧
⬆️
+ پخش متوازن آب با چند حالت
🔄
بدون نیاز به برق/باتری
🔋
❌
🧼
دارای فیلتر تصفیه + کارتریج جذب رسوبات
🎚
کلید تغییر حالت سریع + اهرم تنظیم آب
💆‍♂️
ماساژور مکانیکی و بازوهای ژله‌ای
🔧
قابل نصب روی دوش/شیر/وان
🚿
🚰
🛁
🧱
بدنه ABS |
📏
۲۵×۶×۳.۸
🔴
قیمت 1,098,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/58323/180124/</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/679212" target="_blank">📅 18:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679211">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
آمریکا ۴۳ روز تا مرگ نفتی فاصله دارد
🔹
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیره راهبردی نفت این کشور به کمترین میزان از سال ۱۹۸۳ رسیده و اکنون تنها معادل ۴۳ روز مصرف نفت خام آمریکا است؛ در صورت نرسیدن نفت جدید، این کشور با کمبود مواجه خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/679211" target="_blank">📅 18:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679210">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: با ناقضان وحدت مبارزه کنید
🔹
حضرت امیر یک بیان نورانی دارد که بالاخره ما جامعه را متحد کردیم، و تمام کوشش دشمن این است که این جامعه را ارباً اربا بکند. شما مواظب باشید این جامعه متحد، مختلف نشود، پراکنده نشود.
🔹
اگر کسی خدای ناکرده عالماً…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/679210" target="_blank">📅 18:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679209">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار، سوئیس را تهدید کرد
🔹
ترامپ تهدید کرد با محدودکردن واردات کالاهای سوئیسی، می‌تواند اقتصاد این کشور را با مشکل جدی مواجه کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/679209" target="_blank">📅 18:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679208">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ته دیگ
🔹
رسانه‌های غربی خبر دادند که وزارت جنگ آمریکا پس از تماس تلفنی خشمگین دونالد ترامپ با پیت هگست، قرار است یک جلسه اضطراری مختص به کمبود تسلیحات برگزار کند. سی ان ان هم بنا به گفته دو منبع آگاه اعلام کرد که ارتش آمریکا در جریان جنگ با ایران بخش قابل‌توجهی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/679208" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679207">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای معاون وزارت خارجه عربستان: توافق دفاعی با ترکیه و پاکستان تهدیدی برای منطقه نیست
🔹
توافق دفاعی مشترک با ترکیه و پاکستان محور نظامی یا مذهبی تشکیل نمی‌دهد، ارتباطی با رقابت هسته‌ای و تسلیحاتی ندارد و تهدیدی برای کشورهای منطقه یا روابط ریاض با آنها…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/679207" target="_blank">📅 17:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679206">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679206" target="_blank">📅 17:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679205">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عضو کمیسیون صنایع و معادن مجلس: در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس می‌شود/ فروشنده نفت وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند
🔹
علی‌اکبر رنجبرزاده، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از ابهامات موجود درباره بازگشت پول حاصل از فروش نفت توسط تراستی‌ها می‌گوید اگر در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس شود، استیضاح وزیر نیز در دستور کار نمایندگان قرار خواهد گرفت.
🔹
علی‌اکبر رنجبرزاده در ارزیابی عملکرد وزیر نفت درباره فروش نفت و بازگشت منابع حاصل از آن گفت: «موضوع فروش نفت و بازگشت منابع حاصل از فروش آن به داخل کشور، همچنین مسئله خالی‌فروشی که گاهی از قبل انجام شده بود و عدم بازگشت پول تراستی‌ها به داخل، از جمله موضوعاتی است که مورد توجه نمایندگان مجلس قرار گرفته است. وزیر نفت خودشان را مبرا می‌دانستند و تقصیری را متوجه خود و مجموعه‌شان نمی‌دانستند؛ در حالی که فروشنده نفت آقای وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند تا زمانی که منابع به خزانه بازگردد.»
🔹
رنجبرزاده در پاسخ به سؤال رویداد۲۴ درباره احتمال استیضاح وزیر نفت گفت: «هر زمان احساس کنیم در دستگاهی رهاشدگی وجود دارد و پاسخگویی به حداقل یا حتی به صفر رسیده است، استیضاح جزو وظایف نمایندگان است و انجام خواهد شد.»/ رویداد ۲۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679205" target="_blank">📅 17:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679204">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق، شامل آتش‌بس ۳۰ تا ۶۰ روزه، خواهیم بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679204" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679203">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده مساحت مثلث
🔹
توضیح محاسبه مساحت مثلث با کمک مساحت مستطیل؛ روشی ساده برای درک بهتر این مفهوم توسط دانش‌آموزان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/679203" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/679200" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqpX-4W26-D3Xwyxjdaar-MSjo-8bcyb-MxFXjlKb1Woq74O1BANE51FL4iztaFKXIVQ-Rwh9yUhfQKFgPZaSFQHTzEKR1l91C9ntY6NC4gjfPGo9N9p-BlcjzvnKzawY0s1yyf583mhmsJxEwc_oBnbdTTMrq75k6D7349duyPLWC8P3M8nOIWs_aBg1zdmex4wajYY752K6509nC0iV1d9F2aEWV0ZZGwDcQ_xv2srmXPKKwqRLyS1t5keiW5nqMg9SMZGTHeI9ojPA620Y-eJedxJ0Ny5wCRnqanCz0Ekbz3x-Ud-WrR7rdYNdr_wRm-QG995kx4sFM1iLJhxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وسیله‌ای که بعد از خریدش میگی «کاش زودتر گرفته بودم!»
🥒
🔪
خردکن دستی چندمنظوره
✨
سریع، تمیز و بدون دردسر
✅
اسلایس، خلال، نگینی و نواری
✅
بدون نیاز به برق
💵
پرداخت درب منزل
🛑
موجودی محدود
🚀
عجله کن! لینک خرید اینجاست
👇
https://khabarfouritel.affdn.com/lead/48457
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
https://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/679199" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679198">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تخم‌مرغ؛ بهترین پروتئین برای ورزشکاران
🔹
تخم‌مرغ به‌عنوان یکی از کم‌هزینه‌ترین منابع پروتئین معرفی شده و مصرف آب‌پز آن توصیه شده است؛ بر اساس این توصیه، افراد سالم می‌توانند روزانه ۱ تا ۲ عدد و حدود ۴ روز در هفته مصرف کنند.
🔹
افراد دارای بیماری‌های قلبی‌عروقی و کلیوی نیز سه روز غیرمتوالی در هفته مصرف داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/679198" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679194">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMsCLW7uCT0b2m85l_b4yGg49lLAEAqSQT-GG_FeByIkqt6DA7vXWdZs-D4guyUACJVGIij9mVJxtoJACpsc-L9QeAkqYgwMznc-BmAJI8M6kAqleXrqbxAie9b6UJAwl3jZJ5D7TfqFUvBFJWRc-GutnAbkL6_hPswr0miHVSUYIvUIZW6PdMjYoGl2KwNlmp4Ur1pqhRZjdRFhIk-z_4uegKUU4qDrCtbR2gi4mRHGBxmgh8eo7ExWsv6O-QpAWsMZ53rAmSrQrELVfZdCWS50m019LGdiblU3NJ9euitbWNdb2wpn_R21WXByY7276NhTHqeSlAJGzyvKn0vlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wma4bTDlhpSyypM2bYBwPse-gzt7Yzdrole1Q_cgIFkmHiSxnrhslBb8UPJLpEXl3LF3pZUXExNA5v1pgq3nB9qPWsOHuO3kxYoWI-MQiZFDuDtrGFZbK_l2xie3aTIQ-N5xZWWDEArZXfocSmydYRsuAocOkj329Faiq_Ex9UtwzPE7kHQ1yIaRiH48IXZIpgrZ5YDqNZXTU1u-xU01Qnd5ZuDKVNDEgxKlGdnjd_sF1aA2qpXjt-YfxFT3E2QjHSfCjh6s7lYqyDxvF9ZfOg6nl2Yfa3svNaBCjjmQgI6qho6Q0myTohjSyPUPZcS8qZFhkC6-PUjAS4Wj5Wpdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvBrZQQ1KZcB951H8AtVJPKQnLlLKty_3JGjRrIS3gNeTaXc8vXLjklz-zg3VSGH2dOX90uWiAt-UYI5uuw6J6SXboOEaS_4tZVFe2jsa1TO-uWsyz56b27s3z1yIAhL2htJPfTB3EPn6WJDN98iZQYEW0jczdPPHdnVFo_-laHJUSUvkoJOd6fBfdoPaQ8amTKKUDuKO0_LP2-doE4zzcge1F_U90osnVUXk0H_IcLqmRGY_XJguldcoL3L2wIgb0oyUMys8jb9eCvjYg6Ep7J4e9QbmjOENZPX6fn7hZR458bJ1wQIoFjWPiYzI3FAhHU3ayXNjj_f0bQIG57KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFQQ2qymBq8yeq3A-57_MxT6hMCW3WAevk_SKrfBbZpQrNfOBeQiC3d21FZczYlGi7OAArQGHHdv_4w0RcutorzNda636X4yyQpYh_GMOKKmkA5jVXdNp0qx74Fu8eJO4jgIBCSFK2YAnPUq2g1rCZM39BzKDJkPVYXTBsF3Gui-YuJgGUtXyDEk9kCypdb0mNuX9b3nVvk_JNxgG6-JD_V5s3bJMXRfqSnNXLzqHTnswNA1aIe1-g3Jw3vO9S2EbWQiFjumCdoP-vr1T2k_jDE1V_abJ__c5tDgkB5EUCzZ2CZ-jBluX4s8o1dPaMPUj6Sn2d8NE-WrOHCLgXF98w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/679194" target="_blank">📅 16:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/679193" target="_blank">📅 16:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4478015bf5.mp4?token=djcS8gCiJei8wl8uAWG5ZiyToGgPB4OtbHDM4kqw7rgTrVyFsf3wc_5R8EtvxHDrxDMpOv_Ti_QM3HgVEnDluxxs0qc-MkHQiHcmzK2Po4DFPEsF1VwFU-e60KMOm9_lGr9ssxjqxvi8a-HA3yXv1KLNx7-tLvgSHhgTTqmQ6ZCHVkSwXaWJNY4kiQ-FXZBapEZAOuH9RqdTFXuxCsSjsO4kSqkZzBf3Qa51eLMNwrBhYG7iqlhwY5sec1pzVN3RFYCZSx8uSHk2Uaq_ZqoHSnReZbxrT4BogbkF4-BbajCK8jXhS2ql4tqXgDY4vJ5H4ntvqSt_D1MDWkKqtWifRQoF35rbfJT9feLgNqthstZ-niGYT6C2qjefjWVy9B9uq9Z9hspGB0es__ij_I1LGNYO89nkO-zsKEwzeOIi9lgsxqGRsRDXa7D1GXSsetvM7MvQ_z4c58JOYVhPzDEvLD4zdK8-8ob4txRl-2hZt3PsChAFQxvHhpy2QzZh-VPVQ-hRkvQHC3T40bAZ-RJwkeZEfv1NPn0xhgQmLIRR2Ulu1fkxE0vmH4TuttrtEf80rVRmXnp8FGtUfz5xRm1y06mq_m3SadM2ell4Inf37_QilYhE02KpKY2S90_yMomDzEP1zYPKhaPITjxTSytkLDBHZuftvENV1QBMd-czDf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4478015bf5.mp4?token=djcS8gCiJei8wl8uAWG5ZiyToGgPB4OtbHDM4kqw7rgTrVyFsf3wc_5R8EtvxHDrxDMpOv_Ti_QM3HgVEnDluxxs0qc-MkHQiHcmzK2Po4DFPEsF1VwFU-e60KMOm9_lGr9ssxjqxvi8a-HA3yXv1KLNx7-tLvgSHhgTTqmQ6ZCHVkSwXaWJNY4kiQ-FXZBapEZAOuH9RqdTFXuxCsSjsO4kSqkZzBf3Qa51eLMNwrBhYG7iqlhwY5sec1pzVN3RFYCZSx8uSHk2Uaq_ZqoHSnReZbxrT4BogbkF4-BbajCK8jXhS2ql4tqXgDY4vJ5H4ntvqSt_D1MDWkKqtWifRQoF35rbfJT9feLgNqthstZ-niGYT6C2qjefjWVy9B9uq9Z9hspGB0es__ij_I1LGNYO89nkO-zsKEwzeOIi9lgsxqGRsRDXa7D1GXSsetvM7MvQ_z4c58JOYVhPzDEvLD4zdK8-8ob4txRl-2hZt3PsChAFQxvHhpy2QzZh-VPVQ-hRkvQHC3T40bAZ-RJwkeZEfv1NPn0xhgQmLIRR2Ulu1fkxE0vmH4TuttrtEf80rVRmXnp8FGtUfz5xRm1y06mq_m3SadM2ell4Inf37_QilYhE02KpKY2S90_yMomDzEP1zYPKhaPITjxTSytkLDBHZuftvENV1QBMd-czDf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیر شدن گردشگر اسپانیایی با نظامی صهیونیست با شعار قاتلان کودکان غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/679192" target="_blank">📅 16:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679191">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/679191" target="_blank">📅 16:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3fdfab4e.mp4?token=t5Nn3x8V2VBk1i8OhjTjaA2GsLBCgBA1JC10lloDniDo3WHAX-9G_o7WLVfs1xudPmsvzlfubSTxdCN981OGjli2AmsMoLS2hDexVUWeSMePK-EgP1H4wQ6YD83kWr53RThhq4hXi976h-ptkuqC0mbHDNcLhIyicZ7ShbBZBpiFD5-6hnTfplJMFNeI67BpQOCwxZo8gnH65_gVUFweKMqH9OGju4p5xfopGxOl_2pbth1IVmh80mg-TQ0QqmOWLN5HnUkKxwt8enZ8guZs9CnQv0waLxdjJqToaaOlCZ_wCxSrYKqTlC643M4M-UEaG8xodbMaRa-nPZ89zSOaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3fdfab4e.mp4?token=t5Nn3x8V2VBk1i8OhjTjaA2GsLBCgBA1JC10lloDniDo3WHAX-9G_o7WLVfs1xudPmsvzlfubSTxdCN981OGjli2AmsMoLS2hDexVUWeSMePK-EgP1H4wQ6YD83kWr53RThhq4hXi976h-ptkuqC0mbHDNcLhIyicZ7ShbBZBpiFD5-6hnTfplJMFNeI67BpQOCwxZo8gnH65_gVUFweKMqH9OGju4p5xfopGxOl_2pbth1IVmh80mg-TQ0QqmOWLN5HnUkKxwt8enZ8guZs9CnQv0waLxdjJqToaaOlCZ_wCxSrYKqTlC643M4M-UEaG8xodbMaRa-nPZ89zSOaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورنکردنی اما واقعی؛ تبدیل خودروی اسپرت به ربات غول‌پیکر جلوی چشمان هزاران نفر در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/679189" target="_blank">📅 15:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638a3753.mp4?token=ZkgwXHp5xgVzJFe0YVTyc5S5IbVuEwYn6sRjoQdUG1dQlS5GAM-TOa26K0J85-pR0qOV69kFChbjOHugqY0QBw6ZZDuT_cKBcY5qEId6nTvJprN2yZmxzX2BfBOjPLTZkzuHa7eAOdMYaNidopocN90XNgZKzHA6GjDiXoQS63mygM22jF9ux4Mqm3kmCjMadEVpV8fqL2DSW4piSDDyfHvySm_wpvix-gzIMToKnjgAScE4Addry8_I8XHTK0rxkP1cgYtITLvZWNcic1NbPy7X2YOloeRpac9IGMYMcrighDHzEPNXPAINWXAtib4DkzFc8ZjnIhJNjgsz4zRrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638a3753.mp4?token=ZkgwXHp5xgVzJFe0YVTyc5S5IbVuEwYn6sRjoQdUG1dQlS5GAM-TOa26K0J85-pR0qOV69kFChbjOHugqY0QBw6ZZDuT_cKBcY5qEId6nTvJprN2yZmxzX2BfBOjPLTZkzuHa7eAOdMYaNidopocN90XNgZKzHA6GjDiXoQS63mygM22jF9ux4Mqm3kmCjMadEVpV8fqL2DSW4piSDDyfHvySm_wpvix-gzIMToKnjgAScE4Addry8_I8XHTK0rxkP1cgYtITLvZWNcic1NbPy7X2YOloeRpac9IGMYMcrighDHzEPNXPAINWXAtib4DkzFc8ZjnIhJNjgsz4zRrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی سنگین روسیه به مراکز کنترل پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/679186" target="_blank">📅 15:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از صفر تا صد ساخت آباژور؛ آموزش ساده‌ترین و شیک‌ترین مدل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/679185" target="_blank">📅 15:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXzC6i5SvZzTugyF1wSw-vFLIbOYuXwzFx9gI3BTG_lHC-ktV_N31JaYlG4dt9RKg5PjqLnMmzNPTkeudw3fsQ9n62K8yfYfwdebpacxpQ2pqr9HSBUhCVCDFMW2GF-o2BTKN_JLnfq1KqWtz8k9GHdIw5oIKM4obAOIg_SpqTHr83NvhhkIKAe9CgXs-xUX4P1hnsD8UCDpxka-Vr3UHSmDtao8I02In9GNxRmFqgUmtGRpxElFNOoXskRt8L8Ux0qpPKM4NBCoCu_-cPPAaAc9NGd6YFYPk5PXtl6Y66rcaU-DmUoid53kdkEPsR3ZmCNl3XSjcBXlIi5j0r_zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/679184" target="_blank">📅 15:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام ترکیه‌ای: توافق با پاکستان و عربستان سعودی ماهیت دفاعی دارد
🔹
این توافق هیچ طرف خاصی را هدف قرار نداده و سایر کشورهای منطقه نیز می‌توانند از آن استفاده کنند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/679183" target="_blank">📅 15:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a02b17cd00.mp4?token=Cc8d9xy03uUUbECG0tp9gLh17Bn5INyP-oe236ElB1ShCAg7JG5f3Ht5ZSyzyrl7p42MTGUGUF4KNspiYgONDJ1aV2aVvL9gMEwl3CRR8ip3Ndf2hsSjnnwadtc_vqFIlRlDcja6VrytYIV-QyiIlitjjbb7WZSIfKANfpPbhNyAXfGnSME-Qat3ECZbs6lYU8BBESGk5Q0w0MnR0xi6a1zpyyPdvHUcs0BGcbOo7z_hCGhA8ZbYiCzcXlUxIQvNGLvYhlWDqEuhTTPRSWOjTIXIgi00IDXAuzovNvZYP4uLPWulToSeJdtPoQuHPwfOn58TSgqA5YTlFUiFrUxBJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a02b17cd00.mp4?token=Cc8d9xy03uUUbECG0tp9gLh17Bn5INyP-oe236ElB1ShCAg7JG5f3Ht5ZSyzyrl7p42MTGUGUF4KNspiYgONDJ1aV2aVvL9gMEwl3CRR8ip3Ndf2hsSjnnwadtc_vqFIlRlDcja6VrytYIV-QyiIlitjjbb7WZSIfKANfpPbhNyAXfGnSME-Qat3ECZbs6lYU8BBESGk5Q0w0MnR0xi6a1zpyyPdvHUcs0BGcbOo7z_hCGhA8ZbYiCzcXlUxIQvNGLvYhlWDqEuhTTPRSWOjTIXIgi00IDXAuzovNvZYP4uLPWulToSeJdtPoQuHPwfOn58TSgqA5YTlFUiFrUxBJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله از حمله پیش‌دستانه به نیروهای همسو با عربستان و وارد کردن تلفات سنگین خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/679181" target="_blank">📅 15:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSYKw6htpsTkJLfyDJZB6dBcZk7SguWKho4IhIHs2-PsIMDhOus_fY6sk3qIYcytk7y5OrSbrZRavFBvIvy2214_J-IhMNgudZt0j6-I9C4rDw7pa_kHhpp_aXKWe0EVhe0_3zYsTUQRFKgh0PjcOKSPOmb0xnYBxsGdUBvZT6vRuXpGAs90BRHUmEkZDHwHActKs-9CsXly3WXZ_3WPBc3JKsQfBDT7mCIVAJ4Wh0aYTe8aZ9MSqcMZpUbkVvkssCbLLjHXmzNnLKTuUmOxHvUFxE93f2QLH0c-gVFXYBCwzVwRU15GPwEXy_aR3ceDtk269xSGM0ByLHrweNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/679180" target="_blank">📅 15:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679178">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
چرا قبض آب و برق خرداد و تیر ۳ تا ۴ برابر شده؟  اطلاعات:
🔹
هزینه مصرف آب و برق مردم تا ۳۰۰ درصد افزایش یافته؛ مثلاً فیش ۳۰۰ هزارتومانی خرداد در تیر به ۸۰۰ هزار تا یک میلیون تومان رسیده است.
🔹
دولت باید ساده توضیح دهد که آیا الگوی مصرف کاهش یافته و مردم را…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/679178" target="_blank">📅 14:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679177">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وچهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای رضا معظمی گودرزی که به گفته خود بداخلاقی را نسبت به تمامی اعضای خانواده حتی کودک‌اش اعمال کرده و به خاطر شاکی بودن از زندگی، از خداوند طلب مرگ می‌کند و دچار گرفتگی قلب و جدایی روح از جسم شده و با تجربیات شنیدنی در عالم برزخ و بازگشت دوباره به زندگی دنیوی، تغییرات رفتاری محسوسی در ایشان ایجاد می شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: رضا معظمی گودرزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679177" target="_blank">📅 14:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679175" target="_blank">📅 14:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTvmH1Jp-ArTZD5sF6shLM-g_yHJKLP7GoBB9xUkbuoU-BPKVOggFa6q3xFZBgVgDZ1bxQGQSXIsm2f3vyOo6Dc_RO8ccjnM7p-T0wUKGJ-idRs3E1Mnkg_MM4qt0BcR1YWH_YnDHoEKWtd9o0WLnyJ4aAarj-uq8oCFxMRnAPJBJM8ycZty6UsSXHhF8CcrkUOqqVOX3Kkv-jtXVEsgfMH2ykN_5f6Z7tQSSPf71CgUBrj6fwlOa9Yw9Y97Z_sSRtySxBMUyCA_tWlpynwGzxmjd7I-yJfZ-cbA0OIGBZe5qvPoWowDWkfEvZ8dbETFZQv7wQBCojPQpwfbVN1uDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر تازه منتشر شده از صندلی اف۱۵ سرنگون‌شده‌ آمریکایی توسط پدافند سپاه پاسداران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/679174" target="_blank">📅 14:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پهپادها و جنگنده‌های منهدم شده آمریکایی توسط نیروی هوافضای سپاه پاسداران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/679173" target="_blank">📅 14:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHHmCUrmTZmR3cvk-oJhLjYLQrXt6wn9a1wSS0IMXr04GdPiv9ErF-XXx6vh_7v0_I8POqXuUm6Isw8al2v9_-UXRnvSmk7d0VfJx_5Mqg-vGS0kfhqozmpccn1vIIhGSn8vBBmwGldtlpIhLrs4-_0ppudqs35X3BLeWr2lgSkBwgFasWjFN5ZvWnTtNqyROt5bi_4k8zl9fHyahMWRbQPB6YBgXZzMKdv3e9v24MR-Qq0Q46Id-P5PR-lTeNJlOKcp1aTjyzr5_uQFN2Ne4UfM1-cLSmV5r-UJefwS_jUItuunE89hXNCchEfYW8Of0TFwNOSpf9myZ_M3rx4SPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای العربیه: عربستان سعودی، ترکیه و پاکستان «توافق‌نامه دفاع مشترک مکه» را امضا کردند  توافق‌نامه دفاع مشترک مکه:
🔹
هر گونه حملهٔ مسلحانه به هر یک از کشورها، حمله به هر سه کشور محسوب می‌شود.
🔹
هدف این توافقنامه، تقویت بازدارندگی جمعی در برابر هر گونه اقدام…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/679171" target="_blank">📅 14:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HK3yydbxkbqUPtzWxWAzY4hM2On5mLe3-WbrSuA7b_ai8SLFk6LLJxxrXqnL2KoIm9DqC2P2p6O0wzp0p80h2N3Ft2NKtR278NrkDbh_hHRUDSu1nHJS7YY3bykuBjGPE1iqs7SBSj7hBtrwGp2oitX67Ma_rIYG8fAIOIOTczpZNXJrrjZxpCHSsIOEU_HUvxb5q94A9AtyhSkykIPMfPcVMAFIjalXzCQ_xcztpSrYgpU87FXDqM1RZpwMv-SzjcbFr93haI3nVe5xy_uyAPOIDqqKgNKk8oR5o4zrYCIsl5iEoB2hrUArKWSbbAWLh5VceiJCl3hVGkJF6Cz1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKgPI5kuVy9yMSK0QLzbzZ_60yCVtW5qHxX2A6XoZj55XP9CLK_nNqgdDjYBOqeqfIod6mNBel4P40uFzy7Vi67gmOTqsCsVGangUU0Ng_v2VqdWoTX_IHXPzlLmq2xSvcTx0hb2QTfP1JJJZ0wPeD3uYu75y_1DebvwGuokDA7eWIrmUPmlI0tnAXxk6UuXxUcTU3H_WsLbI_3XT1TJbr80ZHslTWYSL1eQpo5Y14qnnAfnWhLlSzw0UApp8zidV0wbWK0NvMInkECsfTjWscXkgDn6-O6B7m8wq0U8vD8gpUr6hTIUU-s1o4UXSWch0_duydQoV4bqSc_XqLYTiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کوچک‌ترین گربه وحشی دنیا را بشناسید / کُدکُد؛ شکارچی مینیاتوری که نمی‌شناختید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/679169" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYBJixopkVGzJwA_T-eCFUhXnlfhbY7BB3ZaRw4mQKkbuGK0PayUB3QIszlX6C50cvtFjQ8Xj1NaCNQNpKQIpVteAYdmEk2PpIglJTbwdJxps89xbsMSs3pHsq2RuHpIP_RNmVS6turqeAjrSq9Hc7YFzMJtD7IokzzDWuO41Y89IkVcKIuDc7FppVTe-eOkaMqAEuaP32Ch82euK1sd29foCeTR7_GT7ghKc_LOgx0S4jOWi3HkdjGlqq3buL7jYXDO2A3Qk310he9yX8hAqQq1Q4JfwQGZ93iPVlojt4PcRN_Mgp0A8VPzuS9irHCG7Istzg8vJx9P-4TBqjMjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام برنامه‌های هیئت قرار در دهه آخر ماه صفر
علی جلالیان، مسئول هیئت قرار:
🔹
هیئت قرار که به همت کارکنان خبرفوری ایجاد شده است، همزمان با دهه پایانی ماه صفر برنامه‌های متعددی را برای خدمت‌رسانی به زائران حضرت علی بن موسی‌الرضا(ع) تدارک دیده است.
🔹
این برنامه‌ها شامل برپایی موکب پذیرایی از زائران پیاده در محل تپه سلام مسیر ورودی به شهر مقدس مشهد، پخت ۲۲۰۰ پرس غذا در روز شهادت امام حسن مجتبی(ع) و رحلت پیامبر اکرم(ص)، آماده‌سازی ۸ هزار ساندویچ برای توزیع میان زائران و همچنین برپایی موکب اسکان زائران در نزدیکی حرم مطهر رضوی با ارائه رایگان ۳وعده غذایی(صبحانه،ناهار، شام) است.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/679168" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCbNJ7sL6RmBtzDYORS90w2iLq92W1PFXwSW8bEdAe-Rhm5bcm0UMkNlCywWveRp9OyQJ_W7QwRZSCSg0-RrXbaXe_O50TBz8nPp44425FfU4Pi0bwGIaNd-bA2LxZupeOFp39A1th0VvUoPggI1ZEkwoq1OZ8OLz7Jb3Nt8-hfZOL65OQE1CmJD-MoxywRdqL1ISi7VOur_KWoxasHVhMngm1ehKXWISen9lOWu_GorKOoQze6VnK_HVCrmuUUrlrdZpJ5z_5SymWYGuzdC7PaNU65YMS2iiApxuFXQbnG98YfKi4qAjQ06HAVrPT7d0VElBD0NSOPl7KF16-cArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/679167" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150a2c1bf8.mp4?token=FpeOiJvV9Wc0cNit9xtM7HWCoWsppOPo0uT3sE-0jI3vv3WGRObq6_LbQGbkoJPcFfpN20-4djeh5_AfJwjoqJCj_c365HFU6Hac4xFFVjqlbMD25iOkH3Za_ydEx4y2Z5DI8oxiAkLcgAskr5GgLu8xtfgYZM0eevx1xa8LYjOMf1MaCS1J03mqr74J-BxFIpSQPpDVA2I9AXfpaH9W8vSTA6PZV_-Qzkf-gli4-qEyaFr4iPCRgL_jW5095K1gQIETYQPnjvHtAmyElknSiKd7pOeu7pHB2N6CqFRsP02pQs4alo9p6XSYZcSQgWcXnApJiBBto-fuayRujGI0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150a2c1bf8.mp4?token=FpeOiJvV9Wc0cNit9xtM7HWCoWsppOPo0uT3sE-0jI3vv3WGRObq6_LbQGbkoJPcFfpN20-4djeh5_AfJwjoqJCj_c365HFU6Hac4xFFVjqlbMD25iOkH3Za_ydEx4y2Z5DI8oxiAkLcgAskr5GgLu8xtfgYZM0eevx1xa8LYjOMf1MaCS1J03mqr74J-BxFIpSQPpDVA2I9AXfpaH9W8vSTA6PZV_-Qzkf-gli4-qEyaFr4iPCRgL_jW5095K1gQIETYQPnjvHtAmyElknSiKd7pOeu7pHB2N6CqFRsP02pQs4alo9p6XSYZcSQgWcXnApJiBBto-fuayRujGI0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: چهارچوب کلی تفاهم با عمان مشخص شده و به زودی متن نهایی و جزئیات هم بیان می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/679166" target="_blank">📅 14:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_OkTvNIi_4JzAZs0OMkIYd78vpWo_RtVRNWWXb5RQg4BrnVVz4LRhmLNfAFbVIRyJREzouOgGFplQd5ZdcEp1mJNOKlFekfjDX5sFZUXvw9IuhdKscM5SctGH9TguUTuuekRsO1nb9y1jMpatinQlWUixG7m_2edRfQp7QZ7BW-SQSCuLwTbSDdzaAHwif88H1TeJt0qMMoFgYO8ozkB4x90jkF2BirmY6RrqpWQXJ8YjmjLtR4Blpc2TdhOxfjK1Ghh1Q2uVZKpHDrcqKoCOBMXmOg9sUuijtCW-2rLrFOTzpJYLYeS0RvfPJICj3yReaPKdIoYpNt7AUVCjzomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خرید قسطی طلا تا ۱ میلیارد تومن از ملّی‌گلد
فوری، بدون نیاز به چک، ضامن و اعتبارسنجی
با سرویس خرید قسطی ملّی‌گلد،
می‌تونی طلای مورد نظرت رو همین امروز با نرخ لحظه‌ای بخری و هزینه‌ش رو در بازه‌های ۱۲ یا ۱۸ ماهه پرداخت کنی.
✅
بدون چک و ضامن
✅
بدون اعتبارسنجی
👇
برای مشاهده شرایط و شروع خرید قسطی، روی لینک کلیک کن
🔗
شروع خرید قسطی طلا
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/679165" target="_blank">📅 14:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyH-Gc6yoVCJqGJhXlgFeVOsTMWK8l1x-Rt-etSurXi0xIR3Kwiu5wvvb9a6ZmpX0o8_p8lwBKM9LOHQNNyOkFQWnbIGJ1MRDomSt-A4PC7SzpMaeOSftwn5tMzuyYQN8YUZRbyQnW4Ig6mBdRt3QJVvh5VzthCnfbtjgrvSy8TOTpXwYPGPiwlJ14sTbQkYq4oXmvfC6lJRIgXJM38MTgkpvZbw7SbOrsHwwNwrTBSyw7UsgZRZUoFO5BWEufpOGNELM5wd8zG8p8lkIQnoq2n5ED0anDRQYTfX1kqEgCnPSbWNWWed73B49ejB4U1kS0i3eqxt1TTe26vw_MFtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مردی که با لباس عزرائیل به بیماران بیمارستان خیره شده بود
🔹
مرد ۲۶ ساله‌ای که در ولز با پوشیدن لباسی شبیه به عزرائیل و در دست داشتن یک تیغه بلند، به بیماران و مراجعه کنندگان به بیمارستان خیره می شد، دستگیر شد
🔹
وی در دادگاه مدعی شد که لباسم شبیه به کلاغ بوده نه عزرائیل!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/679164" target="_blank">📅 13:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اجازه نمی‌دهیم چین با رمزارز و هوش مصنوعی دنیا را فتح کند
و پیشتاز شود؛ این دو حوزه برای آینده اقتصاد و فناوری حیاتی‌اند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679161" target="_blank">📅 13:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679159">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نتایج تحقیق روی ۱۰ میلیون فرزند: ترتیب تولد بر بروز بیماری‌ها تأثیر می‌گذارد
🔹
فرزندان اول: بیشتر در معرض اوتیسم، بیش‌فعالی، آلرژی، آسم، اضطراب و مشکلات مغز و اعصاب.
🔹
فرزندان دوم: بیشتر در معرض میگرن، زونا، سنگ کیسه‌صفرا، التهاب معده و سوءمصرف مواد.
🔹
از ۴۱۸ بیماری، ۱۵۰ مورد به ترتیب تولد وابسته بود./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/679159" target="_blank">📅 13:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679158">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر ویتامین برای چه کاری مفید است؟ این ویدیو را از دست ندهید
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/679158" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
۳ روز پس از اربعین/ پایانه مسافری برکت در مرز مهران همچنان پذیرای زائران
🔹
۱۶ مرداد – ۹ صبح
🔹
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/679156" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگر آمریکایی: بیشتر عمر به من گفته بودن باید از جاهایی مثل عراق بترسم، الان در یکی از بزرگ‌ترین اجتماعات مذهبی جهان هستم و همه چیز کاملا برعکس بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/679155" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679152">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZurXuxHgQLpJm4oiyA3vBB4TTsrS_XDde1KTM-lLYyhA00FvTZEvQNGFUTtkBNglu-bqY0Rb-lY8iZL-o6eVu-h0b4NG3Gl3RuC2igydIFtcEmUwojnsNLwbFDhFiQT4_uqlYe5sRctAoI2NwhkxU6pGA-cFNeSiTCnKEZQG9qFlKzauddbfdkXsnj8YL5CiIK-sWhlGcPwJUUAoSb9TKtlKmLpWj7PuiYHIG4U7qYJwjWY_kbRSYXvBb3oAvFh8e28d6fMhhUZK_KlT4anuS2Tt_sI6I0E_nVuUwBRFBdmt4BEuZkEGHkP5e6txKa9qDF-LTetfLgYsI-pg6QnIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv-XQ5HnPJoyaKADsB-gUZTkfPtX6mquRsH-p3K6mpWtD4u7LxeEaSscLYEvVwI397uDfDr5HhYIEr4leuSgHtVfZuv_SdHSSXcIl0aYzzBVPN5alZRMACa4Qh--FECbkYFPp1v9g0JpN09FfmxSPkF8CrD1LYYvY2wePoZSNnzZIRx3PJecBsNQm4ARW9uLFNdBORODCCzATapu-Eb41STYFJf80PNYMElsscjF9VIkHRE7OAynihDNqSpUuOZN5iEqVyYraY7pNatrXQoeqc5EwfLuEpbr14KYk_AGzRau7_i_jUQ4uWPOY1mJO7a6GxTSIDMlZJDSfCjbHNA46A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679152" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679151">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfvMi121UXV80QZzwoqB3AIa8RR_IM0EkvpbQyyxx433cnImfSdbg0_go53dLkClmHQ8wbgjpvKb896rIS7sqj14ju5bVyiZVYCS6uhIzNkqACdP4N76bfOH-M2SzO9ckddyIQGVh6gIcvqbFIwA8V-nKKigPkOMP979m3egGuwXXqj9PzjRZO5qItiiuPcbgDwWw__aqt5dWbluS7y6T-JFHZ7R4-9ZtEhuc2DRGbqC7LfCfeeBW5Z5dMDNN4h0OhgOHWmEQ9QQS2m4WvQBsgeacL68301zMibeETb8WGk6E02bIx3stdJ0YevNpfowgx3Dl6lUU33g0u3u0kWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چت متنی داخل ChatGPT نامحدود و رایگان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/679151" target="_blank">📅 13:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679147">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدیویی جدید از مرد درختی، شهروند ۳۵ ساله اهل شهرستان خاش
🔹
عبدالنصیر که به بیماری نادر «اپیدرمودیسپلازی ورموسیفورم» مبتلا است، می‌گوید: «من هیچ‌وقت صحبت نمی‌کنم. ۲۰ سال خودم را به کسی نشان ندادم. دوست ندارم مردم فکر کنند قصد سوءاستفاده دارم.»
#اخبار_سیستان‌وبلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/679147" target="_blank">📅 13:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیب پیست نسکار واقعاً چقدر است؟
🔹
شیب جانبی تند پیست NASCAR رو به بالای لبه بیرونی یک پیچ است و نیروی گریز از مرکز را در سرعت‌های بالا خنثی می‌کند. این زاویه از ۹ درجه ملایم تا ۳۳ درجه شدید متغیر است تا به خودروها اجازه دهد با خیال راحت در پیچ‌ها با ۲۰۰ مایل در ساعت عبور کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/679145" target="_blank">📅 12:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/679142" target="_blank">📅 12:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679140">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلیل اینکه ساختمان‌های ژاپن در زمان زلزله فرو نمی‌ریزد، مهندسی ساخت آن‌هاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/679140" target="_blank">📅 12:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679139">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=K4Bjo9J7sh8Ufr_0gQi0vSG97zObrgfwIGnCf0DH9DUUpicCOIMafUigY9Dy35n9RADzhj_ccaOh22FhDXtEV5sV5UR0AWTrG8xuAhIx2aZzjep_I1-Dz_wnYjOBwgLyIjdmqMetsaU5ZXhu-Vxs-BeMRHKB2KCG26PEmn6qkm8Yuw2vaM3M6lBBtqEwZelbw8EmsaZgGolaJEfScG8b1G2BnM8Ho8eJ7IkCrvCuJkajBDwJYJvWeZ6D7C5NBIJNR6vzeiarX2J8h-VAUeGM-Aj8sWylmAWdcfhjNjJpa8EWkoipxOwqFAKu62KW8eEEoWMk_EKo4JbFGpLoeIxSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=K4Bjo9J7sh8Ufr_0gQi0vSG97zObrgfwIGnCf0DH9DUUpicCOIMafUigY9Dy35n9RADzhj_ccaOh22FhDXtEV5sV5UR0AWTrG8xuAhIx2aZzjep_I1-Dz_wnYjOBwgLyIjdmqMetsaU5ZXhu-Vxs-BeMRHKB2KCG26PEmn6qkm8Yuw2vaM3M6lBBtqEwZelbw8EmsaZgGolaJEfScG8b1G2BnM8Ho8eJ7IkCrvCuJkajBDwJYJvWeZ6D7C5NBIJNR6vzeiarX2J8h-VAUeGM-Aj8sWylmAWdcfhjNjJpa8EWkoipxOwqFAKu62KW8eEEoWMk_EKo4JbFGpLoeIxSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممنوعیت زیارت عتبات و اربعین برای مردم بحرین
«حسن قمبر»، روزنامه‌نگار بحرینی در اعتراض به حکومت این کشور:
🔹
فقط بحرینی‌ها در میان همه مردم ممنوع هستند که به زیارت عتبات عالیات و اربعین در عراق بروند. چرا؟ می‌گویند پادشاه به خاطر جنگ نگران آن‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/679139" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679137">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jTs4Vq-cjvUalGWlzl7RcyozrCvU7DGBq35mPARkxkYL7UwSRE9Y3zo7NxMz7fPwbkdDeRqm8ntD6n45nHI4l5akANBNho5TNGPyVaf4LYntskAuQcom-rdc-Cajawun92dCduUQdR4v47hwKNmeu6jsWNEfCar0kw2wiNJbfQ_91pvDt-9WumVYV7NVzdQhPM9scx7IZ5IudmlnfoFSK6UmMqEuuC0pwQe0n6_K4Z_3s-Z1G_h05KdafsOmcFDKTTN-P71vjT3IThNnGafWl7LnuQ5aYkadzDPEBMdHEY4x02vt1tytWURRmY0JlSbCI1e3gHWnaScr8w9TTaYeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jTs4Vq-cjvUalGWlzl7RcyozrCvU7DGBq35mPARkxkYL7UwSRE9Y3zo7NxMz7fPwbkdDeRqm8ntD6n45nHI4l5akANBNho5TNGPyVaf4LYntskAuQcom-rdc-Cajawun92dCduUQdR4v47hwKNmeu6jsWNEfCar0kw2wiNJbfQ_91pvDt-9WumVYV7NVzdQhPM9scx7IZ5IudmlnfoFSK6UmMqEuuC0pwQe0n6_K4Z_3s-Z1G_h05KdafsOmcFDKTTN-P71vjT3IThNnGafWl7LnuQ5aYkadzDPEBMdHEY4x02vt1tytWURRmY0JlSbCI1e3gHWnaScr8w9TTaYeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/679137" target="_blank">📅 12:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679134">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRl0fzp7UhDx3ySkZgBosxXY3ZAJuANkWDz6Q5Uxm0o90I2dI4OjSFPtsNgdsihbl_Sf7eZCqgVRR-BekkVsksT5QFLOn6lTuJR1BQuwS9RDHzTksZ9OSFPb4xqCbl8jbeNVC4vQR0VQi-EDwof7RDmN1lhHLAK1vawCm3Myf89ye_DeR8EfkOSXAN_sQ_dK-SnwoXWJ-GNI35u286Yh19kUuapKSP9pM4EeB4IEywTofX3T4p2W25YgQWHoofMIWaptjysM4-wIWsvoilCaGWvMUUitD0DTk7460wkhKAxb-uNSAel0-CZERa1N9WkVpDIYlczZnH4vFt6V6St6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhmIX3DBGIgIk_awXf7Ka4gWETQ90xyLSBfQGuXI1ZOEYgjQhvGYatEKl1VAZoM3Tts2Vs8j2r63zcjXQ7s4TDcy3madTIcssnoLQD0JbuwoP544hv6KnOtgGuHKj4rXkyIQW8BSXhrKOCu4TrQ8s6QBmUeXoWJwn-MD6aBPDLY7_QjWopFbLHTuq9NngU8Cj2J2SPBiq7Cw8DblSX7Tz9Axx2Ecds1FY900XFrb1HmS9BH6sLv4NNkebqJ7gdHoPWmJ7eo8ztVFNDT5WO-1jTpCXIf31p3Uj8JErRUsspiBWMgodHyt_Wq7TaKtrUZ0_AGcJQLAFs-L56MJH5Iu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxfpy3WuWAhbHfCTv0I6j4ygnoSzWwLVtuqgSHnOdpytLXsXlzL1KlZUO5ONS3-kU3LP7Q1YqwjDdY3Awf914itPVb_o3W9S74MO_80UdxEBCchz3uCI8BnyuSoCaBRc7uMTHIcEs4iZ5dmaQD-cFGu-RF1zvnZ13WAfbpD81TeztkuYw47DNoJr7SdD5Zzfjs4pFhHUo88i1Sn91_-zCqAPsqljtLi7VjFEY0YbDrQA-shd4VN36g4hpmV-LxCGonZpviP-XTcrVX4Ic4qMqWYcmHmPma6TlSmOHBYHtiq7rcBKIyX49zPULd2LcyGmJSnHsODKMxbd3vxW4ZryjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دهکده زراس در ۱۴ کیلومتری دهدز، شمال استان خوزستان
🌴
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/679134" target="_blank">📅 11:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679133">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=mqIAD7toszkd04Hrs5VrsrxajvllxfetRnzddrR1usgFNWvNQ-RsI0CEgVRVhRMUdAZ1N0VSnFk8kQcOaXpULkHvsFyCNvjWyZ5vkKIMdtXvfcqirLrQ6MLby-jn3N43dwkbabcYnYe50rM-JIoffWk-XJfGxlAs1Rfjf5v5dVNPXeymTYsFKz4JQ9HJP9HL10cKEkIF865ywzku_uZkgcx8d3Hk06QLq0NCFcYvS8jQEGBi7suSss5g3eBOTrctA2YelRwylaDgMHglMMdkfjWaswf_iG8tnxkzWWNzAchN9j0ZSFjutsEdXlFON7ThBm1z-v1pGmwwajxYZYbuJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=mqIAD7toszkd04Hrs5VrsrxajvllxfetRnzddrR1usgFNWvNQ-RsI0CEgVRVhRMUdAZ1N0VSnFk8kQcOaXpULkHvsFyCNvjWyZ5vkKIMdtXvfcqirLrQ6MLby-jn3N43dwkbabcYnYe50rM-JIoffWk-XJfGxlAs1Rfjf5v5dVNPXeymTYsFKz4JQ9HJP9HL10cKEkIF865ywzku_uZkgcx8d3Hk06QLq0NCFcYvS8jQEGBi7suSss5g3eBOTrctA2YelRwylaDgMHglMMdkfjWaswf_iG8tnxkzWWNzAchN9j0ZSFjutsEdXlFON7ThBm1z-v1pGmwwajxYZYbuJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/679133" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679131">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679131" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679130">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=nbBZYFi55eRZvXgQIeThxn4bbrgaOvJpde6871WQNjV92z21G2haeJmREJhvdGFyGq47smz-Hv01thFYGKLhCuXisTybbAaEAuzyMHyKpsdJXyfduWvISP387At1kTn_0kbHEYEgR0qjtj7kynMhPyAHMArUMxH5Xg5cpLngsPKi4zqirk4XoD3bgOF0HmoBKhsJkOK7eV14zkOxXcx1jWv5kvb74OUnTyvmkOZbta8Ho9it-h-NubTxIB3s_KnXYW3qDYpYMu3zSN4zFerUESS7cI4sZvCthv__48jso7RfngZQTwR0Z1U68dKGFOd1JJGPJ5gIjuV14dOIgDdnQzVeQd8GdNY3v156hGiHDBnhWN8ZOFt77YHDouht0F3Ss4OOXzRDSAwaHQt0VzwjaaH9K0stfsoP_iESOzgULW-LaTO-n74DMyKdpdv3enxsCyh8DuyllAkzAvZFhu33a3yPt7KVEJ670GAyrybcWauQkFSKRxUpaYgA5Fx7MIJR6SafrseUL2vQ7RTW9eecQqSYzSSG1iQzDBBKEJBj6zGDV5hReSgDeKI3Bno9QgcnhS8Kg2BjBSV_xLPmd1N_N5u1Qx7Y7BbsMvfh_uMKBYXq4kcxlhO-BxlH4cS3VF4cTOMDtgsYAlABuN2gUuqCyFTEQ9RaxU-bRJzPKVBT78w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=nbBZYFi55eRZvXgQIeThxn4bbrgaOvJpde6871WQNjV92z21G2haeJmREJhvdGFyGq47smz-Hv01thFYGKLhCuXisTybbAaEAuzyMHyKpsdJXyfduWvISP387At1kTn_0kbHEYEgR0qjtj7kynMhPyAHMArUMxH5Xg5cpLngsPKi4zqirk4XoD3bgOF0HmoBKhsJkOK7eV14zkOxXcx1jWv5kvb74OUnTyvmkOZbta8Ho9it-h-NubTxIB3s_KnXYW3qDYpYMu3zSN4zFerUESS7cI4sZvCthv__48jso7RfngZQTwR0Z1U68dKGFOd1JJGPJ5gIjuV14dOIgDdnQzVeQd8GdNY3v156hGiHDBnhWN8ZOFt77YHDouht0F3Ss4OOXzRDSAwaHQt0VzwjaaH9K0stfsoP_iESOzgULW-LaTO-n74DMyKdpdv3enxsCyh8DuyllAkzAvZFhu33a3yPt7KVEJ670GAyrybcWauQkFSKRxUpaYgA5Fx7MIJR6SafrseUL2vQ7RTW9eecQqSYzSSG1iQzDBBKEJBj6zGDV5hReSgDeKI3Bno9QgcnhS8Kg2BjBSV_xLPmd1N_N5u1Qx7Y7BbsMvfh_uMKBYXq4kcxlhO-BxlH4cS3VF4cTOMDtgsYAlABuN2gUuqCyFTEQ9RaxU-bRJzPKVBT78w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار کوثری: آقا مجتبی و مصطفی خامنه‌ای در جبهه حضور داشتند
🔹
رهبر شهید پیام دادند که اگر بچه‌ها شهید شدند اشکالی ندارد؛ مراقب باشید که اسیر نشوند؛ چون من امتیاز نخواهم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679130" target="_blank">📅 11:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: تنگه هرمز به نماد یک تحقیر تاریخی و ماندگار برای آمریکا تبدیل شد
جاش گلنسی، روزنامه‌نگار و نویسنده انگلیسی:
🔹
تنگه هرمز به نماد یک تحقیر تاریخی برای آمریکا تبدیل شد. تحقیرى که ممکن است برای یک نسل در حافظه‌ها بماند؛ اگر نتیجه به‌کارگیری تمام توان زرادخانه و قدرت هوایی آمریکا علیه ایران این باشد که اکنون جهان برای عبور از تنگه هرمز مجبور به پرداخت عوارض شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/679128" target="_blank">📅 11:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679127">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکشی ضارب ۱۴ سالۀ مدرسۀ تایلند
🔹
دانش‌آموز مدرسه حومه بانکوک، عامل تیراندازی بوده که جان حداقل هشت نفر (سه معلم و سه دانش‌آموز) را گرفت.
🔹
او پیش از یورش به مدرسه، پدربزرگ و مادربزرگ خود را کشته بود و در نهایت، در مدرسه خودکشی کرد.
🔹
مظنون دانش‌‌آموز کلاس نهم (حدود ۱۴ ساله)، ۲۶ گلوله شلیک کرده و ۳۴ گلوله دیگر در محل تیراندازی پیدا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/679127" target="_blank">📅 11:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX2nBnNNOuxZoptok_3JtB3XDuudYvoP1I7QrrPw232c8TogkmB0i7o8jczGEYgu471a42D4P64kmOHZ2DVieGRIcxDvFtMi5XZ7KtdrRSZt-Nk2-i0ueuVugxeHdOzAEMDz-BfBznKTqO13LVELnhtQxQs5VFt1wa_SagLi0VQ5lHCD1zrGf0TPdBwJL8-ugItiiyD9waDHb1FpR9yK7cHpI7Ne1MtsaAYe-3cIcUvCYLjew9S7uvR3Figs40cpaETA3S_5v-xJMiP_5Oe9FuA8X4HFtp2C-yjjlO2V5icbuY4qr7gLprk2lnLLo-A7rNuUQNVqUFA-T7jEzahbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4vueUm6HjOY5ZPWL2r5zD_6skVmjOdTXhL-TQ42tbDSFmdxVt9pcsz6Y2kE7foT_s1BYyXbBwQTl41fFZf6a-DwPMECYozf-tDP2c_PfnoChej0QIZkfNEV19CEmY9ONnPTQp09pvcYrec2PnfndoK3GvF9n38AnFjpJ1kUUIQSg0KcnyUm7XuFkjbhbJSYWTHKyVJOK_lOJgpZ3a65DJ8W1pLRUPcWXFzs7c2xsbRvMDbeD686gK1boWpcYV2LyLZFiVzQoYfS-ryE9yKcCaBWY-sdXf3AP1DGFqhaJMHogvcSS4h4Bf_5dfaL4E8ioW6U-LadltzfcWU2sib5kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این گربه‌ای که می‌بینید پیرترین گربه‌ی دنیاست که جدیدا ۳۱ ساله شده
🔹
غذای این گربه فقط آب معدنی با ماهی سالمون، میگو، مرغ و تن‌ماهی هست! اکثر گربه‌ها متوسط طول عمرشون بین۳ تا ۱۲ ساله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/679123" target="_blank">📅 11:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/679122" target="_blank">📅 11:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679120">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده‌ گوشی‌های هوشمند
🔹
این گوشی رول‌شونده به نام MOTOROLA RIZR فرم کوچکی داره که توی جیب جا می‌شه، اما وقتی به صفحه‌نمایش بزرگ‌تر نیاز دارین باز می‌شه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/679120" target="_blank">📅 10:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679119">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد؛ دومین شهر تاریخی جهان
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/679119" target="_blank">📅 10:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBnfxrwUHa2GmT6HiBHQVGrXWV0BtSOcw7Y2Er0q7JZwBC4-tLVUeOyRHmj3iCA4v1IDRoC4nskBSFlENLiVhjrqcbREnEwioSC-4ZksChYgdnngcHKpa-1u0CIqSF9xHKFKNe6QsJG7HvW3rS13unYaAcN3RnUtEfinX2E-qRnmSyshBMeNYLGe4g0GbVqxZy9ZR1_PBetXTMNs0g8585i_mDwvbanjcjTDuV-gs0dPI5_O7BjwtvTQjF2ZnQkM7nJhMfjBzyfnucrmIFw8upx5VcIqoYP-CV213V_f3JYt24Q_vK_XIWQi_7OFLvvKSo2ZY2NrfoHPYZxGoYt2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4rIhk2hdXtEbYVKiDTa2PTRS_P5HBuJpdf2j_g6kBHZML8AcWp7hFqVUwzvY4XEPUhtCkf5EymochEHM0lZ3hpkgkxqkSWm6h2A4gw-bTAl8vTJWRGJXRhDMpFX_FMxZNeBJyRB9nGFF3pn3ksqsK5bjL47q1XukOgq9c-ZiBvO_zmhkWbrKLkIo_Vdc8UuiKue1OFRnOoNh11RmL132lR4WkYGnYmY4TmGnVb6J2coaIBYix-deJCA3gROSAgcvo--7Xnki5yrCJk5fDErG8D1r44YofVQo6QkSjh-Xe4Do67B_HvuBBF4-MPiFi4VDoBQReZahexrBFNl5mA50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmujQg2XDTPeKjOqweJ3lKOWHhfYJAQAQw2I08LLS2WKbA3rB-XuTNXq2eJNCl7vJn6908O325kSHStRFXzWMXFg4KZhHiRMlU7eWAUGkymJvSNzthyMnJvsRGTnPetm3Jj1-m19Dg5RRGe8i7W8i38eq-z7t1RpTF5fgfQvbS2F8I2mHx6QHOrKcPU8To-FgpnRUpEVYiq4_D6XWlOUyMTvNDfEy2W8HzDs2IAcb5YAvS4KC22eXHY-L0hQIN12Un8w0r6jBK4QTJuEHn2Cr2cwVqH74p-FNmBfCluczjbeMqzgub6-XzlXJV6egqfc1M-V3A9ncOhYq-ba_ujC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsJt7Mkszrksfj5ysf25KqWGCEZZgV_i0PwPE6QElWWSxdLI9r7D96q2ulw_QeRec5ZvXVGlXVdpFezzyBWJKRdSa0EjsHGLhuqLelyxD5pLFu0Yr3DtmtZaEV3XWwf5DzIACfrZdhgmBq9UTBtle9M69VRV49nmXzxYzQy2L89h7MIHw0nc2fomqw4Y5T3Jb1Xk13joWWI3n5smxE-zydhyqxC36tXK_JQGCZBepMT27ftqfjZutsKjVyZ0wumNGuw6enfRbFjSuI3lhNeaxwQwOUWQv_7iZ9s369rdHuzUfdT0HhvtQ7P8Y9KWEsDDVl1lYHxuyVIlpqfr8nroew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi_mtSzPNm9XETVRbQIkGi3YPObQzveW-M8Zrv-8Lz-e_ahtq8AUqLMYP4uZF7B68dPCagJgqb3mYFaA19jxtAzOiBE2GdMCyyehq7vb1XtqW7TBVROz4kB06QLEWtr7LUQDsKAT_JBOcI8DyRmqAN4s6nL7J7YaB-OyguHAT5k_GkjUtAT6CUuS05W6fnhhNEWyXYRrKaJ2ro4IllpjmiaA9g8rrDq1I2q8UlE-gZgUDnfJ1jH927rKqsgLIEr2enR4X06tlL1H_OV4-XB0XklyCQny1p5s3TiOgMB4IQGZgVBm55giGR7rBqUDEZQm1ynNnvCcaykS6l416QT9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFtwK7FeSi69RMhAcdmkptOjMZT7VKjAt_1hLw_JCu10NmS4OoaNJJsVL6QMdb4L6AGLcMjNdFLU8D2j761jkJ7JLjl0IcO3gt3UqlrfVxNtBZt2tsYm5vz_tGQjNFQCKeXmnKNmh4MPnLKE2JoiSlimTi5X2KmJQyvMWZM_tNESHtO4660dR-io2XW6aHyQvOcFEL7tXtKecNIB3XVPiwaOgZLjpwrKC-XwE_BWgz9S1ky2GjQsd-V-AMLzrkt_sYVBV3qg24pBQANFkQC_nfg355bXBjhKzPLIrA2bBX_0QTs-HwYm7sdULtmX5ZlPXnDClqQw462Z0La8ZoWz1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترش، تند، وسوسه‌انگیز؛ آموزش تهیه انواع ترشی‌های خانگی
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/679112" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679110">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد بر اثر طلاق یا فوت همسر حکایت دارد./ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/679110" target="_blank">📅 10:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679109">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/679109" target="_blank">📅 10:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghr246KRyiqskIyhyq0OyL2JRcuovM7xrp2Hi-FEKxabWEjAgGb-JcArKiHYXLXrKnmCDyqC6q78Lvem9hvKu23HgLnJxPggdzwrg2c4qOXrqHQ_EP7TsYiANSsOPuiXC2JfJyokQmTo62mIsyqb3KePRV5TVNUDlhSa5w5Ss0DG_TdbLlCN9cbhZX8fOxXQ-jbqzr8YKSD0RHeCprGCpgCZLBRgZeNQLk7QZmZiaJvxIp5AO06Igpk_wQDqAFZISsGL_Z3Rcbzt9GO6pYnCWyHoT6ytZODNr_QEPM4VqAicfqMitZXDyQaaLFchC9WiUw9TD1F2PmGta4BrsdvvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجاد تاخیر برای جلوگیری از تماشای مسابقه شناگران پیش چشم مادران مشهدی!
🔹
مسابقات شنای کودکان شناگر مشهدی در حالیکه قرار بود امروز در استخر شهید هاشمی‌نژاد سعدآباد این شهر برگزار شود با اتفاقی عجیب روبه رو شد. این مسابقات قرار بود از ساعت ۸ صبح آغاز شود و در شرایطی که مسابقات آغاز هم شده بود، ناگهان با تصمیم یکی از مسئولین هیات شنا متوقف شد. این مسئول ناگهان با ایجاد اختلال در روند مسابقات، اعلام کرد تا وقتی مادران در سالن حضور داشته باشند مسابقات برگزار نخواهدشد!
🔹
این تصمیم عجیب در شرایطی که مادران بی صبرانه منتظر تماشای رقابت کودکانشان بودند، با واکنش خانواده‌ها مواجه شد. تاخیر در ادامه برگزاری مسابقات و لجبازی مسئول مربوطه در نهایت با ورود مسئولین ورزش استان ختم به خیر شد و با استقرار مادران در بخشی از محل برگزاری مسابقه، مسابقات ادامه یافت.
🔹
گفتنی است عموم کودکان شناگر حاضر در این مسابقه زیر ۱۰ سال سن دارند!/ورزش‌فوری
@fori_sport</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/679107" target="_blank">📅 10:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکفایی در صنعت پالایش؛ ویدئو وایرال شده از یک برج تقطیر با ظرفیت ۱۲۰ هزار بشکه در روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/679104" target="_blank">📅 10:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی سندرز، سناتور کهنه‌کار آمریکایی: ترامپ فاسد و زورگو است؛ جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/679103" target="_blank">📅 09:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نمایی
متفاوت از تشییع با شکوه پیکر مطهر رهبر شهید انقلاب اسلامی بر دستان مردم عزادار عراق در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/679101" target="_blank">📅 09:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679100">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/679100" target="_blank">📅 09:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679099">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
کشف بقایای انسانی در ارتفاعات شمیرانات
کمیته جستجو و نجات هیأت کوهنوردی استان تهران:
🔹
بقایای یک فرد مجهول‌الهویه به همراه وسایل شخصی در شکاف میان دو تخته‌سنگ در منطقه بندیخچال کشف شد.
🔹
هلال‌احمر و عوامل تشخیص هویت در محل حاضر شدند و بقایا با دستور قضایی برای تعیین هویت، علت و زمان مرگ به پزشکی قانونی منتقل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/679099" target="_blank">📅 09:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
طبق آمار وبگاه تایلندی «خوسود» در این تیراندازی حداقل ۷ نفر کشته و ۳۰ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/679097" target="_blank">📅 09:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679091">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجم تخریب پادگان مزدوران ائتلاف سعودی در حمله روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/679091" target="_blank">📅 07:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679090">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDzDhMJiRPQsQ_u3Dm3f2Fy8_rsKv0qgUp40hC000p7IFqMZ-LFvU75RWdJyiOxcC4SOi0JhX2EjjXHsXQ-lGE3nxH4WFWwKKTn1Nu8Z2r6p23kL2NmtoPbb6AJXoePCxmAM7-uK9Dz-XUaKNJfGo11Qb47jMKoabn3xu-RRL-zTkLv2yYrXWjsUzQu4He65evoa7TFuXrREAwXWP3RvgUKjAHHGSxj0yBUQENJP-uaouyG46vMeL2CyAMhY9EmGSuCwVbJwIFKODRr2ssInEBjecJ6aKtvS1B8RKNj2wW_ym_ATUhUMJubYRPV64wm-K1VMaYZTTtbwr4Iy4CL9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۶ مرداد ماه
۲۳ صفر ۱۴۴۸
۷ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/679090" target="_blank">📅 07:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679089">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD90GhWUNbic7nz36Dn8Y0yqgA_yMRrrj_oiliN1zkMoOHu9brQa2Po4dFSbDoRJ48Rt8KzwUyDk9Dy3y_lOZs27MrUXwpC3MhQga6xO0Vc5nD8XlBY8VngSwJ1M0Z17ix86uONwGPsppFZalqAD4mWv2zSNCtetqs0DyA1CyvqPcSnu5CPrTePZayrlxA8_0t-1zzhJiE2BWk1ZhCLdr81MxdFfqG3al-MpfSzW49JbZoLwrAWlDW0Y0SSqMs_L_2Ti7Iyxi53--S_u3Hs9IOcUtaUiUqh0Bn0pZH2ZQTNJaiOl4ymG2ZoeTkTfOGT58PEZHxM6Z0hoPcy1E_q6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۳۶۰
مرجع تخصصی اخبار نفت، گاز، پتروشیمی و انرژی
✅
اخبار فوری
✅
تحلیل اختصاصی
✅
استخدام صنعت نفت
✅
پروژه‌ها و مناقصات
✅
بازار جهانی انرژی
@naft360</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/679089" target="_blank">📅 07:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/akhbarefori/679086" target="_blank">📅 02:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679083">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رویترز از دو منبع منطقه‌ای گزارش داد: ترکیه، عربستان سعودی و پاکستان امروز در عربستان قرارداد دفاعی مشترک امضا می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/akhbarefori/679083" target="_blank">📅 01:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679080">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز خودش رو بر اساس چیزهایی که بیشتر بهش گفته میشود شکل می‌دهد
🔹
هر بار که به خودت می‌گی ضعیفم، شکست خوردم، فقط حرف نمی‌زنی بلکه داری به مغزت یاد می‌دی که این‌ها رو باور کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/akhbarefori/679080" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679079">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/679079" target="_blank">📅 01:24 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
