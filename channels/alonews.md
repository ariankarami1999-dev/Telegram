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
<img src="https://cdn4.telesco.pe/file/EqFI2UokJEolmIbK9pNbdtcJ1NZQQurgw03JUc5bzQVSn_7Zw_QFba2wIJaBfJ4Dv0k93QsTHbAUtxGlBPqQVt_3WYlG7Xi7sUmGrNWCYv6NTq6nIJk6N3eCwif8MSSwIUQTHeUQMsmzP7OQtVLvzlCVg0REnEWNabnNRfu6mwB3l9HNUZnogGONSsTN8RrhNI11N0J-I3HRGz7ouemnTT_TLadha9vbVlJHoXtU000ed42pKxxQWhs9hibs1eOyvTN7i_kri4jx4xX28LHZDSerfA9IUY8TJKQG6xVJlUFnos2CmCmGHNIuOiOMbkTnnAWuI6eo5mvl9-jDZf5aqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 01:29:01</div>
<hr>

<div class="tg-post" id="msg-132668">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/ سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر نیز منتفی نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/132668" target="_blank">📅 01:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132665">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmxBM0U7YDYiYR7ipoclrEvk9uzBiYDPVmirL2gBkTBgSphKkjW0eM65N0S9b5ezj-0DnBRcuFygZiaWXaFTqU0VhQjYNcdYOjzQZW-YBjhj9ZMocNT-lU3UpGJ3CWcvF3L4Wb5HAFpWeJbX0p0F5WxWKGUEEhN9bv9WroDMnldsHcUlVPfCRiYf9gb6Qx1NPzjM6C-8u_EohTBfuX49QF88ufkSjmmdRFND5NNA8d9B-9JZYYP6dmc1_gagggL6vCD37L5RbrrgvdsAyYz6dokgbF0SSyrmwjHW-buyPvHFwEGO8rMSBprO_BQ71zbdVDLZhOIjeuI87hzXQGjvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lauptj0v3-vzieKhqgyy2yPr_n9VWEqpToMRffQXFoChjLB48wDavoVvWIPPOql3YLeCCKj87sET20ZL4SSypTZmXPFe_G6ZCi64Lec-fwFaaLnRNZEjM6O5imkh_BLSIMejb2Rumx4vCowzxe07eNF5dSoqdDoJyNwA2CrFkbDc5vEh_sZ3arm9c5aSrkYss1jaGMFrSXVUKCnAH1W6FDyQsRtI1-_d2n5P8d2NkukteRx_oYeIXXRkfbx_jNMbekRb3bmOoXyqBwdXhBnPNQf6-mwQ6b5UwoSlbbh4ezEMT5wZr0SMCoqg9ECngrUjK1Q38W5kdMZ3KnyKeA7cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vy2lERbgLmhr6yLvnIQNZCAQWv8aogKNrlRdeNfmcnpzB2qfKA83dNkWKRY_FEc6xylHT8FMPZEpklmxMWKwXwiNo1NTejfKqDORrJ4QZaPy-O9Fhixp_BDuYgiPYxaGjFcr1BslE3OyEm9mjdWf0QCxpKN5dZkGFdNAOlE8TLFS0_VAR6jleCJ_VOZPIfUOK3kl-BPvmj-6Cp9SqcTW7n-SuqO_C90ylQMpMaKdp74AMt1En6QboEuhvJ3vIGPlUPubaO7wKZaySIlIvOHZ8-7QTYRNigD7Xxdtjnkca5Bwyol9qW9q57Z5-975TdFaCV7SszlQeq0We46BHpnLow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ، تصاویر مربوط به حملات در ایران را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/132665" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132664">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/العربیه: بحرین در حملات امشب به ایران مشارکت داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/132664" target="_blank">📅 01:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132663">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhqek97O4Llq0u9molfQaOMPkjZfww51Y7PSwe0-fov5ia4yTtxyATzwcGF7FLkOnxM7_uFzsBNrwvipUVj4hGMlZPV4ttJoUFcLSYd__KJDQqVf5hXulcSMorKe0oaFylKq8b2KeYtfxZh0yi2FxmHn99J7TY_MidY0aQIHkMlZMXmBViMkW8DG-c06kOs6tzcYNKvCDXvtaOK2h8Ahok3o_Ou0VRllxwQnBQOdwMcv5tcTMaBp-fdcEGxUG51lBYm6Y6H_K7BeiWr1VH0a0IALTZLQJ2nvgSPFtiLHgGdePvkd2dYcAw54pU0-GKtEAH0wS3gszHCt9uROks7nGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ ترامپ: «این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/132663" target="_blank">📅 01:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132662">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5jgvFjA3U6J1kP0vthL7cJYzPpYuD0LIvvMyUG9bGy03CB6frNcQ_-nO2p2FFCjigKKp8TwoW8G5g1TWQSN_pCswCIFm0qB3-bj1dmRVa76C01K8JyCz_wBsHCQk29MSQVVvEYeTc7tWPl-dVvPXPLGAqlhNYyNMCZ0bAsZuDYMbcr9kXljIFpR0lNt5jEttyd9vVxnnSp3BW0-sA5CFp6j_nidps_m4yTQRA1z4PpRHpuDrcq_MF20sL2N8bFGGgfTsgtehGqMYbOHfFguSZap_nmKaiUbrITKHSOi_kR-3csmh8aKU8GBBArSmUKh8ShJaqKH2hwIFcWCb_qrNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ ترامپ:
«این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/132662" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132661">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سایت پدافندی نیروگاه هسته ای بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/132661" target="_blank">📅 01:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue3j6ml47At1BGPeEp59Okx1rT1SaAVlKF28K_XycoZ_uBasyk8BoOO38z7CB7Ovosz593mugXfujNOTC358qGxQ7ykxTJzkkCpNCdiPwdnYUSB344cgVGNvQyDu7WYtgGfvGOcK5IoYOdwL_9Zw5YgSJkp42yvc55K8ZoYH_EFJPpWL45p3npe_1iOiCnRB0RkhcM8gIMcn13GotWxHS925E0X_mIlP4BYnG-saYzu2O4I5CYO-npL9r7GP9UV8jVCO_NfQekm-z7oIS2r152fx3b5kpofOKYAIc_UdzMiKUs7iDDfn6TLyvVOSBnV3IY2pGcKV86NIBXnCDdbItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
11 سوخترسان درحال رساندن سوخت به جنگنده های ارتش ایالات متحده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/132660" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc262f35c.mp4?token=Faryblbe7zvp373rozOJqynXo0km3-uLoqbypuQ88GtOGLRMigPsQ6hJ0mKcEGWzlTCno6fYkoY8MsSNmp-yCOkqDARRSMlqn3UDX0_evWeXxjfh_EA0HZ3q-J7c2fKZoBHJ0JF4eftF-DkoCaPzB7-4Hp4JIYebiF8n5Qhw-2cWtF45AihW3bIpL2HA7h6_DUIJjrjUY78PtRCcyfbsPdy3jJlTdkVTF7nLzCWSI8V_CTMAF5ulveaSOIL-clJm4tSzpe-PqCQoL55bpLV4FOsjpAPBWy9caHXKGcWT01k7CnPT41fVLlS_WHc6ss2oLpRRQdi3X9YqcSwAsmrrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc262f35c.mp4?token=Faryblbe7zvp373rozOJqynXo0km3-uLoqbypuQ88GtOGLRMigPsQ6hJ0mKcEGWzlTCno6fYkoY8MsSNmp-yCOkqDARRSMlqn3UDX0_evWeXxjfh_EA0HZ3q-J7c2fKZoBHJ0JF4eftF-DkoCaPzB7-4Hp4JIYebiF8n5Qhw-2cWtF45AihW3bIpL2HA7h6_DUIJjrjUY78PtRCcyfbsPdy3jJlTdkVTF7nLzCWSI8V_CTMAF5ulveaSOIL-clJm4tSzpe-PqCQoL55bpLV4FOsjpAPBWy9caHXKGcWT01k7CnPT41fVLlS_WHc6ss2oLpRRQdi3X9YqcSwAsmrrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش سپاه به حملات اخیر
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132659" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlGD3W4-N9gW3w2RM632qEHsG4PRJNEPMT-q8ksnz6fN4pY1Md3Uyr4_aCoc4HvijvmlINKZljqvH6ub1ytJrEJqFpQ_6t1anF36LeTCEjkS5ky-Q1rvRxNPihcPpPhDaUCJR_UHoy5a8X4m5xuzCAjP9PQ2kodcyntX0Kn_GQgh7eNif4BUQoMjkAD07O7v5JckCkfnKChZ0AuWlYxHnk3kP6KJkY7uLTdD5jyrkYjoRax77GNqb0dFihOb91JN08gb2At8yzkXw_BrPkIx_xufAynByxaraqKD5id37Xps-Y326EjIRME7GppibJ2T-vy5siZsIV4zou6Pm2lLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال
محسن رضایی:
دشمن به شدت تنبیه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/132658" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132656">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پشمام
😐
بعد از برد دراماتیک آرژانتین گروهی از طرفداران زن این تیم در استادیوم لخت شدن
😐
⚠️
⚠️
مشاهده بدون سانسور فیلم</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/132656" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132655">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گویا مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/132655" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132654">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
140 جنگنده تا الان وارد حریم هوایی ایران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/132654" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132653">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs-H5ZU7Lc7q1e_d5EdAVyXTQdv7VCwflEvzFyf7pGjwA73SLn9-UNnCTZjpVpeTEwCu--7wBFTTau6prBegDJUhe_CHMiQsCIIiJ7n_IDvN7yhLyAG42-M_ja21i-u8rv-9NNDk4x18RY6sP-FO8zOMP8DR9_QAugHBFgLyBYM0lt2uxdyKiXCwxT4r1Syb1shdF-eWkkCOwnHll5mPr0YKWJg0gk6kobDxdSrIkOFD9ICGx3H0z59y36v0KD1NEVrVC2mPy8FgaI7VNh5a7ZknqwJezxqtUYeOXGuk74o3E0i97EhRrRzYvw0Il-Y4InzchApYYsqJzL4-XFHvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: باید واشنگتن رو با موشک بزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/132653" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132652">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNUFBiubXWPFh3JQ7gdWvr0r0DQ5B37O37DiYbiLnjPJRouFax7goJnGEi23yJvFZb9Yigs_RQJLeDLqM3yt3wWykbMgENYnAkJ2Dx49JOsGA8V0RnWpAU5f28zw1bWi950-O2F6NkQ0tb9tBrC8r0-5gvasdlYXrXWN4IMheaC4JxyAntdH-QbXDGrdHc4Vb5lLEhMfPE5eeRHF7BC7_wDXcF7Q3IXBGhPfTP9VkqLVT5WcCTDwTu0_DBNV4aPnSKXDfSVaR56JNZ5WqGzdWg-e0uDropAyyEfezMyjy-GaMFH1dmp2huo43U63XG4niznVwfz4WKVsjGIyL5LJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ارسالی کاربران الونیوز از هدف قرار داده شدن برج دیده بانی چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/132652" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132651">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=Iupk9o17mysQNNZgHMGq2RYhf-r7GlAC8sIlV1qpFrBXSalRdRx19szYL3Y4TKnaibeGkGvg_Yfi8DQCdvWZVkUi4uuCN1EFW6-LiPvpeoN2CrSplmObHX3-uCX23MJfF7ImoI6dP9sujvOVBPpd8BGgHxW4CgSCKyOgsPyYjSafGeleJLPGg_uOpjllWvpE_bf8EUun2tuFBmqqlSHPlQ-3QhhPicCiisME3TXcwSPdVyF-BjON9wEZvhSMpAdnNimac4dGfmegUy_mrBCsM_7n8x_FUoaX2e1S_nEPGJUo6ovzjRopmyF7hLJd9tbOCF-y7fD_qMzlpyPFObSUSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=Iupk9o17mysQNNZgHMGq2RYhf-r7GlAC8sIlV1qpFrBXSalRdRx19szYL3Y4TKnaibeGkGvg_Yfi8DQCdvWZVkUi4uuCN1EFW6-LiPvpeoN2CrSplmObHX3-uCX23MJfF7ImoI6dP9sujvOVBPpd8BGgHxW4CgSCKyOgsPyYjSafGeleJLPGg_uOpjllWvpE_bf8EUun2tuFBmqqlSHPlQ-3QhhPicCiisME3TXcwSPdVyF-BjON9wEZvhSMpAdnNimac4dGfmegUy_mrBCsM_7n8x_FUoaX2e1S_nEPGJUo6ovzjRopmyF7hLJd9tbOCF-y7fD_qMzlpyPFObSUSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس:
🔴
ما به آمریکایی‌ها پاسخی کوبنده خواهیم داد و امنیت رو از آن‌ها در هر کجا که باشن، سلب خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/132651" target="_blank">📅 00:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132650">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/132650" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132649">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">💢
فووووووووری/جنگنده در آسمان تهران  احتمالا جنگنده خودی است
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/132649" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132648">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری/پایگاه امام علی نیروی دریایی سپاه مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/132648" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132647">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88d7ae0b90.mp4?token=tJwVqtMZrsBYhOsfEG2ov7DnR7Jwy1YjKDhgH9-UDE0Op-i9I7YvcXP8TmeivIYqdpE43AHdy3xczmZmrOhoy8TWvbH0ziY3t9aujIRuK_YGyr2kXv21I3LufA_VhN7D8JbmucchCupAqF_LdRZbSHXFLPGzOvte9jy84C6ZYbiQLjRTysnx8xDUbZwwdLJKuTg6xaqdSztujdILoD-tMvvypEu0KNnsUclKYczhSoktcLFE5X-zNycASLbp5E4Vo2Aj4Du1nOfvtmvLReUDI2CxsaKo6D9X-29aVrNd-eHtoqcTKUpKw16Noymyfos95xM5n-oy2WcXGlnrclmgmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88d7ae0b90.mp4?token=tJwVqtMZrsBYhOsfEG2ov7DnR7Jwy1YjKDhgH9-UDE0Op-i9I7YvcXP8TmeivIYqdpE43AHdy3xczmZmrOhoy8TWvbH0ziY3t9aujIRuK_YGyr2kXv21I3LufA_VhN7D8JbmucchCupAqF_LdRZbSHXFLPGzOvte9jy84C6ZYbiQLjRTysnx8xDUbZwwdLJKuTg6xaqdSztujdILoD-tMvvypEu0KNnsUclKYczhSoktcLFE5X-zNycASLbp5E4Vo2Aj4Du1nOfvtmvLReUDI2CxsaKo6D9X-29aVrNd-eHtoqcTKUpKw16Noymyfos95xM5n-oy2WcXGlnrclmgmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله به اسکله شهید کلانتری چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/132647" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53c23c50c.mp4?token=NuXW1uyK5yeEh4riXMNkfKY8W-UxXBtEPb1xDjJatPVVr76kzBincME_yLRBEYwcbTsqsXmDwWBrvtHrFVLUlQDBVsZdffqZPwhOp_OzB_E3GYauuMEdoXX_pbfcdOJDOD_-ZPnXuCdBQNd1jVmt81mLPjXMqwgpGWkV7s_kfBXaIQQCAbsNHCGIwlTlcuGg5L-n-U_5a5pdK4HMWJM1eWtUnPOJgCJNKzIS3fTX8sYN-RcAaoNG61h8yvH-wSHuYR5Nk_YVm3rkfJ0ZYhHVMTOF-pistvkCj0ZvZgIQHtG8OqoCTiz-1rknVZI-l0tMa2Dls-uttzYCY9zEpsOM1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53c23c50c.mp4?token=NuXW1uyK5yeEh4riXMNkfKY8W-UxXBtEPb1xDjJatPVVr76kzBincME_yLRBEYwcbTsqsXmDwWBrvtHrFVLUlQDBVsZdffqZPwhOp_OzB_E3GYauuMEdoXX_pbfcdOJDOD_-ZPnXuCdBQNd1jVmt81mLPjXMqwgpGWkV7s_kfBXaIQQCAbsNHCGIwlTlcuGg5L-n-U_5a5pdK4HMWJM1eWtUnPOJgCJNKzIS3fTX8sYN-RcAaoNG61h8yvH-wSHuYR5Nk_YVm3rkfJ0ZYhHVMTOF-pistvkCj0ZvZgIQHtG8OqoCTiz-1rknVZI-l0tMa2Dls-uttzYCY9zEpsOM1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/وضعیت چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/132646" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/بزودی حملات ایران شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/132645" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132644">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جنوب کشور داره بمبارون میشه، شبکه خبر هم روضه پخش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/132644" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132643">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
گویا برق بخشی از چابهار بر اثر بمباران‌ها قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132643" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132642">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از بمباران نیروگاه برق بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/132642" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132641">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HjNeIAqGxzHog_65ieUuOX8JWVeWDhneIz8w3pr_15QjIxpnK3STLDLtMM9_v6jmDSZC--nA8f4TFUrFVORi-qy4Tfsq_-Wp1QulSKGnYJ9gBAQuCHEHS_ggggwMaVtp8bP-8UJ6Y-pFo0Yr8-5TdoKPftxMd23z05DdX6mD9lycqi2cLoF1h4SbxDkbLrredlwEkqcEjKUZ6Ve_L6UGrf8TmBvuXK1rs1YOdSTVgIopSGT78pYo-ZiLo01wJ1MLGyPhk9rUMBHjHRFPoUJA-gE3UJV9sH3BzQPu1IAaQnO6g0SuMTynfMaW0KGmwVKeSIdkqOY7ofFQauQOdRfixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/بر اثر انفجار، آسمان بوشهر روشن شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/132641" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132639">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/بیش از ۲۰۰نقطه تا الان بمباران شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/132639" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132638">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قضیه شده این: شعار بده، بمب بگیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/132638" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132637">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوووری/ایالات متحده تمام نوار ساحلی جنوب کشور را بمباران کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/132637" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132636">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8lXKps9lWYoTz1K70bjWD00RZBAD7RY5SSsShQUCwQo4wbSHqrhQygnyeuf2GznhKJ6e5PQBt2whBV81GmMVE1YFSg-dwSCIBXszKwwd23CjYlvpaKHVxMJ_ZfeqK9l_qSUaZfkZotvgCiRjfCG-OEbA5cF1hMQwkbmeb5ch9usBnBkbcLt_ypnnTdeIoT66riTMAA3EgcxNXeVVnMcbE5piclWbV3piKP-QQXZ2_lejISTDkXguefa2FRNBzxBBgYvuqNOTKjvJpCm3boQOgXrmV0JLJF7hGUQArjgUQTakeK7-Rl7qZ5pf8KUfQ7KxSXS0L-MaTE6DEa2-kpgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ارسالی کاربران الونیوز از بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/132636" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132635">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری/انفجار در جزیره خارگ
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/132635" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132634">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/132634" target="_blank">📅 23:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132632">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/132632" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132631">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKtVyxqOl8_C5wymdUyLlSdMPtbdgcRbAibE9Jw_nNGExVwOwRCvVAIA5ZqoJYyvLymru6RooEf3bKB21i4N-yjFcj9WyMHJUsEwpxdumuu8koAsVIwy1XbqhdiGwoy4n_RqSN2QwZYyF_je6S6KRqcg6HJmOM_3Huh64xe4xOsoEe_b1J-phrYT7V22rBTWD1LwuGH3BetblWQ3HfQvW9uygLe90RZ-0LSenEPad6GD9AjrfBbXOH9kvezl_eAaYqCQ-RT9N0Jk-9GKXtr55f6ke7dJhYNmoDH-z90KgC4SNrYrxsY9leJXfLEE5ef2BP5FY7jED-jn10i65EiPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام
:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/132631" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132630">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=ps9JiO_f03jG5Sg2DFJYvjMbHhlMo5QvVXZCOKth9TfTedqnfVK_1y2Qae-jjQ_m5O2z4VrWymbraPo-yOjOz5bFxPKftGW0yoZDPXTEzlqL3tAEXf_kxscKjURvEm1Fq5ie-u1HxtIsmszPmgvLbvAf7MXMzlx4ghQvEQdSSvZPP3xZGXm9MPNpTRhyuKxVbPNUz2dhK4yl9PV-yfYcfSiekhbq8tZJ6WQrhum1ZLlVxfMMk4qQ7PsB1KOnMf6jlfGWnLxaqm0Ug7a_bKlMmrhwL-hZx7-yw0seGTcq02E76mQ4Cb_0Zbfu7MXXk1Dpmp7jeI4DxsaCz6_Sf474pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=ps9JiO_f03jG5Sg2DFJYvjMbHhlMo5QvVXZCOKth9TfTedqnfVK_1y2Qae-jjQ_m5O2z4VrWymbraPo-yOjOz5bFxPKftGW0yoZDPXTEzlqL3tAEXf_kxscKjURvEm1Fq5ie-u1HxtIsmszPmgvLbvAf7MXMzlx4ghQvEQdSSvZPP3xZGXm9MPNpTRhyuKxVbPNUz2dhK4yl9PV-yfYcfSiekhbq8tZJ6WQrhum1ZLlVxfMMk4qQ7PsB1KOnMf6jlfGWnLxaqm0Ug7a_bKlMmrhwL-hZx7-yw0seGTcq02E76mQ4Cb_0Zbfu7MXXk1Dpmp7jeI4DxsaCz6_Sf474pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ارسالی کاربران الونیوز از انفجار در ۰ابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/132630" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132629">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/پالایشگاه لاوان مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/132629" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132628">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/انفجارهای متعدد در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/132628" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132627">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27659d902.mp4?token=rJSOchjMhAAY1fnsN29FReP_oYrWSHTA_1NjkYBuT662R7x2YJUhA-nzJNYz6AFeqaB3J8B9dewghPpsaUkaiXVd3_HLgwCGoWLvAcWsQZCecgPf4K5tMZ7vdbmOnpLBAnYoiAf0fpdjjCU5I47MMY7R67XGkerihkq3NsBU_b1wW92aDh47z9b6JpuSejXYyHMLrcyuJvqcmW_Gmg0LetFC2XOfFPXHzUeCWc8QNw97gYFtxZ2U0ra5jEohHk1F39rtxG80vU14Cf0NOANsVuTOY5pID3B7mTOTSEyJRvA6rOcnxydxO1TEfDcDjMY1vPb8qKvbiEiqozFTmqjEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27659d902.mp4?token=rJSOchjMhAAY1fnsN29FReP_oYrWSHTA_1NjkYBuT662R7x2YJUhA-nzJNYz6AFeqaB3J8B9dewghPpsaUkaiXVd3_HLgwCGoWLvAcWsQZCecgPf4K5tMZ7vdbmOnpLBAnYoiAf0fpdjjCU5I47MMY7R67XGkerihkq3NsBU_b1wW92aDh47z9b6JpuSejXYyHMLrcyuJvqcmW_Gmg0LetFC2XOfFPXHzUeCWc8QNw97gYFtxZ2U0ra5jEohHk1F39rtxG80vU14Cf0NOANsVuTOY5pID3B7mTOTSEyJRvA6rOcnxydxO1TEfDcDjMY1vPb8qKvbiEiqozFTmqjEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط
،
دلتنگی و گریه هادی چوپان برای علی خامنه‌ای
🔴
زیارتت قبول آ سید/ برگرد دلمون تنگه برات
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/132627" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132626">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/132626" target="_blank">📅 23:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132625">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/132625" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / حملات آمریکا به بندر کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132623" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/132622" target="_blank">📅 23:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری/پایگاه دریایی سپاه بمباران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/132621" target="_blank">📅 23:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پدافند بندر عباس فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/132619" target="_blank">📅 23:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132617">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / صدای برخی انفجارها از سمت دریا در محدوده ساحل غربی سیریک به گوش رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132617" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/132616" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/132615" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سفیر چین در ایران: پکن اصرار دارد که در مناقشه‌های ژئوپولیتیک دخالتی نکند
🔴
ما همواره از کشورهای منطقه حمایت کرده‌ایم که سرنوشت خود را در دست بگیرند و از طریق دیپلماسی مسائل خود را حل و فصل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/132614" target="_blank">📅 23:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132613">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojluPzO192GRVb7urz9d666h1fXhpivf3ei1N588E_NDNtEZdMzpYuLwi30lYn0HdTLHw7nSL0lBCknG7_kvVddmQM0T7WKbCMAU-gADNzI5tACkHhROsJpeYm3RDf4sQ70tI06B9ZKHZT2svUeE88hRYxl4s4__teV2wh2zLwZ-oR67B2Zy6XmXiA8blKXfOCHkEuOd2ZrW7hcISj_rvKYFIAMgebSfJSCEgrIuZYs_AI2du1MZtguceQLocaAcbkle75aBqa3tNIeKgcbeQnQvdp50z4Z1zm6TMv0QnNyzKJEeqHoTPZEp9WKNFJukwU_masvQYOCX1YDJFfWKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک مرکزی: تورم نقطه به نقطه خرداد به ۸۳.۱ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/132613" target="_blank">📅 23:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / صدای دو انفجار تو بندرعباس شنیده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/132612" target="_blank">📅 23:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام برنت در معاملات آتی با ۵.۲ درصد افزایش به ۷۸.۰۲ دلار در هر بشکه رسید
✅
@AloNewd</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132611" target="_blank">📅 23:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال: عراق با درخواست‌های آمریکا برای توقف جریان دلار به شبه‌نظامیان تحت حمایت ایران موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/132610" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مقامات ارشد آمریکایی به CNN:
حملات آمریکا به ایران ممکن است در ساعات آینده آغاز شود، تیم امنیت ملی ترامپ در حال تصمیم گیری در مورد دامنه و گستردگی حملات آتی می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/132609" target="_blank">📅 22:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132608">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a187b5378.mp4?token=GytHCOWnYyQJL0nUJuh4sMIEfjq3E8eFs8OKL2231QCs6ERpg0YQ7UQL9sFyteJzrhicltQHhXcckAsaW7vQaYpxbY5LPN4VbLRPTdvYue9zTI2xEKkj-3uqGGedcwMejldT2BcUDRfhVIpp4q9ovjS1XYFHfriARtB_PKxkdXbgYG9j9tSix64B5kVf8doQqgbhbkz9vo8om12y2EupoFWmNZRvSQ1pqc2Ye6Vrmczfc827HlUMqVTGpVbqR-LGnzKpjTF9NpwQKQf5-B2N6HfHHg07dR5PLG5p-fUdXgH9cKLiwP8yMHopP1L0jzWUx1vUbE0o__W05fSduCxWNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a187b5378.mp4?token=GytHCOWnYyQJL0nUJuh4sMIEfjq3E8eFs8OKL2231QCs6ERpg0YQ7UQL9sFyteJzrhicltQHhXcckAsaW7vQaYpxbY5LPN4VbLRPTdvYue9zTI2xEKkj-3uqGGedcwMejldT2BcUDRfhVIpp4q9ovjS1XYFHfriARtB_PKxkdXbgYG9j9tSix64B5kVf8doQqgbhbkz9vo8om12y2EupoFWmNZRvSQ1pqc2Ye6Vrmczfc827HlUMqVTGpVbqR-LGnzKpjTF9NpwQKQf5-B2N6HfHHg07dR5PLG5p-fUdXgH9cKLiwP8yMHopP1L0jzWUx1vUbE0o__W05fSduCxWNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس گوشی خودشو چک میکنه تا ببینه ترامپ بهش زنگ زده، یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132608" target="_blank">📅 22:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132607">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
به گزارش بلومبرگ، دونالد ترامپ در پایان اجلاس دو روزه ناتو در آنکارا خطاب به رهبران این سازمان گفت که «عشق و محبت» را احساس می‌کند؛ اظهاراتی که پس از دیدارهای فشرده او با سران کشورهای عضو ناتو مطرح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/132607" target="_blank">📅 22:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
جی. دی. ونس، درباره ایران:
ما با ایران یک توافق انجام دادیم. بنابراین، این توافق بسیار ساده است.
🔴
اگر آنها به سمت کشتی‌ها شلیک کنند، ما به شدت به آنها پاسخ خواهیم داد، و این همان چیزی است که قرار است اتفاق بیفتد. این روش اساسی کار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/132606" target="_blank">📅 22:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ادعای العربيه: فرمانده ارتش پاکستان با مقامات ایرانی تماس گرفته است تا از تشدید تنش‌ها جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/132605" target="_blank">📅 22:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e556b8541.mp4?token=MsRoQYjsSJA5SlpdNMMIfp5Ehf6KNPhlWS_R65CtXIc76VQGu34pJ7Itha9YSF7G4OjjVAJ3UnuNfJMjinpd5wpNJ0IA8UoFWacr6MHUl6vsGnrh6JZ5q2XBmBywozJ3_9OQ-vOw-GZlURpfCnCLK8qFzElGcWlaQY5_ZtHEVldg4Sy2VCZjhIEpuckfDe4_4syEaAhU9svp762FXQj8L5TbffBTPfwopy6m--aXNKVfOtOTabjPFHWiHNfHe4si5J8SihrOd8CvMcr6N5Jah3McM1ZYuT9p4jBiDAWfx7RWYYlSlU279y6udl4n6PC42IS4gJlZ3cs644EjAj866g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e556b8541.mp4?token=MsRoQYjsSJA5SlpdNMMIfp5Ehf6KNPhlWS_R65CtXIc76VQGu34pJ7Itha9YSF7G4OjjVAJ3UnuNfJMjinpd5wpNJ0IA8UoFWacr6MHUl6vsGnrh6JZ5q2XBmBywozJ3_9OQ-vOw-GZlURpfCnCLK8qFzElGcWlaQY5_ZtHEVldg4Sy2VCZjhIEpuckfDe4_4syEaAhU9svp762FXQj8L5TbffBTPfwopy6m--aXNKVfOtOTabjPFHWiHNfHe4si5J8SihrOd8CvMcr6N5Jah3McM1ZYuT9p4jBiDAWfx7RWYYlSlU279y6udl4n6PC42IS4gJlZ3cs644EjAj866g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی. دی. ونس، درباره ایران: اگر ایران تلاش کند تنگه هرمز را مسدود کند، ارتش آمریکا واکنش نشان خواهد داد. این موضوع بسیار ساده است – این توافق است.
🔴
آنها می‌توانند از این توافق پیروی کنند یا دقیقاً همان اتفاقی که شب گذشته رخ داد، دوباره تکرار شود.
🔴
این وضعیت همینطور ادامه خواهد داشت تا زمانی که آنها این مسیر را باز کنند و از شلیک به کشتی‌ها دست بردارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/132604" target="_blank">📅 22:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
معاون ترامپ،ونس: رئیس جمهور ترامپ گزینه‌های زیادی در مورد ایران دارد و من دقیقاً به شما نمی‌گویم امشب چه اتفاقی خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/132603" target="_blank">📅 22:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ از کنگره خواست تا سوریه از لیست تروریسم خارج بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/132602" target="_blank">📅 21:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132601">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
اردوغان، رئیس‌جمهور ترکیه، در مورد همکاری با آمریکا در صنعت دفاعی: ما حتی در مورد اقداماتی صحبت کردیم که ترکیه می‌تواند در صنعت دفاعی برای همکاری با آمریکا انجام دهد.
🔴
این اقدامات چه می‌توانند باشند؟ ما در صنعت دفاعی، به ویژه در زمینه ساخت کشتی‌ها، در مورد این موضوعات صحبت کردیم و امیدواریم که به سرعت اقداماتی را انجام دهیم.
🔴
این اقدامات می‌توانند شامل ناوهای جنگی، زیردریایی‌ها و کشتی‌های کوچک‌تر باشند. ما در مورد همه این موارد صحبت کردیم، و آیا ترکیه می‌تواند این کار را انجام دهد؟
🔴
ترکیه می‌تواند این کار را در کارخانه‌های کشتی‌سازی خود انجام دهد. ترکیه از نظر توانایی، قادر به انجام این کارها است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/132601" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132600">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ابراهیم رضایی: کشور های حوزه خلیج فارس مراقبت چاه های نفت و گاز هایشان باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132600" target="_blank">📅 21:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132599">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBAPgqC6gQ0zEuKTEbu_6KjdI2_4CLy_IRdy2ImgBuDzLaBelpkppFzYi7Sw_N2SxcrZfqdk5u2Up48Qrw64FMI_soQjJtacIMT1ov1SXlErEW6VXgDjW6LxGjCI4X8ANkBh_ISUCcrOQceKps1HWcV27EIv1DfXj6rCam2akL1I_EO6TxtyOoz6PTN8kK5pr2R0mEl_e0BL44N5IzH3xYfAd7_QxFcGIg8kDIRLRs78URShRScjJXgx-Cga_4PJHDQkrYHghjJ3Umz8Z-0op0zYpO2WHZPGtpVfUVKXudJGGbxL0Rs-ZGd6tl3IRRfgWU-gVTlJqr4htPkZTedE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: آمریکا ساختار توافق را نقض کرده ‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/132599" target="_blank">📅 21:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132598">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVXuTIP1OtJ3jpcF1-ScRDCahrirbplGEeUDrfpNSn0turbLhns1iXxYTTPNgAzwuwL7RWF6rdXKD_Nge4juWlebjZEpT9z1GC8MfQ-W3EWPjZgX1Uy727sd6oExOkBiTw4sAV7zAKbi9Qk8s8YnYCEt3AnOOisn7td16FDkWjK6Yrir-2PNEaCwgV87SpWbChSexDTGuBj-eDx4T2BWht3SkbAb7PdyKicZyaCKQQWxC1-i0J-Vhg4cvKVRsvEVdRbBtZFluJ9qyVFjM456-gnlOwj1sL6qgRg_gycHBPM0WWFzWSSDIqoslCCjUD_-jsYjA8W33q8r1bp7eFx1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخت‌رسان‌های آمریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132598" target="_blank">📅 21:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132597">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
به گزارش واشنگتن‌پست، دونالد ترامپ از ولودیمیر زلنسکی تمجید کرد و با لحنی مثبت از حملات عمقی اوکراین در خاک روسیه سخن گفت؛ همزمان به نظر می‌رسد یکی از درخواست‌های دیرینه کی‌یف برای تولید موشک‌های پدافندی پاتریوتِ طراحی آمریکا در خاک اوکراین در آستانه موافقت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/132597" target="_blank">📅 21:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132596">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ آنکارا رو به مقصد آمریکا ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132596" target="_blank">📅 21:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132595">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMFopm-9G1XQjyR2-muS48nBDkY0zGumVGmMhVaURxEOE9x1ZdOCCKM_zOt58v1-LtajKa8FTYTm_gJUezm_hzlB5Ds9lhNwmQsaBj8rMqsim_e2iaRIVNI8Y2BlPociri8NPi4t8Q062uITiAoh1BWNFA4VYY39o4I9fFDUrTiluBeAYLItPC-Vt8BIY34M6hwccO6RnDANbXqe5xlpnFH9G5AAvIPClSapbEFEmYWA5UF5XrTWkGZVzjV3wPb0WCuuDPwRI1D3wH0ZB6K_3dcXxjWLe7zQ4YeySi8u-zNCUM0YMZhaafiapSIwM97Qyc-pxzMNhB5DnAcTFVZrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله رسایی به تیم مذاکره کننده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132595" target="_blank">📅 21:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کان نیوز: بازگشت سوخت رسان های آمریکایی به منطقه آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132594" target="_blank">📅 21:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان در نشست ناتو در آنکارا: ما به عنوان ترکیه، نتوانستیم همان‌طور که دوستان اروپایی‌مان توانستند، از سود صلح پس از جنگ سرد بهره‌مند شویم.
🔴
بسیاری از بحران‌ها و درگیری‌ها در همسایگی نزدیک ما رخ داد.
🔴
زمان‌هایی بود که تنها رها شدیم و با رفتارهای ناعادلانه مواجه شدیم.
🔴
اغلب اوقات مجبور بودیم به تنهایی از خود دفاع کنیم.
🔴
امروز، از نظر هزینه‌های دفاعی، توانایی‌های نظامی و قدرت صنعت دفاعی، ما از بسیاری از متحدان خود پیشی گرفته‌ایم.
🔴
رئیس‌جمهور ترامپ همچنین تأکید کرد که میزبانی کشور ما از این اجلاس در تصمیم او برای حضور نقش تعیین‌کننده‌ای داشت.
🔴
همچنین به‌ویژه معنادار بود که او بر دوستی شخصی ما تأکید کرد.
🔴
دوست عزیزم را بابت توجه و ملاحظه‌اش یک‌بار دیگر تشکر می‌کنم.
🔴
فخر ما، نیروهای مسلح ترکیه، قدرت و توانایی خنثی‌سازی هرگونه تهدیدی علیه امنیت ملی خود را در اصل و ریشه آن دارد.
🔴
ما در حال حاضر فرماندهی و مدیریت دومین ارتش زمینی بزرگ ناتو را بر عهده داریم.
🔴
برای دهه‌ها، امنیت باله جنوبی-شرقی ناتو عمدتاً به کشور ما سپرده شده است.
🔴
ترکیه به حق این اعتماد را پاس داشته است.
🔴
جنگنده‌های اف-۱۶ ما از ماه اوت به عنوان بخشی از مأموریت گشت هوایی ناتو در استونی مستقر خواهند شد.
🔴
ما فرماندهی عملیات کفور ناتو در کوزوو را که در ماه اکتبر بر عهده گرفتیم، تا پایان سپتامبر ۲۰۲۶ ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132593" target="_blank">📅 21:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ادعای سازمان پخش اسرائیل: نتانیاهو و ترامپ در حال مذاکره مستقیم در مورد تنش‌ها با ایران هستند
🔴
ایالات متحده در ساعات اخیر شروع به اعزام مجدد هواپیماهای سوخت‌رسانی به اسرائیل و خاورمیانه کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/132592" target="_blank">📅 21:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loOtt_Ke6FkHuQRdXrEwDe_Nf27CR4covpOD_77GoIr8rZpzS0LOrrl3Cb77lnS-uDs9nfMxXfIimwks_T1LYd6lwKq1_I1IaVqz31_0rWG2NiL5rUcirshTZDMsIGPvcqK8Bw5O1ugNI5uvpGYU39qBLLoL16ARr2hh6Q_zI1tL40plo6KQZP_LukJQnaAJGjoFS5mfnXQ4-rqnPPK7lell9dUgVYXpcgsmDQQcKvp4tJ0aXiTmOIrjzDpNVnbP5HpKfj8MXvLEGfnmqK-XOhGokunNEEBm6U31ZpaOpdyrHKekvog6a9oS8aH57OKBzwVA_xizkdoLSzFyqn0F9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه، عراقچی : اینکه به ملت بزرگ و متمدن ایران توهین کنن
🔴
چیزی از بزرگی این مردم کم نمی‌کنه، ایرانی‌ها به فرهنگ، ادب و ارزش‌های اخلاقی‌شون شناخته میشن
🔴
ما جواب بی‌احترامی رو با بی‌احترامی نمی‌دیم؛ جواب ما عمله، با شجاعت و بدون ترس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/132591" target="_blank">📅 20:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سازمان ملل: از تنش های پیش آمده در خاورمیانه عمیقا ابراز نگرانی میکنیم و خواهان صلح فوری هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132590" target="_blank">📅 20:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کارشناس شبکه ۱۲ اسرائیل :  تبادل آتش تو خلیج فارس؛ ادامه مذاکرات از طریق روش‌های دیگ‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132589" target="_blank">📅 20:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ضرغامی: رئیس جمهور فاسد آمریکا را در ترکیه ترور نکردیم؛ به دلیل حفظ دوستی و حسن همجواری
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132588" target="_blank">📅 20:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d05cb3f5.mp4?token=u6hWPIp7wDiQVnJlma2RdFi10T76pbTexFAVO133ZCm8zcobGhSF3lqi00ok6Mk6PSd7pm6727GqAjVaB9YYWeXjCGrteDW-CS8Mko5S4eK-4dQxsWbD1Da8zQgEIyhkkOFrUMTqp7ipdCUId34dV4zPq2GcsRYuyuQWkCE2GZlao_wFbrsSAUB3gE3DT82aPHYbGqtjVRKw9o9gh_rV9k8ymUYmMi0GEQjps4qsbIGTz0QFygj5hJT022EeDzlxD43INvhS5D381IrPf5-WaVJSGbSmawsW0JFVJnx7k6FQ0-aGfasMwibV-mxtaHkvO-bpiursqgwnVuzt4jUg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d05cb3f5.mp4?token=u6hWPIp7wDiQVnJlma2RdFi10T76pbTexFAVO133ZCm8zcobGhSF3lqi00ok6Mk6PSd7pm6727GqAjVaB9YYWeXjCGrteDW-CS8Mko5S4eK-4dQxsWbD1Da8zQgEIyhkkOFrUMTqp7ipdCUId34dV4zPq2GcsRYuyuQWkCE2GZlao_wFbrsSAUB3gE3DT82aPHYbGqtjVRKw9o9gh_rV9k8ymUYmMi0GEQjps4qsbIGTz0QFygj5hJT022EeDzlxD43INvhS5D381IrPf5-WaVJSGbSmawsW0JFVJnx7k6FQ0-aGfasMwibV-mxtaHkvO-bpiursqgwnVuzt4jUg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خنده های معنادار مارکو روبیو پشت سر ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/132587" target="_blank">📅 20:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KARvNoSoAPRBVCADGYMjk89PaQesZEnr9U8evT-DIuERw3U_8W_FY_sM81T1gYgl8Q8f1jat3DiFA_uaSQ6sfI7Hl53xx6FpMLxIIr5-HhN6pt4lZi_zsuoxG9pyv4LXz-64a_liTJYPH5eTJwDYWvPv2sSF7X3W-ObTwjfkn1xjvku00MoV4ZaDmPYhaezscAVYoukHW-oMEjH5ZfCkAe30kE46CZ2sdLy0qpJFBJpCEDIUnqJ3Lt2OWltfENmeaw7XmWX82PkhlS-6Hr8hEjL7YPpUbgMTXOPRXj6X7gLS2lMu0GUfUo1cia11Hhf9O0UfOuEPrI4YIwQB_m0VCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: تفاهم‌نامه را آتش بزنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/132586" target="_blank">📅 20:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0t3wc8-EWhUL67tkzzuhYaDCAmopO09EuINScLzgn__o2cHr5YdqHs0TpQ5MO92XiPWWOqBNIftkEPXqK0KlewukufvrL0P6L0VS5r9Fxk7xjYz4Oz56fugzRRtlIEI_GuokboVcSnvLuQD8FAFmHyXJGFNaqLnYaL_GJf8JAHrrjpXkNL-kvtu2lPWRJWCrVk6mXLF8yPhEW3ONgofGIa1Xg1dJzVCfjJ7MlPYF1Twz_gcBDUDN6JyNvPohGaqeCaRON9KGAux94yaQNJP_Xrga7UNzjLS5Lk7EKwE7Y4qyxbISLJL4s6bPtb__ic77DHU7napKAzDkA73J5kIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: میانجی‌ها در حرکتی مهم برای جلوگیری از هرگونه تنش بین تهران و واشنگتن، و ارزیابی این است که میانجی‌گری‌ها ممکن است در مأموریت‌های خود موفق شوند و طرف‌ها به اجرای مفاد یادداشت تفاهم بازگردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132585" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گزارش جروزالم‌پست، امانوئل مکرون گفت ایران با حمله به پایگاه‌های خلیج فارس، توافق خود با آمریکا را نقض کرده است؛ با این حال او تأکید کرد انتظار دارد مذاکرات آتش‌بس ۶۰ روزه همچنان ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/132584" target="_blank">📅 20:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: ترکیه بسیار قدرتمند است. این کشور دومین کشور قدرتمند در ناتو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132583" target="_blank">📅 20:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ در مورد دادن F-35 به ترکیه:
هنوز کاملاً تصمیمم را نگرفته‌ام، اما تمایلم این است که بگویم: «او همه کارها را انجام داده است. او به روش‌های بسیار متفاوتی به ما کمک کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132582" target="_blank">📅 20:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132581">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69062797bd.mp4?token=V6sVRG0W1agZ1MHWaHzqbPG_8rvB8OKrAnmndAIPfa_x_DeAN2FkxGt8uL-SOeaLU0fS-sRKaw7JbBdKx6CmlniB-Fq60QIf9VFLes6BloF5_qCl6ViLQayFg6WpGcAQqbFcFiM0v0uKvhiCdjP90zzlkBj95ZYwuS7nWJFJUrWEatAQNQPMxyl1jShsoxHySGqHJKVXV7XIgrj3NsFH5SlQErosym60E9eZyMkTeFYGTdm0HjVg2zVIqzrdrTVHVNA2OVQw02x-XQ0Yda5bzgqTRcqiI4ExZnS_SVHVHesrmQaxh6TG5qVCYVvICXS0tyd-sQYkoQ6BhBrGcFa76A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69062797bd.mp4?token=V6sVRG0W1agZ1MHWaHzqbPG_8rvB8OKrAnmndAIPfa_x_DeAN2FkxGt8uL-SOeaLU0fS-sRKaw7JbBdKx6CmlniB-Fq60QIf9VFLes6BloF5_qCl6ViLQayFg6WpGcAQqbFcFiM0v0uKvhiCdjP90zzlkBj95ZYwuS7nWJFJUrWEatAQNQPMxyl1jShsoxHySGqHJKVXV7XIgrj3NsFH5SlQErosym60E9eZyMkTeFYGTdm0HjVg2zVIqzrdrTVHVNA2OVQw02x-XQ0Yda5bzgqTRcqiI4ExZnS_SVHVHesrmQaxh6TG5qVCYVvICXS0tyd-sQYkoQ6BhBrGcFa76A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: از کدام رسانه‌ای؟
🔴
خبرنگار: MS NOW.
🔴
ترامپ: اون یه شبکه رو به افوله. چرا دلت می‌خواد برای اونا کار کنی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132581" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132580">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: اردوغان طرفدار بزرگ بی‌بی‌ و اسرائیل نیست.
🔴
اما از آن جنگ دوری کرد.
🔴
او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من از آن جنگ دوری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132580" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132579">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: من شماره یک لیست ترورِ جمهوری اسلامی هستم.
🔴
واقعاً برام مهم نیست، دارم کارم رو انجام میدم
🔴
فکر نمی‌کنم جنگ ایران دوباره شروع شود
🔴
هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132579" target="_blank">📅 20:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132578">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ: من شماره یک لیست ترورِ جمهوری اسلامی هستم.
🔴
واقعاً برام مهم نیست، دارم کارم رو انجام میدم
🔴
فکر نمی‌کنم جنگ ایران دوباره شروع شود
🔴
هر اتفاقی قرار است بیفتد، بسیار سریع خواهد افتاد. ما به دنبال بلندمدت نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132578" target="_blank">📅 20:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132577">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a722cf540b.mp4?token=PtyGLNGEr-Ksfb0NGXTv94vunBgWR5F3JhGwyvO4ykfusvfR9_ObKwbwMPuN-Xs14Phd_wEmbMC7Rpn6RfFPwPak6DCpYUD75bmH2A3BP4VSN2eunKRBi7f-Wa4sdkihCXJ3OZ4y46xUZDBi51y1S7E7RVW2ZYBJqh2Es8nwWlktbTZKMvkz_h0Al8YCPNpwj1ZeWsLuBrypy-_ZwWIir_tZPKdJskDSL0p0SdYoNbpx6-tyqvY_B93MAyZQV-zJjFjO5XOXwuBWv1_2npq51PwZiulrmxgQ_5oG5LCjFhqLRSVO-hB0VfWbjCxde1fynVqoDlh9CEG2X_tp6yd4yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a722cf540b.mp4?token=PtyGLNGEr-Ksfb0NGXTv94vunBgWR5F3JhGwyvO4ykfusvfR9_ObKwbwMPuN-Xs14Phd_wEmbMC7Rpn6RfFPwPak6DCpYUD75bmH2A3BP4VSN2eunKRBi7f-Wa4sdkihCXJ3OZ4y46xUZDBi51y1S7E7RVW2ZYBJqh2Es8nwWlktbTZKMvkz_h0Al8YCPNpwj1ZeWsLuBrypy-_ZwWIir_tZPKdJskDSL0p0SdYoNbpx6-tyqvY_B93MAyZQV-zJjFjO5XOXwuBWv1_2npq51PwZiulrmxgQ_5oG5LCjFhqLRSVO-hB0VfWbjCxde1fynVqoDlh9CEG2X_tp6yd4yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به محمدباقر قالیباف:
محمد چیزی آنجا با بیل‌هاست.
🔴
بیل‌ها شما را به آنجا نمی‌رسانند. بزرگترین ماشین‌آلات جهان شما را به آنجا نمی‌رسانند
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/132577" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132576">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19994818c.mp4?token=EQKG037YPEszzmZCgEBMh6LjB6uUXsZnnj657-Ctq00dDhaPEMf0WsdQdQjmMxL8zBfgpfqbAwdqUrOR75hO58UW8-cIPQqkVYmMOq4kzK8C5_QRCsaIFUYRwpBLUDCOust25NpTN_vr9_4rPJqT2hCV0ov8NbXpV26xJDdFF2tflEbM7JfRYHe4-8zqvKc6lXy1yUrGhCkGQR3mAZh6r8E99R4uToE0NFamNJay3WyQTLe0_TMgamkd22WdMp19N1Ci_WoWyX6OOB0yRIG14Saq2XhuN6QOgZHlQHUlsfAPcE20vp_7UGVkl2uqhkhM-n2mi2Aout1FHm7Mlk7BNx10QASkaLJzryBJuCVopPGX0CZMCsn156zINyPMvBrn86PfnjjeuxCsko4sNbzEhDoeEAS31zBz-Xzy5RGCsI8hHuLHl3fR0W-oJgQhbjFDPCk7Qd70EOHC0ycWCcQVLUbxFRZJA3JDCn24a3M1mWoFW2Xi9XUcgEQMELAyHd3v9QJv6MQvGehs1ZrnnJuvsQU-zPq_f5XU5lZn1n4W8OiTvGpqnd4nDCVuW_uObdKZRVfvBPoCGSiAlP0XNEeoXx5OVxXyrOgZHxuErqIxB2t97sSc-4jRYcrzSfjSpj39M5Mk6A1_GFIHxLt2KmGnJRb-BJpMiQhaIQ6TgXE5TD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19994818c.mp4?token=EQKG037YPEszzmZCgEBMh6LjB6uUXsZnnj657-Ctq00dDhaPEMf0WsdQdQjmMxL8zBfgpfqbAwdqUrOR75hO58UW8-cIPQqkVYmMOq4kzK8C5_QRCsaIFUYRwpBLUDCOust25NpTN_vr9_4rPJqT2hCV0ov8NbXpV26xJDdFF2tflEbM7JfRYHe4-8zqvKc6lXy1yUrGhCkGQR3mAZh6r8E99R4uToE0NFamNJay3WyQTLe0_TMgamkd22WdMp19N1Ci_WoWyX6OOB0yRIG14Saq2XhuN6QOgZHlQHUlsfAPcE20vp_7UGVkl2uqhkhM-n2mi2Aout1FHm7Mlk7BNx10QASkaLJzryBJuCVopPGX0CZMCsn156zINyPMvBrn86PfnjjeuxCsko4sNbzEhDoeEAS31zBz-Xzy5RGCsI8hHuLHl3fR0W-oJgQhbjFDPCk7Qd70EOHC0ycWCcQVLUbxFRZJA3JDCn24a3M1mWoFW2Xi9XUcgEQMELAyHd3v9QJv6MQvGehs1ZrnnJuvsQU-zPq_f5XU5lZn1n4W8OiTvGpqnd4nDCVuW_uObdKZRVfvBPoCGSiAlP0XNEeoXx5OVxXyrOgZHxuErqIxB2t97sSc-4jRYcrzSfjSpj39M5Mk6A1_GFIHxLt2KmGnJRb-BJpMiQhaIQ6TgXE5TD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مواد هسته‌ای ایران:
ما دوربین‌هایی داریم که بخشی از نیروی فضایی ما هستند و می‌توانند نشان شناسایی افرادی را که به یک محل خاص می‌روند، بخوانند. [نامی]، به نظر می‌رسد که چیزی با استفاده از بیل در آنجا وجود دارد
🔴
بیل‌ها به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
🔴
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد
🔴
بنابراین، هیچ‌کس به آنجا دست نخواهد زد. در نهایت، ما آن را تصاحب خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132576" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132575">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10af6b9606.mp4?token=uEXAnYzSZrYVh8DVEcpXW5aPDLcft_NrnB_DGjubufe-XZb1gqLJI1rcVBGnW-DB3ROi4-2N1fbL0E_6xfMxYBA9pPFnclLxpqXhEk7SGrRR_sEO1Fsf2VsjSCj_OjxwmCXjDnn5w__ZLokInTQWgPF19m4g-T7yYcKR6iIWpGeSPCbFWypGmMxav9SW77sZBCm9pc0QDAAf-VIcTNjO7hK8Qn7FfXS5CtemSUeCYDeU9pik6dSzJTsjflK-BWTaczLJFaDiLO5o08bujRNT5ju1Udm5jVttE9ebZdDTlhSN8rZ1IoGzmUVN8KcRhcNPQW0clzOVoIxm6-pk7-tlYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10af6b9606.mp4?token=uEXAnYzSZrYVh8DVEcpXW5aPDLcft_NrnB_DGjubufe-XZb1gqLJI1rcVBGnW-DB3ROi4-2N1fbL0E_6xfMxYBA9pPFnclLxpqXhEk7SGrRR_sEO1Fsf2VsjSCj_OjxwmCXjDnn5w__ZLokInTQWgPF19m4g-T7yYcKR6iIWpGeSPCbFWypGmMxav9SW77sZBCm9pc0QDAAf-VIcTNjO7hK8Qn7FfXS5CtemSUeCYDeU9pik6dSzJTsjflK-BWTaczLJFaDiLO5o08bujRNT5ju1Udm5jVttE9ebZdDTlhSN8rZ1IoGzmUVN8KcRhcNPQW0clzOVoIxm6-pk7-tlYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من همه چیز را پیش‌بینی کردم. من مدت‌هاست که در مورد همه چیز درست گفته‌ام.
🔴
به همین دلیل است که من سه انتخابات را برده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132575" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / ترامپ : من مطمئن نیستم که بخواهم با آنها معامله‌ای انجام دهم.
🔴
فقط بیایید کار را به پایان برسانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132574" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132573">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ : قیمت نفت کمی افزایش یافته و دوباره کاهش خواهد یافت
🔴
رهبران ایران اکنون منطقی‌تر شده‌اند
🔴
ایرانی‌ها به کشتی‌های ما حمله کردند، بنابراین ما با حملاتی ده برابر قوی‌تر پاسخ دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132573" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132572">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c735101f5d.mp4?token=fQww-MFGyqLEQ9rwc4xJl5PgYHH5UbvY8VmymPtLh7yDI-e-SUq9E9_utpCdhE7_xxjGjNDS2k1garemxnjkV86ZJGO-Xh1JKFUph8_rXeDIEz3wAoov_25fcg1ywGcMCwCtKBaiwfv7u10R-rSEPUQAOFBHalHTEToGRQPswAcrVl6k_DFjZSWIzLfh6r4VKUjnLhyGdhRidFMDFc7ppv9pi0kpMVbA4Dd64Jcm9p3t68MeHe3r0brGNY_VxIQjrgkjOwPM3bzc-_Ppq45zG86xMX91Sk3s2m4lxAWbVjU7pHpfYWtRVAXKOLhwN477JQjYg78XTuRkXhpXKCiQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c735101f5d.mp4?token=fQww-MFGyqLEQ9rwc4xJl5PgYHH5UbvY8VmymPtLh7yDI-e-SUq9E9_utpCdhE7_xxjGjNDS2k1garemxnjkV86ZJGO-Xh1JKFUph8_rXeDIEz3wAoov_25fcg1ywGcMCwCtKBaiwfv7u10R-rSEPUQAOFBHalHTEToGRQPswAcrVl6k_DFjZSWIzLfh6r4VKUjnLhyGdhRidFMDFc7ppv9pi0kpMVbA4Dd64Jcm9p3t68MeHe3r0brGNY_VxIQjrgkjOwPM3bzc-_Ppq45zG86xMX91Sk3s2m4lxAWbVjU7pHpfYWtRVAXKOLhwN477JQjYg78XTuRkXhpXKCiQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی در سه ماه گذشته ۵۲,۰۰۰ معترض را کشته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/132572" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132571">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c1f3d00e.mp4?token=fNGDhT8zvkv3uuRgPmFFuqwVIBWAj7GkT9v8aVNPN6IzbJatWDBft4oK0HYBsQKJMjCwq6VW0JiREo6Wu2gau-jXzb8LqA4Cm4QkRXtwgQzt1S94-iC_iUB3pVzGmCdaHw07az--Ma_mEAS-WSEkFkvdXZKNFFttCkTioA6Jj5nLbfKxzqHPt5nHNl82e3R4R8cVX0a8alZKmK4rPmh23rW5WYK2OAJhAuspl1C5btNJFiduK2uQoV_Hbh7OW5Svqfsx7VIMMg5rY8QDr5UXOebisrmIc9DcJfgahgHH4vMgYTRjJhkArfIGPyCdgaZkr-gE1iHZ8SUSedk8CU4byA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c1f3d00e.mp4?token=fNGDhT8zvkv3uuRgPmFFuqwVIBWAj7GkT9v8aVNPN6IzbJatWDBft4oK0HYBsQKJMjCwq6VW0JiREo6Wu2gau-jXzb8LqA4Cm4QkRXtwgQzt1S94-iC_iUB3pVzGmCdaHw07az--Ma_mEAS-WSEkFkvdXZKNFFttCkTioA6Jj5nLbfKxzqHPt5nHNl82e3R4R8cVX0a8alZKmK4rPmh23rW5WYK2OAJhAuspl1C5btNJFiduK2uQoV_Hbh7OW5Svqfsx7VIMMg5rY8QDr5UXOebisrmIc9DcJfgahgHH4vMgYTRjJhkArfIGPyCdgaZkr-gE1iHZ8SUSedk8CU4byA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي : «می‌دانید چیست؟ شاید من هم تا آن موقع دیگر نباشم. من هدف شماره یک آن‌ها هستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132571" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132570">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری /  ترامپ: میخواهم پرونده ایران را یکبار برای همیشه تمام کنم، نه اینکه با رهبران فعلی بازی کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132570" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132569">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e090ee0c.mp4?token=Qrj0hVhQ7DunBpx_3ocyjzMRXafoKnA9r5U5wuJ9avMvbkPpP7j1GG8y7ewliNaaQTqEOTtauXURudjkFGwmdeoTq9T4RAzvSkLZ1cL-R9rgS8cRrWoddCRWx4VoFy1xGJU7thZ_Tk75nFpExBTkf8MbuigLy2OxPiN9uazJ9bitjEGrL6llB4Ausdwc9EyVC9AuNnWZvQCddBKL47z-HkAH3eo5Q_m-t_4R-7owB6YqQ23zbJnH9tXbI7KurTNlLiDQY0d3sGkbpUTJFB77e47sgJsmmV3_RvDDmK6bIho1UvQ6RB2iOYW8Yx8ShmzamHbd-FyhJZiG3VD_YwQCMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e090ee0c.mp4?token=Qrj0hVhQ7DunBpx_3ocyjzMRXafoKnA9r5U5wuJ9avMvbkPpP7j1GG8y7ewliNaaQTqEOTtauXURudjkFGwmdeoTq9T4RAzvSkLZ1cL-R9rgS8cRrWoddCRWx4VoFy1xGJU7thZ_Tk75nFpExBTkf8MbuigLy2OxPiN9uazJ9bitjEGrL6llB4Ausdwc9EyVC9AuNnWZvQCddBKL47z-HkAH3eo5Q_m-t_4R-7owB6YqQ23zbJnH9tXbI7KurTNlLiDQY0d3sGkbpUTJFB77e47sgJsmmV3_RvDDmK6bIho1UvQ6RB2iOYW8Yx8ShmzamHbd-FyhJZiG3VD_YwQCMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد توافقی انجام دهد، اما نمی‌داند چگونه توافق کند.
🔴
و سپس شب‌ها به کشتی‌ها شلیک می‌کنند. من آن را دوست ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132569" target="_blank">📅 20:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132568">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3852511a3f.mp4?token=IamPQC-QANBL1ZifQPQskPoJNHO9IL38906_680egDsywZ6izJLDACET1IrViU9n-Oah4QA6FxUUtK9W413tLpod4JjaPmmbV8cu0HwRzN5xP4cC71w3Ux7byKIT6GQD8Tu4zV8fdSIWspI5vYGFtikQEFJLQQYyFlU-08pmPTLu7rfbNi_tbwEWNYvp-cwnj1S0_4h2e5FhbVguJ9vfyJnIZ76KnDk658_jsKUiUmf_2sjW9tAWgpt4cM9D0Ovh1u5EQ2hQcA2kqFVVxn5WYd5vaHRVOpQfgU59iDj5BpIiddXO1rz6sMunWGvDxPInTzSGsCd7titAg5eTKJHD2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3852511a3f.mp4?token=IamPQC-QANBL1ZifQPQskPoJNHO9IL38906_680egDsywZ6izJLDACET1IrViU9n-Oah4QA6FxUUtK9W413tLpod4JjaPmmbV8cu0HwRzN5xP4cC71w3Ux7byKIT6GQD8Tu4zV8fdSIWspI5vYGFtikQEFJLQQYyFlU-08pmPTLu7rfbNi_tbwEWNYvp-cwnj1S0_4h2e5FhbVguJ9vfyJnIZ76KnDk658_jsKUiUmf_2sjW9tAWgpt4cM9D0Ovh1u5EQ2hQcA2kqFVVxn5WYd5vaHRVOpQfgU59iDj5BpIiddXO1rz6sMunWGvDxPInTzSGsCd7titAg5eTKJHD2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد تورم موجود در ایران: تورم آن‌ها ۳۵۰ درصد است. وقتی جنگ شروع شد، ۵ تا ۶ درصد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132568" target="_blank">📅 20:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132567">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: جنگ علیه ایران یک موفقیت نظامی بود
🔴
ایرانی‌ها دنبال توافق بودند، بعد به کشتی‌ها شلیک کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132567" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132566">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پرس‌تی‌وی به نقل از یک مقام ایرانی:
تحولات ۴۸ ساعت گذشته، عزم تهران را مستحکم‌تر کرده و یک دکترین نظامی و راهبردی جدید به اجرا درآمده است.
🔴
هر تهدیدی با پاسخی قوی مواجه خواهد شد. ایران بین ایالات متحده و همپیمانانش در منطقه تفاوتی قائل نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132566" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132565">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8fc7e935.mp4?token=CV9uB3LQlSwThT9GngeRIw54baht32f3wnUcIkbqiLDJMyLpSNHOcBuHJu6bAXgIt_U0VvUodLui6RgphZx1bhuCTer2HcIpdL2kEydOe6PPKo9bEXb4bubpJ9O-mQbPiZzfKEkoXgoYHb6jsf5usRim9098ThnAB4sJ0UIF0EOEa2C_NwISDxA1yMgk-2B_K2hieDxM3l5SbgrLFDjS1dXfbSTqTbQkr5WNXBdBoSchR0b1fng6LSGGM_bK1fq2odILoqD_epnt-NOV-PQkzMA371RHn3jlEFZJqjV64GyU015cxfkEX4KBRkAWFOQ8-nxCd8nWpUVlEZmNDh3Agg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8fc7e935.mp4?token=CV9uB3LQlSwThT9GngeRIw54baht32f3wnUcIkbqiLDJMyLpSNHOcBuHJu6bAXgIt_U0VvUodLui6RgphZx1bhuCTer2HcIpdL2kEydOe6PPKo9bEXb4bubpJ9O-mQbPiZzfKEkoXgoYHb6jsf5usRim9098ThnAB4sJ0UIF0EOEa2C_NwISDxA1yMgk-2B_K2hieDxM3l5SbgrLFDjS1dXfbSTqTbQkr5WNXBdBoSchR0b1fng6LSGGM_bK1fq2odILoqD_epnt-NOV-PQkzMA371RHn3jlEFZJqjV64GyU015cxfkEX4KBRkAWFOQ8-nxCd8nWpUVlEZmNDh3Agg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در آنکارا: اندوریل در حال اعلام یک توافق برای ساخت موشک‌های جدید باراکودا خود است.
🔴
ما این کار را برای لهستان انجام می‌دهیم. لهستان با داشتن یک رئیس‌جمهور عالی، بسیار پیشرفت کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132565" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132564">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: امروز، بیش از ۲۰ کشتی جنگی نیروی دریایی ایالات متحده در سراسر آب‌های خاورمیانه گشت‌زنی می‌کنند در حالی که نیروهای سنت‌کام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند.
🔴
ماه گذشته، کشتی‌های جنگی دریایی و هواپیماهای ایالات متحده در نزدیکی هم از دریای عرب عبور کردند و قدرت نظامی و آتش بی‌نظیر آمریکایی را به نمایش گذاشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132564" target="_blank">📅 19:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132563">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: کمونیست‌ها خدا را نمی‌خواهند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132563" target="_blank">📅 19:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132562">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae48e0068.mp4?token=smJP8C4EuRuq92ZYwRi2gV1s_L55l4Rh6hPOwe8AVD565TZEFqpgVpRVtOpIImjB9duRstV7palHzJz_EFEq-xSemXVnX5-ILR6SNBG6aOuNGU8yUSo6S4jyyfXNhAwd2N1LyBDCxvjdS8EEvr9dIw5811AXq-8pZIW2UKPW8RH-liczLcqLj8FjIV-B5S2MgCbVW4jjg_t_3scsNBbwM5wmCkpyCMw3rDhp7DEoDDziuI5_et6KX5DKO5BXufu9mg9O6WtfiiNrtzZ-IKVMQ36hd66ZLNIsVqmGSTY73kqQU9NTbO0_9zJest1mgWOn8CCZhoSJgYWxaglfh-T71A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae48e0068.mp4?token=smJP8C4EuRuq92ZYwRi2gV1s_L55l4Rh6hPOwe8AVD565TZEFqpgVpRVtOpIImjB9duRstV7palHzJz_EFEq-xSemXVnX5-ILR6SNBG6aOuNGU8yUSo6S4jyyfXNhAwd2N1LyBDCxvjdS8EEvr9dIw5811AXq-8pZIW2UKPW8RH-liczLcqLj8FjIV-B5S2MgCbVW4jjg_t_3scsNBbwM5wmCkpyCMw3rDhp7DEoDDziuI5_et6KX5DKO5BXufu9mg9O6WtfiiNrtzZ-IKVMQ36hd66ZLNIsVqmGSTY73kqQU9NTbO0_9zJest1mgWOn8CCZhoSJgYWxaglfh-T71A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در آنکارا
:
لاکهید و راینمتال شراکتی را برای ساخت سیستم‌های موشکی تاکتیکی ارتش اعلام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132562" target="_blank">📅 19:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132561">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ در آنکارا: مارک روته کار باورنکردنی انجام داده است؛ نمی‌توانستم کسی بهتر از او پیدا کنم.
🔴
فقط می‌خواهم بگویم که در آن اتاق عشق فراوانی وجود داشت. در واقع گفتم که متاسفانه مطبوعات نتوانستند این صحنه را ببینند، زیرا هر یک از آن‌ها برای مدتی کوتاه صحبت کردند و من نیز مدتی کوتاه صحبت کردم.
🔴
آن‌ها افراد بسیار باهوشی بودند و قلب‌هایشان سرشار از خوبی است، نه بدی، بلکه خوبی.
🔴
تجهیزات ما کار می‌کند، اما باید آن را سریع‌تر برای همه، از جمله خودمان، تولید کنیم.
🔴
فکر می‌کنیم در عرض یک سال — حداکثر یک سال و نیم — به جای اینکه یک یا دو سال صبر کنیم، آن را با دو هفته انتظار، شاید حتی یک هفته انتظار خواهیم داشت. این همان چیزی است که می‌خواهم. و واقعاً خوب عمل خواهد کرد.
🔴
بسیاری از مردم فقط در حال انتظار هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132561" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
