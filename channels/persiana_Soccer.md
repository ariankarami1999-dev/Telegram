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
<img src="https://cdn4.telesco.pe/file/l2F25VWpSXTZAfmFUCSH5fyE2H9lvUDXTki1qNafgRmMwv7SYpN7V6kpB-eJr4J0enl-j4OPLYJxtPeFAGoiSnVE1ohbNBrfO2_7hqq7KIveY_g_MOmfb_Vl7e0FDdvIzG_ir3emmeAhGQnm3ZrtHA6PlgKDQ6eI_6YVSweJidtiMPePwHFlrtRIfd0XMDIJgZAQN3lzuv2pzRAynsz-kQV-aFwRvj4FOgfmgKlS7zN30jVw2QkKg-iPwalNNStOhJ2mnM9pjpuDo5S_MRuZNdDJs6vjUS_gOzwRs-vLhjdbfqoWOzOTob8IjJqqODac0g07xl_SwH2FmYvWNb4N9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 306K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkDVtjo9C8-Nfvo1XyNaa-lLqUMBHoO1v7Df_dTDPjKZJtJtugwmDd5gDsL9p79vt6XsqrK9LhXFm4A84kvpUm9e1e1etO_JzuTpQ-ILmNHDgpq8KlLm0ALlB3Yn3RHThV1HQn4dX7vSXF-9dplIznpSsBQZRn4FZnzY6OdFxUgHpXKigU_HEu8lg7CMSwzTgl2Yd1h5BuU5LmrhuwhKvs0aVHUKZ0byGao9MNCReHIAa8JtuwpBNoT6UN28RrxgdAtE8VinIB5EfOaJ71AI5ocm1JoQ1a4kUqxzhTXFYLNnhR05XiTb7l0xYGJ8wLmH-kPCoR9emPOF2WSNmelzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=Lu8DGiAi_n-dGXBcM8Vhz3rlhTCZKudJEX9HRCX5RHP1lH7OVGj1eSetcMF1a1J7QpyoxVkhol0FoMfmv6CSU8ljpMhT67N9xCawAfzhEp-7KyZ8jDDF3wgujPRbt4LFVK1R4BUEjUufLf0Dc3YEkGOX6CUbd6XKyW8bm6Y6ziGAi3UzOrZ6HG4l5AkyjvqQznlLL6dr1zNezxPtAgiVZBIxRYQvI1ooicqpwRM29FxkO1tBoR1-PDpCS69rMIvJmUjopq_iDmOx8Iq2a046CIMODK889IVgicVp5lvhhrHdcRd9yIyvJhiNL67l8_OsBbrVRcTXFPhiBV68QJ6heQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=Lu8DGiAi_n-dGXBcM8Vhz3rlhTCZKudJEX9HRCX5RHP1lH7OVGj1eSetcMF1a1J7QpyoxVkhol0FoMfmv6CSU8ljpMhT67N9xCawAfzhEp-7KyZ8jDDF3wgujPRbt4LFVK1R4BUEjUufLf0Dc3YEkGOX6CUbd6XKyW8bm6Y6ziGAi3UzOrZ6HG4l5AkyjvqQznlLL6dr1zNezxPtAgiVZBIxRYQvI1ooicqpwRM29FxkO1tBoR1-PDpCS69rMIvJmUjopq_iDmOx8Iq2a046CIMODK889IVgicVp5lvhhrHdcRd9yIyvJhiNL67l8_OsBbrVRcTXFPhiBV68QJ6heQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHb5t-6VV4WcGaCLuUx5GO_N977Q3fjlIgkg3gK2PNYlTaiEfVdMnF4wNuPk0A_GJc6y_EVxL4Xn7_fyckAYyju5ayoQApr5om8nB1Oj5F_SHdXvFh-LigGla2XWBybo9SUTSWvAylKEPtozjVnRrFcwJ62rwyOSTCjZj4XZAxqvzcSKgAeLpK6HhWL2vrqJmqCMoP41_mZQcyHjjQxUuLL1E_3SATJ_U6RHxEDPPsTnSQWBowUcxWeFicvjxGzag9XsfabDbEJCkXx4pDVnkVNpScBV0QRwi4Rzc9V5ymspdpaP0rmqruic4ryApJfETw7ztb2B9Xz79uznt-yUnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=rhCf8RtOT6XzGvxpE2i4fGaOahgxwYCTh0EdM9Yh_JbloCSwJwczDIDHjt33Gijj6KqLZblOsOvVwghU8WB6lc_RTjX7sPw5crbpTc6e6ni8pT89wIQSMz8vHl1WwgzVUHzFrz8WIEIvBw_YGxlL13YUiahux7drKfzUsP2EiymqjYU8gdoBjZOZ7B8fR66gmkCao1s3ugjYfUHa0GuMQF888hBnJd7jVHVklOa3bzjh3Gi6NVfeIjaCHef0I7MbaZPBv-8uWEvJ7N2aB1XyMp7dMZ_BkrtuUGqz5U8xhbg4cVAYr321BXVG2dAVXX_7B9-Ef9eAFCl2_FgJlFKWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=rhCf8RtOT6XzGvxpE2i4fGaOahgxwYCTh0EdM9Yh_JbloCSwJwczDIDHjt33Gijj6KqLZblOsOvVwghU8WB6lc_RTjX7sPw5crbpTc6e6ni8pT89wIQSMz8vHl1WwgzVUHzFrz8WIEIvBw_YGxlL13YUiahux7drKfzUsP2EiymqjYU8gdoBjZOZ7B8fR66gmkCao1s3ugjYfUHa0GuMQF888hBnJd7jVHVklOa3bzjh3Gi6NVfeIjaCHef0I7MbaZPBv-8uWEvJ7N2aB1XyMp7dMZ_BkrtuUGqz5U8xhbg4cVAYr321BXVG2dAVXX_7B9-Ef9eAFCl2_FgJlFKWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=fGewFTEih3xe2lm83X5wfQgR6tND1YiJ78eiqK0brADKp_RNcE-tcBlNhbAouClol0lCt3Bwwldm9BnLr87_61Vvc3H4N2cqtuu3ysbAGIqPQtsj4qYEJYqpTN8t1OmcoR8mdFbJAeWSWHzTNN9_WAd19p1zWYx9tZo0DFQoGNZPikdT8Oulon2rN3OUzB5dp-PNQMzFRKze35YtcbNjmT6IeU1pp6ujboyqvwHylwkO4yj6P9X-eehXFB9pjPkoKBGs1rNx9UDJcdGnXWXUkr3ZLsFuQwT-VHNdyBPftpzGl7Mf_6wCQKv7qKufnmZjLk0-IMIeHRXDXZEz7YudEYCzagf-Vdx5L9FJ2N6PuEISEWgHD1bgdgphDZa2Ej-gngZPpnw6-TiE651T6mfJHZWa09VWNhgu4Kgg6IgBF3tT0-l9j-mc7KwSzdkqSLHWrsz1ZljOpMCtk4SwZey9EpuKrkOe_Dv3FJcwQiXeBtQeZ98zcJWICwPWP83PdX1qm6NDGvfxHH_dvaOmEtdVp9-_kJQb3gxi5w3f6aBzrb8vjL3BrdKuSCz_omj0Bi3f_wdphzwYyG5i3xP4H3Xy4UJxt3aeVisFz_eCGood0VA9H24neq9nnAufkEURzXW2Wx8iNreX5Ax49tX9dlsh0Gr4-33GRN1uDQH_yj2Djjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=fGewFTEih3xe2lm83X5wfQgR6tND1YiJ78eiqK0brADKp_RNcE-tcBlNhbAouClol0lCt3Bwwldm9BnLr87_61Vvc3H4N2cqtuu3ysbAGIqPQtsj4qYEJYqpTN8t1OmcoR8mdFbJAeWSWHzTNN9_WAd19p1zWYx9tZo0DFQoGNZPikdT8Oulon2rN3OUzB5dp-PNQMzFRKze35YtcbNjmT6IeU1pp6ujboyqvwHylwkO4yj6P9X-eehXFB9pjPkoKBGs1rNx9UDJcdGnXWXUkr3ZLsFuQwT-VHNdyBPftpzGl7Mf_6wCQKv7qKufnmZjLk0-IMIeHRXDXZEz7YudEYCzagf-Vdx5L9FJ2N6PuEISEWgHD1bgdgphDZa2Ej-gngZPpnw6-TiE651T6mfJHZWa09VWNhgu4Kgg6IgBF3tT0-l9j-mc7KwSzdkqSLHWrsz1ZljOpMCtk4SwZey9EpuKrkOe_Dv3FJcwQiXeBtQeZ98zcJWICwPWP83PdX1qm6NDGvfxHH_dvaOmEtdVp9-_kJQb3gxi5w3f6aBzrb8vjL3BrdKuSCz_omj0Bi3f_wdphzwYyG5i3xP4H3Xy4UJxt3aeVisFz_eCGood0VA9H24neq9nnAufkEURzXW2Wx8iNreX5Ax49tX9dlsh0Gr4-33GRN1uDQH_yj2Djjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vQvSn5b758J3-H5O077WT1Cz4gEZovSeqSIKIKr5w8UQrvRJAiXZUmQVgmA3twVxiMNB90C2wk0U8xZ-5fYBptSdNarmVhs1mvKsWlGiE2DULz4-SF1aUjWe01ykH5Vg-U0Yp9x2HQ9BhB2EzlJ9ANUmBfaGIAlNL-ygr6H69ObRm8yn3mNwIVP7S141_zIQRNgUTSiQU0D_WU61MKmeCl3vkpNAZSd7VZ7_M3st8PXdh7IVx3ul1KIDhd9raztS96iZOBEQN4xHEewLt7dh9jb5cmbYBSFfMFp9vWCAmPMzYs_sn1EsdhSUsRlZUjc_Px-J3ycJfpj1nCGojox9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vQvSn5b758J3-H5O077WT1Cz4gEZovSeqSIKIKr5w8UQrvRJAiXZUmQVgmA3twVxiMNB90C2wk0U8xZ-5fYBptSdNarmVhs1mvKsWlGiE2DULz4-SF1aUjWe01ykH5Vg-U0Yp9x2HQ9BhB2EzlJ9ANUmBfaGIAlNL-ygr6H69ObRm8yn3mNwIVP7S141_zIQRNgUTSiQU0D_WU61MKmeCl3vkpNAZSd7VZ7_M3st8PXdh7IVx3ul1KIDhd9raztS96iZOBEQN4xHEewLt7dh9jb5cmbYBSFfMFp9vWCAmPMzYs_sn1EsdhSUsRlZUjc_Px-J3ycJfpj1nCGojox9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx-yHtzyU0118UlELMNjPu4BdHndZULQWcwSwLfq_LKfWlfJ33HTozyG_DHFzvOT4LhkuYj8RRTef0zdHJg8FoPCTFqSF1xwxjOBa5i8CW_SWQt_5wzN812vKh70TfQZV0Elzv3qd9Fjc63UgS5ZdqEUzJcSojAa4MNiUJNh34BEA65B5CPhr1nu8atMuwYgwYr9lA9PGud0xD6v1u8vWX7bG2FbOUY05kEVy1ZBN0LBWzGH-3UDW8Vhu-0_zDrsdUr70X_vgDkm-M1KhFBjknF4XgSJvJ53CCIlM0b08Gl21g6ppp-iiom3Y-qQ19CK4K6jZMuu0df9BCAmhC5WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqv1izsHNzgvRbTSWR_sTuHYsMnQYNfJEFMRr6fYPUS_r-FfPD3sVOdaBCor1ItShdxF2M18D16zvYggKcdSZ7vDCZE4sl9cEV_U6Gb6xpBs8wyhqWG7uZzYPzB9WgtkqQ0NFYXTToKFPXqy_6TRqvnq7_I2K8Md5gO2XXVARdXBvvI91XVkOcnVh6syvTJRV6WVU1PS_arNdu4hiDEJ5dd3vavfA8T51SpVfykgNA5sP7_Ih0umpXx40BTL8Kv4nGhGMvjVT712vD7dQhk4ejdqWHIuURBlLMI8fVm2Abmk--GQb7x5PUeQ-FnIsZ8baopVPhv1cDuoawj6ItZsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBfTSDUKFejB4cfDxaGDjV-a70XynB8Bm30ZofPKNHhE7aVY9Pbol-bUiOnRQV9n_j1DD4_LG8tPL7fwKRumjZz17f58pxxHttxC3i0XHOfZUjGAJk29Ro2EC4tLAtVuhufSYHVkZZbcvIllWSQuc6PrDX9jrmcq-l_ugCypxIwZMFJQMpm8CqJprE3rDWk9v6TSgw4kmzkN1NirbnQnVKcnH4MYVrFBq_v_pjkEBkCiEj7x61_YOHd0zZ6LOeIzaTmu_BNLE4y3wi092EzsV3XrydYBj2xXyQVBhyr1D5zqCpitfBF_SvhCovqhBEZNhFr9KC82Jfkn_DHlDWzv5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-JpyHRxjBd_unikAcuWk3STnXH5Ut8OOEC9eL6KedhPXpjN_94ucji67yQqiccS1g3F1BPRrNgrnhnZLCOUw62kYczFrUyvGhydzbE4Vk5HaPlvhpH1jNjbkxEuglzktxB6kPb2R4PNyK0PSiW444sUPeqnm6sAxTduYQwtjT2_gEIQRmkUD8Se1vuY_sfmx_MG2bZbm2J_g-qirpFAWw28gaMa65__3oLdC52cBnJ5gxJC1YTW3yaZo7kSdZHBKrBnoMINpNr2wDJJ-ps86NhxJxLeZZGuwophRjAe1cNR5RqkrdGVi00VfTMB7Ghcdcm_YRjHEa1eSIZIKw9RQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9xxwdHZNgh2vD5HHY0xgrfB7RNB95r_kYNy8uhBLaVEfZBJnEcx1UzNPxyoVKffFIXJGk6NQDqRsPyq8G30oTp8NN37I7McWi5QcY0bQ_BkqZaiWuRTD8SdELmJFJfB4orMkF41M6D-XciXTc2xxiaNxI2tnxNBT9owYghzJ6yoYkrnSY_kvJJ6ytI-5gtsk7SR4Z6T8F3fz0x4WbOHSaM80EKeHKWnh8eqveS0rWCnYg7HYDaqHpEt_h7GhDy_1jL_Mxmw39xqfcLuCGcMLIs2iOAarP5Ei4Ut-kEsgtRgcFsPxug6aR0FxhUIL05zPV2_jwIDrNCd5HWNNTvdTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXqvL41eJEl4VFYBDb9tRJ-Yr2AU-lyk8ICtZuBrrSNVHOeVolV5oonwCuutZFanOvg8bfEXFl2SaVi23OzqUyQ5LFov2FXxBFa4WQQFPqCBJLNHJIB3g4JhEEX5zCDhaqzcaMdb4mlQFQG-RORiddjbZuAxAw3RRc9tPEISQanGGCFbXDgAN7TCbpKILKDfhWILclWMtkSXw8EOleUG-wx0qZ1G4SwPtgmEf5cL_FNbSC39hTXXjz4y_tetuJdB5a1CTWYbkkQqZBrmYoYa2DWI8e5aX_Qgx2YUl0MZPC3ykI14CtBh8SjBVO3xKWNRWE78qY2DhFWWr7TLFF9ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=FJkCdf9vR1J7EYh5HUxLYbiYcJG7HYV2M5FexmDCr31hv9KoLJ2m5dnmL_C-8qSCJi9UpsHXn6vewzaEdF79rhk1Zbg3s2KGkWaQxuLXVpa7J0y_DxH0mLdGLX384sp67LwQCtHg9LwcgjZuWqXWCWZBcXQ5B11ZGlgn2MRLGUtdq8s5HOotwY4wTlxNSsD5gTHFH3p03LvVUKh0f_THtrqHOWbIGsHrpl95D_HAEeJF5G0L30ZXhHP0ZAHkd1JwA4EJgTzjslGr9J35OfPy0C0qCXfXevZq6LPJk6pmQeCuOg3Tkz7kZzpHw1uDMhbLbaiPCxL5KXWZkai4qGFr22zkyy3y5pqhtmZbxZxjmLCYi9qLDXEWCCQxwgUOe0cfdoyrQeaEk7vPjqK-ZzEdSqLhHvj2ZvJS58YgH4cgpuiKC4umRM4bBs1S3qVyVcxiIwdcVBcqtbxtJ_Yu6IDd9HphfW_NtH1gc5zMT15qZeMkDlaTW4mZnRkjUi3MuLUt3zMejamOeohvzWImhGDsl4VxRYs0JsV4Uh0iCu5GrZdo0JMC-rmNmpy2AqWw2Tnh2uv7X3XatOI4xQTIoP-egoXhvgan6QGsiIMCQ8lf81WRlKqv1wzDrUd7ZO5r5HMsX58nXV1JxwaL_DPzgudQLZYVDYdu3DHGZz1EDo4VrdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=FJkCdf9vR1J7EYh5HUxLYbiYcJG7HYV2M5FexmDCr31hv9KoLJ2m5dnmL_C-8qSCJi9UpsHXn6vewzaEdF79rhk1Zbg3s2KGkWaQxuLXVpa7J0y_DxH0mLdGLX384sp67LwQCtHg9LwcgjZuWqXWCWZBcXQ5B11ZGlgn2MRLGUtdq8s5HOotwY4wTlxNSsD5gTHFH3p03LvVUKh0f_THtrqHOWbIGsHrpl95D_HAEeJF5G0L30ZXhHP0ZAHkd1JwA4EJgTzjslGr9J35OfPy0C0qCXfXevZq6LPJk6pmQeCuOg3Tkz7kZzpHw1uDMhbLbaiPCxL5KXWZkai4qGFr22zkyy3y5pqhtmZbxZxjmLCYi9qLDXEWCCQxwgUOe0cfdoyrQeaEk7vPjqK-ZzEdSqLhHvj2ZvJS58YgH4cgpuiKC4umRM4bBs1S3qVyVcxiIwdcVBcqtbxtJ_Yu6IDd9HphfW_NtH1gc5zMT15qZeMkDlaTW4mZnRkjUi3MuLUt3zMejamOeohvzWImhGDsl4VxRYs0JsV4Uh0iCu5GrZdo0JMC-rmNmpy2AqWw2Tnh2uv7X3XatOI4xQTIoP-egoXhvgan6QGsiIMCQ8lf81WRlKqv1wzDrUd7ZO5r5HMsX58nXV1JxwaL_DPzgudQLZYVDYdu3DHGZz1EDo4VrdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzfgXG7pIeG7CRZr6bJuUlubsnLEEIyqrJ7Ex6tgpCxOTq3qRl7otHHAjhJrHU3MoVB5d0w2aXDLPbhYaXOKpmNWZ9Qvym96hKTQywJa44LBbVCewRPjA-UYrlnyvuaFbJx8CtVKXE-Sr3hOHq6L_MJLSH45j9C74VgV2TqnoFCL8tUo14Ear39vzxnz9FCdyZ4hB4KlRin0xeHKzNr290u77X7IL4J3pm1wSzD7-rvw7pzCKNtXNHco1O4FHg77v6y1lf1hzIIH7oz4a1MRi3lc70lluUD5df7lQO1zidyP7rXRyJF1WIe3zegCmMPBC7VRddoE80MGwwTl1JNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI0Jt5mpFjmax_shUM2-iJiOIXw_Bg14kOp8BritiJT4cmrorig5ZuG2gA5PpycaJuPhK542r_QcHd4AhIOzUvP9MSWayrnALxjttiL5_hRGoUzWpw5lQLT5AvigFL7hPOcWIy6dFbnnC1JGZS0n0hqeUv6NYQlNxijLnyD_5vR6Y9Qb6HaRQCeNWiz90YVmSYnky8kwBCJWs9MAWFXVMMyLhKtnoThieXKYmtq31U61CueaKNd_wnU-zQxsOBEwVzFwXB0_tFJV27SDqntIdXfa_O7O8WA9_x5TsmzOFr3PmC1XN2cSeG1iV-NM3q6m_rdE0_3h_PA290ugbbg-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXZ3sT3FICq0G3Newx-P5MthINY0wVcaRb6SzcI5tBep2U5xYjwSovmQk2ydyWexvpZvjA-X-aVmBfyf22O6tBBi071jz3Weuqr66-WQbthjf6EueooAk7cutn3sEii3F4mdvjdMLdsYn61Q0p1jfqA5yqsD7COBTNrDJ8Y02jszhSKXJDxfu820nXXJQBwxLM9d16j29Ggiu-1Aac130UwPbvm03hezWxsFvcsx2Hb34w2vID_MYy8EexFjYXwxQ6RrvxENzr1E3yTWMe5IJkIscwKno4BAMjlagbZBvkCpi_q5tRK3C8DUBXPpYRwISNMsDwA21c7dOZUsXiYQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHW6PIZNcudZZcUufhRNdheYNly8avOpDYvsV8n9WSpjxy1xfuS82yviCoIomcJAOtt_60nsQLPyk_1ifM95cGFliXwm0xAEylB0QMWlvtH2eoQdE5frWSSEaVcL_DNMJi3I7zhq8zMze7z1hQ0nKTst7VJhZzo9ZguGTu3hCVVdeZZJ9PeBD2kLOx_wTl6YDP10xqCAsgUywWQjJVlWk14tW6WS6jJcOTg4PFIaXv6ks3cNzjHNLPcFBwR_IP6ssg6gYwJMmhAiMvUwHWJ7zowpf9-A-aJTJd4hh28c8-JNiaOPTOAKXajfZadjjPkPavQnpXFBac_TI3iezoi-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9cbDQb4NpTY3KHJRYwEfrRFqHlrRQ097hs_q0L8QQ75QFYCyI5O8vFUYIaDac8QcTTbFwPI-b8U9rF4LRlLbvvIfOXi8UTF-PPV882GWan7OQzPQDb8-aPgkL1iZYvcAkbXcE75aaQdg4F_MaGxQ18Y5W7rUOqZ4y65j-UMcO6yiX9UFXS3Xm7kJfI2RRQKr1nfWeyWq_mypCTE9X2nJYC1N2tmyGEsuNjL3eJjqolYnhr4RCpFY710XM-9vK9RnMdkZs0tRGXo4K61b9I06b_EUXrbBm5ynOJUq_DNUJXehoEjmNQy2LzuulAxzEtbPltM4vT5-iW0_sc-7yuynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq_JXP3SjWHLJU1H-kk1OkLZwQEd_iT7uKvMZEER17kxvI_JN0uOt-R_gGddsHO4OqOy4-Q1hWIGlsLFaiBCTwlwHubEbwK25FAKorL8UOCc70fl1WWJwPCUi8qRiVoDqyacEdIv5RA8imp3BE3BYA3-lcvDjToAAgZGLK005U-fSVxDYVbHR2We6Eg3l9gCv6N11ggT8XUiTyf9J98Gtymlmvf4NwRvJcm1DvaJ1t97oapbuTwpUqtetf8STQcFY-7D0b7yO7Igh-25TxU1TYDXpINZUim1OhjnEGnqtZaQP82Mc4tgwfnfopoiPLsWx6oc6kniKSqS8i_P260Bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-k0BMGeCtg5oLu14coGxyuLUbdPDMaC-efmA7iaVzRKo_S9susYk-MNTSrbsuAenOoHbTZxQ_qH8jPNEd27u-AvyxDiqQ1dVgU1SmKi9jUl5CRH9aIShAPxMMHojuOP7vYOkd-JxjLPss1uZMcVlsOiFMZbLh8L2MN-xqteH83mO450gJLl08_vC3m8ZEx9px7XkiW0S5I4-QwGSdFxCs75aVw_ETMT4U5cpWXjzcwJP7-QfB33OZFZfkIF4Mnsuv4o5ojd5iN18XxvWLnqXIl_oX29BhF8j9LFOYvI_HLv4Bgglke7jpl2mJTw-IsEM-6vwoGMoyHOPV3JrQ-vOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeE8ttAfMEk8sS_1XLLBGrQhI6fkyo0WvTuxBm31siDFe4A4d7k_5C0U2VxQV4oJnpYpCtK-_sh-JNsv2ekOTe2Hh_TDt1KJYQo9otL53jHHZOzwx7OEcjDsDRJqg_uC6pBxabMmyKE4dqrT04i1exn222kPJJq64YDu3yXcW3rri8Y_0ERcF7QA6p4teRi1CxKCvNA4Vc-ZTR89jBd3a3u4aB0igpYiTOAf_IQsQGlkD-LlF_0i-OG3Txrxd627dbat_jq4f-uuEv_SqoUrDOfwADpCIyoBy0MJHpjRgjDVzJibMakOsGVmySVaf_56WM31CkDlcgp5WVULbz22Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4hscWxFTq7Q_mDkWPsUjMnvokaT_NsomlW-Tv33NjopX4-9tztrAeemW6EZy07a1Nk0pZLjvDy_NL-ZPdHRVeW7KhW_vFWgAlwys5n2JwkvXjkKWr4haVPmZVX4_9eD6vOdFLhd_ju0eeCAGVif_z41lC02l0AuDvhnCfvV4l1UVQWRIzSQ9-wQLmRL-LmVrPiz5sT5cZrbpxm17b1bf1Ng4QRLNeJXW3FCxNjWk0O4hjYyigVeOKaPvfD_3QB85FMF5prvfOhf1wGSFpzb9tIg8fF-Ego0Ao_hACIgGqZAg68Ob-7clhz-SF5WmR5y3wn-ojPCOYWQBOoZJDvoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAopd_YkDgt-bsG2AtoFMUupvdRklFQZlFAdEdVfjmY0ALDTWTvKo34VcLZ7Yk7CNTDQol44EvGTKsASD4ubxwMHuQ4tu2CLrTB4ycY_dY-i5belO1O4rGqZlbScvMXXw_q0jlMjW95jsnp_3uOT-0_w0O2hQK23VHj2PtPktG5WXI3lJL26H1cLZCkBKeJkyRu2hTZbF-ApYjxEQpiQ-6HMcoP4ffXRIJPyyzqKiVu5uiQFMSguZS0RWp57oNk4Zt1DBbZDJ2pNn38-Zrzz8Ba66uqCCiSCBxjIDBtbhaWUp1oEH7l5FzFjz_ASOVCHDAhJXuo7-319Rks_r5oQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmaF5RSOQ5KCXMKAxgm87GKPtj-fpgehULC1XZA6ePr1mriMzQ4-yd2n9dCrcctK_Isw1Y5VBpoomLkdMZhLGj43zRx6QOSg7Zhn8UCG1FrQWdg5inyPVpeNTeFjOPFDGKvvbD7yUHhHfbglGH1tGIOx5l_-ZU0GJsHBOuRH92QFeF6YYhuDU_8FwLg8SlIuIWTLsJxLBlqBEjIe5QBCw1dTJKv-fb1ksSfR194Q9oj5VNFlCd3s-n4KvNNblb3SawWkMNe1Mok6R5XGHds7KdkiBtXPuYYSiJ2RCNzvIn8KwB6kNmHIMa2bhQFXDThRqRCOgrGL3_ZMdRbCUpf7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD3tKIa6sTGHu3QHmyTjNhdvupjfzjWW6wQqc1Q79a3V0npSmzXOFsTYAbmSHfA_T7TXHvq7UupSPZWwi4ZtbUL9PpGvfdrdVJd0C5iwD4JQAZYZRIBaMmISB-2Jzj-AMbhhPPIbhT01TyBSsBbbeGFWiiAVOEBZVkSMweNXDRexkyvRqoMePU8gRY7GCyarqUJTbpNrmTTaGDYUjbzu8UUc_a34-a1ajeON34E4lJT_eXR9SManrO2PzoArivBBZepTxfG_4AXkrtn65e3L1R1Gfu6R9BrJIupFwoLatKbmu8FVeGRObPis0s8vzvszYAxGo4--wlBkqNgftaL3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBu27JtdHfoG9izratTut75-Cs_atB2naNPzP8oys2CCWIvL_oiKwH2e5HvpNhIQW1keJA9bfc-JZU1myRU31Eso71s8RNtHzk9z2-NLPXctaxV2HI2mPKN8-NWj1CIyHgf9ScN2i4ASW7OpP497V7ptK3tC8hOxxX_vIZJkPwBSzpJAhqysn879RxesSVr1_SQrzhRR6oa-sK5t5sD_VTaJkIHQ319TzhKMzqhsVKb3iSS-PN-lu5PivdP3Quj2S5lpn9--SsvhgIvN1Af8lflBlKGwbV4DKMOmHDR7HQlElfHPWgQWNjdWz5GT2P1e5XliGQv_SIztQzbY06IpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODqy9_PzirnLEp1CVDgWzj-b_Tj8jHlfG5ufIFW9osRLpAZAQmGEqHwURQJKPBUWjZXLVbYyqDxOfv2UxACUkELrSxCjI7BGmslRucFEHmtf9Am8QS2bM-pCFSegNm3cqeWOFGnKNI2tct-mStrFEfNBJHgOPU4O064XR-1oWHKo0JCMTGbmU4F70VsMpouBU7O-oCfyxTZLPhFwYKOn45SzfnEEfnSBUNPUmnntokVKt2qcGvDShv25HUJtKdzSqtj6FmaUWtS32mToZSdCGNg4kAfHVdr1Ow-L2FNoUcVUHrQWmKwf9-3pHJMfSJVRAPfgC4uGjWg3n00jhunwpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=iZqtXhD3Zxh5uica1H1PsvqKDcvMs0bzhHW__cEbFSd7KEVDVE3VLiS9giyeCRtlMsupDJdS9WmX-Yon_N4vH0na8vWdoyr0nzt1SQjaJaZ1MXe2b5TUi7SI0gvIxC1WI03mER36dgd0MhlZcRFFXnSOnp1psdV6J-Bs6CiYceZOU2Z8NA-PIo9lQaZJXXkO9XxftvNLD_E5IjBhuDOEofLvxu2ueb45qt2OwRjJ6YaO22DKwKmRi62mXi0BdIyKDXtUr7JflSS5t8U0xOFFbuQrr1poKl7a0yqOZrjzcbadRZa6jlAxCRajncrmQ_JBDa5Q1Kk5m-AvRYGUlJI_5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=iZqtXhD3Zxh5uica1H1PsvqKDcvMs0bzhHW__cEbFSd7KEVDVE3VLiS9giyeCRtlMsupDJdS9WmX-Yon_N4vH0na8vWdoyr0nzt1SQjaJaZ1MXe2b5TUi7SI0gvIxC1WI03mER36dgd0MhlZcRFFXnSOnp1psdV6J-Bs6CiYceZOU2Z8NA-PIo9lQaZJXXkO9XxftvNLD_E5IjBhuDOEofLvxu2ueb45qt2OwRjJ6YaO22DKwKmRi62mXi0BdIyKDXtUr7JflSS5t8U0xOFFbuQrr1poKl7a0yqOZrjzcbadRZa6jlAxCRajncrmQ_JBDa5Q1Kk5m-AvRYGUlJI_5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23659" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9LF_voUf_O-HZ86qX-xS2cnUOiV8mjgmt8brdyljGtkt9E-cn8c7P-vRR_Yx4I2kkszSHBPUhF4Ink4_sIzYdBDHC8LtDhcRW2Zf9thK6UQO8_lZLl8a9fEEyq5iLSWOnA5FU6RzAZBzX8evsHPLj8jVOVFFqYKJRT-IfFCyS5_Ne3OBFGNNLz6u9qzJAb9xoP0lzovubiIdHe3nDiqRw6Udq3UsuJ1H_V4wueeqyyxLDjzw_uYSPW0fk6EN0q0JMKJwg8uYrspO2r_ev9yupIsNaqXh-uKwb2jbOqx7d8262aCS2uiyvHOXtQWWgG0KBPQtD4VGl0_AEDC_aDuiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddNOIxBYMg9NYUI49WM1IoiZ1uCXr8DYwdUBPrtG1FDqf0klZHtpT1deYy4vqeTlCBBQuJs_gu_pDSYz9lwaUQX3hjtBTySxyjE0h-5Bd8z1N554xPzPeRAPiMQmLIOzDZ5uYOjDUMVxbMIopDL0fA93uSyz-bG_SyEsXJ10t7Bq2iSojShY02rzVL_L6r_jkWcKeqzJ_B0hx3hhZ9zsWylS883-qA30Cf1fDvHUU1eCisHBADDqiDD1wDyO4ZAiIfD-Po6xj6zs4_T4eMMSVy4ggxqFg7MId_eCLrkYTXaWsBUlWeWgR2IrRjbpTuSbwxykV2QBKmpSH83oGANIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWkiISVTGwpcYQSt6XCOVtvOSkZI2im0hA9Al3Q42Ekg-EZ0mHiJPVagVp6v_98xFwTGDsjcxsONFvpjrfiz8XuaJ3f0nxHyZX1JVZqiLjeNuDbLrP2KvQuWvBdyPsKpfdrpOR1bzML_Fy_PfRTq6eMh2z9WQLaxY5Y6O3beIAhFTjHaUXGDKkd5EXiEsIFH0YopfKZYLPaL2eaAayOJl_prBi5IORpdQ4bl94ByeEowr7a0JlDmsFAv45a7Ae4aph-BJSjvOfXOS4VHSOWbxPTaYwmmDndBwNqZ4_BEjcJo9VPpZC5AQdmbK9OL2ZwudNojPFqT6TwOCRqoGxEeCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=JIHOCe-em6Ge0YXr_CymkOr0qc0XVj8SBVleuvt0Yc1N8dj32W7IqK8z1AwRVKFZjYp-5DZiWKDQxfDyFOEySR7cI8mN3i3EWXSL3EMRnmDWqu4Hx3OlgWTO41XPLPpQAfzjJ63FB2b-kIs09jX6ZRMSDWNlgXS_XYUkQGerGvtyavoFmQ6-yXjDh0rBpXy2k5TiHvm0Cdy_dT1j_8lseqSzRR1XmuGPhulEVH67O2rvXVhwRnvYGcQJ-maGkE_5OwP-EUWYzmDMwFaqHTUDr-APbck0JLn_WUNn6HTs0mSmT8CsPAU6fbNEoDp5OmRJLZ5PTOwBXVrlqg-hHBiMuk1bRJ6rtXrmP2wGHnciDaS3lMYIIqUxDkf6DKJTRRwAXVwmpSFbM7Rat1_Wk9q8GxcFsgNWhnVIBmm37AF_B9g1I3_SD_fm37VWs_HebX34ha3m1xzPkuVACk5JMlS0avcuyqUvOpc8k-g_FgwHoQn1AkSN3MBhYJ_D5db7P86rUCQal8Tvjyfvw8zO2-QJysesPNLGNw-yiy5FI_eW-P3RmdJ7zx5OdpE_wMbOxHgtxPBdtW3mGAKjYyZfhAImwNTLCyZr-gewBCLm-XCquTgfDy9Iaqk3VhaNGUb9oP24vAxY6PKd1lHm0Z94n4IO60-NGQlOnnyzBfoHZjOCNwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=JIHOCe-em6Ge0YXr_CymkOr0qc0XVj8SBVleuvt0Yc1N8dj32W7IqK8z1AwRVKFZjYp-5DZiWKDQxfDyFOEySR7cI8mN3i3EWXSL3EMRnmDWqu4Hx3OlgWTO41XPLPpQAfzjJ63FB2b-kIs09jX6ZRMSDWNlgXS_XYUkQGerGvtyavoFmQ6-yXjDh0rBpXy2k5TiHvm0Cdy_dT1j_8lseqSzRR1XmuGPhulEVH67O2rvXVhwRnvYGcQJ-maGkE_5OwP-EUWYzmDMwFaqHTUDr-APbck0JLn_WUNn6HTs0mSmT8CsPAU6fbNEoDp5OmRJLZ5PTOwBXVrlqg-hHBiMuk1bRJ6rtXrmP2wGHnciDaS3lMYIIqUxDkf6DKJTRRwAXVwmpSFbM7Rat1_Wk9q8GxcFsgNWhnVIBmm37AF_B9g1I3_SD_fm37VWs_HebX34ha3m1xzPkuVACk5JMlS0avcuyqUvOpc8k-g_FgwHoQn1AkSN3MBhYJ_D5db7P86rUCQal8Tvjyfvw8zO2-QJysesPNLGNw-yiy5FI_eW-P3RmdJ7zx5OdpE_wMbOxHgtxPBdtW3mGAKjYyZfhAImwNTLCyZr-gewBCLm-XCquTgfDy9Iaqk3VhaNGUb9oP24vAxY6PKd1lHm0Z94n4IO60-NGQlOnnyzBfoHZjOCNwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpM2AwSj01XutgxxtIcLVt5TmFFaV6kz5uPefznp7se1fkzMGmfJOCTUhUCu8EkMuGS59fH7ep28ccpRS-d6xV0GzDfhq_ZXW1ZRNztloR_aZLvbeLiwolMLExNPbKlhM0hy0DgbtaXQjWCnt8Zxnd-EFwBR0VXGDogJwWNzaWWKEBBOUiIMyIfw-Nqu2teu-k1Iy83odBoyYj10rdA4B7i7qE4804e_VqAZAzAjuKK0jyXw-z9xHHfh0aW6_F0uo1st9alImZy-iV4vF-Dn5gmNrm9mmN-lGCpaau_ltpqEb6oo8NziR3_5RNbsDD1eP4HB6CmwU2IH7kgDk9P7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tW_7DSmZyhxysHsHkw1A1P8IlSGsgFrzJi3vhyTALCeL1RH7Mc2_IFA-nXJT9G6YGIzOSw5WdDKyhHjOu3oqsvl5ZiHPluClvF4WL9EiJXJY3MXLBbIqf8FfjasRVL37y6BxHe5y3AsLC5D7cAstRubE0CQNYnWlB_kqFOhL5FbDjb7FbETQ5g0gyt7cUzoh5ybzak1p6jcQL5N4Et8jLD14Gl7mw6PQl6_yN2tHkrcCAbuLdcdHXGsZ9vIsks02UVMkVOud0xC7uPUFJ-2jfbSGiFo0dowEEwhp3Ouxtzi_i9TVsepJ5MmERKbXx31v37n_DJahTp6gQU6jw11qTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku6fdC2qhKWVthDAeFVRrkstqDxgYUf5Vuo8fCNH7mhUAYJ2dVLrJapk3-hF5gBdCxyG9dr1p50PXLk74vFJqnn85PlLXmyrnejTgXE-eD5cKtKJCzX6qqQ9-gcxyHhtic1s8jvS2Y-fni0xuKsjpbaoX6GanAitS8Q-Q4EpqnHfEmhDKWJ-rdKyqQs7yCEnf4JVPZAnQetfNe2hSPbaSQDQ1nCGH-WCmYT4SynlUqFpiWr3su6dhznaqHKMuPSP5TxSCJJlx9h2-Z5UCS8XdXafWqDsPElujDEyrBYdBCrav3pm0p9oNJg4F2baChJhImMnKfe5a_iO9yc62SWZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zi2lC8cAD2YYTfXR8-Oj1TM14W0Awt6OJxB1dTZYv063dw0Tsl_AYwC22vec2QWiAltTH3dKdx3T2h7kRI30BWtvnovFKoxFmuouumKvndVQdRGW2Dw42RGJkqNUC1XYpd-_j0sV0gdT3079POy0A4TVfpAeuRzl_2v1oiLnSmIXqd2h1KHjH6stvi5RldYHFShTwtDJ3yu5EEses6uzOEYySw2OQwCI2PCQprbTUSzu9l0nxXEZOMxeq5xJoGV2vymTGBdlCzsJ1R1tFvbkNSmsdviQMkbBUcLISYvPodqHLI7RefQkRnp0SnfmTR_0gPJP2-nIUJ7b1Vx-J-zE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYfjqJtZcTLlS8jETgd3NId967X5pV5Vx5zFaHx6l1Vt513exOnvR-gYn5pHkoUYLuK-hG1CsCx5zFJCrIvVCiCZhTizslVKbqDo3T9oivjOEfBugC9Nhm3ebXbYc2McrKCOodWi4e3f2O9Vp5zoVG8b35LZYWtbStzrh2kCzfynOwP9ZUNk7tgRncnHe0D-x2xtyQ1t6vjbkOfSZbQF_jsEfYuCMwiHsBLGlfg_83ZuVqevTWAaXwr6OrYlwzAX-ZPvQPdH9v6Tw0Yl1RL36ycdHP97xvuCI1HhTnOJq7QgEIPcCNd6__SYufJm-uUCwqtymM6iRKw2su6LibRlzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=IzTupXOFI8E1DOeG2z7zvkoM5hGmJux0btnPt2ZqMnZWePHuzGoqylkpMUCjI5idUraBmwVUtlM3xGfkhuNQeytgSve2HxNer8w3k66uN6l-z9RNZ8YTzNaKOesyKjGsl8wmOyu_4YuSXZtokd_iXzO6_oVFpFkUFJtEXGh8BDAiResA_1qBdXSRzsWSddy-zqY7oxMdKglPKA1W-3r3OHokG3PFk-iqtGOzSQkrxdtvHacbyXSpP6U17vSCn6tOM2YSIo9eXJIKJtOwMbQjlpYdUJGfDh17veXke0ZI3f3nZSxIk6JTbiADpcpNlVWiXrs3ooNf4fUWNlTqBQKZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=IzTupXOFI8E1DOeG2z7zvkoM5hGmJux0btnPt2ZqMnZWePHuzGoqylkpMUCjI5idUraBmwVUtlM3xGfkhuNQeytgSve2HxNer8w3k66uN6l-z9RNZ8YTzNaKOesyKjGsl8wmOyu_4YuSXZtokd_iXzO6_oVFpFkUFJtEXGh8BDAiResA_1qBdXSRzsWSddy-zqY7oxMdKglPKA1W-3r3OHokG3PFk-iqtGOzSQkrxdtvHacbyXSpP6U17vSCn6tOM2YSIo9eXJIKJtOwMbQjlpYdUJGfDh17veXke0ZI3f3nZSxIk6JTbiADpcpNlVWiXrs3ooNf4fUWNlTqBQKZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItXVCglFQwP8r0SpMHKYBoVr2PWX4TLQMCRtukZqUBdA_4L1PKDdknwqmPO-BLVUu6_RNns-_OhpB8wTv8Y9xl99RSt78x5mqXCZKQbuUUmWlSkHjASXPWX1sVTgNAjGH36slrIoK4iv7LwWsjoEI3tQqEUYF1CoQLQe0zSMm9sP3Fc139QrwRPWA39hVrN7_xZ3cj2KAci0hlTm5pNWfeBAg6bCJ4gmXCUH2OzWTLQ8eli1S1Qazr8H0Yn6C6uUcG-nwAFxhpQlmO2pVJ6U1SRsLPxzu9lSsZG1Hv0ZLS8vmVo-aZDbndwx_pGNjt7c1drOKQzDPMv3yvTDlU6LHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iitxzcOsm5Mp1o446z3z3nctRzWjXhnf-PI_d_EfIWsjALRoiKlkcV6u_9XKcDrX32krCg5X1rcZw-mYif5ehWQxb_qCSZ_6MIpDEGc79FFYf0BidXl57DHQ-iczcg2MOtpiKnIzVX4VMLiyvWMnfTEnON7sPrxZUH5fCrJ0lxNAWI6yLYyWChi1n7K9giN2OUt39WLiDGxsaGGtL9v3uKXB_6EU_oYRdcgrYIXqeU2Jc05r-sILAk7VCOtzXW_n83ie6N42_FtBBWEiW_4F0qLPqmdjlZSUXKTsoMvCKjNkRTgTYD1aPsESH_b8_kl2wHRbjeQdNV1xi5tu5mmvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRHa8m7N0qBWeHi4XyCS2OtSJgz8XrNUGOUwcy3ufWeE68QT70kz5WLu-j9qU4C-WNU4EvpfEbQr2q5J9rP8vrKsYPU7Nxq9X6wbWWR28yBTkzdcmOLEEC4u4EBXxVO3fcWtH1wazp_Jb4mI5tsaxIMs6rTJXdvURcWhD-idW2HsLy72N5PHR4iPRj7-lPIPpW8D4O2zWrq2C1at5-vuVYRCbzQ1VfaKFc19yn833AFLLBIox0O1C4LzBmG52IXUf1eAuys9HSVfTQqTVmr8dp-oGSueVVPTHIJJdEVnXB_aNMTEZfoXZQOmPvsJ9RQuJ7Wofb6ftE6KHo8fR0QdYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkiX2qoJrzsRhT8tbSKOnDBpRb5V-_HVDxiOP25Xktx3DqcW_Tuipqsvlq6QYa5Mv38hsLbTbBD4f27e8YHnhcg94PYsDIWj5cRNvqmsm5lqiwCE9W-41gIl_DRm2FCHvX4WwWViD6vcv_nQt9gybLlOYAywnCZsBJdc7-JHMHdMHbdbwuY8SYTh8Lrwz7ciAoAUJBZfeJ3Gl9SE6Zssw1dHPS1X1LNXl4OXvFhIkycROn8RcR6iUZb4MSdFv-coXBi2DuyO0EJcniuxItHDocLNKdtrpv5H1f19qkk3QvMTssH5CPF4IhIgjiOPWMsUKD_2hpbh27emCxHVNFT4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t26h2GrjQ_FJb_uOagi_K0M7ETQ8dEwIQzF9CQvbXJOSoM4ERRwSRIGapoo5-akXpWJBkLQc1qx63CsXiV4dcngyvJ8NkdQQTHCch7Fn0g6A4tTmH0K7K2LGrmUzPhSdnZdGeYnpMFFd0R8p7zgzZnFCFJeGlC8PGOWJYAhi3WF36fdATep8WfjNGVGsuZ2xNmikRauC-xqibQG8bGzpcKIaARBASMLEXY-VWlt4sIRM37XvVypRF09hu0ypL4gKW2Jf5-NVyYplN5o1Ap3P1pdTEm31DwoRqB1bEjA6wMNmEx9_18jHWL-mc2D2xj3qqNG_ALHSql9jZwawu-7lCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mN_4RKzFiBLY5jqW0EPOrKo7ka1TkatJjJLEtP53mqhVPomn085APO3dKC8N-Yq6ZQt2SMxm4fw3WtGr6MCmr4wfwrwwfgTg4zmTgNpja27QlzAFW3z3p0ZlYn4nJoBOHSL7TMFjvY9q_Kr4uVxxN0ma6Sw_3nHWEpACAKwcB4a6kXESbK_CxkLfarExeVOP9i0bDaIoJy2kQms3tGMwss7Cit-A1eOll3b_DSBZsNDzpWapePjbxvs9KeAbJwGI1Ia2PJ35pKNLJe-I4zNzNpuZvNW0YrVRADUeEeQQcv4WKUhw2oezjzNq25ZjjCViwVxo0j7jpcHGCea4Ycy2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0Gj-m8imWJYkqZwj3RBRlIAaoRGUN52RRiRm3n7qNiyvf4RgPazon1P9-iBWX_OTjGaA5BprFlFM9NzcA85wc5N43qyVZWcbptlHgZKaMdE14_NjTq3b-3Yy6Q9wttlIqGlBL7f-zhTlPVaBcVKrfPqNJtuWcKjCDpKERSuLMloHNzJcMbCNvIHoQr0UsGTbw4sjNq5PFg1LR4X1a2eQL2YANzNLWT9AiNmW1kZ031XjGiQc6GqbPFjgZxpsfMSRWm0gDjPD9cWq2P3rJKk5J9FdGA7WK50OoZRI3pJ9JohJtE9i4GNMBcxS_pYOLERENquaviPiAlLAPGCNS7C0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0sSTpo3KJtjO1dBYJiihqESa8dZIPfulxW-aRWO7yv-onOF_TtTxsqqHuioDXQimJSYxKTKNOJyyU4ZAnxL4Pt5k-d8JxUyqTfL-LiQG7qncXsRfWPgMTRgyUnfFjaNp7FKSwFF6nGztfdPxDoh3U-ItLg72eah1wPu5_DpLvV7GNUA_gRwaaKeN3BtwopeN8ZZTmfr_ZKoCKYLQ3M2ZY5RT-THQvZIfo76-lLOJCgxMr1y3JzwcTRQlE_9eiWLWFJ5TgDq63OpGql2gFerQ8f5xFJPu3cthDzB509vP7XIgwyy-MEG0whrIiWIhHi7a2N4wafN6IMEF0qIH1rYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJO_Hu9ekG8NdBmscXoEWUoMkwM2Qfe5vsvRNvbeHZDkyqeq8t0FFeWvSV8r0h5ZyYT1GT7l6kWpajhFvLBzRVunjzjakv5mI-R8K85Bv3JzEGd7CQiB52Ok_wiUcWULKTWGlqZprwIHVLwd_OgEGKxF9WbjebInpCLUn66ypy6NQcOjFdMHPQZFXycElzwMuIPkUeeyExxjyEx9KwBnuYdLe1pTLjopJR52JBEpmNDm1tE3glVLI3WBvsiTQ3EbMlXsfT5aYJXnaecEgf2oY39Mrzs_yyni0EjUtffgCYU1icg6NQyJ37Y3So98Os112bJW_ayAFTreS04AkNOWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph0Re2bUMW__TThywqKtodEIVV-iXDU53oopMLDSTkJ-rhHhJlA31LL3AqH9nw0sKfpGjWLUW9Dr3lN3k4Mk-akAZJlIuKqxW3GYd5OPo_5joHGtsTmmHuMx3SdCgwDY2vTdaUVYIMa-lGGSEFPyRuUGAY-anDSL6gA_ar250YP-TOTmTXJR3b12HTUEATNLw55snkXGt6WhEKinCO_W7b43tPDWaN-6jBV4klyQ8Ay21BVfoNIkSErWreLKZy-1LWIG7kFvn4ePNr4qXJ9alH3-nfXB9CvtClRJpsjrgRoALPiKFZCvUxwwru2lvTvOWoZxhV7gcXiY5i1xx6CWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvUr6YnrLjvsA0faz4aIWXJvf1JEvScMAxIrlZr5i-lDLi5HE1L1EX054kjQgdzqt4U9fWRUIzmwtAiX4LX6QW6WxKVWUbqKkPKBx3TImQ0zwPCTIC60bxpjWrcRYK1lz_2PfzJipJfEpXA7LKICBpOKupKbov7AROb1nNjZ2KTynTRscYkua03xeO-tTylMthRpGw9yJBPJt_Pha8076H3zenSluSOH6tScCBfMlQqYQW0-lW6hD__7TI49KBzU-CVd-PrHZgSN4wK2bWnMz-U7EUrHlULrj251UpWMwGlgVOFx1DliYEme-Uo0vklJVc3aZKtvhoXq1iH1WSbg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=RwP4QYSRJi5WJ8CJLG0PPfHlWgbbReuADnOtQbsAXWvM8uTAiADGPtdtHQUeWdhok041gB4aRbDDTZII_TDW6wxss75en2EKDLO5Pha7DmAt8ymq9gn5PnCYSar5X10q4_4F7Kcm_5uRqo4NNsUv6DJHNpBjqYACYacGKYoUKcvaeEa_YlWoOUSy0Jtv2M0Cm879NOL32SdVY7HT6lyKAPqbo7uI04HFknvJy4jwpVfzT1F8O3e7gZRxRJceEjq_pOPcZVU4kOj5_47Z__BUBwfErzwdqwtX6301zV4goWRgVFVZp0e_oeyeGke2QSmP2b-_6G1nC6rFac4EEoqtMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=RwP4QYSRJi5WJ8CJLG0PPfHlWgbbReuADnOtQbsAXWvM8uTAiADGPtdtHQUeWdhok041gB4aRbDDTZII_TDW6wxss75en2EKDLO5Pha7DmAt8ymq9gn5PnCYSar5X10q4_4F7Kcm_5uRqo4NNsUv6DJHNpBjqYACYacGKYoUKcvaeEa_YlWoOUSy0Jtv2M0Cm879NOL32SdVY7HT6lyKAPqbo7uI04HFknvJy4jwpVfzT1F8O3e7gZRxRJceEjq_pOPcZVU4kOj5_47Z__BUBwfErzwdqwtX6301zV4goWRgVFVZp0e_oeyeGke2QSmP2b-_6G1nC6rFac4EEoqtMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZjMI0bbRdmJoiZbvEEQ3O-O9keeEod6Li1MFdA1GA6xe8FyU_UlRB8oBa5rOJ-0gDY0goQUok-Ap2aZfJXPhgWfUVqT1H8tXPv40Vy3WNvfohBuUVf_Y6adGNIU-8oUniF6YeD_ForPjCAuSqCdXVvwkYoJF-s9sWZnDYR-4GrxSlaY6ImdKZ6R4H0bfIcia-qNjaQavX1qpXKOgmFeMmzomY-woLPfERQb9dGleXMpyyrRchi8HrlEGJjHtA4F3xbv72B42-NO3bsWFfsT2qexDOPuHnyl644LDE104avvJ_P4hglJLQmhbVvxLyqsfvA7Ko2wBDlFwabVx9hRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STMiUiVzS7eXfNC5keGdyTRv9xbE3Zb01IvoTun7zVU8d7of_LMsvmjkI7Q2IUoEE522etVcbpZXcfeirQCTPNkhSAKWon6JvpRuPKHlBdzLW6tH9jxRv26_Ojcww-PpMU07OEHs-dFmwPGHHcetd2in83fNEcFTSxIwsElRredrpHJiuwEEV9B3d4vQrtDIG9gyoasN5jmxfN4zuwGhQ09bi16Q3rsrs1EaVZWbpmD9oJf0kIepxRpHrv8vPNCcNBNSqVZX6DAF0ObhWY81xz2mMwV_LoBmOEob9J2W4IQEpdSFrSOsR9pFNlHixP-AS_1qiJipUyT71TKdNaP5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZeNdZbBra6aG6oBP_7MHkF2Y967lnq0hCuXOlClaYccr6UhDPxAYMgVWbr8Oa5px2el4s_RFz_N67Clb5ii_Zo52IfpZZy-fcRzPVJixE1n_NPRoYGvn46SjX2hv5xaumHxnBICmj26WRl774dnEUeroNTg4QdchG3oiRVgBPtT2TPAKyYeqeIVd7DSxKZKciBa9P8YGnNHnUtLX0A4FFQWV8m-n362xVKjGdustA9Uogkd-Z1FzANSi6Oamci_hGC5vXwkUwUXrmWG8khtIAnJfqUxNKZYOPfn_pB0HJx1gRN7GAjSDemII7no0kkdTwhuzLHjIJQ6BDcPFZYexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B74aT5saNekJElWZj13Yvj3vYFVZEm4Roz_6zPE8dsw5-ZUJ6BeW7xvCcEy8SdfS0ySM8uhmtZBW5FhUjjtqXE5V3s4eG9qRLoTpQxmh4p4yCR8_NStpowVVBQFfItvNC0SugToj6vKmTLH_s2hOxBXyY2ehJEwWg7a-1eEMCmM3dMT7HKEtKd0wDhMxCmkpQal2WbWa5oVN7rsMe8DwlFzZVwUwyhIq3DgerHWEYcNjpbj-lR-mMgK13HumT22i-I4FmoDD8ALex6afKrT8a66-6OsGS2_ugADKCzi1ZnZSq8moOp-gPRufp9HRpUupW9Hlltg1ezzYwjYq1gKyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-vaNJ26UP7WruwPhY8rt4IsZ-lyfPyppvenQbzFW3urnDR8UG9nRiWWN8tdBnxClUEmftBPDTTn1vi7E9azb3AMpqwZxesknCt39k_BMANwVNa4DSmU_Lwuj8HHi0hPKNE6emrRXnh09UinprH_k3c58lXbAzM7bf5BpTBQg4jXDx9wh4Dc8sRQXdV4uqOGlkcxL7k2rzPpHzpVZlyYVM6pujJ0j-LZ0wyOzZR25loEIWUQHkbaCIGljM902icBb5mD_e8FN5psbL0Q_QUEcqSv0-rG91_8u5DKjAykkqL0M9rvLGvyqNErTPAWeP44C_sNT795XDLr90ILREDwIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5vlvyBDX3gkMekRKW52Yk5FKq_CuVOQhP45S93HodeCvsJpd-2REbaXsd91cEd23YROujXTNl54DhCLIXj78py1bgQ4-bpnlIxohxLINN6BgqEjcFNe53gAL329E1_fQtCkesihYHsB5b2NtREsghBhEL8ScCm8hItsG0LM6mr0rHdgggrGnneL1oipAMsaOV9kl2ZLH4LTssO8pwlxzS99KtMjPAgIOlLEXDfM4WIlFuPT6WwZInwcj62z3u47QSuR-mo3wninZsoFO_2MpSMe0QbqMbI9vJdS5UMpgB8VphCh35te91-Jz5E9o9AhaSE3FdMXchbsEFBE5e8aaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhz_maP6oaotTPInca0HsI8nNzP7IbSEyeLUK2DCdH0TZ5LiXRn-BblXC2SVhbaji6pydtW0vsazGYeFaIKTbI7zRchejSUQ2IbqH9CUY-oqIiqzSaAy45MEnwLJe1m4Muj5w3kYTTZKxtFzrDdx22-DfKKdtlGQS4IuRbJB2fI42FyoaZEhWuEiDJTGnOwcp_pJjbteEdu5T8qlVZdQ60eOGJ59jTDlxd_7Kf48qjxSvp_-KBhz49Qq_tisPvb0o70RYdfJ3N2r-CW6JlFPQfzuMbpRoQxf162YmPHulcw5mE7m7Fw-wyIYvbDrGYPpX5Ae9NAzkFM7XJCY2xZwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeQtN--jO5gICwpY5eVPsBj7bkV8gW86jKqnA4sDFBOFtHL8cAjseGTBZMthPQebDTHkiLOmFRqJ6AWFcKJK1cMCcL-H1pAAiHCmdT0ny5GB0_DhBrJKRkD32wXJlwxK4UcQnnyXL4v_rEAiZxIzDeNlyqKJxkK_smNiVpVgPiLZL6Ah0NfxGng1oWGtQQlP8Yz0ucVhduFMxfpqmO5oVtvU2mhg4PhLW6OJXZj1ty0oB4j2tocfJf6ZI7in40ErY_8CKb5W785bhCi7bxE2ksrCxjfhSgXf7La2_9sIwousEdOH8SRU6Z3JUVGPD6dMa0xS7bi-oc_sp5y-UFbFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=H45GeEXnPqaRX0lYH8Gtp3Jv-cTjMyn9LYj06tWE5hxklrlxA4GgwluAYrB3UGPWN0vjDDh4LmA2_4yuvEv8gMMjJRJrdmKi0kidU84eC0wiG9qt0aeJAr4cm6CIdnaPVk0jPaKtEm2yV84W4Voc_xFkQmUIE0dQpg_281iaPunyPf9l4FhWlryegceUdVbaiu6UN1Km-BDk3lX1MTU_0GNvFP6hagsgAc3qFblulJ9XGJ0Eni8IlGiZTXR7C6BM8eNJLOtKUf9VqSTEvkg432zAUN2Jb7kpFMStzBp4k7i7P2rcZToQYqlkg1TDiUfDmfScSz01CngYcxBCudytlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=H45GeEXnPqaRX0lYH8Gtp3Jv-cTjMyn9LYj06tWE5hxklrlxA4GgwluAYrB3UGPWN0vjDDh4LmA2_4yuvEv8gMMjJRJrdmKi0kidU84eC0wiG9qt0aeJAr4cm6CIdnaPVk0jPaKtEm2yV84W4Voc_xFkQmUIE0dQpg_281iaPunyPf9l4FhWlryegceUdVbaiu6UN1Km-BDk3lX1MTU_0GNvFP6hagsgAc3qFblulJ9XGJ0Eni8IlGiZTXR7C6BM8eNJLOtKUf9VqSTEvkg432zAUN2Jb7kpFMStzBp4k7i7P2rcZToQYqlkg1TDiUfDmfScSz01CngYcxBCudytlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6CHOwvdi_IXgI1XsElm_s0TUyG7Rr2dK1D1BTt69kvcuACB92LvAfBfpeEXlbj8bLZKVWK-K4XgoHXtyX9DHEL8HDwEBTFGjyKKkDUFd8IrJqBXHBM3M3nzcOXEGp61EZpcoMQEyX6S6rf17EaA-15otKB1LfiHbSzGYdFbyaJR_OmX9uZaioNgkT45VJxx5pZdf0U-xVxGkLBWLmG0Jyo3_ccoiSedBP8fEknk002g7XFZn_cBqxDdFbhsZqEVc6DXHePGv6C_zUSOUxMP1DmgUQSkqZ37qkHcSeTQe55_siCFA9gdFNKqg_baB75Drr9mbLsmGOpZzwRpkkvjcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXehg_O-gIEzGWVJuNR4Sc1SU0JVsYzqpBSDbIgpnVHMTRVGiag0Jvz4IJGsSe_IH6_ItVpgb50-x-dWhOobetkx_WlQfVaeXrbS5iHHlVWk_-WEwzzl6G0-kdSaNWZQWVAFcm8kt5JVD3mtUuR7vBFcy7DGDj3AuuNWkb2iq92QKk8yte7qpuH1gKbdz8x_xckp5ouPe2crZIh0PEAuTF697YeQNxJrhoXXnhCkKfzhYsl2QWmP59jCYXnXlbviRlZyhzYH_Zoza64SxtFr4J-ftHtGTIUlU9pQYZmbCwgime4KaCOenjWchOD2nc7RWH5Lt2OMosR4s4IbS-Xecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3lidmx-eQ9g6EJwDldWNFwAD3guRcwXp5sNL1NCr3pjVo5CqaoUE0U6Q7rjEr9vvwXVTklQLEBYYMWIdQotfW_MlIH76pylFnnfv2G2DZ6waGEpRWRLCCud1UY1wSXkaR4o6KTHmtdtyqVpqjED__Od1e-y0dolxG32KNLqx_Dcj54F4uVo9MLBFpwLWI-rmvEgoI9cq7X_RDBkBzFUfZAAYg2U9y10kfD0QqGoHdVo0e8WS2HMvpe980xlwz3ZAusfmqFAzAN-WJUjQJBaRUffx62SW2lctp9juJd1En_T1_O5wqsdPQRPtdHqAxA7m0KlKjwCwjgSq9XCRNR3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-Nqk0Ftc28-nqwvNHHT0GBvf_FVesZSJ_5yMq9BIBAuHChKsD770H8WHhalz7qBZj_b3ckrpdx_XYQTH_FwnXU5Q42uOFN8HabRDmrxPj75nSIqsa3-0guJg2RSbxRpvGdJfq3tfc9wrqqhNZzsvuSC-d5ICeMyfVwyPOiWn9mHOlns9JziK4YXAzbKCmBxXvgmobm6nel-B9ryiigyyj-eXwjSdAzIVOG1CqkbQxJttftp82uBgzjFRtvFmFwR0DfRH_dJ3VcPR0Wl4OtNe9cz3XfPssNDOucfBfdU5x1__ycZYRALbv2bDw6ZRKAQBe0hIH5U1l60rlp0l3K61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkilxMtmdRrKiN2DJ59bx8OzglCc2PFdYPJtT4A1rTGYcHAZgQaj4cINfXkk8WyTzisFuMvZqECtWtMDU4m7qMsZrMOrZIV6JLHh74Si3l8PuhRDv2NoDwozwIAqP5SsNxyWBFBEqLmOcIzo6sHNcH-xL2aHTwNMYlYa7xd95PrmjKcc8f_t3hRsNwPJi09dOAjotooujPIqvT7BNDwmgXA5GwoPuUmWv9OU4ErQgneBwr-PCndK7ZN-UVChGb5_Cln10N5hDiix1DQeD115U2nzoCpQNbrOMSmCuLFCdvRdQqPS4e6PygLJj8NKngeTaRZEGZh731Dzj9t498mneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=g8PYvxghk9qlaGH6lMWObjTlr9zcgPQUxAxKGMaBA3Xtf_oafnIqAsNV7ikTWrs4UOzVAM0im15iau_4FNgw-UzeUHC7v4Crm5Jms7eaJQqPdpCXjx0oU9tdXgiOywXFuPNL64z4sp1hEpMG9sIm_DdK5xjNdw67PUBpO0eQ5JZXf28AN5frJ7Gss1A_gu_RNKZj0_BDZNCrCXLhOylSaLvHyyE0bOMnq6JEPuw2VSgouEEwTiBn9NNTuX001G0yMLzoH239V3Tnj9NOyjFGHdcBh-uDPG8jKeBbj9VZWp22IP2oePFEZMBh6Yskuh5uSDc-O7Il_AgzXOj6h8GAxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=g8PYvxghk9qlaGH6lMWObjTlr9zcgPQUxAxKGMaBA3Xtf_oafnIqAsNV7ikTWrs4UOzVAM0im15iau_4FNgw-UzeUHC7v4Crm5Jms7eaJQqPdpCXjx0oU9tdXgiOywXFuPNL64z4sp1hEpMG9sIm_DdK5xjNdw67PUBpO0eQ5JZXf28AN5frJ7Gss1A_gu_RNKZj0_BDZNCrCXLhOylSaLvHyyE0bOMnq6JEPuw2VSgouEEwTiBn9NNTuX001G0yMLzoH239V3Tnj9NOyjFGHdcBh-uDPG8jKeBbj9VZWp22IP2oePFEZMBh6Yskuh5uSDc-O7Il_AgzXOj6h8GAxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0pU-Um1W_OWOApaXJpGYlPBMmkB-XzOt7wP3gxt8lTVR1qcXpkMYvPtwZlyXlyTPCASE_OkqUi6CY28ra3whNtRPTDUX6jHjhg2x7hznBV8kB06Dipqy2VVTubzle_h8N4ZCMFZdF-UnKBa2DRmmNepXH_CipJsNNxtdyXkwqDq498q6xzQGUs9RG10YPgKKo2h-bDxzFfeK9tXSQqUIG8E7l-dua-XyecNqOKyjZ3HmDe1dcQtydYxqOX9FcP0bHtc6kQq6FHjzv7fHvQKGHPWuauhlSCVTuHzuQkWcZeh-kvTI07c00urU2-LfqIfn_DaM-TBD6ireaSjgHffvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba7VCzTHxlxR9My8u-moGQXjHUAXyiNsmzARciT897EcURP7oNbASyDyBT9WEyzMaopDU0VkHrPzHCwLU0deNE9s9tMNhQg881c_ZaSwoz4pkifU_AjN8YlhRf20tcJohDbtkYV1-QprFrwqTZh1pTHE7IbRPnzWkcdtzTiYGcWn-o6jvKf33pa-Beu31p_xZrPPpLDjqkkUk21Hb0hscc7SKScNR2ooyS5sCStFmg7nlWPBK8Aa6Z_FlXkl4GIDiOXjo3y63MaajgwDSfAxQYqW2uu8sh_pqbKq76m_8_ODkDuX9xSFmMKK-bSeUUTLEa2X_lRxc0rt3hFaD_mW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
مدیر ورزشی باشگاه بورسیا دورتموند: چه رئال مادرید چه هرباشگاه دیگه‌ای نیکو اشلوتربک رو میخواهد باید 60 میلیون یورو به ما پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23609" target="_blank">📅 18:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=myq55-IOR3RbhBSKTAmlCLsgkC7vzI3kAhPe5wQrGVaXgPACCXq67a6iCpaSnRiqqG0OTkGDfjRiXwdS4dqJ6nV6ri8hjE_O0BGyV-dNF2oSUGmkOkIkjU8bEoEAc0AQPKe8KXbFYTRK9Jpq8f3sSWCPRo8ARwjSRyQGUiDSBqy3u6PR3CDCWSKnph4b2HPW_-sNGs1gvntLeP2-MNiG7gu-N3TQ3SYkVV_M0bZ95THFMgsZKjnl4FT4RA-VO83kxARpsYaMK4mEBO00S3XcECZy11UAbFERbh7mzqBPFIMSlEcg-gC5YK7-hkToSmRCH_7gEs5RFuXVMPA-gplkep_cEz2RbGvUV4Xfue247wojQd2ZC1Qb0RfuK20cyk78e9lKdkTeYszhWZXHimdrD6NV9RqUo9qiSzGosbagMdc5GaG-n7oWDpgxwJtZQhKleo_ktv-zqEj6xS5F754ha5q4lyuzIDeGxVfYtLJfs6b3upBRnGw05zAlBnuuyCMlwzKcg03EJvYiV2AmOIQnv1hKWMteEeFwdoeea-GWpgDzJN0LeAsdsMCmAvJ7dSC8Tm4WTBLsVgZcs49E8BKci0n9rK1Ah5hBAU8W_kzb2lvRjSAgEZzHVs7STKqW988X3g8EmC8rwDwIznei60SpMS41T-rK0cVxqpUnwUmfVRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34a779f0d.mp4?token=myq55-IOR3RbhBSKTAmlCLsgkC7vzI3kAhPe5wQrGVaXgPACCXq67a6iCpaSnRiqqG0OTkGDfjRiXwdS4dqJ6nV6ri8hjE_O0BGyV-dNF2oSUGmkOkIkjU8bEoEAc0AQPKe8KXbFYTRK9Jpq8f3sSWCPRo8ARwjSRyQGUiDSBqy3u6PR3CDCWSKnph4b2HPW_-sNGs1gvntLeP2-MNiG7gu-N3TQ3SYkVV_M0bZ95THFMgsZKjnl4FT4RA-VO83kxARpsYaMK4mEBO00S3XcECZy11UAbFERbh7mzqBPFIMSlEcg-gC5YK7-hkToSmRCH_7gEs5RFuXVMPA-gplkep_cEz2RbGvUV4Xfue247wojQd2ZC1Qb0RfuK20cyk78e9lKdkTeYszhWZXHimdrD6NV9RqUo9qiSzGosbagMdc5GaG-n7oWDpgxwJtZQhKleo_ktv-zqEj6xS5F754ha5q4lyuzIDeGxVfYtLJfs6b3upBRnGw05zAlBnuuyCMlwzKcg03EJvYiV2AmOIQnv1hKWMteEeFwdoeea-GWpgDzJN0LeAsdsMCmAvJ7dSC8Tm4WTBLsVgZcs49E8BKci0n9rK1Ah5hBAU8W_kzb2lvRjSAgEZzHVs7STKqW988X3g8EmC8rwDwIznei60SpMS41T-rK0cVxqpUnwUmfVRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید.…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23608" target="_blank">📅 18:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=SKhh8HEcvlGIIk5Fkey-3_n4TIh217FDUzTE3rdtPwsbvd0V8EVgf402Y_HDDGlEiHyoilk4fta1dniymVto2AtIUB9yA1Lqmw3roYv6Cb2EiEqar0mC6exLFUamFnbeiIHozgnbddS044MCY1uJRruuSpF5MgHrGl9knvHAJdo4zO2ZGcE9lYH3n70RWnp-6wc16KjP4_UQih7_AFGYe1H9eSgHDZnnWu-MhVGaBTov1xFj9BHs1EIiTYt7VJ8i_UQp-ew8llldw8mh8DsjCZVSehplhqw7e_zQZv7m8X1cz9-TGtHCk2a6I-ARt6xHQbK_S6aDUPSKKU3hRaOlkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa7cb37c.mp4?token=SKhh8HEcvlGIIk5Fkey-3_n4TIh217FDUzTE3rdtPwsbvd0V8EVgf402Y_HDDGlEiHyoilk4fta1dniymVto2AtIUB9yA1Lqmw3roYv6Cb2EiEqar0mC6exLFUamFnbeiIHozgnbddS044MCY1uJRruuSpF5MgHrGl9knvHAJdo4zO2ZGcE9lYH3n70RWnp-6wc16KjP4_UQih7_AFGYe1H9eSgHDZnnWu-MhVGaBTov1xFj9BHs1EIiTYt7VJ8i_UQp-ew8llldw8mh8DsjCZVSehplhqw7e_zQZv7m8X1cz9-TGtHCk2a6I-ARt6xHQbK_S6aDUPSKKU3hRaOlkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره‌خنده‌دار هاشم بیک زاده از حج؛ میگه بری حج نمیتونی با زنت... دست بزنی بغلش کنی
😂
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23607" target="_blank">📅 17:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrIDqri0DLMJIM66YjG73krr2r5xNnykenNvjrjqPGYd8bsvLbsm1XR8qnO-RQsCeUAPj50uc5g9jTgrZhjd7flRN3RFw1dNaZIMJMk0R9fr9QYIV7TGrJEBiVVS4KHIN5DjbSHIxnUL1gOw-KCNFCpQYbdF8EhLdDVLShErBt29vHg4UPaV1OobwHgME097pH5ubnCOWLFvwfXMOSWWRgmdARCz9WFw-hvYnyVcPi_qmzCquhnKjjJ3mBAQBK90ZOZrgZniNSaYI_R0PF3Q-YREx_nPJOFI4cYS4bO1M8p_w_xnHeBrFzqTq9SyA7KF0ghlGMF7uUmJvgxdHNsfFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر کیپ‌ورد، کشوری با500هزارنفر با 7 سیو مقابل اسپانیا بهترین بازیکن زمین شد. آخر بازی گریه کرد و گفت مادرش چون هزینه‌ویزای آمریکا رو نداشته، نتونسته بیاد و بازی‌پسرش رو از نزدیک ببینه. فالور های پیجش بعد از این بازی از 50 هزار نفر به 7.5 میلیون نفر رسید. 15 برابر جمعیت کشورش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23606" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8LrUcNtCsxS3Pe77DAtKvXVeNtHGnFO_VYPkxvYOkJKbxoBYT9SL81Tw4mEG9WMvZiSzdYtO1TGK1tn1SCcHM9nkNx4CDh5FEwH29t012EI9arODOHoj8zR8airp0Ycp8hj-JJbvMmwmhtdIcK9zLeWC6VvgwhdcUV-rc2QIvzJZ5WT9uFZgpXjDG-gb7eYdzCD2ZFJSPzeNah2G4LjemRmm-3EtmvwdA9gcExw8GmnlX7DLA8BqkolaqeSFbRrhpM63As7wmWaKXpAmGEmvuW6MDH6DM7t-JbFkyf2cx-rPtbRxZnWOQ8FSlpgie2ieImpQ1jFZnXZeMI_zQOU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DueyEAycga7aTaV4ZPzeqFmOLE-c9sxtWXxt4swbtBitlMXEmnS_RD_AGEJpS0dEbeztBv3oMMmFafsCiKxDYdKRbbhrR5-GMNZcnlDcLgynEB3lzV6tuUM8a1OuBdO6sFCTynBMcTLdZUQ4WBo21FodhUsMrTby7-Za2AbV6zX0rHXO50hCki8owKEzwRlPAkfSP1kEf83G3uROCwg1L_oe5HDR94KIeSHfXnLmXlsjrAGFtHz1gl4X8LQaNq4Robh6akKVNb0jgMVpuGB2YUlPfpZ5R2tnZZhBzfsS7HJkfkNxZomO2-Ng6uipRPBWixsALrG-CtnpKbT6yQ5OVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23604" target="_blank">📅 16:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFrP7CwBB2KUyht3NjvMyB2ZE1UeYTdnp_J-KoTv-AhgblZUlmarKAus1e-0Bsp7INVqKJecYrK2P3e-0Wctg3YcLcGOGKQEFlF9KmJTlkgur6ioNz1aZaEuah1C_M0TI9uZ4sCXNvuJllHPHjr6TVcwkRcqeM7QtJapfv8psVo9Cus6sw3Ah30jrgK4RQ7Tql-1Mx39cVbGFGTaiOM3yMjG3JGyET30-CScz6nTnCmS4ypuqf_cjCGw3FB5P5wOcLyPjEb9ViMBa9JS2zkFk-tqDN7sdVeLEPsExYCl8MRoXipobvdH_KdiJblIb4cEto3J2WF-QeDTDFClMA2_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23603" target="_blank">📅 16:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqpyahrsNsngONDSe17Nt3jBMtVqxQrujpzHB7iUO1bxeMVSywzLNy1cOYSpcKc3I7SplBYXp7PJ9rGqs3zVFi6qw4D_MSmEHu6PkRBji7BbPKZkqFrGEMi758YWsKQrz2VIqPeTz_3RSJNr-FTcieA9d7Qb7mpCZaxEILSNwBkmJj3TD5uZQPSoY89-esxfgTCIKMmdJ3U4prcuWpvDB7G9Ma2yV3tyHeQ4lTt7QxPZEfHfiQP079V91_OUnMMHJOeSqtEU_o6mED41iWKuCvGN5sIibrLd4Wa5kJo920zF-stj7_dY_nX2G_GXQ3IUW4KV_z_yRS47bUsC_fvn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23602" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=YFEMaM-ON7fEcc05qEU0uPsJO3xayAQIHgBClIONj8nFO1-ULe9NdwfkG5KSWjHgk2cV-BzSMLl369RMkIHXE7Gmv2YPCbPjsl65gQfy-YPxKi0E1lku2cHAcqMkUv4_95bTRE2Y5ZJtU5GdXcsstWXEhttHUHC9bB2bH7okp5_c4GUzCt4UIN2KBvH6NDaQMVcntQtqX_Cjp3ctgN-QgCf8wiy_gUm0qfvQuqRDQ3btrD-uqmxpHjChjsQxPbhYVmK3QyoGCdkxSE2dx2qIx4JX4yKgnKMTcb5ipWy0npV_1rV1m5_uNx1mToxlfPaeOl5yJoBFcMkMjmADGSKn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b865e790d4.mp4?token=YFEMaM-ON7fEcc05qEU0uPsJO3xayAQIHgBClIONj8nFO1-ULe9NdwfkG5KSWjHgk2cV-BzSMLl369RMkIHXE7Gmv2YPCbPjsl65gQfy-YPxKi0E1lku2cHAcqMkUv4_95bTRE2Y5ZJtU5GdXcsstWXEhttHUHC9bB2bH7okp5_c4GUzCt4UIN2KBvH6NDaQMVcntQtqX_Cjp3ctgN-QgCf8wiy_gUm0qfvQuqRDQ3btrD-uqmxpHjChjsQxPbhYVmK3QyoGCdkxSE2dx2qIx4JX4yKgnKMTcb5ipWy0npV_1rV1m5_uNx1mToxlfPaeOl5yJoBFcMkMjmADGSKn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جز‌ ترجمه‌های‌ماندگارتاریخ‌ ایران
؛ پیاتزا میگه به خلاقیت‌توحملات‌احتیاج داریم؛ حالا مترجم: سرویس خوب میزنیم تو دفاع باید عملکردمونو بهتر کنیم:)
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23601" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
#فوری؛ کسری‌طاهری امروز بین‌دوستانش گفته مذاکرات خیلی خوبی با باشگاه پرسپولیس داشته و بلافاصله بعدِ اینکه مدیریت این‌باشگاه‌رضایت‌نامه او رو از روبین کازان بگیره راهی این تیم خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23600" target="_blank">📅 16:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiuwT8arFJAi8KzdjBIGP_9ThRAbqxmlwinw3PUdD2XCwKtBEhSLsDQx035dWDj1vn0xVq8_RnlLByCOdSkoB-fkXtdx2w4P60N_O4aIHGAyZXIGyMHC7hM-YlOICTOdvy3iXImLmnW4KaKT3wJujSkq2K2PFYyspYvmvMwzYLoSLt_bd23yh5RidrABKE54CyaKxKwpD8BsnfVWw57ucIKinRA2Qb2QRPOxnJ7tjIgulRV8au1L89bw_tiHZV8mOnJWMwUF3yDUuuPMTChVmOislo6WLxcHFlzb2gJ5RCGtLx9k9aWUjcBy2ZS9kj-VDGa9ZYSCvNcLbROaAeNXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
تیم منتخب روز ششم جام جهانی با حضور رامین رضاییان و محمد محبی از نگاه سوفااسکور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23599" target="_blank">📅 15:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPOoTsTC1Fttr8b2hjvR7GgbyEY261WBSLb_k0Y3hiTl3hN-nlAX3g6Cm78ImQnv-9Xf9vjlcdmC4_EdvnLHstXQRbLNpU1AEXIMqJqTPEI8E_lIgDAjD9xx_u5-RcQX0BYfYO0p3SJ68JkEtBgq-W1TxqxWlcixHWs0thK7Fb-eDGcRRpIAqg_IfN0ipIpRbFvD3s280zn_j1KprXMiCUqnyu81fB3ZDG0YSza_rIDIaZFBaF7pZoNq7BEaIqZZFmThHqv6L2W1em3wLVw7yLlOrn5UrBfO_MxnpxrONuJJhWT9KfBuzewUmtF9fIX62qoizwUYWTVuXrMWGKUUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روبن‌دیاز پس‌از ۱۸ ماه رابطه و زندگی در عمارتی مجلل از مایا جاما مجری‌معروف بریتانیایی جدا شد؛ بلافاصله پس از این جدایی، با حضور دانیلا ملچیور بازیگرپرتغالی فیلم‌های‌هالیوودی مثل‌جوخه انتحار و نگهبانان کهکشان ۳ درجایگاه‌ویژه‌بازی‌پرتغال و شیلی و تعاملات این دو در فضای مجازی، شایعات رابطه جدید دیاز دررسانه‌های‌بریتانیا و پرتغال بالا گرفته تا او علاوه بر فشار مسابقات، با حواشی سنگین زندگی شخصی‌اش هم دست‌وپنجه نرم کند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23598" target="_blank">📅 15:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=Dv-bl5SkDnZmrbio-eVGn3l0UmIe0BUVYqSB12_h4XyTqFgT73JPQ4ebUP83tf4BOaR0hK8By4wsom2B46_6vAy6ASre2rGKs6M_iTPoF8pYUsrM9KEE-cFNPy_kdqaHCnJgeE4AylZiw07xlXRa-qKXNwEeNvbQ1Hg6Eu6wu0TMeEVRS2dw7GPPT9pbeQ_3Ntmoc-0cIdhXUzMqVFQzi29L40SEoOaaQNeu4ywEtmPjv0GoCJQARf4wmRR6YTeKjWaQvYCjTzLa2XkEaOgRe2J3DiQsFyRykGgqIxLHZSKGbf7Q6dKmLPhnh9chRe-UuVRsixWZUVtprZuQ-3gNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17684a49a.mp4?token=Dv-bl5SkDnZmrbio-eVGn3l0UmIe0BUVYqSB12_h4XyTqFgT73JPQ4ebUP83tf4BOaR0hK8By4wsom2B46_6vAy6ASre2rGKs6M_iTPoF8pYUsrM9KEE-cFNPy_kdqaHCnJgeE4AylZiw07xlXRa-qKXNwEeNvbQ1Hg6Eu6wu0TMeEVRS2dw7GPPT9pbeQ_3Ntmoc-0cIdhXUzMqVFQzi29L40SEoOaaQNeu4ywEtmPjv0GoCJQARf4wmRR6YTeKjWaQvYCjTzLa2XkEaOgRe2J3DiQsFyRykGgqIxLHZSKGbf7Q6dKmLPhnh9chRe-UuVRsixWZUVtprZuQ-3gNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
یه عینک بزنم تو برنامه زنده جذاب‌ تر بشم کسی زیاد توجه‌نمیکنه‌بهم؛ همون‌لحظه عادل فردوسی‌پور:
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23597" target="_blank">📅 15:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKCOmMMs2dHaO5G0CHpYbdzy2sUdFhpAfc182Lip09RTDh6BCogr2vc3F2FniiLW8-GrCl7F6uqGVpOh5CJlj09vG82U83EVaGWhJi0q48hqJ2U3uFhVnrkdixfpp9C_3Q0CBxcPhqnJ8N8FufQ72PFgVWKjz7ein49rQYXfM6IVS_Hu-rFvgpGEc4SoxvfYXHQtSt6ztjVXT_E8L_FgMLZDLpMss9R3CYBR-p1eQgXJQPvPcBDA4t8WXTAwlzy1BjhmgrllZEC3_Ul-EQwBgbk6387x5UtbRRzoauMWk4uqvTQ0Jt2O4Nrt5JpdwMDpwTOmFCJMfmepBKEfDXP7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌نشریه‌فرانسوی لکیپ:
دولت آمریکا ویزای مهدی طارمی و مهدی ترابی دوبازیکن ایران رو باطل کرد و نمیتونن تو بازی با بلژیک تیم رو همراهی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23596" target="_blank">📅 15:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltLHEQ6fHlGUURaYJrEvO_0StdOvUcB6vqkcgMn-aQ6TNDPedgmDgcyCIT7DQ1Z-wH7HULnzvfu5xtZi3OxrLaspHsoTWHc6rxd17denfMDIXnOf8vcPaAb-sTOOZ3iVvx6Oh0TXkEw7X86K39DMd4V--r-V8illAJUyNBlGehMVxzMEqKA4FLZHQnHBR3lBBFh-4D-TE-dcxuGcUj_XjVSMPaFEcRDz46-pDaOLMozq3cxedBqkDZVqh8o-GZUeLsW6V5XAZTZ2QU3eB7HoeReyYp3tobS7IDnkDzHtBcMK0zMY4MsQ1hv9B1P613a0uM1aiZOXvHUSv5LeXiJMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بااعلام‌استقلال؛ سهراب بختیاری‌زاده بعنوان سرمربی جدید آبی پوشان در فصل بعد انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23595" target="_blank">📅 14:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fybfcYvGBPC5c2D8L8RZD5MX7pl7JRa4MtF2E6syDwV0RNotL1qfLQG5r3Zr-ZTQyLVBR3UzNSJxfraNERajwITxC9eDsQqOoDK884G4kN9CmTIWNfTQ953GTCPc6Cdc74-MELZ93yizX18CoelZK6zrUmEhTS-Vvk-BbMQnscLDqynHaVyTUULSb8rlNAOK3qqUXxw7pyjSbW-9S5PNHNf9W3FCCH1rVv4_eIuo-FRyIBJyPOJVLnsVKTD2IBkgQ7NpesZMRzAnUcX-WGGWKGpZR1cvUDEGLscsNHZOH03I65sGAWjvCp9sznlA17iGfX0wtDvPTYNIZA_KeqDyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇳🇿
بازی که مساوی شد با اینکه نیوزیلند ضعیف‌ ترین تیم‌جام‌جهانیه؛ ولی کاش تو خارج از مستطیل سبز هم همه چیمون با نیوزیلند مساوی میبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23594" target="_blank">📅 14:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXjwDm61oWCKtzPPzYZTIAesvbrFF3px3J-W3QiRtpjY2cpTxhREPg7AnZOMyIWeBE1sZ6ulWfng4eDqdC4N267AkysKq5lzA3P5S1bPwKMJp2Hbvmfgj53hWBaNCFM1yTdZNjtmZHcrV-5ONxh_dE-9bSssTH8fzCfC92fuWd1HI348ZIwjA5Cgb96gISyfSS02L-7Yh8w3RmR_MwamNlTGF-KGy4Wvtoi1wCViN9O9314SvXduL_LbwRypepDgEu9jxFTkoyvQXHgUsEUIOjXkGrbaxy4UKsCCLW4tLS6Z0315KacAEbJFBd2lvcbhAT0ZJ99IfUwDb0RIvkrhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23593" target="_blank">📅 14:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bomunTelsRktVq8AhD7fxUgh81KiYrZr5V_0DJLniQeMsBa0J2XoBl5H9-SRH9D_E7q1-bHw1v-4-ZJ6jSiU4BgnuNG3Z6CqXo9b3x8YuWcAonVASPyrF3XI90gQGa5dEEf_u_odG7BqbmzDGpdvmGSQT6_vJPlUCrhPhndpOr7KI6sm43ANDkAiZw7wJFM8mlJ-T3qWMLZQctWdEeYXZRvAIDwQSa8FYTQRwePB6xb_fIjruNkYo4VS3xj8Oe8Q_XPhr9hwEh0nzxrqqj89O2Y3E5hGsWyGZrRFpOfQsZcED7zRlNgx8yAGNjzEcAeLbqgfKNBw-zxM06c5gmYwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23592" target="_blank">📅 14:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSP9HeNUJWUIgiApmZyCzJc0Wthpwg33bzVRj7AhqMyGkTn-gdj8HdGOJW6-jwkdkvE8LuftrPO3WVvHuKNk3LPl3oD9ja3ArlFjCKkcPqilLcdpg8hetDDCdBx-Azo_RQARgniFvGcBAyCLQzxf1m19jfIjjVnbWUQtFWgcjzOGqagJ1bd5Vp8SNXrVPYAfVMYqRmmiM2bw3GaNUhMmqkg8MXAqHHL9jUb8fDaRUwQKbsKWcB9rcwCL4jSp7N3oSApm0tQrgD18hj4BNy8fW-OHEcnpb_L8-ME_E7Jbm9qA7Nhq2CcATEuQeJySyJGEj74xzeNWRmvO-_JCq2tndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23591" target="_blank">📅 13:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=UylNnFcZLCNiSWE48ZWkZZEAjwB4ek930-lO9Q7D9Ql0dDIwxFSD73GKUNxHTWTRywhyI3j446Lx3dpXnnurHYrm-SEFynW9ItQtX8ihRxRqH9vp6COP0ZVbBFsjhJsW8g_meKweT7r4k61AbPOka1WRJcSov3VTRu90Hqkzz3Z95K7h0xfxzaCxOCS03fgV7xCVvId95A-JylU2v93zCrcmcdWJ9o3OiSpVccbpyVdSoTJxCSGnBBEVTOwYrIp19LvdshfHg5-SOZcAwIhb1skmji78QR00KcnPoF1kGsWiHGg_BqA94lYOcLf4eq6umVdeERgRfORY9jfYd4mECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f5900223.mp4?token=UylNnFcZLCNiSWE48ZWkZZEAjwB4ek930-lO9Q7D9Ql0dDIwxFSD73GKUNxHTWTRywhyI3j446Lx3dpXnnurHYrm-SEFynW9ItQtX8ihRxRqH9vp6COP0ZVbBFsjhJsW8g_meKweT7r4k61AbPOka1WRJcSov3VTRu90Hqkzz3Z95K7h0xfxzaCxOCS03fgV7xCVvId95A-JylU2v93zCrcmcdWJ9o3OiSpVccbpyVdSoTJxCSGnBBEVTOwYrIp19LvdshfHg5-SOZcAwIhb1skmji78QR00KcnPoF1kGsWiHGg_BqA94lYOcLf4eq6umVdeERgRfORY9jfYd4mECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23590" target="_blank">📅 13:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23589">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZaQjU6r1KYknpT7Sj43-WcMyaZP0UGXdWdluby2ajyAVPuD4x-VIc0c1IWUG-025LOG8zpDuziBd7DtbdT1Y0u6diNO0AcooaUl7CTwjyRqDXgwhAul85CJxIAizz3yIvWIZvWkGC-LyM3utLAVBnePv2TS_YsxR5y37Phs5nwN0HuGxZ86WCJQqDNwxp03TNhmBoZn2VqpkHxlPcQ04dE7-hS8T29Lzo0_qBwc9FvYISnJg7VBZ7diKbezHnfE-WTzw8hU9oWG98jQX66asYad1zUcBfYTezNQJYi7lmPhcjvdgmHpESr4G5nii8z2fwhuuX5YYRsEEENCwPX_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23589" target="_blank">📅 13:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVLBGaFGzu0dkYAMwfzd2Ra-Yt7ZYBgAzk2IRsfwtBDIFn29JRXI-K1hrD-PirQAWgYLagSe0j1NN298FRUuKBcArR2sL0ry9Mve52NJQbpIEr_ZjHZ6ipXs8YSAxH8tDrrrJ7xAZnFvKQYBf2tm6wIu3l0s1lgtjKHVpNomPWlhYL99s5xgoiRPc2G58-kpNU8Ia6w_9IKWdALOP_9w2T-LXeeeP5XbUAkogvHrc9mW4fDNRNWonouup0LngH1SkzlB6xgt4nJIWz7V0vFIysRRf_SqhNcEFUYVETwCaHfK2nHmn2T48DIZCIIC_Lc8msRvBkXoDS2DBWBhKKx4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دهنت‌ سرویس پسر یه حرکتی زدی شدی سوژه همه؛ حالا تیری هانری اسطوره آرسنال دیگر کارشناس شبکه جام جهانیم درباره خوشحالی بعد گل محمد محبی گفته فکر نمی کنم منظور بدی داشته باشه. خودِ محمد محبیم گفته بخدا فقط یه خوشحالی ساده بود که اون لحظه به ذهنم رسید.…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23588" target="_blank">📅 12:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFsDRpjiFEGfLYPjxvkUyH42G6nljz428TYhcEvkpF2cPF-hfNxwe3sR4rhWGEIBY0E2qNqbl2DS0YTTlUGtQsmNwZdNAkYaAz8i8D7RJhMHiYipCJQBmN8pCE49QJBw1IiGuPgIHRLDQKzkQzSw2yi7_UR-WRPc2Di8A_F0Cmra6bEVHDBqBKpd0QhH4b8HRe7N8JUXLCojJSTwgO4LFCNI5gOkyXAZr8mqEc3SeNaDHY55En6yn0yBHBFgj88SY6bxNPH67lUY2TbqFn2RMk4dALjOSBpjkhXQ3xamtUI8XQlSLu1LJh-embDuDzli-Z_iCWDor9Y4n-5KVTkUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23587" target="_blank">📅 12:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dafS8tqQRmoIwr1jKo1P_yWIbmqW2YR6m2aOlbM1rIfrAGmACxmm-ZKrO5n4gwDjbtPGZHecknYYt383LqvzS2zeBTFmcPEeBlILLg7e-EDzlCkAQ38jVOU51uwDONc6ZW70tB0gl77VHG6bl6V_HtRfA8NjSkRcLE2gA0e5W6HOey8HEaa1M_iIK5FZ25hP7rO13jC0iFlAbDX31S9fZJjgwhPGcXBSBRolbMYGJXcxcTKwtjj8C9C9p8aWaCiAf0Ld298cXpZx-Uyr5dzlTBol6oSAQVJkZQ3y-2vmQJP9XDpytEFkP9FuVMCs7Xd0unnVHYRLTZHQaQyrtsPulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درباره وضعیت آریا یوسفی، محمد امین حزباوی و مهدی لیموچی که هرسه مدنظر باشگاه پرسپولیس است و مدیریت‌این‌باشگاه مذاکراتی‌نیز با مدیربرنامه آن‌ها داشته بزودی اخبار تکمیلی رو خواهم گفت.
‼️
آریا یوسفی جواب تماس‌های مدیران سپاهان رو نمیده و چند بار گفته یا لژیونر…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23586" target="_blank">📅 12:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIGQzg5Tsm8DYqVjEPYQS5B6nAb1M3HK-BgtkaKPtDMKMDGOWguRBCuwEkIs1Y6_MycKpyl8H-5eu6yBBnZ6YAKNomC0RfMo1XXs-lafnqvOREtwViLrt8hr5QVBA1kU9k4kSiHVnO7HC2EVk_g-Z450nMK35WOLucEy2p6U1yerPmc7RfUU0yATpzpNFpkUx5qVt521rlWtyJ5HAG77U2--RGqNq0rtGdXubUwK4EP5BaCnx4jfgWV2W6kzAlyHxZwOTb6nOeP-TunvR1h8GGYSlqjSlAlQUdAsrtCAe-79BKHqwuVqg0twvY4qXUy7ydwjlpCMc7A7mvV68_w4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23585" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdsHfqwhCUk81vl6fO-qFFrPmCn6nomTQMjltBkynmwsnTQPAEP3smNipa6MfPmCKffcLVe4A_11r_X9f5YMiUL_HTwM7itPy2wHP9MLwVRoO1fI6rGJOLJxlU1jA7yzovBnlyvOJ06oEqjAdymuoljLMuMc2Nnv7kPxC8M-X4k4bGoqQQ2o1XbAXWfO49q9Y4R5qukq5vawWaTjKMbD3n4YwTnaJCxnWRCHusS5xbGNm-j2KUDAHm19wGwzomyrYPPIvQe561Z43sJpikRrOurdvZLodbK2wDuCH8aow8pL26bCnsrldqLtzaM4xsNOwKoZaqLFtByp5Sbz4bn6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#نقل‌وانتقالات|رومانو: ژوزه موریینو شب گذشته درجلسه‌بامدیران رئال‌مادرید از علاقه خود به سبک‌بازی ماتئوس فرناندز ستاره پرتغالی وستهم خبر داد و درخواست جذب این بازیکن جوان رو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23584" target="_blank">📅 11:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23583">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚽️
خلاصه‌دیدار امروزصبح دو تیم ایران
🆚
نیوزیلند در هفته نخست رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23583" target="_blank">📅 11:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23582">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKDE0Xa78VpZjAaliMMjKyqCONaEQjcLv-x_xl7aXuFkHu8-qTo0cL08iwKeq8YofdRX6q_i_d9ETVx6gf0csmwtuRPowr_1PWpErqjZVyHqY-Vreb7VW_Yoislt-VfZbysua4s4_H94JrWMjaCSWR2zfcD7qP0byBss-f1V6C7NYlYmcRgglYGhlPSDAhD_6wxesBfBS1SeiuqMKss9hVD_2wq0OfWSta_wWcFYpw9-ItIxmqj92KRPkFL9zGLLkflF6IRgX_z_SngmERLfiBs8GzRspA2wRu_LDJ1uhi0zXIHFdKEHj097ejE86F4eES2ufBu1IQb8jEgHy1tUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رامین‌رضاییان دربازی با نیوزلند درسن 35 سالگی: ۱گل، ۱پاس‌گل، ۴ از ۴ دوئل برنده،  ۲از ۲ دریبل‌موفق، ۲تکل، ۳ قطع توپ، ۴ بازپسگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23582" target="_blank">📅 11:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23581">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrjjycoJu7cX6XExywzDq8a_pTr_UT5kafvgCkEZfgTRRxp5HjvOsG_o_5Gow5IQJ-XyXVUH2u4WguTu6cgYybNHzOxrSFVgmG8m7JGfSw3oHzdPKxrBIauQbOlztdlJ1aocxjexGyBW-_rBC7NPq70_Exoi6naQHrs_8diWwRJgUzWiDANQ0gvUXnWjER8aqsQnOeDmvJY754DKJXkBzc-lCnERKLxca3t7OufRwGHHWKRRMyIUOeKx1CTRk8fOS5ypm2_TYRqDp0tb5nWdyMxR6OFTvBxTLcEw5WeEKl44INyUC0gi5z2JHNXQQLoW1MfUPU76mV91NxGWp2orfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امیرقلعه‌نویی‌سرمربی‌تیم‌ایران: میخواستیم دو شب قبل بازی بیایم آمریکا، گفتن نمی‌شه و فقط باید شب قبل‌بیاید. الان هم میخوایم برای ریکاوری بیشتر بمونیم لس‌ آنجلس ولی بازم گفتن باید همین امشب از آمریکا برید. ما مظلوم‌ترین تیم تاریخ جام جهانی هستیم. ساعتم هم…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23581" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23580">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=KP1SzL8ro3Yx6E7g5ALXmXWk9Rg5UB2tRudxJj_xLG-DlXmaUI9Qbg1SO470NqZPqBxJj4svlZruSdKaF6DoktGIwMQNR0pcUdISrm0KWLchSVhfCnAHTwm-wKkFTpPFy_ld8VdD4qCImgDSTikp3u2HMcFBO3T08FjRgwAOJ_cJ2d8bUG-goZIFJlUaX3AiA5sQRAv7H7PQkqE2GjlWTDpXzFyEBmfxdo-42LO9zbQ5PFM3FNNFYCfp_79ISWMmi8FhfaulFYSay9WQEplEO9qBqCSqH5JQpRAZ3xONMcYslbOYoDtGsOX3p0YB0KdRLId8CVoY82quRQiaDJU-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc4a75ce.mp4?token=KP1SzL8ro3Yx6E7g5ALXmXWk9Rg5UB2tRudxJj_xLG-DlXmaUI9Qbg1SO470NqZPqBxJj4svlZruSdKaF6DoktGIwMQNR0pcUdISrm0KWLchSVhfCnAHTwm-wKkFTpPFy_ld8VdD4qCImgDSTikp3u2HMcFBO3T08FjRgwAOJ_cJ2d8bUG-goZIFJlUaX3AiA5sQRAv7H7PQkqE2GjlWTDpXzFyEBmfxdo-42LO9zbQ5PFM3FNNFYCfp_79ISWMmi8FhfaulFYSay9WQEplEO9qBqCSqH5JQpRAZ3xONMcYslbOYoDtGsOX3p0YB0KdRLId8CVoY82quRQiaDJU-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
امیر علی اکبری در ویژه برنامه شب گذشته جام جهانی به این شکل انتقام همه رو از ابوطالب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23580" target="_blank">📅 10:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23579">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjbzB6bN_35TUypC8s4BSaDCSBgGNNyIlTaBE_x1HJs0nWc9B-89ML6i--o2QvHTYxKPMxpPk6-UjwogW3jduV6erAlPe0b6X7Mn5K8ITcPkyUe6VnE59HgUlm-fKm1CwFFR_ZtKkzf7Ha8nWW3e9AoQhuOOnMbw6RoaV65-H-JGyhOoCHgU_wJmHb7iHxgZ97clLg7wHeBcnOfXmVukXTxTkIKqDdumLW4y6EE4JvTU9sMXaidsw-uSBnW9IJVWf7Y5KzcXBL3tcD8XmbSAC6OwGx5gWbJAQ330CpsqY84lvRdILfKBaYz_M9r6ubhZcH_X4WnWFEU0uEhz_FyKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23579" target="_blank">📅 10:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=YnSWVwBCVatoPMHC_5bMhrzIW5omvtr2Vo7axx84slbIcoWS1AUXbexg8hyWlK_f5c5KE53gflXbdhiZ58EU4XHb1YD7XzgwJt9uJTarw6QkOU1CRMYc4bAoj7MqL2jjF6jB7T-ibkW87iggyJKBDo7c6_TDQQEXWO5QSVVI8q8Cd70EoyEOJ4xxyH9wAxNRS3Qp_xW-ALYw_XMJ8A6m6IYgC4w0776-E2HXBHtpGNEcHtlqo6tI8Vv36of1HeptH91Fv8CulFjkYbQBIUUJuN1F37nwQcVlI4Txv5OGH96K39Yj-QnAoe4fHRn8LSN3R1iGrOYt_2opBE0fMp-meg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ea73ae1d.mp4?token=YnSWVwBCVatoPMHC_5bMhrzIW5omvtr2Vo7axx84slbIcoWS1AUXbexg8hyWlK_f5c5KE53gflXbdhiZ58EU4XHb1YD7XzgwJt9uJTarw6QkOU1CRMYc4bAoj7MqL2jjF6jB7T-ibkW87iggyJKBDo7c6_TDQQEXWO5QSVVI8q8Cd70EoyEOJ4xxyH9wAxNRS3Qp_xW-ALYw_XMJ8A6m6IYgC4w0776-E2HXBHtpGNEcHtlqo6tI8Vv36of1HeptH91Fv8CulFjkYbQBIUUJuN1F37nwQcVlI4Txv5OGH96K39Yj-QnAoe4fHRn8LSN3R1iGrOYt_2opBE0fMp-meg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23578" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23577">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_DAykYFw6FuC0-xlpkxc6s4nswWdpmmN01vlcr6Bbj3Z8jnj_P9NPlCVheiI46Xhi1APzPxK3zjT0eKVpTG6TYtEAOGtsdFJ77FkjvNg4XcyYCfc-mnKdVIZvpZxiEHwodH_n4On39fv7Ogf90MdfsU96WDHQYyWq2y3CXcCFML6oMPFm7nSc8kLD6u5zLO7m-3Z7YMWerHo2RtFEpgGMaM4rTpW2LPdgGdoB52OQk1Ka-UboAgbOKZHPfWGhvCJUoijKNvGzxEY_dS7CXwJjDgN_rBkgG94z-47M1dfgHoVvBFxr3NrQkL71p-oMkJNKa0JeQVm8yGOpvvRSYB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شش تیم آسیایی حاضر درجام جهانی 2026 در دور اول مسابقات‌شکست‌ناپذیر بودند. ببینیم اردن و عراق امشب‌وفرداشب مقابل‌رقباشون چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23577" target="_blank">📅 10:22 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
