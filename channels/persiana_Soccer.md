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
<img src="https://cdn4.telesco.pe/file/pCk9_c_qhult3DUj9RBj2Xzs3hwBSwngvklLjKDB71KNhdH2qW1AvEXPih4h_k9Zso0vyj75CB6toKmqFcD63cuqcKoC0YAIO0hWTO1K6PuHnIR5oYtjOprRbg6CK1-OLdnD__dARESixlNWr5XFyB-eIzjs-VctMl3E0nohqX57le2pALfM4KAQMtfLzhxWVKrTyVlUoNrjBfj09esFWulovy4MOrFuyUgHJ0xUGhOkQQ8cZAUow_thLzXJAgOMgl8e5naPGBtHXSdidUvfnk5ZsG17xAJKc4kP_JVmTXL-2E8hpPQM-IZj_Shq4D4AMuF9QPSwNeHElGtrBSXmsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=MDWYKdSv856HleChpn2PRgYOUACV6Ty4w1jckgPNXOFUa8epqD0b62se90aqNOpuYCNpWEbdSYYLMkgfzjwFP2trD6rjYvpi2IapTtTXc82uMh8M218dnlf3KAnS1b1meTjtuTFZQl0MC00VQScukEC9-c_FwDhZa5AYIA8jVN9Azow6HkVZO9yNsFcYZMLXWKnRGc0MDPmEVnXYYh016F7-X_IB671JsiUng2tB4QlzXRlD-mUJBu3APetv-PaeRyFqfqURb_cpEYRdEx9kvOSWohHAzvLf0e8vPLpkA7MlOiwCSfErRvxmJ-RrngxppxKOgscQgIOLlEluzyPhB7lkrEfL5pKYTkqD1FbVwG-6dQDF_eqc9FDNDowAmyKmoGJwy6BuL5Df_sUCxPhqZo3x85MRigWkhwQD34DGNZhaNlQJhlV2wtWlDrgnW30KVlDfIHBaZQUEgXkvyk4WkP93j95sohOTM-UOJKkjoqokzrZR9taAe8ebuhIdg4XoVuoOBAdipZaFJ4QxLrlXK-c1SzJLguyzYWziwVpdYttH0OmEZBKphyAoi91YLanAwWwTgp9eIiV59E7hH5CD0OGXrR0NU3F02CCKvesRfdDyCR5rrM8Htk6dcGy90IW-up8cApHj_VrVymj6DPuu0CKeARrmmhB1mX-vHe_duUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM8iVPTsqZA98Fi79nn-01QokNnzJruzx7da6YgvCOP-QuBBhW68toOmt5wchIjG229cO061zK9x6nZfzWj9u15oypokbzc6fXRZP2uALtNcs4l4jz1KLQaG4CgxePWECM8LzTvFuEvw6pVNPe4VcGihyv16BEYzg9KoRRYg3nJMZqng3-UGIWHBvJOcMDN-WtxQH1oi1V8ojtHYy1xJNLo_0_ZhexA9_pu7mcYP1Hz4QJttRGuIqi2bd5pPVYvQACrn-0TKU08TxHcss259lwwrc8T5j60P0x8qQdSq1k7lNfaxaBj1hjNhgQ0nHbbAZC0Ozcuukv97KJvCkcF2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHIj1Nkhvp5MnOLtmuILXjECSJTr23bU10YWqBcIRJGFOkAFfKTi2Qyv2QzIPAFA9IS1S_CPTp0slCLTWlVFl5Z7mIMtvGPUzd3Sf3InLXzx9dv9fAEGXdhwD85fpqjvBRJl1DQXCRkw-qyu7TrC75eoOV1uvsmmApoo5PzsHHv-anqTWEBX-gVFA-4PtXh0GyX2IUmJ7ZB3eB76SSXQNltCNuphBMTVKf9W4OU35uE84rdMJCiZMalKU6V5fsRtHQVbSnWv8BhyhLLXCpeugOHV5lCMS96ywg2PlyFJZm1EHgtelnX1cQw1LPvzwiFVWVSuJGa8HLm2_zzivJCR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS41kz7ioSBK0291U9p1E8YgukCTOnQeajopz4CPRg1ak5PuPY00fFMkzIiV5-6XWKZQ9sDG3FBivBxMCoAev5tiQ7IkmDl95z9fjl-WoPGKt0ZSPvX4X9Pe5XrnyVwS3enzx6TWo_jAplHbswfw8CI2BXts6nQfXUQyD40LLZRq0cB2o9zUhfq_0GsTM0-PLqP_pPOUnczMI0xii8IwT3b5PFtYSRj0Izkme2aMeMiPh9CuiMe7H1j4lx6RQ2ABfBV0aWvxRjbvdWo0ECFNto9fbL5IwkyJx3ORQWhG_TOJfOAdy2O3ji6q8D2QZ8hJpsaUrVFGzrTn7LijdNMmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjW1Ox9FJRHNC-MCzHIwTcHwKKNl2cEnCK9lrPJHrneko-kY1NJ5MQy3Zl8ptU8O5x2JSvsJU9O5pyHcBjF-PK1XDuM5r1afvT6ptCaY3Gnli5AqNfb3I0W2ReHOt2eXhWEGPbPs2pgguZfnTjpFLVcFEhnRjXfNFMep5z0Kfbi5K2nQeidGKAlD6LYgIIYczdgsT0GV3U9qi_1yEK9orNP9P9BQFB_4HiCWS7KBX187JB_1VccE-MLyAOCZ1-eALUEWXo7xFIya3JLWBG2fM5b_16qD87pIf_s_Dqlf3gCO4mALmVIE0tlI695pp9F889PMp3JFzuzSromjp_83fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H01-inSsUJxPg1eFsKYFbSGJ8tkWX2OTcpOzXNNBlBLX48yp3X_CJT09wbrDCu9UX4T8jpzMGQc3wuwieEelAvrkwWg6MSDRoo9l3A6fygV4SR8nQjedOBtHwUUxMb24nLCyLSy8UL8A5HbR5aPrTypXrSijvsruINxpdLIjQbNYGU1mI-HoJgGNWajDJd-5HM0EiJegjIOxk3Bcdp66l2OCSHS8Uhe0kcAgfX-51JGbk_RLZDqNiQs8JCN5a6SvEN-DFAS-xAhIkxmul8rzwii-1zZUWRpbP9McuojDV9DOkiG0QglWtxYiwEA2ovp8kG5tgfg5zqrQSVqjdxSVIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=WpQN-GPbfWgguyOl9RRy7l-te_iOlt1LmxTbH8SDmuGj4LbTs__xX80idVHglhjjQgWtiKEIiLxgmJpZ3oMynDkAS4lnDq5pus-HLodwYISoKEiNEDGFxkV7n9IWh-pI0jxhXLXP4R_pzF7H-vU0EjPHazFSr_FjmSCq4OkepJFy0hde7Cdi53i6zu7Rabsvd9FwnbQr95nQXBShxBnYEXVJ8vv0yCKCutE_GMAH2Tgqbrm20NFcasBh3ZZ1b46c0QEPhgzefSEhC1f2XcYn91EfRfNTiwadsA1KVKCrIUuJlolH-QdL3UeSe8IgYY1Hi6kyvT9Zbl5uorRfYX1CwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib28Ar0idDyVXn-aLjzj3NNEVDEZbChNnBRYFm8vBiaTFPHW3FDPtJne0XzCZIP3-gCYxJg08v-nMdqmw3w9I_mjS-XJs1k3lw1aEQuFlI_BUqeximq4iRGSMwjXaL0iLmJu6s5SFW5M7544wVCdKkK3opunAREnbhPr2LZTTdVhrgD2IMQ9UtUR1nES2mHFMJA5dyBcR9lPFeZEJ_nXOiKJjYMDhUi0K83mizJjs4fiq1ASGfMh6hMptHlWQ1i1NnCQiQHCAoX4-rblVlDMtQ-pVHNhmLwmPx4sRfOCOReh1mFCvh8QorgrCX7EHMug5HTsmIkr-BApZBT5pVlBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=he82DyMKikySUZz3wtuooAoFYmM67hCOFy-bIYZr_xtmWaqtnQsTCaHM1TqZJX_ejMA-KZ1JIT37NqmeKBtTeM9WZiYk3hxHDcN-nS47g9Uf04Nh2KExz84-rUFmJB2K8l7VmsyEQBMJ498PEjkYunYiV26xOAnEe1fbVxGPVDA2mezhLb3PoCvXoyGWp9j5WEAZGbt12rDa7qvC92BLV6gfPr1iuYQFLgh-Mv8SoRQC_JTlsz6iM75BeDNoUaXgYJduf8zNarYKXWsLyrHg9T4ISfDKMAj8jV6EBXP3l6vKyHkavzmPSJIwzy2Ov2n2-06LRMh4Tk1dMzF1zgnutA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDMAMWxspcSyEjz6ckOOw-9XzKfFKu-t2ap0XWHAD2T25FbxX6F6hOM7oqF47dbhNo9jM9qOgWJAgPEzgnvT1GXQo4DVCb8iQf-zVvjwTqqmsKScSKIzH-xUSIpCTrpNxzEpFheiH40TDbjHfZZ51JD-10A0ZuAYLhtmtMnHj3DY0U9aWv43oQQvMvwwyt8fICIEJRIGYwBu8JFh-HXUljhiRz1C3nHDpZ6rqDCCZRxYummI5nK5Uy0grl6Cvq6_s6Xcq6ZqXD4vjz_doEqrUGfe02vaB6RPHQFmNEsD08k6ReSuHidREFHyFhIeDldkjsrA655qJROikIqR3nhh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30246">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA2LIj926JayhKk0G7JmtupN733f6K1drSCiOdv3fwIMQgFlvawwqWUwaPtW96a7nYqsmgJbEC7cLN4HDRPKu-8doRnXjvHJ0i1Zd68oa46Z_P7mgKTu5TZUEbrbgAIHIwtO1hQV1BYdFRCRc07S6lAF7YkU-o7Azyi6K9ajrz4T7PpYeTdvUjStp_nEZMQQxlK_vSGoEZUGvRHQk4RMRvsUeQ83tVthBnJ1O9SIMhkS0hW_QnuXKvYUv5C8SnJgsk7arqu6v6dW0-zNy1hlsszLC85V1nPelBCG-qu5Q4g8O-cO09i0-Lm5hwvzyKhacB_QoQFerl1fl2lnCtvcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g31
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30246" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fcduz4YIwh0vSVNtbfz4FyfckC5Avqi4sWdzonCXR5Pycu0zhTM6CzSgFZIp2fm_xMe4ZJN3wvedd7GXgzwoO-unGDFlZE4nYsbT3OrMxLHYswo1dj7C3T22iQIEWlBsRtbP-nQTkXSg7Uglke4BLJLlIxLSejzrGWNpHmOgCpDBuG1TCKzKdZSS8nhoK2--HvG4aFr4Zv8KXurD3o47y4OzE-0sjmG0dCV0Xmqd3lzKi38ELyMz4N3_nQb29u6zSOPBvITpLfc8pM128isq8UzNv1rdEX8vT1wlWuyIvm3qjqQlcTxr5azjaMrhePF3C39kjE48-GbuDp-YVbUYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peMdUzxsSRgtI35luBy3UR0yzWP_AMCzvHSdmf8IY2XWZpIm16hTKpyT6dtQRjc28h8vJgdxp4aGkQK5kvrEpDha368g9OG-Ypki7oC0pLHTEhAAKWQUJKHW0BrvC2j2ASk4LkL9ZEtPG59v_0yKgxiTwgbwS_4RdZtwD-qyO25hX0KvvHKsXbS9MIbo82blcRXc2OrYXvTylWk5WVsF-QZQVUQH-iIcovNqDZLn3Q1rUQZe97ZisHULQF8dilHdwQT1PAlfXu_Gkkk0FAtmKiCGF4YMdR4PgYTk0nZ0wf0BnjXeJFiVviK3mQWhPipgbJJ42olysXr-J4_ANd_e0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaPiOKHtAqgyxBKJGaHpeuDQgI25WQXIMsJFP5RK63Pl5ozxe0njWNipN8SjAMkWy2z2VXvbyjUSiYm3FzHfe8DoPE1CL803fCNwhEUb_Im7pbcGNR2bbmYqHarpmrFzoahXQbnRRr-e6cBSIgb_HvH35Si_TL-1mlKAfYTLBJflrgK35gbSLTnKeJzL_3mJnTtBv0XWxSTu8KyVcxGhTz3oKWwuOahkB17BuVD7HM-DtDR7egNkCksp_vFZX7T33LS-sa2l3VU_i0STfWpcuz2gV0KAM56j15Qxo28RgFldYy5M6LEoj5kr0cVq_ztj0yflJwvzBAjyuq-zJDuzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsdX8REOlgJoZuQY4a2TMRqNndkOXm-Kh3huHKz4g_XZZwsUS_doe2-16wy9feajPgNaqUNMwH2llL9tCiSZdFMHNlEp_apgm9KjXpDN37SsEXlU8niaiS1WfuEHIQbXB35Now-_huFOSpgQZDr1PPxO7PH9Y6d17uF6UpmSOOMiePm2h7CkD00_ONQcjK5Lwb0Cb63PRHT1g79vbZHe-PXwRQZ5wI8LWRMiHi0kaowYAYH-Kunw81znKU38ky6O4-gs4BK4SfgJWhGN-KFfPPupruKRo8T5B8ogORgCsiG7WOi9Mp9_eE6q5zRzVkpiAoVd38psIiFgjeIRJy6RnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC_HRRWP1hRRir52Jhrk1EiS_ghTWze7isE8ju9l1Ri6CUNkUJRTX7cYByqPqd1_v5enGENp_84IRReXd0YKSHJJ8hJJ3OaiW1dQyVvHiPwUqEwoLYy3mg4CiimN48Jcz1zjYUd31uVYX8qM1Kv1QqaOYES1n6WdnQviTjPZ2zM8MknK56Wp3j-LZ5Vx9_QaUBtV7xT8qnJGeesBM3-o-iU2CP0VHXVdQI-1tg-g-yVmo70p6w1eDDXTTq11GCyXuecedLMmQYcMLOiDZg5hC7tFI_rcqcbz2CroB00H9OADHrHpi4vtkXsr-jLy1IopaAZAcMbmqGtn6xEPNB2H1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZsXtc1hQY-rXqRNIp_zVtraUw-lz7e7o0qmPdlrZgjHQfY0SMwurIrDAUAwSeztFKAEoM0V5EhNrj_e5nZbG3sV1Sa1Gdbd-QBjcfalRUgyeNPksvJebwHsulDuZJLpKypqsIh1e0uWRe3eGTH7NOMgwBuDU-QtpjXdRqujbUQX-F8Sa8hLxBKsm_gHp5A_wxKcGPamZ2w4JAjXEaoyiZQw3xHEcCio5Qf6R1_5m22ODhFWDfZB6l_YJ7sI9VV2ddZ-FbYJd-T5gcoXmswnlqERyCmXRW-RUTQiyYVpSaO6k8VPqsJATbmHq_Wkg1mtx4OuFiyWUP41c2lAhtJkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=O5gzquJErXub5ybjpB6NztJPgcUMQmC0_0xpJksrFtDbRIhlCXE1W94o5bDoX92uvGUeFKzn1tuSBxuokJeuzEOXd9AhGm23oUq3aRXcuQTGrQehgzdsoRKZGsPxQN-n02E0v_Y-S2LO3VYk2scx_493UieeXNkBu6F1a-c9yPkPDS2kEoxhi1dMB_MV358ZD0ddAfAu5j8B_lmb0bftJmt6TINPwsVcY6ZUKuzV_ITSPtm9b6NWNmboXVvHju_wIT-D32NosKDb0x3DXtGley6XErhMiTq53_7hy24qWwxx4NwNI9NyZDU8YUVtXGncDhHdAsr35nIEYHw2kLoN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=O5gzquJErXub5ybjpB6NztJPgcUMQmC0_0xpJksrFtDbRIhlCXE1W94o5bDoX92uvGUeFKzn1tuSBxuokJeuzEOXd9AhGm23oUq3aRXcuQTGrQehgzdsoRKZGsPxQN-n02E0v_Y-S2LO3VYk2scx_493UieeXNkBu6F1a-c9yPkPDS2kEoxhi1dMB_MV358ZD0ddAfAu5j8B_lmb0bftJmt6TINPwsVcY6ZUKuzV_ITSPtm9b6NWNmboXVvHju_wIT-D32NosKDb0x3DXtGley6XErhMiTq53_7hy24qWwxx4NwNI9NyZDU8YUVtXGncDhHdAsr35nIEYHw2kLoN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI7Z2XTaugHaHJfQbFlw9L51KdgAg2vyphjV6td9URW-oP1cRzKjYqNpGKwZdNynV4ScgHhvqSuBNuApUvARG39nW1949cUcSx5lym6nqirJVLiQzkyYiAo8aG692xSOeYcTNfjlnR4UA0Tent_IaGJrbbuw-iN5d_OD-ueMtGCDTPwwNGq3NwqednSrUsCQVYykgWNsrQIj9cpRFVQee3KTyhCSAxJPWNGYMLF-JBxFAmewpeYgB2pGcdtE50gTFLOUtBeMWlPWVSP2-vR0lVB_uAlyGYBBGBJTwn8VRFH1itCOuhkvDFviNdJPC1B4S15hJJQGomE2jLShFk7QGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=ExplXyC7aPjaN5e_7Nbf36dhHCcsHQKVKmZIsH2reUu19YLThC0UWyMX8yI5zhfes78zb9VVueO-c6d_QntgAi8jBY1b7akBr5tlZuMku_3qZN4nXtp71o0_jE9xK5M3ABgF4K20LCKpQ3sZ1Cg_VhL5Eg4D2t_nFOT803tH1ncMKHLWyt4Ni_jX-9wHG_QVTgJYuwfqjj_X-DZ2O5pdssw3m4BtJEp4t8il5mKuRNdL-DDJZDr5Z1dyo83G46lqf2iqByS2V-QCaSqgX8480Nv083AJ_ENs-iE_RXlY1mC3nAiVbvgdJhJAn0YdbRTY3Empk5jGI2WxY_3D7NRcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=ExplXyC7aPjaN5e_7Nbf36dhHCcsHQKVKmZIsH2reUu19YLThC0UWyMX8yI5zhfes78zb9VVueO-c6d_QntgAi8jBY1b7akBr5tlZuMku_3qZN4nXtp71o0_jE9xK5M3ABgF4K20LCKpQ3sZ1Cg_VhL5Eg4D2t_nFOT803tH1ncMKHLWyt4Ni_jX-9wHG_QVTgJYuwfqjj_X-DZ2O5pdssw3m4BtJEp4t8il5mKuRNdL-DDJZDr5Z1dyo83G46lqf2iqByS2V-QCaSqgX8480Nv083AJ_ENs-iE_RXlY1mC3nAiVbvgdJhJAn0YdbRTY3Empk5jGI2WxY_3D7NRcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMM9X5svIBxEro4wDmnVZRHtfgfV5i57fw0nwjBpLsnVuboJ9xZSlAxBieBOzrkiZ6Uwn6Qwf-hpNY1fHgzemk5XMqR0Jc4e_vpLM2ShWlbYl8Arodtg7saJ2hwYVi_5f4If045naP0AAE6o35Tmhg9in45VWxA2C5-svul45jsruVih9uA1FVAMah3OM5ukjM4YOlrElvk-IVEQgPNNKqFuOMsU4pTTPgtWsCAPiJ_PmGZuyG3hYjOAAM-3oUa_eLz95PN5ZnMwRB__2HaXYPPMNqns_DwZFtowaNIMrcovmg7hfpnINsPcEF3HqlaL2X5vtdXEcB-W6pHzQIATrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFtDdl4f12L4RsNQ4PhHF-23V0saXLzO7Cyn0__US6ZIzcPvvTRFeuxM-rRWvEX7jUCVmWQDS80nK4Yehl0WT9t0w5psZ1paXJWG4HEbHg4oow6vtLYJQqIFFZh9rUOcHAMHDUwCatLNm1mSxiSwQAWLDOwJXBJBpUi2mDmZb8H70kmT3VDCRLF8jWBa_9v4sT5Q1ICvg0mi0Bu2qL-Tav0gb4Fwu5bWR8zL5UYZNmODV7eXnsLZDrE7t09XWIGuB1kRN0zXFHbvxohGIHWJxLyXGOzl-brh7e7mLbC3Dqb-Nz45EUDr1IXer9aFVUDyKJpfNRN5D-7atCRjTZY9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=cT_iG4-4kAievd9Ghtaj-AfCJmFhtJS7f-WD-KVtiCMd6E-RzbCl1nN5-uYX2pAUQ1kQpf7rK5Q0CdlkA0t9GM51NF9PzHT4YAIgifl_6o6yUqcf98p5EBFogbs5s-LXuGipx61R-3Xs1LjrEM9JW-s46ciqo6Zk4iRiO6PRa-dqxaLT5mkXOlF1cIjTd_DUTmC2Cq3VinEqPxiv7lZV93OJOeULGL1fYob7zGhk6YhGiCGpk5FcKMibcq0n5LcHeXNdbDZEZvdU1JiwekAmJMNLvZs-T6zwW_oMjn4csXO8zXKRnimX5-HlFKtG4l4iX0mlRSR0xMzgXgirAj4aoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=cT_iG4-4kAievd9Ghtaj-AfCJmFhtJS7f-WD-KVtiCMd6E-RzbCl1nN5-uYX2pAUQ1kQpf7rK5Q0CdlkA0t9GM51NF9PzHT4YAIgifl_6o6yUqcf98p5EBFogbs5s-LXuGipx61R-3Xs1LjrEM9JW-s46ciqo6Zk4iRiO6PRa-dqxaLT5mkXOlF1cIjTd_DUTmC2Cq3VinEqPxiv7lZV93OJOeULGL1fYob7zGhk6YhGiCGpk5FcKMibcq0n5LcHeXNdbDZEZvdU1JiwekAmJMNLvZs-T6zwW_oMjn4csXO8zXKRnimX5-HlFKtG4l4iX0mlRSR0xMzgXgirAj4aoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSYZqSyVbbfIr9WMC-OB12R1UV4C1oxUznBZuevUaEbQrnmd5Bv-2hwq1HcJSVSAfe-v4peOk86dTj5Q1vhsYOVeAA1llmUOrW7NKqzqTe3a6w8IPCfZgjn2IbVrIsnDau6p3RWsClUR-b6nNXPWHg2fb0Zu5yMiooAXI1iCdYh9U_LWF_55LsHQ_a5x7nQJfBg3tUs5VntfwRkgPSFIFQRyrSJka_T60Id-FvCjZEVYwe_EGA_1TMv_ovt3BoyuKAc3w2CHGiNuqnYdLHDT6RUFqxlOPLNH4pXDcFSnAyLf2G8AQXkW0aBcYntOmI8Hn51l8dC3vLXiula3tb_QJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=WI-Tg-y30GNB2kyB3PPaunAgiAK-G6Xq2M9zGRWeUoywHEQbInVNFsgDIJUhuY_WKosXG3BL8pt1VbInWGfhEduNTOUOBOvq7J8Qwx2bB3JYb1R-iBYlTe-m8Uq6BI4lrLarAyuqbOwu-3wTqW11-twc_Rh5VE5pK1wEH3v9XJetk-r1oYeS8zUZVpR2YloeVHkOzrJA-sS1u6kV_Q69icK61Jm5uv5RMfZu79uJnJgEERD5TY47VN1PbxEP0WtxN5Fu8aPKzIP1FSi4L4GU3Zdi-sEkVZJ8QQKxoMDd4fVzt5RvPF8yDafdo-1Z-pUzOLd5-xAhOs09ml0aLx8HO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=WI-Tg-y30GNB2kyB3PPaunAgiAK-G6Xq2M9zGRWeUoywHEQbInVNFsgDIJUhuY_WKosXG3BL8pt1VbInWGfhEduNTOUOBOvq7J8Qwx2bB3JYb1R-iBYlTe-m8Uq6BI4lrLarAyuqbOwu-3wTqW11-twc_Rh5VE5pK1wEH3v9XJetk-r1oYeS8zUZVpR2YloeVHkOzrJA-sS1u6kV_Q69icK61Jm5uv5RMfZu79uJnJgEERD5TY47VN1PbxEP0WtxN5Fu8aPKzIP1FSi4L4GU3Zdi-sEkVZJ8QQKxoMDd4fVzt5RvPF8yDafdo-1Z-pUzOLd5-xAhOs09ml0aLx8HO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc4EfyrX7uBga12yzXHUs8WkM9SIRIu29_sLxvpz1jK7thUlwXk4TynWemRbEG9hVjeLn00ZZV3tEuH66kuJwvmpo1Y-TJVrfswN7-aT5FhGgQ14MQdrxLmLwXdA6m1UDgI6UmIWCs6V-7FTp6DDRcOvMN_UWG1whZT-a6MmwN-eZ9Bp_r6u5WO8ZTMgBUwMkjjkhN-RLH0xKdENyFaKQiRyHXRJTfWg7bz75_NJR9g4FqCIqlL8ryQ8Sz3zpTrD7RmCA5WOHzG9Wj3dw8dI5za1f6eaJ7Qm_hqgIUsJFlhPNQXgVO5UdtfWIAlqvthFNUnVpejm-yh2-wxEg_F-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkXV051yzgHAAJR83YcehotCKkWVRSZJPoTF5VMXm-Wh44DqqWpkrUvi_M9uAs2cLXCu7bFMcyhpmGgZEppVfKzOV4Iosf3-bCUPV7ib7-d0TjYjeCf746tD2trIXPmeEejHSrk30K--CAsVboacgWO0-CsgFp0CEIo3mIehonlxwgaCMPqCjAE2rlhEHJejCczCnowm7fFmQnbZEUv-f0nAXXjjo22X1T5fx_EoIBQLgFa19WntiDsaPZLiyKh9D_Va2AMeMsIP6HuSLKG9RYz8vvcTO3IKjvLNo8DF-ubaj8mxb5IjmDI010ZYr0l4_60mSPOAngWKHVFgj3wblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgzRiAsNDcNwDvjAG39xsdq6gYxz6Fe45ONkU-C9MFFJVn2l1-f_4JgBj130OLGOcm3UIdxULqXZYHfuctG7aRJ1IkRrBaOyNjENN4uf52ur2Vwx__R0xQHRDT29R8fwl8P5S3CgdkGCqrcWozIURCa4R4Pl0jzC8JZl8NbU3lOmzyQAzPKNOHmssFxqoWZDiO6jWeqaT3ZLQEg5SqZ6_QVhL0d68F0q4_Eb03V2OKmDdsYWKMe9RswOb52uq_KNAXKQr9PcGo_NAJ2ghFrlOLDBKHPBlBLlR33VC6VvUVExRbCV2zMqqBscoMOtBP354a2HcQT6ALqS7APUrHSn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=FubKMF8oYkQw0ELXK_Gs3O7Jjw_yoBGpjUQS8nHJMbCGMxFNc-UDDGo4pg1pSLegfWdkCxN6VXogZHf0jD-J7eYYSNsk5wrModtorbvgj3F9dgycZwwJntOfXHmfw8Gg2kNkFOtXQYRNAoU_gJbtv4YsfdgahxQitG0JQW6ysRAH1c3aRlWF2HnqvDYoPMeFOvOCpBwAhsr2Wy6oq8OtmwBroITkxhl52ZjtpuHjol_ulEagwHqelWVgZX41DND4D4Tcd5pXAmnxayCgelW4TiqkcHSMD688sgr6FamlKehFg5uddq9tOE6pOe2fhYdcB98R25SM-jRoCXHcYn7zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=FubKMF8oYkQw0ELXK_Gs3O7Jjw_yoBGpjUQS8nHJMbCGMxFNc-UDDGo4pg1pSLegfWdkCxN6VXogZHf0jD-J7eYYSNsk5wrModtorbvgj3F9dgycZwwJntOfXHmfw8Gg2kNkFOtXQYRNAoU_gJbtv4YsfdgahxQitG0JQW6ysRAH1c3aRlWF2HnqvDYoPMeFOvOCpBwAhsr2Wy6oq8OtmwBroITkxhl52ZjtpuHjol_ulEagwHqelWVgZX41DND4D4Tcd5pXAmnxayCgelW4TiqkcHSMD688sgr6FamlKehFg5uddq9tOE6pOe2fhYdcB98R25SM-jRoCXHcYn7zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=dZIKLOJRVTZGkLvqdPeDGhq-261JP10tAUXiZ5BmCCYZvflRP5jRKBJ-XMs8LyA8EpH51oCmGl5oexXkDw3ImRNRQ00uELyD8JIuhJQmBaMmjY9u3vaxjlbAlis0vjpBZFOq6dcTkxDLD9MU7zgCCQVVQBmEbxFj6eiu1xY0HfUMAbcLldHjb3UmN3h4A_7Aly1bvhulgRf0I3Nr-3CuN0HcQysIJKgspWZdLaQd_u77eSRJ2G2Mgp4AKOaxgDDO0GvU1iJRiGQKysbe-WKkrgQq5BbeYLIbhroeIKdmaXa6AUwCJyaNQ-q2Md1NSItjF5ayqI1_uvBI3HpHclAEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=dZIKLOJRVTZGkLvqdPeDGhq-261JP10tAUXiZ5BmCCYZvflRP5jRKBJ-XMs8LyA8EpH51oCmGl5oexXkDw3ImRNRQ00uELyD8JIuhJQmBaMmjY9u3vaxjlbAlis0vjpBZFOq6dcTkxDLD9MU7zgCCQVVQBmEbxFj6eiu1xY0HfUMAbcLldHjb3UmN3h4A_7Aly1bvhulgRf0I3Nr-3CuN0HcQysIJKgspWZdLaQd_u77eSRJ2G2Mgp4AKOaxgDDO0GvU1iJRiGQKysbe-WKkrgQq5BbeYLIbhroeIKdmaXa6AUwCJyaNQ-q2Md1NSItjF5ayqI1_uvBI3HpHclAEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyolV2tO0SG37ARp0g_I2BmmNtP1_K6n9zr8nkVkwrN85Bk2urzSluu84sxPNZkJWiYbOgjxfpPY25RRO5s1ZV0ojEOOliGJmtwoP4ltLCUjlXKkVAVIx3nCJ5_2BN1TsP0ugdtyHntOXvi4Zz4Ahu8TVq1HjQEDniCpL-muVOlzFS3Ay1ZSQYZJVxyVKoIlj2xkck8U39xRp0rUW22r0XtXq9Llxvwzkpl6LhZQzpSB4r3-wnF5hggkUcqDlr6LiUWmi_RDyDLUI_pC80wyaj_GPA3qgSfRnlhT5DG4BfeoLqOYpzuZbINMlUwzRPu6TkGJPEi7we1GMzEjfIyl2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0ywFHAwxftJZsYQ88xzEJ9RLRLNHkf7EJKZCqfah8DFzWs_pNDxm2gTrzasvw1sBi8qCH4YpYETFpxPSScHXMuKsume_uSDPMNpKxuDRBKZ1V2gDYCCj4KU7kHoyDjo599XtNIrF6RKG31aw9CFOuFOLzfx_LFZu4Nyl9ZkdH3clml81X_Zkonvyfb3wEXRQ9VqrmHcjMGyxMj53S77x6bug_HWtm1mhaUIseMgzjYk8CdjhIKc8sCJRNXI54BYldU4PknQzmSNDKfkCMjbmIBb1kK25MFCKwdNEQp72UwI6M5kXQwDpfE9HTdZ9EaftNZP6viTphT4W8jK-o2miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEwkNtBgB6UJPdyEFUzox8kj6oI_TMRqv6B67L6nKUgNdocwHlCJglWoKN7t3ZpZgoL9ILcD8ATqusXFpqy0I_BgEJ_AzRwHExuPVlAPQ195cyIH6BPu2B6cqtdsky8ZSMLwCiUndqt7IpgcfEz5FMXFXa6Zyh-iNE3lp6WUKIuIzUjvbFxHAa5WPfu9I14KBqZGD6aAf6lvtcvSIFL6Yb84WtcSU__euZN-IHvUY9bPAViYBqDJWEOHRY1uRgKzN4MD_07vOR-_qjwx7ib4m2_55Uto-z9TJKO2hu-hFomfbBAteZKItdxxgv-p4kVcCv2mv6QFnK0zZ5JtvTbZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8PprnrHuUj6P1Qunh8ppUTWApMSOHpzLKuAYrTMjcFwskvJjqgGFG_3DN6VaFKGF1AM48s9dqnjc_vpWID9NXH8vnrQFjnABOkmnPkmmjqWmxWlYnuO_cZlWo9VIQRtOVIhLP0pFX1SDNmgGikKz8ggwxia6XeF9MtGKLmKbCtVTbh-lsBWNJRrUaUibnDyNjurBlnyJ4bSSpmfT5WUgqlzC9iaZ_Ya42g415XFTs6iKR7XU-lLNDag6ssfKJjvyY758j15DtIy0J1mxnk3XP-li8wqa1pbe3bea-JHeeXg9idgVEelQvyZ3Xm9lrrIOglP-W49PI3VxM1T10YXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5iOohwdnf-G_mYVgJRBpgJaUPLDFsIaYS1Z6Fln5P-_hPiAsbXJVAJLs_AyZrS0H0rgkm9H2g69-are2oOSRCU_GTSitu76yQXRsfnrKq8m1VtyFPYmv2acCWiinKVxJmI5Im87nGSenY8lzfQe7686OJfZCjHEtUHikad2uAKzDl4quXsswYJ_ZSnswb74u3pb1YeYFgtYaYXEru75UUJGCnPVnwGsvR9Egigg4A9EOOXXinf2Ftktr5oF4sSssvdhzl0QYFPLcSeV_JkMX_opRfKFVEJlxMJj_kMUG_nHVShaimsDCiBxMESORq_ss4zBsTPQKrk-cmABTFdE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8W1VLChaLGrKD2_Y5sLsL9jaZnfqcZjvNTRjK331rjw7xZ2jDEm6DdlKk00fPgjyr0KpjaI9TFE8GuIexIDNKy28_hAfcAw-c636oECLjQgJO37K0KNSIOFtcS9NKRqYjWHqkacIG2btyaLu6ZMSoaUN2OGy1HQxp-Vkv0xXC8GvIynLMSHCNO2F6sIND8kmTtVDwvCD3e1Aa_pylEth7n21DgI7KnBDW4Ri_v4C16lk3wwO4SEsX65Hr3p_pVomzf0KIYQ7ybQKK_qXIeaZlK6h0rJlHunrZMAmwvV8I9d2Ffiiagmvge_7DCJumS5lM53E-n2CDcA-HxVXQC-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Iu2H3gnLgLov0a13u6c5tj7mjyWr7bdfAK6Aud92uGMACWy3h-uLB0qt1zF4eQSiJwTuVd5ojGehdlehlfQyP-QPFwpV8pqu9BJeWSjFwUNAFgplhRhn5g5NLm9SuQq2ZOBN-1PuU8bKaFTPIKEnE4CpVm413TWeNH4HcaJS5dwYG-MZrIIIHTdyhE2Y2LQZxJQvIe889mYQ3wdlHXp4RUoSqZtauz-gewslgJKl5MchIQFvU2dGLbBgGCenJvriDmFKgfGenUKck8SPmzskHSz56m29p78HBIfnVyebv6Kr0tIGMT4dkP3T_dkBEDzupFA7YuJWWrlhlwuTpStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=WYhF2LdHSTTPAApBx0RV6wC1XRDZVrbVFrSCtG6WT2McpkwvLx6wzB2_3CX7OdnmOmZ8B5zNaPnRFSC45tLBwMrdx9uL6XH80in0Pe2kE406PgyM07QayywRp4UrUwWrx29vJhDGlWEfiZw_CGUzmaJu36cLqTWI4Ba95d1eZLAgOHocOwJVhEQT5dfUlYQTnLBn7nTfx8xLFs9hYvBkQxOESU1mbf7Ei2qm8qRd8iY7HuiY2VK8Low_53DqopDDpBw3pi0IRigqO1xQ61tRDc-Sy21lZ3VMprR5Isi__xsauTWBQMadnSfs-FiIFFn4mgYvqh2u2oKh1IdowvdgUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=WYhF2LdHSTTPAApBx0RV6wC1XRDZVrbVFrSCtG6WT2McpkwvLx6wzB2_3CX7OdnmOmZ8B5zNaPnRFSC45tLBwMrdx9uL6XH80in0Pe2kE406PgyM07QayywRp4UrUwWrx29vJhDGlWEfiZw_CGUzmaJu36cLqTWI4Ba95d1eZLAgOHocOwJVhEQT5dfUlYQTnLBn7nTfx8xLFs9hYvBkQxOESU1mbf7Ei2qm8qRd8iY7HuiY2VK8Low_53DqopDDpBw3pi0IRigqO1xQ61tRDc-Sy21lZ3VMprR5Isi__xsauTWBQMadnSfs-FiIFFn4mgYvqh2u2oKh1IdowvdgUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaHlem7RMLEpQ7VddLiRQJniP1B79hB8dv8wIPzg8NmeITdtdPJuBr1lG7FscmqYUw4v3-FeZ-4qtK9RPYSoFtXuOWSiAMB_ryAx5MT3COtA5N8L_TNZuIFUZ9uYQFk8cvsOqloy5WmQZRLoxcbl4bZ79Va-FLOMy9WOzq_eNTPKfZIHjIItf79QfeuI1l3MovfnwydK3ChiwaSg-SkKZ7MPm1nyGEUJ9CGwB3IF0JV9nkyzRlK1Ky278d5dzrTIgJaoUH4-u6TXFCWgHOfXmjMGwZMKmQIQMnZHvWA_M7YL6AscFi3bKB3RolCAapas9vTYJeBQNNjRlBtzuYeQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwRNLmw9r2O1W-l3UNzm2bBiWQvBRPnVQGJ9a-rUwNxPiaZ60HdSWx9RvpiLhg_ExgD8R4-uj5GFK84IEsAydtqr06JVg6A_sh-Bznd0xWZ7eLGNr3T91J8UFbNC0B1dCMGx4dxpxzAqvXLm8vC6XOrRjA-pERVx5L8L7n1KX5v33xf4ezsVd9uEzfxZs5ajJn9HiWFOaBCXwB6KgVB3pZdxfzhbxu8oBgIrHcL3ktWKBD80A8vPt5j5eQiGiTWiqHqKEDRls1vDEw6z1C30WkM89kMx6BAqsM2omrtiODF_H4ot4ROBXM2uOoT16ejeoHcR-EyitTtg5MnuSSBg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smFvsG5HbICM_y9bfB0_TGwDXEb1paH9ySmyGrWYsWosKZQ-IqpIN9NR2rRgTbCIRaZQWqmoNmmMdk3rRTYYdkQX8ODI0_yoGy5uir1fRO1E7DqiHWDU81fC7G8zvDvvRdHV82DhTaV7d98jq0VPpWvDsPe8L18azwHAIlcxJfRvQ4xTD3j7HOpOWk10bYRYNv1v9WBOBJmP03p2UsWkt-D5kz684JWkpTYoFhqOX3drWf9lzu9_fD9jr4Tn0zDRtcM1I3pteElpv4cEFxWmDFXzypUnro94TjMyzwIaiQboC7dOVQv7Y2bJZAL6mxVrUK-NPDY8E1_9KLGmzaryog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VsVU_uvVOKKQgv5wFNJlrnFDgvXhZFSiSO-fyUGjEiBFv8AtpSs22ugUD4sbWN3b4YRBwjINUIHGyi_aAZ72Vf2iKGH_Wg5WMTC5llvN5IP-pjV6T5mRp0qXpWuonhUMcGwP9uFUFM98aV_xe6UKencl0tCN2vKGbW8zQE6hUv5ywtByr5ak-vL2Mr1Jv_DB8zRlo9qH2TBslt_FNDl2U0XzUXGuTGNEka7p5tqkjHiIZXSa6oVGpivek3J2CvDMsEYPuerybhoFAZ5e3kuHUAuDM1DZRZo_oQ7pGWioiYl_KdKc33MNWhRlBwPjJbQgrApoWYTODDqWHnmGQYyuAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V41v-5Z4wRXYGwJIgtqMQetaTG4orZ2-nwiPUYwK3xy4fh0FFuubP3Vo6PaZfutXgihHxGpNa_pLQGA2b8W6F03LKUDbmKI2KcioM5wF0AfhcDSw5u-FeT62kPGGrxk6NI4d-9UYPTbIzDmrUX9BbyJBlYQ5uEIUWEAr12lcZD3ErbiknCCh7A-FK8PSUtJ_wayHdWIl9fdcGj9XIrGHfyLWywOPxcwlKCaxGL8wrQ3K040A8Ipa2GQ7awSxT85kKprbfZPzJdx3B_XEJK_A0tHpkv2yQQtiJCGvS-dZPEpEhhx5qrdiTiPCiMVhImfXsG3uN7YhkMz9_hjP2pGfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=KxNJkYNjWAo3fa1liyyGh7ECO1iONXSKIImbWmM1lHApPQW5b2Zzhahoaz8C183c6m2wsOzgOF5Jp54zcgcW2oHU1-MI-Sk7zWpE44GACfU62hu0VpfHY3O4DBd9fDLlNxo1cSmLAJQvG5h7Laxa6c8c5wpKCjylvq-4RYxFUJ9YIjPLFDHM-NX-bMS-5HUI4IGH6qkIMg0FzLvcEtI7E-J2rEjLx9KqziDKhkQUuQQz4pAzh8A8wlohcBjGFAkgv76nVlW-e0lSLNnVkWA_0uLelcmfnXAYhdubVpHrVPpzEv-B05Ykf-ZOcqAuMP7uevmUNHNWGoTbYP8Sm0t1Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=KxNJkYNjWAo3fa1liyyGh7ECO1iONXSKIImbWmM1lHApPQW5b2Zzhahoaz8C183c6m2wsOzgOF5Jp54zcgcW2oHU1-MI-Sk7zWpE44GACfU62hu0VpfHY3O4DBd9fDLlNxo1cSmLAJQvG5h7Laxa6c8c5wpKCjylvq-4RYxFUJ9YIjPLFDHM-NX-bMS-5HUI4IGH6qkIMg0FzLvcEtI7E-J2rEjLx9KqziDKhkQUuQQz4pAzh8A8wlohcBjGFAkgv76nVlW-e0lSLNnVkWA_0uLelcmfnXAYhdubVpHrVPpzEv-B05Ykf-ZOcqAuMP7uevmUNHNWGoTbYP8Sm0t1Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=JVfRwREm42V9kjeaxmCs1cdrPxLkYUps8g8SFD7xCW1uAp-yG5Wies4AE3_n10hRZHDuyFjZesyWDt0fDtiCCQZP6gotrxmqHA6vad3ur3KoM6IlGo5OSW80eBOO6Z7a97jmuX-W-jUimSO8-HFH29vX6nIrPS49xFm2VE3vjin1guvRcZFJATmY4XYZ8Ixlcu0brptJDONNQa-9miPdO2zFOV9e4T5pWPWp6FL_ajzZKndN9AdFnX1DIGT3YHQ6itO_qG-WDYACm9vFeXi6jYMgh8t8Vxo7xWfS6yfTJPB2LopZ1zcy9DOGwMtM7yhUqNJugT76C3R33k5-dpJAWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=JVfRwREm42V9kjeaxmCs1cdrPxLkYUps8g8SFD7xCW1uAp-yG5Wies4AE3_n10hRZHDuyFjZesyWDt0fDtiCCQZP6gotrxmqHA6vad3ur3KoM6IlGo5OSW80eBOO6Z7a97jmuX-W-jUimSO8-HFH29vX6nIrPS49xFm2VE3vjin1guvRcZFJATmY4XYZ8Ixlcu0brptJDONNQa-9miPdO2zFOV9e4T5pWPWp6FL_ajzZKndN9AdFnX1DIGT3YHQ6itO_qG-WDYACm9vFeXi6jYMgh8t8Vxo7xWfS6yfTJPB2LopZ1zcy9DOGwMtM7yhUqNJugT76C3R33k5-dpJAWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntOuPuLvdUGtxUJzfCFE7grMLQlZ7D3fkAW9XbLN7fkv0F99fCT4dnjeTt5iI-UioEeQUdvT0rbI4pVVq3WnPYADF6lqTeCMmdJa4f217wYzAY_bLz9bEU12ePHzTvDBRe0Sf0P-OIHcX63G9KgHFrwMN2Fxf9sIc_yzTSwXw9CeSj3hovN1n3Fp6SZvdO182PY8ab7UdYD7t8PV0VO28TUzpV7ON_0DQmNPjkSbLH2PmDGgowyBOeKgqPtXpPk1N-HGYN7fY84grhE15isD6VbyfqpZP1J9to66KBcygODC4Kn9eA6eNv8RxbcmYaCxEgSMT80WI21y-uBzF7IMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaKJheUph2ZOBRx70seFGkG93Sd49cMQMOI8Ni-p91AvUNz8_wAQ_wBxu-9zSGHmH9s5asNsfcKHGkssarE5zRCjAf-WymGFzUX7nr4XIVtx86Im-779VxUpgnKy9JTGHe2e-ySp69kPAhBDNGVKNBV_NlBg8wNCTL136sB-bHvLPG2ke3-ZwtTlqBBTfjMZJlrphE48DtBzHaJZNOSldYwskGCW-iqfDTpyadeHsYGOfXbKBDOmaFgBMex6lEeBqZ7fxxGWSQBx9syOWNvmS0x4Cd3kvNsEH3pS8zNcR67tN_Yhx640LDp_ocGCouwlUmnKR2KUBli2Zy_EQHkN2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrb_EvkhX1pz6GrIbojfc9ixA3eylKhc2x3f1D8pscZ0c1lj5bNoyi6smELfDOeaexaMrmgW0Jtwgnx07Ap9VgS6t3GMZH_rPLpOq0Ky-4ZhXZqGsNt38G1ULB1lm9cVKwlTVrqiRe_af1IQXV4Aj2xtUq-Z6WnEnWnJXu98gp2YMWEckrK8LTo7RdnkXDNfJUvaC4N1tiRFL5ip-U3mM9KuyVP2MPUGoUkn1XX2gZbw6ryjco2CamrUwaiah2WMd2ATDQU4sAsZK9X2S2qDzc27e1gT6PN0nAVEGsie4kbBYVShaSx3t27XpQCQCus-vvqIRDWNUcZ5ScDDvChDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D81mZqT10wrczl6NUz_APKKEcRSvX1t9ReKP5w5emhXLVNkoeFkMHpqtx4IIjC0J9aUGcYUE89_UA2pDHXnr7yBJn95A_fazpRJz99m4N_gBu0vw9Qve18NCFk19cMvf7DaeDTJ_C31P9U-CvuHVTU6tzOI2wwEpGIboESK5pOogZBQSUe7se9EXzetOeVKN1AQxwS67FM1kt5DYuboEHPrSEj01Gt05rztBgd5pzOhQsNjw-Ganu-iWoP2YG4R1qcIa6gI694__pR82TTU_vdOoRKkbV3ZxLHFeagV75Zg9mMDAoq4pxVCKm2YyVuBm41PcKAB5miM-ZstyboIH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydCIWGxa6n2CZ_gPRmD0e7YofNR_iGsC1NL9ZPqjKFFmak2quB5_8jBu-FjMziI3z68lfcWgkJ-z83_2ia0l2RcLD7yyGl4w0vVVQs_TCkTHGzR3jUtyNWh2sTJmZKen8rRDq1xTyl6Sj-lvMuxf3xD4S8MteyakZt9CWa-RateYga38cz7j9ikmiDZK0Chp-P_y8CS2yefuzruZ-yKHI3iIRZrwS7HPNxFZ57OIvvGHMydUE-oW1G7fs-XFm6PnoANCghhHxqYzCwrA8ZFvCDWgUZWTd7v58Fmj9rM7VaTGhvPUwHK9f_9MRgk-bJZtkx6GwWV-7NbO9wRNpDD4GAso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydCIWGxa6n2CZ_gPRmD0e7YofNR_iGsC1NL9ZPqjKFFmak2quB5_8jBu-FjMziI3z68lfcWgkJ-z83_2ia0l2RcLD7yyGl4w0vVVQs_TCkTHGzR3jUtyNWh2sTJmZKen8rRDq1xTyl6Sj-lvMuxf3xD4S8MteyakZt9CWa-RateYga38cz7j9ikmiDZK0Chp-P_y8CS2yefuzruZ-yKHI3iIRZrwS7HPNxFZ57OIvvGHMydUE-oW1G7fs-XFm6PnoANCghhHxqYzCwrA8ZFvCDWgUZWTd7v58Fmj9rM7VaTGhvPUwHK9f_9MRgk-bJZtkx6GwWV-7NbO9wRNpDD4GAso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4Fox41FvyujCT6sIhB59dwfp4LpGlABPiX6aoPHI_G2zSQwNtpIzBXqNkwYyVGekZWerxu5avcaYSK1zGhY8-w5MZN7RGjgImld4HHDqMcDukzsJuBc7szhWS9SvaROWR2Pr1Un_knINfjDi1QNNKv6wF_xChg8KSrh7SLtJQWOg7WuBzIIbZ3OOwoFHBvnSYmtXBHv-7YCaSkp3_TzPnaAVu-29n1K4F1m8FTYSSTQAmQf0TqHstT1rFxnBvcsVS19S662-7LMNAr3RuNFmnvh6TDPS9zo5x67I2W6NyWnSr5QcBnHkZTabJjXu0xFXhhN6tdgkkk6CewOEeu4aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXwiLRR_cceohdq5yc6J334GcBD2Es6aBUXg7L3H78YNbQ7tOMsZ_9qI5kvAzP1Aw3ABPpROeskBhX2vIhzqA1zbqorDuLbsDEcC-IePMSF6mxTWUg-B4neOQzLkZEoya76CL6OHZr1dyjMzWCB26TiZlPHqX0_qmwuzYzfOD8EV_hCfkSAq4gpAKPnj5Z8PoPpBYFc6WbHwtxBvyYz2YmgxPRs6qTaDZRtZWm_U_cc1eQ3LnB4mIjlyyEQYDZbijo_8Yfs1Fb-873VZMd8fmD8aQSZAzxLDLheLRk4Yoi_zhe8MvuDRxIU1dwaRNZ-3sa1Y3AmPdW6ynNAd_P6x4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAzhpIbSFHuXADlPWEGEHS4L7eE6mSZ1VK_J39BWoaM37q0cRkRtLD0QQ_2yVC6FYGVha3avnqptS0TGiI9Wp8a7QNjtcsADWtebDDhAg8ezCxm4WfCRxh60JC5rOqhVO9UtxF1SEXr6aGb7Pmfz_gbrhEtX-m2fKK1xKjjaxFiriLPwFUf0dWdGlQQiA8MXzsS62QH_U5BTTK1k0F7s_4XMP24lRUUFRhNNJKWaRFEOwF9DRN0_5_o2qn-_miE3aW0IhnTsAKS6naS4bwni9_EOoDaYx6nsBAFzp51P-8oFPKpZpGLRaL0FZgBTlqaVCMa_36RDbbX919Nad2MKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRUBC8G16Fr06B6OsaDpyQkqELy6PTh2w1qLhuMOCfj8r63qOT8GnclVw_BQgM9E5jJvXfWoLtlKCw4aVwmNqx8-m-BYm6AyBMSgg5FfCD-x6LV37H5Int3aC7VaoQVpclCaTvh-7LWsam1I1ZTQDPn0GYcfEfHpXkFYfscIkZW4H6sglaEhKd-P-sxPelZTlFLPl1t26R6lMAafKFccDZRxNeVhAp793UksAmn9s8QwkzaTibO_LscjbdphpMuZ1j2mkk0R-KAJBL7T31RXd-uURms205l0yzyRkY8h8_xbtGtAuOGVJlue5Y1U29oFenVbGwZLyM_EjW68wH-iKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=DHsDzfFefpNqkkHPGmjo9LdOtEBcVP_LKGvNKNz6acaQuwc00e-Gzs6iuYwBKGLv_WxxE9LfMSwzEY4FdYTV-t2tpWlvBjVimOEweD8ThjUuGIbeQeGThjoYIy8tYo2CbHSu7ITLSiyykwFdnnoOt3on1u9AC4v6XCZhG2AIam8HvMJ9qM7bzdvvJSt6cP67fbUTkRWw4xmvvVeG2mgdym31moDfCwy5LRbPtevoxhoohpWkGZMiAU-jAPQ8O0lKfXnAPSMCChzMB5UN8jlJuyYsjLOcex-kjpU5ICxKhujiIdUHDaZELuTprIf4ztcztpM41yQPjxsntgIAjWulxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=DHsDzfFefpNqkkHPGmjo9LdOtEBcVP_LKGvNKNz6acaQuwc00e-Gzs6iuYwBKGLv_WxxE9LfMSwzEY4FdYTV-t2tpWlvBjVimOEweD8ThjUuGIbeQeGThjoYIy8tYo2CbHSu7ITLSiyykwFdnnoOt3on1u9AC4v6XCZhG2AIam8HvMJ9qM7bzdvvJSt6cP67fbUTkRWw4xmvvVeG2mgdym31moDfCwy5LRbPtevoxhoohpWkGZMiAU-jAPQ8O0lKfXnAPSMCChzMB5UN8jlJuyYsjLOcex-kjpU5ICxKhujiIdUHDaZELuTprIf4ztcztpM41yQPjxsntgIAjWulxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbrHu0lbPG2gokeR-GqMAC-QJocGbvABvf_Lk91KjeYsKkugATajj5aQBAfpF-7q3fOjIUnE7ad94SUJQ0NefxJvP6vz5AiMz5XFkWQxy6eZPMIZ81UiZmOKbrkjxF_l0SO6p5bUu5XJWrnwaHVAu0Wdp1gFjEdSRrMDa2BIoiUG5BEsr09VO_mwPKIutxSimhutintPuACkSWcrO9WE4jfDMFn2A55WrtxIMBRhlp4MJhoC4rF9dlKHn09EfoDakLkglz6NNyGMqXVSifWe4NO1iJwcGvMOCd07xzfSQ3z-gipcWEBRNxvk1n6MOVAbtVYyevk24RNHE_-FIU-ZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=h2scl1K9SElu0rhcS3nqso4HkvMleBGpKBw0Yzl5RfPvVsBMa-5QEg0RJ387b13FZpDMv2sh5i7sbfd_h9bm5il3qV73Nre-iXzngbucQoWD6gU_hiip2gFaer5q6mk9O6v4jsia0_w8WQ6yl5J-oOd-93PFgJTpuRnW5H_mUXyMwafIAxvrrdJGkELKiOYmPbdGGYdGksJrCASs-EfiFKoWeioE4TggwUfGzFHc0tybTCft2SGkatV1bMQ2uVwZNIjohj5nZCN7Y6yBapvSB-Pm_60xqDPFckPFCp-INPpwxFu6u1DW2gBOV--jfu4wajMGsTaozpYkrqIowz8c_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=h2scl1K9SElu0rhcS3nqso4HkvMleBGpKBw0Yzl5RfPvVsBMa-5QEg0RJ387b13FZpDMv2sh5i7sbfd_h9bm5il3qV73Nre-iXzngbucQoWD6gU_hiip2gFaer5q6mk9O6v4jsia0_w8WQ6yl5J-oOd-93PFgJTpuRnW5H_mUXyMwafIAxvrrdJGkELKiOYmPbdGGYdGksJrCASs-EfiFKoWeioE4TggwUfGzFHc0tybTCft2SGkatV1bMQ2uVwZNIjohj5nZCN7Y6yBapvSB-Pm_60xqDPFckPFCp-INPpwxFu6u1DW2gBOV--jfu4wajMGsTaozpYkrqIowz8c_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFhn_swU17YRXjNYxGGMqq884W59C7svUIj9-I1A60EyJSJMpDG1Mt5KELV8uxwILdsDIgUWRUZhKBGBCnOfjeNBxSyEMwcy0NUeoC8b6VBlgj8qjpqQIj_-NSxwDyCK9tzkbVRdCAJbVcxwurUl9En638VQjou9qGkazebcaucj__iEWOKXDYT1pAaAQwZ-cMxh7tJR4jXQ5wPbW-TipQXiammWoC438knqSggauOyeGQBIMDgKJZ-ZN1L6msHzMGhvRqhwDanoK9pU8C7mEzWcfojG8MZsC3dbccH62fUZYenqAOhTcc6duhuFpvjpePyimjqZhZuEPQnI37hYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pymnKb7RFkH3UEos6vGyKA9mO_He2kbNKGCTE4XyISB8E5y8--xKdTGdktTqzmHe_OGGXivfb2rDobNGUEvm7P-URwR7TdcOdnnSJ9WFZeSsxB3L2McuC5up1RzIa4PRdXsXpRnOQraiQ3szfBR65ZZc01UP-CoaZvhQUYxlZ9GoapmUT3-eHdvjdP76ivE2i6vBR7gIajbGpOqxOz1gbdrxSLIbdeLj3g_50MoUkSL4zjLoRs9xPtezTXxEZpQ3-7m_ob-t08qkSV4UaxUxIitfRcqnsAsGRysNtavX2Mo6LO4PAWxNVJVncVhAwhzKnvauetxirfoNiOf2KK6kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCiUyoBNVVsspDwxKYJuNTMX0eg1ug_f2Mxq1geuSqJXXKOukc8-CDY3xKdMIeWANwDdIB6NsQBqcpncpU00pWNIuCy4xhxHNam2jnBtUyL4MYoGwPvH_i5XbzCeNnzyk_vsAg2RkehnXn7d2uFHezb7sOasFcAetAMylhhi9CYY5tdmLMil-Q3tE1h4RZh1bpdMo-LyqducVZEBdUkJb8x5ETZMNabns3TItrWMUWdRQ7xx1vCjUdLlsJfT-gU1OBNIragn8BLafpqIefSh-SdZ0-DH_oVqaazHmCs8KOwyv8vlYt9IzDys-cPuYwsP0Td_R6eNOXe9FL11YIpokA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsUffxITHAu5ezbv8x8WnTiZbTJtW3o7T8k0HLr_fQzt82QTX4v-XwAn0uX81XM1rHk6CdVnWu96pe0I1P316pnmuc0NsrGUPh8kyH4jTiwaWQB2_B7cpk1eguUxNut7eVseZgn7BXhHqTnVEgLNatCue0sM_aJ9wlzXFcY-455VB3vJIn5ueTqsbrA6RsmS6r2sBWFWprfMjN2vEKkkqUD_f3PPpWVXT2rqsN2u3UHvmN_zlHZ2tnDBhBhGkFragBo5vvRZEiqcRKU8wKtkHI-DiBBOD6sN-ZbZF-me90k022ncJvT1yFG7HcBCk0lou33YymUq201Gsc7ZjgdxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOOptRQ12rhCsbPTpHovaK1j9q_LKWjy12AMa0qM7UPfrw314Cv6C2EE8I_L4Cvt3rYO1UDJCGaPQ4WWYiG5gFKzg_P45LV3bbZJol5p2M5Gy2GSLj899EgtuI2GiM_SORnW4nmJtTgoGRkE-DmRhILfB-NIjqdtYDuS_kKz-skzholWtZb97HzBbGPYvS5_NAzyyg8ccJ3MwzYElyeyHvu9Ua8KpK4VXVXdvf0xpjPq6bJitlWBQ6hCkkNKISOkKrqBAqjHps1W-UAIh0sZ2ht0xuIwGw1tG7nO_YG6LEUmFpC92zeLqthX1ehgkrOC89nEed2Z4w_RNScwFb9Qdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJqs2K5_xm0GgzaBDE-AzH9gWDDODcplJvDKA_MU4tNRPWAjv42MQgD0IC-thWRHGstgWzKgryl71XdmI2Lo2ujmdFhUVYaJCV0AUMd5QN6FCINrkTzFu9Dr0IqF6ET4IE6ixN7GkrbB32KUnXh7Mjqy4wUdb4Y7cn2xqD_RAo56fvuu3Yz3QgkJzIEkQxTAtTRylX1BuCBnyAzW7iM9WtKZT8Gszruk0b1hqsZg_psUfdtKOuqZF9GDxrQsDeQs03yOymIrCwOnmgZmuZMe4vF0lBhmKfXH32k9Bzp-Ot4SeaMUOw-BF6Top5DVdXRKfKk0fy-iu0sRi9Ez_1de7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRQyufIYsIW4aQ6XkuHdeq7zO9CeDsMHZdz_zo-7PjyK5XGcpt9v5FcHdf-14HB6x2ZPEKVHl3KxTgGHQSp7dKopoZcrn6jZiEY3ylE4XbpZ0LqFzGUJ74vHCO2AOyxcuj6tvNKi9LNyLmha2sYmMcyGUgcmJBtdLVjq92BJ7gZv4j8pbpmfOE1TSUQCTXJNbo7NeuYXIb80MOGgx0y39U3bTm_5GHL1C-ac_okR1aQNGBgCybr5NEaVCWds93CWaIaqxYxoqMOPTb0Zts8MR0zSwnX2EfS3iD5RCH4qXkSUWB58XuQxbd_woTQKI3_UgB5mK0_wM95Pj8BnTIgFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIq50wDqSiArdMGLR5VPuOFzn5tl-VY719xaZstMP4_tKvVjqpwNyrttPe2hrKvLEoO9eu8EU-qUIXysQ_6l2UO49PtWYiLGqYlWAYSWv_kBxIwl6XQEipux61fvCU-gISlHu3b8y3AplgU4C5PZZar4azBXolJ6YnORy_zLGykZpx1OZR05-SOYe1vL8C31qG1gqB2AM-2Uy2vZUfF7v2tYUHNhb2HXRMY1Did_wcTVTl5tFS3Q0PbXjH2IH9RbrNukmHGevRojw3W1aFrlX-CMbtzgDEsTiHZAW4sLwgY9H0fN8px4t4ljbXp9zC5ZDtMBOV7XwMAu_mZIE9FQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIiNcIICChwrtMjSxAkidGlUGcZ6blJIEmPyNN3zFhKIHVgvcpUMJu7CWiA8TihurcHGa8xnmfrDB8UMOhpOG51d9XM2IInHb4eAe5-sPXMPB8M-XdNa1xuILtRXiqoc_y4UKagn0IEJTjz8zV-uICbc3qiR-Lw6JCoBeQWxXO4wOtA6b-AQmUhrq7iqPllIsOzFv-z0oVQU99t_YgarfuKwPHRTEtFl02j056xxo6xB48E6aPVLVs5dAL1E6fKMdWn-wBQ0RiEJeT5s69BxyZzhwHOC-IiTsV2m7j3EyOLd7gZsGjA3yeTDdLPKCIhQ_oEwR7odl2e6rg49YFebMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq4PuakBefxY6D2BkLouZp66k0l3qoRWfyeKlUjsh20cIKTyVt-_5kC3WDfF4SYnpIsz1bRUzfx9XRjB6I-Ac5-r79Stbrdr3mP02d3W1thWityYEPSzreJlHnQRLboypkwy_LXrG-4glyFMKXNJhj4lCfeqB_JwV9vifUdrR2f0Zz7bcfJwhy78VcX7_r4b4r-o0oihQeqZroGZ0ij82zor1Z4BRAWHYJlZJ_TomrJ0DgdBQvtp7RHOAkC5WI0L0F3HjfXj0HU6JeUeDV8Tb343FqAxjvf-BMdJMvlX2anilwddtF_2jQs36ypCmNhNfuWPI8f9ggvoF9BPEDk_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=n4u28E-sxdeSdQT_FG6R_o5o8Xy7mb2bGImuIau3VbzYXV6Y5L5jOCPDc3O01clQWsNwy46bDzFFKsCjVgoRlH-ikn4nZWaE7VAZImnXYEhA430LDyAcfDBLcgSKzKN-TxYRwXFKO3NWap3558frlN0KO3z5Siru2SMjoZRIvC0Ys2rznibLNJd8PMzVtfH3UmfQ3wyiQFMvq0ewUAYnx_jNXAMJ2dZ0tycEXPJrE5qr4K57vDpQRhBcpWqPyA4-5M20K0DgaId4k85SkmG-aUmz6H7J2kmBhBa2fufqEXH5WnjYDbzt6tdAGqXwWBs2SA0byLXkow-TLzJdhZC53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=n4u28E-sxdeSdQT_FG6R_o5o8Xy7mb2bGImuIau3VbzYXV6Y5L5jOCPDc3O01clQWsNwy46bDzFFKsCjVgoRlH-ikn4nZWaE7VAZImnXYEhA430LDyAcfDBLcgSKzKN-TxYRwXFKO3NWap3558frlN0KO3z5Siru2SMjoZRIvC0Ys2rznibLNJd8PMzVtfH3UmfQ3wyiQFMvq0ewUAYnx_jNXAMJ2dZ0tycEXPJrE5qr4K57vDpQRhBcpWqPyA4-5M20K0DgaId4k85SkmG-aUmz6H7J2kmBhBa2fufqEXH5WnjYDbzt6tdAGqXwWBs2SA0byLXkow-TLzJdhZC53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=D1yTg0rszQz40PB7sOfmyYJpYPyK1VaUf_QANtPj6YZ4V6X1jrYz8wUJFkuoTgsplk-QHYXTWMZfCC29de5wHbrKCRJPr5rYc1OcbgeTki35Bgrdo_n1u2f7bPqVzbcDxSqtXVExqy6AV2nKbh7UOSS-imZRQ2rNjDmWEzJGVXziAbk9bn4R21_GRKR-nKBisLsu5s2COfgF_YfYsyb9tke1-T8v9ajcfbPIZOYfggdSGJP_uimrl9A06xPoLYnchKsRrCBbcA6yhdS7wS2_YRFHOU2Q2wltSpXzxH5Fov15RQx5MHBh5tZrsfk9B6p2JWCKZtJ-BX9A1LemI4Ew_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=D1yTg0rszQz40PB7sOfmyYJpYPyK1VaUf_QANtPj6YZ4V6X1jrYz8wUJFkuoTgsplk-QHYXTWMZfCC29de5wHbrKCRJPr5rYc1OcbgeTki35Bgrdo_n1u2f7bPqVzbcDxSqtXVExqy6AV2nKbh7UOSS-imZRQ2rNjDmWEzJGVXziAbk9bn4R21_GRKR-nKBisLsu5s2COfgF_YfYsyb9tke1-T8v9ajcfbPIZOYfggdSGJP_uimrl9A06xPoLYnchKsRrCBbcA6yhdS7wS2_YRFHOU2Q2wltSpXzxH5Fov15RQx5MHBh5tZrsfk9B6p2JWCKZtJ-BX9A1LemI4Ew_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKeeIuSQMtkemxGZAM0G0exkrjkL24IJq7qldR0ITlxQEhd9SkRp0i4VbwspiGyR2jPkB8mTFCogA3qCwEVi_1kUWK41wCZB0eixXxYYaLcO9-Cs7ErETQOmLNdHqUCjg7EsaYolo0BPVg8mx6unfuUFUqfDrm1HntalzvH2auoRiMB9eKq1xmjmlZsOmn8NFluuEK3cckEvqaL8xxhG7lJdbaid5Lf5dYA5sXu_gJVdIozOHcqy0vI6oKAopgrHftns5_U7Y0RYG2Xw7olRXjdwRtRYKTCMjNWl569U0doSbdItgnkMpMwuKc7IfS3Wnu3eoaAMwXppUN5cpEslLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ3Y0u_vhruPm6L1y2ZIGf1iGGFl6N3IRYnQPG3WzL-2P4XqezlgprCjOm8_knjn5Rh0CkERYK1MODbBW2bbzNknd37nd8iEeuJQ9BLIqhanFBmkdOVq-5TUY05FztannPZxFjk_N22fqXHynTxph4zSytO2OE8QyvWNRSkc70vjcG0HkKM6Gs4cZsVFITGcS1yb4S_QnkYF5n5DiZOQYa0DeucTxBofd1CHNjuSI1s6h1_1Qo6f5KkgSG-k0pb_SZpLnlor9TYVQSCaW0QG2CYzpr7tN8Fmv_yzLll5eoi6ApRHiQai6hDfqesyu7kBUgXqRQ7ARjFNsLQtjkd7qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNeC_gISZVx4Z2MPu2s-EoeSQnPjj5UprFk1-1l8zCYCWZwmjdV00wHZIde5dt6yvwav3ntKI-T7R1eVTSv3xSRsrkSPKLEWeObhl-VkHIgH3uN6q2R3PXoyVfO7sLp4VdJAQSrn8O7504GBrfKzHN_2yQo2qoScs1-gPfzEwRePU_FkwEgIIbiCvWpKwHtPw1ZZkolYw0DbX6hpSfA4BoEZldgVehTCR_PLj6PlxsVRZv5ftHq3QaHgKE38eCfW_rtjHh6cBQZSdNg6NCVOK4rajVTb6Ed1sJegF6S-jpQpMdaTrSVTz1ePjWjw5qN9sYHiItcExpwOveZXCcy7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEBHRoUr1XHGGQtw2Wb3z6UsCMX40ZE2cjdqm-34898zyBD_oer20lzf_d6xMc9BRltyGdHYZkeGQs4vn9VYlvuvFlk9VFuoCinWdKfm2ConUu5p1Yw_BO-_iW-ryme2fDsP2OsZnLFTSSzSTmwWTDqBBLC7RS4m3-HXenPksjKTgdJCYC4eN3fqE0bFVWMPfqTLhl_scyDQYs89iB-q2pyaTvEzcew_64mEAa8WRApCFrkEIrGnp0J09Mglx4l5b7G1Wr8p1KSvabbXNJJCUDi-erkYybmXE7_IA8nS7pXTgrO5WuwYtssgjddvE8DekmgZxzwm1buOlFS_r71KlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJoHGGJkFMh5yAL8QYT3QFFdUOEte4c5xelg0v9UjE7mNn-PtfyIs9VxFSUTPoiNDzoIVg4OL90d47hsKKY6F0Szh-LhSCAcSKulhmdT-aWRZAvnMj5_zJ7nmIs3RjWfdL6y0ah0FiJlkJOdcITKFhDxK7EwrAu-msocEE0LvFKJEeMlUOYRqFJshEYM_YHYkSqnXMmfpPEvfFBcXnVqoGiLPu9iHhaP8KU8MbcMwoH7yBwdpOJinHhoEhe_prfBiHpk79oACkUuOCHHtnofxsgcLjizFB5ew8Fa8QTojftmh7JgkGiVuWmUfk9YG2VyZIjPgRmwCNEpXN6yBMjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=u6Z_lWJaxCbp_ISKtVOkYGbuASF6Zoe-8LylZXECXxkbFqRv0b6ghFZF751T0W0xopV1Tc8PodNWRNDzZ5DmtsZ_aoH76PJuKWjusQDL88jTfGaoU-phSsYG_dz0bTYFYLPwSuiKlSst7AzfBiSr0niBE1SG70Hh21TX4T9out8iCIm_hLh2TEmiIhe4iaRwxRvP8nmUnyv56BaIrMIE4iUVxI7Re3JtwtZtLyuVlSKclJCaYW-r5vnUp-C2oFPEHiwdTfHBq8PF9d6XBu747asWER1Pgwxd81HO0vBeexi-tehZjyhErZOF9v4WYOOuyqpvVwW7bFdavaDCzX90oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=u6Z_lWJaxCbp_ISKtVOkYGbuASF6Zoe-8LylZXECXxkbFqRv0b6ghFZF751T0W0xopV1Tc8PodNWRNDzZ5DmtsZ_aoH76PJuKWjusQDL88jTfGaoU-phSsYG_dz0bTYFYLPwSuiKlSst7AzfBiSr0niBE1SG70Hh21TX4T9out8iCIm_hLh2TEmiIhe4iaRwxRvP8nmUnyv56BaIrMIE4iUVxI7Re3JtwtZtLyuVlSKclJCaYW-r5vnUp-C2oFPEHiwdTfHBq8PF9d6XBu747asWER1Pgwxd81HO0vBeexi-tehZjyhErZOF9v4WYOOuyqpvVwW7bFdavaDCzX90oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh-Ep8bV6DukZrINtFTuzx5whYUXZ91rf48OuUY3udHqDocHKccQpXQjHmqKx-BOQUYbv--MsrR0z6kXwSW1D__-6djc7uC9J4T27-rr89QmE-f225uAvGQiYPPT7q36l7uZ0JRPAu8eFMWXcZqAyy3EyqQlMoLMkfPYzEc6jDbgtMZGWnZACtYDCTchWjTs_8unGZdFBlooXFteo-2RQQ9He0OkNALSmHmDoLRS-mqrRxczYDhkoqqgqxWfF9nXAtkqQ2c7BBzghSYggiIoPRhUHuU68_1xq8Gm7SIhs_RKTA83hNNJTEHEDSii9DRkguKqFdREnIclhmeEsjXttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=rd3cx5ujJ8_zU5tQaeuTJwxKsFwV0qjvHMu5yLHoqx7h6aOXx4TYTQ0NHnVVOIa6iu-wnn__7bEj6LBwl9TSxnVsUgxiM2oi42HZNLXxkcI-51a_hyZcYhriptl6DOyK6ds95KFmg0mJ0NfWovCf65_ZsR0rWtjjbyQ_9clGcIcTJn831mN5_ULVmOuW7CpuG5jR7oo6wMSFQD9a52H_5jLMgb_hsUyOnM4dt_CvqfpPYNBAW75deKAzk7nknaNIuITbnK5XRFmk1DxKeOAUn6shwXroXah4jMLxWNRP4-yQnUijghumgLi6gJKN-wujz_JJw6r1RU1ExYB9P7ddbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=rd3cx5ujJ8_zU5tQaeuTJwxKsFwV0qjvHMu5yLHoqx7h6aOXx4TYTQ0NHnVVOIa6iu-wnn__7bEj6LBwl9TSxnVsUgxiM2oi42HZNLXxkcI-51a_hyZcYhriptl6DOyK6ds95KFmg0mJ0NfWovCf65_ZsR0rWtjjbyQ_9clGcIcTJn831mN5_ULVmOuW7CpuG5jR7oo6wMSFQD9a52H_5jLMgb_hsUyOnM4dt_CvqfpPYNBAW75deKAzk7nknaNIuITbnK5XRFmk1DxKeOAUn6shwXroXah4jMLxWNRP4-yQnUijghumgLi6gJKN-wujz_JJw6r1RU1ExYB9P7ddbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njw1Ywk_c3teLFSCqcaDXrOlt2WjXz6E86RNhjnBpljWVU3y4iPuVkm-YXcmiEyw5pqJpSRA-kNqeP0BHwfehKMRu5oIvYOQe-T5ohLp1nWMueQq6xcI92BImdfQzdgLRb7RbkPB-YJmwCCr2u0PJOsb549bNXKQlgYYrX6rXCJdrFc7tNugTwmsGLiZsHHENRu9RssEqu_6KqwpZ7tRFoclzU4wtZcc7yFhpvLMbGmFesvbMbo353FB7lmD_wGBb_fWjn-ArL5USP691XkTDr8jbRz6Yd8tFimEbV5bVlNP32a0-yUfeRgYf8U1ya85Wjnxhjq5GQaycBiulN-AkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnO5_zON0z86XVMGA3l8RboYM-obST7olybk2h92akLRoayaYLqfASYKxGcSDDupefxtzb5IIOrrG43P0n4TW6JWdYAb5us4THq9hCiKUlLqxoQJuh0dM7-8567K4QHOYs_KKDm2CW3kE1MLv5bP5JhyltJVQBdRUh8r0BiyQB2vaIa1JJfy85VwPJmTsk6J_MXTBxgLm2oKyEo8PyOnZDSe0TfgW5MlFB2ah3F83PQ5qGlbc40w0s8StE5s4BcObEFT_zWk89HSnd-gKrWziiCBFrH9JM38cSZJsM1yM4k7NqMjk-SGanKFPusXc_OOFn6mH5kTEtZ0wGduc_0uyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKo8JGyi3VfbqZKEmB40r2ce_vSMuFiY7ekt7kaPEr2p0_cx1WKreGfk1w2fc4J2O7W-CmUcAau1-R8WBXt0IC1gdXHIavooD2I8K6w1ipAvLSFuw8Pq0y6cAI0jA6u6q8zR2GjwGLYm4SlLOH_CArKwNr9Q9_OzbMpg6lxfyhc9HN2sKW9DzFSsLtqvAFhDEGsUkfl-CIh-fkmdLggfowtYU8C6fRvKZqyqOISCTdG4OwS2wdTwDyJL0o1Je2WB174e5bX_ljiQrOJVVn2xHDcll1g5QWghnL-f9C48QIbbZMsjB6B-9SY2LAGtZacoHl7hWdVcYY8NE9Grw3pqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYbjAnxoHBWllqjE_kfTkzn9aX-R1dE5TlUOtJzyrBVtIWaAue4gOsC63hgdBmTjROcMofVa7EQkVPb9MXzHQTyk1FZPH9eDjwULY99bmcm0XVN1mUFFrIzQsIyU4zwl_4vDMHCg5np5W7gHi8aZP96evJISeMJFwGYJM2dORCNnoZwITbBG-3gNMCkFtTrIiMkl6LBTjH_TwgJ7bkKfynd15QJxC8j0X6zQGDhOksz-nwuKqAS7mVNyQkqZx1nTLklHyqh25dIBaJjPUJ__Ubf1NQ4eEzQLHR7BvHu8AhiGGgW85WAghF6VyOhx873i0imrKbfuRQrA9u-Pj6boUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=GjmM19NCYDr2D5D_eRBNcMtnQQk4kaf75EPRJPMLRnK7dTTiQ5s_kGZ3bydOH7NFko-4eJvDZLL_pN4dPthX9FryXCtM_vm7LBgbCZNswGCuDYm_0LE-PRpjM1b0ySozPuoUq0LQJJ-aAxYW5y7jDY2Yp-5aoIcIRrwycpQ9tdXKuNy-WsRaNHzYf2ATQddgzHBSYclME-3ptkkzMWM9-HDs81Vd8-Z4wnbkrLXomK5LsM2QZAcHUVQPxwXv9mbJhEhSaLLeJhpNrHUSsP9j6cYM-Mpww6dkJtN7S8hfT-25wpc4Cy07UvB22yRIQUdwUFCc5qSMcM-w2fNzf9T_ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=GjmM19NCYDr2D5D_eRBNcMtnQQk4kaf75EPRJPMLRnK7dTTiQ5s_kGZ3bydOH7NFko-4eJvDZLL_pN4dPthX9FryXCtM_vm7LBgbCZNswGCuDYm_0LE-PRpjM1b0ySozPuoUq0LQJJ-aAxYW5y7jDY2Yp-5aoIcIRrwycpQ9tdXKuNy-WsRaNHzYf2ATQddgzHBSYclME-3ptkkzMWM9-HDs81Vd8-Z4wnbkrLXomK5LsM2QZAcHUVQPxwXv9mbJhEhSaLLeJhpNrHUSsP9j6cYM-Mpww6dkJtN7S8hfT-25wpc4Cy07UvB22yRIQUdwUFCc5qSMcM-w2fNzf9T_ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC5vM8oLa8QbPSp1Jv2EmXlsVtNOgOcMyxMmYzCMjUw3JXSWvPUAXVJmqtQSQzGiR25b7uDGsaKEAtoa7uXsgnwyTvOJziFzf_sWCsJKFVBnn6UG6Kp5_8R0D9sjQNADHUjYQWuP32gISbnt4oSZ_H3AdARouWUd4Ce5aCLyA2B5NLRnxKClc9Pbtbp88Fh6oX0YILxgasyRf0O8TNLZZKeucCuyRWvdhtSFHzkbmSY7WbjPxcuXRtdv-t7I-fYLvUiX7TOvHobILJPx9--8UtbcYC0xH2N7sGCT7uU8uD10KJXymj3e-CYC6JnCtzTvsjzxkHtvsRvCGe_tFsOjsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLzRTDtCwRNhW1oIUczl-ovi4MeIaOTbOdpSIIbV0d_m0Ej4uIYRJPLNLxksnamrFXknAPRg8Mbi2qyVNcktCR3gq0X-pEYzCJD_SaA3XV0nayDqWBBLibyPDP9dVhxVvxXcjLF06J9fkUMtoKwBjlASW5TgSeyfDPj0SV6GOkxg25cQpiItVNYUYECn1zgZASN15O2ghT2BsGFg-P-ntSlp8RaiJE6V1C3JR2h4lLMymzuPl4R80Y9MdnIxTxtb5FVkQ90ULhJ5faMRMwYox1aVSxYiLTYB6v2wTMc9UcG0XQWmodaPC9wDa0ziIMJRuo9sTSPP1rMhsqdFPVILww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naHhcLgKtx5dUHrRIY47UaFx7RVJB8El4ykKPoBzUqbZV_22IlMKOjLnsdl6GBZWRoXVT_xucOTeV-Fh3s3qj3cVk1E9CoscKrlsbRFu0iDsd8d8Qn08jqOEnmeMn3jx5Y_6Uumxqw9vdKW_K2brC9UnCBPX-8ZBp9cz_o1GrcNDCjJGtMRryXAVR_KhR4ji-KN-RqprYY81KISFAS4WhyEz_JsbedZFXgQLp-QR62Z3hYjEbrzfbmNTzicm8w5DBCufCnE_zix1JnJRWD7rDsOUmxgTkqQIsIzvJqUftI8qm6Rfc_4zzhXZmVuTES-E6MNbaCUtrmQshuv-wgyVOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au5cuNJV-VVmeyf1z0qfvpMc2E1_lkwItQQ23eHIF3XgklPZ_fncvnGcOx7ce4BtLPgU4gtuACu_tuIF_wMmvnTfemdSuDoQ4l9C3PV8OWxZca4vWPS1BR4xJiJyhGwI-94r7fWz4SxNkVJfEaLq0hw1BWJsDJ2a0SXAI5aqFmCGFrkoH_WYzmIn7i6QRa040-aOMdSlsTiLb9yln7PQ30q-nBf3S-14DOElva0g1ayxdfb9Y1sufLH7xvIpSY8b8e2b_0R8R_T0DY1BIvZQnMLAYADYhQNFG6duuiiS0UmOPZf8-8Ee4UmTmyQ35CX1J-apzuGB-vtnfuzKR8XlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mo3cZGoWtBzcEPVtAWU6H7-s3RcMvUAqSTuASaVDkavllrd2CgXd4IOdqz0zGbMxC4sTkLMAls7HVA2Nw_cUxBj5S5bZv-mUuEVdrFTbcTnamEc6WQJlVVqhM8LP3-UUSr2Qujph1EPbNBd_IUTkuUWbpOEv9C_vEVM3BC6d7e_p5IRWQ8hxVYo0HGOFkIWYbOmr3TtA3ciybfp7JG5fWm27ZnrVKaNJaejzF_QF4y_oY6ubadY-qobze0Z4FWwLiGLSVedYqLpGoGTANuYkYzK6Md8-sQsygmdgHgB-uYIVkgEpka9gxlbKCdm_a0HRE48qlclpYqnhgRJscZxZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpgTl5XEaW2iVf7fXyYfSpSvMQM9Jt6Ud-H70bxlKx7-91iX3t3QdVDbwpGS6A-15xeLtSGwctkqpgv3-Ad4KvWXelnOjAUtYqEEOaV6lcrjOHzbQ3oF-2qrdcfbsnCWW89ueKIy49bnVHc5ABm8_jmM9mBZbVXRjtNwR2slhFPlSuQbOejaL3wT85qFuTI8AVucuWEfnNxStnPmjMPi5LPafoLMx-bbKW2r0-XPZW7bT-yMFeLPQKJiw7sQu1_S2SszgWQKOpxCumqgQvkOaGyf55wR3Xkv_WUSQODi91kYvnEAQM1X4FmWI9hMCq5RJR8mmKNdfRyohx3HmRw0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7QoCOjb_QNMHWYmtDy-ajfLQtMvCX2MPBQY_YpdsqwQttw1lAdwRRxytkiYmUb_wO_xpzNkXw7CGpGbD85hpvJUpNlDkX9BGBe_ls2Feo34b6y3fSOHdDM-GxiKW5tD8r_jJ8xZldKydZaA8LQ0IKq8Kw4fs5qYxMjkuqXnmEy_DmMyLdDiPgDSV5zdbc9EFKIWaBuu8hxazryKMbOsKEwWbXk--Y-DDCFKelyqvSng6az-l9YgovdCHCSCgw3tRDTzs8EO1D1j7fit0el7yZ1D-jyftbGaRPe9nMHAuX_kY6aWl_CkG2gwi1stz-1vZ9Ljo-w1GkQUUDoxZtFSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuVthvMsbSrIf5QTRjARCaiUpdrT9aD2-gxmcc9K5RGWLPHuM1arQnEINxCMtHFiUiae965rQp9Ih-vKB1HaP3tUSaDyQQkjOUsGT7rftg84mIpFGfCzroMg05J_E8KZTQizKNsr7vUCKoYz2GtcrJEkW0i791zcHpiEQGgMTxP6GFatSOrYCxg-4Xr5RsC5psay6Rc7IPgMuCGlvNzn8yX2uMVjKejxcY4jr9czKejd7Lu0tQVvF_KOY9SgLptjuLbuUPe9JYI_0O2U8OzAptQNKrONqSAdF7QqZZEH1rUSezFMRNL-fiFy9LPEoIF1QRWgJ-tEE5ZOM7FEIhWESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfChPmWFbRoBNnoGAkq9zy3VAcfGG2i9pqqhuhTu9GSLdA0I_nisTBXc_1kft3XYqaBcp3Z6KyGsc_nn_8qzO-HnY-ziP2GKIzlHyCWGxl-cj8uGSiBfYxIb26ValNOANbvpE0H1xLGCkEvsvAmWOm1S1mAG3zA5E9f7nUBU1BTjr-3CI46R7HKCl9qBIzT8JursE-dLCtR2USaUETEKZZgqiNUvujejm1Hll9XZX-w9Z-2tEI2CrSvNascsJyk_ABo4G6nw82Cfnixkr4LgNZHwPGafIQtERpVMvFMD3lwDT1lLgnekZkbNFmWnZVGxKKkB4WRVj-2OmP__ivrPsBuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfChPmWFbRoBNnoGAkq9zy3VAcfGG2i9pqqhuhTu9GSLdA0I_nisTBXc_1kft3XYqaBcp3Z6KyGsc_nn_8qzO-HnY-ziP2GKIzlHyCWGxl-cj8uGSiBfYxIb26ValNOANbvpE0H1xLGCkEvsvAmWOm1S1mAG3zA5E9f7nUBU1BTjr-3CI46R7HKCl9qBIzT8JursE-dLCtR2USaUETEKZZgqiNUvujejm1Hll9XZX-w9Z-2tEI2CrSvNascsJyk_ABo4G6nw82Cfnixkr4LgNZHwPGafIQtERpVMvFMD3lwDT1lLgnekZkbNFmWnZVGxKKkB4WRVj-2OmP__ivrPsBuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=EROzCSYGSc38SNMW1jkcHURaCi-zcPAecx6HfAHL62-c9fUz5mcHuV-BDnYHWbLsWVsY0uE3bpTf9gqIN3zdG-cv0dqqDiN_E1fvjmGuiX7fjLZ6SCMvuA5RzRlPxiVh0FJpB5M0mzHa6oqtGi-Nn0xnZYxGX0qO-NVKI0MJ12EbAoqEtMPQVJNY3AroJ3a0EYSQkrgwU1sfIEhKqD3zmNN0aaHRTk0SclDU_TPyeIviXt8x189XtQOQjm32EFp_BZmKgYT7WKiRNX5kRVXKq7_rBWidVnlhxQOhym3xQ66EfAjvZ702-cdPHI9Iixqv4vXT0oqfl_qjrHOalNUYfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=EROzCSYGSc38SNMW1jkcHURaCi-zcPAecx6HfAHL62-c9fUz5mcHuV-BDnYHWbLsWVsY0uE3bpTf9gqIN3zdG-cv0dqqDiN_E1fvjmGuiX7fjLZ6SCMvuA5RzRlPxiVh0FJpB5M0mzHa6oqtGi-Nn0xnZYxGX0qO-NVKI0MJ12EbAoqEtMPQVJNY3AroJ3a0EYSQkrgwU1sfIEhKqD3zmNN0aaHRTk0SclDU_TPyeIviXt8x189XtQOQjm32EFp_BZmKgYT7WKiRNX5kRVXKq7_rBWidVnlhxQOhym3xQ66EfAjvZ702-cdPHI9Iixqv4vXT0oqfl_qjrHOalNUYfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=PYKYFVS7ieobPGnx9LnxGP7DCJLgJ4oy6AW--m-f16_tcMqPw05nvXjy5NcVWNmttAMCOkXqw_I8pDW6AZWQHgS3VdE2xbCtZugWjujiSymUfD0gFf6KTqpwaPvc2yytWMOH4hrtyrDycGq_w0VnHiYAN0Ckki1l6Yb_a1HYDoG0VCQYAf6EnEL7gs9Z8zHeqe_r1wyahgjtxBg1b1fKGBYFEH9pwEpjJdXHyIQ2bEfg9VR4XdKZnp5LAHp4N0nj8O331inwM0SNoCn5JB4UDOvCskgNHX5TrHH4VZ9QLU55WM0Cq1TIZDPHR0rdEibxPuLzUdXrINsKcuXcdx4d9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=PYKYFVS7ieobPGnx9LnxGP7DCJLgJ4oy6AW--m-f16_tcMqPw05nvXjy5NcVWNmttAMCOkXqw_I8pDW6AZWQHgS3VdE2xbCtZugWjujiSymUfD0gFf6KTqpwaPvc2yytWMOH4hrtyrDycGq_w0VnHiYAN0Ckki1l6Yb_a1HYDoG0VCQYAf6EnEL7gs9Z8zHeqe_r1wyahgjtxBg1b1fKGBYFEH9pwEpjJdXHyIQ2bEfg9VR4XdKZnp5LAHp4N0nj8O331inwM0SNoCn5JB4UDOvCskgNHX5TrHH4VZ9QLU55WM0Cq1TIZDPHR0rdEibxPuLzUdXrINsKcuXcdx4d9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8vyavaaXLct3J1CERqkdYFT_81QC631Dyj4hei-gnERglcI793nSFsZuvxcxQdLH1GHTE9wLNAaxZG0G-rISa2Xgv6kKsANsG3MvjUxPlHhLb988Swoxkxfn4VIEKj2e_Lj7Vq3lYq7uLogSBqVBFf-lJv5KRLTu_polDF7uYcs2dX2UX-tK80P7opyi8VrgGEkPi6S-QE3UE0u2Eo1JOAsXWCwbQtJTpye75FT9qN7hlDuIIi7GZsUJmFbHs7f19OiU8NwT8wH_zlOoWHQVLpQIwq47S5xQmNq5zOMIK8QcZZ_pdqey62503JiTklZVeYCp5Dfn0KunYW0XkJ8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNYKUpKkYPsGL7-X1VhE-p7vg2iTgN3WiSZxyDLTUxWjAxNPA_rc9ptbaKOn0Q9II0qQRL1h34GS1EPTnjb3HiUfprWvpQ8xL4Q8C19fSUVlQfPFjgzLzn3KCNslHyON7di7gG5b8eGKtp7YwtZ8NKPJwYA11HIdWES759C8pA3mO1bDuHAaxNRG4N5dIHKa3g3Q6lzxKDgvL66pb5JhYaQxRrA4Kf05HQ5Hp3MwavCXROB8V1a5HVEcuF1Byj8pthf7ZOewkaVFAtlrSmUS92aG2vSOVRw3HmoW4IcqsyxwfEvMW4MU-nFofXx9ZHToKjIppzlRjlDIW5_FITdbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
