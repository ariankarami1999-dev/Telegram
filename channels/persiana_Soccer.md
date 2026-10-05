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
<img src="https://cdn4.telesco.pe/file/mGbi62DMHpc2Xv3XvVe9665kE3YYSNsnxaA502byat4ODDRvX-BdW6BflB6rNYZJKR4r4Gge0qDxe_TOfDA_-jcp1RD3RwussQQv3pzVf1DoqnL_4I1wPF5Gd-MLvSXBwq-dNcYjRSLfBPriv4nSsJlVeZ9uMREa-K1yQnuKjaGyFwZWHd1zElidrAbLnEwt1ufBHSKwhrQzyMY0fQcUlpba9J9yBplKSycPj3-wQM5HG92CrYetM-A-H7Bz8vVqsQWJyU2iqpK0HZq885t2ynh5I8uBG6Q40X31RRrHTCTmf_nFWf_-ZYn8G-Ugt5UBRD-mNK0b1gnh-9aTyqp-Ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 480K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC7Ykaul3nWdOBSIKNOH9Ava0GLsKDeF8SSlkgEZ0djOu4_3JqtlagUbpFZeJsEBYG7Ed0kpM18gmr4TYzrGjJwxOpwwwvSajKV-ilHTEhTqoWvJYdWH_jVsU3V3W2Dcn-wyl11XvqGtSmN_V6i0TrF_EB02Okadehr7rPme74SMvS6YYtdGIXakJB7ooZDQpkZaNhZiSbBHAECFVeFrfsVJvy0wSQX9M7RRyxLFZKHZ2LfOcHXoa77hlmWeb1yGh6MqTRYWoLwgw-lwISGTH66my8bUt-wADkK_xySIGYhUbVbJMUoI4E7Rfjo-VOcfrq5wFI7Kf5mwObUlf0HZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=SFeDzZQ0Dl89I8R0LNOm-9S-KySIb97QJyAbVxKv7jy4g0g679ARJqiTjKf00-GPCbzjdkT1OdJrlXrMtCIiUetQe6-G1K4UDHfttlhSPPuJ28bbYNKwrW3aIOgWqAe0HyzFL0UYT272gOLuAR6ICOavsq0pGq1_7UtWdWXmjK_Te4FFCqMWyM4BVec4NCn1Gc4YM7-w4yjaQueB3fPw9QC1EZRpPzfBN6YXIiFqtA_0qURqyuueH3lKpNSJzm1ILKr4Ip9ru9Komc1fHY3ngywLDSjlfz4LihG69Jc97gZcJsgRAGePeMSYVdioa9NFfqUI_tC8emB9kAHUCjOcJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=SFeDzZQ0Dl89I8R0LNOm-9S-KySIb97QJyAbVxKv7jy4g0g679ARJqiTjKf00-GPCbzjdkT1OdJrlXrMtCIiUetQe6-G1K4UDHfttlhSPPuJ28bbYNKwrW3aIOgWqAe0HyzFL0UYT272gOLuAR6ICOavsq0pGq1_7UtWdWXmjK_Te4FFCqMWyM4BVec4NCn1Gc4YM7-w4yjaQueB3fPw9QC1EZRpPzfBN6YXIiFqtA_0qURqyuueH3lKpNSJzm1ILKr4Ip9ru9Komc1fHY3ngywLDSjlfz4LihG69Jc97gZcJsgRAGePeMSYVdioa9NFfqUI_tC8emB9kAHUCjOcJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX-HSAy8DACTE-tXoitNwuPbdDFzIvcsPK2mkhMNsd13ppW83mklRAb2ue_8HduIEYrd5rM2H_3gQ4gh78s66SAr40CFhQnSiN2am9WaM38PwKg70lyxEPdgCiuZgPBJKThnf3arNkqM7KST82wuLvvoxe_mOB8VH_oRJaCMS1aO5on1y_Uz2ygZ_OidSsh-Uc2mqxAmNjc1apdSDvEjPiC3YuHY0ujoqoBJPWsFrmn-C7mbQkssOdgDWp3xqUPcjOcA1FGON3RxgNrIAIu_uySBoJJg7mCytqhnWwixPe2ltn9-Lct6EkFS7UWKXTdmRnOSNVLSpVviDuS4UBmSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJSr4UaCqDlAwg77ETAGWXZ8pvwEMuyHvkzUZPmPcGtD1LvQMlakIm60cAppJOsp6bmN484FyAsbUV0Rpqtdcz-1O5EhA_HtLs1dZwmkRoRPuVdTUUHqLAuOW9Cky2tmhJtSmMMqYhAzOkifSJ5g1Hi2F6turD3xkYTRpAZLSRhMtcFeJK6fhC7VlrrpvYeKM4xQoyZ8rprHk0u_SFfX0FCCf_c2mo1DrxejkVIGgw_aKkRNe_DqDXaKjFYMEo_eK7v8NoONAN___SV-RBXLxlOghQ1ASBAGbENaQOH90UoZtBEpshROC6xF9LYqNkqnBf6K_buweQrPmtZisZD94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJoOEhx2JqDllo_OTrcKcsC4oD3bOb59Sc923qgGIkdD25IhyF0pYrlphVW3cD3KSU6rizQZLZ-N2oU4-SyvumZ3IMdWyvWu4QCkwGn2HaTTv_mzavffreRGQjtuV4yjjYy9K4Y8C71d5MXykj_qscmmlEps3X_nh8RhR952-R5GbHPxa3z7cJ7cDzc8ZPDeLvcckHToDCjcAOCJgDO_NHi-DDjm1bgmqFmqyf8-KML6rnNeseEY9culN7OSJo3rx4BMkh5XT_XARVpiWTEgy8g2rD7s7IIZJ-8JgilPBEemKSEr2NGGS8jOw_ooWxUCBiULjTpfkM7lA1pAdbjzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=hM0LwubBZlHb_YanRUcm8sDPyfCKWCH7yB5Wx-2QDrGquumvGl4nts4aYc3-ep3eWxmIyEZt13pR5J4oHRBTmJnymg8ihk1h3W9s1sKtndGPvp6-yYt0NnuzPP-Rkv07x03Z2wdO6Ta0IV3fgNTDBLQ4vK3I925CtQNcdOUKizZqJeaBYnjIBf7kKhpJd_c3l0nwlfx46c-3aYgmMa-t6dQP-RRv-SIoCgzyosy0TqeaZTVinGcLUSQZodaLln5tAGOT2Nv6osRs_AzZu15nDnjoYT1_Ofe94TcKn76bFxXaVIc8bf6Cx-1ob9NbiQgtOgeFxK2HfHlC9uFQ8lGsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=hM0LwubBZlHb_YanRUcm8sDPyfCKWCH7yB5Wx-2QDrGquumvGl4nts4aYc3-ep3eWxmIyEZt13pR5J4oHRBTmJnymg8ihk1h3W9s1sKtndGPvp6-yYt0NnuzPP-Rkv07x03Z2wdO6Ta0IV3fgNTDBLQ4vK3I925CtQNcdOUKizZqJeaBYnjIBf7kKhpJd_c3l0nwlfx46c-3aYgmMa-t6dQP-RRv-SIoCgzyosy0TqeaZTVinGcLUSQZodaLln5tAGOT2Nv6osRs_AzZu15nDnjoYT1_Ofe94TcKn76bFxXaVIc8bf6Cx-1ob9NbiQgtOgeFxK2HfHlC9uFQ8lGsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZyv-jiw3k9hyeyGdGPhfL7hy6pv0zFb5_QdqOEB5-98OT29MlMvKstwIG2_7A9Y65-t_rrRz4UJ2p0nG7Xsf5Nsha0mmpeLc1uFDhxVFkAl8WlYTVLn4tuz3ibbF3XJHCaZrzkMFMpxJFR87w-vgIhIW_sdr9N-px78RpLgBQb_6eRAnlSpEKg2zE2Vml1fnLuncIQ1E0I6j-Nm06Q2n1Ax2Ij2OpgXgPV4xQo9uKwK5TnXNhCDyX4yU7nVCav5h4aItr-v_zAWzYiMHTS_NcgqwsI0LJm9aSM7QkrTFlu5GHcUEv667znI6SMa4IjSl5xyRL8qsItVKJh6E-6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31037">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXIm8oMzLofXt2rX48Rpszrn-ItdeRKjb6aVD0bNSC8lXX8vUwtUUUg81KJMdMlSuSI7lJSWN11MPUMM9SSI49-EfWJnNeWKI1HseQzbP3yhYg98QEVehXI-7UuiNsb6Bs2F-Xc49AGFhiac5ffa_MbjHmsjHuN8v1AEu1usLKjZgbPu2ygVwNz8LauV6ASm2g699G5klNwKGEMEVYPGDHSG89anlUGlhXkw-Z2EuYKdQwIfkxbQJrsNdW7xiZLXTeV36G9qkpH9SA9eP3c5xQw_G7defGzq_gTaDC3Vcua39aRdOflE1H-mz469Hy7R9k5lkyyvQlURGijmJEzYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/31037" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31036">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snfilwBHiYZJ3ZTUVXXBZno1p7rtsZxohxBQ_Tso3DMG5z1vy41uHni-EEMIwl7zCiRRW6-L_4Y-b7IABoN5cj-LnImXq4Mn9-XOzokMBKmVeKrL9u0Cx0DTKkDi2AH0XLLI1Tt9obkKqGS7Dbb0jgrNTK8XrxN06f8cGJCbVVmM1hONWfe_pg6cMAjiNZ8257m-taUuzNN_lPo28aS1aBzjcW3360lO9VRuGV2sx_gN0i6Ta9kCMyacE09KJ43TLrCANxtvg_6nUkvs1lz0vLTPMpVQ3ScNTTvmfApZgR76QjjJ6r_0eEonmMM__2My8oQ97YqkwssbRdBq3n79Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
هنوز شانسی بت میزنی؟
💖
فرم Vip امشب با
ضریب 2.25
بصورت رایگان قرار گرفت
✈️
@best_form</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/31036" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31035">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvB1jK8mBkjeHzo2tnNoJ6x24z_pMsHr94VSM_L8dz7erWUEvwkFD9b88h9eChwzYcxrokiXI71NpUdPtBGDFBmkCclRAD7cDtC9lCFMP0DvI7344pAFu8J-vcrLG_AZYix4Hp6ISltiGxXyfbEzGZ5SsLAC-LEgpv1zViZqnsqxgppnJvlZ5nZcGIPchPLS4750NUpmPbCQ-Tk5NiDbs_6A65aJ8Vk4LFnU_f7MbPN7CP0BJ9u8MoDwkrrJKHefQofvcUZojqqCrMjI2pbPXM5SP2sWkC5p8gDb2djm9Pmf2XpVSbheVPO41pbX-Hr9uIKMDfIhhPxodfscCTiz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌جالب ساغر مرادی و فاطمه از هدایت یک میلیاردی سردار آزمون: این کادو برای ما خیلی با ارزشه. سردار همیشه به بانوان نگاه ویژه‌ای دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/31035" target="_blank">📅 19:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31034">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFrvmyOFaodmFAgucb2wAw_1ShzbOPSCxsNQPl4gjDfVlkZQ2mZc079XBMfSgmtsvWLJc4m7pmc1bV6vDgmYkr7UhhO5J1jmmcNWuK8Pb_HtYb6us7Atj5kt3t2Yu3TNvt5Sw5Od5SVt_G3jnOtQcy0KjkyAXjTHifzyHCNOk65mtVJRq_58YFJ9d2LYqL2R2LxGjCmTPvPqtbS6muDFyeQ6McYSWcddU_3l-a5nV6XlL9ossX_DMml8Ss3c86IDagywIDb2DcAY0tBYB2ICW0mFgVyznPfeMsifxuzy5Vj0ZwVc1fJbJnbQWmMGSfj7eO8rrmAYuKwXZd6jubQFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/31034" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31033">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOHQDv97l6UUmj_yPqP20HEOsIlx731dhBjtwEre0tM2_15GGn9kb2Vqsl9MfU3jqSjQ_aKM4l05GKp-kp3WgkJBicZo0jrjPAOjoQLEoO1sPriWi0r9uE8bxE0JYkgCaCSgSljdzmVhoCj_K17D3lF3x7ha--SUwPOlxGOJ5pwSUzGGoVAFvv_Dp4D2XLorBtvt6Kw8SKJn1c9wlCDLK1JZTPfzQGtqMRwsCjjJBjkK1tYi-aJePsdknXbBbVHWDz47xTbBPWtXmyj0omRPM99NZLXQwsYzxvnjLu_d49cjVKEsxVSYvIkJ0dGPXe1GE0aQAm6Q9MjVV7zqkpSDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/31033" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31032">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxa8wqA8sZp_YO79tRAHPLW0NmhPj793fOlG05rh0R70wZmq1AmEeYT_ep3B8ddlcbWkfp4xHK3hX7Dyos4K40bCYjFdUITtpfp6-YiGazcf6Hik7xyPLWqkyolUS-uUj3eYs4Lla1MRK6YNqn1AcMtIpimvluUzNlvezPn4U0P0c_02mrQz1H3FJ1Y8-BfEghKkwZ_OLDOjEiSvF5iSPmidh1zgLJJf8LSz1eEiedzPcMSj9ju6b0h_R5XnKDAhm47U4MxMdGgCcEe6uzYxeweqxDAUyQkMiyx-Zt1M0DAJ1v4YhgN0wO7wFMshtImM1VuWJ5wajsfgTrRiq-zutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/31032" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31031">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMCOrF06160M0PS8zeuezlj_h2HOwHwwIt1c8989ewK9t8Auaht3odshIlGtZX9icVQqqvavvF2umW-LMejc6onOfZSsFI7ZCSD1CLCqtbb1BgbMSBK8yeucGY3Prmu0rFMs2x8sgkkTdEKJQ4Ke-VBZPQ9Uh6QlK8W5xcCydr6790ak-FRCt1hk9OQhvATuD9XHRx108uxYzUjW6PQnnH2ZhyCxqD2cNVb8XeUhu_3pdNNP8tB0b4V_a-A7YA_28UW1QvHcpGJ9BEoJ-yGKSZADshE-uvMYCW3HEaAPphwCOOxeNczXmGN3kmztYToxupPEsMsejTUiGrnX9MQ4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارش ESPN از ایده جدید AFC برای جذاب شدن بازیای ملی:
کنفدراسیون فوتبال آسیا بزودی با الگوبرداری‌از اروپالیگ‌ملت‌های آسیا AFC Nations League رو راه‌اندازی می‌کنه. 8 تیم برتر سطح اول مسابقات به مرحله حذفی صعود می‌کنن و مرحله یک چهارم نهایی‌رفت‌وبرگشت‌برگزارمیشه و نیمه نهایی و فینالم بصورت متمرکز و تک بازی داخل یه کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31031" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31030">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ9ETo-5qnrW0-EGrOXSR9fqKcckDgIi_59aA1wOIyZL765psBl3hIgtj5ufyxQFpLmjhFu8GqwGuzvuqIQUzoF90zCJH_yWMftCMycqDR7mqlihD3lcO5vFNS6133uf1JUhnI-eZhbAzRHI0TmUnHPxfvRUXUcRaAC58QH8BCgvtYeGNakGNlryEyehtyAGmceFoOIgfMAT9wyoMQPb08BicbjbIP2olca0O0XhcfH9Llnbr1IE8rS_kr2FQ38wUYVlWc1pCOV8tJBAkQrYLTNsZKcOWwyEG01Na7YryFPMcsUuVPI8uhQxic9SbXwznx2-bgA7iAeLwa9YFKdolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کلودیا پینا ستاره 25 تیم بانوان بارسا در بازی شب گذشته مقابل رئال مادرید موفق به ثبت پوکر شد اما فوتموب باز هم راضی نشد نمره 10 از 10 به‌این‌ستاره آبی اناری‌ها بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/31030" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31029">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUyUo8Y-YwxrtTObe5PBghn22uaIo1YrAbl3S816N9j0KnN-3mGiHRq2oYtTbT3sp5mQOXHs6aNTFS0MyVTDzFU2zHkvRRjaYgYiVIcpv6KJqVlWFgqUpUSr7GRsgLXqijwqat9R-8BfRmMXOltNvtWeFfCXi5-vnWSnIZm6AHrGy74IBUMPyv78o30HCn5vlIy7r22yvyX85c-NZnQSYAaA4QEqlEYsKeuhDtHleve6BDdJFnT3lwNUuP89Tp9DH1XGoL49ooc4jm2EtDO0UtwBAZaKUIjKdjGxDVFNIeATLZyWYrjAwjVsbmSNl9SybqJsewhnMlc5HuJeNphaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
تیم ملی ژاپن امروز در سومین بازی دوستانه‌ اش در فیفادی؛ دو بر یک نیوزیلند رو شکست داد. ژاپن در 16 مسابقه آخر خود در تمام مسابقات تنها متحمل دو شکشت‌شده‌بود که یکی از آن‌ها مقابل تیم ملی برزیل در رقابت های جام جهانی 2026 آمریکا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/31029" target="_blank">📅 17:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31028">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=gMpidDY2TJkKMK9v07P7BqPGHkdFdMtNBtd7DA0vrbUcGyEtf2msRgApSE_3sxwpKMSfPVOHzUwsC0MEX4qr97gW3QJAxI1QSVjaswF6jdZKUIf7OE0XLyBr9CbLN0IFujUuGX_TDa7fo3ac8-zw6XEo5FDEGxdqO_AigIIT1tSaRBAJkQRnq1e-ZoQyWK0Oh-tkppcFzLbX8_VSiSYnZzIYna_mvsv63UUM_TOc0FkzwRe5d6zYMa_S9r9GnYMP8FmXb5AQir39z1-bDkcU4dPvtAMhuTBu240Z0BBpsjHLeWLSSmt9klCslSE548Fj5xUP7MEu36Slh45DZzJuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=gMpidDY2TJkKMK9v07P7BqPGHkdFdMtNBtd7DA0vrbUcGyEtf2msRgApSE_3sxwpKMSfPVOHzUwsC0MEX4qr97gW3QJAxI1QSVjaswF6jdZKUIf7OE0XLyBr9CbLN0IFujUuGX_TDa7fo3ac8-zw6XEo5FDEGxdqO_AigIIT1tSaRBAJkQRnq1e-ZoQyWK0Oh-tkppcFzLbX8_VSiSYnZzIYna_mvsv63UUM_TOc0FkzwRe5d6zYMa_S9r9GnYMP8FmXb5AQir39z1-bDkcU4dPvtAMhuTBu240Z0BBpsjHLeWLSSmt9klCslSE548Fj5xUP7MEu36Slh45DZzJuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌شجاع و حمال‌گفتنش به دانيال اسماعیلی‌ فر دربازی‌اخیر تراکتور؛ عادل: یه روز باید یه مصاحبه با شجاع بگیریم و قطعا اون روز دعوامون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/31028" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31027">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQtgC6zx7DywAqPZks9aCOBYYsA-KnqaNTPHH_CprnBPVWBBX4TvHWn_OTp_IPhxubBbzBL6pwI_f3jFIaYbXgNQ4CtXDFBFQtolaYgB3m3Bk9jrZthuVNS_WltmQmQcej3oihBKwB3r6SY_hLs8xuC6zJ1NSVLunP-P79DnOBFzIPpgDC5l2tahJHXTOHTNe3PnSZYKBGLdCy_80JpUb5vat3yPUQZv3InXf7L4FonN46AAvLYFAomEUqKmhTnLAGJUE-Tpwd5qRBHQeX0wXQloK1A_BF3Dydam5-yDhsIlj29OF7KTEQEl1POmpwf3Dv_TF1qTpY-ejZPRULS9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31027" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31026">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=X26AFDTRJpw94t8EYJYXnqw7N6Jd3qnTelWuxeNuMuBXKHWsWewemaB__hgMLnOQUPC-j-ywjb048jsc1Xk4PTiwgFY8rgYLrXN07cMcCVPpSmA_7aVKQxQQqiaOTBNS8kNn6u13sKoLvvieDb09vT_5aHD0ls3wrO_l116QJBGKG9O9zjBdaV2jZmMxBHN1CYQ-SIIlLeUJ7T1h5Th9_Q0WL9JLeEbWPSAR74Spx6_QjC5n6QC3AhS4OhuZFlXhjQ50zcvJ31N4kPW82Vp0qScKebeYJvbWBjut0HIk5eb0zS7JpT-W_OynyDJ2UPAgclZLhr7N_N_mNhsePSqfIZoeuoerv5A_3GAVMJ2WOD1dm7BU6mEakeRuhTF8Cd5dHz5aUN5XFSYot8vDz8NdnJ_Sh6QdJKsFA36mg9LXxFTEFBidO4g5xUF4DPUGy2CBuUr6jfYwbyuFZlfMO4DsnsTCRVrsMM3KamrmsL8Ct1SIkH_80gPSvh_76Ec3D7fRktGOrTpMgN38vdd-aRKJ36Rj911qkUjJ_zSv6PVhxIsoFNj9uEc0XiG0e7Np2jAbea2hB-Acg205uO0AGnjsaE2daLkpDiHVkWff8yUfkr3JK1tksI_N92nz_oa-6PmPjL44tAE5zqE3jy1T0f4bn-kBqtNE5hysBUTWyp1lHUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=X26AFDTRJpw94t8EYJYXnqw7N6Jd3qnTelWuxeNuMuBXKHWsWewemaB__hgMLnOQUPC-j-ywjb048jsc1Xk4PTiwgFY8rgYLrXN07cMcCVPpSmA_7aVKQxQQqiaOTBNS8kNn6u13sKoLvvieDb09vT_5aHD0ls3wrO_l116QJBGKG9O9zjBdaV2jZmMxBHN1CYQ-SIIlLeUJ7T1h5Th9_Q0WL9JLeEbWPSAR74Spx6_QjC5n6QC3AhS4OhuZFlXhjQ50zcvJ31N4kPW82Vp0qScKebeYJvbWBjut0HIk5eb0zS7JpT-W_OynyDJ2UPAgclZLhr7N_N_mNhsePSqfIZoeuoerv5A_3GAVMJ2WOD1dm7BU6mEakeRuhTF8Cd5dHz5aUN5XFSYot8vDz8NdnJ_Sh6QdJKsFA36mg9LXxFTEFBidO4g5xUF4DPUGy2CBuUr6jfYwbyuFZlfMO4DsnsTCRVrsMM3KamrmsL8Ct1SIkH_80gPSvh_76Ec3D7fRktGOrTpMgN38vdd-aRKJ36Rj911qkUjJ_zSv6PVhxIsoFNj9uEc0XiG0e7Np2jAbea2hB-Acg205uO0AGnjsaE2daLkpDiHVkWff8yUfkr3JK1tksI_N92nz_oa-6PmPjL44tAE5zqE3jy1T0f4bn-kBqtNE5hysBUTWyp1lHUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعداد سوپرگل پشم ریزون دومینیک سوبوسلای فوق‌ستاره‌مجارستانی لیورپول بااین پیراهن این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31026" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31025">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=mlgqwGjIYx2zx22Re5limyBuGXY20uKHfW0z1ZQMScGXlJ6JYnfQl6TSTkgiP26ZhCniPraGvcG5jnmTwS3EPDIh1QTgpSlQEEiZ38lA3qFQijmeDG2xRCxz8LKl84trWePBxaQEGl8934OiYE6CZc6TfxIOANy1KbT4qM3GgLjpBjZ28T4npYcDDXNz6VxPU0eLxSIjy5mk5JEg6tu-6XS3mjdlKC8UKjXcHkS9BilPHVMR9uEXjgIO5K6ABbcX7yOcvVfrl97-5Ze1QGMyKqkMmpFPNtGx9smkIySwkWx4bpXad9m4LnmToGOpwlZRRC-sXu8u5bVewxYwUgovKE3jzZM6XAc1WNpjLpvqCDmjDXHhQL76dU2FErYyHWUNiFuiPGQoyrJB7ZiHTPvoSZK-BIBaTaRciwyCZTFbMqSja2Ro28VYkoNfM95oOREc1kOqgiRwTBdbp_EJMtfJ17_s3pueNf4NuhEqGUdSjLRp4kA1tD5yEjrkPbFDDISXUaMLSUQ37FTW6ZdQZQfFWDydsOXH0K42ALve4bBUuy6hd8Mi9a2H0OqriXUY7VyOSovrJ6890csMfnXDE8PVyk68-nCVEHdFqVtnNKbcfrLYYuZdaBYlJpbkc9Kuv0wG36gu-V6pR74bO_QBo_uBHXGnX8iq_kgd4qxAx-Ys9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=mlgqwGjIYx2zx22Re5limyBuGXY20uKHfW0z1ZQMScGXlJ6JYnfQl6TSTkgiP26ZhCniPraGvcG5jnmTwS3EPDIh1QTgpSlQEEiZ38lA3qFQijmeDG2xRCxz8LKl84trWePBxaQEGl8934OiYE6CZc6TfxIOANy1KbT4qM3GgLjpBjZ28T4npYcDDXNz6VxPU0eLxSIjy5mk5JEg6tu-6XS3mjdlKC8UKjXcHkS9BilPHVMR9uEXjgIO5K6ABbcX7yOcvVfrl97-5Ze1QGMyKqkMmpFPNtGx9smkIySwkWx4bpXad9m4LnmToGOpwlZRRC-sXu8u5bVewxYwUgovKE3jzZM6XAc1WNpjLpvqCDmjDXHhQL76dU2FErYyHWUNiFuiPGQoyrJB7ZiHTPvoSZK-BIBaTaRciwyCZTFbMqSja2Ro28VYkoNfM95oOREc1kOqgiRwTBdbp_EJMtfJ17_s3pueNf4NuhEqGUdSjLRp4kA1tD5yEjrkPbFDDISXUaMLSUQ37FTW6ZdQZQfFWDydsOXH0K42ALve4bBUuy6hd8Mi9a2H0OqriXUY7VyOSovrJ6890csMfnXDE8PVyk68-nCVEHdFqVtnNKbcfrLYYuZdaBYlJpbkc9Kuv0wG36gu-V6pR74bO_QBo_uBHXGnX8iq_kgd4qxAx-Ys9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سردارآزمون به ساغرمرادی و فاطمه احمدی دو تکواندو کار ایرانب که در مسابقات بازی‌های آسیایی ناگویا به ترتیب مدال طلا و برنز کسب کردند، نفری یک‌میلیارد تومن هدیه نقدی با هزینه شخصی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/31025" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31024">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=gE7ESD7b8DOqa6zNBHYalIU0C0GAlxXIOH41t3bNPUNaQeFq919XXwlAXradJcSPWB7Qlc2RfewUc-Klc24rbkV_BOIqtPIwsjBb3n9Myz2dDCEcEQxOBSBzfbHg-IIxDXl0GcE0mjap3oGv3zA3jcs-YFoQWBcH1r2TbtcbYEiz1kE7184XlCtcwgTHNnrqWPup3C8C1-8Ks2F9hghGld3KjDd1t6e-fC5w_YHh8E4vO89jimjGnNqR5WAinPZADgKR7Gqgtk8Q_xo0prOUwDvkRaqsR86yFJuy2jawHLcKemFKfjOeG5EmjNPXmi1qSzzOaCWt14a3dYffDW_iaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=gE7ESD7b8DOqa6zNBHYalIU0C0GAlxXIOH41t3bNPUNaQeFq919XXwlAXradJcSPWB7Qlc2RfewUc-Klc24rbkV_BOIqtPIwsjBb3n9Myz2dDCEcEQxOBSBzfbHg-IIxDXl0GcE0mjap3oGv3zA3jcs-YFoQWBcH1r2TbtcbYEiz1kE7184XlCtcwgTHNnrqWPup3C8C1-8Ks2F9hghGld3KjDd1t6e-fC5w_YHh8E4vO89jimjGnNqR5WAinPZADgKR7Gqgtk8Q_xo0prOUwDvkRaqsR86yFJuy2jawHLcKemFKfjOeG5EmjNPXmi1qSzzOaCWt14a3dYffDW_iaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صفحه رسمی جام ملت‌ های آسیا با ویدیویی از بازی ایران
🆚
ژاپن درجام ملت‌های آسیا نوشت: تنها 94 روز تا شروع رقابت‌های داغ جام ملت‌های آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31024" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31023">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYVCqs-5rn7sVRkcS22ngECM3LQuqzMjMp_bnVsxSawFx2s6r0ybvJV_VNTpzTC89JyjCpNP44SGEAWWcT-sNFz9O_-HvTvUKvFJfjtaDYJ60FawqgXCFWbivrBjsYduj5GXevETPKS5N4SwKDjVvEn7DZBIGTUW70JVPBJMBkLYG4Y7lfzR5tnfelXU6lYmtzDAhUmHxJOn16My7XWMzTIhKdQf5fXuRlHUzFZ84H9fuNs1VbdwCWtm-VNIbAHICR7r9-QdNgybBqBga5JgqTpjyR7FqCahR-e3BGXsm5tSjOJlBWjfM6Y3lJtdQi7SU7TwcAAr0tQ7XMGCBB1sgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمیته استیناف بعد از برسی کامل قرارداد یاسر آسانی با باشگاه استقلال؛ با انتشار بیانیه‌ ای شکایت سپاهان و مس شهربابک از ستاره آبی‌ها را رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31023" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31022">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWgluQFfE_neOrbTkkUHBuZRkFhp1QbpB2AvjwH_scJ4fJ1QbM5cStxBLfjci0YRaq2riwq_MSIDnK3N29msHp5J7hykKLaBsoQUelMYiAdULreF9R8mjAZgmc_NO7iA0n8CPAtPIDfoxdV0Mf7U-ZFLjeMOjqC7K5gaQNS3G9fU2aeFWZKp3jyiSFA_XufuAZopvj1SVeiCwdQckDqs_kkUvXFE2f8WVrfsbQVMfZTqW_4KXgZpbtghTcz3gznuW4TrAt1UNXdd4kyz9iM96NfP9yvTFwczvswHV2SrqyTBnNJzF_6-Schpgrg-YswH9wuOh8MJFQpsuavPfzfMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ خبر کوتاه است و دردناک: لیونل مسی آخرین بازی خودش رو با پیراهن آلبی سلسته از ساعت ۰۲:۳۰ روز بامداد چهارشنبه انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31022" target="_blank">📅 14:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31021">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCoptQvY3l-pQUKSJCv-PlUZs7eiV2jDdZjBnaD5iVA8NWK77QCP1EMfdpHDEbuoVcM7qQGAbPe_vy6wkms264b92ZrjsSPr5AShsiZ3qXFh-Cj4EZNailSooRTCZ-2eBHiSQcQnBG5PgiuTkbzwm9FVAmoppr9ScCILXercRHInMHZQCcyCgaJx1kHySd_q5qzs4VQ8JyzcNXsyTa_rfnH6kNF0RiTWNH2ZUxn7g28zMS2fSxvuv16u-UCTFDpgXsTunZwzWqAAUlRrR-GCtSh2IMYBDEKRr0AqaSHNMiWdEuqv7nbQQddSK2znwhuXQgSqVsYrwytyVBSe3Scyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31021" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31019">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oq_0u9KrBZS4zwpjlhREIxsetoRQFgUoqEgIS8fSUdQvKPlitcrwUzIqKQzrOAJ-CfibC6n2uSx7VBA223Hkzj5HoGn1bTiho9HAVTnVGQ53HGvFgTw3J4BJ1qFOmanp7uRn5UBbHuu29IgbJIB4mJO-yiYZu8JzYSrmSz_nkJHbfcIIzkmG5Cn8txy7l0pxUdNjDT0n25MW_bXiqBR4x79_R1grV6b6uAQjNn-km9X6EsFuALsrwP4TqRHdKlU02IoSBTCLMsyvXiiKPG4G-8nI2o6u6y8_n8VR8TJvq7s46w-7r0wVFO1ETukU8ad-ucfageTYfzzXdwCplPDf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-oMyZhqkehN5FChNgUJvGjAV3lQFmCPaJT1HMQQERtn2WbOKBqGwt7mneQs8LZLCPwFoSfYG_YDSkNHdk8cHwOSwyKVzLsXAqsmkAWhO3LpgonHCxVKlclT5oGEw3EdRHb28eiXfEqhz9Lwct5LgjBH4NSxln4Kl2fsJbhOCocVfH7oMujSBfJQUOty7mLrC2IdbwK9yq_EoAl0bWKj0E6Es2WzFrHYMJ6KspDr22cQi1JXX0gmB0uZKTatCs57B_f1YZo9uOz7WOlvWgVEb3DDtjSlchmvGqKhhV6z2WsurdtkO40OKODfWhaBniJJHzis0Siv-RSDr1jtBOFfow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31019" target="_blank">📅 13:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31018">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLjVzel0ub7bcE7031k4wRCXLvII1X_n_Ngo92LE2iF5AGsrDQUpck3qbuKMDnJor4LfWuf3BYn6pvO_GEGlJBHRYfcEuxoKOqOl74XsUsdWE0eQiLEwXqkqxPxxAV6nnhBbnMlmbxodcia6Za5pXRdDCnKsd_8DkwiXEeftQKQZJ8wrLJ0Gyow_0TpeyC6Cc19PzNaDvGJMvNz0G6-mUiU-KDJQAb9bSZ7ll2zf3Bb4rlcbdmZyHPNqO_PgilQP3QBsiEK6VvSUVDmqrJ1bQJh1buHC-IXQNvYdlPGcPc-vddkqJJgl74tVJ6hDrMRNqd8KcmHoNPOWmf1tU0EL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31018" target="_blank">📅 13:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31017">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=fi-2EsDflj7eY_lVat40ZeLv3lZZyss2RUiGfPt4M3fgMdw5wUL9MUbJGxrDEdhbtkGUsAiT4BWWG66GgsqxjT5EbVIODajdO1jvwQ5rLsRgknSMXQ69_PK8hmYRl_FQub8BIgjzgoXNybDfsPRktDjkXc6_M0No70fJoXKDcz7peevJLGcPcukFUJAmZBJDUs6GiqHasAx3NR3-xJdpY-73-sZowYmitXE_tqqDtI_Ujbiu8R477mFNyCuxjbh-nUd0IDBYx64homP8_DzLRvKEez0r4-u1y4IK_gO3Serp0FfNKDMhTm7BJIt0hKmcDjlim8mI8WDO0Wx5ndQsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=fi-2EsDflj7eY_lVat40ZeLv3lZZyss2RUiGfPt4M3fgMdw5wUL9MUbJGxrDEdhbtkGUsAiT4BWWG66GgsqxjT5EbVIODajdO1jvwQ5rLsRgknSMXQ69_PK8hmYRl_FQub8BIgjzgoXNybDfsPRktDjkXc6_M0No70fJoXKDcz7peevJLGcPcukFUJAmZBJDUs6GiqHasAx3NR3-xJdpY-73-sZowYmitXE_tqqDtI_Ujbiu8R477mFNyCuxjbh-nUd0IDBYx64homP8_DzLRvKEez0r4-u1y4IK_gO3Serp0FfNKDMhTm7BJIt0hKmcDjlim8mI8WDO0Wx5ndQsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
چراغ سبز سرمربی تیم‌پرتغال برای بازگشت کریس رونالدو؛ خورخه‌ژسوس: پرتغال همیشه خونه کریستیانو رونالدو بوده و هست ولی‌اون خودش باید تصمیم نهایی رو بگیره. من هیییچ مشکلی با بازگشت او به تیم ملی ندارم. یه سوتفاهم پیش اومده بود که برطرف شد. همه ما منتظر بازگشت…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31017" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT4anz9JMvVO1F-lGyLcqpFdar5Az106SVLUcBUmyQFqaSBSg4G8FhCTiNqt6E6lvwp_NmNfMKK0_HIga6Vzc8lDCLVXG10TUnl_ZyHCsMCllUuqItSfytUUU27R8f33I-jmiY8XA8dNZbrDRvJ1xh7N7OCfIy9aityCzZLgFW15Inc4QrIAfbFxDtQdMxvASaun8IpcwpPqhii1a_NinizKwtPrpl7Xz9JEq12QZddiFlF47PqFlUVyGab1wRPrjhvbgXxDtHhW63HuWxu-Qhe7hPqaI8RhZLT02r5lbpAdA8R-Lvnut0Pq90qCIUq1ruAtQleCEtAmqsT3-oQE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcNajzErtTqGs3NGHURYIt2Yvb5p1oKPmFjaiXgJwmAgAnRtJAzEjLDmVE1fdqRCFYxNADZX7ifR9ZhD84juakwCcouYKxAvKJO4Ia1T5c2pUD9ddmA1S3bwpF3oOMteBpgUR0bPNDsgGeZzleHk3_xMExYyl4mVs_TC0o_MqcM_5fGudcFuWvbIbmo1BgGM4F04TE35V3g9A3pHgeTdio6a2uZeTXoMcFc4UVD3jg8IflDdBtRMqIjb-VX5AcRFnBYvfBGo0Rx3OVFB_3mk8eGkogdsM2J7MptfxGWbk4RfpRIfB4gd08CaiROTMRnOtk1fzjRbStNuTzSSvnviUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiIa34SmIP2zYqy8TA8apS__fH5Y9L1MxXH5oHBRj7SAB3Da4V50sSEeNzVtuGJhYNLepetdTKIIflUMrscyEbyfkWY3FT_ZDxPj9ofsRltAM1Q4bClB-Yd43YlwOGPHW2pUDY7VpZiNr4wUVvz7RmP-pU6EZF47qQiJ8OFxqp_B0U-uG5MmI6dHyuwd2rOFk-QQfxbrbTdSYuDN_SH9pztOE11H6RNHZ_7aYFAgFWDSP210bOgBtWTwMy4QZapMKiJv2V14ryE73hAWpAjaGdnODHqHb0poTo9hfAo2DTloY5IqvhnLCDNiS0We9Cj62eQpGgzns0_iA8bN-EKjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWPhZdgGF5XfV0aG16i4kr9C0w4SCAC1RSrEsuAED5XClLzE7Iq-wtVdl4kDNhYa3TTa_GXkHAORZwzjpr6ykMflyzwLak6YHIgsTQbejac4OK4HxyZH1JheF8enoIaDZBE3iQ67gLStnp5Pe1KGpr8-yibidq1_17rML9eemhyNWPpR3lV5EIKll8TWzdTw-dpSUgCvsm14aoqJFU2MMIkqQencencHhvhsaSMnow35YLnv-GC6Z0K4h970XVT_jbro25q90AyiKtxe4pZN-zk9y-T6nJfTBcfys8Tyng_N0ASwBsiMr2wXuoBJixpptw99dZQFWjVyavwAVSTk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق جدیدترین اخبار دریافتی رسانه پرشیانا؛ کمیته استیناف فدراسیون فوتبال بعد از برسی کامل پرونده یاسر آسانی به درخواست باشگاه پرسپولیس مبنی بر غیر قانونی بازی کردن یاسر آسانی آلبانیایی برای استقلال پاسخ منفی داده است و بزودی سایت فدراسیون دربیانیه‌ای این…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31013" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8ITAx0rrdK9WuR9eBJQ2bIIFKPXCgUUReh5pXfzBnvKRelHSCLJYfi0MdAByUe8ucfjCzV1d48kND4A90wssis-kWomUTUYDCWRDhB68qbvnWDrUsLsL5fO82nAz0c37YTo-oQ1CedHXP2BqLrUBCnjWLYvxV1TTLCeUKgyleIJhmQHo4aEzienDEvAIlnoia_CDZ58UUvvmHYEWxuLERancQdDRtwMBN8K_MZNjJHE6FhBhAyZm0PTFWX_sWGFJQeauD3UmPG3viAc1Akc499KtcqzA60Jz0vdKRki_5TUMX0Ra5_bIG81H23BblshGDmHoRe2MhM9kAmmxH-8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31012" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3A8hkP_M3C0bZzTWJDRV3-326NokpQnb2mrvzoPI-YuIVZl0d7trz0U8i1o5FKKp7bLfFgfQRhLHxWZ4lPGdOj9P1xhXC6ouHcVqX5HQVWJ-yw18Fur_N1pjK6yUGykXABtO9cdFF1-Lxs1oreT0Fg0U4ZrqnhMVtFPlr4p-Xy_srzZ67Flbk2cs392ro_66JcjhQTkMjJbZqgUsapUkK97tHqydYNINQmdbMk0OA3iAmkUGBxy1dyXvO_44xh5BrxKOKpDbrDZXXHJORCGRwsf5lPUWuERAh7tnOZbluEHeFIcg4sBVRCYZCtjYHaeLpaUpegETRT9Uwovqez16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه آاس:
بعد از فیفادی رئال مادرید قراره از وینیسیوس‌جونیورتستDNA بگیره و نتیجه‌ش رو با هوادارا به اشتراک بذاره تا بشایعات و تئوری‌هایی که توی شبکه‌های اجتماعی مطرح شده پایان بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31011" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=fHzin24BdRe12_S5pcSJrL4cH8X0NExcP0LG2DbIi6Qz6BqvsmgvPwnDq5yvxRyDfsxJflq_TjdykFsQP8Jgr6lhCQg7Od-B8phyYzC2DpFzD2zSrfDIirdQwSh-HdU6beZe5xoPTzm5mrP5yOusDq0SC_G2O5QW8J8p_nJbpllCLXCFLtiTlEtETmAGZXGVBxwgY0NQl6c_wN9ze8I--hiaVUCa9yilL3xJlANl9PRZQW9BHzguMK5Kdp47Y2WOM7XZarjPMWy6PTQ-u-nFpBda4IzgYhu8ZxS_zO7RWuoZnvqrVUKdaNuy_rqLuUj8-0aRx_lCr5gVXo8JjztB6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=fHzin24BdRe12_S5pcSJrL4cH8X0NExcP0LG2DbIi6Qz6BqvsmgvPwnDq5yvxRyDfsxJflq_TjdykFsQP8Jgr6lhCQg7Od-B8phyYzC2DpFzD2zSrfDIirdQwSh-HdU6beZe5xoPTzm5mrP5yOusDq0SC_G2O5QW8J8p_nJbpllCLXCFLtiTlEtETmAGZXGVBxwgY0NQl6c_wN9ze8I--hiaVUCa9yilL3xJlANl9PRZQW9BHzguMK5Kdp47Y2WOM7XZarjPMWy6PTQ-u-nFpBda4IzgYhu8ZxS_zO7RWuoZnvqrVUKdaNuy_rqLuUj8-0aRx_lCr5gVXo8JjztB6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تیم بانوان بارسا در هفته ششم لالیگا؛ با هفت‌گل رئال‌مادرید رو درهم کوبید و با شش پیروزی پیاپی در صدر جدول رقابت‌ها قرار گرفت. تیم رئال مادرید هم با 13 امتیاز در رتبه سوم قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/31010" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg2EjZN75HwfsiYHpuh4eoeP0pFsogMkLJFBfKoHbs4JmOGb-yBYN-QOaGgDEhbUiFIGgH7unjllLj_Z6KhHWv_qOs6nmtC4JjJh6iwUHYWNwpbflLhmplKCOl5cdIjvGuuA040ka_gelKCZze8cLur35YIQKb1WvDYeetGMwKLKMPi0dWMiFNuQ5uPEW4Qs79svokv32sA52pmChcKiJ_JUsJmdd4fTzlMpfRPkx4g2rWFzuUV--MaPokjwRJIvDfmvy4aknJYBaiKfPDNcECI75UhklkD1uIT20u4iRoOUIOvyPQURAmaKMfcnXfdW8L5YvxEEgDTDQnkRCFQEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31009" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3HCvQf3i93YM_2a5hRUKOX6HUQ2o6tBQMTxezn-69QHbVkG92e9CpmkTMlcSQZtr_vffNQlysj8I8N1imDR_9TQ1MQWDJZU3_6TJBrXgGBgs2V1RRNL926PLa4Ii9cGaRu1bjJt_CjIXh6OXkj1IW_56W9OV7ZE_2TIB1LTYFzcUT1k6yrG1z83fLyUfHBdbVnyNxMLSCufvL1Jd0bdTlcKySwAMorKyU2spu3xJGq0E6ooO8U8MvkOTmTompK-nrjvbqvbhsQ9jEpIPlCQrgXnwuzvVkdyn4Cq-7MXf9CEIksNjG2GHKYZ_eehjNMcRw3X1MeQveEYS9hIeoQPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/31008" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-PfdQug0NJlqhLB8wY9jGPKKiB8g-4EtAE6YKs79yQIiP7U_WdKqz0Lln1f-t2LeKEhsDtCoS3pL3UgBp451KvWm4MbNTiBAW6LW6-I92yWOXxdPkXK4wjk-VrDFtDCIUcEU-n22599DFvpCONrsjgDNrjyfrR0AooGk3ph2i46fJXQjESpQ8ihN9R26tpYvZRMLO2heLUkbLxH83tYDSRz_PtAoPpeFI1oJA5chh2KyI-aIRHWGDba3lT4CIj-WJInI0Pk6SL9BjpZnpHyDTx9Wl9agL21wX7EhfjDVOp6CZm8Kuapmx1PJGEOJYG0pBXZjk4QqHCpOX3fbgJM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31007" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=twG9qVDaW-a112ZGCb1Yr7YJFKCdPAKOitgfcrFVnUPQcMynQAeB8W7jrbYtw99Ck45oQ4_y0ET__hjzKQqFWk1zcxzSbUj22wgQkqlOKyFiUXEbIaywyXtZUAGIfoh4r8bLZ0fNyqTfhmzgL3rl88-nV1GK1DJ1jHlRKu-P43KuBp1A1kz08r4Eq39T62ue7R1-zZ0N2r6O89LM8TUbxFQgscFZUK5mtQ2kBc2v4a6lB-fjs-han30idvfrdi6aFncKAE8xEls5-__nS1bBVgRN0tWC3iu1zVaFt5LvcrI5yw53HvZI3sBdI8ZKDoPyLnI6WW7LzWLvu_ys1Bllmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=twG9qVDaW-a112ZGCb1Yr7YJFKCdPAKOitgfcrFVnUPQcMynQAeB8W7jrbYtw99Ck45oQ4_y0ET__hjzKQqFWk1zcxzSbUj22wgQkqlOKyFiUXEbIaywyXtZUAGIfoh4r8bLZ0fNyqTfhmzgL3rl88-nV1GK1DJ1jHlRKu-P43KuBp1A1kz08r4Eq39T62ue7R1-zZ0N2r6O89LM8TUbxFQgscFZUK5mtQ2kBc2v4a6lB-fjs-han30idvfrdi6aFncKAE8xEls5-__nS1bBVgRN0tWC3iu1zVaFt5LvcrI5yw53HvZI3sBdI8ZKDoPyLnI6WW7LzWLvu_ys1Bllmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی اسطوره‌آرژانتینی تاریخ برای انجام آخرین بازی خود با پیراهن تیم ملی کشورش دقایقی قبل به اردوی تیم ملی فوتبال آرژانتین اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31006" target="_blank">📅 08:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31004">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFTceET7WxaSc9k4Uufspte33bYmla3ZupzJClrtYjT0NSOQBkJbEYUGlybqNG0KPs19ggnMMYXspszux_mJZNUS5axJTG4UhoYeSf3-_NaExFK8dR1lfsJ_65_K2h3ngtpPWicMvidU6Tg_xuGjmlP4jlR82IXtHXXvmifjlnEaT0BUCJnFx41wmQfaI-lZQSKbqYFdExgBRpAIzPYOE-hqiW6Fztv8Gmq-w8mY83rQ3coJ1ZPnMMKCF66gPsN80rqklZJbk-SrwTru4b9zf3G2FM7OMWcZsoiwYcU1EDhUVT7q8GxfzyBdUqKEbNCg3ogmpqa3df4lGNRnI881Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31004" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31003">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_dcs4SbMc5Etw_V5NBJ5DExLH-qYZ0xhOkbnUVlaxkfQtY6qftyd2_5OG12WazXW46xrDmnlelWIM7dhd6aAdbSQP-OMZfnzSPcc31VFra9_BYypjSDqh9cm5rUtRMhkmDK5WImYNKqFkDuza6X_XkbTWuzTzV7XAn-hwl2TWTs-njxVljpcSEn2cer4NVpvdGYb9CbRKFOeonSKQdw2G00VHF7fFbwoiBeZ4_yqpP7be6wp1QR351meKNEY8DvJrlkiNH7tDEsaiBdzZV-E0siT191k2CKr-lrP3kqYEZ8FcHvmrR5YcSkEQ_2WRcBNvF2fPvj2cNHO1vwPocGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدار های‌‌‌ دیروز؛
چهار برد از 4 بازی برای شاگردان ژسوس و تساوی بدون گل ژرمن‌ها در یونان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31003" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQcxaF338fnLwgrDcO1Yjx7yhYYAQSt6HKpUcsglYA_drKDI6lCQ7wNqkxW3Jtd_Jwc_g51Y5d7pTuXcyK2rPvNI586QktyywZTVrz7SwETg-q7uE7DFsTZ3BFDzo-Hd3U5FzjTonM7kX5N6-_afugkHRxvrKd37-IM-q4XcIis3tsemTJJkU5M8fo3l3mk9ZjFRCzg27f7HUxuixLE7Sx1NwEzJIpROzEX57_6GXScXl2LUr-5UXygjfsfzsFxgmWxoJBMWeyc75mBJDmnja5yEnT0j8cUHO9E9BeWgTZW7CLyueIEXlrZl5G5zvEMxII_GelHK8JVVQe3VLTX1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31001" target="_blank">📅 01:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APctPgTemnWBqwuApNqr_l1kxwgYtj_GnolTfx9gT7dLVS3my2aWc-EVWfNZhRnzdzZXAXJH2bwZUKVbz7WDQjlqZaBZQc9sB2fBFlInOOUq633IeKUg9yYZvDru9ld26dHwmDGtT_WBXkcDrbP1mqd0Ig8OZptfTE5gu_-Vzivk6CbTHn9Rg6jr2fDt7Gy9EoVKerLn4vkbmGRZBAOV-OyPHoVkVIgJcxTk8gocsTL0c-LpGRm0NHGcmt4VeXgjvNGyKLLM8dNMdSUZk8mqyuWoHUhyVB1a9XmuF_0vIEQp1bwrq-a2dF6q_aFz5DT8PAixLx5DiRSPcg-y0qWfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31000" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇵🇹
چهار مسابقه چهار پیروزی؛ تیم ملی پرتغال به عنوان اولین تیم رقابت‌ها به مرحله یک‌چهارم نهایی مسابقات جام ملت‌های اروپا 2026 صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30999" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMWDNZSYFk0i-uOzzqn_j3IOlffiS3s3nEe--wP84j6GKcgGazR0RhRq7gsS2FHjmzZgYV0fKDETzqj00AoevtWHGfwgjyETeJyLNET38Ptdl-60KBxCQ9JB0Zm2YpMBt-z01JQZz0m5WB4Xvmbl5WsK6Ck2X8JyEArmdaFgQVNEdJLYux27NJnAbPd2vKUo6F63ea3wrFp0CVHTfyV6JaBhOi_Cj4LCPqPIvz1zt9bEASj11VBlavD3QWyEgKo8U6VGwtT0HUHOdy0uCm7XR19yrQrRBvJRvhi94vSBvhFpjJsEHaJR8OrgYzzHmGqCfccUYtiCFDSH_z1b_wkCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30998" target="_blank">📅 00:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOiMRGI50_nauTPRd6-dGXwlxmoYBiHOEkPv44p6sz97MJ6tfSyGWMkyc0cDDcBiQMFApqdr67Tysxm0PKIVodKV2pJFkEy-ZfnrUXp2FGp0AU3pI6fbcM0OqwFsEPrCBTaIC3NmAEXz6f87PAZpNSuy1Psi1Wc9Y-CBEBDutvCZIyKbRia8uoggYteQaus_z0kVm3QC8rBMQ9pvFDB728NqFmRY1iW9DVeIB0KtZO9HAlnmJpijjaEpTW6vbwMvY_y3DzFRtwuSSyuL7UCWucWupvzD8Fj7tt1QEDtsuPQjBX1pHwJdpvIEiyEmfpfdS2xnoiIVxDUJv8zpTMfJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30997" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1YfTgJHS3qvp31O94N0uy1s4Tt9sWbtXKOp0n7NyyTpy9lQkqEP0nDYmwqGRoGEvFFvWLrrtCS7FGaZmc-Jz2bEJc58Yh6fiaK6VPXlEetdKuNKbD_bMR_Pf307ETIHlWUr6qYpdKCJV4-kRq5xheqBC3BBhRJSPg4meutteq_eIjs1UqkyexDs7h5MfIMerZkafWP7FF2DATLNBjDSOFOySwYXnuk35_N7zXErd7ZLdqr4zcVPqzTFu0ipclDh-z2_vdJSLisd-ZTJgN4bZoKVnInhqjT4XlX3al9mU0FzrEd-0G24pXOxuZ3d0xfZ4N2gK8pt26e_1B3RcK0Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9256e00306.mp4?token=dd4yU5rr1zkdBR-nyuLYp_7ENBNODrW32kqJw0eYFbXaO7Yoad-UQJWZLAHKfE_uuxHYfqAxXxXOOHnNfYgvUtJIHOXUGGdavg-7t2mOlv2Uemveq1pSPs7b8XPqHQCJxLadF06gkFzZRxod_QLlizyFgMAIjuG62Aef6nsFIBd_9622LXhllHetk8Wj4zmFMEbF6NOi7yl9Vd0Fmz5y_GVwADS2mgvO-gzs6mxVSoO30CubD8US15e8GwPKXWWGdkSugpX-k82oDWheN7bTWvmCiIDe2QM0oj7SEJxj2M4axDfHS5stUrfFoB4YtppZaDvG6hgKbekRQxFzItlCMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9256e00306.mp4?token=dd4yU5rr1zkdBR-nyuLYp_7ENBNODrW32kqJw0eYFbXaO7Yoad-UQJWZLAHKfE_uuxHYfqAxXxXOOHnNfYgvUtJIHOXUGGdavg-7t2mOlv2Uemveq1pSPs7b8XPqHQCJxLadF06gkFzZRxod_QLlizyFgMAIjuG62Aef6nsFIBd_9622LXhllHetk8Wj4zmFMEbF6NOi7yl9Vd0Fmz5y_GVwADS2mgvO-gzs6mxVSoO30CubD8US15e8GwPKXWWGdkSugpX-k82oDWheN7bTWvmCiIDe2QM0oj7SEJxj2M4axDfHS5stUrfFoB4YtppZaDvG6hgKbekRQxFzItlCMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شکیرا همسرسابق‌جرارد پیکه: برای‌اولین باره که این‌موضوع‌روبیان‌میکنم‌ وقتی‌از پیکه جدا شدم. یکی از هم تیمی‌های سابق او که اتفاقا رفیق صمیمی پیکه هم بود به من‌ گفت که بهت‌علاقمندم و در این سال‌ها علاقه‌ام روپنهان‌کردم و الان بسیار خوشحالم که جدا شدی. یه لحظه…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30994" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEYE5OIkjgUupU-QS3UR2umw8_Wjsw-YPn4vfKRQfgPHgQJrusYxVh0wPLWIwbICnMbLoD1ZyzZj8P8NHCqQ5Q0HsRRAchTYaGC-GewCUa-ZozoJvDgtVMvmDaKzu6QHrDPvLeeXqg8EEkA0TNaWqpSLfHQfG7-RBPcKEx5Zq5lYZWo2-kncEZUjj-s-BiyzkZuEsJixynFsWVzdkF9wpryrFpRJ3DX9t0ZT1oUFANiKb0OV0kuGkejzVqpsqm2hOZ5sGrqjbJpDddHwj5csv1xjybqZNhPtXBLBjFeaCwlHmhwMCGmfS9Vmy99bOZmlS5caTPYqLFron3rU7Lvs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30993" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30992">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=oRKNWi1HF1r8sG2olDQJAW0kl021Nvk1IzQ04gSva0YWXQIKWYcOVTLaUxyz3O2VZbaWxpykexOSVl0-PyGt_HOd5EwByLWKQb081iT1p1-igM4bLBxb-lhHbvwXA9oJKspDTLaJxU62VX5-MjkeGeDCj0-1PCHapkkM3Dy6Memrb8oubzN_A9R0ethlExaVkiy3XEBvwIvr5QbCKYl3fx8o0PhPTIGAb2D2KAWVgvT5sITklHF9rxjtqE1cpjhjj0jcBxeK5c6PDn4w42A3oP2rPGzv1hZ7xktxoZ5dChNJiEOijkosy6Voq1PBfapVp7-BuigVpl46f40HspEo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=oRKNWi1HF1r8sG2olDQJAW0kl021Nvk1IzQ04gSva0YWXQIKWYcOVTLaUxyz3O2VZbaWxpykexOSVl0-PyGt_HOd5EwByLWKQb081iT1p1-igM4bLBxb-lhHbvwXA9oJKspDTLaJxU62VX5-MjkeGeDCj0-1PCHapkkM3Dy6Memrb8oubzN_A9R0ethlExaVkiy3XEBvwIvr5QbCKYl3fx8o0PhPTIGAb2D2KAWVgvT5sITklHF9rxjtqE1cpjhjj0jcBxeK5c6PDn4w42A3oP2rPGzv1hZ7xktxoZ5dChNJiEOijkosy6Voq1PBfapVp7-BuigVpl46f40HspEo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صحبت‌های پیمان حدادی مدیرعامل باشگاه پرسپولیس درباره شکایت از یاسر آسانی: مدارکی از ستاره‌آلبانیایی‌استقلال داریم که به کمیته انضباطی ندادیم و اون رو به دادگاه عالی ورزش داده ایم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30992" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30991">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIYPRW6hRJHD0Jvu0RUo42y46TatMFS5lcgirnlwAoqh1Htmt1b5l3lJUwxOrgsr4KI870rF1LWjA5oK7JzSg9SAY5BeROmhtQa4DAoHwveVhpCzRwyYPYc8_uXQkDxFpnd4YWP-NKOQrxExWOE23F1s-Zp7PZdafEODjBuesVanRSCviHRB9S9sYf9xFJNiRojjzWtWGFa41iKI8tcifKgG1HHqcyq2jL2eWgQ9WFAWwE4OibyXTTRsncEjN943c7G348dBXUvrJLIRSGL6riFbeYKId-FKAPWIIU9BfMyHlHQfYgtQs0hu4X4IqgokBXlLLfhp2CWd1KpeLxs_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ادعای میگل پریرا خبرنگار پرتغالی: کریس رونالدو مصممه که هزارمین گل دوران بازی خود را با پیراهن تیم ملی پرتغال به ثمر برساند بنابراین احتمالا درسال2027 به میادین‌بازی‌های‌ملی بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30991" target="_blank">📅 22:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30990">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAv_aleq5eSpHKfQyz7r37MrvwdKk8sL3RlIuAEtCrri4OYVbNBHguSMTwQm3VPvIpNtAbm10sQLZVLpNLnzKC8JlBZ8FVeX1RiFKL0IscryXuWYzurT8Jf-Qe44s2MqbYJIl_rdyCvacO1q84THcH34RNOlwVAb44AJaYdAh5xinNalBE7De4F9vl7MKPgPwXMw7BBWFcXC-1bRAasWrGXRpJGaihVaYX_p4NmK8yxOFI_3IIdO3jO0k58ZyLgzbsFCprBsATzhPYvfOydgkf8rMiyRWDFc6u94RqF-QhvF4b7-2y1ZSIBCPiAPu-2G7wsPbVR0p9K552rDL6VLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمسابقه‌ امشب الکلاسیکو زنان؛ بانوان بارسلونا تاپایان نیمه اول چهار بر صفر از رئال جلو افتاده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/30990" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuoyg_3tQd7dVqusgy2eX_kRWqK2x182N_GvWn_yJlTTYIdXzsuA6ByiknJgTgkr0ZJ-gg_nJjL3Ka4cwy0HM0_52U6b7zw_uSGlXZf8vszVyTMVunAcHpTkv31071BG1y5S0NBRGjwFC79DipXRD1aTwyqF6igGDPK8VpnbVw1TwXQzPowbYt73LnejdOfDUf-XKmOziET5jH_goqeP4MHhWD5N40xjUveM_UQTLVy4KeOYbyqxGyJdgwTEtprLMuEyiexZXmJ95W166rjriReLjcXytppLTUFAZ7Op7H3KiSBBBYIXGOXybcDY22YDsnymen12S7MCYQ7zTdfSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/30989" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0I0IScmy6JI1Sudh8uWQ1_qsMb4SbxxpfQV8-j-FSauTFAJ_29FYFRI144p9Haj0sgMxcs8u_lVPPJkVYULGuPD8tXYk5LZOP2m9Q9wAlCTPN0pZEFVMMu-xldWVAN9g_9An7d35QzHuAp0VW1u0njon-zuSs1DPk3sFxgcDDQmJ1ozMklxGUcJ_hAnXpXvazEQD-uPo9q9s_LTMtTAGlX0jMUrFoJkQ3z7m67QK7cP4zvnelm7pdvbtRlATbwjdmnTtHw1hgsJRvYY8jC9p04ZQu0-Isx2Cew_oJ1E4W_e4lih2ZzN7F7rGKcd2L0-8RTwtibQKjbIhIwHI5rRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=FxOkfwf_IielSriy9JeU0_hZz_VSu2v_PAAZR1KCMfVVHLVrQZ3WhehKTffNLQvISMI8nIsw6zfhU23i0a-lzgQUs4KESAGsCxlfxO6MMWPwBEt60t5ixLRkma82v3kGdAT37tDFAzrkOq46V20ELTCkb-WDBgol-fSrXcE9Jwvw0My2AgqFhbNiwxy5dV0ai6xW_vjuwfuZUmmgBbNmk90nhzDSQH9qcUF8CSkqtWUVxf0HbOSS_MhEkFRXorZgPEOV2UfVK8t-zfjevvcN6NQETnPg2r1c9BhTuJrhLGIFmRHiTkw-mhmmjsENmFfUiiFzyjr6kHrUpgdC_Adf1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=FxOkfwf_IielSriy9JeU0_hZz_VSu2v_PAAZR1KCMfVVHLVrQZ3WhehKTffNLQvISMI8nIsw6zfhU23i0a-lzgQUs4KESAGsCxlfxO6MMWPwBEt60t5ixLRkma82v3kGdAT37tDFAzrkOq46V20ELTCkb-WDBgol-fSrXcE9Jwvw0My2AgqFhbNiwxy5dV0ai6xW_vjuwfuZUmmgBbNmk90nhzDSQH9qcUF8CSkqtWUVxf0HbOSS_MhEkFRXorZgPEOV2UfVK8t-zfjevvcN6NQETnPg2r1c9BhTuJrhLGIFmRHiTkw-mhmmjsENmFfUiiFzyjr6kHrUpgdC_Adf1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیوکامبک‌تاریخی‌پرسپولیسِ برانکو ایوانکوویچ درورزشگاه‌مملو از تماشاگر آزادی با گزار مزدک میرزایی؛ اون دوران الدحیل تو 51 بازی فقط یه‌باخت داشت که اونم جلو پرسپولیس برانکو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/30987" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGeM7s55F4piV-Ba5BrQKOqn2_DD0h7gzU1F1Co1E770A8APiAPKJbe2UTFjfiLMUsYV-fD0z-USBfzRAHOQi3yKM5TFdIpH51DwsG91i8StV8VXgiMAXT8CYQDBqFMkrEHzcDpDFpxpC4Dqvp_Ecsm7_ylCp2OZy77jkDcB-QqvXe9vaWlJb1C493fQGKH4t9t9s659eI2XlBrqCPYH9v1cr1cyshLRx92kcZeLfAZFKlQdOKqFEIAQ6cfcCBcRHKIky_D-j_BnidvxF6nCjBZiKs7BauIKNEFYRLYAy_RkbM4Ue8dfsBkFN3Y-IIqL6exXPYfO4Vv5NNFsyLEEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خرید جدید تیم بانوان تراکتور برای فصل جدید هستند؛ نازنین دواتگر مدافع میانی که سرخابی های پایتخت نیز بدنبال جذب او بودند در نهایت با عقد قراردادی یک ساله به تیم بانوان تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30986" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=HZKVwAitZETmWzywOl7zubtrO6KIuLssd9Ujlc82IqDnbB2Pu5e6BIo7Kcx-4iFCNS4wJw4snX-Sf3lDgb950pBiej9Z-KcnI20IGjw2HiqD8quw5gF-VoBGCAW8aM7tYupS4CTzRoDPJfphvykNF8FmsIw5TlH2PmmtX2X3DTwxHAdclcj_nMfhx90izftba3wHuBqI3WOMz4eTjh1KLdzSYoxDRlhhmXw42WoH8y-ir8BvPjqkNR6wHuYVe8Z1ThDz7iZHNS_bisSYHk8TlqGc3Krt5q6-dSlPZ07CeX-FIR5JnZDpTWNIm-f-QJ_oV6wjecxq2AiMnm4CUe-AIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=HZKVwAitZETmWzywOl7zubtrO6KIuLssd9Ujlc82IqDnbB2Pu5e6BIo7Kcx-4iFCNS4wJw4snX-Sf3lDgb950pBiej9Z-KcnI20IGjw2HiqD8quw5gF-VoBGCAW8aM7tYupS4CTzRoDPJfphvykNF8FmsIw5TlH2PmmtX2X3DTwxHAdclcj_nMfhx90izftba3wHuBqI3WOMz4eTjh1KLdzSYoxDRlhhmXw42WoH8y-ir8BvPjqkNR6wHuYVe8Z1ThDz7iZHNS_bisSYHk8TlqGc3Krt5q6-dSlPZ07CeX-FIR5JnZDpTWNIm-f-QJ_oV6wjecxq2AiMnm4CUe-AIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30985" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qngygpeh26HT7tUpdtwmC0y9idahJwOi8iAr0BQg50l8FX9E4FM_Q83Zpn4mHBKTuXOydMeA-dpUw_1EGh8Nt85nDWG8RHMn_prKG0jHlghRNNL_RM3uKFIwSGdr7NyDr8O5THDZIjAGseVp9w48stH5IvzAre86D3wiKCg_tQIdr88FJ2FBPwQPDCFUEYF76UbhOnTS124LJNIc-VcSfNS3kL8muJHh4NsjD2JVazzfzVcaIdXwCJ_C4WczwNtRwDnsdLIOSeethlDGcPqEQCUyLhYpWaGSYGCTZI0-z_Y0yk4kAWw-zhWWjs3PoXy-SEUuPFRlat0Nu7A6Cba9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد کریس رونالدو و لیونل مسی زیر نظر کارلو آنجلوتی و پپ گواردیولا در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30984" target="_blank">📅 21:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1iY0lPMEmdDLl2vMXFgaTbl9hI8zEZCtsw2aXObFRaAveLPVnKyuPWwLPE4TRL1xIKmR2mgGiA2c87DbRaHX8XB9LdVdLCuVlzfOxCwwhAHPalestbKshrYam9OhtU8TL4Fyff4tUMiNnSrNvmv2BDewxHsXHjPTEho3ouc1u5n2kRPD1RwFikXYyEiE_PAN9LuMgEnTn5oicxoz0KNHiTP-KFfR9Xezix6WXse5riIifvEk0lNHYMbWYsDDO1VpxBkWtKzShROoA8gtQo61TfhQ7nR51FkVIGabVa9-_uWJe6jcI3tPsvHgIUY8DiI2zMQANlX2j3RgNt-R2c-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی و زنش درتهران: متاسفیم برای فضای مجازی. مردم در واقعیت خیلی به ما لطف و محبت‌دارن و هرجامیریم یه ساعت باهامون عکس‌میگیرن. مردم‌ایران خوشحالن!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30983" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=rB4EU7jAkFVvCGLhKUs7aTgvZLdmYgjsID0HJB9Jqn6uc3BS5YVjBT8H9NX6YYEFdgzXkqOpLExbBOdubwipUK2POEuzHM27gSx3VUHAoPQbIJV-ucoSClNUwQgr2g-53A_84M4AYj5pekDp-104SsoNqu5obRd8YvTxyMfUc1BihqbOj062XKe8BPgtR_qOJGsvRuyVZaXT8IF8SpzYEYnMhvBIX8bPT5uP1gWlTWdgrnHCYn20HlkgkW8Ys4PsRmZNjgdpKXXQpQtzdGPig56V_fcOfJsVG3EKsiIPxZyFbd0ATIH2i_M4V5gFH75za7dEjsGxb7x8DVpivXRd8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=rB4EU7jAkFVvCGLhKUs7aTgvZLdmYgjsID0HJB9Jqn6uc3BS5YVjBT8H9NX6YYEFdgzXkqOpLExbBOdubwipUK2POEuzHM27gSx3VUHAoPQbIJV-ucoSClNUwQgr2g-53A_84M4AYj5pekDp-104SsoNqu5obRd8YvTxyMfUc1BihqbOj062XKe8BPgtR_qOJGsvRuyVZaXT8IF8SpzYEYnMhvBIX8bPT5uP1gWlTWdgrnHCYn20HlkgkW8Ys4PsRmZNjgdpKXXQpQtzdGPig56V_fcOfJsVG3EKsiIPxZyFbd0ATIH2i_M4V5gFH75za7dEjsGxb7x8DVpivXRd8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توییت یکی از طرفدار رونالدو: تو امتحان امروز به سوال شماره7جواب ندادم تا به رونالدو و میراثش احترام بزارم؛ رافائل لیائو لعنت بهت تو چجوری دلت اومد اخه شماره کریستیانو رونالدو رو بر تن کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30981" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/calhwDtcqDEMWgERa-s-DgTwSd92yRBsF7ib2o4Qw9rfUgqnDJWolKqq0Z2uuRjGQe5-ErLItMe-d1tZsm0-JyiWa-NWlHLnmN_kLdHSAtk0PGxrqLRh7mkaUUPNaGJc9U9ukGKz8CgYr5na66f2iC6cWvwp7dzuEZuyRJeXr2-_udJkpGdO2iJ_JZd7sFpBQ_IZs5x3PsSFQgZsBZoKAEQRhcvVoFX1d5R_IaiBzycvoAVAF2X1lV9AywE4cAV0uwGnmS-iigVShQ5D1JmJsdpM8_auOkWiDyZj11iaUXm4gVFR3ramGPFqt1tRj30W9PKZaiSRRzRK1uKnITX4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujCsZ4uMB3t1spo3UXrkzkp8EMVP0sMttDKHvOnHZ332z4WHHsGwMmSfEQ0dWED_S2P6HpR1nSYhCjlQPX7CcuO-JT67F4FMYwf-DkGg9cWwqIo9xf2xhdj3IVwyAeQrteuZyLiCJUPNislvY5L2BHVY-2Lbc9Prntg3nAl86vv3u0qvisaBVbTf_8mehLCiPQa3gICNPVgpTi-2XmoKuB7aD0cOecNe9iKXVBX_oI-kL_gTXuGeKHR5bPjR49Ht-VCrlGf95M16-i09rBxBQGbF4AiC2HN-Hf5cvW3LBhf5uQKdfdCzjPaXmZU4Ah8VlGceYrqHzjdvcXzccjBGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJPmjhYVLPOpkXQugpoJYkvbKOKcPaB93csg52ro-VeFl2BlLWQ70eMmxkNcoUsLHTZRHfMaZBAdu6Le72Q4uMpd0DqAsav9L0hisksMeUHjXiqlCtPanNCsjLNhTgI0mhQ1a2p9779apqDnGDonnEAc7NgMjPTz7nWotTsNzfMK3vnAlADAMi-22MuKA4sHshqOyN7Bpr_OsAXxpKyVMN3ZUkUVfdj66ICIy2fib1QStSDnPm06FO_O7P--IyaIiUpYd4FtPLLXqbXpDhsPcKF-VcLDeYrxiBi3NkqAGPywilfueya5Np3MAtCgugfMiSSZL8NlkGx0S6FrUB8tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7TcdfIK3FkabnYFhUHe18xvgeyreGftTNUX-7y-ajriPppxX3VZXWWXp-TrE37lErbAQXSMXJBXk0FfTJHFLYgqH2OkB8-zfjcGjnL2P9Qw7gLOhGITIoxQeSx9YV8vZWu6o0Uo5hV4V664votVD0xzoKRzfIBOkGqaV80sKpFucZZaSLtWgYr4mUUTPNNLIm6aH6yG4wtke7RngStG-w58wc2wP38amrGEqoC4dOQbobnNnwJvbR9dMnmaKdCMmWQTMbYGXqdB1jfynreaMcBXtkU7yrfGsWkNqoV4P95NNBeLXcwvgn_ppAHwXqx9_TVeoq7f8A7nZukIsthkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/30977" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/30976" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdR98oeAjXR9X9ao2zqppwMfPcKnDUd6CnuJuFA7sKPwufZ9t0nmJvmGN4_CcNYFEpI2pWFqHM-4f9Za-cjKl-iAnlVOKmO6auYLLIhiB2iIIRdNel4tlhOIn0VcLYgoMTyNatxRGnG8j7uD8Ei_bdpZQeMnMHfP6H3tg3RSy_tU2YvZSU5hTkRRqsLwX4IlWc3Ghod_KKXwnkhA9uCspu-n-nNYIghv2n05g42qoXgtzHrufDUtoz5KBiSbNaAj8Tekk_OYV1vGoMS0V6lLQgHbQYMM-Dsk6OLS-f-LtSzIPn8na3f6Ru7-47sCnueb_aQC9b_YdntlZECAiie5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی بازی‌های آسیایی 2026 ناگویا؛ چین با اقتدار در این مسابقات اول شد. ایران هم ششم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30975" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkrSG7OY1oVrs423M4kJnK0lXqknFRBR6cPaTJP3fh8TS3_Cg4uTwBbOFQn1uecdMy5REsTcCHK8VO56w3mxxontaIFgXwJtMASn8U_dFrss7aMlBbqqdxfSmsW7oIzaMG176iyQi_qoOqD3Bx4h658mQ5oO8T_QieK_jZ_T8DCRzf90yf70MU6Exn4BCF3QyWd5B_HNvyW7QmmoH-T31uRffeGHukEl_mjH7Jhcd7K89yPMES_-bJvoSBkU0GI6ZCSbQKGz8P86f80pMuHXSriQ3KWtKP4xyBP8VOuvjt4IeWVvM057KwPtLq1eaU3zOHcluxDQGj3KPji0Qb4ADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30973" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30972">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30972" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_8yg0Vs2E0JVvlPvzAYrxfZxXjWJNKoWFpqL4PetnnlPeyOPwThfSRWO2-brv24Bx3sw13AbdiQT1RwO-y9vlOXa3xIwF5cw4u_bvEdZiUyJmeAdpvNcqduZqMUM5CwZmpQxYC5jKAwCaKZJt9qboOA1VVyAziM70CivnmUOZpNukBhXBIVp6WmXuLMgnDj5U7iyYGY-EoyguUQSjZyw-XTcPc-SoN6vd37Y5CQO0ulU57qki2GLLk4_h-YtN2BTagOV9C_HC3qH1FdzF-uGQePBZJ1wZoy-tAziPJxGaqNueiZhCWQnKpmpX5syc1ChCMl77EkxHAJHvjpDeTV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از شکست شب گذشته دهوک در لیگ عراق؛ مدیریت این باشگاه عراقی تصمیم نهایی خود را برای قطع همکاری با یحیی‌گلمحمدی گرفته اند و نهایتا یک بازی دیگر به او فرصت خواهند داد. یحیی رو بزودی در لیگ برتر و یک باشگاه بزرگ خواهیم دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30971" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dowoD9EEbySk9VX7xoekyF_-VxrIIG0WsaeoP3FA8i3PdgmZWBU9GBauof_DNopgpTN4dgiLM6LWvPQek4hO7-4Tdyb2Q8vkFAVd9ttemGVTXwlVAzWV8VyI5cUFlRmpT9ZqeH_gT9K1uH54hxCSr0gS1wjF-QrAbbz35tvzbd_hZOj3bXjXB8BDairtLgeK_62KL4abG7eb4UWMlbSwFZyLMgmjTy0Wkzf4CtGcy70u8CLNd2fHLNvdAglIbrjLeHr_h0gVrjz45KmEqebYYVrK9bTxNFJfm-TsifGOj1sJIBScOGWRK3Sasm71womAk86Cu7vF1UxzPaRWimqrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارتینلی ستاره الهلال در مراسمی که اخیرا برای پزشکان در عربستان گرفته شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30970" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZMUcbqejwraHK9Qa6N37bED2QPc63hQ4sGjmsYzxsj0Uessph5ZjrOzGDXN0Q_66FgYDQQ5ktF30v0KWR9PmTxJtNmSnaG5R_Tqm2gpG0_FL2mABWzvZV8D0RuiIp54tO5Y8oJztigoV9QR9e3t1SRk3rjeUgUbYhcDzp_Z_xWajYEsmWwnCUpSrNAIIdqLOTMvHJd5AKrbKqjhsPlwoqzj9yxaWaisnXlVVtlX294RRST3YU6gpcKbWsa7HHI8Eph7xvtOBR4JYr3Q6-mEFdOK9bsxzsYU2An5_e1tx2UiT1SZQyLPXz9SB1JMcQnNUKAnFvE1Sfnscv2KKLCKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30969" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXSiyYKZmJTDEy79seHB5zOvqd1bAnqkUX2K8DbFEk9uA_FLmSHwTm3bDWIUa19YLooeC81_8qynaHxwfQXsUgeVkXlKTPDSfALXdPL96PLZMB7ayjbHeVlTUWHJJUZNB-nPqCm76s9zr0QqS_5026Wz4ff-vOscHulEbdrwO40Bsj_mEejSKbjnjT_ZVWqsy2pTvQ3Op4s4szdXbPhn4oErKgOND_y2pKhX0ad3U6UpfvZLX9QhYCQPwFea-fF6Z0IAhgHd1CjdwhwBtbr_K9B8LYJOnhi4CrOH7s-oiqMjsjOQHBk63XUw82rBCjfsEbNPswMRh7G1NtLYFYXoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30968" target="_blank">📅 16:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6_nW25LVeYqGYYLMz_zv_UImTAOEl2sQ8ZffdU2R0ejzPp_xg74d7qzDsi0ztB48FSZGUk39WftSW8OaOgHYaA88CcC3BGrCxN0WSr3W35xa4RSWpbH2IsYme6xXnZxv05xk7YcqRkVMxdNhZF3aYlEbw2whf_l7uBY_QDlxa09pec9JqlRE8eTS-mVjd3Xn7iqJIKBd_r3ZSM04YaDyV8oUYlSvvBYtqXd-DEXy0zIGmppZ9RDUGXOWZHrhCjFF8-iguN5hqNfYyTFoqrzzR8hag1NBC2fLCZnjLhlho4ecwOFl0iLJDF9qbXhyef5_yqcygCUfu1zaqxZb4ezEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فدراسیون‌پرتغال‌میخواد این هفته یک جلسه با کریس رونالدو و خورخه ژسوس برگزار کنه و مانع‌خدافظی کریس رونالدو از تیم‌ملی بشه. البته خیلی بعیده رونالدو در جلسه حضور پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30967" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEBdqdYKOq-ShWHvT9G8ZYP3TwLVMOZDno6L8xvjAdgs9xKCzhcrIz6YUBWLEVqILO0bTkQ4_-FwveKEzSoXmOmQ5BkM77ug3OYFrWJVV8Q5ACslpWoPEVjbzlMCUHySk51i6ZZUNCnruiZRdKO-_xdg4wgYVBS_CaopbYP4jLVnVRZDDBDRJZy6AcqotwgQivtPomQZHy6qC7Fy6jfjLfkxXK0qwRPnK3FOpivlwRkQraFw-jfyTDHpCAsvVdGPbPNhuZkfBEDm-WmyyWRmCuKRKTdUnEaJrGTdoNwXvZg5o8AGRdlkgKIYkICwyM6LYumhiBi2zfnCW5pi1Kpmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLEltr15IKnwRDpAzTj6CuPzivyOO6XxOtuqegrAuIEZFVFnGBZdUreH40aojmoesW330wiLukH-j-NVnQFfMAp6R_789LSRBmG00XckJvPs0J7NgSw6D5POijErgojYkgR2Gu2xZwBkLbe9ty6hZwcOge9fASkqGxP2ZfmpVxoIGVnjU4Tx39hDHmPBPpikiAI8Wos9vsrSpNE9Ku-HFQDqPMzsphLsFukgpmkAsBwBlQIbHSPG_7QLy_OVhlnC3A9v9j43Q3m1wE14NYzNLcfZlKW6EIbmMxo1W5J0RN3dpHTOgHc1z_pBggiPQGYhh3QrVIvE8LB2Av7evcNcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxezVAATVBBN5xmNtp7AxPCLrY_2wQmcHs6PE7Qquw9jpntu_mZ-egn7S0iSfmBDdLEuvZTfQDdVfo7-JQlxRl00eKxgJYe6rIlUiClJnhym26c_R3Hk0JgVJbon4i7_wIWJl0SjXB4enfP9DoFbC0tEMpLJOyb32SUfQBZylQ090lr_B-c1jhM-saC79RqUEgfdgB5Mb0cBt18q4nEpVdyUZkCUSYgCEJFa8qZYgKEm-j2HzEyGFi0szox01FEhPJlnjAVfeARqvWjPBn-0H_jxMgzi4SzmKhUW4nTiR59eCRyGjY6I548SbGi8pDQP14D6GYBS-RDoOG3Yxiu_qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiQlmv-784f2T_tpSDsCACTFcPZq8QyISN4gH-jCKHwICqEAlqkU64KCZ2KDZdWHhy3QogBoHChjLn-H03H62EjETRoypBcymvWHTFuMOd3mgBi-dOGGaTt3zNZ2tztshPpLjBZqEinqdopHMcGc8TGE8R6ogh6hm9NNRHTcJb2z7PTofGtIS0KVNybDOWlk-MF_n4VlZIaMeQRUXnNDnWXWemO_qiv-6RSZ11FE5NLmj9NJB0tHamIuQDKVjctl_xNx98im99iF8l3rleDZ_4cm0K9Hv66wVspfu5TasVDsrpBYKz4v9sGMwjsQQM2_8MDf8mqzWM-bS-eo1gB0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=N9XNNzhDPRsL2zRCy1kEHjvleNk5Yp_zz3soekRQrNr2x9XP-d8qhpl7nt17YeNhBv4FL1i2XmbJSURzG790Fgxi5Z9L6pjgn8Cb43awLm1Znb_MURxIgutomOqTfSXTUh__tXKW3EQbnOmkUvziL1BKf7Lug055HL6JxJNQQvnA6vqPhhy-bOMGUNS1qbenkc16nfTqHeFYrGd_Amakp8dvxTwi5qvsKPM5osNPj7bFkvQd0_wUSxlAZiotntTGZscpHF7yuWBlSl7ml4Hw7NDfwNelVvCdYwVkYtfSkw4IFPxtJl1GImpiXUa2RB6wEO3XQXAZMggRG0yek3vJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=N9XNNzhDPRsL2zRCy1kEHjvleNk5Yp_zz3soekRQrNr2x9XP-d8qhpl7nt17YeNhBv4FL1i2XmbJSURzG790Fgxi5Z9L6pjgn8Cb43awLm1Znb_MURxIgutomOqTfSXTUh__tXKW3EQbnOmkUvziL1BKf7Lug055HL6JxJNQQvnA6vqPhhy-bOMGUNS1qbenkc16nfTqHeFYrGd_Amakp8dvxTwi5qvsKPM5osNPj7bFkvQd0_wUSxlAZiotntTGZscpHF7yuWBlSl7ml4Hw7NDfwNelVvCdYwVkYtfSkw4IFPxtJl1GImpiXUa2RB6wEO3XQXAZMggRG0yek3vJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZeJo30Up0Ou_i2cwkwo9zS6LAdWr9mcSOeGZL2AykeLn5o9FwI3K9smYa7fseS1LuuP28ITAAkHQKHm8O6MyceM_7baeFaC2nVPXL7fZ9Z7aeSZpIvtiDFxr-uYRUfdiX_0FislfwycwUIEhnjJ5cLVamhS4j3XIb7KAr-fMv2z-GXukmyMlnSTx97feygE0awj4aC2jpJdpsfeLTOiszn_c_75fZ1pY-80UoJmW9ThH717L6HRktPTtv4RuTXDaB2xBDV4CXb_DQqlXBt9tDWybatPqNgYLG46S_IFQ_I4qMHNf06gAhJCKRfzmKaR3z4VcCghjQEibWmpfjX59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmTwTUWU2HVgglHCE-cFtz_271SAFtWSE6uwk_d_CZF5MG7MNO_yYb6k8A8WGUpvoOVaS-mTmolcBGniPAgFn_gBAwIVIrhenDYEH_3r42bGozJ--M6aSDw4TiiXuoJXbvu0nz6T65vOuRLTwAWwLIvlhIF-AhdEGlqXI3ePfuS9kX_OZzZ4Y0m-FXflCwS5DhFvfANc8EEmW-Mno0W4XAn5SZ_YOs0NgKNUsx3QWTUoX3jWL1j-9Wp6Xm8uhKTVkt37c2lqNE4G7c9gP2MuDuFyyZfOLYce3456u2jcJiRhxNHRGDXkSa-cF5t5a73erWcvOgRij9K3JS-wVijWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30958">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XneK7BF4ebwrXCGvRzujr9mlaMd5Q1o931KP0uYNZ2Wc7v5nTgt-uy3GVg0NnKmky85Crl1-z1zzefwPQfLNYvUZfS0eRxR_NrKONVWkQ2SrTvRvgX7p-1sle3WMyPU2Pt0Jx298P6tji9vsyetvvfe4tiUhXzH3BFrBHTrqGxjEQzzOWNu52EYBzEDaP1CYAcYeWvBl-4BwMwP5Le5Kqwxj3FZfGguknwB3z9bx1FG57rfOCPytPJFMwZnKlD_kIUZ_02HVg6Y5dFxwzs9G5V8EB-P9ssjfPjw5EYzrQLwCSnqMT04F3RFZiesrZaTB_277IgIe4y-6yBMzW1JY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30958" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30957">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=roY7DIErr1btn3M0-ivYVQpar4i-sEbeFV_u4axNhlmR83czrzByEeonJQSbCZmTlvdp716FhvXcBnLtS7E2yNx5KFDOW4_Qf1GlNrfYr1iPAmKiBgJKNpav5Va8Wl4Cd7woJGFmaAP6f3ZKqqy4xN6luz50WXCfLsFBJktsmmOHfYgfr1IX-hlxnWTBZxYRiZDIMywauuXmJuJcdTEmFglKTUd8QdQdORIdUVQ27Wm-UeOZGQpRol1FCWYsfM4TYIrd50cPN6Dm3FzFrr0_l0wYwyOt1n5Nm2lmlP3f_5ZgqSi9rPp15Acp5rh8KzKGodHuko86meUToRTYAVXHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=roY7DIErr1btn3M0-ivYVQpar4i-sEbeFV_u4axNhlmR83czrzByEeonJQSbCZmTlvdp716FhvXcBnLtS7E2yNx5KFDOW4_Qf1GlNrfYr1iPAmKiBgJKNpav5Va8Wl4Cd7woJGFmaAP6f3ZKqqy4xN6luz50WXCfLsFBJktsmmOHfYgfr1IX-hlxnWTBZxYRiZDIMywauuXmJuJcdTEmFglKTUd8QdQdORIdUVQ27Wm-UeOZGQpRol1FCWYsfM4TYIrd50cPN6Dm3FzFrr0_l0wYwyOt1n5Nm2lmlP3f_5ZgqSi9rPp15Acp5rh8KzKGodHuko86meUToRTYAVXHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
زیباجوی عزیزمون با این وضعیت بازی مقابل تیم‌قدرتمندهندهفتگی‌حدود180 میلیارد تومن درآمد داره. انگار وینیسیوس واقعی رو کشتن تموم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30957" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30956">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODq3e1n33C125dTCfC-gSG0QqFV_Q7SueZNjzBn8QrSIW1dqdsu-i5DzOtl5ITO63tyIALg30M5zuxh_zABppbXCJm_53xjwVr7gCBQCfQG9vOAdt6k6A84aukm8yHI9vZDXuvpm9ZO_lOS8NdoLd_IgszObR7RhPMaui8cMl8jL4b6z-F4va-FxL5iz7kSqATA2OVPP2Dss-wSvvZTvhWU9M_59RAuCo27W2QE7B4MNroOcTSJpzJ-TyUpFLKVUUF_45f0QRzGX09mJuebBwWWDXkJk5gJig_v4DyslHXozdwy0ExXvgJZOKHNjcnXFeje0kOs65qU9qKG_I3e_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ در صورت موافقت امیر قلعه‌نویی تیم‌ ملی روز سه‌شنبه ۱۴ مهرماه در استادیوم یادگار تبریز به‌‌ مصاف تیم ملی گینه بیسائو میره و بدین‌ ترتیب مسابقه تراکتور و استقلال لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30956" target="_blank">📅 11:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qG0fARIRJi8shZCjDS_SeNtpiCBXs9MR-_vk8qCaEvksAutxMhisuw5pK6jbaE6X6BULfgYVEZFPJkdBy9ERpp0VVDyC-5mF108IrpOcadm4825XF0Qa7uQir7JzL33o8sb697Dve6C0pGtF-Au3lkhC8hvU2BxHgUajyvSOFAV8UUZcikQbMsMQxvWQ8HXCNb9n9xTFWvXb6EQ5H03mvI1pBTlmbITWhs4c_Lkd9gKhVzTfJKRMBaCiFQDy3LfLcGIbMxgt-wgWMrsw2Q1PYvasZkhulEURqR8ImfHa9RSa8UfQxc7vxj4hH2ce2N7mtIPV7SUbqk8_jZB9HD78GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30955" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30954">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56284423e.mp4?token=rJc4PU5xJObCsBIZcilYQqTAlKJIB22D7cFD3iyohg0wYRs0sdY_wu9hB0PDu89UO2_zBgHYTQuvC-vX672Mhenb1C8jpI9HX1bjLhVXE86vacXGtJNa1KNvLIhqYRFWi98GrNyhLp4vUb-x2rfkx7_iDk_5Y_GlLbXI3CObF3ctOTPCyhhg3IWHzZ1KRkY5Gi9kYPnjifyMqr20Hzr32Hw9EiXnN_epsbhZXbQCih_EUEL1Q4-t___82bGJDqhJ0o3GnXzcMS-5JoCVUpZjD6yzAwpjWrXdfCWAvEUdW32Mv9qgXP1hvOCdAZr_4njPpewzobSx_fOQ3Yv5iN2Ql4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56284423e.mp4?token=rJc4PU5xJObCsBIZcilYQqTAlKJIB22D7cFD3iyohg0wYRs0sdY_wu9hB0PDu89UO2_zBgHYTQuvC-vX672Mhenb1C8jpI9HX1bjLhVXE86vacXGtJNa1KNvLIhqYRFWi98GrNyhLp4vUb-x2rfkx7_iDk_5Y_GlLbXI3CObF3ctOTPCyhhg3IWHzZ1KRkY5Gi9kYPnjifyMqr20Hzr32Hw9EiXnN_epsbhZXbQCih_EUEL1Q4-t___82bGJDqhJ0o3GnXzcMS-5JoCVUpZjD6yzAwpjWrXdfCWAvEUdW32Mv9qgXP1hvOCdAZr_4njPpewzobSx_fOQ3Yv5iN2Ql4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از سوپرگل پشم ریزون ستاره‌های فوتبال درمستطیل سبز؛ گل‌هایی زده شد که هم‌تیمی هاشون هم برگاشون ریخت. عالی بود واقعا. از دستش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30954" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30952">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=lI39SH4VDkOXqcem8X2dxb83dUF4RQ9FiqZVjw2z6pm4mQ35l8GYZu52PQi5dmy9h4zC5z2KDhV-mwXJx6HmdIRVrgp90lc0bUNsEKekZ8PlyaqQDCwKKxIifjLG2JVpLn0Nc-3MHAQI8XmZuTkQwbukMZx-NtIlUVEO7GEMi5T4F8pFf8-FIg5acjiC_p4mKkaJzKG2Mku4SHEvz0zBNLt6gmmhj0ruB8J_U5fGWazGTxH7LSgINJvZPovHq4cAREbeed7HDX_HmnpjwleMFqyxLQNB2OabjhjHepSHrDR60qVaeBuvRJcvPSbB1fu4yPbWpSNRv5gvGwGwD3MREzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=lI39SH4VDkOXqcem8X2dxb83dUF4RQ9FiqZVjw2z6pm4mQ35l8GYZu52PQi5dmy9h4zC5z2KDhV-mwXJx6HmdIRVrgp90lc0bUNsEKekZ8PlyaqQDCwKKxIifjLG2JVpLn0Nc-3MHAQI8XmZuTkQwbukMZx-NtIlUVEO7GEMi5T4F8pFf8-FIg5acjiC_p4mKkaJzKG2Mku4SHEvz0zBNLt6gmmhj0ruB8J_U5fGWazGTxH7LSgINJvZPovHq4cAREbeed7HDX_HmnpjwleMFqyxLQNB2OabjhjHepSHrDR60qVaeBuvRJcvPSbB1fu4yPbWpSNRv5gvGwGwD3MREzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30952" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30951">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=spRmRo9vhVclsB1pnA4uKZIh6qCATGggAndDk9iTpP2S6gm0mCKRK5d-ahDyfeE6WuRiviu8ImbFizQH1aNao6teC6IaEqvZZ-2MwktGN1VmEDvugTeHkd8QzvkmYlUXylpgp2fUCZDPqo4RaS7Qe3FYdK1t4Vu-0n65hbMk-8DXigUxgDwEtgs9uIUe700ywjgdgnDA9zzKgW30i2k0PcVhKjtRWfDLtDW2mTa2MqPGOu6yJ0uCGiaNvzEa1DAusl_lS5NfXFPFg37YJXaTGQ25s9363vbDoXqp8DeAnzxjJ6Z9e9cloFIYZfAow4MsJxoXV4TV33T-v0sevlEosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=spRmRo9vhVclsB1pnA4uKZIh6qCATGggAndDk9iTpP2S6gm0mCKRK5d-ahDyfeE6WuRiviu8ImbFizQH1aNao6teC6IaEqvZZ-2MwktGN1VmEDvugTeHkd8QzvkmYlUXylpgp2fUCZDPqo4RaS7Qe3FYdK1t4Vu-0n65hbMk-8DXigUxgDwEtgs9uIUe700ywjgdgnDA9zzKgW30i2k0PcVhKjtRWfDLtDW2mTa2MqPGOu6yJ0uCGiaNvzEa1DAusl_lS5NfXFPFg37YJXaTGQ25s9363vbDoXqp8DeAnzxjJ6Z9e9cloFIYZfAow4MsJxoXV4TV33T-v0sevlEosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30951" target="_blank">📅 10:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30950">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=u0KCu2aUdi10c-1e3G73J9cWqW1yRIdIjdWbIyfHVEGkftnGZdvpfyn4RFQuC6IYKqwSb20hX0JAyJNbd9FSTQ9awLwXOSw_QlMp0hB3UYqum1XerB1-CPUonIj-15iBORssJX-Acz13NH5Qz7smho2D6dtu8O4uytOfaT8B-MzaUwuU6ROmkIhQagro6GKp5bsA7y7tBLr4P6DXy2LIstXONfPV9P0fQcGJ6o_pJW4jjc8wR4z2ryj5aJVt3S5gGvwH-3fq1sI9zSXdOTw3puqVYFs7tvYxlUk2MRSkScaKfinnPoEosdoDfs-W9J4ULG0Bx-rBjdCicNuE--V5HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=u0KCu2aUdi10c-1e3G73J9cWqW1yRIdIjdWbIyfHVEGkftnGZdvpfyn4RFQuC6IYKqwSb20hX0JAyJNbd9FSTQ9awLwXOSw_QlMp0hB3UYqum1XerB1-CPUonIj-15iBORssJX-Acz13NH5Qz7smho2D6dtu8O4uytOfaT8B-MzaUwuU6ROmkIhQagro6GKp5bsA7y7tBLr4P6DXy2LIstXONfPV9P0fQcGJ6o_pJW4jjc8wR4z2ryj5aJVt3S5gGvwH-3fq1sI9zSXdOTw3puqVYFs7tvYxlUk2MRSkScaKfinnPoEosdoDfs-W9J4ULG0Bx-rBjdCicNuE--V5HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون یارو مجری بیهوده یادتونه که چقدر راجب فیلم عروسی سعید کریمی بازیکن سابق ملوان گوه خوری میکرد؟! دم‌ از شرم و حیا میزد! حالا در نبرد دیروز تکواندو این الفاظ مثبت هیجده بکار برد!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30950" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30949">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI9Lko7ylXRU4eoovyG_aNtchax016pZ-hcqExP-JhR9LcCc8IMdAE2UKK0vO8vj15FH1tCesSyMv4weoAJcB0lcXOvn0IJ9a440ZiE-Y1M_Tmml-PpVCdZRoszIAi1v7GpgALu5pn_5dVmdPV9KrNS4ZsZn0aBM7q4o0fh5tWLUJ8p7gxsS6CiS5N_sHWJdG1S_Ge4bCoGhib76NUa3Kf_IFMCB_KNG6zmsqtFPtL7tu6yZgx55tZC1LXZnISob4YrvXJQyBs7vkMtwxpi70RFRCapUb-noN1ai6xWvQalcPHZcXOMiu-GWi1Tjaj5BjREeiA7Xqy2-ANtBTpym1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای خبرنگار لیگ برتر: یه خانوم در کمیته اخلاق اعتراف کرده که با رابطه جنسی با چندین داور، برخی از نتایج فوتبال ایران رو تغییر داده!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30949" target="_blank">📅 09:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30948">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-Ty4R2m5z1kokphaH5SM6h8--V0h_qfquQpu1W8fNhlF1Wt2WzCJ_1tf3__U8ixR9I7LHWjs2Q0dHAqw53qZPSoRrbkZSsr-7Ap9VWL-QF8bhC8B9PKgWaXSgaTuDO-pF0TapEaLEX5XIVAtmfxkwku-RDEPaPpfMNM7pgPwJMUXnwD2jSXLrxQ-8Y_ouqDDjXZdg6O90qCWTZw73y6WiXvST_N98-rVBphNy3mK0tcjJ66RYv2OabwK4ZQncBrO8KkS1XNnscpDrxy2y243oMQLBEQjsS3rjSDcEX2XzZr2lGQJQVAIgAK59Ewk1SNuSyDTNAz1fNK6e0M7hTYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30948" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30947">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0EJAgKrpI3xHjjJCZs6s2UGd6obQRYr4kQlKlEwefytj2yoagjAmBvPxGo2Y-wJxJkjhYckEMknN4oXzsidbLFM3zmmYQOkMoa3A8eCC62-clZ1hyKYia6efW5-VWL2sS50P1QRE1ri-LXKbV-buSlKn9ZaTcsCo4iNG4dcjh25ZKzRIuBL5jGE_730Xdz0DWKRoiTuDfC4nHnCxJowtb6sA8w6w_ORBELyyhrt5EEAthTATlhvGvYeTn-7yTrifR788JAB2ch7adommNej_yexj3HR-R2K3H5D4VnMDC0NMfnGhqLyq8gKg-HRJjaSd4H4FpMtl7pkSTEu4hTUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه روز پانزدهم "پایانی" مسابقه تنها نماینده باقیمانده ایران در بازی‌های آسیایی 2026 ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30947" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30945">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umq95ds_vEgIleYArvDCDkEB3XhE6B_Osbox99-ZShmbBQvVTEQYrxadmPru_p3ndWoUQs_SpiJzXzLnydTiaO8JrI77zQwDDdooCVUF19xEM5YMsi7BOlftFr4Vr1XJ-t_xUoaBWnkiuvZdTkpr3ToWJLe8rWxY6dPgackBVmehhuqsg3CrUdfwi74mbqMRnDutUuESVwNHwBq4pifbauYe1KzKPtbTzoBH_Y1mMDhzQQl79Tz9Cuzw4cX4ayOo_ebaREzDI1O4EuUs_57jqNG0Xr76OE4lDiorcHKSnShMZbKBwLl3fQCa6UKd8MK8RRrcdSFcdtu2l2iTBevErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز
؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30945" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30944">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRkoReJZ9CQOjArI-FL-63FTUl4N074yvv1DGHdxKUgwSUBDm-zFLT1m-zw2R_JE1N6Ya_pyBOfU3GoiOsGFfFAXMSRNE1M4zmhSED36ic39AFNrrWq05iAdS83AVfYwRb9rm5y1Kl2UfzPMEZwHX05zfseA1WfHet9DSG7QQppf3ve8rs0HmFNaJuKRX9BYUipzTVs3cZhIa1s1emdUni_FKU_YD0i_ntYggGUaVFWXIWm9PNWDa8zuM5sMQmPQsXtSAdjJ4L4L3wanIF5hIhhnSX_p2GOuZ4ujoAK4ZjzFhR7bmYpVZPoOoKAQ5Jm_vlfYEMxBef3uNoF6MQWWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
تحقیرکرواسی‌بدست یاران توخل و ادامه روند فوق‌العاده اسپانیا با دلافوئنته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30944" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=ZAq9HDJ5WqFEMhGK6sOIEqOteaJ0lPymkSb6mMR2VeSDSpIlelK2WVrp5aiuwjwMQL-WrIR1yk6g-kc5YlHlPFOhiymz1nf9XLvLsFH3pco3GCgb2YVnyin5Jxi_qpd6tCxpNqrPNb36E6HUREAZTf11LB2wjdFBO2NjPYdbiJ0Ippf-ALrSwRBcC9qfEwbeg8E17qoEPlcbQy0kNGBYNlDZPNHDlun-W5Q_fL2Y5DXa6u5Mm08iWVTI5WdLtCvlplMIgJ5JkAfp9GKwGWVxglm9P6PhUPz8sfaxdsHCX6rbzmpCntAsWTJmkDjtF18dYjeCtSxZ0vF_SmgCVQ7IXxD7DreyzqydyDXjphieilwl8bFanntnllc4WzvEKtdZIkfXPYuZV92M3zuDDPIehyCKCZ_PXYCOcdhqYEHgiod7NcV0YW4DawHGzXzN-HT61AYtEIiSoKvkcr3lOQo4Yoax37KmM4XR-0H3QLQ_GgA54zEiih4KntWc6XxM5z_ktCNQH0j8mXipDgrFimUOwaAT7cjyErNyjbF0_oVizClXrwOdEZ-VFogVXz1f5-L_Y0tudOKZcUV2pdqrLWEzCPwAcyVuzkf4OY_3BzqEnhADBMgvBd0vJdYuwOtZi6muSaRGgHTgYjaC5pL-uKEL1fiLq3myX3iRmfE8w4Wf8JY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=ZAq9HDJ5WqFEMhGK6sOIEqOteaJ0lPymkSb6mMR2VeSDSpIlelK2WVrp5aiuwjwMQL-WrIR1yk6g-kc5YlHlPFOhiymz1nf9XLvLsFH3pco3GCgb2YVnyin5Jxi_qpd6tCxpNqrPNb36E6HUREAZTf11LB2wjdFBO2NjPYdbiJ0Ippf-ALrSwRBcC9qfEwbeg8E17qoEPlcbQy0kNGBYNlDZPNHDlun-W5Q_fL2Y5DXa6u5Mm08iWVTI5WdLtCvlplMIgJ5JkAfp9GKwGWVxglm9P6PhUPz8sfaxdsHCX6rbzmpCntAsWTJmkDjtF18dYjeCtSxZ0vF_SmgCVQ7IXxD7DreyzqydyDXjphieilwl8bFanntnllc4WzvEKtdZIkfXPYuZV92M3zuDDPIehyCKCZ_PXYCOcdhqYEHgiod7NcV0YW4DawHGzXzN-HT61AYtEIiSoKvkcr3lOQo4Yoax37KmM4XR-0H3QLQ_GgA54zEiih4KntWc6XxM5z_ktCNQH0j8mXipDgrFimUOwaAT7cjyErNyjbF0_oVizClXrwOdEZ-VFogVXz1f5-L_Y0tudOKZcUV2pdqrLWEzCPwAcyVuzkf4OY_3BzqEnhADBMgvBd0vJdYuwOtZi6muSaRGgHTgYjaC5pL-uKEL1fiLq3myX3iRmfE8w4Wf8JY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BADzANHmdqn3zsLfKE_GmHP2WbWcdRWSmJzpknQzFXti9C7fnIOH1GBtTaqZDjFrmrksqErjPJ79qxgUSX62YBjrFQcpqR5HHtsKs30hQB7IpQkhYZ-B0eZ3uDuuxweW2asoRfwvGHYN_noa1ebrYm3Ax5ieUTLWPb9R2gXjwkyPVqT2N_nWj3xSwvC14b60XuQpCiy1Etrjsy-BgqHgeBDGfHSk-E_XV2JHPMDAbjb499wz6uAfOFjy_ZmgkOBmA3QO1G9NO2IjtCSOJqrzFBFKpI37VEZNOPLEhoSNja3hbujl4M37hIQgR9yez07iZ5otP4hteIMJeR1g1lzqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOiMZ8NShm2o9_MhxAFC01KW9Tagp9aikw89msKGeCRDbwjelojgJVW72WBC5a0MUR-Uux7_ok6pGZL1h406ETBQ4a6axgJEr_LyIGetca-hhPlj34c01VZDAkUDBSTNv9YSfrgTL_YdzfrsQjKiei4AJxwqKwwqwrc40KbdoyghNyTRpyUAKRBSxrAaZ-d3ZNa3Q3CgHK2s-o6s9ULU-YyuzBXFixLyXyU5RuZ71b4L_OrHssLoW9sPDWlaLdRmrGHgW_sofhHmbJBRbpNNjfUS73ZYrXdXs5qPkhOhGOSd0afZGsbybnXyi-csSAYc1J_igamANYS0_jP2eUlbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow0Bc0Eqp6JoYX6fpatEjE75vrVSIGsJmxErC8CvVtuDXcUTd8lQSDDxL6ZiFh7Y1eNp5RQdqDYSH8kMaNwXz_V20u65aDyk31ZZYdlP4jQ_-Ykyw8phUzZdeJWMYQcZhWdqmo13S2rbCZ7LSmavajv-rcjDae6qK55A15IuLOChq0nkG7LggjVKOCh6UJw_3FgaggUFt9OFtzr_QgqsPfaP8Xr-d5pyY_H2Wc_CYe8Mb0-CyIzVqoAQi2kAaxs0t4dcJ-SKeW8nqkV_A0B0EG3Sw3lz7droYgU20nnpXN7gzK3zmUrIOXRBqJSKEMKxSdlb4fSjym6TgpNyi8xLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkuoUKUhKeKASYZloKZVExyTMyoUg5sGNmWkVAqfoLD_FEeXfveGr0kApTr54TzJjhR422S9TEqByvBzdjgKoMiPnZVu4ZAXzf7RBPS3af38CfRgUnsRfiJlOdm4s4hx9FzrC4y24zCy4gL3mR0UJ7iBIzxk_POgA4_QXmYtjR05uUxu20mN27LAiDGVuRZ5MCF28ITvhlvuJODYdZrk0V6c-3OFqKKJalrOvGx4phdCYkTC_4_CXKn5pTAkuR9WXjruRCAUG9SezVa7-2cs0KBdvQ6dHan6M_0H7gEitHsNdWnBccYsHWjiZmwmt8aqU91QXFysmYECjuiBd0oygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx7weXn3GQKu7EArGp_dV2byfqz-envb3bbL7xqz5uXGBJCrx2UPwvP82sEmag_rmH9sT4RL-eZKBb5Cn7dXkbZEa0IAoVKX77Dr_CceHYcH65cbosDbFw5SrD2PqBfAwJd-WsICxiKVt-hPn2KN3LZE21CGwGK-2qMoYWwBHu0zICOXHSWYnOeW68KbRD8celKPcU6zlHKd4mKu84KcmsZAY8CBRw0Y2Kz0mhEMzHZyZDsZer0rJYmXf64506VgKGtSA8TlDrqI1NjxKqbpDlqHFAPoBqJEpgDTtefoxjO01GxTeqCaK1AR6lJRDqf7agkAHccUkus1LsmYSvbdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=fOWKTsNwL89iCv2lxX9LPhem-9MguuOUXZhmExMp7PAYtlc52cfPn4vhuzESV-aAsv7ld3qHtQI4GcfcnMBAeoUmgg7t6SbdybZ2kwO4dv7RLigwy7EBB3Lw_92J85EvNlIwG--q_sWjVOu_1PpcUaoNn9l5uK1-DNFCeYaJlFgT2oWOoAbPWjLknZdCB7d5oDdTwgc3yJVDKyI_pZvM2ZsqbZcmD7v4LA3_CFJmnmWv8uKC16rDGY4jJZlqPAuJnrjJJIIuVoRGxI_3oayX4q5-jdv_YAU-oabjmRht_qVn6yiUSul3tTaK9oTLTpnXLuugzVZ9RKhle_9X1Lm50Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=fOWKTsNwL89iCv2lxX9LPhem-9MguuOUXZhmExMp7PAYtlc52cfPn4vhuzESV-aAsv7ld3qHtQI4GcfcnMBAeoUmgg7t6SbdybZ2kwO4dv7RLigwy7EBB3Lw_92J85EvNlIwG--q_sWjVOu_1PpcUaoNn9l5uK1-DNFCeYaJlFgT2oWOoAbPWjLknZdCB7d5oDdTwgc3yJVDKyI_pZvM2ZsqbZcmD7v4LA3_CFJmnmWv8uKC16rDGY4jJZlqPAuJnrjJJIIuVoRGxI_3oayX4q5-jdv_YAU-oabjmRht_qVn6yiUSul3tTaK9oTLTpnXLuugzVZ9RKhle_9X1Lm50Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=TJmx3GWvqA5Jj-icUlT7Jw7QeuD3fmIrFytDWVmonnM8k8nRrjzYB5tlw2KswyF40azQ_d0X2ZXsWh3dThmNtAZzHIuzh5FyZXPR7YRUthB12ugEvzN4PjzMjDfQjQHvMGU6lu7If8FfGVzK7Yu5YYjxwmthlwBNAQMkTwkqWVwajKZS7Wu4NQgIWSZEjLHKOGDJLOGmbyXxwNUbFhjp6KU8zBE4k9SZM-cJ4qIiQ6rVyYtlDM8QQxSPdg3WgQoU6-L8IpCz2wz_s8BaFIqxbVoK3cHoqmjzIkpZwDk_dQ2dqzjsY5AHngDLe9P36WhiVDVvb4SsCHeAqZuP1y2egg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=TJmx3GWvqA5Jj-icUlT7Jw7QeuD3fmIrFytDWVmonnM8k8nRrjzYB5tlw2KswyF40azQ_d0X2ZXsWh3dThmNtAZzHIuzh5FyZXPR7YRUthB12ugEvzN4PjzMjDfQjQHvMGU6lu7If8FfGVzK7Yu5YYjxwmthlwBNAQMkTwkqWVwajKZS7Wu4NQgIWSZEjLHKOGDJLOGmbyXxwNUbFhjp6KU8zBE4k9SZM-cJ4qIiQ6rVyYtlDM8QQxSPdg3WgQoU6-L8IpCz2wz_s8BaFIqxbVoK3cHoqmjzIkpZwDk_dQ2dqzjsY5AHngDLe9P36WhiVDVvb4SsCHeAqZuP1y2egg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
