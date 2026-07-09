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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhv62mcsOOLL0ete9XfnCRObegtjel1jQtta3AHlgSz3re9QZ9fYTmus_WoPanpD78E8DxIrxCQq6GmkmthwXUWO4TxQTkUuBLqbzj3_UpOxakhMPpQf-2ArkU_TazLzwCoe4hGm2catc2RnwXdRCwCdkK2QU0xEdUI3n_A6KUasaTWOjM9AocRVEg6MGGhoeYxlq-VpoLhvXqQQtOdAHXRuLwLnrs5Aecx-UMn9Pw1U0zMcWdPP37txErsNC5EyFGvIEvVwLmQ4CET7HTGpYlFavr0YdJb1jynC_S8MVKTqtqSbjuEjBx8e2iDA1unVueQCpRVXZMkhLOuCVqOaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2075261040867037280?s=46</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farahmand_alipour/5980" target="_blank">📅 20:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1ff10c03.mp4?token=RyxmPD98pdd-V0E_FwW8_08eZBF5h8r_MRTqzB6VdbDEezYIRqVWnwSmxnJ6ZcLPiWBiBTw0mTbgcvfYtEVoZJB9eUPDm-MAFEpKL0qHu7zbjRbBE2BD16CmDvjHKhg8zLxUgYYfH-W9MTD_ss1xC5pFqUL_Viac6pWvetmVimijLkM0AeMqaW-OgmjjTRydTdN1GtHAEY_Jh_-ucHRbjS_j4fEiYm_6P-U-fwYSxNCIjZ8qNlKPOIcDvlx8XWMOk1IHBcatH7vv-PNviQ2NDOL-ofiECehXZQq1BqIarvN5fIEq_xKpiZSknfKvYkmCE_FTF6Wo6cv_Qgmtb1bCzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عربها در حال آماده کردن مراکش  برای بازی امشب مقابل فرانسه  امشب چه فرانسه ببره، چه مراکش  مسلمین به خدمت پاریس خواهند رسید :)</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farahmand_alipour/5979" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farahmand_alipour/5978" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c12274c3.mp4?token=Ja1CxAR8F-I8oMVGJma9AIRwT0h4EaPDKvZ-PsDGnIxc59zQ-cc2vtnUuJ3RCM7CcAfcbSCe74o64NJPMZestxYMD_ShrGYsxGWMYn79-S9SBK1EFCG1Y6jesHvFvLBsCiJxqgrLnDNdULV1pviTMRQHTPpcYvqPghz5EUIj9FgJGjixfwX56Kg_BS8FnST0hiylJ7Na5yw8vUx8uR62g0Reaaa-udhUMW61Saf5YhzCjaJpDHTvsSm-8AAzLlX2CN2dhAzgN0qvw0_kFPGcqt3mCUBYLYtW6p5F71bYxXr3KxufLHFrmow5ezUWj3vHIooi-_3OP6cMxdD3YKAswx1XfBJ6BvxtkjWr_c_MWgL4Ojma9Z85HnPHqUMaHUTO3LcOt1bzlgA_oSQOIesNdzXUnbg4s9_nOYFEJKCNuDLCarZDFzgXUAK3ShfCVY9SYbnIVttRXL2iGvA_ihouiZa2ow8OSTzjjNF2IHlkp79MqCVBOY5LshrmXgGEpKi6OPj5UCKtOFEZjOqLTg5bVppYD7FU-bqCyoUfgVZHmwXOO5SMz-SSucN5OWezcHBD0qJnxyIkhFw_C0KXivcdQH-F8lMBMJuBp1JejDCSI7G6P5tY2PhTI8DwHTQ0NcU9p2tAUhGf8jjZMJT927u37nb36nhqFjXH0_2p0NAWmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم روی تابوتش رو هم کندن و یکی دوبار هم تابوت رو زیر و رو کردن</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5976" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUD9wU7-hVaeg9IOUTIckMwFDkbt3kh5NfRMt1ENq_iAc9yY4l1FEKWlMNFWWrgtn3RfZAEMDh_H61Y-Enso851R5MvpXCcZhojogz6EFN3aq-OmaU5frwqwQmJ3oHl0SwTA-R_RrvfmX97OqCylYP-IaSFVtEiQjaZkfIsU7h3rkXQewqQ1Oi1bRVWREakvhd-Q4OcPiSqOoQha4Nv-ZlEBYgwNZVyDDpi8KQzvrxC5xMqsiP-24shU8Ib5XIKIypJZc9SNQo-o4cRJqiaz7D-WN9L7akJILv3KkN1euT8HWNz4cw9I-cWkV-gOCuQjZB8QEDH2XEu7T4dw1gaO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی که الان قدرتمندترین چهره نظامی ج‌ا است.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5975" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpWKK1f6GSdx1XJYF6aT0hQmPwc12h1RS9u4c8-F-oCfckATc-AbLIo1g-1lSj1YbYnqLQn3NosFT-rtYTcQUqL6miPxg_TE-uxT6MEWOxB2wsgkMllbHGPHRduExqRsz-hkX63JKWvVHm_Jd2YeT_90fzVVIlGOftOKEkqBzj87KPPyBG2HeeEBE8xWv3nxIocGYAnzZQxHLbQkqL5bLxs8aZCHVczdFSCJW5-XiHv_6jABE7sNZiA2HA5ehl8xhy2MpR3a_S68Qt_4BNwkxdJnVOSsK7bGQZpavb6UFQaAOxWrFjo1rtVtjyuyN1bgQvhDGAAF9Rie3o6wx-5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=JiOpFzzD60GBOnclHuQSa1cSLC42v8oehTgjX5SItX21AFnXbHm7-ZVwgY5H7bgeiggFGGvwzsRp8MSgo8JcL9bK8nJgBnpW3Or1nCYPZmiMhgkmfGuDZdDeNMv7piPUfQKOFHe_yxofua83IvvbPPCSzDSuxcxq9D1dXYlxfXSRiV0LtP9PYhkN8wJKmw4RLA9EwZCY0cTRaLbNLpemxsBgN-ggziNx9UczzL91FBzP-EAwsvh34EoTWN8inyYVGl54eDx6ouvf_dOZs_juaHNC4BgMCyG7WHsR6uMrcM-Xi-ICL_0IvasdCu2fkbxlRJd2XWwPa2KvJ2cR6WIzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=JiOpFzzD60GBOnclHuQSa1cSLC42v8oehTgjX5SItX21AFnXbHm7-ZVwgY5H7bgeiggFGGvwzsRp8MSgo8JcL9bK8nJgBnpW3Or1nCYPZmiMhgkmfGuDZdDeNMv7piPUfQKOFHe_yxofua83IvvbPPCSzDSuxcxq9D1dXYlxfXSRiV0LtP9PYhkN8wJKmw4RLA9EwZCY0cTRaLbNLpemxsBgN-ggziNx9UczzL91FBzP-EAwsvh34EoTWN8inyYVGl54eDx6ouvf_dOZs_juaHNC4BgMCyG7WHsR6uMrcM-Xi-ICL_0IvasdCu2fkbxlRJd2XWwPa2KvJ2cR6WIzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=OtH_30IVTKk7bOWF-g1mDFGcVACqLm_BL00quZomOcNF5yb6lhA3x0eIGvSMG01n7qqC7ceBR5FIc9u_6fXPoeYcf-FHjtrhci41rM9Q731tmjavybbqdntvpj5lpqo-8wl5ED6NGQXi25Z_FuCPBLmAcP2ujhf-NqnlO53L4IdiajH6BPiKGx8HLz5HdRM576pDhq4M7NGvy7127D0gPoIZa79MyiY0U0uYqEP9evzkU-Ph8H1drenv6qdyB3e-UZ5fBKIIOs0t5aCWCQ2dXux3nHq6NCAhkFuEK_KHsCoL4jUd2sRSpbcO3CTTsZ_ZRuvlp_MQadaPLatmhl7bhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=OtH_30IVTKk7bOWF-g1mDFGcVACqLm_BL00quZomOcNF5yb6lhA3x0eIGvSMG01n7qqC7ceBR5FIc9u_6fXPoeYcf-FHjtrhci41rM9Q731tmjavybbqdntvpj5lpqo-8wl5ED6NGQXi25Z_FuCPBLmAcP2ujhf-NqnlO53L4IdiajH6BPiKGx8HLz5HdRM576pDhq4M7NGvy7127D0gPoIZa79MyiY0U0uYqEP9evzkU-Ph8H1drenv6qdyB3e-UZ5fBKIIOs0t5aCWCQ2dXux3nHq6NCAhkFuEK_KHsCoL4jUd2sRSpbcO3CTTsZ_ZRuvlp_MQadaPLatmhl7bhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqdFmRnkB10XhjVnRdd4D1IgE6ivMjWbrzFNjsqt9yosU9AdnnZ2k17wc2rzcndI6x-8zwjCxqWzJ32PC0Hb_OWc2kL_IicqN3_Ps-TSSo4EjLiG1fwpP67hzyb7TJlwzBQqP228Kv81u1Z4gOE7LGCsf9nEGFPBwuSRSY_gRzGPAyxwWhP1wH_VUnF6gP4NWW6khuV64E9ObZ906lKu36SEU5huCK8X69X6MmMyeoX0ZVHxko0dbRtlvnEd39WoxQxknKTCHulZYx7Oe9kyz0tuHIXnfLPlak02PrGyeBlkeWHyaTzMgSKksVf6qMYky-gOn9OL0k0dKtj3KA1pVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=N7vAEdNvEHMP-uc3_ZYf5mCO82lHA_RncdSQOGzwb4Gtqa_-3EHTzvjw9i0RWw7wPdC-kpR1lgg0K7I4j2FwC71YhV8UMtsM34mkmXE-3jDxHOcn81c6gV9fpg_TgqnIIqWg4VGWbykpkY_JeovrCn2iGNX_ikX8PjNdtCDbPhrPL2BU5lEjVNiw_qEk1W0xKvy1qjjKtdLi-SBS8G2cwU2MvY2DRQilSLB6nda8pVcgJxlvDMC5ccHhKbpEnr0849l1nheDIPDtJmFS7_C6YvqUR5W2DJ0qs5a_W6d6MvIpl_SbP34pQfBQF8tun3Jh-ZN4IK-nekc-n1P80kNBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=N7vAEdNvEHMP-uc3_ZYf5mCO82lHA_RncdSQOGzwb4Gtqa_-3EHTzvjw9i0RWw7wPdC-kpR1lgg0K7I4j2FwC71YhV8UMtsM34mkmXE-3jDxHOcn81c6gV9fpg_TgqnIIqWg4VGWbykpkY_JeovrCn2iGNX_ikX8PjNdtCDbPhrPL2BU5lEjVNiw_qEk1W0xKvy1qjjKtdLi-SBS8G2cwU2MvY2DRQilSLB6nda8pVcgJxlvDMC5ccHhKbpEnr0849l1nheDIPDtJmFS7_C6YvqUR5W2DJ0qs5a_W6d6MvIpl_SbP34pQfBQF8tun3Jh-ZN4IK-nekc-n1P80kNBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faYxdnp2I_ll7nUJ02SPitsFDKmSusgNOqWtghQpQNHsLFu5aJYA4FPUtjBQDzJAQz0JJkmT6usdfPoxIezHToOFSr_sS0OKbJkASGMuuvfU_WK6Lth2e0l7Z8_AFcVjIftzA0Nz4Vf0A9_VkpMxeHyy8gMGSjhQiWPIm17_tJQ6My9rOpgo2PzA3HizbEYTEsTS7Op7vfrLenUlw4RADkWAmzKEG_48SLN_TYhSoVV_l4ULlF7lz3idsIP_GuSLhRin4Y0I4GDoETBtOXsj9ZQFuG7KdyOpjq94zQS6g2mcSX_9GetHeYNAp30u_ba87Cb3Pllwl4tkKRexKCDzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=tPezk6KeZTHeneGiO4KF92Y40hBu5HxmGSe3uLtb4qswCckUJoYpHLoDc46Hh5re6CsxW1FBUYHxg4i46gxsmUfWiGqrNnW10W05D7PmzfXxd4fL7dDLNRVY9iMq_NL-YEHLAGH4Uq51g2S4lsOoDlgVKBshnEb63K9IvWFa4U6eMZeiTioUAueialrcBR-5VHM_QMB0oAP1be9Iue8nVGPGT2gTv1Gbov0v9hZTyJ8LNrnZY8IFeYe1MRZ-BgPb49hagphGKKuOm722u1ySQt0H_HwERWbw5JG2jSYMAzwvwMKCWnYePoS8bF9Ek43N5bSJoFy5L08wkXMs1Jpgsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=tPezk6KeZTHeneGiO4KF92Y40hBu5HxmGSe3uLtb4qswCckUJoYpHLoDc46Hh5re6CsxW1FBUYHxg4i46gxsmUfWiGqrNnW10W05D7PmzfXxd4fL7dDLNRVY9iMq_NL-YEHLAGH4Uq51g2S4lsOoDlgVKBshnEb63K9IvWFa4U6eMZeiTioUAueialrcBR-5VHM_QMB0oAP1be9Iue8nVGPGT2gTv1Gbov0v9hZTyJ8LNrnZY8IFeYe1MRZ-BgPb49hagphGKKuOm722u1ySQt0H_HwERWbw5JG2jSYMAzwvwMKCWnYePoS8bF9Ek43N5bSJoFy5L08wkXMs1Jpgsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlTgMRudcU61lMn3UlkoNdZYlXbXeTXA2jSUxcTUbu_Rx9plSQxdamd4UjoF31OmY1pXdhVwidWElPv2oI4YA2RwIYwPClmZw5G1n8uC40P3Lso3le2ukOyxL6ou03GPKUKFK4Z8EJf9gaC_QXuTa6M4jFpW5MasD11fs6LmZuhD99zL1XK2y6aFsuhk7yssG-dzCyoGGJfnXIle0pV36l8jXPNFTK5Fhm4cgMI8-6zC5oa3JAdrn6Js6I9MzsESisZy1OElY6aKqMrcgkX3t_0pt0w3sFk5dMFWaDiufXO3Tc27TlxQF5UrrGeVudGf3TT9irf4z1Tcs8Prb9oZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=GMu28oBiNn6hs1sstz2hAJvq9A31uTXPMo_XUaAYoLYps9tSzwxYXkx0LrtiBs68VarxGJbJftXlXtwPqHiCOihKHCvwLn_rZou8EEOLGZgJp9wrdk4wa6Qb0RG4zNfndB6Me-EsBZGRctmg4H0nxHGOufWSmzaeNoXy1yLUHmX0F8aRqr2mrFDW5okPNxsOHU0OAlacb-viYMWLYfbXxhVv9R1_JNwFULdahZAwhm4zHKbCeZkTts5ClJcoZ8ItDwbyqH_Q9aaPaW9jnOIjdStVHtcTIinvLbnZJ31eKcx2vn1YuB2TbxmljOYjuz4DMRPJ1X-aPIAwsRAe_Dpt5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=GMu28oBiNn6hs1sstz2hAJvq9A31uTXPMo_XUaAYoLYps9tSzwxYXkx0LrtiBs68VarxGJbJftXlXtwPqHiCOihKHCvwLn_rZou8EEOLGZgJp9wrdk4wa6Qb0RG4zNfndB6Me-EsBZGRctmg4H0nxHGOufWSmzaeNoXy1yLUHmX0F8aRqr2mrFDW5okPNxsOHU0OAlacb-viYMWLYfbXxhVv9R1_JNwFULdahZAwhm4zHKbCeZkTts5ClJcoZ8ItDwbyqH_Q9aaPaW9jnOIjdStVHtcTIinvLbnZJ31eKcx2vn1YuB2TbxmljOYjuz4DMRPJ1X-aPIAwsRAe_Dpt5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqgjnWIFrD5oaArer3dCg0iT1aoSGpXbFspB7MyFURmVs6-gtoFDbCceN_sIGmqDc9009-CGze9bYnaCalYrXFZ6LxFmPvN1yIsHUPKv4h77bjwSEA30O6wd5uF0pKscDv_PtG2qPLnycYJJ-dOGQG-ui4uehpgVVNtuEkbKDzWAmVBW0Pn7rJlkEmkaub5mH_Ql3qUP82fliFifea1bueFSi24wgpkvRgjpch-TaYnnNyK745SMDlupQ-RC5nSRQ7kcwZ_AcgGFp_cfxdsi7UxT0FwwabNlrORvC2BgnZf03CMFNU0QoRjMagQTuHFp3Oxh6PxYV1taHNhOMq_LYWLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3ZqqgjnWIFrD5oaArer3dCg0iT1aoSGpXbFspB7MyFURmVs6-gtoFDbCceN_sIGmqDc9009-CGze9bYnaCalYrXFZ6LxFmPvN1yIsHUPKv4h77bjwSEA30O6wd5uF0pKscDv_PtG2qPLnycYJJ-dOGQG-ui4uehpgVVNtuEkbKDzWAmVBW0Pn7rJlkEmkaub5mH_Ql3qUP82fliFifea1bueFSi24wgpkvRgjpch-TaYnnNyK745SMDlupQ-RC5nSRQ7kcwZ_AcgGFp_cfxdsi7UxT0FwwabNlrORvC2BgnZf03CMFNU0QoRjMagQTuHFp3Oxh6PxYV1taHNhOMq_LYWLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwfh4OekYtPf3XznZJDOBdCXn3dc8vmf0eqWWT9SnwMNNYoxYIXOwxsUFoi0uO2PIzYXjzC7RRRt41wOpwa-WDRBc6056H_aOc2MIhiR0EUEVM44RPKjIp8yxxnD2JXzk7ti-byVD-HR9QkpVUukR8AW_ISgbdgQPMHr5PdCRc_WtNaOjrZ26hK60k9TFCF5MCsfd1h8OBsQv_w28L0ne51JbL-3k1-JgGiTsBWCYonhKqXeEwvrMsLUhswBl0q3q1JstkSTzAzvqg69qWpLdUUCV2ps7SWCwcn11ygh0XfyzgnZ_ApSHq1XS6_VUahY3wQevruAOgV7unEp7iJ-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=M_sNk8N-BUJ8JeBzNeDJ2PDP0M5reEyxUo5qYYJivZp888rhnVKvkuQoS0vUbNgbMHIsrRHpv4G5sau54mWcof_h_yCToqCzOtLg3d7faVAiapaA4spiQAdcX7M5ig5uGkSMQtyOey-JkkYwcWABZLYJ8qXXbCCHUY3xWVCLFRf3om6d2dRv8cOYgimnf8OmL9FPG0BpFHYWC2JtJvjzh94htUYWgrcpamDO6FVVY1dgdo_sEx30l6oKZNtGfN9au6XB8R_HtpwX7LPtdwPQ1Gahh9Cxwn-HgQBJFFORVn0_fS_WmLeekp6TH6chESapfsnTHcuA0QQLJoYfNvW0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=M_sNk8N-BUJ8JeBzNeDJ2PDP0M5reEyxUo5qYYJivZp888rhnVKvkuQoS0vUbNgbMHIsrRHpv4G5sau54mWcof_h_yCToqCzOtLg3d7faVAiapaA4spiQAdcX7M5ig5uGkSMQtyOey-JkkYwcWABZLYJ8qXXbCCHUY3xWVCLFRf3om6d2dRv8cOYgimnf8OmL9FPG0BpFHYWC2JtJvjzh94htUYWgrcpamDO6FVVY1dgdo_sEx30l6oKZNtGfN9au6XB8R_HtpwX7LPtdwPQ1Gahh9Cxwn-HgQBJFFORVn0_fS_WmLeekp6TH6chESapfsnTHcuA0QQLJoYfNvW0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Ex776OmEIDMpk82Kq3W3d-r8jFR9SPcyGoK5Pwbxd34i87Su-qxFLoBohId7iU5rEqUzNJgQjdQ8uVZTksCUn7PjKgRjXQNwYEixtpwIs1SyCbznAj7i1yqxUi_NPL5kUBzffBjDL2zg6lG3JwzpV6RStQ2BczhB9syA67q2rz1cvpgUo8E61sU9LOtMRQg0EQBl_y67vhYvNG7hKZ1mN-8YbQst5SIdOMu7dGejU-uW0Vo_X8eyufVcatYz1PM8LmguWPsR0r6u_US3MyzIAy3316saLIPE3JlhMUkXloOKPpUU8zthi6sGWrkU_Jww3ci7brExB112YNFlAMYCIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=Ex776OmEIDMpk82Kq3W3d-r8jFR9SPcyGoK5Pwbxd34i87Su-qxFLoBohId7iU5rEqUzNJgQjdQ8uVZTksCUn7PjKgRjXQNwYEixtpwIs1SyCbznAj7i1yqxUi_NPL5kUBzffBjDL2zg6lG3JwzpV6RStQ2BczhB9syA67q2rz1cvpgUo8E61sU9LOtMRQg0EQBl_y67vhYvNG7hKZ1mN-8YbQst5SIdOMu7dGejU-uW0Vo_X8eyufVcatYz1PM8LmguWPsR0r6u_US3MyzIAy3316saLIPE3JlhMUkXloOKPpUU8zthi6sGWrkU_Jww3ci7brExB112YNFlAMYCIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfj_AsZzBbMlBAHCoWZS-3d4MDeN7nwErqQIAq823DNOjOxF2E1iHjslhhtYDhiVQjvVtqNbI-D_qo82j01Q2L7Nf46UIEHFJJJTI4yVUDe3rbLWdDnIY35IC9HoDas-fagEdUIHNCq-UylXGKl1ordKJzcNoV1N893cax-x1zB_wak0BPICa2R8ILCNwlqoF9Bo3dUBHKiPWla6aftXDF4ABVU5HmSKVwnOUBA1NvRlxK7avf0MtuWyVEAi35oMPtcJ1OQADnpDK2HG8tj9WqM25wUqQ-nkzgHPfFgGDnpW7_12XXfkleYd4z4QtbcPVzmEID7TjL2in5stgytvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UUp6AO94HcU9zbh6MAxryYeSgvDLoiXcV65KPQhq0qZ9LKEbn0cNtRDS1ZsBlg-CLSdFm2DtwoFd7-TDyiVVuB6AjEkgCO7u4S7d5hosBAxlHVl9USzq4hh4-Y_yuq6yNELMqKSXH32Wj8xWldmuk0tfWmVUZf4-UmhZuTSKRH9_gymblAz-mYJakpfo6PtegDW0XDcLBrZeRkWdRlTytltHImxsR8L2RFnj-CKhR_yfZN0eBtlz88TGcz5NfD42oc0wYQIsmRc25QqVqxuDJ5dVmZuld3DpF4G7mo97bEglznTPmbJWrl6X4121g10IQGshaah8v0D1sFXG4PgkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UUp6AO94HcU9zbh6MAxryYeSgvDLoiXcV65KPQhq0qZ9LKEbn0cNtRDS1ZsBlg-CLSdFm2DtwoFd7-TDyiVVuB6AjEkgCO7u4S7d5hosBAxlHVl9USzq4hh4-Y_yuq6yNELMqKSXH32Wj8xWldmuk0tfWmVUZf4-UmhZuTSKRH9_gymblAz-mYJakpfo6PtegDW0XDcLBrZeRkWdRlTytltHImxsR8L2RFnj-CKhR_yfZN0eBtlz88TGcz5NfD42oc0wYQIsmRc25QqVqxuDJ5dVmZuld3DpF4G7mo97bEglznTPmbJWrl6X4121g10IQGshaah8v0D1sFXG4PgkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=HnQNlopylISnaVfv5MQVpY8fr0J2PtPwZWWrYNllWThSisc_apiFU8ukroN1DOfh5tdASPo_OPjoNRuZlycBi5anCJb1GaCs_DZn7q1QA8LxETs6ZMq4MnQc2sjwu7U8KXuoenQ_eS-4kcToN6azunmEvbGyjbdgF1SAa3LcvwtjTY6ydlkRzRDsAYRMRElAvcXsC77YL6-euf3RVV2NLvbfYdfiDxtqvAjG-ndJh3tmGoHxaMW9ZXuwnJbDqFi4otQPmJwuapxjvW-4bLXJWnyheP9oazyU1kDJg8n9C3BngVqNn1nq8qt-VZ6SoZBnmDTwdhGKzxgYsh1Odr7yKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=HnQNlopylISnaVfv5MQVpY8fr0J2PtPwZWWrYNllWThSisc_apiFU8ukroN1DOfh5tdASPo_OPjoNRuZlycBi5anCJb1GaCs_DZn7q1QA8LxETs6ZMq4MnQc2sjwu7U8KXuoenQ_eS-4kcToN6azunmEvbGyjbdgF1SAa3LcvwtjTY6ydlkRzRDsAYRMRElAvcXsC77YL6-euf3RVV2NLvbfYdfiDxtqvAjG-ndJh3tmGoHxaMW9ZXuwnJbDqFi4otQPmJwuapxjvW-4bLXJWnyheP9oazyU1kDJg8n9C3BngVqNn1nq8qt-VZ6SoZBnmDTwdhGKzxgYsh1Odr7yKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=q3p5S39CRY-9Bf47MUUHZbZJmaT5KrMt2KBogQLx7BstaqeI8siyW6CzqQaKXodXNYuwynBfqPQPJHmZiIAMyAkxHqqVKzZZp8sbEFEC_fjYlWOod_90lVRX1lLxbY-qJ6RQISyZIEk-i1IFTqX514-RtLN-VTNL5UcLk-2u-azy7vErFNrZI8snMivGLfkVcdsWXSJPovM4wXYM9kABQQyfxAEM6cqehtGAXYynC_Z46ZBz89plMMhST6eRpBqP2D8PQQT53gsK0vWGIUj2l4b2AMFkVtUwJ8MXXZH_8pcE-ynDUcXLiNGU5D8Td-3tBMubFFk9aIONKXc3ueipGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=q3p5S39CRY-9Bf47MUUHZbZJmaT5KrMt2KBogQLx7BstaqeI8siyW6CzqQaKXodXNYuwynBfqPQPJHmZiIAMyAkxHqqVKzZZp8sbEFEC_fjYlWOod_90lVRX1lLxbY-qJ6RQISyZIEk-i1IFTqX514-RtLN-VTNL5UcLk-2u-azy7vErFNrZI8snMivGLfkVcdsWXSJPovM4wXYM9kABQQyfxAEM6cqehtGAXYynC_Z46ZBz89plMMhST6eRpBqP2D8PQQT53gsK0vWGIUj2l4b2AMFkVtUwJ8MXXZH_8pcE-ynDUcXLiNGU5D8Td-3tBMubFFk9aIONKXc3ueipGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=IibW8BZCmKDjhJHoX86woVJDpshiXg6iY6U5dd2b2kmjQ5wizP68MDuDngE2wCFtUSD9j4bb9NLoGpxGxYPCPrEsTty6SWK95AG3pidfmaGluwCtZeSPkPy1RAkXurzHCcYLahGqyMsojVxPqw7A_YcDwNIxPUuecEi_Ay5UTstRjNqsoyxmTWY3jQu8OphgXLrkbssVlROSzEkiBV8A6kBdp43gxwMQ-kAQ9oeBMI_BWJoq6wtaAz2mlIKJq6KfJ9Zp3RV3kaJZOZgXRjHmmnwa9hbaY8tQAn5B5vmyvSegBmH-NkEW_FXq0p9ibyzJLL9wPD7qWyzYQctWV5SYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=IibW8BZCmKDjhJHoX86woVJDpshiXg6iY6U5dd2b2kmjQ5wizP68MDuDngE2wCFtUSD9j4bb9NLoGpxGxYPCPrEsTty6SWK95AG3pidfmaGluwCtZeSPkPy1RAkXurzHCcYLahGqyMsojVxPqw7A_YcDwNIxPUuecEi_Ay5UTstRjNqsoyxmTWY3jQu8OphgXLrkbssVlROSzEkiBV8A6kBdp43gxwMQ-kAQ9oeBMI_BWJoq6wtaAz2mlIKJq6KfJ9Zp3RV3kaJZOZgXRjHmmnwa9hbaY8tQAn5B5vmyvSegBmH-NkEW_FXq0p9ibyzJLL9wPD7qWyzYQctWV5SYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=G_8yJYL40pwmow4l446eEF_tKA3PuuOP2kIsiudrh8WAI2XVjxJHKKva4m_wxAG_1Ph22oEuZGKdm2Bp4uGZmBMakvg3dU3VmpMKvxzcrFF6WvS9cmN_Mj7TOj9aO4E4A_Ia1tja8LTT3LTn2vLpOkqkd6TJELJ00kg-FIM8sldUC8fqNWSBcG7308wK55oDNuTTSaFC1OjgidhEHWbpjhtubGbRV5Tbt7POeCFTn2Cv70qHKcQkd5F1yq3SY2vUVgGaKczxNNgupmDTceACodfsMYfUhCl1EKx3iMmNfgVJzbEK6CyrGYzCk5HLQIp6PxanIHGmJazr7ikbTt6XpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=G_8yJYL40pwmow4l446eEF_tKA3PuuOP2kIsiudrh8WAI2XVjxJHKKva4m_wxAG_1Ph22oEuZGKdm2Bp4uGZmBMakvg3dU3VmpMKvxzcrFF6WvS9cmN_Mj7TOj9aO4E4A_Ia1tja8LTT3LTn2vLpOkqkd6TJELJ00kg-FIM8sldUC8fqNWSBcG7308wK55oDNuTTSaFC1OjgidhEHWbpjhtubGbRV5Tbt7POeCFTn2Cv70qHKcQkd5F1yq3SY2vUVgGaKczxNNgupmDTceACodfsMYfUhCl1EKx3iMmNfgVJzbEK6CyrGYzCk5HLQIp6PxanIHGmJazr7ikbTt6XpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv_3NDUg-lGLRLGrcNycCj8gcNOB68jqqdKol5sV3pMFAyHquQNOneY98WuJGHHPlFpbFrriFC6CjkvOjZtNNQegRl6NM7vcI4YWrvmBKYDKigBbCAflT20CSLVBVsfHOc301ixr3P5vMwaQq9Fz12oJ08idyRkGeSEgpWq8YX8xOBh4mz3sPCQ251iManloASlHOzqBbB-xUvI6Hu9fMeDeBi-boKWeQ_pyU01yyp_oAC24gj-s1IzCY2O3J9v7kjm14EpwonuVEvAS1cTMmtSYBexN60lz2FmAZsHoQfmt6sQ56oA39EXaIVVJyN1dctgmPnXFOSSI_IF2fijYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHed8dCaeghiC0j35Hv0bHh-g4foh_rvR2MvYhvAzKRj3eJI8qlo1wJFs0dkgiTZc4pSBLgLrmyooLvexXQ3uke1QvN1cW8_JRp4fogRHG5zsMfWRdp4Ytf5YGD700oPDXmoUGypAePYp4x9I_FfHpgtRGssc3R3U6fwxlwMIm1ekh69JD3iBw7PpyNvDyoJQo4n01m7z8ZaLYsp4nQJhl-WuoyxX2hdt5Gm6JRSLzfor_uTSlkd4jlq5rWYcoEpgrVMmGwjOPIiFIkWlrzsbcqfq7Imz8gwsOcuGAhk-XOdckAeHX2T5ewcz5IP5VCJDLy2-FuhBPIYtEH4r-2PUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHjK56y35dMEm8XPWSjZ6qW59N4W4muoIb7pCPXZtzKhdx5sLCt9ab2t4zvKPLefAGJUXl-b7nyYghq5H-WbcgiEvDOc48YGY4seqynfEtb_MsFEYh2vDXfm1S_T1I7-5jeb5NlgsvParC53ZY8tOG6C5KMn-xZVJ0nW0sU6xoorDtHVxEDWDbxJQXVsF5YsCmNc-ZJzWOP4ANhVXt6pRNB_2EW8ps8BY_UgTeW3-aUG7ZHgCoVsVj128nzek7Mspz-gKrJ3cwvdvJGFrgTVoEQ6SeJtDIBquxIIOWzSpVngV_Yv-FmEjWOE0SBCJtahQyrKHz5ZHbaGohzxQk3Xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=sxgo0FEj3cg31n_wr98qOmf82TSEjVn06j2uyLmF-8DH4WTftipn5u_bHlJVZpJJatPMZUeiO-yPxOo86K94tW2qJqBXGI8KxyGuwvoPWKLXrOLrkdgjpwIrnVlEOod9M4o8AHPW32Pc0GMrfX6B3yhKhfEloENogrOwdwoFGqbVHOZAO-sOTAgJSOOFkWi9yDnx6vcq3D95zkRKl-TnJd3dSdUHpOgD4EBuMixmuU_7OIz7UUe3aHYHLokxdwTFxPO1BQ9WPyZnWqVsef9CDdjZlUUs9rg3Dj1omVejzMUAR1K7_PXAOi5draW-YYYfQZn8B9BhEzS-ElR2fT7u3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=sxgo0FEj3cg31n_wr98qOmf82TSEjVn06j2uyLmF-8DH4WTftipn5u_bHlJVZpJJatPMZUeiO-yPxOo86K94tW2qJqBXGI8KxyGuwvoPWKLXrOLrkdgjpwIrnVlEOod9M4o8AHPW32Pc0GMrfX6B3yhKhfEloENogrOwdwoFGqbVHOZAO-sOTAgJSOOFkWi9yDnx6vcq3D95zkRKl-TnJd3dSdUHpOgD4EBuMixmuU_7OIz7UUe3aHYHLokxdwTFxPO1BQ9WPyZnWqVsef9CDdjZlUUs9rg3Dj1omVejzMUAR1K7_PXAOi5draW-YYYfQZn8B9BhEzS-ElR2fT7u3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W160lPWdlwJtmtTTfsVj8ee7k4TXMv3h2rlUKcxbfU9GMqMGBLYtJctyc4IAsPmXaIfWYdyxp95yaI30EIRcRM49HYG9CxHiX5jvIjzu6ldYmJlb85KqNFkGXd3ZV5ZSLISpqnue1PY2BXVm0WwcNnwj3iE97aYiOoOmCOaUMAgD4VeTh7gtyNoYKlExo_FHX5skP_48ye_QDMSLw-zH63jDGxuesi0_9l8b3HKoArtEZTiPiwn9bjFV4xBsgdniWTsrS4274mXzLoV2sj9rvzBYP0o-foL6YhWvjBSPHDS3av1yyUX5hA3p49NIclB4832ePWCiFu8C8UihA8-LGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=WSklTjgA7HP5ugrVOtfQ5fda7P-qk501TI7hUv_ZvFm4jGRqhskMwRRhTmCpZYAVfJZ9AsN-M5XrgKmsRKbvF2JRU8uxwfRgyyQ9klPq6lX5G8D0eGhhytYOCdFCuy53iUDe1vF20D_wqY8iZM5dypMTUmj88O8PzhdJbaN5pnyRA4AZ4Z26TbehRXDIH1wQV7kIfoqOG_Pc1qaoDhVafnhG0mZQzkuTYrFuuABqmDVltJy3ZrkJiE-Xs1WSov1YvGbejTRX-UImNANTh-WElUPy7TSbab0pwlLnZCc7gWBQcWtmZxYj_KMsxjrfhBKL9j9aDhCklLqpIw56vJ0eNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=WSklTjgA7HP5ugrVOtfQ5fda7P-qk501TI7hUv_ZvFm4jGRqhskMwRRhTmCpZYAVfJZ9AsN-M5XrgKmsRKbvF2JRU8uxwfRgyyQ9klPq6lX5G8D0eGhhytYOCdFCuy53iUDe1vF20D_wqY8iZM5dypMTUmj88O8PzhdJbaN5pnyRA4AZ4Z26TbehRXDIH1wQV7kIfoqOG_Pc1qaoDhVafnhG0mZQzkuTYrFuuABqmDVltJy3ZrkJiE-Xs1WSov1YvGbejTRX-UImNANTh-WElUPy7TSbab0pwlLnZCc7gWBQcWtmZxYj_KMsxjrfhBKL9j9aDhCklLqpIw56vJ0eNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtTcphVhJkMItoukmejaTTnO3kLCsT8OF0ABM9mPXfDtaXmeCx4WslLo49m29jttPemp4AxpA8HoGloLH-wewhztKRoX0a6qdfeGePjvoqqaE8njeqjYmE9RgXpXYEoyqb1eTcqInBoaB3dYs7I419lql-oOzx5-MWTUUlzleK8R2f8pJaiiReLhiTBFnvozRo7YWFaHWF0pO3Xxmnn_i-Ed0qwbIKiVWTiWkKF7SJF2MYUVSmmQUYqof9pJwBomwITTGJ5pKVcU0ZRer0zo0wXhBWDCh67Wa3deBFNzd_qDEFhw8F_t594rn_JOux5HMXTN54mheYLikOwAbpa4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLH36AliZNcLdPcu2_dlBZzUvdEt1edv8EVMoPSuXNTyVHvqtdJnOasNINLvau0X9fix9dEjPb0-VhJzjpd5W0dixb705zX5nikbldWXFhCGTw50wUkobwQDLn-mPQfcoDiOVC1GcvPY-LmUkUZtEfnJkoYSmONynqaO7myg3lPsQLcrJNt4hQ3nlesHSyIA1XbZNLa5-i8DCYrW1l7CovWWmrKEYXHtncMBC8E1AKXoP93AwDJcC8Lb2b2k6bCaMb_RqeTgVd7LcwffH_5Q1uR8ErItKKN5yT5M4L9uiyNwU7g1vtO_kf6n-eadvdr1SkrfFwr8_YVpVUfKIut45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=pl3lHfTPOLd0qyjQDEDQkKqYRfrWmS9CG753zbL-7x_24SCTOcoIoJNFvnY-hsf10Zzha0kMU2IURVWn_Q1O4ElHi24Z1ZwdIv9bCnvcE0cQJ7OuuoOPhUNnXxW0l7Kg8HVkhgIpnjpa9ZwKOAMxwR4ePMGpzCh0H0d7IFpAxiM_DVKT-IxNgVHZu5dFH5Oie7wGdHNWNr44DYq08VQzcUF2QVELOhHpAH1Sw2-JB0r-V_0B48IjjVQBig810Oob8845uq627fIdrsmJA_ACcRb_WORcrWeOasK-igErxiM6sc_sTKsUqt4ppKqkBqGbDcIJQBuTyXrC2aNKFeTjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=pl3lHfTPOLd0qyjQDEDQkKqYRfrWmS9CG753zbL-7x_24SCTOcoIoJNFvnY-hsf10Zzha0kMU2IURVWn_Q1O4ElHi24Z1ZwdIv9bCnvcE0cQJ7OuuoOPhUNnXxW0l7Kg8HVkhgIpnjpa9ZwKOAMxwR4ePMGpzCh0H0d7IFpAxiM_DVKT-IxNgVHZu5dFH5Oie7wGdHNWNr44DYq08VQzcUF2QVELOhHpAH1Sw2-JB0r-V_0B48IjjVQBig810Oob8845uq627fIdrsmJA_ACcRb_WORcrWeOasK-igErxiM6sc_sTKsUqt4ppKqkBqGbDcIJQBuTyXrC2aNKFeTjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbz5tcgRuhME00kCvGcWe6gZs73dKdQpSwLQ3qAVe8LjiDd4DdJI0zWZqY-MJ2g7hIoxH-QMJ039BIbPOYjX6HDVsSwyhM3VPfR1E81seX0MC5R7VJ3KzfCoMwjFwDMQeU_eZmvIMQD1j9NczUXjbzXMBCJRJqZYqlDpgGT2NcKLRYWMBXXOpJmDoGfPayAPGUqU6JIRwn_IdJ5hN5JfKxP6g_cMH5Ix6DHN2588ZQFelM52iI4GjOwsvPxQnaCz7WVW0Of8XEXQ2Mlrr09mNX04DXgsWhimghIVyR8j4o3A8bAJnouAFARurdTJkvtU0mam-eYuZ1Zf5ody6Jjlsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmjiSRE74Rox0cv6A3pd_5eGN-1d2ah7eSswOeFKIa3sv9kW9K5Pwxfr2VECxLf3-9w7o5yyQslS0BeTlKFQHpFY5RAPrhwTwJqCHUpG0bmxx-qBK3Ew_rOlIR3qt6aYOvGJRyvbP1b1DiiMDHCIsM8sY_7ueDCtUs68jiX3EmnX3LlfCmyr_ID1TR4F7N5-LeOnw7vJUrW7-c8G3JemHGq4VG5XSS24kHBVVrA776tXaDB9R5p-0kWEuIfrmsaq6waSBlXYg0tEoU0kLXBVQdPVclJ-oSB_pE9P0qma-nejCCDUgmh9wibDlealATWBXofEeG0MYdF6iTPo0j_NCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0do461wEW5n6Tta-CbeK9TLNdqwxEiCDgFcA_hv4yZl9aGnEYxYVgrNCau7OTzYJ9bq9ILQqayPG8BQWuD4LY1UH6CE2Wan84GHq3cxWNK7y97g7HHbWLVaet55d8FHr94P8wGLPoAM9hY1gPvTmZMSnitI2r1vH7ysrG4_VTAL_u8jjWY5Ham356YRLh6xpuI0st7I4Dbci0ggvwG940w284vdBXEkE9aH6oUNSATf9xwiA0jbrr74p48XmulmWvjWqI_Fs-gzXH2BCI_LsZFfT0dRZAyqyNDqwCFCvwmYdNrt67A3yeCeOQp5D9bmkdvA24GrQ-C2eljNIblFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oH8f5uExhwt0fovewJN6CSjwo6WprcuQpKy3aHRdTrW-jaw5t3PmZPLzZcsplxBgHOF_YshEJgE2z7h0MCuCDidbtUT9MTDnDy6psVWZYObFIikB2P7SzkFMh0Cc2juPmVmunB8o6sn9u3jbeQDroZ89xTidWBo3qJCeyEzwUvlQT5IgusnriwuU2ufdSMEjq_41NZBPpzCd9zwVV6XWYla1REEzwX73uh2Eku4pFXbmnoL9q-Ie42jNzPx471RSKnZaU67VqEB7ZltG6HqDh8-s81RtMkkW-NAdbkQJuC0yVWsgWF54zKUKwCdUr4pZRfCRVdXQaiNrMX26UmP0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1PKLX8zh3JvFjK0nE6hxUzoy8a5ldCyYKpMCepVSGsQuSyTYUNPUpUJ_Gbi5TTX9vH7D-8bgDknb7-DRIIHrheLBE8v3u-H3FOhZ_jr-blT0wye3CjJihVWu4VoQUxO14GZQ82BxL0_nxHN8ZViARy-dXMH8a9vmZUSXV7qJrhfddSf5czjZeMojv2aeXyCl6Sq5G_-fYw6Nq5_0dZvC0MFZWOJ21uv2-3q6_5NvgzjvSXbenfo-jVDwGCE2jH2lPNxy35HmHoPKXKDPhrcALkQEppWZL5Btdu0SrHeSPxBwqkgAzNBlx3rt85k4SzENYlvSd6y2ZafD3hOUxrd6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZtwcPundtT-4EVhMMDIpyzeGqZggFPUQnEdbUWHLrexygjjGXxVJ3fT6JZO02SDGYqNmpO6qXUOBiNYLHgjhTXwNa8V7w-UUFEulmMk5YZ5gUQ9gk1ZNhz1n_iFuejahjLMYbR-KX5yrnz9v_U1rjBm2dRXHTR22V4fnRZQ7cQ2AyDaSFidMrIOccNdSebR2Nj3jCyp1uzoVsf2VFLYkbqCMvu3haegMkgo8CikkVyR5S1UIrK2Wa5yBkIneohPTKDbEJb19DkWnADS1dQAP5Fzo44xVRcXW6gL7EW0HfDTsDztAXaAuIuyfQkQLIjPEiOl0s0J1W5JSXa4xU0ePg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=NXgM5pelvs8b1qQMX0UQiEnIqxP8_A1XfLu89vwUSZvgklf0Vpgo1c48FRkVDgXsCBOypGuAxIC_MM7BbwqGjM06Mwxj1DkHE0l948OY8ELU9GOUTY6OMa29EEFxdgv3kPJeDmYVC9bhz0Jr_XJXSnjGA1zqs8CjaLyr3hLrOkB2y1qNxjgGrXiZ8DiIT7LqaEKkyXvjPEHRLnQzt_V4y845UeBYQ3G21v79lC2J-6jS1T63s1k_4i01DeVtMfds5-q9UMbROZV6ejUi-iH-Jtae2WDjemA_kv0xmExA5OmroCg_QUeXiMO0MD2K_jjFjo7PhoCtDeLoDS7QAdvWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=NXgM5pelvs8b1qQMX0UQiEnIqxP8_A1XfLu89vwUSZvgklf0Vpgo1c48FRkVDgXsCBOypGuAxIC_MM7BbwqGjM06Mwxj1DkHE0l948OY8ELU9GOUTY6OMa29EEFxdgv3kPJeDmYVC9bhz0Jr_XJXSnjGA1zqs8CjaLyr3hLrOkB2y1qNxjgGrXiZ8DiIT7LqaEKkyXvjPEHRLnQzt_V4y845UeBYQ3G21v79lC2J-6jS1T63s1k_4i01DeVtMfds5-q9UMbROZV6ejUi-iH-Jtae2WDjemA_kv0xmExA5OmroCg_QUeXiMO0MD2K_jjFjo7PhoCtDeLoDS7QAdvWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFWGxncHtUrQ3s1-wYpsWPBHQ1GBvbpeljpYh6clCjWXE32mgK5F-Iu2r9Cy0FWPM7N5ONYJT9IvbKdUIy1_ddPu6NQGrigL-itxtsP6FgPRz57gv4uRLC-G7fncL3emQtLFurz_OFckrT9dOB5aVqfHnq80DYIl70Y0it0BxBnB31t5qLgKJlWUU0HmjiB08bhgFHUuYZhY2MAeiRkcvSsG7qzhko3ny5cF-XfgNmLc9W5NW4o8-s3Ps5Lcd3XO6iYVuCJQKUFngPMykoOABmh7k3_TcCb94ETEzUvS-bY_0HhgbEPiywiK1J-t83CVPsp8qcFfHR7I_BhUkmcCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=j6atzuNoo5mX0sJfxL7Q3UEz92TwqpWTiS_EPEToOBkh8O0ih-_brmxNNq6-8N5G9Z0fzq0aj5sLqHxs5Hbr5hdb8Rphy5Kk5lu9rrUGnzSQ18ifCyOia_H3GfaUocVBQc9sH5zyDFnfDZkgiZWYiQ-F2F90s6EwFYWXhLA1E1ktYFDv_cQ5xhrdmc8nygYIj7TQ8d5q4UMYVPDrRMVBMo0O0cFyactlOtlrVWwXlQKKBDdREuc8uDWZcT76uBBXAjQD3x-DIWoUYTiJ9ggmI8URFCKcTDdQub9KYHie63NrkX1ClsEwr6P1tnxOGCUsUEAoV9DD4P1xY0zvNMMxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=j6atzuNoo5mX0sJfxL7Q3UEz92TwqpWTiS_EPEToOBkh8O0ih-_brmxNNq6-8N5G9Z0fzq0aj5sLqHxs5Hbr5hdb8Rphy5Kk5lu9rrUGnzSQ18ifCyOia_H3GfaUocVBQc9sH5zyDFnfDZkgiZWYiQ-F2F90s6EwFYWXhLA1E1ktYFDv_cQ5xhrdmc8nygYIj7TQ8d5q4UMYVPDrRMVBMo0O0cFyactlOtlrVWwXlQKKBDdREuc8uDWZcT76uBBXAjQD3x-DIWoUYTiJ9ggmI8URFCKcTDdQub9KYHie63NrkX1ClsEwr6P1tnxOGCUsUEAoV9DD4P1xY0zvNMMxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=jwi2UEAzWmrqM_e3H7rrelYy4tabN9pTzoyR2pMoEcJDU-q1St4jI21A9BTKoMI7IEaiKkqO6S6pJ7UELz53_qDKwqcnEw2rj2r1fGWP8af6m9UPq0VsM5UJrVnWKWHKaG5s1FOi4MrL7yg6PsXWb0f-PyzKhghOsWSjC2mjC63viPfqA2MwOcYLs3KN0hLdHJ73LFyHwp9Oyf8Lp_yeABRhyqLDdyfIC31RAEXVB2i4ESc3lbG43FTiM24_5EPYPrJj_inwAIkhmBqr5-0SaON5wZzqI0glaZRh50QMXj-mKh_oaorh4cdy8MLqhVTIpjYYVCwUvrWNp98_0n_NTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=jwi2UEAzWmrqM_e3H7rrelYy4tabN9pTzoyR2pMoEcJDU-q1St4jI21A9BTKoMI7IEaiKkqO6S6pJ7UELz53_qDKwqcnEw2rj2r1fGWP8af6m9UPq0VsM5UJrVnWKWHKaG5s1FOi4MrL7yg6PsXWb0f-PyzKhghOsWSjC2mjC63viPfqA2MwOcYLs3KN0hLdHJ73LFyHwp9Oyf8Lp_yeABRhyqLDdyfIC31RAEXVB2i4ESc3lbG43FTiM24_5EPYPrJj_inwAIkhmBqr5-0SaON5wZzqI0glaZRh50QMXj-mKh_oaorh4cdy8MLqhVTIpjYYVCwUvrWNp98_0n_NTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObBbR6-i5CWair8ouDViO8Cpx6mEGXjVKLyu-3yEXybsx3c0vctnK3TrvSKyFZdq5QKbJLE1QiOx1U0sRJnsJUlMN6DuvLCcYkBAxZ0wM1e2dlpPQ4Ez8wXqx1QH3scJtY9nC0L0cQw0ZRUuTbCwFvdjjbGtPKEdUMbnljfvsk6s3IAt5imZcrC3t2AwNheHtt1IfvvskksAGQS95-4KKQJmweGbKH3wwP_-CZ0kIiJpz37ckpoQUfdPUike4lpIYZA4ZFybIXfU18GSyq1QG0zBtZbuwAExBL4aOjTsAXwY55y4bo07ACPBvZIk6WuXKUkjp6rp_QfPVDlKgNhD7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=alWkKyVXYs-WT9JFzXmLWTp7o5tiO8pe_i20FXvFs3X9aR32Tg_Ptir8Vzj3kidVJ9DOn_gAt1e-Hd_7IZ7P6GsAX7YtBICjgvG_FS_RSiNBC0M7bjHWS-ijFdvpFepkndpsN3Drk7yKGYKLwBDg98nFeDX_gvFzmjZ8JIzPUisUZ_fF8y_PUZ0l7nAnnCkdHXPOCE2Yk9zjypc14T6yk6435VEv92Bsaewy3OHJI75Jp2eqxy2JXdqqa6gJzYY7HcV_9R_WDFHaaKIRcIWl4j0HmomCizIw7g8ovuXBbPqzLnYY-aPtQr8KSeBtNVfzh4aQAFeNvmO6ST2zwn0vyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=alWkKyVXYs-WT9JFzXmLWTp7o5tiO8pe_i20FXvFs3X9aR32Tg_Ptir8Vzj3kidVJ9DOn_gAt1e-Hd_7IZ7P6GsAX7YtBICjgvG_FS_RSiNBC0M7bjHWS-ijFdvpFepkndpsN3Drk7yKGYKLwBDg98nFeDX_gvFzmjZ8JIzPUisUZ_fF8y_PUZ0l7nAnnCkdHXPOCE2Yk9zjypc14T6yk6435VEv92Bsaewy3OHJI75Jp2eqxy2JXdqqa6gJzYY7HcV_9R_WDFHaaKIRcIWl4j0HmomCizIw7g8ovuXBbPqzLnYY-aPtQr8KSeBtNVfzh4aQAFeNvmO6ST2zwn0vyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa5JU7EQ2y-Tn1sNGHs8WGRjkDINIOO0lqdmzwxMykZbPDOXj0A6gFMaLOmlmMhW0e8D-QmV3BkqIrdiY-7aL9DNHMAl9MKcCFb8uTHXJN1Vksi_3h7wXkmTtb4jvSeF2zhd2dFsNTKQk51NWsCqfnDAz0KFA8ey5U4wokOQZC0qsS2IYJTbZQv1SPXeauokgZIXM2cz23faPlByv_eGZqpar3dQawreu2iwxZFzbDcki4-b3FhwGOal45-mlo6uH95DpG18sYPwe_HHSjbeY_Q1t0K05xx_ZlbrbOcGgV3RQyjSStFHYc-0UWu7MUgLArZR9qbcTzMcy4-Gp3ZeCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiiHReUwcHD8JzZMBKgZI5Z0MtUqukl-b8NA6ClQVXMI4VtZiTaa7rdGqAOCMe1ZgrsmATBp77dwAHeSqW4QWQhYlGN2_m71AljwjTaiNKH2IFuogF655jY8mB4Q9BlamDirc35inN8XnX6V_ZEbdM18hBd4b8A3lap2UiogQyoJqgkE5sYWjUwUpoO_2YrddyRlaPsR5L8bmTMRvsfaRIPUDgerXKBkSHREs8cvrNMDS_G4H8NTgZyGbe_qj8chI1InVGyMpMB9oYgxdIMhbJ3DZyGK-ImEyqNoKBBokIJjkN-4yru1E_Mq6waLhA6sgjIhogvwmfYxhXY93GxP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw-0m4rgr3CaLQqZTjb3oBFnIBdAJTkI3BvrdMw6tN3B8c8A5qgQc57O9Lkm18sh8xdtkw-HbAy4M0cUEfGP6F3-N-19HsJNGDfjfMb33DVh18fhT5z5zAf0rPGbNYAluHQo2Jb4bCrpL3Ke-sgtJg96bKdZB1DcXiDzWKpQ4gt4CMLlk7g4UgMsHuct9vWiFOnshzcw-QiwiFkvEHML7eWSi8sFO6ZN4EemVtB9Cs2Tl-3oZJCnUEHYgAwEMiqJN551eYXp7EyO3B9pJZkOrpDhz9OAevW1p0QRorRFhJ83xa6lKWJDcLPQ8aAma_wEHQjqdiDTTJQxJQVfps4CIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV3AgUF4ALXxUm2fvpjozwDKqernk9MKHMBJIjqHthsOrt6-KYVfSU7y8Xjg7RheDUOeKF5hbKGkh00i42zgaybiR5QtNibVL_l1VCcuhbuePOxsMgNZVmHRvTrmtkbLBbOVyznUmBt86_t1GKHI0TqW9LmzXtlt_soaJqhhFzXVgwQfO46m2HCm4vFXkkJLNE1VcBj89oMJ0HK0ZQcRmQefs9tXq7W9OwJVZG50wHdKdVY9Rga3MGUT16Z4JSd9B0BL-Qjmbs3CaUWodA6oZVAYNxLBMcc6wMyaOVdRafckhin3BMdnWDCB5nL6pCGaiHbcPXsOjnBDNAr7_r8AOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr-ZGaDrjymtn1D90gDyezQKR3fDSZQEgl8uBxfQ0Lpzz4nNgSzEu4c6rvKuKQu1fkAmikwR0RzUOJqqwIFAoA5OFGSrDVI-1FZ-kNZmDtHxOtbJiZsM9gv8TMHWBvSsEVc8TpOZiTG_-bMLLJBHzW31sZn0bABdI2kNufaePsENbppdVH_JXf0I09RUlVFmnEBXySJhfrD174bHb66oV7KDe2X48_wORAUufoxnpTBntqDfJErQt9OKFwq6Zn4d82mbY-mQxlWqajQjCBDuAR8z8X-6orObBOoPeDG1d8ZzBTOZ74NFDqm9aVj5zaCRlB5Bp2zLsgKnUUtxR39Lgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6iDgvFd-sqC0u943SGAS2IObMCpjChZRgPuGLHvj0lJHYM6dZQwJ45mDHHiPFVwLxhzxu0RVjk0kFZrzJV-9HxVU8-JaVgdJ2ctMlk38W6s8D4TyDYmirMTPKdFFAr3PWN3wzNLq-RZc6tQnHsId12VBGDnRE4Xy3ntrxZXH6rY8Cr6afpPu5dpEY9h5Of8ysVWQw8kD--8oQBO5NF2kVa_94WLrsXmSisb9UGu8crG3uGCHj8T2mp3gDFgZyCdnGi8L472ZzABP6EfBRcitpioDoLdtVy7P_D9TSSNflgLsT3BleqmehTZs1Bm_Azwh5jsiM9LpKM0EM0IjfZqbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=TcG1YAm-u9yWU4KilYhpDMDTt3nkKLZyrobmCeqL_Yf6lZ3KVuNz5O6a1hiA7d81uUj5zpRuPw6iePweg70w6BXPTEJRPoB5utgPTQvtt2VrOOObeI7dm1kNDp7eFXr1nglOP8ZRumoVhC0DSAbwZ6sJwGTEO3DCvHpHJzCVihQOB5hHjpX8LHVqP_RU8oFY53uPvTycouYCd8SP1CJCWtt11qUXoiRPT7NR3WZQtOIfNPiYTAJntiRLsDuWm09_lA9CL5M5x3WJqBZvuCQTMrdmcxK3IfxLA-ARHop5kUD-KedhNpV5q8J1R0o2PuKogCLRsZv6d4LoY7N61vRxBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=TcG1YAm-u9yWU4KilYhpDMDTt3nkKLZyrobmCeqL_Yf6lZ3KVuNz5O6a1hiA7d81uUj5zpRuPw6iePweg70w6BXPTEJRPoB5utgPTQvtt2VrOOObeI7dm1kNDp7eFXr1nglOP8ZRumoVhC0DSAbwZ6sJwGTEO3DCvHpHJzCVihQOB5hHjpX8LHVqP_RU8oFY53uPvTycouYCd8SP1CJCWtt11qUXoiRPT7NR3WZQtOIfNPiYTAJntiRLsDuWm09_lA9CL5M5x3WJqBZvuCQTMrdmcxK3IfxLA-ARHop5kUD-KedhNpV5q8J1R0o2PuKogCLRsZv6d4LoY7N61vRxBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=jf4XFUJmS501PVxvj7ISziVNRaauIsNSZ0CjvlyhZf7-4Ucab3yn3CvrrcGu1qCGHKMxBpy5qKeNd7Q6L3Y5NN1GNU_W4aSp8os3yYdEYkcavDpf5aV7Xh4lHAcJx8VoXMW8LtjI4Fh8hz7zG1kCbhkX7e627GZVrWZj0lkJnpxlH0wfnMlI9JufznIYkjvaBwK8HkKKAWqzC_OkO4WxhgM-31EnP6UqjxuVIGiSV4VSiAaAZFk09l628zsvDiomAmxOvgu_uoztiHGs25LO9SQ2hEh5gZu_NhWtnF9VpPksL30rhqe4TET29MHNqcbpSg6sZbwope8L-PivkDxWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=jf4XFUJmS501PVxvj7ISziVNRaauIsNSZ0CjvlyhZf7-4Ucab3yn3CvrrcGu1qCGHKMxBpy5qKeNd7Q6L3Y5NN1GNU_W4aSp8os3yYdEYkcavDpf5aV7Xh4lHAcJx8VoXMW8LtjI4Fh8hz7zG1kCbhkX7e627GZVrWZj0lkJnpxlH0wfnMlI9JufznIYkjvaBwK8HkKKAWqzC_OkO4WxhgM-31EnP6UqjxuVIGiSV4VSiAaAZFk09l628zsvDiomAmxOvgu_uoztiHGs25LO9SQ2hEh5gZu_NhWtnF9VpPksL30rhqe4TET29MHNqcbpSg6sZbwope8L-PivkDxWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=KjepMbtXE76yGz65249fGmzXoQGQs8UKwfekYaM45-qoX2BtYSh4oDNeOhtGIAvXcSE2PUl8VHFuvEk73PRY3po-NKqWnqIM6MbNXHozlWX05-6SorIJHmoMlbuQSWymC9-jBD5qmtsRaKbynhOxYQSnliivc985GdbjXeg8_EAYNlDuRU1A1XcuN7AghLptZiG_ev_C4bJDZEaDQX9pLnrYKf4U2Ya-xUx4eIA7wgof20oF6ILM4QHcCHxuu5IP-t7zKCayqumZrGMaGGBujCpSJExOINcBuN2CF2gBStJvn7JgCZh9iL2UNHN9jFZIysuxjbxlVvApWJrM-7Ngfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=KjepMbtXE76yGz65249fGmzXoQGQs8UKwfekYaM45-qoX2BtYSh4oDNeOhtGIAvXcSE2PUl8VHFuvEk73PRY3po-NKqWnqIM6MbNXHozlWX05-6SorIJHmoMlbuQSWymC9-jBD5qmtsRaKbynhOxYQSnliivc985GdbjXeg8_EAYNlDuRU1A1XcuN7AghLptZiG_ev_C4bJDZEaDQX9pLnrYKf4U2Ya-xUx4eIA7wgof20oF6ILM4QHcCHxuu5IP-t7zKCayqumZrGMaGGBujCpSJExOINcBuN2CF2gBStJvn7JgCZh9iL2UNHN9jFZIysuxjbxlVvApWJrM-7Ngfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=GpOYOhs3bvYx6M-vtf_v-Y94eM6ryz5Cop6VLH6z_QNm9LFiMmnDop7ilrA9oAxlWlRuduDhntN0xs6dlOzOKaoupnpDsemL5JeF60ANLOUK29E_8PAZ-YX_7muUkufCc2oXDk1B_XLrXhC8hbnM63qUqVeAnlBncmasnREVNV6JD0TlaYXvA8I8d_mE0L9Le5aZj-W1TIVqV4uI9nOsZDYKnlYLeC6IcoQxPigAihDcyDyw_gGRHt2zLw8nYlndhxS5YeN4XUHLvY3y2SeBWbRf94V_DVZv63i3vLZz-c19b5NE_zuKpZw6foN2t6MGq6iFqtDW6agj6QEyDpex-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=GpOYOhs3bvYx6M-vtf_v-Y94eM6ryz5Cop6VLH6z_QNm9LFiMmnDop7ilrA9oAxlWlRuduDhntN0xs6dlOzOKaoupnpDsemL5JeF60ANLOUK29E_8PAZ-YX_7muUkufCc2oXDk1B_XLrXhC8hbnM63qUqVeAnlBncmasnREVNV6JD0TlaYXvA8I8d_mE0L9Le5aZj-W1TIVqV4uI9nOsZDYKnlYLeC6IcoQxPigAihDcyDyw_gGRHt2zLw8nYlndhxS5YeN4XUHLvY3y2SeBWbRf94V_DVZv63i3vLZz-c19b5NE_zuKpZw6foN2t6MGq6iFqtDW6agj6QEyDpex-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCc1yTDv5XfDZEfc5Yn8lBN8TtC-xZX2mWijs0hv7IW4r0F4fowZJAYvwtzVesbAvtpaRaMrk25cZqV0ynO_yZL-HoQ7RPnXkd_fbl6iIfDb0B_BkfizNU0PaE_edQ4Q6kQ8aHwL7B76x-LUx7bx1XrcVJAob1kUTWBA46qbl2U_NC3q5CXRAUCHwZ3Zd0AJvev-emMjY0xMHOLXPnD1mjgPyPyUXZmkGGKcMt6J5zWROPJI4o_pZTsHHv7RyZrUTQxJ-mJZec2AZRpDoSm_yt4PldNynMmTCbtAi-oWCUAjYbHJPQFyAYG7qBLbo5Lk22bO66XMYUqtubbAliSyAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=OJwAwA5GeNVifqHV0Rt6bOHuU_lZYSbviL8rHw5NdfLbOpvr7dL0S37AJRa2JjRjbtPwMtwNvOSuJOig3jLGPXwGpQ49E3g8aDDAORA-g4Yu0uhXpZ-1T7VtGpiRzd5zLyklvNyv1fCaT47_uvPBbEuJZvhN8K9qbFnZtFSjiBLs6pyi9aOgPsxH_0DyrC5S3SRQfBQdoGLt9jTRSPy-v-dgbLa05OPGrvEwBHsBS8rPvg0kuVDmPBVukFZtgK5q2qqvxCtVeeyM46Zyyt58wsjW6cEV52q1_r1ERJfUrECKjkkWxInoAbnKfClfkPTKnIPTmJOt_IJ9dCKqYjbyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=OJwAwA5GeNVifqHV0Rt6bOHuU_lZYSbviL8rHw5NdfLbOpvr7dL0S37AJRa2JjRjbtPwMtwNvOSuJOig3jLGPXwGpQ49E3g8aDDAORA-g4Yu0uhXpZ-1T7VtGpiRzd5zLyklvNyv1fCaT47_uvPBbEuJZvhN8K9qbFnZtFSjiBLs6pyi9aOgPsxH_0DyrC5S3SRQfBQdoGLt9jTRSPy-v-dgbLa05OPGrvEwBHsBS8rPvg0kuVDmPBVukFZtgK5q2qqvxCtVeeyM46Zyyt58wsjW6cEV52q1_r1ERJfUrECKjkkWxInoAbnKfClfkPTKnIPTmJOt_IJ9dCKqYjbyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq6ASlZXX_04bE_3Wj4Qoiw8Zg4kkVNmTYJi-Kj4ohDvzpMNjv6CnKnIUf3mmAkWRlLceShqfCOS5WOm_3Fm5SIkRkX8AEqNUCtNvajkteEYZlIWmvs_P3IWjQmS5DMhxRL4-T2rdZorLpapVDDztVtIjmBx91dr4X6Sy94iAWUzDkDY0RN4IXr0LRROZUmAvSYkKyB22wiM4rXzriematYoShUUkWaCwRNMjYHuH9TyavESNuhs6tQOoDFvKs5-TVpzUWm1OR8573BzPx84L9GztvAM2Kb9cvOQ985usR_9eyhoRTzk-K5obzK3F8RtqdyAhMPbG7iR2N0MuM-pXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=Z4h0Z1w9Uh72aKWaIgmM1HLOQR9cortB5rjz1xgq2mT-LMb5MNkDinqNmGCxLTF8JGFtV-XHKQSItHZ6J8LhyHHIbCFXKGB-PFYG_M0J2fMnrc47Ysi3lStLhPqKckD1uqqDHipV7esKeIFUy0ybZOYM6LqBXxCBWEQwZwCo4LfQHa4ZCaKEcupR3bXTk9Rj7FdK0Wnf8Tre0otNo0q9RqeJ9_hjg_wb1wS2GD8A_9jG4hL2sg9xGGziduHFuls6LFthzw_M7R30xMn_KXe4mI1_L1_dK5VyMo2WWzhpwR8MG-vIyT1G1A70P5JHniCAmyQmyq2h7tQ_x7GuqP7O7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=Z4h0Z1w9Uh72aKWaIgmM1HLOQR9cortB5rjz1xgq2mT-LMb5MNkDinqNmGCxLTF8JGFtV-XHKQSItHZ6J8LhyHHIbCFXKGB-PFYG_M0J2fMnrc47Ysi3lStLhPqKckD1uqqDHipV7esKeIFUy0ybZOYM6LqBXxCBWEQwZwCo4LfQHa4ZCaKEcupR3bXTk9Rj7FdK0Wnf8Tre0otNo0q9RqeJ9_hjg_wb1wS2GD8A_9jG4hL2sg9xGGziduHFuls6LFthzw_M7R30xMn_KXe4mI1_L1_dK5VyMo2WWzhpwR8MG-vIyT1G1A70P5JHniCAmyQmyq2h7tQ_x7GuqP7O7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=ibOof3-IAyXm9McPQxp5aWb0Q5_Lzomyw2Np4g-ZH5SrGkZP3lRuXgWBIiswkDb8cqeqtQcTsW0CR3XLIyGA7_-2UgNS0gs74KnF6rR5Jg5q8sIg9SkblqmnZuR1bv4tKdE84uAbWVnJi6xawBqjlXmddZ-Gq43MHBVKmz2CHT4IrMC-hX8TE2CASjRxBA52bsOK-BVQi3jrZ5egkF_tiBOCiAtKOd3v-Jc8l6I6NE8lozvi2orkwSVw5dbJVVXqXdl1bsZNvwZVHddrHAwF806fa9lH4Kc5JDOC7wMobeHFbBhx0UEUbHt12wj-U6ZTMj5hWY7zWRPyDZFltPbPgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=ibOof3-IAyXm9McPQxp5aWb0Q5_Lzomyw2Np4g-ZH5SrGkZP3lRuXgWBIiswkDb8cqeqtQcTsW0CR3XLIyGA7_-2UgNS0gs74KnF6rR5Jg5q8sIg9SkblqmnZuR1bv4tKdE84uAbWVnJi6xawBqjlXmddZ-Gq43MHBVKmz2CHT4IrMC-hX8TE2CASjRxBA52bsOK-BVQi3jrZ5egkF_tiBOCiAtKOd3v-Jc8l6I6NE8lozvi2orkwSVw5dbJVVXqXdl1bsZNvwZVHddrHAwF806fa9lH4Kc5JDOC7wMobeHFbBhx0UEUbHt12wj-U6ZTMj5hWY7zWRPyDZFltPbPgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=peuRsmZsCB25p_cszOFiJkB2XFtfKYMR1Pk19FHSG0lJI_NXvFQ3SXqEAw4XPYDdslvIJ-sqVQN07KjNqZbm4eR-IBMInawIFKCUGMib03KvzKgQXjEU9K6OYmn-xKncNt6L81awBIbV3pdfxpp4uGhO0WruSNGTaeU5tvWvH8FkaqfihTnixGe7wmLCPpgL3hUm6n50N2J31BHWyxqOGyqoPYEKWEq_NeWLhJysjLrvrgN6ntlPuxOw3DGh7snIe8mhmLHw3TYe4Oj6qeVwzSAjdrmBE29eWhclcXD1ZmLdu_muvFMHznODuKOs4TdmMAB8CLOg7BHnj5Rq-epOJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=peuRsmZsCB25p_cszOFiJkB2XFtfKYMR1Pk19FHSG0lJI_NXvFQ3SXqEAw4XPYDdslvIJ-sqVQN07KjNqZbm4eR-IBMInawIFKCUGMib03KvzKgQXjEU9K6OYmn-xKncNt6L81awBIbV3pdfxpp4uGhO0WruSNGTaeU5tvWvH8FkaqfihTnixGe7wmLCPpgL3hUm6n50N2J31BHWyxqOGyqoPYEKWEq_NeWLhJysjLrvrgN6ntlPuxOw3DGh7snIe8mhmLHw3TYe4Oj6qeVwzSAjdrmBE29eWhclcXD1ZmLdu_muvFMHznODuKOs4TdmMAB8CLOg7BHnj5Rq-epOJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=bhS1FM4s27rSL1k8g6PFX9ZMjuuXNK3Ak5X3uV7eVQPzrUWAb48Qjnc63En_m7Q-uZSzSWhbMYe3eWAD3tEGthrYnArtJ4GqhBn01YbGUBY_Pc6zCQri3TDL_HXMmNeLETjIBk7lGreEzNWzTyTHqTkyHWN36maa7suTIqc-pMlzCJmBXq6H3-hDVIOTbSaHRT8g7A0E6kLCVpeFZVncqb_zyKdAPyQV1LiECIVHQBGO0ZyYS5QlWSq5oHOIblWubmCral8XTx0jMFYC6RHEQbeCvsmRLO0fWIyen2xmSDzbYOfv3I9f9r9C3_gfTzqm20OeRVpcPtH9DM9lrQAdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=bhS1FM4s27rSL1k8g6PFX9ZMjuuXNK3Ak5X3uV7eVQPzrUWAb48Qjnc63En_m7Q-uZSzSWhbMYe3eWAD3tEGthrYnArtJ4GqhBn01YbGUBY_Pc6zCQri3TDL_HXMmNeLETjIBk7lGreEzNWzTyTHqTkyHWN36maa7suTIqc-pMlzCJmBXq6H3-hDVIOTbSaHRT8g7A0E6kLCVpeFZVncqb_zyKdAPyQV1LiECIVHQBGO0ZyYS5QlWSq5oHOIblWubmCral8XTx0jMFYC6RHEQbeCvsmRLO0fWIyen2xmSDzbYOfv3I9f9r9C3_gfTzqm20OeRVpcPtH9DM9lrQAdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=gY_6V1OaR09tjN2mI8lAiSJV6Kx5CljKdq4R6sOdlkmkjfWd1QjA6CdzFb9TMxBW6m74UIyke9L2QbdVSjd5Ev1NnkMirB5vVcw3IiouIfotAEwZRZXQu4MZtzYYHS2eKLb3q8LV08sjGcfv3N8reC637aq7cBi0-iU8uI9nyOWEzwHqkJDYlUHL99fIjGRzRzkf1pGPb4AZSdZXG5JVjttZxQHt1uy_K0X3sbugEXKdM90U2J_IusbByvBfe_NKbNYjfxxUEaGsjsAFdeINa0u-z1_u6M0sQs6eLRS1fizYK_GO4d8gWOetbkVlg2R_xFK7Dd5NDQQDd4SECghNqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=gY_6V1OaR09tjN2mI8lAiSJV6Kx5CljKdq4R6sOdlkmkjfWd1QjA6CdzFb9TMxBW6m74UIyke9L2QbdVSjd5Ev1NnkMirB5vVcw3IiouIfotAEwZRZXQu4MZtzYYHS2eKLb3q8LV08sjGcfv3N8reC637aq7cBi0-iU8uI9nyOWEzwHqkJDYlUHL99fIjGRzRzkf1pGPb4AZSdZXG5JVjttZxQHt1uy_K0X3sbugEXKdM90U2J_IusbByvBfe_NKbNYjfxxUEaGsjsAFdeINa0u-z1_u6M0sQs6eLRS1fizYK_GO4d8gWOetbkVlg2R_xFK7Dd5NDQQDd4SECghNqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
