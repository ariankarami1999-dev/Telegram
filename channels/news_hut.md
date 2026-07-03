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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 21:24:38</div>
<hr>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrM_b_XCOK2IvpO_UtxfdYuZzUjU1NJ_umw4cgwCNdN4dWfVU-0bjUSVNBw-e67Bp1p-tvcgPD2F9Sa03oobo-UQBRdl2shbP2YzvXVsVZjrxu2y8kL-sNiRD5V77BI5G20bhbjyY-ZoRT2ZgTGtFXJTVG-bHtZi-oe8SBUcl47LJOn4_ZWx_ns0MwF6LUraCLp2wwmNixH3TcEMcBiAOxLnadAuF_wki-7GEvc6qGOX3hryjnc5hyykwMM3nyWlvjO9SR8wsGEPvMUnRceOzwA3ZcuALb7kl_6PCb1glI-8s87VG4Q5pNrcu9OzktZ07SlLwJ1s33Ia1OkIm1y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhVfeSQS0-k8zhwufwtMKdG94WBlV8zZ8n5rCJqOpMvSWNItbr8NhQPrVGjXmOyzJ43wrOGztWkkHey02-u4Ozty4WoxkGiSuiVnVOvLl-SzZsK2sKL74_oG52gfx17PMiV_YY4M27pnLV-vO90iimkCu4Jh18J_Furfs7iMTHp7Cs3cWDyszi6y_s6mSLiegv-ehFjEBRDALCaT-xPKqWGD-X6INgc5Px4uPERfcrTfor5tZdZEUV-Dk83Lw4hUK1Iye9c2rBrrMxQm7EDzqnVO01qtyMKBcASw8amTgXWKem1uXFh2Bq3rYn4XgasIKWoq73nn85eKMcaFkQ99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfb7i3vKjbMXa19xtT2ohmM62JvwU5v_xC57UlCYTptHJgGVGcIECy1v55bNxPILnZWuLIyGwTuQt_TyjvH4e24PfmWeDgYka0uw3RsRg2xhIO0H1PMK6r4dSW10ZbVJsRslyQEqJ94S8BBl3UBnXgP15DOXAb8C-YnxvoxvmL21qNJheOqbq7XmcAm5vXOt0GuCRjw7RzjVHU6xbj6aLQcUWIbSRAZ3LsKK-4jsEnHRN0NtQpMOP-TWs7xO3SLdmiWtTDenYbYRXHJnJL3EU68sD32g6qLZROghnrCL1cX3KFt-mDYk06I1giUqGyXs3ewRKENxCyXHS4WisPtAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHJ72TPPAe7iW-fBNt1czBEUDqk7nH-AIBEPZtyRNh80PKTGV5QA611QNuBKqCMJ_vZmyrKbFm5gW5RwKdBOoUNBIjOqjizL23Fn0s8lR3-cVADN2M-tMLo-iummAMWOhqvd9DeCg-aoDtPKvAl2hEhbtjNhD6cGsAI5m17Ke5FmP_00xzBRULN45IebrOSPEg7n1P0MGkBXY_v0eM5vo8aRF6EbDT0SCnJVDSMXc03MFOKWYsN8nVI0FVLvtP0pYxhvULsYfCKj3TgjsOX_A8mrrZh8_GwerUOBVlicuVAb1DC4UGp7BjvPQ4-63kSMfRq-q6uxzYbX9ECkiYDM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YjzF9HVK8ZbOHP137q9dubClR7M3XkXPCkf4XJ0ZzzxNbxpFux-Y3e7ZATMpcQaePG8lHmUpjAMe65pVHtm8XBQNAIFJB8_x5y-HMEZgbLkttEgPBE41eFMdG_EDUn9fGPCbxknHVz2jHe7efHy0dj3opG4bOGLM4Mwm4K1z4POZXVJIWSPwjEcVa9fue-vAenptxDwmkFPGDah0e7CwKXoTvZOhExhkpGLhxPeqCdubwLM6RhGW6L2T4SgacHu7weZgk-rHgcrx_5555IgHf4t8gjirYF9MZWLtemLh4z6iBumB-LBh5UKMe032-MIDzAnN_MJY0TY_3icxzJqP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOffS2N7OHGboVmRoeG6o1qoasmi3LzMueLjNYQ3suTViAC_Nk33fyx5hG60ZlwoErKhiEueQLj3YQUEi-faUkM7KZ3baGxeXxFQ5gDqdyxzVurU0mkIabhqCwIuOfjGw-UYbCxgSwsQs7MPI3-YSvaIYwpUVzl8sxONEf3vYIuaKBDeoeCCmpbc48xa1PPvo0OUXN8EmX8KuBr_26dkZlAHJ7yO36QwUWB7vuD4rHLObmcdDlgqynL_RvzQ25qdl2-3oWXaK9SpksxHP6Y-GWjsLm2EbE48nbzdkLJXsijR82jn-TP49MhCdzztfgRfsybLexZUxSqmiLya-1f0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBpInqS1q9i8uc086QuO00AWM5JZZeQoSnPe963lM0DhGUsR8ANd1rsNDE_1CSCqEzKrDhDBcBD82sdhsNN8bwNKte9f7ZdPxKJ1Iv9Sirq7zYNuDjwrJObo7Q8MzuGNyHIufkl3vhQ_QDDoyPsoz5yCeo_KbstF2ERSi4bXJnL_VzcLQ2caYh4Wzo9kTAG1RnxB_YOv6c1Dza4NEuYBlJTxQ4-Qy7_QfoMmdmKCiKkD7fP5vp41X4_5N9Ev07JA933WoyVE5dbkeih0Hc0oMyS3CN8KiLkIpWFT7qrJ9aB4E2Srsvj7YGFfogs5WSA14EKI-af1n_8_yC7sXwF6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vngU-gluAq2W7NrN-XrlXjiU-py6pVm8p2c3OM87UcorsBppSzzd2Bjh4IuEINnOxslNxipm7Hz7Toj-ubB7FodO2iQqg__75eoQxnKI4C8o9PALuY6wByL6jEqJT31n9MkvHUkkpODg7YUif645cp1zfT6XdodH5i_N1DVMbXA6lXbjgCo9-FoNQ3wHK5zSpO_1L0BlH9Qlu5dzdm0UibkxvIoQw8n5RKKvadCFywvT-ayW-9LUccOiJ13ZhSUPB3dkVZavJDp1u8GZ4OVN3Nq-zVnkW_WQ2-9GHiW1Sk7vIyM4d8q-UHOJZbq6NezfcxVFDRqzP5Niqnm_ARJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkW608S4bQ927Sx8P9ZG-VBQ8gLIRWq6mtJiF-qgIp36m6z5abIC-0V5XQBqZeJh2H_BKyBEGMP8-VnuaYWBPGa92faMHtJ2X4UcHv9VC0GeYymbHwoA-GHza2_MahDGSDtmaClsuZqsxb0KIvm8ZQD4Gv4m8PewKRILh1iex5qjYvOvhn9keVzK9Tv5EBj0LHn1lGPLQJtVnoBwdYspEkpiBEnJABPbZ9bN0LtNrsJnyC-xsSRWqhnMOFrgOPywKY4GEJaMdQIn8PjXYkv4i0PmBEZ5XAMzELA4J-7XkcAYAkb6bSvr5eJn8_MVC9xWt7ZWZLe-uYPbnkg6m33_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE9hlzuE6wHxUBLtmlUUvV6NbH-y91Gh4DyiKbA-bCYPyhaIWid_xqSYSIAPHFq0AkAxSZrfrmybelu_zSl0BHGW19P_QIardt4J6kCmOCtaB4GJ3Pxrv8Z3Al73QvpJ2VSZfAtweHZeKtR7tgagRyPZaRS8lZFBARsWedxEyGBPFgtCol7mbV_rx9zq1g2E-mhAoZRqhY6I21lAGl96Nxy-U66ySmFgbWJJtBiMcEgs7xE1FwoCGg4yeClFX8qjGezGXDcCer5C_00s1XIcYa3hE36DYsXftMn0Gw0i2_6-vVnQ7VQ2Ezvomc0eW8jZQNan6tZ4ib0Kx2uui65c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAqfFfhxhVn0HyNo2j85fM3x8eXHD9e1JhKiDJuyMd9pnD5cuPlma9mnXAR4Jsjb24L1WHYhMpuAa26eFCDNPPGcmyYX-nsVHmHJzMp6324mZO1kqSgWU1kvwPILCFIYEIhcT6QO2xlz-7BcvJancWAUtuDKcDuOfOnB6USxLzrUTts2xg7VWQJBdMxErWaRcfJfJSxGqC_34Dz3wdDt6WZ-skLssiwxytYJclNqMpSXVqrT1a_hTA6jdUvkB81DWpYYDUiRxjweUJqKRz9GTuUP0ldy7m05doS4RHcv0uwYpcLDfbWlziHGjI0H8rU4bkN08kX8ogCJv-7f9k5mdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3MpCKVVrx1PntTNygC3Gt4JlZE2kIm26wZ6Z5dhDpwehE1TrdQZtUAIf2nKcq2cReCXqLz12_1fWi1kWZSfPkj4DF78i9WdKWSCmBIXZUoym7FJBKQLODNVt70vcubZA21NB_9EOhXBbZFCQI-mgV_wUnwM7oPTVj177HEZZieRA7cnC1lNgQhFSoj0yGS5-9eiC4hpeN8kz6fWtc8G6hi-9W9SrCpTMim0TBL24q3fon5F4YtVN9BXR8M2ltgZ0xRPOApd4T9zP8JO2I2ht_t2P9Uj9FF7gm1ErXGzJJQ1AKo2QYOIBxriA1TG5RS5WgurOX7iCE_xUFHCrROFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwcFPphLMY60S4tiaO6pnVWhXxiEmEPfv2-o3TF-ImAep8eXQSe95F0yHuqIfvHjYhb8SUwAM2ymi_U5WqHe1y1PFoQ0u7vfj0QriwCUV5_DQ7gv2_gfkdXt-fUenrv7wtozF0YFYDAHB6_2EgTcLJcvYElwQ5KVc5CkBLnhRr-8E62lUalZLoUgd4KTX_UwEuudw-9IRrUaeMHVkIMbD5tJCywtjL2qFwRtdAFHcuxw_FdYLjGjDfVy8K8BH24UnkGHfnF7myBXbeh73WzI5xuAoRA4Hi8vLFW2YX63vchqr9TWpd7Ow2kbmDV5LcZDlBrCOsFJYXW4fUOlMuoppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5co03EYXC2qCEUU4NwkAcSMs2KgZl9kQ531gABP33ZlPkZlnS5RqGSTtG_ovE32elJeGgCyBFBG-pvKKJC18TAUlIPCEGIpNsYRS-fqXD2eLjeNJSKD9mVS0Dv4zlecqSsOJJU8_pQxEgy7A2UACQuzmqPkbFumiXDnmf29Nsir14rdI5N-fmTc4Y-8Oea_IGoL-cYc2LU3TSTiy1AF18UhbGg1ai3N6lkPrHOibkQDz3ddgXb77DdT_rKSynahu5Xl_omb1VLuO3n7d4mG6O2yLZOF48SEaJuDNetM_9DnQ2WrJoYLLar3wMzdaUor0w9LoUcALgUAZkTQw-p3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBBOnoUSUBBstq2fOjdeHOGIY_eZQi2INYe2FGluG-ULthiTYiC9Ci1Pnkb7HYrWIrPw0sS1aIq04RcC_5KFIPrYSLaC1WASySDx5rlZOPjDlAcWgOcP8ITvKWtUCP674Xq_iLzY5OzqAdeYPDlSNOX7u5I0ZVVK00kjJsZL-EkQvNmyhx3kAWWoY02zy7fUNXHNlVFYofCHa7nWnNwxv2xdGnynbIwH4XQKZAGxYwBcqB6FGaWqz4wqBtcCdN7U6siBt5trOC3qHXndXUuuYjTbYpt8Vor5crXPCIS1FZCsM0FEzP-8-gt4qFNdUArD74V236PijLQHREds8FEYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkacclbUkQJyLHfmEve1mOWIEHpZDK6HYL3EOtUAMc1qtzgL7jW7caPjivIgl2m4mlGxl5DKngMhjz9w8STRA2OfwD3LUpTfOgj-nYsDbvJ7uOgjBPJRPm2lKnTjUhNnygohDc_iPajhbp6NsEkFzeOFSB1ehSqjpLqqxqQM1ji7k3ezKM2GvtYHjeoIC1VTH83SNZkNbLKvXwz1ozA24nOW6GS7V2z3yp6eLhgjeQkyFiHcGSg63Rn1Ogj6R05dULawNNy_yfbNrEmaurEXZCtT5D4jhp2B0lTdy-FL6gZbyTs6vEVDSzf2P7nUwKN-ivjCx7zNZNPA4MHYfxNZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=XrXIw8yYouxIOZoPdLLS2n0GJWsBAoQE32HXhR58NeFOYMxmQO3grJpIjMUMJdQyAyv8I8W1sUmoe8DzfEQD06LuT2c8l2bdoPixNU5aDE2q5tHEvF0QeMkqOWwZjJ9VhGOyECIOjHH_CdgKp50yDDP5eO2aeSlFTFdPaxTVHp57M_Gqs3iSbPd86g9xzzjMoU1Lmrp8X57B7VTqUJzc-Muw_wBTkPsKST8nosVRtmtGBlf2eXXLuQNqspOnmr9WM9sS1eFZkWzTOUINpGmAIO0kGiDn6RgNht5p8VCyuHvk4d_PK_xZ7lDwPnb6VE5igGNnxVFOh35jhfgSd94Ztg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=XrXIw8yYouxIOZoPdLLS2n0GJWsBAoQE32HXhR58NeFOYMxmQO3grJpIjMUMJdQyAyv8I8W1sUmoe8DzfEQD06LuT2c8l2bdoPixNU5aDE2q5tHEvF0QeMkqOWwZjJ9VhGOyECIOjHH_CdgKp50yDDP5eO2aeSlFTFdPaxTVHp57M_Gqs3iSbPd86g9xzzjMoU1Lmrp8X57B7VTqUJzc-Muw_wBTkPsKST8nosVRtmtGBlf2eXXLuQNqspOnmr9WM9sS1eFZkWzTOUINpGmAIO0kGiDn6RgNht5p8VCyuHvk4d_PK_xZ7lDwPnb6VE5igGNnxVFOh35jhfgSd94Ztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuyD_d0eAHoHlHWnNrOUsMArYgvrxbhnGMD4OOZ5FWyU_Nh7oUvxHX9iply5gJtDfZPjlv0s2KXpu19VB1wgp_o-kWjt9NcE4Ziz5TsckhiGOuxPmc7kTIR3LpZ3kaVz_aRBLmH12X134qnNYdDonRl8Yz8PTdOquRmTxjPhn5Ag_1fIU2FIKbGL2sAvoCOy_IPDo1raV00ILc16GgrNueugwK8VeYGraOmC6DTDTvp3skSpA3cdfn7oFWgQclPS0Qi2puha7qz9iqeMrnFPSq07ijJIFPP4InLBVeKSlC3iLPuIHgqjN96FkXIKjMrxOi3ZLUrALaHV8RbHP87y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=SaVY55WGP5604kTCtO9LMiSk7nFJB00l6ugou6P78pRT-3xpNwfTKuCWYfOv6nGfF2Z_lhsSJEEf7wCdS1kxq0n8Goa1ZRd98G51_fbdVHDcuNRz0dMdNyv9CobfQoK2Uuggtg0mxDIZOCujhXnKEAochMr8XY0koZ6PCphqzR1JndjTXmpwgBFkH5yxIqh7XNAU-L58TqxqZdXe57mwrvOSaBuT5eziKrALJ34JdI5i0YLKVGlRIqu34gWAxsqv4XHx8Z9ghsPmnlQ56PRJNMVKYiqV8_6iCy6ldJcIZoeDut3OX39IN2yl4TWkihHV1ov9p8kZPpVqeBtd4tXp1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=SaVY55WGP5604kTCtO9LMiSk7nFJB00l6ugou6P78pRT-3xpNwfTKuCWYfOv6nGfF2Z_lhsSJEEf7wCdS1kxq0n8Goa1ZRd98G51_fbdVHDcuNRz0dMdNyv9CobfQoK2Uuggtg0mxDIZOCujhXnKEAochMr8XY0koZ6PCphqzR1JndjTXmpwgBFkH5yxIqh7XNAU-L58TqxqZdXe57mwrvOSaBuT5eziKrALJ34JdI5i0YLKVGlRIqu34gWAxsqv4XHx8Z9ghsPmnlQ56PRJNMVKYiqV8_6iCy6ldJcIZoeDut3OX39IN2yl4TWkihHV1ov9p8kZPpVqeBtd4tXp1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDSaI0hksBIEj3BxMW2xqHeIFfxG0Ey75XbiaGyWasBhcPdOcrSIYlLbGQc3Oq3Q9vak5XXAJrRJ5Z-6-XxZPQ5p5wz-x8N3InAXq4jIhIWOwc_TM2QKX1IeQeWK-QMRadwad-GlilSYEK_-Ay8G-YcbrJbJK83-DTtZ7fhcIcrcIYXj9mzg5UrsAYehYnBCJbwFD6RNAMHQ4fD5vyCP9nXOkvhQMKgr4V4Nt5C7rlc3BxxBd5JK_6aaNBOViEejskyRYpfPHkqU2Lqzhe4P_a2KnUf-rHoq3d5YdOE2DVgZYMCHluDb3F9z-zNzAopcF2tS9GzjiNuv0_m6SnAP8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlD5Sp6FtV9mA9hhSpZYYybv6rajVZ9HkcyZePjPr3V8BTggmfgy51_IKE5g_f71uOjFY5dL4LqEiCrrt4MsfrOveh23gpghXujN9F4m5sZZsJhhOHHpHvu6ntvYqhQ7o1D3QY2Z9_iGUP5D_wnuItw37S1LuXdCBb12WgW0H-0qJjrDmy9hLiB0721jjCKvcLwbpZegwsj8nFj97aiFeboYHuNzrCZ4eBUfPkDNZshbg7BmWIfY8RWuIPmby39h2GBoU1IAiI0s47vSKffbqRd2sK8sQz25BBJPTFwsIrVDs0fMlD_kb4KCLpyp85RD_MO3Lf25mx-i4r7DKGwZ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj_B4aGQISqxaeuOO0OnZ8W3bR0ld4e7UkFiPwo4mQp5-ZOV8hr9W6ykak6AMmKCQntG6qnNFxbiap4NZjgVF9biUoZWWzbTKZClLNu6hExpzzK04us-_Zxq_G2WcRdxxhjvCQ6LIsBmizvv6Vq9cbVoMDtzm9Baod35NPb7HZmgZgeYzqfdP7MEDTtdRdZU2kIG7FdejxujxgrTs4nkvhrhF-wCGwpVBJYeYwEAAWAczDMsHm7YZvM2NPs11osEo3RdK5ZVBx9Q6MNyaEFS7CaF5XrpupNAE1-2yZek2DDfsqh86EOHmm6eUwi_3FdQ5OX_Rl8DJxJ7PauE6hjbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gj1s05Lim4MOXClsV_yCgSuf0y3HVjil_maz4j4TceYQLYIPEdJ5TZBa3FeTuS6Ru8AnEiMy5IVhWGM7nu2FW1oRqVwdeBeDYx1dzuPpTxR-PnpYAGjbvAcv4cN3VqNYJf8OALcSB0biOEfoY6a-nHzk8PNWAgy5YEVCoOzy9fjldS7AYAJQUGvRNJhaFdSQYjH2pkAbmo6nfAjWcp-xjayo_hy77xzpX16Z-nm40-pnmJnkrBatpWdAw6C7cCz6chNkpA3Zhme4FpIUIy67shvG7FmUJ1LGX9HY3XwhEWUX3M1l2X-44AT3qyGO-lDY85FlWHisolRr_yRNMiNf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqMJ7iqIqoM9FWAGnPVN5s-77eX8YNQvfSLQmKPm5XiZxJ4qWCws6-iBdWPN0aK_49OD3XFNzI0Cob8Me02Q9_qqbLMkMg7V8JEILfPIFoNxLgZmT_fp3FB1YaqGAShvIL1ICW1BTK_USsBxRjXFdposY_uuiYzcSfS6MvjPleTj1S7Hpue0rN4M5bn22mzPpBBS_D9fmy3q93XkauV4qoBipjRSpOzpe2bj9DyTT5FH8sYat3xh8U301hNZaWCU5f6H5YuxpLCpyetoAKUnAuNC1YUsX_paQSEjF3n_sYz_MIff4qG8wNlWpZdWjUrmFcsMq8WUTp6Kwos2LwcNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=vEXB8MxQKcP6NSINjfOBVonIY1vldRrQLX5MzbYyHmApomFEkTeVNFgTmxNCey5gLlOMAhhNrIG5kwEbhDM8XH2vpIsf448qu3735uWP5Rh4BV5pz-CgqsCJqT2wTc4yunU-xkOyy1FtiNj3omNVa2ktlevcS8bd3K06WDPY1flwovpTsDsS3K1CohGWQ90IUy99W2AQx7-s3TJPg70tN-fOS-YaI3-wkWLGgjv1La4OUlR_HIQQ2KVLkFkWLXb3YHzOcBEPABMUWjmYZmCIMzGRBnBZvZvBuIFf-SXAZ-r4PsieOtH8OH6UOHnu9aTTzwmYgDWP-U2cRD6jvFkQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=vEXB8MxQKcP6NSINjfOBVonIY1vldRrQLX5MzbYyHmApomFEkTeVNFgTmxNCey5gLlOMAhhNrIG5kwEbhDM8XH2vpIsf448qu3735uWP5Rh4BV5pz-CgqsCJqT2wTc4yunU-xkOyy1FtiNj3omNVa2ktlevcS8bd3K06WDPY1flwovpTsDsS3K1CohGWQ90IUy99W2AQx7-s3TJPg70tN-fOS-YaI3-wkWLGgjv1La4OUlR_HIQQ2KVLkFkWLXb3YHzOcBEPABMUWjmYZmCIMzGRBnBZvZvBuIFf-SXAZ-r4PsieOtH8OH6UOHnu9aTTzwmYgDWP-U2cRD6jvFkQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=F1Yy4PhnHyrSi_UXGB37vqXkYpeZMwU92RhjtPOfz7qL0ZARlD3UL-zS9BrIWCzNVD0mEvkjDcGGmgqmMN4P5aOe7OvkU7mcnwiH9nUPMR0BxRR2QIqgxsICM2Sm97ehi515tXnmcpbBeufVjjlJskJ3SZgxWOMDUy9ZtNpynTB6d44Ne3MuYhoBnHlyYlQATOovBeACdZtbWV7zMVqOqQvaGB1VpIcE6iZehw2iCRPF1XwtHjy1S-o7y3ZBEJbe0JcOegXgtdYf0JKOOpIDbYj87RbLRUsWkflzeoGm92i7NIKT4RhcGXl3HyAGqFC8GaWRn6dNc4MHK8SKTB9XuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=F1Yy4PhnHyrSi_UXGB37vqXkYpeZMwU92RhjtPOfz7qL0ZARlD3UL-zS9BrIWCzNVD0mEvkjDcGGmgqmMN4P5aOe7OvkU7mcnwiH9nUPMR0BxRR2QIqgxsICM2Sm97ehi515tXnmcpbBeufVjjlJskJ3SZgxWOMDUy9ZtNpynTB6d44Ne3MuYhoBnHlyYlQATOovBeACdZtbWV7zMVqOqQvaGB1VpIcE6iZehw2iCRPF1XwtHjy1S-o7y3ZBEJbe0JcOegXgtdYf0JKOOpIDbYj87RbLRUsWkflzeoGm92i7NIKT4RhcGXl3HyAGqFC8GaWRn6dNc4MHK8SKTB9XuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=OiNg9I4ZDPMPDrUAUG-bnb2HG6REZQhTfRsVJLhfscaJDmg7FZ0kfBl6Z-q44vy1U_sa6gDnxUkBP9fdZG6H4_x31yGGzuyux_y6iitvYqqxX-DMP_z9aaq29TPs30Ep390Svgx0IwjrzmF3s6ISXeyBoqs5OaD7XbubBng-Nyps1N1E2nIKAZ2cYWV5DwmJQNJAVvumyHiWSzc5iETMDGKBc1ToqgogUeCMohY4oa7VMu4PE_v7KVq0JTABQxvsPckRfHF6ynXCFfl-OVgtoFs2wk7jD5YWUKtpy_lCH_4jFeNKmu-YOH2ZVZMQYACjAfrA0lm4qSOPBUMemCHugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=OiNg9I4ZDPMPDrUAUG-bnb2HG6REZQhTfRsVJLhfscaJDmg7FZ0kfBl6Z-q44vy1U_sa6gDnxUkBP9fdZG6H4_x31yGGzuyux_y6iitvYqqxX-DMP_z9aaq29TPs30Ep390Svgx0IwjrzmF3s6ISXeyBoqs5OaD7XbubBng-Nyps1N1E2nIKAZ2cYWV5DwmJQNJAVvumyHiWSzc5iETMDGKBc1ToqgogUeCMohY4oa7VMu4PE_v7KVq0JTABQxvsPckRfHF6ynXCFfl-OVgtoFs2wk7jD5YWUKtpy_lCH_4jFeNKmu-YOH2ZVZMQYACjAfrA0lm4qSOPBUMemCHugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kee0uL3Is74HZeUoe09qLvns1law0UxsREDpFBmkX1awb-FOB2MNKERO8G5_uGHX_UL2T7HqvmDUSaoU9b_zEnBEquJgkJ_WrHE4W9FrYiQk6on4QCAEN35lT0oADO7Id4gbgCQCae4OnxB7jJzWjGJAkML-6oG5dfPSciP89ZOIImCyP7-dX3ztMOmhH15YtPLYSFo8acW8qT-lZyn0jCoRg2HzFnRpZcDxqQJQcRA07wMq0T8WdDijKohh5oWcTtaJiDmCkNI-otzAKsht4hFBYpr8vC8bjAwslDl0U7zv0LqwKsI1zKB6ivJwNeoN-I3B31WRnAh0FCg4LcNswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5z_b8id8gVTLWz4FrQmt8XBV4YwcbXsvky21LczrgkF2eFnSCXqQSnzkk3buxEBzOvYK1FJc8gMPIXyQ9QJoftNXB6-LcAQL5wkyancJe_CGD6iXlHMagurtjCDpKflcUOUD1BIvhB477S0YEGe3KtaRyKMnkhltDvuynFIoEQjLeFaUDxu5AGUQP7jx6C8ya1XwICWhmzueu_Vk5fl7P7jqGnKt7WIF2aKuZBzqsCaIrja10SgRM6pvSfcstNVzhMR3vdSJrqrie3yzd-8a_MszCGM6gJfQkBTxqhUiwCHofQDQV-4-vqBkqBrCcQmGYhw_sDLR5Ub03zANiIdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IX_HtTlzzyzXJ6r8e0RhnXYzcJdU8Yt05TSt1kQhZAH7diaMPWz6S458Rx1w-7kJ2UqtfqKpwQduuvBcLmz92UfnJxiybBkUUndMk0fGNPpCdwkFTu01i8fvFIMakbuAws-Uzb3MEJNDLH8s6lfY_pEXUg23H9btDXJxqf9WvEk8HSx3jbWyTX4OVvf6F1y3ZQKpoPkslo3sBrGtLhe9wVWCzuFnq2fvZwpcBqeI_1XwZ9NQpuPJfSvvkS4QidkPK_va9q7nhluzX4b7Ib4ATgjd7Uuv6tvPpcYegW_ehhfRnvnoSiJ_F_gLRXhhvSn6eeX4nuW08pZJkYHRCPStBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=e6hr9EFaEqxZ1qwYXdpnPaQDJjQLdBEWXwUbLjOLSCS66-_w6A0MgJo7LyEh-BoASmYg8WWXr-9NhHhROKxmQdGNh1TAHlgMINL_MPglouCkgV1Wx1NdVKqcleSSPjORXiu-m_EJMaZcOHQMMKBm8KEL26G4cao-b4HK5kIpxCYbfarut_9EhqzKElvXRmdkONKUT-IKzKTrcEkkBsxjf-0Epq_oWusdZq0WiBe16lyXWVO-Yd-o5Uv90qeEVl9x1oKupAZ3bEjBiE2yrc10bVll-6er3Qv-4p4rgT7jhzectG0qrLt2zuaWHz1lgyNKevzfIKq_YKWFAtxuc9HV6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=e6hr9EFaEqxZ1qwYXdpnPaQDJjQLdBEWXwUbLjOLSCS66-_w6A0MgJo7LyEh-BoASmYg8WWXr-9NhHhROKxmQdGNh1TAHlgMINL_MPglouCkgV1Wx1NdVKqcleSSPjORXiu-m_EJMaZcOHQMMKBm8KEL26G4cao-b4HK5kIpxCYbfarut_9EhqzKElvXRmdkONKUT-IKzKTrcEkkBsxjf-0Epq_oWusdZq0WiBe16lyXWVO-Yd-o5Uv90qeEVl9x1oKupAZ3bEjBiE2yrc10bVll-6er3Qv-4p4rgT7jhzectG0qrLt2zuaWHz1lgyNKevzfIKq_YKWFAtxuc9HV6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=hL-wqyNHaHJyTxaow880c4bswMjvz3A7VX5lFsFSsPYxVKbTikba7VCqjfj8ubcEonvP73LKR8RTkufjpoR4snh_0lQnfBvMGPdtQGPFcGkn0qZCEA3wmbCg_vl8d1BSrkhX6rkJ5DTYmgLWe3_e6uGKa2WYDduCs5cRL2r4ks8wh7la45F8CbupoKkas3HUG2Oz1kH3DaNaMH46BLLSseawSM2XRbMK5JCwF4mtgUymNjc6NQF7zBk8SREp3OFNPRr5YYlbazEfjEgrGYTsou5f13WFBJWxCr5YGUPWyRdWeJcDsMQZ7QK11i7TUw7hwzYwkIXieQpOV-DnAe0iYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=hL-wqyNHaHJyTxaow880c4bswMjvz3A7VX5lFsFSsPYxVKbTikba7VCqjfj8ubcEonvP73LKR8RTkufjpoR4snh_0lQnfBvMGPdtQGPFcGkn0qZCEA3wmbCg_vl8d1BSrkhX6rkJ5DTYmgLWe3_e6uGKa2WYDduCs5cRL2r4ks8wh7la45F8CbupoKkas3HUG2Oz1kH3DaNaMH46BLLSseawSM2XRbMK5JCwF4mtgUymNjc6NQF7zBk8SREp3OFNPRr5YYlbazEfjEgrGYTsou5f13WFBJWxCr5YGUPWyRdWeJcDsMQZ7QK11i7TUw7hwzYwkIXieQpOV-DnAe0iYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=C3MpPfDypBq6ZPwiBSABAS5BLzuZgJX39HHre8YsddCADbi-sdSCuDOCGIQFJMDaFvI4vdXqs22zWrlN-yKAZI6RlRiH7bkt-zsSlZ4rD1rNLnR9LYXav628PSshZufdYlXARxQr1C-4JDDsY4UaJq4yAC8777uLNf7Vmhf8Gz8iW432QCT6WdKmlNAab7726wYhi1wT7IW0htiO9NN3q8YewNMWZtMO-jMXJzJEYecNa9kd5_ngWtXhmHrNxhlRCnYmk_vCSTPEvPmgCX6aV2WYpTj5wgMdRWVnve5zHNYmtdVt1KvOBoWK4mlbsTLPemBqhC9A1LmGY5hgqW6eRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=C3MpPfDypBq6ZPwiBSABAS5BLzuZgJX39HHre8YsddCADbi-sdSCuDOCGIQFJMDaFvI4vdXqs22zWrlN-yKAZI6RlRiH7bkt-zsSlZ4rD1rNLnR9LYXav628PSshZufdYlXARxQr1C-4JDDsY4UaJq4yAC8777uLNf7Vmhf8Gz8iW432QCT6WdKmlNAab7726wYhi1wT7IW0htiO9NN3q8YewNMWZtMO-jMXJzJEYecNa9kd5_ngWtXhmHrNxhlRCnYmk_vCSTPEvPmgCX6aV2WYpTj5wgMdRWVnve5zHNYmtdVt1KvOBoWK4mlbsTLPemBqhC9A1LmGY5hgqW6eRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=GGAutW8edx4IFlIEBYnBdbBKYS3YKuRiqGEEIPhpWH8-2Nim1DpRKAdSVo49ZUXyqZbpSDNQQjD3mGqnGjC3jOFD7XiHPm4xPGoLW4faWzGAP6f6fKZMDgczdUasVZqmt-8br2yoO3GT8H2uK7ei4fs-aaKfyRN3VvqRpR-zGj8NNBYx_cNiVnet6aswArPMBrysh_I8EtPcczBAJNX7Ralcip23YX3KnePOO8GvfU-PphVJmqccZhurQPqcgp35AsW7k1y3CSsTNGs9RBu-rwtERtWJ6d0jmDIgtFpsRPjVaksFp7sjdqOq28hSOOpsmR9pCJeZuaelBTQKV-jlULGKfpYMj9jHGH3g984fqatKrTCIFylcLPw-s-lE5Ibzo3IcHutO9OhtQbTe9qUWJB_4cr_KCJD27yclee6-Q1uX3cZAXvZsaROe-DPMbxRB4yeg3Qd68-5YaCtAKjHHgn7E9GhSa3tB6Uw0wBcEAjp-EmOps6eKtx-9VrC50Zm23bj0PGcFl75j0vLHhTJMwbbODJMH0bX9evWCxYzmJ0WSqYjjywNuUWdfRv8xq6P7mN8OnTp5KB7xmHrGjtjwY4urXa4LvC2RAPTKYO1QtkJdGdzFX4r5w_VDAH2UX24pGvDwdQ7boH7S8afXUFdJ2IYbJIfUqiAj-BztjzlOATs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=GGAutW8edx4IFlIEBYnBdbBKYS3YKuRiqGEEIPhpWH8-2Nim1DpRKAdSVo49ZUXyqZbpSDNQQjD3mGqnGjC3jOFD7XiHPm4xPGoLW4faWzGAP6f6fKZMDgczdUasVZqmt-8br2yoO3GT8H2uK7ei4fs-aaKfyRN3VvqRpR-zGj8NNBYx_cNiVnet6aswArPMBrysh_I8EtPcczBAJNX7Ralcip23YX3KnePOO8GvfU-PphVJmqccZhurQPqcgp35AsW7k1y3CSsTNGs9RBu-rwtERtWJ6d0jmDIgtFpsRPjVaksFp7sjdqOq28hSOOpsmR9pCJeZuaelBTQKV-jlULGKfpYMj9jHGH3g984fqatKrTCIFylcLPw-s-lE5Ibzo3IcHutO9OhtQbTe9qUWJB_4cr_KCJD27yclee6-Q1uX3cZAXvZsaROe-DPMbxRB4yeg3Qd68-5YaCtAKjHHgn7E9GhSa3tB6Uw0wBcEAjp-EmOps6eKtx-9VrC50Zm23bj0PGcFl75j0vLHhTJMwbbODJMH0bX9evWCxYzmJ0WSqYjjywNuUWdfRv8xq6P7mN8OnTp5KB7xmHrGjtjwY4urXa4LvC2RAPTKYO1QtkJdGdzFX4r5w_VDAH2UX24pGvDwdQ7boH7S8afXUFdJ2IYbJIfUqiAj-BztjzlOATs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=YWqWJAMTx-KCrNQHNKXWzDLSLk9RL9itjoAxS3ctcOEygXPeHKKvkQVax24Ln9n_LS8VKIw3D311MHOgC7cIQhqL7wrnzhxL1Q_f6WbqU4zXV7ugQWxR8C5D--8S9Zhw_XxIpOblnIfkbRDuuZ4JcuPnZRbAzSZvtfs0BLrWo0Gexh_Ik3Dw_sooZ16WYkJthevha2VE90RIv-O72l-iwGkpge38Y--n1gLpmVDicHx4I1Jid1V6DiSJGtH2IFRy0pgJ_P9Yi5uidNUacgy3TrCarjBzBYlfertFS75f-F7yGUv7oWwegyZQfAdfjTJ4ZDnxakHmxLirLlUCWBOOBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=YWqWJAMTx-KCrNQHNKXWzDLSLk9RL9itjoAxS3ctcOEygXPeHKKvkQVax24Ln9n_LS8VKIw3D311MHOgC7cIQhqL7wrnzhxL1Q_f6WbqU4zXV7ugQWxR8C5D--8S9Zhw_XxIpOblnIfkbRDuuZ4JcuPnZRbAzSZvtfs0BLrWo0Gexh_Ik3Dw_sooZ16WYkJthevha2VE90RIv-O72l-iwGkpge38Y--n1gLpmVDicHx4I1Jid1V6DiSJGtH2IFRy0pgJ_P9Yi5uidNUacgy3TrCarjBzBYlfertFS75f-F7yGUv7oWwegyZQfAdfjTJ4ZDnxakHmxLirLlUCWBOOBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=GNf107zgdTiIJezG2QvuxskzUpeR5IUz5M5wYSvGk6aiv8hCvT7OHqN1WsvSLIO_ggYHriGzJFJvvW7bku01G3wUuISwjg5t3A5djFz7oM7ZakCDFl3hYaBGJcPkt0EZO_jTye0W8Aai1ZODD88gbtCMGm1kLVi10MjFjtFSwh3d4n_gJ-jZDrSifOWwhqlu1WRllfhgJHgDp4XrnLqS-bxHyw7MYkWE2tS38jhJNTVHQK3Sd38LbiImQj8DQemFpNbZ7gFuikzJMWRx8GCTa70K_R5Q6bNMeLCq3bip8QF_x51cYgQEO31PPZIKHcwCJ2DDMO_Ls6E5MFheG-9kSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=GNf107zgdTiIJezG2QvuxskzUpeR5IUz5M5wYSvGk6aiv8hCvT7OHqN1WsvSLIO_ggYHriGzJFJvvW7bku01G3wUuISwjg5t3A5djFz7oM7ZakCDFl3hYaBGJcPkt0EZO_jTye0W8Aai1ZODD88gbtCMGm1kLVi10MjFjtFSwh3d4n_gJ-jZDrSifOWwhqlu1WRllfhgJHgDp4XrnLqS-bxHyw7MYkWE2tS38jhJNTVHQK3Sd38LbiImQj8DQemFpNbZ7gFuikzJMWRx8GCTa70K_R5Q6bNMeLCq3bip8QF_x51cYgQEO31PPZIKHcwCJ2DDMO_Ls6E5MFheG-9kSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQuHgivrHDcaSsQOTasHqgP8UNtPlDiFNYGHhpsHERyu-JbjGBem3nne_b1qbpQgQx7a8AdyxTWEJQc2HrXHqDvYmC8jpr7267ETa5QiSVLqPR29SUEiiAb9unvfjR0YUsPUIQqAC1iFmbWUil9HUurs3-r4gGLKiZKRlUgHHCpTrESh1Svzc45knLPRhH7q8dEBCcnai6VdTae5X74TSWM_Pd7RzU483BXoE0vK9aYdU3qbuKck_PG2_WdG4bJO-7MfAKZsGyIhAG1J6_3iev2HKaAYFcooVgSsNchLbm2MY8Lz1GLkkCHdSTkOqYnfa0-VMOq93adeaLI8jkXgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSRF4eWBEXi-A9s8OFiVdE-ytSK_6d4oWNUiUMRp3U_ajrUAPIwdixVz7STpmWc9Y7T0PPA4mrhLLh4hPxvOtydMoVUypiJcmI44FM72LC8ZGRP1612MDJq2zTCl9QmHSTL5Iiy0t8VUuwONySEPbtf--_UAuLCz5CE75Fe7V0H1EeX4PnyqJGR9pKMo4EZsI-IUmT4MliQhFVJ8DpKnKlLAekYeBDRVSoHB8S96mawTMlRj-Npl7m0qZs_yiBr4kMg5BIMyT6lP0v_zgwhcucI9kty5geUE92caOoCmZMLlmb06kjv10TwzYqaIwO7PmWk3w45P3V4T24AOXRlxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=iDmYRUXwBx2MtFk2gy16ktfpDj9SiFPdMouiD5OqXKApGlQelW_FoTUCieqPePz1sB1S0SCOoxh_XhpZRXOp8GhtKkg9v7fFpIk7SFDk51sOVZH-gX7hOl3vFCYJNiVYkDWJAdusrkgJtdE-bSSLc3DNqYG8Fp0Y5D_l_i7nPIad5v1x23GP6wx1vrS-JEALTfKrEMzpApcaB2YcqbSsfAVWbxuqP6Rz9EyB5FN6Bk_BK-ja3d_60iHqPqFtlITJgBxxoewf0sgGUR7MG-6xzyZ62NiOZMCQ2z2LGkKm4Si17LpUCTfHU5GsymVXKQ_9XMBX7dKu9UQcbMtp7bJbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=iDmYRUXwBx2MtFk2gy16ktfpDj9SiFPdMouiD5OqXKApGlQelW_FoTUCieqPePz1sB1S0SCOoxh_XhpZRXOp8GhtKkg9v7fFpIk7SFDk51sOVZH-gX7hOl3vFCYJNiVYkDWJAdusrkgJtdE-bSSLc3DNqYG8Fp0Y5D_l_i7nPIad5v1x23GP6wx1vrS-JEALTfKrEMzpApcaB2YcqbSsfAVWbxuqP6Rz9EyB5FN6Bk_BK-ja3d_60iHqPqFtlITJgBxxoewf0sgGUR7MG-6xzyZ62NiOZMCQ2z2LGkKm4Si17LpUCTfHU5GsymVXKQ_9XMBX7dKu9UQcbMtp7bJbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FiOwk7jtSOiOw9iZwNVYowb1SYVPNHxt3QF1xMjnooFOdvoXi470Av7ChAwWwQvv1YIGE2mqYk-ao2gwbsfJ0JkooS0_8JE4vfqBP-OdhtoGSLufft7TBsQKQoFDm3t6VE9ecQhFOhNzTaI9wc4jCwQVbw1u3u_31fwlGtL2LVd7xs_1jLDTsvPA5eW5UfapiC6eGtkHRLy2dDT4uAeO4wEv79rPBJs4ZTIlaW30_MPnXDLOzhaj3jsOA9L4P4n6homYZZt54UbTUweI5tN08VFZXSHqLjmjMKmKy5QwHiRbfbRwctPIKVbD6S9KgT3bMehrtez0GlELgOhRdjbE6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FiOwk7jtSOiOw9iZwNVYowb1SYVPNHxt3QF1xMjnooFOdvoXi470Av7ChAwWwQvv1YIGE2mqYk-ao2gwbsfJ0JkooS0_8JE4vfqBP-OdhtoGSLufft7TBsQKQoFDm3t6VE9ecQhFOhNzTaI9wc4jCwQVbw1u3u_31fwlGtL2LVd7xs_1jLDTsvPA5eW5UfapiC6eGtkHRLy2dDT4uAeO4wEv79rPBJs4ZTIlaW30_MPnXDLOzhaj3jsOA9L4P4n6homYZZt54UbTUweI5tN08VFZXSHqLjmjMKmKy5QwHiRbfbRwctPIKVbD6S9KgT3bMehrtez0GlELgOhRdjbE6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=hgW_5NwDo8WbJA-DnMNQesaNPkCQFgL0_e3jAiWvYgeUmApEcx8nNtCAsJUCpwqEuuXuRIoF11RFzWO2_3gewxVCbGYKSCqbvQ4ycJeD_DSArJOlSgIs4IgIbFWuEUzDa1iQxzupza6pmBh1X7CT4CZA3rMG26Kz01BlgDUaZEytZ3Z1rJwlOFn0A0dWyygFsgHdqft2S5IHUX37JkWAGRPs5DfkSOJYNASizDQo3SZle-pKrQCsd0fAgFBQpfJuIB8VAYbetFwM5xQnUPUSAVCqnRyyII5WAYy0_7nhB84GS9MGYeaqFRJifQLzEYKZn3cD1faDwpqQGe5qt7qSPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=hgW_5NwDo8WbJA-DnMNQesaNPkCQFgL0_e3jAiWvYgeUmApEcx8nNtCAsJUCpwqEuuXuRIoF11RFzWO2_3gewxVCbGYKSCqbvQ4ycJeD_DSArJOlSgIs4IgIbFWuEUzDa1iQxzupza6pmBh1X7CT4CZA3rMG26Kz01BlgDUaZEytZ3Z1rJwlOFn0A0dWyygFsgHdqft2S5IHUX37JkWAGRPs5DfkSOJYNASizDQo3SZle-pKrQCsd0fAgFBQpfJuIB8VAYbetFwM5xQnUPUSAVCqnRyyII5WAYy0_7nhB84GS9MGYeaqFRJifQLzEYKZn3cD1faDwpqQGe5qt7qSPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCJxiU5t2tpNzjUdAi96d7uBQgXZNMLAJn9Sav3dNN718PmxQteRhx12OCdN4gxyIJy0DJYi0UxO8vuI6R_mp7JvRwY-DsTNeQolecpURj73GNMEPD1w2FvWffcp02X36qqi4yr3SRSpSq-lH9BA9Mg1kkas_7BJd_gJctG2E_TEtEwrGIdVbFVZ1mupYHlqyN8gwsTRPDoKWxNjarcaCgtxW9D8a6334xQpqDp7CGvBTmTMTSmjWu-HQsLyaK9qMnzic5B-47hmSLbASqN3Xy5NuRzU95N9IwxqQkOA3-m4Ax2eQVuTLn6_vgUE_cDZUNTkHUG4UAAO-pgWXTkiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=eY-qn4cexZDNWV67whtTh572Psj9Sst753Hxq9H4siKVB832zLJ8H3Skad04SvpJR64VG9Lhc1kctJ-sgis-9xpWA-SzupFVD0hO7gw3vInFaiikEwDQ7mTjXWY4719FKMVeC_Vt8MEF6X7OskXOyGOrc0Gz0OquiydZ5LxURsOTDMuygzThKdv80mP4mhfjnqxDtvBrnWWO6vZBZm4Z_lhdUkOFSaxSV_7kclHyxeE7x_QUGlv9lJFTDmJRbzGs-XN5b11H8lhvb0mC4AiMGJj5EYOi-i5D0n-L597DfJKFTqYC6k5EFf-a8ytcp4kZg8lM_P0tpSTTDivI6oTORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=eY-qn4cexZDNWV67whtTh572Psj9Sst753Hxq9H4siKVB832zLJ8H3Skad04SvpJR64VG9Lhc1kctJ-sgis-9xpWA-SzupFVD0hO7gw3vInFaiikEwDQ7mTjXWY4719FKMVeC_Vt8MEF6X7OskXOyGOrc0Gz0OquiydZ5LxURsOTDMuygzThKdv80mP4mhfjnqxDtvBrnWWO6vZBZm4Z_lhdUkOFSaxSV_7kclHyxeE7x_QUGlv9lJFTDmJRbzGs-XN5b11H8lhvb0mC4AiMGJj5EYOi-i5D0n-L597DfJKFTqYC6k5EFf-a8ytcp4kZg8lM_P0tpSTTDivI6oTORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=j2TCOzXoEG_vJKDj48FiKXlVHTIdm6xFiVsnQhr9k3g7TlVEBs6VLF6Q_ebOYXr4UHLW2Tu5wo6k_qC3FG8qN4HFud0u2MNevvddbKk2Qw0u-enGFfKxS-e8XTZ8GUjerYzukgZW1ro63tPtlqs0-1mho6pWvS4_KmqR_Td2gglLAvXrMo_3-k2LO5HPJ1igtFaZjXhevpHJYM3rA5vkRV6RNn4Owkm1L_D6XJPaTMOkO-DyYVlXTAlFyHWruyS-ze0Z4ZFPp6STm9H_alTbj2rnOXsp6sorqgCa2GBXLI__7IWCC9YpA5WkAruWlJt9r0bfhp_m-aYi8LIprPOtww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=j2TCOzXoEG_vJKDj48FiKXlVHTIdm6xFiVsnQhr9k3g7TlVEBs6VLF6Q_ebOYXr4UHLW2Tu5wo6k_qC3FG8qN4HFud0u2MNevvddbKk2Qw0u-enGFfKxS-e8XTZ8GUjerYzukgZW1ro63tPtlqs0-1mho6pWvS4_KmqR_Td2gglLAvXrMo_3-k2LO5HPJ1igtFaZjXhevpHJYM3rA5vkRV6RNn4Owkm1L_D6XJPaTMOkO-DyYVlXTAlFyHWruyS-ze0Z4ZFPp6STm9H_alTbj2rnOXsp6sorqgCa2GBXLI__7IWCC9YpA5WkAruWlJt9r0bfhp_m-aYi8LIprPOtww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=qGKOgbng7hmcy2G0UlJ7VXXVzb9Byb4LAF6JsT7g9nTIxLF2PMEp8Wzr2QrMGo7lOcL_8Y4HhfhpkPi9LYYmi7pBzveBUrCDx756hMe74_fL0s23rE66aCo1KNNuB11GTO3V8oSm3QBb29X6H4G6AEMtjKZWiAwpmn2pqq0FDxOThekFH0AyPo8PH9Slu3FZDSYB2qy9DQXnOqVFll5NskvT0pmbcnp4_gbaqwdR2IBY2zp8zDizB6blac7g31kX3xldxeeU3j2Zg5P2nAu_VrMMTAX_AnAIV2h8OwN61iNuIbsPEM628MVdMw8S_WBE7iulVWW6qrTIpDJ1wDcnPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=qGKOgbng7hmcy2G0UlJ7VXXVzb9Byb4LAF6JsT7g9nTIxLF2PMEp8Wzr2QrMGo7lOcL_8Y4HhfhpkPi9LYYmi7pBzveBUrCDx756hMe74_fL0s23rE66aCo1KNNuB11GTO3V8oSm3QBb29X6H4G6AEMtjKZWiAwpmn2pqq0FDxOThekFH0AyPo8PH9Slu3FZDSYB2qy9DQXnOqVFll5NskvT0pmbcnp4_gbaqwdR2IBY2zp8zDizB6blac7g31kX3xldxeeU3j2Zg5P2nAu_VrMMTAX_AnAIV2h8OwN61iNuIbsPEM628MVdMw8S_WBE7iulVWW6qrTIpDJ1wDcnPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=r3EsrkPT3SvWO_9sIPBu6gcJkKPKwpUzphGaEDRBPfr0WukiPfBdVWB2_Gm_WQN6O2oxi21jrLV0uETF--AH2AFuuQvAyX0tcMp_RhCAaussYibTNObNZBnrOolAoVu545Wu_lUQ5t_DqK4RzWiz0lcn5Bf4a_ZBsorlpUlqbb54WjSmXYWC7sPotkq3flpqucTHlmMGra4og1d7mr8ddu3eddOtgIKLwqYgdBvNgj6T8w0xmX13yCYoXa1kL3pSJI74kXKFqZu7fItXxUP9L6d08erEisXDJimhohJQwQRdeb0zJlpe1gCUGIHCfBHaMwnZqlOoq0gX02PcKMHu4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=r3EsrkPT3SvWO_9sIPBu6gcJkKPKwpUzphGaEDRBPfr0WukiPfBdVWB2_Gm_WQN6O2oxi21jrLV0uETF--AH2AFuuQvAyX0tcMp_RhCAaussYibTNObNZBnrOolAoVu545Wu_lUQ5t_DqK4RzWiz0lcn5Bf4a_ZBsorlpUlqbb54WjSmXYWC7sPotkq3flpqucTHlmMGra4og1d7mr8ddu3eddOtgIKLwqYgdBvNgj6T8w0xmX13yCYoXa1kL3pSJI74kXKFqZu7fItXxUP9L6d08erEisXDJimhohJQwQRdeb0zJlpe1gCUGIHCfBHaMwnZqlOoq0gX02PcKMHu4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=pjq3h2q-X0ALMAwpKdAShO6qSH7bjlxeUaAiX99wFoZmt7IwpYXXZQrG5KnW_zY34oXd2cMr-mFRtWGF9wtasi5JU0DtUhEzQConhxPJe094ZSRfuXhZRnLocLn8Td6eWB3gHvV_su2meg7ZunRtUUE7Ys7LbT74vufl6igdzAOQVDWFi4b39PTiWDaaiiOCv6BX1l15W9UR6DuspLiFcI0mwv9s4Bc7E95q9xT5NHGqfjtmKpTIU8Epfd0K7xgQWeIqnEfqb46eLV-4Fq-lrGKCks_lc--nucqIq-c47fQT74nf5o2Qauah2_9vc_5ghegxngaMyxbsCx-BMf-gpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=pjq3h2q-X0ALMAwpKdAShO6qSH7bjlxeUaAiX99wFoZmt7IwpYXXZQrG5KnW_zY34oXd2cMr-mFRtWGF9wtasi5JU0DtUhEzQConhxPJe094ZSRfuXhZRnLocLn8Td6eWB3gHvV_su2meg7ZunRtUUE7Ys7LbT74vufl6igdzAOQVDWFi4b39PTiWDaaiiOCv6BX1l15W9UR6DuspLiFcI0mwv9s4Bc7E95q9xT5NHGqfjtmKpTIU8Epfd0K7xgQWeIqnEfqb46eLV-4Fq-lrGKCks_lc--nucqIq-c47fQT74nf5o2Qauah2_9vc_5ghegxngaMyxbsCx-BMf-gpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=WAUHx4P4aI9qENdfpikq_b5EorFFzSpEIETlbhKfUN4a5G_VL1yWZQp9jJrgys5e4ICEmhTzopBNNowKB7FSIREFF_6lp8EduueABA3b-1Gsq40gpV00lZRSGREEgrh6b0SQjq196CnBqHLs6ELLvn7eaP2J5-JwNjOWTmEOcGQqxaxQDKxX1Ba-VlCA2aL-_-D3uTFnMtIUcaPn7BBanj2SqicpauqNyvZn1NbPZi6A7VQxNl6GMqd3NlMhCY9TSBFtQ-Xd4uBnXC46XZFsY09Bt4ji56rROlvF82kqTtNmOi6GsD0KW_4W2HOQF1wcWCvKOqJx4ebRh3661qOMjCt3Vc2Va9bzEAC9-GfRwSx6txnZBz0mKhzL7TJlwO0-N5vgRzR0e7HWy509Tbaxio0X0GZwHL1VOxMEdXU4tCDnHHpe28ak_5q84-vL-Q_bV1GIBHNU7CjxdgnvEOFw1q0c9an65LKjIm_oDiIbfPYFImbR2Y909vAUqzzfk1MjyZUPBjNq2273tp_4iSl5kkxXJycLxEnnHB0VDKXiTTfgiRZpVvJXBaf9z2pul5vLtmej_yQJW_cu5IF6mceyjZVxuIP2S66IyBViNJCN_Mpgz7v9ZwRaf_nbrt3nlR-D_cjNQMwhJXmZRGfM7TIcd_BWUiAH9djNn0RIsOxkbqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=WAUHx4P4aI9qENdfpikq_b5EorFFzSpEIETlbhKfUN4a5G_VL1yWZQp9jJrgys5e4ICEmhTzopBNNowKB7FSIREFF_6lp8EduueABA3b-1Gsq40gpV00lZRSGREEgrh6b0SQjq196CnBqHLs6ELLvn7eaP2J5-JwNjOWTmEOcGQqxaxQDKxX1Ba-VlCA2aL-_-D3uTFnMtIUcaPn7BBanj2SqicpauqNyvZn1NbPZi6A7VQxNl6GMqd3NlMhCY9TSBFtQ-Xd4uBnXC46XZFsY09Bt4ji56rROlvF82kqTtNmOi6GsD0KW_4W2HOQF1wcWCvKOqJx4ebRh3661qOMjCt3Vc2Va9bzEAC9-GfRwSx6txnZBz0mKhzL7TJlwO0-N5vgRzR0e7HWy509Tbaxio0X0GZwHL1VOxMEdXU4tCDnHHpe28ak_5q84-vL-Q_bV1GIBHNU7CjxdgnvEOFw1q0c9an65LKjIm_oDiIbfPYFImbR2Y909vAUqzzfk1MjyZUPBjNq2273tp_4iSl5kkxXJycLxEnnHB0VDKXiTTfgiRZpVvJXBaf9z2pul5vLtmej_yQJW_cu5IF6mceyjZVxuIP2S66IyBViNJCN_Mpgz7v9ZwRaf_nbrt3nlR-D_cjNQMwhJXmZRGfM7TIcd_BWUiAH9djNn0RIsOxkbqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVl33akQigiK6ryIBpIx6Ua0MxeJYA7rXS_hL8LFtUwPWdIIQkPHMMIZP_daJb7xQuj5mI-aFGa1y_GiIUJHZAEi1f1Tv4eE-hoKmQhOmZqEj9OhU9shxGAkpKa1pj3kJohypsCpm-pOzVY_aFNMTnWDx_hiBnr4A6FAiBey6-R7ev6mkUKM8rT-ocJ40sXgjNFpYbVjGhYXKdlLG7iPMjYfZU6LSjmKnVPyXepjTulJT0fIi2RAmWSh_no_FlgxZyFwMJ8pRfzt3iQFRJdUbzORNgWjrUZiRS7wqes3EB6SapWtmT62Ma18OGmKBRVodnN4notrw56cu8h1oUz5Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o7iWTYA0yv69Mm0GGUGhyYfVI9MDsX0NRT8BTTWkyp6-xsuOR6MDu4xIM5eTyA6bTw5Q4v37kmIFccCCz06aXDQ1kvD8HigsWcgyQDNpI3rx-EtQ3qQyQEPb1hln0r0igqwOEAEwH1ygrwRdCXfzZ_s89DX7lfvTz3XwcDKVGCxMkp_e38teceMfLTxsqICLe7oLFibE20ykiN19sh2n5ZXwlAfZym_KIqQhZuo4I2KMkWGh2BySwQB_B3V4cWknD1GNk5rcW02arJ-be4LlXxGlY6oZEiv5UC_AMRgzpeoA7Wev45wYgJrl6v3awWeGQ3v75DFMbVupRKFQ6Dx5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2oJOpYvh8nHbYC87IMJ58y0vSZrBkUR3cn1f_M-p18EMEbcRLR-6KDtnMjZi8xSJL7EM3rLd3A6ZlxBEktT6sVdhsDZr8o773CzegrAL85ZnLpOV-kNIPEsr1UUYBIxyFxYOdUXkNlUTqri3jioLSoPVV04Ta4O7LrPW7BnEaDHhqelfbbuHK7if1YOBmnvePOyMvhEStGlT4mV1MF83Im4OcLS-v6jZFqFxTEWj6zIw1PGEclYBWzUqVvCnXtgRUFykbX-Vtm0LZMuFXJ6aMmURiIodbZ-hHGQgTDHP9JV_jOfpoevylqwFTmcA6QZ73VM29kK7tGC03c-11boQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=Cdo7fWqNlS-8tca7BLJQR3UiRy2UOnvJHAOd2atzLcDc04lSSTYUSOlo8_1Z5_2koo11AhoyFA_cp3BtuFplqZuLyEfpYDX-hEwx7sGsn8RwyxdJxkGBsFpURJoNwup3lZcsFjoXLlgmtd5ug9FOxYl_8BRIPVYtYj0Hjr6WnZjoMwg4WC6J3H034T2xtH3broiss_IB5WKp413uF9pLswAl12noeWldOAZj8yAN-i7qyP3SaG3vXESstKpnxOWe0T5LgExowIwsvYTD8iuy6LjEufLb201It9ztsIUAr5B9XVsi_pzYn197M-hWsSWb6FgZGuCu73hqoZs6V5gwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=Cdo7fWqNlS-8tca7BLJQR3UiRy2UOnvJHAOd2atzLcDc04lSSTYUSOlo8_1Z5_2koo11AhoyFA_cp3BtuFplqZuLyEfpYDX-hEwx7sGsn8RwyxdJxkGBsFpURJoNwup3lZcsFjoXLlgmtd5ug9FOxYl_8BRIPVYtYj0Hjr6WnZjoMwg4WC6J3H034T2xtH3broiss_IB5WKp413uF9pLswAl12noeWldOAZj8yAN-i7qyP3SaG3vXESstKpnxOWe0T5LgExowIwsvYTD8iuy6LjEufLb201It9ztsIUAr5B9XVsi_pzYn197M-hWsSWb6FgZGuCu73hqoZs6V5gwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=YCVMi1BtrGbbxy0yZyFtC0cXHP_flBJysIxTy0OjImzsAcZx3DQsQymeKbqGEWSSKGJ9ojU7KAitS-dQlM5__NJ3XG-oqpeyNAtdQsVy6Aa0YcfZX2msqnd5sQw0IBRedgFs1zaqnhhk9JD-cAiWidmUCZ_-cvQuwPDZvmAWTt0_2yc9dTGi2fRtOULSLMr9TrVb0eb2jiMEmqLWQHdp5XTSwPLTCdmgd5H5Jl7dvuSl6geaOk3Di8ksuDoCYnN3PuMJJC8qU_ux6qbm7xdJa1LuOy6RB_DmcapYIm_YLL8zmgSKVzBwtxY80ep38M0X5TgI4SujudeBZRgXW5Hckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=YCVMi1BtrGbbxy0yZyFtC0cXHP_flBJysIxTy0OjImzsAcZx3DQsQymeKbqGEWSSKGJ9ojU7KAitS-dQlM5__NJ3XG-oqpeyNAtdQsVy6Aa0YcfZX2msqnd5sQw0IBRedgFs1zaqnhhk9JD-cAiWidmUCZ_-cvQuwPDZvmAWTt0_2yc9dTGi2fRtOULSLMr9TrVb0eb2jiMEmqLWQHdp5XTSwPLTCdmgd5H5Jl7dvuSl6geaOk3Di8ksuDoCYnN3PuMJJC8qU_ux6qbm7xdJa1LuOy6RB_DmcapYIm_YLL8zmgSKVzBwtxY80ep38M0X5TgI4SujudeBZRgXW5Hckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=HR5V7ifuvzM9U9KEurhUICOwqE8ANgXRcSgy7qvhuCgON-aUhnGuYlmYlX4hFRijSZwBgzLYL4ILw39z2eBlOq6MUPHBV_riC_tv3wDm8saQfB37ygkifJe8skBXyIxrsW-XcCUYPLYbK1j-nF0pm40USI3Ax-VqB726KCKwtdcdLAZivmCXR8pj-o-vh_QOHHpP6lwV-KZfTvShquFscf2sMJhmd4ZJQxfyN57PuZILYH_fELJ4qvP0ZI2lU46-RFsqwVLjsj61rVg-ngymndZcxjJPWKMU4dp35p9JjP-4TJ5mDtx2Qc5mOyldKshjqM8d-8rdGh2KSSrQ30LfWKp5sO2PkConY7THxQJhcHT_5M5zObyCYxLhYNw7Q5jCUPOWHu3dmKvjnkBRcjpKXI7CFyLbUc7mCH-5vQvM-B1fzrs764Hm8E4Th-bK8jQNiTB9fFOAw_41QeDuYBpgKfe7qmwddgQXumC4BVYXwDb4UsRWBb7c1stVTodSMjzJGv6Ht5Kngr-GVS_CbGNpNCpPThhClam6Vl_-D8__iaBkRzRUt3WQi-OnNAObNYtnQBB1LC1kEOJQgnzIuQsxqRGK2WFlhQOy24HxDkOc2OC__vXXJjNmJ_HzqrN-d67otZ_q9KGJ35SMYbf44-1p1ZBeqHdB1UAJDg1G4ohV3Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=HR5V7ifuvzM9U9KEurhUICOwqE8ANgXRcSgy7qvhuCgON-aUhnGuYlmYlX4hFRijSZwBgzLYL4ILw39z2eBlOq6MUPHBV_riC_tv3wDm8saQfB37ygkifJe8skBXyIxrsW-XcCUYPLYbK1j-nF0pm40USI3Ax-VqB726KCKwtdcdLAZivmCXR8pj-o-vh_QOHHpP6lwV-KZfTvShquFscf2sMJhmd4ZJQxfyN57PuZILYH_fELJ4qvP0ZI2lU46-RFsqwVLjsj61rVg-ngymndZcxjJPWKMU4dp35p9JjP-4TJ5mDtx2Qc5mOyldKshjqM8d-8rdGh2KSSrQ30LfWKp5sO2PkConY7THxQJhcHT_5M5zObyCYxLhYNw7Q5jCUPOWHu3dmKvjnkBRcjpKXI7CFyLbUc7mCH-5vQvM-B1fzrs764Hm8E4Th-bK8jQNiTB9fFOAw_41QeDuYBpgKfe7qmwddgQXumC4BVYXwDb4UsRWBb7c1stVTodSMjzJGv6Ht5Kngr-GVS_CbGNpNCpPThhClam6Vl_-D8__iaBkRzRUt3WQi-OnNAObNYtnQBB1LC1kEOJQgnzIuQsxqRGK2WFlhQOy24HxDkOc2OC__vXXJjNmJ_HzqrN-d67otZ_q9KGJ35SMYbf44-1p1ZBeqHdB1UAJDg1G4ohV3Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVZYU6UD5aDyg4qqMLX63Wpb3_Hfa0koQgZ3_JxvB73qVe-g3fppftRsCarFVr_rFS-TKFyYvzhRFvAI_8yAe-JSnITndnoU-zZKhRD90BhqY7hVuKZtpecKc8bjNMqXFZkTFHV1FWs80QdBjNHTUkkV0GR9YRHTcZwM2gGvRaRdxDnlqoA8wPAJe96Xj_fo5dQx2UNh1Z7HjC15kvq6NWyVfUQN3LNFXmOnS9FtEC0G9ir94K6y9NRxcSSLFc38BAxZvhcZ9j3SdjuLz2Pmpk7qku5aIxxoeiWKipJUoaC6LJmp7qenjrQrB0K4-res5fL9TaetDyds2y1adbH-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=YMA47ZDbwQDem8PEqk_lL6MfO6iZtIcrPbgI9SECuA7bsITlQ72ijAWbsBRmM4nwHaxDftxpiAxtMr_csc_EJDaAFFZRyLkwoLxfqaVCGAJNmeQBG9R6WShMCcFco4K8MJjsYmWHA9OyE0pzPQLbkSbADGzWWm-l2AdVrjNlfQaoiob6vBbNMkvD1Lfzg8mdeeCJptCFjU808h_3zo18J-9OqiEk9DQQl0XjJRa0DaEG94-q-zdOvWxbcM9J5i9-OecW9OKwpS4857tLOe9_s77uljKPUuXMZhuamy3lS7IytOKGbIXVNrTfw-9mHWIGnHNipQ7DMC-vY59OOkJiHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=YMA47ZDbwQDem8PEqk_lL6MfO6iZtIcrPbgI9SECuA7bsITlQ72ijAWbsBRmM4nwHaxDftxpiAxtMr_csc_EJDaAFFZRyLkwoLxfqaVCGAJNmeQBG9R6WShMCcFco4K8MJjsYmWHA9OyE0pzPQLbkSbADGzWWm-l2AdVrjNlfQaoiob6vBbNMkvD1Lfzg8mdeeCJptCFjU808h_3zo18J-9OqiEk9DQQl0XjJRa0DaEG94-q-zdOvWxbcM9J5i9-OecW9OKwpS4857tLOe9_s77uljKPUuXMZhuamy3lS7IytOKGbIXVNrTfw-9mHWIGnHNipQ7DMC-vY59OOkJiHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=giXHeUf5dYb9QM4z5vxptnv_kb1NLi7xhwdPx340oYTb-bnE2kMhErlZBbCfBmpwtpfMcGGLICytaCF3ainXfTf1tjdRUpmxcClR1ljjPo0LU066gVFSv9owPlzhjxwRcP7mi_vke87OcJtzPXXzBkcxg-qDEcOBs7a0r4kNAn0yYLnApakM69Ahts5UrR3mp0z9nQrYvTXZfYn6cZBtKo10hqHqGtxUg-Y8fEBY-kJcfpnmWtRn01nJ1b65WvGzBtr5PpgUCHzF8TpLPp5eoDfdDJvXAy1Nph2RHRJZkyybNoaC65hpyg-tO1_B2fnatsdazvmtKc-ZbPbmL3txnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=giXHeUf5dYb9QM4z5vxptnv_kb1NLi7xhwdPx340oYTb-bnE2kMhErlZBbCfBmpwtpfMcGGLICytaCF3ainXfTf1tjdRUpmxcClR1ljjPo0LU066gVFSv9owPlzhjxwRcP7mi_vke87OcJtzPXXzBkcxg-qDEcOBs7a0r4kNAn0yYLnApakM69Ahts5UrR3mp0z9nQrYvTXZfYn6cZBtKo10hqHqGtxUg-Y8fEBY-kJcfpnmWtRn01nJ1b65WvGzBtr5PpgUCHzF8TpLPp5eoDfdDJvXAy1Nph2RHRJZkyybNoaC65hpyg-tO1_B2fnatsdazvmtKc-ZbPbmL3txnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=iTUnld2RdI_cUh3_IUAhuI8TUS3O-0qpOC5Lh2aIeGfEszDHuqH06HqnnGkOiObLOQJcbBzKdvsf-_GERPttmWjmUkobhKFylWoC0ptLzm9fjP0qnuwWDUhm9-01PSeGafMISh3RUtmE3W8Iin9Wj2D5PWN-hEp67YD1yDJKPsdIwnnFJCLSVCSD0H-afQtKkTfYqXlHuZWTa0O8n8ttTjaZVbwoUJWXNhYIYS2AxLUK9N9q7EBreFqPHFX3hZ3xbsv_htQan69ST_W-vjZS7ZWayW9obpRU0boBeHMY8ylzFLRYpY6ISx5uG3azqnKqFEsrRB-FquhZC2oA4LcIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=iTUnld2RdI_cUh3_IUAhuI8TUS3O-0qpOC5Lh2aIeGfEszDHuqH06HqnnGkOiObLOQJcbBzKdvsf-_GERPttmWjmUkobhKFylWoC0ptLzm9fjP0qnuwWDUhm9-01PSeGafMISh3RUtmE3W8Iin9Wj2D5PWN-hEp67YD1yDJKPsdIwnnFJCLSVCSD0H-afQtKkTfYqXlHuZWTa0O8n8ttTjaZVbwoUJWXNhYIYS2AxLUK9N9q7EBreFqPHFX3hZ3xbsv_htQan69ST_W-vjZS7ZWayW9obpRU0boBeHMY8ylzFLRYpY6ISx5uG3azqnKqFEsrRB-FquhZC2oA4LcIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emWDgS6ci80vPkq6xSag94jpNcjyJIMJooYT36u2dLV2SWZvM2nTNsEyAWmTzag1vGYLPEKhJMrm9qFTlgPO_Jf2Fc9gD-M7zHNvG_9kVfX3hUOmmZViFo0WkHPk0gdwxE3zE3vMduVX_f5crEB4jiaAjWfjk0mijU2eOhjQf5E9OTr25tGBRdPg8Ydhndk7c9b8STHt_nza-mcKOmskTGGjLXnjnhPQ-bUhBj8XVa-TkHEflHBFpfr2BC7bOXqTxlI0p7VNTBaF5l_uUdGro-FOa8Jmv4y8tE0VxHqiUA47IK-EmA8G174kSLcg_0esSVTSZQe-prF2OwSqPrMVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=fmepps3RFghir_0knmcPYXf8tsoVzWFXM9aZFGFVZPCl7MVYWLrm2X83TQCouJO8VdxGLJmDiDOyaw2UDr3DcXm0Q_MdT_F3jGWKHQHLJdgdUZ2ekpDLFr7mCAm-0jqZCmWVoA4jXEASHN6nYTVtJdYIlDsM0IaRAbK1fx_vOmjkWuUq7qppfsAoBmiuHRpoLI7ygKftnF8m2V1RsHTlQXfzK_UHOrJKaGPsbsEzsmHndPQsGcUVfKlmXq6IfZqSWynBPMOEJ6eV8HIqR6qe3Cb6Ws2JvEI3HizpyG_0nDh43mUQkpDT1WpBlAOeB68GG0-C6v_58PcBdG7JGtpUOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=fmepps3RFghir_0knmcPYXf8tsoVzWFXM9aZFGFVZPCl7MVYWLrm2X83TQCouJO8VdxGLJmDiDOyaw2UDr3DcXm0Q_MdT_F3jGWKHQHLJdgdUZ2ekpDLFr7mCAm-0jqZCmWVoA4jXEASHN6nYTVtJdYIlDsM0IaRAbK1fx_vOmjkWuUq7qppfsAoBmiuHRpoLI7ygKftnF8m2V1RsHTlQXfzK_UHOrJKaGPsbsEzsmHndPQsGcUVfKlmXq6IfZqSWynBPMOEJ6eV8HIqR6qe3Cb6Ws2JvEI3HizpyG_0nDh43mUQkpDT1WpBlAOeB68GG0-C6v_58PcBdG7JGtpUOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=XctpDi_-RJzE4MdN2jH8xl7JDk8tlu0bhl-HRUvP1FDO4tHFGd18witU7k6ParIU3d_P8SO4w0q6HQezKryUxBldMBrprW0t5Bhvlaro7fM6uvqNP6Dy1Dr_kDuxaJ43DM850l0yWSXaJYOrDxMEfjH3TvzXEIg_PmRXwQiQdcQjAwMfnlo5VCMpshoIYzLx25fk48UKv3Aj7EYSD-B0NI3uC2BAcBLnVPgkA0W0FceKipmFJCLpt4RbY-eG9Lm3cBxEHf5Tu87bSU_pBd4GnO9j-bzXb3lZwGEI6sG3zFCHUOp7T6rWaOjwinuOyfn08EUICWASwSaUn0zwZKhwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=XctpDi_-RJzE4MdN2jH8xl7JDk8tlu0bhl-HRUvP1FDO4tHFGd18witU7k6ParIU3d_P8SO4w0q6HQezKryUxBldMBrprW0t5Bhvlaro7fM6uvqNP6Dy1Dr_kDuxaJ43DM850l0yWSXaJYOrDxMEfjH3TvzXEIg_PmRXwQiQdcQjAwMfnlo5VCMpshoIYzLx25fk48UKv3Aj7EYSD-B0NI3uC2BAcBLnVPgkA0W0FceKipmFJCLpt4RbY-eG9Lm3cBxEHf5Tu87bSU_pBd4GnO9j-bzXb3lZwGEI6sG3zFCHUOp7T6rWaOjwinuOyfn08EUICWASwSaUn0zwZKhwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=LbTlRdTwa8g_r8QgD4zRG3Gfp-hZsAXx_EiiuBTxSbMpkHzp3_SAPakwka7k0d4eVFVt0ockfW8z3IHvsELTODWDW8Nf88PzXg0y4o3ASb8SOaUm7HuvB7k2kabcES919dT9r3bJ8MBdnLHZ15vIbnzKNuTJXmIii4Q3gan8T4ybTeYxoBXlsyEMLBtmGMzW6tHiSzHK4sPxiClBwOvf8udmUA4PtwX7EQNXU9wFQl7lsdGOw4MLK0jk1IsHbqEGG72zU3VVu08PG_PaIPAILGFkFhOhCLxWYB5T1-zUh0L1YvIMqpjgfBftQ_XptPe30RL7TI6MqOr9r17MqK4C8hlk-i83bfGOIEyQxb5QPyAlGoqS3hFhHdACoAIkrefiTQpf-GxRMCVKL2feC3s6JPQ9moHrj65Os8jDKu1ONEjS7GXMhwEpa-1IVzkqOrScAgNKIodzUpGuiK7EVREw8m5fk7M7nQTOv443etdjIgTBivweA_nvrMbX-BWSUmSactl72RadROzM1jLu4F5iV1dD-G1tOaJTA60fL-Ft-MnZyo0wR7j4K5kk3KaZMEcakcYAtbCkqpjgEYMkTM-ckKyDBsrx-Tv1SXWiQ3x3KJwEbrTjhqEPYKdtmRkWuQ-H1FIJAQLaP3jOul0HtoXPKDwwxNuqIM35Cp1wr6DSV8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=LbTlRdTwa8g_r8QgD4zRG3Gfp-hZsAXx_EiiuBTxSbMpkHzp3_SAPakwka7k0d4eVFVt0ockfW8z3IHvsELTODWDW8Nf88PzXg0y4o3ASb8SOaUm7HuvB7k2kabcES919dT9r3bJ8MBdnLHZ15vIbnzKNuTJXmIii4Q3gan8T4ybTeYxoBXlsyEMLBtmGMzW6tHiSzHK4sPxiClBwOvf8udmUA4PtwX7EQNXU9wFQl7lsdGOw4MLK0jk1IsHbqEGG72zU3VVu08PG_PaIPAILGFkFhOhCLxWYB5T1-zUh0L1YvIMqpjgfBftQ_XptPe30RL7TI6MqOr9r17MqK4C8hlk-i83bfGOIEyQxb5QPyAlGoqS3hFhHdACoAIkrefiTQpf-GxRMCVKL2feC3s6JPQ9moHrj65Os8jDKu1ONEjS7GXMhwEpa-1IVzkqOrScAgNKIodzUpGuiK7EVREw8m5fk7M7nQTOv443etdjIgTBivweA_nvrMbX-BWSUmSactl72RadROzM1jLu4F5iV1dD-G1tOaJTA60fL-Ft-MnZyo0wR7j4K5kk3KaZMEcakcYAtbCkqpjgEYMkTM-ckKyDBsrx-Tv1SXWiQ3x3KJwEbrTjhqEPYKdtmRkWuQ-H1FIJAQLaP3jOul0HtoXPKDwwxNuqIM35Cp1wr6DSV8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=W42lOdr0shMTuv2um3iRMTzdhimyGCJ-5MmVMjkVyZ13zt9L2GycOPCJxE-po7q9J_Tt16vmGBFK64ABPo8EfZLuivL5x0uybR-Gfzos2FOmEEaObVBSG11Am_BR-pagyVs5_pUB5xcZuWMWr0FU-8DNGaDaJUDpxVobgu0qm0NLyceYltJ8zievD4GmU8X4JjRAqgM6ACsNO0pWLCA-wbElBYprlnryW-zOF94P_C6dj6L8d8OuXeBopr2kezJiYuG6v4HLsz_Ectjjgje8XR15TNjf5JUvlN7gtDUEV-gnxfXykAaY8X2Fe_YVtpIIw0GrNoAAgA-4bu0R4qsOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=W42lOdr0shMTuv2um3iRMTzdhimyGCJ-5MmVMjkVyZ13zt9L2GycOPCJxE-po7q9J_Tt16vmGBFK64ABPo8EfZLuivL5x0uybR-Gfzos2FOmEEaObVBSG11Am_BR-pagyVs5_pUB5xcZuWMWr0FU-8DNGaDaJUDpxVobgu0qm0NLyceYltJ8zievD4GmU8X4JjRAqgM6ACsNO0pWLCA-wbElBYprlnryW-zOF94P_C6dj6L8d8OuXeBopr2kezJiYuG6v4HLsz_Ectjjgje8XR15TNjf5JUvlN7gtDUEV-gnxfXykAaY8X2Fe_YVtpIIw0GrNoAAgA-4bu0R4qsOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZRKo1qn_46Dm72kLduW7x2hoqOeqmWIPkvkYkteP1hJPbu-L3_5OkDApP2bkHdFz6XvyUX0gvlk71T3VM484bDBJdcK23i5vb0NWcvkNUGuWnmR8xqWzzhN3I3dcvp_jEGO_lnTIwOlvvAAUaYEgO7ZfKWqZenfxNClUaPXNdvFTnte4mJNyrPxpP9phMcgMtk-yanmE-Yw8x4XyN4HNP1qqkx90XocmsOGAWLe2wUGIm6xRNxrEtk2Rf25c-36jRo-yAKpGg7basER9l-2RtOS_vD8-egTFfrdZchCsB7fIE4ZDVIgL5j-A82DGTosqZHLSwA9ZL90YcNcuzCphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=L_SwugqTV7RTRiZpj8mbna0towS0MUnf1X0Xn8QOZdBo_85VItmOE0I9o7naBuOs3R2tzrQyaRwxAaHykOHCJirk5AM_N_nPihDKo-BS2gr0AODYo--3wdAJYKCgPAQb4Gw1TuGRLCDZaWrf2N2giiPN97m_AulvIB246UrvfPBOwee06AOAN50OTztltSHUXT33hpeJ5c3soTlgCwVtWJNQ3cWL3j3Y0SVTUbN9_uZ8dsTHJo2_cU0sh7bThYqtmFO-pcHFhq6mDstAbKHzVPRRy7dFq67048Po4Gs6i6Bhq8GVsnJtFLufVrv99dvSZ2dwfzYMuKjA_sLaMDXXHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=L_SwugqTV7RTRiZpj8mbna0towS0MUnf1X0Xn8QOZdBo_85VItmOE0I9o7naBuOs3R2tzrQyaRwxAaHykOHCJirk5AM_N_nPihDKo-BS2gr0AODYo--3wdAJYKCgPAQb4Gw1TuGRLCDZaWrf2N2giiPN97m_AulvIB246UrvfPBOwee06AOAN50OTztltSHUXT33hpeJ5c3soTlgCwVtWJNQ3cWL3j3Y0SVTUbN9_uZ8dsTHJo2_cU0sh7bThYqtmFO-pcHFhq6mDstAbKHzVPRRy7dFq67048Po4Gs6i6Bhq8GVsnJtFLufVrv99dvSZ2dwfzYMuKjA_sLaMDXXHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=blOzNSyxgvNnZ47YMeFD8P9yAF_DMfhW0vcTBB1iQ_Yt0pqNAI7j9mbJLIjKOrIoIEAOT9C0Br1NknlGTZ_4MtmUvs-e867fnflUKat8pFhi9lZqGNr9QIm7eM_k-1EgRjplHi0JrQCfMLt-JmaduRMsXy7U4Jomu7AGJVvoohInldUgqu3NiZm0KWGrQcfp-az_V0VeuECWyPLZFjQ0xsUg01oFiMq9nwvxE7XMMbcyYRa3viPBp22VN7ffo_ho1NYElFPnsC3LbDZl6wcrY16HEJLm3QYcuW7n3hhpGU1-Luc0V1hYGsS2KfWFZ4TQmReLw3QiJ_86yjKiM0CLWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=blOzNSyxgvNnZ47YMeFD8P9yAF_DMfhW0vcTBB1iQ_Yt0pqNAI7j9mbJLIjKOrIoIEAOT9C0Br1NknlGTZ_4MtmUvs-e867fnflUKat8pFhi9lZqGNr9QIm7eM_k-1EgRjplHi0JrQCfMLt-JmaduRMsXy7U4Jomu7AGJVvoohInldUgqu3NiZm0KWGrQcfp-az_V0VeuECWyPLZFjQ0xsUg01oFiMq9nwvxE7XMMbcyYRa3viPBp22VN7ffo_ho1NYElFPnsC3LbDZl6wcrY16HEJLm3QYcuW7n3hhpGU1-Luc0V1hYGsS2KfWFZ4TQmReLw3QiJ_86yjKiM0CLWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=kLuiFbJsYSjBergrymrPb4aG8vVEsPy53pwDKZXBvZXroBygMuPylNzNF3iU55YhgNyhUn8pLLPKrp0GtuEEeelJ5dGFFAjnnT8l7eawZ72bu6Srq_kMTEUbi0edA_oo6Jd4jlVTYDQY_e6x-vmSc_6Fi8hIicXiz9A2d5xTJB0s2TBQLx5uUl7H60Vr20K0jxyMqjVrOvOR1bE43t53Mq7YhS3krcf7aYx5qelnC_f4E8JqNHeAmUYMwkrqMfgChnCtpQONPRitA96NYMQOS0XXt5FC1l5-PCUouO5pd0biHnQToWfG12ZmRv-iBy_cpXVl1dlwoEXxkAR_U3C04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=kLuiFbJsYSjBergrymrPb4aG8vVEsPy53pwDKZXBvZXroBygMuPylNzNF3iU55YhgNyhUn8pLLPKrp0GtuEEeelJ5dGFFAjnnT8l7eawZ72bu6Srq_kMTEUbi0edA_oo6Jd4jlVTYDQY_e6x-vmSc_6Fi8hIicXiz9A2d5xTJB0s2TBQLx5uUl7H60Vr20K0jxyMqjVrOvOR1bE43t53Mq7YhS3krcf7aYx5qelnC_f4E8JqNHeAmUYMwkrqMfgChnCtpQONPRitA96NYMQOS0XXt5FC1l5-PCUouO5pd0biHnQToWfG12ZmRv-iBy_cpXVl1dlwoEXxkAR_U3C04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9dQOOJ-Mj_smZxD_li4UmSEN9JVzrmhdG_7zLJPXjkccW7p3zuy8uxiaXlJHoxF-dF23MqDAOOAttSIoVPLwIERp9ODZjXKMD_O8FSiS7wr81uaFSXzRZ55IT1uMZ0vcC1OLpAghJMbD3r6hz6GYl8QRQc_DX3XiOgnwyEIbA9932Vle9s5D6B7wpRCttgitFbaxiDz2VZhNKiipWmqZ1nNAGvAwe5hydz5Qi5PFoz8VHl2AtnZ7vuHsjFcdwDrNaeKobRE1fOzxOGgQURwH28GZHRxBm2ATUYTLRl8sJdRjG6s-E7MrzaCMrQXwh-qfx3gp7kcqnDs7tejjSImFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=vYUw3iRhBy_wAKatwfefZjP7Kru72Mf3HhVav6c2jf5HEAZ2lzqFRbR53M5w4FG242gBsdM0TfLSX0mz3RtEs2uNqYNHRoznBmBWoHLfNbCeDOH8nMnBB50nx9Zr1zO1RTWCuE3lDPFX3i9uxHfxb5hjmlcRk2YSrGLqbFWHmOP9cF7Gki3gMd0m2pENPI2q0ybX2oon3iWp_4JO__-rZ8Jef5UxRxsJbzqpCxf0BYtvvw0uKduPkEnM-AOzglj9Y9LcuKyqcPXsOb4Qy6qyoY65gZg2u0jceq_s0Dct5WAzAWZHUlv9T-3cmwMNvwV42lQbqowfAWqMCXDQqZEFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=vYUw3iRhBy_wAKatwfefZjP7Kru72Mf3HhVav6c2jf5HEAZ2lzqFRbR53M5w4FG242gBsdM0TfLSX0mz3RtEs2uNqYNHRoznBmBWoHLfNbCeDOH8nMnBB50nx9Zr1zO1RTWCuE3lDPFX3i9uxHfxb5hjmlcRk2YSrGLqbFWHmOP9cF7Gki3gMd0m2pENPI2q0ybX2oon3iWp_4JO__-rZ8Jef5UxRxsJbzqpCxf0BYtvvw0uKduPkEnM-AOzglj9Y9LcuKyqcPXsOb4Qy6qyoY65gZg2u0jceq_s0Dct5WAzAWZHUlv9T-3cmwMNvwV42lQbqowfAWqMCXDQqZEFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=gel1i0HbKTDSYGcqdT-rHp_d8g16R-1RJWLFMMtbXhxEBmQ7HCe3CxLhJJj3uVG2KOeSYLv7A3_3lYQc440xiVgeV67KuDyuv5IRAyck0bzACKSiO0MCmCqUn01zatVD64WHonaQqH_rV_D_SLAMWGV0O9M9O7DDnE6sk51U5vLTarso1jY13EySRqPrgp5azdH5ZUzvD5tYQFKLB1DeR-Ddimqn0O92_AWbIMvR6WrOwbOB9uu29uM9FjWD1dWDNHQRdmVkciU4C0eqertGOY94_bLxf25MM02PVTEYC34sP7H4xi8XTsayvXKkosKHjo26l2bRU5MYz8ihhImOlA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=gel1i0HbKTDSYGcqdT-rHp_d8g16R-1RJWLFMMtbXhxEBmQ7HCe3CxLhJJj3uVG2KOeSYLv7A3_3lYQc440xiVgeV67KuDyuv5IRAyck0bzACKSiO0MCmCqUn01zatVD64WHonaQqH_rV_D_SLAMWGV0O9M9O7DDnE6sk51U5vLTarso1jY13EySRqPrgp5azdH5ZUzvD5tYQFKLB1DeR-Ddimqn0O92_AWbIMvR6WrOwbOB9uu29uM9FjWD1dWDNHQRdmVkciU4C0eqertGOY94_bLxf25MM02PVTEYC34sP7H4xi8XTsayvXKkosKHjo26l2bRU5MYz8ihhImOlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=tu08QuUS6aCoCbMJb0sIj1NLFs5j9RkcWdCv1dOXEDuHiw0FW4kuD4CcKhniCGZFgvigbH7ihl96U1XLzOFSa_Lv_143ZlZwiTSHshSIekeZlNYpktDgrAgfqK2QcpiIIoppvaGyOD2eb5lXL3Sj_d5gYsUKyIDkQnxEe7tv959BEkDXVyPBdA8YzL8DZGHjvHQwcp25YQBFZ2QQlwhpCdF_k-lD7pOP8SaHOKfnS2cwu7Yx9rzW8SPPycUypoPUZP9L4hp-wwajLmvPWsg6a8T2uMtWwwgc0jL1o_xCm-06FPrrHhgTFrYmYk5CLtUwFdHzwS45FgZa_gKAmPQAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=tu08QuUS6aCoCbMJb0sIj1NLFs5j9RkcWdCv1dOXEDuHiw0FW4kuD4CcKhniCGZFgvigbH7ihl96U1XLzOFSa_Lv_143ZlZwiTSHshSIekeZlNYpktDgrAgfqK2QcpiIIoppvaGyOD2eb5lXL3Sj_d5gYsUKyIDkQnxEe7tv959BEkDXVyPBdA8YzL8DZGHjvHQwcp25YQBFZ2QQlwhpCdF_k-lD7pOP8SaHOKfnS2cwu7Yx9rzW8SPPycUypoPUZP9L4hp-wwajLmvPWsg6a8T2uMtWwwgc0jL1o_xCm-06FPrrHhgTFrYmYk5CLtUwFdHzwS45FgZa_gKAmPQAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
