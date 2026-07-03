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
<img src="https://cdn4.telesco.pe/file/RL43ruEtqcGwsh9m3dN0nKxVwM1sKBucpSi8Q22f3XoVqENTABM93ujHpiFWU3Y6vr62Z81K1W7xbp4HFFsvbdtucW85XOSjCcKx4B6ujTd8EVszlg0Oub2ZuUVyUbnR-csxKH6izTDLeSkNLbUUca1YQo9kkwcJ-vfz2qqrQsNIgUybYkfxDiZ8ZPCp5kohv-C2Bs_QTFsst3LjjJRYKWy70GCjwaugATcb60toIV8SPHacc8K-9LoeTDWJ7P7xQT1XLPeRZ5_xHCKa3zwNpTGPdAa_yMxNGlIjxXKEQGTWXB3wm-TPhny6RFixkc6TpA22x9hFzIfo7UrfECH-pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 211K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHJ72TPPAe7iW-fBNt1czBEUDqk7nH-AIBEPZtyRNh80PKTGV5QA611QNuBKqCMJ_vZmyrKbFm5gW5RwKdBOoUNBIjOqjizL23Fn0s8lR3-cVADN2M-tMLo-iummAMWOhqvd9DeCg-aoDtPKvAl2hEhbtjNhD6cGsAI5m17Ke5FmP_00xzBRULN45IebrOSPEg7n1P0MGkBXY_v0eM5vo8aRF6EbDT0SCnJVDSMXc03MFOKWYsN8nVI0FVLvtP0pYxhvULsYfCKj3TgjsOX_A8mrrZh8_GwerUOBVlicuVAb1DC4UGp7BjvPQ4-63kSMfRq-q6uxzYbX9ECkiYDM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YjzF9HVK8ZbOHP137q9dubClR7M3XkXPCkf4XJ0ZzzxNbxpFux-Y3e7ZATMpcQaePG8lHmUpjAMe65pVHtm8XBQNAIFJB8_x5y-HMEZgbLkttEgPBE41eFMdG_EDUn9fGPCbxknHVz2jHe7efHy0dj3opG4bOGLM4Mwm4K1z4POZXVJIWSPwjEcVa9fue-vAenptxDwmkFPGDah0e7CwKXoTvZOhExhkpGLhxPeqCdubwLM6RhGW6L2T4SgacHu7weZgk-rHgcrx_5555IgHf4t8gjirYF9MZWLtemLh4z6iBumB-LBh5UKMe032-MIDzAnN_MJY0TY_3icxzJqP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=n9W0VdK0aKH5tpBQoOod4vcXXTpAgbJ4VhFjDI4MaGipCSqoexQ5CgVemzXnZYPogOOV8jYF9xP7bAsOg3euAZ64IdXfZTXqm7a-MRBYeqTLjFHudXqn7jfbhOTDwwKhE7KsvLCHPHfiIXE9hbLIvZmMWfiSxOPCevhlUBL7GiJZlPtsMBHSUKAikgNwXh1bYpFW0KvohnvI3N1cH8aEYhFrrMAtJFa-kNYfTir5D13168A0oyTpdUv0mD8XAYTGlO2IZZQxZnfzycdLAtd0DBmt22uPwTzX1G7gbhGw_Zv-0cpR0LhA63CBYtmL6P68g2zVwD2iS37r5Gi5SuZe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=n9W0VdK0aKH5tpBQoOod4vcXXTpAgbJ4VhFjDI4MaGipCSqoexQ5CgVemzXnZYPogOOV8jYF9xP7bAsOg3euAZ64IdXfZTXqm7a-MRBYeqTLjFHudXqn7jfbhOTDwwKhE7KsvLCHPHfiIXE9hbLIvZmMWfiSxOPCevhlUBL7GiJZlPtsMBHSUKAikgNwXh1bYpFW0KvohnvI3N1cH8aEYhFrrMAtJFa-kNYfTir5D13168A0oyTpdUv0mD8XAYTGlO2IZZQxZnfzycdLAtd0DBmt22uPwTzX1G7gbhGw_Zv-0cpR0LhA63CBYtmL6P68g2zVwD2iS37r5Gi5SuZe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=NK8MRJbk_AFJJIgDsawp0C6uAfs9Fr4hlagK6bYTNMGeE_kpbK9q1lxeeC1k7Qvji5gZ4jDWSamSmzmZOFCG43hgkkLy739wgFxOqY1dUe4raR1s8cFXQXt-VEQW7k9O4_zUPg-mQpIGI9OQAo1bEKQCI1x10TY9aTrxrWTOAj46OBp5rozCUPrs63SptDF9otnz5Yg0K_EeBCXpTEVzV4Se6fuqDlPJeasm8UtNciYhRRBmpbdliZTJtEkcMl31fqUrsvO4xxg8v9PQ7F9vydaRsuYFW_8djtA4s6Fe1oK5pv1h5OQpZ3wJqkBnwp0YGgMC1UU9BC81AmYiVtuwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=NK8MRJbk_AFJJIgDsawp0C6uAfs9Fr4hlagK6bYTNMGeE_kpbK9q1lxeeC1k7Qvji5gZ4jDWSamSmzmZOFCG43hgkkLy739wgFxOqY1dUe4raR1s8cFXQXt-VEQW7k9O4_zUPg-mQpIGI9OQAo1bEKQCI1x10TY9aTrxrWTOAj46OBp5rozCUPrs63SptDF9otnz5Yg0K_EeBCXpTEVzV4Se6fuqDlPJeasm8UtNciYhRRBmpbdliZTJtEkcMl31fqUrsvO4xxg8v9PQ7F9vydaRsuYFW_8djtA4s6Fe1oK5pv1h5OQpZ3wJqkBnwp0YGgMC1UU9BC81AmYiVtuwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=v9GTWsBpyIsFNCMeSuJvDA1cAF-uwnq1UM9VWM5VCsEL24LlZSXjyjZmn55XI9Ms_7-D4ZlPHnGtmHR_L5hZnArGDmcvLuVr__vP8ZJRCO8Nu-LSUYyHI95Ybnv0JWuRW5s28uaWY_uG94fem-pTBZl7U2RXoMQ-KaOp874NYH6BDpHoZHuy1uOu3F3_sy_0mVqVbyPGpfLTY4aEZO6_FnOczirQvAUeuOuBnI1XK5UqEOGEiwes5XQhx8ufUtLNG9HHb7zCyBDdhJ6v8tOcbeIhzFR27LOOLDWRZxfqpKR0UHL8KjAdi6-kMfJBhzP7EH83iW5q6sk8q9-PlB1rpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=v9GTWsBpyIsFNCMeSuJvDA1cAF-uwnq1UM9VWM5VCsEL24LlZSXjyjZmn55XI9Ms_7-D4ZlPHnGtmHR_L5hZnArGDmcvLuVr__vP8ZJRCO8Nu-LSUYyHI95Ybnv0JWuRW5s28uaWY_uG94fem-pTBZl7U2RXoMQ-KaOp874NYH6BDpHoZHuy1uOu3F3_sy_0mVqVbyPGpfLTY4aEZO6_FnOczirQvAUeuOuBnI1XK5UqEOGEiwes5XQhx8ufUtLNG9HHb7zCyBDdhJ6v8tOcbeIhzFR27LOOLDWRZxfqpKR0UHL8KjAdi6-kMfJBhzP7EH83iW5q6sk8q9-PlB1rpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOffS2N7OHGboVmRoeG6o1qoasmi3LzMueLjNYQ3suTViAC_Nk33fyx5hG60ZlwoErKhiEueQLj3YQUEi-faUkM7KZ3baGxeXxFQ5gDqdyxzVurU0mkIabhqCwIuOfjGw-UYbCxgSwsQs7MPI3-YSvaIYwpUVzl8sxONEf3vYIuaKBDeoeCCmpbc48xa1PPvo0OUXN8EmX8KuBr_26dkZlAHJ7yO36QwUWB7vuD4rHLObmcdDlgqynL_RvzQ25qdl2-3oWXaK9SpksxHP6Y-GWjsLm2EbE48nbzdkLJXsijR82jn-TP49MhCdzztfgRfsybLexZUxSqmiLya-1f0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxDX9_bQ0Mrq1PcEnVb1gfqFuMM0pk8xRQZ_m8iqEkox0Kfd6W2GFbXSYYw77Zv15kEp3mH0LfNzdiSZzl-aGteYKpSB_YKcJLAu_S9EsZt4RARnlqNAT_VRevAbTqQ8liZuMG1QM69sfh9pYucmK9w9XYxazJZY-GnIhJKnJzGfQsLLvxDa8TormROnyAdc3-XtECLWDXVBc-kySY0yS8gmlVZfqB6_3N3X7zXZBHOi00TzgzL9ldhe2V55f3aexO5zMXPxJ6rqoC3r3ZirDUG7ePAw7jcPPKWmDF_syuDwdR1VUzH73cSb1L2nlb62uKGyD1smeKtLsECwOM3yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=pv2LIAB3DBGOrYN27pnTjXp5USeXCeEmzjYSy4_XPD-CdYcm4hGybNv_3iHnuBllV2IBVLzTgu08VbffL3WgQslcy1CZU-PxdK6HNvF2wKUCZmDfri6iLQBXXjtqNajjgaI3BcVgnQmh9mPH8MzhzOKX08p3kvuClphQxeEeRoP468O6YYlmuRM0xiNlag90EjPZNAlefH80VcJ8hqsf5WxFdYmmeVUTH5zaT7O6nLaeCJ75m3m4-5rXjUWKIehiNMldwdvnZziK8gVtdd2ysfIj17gOPF3aDLCe9NIum_gszUBbIMB8JNQIeMz3-Cfv5SJD35Njt48uYIkrDbD1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBpInqS1q9i8uc086QuO00AWM5JZZeQoSnPe963lM0DhGUsR8ANd1rsNDE_1CSCqEzKrDhDBcBD82sdhsNN8bwNKte9f7ZdPxKJ1Iv9Sirq7zYNuDjwrJObo7Q8MzuGNyHIufkl3vhQ_QDDoyPsoz5yCeo_KbstF2ERSi4bXJnL_VzcLQ2caYh4Wzo9kTAG1RnxB_YOv6c1Dza4NEuYBlJTxQ4-Qy7_QfoMmdmKCiKkD7fP5vp41X4_5N9Ev07JA933WoyVE5dbkeih0Hc0oMyS3CN8KiLkIpWFT7qrJ9aB4E2Srsvj7YGFfogs5WSA14EKI-af1n_8_yC7sXwF6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=CngbaPnhkYunY8Im3WvkTfY5gNbEKrOBDp6ZSgJC11cQZT6YsKTIZ7oFopU0PCkq6bdYy69fDHi1EuzVGWyIYVRIzO6ssDww31_YTWxMwadyM63IhbO96t3rNiT62V4YzOxvL0dE7xmpeSG3dhHTEzanug2r_Co0T5m5MYNGdk86H0U9wnIw_VemFeFtJUpw01onEvNQFRj6ZjCVDAIE3zEtT_Reih8S1sIwuJ44LdX7vAxv8vC2D4u-r17m4GSlDCW9UcDRbKG3TRBzn5oTh7Jk-5F7Q1VIn1b9s05o8qA3vnZ1I7DCVGefySf8RnK7zOcggmdqTNMLgOutU_7JPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHCBypWj8V1smiqBxI6jysT2rPmZi0ZHfsqPyz6OLnyYWwj6Tl5MLZJNm-uHHTbUX8IwjxVS2_9e7vvw8BXO3s5tGrtjsJKzMAO9yVSsslDKJ0ysKf2THTUV7ak-Gmriq6SayV0wrnLyb0-4fbGZDqXss9P32XUa1kiuccuHi1zu-AhOKLtyI1UWX4mUuWgo-rqheI1h3zc-_I8Z3XlBPvLpxUPepN6cDsrWKqpy7G21MTEgMq-QQs_bav1HDKKBT5v5jv26tGiWu3vj3FM_SQE3qgPhoW_ZGyBMuaSmzdwXCBwAFyqOh8rsXSmu-xWBBUSNBrj7Dgk2FKEWFu-Lag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=XDp3Ij1NbT7gMnodj40QomRka-6UzYZegjAGspitJ-iN9Pb9F_adEKnf1H3jrguNkOB8_TGCDEJiQHy1kgHAK17cqU3rL2jVxyZHL2ckt54QbBs3vjrUjxlqM1tSOf1gJ-YhoaWECZhELUJrOaSs8PpxKu2KUO-gco6NYWIMmAxKp3UeOf_rtXPpqwXCTl9FHYxY_JnUI4kDO_fpaTyqn5wNwyhbWLw06AR-K80fOgg-8EzVGUZGOzq_VJXS4G-H2qBwQttHcNgKykUqnV3E2hLv56h0eiG9H2vRxQXZcFvjItGAawYExUnIrQj9gKASjfZEbgrPwAQ5eKTVzHhi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=PabOKdS_FRrbrp5iOEPr13riN0LqpdrwmtC87WTog1hMDZrDtWNC2Uc1nfZjYZ21jnFc0dw-glZV5xilE7PoqKeFmef_PuEAIEe8MfgnR0BJtKLhrbOzM-EdHqiXKKQjPvEAj-zmNiFpZ_HD1PFCooCd9yTK6Gj7Pr6nxzkRdbVzaWEJHBZ_ku7XMsP_2bl2LaLTRrhpe8qAlYwo_1SsYeSVoDeecMYaf5rURsetRp5xdONKEnjzcYxDSe4wwjFKFDYZH9sfhrKP2_WYp1XqJib03kXxx0gquExEhwPnrMth-ayMFutM-uZ6H6b0rziNMtx0FL4yNdfj8DUXJPAV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vngU-gluAq2W7NrN-XrlXjiU-py6pVm8p2c3OM87UcorsBppSzzd2Bjh4IuEINnOxslNxipm7Hz7Toj-ubB7FodO2iQqg__75eoQxnKI4C8o9PALuY6wByL6jEqJT31n9MkvHUkkpODg7YUif645cp1zfT6XdodH5i_N1DVMbXA6lXbjgCo9-FoNQ3wHK5zSpO_1L0BlH9Qlu5dzdm0UibkxvIoQw8n5RKKvadCFywvT-ayW-9LUccOiJ13ZhSUPB3dkVZavJDp1u8GZ4OVN3Nq-zVnkW_WQ2-9GHiW1Sk7vIyM4d8q-UHOJZbq6NezfcxVFDRqzP5Niqnm_ARJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkW608S4bQ927Sx8P9ZG-VBQ8gLIRWq6mtJiF-qgIp36m6z5abIC-0V5XQBqZeJh2H_BKyBEGMP8-VnuaYWBPGa92faMHtJ2X4UcHv9VC0GeYymbHwoA-GHza2_MahDGSDtmaClsuZqsxb0KIvm8ZQD4Gv4m8PewKRILh1iex5qjYvOvhn9keVzK9Tv5EBj0LHn1lGPLQJtVnoBwdYspEkpiBEnJABPbZ9bN0LtNrsJnyC-xsSRWqhnMOFrgOPywKY4GEJaMdQIn8PjXYkv4i0PmBEZ5XAMzELA4J-7XkcAYAkb6bSvr5eJn8_MVC9xWt7ZWZLe-uYPbnkg6m33_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE9hlzuE6wHxUBLtmlUUvV6NbH-y91Gh4DyiKbA-bCYPyhaIWid_xqSYSIAPHFq0AkAxSZrfrmybelu_zSl0BHGW19P_QIardt4J6kCmOCtaB4GJ3Pxrv8Z3Al73QvpJ2VSZfAtweHZeKtR7tgagRyPZaRS8lZFBARsWedxEyGBPFgtCol7mbV_rx9zq1g2E-mhAoZRqhY6I21lAGl96Nxy-U66ySmFgbWJJtBiMcEgs7xE1FwoCGg4yeClFX8qjGezGXDcCer5C_00s1XIcYa3hE36DYsXftMn0Gw0i2_6-vVnQ7VQ2Ezvomc0eW8jZQNan6tZ4ib0Kx2uui65c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Y-w0-qMmE4R-bjE1WiZl6sQBBIJsxCU8SXx2hSpAoqCn4UWMlbtFeh6FqHlmFxKNPzEtAXC9QJq4fvfW51CMAo7B4KL-ElFTBAkKCPte49vMOapz_estr5akJVmi_tHFpghSXyZuYsD-ZsNKryU0-1S2TpIGBLxf02CyKlJfTGk-cmraq-YB3tFFFN3l-GQgKZyYQnGp8qhMnd9wAXEeRiI0772nOLsAnkOtQvgu13JWFa-wQYiTQrKAhri98angrgg65Pe4dcdAvkX_pllQiS9UgwLGe0dR23KY5zWJwItvjs4n8D0m-Mqi6boMTG-UQWplwfI-Rw0_tKhuWHqGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=pE7s3MJ0sUX-44GGMl94wR6Qos_YZCD46XSW-hvASm2w9SoWO8sQfeqQpLLbwUyjAVifUc0mQ6x-JLScxRHbD98Rh-AhU7h4UhlPj6URmbkKVhBMNLciOgnFfHYsrfqd8qZy4IEtFgK3GqUnnMBuwEWeZm_3wvv5shKqGDgkgKEvyuL6oK0veJCcvrfD96bz0odXgYR_Bhr8BDGBDhSoD3C-2DnW5EDU499PXKRHw3BkrwyX1UVan0INOsYX_WoDjg5HiVcRI8VPoQfvNu5ovnHZ2Qv4fizIWtL21H-JLDysn2TwW3XssDx-hg7F8j8VHrdxd4KMpXxdz9V-9lr15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAqfFfhxhVn0HyNo2j85fM3x8eXHD9e1JhKiDJuyMd9pnD5cuPlma9mnXAR4Jsjb24L1WHYhMpuAa26eFCDNPPGcmyYX-nsVHmHJzMp6324mZO1kqSgWU1kvwPILCFIYEIhcT6QO2xlz-7BcvJancWAUtuDKcDuOfOnB6USxLzrUTts2xg7VWQJBdMxErWaRcfJfJSxGqC_34Dz3wdDt6WZ-skLssiwxytYJclNqMpSXVqrT1a_hTA6jdUvkB81DWpYYDUiRxjweUJqKRz9GTuUP0ldy7m05doS4RHcv0uwYpcLDfbWlziHGjI0H8rU4bkN08kX8ogCJv-7f9k5mdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=j8kU6u2_IAbZRw5MIHapAjBWnh-7BArJH0x1BtiY_9tMZn21s0aCQZ3eBBtGNaQO6WeYC9hE1hVhRGKGcosCte5AzymlvTsaNyoCB3bUl8W-6lJw1Dq5s44IitZeBbg9XDiZlZum5B9ayG315EmOVzsQ5DoM4GoKebK6J_dKFFFWGdajU7gZ6-6HGh2QCqafu9ePSRk2NGajvxKaI3Slbr8gVE_Xoi5Dn5FHIdyDVhoQSuOWPZUYbcmxCfnrLGN3Yqmwzh6SHlOxoVbcg5LxgBsxgLB72ylZvrhPYqbpNl-SBgNAZZ2cjQYNyzahQYnpXcTNtA0SUXdJhnCmLO1c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=EcnLGljOrgt6RTR-0SwNwYsuafcJj96IAL8y_EYFMxGMVByJt1PwVVUgROc_ZK0-dzi8VVmRT2SgLqKk1nJNoVc9SluGekMMDuHAx5sOWWMbmWZsEc3curm_yrCxBItJAIgD7NYyuSHstwAFezhr971mOPTdDCvXoIkBZssgUaXetmJ9_D_EmBN8mV9T3b93pQ5ZI6c2DeHquHReeX0swkGcC3JJaw9Xp02bwgGN_r5pVHP7H9qr_DeuXErutwV6xQxL8QXHFjZmaTlHjgSMRfWUYiXO1isp6pMDiIVBBJ_T_94U9GD-UkDlR61NwpYezJRnfmOCeU0XNjzUk7HzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwcFPphLMY60S4tiaO6pnVWhXxiEmEPfv2-o3TF-ImAep8eXQSe95F0yHuqIfvHjYhb8SUwAM2ymi_U5WqHe1y1PFoQ0u7vfj0QriwCUV5_DQ7gv2_gfkdXt-fUenrv7wtozF0YFYDAHB6_2EgTcLJcvYElwQ5KVc5CkBLnhRr-8E62lUalZLoUgd4KTX_UwEuudw-9IRrUaeMHVkIMbD5tJCywtjL2qFwRtdAFHcuxw_FdYLjGjDfVy8K8BH24UnkGHfnF7myBXbeh73WzI5xuAoRA4Hi8vLFW2YX63vchqr9TWpd7Ow2kbmDV5LcZDlBrCOsFJYXW4fUOlMuoppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=fkHBdigvO9uFgoFj7-3Jg2ANjPZfzFmXVKpm1A3S3Z20hkYjvYsjWutLNxi_rcIB1p5dm-4fA6p_fONmuJiVv1JbHchTb8MVIgeM2cRy428FgqjRQbBFOtF9P8x89GHwYTw6zB8IoysST3AK5uqwnh33YcKRQ14wNM815su4GZUEE4zdqD2xwh5dxsgDF5pOGm1wNoIYMRhoMa5AivZQrGzDMKDli1IOPK-DBAYundZrAN9NktNV9J59fhDhgPob7cyMt_oZHa301LDa7hfY1KoWIRbGh-rGmQIRzXNoy9j1jDctY1e086w1AOq6G7-xbZwvYlAQo6u2vrYudANfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=fkHBdigvO9uFgoFj7-3Jg2ANjPZfzFmXVKpm1A3S3Z20hkYjvYsjWutLNxi_rcIB1p5dm-4fA6p_fONmuJiVv1JbHchTb8MVIgeM2cRy428FgqjRQbBFOtF9P8x89GHwYTw6zB8IoysST3AK5uqwnh33YcKRQ14wNM815su4GZUEE4zdqD2xwh5dxsgDF5pOGm1wNoIYMRhoMa5AivZQrGzDMKDli1IOPK-DBAYundZrAN9NktNV9J59fhDhgPob7cyMt_oZHa301LDa7hfY1KoWIRbGh-rGmQIRzXNoy9j1jDctY1e086w1AOq6G7-xbZwvYlAQo6u2vrYudANfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=SuSQTAqlALwUfm_O-sZZyBjwI0k6KjM48A33DwHoNamnJLEx2QAvNDxLKnB-ABT4_05jesWWfYWqjHhcVh3MNC4MeutZh0kM9JMTBrmv1bfuYfvjNljgKD1EfCWBv7v-8B6YIsYYDsKQgRzNtkgPYxjg3wPmWsnl2g7SPRchQ_1c2hI12Xu6g3bffurxI7nytHsd_1ox_vzk0bYwA7je7EDDkxEhPWPMYNo1r9hZcD6CKl7Bp3A6bi1JGJe-i_7IwcS8dqQ4Z7eCej_TcsVovYUZ88ozpo0VezB17zCtgRhceP7Cs5HXPwz-XG6ewvk1LEhGZH0oQLOFJ6cSE7P2qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=SuSQTAqlALwUfm_O-sZZyBjwI0k6KjM48A33DwHoNamnJLEx2QAvNDxLKnB-ABT4_05jesWWfYWqjHhcVh3MNC4MeutZh0kM9JMTBrmv1bfuYfvjNljgKD1EfCWBv7v-8B6YIsYYDsKQgRzNtkgPYxjg3wPmWsnl2g7SPRchQ_1c2hI12Xu6g3bffurxI7nytHsd_1ox_vzk0bYwA7je7EDDkxEhPWPMYNo1r9hZcD6CKl7Bp3A6bi1JGJe-i_7IwcS8dqQ4Z7eCej_TcsVovYUZ88ozpo0VezB17zCtgRhceP7Cs5HXPwz-XG6ewvk1LEhGZH0oQLOFJ6cSE7P2qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=vyJwtNkuNVMa8-8cS9tnfkZO10JBpDBgE5S2MEDyPAfjl3hZAt_fracH2jrrhlDq522AanIIbcxomWfLrlDvc1MuhLBX7054dPmt6vcSWfRVhIBa2iE_cQZoPXh0gbrOPRA80Cid6-Cecg88W7my53HIrnnAMoa8lhWO86BIVSQXOlES4qcMVaU0b43SX0wbHVMRts7e82GC7DRo6ujYvrYYHJVkVJZhLZRo9BtyC1W51RoOBcvUIYsdybQKiKPyVFgMO-e1ASqg7RZX6FD1U66apeA3EArQXslJDNuOlZzsq6-oioZ1lyL219HjngSDKl7Y9Nrs7b2DNHA7WymzlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=vyJwtNkuNVMa8-8cS9tnfkZO10JBpDBgE5S2MEDyPAfjl3hZAt_fracH2jrrhlDq522AanIIbcxomWfLrlDvc1MuhLBX7054dPmt6vcSWfRVhIBa2iE_cQZoPXh0gbrOPRA80Cid6-Cecg88W7my53HIrnnAMoa8lhWO86BIVSQXOlES4qcMVaU0b43SX0wbHVMRts7e82GC7DRo6ujYvrYYHJVkVJZhLZRo9BtyC1W51RoOBcvUIYsdybQKiKPyVFgMO-e1ASqg7RZX6FD1U66apeA3EArQXslJDNuOlZzsq6-oioZ1lyL219HjngSDKl7Y9Nrs7b2DNHA7WymzlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5co03EYXC2qCEUU4NwkAcSMs2KgZl9kQ531gABP33ZlPkZlnS5RqGSTtG_ovE32elJeGgCyBFBG-pvKKJC18TAUlIPCEGIpNsYRS-fqXD2eLjeNJSKD9mVS0Dv4zlecqSsOJJU8_pQxEgy7A2UACQuzmqPkbFumiXDnmf29Nsir14rdI5N-fmTc4Y-8Oea_IGoL-cYc2LU3TSTiy1AF18UhbGg1ai3N6lkPrHOibkQDz3ddgXb77DdT_rKSynahu5Xl_omb1VLuO3n7d4mG6O2yLZOF48SEaJuDNetM_9DnQ2WrJoYLLar3wMzdaUor0w9LoUcALgUAZkTQw-p3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz0732779nWRs8b2cUuUDWdgS68-oCsUm06cdpwdqBuH2J-k9_sQ248bptz3ss0XZ3qS8ubrSUIU5xQlCV08czd1XAV22JhOH-svqCjDXZ5yEa6PwMj9GPifGIPgCnMy-lPN7ctKHHhirdZ87iaCEl5XnaXvcF6WICObR3uqp_6oBTGzUoVEU8-N66KQ6gjLMyWVneznkxfriPOHHcPvTjPlGNy1klCuA2TdyawvqLjAnXOU_qO4Cgw1XoaHuatHYNpa1b0wwzjPzWBfrslzsqaNYcIleeQD-jSm2XMAI-dBNQmdiMttIkWR3KoZyGXxFxM5XF63yUrZyRGTjXIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBBOnoUSUBBstq2fOjdeHOGIY_eZQi2INYe2FGluG-ULthiTYiC9Ci1Pnkb7HYrWIrPw0sS1aIq04RcC_5KFIPrYSLaC1WASySDx5rlZOPjDlAcWgOcP8ITvKWtUCP674Xq_iLzY5OzqAdeYPDlSNOX7u5I0ZVVK00kjJsZL-EkQvNmyhx3kAWWoY02zy7fUNXHNlVFYofCHa7nWnNwxv2xdGnynbIwH4XQKZAGxYwBcqB6FGaWqz4wqBtcCdN7U6siBt5trOC3qHXndXUuuYjTbYpt8Vor5crXPCIS1FZCsM0FEzP-8-gt4qFNdUArD74V236PijLQHREds8FEYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=gIHQkU6_gh4CbBKVhHiGLgGffQ-Bj5s--Fu9zqEgtWu7fuIsY-KawyMyYTYjt9R_HerDJ2lVpYCQXuRuBhv7epyob1_-AHtUGAATIIyaUMAhuldzB-514ObsusBsywUKA_4gL_Cd07Y6BHhx6EJIJe-eg2F0REa4Wf6FHJORF_u0Mc2A_SU6trNX8lYmewHAfq1QkOyK5v56pRYTA9YVdJ2euq7v9AbZjvHtyXYuXn8jtjAhJsjZxZbmsKP8I1IIRaILi1orcxpTpA9wbDXCHPE9xLiBlYzHxqQbstxTU84sORBBqzThbMMk-rPI3iFUctrI1zJagopLhCJWrA2qOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=gIHQkU6_gh4CbBKVhHiGLgGffQ-Bj5s--Fu9zqEgtWu7fuIsY-KawyMyYTYjt9R_HerDJ2lVpYCQXuRuBhv7epyob1_-AHtUGAATIIyaUMAhuldzB-514ObsusBsywUKA_4gL_Cd07Y6BHhx6EJIJe-eg2F0REa4Wf6FHJORF_u0Mc2A_SU6trNX8lYmewHAfq1QkOyK5v56pRYTA9YVdJ2euq7v9AbZjvHtyXYuXn8jtjAhJsjZxZbmsKP8I1IIRaILi1orcxpTpA9wbDXCHPE9xLiBlYzHxqQbstxTU84sORBBqzThbMMk-rPI3iFUctrI1zJagopLhCJWrA2qOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMd6PvIQtfL95x9JoCWpAxXEkyBUaPtU1jPdhIMcGj3ZEwSTS7MwwsgYR5slKPC8GImtfwSXedf5Pu9SwP4lSXw_AI-V82fpV5zrSywt9D6V4gTblnqgIyn45ldxQWBk93VMFR9yl1itvIqKL059EHXRnhPvJGi3umD89wYe2oXe5C6TEvEq0x4ajj8deUVB5TEOoL5RQXLSz88g_XSJJXZaT-EdeGJe3jOk7qHcwB4MkPlVnBwsoJNKrvu_cwJpIyfK4udfmRjCTELoAXoiETPGOHR9s7GB9dhQ8s3CNQox7Gkt5SksilDg93B6v93Z8oPyqj94r042MbNKKoH_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=OXPs5kwaPPtEKR2gWNOT8ziwzdY7M7I34RuM82zzFO3P8YxhRfu45NnAcYg8u1duJYDFS6gzvBDe_nipjFTgNl79HaNOzhthjaprWcAiGslF36XrXst9lt5wpVJFlAlT51nK_uJFfOyk6NZWB_f22yZxIM6OT2eQSJkVEwSGuWQI_zVdIm3nH7KAku3wJhnI42unHr9iEGjsMdrJKpKRAhZPOPT1ac8JajyOtwYlR6ryjuGJ5J4FGYoiVr2DpYzEG_pkrBStTiph16UeNkTGHzBvdaC2WURQeZg413X25d4pmk8RWvt2idk_9cX2TMM1rN0nC4ANL_G_XQjYtD97kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=OXPs5kwaPPtEKR2gWNOT8ziwzdY7M7I34RuM82zzFO3P8YxhRfu45NnAcYg8u1duJYDFS6gzvBDe_nipjFTgNl79HaNOzhthjaprWcAiGslF36XrXst9lt5wpVJFlAlT51nK_uJFfOyk6NZWB_f22yZxIM6OT2eQSJkVEwSGuWQI_zVdIm3nH7KAku3wJhnI42unHr9iEGjsMdrJKpKRAhZPOPT1ac8JajyOtwYlR6ryjuGJ5J4FGYoiVr2DpYzEG_pkrBStTiph16UeNkTGHzBvdaC2WURQeZg413X25d4pmk8RWvt2idk_9cX2TMM1rN0nC4ANL_G_XQjYtD97kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIMDjFAkbnSqgNKc4hMlkn2Vv9ODgjeQDRgWt_WwZ9XO-Em7uMsE8CcCo-79bRVIgQaaL9REDf1-jhHheG5aiP_qkZxGrwmiqMWgYwhiyHkBnT7_FnXOdgNNuHzbRWoUO9c3VS_1YdoTRU8tQkVWQSWqlG8mhg1qIFHURxZ--ao5OmB4K24MBMCS_A42e-nDfzPrUxW0COTbOm99CE8pczo8pkbEowD2U7sE6roaWdZ95e8k47vNmc9S27QS2I1KWGq_BV3MTBbzonGBJyhl3SfNCsK-B7wU6vV6gmifLDoIzqM7kXr-CMHLWJBmGcraWZYQsa47gTIW01NgqA7img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5xYYid6wqbGSxkz9k1seOj9Oz456HbYJf8U9BQpu7RO6ZDJcb_Ch1mszOIHOHvRucTKTGP-U8dBteQ4duJxITpIzUMjJgBPaL-vwTMrKCyGcDg_VefzNHGHcbi46Da4K6muDmkkIgwjgowCZUbXigj7_Sjwm8ZhPsD0x4t0coDJg5XeYQJu8tDKVd89pxonQHdyD4Xgl8KypNNXR8k11YXxxQHKEW08O11tUorAuI2eGGL1N-_YI_SnEpomsiFjPzxfwYoLV48h9-HQPzFqpqOE9PAuVk8uDO0hgdm6XGBWsw6FxYxg01d6z8V1rpEze09CYOI3oDOr9rBSLnBxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj1s05Lim4MOXClsV_yCgSuf0y3HVjil_maz4j4TceYQLYIPEdJ5TZBa3FeTuS6Ru8AnEiMy5IVhWGM7nu2FW1oRqVwdeBeDYx1dzuPpTxR-PnpYAGjbvAcv4cN3VqNYJf8OALcSB0biOEfoY6a-nHzk8PNWAgy5YEVCoOzy9fjldS7AYAJQUGvRNJhaFdSQYjH2pkAbmo6nfAjWcp-xjayo_hy77xzpX16Z-nm40-pnmJnkrBatpWdAw6C7cCz6chNkpA3Zhme4FpIUIy67shvG7FmUJ1LGX9HY3XwhEWUX3M1l2X-44AT3qyGO-lDY85FlWHisolRr_yRNMiNf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks4kg-7BhHp0n_dQOwxPW5Fmwfw5M6tLi7qarmHKL9aOZOBBCfMvCM-bmfRRomUAMaFBPBqMLPD0yiBlK5X-NSsRGUsPG1BqivDLj9PFNDWL7YRtAdj1jYbX5Q0-Zu4hBwxqWqpe-vRIIUc-CY3h1ITW7UaDBnQS3jlQzE4PYLACv8hUNmDc0MF8t9ocvXe5XmJUvYbSflMnaXiSFdfwoBJjtjqoNI-Ag3HJwg4vhr3Z8yTIra9rZVzaLU7sxOjL0VwwBYoR1_e06f6Ma9vgkCwuhnrb3VFgovH5vcs2km22Gxxb2fTS5gLKOxA-GeZryAhZ6Ch8n3qqhhxhpPCjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=C1vQoOGYEapakPdLD2PWm05sS5xrOVebz3RIYZYWq-SNqZUFknhVxajlo-OFtC94QIerxGt-WrgNCFnORMNReDjJOaPm4piAZbGWSJwcTd0iAE2bF0OI0Jr_cybnCf5NiWykes8ev0VFAlTdCjoGKavVILuQKhNf217Ho1iOxFJuWKsDpLyl7TjwRSbY70I-1V7NvtTze7GcdsSR3h-qznsk1Ll2rH3Q9_gjoCMGr03wyEJriTKShR0dt2mOtHDNFGp9kiU3FBgKFY6YdB0QVkRyHxrYFZqHPucI51jUn1HFVd488vo9P_hBwDxyEF2PYuPEn0RHKcoAo9pKbOX6NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=C1vQoOGYEapakPdLD2PWm05sS5xrOVebz3RIYZYWq-SNqZUFknhVxajlo-OFtC94QIerxGt-WrgNCFnORMNReDjJOaPm4piAZbGWSJwcTd0iAE2bF0OI0Jr_cybnCf5NiWykes8ev0VFAlTdCjoGKavVILuQKhNf217Ho1iOxFJuWKsDpLyl7TjwRSbY70I-1V7NvtTze7GcdsSR3h-qznsk1Ll2rH3Q9_gjoCMGr03wyEJriTKShR0dt2mOtHDNFGp9kiU3FBgKFY6YdB0QVkRyHxrYFZqHPucI51jUn1HFVd488vo9P_hBwDxyEF2PYuPEn0RHKcoAo9pKbOX6NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=Dk89cTjmb0Cho9uVilpWgZUQhPJ9COcLA9N9fnaeqzkz9ri-THeK7_CHzQHVfA3G2ty29IRCfYrZ3DdcZyJBBTYeF4T8mE84g2gpH1GWxZh8Yd-JgRexU7Z36PtPsToxt_F44Q0K_vdaHLwYpySuZ3hlG5uLIYe1keMrSIR_N6PJVwdUkQS5HCdDmNyt9pisi50gTKi9yXCoAzVPLta5SDigxwN7qzCdUyG9zxckx6OYWX9VdS8B06xk89LHlmGZwyV156k9SOLw88JeojRDR9LiRjaiVZX5i77mz8cKu3u_VJWtWin_oW2Q60fMfUXwUdqXetAV8u3lEH9WPMqSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=Dk89cTjmb0Cho9uVilpWgZUQhPJ9COcLA9N9fnaeqzkz9ri-THeK7_CHzQHVfA3G2ty29IRCfYrZ3DdcZyJBBTYeF4T8mE84g2gpH1GWxZh8Yd-JgRexU7Z36PtPsToxt_F44Q0K_vdaHLwYpySuZ3hlG5uLIYe1keMrSIR_N6PJVwdUkQS5HCdDmNyt9pisi50gTKi9yXCoAzVPLta5SDigxwN7qzCdUyG9zxckx6OYWX9VdS8B06xk89LHlmGZwyV156k9SOLw88JeojRDR9LiRjaiVZX5i77mz8cKu3u_VJWtWin_oW2Q60fMfUXwUdqXetAV8u3lEH9WPMqSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gp1JiwqeMD9z-5DfwHQ85NY4Y54PIevWB6s-l0s7vDOXI0qeHHuINqgzJDHTRe_rLKXQ5auhLnjR5IsmeVLanHINzjyPVwVujDfxXq0OHE_fn6GrsyXNgra546WTk7ZLSvs28Un1Wnih6SDCjwelUIopwEN4NRPcm8Zrt0giIAe4JF5SrCzD4HRAKhKpVuznfXHKIlxNbXcFayNu-0YrmGfjxKWQlY4fEnmuWqhbM4yTRaqNalzLoFCKSZacTnMj2mClGpXWESNp1JkPfW_RnAh8m5JVIdmIuK9WvXHkmhkiHC2yjQBDLEEt3uFbT-F9ofeNtpYwowD6AQcRKlF32A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gp1JiwqeMD9z-5DfwHQ85NY4Y54PIevWB6s-l0s7vDOXI0qeHHuINqgzJDHTRe_rLKXQ5auhLnjR5IsmeVLanHINzjyPVwVujDfxXq0OHE_fn6GrsyXNgra546WTk7ZLSvs28Un1Wnih6SDCjwelUIopwEN4NRPcm8Zrt0giIAe4JF5SrCzD4HRAKhKpVuznfXHKIlxNbXcFayNu-0YrmGfjxKWQlY4fEnmuWqhbM4yTRaqNalzLoFCKSZacTnMj2mClGpXWESNp1JkPfW_RnAh8m5JVIdmIuK9WvXHkmhkiHC2yjQBDLEEt3uFbT-F9ofeNtpYwowD6AQcRKlF32A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWyQE5mnwVEpun5E21vndn2IQ61MQ5Qq3u0cz7u9Y3Xw-uunj5eeRamPRPZZaP6U2_BZQ2tfV1yWoJb1OCjM5KZJFZ2YgbXZM-dVrjjDmI64StfNF2pZ95AaQCShm2-bgQBM-AQK5FoWr20_H94VOzwTetE9_qR_lDv7oMyaNYVcn1a8SK84huRACX_RDsdjhQGL6z_ykFDp7-Dgf3g8O6ppvX_OmJ7GAWHXdrxBrlkLlNbf0LFfuolV-nxVdwl3fpyNmM8nH1NmgsUOhnAzsJBdveX-OLCttdkTBeT9fxFUbu8sH4EIi5VLiEcVEzvhSU4l9PYKwfNzw4qte0tr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSc6nVkk5Ifpf8FGz_MyzhPP3V7p6RD1amhz6yA5yZ_1cBm7W5ZrcxvtM067l-0zY0v1uVQLZb3lEwqfbuLckjO4FjKnhCDWKvM_qCCDVwXsQhn4KDVo-KXC_Os9sjzco3OzyPpfQU33cu-juN7XegifjjPr5OkfS-4fq9RNkRV4VpZcUri731Gmy9WBgp8x31s3TrcnGA3_86Gww3pFIIrPhIOzDaxEfHmlek9qElKOJ4JJoW4TiqEp9lK9kTDoXFTKfelPipNMiY6s0CeEqnzuIStt3qbl8YU30_tPT-ulVvLqxF58Ban9_sSDmB1icyKOiWlnYHjoHNGcOdzfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IX_HtTlzzyzXJ6r8e0RhnXYzcJdU8Yt05TSt1kQhZAH7diaMPWz6S458Rx1w-7kJ2UqtfqKpwQduuvBcLmz92UfnJxiybBkUUndMk0fGNPpCdwkFTu01i8fvFIMakbuAws-Uzb3MEJNDLH8s6lfY_pEXUg23H9btDXJxqf9WvEk8HSx3jbWyTX4OVvf6F1y3ZQKpoPkslo3sBrGtLhe9wVWCzuFnq2fvZwpcBqeI_1XwZ9NQpuPJfSvvkS4QidkPK_va9q7nhluzX4b7Ib4ATgjd7Uuv6tvPpcYegW_ehhfRnvnoSiJ_F_gLRXhhvSn6eeX4nuW08pZJkYHRCPStBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=NEVP3n7B9-Ssp2EhDR2bNa2NolbZkzkCexEOa0uCPAM1s4dTVAyyKatMLKwRvnpNRvjIdgoWZAefBjZpkcjjHdg2LB2axKDVVIqf5t3aDNUD1Jw-22A7bAgdoE4E1Bg9O3-CpTxD0osCIGfTYx3ct0fhAKSNWaTPD1V9nffzieaAVX51aH_RVJMQVbC7gp6QDwIFHSjB3SxVnGdDDvGLI0wkdKnIsqWxlylhtmkNkCa1tKddJbKXujvvQlQFOuPaQUZzMwRGF-5fsEFMbRJCoF3fSl__QMQBwD6wzveGLTvvYvkhwNtXaPENnf3TFz4IhSjDaiSAUPlR2nPKVBJNUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=NEVP3n7B9-Ssp2EhDR2bNa2NolbZkzkCexEOa0uCPAM1s4dTVAyyKatMLKwRvnpNRvjIdgoWZAefBjZpkcjjHdg2LB2axKDVVIqf5t3aDNUD1Jw-22A7bAgdoE4E1Bg9O3-CpTxD0osCIGfTYx3ct0fhAKSNWaTPD1V9nffzieaAVX51aH_RVJMQVbC7gp6QDwIFHSjB3SxVnGdDDvGLI0wkdKnIsqWxlylhtmkNkCa1tKddJbKXujvvQlQFOuPaQUZzMwRGF-5fsEFMbRJCoF3fSl__QMQBwD6wzveGLTvvYvkhwNtXaPENnf3TFz4IhSjDaiSAUPlR2nPKVBJNUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=mjxKLSPRa4faewki8mmvPm6m-CTBAg-DFuK2FHHE_cN1THN7owYeE4azrIKIaAbmskNUSvjRKsFSbGakWd1Peu74y6pTnkzy0qhUFuK9KsPKlwIMtUYM9RmElZ16T6XPTmn30ZVGS2XV6iBdRsaca_SWFgwiIr18az2FW9oo87-kwAkiIQqnU8LEVR0JVvzdGhtrk6W-la2n3USIeqIMzCQ66xYwkZfwe7x690PGhRDjFFgudv66veX_6pvdpu8LIHMz0NnRA6nUDftbZPkGXhSLLRkElnH3APGd5ymsiifTDR3u9QSyYFYH9vnvg5ZZlBGGhnrqLsPNjYLbpLiNzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=mjxKLSPRa4faewki8mmvPm6m-CTBAg-DFuK2FHHE_cN1THN7owYeE4azrIKIaAbmskNUSvjRKsFSbGakWd1Peu74y6pTnkzy0qhUFuK9KsPKlwIMtUYM9RmElZ16T6XPTmn30ZVGS2XV6iBdRsaca_SWFgwiIr18az2FW9oo87-kwAkiIQqnU8LEVR0JVvzdGhtrk6W-la2n3USIeqIMzCQ66xYwkZfwe7x690PGhRDjFFgudv66veX_6pvdpu8LIHMz0NnRA6nUDftbZPkGXhSLLRkElnH3APGd5ymsiifTDR3u9QSyYFYH9vnvg5ZZlBGGhnrqLsPNjYLbpLiNzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=HuZpOpEedwjcSAOqXGUnKgRzJEsPdqlHQ6U50F0XqIheFG6oYBjz32au1AktI289Z_S_apDQd3hwKavNdju_2RR3zyEvhdocSaKmwLWKtrG89jMYp7BPAl5NEdmYdFoIWgBp-JwGyubYhMdbw_P2hiJL5wI4khNt_v2d4PFoEXp8sog8fswwPiYzkPbL3EHo-xdL-UfUrv1JbqWPMcA37uYgyaeDZlKAuygWnLnnXMSpJ5xojCw4-i7SS6W9_PUBS-kEpqMwBBBLH03jU7Yfu1gYqbl4eH1V2SkcPIWEd0Jc9wLnCY4kLv2XHu0A2ebYZII1KYMOUJHMxeOm5t2enA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=HuZpOpEedwjcSAOqXGUnKgRzJEsPdqlHQ6U50F0XqIheFG6oYBjz32au1AktI289Z_S_apDQd3hwKavNdju_2RR3zyEvhdocSaKmwLWKtrG89jMYp7BPAl5NEdmYdFoIWgBp-JwGyubYhMdbw_P2hiJL5wI4khNt_v2d4PFoEXp8sog8fswwPiYzkPbL3EHo-xdL-UfUrv1JbqWPMcA37uYgyaeDZlKAuygWnLnnXMSpJ5xojCw4-i7SS6W9_PUBS-kEpqMwBBBLH03jU7Yfu1gYqbl4eH1V2SkcPIWEd0Jc9wLnCY4kLv2XHu0A2ebYZII1KYMOUJHMxeOm5t2enA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=XwvpRQFtdEZ2qdvoRnLxfXh7uHi3_ndZRy8rpzPtOMoVYVQ2FpUjkvMGzuvokF18qIOEBr9CRMEAiTc5az2Dt3q9OPoo0f81fTzHxctVqrY0HxK-WGVLDr45FE80bM9UuwDn2AgcwUAdbXRnfc0bKo7m2hIzDNSH4x-aRshmHaWsqLT1iskwmzPzE4AkyX3gczMNt3DK4dNO9gfeGxdCyREmihXqvOm7dnlf_CP6lbvhqvWCQZcgX3lSm71iKhHNvi57VjDiFjZb3NkRhgaxivFd0-BQlOrDBKRLPQOvcIPuOvmGenw8ih4v5FL68D6-5nxH_4qQJ9IoKFJELfR-5FgpcrRzJYilLa5OLwzgUwCk1tRLwJVCx9K1ANP4sbnIqdtoCHFuZ1zm7eh-FLtLyy1L75XjarJPp-tLAHhCngyp2-DNnWlNzQxLq2ldnsERsiXE_Y7W3aXji8oydnavYg5Jgn5lHTnw0Vckc0D4z3cziLrAq26GYyEzKaSnVv9Ky7LX81Rbaw1JGAVoP-M0x62ZVL37V1h39yuMWOMy5IjUQ32Z2TvC2kuGICoFAW8_eV3IZVmcZzLa4STUdgJ4N0xvzg9fnPbQ59w5v6A3x9xVw0vFEt6vXqC6dx7gv1rWFMHRxRISP3PXjAzTsuIZtc2IHgzCPe2kzxmzgAvrp_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=XwvpRQFtdEZ2qdvoRnLxfXh7uHi3_ndZRy8rpzPtOMoVYVQ2FpUjkvMGzuvokF18qIOEBr9CRMEAiTc5az2Dt3q9OPoo0f81fTzHxctVqrY0HxK-WGVLDr45FE80bM9UuwDn2AgcwUAdbXRnfc0bKo7m2hIzDNSH4x-aRshmHaWsqLT1iskwmzPzE4AkyX3gczMNt3DK4dNO9gfeGxdCyREmihXqvOm7dnlf_CP6lbvhqvWCQZcgX3lSm71iKhHNvi57VjDiFjZb3NkRhgaxivFd0-BQlOrDBKRLPQOvcIPuOvmGenw8ih4v5FL68D6-5nxH_4qQJ9IoKFJELfR-5FgpcrRzJYilLa5OLwzgUwCk1tRLwJVCx9K1ANP4sbnIqdtoCHFuZ1zm7eh-FLtLyy1L75XjarJPp-tLAHhCngyp2-DNnWlNzQxLq2ldnsERsiXE_Y7W3aXji8oydnavYg5Jgn5lHTnw0Vckc0D4z3cziLrAq26GYyEzKaSnVv9Ky7LX81Rbaw1JGAVoP-M0x62ZVL37V1h39yuMWOMy5IjUQ32Z2TvC2kuGICoFAW8_eV3IZVmcZzLa4STUdgJ4N0xvzg9fnPbQ59w5v6A3x9xVw0vFEt6vXqC6dx7gv1rWFMHRxRISP3PXjAzTsuIZtc2IHgzCPe2kzxmzgAvrp_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=KA0ig3VV572kEUEpa9l4NwLyHtzoL6l-EWQEVFFq-poYPrpxbnaJzvRuncKZo9TNDo-q6BfWnq9-FlQ9ce_j9gMC8m_SonBJ9N6GIE8pOPmX3M60OWmsJD4t4-QSZgyy0WNtNAiuoUgB1N15xoRdfRoIgZyktZSE1FvMYAFxA7MtPKXqLHr945Omutb_gq8epADGEipgRBiU5jRJkARcj1YMB-pfLOvB58DHs7pMGp6oZksJMLKZZfye8iwhuEWhMZ_4VM0w-dijEyRRroSIqkTGXWACZcFt6tcgvwWNw2IGdHW9kE1mHUkpFJHqkDBEtND5pZWCfcYCS3m0Dn0ebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=KA0ig3VV572kEUEpa9l4NwLyHtzoL6l-EWQEVFFq-poYPrpxbnaJzvRuncKZo9TNDo-q6BfWnq9-FlQ9ce_j9gMC8m_SonBJ9N6GIE8pOPmX3M60OWmsJD4t4-QSZgyy0WNtNAiuoUgB1N15xoRdfRoIgZyktZSE1FvMYAFxA7MtPKXqLHr945Omutb_gq8epADGEipgRBiU5jRJkARcj1YMB-pfLOvB58DHs7pMGp6oZksJMLKZZfye8iwhuEWhMZ_4VM0w-dijEyRRroSIqkTGXWACZcFt6tcgvwWNw2IGdHW9kE1mHUkpFJHqkDBEtND5pZWCfcYCS3m0Dn0ebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=tw_-SQ9Njo6J5EF6rSAzePd8nUag6jHSzvQx-WhOKdZ3PNn1dMfwQnmOmnQ--nbdzQfiX3kOiw4Y2pluaiit9AnZ-AMRikYV1JbdnbeALudoq4nwZYG9BpO4COrXjJqYR6ON9FBNs-ffBFChKRL1BsMjZ-yllXOb1u5cTNAqwonOTHenf66FZ9wDcBQ8bSBqHGYuxZERDRYjidnLOaAIBm4I9ijFNYO10l5A772DlOnlGXrbQG7WwpF2C6QvEVYC3pljHTbQi2ijCPcmVKelxxMsj6Y1EYrv768ppzNI0fSy5BxyIB6cqWmPudDVEPA9-V4uXmVdPUqD1RjW3VydtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=tw_-SQ9Njo6J5EF6rSAzePd8nUag6jHSzvQx-WhOKdZ3PNn1dMfwQnmOmnQ--nbdzQfiX3kOiw4Y2pluaiit9AnZ-AMRikYV1JbdnbeALudoq4nwZYG9BpO4COrXjJqYR6ON9FBNs-ffBFChKRL1BsMjZ-yllXOb1u5cTNAqwonOTHenf66FZ9wDcBQ8bSBqHGYuxZERDRYjidnLOaAIBm4I9ijFNYO10l5A772DlOnlGXrbQG7WwpF2C6QvEVYC3pljHTbQi2ijCPcmVKelxxMsj6Y1EYrv768ppzNI0fSy5BxyIB6cqWmPudDVEPA9-V4uXmVdPUqD1RjW3VydtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjaBdCKujJz4_8csg_3CsIhUQwEWCTQB1Ntqin2EGBYaOcJxi0kYZQsIcLjBwOf0hLVQlk13JTIA1Gg5HFL50fZmUjC1VoUlJt5LpNYpN0rlmiLVw6mCs8ST56vHUsW-YFYq8mB-eHagFcM-Dlv_LLKX8wxSsydh0C8lwoRqn0JfW4qCV7wFXMvJkalqH0mQKLzt3e9yPwdD9E0EcNhKz02TrTvyGTP6eC3ouxZGC0Y-p3iG4HwwXNo_kiTc-Sl6W8d5CALuIQSMYrNqnKQGOtbXS0s0TDC2jb09K5igezKI4UHVtb3rcaweQ3x_gKa2EnRfbYiHkq5OWpCY8T4kDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4U99FC94T71eQccA22khf2JSZXr5gmTDFKX2XkH3XN6Yeq4ETrHP1EnQ97z6721nzS2iY0IitRWV-C2YmjOsE78fyIcxQHirQepcbDrtma5xOr5w7aiKp5x0gYEkEJykAyKxKbSVST7psWgnJ0H8-DtAWOQolDS_3xX55KxC7lTFsdodvGe5eLj5KlGbyrPykSLAoZ0X6SyBaDMTBrCoom6MqcvTlomOMpRml5M6sSG_r2mBixtBxFMaM7ev4D06oK4pKA7dmsz2myRGYgZp7PBkO0Q98fRADwB8Z_HOwkup5vjAMA1R3eIx6Mcjit_AuzSQkb_SDWuZiVyS1BGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=nJ3N9gBUb2KsJpfKU61JSAGSoNTBXRYwJ1c9khnnAMleH778vZ_crnFBvhdEwevEpIyZREQTaOtBKGcMkYImocVRCTvpqeGCGuHb5PuDvyur-1UxiEtuXGeQa_B3ZJEThmMy8Vkg9oTLKsIX36R44sM1v9-9BD2Pd9mR1EQwCuVzGZAjJEefRTo3PuOVKWYtbzfwUqocIz3BKMX7jIoFoo5wbsHvvR2A7TNIREcy2h1aw94b1nTH5OidbfxMGHrKfUoJbGNqgzVDfFRv_nKpmbXvvOXvmF9w7qW_1lhyW1xEzYwlFT7VotUJAosCwQXaQl810PNlarwKJlasxa_dwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=nJ3N9gBUb2KsJpfKU61JSAGSoNTBXRYwJ1c9khnnAMleH778vZ_crnFBvhdEwevEpIyZREQTaOtBKGcMkYImocVRCTvpqeGCGuHb5PuDvyur-1UxiEtuXGeQa_B3ZJEThmMy8Vkg9oTLKsIX36R44sM1v9-9BD2Pd9mR1EQwCuVzGZAjJEefRTo3PuOVKWYtbzfwUqocIz3BKMX7jIoFoo5wbsHvvR2A7TNIREcy2h1aw94b1nTH5OidbfxMGHrKfUoJbGNqgzVDfFRv_nKpmbXvvOXvmF9w7qW_1lhyW1xEzYwlFT7VotUJAosCwQXaQl810PNlarwKJlasxa_dwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FnD6qi6qtyP-roxLM_oKYqj6ypPHOmVxpyAPbTJ9k8jL_pzU4v9xRjpprUe3OObk3MbsEPQ_1eejihl_aVJXgts6e74gmc6ylgXEBI81TOgNyF-hNv-MI_Mp1m1hFGrfjI0faKYPiccixKLSX8xqzXwaF3NOTdjQQWUiRl9NgVxcV214E7xlNZrcHmQswbVNe5kWdZ4JnZGZc9k0UiXOCT22uCtXaj8hPX2HJPM3h3Q3ECua1L33UPHzTgGGL2Jtga1sw7EVnyNnL1guB9QalGnUYDl0Y-cMFz0l5nB_siEiyFlntgO9jOovrxzrXSl89xTsTacVE5O2rGsyXx79uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FnD6qi6qtyP-roxLM_oKYqj6ypPHOmVxpyAPbTJ9k8jL_pzU4v9xRjpprUe3OObk3MbsEPQ_1eejihl_aVJXgts6e74gmc6ylgXEBI81TOgNyF-hNv-MI_Mp1m1hFGrfjI0faKYPiccixKLSX8xqzXwaF3NOTdjQQWUiRl9NgVxcV214E7xlNZrcHmQswbVNe5kWdZ4JnZGZc9k0UiXOCT22uCtXaj8hPX2HJPM3h3Q3ECua1L33UPHzTgGGL2Jtga1sw7EVnyNnL1guB9QalGnUYDl0Y-cMFz0l5nB_siEiyFlntgO9jOovrxzrXSl89xTsTacVE5O2rGsyXx79uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=EELnTJ47HTegBI-1F44wTJsScZwo7pSV292spDfBWSOHN3KXJGEFgVYD4lZDV9oluubfNOlbdP-UcJIxD7xr4KNbqxhd9dwEbojqH4XMish_M4vlQCM0EYrUmkFWXuDO61TmCxQGs6wFR_bqGZ3moSA9yG6_tgBWGbUrjOylg1SS7tlZpgF65KCqKPDvwK4cbcHtKQZqinfdQH_sPIBVZ9c1U-H562lfbxNJpdK_bd72zsl1EKDPGDZsVhCCZYTBP9Eq28z5MbMudk98Q8KXpga8qtdmO7quSKmX69gmHJqAbodc9NCELDL6kObKH-J8KTKQ2mVeqTZLqxH3P5DMNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=EELnTJ47HTegBI-1F44wTJsScZwo7pSV292spDfBWSOHN3KXJGEFgVYD4lZDV9oluubfNOlbdP-UcJIxD7xr4KNbqxhd9dwEbojqH4XMish_M4vlQCM0EYrUmkFWXuDO61TmCxQGs6wFR_bqGZ3moSA9yG6_tgBWGbUrjOylg1SS7tlZpgF65KCqKPDvwK4cbcHtKQZqinfdQH_sPIBVZ9c1U-H562lfbxNJpdK_bd72zsl1EKDPGDZsVhCCZYTBP9Eq28z5MbMudk98Q8KXpga8qtdmO7quSKmX69gmHJqAbodc9NCELDL6kObKH-J8KTKQ2mVeqTZLqxH3P5DMNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBwVRB_FwXJ54HJ9xJLZACRHXiBEj0fmrSpuzPp2rgHvHY2uHDAkhNxRdgG25KF7-sYz1-6l6OXzFhfBJ8ZwV3o6-qnwIcdmRqr9yqXh1PjI-1abtjmS-6DzCPUREYPgMwPMKGvq6E6BU9rVUWA2PCVmcqEVbYvAJp8e8wkFRINS9ndyAFfP-yKimE1Q3t_X9qcQ2i6fEpG1mD5I36xj2XNh1b-u9JNHlUuCSXQMaRPlz51I5r_b_ZXlL2m1kA1IBI9wZrHsn-ZbAIUR72SbfNlI2TD_u-vcLC7u0Jp0enelGouL0pF0vG73SnJreU3W2YZrb2z-KFoPfuh7gCTluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=qgRybw7nerDK8zPI9qN_YpyJF3QKQCIlgkWVvq3-ajD14PEU4Hr8zAIMMPrNCWazex9RTBx6ihd5J63waG3eYhBnyp2PjLPUbFmxIoQKsy5ksaLaWI-DOXcSXpSNBt2gidXDdyyLDdgKekh-TbwNw2U1SxcVb0lYfbTkbF2yrFZi1rkHaor9tXqTEY6LUzkGlu7m_kp-HQ229GLtUWw7eg140eOK05yoF68DB0l9Y-Ceze7UNcRkl89M36C6Qa_-FDs7CfZHlWOqikGrt2_vOaFcOi-bV6ptFRa-UlyZeejHDfP_s2o8nZ6-Ek00KsGkLVEnjpyoyOyKcRoTBRVCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=qgRybw7nerDK8zPI9qN_YpyJF3QKQCIlgkWVvq3-ajD14PEU4Hr8zAIMMPrNCWazex9RTBx6ihd5J63waG3eYhBnyp2PjLPUbFmxIoQKsy5ksaLaWI-DOXcSXpSNBt2gidXDdyyLDdgKekh-TbwNw2U1SxcVb0lYfbTkbF2yrFZi1rkHaor9tXqTEY6LUzkGlu7m_kp-HQ229GLtUWw7eg140eOK05yoF68DB0l9Y-Ceze7UNcRkl89M36C6Qa_-FDs7CfZHlWOqikGrt2_vOaFcOi-bV6ptFRa-UlyZeejHDfP_s2o8nZ6-Ek00KsGkLVEnjpyoyOyKcRoTBRVCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=vQmD5jQTmb-lvWA8EVmoH4TPZxTkl2wxwNmt-h7rGFfilc4Contl6tKz9KPJ_JHpOcsRyuunVfDkknXyV6R-F00BJhvJTK2Dw66NZU2FWzqkUNEGxS5OqOtcMPlquI7CRcBZ_oN3vn3iBi1g3rH3w3XJVU68KYniRlptwJqs5QimNzt4vBjz6fvqbQZiht0rnUg69zVMbMr0N_lokrLzdlQDttXEY4vW9M2c0J7TMAMydA5nLcdnu79IESRNMx8Zvbk5FJxMRAJfJ2PMQ8Zr5RhULv41DCrFB2m5DGUvFcfP_k_PMkKsuRov0wMxEYLTUjbfhruTdYICFVcvSDGVkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=vQmD5jQTmb-lvWA8EVmoH4TPZxTkl2wxwNmt-h7rGFfilc4Contl6tKz9KPJ_JHpOcsRyuunVfDkknXyV6R-F00BJhvJTK2Dw66NZU2FWzqkUNEGxS5OqOtcMPlquI7CRcBZ_oN3vn3iBi1g3rH3w3XJVU68KYniRlptwJqs5QimNzt4vBjz6fvqbQZiht0rnUg69zVMbMr0N_lokrLzdlQDttXEY4vW9M2c0J7TMAMydA5nLcdnu79IESRNMx8Zvbk5FJxMRAJfJ2PMQ8Zr5RhULv41DCrFB2m5DGUvFcfP_k_PMkKsuRov0wMxEYLTUjbfhruTdYICFVcvSDGVkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=M2XVhVCiNZoXrX4Yi819yVnrkpDeburHcFW6tYDK-ci9d1M0EX6NtswRlhn-RAhsvf1L-iStqQu3chgw2q3JurxRIrLvZjzr6E9PxYookp5NVJZFrJdHgzQ8YNe-bRoBXiwfDAnPd0BU-GYEx1Q2z_qO-Vi3lU5Ph0_YsLW16Y_lZLy-4i3Q5cmrusKm0Kfjn-qELT5OFQcImCBHo8xVRksgk0un3b7rKdT0b-3CFecM3NQxL-eYsie9oyykGZhTmlXiQLa1kD3xSCF8AqX5csojW2SqLRZ8VbHpaZlnjKVyjXmwz0PLQ-lJX9Xovms2upo3mgp69KqciYbmX0Ci-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=M2XVhVCiNZoXrX4Yi819yVnrkpDeburHcFW6tYDK-ci9d1M0EX6NtswRlhn-RAhsvf1L-iStqQu3chgw2q3JurxRIrLvZjzr6E9PxYookp5NVJZFrJdHgzQ8YNe-bRoBXiwfDAnPd0BU-GYEx1Q2z_qO-Vi3lU5Ph0_YsLW16Y_lZLy-4i3Q5cmrusKm0Kfjn-qELT5OFQcImCBHo8xVRksgk0un3b7rKdT0b-3CFecM3NQxL-eYsie9oyykGZhTmlXiQLa1kD3xSCF8AqX5csojW2SqLRZ8VbHpaZlnjKVyjXmwz0PLQ-lJX9Xovms2upo3mgp69KqciYbmX0Ci-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=D22FJEhiHO5ynsKDvKlgkGmtDXwl59e222839dQAgHPXZcQ3TWKEm2Fz8RfUqV6LY2W9rHNVLS-vEcPdlHhLROBkDlhJCSKewOfW4yXJMaBQ-ES85xwem_sX8qBWsPBvc6-MKeVw8U2KWy7hETdM9wBPe-HUwbTnSD6F_6uFSMmqyoaWEgWuWVohdDlzPXKt4zWi3OZ574YPMgvGunWw45fBzXI_ubGiXoLqcgIzr3hIlhdv6O0gIoPLRZOUcGjpfIWz2e4pAZaAuvpbHnKb5Oj9OL6z-9xVACpnbDwE6iKVIbwNp4PbqDhOpd6Y1ZhD5J6TbRokozvzrt8Osi8GDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=D22FJEhiHO5ynsKDvKlgkGmtDXwl59e222839dQAgHPXZcQ3TWKEm2Fz8RfUqV6LY2W9rHNVLS-vEcPdlHhLROBkDlhJCSKewOfW4yXJMaBQ-ES85xwem_sX8qBWsPBvc6-MKeVw8U2KWy7hETdM9wBPe-HUwbTnSD6F_6uFSMmqyoaWEgWuWVohdDlzPXKt4zWi3OZ574YPMgvGunWw45fBzXI_ubGiXoLqcgIzr3hIlhdv6O0gIoPLRZOUcGjpfIWz2e4pAZaAuvpbHnKb5Oj9OL6z-9xVACpnbDwE6iKVIbwNp4PbqDhOpd6Y1ZhD5J6TbRokozvzrt8Osi8GDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=gwz2S906FP8rCzxWKpXsjh7RnO6e4AkPTYY2h5v_ccB_FSBkwn6aPMW9EEGmRqSuDOa5wYFDYJXvED4Q32BoUdy8zcWLN7DJ4tBP6m7uXQzrttMq_KP7KXVyXlCmFn4KMeA821oD8_a9q5eRx855BSMoICXPsvnfcMn9DhzgsKgTSv9PTwpZb1CjoxXh7-gKS3b4vLcWWKOlsL-lZqhRUDw6a3bvG_axQlCS32d35vW50FYNWy9R1fu3QDXgiavJEJ7aQ0SlWuqfyuQ8deui-t74KHtRedUfZgdJQ2dSqN_wiHVd-pupf0M8Ld77AKUlT-zuwqwQb4uo4KSQYld5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=gwz2S906FP8rCzxWKpXsjh7RnO6e4AkPTYY2h5v_ccB_FSBkwn6aPMW9EEGmRqSuDOa5wYFDYJXvED4Q32BoUdy8zcWLN7DJ4tBP6m7uXQzrttMq_KP7KXVyXlCmFn4KMeA821oD8_a9q5eRx855BSMoICXPsvnfcMn9DhzgsKgTSv9PTwpZb1CjoxXh7-gKS3b4vLcWWKOlsL-lZqhRUDw6a3bvG_axQlCS32d35vW50FYNWy9R1fu3QDXgiavJEJ7aQ0SlWuqfyuQ8deui-t74KHtRedUfZgdJQ2dSqN_wiHVd-pupf0M8Ld77AKUlT-zuwqwQb4uo4KSQYld5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=JwmuWgGczdGkkq14m43LUvFVZq-0ut4NoyhCLsfUiu-e9OjjBp_s8xwdzes4KUsx2yvuS9a7P4Db-Jf_aG2BSPHy0vNGvvBpmuyDdzmwprgW66mqs2JxOmexLvRiiV4VjRvIa5RGgDV6v69oeLjF5OkX-EJ7VW5qSUfpNyb1lCc9ni_eafUPf9dNI0VNHs-Onx3tW7cgE4JPbUwy0KZznRDlyUYZYoWilYXf4nrvcM-wkoMHUh8mQHS5EQ8zq-w1dq01aPd83f8SCAx4TiYmjvMegzUzzsoR1nYS7IGD6ZVJTHsxN0xYzvmrYbkeL5jjIZ1MAkPUsiM7xaOglw5H-nakI_dvqO7d6QnKV1Ml7l-EoFV4MUHDskR7bcDnMFR9fvs7I13FGE1FVsQeCosTS7WyPfFzUbu2ZDzm_s81_jhiTIxC_LwlAsIwNIt83MPOnUHFWiEQAmhV52pEJlcJ2k1N-budhckgoEV6Yo3P-4LBTYA0BZFHPzbXfy9oJaJ4vZC-A6jH8JmdpthUiwPa6niK1UcE1sIUTHra7FKnoE1ecz8d8wPUZYW8zJ3w_zmISMgHTRNiyBJkT0WjMRwNDa2rS8agK2Q0i2PH9XrQwD-E-ll22V4-a_BltBnPGz7XDmu-uQNhqcf_vGF-Eu_gMwq324XEMZWmuPLFW39Qr7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=JwmuWgGczdGkkq14m43LUvFVZq-0ut4NoyhCLsfUiu-e9OjjBp_s8xwdzes4KUsx2yvuS9a7P4Db-Jf_aG2BSPHy0vNGvvBpmuyDdzmwprgW66mqs2JxOmexLvRiiV4VjRvIa5RGgDV6v69oeLjF5OkX-EJ7VW5qSUfpNyb1lCc9ni_eafUPf9dNI0VNHs-Onx3tW7cgE4JPbUwy0KZznRDlyUYZYoWilYXf4nrvcM-wkoMHUh8mQHS5EQ8zq-w1dq01aPd83f8SCAx4TiYmjvMegzUzzsoR1nYS7IGD6ZVJTHsxN0xYzvmrYbkeL5jjIZ1MAkPUsiM7xaOglw5H-nakI_dvqO7d6QnKV1Ml7l-EoFV4MUHDskR7bcDnMFR9fvs7I13FGE1FVsQeCosTS7WyPfFzUbu2ZDzm_s81_jhiTIxC_LwlAsIwNIt83MPOnUHFWiEQAmhV52pEJlcJ2k1N-budhckgoEV6Yo3P-4LBTYA0BZFHPzbXfy9oJaJ4vZC-A6jH8JmdpthUiwPa6niK1UcE1sIUTHra7FKnoE1ecz8d8wPUZYW8zJ3w_zmISMgHTRNiyBJkT0WjMRwNDa2rS8agK2Q0i2PH9XrQwD-E-ll22V4-a_BltBnPGz7XDmu-uQNhqcf_vGF-Eu_gMwq324XEMZWmuPLFW39Qr7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKJ6V3206ur2UUZ9xWTV4GvFPhCI03ZfXIVt5A5R-D7CYRul1hmoCGDLfOJa3pfRSTlaedtQVfbBTzyuKl7WpGSaVxxMvF2_gh2X0NtO5szq4b_2gFGb2SsLWjp75Pxnp6nH0tVM8UWAZU3GuvacfMWsJmQo2gMdIyVMgQcaWpXYPnN0V7wGTpQdmibkPKnQ33jwcDc0hjM5duSUVQRbBkTYk7qZENJiHcb_kMu4tXQTESLHvXyPRkSIxvk_inkaDfHESsu5WBPhuWzXuqu4n6qJLHbRvD7ET5SDwVnADL3YBGNpVREgFc4XSMHA28-JZWSUQGFYnIB6liyjA1qRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SplvYUVqfgZdVZ95nfPFqtivfqDS0xHEXOx5VIUgBSmDABsMWsVotdcccORfG5LQ_A32pVgZlnpFDWPyrcr6OHzhSwFoCokykFM8royYgkcA03dwXw7AU5ggWNVaPiC3fMl76bBO4QpKN3CgHTLr1-VKQOfFe06eSu2fWaVCKGK1fgnb0yzh9zceCkDyTKUxdhNzy3k9KWAcVHs0NK1DREM2k_lNEtp9yJtAiNeK7gZRU7K9xhNyH6t5MoijuRqgbZkZrSTCqMmSz-B3f5ukNbHVZnMMyMjMwMB9dG8zs7lfl88xj1tcZ__l-hNGXiCC1BrYev0RDiDM6JVwyuvnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2bF4Gve93iTWfoCqHaWb3Kj0jldqZrbjinfyh0gPPTNHV3LPJ9KNIZm__XtbMZmst2dgA7zMZBZ29WZ5dSWgyG9Z1qjoKPw5qgLz-D5zBPsCxeWYQZrIU7qiYXdIis9E-rNOOS87QXWxTQ2EKtNIirlQlbPb8l2YjcacBZNGOC9NJf2rVF4Usy4dfraaBdoiVahBdE0Gd7WKynWjUZ3Cs9goVjP9CGutt7aJI67Bl54qmwOa8HX1g-yB0hKuR7zsU20lwmc89cmYU1W-kSQJlyu1qoFrs9aIJdGxVabOpEUA-4GwelofRT9TAPmF54jWOVd-MCHyFG9fMA0BIlkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=CGKN5XSVhD3z52WCruw4nH8Sh7cWqkWEj03ZJQ8VnEIVke1keUdp3rZSRq-VK7mP_TyBu4MtHKKGbB3WYS8M1sw2CopRUBd84qKndZiA9vavF3kHXE1nkyKgodWar2F-zfXu6DAMLjG6UvduCNhFI-qhgMVFRLadI4cGgzgTkeq3Tdp3eN6NMGC9i8zDPgKbngGKF7liT9ixPsCDZckblg2tfRabjc_S6yzbnC-kZP8It2dFOCR97zGAlfm-W5C8IIaxnEuuIWojOdBs8eqA3PqgZeJ-VNwk5_wimqchvieFhsADd8egvk8rrASdYpxpMO8V-ygEyo79RAE8Gxi6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=CGKN5XSVhD3z52WCruw4nH8Sh7cWqkWEj03ZJQ8VnEIVke1keUdp3rZSRq-VK7mP_TyBu4MtHKKGbB3WYS8M1sw2CopRUBd84qKndZiA9vavF3kHXE1nkyKgodWar2F-zfXu6DAMLjG6UvduCNhFI-qhgMVFRLadI4cGgzgTkeq3Tdp3eN6NMGC9i8zDPgKbngGKF7liT9ixPsCDZckblg2tfRabjc_S6yzbnC-kZP8It2dFOCR97zGAlfm-W5C8IIaxnEuuIWojOdBs8eqA3PqgZeJ-VNwk5_wimqchvieFhsADd8egvk8rrASdYpxpMO8V-ygEyo79RAE8Gxi6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=NQqbdtbZU4ZDirQq54ZWE48L9Aeh1-KNFVxuhAeGf_XIVbvWYtGYzsu5nc8pCrevHVqX4_9VhbstguFSi53x1Fp4eWPkgzg0lrDA4wBk_HRtkRrykD65yPM8bVCUlfjJEl32AbBj9t-J7rvdLl-niS3igCuqSCaKEo_I9JbXochaKrSYiSDMOaJOg3x83stz5GjCYEKYbyH-MmmEGH-LXIyr6VUfLW_BL1g9_b5y06E2r37IbG_LzpT1LAYvk7qQpMHjzeBazngoGEQmXTYDRKbF_DPHJFkoM5homdjA7MsVXpFvygdESvvnX4jdmpINIvL8R7M0mvmqtJogAlVuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=NQqbdtbZU4ZDirQq54ZWE48L9Aeh1-KNFVxuhAeGf_XIVbvWYtGYzsu5nc8pCrevHVqX4_9VhbstguFSi53x1Fp4eWPkgzg0lrDA4wBk_HRtkRrykD65yPM8bVCUlfjJEl32AbBj9t-J7rvdLl-niS3igCuqSCaKEo_I9JbXochaKrSYiSDMOaJOg3x83stz5GjCYEKYbyH-MmmEGH-LXIyr6VUfLW_BL1g9_b5y06E2r37IbG_LzpT1LAYvk7qQpMHjzeBazngoGEQmXTYDRKbF_DPHJFkoM5homdjA7MsVXpFvygdESvvnX4jdmpINIvL8R7M0mvmqtJogAlVuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=K7qXhkE5XiOXO74AzXVVmJBXxKfLMSwUuwhTGzXEwvISJ_yu1Qqv559mtwsL3QzX_OMRBRrznjOIQiWGihW9vxNKoslGQ0BaK2BBOIbPBI29nAN0gCpaKtcvix_lH7YY4QxPIbcNnuSIPIdAIjMdHYCwL5GNKzSzP0sw1jC_Igcc12eIjlzysBmCQSvmUiO4BxdFv9MM3sdZUV0uV7eIhSWQFBuonGEjZdrKuQQQ8sCTgdP-Us1_R-zjItjzuGmH3LgTbu7smfElKOrOikY7zdGFpa2EX9RnYbvpsUohyNA23ljzRz8efJV5cVkSXJ3juPf5Z4bUQxhXVV-BvUgT7zBNS62_Wardxrj04OemmHFy8xldrkgYMqDBz_8SQ5cixUvsHRE3275u1hoAEdL8DTLMYvRdnzC19vMMRdJ3h8M-yiA4vnJA9-uN3JgbzjdO0mGprdUqncuAosCqKlaeGmOL0N_OnRVO5LVulYKN2dOoYUfKdjSF1XvzZn1LnZc3flc8ENu_N8UbfxVCBGLta5c-OnwmMKmIqtHsIXtFDP_V9tDGb6i5EfI5Hn2tMJRxLAGwVJLZhFztM_QBXQ_16jvEeI22Wwab9bN9B78joL6dPhXCOdICjUeOAOgJbuTrYdkG5vcZbs7p5pqS5hgHps4py1wCP1fopLX-iKhHet0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=K7qXhkE5XiOXO74AzXVVmJBXxKfLMSwUuwhTGzXEwvISJ_yu1Qqv559mtwsL3QzX_OMRBRrznjOIQiWGihW9vxNKoslGQ0BaK2BBOIbPBI29nAN0gCpaKtcvix_lH7YY4QxPIbcNnuSIPIdAIjMdHYCwL5GNKzSzP0sw1jC_Igcc12eIjlzysBmCQSvmUiO4BxdFv9MM3sdZUV0uV7eIhSWQFBuonGEjZdrKuQQQ8sCTgdP-Us1_R-zjItjzuGmH3LgTbu7smfElKOrOikY7zdGFpa2EX9RnYbvpsUohyNA23ljzRz8efJV5cVkSXJ3juPf5Z4bUQxhXVV-BvUgT7zBNS62_Wardxrj04OemmHFy8xldrkgYMqDBz_8SQ5cixUvsHRE3275u1hoAEdL8DTLMYvRdnzC19vMMRdJ3h8M-yiA4vnJA9-uN3JgbzjdO0mGprdUqncuAosCqKlaeGmOL0N_OnRVO5LVulYKN2dOoYUfKdjSF1XvzZn1LnZc3flc8ENu_N8UbfxVCBGLta5c-OnwmMKmIqtHsIXtFDP_V9tDGb6i5EfI5Hn2tMJRxLAGwVJLZhFztM_QBXQ_16jvEeI22Wwab9bN9B78joL6dPhXCOdICjUeOAOgJbuTrYdkG5vcZbs7p5pqS5hgHps4py1wCP1fopLX-iKhHet0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgxv79JJiiqQdfGdT9jtw8hyLqFDObyHZC9tZutDGXLHlx7ACqCU4zmnb4GEaO70jW6N9W1pcZh5YMrbtVrDhN-xO7b-t71nt3qS7BbyqmmyxgeitsS4UL7MLNLwBYUPo_4W3VxVtNsLl2gWnBkzuhB2XI5ZQW1UWuIJTnrvXzsLK8pEqBcmua2ZJhUXkIgC7RJH0mZzAogEhiQzaQq0pNoHq9xbezL-TiF3KWxu8YpAMzAf0p24l8xRZ5bm7CQVQaMvKMXLOtbCTs5rq7zBPdWOiO5lKTMiWxju0k9C1znzb2f6ejgp-n1L1Vkl59D1DfU_p3Hqs7DvIu5FAO-4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=Xi2NpP0H0KHIuy6lBogjFTjImq3OxBQBLu2KdZulv27-5QayQFmj2HgW4th4DFuhXPK-767b9Em-L65gleOdpk4WAPaZgZgrDaZEem3IE9gpdcbFXp8DZR6M0CzIlVbjZlkui_FMVLnn6hFcYa1pFQ2XbkZdXhvfqrigDYiIqJTzMU-UMJYE0eZw_ZWahyuzAt_NnyDP9J6Wd1MA86Xm16Out_imFQYRpB-vly4UKqq691Zattzztqnt5P1ILmg6FKo9lz9rjpyKYK1R8KwC1gR99pm43dw6XoKnH7xlEOKZ1AtatVJpnPJ4pY49rTcYgs8v2TEzX2fHILIz2nGpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=Xi2NpP0H0KHIuy6lBogjFTjImq3OxBQBLu2KdZulv27-5QayQFmj2HgW4th4DFuhXPK-767b9Em-L65gleOdpk4WAPaZgZgrDaZEem3IE9gpdcbFXp8DZR6M0CzIlVbjZlkui_FMVLnn6hFcYa1pFQ2XbkZdXhvfqrigDYiIqJTzMU-UMJYE0eZw_ZWahyuzAt_NnyDP9J6Wd1MA86Xm16Out_imFQYRpB-vly4UKqq691Zattzztqnt5P1ILmg6FKo9lz9rjpyKYK1R8KwC1gR99pm43dw6XoKnH7xlEOKZ1AtatVJpnPJ4pY49rTcYgs8v2TEzX2fHILIz2nGpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=jGPdjlnWeGkVyQP7z8UNQ769qt3TX088NYo-xqLz79QT8y0rETAS2wgnecvijvUbBNyUJrlNg1uTYdkucbv9VoYcPXjqtXVcEJx4Hh5x_gXlmCfGtGAOkUtBVA4SE8Nx4qqTHtVKmxDj1dT6SsCcwy3RPDlolSGCxdhrVkkhIZOhPwshEaoNfkfQ80C4XNVf6uyuLFR8aN6Yb_4UHmpVoG6iLdAaRQxTm4UjgJjS6Jr0jKfElO9_2SfAU9QLeA6D9WHtUVrBzkr-wbG_2ksAESSN6NS4khEIhrrLcYIIrXNveunIhOp4L09it-LJnCnIa0c-EAZnut970bt2riEf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=jGPdjlnWeGkVyQP7z8UNQ769qt3TX088NYo-xqLz79QT8y0rETAS2wgnecvijvUbBNyUJrlNg1uTYdkucbv9VoYcPXjqtXVcEJx4Hh5x_gXlmCfGtGAOkUtBVA4SE8Nx4qqTHtVKmxDj1dT6SsCcwy3RPDlolSGCxdhrVkkhIZOhPwshEaoNfkfQ80C4XNVf6uyuLFR8aN6Yb_4UHmpVoG6iLdAaRQxTm4UjgJjS6Jr0jKfElO9_2SfAU9QLeA6D9WHtUVrBzkr-wbG_2ksAESSN6NS4khEIhrrLcYIIrXNveunIhOp4L09it-LJnCnIa0c-EAZnut970bt2riEf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=vtGop6YN0NGX9ot6BrdCi0hucKEWk8Lh3KQayadg1x56kd239FJ81WMB8tnX5lU5AH-NZGbcJeTkCWP-ys7VkRDe-fs3fIinliX5K6ON0jLdqNVp_4vqCemcrLzxNJg2LpR2wS7rgidBCjo7fSlEICFMogtAkdaFzFucLpiteb0cn2Slm600vOMgr8m1slN3TLG1DKFjIoq7j35DdmmwdEpvz_O1OzQMHBcfNnjB-G1lN1O8kTN3Hb-OWXeaz96oWJptjzKdYgXKtJ53I67R4O-fWqPhAjf5SZI7LN0fmu-3LoQcMoQ7UAWFxEYQptXejIbg_B1mnrWD03JS9mhBng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=vtGop6YN0NGX9ot6BrdCi0hucKEWk8Lh3KQayadg1x56kd239FJ81WMB8tnX5lU5AH-NZGbcJeTkCWP-ys7VkRDe-fs3fIinliX5K6ON0jLdqNVp_4vqCemcrLzxNJg2LpR2wS7rgidBCjo7fSlEICFMogtAkdaFzFucLpiteb0cn2Slm600vOMgr8m1slN3TLG1DKFjIoq7j35DdmmwdEpvz_O1OzQMHBcfNnjB-G1lN1O8kTN3Hb-OWXeaz96oWJptjzKdYgXKtJ53I67R4O-fWqPhAjf5SZI7LN0fmu-3LoQcMoQ7UAWFxEYQptXejIbg_B1mnrWD03JS9mhBng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrkbXM7BJk1DH_D5EE3JPl_FaBbFw2kVoy5zeILsn0BWhsjBc6yMCBuFItLcwVVxatiNZ6hSaEk9m1LViFTlrzuEfpHkbDwIbJRUWV6-yGyDCvwDwHy2jUhproyV8SV4qBRvHnR2le9csKlBhgjeYkjtaBQObZkiTKSqC6Gsxe4qJnKjFB27ZpdDfMXNJsWvaubdSuU6x4BlHf3ddCWCBpenDhW2YrTH807V3NUDLrhT4cIlM37ArRRln9e80PNT2abrZVdXgdIYjIKMuoPQdH5d7Q005SIZQoDXdKRWjuVVmn8T4uvXh_tvmTdgnuqe-pd0Gi6NGPXCQv_nBRN29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=AjvwnnzAZZvgW6Z5hsKhSLkbj9ISvbFyYViYvB8gYz9nii7anY9o6F2ZrjNeNvv0vaPke4sbadDZON50rI3fAh85b__6KrYwOJtd2-U3IlEf09MjU4dQBvbIoDuXZsqU17uIBwaMQkBIK7FHAbbO697YqsreVSST7uisunnNg1yuvXjngHRloTwj5PA_RO7TqaQNZ5qwwl-OzxSg6brfGF-d0Ch8qme6LD5vSx-j1cy0ijLY8_NffEXPK6yMvZ2ppqa4JpYaRPPhG-pCLSo5h7Q__MBQ3RfnOrSworsz0P44vF2loVFRa6NE0uyXuYCTVT7dy5acj8RqJ7LT5ks7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=AjvwnnzAZZvgW6Z5hsKhSLkbj9ISvbFyYViYvB8gYz9nii7anY9o6F2ZrjNeNvv0vaPke4sbadDZON50rI3fAh85b__6KrYwOJtd2-U3IlEf09MjU4dQBvbIoDuXZsqU17uIBwaMQkBIK7FHAbbO697YqsreVSST7uisunnNg1yuvXjngHRloTwj5PA_RO7TqaQNZ5qwwl-OzxSg6brfGF-d0Ch8qme6LD5vSx-j1cy0ijLY8_NffEXPK6yMvZ2ppqa4JpYaRPPhG-pCLSo5h7Q__MBQ3RfnOrSworsz0P44vF2loVFRa6NE0uyXuYCTVT7dy5acj8RqJ7LT5ks7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=VHHnqL7A2coCNAN_ENLQDb8MuU47qXbgUoLWFMU7MOLGYrRNlE1sihfoQ6vl6_qgbCA4KpiXT-WShVHdFROOF9PrjbrouNByILWC_GCB61JfSmAfpyX7XM6TGyy7ODc46rFB_6bvKMFPavg8Yd9TfdG_7L-qgY4HzpzAUG8IFxmYO3hn_98oMOMcSdjXFqfaJslk8-z-gr_Al-7z-C1paQQQOKI23bXo-kD1Xx6A0hQg6-5Nzy8vlbBLG5JTUuOKYIwL0UQq3zPj5okdjjS20ucetrqf-zjH8Bz-ORvaKyr1TV2GCx3Emq9SFtUHhj6gYoPKZGzQ-HUlKLKccnud7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=VHHnqL7A2coCNAN_ENLQDb8MuU47qXbgUoLWFMU7MOLGYrRNlE1sihfoQ6vl6_qgbCA4KpiXT-WShVHdFROOF9PrjbrouNByILWC_GCB61JfSmAfpyX7XM6TGyy7ODc46rFB_6bvKMFPavg8Yd9TfdG_7L-qgY4HzpzAUG8IFxmYO3hn_98oMOMcSdjXFqfaJslk8-z-gr_Al-7z-C1paQQQOKI23bXo-kD1Xx6A0hQg6-5Nzy8vlbBLG5JTUuOKYIwL0UQq3zPj5okdjjS20ucetrqf-zjH8Bz-ORvaKyr1TV2GCx3Emq9SFtUHhj6gYoPKZGzQ-HUlKLKccnud7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=GgYbSu9hNyZjWZdiXW8NOnMMd26-kaSvgr6xaFfC3qWPN8Im2xvaxasVHIHVB0MHT1OEjYC4-Hk2XdT3HpSkcZFKFL4zUvPqLvp1M2co8kbK3aqvQnhbHz5TzafjoBtE5J9QD2ljYlF7Hu0OqwjMqhFGPUTOFNBYXgBzPkTB3nJ6NHJqy868OtSCtJukmR3D_gWDnGiIZAl7OH_DVmgE7wsxbi9qqilXtPdUVpP3VQHg7e5xbLOeyLxVka2LsARYtBj30AxLEcPaYI_nDKEyrpq97ggIHuxcnaUAa3jQtM_wNfDPi11phqWyzjUly-n8p8Ma2gumNTpkhxJwUmvkCbq0ntpbfUGVe940xnhxrY-CXcwkhL-qrZPK71u6wAF1cuy_2olb8d4Hx3WavWgqESicG8m3qaQLZb8qlZ6Wks0u2uYq5wvBqSOhoVy98XQk4LSvFItQ9RUAOKklJh2IW725i0yF_JuYoSJLkpufgmidEWHcZ_Awb0pb-rFoZoRCFClx0Es8olgIpo8QCofVMiZ_lUilscJz1tNLKC22IDDLZ8LI5phFcXTm-ap1z74v5F5J4gTP3kgtN9U9rNKC7uzStYJ2rKBLzFPB0guOcwXLUlGQfqK91GRQt5hv08-eMPHs8c9E3foEo_Ti7Da_8ApFoGWnRiDXg7YOW1z_QIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=GgYbSu9hNyZjWZdiXW8NOnMMd26-kaSvgr6xaFfC3qWPN8Im2xvaxasVHIHVB0MHT1OEjYC4-Hk2XdT3HpSkcZFKFL4zUvPqLvp1M2co8kbK3aqvQnhbHz5TzafjoBtE5J9QD2ljYlF7Hu0OqwjMqhFGPUTOFNBYXgBzPkTB3nJ6NHJqy868OtSCtJukmR3D_gWDnGiIZAl7OH_DVmgE7wsxbi9qqilXtPdUVpP3VQHg7e5xbLOeyLxVka2LsARYtBj30AxLEcPaYI_nDKEyrpq97ggIHuxcnaUAa3jQtM_wNfDPi11phqWyzjUly-n8p8Ma2gumNTpkhxJwUmvkCbq0ntpbfUGVe940xnhxrY-CXcwkhL-qrZPK71u6wAF1cuy_2olb8d4Hx3WavWgqESicG8m3qaQLZb8qlZ6Wks0u2uYq5wvBqSOhoVy98XQk4LSvFItQ9RUAOKklJh2IW725i0yF_JuYoSJLkpufgmidEWHcZ_Awb0pb-rFoZoRCFClx0Es8olgIpo8QCofVMiZ_lUilscJz1tNLKC22IDDLZ8LI5phFcXTm-ap1z74v5F5J4gTP3kgtN9U9rNKC7uzStYJ2rKBLzFPB0guOcwXLUlGQfqK91GRQt5hv08-eMPHs8c9E3foEo_Ti7Da_8ApFoGWnRiDXg7YOW1z_QIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=IMGiEQL-chmSTMDh_yY8zBFKY2UpnQC_kwEqItKMWit5e5JzpmXB9HxrVn6BR44qmcIhw4vsMUQNnJ4wclIUqDsbwCO56Tk_A_N_A4D9iJ7JWL5-R-ZC3MJrc-1kWtiv9wlKaU68lB6IcJVn_n54dCn4nq-SPkpflelGD1bB6Wu--RAcrZd3MTajQ8QSUozg_LSUBo6JoMayYHjkDyeOe5A9GbVzypbzFfNGZCBiE2fRRRFhygjZVjDiCxw7SMWBWuJiQ9lv3BJdcCmSTr6V_7wePpnnzKgA_IKF4Ao6CJ2CWT89oV7PPSmLiK9K_o2taXeLGZjPtHOQSOWAIwgrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=IMGiEQL-chmSTMDh_yY8zBFKY2UpnQC_kwEqItKMWit5e5JzpmXB9HxrVn6BR44qmcIhw4vsMUQNnJ4wclIUqDsbwCO56Tk_A_N_A4D9iJ7JWL5-R-ZC3MJrc-1kWtiv9wlKaU68lB6IcJVn_n54dCn4nq-SPkpflelGD1bB6Wu--RAcrZd3MTajQ8QSUozg_LSUBo6JoMayYHjkDyeOe5A9GbVzypbzFfNGZCBiE2fRRRFhygjZVjDiCxw7SMWBWuJiQ9lv3BJdcCmSTr6V_7wePpnnzKgA_IKF4Ao6CJ2CWT89oV7PPSmLiK9K_o2taXeLGZjPtHOQSOWAIwgrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYlJWMbGK3pm5rYYu-mXpqEFdJ1J8xaKr0DRKzojrh_T66X3gOZwwEiMGu1Rk9MCoXKFQn1gqJ67CDEyBkSGBOfFI4jaJVpIpeeL2o-peC3xnfV9kL8ed71j0jyQOf2YyDwnjOjWbfnhpWCjkz2xZhnabJXwRdst7cv1TIUny5tsr3VKgS4OzEv0Ft7ulswuiMPYPCWAcVLQXeGBBQmlG6F5KAlOHbFcDqISfrgi8ERakmBRUYJMVECIi99EG8TzAKeSk5Fr0IO2MMRrjG3mmkdbheFxZQffK4hf6ob7Lwn-DSUn60K2pmQq-MOQf8vap_XcaOeV3ZGyxeN1btbd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=OGHBXI6tbEc-lFkg67TDG7mx8pQAAv_XDvFHMUWcGk08gkAH0J-BbbNXz0k8Ee6eXtNPtg9HyEZcgkEObrm7N9g69ycSdQn6CrhipDtonSGnjEEGBbY6tA736t2Wn0jVuB1W1vs6m-3vAyrJoDwvgjZmiXocdg2S59OsfUcbiWsv_RPuJMHFWyY6rjzj18KIuK9gS8lagni1pcFoLFEERpOPJFr5xn9j8-V-8jiV819Fo_3lTqmXd0eVnYjytjkAjZAHg056Q23Tq6KD4BD6y7tzSOnz4EqQZRBLcMzQmpb_v9Z-dRo19T1jJJZevw4P8xw66_P-Zc0psUogdFDFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=OGHBXI6tbEc-lFkg67TDG7mx8pQAAv_XDvFHMUWcGk08gkAH0J-BbbNXz0k8Ee6eXtNPtg9HyEZcgkEObrm7N9g69ycSdQn6CrhipDtonSGnjEEGBbY6tA736t2Wn0jVuB1W1vs6m-3vAyrJoDwvgjZmiXocdg2S59OsfUcbiWsv_RPuJMHFWyY6rjzj18KIuK9gS8lagni1pcFoLFEERpOPJFr5xn9j8-V-8jiV819Fo_3lTqmXd0eVnYjytjkAjZAHg056Q23Tq6KD4BD6y7tzSOnz4EqQZRBLcMzQmpb_v9Z-dRo19T1jJJZevw4P8xw66_P-Zc0psUogdFDFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=ZGjPqlTP7t_Sz0B6pDFSUFX5UbAhDQjCAHZqGpl-PwjF0IsAxTVZxANgf8hrwV5qNY3a8SLJobMdPd3M53DUprQU690FLkkoN9Sqzo46lZ3L3elPev4IBJC4L19yyKLbviZ-kq4bXmr6G4kephOIek5y2KK08bwQk4PG0vYgQo9L3EWhDtzRrKZTrcmuPyQUl8IpsA9zA2xuakjyIkgSKj1I4098-GyI9A4BJk-ek3K7V1Lbhz0iKVu6pz7P5m3Po3C81OiYmc-zK2pywaz0NrcpIHVJHw4gCwzV2-9_GckaDFQih8f-BIvoybekRg8mJRYRcW4kBfBrfmBvk997gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=ZGjPqlTP7t_Sz0B6pDFSUFX5UbAhDQjCAHZqGpl-PwjF0IsAxTVZxANgf8hrwV5qNY3a8SLJobMdPd3M53DUprQU690FLkkoN9Sqzo46lZ3L3elPev4IBJC4L19yyKLbviZ-kq4bXmr6G4kephOIek5y2KK08bwQk4PG0vYgQo9L3EWhDtzRrKZTrcmuPyQUl8IpsA9zA2xuakjyIkgSKj1I4098-GyI9A4BJk-ek3K7V1Lbhz0iKVu6pz7P5m3Po3C81OiYmc-zK2pywaz0NrcpIHVJHw4gCwzV2-9_GckaDFQih8f-BIvoybekRg8mJRYRcW4kBfBrfmBvk997gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=wCJRccbjQ28qrbPhBX2VpzXoH-voIKtscn-wwZMZdMoogmCeFse_J9isFI3XRUiDxY7c9Z63taSIAe-SquKb6I_Jg2QLW9FDttHKoVqxUZibZtMH9zCrJYlTh_HHxK2Mzo_Ruu0_a-j0qvjUz1pbsVqJMzmHEZ7APhy9ztReB4Jp3ooQRji-39M6z6LNHQrcu6kNEHg8R4sTfwDJjEJqmzxG-I5uCLlAYTtGpMhIlPHXcoUKqOPTMqxRtMGOXX7VxfJuXlBWqj1DHA_kTcaDCla2elxBbidp02u5LXpoOCSlGzsAo863Elz73Rgk_IMZAnCTjf9sy9cWHg0qISu4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=wCJRccbjQ28qrbPhBX2VpzXoH-voIKtscn-wwZMZdMoogmCeFse_J9isFI3XRUiDxY7c9Z63taSIAe-SquKb6I_Jg2QLW9FDttHKoVqxUZibZtMH9zCrJYlTh_HHxK2Mzo_Ruu0_a-j0qvjUz1pbsVqJMzmHEZ7APhy9ztReB4Jp3ooQRji-39M6z6LNHQrcu6kNEHg8R4sTfwDJjEJqmzxG-I5uCLlAYTtGpMhIlPHXcoUKqOPTMqxRtMGOXX7VxfJuXlBWqj1DHA_kTcaDCla2elxBbidp02u5LXpoOCSlGzsAo863Elz73Rgk_IMZAnCTjf9sy9cWHg0qISu4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFGcWVXDLHEB3iKahqseeLrK8V06eYgC80uvVxhtDZnxLg864pOmPoY51jA2w9ctL2OZctr9tcUV16nCTOr5JXdo2HrM_nZP6LIl5wGrQ_A6lM23Do9Qs_1gZa2N1YqGfxDGTtZKxxFzK8ycAm6kjKbjc5CYKVBnAxEkqvRo28n5KEZpvpo8KLkdWtkwanS06z7KI-GIRVZR-JiVXfYoxrWdy4HeZOX6rw9tmy4dW5XlQHMIVwzpqDCywt4HuTY-vxifdTLXvDsHPCMeWiJJM-5gHv2T0AMNkk94uxqNH_8JNFzSw43NOwtOIGgoVKKlNKjrhn53VjKBzGaD2JmNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=e9O4wtitpYneJ_WuvuRRINO79XzwB_QpsxNFWemxAPHYctr5HttnQeEXOws1fjUaPFLI5JVjj97Wy1Qip7-HTm5FVBrYYLdP1es_X4JvrE-VSS4kQ2T3S9dwOZzlukjbmY5EtULiJpKqHlBC3auolSGjXzOeormmM8Ho-uXz1w09Gvw2iNNq_LAbcfVth86dQ56oZ-cOnOAjJAvD_zUQwZtovtlK2AYGEMAtnGM7DEL73vHToY0goXMTJf1NlrlqgIR-sCAfzLmMlNz2uHOzDRQFVI5rp0ELfF_Nb-JWupXDo2RdppB5Glub5jNyruL0fZQl8dt9FpOFnGdoNH0BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=e9O4wtitpYneJ_WuvuRRINO79XzwB_QpsxNFWemxAPHYctr5HttnQeEXOws1fjUaPFLI5JVjj97Wy1Qip7-HTm5FVBrYYLdP1es_X4JvrE-VSS4kQ2T3S9dwOZzlukjbmY5EtULiJpKqHlBC3auolSGjXzOeormmM8Ho-uXz1w09Gvw2iNNq_LAbcfVth86dQ56oZ-cOnOAjJAvD_zUQwZtovtlK2AYGEMAtnGM7DEL73vHToY0goXMTJf1NlrlqgIR-sCAfzLmMlNz2uHOzDRQFVI5rp0ELfF_Nb-JWupXDo2RdppB5Glub5jNyruL0fZQl8dt9FpOFnGdoNH0BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=DpqwGYyxorEWF9jiNqRz-YR53e1IDG7Sj1qWijR6bKd9jJVHbIomyBOLLL3Jx7623l12QiThpb8qcg9WIjCqeiVNYoYxgHVc1yROtlckmtGwqYYd3gDurpTNdq49U-T90fPUb1_kgega8Kko5xoyK9K3wSzj3HWzivyn2LBcGJeVEBboK--vBxiy39gTcZN_a50XlyTv1D7YZ4dFamjxojhO0hqBah0ZBi_j58pw-B51HKMJWADYVnKcbWuiE9w9qm_HVbElPIEOzk26TQk_RkSIs2oJTvUutbVlxsP8_JD-kIVQzPw4HgEvkylnNa2I5BvAMxdS-nn5mcZs7bOTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=DpqwGYyxorEWF9jiNqRz-YR53e1IDG7Sj1qWijR6bKd9jJVHbIomyBOLLL3Jx7623l12QiThpb8qcg9WIjCqeiVNYoYxgHVc1yROtlckmtGwqYYd3gDurpTNdq49U-T90fPUb1_kgega8Kko5xoyK9K3wSzj3HWzivyn2LBcGJeVEBboK--vBxiy39gTcZN_a50XlyTv1D7YZ4dFamjxojhO0hqBah0ZBi_j58pw-B51HKMJWADYVnKcbWuiE9w9qm_HVbElPIEOzk26TQk_RkSIs2oJTvUutbVlxsP8_JD-kIVQzPw4HgEvkylnNa2I5BvAMxdS-nn5mcZs7bOTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=aifaYvbUFEOjbsM--qAK-byVjcurXrHhpZEgEQ5zB2ly57SEo8RnszF0xN4piOzISdKKR5e8a3vv9mdq_S548lkSl6O_agTEkt6JOIXIJfyJSoQSstWEvaxgheXKCnOEFgxJJYF5MRsw7fSWYxtiktjfM4aVkzBzK9jrqOjN9vk0OCTg3flEH3fBRUUzYonZzB0J7m5Xa5UOx3qw-TyxSJmr8IQPw5_rLOKlhuY05i5b9xxbcxKDjYpbdb7QouhxJJaJBPGnTohruyujjfkmqidJB0rrIOuZavAxGdaGW5_JoLoNuYo69CTwCKRarmpfBvA_gVLBt9snN9iyahYbIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=aifaYvbUFEOjbsM--qAK-byVjcurXrHhpZEgEQ5zB2ly57SEo8RnszF0xN4piOzISdKKR5e8a3vv9mdq_S548lkSl6O_agTEkt6JOIXIJfyJSoQSstWEvaxgheXKCnOEFgxJJYF5MRsw7fSWYxtiktjfM4aVkzBzK9jrqOjN9vk0OCTg3flEH3fBRUUzYonZzB0J7m5Xa5UOx3qw-TyxSJmr8IQPw5_rLOKlhuY05i5b9xxbcxKDjYpbdb7QouhxJJaJBPGnTohruyujjfkmqidJB0rrIOuZavAxGdaGW5_JoLoNuYo69CTwCKRarmpfBvA_gVLBt9snN9iyahYbIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=uKd7DNPdMjW4FBTecpabTOeRU997TWvUVcudKM4UikfhfZ5-GY2-UPm4zYJc1fBSE2X_nGgRvfNdTkD4fEe6OtOqOV5RSnP6IxzwzIxH5rZZ8p-0xwh2i8KwjbizzbEmuf_KL-apUraUnlOQ2NlaKrs91TV2vbByrvseG7vD7vSZRaKjJwmADJEvNEkayTcmqqqafRLq5myQI0pUQbbBZrtOucyvVxSEU1YFuL6VRmsry3l6bgg9eQOBxYIC3B3T-vli3MRY-HsLsEYtK-uHLgrS955zN6kR4cFMxU0wZBaSCoZFasC0PtGmmEJvNNMKt1Ea7T7S-FU2fpoeXgPgmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=uKd7DNPdMjW4FBTecpabTOeRU997TWvUVcudKM4UikfhfZ5-GY2-UPm4zYJc1fBSE2X_nGgRvfNdTkD4fEe6OtOqOV5RSnP6IxzwzIxH5rZZ8p-0xwh2i8KwjbizzbEmuf_KL-apUraUnlOQ2NlaKrs91TV2vbByrvseG7vD7vSZRaKjJwmADJEvNEkayTcmqqqafRLq5myQI0pUQbbBZrtOucyvVxSEU1YFuL6VRmsry3l6bgg9eQOBxYIC3B3T-vli3MRY-HsLsEYtK-uHLgrS955zN6kR4cFMxU0wZBaSCoZFasC0PtGmmEJvNNMKt1Ea7T7S-FU2fpoeXgPgmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0-_mawHzJ4Ab2f2llEtErJ8Bdgy9XuS890kbME9wNPdtfVAPGINT9wJNX-tsqTunuLpiyAgWkjJUun7of1le5Yo2hut33G5ZPJlhqiBbIRgpUn7qRE9aRJgMMaOISWbPH8DYz8zpyOViIaGlP0KVC6qtVSKU1_ChBLrqV67HfDzoQRQDDc8Lbn9Y250UpLjH5nHKODC0_8PXL90tgsdfhjCJOLcpTbyCdnpaH6FwykaPpNlzvFJLeEiXJm1GqNcB8WN9gWlhYtKQRyaqqPU2YFMZWnZlnXCVzER4jNt6mhw40PzzEU49AXpjj-Z_3eJfEB93Hk3Ql4VyEbhpykpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGRf4ryf7Mq14I84U1g3pJDFhbGG5wBQhhI3_1hHwisRR2oRHRlyFOFq2eqe6UoLvK7MCdGz71QWd4K0ARq-sNffNDRhwhaQ4ZoYaJ_01zqvzApVh1okD-TlxC0uFlHtg4NZi5kaBprexhCucWrbQE_NDAWxsk-mYbuZyMNqRGVXEgDdQsHw4HO4gOIYifsQX7YDOH8wisG5dR2FVsmdrAi4nbp66yU1eoKIM-7Q3xfwWg3lwWhojNjCTy5SHQzeO4kGOPnJy2-7wIKicrkBMo5eAPWh-Q7FG1I4OrRJAQxOvif1n_09-muqlkGjlDa7MqIuWdSd7pgx_F0F43PSJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdbarhxmmPVlIuunMZmx2VpPw_lhNDFZzDDmf40M_ZTLYNtMmAT99RkcUvXNSi2djygrPXlwmVBkN84Kf_te52wBWqVuvihrtaz5s5E8aqJ-_Wo2iAGqR6hlF_ma7EdESbKpk75_lHTqRi4V-N2gPxWUoQ5lqIjmffp05-MI-Pe9G_RsOLUYrGxBZEGn7w-3QtGEPF-_9uYpwPt1TZS2sv3BxGPQT5uk3cxvP0GEmuWZKK7C1QXwxdTILnsNlzjepapUCIeBpuoXOVhlW6FyMV5IPFRmL6OWzEV05h9ZnllKyTwhD47xxbe1FnsCIA-tPFM3NjdSFh11PTX7-N0Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
