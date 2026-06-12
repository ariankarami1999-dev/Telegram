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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 229K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 14:17:28</div>
<hr>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4jIDnm40vzGUk8aN00Izam61O9raEybSocUTX6rO59SXc_x5wDDrQGJ2qx4soi84NuEJWFaJfAxgneILhkQuArTEfxQOrSVSfVrCHOqQafXePBXK61vQ-bNwwBxhbIoUy5ewWLRxIWwFUdZYTNLMwfCYsfCSdNNPHOd7Y9zVQ1QGA0T7iCPXqSkWNjmb1ueM4N3-p6KskGyo01eJjrwkv93xDsy5JV5YfsNn-iLhd7j4uGdFfAsYhuRj9VcMbeA92oKt9yFHtYHsyfqjvCrAIBFdUWS-40tmRnEoi25QshdCzmJPdsWzfAcIb03v-DLBHTgn273P6ag22SZZSaigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=iFSCQ59aV34n2iZcT1Bkg-HvlsjjHfvuTwCl7Jf22IqIo82j0iDA59e_aZEOAWc-l1cERUyQWktvYNvsnGIWGtCIKbugHW1PAkuI9yCrkPA9vs3hDI7V2I8EUtOvZwQ2MWFFaoZ60CpC9Yz1BXzCAqQx4pVXgW6fe5xdBcSTOntZ0zfnq9eD0DnYZ58IHGjbBwlSxeLCCOGo91k2zPhDgEd5DOTSjjlTdGqHMMP3hQ1vXjNq-XuYbbP06owKHYSCiW0eTS2_VdhFVD_oPQTDZ8Z4iYe_iWhkocO8MjoSvOb6v2i2uqeBEyhXSIaHnpt2qTINDxM3oXbQwSTYhKFO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=iFSCQ59aV34n2iZcT1Bkg-HvlsjjHfvuTwCl7Jf22IqIo82j0iDA59e_aZEOAWc-l1cERUyQWktvYNvsnGIWGtCIKbugHW1PAkuI9yCrkPA9vs3hDI7V2I8EUtOvZwQ2MWFFaoZ60CpC9Yz1BXzCAqQx4pVXgW6fe5xdBcSTOntZ0zfnq9eD0DnYZ58IHGjbBwlSxeLCCOGo91k2zPhDgEd5DOTSjjlTdGqHMMP3hQ1vXjNq-XuYbbP06owKHYSCiW0eTS2_VdhFVD_oPQTDZ8Z4iYe_iWhkocO8MjoSvOb6v2i2uqeBEyhXSIaHnpt2qTINDxM3oXbQwSTYhKFO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjBzULUFQQVWI6ciIWrCx3ZZA17Xzx1NmCzb65tKfh24-ymSDyRX7KiA1YtNh9J2401psaxqlvmZ6hoTQi26__vv6iCHRYUQso26tEREDUW21pAvplhZ2517x4ktar3hCW6xiIBPnEAceUenOhBoM4r1DHPIP0IgeuncFt9EBKrm4wOsLfL9sWarvjSmcs3Q6LnkdNSv2BioKkU6R5bG45yYIeS2ca7MZ0DofG2mnhcLT4xtjXTs4_XGONlWja8XMVUZQn62FdgZHq1b9B7KLuy6sAQr_-CFWhzuh-SK6uZmgikqXxqeudH4c4yBC6ne2WkzFltbLVsfpt3feL_auA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-pg1wK5YY32ILGFhDrRDPKoXZLPRz6mVFFZHR_2XkxxameXzILm-bo6zBdKl9TEj3u3KPHKfIOuNUasdM43ZQir-OEvFK0n1vtZfGEkRWwTMDwj5OuMppTWORpun9YUFKC91k25B6hYZDY1qzB2swaT0lcIklzKUunfhGRqHBsVtVULM91FwqGK-tUOyE2Fu8FBobdCW_lcRqobXCT7TOQdKJbqqFRWx6CVwNxCu52-PMao5xi4iYjgZZKAZaozAYHx6SAlET5BBumgLCyzkT--VHNtI_bEjyBnp0CKmmFfMALKYmpGEM__JP7BFEdGXqFkq5LLHZ0o25pSTlzCQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ueYb-rjSchGzMSzErhpen9ClbFUbC_VNoouwFhEQsvJBiliS3-CCyvwqOhkv9IvW66yctTzhcuLQnn7WG63X0FlDmeD8jfLKdhDZb_L-49dw2zZqMi2d1xLUGY7cNZA9ngITBKaJJObM-gelFkjy0DvkjYbnHtLwCIUxR3Cu4ZvKRTvLfpFtl8ApkEtWSfoHYj6X5oAzAVGCCGB6cm6u_kbKvUApd07940lt-Oaj8eyuojpOyV9TNVVM2zfMUEV78Qar329lsubxaN1012jINK8aavgyRea5S8AT94CyNT5E2zkCCGXHGNNK3ew7y37MMle5h6BNCNdPNnCaxaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg2oDffGcLDWoVysbIaMiG9OrmC4vhdYTFZFk5EbZ_yNmmab8BMyN8P4B88k4XHYcESVofyqtGh1BRvmVGler2R2jJ7s0lQdJDhGny5xebjnZC8n73AlelEcq5XZYHYKSQzE1nvVzzHgqn42EHzXAyrAwsFq6OMKs6j-qWSy8McsIY7HaFlUwPkdf-6US0r2yRbldpt3O2-0zyaeJ_viWiMWVaz2sObu_P0mRYNYrksq0Gi8f7v4IrH7mRpv6pknoDXXZYZeQ866X3zkPDEgu951wO-Immgi9pRCKiHtrLQGXY7fFgM9AU-tmudFJazdM4X3VfCuVrHszWa_rizRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=kws5EdyoJuwu06j-2xUZzUJW0YCYMzfeD67B2cnSMIwpTMLMr2ObwA7V8uDg2oa4BlmFYXTviLj2QkT9FGxKweCR8haN8kPQGTvzERNSssneFinDXyZyxu84KUAH3_Nu5HhFaJBOuste6IRgxauFDCQITVZpU4RAZiv1lgyuYBadNsVUhpECvw7oWm_JStQqqVTJvV-OcmfI-n_4-WM0IkiHad1QpToNwxQcXu-lgcBGCsyZsX3gTpq9ePMkhey5qwC8TBYMegR6luO_GKfI4sWmbeRGy9dlXx2KrtuFJeu2cqdM-hHNojAxpfZaJjOLkmQHrf4HGigked5YwP5WJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=kws5EdyoJuwu06j-2xUZzUJW0YCYMzfeD67B2cnSMIwpTMLMr2ObwA7V8uDg2oa4BlmFYXTviLj2QkT9FGxKweCR8haN8kPQGTvzERNSssneFinDXyZyxu84KUAH3_Nu5HhFaJBOuste6IRgxauFDCQITVZpU4RAZiv1lgyuYBadNsVUhpECvw7oWm_JStQqqVTJvV-OcmfI-n_4-WM0IkiHad1QpToNwxQcXu-lgcBGCsyZsX3gTpq9ePMkhey5qwC8TBYMegR6luO_GKfI4sWmbeRGy9dlXx2KrtuFJeu2cqdM-hHNojAxpfZaJjOLkmQHrf4HGigked5YwP5WJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OftcdZupUKOZpQddyQT7GhNLmTwTIO63fqKywbxUsNtLw6kXdaOJ553hvWDqsUQci8je6Uo-j7Qp657O-XycCAsd5zM6xvgONjmljALMTHasSylk6nishnezMaiWo1byvQrk6aHkZrSqrIciSVDc14K3pL1PFreT73vymS7JIj5L5mSgb7LlQOfGPvMWZTbU8Zke1lopTvF4FEyngm-u1Ggh4oe-mYJOe1rBeqoYJl4kKTucLf7BEJrXCrQsEqwG6l5yfUc7wOJC0oH_hUH92CEgQNNrWMWelPaGkCK6QO5NZu2Nhs2_KGD3JvyQKHDA_VKZe-2FTdpoNh5EzDVR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXNeuV1LqJGxwcW1WHx-8PBnqAEeX8TbaliuM1MBRoHwCZ2WHr9eGLnZFC_ZaaDoz0ykE-bflPIELChhKdZBXwCqieth3X9fdawgf3_mq38AbHn9YMmO_DgIA8mpOBCor_05f5_yxeFY8wNEg4qrWV5oDB7H2azWvXvk3snC-VZ0JZKs9O7UVFfNDovNK6cYVWLzV1InsPRTKA0XD9sTqUoDXuGoGCWHwZ0Bg7SCfYZb2m_DcUCkdPpVGw_Vpajn-8r8PalR0oo1gyKsCakkUFoeq3XGsmY0GnWX_h--P7krFZXjGmK2HkGlHf0NNHGMzi_4qctI4044Y1FfowjehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKmK993hS42quTpqzkOVKbHYEy-hnYvE8waNL9MgtIDdLwc-ixIEgPfuOMoRxz4BtWXGRV1P_dV-jNATnx-OP3A6OWNhMV8ERDLdA0E-so9Jh7UKoPv1YcLSAeATzyvNe1l0mbqagspD8ooG6S4W4E3gR1FXVizrgoPihwxYDweDLg7BTl3sWo21ySpL60wJhClf5LZBrbuqtnNO__1WKXQ5qm4N2VyDkD5ldWPr2J21i4e8cHDTSe74CMYqkj2BfcEnTFpK0Uu0Le9OydCrBC629bM2JgkDrOcyxiBqi8q1SjNJf3kFEvVKksgtuF5IWtG3G6niV8Ivjo0--u8n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=k2QS9m94WqlrJDM5HdHNAQrptn0eMWN2dP24NGGzKBwJtXsVfoxZznaOw5MASANzDJv02-MIiLhDPR9JXKoZa8VbJXXGN1J4alS12EDUDysnLkGOn_8A7VO06f4_s50ctot2Y8F3LhkBbGOFvP_9lSJP4_w_lF_AbwLHPEask54HFnuwzEk-VIsmYKwMB8NLQTg2BlS6iSHUxP6Z-3PkFb1s1jYN8_bahmp41H26moa8DBCC-0x3f5uGXTSXqd8nBCOSKoEgUU0aWidSkmJP7IasZlE2E06O6oRFD7DeTe-gPgJvyCsHcICTxBhmYGADOn0FoUs_fWJjPmwMo0-QCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=k2QS9m94WqlrJDM5HdHNAQrptn0eMWN2dP24NGGzKBwJtXsVfoxZznaOw5MASANzDJv02-MIiLhDPR9JXKoZa8VbJXXGN1J4alS12EDUDysnLkGOn_8A7VO06f4_s50ctot2Y8F3LhkBbGOFvP_9lSJP4_w_lF_AbwLHPEask54HFnuwzEk-VIsmYKwMB8NLQTg2BlS6iSHUxP6Z-3PkFb1s1jYN8_bahmp41H26moa8DBCC-0x3f5uGXTSXqd8nBCOSKoEgUU0aWidSkmJP7IasZlE2E06O6oRFD7DeTe-gPgJvyCsHcICTxBhmYGADOn0FoUs_fWJjPmwMo0-QCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=louqMHhWtgezrv-mQGolMkevzvs5VItwtMG3HCek2YuuFngKUuYwxKn-oeudMHc44rGX_puxfTJuFSQd2oT_NqOp3QiI89meYzi4RotXcozplGf5ilSwwRNFuz-A69VKWI0oHySLHTFE_pWwgWLWHhMsEbKTATaV0NcRXGJxCrk6tr_jbs8YvP6CaQ-QJvmvmmpvQzm2FYYyVSIOKUfsgniaIhhga38w8nKf8Us23IdFi7tDQoCCZaKZoIZY-_3n7HiYVgN_nesSXeWJFEMPCRJ9QPRwYw6Fdy4V9Wg5Ly_JkzcXZ26rmim-NZ7sru5cJYhqhANsAOavgarjR1bSGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=louqMHhWtgezrv-mQGolMkevzvs5VItwtMG3HCek2YuuFngKUuYwxKn-oeudMHc44rGX_puxfTJuFSQd2oT_NqOp3QiI89meYzi4RotXcozplGf5ilSwwRNFuz-A69VKWI0oHySLHTFE_pWwgWLWHhMsEbKTATaV0NcRXGJxCrk6tr_jbs8YvP6CaQ-QJvmvmmpvQzm2FYYyVSIOKUfsgniaIhhga38w8nKf8Us23IdFi7tDQoCCZaKZoIZY-_3n7HiYVgN_nesSXeWJFEMPCRJ9QPRwYw6Fdy4V9Wg5Ly_JkzcXZ26rmim-NZ7sru5cJYhqhANsAOavgarjR1bSGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=SrbKG8yY2qhiSbeq7CegsemBDbLRPx_1N6UFbc7ftcqok2NqsJIo8yDbM4DOYpbFfMFxXDa6gx3M1vXXozlutSkiXsw3GAG5V9ZbJGmzlgrJFsTHVXnH1aoAiAz5i-l45QJ8nVl02S7L_qS63lfhdaKmdtZIiGPqCqFA34oOf9rzWwUI9D3uahtZWjt51F_vxluRFVrTuQxNxwL36UoMy9A7CqLvRn5Z65aLy0ueMFfD4OeKIfWJE2GZEblDiqu2v_wH-Em5E749IiohB1gj9ACHnN2g6cfe-Lw4JOexy4_De8I92jZKeCIyX95_OCHNiYdSUV96bB7lw1HxtCHJ_GYmN3EEfBqLLsPjzEIxU76J3wY8slnmZ9OynHxhheNO2PbHk-nbVTOUDf5PuoJLXZH2qi0gD6V4M1ElDgXB-1Nh8PZrGEmIBEhlWy4Az_5_gknyWVwKnbTFz1bVG6yIXzOjGrQDWYfdvD-PStBM7vy2qH02Zen0VMlgzoEp2TYKzbu-O4v2hAIRl7sNY13lFSrvuGFTxUbRlAThBdhY17G7xN0NxwlkB_DEYmtSVPGhwCw11qtYCEaWbCcL5nasPtxJZYZfK-CRBeAvkYEl8UC4uuBBeQsYqcGMlQSpIWIB9TIMLwkIFK4gOVu32afAiN7TnE_k1xfYlkrfgdHPIrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=SrbKG8yY2qhiSbeq7CegsemBDbLRPx_1N6UFbc7ftcqok2NqsJIo8yDbM4DOYpbFfMFxXDa6gx3M1vXXozlutSkiXsw3GAG5V9ZbJGmzlgrJFsTHVXnH1aoAiAz5i-l45QJ8nVl02S7L_qS63lfhdaKmdtZIiGPqCqFA34oOf9rzWwUI9D3uahtZWjt51F_vxluRFVrTuQxNxwL36UoMy9A7CqLvRn5Z65aLy0ueMFfD4OeKIfWJE2GZEblDiqu2v_wH-Em5E749IiohB1gj9ACHnN2g6cfe-Lw4JOexy4_De8I92jZKeCIyX95_OCHNiYdSUV96bB7lw1HxtCHJ_GYmN3EEfBqLLsPjzEIxU76J3wY8slnmZ9OynHxhheNO2PbHk-nbVTOUDf5PuoJLXZH2qi0gD6V4M1ElDgXB-1Nh8PZrGEmIBEhlWy4Az_5_gknyWVwKnbTFz1bVG6yIXzOjGrQDWYfdvD-PStBM7vy2qH02Zen0VMlgzoEp2TYKzbu-O4v2hAIRl7sNY13lFSrvuGFTxUbRlAThBdhY17G7xN0NxwlkB_DEYmtSVPGhwCw11qtYCEaWbCcL5nasPtxJZYZfK-CRBeAvkYEl8UC4uuBBeQsYqcGMlQSpIWIB9TIMLwkIFK4gOVu32afAiN7TnE_k1xfYlkrfgdHPIrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTJ4Co0rE664HRclWt1Z0Kh2_vgoTr8ECvF4G4oULSlzwCg78rtr8_0zvpOa717H-QLi0bLC6-S07hpLCfBC-_v7etYnkqSVwl9j4Ur2jJM9xEvrb5vaGzuAoznpjvLmuovf9RI1mTQipDZM5gwFZn2yS9xl7wLt2qIgBkSSMP9y_oatB7HiTW2_qJwBV1gLiaNXfqyxCv21pcnMU2L1MX1vsN2qByPBryje8J0XzYDBIfJF9ZxyPT6iZy8kd-JMc8AV1wZGxptaDKpcy8UWri8YsnBRD1ku3zcxJgG1nx7EhuuLCVo_HPSSfNKZcAsuPp0BfB3aYLygeaBpwNFfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=icXykRtMRRFaPo_8Rll8P-t_TEDYPJKiUeU70ZR9SUXfBKMH4cP-N2aMfAEVLZbSTLRMCM9jvd3_afevfKWYEEYR5Iamlg83JpsRXXFIe47N3cMPPorbuKnrGgnbdat9wK5yS-fuOqrrSLXWB5rHXR3kS-jG8Iotu45Xu-9yPaHIecSs_p67IDyE50k5gw5jLBJTJjCr0oZQfJLJV3-dQSGj_kCt3lt5lxGWab3Xo6FZv5cUCDpTpuGcJN9QDtWlPlvZiRUqHTgWLGSAR1xQT6la7OPvIwCM15Vuu8_c35KNRJQTbaG-ORMaSeYW4kjrBOFB7kONnSxZBK65aql5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=icXykRtMRRFaPo_8Rll8P-t_TEDYPJKiUeU70ZR9SUXfBKMH4cP-N2aMfAEVLZbSTLRMCM9jvd3_afevfKWYEEYR5Iamlg83JpsRXXFIe47N3cMPPorbuKnrGgnbdat9wK5yS-fuOqrrSLXWB5rHXR3kS-jG8Iotu45Xu-9yPaHIecSs_p67IDyE50k5gw5jLBJTJjCr0oZQfJLJV3-dQSGj_kCt3lt5lxGWab3Xo6FZv5cUCDpTpuGcJN9QDtWlPlvZiRUqHTgWLGSAR1xQT6la7OPvIwCM15Vuu8_c35KNRJQTbaG-ORMaSeYW4kjrBOFB7kONnSxZBK65aql5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTZyZxPx67eTSkQOgoe8vmKSvMmnQ25i_zsUMU_eLQz_Pp4Rm8RwYb-y9LUwcU2aLlFL7nWHDq1WRxkYXYuM3LsouKzQhMMsX5Y5PDuR5oDTrqZmJioTfX_9OFyNOyXXEvM1frnRApmypLg-3Fp02K7wCvKHiNvsMBw-DM-gLp44EgNy3gQrP8xgyIaj_SrnDNrFOL4xNFVN0RtsUcw2j-2t1zf8TbbK0vn_blEjuCz-Y_oeO5RXAJyQWkgtpDtRoAq19DR3vAIBj3rGBw8y5x24vLXyhymMIzY-u5GQTN9x_YvKN6H2SbwAJrUXhgueMc-gWzzhY9UPv53by4eYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=K1gDLrXheoS_G_uRfUSYOMHKLf06S01vugdV-A44C5ya8mMHSqTErqov9yH5bUlznR88ibIryOnJuujK66naHIN0kBIFfF9GKT1LL1-GayUYCd52-6b_QTiLpeYD_iJwVAOneOF4eClqIKzvhzS4qDB9gSz6g4WsS-7TPnqLcdiamlSQ0htyOgcQ5MF85PILVDADckHZteubiqhYBSFLJd7vEtGLlzq-O1MgakArnYDu8kSd5_DxLWGdb_CL7_Ath_YprqsDh4EexF-pufsysO0OQksKQEGmS4raUI1nItu67C8H-HRwGJBG_1GcT7BFBz4-VAM1ao9p6cuh0XV7OIiCPZIYweq9vRgqHEyh1pHnDwXphnSqjN9Wb3mqUU-DsvayY-mrUqWgl64mZ8T3mcTXPZWkJ-O0a0q4XqOHQVD1k3UHOfxDfc61mS3cFUv4ix40oXEnTh4WW_d88s_IPQCvsRGEuaCCnmMs7LHt8qSEcXAlNqnpqQeVb6R56DqfyQjCwjDPtNf_P3sLvVBC5TgLDzM5mdV4SdUGObOtXI94ZzoTdhSmuHZpgAuwWgAP0c2_pueumYf6-G_BD5Eff_1sY8cC92Y7Mu3zFT34uFxn4o-I0zgR-FaRms6955euqmZmBoHFXYPuRQWgG-RGQqkfEQ9D7kB5sq-7plgNpRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=K1gDLrXheoS_G_uRfUSYOMHKLf06S01vugdV-A44C5ya8mMHSqTErqov9yH5bUlznR88ibIryOnJuujK66naHIN0kBIFfF9GKT1LL1-GayUYCd52-6b_QTiLpeYD_iJwVAOneOF4eClqIKzvhzS4qDB9gSz6g4WsS-7TPnqLcdiamlSQ0htyOgcQ5MF85PILVDADckHZteubiqhYBSFLJd7vEtGLlzq-O1MgakArnYDu8kSd5_DxLWGdb_CL7_Ath_YprqsDh4EexF-pufsysO0OQksKQEGmS4raUI1nItu67C8H-HRwGJBG_1GcT7BFBz4-VAM1ao9p6cuh0XV7OIiCPZIYweq9vRgqHEyh1pHnDwXphnSqjN9Wb3mqUU-DsvayY-mrUqWgl64mZ8T3mcTXPZWkJ-O0a0q4XqOHQVD1k3UHOfxDfc61mS3cFUv4ix40oXEnTh4WW_d88s_IPQCvsRGEuaCCnmMs7LHt8qSEcXAlNqnpqQeVb6R56DqfyQjCwjDPtNf_P3sLvVBC5TgLDzM5mdV4SdUGObOtXI94ZzoTdhSmuHZpgAuwWgAP0c2_pueumYf6-G_BD5Eff_1sY8cC92Y7Mu3zFT34uFxn4o-I0zgR-FaRms6955euqmZmBoHFXYPuRQWgG-RGQqkfEQ9D7kB5sq-7plgNpRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=eoCpRhVPSwlXhmv_fklyVOI0nQ8FZ3RTkKzuPz2aGdxiX--jcsv3YDBQ2HXrmBzJs2CwKfrv5aiRRtKPnlIUQ7bPws86K52fSAvVDYWWzyT5vu5ZWztmlE4enDmgfailGGrLvCXo6S_ScleCrN_TLnX3N6bOO7otuKbH665tiwtx8xCubIluIalCa02NArNTEgYFU9PEMmwv3ZEIeM2zwS5fbKP5XPdxNnMOWfSI5e0xuabIvy3HaZDdvDeVEme3fTfDPJnJF1S0ocpssWfzcOqrR_TZWBhg4JKnqr9TpcBU9gDjHgsj5uDZMZLi6DSf-cN5M_yaMGQ8M7nkPQ9fNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=eoCpRhVPSwlXhmv_fklyVOI0nQ8FZ3RTkKzuPz2aGdxiX--jcsv3YDBQ2HXrmBzJs2CwKfrv5aiRRtKPnlIUQ7bPws86K52fSAvVDYWWzyT5vu5ZWztmlE4enDmgfailGGrLvCXo6S_ScleCrN_TLnX3N6bOO7otuKbH665tiwtx8xCubIluIalCa02NArNTEgYFU9PEMmwv3ZEIeM2zwS5fbKP5XPdxNnMOWfSI5e0xuabIvy3HaZDdvDeVEme3fTfDPJnJF1S0ocpssWfzcOqrR_TZWBhg4JKnqr9TpcBU9gDjHgsj5uDZMZLi6DSf-cN5M_yaMGQ8M7nkPQ9fNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RevAyYE8brVi6jnn4LboQ24WGeuo9b0jKXU8auzmoYvRmZGRONDYMAkIwGSMAefOMcZd1Z3XJtDNhvPA-kKF2vsqFkVzYLxV-RSg4DjlTtTJetaGmME-omRyHrZ62mzjQ_kwr3xR1vACTOskSyHsJ2R_Yau-mEeECYV2nyX5QvF5UVOQ8NUbhkbzNl0x15sLpkPYUDc6mdYL5E6ABTnS8mx3AblfNTvZMEsh91pADYHcIJ4ppNUn-_AEWp3KT3Yg7fzXn0LL0csaN3EehW3RS1LDGWpK4yRWU_ynFwb5Q_xvb41tiqWktdyeK4mpmTmwSnz72H71JPARddmKrLK7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=AOe4CBWnsy1sU4GbmiJwuapAw6VnNZ2W3yGffzaBZq4YCyVycqNcMDV7Kk-2w-OgmmcFhohFBKa5HxGgmpN8N_oMGv1hNbQZLoebBuu6RUABDgtjYIEFWNe9aWQ3Haji8A3UPwGT1KytKgPAgvC0b2QqhvXh3-Rk6jYHIPBEX-zJy8rOxLa4vZVKuXhSvQnCiORT2219PL244nEtnEjgDaDV3hU0YsY4u8GWeCQ0CBkGLi5cc2ZbFkQ2qdVWhyUBLQsDLnimbe6hAgP2FSBxJ0WsIeLsZOwEWaJIAV1Os968kn3YnH4tn_287uxO_lfbm2N0PMC9SBC0anaiWY3DKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=AOe4CBWnsy1sU4GbmiJwuapAw6VnNZ2W3yGffzaBZq4YCyVycqNcMDV7Kk-2w-OgmmcFhohFBKa5HxGgmpN8N_oMGv1hNbQZLoebBuu6RUABDgtjYIEFWNe9aWQ3Haji8A3UPwGT1KytKgPAgvC0b2QqhvXh3-Rk6jYHIPBEX-zJy8rOxLa4vZVKuXhSvQnCiORT2219PL244nEtnEjgDaDV3hU0YsY4u8GWeCQ0CBkGLi5cc2ZbFkQ2qdVWhyUBLQsDLnimbe6hAgP2FSBxJ0WsIeLsZOwEWaJIAV1Os968kn3YnH4tn_287uxO_lfbm2N0PMC9SBC0anaiWY3DKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx0kL_ZqQ3DRpL4HmtP2XI3zoX4xFKU5F-zNFzrUvpZFGiLYKRpPUsvsomF2MMxIWeZxC6CfqFxbnXwgk00nf63dQL7kSyBpyETnBcYs7hBh51iM78SW0XoZgCCjq45YMK27hwOvcjvCbr7TAezsgsQd2gpKOOwJNjJZH25PvyCvv2rb7JQ_Vl382jEaFno5Pqqsvtlbb70dFndM--XGHXdOukvxaGlH0FOVy9ca-ugBM6ZhBjNLcmn0Piv9FWSjG6Vbc5zaENv2DGW4jWiDX6kKP1CRwgth20l392wXXzM-Qd2lClPj_893vrspcbZU8JboCuEKdrmmEojfdNjNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUCBUFL_ObnD9yxtGO5MjX36s6W4knMsyW46UMLH7O8x3sUFWonEHWA9RYYRLXPfX86dPVQ7GIT1aCrgVAlRXew5EjwwInJBRqXDXrBGrx5CvipTvQUXC4qPMqB_qn8JoHwigdEy4BRhrbaUvAyemU2XvLJui7uxi5U7c3OGlZXtFZGhfCuo13ZiTfM_HgdOjk9CQi5oQOoiJCoo8wIgJl5D76wbd57vai9fW2zo7LatnZpRGdAiCIFjomWEH338f3rNjNheaA81w4y_SjpHq_jPM0jLL82XhAEQqoSoVDlPUkHXteb71awBNUA8P2PCR4KadM1pl3RDjgucUI6cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnGxng79CYyORT0Fb7Ce_eNDx-8rpOeF-3Yj7wxPvMWRzhN6bw8v6KFveLQ05Uc5XVNNPntwPFUMvx77fXqW131n8FI6U5IAhw1F3hZvGOz1s-zWCXI0FurTPfEldaJy6XV25lC199sHmUrGn7ufVn3Q2I8MpK4otLEvNTZgB5eS-T01UlEoD-bFv-ZF6SUUkgZEeHx-rRt5i5REdeRATTcMMKUYgoMi_deiXmaW0wSsC96zcBi_rT-3D3AAEfuvb_STB211kw5xYfnVtRvZJCEBU0dUgKSAy5bPlN4Iihrpizl25-2TqdKZ-M5AhXVNVK1MHhS8PLpsBorFp_ZFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=sppnDpwMWkACN8koQy0YPj2kSUinl6Z4rPaPkHw81Cei2KA_4jvJSFE3P35kPpV2CbDvV-PX9z6SLnbIjL5ZWWIlPZ4ZVeQAnErRcG5Q63e6q7NE-_lyQrqQTHW5igZ4ycSbdF2eAewWWOX5uDgbzlY9Y_K_HUzHr4ZFINq5sB9-5uBFKn8BaoDCCgHQwBvbIolkwMhtfLE0Kbok2IUMdUlCZnB8LTDD28I6VnBgl_UMoAOYkz209TPb0FEVuk9z-faAJj6zNuFcqoqO--XA5AEYQBzaV727L8K5vvXqwjANhvMzUyFigScY2foOGldvZYZd5sANujReyb2EngoWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=sppnDpwMWkACN8koQy0YPj2kSUinl6Z4rPaPkHw81Cei2KA_4jvJSFE3P35kPpV2CbDvV-PX9z6SLnbIjL5ZWWIlPZ4ZVeQAnErRcG5Q63e6q7NE-_lyQrqQTHW5igZ4ycSbdF2eAewWWOX5uDgbzlY9Y_K_HUzHr4ZFINq5sB9-5uBFKn8BaoDCCgHQwBvbIolkwMhtfLE0Kbok2IUMdUlCZnB8LTDD28I6VnBgl_UMoAOYkz209TPb0FEVuk9z-faAJj6zNuFcqoqO--XA5AEYQBzaV727L8K5vvXqwjANhvMzUyFigScY2foOGldvZYZd5sANujReyb2EngoWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=iyOwaC07ExokQafg1u0-XG2zb6NBCBgNUdK5HuWM4ZSXTjRBHeLRvGPtZtwenzKz9Edf6PQXMrDM_Q5D8trw2I3AMDMXctHTGtsudrZBlKSCkswYxPUhB8zEdkDNnjL7Zm2HALvGfQJttQ41T1UhcTIG7zuyhTO4aTMS9k58IrY6ooFmoHC8MroCjSAxfDA-NIJm5-rxGPEEVW58x5MQ2yGphr6DzFqf1JcW_vHfbgaBBUAHsmlo2EMCNTz7DcgxWEczh_kPTbP4J6Mv1Zy75SEyudQLmUzTjcYEdPy8OJD3Um3hUCZigbbCZ9I85hed5gBPKiX2gu2drmju9IwMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=iyOwaC07ExokQafg1u0-XG2zb6NBCBgNUdK5HuWM4ZSXTjRBHeLRvGPtZtwenzKz9Edf6PQXMrDM_Q5D8trw2I3AMDMXctHTGtsudrZBlKSCkswYxPUhB8zEdkDNnjL7Zm2HALvGfQJttQ41T1UhcTIG7zuyhTO4aTMS9k58IrY6ooFmoHC8MroCjSAxfDA-NIJm5-rxGPEEVW58x5MQ2yGphr6DzFqf1JcW_vHfbgaBBUAHsmlo2EMCNTz7DcgxWEczh_kPTbP4J6Mv1Zy75SEyudQLmUzTjcYEdPy8OJD3Um3hUCZigbbCZ9I85hed5gBPKiX2gu2drmju9IwMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx7HzOBHzGtYfv4Nqf5LuaZmC8xOwl9NyXZV9xRPGLG2mcNVKC2hsvd6Wm4GxEfVuSma2sKuWHlAEO8X__UR_6MSnNuahmI_REDpEH1JrZRDvXenyT2TnWmWcfWRWrwtUcUJYSQvarR9LhPzqdFKfyF4ldA_gvplvl9c0D5jtfnMxGrfMNDR5xuwFGy85OIuH7SONnCQ3s6pfF12gXid9hqbPvduPZkc91UF4RRhQra571sCqcJXbC3S4xPP-nEzqmDG6RhyvZkAUR0O_Q6Fjk4x5W_Nxv_sqNwoQuCw1xKq6Nn36VSN3D8xs8l_XOkXAYXs9nPwcdqYdoqg47Vmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_1utVaiSF0G8wnc0I0s-6jFu8QJqlNu7neUWlbzKDYl87RgaNm3u-A3eWHN57ywye9nsLKCwydQAW8MuysF8Vn0qhB2AouCp0-huPriUOcHOlxDFUx56gzSk5jNzVA7zCCjL4vqQxNnvXg908l-dSTAzxRcSrWsezmK0k1wzZlEhnFZrPunAQgY5CQIiAJ-4W7szqjb-xLYA_Io1NvEPwMk4AiFQY9YJvPfM8vA-5Aou0HYgoyMoq2HOc7PmDe4RDG5y6_WGzWIne0ELjxfFvRvUBP490q4MSqq1ygf7woJjv2_ueYjclzwC2-5RVuU3x63x-BfDGB7JLXUKZhoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdDPMKRcCDz8t2TMnRSk_KcUFwRquvgDkafU1s6kU1gaugORxI_VrlPp03d0Tfvj_vMcGIKg9ww9_vT8e_4ex2m8ujKR2FcW71B8FS5tKNYc5YGaMFLoHFbW9Y20xuWaUzz2_8ho1aM7tgvGEinDltZGxpT66eI45VZ1CjTDLde4nnoDhnfopRH9qb-fnB0yDzMd66Hdr6tIlbrRmWjiDAbB_s0pSzGavmBU4b-odDSg7HRy-W6fpY34uyXsj-IlaKBsTO6jwMYZPpqVt1jS6M7TfTBwhwir1t-TZvNTof6UXKFTm266jLwCc3vS9YJ6LDF06abPHOzoe1xVfqyaRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOiEeDyfnZdHUdlEoNDvYqAuOzjgHpY6BXvv823lGuonIH84T6t9Tg9KPkbrTLvAc8mIvMtKxYVL0tZ7TdnWoHMSbshEfAfTD8tApwrVib-bpJ0uSfZ7qO2TONhsC5C7a9k9WXzqlFYSouBaZzrYxEsvl5lHnR1T3gtoSpMj0GaU6X0fSGiLrrUgnOjy91g_Rlp8AagXcngGustPcJRLC8h5jG5pYiX_pJhrbQmT3igyCyvF5pgIqaVL5DPtwJSDhENmdVJyGGeiv6SOqG_rdEKouZLdyr5uEpLN2xglfwsP0ZE2xW4Mm76qvZJdPmZdi0qNJcVdAMtD4CcR1lstEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwT_cVvPmUoaEBKfmMDE4NYUNgC8Zu_EgLCHP_h8hyzaUEV_srLwaHwU7415kihpqTfTZHENq35iroE0ccZjhbaN3t1bF8oBIIZZvnewa5mHKV3IP0M7a--cw4NX4dwCc8_aAQR7hRMKgZpETGOyUvUepszIH-Ta5_PWeRwSCGJ-2RE5GHoT9p6Jc1F161bG-kCe0vL6EIGBKdXkn_ljuk_jDHpN5U9jFm-O7bKcJMMtYDIF8MF2bAu7bmElOlQr7XzsPx66n9e0cD649YZW0ySa6UWJ00uLpr5w_PvWMlffjVWJIEY2eNN1TSuhBa84_DLRdwLNAZw6rtBjYx-2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9AXIHalUyQwXdGw14RhtYvDDFAxrKsGruJDiORgz46UUcbWGLFCsKBxpAA_k4m78VUeL2Bz6nOHij8KWz2hi1SNKO8Gzgi0qrYVYYooFpJqzv4gJRBA-bS7fcL7EabOh_GBmdWzhzb2bUB337dz1J3P8g3S0Z_cqQKUwN7v5sXA_ByEk41GgdaJ5-hnLn_wjo1fZT2Agy4i3McP3CAZW3IJo1Vs9ZCCSWnvautD_8XB7BMTtFN_99LYOEiEAWp1J06qsRbOd1654QG8UalOz6nTqQlfzweeOnCM55U_Z_VTjXyfagP2fB-NbzQRqywBXTf9-qWC4pNkoXfnI8hHKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_ajVbf1_Ngn_CjWf1ePAHIKivBzSq2vWcEauuGbOtSm4T-zlPcSvIwQpEacFsFGJ0XrV0e4QXRpGVb5QBC1p31x0rD0eaPZDMMoLxs9OP5iqW6yVEyUrGWxzCJ2AVwhLClAN6evgVz1WW-w-qYgdDWqzcOyDQemTsCNHUXcpGUw-zgaY7BUPwuGeFfVtxQjUNaIInKvgLs12UDERkFkAEG5UITwPyqM9ncedyfZhqXfC-kPqzmYx5Df6kCFfdOZqpL6IbyxyNk1ZhUUcdd_QH4RuKrhzvzKwBN0op_FbI9BPlV6t9aztR1f4lykjRDOLhxlttPfaakYfTtwN3X6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq8SMvAs2t0WPBAO4neunU1e9Lbyr1Q9v3HpB0V_nXimH-bB7u0b_pUdw4_TcF8GjuHsEKND48e91eq12_EnRQuBZ9-x-z7tmdsmNoifEeCGqsEQTXNWpE7oDO-zr9qC_9G_tT756eZL4lM5U-dQh9XN4rcuz4RwS4i-lJZ09JMDUi4EzdPIAFBqWQk9C_pDAO08uqprCUHE5169OZuIeagY-X-UlfVe9gbuLpVUhCz4hemlnJF0GET6-rh6g7w42bEU_s9ZVFljEPfV9R8mILudFHm5HPEMMqVMmwQl7RPbSJ59Rakc4YD6b4kv6ow3esCdM4ykh-qPsnLHjLbWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDm-Wz5Nr7wjlrztBQSxE86D2hfifyvwrTak0Uql2Bh160GeXGG9i1UetRxu2H_vVyG7V6d7IvU6jNZ-lKc1Sv4YGc9RtoCyA7-78uXx4FDuPSnba_NzNiGfdYhV-1m_BVUZRoBpthB9bt7L-_FfY3evteE4WW8cB9lbVmbihuM33G4KOWEeJPETociUBIS5Q4lJB6lLcqxww7PSBUM8keJenB4KVqzPDM4EGcMj3BZF2ujyIeQJN1O88qg2i6iXl3tki3cx9a-EpwsjYVZac-xtNPg3EEj6d3rOO1PR6WBK4aRJ0WFD5uTu6OPSPj0lUHE6cdPi5lsKoMdscZ8zdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw4MjlnmPVC3UrCKAqJOPfUzEJGsWdHq3vlK7AoMp_uZRR1fzfx-r0zoqgJC2bkS2MgGGU7g0jBSTRGg2vnUUu7rPRvCq1037h-ACp7JlLxn7LoUS44jewN9BHAy4KWpEhFd6AWxlZyKqNDpWtuS-ukbh5-IAYz_NWIFCEKMUYEuDsJLVCuslZK73u7fsQkhY-5gI-gGHasNFKfgV3p8V4ZURyR5s_1FAvIVz8MQx9RzcWmOn795wm4G6ns_tWaOsW_dpHJp-pZKT6Bw-19cM1MOvb0di4_WXJyuY_QtHeuJHDMbCQH8nGf9Mlp24w9cRY1P4uQj0DppSFxgOrxdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehNjU7-X1CmQAQr6scOwQzMvFVOMoQHs7-nRgrKbD6pgj5dVODS5xUybiR9vCdN6GvOs3Ooj4pvmM91GqbpFs2mq6nxgmhkIloqt1I57qGdBs5M6rTaTYyj8Z7KJ7332fKzvJ1LNdDqtRel9fNvlTsJnHhYrWVw8Y0FZDpfTvfY1-EJcXZgd2XC5ZiIUswZs1_GahOLb6_PXmDWse7gZahLQ1Qq1CXSIhuVi7OL96OGZL9E1sRZeoJFVnsMItdeglceQlt-qKbz5Q8AE57v2YRmuCWppMUNyr93HAywIFAgSez-PQGxvoXxqR0cEh8FcUnah_n1qaAoKr5J3PTujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODZzKTfxpNjhJ9K8tkkLlHjtEBrjXkfecETwRN3MJux3OAIUFZYOTuqeqQtGELlASZY2cMYdzdSGFlNlx8WnVvzGxtMSH9KssGOWU5Onf_BOTeRtY8X9TvcNMIyELskJi1XbKhjgxBH-71f9HTzQQVex8sDnM2-8gspEGmBD67BbPVSBLx_qAXnrmNr0qtVMdO8DZ-sAELoKAthvkNopM0w3n2iSQL5iFo7sFhj6szjAQ-c1sRxV4vYTaLcynmzbgBd3DLq9_hG8sQaL7WvYpIcJCTxxV0PUq8x_658kbImLxrtZpOzniRk9xHYo4PIc5j28wzwseXr1C6EEkS0oqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDFWYSzd8c3LCDiVLc8Gnofil7g8vaMwJEceKguBPlN4sF78WuSVeug8yMFsNFQrTlCOBMubJlFEDwvI58Rzkbu2Sv8_PfaBNk-b_0xK2mP3CTDAm2mJeVHG364RZNhugk0UgHI-pTGkvNoYrB9bJak8SBRW1hsHc9h6NIMWkCoAtMBkOevzez4LbawHv5n_hL96Rutv5nkJDUCIF7V8JWGpvyd8TL6JbVEKGZGeTxG0fLM_rm4EfcW8qMBs7Ra_O34zOjL0REwH3Q-EhrZZlfzrC8XFBajXbFpLxAryWKNkEruO4eV9i7iUBtQdFWLuEahWQRTQSgO-MDHfXW7Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=eL-_7amGTXz15ixN-FDYbG9aiqBbStWlZi9HKj8mG_K2Ex60jLOhoAUtJgnjywBJevISxtcYZu2Q-E4SoHYGREIKlsyGj_mWWI-6MeVkqIShzdqcJvs2hqR0UqtM_9loGADt_sqfS3FoSuGuNFdjjbOdRGFOKvN6bBDTSKxssimcxpTiS1eYn1F42w1gwmaIboZjfgRrU07yh9ejU-jXyDns8FouJVcdK0_3rfOavjMZvKfhbrX6W-Ebt7qiCK841rO_XKNmJ5rhcuo63Pl59gwfDtUn0u1mqsXvvTwMNH7YiovNskg7yP4OUCcOGm2JfYVQiVgFuPKwFXHAvfj4lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=eL-_7amGTXz15ixN-FDYbG9aiqBbStWlZi9HKj8mG_K2Ex60jLOhoAUtJgnjywBJevISxtcYZu2Q-E4SoHYGREIKlsyGj_mWWI-6MeVkqIShzdqcJvs2hqR0UqtM_9loGADt_sqfS3FoSuGuNFdjjbOdRGFOKvN6bBDTSKxssimcxpTiS1eYn1F42w1gwmaIboZjfgRrU07yh9ejU-jXyDns8FouJVcdK0_3rfOavjMZvKfhbrX6W-Ebt7qiCK841rO_XKNmJ5rhcuo63Pl59gwfDtUn0u1mqsXvvTwMNH7YiovNskg7yP4OUCcOGm2JfYVQiVgFuPKwFXHAvfj4lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-H6iWr8V5f3enSfyRH78CkhEl8oVclRcz77wcTpLw2Mf2olnHS6VbRshZavLC0lcaHQHKvx5gv_LcwMK1302jQlEceRW0Z9DR_T491-TAYjzgRyflCZOacVvA9LhssFaevHXZGNr8D_0XIZ5r5KQkEQUo_vFGAY0J1JUikzT5kNSfQT0w6SXAkzKfTb6d4P1939LkUmI8X7vmh6mKvS0JDPNt7ez-PLhYXnG5ImWl00ACwWrLjY4INaAc_uyrr-8NkpolIXxdpYhzbrRM5f6VAz1nNZQny4zoDfUhkScJNgIp-pFQH8BKU64q6cWKXqJ97sXm-T9JRl8xg3BM3Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_n09JkNY-boKH0bQPkcC71dR-IgHkijSXS6esttaISVHYhr26g3S9d-d93EGH2YPxpOJiJelUhan4eWW2M1YVrH2aIJ-58Z4v_GrrOA_RmUPkihLl7o_jjgQV0C3ll8pjd_oLDJKxKL_7xAxbtgTFuiRpktqLJdVElKn937wpbBSDSalDIeJvj9L3-huV8ie-Vs60c57pSALnqrBw58RyHDOH5Hs_10cLnJfBDMD2YQ-QbQc2JG9NN6z-V95V8_jLkYBDY582QcQjfWUegas04TUkChxCBR1eR9b1rCfkUerMsXJEWywP-HT5zhkNbaRvTos7J8GrsSyAlyYsFjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Vq_XEWrvs8Piu-YGfeuH5wUXW7qau_aTs4LkIModGPzxw7ECvWuO78STMBjkYLhT3EFD5KQUZxyHPScVTrGhgaxsFsqVhZnqNmHUdBtk_6xqkqDBAIlUkXQDprGShl4bB6ATgWySLv3SOvXTQ64Jfv8ejMggcIbm7gjbnprKF-_LSCxzjB6jux7YOm4RUNcc_aD15psXReC0-jbPDX9OknmHeNqjzYhy8vVhXjcpFef5z8TTDFfKg09c3G-yJ_4E6ER2JJx9gQlzE73--MCOltbCiJAzVkdlkkeLnAztw7tebb_e0I__miWO-f8G-GEb9szHznOy_lCfYZ1J_mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=Bods0gYlznf8-EC5x01WhJaz_C_4xeVWFT5MT8mdBZqQ5sAPZLZ2BmVbIvJOp52baPzn8BXtawWuiYLW0kom3UJq9RrkfFEk2gw6qt9uazXi-6eXSgiJrmmkg3WqszLmxB90KvxtVOkYj2TuBV_1CfLN3x0nlIENyne0Pd5bDsZE_DG6EVleS3M5FvyljgzBgV25yZi7K2pYyRZ2NoKWoRS0LpmPlymeNl6AmYRafi9m5IrYupZ1YKeJa2VLCxNFoG0kc32n9SWbgQkhxpFes2J9tCOmfJ-il5kt5QaA_9P1Lk3ZY3MBm0GwqVfcquZPt--50D4f_PDCgITGX19mcqKOBIv6lwW-o-TuuTa2J4StvC5wXOfPnDNAgE_1R23UJZ36bRHufj__lfNYaNgypJVzRfU38peOEe-Ma9cyQpxvkj2FQ1xdOGtrYrBKERNoYcC9qC-P1ujeV-wuKgiEJ0qTG5Z4JmnmjoNRLI2ia1VJ158US7ziVfA65ZAYAQE2qJHUZpLrEI7Xo9fi81coByQm9OYL_QWBC7AKwl0CMrrOAEIDa_E0C_230fFiLh8-cn1rLNtQ65G1PI-bbWh4XnobQHiylC1j1t1F_qXwb2LwYI_dNxZspXKPxipNHK8zJdy-d2wXVXbAp-SoFvUEuPwQeFqdyGYV14mhTSa4oBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=Bods0gYlznf8-EC5x01WhJaz_C_4xeVWFT5MT8mdBZqQ5sAPZLZ2BmVbIvJOp52baPzn8BXtawWuiYLW0kom3UJq9RrkfFEk2gw6qt9uazXi-6eXSgiJrmmkg3WqszLmxB90KvxtVOkYj2TuBV_1CfLN3x0nlIENyne0Pd5bDsZE_DG6EVleS3M5FvyljgzBgV25yZi7K2pYyRZ2NoKWoRS0LpmPlymeNl6AmYRafi9m5IrYupZ1YKeJa2VLCxNFoG0kc32n9SWbgQkhxpFes2J9tCOmfJ-il5kt5QaA_9P1Lk3ZY3MBm0GwqVfcquZPt--50D4f_PDCgITGX19mcqKOBIv6lwW-o-TuuTa2J4StvC5wXOfPnDNAgE_1R23UJZ36bRHufj__lfNYaNgypJVzRfU38peOEe-Ma9cyQpxvkj2FQ1xdOGtrYrBKERNoYcC9qC-P1ujeV-wuKgiEJ0qTG5Z4JmnmjoNRLI2ia1VJ158US7ziVfA65ZAYAQE2qJHUZpLrEI7Xo9fi81coByQm9OYL_QWBC7AKwl0CMrrOAEIDa_E0C_230fFiLh8-cn1rLNtQ65G1PI-bbWh4XnobQHiylC1j1t1F_qXwb2LwYI_dNxZspXKPxipNHK8zJdy-d2wXVXbAp-SoFvUEuPwQeFqdyGYV14mhTSa4oBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQYH367n-FB8ZB-FSOPex96yrjlX__EdwesqOptg1QWNGOwxHT5EHnbPxnBqfh7nULOYri5yr_Ur6qm3nzkMDktDSTA72iTi41opyrMtYJDITTsZosRQ9m7AbNyFjzzq_w4tx5zyZeM6WrEDu3exO7GzRIvANWbyzxTuSVWULTHlovm3YDYudewxSKOPhWpKuIPDCPl4UPoi6737_RV8-hbptNWBKNoNb_5VDTu9T4i_JNNX-9wWpWPzLQG1G79GsxYE2x9KO1ApdCwKzjQ0M4dEy7Rlc4LsJVWvmQyVYUt-PnRPV7Luezi5dtolbQ6fEySKsQrLvm9HSSiZGBgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB6jyR4eIuWmpmTVUjytqF5IFeJykCmPo8WHgyERfKGHFETjIsaq4hXr3q-6g-xlH0mSV6XQsJaDX9OroCF0CijvOGljNXQUI6v-dTMYTctvzrxVWtMrpmnL7W2DmKTMm-h3wwF-pa7gjLac6BsrgOXO8xtexHQhSMmBKgGTdkgV2G68zEr4dNSBUY-c5H7c6ZehD8rHHDCDLtn6N0GExcd02_VtZnSEo5SBkpVwpHs709w8ifaoQhSB5Okeg4rZkUUYRVzo2qNd_GCEc22OyW_XmA2hVS_4Y6ol9ol0NWjBwoQWlE8hC5FXL5uHudVLgtvG2FrGSpL_mbEmabcocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_4AEi48s5WpJY7p3RzSzIghb5E-mxCo_-x2Ia1dIQh2S9BB-I-QFg9sG3JLtHZ2ZE1WdYxCQl8SKc_Q4Ag5V4TrXpmT8CP_6xcriyD2IcwQOXSPUzFaitSwEITzMCZ8tOzVtqDNaevM1Et3Sc3zibanKX57c76gNZYgGPDX45WhH1A_ErTetATKE_40-kJt_UxMFbgJrdJDEaMkdgk4JrfrwfwNHx5p3Pm6pQV598jwvMzRXxuGUZHX6rGsSVD7kVI6ipv-mSL0QgIceBYiUJt5MdXUb-Y2Sf8VLQK3v1Limxd7qbISMw2fi6QVT208Lkt0EliFvZl2HseLyVgSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePQ5kYzkhcAjsb5wo43q0BhglCVQI5rLfkmDOyK5eDUiFWRZzJJqnkCBdVHgeHg-F2im6SbHNG5GaExPxyQth48yua-fxq7Mp_NB_mYNlReB6LM6ZeV9rhlH_Eqd-6HKBUKNGpoMHzkV_rIwk9wi1fP6_mNYZW9uZHBgM2c9trHjBhpjhomL36FaS_lW2gyscJnFfyYn_WYLbkPljB6EJHXWsOmOYPD5W0LIZLmB03vF5hZLu_k09fhtxH5ZGPdB8dgdGFuWXHk8VfJV0OI67sr1ht1n_5kvPtc5UAOEA6DO2TuFNTP_NRY3mbZCQpdMxgYz01x_VCLz3kiJGWomFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIO_vI7NG54HHsAmt8kmUhkoHkLfbXHHKT_hRmse41FCsL-xx2uRsDXCeo9uTgpDqvItvbNc3UiLe5JdRP8oQl-wfbdLiTZF13P-dK-vFQvwG_DTlzvDrpK_dw8Xb1X-OSgjdfz2CiWpPhFw8_QCisYgiktDRbcbeOWZMsrerSHXJ-ZAumHo-w_VNoKYYSIgl5SumrkbT_3X4LZFNXmqg6Xc-b5qAWbRKzABXKkWC5Ws4-5_omjLAEh0rC_cJIYXkZ88MbtLLw6ICK0_vBlrwUgK_m0YLBzzhIj0CzztQkRfhHE2XpBeA8kDnoJBBi21KW5DQ58bPz-28z5LFRc0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBGNHoD6NSlNZwNZsZTrtWuRRENMl7mXGMEdjsYt8jdJTCsp4gv-2OddOXhp7aEYqm47IAVUiNhaRjFGLI-45Sk93kJpXkD22xDtNC1jQRD33U0ybLols2p1IY5pSox1Xe3X5CvWm5YhJVAIRilvWVo9MQj8_FMYNBFW833hX7CRFck-BCIX1j45PyLHBcDoF9EgKh4edduG6AhLyEqYRuAEcH3mxEvAtIdHb8yWtlLV34E168Vbe4FigjyN9fcvw6EdoAX04HJgzP_CZkLHaA_stFoDJnKrRwglRFIN94UySJwnQsWXOPip0xlOs0hVcq2en9JFS7SdY_1Qd34glA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2P3XPQejSKOPhba5gRnvnAHQUKaFCAwJJxN8jAThzsz1U8SHu_5BJgbWNeFvGHv1Ou1mgOBbz6_EiKdxuPX1QQkpB8bG9uUcPKzaM8N8KnlLZ_bkqyOS2LNA-yV3bAZZSGsuweuTiNBNvCkT6JSp9RYJGSvcW7BYvUVaviWwn-O_VCjAuSbfz6H1FwXbbBzNGdir9Tu16Kx5P5j3qVL1XfEZHSBKIM_b2pCNXf-Q2jB43BGnqMCi2OjBBwJ4GqQh01bZyGfpPubZ18pOf0lR9rsW7vhUZkQHPxadQ0dFlqzsfEHv-zXBF1Gg-OYAbG1cOJPH_3ASzsh3wgbFqxpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaZyNY7WEQzkBwrMi1fHDAYd9adFiM9Tk9mS2SLpzo3mmJyIYc_NXE8eUXUcFZbL9Q66Oq8TSvcIh0By65ugdSAjt569fDRxOolJZUUoJEni5w-JlM7c3UtxP832Hs8PIVV3Djhu8q1lvvZ7g9yYeHjhaI7yrB6X_UYXyabUoONsSCozD-hhcpv9_iE03a6yhkBv2KYpsxZSqBGN0oRL6r_7Y5bUlSCsPP-ScOfkX_ckeYSfBufB15Mk7BSPeZwuj0wrc740BWXGwwffddRfHHWe9WD6lRGqETNuldoX_hGcsjpN_tivu5iCg72fZgn4Ixphe1VKMKqRW01k8_pIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSKNQ5atoO8M0U5AV042vUD4fbQx1-pqyj5zwqY_G5KsvC_qQarGzm1NsFY09UjEfTopLKrXtsM7nAVjMh6K32ND0EW9tRz4ihR9857CeSfOtzsuVimzIZ3dG8EgTYRcpwOA5uZ3C3JmEqash_3advIq17eHhNbTGcohGME01R9912UfJduipZpYEjsOz1cFIW0GJT4waO_ZdenMxvnnYVWzl08oV6cVjbECOgNXlfj2enKd5r6WKlSnCop_OaGrSv9H_89XIilzH0SvW55yQ7_nvpfGqXmT_08o6XkLDAA3OwzsQvTyMmfVFqmle__0T0oiEJuBHOszs10ao5ZUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSwFppBjponuuwkzzXJ_7-rF1X6dYJmkLeQqXIPuKllacymlTOOFv_sUlxLVsAYui5cJ5AVZQMk0xsum7dIDsItWQNuFNqKa2ua45mduR0cl6WnNr8uvDUBTyzMExodgF5hqdMYCbusl2LXeMKqOv09Sz8jUfwRv7y-e8-pau3PV_LIq4ZcqBxGBMjDJ4b79dWvJSwtUc7_vm8n7hVnlGwcYp7MAfAAEWmVpBSKNzWPoJ-cCNgqWCJYQT9rJX7MfMJHR83aOCWS5-ijmoEO87dOIdem6VccL5nhS-k9qrmvEwCG4b0Luyy5WI45nHOtFAilKel9a6rJe7wxOvAK-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2IEnvi1RnLEGJyiSvx9Qd6JtLB9vmqgr8NAQI6XWtNt_ECm1Q3aM_VwKfa3ejrApngxiyL_oUMhuPrwQW_dz8QQEoyK19ihR0HZCrk4K3OyoUnT_H-ot69epTqtN2jWEbv_y2lVqIpUUXzOG9zXYHDE9qS-9eRsPq0ojz9ikX7omTzVOWSXobn0lPD9nPOqiUoDQV5RRKtSSpBZImEBhOJggiMcqY3RJesWk3wEaDKyG4VyvKrctsar2Jke0qCiswNlxnZAK90LkSgJu0oBf4b1AE39JjehgIcFD6A1EmNI_poOOASmOIIPwnUHiAsFxFQvZNlxRkr777fA-5uKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP8Ab9DYUh7PZnwIgybkOShO6JGmBk584-_FBsvH17VyjvmGtVzvA6-5nll8CBJq_Dnr2RYsA-JcJrO7fiHLE9_ZVoFNJTKEhvpnRxX0X8I3bWxLkfNdJcUazve312TsMhdrcFlREe6wz91Oj0S4TWNAzYnjvKswlJdBPnGnaC0L0dq6sFKwRJBZoqHu1w5XyPfnFbJeLWsShUXktFWGBb7_eYmEKdFUZRYppWCFQzlcGrdqBa-77VZqY6zZ3jrGLJjrknEQTbGSm5dKXpAiPoQ3BpIXPqxjO7nIGvn6SU2CDzfXj5sNaqkglT_z4hGxzKOe3a6_3Qeqvb3XIa1lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqKHGUqbU7M-4UwPge9e2YycZyPAVPAMcOo26Wz4_VdlBvbhvvC54uH85auTZsgVy7NsFRVJhIoAkR33B8-MOkBmRuzV672mXC_WIvnnCAN9mwx7yGRrBXUosepu_PyejQmqkrwDFhRbUlcocSZxVoFEJfHFBYHdcbjuZTWdOTv6M3cBuIXNnpTjwMQyS48A7nW75h_0GkKmhO4EG_8p-8bvdZuuqlyid4RaasQW-hathbLlR9p3te3ZWDg5E01KQOYRFO8alrRApOkgtIfEKQFMLtgzJAW_FUblKydGux1mEEviKKqpnIxzrOT2q-rj9Jc8iPe099FhP5f9zEFO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3nOj58Uvg5VYu0QR9vVB0uAi6ktqqukZ7AftU4FBBDcvxHvpfuiSSeTlltVZSqcqp61Db8BxN6UJw8kqN1fm6Uzw1e8gTbLcoGwOBb-XmHKsQEqb_ZAESD0xTbazmQeKo4x6Abnn1M1KYLdJXXv2gp2N4y58qlw2toT7MgJH82PPjMc3neVuWrzyaojkxxjdnZUwjHORqO8GRevS7AEqXObdYuqWvoo9_BMF7F4PibP8IuQMrlAS_3z9p-4d2LoxndsJkdjQ6bM8Ea6DFO8YVaUv7X1rk5q4ii8GH32CYsJC3kiVHboVm477Td6Pi6oevHxwFBm-I-mCw8mqzu5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOF8F9XCN8AY0WRaf6A3o4OV084dy8_KubpKbwe8F12c9dFjxekfrvgb6evaki4-C2DxfuqBefVCMqEeq1agmrA35FsWIT7vVpxD--ki3ijX9NZoMZGkF55Frzt8TBSQ9Y13_SrmNv-lXbaUXlJEXgubFOPv9NhR8Xgv9sHmtG38BRuG4WTomZrjZYwXAamWJX8tshkyiFDGPufIe9VLH54lXuAuiI_s7W4LRwLKMcpdv0ldzNul5w8EXdocnj5D8yUVjfyZzVMYplQt67mL4DVCKycdQhvDfOwYEcDkUroaRvdTE4QAltcDM71hE_lMU5epUg9ld1YdfaN1rXnFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grI7MhSvuCAbJgx_RB0JndoY6ZFJz0k8mUzk3OSNVKe8pbNQNs7W-T9o5PkpqPSPQ26aMXSRpEjDo_rLKwv3j2mcBESajx0fLGdnhW8cyMydOlb0iRTf_yeQ7GilO39SnRcIXiNmu8ZR3ep8aKfs9CuWmNu6codgh0b-9DNu75ywIK6qVyg7ooSu8jmLWXvcJbifSxutzlDDrJqxBAJCSgUnnX7zkO5PuqPw_6V7G5jzTNPrysKQsEu15nwK_y02u7k2dWhlRYO-_m9kRR7BHnvpG6QfN2rQNjPSRYFXehugAXBkkCj6rZjXdNjDlzUFSAKkcpmmSfv9S9D4b2kHAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7Wmb6uDa39QQO0wiZsWpN5auGYg6UEvjFNYj8Ot-tv25macjGKyCP_LOZYyDWNvjJhS-lt7dkZFXPZRQ0f_cC0D6VvMudgbFZjPgRjv977Gf_WJRuOvrxvNAX0pXQp-4uPsuqokAwaVPQaBdYKxsXgVZYGzm_xUzcM7qcZMlITrhkEF_lyn2H1FIrU3ZWCqZz1y85HSPJAJmfRE8oJba5OkXBKbF6RcvF858wb2SGYDxBOKrE5uuOhKHUB5456oIBJypxG9rc4W84cYnDjYhu8gFe-qN2hUwIOHSGK9Axw7zmt3US3byo7DuocrWhFA8KtPTAHlnawAPBf8JP_VpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm1BoIeQ7KenCQDEs4Srm7HuC5RkOWMMWWupIAXb9e9E8VpLoD-1FUsT0uTQlUNa2TMPUZoJ08a1plIGfpCHoNuEN3OAJ27Zyycad-1tz9fx8avRwrTsu_HoMe8yvaqAyHKyNuttTvrFLLxv0H3N_PEWHEuQ_Khq1o4RKb4FC_sZ6dr4_8ASQFSswK59fetc7A54CVbOAoOL-uM09B_HEYYbrOBv-VIh6PqTstvRfUH9TZDD7NtZnBXg4B_oQ8zjtZYuzUPcNYSdywWz-J2oZnzhQ7_0vggzk6G38sJ0J0smY0LJIQcryqWutJ47ew4RDAUnxqInkz1jtuNYlQzf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6VSzdKNQiEbQpBENlHqwOq9rLNkvVtYi8JCYDAcUfYVmv0tOLfm-2JIYZB4QQPfCGwu-r2B0Wb6HA0WH06s3Qla8GLKBff1TUtHXcCWoWznunmaDsGLROS4QyxvmCr4n_5m7wfIOm1zIrsiggSbpvYFD_RivJFUpydAfzoSzXHjYFIPENFjgvoAjgbHJuu6PmiYPupN5L1kmUw4ayoEm2vBHSryFeyedHLihsTJKeHkVO9OY65rLMUPIeycigQp4yXdtBvCMT3Ms-XABwTa0W9Se8niKEkISPlHMDNAQOwC2AVariSiUpu0M6v-MNPMO3_0fxtYrfwNfosv5FBEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISmozN1W1OMY5ccfg_qoAqkgl-sy2mbch-rorik_8Pdef62iv4_u7mCGm_o569CEp1kx7EkVG8yh8JKkpPAvmLuAepJxfX9vG_VoF6Bhi4ir-Khbloj81bl-6_K0HY5c2XGApVaso8dbu3Sg-Ku8stCrsGNLrEOwe_03YprL4M4ueAKhTr7yew6J8JgiSv5lnBxMrHwxPX3e-YVWE7tOZbFXIEjiwH2Fm6bWXIiWk5SvFuAyHaP4JBeXTRuHDkeRaYJH4mRbXCI3rY3NmZ5Eseww-mmiZiQ2Z3ZAHFmbBfms5-gwLISbo38dCIbBRW33gzoknpW2CwKOVaAsUMS6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=gOF9n7rvi46yD7B9NICZzkkKLc-Ocm6ruo0lfKErQI1bvssmwXEpjUWNv3doSafjShV6jzg7AlA3s6mZmW1RA7bgMJBCMRgXSFhk55CfnFj0Wdny-ufbjBjpfaCgH7oophIW5aELcIC3IYOnzp5DDTzHhsxT7SzXMSmTM2HOSSrtTLGBfPXOWhztSCk-bcXSTW9VxupUociZzWNw8Bm2hWOICVv0nWZuNvKvpHnPa9Uwps8PdWosn_9uauySK-ffuCR4Z31zq3axqgMPfnlQ2_wVwHzuw6CtgLVifGi48gfXiqrIF_q_WypaygGf3cxyyp6BOt4BhsPljjBjPeQWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=gOF9n7rvi46yD7B9NICZzkkKLc-Ocm6ruo0lfKErQI1bvssmwXEpjUWNv3doSafjShV6jzg7AlA3s6mZmW1RA7bgMJBCMRgXSFhk55CfnFj0Wdny-ufbjBjpfaCgH7oophIW5aELcIC3IYOnzp5DDTzHhsxT7SzXMSmTM2HOSSrtTLGBfPXOWhztSCk-bcXSTW9VxupUociZzWNw8Bm2hWOICVv0nWZuNvKvpHnPa9Uwps8PdWosn_9uauySK-ffuCR4Z31zq3axqgMPfnlQ2_wVwHzuw6CtgLVifGi48gfXiqrIF_q_WypaygGf3cxyyp6BOt4BhsPljjBjPeQWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/layYRyJRv8FmFjuEYNR1aie4qGJ2irtstC_vGetj1OZ7Pc1VECADAYlP_zw5yJyKACzk6VDqfCZKJJxk3CRp8Gf9FisOsgpYefCaK5Zz_9uNQRQ3A1dTI0k5XuhCbHek270vfciRV8KPelM9z8oGiVoJWibB-3tHDQO_KHFPu43Agu3TYdQy4gzyIgenh6xUH7pap12ShEMLqPMDdD8vU73ubXAWjMdAKYbXnoGG4PI2Ph_gB2TTdrZKKb52KGyerSrgz74DGK3bF3EdcSP7cv_2V82JL0ltkg9CADHuQNR1z5OmogKoAZKBMa_5sUIoXTgUmGGjtSnoLLKl87DHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUck0cDsC3Usx0vV_SnqsMlTPF_EoNYNhaIuiQFlebyJ1Q6RaBPc3cvbxZb4ppuPXudZDJYmlIbQZBG4Tw3SuulmuwFD1c4r8abHf22AqK05s_peeS54sKRtBRekROzHzYPPLLWtzrOE-ysY2N7_Y0kkbNY5CYm0912WKIi2pbWnxw1VceAumB6LQFZ5irLvLGYma5-YEWqRmz96K1YaNt0tbx7Wk6Clby1QOBVthEIcsUjJVhZlySxgqgwTdwL_4u0wuwv1bVc8rZXq4MJ7Qriw66mMydZF_BQd5OcC3FXcs-Cg0xd1kwMWByPy_9k5dvCj9NQYS7nbTeNn0Vz-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=V0bREWxp_oWcDgG3oaAq8aoHX4YDPr0SFMonNmLU9jho3ZwbH41k9hXzMzibFKmkgb69ZyrgLruZaX8XFo9NhhXJB3RrxjTtKPFc1OJOTqAHzfw-g8UgblfmxO3zU5hUh9wU5CxzNESar69oZ5iaPr0DPbiNooZ5DCB3jKcxImJuGMU61TYlVI8DZ7cQx76zbIOplOOIjydWQwYOaEQuKiMD6SMm9KrgNw4J36s-ULd5vafeXn4UYlJJn2bw1G0Rh_S8GC3PVTUM9bK2j8xeSNYBRg7VkIlTo3XiXuf1Yb7BEJU2m0yLaPuxR4YHBJlcojcyKUsob0WDGy-JuE3sdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=V0bREWxp_oWcDgG3oaAq8aoHX4YDPr0SFMonNmLU9jho3ZwbH41k9hXzMzibFKmkgb69ZyrgLruZaX8XFo9NhhXJB3RrxjTtKPFc1OJOTqAHzfw-g8UgblfmxO3zU5hUh9wU5CxzNESar69oZ5iaPr0DPbiNooZ5DCB3jKcxImJuGMU61TYlVI8DZ7cQx76zbIOplOOIjydWQwYOaEQuKiMD6SMm9KrgNw4J36s-ULd5vafeXn4UYlJJn2bw1G0Rh_S8GC3PVTUM9bK2j8xeSNYBRg7VkIlTo3XiXuf1Yb7BEJU2m0yLaPuxR4YHBJlcojcyKUsob0WDGy-JuE3sdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=iDL3TY2W7VaUNjHcRGZkspEk3tyk3ut25RJGEhABVZtzNV8soKK2jCsgWCZmAVNNrOFDTGqfB_UeKQuL5z_3UjFUKFBR5uV7bI_C0g26usLl2ZmwykQQLdp2IYpNy9CmakcO3MADJ-WMF8OOjRkesemKMcARhltZy-XtPaVCSSSMYZWqMIAgi3T463c-UWH9g1HxMRVpeXlhsegt4hTfQhXHLZSXX_sppS2DPsost_GvXXxQXAERt6u3sOOTOrmK4OIxE7EdcPrdqapkia1c7zL9D1p_Z_Hx48knRBCQrgKywJ8AFyDe61me7TkduX3No40mDD3PZtOzOUQ84oydBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=iDL3TY2W7VaUNjHcRGZkspEk3tyk3ut25RJGEhABVZtzNV8soKK2jCsgWCZmAVNNrOFDTGqfB_UeKQuL5z_3UjFUKFBR5uV7bI_C0g26usLl2ZmwykQQLdp2IYpNy9CmakcO3MADJ-WMF8OOjRkesemKMcARhltZy-XtPaVCSSSMYZWqMIAgi3T463c-UWH9g1HxMRVpeXlhsegt4hTfQhXHLZSXX_sppS2DPsost_GvXXxQXAERt6u3sOOTOrmK4OIxE7EdcPrdqapkia1c7zL9D1p_Z_Hx48knRBCQrgKywJ8AFyDe61me7TkduX3No40mDD3PZtOzOUQ84oydBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nScmv_pO9T34PphtNgaxVr9BYy4U36UNzFRCnuVJvEXxtn0U47Gn5-qiv4IIX_Li7PS-kH5wceZG-_k8hssff9tM33brDChNMty770WQPmiH0DrzA6EFRdrIaaX1h5QoFF7MhKLitMbgUCjUJae_rr6lekD6LzA9l7qmSMMcSgIiVVT4ch7DM9XUFUVIi7lKhwF-A7YuuEO2lk9HorbKOIa3Gpct0fRlfm67qWXC8CZg33IfZADAEGB7wA4HiozyFKQM8aPQk7YTy3BwLfI_tEI8BogWaZtHX-u00L4W4-WJ-NkAGL6CjO2bycKw17aGEV3x1ZvqG5iQZoI-yk4x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz5I-75mbBdQECFqi3qE_QnGhypFBN33bLsXQLVTWgNUuXvOB6zDFUNNzJoCEc-YoHwK7Kd16cLALHwCSZ4DzCwUEyDiWWpoznthq-QM029pd-w6pbDHc-8kqgsAK-IAm4l6SWdNlsb3u1VeCPx900jhhcX0c8wuRZypZqsw9XGWFIquwN-9rK65cbHqOA1gFqygSIPL9SIZnhqgDEuY0dCIqT0UVT5NBB6603nzTNZi-1sLbgKjJ9-R18H67JXY3ne77zx_LYogxlT5gtR_F1bVNbBpqsg4nP_02gt9bErT_xbnjQAXgXqfeoKrf3HjvLOsP_LovG1-U2k657nn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=uFv6LlfRaY5FqklyRl83ZD7NSriRhMsqgs7UOAxvw6gvvvx_y_f5IJmkt80o21x0lQaN5NhtC5N6ytTcqremQ6ENP4y-q96yiwfpk1hL1WsULUn39mzmXxK6ugX2Vm3Wpdh9IG-O73Nj2eGXP2tcWIr4IF9Lg-oOHgYrgJHfu7D6K2ieGuMHaGJxJ_k4qdWXGH940yVr9Qtg-x5V96tZKfp5TGEL1FXixm7r11BIUo0c-D00r02z_hMXQjiHyWQiqoxPp-wK2BGdK-ChysuUFwK6DKL_6bTnfjBvCLardo6wFUxjCIzEAnmkDjwjO_RpNUd8-xurTda8gn_tWaBTcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=uFv6LlfRaY5FqklyRl83ZD7NSriRhMsqgs7UOAxvw6gvvvx_y_f5IJmkt80o21x0lQaN5NhtC5N6ytTcqremQ6ENP4y-q96yiwfpk1hL1WsULUn39mzmXxK6ugX2Vm3Wpdh9IG-O73Nj2eGXP2tcWIr4IF9Lg-oOHgYrgJHfu7D6K2ieGuMHaGJxJ_k4qdWXGH940yVr9Qtg-x5V96tZKfp5TGEL1FXixm7r11BIUo0c-D00r02z_hMXQjiHyWQiqoxPp-wK2BGdK-ChysuUFwK6DKL_6bTnfjBvCLardo6wFUxjCIzEAnmkDjwjO_RpNUd8-xurTda8gn_tWaBTcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsTejlFbQ3z68kJDSMwOMZHhgP3H1tN0HmXzvBQPeU2BvkTLWwIZ75RFeVbQ2T6tcQPg3stz0dyCRcfSkX9efL8bfcX_fsVpbx2yRnqyat1ntHzINZGfLaVIytGfdp-yKZpFXykv_I_ZS8gGzh02desYAws_7597qrWMg_7qm2eNj_IyNBRv6ayYy6H0vL_UPD1V3Oz83cbpHBTi3LQIAUmZnNmNq8tzb7lXq7Sc6dAaUSkxWmTrCri9ML9cIFgmoRZ0F__pVibwvYipcWBAc-MXknpQiYVfL_4ogwN11iXKSEH6I6GY0Zk-M4pXN0JNiWVmxvxcCVfwqOpVMnw37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e23p1j80IW1gqore0LrwbSXeI4DpkcY6AAgD9Kist0dFxR8GJVVu8O0qNvARUz3SBs990Mqoy-gUSJ_WUrSVXIp-KDD6f6BePXNTuYKy64w7RbJWPt1Enoaq749iyBV_H8eggA7-MSlbsMeIjjO2uMqfCwtz4Mgu5ixW5gRWR6A353pnRj5TNwsPpSVFsQzT6GG2GOUEDro-Tr3kOlS8Q6fGslqdsB8F-91DgXKUcp4eFEYAnY3T9Ygj_6ONTEgCXU-ptaP4vTm7Er3EsgXQEGBJCN1Vq3colPr_7Y-tXodSDLmE-g6JB-D9mAxLHhpx4WM1d0Op9_-cVPcJTPGC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgWDkmKD6TXoY9uVB-8wKRotS-Hgz0looyMSpEhYSt3cSSOEyicx8zSpqTnn9wmql6wUTmMo-BF0NYHvfxQanuRQIE3O1JZ98_4ITjOkXjR8-Ro9mPEZGT73TKMz16CaELkNypIs5RoTRHLSQa6CIp-ObKPbKCVq3iMauu4SATiA8byXCI7aXydiaj09hYB3mE1xg3v4-LA-QMpq3enc9BAwiuGIcrxlsTX44e-miKG33RkcJzlwCFXA--ficxqq4fTBL27g9mfzpz1QbkqZwk8fXjnU2UHz5nsMWDn5SUo7P5RU-yy4DA1PC1V-L-Kke10visrrIbn6LS8MJTuJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=O2a5l3VSwdzR6Y2PAZl-1Qwt-B4hOyp003FKXkDcH4Oo6DJUACQc4g2AUXr9yTlZFWqOXBgVfaMD7iAw652u4MpyqxnVU2FTBsZES1yt7eluS0lJj4F-4s9LCrzoWIxdc09mDg4VHTrAOlXz3y6Gxxo4t9FKv0PvQkPDfqfbzECRsWnS8nZZljzPC5bMbczb8tsXjgInrs7gVA8ti5x3stQJZoSE4zJJQJWBSQiGLVqjQKRvaOsj9SFRd-NSWuhLErT6lOQLZt4GrJ8R7qEyVq-DQb5lHc_V5U_AACrFnih5zvcXkblkpJwYMce0oIZL4YH6SXlYz95owIfLAfyaHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=O2a5l3VSwdzR6Y2PAZl-1Qwt-B4hOyp003FKXkDcH4Oo6DJUACQc4g2AUXr9yTlZFWqOXBgVfaMD7iAw652u4MpyqxnVU2FTBsZES1yt7eluS0lJj4F-4s9LCrzoWIxdc09mDg4VHTrAOlXz3y6Gxxo4t9FKv0PvQkPDfqfbzECRsWnS8nZZljzPC5bMbczb8tsXjgInrs7gVA8ti5x3stQJZoSE4zJJQJWBSQiGLVqjQKRvaOsj9SFRd-NSWuhLErT6lOQLZt4GrJ8R7qEyVq-DQb5lHc_V5U_AACrFnih5zvcXkblkpJwYMce0oIZL4YH6SXlYz95owIfLAfyaHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNDhksSvXvA7lK5E7OYBZHiDSP7JNttFFE_oh3LvniH73Fk9bidctwEov77MNlaXeL3ze_fLRagsXTOdhJgtQXSCy4RbePxoSI-smZC-2YN2MTTrKCf40I91XQoOWWJ4MGBGh9cFcw2Q8mWcEtVq4pXrZGN9B6tLhCpG5muJePtH60-ulppm3OQLoPLDHIDG1arRwe9OgbEUAlLLNLwoCyKTcTuEpXbU0dGYoZjsNrjNJ807zTWi8HtofeqNxdeBWEz_IxAnsmS81TWTF0azuD86zYyjf3Ch2kku35OEK9HD70M3nx3fzQFR92L2GxJg-7MR4MZ7MnVaKdl2FUjcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbA19h8MS0AmLDQBE5j4cttMQJdFejtR55NCorztA1gYvAyZqBUX3dJOe4siL9AeuUNEoDMylsVBRYid1zxeeOjn1TH6NvWFL59XMlZ-eZhubSXMovNMgHya6C0B_eLjMjuNsLI54ZKIlAd_arP2ZNmRBt1FOa-DvJMdAL5PpzuZeAz_yxgg9iGTwuCsKiv53jGbG9DA4CIq6jGDDffMXeTqOVYTYpjrjE2Llyz-K4oKDNNIZ1CUyezvtxgY079LJDp-yNzuy6KrIaBod_S9wyugBkOv1aEmIhD3tbHRro7kr03iFLi7CtS-Oog95QlXtXJRtKm9nTsMNRYC365DSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNuEMfYD_2Q4bThnghcUVsCrY_y--DD4JZncaGo0bFKimja8jy6dkjC1BiqeqYqwZQ1QWGM9SKpYKVMm6wtxlS3CN5WRGru3PoLtIl2TdRTmKwKlijESdsFpZpfA77BQvzpUzVjtq9ULzMhgFrL3-Z5a16binP1BQ39p2yhgPiv22S09mBeLPdNy_8C5u44TzcAKlZp_5Q5cQH3HDuA5u28lk2crTTh7BqHY9v3jplQJR-HLXHjt9jkxNCXsq-xAY-nfPBk4O-8xBYTBXnYzkSpWrArqOhKDJlREUwSIuEfW8eo-OxZ4aT7cXgK_6hl8cyvvfeiGNKGo4g5jtP0Y-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfH-CYonkIaBpOWoqMvHq-ZZ4fOS07NMr9FvfcdJ8S3ZREQJ01PmoPy3NQn3swMF-cIgf670tEEN-rS-6JM1FkiSpTQslGlbKvr4LpFQuaPpYo28VfOtF1a_NtOLnYlZZ_R6JyGLBkdsfAfY7lxlI-hcMR76OdSmsbT8UyTUAE1NwvTUxhgT83qQbaD8Bi7XCX_AGDUb72z9zd_aBBxMSrbKgjSVZrQyvGs3ytE-wPWJPWdrgYI5YsLy02Ej7HP3FXYtkxTdY6zRLLguUq7LKf1U2wZJf7FY8CSd04uapijuYM2oGqDi4MoDqtgIqVe_cKrvnj0kd8aaj5zNpx5jOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=TMwHuFZ5JSeKQnce-KARwB7zyRPX56wvR1Y7BeKmNmNBJ61IOsn0MzkhrWgzhpQnNohrAPv0C1flWchH-sFw4YnpUIz0cHdkV6Se8fI5VIznnwKonU-P8422kkKC1bttniWNViQyRyCnOg_aKLcDBZUw2VkkHBq_Vypkha8NrVWzZNUZKAmMaUbBWv2TFLap-6TYxzJWWYMiYIddr1wmMwjqi7ie5D02X7pwZDTlCXX3ponET0rNYScOrvpPw6ZQMYSD7yU7gxnNx7d7J7Gyf0zaP1hEPu9WD6sHfilFrO5ntr_gSVysHgODGTNl-WWgEoN5-Ti6wrEhH9Zv5Y9mDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=TMwHuFZ5JSeKQnce-KARwB7zyRPX56wvR1Y7BeKmNmNBJ61IOsn0MzkhrWgzhpQnNohrAPv0C1flWchH-sFw4YnpUIz0cHdkV6Se8fI5VIznnwKonU-P8422kkKC1bttniWNViQyRyCnOg_aKLcDBZUw2VkkHBq_Vypkha8NrVWzZNUZKAmMaUbBWv2TFLap-6TYxzJWWYMiYIddr1wmMwjqi7ie5D02X7pwZDTlCXX3ponET0rNYScOrvpPw6ZQMYSD7yU7gxnNx7d7J7Gyf0zaP1hEPu9WD6sHfilFrO5ntr_gSVysHgODGTNl-WWgEoN5-Ti6wrEhH9Zv5Y9mDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8Mjv8ugV9HVF-qriScT8CeTQiD3cl7pSFA8t3eZQSbr303vXqUU167sgFzDr4ANWNW-V_XKcAhWH50j6eqnxK3vZat7uEy6KopQGN0BgAwo-N-yauovncwQHmHga0hiRvuPk-t58nPbHUi1VKg_Bxw6b0RIqrj_cL4DywSoN0MCBpf4XCFMp_QltUVAimClf-5LlxJhWTaZtD0VH_2QL6ce2hEn5t9ekEXKfqe9xlxdcUmOSkQdXsSTdOJOPpv2APvJjTP5LcqD9PGiejh5xneJ39TF4ObXqjtnNC4hLRLjurg9oMtaYi7XNYlSPug1uPxZJMDdspz63scXCWMYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKH4gLwcUPCOFaJdAydr6nd-7PQpztXAsen4Jz7_HjQe0m4kHpT2hPfEzE2prrZa9zCjWDSkTODxYOJkKNVQbtQFN-ABPSWDI-DWnEvGG9yI9lqE1kc7QI8DPg8DI3fQP72Bvvk9es1TCp_JKGChQytGzJ7_wfRe8hSftSSkrwy1HAeDlwJGqNb-3HOr-QEXxHPRTw_LSqnP5o_s5cO5TtG_9MhWBH5sKnaW8OJjZM9iCUTKwcrLw-7Q9FcrlsQ99nltSs5EXcIB29fV1mMossPNbV1z2nimzkx5azHKbzC5b7YqfnfMV4rZ1JbJgZQEBwk1kwG8mmr0xDq9aT5wI-Zs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKH4gLwcUPCOFaJdAydr6nd-7PQpztXAsen4Jz7_HjQe0m4kHpT2hPfEzE2prrZa9zCjWDSkTODxYOJkKNVQbtQFN-ABPSWDI-DWnEvGG9yI9lqE1kc7QI8DPg8DI3fQP72Bvvk9es1TCp_JKGChQytGzJ7_wfRe8hSftSSkrwy1HAeDlwJGqNb-3HOr-QEXxHPRTw_LSqnP5o_s5cO5TtG_9MhWBH5sKnaW8OJjZM9iCUTKwcrLw-7Q9FcrlsQ99nltSs5EXcIB29fV1mMossPNbV1z2nimzkx5azHKbzC5b7YqfnfMV4rZ1JbJgZQEBwk1kwG8mmr0xDq9aT5wI-Zs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qImWAoCAB5PeRFSyaX_BlMGYWlpchQmEY6B1qKU73ldBxpdhAAwc63t11Xf-HfkJBiZPRN0sfaAkZbEgi8uto-H2dknqGTh-i0XoSCVOdFv6VuwnxMlcXxm5Aty1dXuWfZUdTuVzelMmbgPxIR1BRO5JeXHM3nMLyauabvFbfP46RgQkSPc2XNpnAsrfyvcLR3y5v2yerkE6AV0syyf3VIgUZrFippOqj9XI6mbBnsfzUJZMYjjHqxHVbmaaN0PdPomClt93JHyguz5PjQTM3YUHtrjbv00-tPdRpSFHOmzOTf9AcIeh6_TVTcQSco5jBg6jQvFacmLtuprp0UEZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLJswYOgBx26tCaa6Cg9sYhXyQXdadEuoWg3BWXJ472Ze4FPY5hH3ZCgK0QoTjueOhyvatpK5mib7Gfn_vroNgvSY7xWab59D-eG0M2pJGxPx94hUAhvOVlbpCN-x8K7MlzWXL7B6GaURV1rhdeIqpvNdepcug_JTsiMkiuHltZTKVpjcPw_cO4QjUsNy_TszQWuXVQwenk7T3gdoabekeIPuekHhDG_NMKTmWDYg3ZvlLVOkc-z2ryJ9tImMj2Wv3iBCYiyGTpLnsVUwjpEkabmmASx3VKnHUPIYfzk8oAwCNv3LvtblGIcSqFKKo9BoQXGF_wSEwVLnXUvDpPV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=uysZQl24U2b_cAdhJWjTzAoACcXuUH3vpjAi1n8_WYDae1g-3R5M9yRxc_MbBFo7YPmIOXz0wbgb2K6gWiKImliNd7aQvu4oy32u4OE1xapqiXY0PiAS_MKtp3CHYJJqIwNm9DzpscInpvVgOm8_tD-N_3ZJXBxkllwcpyOzsUxFrzBHz1clwNCwqchEGfHs87jR6p-PXmGJvl_Ho9AvJbAyTXYfCMKljIsVa2jCaRM3wJNCqKaCGtNeqElndMGiuXMPxh2ZMJM59H5FOx-RxUYmsU-YM7uPe4D-zzqRlYVmQM06SbVsN2ef8kj6w-OYfSr3ABdZ02ist39O2XTaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=uysZQl24U2b_cAdhJWjTzAoACcXuUH3vpjAi1n8_WYDae1g-3R5M9yRxc_MbBFo7YPmIOXz0wbgb2K6gWiKImliNd7aQvu4oy32u4OE1xapqiXY0PiAS_MKtp3CHYJJqIwNm9DzpscInpvVgOm8_tD-N_3ZJXBxkllwcpyOzsUxFrzBHz1clwNCwqchEGfHs87jR6p-PXmGJvl_Ho9AvJbAyTXYfCMKljIsVa2jCaRM3wJNCqKaCGtNeqElndMGiuXMPxh2ZMJM59H5FOx-RxUYmsU-YM7uPe4D-zzqRlYVmQM06SbVsN2ef8kj6w-OYfSr3ABdZ02ist39O2XTaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=q78InhFl_Yxiytr_6Ejy35x-3AGblQixH5UlYPl87nIRwtmYDe8GjUwy9CiGNCxc7d5NyMvNqHQPmg-_WjFp-LI5YEXJDxnE2YkZHrnNXKYJmXvW_TxB5EPh6X32fWo_Z1BtQ7df-1GSiikN5BHdhXEfBoRIKfk4f2v5QyAffCV8dy41j8jOWNIynVatRwQVeD7w6eDFl93DuxQ94ihBTlKIMUmzxu5oru_CeOdsyFtFcRPPbCjeY2_E0HfbdQELNzz_IlfnCIrfpN-og4tdCUNGTMikEX5FiW3766DHl1feAJbShtM-DtLNUXwVV47xJjjs1hlS0ngQCjzo47L37oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=q78InhFl_Yxiytr_6Ejy35x-3AGblQixH5UlYPl87nIRwtmYDe8GjUwy9CiGNCxc7d5NyMvNqHQPmg-_WjFp-LI5YEXJDxnE2YkZHrnNXKYJmXvW_TxB5EPh6X32fWo_Z1BtQ7df-1GSiikN5BHdhXEfBoRIKfk4f2v5QyAffCV8dy41j8jOWNIynVatRwQVeD7w6eDFl93DuxQ94ihBTlKIMUmzxu5oru_CeOdsyFtFcRPPbCjeY2_E0HfbdQELNzz_IlfnCIrfpN-og4tdCUNGTMikEX5FiW3766DHl1feAJbShtM-DtLNUXwVV47xJjjs1hlS0ngQCjzo47L37oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=br43qaaHRPXzPk_7jtwA_LrTot7ThQIAFJrDZHWi-1j0btFWUkMIzGxwXnZAsaTSOgxjPiXIs-2-fjlpssoqruz4RdNMTCXHCQquPhk5XiUtxLHO0GmZ4Lf_jLTX3JrIQwCRRPdC400J6fNuHZSHK3V1SS8_AlyKw-1TSvU77qPFVPR04dXU1Q2sPMPTsxiugnHxwglwF5yEVZPQKM0YunspoGQ-vrDM5rhp8LWXRsHzK-nM27Teg86Ib25zhfeXV6lvJF0vXgfu-O7PHNyi1ihDCKybBuJSDWoUHO4zOY2IKhdA-SMidL0nUiuvcHcWPaAISJLoh081qOek-m3b5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=br43qaaHRPXzPk_7jtwA_LrTot7ThQIAFJrDZHWi-1j0btFWUkMIzGxwXnZAsaTSOgxjPiXIs-2-fjlpssoqruz4RdNMTCXHCQquPhk5XiUtxLHO0GmZ4Lf_jLTX3JrIQwCRRPdC400J6fNuHZSHK3V1SS8_AlyKw-1TSvU77qPFVPR04dXU1Q2sPMPTsxiugnHxwglwF5yEVZPQKM0YunspoGQ-vrDM5rhp8LWXRsHzK-nM27Teg86Ib25zhfeXV6lvJF0vXgfu-O7PHNyi1ihDCKybBuJSDWoUHO4zOY2IKhdA-SMidL0nUiuvcHcWPaAISJLoh081qOek-m3b5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgLDdfaiz_Qko6yfF0vZ2dkk3CgFWcK-GVenTZoTUSIrqNRY-f97YF2pGM9siPxZjO1QbRJdrd8-OD2FvR-Y6QcSfCpBOxlpS-4DiM-32YyfGu_YZ-0_ZRHuM54ctur6-wLSHnmuIfe3HmdFI9NqHZvgfyqfDeIRR5Fqsor1MP8aJjZ0CRwFZ4dThO1agF3NGb95vWPQy_2kKpKmpHx4r4j0877JgAq_lQfT4BdewvT5Ftvko63ZljtnCOrwS6vqkr6VKvzLOmVLVXJvTx6m18WkwJIvnCW0uSB1QijXA9FCnSkIIRK1Zk-2D0Wt5UyW4TBfyP4OFeui_m60FsT3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAU4Ub8E13GzQgByyqs7FVztPsbCTPxDxHaIlIgATfwruh2-tgn8Vdo3RBbgyKsTVYJ2yIUyPBWoPCfK_Dk2q9toqrgh99KEgXPmFoRoXKdb5m38lUtU28u5QUiFQ6t2hJ-PJsbFl_cQTi3sTOY3LklQNYiOALDhpdKnV5hF6fnuyC9FMqfDOG_rldy5knl-TxTe7Up4YhHrvbS499nT2KhViH28pAbT4KM4aZoeR8Q-CYL0Uil5krQ4qzJwh63cf71GUJQTf3fDx8JVSgVJ_-9AsNy_v8aTaLBM2gJo3MzS0jwJJr5Fc9wgCc9UUr_tpbmNZ4UNU0wDmX5ZoLuV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVBwgtK22ofthD8VvFZTifvXQBqyqyKgLkTntmatv-2luapAYMnSKKwtelSHQWQaYbwlEpyBcXG8257NX5buCNjb-lTdIxVFuzKL3dj7unNMw1YjBpzX7_IHfqAv60LswxFRTE0Ks1PJpoiqVgU8-h10Ub7LrJt1-nwIupqpYBSGkBLo9az6TQ3-2l3uiky80CsKfCRzdog0Tj5mr6_lF4SRQIaU7zDduNH376dvu9ohgrhaZSoa6oY4AjDQvS0tqZwnCa7gTeMPaawGKm7QHjmdQ4YmjwCDTRXiTGuNI9S-uws8amZcXv7r39qljL-k7AE10l7sBkT2sbdUtF2-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERekesFOBuDkQQr3ZffmqWs3nOqP_T0rcG8SXxYPv1YPgRdHerv2N6Bp0quReh2jvxNzh6lCOh_uU5ddSzUL0F4SPTEvB_t5rUXI3omfzZ4Nyc6CZd-WyzWmw5d9k7895gfkkFKYQgtUCCeNqsRKZenmK7XazUuQ2o4zW29EvTGbnQvXrFE3I1d61GNAecyPmc9HQjdqvu9i7hynyYQWB10fgOW1H1nW6ChnPKCoKj9yDX0V9BkMrNXTCzJ0394mUgRZ_PCrChk3jBTuMOzL0enkgkDT8AWNUc7EtOap_oAU4qz0leRUMb4SWtRw5VTlB5LbZAu6jY71kQRxpIHdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=p8eIoqec5ITy96EOcOYY3xlWQwxiAKoH4vfmLdrFSKXW70UoUKuUXhQz_PFM4PvCvJGWhFq-ydeSO601M22xHhZuUMsaG4kmmjZUmoMn2F1zN3sbD1Ey-fkkBHcwDj1W31SfwwLmWgTy6aaAAw_426Q1rAjYQrI8d9Ftq6bCdD-kbuwB49npl6_hmJkaeGIA9bGcpoPOgCbldKVD1CHgPdt27zahT4dp0AT6qx8LBiPCkK936_9Xrp-yautuqYWVlqlHmou8OJrm3B0MUY8_goFhUdRhkTQ1FFLoUVa9NyfVAkCFSHnNZqGup9-BNmLuGCYx3RIuasjmBIetKIC0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=p8eIoqec5ITy96EOcOYY3xlWQwxiAKoH4vfmLdrFSKXW70UoUKuUXhQz_PFM4PvCvJGWhFq-ydeSO601M22xHhZuUMsaG4kmmjZUmoMn2F1zN3sbD1Ey-fkkBHcwDj1W31SfwwLmWgTy6aaAAw_426Q1rAjYQrI8d9Ftq6bCdD-kbuwB49npl6_hmJkaeGIA9bGcpoPOgCbldKVD1CHgPdt27zahT4dp0AT6qx8LBiPCkK936_9Xrp-yautuqYWVlqlHmou8OJrm3B0MUY8_goFhUdRhkTQ1FFLoUVa9NyfVAkCFSHnNZqGup9-BNmLuGCYx3RIuasjmBIetKIC0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe7ocaHmAO9j28j42sa9RhMP59kOnkJxQLY11I7n4NBOXcOCoSMqa5J75BzOs-Tl2BIaVUeinPEs2mtR_KO6nrg9yI408Ktarj1WdAThBaSZrAaikt2Mxs7_kw5uX5GwC-odrYT8uohfHbqQ64O2x_e7wlxmUykSMqpAs0nLOArxDx3QOve01e0uBsH57kd2qiIONtmoPLLJQSX54KA29SV8LOzOzOM8Pl4ZBQO1hA2Gnss-a7hP4XQ5s5SeNrNl8qqobLFFadZ0kMftNlVATJMfTMEWeOJc8hzszauuGUJvmXqpIaU-QpJeJ2MTPk3rugxmvK8SXN6e2WavtYp3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aImSxeIYn0ECgITyiy_oY-94maPK4CgBdcyQrQ788MVJ5LLrccdqxeTnB5ntgTctyzqdlfH_0SlHwq8vpgQho2_UNPwicOndkoXXuy56u1jKuvmcSru_k3BvZyxvOfoOU5no56br6bevYN32DKxslh4A2ipKMY_JKiLKQNGy_5ddAdq88loDwLn_92hP63ab8Y7NfdBap0pcGHWJaCxOvQ04EyvGxrAXBuLGPzC9ACT4n3sU1pQdzI1xEc5LFBWBuMFPXqf47q7aZ4af-4nf-iIHzc0RgKOqlKlfiWnDveCDqdnSPx0stT_JET5xTyN0oUuu97Z8mMJ3e33AtPskgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=XfxppksOY8oS_-K15-jWMT30GfCjUbeg12CJFLeglokZMSueLjZllWRluSzzlyc_MqCXvXnSI8l_6bUFZrX6oTl5OvvNq-DZseL_qz_5vbzHrKkcBq5Nhl6ArciPRpJkZdaYyV_eHoXeOsccn0auU7Cvu4dbbdi-DWHJLa4Ld9Lc4DwI1cQWxVSGRhoZq1wBd0bjOvKZLv2urqYFzHEY-spGUCDHGLN1lnMc2AepGBATXx7Gvz1iaPurQKXo0q07vII1LI6hCGWUyfOwD0-pOA_U__LZDOobXAzDOMp6YYc6CGS6KWUY0QSJJTYvXFglf38qM0gB0zWDuVYzc2U0-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=XfxppksOY8oS_-K15-jWMT30GfCjUbeg12CJFLeglokZMSueLjZllWRluSzzlyc_MqCXvXnSI8l_6bUFZrX6oTl5OvvNq-DZseL_qz_5vbzHrKkcBq5Nhl6ArciPRpJkZdaYyV_eHoXeOsccn0auU7Cvu4dbbdi-DWHJLa4Ld9Lc4DwI1cQWxVSGRhoZq1wBd0bjOvKZLv2urqYFzHEY-spGUCDHGLN1lnMc2AepGBATXx7Gvz1iaPurQKXo0q07vII1LI6hCGWUyfOwD0-pOA_U__LZDOobXAzDOMp6YYc6CGS6KWUY0QSJJTYvXFglf38qM0gB0zWDuVYzc2U0-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4sH0uyJ_xrK6_CckcWbluk0FaVqalnOqIoDfImXArFM40KbWJtYPTKLOuQcVjnTFAXR0wGzphEdHJZJQibYeayhEl7v330CwSILw_kitHhDUvR9fDwxXr1obTiWxYK26FvFuAzpc-Dn1J3OjtuAUkq-h--yf25W0TVrehBTx6Dkh8h3iH63B0jn4Ur85fySqubM-TcQJKvUcX-PGIHBnyK0t9swFdUGj0M_fxq0-MukCqM2R02A16XfMEn88MY-Z2orEUzEGV3ND_VVH5Ed-4wdQvUmXhhQ0MOeCtdCap3uVk3f8cvk2pHToYuuBIOGsusCaUS_mo0xm5KUBx45cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
