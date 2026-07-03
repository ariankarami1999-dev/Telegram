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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 364K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raw_V3scxhgMPK32d3vGN8DsVKKfyzX5EA1fALNuAMj4i-AaJwXwHaYJz-idojoKf39tGkiRTznG_j9Sf6P8_XmzHP5Y0wxa0HaZ0qOQjEI2pXrY7gJ5YjTg3asqaKhg9Aujpac3iAYUOF8upa0ohqzEKxMPjS6AHQj6pm1Wf6LuMqwqrMlXsf4eBVrcxY7GON04DxE5f18JKKgit4l-QEjDhqXVjubUbTZhkQVR3-u7PVKyeMZumLBjM3ih7e_AHo8oQ10eC_1rVFl-6Yk3pt2bchQGIvepW8O2_RPP0-KsAN8vInLWlHl0Mf4_9QnoL7Qt-J3HwjbCspr5sXJAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzK9tjm8ijbpG3UGBlluBRWppm3mmrM9ij9b_VauIOhYD0gpNSoDbjB5ApRPQwEklaBPZGPj-HZ1fU0CFFNb7iQ9EYsL3V_Oh4sw-cTpZ6BL9-KTgJjrGHeSZQbavhzCP8nzZSW-i1MevaMuU_rLls-yr-2CAu6icIqyrlDu6C-CyZJg3ZAKmAAEJdpTlUgzpCAXqD_BW-MUDFGNlD7wMaojpEk3c4Q-z8KajAFYJn-ty7iwKYcB2OjMJHJKRaIZWfFr90JXooG4UlaceFXQxDX58G1bZ_v1CfQfG6G4No85VOc6VhFLR-HPtm_U16D6VlRFaQI-9LI8N6cOTBPz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcevOrDPKtSbAQ7cHxSHRTzCm81mwmIHs7ZXl9f_GugWj619JQ0U429LbImiNh2DUklhUmTu-Y-WfXKKIRd1J_DiP0p3b-hScCzd2KWdB0aKkwXTQPMYCMvBoox2KSakr2Nu1CELlyC7ieLp03DBynNZj1WnaZetmQ2w1pRpd3bAdGTPsmQcX4TWWVHLrMV72hxYeq5M-DY2fx-Zw0HIsj__2MzFaDjOVP__kEQmK2PfFPyPTcpTg7u3NEbxcTZRV9CvB-uDbt8eeDnDIVT1OEN03n7hvItsY7Hiiig3bnmZnnw61i1yLNWWnw4NtH3LpwcA0iIbOxsKVVALA6mMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSl7x7bo8zqZysfbyp0sHOYVG4O2JCxcopm4Y18JoTPhPyKFTR2AoCbfymcY__Fj8wSEC6u_w2XnWsrHGRX2cZ4Qhs3f8yt85WI1nl1d0Tkp3Sz8jRBjnyYVMKWHZSkIyhCtv3-CXXT3rXqVr3pt7alEKekl23Aen3PXnRUXFaMGgZujVTd5QALgBimfRnhlOSbSonqJ9sPpFgrHV8oha2aRRJ0Zy1y5EEIlFqCXSO2N2mCTeU6o5lUrLq-IhdMeoGyMQvthsIXAERvOSlGpcnzbIGs-p5I-DZmNYsWfFixchEtCBzD14ETipYRbBpp0fA65rCZnAXF89xpSoOLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smy6oVAReFaVFM1Ts9ZvQ4wAh-9me2KAex4b8C8HQeR9cYiYd-9x6xU4ZGcTcweNzVZub_xoyc7gldpyWE6XK7jWUKk_bwh9amxTqS-rBZeIpI73ih-Z_ZjIVMmYc4UmfwPRgAJ9Bzwz7yMRLYmIPwVrxOTDrcFsc31MWktAtDwo0W4QX4VQjQ3PH4Nu61WM5NmL5FFM2hM3YoxgL2_vDt8LXgXyPUcPfxpQ_-9YsDb18YMq4hZYx8087MIM0bcw2J8pCxN_dIWlhndye34c_7X1nqkP3Mw9zueznD9PtVZeRoyypKEandwB9ms73yBs8TQ8nyE5_zgZh7CAwziWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqwdVP7f9epjtHbBWvFAFpB3aqept9TLqIwluw54_sohdRd2cxo-bqDJ6sUaI7kuvguC0Ol_OhUWdoXr7P8ZFBSLGZjCWeDZx4iJ5D_lzTlTX9zObBBSCe_PEd4V22KyV_IqbuEo4vX9jltFMymRzvlmxExGNnH0-sUShZxzMBspd3XkeOhTuMEHncFhWxOxoKb6IOC96podfB-K5w9BRrJC2iAzEPoOu8p_4__ji8LdcnBcx5U2Jp_uGItzP9pLCmV_aQsJWSBDSCfER9FA9fIN6kQWkVrRC-cagpj0BeAjj9CEDj9fd0lzhdCYXZQcfZ21j6hQnlw-mF0IWJW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjhgvK8kvbb6JM22Y_Z_2vsexBlT29RCJndJ70dKo0i2qf-W2-dbgLMaMoyoifUk8VR-LVgLTH0UyKblvaI-XKG36gxQOnKR9R1VZi_zpoR2sgfmWmSWep547fv2lmW73M2DXCIoTNmUY6a-uDWa3N102AXMOyynAtXtsRIjoWd1ncpclzp2DFCTXQPfkRPhx8AMRT4JyxW8ZNpmYBFvi64vvt1YDEBhDZBfHonrWDjyQ5mp_tSe5cQhgkcI7Oclsk3YkMUOJB2SgB9LrkeC_0SFd3KVXXArYD1fJvg2Am2zjETIkoSHvXRA9hQIE3UgHjtOGW8fWJ1tCTh2TlS2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ9vVu8EoXm-GXTXCptmzcGmHc9uCCkBIGqjAHiJ3sBHyvZyThnSjx8oKxnSV-hgGAH2WN0ksVW0PRTuSYgRcQQcTcT4WAmXAUYoD4WBRNIg2mVut9JCIwnc-c-Q8rphNXR-rQT-a02SUfHZS-ZMJYh5f9fKaCQSJ5H2Sa0S9c5G3JrzhmSNFgisKKfpBiXi27X_XbnXHKz3E-i8wxWYyrvJmQKK9kPsI2v9zyDEvslI1sci9GhGqiFi_11-2hLuU2Xitd8oEUc1s9rdhlPsol-pL5Ukx_YDKypaijG3mxwSUcvXPI47qPuVNL2sRXZaIvyfF-I8Hc6erxe_Jiu_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=W_rJYewke_RRQ8m2Gi07rgGm30Qc7CHVVIP1_1kw5Zrfi_ZzKwB0Ezhww_ZUwox-6pf_lfcdgxrA5c7HC-Bz2DePbXISARl3KxO4Ip3E6O7OBUOUWci5wzCBc2kBaEVL85NzIFIV5gHTKZ8JsBjZ8fA-qN2ZWdO9TS7pyqi-D3qRhTdwDW84JVdqzIa_vTBqNWBodABj_A5ULRT6h--qyhXJaekQ7WzaVr-a8XhtPV2Zcimc48yyoL-RCon9Z8X2rsNG52xXV0t_u6b864yqmOVZzm-5i8K9GLCddqh64quFxlBYsPb94RP7RT-gxfQMoCmTErcYtV0YlHbVsDTg0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=W_rJYewke_RRQ8m2Gi07rgGm30Qc7CHVVIP1_1kw5Zrfi_ZzKwB0Ezhww_ZUwox-6pf_lfcdgxrA5c7HC-Bz2DePbXISARl3KxO4Ip3E6O7OBUOUWci5wzCBc2kBaEVL85NzIFIV5gHTKZ8JsBjZ8fA-qN2ZWdO9TS7pyqi-D3qRhTdwDW84JVdqzIa_vTBqNWBodABj_A5ULRT6h--qyhXJaekQ7WzaVr-a8XhtPV2Zcimc48yyoL-RCon9Z8X2rsNG52xXV0t_u6b864yqmOVZzm-5i8K9GLCddqh64quFxlBYsPb94RP7RT-gxfQMoCmTErcYtV0YlHbVsDTg0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=v0WWt1U_w8izlAU84P8NRqHfAESVs6NoV7HwID9kMmWHEv-zc5NeWr7OuO4HVOSoWqn21mzpwECihsWnwZFTSZ-xyTw0hxPryss65AqVLWvPUozSWil-94xiJlBFwWOK486I9Ktmc9LIw1dcFFqbFaNdjNwHJQv5s59YpRy7G4RG-dXSa8LirQFd3tS7vjTvxooiNsyVatpvyD670ASAomRkwMPBwVdvfnsX9SOD_gGF1Lc4whoHwZXSx-Aq_zhs23OlT73ahkzC0lYL0FgOTbc4kMEPNa3ZAthwRxgpS1BNxcFyJcTuO3MVJzqOJwLkwXp6RzQZPb6KPo9C_f_TOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=v0WWt1U_w8izlAU84P8NRqHfAESVs6NoV7HwID9kMmWHEv-zc5NeWr7OuO4HVOSoWqn21mzpwECihsWnwZFTSZ-xyTw0hxPryss65AqVLWvPUozSWil-94xiJlBFwWOK486I9Ktmc9LIw1dcFFqbFaNdjNwHJQv5s59YpRy7G4RG-dXSa8LirQFd3tS7vjTvxooiNsyVatpvyD670ASAomRkwMPBwVdvfnsX9SOD_gGF1Lc4whoHwZXSx-Aq_zhs23OlT73ahkzC0lYL0FgOTbc4kMEPNa3ZAthwRxgpS1BNxcFyJcTuO3MVJzqOJwLkwXp6RzQZPb6KPo9C_f_TOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42rBsp0JGdN3eNIHIjf-4iCU0YjrLWXw8_Oh4zVW0U6mNxRU0uB2_ZjASmSA_gB9CPfaPJ15nMFe1Pqi6lG0robeF2cmCSMMYhcM2MIn0MuGNT6gY5oAMuTsxTlucBRJmcUuoh7oW4D6CcjCHd5X6caSRNk4skWGZVtlOfjKCRhfZqY41OEdSIKqESZvG8UAn8y4812_b17MlbuQSd_yLuHCd8Km2fJM7rDr6zL9Ql-ltk2MGEVBH16suyzn6U16bxaC-Obc_vTnBDb_R3lmy8XvkHnjfNGlDT0NmcXYrKudm2qFAYZojHEosXWDHaKa0ZGRTAk3uNJNc8am916NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C63g1KuXvvgGV83-iDi5n5V2P23NUgxW7tRFs_YCWTeWnLUFB2HItaIt0X5KB0z8-hB8h7a7QSTQ6XYAfgv21oCQLiA7wllc6iQBTsjPx7z8THaUxlubuTGQROfnxV6UzJ90rXblIEwps2bMv24RrtB4N3SqDSfYBWqGHpNjJMuWchn4DjfffvAl_MbhbhbKaot7WInvhJCWmLPbiL1zdfOsnfwLzzfYgFKpy2UPRiGKaymZ4Fz7w49WkDPbpMeLGgweO3WXc_kC657a0IxC1RsjsIwY1sK0w63K-0hDPcEuilOnfkkMc2mnt9e4ja0Nnk8ytCYiGJQslKuHNG_Wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsub6-Ev98OQHQ1hrgZZbFla4PqbUui-tKBUk7fSByeqph6VFGLeITeQpN-RdbiMCpZNNe_Wa6pg4e0k37Ho9DQ4XOgzNet5SgS3xtbbdEyiqPjFYnKCjB6wEi9COKWsZpZmaNYYfV6zk4N8sEbmAc8pB13VJT7344hcWjVUbfIinx7J_8VwJiHdac1n2sOPXuHDRUby-kZe_9AuPycFP-mZfcMan_HylNglruaN1w_jXk-1RxMbiOaLbasDhUUVvBNKLmovGBGHEFF_tAUdh5kfbHUwVUyj9Ut6FiaxnffDBWTij8DpD5AJh2CZvoAQ5AR1J8XduYHmbyrYP7o7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ao3XEIqoEe35wxzH6olf-SEff9Y83Vcol1-HmlR1DfGRjZYp6Dyed3nlMcqbl7ezzOM6KdB06kzxwSJsqD90PT72lH75k60UhEAt6ZpnjTOTwki_66EJA_z0hDECskDSLRXzqUjHaK5bDLt48xX8Bv8b7xCxzQoHKtfE5ejXADT48o81PnqdNlNqP5NHMli1XAozFVutV9OUWVvEAQ9xaWJHhz2C9CaNlphfjtbQLRyi0IPSD9x__HpPg4TjXOVtZmMzSAr7npERZbGUwMJ-fg8BN7NeHKeZptmL57oI1qPQEEbQdJ7892G42jhTFWQWWyjX4kXcA3QPOrnBmxe8zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqhZU6uHNZm2T1QY8glJbp5e2ury-RwlfvCdAebu4WroGSm_SW4FZs0HSiVdZ11fIrI4RxPN4byPr0V05_gcfIewDSN8CGAxGCN7PiLX6YTZk-SFVOvDy57wJnR2CNNfuQj9E_-2EUO_5e3FgM0KEDWlZfl3Lk8zrZpWU63vjf2NmphqwXUqzEOZFk1VaH9qtHeEpeoDaWZB0OMFlNXDiy0-qtV96dAOZafcgLJUKZWZFNKIKFlZV3cL69xwthWJq1e89pxSG3sOI3P9wF_lkEql4_pjc1tiUCg-EnCm0qO3THcJEa1J_H1Lbj47ixqvYg6ZfZWGgTJ3NpvejX4euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anbSbDZktwwjSk6fK6Tbjpk7ZvTr25LzIuUTsMbFZVKyB_ffy6CnRn9mSOLP408mzumr1Y7-CC22VkNpZBHPbE7UQarrA5nYHNFXBc8iJL5kkynZc_HH5VCD8sLXoOX-eoc7hT0pFXBiRCib7dLY48Z3HdyKO7AzwXwlwXp-sLjAry1dnRCoI9ZLnbHJ_BF7SpWNwEuUjQukizbnO5u5tV0tYbZ2778R2yridNBLzRycgKLuMzx5hVLU-NFPXQiL6TRgRTmx4lLNWgHhCE1Wjlu-IFIgZbnhwoTUtvSBbYz9M75kgqkFhELQ-MWR9mkq9I2yVGLb7ZXsx-39NDzd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJVz-uRXOIpJQpyPxL-v8zgiX3rhUnO8_2FNBgr11YMWQzxpxD7Kq0pMMWbJRbbwflFkgVTXtouOmfQNXhb1AS_rr8eXqXsmLbzYUJWNLokmDIT7lip_MtJPOdfcFqjfqMHd0J3DDDXeo2wYdI-T-4JjTcOzyyuyBCwoKcVpTpWfSwm4zh-l8nid4h2roTa0xzQxH6DqzszDylDgdm4UvY1-zZtGawpXATBQAUpJRSKWUz4Y61brynFr00jUhjEHfsb6rcJ71qjslsxifSUHYG9FQ1WYtzowIUjxpOIK5isBZi8PyPs4FAWzah8KYiXyJJJkSHFmLe_o1cfaUsba2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeHRhZ_TbzB9mfo3nATNy5WYIGpTVR_NagvLv9JoYYLPbpIoq95GKiHi5dm93KDlaDhTejBBW6lZUxhs2ANvZpnfAEwCwcyerHtWlFe9xKHAzU8Fp5OQbdfk-UCAK2vauCOCthWI1bt3dFQY6A3Wy4Gv3ShGtBvIow0MumTIVe34WIoWuSvfwkYHFnzAZ9wuZp0wM6wUFUXLsrVxusSALJoQ6rXgvZNF6aaJ7Ci0dPz8XSYbWk0Fxhwyz-YQ8ooearjphbr1euJFHlpP66o7ROgqr8hmVgjDPkKr8eukPy0d-KVvLAuNvMHhoYdEuw_uFLpiLAQ72DXSsl8HrIHLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUPl_xPmE4s3_gsTHzlprBPaDb46Hzf-90HrhnyA9Nb1NlW4biYe7bcjsH6n8xhkXP_PvNrvoydU_7mPabEXhQLObpRngJUvsOi7SRLRojj-koDUtA8qMigCjkp6MgX4MjPDFMVWGLP1RQTSOw5yBFmyz9Yri1pkvrYL-pgcs9gQ1y03Rp8om_9r1uJ-vYdc_QOaUhPRE7-pU2aLJcJmdzJYT2wzVZxLBbQ2mUtYiVSfSKWuLpdWDLRILLmE5BpARYOHsfqchSfjZm-jiBbtSvZ8dngpkHo1Q1SqjrdGCypLsw6IKz2mgvFESECZ2l4iTXTaaK-ibB1vN52UDRUU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrAnHaoutHVmpwJGDM0rq71j9A-m3tPPU9HzGk4D55FVGbpV5J8S_nHZ3i8Apq2QDb4lZkC5lsjF9MLSRGA_MBI7uT0BlPMORO_ApJXP01gYOLv73X8KX3_2ElQe-6Tksw9v0Q3HpXgdJbHwIDbyvNmpA6o3u2ZZ4whgM9NIBh3_BRlIOIzq6ApkMOGWXI0NpROFLBl_osqntVCbKgghUu3kYL3t2NtCKUVuZShhIPOBKJvPmsN2Q4Mbh4sadbDt4VgzLgUSH63XXjGGDNXcOXWGBG1_1r22qjsmgFLnvIGHJZ3_8HhwtyE7CwISFussRJVv7XnEFEdKiLLQIkJjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U04UyirZYpSNoUlzbEf6WZ4b6UEcGNPwhMPXyldOOHp1iAz2AqUJzt4A8_ZRGPk3sWxOrJddwHhsVcUaHPjH1xGYgdHXN9thU_JKbKfCT-QsWL1gTA-FAeUM6zs_BKTWU3WLBm_8XTzCvvSO7odWURqRchljUls4_f44LYSiwZm3WhhwD0Tp-ATXB0PB_Uc1-M6lVHy_m2fUbdLwond-bruKLscuBOly3F4r9ZDeJ1vk5IQALuZ6OBVI81kV7_IVJ6qEJ92trob_Tnbdwo5dGNljBng-R0jvV07hfxaJhrL-G3PkOJJxPQ4kHNlUPmQxgtS4wYmsG1IjCqg8pvpGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7X1YSIvNKkMq0pVRarmbwPBMsfLrq8t_eDCa6OfK3cnassKdE5e9rlRAxz2o2cLGdLHVftstXN97lYJdQ_d4fH-Gm51EJr7siwpzxoYSNeLaTjlEaYz_X743WBF-a2oMIlj5VYOBko3NhcQJcdOYp6sta1yMPiDJRklq03QG8ayCC06QTk8zNRgsOuKeW7s5teJZRTpR4_-gNX3547hcLcEGcKPrZS0w6e8E8XApjsb2eYQ7Pb18tab1jRRFR7pgtOrROHf1AGubutUaY6YrCRUE0c6HNm9Q2tIZC8WRUSVr4XVLPytcklJyZ7RJf9UTvRGV669H-iTnzcQ-b4I0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLLNuIuDQuHeA9_cNVA2TU2NzWe7jGhOH997aZta73702QU3nfycN7rlQW-OQIa-N73hI8VEibjrvZqTF-qzfCggJ3N4llda_oCU9fE0li7uoQnNpGXLTTHTyFEZU3QnBNe6oT-4-rCl6zVJ1E1dV48EtK7USY590T0upZabxWSPoqwEKT6jskrepc8TGjlrZIUw4ph3crVm_8rASDak8fHx9fx5UsMTWQ4etbSreph-R8xQ4kQVzDw5bXAFvrmIY7uelY42WHytL4uFIfbvyMF4Ei87_02PI4qfGeRz-1hYluXtyEx3FI1Ak9h6GRO5lYH4CGteDJA1lcShFVM2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic9v7ryG-wSYgI_BHdv7LznsCkMYOBQPnexzB7qk2KVcBZ6r5I554UGQyvYCb11NzafAMWlshMG-Popjg82qcI_pdk0ZrpvONVuhha94cZ8_sfcJ6-OSFa2rtz8mPCo8kXC2Ou_HYNHwOOP8Jn7jFXjV8HIPqdGSzKxEn_EaAxfCAaRoBLPwTKjGizUYh6ttkoizQeL12SL-u77UMlYKF4tR2dBz2rsBpfi1AD9aZ2qJKML-FnmaGsBph9ZpTKDDX8N3o6UYHqI1-0MAiWW8LE4SJ9HkVSg_ArdVTg2ytIJ85bLxZRS6oz9Lm4CWn_-Fs0ctYlyfQ3UmzBchziYPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvnP3TbPIKGfn55KonGhMOkYespjZj_0uirOO_oLMleKBB8jNJ3tp-Viah299LaOebIXs6Mwqnfv5s1ml9uVnlXT7u4bS2ntgAeyGKp4SilkQq8_w3lC77SJb0YZXvhWFuVgkFTu3uQPA6RRBl6wv7G0HqhSYtner5DVsE-5ecTrRD3sFBBK1R0pC0_VTj_qf25mkJ5o37t3CwRn2_bTONBWDo4TEcTc-iB4nra8xAeS4c-FUE-4IH0Ki-SoPmONb8w_3FyH1XTdlu23z8y3SU4BiGxI8d1NNBAy63gneBNyhDvVs6aUmiW58bYaviF8iB-biPhAWWFEzj5KKGfMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtDRFVBi9ijMOGpe82BCFVaihCi_UogxchFj78rB_b7oyyOlky65f7HKxt1jtQ-LWZ2V5EhrOtW3iOm5931juyUKvqksN_6GV_0IylZ5_BT09_93aL3hRPbv3DYTFbWd3YfEfq2UxpRY-Vuv025VxdShVUvV3gTNFIaxMuMMyULBb-wVkDxBU2P7rGzpBw4nx5nHDEsT_S-8TWKcm48LQBNDPsKkOvFV9I8LrcVJDqepnVBbuLMhuNdkv1myK2Xqtog7obXXWhWVCQh2RAo2CkVhqA4-G5mFkKIqdyK_RcWyvcZ8Qf7COCU7GRoy_nqdnTTuRWpkvdV3GtvxoF_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPzCPmochC8v_1bwATTt7uEcKU_WjHaUyV-HbDBlDupJxQgpvqtyB0ewqX8u59y6Az51Lp8_oxq0BtckTNcF3CGT7ZVDg574R0QuGTtvpL6rjYGizCnqRkf7Nc4MtEJ7pHA6G1AtBpBOhS-dRVsESk-_QI9YseSU1NhygwLe8VR0a7zfVGeDirtfyzSTe7FHva4mBSrDZv-rgpRt4DvkZ4TpcRRQv9mlOGBFRHpVRFi_F_HRFzt9YBrDBE32dJyuvvu1-mKj5v5iy-k31sOPek4myhxeLYCY2-azP1pvO0pNPKEh7ObzF6ZCyF0byidmDjLduMY78qjlDq0gZmEorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar4xpOZGhJYAuX-f1Gl3-a6AmFFJ73xTSrtu5ZFCE6st3mXDEEmvTkNe-urFvmgUKcmK0NH9SRCqTm1T_5U5oDg8_gCJIdtdmfuDwUqO44e7vd1OprBDZUVFmLPYoTcWjXg7gPqkIlollKo5dCus_q9yoUhZKA-V6-eEHQMbwBoR51j3xWGV9xYaBtefK5YlHAN0o0jDSvWuUPG4a1oI9LYN1VxLaTNXqG_e3R97LbTlDe9pqBh6PGaMKAJks-azs8NxIghTiZ4cAbBdgtdUNEAnz8PdaAXmlKH86V6l03XVlfFl4PuVB8zL8dwdoIHnsAKH5jATEOjaq9igsl1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPfjp7-6A_XgRzfgM0M7XTqlJXkjIJEpOcjiXKuWkL1AbyS7veYp8CAd4jNxBkaLA2_E1CnjCBBpt0M1-DLaZsomikBki9te1rdKmpLbREy2sP2Q_98tBAryC_qehQWi0Vqr8ILJuhxu4bfVyNjhpxfOS8KfAyskrGXSMd5IlLacfjKbzgb172qv-jOeHnSr-cAf46puyB2G1urRbTJmoIgsPSNWQGTAjyGaKr-V9c3QI14CL6LRJkeGHhXDEE0coGMsSD2VHiVU3N7AwSUfU8w2XhKEq0n3dj07cXidxs2dqdJQ7OYkWHmCHXkTaCl30fmymvSBweDItIkRqdhn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTy6wNAEaR9H9G1SdmqZtD_sIQAlC3uhWTwj-skRYyNrACktz2ckTwdrF1bG_S0w6iqxqSCIAvWtjg7Cema4czG2cNOI3DMHk-NjrLJU0y1oRrAxtF343oEPrF--QEls8shBp32yrgt9-1zWgZcGHMgt0imMZK3e-epIrDUfdu63DGyGYqmD4EOSlL0cWdwVLejYuRyo-gOxD4-Gv42Dg6-GApYrOdx0DHg4Ia28DdftCLSQiINPgpbNvVzSndauyiBTaepkimIRf2mGVxROeo9runVJWHPb0YRdPySB0Y13mqGoGr3N4Wb9_YhYDGmQXapyWwCLggPdPIZIhe8sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQ9Dl2SQsI39-KChvfrx5CPMexZpTEKVq0XmJ3mGZ05I9IsTfUGkZpTwocYdvUEdVpyOqiFr5ZttV29qsqbBeH-FQFoBkg1m1rERSxqtsCMzfiU0wPnrEt1tTM8vSec5zbEF9X1X037PsiV2pl7OzutpR2nfP6-BNyOPmUhWVm9WLcgoEcOd37wzdf-qLosHlyeR1vG-lPD5MlpeWw0AxYtS1Cu9uiAAu-XTjFMRBqImgnr7nq--1IJyJRJQg0QifchFxwYRgQFOdQ07zHPnUk4ssJsg4K8BHIN1E594wkrQ3rrCaC4pSKDXUnBzPKzn3IPANf4JU715hUTa2Z1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8NiN9iYUa1derQ9tHgxPVCQVEozTv8Jcd3pZ_Dr4Yr1EI41p2WKsLkUSfYD8kpz_xWnkSg_jV6d6E94BnWrS4_82OjFilDeyHLAxrOGBEbef8WDcrWFmVDRiM36pvozBkLf7VpalphfT8VhBoYX1FAb8M29l4_HWAYhhhcz5sh33BnGWUAZT9nmFoOFvWf5p8l4KGgyWEvBYkfvd-gQ4-wSJ2B1c58pIx-g5ySuJezZRrjt65Ix-b2d_goysxFaRDsHJ1fb9lglbQ8r29m-dmwfLfBMKPzZecQ95_o3o5XYAiMGENxuoULZr829pBcmD4kwtTBOOFWnudyXTmTebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnTPB_wMzPuJ_MQdvdGa7EpHH7CN5tOwWTDZ1gmCt5p6oz3zmuikoMKHOG-ev3fv4tUK8LXjHgyihxMXO0BlT2th5o80KTX86tWAXkC-wK3Ya3PipFxfabZFtL8sAaB2AdxIMYTIlOGlgCcw-xIeDJ7JtlsWwhjs4dBTW_N_W0sEs8WgaOE7m05KX0VNKrt_uaxVt_pa9pHJe_hsjYflSt-Xb0w58lzGz63mJRGkiox4kR0KlB7UM6w0QG_38rPYlGpqCkLhWui-Hr4veJGcPvkUKiayKhELyVn4I7puzjWHsJytoyFxFcu18KVOJyfhrml6ZKFRwhhKHDEn24Rgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQFcOffPsxRsyKQ-UHhkczAFCjpMM_UyPI5cf5wl7fM-_QLUA_JNeq5TkI1y5qK26RW01Zxi67uta2T95gP3-4n16K0Qw4jyu3RxV1tI39_ePWlghqgUjgbgYafCiaor10wM3FO0u0UwefIqT8a5ROA239xlwtMmmFZ53ULPeQRroevzp6tHnYN3pGGh533ye_XmY8plZeuX8-CjQclHLcB9Cld2fpbsMxFL2EUmk4VuXw3bN1PNs_1zncRIz-B96P0A2bU0CaNFrsK-Nj2awEq2HTofPnhp5zUkdXYpzXnAsY_bN73f8dgIkuQVPBZU_mHDBxg41xBxAZM90uPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q999psRSudkRJR1kdMvRcHNd23DfV3RCXX0eABKxOB4hVVeDfzkyThb8lGlVt-1P1_lVPuqyYCGgEj87Zb6JlRk3qWx-1kVcENR5KcffegOH9MW-jjKlyq9IBTrIlHdCD6_T80XmqLOFEfG6l4rsWqeFuWW5LJWhYKPQVuxS1uy606NG84udkCV2e4I5CI70SHOakF4pmHGLkEa9mweLyVUEw-7Om-yFiVvTtZt29P3nXbmNv1tqEsbZI7z5R2d8wsWimetRUYgeJaiSAVfW2JG_HOsQWuFYUpFiq0HJCtSisRX6N2guA4Fijcfb0ojfUMEFZQzN3GULUZ7l51nllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cONLrJiBnuaIUThq8HvYnW4ZPuCnf3TPQLYxDy9xXD9GeCqa3Qx5SbBWyZZuF9NTUQZomrWvJvRY4pj-3a7-hAyrEIH9WHH2rtImhhcWHyuXUUPWB9GhbOSVrs_5AKOLG1QYAaeNAfGUFcpm4JLyY5--UZO2kwRzWG2jdJ_Ct3I1nfwH2XDwOywkosYKtBOpvU181BKfQ6Gpy6ojGG9o6iS2Juf1-CBgwDRmFTsP3ck4qJUQAl9XLfiBNgj1zmu78vNRRrxlZkpAkbhm2C1iSUUdp9aHYG9B9oMaRNHJFNwIxPXBYRicG1U2H-8sLU-1D4jN8_OxrkOCbLT9AijMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GynqylbjLCswealFRq6ejbS1tKbsHpmt272OBtobUIlQ6qnAcIEabKO-bFaMQMt558QEgTIAcxl9UpzMCmgko-PpwDexJsGS1m4GMsNrxrtZvVtyFzQeK2m3d3a2yWEAxMRsEkn-b7vFw3oCNBFBjf06LEzOVvA0ZNVZtGMc44zevik2MZvxRXHn4my33Oy_RMPRysnxkqEBj1N4u7c61lX4RWBZaJjiHasypHvNoGOTOaxMOD409bQCgQcUyDrtqppy5Gvxve-tGL9I2KUWVZxVLHif6clbq6Ky8jdTK-0AHB13gr1SFuOoPz_PbPjWi8X8e7_Iyuu05OW7ek3ing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxnEhP3RiJBFfaNOuOYUVZMboWJHMiMrzm2efoSZ_Ho_4581Co8YNmRzC1YgFcX4b-hHH3pKuBWp9-iHlr93t4WahHRfKzqI7eJ8pZC3EUIfY5IZpIIRz5HUg49wDAXCqXPUpUOix45Q-iMJnrFaQKiNhtolI4-v_U3agu33MoUrcU_Yy0bqZr-erpBBedBcS7xVqWYdLPFPl-dZTX8nrf6rQv1rJw1THXCjUQQVlSTrvsNn2UqgmqTR-db8YHJ7SlXQ41U1fhwnchv5jp3gWjn6fecDJlaNP-mXQ4uihkIRYtxp8MlhoEvqKQ3ouHhPElF9bvm8R0d0d0xHzZ55NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=LNnmUgGif0nEq7RRPee5DOCf35A4zEF57rpeLs9H9cRJYPBOIQoJyUWmnIEgsNP3ci9uRl3HMZSGfj37AlA1KiMzpJ4Od1nAq-ezjRBTsTNW_HPF61csPKD3wjkJGBrukBTck3KAv03TvW3yGED3OGyjPRY90RU-1_AnXuzxJrDXJllXa-FOKUBqpjaVdck0SjD_2MllxoGjSIEhBV1NkjNhlkgw92HPVLq0TEYYl28b8RnBgDjGYb7_02y-keppvIq4HVaQjqN77DhlNAJu_fWKhDnstk7SWKo0-vUlO9t6iTyFJbwcLW0hbrzxSa9YkIn8cnU2jz_epo7a5C3Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=LNnmUgGif0nEq7RRPee5DOCf35A4zEF57rpeLs9H9cRJYPBOIQoJyUWmnIEgsNP3ci9uRl3HMZSGfj37AlA1KiMzpJ4Od1nAq-ezjRBTsTNW_HPF61csPKD3wjkJGBrukBTck3KAv03TvW3yGED3OGyjPRY90RU-1_AnXuzxJrDXJllXa-FOKUBqpjaVdck0SjD_2MllxoGjSIEhBV1NkjNhlkgw92HPVLq0TEYYl28b8RnBgDjGYb7_02y-keppvIq4HVaQjqN77DhlNAJu_fWKhDnstk7SWKo0-vUlO9t6iTyFJbwcLW0hbrzxSa9YkIn8cnU2jz_epo7a5C3Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYkj6ApdFuioBalNCfLX2bxSwIOh7V2EwxhuZiKklVgTKt4yNGCl59tOXnH2eE0eVfAxCEBbcnkd9EeUABYzNaRCqc1jLUlAgO_M4p921oWt60-l1-Rj2FdtWZsgm66CH3mUOOgeElWHQ-hIuec-qSalxya7rfRhVumJRmCXDdPFXRRxwx4JlRlWu4KeY9XclRUhtq-_iiWM0j8zpCAsZbFEdLUeE4wpKxFr724Md9TgRZTUlMyDChwsBFV-oKibbPogZZLgmmlMyD3iRIVS99SUXIntrenlBlm1kEjcOJpRCCvaWNqdtoJpB48m1SFrYTSCpC9Fr4XCU8-0KS1EMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=sEu8CVsYnyHsBYV_BqhCluw_7B3Kp6BrfwTcNOvxx_Wnmtu8Pb-sIXc5QYpZMWpVHZuWfvgecVK6_r3MWdPvd9BL8jJfOCIzbsdgLhqouU_7uBydKBOLpFu8fYJj1FHjj6ELb8SmC9TDaBgI0R-AsFZXLPiNq2H0AC5D5O-g32y45axD0Wa4beYRR7tUUlDKTnr2ikztZTw4IHuBq3-iyoaDhu4STdyXE2ucNQhnhDV-aDTnEOVO7wI7Sq-_VhLl3d0HYjatnRvf73xsUeIXYQbjfNT-o3YVc5biQSFlaYMas2xqgLpUiow8-RzFXrIQl1SMe1osBcQEh3tquCdfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=sEu8CVsYnyHsBYV_BqhCluw_7B3Kp6BrfwTcNOvxx_Wnmtu8Pb-sIXc5QYpZMWpVHZuWfvgecVK6_r3MWdPvd9BL8jJfOCIzbsdgLhqouU_7uBydKBOLpFu8fYJj1FHjj6ELb8SmC9TDaBgI0R-AsFZXLPiNq2H0AC5D5O-g32y45axD0Wa4beYRR7tUUlDKTnr2ikztZTw4IHuBq3-iyoaDhu4STdyXE2ucNQhnhDV-aDTnEOVO7wI7Sq-_VhLl3d0HYjatnRvf73xsUeIXYQbjfNT-o3YVc5biQSFlaYMas2xqgLpUiow8-RzFXrIQl1SMe1osBcQEh3tquCdfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilnZEVd0-XdjuI31olFJ7_WdhYxMxfsJbLKi1r2eGxqollD5vLYDsyHUFj5-AfrhnXIMw9RXziAKEpA3EihOFb1wfKyaL__OGwZ8QZsIUQAHZvwjp4LdAWos2NKjOWyoYV-0oPFkzBc9qJTaeZQM-e0gr2JS2H9epuKmhnQmidK1EHklSqfA_Xr8OcGO9ppzBfibIv0We-XbnZK0gB5wjZDQrgX9JSAb1Pmi9-I4tx1W18Qs6ojlhOxqQfSeZFPOWqYyPDESDreYa0FCtYThOOyBbwLAIjvmFHyDpxK5fBi1XH0D61b8bwRffyAeAeQUwXFTa35Pk4xq5dzIdBHdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8E5_5YgEuhJzxV5iWlMSJCePczSq0jenREZFopqKrxxo9xZWlr5sZFf7JpyjPBnfpMycTT0idNgLFs2oUd8h800aiH8-rF0JuCEDHC45EQt8IPY09TGLpD5twu7jFKBsZy55ywmbsjBZK_z46byiceceNHgMB4hb6cbc3ZuPguJHCCt5aa9wto_IrGj4eYgAUttd6yjxlJLuYGVXObVlBfxWpPkGzo-ZhPd25uotOvLWI767lTNO8Uf7H7na-uMIwWoiuHmM2lJyD2_q70xwijX-2AN8geFwX1pv1nOvK202k88PnebWIa7-9ZhxhOWhwmkIUSOHyebrTRa9zqMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbyBmiIH0wnPxFRgh_xq8ar6rLV3dSZVq2oJeR1J32Ml5IIWcs_rIuCvqGwPSTUnEII--IN_vn22EEtZEW0vmsWseZyoMjoAa6-30xo5SLrBZU-lFvK6_aMl4ppzxuvKh8XD5hyGOhym-lawVkN2EqmiHBM0ts1DcVWVHiVFBeF1aPs1HohZDgg467ARgIS7yjFQY_r6kmM8SGgB1wsZ14yyUkkAHbU6WfnJ34Nxozw_NRlCl_XhvR6BToYiXPFXZeKZelfZ8zMwvd8WHw8CzplM703HSCBZ5rXbmdBS5ddWFzoZ6t3d70U3uR2Fv5wNZYqxsq1ekmoW_Xjxsz2FHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djzukc-u5eBQ_kkMEwmOpqYEJ-nuw5g1BpwreKmi7y9pz3oEVDTU-znyAD4sksneWk9BfA00oFiYX2Id6WraFLLd7nw6Ad25AuCQP3TgYsVDd9fwNrD7y7tsNBkpR_kc9HVoU3kO-dKzDWdTxfpNAkHl_i7UYzqOj-NNQ4H7Nn2O8iE50BigqeRzQR-e5PY45gycnFBW4CJOTMBjtMExFNSyyT0eNFXHwUDxOazwalNR0BIzvgLB0XVasQ7akl3dTyN1Zxf1NiFXdBZpUi7WpO6lITp0dPkDip5ZfZO2MO6ygry6Z4we7NYnpRorb3bsvUaMfuFX8Xml7ySZP6W9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=jQYOjfl68Ruameqf5-Okmt6z5pFhLhFclWTFLHd7YzYYL8j9xm-GfY1C1YWIDncV0_umPI88tFf88GJ_QXSP0vDrWHN6_YwE_-CbW-AcKc9uXcuBiTwaHAM3WM1F97qTzGwVMvq4MK8MQrMAHOpF2RV4acLOYsheduAimy1Z6Y2SyxUYq8Aln_kr5lj1OVqKvHo6tk5HqrBIZJnppRSDv0DrflVx61pl9eOP9_rVFNrLdtJdO4L-bscvdrQhPmUmKk6kj7exmmLE4FUzYBstsd1-tD6q1IcXtlC4lAtAGrMdOFQm_ctPFwsHg8RH01yGxaTIbZeWMIGz97e8QNe2Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=jQYOjfl68Ruameqf5-Okmt6z5pFhLhFclWTFLHd7YzYYL8j9xm-GfY1C1YWIDncV0_umPI88tFf88GJ_QXSP0vDrWHN6_YwE_-CbW-AcKc9uXcuBiTwaHAM3WM1F97qTzGwVMvq4MK8MQrMAHOpF2RV4acLOYsheduAimy1Z6Y2SyxUYq8Aln_kr5lj1OVqKvHo6tk5HqrBIZJnppRSDv0DrflVx61pl9eOP9_rVFNrLdtJdO4L-bscvdrQhPmUmKk6kj7exmmLE4FUzYBstsd1-tD6q1IcXtlC4lAtAGrMdOFQm_ctPFwsHg8RH01yGxaTIbZeWMIGz97e8QNe2Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpV92z4q5GvX9C2IWF3qZ4WAp7HCfojdF4PD1Hm8t3lLnrId35a-pkkTRxF7BIQbdclOBgXs-H2bFZQ3lO4zXm7BilqV-l7vXUNsZQilJU0-_REkPZbQKs1VN6GEUAsqXRQNGk-3b5xju4m-5CF0IOu7L0xHyGozZ-EIq7-2S6JZ6phAkqo6XcAcqLQsdj3RTEJsmZtSwwDzwO7ylAC88yEKpSSiqetFzET4MutcSksSN56X8SRvo8BPNmEz8AlR4pke9yDcnd_0u8Hq7NUa8dduh9L6heS1Hqiu-_ZNp3ASA91HsJjYJfiDmT662KEA7PdPt8P6t-16BgHBTs1lNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSWm1rLWdrfy8c5jUeFzGFr5M3EeuWypXJi0RgVMN4BqMmjnMPNFlctBs-Sa8EpZNKT4gdkYFW4LcMHtsxUmjDnEhXoJTQ4a4gHdvDOrjbDyiV8y6KWNogdN26bn8STCGkLXIH_G1W8ujaRDVI7WpGAF8yk7C3ZIwfh1URUOy6-WbdS36mTrmT6Y4T2Z8DwqXHZn_-IEPRXeDIh64ew6Sxkk6xO_r6aUqjrOcF7gycNgXrga5xpyZFrukCXUKc2zRKsSc_2RevEH3SK-RR_i3lhnxRBBo0nKrLtVRFgv4QA9AI9PCfksJR9nrU1FP1WDOBGHXyIyIPK3t6DtWVRlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHO-OzR54Fb7xdaRvSnX4G0fIM97lA_d1umkWCLQSdEpU3Xh2q-QzDSTsHpE_p13zTWncbYcRapjpQ6tqS5-2za3HP7N40ZbpgRHpTtFmjKeLu29ij6OOJGjTkNxX9imEJpwlFk5NEuJ7-sW_jMVShkiY21EaAduQxj_tDsSfn59cFct-1IgIp_RUmExWdM3M_XPSSaWau6dWDHpixWyjddOVJQHyTLMCMZSWgrkTizb-h_UHJk825SsLmf7_fy--fdQMF1Hn2avlwuUvjm77aZ1QvoccFUIHxJNtzVYzBS75KnZyR2jDb_vwE_hF-7Tijpec9_jWiVlpYllOcW0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jck2xkdbOK3FptEKU36hNyMyaCRRHUzIx6coMPh3HRhgqpp9DhU4XyW1IFFBHOHsgePFitm1o3DVqIqjMR4YN4Z3n-kkqzKAj2wj9DcWwmI6p0Yl-jRdPbqrNBp-KcozSYXuizobBJRfsQ3dcpCOXzESteizjiDMhncDJ3Xrad3elmuTeSwbLfiplJ-XrMRbrqU0ZVULBj4HiteyW8yFtr1mBZvFuPEMqXvQjXzYeUdhAXdYhdap8q7hOWYZFjLHDQYDbFwX8AkVMlyVOhd0f-PUP24Rri8bUQa3lL4Go1lgTB9lqTrmE4yxMm_JoBLgQG8OcO94NQzwEvh6Wzo9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjb2KFnAOs9BL4vx9SKekezBdkH5k7d2PNf_JI5JC2YotmAKUILDpXxFa-KPt4vPC7MgL4Xu5DVl1_6TGv8pOPVSExIi6POMXpaj3_Mnh-g1_2Ezc9LptTnDmeL35dzmX1qkGXhjG34_YKbpyKM66_4x-nYmBU69MYEuFk1xAXsItAp-8bURNIVCe7ORPjxBygCa_aVQJsjGp1svZN-eDZe51mpKmICZVucSxe9L2v1_DLeATGuO7F9urShYJBjpXNEwLx71RapWNKI6Kty-84fWrLUUG86AyJbpLat-VAJnnpbxMU4-L5K8qWng5umpO1Gq2Xq8vbzjqCzw6omHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTNogG7xJmlc8_U5jbFal5ocs6M_IuvigrZBK2Y5a0fKTPLo3f1lZS8-ETgcwzHPsa0P9z4zXtahDHK6Xy9tV2rAgwR8SUHqHW8Mm88ZacD-H86Im2ggILJFKvZImlcRDXepNUSWxUcdZB5JrouTJIwLdaoUS8XNEPGwuGGWUkujBVj4Y-3lieZE-LqmYy8LSgXH6L317j6roILCABGr181GVKb1oWGvAjIzFYslpYyx0jDWdZ2QcFdkFSRVq0-kU_i0LE-d64oy8HSDCKZEfzLR60HEZhKa3kMPkuuspbkYeUQESvcY0WfuWJFmvHr3DIIyHgRA4lKXpLDvgaFwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRa097kii85fcUl_wZPD6zj5tAV-mRtRyyWMRNhdH-K7npkrWmSAtHIElrGSAjvx0KRrN2LxLx4yj6EFfvaWo8b07PsDguHqaRFd8ZvuiAeecUsRbiFUoX5dKyy9-qOD7snw51z082qN9puAqZlVCCHkQ54e2VTV_4U-sEfXr7T_wjCckKSBJ_qOCBALby9fDdATalRXcUOaGJ5z552smnU_M2OqsBdjxe3UTAQWsBIimFMk--PQx6zerv4rxkv-UpJNbbjEhvmFBUQzSOE-tdakSW_PE-o5XKCVDQ9KXSTTGbTxe6zyZq631WHdGj9TTEJv28PUYhLURAgf-uwbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcWggRxGo_7ltwkbgtxo7dRlhgXnI4mOrbQEeh3Qj3Yqk3KnvCwrGK_m-XxSphedCNyrdBL3DTbvRu5dNSj-WU_zdsBl8CC1FUJlm4YllwquSYT44nzvcArsTlK50mZLfZKgk9Qz9P74lTxEdgKEyg3slSJO83g5_aYgPHSh8si5Q_nCUJNkGucq2-fedLWvqnGhjDIMgTdpNBUzJmuEJ0bd8VTt_TcWCVVewyyN5_tTKhg80VG1f-V0JGKmWtSWkQyYxZ7wxP_0Mj5HN3wQtWD1xJBA70nnT6Rt_hJaORgIut9Z8eEkJv1XJ0-LCy2AXfqCRgUL4LDj23dyW4xmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwTpHA8wk8IMnshp97lS5M_WjLQtDsFlVNT9nj_j5XgwHRg-5txPrbenJuPFOFjgH0my_rpimOb5hL-1EAX4bsHAoaTB4OKrAPlKUkaLoe-BaD0gj0AlClJo8-s38bAeuQjW_R8RSCI0383xPtMUCu6I-6mErHdH8Ulh1IvdMsmVqbXZMuRjaq_BIJq66DCCpT3ssCgVB3e5e_7avUKsQrch9s467AV0Xoxr12Ey3c_FQz7IwEduD-Hm18l217NDf6CV2JRG6nDBALcWfbszKeeQl0w2_-QATo8VlCmh0RHLni4IqmZImPKcar0nqrF2XTA88pjZ-NYptcm5VkSER1bc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwTpHA8wk8IMnshp97lS5M_WjLQtDsFlVNT9nj_j5XgwHRg-5txPrbenJuPFOFjgH0my_rpimOb5hL-1EAX4bsHAoaTB4OKrAPlKUkaLoe-BaD0gj0AlClJo8-s38bAeuQjW_R8RSCI0383xPtMUCu6I-6mErHdH8Ulh1IvdMsmVqbXZMuRjaq_BIJq66DCCpT3ssCgVB3e5e_7avUKsQrch9s467AV0Xoxr12Ey3c_FQz7IwEduD-Hm18l217NDf6CV2JRG6nDBALcWfbszKeeQl0w2_-QATo8VlCmh0RHLni4IqmZImPKcar0nqrF2XTA88pjZ-NYptcm5VkSER1bc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2kuM0XMqyT1cdNhkd_gTk3QImlZI7ShyoEIolp-pp4PKfN4AxJowt-5hp_BB0TQQUv2lQU-IbqS9FaLqn6XbAGG_XE-BobWfRiZSPGGWKPdUtCUVWIEARlN2FykULT3hPgiHUBZ0CbQhW2kAk1ww1DgWY_WPlhhDcJomAtI4kUcAjzB0xTyaQ7-Ae3nEAJhaYSgGBhU6LZTHD0mStTvxrNPVNul1vRUQZ4-VWAMdfsC5jlIh1rYhjxBdPwUiSaru9BUt-QGqjylr3Sye2jn9rhSrG_UOND6RuaOY1tWdid6Xvsr11auHhwgKObnbHL0HmXpl9Uxk3SJGxXUSdI0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTKkuLCdOcRC2Sf6dWEpu5bnzwx1byWNoG5o2AfZ8Krr_CiTmSOLTh-x-gdO0OvFZ1BQUlgebFSgfF3m5fPvu8BIvIjs7EYiEzMUa3Q2JTw9B-d7-N-zLalb-2DmuAV6x-rx5tLXFw_S0WJDGCxwW1R0_HTCDHEPnBChr4VLfX1ZFhotvS8u72uNHt1vMAeKXN5u2HUkGsFwe8J-Vc2ov4jbLgB1FCDibzEv0mwKIHaGdciaGs3Vy-LnO6Pq4DdVi-N8smFnCsOmmGJATEcsVDxFAE7DLB2VnzynIKqac_QhoKMIr3-AhxUSPdj-f9TRYHrHNmUz3Fcu95IXEB-bJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=TM9grBmT7qfXTvlMKKFcNCD3iN_6iR_IhWCU7bHgstcTMuAWSiYxHGkXpJpcBUCjg1mWvjREx7-KeprzlqFqF-YQPQbNskbVj6oi7fBbeEHdznvVNrPU4-yCrHIdowkOciI89vF6ulOJwzLuSskkRQ7_GIx4ChjCjMc_bC6xRfkMC7x3yQQr9aZO30TOMDIciwPsuts9VrVNqLoN8Rd0tOuucl1bI7fyDKJEKvVouuyS2zYnmJPD7hbyz51v4Z9lBNy7Ro5chcNATTGuMGbRYmA-DMURGDSuSzaqrZPBE86TAejVFzhHvK3z18HTI_2SMtLDrYdebTGkAJKKt2lyNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=TM9grBmT7qfXTvlMKKFcNCD3iN_6iR_IhWCU7bHgstcTMuAWSiYxHGkXpJpcBUCjg1mWvjREx7-KeprzlqFqF-YQPQbNskbVj6oi7fBbeEHdznvVNrPU4-yCrHIdowkOciI89vF6ulOJwzLuSskkRQ7_GIx4ChjCjMc_bC6xRfkMC7x3yQQr9aZO30TOMDIciwPsuts9VrVNqLoN8Rd0tOuucl1bI7fyDKJEKvVouuyS2zYnmJPD7hbyz51v4Z9lBNy7Ro5chcNATTGuMGbRYmA-DMURGDSuSzaqrZPBE86TAejVFzhHvK3z18HTI_2SMtLDrYdebTGkAJKKt2lyNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_2JU31E7rfCDwVJUXr3PJGoVY0GSYrUiDHCKPDLdW6F6Bp6_eyMZ9AadiIckxrfcwB1zqj3ZHJUyTRlGmMq7wJuKKohJlSRunSeazeNsSSJAjRXo2ghubEiJFBob2P5LRd-K-KteuvGDJZTjg8t1qkuaW3we0TIkd_lguw0c5lSaGMH3_4RP2-KVLic9HLoD3eZf9LPtgMNlp60fHaBQdUnWeS5QoBZ3pT0ukjoa0B2bHdNwoy_7M9I--qew8a96czVelzAPQs6Rfkybe7DmYqB435ZaC3EoLdilHckUt3yiISKUDubfRPLR2cbLEcZa3-KgZ13W1njdriDwSdHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUJvM1-LPP-qp6T4cLCpcuJEM3GArKRglYmqbrvQdjxhVxP9_pkKyakQChvBI8gprCSoKBEQVe_lu5zIKwQlwmTLspmRR8IXtmuH1aSoTogCAUFlvyU6FpRkrnXRFAx1oAnRFS75kHBFJcOiZsaWGfpuY16sxFJyxWDW0qdepb4RXqv9a-G_MOyB-XBDldG6jNQbCUMendXrWQOxp1KCiGwAuFz_cxE20nq_hra5dKHaHnlMfB7SYAhkldMJYqBASghCj7QjIrh2gPo0Tvn6L-31SeFLMluwl1tmfPOcTlQZLrYn06tnqxGHVaLzIVim4cTJ7_q7oMhV376Mr6jTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Anp8RKS6on4FHz-8DkSH81YQFg_DATY378sRVat7Q_L_HrJ3MO943s0ZAjjnSzz60vqR_3QJPHw82AFZtfEFUo4bH8R54KfmMGdeXJu2jdOWu_nBkzVWa63jiq0RCy0X_mh28j4dDDhdCkLCeCc9oSmeajz1t7rwawGZsfDUapSVVmt-O888BH3PUIsf_VtcD3UlLWVYPC5-ZOORDQc7CSNsb_9RLS68buh91NAfBNwU4PzryCLT9bv7Sxy7B1Bk9bSbSFdVqZF8zyHZwqBadQC0D9vcOJspEfzpJBsQCMemr1R0tBnWL8_cpE9488rewYKNT7FRohQ1bMfysRCjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Anp8RKS6on4FHz-8DkSH81YQFg_DATY378sRVat7Q_L_HrJ3MO943s0ZAjjnSzz60vqR_3QJPHw82AFZtfEFUo4bH8R54KfmMGdeXJu2jdOWu_nBkzVWa63jiq0RCy0X_mh28j4dDDhdCkLCeCc9oSmeajz1t7rwawGZsfDUapSVVmt-O888BH3PUIsf_VtcD3UlLWVYPC5-ZOORDQc7CSNsb_9RLS68buh91NAfBNwU4PzryCLT9bv7Sxy7B1Bk9bSbSFdVqZF8zyHZwqBadQC0D9vcOJspEfzpJBsQCMemr1R0tBnWL8_cpE9488rewYKNT7FRohQ1bMfysRCjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENFKOI1KoaTd8DklCbsf3k7SJmnt7fy0_wxWz6oTcsg6H4-4_jPAjiEKwSVgnS5vtOd07G8ezCgsPUik8ndgCIU6PYOzPIEAUjjtSj3mBHsPZtua2Qtd4okksBc58UdbnqORofuS6-OhOUSClp3wmGex3vujH6X_ASMPrP0nP7iIZG3l0LxKMFFu8KT2a7s26EHdyRclpQ-_0o146OFV3A2aFLBAt9IpjmrctBzDGi245BwTu9joFc8_Q11lWDjDChPQuF93bwD9G2F-kTpC33YfX0_rs9OcdJ96klG4Ep4qbfh_F6Y2BLmTI19-VHF6xmOEcA-6zYiwBNDVrqtq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=dKRZw5DL8ALlv5WStRgZFR6M3X5GMP0w1MfDMrll4a2SqPO67WirN1rdcRJuW-89kPV6Wq4OUfmX5MOm1dItb3aIYjWJrbH1GAAkWB6cw3zbsL0nzJWNX06iNXl1BfAvSQGdyxWp6avptk9ZSb6XMWn7DpZ0-Aiu4CEwB8F1s7gxM91msZhHBdXbQa8zIX2wwQXvR4Zu3g_zq8bJksPXdF64-f_Kjz8GeMkaTW0v2DYs-ltQ2dV4RsqjWG4zNkb2TiGKyO4HR3dLgc23sHHi1ZZEPd9eyK8FV5Ghxh1gYCl7LaOCrUHN1UBma0wuri5GouQBOZEs14-oiPa4JlSRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=dKRZw5DL8ALlv5WStRgZFR6M3X5GMP0w1MfDMrll4a2SqPO67WirN1rdcRJuW-89kPV6Wq4OUfmX5MOm1dItb3aIYjWJrbH1GAAkWB6cw3zbsL0nzJWNX06iNXl1BfAvSQGdyxWp6avptk9ZSb6XMWn7DpZ0-Aiu4CEwB8F1s7gxM91msZhHBdXbQa8zIX2wwQXvR4Zu3g_zq8bJksPXdF64-f_Kjz8GeMkaTW0v2DYs-ltQ2dV4RsqjWG4zNkb2TiGKyO4HR3dLgc23sHHi1ZZEPd9eyK8FV5Ghxh1gYCl7LaOCrUHN1UBma0wuri5GouQBOZEs14-oiPa4JlSRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeuHQtVYr7O0MVqtHKQ6LizUStr9DZMz5fNiLy-ONccJj6lvc0rluIH49FMvSp7hP2F4kbuZ-e_UKXlQDYd-vtychzwz9KMW4wwJgYYyhBcNSM7b2yjC88TG44zQwJtro5uZuheccPPN3Sgv9X1Hf-oK7Z6OXrJWzxpccoFv9KGPUCfoHUAO2c6kxBrjj2ZEYNZ8e4Q1WHZSIzFZvPji_PyQHjG9sLFwwUHyBS34ddh2V7K1p2nq87D5TWRpuqFegcUVh8V3R6KDjd5cTG6Z3K-oKID6XNWK9UeailuOl67G0BvWNwvadr5zNM3My4uvtzI96-0q8__YV0nAysvn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwK75UtNbbNnO2dvIybfn9TNPc_jDXixXekEd1lQ8hBv07pqCX7N6mbzBkoEMAKFT2onfc6aW9I3NBk8Y6Rb_V8YS4FRB2p47bm6TFOKrNFFf7cGE4HFTu81DvYlig8Zcpsk74GttpggxqtnOYHP0kHSoc8pYl8hfPTrZ491y0PnQgNtMtsks0obJZxpDYkM_prS_d7Wda-bz-KQ48PXVbWJ1awex1d5TTNuYhtKyR7O3hWrRVcfu9U3aN6Om3749g28czNbU7Vu9sW9tNDIe8AxC1dJuPOMi9fIRcZCKCvF74CSLllujzi7JNVxO4eR2XbUwzzG4eUsZGJ77EMcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=jCxW72eDi2KyH-MtH9UOCh1nw8BSRAbqxl1YewyL9SBDQZLulO5uMlRsM61eamtXEI6jgZve_GpQ3g-xtSxHjJeySda6QxfWF3lOd3MO03c27Q56tXcvWmZLsBafZIMHCtywcmjg-xQm8Bi7caOxGokG40EYZLYr1bxbur-pEgZsdPMUelrMJFhMNgSCxmI9VmR2FgNToWyNiMMJcySx2rAOSCeOPkW6OBx7vU9Qhou7j6JVXcTw_TMwXbDPSPXgfUSmlaugh556N9YEy9ce-D27Yii1AZIIBSt2DeI3bWuygwLQwsnwOrGkz7wtQATMoZPZDAH_2R5xYum_LX4m7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=jCxW72eDi2KyH-MtH9UOCh1nw8BSRAbqxl1YewyL9SBDQZLulO5uMlRsM61eamtXEI6jgZve_GpQ3g-xtSxHjJeySda6QxfWF3lOd3MO03c27Q56tXcvWmZLsBafZIMHCtywcmjg-xQm8Bi7caOxGokG40EYZLYr1bxbur-pEgZsdPMUelrMJFhMNgSCxmI9VmR2FgNToWyNiMMJcySx2rAOSCeOPkW6OBx7vU9Qhou7j6JVXcTw_TMwXbDPSPXgfUSmlaugh556N9YEy9ce-D27Yii1AZIIBSt2DeI3bWuygwLQwsnwOrGkz7wtQATMoZPZDAH_2R5xYum_LX4m7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=GyOWwwecpJuribyoiEMIgD-M8t2JvSioeuj2vUsFczcEgOMTkwemZVk-1REo-JDXcB_Fr2aFQESiGM4kz2jPK1_hX50VHMgPzI-9x_yLALIAVCZ8cArfP4B9OgMNR5AmLuipRtEYk_vyMOG2u-d6yCJwPdYjS3ukKQ4UBc54HYtBRcKJoctrTriTMNS5nVi6SQ1_4uesPO6waM00Xj7hkS9g9OCuEMZ7MOp7BKI573kW1KJnLKWbDYeN4hkQgr5R72f4zYo4RxP-gSpanQWDJ0YDPRSzdOcR6Eyp5gXYyCDcNzGiuahOXtY4UOsqKhSHNOzSEV6j25bOaIODL5KC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=GyOWwwecpJuribyoiEMIgD-M8t2JvSioeuj2vUsFczcEgOMTkwemZVk-1REo-JDXcB_Fr2aFQESiGM4kz2jPK1_hX50VHMgPzI-9x_yLALIAVCZ8cArfP4B9OgMNR5AmLuipRtEYk_vyMOG2u-d6yCJwPdYjS3ukKQ4UBc54HYtBRcKJoctrTriTMNS5nVi6SQ1_4uesPO6waM00Xj7hkS9g9OCuEMZ7MOp7BKI573kW1KJnLKWbDYeN4hkQgr5R72f4zYo4RxP-gSpanQWDJ0YDPRSzdOcR6Eyp5gXYyCDcNzGiuahOXtY4UOsqKhSHNOzSEV6j25bOaIODL5KC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8vfm1yCwY0Sosepw4TtlW1wljYFl7Pr6nBVbDjezlbMq3fKIafa_KuD2DRYbgOY6bEvjXQueLCfANe6p9BJkBojdAOWA646DLGmBaYUKXHKCxC1w5jS84TZa2Q2o5LRABFQNbAj0__04Lx4XAg0OywCEtGN2GlIclGHCWSWKAfBLEf216ksoWEB9BUCG_hZ_LYdbbY2DrULsIaBIkknLf2KDnKhEuhZobrvD0ycQOgXiFuD9T4AySXaPf6-hMg3fXfKzmKNwUCe6b3JhoxNWF5VCyXjg9qXC1DpkiTJTM3gMWTY4xwYCRE8MNg-kPKQAvID1wzBlIyd_5xK02kX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOiEG1yT8Iig3KOkWqhFQ0mZYCetvu2vQf11nDGBvUageJ2ngwg3GPoB9TmpJKKlDprYI2hWNIVecssgLl44KU-V9k_UtHrE68JhXt0kCO114RMf80OIfsir6BC40VlfVwZD82BPoNlZImFPudrWH9FgnH0Ip_q2N93IJPOG_MH3ZXt1yKKU7600aaEMMGMIwtzndneYxlZdo_BqzYP6Dz3gvFWOYlYmSf0LcbBahiKl5AiMxDAm_A0W09vga8Kp9rlqQ_R7M1MtEZMjgg1rNiuNU1DLHNr6mXwEQuFlAAkELnElO6r6RT4KdRYtVW_yVFGyS32bGATNJpvl81aLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOJ6WDV4LZEVYhOPPYIfl7FA4GmIAXfp28vk9yQCm7DRdNuxYBrAGfpZsALyNWP2eNCqzejLv6o6Hzd-yh0O0mhYPoOBx4UfNkbrsdxK5CuNChDDjshdFP0XMhCZijfbifXNVFIjXw7jMj1TKxnW67VPcZGkIb-n4-Ie2bUQkeQLjsFvAEN8pRgM8LHLWsu8XuvqoWyiJuGinxhYK6vigAfYE-1r2ZFLl4OWOdEVqbP-MJNF_dD4GID_uOXmhAREIR_1RN2QqW-QOThp7AkY-EtS0zBQtgFC7WCRMGN1SRvBxBqnKIlhO220E3qn6zR_n4ecDmK7H99z1cJZOpWqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=giHoVTa81AZxmpF6M-dI2bYDfjqevatEIuOgx8NeZA0uf97OW7rfjmipQ8QZmeExIuAqKhatAsCBIDioP7IWWSMNYf6Pd1NpnW2ZptAGPAMSSsIShLGDvsIzrvPU8sN1mP4cwqHEJ7l-le5ZXVtOJtA3l5lGyv4RK9BSPPrm3ZH3v5THfI95O0R5E0j5ThTVb0FHUl6V3jshhSHalNRiIZ6pN7KDI5EQxU_TkCVz3dusRAHCoGSzUlb27AtWn5Ud4SjvDvPS3GbvPlpurNhjzzP29ajhCHv1bI0t6Tw-ERTyph1PtALgJE8FwkWVXnzuea3sLYhdLzrN3PR7Z4uxXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=giHoVTa81AZxmpF6M-dI2bYDfjqevatEIuOgx8NeZA0uf97OW7rfjmipQ8QZmeExIuAqKhatAsCBIDioP7IWWSMNYf6Pd1NpnW2ZptAGPAMSSsIShLGDvsIzrvPU8sN1mP4cwqHEJ7l-le5ZXVtOJtA3l5lGyv4RK9BSPPrm3ZH3v5THfI95O0R5E0j5ThTVb0FHUl6V3jshhSHalNRiIZ6pN7KDI5EQxU_TkCVz3dusRAHCoGSzUlb27AtWn5Ud4SjvDvPS3GbvPlpurNhjzzP29ajhCHv1bI0t6Tw-ERTyph1PtALgJE8FwkWVXnzuea3sLYhdLzrN3PR7Z4uxXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJhHMHJME8GqUsc-hpr2g41Am8_ROVOtqBTCh533MQcIKkaf6D99t3nhOeaIX-28wpjdLcJmuInQPx30BHXgrUZT6W8V6Bq2kjXknJCqy56UBjGpiLBKUR9YWxhKqcrzbzu2awXsEXEmW6VkPDyuIQez9tw6mGtPnisXrrIwe2_maJTdZvO4vbey7uWKjTmmQd5Yl0CGAUlmeE9SzRvHU5V5l0NK-KgKYSoiMNy6CD5_rm6OvUjOGmN1opmnFUR5iFwth2u13VEFs-2Qgw3UfVjqWZV-4fh1lSyXw017Z5XpK9QtWVYxx0376QhW-ehnyCJbXY16CHZarOhRxJainA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=Dz7_DEK-T9xbzTQvMu31bA-cLxtQ_4j_QoVBMhs0DeMq9Yb_Vc_FsCCBZCl0xc-MBDBmKQlWY5Z62FHaIDoLsuZj3Z3kqPdoxUixHQBPj8Hw9I3ohZTP5tg3on3wqbBWQGywGCKPwTdBOudSIncOoXKry8ywNZsufo3TYzHs6I7-GELqhsLuOHkBK-mBq5ya-k-8PtdRx68a-G0_fw7ZWGhAHbrPQfNbMWzQWcbSx_PTGYEJCkwa0KET1zZ9YmMXHEftIlS70Sk2k94vWFKlIEN6vVYe_bZMAQ0TZQGHfKHNWpuB6Np6i8cZc0seiwvYKDvRy2Vr6AcMHzXIshqhBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=Dz7_DEK-T9xbzTQvMu31bA-cLxtQ_4j_QoVBMhs0DeMq9Yb_Vc_FsCCBZCl0xc-MBDBmKQlWY5Z62FHaIDoLsuZj3Z3kqPdoxUixHQBPj8Hw9I3ohZTP5tg3on3wqbBWQGywGCKPwTdBOudSIncOoXKry8ywNZsufo3TYzHs6I7-GELqhsLuOHkBK-mBq5ya-k-8PtdRx68a-G0_fw7ZWGhAHbrPQfNbMWzQWcbSx_PTGYEJCkwa0KET1zZ9YmMXHEftIlS70Sk2k94vWFKlIEN6vVYe_bZMAQ0TZQGHfKHNWpuB6Np6i8cZc0seiwvYKDvRy2Vr6AcMHzXIshqhBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbxeolOwNjfSwaeNPayGMXUiIJmuMoIomyqZw8PMKboq6eeFkYfHMW4Kbid_jxUKFWOsN9udJPlzw4_z5si60ns1lcKeMafCNbzZnTTNgqjBCIKmfyv4SJbHk6eFB-_rMCoX0-tk2MaxCojpGiGJm1CnU4p9QEbUvSQnDjiANXu0rjojSwm63LMW-MgP-bQ5PRWMEdmltsWZYkuYAsoWjxBnbg_4kkvLX_Re6PvX87uLSqMqNF0NXcg7kbJlnYji6ClWPKQkffgcbve_veJqrVHAL7zeQlDAnSWe41XlR8DL6jRXWVKpPO9NOq0MncNrd1pVeu2QzzuyVviXHpR4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=e1ZBYlXNHyOOYmiUjsjGEL7LqJL_fE0u9KWuEhVz9JKa0IVpZL8OyJz-r9i26Fsuj-LV9UyFxfG5d8yfA-nYgAiOJsSMTzi7ggZBBrJT8Uld7I02NGlkOcj3SyWI4KLS_aVuG-F_YhnSQEYZdqfs69DKyr_82ireEMRbEpyeP1LHL54fS8ogPTtXEtYHJoYxVw1QrgkZn252h2qZbBfLp8rj3OtQeiIfIG6otjI-mYYAKTKmJdIpaD_6Ra-8XBQPkMbSW0Jb4BJ3Lj41mQ4lCxgWctG6cLIhPsSzgwP9wM4FZEXn_2YqhvjUyy6avGiVoqxNBjVsbkJlIwcl5wF9ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=e1ZBYlXNHyOOYmiUjsjGEL7LqJL_fE0u9KWuEhVz9JKa0IVpZL8OyJz-r9i26Fsuj-LV9UyFxfG5d8yfA-nYgAiOJsSMTzi7ggZBBrJT8Uld7I02NGlkOcj3SyWI4KLS_aVuG-F_YhnSQEYZdqfs69DKyr_82ireEMRbEpyeP1LHL54fS8ogPTtXEtYHJoYxVw1QrgkZn252h2qZbBfLp8rj3OtQeiIfIG6otjI-mYYAKTKmJdIpaD_6Ra-8XBQPkMbSW0Jb4BJ3Lj41mQ4lCxgWctG6cLIhPsSzgwP9wM4FZEXn_2YqhvjUyy6avGiVoqxNBjVsbkJlIwcl5wF9ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTHaf5zFAxjCUG6Tho3sBljOaK93mZpz3h1iFsc1jnOkTR9vAoqq2O-6HIJIwwv5YoiKp5nfCYMXOmpS9jg9s7f3AVY6NF2gpOAauvdP4-3o4-XrBLNCPN5ZSh96NpqSsDdVyytX9kxkokWoJsdTUgUTXxiagFReR5Ft9Hl5VqlrJRk6JROARjNcqXApiIooIhmCQ3o-ydZjrlbVDZdY13DUpWk4IfgbIPkQDlo_relR5OFv6nI-K4TzN6WqnFsyKZxUp1pyH8_vsDxGyC7lJiSa0_0qlMcUME-Sq7x8WoHr67OnZeJ_4XIq1EI4T0_tBDwibhN8S99gC6kC40JpcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sfkzs58COOEBkeEpKY0Bfz3jLXIswyomOJ2kRkUGtTMBpuoJeAHp2xw4j8UkL2VIuFTCQeK47XCMkoZQ3qQcceBh5oH5YF-2REl7dW0t456lKNXKfq9pMDzN99AdQhQV6wAXcsb0naon77HQbgwBnkgvBpa7G6JA8Gk2K5DNePc0yoRD_UxiVwym38n72z5UPeKhEr2dyzseSMZQEfTqcFpZRnDQ8Ng-V50vFj8pV-OYZ4deI8OSABySIYTg_KfcWQjNsDtwhSaDjZDUhINJdQZZ0Ma_O9fpwMHnuUrMMnNfqM2Sq6lfJtpwug0ZlSD9cQD4wua51dQuKUiOeuWemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsEjwJ6zVwug3GSsF1hkp0qwmiO479X4YOM6t-yzI3LcCfgzzROyiYBM50djtdRpmtpp6g2_C3g1S3hY0QL8fN7vXB3AANHHt69-C7XAQBTVBGVpDbEFWeFhpvD3En091o03WtKaoCZGUozXH6lDyKA5IvW98_ZLlWh1RWjKf6SSk6uS0pDZueyrvwyFy9SXVcqcvJnibsbteYwZcoMMEg4UyeJwh9tTa9i9UNv5stBVpPI78VyIKUAX9N7oxpG3wzhvSTUB2DwHQ_yIf5wSzR4A0FdO1ho9ydV7XdCt2LZGKsyJ5UwjM48A-ViQiZgwySW6OexvFw9ePavurCRDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3E-Tu_J0bB7Qemz1EEEnT5O8Q-k75LRbaRQvrOwYo48VcSjGT06UmsU8nyItL-Fw3gqdWxzmawkC4_0zHDgP2KkQBuMcVKf_60WpTlN8tnkBC_AgUT5rS7BcHMu855HlVjt5QeLR6hy33kprVCbMR4D-U2-FEXvs3E3-IJMT2VC6j1nW43ImuS9eupX_Q1da59hOKlSr6ifq7gjGSEpcBEsm2tRRuZKo3BGWrydaWI_4oCNXCVBGZcex6fs16lP4Vd7npXdJvaTdRULTMYLtw6N49E8DsxsYYUNuXDn4ZSzw6fhc-Lh1V5Qwxe1WaWNlogcADYBoOUsnEx-5XO_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnnaRNRHpKbfLcy5dbF9g1-GhgJSWdOuJ5ZQAqNNeq4UiQg3BvTTs-ioUQqPlVHiSwnkmEOc4ghvBdic3vWOrz6X4pRV0qARJEBfULqY1Hcq37aCvcsxTTRwP5DCjcAcYxbF2lutASj02gzkv9iFaini1yRw4wZlbjg3CWS8QkJcqLjoNDpCyrCrnkBVOQgPmJWNoFEkDnzqjf8eCWf6DVWjso7KNbRjTOzrjRgLkpWOV-XuN3Ebg4u1-NPlDdDxUnVq0guUU2edlcpaouXI9w56Oc8GuchvziUXYdmLDnCMUHFDbENWqBAfEsaQbb_8rl0ABzqq6rOYSjdwoxSeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=FBvD3IW8lkDDdItAF-xdHktZ_m0_szfRBFI7T7NdTc-LGfraA8dLEHsnWD2Q5QcL7VOnqfvT0GfsC4O3YSWgUxvupyMZYxGMdtuuDuW3H52rDXPnjWAQ-hGvh4-O6CXlVwa0KOjMevXBPtsJ259qVNT-8BT72z2SRg5d54zBGBlhERc9ThHe0BJLNJCbrIX_1olgPbWqKhK0gMM6JpyBvdUJ2JCqaQbI4Wi9vSYggFRt7tPp87RzkDNXLkfllPNc6Oh_VOAz0xTWVFhTmL5lsY-ama7vf2SEEb5DKrMJB9F8XNZX9pU_QOUN-7vRS8zhYsvzyiwt1Wb8SEs-fHyPMU4Y7Sdo86r_1IRgyZwEW3ULrINcrOTmyh70CmYN__P7AI6_PPZ_NxuCmhQbgCEdQGNB0LjZoPk3-pdu4-lcg3vIlYwApU4jqqNcoD027-iukxKqcjfAdY4TR6oyzJYSpkHjBzCOBJycdxxl1icYLX-NrZqK6TvrF5UplcTiRAHB_cvZSEpzjoEBkDEzdr053szNRmLh7DH4yzih_I1PcGpGMJlYT8mxcMSITrpCsEq0NfJFCnuDmBbF-pKy1N2NfYm3qbQNfhckqwcryVxzKpZjy1PNiOV9LivTesG8QxT-r6Zz2uFfVHLwBRiQvFduoGEHHZ7QZwVFxUVui0G-n9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=FBvD3IW8lkDDdItAF-xdHktZ_m0_szfRBFI7T7NdTc-LGfraA8dLEHsnWD2Q5QcL7VOnqfvT0GfsC4O3YSWgUxvupyMZYxGMdtuuDuW3H52rDXPnjWAQ-hGvh4-O6CXlVwa0KOjMevXBPtsJ259qVNT-8BT72z2SRg5d54zBGBlhERc9ThHe0BJLNJCbrIX_1olgPbWqKhK0gMM6JpyBvdUJ2JCqaQbI4Wi9vSYggFRt7tPp87RzkDNXLkfllPNc6Oh_VOAz0xTWVFhTmL5lsY-ama7vf2SEEb5DKrMJB9F8XNZX9pU_QOUN-7vRS8zhYsvzyiwt1Wb8SEs-fHyPMU4Y7Sdo86r_1IRgyZwEW3ULrINcrOTmyh70CmYN__P7AI6_PPZ_NxuCmhQbgCEdQGNB0LjZoPk3-pdu4-lcg3vIlYwApU4jqqNcoD027-iukxKqcjfAdY4TR6oyzJYSpkHjBzCOBJycdxxl1icYLX-NrZqK6TvrF5UplcTiRAHB_cvZSEpzjoEBkDEzdr053szNRmLh7DH4yzih_I1PcGpGMJlYT8mxcMSITrpCsEq0NfJFCnuDmBbF-pKy1N2NfYm3qbQNfhckqwcryVxzKpZjy1PNiOV9LivTesG8QxT-r6Zz2uFfVHLwBRiQvFduoGEHHZ7QZwVFxUVui0G-n9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=XAcrM3xUPLWm37g2M2bk1D5rimTYwvufudtzWF9d6GVSYmGWoajnCPl1p8odbL07xeHIRaP3455iYzcDnc1OZZ4jYTKxdGXgHDabxj3c7RFyJXI39w0eIVu7KT_GHWtmL5lvpp6TlTxVd_Emi9TwDFXP3IvvZOYN6H5fzHKu3sdSVHEqn_mpbpcqnF8UWY77IT5u4T4cddWr-6_uRLqL4ck6E3KT0hflpx4GQJea5BsJNiGySvdE7WPsY25C_pBvRgTKKHsNkKR3eFQIiplUjQjrRqtb9rh6YLUn4-tboZnrywFVoYSzLH6F4zntmYqR8ZNAoRkD041q1pRz7p8hLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=XAcrM3xUPLWm37g2M2bk1D5rimTYwvufudtzWF9d6GVSYmGWoajnCPl1p8odbL07xeHIRaP3455iYzcDnc1OZZ4jYTKxdGXgHDabxj3c7RFyJXI39w0eIVu7KT_GHWtmL5lvpp6TlTxVd_Emi9TwDFXP3IvvZOYN6H5fzHKu3sdSVHEqn_mpbpcqnF8UWY77IT5u4T4cddWr-6_uRLqL4ck6E3KT0hflpx4GQJea5BsJNiGySvdE7WPsY25C_pBvRgTKKHsNkKR3eFQIiplUjQjrRqtb9rh6YLUn4-tboZnrywFVoYSzLH6F4zntmYqR8ZNAoRkD041q1pRz7p8hLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWakXA8DRciRq8Kmo4TDSnJ5y6p-rYkk2ZY_Dr4R4rmc5TuAKTlI7RVeVTH0icLnjveSYnrWmLjakRWe7ZR3qy8flp1KB3BLfI1BTOoPgwAAXWneSqFQ8XVvWuYkp7lBlCH5IJ48fzV-FlusVx_xS7wYmriFzyzcXUnroBcG_zW4WG46ap1wcRYg9w84XsGzkPZWNdbOqEEVM95rFC8xX_zuv_-dEjyll4bnNHsEJDN2rJGVYDKJ-lbsn2Hb_pu0t-GsH-qs45qe4va-JDwTL3Lym1NPCIAj0xgX9jzCeu-nbqCFh-8Mlc9H8-fm__-iUJEro3bfc-KcVbeuzl5fkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=n8HPsxHrU_LVtdgV50EAelNu2wKImEp6std64uE9etWoQusamIPtYy01Gp9_gbIFUJFRK7A7GH-7ZXGnDCPnx4D_vappEAx5RJt6GgpaOueHy8vsjzXRWTnMbKKWKonocZ2ctIcsnMWg2ZoIH3DJiwuMI6bq9oa1-Gs-vxsjnCECujkV85PiKHkick_w6-AKrFm9WtgNs3Uiz7UeNl4Rz4YlR5gngcs7Utx0V03kW-9o_bZN84IZoNi2o_yMMZ8r_Sg8--XUoVTGHSKYYwWb2k8p19_UoFyXG-jM8CNnMb1BVSYhfI-yaghdg9nbuUmXF8WLAQw1ZEsYd8ghjFPVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=n8HPsxHrU_LVtdgV50EAelNu2wKImEp6std64uE9etWoQusamIPtYy01Gp9_gbIFUJFRK7A7GH-7ZXGnDCPnx4D_vappEAx5RJt6GgpaOueHy8vsjzXRWTnMbKKWKonocZ2ctIcsnMWg2ZoIH3DJiwuMI6bq9oa1-Gs-vxsjnCECujkV85PiKHkick_w6-AKrFm9WtgNs3Uiz7UeNl4Rz4YlR5gngcs7Utx0V03kW-9o_bZN84IZoNi2o_yMMZ8r_Sg8--XUoVTGHSKYYwWb2k8p19_UoFyXG-jM8CNnMb1BVSYhfI-yaghdg9nbuUmXF8WLAQw1ZEsYd8ghjFPVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=sxDu56e_6iAHbUxM9XwIjDhEffKOpO5gfTCD7Slj3-2BwDxy4DVz5G8ZqrIKefBUguD1Tzzxz4ocDrcjKXksG1GSmsTlf71Zf6E8CZFuh0x98yiGh71zcvtt7uV2BJi6PzDTUHbxufwXLXfMXGyuhAxBGag6hqU1GBrsDG8c2me_Ir_wVvOlbovArZHLlqY2yKIeefoguhGCHG1EkFOz3WRIH6VtYegwVkP7miZZjdz1iQafJIrZ27RziMQOnAjumpy57D7ihXJZPd2Yy4A-qyk_qyoc1jIHsf4qa8f6n5BZqQ9Npq_-FHU5Rt7AIjqd6glJSAn09WbwwyjUs3CV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=sxDu56e_6iAHbUxM9XwIjDhEffKOpO5gfTCD7Slj3-2BwDxy4DVz5G8ZqrIKefBUguD1Tzzxz4ocDrcjKXksG1GSmsTlf71Zf6E8CZFuh0x98yiGh71zcvtt7uV2BJi6PzDTUHbxufwXLXfMXGyuhAxBGag6hqU1GBrsDG8c2me_Ir_wVvOlbovArZHLlqY2yKIeefoguhGCHG1EkFOz3WRIH6VtYegwVkP7miZZjdz1iQafJIrZ27RziMQOnAjumpy57D7ihXJZPd2Yy4A-qyk_qyoc1jIHsf4qa8f6n5BZqQ9Npq_-FHU5Rt7AIjqd6glJSAn09WbwwyjUs3CV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbdn6iOKrGiMPQ9riuzAUGsxB4slm_qlRhuYfnryHv29nguWqf4M9OioZHVokh0sE4isTdLXGk7poRqRKtY7WMdM3WEMQTvdL2zytz6TV-0aF2OLq4ZKleXodI_DHaWx43NpHl5Ym_4ty5Han3sskWj_YUHnV77-Lr_UcBeS87BjrAcfmIyMUN-smkC9Vy3m5E9w8EbQ8U0QrSNYXFPSTWi0BRoWyOwi0DuuKTL_A88K0kfVAzN-FwIfZtVZlm9-1NRHmoT8q_zsQ3nVS3QIHIfdvZ4PzM7lPVzgAykBpB0lqr1sD0zw7hcSrqA524CQ2II3dJTnPmghOjcVwDkkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6OAnl2U06ZKrpv8-vqQL80EvLld82PEy7303wCHFSC8R7xtrOy9Oj2MUWHCdifYsuLkyUglxfH92O9Ow8PyegA7WVlw9YASG1n4Pm5q9z4uBC2Qkuv2xro0d4FH8yIG3VtVTmBV-JYl9r6mjY3FeQzOl5R0083v0HbSJFFLK5Ccwl2m-j4OIYSavuB4hSjxej6HKSQgRUPHPB_EsoO0UQrKRmTbW5fXUUQyP4fGrBJ0GFcGzC3xSrqgF5wLZ-t8hBDJa6MZ_P3sjxDQaEIsUYX_J9kH7hCeg59gruKfCX3tRA3reBlnt1B-TO1bFXce_PwKH50RlM1F6ofcR5bx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
