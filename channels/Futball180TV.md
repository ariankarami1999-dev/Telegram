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
<img src="https://cdn5.telesco.pe/file/muwyYlAKgTHgX7doJwtD_7EUe3ubadYsESr8WNOq6D0pgSupA5uSj2IVfTxFgZTk4V8UYG83Zol6jnvvtVEdzcJkncc_GlfI1Uxfg8agMlCHsQWKhiORi-q5hNi3lKGs0ZvXaQ0ujnAfXwVQhtaoGsn3CA-CFhlMdNGR9EE7sx6Wg-59OtlE1XnbmpiG0tAYvbYh5Qu7P0m0C5MJptieXs1Zq8u-WZeYn-0vKbpayg2cyueTTHz-f328pyFOKG3V2ls-4tJFHKbrarybaDAER9rflqnUYQAvj6ah_2IR8iB8PhlGs61kLnQEEQkQQx75geQhwscsFz_HxfF2LI_STQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 465K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 01:12:25</div>
<hr>

<div class="tg-post" id="msg-103847">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOFn2WPwigCK-2RydSWAFYzdAt_-x1UQx4qoSxJkXhyvu1p3aCWR_8Qj-XS2-1tmYDrFTYSbBkn-5m1siLop6i14UMm53ti_C4nZVAJbdzxO_3Y887mfRimBKO8rC9W33fftwjW_D6FBTBLH3RMRY3DTB014ScKlH2Gha4YSPRHsAgyDdcb-yjfX_sSGbv1iT3vUHF_P89Sulu__1LGcfU3Fdql6Nsf4AbUY9Fmmkjk3dedRKIX0A23BvpmntavW-ESAuPVdSfkizw3XFkn-Qo0TCraHx5NXoJ5ZaXp_FQTVCbuPSKb0DaD0b_0fq20mRcWNCac25CxxB81UFqZrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
از رسانه‌های نزدیک به الهلال: اوسیمن هدف جدی شاگردان اینزاگی قرار گرفته و الهلال تمام تلاششو برای جذب این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/103847" target="_blank">📅 01:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fbd749fe.mp4?token=gJjKoAo9rE7lcu6SzmsjEl8XnynTR3_5JeUX1BeMAWpwz20xHgyqa9XWBe1UA2Nx9qHT7I7L9TSVCRHathIyxHB9zWKE8F2eKTu72io23mWrY3AfQ7jzjrJgt9_jzOOLRUd9vkQ1u_UjJNNW0AxP2Dok5-SGv5uck8INk0U7WHvWuKsdoeaj7KUx8zTwc962xy2LpoMRpJ_ikhdQkC08lfaF_kkBUb8d2awf287M6eXsOmKTxPirIbMDfkeJL1PaP4HFvNe0agauI6X4nHst2razKRVynzaxIF2Bz4OAWJUTBq-amNxvfvxbRjF0r_gIHLIvbxuWMJwuW1K7yltPMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fbd749fe.mp4?token=gJjKoAo9rE7lcu6SzmsjEl8XnynTR3_5JeUX1BeMAWpwz20xHgyqa9XWBe1UA2Nx9qHT7I7L9TSVCRHathIyxHB9zWKE8F2eKTu72io23mWrY3AfQ7jzjrJgt9_jzOOLRUd9vkQ1u_UjJNNW0AxP2Dok5-SGv5uck8INk0U7WHvWuKsdoeaj7KUx8zTwc962xy2LpoMRpJ_ikhdQkC08lfaF_kkBUb8d2awf287M6eXsOmKTxPirIbMDfkeJL1PaP4HFvNe0agauI6X4nHst2razKRVynzaxIF2Bz4OAWJUTBq-amNxvfvxbRjF0r_gIHLIvbxuWMJwuW1K7yltPMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚔️
درگیری حامد لک با داور در جریان مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/103846" target="_blank">📅 01:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsLdwq6-aWllEVbidetNdl6-WMILohUiQVtaRTI5WjemSP8EQXYb_9cjdg0khjH2dEVMZyF02KwvsHLaTSyqpgqTMmExOCDdD7Zb8oMCOHiFCFrzKq1Dj_jDu0ofKSQuZ6MfuV_6u4l4FNMJlqWxlW9YGxbBsuq66sAAb1T-pGkpHVMDKQtwHFiachsc5F73bHPmfyVrWg_oBW88JxiTOdqZe5eNFMFfqpWrY-w-2Y39Q2mx0hLfJb-7MlPltmcu8lxTDP9zLgJ6WbSBWyvJDGVUuMhar-G4j6vdY3BwN-C4Gcldugjyxh6HQLvbCd62Pte2nBsIrllop9vpV_J88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
توئیت ترامپ در لحظات پایانی مدت‌زمان ۶۰ روزه آتش‌بس: پیروز خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/103845" target="_blank">📅 00:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSiY8ioirgzZ0dRbwQCv2agwjzp2jCiYYlxN628xQWRtAa17Lf34QUuIhUD736G-3LwGgPE1gNjBJrq0tICpbWGkNfr27BQ6YsGABL81Rc8Y6toFxYslS5gr85XyucfqbejQf8xgWVRXu_lpzsDoIoeRUVhyNinKWu0f9Msekk6F6EnVOIf7S_XfYcMG3SMJ_dBCwKgXDAodCVumrq4wsWBNyeUpVniSlP4QGV4xSOSbZfryEOMfPgaodT_jo60cY4T3gUoSw1NX_bCTMCglJeObliUORW14IgNtQKSwSXaKrrRYTfG00YlhdNA8FbrG_nV05BKxct30Bb1r0cxXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جرارد رومرو:
✅
مبلغ انتقال رودری حدود ۷۰ تا ۷۵ میلیون یورو خواهد بود. در حال حاضر قرار است مراسم معارفه او روز چهارشنبه برگزار شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/103844" target="_blank">📅 00:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7Cop3ytZpL30pkcbBmcf7Sdz2q8Rr_zsIqubvIPG6W9awj2fkJUkfDeB4-q1e4KgMMHqqX7Hozf3kZ3u-Noo3dc0G_sr_C73MKPH7ZzfYvgyUxVOZNFqJLO5Abs_JU71W6pFf90G_jvvU_bc38Jp5fcGvy03EqNbZAtocDiSdL9_ZaTpwwm9sL4vKPNr3ANIj8k--sTCK1IDAW0kbfsxG4PE0dmoD93JhC7AWKPNsAA-IvZFUAl_XHMDwqEdSX_TngGylCaYSDWaDbfiPt0AD6XKERA9TtmcukD5w8WhxgG674N-xXPHxHqsWxFZrXvzgrnlaEIKgL0sjiOFQDC_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🎙
پیمان حدادی: اعلام قهرمان برای فصل گذشته منطقی نیست/ می‌توانند تورنمنت 5 جانبه بگذارند که ما هم شرکت کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/103843" target="_blank">📅 00:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2opvGePKLeINu2kn93_VdOlSockQ1jJbiw1aAxLHQTkEIrbrs6Epy7Q3I94IIdes96XYhKvVDxCW_xxx2q6Boagl5MMPIwgr1VsSfJp0MJw1AksLoG5tv-Kw9Vu6ySkcpqxDVVaI7wIPCROOByHkYkjVI1G-BcsYTFal2qLaqhh5itOntFdAsP4tA0WI0kjfGsze2Z23SDwCsapaXzTKSRtPOxAzZrploF91VzQvdHWPNQ-AEu-LONz8eHe8HktyY-qrPUid0BRZd_4vHqe9uebQqAvf8uZjwNZUxhxyPFDVIY-pL_2JO9W3knBszUSCHowpndFMBN91ihbvSDWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوووووری
از لونگاری؛ مالکوم برزیلی از الهلال عربستان به الدرعیه این کشور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/103842" target="_blank">📅 00:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG3eUZaEQxcQ9DfLtbyz0RHO2y2Xdhk-TDtPEjmXbUYSu-qn_UzsECA5C1cRJjk28SYzXBNzIpiCT-C_r0uPb1ylGQtyJgbYLL8Ibff1CyFVjtdmoGwmiF38oZFNL7eoQUuF5UKzhQZueEYn5Sjv4TqHBVCOT_B3xJOXU7m7ur7b1HDGjfewrd1Zwo7ShpETFchufaHZV0xyvTSJSAdYItTP95c_3bFFsjpVHRNtiN68124YxRTnM2EzWLEgMtAkXSTFCoSFRWFyypa4Y3c43PQTV-LdgjpKtJ1ZaAm7WHAdX6EJ7C1_1KA0FFIGcxr4JxF_AN5Vt9eyz524e4xlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🔵
#فوووووری
؛ باشگاه الهلال به صورت توافقی با ژائو کانسلو فسخ قرارداد میکنه تا این بازیکن رایگان راهی بارسلونا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/103841" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/103840" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ulqI7dLzItu2f9sdVIzxg26o-nEAvW45Zq2qota0P6wXe-bZ7m76Ia4LR2w43WIcHihCbMZI57NXmOvkj-3f5nCIfHB-x9dsUsdU4HkHNQS13jJpBpw-5krdFgVeHvb-jMzrPKrsf7Gdx6co5enkbNAc8k9HKf4Sg8nYNxhB-RRSEBmCZPqMrxWiphSOQ4iH34WPYRh3QITG6z6dun1fm34UVLinm0NQEqfAzHjC19vlaq8JEBolF_gRJNPl7m6rCMXUrHMUWjDjw51VWLBW1OxnQl3FV8gvrOgeVj7Z3Y1EqstOM1dFssE4nuxfGqX61Vpo3xgbTvFmltpceToFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ulqI7dLzItu2f9sdVIzxg26o-nEAvW45Zq2qota0P6wXe-bZ7m76Ia4LR2w43WIcHihCbMZI57NXmOvkj-3f5nCIfHB-x9dsUsdU4HkHNQS13jJpBpw-5krdFgVeHvb-jMzrPKrsf7Gdx6co5enkbNAc8k9HKf4Sg8nYNxhB-RRSEBmCZPqMrxWiphSOQ4iH34WPYRh3QITG6z6dun1fm34UVLinm0NQEqfAzHjC19vlaq8JEBolF_gRJNPl7m6rCMXUrHMUWjDjw51VWLBW1OxnQl3FV8gvrOgeVj7Z3Y1EqstOM1dFssE4nuxfGqX61Vpo3xgbTvFmltpceToFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a24
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/103839" target="_blank">📅 00:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
⚠️
امیر علی‌اکبری در مقابل علیخان واخایف از روسیه ناک اوت شد. واخایف با این پیروزی، کمربند قهرمانی سنگین وزن در سازمان روسی ACA را حفظ کرد.
❌
هنگام ورود علی‌اکبری به قفس، ریمیکس «ای لشکر صاحب زمان» از صادق آهنگران پخش می‌شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103838" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3713adcda0.mp4?token=KEK607Zrko57RaBlD5UE3b2DkQSsYTy_2hyUZi_6irFlwE6S8Im24lquIYTJN3iANpaVNr-2eElhFoRyl7_oJLPIUMoTPcoTXa-8Zbe4JUjhrcc3GDuB-bX1dDqGSklJ4oXWd1xggI3w5yPqkIE0TOr16tkgQsAP_K9UvK9_vSxuz3OgMXW5RS0wr18DacOi5rMgMJBIDK4nEWxlbuHQwOg7mxPo8fZKAeBkqBUKGvgPIKohfccbVPvmCqQR_PHTRhgnGHZZA1oPzKS7iOzAqJTzy58xQIM2tnK2EroFv8KvJLaE46Gqz2kErTOBDx8E668sOqhO4VAi6xsRy2L_VGgn5ilg3ksFXGthfM7KjzfYRryVkaMzXKAWjjk64JWLncqr3OoU-mV1_dS4GsG9FOyLLvgvXYN8XODaWlLewBf9e8MXJ1omKCuhiMKOnxizhdmcKJlWEb6xF-V56GaB_MN5mF2Dd66Zejq_k0cDNJHDrA_na8Lm6RnL4y-cUx6VGhL4Hcq7GHUtGKtjjs3Rv6iUbDR3xvZK-rF0KBALCy5X7QZVOvr1ZMuQeqA4aIIZukcMhtBfxRyud6AOOZmqE4ZFBTmvOW6N3NDw1tqBgmKKMTKHWzPMDqdWZXm_e6hcGejHw9F5Dxud77kaYSFkejPrhjpvrVCV5Y95dWxgKmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3713adcda0.mp4?token=KEK607Zrko57RaBlD5UE3b2DkQSsYTy_2hyUZi_6irFlwE6S8Im24lquIYTJN3iANpaVNr-2eElhFoRyl7_oJLPIUMoTPcoTXa-8Zbe4JUjhrcc3GDuB-bX1dDqGSklJ4oXWd1xggI3w5yPqkIE0TOr16tkgQsAP_K9UvK9_vSxuz3OgMXW5RS0wr18DacOi5rMgMJBIDK4nEWxlbuHQwOg7mxPo8fZKAeBkqBUKGvgPIKohfccbVPvmCqQR_PHTRhgnGHZZA1oPzKS7iOzAqJTzy58xQIM2tnK2EroFv8KvJLaE46Gqz2kErTOBDx8E668sOqhO4VAi6xsRy2L_VGgn5ilg3ksFXGthfM7KjzfYRryVkaMzXKAWjjk64JWLncqr3OoU-mV1_dS4GsG9FOyLLvgvXYN8XODaWlLewBf9e8MXJ1omKCuhiMKOnxizhdmcKJlWEb6xF-V56GaB_MN5mF2Dd66Zejq_k0cDNJHDrA_na8Lm6RnL4y-cUx6VGhL4Hcq7GHUtGKtjjs3Rv6iUbDR3xvZK-rF0KBALCy5X7QZVOvr1ZMuQeqA4aIIZukcMhtBfxRyud6AOOZmqE4ZFBTmvOW6N3NDw1tqBgmKKMTKHWzPMDqdWZXm_e6hcGejHw9F5Dxud77kaYSFkejPrhjpvrVCV5Y95dWxgKmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
کنعانی‌زادگان: در بازی مقابل تیم‌ملی مصر، عینک فیلمبردار را به شجاع دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103837" target="_blank">📅 23:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bb9b634.mp4?token=WLjgbo--dN9UnFCKG0Mh6Ef7fFoIQdli2iYwPWTiDx8LuFbQf4nWBz4Lgays8pgXEz4OUj0P0z04wB-mBrSLSl9ufvq1bALsIoUMNDCZlxCqTT0Wn84UAyY0JpsH5ML9-FSCOvYwJM3027EYqXoxqEzda7ouDZqD1lN3avG4aCu9lF-Id5ygFVNB2DPhMqRZLl3aokJ1kKaB0dNKC_Kq6W-MhrzdTzeiF9CDGs1gIDCC6bdao8QG2OUe7TeUi-LzuavlQuvpZNt7pB_mFClvHX6Onf1pASkIBt81Hh1CaB6Xb05rWlI6BYF35XZ6PUQVB5b41P8bO2qFsoTlNwlL6LqC-yCHCfjKXPCmBR9stvhS61C5Wh_5A7FUekqaUK12cnGtEUe7f6EI1m8IGdoVTzszrgxZkmxs7NYAkqvcBclq0X4F60xnSaPYh64VSrSQvceZ6XP6VjC_agKbPacEYQFDJYoTAw5oaPfPgvzwtI1Nj6M07FZAps1_wgkQfsjYdgCjUE2NSecQuIseoPFp3bkbiqjaKmCk_7O8MHIsPPhg_uYqn7qGw1kRLXOA2aLJNoWlZvcl9E33iakFpgza_4L7xApYmjYroqeXDhF-YZuzv-SzKjuqfJ84mYI-pFx9PUIWELGPxwU1EA6xCjpo2t5au_rKOBsnC0_lhAPx1w8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bb9b634.mp4?token=WLjgbo--dN9UnFCKG0Mh6Ef7fFoIQdli2iYwPWTiDx8LuFbQf4nWBz4Lgays8pgXEz4OUj0P0z04wB-mBrSLSl9ufvq1bALsIoUMNDCZlxCqTT0Wn84UAyY0JpsH5ML9-FSCOvYwJM3027EYqXoxqEzda7ouDZqD1lN3avG4aCu9lF-Id5ygFVNB2DPhMqRZLl3aokJ1kKaB0dNKC_Kq6W-MhrzdTzeiF9CDGs1gIDCC6bdao8QG2OUe7TeUi-LzuavlQuvpZNt7pB_mFClvHX6Onf1pASkIBt81Hh1CaB6Xb05rWlI6BYF35XZ6PUQVB5b41P8bO2qFsoTlNwlL6LqC-yCHCfjKXPCmBR9stvhS61C5Wh_5A7FUekqaUK12cnGtEUe7f6EI1m8IGdoVTzszrgxZkmxs7NYAkqvcBclq0X4F60xnSaPYh64VSrSQvceZ6XP6VjC_agKbPacEYQFDJYoTAw5oaPfPgvzwtI1Nj6M07FZAps1_wgkQfsjYdgCjUE2NSecQuIseoPFp3bkbiqjaKmCk_7O8MHIsPPhg_uYqn7qGw1kRLXOA2aLJNoWlZvcl9E33iakFpgza_4L7xApYmjYroqeXDhF-YZuzv-SzKjuqfJ84mYI-pFx9PUIWELGPxwU1EA6xCjpo2t5au_rKOBsnC0_lhAPx1w8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
😆
حامد لک: مشکل داوری؟ فوتباله دیگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103836" target="_blank">📅 22:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867654e00.mp4?token=DPpCKiSAQ4JAzFELwUcAO4qlHL4p4awbqxTdbYAghs2tZ1Mq4rl1T_rDUdch47NHyLxIuc5p0-p0Jz-I2gCJf5ojXpTeoH7dNHG9c4vPVfSTL65NwQ3T1F8rHBqRU-sGzJ9m4UN_IloFuLrCrCQ-x3MEeSVJ8ilqm552oabVfm65TWKaBr4XVFdokk32SaCN1qPoXAxRvN9Bg-640R41c1ipo1PTarFLXvRI8oNKmQ1297nXlbR2em2d9kxMPVjDI_nWw-WVh79JZZFV9oU8DqxkuYAcQLkkRvJVZ-TPpay8AP5rzod_2u5fbu8H1375XXWn_UqKcpvRtch-V2flIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867654e00.mp4?token=DPpCKiSAQ4JAzFELwUcAO4qlHL4p4awbqxTdbYAghs2tZ1Mq4rl1T_rDUdch47NHyLxIuc5p0-p0Jz-I2gCJf5ojXpTeoH7dNHG9c4vPVfSTL65NwQ3T1F8rHBqRU-sGzJ9m4UN_IloFuLrCrCQ-x3MEeSVJ8ilqm552oabVfm65TWKaBr4XVFdokk32SaCN1qPoXAxRvN9Bg-640R41c1ipo1PTarFLXvRI8oNKmQ1297nXlbR2em2d9kxMPVjDI_nWw-WVh79JZZFV9oU8DqxkuYAcQLkkRvJVZ-TPpay8AP5rzod_2u5fbu8H1375XXWn_UqKcpvRtch-V2flIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103835" target="_blank">📅 22:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd00ae5ce.mp4?token=toLAIqK32yp546p04DIFLVmzEEGV8VRIN3NPKuipX3jPrptCs2PjpTM1JbMPcjQ5gy_q7O0OwKOrjZc7Kh-CceBu5NfadHjJhq2byHLBwpyYOOHrW-OKH84EYbiOIhClwSeMXmxKcn7DySSOiGrbJdrdD_GYR4DcFAYWQuFMU_ehS9YGdLrpxMZSkG6qK4bORExOjJA3veGfxpjD5vOD0punVe-OQYlGQDe2r8EA6lUhI9jhdcQ35V3jVgIIiEW9QgXY5VdUzTzkczA-iHHMv67QGHG9wfyVXEJ8dGkFf_eb5aC8eNn7Cm3edGF6GbFJ33Z_HR_DrfZvP0ocYsqtp7jNsE2MfVRc7h-6YsMGKNi-cLOBfcTu2HrXr4bZNbfkj0xRGT1U01kr7hhxEcGCCTl6X5uj-TOcJ8mtQhw_zsskuAfwu2Jm3aDFe69KOt0o8kbRRQfGcE2zuLNa7AtEiCbCZNyU5h_iq9gBlvJL2AJP--BZcEbWbf95sEU_iLksNknPTc5w7fjk6tFNbN_46naMWxXBotbd3MtPmRr2nWKXRKtu0l7UyOiiVt9_B30u7O2RrMtmY8_R6YE47GezfWgaHaWOBcZVq5ZCU_2RMBhXKpo51Pi-VqjYmLr_OzMjyiuefaUCgjWTZM7iG7RG0R5GX7Q6dFqAylt_SBFeGVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd00ae5ce.mp4?token=toLAIqK32yp546p04DIFLVmzEEGV8VRIN3NPKuipX3jPrptCs2PjpTM1JbMPcjQ5gy_q7O0OwKOrjZc7Kh-CceBu5NfadHjJhq2byHLBwpyYOOHrW-OKH84EYbiOIhClwSeMXmxKcn7DySSOiGrbJdrdD_GYR4DcFAYWQuFMU_ehS9YGdLrpxMZSkG6qK4bORExOjJA3veGfxpjD5vOD0punVe-OQYlGQDe2r8EA6lUhI9jhdcQ35V3jVgIIiEW9QgXY5VdUzTzkczA-iHHMv67QGHG9wfyVXEJ8dGkFf_eb5aC8eNn7Cm3edGF6GbFJ33Z_HR_DrfZvP0ocYsqtp7jNsE2MfVRc7h-6YsMGKNi-cLOBfcTu2HrXr4bZNbfkj0xRGT1U01kr7hhxEcGCCTl6X5uj-TOcJ8mtQhw_zsskuAfwu2Jm3aDFe69KOt0o8kbRRQfGcE2zuLNa7AtEiCbCZNyU5h_iq9gBlvJL2AJP--BZcEbWbf95sEU_iLksNknPTc5w7fjk6tFNbN_46naMWxXBotbd3MtPmRr2nWKXRKtu0l7UyOiiVt9_B30u7O2RrMtmY8_R6YE47GezfWgaHaWOBcZVq5ZCU_2RMBhXKpo51Pi-VqjYmLr_OzMjyiuefaUCgjWTZM7iG7RG0R5GX7Q6dFqAylt_SBFeGVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🚨
🚨
🚨
🇮🇷
نصیرزاده: اینکه فسخ برای قانونی شدن باید در فیفا یا فدراسیون فوتبال ثبت شود اشتباه و ناشی از بیسوادی است!
📝
من قبلا در باشگاه استقلال نبودم که بخواهم از این تیم حمایت کنم یا در جایگاه مخالفش اما ولی باید حرف حق را بزنم/ دوستان باید سواد حقوقی داشته باشند که در این مورد نظر بدهند/ موسسه سیلا، کارهای وکالت آسانی را انجام می‌دهد/ این موسسه به باشگاه استقلال نامه زد و گفت به علت اینکه مطالبات آسانی را پرداخت نکرده‌اید، این بازیکن جدا می‌شود/ هیچ کپی از این نامه در اختیار فیفا یا جای دیگر قرار نگرفته است و موسسه سیلا این نامه را مستقیما به باشگاه استقلال فرستاده است/ اینکه برای قانونی شدن فسخ باید فسخ در فیفا یا فدراسیون فوتبال ثبت شود نشاندهنده بیسوادی است/ فسخ یک اراده است و آسانی می توانسته فسخ کند چون مطالبات داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103834" target="_blank">📅 22:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce26cb22e5.mp4?token=QYgYTbA2cS6EfjvaczMFP7DbIPOXAk25qHH-8erVjfQ-cYApukCQ_5b4YZadEXZ0Z-AR7wBll-1020o1gog-gv4VEER6RKqlud2Fq3rhctswIjZbVTXDwTP7kdEEnj6D3Y4hipxtf7MzsLTxRmnZUcaDH3jX8xUn18rf5pyGyEjeoJZb1FwyLw91waxumI9RqSetX62QnMZL5SLuGU79eqF81dJTHOHmzpMxZlt9b2qxZsp81pwulFWN3BbH4j1knPgqgp0uADpv1ZbZxS2bu9qLwRILnOyuicau81OIaZt8abtZaroyEMu-snCVnGvEGyO4XXb8iegTwsIdQIEFcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce26cb22e5.mp4?token=QYgYTbA2cS6EfjvaczMFP7DbIPOXAk25qHH-8erVjfQ-cYApukCQ_5b4YZadEXZ0Z-AR7wBll-1020o1gog-gv4VEER6RKqlud2Fq3rhctswIjZbVTXDwTP7kdEEnj6D3Y4hipxtf7MzsLTxRmnZUcaDH3jX8xUn18rf5pyGyEjeoJZb1FwyLw91waxumI9RqSetX62QnMZL5SLuGU79eqF81dJTHOHmzpMxZlt9b2qxZsp81pwulFWN3BbH4j1knPgqgp0uADpv1ZbZxS2bu9qLwRILnOyuicau81OIaZt8abtZaroyEMu-snCVnGvEGyO4XXb8iegTwsIdQIEFcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
از خبرگزاری ایسنا؛ ارونوف بدلیل ناراحتی بازی نکردن در شادی بازیکنان پرسپولیس شرکت نکرد و مستقیم راهی رختکن شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103833" target="_blank">📅 21:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx5FkKP5nYXQTqzA74rJpKEvky4nh9_zQKcVeRnqmk6G6jiS6nc9FlZPHM9iXSG02K0hBry49Wap7GFG8HCht9wm2Ak1FVf51XVkAiSRMh7poPXiYi7pFywZ0Vc6EgfXWLbJF8oh7Ls0CqGYjHWZ_dsWveA4kATP0sgEVMQZoxy_daMJiWV-EGUJiiBLkYloSZQ1O4AD_BZuu0m9mKanYKMTY6h0xb7CG0azdyncn7WDSsaD5zw9JlO3FhQDtj6AeXb2FfqGW4im245CpObzrynjeY9KStnroFvCD461A_aQEVXRwzEldDyxDxHIfK1tI61qWfL_R5CprtDZVcNEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
برنامه بازی‌های هفته‌دوم پریمیرلیگ ایران؛ روز سه‌شنبه و چهارشنبه بازی‌ها برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103832" target="_blank">📅 21:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKpIiTSg1alyb_dBZdpw1OQ-A6hBY-DGX77WAGiozggd978eyWbqEMOkz33Qn0eTHwQryABV8AOFwodKWni_Mp1f8Nagmxzz6o3FHVv8SGLONwE9YdIZ3qvOMM-Z0otFLNT4U8JNhl7CUqTBD_AfVi9uKGu85m9At2vqYDmcmrlcIybiHWNq7NNcmgZpBy7XwQ6rNlFG3T5eoIysIg7qyXxwPWWpumrMUMprgxkZta6A_j46oWg0QNJ4OUwYqkEiReEugRDCRmCUneHAB3XczTGE0hv8_lzembMq1JpmPLOpXfLnEWpN10RkspVcKgDTuz7SBJyPqU-DDeQuQLDfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
#فوووووری
از لپاریسین: لیورپول میخواد پیشنهاد فوق‌العاده نجومی ۱۴۰ میلیون یورویی به پاریس برای جذب بارکولا بفرسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103831" target="_blank">📅 21:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpOl5O-jekJGmywl_D-7AMYl1LoDWHjo_Bthmr5S__FxbOAxW_Sou-csNrpBUSNv5sBeqfNiXlpSG6TmeL49pWn5mueGS0FQN1YPckg0OwdaJq0q9jtzvqyGSVZhMlxZvWGBx6jfOFh7Oxv9WL_xay6QqxhgJTm4MJvRWS7eXDjRRF4DHnkZE2CqO8PWQQ3N4LhkpvKG5jNEL61BX_7ET8Wlf0JsHBH2RBebbg_T_0W33vmL9l2aE-WAcSSA1Vfjb2xkR6J9AEnQuTPXncpNkIIKoTob_JIG1HnG7lrloXNg9oG7uxT1nERsHA9gnenb9O4skmYYkrv4r2p30D4m_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید نوید محمدزاده با لباس فلسطین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103830" target="_blank">📅 21:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgx-NYioOiNnuiHA__379NWRHW4nsQyuJEbbeNvHe4e5IgLSOcsq_X-KYoimGZuJHKFu0sp44qK1k4Wd9V70xKBSHzXYdej1esTJKYHazlzfvzxF82GG4I7zQ9XVO6DsOMjgaN1du3vQinaxBk6OQ64Kl9ZakiD6qIfld4aT622XNW1cD5q-7Iie-kMx3thZM_xkZEpTSGTbYrPCW2NedwHnFiLir3Cpkk_sKW2GI5oXCbw-5shEdxt6U4_Z2ORuO_KSr6a6pa6cIhSIi1yMINTX72J-LK-AD9Z_5zQkeEg6etng0JMYvBZZXxmEEWatBkujiIOwE673Wxd_1AD9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
هفته‌اول لیگ‌برتر فوتبال ایران؛ نمایش اقتدار در قزوین؛ شاگردان تارتار با صلابت و یک نمایش درخشان سه امتیاز را کسب کردند
🇮🇷
پرسپولیس
😀
-
😏
شمس‌آذر قزوین
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103829" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3eimCDag1JUhZQUQ8wvlT4zhDBJVmuOD9LZCkhWquWAhWbn1jX-rYsrjF6RCY_sTHkK-T6bYF4QVJOcX6CQSF4M2uzxkEC94aVRMzFqLPs7ebAB72J_GHskHoL1aabTDO4j-R316dBYqN7Ag0UIKWdmIMOQEni6ylUunnSzTnDVnveR5w2nMf6dS08G4CMMJyRM6ibBmOWYOvRvUeOP_FtlXJ8TT1be5zGEpUNRm5Tp1hOGiJuptHcSexTquEiXWXHoYU6A7AahkzfzhnllZlDZuwimZguoP_Hf1C7XPSGXsqF21udlUhY7ZtMX5nKxnsDoKf39Cf7wLux8VBfUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رامین‌رضاییان یه استوری گذاشته از صحبت قدیمی مهران مدیری که گفته هرکی دست به افشاگری بزنه خائن و بیشرفه
گویا جریان درخواست نود رامین جون درسته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103828" target="_blank">📅 21:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe1kFV-s1hiH67rQ5k5aMmNb9wXDBC3QoAHPa9Cv3rdH2zHC9Si7DNS9z02sA98qSYVinjLIxjCSs5hRz9CamIdtffDuD1Wv_5xbJ8LfeP48XQBNMa-HTfTkDnOhtw3QljPUYsF0xqLkSQFlDbAn5DwvJC5g26RwReJ6lcZb4eyk85QULJ6bi2Gfoc_IwLhPm9R3gCjbAkgiegWlrpOxiUPxOot-Jk7b5ObTWiNLqR-UgLZ-kUVIPHY3UeeOqC7sqHrf_Z0U3VeG-OcllVzU2F0dzkmN5MLr63C8BKWv_BswdeBFaccCawjsEgBMuJ4xMuuftAr0ZAzPHt_XFcK2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
الطلبه تحت هدایت علیرضا منصوریان در هفته اول لیگ عراق با نتیجه 2-1 مقابل تیم دیالا شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103827" target="_blank">📅 21:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrEcOFEpi8JGr2X0mV2Njrnu8zX7hcgfLLf-cZNa1EMabb21P4cWGwPq1i0V3YV8F91QeRR5wqhEGY5B21dJPiABJodAhIZN3cme8BMO4pNnTYg_g9Grt7VI2Nlme1lUQJQWSxa5YQ_PJt1C61pee4HaheKK-fXRGq1XDuSx80nPk9iVgcLZCC-Han3Mium9Yxa_9nDyGHJxod5G5xc1uh00OxbdWtQX9wcSVjsXTBOrCGAu3ZU4xdVvARbvcLVOHnAeQPqnvWZg4wFEE34GKiezk2OftnihnCRF7mURH68OOJZk5aOV85BvemJI8FQn5358pcB4-K5Ixr61yiCtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از RMC:
❌
منچسترسیتی سومین پیشنهاد بارسلونا رو رد کرد. سیتی گفته فقط با ۸۰ میلیون یورو راضی به فروش رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103826" target="_blank">📅 21:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e246017a9.mp4?token=Pnb1GOoUK_ZruXWSMTA20Drhc7Oo9bcpg3g4-27uFmGx1smiJ27iCRqekNzZeKucQ5jtbhfyNHvh052ClNVtGbCtoZFsbPFbg8P2JssafC70zz_6pXCtKE-kw2cC6PJqBPbgpFEY49BbcXrlFTCto5v21PmE0ixESVqpejdMWGzJj0HWa1EjjbBl24cU9VpGyk4ZKPlOeYYRddcma63V3ki5HaZBggMDZn7WSw6u-QJ9BFYpsUMSNCNLcBTU-tYA2c969xcQfv0zoJpaG7MAiVyZlkFwILXukKMjaWRBzrmm9ZLmT4gvStWeTQRlJScmdLt9TuI4U2zkTd_EOBiFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e246017a9.mp4?token=Pnb1GOoUK_ZruXWSMTA20Drhc7Oo9bcpg3g4-27uFmGx1smiJ27iCRqekNzZeKucQ5jtbhfyNHvh052ClNVtGbCtoZFsbPFbg8P2JssafC70zz_6pXCtKE-kw2cC6PJqBPbgpFEY49BbcXrlFTCto5v21PmE0ixESVqpejdMWGzJj0HWa1EjjbBl24cU9VpGyk4ZKPlOeYYRddcma63V3ki5HaZBggMDZn7WSw6u-QJ9BFYpsUMSNCNLcBTU-tYA2c969xcQfv0zoJpaG7MAiVyZlkFwILXukKMjaWRBzrmm9ZLmT4gvStWeTQRlJScmdLt9TuI4U2zkTd_EOBiFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیوی‌بیفوما بدلیل مصدومیت از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103825" target="_blank">📅 21:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4096d1153.mp4?token=ERxXrLKcoXVKf9-6Cmmo1mvp-Cue3lc46EKGv32_wSuPHB1rMa2gSaXJ79GWb2MD9mu7vrvTbJ_huKL6Z-AFrrBzZDF54XwEIKjGSNY85Nd7EqZ-J6K4VTq-c-UISo9bGoBFIkV3M5pGHmmMwaZmjsAmU6SzN6aNCsiqcRKHD0wVQiPPo2QWw7qfehZt8pYPF1OuFBValjBghoojg1Y5YDJ-zXIyLW5gM7qdFuObLWAuCJCMkshOHqJWMNtm39gkmMImEVjh2gBPhYOjqoXkyFqSSknkjKTQyR8zbLika3qTU_DI6CugFEQMQcIPElbjff1LNOfDz2ZQuHDEhWCUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4096d1153.mp4?token=ERxXrLKcoXVKf9-6Cmmo1mvp-Cue3lc46EKGv32_wSuPHB1rMa2gSaXJ79GWb2MD9mu7vrvTbJ_huKL6Z-AFrrBzZDF54XwEIKjGSNY85Nd7EqZ-J6K4VTq-c-UISo9bGoBFIkV3M5pGHmmMwaZmjsAmU6SzN6aNCsiqcRKHD0wVQiPPo2QWw7qfehZt8pYPF1OuFBValjBghoojg1Y5YDJ-zXIyLW5gM7qdFuObLWAuCJCMkshOHqJWMNtm39gkmMImEVjh2gBPhYOjqoXkyFqSSknkjKTQyR8zbLika3qTU_DI6CugFEQMQcIPElbjff1LNOfDz2ZQuHDEhWCUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اولین بازی محمد صلاح با لباس تیم ترابوزان اسپور؛ ورود محمد صلاح به زمین مسابقه در دقیقه 58
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103824" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHlVytNMsN8pxX7yUDvtS75ZBded8IZrLfrdbmiX3Ocf1MGN3AaeVEGNF_xdrsHt8nfUAUxibmnryaeIthmEig2zVQR5OxHrrTI6ulyT8eLwQWRZe-oYVjIrlqGOcbZJxHrrWmDWqVyCm2arXbUKImr0uwshNrOCDfTpy_74F4BKihP-XxBwxA4a4E0tdakSc2AosljP3mOSY8DGfc1_DREC8S0Sxbo96ol6JEkgphw-p3xBoK7IBMpJDYdZBru3PK_qZNyaXVmWYDpIA2y5Ic6mi9M9BGCIuRoL_P2F-NyLFIEIh_BZhMTHovYE-eOFy0cA47NDEYrVfMhACVsWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در غیاب رونالدو؛
🟡
ترکیب النصر مقابل الفتح در لیگ‌عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103823" target="_blank">📅 20:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639cd87b79.mp4?token=mRo_BSL912MZ3vjFC7-Ab-nlRtYEdW33HeoBeR71DrNiybdJ0HUe9HsczgDPWmVv9jCJPt2zK15yXVHQuViCjQk5-yZTNgqZqwjUhKCPbTwgsM4uRnEB4DTGRWa6BV-dIYhw4AEqIpx6IAC48TUFX6JPecOb7zHKMAtpA_AAhjDG62E5Pq4CRFFLrDedy9R9qqpaBKmeqsk94bZRJ9l64y23mVSZ71rDDPi23GYzVabcdghaB-T7jZHeSpB173pW8W02wJpTs6TfKCgerSiKbRfPjiAGcn4y1m0UBYHNwKVLEaY8fleCDqKI7fQPaqt2SqK83z_9-ckPFZuH5wcvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639cd87b79.mp4?token=mRo_BSL912MZ3vjFC7-Ab-nlRtYEdW33HeoBeR71DrNiybdJ0HUe9HsczgDPWmVv9jCJPt2zK15yXVHQuViCjQk5-yZTNgqZqwjUhKCPbTwgsM4uRnEB4DTGRWa6BV-dIYhw4AEqIpx6IAC48TUFX6JPecOb7zHKMAtpA_AAhjDG62E5Pq4CRFFLrDedy9R9qqpaBKmeqsk94bZRJ9l64y23mVSZ71rDDPi23GYzVabcdghaB-T7jZHeSpB173pW8W02wJpTs6TfKCgerSiKbRfPjiAGcn4y1m0UBYHNwKVLEaY8fleCDqKI7fQPaqt2SqK83z_9-ckPFZuH5wcvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
سوپرگل صنعت نفت آبادان مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103822" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6e07b20f.mp4?token=hxvMVgG8aUUDPklm4DetFoKM9_IV598SjM1HnTTIkCJRyA_YOgrEPHGZslZh_mL3SD9wX5ffzUNuLMQiwo2ypjs2mtWg5RM-1X0YQtvGBvTW2QbldJZZU5w1yOXiTAy0p2Hdh38hCeG1LiQu-W7gfbaERLzSBOB-kNONfCCqt1U4Mq2gbmm9qPW591oH2SHKWL7wEPQ-2J7ItnysHUKCNY6FRNPT8h04ahMkVLq8TggfdyIUh5z-p5XvFeIFJO_MNDg-cJgOivlzR8r5xHBIgOAsz4Nl_seX9v2B7KDJWJ7Fo01lL1EPCtnNrtssPKcbHDrL9Lnyk1mrQUGEd0CRzkg3TergSgHOqCCzK9a8wdG2ACXFn4PfvkBH-RCbrxOvIsucksUkJG8j3m9XepGeV1_FZYkqIl0oIFoGh5afPr4phfzkt_PymtJ-6ooOOEBqzlXVvaKgrA0zzbfKfLtvnfFFq69BvRQqirfiyY3PU21LwRllEDtlsZBh6DC5zRq0Ft1MAYi0n37XYjfnivPt-lg4A0j6wlsZ_a-cgPUiYPvDkyWvh_j5djsoElkeDn5kTZfypo9IbRz9jm0KdMdAMsRj3botJlIt-DfZ8d7TK8hVXd00FOei8r_ZX7e2LfgsMHXMQh4FH_GO_DBkWB4Ch-FuAstbTpVIbNEO407FGuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6e07b20f.mp4?token=hxvMVgG8aUUDPklm4DetFoKM9_IV598SjM1HnTTIkCJRyA_YOgrEPHGZslZh_mL3SD9wX5ffzUNuLMQiwo2ypjs2mtWg5RM-1X0YQtvGBvTW2QbldJZZU5w1yOXiTAy0p2Hdh38hCeG1LiQu-W7gfbaERLzSBOB-kNONfCCqt1U4Mq2gbmm9qPW591oH2SHKWL7wEPQ-2J7ItnysHUKCNY6FRNPT8h04ahMkVLq8TggfdyIUh5z-p5XvFeIFJO_MNDg-cJgOivlzR8r5xHBIgOAsz4Nl_seX9v2B7KDJWJ7Fo01lL1EPCtnNrtssPKcbHDrL9Lnyk1mrQUGEd0CRzkg3TergSgHOqCCzK9a8wdG2ACXFn4PfvkBH-RCbrxOvIsucksUkJG8j3m9XepGeV1_FZYkqIl0oIFoGh5afPr4phfzkt_PymtJ-6ooOOEBqzlXVvaKgrA0zzbfKfLtvnfFFq69BvRQqirfiyY3PU21LwRllEDtlsZBh6DC5zRq0Ft1MAYi0n37XYjfnivPt-lg4A0j6wlsZ_a-cgPUiYPvDkyWvh_j5djsoElkeDn5kTZfypo9IbRz9jm0KdMdAMsRj3botJlIt-DfZ8d7TK8hVXd00FOei8r_ZX7e2LfgsMHXMQh4FH_GO_DBkWB4Ch-FuAstbTpVIbNEO407FGuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
احترام نظامی ابوالفضل جلالی مدافع پرسپولیس پس از تأثیرگذاری روی گل اول پرسپولیس به شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103821" target="_blank">📅 20:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو: جد اسپنس از تاتنهام به اینتر میلان پیوست.  𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103820" target="_blank">📅 20:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
‼️
🎙
پیمان حدادی: اعلام قهرمان برای فصل گذشته منطقی نیست/ می‌توانند تورنمنت 5 جانبه بگذارند که ما هم شرکت کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103819" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad592f134d.mp4?token=Vllf5ERml1PPjMaEvmwInNQNbNV0UIDHT7U6C9Bf1sswaHmq3dldM-0ZbzJtfRueHMrcNZSyRo8mUzOUxvnnPbheRsiaUBobrfpmX70_VkaI4A6dkw0ST5fjzM3jkv2MnLOsbNyqx-AIdya8tLG200kM1WHNxGGLQvENuCR-qU5q_mOORASm4C9PkFYkq0X4xC1bCGr0KhTD4MOWo7LVDMfvEERc6fY-qpesDlv-dd1Ovw7DeNxiYQOfrZeTMz9NUfYuUILe9rWODYuklD_KVGUnIFqQNTBggDSimfjK11Dr83iFhREBgh4_qq1a8KVu-egPZLbqEklKEkYtnd3uMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad592f134d.mp4?token=Vllf5ERml1PPjMaEvmwInNQNbNV0UIDHT7U6C9Bf1sswaHmq3dldM-0ZbzJtfRueHMrcNZSyRo8mUzOUxvnnPbheRsiaUBobrfpmX70_VkaI4A6dkw0ST5fjzM3jkv2MnLOsbNyqx-AIdya8tLG200kM1WHNxGGLQvENuCR-qU5q_mOORASm4C9PkFYkq0X4xC1bCGr0KhTD4MOWo7LVDMfvEERc6fY-qpesDlv-dd1Ovw7DeNxiYQOfrZeTMz9NUfYuUILe9rWODYuklD_KVGUnIFqQNTBggDSimfjK11Dr83iFhREBgh4_qq1a8KVu-egPZLbqEklKEkYtnd3uMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل دوم پرسپولیس به شمس‌آذر توسط محمد عمری 15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103818" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=piDQfwcdEMJQp-A7YBkrlqjoHLjyu3VEFIpQfhEB1CoLpG4YXgqRqAq0qP0Qit1spSMQn_mZdJ8AAsdQBTe9qJkv77cO7TingVqj0IY07GIYG1Bfjq_DlO8ss3MhC-fOP-AKLG6CML83bUYm7J_EHJefRPWIKv9tUAgQFO-Pn9nUs_45K-MCb84mEcU9naRDDXms4g2R2QJTUOzN9EqiqMAofKAX5WyujaqcSkC5aGRtOHfcwJqZARdckV620jLwlpVCLzbdeCYFnHS7bqBLucj2V3DfZQ8Mje9BV2hjp3UxL8KFy3-xHQxJMpjZ408v9ZExLhwEPZNCnNc7RU0PPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=piDQfwcdEMJQp-A7YBkrlqjoHLjyu3VEFIpQfhEB1CoLpG4YXgqRqAq0qP0Qit1spSMQn_mZdJ8AAsdQBTe9qJkv77cO7TingVqj0IY07GIYG1Bfjq_DlO8ss3MhC-fOP-AKLG6CML83bUYm7J_EHJefRPWIKv9tUAgQFO-Pn9nUs_45K-MCb84mEcU9naRDDXms4g2R2QJTUOzN9EqiqMAofKAX5WyujaqcSkC5aGRtOHfcwJqZARdckV620jLwlpVCLzbdeCYFnHS7bqBLucj2V3DfZQ8Mje9BV2hjp3UxL8KFy3-xHQxJMpjZ408v9ZExLhwEPZNCnNc7RU0PPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به شمس‌آذر توسط محمدمهدی محبی
11
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103817" target="_blank">📅 19:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6baeb89aab.mp4?token=ZAkYWtjhP69nqVNRRcemsyeSujlBz64WuNGe_KupaUlPbcJpgc9TFZCoynKp-6XvNZuYGfmAcLPh-oD0JjZu5m4YRXECfGqqvgxuevyYJkyvr0pa0aRyFbA7THJb6NhsoNVKcvCgU7xSRfokfUESZaRXqJ8qCknklYXZ38ZmCq0mznbRzb3PfKTAPYtzrn8GQhivY-zxNcB3Yxl-moN7CK7r3Kaku321MUtnmx2QyeCgxnZgm3_3rzYBGSd67ta4jpifzARg7VjWmA1irpJMtlreyQ6GBnq-x4RDFTtZOcQXJZdmPyUMiJUhkVEuJf4oA2Q0X7oBZbgtToIY1QnlqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6baeb89aab.mp4?token=ZAkYWtjhP69nqVNRRcemsyeSujlBz64WuNGe_KupaUlPbcJpgc9TFZCoynKp-6XvNZuYGfmAcLPh-oD0JjZu5m4YRXECfGqqvgxuevyYJkyvr0pa0aRyFbA7THJb6NhsoNVKcvCgU7xSRfokfUESZaRXqJ8qCknklYXZ38ZmCq0mznbRzb3PfKTAPYtzrn8GQhivY-zxNcB3Yxl-moN7CK7r3Kaku321MUtnmx2QyeCgxnZgm3_3rzYBGSd67ta4jpifzARg7VjWmA1irpJMtlreyQ6GBnq-x4RDFTtZOcQXJZdmPyUMiJUhkVEuJf4oA2Q0X7oBZbgtToIY1QnlqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
پیمان حدادی با کنایه به استقلال: یک باشگاهی فصل گذشته برای پول رضایتنامه بازیکن ایرانی 2 میلیون یورو هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103816" target="_blank">📅 19:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae65e3495.mp4?token=H4CQfZwXDDdWMEwQWfWKp_ky3JEervPxMNOIPVRk3RmdFBIqqpzUgEv3MKV8HPackw1zYo4-k-pcht4JleK7zSQcCnwdK5LQ7MmFUW61oPbwrp087HXeus07xao0oz-YWafLi-y4YT7g3dR5WavdmQ5HQ1PkX4KdiH7JcVWWfyKgw6kVTLSslEAjTmS25x-m2YoTLB-1ZVOTXZAhZkjWD8A3mF7NVpHpbzA2MIbVUn2cTB1B5IjO__fzsbsBs3sexlbcZh5nIekguDint_6zpn46A5tIXa8E7ltCgV7B8BEsx0j_zYLpkL43XPmDOlfgQTrXBxgV_HGFe5GEJtdyjo7vZxBQ0gA18t2q1DRaFOYuMIru8PPHLYevJMaZ5B_NwrXvo_OM9Wmd26_jzmhRF2mlcm2PoUZip4aBMRP0gpB_ZgAIyfUa9kiCzwieLnvBJwg-sxTkVKyEVpL-T25bxf53a6FVQqcLVTq7Rcp89wzQwBxggVMaUOdENYvoR6CwiQv2ou0Wikpk7tX2CBFOGtPtWmXpdOGfo8rVnsHgxiwj4FCYBL6rC4XyUUqRCeEsOfD6lPGRRKoxBWWR61GW_OqRMuu3LB7y1Mo0lqlo4bCgje1LVO_Dw4YRRgLju0sb0gKIT7sJ7WR4NdPnEkj4aS42GMB4gsIReLZAHHOc1HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae65e3495.mp4?token=H4CQfZwXDDdWMEwQWfWKp_ky3JEervPxMNOIPVRk3RmdFBIqqpzUgEv3MKV8HPackw1zYo4-k-pcht4JleK7zSQcCnwdK5LQ7MmFUW61oPbwrp087HXeus07xao0oz-YWafLi-y4YT7g3dR5WavdmQ5HQ1PkX4KdiH7JcVWWfyKgw6kVTLSslEAjTmS25x-m2YoTLB-1ZVOTXZAhZkjWD8A3mF7NVpHpbzA2MIbVUn2cTB1B5IjO__fzsbsBs3sexlbcZh5nIekguDint_6zpn46A5tIXa8E7ltCgV7B8BEsx0j_zYLpkL43XPmDOlfgQTrXBxgV_HGFe5GEJtdyjo7vZxBQ0gA18t2q1DRaFOYuMIru8PPHLYevJMaZ5B_NwrXvo_OM9Wmd26_jzmhRF2mlcm2PoUZip4aBMRP0gpB_ZgAIyfUa9kiCzwieLnvBJwg-sxTkVKyEVpL-T25bxf53a6FVQqcLVTq7Rcp89wzQwBxggVMaUOdENYvoR6CwiQv2ou0Wikpk7tX2CBFOGtPtWmXpdOGfo8rVnsHgxiwj4FCYBL6rC4XyUUqRCeEsOfD6lPGRRKoxBWWR61GW_OqRMuu3LB7y1Mo0lqlo4bCgje1LVO_Dw4YRRgLju0sb0gKIT7sJ7WR4NdPnEkj4aS42GMB4gsIReLZAHHOc1HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
حدادی خبر داد: با رضاییان  مذاکره کردم
🔹
او بازیکن قابل احترامی است ولی در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم
🔹
با وجود تخفیفی که داد رقم درخواستی او در بودجه ما وجود نداشت
🔹
عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه ها بود ولی از سقف ما خیلی بالاتر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103815" target="_blank">📅 19:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca7dcd99c.mp4?token=kc8HpoMH2JG9qU3Hlf_A-GvusGGAm2MjlXrfeyuhBNA6Eq6K_7jdA-ZSMQIE53E8ZFgIZGNWIZ4EzK71uM_IakLzhwHEzLYRmLxytRG9734Olubg3P2SuhaL9PW_dT0ho-bHtGfuUfx6HUUax-IjWOy48Z7WKnW-cUgKR90TBrgGbSQC9xbEgRotuXjMo2eGOTWptAbJN1ndVMYNzpHq7vvpd7KZ0CZuh1g8YLN3SfcVkDeHvIotDOk4JHloohVfDqf-BofnAePr2iV3175UQ0AG1ymecTxp40KyQUDxxzs6Zm0J51NiSHfajt0peptAhtNZfPsNLfveyLHarQYXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca7dcd99c.mp4?token=kc8HpoMH2JG9qU3Hlf_A-GvusGGAm2MjlXrfeyuhBNA6Eq6K_7jdA-ZSMQIE53E8ZFgIZGNWIZ4EzK71uM_IakLzhwHEzLYRmLxytRG9734Olubg3P2SuhaL9PW_dT0ho-bHtGfuUfx6HUUax-IjWOy48Z7WKnW-cUgKR90TBrgGbSQC9xbEgRotuXjMo2eGOTWptAbJN1ndVMYNzpHq7vvpd7KZ0CZuh1g8YLN3SfcVkDeHvIotDOk4JHloohVfDqf-BofnAePr2iV3175UQ0AG1ymecTxp40KyQUDxxzs6Zm0J51NiSHfajt0peptAhtNZfPsNLfveyLHarQYXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کنایه حدادی، مدیرعامل پرسپولیس به استقلال: فصل گذشته لیگ برتر قهرمان نداشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103814" target="_blank">📅 18:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103813">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTJ0LpV8t0MZW86TvZkmWO6Hem7eJRSzvazNuF20LjvrPukZVig2D9yCa3potCNJUaQsOAsuxxCrQSo8fHwm_zbrz2Gk6oUrpKaTFXWwIyVCQyNDYRiukJ1JlyvGqnk_CrTFq2nT5uk3aTH99tWdp_iv9O_rBiuJ9CKShA99BOkRpP0r2ql5VSkM1Hj0QN8LhdQKsc4Mk4imAYy2yj7bl4t8sy4WYu5U2JbiUMYPpQVQ-J_2Ri7bTFT6X1TM-xrPPKICuwE9AsD_NIf541GjMcVV57A3YVRKyvcP9dqGWTiKM9GMD6cq5XRcT8GDm-pDRWY5C51BWsIWmBr4Qx0Pyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
هفته اول لیگ عربستان
🇸🇦
النصر
🆚
الفتح
🇸🇦
🗓
شنبه ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103813" target="_blank">📅 18:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R62mojrRoESN1mHf-ivVjH4QjQjWMmSeRbiR7fifGbG4JuTkucLIGu5w8apqJAlRzVbH5OCO62Tm-YqnUufU7OAV4WTOd529y4KFq2-WH9hK7rD3B5TKRPdPv7Vqy9eMVkNb0L_SSaeSptfwZHKKcAbi0CEf3bqeZRCMNb_wlI8nkCAD4UU0nkn_WR7J2q0Y27sHa-rWqj1btqAuoRMqU57Pou94V7aG53H4tivII2VZ1gkf6ZEFEeP0Fk2P1iwosib4ZvtEHSYNhvU_EyBWloTc2L3yjPPCeUjiS_m7E6vq96jdmKN76qzcm3ZqQFm7eZRkFXDq82eu7gexy6mqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیبببب پرسپولیس مقابل شمس‌آذر قزوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103812" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103811">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103811" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4kltlF8EuSdcM1Tvf1x0NNGGghGhCbWavGnjmupPAhwWzaS1W_vMS1sCRTKGYu7us421x4vKQfEFXNpKSxfHxiL5nqnpww5RB-9w6erKHeJ3EVZ-S7iiHGxbEukhQw008PnkBHhSdpNwGBdi4LRF6NzQ3xXONGHLxLW49Ih4_vTidLffyZ_Y4WrSawvtrTkiGWg_ZM6AjGRRi3QCtFzzkWBp5I7Cb5Zfxo08-VT1uh4PM4fcHeg4-HXiioSYnscOu3QfO5b1lqxWPQAvbHLM2UzU9Xhct7h7jA1YhHvF2EliUJp6VgjXPVFjxREM0cT8j8ui907f_TQlMZV9jhmIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g24
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103810" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb39b1afd.mp4?token=vjsWmDVPJfFbxGGe4R1VzAUydeae3Hi8sSXVugaqF4UMVChXUsbVtmTQvNrhzPfKQOIHIFXIEFervggkQTtILi0JhkhdxPPLp1ZOlpbkOkzDaNjBVXCzNgv7VbmrsQnk3UP6cCog154oobekCHK0B1Zbe126Ix3WygXQf9Ar40Oqj-aDyJrWjjWTJ-nj5mZE-dQmDQ-ggpMrlYWPZ0xVUF1aHTmrCMoFuLXH7pp6R6dwzzgRP0GJjwxP8jutWLnugy0d86A5MEiZXqJa2IMRLDirqIgnBgf2_qxyfYtXHoV27wg8ij0sosicwM3snsGIKdxrhhudUtYZWuRddJDg1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb39b1afd.mp4?token=vjsWmDVPJfFbxGGe4R1VzAUydeae3Hi8sSXVugaqF4UMVChXUsbVtmTQvNrhzPfKQOIHIFXIEFervggkQTtILi0JhkhdxPPLp1ZOlpbkOkzDaNjBVXCzNgv7VbmrsQnk3UP6cCog154oobekCHK0B1Zbe126Ix3WygXQf9Ar40Oqj-aDyJrWjjWTJ-nj5mZE-dQmDQ-ggpMrlYWPZ0xVUF1aHTmrCMoFuLXH7pp6R6dwzzgRP0GJjwxP8jutWLnugy0d86A5MEiZXqJa2IMRLDirqIgnBgf2_qxyfYtXHoV27wg8ij0sosicwM3snsGIKdxrhhudUtYZWuRddJDg1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های هوادار شمس‌آذر به مهدی تارتار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103809" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f0533ec8.mp4?token=hoQXnOukN3_XRHZ97yMEJrODSQ6MoOqSRz-9tfosHX9xzKF4PfOqkSw1gQkZTigDiSbOVbX_uptH7RJasfYeiciiIejuloKgfxW2TAgvTma5lrYzACW6yByHaJTLl0z4Z8iSBDcPMXRPYv-47lf055bTRuokNYCSV49NXAj0J4HZtLQ3i-l9GohcsbJIxhZaootqfjglukMy7_QWQeZQOA31jDXlMbFJvIXutC7HZOz1Jnl5igsf-q4Pm-vxWFtvliTzzZ9Lu3buEikXHRspnUbQAvRPxkFoACRd5qxXThHPPbFVci2r11FhHKOrZ8vuBD0EH4KFxucaDsan0E1v5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f0533ec8.mp4?token=hoQXnOukN3_XRHZ97yMEJrODSQ6MoOqSRz-9tfosHX9xzKF4PfOqkSw1gQkZTigDiSbOVbX_uptH7RJasfYeiciiIejuloKgfxW2TAgvTma5lrYzACW6yByHaJTLl0z4Z8iSBDcPMXRPYv-47lf055bTRuokNYCSV49NXAj0J4HZtLQ3i-l9GohcsbJIxhZaootqfjglukMy7_QWQeZQOA31jDXlMbFJvIXutC7HZOz1Jnl5igsf-q4Pm-vxWFtvliTzzZ9Lu3buEikXHRspnUbQAvRPxkFoACRd5qxXThHPPbFVci2r11FhHKOrZ8vuBD0EH4KFxucaDsan0E1v5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
اعتراض
علیرضا محمد، مربی پرسپولیس: چمن استادیوم سردار آزادگان بلند است و باید کوتاه شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103808" target="_blank">📅 18:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqwsFRcGdzMk0mpRn-xPe0cnQRwYfsGUFoiZC1d7I_cSFDGX655XlGvSFBSU5z6aNCpUAtZjKb_jkObLbcuqNMrkv5Y2M6LGolzNEPcD5TUniOYOyDpXGKETntOBK81_TcP6fpuqLIxd-CU2xL6c_0tQUj7PIaObaijNHxcm2yrVqDEqjE7Xqiea9GOATcIsEDVrbFVD9uqf38_HtPDOutrbGdvWF9cU8N-MCuKySZ1qXyOXbTvyb5eensCPw3DYf1Fqva17R37-AL6H3s_72XulqmSehlcwvsGAStL_qV9PgueGL1jUhdre6yzxnMlFqNF-GOOArwhWi2it4BQAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
واکنش کنایه آمیز شدید باشگاه استقلال به استفاده مشابه طرح شیر در لباس رسمی پرسپولیس با ابیاتی از مولانا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103807" target="_blank">📅 17:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103806">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bdaff9e3.mp4?token=pQEYq-MvWSNzwEB3BtKf4nxarQBOlka9xRpYriVSxUlWXV0L-y2TQAtFwAqXoTFKLvJZUhi8__NZMI7N70-00dMs9WM0NJSZee5PwOBQiorjuXscJXFWxHpQHDQYwjZmc65v_A_pcP7ayRICbsZVcvbBMJi1T0AMaaal4t6qB2v1xasoC74YACFIPN-VJDEUzy_sa1QpedgJOlRcxBcvs6vLHobT1I8_gHYRlge3CTXZH7OVj78j-C1ZS877MbwSFS60Kh-0opDNsWCAjHzB2kt7i_ZJXF6xGQhQ-S-nTWdlnAVWY8XzUzjYVUhL1wTb-4MvfIuEOaYItCevPxIeXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bdaff9e3.mp4?token=pQEYq-MvWSNzwEB3BtKf4nxarQBOlka9xRpYriVSxUlWXV0L-y2TQAtFwAqXoTFKLvJZUhi8__NZMI7N70-00dMs9WM0NJSZee5PwOBQiorjuXscJXFWxHpQHDQYwjZmc65v_A_pcP7ayRICbsZVcvbBMJi1T0AMaaal4t6qB2v1xasoC74YACFIPN-VJDEUzy_sa1QpedgJOlRcxBcvs6vLHobT1I8_gHYRlge3CTXZH7OVj78j-C1ZS877MbwSFS60Kh-0opDNsWCAjHzB2kt7i_ZJXF6xGQhQ-S-nTWdlnAVWY8XzUzjYVUhL1wTb-4MvfIuEOaYItCevPxIeXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
هواداران شمس‌آذر خطاب به پرسپولیس: گلگهر سوراخه گل‌گهر سوراخه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103806" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103805">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64759a3704.mp4?token=ruaXSGfLqWxG2s3B1HrET7DBIO2Xm4wGr1QXCHFtl7mtj2m86HoAyK0C3j9iVAFj7XDca5kFH1tLhyo73ru8-c3Lt8U3RmEcDn4rhFmAEt-VS_H1iLl3Cf4kEbFVxRdKvAz-Ft1ZA1_8p_zRVgpLToNC_QqbbMxG9Hp73tgKXsYCfe9rUWdxncdPinPqeEQn5v-KvAQzDAdCMIcKqtC3TvuU8PBXa5Wjnv4yb7qiNHKUGaAkyla89fGAoXT-QPIw_o8eH77qUGJfMQAGEmL_ydE2hzW74xJx3-YBl9AGa_Xik8bKav6o39xJ7EcUi-8kgez_hBvt3zw0C5TMgniXIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64759a3704.mp4?token=ruaXSGfLqWxG2s3B1HrET7DBIO2Xm4wGr1QXCHFtl7mtj2m86HoAyK0C3j9iVAFj7XDca5kFH1tLhyo73ru8-c3Lt8U3RmEcDn4rhFmAEt-VS_H1iLl3Cf4kEbFVxRdKvAz-Ft1ZA1_8p_zRVgpLToNC_QqbbMxG9Hp73tgKXsYCfe9rUWdxncdPinPqeEQn5v-KvAQzDAdCMIcKqtC3TvuU8PBXa5Wjnv4yb7qiNHKUGaAkyla89fGAoXT-QPIw_o8eH77qUGJfMQAGEmL_ydE2hzW74xJx3-YBl9AGa_Xik8bKav6o39xJ7EcUi-8kgez_hBvt3zw0C5TMgniXIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
کنایه‌سنگین هوادار پرسپولیس به استقلالیا: جام تخیلی همش برا خودتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103805" target="_blank">📅 17:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103798">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUGdlivlYkGJ3tzQ4kBsRYyoizzfbbzeo9v688uyJP3cS-wvmDtkCLgsJtzODG4CDBKBy_wx2fGODkATNlwIWvaGkCgsETXa4DoTO4IsgqijQccprSWbHp7JQxDfwoAQ0hICi1tI7ZkQD3HmJAvnUMZKl_hxF6f4SDCXXemvVHJV41b6H76T7dlmvhL-fQeZUXZhgYdi95_UFTA3-m_Ey4NAvVP0S7c21BFBrshlPA041DU0UvHafmnVTffVZ6fz9d1ekimSLXcwtWdeViy5Fh8oAcIsr6ZWTgtgCi0PS2AfYXUweluQbiLpMNYrFLR3xyRQUW14J9vQSeX_dTs_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_EIHWWhRTe9b2itma5mjNg6Nj8G5YwM4sgN5KrtOyjW93hqV_yEtQ79vnO1sH64r9PJvmQp2aZXb24jxqnopSO02IkDEq36DYMIkYqTCT8FWnmQSvMcActEeFpglP5TuV0z2vYtI0SJ6ps2t5QQ9EJuxVXsDJUtNoChQDmH5Eh4uX5OdWUzdySz_Gyy_7za-a70k5nFHXfB1hInzzNPOgk18-daxjjZyfWCSGGHI096kCm6N-Nu3yGnMzUD5HXcQjEqEgPp5H5lqrjoBRJCx3vfKEQxZenbXpfoTPm2U2Knv-Ru0PSVXK6_sqXXF7fOCfE6RqAG6jfVX07C2wxWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSpEDRfHs0EMisObs1AI4xHzcookQM36zpGZ5zZRi40d6c_m_mFHLodL1olo792z_9EtMOuqvBOxpn4De7PwbK9QQHL_cnc8YZkFO6ZM9qO21mI9Eg5kpZlqmvWZ65sM75O0UxSkrDE4Puj35sSJty7jdIOME7JmcjrPAksdqGCAFNJE8PpJ-s7cDJRQv5ZciR5maldsSaZNOqKdAvIyGcFjbWPBubeiuVDgEyQtYTP7NZXwKbx9iR0pC4ZyGj4N-5mMJiZZjz_afPK7tGyFYLojRMO1wSwbJpovAtWQY31JQEgTrJhUHKM79pe4D6a14ksCuCll5UGmNtjmzjuVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPFmbP5351ECtf7UDcRuyBzYnMKJyCURM5ll4CEt9ATwkOXi2fLycQ3NqYcmJEnrDQquAzcB0lSKPT_Q_ZnGmRGObkPWF4AXjZq7Mb1jPMiO6b6y46EDSxX9BCEZ-yla8370wPNXu1fKSRlEC2fYzbrGmYXS_bX33jInvJhfXCU6YPWviavoV36sKJZe58HhwFIVYPD7HanBulRBnzLcVRZRTBhDZfql0w_wOqV74pf3HJjTsQVZ869vdHMT-VUuelhpBCVw64Gw7tVwvRbkvlJCEZ-_c60t5FwD_Yr4t9_GTHKxzpMZqv7jtiQGI20lNy8poxWKOO3MvHsrLL5VuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nB4pecy2AtHVwQJbIoktBisxsYc1iQ6BdNPKKmx88kmC5gm2hiKkxyVMXAlHo92-PNSd7sJ0-vOdxDGfzmrK4c5Stgt5bTP1zIEorW7koWugeHHX0E3xOmSSisQhBBGdbVhkv2g5CbI7RClsTgi5YUd3qZSoFNkcs9oSuJSQmH6r8qEaZ1UI22R54hl298Pz05iHaWlqUt7SuE-tAyLVcFWA4oHhCcVAVPSaFEwcX97YRhalCu_3XKddvSCU142gnIKQY0Cm9WWgFEEiwlJx1SUZidT1g24YsabhVOx8S2tqs0KSnj83Lk3bcjeXrUybuLXoJxj9tU58IibfPgwRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PiGPbjzpHysfuyLxhCQSLHWn2PF_9W9P3gnJwyyNJBHkekoUmUFNKbByJbBEoOI7zikyJ1Dzfit9CFpxUCSkBGejW_X3wURCykLIG6wBQox1U17xaIOHmWtK9qk0z2uzA3DKveiVK639i0Vxx1vQ7s3y-zORtAATWES8ODQOucz1qDM_fpJpcBacYgh0K1RQmuxSn_TFn3dStb01Q10B2NNQT1QppIihmXqh8A-QAQmcJ9JDBdNf5rG1IS_Uhh6q6N6dcHyanmRHfS7_6pN36-AXSVYg121nNUHAVtK8Jfk4DcPFw0guT1RPAEmj9H5J7by5bTL8dA-KG89ykwIVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNH920nGepqDnseR0KYdPqYO4xPXdh6D4VSjF4hg9aXmpmWxDEwWIUB2zVRGJ-QfJPQ4fcDZjpNnWJi38B6V9MPBnaVVcxcN6FKJFB7ZI2vDwzz0suhSKp3sHu4TtQw0nTh44sSlyWW155JsPZasb1XXXUyi5w84cqSm4R-dKp94cKdipP1CirWk09hE-oU-74iV6p4sdNERZwLw7rDzHiXrS-4Uh1W64ooJLHDy6aYJzOAOGpl48Co_QW6xqeYpbnAzwExWVYqKSUskln0Vb_N9Lls8hAEZ1hdDz1jdBmOB911iIr8Arvujo6JeelfrDGIPZ4lVtEKE1VTynXJ3bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
کار خوب و قشنگ یک هوادار بانوی استقلال پس از پایان بازی دیشب
👏🏻
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103798" target="_blank">📅 17:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103797">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935fa0a60e.mp4?token=twxTvCSD_jWuKLbc0W0kfCUYzmwHSmnySmIyRUAejiFz71A4k2OcEq7nSRx4V5wPYCnk0h1ThhQPj1AEhHa1eDw4od0O5wONRmHBT31kq8tt25vUuAxZHieLccl1JlCrAIGJyM1KWX7Vj8zKI-DXWaoncgERdU3l7ub7V3NZZKlloNK8bHVtcvpwtMbsUTLw4vvC9VbcdgmiRMQ5lxT6YdWP-URXHcFe3m2A92XmUZnQUajSZ0RotDrxKjgS7jJ40h5JnmzkK6BLQgIESbwdpxKSkNl-lRI-a2xjmDJwrQgy7iGFrk24x1rVKiK89RTllCGQYQQO5E-7rtnnCZErZbrkxuA1UZ3gKUB5KIwpza2TE3J5Jbxm-ga5wyIC5CCmOJ-R_VU1ieEW13-Vx_y1adgL6ExC1eUECe5r0PvFLk7j9SEXBVjnM3or6lNwbdC30mxgKX2dDGU4MJQ_F_2EsBA01yM6FGip8FhU0LPqNYQXnfknso61Jo9I7Rwt_7njG8-ahOl5UnDopDRTfhMhkLBZxIXsrhePI4KLiqNvORNHVpFsqqqz6GZ37ZMLhaEoKs8PgRPIiZGd-Qn403c8WniWzHV-HixcQE9rGzdlPvPFxCd8CtPMMB_EGAN7kN0m76ZlJxOJEFYhg3VgBBfFNFRkG9E_J4g4--ovA4eF_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935fa0a60e.mp4?token=twxTvCSD_jWuKLbc0W0kfCUYzmwHSmnySmIyRUAejiFz71A4k2OcEq7nSRx4V5wPYCnk0h1ThhQPj1AEhHa1eDw4od0O5wONRmHBT31kq8tt25vUuAxZHieLccl1JlCrAIGJyM1KWX7Vj8zKI-DXWaoncgERdU3l7ub7V3NZZKlloNK8bHVtcvpwtMbsUTLw4vvC9VbcdgmiRMQ5lxT6YdWP-URXHcFe3m2A92XmUZnQUajSZ0RotDrxKjgS7jJ40h5JnmzkK6BLQgIESbwdpxKSkNl-lRI-a2xjmDJwrQgy7iGFrk24x1rVKiK89RTllCGQYQQO5E-7rtnnCZErZbrkxuA1UZ3gKUB5KIwpza2TE3J5Jbxm-ga5wyIC5CCmOJ-R_VU1ieEW13-Vx_y1adgL6ExC1eUECe5r0PvFLk7j9SEXBVjnM3or6lNwbdC30mxgKX2dDGU4MJQ_F_2EsBA01yM6FGip8FhU0LPqNYQXnfknso61Jo9I7Rwt_7njG8-ahOl5UnDopDRTfhMhkLBZxIXsrhePI4KLiqNvORNHVpFsqqqz6GZ37ZMLhaEoKs8PgRPIiZGd-Qn403c8WniWzHV-HixcQE9rGzdlPvPFxCd8CtPMMB_EGAN7kN0m76ZlJxOJEFYhg3VgBBfFNFRkG9E_J4g4--ovA4eF_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
ربات مخصوص‌استادیوم بایرن‌مونیخ که در محافظت چمن نقش داره و کار مراقبت‌ رو از انسان‌ها گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103797" target="_blank">📅 16:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3l4_vmr72LPSTBtp_0wrklvGuxkti9n3KYcI0txCHvw5AiT_r_2Cg4cvJqi1cbBty2FIMt5UDobRsyQIBQyB8kBmhBSPtgaPioHeweyYsdtzAcf7T2VR0JaVjLuACSl1YorcAO2D7wDkBEbeBhjOC4OAjpfTxXj4FGd-RxIOFG68zkA4YYVKPKPwD2ykozkEEMdeR8ZIpSVzPvmbYd64JHc0L9G2JjEEWYW6AeUvOGVbJZlrmLQ6JxA9HXzZNB6lNb7tMuIlCjrFUzPaxF2n7bgDX3E1v1dfw7pnEs75kMRaQXJUoCbPsmg4IXsGwGKs7mqdTgB_R1_-yAOGf9d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103796" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqqEP2O2PxvRImeTkO8qlr6nPBDOy0sL7mMTgfrH5nqmUTydYDjkrOA73iJIco5EZGxRG9YR-cYaheXSeK_hKpxxwjkLF-e8v0F_2NvIq0w-0wY_HjMVn1HVk_f3Yz4Nsr-FVVbdilITXfwW5p4JNsZQn-ZxVZcedmQUAf0rQxsb9xrW70I39szFmsu6ETH-syfajrwcvJ15SHfxZJGQVAn_OpI_htPiWSexiNnFgG8vQv-w3ZAZFmZ_D2PXzAywI9hWxB_3JV1EpFEEx9LUWprANcb4nenM1xNhm1NSpvv3hdXG-sp-lWCryVitefNAPSzxfG2OxK2v1E0vWofFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غلامرضا محمدی سرمربی سابق تیم‌ملی کشتی آزاد هدایت تیم استقلال را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103795" target="_blank">📅 16:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103794">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVXV1AbGeOKSCWTDJxRHfA32jiswQh0TvFY53nW8pCHcHuK_nZ6KE2qdc9AUZ7FscXauLGChFEBpaSi7Of1ImO0YgLntK2b8CZvXElXZKaZRmRdgoxP_rRvn10WaecrzUIwwY8kZSE5H4n5YS-E218j-4XQNcc1Ce6Gpj_st2A9ulyP2zWQqcFBISuW6NQ6ix6LKE_7_KpOgNpYklZaDYbHxIou13lKhfT9GRUOvYqlwlMWRM6A4deLayp2qgUdwRnutYb8HUwSe_sX-z8-LCeuD64js9RCsw74Jv_Zq0jWALH0bgzS3PqK4Zb1Zw4jslA9jA4ra1agIAGbGnv9rAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
جزئیات ازدواج رونالدو و جورجینا
🔴
در صورت جدایی جورجینا ماهانه ۱۰۰ هزار یورو تا پایان عمر دریافت میکنه
🟠
مالکیت خانه رونالدو در مادرید، به ارزش تقریبی ۶ میلیون یورو نیز به جورجینا واگذار شده
🟡
جورجینا حق دخالت و ادعای حقوق در اموال رونالدو رو نداره
🔵
نقش جورجینا در تربیت فرزندان و مدیریت خانواده را به رسمیت میشناسه.
🟣
در صورت جدایی فقط اموال مشترک بین دو نفر تقسیم میشه و هیچ دارایی رونالدو حتی یک یورو هم به جورجینا نمیرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103794" target="_blank">📅 16:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103786">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTslnYryfEBesnWjgBw8y7nZ7s9BLQK5TkPuQg7hv83DKLfhB_q-oJSZTkRf9eOB62o2q7NL4AucAU_Tv_VPS-o_0c0P-eJHSF1oRo_y9BFH6SXiBejeRYIYPB-oFgPd127JfX0dTP1msDNW_Yi25pMJizx8YB_E9_4SdlIrtS-HDlfDClS8O_pbE3iby_62qvxb2rrlErz3f6blWl_n2-u70jSpFzqh28gBZuGp_-MFCH1oufFrQ-lU_BS9mxIi6w8d41mHQa9h_k74K2oaWSJHzC8bKy5c1lXzAoQ7X4YdxMGOzjbfiVOvn-MqPS8MuwMOYXZFr-5iP9B5BpN1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMCvXmH6dAJmFufzxbNvUUSMKmwH9GX8QM3axVcVVNTAn3eT3UjvvA9-e7vjsFguz4bII_Fxy8HD93XkNVTOTgtUwtAoNFc7Hwsh68tgpNvGyJeoB2SkRoCDUuBK6aJc0lSthNG6Z-75O7poN1F37FJt4kEPCszrHFCFGdh_fyb8dE63tpG9_Yg2QZzus6iP0fQVKNl79eQ-SvsG_SGrhBebNZJpGyVYJ4KK6KB3QdF903u2fxR-Oc7opJ0bXq9mHczawaxSpayxTllkB7xlyu6mbkOCpOTeeuvfKj0aaw2kIPqvRwBAXQ2ggJKnV-k2GUROmKzPErG72GT0PDfFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCnM3NzlE-D0FCtOTG7rjWHVBlFDZlu1Q1YnIlhXMNNf5nTMLFnkVqYj8sxGvemU2MDbWvX9bEegfbfTXCWhVsEec4yZvWwJK7E007_OHSxdfok5XvuePvV_CD6OkPFNeMUFFaZX2dlUZ4T3PRQVuPAppB31VuXO_KQHAWqcvPN521QZEQu51AhRIxBTAiYAGEa4ON4H9GXTjUqGdTFq6Tdmgd8ySnimVmuMDiwGbJ2cq1zcq3uqoZ-nNMSjCUezPZKxITybJhCOCrBLOJpzgjbDwfmsqiUryiRHLUKLeknXqaHamZPXcTEJAJ0hw8AwDe7cYZbNjlpnJZJU1qVLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_bhVm7_VRc5pZDd_BH-Vl5yElS4Xezm6RPgrU7wGFsGIVIc5KVZzeQVWmChPw3CF6eZkR1zSpHXbt4E0FCGuYdGl2bKITFNEbRu_QkktAw8KMDocHsOozOoPezGHD1GxQmARvV-pVD1_SFpAnBSpKFDO-O2bcVEZvnD2_TiIWafd_YSpXugChIT3LqCBFxJv-kZyf1W_7hyU5V8bXiITeEqDa4Ve9SCS4f4FMss_siS69tam4CcEtulrf0VhqU1NpPzHzUgtHBarKuWtDNuqPNrfPyP2V54ih4yM7wlaYbmxRSbXzbKoMYYocA4cIppYKwgmtu0jsWSvCLyztXyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONZvIxB_gRCGmHdrZKw72S53EonALhbO191tl_FVUGFcidh2n3Axd3vYCNPHQTDitXqiRyxhAxsE2wrw5mDTlGIev4eD5KShegLxo9Hr99hqWtjs5VfQ2fVPEI1mozbTUvxF-5Mr0SL9F9ZMwhueP7cHqaXskgsBZGpN2ayXpzHz_yn6mAVyptFDx8GqlWiXVKGEwv1kerPLrpXyhwF9n_dDTbed3LXsY8Em5Ocif5g-rGMHU5GN1U_1ueI3t8kjWn9EqczWWHwMzUl2tx3IMUyZAGUX089is-iSCDwAdNjbNOEuPmb13HGfbpD1JwuPpMdcjS848ZKp_HpuvzeyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwY-ZHKH4QQGVKdeiKiM8fA_QER299D2zgpbWUIn6RQq6uEHJB5n7G58ENsAZBVSXf5l39QRwBx0CZ7jhGXqJQ1HWaSv5k_IxMu8xgiVv-U8d6GhAJ-YOuq5pOxMaVo8z8okMExVOM9JAJeT9z6RAwVqhHnLa0Vr-9fBVt-ic3cy6EE3T3EXVKh3PqkzNY87Pkff3YGxRMS5dwu3Cmczgzod8JyHia2Xyt5quNMWFZNkkV7BN2uFRdwhsjlkntL0ERyEAnsw4NIbIP7aETaCASN1g4rqnisNRw-0umjnBwwLca7v2DswhPFpubUrIvRnM7w4bzjza-0EbI_-NjW-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GR4kJ69NxieEjOQ00BWlktNkm9k2NtS2d3qcyn61_ugPsElpjGGhwHHN8BBLvXlF449xvQBwnMmTiyZq9L_xfpEFv_TpK4SSp6rJb_7tSCJNsAuHDU6R-nVM_PBJxYhliqQZ4F7NdbLGtbh5lzWDS_4og3MVEYKJHeaKsteoMWathqg8rjT541BIWXTBr23AV4Ngoo176kL-k0y_VuSFDBNkuMz_9tfyLpjfRd4N3VFxayHK3P6WO86aRf9Jy2uOs8sd9tGC0INRtLNvKfVmihudOgF9yd9StTzESzSm5Jtm9n32peOsnCzpRLMQMOrug9rbvdFd2DtP1b80K2dBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoqIApuMkWdbu5m7LOVMOaCIVKwTFPhP5ORphUzsmxS7Nv29uMpPcZmC1EZ4ZL1x02M295NdHNDNtK5cB9t19wAyU808nng0mJ-rgi-YaodVCoIIRfAdemqiuMUP7BK7Md8feTEhPvjHkAYTkLdJ8KFRqN-B9UpYwDPIHaX8KLhDALC0Us5RDA3nwEUzr4LQf_SVpxa3Vtn8JN1r4rQt93hGFGQvK7BLPljhX3xxcBjOMngOiwWslZl-amrDC1GBj3TG-xtlKC6pqevJfrb81cUhsfXL3W3tN_Zywar-BrishuM0WocmCOD3vXAa6qG-D97vHYOAx4DIgkeZbIpsqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رامین‌رضاییان خوش اشتها
👈
😂
👈
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103786" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTv7jGqHDZvFtDos0lzJQL4j3JcVbQFI5uNk15w0F9srLCn1_p4kBV_AotrUb5sV7RFO55O1e044xQufApQcRYc77NMgPCHECNwW-crQjBUbgXO1bgoeR6s7a1vGm9KX5allM2aWawAk18Sq5Gxf8BWo7wDFaUExAkpMm-NxdatN-KspxlHtpf8cq52dmHsIavCcbF9cVv-OGCiqpDjwZJCcGZdmqtZjJgBHTs_VUM-j8DoPUvTT1WS5uPoQoOvL0VOs6PUD8iAUQGo2F0wF1aLnOiwLJYzbmgxmIx_g3FtLsOvwsSfkV3lej_LacTZX_8MS7IxD00BR3OjQl68oqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPo1QC0s9osrNh3zGRDQU8zStZPoj4pJkhnUdLxW6aAsbJi2SwttTSvSlm5iLTnL1nMH7sqz9JQpvg03xFlFX8guBaxPJ1wzpMASV2dPXjJe_UF0YA9ahrZbeVqUFWucGvDH5jMI4m1r_JgIRHBB-uOJfJZQYCbS-wNenCMI65-qmAkhmms3oh7V3P-TAKGl8tS-NCTAqar94hO0gxgU6pLgbhVjtpBvlQ_AtqMJ_KvWybJ-dZWAiX9Vbg8lBJODEGz5sLf_3zM7bwIPrHh6VtalPKSWjq8AKVgI_BwNGzkdXUvEy-SQF3zveaiDJ7WHDvi8ObXwnXB1mz5cjHvbHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
یه مدل ایرانی - آمریکایی به اسم جول فرشاد مدعی شده که رامین‌رضاییان تو ایام اخیر بهش دایرکت داده و خواستار بزن و بکوب باهم و سکس شدن. قراره بزودی اسناد این اتفاقات رو منتشر کنه
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103784" target="_blank">📅 16:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmLulLXIdAjbm3s0xsXZ0HjxAqFBMY03b_hR8nTB5xZAXcxEN5RozjK196UqWs4gub_nrgH-NBrxOPMDQtyr6UFhAp1N1bXMrCi5aeEP2MFXUXqg0HTardCSpQHptRixVzfI244StLu_LXdTYGMioymDYdutycfg8ckZ70u6YGaFbEUSaf2ddYUZ7fbHW_dDHxmDij60MlGQOKB-3E6l4m4LgloN2EiQTInYMK6wJUNu-E9gqeXyuhCwz7bBtyKLl-7v364SATlKGyjtE9oa-YbG_e1imPO6bM81EI9Begmz-2gQKVWBkPy3_59_pauiOAo32_23M3oOuYgNzQRDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
عکس جالب و تماشایی از تمرین تیم فوتبال خاتون بم، تنها نماینده بانوان ایران در آسیا
🗓
برنامه دیدارهای خاتون:
📌
خاتون ایران – زسکا تاجیکستان؛ دوشنبه ۲۶ مرداد ساعت ۱۸:۳۰
📌
النصر عربستان – خاتون ایران؛ پنج‌شنبه ۲۹ مرداد ساعت ۱۵:۳۰
📌
خاتون ایران – اتحاد اردن؛ یکشنبه ۱ شهریور، ساعت  یکشنبه ۱ شهریور ساعت ۱۵:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103783" target="_blank">📅 16:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnMG5SRn3CNrL8HXuPqVhGGgYv5i3Q-qZA25Afqvtpu4Y0oZb7EyYEBbUqktR_K5x1bs_6wQpSYSIsuEndoWr0XLNPwPJNfp8Ku2pZUYpLLpWjb5_dpRaU3OxcUkTNMGBsNqTlY9vQFLr-DkDXUnX6aSBZXdjtCRQUBu53Rvtb1zQmFanj9lT36GgWmZLEHw4VJIOfUEtxkOZHqioFNNpVTep8_r6s98A-wuNCfQygsFbRYMFftEUhbXzVVNHbnCADu47TQmn_i_JVOF81XinipgN9qtxi7ozLPqAGFPHGEwXNA6x6GPmNLHufuvjNl07FcaqQeNkiYOKAfigXb8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
واکنش کنایه آمیز شدید باشگاه
استقلال
به استفاده مشابه طرح شیر در لباس رسمی
پرسپولیس
با ابیاتی از
مولانا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103782" target="_blank">📅 16:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd007f5dd5.mp4?token=UyCkAMxww8HD1kESkz9hjRJt6RISt3a92QKUr8a_Rw6NXdFfdV_ZUAlX0D6JPqEbItb7UhKqTnSFuNNip5sU-OfXLWwYjES4Vak7y32QtLIlvSd3Wctgm4iUG0WUVb5LcvwfKXsoNC3EaQo4m7FaDOcMGaJDwwB567dDcwTt6zBE127U9siIUh_WFAzvGELCJxgPqP1gUG49ISVPvgItSk-onDDgp79oIzAWhtuCbqqPr_RlA498yLGDDfp_Gn1-BKIQXvQJzgnmpwmmRPdw0cmU8ojfrcAB64Xl5DUn1WBCJvdrPysxW54Go1khCgpAjUOlByBnukIw96xFgLPMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd007f5dd5.mp4?token=UyCkAMxww8HD1kESkz9hjRJt6RISt3a92QKUr8a_Rw6NXdFfdV_ZUAlX0D6JPqEbItb7UhKqTnSFuNNip5sU-OfXLWwYjES4Vak7y32QtLIlvSd3Wctgm4iUG0WUVb5LcvwfKXsoNC3EaQo4m7FaDOcMGaJDwwB567dDcwTt6zBE127U9siIUh_WFAzvGELCJxgPqP1gUG49ISVPvgItSk-onDDgp79oIzAWhtuCbqqPr_RlA498yLGDDfp_Gn1-BKIQXvQJzgnmpwmmRPdw0cmU8ojfrcAB64Xl5DUn1WBCJvdrPysxW54Go1khCgpAjUOlByBnukIw96xFgLPMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های‌جنجالی محمود فکری در حمایت از رامین‌رضاییان: قسم کیلویی چند؟ رامین خوب کاری می‌کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103781" target="_blank">📅 16:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb73e86aa6.mp4?token=T4qwTz5lUspVnwzP_c-5WPnIqx-11nqvbuwzZKGCOo79a6FhyHFyNAnl0A54QDJWbl0T1UiWC2uokApRHc6UjtPNPB_Azpamq91f-7dhTX75ohRtkguPUPxJLC8WXJl3HeMZPTvB6BWS18HLMWM3j2UpYesOWmFHzmbQ3vzbmGRhsvvEhDdmrn78GaS1samavFjDtBq7zjmX9wXmOb9TormcwYkxmhxrGKOlczbVwZDOBwH0S1dsXP0haaIr5RhAUSz-sc106ORlqNHx109AU-BxpWoZVrFQPo9z7sGvZTb9BCycMd49ctkMqwxRXv2wH3MAakQ88PZk8rxjlsY1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb73e86aa6.mp4?token=T4qwTz5lUspVnwzP_c-5WPnIqx-11nqvbuwzZKGCOo79a6FhyHFyNAnl0A54QDJWbl0T1UiWC2uokApRHc6UjtPNPB_Azpamq91f-7dhTX75ohRtkguPUPxJLC8WXJl3HeMZPTvB6BWS18HLMWM3j2UpYesOWmFHzmbQ3vzbmGRhsvvEhDdmrn78GaS1samavFjDtBq7zjmX9wXmOb9TormcwYkxmhxrGKOlczbVwZDOBwH0S1dsXP0haaIr5RhAUSz-sc106ORlqNHx109AU-BxpWoZVrFQPo9z7sGvZTb9BCycMd49ctkMqwxRXv2wH3MAakQ88PZk8rxjlsY1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
⚠️
صداوسیما همینجوری داغون و بی‌کیفیت هست حالا ببینید چقدر اوضاع وخیم شده که برنامه فوتبال‌برتر رو چجوری از محمدرضا احمدی از مجریان وفادار خودشون گرفتن و این مجری جدید رو آوردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103780" target="_blank">📅 15:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎙
▶️
روایت‌شنیدنی همسر طالب‌ریکانی از چگونگی آشنایی با این ستاره محبوب فوتبال آبادان
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103779" target="_blank">📅 15:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66527a14da.mp4?token=GPiFY4eQt2YBaNK1ZF2sOVJEPsLUPLbwfYHzbcu2XJ9Mc8_xjpw0Q_EqauDOq7BrHEf5rJhgFbdkdXaH7fyX23aG6PaDo1m5NqvskR_suJYeIPmbs5OmqsGG1hJiOrkLvW9e-6ToChkdpZdn6uxcpQLhEILIc1J0zgN1QhJm67qqtR8Tog1Qf-CFZLL0twK69a4PYHPw7r14kRsO8vtHBUQr8bvdqhIUocigPlL_x-ETnATsyc2Ig5jB3bdPk1_lxkI-hJbyRzPRBJ2IsY7TRQf2T9djQr-abV_OnQEEwzvjW4xyZcGsXGarpPBg_FPv8T8txtx1BLVAjy8gd9gR56PwBSJOSCChgrJzcjJLOEPUHsW1JJawjsiK1RBrAfBYB2ykvP0e6IUIgJiY6DqBak73EPRjzZb2hCu2cPtOviYHLh4kPU930ilq2v31-hwViCIAGyEc0XXEa9E3VfqDJNEAKmiFD_rpyfxLoR-R-QX1WYHqLCmZs1Tu9ovZnfQ0BJdvOVVnKUV858IHEEKkWGBwFS1QTZ7F0m3MYeHWdz2NkvoCmmhJfpEZGNP58jnW9yvMduU2_SwoYpf1IHhCtBvWhC5Bvj8ZPDsn1ZeQ-d0P7vO84E5-2nI6yvu9XpedLx0pUg-8CNGZgeTkc_42Opury8adK0QEhJ_gRLoILks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66527a14da.mp4?token=GPiFY4eQt2YBaNK1ZF2sOVJEPsLUPLbwfYHzbcu2XJ9Mc8_xjpw0Q_EqauDOq7BrHEf5rJhgFbdkdXaH7fyX23aG6PaDo1m5NqvskR_suJYeIPmbs5OmqsGG1hJiOrkLvW9e-6ToChkdpZdn6uxcpQLhEILIc1J0zgN1QhJm67qqtR8Tog1Qf-CFZLL0twK69a4PYHPw7r14kRsO8vtHBUQr8bvdqhIUocigPlL_x-ETnATsyc2Ig5jB3bdPk1_lxkI-hJbyRzPRBJ2IsY7TRQf2T9djQr-abV_OnQEEwzvjW4xyZcGsXGarpPBg_FPv8T8txtx1BLVAjy8gd9gR56PwBSJOSCChgrJzcjJLOEPUHsW1JJawjsiK1RBrAfBYB2ykvP0e6IUIgJiY6DqBak73EPRjzZb2hCu2cPtOviYHLh4kPU930ilq2v31-hwViCIAGyEc0XXEa9E3VfqDJNEAKmiFD_rpyfxLoR-R-QX1WYHqLCmZs1Tu9ovZnfQ0BJdvOVVnKUV858IHEEKkWGBwFS1QTZ7F0m3MYeHWdz2NkvoCmmhJfpEZGNP58jnW9yvMduU2_SwoYpf1IHhCtBvWhC5Bvj8ZPDsn1ZeQ-d0P7vO84E5-2nI6yvu9XpedLx0pUg-8CNGZgeTkc_42Opury8adK0QEhJ_gRLoILks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
اگه نمیدونی برای برنامه‌هایی که داری از کدوم هوش‌مصنوعی استفاده‌کنی، این ویدیو کامل و دقیق بهت بهترین نرم‌افزارها رو معرفی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103778" target="_blank">📅 15:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0514e98c89.mp4?token=EotgUTCJGoV24tFHxwhweYNzfZj-GJuubXu5_o0vPKRv8tvbRUr1WMxA-hRxH06pnMnmPacQ5HWh-MuMwbrKV1irjaCxVZlZatmspNtIflXngDYLx5CamKk1bbNtgj9sOI00tbOXkI8cZ5gzjk480LcjBF4xOIYk1Hg8RVv2qhsqx2r9j9iFMTyTzi_uAzy2RjFmAJn91MMzp9S1yNWyWmoDDeWBfxYoVfb2zS5UmvVNA3M401ClWpsdtssRcb75H8ztZStwUS2AleLVbGdxsX-8f5CsaMc-tzVMZ5_vUxze6fAUKgjPnUyr3BgxoUe52uJeieENH_CFFuKMi7oORA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0514e98c89.mp4?token=EotgUTCJGoV24tFHxwhweYNzfZj-GJuubXu5_o0vPKRv8tvbRUr1WMxA-hRxH06pnMnmPacQ5HWh-MuMwbrKV1irjaCxVZlZatmspNtIflXngDYLx5CamKk1bbNtgj9sOI00tbOXkI8cZ5gzjk480LcjBF4xOIYk1Hg8RVv2qhsqx2r9j9iFMTyTzi_uAzy2RjFmAJn91MMzp9S1yNWyWmoDDeWBfxYoVfb2zS5UmvVNA3M401ClWpsdtssRcb75H8ztZStwUS2AleLVbGdxsX-8f5CsaMc-tzVMZ5_vUxze6fAUKgjPnUyr3BgxoUe52uJeieENH_CFFuKMi7oORA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خداداد عزیزی خطاب به خبرنگار تبریزی: گمشو دیگه توام. هرجا هستم سر و کلت پیدا میشه
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103777" target="_blank">📅 14:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afefed3993.mp4?token=LoHw9gfvQHnCmKXiHXFkbMoKpUt7ayXPrxjHB0DALEmz_46e1wyPOUXkSVYVL3mfPo7Az751THoflNy5OUKK36y3_zjqYcmNa_HfNBryMTUE2tSxknF8n0mrPOtju-9c_m7g_c-KAzZXkovGAszYboYZfLyEJ4UqoaW40pnQENOYUkHH0GTJMloCaIFVAgRNhBWtK6GcJZtychONMS3ZiApxLxPluDX2z2j8GEF69GmWwfk1W08pPrFhHDlwno40_9e4LrkPxtC6ZJ1sH6OX4IMbyaF6Y0-_p1WHYjOLWu8A-QH26v_Vvh0_9vxOKC5D0pkrkVeN5QQ0ouqJty9KBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afefed3993.mp4?token=LoHw9gfvQHnCmKXiHXFkbMoKpUt7ayXPrxjHB0DALEmz_46e1wyPOUXkSVYVL3mfPo7Az751THoflNy5OUKK36y3_zjqYcmNa_HfNBryMTUE2tSxknF8n0mrPOtju-9c_m7g_c-KAzZXkovGAszYboYZfLyEJ4UqoaW40pnQENOYUkHH0GTJMloCaIFVAgRNhBWtK6GcJZtychONMS3ZiApxLxPluDX2z2j8GEF69GmWwfk1W08pPrFhHDlwno40_9e4LrkPxtC6ZJ1sH6OX4IMbyaF6Y0-_p1WHYjOLWu8A-QH26v_Vvh0_9vxOKC5D0pkrkVeN5QQ0ouqJty9KBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
🇮🇷
بررسی عملکرد شب گذشته سعید سحرخیزان برای استقلال مقابل مس شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103776" target="_blank">📅 14:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBwiiZqSeCiaHq_7AJqxcYVYZtSknRPtkU-3J6I6WWly0urx-U6vfCxdPTI95nnUhY7sTht-wU3ca2gGaw4XeKHEVfdW-lxn1VcMoEuiv4MH0jaCCvJxIBaXuQT8GePRHL1NxQo9JLtX5B00omtfHFFLKN3vrh8-Hd9zwWvwJ4qkYdqGSBpXZYmXZfXx2If4xKRyGPR4UzyrQXIfpQX2WNVUuSLB83MF_wHDt-na9fsCZQsXS8xqn7GoHzluH9Ka1uYI97SAmnh2Bm8DiRHJiKpmgSOnQqFUqL506EaeV3qbdO42mwIk7ULZ5AlzszO4ETi5p73XGtcDh-cig0LcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین هزینه نقل‌وانتقالات یک‌دهه اخیر اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103775" target="_blank">📅 14:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e4a9c065.mp4?token=sg38Td99-vzuJYFpqLy4lXLgy4dSYydIbtWTMKwCD9zszzJDM0pcDZFW920VEYG9luhnubSyQ2G_XzXdYKAIe_XJ1a1-7F0SY13kWnvvC7bxPkPY-raNOfT39QDD1BstSxO0naRNimgWlRHlxT3y0npAuYCb7sJJ8LrtUutvfDULqbb0XZqVwBeuu-krAo4xum-xH5Lt7KApGjnTpEAovZDcp-wwwCykAE8GgfeMlA9LmTCp40nPCX-vDYdI2Bt4zReZKTiBCnTLzpZT_-qihjRKzrn2LIUmFPkWLOucMadW4vuIYrP3ffq453IqC0tCNPw5H9UFgiP2IJqgiYArqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e4a9c065.mp4?token=sg38Td99-vzuJYFpqLy4lXLgy4dSYydIbtWTMKwCD9zszzJDM0pcDZFW920VEYG9luhnubSyQ2G_XzXdYKAIe_XJ1a1-7F0SY13kWnvvC7bxPkPY-raNOfT39QDD1BstSxO0naRNimgWlRHlxT3y0npAuYCb7sJJ8LrtUutvfDULqbb0XZqVwBeuu-krAo4xum-xH5Lt7KApGjnTpEAovZDcp-wwwCykAE8GgfeMlA9LmTCp40nPCX-vDYdI2Bt4zReZKTiBCnTLzpZT_-qihjRKzrn2LIUmFPkWLOucMadW4vuIYrP3ffq453IqC0tCNPw5H9UFgiP2IJqgiYArqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
بررسی قدمت مسابقات تاریخی و قدیمی فوتبال انگلیس یا همون FA CUP
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103774" target="_blank">📅 13:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89232eaaf.mp4?token=l9o5F5OZrdKRZgX4DWDU0i5D8XUocrFpSN-McNsHwXJK2nSFkYhawnjRfvqBlbT7Bj85XS9iRSSX9BFgz4xKJEnBLg46YhKFt_dXczPqmYNPbgoVdoFA4mwmDTrmlBsHvghFotm55B_z5UIYmZovagp-2i9rEgKIY_DCMWw_Ce5TAjQkTYdeAOLCJ2SImoPbpb3hl2CRBlMEYVVLjLhA9w5lom_wXoyqAhVrBhy4MhsPUzZMxl1s9fr1Do--SSwRC1J-9-gwusViL_qGYPYbby0UW8levH1Gti61RUPVPxLQHvLg8CsAt1ouyeWuRgipGxGj6c4_u9scQ3XDKMSclQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89232eaaf.mp4?token=l9o5F5OZrdKRZgX4DWDU0i5D8XUocrFpSN-McNsHwXJK2nSFkYhawnjRfvqBlbT7Bj85XS9iRSSX9BFgz4xKJEnBLg46YhKFt_dXczPqmYNPbgoVdoFA4mwmDTrmlBsHvghFotm55B_z5UIYmZovagp-2i9rEgKIY_DCMWw_Ce5TAjQkTYdeAOLCJ2SImoPbpb3hl2CRBlMEYVVLjLhA9w5lom_wXoyqAhVrBhy4MhsPUzZMxl1s9fr1Do--SSwRC1J-9-gwusViL_qGYPYbby0UW8levH1Gti61RUPVPxLQHvLg8CsAt1ouyeWuRgipGxGj6c4_u9scQ3XDKMSclQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین تلاش های لاپورتا برای جذب خولیان آلوارز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103773" target="_blank">📅 13:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYsR-2J3LLXSWZjwhGw5CBFaPMRBxABsleq4Bufow0enXYFMO_uvu5ia5eyulyoDVZ2E2DIFanEn0xx3Ux8_TAJMb5vI8AsyAoP_kU6BS7CwbO0X4R1OAqrchjCr4ltRuQGvCfrGia8ZaQJzm-9PdUF0BfuH-tZRB84EF_a2jw2H2Rr6cF1v4heI5yZ7eZDYP8iItQFv0pmMXaSNTEfFtMrBrzDMZQndvh3-gyR_03bkgYATEzpqItTK-uN9Yy5LRi17xytnhhjJ6eoXReVgDqp43sm3lSzAT0Vv2PY6LOlTT8l40NyJ3C2Zt7HQ2cP4oHp6KHcflZ2-DdrGkKQrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جرارد رومرو: مطمئن باشید تا روز دوشنبه رودری بازیکن بارسا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103772" target="_blank">📅 13:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇫🇷
#رسمیییییی؛ پاری‌سن‌ژرمن از عقد قرارداد با فران تورس تا سال ۲۰۳۱ به مبلغ ۵۰ میلیون خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103771" target="_blank">📅 12:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWsGAzunRKhnQxGJgIiuiBSyItBjHGxUfYoVZS7fMb9T8EtssU0CUQhYYMPzttQR5oL2s7JtvMTb_CxAdDS1m3Xmd69ynlkh0C74i0MfrsfV_Ybtc4BzqeNL4caR3xhFZ5wecqY0Mla1KvfffXsuA6viI1PiaAPNWBJCk3RKHFMFr8ND8nsNToyYL1j2bIuqxGhqHmJqxu-MvGvL9EqBryMg6CG0cz42VAogPfkMjuh5-jh4_g-MaY75EgDPt57n1potgEryeZZltxdK9RhPxBi170vBLR_E5Eyo6sV3aGC1zl289y8EUGO-eSUlZ78_TnR0ECIMfhmrUW4Rswy3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#رسمیییییی
؛ پاری‌سن‌ژرمن از عقد قرارداد با فران تورس تا سال ۲۰۳۱ به مبلغ ۵۰ میلیون خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103770" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=Lau8rKbRTXHCwDKsSB8K1UxhCMPnBS-hEQnZhXiLLThgItPFMag-E7w7sgjSlT6gTruZ98_HlC1tCNlyDNoQ4ZFA60gA6523NHmv5LIzMgjsQj8I7HJwF4Zl_RtTXCE7gCtErJAjrZ3yoYk8CKL71ccX0N2rmlSlYWUeoUG285lJgNl2pqUzYxwTo3xbvIVvPSwcJHB_7gb1odnzfbTiwsAMtQahXuDMTetSfR74zC87K0cNvfvN7nULzwqODP_0oH9X_lERo59yKU3lbskBRcQf_UYK3JBlFwauZ1jP7W1Bn9esTlnyhEdPDs19fuabeZiySTPq-_p79Mb2NOTVzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=Lau8rKbRTXHCwDKsSB8K1UxhCMPnBS-hEQnZhXiLLThgItPFMag-E7w7sgjSlT6gTruZ98_HlC1tCNlyDNoQ4ZFA60gA6523NHmv5LIzMgjsQj8I7HJwF4Zl_RtTXCE7gCtErJAjrZ3yoYk8CKL71ccX0N2rmlSlYWUeoUG285lJgNl2pqUzYxwTo3xbvIVvPSwcJHB_7gb1odnzfbTiwsAMtQahXuDMTetSfR74zC87K0cNvfvN7nULzwqODP_0oH9X_lERo59yKU3lbskBRcQf_UYK3JBlFwauZ1jP7W1Bn9esTlnyhEdPDs19fuabeZiySTPq-_p79Mb2NOTVzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
:
🔴
۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یه نوزاد شیر خواره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103769" target="_blank">📅 12:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBlcpqmk92aoBpeCnIGIo8j3LXtYT6AVWxih7xTonmgIkAdSkNT0Osub0qg-qjEQRn_M9vjvB3NH66pi5kSi0Fgg7VWxty2wi3y1D7AL7GHiH3d4skjWtICVq7h8lz1lIuZkgngtunxQfXN_tuJ31ipo6Aw8BRQtvUigm_q2um8r5ataKUubKsHkS7HmgphpJqRcdKh0eXGY2U8jRNGzFd6PWxBlEubL3cFq5X8IxqfRBEzodqQOds2FmTXZwAC4WgQZLxodWkaRYlCVa4C38cKmx7WV7kAS6NprUkSpH5ykYtMmll49ZLKGZO0u8Clmf-T4BI7eilseJ-IS6esajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار دیدار استقلال و مس شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103768" target="_blank">📅 12:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103767">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d46239908.mp4?token=cfiujMEwWeHvKs80kBEtTdeH4ZlomY0-aWKpxk0rWjPjcK-veZ__YoJkPOsOSbVLZ9cjTk7akz3jQM6JZQlg9e4-6TLByZEPC6knFxiF7RF0aZUHnDAtHhGcs0a0JcwOb7aBq4HSN3O2bhmFsNz-n_oM0EW2nQhzpsym-GS3EOqNHYU1ZMDWOZxTH1ja-gNC3i0t47Nk4n14tVnesrGwiakmfm8X9Q6Q9hgzBvZu4NcxMOjT5iiLAKwKiQMQ-cKF1xLIdTinpnVnkRVCoSUPPKLguF4jz8VT6D4XKHf-75U346FVeXZLE34uqlAca6oAdHlQE96QhGAAFNJZ7JAkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d46239908.mp4?token=cfiujMEwWeHvKs80kBEtTdeH4ZlomY0-aWKpxk0rWjPjcK-veZ__YoJkPOsOSbVLZ9cjTk7akz3jQM6JZQlg9e4-6TLByZEPC6knFxiF7RF0aZUHnDAtHhGcs0a0JcwOb7aBq4HSN3O2bhmFsNz-n_oM0EW2nQhzpsym-GS3EOqNHYU1ZMDWOZxTH1ja-gNC3i0t47Nk4n14tVnesrGwiakmfm8X9Q6Q9hgzBvZu4NcxMOjT5iiLAKwKiQMQ-cKF1xLIdTinpnVnkRVCoSUPPKLguF4jz8VT6D4XKHf-75U346FVeXZLE34uqlAca6oAdHlQE96QhGAAFNJZ7JAkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال کنید کار کنید کار کنید حال کنید ورژن جواد خیابانی و محمدحسین میثاقی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103767" target="_blank">📅 11:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103766">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1z9BpRCYY28ZL7IPabXl_VUSxOm_CF1iaJxex-LM5tep8XhFOG2-m9EpiBAFGeYJCnQJl8Gjaerded0A61554pQ9HiRJ1COTC-W_S7zITG9a1AnDWtvDBnMD93Lk0IEhVzhSvzsSI9lLV9K1foXUflPjFMrOQ_CjxZZbiMc1bLsq4gjaww7m4Eua7IZ_y-6wa6s-3oWLh8HXNp7tSFQJ4UrcgkKcHzeUU92JZ0mCVsykvZ30nKE1rVQxGkjrAk1dt1Kdzi2fXC1vgllgOiXE7u0cz4GGc7U-_A-NaRVwFJPLNu1a4R1CRPbEhpgRQFEfSEC5u-S1A2RNLVlm7uqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از ساشا تاولیری: الهلال با پدرو نتو بر سر شرایط شخصی به توافق رسیده.
🔵
چلسی حالا برای فروش وینگر پرتغالی آماده است و خواهان حدود 60 میلیون یوروئه. الهلال نسبت به رسیدن به توافق کامل با چلسی اطمینان داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103766" target="_blank">📅 11:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103765">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g-DqRNXc7Yb0BkQh13-5VtB-pPSA_kl9JDyJNq5BkX2xIH9SnUQHNrNje48eJ7E9r5Lm8SdKfvFwme_A98w9cw9x0ZmeBDgv6PTs8Ip5kwaNDcyrg6wOtfm-6_u0LVztqDOxZgyjK8GGSLs41FyJzEMakv07bXiUr83r0N_p3Ha7HZ9BTP0Lh0wUFXmjhnBk_WXl4s9NfQhl0Crpu7KeBZNPRzV7uTX0tEKg6j4oOgEf3sQ1jyzJIZVmIotMhBlNpwczYyA78tzufFLvjbMI3DXnSmsjPT0vf62T1Ugx_At2rfGk5hLsdHnyPN4huXwJz7tOx88PxxGkqFAqj2K4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز: بارسلونا سومین پیشنهاد خودش به منچسترسیتی رو برای جذب رودری ارائه داد و بنظر این پیشنهاد مورد موافقت قرار میگیره
🔴
پیشنهاد جدید بارسلونا به رقم بالای ۷۰ میلیون پوند میرسه که به خواسته سیتی بسیار نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103765" target="_blank">📅 11:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103764">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxU3Za4v9jL23NMWH-BDpSW13fra7zbZqptqKmdlRW-q5ynbT6DJEUrEcECPOSXdDe5jSmRBHK_hrfvooB0IxujskQ3CMSqBHrL_lnZmqvhSniAG9Afd3LDeFCX7GBc7fIr3mHV8PuqMpdgbPFNDmiA1kHYmiHNyU_XynJEkwKEuAsFWJ_pn6nUHYiSwMWrcPD45Z7RzN-BU7sQGMpCdKO_hNJt2aRUrgwYtzfP2xOisosJwdQGBK8PR6WbTJguoEmzRS87JEXjHfZSqx3DaJ1935-fa5fXpZM3JW7pDUDJc_y1u40Q2doa4YSKU9jvyJTMQzrESKbuxufrKC5102Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
مهدی‌ترابی بدلیل مصدومیت در بازی دیروز مقابل پیکان، حداقل ده روز غایبه و بازی مقابل پرسپولیس رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103764" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103763">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8788296ec7.mp4?token=D1KnAT_LXRrzv11-0E9cHL_Dn3IeccUBP6F837VxxHK27-g5nR_yxfMUVUZLQEuCDIgdgkiYlQzQlETkCFCgadlQZerOeYLhATIZ5EXjAYltqzleIRYlDDHX4fOBJKOk-I4gh0AlOu3lr2wiLUzt3SQye1YQhuciYO8YjemkWea6A4WVbG5qWfIAHQ982z2RaF7CvXCkyObrHLvaBResTivD4MSqh4Pnh6sKXWRz0bIRsKcETmNE0Pdk8FdVBwov7YAqBOjLaTFeFf2BSUz7I6QZ7w2AJFIqDoKbfmc1q_nWHJejNHEMAKYS7Kl_0G_3UQO1KhGHSCidPtyJt8y5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8788296ec7.mp4?token=D1KnAT_LXRrzv11-0E9cHL_Dn3IeccUBP6F837VxxHK27-g5nR_yxfMUVUZLQEuCDIgdgkiYlQzQlETkCFCgadlQZerOeYLhATIZ5EXjAYltqzleIRYlDDHX4fOBJKOk-I4gh0AlOu3lr2wiLUzt3SQye1YQhuciYO8YjemkWea6A4WVbG5qWfIAHQ982z2RaF7CvXCkyObrHLvaBResTivD4MSqh4Pnh6sKXWRz0bIRsKcETmNE0Pdk8FdVBwov7YAqBOjLaTFeFf2BSUz7I6QZ7w2AJFIqDoKbfmc1q_nWHJejNHEMAKYS7Kl_0G_3UQO1KhGHSCidPtyJt8y5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇮🇷
🇮🇷
سیرک لیگ ایران قسمت جدید؛ بعد بازی دیشب نگهبان ورزشگاه شهرقدس در ورزشگاه رو بسته بود و مانع خروج استقلالی‌ها و مسی‌ها از ورزشگاه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103763" target="_blank">📅 11:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103762">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279e38cd4f.mp4?token=CQruVqdvn_DVfLm2_xssXlImfAXdTfsYA03VJgCzzBsnxBCfUIJneR8QF6aMr3ECFOP90JuQYUag_-vIYGQl1b-kJN6s_lm5f6NkD691Sv4xnbURuI1q-4OgFkPNS34RC4DMY2Janiy36FGRGe59bGAJPZ5shUEZqlDXQhulfPcqGuXd_4DxURQTrMbcWLMJXBMl6gk34lg64d-iCkw-R-HCjf80vB3dQLQMmmY2bxyT19OQ-hTFqwJd02seLCtkxFZgVWx8TOxaCHcY9ZqH_ZGX_xPup6bNcJLG6EfW6Ai5UtcT3QSKu-XNKCxJ_1JpM0fT7zKqDkQgsdCkUfjEqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279e38cd4f.mp4?token=CQruVqdvn_DVfLm2_xssXlImfAXdTfsYA03VJgCzzBsnxBCfUIJneR8QF6aMr3ECFOP90JuQYUag_-vIYGQl1b-kJN6s_lm5f6NkD691Sv4xnbURuI1q-4OgFkPNS34RC4DMY2Janiy36FGRGe59bGAJPZ5shUEZqlDXQhulfPcqGuXd_4DxURQTrMbcWLMJXBMl6gk34lg64d-iCkw-R-HCjf80vB3dQLQMmmY2bxyT19OQ-hTFqwJd02seLCtkxFZgVWx8TOxaCHcY9ZqH_ZGX_xPup6bNcJLG6EfW6Ai5UtcT3QSKu-XNKCxJ_1JpM0fT7zKqDkQgsdCkUfjEqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بهزاد داداش زاده بازیکن اسبق پرسپولیس: اصلا امکان ندارد آسانی و اژدهاکش بخواهند غیرقانونی برای استقلال و پرسپولیس بازی کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103762" target="_blank">📅 11:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103761">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAAQkyaRYgLmrP8OIKYJSw5ZDo1c5C4_dCdbXsEJJiDgV6-MtO-Re_nr_MNMddaovZgRyxQY8RHxEIiNzSlSb-uqtv5oAG0AmLRWz26pxkpP6Glf9frpF-H4F11IhcYcpeDs0hDefYe8ganBKp0G0ibx_nnlm3VXJgH5PFelKK6UIXi2Xhg_awmQOubnwqf9OF1Xh6M3H2aSl_MrxKSTGle2eK0Lkp4n0UbcYPg72r6UzDSquuy7jX7Wtf2pJ8CcVPhAHODERJU8FYYYDBFCWbeQcwAjO1y0oN4M09FeXDZ57GXPtnpRr_H808gopMtCmNN_LmfA04kmnwybkWCeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-میخواستی بهترین بازیکن باشی؟
زیدان: همیشه دوست داشتم بهترین باشم و براش تلاش کردم. ولی بهترین نبودم یا حتی جزو ۵ نفر برتر هم نبودم، شاید یکی از ۲۰ نفر برتر باشم.
-پس برترین‌ها ازنظر تو چه کسانی هستند؟
زیدان:مارادونا،پله، کرایف، دی استفانو، پلاتینی،مسی، دو رونالدو و فرانچسکولی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103761" target="_blank">📅 11:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103760">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6e913cbee.mp4?token=hh1w4QPLK9iPZeEO9m9TVZ76RQqJL8sX7cS7a31EIqraUGQqEX2YXUiupG2FPw3byv5sLycRpuHpZMVI4vKkquJmnBDt1_txj5WM0I5EK_ZdH2-ghD28lO9zv_lLU0fyMGb3Qz6zTCjLk72xDq4tSfLkPa-qom4zJpAfxTaguovqx7A7iy1FvoYgiVdTi-HKaFiEkK5k7Db0VdAIeq_9HO5akoLgW6yOJRbD8Hg4TRutM4SFLd8vy-KJEjZMyJcCPf04jF2WQs4wr0K33gB2pD2oxbsEkWw9TIq8Iyp2oJbBrmqtlgWYJKAFV3-0q02dh8P1WR-ou7ZcyYIIPfgj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6e913cbee.mp4?token=hh1w4QPLK9iPZeEO9m9TVZ76RQqJL8sX7cS7a31EIqraUGQqEX2YXUiupG2FPw3byv5sLycRpuHpZMVI4vKkquJmnBDt1_txj5WM0I5EK_ZdH2-ghD28lO9zv_lLU0fyMGb3Qz6zTCjLk72xDq4tSfLkPa-qom4zJpAfxTaguovqx7A7iy1FvoYgiVdTi-HKaFiEkK5k7Db0VdAIeq_9HO5akoLgW6yOJRbD8Hg4TRutM4SFLd8vy-KJEjZMyJcCPf04jF2WQs4wr0K33gB2pD2oxbsEkWw9TIq8Iyp2oJbBrmqtlgWYJKAFV3-0q02dh8P1WR-ou7ZcyYIIPfgj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
باختر، کارشناس حقوقی فوتبال: تا زمان باز شدن پنجره و پایان محرومیت نقل‌وانتقالاتی، باشگاه استقلال حتی بازیکن آزاد هم نمی‌تواند جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103760" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103759">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103759" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103758">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqQ28FB6hZfrorinGQjuTAB3vs5Z9MVOJi6gc6DhGilhcs2mBoaehJVRwrEIKOglYXRzYdsJEQtgbKmIJt0ZVa6YcnNvvId_sI31szUqeIQ5b2SO4D8RBhz2zQSOqRtkxjOaf6gRa9sTgijkwrd0XIeimVzli0fi_gafiPca4slybZnyGLiOan5RW6-YMrRb_LQywFhO_1QxULCn2gCnjskFbpyq2RUDyzRcGeqAK9_ezXMr4_XKNhziMUXancbBXfMA9ydTvGAT-9O7PxPk9y1uo4BcwgXdMcDa4DKmXOiTn38iUGqblnCF-v63zcsP_cUFAQ5blhGdo1SxNbY-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r24
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103758" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103757">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⏸
🇪🇸
موزه جذاب و رویایی رئال‌مادرید که یک‌ایرانی ازش ویدیو گرفته و توضیحات جالبی داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103757" target="_blank">📅 10:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103756">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQeXiLZoCFNgbzM2WXJxZZXo5bZynGPDIKLn7LDaszkJnimUWbzFLcMRCOkKNSkPkRWJVifoi0mSpOFr8lvQp_YuE24MtTB9pFnwdG7QIPW6g9jk7BZk8bR0R9kWcVoa4CQDvWWoyMyAXiK1Nr2PoZp-Bh9A3BCNHE9sMn_yG_lUAwKdptkU7KiS5yjiBMSA89yTIGRrBMs-syj6_LbuHH5TCwrBGWR-M7lbOHXG4ocjVrFmw3JK802JlCIJg8liVB87ew1WKCngulh-svg0rGZyZ7x_EL2Ukmii8wSMRBtND5Gn3FBBvLlwN_j2Ev0cq3FQD-_NaihPj6xFTFCu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
پوستر باشگاه پرسپولیس برای تقابل امروز مقابل شمس‌آذر قزوین در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103756" target="_blank">📅 10:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103755">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js5-TBxkYQLFBU8liLjQUe9EcKdBLEI6St1hNTK9rPHZQhTgINavL3CFzN0lCCm8YP-mfaxOHYm7ikwModbt50TCaqE2gUisylu8Y3CUxxbYQMK2kMZRq-lcAlASLmn9z8mFwznCKxl1e87SyPOkprOONd0ql6c7pHO7SLNGxkJ8xke67-iwAGewowlFou98fFSd8Th-w3gVj4ElAVRnFmXF5PE3Mr6nsHHKsHW9ROvOAZ5L7myWE39kVjrAOgaCDsBI33otPoiWPBpsOz03PNsB0kxAK-qBNT0HbM6iyAMVwp_Prze1fMPJodRTEHYjjz_jvGwZzADY8--CYDepAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو: کریستین رومرو به اتلتیکومادرید مبلغ 40 میلیون یورو  HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103755" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103754">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1dILyA5LRDJOsPB2GODIb6iodMf5ugaR_094elZSfEpKxWY_tWgyOJhv3RMFxP9DFclHdsRL2Uleat9EK5dpWMfbi4b8i_crztMInMnpyX_gfhZX2o01gnx_65_dheeHCa3rPnS2rpCtls3Y5YGAPuR2i7z70F8O8kOJ9UNmWdRsx-6TppC9m9K9lnnQcxg9bqy2Obl8PQtn9W8w-TGRrhrzSHQpZ0o3zVUr6KjLqRWY9gc_VinUPPDpAV1IGIrS2nbZtOf1DjwCao0hnFQe03yIzbQoncSCGNbJ9z1g5CPn9kWyCbWY0biV-5CfSAHAOE1kOsJmytLp3q0tiAUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از از متئو مورتو:
✔️
انتقال رودری به بارسا تقریباً نهایی شده است.
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پس از روزها مذاکره بین دو باشگاه، مذاکرات بین بارسلونا و منچسترسیتی اکنون وارد مراحل نهایی خود شده است
🔥
🔥
💸
باشگاه کاتالان به دنبال نهایی کردن توافق در ساعات آینده با مبلغی بیش از 70 میلیون یورو، شامل پرداخت‌های ثابت و متغیر، است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103754" target="_blank">📅 10:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103753">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb15999303.mp4?token=f55BJwtgzWFzM1MtEOWA3izOA6UpuXVPybWTOI11owwOTtkUJXTLlq-8Mppm5lGG5PlQeF8YDbdmu1drp44NqIFx_wvP6ZhRFTLNR459gZXl1gEsE7mIgNxF-EXN87UrJypu-PdatDFBkQpP9vBvF5V31NrLd7c0Ucc-g_4cEYP7dhmdgP3j2cLVuY21YdYYzgskusm7mncAq0D_LXfkJtP2LGruOsncZC-vQeEwfFtisHzKYGlunxea7-qICfWxD25rEOyy3JrLMg9Tla0PZTtR797rGqbUF9qGp8uZ7yKOZJg11E7rj9jdsYYHs7O4tfUDSyYQZRRTzaLT3ruXpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb15999303.mp4?token=f55BJwtgzWFzM1MtEOWA3izOA6UpuXVPybWTOI11owwOTtkUJXTLlq-8Mppm5lGG5PlQeF8YDbdmu1drp44NqIFx_wvP6ZhRFTLNR459gZXl1gEsE7mIgNxF-EXN87UrJypu-PdatDFBkQpP9vBvF5V31NrLd7c0Ucc-g_4cEYP7dhmdgP3j2cLVuY21YdYYzgskusm7mncAq0D_LXfkJtP2LGruOsncZC-vQeEwfFtisHzKYGlunxea7-qICfWxD25rEOyy3JrLMg9Tla0PZTtR797rGqbUF9qGp8uZ7yKOZJg11E7rj9jdsYYHs7O4tfUDSyYQZRRTzaLT3ruXpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇫🇷
آخرین‌باری که بارسایی‌جماعت معتقد بود یه بازیکن از تیمش رو به PSG فرو کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103753" target="_blank">📅 09:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103752">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔵
✅
گل‌های دیشب دیدار الهلال - الفیصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103752" target="_blank">📅 09:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103751">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4ae02899.mp4?token=uYLxGHU1A08MhAZwbuawqRTO5fkVdd0pHzukdErV_fP8yvvqbxSyfCi9j-Un5waMV9czb7Pcz1zPnbmYWdsD9DpMJB7aHdESe6p2pzZCY-z8Kwk1LCqoRb4ECpnNLZi9Wchq6G2JzFFqYMLfe4VvkvRgHt47Pz4yehPrfqooIMzQ_UtjVCto_IqkTfN1lCoamxQr6UiVShG1kDfO7YmMdRT38zieVt3rLd7DVl7rRy_AR6KqJ8EnINXhr9H0IfjR0AzFhbjj6RK6mtrRjGAec_Wjl9YW8KDLoEDHvptqEp-b8FX8NyekqsUminodzZI2w3kK-8pbNJDBLxA6mzH6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4ae02899.mp4?token=uYLxGHU1A08MhAZwbuawqRTO5fkVdd0pHzukdErV_fP8yvvqbxSyfCi9j-Un5waMV9czb7Pcz1zPnbmYWdsD9DpMJB7aHdESe6p2pzZCY-z8Kwk1LCqoRb4ECpnNLZi9Wchq6G2JzFFqYMLfe4VvkvRgHt47Pz4yehPrfqooIMzQ_UtjVCto_IqkTfN1lCoamxQr6UiVShG1kDfO7YmMdRT38zieVt3rLd7DVl7rRy_AR6KqJ8EnINXhr9H0IfjR0AzFhbjj6RK6mtrRjGAec_Wjl9YW8KDLoEDHvptqEp-b8FX8NyekqsUminodzZI2w3kK-8pbNJDBLxA6mzH6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
دیشب وسط مصاحبه یه هوادار استقلال، رفیقش میاد انگشتش میکنه و در ادامه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103751" target="_blank">📅 09:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103750">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9408795cb7.mp4?token=bhWzCgZOVGWRferOW5970hry1BjWwxG0VI_qHeEnQT4xNHxHSg-Uy2siY4gfkGH2hLneyPBUnzGW_iao7tTM1KaF43Rzwez9hSqpBsbwNtvIjoiPV0Kt855DARX4a8c9Lbh5io7D78ddHKyAxzL8FY1gieVkjaRheBFaVo86mI3mMobAxeKKzSn0wLJPkNqgbvoXe7Q9S9JafE5MNwE6JcWNsW9kstY3iRRbLIb4aCm2yRRuYrLqldQz35iYQQ-WHtybBVEHjqhxyHonh5mdUZSik9703CfN81iNSfAxpzRPWvNqQAKtl_34oV7u7vKxOzpXxvS-NIotHU4n5sSL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9408795cb7.mp4?token=bhWzCgZOVGWRferOW5970hry1BjWwxG0VI_qHeEnQT4xNHxHSg-Uy2siY4gfkGH2hLneyPBUnzGW_iao7tTM1KaF43Rzwez9hSqpBsbwNtvIjoiPV0Kt855DARX4a8c9Lbh5io7D78ddHKyAxzL8FY1gieVkjaRheBFaVo86mI3mMobAxeKKzSn0wLJPkNqgbvoXe7Q9S9JafE5MNwE6JcWNsW9kstY3iRRbLIb4aCm2yRRuYrLqldQz35iYQQ-WHtybBVEHjqhxyHonh5mdUZSik9703CfN81iNSfAxpzRPWvNqQAKtl_34oV7u7vKxOzpXxvS-NIotHU4n5sSL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇷
محمود فکری: پرسپولیس سال ۸۲ برای جذب من خیلی تلاش کرد و هرچیزی درخواست میدادم به راحتی در اختیارم میذاشتن اما در نهایت تصمیم گرفتم در استقلال بمونم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103750" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103749">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040b76d16f.mp4?token=GNA_a0kDUPMSAj30mDfpgm69ail5I0dFtsW7UX9MthN2wsDbxCWZsOTLIVGgk-9uUFsreQaE1jBNPrhX7PrF1Y2F6P_3yReqpTyZ4PVbMTc3uwBtIMvNT0rlb3yE9uSL_RORntIT2XEoZC117IhtL_1I4QJE0v3VW0T1QDhQ4sy4qHY68YbZVAghsyt_OcsPphT1zNBgprCZyjXOu2htmiEeAt2HNxWO7_MsFghgmr7LYVFrJzK-Yo92kOGY4uvSnP5jfe7hceXROYnJTtrhmW1HwV-aOLGdFrAlyPlkS-Lf1t1koQeKRTO8WrekbgfQjOV6DWVIZGyIs3QXqoLXSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040b76d16f.mp4?token=GNA_a0kDUPMSAj30mDfpgm69ail5I0dFtsW7UX9MthN2wsDbxCWZsOTLIVGgk-9uUFsreQaE1jBNPrhX7PrF1Y2F6P_3yReqpTyZ4PVbMTc3uwBtIMvNT0rlb3yE9uSL_RORntIT2XEoZC117IhtL_1I4QJE0v3VW0T1QDhQ4sy4qHY68YbZVAghsyt_OcsPphT1zNBgprCZyjXOu2htmiEeAt2HNxWO7_MsFghgmr7LYVFrJzK-Yo92kOGY4uvSnP5jfe7hceXROYnJTtrhmW1HwV-aOLGdFrAlyPlkS-Lf1t1koQeKRTO8WrekbgfQjOV6DWVIZGyIs3QXqoLXSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👍
اسطوره علی‌دایی در آب گرم گامیشگولی سرعین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103749" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103748">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGcDfDPFf4l0TDpW85u03bkGapQy6rmYMk1gc441PTFN4kidZ7emDc_bY7HAnv4kUz9XmwKAFNJhrN-1Y5yKQOgzGwN66f4paKansxggJnhAE-DpEsnpuHIRIhyz2u18IjIKwqa-w0UIDIT1uFOa9FfGzSA2z9I6Qhrrj850w0JbUnX-_IIRjCvqgQc_1g-0M-k8RvyHIdgjKVcZJ2Wvl7rAbSsTBGc102efPjgxjuw7IZqXq0hprqWqCN7mM9Feh2AWcnRRHGUwscMll5eMo4g4Pzh0eUm89gs5f68bQtNSKzSNB-2m5C-i9q7D_vHW5346qMIudELg3QIJTVVphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
تاجرنیا: طبیعتا درباره یاسر‌آسانی نگرانی وجود داره اما چون بازیکن با اخلاق و خوبیه ترجیح دادیم که بهش بازی بدیم و با علم حقوقی خودمون امیدواریم مشکلی نداشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/103748" target="_blank">📅 02:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103747">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205c3a5736.mp4?token=fQqiSo-DhGkz9ljqqQErBnRsDFuGn-qLIix3hGNiwlMymMJL0nzzFP8qThUDyJbR0zg9_EKvW5mDOhcP29bMe8IQaEHohMNjJulVPJkb2MoxPqZR051yyoUrlS4gyN6WZDh1g9S2w4fJF8s1LsfSr12bqmXWoj5eqMBBUnY3ZutLJQluhOCGZNhwTMdDdoI_MokaiAnwG8Ndq7SINaJRsnUTurwlKx3RsJEk7CwYBXojaUfzRMH32MhpAwDj5_oO9-toFE35ggsXHUC4TGAwg1wRWUiC6u8o5Cpg3kduk9Eh-C8ukijJBGZ8dVLtFgHqagn0nQPk9fX-MuD4vLqiHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205c3a5736.mp4?token=fQqiSo-DhGkz9ljqqQErBnRsDFuGn-qLIix3hGNiwlMymMJL0nzzFP8qThUDyJbR0zg9_EKvW5mDOhcP29bMe8IQaEHohMNjJulVPJkb2MoxPqZR051yyoUrlS4gyN6WZDh1g9S2w4fJF8s1LsfSr12bqmXWoj5eqMBBUnY3ZutLJQluhOCGZNhwTMdDdoI_MokaiAnwG8Ndq7SINaJRsnUTurwlKx3RsJEk7CwYBXojaUfzRMH32MhpAwDj5_oO9-toFE35ggsXHUC4TGAwg1wRWUiC6u8o5Cpg3kduk9Eh-C8ukijJBGZ8dVLtFgHqagn0nQPk9fX-MuD4vLqiHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
لحظاتی از عروسی جذاب لوکاس هرناندز ستاره تیم‌ملی فرانسه و عیاشی بازیکنانی نظیر امباپه و اشرف‌حکیمی و ...
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/103747" target="_blank">📅 01:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103746">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d121350bd.mp4?token=Wz2RetR_tk_bjBpyvqGlAntQ036OSHg3mJAeqMDrtR3v1qpfTy9odV-H8uTJTdKYL3ocz5jW8r8m69m_xfuvT_wwsWG0miXEguGhYQ5HqwoucA3IYF1cqq-YsBBMNpeSOlZTyHxXdftV59nnmVstnFSV_A9BquOM9bH6Kl-ZhmLaQEVLA_iu4nOUCNZ53MTBD6-Ty2fHhgM05DgPpN9KzqiTdRF55buOWZgY7Gcv-jQVnOJIoR1ahFPjmMiQqmQnVmJL0rzsrpyW1qFwliC-Bl7XZfFVp4xJdN63qt3JI5LjHWQ7Pofp9Aar3l60jx5DcwgU4bCwmGq0Xm9fghzgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d121350bd.mp4?token=Wz2RetR_tk_bjBpyvqGlAntQ036OSHg3mJAeqMDrtR3v1qpfTy9odV-H8uTJTdKYL3ocz5jW8r8m69m_xfuvT_wwsWG0miXEguGhYQ5HqwoucA3IYF1cqq-YsBBMNpeSOlZTyHxXdftV59nnmVstnFSV_A9BquOM9bH6Kl-ZhmLaQEVLA_iu4nOUCNZ53MTBD6-Ty2fHhgM05DgPpN9KzqiTdRF55buOWZgY7Gcv-jQVnOJIoR1ahFPjmMiQqmQnVmJL0rzsrpyW1qFwliC-Bl7XZfFVp4xJdN63qt3JI5LjHWQ7Pofp9Aar3l60jx5DcwgU4bCwmGq0Xm9fghzgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
🇮🇷
افشاگری پشم‌ریزون محمود فکری درباره قرارداد رامین‌رضاییان با استقلال
❌
باجناقم، نظری‌جویباری به من گفت از قصد بند فسخ ۱۰۰ میلیونی رو‌ داخل قراردادش گذاشتیم تا از استقلال به راحتی جدا بشه و دردسر زیادی نداشته باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/103746" target="_blank">📅 01:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103745">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eac5b5b3e.mp4?token=e7Uup4RlxAwjSPU5MmUqrb82MfSq0kuz0A7SgdfznO-Zqu1biE0xnEBrTqs92KZrV67li227hNW-YBDGlQzaS7KpKgW46HM_jXIqTAgCnsd2vicRsIR0dBi2Lk4zaZ9oYQAjsT5NjYzMdHIe_0u4pILXpxk0H_QLfFWhBs7MF4FjLs-bPj1vQ4dT1u6qJS-xUN7deDFxX_7iMwpaTkclCF2ugJeleKkXTWIP8KA5IJa0fd7tTJHsWiey1FWsiKS85EPfKsK-jpV9iHdb9S5MAnr1kF7eELICkh8f4GFQu8vomTwZUwHo3UaslM1myBhWoWn0jIUjTy2BhLutVLzf_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eac5b5b3e.mp4?token=e7Uup4RlxAwjSPU5MmUqrb82MfSq0kuz0A7SgdfznO-Zqu1biE0xnEBrTqs92KZrV67li227hNW-YBDGlQzaS7KpKgW46HM_jXIqTAgCnsd2vicRsIR0dBi2Lk4zaZ9oYQAjsT5NjYzMdHIe_0u4pILXpxk0H_QLfFWhBs7MF4FjLs-bPj1vQ4dT1u6qJS-xUN7deDFxX_7iMwpaTkclCF2ugJeleKkXTWIP8KA5IJa0fd7tTJHsWiey1FWsiKS85EPfKsK-jpV9iHdb9S5MAnr1kF7eELICkh8f4GFQu8vomTwZUwHo3UaslM1myBhWoWn0jIUjTy2BhLutVLzf_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
🎙
نطق جدید از استاد محمود فکری: با حیوانات ارتباط داشته باشی بهتر از اینه که با انسان‌ها رابطه داشته باشی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/103745" target="_blank">📅 01:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103744">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e109a43029.mp4?token=Kneoy-OxjEFRbgdX5RPcCOueShyCqT1PZKn_kSdXGZOcH5Yoza3VYSLssorlU-BdMP7DUeEyZF3Kxm92bE-ckbnVqof3jgxBUU1XYG21hjnhOtv6Ja8w6nzjvf3DaTsiKEb6kAbyvRcSDnF-Ajt8qidDpp6ldIyWSHSI3penswTXnISXVRpchsoHUOChfBHCn7_7E1ePmt7lUrwh7z38PPeiM8BpxTa-4zcSTKnLJSVCCWOwi98EFAD5zqQP6ikncnEFbryTErbyBSNuSljhuhQcrV8qQw05g0-fNNtfRxfsSEjPDOfQhM0Uy-j76LPDCtWYxokFihKoaMGJ44LAdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e109a43029.mp4?token=Kneoy-OxjEFRbgdX5RPcCOueShyCqT1PZKn_kSdXGZOcH5Yoza3VYSLssorlU-BdMP7DUeEyZF3Kxm92bE-ckbnVqof3jgxBUU1XYG21hjnhOtv6Ja8w6nzjvf3DaTsiKEb6kAbyvRcSDnF-Ajt8qidDpp6ldIyWSHSI3penswTXnISXVRpchsoHUOChfBHCn7_7E1ePmt7lUrwh7z38PPeiM8BpxTa-4zcSTKnLJSVCCWOwi98EFAD5zqQP6ikncnEFbryTErbyBSNuSljhuhQcrV8qQw05g0-fNNtfRxfsSEjPDOfQhM0Uy-j76LPDCtWYxokFihKoaMGJ44LAdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
✅
استایل جالب از یک هوادار مهدی‌رحمتی سرمربی گل‌گهر در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/103744" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103743">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c593055ab9.mp4?token=Egid7z5Ix6Xm3a5mEIzf5ODU-AaPytk-gtSH4qsSf9S7NwBUOHtoB-FOg2jP-kd9s5lFC2KDCbowoSxoW555wbxz9A3fdI3hffm5A1MvqC5DMn92HLWPL-gq-KpBVZWNXZpCwytrqdvVXYEe6vNqB_Ex_p2uLBero3bhs9KI39qFJjlxNT-75jVoPkKf_KAN3JWu0y4gf4KMj8nGZXzqC1exgjtzO8ve_l9_k5Wi3-XR6s9-sl9MPZ4MtgQqz1-a8VWTU9JtHncV7VUiX_Jtw8vTdz359ujYxyCXYUk3DDep58RG11g43P-jke3dUUZhat9WXPllKZ8NSKfAH7sRvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c593055ab9.mp4?token=Egid7z5Ix6Xm3a5mEIzf5ODU-AaPytk-gtSH4qsSf9S7NwBUOHtoB-FOg2jP-kd9s5lFC2KDCbowoSxoW555wbxz9A3fdI3hffm5A1MvqC5DMn92HLWPL-gq-KpBVZWNXZpCwytrqdvVXYEe6vNqB_Ex_p2uLBero3bhs9KI39qFJjlxNT-75jVoPkKf_KAN3JWu0y4gf4KMj8nGZXzqC1exgjtzO8ve_l9_k5Wi3-XR6s9-sl9MPZ4MtgQqz1-a8VWTU9JtHncV7VUiX_Jtw8vTdz359ujYxyCXYUk3DDep58RG11g43P-jke3dUUZhat9WXPllKZ8NSKfAH7sRvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
افشاگری جنجالی عبدالله ویسی سرمربی ذوب‌آهن اصفهان: دفاع وسط نیروزمینی رو می‌خواستم، منو تهدید کردن و پرسپولیس بردش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/103743" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103741">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404f90ecbd.mp4?token=KZq6EMBn__-zc-HzOS5AbPnA3hkc-hEr2kojRQGa8fp5Eaj3dbihGzj5I3K6hmbesfsuGlS-ZaNOeNKhtxo9BtveuHYWG4uwEeCtHsjJxX1YJePkpUI9uQYf1EKDdVtlId7lXfpU0XPOFPrpRym8ehu4PUvqZ6YBbd3k6Ja86MAOadW1AprHz2bC1hAOOXquDEUXKAV6ku3_57qYeSQTs5Of1g6gjSYMgLLARSD5AWnbVA5bWcV_F5cVfLFt5ApOUmFlsRg4-CX_Qnvohx8FBC1K7N0SXlqZ8HCUqsR_NsKlU0rCn_WmKQ1RwRK9JgjkjHtGlOHzqE22uNfCNC96TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404f90ecbd.mp4?token=KZq6EMBn__-zc-HzOS5AbPnA3hkc-hEr2kojRQGa8fp5Eaj3dbihGzj5I3K6hmbesfsuGlS-ZaNOeNKhtxo9BtveuHYWG4uwEeCtHsjJxX1YJePkpUI9uQYf1EKDdVtlId7lXfpU0XPOFPrpRym8ehu4PUvqZ6YBbd3k6Ja86MAOadW1AprHz2bC1hAOOXquDEUXKAV6ku3_57qYeSQTs5Of1g6gjSYMgLLARSD5AWnbVA5bWcV_F5cVfLFt5ApOUmFlsRg4-CX_Qnvohx8FBC1K7N0SXlqZ8HCUqsR_NsKlU0rCn_WmKQ1RwRK9JgjkjHtGlOHzqE22uNfCNC96TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آنالیز محمد تقوی از برتری قاطع استقلال مقابل تیم فوتبال مس‌شهر‌بابک در بازی امشب لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/103741" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oURsLCynisi0T1_jxobwNvFqhNPa_lzfTg_KF_fEYaUP_3Xcu1Yuc0FUtbxrPHaCEOnzL7suUngh0nrYGjRguKQJUJCC-s-aJYMRLYyZMWLgu-7d3U4N4-NQLABWa8wKinwnSy18muyPDNtCrLoWMxp4MSMqDaAzTP0NY8E6eSX5iHfwZZvg5FNyDvZUrkY8Z44KNZllHoohXeNHwSCDcRCYS9pqf1Z66cXNtEolyU5UX-qIjZoxoSAh27KSTqb9PhMt_LBv1eKbpYeEUOaO10eUsyHPCiWj3Qi8zjHIuQ2KsSVtlLPRx3C9YRrmHdLzPnLbT45m6dAepPPkoOIhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
داکنز نازون همچنان درحال نخ‌دادن به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/103740" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3aa311a1.mp4?token=U4-8F7Rb7FLMMIDYnnI_7RZUnweyyIkgHhJN8Iai2Pve2kulAMZkNh8EJEgrUyAgu1ZJU2b9LWFUDOz2W4xKkTp3L_8oCGZ-iTq8Dz4nZOBDHlUp_FEk7UXzqfIg_iD1bLjiNjMVHGetUjTQyvPstiQnU3ZT9-gwlPqqNcNbIkyQGRxKcFBbHViN7sbSmDucBtwKaY0Biqd-MYEUT8FzOol-zgyDoaaf1zp5PIJHNyiuQ2vJkGT0kx12wPDaRefne5kOayITsLkosXnXbMeOnVzcEyPytg0qbChC2w2YFElFzVSybRmMr7xwdqai28WObICzQmREqQI4W1Q_eaBjYno2t53mvguTGTWempzQBAbU6torWFGr0oOkyYi2eiuACO7tZrGiFlmqFEpLntl_I6Ki_KmAsriJGmgonue1VETtXy1qt5wpKhO5YMIbcuP8F7MfSo6usAJATTRjKQuhaeodMISsrEsTcNbrf4V_atOs2fyWe6BfGKGoYOGKW22EvqhxYbREGYwpBZ3wcb6nA2h_T5s6JSEYm7JoakT7E4NtvkR_pZwIZWPQd9guVEKJ-UtMGf1K5LxWyTJ9kWKKydaTnLKXJiQBCNpL7puzvGm07R7_gHKmjHZQeVC0Eyk0_Lo-0hsNprKkB_lqSutBhQAZLkWns65V_rQ5dTjLE9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3aa311a1.mp4?token=U4-8F7Rb7FLMMIDYnnI_7RZUnweyyIkgHhJN8Iai2Pve2kulAMZkNh8EJEgrUyAgu1ZJU2b9LWFUDOz2W4xKkTp3L_8oCGZ-iTq8Dz4nZOBDHlUp_FEk7UXzqfIg_iD1bLjiNjMVHGetUjTQyvPstiQnU3ZT9-gwlPqqNcNbIkyQGRxKcFBbHViN7sbSmDucBtwKaY0Biqd-MYEUT8FzOol-zgyDoaaf1zp5PIJHNyiuQ2vJkGT0kx12wPDaRefne5kOayITsLkosXnXbMeOnVzcEyPytg0qbChC2w2YFElFzVSybRmMr7xwdqai28WObICzQmREqQI4W1Q_eaBjYno2t53mvguTGTWempzQBAbU6torWFGr0oOkyYi2eiuACO7tZrGiFlmqFEpLntl_I6Ki_KmAsriJGmgonue1VETtXy1qt5wpKhO5YMIbcuP8F7MfSo6usAJATTRjKQuhaeodMISsrEsTcNbrf4V_atOs2fyWe6BfGKGoYOGKW22EvqhxYbREGYwpBZ3wcb6nA2h_T5s6JSEYm7JoakT7E4NtvkR_pZwIZWPQd9guVEKJ-UtMGf1K5LxWyTJ9kWKKydaTnLKXJiQBCNpL7puzvGm07R7_gHKmjHZQeVC0Eyk0_Lo-0hsNprKkB_lqSutBhQAZLkWns65V_rQ5dTjLE9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇮🇷
پشمامممممم حرکت عجیب و خطرناک هوادار استقلال در پایان بازی با مس شهر بابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103737" target="_blank">📅 23:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇦🇷
15
سال پیش در چنین روزی
؛ لیونل مسی در تقابل با رئال مادرید موفق به ثبت یک گل و یک پاس گل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/103736" target="_blank">📅 23:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f450f285da.mp4?token=v5Ru0Jw9zYXUx6d7McLTPILxqVJiRmEtTYz0c1IPirML6wgKpVp8NfAXYH_vHMp3lE4ld8QxNtmttHbh2Q8-DMbQV1ZLFFqXYBHWGz0K7WQYJA6UmuXZrLEIiwLDdc1dO6f8zvzG_wMPxHVzoTboT36_24hHiqN8OMyH3pBQuH5W4p7FRpk0KYzfaqAtj37TUb0cNA1mF6YlVkSKA01hOt0Za5Yoe2xYrepV6hDdK7vUJsnp__p_6tACBLLvb1ZYiR1NqHErndA54tZSGUwDZ8Wp_SFloop37MygKaf19-iWeUaDX-KF1CfdvLLIIw3TNySzEXwdylaNyCMt81VSuxABd4_NMiSIqbzfrTygO8YvV3hdJAhQn4XEJMysdRPMK9vtZDChA2GddxGMFm8HJsh4_JetMN7zJ04oa6716DVdi9tZNYQU1zh9awpw_KtYzEmQZPVU9Jvk_2wlHrumW2oraHofotq-a8lYMVkyY0Liukriwnfsv5KxFz-XroFEyH2vfG2Bq4Wz906LAfJiuuIN9lGDayUkxRHgOKQ8bbQjg-gCrnEWMdx0KlewavniO4SblikYPGxhymelHnuEx6bekYngnZp6cu_Amh3wvUwIj9da-0WXHjtet2rTLht1OLH3TDHr53aq76rLD7IZFwQoZ4mbvAtmQsFrAtLcr1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f450f285da.mp4?token=v5Ru0Jw9zYXUx6d7McLTPILxqVJiRmEtTYz0c1IPirML6wgKpVp8NfAXYH_vHMp3lE4ld8QxNtmttHbh2Q8-DMbQV1ZLFFqXYBHWGz0K7WQYJA6UmuXZrLEIiwLDdc1dO6f8zvzG_wMPxHVzoTboT36_24hHiqN8OMyH3pBQuH5W4p7FRpk0KYzfaqAtj37TUb0cNA1mF6YlVkSKA01hOt0Za5Yoe2xYrepV6hDdK7vUJsnp__p_6tACBLLvb1ZYiR1NqHErndA54tZSGUwDZ8Wp_SFloop37MygKaf19-iWeUaDX-KF1CfdvLLIIw3TNySzEXwdylaNyCMt81VSuxABd4_NMiSIqbzfrTygO8YvV3hdJAhQn4XEJMysdRPMK9vtZDChA2GddxGMFm8HJsh4_JetMN7zJ04oa6716DVdi9tZNYQU1zh9awpw_KtYzEmQZPVU9Jvk_2wlHrumW2oraHofotq-a8lYMVkyY0Liukriwnfsv5KxFz-XroFEyH2vfG2Bq4Wz906LAfJiuuIN9lGDayUkxRHgOKQ8bbQjg-gCrnEWMdx0KlewavniO4SblikYPGxhymelHnuEx6bekYngnZp6cu_Amh3wvUwIj9da-0WXHjtet2rTLht1OLH3TDHr53aq76rLD7IZFwQoZ4mbvAtmQsFrAtLcr1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
👍
صحبت های زیبای آرتتا در تحسین پپ گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/103735" target="_blank">📅 23:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103732">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT84Su30lUzPJgATT3s6FyI8pDys4lqxakmplqToSKNklkHbqtm-xvEavHlvYirHhRn0_0eJKQ7gC_BYLJ8N0CQ3LedcwrZKBtwB0rDwdKSr_3rs2Q2m3MbdFcN6DJyKSJGmxjJ3jbWWjiW_IaEcHdjrgBHOhBwT8QfWMj8j2hyWNRcFPbxmWw9XiMxyquKXwo5UjR8hXBOvj4gJ2jisikKubisvvwye49pcqhOfNYTsQuKK0PkQ_L3zQvHcQhgQ5MuWg3lr6OwRGRweG7RqxzNt-qW1_dfhzBHDj8iGaIc5m7Q_z3gmZfBKxpMwrU5RZWQD0dzGmqe_fEaLS-mqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjSAo723T_UrMocfpRuTZ1Avx2CsrxT6AfWkj8hqSePJ0XR9iJPt0548UQjab0gzHYpMjz6evEb9ygRMYRbeqaBjLqM3EEu64ha3ETl4ALw829xsrGtZhazWw5lrXlbTwbfIcr9rZ-_Q4xbihVeWpiaZ5o4eUAJH51vjlxLSKydDMuW7PKCc0CrMvQknjFj4ftb3u3dk_V0q2SMi6s_8oqXNesnZjPYEEUdANBvaUz_QrKRy_LgiGUffIZ9gAn8qq7QxG81pxk8uNKuGE2ATGntiLIUSUwwVxm3tpuIxIIuQREQ23uX_MBHO40yK-gT1KfDJUkyicogq76ZBldbCbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J07YPbZ8wLNiiLoax3JV77HFA8UB956DkIEshShXD3AkVMB7ZcrKi8crb7WhravaIr3P0MfH0DaPyzZksBfca-YnXABU6QY5pA2FMm37hz8E-YQJaweNmOowKQpqlVRM8AhVhWRxNjnZf-DLmYvg3cv5k4ffFITY1Hk82TK8vSAWDL5Q90bjQoxRRsTcJMxUVwD2WgkeNfQW4RkU2-ry_DQe4V4s5ozQLg0h3pDr4QErWHAD-GJ3b2te5zQ-QOntb6amZEqB8TfB6ilwE25Cd9hheAuHb0KHVp4em4KFMnqnZKdwMbgdUkFgX_VOYIjHkpk0Yh9-YdexhcuPXtiC5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😢
😢
خب برگردید مثل‌اینکه رونمایی نشده و باشگاه پرسپولیس نوشته COMING SOON احتمالا فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/103732" target="_blank">📅 22:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103731">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCh-BmWY3NgARwm_eVf-6dsW4CHWWz3tNcVMnKkdvjo0zqX1KHilVL0o12Rku-ee1-_2EVJzHBctIrD4oYnycTLNhAmaMPnxv2DjdK8SYIpT3CktLI6AUP-NayCPX9qy1mCvQm013M5E207ed9OWjyobZVZv39RVn_WVCVe2CcsP5NCQGvVybh5LLW6BNEApIq2Vdhqwx2U0JZyd2qqRhoKQ1r6xC9jlhEGIbfLfqiZOwbG0W-gXu9eJMupl2vKll9VyverTLlZtRm_x7rBmi_CSbuLnnHVVOtV3SGj2mW3-2sMj5zBZBeltdszXg21x4b9X5DB1Af2qfp67jfJi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
فووووووری از الکس کروک و بن جیکوبز:
اوسیمن خواهان انتقال به آرسنال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/103731" target="_blank">📅 22:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xb9-F5vRVwV_Eb5i4RNjsLEUvoB4CEfUhckEl72QxTkf_ZThLzItQVvPdX58QQzKGtYAPCcuUaDX-kqHfdd_s0L-XISeGx_Kh8vcuJ2mgHL4CMCjKVtXXRG6hWvVTi8DYRnt-j7uPG3E29gSGv0mlv4ebgukbSvIdIiq1cQE70UMzy_7Myb0HwRfz1Oda_fSQwzORmy6CAlFzg3App0WhEd1DSzevvsq6j4croivUFo3YfGRMjy6jVRPJInfBNRzPbov5Zlt3jARb--w4sfkuzN2CYVmq1AUBQz2BjGsZAEtiiQgvb9UUjjY3Eu8unl7f8y3T660aVdyWiqGAy5q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7WmhoqtJGxq9HkC5VcEYFn8lKX-SCum1tVmptwhaK9VR2GCUjFzxV395ul9joB3shLUH5O88i8BfoU3iYh0f1gvTPVUUw-apuftHD2g1jSzXOjxbvSAZfrsMGwDqA60A67uMnn4AJn0z3IR62D9TG6_ZG-Yl37v_uJOgX-GHVDlkyjvDKxN0M4RuwXuTxIe6ohQ238nL9DlH2sT7ITUc0LtnMfiHOIBZ8afXW9nCFirL76j9MObpSv9hls4PxThHuvy-2XVVgG5COyGLwjk7726QKLr3TTgCvrjTEwHfi6QmOJPD01RFM4EQwU84NfMgbSpRWeVxkCbt0fB9u6uvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
💍
جزئیاتی از توافق‌نامه از قبل ازدواج کریستیانو رونالدو و جورجینا رودریگز فاش شد،
این اتفاق پس از مراسم عروسی خصوصی آن‌ها رخ داد! این زوج در تاریخ ۱۱ آگوست، در یک مراسم خصوصی در ویلای ۳۰ میلیون پوندی خود در کاسکایس، پرتغال، ازدواج کردند. آن‌ها یک روز قبل از مراسم، توافق‌نامه‌ای را امضا کردند که بر اساس آن، دارایی‌های هر یک از زوجین کاملاً جدا خواهد بود. مادر و خواهر و برادران رونالدو در این مراسم حضور نداشتند. فقط پنج فرزندشان و چهار شاهد حضور داشتند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103729" target="_blank">📅 22:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4384r2p0KYwfMk-AoJIRdDn1lY-4ndf07X9DxDK5W4P2jIGeTs_NryQmIsuSVZEOw5HAOliaW7V1T8BAW8oge9evpJMhhktaOZn1RtoZecQG90qgmdgDj7-E64U3Dh7geT5-Br7tkwXTzX4_L5f7QvhbPDziyOEqAJbt_0KPO-fMZK5ojkzj-661M5nnmHL66snMSk5yTbbJPc-LSuCdxLZuZmh00kvDqemaPR0qb5B85zKbCtm1RAaojSSnP7YlMkhr5x4oaeE_I_RK27osw57E05dTBK3gxdI_hZ0y9XYVJ7ey6gvk59HZaKrpGuUDik5O5JX_VUw3urM55GIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
نتایج روز اول از هفته اول لیگ برتر ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103728" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
