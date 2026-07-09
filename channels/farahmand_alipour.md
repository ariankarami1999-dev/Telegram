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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس و العربیه به نقل از منابع خود می گویند امریکا امشب حمله ای را به خاک ایران انجام نداده است .
ممکن است حملات توسط کشور ثالثی انجام شده باشد یا صدای شلیک موشک های ضد کشتی ایرانی به سمت اهدافی در دریا باشد .
یک مقام آمریکایی هم همین موضوع را به سی‌ان‌ان گفته.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farahmand_alipour/5987" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farahmand_alipour/5986" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farahmand_alipour/5985" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG7p1iTApU8POpzzXFlUrTr0X1yZwmkgDED3tUJWhV_i-_jMW-SOCPM2P4F9Jd3nhZDkHvJYrketdp_1svGQIJwvTVbTFVJLD1ujWu7JQmPS3rMgdtnnibnwqkTDAFFK7gnbng8e8uJ_NTwuz4ueQDuEGIY9RhhyADsjC-YtXZG9amek3d-JHSVD_3P8C3V32NKyZVf4AlUgojymZMyhR36NEsEzauGIAkVSGqsOkI-6041CllZdWgQFu9x0G_22z0Cugsub_NrsZPMurOeqFzkCpAoZV2HaND_sUpfWbSbwcS0NY02_HFbOsvtdsmpLxM-Uve7oMgCRtr_0Qy9_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده سازی قبر خامنه‌ای در مشهد همزمان با حملات آمریکا به جنوب.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farahmand_alipour/5984" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5983" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
گزارش چندین انفجار بر اثر حملات آمریکا به بندر چابهار،  انفجار در کنارک، گزارش فعال شدن رادار در بوشهر</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5982" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏پر از خون دو دیده پر از کینه سر…
‏شش‌ماه از کشتار دی‌ماه گذشت.
🖤</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5981" target="_blank">📅 21:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUD9wU7-hVaeg9IOUTIckMwFDkbt3kh5NfRMt1ENq_iAc9yY4l1FEKWlMNFWWrgtn3RfZAEMDh_H61Y-Enso851R5MvpXCcZhojogz6EFN3aq-OmaU5frwqwQmJ3oHl0SwTA-R_RrvfmX97OqCylYP-IaSFVtEiQjaZkfIsU7h3rkXQewqQ1Oi1bRVWREakvhd-Q4OcPiSqOoQha4Nv-ZlEBYgwNZVyDDpi8KQzvrxC5xMqsiP-24shU8Ib5XIKIypJZc9SNQo-o4cRJqiaz7D-WN9L7akJILv3KkN1euT8HWNz4cw9I-cWkV-gOCuQjZB8QEDH2XEu7T4dw1gaO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=NXtPonxBGuXY9jyfEGkXafR7rHkkBt8MgUUkYzWeNRbThahamPrTPoxps0N04ihfnEBtD-X3xL5pV6rULNnEWEY7BVzKnQW5I1z-GHvT2TWKEzJfMx87cikmbo7fRLTPhsX1JTs57NkHo6LPjdMvDwWQEHpPS64hTe8oZ4buOEjEcBwpe_gtwBLM_iHxDzS921B6y2k37CSGclrWCrWJKM8w0SroZOO_0WWf9Psx9f5quoFR6vry4aiQGJhRvz8D1deie6KjPYqDpHFlP598ofuSKILQEiBkS_TQVwYRGSDpf1G2lzv4y2Ul5b4HXJklicwiwU8P4rlZc0uYjTfcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=NXtPonxBGuXY9jyfEGkXafR7rHkkBt8MgUUkYzWeNRbThahamPrTPoxps0N04ihfnEBtD-X3xL5pV6rULNnEWEY7BVzKnQW5I1z-GHvT2TWKEzJfMx87cikmbo7fRLTPhsX1JTs57NkHo6LPjdMvDwWQEHpPS64hTe8oZ4buOEjEcBwpe_gtwBLM_iHxDzS921B6y2k37CSGclrWCrWJKM8w0SroZOO_0WWf9Psx9f5quoFR6vry4aiQGJhRvz8D1deie6KjPYqDpHFlP598ofuSKILQEiBkS_TQVwYRGSDpf1G2lzv4y2Ul5b4HXJklicwiwU8P4rlZc0uYjTfcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=pZS-nPHPbeKg0MEVQyQ4WJapS33I28raohJgajNUTycCTKeHcU8ZSy3x8oqQYC_veaWKQGNQJrajGuMJAGvtTOsgJ6QLh1FE9YgDl4-TEH0eIBCTRZyrkTdVnfoQFKWJDbsas8IfRaTkDYSs7Ye1kmP8S6ia47szsdQHOtSOl7DG0WOBPSbaA8xhDOuHxQ7mVQktLyHxOXrwrKBjlyk0xWhMgfldIObT_GZ_H-kf_CadL8t5m-vdnXDcgIygR-1NAsPIM36FsgdKAPEZVKQ4v3xaWTBtp9jq4r5OfaWzeZoVpG58dxrRaukH6JqyYaQfawyW4or8Dti5xFIKt7wLJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=pZS-nPHPbeKg0MEVQyQ4WJapS33I28raohJgajNUTycCTKeHcU8ZSy3x8oqQYC_veaWKQGNQJrajGuMJAGvtTOsgJ6QLh1FE9YgDl4-TEH0eIBCTRZyrkTdVnfoQFKWJDbsas8IfRaTkDYSs7Ye1kmP8S6ia47szsdQHOtSOl7DG0WOBPSbaA8xhDOuHxQ7mVQktLyHxOXrwrKBjlyk0xWhMgfldIObT_GZ_H-kf_CadL8t5m-vdnXDcgIygR-1NAsPIM36FsgdKAPEZVKQ4v3xaWTBtp9jq4r5OfaWzeZoVpG58dxrRaukH6JqyYaQfawyW4or8Dti5xFIKt7wLJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=RvUJb8CSOpn7p6aW_Wv1GeURI2nRSETe9U7xiH_SZL03dYms60skcLudXQQm1yRvVgzPbgZ58nhc6bMxaU0wPkEVmlpBBjlYmEzr638tlZ4nmEr1DEUgQLK6M4cAIuGbMADdGNJ9RhAg5ShbNU3rLGdSJL9ixQqoDn-nc2pBZHf-KKJ6qOYBPQLVblmVq7seGJTRNyfcIjPfAPIO8Nn4EkJM97QxKsVXHQMs9dvQMYZkhZOnmERKXWOOuEH-1ThE2h0P5QFl6Qi4TTbumnuR8bdyCTJ-YYgdiRPp899gb7suK54jCoYZz5e9ejWkve7-UHcx7UMG8QgpJXrxEEwIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=RvUJb8CSOpn7p6aW_Wv1GeURI2nRSETe9U7xiH_SZL03dYms60skcLudXQQm1yRvVgzPbgZ58nhc6bMxaU0wPkEVmlpBBjlYmEzr638tlZ4nmEr1DEUgQLK6M4cAIuGbMADdGNJ9RhAg5ShbNU3rLGdSJL9ixQqoDn-nc2pBZHf-KKJ6qOYBPQLVblmVq7seGJTRNyfcIjPfAPIO8Nn4EkJM97QxKsVXHQMs9dvQMYZkhZOnmERKXWOOuEH-1ThE2h0P5QFl6Qi4TTbumnuR8bdyCTJ-YYgdiRPp899gb7suK54jCoYZz5e9ejWkve7-UHcx7UMG8QgpJXrxEEwIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5IkZpW5k6BdN4KHMLIqInX-u1IJAUrGYsK3z2nowxcw8zDtaxDOyjygbEwH2VKIsLti3SlXsetNHepzlipZ6vQOraohJ7oZyhmNpYI5TT2JNVk7t0LyQm14ZJuZl6yJb9Dayu1xzdLx2LCKby_MRClr6OHTCHN3HwYpzug2ruEkNrlvY0ctggrrx0DzE0eCLincPdflWVPTv7Vgp24Nv9gMH-pwpcJVldOVogI9CoPmhuciv25yobLloQtJBKfPWZ2kUsM4FLGQP26e2cu_EGjEJWp3OYUjqspYR9TfxYyFdP6vtngRP9Z9BChswIIiZ4GLjo_o6Ab_k_5WWjrZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=febwc604OluHQqMINuUUfPQbFD0PZoJ39pmTpv27GUmYmnCC1Qw6VtS3eA0kXUAmWD_5XTIQXiPvGpVve0PZIlpwSLXJWrArfMph7QHoWgP8eOixqaeFitKBtXmiZVk4pBkuxCtIFvFGnit0cMrm-imcP9nhJXe9MeunFRSRPA2s1iAwUU5akE8VSghe4P2vVSMpolsCApDEAUU2A-yQYIwt3YxmqwAaDmZQkaBFRtptm2h66HHRIQzIsyUoPqAkERwxuHeMnp8HMHwW4mqQKcH9ej-JbmjHjzbSjcpRVeW3nPXzm-1KTp0ZzVXg6FeHmT4sJ3OpDYyMEqvjsp7z8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=febwc604OluHQqMINuUUfPQbFD0PZoJ39pmTpv27GUmYmnCC1Qw6VtS3eA0kXUAmWD_5XTIQXiPvGpVve0PZIlpwSLXJWrArfMph7QHoWgP8eOixqaeFitKBtXmiZVk4pBkuxCtIFvFGnit0cMrm-imcP9nhJXe9MeunFRSRPA2s1iAwUU5akE8VSghe4P2vVSMpolsCApDEAUU2A-yQYIwt3YxmqwAaDmZQkaBFRtptm2h66HHRIQzIsyUoPqAkERwxuHeMnp8HMHwW4mqQKcH9ej-JbmjHjzbSjcpRVeW3nPXzm-1KTp0ZzVXg6FeHmT4sJ3OpDYyMEqvjsp7z8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=KjDaZrMqkWnuGGhU7ivq0JQRuYtrhccKcPr_tJKPsyqSkM5uxBqFNiUt98wMUnW3qsAlqJftoJxKfBvnJwdNjupji8s-3Zg7AkzdOGPLBugM9ZsHWe6X_j-Nca5n1Xw8Q7tubAwBUQ1sAEFHnDJLnELh16yQFVjN7bEuxYvET7r6kk5NkLE_qtfWPprs6cpTii3JbxM7C7JUwRfj35qbzq69VNOdvy4Kt-VXQy9qPWqYlPIziG1rCjawRGybxO9RXDLiW6xBQrBK3v0M8EkrFHDGSJ1jFM1FIRSB3rd7vIOjyTXfOm_OlFYicJ331DV-N2Nsm-kgGGQCzfVgLbgZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=KjDaZrMqkWnuGGhU7ivq0JQRuYtrhccKcPr_tJKPsyqSkM5uxBqFNiUt98wMUnW3qsAlqJftoJxKfBvnJwdNjupji8s-3Zg7AkzdOGPLBugM9ZsHWe6X_j-Nca5n1Xw8Q7tubAwBUQ1sAEFHnDJLnELh16yQFVjN7bEuxYvET7r6kk5NkLE_qtfWPprs6cpTii3JbxM7C7JUwRfj35qbzq69VNOdvy4Kt-VXQy9qPWqYlPIziG1rCjawRGybxO9RXDLiW6xBQrBK3v0M8EkrFHDGSJ1jFM1FIRSB3rd7vIOjyTXfOm_OlFYicJ331DV-N2Nsm-kgGGQCzfVgLbgZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l53BubM6M2tCJV4QnSjP9wTvMUjaDPwRL1MLF2hn0wWJgGzm38ZrMpyJeBL2pxwsimqyR2LSHQkQ-Lv1q2zhEA1NtVUg6pT1rd_dSIdvEdRe-lCfGWw7kuGG7pA5_FmI1EvPv4rnaiiMS64w7WX0Ba4HyBV1W7QEKn-YPsc4nntRpWDIVMKT4M6hcGmjPBa7FdYS2mcHDvC8J4HsGQq_ardNCHAxtU95rWuUtYj9ropjlnKJ3vsJsVOs5Qt6GWVhCWCKGniRb2tdmhw0eJK2SpYExzQgskHchdkCOIyEdR4IQxmJU4blVKj0ZicPeY_eq4CKp5ab82l8LBopn0qeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=bpN3u3nJtTwm10Walx8rvDYp6SfHsVF7LeRciMTx8I3T01hifGXf0TdvlykmcDJ5A208pZBBu94-j5ZfwPWEAFGHl0v79R1pSNJVkjKGwU52Hq9wXmqrN0gXQk_UQseSwHo0EHRDZRZFaxJHhZFH8EAr3k4W7_2nsV1Ecvaz54yka20n8pBHL69_27CGymdyEQcR-ACG3JxskJspRRk6Nm5kG4xBdYO1xGCDzV-M6T95UqeUmqarv4WQVL6hM7IS1m7-b5ANZZPafeBfVW7GZ9vv5MUj1iinzDUzX78fOEasDpwukb6kLXCeDyO3pLsOOoucvM6JxssAqQgJYaBGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=bpN3u3nJtTwm10Walx8rvDYp6SfHsVF7LeRciMTx8I3T01hifGXf0TdvlykmcDJ5A208pZBBu94-j5ZfwPWEAFGHl0v79R1pSNJVkjKGwU52Hq9wXmqrN0gXQk_UQseSwHo0EHRDZRZFaxJHhZFH8EAr3k4W7_2nsV1Ecvaz54yka20n8pBHL69_27CGymdyEQcR-ACG3JxskJspRRk6Nm5kG4xBdYO1xGCDzV-M6T95UqeUmqarv4WQVL6hM7IS1m7-b5ANZZPafeBfVW7GZ9vv5MUj1iinzDUzX78fOEasDpwukb6kLXCeDyO3pLsOOoucvM6JxssAqQgJYaBGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWalY5INqNveCwdmJQkgt4OMzOPjJVql2sd2qZiFCCwdrJR3efnuLVZacfF7EM5G284ZziWRzwzSTNY2vKSusD0IB0SutJjbtWV98KPrHK-2ak7gJL0KjfooqBqugd6MtCexB2yH_2qgXHjOzLfDJ2NXQMOIt0CPTB8-DSXUxcE4Ofr8i4YWNZyJim7wqSFf4bCREi5H-5p2HfPAkSL6YeMtGy0y0bLVu9AY_iR4mus1GHc_lAbU8SZR8mc--E2pHBwNDghbsxrZcB54AiJ4Kf9ufUOLdPbdMDj-fsMaSSSU1CSBfb4jd2o9xH5Ugf4m1zUgJI1OjFBzBVbrXVSdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=Mdix2qlNVvdj1FdQZjJRrWJU0A4RbXQMUg3-zj2zcBzqFUeo2q0R-lB8645yr1nTig44WHI-YEpe_pZpdWi9wtkEXwsMfRxz_GlVk_vc2HP3WqREXTBerxeF_zkvhWe6KP11mctUpyKkJP6FgSOdTjPyHsla4a_hjjzJhz3j7AjuZgHZjlf14gsXutq64e67elxl67rZROzOd9vLDShtHGbwBEDNtI4gvvHoGbLTR6gHjY_pKvQ44gL_ZoD1L1UQhQQRYeIJbIadSOiBWVlaD3eE30q6mXnPc4meDCguvqBRN9NohU9iLr3JwxMs6GKpL4vpy-g0eP5smaeW3cMBhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=Mdix2qlNVvdj1FdQZjJRrWJU0A4RbXQMUg3-zj2zcBzqFUeo2q0R-lB8645yr1nTig44WHI-YEpe_pZpdWi9wtkEXwsMfRxz_GlVk_vc2HP3WqREXTBerxeF_zkvhWe6KP11mctUpyKkJP6FgSOdTjPyHsla4a_hjjzJhz3j7AjuZgHZjlf14gsXutq64e67elxl67rZROzOd9vLDShtHGbwBEDNtI4gvvHoGbLTR6gHjY_pKvQ44gL_ZoD1L1UQhQQRYeIJbIadSOiBWVlaD3eE30q6mXnPc4meDCguvqBRN9NohU9iLr3JwxMs6GKpL4vpy-g0eP5smaeW3cMBhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxoDFZLRDiR9e8YSY3QwwTXdARhB139F5hug9pVp4TILSeXCPSJdvMMEWm9w3fwo71KTvR0A3RGDU3oeSDL8br-yedjfOD1L8vvTrGqr7Zcn95Rfc8S0nJv_5PWDetUTXapQvWmkD_CYfUKXVkmRpkJ5_UXT9FrC8vlksGqwVg05wfXuiQOWDnJWAffj9Z_o1106wMSfFUmZCfP06GR3JwDSOFlpyk2-foFkkY5NvzVht69lQ2Gjv1AbRojXDKnCMV5Fw-aqHBKqFFbclKXfXiCMsJFvutBQEgmcjDKtPHXCJTaYrm-Kp5tv10fpdm5JuKkaQXvMKaoA9IuaXvxOsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=YUL697z2rAIayO_0cHW6a557J8x3JRVtYqDL2BxuDjFpjXBR3BjZ7swAKroqv9vorcAHRZWSuGGTFTEbetzPnjfQ_lOBpVMsLb92o1Dp2KSvybTUTQolndNJUsCNDGbTjXr4PutD_F-rNd8znbAXSRjA7BunJyQuIoo1cKZrCmRvMmWiEHSK56pbu2Q-c9xM9yWZ2lY8fU4KkD7835U9jtPENYrpHd99WLp8vcUYT2FjMOoZe1fpJ-WzRxIQx3MbyqVCeonnjdyTFcMco3Qas8SPx637QsH_wI8WWt3nwn61mMswvQK2qtcCj1anzjyY-28zLa_X-CrINc3xe674Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=YUL697z2rAIayO_0cHW6a557J8x3JRVtYqDL2BxuDjFpjXBR3BjZ7swAKroqv9vorcAHRZWSuGGTFTEbetzPnjfQ_lOBpVMsLb92o1Dp2KSvybTUTQolndNJUsCNDGbTjXr4PutD_F-rNd8znbAXSRjA7BunJyQuIoo1cKZrCmRvMmWiEHSK56pbu2Q-c9xM9yWZ2lY8fU4KkD7835U9jtPENYrpHd99WLp8vcUYT2FjMOoZe1fpJ-WzRxIQx3MbyqVCeonnjdyTFcMco3Qas8SPx637QsH_wI8WWt3nwn61mMswvQK2qtcCj1anzjyY-28zLa_X-CrINc3xe674Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqhMeOyJxvez5nWqceFZ8YNf5-vekHeXXCTOuCXq-am-6B8VLeQTapXGTyzIAvLEtk2XF-0dsicpWZj_2wAYIF3OwEnjHa3G30tG0eu5qc4Y4Nk9yFenqdQd7NDJufxuvDksjoBENqUQG8OQ_AxXfBrAatGoGa0IBdPzOpaQwufGI-otbJBxCs3Q5A12aBjOAk9Ruurzlippk3yY6-8uDwHeAc2KlQDJS2ZNx0S5OPBetp-nG7oV8jBfmvxbKu-PWMGyhLftjpI2hgOoXljNGkAILObw6huOkDegUS9d9GIDCcPxUgFkKTxwOC3Q1VjX1DcgEoAT97UmMtlMV4ZjDdFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqhMeOyJxvez5nWqceFZ8YNf5-vekHeXXCTOuCXq-am-6B8VLeQTapXGTyzIAvLEtk2XF-0dsicpWZj_2wAYIF3OwEnjHa3G30tG0eu5qc4Y4Nk9yFenqdQd7NDJufxuvDksjoBENqUQG8OQ_AxXfBrAatGoGa0IBdPzOpaQwufGI-otbJBxCs3Q5A12aBjOAk9Ruurzlippk3yY6-8uDwHeAc2KlQDJS2ZNx0S5OPBetp-nG7oV8jBfmvxbKu-PWMGyhLftjpI2hgOoXljNGkAILObw6huOkDegUS9d9GIDCcPxUgFkKTxwOC3Q1VjX1DcgEoAT97UmMtlMV4ZjDdFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trdUetxE5CeGpuN2DyVt9StaY3IHyAupG_7bsjjvjN6JnSw4K6nxgcL1Vjv483xilW4E-y1Bu5dea0sts_Q6hrDnU6uF_x-KBeTmoVXetwcwZk37Xg2C1hATgdTs4AqIJQE3DpfFE3SXFrW-zhUqW6eB0SdEO9tjOtJQkkY-Cz9Xe1xGMmpRJR7RGiJgsuwVCY0glYOrDza-OV0MCwzptp0Zxqp_9E07i3HNcDz5fACPHJuMv0mf4A2TPLVbOw4ZI7CGG2tC0_9ZjGSUm1z-gtRLeNaUtE7kcAYRDbSa8CC1m9v-tWT_4NBJ2FNBopUt_QGmLfTGwA_p8NBy7RaT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=FyNqrnfVcRGSV6aNGlkglo_JuGhEmM3vkUZJrJ2N6_-5sZ_VWpWMhyLCRLeVIhaUNcJMrwLoxm41F6fK94hnLy4EOXxT9pYHoLJcCUpbg3Pa5jyfmbYuO_ke5QibvNMwZ-8tHs9l_27VI48FzcPltjN0-mTl3I1_RiXa2vmeQAcg6iJXHRN6i2u0f0_w_zZM9-yfreYyGJucuAktHHJ9naO71esIq0hbNzc2FKjQx9Mm0Yo_UDksED455uhVRTWkD9JMc_xT9lCcHN3IykeGgItkAWWa34werYHv8VCYFSQammWj7YoAF4EU9rleFwfYPGSWXghfl2pcCdI25bN5dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=FyNqrnfVcRGSV6aNGlkglo_JuGhEmM3vkUZJrJ2N6_-5sZ_VWpWMhyLCRLeVIhaUNcJMrwLoxm41F6fK94hnLy4EOXxT9pYHoLJcCUpbg3Pa5jyfmbYuO_ke5QibvNMwZ-8tHs9l_27VI48FzcPltjN0-mTl3I1_RiXa2vmeQAcg6iJXHRN6i2u0f0_w_zZM9-yfreYyGJucuAktHHJ9naO71esIq0hbNzc2FKjQx9Mm0Yo_UDksED455uhVRTWkD9JMc_xT9lCcHN3IykeGgItkAWWa34werYHv8VCYFSQammWj7YoAF4EU9rleFwfYPGSWXghfl2pcCdI25bN5dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=o_3iRFgwycHFOGY2mG8pkS7lDFY8xLVQhAxYqBHlY8xCAG-w6r2sE4gqrXYwcAzpKmjmKdX3EVboisleqp_P_nA9h-9yy_zGLjb-HlQJQtARJTTO7SNjiO_frc4NxJlRHI-QcX1GhXBGDLPCaC-91xLoNyeNNkN_a0tluCQ5J95yxctgPsjtltl981KvOcGsAMa-joJptNZcDepp5q4XeZ-yxCWzaK796sa1vs3MfxyVcZa_9R6v9TGIujoRQeq31BGF4J1_2f4HL9O2nXrtq_VrF0vv6Svh6Yd_ZdYJyMbItqpTnAmQdEFYkfMa2k0XBDCFwjX67HNdNTjeHImgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=o_3iRFgwycHFOGY2mG8pkS7lDFY8xLVQhAxYqBHlY8xCAG-w6r2sE4gqrXYwcAzpKmjmKdX3EVboisleqp_P_nA9h-9yy_zGLjb-HlQJQtARJTTO7SNjiO_frc4NxJlRHI-QcX1GhXBGDLPCaC-91xLoNyeNNkN_a0tluCQ5J95yxctgPsjtltl981KvOcGsAMa-joJptNZcDepp5q4XeZ-yxCWzaK796sa1vs3MfxyVcZa_9R6v9TGIujoRQeq31BGF4J1_2f4HL9O2nXrtq_VrF0vv6Svh6Yd_ZdYJyMbItqpTnAmQdEFYkfMa2k0XBDCFwjX67HNdNTjeHImgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz3K86AmDE3lT2buB4caedvCLTVgEKuHpXoEsxlmwufS_SgX8I-NhOCrjJnPWe8y4aKaj2skEWNY4a2KGAahh6W06UO4IlLM8Ug9t1VAs80qF3k0p_pikY5YuFwMT4HD16w84rl-v8laA7P0qE7DXvrjqLiqg_3zLEX-DUVefRZTkcO3Z6ZVmclVQw2-y1YQvVLcZPk1M-Vv65VghsNfMUWq9VOoB3QSMXX4SDNmqyBSwRw13U_ULqSG7pnL9xubXiTts0L3Me8Omc9J5DJVEuflgz0lH-ye4F9mWoiknrgeg-IsH0Gfc8irjgGuKMG2JKXZPGh_FLbEmM5v78m8Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=kXlgZUmNiP1hh-X5QypJz45rZcO1ltk21huDTQKHGHwaejrwtNRDOwYJA80a_XOLOwDxtoqJOlF7tQ6xCUfZ-ykwCYe9U4EhJuNAtzqnXt9mrIX9GHrWac9wp5v0aOni11HZfjnvkp7Sy3szvwyMxzEOFjcozmAY8iVK6JOb0Zxpj62dCZs_FcM5gc3EMRU2o8RgzSfchge16R7Lxdc90mhXn36b9YcZcSXPCKNjIx1VPJXXctiWfJQe3sMi4TG_bJw0uAN0NpCwkD7BfkCHZF4fkjOIohHgR-F0YzcfHgAXWANLeYkVzgH8JLJ4qEKWYbHZTP80Jr-s4QflKpb_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=kXlgZUmNiP1hh-X5QypJz45rZcO1ltk21huDTQKHGHwaejrwtNRDOwYJA80a_XOLOwDxtoqJOlF7tQ6xCUfZ-ykwCYe9U4EhJuNAtzqnXt9mrIX9GHrWac9wp5v0aOni11HZfjnvkp7Sy3szvwyMxzEOFjcozmAY8iVK6JOb0Zxpj62dCZs_FcM5gc3EMRU2o8RgzSfchge16R7Lxdc90mhXn36b9YcZcSXPCKNjIx1VPJXXctiWfJQe3sMi4TG_bJw0uAN0NpCwkD7BfkCHZF4fkjOIohHgR-F0YzcfHgAXWANLeYkVzgH8JLJ4qEKWYbHZTP80Jr-s4QflKpb_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=PqyVegU8CRbgEoGRq8sC1QOAXWNQwPKTuUXYhys6-_SlfsuhwfBxcgyztwn44lodkRxoMkEkC-1Lv-M4fQ-qVoGMg-fVVOXgey9q9RsGz9kMdgrdEJJhNMZ1hSZaHzct8tH5VfQyvOFZboBPWeMNj_qX5KZBQ4ZBGbSdt6Kr-_QpHWL0ldt2jwbiRENq7_jmVL8_81fhPqnvOeTxI870Oro_yPOYbAz8upLfSoB6vg-doiPS3ZkDJoW0D0h_WkGd5th-kuB7UYX237QnBKycuBadJMC-FbDxhc4TRUzsW8Grlh0Y6fSiatt-ojrAwhAqrnbrrD1omKlmzkuDKDS9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=PqyVegU8CRbgEoGRq8sC1QOAXWNQwPKTuUXYhys6-_SlfsuhwfBxcgyztwn44lodkRxoMkEkC-1Lv-M4fQ-qVoGMg-fVVOXgey9q9RsGz9kMdgrdEJJhNMZ1hSZaHzct8tH5VfQyvOFZboBPWeMNj_qX5KZBQ4ZBGbSdt6Kr-_QpHWL0ldt2jwbiRENq7_jmVL8_81fhPqnvOeTxI870Oro_yPOYbAz8upLfSoB6vg-doiPS3ZkDJoW0D0h_WkGd5th-kuB7UYX237QnBKycuBadJMC-FbDxhc4TRUzsW8Grlh0Y6fSiatt-ojrAwhAqrnbrrD1omKlmzkuDKDS9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=dzvL7Ivb3_QFGgpIjRUlkVx0iT0qeVVacujHKqrMS9_vkzmvETJrCO56mSHDZIiRJHElYuU-UOfcBtGrUU6Rdi2JhtDvLZDp2eum3Gt8r_hC-MiGeppRcY4rZ2M_KEpOG0OOZjxSFUwNGz6GQ3JcfD9RWLCeRLIJR1VFUddgI_4QKpW4uS7LQ6F38xVqVvUseO0uoYrkAVM3-S4X8IvbVdglv0wFJ5K_froU1BukaV9WMZ6oWdkNisMPcPc24Lw86WlPqEEZwYuEW-3RsCK8hVRHhM4t8ascr3yVigbgsFSRaptZVvHWR0CsWa5s_mEmTpZLMdAg1pWFoIu-mQ487Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=dzvL7Ivb3_QFGgpIjRUlkVx0iT0qeVVacujHKqrMS9_vkzmvETJrCO56mSHDZIiRJHElYuU-UOfcBtGrUU6Rdi2JhtDvLZDp2eum3Gt8r_hC-MiGeppRcY4rZ2M_KEpOG0OOZjxSFUwNGz6GQ3JcfD9RWLCeRLIJR1VFUddgI_4QKpW4uS7LQ6F38xVqVvUseO0uoYrkAVM3-S4X8IvbVdglv0wFJ5K_froU1BukaV9WMZ6oWdkNisMPcPc24Lw86WlPqEEZwYuEW-3RsCK8hVRHhM4t8ascr3yVigbgsFSRaptZVvHWR0CsWa5s_mEmTpZLMdAg1pWFoIu-mQ487Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=CsidQ_-6sVnOxGQpXIUO_Fsf-Cd9XxPQoR8wQuEi_pgmUUt9feh2tASTcJkD5RPKHdKnWxGFIngmFEOh3TeEFLW2htLOJZ81hQ7Yw2p6WPO294HIM5QfPxfE5UIaatdL4sCsjxY18bJNrNtBjuka_qzvebJK-owRgMKvTRUEVEChb4CT-ESfbhFTfAF_Rqum8fS-MAYW_-lLbU8BBNStSHa9h0fCdIIlGw2Dyk493ndX3co1PDtTca8mMaBNc8foKa97gHOjB1I3I6ckiwZw3uR-NuQ6BFM_x4uW8P5xpcV_vOgiTStQnGQaetzPK8pVwALjANBESeDHSl4TuxRKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=CsidQ_-6sVnOxGQpXIUO_Fsf-Cd9XxPQoR8wQuEi_pgmUUt9feh2tASTcJkD5RPKHdKnWxGFIngmFEOh3TeEFLW2htLOJZ81hQ7Yw2p6WPO294HIM5QfPxfE5UIaatdL4sCsjxY18bJNrNtBjuka_qzvebJK-owRgMKvTRUEVEChb4CT-ESfbhFTfAF_Rqum8fS-MAYW_-lLbU8BBNStSHa9h0fCdIIlGw2Dyk493ndX3co1PDtTca8mMaBNc8foKa97gHOjB1I3I6ckiwZw3uR-NuQ6BFM_x4uW8P5xpcV_vOgiTStQnGQaetzPK8pVwALjANBESeDHSl4TuxRKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDvGNGKb91b8yzAsmgaYl8_WKaUvYC9CYO0JvZxvXiFLLE7KqkzM4hlBsnjMw5-cW6MOPzsbQZ7uM5QuawztkbHMFP-fGdVbBpEJ7y0ZfTgfYlQRzf4DcJyngsq9g5wAH8cRBoL9N_y6eihsowF1-vISxNujempRhdytF5qWngqGDCLq87K8q1sXZN8EIttFjo72ULceK6yL7NG6ExrSH8c72aXu3qx46nzfuTCfFGnItOVi8rbGDi5Iq8g4aw0XxN5DnzorrHiru_FV9WmjChrP28oh3M1dBtJrxDSIZKH645fyGbjDP5p_gjKJoMxkSbup9R7wp7ToIE0Q1mpgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvu1OTRgnL_CHXALayDb3q7LA_Tenbu5voJyrstWf1e2A5DDL2AzLOLaAXR-fpg2Hde64L2BrPUqcViMrvfoJgNVxAgUW-lRxxygof306Gkpon81qrGr3uMIIne2ZhyMPwtpAWh2Z-irUURyeG1w9vurb958zrxdJaB5WKbCThIRg_m59WllF5excmL_9iC3_XCMDMz0ZZFnfUUafrDlUIDBNh52SrGeG3hx8WhcCtASpgoJXRi9bPEZZtvF1TGjbGxfYUcKHYvOrgsqWj0bdnuBs6eSJIjLGmwehLKEQYsCow4Db_nznxuDFdAgmy5F43G89zvxG9LiPxa3LQGWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9cgCWljbRS_mtoTZYyNPGRzPFwKMW-FsmhjUB7Rn8tu7NQLCwF3wX4YZz4XfZpbW19jyqLu220lN65OBSvR27AEW6yghC2bCdm4rYiqpXmUVi8UZzkEF8N_osHntVODliFN8YOVTvpDMg9WNyxR9q4q3LzouzDiV7GyBomDBELC1RTZVOyQqtEHxnyUeuOFEYy74ZTW4-65uL0MJm0I6dpJpugn7_8rLknA7H3oD3kTEqstc0oTHdN4tEvJAVgl4kSalZ_yAblX-afCW9ViBO-DbkaNZrdEKfy0MNwkDJ-K4qbGk-VIXTyBd0uJlKDb3LoHnAgbLCugnP2H9Gqgjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Q09lDy59QrxUuYunVFYWQugg3jZRz00-Tf5imHmBpra3ZCjlUqgC711CRI2seT3D6Z1HD5EkDnGFLdD-0bpcBciMNjKypQcpC41lpYzWCh-I7a_FBQBlZtEtWQpgBZvij6wNfSsUoW6B90CBM8iOnrw3OiCZ22s61Rmyp8uJWfuHQNe1oiVHa2_CePyuD4YaRjiRFP_sJs68qwfOPsXBISXyJWB-UN8OH1OvEMIpF2H9XyOXTd0PXuvn8E2C2J6vd9N3EgrHIO3D6U79BZ02FCM4ZregI0iNb8S7HrBax6HB9k3vzJguMDi-jABnwRijiJnjwySdSL42W4yV1gKyFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Q09lDy59QrxUuYunVFYWQugg3jZRz00-Tf5imHmBpra3ZCjlUqgC711CRI2seT3D6Z1HD5EkDnGFLdD-0bpcBciMNjKypQcpC41lpYzWCh-I7a_FBQBlZtEtWQpgBZvij6wNfSsUoW6B90CBM8iOnrw3OiCZ22s61Rmyp8uJWfuHQNe1oiVHa2_CePyuD4YaRjiRFP_sJs68qwfOPsXBISXyJWB-UN8OH1OvEMIpF2H9XyOXTd0PXuvn8E2C2J6vd9N3EgrHIO3D6U79BZ02FCM4ZregI0iNb8S7HrBax6HB9k3vzJguMDi-jABnwRijiJnjwySdSL42W4yV1gKyFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb5FwBKHc-nKw321C009trvyCUcLH2lJAm-5xEzXtmY23xHbXrLbjTAJGxE5UTf94rOpXpDPiPsmILa9xoMpYD79CZGKiCOOCpCINwTHpphnEWHLmZLRtRioiE0WDhPEf17gbg3cZ0-1itMFgDX51XWiPpn7u-he2Yabff1u61isqWw_ZFMGBSD0Z3AXfNGM_SBFJ8qbLXHdC0WZwGnq1lX9drPVCH5eaWFtfJSBxSBLgbNj5X43My3ZF-0m5qU65yZpik83KIUDhCwSds_qJh6h8Tt62FIZFKLxNcjmy9EbgOQmTltFDQpNzXwGALOFcWBRVZQid7no2Fu4wiQm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=nZKMDheReoY1gvHD9hIYbuWABdMomPW83nKkCdF86d4YMKnyDEGpi_u3Lqg8eR7y1tz2VHr6svUb3Bi8cfPhpQwtIlKONQQ1tIoe7DRzGNj7A2ec5YwjeqEo7eYvh0CWDl01AHbLKcBteEayS-P4TvrvRPh3v3J7tFxPXAl00bW9MAMdPpbBj46kTtWHJhe7FBQeRteDkSrm6wvYkAokqPPAtugtK0UgdTWNrcfLBrqIuGGdBUCu51secyBHAR3V8oZVsv4wf_xZgXQnHbDhaco2I1GTQUyfqgec0cYyGJ4oS-pL6xLeKUHtMr4EQMGab5f3Ofqo1ArFF6-0xOXnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=nZKMDheReoY1gvHD9hIYbuWABdMomPW83nKkCdF86d4YMKnyDEGpi_u3Lqg8eR7y1tz2VHr6svUb3Bi8cfPhpQwtIlKONQQ1tIoe7DRzGNj7A2ec5YwjeqEo7eYvh0CWDl01AHbLKcBteEayS-P4TvrvRPh3v3J7tFxPXAl00bW9MAMdPpbBj46kTtWHJhe7FBQeRteDkSrm6wvYkAokqPPAtugtK0UgdTWNrcfLBrqIuGGdBUCu51secyBHAR3V8oZVsv4wf_xZgXQnHbDhaco2I1GTQUyfqgec0cYyGJ4oS-pL6xLeKUHtMr4EQMGab5f3Ofqo1ArFF6-0xOXnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns5av92_j-50vq-hRZpGO-E2GgFtIm2fKF0Kld6lpzHAauF8twY6UdefJFB7uDfQvVVlgERPctEABcq94fsnhigdki61u02gLBSMF2yl0p2Bm-9ijtatNh3MKWj5hb7P8OMqF1iKTTj8E627XMZ_A2aXWFXYsNMKuxLhunDgV3qp0yocccrvZnixMacX528QlUQ-WVo1Q9geHaolhKr6eFQeeuqfn18dTpERvlPgnZhOMkWK2G6Bm94sjNB7vdf8yGZHkEaNW-rQtMaeVpb_9KmAquqi0QnImz2GMixJzCat7-Xz-v_mBD9xMO1nBf_UnHEFyyqmXy6qQa5CrYf_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RitD_x8nzgTugyCRaSF18JdGEDdR4XoaXmskbbpEWmH8HvU0u-WzK53DozARuLXap0lr5E9m5HyJ2586Cn3gMx1FCih_cwz_VOuzi6QBS_kSqLqccOG4tCO8JAdcgyZ3xGip9MzX6BMWp3hEG4fUxHixxfG0o3lNmm0TCppcmNMJS3QYe0yTJPbF9vN_FO3rpngK6Ri4VZhU3O2VUqouzRCoMoqHEzqLB1dgJnCsiGsxoOdr5rYwKwnc1AkE8J1q8AtJUhFL0_SVWEzSeMKLvd5QBLIi_TRECx7eNRPkbinfMyNJPM5GylzPw5yg5u1m1by7MnGfc1_bIKbZHBcnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=udoYvQmw6kj0qh7zG9Tp4Qda2N5BKPvajqT43U_ep0zB1JsZFO-hODDhnD-htuXKbiS6yqR8_vQaugFub7xS6vhdW_l7vDCkGi40c_EWT7qXm3bMM0NETP47DPOhr_ZOPTBLnuOGozmrpCzzsNFUM21eKFUEB0l0xei1xjt-lHf1aF-abvx7m3UW5Sg0oQNajLNs9DRW_Sgsh8XIXSzU1CyS4Zq-2iyKDj1cW6D_eiEq-t03VNxJtyi6cyejwpdHJK0SZ6jpLt_vBfayvkAF53HN9jZT8-OUl1HN4MEojpKTGO-ZQ02RoTAxELgOOlsG4apflqPV5cEVINbfpFC_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=udoYvQmw6kj0qh7zG9Tp4Qda2N5BKPvajqT43U_ep0zB1JsZFO-hODDhnD-htuXKbiS6yqR8_vQaugFub7xS6vhdW_l7vDCkGi40c_EWT7qXm3bMM0NETP47DPOhr_ZOPTBLnuOGozmrpCzzsNFUM21eKFUEB0l0xei1xjt-lHf1aF-abvx7m3UW5Sg0oQNajLNs9DRW_Sgsh8XIXSzU1CyS4Zq-2iyKDj1cW6D_eiEq-t03VNxJtyi6cyejwpdHJK0SZ6jpLt_vBfayvkAF53HN9jZT8-OUl1HN4MEojpKTGO-ZQ02RoTAxELgOOlsG4apflqPV5cEVINbfpFC_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6ecx8Xi6UbV0RQxDOcHbQQb3wz6yGSCcOujVs9Wej_4d0NN-EauPSglNe3xuyl1YYTWiiYfFGK2JPGupa2LZcv9ysSoEvW93nM8qEBk224JVRAZc-MqLVHYrB6vCpe82kudSUEmtQG2Cy6RFhFzga20ArmL8aNjj1f1kOVeMv5E3glmg-t_MtQRrYVAxj7g8V_yf_fm4D5-oTt5Jt7uv2fU2GbUyCBEYjhEaWZR3hT8xo95qU3Gy4ji9hyvJ_9Sw8k_jKlo5HZNh2-sVrI1YHqCnZxPTLQsVDLpuz60XrBH_SARwYKnxYgHKBtTZaNO7unJE52ZWFVidUxlHXq_bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTwHVgG-hj03LwDuW1n_3vAEZeFDma4EnAnPQccuNomBROmR3UBwfPX6-iWV5Juo6ALLRpHzcLfRbI8uwPZnsG6duFSRjTI6As6TL2jL0I5lpdvkyyLauguRXJO1j7gap4na8AfySVTF-D2_qPgdOAASjX6mfDNa5mk3B5MS1oQmtkBKWalDVX1w_-pi7vg6I4QQBhNDN6HbswQ4Z_89JpYZsV7HJS2ZBoeqz3I_gEXgBV_NB4nbVKKLHCFaxlpMXx7xpc-r45jUzDS_wfLWP1wDl2DTHO8sP236Xye_4dBLHy9-5dXTOVelxsAWEvJ6hFt4Ne61vErs2X1ohiXsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUwYaCAWis5c4Lk7vqtJHmZv7oYESJz9HfOQRi-BYbkz8EFLDYHhxipYDBMmRrsls5M92JUkgAzZVThBNRkcRBH_3Td8HmLQ8NrM4hPqDl-pKrGJ9EhZPwpPNReJnrZTPKn1Si78ORXySg61jO5zzf-FchLTW4c-qRI0kO1aoKGJcL8TFZ2Aqm3yeUOU1WzbMJU3Tlm0suMkCfhUE2CiqHJdaPCy1Y6TTHYd8uAQ16iab75Lezdk41DeN2yK0-ifr-3HinRcLYdYugTstlzvgpqjSMmI0yg5zJW5cR4dhb-5x08tJqSF8DXui_TmZvn64WNRw3Kxa3XDur9zyDft_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q71-X76D1cPooJYuhwKCjoI0I4G5xKMjxIhGrTjyAorU7BSQ_9OUboQB8QaqeK-XnUaG5RHDgu6ACVyz9FqFgqFZeEat12agXYWYoXIjuMHXFMuyGfYhHkmpmwMZVwKFUaaBiZeCIUlY5A-K2XXLV04Zh5OOAeDNtFEa2qzfNbcletiRQG-xVkkyV1F6fOChvj0LhA4LChxKVC7BR-V8Xz6WRibUlrN6bOgqfHncsjWzcnd6AN2sAH5DQf_Yv3Jtkm3CtT8D95cedNzXAxhBTfPpArR3JgnHNrrNDI9Nv3kny-A2zfnp3cIHajaPqsjm7tNXsSpepD8alSEoqSNNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6uMirCsPGH1-0_tWJ_plfgBg1gZYgBzUbfnySZZpIpO5zNfa4QnMLrYjbqUK5B6AWdnR49V-HmWkkdDcfo7d59t2AIB9EZLYH-XCArY3pjj0bTVpEjxH8rgdrw9NX581agzZTSjHudlH4fp8YU2YuV6ZtKM7lOJDDyoCNBv2WTcRr82iZRhrqZcjxp0Lc7XKI0SGuXM2QhWqTCSZUYTWHps4QC0mh270-Xmwqw4Nk9BMZZDf4YrmU31_9J5fzmicbOCSsmfw4bVf3nb8aaYe7H2T3EwyGkf_mgVT7YeB6_Flp7fwj4yUeOSS4P7YZHPRsqALzkbjLKuSOqhfJ_tdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJKPPb6BmS-GBvPftVOCBQXbmI55UudJieQ_w8h8PA2tntKC_FoADt63BjzpKCF4v0HNYx_MYE20MY7uSGkf3EHwYbd7Fr9iQaQoDANRWpzbNEqR1g_66mfJ55AukX8noBfzlYwpuX7o02h9-k4Eqq5eL0XHvemI3KmGeO1IIUwMzsu1-G7wBKzBYx5Ki-0LAx5GClM60oxvS65m6RK6AURddJBJQbnHdMnrzD1WjztgdZdRNbTGwkR-Y-XBMfoNdcBWbVbD1Y7VR9wRVNvoI2CpK3DSi5SBVzLy99uyO91saH6aeWqfFy9o5UquM-7WEmtwsruZg1NxVpBzUrQ8SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=aMmKSkkCxwob1Ai6ygutH-RmSwUZqg4IEZTCU6YPDT-73vax-dFrU76CB-bd3TDf7vp--GCeBR9wcBoo1uCKu5ijbaB9f_Fr1qvArpreFpMPKgVXt46QTP2Bt6wFwOjmDDwUQWG3OCfMhYkRznqw6ldDvDAF-9hWL2UOVtG6veR1BD1KgtyzCVq5K9z27uoT7cJiFlKLsNHv5SKCK385-MjBd-V7h9MF6zZKkVgC8yv9rB-XcXQKckfKZ17ACuPCxdr1Jzapk-2a6_f9Yk_DXUFfqxRMdgh0TryuxY6zpjkAYqNv_9CiF9RFCVfSEforDFPf0Vdao6ebwf4gnCUEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=aMmKSkkCxwob1Ai6ygutH-RmSwUZqg4IEZTCU6YPDT-73vax-dFrU76CB-bd3TDf7vp--GCeBR9wcBoo1uCKu5ijbaB9f_Fr1qvArpreFpMPKgVXt46QTP2Bt6wFwOjmDDwUQWG3OCfMhYkRznqw6ldDvDAF-9hWL2UOVtG6veR1BD1KgtyzCVq5K9z27uoT7cJiFlKLsNHv5SKCK385-MjBd-V7h9MF6zZKkVgC8yv9rB-XcXQKckfKZ17ACuPCxdr1Jzapk-2a6_f9Yk_DXUFfqxRMdgh0TryuxY6zpjkAYqNv_9CiF9RFCVfSEforDFPf0Vdao6ebwf4gnCUEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6AgNesYens5yr2kPfsItuFaluHN9AToZ_cDp-mRP9fw53NxFeKUjWaWIPt8VVGbRp7QXOtMX__O6lr2gpiBD253XsdK6vdMxkUSWFT75iPtgPlBqzK1D1RLcB7YSkdIB267vW0zP_Phqz8KZafVXdF9vZiL6J0j6tcMUnRam_1j32S_pz61UxdStnLh_jOWl1a-Ro7O6UcRF4_bPjvRRpuuv2shun9gTNc2imH3fP-SaMDwfGCd2KgTrzDEbW6UsUM9kb9eEoneCa3eCJrZAtJnkvldwUhpD7J75IuBOIUD3McYIWYLE2lVwdMwOJXmdcbIzCBmE5-D4Z-lB37ciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=qrb5ocToo7gKjWDiJVga0xEZ_0ZpfgeHNvW-mdc57iwyrz2HIaJU43-FfJaLVCBDiUcZekSV0LrCTQuQmtNdT2JQUtCw-6mIJ6lITemzcIhniMc4KWPZvB7G4xwlA9zmNSm1iA_vXGOj32P9YRHodwWLdnXuyyMU1xu2uJDyuhBilDIpWRamAmkc8nv4a0n-jaISKMoJuoWXF2FJeT_gAqMYPILVeQHFHOBtlYK3209LUwX_Pn5im2Jm6TF4mlcX7X8wB9NU23vRbORX84-CixGsc8-pBH-chxjIg2vaBcbZjUq1xiEO0un4cPIHjdfcttP6JRCzbJvrY-98sYt3CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=qrb5ocToo7gKjWDiJVga0xEZ_0ZpfgeHNvW-mdc57iwyrz2HIaJU43-FfJaLVCBDiUcZekSV0LrCTQuQmtNdT2JQUtCw-6mIJ6lITemzcIhniMc4KWPZvB7G4xwlA9zmNSm1iA_vXGOj32P9YRHodwWLdnXuyyMU1xu2uJDyuhBilDIpWRamAmkc8nv4a0n-jaISKMoJuoWXF2FJeT_gAqMYPILVeQHFHOBtlYK3209LUwX_Pn5im2Jm6TF4mlcX7X8wB9NU23vRbORX84-CixGsc8-pBH-chxjIg2vaBcbZjUq1xiEO0un4cPIHjdfcttP6JRCzbJvrY-98sYt3CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=TZqoZaUzLsPR2CLs1Ti3KQCN131LHVXCLu9bFdaMVGlT99Hmmp0IoCws6gORkTRD7i1VoV3bJgoL7xLPBf4IQC6XLC-4yfnQjSRtVDUEs-iRYnzmV57tmaJuF6aGUu8UgZFzD4jQKJCknkSPXDF6riEgNQ2TmSaLwsWutA9RQwl9RIXh-JA28771yQkGrlJBZaIY3scLzkCjcn0iJhKN8U1WZsQBVC_KvlFSjQOLiAbYOaIzZQwKmrOHD8Jyl4UgIihdxayFAkMiY1sgkqLudI5DweliY4qN8zhaG-7a_GJnHHqCBrmD6ZY3XAMG2zX9mRQcPg8r65xGoKQtvfHk4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=TZqoZaUzLsPR2CLs1Ti3KQCN131LHVXCLu9bFdaMVGlT99Hmmp0IoCws6gORkTRD7i1VoV3bJgoL7xLPBf4IQC6XLC-4yfnQjSRtVDUEs-iRYnzmV57tmaJuF6aGUu8UgZFzD4jQKJCknkSPXDF6riEgNQ2TmSaLwsWutA9RQwl9RIXh-JA28771yQkGrlJBZaIY3scLzkCjcn0iJhKN8U1WZsQBVC_KvlFSjQOLiAbYOaIzZQwKmrOHD8Jyl4UgIihdxayFAkMiY1sgkqLudI5DweliY4qN8zhaG-7a_GJnHHqCBrmD6ZY3XAMG2zX9mRQcPg8r65xGoKQtvfHk4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilbCcmoHy1e2GgntLKxoH1PrXZLMPKTyEXfQCTFGbbrSxJNzSVPkVNoET7l7WzETICjSL8iJ1Bky5u--tVwPZ9UfneRLW3qxRUeVaSs-4lFbj_V9Guq-p-VuVbjRbGrMefo7-4LwcKlgWF7E9ahDLpn5D5KPFSu7mcpt1uRrqIh64spC_NuwCZBNvfwlg5oGdYx7etFe_o0qwMOxp8iwY-YSdNmSutjRTrA4hOqwf_Ls1gpiqoSAHz_yZ4LpxEyU5bHP7DKMXmp-r0SaP0QsX2Pze4oZVbW8HO0-nbHKxg1PQBp26NosroaEToZvd-WJShlHPxrcXvqLGddBGsgh1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=hYtBqqvWrVmw93sbuzzo5tgUUoqdE_vg-EH1xw5lfPY_lHdi-Px1D8Pn84tqvoMUw7PsxlJN9LAnPkNCrEm9N8i6AufmHXcGeGNqE1NDCkoznnShVd_lzdR3RIuKmz0ELLURYgDfjYlogtoyL6Z2YheDd-nIryry_SX1ZEou5O6hyWofYDxMBE6IoWvcpGKXjAHtMEQwfHk4BcYlyFokKRz3cuwnd6OxlnPl_Ud1M2Kme6pFcBgGsMmVUrC9q23cTJeaP1g1NCbBA4TuV290zEW46Jwbm-Qrwlh5XM7kX9eV6sOT0eM8ZJzsBRn6Ma4OqUx1iyQLB23wj2DGBWmfTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=hYtBqqvWrVmw93sbuzzo5tgUUoqdE_vg-EH1xw5lfPY_lHdi-Px1D8Pn84tqvoMUw7PsxlJN9LAnPkNCrEm9N8i6AufmHXcGeGNqE1NDCkoznnShVd_lzdR3RIuKmz0ELLURYgDfjYlogtoyL6Z2YheDd-nIryry_SX1ZEou5O6hyWofYDxMBE6IoWvcpGKXjAHtMEQwfHk4BcYlyFokKRz3cuwnd6OxlnPl_Ud1M2Kme6pFcBgGsMmVUrC9q23cTJeaP1g1NCbBA4TuV290zEW46Jwbm-Qrwlh5XM7kX9eV6sOT0eM8ZJzsBRn6Ma4OqUx1iyQLB23wj2DGBWmfTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU1voGnYDmkkH-ts-_su5XisydMBgLsT-XyA6_bVJDNL8LivARJ4Ljr-nWVo-7jApabzPuI1kHoDaCOQXN5X96pieZQQc1IdHBbTx_LYkvGT9wiIaJXIMcmZC3WGFvcEC6KPKQg6gIGzV5hQvwRQbaPewgy5n3IQVlVKZxxYvzBSURreXHtoSPEsNvUI4GCEfPDHAH8IWpD_r3UBYri5p3-ewmFHXGe0JdBO_v1REmdXwzcbssqRgYXQcGiiwNm2Fe_xs3VOd-pL57_fp-F9wCxdDoBrq9HUxqJ1TJy4KCgZz3-FOUCVJ6Sm73NraRFs5buKvHPHISVRTFjQRjplLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imxyqx9cOTpwNYArmIgpM1eV8XIiqpDrMjGx3CyucLwUhwHIO6nfEN7Hgh6m_5kRF5F_dvRbEMcHXEhqdK-Lt2mUtOlZIPTCSkTkPSfKe6YVs-yzvu6UmpcgPhJDeMNqGF9Wg5ZBJfV9RClB62BCvxj26kr1gi6REKQYaf0wW0Rs2T1LP_drfWxwHeyh1VDhv880y8-rmS97Bd4FRj9eGldolh0e7gOGy4BABt46m5Th-zjFFOqrEkDRXYYsMv03SrSCKgTCpmvdmzpJuBXYPuRtGYJJkuOYYIgiaEhn8Pz0n7wdILmE50rSOVvAgy8UbbzcFZvF4cBe2ZfkaNZhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA25mO0ylGEO1m2LDggXZb9scnAFgMDPVwNcJWO5txAERFybNqg1F1SVOfbfqCMauBGL0UPOlpKmClpmCR6OyyziFau5sTPQvLXC-pvlzjrxRTb-0UsFZ_gyqgGy9o7xLQo3mF7iJSSMSE04oKYitpvhrVXblQdT0jObaSK-p2iRvD1AH2tivatPEOZr8kf90pT1Gn2e2R4WXAQgm-VQXcK5puAUw6m89-4QidaWYfAeYez4Io-XKALXoUCqD-oxxuTey0WinVImm1ZQp2lqEz37rNXbbyhF3AXpcydmdxmiaAeznvI6XTKA8YWRhQtAI08ERD4pZT3iAU8R5GPrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLurZkXWWOM8pxU37isWp3lQFYYQzMrgDU05slrBkfMGBxjP42RQB2aDxNoIfY9yeMH2XrxXk0kzr4Cjpj74OpyjQGEd8kN7K0GkNg2FYdk36P8Tx0owYy7dJ-sxijNc5q5gcMAAkEWoL6L27NJOXWPjAhqJa0K-99dJlK2mhYiCUqI1rGQcbUDSikVBguVlwRGF2sOC4XGKBR40-a82vdVaq5DipUG33LBVnd0rvSjheFEaQogYx55MrPTv7dCikPRcBWx3N-pUMBkzHRBSh8QxNYFSUBbpWdm4ymvtTZGA2aUbnBzkUNfSTEsVS94RPnbV8K6l0EFAseK-m1Fx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYbMiwLofFcbd1hngElIdmsJYNPY5d7pvybmp-fybhFXsNmYCcHA-FpdvB5E9AVHjtLX690Kscv09vEKrBcE2hkU7ULMXsKIXGy0WAERYIBGxOfM3Oo9J1qC4nZLDTaphQn7JzOKnh4zAOcuueVxjNQNlGF5kjU0ffg0y_yDUZKbgIwgQUGvRJmNvImgBIX-Lu4PNQvF-GJiOzYcQVNTSuFxhG03xr5HE61pG2mAq82pTEDnpIl502Ji8O9ggQ0DVAVeaVyWpaJ_zQGMUY0RZT4oO8qr9htU7wC01yYYKKToOCgXuKwU8FVTceynlFekVm84Sm7afUDNEan3PLBxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv62ShKg96SeTw1jcvS-pOUP3wv4c-CJ9b-gglyOW3qj95KfmpDGgjiigsLRDKb6mEXZyPR3BwNvMlzMtQa6MZuO-13_pY-e7tS_swNhv8fkx8iYQ_WKe5tLQNgJhXHSWix8JQvWgO9QzWWXHoB4M-hx3ehmKC-AQz6sGMAKuvpjHMTJHmF0Ip2dT0WXc76VC-zsYI8WmUob5hc_kjSmGyCHlCQ0vFygG8Tav0FTtnUwvVCSFYm7Z6Sq19rVs7lN_yIWbtFVQ500hKZBaD5R83PRYnbu0KWjDd4BM5zamy6Jyaio21Qrl0Q2RutXMtblL-7Fy-gmfgzBbanUrQbk2Q.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=ACkpoUSB4UtYf2FHz7jH7CGeiysey8MIpB1OgGit_roaVL2jxT9AuSC1aK_E7uoFXemhC9fD11OKu6txntnIDPY2jmpZ__HatjvAiYMBzNulmuFU2HrTOmAo3rsSfqAeDQjRNdvkskat6M7q2w1bnIpd7-v6TlwuKA6FyJwL9I3d-OffIBNXxtE2FI1-_ZuM8eYkgPKMMJkIoWJ0bm-APOg8aWQXMTUX7qnMiDjSlONRoO4VVBh8R3BgQXSQGmbhuNy7Q5rbd7bxFTGgnGxlZzHY-LEjWVNteNMKxcqZVrBiMDr--FoWiOxnomJhNZXJqU-B0PCPe1BDgiZqBlQsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=ACkpoUSB4UtYf2FHz7jH7CGeiysey8MIpB1OgGit_roaVL2jxT9AuSC1aK_E7uoFXemhC9fD11OKu6txntnIDPY2jmpZ__HatjvAiYMBzNulmuFU2HrTOmAo3rsSfqAeDQjRNdvkskat6M7q2w1bnIpd7-v6TlwuKA6FyJwL9I3d-OffIBNXxtE2FI1-_ZuM8eYkgPKMMJkIoWJ0bm-APOg8aWQXMTUX7qnMiDjSlONRoO4VVBh8R3BgQXSQGmbhuNy7Q5rbd7bxFTGgnGxlZzHY-LEjWVNteNMKxcqZVrBiMDr--FoWiOxnomJhNZXJqU-B0PCPe1BDgiZqBlQsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=qCg6D5dyanuIgqJ92-iuatb4vUz2TkSFaJ9qDcpzYKiQkhmknjeh1NCCxICqY0huwTUdFbMXeyj378lPg0-gzAO3J0hXVzOaigiGf5XrHS2S7pNfB4r_MLCXH3ZIIePa4lR5zmuofii0rEITmd9mz_KfXpVoYjUFgBEyDAWzFDZBckb_mLmgmR8f9roSeVSO-IIax2BSI7nguDOwqAXWTpF932vB8yPGfii2rApFCRa90ao6bHthTuBSJyrTqLriYKD_dvFgSINiL6wp_rNNCwQ1aDo1DVSWY1rW6F8yOVcvCcCxkr2fiTy3RrCTc3-esIxGkU8nMHqF1-3afjSeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=qCg6D5dyanuIgqJ92-iuatb4vUz2TkSFaJ9qDcpzYKiQkhmknjeh1NCCxICqY0huwTUdFbMXeyj378lPg0-gzAO3J0hXVzOaigiGf5XrHS2S7pNfB4r_MLCXH3ZIIePa4lR5zmuofii0rEITmd9mz_KfXpVoYjUFgBEyDAWzFDZBckb_mLmgmR8f9roSeVSO-IIax2BSI7nguDOwqAXWTpF932vB8yPGfii2rApFCRa90ao6bHthTuBSJyrTqLriYKD_dvFgSINiL6wp_rNNCwQ1aDo1DVSWY1rW6F8yOVcvCcCxkr2fiTy3RrCTc3-esIxGkU8nMHqF1-3afjSeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=PObOL88JuhB8uhzv-x6NwIkgOTrYqYu9J2vGxX5gvppS3SpxLrkQZWYtTmqG-N-JQQBNoVj74yZnj4fQrUKsea91xCMbRVEAXejSgDyAfCcaTYagopa4XA0wVLcyH57QiRscs31hnk3F5V__WmR_KAq_U5idFUjhk7KkKzSe_ieFMnDIVqIX2qrPKNfbFKHN7BI2HxN63yVChcKdSqKYFqqgo-q_AL7dQkh9hGtpkccB8vHYiRKac8YPW-2EMi5oO5A1Fw-cb77bHiJdCoP4b1GloemnRR4F6bck71Q5xS90QaK2PJoCbCCJLdXywSTnVcTlgYcncRyPQHhAlTOtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=PObOL88JuhB8uhzv-x6NwIkgOTrYqYu9J2vGxX5gvppS3SpxLrkQZWYtTmqG-N-JQQBNoVj74yZnj4fQrUKsea91xCMbRVEAXejSgDyAfCcaTYagopa4XA0wVLcyH57QiRscs31hnk3F5V__WmR_KAq_U5idFUjhk7KkKzSe_ieFMnDIVqIX2qrPKNfbFKHN7BI2HxN63yVChcKdSqKYFqqgo-q_AL7dQkh9hGtpkccB8vHYiRKac8YPW-2EMi5oO5A1Fw-cb77bHiJdCoP4b1GloemnRR4F6bck71Q5xS90QaK2PJoCbCCJLdXywSTnVcTlgYcncRyPQHhAlTOtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=VAiNqxajFzSCoUzopob3iz7yHnxFKBQlTCrC6K98Oz3MkP_vXvvmbY8mtQC9NpewBoOn3zQp5rP8aVR49LxrOS752BVkJOpQWN306o5dcjmF004LC6xLHDfV7NRZpXrB7qbvPTzOGj-f8QlrKjP9sGOVDuirX5IgKL9maMAevCuGPW2GvDQQ1eEJHRzQJo1m8ynmPO5fsPDIJqR6TPFPlTqtXwDlRfBSizxh0cj845mILutJopVVdO5cbyFuFZalFNEjZ0FV_oLZRG0dbOjdi5MetSQ4NvkAune2rsE31eEIETD5uX5DOZyVaVlvS_eWUAafzLSLfMeoFY6Q5FwtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=VAiNqxajFzSCoUzopob3iz7yHnxFKBQlTCrC6K98Oz3MkP_vXvvmbY8mtQC9NpewBoOn3zQp5rP8aVR49LxrOS752BVkJOpQWN306o5dcjmF004LC6xLHDfV7NRZpXrB7qbvPTzOGj-f8QlrKjP9sGOVDuirX5IgKL9maMAevCuGPW2GvDQQ1eEJHRzQJo1m8ynmPO5fsPDIJqR6TPFPlTqtXwDlRfBSizxh0cj845mILutJopVVdO5cbyFuFZalFNEjZ0FV_oLZRG0dbOjdi5MetSQ4NvkAune2rsE31eEIETD5uX5DOZyVaVlvS_eWUAafzLSLfMeoFY6Q5FwtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIsMHLAthRmAtDsEKN4ssxM6VYtnLM0xjekXOgbndaZDGWr55ks7vmqTfywSVPn1ADOe0Nw3DVGmcMCr50-tIVBoXPF-DjynZ6S62kuMQlftf5unyKKKU7Uz4wZClM56Mzz_nrFHejtQdVPyKQpd1Rt957_uZS1TJZO0gL1DDJdqVk5OgfGCxd-mXhgiqh9uhIA2Ej-FaH9egnzDNvwLRWhcWBWqWa8MnG1gSjWhsYxaq6McR9ZnKZJlbpVQvxSLFOONpks1gYg7023JZ-p4kdjdaRWPddB4a_dQfFZq2S88Hzy4eczf8-bV4w-HvHlBk9Oyx_DUwacmRG-R3gGpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
