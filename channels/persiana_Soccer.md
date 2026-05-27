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
<img src="https://cdn4.telesco.pe/file/uS6TEvX0AbxU5_4YZmbrIq7ZkWqdW4qxEZ5NeWkd99gmsj0ktVpBvCR8-CLPxXIeYF3jhPtBYaNBp4Z17n5W0Pv5sDi1M0Z-MrCjfg6-tUJpxaOgxILINeygu2W5ANrANIqkKhnvfwDCwg1jOL10pfJrYhAwX_WcoF94aKARMQAH3qzizQkHbN3JBsOCRu64qV3XhN6M7zJ_jSElJh1Y7D0u4CehuOcnIh9rHLTTFeuDm2gpyvaKrG3J-4jABfx--m1klgMVTEUBz4OBm027v9mOjU8Xi5T5unHeHYwcZnl4AwcAOpSdS-IY7TMT4dr1CfIhqp9kt2fHIE9he9IczA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 186K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 23:32:33</div>
<hr>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owB7IhEE_7KlXugIvpl5eDTXy1e8lYLBwxK3OOg7RCyyq-STVTUEvIw8zXrn2Pr16t07I0JhRix_8nrCdg-FJhvvB9X5V-jHkYjQfmxR1YhWYWJqdBlRSV4_ijrI0X_YzgX5gDwioLdM4pftAILIHkaQuMvuNehrOk_ZqivZUGQMuEqW3-lCYLTJLaWfElpKaADOmPS6gztq73g42nLx8i_IPMfpXZ9eQAJ-sqaxtsl1onjjxGrZbJiXv7hZs8NX89c9hHT3uj2NMggJ1bOioGcsuGX4sR2RRvvf574DZZUj4SVS1ujynOHfDNANRarqcupy_jO6joZT0Ip9_qKMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=fjaGFx2g0m1igLXXBnLTxMOtW0sedPSVWWymqfc5aHTIUKCN-HlmQo5-w7ZWGvV65dcplXpXHmLA5RZVp83Cjo2rCPqcmqBbj0iUfCzz6WiD574E37aWeNTSTZ3dOm55t-P20EzBFUVqBJiWmkaTonbQyHSDxhOGpbcyPzzdgTSmwsOvuqPh3aPx2OFRaNjexvztgWaRhHYjsBQRU_RzoKdem1Ia6fPxuULeuUE6uj3FoqDrRmnCJjtYIRPZd9-WvJ7AUq_PBAETP3WZ3vPBlvGnLKmk7MAMqJN8ellxxwxqI9Ysl9-6t5EDkDCmYp7RfrG1MertTJDRYDweSXkYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=fjaGFx2g0m1igLXXBnLTxMOtW0sedPSVWWymqfc5aHTIUKCN-HlmQo5-w7ZWGvV65dcplXpXHmLA5RZVp83Cjo2rCPqcmqBbj0iUfCzz6WiD574E37aWeNTSTZ3dOm55t-P20EzBFUVqBJiWmkaTonbQyHSDxhOGpbcyPzzdgTSmwsOvuqPh3aPx2OFRaNjexvztgWaRhHYjsBQRU_RzoKdem1Ia6fPxuULeuUE6uj3FoqDrRmnCJjtYIRPZd9-WvJ7AUq_PBAETP3WZ3vPBlvGnLKmk7MAMqJN8ellxxwxqI9Ysl9-6t5EDkDCmYp7RfrG1MertTJDRYDweSXkYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq36dL29N7GkQM6dwtBi9cv7-2oXdccHPogBxXjaWOb0NY-Ox88aF-zapYVCJCm_lvfQeRTOwhEvVTey428vFxq6jPi9AKsf0UraYW5PeufG5w3REbOezR6_v9Nv2h3fo9wFdC9NX731QqxQgdn7c8QAwtKV6SjTPmUn9CtzRQVYvKUGOw8DAKn_GGEkvQyNsRW4kl1Zz7Zcc0E0uj9V-8YeCb_kLfgJS9FUriSMWxV62qHrlTeaOFI1X1TIc-yKqe4Hr4WEk18XQxrV1KAJF1CiQP9DuorH-GnhCKey7fIdqGTWKNogG8awpUUytzW16A9R-U1l54YrDU1NAeUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjbcRtSnIUQZCdlnmg5FhIX2uWLOX2jAvpuKLDfHphEEVkuBmk3WQgT05SUd-bcXQiAG-PbabrNuVjFRMWj6k1-jXKKpn6dq6ltL1OZrbxpVM0X0iO77c3poqjsgURssSwB_wqPuAhTu0O-s2qAGdV4FHSeeqj6RAUHu__olLCu_i6R2YJSaw9FfS_liymN0wA7vheQKA3C5AalmC4LXfTJwMmwJXljtkJjGpzoix_CBOc-0DWcQMPrOdpRaLWoeISBNtud4a3qbOjVtO8q8h4vJTdgcV-iTb1gTECuFUshzQ1xO7RhV4GDJY-k3lpLW8YsgUjLZ1XupJvR40yR3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDZ9gkrlwbN3ogcGc-h0mAJlmktl3n8s05UFkcXQzfMRVPzM1hTOqimj8jFyUsyCjLVdSrdghEwAGHr3MLBPtT-KYJ5PoXv0Gp4a8FkQU02tASDudee9QxjQ1de4gzNQp1lQM77KfJvmf04izsnJOqSlDWXRqTXR5vFnr328jfs8ZNFOeBd6IpA-QJrja_bxtibEs7CDB_Ppv4lZExrDqDEJzuIZqezTaR029z3eX9QTEOjg_t1fvEdT_8pbN7WXXW3od-o5_sFXtheyGaflry5tyjHyxKlkH0AiHKINWaVLxfkGtpUkK4cycSThTGuyH0a4m28T0wFxUYXfx4LeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwtjMsch1ufA4HetBnHAJ2I2erjg8SNet83wjyhxdvEK84F7ELr4v26mBCEZfc_oIX5HH6VsKtaSQZnNK2B-rcCZYelXrk2KOmfYmvmLRz_Zxc3qLYumXLnvo1gK0JK1iwe3NbTq9BOsWl04w471hjswLqY-bj7ELhp3iyikPBfF1HmCoxEApN-_QyTut9ZSO38uKaiDRYTkc8-L5tTgF89jiArHdr89RMtPIblrZQwWS3NWMpyh42rr_U_6i6hyzrSNGrTu4OuACl59xMD6xAUf3lTDT0_UnjI4z6vvZ1VgrBLLBCVq6dGGZS6T1r2iMlRU4xtz9X90oRLx6OzALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO48vIeDxHM1nQt_NHa9WdjnITW-IaBFNn-AqvsMH4oOjU5u5ZRIC58a7URUCoy6g_oJiLLRTznswg2I5OvgbsDUExZSDsBO4IYMU_Hv1qg1LrMAv0ojJ-EqQvNbBgjY9oPRwFBIgpx7O3UO5-14mkU4r19_RmbfEOSySeF92SjAZkppaUitdNyD1aI100i4Ubd6qECnF1vX-WKabZF7PjoRM9o6n2LjFOphXXXvQyKaDJQiSZDNBYurzBq5qHwMLRHmnE2UPejzJm48clI7a6ckHfVilHZWkuRdSMhJ-TjFuguiS0X2uAza0x3Ah9fiIKU5qWWyjY0U2WPPZV92kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGre-FFffyY6HEz8-7It02g8qwFexCv_siPvt_lK9q4g0ipVpEFrOOme9a3ShmKf7Ma05dQ9SdcI1flkK583FjIPVZgRx7rPk-N6w-EZW7M3WvRkVzB37B5qLKY6Jw83tSHiivKDR3k5w-055e22yur-be3Fpovm9OXSyzC8bJnbEh7nnnWmNHKC1em_LudEy5FPcyirtag6gglmb81sBSV8fUUi3Zbh9AKN3Got-dXPLjg9aKkUhAkY8dTj2v8ykryakNhY0kS3Uia9y2qtEYGNlqBR5xOOuhccr_nHQeIl8k6FXfDZyt-OR9dsVeGgjJuXNjoVydNYky8RQ5vNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPDvu5rblTQyljMbo9hnGPdLD9weTvUBWoRXaEh4_xMXYecPgIIPGP5NDl3tTV6oxNl5b5TRXOBL_UWkX5Ru9TmW4NDtDzcK1QEv7A6GGpuDkzm5YuC9nqGSeOCEpi4chBXycq9QzP5sUXcBsUieTmtXFHtEEZ_OwgMMssLZdMprKEAhKR2ldYya81zLAzyGAR9Zi4B-beobs6OYmNbn7HKTscBXXdVwV7VCBE7kba0--X4z0UlEa4gIM0raTnbyfPriUhXAfOVsDMYNdEouwq6ECXUFqB5Du1B1XresofPXYmYiNIN0CYqy9QExE7jyESSao5DR8JDTgNzGh4TuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تاحالابدون واریزی‌روی‌فوتبالها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22351" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGyuqKJyYz0W6VtwXAMhgyWJncdL3AtBLpeA95ylnc7uOb6Hmas8DlP2vjm1qidIi8VPf0uxRKInAwkSnGqlIvd_KJxwfkvGneqYvjmgfMOEMnBEPfif0k10ArjY943fidFPpHp8twjt3BXbMWXtqh0qifWipWRkaSeLxPs_Pi9SHbV_Wm4PODwKx14OBRrtfIDQcFYph5v0LML-gMH8oA4ylBWSA1YK-xI09jBQTyNsYScz2bTEnWDGSoy1unGbKyGAju3OKH3WnvPrb5AaNE_bX5aXkyfa6bMEY4XJs5A82J4lsqzIfnoBs6x6cNiYirOm5mvQ8pcS_jqyOp28VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt2JHXTTsDq61iTwnFHi43kK1g-p4jDmagEufJT7asW-Mi_qTGtHwjBl-tMKa2ERuEQQMKVvSto8lz2jAvsMwrovcTSQiiik2-1KLhEAg1XOvp271SNQ0uPMSMByiYoIaFIFQxdC2-Ba7gFbhA4blqGvw7H6boM9qEjyaplDOT3SaOieP7JODuMT88sHRBsclE9CLJTMpbmE_ez4z2yeFQWS7mfCu_Rn0ruVB0gbcMjU3LP0fVwUNwStsdXe3twLER5fHkfS_hQcOeJgfkSwd7w6YBpJEXoPOpgDeKxg-XDUw9cuTKZSC2XCkKyZ2gi9eeqg4SCa_g0hpJK-BTd7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=JoW2_AfTlFZOevBwXY_23Qhc-d_tkCYkPxrBGR7YNGSspKUmpLoaCt-YRdXi9f_jjRWzao9r1_PXYEeCt0mIj25i_r43wFRKdTkp-kGolKSlrO71-LjLjnr77vKETkdmE4jQn2tjhmZEI4PY4vB3e1dxnF4L60kEo3mWMgcVc9tYqxjNO5anB1ogG2G7ijMRIJIerksjgon85N9TYOdFK-x-tt_R_gC2XIQFydBLRuuo18OMfdiLRaZ1B80lQPq5IjRXbrEOi4RmKrrMI2RAL7OKtLRKciguQgYjGefKEUP7rQGMrDP-nGTIsRSaCx3x4bckLLKmsAg-EuXLIXhbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxlhxWec4vikmYtDbIXItRHSiz_V0Z5cmEqaSJb-jaHg9UIglVJX5vUv-9eF9-PFVIBynzImyDAyespiOMyuw9czq21TCBlAvCijCoT6ATlV8GiL-NnXme0wbzS2sjQCY__7O1yD1fOG7rETUbFUic4Fe_PUHztzvEnDbVu7m6DJuWgtghAmR9y6qCFslhBU7xmAhG_GzRrhMakv7Bpi_tijKzwqqr5TdSizko7Xc6pLyTfBGHh_73-bC9ewLvkYDTyrGFBk1oBRz4hUjzfqiE5_xrgcVvkKW2DGQrrwkblCYyh8Ax6IMAvlEsg_Gx0ztwzZlP5VEvvQ4YgAQE6W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1yJW0WXMeCWizC5LHbFHNVYyzYn3IZ-ED18r5lU4U10jzfAyEoIGgDnACogi72mgkNx5sV_y3_vTFQ25abGR7C-pVSfzo1RbYGlufvQHV-V1fiFM87pygqQywj2e9lgDAXUU6HpacFFxK7wcUGPH_I45h-mJWUssNNZBDVvbS1F4JEJk0Kd_o9iQFfs4Imn2Os_YGJD8vAj7leU94ZaEPleGlv5qF0Cp_ByvM6_IOh49nOCxDHqfTWpKVd1VdOCJFXGEH_oVdcZYJ4dXRE-XBY21uD7MXcLLbQT5_tyGTak1U-7M5R_agr4X3ONjYU4dLRKNX0VeNu1khcOlR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWBmPe_d4xPyR9oYyMcTBQwdqmszxRcMuoDI-ZSh_YWb7xU4KoNgdEGxBhSakNjRhtEIhqGP0ouHb8bbkQIkgMD-Pq9HVggh5FqlR8bmv4nW4gpaHb5_HiAEfQEjudEOFehknNSHm5kpFjyRa2TClxVAuLjFoHMyRWJe7JM_DwaiCfIdG-vhatD_Su7d6Ysu8L70crwCYeA3BPg7eTqi7WeimMXrxxpnmWoWHb-J9J29jFE5hMeIFicPjkw_AqV9taqfmkdM1bRiv9ym66BC7bT7pPswOxbBE6mejfS2GHokCBDJihg1mVqS3Un787Y19WcNba9BD7osdKoij7DFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXCXlT7yrbtl8LURdqvUcMzlv_cmvmFZiiyBhVbRc0LfM1NPH8LKUKyZj8KcVGxOyPGRG1CcTIwWUB7EI95Zam0rEDXqvvRimCf7bXYNVXkUFExcscncuy7A8hKfOTSAIvYju1UTcO3u7QEu8jPgGUZUiOn6HAngp-D0Q4vtT7Ssq0zN7BCKnLKFr5QhFVQfJ-iVT0-fmPHeqERD03j_-1yxahO1LK410RhXPOvpym6aq1RVYjpQ-pPBnbspE-NyyinZhv4wskO6FcUGljeSRFgY2vPSsLUCNF3AyRfwz5vg88mCoZOv4MmwYV4rd1EZqOUWELIEYHG27FU3-qMyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsFjPn8wZNPaVob0Ni1PoAaeCceN4Km00bGrGimnnFvpUFIJAMG5FknJD074vFFVBG5tdUYMVQakX6jOfmvtnHdhvpRIa6IFjppNOcArdoH6pyWn1AiO_5zL7U0ynnsJNNYwp4sq9d8Cw8bhcRnqnSwuFzL3I4xCgQKFsqu1Zbn3HKZNqYnM3dQYWcBg2wo-s3VXCQh2gFatKWKpFGhTFUZKH_naLMmF_f97Qy_5JmiKDciOkGHXSJ8RIHpt2WcPm2QBsiSJKAfqbwkIjrsFerNB7GAc0piAs6ofAxtChFZEbkJhooogiJ4gT9eL_8fLlXDoZm071zfqiqWFbg0kBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5e8FPaiqfWko3OzqohdJi6xarX1ALmKk00RoN4NUoHmd1K3tTy4CCGVP8jiRl2TFTw8e1iiRzisTs8QfSy1TPTpxYG736XekY7COaYV5fvnd1sWPvlelORDrIGb9QaFZjsmkDHejsuDSo2-18L_RuY6ZQkG4s2keY-X9ZsjG52Y07Kc2e6XDq5ze8ybJux8tUjOIvduiTNKJ1Ra16qL86QArBVF8v864yXrxMr6KDG6MBdahXy3iVcRJM3Sc8aYiTCLHF2Rc6DeU6yVCGFNEUM6_N8xxIUoGAcyQQJeVVw4TazkLR5HziKAPQZvJLwlcaJ9QKhMLtQZ3spe3K_gjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsBJEBq9kXYou_GdvGEokKh2cjeZWO14SqJ-zryTZxIDmJljE0-O1MwzTpHVe995mz_Xe4d7Il9YKW1sv8FOrEdbVN82M3S1vx6pEZyK5U2g5Isa8nQ5C-K5dXpUYbBDbC1iU6uRbuPkGuy6RYCcZqMafpBq7pPu-KE5UQyg3LZoqGLL_fmlOTgjBItpd_IXStkKfhsIFcC8UjDOWYKKjVU2FwdpzSTJR2jlCm3HQomQn7jl1_8AY1YHwmejZ2F1iOJ8ksSkPNkAK_o6qAqNbPGgubjyzhHCjFiIeA6y_oQuT6o9QiOEaKTa4G2nLa7f74ceUvAqTO3k1WMJT4EQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYk8DPlorYhqsaXd81Dy3nWs1DyWWHUomE2oi8ZcjUY9LDMb-ofLW3MYwAPHUyf8n51c7yxuShceN8Hkhjdk4KFGXudzHJoRf8xDz7TyRaghKd3h94uteBEljYPC4bJai5FJ3IIbO7qOHkBjT0NGgyaMRgT5j0UGcUsUsAQdcR7W49pNFIvVHOghY2cykbXBWpqY3pu0XeNcVpXBE22gHWpmZFMj1NhUpJ7uXtD0paApWuhf7JwwejfZyIu_5OuK7m8u5HlVnmkBbsW5-YICyvWAoGqd4PwOHiG0-SctvkyTQ-Pe1yBlBuNGadX4J3c_02RGb-1hYZA4nB98YaeuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRr_0rEDfsAwJVoAUV6DIbGZBrsYQRTqG_mkKrmEJYQZfnBja33CEjS_f81hsXuLjmLuoyAdLK-U_ljq7RlnUKlSrs42tuI8K-3gCVKYCbpPhEvPFHNo5C0K8j_SFmWku3Nj2Arck2R6sxWeSfdXNCZMrfZuIctxdBny7oWqPQj1CAc7uIOZwANgbaGEL9VRt674-12Ya5F6NJ1kpWhQlHCAmWUsv5_hzbZ4DYDFlZRg-jB6dNeFuRKeX_gzbeg1Xh4dKgG1THeuMYY_ArIxJ_VIkLLuxAZNrrgF8BtAUE0Sb526ygZtfHFlpUu_WB3Q_u3gYuKT2xiAEqQy-07BBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxe1H_Kx8MsOYV28V57etsy-es-5mnCawTBZH8XoO2Hqftre392FCOjbAfwZU4LZrups49rFRM3pXfbO2ixajGh28tCbSUf4bAgRAK_OaPX76ne4YSh9j_sP2irMA5rijELvooOEVXWCa3ZuIDWjEoofs7DjHee49palkCQALh-otCLCIzc0phsbXaCaRR4sZYZFfboh1KalKXKbtR7Iv2GNGV1O7vdJaj094Gh2YwnHbI3sAGKUZU9f27EknJcGd4n2MESNyoZiiYFtPZpK3CVBXlMYEV9htx-HcbJw8nBhdLiSc5_qBiNuckK8FWkGmSY06GOPducIyzcDCKVe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKbdgTUk5iNECfNNdQ3nCAs5zqTwL-LnT6yjBzHeC9u3SiMnv2uxVKIzWFzm-DGwK-xubZ15v-MxCKiiHH3bPX5wGfRhj-u-z21-q5JflhO5jdQFBT3rsqYfEDQfS6jDhRUOl7zgC9kZYevsDKRHEEiR2feVjUIm4O6UVbTy36oR8zEJtBJEuBbKnZK8xhxLbLBWk_beYJd8Hogb9otHzVVskkKVCFB04MsTiqv4cHpkLMnCV_zCVhDUK3vf0OaoqMDXTyA04mmVwR-fBr-AFU1WWP4MoHBrY31wlJxrv2q33Fm3JwRLVnUC0Nknwcb5BSdZKqal9lk2js_3_5MR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان‌جایزه‌بده نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22337" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=myBjcAJWje4zr2Q4KsA7-WFhDK-8OeKJtDyTYu9_m8fEGseGZvnGCIAMj6OglF6y6k3cvq7unSDytGb7e9wmr_lcyqvJCo9eDbFknvI6wiumDw9crA2_ql7u30s11XrnZt_k0Baz7g83P4sus_ev5rXOAiM9YMUi0dP37UQ1PkZU6EBSOX_nfM38DvwxuhyB58yS5B_JXIgKXbNbhbjIYLL5Ro87WjzTigDjbUpXVipuehMObqUhz2vJnnMnwrhXnmjNPHY5LSGV9E88iip-vGXbFzgFP1NGUnioNam-nrjnSwXs1y2qvqBj7d6Wxf_OiDNdlbCDBydl3bTbVbeDjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=myBjcAJWje4zr2Q4KsA7-WFhDK-8OeKJtDyTYu9_m8fEGseGZvnGCIAMj6OglF6y6k3cvq7unSDytGb7e9wmr_lcyqvJCo9eDbFknvI6wiumDw9crA2_ql7u30s11XrnZt_k0Baz7g83P4sus_ev5rXOAiM9YMUi0dP37UQ1PkZU6EBSOX_nfM38DvwxuhyB58yS5B_JXIgKXbNbhbjIYLL5Ro87WjzTigDjbUpXVipuehMObqUhz2vJnnMnwrhXnmjNPHY5LSGV9E88iip-vGXbFzgFP1NGUnioNam-nrjnSwXs1y2qvqBj7d6Wxf_OiDNdlbCDBydl3bTbVbeDjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNEPCKbGkvacZSQFSjUVQS_Zmv_50VxdUEccUM2EUTZ6oyXz__Olr_JsfMDZJYDdJ0X5xOiCsHcFZEcR8q_AeiBwdErg2J8MQxEZCNqVndZ4-nJnJxNGwDZ9SOmJdfHpXr0dZPoFG-aH2pZwXwUNBQA8TPBnI11KAG05YJfd9nBjcl1bQiGy0KICAKQ7vMdNzbD3D4WXrDyQoe3itzDk53Q2Muu6hJpxyZdDOCcG5jLUP-I5COrGrfKGlHW7rHsUEbTX7UeStFaTv0dGJDjIDC0S094yG_thfWqm_NeoCERZNgQLD-vjGmi-LPdcPXzvMpgGInl9YZnE6sr3qhhv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHNij3N_YdBGl2P76VnBcQskLV-jpjImklFIwPT-GfsdNQ7OP7BhBfKVQdkRZllpkHp8Er8gFi4kujst33bS2pGlvkefJtwID49ztSZ7m_qAr14bbWx9slglWRkhVT_gSthnVyr9CRMnEXz_Y6mXG_jK5YAOiva08t2TL_25d-u7S2IQdBWcgw4f4HyGgqVE6YPwMNCB99zDDjqFDVTbF7_7ernWlOVk9leSok-Ct86dMDJG9-_LaCGJtZq_ngfqx_7PkZZ848QTYVTXyKYMoz5kJPIQjeSTg1g6Da8OGQtIg7yqY3ui185Hhwp4nbAqd3GXPGSrkwlcOdtJhfDz2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwe3bgpyu9HkRx16i_oASw4VAcZEmV0EGfZuWs4vKpgknLLD_eqdIfBxhjNLff2vSgUpcZ4XmSssKBmhFnZBUljzHxw6yyrWR2OD0uaGApDinEkjnUGfiRtGgnttfaAHWYDoGChmbCXXkSySA4z0yLiirzq5vsIApo7YNyACkwM8eX7FaagkAz2vAhKJ7NyeqAy5lVme-Fne9ol0uewxppTVaBVz-T7qSovcVlhZH7pejIhNKmOnUSGg7iOUGTEoz79gj6D1b1TWkdZABSAYyY7QfFx42_Mo5G62CKmtIXmAXN4ROUC9UZTsJzLe83Q3WmPFVBBdLYnKl15U7Tdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgHO73iEAR9IYF6ljvlO37wILIn77f2tiK4b65Vw2sT_qredBUJyOtaQcJl9ic4kbPZ1Y3evF1O6ihV98vETebnLfANjGRevXPR5R37fUsU5wm5vHSiKdCOZNkpkXO40XPokhkyd0M_qtPTWGks0B7Mt4eNtdP8DnCe1qoK5rqX8oyH6NIlyFRO_EbWL-9K69QjUq3k2S9IKHPRCMLesBs0npc23jm5no8fnezW_zj2hDiBtUTCwiKZG9zdRcdL9VePL8OomBTuJzif7kpCTrLej2sAKUwDvZhWs5gO-7fZMLteWX8XVbiukoTWJbTz2UmRqTNtidkGyjf26TRcitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBTgQACfYl_CN7dTBCruiojJH7S83Y8KNhxrA5QSQWCiDksSJhkYqdHVqLxMB6XQwcdglK_MI5YXDqooduH3XtM78AA1LzOOBpk2o2qWdnOXj8rJwD_YFfVxZSlkyMLgT87D0rFHvcFT003r82b8fXFfResjB0sBcb8ICEyHE8RkCCBEt52J1ND65p8G4f4ubBubfHTgZTLtLDtC6CoZuyYjNy23YeLg5Ou2q8MdOb1_ApTfd5j9OPpdv-l1y-dFVR2x7rSg2z9XJONqdsQdvU4Af7eYJ0MY8qC7Wh-zqiwGA9qZxmQ6RlxsyhsshHvkmHe423vO-nlGZknY--GQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqSu6RVfIIqbwuCeF7F8TuwwhNLgqI7BVF8p5fn_EOvI-KdoAo25AleS4LkCNLAsH2cN7r1cZx-x8L6pG_vySHF4sDP1xF4SmKCMv8pqmi1HjykxJ4JQp028I_1JYz4YnPNXYSWclQMA7fJnTHzA_tD9D22S8oCscDqrLkhiyiP0_9sZdNlMOcHKJ_S9ka4UHbtUguFhvGwCAzJPBf5v_tv-PWCPJdMjLITkAv2wvRzZ0t0a6gGVYnVrXKHlQ4pcgAzLx9Ujb4J3DcpI-vZkZHwa2vw_bdU_7DkeOqKOZqW8wymQB1ZN1K2WQfXbYdWnWRprijqyUu5s1uNbd7szjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUwnEqGfRItVXe8yNcAw68bkLoaE5NGxw_sigWpt1n5ZdJluuNKOPR6pWuZs_772H_ngnK2kqQ-CFDT48OSIDBBWGF1NU-AEpaXP6-Wf9OrbcfqF-Wqb9pJuAMOg6QHoI-fBXpWBF9CeOH1ejvKJAYGcEwmB2zmrVa65VIbdEKJ6ciI5cA1egCs_73g00LO2vWOL7l8as9tyhm31UDPbWaBL5xal7JuC8kkGp8AOaqhoEOZpYGiQFuc_Q5wymrRYJTrKsxbFG0AN7h9mRd7GNwdIjjAF6Uotlqezn8zZWEG1lK9F3H_V3sj4TJzGdqeWJgsY-jb67is-OFnAm6ugcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=r-zgWRamN6_Rl5CEtctaZxzdg8YMYfbykVRcQIt3T6yLxs6UNEBL8QDB8qCjmhCq3SMcaDp3zWfRJF4Q2XTSe1LwZI9a74Sg2usaOk9TWEJKop7FhAw4DM8m6YCbEcLGW6jReoGnj4OGwpXwxZt4tHkc2miQ2ldGprj3iULW2GLMXu7kyQH99bnG0UL_1JrXW1ZfsJ3MNReeCOPsWY1_8egnrFsOyKA2mMlit8jFJIDUcclgIwz7SZDMd-MueEZnzLlV6gfGRtA-wpr0iEjGyoyhxGA5UbXFgD7YC5gJ4FvKHOsTV3SoGeUScllkVXJNZNuQDkEkjaYCDTtIx72PlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=r-zgWRamN6_Rl5CEtctaZxzdg8YMYfbykVRcQIt3T6yLxs6UNEBL8QDB8qCjmhCq3SMcaDp3zWfRJF4Q2XTSe1LwZI9a74Sg2usaOk9TWEJKop7FhAw4DM8m6YCbEcLGW6jReoGnj4OGwpXwxZt4tHkc2miQ2ldGprj3iULW2GLMXu7kyQH99bnG0UL_1JrXW1ZfsJ3MNReeCOPsWY1_8egnrFsOyKA2mMlit8jFJIDUcclgIwz7SZDMd-MueEZnzLlV6gfGRtA-wpr0iEjGyoyhxGA5UbXFgD7YC5gJ4FvKHOsTV3SoGeUScllkVXJNZNuQDkEkjaYCDTtIx72PlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8M5opKiah10NJz7D_W_XJ1L4rLk66o67ObE9lMPYkZQVOsiRMJrzZGI2uiFSzcIOf3ab5xJLrj8eQ1Qii9oNRzttX3JZymSyD1o7OszuBd0f-tBBHsg2jKOZIYO55gBw_Ei-IjaV8A-9L0OUqonnW7UGcmBjlkCKXlHg8CyN1PQtyo0Jq3eAvaxKpixXUSucl4QHjF1CgO2IbePX-FXxwmDaIu9wVX1hi5xaIizbMrVPMkmrvST6spUIfBj2UQxsHshCuNxoohY1qGxQetyRWhlbCE1Bew4UR8DEreuSGDlOs14JZc5XRsG6VY20fIbg6KTDqyg4inEmDzmtHfOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLfPuLCLW15p-pqaETdgGI5IJ_6ci0FEP8CvV_7yfCy5cIbKe8F6nF4h1AR2c7lmX8yg1BHZdQ3_VU10_pgMQBr_1Rqo7ArJiJOPL6k_IMLa8jCoM3QeDWZeZp-6eufa09fEBD_4wBarLO6Ycg7ictfzz0JXoSmLevvN1oZNAIf6DSrG6VakdtQ6cUgLR0kkY6wkjW6QsdHMpV7cVBItoKab1zH4P1i2bhbB5h-RE4oK5CHfdKqPhqH_cbdVd2cmoHniAxaD7JzS3QVRHBieif9NZXlwWywtQdRuiGTGhQVZz5wHqsQLqAOmwM40Q-W-APXNToj_lpk1I-VXmepEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=QZmhRz6-W8QM9RqSPPxNqTvt9HciOvq4qhQ4A7aPdKoEGf3gHA5FL0h3iI9HB70W8cKFHyEUIKnzV21H7-ivkvntfy7ljOv02ImTe4P3ZCkt7YofKwwZAoZS_Uum1Or_ceqY9i_ZGiynqdpvBQrxpryUztSITPceWlAmrSXqJZGj-aKoVWYW1kB2ZCxhPQJ-ttcNACqHATyoy1JOCsJlTKmP6MCd9Ae4rieQINfF30NjA4K0L2lJnzzACxHUCPuvf6OMfpmpWjfsaWyWd-Ma6xSFnu_qBUMqAnXao1D_mXqfuaRGXVIG4oz9VHbEDIx9Kv5Y45gJvM07zTFiajUKkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=QZmhRz6-W8QM9RqSPPxNqTvt9HciOvq4qhQ4A7aPdKoEGf3gHA5FL0h3iI9HB70W8cKFHyEUIKnzV21H7-ivkvntfy7ljOv02ImTe4P3ZCkt7YofKwwZAoZS_Uum1Or_ceqY9i_ZGiynqdpvBQrxpryUztSITPceWlAmrSXqJZGj-aKoVWYW1kB2ZCxhPQJ-ttcNACqHATyoy1JOCsJlTKmP6MCd9Ae4rieQINfF30NjA4K0L2lJnzzACxHUCPuvf6OMfpmpWjfsaWyWd-Ma6xSFnu_qBUMqAnXao1D_mXqfuaRGXVIG4oz9VHbEDIx9Kv5Y45gJvM07zTFiajUKkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDhi3u2aixcHTj8gXZNChJhnCe4wxepjU3b8T-iH31j1S6hn6-ng0i_RdUAykdAJLbcvTY9FPuWRf5r81Sw53hJa-XHpdxi7H6EwDrABy0lBHbm9WF9_Uoja6uGYgKLa242t6D_LNKX1AkbBblQJamcx3z4X0fAf9R54kV3pnOR25lVpepdghqjcdUXUGwsyqB6BG_3RM4R6k-_ldQXT78Q7_G7hy3SdW4xPbGfGsAjm95YFQY56bhg4EueCHn8At40OjUfAf3Ifk2FFWgXd6hVfNxxV7I9S5xOahup9U3CsxPRy79Gbp3o8XI3InBS5Bt5JLvg58EnxZw9nfTOFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDR4M61Cll2SSF5fRIH0eDDow_CqPUFfA_siwy4m6CCkASk0SOu9m0nq63fZsP2FJEbklj3v4UqPvkZ4LXlwxtfhOola8DhSzB4MI1sSaRVsXkvOXhIWUh1UlboeSXMFJj-iaZPmuxPqijsMWeG6d-xBPGGXle4OLdgVTHOqlaKkwmJ4LXbSpHoZsuUfHljhIdMyWUTqb2qFg-lfEsCn21z0G9739dHck85g8pu93eiLn2yNmcSd8cgJFk2W2GK2Ry0RzsydNTkuChkO2hQTS9o4XgGWvDbYzvQJiijTfNqGjGwacHgBitPCNDW0TLOteOYw1C4p_1gXu-McRhTDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1h8dBfKGwe-5K-i1VRwr5FfKmOscDI7MiHBU79z0eVYn6rOA46dkpzlbhzmhKMkuwzcSE408YNMrncZH_sI_DyGcHWT22DjCBzTlOtqPwKDaIu7TZlM1dBvQbP9LUVTGBqZbmYPHQJWbHjRTWfbhboptvLHhVk3vvwsPx83u06FdCitgtQBERuYI7FZFxlrfikorqVf3evLCO13XkSdBSsiv3CIYLelMzLWDqA-yadQojfHxBO9ilX_pWy8RJ7hWN5rwHw7ZAKgu6AUmm0yg7xaf4b9NZJa69leAEbPrp-NdoGR7vguhT06krbNT2Go0ifnR_8pBSidolKRoi1S1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJW9xaIJCP94202hfz6yF4229Cma8ZZmEOBB2QzysLwYepYdJvACgGTzlPhdfEYP8ttpzGrhvKJEgHcpWJaZ_Rlq9Zn4Rsm-M__2V_NN8V92Rh45dNJ0aWrrHWHnEbzFmLHs84wN2Ovcdd76S2bcjfZn4hWjtNNm4GnAnwCVQD331I4jWGkX0g7cZ367_bYm9Jh1QfRGJvmWFP6JUKpnXwtdlKib33S5fpAWHnIeLQ_exjjEGPYmfHVP2F5SV2C9GY8_tCVwXNH-3HXOzgphkPQf3GoKBh9KJgSe8riYvLtzJSlAZobTytkytCRqYdBHqOYQzJTsGBriqn4pHXjICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=SBKGIfz3hpbAsE32sv4y_YUTlueJAQ8ps_-O6Wqo8pW61qzm7hLk-LLGAtXtghT3CJ3m9v8UzzJfVtie47CSW2qHrWiu92z5xvp7eWu4MbpGvle5_f80NAiFuneC1iFpqgnDtmk8-jnmjRK2KwKAW8HLF2RMOHUyNh0yrvlSFQZ6GIK4UhoJc1HoHJwvNkQTwA4fs0_pqe_LDlrWZ8fzD231hj5Hfy9T1RdWcp4W7lCo-aDT73v6SwuzvjkkK4_60wNlO4SpzW5HEw9t0u6upMLj0kmwDoPEnRRn7GB6S9OR0SdllcR0J4yV8N3Z0R9wt2pEiLKyrQdYuJ6Hwr7GsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=SBKGIfz3hpbAsE32sv4y_YUTlueJAQ8ps_-O6Wqo8pW61qzm7hLk-LLGAtXtghT3CJ3m9v8UzzJfVtie47CSW2qHrWiu92z5xvp7eWu4MbpGvle5_f80NAiFuneC1iFpqgnDtmk8-jnmjRK2KwKAW8HLF2RMOHUyNh0yrvlSFQZ6GIK4UhoJc1HoHJwvNkQTwA4fs0_pqe_LDlrWZ8fzD231hj5Hfy9T1RdWcp4W7lCo-aDT73v6SwuzvjkkK4_60wNlO4SpzW5HEw9t0u6upMLj0kmwDoPEnRRn7GB6S9OR0SdllcR0J4yV8N3Z0R9wt2pEiLKyrQdYuJ6Hwr7GsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5cKfjyugAwh669SBylCP5tswq3nNkLI_BFyoAlEBF1_9vM4OINBdmMtfmAzaryNbYLyP-dRI52tknW9PWh81PBVdVrqbqQVnxkDFNKORizGHS3_i50wviZT-OYnWLXRkzesHr29MuuYO2f1UcPTyPpKMnM24kJ9QH3-SLWc_bFM8-BzJAHbkmDHE-cLWTnFS7WJwNTnsbe2acOUCYL2hql47JzHAIG_vVpWop8HTeGXDNmyDwGfn3suZew0HFN_RMKzlLdF1YiCbCL3pDoDhq1R5S5qmkum-qeFRUuQ0GQXZZVqSl9OUOWWx4o4CjLmDdjkbhacIBrVOYFQ7jcIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvfJJVhFfXTV7hg2hnrzwAdA8fKCpIlaY0PIpkcYU7CQ_CWpcjBTr6xJk5GVQ-LxA2EglKkKl4OD67tQH0R-K2nE_lJAgBOOPTfzs2beOaDCVdpsyADoZuktD7zqJVVzch4YkW2IwpiYU_1FUeCkwonCnOXig-cbUKI3ajlAN6THBSw_mdxalx5jfTZEBWYQNRlSjdpt3hJtmBsDdKyK52AWvCie63-TlWbEoYoaAh6Jz33RbkYyONDNI7_XO7XRL-U5F4durMnx_NvT7XbmlLlsKzQpFx0Eh3NPJUSIlrPyTz3OTYV3IdbEaGuCvqsHBCX8JeSSG6BCICLjLuzMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKzssiwJAI0pAfiMqwtqWIVz7DUgyUg7DybqNPBOjGacWR76kzXdnPKO5ROF6-622F117fIFIY8NLW_ChIEC2kjmdI2cC0998cKzMQFQVu0eqGBga1oddgPUyP6NsU0imvtQms-Pu60sc-mhikOJvxR78X4fELFsks_OIgaXsnXDlNm_mZs2aHERFAS655sj3WCalOt6GQrNlWPJOIBtjX6geSm_0EVBq8shal4SN7dSZnoum-tjMZrnLxjLfLlCb7wtd4A1U3jyF-qw0NE7E9EYv90TfqBXJEGcgZ6QKAxRwfxEUFK9-XW2NK2L66pMFZ9kYkaslNZjbXGH6lAZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQ7sbzoVOPXV9Pp16WbJfKPxDT3zCYkkeUvUdXtxz2JpDcMRxiJ3eVgZEUsNR-ydvht6OKCgQmk2Hf3Us1r2V6o6kHaxX1H78x8P0WTVXPY94-XiE_PaHbsFUjvTvVvEMCl7cNj1r7SYcgcf_V27nQRnBTfECE4_61d6LcTQjnr-HQ1WAavdOEx3FoMZi50pJ_M6lTXsdcZF1LGcrBsA_RxqT_tWaNo8Dmd64Jko9ixiRlndmZNQAZBouicJ6OFe9h_jd4ME2jDk0gXuwW17Xyktgm3McB_yLXLwSNPDt2KMjiN3CxzhGzhc7xp1OqHKrdas5eUB0MxOrU-9s-BuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-yAblPo0FVhI3F5xDt0SGTI_LmJvIyda12K1730x8yJktlBiL_L_YDFACYTky_foG0Uox-QB_w-51vzJ7yJWguslAmJ7ouHQZBj6b_-K4OuidEYb9g6i0wgfWFktLi9g_Ry-Ela4LmzaV8_mYcAtPPCFveDx-cT2b2sgxes1HFuIeN5f6ZUB4wgDRdRfaVdg81VOSm9m3bsSdto-YjcMP2dhH4hkbT8_-FltPAZY6M14hVDSbJMQ4gVqQYmdGDz2taVMmUEJjQGPbbGM5sKYbbC0lc8Gtd56hY-1U095uuiV2kwaRmY4Z-pipq02Aq2Rp7scXS8-9bLBNQ88u49TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8OdKkFO06Hjzyp-PYPsqg85PwwvdGo77TZY52RdCG5ndg425vDWIcBjFAViUrQSCIHXTbilltnvd-d8qUMDDkiHfAAR-ZPJ5fog0_deS1i8EsEGvnlmpFXLbBRUm-GQ6EAjstpJwuQK5vOxnsuSEGmfKzfbJEQ5na9GP2OrKhB2ZLjgNrg_Y7WRMVBqdLtj8OxUm8J9KXcdbQoAL5lpjZsFpNg18-LcDfNPXHgC4WfSoTBcWoTpwI39ycdboZyZ8sID8x6J1M5cXyjmjx5RqjlKmGJfMPdfqOj7NNwNzEdSdFsbaVr28J5DOYtzcSCRnWmfxfV2c9u3K6c_77R7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ndh5LBh-T9nlJjOVDQeOLqfFyCCYrk4JQwGe-AOkE1lb7C5VdzjCK3sxapm3Vdn6NmiKZ0dqfwjQDqLgNSWK0PujYnUjYpdyvCkjMl2UJZRi-RENIifFdOqA7C5Sj7gC6s2AZQ_f5XkD7gxXXSxoYutyZdqEYWBrQBK-g9f3Vlr_mIWCo9O3WSDhY2vA5APz5kyQPhLf-sT0YmDQNWyntpF02aq2mOWZXyncQrYkWbhwxvOolIP7lXteUnyzrl3ik-Lmq--LM16r_2SWW1wMJVYGfhaj_wglhGSsO0OYKeE-diHVcAy3KToRXbu6mTMda4pai69wpV7urntiTQwfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-CbO2dsaWuXVZhivMfaYEGRe6OpWAjcbD2FQGTafrObIor0Cg94odVg_ssYDhwP5lWZ1nFOnBfSsNU4n0cUdRFngD-Q-OvdGcuif1BPR1PZPJK_vvQi7KUpBKpUwS0kBVHFgplhnYFCBNQ86elGAVP7zIcjnFD_px6lj1TzmFpoxeZl_eWPbDhFDI_WrWw639btDF5dBqhHg-kqkgZ7BNT7Re54HTp6vehNFO33knbnWj-74iHS77cbU201LL5IMauZ0JofMd7N3nPY9JMuPxLRE2PtDZT2NoOkCuZBd8T68_cDNq0gJwmfj1tqyOXeGOfQpTaQeob7L3cY1XeFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVv0aAMuD8aiKd48CvIoTqzX1A5fKwwnwvOS5VpVwwSEpa0GxTY2WH6_YvdGy_uxLfTkmHzoGMpnlSD5Z0EJaCHVzkAX_RoxV40NBIKs-BnzBYzTgOSvGRykq6AylPA9UXVs5syzdm0BqfY7MdKr-5fKwxUPJ__OnW1iBxABrQcQyyOy8vaFETZQpDhDZ7GpMRlxCfnqw68Wu52afpvjP8KVsfj9UIzswkcdUymTyGaEmV_El2v5_R6KaMIozDtBE7gqDQtBaBOotmLQzAE8iLfbwCm0QKUBFvuSdFh27gdsCnvZFDZJW1GxV3Z9oN4-g5ZeDq1c5Aqv6Xif6kzL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPOnG03EctVeul4Qy0iEf8N1AuOBUw6kb5a03vCSmBQcX4EU2iLZWK28l37vdVs5Ki3MoqdgoWhyeCg6cse2Z5RS_8lkVq7vLxPfD7vGFALG5hDI2A7GCKkIdFzuo6uFNEXStMQ70k42S2gmVwj0cL3WuXj86WkNap5VBFjDftYjIxJV3ibGJ_Y021_jnTNrjH4rv98MRfPx-uG_WSVMujISqenvs4aKAWRPG1Tv894MseQOPNWYEvfnIOZrJLqGzD96ww6J0w7XcXAc18qrnAyHtBeWDqHvcMTcHDEw8WQqJv_zdmYPyQZ-lj-Jma_H47dRtgH7jItoLasHmfMtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtfbv8nKcKKoEC-FmAvOJBs9HPm5m8s0hjbXSs6fDfKhskH0bXDJo37qhTQaUYNEWt0H5u0PjxmxP1_2lwikzuJASLFH-3ixuk2xD-1S5Afup3xUzowSC4zPwyVPBykQDoNAm4ETR1FS11-Dsm_OwM7dG6NF7iGUd7FQfdiVolsJZz-M_85zypYKc69FpZ5xnY-eeX0NGIse6wLFcXCPX_5XZJWkUFzwbwFnAZVeKdrcreYD8HuIiSUt-qdGLruTl_DQ8cfgIIxbd3WWo4pUvfWWFYB75pv1HZHfUpCG4rek33dioHGrhB0BE07J2uolhHwWlKravzQfpDYu_DshCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDmKmEC44gcV1-CnEgpwodU5AiDRDz9pF8_dGu83M5xCMkq5wLjv9BF7YevSqWO4oKj57_RdO7oTZe9P7cWSZEgrYH0wQS9AcRYSktQ95BZGubfFSM5T6qFwNRFqHXtBJM-d8bMbpkOgXXBAuLBT4UF8mXiQe82ufyYs1WDq7okRL2hsm22ey50R6r4K84ZdGQaXurFySgkXaZ80k-7V0ZsSMJhTzzDRQm1u8ALj6ppQMhLAzms7J9GbaEjCb5ykDtuhoPOYchRKMiZQqcvEEqy7CJ1P9kTqq7KOOaDGxioLFLfZiKJIQ9HWnfz4VUgpsMa09gKZ5KZsIicBqvssCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SW_EQw-q05HcTwPSISNt0NVeaq846hbG80ULTBC9WWe0Hsg6TbGntxgG2Go7FL8L6KJ8aTULpZjQY738LyJG7ngnwGV61EY0GpUEehGpITJHKBXD7K-3l4JXuzDRuCpNmcOuE_xSsAXBrMWV_YjNohL1Sz3SDo64F_71g88ALUVHApdOdGQWMJNtk391ZvUEOCsH-OqQeh6AN0BiDDEEdKkCqbr_hgrzy_aJSib6j_CkOU8m1AUUIVRPrkYGZyKyJvVW-QfISNlNZ1V_SqW9IvpBQyoXPalL2ULMSI5sgZShsAsHXiub1_2fejEt_-chcSZe1GZialt4_ii8bxDoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqHIjBQRlxNpGbXQaDqp4IAckX5XymSNlVlIoTvOX8DJJK1PMfLt2LEbNejxlcBzyZs9ajzHeQvTcHqi-oHVohdj3W8AB-xnfPeEo-AQWm9WggzmHDAPdMURq8sWhUZdynRLIa2TiDXGFP4pYgoU-126jG7UqYelGNEvVX8N2FCcUcmITezgEMgIo5udfEwiI1EA1TOlpGN9h1ivZZWz3-5SvMw3X-44PK13DBjOZ0bUFxBCwV-jYU2bOrt30ldDbl9wPoWg62l0S6TBhJnZicNFIXXe8pTFfU9Go7YIlw2Q_vLYbmKa4BlzklSqRWMqaYJ5FmzPwAsm9yGagpY5_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trZ99iqtXPrLMStngi_lq7hY3Ll0ZNE36F2EFaYUAL31CXuFO-xpeO46lPBBPNqE06orlU2XqPf4LiZ1Zg8nmE_AaqjYB3NjWTaLRzMWT88M1cW8KabXeeupaG0cPQPS0gtLxOZ0Jr5HhZwxqOUHys7IWTE50bkUbt2t-QjKqp05dNEE1GfBl6xhQpW50eP8FOpX9jq0gSGaTEYx_mpa6sjuPjx5Z3YIZcpj2i3vCVQhZPwKZbgvhFxfW-85gtxrDd4xVUJ5wgl5CHVWl7aEU_mLaOX5wn5WbP3hwH37B12KbKDHHzXaB46Qu1UpyUXbKePMJL-A_1u1Y0_Alt1Ziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbj-93CH6Hg1EWCrg8wMTmJy5__ALLFi2ttTAtiyomuBW6ZFmHFJ7XDdTXOmNTfo_Gs1AJOeeZRrr_1cquqETPLmNFr03NPH6qVK1AqrQ73JYRKFrGUW670ISMSEHqTQl90_ry9gt6QRr-sBbrJLLTGSUpKLGccF7qAeGujwvvlpMW8g6-yCadshlAM5__ezVGZIv8Qfq8jXkaRzD13N-yaMLKoUFecGW6lv4OCTj0GNsYIhuCc8KLz0vLzIgwL5GIBdWk-Qs9afMXwvL6Q6AxLO8qJtackpTK1XTB5kX5z9CbHnXN-bMRslL_j6I8X4d7GuwdZ6tjRbqRqKaCITrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKG9SjBg9m6Gvhj873cEtO9AhDbvY3TPxmSPq4R6W3MxHnNHC8QxpE5msJJmqGSPMdzJiG4D-HRVeUMe11Y0wku2Hx1_x0DMhfNrxzw2X9Hx667Sqf2P9HCBPmVOqccuIMNI2C8wf34FenW1BVodJU4qZrvmy9wufeKs3tgIKnMequG8LvfjC54WhthCHRTGPOtwqFjO58mIjBGUHF0E2OVeDFMZRyroC-b4R3MWcL7QhhvzuV8Hs8rZZQKItkX8v4LP-CaNwrklX7n3g4Zd6E-63BXo1abTadzCVE2bdpFn4nsIbam4JP9w4PM22h7mfTG3Fkk_sHYI6nKrNFLpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx0qVMQNl_L_BJB6psOrq4QiqdZ-M5RS54xuhr1a-YGsNcwFf1eBsVJFZxEyeQzFOUGrsMir9nHRNi_bapNc8pZgD88Jzsf6vLulZ8EsWeLtj7ARzQxocJlfz04ykLMXgKHqaBvqhSQSDq1SkQMdVYdmm0_OhBwYsXV3tNhyW48yvCeZ9w_Xn8wbqPJvNTVE6y8qj7S_5KBo2gfq6a0MQf99DiLugoRbctKVuXocr-3txrRd1kHMWjoY6RUlf-mpGDa6BlqN8W9fN2wWTcOrKY0nzifo6-RX1qJNbtwnuRRkxAtZAi_pWFFOnLq5Mj1TBZJSmqjCn563Wx_eLl7KVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDbjbBKCiRmtbKa5_t-1Vls09iAWpq75983BfGhKDV1B2VFD_ytaNnHgTgjvrHoxjegQ77TG0zwx23Jm84kPlSQLb45EQ6yOOJ8iaZotHVaYETT54wwZNhXmNJjpG_-pbqlM704bHdQAtKe1gHgDBvyg58hTY0BUqPpTDHc16RhQxxwntfg_xbNqhsj6FTSuzogeKSClO73gJHIgJK_u3ZygkV4oj4yxkDNJ5TCa6wNvhBv8vR1doOgroR3rcK7osdgXssQ1YvnVjPjySKrtD87ivyKXEgw1Erw72S9IC5q85Zhf98vOjgh5VfZD0axYJeVrqZNVZD2xVQ1v_ttOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETUZP8_kI3oaMXdVgWrWWVSWuNOZyJnCGzCHUd4GfAI202NmnUim4DKrLwYvFT7XnLiB1bsEvExF1vj4jCYMEr50E0X-fcdDfhTcRmrqRZdniP83gxywaR3GrPJc5dQnD-QFk0Lq4tiX0FTHZagxwirvAMVOuX8GC8EMo3tMZ9k4eAI5WMVYazGu_uEN2mJeTaxvVSRTfK_jwBhwOo1CPxAeEpP7SBnTVjIey9mwHuQW_vqUmAkeYf3jbEpuh4PZSdvrgwzx5gFAoLIszc1xWsr0qqIrvr58oqbLzkUdrdkqPc0BY-cGmmvRrU4g8BehR89ygRHuDLfnc2B36QBQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTpl6TPfj2uW2gMucy4ObQN9OSeTX93yXeFlNH6QGuIhWeeJ1_LWUWao_j5RtcmTLAPYhRl2DvWCThEPQVMerlKY4NAQvbqbufXieMpA6PLVT5QFDiHl1sR4-YWDaFGtyD9KaTOFo7rFtmnE1e25DcGnM36_jIf0TvGlDwSfFVN1u4eNhQMhdCjg5RTizZxS9rbxDJih6LOSDtmViXqqFExOCU0B_aJRtjOCb3gvNyQMAfJhXuA_zl2MfmuwXUUB7BWp5dpa7eKTrYyCPxi_oIvR_0glY70SHYzdRyAMgm6nZZnXnA9vF19auaR3XU_5FuI3I8m8SrG6gXIlNFooyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzRHYxMLZHj4oN1RkihpgZ486pk8Z0YO9XW3g8pKubS3vkKXlGGaskfZGfSaUa_CPWVEypxubaDVRZYIgk5yTEiva3v5Cho9VIrxiOlzXMFkSjeBd7TivGYqdWDj6ouoBq-BNlbTXJQ0saLQqNdzVhgHqWexkqcVFhfYJ68iSgF_b5D75nnNCBTpXllqDtCA3uGvISAWngpB-u0IFojmVOzIdKQ6A1_VQJH197a_sqjSfwrcLxwfBjDjLUUjpSHOpg6kMc-VGBbeV1ZSYnrS52TSW_KaGMftufi17-QHCu7Z0-YWO89Y8kP9h2e0E_U2zF7nu0fFtjAIb15vaprTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTrChPZwkzFvC1sayr9es-Uec3Af7KF3_iftZacNS_co0N9VQGeuzzQXOpnHBL63knLfmjPJO4RRLbWNCA5fKz93MuBLPJJoEMJ1gfFLcZ4Y9z9Y5KxZX3q51peXLomq0lX-_NYs6FOg9FZ0pbHBipe2SU5_hSfKJxz-CgaX7yq3RomMAK8nwg_daHXnH3LCNKxlOvVmwI4qkoqgK3PbJYhhVptkP5gtIx1msEpbUmad4M2qjVUM_l9ENWkmmSOBSWaur5nBwnPL4EACH2MrQc-nG7CXUlyy7bLlDyIYFgorr-sNLxyZ4oMlR1pikHbn2UU4TRVHpY4CjI8T3lTt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSYlIqZor1gF_3VQK3dTPdo5bXw0rDHfHHfvXVeAM5f0zXhTXF1PT5QtrRl9KnGELXDdiPrSTUTLDnKh1WEAWA16KDb2TW-kIWJxLkR-U3UXHRm1By-NSgKXpNXy3Elc4TlpPqWq7WozRieFNAsT9cBEX7lKR1-wdrEqgg_Z00y7KEu8HH919nkdUPygWHIKuHSlbBGQLr8U-lje_TtXbSaKVMVUQ2SRzo9PdplbASzdWvZxqO70j2bZTsUlvYgIguG37Zi_vHccqVw2jgrP8A7eM66kWdhI4IMhLPfqZMdXEKrd0oO24UMYjLicUKZdf4pcxNZg1RZNW6JxeilS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUSYUSZo2ikSWXfNNhYKiySLTp3NpsU5h5iU3NwqoBIrj-rirOSpr-Qafn0rIwg-6UTdqtz90KLmEiuEJqgsQzJvfEptH-qWyMUfoeeNXinbbNI95JPIkfIzdODDVSno4YSt2-zdc0jU1bNPExQmlenyQfZ-kvHNCk1CMw7w9atGY0mmBEsTwzsFYaY6Bxp5NwXCuZWTln0DKV8-_WwyAiJDuwCFIHuUeVvfCTAG2ZOJ4NZiMN5wWGdDuZ2e5qt1wNL0rZkm6G8t0D60RSl-YW6QesB-rMw9RePa-c2xw0ZgqVx2nZlvQ_qck1zb5R_cHn3ViJ2zwaJZvlasFOn3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1XiRuX1euYNyyhJ6RKkhWL_x7FyknWjSTvYypTSU-WFXzCg5QqLDNwB5qDcT4hEpnPWpRlWEHV9sJK-F3WPp9jPoVMZjToXeOgYd9GrwEYUcP9orNSRVLyuvUMJjOH7dmH_VVwGJdbbbWDP4Zwrh4ge1fRbHKoPbLx5maCuOD3Pe3UMGPGeFx8M6ODoOKQXyjen5ExCTh7r-rtYSpAnMEGAUOm-O5a4wUO6syC-KtWT0xIBOE-ZEH1ayDL3Q4gINdn_clWnWLxpCzJG7rOYL_aL8bxAVMNMze--iRha2T5Kp7x1Ub08VxDdufD7dLiCdABhZceMXYLSFNuBqHYAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj6bix4P29fg18KMUHfmKnrNSSnFhXVw59YLhaSAHN7VS8GtLL_IwnyHnzDS3ppV7S2LKID9pcgg2muDJcKLIb-orqSQMNIxHS5RkaB9xFge2NvqMor0MIXey5EMZV73p-zCF07VMSKGpAF1KDAWCPjNCZCFW94ZIC88Xr75J3BbEFbvZUcPkCKSgg4dmkh3jD-92IeuNRftVIGtIaOMmawfaswYzUO1XEfoR5WTAXiAVZs8OwTM94nvXbzk68q8H_e94tRgLT3LV9qV_tVnFRf8l87BI2LCjNehCl2gaTlby0qXSpeCNoR42zmuAy87lNQiYVvahyGnVlhLGv_D4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt-NDauYvxTThnWXOMq1ZnNyRl6NfsNOn9TIyK6Cmzqjx6AXcYTUH82SuHhGmvwWhzOWRYCquxt8kYi8MkHFmyY0l4ocvdrVmVxeLuwQoF4ch8Xkm2iXG64XxocX2NwGllEYxVvR5hjMHVXcZrb5XEasEj3GyFjwpj3-JZZFk7WdOb9H2IfNDC62b5JA5k8ZqZxckFK7oSgKRfZoo9xurH2qvFKRbaRJMXjHtT5Go1a1clPHsr7vJZylcTJt1okvmutjQ4GKXAIpWnjQBQ8uWiWrtFbipmbuQ4snTu2Ajg8HOsEnw7c_fzn9UQ1i-7Vy0M6G0dDsLa2jlhUXcCv6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjV3hGrmLpyWurTBVz5fXNnLiS97PtIbJxjvDloQ8FMbQ7z7g2XV6YJdBKNqjBONHW4cPLdLRSwkueJzUD5Pmo72dH14tnZ60VwN63jMGNqR7_F69xa607bzKyD1MufodylCFOVcE_XLH__r6l7_1BnBsRdXis7c1lbjIUTP1DxTcUTtZHw28EgKDioiCy7MdJujVCpM5CiPKm-nUY3rNYcPFcADHkoqC3xFY9vLkj4ujnoimLEAyBWXx6jUBf9QoU1MkEZMD9TiVkOM7NaOjSy0I2nEModA2YsJT3A_DgZtMdy33ZuQQgyL7r-Rh0hTO3zuzvV3WvLhhqvCdcv2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l85_AAZu3987XA8yQZGBeMHZZbwhN4o8C0FOmfBZYj4PcWq775_Xdj9Rcsj_sw0vp9bohqUj3_9-rQzzG70hGYhfIBgj5RgnW0zBDgS_cPJeI0s5mFMGEOcv_8kL8iRuaiiQJU9W455LAUtlWF9f-YEYN5W0i4c-IeBPa9Y9_s-IfiATDMAcGgTOaVqmXchZ24Cqspdmd6iI9Wi4vT_2p4HgwIEGts0o0XXmgr3JbYXAVo5eUqSychktoWnUo62dyS2tvJs-1TRLRnEGathLxwNJFEBP2dGTMONERqqGkgA9D1BsY1xtDe4f0ZeULH6wNe8QNl7bD31YAEtExlqm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0c_pEFdZFaRpoMbPAMfcfTALSNuXfwoBR0fwK3shE6PG0JXnGkEIKHFR7Ty_ARk6PfRDQfFOpnEsZ3BBfFUq3pbHqFRQ28n_THRiRw_b-RFduEzDCBQ-bcMb3PqZg9XMk1_Z6qr_65Q8sVYHp9xEmn2Ghlw79paQuaZYkrrHHNAnFQRuV_kxN5hg8JOkFQWKulQaGbuLBX0zG0TjFBThu06N8RPQ0EpLMIoivXKgWPDf2PSjqHMwU1S5_bj5aWiHBrLqCSf_oo9YWZyvRByAxlZZ8lls-ZP5J6zpb2H4yFHq8e9HajbVn681ZRDtrS5RTqNvu3z4-7CeR0ymPIQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2Il98NJb2pN-1WMZJuOlambYO-SEEC9Irb5EplGHBQKCZGXlf7ZSb5539bUQPgoj-qRSSWY3Ey1YnI3uT1TDH9tAlSUvpp6yDVK-Oqvugq3B-YBbikPOTFmqykVpkNkJ6-DfAtsO-v0nzXSxZs4VJA-p-yWMNn411FqIYgLxoGX4Xe4CpnBJZatQ4ZSrMEk7e6Ci6bf8fpAOu80GQtq7v2LhzkD2Oj3aqLP6sc6rGPqxK32FS-Q2SJq98I2JOEKUWgh2GiyiF0AIwjHmAgJJpUlxPsbi-YDOYH1XcmbIBkuAhUEToWVo3nKDPRIiNdvftu--d9xSfBHGYnRxhrObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJD9eXbn_swpxSdssS4ANwUnoSV7G65JBJ8cTYVsglXOJTlN3BvUDKxW59XttlTqn5HyKuAbm1-4JaIAV3Jxd-KitAT1MtI2hxL0Aokl_8LRzqW60eTouAGgE7D3yHGCInpBvPHLF7uTHFh-YHNTTChyGEchJUS_dkijDT-mcuXAFD7AavyCDwIiYJepQaiJ82qQZAG91jUB1NXEiBD6GgDPVYKhaWp7YIwfOLRvmEUSUJqsGdjwK1viAh3pt307V4kbTNCKp1Ijdux7SUv2GQYZaBpsnYnuhqGdxkgqm4BsHPjX4yxVoQwvvPTFuLROkLqq3JOIBoQqQKIJzJJXpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNcWCekhXx61B58i1eYX_75Wdb3z3g5kR5M3-qp18yO-vvd1AN96JPbH4cDdCybeTN5DM-jaO6HfVeLtJdtVMBDW_sbjBNQPvcbGYUo_gspGlB47NbuSsO0fPpkmb2ojT2a_eI6XQH_f0Gpw2n-QotjyhDd4MuhDco06jKTN1Sh-9rvpjqxQHdjENXbHfjZNWL7gG8kJUH2wGfr1Ndp0TDy21qRZ1pm1ToIuyb3nIx4zC2uU_x-PxTPcW04-X1vJx719eTxwxm3GhUaWV45ADZ3ygidRR_1R-3FDqB_TEMX-VpAYgQTMZ_4eEFQisM3m7HzqFvH93jYaEM45hkcMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktu7BNpV9jjX0l04NoU2iwP0ioV2bG7jIM_NHS0FLK_OaqYaf9ckyfqlNxVVIW-waEGAf4bp0idVzCROBPYG-krqYiUDlzyL0b8rHKnF-8feSkJanSsj-etNDZoXjRu4hbx6En9zt4KJQKBPW605i7W-izPT9IaijMUTDDImvEdhNFeqLvMhyPZWLDID11NtbhGMnP4yecpbNFVfDuBrQwq2MERQuDmfis49O3oP82EFythx4IEPKs1EOFQewv1vN7fVGWK0J32wPN27yhz6iScqZ2DwUQ_Xfy8LG4c1lhyrfGp2UfmGhear8P6gR7xQflw4f3JAUP63HM4nAPssvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCXSzGd53dGTdv6RcODhZZGdgBGj2f4YOd6G4pXfi3yOMaatUBlUymFugwivpUlAKFjpG84b3ICfrJJjs8S-5Ys1AWND_WFQ2rVHoboYnsgBup6vw2kPnJXiRYUU8uYF92kX0aPelV6n2G4b2U2Nok1dvCFlzXcFXgywoTR8vAVuUCobWy3JjUuvMOHx7LQzA9w-XMQS4VEs7SRpPB2_bCEyzbKlZ9_T_mTam2K6SrzCETCrOq32xvPxan-AXHk6fIJZyHnUC6VvygCNCCSq_zK75lyXPthPD-a-ivzpec_Av-TtlpljQ1qrBDaRfbqn47cCCoa2t_uFL7NV9NFjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8GqHJ7ChjL9GuDWcPAh5Q9pDUA0vQiX_vzngMf1zVW5rSvH09f3PLUSqmPlrpEY5Ef97jAa0ODz1ev1esvI7bDiI7On_hkv7M6pR5aHOyuCss4s9gK7a3uLw3nX9ZxHDaqf4v3TkD7fl4wpTHkLxuoOsRTrDL69wJ3nexy_ov05-uDn3Z3CMGdFDhICOQ12qoq0Cir_Mu3Gf3xGUsYIsD46gdGb2kA_DrH0ZgIwQEnuvHw_JCuMkikoYvJeFZ8tqz8YlRaoCFg8Q3VS94AW3-C5ZmxkrzAwh2PHP-rITXxHJoIrXdDmzZiLjrs8NzN2b6b4GzbFL4ynj7BHg6hl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C36Fl-INiaWvcu7EgWevg5-UB7TdI8oPTRXjP3ou3fOVhn1AWAmOhUwaAzP7t4z_UN35dO1G2Ibka8t3T_d_EBEL7Bi3mDGhrn61yKtOMnh6xw5KuqqkYaqi9_Mo4hYztGoHWK3q7swUuX_M-RFlz9JO-E4PK2WJoLoYzGx-C3S3-XROlKsS5axxdZc3oeql_pQQf8LmcfhYvIKAkBhLf85DZfty6AYl5BHNXK5lkgnWj0XvyenpKt5hEnM0iRF-7nSp26C1vu5c-1Woj6oaG2MVJv-Ef29DQhdlwO5EjOBhyAaxpGiqRwd4acdQkNfbFoM1_DA2-fYW7WeUbgmNEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAuch7PGNBjbASEfvaaicGfPXYgAga2BjmZcFD7g5JVNBpCPNAdJ64neJP2auUc5BnuW39j2OyLpCKZV9tU-h2WGrNWlGail7SethDydrKcwy14KOF9b7KvyI_v-HdBW_mzxJ7mgeiUbf8KJC3ruELKlrpwjNUll8CJ-Y7cLiw-G_aIYrzPZsnb9uujSrjCPfxgyTjluswcjlXlXRiFVdbTpuL5e-qw35Fvys_7wL4-jtDvjAKafQFzr5c5BMni7gxPpC1DjPIFcfqAUjEGSJrgMj8VETOewrWPUIZDjt3rMvbRD9heyzWnCx-_D_qYU-x2GePRtw1EbO3KtQdKbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGuW8Hp3BbIDe2SVDT6NEhok-OGofGTYlhVjOabe_pMIzR1IAnsWgsQVDb1StLXuyeR8Pqk27CwMG5kNXBC_FQTvmq--k7QP802W6F7OtzHzsYj6PHWkgv6_tY3-bTGgn9RdkNWwgeI_bFfHTQGekKygwsW9Pi59s8xo2DH1czPS4oSWKGadZOQD8hkV8pZU_N-UnxdtKNR0YHTCr740YBerP6j6A6958-k3EoMyaRy1lX27F95sE80O2YVglO-t3N4HOpkxELkChLjx3SfxPCcP109n9O3AWcqVrf4TbH03wKvTchdQOKcR8h6tvSky38_DIjZKqbHggi8BE_MX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVzE8zb02oZsA8-lfIxraNyKRx6J7JWBAr4LYZ2Kzf3INGBOMg9bDI8tH6aanTnvt42O_fnSmPrugKuwHiDD0xIHGH0Okvrs4KuY8hhgqN3_PXUneNhVuV9WOhPNM2HKoUPwLtALY8AM_FpTJKjy-OquodiUtkOkfVLrJBJkHrigx_7WMQUj_aOz7axSKzGC-piI3jZJbPnE7wUeXewY9X3tBAhqMt8w5GU_hsMQMThm8mgBEMiuPt5TKtq8_ybgvDTZxX48W0PKO4y4SThfDE5HOIZcMlN5gzy1U4I76dVpOYzTNZ62YxpAowMCcrBe17m2xqCthEyFusBFdpRQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZDuPJrNK2_a-qcFVuV4GVhmuso2GaxkBWKpqYF457KkNt6eNtYVTizEB2r-LJaJIXU4dorMB7KAUR6Id4qGkmQiyYYL88_LjNH-iD7XbOP68HK9MM88GtiKSuBjrME7Wt0Pja6TcyxI7QAn1cNxUxms1iMMCLZP4KQowv6UnzusGeWmnKhyTzaRR6sdV7jDjVqgcLlEp6HR01IrXO7mwKh8vd_6szc7FChQxsl_q95QnVOc2aCzt3OmHwcwwmbsc0JENH3h6uRsg7yfDUim9d8-rubtN-qvV2DHStfOG0qcWeDrfDHOYE-cF7qjPMHga50lbhsgzfDLn_UVTjCx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzFEjidttTOxIov1lNcGwW1zLbmzBw9kAj3EO_Ow9HbjGX0WNdB22D_2VgorFV1kf0aVaNjlVeU0VdogEzwq2claZzBwJ0_8ex-whkhUFaos7JapFPyC0Dk9VQHpUI1dvsrdvY7L4KgyBWxhXGVICdeQh-5oG96M3hyI_wEkkK1Kh2a0_9Nxj8eKKY8ohxLo02VkzJGYtgttIuJUGL1iv0D_O63yrIkIzDOmoGngxhEWNwY5g0XuHw0ISvhCaUv5WnuCtk7Ngk64_l6fqoHut5nc20_B5LsrS02DLWPy2cmk6xcRb787RYl3cG9-l1c7AU6Sv-xGXp-IdwSpDRmOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9Z058CHa9dnUnA_kaspgPUIZ16unEwbWRtjJrw60b-Zh2WY8QGQilOMPBPK1wzL4lNB37tTrcFk6XTl3PNxLdvdGijYL3GYboyUCtKz4YlPkd6juDLpMdmvOYMup3devIwNSav7IPNvtJsaIRFeMP9pgRuJAJoqDy0RBNokUdKF5WF-pSrWKa2ckh8tsJukRiPd95nJlH3kEnEgILMlegjyd5JGKZISQB7nGIUdyXR2TrQG8HWSdZTyd6vjTYnTyu-VK9bxnUUceROYKhKndEhEhKlyFLBH6eijqUMVDONCG7JEbFRvhEbSbm5d5t8OIpvQqSi4v64_uZt3aAiHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=EmnuD2W05BS6veehQWD9kt-YyhHnCfbbQTh-coQfboUuqQ5Obis0R7CorDRFJyVPjxT4813glKKhZh8EvGqDPhduYBgmvfT6QfVKE50JW9zKBCBOOQR5YPM3Kedap3ICxUetMB3mAmQR9qeoVWTE4gyhPezcyUaAR90AfAO1Ro0ajskinmVsGju0Dv-k2KCf3PjK4Cq9rJ-GglhrmnPcCHGGkRALINAl69iBfVHLRmVOy-2J3X-ec1TE91OURdKQgV9do-sHNmH9R3sndhEvVyjQ8ExV8wpVmkq2Ywg9OfGYXANvLbiB2Ei0MU8iPKWPZWZ7N4ab6c_l01TBLPGGVlxr507CerXOXKwu9rDeppHMyFOzDp0kvcuFvkNMliNQl4xFaAB7w29w1T3KEAHl7k6Sv2JVw65TAtQDl1sqYD2o3k6IOhUc_3nQgI8gD75EFJLdkYASNt7ZpW04huz9RhIba7wYUGvSzdvTJNpxTVZbcTwtULDXz_7kN1_ly07yVFndNC8Kz2m1le6THP89oElf_uqb0yS02AF75y2WIfMHO_xcKlsbs5RC1fuclbDA-hL6DE2xxKANyynqtEi4CaNtKn7ELmsW6ES5ZokHq9yH0xaFnr9lD49cSl94Ww_SGcPqO-hfWrzpTOqb3HFoNvc33pqD-aj_MrLy7KoEMl4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=EmnuD2W05BS6veehQWD9kt-YyhHnCfbbQTh-coQfboUuqQ5Obis0R7CorDRFJyVPjxT4813glKKhZh8EvGqDPhduYBgmvfT6QfVKE50JW9zKBCBOOQR5YPM3Kedap3ICxUetMB3mAmQR9qeoVWTE4gyhPezcyUaAR90AfAO1Ro0ajskinmVsGju0Dv-k2KCf3PjK4Cq9rJ-GglhrmnPcCHGGkRALINAl69iBfVHLRmVOy-2J3X-ec1TE91OURdKQgV9do-sHNmH9R3sndhEvVyjQ8ExV8wpVmkq2Ywg9OfGYXANvLbiB2Ei0MU8iPKWPZWZ7N4ab6c_l01TBLPGGVlxr507CerXOXKwu9rDeppHMyFOzDp0kvcuFvkNMliNQl4xFaAB7w29w1T3KEAHl7k6Sv2JVw65TAtQDl1sqYD2o3k6IOhUc_3nQgI8gD75EFJLdkYASNt7ZpW04huz9RhIba7wYUGvSzdvTJNpxTVZbcTwtULDXz_7kN1_ly07yVFndNC8Kz2m1le6THP89oElf_uqb0yS02AF75y2WIfMHO_xcKlsbs5RC1fuclbDA-hL6DE2xxKANyynqtEi4CaNtKn7ELmsW6ES5ZokHq9yH0xaFnr9lD49cSl94Ww_SGcPqO-hfWrzpTOqb3HFoNvc33pqD-aj_MrLy7KoEMl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLuk1-jLwBspIcc--AOJK5305awk43SBK6FwSX8W50_p4gLOb005Gw0olzTCjgnPtDHbry91rjrHIhpqCSN_6IPCHHJ1AbNmBrzZXLhYOVK3br7LdoWFVBv6CdnMNww3N6k1RfMp22A7K0ocK_VX7FVCmwgTe8aXenmnY5uG9m_fOU2KrypjTkp2sZYhEv4dw9Xr3H_8_9n6IE5-25MN7KhJUPhgHK3rBkIyaa5wTtUkFGWu4ayOni1wOGEelqaAUCZiGAkNqcm3mMH77KTlhgZlTWx5niB0PgKomptvhn0M46dqqw2tUk87T5xQUam-SRAIQUhlRc1Y4zMXKsqT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=nfCoqG-1uezPz3lXZaCXwf4MkXSbh1nRFmWWTskjfoT2st4RYLI-hSEvQanNgZFZ9tIJGOkoJ0s5goumAAsS9-YbNJHfXLojeD-VU5cigiWz22AYNb1Hcof91o768ipWiS_5aomNT2O1yvqFMuZ2Aw9ILZwfboG_rAcXhaasaYB4HLNM_jKw5tTShMF39nGFElHgZfNDMLumb7dT37TwIPcL7gIfa9oBsiuLL4MoappZO1G1gaY0TRiiwn2gDgGDMHNgKeB6W1UmbylT6eXF2FEVrAIupf3jE34WjNG9N2tUu0N5yblMmIymwU3jU1J8zM601ReUB7SxTpKVR0f1xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=nfCoqG-1uezPz3lXZaCXwf4MkXSbh1nRFmWWTskjfoT2st4RYLI-hSEvQanNgZFZ9tIJGOkoJ0s5goumAAsS9-YbNJHfXLojeD-VU5cigiWz22AYNb1Hcof91o768ipWiS_5aomNT2O1yvqFMuZ2Aw9ILZwfboG_rAcXhaasaYB4HLNM_jKw5tTShMF39nGFElHgZfNDMLumb7dT37TwIPcL7gIfa9oBsiuLL4MoappZO1G1gaY0TRiiwn2gDgGDMHNgKeB6W1UmbylT6eXF2FEVrAIupf3jE34WjNG9N2tUu0N5yblMmIymwU3jU1J8zM601ReUB7SxTpKVR0f1xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSQuydh0voaGyQyNKAd4cgUeeIsIZlHBXeqdiwP3Y24E6Z4AXxBa4Fu7yjbtjdZc0jLBuXsgOM-yYhFBEpg0H3eKJcTy1QO19F05CYZIx4BqaFiCT4a-GPIdXyJiby6Wrngy8AUirt7-j9Yb5LatfDa3_IG3KAdvtW2Ds9hYQMS6qFWio0nPi3Lc62K0rUXsu-EeBcQ68dBnj60SurjpJctkK-8_QP62baKIJv4YLyKovWBjesy6AoxCnSavMqBQERJV3btscNQPrFCB3i09Wsn_XIdmNokrwadaTYMbkswiFwFJa7egpz8XapgxmGLn8JtQ8PoPopPmAwm0Ar-qh8No" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSQuydh0voaGyQyNKAd4cgUeeIsIZlHBXeqdiwP3Y24E6Z4AXxBa4Fu7yjbtjdZc0jLBuXsgOM-yYhFBEpg0H3eKJcTy1QO19F05CYZIx4BqaFiCT4a-GPIdXyJiby6Wrngy8AUirt7-j9Yb5LatfDa3_IG3KAdvtW2Ds9hYQMS6qFWio0nPi3Lc62K0rUXsu-EeBcQ68dBnj60SurjpJctkK-8_QP62baKIJv4YLyKovWBjesy6AoxCnSavMqBQERJV3btscNQPrFCB3i09Wsn_XIdmNokrwadaTYMbkswiFwFJa7egpz8XapgxmGLn8JtQ8PoPopPmAwm0Ar-qh8No" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrC3pimB_Rrfihsw2XIJrZ2inEz_1ZYDQd7YmfgHb6Mpau0p5pDJTN6ZgBsIejcCMxfUUn7cQmXuGZZry_libJkEOLBNWfWnLEsIzO4pWd7pzS9z219yS3m0ne3vLos12zmy4oB6mjSFmW9SBwCHxaR6xuwX-rLcGEczL3_qqqv0i-BO7ZAjeGGcti4F-K4Qt81ZE1D7-OySjNzqDziZOxNu2gAT6cCgTFfQSMyK8i1kS9aY0pMIponIvZo4pJIYuTtjUiZvaGLMJCLjQA4nk_hUd2hk_T9JpwHBXYtMsheX__G95SQwANEq5ddt-7wDtEI7eaIsWsSICeOSfuxYmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_-Inp9LE-q2v6J5qondVXbSrVQlQb4BXAVER_dECb7URdVUEcW-tjPaocZ6m8PytMCKgybf0aVqBtxx5KJya517feVt64W_cAsfkhm19DTi4S5aY2PDSG5BJE7mCdF4NdkOOiLe2pPj7UKLwF2Ak6l7GTmT842pZQcUIpKUSY0lPMhjg5hnbCGm_MilVj1XmSErPLz89XySb4VPLouZ4VnUysMX7ZXVKIS0Rjo9x2Rm2FFVZ0PJxxFU9-ty3Z4dQ9vw3divRGgVLDng13XOLtiBFg_R6F_bPQ8HNj0EjgF3itmfKZCQAaRghr2N-gUL0xSGRe-oWTL-bp-DREOIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEd1TB2hJb9FNIaUtJGeIijMl2PKBUNUcWdNhmk5caMjWGAPiczWgN2THiRmv0zCiCWQ95kGO5_gNh7Fefd1DvksYtWKFE0Av5GJAFKMnhxAwWlPpsZGr0mVO37RIfg7kjO3AhB4t4SXzAgHFLwtvCcMwCI02UIeSKCJ9KNbB_FX-0sjJg_Fjtp5tx6fQw3YV_o7XF4gnmDvpWh-W9j3cuisNzkT9fk7tQf6_ocWW4yYMfMEcV1pqTskJAKIBc2lcKhS307Rt79ZBlcFXIrBiiRm3tZZlGOKYsrjfH-EfOrTPGeL47qAJPB3_KwJ2HAiJ6HJhZloGdnOtByQtXrlaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB7NXz0tAHw9UaRPXZ397PgS9Gmp-ZHaq6BJp16a4GWtns_o3qq2trD3wFHYwWPigF-pLVTPr3mHlaLKiBRplDbsGwzBmkewEs1Cmwc-c3QI752aGQ0Udx7nnB5Nibf1SFTHCZDIjjxd-X-IkjXDOlVZ7dLAgjtCiYl1iFIIbIjBJ9QjfwC8xB3TJ79AaaD2nO811XW_nIpyIr00wo_3-oZXrT2qQh6i6_Vn76ZV9Bb4pq-QNWLRhCyu2Al2ppa1u-hbCVoLA7-Z_PydRT9rUvhPbCJbaZIjIKqoeda08-KZu4cnM4KtX2LE9sObRtdaI2gclSCGB9218ipnWJzIhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtgxZXIYWa44TmNnaK-TFlWmcnj-uo_dnnysMIG0Duc5jwPkzai8HUaagCN7NrOhYPNxOTsRbMSBuo36WvMTX6WQA01dlzrp4KTIWrTo-q2wFyd0VCquYSZRKp-s1G9qATgw9PJUJFeuyF315PdjHHZ0BOGpTChw-SIhajvsS26J3YN6QqG4tEB-qpETlY-j_TwucXDDp7AtbLYfFGY3gCtvclPu905abKYoYtRd0UzwVDkYdoFQiSBnVeLu4x0zE1iQUVV3rp31EdAl29yIcmyDGbgYf8w-hvX3e-DVEHX2TiFSyXINul7lefWocJXsjDuGR58gtGnTnxLcG9XdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5rekzTLYSjrvLUgL7IH4I6SFDdcQc_wxxBGC8pvBxtib1Dcm0TSrgNHsE_oxaqz_DfCQNGqDkpvFNR-GslSnMIOTpNFr0g830gen2kmjCtsw5FCRFaBLtx_9jq9U37qRhwnUjBH5fAQvFPzwMu61KY1NPo9wtCNsx5-lDTF5gQ4a9lGbDJalbxRAeOOp9qAp-5vjEK3mWJLk8VDJ9vForyjtwVlLQa4R9UMUMMkXgTq7o4Gp-2c0ZGRjekQ-IihJ2pSIaiFCJmpwp_Z5QpAlMc_lQW2gYBkrlE7UBKe8Gqwut8g872LctXO7H_HFMCEO8oLxw7LUD9BZkM8T1qDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDy0RlovkPj6Lv1B5rPjSowfKA9mdqEBWnaFppbB69UccKpD8_uWBOyjErY0lPCglPPrQYxZBzF_8Pvx0vFQAMWJU_ehqf4ls5qQYeq-9gYE42G9PLiNoAEoUIgVkuRYBHjWUy1BVaA_sCxFm_n0onRGsxzDWD05cMn9HcvO1aaNO6eokHxn3VlDwtPdkUctE2VgVGnVYYoDJHRxWtt0Bq_OCAMaNNKQ_8W35B8EERpMlHJbjzuQ3LdEDue5YA40S5QdGn03NbpKeib3fS4drjWAnwwkQ156nDNUJE2gBb96Z9DTA74eovkow4Xs95PhJfXO8XWtW2gRpeaTuf_Eng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5f89ekgAZ1fOSDAQw_mju5nQA3utZ388611DgFiMhVPWgtwJBKQu_VvQhrnfdZ2fNRc-YP881A1ZqI6Le3u4v7NBMCHW2MXLTVSKPOpdI9WUM82JrtQsJEbnAt8z3-AR3b7vSdzBhSwck7Lnpr7XojfM8_vN_Lg0ixr_bBtlpDUTbb9T8hx-b7YPI9NVWWpHok-JRzkM_j2-Vfh7R8JKLfNT8YfDqxA73LtqCeQRfzp7mkzBcnlX1nNf2XUOois6LpchIXulFDahOf7uJIfgrlliUG9x8iFovqT9n9eaJY7pU90jyhwSFPXcDuneQduS3SO-Bo2kK-cqR57HiJx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyrfvDy2ioSBmy-D6Pu8yM7-mVfN5fg14moUZkNoDehsq3aInKj9NAA9eB7D4FNvvzkwAn08j1ilpK7jnfRnhoMdpXJnNIb-DOf6pFpWpQTALjLGHP2FJNFUhthhSzC81lwdXa6DDf906bAzPEVNmLdfNIXSexkM4DgUHtkgWfuzrtWpcWmZ-buIyRzXkAvemNssdA3NZb5mUNRq3HocCb7Jn4jYsrMXZnbJO8nPUGqtGPGGaW7xailgdL15369VhlIPvxYKssRucfsq-ReXC2EbKtC3VB89egPdX3jzd00aONbIqhRVGz0jWpvyhWgTDv2nfGthTKneACbIhBn_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZHVhNOqMIqYVufr8f0TffqLwHtYCeTHw74DZj44iog-yKGkW1TUiO1wKawbVPhgJgOsG7uevmmTFZVgMu010WfGf-cb21kVH66xNvdswY4vQY5Nu_iGOQWzt3MWvagqWTyK_imV_VUa1Bng3vwXbET40gdJx54eJFx7oXWbrRM4HGt3DafxkJQayhih8qcx-WVW4n6rhs8Vv7kj6ZZpmdqKZOMJGqd8O-IDy8iv0oxgV5_wpRraKfwYLtgR6TMf2cPoP4dJQt6b37zfJY-AF3jFL4bjCXxpx99N-LwlJj-ofC0QYVRkvClPBoJmlplPXR55zGDzny-9yHfacvzocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVebgkEaVkKD2Uq5g25QOxq0SmG42aiFTPGMGdpIVOw5fiknIP5DL1G02hmSrZ7kbjbCej9eBncfKSP0nRqXcdH0muF5BGKUNNZy619zycooXwFDERmtDw5AAyWHBobFMpxCx54IIwTsph9ptp8ZA4Hla20fLnKdJmpfst5uDqpXhiPENafpO1QJL991TRVN9nQd-KRQ9k7GUAJWheiNuh68ovnW6ZSZDxP7eJSeHv2KXgKphkJdyJ-ay2LoqBPEDx3RrPMvKBq8fHmYdPuQXXoKTrLRNgdvWbQ6q5TAWhwIfuh7Zb1Z-d3tqgqb7wfOb-BH6BUUeeeBEVgS9sxHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGiblFwkn634axirdW0bXMsu4zuxnrj1kRfnVfVNS_cuy9ZuT9dzorW9IMCD7ffotPb6Qwd7pmyqOhtc5qknbrxQ-WWyg1B0rUdaaCWbq4hVK59Z8eTSCA_tZBdLTTsen8_qi5tVLPds8EMwosLQe0USovJr_poOcRFvFaRXDqHtXkgdIpf4T4oN02z4Y-3fOOtU5BgZwf6M5snc3lv2BVHrHzKXkxgc29c7Jg7aYa98RYw0YXKkgdr-kRsjDUYEk6Egt6AJQmid1iXI1wm1KkfbatBYBM6CrgByx9qDG3cewoloTMTH5BgablM2g7d755RhQfsKf1ies9XAO0CVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTzz0fmtSTT3fCbDf0n9KbQPK8YN4zq1ddwXDtDDpOHmXZn-qUfkgGVaQoU56XuaZLCgF2ls8xhOimL8FqiQzasXs0BkhSlJ5XkXYRxS4eJbS04rE692GiWPPRAfb8unn8UC--GH_6mQyrDLuzyjGz1-DHg00BxdlVww5YQmqYPnSINHyyIZZeryu58MutIstIJZXBuWf80M4PTbm-YL-RTsgjEiXBk6L06blH3lTymFUrMwMBRy84cteOhAmlhBh3TdrxKr5fsufSi8xsWUoVze2LuGUieQ-UGjQxgzwVvifWmENK96XdLQPenXThBZ7Q5OmzalyPbVwh3AZ5qarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjKvEthM68cVVip2qQqKuCnOEoanEhuqYOLBEQbfRRLEpHIpr8rKmQTGKcJKeXo6eSWLbB__e2UbNTrNA_InJ3YdyTiGa9WM6u7ifDVCIBBSSpp2spEG0qXjrGmpWgBtqSPCauo7iWffO46C9g6Z8LDIuD_o-kggfFSfzp0k2hG_ZS1i_8UIpfdk9WILunrB2T3jOSBoPsvQ2yo0z8CvXt2CbBqcpOLoEDrOeBlmQmWX0-zjao-Ed0VMyV0JSejSzEKhr-OBfE4AOOHvfRgLCbsv5gT6kbUS6lOs3is22AjEqLQX0PhyxTLOMAsbIvizR8eqPtz9pCqp3Zd5C7LDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
