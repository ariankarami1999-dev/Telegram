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
<img src="https://cdn5.telesco.pe/file/NmvmpTe7GEian4gTDnLLqm0XAduXjdy5fpN88Kb93KqZbB0x2dM0WJzw05c-KTePRvBOmnpjccjzyq8D-LvzuSl4SWz2Nt6TMiZ40IXy59bEbn71FNH__mWAd6qQrrXTC-cW8N5B7qHzKVJUFLo4W7sZzPF4xTkcJkD1ndbUX-NM6PiNk1TrYiuoKqi9Bjc8GREGfWOLuDU3BROKVTfEjwTU1-pvtHE_5cAoTzbc8hO_zsUhSOD2vlpU-FHE8BMHa4qyr_UmcZcRekkYb2w1_6vemd1yafFcm4Y4ZQoDTlQ5yicKkZMFcAxDd1dFErFuu3kVO1atbpSa8-IqFkN4Qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 412K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 04:24:08</div>
<hr>

<div class="tg-post" id="msg-106645">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/106645" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106644">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMNp9qeQeRh7m0CxvLIAGAT6mH68CZqPIvpxy_dFIaepbcHGrsjWNWORDy5545uKWEsK6upXGKPhgrYSDqi-vj-s4rEBfPc3ITe8-xicf4ZDAPTejKolkPqypmuQ93-mivZ54zPxIXz1McfinUB43eWcyCWocrkCEv21XrYOKqJBBFtalS0-syxwOHRPlFbe3IeYhgV6av3w3eDSu7qVZUKOqLaskNHyyRlXi-H7q1UsGVuY3aY-9TpWzBOpmMJmLbbrjjoSl8EhsFYM4b1OsdIo_aeUuCO1hRSQYUgBT2sIBV70W2m1sVcKD1ZKoqnPsnkNcmSbRuDb5PeijzyaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/Futball180TV/106644" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106643">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/106643" target="_blank">📅 01:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106642">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYybT00NXv0Ajeg5pmDLLWIqIn5lqe8_E2QUWWEqn_OhnuqEI21rHui2zniStZ_49-EeHC9eXwubhLXReql2bpj8HLyMz08w-uIU0uCchCRtebyTjV4G7R8-1Z0U58LmQTg5S6_kcj_0vV_AjNNvhdnMxzAp8JBVCTnWrlquQkRt_-zJudNecRjTt_Z06hRVyxfs7_ZiwI1mUd9UpxlLIat3FquInnj9HIYWCUIunNXVwUez2rqC_m8I0B_njCzeFlOlxFQbfzWWPgu0J4xejhfn7COsBbkyUeDRW6iCqXBKBs7oY3bWffzyZf1849lhzb6-OU_LdXPYepkOT8FhVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
🌟
یان دیومانده در حال حاضر بالاترین درصد دریبل‌های موفق را در هر ۹۰ دقیقه بازی در لیگ اسپانیا، در این فصل، دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/106642" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106641">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7H-K1f7vv8fGKXwod4WyubJCEy0eVxgwFegezV_1KHNqLb_JufrOzOsuqL7NvIJEKYg9DiHoTEZnDe7rT1fvFCPP4hYVffC31ezP2UIa1ImRvC5wQvDa611UFjQ3BCFW61aDBcK0bK1gS0zDAnuHoe-s745iF0FWRO0QHh6-ftzXfzGeF9rT2vqsh7UVKhp2wfOzkJXeTa0VXk3ADPnoyUjiZeq1ZZ3fIVFbVBV3x7GThEybJeuE_fftAZdCmGq_Xie35cp2wJYamK7cTMx6TTf62aizYORJSOFA6k647t2qvUob2OpnEORA2EZY1jce7kv_bgu4GQk_anT0Xxg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
🇪🇸
ژوزه‌مورینیو: کسب سه امتیاز اهمیت زیادی داشت و صحبتی بیشتر از این وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/106641" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl9Leew-JKIVBmWn89Yr6v1fJ0G8BwBA1x7LnTAM4OU9q0jr857oKeXYH3SNmiA_lxoDh-uQiseoQvJTzV2cvTSFvDUnxd-N43xpXxkSDjQo2nYl8JjBiCvkOWZ2d7bVpCDmdaV-X_QFWrQncOTq6aNEeR8d0AU_rnkw8sv6nHcteCZggMxjl0VnrL_ZrvLoO_Bc75us67SctSl3RTh-bPK_h_Ptqy7u5LyDPf9oAp4YUM7ndY4TTjNHEFxFEfh75QvEQvfOFEXq50BedjGzD7WQnFhLRoOUNkBSbDcG75U2OQbnUxNPMfdDxTji--gxTIv6yYBsjiX-dhwfb2Q9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اسپی یکی دوتا بازی گل نزنه، شعار حیا کن رها کن تو سانتیاگو شنیده میشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/106640" target="_blank">📅 01:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=tvChMYiGIpPfXAo_8-91Lf5k1PDQhRWeVKC6jP4QJZ13Qckv5vEI03h1oEhIrj-wSpzWwDQTSus-KPLh2S0l2_nIsAO4PBvCkdkDt6tT3o04bATarHe-iI2uK9VFlmJOJm6eI8UsRPcDT8sIj-MmM3ssvpLzH8r9nHHCsdrgVpZk472qYyp4KtK-LnfyeliQSG0gyT_N5SPwHyfqkmtSRF2jlQZ2OpXZPKggsxM1W3ag0xUkDuUueq7z5H_4E7YOtUSGDls9dFpGLI97LgxoylUk3zp-VteiNNbKF3b7sLXlZ4gbmg0wE90env0mrchH8DRc4pq6RTNbL1ybFQrRFoiUN8cTnrX9y_NmsB78YmNlcEx22AfX_8JwYCnb4KhKcWUOFuUKW-fcSN3c3IemD5_jzArpQsb-TvSG61c5M5ljDybOS9wHtvEP6B-arSiU6dthuTpR7m152er7YQAm_aHvqRIfKLG4l59WMMVtWCKsXuXQN8Y5x96HI9vn2CcwyIgbpqPj-CfhQr5Up_105Tmazn6u36w5O5eCECrYpqcJDl4pnOUGnoO42qcr8G9qojRiTWSsOcB3d2EqZ0wzPXTXNNur7-BMunrVqYZZLxVzV-8xnIy-lKw5iH5kgL77uNV26zjlvq3sKTJG15OIPBrmz0oCrrXwTjM-G0ZNenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d40ec75d7.mp4?token=tvChMYiGIpPfXAo_8-91Lf5k1PDQhRWeVKC6jP4QJZ13Qckv5vEI03h1oEhIrj-wSpzWwDQTSus-KPLh2S0l2_nIsAO4PBvCkdkDt6tT3o04bATarHe-iI2uK9VFlmJOJm6eI8UsRPcDT8sIj-MmM3ssvpLzH8r9nHHCsdrgVpZk472qYyp4KtK-LnfyeliQSG0gyT_N5SPwHyfqkmtSRF2jlQZ2OpXZPKggsxM1W3ag0xUkDuUueq7z5H_4E7YOtUSGDls9dFpGLI97LgxoylUk3zp-VteiNNbKF3b7sLXlZ4gbmg0wE90env0mrchH8DRc4pq6RTNbL1ybFQrRFoiUN8cTnrX9y_NmsB78YmNlcEx22AfX_8JwYCnb4KhKcWUOFuUKW-fcSN3c3IemD5_jzArpQsb-TvSG61c5M5ljDybOS9wHtvEP6B-arSiU6dthuTpR7m152er7YQAm_aHvqRIfKLG4l59WMMVtWCKsXuXQN8Y5x96HI9vn2CcwyIgbpqPj-CfhQr5Up_105Tmazn6u36w5O5eCECrYpqcJDl4pnOUGnoO42qcr8G9qojRiTWSsOcB3d2EqZ0wzPXTXNNur7-BMunrVqYZZLxVzV-8xnIy-lKw5iH5kgL77uNV26zjlvq3sKTJG15OIPBrmz0oCrrXwTjM-G0ZNenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
کارلووووووووس اسپیییییییییییییی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/Futball180TV/106639" target="_blank">📅 00:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وینیسیوس بیاد برا اسپی چند دست میل کنه</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/106638" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عجب بازیکنیههههههه
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/106637" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کوووووون رئال‌ نجات دادددد
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/106636" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسپیییییییییییی</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/106635" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلگگلغاگاگا</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/106634" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106633">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=sAjS8tFVVvHwBAQ_j5d340uffUZccp3zB-YCR7SHdxIlSAKajOSpxCj7r7dBY5yvhrkJq2wVibBW96cQFGS41BkixbCf_9meLtuhR55ZwOCaP_I0veIh3GOAULKAbVnndZNZmDNJmDATSNoU9pXg_aG-bEV7OQZ04LE67lAph-PA2FOBnIR8NzKj8jqLw91Y_CngcplKK53UnwwS3W_wo3e4vKd-a705-8FHGZ4u7W7HAqD9H2ykS5FAvkfAA_wUaPR_PwTwW1SJAAY1GsSQ4X-dHHtdqPXIG8OvGVnceY2EGW_2jhuN4lQ0BJ1mM0OMPnaS6-gUn4hCS3qIQyORnWtsbS4GBHoXatkHUbgec62frcaRYAmHHjgocYED0CR0vftiEYfoIIwOyAuaC98hT819KFM2RpmWHQaU2_WeiHfv3Aan7J5HcD2zupO0_siDsUBzzYIzSa4kBPUErp_75gGM8ZGSJ4t4saIYFGRcxeQTsXf_k-6msW--9mwuGjDmO2mXHa631D2xgCUlgnX2oUkkSoaqgf3qrnKl--uX6TTSIlkDPSAKjgKiM-z0T2vc2VPuUVvJbUsj9RCpCC7lhCWULAqlkf7MyD9jdoqpg5-KIntHnWqlQ9fwnJmlEEmiyumZHZPECBH2bXa4cmEuqoNYSro09g2vweI7NR-Z5bM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90c95a451e.mp4?token=sAjS8tFVVvHwBAQ_j5d340uffUZccp3zB-YCR7SHdxIlSAKajOSpxCj7r7dBY5yvhrkJq2wVibBW96cQFGS41BkixbCf_9meLtuhR55ZwOCaP_I0veIh3GOAULKAbVnndZNZmDNJmDATSNoU9pXg_aG-bEV7OQZ04LE67lAph-PA2FOBnIR8NzKj8jqLw91Y_CngcplKK53UnwwS3W_wo3e4vKd-a705-8FHGZ4u7W7HAqD9H2ykS5FAvkfAA_wUaPR_PwTwW1SJAAY1GsSQ4X-dHHtdqPXIG8OvGVnceY2EGW_2jhuN4lQ0BJ1mM0OMPnaS6-gUn4hCS3qIQyORnWtsbS4GBHoXatkHUbgec62frcaRYAmHHjgocYED0CR0vftiEYfoIIwOyAuaC98hT819KFM2RpmWHQaU2_WeiHfv3Aan7J5HcD2zupO0_siDsUBzzYIzSa4kBPUErp_75gGM8ZGSJ4t4saIYFGRcxeQTsXf_k-6msW--9mwuGjDmO2mXHa631D2xgCUlgnX2oUkkSoaqgf3qrnKl--uX6TTSIlkDPSAKjgKiM-z0T2vc2VPuUVvJbUsj9RCpCC7lhCWULAqlkf7MyD9jdoqpg5-KIntHnWqlQ9fwnJmlEEmiyumZHZPECBH2bXa4cmEuqoNYSro09g2vweI7NR-Z5bM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی الچه قعرجدولی به رئال‌مادرید
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/106633" target="_blank">📅 00:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106632">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اندریک بدبخت بالاخره اومد زمین</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/Futball180TV/106632" target="_blank">📅 00:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106631">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسپی رو آوردن زمین گل بزنه
😂
😳</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/106631" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106630">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دفاع رئال جلو حمله بارسلونا رسما خاله میشه</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/106630" target="_blank">📅 00:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106629">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مورینیو ریدههههههههههه
😳
😳
😳
😐</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/106629" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الچه قعر جدولی مساویو زددددددد
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/106628" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللگگلگلگلگلگلگلگلگاگلگ</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/106627" target="_blank">📅 00:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=u7lTqf3XZTw8knsSoQbo9O52zV_gD0B4hTvs0iSPixmhzy7hoBK_B-I5JM3On1Bu9ROYqQEBtB6__cyqMFrXvtX6eJkh4Ilt4bQC02Tujx2o2olhDQjcozGSa4HpnCJW-oefzmNbviQm0_w9oOZdwY9B1QetXbewAU8_7oQ2ccE00Qetn6VuC_tpkSIJIpLONunsPYqIfl2BfEqem_sJxqo4nPVEDi5oer-ef31fqLY40-ZU1A7aoxszyNDYY1PqjzFksV2ljLLCsDLvLPJe4GmChrZMAgXjNGpxFong8rnNH77ezlpBb-S-VmAaodrzKVKKXSI9sL8kPT4JhbZ4OTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6efefc36b3.mp4?token=u7lTqf3XZTw8knsSoQbo9O52zV_gD0B4hTvs0iSPixmhzy7hoBK_B-I5JM3On1Bu9ROYqQEBtB6__cyqMFrXvtX6eJkh4Ilt4bQC02Tujx2o2olhDQjcozGSa4HpnCJW-oefzmNbviQm0_w9oOZdwY9B1QetXbewAU8_7oQ2ccE00Qetn6VuC_tpkSIJIpLONunsPYqIfl2BfEqem_sJxqo4nPVEDi5oer-ef31fqLY40-ZU1A7aoxszyNDYY1PqjzFksV2ljLLCsDLvLPJe4GmChrZMAgXjNGpxFong8rnNH77ezlpBb-S-VmAaodrzKVKKXSI9sL8kPT4JhbZ4OTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گل‌اول الچه به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/106626" target="_blank">📅 00:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الچه زدددددددد یکی</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/106625" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/106624" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=XVshFr2GDjVGmg0q4H9cW0vUAKmRBqucLe0XUtYET1Gyo__g6mw8Jhj6R75EHkqvOG4iTpMgdTomZNZi7iEF6uedC4u444mPiNrny_a-WQK68fVt0CRtZKNSguWa7crYPlo-EaCsBOukWdtTjE1Mj93sq5uXwsUpC-INte3j-jAdAFwUm4Mx__LGRAQY8ZCIvcuvA91gtLP453Ts9ry9IBRf_jm7_oGpO94NEWxiQSJbfW6O0FnSCIokdSQLmY7kJuIbtXksjXT5cXK1X7tZWZ1DSMVt4j9qz_FNPUYVkMYMehoMoRp6ECBDVAEktW58ul-wmt8z19xCzqfErIGmqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01890ef1a2.mp4?token=XVshFr2GDjVGmg0q4H9cW0vUAKmRBqucLe0XUtYET1Gyo__g6mw8Jhj6R75EHkqvOG4iTpMgdTomZNZi7iEF6uedC4u444mPiNrny_a-WQK68fVt0CRtZKNSguWa7crYPlo-EaCsBOukWdtTjE1Mj93sq5uXwsUpC-INte3j-jAdAFwUm4Mx__LGRAQY8ZCIvcuvA91gtLP453Ts9ry9IBRf_jm7_oGpO94NEWxiQSJbfW6O0FnSCIokdSQLmY7kJuIbtXksjXT5cXK1X7tZWZ1DSMVt4j9qz_FNPUYVkMYMehoMoRp6ECBDVAEktW58ul-wmt8z19xCzqfErIGmqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
سوپر موشک تاماهاوک سوبوسلای جلو تاتنهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/106623" target="_blank">📅 00:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سوبوسلای چه سوپرگلی زدددددددددد
🔥</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/106622" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/106621" target="_blank">📅 00:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoOHa6iM_IW8pJGbbdnB6fYnkA7KhwKVGPB9kwTIp7zge2qSX4qd3Rl0o_ShMyufiqg-YeJwB6V-WDntbhjs14-sIauj5rLEzIreeAa3CDhgaaiKDhEMm1D1MiKKcSWXMjkeynWtF2SFd4JZ6OqkYnhLxzCEFlFO_RtB8olfSGkxQLrNNwT-Xt-riz8dutx1Qvj-5MWF1LUgmwclMmGU0UQNXVce08hEXPw7rU7pFTyQjqR4klhVU1221XTGGWfjwUSe86HgRWqv7lGEyWamr6mEQckukR6gLLH9uJEXLPF5Jg0phGmpF7GMfjkeWHOAzCA-VCeSJ0M6I9hZDNTbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
لیست تیم‌ملی آرژانتین برای فیفادی با حضور لیونل‌مسی؛ بازی مقابل بنین مراسم ویژه فدراسیون فوتبال این کشور برای خداحافظی اسطوره تاریخ فوتبال برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106620" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drVnztR0ebwXRgKEyYiB3VRWzLuDc30PS9ZoF53_sFlT34EzOG1JHVknfcVsgTU7z7lnOukY3Dg2wPWy-UOOAnpXzsMUXonyOBW5l52dxxkgvwnp44IslzDBhYO-8db54PK82QR5gg0uGAW0s_cXpXJypR6MistloVa61enpjPZnzIKUXPjmuS9TnTYia9lMbdWRD3-KKqlvUnTRbpvHuZSm_1tEzfLPc84aHGMQaAEFUC7onv8d9Q-nK1_uhqa2ZLVfkBcGhYr30EMoPxpJhrSlqckIC1JD2zJxLbbItZkycOkSHHfO9I07TK4LsaUSR-jKRTMdVnpIGq30gDpSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
جدول لیگ‌نخبگان آسیا در منطقه غرب پس از پایان هفته‌اول و حضور استقلال در رده دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106619" target="_blank">📅 23:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=jAPlrjapM5Uh0VPH8b-d7VEL4ULF2rrXtdJe6-dL3mEwZ5l1IDr3ASrS7fztWtVv-nnnxejrVvwIuDQ7nycDtsZtJaKl6kHxq-vA1vC_HeC_xP8NzTmdsx7DdWjFyZmeeP3ichdiA5pRpI1Mt52xttgQCtcRSivWeqcSeUinT2kgg7UNh_OJa251epiZ5lwJuPZwLxL4Gg34NL9yaPa4zQOMnBTmSKaaCueh2-GaaGQhdmN-TEeVMCAQYOY2CaqSuQZrGNygZ1Ki2SC0APVatHD7PhwMhcOvxg9seIK89mWNT2ez29Nmunz2rRGJZF3X55PywW44ltN1Ydw8XlkHYiXT5hnuqRAPWGLPkP5MN7c19tDh0tGndbOHAzQ97SQugUq-SBb6VxBQYYpfp_j-vA7aRh-vVqgZp_Zyejmh_zxZEtpeD7Fh9ipRkKdAA77oW0qoPNweeui_O1hi0h7xRV3mI0RyN0oLmUiSdvXrtcSmBViEvbivqgzzFu03EvRObIIWqyCyQy0F2v2X4OseUCv7Fopm0RK7-WVW5vP1VBolLi9rgP5-8OVSE-OmowCv5ecOBWVHY-9BfhsZFCN63nl7eQudvldN_5lxE0S4aP-RNKfPtzDwDujm3XWoFf-Gi0IsKn8E0ggq2BN9Xz8KRAI6esL_G2LAiA5QPINUstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01ef226cc4.mp4?token=jAPlrjapM5Uh0VPH8b-d7VEL4ULF2rrXtdJe6-dL3mEwZ5l1IDr3ASrS7fztWtVv-nnnxejrVvwIuDQ7nycDtsZtJaKl6kHxq-vA1vC_HeC_xP8NzTmdsx7DdWjFyZmeeP3ichdiA5pRpI1Mt52xttgQCtcRSivWeqcSeUinT2kgg7UNh_OJa251epiZ5lwJuPZwLxL4Gg34NL9yaPa4zQOMnBTmSKaaCueh2-GaaGQhdmN-TEeVMCAQYOY2CaqSuQZrGNygZ1Ki2SC0APVatHD7PhwMhcOvxg9seIK89mWNT2ez29Nmunz2rRGJZF3X55PywW44ltN1Ydw8XlkHYiXT5hnuqRAPWGLPkP5MN7c19tDh0tGndbOHAzQ97SQugUq-SBb6VxBQYYpfp_j-vA7aRh-vVqgZp_Zyejmh_zxZEtpeD7Fh9ipRkKdAA77oW0qoPNweeui_O1hi0h7xRV3mI0RyN0oLmUiSdvXrtcSmBViEvbivqgzzFu03EvRObIIWqyCyQy0F2v2X4OseUCv7Fopm0RK7-WVW5vP1VBolLi9rgP5-8OVSE-OmowCv5ecOBWVHY-9BfhsZFCN63nl7eQudvldN_5lxE0S4aP-RNKfPtzDwDujm3XWoFf-Gi0IsKn8E0ggq2BN9Xz8KRAI6esL_G2LAiA5QPINUstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106618" target="_blank">📅 23:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیومانده بالاخره پاس گل داد
😂
🔥</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106617" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امباپه زدددددددددد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106616" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگگلگلگلگلگللگلگلگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106615" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96af48f644.mp4?token=eFMiRysjM9fWGPvIDUVYsZgao5ch5zraevmRblNTJvwYhC1csgmqMaEgli3pw4kwmE5L7rTT8IpDJW8mGrL5XexSXu7yDBXyb1WihNCuG3r-mYi2dShtRjNzAEYnVMuZs52SogY1afqWjWUPTdt3AfmmP1N0V3w8ci8SitWaFXgaoHV9IO6ZCECUURGKNGW-4XbiXLJ8rnNHGrQZkflAT4bMw1HAbMA3UTodVVaw1pzlQwoCGdXym-B25vk6MyK9pTdtsScRdhzP-oEDR5wvshalubv_Y_iyiaggATFFJROUO1MFmr51YcQr6bmVnZ3JM2HPcj2aJmVDv0D5HUVq4IqEHhD1oaY9DV8iSKbPrE1XKqZwieIoFaFdjuirwG77ThRSBua71PZfC_T65UOR-js3T5-dEd60GHDajyqvITlpxp2rL_2ExmbbhJJInb5vLF_O5rNP56NdzXvAVg4FwW7zJiTFyHoLHSmFZ2HfiuXIG1c68BJaOMg2lhOY0lV45BVvDyKOmURtCoEXOZtkqnD7Vrr5TdZJ_8oqStRSyvUj_OU5hMu2-9WO_oQAtWAEwcuESlkkgw9MOlXbAiOE5FaPqJ02yOaoQJF9XahY5bNTjM7ajrmbFvGNrKEv1QfR0YCkLusQfSroxYJyUOWWOMOAmXTrjmAGu1aV9li_h9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96af48f644.mp4?token=eFMiRysjM9fWGPvIDUVYsZgao5ch5zraevmRblNTJvwYhC1csgmqMaEgli3pw4kwmE5L7rTT8IpDJW8mGrL5XexSXu7yDBXyb1WihNCuG3r-mYi2dShtRjNzAEYnVMuZs52SogY1afqWjWUPTdt3AfmmP1N0V3w8ci8SitWaFXgaoHV9IO6ZCECUURGKNGW-4XbiXLJ8rnNHGrQZkflAT4bMw1HAbMA3UTodVVaw1pzlQwoCGdXym-B25vk6MyK9pTdtsScRdhzP-oEDR5wvshalubv_Y_iyiaggATFFJROUO1MFmr51YcQr6bmVnZ3JM2HPcj2aJmVDv0D5HUVq4IqEHhD1oaY9DV8iSKbPrE1XKqZwieIoFaFdjuirwG77ThRSBua71PZfC_T65UOR-js3T5-dEd60GHDajyqvITlpxp2rL_2ExmbbhJJInb5vLF_O5rNP56NdzXvAVg4FwW7zJiTFyHoLHSmFZ2HfiuXIG1c68BJaOMg2lhOY0lV45BVvDyKOmURtCoEXOZtkqnD7Vrr5TdZJ_8oqStRSyvUj_OU5hMu2-9WO_oQAtWAEwcuESlkkgw9MOlXbAiOE5FaPqJ02yOaoQJF9XahY5bNTjM7ajrmbFvGNrKEv1QfR0YCkLusQfSroxYJyUOWWOMOAmXTrjmAGu1aV9li_h9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید به الچه با گل‌بخودی گلر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106614" target="_blank">📅 23:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVraLHIpr0ReAS6Qm8bx2XrZXtPEkYB08D0Op14BBOW8x5v-_LwEH-VxlMFq_khBkGZrb5BiINhqmAR6YfkEzYgrbiW-1tr62CnkTkexfsVascO5OYGJQoEzwqJx9nSABZL613T8R4Uxxv7eQbfS6-qcncEQs8NncPd_AAgyg6C5Slr-sQtytbcT0xv9MvuNTpVyOoZSEHRrTLRN45w5mQTpbYhJSJV6bFbNOJMTqmgqfTs0ZG38fNfPXtpMyRol8PchPcu_n6uoNIT1ZdfgFKHBXBmUa5FSv7oCsgaDu42dGVrXeD7jA4oIw7YwqiezeSjemomNgkahUxsa5yRgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووف
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106613" target="_blank">📅 23:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عجب سوپرگلی زدددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106612" target="_blank">📅 23:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آردا گولررررررر زددددددد برای رئال
🔥
🔥</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106611" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگغگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106610" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=N0Mkr2il7Nc0RAs0hld_iWqDygbLgp2mAAldtvUlbqGvJ68BA0enOVYaYlGpMe2G-ukPhV7VVW1Ut974mL7tmfh52sIZh5bhMP1wScsYpvGR1xff6-EMNS0eQKIAAMQ5M4nGbgF_hiRd85lZPaLxF5INxLUfNEKjf7int_0bYRW7-Oq5Zim161V0naY2df12QrVhCaoWrXJ5Df3kfyf2b0AdYeKrORKQ9E9JYKQuu6WbOiN-keg9twTIqe7KZu1Y9QH43otqiurqK1w1UF5w3newOjJFsA3g89aez5pmsq1DDfTj4j9vipVvYBKru1uSKgTnilI46UmkgADwAYXGX0shi38mMYaZvq-AiRpi6_hPkbQyymKalWoCr3JLAfQhxWmRDj8GJAD-nFOIlNQyaeqR1Fqv8iMTtoq2JIeYGAoKAsIeouRAvkMrL5cFGVnPgYnyFnv-WOYc8_uS9-szCzBnUORbkM0QtX0HNk0u2OKbsRwyI0cel6plvEYAm8BC6GFu_8dVN51yEEOnTyA1b9s0UPuu2Ml98oEsXcJThZi3Tdlq-8GDUQ3cU9gqd3Xu8b8LEb5sVk2uXorFtL_N-ShYcvdN14Rlbyzx413Ux7Qi7HPKjnCIVVNaR1j-cubaT-yv6rtONeBLWUReJdb0pCUh8gm17Osv_FFwmz_qxOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9c936306.mp4?token=N0Mkr2il7Nc0RAs0hld_iWqDygbLgp2mAAldtvUlbqGvJ68BA0enOVYaYlGpMe2G-ukPhV7VVW1Ut974mL7tmfh52sIZh5bhMP1wScsYpvGR1xff6-EMNS0eQKIAAMQ5M4nGbgF_hiRd85lZPaLxF5INxLUfNEKjf7int_0bYRW7-Oq5Zim161V0naY2df12QrVhCaoWrXJ5Df3kfyf2b0AdYeKrORKQ9E9JYKQuu6WbOiN-keg9twTIqe7KZu1Y9QH43otqiurqK1w1UF5w3newOjJFsA3g89aez5pmsq1DDfTj4j9vipVvYBKru1uSKgTnilI46UmkgADwAYXGX0shi38mMYaZvq-AiRpi6_hPkbQyymKalWoCr3JLAfQhxWmRDj8GJAD-nFOIlNQyaeqR1Fqv8iMTtoq2JIeYGAoKAsIeouRAvkMrL5cFGVnPgYnyFnv-WOYc8_uS9-szCzBnUORbkM0QtX0HNk0u2OKbsRwyI0cel6plvEYAm8BC6GFu_8dVN51yEEOnTyA1b9s0UPuu2Ml98oEsXcJThZi3Tdlq-8GDUQ3cU9gqd3Xu8b8LEb5sVk2uXorFtL_N-ShYcvdN14Rlbyzx413Ux7Qi7HPKjnCIVVNaR1j-cubaT-yv6rtONeBLWUReJdb0pCUh8gm17Osv_FFwmz_qxOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
صحبت‌های عادل فردوسی‌پور درباره اسامی عجیبی که بازیکنان استقلال در پشت پیراهنشان در بازی دیشب نوشته بودند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106609" target="_blank">📅 23:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=GIfg3Bu3eVCZe-9pXA6Fda7BE1jzrdaj-3y7sqyNUh6ThsvjDZ00bQnEqE3ZOuNRYfXqQy4lGBWjvB4rNEThCuXXnV2Zc4-DWQldyI0s7Kt7I4GBawZMqxbIJBPp1f6mofB1oJssponKRUHUpbcy9fFfElgvWq1Jk6w4_m83xmLMbYxXwMbPhMBOMErnD0JrdD-2pWJBixViKtadWhW5oKWEo-TSpetSgpcfLHLoOXwFo0m3K7d0jjI-YMvWk940BMYBhkqrRyvctyXtdOpfShAuTmnpEQtXLnatdTjQ-YcKETz4B9Q3wWW5NPcHZpBp6TYIEbe9NubE1gLNlqWQmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/001b323a9f.mp4?token=GIfg3Bu3eVCZe-9pXA6Fda7BE1jzrdaj-3y7sqyNUh6ThsvjDZ00bQnEqE3ZOuNRYfXqQy4lGBWjvB4rNEThCuXXnV2Zc4-DWQldyI0s7Kt7I4GBawZMqxbIJBPp1f6mofB1oJssponKRUHUpbcy9fFfElgvWq1Jk6w4_m83xmLMbYxXwMbPhMBOMErnD0JrdD-2pWJBixViKtadWhW5oKWEo-TSpetSgpcfLHLoOXwFo0m3K7d0jjI-YMvWk940BMYBhkqrRyvctyXtdOpfShAuTmnpEQtXLnatdTjQ-YcKETz4B9Q3wWW5NPcHZpBp6TYIEbe9NubE1gLNlqWQmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌دوم الهلال عربستان توسط ساویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106608" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106607" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106606" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e75776b642.mp4?token=mtRRL1zEwqSruwTP3aES7y-gwF1JERXZDrIEywrz3Q-kOcPWGQTiIQBz_S_X8BNK8unKDpcE51ZrL9oQb184ePbAlCkIUndkRQqOKXU80dblkBcd81jpkZx-7bbU16_8NmeGl3hLCQCsLahiGAmtFFqozS1zzHr-CmYkn7uR8ot49UO6IvIZBlKxHkNlSBE6vbngZ8IMMMUUTigln-vtpqE_QGXplpNCXHyQTZ-DOCC3_TxfhAU1ifTCKlCGrsI_bnKvmNxskiuiOBJTvHkA7xu5Npz0Dt2bJWmAn8pn8EpP4f0b004gyoDyPpoRm9UlySf4YbBM0zDbwcVuJ_3Cfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e75776b642.mp4?token=mtRRL1zEwqSruwTP3aES7y-gwF1JERXZDrIEywrz3Q-kOcPWGQTiIQBz_S_X8BNK8unKDpcE51ZrL9oQb184ePbAlCkIUndkRQqOKXU80dblkBcd81jpkZx-7bbU16_8NmeGl3hLCQCsLahiGAmtFFqozS1zzHr-CmYkn7uR8ot49UO6IvIZBlKxHkNlSBE6vbngZ8IMMMUUTigln-vtpqE_QGXplpNCXHyQTZ-DOCC3_TxfhAU1ifTCKlCGrsI_bnKvmNxskiuiOBJTvHkA7xu5Npz0Dt2bJWmAn8pn8EpP4f0b004gyoDyPpoRm9UlySf4YbBM0zDbwcVuJ_3Cfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گل‌اول الهلال به الغرافه توسط روبن نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106605" target="_blank">📅 22:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🟥
🇶🇦
اسماعیل‌بن‌ناصر هافبک الغرافه بدلیل دریافت کارت قرمز دیدار با استقلال را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106604" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxL2Dzu5TvxkAbw55V-huuCQ04oQHo88LB6UVd5KEn7R0PntljQ_nONMpLPaNB6f-ZnAmNJX3bxOifNvWZAyqnCQcKdgNrek4_0gEHqlf9ShKWxKCi3oBgI-4JUuVNlMdXhUZP0XyEHEV6SnWqV8c9j8jW-R4kfGomE7eseIura1SbylRnM678jGEpioTSDZnglnIDdA9m4CDJQNcFbzVNKmL2xzZrGYYg3BdGSkITHn4yBx2bzKn-Ap1Jc9VqJ3RFXENmukA3lkUD5mcA9ARGU7wMjcYJgDjTo1567vHZMLAc0l1cpk9mn7ym0Mv_ZDnMsq8gvS-TNSyHNgLIZJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
ترکیب رئال‌مادرید مقابل الچه؛ ساعت ۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106603" target="_blank">📅 21:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
🇸🇦
عصبانیت
رونالدو از مدافعان النصر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106602" target="_blank">📅 21:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=U7qg4VRhAFSt__gEGlgVsibQlonfS1zHhGpvOvvF4FBxZQmNtiF82672i3lHPPhmepLKVtke8g0Hie4oG-TbfZmJ5Dx7ukhBaHVSGEjQ9W7xT-MPSPMs3HyDG5WfbOnblLG_DshQ0pv0006xLfXiPgicRju4mTJ_jsHe66RpDEIkm3h2fsddh5KviXhWzfPQmif9FXEecjktQ3iBWcE2aQodhoCGzx7terQ5NvOvID8N50h8_7WoKJF0zXE2_F11kMClYCF0dF0c-_aBA6Llb3K5TiJ_woILPtOCq9PWmOORnzqup7yiCSY-ySTFm0Pi44KcSZa2N2tawroTP1sw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5839d9f6.mp4?token=U7qg4VRhAFSt__gEGlgVsibQlonfS1zHhGpvOvvF4FBxZQmNtiF82672i3lHPPhmepLKVtke8g0Hie4oG-TbfZmJ5Dx7ukhBaHVSGEjQ9W7xT-MPSPMs3HyDG5WfbOnblLG_DshQ0pv0006xLfXiPgicRju4mTJ_jsHe66RpDEIkm3h2fsddh5KviXhWzfPQmif9FXEecjktQ3iBWcE2aQodhoCGzx7terQ5NvOvID8N50h8_7WoKJF0zXE2_F11kMClYCF0dF0c-_aBA6Llb3K5TiJ_woILPtOCq9PWmOORnzqup7yiCSY-ySTFm0Pi44KcSZa2N2tawroTP1sw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇪
گل‌چهارم العین به النصر عربستان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106601" target="_blank">📅 21:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvGnF-ouDd4PvcHsLjB_xsNCyOWZWBoRcA53dGvYtascjkMOeME3au4dins8eJmvFi0wFGoRQFU8nbotD_GTaTd3x9CnwO3o-Nxw4urLOQxbShZLe45f9LLvaEI1YonfJifAaMF75OoVxHKNazagVgOP4YlGlRPTOn9YZtoVcZ4T_JelE3pSCmiKTgOtMvjHebyZMGdNR8gEMabaP-Le7P7iXh_TmHDXwITGExS2vRptnPMo--nh2Sv2P_WBGWi1Rew1Ex15b20CVmVHqA4RGsUw_s4PYn2QnYuCX6jl2w2Oj4mC1RrXkmeo-8i0p0jIS19SjEA4mfbM3tof3EZHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106600" target="_blank">📅 21:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=f3eMK4-UjtRUKVBKqDLLGH-go-1RGBCAJ2ZerEtvTMA5MYSC4GcN0jee8ksH5iVm9iIFAnqn4DtlYjgbX_4lpd0N5yDr_DvcNX0reiSNV1E6kJ9E8rOPtlfwW-YXOZqKpeg8PCwXXM26a7LLXFT9TPC2F0vLsc_2ufUcc1-efs4rblf-t-1caSvuzoIyQInSUioPAJJHLF2y8QvRud5d1MSdtqNFmkS9Us3SBh4dtCvU2tbcovf1POwrQ8Dtcbx24ZHAMkLIE7gGOWrKvdOU2PDmAwGmLltJFpP_mYc5fJSQFu5NQXH-N75MiWUi-_t51BE3-L6Aa2hVCc0PJNNt8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424b5a6f9.mp4?token=f3eMK4-UjtRUKVBKqDLLGH-go-1RGBCAJ2ZerEtvTMA5MYSC4GcN0jee8ksH5iVm9iIFAnqn4DtlYjgbX_4lpd0N5yDr_DvcNX0reiSNV1E6kJ9E8rOPtlfwW-YXOZqKpeg8PCwXXM26a7LLXFT9TPC2F0vLsc_2ufUcc1-efs4rblf-t-1caSvuzoIyQInSUioPAJJHLF2y8QvRud5d1MSdtqNFmkS9Us3SBh4dtCvU2tbcovf1POwrQ8Dtcbx24ZHAMkLIE7gGOWrKvdOU2PDmAwGmLltJFpP_mYc5fJSQFu5NQXH-N75MiWUi-_t51BE3-L6Aa2hVCc0PJNNt8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌سوم العین به النصر توسط سوفیان‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106599" target="_blank">📅 21:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلگلگگلگلگلگل سوم العین به النصر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106598" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=dbadIF7PydG3KKpFKvPDCTee353IdfkfR4z_qf8sk5X3Q--R0sFCxY2tL-G3yHI84z8yw4-_wuMBKV6mttEvmBi8m0K1qry3zcG_v1z-RPH4-7dyUAwbxmPUuJGsqGjr0d5QgX3FX_S0HV_cn4IXrCZ_Fjd5y4_WeCTk9JpZbYVworIjxxMBMPRgb8lTQV-Jn-HtietJ6KPZYaH-CHsLizmTS_ti1QJ2KD3lKhjyoTUfY-oXuu2c7RZoiNrcnU8tF1gwCF6KlOeSI8_Q71dsXJTiViFmtT77qRCy4HgSjzPRIawTRyZSU6vH7gV3g9laCXwyDKd6roLgktyfRanWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9f6b6fba.mp4?token=dbadIF7PydG3KKpFKvPDCTee353IdfkfR4z_qf8sk5X3Q--R0sFCxY2tL-G3yHI84z8yw4-_wuMBKV6mttEvmBi8m0K1qry3zcG_v1z-RPH4-7dyUAwbxmPUuJGsqGjr0d5QgX3FX_S0HV_cn4IXrCZ_Fjd5y4_WeCTk9JpZbYVworIjxxMBMPRgb8lTQV-Jn-HtietJ6KPZYaH-CHsLizmTS_ti1QJ2KD3lKhjyoTUfY-oXuu2c7RZoiNrcnU8tF1gwCF6KlOeSI8_Q71dsXJTiViFmtT77qRCy4HgSjzPRIawTRyZSU6vH7gV3g9laCXwyDKd6roLgktyfRanWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم العین به النصر توسط حسین‌رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106597" target="_blank">📅 21:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">العین دومیوووووو زدددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106596" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگللگگلگلگلگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106595" target="_blank">📅 20:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=WSlflJivzSOEw9vhRWTnrFldeE2V_xTbaE3xS7dejQ48iPOr6FVWgUx9EYudZPBcGtOx59v4rUrOEqvrUpuwJBWghBAGdjUAxpNL1_po-aI3VztZgPQFku_F7a-JHNeU0S5Aq9iWTCMcmCjnA_DGWIGRfekIvd8yWxnChU-q_nOcbKQSYdazLJtAU998xnXpkY5E7kDjsulNPbpz4Zzk7q4cYzBKh2jsyLWKh85vAMjUsf5d3Gt4KaaRLo8u-iMLDsD3WbGtW86K5hwzmrQz2jEwlXO-RMwpTW85Qg4e2Epw7TInrWd6fSr550e1AGLqdrzVWW9xgCR-4zKN3up6iKxlkP5SlbJa3RtSa0mk7TbXE89_dLYlmdCyHJF1fphL9UnvSW1DNmMMa-ba9gNvFVT7TksEpTeiYmOYKOQMlG0YbYohpz_gXJro5XCxuvBHyylTqJU9hPuVcn34NSowmArTGA1q407G9_ZccZDHLNuRK-qAxcUFbic1anX4WnAXe1DkFf1xdEqNNXTr0pqE2zYB8z-t8IQnJ8ccoBTz0d1PBA0Z-loJ9qYUF3W5y0UX9v4fYg8Lf8e5yGmiUtfRbSOiGIa96X80LV9U_Dyo7wiHNjGujR-5ncpRl4Y7QK3iRDVSTzSy_wwe48wnICpU8-0Jf1K1jYq0LW0vkdPpYV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7815d7dc.mp4?token=WSlflJivzSOEw9vhRWTnrFldeE2V_xTbaE3xS7dejQ48iPOr6FVWgUx9EYudZPBcGtOx59v4rUrOEqvrUpuwJBWghBAGdjUAxpNL1_po-aI3VztZgPQFku_F7a-JHNeU0S5Aq9iWTCMcmCjnA_DGWIGRfekIvd8yWxnChU-q_nOcbKQSYdazLJtAU998xnXpkY5E7kDjsulNPbpz4Zzk7q4cYzBKh2jsyLWKh85vAMjUsf5d3Gt4KaaRLo8u-iMLDsD3WbGtW86K5hwzmrQz2jEwlXO-RMwpTW85Qg4e2Epw7TInrWd6fSr550e1AGLqdrzVWW9xgCR-4zKN3up6iKxlkP5SlbJa3RtSa0mk7TbXE89_dLYlmdCyHJF1fphL9UnvSW1DNmMMa-ba9gNvFVT7TksEpTeiYmOYKOQMlG0YbYohpz_gXJro5XCxuvBHyylTqJU9hPuVcn34NSowmArTGA1q407G9_ZccZDHLNuRK-qAxcUFbic1anX4WnAXe1DkFf1xdEqNNXTr0pqE2zYB8z-t8IQnJ8ccoBTz0d1PBA0Z-loJ9qYUF3W5y0UX9v4fYg8Lf8e5yGmiUtfRbSOiGIa96X80LV9U_Dyo7wiHNjGujR-5ncpRl4Y7QK3iRDVSTzSy_wwe48wnICpU8-0Jf1K1jYq0LW0vkdPpYV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لحظه‌مردود شدن گل السد از جایگاه تماشاگران در بازی دیشب مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106594" target="_blank">📅 20:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=D5FgtsTgz0EBDhHPkn1c03sYZOoaNgnR_oGk_wdcJ5NP6bDJztczvmJnUs3-j1eVuuHbQ2cDj-xTStDTWE4gpLvKzheRwNz4mFHOjFsNuxGglp7RMfFA3Ckpr18FjcBbo1eLT7amouwWGN-2ri8zqrnohC-88ogRbUsRVdDlmw9DUurmNBzQ99y6q51vjLJmzgyRmRNIsOjYgTgpPCQiHyFP1DXxAMMlo2i8NaU6-yc9RbGRG77-7GQJpd_SM8C_oGl5R0dnIV-29eNToV8lYNJmaXOCpkzbkIgMJB6W57q9WkQ2KKsE_RCsCSETipMk00kS7sTzMrwfaZQgfPIooiP7f4dADjUDUYRhf8lsxI1gI1pL7kGrJMEsAn71sjVSkGJGmS5jeWj1AFOuaIj4z7IO7f5Hu4l6YJfC-d0wO9PuCIC2KXXCbS8aOiJexUYCx01T9XlBIkr39pqyCJitcZlOdqIonjmdGmakCORwOEL3aDXY-tfMuvcyxulXwDsyFmxRt8ED-KDBRp-q0h9N9pD5mmrIt8rRsYhH7w8sMmiDYcZHMFwtrdJxhVPv7eaRsYK8BkVsUEiYJgC-oygDf_Dwh2ums0V2J56DGXBXOAr341Clti8YB3go5LuJOHWzXJAgIEZqfKucFnOIWtQ5lUPD7ROArRT1Vb4cvWlIXsc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5e9475ab6.mp4?token=D5FgtsTgz0EBDhHPkn1c03sYZOoaNgnR_oGk_wdcJ5NP6bDJztczvmJnUs3-j1eVuuHbQ2cDj-xTStDTWE4gpLvKzheRwNz4mFHOjFsNuxGglp7RMfFA3Ckpr18FjcBbo1eLT7amouwWGN-2ri8zqrnohC-88ogRbUsRVdDlmw9DUurmNBzQ99y6q51vjLJmzgyRmRNIsOjYgTgpPCQiHyFP1DXxAMMlo2i8NaU6-yc9RbGRG77-7GQJpd_SM8C_oGl5R0dnIV-29eNToV8lYNJmaXOCpkzbkIgMJB6W57q9WkQ2KKsE_RCsCSETipMk00kS7sTzMrwfaZQgfPIooiP7f4dADjUDUYRhf8lsxI1gI1pL7kGrJMEsAn71sjVSkGJGmS5jeWj1AFOuaIj4z7IO7f5Hu4l6YJfC-d0wO9PuCIC2KXXCbS8aOiJexUYCx01T9XlBIkr39pqyCJitcZlOdqIonjmdGmakCORwOEL3aDXY-tfMuvcyxulXwDsyFmxRt8ED-KDBRp-q0h9N9pD5mmrIt8rRsYhH7w8sMmiDYcZHMFwtrdJxhVPv7eaRsYK8BkVsUEiYJgC-oygDf_Dwh2ums0V2J56DGXBXOAr341Clti8YB3go5LuJOHWzXJAgIEZqfKucFnOIWtQ5lUPD7ROArRT1Vb4cvWlIXsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
گل‌اول العین به النصر توسط حسین رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106593" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">العین دومی رو زد ولی مردود شد
‼️</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106592" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106591" target="_blank">📅 20:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106590">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">العین خیلی قویه بیشرف
النصر رو کرده تو قوطی</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106590" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106589">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">العین یه گل به النصر زدددددد
💥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106589" target="_blank">📅 19:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106588">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106588" target="_blank">📅 19:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106587">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXeSsIMXg4PzE3hQ8PK0JY4FXZtU-Dzte6dSa_mQ52odgJOR-x5n5CqepxQwMfVJOmFIYffyfCLGVVtA_FnyKCRbJJwYerDlrTsgMdtGEYywH7rfIrN2oJRvSILjp3ajyenuw3nug-jPVnom93P_aB1Gf_txOc_YCjLRRJqFKjj5vCeFQW3fy_j6nFx9x4_cKW-m7w4zORFFX5tyfvPTqqdBnfXWi8MTdR2bOmjWHDXXraYqsBhA_Gx_7QswqJQwpy0Xkvtdag4I0DZol6Q2tgxmJf_l22QnEB8O6j748CtZt7IVjqXSQ_Ce-6M_szgvN453e4QhZs-opXeklulPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106587" target="_blank">📅 19:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106586">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=nmuZprnU1UjvRibC1exrsBBkZKiV-4RvT7_b3nFf1dMPCHrO408kCT90OyZFfTTSVWi9-0zqJvOTM2DOeMF5Os6tspvjzF_pW61immwiV3nzt7m5ewBKiTq7YGFF32REoZvgEJOQBT8I8KBY9OFjS-e3EhZuq6D5rmqg0kOSF3aHQPFeIqTbT3zShH8PL4q8AO-JbCmZJykMmaEjmm7HiGMdY2Vr5hH2NY_rJmb0imyJQu8XDoG5iJpQrurfnsC8JDiVjNA90ncYJh06WQuKCFYt4Ttv-5c4Hx8QjGC98X4IDXDkml9LIjVfnBGdabuX9UWnrBLfVsVw1e4TZutV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8940fb69d5.mp4?token=nmuZprnU1UjvRibC1exrsBBkZKiV-4RvT7_b3nFf1dMPCHrO408kCT90OyZFfTTSVWi9-0zqJvOTM2DOeMF5Os6tspvjzF_pW61immwiV3nzt7m5ewBKiTq7YGFF32REoZvgEJOQBT8I8KBY9OFjS-e3EhZuq6D5rmqg0kOSF3aHQPFeIqTbT3zShH8PL4q8AO-JbCmZJykMmaEjmm7HiGMdY2Vr5hH2NY_rJmb0imyJQu8XDoG5iJpQrurfnsC8JDiVjNA90ncYJh06WQuKCFYt4Ttv-5c4Hx8QjGC98X4IDXDkml9LIjVfnBGdabuX9UWnrBLfVsVw1e4TZutV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
پست‌سمی الچه در آستانه بازی با رئال‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106586" target="_blank">📅 19:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106585">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
🇮🇷
🔵
گل‌گهر در شروع سطح دوم آسیا مقابل الجزیره امارات به تساوی بدون‌گل دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106585" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106584">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6whzucQaq_Ndfbuy0T5wFXdQG827CaWEQ10qU77WkX4UeJ8DMy8Swgn7vQP5MTsqNRxhWKcTmqRull22bLdfedK-a0_H0no3AR54ibdTsMwk7s4Vt2j5g-Dq-ceughiv_UnuitiZqSl0SkdVIZ_0eUimOA0GKqYQ9JQ7E0YYKjfXmhWCRAPrrzohJM89L2Ljk-urtyPq6NOKwTkL-mbbFOB_rf-GYiyMKENmYFH9udsXxLgNO_vuwgppXFVrnhU91h4It-7ush03wAKX9FgI-Jasl_fpwGRpFzZFTnQl2jGv-nbB1oz19lRgCenAieM0vbvhFvkE0RPhhZFJ6WlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
لامینه یامال دومین بازیکنی در قرن بیست و یکم است که در 5 هفته اول لالیگا، 3 بار هت‌تریک اثرگذاری در لالیگا کرده است. تنها کسی که پیش از او این رکورد را ثبت کرده بود، لیونل مسی در فصل 2012/13 بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106584" target="_blank">📅 19:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106583">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=hZylhoG_4jwejMPeWPmCRQryt0de-BzPMTarwEzdohJzwePJVNs5ynx-ZUyF-vmp-Hq7FCDUbgsgNzYbsWBih_xZtvTwtVS1r7NrWyAWuhr5Aqi7DcSs7fUzPJsEnILi20Cg1C8bMPEkCilnZ7Bfq0JIV-097DmEGuUKZOC7qMb-a59BvIWDKtG3YD-7-0U-yZN18oMgH7C8L2pgCuTKSal2M05zSpaljykIPrSBuOYzvzJ98kfgU1Yp8GxgmE5UCIoeTI25OLKytzPgx1zeTACjnnosnPFQdqnmdMtZ2N3oefImhY8ed96zS2r2JWfQ0B-hoLjQlOQQClSaxJWKOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e25f47d65.mp4?token=hZylhoG_4jwejMPeWPmCRQryt0de-BzPMTarwEzdohJzwePJVNs5ynx-ZUyF-vmp-Hq7FCDUbgsgNzYbsWBih_xZtvTwtVS1r7NrWyAWuhr5Aqi7DcSs7fUzPJsEnILi20Cg1C8bMPEkCilnZ7Bfq0JIV-097DmEGuUKZOC7qMb-a59BvIWDKtG3YD-7-0U-yZN18oMgH7C8L2pgCuTKSal2M05zSpaljykIPrSBuOYzvzJ98kfgU1Yp8GxgmE5UCIoeTI25OLKytzPgx1zeTACjnnosnPFQdqnmdMtZ2N3oefImhY8ed96zS2r2JWfQ0B-hoLjQlOQQClSaxJWKOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
امیر نوری بازیگر سینما: والا منم جای نتانیاهو بودم به ایران حمله میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106583" target="_blank">📅 18:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7qlA5lYXWnob20t7-TOwKsnKifY6wN-On6AG-0srL9nYBTe1twFurYwRaznWxPOUfM0nvZaQW6GeiFNjyDkq6yDZSDQ1vwn04TA336nB5N0hC-2Axc68YcRPPsNhIrWK8b3Ct_YCIxAaHtM7cXOYFntNOOR9yU1fk_XmZthmXKk2B1qwn_uI3O_TivugcIGGiZCjyq7_1ah9EKV-ASBnHuRy9r_Riz4Bwq9ohsiKXvMIanQfF8ueJYpM-AAyM82VM3XygjFxdRbfVeQYmbjj8rgD6MtdKw94-_uI-200ad2eUYK_XaJDafnG5idvvll_nKIqODEhiw8e0SNH9-BgqOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cfdd069b.mp4?token=Okrn2lclBCLnNBQidkB-GVp-6CALJxbcTYcCm-TJP7fgwgTYEt4A5_Lm2uWNoOkOB0F-gcDMrmHkcMJOTsuNxfg_z67FYJ294OSY2KqLaYrScykC-Eqt1KYqmoGZKnqupZJJhKW5swTThljqOTE8SFZu6Wp6uLz1nsXme-KDU-Et2Dmkud5BJWKyhG9ZanQjMO27BQHrsA7dwcM-f3xVJ9tf4GE63CWpzFs-ZVTriNOvIG7uRb45iP41TrSOF8nu0cF-cj5FMgw2U2wev1oReM3vhhAqF61vIHA0nOAn0Pyx5AaWpIoeQsgKjDe6N4BYceXvXiXPJpW2DQSSLvsM7qlA5lYXWnob20t7-TOwKsnKifY6wN-On6AG-0srL9nYBTe1twFurYwRaznWxPOUfM0nvZaQW6GeiFNjyDkq6yDZSDQ1vwn04TA336nB5N0hC-2Axc68YcRPPsNhIrWK8b3Ct_YCIxAaHtM7cXOYFntNOOR9yU1fk_XmZthmXKk2B1qwn_uI3O_TivugcIGGiZCjyq7_1ah9EKV-ASBnHuRy9r_Riz4Bwq9ohsiKXvMIanQfF8ueJYpM-AAyM82VM3XygjFxdRbfVeQYmbjj8rgD6MtdKw94-_uI-200ad2eUYK_XaJDafnG5idvvll_nKIqODEhiw8e0SNH9-BgqOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی مجتبی پوربخش درباره جاویدنام سحرخدایاری ملقب به دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106582" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106581" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106581" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdFQ6_cUEez_Bo8YohefJRdM-w0BFBMY-mFK6dmtWy6TatHxntbr6R48VlM6IsK724DnUIx9AdgpzLIgFwbvjQiuzxw1vVlNSAvzMsPLfjgdLhEkBXXWF4ZwevUCX56gGgN2pdGqu5PPCbHnPU3JsxZj2e73WUevfF77U-b-mfBzfH2pA7MluoXtWGQLsRtOuwBRz0z-WxlAbmXDNOGIViDA1ubKw-VYLI4vJEVlNtBHwsB55Av0fGqmTdApTiy6zeNnacBJt6e5Nh8EHnQ7jiDUe5O5c8P5HzyZFWcHWU70IJxe3jpdveoHoWZsDJMTrTtKwSWLVAU6Nk9inyzLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106580" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0ea3f6da.mp4?token=kN_nZGYfUI9n4hwx0-Q8cws6MrTr3XjWpsvc4gL955fRyVNRwzgG10AVRK27mMWH26fXeKcOu7CxzfVT-2QG7aqcRgDNDfHkp2uwX6pVZf_ULwf5uWu-LHsuNjjCFgHUvN0LDq6xFQShvmlcr09Ss80bDJnl11hHCdEjmjmXLlIGBJypG9k0du6CR1bRvP3Bxe9x34CyK6uF82QCrZ8Zc3aRHyJyHnkvv8h5StlvQKMOYA60KAhM7hn2nPoP-GhGA2ATIy4a_oJgnLoe3Jpd6suS5a__ZJXsBA_Bwpq6vwhwqmEW5sK-IxOiRAA1QqOEyNundoZwbVw88kxa14EKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0ea3f6da.mp4?token=kN_nZGYfUI9n4hwx0-Q8cws6MrTr3XjWpsvc4gL955fRyVNRwzgG10AVRK27mMWH26fXeKcOu7CxzfVT-2QG7aqcRgDNDfHkp2uwX6pVZf_ULwf5uWu-LHsuNjjCFgHUvN0LDq6xFQShvmlcr09Ss80bDJnl11hHCdEjmjmXLlIGBJypG9k0du6CR1bRvP3Bxe9x34CyK6uF82QCrZ8Zc3aRHyJyHnkvv8h5StlvQKMOYA60KAhM7hn2nPoP-GhGA2ATIy4a_oJgnLoe3Jpd6suS5a__ZJXsBA_Bwpq6vwhwqmEW5sK-IxOiRAA1QqOEyNundoZwbVw88kxa14EKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت ریسینگ حریف بعدی بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106579" target="_blank">📅 18:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpZaZAZ6AWGlBONpQOaWxRW3DWE__XQxOYbbpWTli8EofWBdjNUhwGKysfJKuj9E2ziUF_IRA7L3p-K7qQBnWcG2P9LaMScY6V9J4AoeHrA4ilFc0ZKAFpPh4KNSEjYQXv3247KT17n8s__c7ouBfV3Zv-X9xSrivjNKJzBMSXE3UJ4X3kCa7jHMXQqjy03swYFcLNzgKcK__BXVPMi19CltPtVLdC67vc2G1HfZ4QOBmDppO4jF0F0zpSSVIVkOE_2yB-I_SqLD2_1c2taUm1jpApdUlSMZyKXPT2YrtxYjg4Ud-BWem70X7IoQi9CI0qxQfjaUJrlozmSzfKC1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWlrItFCctofaHe73qmMvb34P3FzzVuMLZSX2CqIWnfwAlO9AOjBY2Ejrdco24OSRXEM_hVtN8rzPPqyuqXO31b4810ZRL9Jgo8P-2wTDjkfHD80B69oMENhUemx_oJEwC_UNRVILc-yVhUQU8SBZcJMLkXO_hS_-fWq7a-gAPIwrfZbleyTwB3cexhq1ASlBZ-AA6KgqO2Euz7NFko7h5RTOoktiRIv9BPoMpvVNV46Sa24gifTvs5mAofGVtgunJuNf-aBrn-0S4h4kAT0M-0vqkNeHdWhwwXFu2EqQB_mGufg0XNK8vIve4WLsXCFoS3jKMI2bfcsACkk0mcwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCHtGBbfoz6JKaPfENzx83JqG8eqDo_ChuSiTNNOOk1i24q4QaKhVLuArjnaDZzgsn990tg_my8g6vNPDA0GR4kBrwTizEhu2TThUELaABtv9siSSgjE3nRUroB8wI1i7uB5EVmtQgziAtt4PVVLgRaaioemgPhAId4gNo36WAYxQ1MRIIKgfq_j_cZcs9BurWK1SQxyuUHMEHiZLRR3_kRRD93aqAlfifNz7wwOj9sph1XwGJ-IOwbm-FIXrzah5pDNz3qiGbe1WTAzppaWP3H7Z6BKXDRY8bI42MQC2J6euejCLFPj8fN0gxruQaZPzlFr2n462fWlbmJrNVgb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIdbnPl32HeIOtRYTA2eIzt283gmA2CYWXz1CGnL3cVc2NlGPA-dzqyDObkonSVpizhsBqLfnJ9qlOI-Xvq8a9FmrgdT-_xuJb30o1nSRDctr9ulOjBMvmDC02RrEXkO-jkaY78FtaAPyT7m4fs_RFchSxv6VVQAawVNI40s7hftol510DzcpzetJVkzUmLNVsrhzeHVhnv4WZ4qRh4GKRx6m5z3oEtVQMhVyodr7i9tBQu12a78xS_e84PINDZyF78mC55FlJWGfEgGmVgJnPS-9V2Js6qm6kxFegZjuWyHEK8ZLeuYan79MdAdJP1R8w0hNQ8FMfrpEI2DcjMWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xut5J1qeRY5GOWiXclolt6t9ueit-Aj2osA4I9M3QJ0k1a9O3hWmdXOjPuSH1UhDtl3p9Bhg1eKbVA9Ea0-TmeyVt_FcQQi9ZQIl7BJDfTFSw0rrATJnCyP7lN0Wmk7XKfbjUDvtqV-VR6z0WZ7inabpoGEHXv_6fozhckCSy8lJOwMl_7XP166_-15OOknurrrw9GGBCaGMgFTo-hKseUHnP-MjcgoRymKexgPAR6pYidwGx-t_jgBStRZvEsAvnvnE53p0KQ5d5H5_IeLJ_zA-igF_0K0rHEM3AHrgc-K_rYraHUqmh19EeoybpjsEedpw9M3dOAlNo2Sdyr7jCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsvpX_QEyMPDlLor4QJ4wabIPaaswl2pG-PNt2PUa6Y4_9teWf8A-OMJPYaln35WPgu-RhNwRy4Ns_QGx_ktVvOkJjiHdNvZh7mf4rWM1Q9Gs9gTudtmQmgNRXPhyHsilLMUF7eUwYm1dmYM7coGemhBLp1CSaz6V0q-ugB_LwRQtmUPtEi3Qqu-cLXH6yvrl02SzA9nuSej3I2QpYGXckwKpsOYYyCKcw1cTNBLDD15GDXH-82VL8w8phFUMyPFpL1QLrZRXVk4cOTGEgO7aEbAVFKTT00NOKbiFlfN31d2wUm1aYFs3dRzyfv50enQq7sDvgGggG22VkztfzTQcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
سیدنی‌سوئینی یه تبلیغ فوق‌کسشر گذاشته که داره چندین ورزش رو به صورت تقریبا برهنه تبلیغ میکنه. همین باعث شده از سوی عده‌زیادی از بانوان مورد حمله قرار بگیره و به نوعی به اعتقاد اونا باعث ترویج برهنگی و نشون دادن غیرواقعی ورزش کردن بانوان شده
حالا تصاویر سیدنی رو ببینید
😳
😳
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106573" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy5c6IL4y62QNJ8kOcerHoxb803lZEkOLYrHHsR4N8Cf-4yh0yUKdh-8FGUxmjvC5aSdnlJPOOnk3YpTz-S_6R9temo6Yxi50J25XcIcW99g1C6T9mkOl25q2KLCz6YFDZ4CQ-NAGrDIFcB4nvHuGXxhb_7KEen0f8jn0G9q8MdZOXEk9uf3yqis8q69OxAjz0WBdGcjI5VUFnKB3g4GVhZ0Alp0nHaQeX3BJtWp79kBWGHlxv4sAr0RZruiK47gsXGrvaGACtXI3cj2BuRXtEcYxGxL-TCex2uv8rBaoxko1hej9w-wkJC-YQCG3EAHzo-H8KtMnwXQds9JNwP7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
جلد امروز نشریه لکیپ‌فرانسه که بنظر باید برنده توپ‌طلا رو از بین همین ۵ نفر بدونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106572" target="_blank">📅 17:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4542b716f1.mp4?token=UEVHvGCtiB_1Y26D2NfQENcljZ3a1oIafpFTJ7bGKA_7ro-4fJLSYa5QZTeO_fXz5-jefqYLaiz8zbVzcwv-O7VUUWmcOmwUnzIdmhPlU9q0pd9ebOWLJZ2AN_sk7BUbqX7fDJ3eAO260zHdL_2e68pGPVQpMNvJ2z8AM08TvtSiuMWqga6Vx5MylFsW1YSYgx4l3NjB3cS4Ax_ZooNqCrnxJIWzfzBbj3YjDhSeD0jU6YNpdXtvudcNYfn5LFcZdYyIRkbrEXwRghQCzX5t5pNs1BhXbBWYr5eJq4Un34KB1nGkYPqwUKIwDW886panFLxWSRRj6_F0UPJsJAkxiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4542b716f1.mp4?token=UEVHvGCtiB_1Y26D2NfQENcljZ3a1oIafpFTJ7bGKA_7ro-4fJLSYa5QZTeO_fXz5-jefqYLaiz8zbVzcwv-O7VUUWmcOmwUnzIdmhPlU9q0pd9ebOWLJZ2AN_sk7BUbqX7fDJ3eAO260zHdL_2e68pGPVQpMNvJ2z8AM08TvtSiuMWqga6Vx5MylFsW1YSYgx4l3NjB3cS4Ax_ZooNqCrnxJIWzfzBbj3YjDhSeD0jU6YNpdXtvudcNYfn5LFcZdYyIRkbrEXwRghQCzX5t5pNs1BhXbBWYr5eJq4Un34KB1nGkYPqwUKIwDW886panFLxWSRRj6_F0UPJsJAkxiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
چطوری سرشونه های گرد و پهن بسازیم؟
به توصیه های استاد هانی رامبد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106571" target="_blank">📅 16:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106570">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO36-mx-xZuoWoIcsr3Xf-1FqKztIm-hoCS-6QZFVWTNSJKXOYHNjzi7xFSZoiJ34-tg1RT6hyukuin-kCZQwU7uD5dEW5zV6asFesupTk-2wZkc0zz6zPaFNp49KkFhFXsx6Z0zlvkXuPc2icYfujKM6NRsbFpes0AsFEkhraNhM8cUuGWMsvg_tEZeeyFhNTTyx0RhKbKJXUb1liridO4QeqqbwIUcwfzZOljwBCz95Q-4HFe6CAgGDrXkZmqtlacN7GBKhOwSSt68R_f7fNs6-fxnUBSVFb4ikJYrZtVuuu0CrNxcheFc4CawPwjAUgsKbBgYlmTisVWLtblZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عملکرد فوق‌العاده‌ پشم‌ریزون هری‌کین در بایرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106570" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106569">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aef2c9a7f.mp4?token=QisQBO1tAkB8PfeMP2_gK0xAgRs00_o4YF9oSp9G874gd-1UtdnTqYsHNOJyJaqhGQ0w5GJh2FTh_ELWHbJ2N-IGiEsWxRgHkmX_burQY3Y-uVipiWtmIbabDsBP_6fz7LzJuwRpGEf64k9uhxV4GU5M3CkueqGbe81H37BUUB-kHFsDjdvD0WhNsrQ1TMZPWp5YLPxE1xFTqnOHyTyw_3QlWWV_uTPJ3zTSP1ixi3kj1ZintTbvlStQSNk01-Wa0M4_-9Vb_yEfKVuHqflMCULhuPWwZurQLvpLTCuzcTlZH6MA7rbLRmFlk2phL5DzVuCP1oaVT9gyds2mkvOfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aef2c9a7f.mp4?token=QisQBO1tAkB8PfeMP2_gK0xAgRs00_o4YF9oSp9G874gd-1UtdnTqYsHNOJyJaqhGQ0w5GJh2FTh_ELWHbJ2N-IGiEsWxRgHkmX_burQY3Y-uVipiWtmIbabDsBP_6fz7LzJuwRpGEf64k9uhxV4GU5M3CkueqGbe81H37BUUB-kHFsDjdvD0WhNsrQ1TMZPWp5YLPxE1xFTqnOHyTyw_3QlWWV_uTPJ3zTSP1ixi3kj1ZintTbvlStQSNk01-Wa0M4_-9Vb_yEfKVuHqflMCULhuPWwZurQLvpLTCuzcTlZH6MA7rbLRmFlk2phL5DzVuCP1oaVT9gyds2mkvOfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
فاطمه‌مهاجرانی سخنگوی دولت در پاسخ به سوال یک‌خبرنگار درباره چرایی تبریک‌نگفتن برد دیشب استقلال: ما فقط بابت بازی‌های تیم‌ملی تبریک میگیم و توجهی به سایر مسابقات نداریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106569" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106568">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=LioFSCRauiysqYvcyTyVd5raOH0CZySXM0VALhRFZEbIUL1Hq4k9U1B_aRa5dEJzPg_5UswCazcw1r8MCTSOKsjM9UEBvunkOTIwR4HZ5OwGp8JndHebnYmI3FcqeNCJ78ogiwFpbGy_HSKqK-eyrMtE_njZqO7KsssE7hVy-I1n0qiew24PoW32L9AM0wUjZ6YFmjz5Heh_CDrfOuYiE09QT8vpymKmbshM45gCBfPSO9tDRuK4dPVUBIcXhiIX7YzBdGc1E5sF5SPYPZWva3JBlKUDttj0aYaJxzTbGYdr1F155kFvAz5Cmp1vC1chYH3lxK4ukNbx7YP8qJOQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=LioFSCRauiysqYvcyTyVd5raOH0CZySXM0VALhRFZEbIUL1Hq4k9U1B_aRa5dEJzPg_5UswCazcw1r8MCTSOKsjM9UEBvunkOTIwR4HZ5OwGp8JndHebnYmI3FcqeNCJ78ogiwFpbGy_HSKqK-eyrMtE_njZqO7KsssE7hVy-I1n0qiew24PoW32L9AM0wUjZ6YFmjz5Heh_CDrfOuYiE09QT8vpymKmbshM45gCBfPSO9tDRuK4dPVUBIcXhiIX7YzBdGc1E5sF5SPYPZWva3JBlKUDttj0aYaJxzTbGYdr1F155kFvAz5Cmp1vC1chYH3lxK4ukNbx7YP8qJOQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حمله تند مصطفی هاشمی‌طبا رئیس اسبق فدراسیون فوتبال به علیرضا فغانی عزیز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106568" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106567">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کل کل خبرنگاران استقلالی و پرسپولیسی در نشست خبری امروز سخنگوی دولت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106567" target="_blank">📅 14:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106566">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdGcMHYoGfPNCB8R_36ShF94sg7zivmrT4pL0iLj6SCRAakqMHeCgg98CRr6C1ovdL-IBLwShNgg9r214_ZR1Azs9Vz6en-NchGSE2i7SA-cgd-6OP1E_Rng1jK4bcn2AduPQHtVORISGPe2_k7ss9Um0ToGrdgt7LpEBY0GS9IbxN4Yn0t8UQaOGz8JqxzV0RM_tmL1Qkmh77VJk0wDscXN9zb0AqUUmANJPkAAp8S7wVzUDw7klntvlDU32fTtQWMypG0ZjCuVkEF0uogvPy4UsP3VYZaSeIVfJMzUzSnhEtMkYtjbZR5xilS_5OoMbVr6L3EThflK7hyQDGDq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
هانسی‌فلیک: مطمئن‌باشید تا سه سال دیگر حتما حداقل یک‌بار قهرمان اروپا خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106566" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106565">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaKmMNiMmNJDQg-lzBjUnwz5H03k2SId5LPegueRHpXM5tacc0qbvL0xier2x81sqNrOwuc9bK0-7JBfYTQK4OABq_indNK9rgqQkr9vWzFLVGNY_SSTS7XHo7re5bzGgnqgX-9jYpQg8RQWQMvUwwzz0heiDWnMszwOvgTOXVKgCbNaIA26XV3yno_DRmzd-m4jq-XGkuasFbHUIi-pQO_PpUkBjQjyIiEomqqCo9gjCeyjqPcfxrXXkuHr7xo9RlBQubM9DzhJHV5PZVIjs6od91ADeD886OlciPuFesRoajubxIEv1EqMowR6blM0D8kWBqqXUz7jG9dsOX--yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106565" target="_blank">📅 14:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106564">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py4SojlfAfQfV-Mc5R2AppQIiYDC_cdv8YnnLsjOiVb3I9h60WO3tCuMz9O7A4hqS2Jfqg8awD9AcGw0zNGHsyYPDoRIlxBlVxgjR_jACGgF-qDCjpuzeRRUCjaSMR4oCfQ9O3C7J6EPYtB-QSZ-c7iEP6NwXqvT68AB0Ldq9s0qzu4xf6D3UzcuQpq5ThcVXaeETK7hasNpsagpcp0hsw41fIBKICPy1PkQEwwJYxWTHHCdBYP_8v4uKeluFD6l_ns2szYi6lgyRlx4u80TU9i2tPqi8OiLvDS6OBXB7awHiVbd82yNeoAhx7QxH_bJRqTp-Mi8SYnRR6f02P6rKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106564" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106563">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=oguduUb27TBSaK7t5-ljZFn2FnG4fBjmS9bv8Gi8q2OSGy0KBhXKeIzAGVBqrtmi01otlTlYZRNjEnx4mpxRptnx3cB9NqqS5VPSE8ORvQrGEPRlodPabLL0x3rBpPHRoyUkIfK1IoK1mZW1Uq3w_Ar21V-_bHRFMLd6_MUEAaCmfNhK_TcPIFp-zueqCCyDtQYTUdJvVaeKZhM5K47zBX7zyxf-fF8dZwizJUIrRwzW1cTbxKMC1bF61_YiRlBKcVRqSL15-4R8yfHxztgQ3pgh7maGVC5MiGuMfXsycVRYDTFHWsDFv57f5idHjSTxo55FtrbJHlhItdVdI9RHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=oguduUb27TBSaK7t5-ljZFn2FnG4fBjmS9bv8Gi8q2OSGy0KBhXKeIzAGVBqrtmi01otlTlYZRNjEnx4mpxRptnx3cB9NqqS5VPSE8ORvQrGEPRlodPabLL0x3rBpPHRoyUkIfK1IoK1mZW1Uq3w_Ar21V-_bHRFMLd6_MUEAaCmfNhK_TcPIFp-zueqCCyDtQYTUdJvVaeKZhM5K47zBX7zyxf-fF8dZwizJUIrRwzW1cTbxKMC1bF61_YiRlBKcVRqSL15-4R8yfHxztgQ3pgh7maGVC5MiGuMfXsycVRYDTFHWsDFv57f5idHjSTxo55FtrbJHlhItdVdI9RHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حمله تند و‌ عجیب یک آخوند در صداوسیما به صحبت‌های لاله‌مرزبان در حمایت از مردم مظلوم ایران در جشنواره ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106563" target="_blank">📅 14:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106562">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589bf63655.mp4?token=bf96zCcLWUT-r3tsWz5eEGqZTSKFcoGHlQfOztJC1HnBUmfQcjQq69tKbTAOaIv5xX1RnhPAEJjfFtJWynQYkPOHdtwLOqQCVzuVgmjnjvzFM9NUO3AHANrqqwMcwi1e91KdBsNJawY4jtm1VScXjiKHWwr03Qair3ixllqY4t-Jl-pk4u_Y71atOx6zayPlG1Ps_1PDHqz1wQbXkwoYSEcllQ6iEGX4zIOgIcnxsgR3g00mPv_F6acJkEu5ho4KOT0Y1m_uWaohrW3UQ6AGbocxhM8BZyZGOjYb7aMiUVXFy3Xhn2lojrD79H3u5AQF8GP9PL5qzeYqzr1vxaudPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589bf63655.mp4?token=bf96zCcLWUT-r3tsWz5eEGqZTSKFcoGHlQfOztJC1HnBUmfQcjQq69tKbTAOaIv5xX1RnhPAEJjfFtJWynQYkPOHdtwLOqQCVzuVgmjnjvzFM9NUO3AHANrqqwMcwi1e91KdBsNJawY4jtm1VScXjiKHWwr03Qair3ixllqY4t-Jl-pk4u_Y71atOx6zayPlG1Ps_1PDHqz1wQbXkwoYSEcllQ6iEGX4zIOgIcnxsgR3g00mPv_F6acJkEu5ho4KOT0Y1m_uWaohrW3UQ6AGbocxhM8BZyZGOjYb7aMiUVXFy3Xhn2lojrD79H3u5AQF8GP9PL5qzeYqzr1vxaudPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🎙
رضا شاهرودی بازیکن سابق پرسپولیس: نعیمه نظام‌دوست گفت هروقت احمدرضا اومد پیشت، بهم زنگ بزنید تا بیام چون خیلی دوسش دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106562" target="_blank">📅 13:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106561">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a994c05864.mp4?token=VEfIWbwSq7iiwgdfxA1vG1ZvkXGu6LYEt6_Q7Uqfh_JNYRGWlDFLlz1ok_Ylqt8VNxnHRr70-qOpU5X7b_YXsSM9HVwYUEXanEblL-f_TIZq8icOLZ8E923yzI_vBU0E5v2Evw2ShgvGBqZpdQueQFESNVSx8eyEkMcRbfn3WVS9foEIuqy5LsbvylfyvHPLepdivyStwroBV9IoYU6xOB4BLErK6STnWr5MUrB58zSta0CSU2o-jkbGaT-kjBefwAmPKmpFDsaUpYhnMd6N-5JpiEW1_ZkJbBr15a8e1jGuTHww-vgszKuYrI4aRzzrh4B82fDdolRvwc8yJsV7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a994c05864.mp4?token=VEfIWbwSq7iiwgdfxA1vG1ZvkXGu6LYEt6_Q7Uqfh_JNYRGWlDFLlz1ok_Ylqt8VNxnHRr70-qOpU5X7b_YXsSM9HVwYUEXanEblL-f_TIZq8icOLZ8E923yzI_vBU0E5v2Evw2ShgvGBqZpdQueQFESNVSx8eyEkMcRbfn3WVS9foEIuqy5LsbvylfyvHPLepdivyStwroBV9IoYU6xOB4BLErK6STnWr5MUrB58zSta0CSU2o-jkbGaT-kjBefwAmPKmpFDsaUpYhnMd6N-5JpiEW1_ZkJbBr15a8e1jGuTHww-vgszKuYrI4aRzzrh4B82fDdolRvwc8yJsV7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇶🇦
توصیه جالب صالح حردانی به نیمکت استقلال بعد از درگیری با بازیکنان السد برای سنگین کردن جو علیه حریف قطری: همه بریزید داخل زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106561" target="_blank">📅 13:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe5inIDUH4ofwJSMZzGbTqsT2DFZjJZSgWQILLPkbY7FKyN0fTRuZ6xyrCxkJgddhYp73d-ZPItul2xqtTdgAw6dsJHiQ1vkrsR16dlxvWPxf25gD23ddxoiIFdAowSBl6NyFzTQOkJX66r0TYQsDSkIDLGy23uPFSNGmYbs5maHdXLz5IxLbQpSe293zf2niADrBgqUItrUvbyxeEDWlzq8dAiwKYgrBscoSAHjluBa-lBYXnlRbtWaYrSfPMyJRvAc_ECUOCjT7VAw-t4adVDWkMgurXAuKOv8qYGYcwa2pEPXmScmHF61souTrPTBUeSaTmEmOcnrUWNWDZL_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
آنتونی گوردون:
من با این باور اومدم بارسلونا که می‌تونیم تمام بازی‌ها رو ببریم، ولی خودمم فکر نمی‌کردم قرار باشه همه بازی‌ها رو با ۵ گل ببریم. ​الان واقعاً هیچ‌کس نمی‌تونه جلوی گل زدن ما رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106560" target="_blank">📅 12:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKK9rM40etGjIc6rEzheY5gFFn4wOZodRalIM_bxgJ1KUdqphetTWMuwjr_9Sgt1phXb5fbiKBs_XCptuYctjgMzB3wRJOmjKjrVUhXYm5HPVJbnIFUUeoqHIN194x7CFvsiMeRUxDYE7DLKzuTAlEY0xrpi8nHcvTVcbGdMFt-xPOTDMaVbijPgrHCDzkwnpR3j6FA_7bTmOTXbPs88ssMjGD-u6ECx9qTki7Zyc2HJvl79efguzjbz5rPDJn8VDaExoDBpvHvgvr2XVJgFYRzF0HGq-9NOiF8SGiQ0X03SLNKvysN4ds3drlH-CNShIlAZ5eErBTuSqyFr3k37UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برنامه‌مرحله گروهی گل‌گهر در لیگ‌قهرمانان آسیا ۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106559" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106558">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106558" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhC-_JCzCX7lQT8wKDxEE7i4uf1zxTXcBk51vUCNRxTh-6fq6FmReV5FihbaXTLBepauR2JfTQj1JGZl4joyGMOjlHh-AB2S8X8vx4N-ZXKJPgHYHrhQ91gXr57K0d54TEVsoAK6POmX8QdAxGtzJLSl_1yTtydKi9hYZtSgwSqM7um1n1kn7VEYPdIu1UepL3PqI4tFINYOUKYACZSx3T-bdKvcMXfd89Dgve3T-UilZifemZ7WqedMDd29RB0WaR6Wi7CACA96OC40Adm3-JES5aAmHbMOCCa5RTiPPJQeoYHjuBJodSUMzWJc4N6T14Nca8agIbfBLJ76bpQWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106557" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106556">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851e159f48.mp4?token=S5t00ue30oOqbbG4FqA9enQALW40OQoOiLZNrEY_ToQhF-aqpaiQ-qTtbiIYusxFaA3pButrQnqh7oU32_ZHToz1kGlbYghLyKyn2lzcP0Zv3cSHXcdABb9Jry5pKwh-0zrHGEiu8J0sfBb45EOnxVzLwW4BDQsJerU49cSvVgGCOJOxYyZ-jk-5HHV0zkrYWcLf39J6Sm4FzYrI3qvPmeEeZHGJMTIlSdZu8XXpl75WqINs5vFPz-sDbpT75fS5rymUUepMntW-HdPmJAWVVnoQLkkiWHhw-Pw3aJA8IDoovM6ki3EcTytH3sJ-qRfRsoqBe2QRU9VoJ0n8E3-yRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851e159f48.mp4?token=S5t00ue30oOqbbG4FqA9enQALW40OQoOiLZNrEY_ToQhF-aqpaiQ-qTtbiIYusxFaA3pButrQnqh7oU32_ZHToz1kGlbYghLyKyn2lzcP0Zv3cSHXcdABb9Jry5pKwh-0zrHGEiu8J0sfBb45EOnxVzLwW4BDQsJerU49cSvVgGCOJOxYyZ-jk-5HHV0zkrYWcLf39J6Sm4FzYrI3qvPmeEeZHGJMTIlSdZu8XXpl75WqINs5vFPz-sDbpT75fS5rymUUepMntW-HdPmJAWVVnoQLkkiWHhw-Pw3aJA8IDoovM6ki3EcTytH3sJ-qRfRsoqBe2QRU9VoJ0n8E3-yRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حواشی فوق‌العاده زشت لیگ‌نوجوانان گیلان و کتک‌زدن داور مسابقه مقابل چشم دخترش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106556" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
‼️
🇮🇷
ادعای رسانه‌های عراقی: استانداری بصره تمامی هزینه‌های مربوط به میزبانی استقلال در بازی دیشب مقابل السد را پرداخت کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106555" target="_blank">📅 12:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106554">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1348b5a435.mp4?token=kDQz0b1jVZ4a85pVT4HguQmhdH_M1E9MGByp-h68iO4Uz2GL5KEnvmxAuCcftE6-SgkZVsrNNTeaLJOff8BsQj4LeSDeUqesmdM0Yc11_9kNMC1jIVPlFxrutWnP1cfx_pf1epf6ohQtGl89MKolC5dOArQNDphY80pz6rS2rr_TaaHetitJWPvI1VrP9rMEZFp6CeEbemQXgB9JLUSlV56Anra89C50KggyVGuytd_yreS_OfbLC-rhlvIVG_yEER4hgwyA2n3RY3l-Zt9AjEH81gsFpsL0QdE9VqFLyGMN8SmD8zQiZsnPXqrK3ThKLVanx2meij9M-T-odHa-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1348b5a435.mp4?token=kDQz0b1jVZ4a85pVT4HguQmhdH_M1E9MGByp-h68iO4Uz2GL5KEnvmxAuCcftE6-SgkZVsrNNTeaLJOff8BsQj4LeSDeUqesmdM0Yc11_9kNMC1jIVPlFxrutWnP1cfx_pf1epf6ohQtGl89MKolC5dOArQNDphY80pz6rS2rr_TaaHetitJWPvI1VrP9rMEZFp6CeEbemQXgB9JLUSlV56Anra89C50KggyVGuytd_yreS_OfbLC-rhlvIVG_yEER4hgwyA2n3RY3l-Zt9AjEH81gsFpsL0QdE9VqFLyGMN8SmD8zQiZsnPXqrK3ThKLVanx2meij9M-T-odHa-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیرقلعه‌نویی سرمربی فداکار تیم‌ملی تا پایان جام ملت‌های آسیا ماهانه ۱۵ میلیارد دستمزد می‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106554" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106553">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDT5X4KDn3GYFTFquZFPGzWVC7voiastGlgjrLHtj-r_vbeRDfVttrVg2NII5EI_QT3ry-98jAndPISqPCoZXU7BS0e58XtXdjZzYpgoMkaLEaEl4iYZeSMmO8IGQPm-BnnlTdbBDrgorq3yfnxSbZw9fr8x-w-xjz3rEGP2AhDV8EGxiDfCjDAnWAtPbFkih2o_wV77sxik0eoe4KgKp59Dp-_PTf9l2bHPHcv-FrA_jhqehNvcvWt6lca-dCiXyBOOQqzS7tFVBccGODYmMqGlWWsu6WkLgxhgSHse8ZFNjck6Um-UvinZW2S5ePucfECL64xpZmk9dS_REm7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
‼️
مقایسه آمار چهار مدعی اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106553" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106552">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d711d850a.mp4?token=KZPAjU39U5lrW1HqTsrNOS-93UHx57myrKSlh3MGD4OI3gNuS6XacEv7Jfoam-7J4-aHhr4XLrDSqDlOxaWy9XeaDo9uRk3CrMNQl-BZsXjYvag49vUgh2URIUhNVjG87T-U59WjAQ2lAqAlYxrJUDvmO14GtcooFdE3feQKg_JN3jdrgQ9ufQims19MZtjlsTXvGlYO6wr1GSE0ojqn_mHKo-N293WFG0NiZ5WcISZWA4kvhpVfNktOe4PtG5yaQo3r0N6XC1Lfso3u3mzMrzQSSSuRrdzJ0m-XzP_VzqP_EP-59Ena-tsHs32BQFWmP3CZiHyCWbcWHFErCd6I8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d711d850a.mp4?token=KZPAjU39U5lrW1HqTsrNOS-93UHx57myrKSlh3MGD4OI3gNuS6XacEv7Jfoam-7J4-aHhr4XLrDSqDlOxaWy9XeaDo9uRk3CrMNQl-BZsXjYvag49vUgh2URIUhNVjG87T-U59WjAQ2lAqAlYxrJUDvmO14GtcooFdE3feQKg_JN3jdrgQ9ufQims19MZtjlsTXvGlYO6wr1GSE0ojqn_mHKo-N293WFG0NiZ5WcISZWA4kvhpVfNktOe4PtG5yaQo3r0N6XC1Lfso3u3mzMrzQSSSuRrdzJ0m-XzP_VzqP_EP-59Ena-tsHs32BQFWmP3CZiHyCWbcWHFErCd6I8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سکانس جنجالی مرد سه‌هزارچهره در کنایه به فساد بی اندازه مسئولین مملکت جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106552" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106551">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46287e0aa8.mp4?token=mI99oupxXG3ZdNKVOY_PtlDrNsZo3C9czROnMAG-aPHRmTlMCVzzpQD3UdHwUIh1QyfRnSOn6g5tg5qpSfBPZLywWJWeX6IesdyRHaARjmcWQvqxlmrnP6nhVQcKMclG1ctrDz78kTlFQHehDINJlfuqloQMhtF5OsNcS4MYyKK7DF0qKWQp4K-s8vnGfIjcyvP5NzgrQyy_9ZRxXrTgsDvUYCOg5g8Gxqp8Qd2uaXk-aXfhOKStEPYHc4EB4xRlgMAXinccPF6-iZT8xNeZeThw0dcTafoINvfxjwmmN3nezeOOBO0QuuULExSsLMivJsV5FTAO9rEAGijZktLK1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46287e0aa8.mp4?token=mI99oupxXG3ZdNKVOY_PtlDrNsZo3C9czROnMAG-aPHRmTlMCVzzpQD3UdHwUIh1QyfRnSOn6g5tg5qpSfBPZLywWJWeX6IesdyRHaARjmcWQvqxlmrnP6nhVQcKMclG1ctrDz78kTlFQHehDINJlfuqloQMhtF5OsNcS4MYyKK7DF0qKWQp4K-s8vnGfIjcyvP5NzgrQyy_9ZRxXrTgsDvUYCOg5g8Gxqp8Qd2uaXk-aXfhOKStEPYHc4EB4xRlgMAXinccPF6-iZT8xNeZeThw0dcTafoINvfxjwmmN3nezeOOBO0QuuULExSsLMivJsV5FTAO9rEAGijZktLK1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تعریف و تمجید میثاقی از امیرمحمد رزاقی‌نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106551" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106550">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c06af095.mp4?token=GUtGImjkVVpBXf7PdOYW3fn-5YUFXjNPuXFGwlNVrUgyfabh1926YTR0dF5U8xio1SDCyiGuBYruz2e0yxs-RMbs_WvVrPl6uM6902q_UKJFDdlKnXoy7Ipsxi6pnrcCs7ImKQDa-bf40OLcochXR6MeUUjBB5drkPwXeuGeyKufJqqFvmO1djwmtt-XnrOPTYtTsNTyUoKWP6itn72HvHSClFwQgYtPonPR8SEuDMF-sS_vO0EteD5KzCDSButMOZ6QlHItfZg3RUxOsf-oEMSHG2OdvDRtpNCsb9c2LnS7Q4Xp0zjFo4iiU-d_BSURyq_qy8C778aMxdWn_CFIYWqCk86T1neKkYZ0--bBYiUedEJiDhmOHQHmWd5xVL2m3xTdMkhQ1vswkvILN3Pzlwj1k3IU0xaUmOlsWhV29Lll-hBLKqNRjl8oTYQPFLxDospK9Ta6uVD_H4_zQ6dmaG5ZnNu34Cyu1-IGmydzOnaywn5bLIrt1DEenF2_m1mr7g9Bp6Uoof-bznYKzOGeDvB0pgQ_jOuxQypLkYbk_rksMw-fI3-zKit0R10mbGr2Jc_bb42gYPTfgTLO8SzWH5Ci-l0GiYbGmv6auVFrLS1O2hLy4CaZrrjLha_enjlriKl8cygFSCTawoq2TWDmm5Z1uV64uBGeIIqJ7urpbt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c06af095.mp4?token=GUtGImjkVVpBXf7PdOYW3fn-5YUFXjNPuXFGwlNVrUgyfabh1926YTR0dF5U8xio1SDCyiGuBYruz2e0yxs-RMbs_WvVrPl6uM6902q_UKJFDdlKnXoy7Ipsxi6pnrcCs7ImKQDa-bf40OLcochXR6MeUUjBB5drkPwXeuGeyKufJqqFvmO1djwmtt-XnrOPTYtTsNTyUoKWP6itn72HvHSClFwQgYtPonPR8SEuDMF-sS_vO0EteD5KzCDSButMOZ6QlHItfZg3RUxOsf-oEMSHG2OdvDRtpNCsb9c2LnS7Q4Xp0zjFo4iiU-d_BSURyq_qy8C778aMxdWn_CFIYWqCk86T1neKkYZ0--bBYiUedEJiDhmOHQHmWd5xVL2m3xTdMkhQ1vswkvILN3Pzlwj1k3IU0xaUmOlsWhV29Lll-hBLKqNRjl8oTYQPFLxDospK9Ta6uVD_H4_zQ6dmaG5ZnNu34Cyu1-IGmydzOnaywn5bLIrt1DEenF2_m1mr7g9Bp6Uoof-bznYKzOGeDvB0pgQ_jOuxQypLkYbk_rksMw-fI3-zKit0R10mbGr2Jc_bb42gYPTfgTLO8SzWH5Ci-l0GiYbGmv6auVFrLS1O2hLy4CaZrrjLha_enjlriKl8cygFSCTawoq2TWDmm5Z1uV64uBGeIIqJ7urpbt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وضعیت سربازی بیرو: واکسن اعزام به خدمت را زده اما درخواست تعویق پزشکی یک‌ماهه داده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106550" target="_blank">📅 10:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106549">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9668387e.mp4?token=iK16T_7ngfuQbrVZNQ8S4msrpjqAXyYCBqchxjFzy7GV8nGSRH0oMOE9SH1TYhtzDsc00Ku7di7v6UOllpleb_Tu5rUDzYMK-4EtPiLf4SkcA_I1hTzfI2xV3QBiblQJYpyOnma8k6rSyylAoWI9fOcNNzR8z1nKDaioINeWq2ItLtXvll14Ze2kg1cfB-mEKXwjLtGt4wLdwx2MyP7gHI4YqJD_MVGKERN6SmEDDFOaFSVsyCjME_yqhJzVRFUir_-4syuqE2HXJGLX0hcQoCJKbv1EBd2iV_v8wgd_7Xg_Mji0OS7i08wRwCImRsjszNYx-65Bu7DukjkKRM5-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9668387e.mp4?token=iK16T_7ngfuQbrVZNQ8S4msrpjqAXyYCBqchxjFzy7GV8nGSRH0oMOE9SH1TYhtzDsc00Ku7di7v6UOllpleb_Tu5rUDzYMK-4EtPiLf4SkcA_I1hTzfI2xV3QBiblQJYpyOnma8k6rSyylAoWI9fOcNNzR8z1nKDaioINeWq2ItLtXvll14Ze2kg1cfB-mEKXwjLtGt4wLdwx2MyP7gHI4YqJD_MVGKERN6SmEDDFOaFSVsyCjME_yqhJzVRFUir_-4syuqE2HXJGLX0hcQoCJKbv1EBd2iV_v8wgd_7Xg_Mji0OS7i08wRwCImRsjszNYx-65Bu7DukjkKRM5-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
آیسان‌اسلامی: هانی‌رامبد بخاطر مسائل ایدئولوژیکی از هادی‌چوپان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106549" target="_blank">📅 09:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqHkKhZtSndrU-aiU8SSow2esqinr0OOI1o-KcAshnl-vOeZeu3jOZDizP70qZhb8Uo6qVSN5m1jbLDELVPpN9F8_JB0vTLKuZiSbYOJ3auGHAd6okuM0iu6Hz7BBmsSzuyL8YEo932dBUprjs1PQBz0EoQrTNNb1CIggL8BNfQSGW-N_5TjghgSxi3l38WPvUXhgoKxNJF4TALseasqECbPrpmHQX2EKb_CuZE0DkXQkcq9Gk1BTxuXQqNrHnPe5e5x12y6DFY9F5twZFxR6xBqGMO60iTXjPeLD9Pw1UvS_weu2J_4ZNsQkfSr8HXV-qGDtjn85i4DfP08EiRD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🟣
عملکرد فوق‌العاده یاسر‌آسانی در تاریخ مسابقات لیگ‌نخبگان آسیا که تنها ۳ گل تا بهترین گلزن تاریخ آسیا فاصله داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106548" target="_blank">📅 09:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106547">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKedEFxFYCUjgHIHY92eBSOWGBnqwNiHJJoqWuG0TR3HVdULfwt1JuH2JOF3sFhVWKs1bV7Dk70t9KJgUd8KeNIlqlNXxK9UPpHpie4ytgRI434JTLHcd1nGIzfemiiDSwjAoQgY9zNOsL8z64pQlO9rpDLX-xy48y06r3soR97WDcqoqUMM0kPtkT8wJPbsoJwV6oeWK6Q5Orwok9gN6Xp7aCyW8A_pQRVbWw6uZ72nkz8b0fhwLxDCs_8hP78ZKLFQ1hw4NwvJ4sCG8NfqVjfVpXtb9JFaRWPYGH990b1Mplt6KKnGK42wnUYBTXGiX6N2k-tRQdRyMmykP_aACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
‼️
مارکا|باشگاه‌بارسلونا قصد داره یک‌کمپین تبلیغاتی فوق‌العاده سنگین در حمایت از لامین‌یامال برای کسب عنوان توپ‌طلا آغاز کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106547" target="_blank">📅 09:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106546">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6843e64d1e.mp4?token=p1M7NRLLCyXub0bJpiEnDtU9kNKN5MHYhc-MAy6t79ov6HHNbR-31JZcx1qsRvjNYIp5dj5xXtJOLlkYvUWI3NpGtQRCGHPvARLsZeb2v6KGYbiWHACBOn-X0QUvfUJDvqmCn3Z7iGqeiuk7cdXO-Yr8YAzp01QNHnz3IFcz9kl-rnRNWscLeb5n8o1hf4k2x3zfcEHriqb5JohYmDl3tPlE3Djjo7L7YSj7hrGS2uokKzKMDtInSkhe_YrGNIbenTjTevCh7kXJWditlWMuJt0pgy9cqCP5-ZLmTjACelnefAtGYzJtN6JkU32JO0MitU33vhuKYvlKRBOP-quiOSuXmqN5EpX1-tha0XFS92NZQiBmNeH2nBSyqN3P7mLIG6tc6r8B-e63raMhYkuAbsOPULB_s0bDr9BoTDz5nozPQImd89ZqScFascIJB7QXBynLwUqD8jnI1ZmCK5TMCp4wggzeNRYQXXyioy0rDhRMQvT3iTE3AGEMPVOnPWEYbBL_zjkM5o1TL-FmiZrroqOrhdRVOHF4CR0RYNdjLIywwlxu6f4nSwURz1u4922kulcxDoRGCrtibAXM_wrXrFXsci5hb99Qv_kD_1G3zIWzSmNSxOCsntNCLMN4bEBoQfsM0mubPaL9ypluEMUwsu84lCQKMH7HofgiiXR6S4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6843e64d1e.mp4?token=p1M7NRLLCyXub0bJpiEnDtU9kNKN5MHYhc-MAy6t79ov6HHNbR-31JZcx1qsRvjNYIp5dj5xXtJOLlkYvUWI3NpGtQRCGHPvARLsZeb2v6KGYbiWHACBOn-X0QUvfUJDvqmCn3Z7iGqeiuk7cdXO-Yr8YAzp01QNHnz3IFcz9kl-rnRNWscLeb5n8o1hf4k2x3zfcEHriqb5JohYmDl3tPlE3Djjo7L7YSj7hrGS2uokKzKMDtInSkhe_YrGNIbenTjTevCh7kXJWditlWMuJt0pgy9cqCP5-ZLmTjACelnefAtGYzJtN6JkU32JO0MitU33vhuKYvlKRBOP-quiOSuXmqN5EpX1-tha0XFS92NZQiBmNeH2nBSyqN3P7mLIG6tc6r8B-e63raMhYkuAbsOPULB_s0bDr9BoTDz5nozPQImd89ZqScFascIJB7QXBynLwUqD8jnI1ZmCK5TMCp4wggzeNRYQXXyioy0rDhRMQvT3iTE3AGEMPVOnPWEYbBL_zjkM5o1TL-FmiZrroqOrhdRVOHF4CR0RYNdjLIywwlxu6f4nSwURz1u4922kulcxDoRGCrtibAXM_wrXrFXsci5hb99Qv_kD_1G3zIWzSmNSxOCsntNCLMN4bEBoQfsM0mubPaL9ypluEMUwsu84lCQKMH7HofgiiXR6S4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
بانوی استقلالی ساعاتی پیش: به فرودگاه آمدم تا جلوی آقا سهراب زانو بزنم و پای او را ببوسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/106546" target="_blank">📅 08:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106545">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCyZcuPDXk4t3MU7_Vxw9CLKOe-VCArUQ_VohvWvp78g3KZ0xLlOXnbtVpCz9NysCG7-j-dS5Db6j5hl9ALB69TkOWXgn1MBOAa5cTtBkOxGcyR3z_r0Jkdcfdx68sbiD3y7CI6vIGRbsBy3ypc8V9odVdt8SYBsGmpSEtb65IL_ponvEFSutBxVNy3Pe4_RA9bmtrDNUN5zBs4dhU6EeVclsS9VaWELatqpIMvUAztO6sZM0MEvlut3TKMd02KsmOCKgcz0HoHc9eZfP5W1nfKTA0vAT30DR_-Ol1TG2SxD27BdhrXomygr4RD1OTC-VJIvc9i_j8ZOw55CYeTsew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/106545" target="_blank">📅 08:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj5Ado0XtlbvM9E_TfghiECvT6tA8bTGU5M3QUk7j9tdT1fvWvXyeYKeE9lLCFhrMB5t4Kh_d9yxGdybvoecyuioZqwxk9v71RqwgIUqP2rRURWFfNE9Nb35LhsqjRQn3ZrLlwil3Rw9-5828f7JyHIPdoWHnH8cjtDaG4CRbLZVC6zIXLbbjzbD2Nf1VWZ5ID4ZqTMDBRXEGhVOyG2aoLyOWVhKEWDra9lEs_5S3_dQLUAftKYI5vQHMYXtCEtswbrtq9Y_zV3KoIMhPN5xIERpTe1yi4wiSWufgKAJWcyUZOSPbFU2i8fjc0Llif3i-Z8yRJPXuU9pNJtZzPBhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تمجید لوچسکو سرمربی السد از استقلال
:
🔺
مقابل تیمی قدرتمند و باسابقه قهرمانی در آسیا بازی کردیم که از حضور نفرات هرچند محدودش به نحو احسن استفاده کرد و مطمئنا رقیب آسانی برای سایر تیم‌ها حاضر در جام نخواهند بود. متاسفانه بازی ضعیفی ارائه دادیم و چیزی بیشتر از این برای گفتن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/106541" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b135c8df42.mp4?token=V8WzI8u8NI4Ivllb-hP9NdmH_eM_Qj6sxD21s24EyRj8U9U4Ybz_xtAaj6JzXZ9D_YyBOc3f9Dh7FZI9ivL_CE5xVxqpi95QsC4KWgjqUwJkuF_rfO5j9PL7c8raKV32j4Esy1bnKyVzBERWBLIy6mkc3kFU8pZVqDj14iP9TB2ji98FtCwiUwdc7bpnyFkTsnG_ndMidBdyfUIK2dMvDgXbT2Z52eEZVYwnlRqZwf2dUM5_3TvNfxTvoECm5fUx0BJE5EyXtEftwmKvsm-No7uz5qAyN9xIX7DjuctlQjtHSkihKVbXGDNW74mqFbdR2YIG0tHQxuoPBBe9E-8ruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b135c8df42.mp4?token=V8WzI8u8NI4Ivllb-hP9NdmH_eM_Qj6sxD21s24EyRj8U9U4Ybz_xtAaj6JzXZ9D_YyBOc3f9Dh7FZI9ivL_CE5xVxqpi95QsC4KWgjqUwJkuF_rfO5j9PL7c8raKV32j4Esy1bnKyVzBERWBLIy6mkc3kFU8pZVqDj14iP9TB2ji98FtCwiUwdc7bpnyFkTsnG_ndMidBdyfUIK2dMvDgXbT2Z52eEZVYwnlRqZwf2dUM5_3TvNfxTvoECm5fUx0BJE5EyXtEftwmKvsm-No7uz5qAyN9xIX7DjuctlQjtHSkihKVbXGDNW74mqFbdR2YIG0tHQxuoPBBe9E-8ruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇶🇦
روحیه‌دادن لوچسکو سرمربی السد به بازیکنان تیمش پس از شکست مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/106540" target="_blank">📅 01:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7GAgHphgBXKXARQX2EHVmnEek0AXONHzi8Ngd5Cgsm6XmeXX-lxw6vUd2Tcx3CChAsjhRgHJeiBA-DqoAU_StbsUvh3Dd2SisNki8xvzdXKyi8a7x9oJQa7cUhZ71japLGpkCi5yMswSQGCYOQlcVRxWGde47pt8m40_nK3auDdFbNVUqYqUiPLMqi1--agjufPOjvM7u7QATbqZZK06AJ1YoYsCqQwZetMfYRu1A4tRGimWawXFrxGxuOk2Xb8tCvVbIcGtmdGonNzdbSRN76km7xcDfQ4MqGiIgRZ3afGfkiCZdviFUSOJSu9fjyw_VV8FEsXJmy-JI1v-FY4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
پست جدید یاسر‌آسانی ستاره استقلال: این فقط شروع کار است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/106539" target="_blank">📅 00:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1214641e23.mp4?token=Oq0bVZrtEhXsEl4tl7m1uzZLbh2u8xUgXjoSiBEjL9H5mtVdNx7vTB_npEL-q9pHzewEw6ywHQBrC6IUC2TInPi_-Cvhw7-c6S5N7CyZ3JDvs-s2aL5kvHH3X_aEhtAWB6WMFCRRUyGVisxujpdSTklCtA0kqACnLnKioza1bRRtCRT-L48rHZlReQYnqpb_qlDR7ADk_RZfVEYzIcamKsKBIjZUIFSniFtPErsu9ytPjxTyO3Rv2_YNMhAzxtv-nXrfe4gE00XuU5rsxmFxFnCWmuEibj8I15ijtOsDWWR_ZJYnlBCjC6m0agbUEMpzzyNTe6Yx8n9J15g5DlOm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1214641e23.mp4?token=Oq0bVZrtEhXsEl4tl7m1uzZLbh2u8xUgXjoSiBEjL9H5mtVdNx7vTB_npEL-q9pHzewEw6ywHQBrC6IUC2TInPi_-Cvhw7-c6S5N7CyZ3JDvs-s2aL5kvHH3X_aEhtAWB6WMFCRRUyGVisxujpdSTklCtA0kqACnLnKioza1bRRtCRT-L48rHZlReQYnqpb_qlDR7ADk_RZfVEYzIcamKsKBIjZUIFSniFtPErsu9ytPjxTyO3Rv2_YNMhAzxtv-nXrfe4gE00XuU5rsxmFxFnCWmuEibj8I15ijtOsDWWR_ZJYnlBCjC6m0agbUEMpzzyNTe6Yx8n9J15g5DlOm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇶🇦
میثاقی: بازی مقابل آسانی آسان نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/106538" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
