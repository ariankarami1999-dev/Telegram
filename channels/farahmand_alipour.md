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
<img src="https://cdn4.telesco.pe/file/jWXPGVeNDJNu7KZoJPxhu9h7SB0oKcYWtXN6TM1cbmhYDyGV2qI0tjyCjcO73x0bx4xGJTS_EyPh-1nSQhJcRWG5ev_f1wCeo0Sh6gKtO9DCzR-FwAGre3XXC_NMJPsJQOsXoeVvD5svwWY3UW62fTTiwQlYWVw6LfjvmWBWVjUdJrbky4glOemIZ6FKJr3myCu1o0HH1uWp1pAndyUxUuNQNUUnX46OCwKhtlrJUIzJbq2qEA-kOHOiwWp0zJF4ftKLbmADDR1-dYPfxbBcfjNuDnMnb98dOEfKnYnfrQToKxVGq5hVBNQdEemU81UjDfkoxRjc5HhN_GK0CoGb7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 00:30:37</div>
<hr>

<div class="tg-post" id="msg-5992">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فرماندار کنارک از وقوع دو انفجار در منطقه نظامی نیروی دریایی این شهرستان خبر داد و گفت:
این منطقه شامگاه پنجشنبه در دو مرحله هدف حمله جنگنده‌های دشمن قرار گرفت.</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farahmand_alipour/5992" target="_blank">📅 23:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدا و سیما : هیچ انفجاری در شهرهای بندرعباس، قشم، سیریک یا جاسک شنیده نشده است.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5991" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5990">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارش‌هایی از یک ترور هدفمند در اهواز.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5990" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc8bb9ea.mp4?token=quRvkxBN-Xr-wOx4666BodHr-JIZ-AkArTAv7Ob0DaVZYl4P7VqxXPpRBYPQL0NqN_mKyQlnT930riRGJJ-K1dvEIWwP3w1S0iV_dUSVeJbEn_pY8MOih8LDWO4xSG1tXmwtg5eT0iM604W1c-mNjAFCgefmPgYWq4NZVEL1pdrgx_WX0FSl0VyGp9m1hH87wTxA7ICaeKc9BDjem6Ejr45t8ywgAUaPBJe3evlKGxrZidzZ02ULbzomHLGbDOkaGmxwTBflgAb6-L-4rLy0zDKjLb3iH7_CLAWeI5tiGoPFzqzTnmo4M0GlsUtw-YimFqtrW6YjHMFc6DwuiJAZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌‌های مجری شبکه سه و تهدید ترامپ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5989" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5988">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIpLlTI0pELFXOsNeFkZw5ajMZbyea7hENTtUPJQpK7rD4cqzItgPA8iR8ItnUvuhVuvAgH7jxbhBcTZN3eXjPTJLgcstdANXgCfoK0ZpniCxfJdxOFNUlftaaBcpkoeLYy7mRYnH_MJOK-ARIWvQal1GomGdPcpcYKC9lPU0pxunj7KWeykYuFBBU1BmH6IAVsrCY5q6cTfyyY3_FIUatv7Wb6AuO3qvIFlbiGK0iGNIkR7zRzwO-K0blK5YxkxqovFuOEP5N0CndrQERqAugZUHuKoZeNG_XDCu8jw7bLKO1y7l-8w8g-luImbBe6tcCK9wWGRKdbg0zxs22WlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه‌زنی ‌برخی رسانه‌ها:
حملات امشب احتمالا کار
کویت و یا بحرین است و احتمالا
حملاتی موشکی به ایران صورت گرفته.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5988" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=UyQLsBCVamwq3loJaiTHy8csFuQJ1PSmS6M9XrOEZ1tLdKaxdlSa68uGReD59QyVy_YCXuTe9NfxkEMJx3TcdtdSAqvZFX1w5xQNg7ziZJtRswHQwL7_3y3RojY6hQijVHUZBWKHdPnsX1E3HXrh2l4MtzRPrdbONOv_-eRcURpQZSza5GNlWRibKSLxBrotb7OzIv3IGURtFv23SnSHcBKeJK1faw7OCGWM366XgZ4AYTXQz2bR1WlAT5D2EA5BGvKTuA469g_I_bcebkP5bycCvJCtFoY5Z1ucAv9u90rfR7WuN-pG7cJuK_F32VuosgT0FxHuzjU1mo5V8pbR4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fffbd82aa6.mp4?token=UyQLsBCVamwq3loJaiTHy8csFuQJ1PSmS6M9XrOEZ1tLdKaxdlSa68uGReD59QyVy_YCXuTe9NfxkEMJx3TcdtdSAqvZFX1w5xQNg7ziZJtRswHQwL7_3y3RojY6hQijVHUZBWKHdPnsX1E3HXrh2l4MtzRPrdbONOv_-eRcURpQZSza5GNlWRibKSLxBrotb7OzIv3IGURtFv23SnSHcBKeJK1faw7OCGWM366XgZ4AYTXQz2bR1WlAT5D2EA5BGvKTuA469g_I_bcebkP5bycCvJCtFoY5Z1ucAv9u90rfR7WuN-pG7cJuK_F32VuosgT0FxHuzjU1mo5V8pbR4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا در مشهد هم دعوا شد :)
چند بار زیر این تابوت دعوا شد؟
توی میکروفون به نیروی خودشون میگه خودت رو کنترل کن!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7p1iTApU8POpzzXFlUrTr0X1yZwmkgDED3tUJWhV_i-_jMW-SOCPM2P4F9Jd3nhZDkHvJYrketdp_1svGQIJwvTVbTFVJLD1ujWu7JQmPS3rMgdtnnibnwqkTDAFFK7gnbng8e8uJ_NTwuz4ueQDuEGIY9RhhyADsjC-YtXZG9amek3d-JHSVD_3P8C3V32NKyZVf4AlUgojymZMyhR36NEsEzauGIAkVSGqsOkI-6041CllZdWgQFu9x0G_22z0Cugsub_NrsZPMurOeqFzkCpAoZV2HaND_sUpfWbSbwcS0NY02_HFbOsvtdsmpLxM-Uve7oMgCRtr_0Qy9_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=XRti1S1qSjYwISwhbvpNONb83M9ZFB8AUxfwQAqyJl-YFxIrB0Xo-9nDIdKkOTF6JtpTRgcwgdB6tMexerQK_GLWXC50Itz0WcAIdaxdZ0vx6uDZHqb2V2HpVXvJEpphnazUBkbxRbwC31LnJprmK-YP_g0MaJlOGlU0pELuwQZNBnmzicvSjdestqU83zQlvvhp8XxquNlMBFLHIDvQMACJP8hGIW2Ga6Eyjj_VUM3h0UTX3VkxYhQw9tt30FU6Ad8Z06-82sLv6cedpHMuH0uSYjRkDwXwAi0lzUDtnFpxquufzHcAf-UWerJ_AT5yXg-h1-SgX8wirSH7VacvDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeac2090c4.mp4?token=XRti1S1qSjYwISwhbvpNONb83M9ZFB8AUxfwQAqyJl-YFxIrB0Xo-9nDIdKkOTF6JtpTRgcwgdB6tMexerQK_GLWXC50Itz0WcAIdaxdZ0vx6uDZHqb2V2HpVXvJEpphnazUBkbxRbwC31LnJprmK-YP_g0MaJlOGlU0pELuwQZNBnmzicvSjdestqU83zQlvvhp8XxquNlMBFLHIDvQMACJP8hGIW2Ga6Eyjj_VUM3h0UTX3VkxYhQw9tt30FU6Ad8Z06-82sLv6cedpHMuH0uSYjRkDwXwAi0lzUDtnFpxquufzHcAf-UWerJ_AT5yXg-h1-SgX8wirSH7VacvDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش
برای بازی امشب مقابل فرانسه
امشب چه فرانسه ببره، چه مراکش
مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUD9wU7-hVaeg9IOUTIckMwFDkbt3kh5NfRMt1ENq_iAc9yY4l1FEKWlMNFWWrgtn3RfZAEMDh_H61Y-Enso851R5MvpXCcZhojogz6EFN3aq-OmaU5frwqwQmJ3oHl0SwTA-R_RrvfmX97OqCylYP-IaSFVtEiQjaZkfIsU7h3rkXQewqQ1Oi1bRVWREakvhd-Q4OcPiSqOoQha4Nv-ZlEBYgwNZVyDDpi8KQzvrxC5xMqsiP-24shU8Ib5XIKIypJZc9SNQo-o4cRJqiaz7D-WN9L7akJILv3KkN1euT8HWNz4cw9I-cWkV-gOCuQjZB8QEDH2XEu7T4dw1gaO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8SSHnSVv0tkraq-S0j3cmxJ4wqOgXM9ODWKDy6DMAdLIfHglbVePiF3c5_Zh9Nlyh3alept5cMteNDUHUl8mUl8TejOPyTPU_ne6Df6ciCkx7kFgkbAmfDvTFP2YrGkxDK1NIhQhrQNGcexqhs1b2mwXIF2aMg_X5DnymnesdaF5kGMPy48vbYT54S270ZEF07Me636Y783dksaAhwRyC53Lqt97nicgPP85jCuC1oRl_FRCHoWtvJib89X7ZQFuAP_oqQ9KzLLodHsc4dQrVDeHNSXMy5Bd2ToOJdy58oCyIiY6FvIog0t_zwFz-TtIECH-kM-8SyzVUlIooPc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=NZ9VL61gALAXy3FiQ6PeXFDUjJw9WD5fma5aB8Ze8nVlsnxNbTfgThhCK5HIg8SbTynViOQhAyMYJqe0UJ114DtZEXw7iNXR5m69L5BvGDvIWdmaManrPDW0CNhyRvbFXljZf7PF217EuPGfu53uMwZgTG-hq-EqzAOUyuvSSERMufT1j7CL5OWcNxPiuY0jOkcFY7pmcldIskIZAGAr_V2HcE_CJ8IBP04-moq4uKfgBAez4rv-uZoQRmfE-Ky8azPoYqXEo1aMuB2A2CEBJoF4KBoKDDerwwcVicZvqk9RI0oJ_AodQ8N6OSN5xOCNgbV07Bew_zSw07Ef8yh4-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=NZ9VL61gALAXy3FiQ6PeXFDUjJw9WD5fma5aB8Ze8nVlsnxNbTfgThhCK5HIg8SbTynViOQhAyMYJqe0UJ114DtZEXw7iNXR5m69L5BvGDvIWdmaManrPDW0CNhyRvbFXljZf7PF217EuPGfu53uMwZgTG-hq-EqzAOUyuvSSERMufT1j7CL5OWcNxPiuY0jOkcFY7pmcldIskIZAGAr_V2HcE_CJ8IBP04-moq4uKfgBAez4rv-uZoQRmfE-Ky8azPoYqXEo1aMuB2A2CEBJoF4KBoKDDerwwcVicZvqk9RI0oJ_AodQ8N6OSN5xOCNgbV07Bew_zSw07Ef8yh4-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=sa_9FEZ2CNEE8GoptWFD4q3a12okJGlgmOSFwH-iSOjlLU-04j7nryNNQL8AQB-g7YyDb_i1obozvrWGFLgjCnrfj6n3RR4A8VnaLdZsl12CJBDuv_bLf_e3eaubb-a4_-thczsRL_TFvQihRO-ZyCzsiCjwFg6tvUvEx2zCQEGI03tOkui24VN6dHw3FMcZQdZh7caE8p5Sq7DCVhmi9ePCMGkTpmoq1tryIbA-xVJKjVCcAlcAowY34TlIOlPOqYXX5uDn8meWgebCsB8O-WFgzJ9D9MsHting2XoJNZfwPCCVe45m_hf8lOtLxVQ0QX14Jsd3TfNh2hwjwQjFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=sa_9FEZ2CNEE8GoptWFD4q3a12okJGlgmOSFwH-iSOjlLU-04j7nryNNQL8AQB-g7YyDb_i1obozvrWGFLgjCnrfj6n3RR4A8VnaLdZsl12CJBDuv_bLf_e3eaubb-a4_-thczsRL_TFvQihRO-ZyCzsiCjwFg6tvUvEx2zCQEGI03tOkui24VN6dHw3FMcZQdZh7caE8p5Sq7DCVhmi9ePCMGkTpmoq1tryIbA-xVJKjVCcAlcAowY34TlIOlPOqYXX5uDn8meWgebCsB8O-WFgzJ9D9MsHting2XoJNZfwPCCVe45m_hf8lOtLxVQ0QX14Jsd3TfNh2hwjwQjFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=h3H2dUz7tjFmnNVqGgyEbNObo4BW1xhKpb2J6T9fwzFOxTlFu1_yT8SUnAnCwxQtvMe1qga44Zm4310W4TlYeSreGUk3ATBNVB_r8WjR7dGsPIuqBo6Wkr9TeYgTa7Ki88epvfjvRrGoq2fEg3oXoMlQD2Qu8_lAVSNsvH7WQDcZieWjpynqy4jl-_BPke4FOeKuxMYcxkiOcyMsa1IXiv5oS8O0Vg-ISNZmCgNnuO9hFF9h8OMi_tGcM4AsTHwlNAwJluj4oX42kG6Y08T2OgprBNLKtfnb-jzY8T34U1R1VLeGoQp98fEfBusso_1UpLFnFmUFd2M1XyIaEz_b7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=h3H2dUz7tjFmnNVqGgyEbNObo4BW1xhKpb2J6T9fwzFOxTlFu1_yT8SUnAnCwxQtvMe1qga44Zm4310W4TlYeSreGUk3ATBNVB_r8WjR7dGsPIuqBo6Wkr9TeYgTa7Ki88epvfjvRrGoq2fEg3oXoMlQD2Qu8_lAVSNsvH7WQDcZieWjpynqy4jl-_BPke4FOeKuxMYcxkiOcyMsa1IXiv5oS8O0Vg-ISNZmCgNnuO9hFF9h8OMi_tGcM4AsTHwlNAwJluj4oX42kG6Y08T2OgprBNLKtfnb-jzY8T34U1R1VLeGoQp98fEfBusso_1UpLFnFmUFd2M1XyIaEz_b7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=Mwc5qY7zO79cTC1_gJe6WQymPh_aZ5hBHPlNbJS9So95zzi1K43fMU6GbHUJOJP8pyoo7OJ6LffY2oI1C_mL0mhj6DjFiNYfpZwx38murtoTqOCWtCAJ2BkyxkJC3-73fcLVY3ZzPRM6roDnlwOJrF5Wlv6etW5S6jC9MVHW_oVqK-WiNc7mj1un4TrLNU3SwZEDPSvWQCN1GcocAFIOarXe49sC9ZXZGSVZbg9iEaGP4YmDCquHaki25UdmnH-FseJUDWgzES73SUGA43FcnknuC8omuVsnc_b2aHOPCHqU6cgrfjIWqVuORfwCUJyW8j1TC7L6nVL8eHLtLFHOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=Mwc5qY7zO79cTC1_gJe6WQymPh_aZ5hBHPlNbJS9So95zzi1K43fMU6GbHUJOJP8pyoo7OJ6LffY2oI1C_mL0mhj6DjFiNYfpZwx38murtoTqOCWtCAJ2BkyxkJC3-73fcLVY3ZzPRM6roDnlwOJrF5Wlv6etW5S6jC9MVHW_oVqK-WiNc7mj1un4TrLNU3SwZEDPSvWQCN1GcocAFIOarXe49sC9ZXZGSVZbg9iEaGP4YmDCquHaki25UdmnH-FseJUDWgzES73SUGA43FcnknuC8omuVsnc_b2aHOPCHqU6cgrfjIWqVuORfwCUJyW8j1TC7L6nVL8eHLtLFHOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=BubEHRK5N5HKu_wJnHiitRpuM12V00ZoQNjAA7hNSPcPwG0qwfPq9iHSTP3dJDcB05uBKY_QVBiLCAuJdv8qlQF4wPFVxUwqKiWLS_bxZp07aN_wVlPFFW-GanM8lhiBdUU3g1TX0B7ayXY0Pf4U1zoE-qY3P0Tp9Pb4F3OCzEbCk0-ClVOjO2WfiGEXyrju-JxQSeQji4mJLmeMiY7zJac04e3U5mi7E2JhUYabcIA6johTD-yplpc-o4IA8fT8460IBr2WPn7oqKUlD-H0QflEIiiaT1aVON2FWL244ZCwYozxuDArp8O59BujYal-QiZoY9KrVBByj8uqXhVvzWhNn_DGI93bLMwS4Jf4rVCaa0NQQz_mjfWCJ4MkoHoKKCegByTNRM0_q2EV5mLU2FfDFayJwGfVranT0QRH4Zra4DTgjQxx_O5lzsqfkys0sMQ3uKB9vEbjmFJrU18TvekzUcRF6nuXS7ZZNbosurBkeQnN3QIAYm6rMNHA_v5obVkgMDK9uauXlQ9sFm5Dss5cC_r1pMoW-MDWzOWH9x2N4XUS8jWmEsGUPnlgCCL9nOx6pu4cPG4xjVJyMrhSd2AcWbSoDRJrp_hZkem5H1xxpzpImWgeNQ6ElwU7fGi1bu8rPVV6iHyiVWkZJFmPxu8cOeo9c-GHUr1QUN9RJBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=BubEHRK5N5HKu_wJnHiitRpuM12V00ZoQNjAA7hNSPcPwG0qwfPq9iHSTP3dJDcB05uBKY_QVBiLCAuJdv8qlQF4wPFVxUwqKiWLS_bxZp07aN_wVlPFFW-GanM8lhiBdUU3g1TX0B7ayXY0Pf4U1zoE-qY3P0Tp9Pb4F3OCzEbCk0-ClVOjO2WfiGEXyrju-JxQSeQji4mJLmeMiY7zJac04e3U5mi7E2JhUYabcIA6johTD-yplpc-o4IA8fT8460IBr2WPn7oqKUlD-H0QflEIiiaT1aVON2FWL244ZCwYozxuDArp8O59BujYal-QiZoY9KrVBByj8uqXhVvzWhNn_DGI93bLMwS4Jf4rVCaa0NQQz_mjfWCJ4MkoHoKKCegByTNRM0_q2EV5mLU2FfDFayJwGfVranT0QRH4Zra4DTgjQxx_O5lzsqfkys0sMQ3uKB9vEbjmFJrU18TvekzUcRF6nuXS7ZZNbosurBkeQnN3QIAYm6rMNHA_v5obVkgMDK9uauXlQ9sFm5Dss5cC_r1pMoW-MDWzOWH9x2N4XUS8jWmEsGUPnlgCCL9nOx6pu4cPG4xjVJyMrhSd2AcWbSoDRJrp_hZkem5H1xxpzpImWgeNQ6ElwU7fGi1bu8rPVV6iHyiVWkZJFmPxu8cOeo9c-GHUr1QUN9RJBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BQDYI2LHXvAavd72Gl5WZLArIifTuabdAtAH8RysQjIT5k8-qAoUKopylvz8cPJTx0t3WS-65ySnpHdcjipO2lVvQo_orDxuwWdlf3xNoknSHC4AkG97XI3qOT_CI7PNNbkUeamZ0h0mVXbD77QCyksjPLWsV6fDXfl7bpqD3Ivz8v33Fj9y2fIjykgZkL_DE9GzNQNOeK7HaSwWk33zyxZgWrWGIyumxbYj5FmkAbnel5MwBGrQcbzGiI_wY90x79IygGzNjsinRJkmwpEE2WUzkYMoq4nEIOOkSGOwpoNM0bFN5uUK4SF2LP0UnD3lXxHedCU1s53fr7zRDJmsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=BQDYI2LHXvAavd72Gl5WZLArIifTuabdAtAH8RysQjIT5k8-qAoUKopylvz8cPJTx0t3WS-65ySnpHdcjipO2lVvQo_orDxuwWdlf3xNoknSHC4AkG97XI3qOT_CI7PNNbkUeamZ0h0mVXbD77QCyksjPLWsV6fDXfl7bpqD3Ivz8v33Fj9y2fIjykgZkL_DE9GzNQNOeK7HaSwWk33zyxZgWrWGIyumxbYj5FmkAbnel5MwBGrQcbzGiI_wY90x79IygGzNjsinRJkmwpEE2WUzkYMoq4nEIOOkSGOwpoNM0bFN5uUK4SF2LP0UnD3lXxHedCU1s53fr7zRDJmsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjVpt4Fanz6gYaX6nXicHC1lirmrt_UScWjePQqLN5wTTIz_f9HvSm4-4v4fItPeWIW4Ndzj1jJJzGEXof8SwC53xcF1vuHHeCLVrOtATY-Yw1IFXCZa5i98P5dGr36AKuAf8t7FStKh9D8BQH_Vyi2PeXjyJnx-TY5cN6nuMfNegR56Kz4Eeu9uPIANJw5h4MElHB9U40MWjX9FBw5eYxpPruVRUbNKPwGdDSajKme6O-knvStGqvLNJIkBfsvfPZ_01W5jVgzEabEg8qxeEWrZWSV1AvI5_Ud9qUT4IAgJMXkZlTzQDAQvXH-6ZSbpkolAdV36MZ1xmVH8lVRJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=jmnveYr83k-w38Mz2GVMxnowqnZbKovqlOrCoHorMLFOmYCYoOWGisHa3j8g6A4xhWh1V1o67aALROn4codbRmBv9NmQ6NkDpgasPIqrgjRIcfCV4wpQzTQmLQ-ln8f5JhnhhGe8MQrCIBmHZzuun1zfMqk-otGYyxokivaoUTWNLS8405r-2G-UhoErhubRbcuRM8T7jKbbXZYlz09oopCui4hyzlUR440iTqNhaZKaKyjYnM05yOaiXCQeTD5lguom_CjhTAfv9rxemCF1InwCYxSefkhf59k6c4TETMXaFicdR-FToIg0hnDzuSd8mnPyrwHf8bH-EwEOw_8IiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=jmnveYr83k-w38Mz2GVMxnowqnZbKovqlOrCoHorMLFOmYCYoOWGisHa3j8g6A4xhWh1V1o67aALROn4codbRmBv9NmQ6NkDpgasPIqrgjRIcfCV4wpQzTQmLQ-ln8f5JhnhhGe8MQrCIBmHZzuun1zfMqk-otGYyxokivaoUTWNLS8405r-2G-UhoErhubRbcuRM8T7jKbbXZYlz09oopCui4hyzlUR440iTqNhaZKaKyjYnM05yOaiXCQeTD5lguom_CjhTAfv9rxemCF1InwCYxSefkhf59k6c4TETMXaFicdR-FToIg0hnDzuSd8mnPyrwHf8bH-EwEOw_8IiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=N7QsMqbxRQufhi8B5kLJd-GzJjrKoyOkiB8Xf4I5GQePV5NJKo7frf4PcCO0nwIiVqyH5o9EPA6iXBG9bgP3uesuBEvspbpM5PF49uNF0N8YIGxzO53EqpP8z5L9fKeuUlJCzBixxh9FNo0FVv3nf1mmOKrskSXmR2gpYbr-kDRGnDEP38ACwdrJw6C9V3yFBnzcVNUxt-8GQjYA3KlCJcDDh9_zoE-Uz1SMbkf-vnEHj12lqihPHcFv7debr2L6dDuj9L_mlVq4hYbGR3y5_P2PW-XNfd7-WFOvoU-RoPGzzG81Izs3JO8WWtrGww-zvMu_qSg5eaiw4D0VCRqQVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=N7QsMqbxRQufhi8B5kLJd-GzJjrKoyOkiB8Xf4I5GQePV5NJKo7frf4PcCO0nwIiVqyH5o9EPA6iXBG9bgP3uesuBEvspbpM5PF49uNF0N8YIGxzO53EqpP8z5L9fKeuUlJCzBixxh9FNo0FVv3nf1mmOKrskSXmR2gpYbr-kDRGnDEP38ACwdrJw6C9V3yFBnzcVNUxt-8GQjYA3KlCJcDDh9_zoE-Uz1SMbkf-vnEHj12lqihPHcFv7debr2L6dDuj9L_mlVq4hYbGR3y5_P2PW-XNfd7-WFOvoU-RoPGzzG81Izs3JO8WWtrGww-zvMu_qSg5eaiw4D0VCRqQVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSg1bYCWah4eVYyx2tDQ2cwqux_U-0c1os1vz_Vw9pnt7GOnIRBmg4VALGrdATxDHhSvY_70ws2LyUq_Kv3G2WYb8xXsGWHPNwUE3sx3lpOInpDaPn4CvSw3E3PVDGPgTTMDta3WlK1Oob-lmboeTYvtRqn1YKA3puqfr4pDe_qfPGZMxEIbBy-gAFNklU8lQs0aCKJBxh0UmqWItp5cBcaZbKWqAwxDp7VF-RG06S2ZmGM-2EwgT4eIM8krpVfFjA2kFoyWUP4qzm4Z5Q-eA5JbU0cK1OpZIJoUBLV9vlkU7lmudf6H17F3y_5moQd8g1_aNq1saQvaP2O6567pKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=bpN3u3nJtTwm10Walx8rvDYp6SfHsVF7LeRciMTx8I3T01hifGXf0TdvlykmcDJ5A208pZBBu94-j5ZfwPWEAFGHl0v79R1pSNJVkjKGwU52Hq9wXmqrN0gXQk_UQseSwHo0EHRDZRZFaxJHhZFH8EAr3k4W7_2nsV1Ecvaz54yka20n8pBHL69_27CGymdyEQcR-ACG3JxskJspRRk6Nm5kG4xBdYO1xGCDzV-M6T95UqeUmqarv4WQVL6hM7IS1m7-b5ANZZPafeBfVW7GZ9vv5MUj1iinzDUzX78fOEasDpwukb6kLXCeDyO3pLsOOoucvM6JxssAqQgJYaBGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=bpN3u3nJtTwm10Walx8rvDYp6SfHsVF7LeRciMTx8I3T01hifGXf0TdvlykmcDJ5A208pZBBu94-j5ZfwPWEAFGHl0v79R1pSNJVkjKGwU52Hq9wXmqrN0gXQk_UQseSwHo0EHRDZRZFaxJHhZFH8EAr3k4W7_2nsV1Ecvaz54yka20n8pBHL69_27CGymdyEQcR-ACG3JxskJspRRk6Nm5kG4xBdYO1xGCDzV-M6T95UqeUmqarv4WQVL6hM7IS1m7-b5ANZZPafeBfVW7GZ9vv5MUj1iinzDUzX78fOEasDpwukb6kLXCeDyO3pLsOOoucvM6JxssAqQgJYaBGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sza2vd7bXY7UmMK363wsukVX-HarJGlAJDHZXbH_n1O_tvkGkVm1xnnNUF-qoiLl85rh6Ppa7dqG1wrKs5SQGRtJYOmW0I7oquih_S0Jdh6mMl9jV2d3Jnr_0hrUsA05shlG616_azFeC0RfBEU0hXlmXN1C3I9n6-i2adEuwESZyFECiu7FjhMrtNwQoO4O5tUkW4h0C7248OO8OR0wC_9cK0AwUs3Vo6MP0RtkceZnzKubsRxgnbDbcvCaU2ztw4XReWU82_QlhHF80mp1kDnjBXo9IGAbQwvTOtpJ78kIG9kbHl-TUNLwTdYqd2K_jKZ2TWV3nM2qhoghtYIBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=AF7JGjnfFzN86bd1faJa24OJ2H6v6qGxTPi_JlbP3HTYA39RMx0w99pXPj7c-Dsm5k5Hwv91c6yEjo_v5a9Gq85TKFgokhxLFriRGw_DTGGfQXt0FGN8vIXjDg-kFNQmVy1eL6xLgLJ1ANJl20oNKeCxMLYAtd2aJvPG4zA0gss2ErXO8D49N_fIHWvGcC8RBR65-_1ezkPksei1mDJQfdgqrgA4BDb95cFGVThZB4uBp0QUz5IhaI_Zx8rNJKRPF2rTKJOYl0YMH8zSb_6dabC_XECUfMLosqzMhWs5xS5qxJuRL62SjwiyhSvwYEpUUjY_N9GFkzEnFvE_a0eTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=AF7JGjnfFzN86bd1faJa24OJ2H6v6qGxTPi_JlbP3HTYA39RMx0w99pXPj7c-Dsm5k5Hwv91c6yEjo_v5a9Gq85TKFgokhxLFriRGw_DTGGfQXt0FGN8vIXjDg-kFNQmVy1eL6xLgLJ1ANJl20oNKeCxMLYAtd2aJvPG4zA0gss2ErXO8D49N_fIHWvGcC8RBR65-_1ezkPksei1mDJQfdgqrgA4BDb95cFGVThZB4uBp0QUz5IhaI_Zx8rNJKRPF2rTKJOYl0YMH8zSb_6dabC_XECUfMLosqzMhWs5xS5qxJuRL62SjwiyhSvwYEpUUjY_N9GFkzEnFvE_a0eTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9y5aOMvMoD9SyVt1LjwlsLU6_Ix-YxAAW9RtyVQjc3o7VnikrBAtCNrsA2TlkFl8jY3Fh7k8UELLiuC-w-kGBSwUkB-bdRzYEw2D2K8f8SvfK69VWzXTw46-gkXIH18gZ3xi_GLt7MRD60KJSTq94xNr1K1RH6RHoKIyOJUONB36478UTYMH7KgFg5HUIMKKRHO41GFG8dnUzGlgVoCnlt_-UwcP9F0qlNFUYI8SHSm2316D6kAl1PE132_w7VERUStp3ox9C9bCuEUvWjXxlrqdI2fEiNer1QKbiLwTnoYmfw-cb9T_mOyvyysin9aRCS9kflNCSuNP9bN6aCVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=l6a2odKNzxiT6TyxlZ7vqEQKBH-B0wvd9mfpVljUnB7l01-MLSObZqUplrzv7tb0qqR317obNqlwOBCkE9UiqvJvIOP00nmU8kUvKaEmS2L0GpHnlxIS_72ISZanTzsHgv99yVBFVxuGzut0P357XU45j1CRSnKQ9tHP8JhzFQbwG4OJDkxALnJ30xTKA6ErLop_E_IT9uWvBgn_f2uKqsw7HHhlXFAOgFWtH6mYDVn5j0xOBOQMibi7zBO7crwntIvU4VgqfsUSbYbj90Iu6K80fvPcuszfW-PdHjAvitFSK2-A7JMdltPonvK1vldVM5gdodcOAe_d3LbtueJ-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=l6a2odKNzxiT6TyxlZ7vqEQKBH-B0wvd9mfpVljUnB7l01-MLSObZqUplrzv7tb0qqR317obNqlwOBCkE9UiqvJvIOP00nmU8kUvKaEmS2L0GpHnlxIS_72ISZanTzsHgv99yVBFVxuGzut0P357XU45j1CRSnKQ9tHP8JhzFQbwG4OJDkxALnJ30xTKA6ErLop_E_IT9uWvBgn_f2uKqsw7HHhlXFAOgFWtH6mYDVn5j0xOBOQMibi7zBO7crwntIvU4VgqfsUSbYbj90Iu6K80fvPcuszfW-PdHjAvitFSK2-A7JMdltPonvK1vldVM5gdodcOAe_d3LbtueJ-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqhU6t2hbgN0d_FfdXoKlnfgi1PYlY8rNhtUoR5MPTrQmGuTtH6pNdSUwfvBOAK6Z7OiR9dd482vWcGtEUpRc8DCYflB-M1S7tZIPsxYm09jCdkPHHPGt8OfmrJMojWd5luLtgiW0ZNSh2i7QjdywmXYxj_ofizvbOnJf_EwF4NA2fS-N1LPZ0iv77NPbHUywDhgRYPwPjWZLBTi6psXUg1ESZdBoGdnCYWi1xCaW2Vmud13p4U0_Ue8GVrWwrd_IerM-2cvrNAgGNSg9Ec3ZG4LhqM93FWZehlYWH6ViJ7QBcLidHq1rmDssry8ETqP53w32jbbIGyhBYCAtMspyFO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqhU6t2hbgN0d_FfdXoKlnfgi1PYlY8rNhtUoR5MPTrQmGuTtH6pNdSUwfvBOAK6Z7OiR9dd482vWcGtEUpRc8DCYflB-M1S7tZIPsxYm09jCdkPHHPGt8OfmrJMojWd5luLtgiW0ZNSh2i7QjdywmXYxj_ofizvbOnJf_EwF4NA2fS-N1LPZ0iv77NPbHUywDhgRYPwPjWZLBTi6psXUg1ESZdBoGdnCYWi1xCaW2Vmud13p4U0_Ue8GVrWwrd_IerM-2cvrNAgGNSg9Ec3ZG4LhqM93FWZehlYWH6ViJ7QBcLidHq1rmDssry8ETqP53w32jbbIGyhBYCAtMspyFO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFtnmiJPxY8-9Ca7mKgJg18N2Bp8TLNG-qGH3LUk-tvtuMV9o9HIHqgM5J7PX39TDVgvU-uGOl4MNZZNYviDDU67HYTNq4_6o_cxLr4a_6LsAcxHlrQw963zgBwPkgIn3S8x28S1zjtLfJhLvXb4LoPnkiW2tZodEJviJwp0C-w1MqLCDWqytOLyTippr8sne9n3oLlvPBu_A30FkE47xH6omU-c8QJBqL9KEIOE0gOIYsXFldW0vkOuK_I3saCfrEIOvW3TSNjx4UG3FOBS1x-mf3-Gki0aZJUDnqb9RWAyaTPKr4LTlfnYfC0zy6itwN02VeOFnFtevk27RDsHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Rh-0h8j2tO3vdegjoNni1GomwXhkWACp51c7-PpJkoPncjjLnBuc0VE8VHxVVPFWnj8wJL2n9TQzVplRDtO0tvDghXdx8pJ6wyolpnAXUV_EPOIUzA27C7QFecLzt9mMtnN9hrr7I-cqzjlVnsNkG1f4yPKErt_PSkvzctHHyvNRKKNxfItimGzOrkcZyTdIJaJpjTsBtNd-1LW4ruyJCJ-6oG6gVuNwu5UokWPQzPIOosF3XYDTen0zCIePwQNviuwHXvcUOxy8a16Mqz-DPl5Jd5Gxh64wW90oLWMds9j7zXhV_cDQNrv3dgeYjZiQdsSJohydnElZNjkh4DSkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Rh-0h8j2tO3vdegjoNni1GomwXhkWACp51c7-PpJkoPncjjLnBuc0VE8VHxVVPFWnj8wJL2n9TQzVplRDtO0tvDghXdx8pJ6wyolpnAXUV_EPOIUzA27C7QFecLzt9mMtnN9hrr7I-cqzjlVnsNkG1f4yPKErt_PSkvzctHHyvNRKKNxfItimGzOrkcZyTdIJaJpjTsBtNd-1LW4ruyJCJ-6oG6gVuNwu5UokWPQzPIOosF3XYDTen0zCIePwQNviuwHXvcUOxy8a16Mqz-DPl5Jd5Gxh64wW90oLWMds9j7zXhV_cDQNrv3dgeYjZiQdsSJohydnElZNjkh4DSkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Xnhvt_J-L7bcYMCMtSch5RnhLvJRmqOcpTw-9tgCPZq9CvtuoIPTNZh-RukmwkEY9-NGWJZWi0bmqUhTi-nYlpI5oBFMIcEIBYdx19cBjLMyKYuwjDlAnJxEyFG7axqqB6SikTIM_na-4uF51Oi8k68uTRQLgTuq8L3ZE9q3IgwcdzHiKBjLDq_ckPIqlS77NYGsrCBiEypjZsQZxwrjHnTndiLcaD5Y3kyqVFooxupBiKcJekLQr_gsQ9OR58H5jMExQC62nH-FMnMrTWyGpB0K6OziJV4l3dyO5JMJWouyYyl5BER3Gyg2sn687B1076oF1zADaYHjMHf5cCVwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Xnhvt_J-L7bcYMCMtSch5RnhLvJRmqOcpTw-9tgCPZq9CvtuoIPTNZh-RukmwkEY9-NGWJZWi0bmqUhTi-nYlpI5oBFMIcEIBYdx19cBjLMyKYuwjDlAnJxEyFG7axqqB6SikTIM_na-4uF51Oi8k68uTRQLgTuq8L3ZE9q3IgwcdzHiKBjLDq_ckPIqlS77NYGsrCBiEypjZsQZxwrjHnTndiLcaD5Y3kyqVFooxupBiKcJekLQr_gsQ9OR58H5jMExQC62nH-FMnMrTWyGpB0K6OziJV4l3dyO5JMJWouyYyl5BER3Gyg2sn687B1076oF1zADaYHjMHf5cCVwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVg3V40bhVL9avG14guKa8bTJ_CaaRTBkUYiu-OP-ib2kawsN8nMC296n8x7oLvkb-M6WHv00R1RWq43QSSOrbDWM_ZVPbFg639M3IalthgUv-52kWw7OIS1GWSZOvdIBTM0gpHlpa4aLc9hDsa_g2xnaWJG0MDLAfs3gBoyA6yfKpL2Kzwe7VXp_k4x0QGwESyc-2x1-a8Oaypb3xep_I_dGnogzijaqblZEAGETazbFjQnEkWl3nJ0y5-QoJpZTQdjeByF8YUfKV84yrZQ6gqGH9UD4sQLY8OM9GS8YJct70nkt2N1EiWWytP_pU9NcWskjoVsKxrYif1XzZkSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=XBTM6bAQNrIVoH83Eg1NgB8O9km4yOOjXR1QAQkX5z9n1TTV0wgr3ZJTh04suacbUHDh3SRPGJnAiW_2WvM2kzVE42ZQpPc9ou4exMX6xrzx68TkwmbwQXao21OPnz6WtlcpNQCo9xW5o4l9PEcNoyY7JQU9fJv9AZjV84Fw7jmUbXYT7fKWnMzW9zUmSTKG7U8AbZq_Orzsx5UMubOkm8PYdbxst1EOQI2WuqB5tWVgkpxShRSj6OhX80AXQeLw5uVJ4JwLtbip4I32b09pTnLS3cJX4JcPVLs8MnIT5uA6LVi18e4FkBQMddQtQMbBPRyr8SGdO-Ya4S2AtdlGbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=XBTM6bAQNrIVoH83Eg1NgB8O9km4yOOjXR1QAQkX5z9n1TTV0wgr3ZJTh04suacbUHDh3SRPGJnAiW_2WvM2kzVE42ZQpPc9ou4exMX6xrzx68TkwmbwQXao21OPnz6WtlcpNQCo9xW5o4l9PEcNoyY7JQU9fJv9AZjV84Fw7jmUbXYT7fKWnMzW9zUmSTKG7U8AbZq_Orzsx5UMubOkm8PYdbxst1EOQI2WuqB5tWVgkpxShRSj6OhX80AXQeLw5uVJ4JwLtbip4I32b09pTnLS3cJX4JcPVLs8MnIT5uA6LVi18e4FkBQMddQtQMbBPRyr8SGdO-Ya4S2AtdlGbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=SLlOAJjvYOZzYgSejd1aDlKzA7Jc78_u-tC2bvtDxl_n7dOzES15Q2NoQANE-PBvN3OiZ7yRkxZlCiBJlWOuOhbrOQaHMbWF5JFhCANFfiXCJxGQvzxvAbs47EQ9WG3kbZtxZ0LlfA7zZ5oax-KFQHNqQM5LpWfZQOGSMa12ZK5ZyfNI7mP38W0V4lGcU-X_ejVwyKoQVfZ4G6drXlT33z2Vd-NXhCGVOTG7Lt5VUT8L9QW-J34gnGdzYUr5vA4_AG0CMMf6sHFmRqXnJ52dyatO7tZiWhmBa_QSQEUpIQaG8Cw8v6CyohfGm8_CbAIxBegHFKtodTWzLQNQAain8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=SLlOAJjvYOZzYgSejd1aDlKzA7Jc78_u-tC2bvtDxl_n7dOzES15Q2NoQANE-PBvN3OiZ7yRkxZlCiBJlWOuOhbrOQaHMbWF5JFhCANFfiXCJxGQvzxvAbs47EQ9WG3kbZtxZ0LlfA7zZ5oax-KFQHNqQM5LpWfZQOGSMa12ZK5ZyfNI7mP38W0V4lGcU-X_ejVwyKoQVfZ4G6drXlT33z2Vd-NXhCGVOTG7Lt5VUT8L9QW-J34gnGdzYUr5vA4_AG0CMMf6sHFmRqXnJ52dyatO7tZiWhmBa_QSQEUpIQaG8Cw8v6CyohfGm8_CbAIxBegHFKtodTWzLQNQAain8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=WMXPRF-QGtxN0Pat1loREYx036vtZyT5oeYIyIQOxExCFuywzESI1-VJinOxQ58Q9YToqgZp3UFBWwKh4gmt79kQH9KTrg_F6URjfTpr2sobNq8okY1n1xs5Q5kH5vqsWQ9MW9CkuauOXOXAZ-Rw08rCywTNPkia8inc6wfIahpWl7rpiL_e1_orR_NFQ2rRahqnukJow-5j5anQKcgTMV9eQihL8t8wq5PW483rtqg1CbFLvVKQyX9s_8gEKvPN0pC998XsRMVR62ORjddD4leR7gxOKoGpsueaCl-kW9RRDb9tceooxTS2QqefTdiEIgUWwk_R-UoVkbJaiZP66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=WMXPRF-QGtxN0Pat1loREYx036vtZyT5oeYIyIQOxExCFuywzESI1-VJinOxQ58Q9YToqgZp3UFBWwKh4gmt79kQH9KTrg_F6URjfTpr2sobNq8okY1n1xs5Q5kH5vqsWQ9MW9CkuauOXOXAZ-Rw08rCywTNPkia8inc6wfIahpWl7rpiL_e1_orR_NFQ2rRahqnukJow-5j5anQKcgTMV9eQihL8t8wq5PW483rtqg1CbFLvVKQyX9s_8gEKvPN0pC998XsRMVR62ORjddD4leR7gxOKoGpsueaCl-kW9RRDb9tceooxTS2QqefTdiEIgUWwk_R-UoVkbJaiZP66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=DQDyHotANL2n5mHvKAdwZ4IsYL_4apgLG-CZBlaXG7PCfSRji5cY_O3mF8U84tMbnq14bMhdxlHJgQnN-G_t8fbP5F5BH6HEme2pmAeSVSHrTv2IVLMmTBd_CxeQxKig6YPqye_x8Gnuatdy7D0oM-00vcDo8rs7d9FNkKCIPkNkMc0rqAIs7MiArUgTX-HTY-BZP7TMH2iGEqeKwCCnS4gyvY-7nO0RIAl7SPCPZOsg12IONu97WZCZfLCd_dmCT6OhJ0d5dkWb2j-hOfF5xnmNOHpO13wTOr-bzPto0zVORCuliST-Knq31Sg016NBux43GXl4db1CMDb11gbrcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=DQDyHotANL2n5mHvKAdwZ4IsYL_4apgLG-CZBlaXG7PCfSRji5cY_O3mF8U84tMbnq14bMhdxlHJgQnN-G_t8fbP5F5BH6HEme2pmAeSVSHrTv2IVLMmTBd_CxeQxKig6YPqye_x8Gnuatdy7D0oM-00vcDo8rs7d9FNkKCIPkNkMc0rqAIs7MiArUgTX-HTY-BZP7TMH2iGEqeKwCCnS4gyvY-7nO0RIAl7SPCPZOsg12IONu97WZCZfLCd_dmCT6OhJ0d5dkWb2j-hOfF5xnmNOHpO13wTOr-bzPto0zVORCuliST-Knq31Sg016NBux43GXl4db1CMDb11gbrcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=VFyOO_Z_hxPmrfjNKSb9PKhyP9eTcffqVN02t1-XJpNl7AyMEo85eCAbmHFrGScQiF9iQ2_FcogjXHvFm0Fy93X1kF2lwRxCRRrzpnfjfCK3te4Pc6GULZLfIYw0I3vS28FhO95cyVX8R6B8YiHOsv8dds8gP9cUrULFBUaaBQvbUJEZC7_JGuKf-b1fnsgEzz5UwV6f2WFgIEy0-rSs6K40c8zgmk3IcPWyG_c6r7WeR5l0vGZ2TfNQYzBhcSmnXD30zJkuPGCGUQCij4Zpioh-2eqRM6t0nllMhNGfmS9tViGC_TQ3iamm8t_uNj67kzVynrDnTtliJTH7qJChSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=VFyOO_Z_hxPmrfjNKSb9PKhyP9eTcffqVN02t1-XJpNl7AyMEo85eCAbmHFrGScQiF9iQ2_FcogjXHvFm0Fy93X1kF2lwRxCRRrzpnfjfCK3te4Pc6GULZLfIYw0I3vS28FhO95cyVX8R6B8YiHOsv8dds8gP9cUrULFBUaaBQvbUJEZC7_JGuKf-b1fnsgEzz5UwV6f2WFgIEy0-rSs6K40c8zgmk3IcPWyG_c6r7WeR5l0vGZ2TfNQYzBhcSmnXD30zJkuPGCGUQCij4Zpioh-2eqRM6t0nllMhNGfmS9tViGC_TQ3iamm8t_uNj67kzVynrDnTtliJTH7qJChSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkuUBcJ5tavwuBYU0d_NRAXyrpGRZB9HyVoM7lZRK80iz3W84o6ymd9zEU5V2RCOidfZUwHakzkcOrtDHa_22sN8L6DD89WQJLeQDnCTCiZFPIn-z-vm3SkXE-8AvpSI_qokp7Mqg6jZ5t3kEMZQsKOXZlz4xtYIuSqVrlV1gzfgVKAzUW7vKMMlTCf2GMxe3dtXoO0Ffk8oHaCpbI2g7_OQMBfmOUd2zj-zU537OAOClT5aIyrcjbi0C9yPpwkjTXvcTKgB35LfqvrG0UFEOEt8YqYsc9z5rsYbrudMAE8zIpTWmEkL6LF6B_xL2cFtkGBfkoaXVNzZCWFZOwb3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sym8cWynfJFUyNEVAAvydgn3bUBJub7_SCoZIRBPAIaNfnmmbXArVeVZKrKbC5IAI67XvK3JiqvwPxI0joyr18dAecMjlUNWb298sxW8Lt2xs73LkaB_ShCod-UutCuXVT2T8PzbSk1WT25fP7ucCo26SFVfnkQ3PRGmV8RKItZKyCRmg4HgJHIXpKktYh08L6XtKdsE2Elf4XeM4KZbDoANkhukNk7PY0sv8Teira73vU6JY02oBDZmc7YJKyepp0hTIoON1QHTWk6N3sMN7xYON7oUzqfjUpeCSli5woRXOeYg1w0J-SrfOgvEec2x0Ev4qebJT8H0xCPhzH4alw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcXW6diquyEzYgE6UfAYcDThC4k3k6pGSzgNTLFvZgEZvTsJbmHwaDFzCHuAD7mAMVt-vt-RxSK6hjtlP9xlawiXa0hOFUdguK_b45-1UXN0nmdCxDCiTy2npI_glw3PVqpzR5uFw4OQ7Fj0kaQpNnASr8aeH_GEht5cIiXwhkJA4c_qLGrQ9_GPGfMQPkThmAgfdp3Skg9xxPlsjVDlRWJzKGrkiZfqAJ5VE4tKBR4yDmoHwqS58BYYfens6TRblpSl73Ye3zDLfzmNde7KTgC9vDY0vM8gl_fLjZdiaLil-Fw7oYeswQuziXTscUEaoBm-Kca3dzFB55IYKz2aeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=VcAG_hq58-dYrrYY_mkJo3I2JLtUUdwG7N5jSqZE_ngP81NEe-XDrdY2nNI-QQqukVRTINk7G0ZalKwMal_osbdZHwCqYQumrech5wG1gKAQW8rend0Kx54WbB8CNgHDIahDxKfvqBYGOC8eDhCrv89pgeCJKQB-vLCgEFp-lB11X9K3gULqnUZYHOgNalTgaVCwJknJ1EnQunkcYdbjU-kAS_dJP3tIyj5n5nviZy4wdYl8L4IvoKXvv1LjDaJ4EnvRnE-fvwmY0kl7Q4QHt305OOSgJsoGwzgqGSG1MP2FnMYTtTW9eSSrZC-3r2tlP0aV5vmFTa5JIyic0MycaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=VcAG_hq58-dYrrYY_mkJo3I2JLtUUdwG7N5jSqZE_ngP81NEe-XDrdY2nNI-QQqukVRTINk7G0ZalKwMal_osbdZHwCqYQumrech5wG1gKAQW8rend0Kx54WbB8CNgHDIahDxKfvqBYGOC8eDhCrv89pgeCJKQB-vLCgEFp-lB11X9K3gULqnUZYHOgNalTgaVCwJknJ1EnQunkcYdbjU-kAS_dJP3tIyj5n5nviZy4wdYl8L4IvoKXvv1LjDaJ4EnvRnE-fvwmY0kl7Q4QHt305OOSgJsoGwzgqGSG1MP2FnMYTtTW9eSSrZC-3r2tlP0aV5vmFTa5JIyic0MycaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddiReEzu-ErK5rLjgRtHtrqoearHgLuhXVKYVkuCxmYyjlwsCCMdeTSV6az-Hnu0GyVm0uneHqTqQ-6SQ-k3VUG9sviYL0-ejoHVk4_kWotZdPS4TkdvayxfrjsbJUURmC3aGUSe87wB7DLs6EAIxnmgQ0JHe6mWWyg4VWqjPr2zHGVksMcSUzKYH35xqsDRyO93JRqfqehzL4WGXZdMnWjPOI_D5dlk5UGMT1Wgld6fSkVct37xDg8Em8iNEZ8hJNSiJDzoA9w9Q6tM9InwEH0x5bHq3Gz_ygNXxnANfcne3gUUoP25j_6FZEoPfuLeHHwAwWDgLELM_EHpuKNigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=qPjPqq-ZeCOL2-UCUCghM6dMO45MwnNcOr6nyD-ovG8i4knKUfSARI-R_dwMhWBmDfzgdCM5MwGMghwSJZ96tRcXrUGyjkXDDQ3dG72HMgstPJpI57Wuy74QyivmdC-WIu3Ix9tO_KRpfXZvm_fEIKJGb4meH8mkxOuioikWVkXhlGcFpyzUQgPIbA7Y-n2d5glhGXafZAezMBMd58c1Rw-p-YVNmaOQHFTxhMWErau4nNHBXi_GT6JQYsw18Ktmf9apFAgVBLU4Wnt2NR50e6wrsN8mGMaMpIeNKtkY7E2vJV__bss4KBoM0Wifvi8r8UeiKXf-SyKw26aExwYVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=qPjPqq-ZeCOL2-UCUCghM6dMO45MwnNcOr6nyD-ovG8i4knKUfSARI-R_dwMhWBmDfzgdCM5MwGMghwSJZ96tRcXrUGyjkXDDQ3dG72HMgstPJpI57Wuy74QyivmdC-WIu3Ix9tO_KRpfXZvm_fEIKJGb4meH8mkxOuioikWVkXhlGcFpyzUQgPIbA7Y-n2d5glhGXafZAezMBMd58c1Rw-p-YVNmaOQHFTxhMWErau4nNHBXi_GT6JQYsw18Ktmf9apFAgVBLU4Wnt2NR50e6wrsN8mGMaMpIeNKtkY7E2vJV__bss4KBoM0Wifvi8r8UeiKXf-SyKw26aExwYVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYxULA-6yFUcqoQEM52VzswB7jDe_huwAOyY9a0ADmDdOSqyTEzSJiTTxQd12rV7QTHXYUotUGDaS5-7g1j_kw9yoil4CR0JaJfQvSMYUYFkkGUhSLsuoqCYrTG6kfffs4yrjLAmvQ_Cv1i-cF7EOb21xIFmnO8oG1GbA4HEoj0Qehlddhl9aOAjrXFs1s5lv5aTsei6D3M81DWTNMJFRLop0hc6363G3pqjkfM11uPhn49fHSbKHnXZur8SIi01T6zuGA7nK36hxvi37K4ua8BNmRfidv-Dh21vOP27mIbRSz14K8zurJf2aN3pCWZX1dfNoeZ9zvh2CtH_CvZaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJqfBKWL44FBG8zcI7oDLgN7r8JMbphHqXuZXFdb4McfPVqvqVe1JFHkiDyxnntusmjbJVOIHq_sJI872HWZ6aVJlkYHa974VeE1YhGYtZLoNXNFsTqUBbxkw9jmAEwOLYwgaMSUNy1Y4xS2t1tbzqDIBXJ84ym5ujsGrvpYp3Eky3wcF50511oKM30bKTFicciLZW86l-P9qXxDhCuhIDrn8lcatYQkXw7kx25YXtmbXD8MrwWNuvTcB34gRu7UOt5c6GB2OezLM1zK-ZdE7TMNdLF6fFGPvKkzxTke_Ks8XbNQ4bR2iXeGpkDxaDbuR55GWoPPL5EWrdp7e43UAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=b8C64YZVX-1lPYA-Cyv5gfZA2xNtbiLwy2TL2CfSe9VVhNSWkR_UFmWyZEdxT34K0YDxfz686MTZ8115fR3HVAvlist6_qTro2POzl-y91EQX5g4dQEejAm4oCq-x-FW9PKwcY3I3YxfZaPfGBK50uuXfh26JEUAy3RnDbw5JzjA5YMIw-6Ey0uu9LfRYSdTk5dah58cPOLvbSvAwwd8nS1S-QwCxysqM9B0pgdlHR_Zfzn4vrspx3SjBv13IJQwxJEMSuCPO7xcd10cS1AFKKDOdHjUmQpHGL6JynCv8iECqapyBzEoLYVJTRF3aBPsOb229cBOAqjn5wFNFkShhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=b8C64YZVX-1lPYA-Cyv5gfZA2xNtbiLwy2TL2CfSe9VVhNSWkR_UFmWyZEdxT34K0YDxfz686MTZ8115fR3HVAvlist6_qTro2POzl-y91EQX5g4dQEejAm4oCq-x-FW9PKwcY3I3YxfZaPfGBK50uuXfh26JEUAy3RnDbw5JzjA5YMIw-6Ey0uu9LfRYSdTk5dah58cPOLvbSvAwwd8nS1S-QwCxysqM9B0pgdlHR_Zfzn4vrspx3SjBv13IJQwxJEMSuCPO7xcd10cS1AFKKDOdHjUmQpHGL6JynCv8iECqapyBzEoLYVJTRF3aBPsOb229cBOAqjn5wFNFkShhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJNOyLESCmljwvCM4SJJ5EP7qSh08rJFuscZnFNjV-WKj6_ua7WXv74HxdxiCcMAhVyaVk1sGJPS3wXihG8tDBvkF3q6dRuwD0_bRGEDPcl249Z80f_fwh4HYNUKnQWT4ObLOr0328tHk6G5FSINkcFxYcRZAcWjgvYdNMvSxY1v5nkZayjmwWpjjqjP0gxrWbJPVqQmfJNOexAYpAkaxfy-HErWbuU7ItP1IKUuxjTp52ClXQiBtINQm3kqMXBs1IWbaV0CpBz-WfznVexE8hfK4wrlmeoMp_UG6tMp49WLXi73o-9tu4hn_z-UY02s4ig2_JYqH4rw1yBUUljT-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBXSQZOtDVv9j0gOGwqKmnGXKM3WBHhwtqe_YssO3batwhcsBWWSIKNPvJIfUc4PZAJK91dO57x1gtpCgwUgbqMM99wd62jl0t3_VC-MdZtJGchyyBwWdJh4Ru2W_gjax9KSh-byGjeMG8fOv9EM05v9oSw2J16uNbEqoay91uTJoXQnaYn9f9D-sbD3eG0g65jnsL29-SDHIXvqSKX7MCRd-7jmSd73LMLNGAb9315yMtqiFyJcqe4UO-c3ArifPAO7GNfvTYxX9aKsccJz0FqID-V2LstFLyK-f5p_-IfNnO8b_I12_Fz2FiorOpglxuLRb-NlJk6fz-wKtEYFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYibvvUs_wCEt22s0cJ7-gsmz3Hl0UBdWqDoTZvaUVtS5GBkskro4Nvfp67SpK9sq8_waKuSWPp31RfZe-OEc8plxyQITqVtoY4c3MH-nMPKUjstC5hYu0_i3pRFlXZPiRUOZvJ2Nq0CaLFZJXAaaWg5nmYKo9menZGVM24vOT8ZKLvnfA98CE_S_oq-kdxGKuSKCyQE0E5GsJYCwxW44MofzyliFFqgVqWHuSLY8CGX-TSKP7goYqvAyZlcNLYThR3el5xkg98exh5MryLbshRicSadj52U4Gsxb58muFlqXvcHsKmFl338Rhq0Im6cg_LlBXjaQaADc7vWmOxrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueam0ZPhZ2b800SygxOWY6mjEgt1qf8hjLG9DmkfwFmRrK6YLHLW6Nt_6JwYtzSmdX6h2Hm4qZvontZgaweoj168E0LDJpgmpcondBr8KS_Y_IiS3HaTHOMIlH3Kcah2h-Dt3W-qkpLtH2kQF8wZhaQqZRUScU10nC9n1nXLS-v7L7s246K5-7qHw_AAhXmlCvyy1VnnAFWW6MlgKuWAJGXFOQ4I6Ydd0QJRJeD1YSty-xdDfzc-Te6LkFxggGtrtQmN__YGKLO-KfDsvzq8_p2gBBR5ifp4WR3XeK1nKRrXK9HmLyr5IAruip23Y3h6BscRDe_va1syTCftS7qviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_wjcLQMKhqByC_VRs_h6mLMT_ClmCoM0o0KizGinGhz9DOJgIS-gPYBfdsQcdmwKm6Es-L7O4FZsT8QWvUtx8nAPFahoLzTw6zWYbpcOqh1kpNgJAcE2qwd7AaW8OtbLMiyHUvEkHuol8ghFnSB49DGOr27AtGQ0dWjQreZ8NoUFfMiqoE_53gCSacqLpK46TgaKALKCpS28rJAuljUD8QNX2BfnosPNKZQxLxXYGiGZTqDyzptuhEzMyqxsps7xT4dQMQ2BOZ1h5Tzy8fv4AKah4iYm-X22eTjrfM0xWLMBMpDojgClvxHKZPayj-Vn9HLVn0bq-1zi6_iKCBVzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN9uykwXmBczmrA7qX2T_c6Ixs6cYtD_iQgGLzhnwv24xGrrChFzANaAenFDsqB_ojr0xJgBVAZZPeQv00Eln3cpfyE-fXX7OQ17eQjDrhRQjhEMBFPO_NRCn37eMD_9Hxi7rxvq0GvOvPa5N5Y1LZzh9sAxl9UCuOsmnHDSp6PBR7bhN2kVypJi2dAgjjm817kao5_ML_E-Hrttoom8p37erSxRZXBuJ4s5H-n2A_v8BGMsFA4dP_fiqbXm2MjUh_hNblcrtoWjcMv-VMSgj96OY0YMgOkZFyEjlAI8gj4DfNGqpXaVaQC1wBosQNNqPpAt46m74DsIOFaAg_3Mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=wCKCWD_vFBzjz8fZYYLDrc5TY4tQFQYAuS1DcD3f4hzYETdiEvt7rkEZtNu6e4VfZRV3vwpaD3piRKXPSi5uBpSBXW6rBkWRWcBz1MD3h5uPCrGvG6P0O1bU2SNoEQGrdyib6YISePFLKzsXO2bVB-kqBLl8OMHRRaVjmlTZDi24LhJDGCvagB5m-QZT_bK9L5WQC2xWRk-MAoKQx49opwGc8-01BcaDkYipvynJyElnxbB88stia8Rhwq3XmgR-NgFcRuvT7Lco30ASFlQ2xQFhVHzfSxhljFQT7r8wPfrvz98Vc8N6o5TA4S9NY0scpTb75BSx_Vthm1MpZy3H9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=wCKCWD_vFBzjz8fZYYLDrc5TY4tQFQYAuS1DcD3f4hzYETdiEvt7rkEZtNu6e4VfZRV3vwpaD3piRKXPSi5uBpSBXW6rBkWRWcBz1MD3h5uPCrGvG6P0O1bU2SNoEQGrdyib6YISePFLKzsXO2bVB-kqBLl8OMHRRaVjmlTZDi24LhJDGCvagB5m-QZT_bK9L5WQC2xWRk-MAoKQx49opwGc8-01BcaDkYipvynJyElnxbB88stia8Rhwq3XmgR-NgFcRuvT7Lco30ASFlQ2xQFhVHzfSxhljFQT7r8wPfrvz98Vc8N6o5TA4S9NY0scpTb75BSx_Vthm1MpZy3H9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNBRd_7fwSOGnuhaGzdJvLDahDooAyUbnUxRhztGwUptcrM816h0cP8w_8nqbE0v3qci6DsJhzs-O3rhMwOsainUk0ystxD9EPoC67bXAL3j8ZEXpWLzGiQEwaCNfKOHpgEA8JMKpQQePGGcx8UdJlpZRoXjDLvm5parXlw0MXkyz1qsUG6iMIFQSqTVxLNF9X66OseV4gIzfkRRFjCMY8UNISQ55rZ4UeSugiwWXgvNsAVhE5C52OJRz9t-wpuADqgc8eW5MY8aKnpsdHOdFeStkof6HAeoKmZRdCv-7oGBuG7m0x6miPWIrZBZIec3OKFp5MxS3JDCZn7MeWloPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=rqHWKdR1mzA2JFmmVt_i_RQhdFXb-J9NZ0Q3Y4AtTqEBCahWnslzWwZLJuG15uUrWJ6wGoguYd1acsWILB26W693NvQ_f4ZTKtKq4BKpLhuI1koljwEXfH_sgIHYoj2wOocRIDLAJcoz_LLksuJoxS9o0mXg6AHYvQoYXG05pu4gfo9JE1CXyeoaikZbGGHf9u6-b3YlqP6z7QCgb6DLq90YAAsoUCpIsyDRnenCtQDlFd1Mcb3sdZI0h20Wd6OJE9B8nm3RjuKI3DULtOsQBN4pjzS9Tvu00DS2noDvAwDWgQ8qqnLGICyzgeEnxLsEZXSZYBEN2apXy4C6uXL9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=rqHWKdR1mzA2JFmmVt_i_RQhdFXb-J9NZ0Q3Y4AtTqEBCahWnslzWwZLJuG15uUrWJ6wGoguYd1acsWILB26W693NvQ_f4ZTKtKq4BKpLhuI1koljwEXfH_sgIHYoj2wOocRIDLAJcoz_LLksuJoxS9o0mXg6AHYvQoYXG05pu4gfo9JE1CXyeoaikZbGGHf9u6-b3YlqP6z7QCgb6DLq90YAAsoUCpIsyDRnenCtQDlFd1Mcb3sdZI0h20Wd6OJE9B8nm3RjuKI3DULtOsQBN4pjzS9Tvu00DS2noDvAwDWgQ8qqnLGICyzgeEnxLsEZXSZYBEN2apXy4C6uXL9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=SCZko7pXGlY5FWjZl5B8kZrHDmHHHlwqlN8cd-5ilKIc1SlMuWhvQuVvSeXS9FmTzEcek27NXpX_-JYd-5K_wU0Td2HVcTYPHF-N2HeY84RPIoBONaLDJ1oMh9_5-0Lk8g6G99xGnaTTCSNH1Fnr8YgGvPpaMctW2TIry3K-diH7KsIcNPQixZPSEhxKlPp-fvRD2nUKIyGmlAnO48c7lgYizpF1ESmKJ4iX4CiMsA0G7ufMrfOa-dM2mmtjPKkm5lind3Ga0MYhOsRCWjG4DS-q8tUds_czc-2ZWOofRDEYpSmaPjESQCD_du0WWQ46wsW8qL1el5gyFyEwumhlrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=SCZko7pXGlY5FWjZl5B8kZrHDmHHHlwqlN8cd-5ilKIc1SlMuWhvQuVvSeXS9FmTzEcek27NXpX_-JYd-5K_wU0Td2HVcTYPHF-N2HeY84RPIoBONaLDJ1oMh9_5-0Lk8g6G99xGnaTTCSNH1Fnr8YgGvPpaMctW2TIry3K-diH7KsIcNPQixZPSEhxKlPp-fvRD2nUKIyGmlAnO48c7lgYizpF1ESmKJ4iX4CiMsA0G7ufMrfOa-dM2mmtjPKkm5lind3Ga0MYhOsRCWjG4DS-q8tUds_czc-2ZWOofRDEYpSmaPjESQCD_du0WWQ46wsW8qL1el5gyFyEwumhlrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD_totQXUYMcGdLrky5pMHq1sMSZBBCkmVlPVHzy-s8GbZxUs8s9yp3W8HvN3AmiSR2Wbymg0b13jr0Ho3VTOoi2GQgIglX9s0fDeieipJsRQzTlc5tkiZO9OfmxWTRn1KW4pDI9sabiUp6gjk9eedtW0D_f0Iea7AkgyqlpUNPMVxAWirAB12_rf2SdrbvaKlyPK32L0xnbvBuylBLwB71jo84bsOUD4rOI3Q9e40Yu82CNcmt9RMBC-ZyvcfLg1QRWdI-aR0TJfynyQXpzq7k7pg2lKzbeMNMVdJji9Up8okiyh83-c3DXrl28yOj4Kdg8FBk8lRXkFNpg-hKZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=ciAnPoYG-CdqbkVwXIKsH_0man1l3jpwQgwrcz6az-kCFcZSJFLZGue12XZQxTcV8821ZGpzQTnNBoYucfNMCMjsRx_NQMHCAPiE-eqYhljW0GOYxsjvaqHPnT5zYOkDcnaUN7qaP6G4rxDLJpRIZyVDIp_a8GaSVw5Q-dj5SO6dmmLqiyTxCfxxPkcxzAovVn51A8dtisa_UPtdwbXkGJmNtShnJc92Z0EWv4hRXcQgY8eH_F8UWB9a2gmQveKM1PQqLU8dInlSTSfHhtR-IKXeOsHRzWZyyPLVd97Lc1jGF-hr-0jfGvFqIAsclYpcWb_fllrTfQGHKRTbsKuyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=ciAnPoYG-CdqbkVwXIKsH_0man1l3jpwQgwrcz6az-kCFcZSJFLZGue12XZQxTcV8821ZGpzQTnNBoYucfNMCMjsRx_NQMHCAPiE-eqYhljW0GOYxsjvaqHPnT5zYOkDcnaUN7qaP6G4rxDLJpRIZyVDIp_a8GaSVw5Q-dj5SO6dmmLqiyTxCfxxPkcxzAovVn51A8dtisa_UPtdwbXkGJmNtShnJc92Z0EWv4hRXcQgY8eH_F8UWB9a2gmQveKM1PQqLU8dInlSTSfHhtR-IKXeOsHRzWZyyPLVd97Lc1jGF-hr-0jfGvFqIAsclYpcWb_fllrTfQGHKRTbsKuyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTDg1DyPsPfc8YY0jrbkjeK4IGU-HLwZpD2RPJbZ3gGB0aqFrFGc6_Wo0sJwKt95FcMMpVbTQmqZRdwGKjOj2zBAEebgccsFiI87eadmtKHFN8Cl2gP2-GeMUq4Rh_6dQncb_me8SwkjxrNZZ-IEBXm9dQSDHmNqBjIaXnuYGDQ-AWjjlzR3FpmuoLpP09ydf1tCaVvCiSpu83awpgxkx15y585z-oj5BLRAEu_q_pWvuwOX0Q1E5vpblzbYw40jk5HGI8Ps3SYPVlRzvJ2-Imj4t0bIvppTxSq_yky3StabesNv-jVrqoJdRGsk7QQl_xg8Gro59EBONzt9jzj9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPAhEqdpCukSlJWNAci8xdDUebRazo51mTIRimFAIN5vOxi0fpEEXqa5EchmxxIFUX85vVs5fb4oEFcCCL2aMiCp-CjMfVwyQOZI1i78shEqWQghGhkAx_Tg1qQBDuR1owyHFiMWGgcU-NQtuGq8g9W8TXKzbK4Dorke3qY3W0OFV2O6ofdNGmrc7ods6RLH0_7n9gY9OsyDKNqT4ViLKPHEFi_P8BlgpBy3Kk0UBo6AkvcGJNnp-6F1QAMrl0g1iLoBJZPMb_w8Q2GhsPYqvdmByUk95sAdoeJ0VkJnKvrdbNbwiPMms032ltER7hOLGEB8IWxu4EoXf1LCxZkmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYs6xh5otkbXISuEYGzC5Ohh0BIrhEl9cdDoemfGC6XbPSd8k23JJ1ZBy4lDrgfyZCQxZWnDHUAKy_iamtKctAavkBHXNflRr532rtDUFpAxcNJsyUwtqG1NSz0974dksfTv9JxMFoqzpSU4Wapg5b5g6NJE_SbVPM17JGACyFmr0QyVbNuaIKHDD7E2A5gHeyampd6hu-KpuC87XQj-lwdk24jZONkCe2DPzaegbAieUbmRUza6x0KZs4YQaSo8d7PLpIKOGnGuh-tVDXMIj9cdFtVk0aNXqJkekLs_aOkdj3oCQuOXzRkbqyN4IqrU9q9fFLBueQ6g8Mhs9knh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT1oHsDGxPKq5dcQGW298-95OF1rBy68Tie8jGuuLNJFxks9utXTfKfttZz7F11UgkX4euLuWJ9c44YK2XhyEXGzrzsBWHXmlqNoxmwYNLvrnBmdSYfqKH7MFI64ONpvuGOAMmPZhnqUcNk464xdjEclOvPJc14HtFxADWCpDAWio4D5ViHvx_vuir11MdUS7OT4U2P3vNHf_8LBEm1TfSWKX2VExp6J-SFVnwQC_uWjUD76R85MHTt_780hcxeTFgdUnQMuFJ_QY4FOtM5l2x4dtg2WAGcSsNkTrsE4a6lGz7-0BGK9dwBIkOvnwyCI43LEHoMBTvoRmgHHj1MhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5D0QPtex2FPm_0RCoE0w1BC_Gda73JcnzK0BQzUEv30XHc8Rwury_kRPyJGa9OZ-_PMWtagainCXSeg2djSZwsLfb8RDofyvsl4UfDVdItzvo2M0NDnU_qsBQ5b5wLW_iuQnloSyYamj2d9HFnHnsxci_9PJ9iyPwScRvvs5eGEfWYlsdzGkYFCsyKmeAzIIlcD3vmVWnxpCIvtlpz1BcunzgIUD6ndSlnkQJpFG0kyUqV2q7mN8LIk4v9ZV18rZBFfuh8ikOdzO0nZZZpGYzhOWyqjbwZQIWftfD4_Det45lJ2lSJBBKobdVdzFjKRc3z00da5c46b4R16UPXrpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crkoXUZMJiuxXQHMKNET6jdczZjx0x_67jVzbX07DgLdM3qtkdvsKhn9oEGLKmKZaY3EwOTzA26t1x8qosm9lAb8ZOEpPfLHCLcY7NQgNb67y5zhTkZlJwxukjriKvBGWQ1h_RpeAyyaqzZn4Ms08VmJf7TVSFM6OvqgQ088ddDCSS5YccpZ0sflKilR5QabEE_pZQlUdXMYdfGZXhlHpEdPEYRXZaq7Gp0S90P0ut3t8ceETxHYqNYA7gbm3KGqkfipEHxH1anI7uoqK2gcT5lhl5QXC4CedX0L_x1NIY6gW4UMJ4cUM1_yVPFq3Jv_DBPiHiCK4v37BFkOFkZNLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
