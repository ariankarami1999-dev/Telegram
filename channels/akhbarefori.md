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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-665877">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86a8bc2e2.mp4?token=UMm7rXgh0HhC86IEgBM4NHOH0HP3syDblmF63z7QntbndqAVTEzT1afCXfFboazCZxyswfRf8yFr0YzIDlsmmJFT4Gc1iInAl4Be4Ki1Rtsk8WEe6l6dhS7dAuv-6iGyEPeyaUi_HwuEHjrLqpUQNAWoyXILOndnYyL7wReTIsiAeO4H8VqPLHkWdIAzSfCCdljxRaMggu0n0sg6VTS8wTKlYv5fek3QGBQ-l_NULhYFIGQxxcyqm48e3_B17ay3A7AIM1nt81EI67pX_1jSHdY2Oh8SD7KKjh21SoM6uesGDkTe8a89wnURhaL2UW-e05eoptWfAE5hFAC-zXo4SiHvHq27HGOPZujHefvN1WMRPiVzi7XCs3wUDJVgoMLKI7pl8EWpOyzrM6gKLvQ51UspWJoUbtNqqbqe4uHPvp1FT48W4flxmB6-Bc90tHQk8_GUv6JiGc3m2WIP7VqYSTkHY22Io8BlPxFlITZNQkWALrv0RcAkZYt0dcE_tOFr8vHjjDFBb6r-QRDBoGkXakAuTFOMU9nOuKVitz4e-HfcUhLlFXLMAa5sJ89JhEtgBZOMp_rhdjwsim665YPp5AjkkvVmptHEyzAnTiu6lScLgNJLX99W2zAxSQXMNzGYVVh2TO0d6y5LUC3X2XM_GDIvEv11flfpJ-RyR-B_2JI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86a8bc2e2.mp4?token=UMm7rXgh0HhC86IEgBM4NHOH0HP3syDblmF63z7QntbndqAVTEzT1afCXfFboazCZxyswfRf8yFr0YzIDlsmmJFT4Gc1iInAl4Be4Ki1Rtsk8WEe6l6dhS7dAuv-6iGyEPeyaUi_HwuEHjrLqpUQNAWoyXILOndnYyL7wReTIsiAeO4H8VqPLHkWdIAzSfCCdljxRaMggu0n0sg6VTS8wTKlYv5fek3QGBQ-l_NULhYFIGQxxcyqm48e3_B17ay3A7AIM1nt81EI67pX_1jSHdY2Oh8SD7KKjh21SoM6uesGDkTe8a89wnURhaL2UW-e05eoptWfAE5hFAC-zXo4SiHvHq27HGOPZujHefvN1WMRPiVzi7XCs3wUDJVgoMLKI7pl8EWpOyzrM6gKLvQ51UspWJoUbtNqqbqe4uHPvp1FT48W4flxmB6-Bc90tHQk8_GUv6JiGc3m2WIP7VqYSTkHY22Io8BlPxFlITZNQkWALrv0RcAkZYt0dcE_tOFr8vHjjDFBb6r-QRDBoGkXakAuTFOMU9nOuKVitz4e-HfcUhLlFXLMAa5sJ89JhEtgBZOMp_rhdjwsim665YPp5AjkkvVmptHEyzAnTiu6lScLgNJLX99W2zAxSQXMNzGYVVh2TO0d6y5LUC3X2XM_GDIvEv11flfpJ-RyR-B_2JI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احساسی‌ترین صحنه جام جهانی بعد از بازی آمریکا و
بوسنی
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/akhbarefori/665877" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665876">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0edb585c.mp4?token=pw8bf0E5yEWR9QpmxKCvV8x1TZki_4FaP3Plic3961GS-rgm8C8Z4aYqpT2Lto-TVcS4qa70NOOzRYQyc_QrjXSxP5uT3tqpCXHX6aWCco2fgZguwBTGB-J8rE3Q8HoWPumW_TQ1xaGaLEdNkI6QSQqkCkldpITxPNC5WULzTj-TXAoywdwDs_ClXsMiEBNQGOa4kRPzqE8tMT84evwEHwNfFsxdihMJ7cbyUbc7GPdEbkvHhcp5_YcIdAqsp1ga4AA6MdmKSMX2Lv6VarQEL6j0NbvSKThkpv5-AKSdREGAEqxQgLrCB39kvKzzFGm9YLVFbYzHy3nqcn4_piel6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0edb585c.mp4?token=pw8bf0E5yEWR9QpmxKCvV8x1TZki_4FaP3Plic3961GS-rgm8C8Z4aYqpT2Lto-TVcS4qa70NOOzRYQyc_QrjXSxP5uT3tqpCXHX6aWCco2fgZguwBTGB-J8rE3Q8HoWPumW_TQ1xaGaLEdNkI6QSQqkCkldpITxPNC5WULzTj-TXAoywdwDs_ClXsMiEBNQGOa4kRPzqE8tMT84evwEHwNfFsxdihMJ7cbyUbc7GPdEbkvHhcp5_YcIdAqsp1ga4AA6MdmKSMX2Lv6VarQEL6j0NbvSKThkpv5-AKSdREGAEqxQgLrCB39kvKzzFGm9YLVFbYzHy3nqcn4_piel6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده‌کل ارتش: با اراده‌ای محکم‌تر به دشمنان ملت ایران اعلام می‌کنیم تقاص خون امام شهید و شهدا را خواهیم گرفت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/665876" target="_blank">📅 12:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665875">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJMACxyzaBFE7MZr98BHJHNH7baHiW-5lNqPl9hjo8dnv_KGL9OUhFfj6UY1ndNLgWaKzXLMeWDfERxw3Xisu1XQQj1bjiH4H5KlTCCfFHoOxT6wTL0j6uyt0RLELsE-vFnYO8e5LzClekYU8N5oApERzZ035A2VkE6V3yvXQi3vNFiohvgvXtcK-hhzg9J2m6rw84EPuouAcJrKxbqBK1zaaEnsYfYK9kGo0ftAWXfm4QcaQP3wYDFuO2mVpuASTt7CDqFRA-w6Jn2s0DgB7vq1QAZKw5EgcKC_4V5mo3wMzg2JjJI8Yu5u2walsFTIf46UjbtC0czADcu1_KPrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار رادان هیچ صفحهٔ رسمی در توئیتر ندارد و هرگونه اکانت منتسب به ایشان و همچنین ادعای بمب‌‌گذاری، کاملاً بی‌اساس و کذب محض است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/665875" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665873">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206ec001f2.mp4?token=u_HawngVF0F5RKq7X8uwc83UMIomHHgUSkljfgiU5UCBwJ7HClFLOebnWzbGnDPAlSsQ3AVii4ZSP3q294TFDykTjUiPbFUBIcrSUZQHN7k8u-LrGd_qRmUspq6vFynlCBcJR07zhUcQWds0rJCiNYhR47tCFz3oucOvac3036RwJ4msNbLoCS7ZNVnwAdXpXZFerH0Csm4TvcrPtArr78c7UaUGkaOen1fBZZp-OYSqR8EJuSYBxgiMwCFjTNlj_QLPQECpmXuDQ4MzRFFyme-qpOP5lKrukWXm107DxBGybgLv6O8lqj2mBYqzaAJJEIxR1zLHO3ZH4WkTZ2nHHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206ec001f2.mp4?token=u_HawngVF0F5RKq7X8uwc83UMIomHHgUSkljfgiU5UCBwJ7HClFLOebnWzbGnDPAlSsQ3AVii4ZSP3q294TFDykTjUiPbFUBIcrSUZQHN7k8u-LrGd_qRmUspq6vFynlCBcJR07zhUcQWds0rJCiNYhR47tCFz3oucOvac3036RwJ4msNbLoCS7ZNVnwAdXpXZFerH0Csm4TvcrPtArr78c7UaUGkaOen1fBZZp-OYSqR8EJuSYBxgiMwCFjTNlj_QLPQECpmXuDQ4MzRFFyme-qpOP5lKrukWXm107DxBGybgLv6O8lqj2mBYqzaAJJEIxR1zLHO3ZH4WkTZ2nHHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک توریست آمریکایی که به تایلند رفته بوده، پشتِ صحنۀ عکس یادگاری با ببرها را به اشتراک گذاشته است
🐅
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/665873" target="_blank">📅 12:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665872">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd9198640.mp4?token=tSc-LPypei3Vz93rrEKeKbExUfEI-E4Wl7MUK3iO_7pKMFM0FR2F4V4JweoEFA1TULrggQp61gUppjd8fL-9ZI_ocyicqrPNgSFcfRHLSB7OcWD4In2K9HXY2dHv9BaAbJYqYZRa02ZN8kBQVj7NpapUzlLz4Vv_CODx7w8GJapFUi2ncV7BcvJEYoL8KVu0KEHDiHcBfg2h9wOk6t3k91MuDRh_oY9hj3Ygw47xToe9mPEaNQ_x-B6UKzquinfOp4i-j3yDtJZpytFQUCYPENT-V9LKSV4UNTREyP7XKr0kBR8tiBpB-lFa7f4BtTDn_IN_2xCvksKyLCwv6HbysA8wDnzkCfIi_tUi5LKozuepHMaELTwhQ3Kp4JS3WDmfiZ_op4i5ZkB6cVzksRtIpUeCMqtZtAW8VnQ280EMRazD_4tyV2kul79JeoNqXcti-rBA0qLHUVEKUX4B1tXl0Cs4lBjGWMNqCWKN6xoXBDArBc-X-IxzjFNTw79rClcT6gPA0nsTbvgDN0SD1iUAVL3ALLq5cDELuLlvqGWwoQwa83wPIYRrRKgRoa_2wyfk_cSP0Yu9s4soSe-YmYSekfVYr2JW0OqdXKZaMFHfeNZdQ9X1wuPL8twmmRKKWQCG5mbmJTsi4yvuruiieJRVViJSYVUOSldMAehpqDH5q1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd9198640.mp4?token=tSc-LPypei3Vz93rrEKeKbExUfEI-E4Wl7MUK3iO_7pKMFM0FR2F4V4JweoEFA1TULrggQp61gUppjd8fL-9ZI_ocyicqrPNgSFcfRHLSB7OcWD4In2K9HXY2dHv9BaAbJYqYZRa02ZN8kBQVj7NpapUzlLz4Vv_CODx7w8GJapFUi2ncV7BcvJEYoL8KVu0KEHDiHcBfg2h9wOk6t3k91MuDRh_oY9hj3Ygw47xToe9mPEaNQ_x-B6UKzquinfOp4i-j3yDtJZpytFQUCYPENT-V9LKSV4UNTREyP7XKr0kBR8tiBpB-lFa7f4BtTDn_IN_2xCvksKyLCwv6HbysA8wDnzkCfIi_tUi5LKozuepHMaELTwhQ3Kp4JS3WDmfiZ_op4i5ZkB6cVzksRtIpUeCMqtZtAW8VnQ280EMRazD_4tyV2kul79JeoNqXcti-rBA0qLHUVEKUX4B1tXl0Cs4lBjGWMNqCWKN6xoXBDArBc-X-IxzjFNTw79rClcT6gPA0nsTbvgDN0SD1iUAVL3ALLq5cDELuLlvqGWwoQwa83wPIYRrRKgRoa_2wyfk_cSP0Yu9s4soSe-YmYSekfVYr2JW0OqdXKZaMFHfeNZdQ9X1wuPL8twmmRKKWQCG5mbmJTsi4yvuruiieJRVViJSYVUOSldMAehpqDH5q1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشه‌‌هایی از سفر رهبر شهید انقلاب به کرمان با لباس مبدل پس از زلزله دی ماه ۱۳۸۲ شهر بم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/665872" target="_blank">📅 12:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665871">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZZ8d1urVysIeg1KyLvEp0jDEp56mcYyTy_sAVAS2mw6205eBl4hp5qOHw5r7rFcOxDKyV85_h7_Kn-Mmhnu59biEtPQknJHY3FEJ60HEEb_LO4_MUPiwKaPzESynPynMLDA6nBNmcEf0eXyJa6kA31ekJBX7Ypq1dJSTHadH4RJ3bPYYQaeoQb7D4sR0nXRzuWILtjcQPuoVJYriTPwJ5OBeZuXOweWseXML6CoYTOEQwIPIvwPf8vFPAZI_JJei9SfF0r3r9diHhRmGNP8-hoxJUIWCmS2uAYKiplHQ5GiPbtzsrcbpqCCbcr6abV610Sc1JGeysfh2QNhF6ILug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از جاماندگان
🔹
اگر در مراسم تشییع رهبر شهید حضور خواهید داشت و مایل هستید به نیابت از افرادی که امکان حضور ندارند شرکت کنید، آمادگی خود را به خبرفوری اعلام کنید.
🔹
در صورت هماهنگی، اطلاعات لازم برای ادامه فرایند در اختیار شما قرار خواهد گرفت.
🔸
برای اعلام آمادگی و حضور به نیابت از کسانی که امکان حضور ندارند پیام دهید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/665871" target="_blank">📅 12:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665870">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=UoiooKzpYiLUFH-FX6POb8v2GC9cuSUhTg-6GPr91xaP7HDMWKpqRF4qcIRFy9MGSsSjctPhsCEY1jxZcz5D_1q3v7eReKIbK64pXFndmRIj_YgtxhTHHY6FCvgAOZ_YdqNd1hUlbwpclE0gHuZu4WxRWvJJeRf3c4ISj9pZUqOXPhEp1q0PnAlC3TNVvLia8_8ENmWTfM78rZgk1FT1VZvS6bYxGt1xbZfw-0-lyKSmiw3C0jD-s8uNa5DeclzFUcZe63yI4K4BCFBC82-zAxqq0FKDU9hPYkU8zH_rNDvHSw-7J5kRnMygLu7ordeNWat29lf_M_7DiFtHQTYnzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=UoiooKzpYiLUFH-FX6POb8v2GC9cuSUhTg-6GPr91xaP7HDMWKpqRF4qcIRFy9MGSsSjctPhsCEY1jxZcz5D_1q3v7eReKIbK64pXFndmRIj_YgtxhTHHY6FCvgAOZ_YdqNd1hUlbwpclE0gHuZu4WxRWvJJeRf3c4ISj9pZUqOXPhEp1q0PnAlC3TNVvLia8_8ENmWTfM78rZgk1FT1VZvS6bYxGt1xbZfw-0-lyKSmiw3C0jD-s8uNa5DeclzFUcZe63yI4K4BCFBC82-zAxqq0FKDU9hPYkU8zH_rNDvHSw-7J5kRnMygLu7ordeNWat29lf_M_7DiFtHQTYnzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع فرماندهان ارشد نیروهای مسلح با فرمانده شهید کل قوا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665870" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665869">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نیکزاد، نایب رییس مجلس: هیچ تردیدی در خون‌خواهی رهبر شهید و شهدای جنگ تحمیلی وجود ندارد
علی نیکزاد، نایب رییس مجلس در
#گفتگو
با خبرفوری:
🔹
اول باید تاکید کنم درباره خونخواهی رهبر شهید و تمام شهدای جنگ‌های تحمیلی اخیر بر کشور، هیچ تردیدی در میان مردم و مسئولان وجود ندارد.
🔹
آقای شهید ما، تمام مجاهدت و تلاش خود را در طول عمر با برکت و زندگی سیاسی و دینیشان بر حفظ استقلال و عزت ایران اسلامی گذاشتند، لذا ما بر حفظ استقلال، عزت، اقتدار و تمامیت ارضی خود تاکید داریم.
🔹
اینکه دشمن به اهداف خود نرسد و هژمونی ساختگی‌اش برهم بریزد، برای ما از مصادیق حرکت در مسیر راهبردهای جدی رهبر شهید و رهبر حکیم فعلیمان است.
🔹
باید تاکید کنیم که خونخواهی زمان، موقعیت و وضعیتی است که مسئولان کشور و در رأس آن رهبر فرزانه انقلاب اسلامی، به خوبی در آن اقدام کرده و همگان حصول نتیجه را مشاهده خواهیم کرد.
🔹
قطعا در این راستا دشمن‌شناسی همه‌جانبه، حفظ وحدت و انسجام ملی، پرهیز قطعی و جدی از دو قطبی‌سازی که رهبر شهید انقلاب بر آن تاکید داشتند، از الزامات است و در این راستا تقویت بیش از پیش نیروهای نظامی نیز از واجبات است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665869" target="_blank">📅 12:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665868">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdA9lzoF_0HqjqCyCsSDvk3Ps7q5Hh4cgrawg8nLbewZQssTj3jgIPeO4kjumGnjmyrKyNMYupGR096SPE5r2Eg2Z1X1bjx2c7LT_03v5IxGkIIElrFgWHQDhpi8VAZTUXsU8WxYRL7K7ilcDNwsjLuW0JMJkRZA3jsqfpaiqECl3KJhfpHLpPXOWlokaR0Jsjc4Z4aQ22UG0SZKlVbxiQL2vz6HLVZ0FKeRQBfkZwGuYYcP8SL4VN6mAQb-5WvPZzb__9d-5AsO-irGM4bJOUf30U1oWCfusIPHRIQgL6RvUORcf03TLFqZdO_7VcI7CaUxB22cxDuJATczUprSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت دیوار سکوت بانک سپه چه گذشت؟
🔹
یک سال، سه ضربه: نشت احتمالی ۱۲ ترابایت داده‌ی مشتریان در فروردین ۱۴۰۴، فلج‌ شدن خدمات بانکی در روزهای جنگ ۱۲‌ روزه، و بحرانی سوم که هم‌زمان با جنگ ۴۰‌ روزه شکل گرفت. در هر سه مورد، واکنش رسمی تغییر نکرد: انکار در ابتدا، سکوت طولانی در ادامه، اطلاعاتی ناقص در پایان.
🔹
حقیقت اما جایی رو شد که کسی منتظرش نبود. در گفت‌وگویی آنلاین درباره‌ «بانکداری در شرایط جنگ»، مدیرعامل توسن، بی‌آنکه چنین قصدی داشته باشد، از نفوذی به شبکه‌ی بانک سپه پرده برداشت؛ نفوذی که درست از دل امن‌ترین لایه‌ی این شبکه سر برآورده بود.
🔹
این اعتراف، بی‌آنکه نام «هک» را بر زبان بیاورد، همان روایتی را تأیید کرد که کاربران شبکه‌های اجتماعی هفته‌ها پیش‌تر درباره‌ی هک بانک سپه در جنگ ۴۰‌روزه مطرح کرده بودند.
🔗
گزارش کامل را اینجا بخوانید:
khabarfoori.com/fa/tiny/news-3227401
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665868" target="_blank">📅 12:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665867">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaqUC7eWIyqudwMm0AtyG7BT3GYQzWaXfKqFhcXk6AbZXgWDcFq0KeRw40nsDe0ZvWa0kKtbGiMaMNa0taXzgyw5n5XMHlIOAsWNWrHw-pzv1uUJxFf-S9d7umhP2MiCccFsJD9X8wldxRMV7Pv6QHzmUi2dXFcaWgNxZW0mnyghe-QPUPlxqdQuH0iTvCuezJ6AKXa49K0L8cFHw_-mr0BOy7SGrQngCu4IIkjZfznfiTYe6caZr8_ijn-ENVy_ytlcsb1CqCOeN9OHtLUq6YoYPX0DRrJ_pcvE9vMkOCzbk9wUdeUmK6xtIHc_lsnYJakEUKtxasCnjryP7ujweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها بیشترین آسیب را از خروج سرمایه انسانی دارند؟
🔹
شاخص خروج سرمایه انسانی، میزان آسیب‌پذیری کشورها از خروج نیروی متخصص را در مقیاس ۰ تا ۱۰ نشان می‌دهد.
🔹
این شاخص صرفاً تعداد مهاجران را نمی‌سنجد بلکه، عواملی مثل مهاجرت نخبگان، بی‌ثباتی اقتصادی و  اثر خروج نیروهای متخصص بر کشور را هم در نظر می‌گیرد.
🔹
در این رتبه‌بندی، ساموآ با ۱۰ در صدر است و ایران نیز با حدود ۴.۶، در رتبه ۱۰۴ بین ۱۷۶ کشور قرار دارد.
@amarfact</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665867" target="_blank">📅 12:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic6Il-fJwq0ntlbaczuDbchWJYkcVECkWti0khchVaztQUGkn6UyiiJJDbaoGyr-j0kh4LEfkFOyoOk9-UzfA3Xqpx2h5dx1ndUFugtypocL1U683UwZWhZgG1ZiT5Pv13ir1aUy722aRgVyc3EaByeIqTca4w9hwzA9DFthEOz9oUhmd7hpJ0TM7XV3inXpYyrs1LYcQvkqZsR462Wz1lzRQlqiyHKGzvs54_E9PH6-YPI2nQSlsixfilzuYDW3ADMJW5b-yGZcxyhF96LTFzgHWKEg8NpxNh4veSAohX42txXtG0z0QKDJWvvdadO85OwenLdCa-7JNFdRdRzL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای روسی: به شما اطمینان می‌دهیم که مراسم تشییع هیچ رهبر غربی هرگز تا این اندازه پرجمعیت نخواهد بود؛ زیرا آن‌ها انسان نیستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/665866" target="_blank">📅 12:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665865">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
گروسی: درخواست دسترسی به تأسیسات هسته‌ای ایران را ارائه داده‌ایم
گروسی:
🔹
برای دسترسی به تأسیسات درخواستی ارائه شده است اما آژانس تاکنون نتوانسته است به آنها دسترسی پیدا کند. آژانس معتقد است که ذخایر اورانیوم غنی‌شده ایران همچنان در تأسیسات هسته‌ای این کشور قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/665865" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665863">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f05d6012.mp4?token=uL5Wf8AJgo-rZBJqnZZwfbnsD1JzkQ96fz7WHQDC3JcA4DX1h6bw54AMPa45Rjh-NOWGvlu36vKZjsgdw2vx2dMFtr3AhnaLeBN5RSkoTLgaX6CTYmVYRx8ZlbY_TWJ0LHGjHzbTRQX92x-AUkkLSJfNRjMUQeHD04Sg0aOC_JjX60dPOquIwS7LiaZUGLM3wzBPCiD4K-yqBG7E9Gz5jOpeP-raqUMhqTyvQRvsz3H1ybP4DJcsN-t_V9GCZm9K6DeOuEDgStqYkZySUXOC5RKZivNi0sgaqoHxV9TMqIv9bgiFbyUV85g3s0fLCknro1RrYbavdWIRrq1tnIP1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f05d6012.mp4?token=uL5Wf8AJgo-rZBJqnZZwfbnsD1JzkQ96fz7WHQDC3JcA4DX1h6bw54AMPa45Rjh-NOWGvlu36vKZjsgdw2vx2dMFtr3AhnaLeBN5RSkoTLgaX6CTYmVYRx8ZlbY_TWJ0LHGjHzbTRQX92x-AUkkLSJfNRjMUQeHD04Sg0aOC_JjX60dPOquIwS7LiaZUGLM3wzBPCiD4K-yqBG7E9Gz5jOpeP-raqUMhqTyvQRvsz3H1ybP4DJcsN-t_V9GCZm9K6DeOuEDgStqYkZySUXOC5RKZivNi0sgaqoHxV9TMqIv9bgiFbyUV85g3s0fLCknro1RrYbavdWIRrq1tnIP1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینستاگرام ویژگی زیرنویس دو زبانه و قالب‌های پیشرفته را به اپ Edits اضافه کرد
🔹
این قابلیت درحال‌حاضر از ۱۵ زبان مختلف دنیا از جمله انگلیسی، اندونزیایی، روسی، پرتغالی، اسپانیایی و هندی پشتیبانی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/665863" target="_blank">📅 12:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665862">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قالیباف: اجرای کامل تفاهمات به‌دست‌آمده را با قدرت مطالبه می‌کنیم
رئیس مجلس:
🔹
اگر آمریکا و رژیم صهیونیستی به تعهدات خود عمل نکنند، جمهوری اسلامی ایران اقدامات متناسب خود را از سر خواهد گرفت.
🔹
آمریکایی‌ها در این جنگ به‌طور کامل دریافتند که امکان مقابله نظامی با ایران را ندارند و ادعاهای رژیم صهیونیستی، چیزی جز تبلیغات بی‌اساس نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/665862" target="_blank">📅 12:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665861">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اطلاعیه شماره دو آستان قدس رضوی ویژهٔ مراسم بدرقه، تشییع و تدفین رهبر شهید انقلاب اسلامی
🔹
جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم مطهر به‌صورت مستمر و بدون وقفه تداوم می‌یابد و محدودیت‌های تشرف و تردد، صرفاً در صحن‌ها و رواق‌های مرکزی حرم مطهر رضوی، از ظهر چهارشنبه ۱۷ تیرماه ۱۴۰۵ به‌صورت تدریجی اعمال می‌شود و تا پایان مراسم تدفین ادامه خواهد داشت.
🔹
از زائران حضرت شمس‌الشّموس (علیه‌السلام) خواهشمندیم این مهم را در برنامه‌ریزی سفر به مشهد مقدس مد نظر قرار دهند و با خادمان خود در اجرای هرچه شایسته‌تر این مراسم همکاری نمایند. یقین داریم همراهی و صبر شما، همچون همیشه، پشتوانه برگزاری آیینی در شأن حرم مطهر رضوی و رهبر شهید انقلاب اسلامی خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/665861" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665860">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شهباز شریف برای شرکت در مراسم تشییع رهبر شهید انقلاب راهی تهران شد
🔹
روزنامه یدیعوت آحارونوت: بازداشت جوان ۲۱ ساله در اسرائیل به اتهام جاسوسی برای ایران
🔹
مشاور امنیت ملی اسبق آمریکا: آمریکا در حال به شکست کشاندن خود مقابل ایران است
🔹
بارزانی و عراقچی تقویت روابط ایران و اقلیم کُردستان عراق را بررسی کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/665860" target="_blank">📅 11:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665859">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC515MTWN0xU19XRXrwDyNPlUbWS9_ZsiPqSTFFN15W9OdqGVdZzFmBB1wrCYpaSJKCBimv3mLOer4W1f6pEzqtGEB-tvi5vZaWkKLxjJdsMdoDNz8t6-w4-kbTgoPPzcIxNVbgL8L-raqhgwAmJ3kBFdZSIU6O-zfA6_IsRuYr1vc2lExWGD7Sh7lAXj_Wt5hBUhed7xp74pnuFd4_NpxtpATHq3z2AbGKk17hMSKnMDkn6OAyXOtwewMxvfzeKDR8m6Yp-gdNnUahsmcjWhq1WCkZtwlJYeYNmuRcu4XCIg1QyPWDrX6obLoorkR7pM1nSFSoUJC0ubke_Xx51HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زبان مخفی جراحان؛ علائم دستی که سرعت عمل را بالا می‌برد
👨‍⚕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/665859" target="_blank">📅 11:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665858">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
خونخواهی؛ مسیری برای عدالت روشن
🔹
در نگاه بسیاری از ایرانیان، اقدام آمریکا در ترور رهبر و فرماندهان ایرانی، نمونه‌ای آشکار از یک جنایت بزرگ و ناعادلانه است
🔹
اقدامی که مطالبه عدالت درباره آن نباید به فراموشی سپرده شود. خون قربانیان چنین حوادثی، صرفاً یک پرونده سیاسی نیست، بلکه مطالبه‌ای برای اجرای عدالت و مقابله با مصونیت از مجازات است.
🔹
خون‌خواهی، در این معنا، نه دعوت به انتقام‌جویی کور، بلکه اصرار بر مسئولیت‌پذیری، پیگیری حقوقی، حفظ حافظه تاریخی و مطالبه پاسخگویی از کسانی است که در برابر افکار عمومی و قوانین بین‌المللی باید پاسخگو باشند.
🔹
ملت‌ها زمانی به عدالت نزدیک‌تر می‌شوند که جنایت، فارغ از جایگاه و قدرت عامل آن، بی‌پاسخ نماند. مطالبه عدالت، اگر استمرار یابد، اجازه نخواهد داد تاریخ با سکوت نوشته شود.
🔹
بنابراین آنچه که مردم این روزها از مرجعیت داخل کشور انتظار دارند احقاق حقی است که در تمام جهان به عنوان یک مبنا شناخته میشود ...
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/665858" target="_blank">📅 11:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665857">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcRbIox9jEsGLrNcGRs0A5tVpIdZJ7ZBvx-Em7743R9oPbkxVTU5YxRaPAwjcclslFRBzlAfv91JL6zYL508-Ozl4QLSraRrABoFe-oVMcsOfso7PCFVBltV5e9R-uoU5K8SF17rIR55EnzzjnU3yniVdCXL1WsN1dXg7bRKuaEiiMr1UhCwjIyuiDEepkLogFV5Sh0z3rJGefH7HlvllDWBqeHS_0-VwlZ7yU8MPDO6HDoaIIcQEhbk3xW0wPUi430aJRljzEGKSJ4FBd7sGQcwQ72lP5qpqKiLMhAMw_VgmDllnoBD62HBPIHS-af0AbqV78WA9UIP5H4NARpd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: یاد شهدای هواپیمای مسافربری ایرانی را گرامی می‌داریم و جنایت نابخشودنی هیأت حاکمه وقت آمریکا را هیچ‌گاه فراموش نمی‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/665857" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665856">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
آسمان تهران دوشنبه به طور کامل بسته خواهد شد
رئیس سازمان هواپیمایی کشوری:
🔹
روز دوشنبه، همزمان با تشییع پیکر رهبر شهید انقلاب، فضای تهران به طور کامل بسته خواهد شد و هیچ پروازی انجام نمی شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/665856" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665855">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ef817bd9.mp4?token=TtRKO2cnfcR9aB8TfMiRbamkatBaRMvl8XAvweFu5VR62e0uxWGjYuP7_FAGwwpVxfAUMr36x-ERTO5upnmZhq5z-N34MMoeq8kk8Cb8bj68C9ZNRDqK3ZX76GdoXQQPErtXHgTGohYg5TxXfkROVgs9Cw0p9gU6KKIPNvcVqVgDDXx2B-a9VSafTaOAwIJj3X2EhIbZFaQfu5Sjd8EWla1utlH_36Usna4m2q5Jf1rkNekLIMzC46yx8ix-NGha84n7iRLQWZD5CugfNhf6xoLXJlzU8lz4ZX0j9LYp_e4rRbAu4K5c1GGqsPWtdnACC_K1L9AVvehI-2kQjmAXThBIH5-eeOZhymJnZLs_EpivsNuJajUziZt4Wiuua19Mut28cb9QT4gGdfwW2wbq9-k8ZUl5aGzd2B0BkSesEsvfYl3TgVlD3diwqvR_D8qjTAQdcroLzVTN3HM-YLy8SFgHzXdhu-VmnOXzmIJUQl5jmB86TqHcIq1ICKyh4kKuV5T2TvXNhrqAWpxcb6Zmq_75RKoXRqCUibuBQABsjK8_xCigOWt868Bu3oKKRFmMvwreva2o-5Pa_zqii1jxexc8MyTqyr9wT52SA-xtmQtJ8osfj2j25YSNNbU8giO5uj_l4gmZylbx-cAF7OnCt9cio4OqpphNGIOXT6Le_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ef817bd9.mp4?token=TtRKO2cnfcR9aB8TfMiRbamkatBaRMvl8XAvweFu5VR62e0uxWGjYuP7_FAGwwpVxfAUMr36x-ERTO5upnmZhq5z-N34MMoeq8kk8Cb8bj68C9ZNRDqK3ZX76GdoXQQPErtXHgTGohYg5TxXfkROVgs9Cw0p9gU6KKIPNvcVqVgDDXx2B-a9VSafTaOAwIJj3X2EhIbZFaQfu5Sjd8EWla1utlH_36Usna4m2q5Jf1rkNekLIMzC46yx8ix-NGha84n7iRLQWZD5CugfNhf6xoLXJlzU8lz4ZX0j9LYp_e4rRbAu4K5c1GGqsPWtdnACC_K1L9AVvehI-2kQjmAXThBIH5-eeOZhymJnZLs_EpivsNuJajUziZt4Wiuua19Mut28cb9QT4gGdfwW2wbq9-k8ZUl5aGzd2B0BkSesEsvfYl3TgVlD3diwqvR_D8qjTAQdcroLzVTN3HM-YLy8SFgHzXdhu-VmnOXzmIJUQl5jmB86TqHcIq1ICKyh4kKuV5T2TvXNhrqAWpxcb6Zmq_75RKoXRqCUibuBQABsjK8_xCigOWt868Bu3oKKRFmMvwreva2o-5Pa_zqii1jxexc8MyTqyr9wT52SA-xtmQtJ8osfj2j25YSNNbU8giO5uj_l4gmZylbx-cAF7OnCt9cio4OqpphNGIOXT6Le_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسم‌الله گفتن رونالدو قبل از زدن پنالتی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/665855" target="_blank">📅 11:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665854">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecfa437d02.mp4?token=pP-pqIkwjJokgCBRVDU-CijxkZqAPkOxCPT5JvLmEVxYB9y6qeowfECrT5nQpNP_bmOjsXH7dUKycvm-SwtzSgHN189xQCN1NmGxKiezkYHlbWK9V9bAVu_fyPoZQKTWxYo676sHeBDapZbACgS_YFvsjta52xniJqcwbbsFaxPIU4oCSVWKHTesBpyEaXWBisAfNppnlc_XzSa6Steg1GOSABP-4RAkVfBSATT0X5gl1S4mNqo-g_RLG4CJVpQovvYmbZ7usRsjVLTYhJ7cJb3KEokugLFF9KAaUIhR_wG36VtfaTCNwMC8-dj8f74MzCu3lKUzjwKr7E2NKHEFBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecfa437d02.mp4?token=pP-pqIkwjJokgCBRVDU-CijxkZqAPkOxCPT5JvLmEVxYB9y6qeowfECrT5nQpNP_bmOjsXH7dUKycvm-SwtzSgHN189xQCN1NmGxKiezkYHlbWK9V9bAVu_fyPoZQKTWxYo676sHeBDapZbACgS_YFvsjta52xniJqcwbbsFaxPIU4oCSVWKHTesBpyEaXWBisAfNppnlc_XzSa6Steg1GOSABP-4RAkVfBSATT0X5gl1S4mNqo-g_RLG4CJVpQovvYmbZ7usRsjVLTYhJ7cJb3KEokugLFF9KAaUIhR_wG36VtfaTCNwMC8-dj8f74MzCu3lKUzjwKr7E2NKHEFBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از علمای فلسطین به پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/665854" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665853">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0saZ7tSxDIKZdAnfXrM3evZOtgihdP4hMAsrID5eN_01VZpGT8LuykvTDD-pEhPngxCja860ix9Pb06Wxl4Ft_yny_Nfn6opnNa3twcye8tjQM5t3QI3cdre52WZwA7y7DQZ7tsbOJwc3l_qRKStfcFV7TNH_j3VoAVpBM39vm8kO6SHKZAx_906UFnTGG1ufSOt2DyYSTzAsInLoaFJ0r6mLTjI0fFEFb59wgg85nQN5hIzYaQxEnYLNj89-Ku0GY-sOX3DXZaosMzIxobDLIMTUUeKqyGrVnA3Tie4V-vaqzRoKY_RX_JyUGY5iXe89zkE1Iyt8xaUKXk6RkmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل افراد کم‌بینا در مراسم تشییع و وداع
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/665853" target="_blank">📅 11:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665852">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حزب‌الله برای رهبر شهید، مراسم یادبود برگزار می‌کند
🔹
جنبش حزب‌الله از مردم لبنان خواست در مراسم یادبودی که به خاطر رهبر شهید انقلاب برگزار خواهد شد، شرکت کنند. این مراسم قرار است شامگاه چهارشنبه آینده در ضاحیه بیروت برگزار شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/665852" target="_blank">📅 11:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665849">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hs8I1K_Rv47payWbK5n6ktxIsoaO3DoaI7_zKRVaIDjDJayDkFWb7fUG3qoi0ZGSrg1S-TkJ97DD9b6b1urdxFZn935eaP1XVCh8UUtP8nRLeaa6zw3iEG5P2zxR9Ez6Fnzd0lE141D5gE3RabQh-5SuFObp4mG3yq9MGU9aIeLM4mrp7cLKjRsJDbq25StXvdTG51YHSxfw1HYVedkxUCXLy27seSEi-ivrUcydCv4o61NYUyt2qcHwsxDcn9qD7hYjSssbKSgs0XKheYTCDlpXRnulqt8mTwtLrZoNDN_jQwBFsHnK1-MoFmtMFLdaZqneoLPBaOxSrca6bQIbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZ7WY_YN3lsSCAENUvh9yOPfKB-zOaACSAuYRBWi6yWn4AtLPTTxlMzr_Mxs1alkhX6ajaoI6ZaJdsaKQnlA-L175qM3NtN_VtWCddVTHnp5HeYZi-adeFd0kIFsOG3Jps7tbOnO_Uexqq6lnSX6jNovgEETgAU9HtwVdK79hxaB8mofxKmdwOOth3iDpIW0w8X-8rYvk2UV8QYpCmCjZPON17YoQmPVMfl-UMlZJrj2ph0LEJGKCg919lQ8ulCoa5I4j9fyXG_byFUW4sMiRaWzBOwi0RDE8FpKF1AfFQ5B1TfXxefPQuB1tOJmxx-9YwzXgKMi6GuMVHxovQxJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHMBGpzG3Oz8-lcgI9sNwKErKGN0nX-NzksHFq_3w4FIrWNPa97fknVMQEpro3_HJQe8FUTCEDVTK9WAK-vAm--p0h8vnhF5w6ma2RaarPjSVGHiQGvHdNSuwvzymZpBfeC-zF0hkkY_-KqR4mHujwoyWYEez5ybUyiLmAh4CNLwxb00z3j_dl2LzPPiZtX76hLNjb0p86kA9Z6Wca6JP2YLtnpuDtUyWVhTH8_YT66ULytex3inr8HqyiAIH2ni2k0RZt8p5qCN6QsbUFCRgYlC5vsvrhXvzgcq9aVSkCn9-pL2zShFbdRxV7d3iF3j31IGg2BvH2NePlKs1RC8lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار نخست‌وزیر ارمنستان و رهبر ملی ترکمنستان با پزشکیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/665849" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665848">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/063a3452e3.mp4?token=b7ABpdwnJ_HyDY5dWB8iz_CmN8LjaFGYN-1gOSb-f_YVXjnad36YxnqipSd9FK2kQpDSYlmnsFWGppeye7bGOH0OT6R8_iELCeQSs8cHAtRZw_eDDT0ZOxo7N5WclE_T4vNtDeMLA-_KbO7N9arFvGZpxoaupP6tuXwWt9eyE4givA47ud719CYK0-JGcgueGsZFXX6DZr2tp1q1hi5aXCpXX8pP-rEdNXRDf1OJOizLMKrqfxTKXX1lM-WOiwX3Lvkf-5XifKAGkC9e9L7796_IusWpaw3NbjRC8h0IrxeCVdVkhlQDdqHbe2nyZ4_WFvx42YVGyfoQHzLO5OXQ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/063a3452e3.mp4?token=b7ABpdwnJ_HyDY5dWB8iz_CmN8LjaFGYN-1gOSb-f_YVXjnad36YxnqipSd9FK2kQpDSYlmnsFWGppeye7bGOH0OT6R8_iELCeQSs8cHAtRZw_eDDT0ZOxo7N5WclE_T4vNtDeMLA-_KbO7N9arFvGZpxoaupP6tuXwWt9eyE4givA47ud719CYK0-JGcgueGsZFXX6DZr2tp1q1hi5aXCpXX8pP-rEdNXRDf1OJOizLMKrqfxTKXX1lM-WOiwX3Lvkf-5XifKAGkC9e9L7796_IusWpaw3NbjRC8h0IrxeCVdVkhlQDdqHbe2nyZ4_WFvx42YVGyfoQHzLO5OXQ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منطقه «البراری» دبی
🔹
﻿وقتی توسعه با برنامه‌ریزی همراه می‌شود تنها در ۲۰ سال، بیابانی خشک و سوزان به یکی از سرسبزترین و چشم‌نوازترین مناطق این شهر تبدیل شد؛ پروژه‌ای که امروز از آن به‌عنوان نمادی از توسعه شهری و احیای محیط‌زیست یاد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/665848" target="_blank">📅 11:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665847">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5621a5736a.mp4?token=noOBqewJr1n97Ng0nqJI4-IVT5p4RmdwOU2y5-uLXVuAM9yBa08_c_OTt_NEQ8QAm22-6bK0Ba-_CbQqdn32ukTltesrecBsUBspn17Sszl4K5CwaH9YgnZNpXA9r9fuYGHb2Z0bD8Y2st659xmUYGovyj0N8WlKe4ASJxXEawajGfwys6vQ0d4VvC_XXzWjBGx99E-jcSFs-e-fVnSCz1Uuma6sybBLswgcsyMfrUMx8_I_dO2EXgQLHSPv6vHhBBnhoyHh07anOwJO_Z1Uhz0NmfqnCSEBALOfeXyuEsTGUyLGJa9f-eN5Ol5t0cvuXVqo5IUEOJtyqag0BBrw1Cu1dVd3IYgBugw3s0ysmHqdxJBgIbdCyLB8w3eh7Odz4ECBvaY36Pu_-S383vZCi_DNf9mAE5j4fu9O5wXCRb-7VIA4RO4-eIuySBUx1-ntDO5x3HkA1u-jdNfKgI8OgJU4Z96Kb-ppUQmwb5Wl3xP6F1aT5EW7kQY4BWpcJb0G3ReMZPKJDGAFz8L64kX0BHBktTiBMWjohxddS0zzth7Ac-S6fIwQz5_vdDjsj3r9xznghOZLdgFvJf2gAIcgPiNSsJDxYU0exyKvmxicWKy7HQzyraEDh6i7ox6kzEB6Oj9qA0hbUhTmDqsMwdW0VHv9KId9_ezf4LJtVdJgVV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5621a5736a.mp4?token=noOBqewJr1n97Ng0nqJI4-IVT5p4RmdwOU2y5-uLXVuAM9yBa08_c_OTt_NEQ8QAm22-6bK0Ba-_CbQqdn32ukTltesrecBsUBspn17Sszl4K5CwaH9YgnZNpXA9r9fuYGHb2Z0bD8Y2st659xmUYGovyj0N8WlKe4ASJxXEawajGfwys6vQ0d4VvC_XXzWjBGx99E-jcSFs-e-fVnSCz1Uuma6sybBLswgcsyMfrUMx8_I_dO2EXgQLHSPv6vHhBBnhoyHh07anOwJO_Z1Uhz0NmfqnCSEBALOfeXyuEsTGUyLGJa9f-eN5Ol5t0cvuXVqo5IUEOJtyqag0BBrw1Cu1dVd3IYgBugw3s0ysmHqdxJBgIbdCyLB8w3eh7Odz4ECBvaY36Pu_-S383vZCi_DNf9mAE5j4fu9O5wXCRb-7VIA4RO4-eIuySBUx1-ntDO5x3HkA1u-jdNfKgI8OgJU4Z96Kb-ppUQmwb5Wl3xP6F1aT5EW7kQY4BWpcJb0G3ReMZPKJDGAFz8L64kX0BHBktTiBMWjohxddS0zzth7Ac-S6fIwQz5_vdDjsj3r9xznghOZLdgFvJf2gAIcgPiNSsJDxYU0exyKvmxicWKy7HQzyraEDh6i7ox6kzEB6Oj9qA0hbUhTmDqsMwdW0VHv9KId9_ezf4LJtVdJgVV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرتغال به کرواسی توسط گونچالو راموس
؛
پرتغال با کامبک صعود کرد تا امیدهای رونالدو زنده بماند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/665847" target="_blank">📅 11:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665846">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
مقامات سیاسی رسمی کشورهای مختلف به منظور ادای احترام به پیکر رهبر شهید انقلاب، ساعت ۱۳ در محل مصلی تهران حاضر می‌شوند
/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/665846" target="_blank">📅 11:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665845">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIiMVpzYGmkcr0CIM3c34AlhObl86DhxY4FLc6Y1daQmN3KOlbUzaWdeRJZc0MMXWtrYe1Dfin6HCDrRChk3ruspepaoOywgIEXYBsmkpTAE3KYihI1YauUq2tWRJLMovaXlcuQz7Ivs0FbRtWf7pEde7KgAhxTLImsQJq3zMfijvT730Vax4xA8PVs82iFYgHo34yAfT4J0lipCQW37h1lhUZV7f69aXfJRDtIeQi7Fwhu5K6z83E5QJ41kK5W2WGJzbB4jNFxBCyl5M0TKA1z23ql8VDVeG-fgxCnlZW1Gac_VkQFPiNgt3ZLP4Da3yJTQdPJqarEWfiCtVj6PMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط اتوبوس به دره در پاکستان ۴۰ کشته برجای گذاشت
سخنگوی دولت ایالت بلوچستان پاکستان:
🔹
امروز که درپی خروج اتوبوس از جاده و سقوط آن به دره ۴۰ نفر از سرنشینان آن کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665845" target="_blank">📅 11:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665844">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=aM76VlrmLrwjSzvQ9f5rGnqHL5f7lqcRIC5ltNzFU0IdBo3AsDhiJM1Sr4bLfe03k7NqepBBZ07vv73-NbvSTIRUSJUCgC5vbq9LxJS7nl7yDxlA-b3xnuN9rdRMQvPjaXd4DCK_-H3ZYJEkhgNEGMlDdxp0LUFe5boa7GcHrx4OlOWWJ2M5RGVmZtjqTE3hQ7D-PHO_rp5yY2Pj-hiToq-Uui0wEi9pQZj9P7y_T8AaBfy7ZKTbvKdY9sWBagrwPgp0InTkJSAONRSg4hiKOVSDa5zotE9iFA2LQ6YoUS-hOLIY6I9w6d9fRKHAHP_vZePUjxDS1fBSFVwDDQ7aTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa82a200d.mp4?token=aM76VlrmLrwjSzvQ9f5rGnqHL5f7lqcRIC5ltNzFU0IdBo3AsDhiJM1Sr4bLfe03k7NqepBBZ07vv73-NbvSTIRUSJUCgC5vbq9LxJS7nl7yDxlA-b3xnuN9rdRMQvPjaXd4DCK_-H3ZYJEkhgNEGMlDdxp0LUFe5boa7GcHrx4OlOWWJ2M5RGVmZtjqTE3hQ7D-PHO_rp5yY2Pj-hiToq-Uui0wEi9pQZj9P7y_T8AaBfy7ZKTbvKdY9sWBagrwPgp0InTkJSAONRSg4hiKOVSDa5zotE9iFA2LQ6YoUS-hOLIY6I9w6d9fRKHAHP_vZePUjxDS1fBSFVwDDQ7aTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از ارمنستان به رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/665844" target="_blank">📅 11:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665843">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01d988089.mp4?token=CuhSg7E0lHB1nUaEIbw6XGmG4CEDQ07FJz7nCk9eudgcijigy339uWV2BsooJWDwcsDd4Su9DGreD47uAsS0vDVH-hIwflfV_s5r1Xr1PQxocLmR3wg6zMmf143WnJguyFjUYXUHYGph_j_EbLlwbG_4vKuOzF7G2oSD4QKM4oa-TOGWIEpeE9TTeF6Wj3UnY_M15lHmzke880ZMyLEI6k_1cm0EM5oU-BPrtz14R_7rzWzh0D9c0brSNlKrOeHh5RSH9uFbb60cmjjVJh6E_qChrIuQ7BNBAUvTH-Iv-5hyIkWfHfWhB-BCMglGYrMLwrwwjxm8l7nXgjVBNK9m8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01d988089.mp4?token=CuhSg7E0lHB1nUaEIbw6XGmG4CEDQ07FJz7nCk9eudgcijigy339uWV2BsooJWDwcsDd4Su9DGreD47uAsS0vDVH-hIwflfV_s5r1Xr1PQxocLmR3wg6zMmf143WnJguyFjUYXUHYGph_j_EbLlwbG_4vKuOzF7G2oSD4QKM4oa-TOGWIEpeE9TTeF6Wj3UnY_M15lHmzke880ZMyLEI6k_1cm0EM5oU-BPrtz14R_7rzWzh0D9c0brSNlKrOeHh5RSH9uFbb60cmjjVJh6E_qChrIuQ7BNBAUvTH-Iv-5hyIkWfHfWhB-BCMglGYrMLwrwwjxm8l7nXgjVBNK9m8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از بانوان ‌طلاب و فعالان عرصهٔ بین‌الملل به پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/665843" target="_blank">📅 11:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d78a6625.mp4?token=OX6YeqcWSRVWykIk_fIWemAlOYYQC2fYspxJqVdNhYvH4G51zuab2x2WBEvaW-mQxOrg1neKvkzCQgYNm-5tAFk1fOtgFm_m5b53NWQDlVvEC8nLHD8U3vCGOCBTNBNkUCtcEfpTuefDoLebrzSCkNByZM3YyRr3Jh0litEAC-pC8xDvHV-P-qCZkqrLRN7GQALv8In4SUqyZYYujnVLmqeJ7iw-gYmLJh-uRQFYTa1NQWDax7MjH-uBEUJ-hXFoGbPQVA_g2IR0dcBfjVjN4oY8cO2QxermT14TPHcA_znqsApkPLQ9bH_QreVpymFb0oNFEwggjWPnyH1qgS0vAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d78a6625.mp4?token=OX6YeqcWSRVWykIk_fIWemAlOYYQC2fYspxJqVdNhYvH4G51zuab2x2WBEvaW-mQxOrg1neKvkzCQgYNm-5tAFk1fOtgFm_m5b53NWQDlVvEC8nLHD8U3vCGOCBTNBNkUCtcEfpTuefDoLebrzSCkNByZM3YyRr3Jh0litEAC-pC8xDvHV-P-qCZkqrLRN7GQALv8In4SUqyZYYujnVLmqeJ7iw-gYmLJh-uRQFYTa1NQWDax7MjH-uBEUJ-hXFoGbPQVA_g2IR0dcBfjVjN4oY8cO2QxermT14TPHcA_znqsApkPLQ9bH_QreVpymFb0oNFEwggjWPnyH1qgS0vAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیاتی از بیت معظم رهبر شهید انقلاب به پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665842" target="_blank">📅 11:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادای احترام هیئتی از شیوخ، عشایر، احزاب کرد اقلیم کردستان و اعضای پارلمان کشور عراق به پیکر رهبر شهید انقلاب اسلامی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665841" target="_blank">📅 10:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728761776c.mp4?token=mHh0htJ6O_8_WC9xPqM4HP126Y7uNiyixYgyq4CtlZFtXl-Gsr_hhA9bK13Iz77Z9BR0v9fzhm_NItAC_Gxbf5Ew1DKBEIgJCkU-7pxL1MqWQ9zWhmXCE5jWrTpJCeWMT79mkd4Lnp6hGVhHk074T8AIX3B8u_KWgvlCj-t-DBvbP3ePF4BghWC_YW0hC3Bn2hqWb15ytVQkpZqeSjKVUcdkzhrq1lJuhRjgxpgl_pcj0xcZmIobdVvC0jqy3qQ0qikcpT16Soxnx49Su_TAAsjHcFhri2Rv5wLrQjhOOtvkoGXIBk6FbdviLerf-qfiIZIIOu6z-BIMTBMI9nmYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728761776c.mp4?token=mHh0htJ6O_8_WC9xPqM4HP126Y7uNiyixYgyq4CtlZFtXl-Gsr_hhA9bK13Iz77Z9BR0v9fzhm_NItAC_Gxbf5Ew1DKBEIgJCkU-7pxL1MqWQ9zWhmXCE5jWrTpJCeWMT79mkd4Lnp6hGVhHk074T8AIX3B8u_KWgvlCj-t-DBvbP3ePF4BghWC_YW0hC3Bn2hqWb15ytVQkpZqeSjKVUcdkzhrq1lJuhRjgxpgl_pcj0xcZmIobdVvC0jqy3qQ0qikcpT16Soxnx49Su_TAAsjHcFhri2Rv5wLrQjhOOtvkoGXIBk6FbdviLerf-qfiIZIIOu6z-BIMTBMI9nmYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرتغال به کرواسی توسط رونالدو
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/665840" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665839">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF0qHGstQo9lV9u-LRARYa9-LUsN51d3VkbAMTofGqGwEvRFikemovU5i9hNG4JA2RjK3Be-fL7XVUBKQkfUBMw2KXYfCwCENtU8j45mNQBBuYi3LVekE_IZgDc8TlyyBDlIc7DTGAAEHwJqP40IA5GR2LkhBVWJjizBScMPf2uphDwQai7XIF9IB2RUdqxeWPeLCiNEKytNCSJvndN2KWWCOA5cnnYpw6cKTkHfDGFRmsIe0OLd2xC69reQFYKyRbItphWZK71L8dxT1AbluAbYrXBhANbsloC71EsYzPPofkkT5Znyl8G_Esaa_ZhWSL06Lf70oFSfT5_D2Q2nHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل نرم‌افزار Signatures را برای امضای اسناد دیجیتال روی اندروید منتشر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665839" target="_blank">📅 10:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665838">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6aaecdb68.mp4?token=UIKpNfYxL43ukK6CTa3jwU8qW20LCowXYk6kMujqAblCN17kcEGrQYmkvs2AJLh63pA9zxQb1f-RIpEB5Utl5rxnujztXGN444M1NEtVyGFQeK_dL-zXpHtVwTwkrczDIl1DcWBs3CwJpRiv5Q_knNNTM16lPlMTbTP-LIgEXRRzE49tE2O7rI5XXB97hMdQ1kUwjYL4T11U3wQ7B8SsfZAd95PWipgLQIfyaH6Dfud6eIrLqwqCtQzvdvAGe34QlyTqZ0a1FJUpJwSZNepryjgpaBYIR-TIkYmHockmIUdJHirTvF6v_u5ZnVKpQ50VLVZhJKahKJytgNMKXqhhtQI_-bcngNt4SL49Zi50CLcq8GVdt1yGTF43mSjpKz_O24vXZgRFYUGHAI3d1zRQdQ76IiHqlhByDUhqiXaSC6JZV42IbSeIhjbPrCiqPrhf0OBKtzZxYa9hyAZxNrSf67tm29XufxCi_Vp82l7IHbV6aiJ_rSDLl2ZUxP5xUs7O1BJatfwtpumJ8olhE6ABfwDU9rob0qA5LRUvN4M246QfElTp8q2TnmENWvqNjdrT3HuDZQfrPlCJnzZJqkFgfDsLBPD0PlC3u7Bk1nc5ceWmSc-wtd4qoFpHI5DblTwJTfRko9RPYDgmwEAY8sB36gkSef65NKkvJFBhNpHXLGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6aaecdb68.mp4?token=UIKpNfYxL43ukK6CTa3jwU8qW20LCowXYk6kMujqAblCN17kcEGrQYmkvs2AJLh63pA9zxQb1f-RIpEB5Utl5rxnujztXGN444M1NEtVyGFQeK_dL-zXpHtVwTwkrczDIl1DcWBs3CwJpRiv5Q_knNNTM16lPlMTbTP-LIgEXRRzE49tE2O7rI5XXB97hMdQ1kUwjYL4T11U3wQ7B8SsfZAd95PWipgLQIfyaH6Dfud6eIrLqwqCtQzvdvAGe34QlyTqZ0a1FJUpJwSZNepryjgpaBYIR-TIkYmHockmIUdJHirTvF6v_u5ZnVKpQ50VLVZhJKahKJytgNMKXqhhtQI_-bcngNt4SL49Zi50CLcq8GVdt1yGTF43mSjpKz_O24vXZgRFYUGHAI3d1zRQdQ76IiHqlhByDUhqiXaSC6JZV42IbSeIhjbPrCiqPrhf0OBKtzZxYa9hyAZxNrSf67tm29XufxCi_Vp82l7IHbV6aiJ_rSDLl2ZUxP5xUs7O1BJatfwtpumJ8olhE6ABfwDU9rob0qA5LRUvN4M246QfElTp8q2TnmENWvqNjdrT3HuDZQfrPlCJnzZJqkFgfDsLBPD0PlC3u7Bk1nc5ceWmSc-wtd4qoFpHI5DblTwJTfRko9RPYDgmwEAY8sB36gkSef65NKkvJFBhNpHXLGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کرواسی به پرتغال توسط پریشیچ
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665838" target="_blank">📅 10:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665837">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fe7546a3.mp4?token=fvE27ODT6viU78pYJ3GFVVdmrx0NIbE9qY-sNIHobaTg37dUK3Ycoe0VSRgKLlyHCsj-XvoUBNz2HgXzilcQDpOihBriBCQf5Ic-1u1em7bQHxLp6BX9YFo_3GWGlWA2YMo_GrZQGrcEWN6YJt6KZ4vaOVcwOo25ynMh3oCVCRKsFxhX4KzZml6WOXxYxEn1giz5Y3IUgFGZGWhl7VPx8ApDQn4arcxl042s3pJndvjJuYLJ_2yzvALXqCXelxQEpEwki_zbhJbeUu8J2LYFdJ3CdLKbNi1oEhMlOS7jy_JpIV4ag01eYKO6WqaiG093-Y70gR8J1vSd5MezLltJig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fe7546a3.mp4?token=fvE27ODT6viU78pYJ3GFVVdmrx0NIbE9qY-sNIHobaTg37dUK3Ycoe0VSRgKLlyHCsj-XvoUBNz2HgXzilcQDpOihBriBCQf5Ic-1u1em7bQHxLp6BX9YFo_3GWGlWA2YMo_GrZQGrcEWN6YJt6KZ4vaOVcwOo25ynMh3oCVCRKsFxhX4KzZml6WOXxYxEn1giz5Y3IUgFGZGWhl7VPx8ApDQn4arcxl042s3pJndvjJuYLJ_2yzvALXqCXelxQEpEwki_zbhJbeUu8J2LYFdJ3CdLKbNi1oEhMlOS7jy_JpIV4ag01eYKO6WqaiG093-Y70gR8J1vSd5MezLltJig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان ۱۲ سال حبس؛ نجات زن فرانسوی و پنج فرزندش در پاکستان
🔹
یک زن فرانسوی به نام سیلوی یاسمینا که سال‌ها پیش با مردی پاکستانی ازدواج کرده و به پاکستان رفته بود، به همراه پنج فرزندش پس از حدود ۱۲ سال حبس خانگی و تحمل آزار جسمی و روحی، با فرار یکی از پسرانش نجات یافت. پلیس شوهر او را بازداشت کرده و این زن قصد دارد به فرانسه بازگردد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665837" target="_blank">📅 10:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
حمل‌ونقل عمومی قم در ایام بدرقۀ رهبر شهید رایگان شد
شهردار قم:
🔹
همزمان با برگزاری آیین بدرقۀ رهبر شهید، استفاده از ناوگان اتوبوسرانی شهری در روزهای ۱۵، ۱۶ و ۱۷ تیرماه رایگان خواهد بود.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/665836" target="_blank">📅 10:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcVA-kB2OpcoJ4xaT7fzeN2oGhnebJKCLsdPkrXkqQuWzQ4l_zMCfsnLmsdI8AjXXOcK6ml-Gu6qFxUQD-3e_-5YTteA2b89gnNfBPYeNO4hw0jKWCAU1_yk-SMtE4mNbNT74eunxUYMGQSEpA_Yiogl69JPuQ6py9IOcr5nRvAoiGSIjUCTFnOIZwrvfE-o7AFeWYyZUYj3hMeoYhvz6Lg-HiISnYVPXV5NjagFuyTp5ypL0TvFF89Xgadp_a4DGQdxOKxuhRQqgvAM43Tor4DklB6c0derd7Tirhfz3bsD0j0jZ7rXf2f_Kza555Ktn_gn5Rt8E9IIDqsmkFp2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ظریف: «دوران بزن‌ دررو تمام شده است»؛ ایران دیگر فقط تماشاگر نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/665835" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665834">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=horEuOIdvOMj-tLsL2HEQSrzob68ZCVJ18iNKeMVjTDMecTvNa42wawpsM84_BJruu3w4e_bENPyE_oN7s3FFk-i3Of2LC7zqMl065THN93Asag3cEvjmy-zJv1eAo4HAnoKXVrbBuH6RTGiLMe8mDJS7tYrEsKa684m3d_IwdNMPZ8W8xi4YE8badC7H9Qo2rZpZ5v8GimYQ_P5ZlJLZAcooUTiSrQckrOctJ9IdWp68ias9Xq8yc3wkvYhzWhM_qut2i7k1zwUfCjriufs26fzKzLJJVqPQGEiPz91VU5aQeXRvEkzQjH6mxbv9gpwu99GDQgzyGjga6p9Zyndig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2cab2b78.mp4?token=horEuOIdvOMj-tLsL2HEQSrzob68ZCVJ18iNKeMVjTDMecTvNa42wawpsM84_BJruu3w4e_bENPyE_oN7s3FFk-i3Of2LC7zqMl065THN93Asag3cEvjmy-zJv1eAo4HAnoKXVrbBuH6RTGiLMe8mDJS7tYrEsKa684m3d_IwdNMPZ8W8xi4YE8badC7H9Qo2rZpZ5v8GimYQ_P5ZlJLZAcooUTiSrQckrOctJ9IdWp68ias9Xq8yc3wkvYhzWhM_qut2i7k1zwUfCjriufs26fzKzLJJVqPQGEiPz91VU5aQeXRvEkzQjH6mxbv9gpwu99GDQgzyGjga6p9Zyndig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وداع جمعی از اعضای حزب‌الله لبنان و خانوادهٔ سیدحسن نصرالله و عماد مغنیه و فرماندهان شهید حزب‌الله با رهبر شهید انقلاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665834" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t41sHOHj9x1elri5GbT-RYHBL1qqCRLErPi48AIOaPX_2Sre7B6nfHCjZDQmO3UH-pP2h0RQsAdNREtf0WIiGpqImJxE5-HVe2lp3TMoKiNjPqx6-vvwPWjjyGnfgIovLdmSbSUwIAE1DjP5LCPSaitrxcLzvMvs-6vrNbUYkjV2eYDaXppuThpWp2ZTMTnXDzSGXUPcfJQyqEuh1wUXA_eJNnxeJ4g7ZDBv5e_xkkDvxSUTixDM8ywfL5WkmofaEaJmWNh5ok-DQdEOyTHva67e3Xm3Z1n77Gt8_zLq82nb17sT_Vl2brOQkSQyZEznyzgg7ORf9GyFtaIYjb3yfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی کوچیکتر از اونی بود که فکرشو می‌کردم...</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/665833" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665832">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs-BhKHn-Jy70V_T7tg2xbEPRiM0kE-lX9JJeWcpwndzE0KJAT90dfQJvZaoJ0DjixvNi3Y_GfhptF6-RXTk38KVVju0UQrlVTaM8y9uMBHhmDiF3rw0RMgwWoF3271zP2tbop0XZNIvidQA3Lek7ZaXkHSMum5mR3d18b1PAaTvdwMQHv6chGRxLPmDTLGM6L08qELnDvjrCs1GZ_bpYU7eXPuAsKrowLBwL8jIX-zXXdqTZcoh2rCJ7mv4IPp9xw9aIx2xEpw_2OffBxK9nsCf6dH_7cTBuIJPxmDu0ms1HUFK9iBDayuItF3FAe3UFQW8nnxr4WILAnqVee2e4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن منظم قهوه تا ۶ سال مغز را جوانتر می‌کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665832" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665831">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eb6d2154.mp4?token=E-dTP7mcFnyaBES9Uzguz7Zy0jK7VL67MLLBRF_PiMQSVn4BNrY3rmFcEPpo3XGpBVX6lqizippE84I_UxTQnRPISSIyhAxOZdmxPnVQBLHyfN2rvJTYJ_H3jBHt7BH95sPJgPO6wnnnSafmtuXsQxLf4YncbUbsfhgVLEZlK_Bv_BxAI5wmrE98M0QT2lIzbR0PSu4VibEAdITuyrySOGtGHtg0mHGCYOMmb0tDBOEhPZNf1204y8KeZSvjfIeiu1jVlRh-4GxR15Fuf2kUiRVY2gmMQ-FLnQs2yCyc4hNGbI-IsbCN-CXR9hMMGDKj78-zXxHwKhRgew5rm0s62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eb6d2154.mp4?token=E-dTP7mcFnyaBES9Uzguz7Zy0jK7VL67MLLBRF_PiMQSVn4BNrY3rmFcEPpo3XGpBVX6lqizippE84I_UxTQnRPISSIyhAxOZdmxPnVQBLHyfN2rvJTYJ_H3jBHt7BH95sPJgPO6wnnnSafmtuXsQxLf4YncbUbsfhgVLEZlK_Bv_BxAI5wmrE98M0QT2lIzbR0PSu4VibEAdITuyrySOGtGHtg0mHGCYOMmb0tDBOEhPZNf1204y8KeZSvjfIeiu1jVlRh-4GxR15Fuf2kUiRVY2gmMQ-FLnQs2yCyc4hNGbI-IsbCN-CXR9hMMGDKj78-zXxHwKhRgew5rm0s62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نیچروان بارزانی رئیس اقلیم کردستان عراق با رئیس جمهور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/665831" target="_blank">📅 10:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665830">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سپاه پاسداران: خطای محاسباتی دشمن با پاسخی کوبنده تر از همیشه مواجه خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/665830" target="_blank">📅 10:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665829">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=Ypd7nx7-Te5r0U6cXMUWLKhtjd0aU02tuf9-Bf8Jjmdg-iT8NSRtyHorg98WiUb_wwnSGoLW6tRo-oLOJNjFOqAc6E8mp1b2zzhhJ3hLRAvDR6miyq6Ldil6zC__GKU1_aiguiUaG_GhisbabWtfdj_X1phQnzL7kZW4JvpRYgiUV1voeKaVHPN4hfRcLuKkRJQSsxn1JBBMVxWKv7MguX9pwGiABRk6VQR08wnf7clveH0osPRiXGt9h-l15AdoLm5H_8HTRO3NOKQA67Dg73L0QmpnfypkezrmU3_BfLhLMifoYvynuEqioL4vZpKvu3Ek1SWHlpu_iYPYl6yJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=Ypd7nx7-Te5r0U6cXMUWLKhtjd0aU02tuf9-Bf8Jjmdg-iT8NSRtyHorg98WiUb_wwnSGoLW6tRo-oLOJNjFOqAc6E8mp1b2zzhhJ3hLRAvDR6miyq6Ldil6zC__GKU1_aiguiUaG_GhisbabWtfdj_X1phQnzL7kZW4JvpRYgiUV1voeKaVHPN4hfRcLuKkRJQSsxn1JBBMVxWKv7MguX9pwGiABRk6VQR08wnf7clveH0osPRiXGt9h-l15AdoLm5H_8HTRO3NOKQA67Dg73L0QmpnfypkezrmU3_BfLhLMifoYvynuEqioL4vZpKvu3Ek1SWHlpu_iYPYl6yJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعی از رهبران هندو، شیعیان تایلند و شیعیان آلمان به رهبر شهید انقلاب ادای احترام کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/665829" target="_blank">📅 10:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
محدودیت‌های کارت سوخت حذف شد
شرکت پخش فرآورده‌های نفتی:
🔹
محدودیت‌های سوخت‌گیری با کارت هوشمند سوخت در ایام تشییع رهبر شهید انقلاب برداشته شد.
🔹
صدور کارت المثنی سوخت نیز یک‌روزه انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/665828" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351721101b.mp4?token=tBSg2QY1aW1MES4mAIV6oOyGohz0nt7c6qj9DvZrWbTAi5Js5PERnB5xoUCMBgtYPu47MwaXwPBhtkbUun10I_y-LEnyX4kTdoMT7c3ZYqVnObEBFluk9eBnstMIxJDdrQfCx4LX9wTqJEryw2ZBC1isF_DRnnnFw0uWHwQKBWp21prs6NmCGkwqFoD_Kpzad7Rg7XacZs91YOZJYvK4e97XLfCJlnsA91X5iFAtzW_YxED9Cm0nlQmoDY_TytUY4xFwh_MCSfe2VpFK-wbjg8Pr0RjyUlSDXlfwxL1fH9K7Ajq_uFAvMbCPjoGY1RZxPCrm2KXDuLuW6slFIlzAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351721101b.mp4?token=tBSg2QY1aW1MES4mAIV6oOyGohz0nt7c6qj9DvZrWbTAi5Js5PERnB5xoUCMBgtYPu47MwaXwPBhtkbUun10I_y-LEnyX4kTdoMT7c3ZYqVnObEBFluk9eBnstMIxJDdrQfCx4LX9wTqJEryw2ZBC1isF_DRnnnFw0uWHwQKBWp21prs6NmCGkwqFoD_Kpzad7Rg7XacZs91YOZJYvK4e97XLfCJlnsA91X5iFAtzW_YxED9Cm0nlQmoDY_TytUY4xFwh_MCSfe2VpFK-wbjg8Pr0RjyUlSDXlfwxL1fH9K7Ajq_uFAvMbCPjoGY1RZxPCrm2KXDuLuW6slFIlzAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت علمای روسیه به پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/665827" target="_blank">📅 10:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665826">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8f6f331f.mp4?token=JCVvQdDzfx_M_IqzFRbPvJ54lPNpItchcm-ByxPIPhU-aexcuXdaOznUj1NTuwAHmHXBt5o_zvVdE7MzNiCfw0Ayoao1cIKYXyIl1-U0cXKepj4YjNLBZvoorHMEA8uVREtQlS2KihylOuzAkFqJ7R8x-ebwAFapf8kkFKW4n3q4NaUEjYPrp-K5YiFT7DasM_nWarUS3bInRQRSzeJ84RjrNcWkvuWNHHbHMRQeUWPHQ3d2Ka_DqRprKSBW2ihXJP4WVKj75q62CBymWklbxEBG6I2WSaND7-7HWmdrycSOp-R2Z2a67x1Y1SSB0kxAZsZuBwZLe6ea-gqmyOxatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8f6f331f.mp4?token=JCVvQdDzfx_M_IqzFRbPvJ54lPNpItchcm-ByxPIPhU-aexcuXdaOznUj1NTuwAHmHXBt5o_zvVdE7MzNiCfw0Ayoao1cIKYXyIl1-U0cXKepj4YjNLBZvoorHMEA8uVREtQlS2KihylOuzAkFqJ7R8x-ebwAFapf8kkFKW4n3q4NaUEjYPrp-K5YiFT7DasM_nWarUS3bInRQRSzeJ84RjrNcWkvuWNHHbHMRQeUWPHQ3d2Ka_DqRprKSBW2ihXJP4WVKj75q62CBymWklbxEBG6I2WSaND7-7HWmdrycSOp-R2Z2a67x1Y1SSB0kxAZsZuBwZLe6ea-gqmyOxatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای تهران در آستانه تشییع رهبر شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/665826" target="_blank">📅 10:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909be738a9.mp4?token=L5hP6qYOMs525xzVlIUf-NwDNZSYhGO9e6BhWpBRtQDcWgIPzBBLTvev2a0Ord-F8MX7ZGBJSn75uPgjw_zp7RaPvsyCZJYkI0fbqOJ1wCVgM90eVhjoXDIpap2reh2YtS7-I8asW5dCDTSl7TlTckX0YpoM2aubWbDvxqrtIobZRFoPbiPBpE2V8yMHJdXDD0x1cPfYacZgDUjBxgB7GVMxyzRGOl4eCFN-dOdzwOvXo9pCmWllqoCqn23cfd6nCBzIX4PIry8r1VIoo9hrEcRE80dijQfcdNfYTHLgvoyg9lVWzjkUyHQHRIhdYVVO5e31nGyYJ3gLDKTcvrBFTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909be738a9.mp4?token=L5hP6qYOMs525xzVlIUf-NwDNZSYhGO9e6BhWpBRtQDcWgIPzBBLTvev2a0Ord-F8MX7ZGBJSn75uPgjw_zp7RaPvsyCZJYkI0fbqOJ1wCVgM90eVhjoXDIpap2reh2YtS7-I8asW5dCDTSl7TlTckX0YpoM2aubWbDvxqrtIobZRFoPbiPBpE2V8yMHJdXDD0x1cPfYacZgDUjBxgB7GVMxyzRGOl4eCFN-dOdzwOvXo9pCmWllqoCqn23cfd6nCBzIX4PIry8r1VIoo9hrEcRE80dijQfcdNfYTHLgvoyg9lVWzjkUyHQHRIhdYVVO5e31nGyYJ3gLDKTcvrBFTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های بی‌امان فاطمیون در فراغ رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/665824" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665823">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
گزارش سی‌ان‌ان از بدرقه آقای شهید ایران؛ نمایش قدرت و انسجام
🔹
شبکه خبری سی‌ان‌ان در گزارشی، مراسم تشییع رهبر شهید انقلاب را حامل پیامی از اقتدار و انسجام ایران به آمریکا و جهان خواند.
🔹
هدف از این مراسم، ارسال این پیام به جهان و دشمنان جمهوری اسلامی ایران عنوان شده که نظام نه‌تنها از جنگی موجودیتی جان سالم به در برده، بلکه رهبر شهید خود را به نمادی از مقاومت و پایداری تبدیل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665823" target="_blank">📅 10:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665822">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab42ac3b54.mp4?token=Lh-8SP3iOj3I6eZ8rx0HQRd_QXHeGg4lVAnV2t9DcR059iZrdCfPCJYFLw2YK-67pjVYd8g0T0-dYTumNz8raMZNvD9iK6I37uRm61WGo_5zMPvuak_HQMyGvtchNknUO69vViZYdDnKByABm6IQ10A_jjahOb8x7wgmGy7lsMS2sQtMubSbYwCbUN_Cr4TOMu0fJ9Rv32Rb9EgngVu-PJXeSonh9JZXFpYy0T3hpaf1-cZnh9zSVoU2JbEhBaHmumkuWsGtjSXG5IOUm89azARHxmjyqVF5sJzVEC9hYW-W0ajTOUMHJhcxwnz_Mqi7jM8iCJ5haaJp47rVxIXbQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab42ac3b54.mp4?token=Lh-8SP3iOj3I6eZ8rx0HQRd_QXHeGg4lVAnV2t9DcR059iZrdCfPCJYFLw2YK-67pjVYd8g0T0-dYTumNz8raMZNvD9iK6I37uRm61WGo_5zMPvuak_HQMyGvtchNknUO69vViZYdDnKByABm6IQ10A_jjahOb8x7wgmGy7lsMS2sQtMubSbYwCbUN_Cr4TOMu0fJ9Rv32Rb9EgngVu-PJXeSonh9JZXFpYy0T3hpaf1-cZnh9zSVoU2JbEhBaHmumkuWsGtjSXG5IOUm89azARHxmjyqVF5sJzVEC9hYW-W0ajTOUMHJhcxwnz_Mqi7jM8iCJ5haaJp47rVxIXbQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نمایندگان پارلمان و حزب جمهوری بلغارستان به پیکر امام شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665822" target="_blank">📅 10:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665821">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5622c9a5d1.mp4?token=N94MJnt7GR6N3GvEw8Xd0QFzpoKhkvogfj95yFZE-pAlGkQKPJatTYGhFWEC9flISsK1siRy5WPb3Ur31psSrr39PalVsbARcZB22COb1wI_YBlf4QnV_tBLS9IHADNL2RdRZHWKEzyxLeidILXEEM0FKgQyL3C19y908R7qLjKakfWnPPlfyXbtRzw4jaldnHJjCNUl3IOwG5bpzw2RxD5O6M9WhUyXKkmUsDmwfh8a5aCpW_RvLqYiuL44__n-fztF41za5PVll_RpxnW4c71Tgyhhs0HuoIoaUc6DweJ_XqXH_klQ8bLtq6M-S6wDPk_fa2REqh1XHEI_Rh7HaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5622c9a5d1.mp4?token=N94MJnt7GR6N3GvEw8Xd0QFzpoKhkvogfj95yFZE-pAlGkQKPJatTYGhFWEC9flISsK1siRy5WPb3Ur31psSrr39PalVsbARcZB22COb1wI_YBlf4QnV_tBLS9IHADNL2RdRZHWKEzyxLeidILXEEM0FKgQyL3C19y908R7qLjKakfWnPPlfyXbtRzw4jaldnHJjCNUl3IOwG5bpzw2RxD5O6M9WhUyXKkmUsDmwfh8a5aCpW_RvLqYiuL44__n-fztF41za5PVll_RpxnW4c71Tgyhhs0HuoIoaUc6DweJ_XqXH_klQ8bLtq6M-S6wDPk_fa2REqh1XHEI_Rh7HaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روز مانده تا بدرقه آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665821" target="_blank">📅 10:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_ANcvfD_HZTS9Uq0dZEXq33FUkmezKSUH9nvFph9XhmJ88HDAeRpjDaBgQdYeKmMeAGs79JXHSI8c1YYnzQxgvAwg4ZLS7jx3xGmXk32jFwnNygBpj7I4U1xQEhtUPNisvK9dojY6lsfV3AiO60tpxzfe9YdBfzrfpODoJ_v60L5VdhzjNKl58Ay7rzR0FKjkijf4y93W204Lai2mZ7djW6qWw6AkXCUzDM3SnsrjSjQnj4kj2oJIsejuTdN65iLOvanp1hGyNZnHIFWSX1YRk3EEbL6dED3Gkx4EKVHb5-S_TcMZ2ge2tlTKVEpKzGHkyIrcVckhRI8m0tudsOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنده بیرون کشیدن یک مرد ۴۳ ساله از زیر آوار،  ۸ روز پس از
زلزله ونزوئلا
🔹
تیم‌هایی از هفت کشور - ونزوئلا، شیلی، آمریکا، پرتغال، کاستاریکا، السالوادور و مکزیک - به مدت سه روز به صورت شبانه‌روزی برای رسیدن به این مرد تلاش کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/665819" target="_blank">📅 09:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f860cc7e0.mp4?token=F-yxY6Vq4xvityomyf0FumJU2q-oELjVHgfLv6y0rgbjyhdw4gNmSZUhsZNo3kLDAbSd-jiKiRIenuBmon6NG003vupV3YdkfAncPvzVZgxnoloXwXVJXjhvn7xN1De76IymM_7c_jZrmbNPtLG5h4g3tG_WZ1rPf4v9bOJPC8AKjgApHoPVjcl2sTNHeDjX61rstHU0JP8wfjQLOS2j8cuYDOq0yAVijyO8cUetW0ThMIm1Z4jMRpNEycbwaky9A6qoOiqhsJti4bodkG_CoUpY3eE1ytcBO2ibmUrTfnx_O5wETEk44XyOcyyrnmVTjDBJW97QhCOEbNgDONmTIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f860cc7e0.mp4?token=F-yxY6Vq4xvityomyf0FumJU2q-oELjVHgfLv6y0rgbjyhdw4gNmSZUhsZNo3kLDAbSd-jiKiRIenuBmon6NG003vupV3YdkfAncPvzVZgxnoloXwXVJXjhvn7xN1De76IymM_7c_jZrmbNPtLG5h4g3tG_WZ1rPf4v9bOJPC8AKjgApHoPVjcl2sTNHeDjX61rstHU0JP8wfjQLOS2j8cuYDOq0yAVijyO8cUetW0ThMIm1Z4jMRpNEycbwaky9A6qoOiqhsJti4bodkG_CoUpY3eE1ytcBO2ibmUrTfnx_O5wETEk44XyOcyyrnmVTjDBJW97QhCOEbNgDONmTIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد خشن پلیس آمریکا با هوادار تیم ملی مصر که در حال گرفتن سلفی با یکی از بازیکنان این تیم بود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665817" target="_blank">📅 09:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXD72h4laj8ENZU7uoMVWzVtosfRi2kT5COoOvWc3TFrFZvIPJRDYoTqLZGHFCXpNPQueyZ1Nn5ZrvVMgE2PHqGE1QWantaivErZ8VEzSM9oBC_jswv_EDIzDVy6DtFFGHoXcAqMkwYRfgsYePHLkEh9v8gzR8oZ5kNgAvYdi0Jxdzgc9laemqoskp5ClWKDHcWqdHCNvYPzUpzD0UqXyZHOIoZEkg-1rAecqrRRCw56g3xOslNuWCen3rmjD3qGAXftUSDH6mjGx0txHbseJ89WGZFgPQzICxNGYALBCGhVnhveD_UdbA9zmHYwgU92NLL8hfO7qzSqNGZHlYdN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ادای احترام احمد مسعود فرمانده مقاومت افغانستان بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665816" target="_blank">📅 09:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665815">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYzqb8VwBhFQY765sUqkrYsJm_OxBysyhKzYZPpVKg_sbLtRvpL0_azKoCr1BqncoeffWA1z7No8dMgnaFEjzqhl6S5yBiWIHg9Lp8lZ-IG5YgBdZgCLXFHgCRx0aFinXTg9cazZj-sdodsEQQEcb_3q_HkV_CzaJk5UptjeEAPMOWy1ZBDmQ6nXGusPJKHE7A2h2fA6T64KPRDaqPjldjGpwJ3GDImfgm1H6QcF8wGaPcyB3GCBG6DwKHreuFeF7Cu6GIYN_Viz0FzRhJDV0wvycmoJOe0_BQeuVcY4DX2yV3Dpn4uW-cwry8-WAiMjErpXqLt69NJPxIi5ms761Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشیدن منظم قهوه تا ۶ سال مغز را جوانتر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665815" target="_blank">📅 09:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=ERPlp5eREWG2iC9q1cybPTE3BXDDT_X1qb-p-AeP9t6BZDQGCezPIghetUTbrP43sAzcxGNiQW6MXiqA4_B0g6HXtWVXeyNH8ByYF0MuBIrjr3jnmHR2y0zx72jRB_BYcdHSmSz7ZglyPzRwwRy_LD9nDsEqLqs5vKSjiYgGaSnKGkVBK7LZVxy_eFiZ_3TEXpU960smXMs4kO-6WylKZA7tS8ipRLS4pqXmzA_oT2ADftO3X8yHw8cyBwVhk5gskUhNIkXf_I1vZCoELx8aSF_DWXWxPB89Au4_JJcPEJ9YQKvEapt5AB4xVvgvFkDSIC_BleozDdXV3HuNA22vdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=ERPlp5eREWG2iC9q1cybPTE3BXDDT_X1qb-p-AeP9t6BZDQGCezPIghetUTbrP43sAzcxGNiQW6MXiqA4_B0g6HXtWVXeyNH8ByYF0MuBIrjr3jnmHR2y0zx72jRB_BYcdHSmSz7ZglyPzRwwRy_LD9nDsEqLqs5vKSjiYgGaSnKGkVBK7LZVxy_eFiZ_3TEXpU960smXMs4kO-6WylKZA7tS8ipRLS4pqXmzA_oT2ADftO3X8yHw8cyBwVhk5gskUhNIkXf_I1vZCoELx8aSF_DWXWxPB89Au4_JJcPEJ9YQKvEapt5AB4xVvgvFkDSIC_BleozDdXV3HuNA22vdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام اعضای جنبش امل لبنان به رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/665814" target="_blank">📅 09:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCSRPvfr_IuzPrFdvy0IEu49EDDkjUtMvM3RhozO-WU6ScB063D0BZoZ_GpqACnsFyV3aHv7P7HQbmTOoaOyzL5bKAx3fY4cca3F6cIsGo6Hz8JyShEJtXE7YGBVWPqVGJ6mMmMolY0IzSb56ygTWA04DlWZXuwNNIDx-5qafAOzSN22SIPx2Znjog_bsuiFWZhIA098SbZKn7gksLIIjZVBlpB-c4DuJ1TXiz6i3oSkZhD4y5E0erQ-rvUcWi8Ne8EagaPrNT5-BUo9AO6naZB1z6sfDJngDILQjPHjG6DwXlx-PvhVPkyqcnMZJ2W-nA5haMSCOVGkzLu2gY-pKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود پیکر مطهر شهیده «زهرا محمدی گلپایگانی» نوه ۱۶ ماهه رهبر شهید انقلاب به مصلی تهران #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665813" target="_blank">📅 09:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665812">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f5f27434.mp4?token=oPljT9eykgWA17H7WzWZyY1C373zwzU5FKnl8s_b1QHcHCH00i0egiD7aHVoaS0XXVjwZK9Id4Rd2t2iaeogLaf4n5B8Iv3BKrMGi8yoKiY2ey_XsiXcNgJUhVoRNjKiZvwtSVJlSccgLBsRPmYHbl3R8sxFDZ-3TyWOzi0-TodQQSGvL8IxQnOTw3bjx5h3SATazdD7IMLQ5EeQiC9u1WzSbYwQmAjtpqewfcnUNz6ZLfWqMlt8_qFMyXrd-ee4QOLf9VipxnCIrtbDXUOFor_QDxkPAWiKzMtlXl7ZBMvI-toEGCpIRkFly8sGFSC4h0603k5dndwdG67L0UL1q0dBIIzmJwpqWH4TEJ3vwlkXl_b6fLcJ1Y12wiLqPQC_TL2W3AwST4kfh63lDcODnhZmCGaIn5N0Ed4kKWAPmHW4ISXfhC6y77mPTTsUygGulHQOZ4C0s74rdAzpXGNbWVWDbnrrGU8VWvcO4ZJ5kyGzoc-_Pi8nkJ8joXuHL8xHCd3lfqv7dLunZYBlSs9ySbd8p7aRr8GkG-kOG_2eBych6jetK2tmLTZRFpk1YYMpFAyPzJ99gN4lSVELRgVH0hnlYV7RWaE2FJIUCawRJaVF5W5zBicSMN7CVeQnqNJdBrmL9Ca4_Y3wfxl2Mh-RjkaFRcEMTkF2rV5ASU7O2OY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f5f27434.mp4?token=oPljT9eykgWA17H7WzWZyY1C373zwzU5FKnl8s_b1QHcHCH00i0egiD7aHVoaS0XXVjwZK9Id4Rd2t2iaeogLaf4n5B8Iv3BKrMGi8yoKiY2ey_XsiXcNgJUhVoRNjKiZvwtSVJlSccgLBsRPmYHbl3R8sxFDZ-3TyWOzi0-TodQQSGvL8IxQnOTw3bjx5h3SATazdD7IMLQ5EeQiC9u1WzSbYwQmAjtpqewfcnUNz6ZLfWqMlt8_qFMyXrd-ee4QOLf9VipxnCIrtbDXUOFor_QDxkPAWiKzMtlXl7ZBMvI-toEGCpIRkFly8sGFSC4h0603k5dndwdG67L0UL1q0dBIIzmJwpqWH4TEJ3vwlkXl_b6fLcJ1Y12wiLqPQC_TL2W3AwST4kfh63lDcODnhZmCGaIn5N0Ed4kKWAPmHW4ISXfhC6y77mPTTsUygGulHQOZ4C0s74rdAzpXGNbWVWDbnrrGU8VWvcO4ZJ5kyGzoc-_Pi8nkJ8joXuHL8xHCd3lfqv7dLunZYBlSs9ySbd8p7aRr8GkG-kOG_2eBych6jetK2tmLTZRFpk1YYMpFAyPzJ99gN4lSVELRgVH0hnlYV7RWaE2FJIUCawRJaVF5W5zBicSMN7CVeQnqNJdBrmL9Ca4_Y3wfxl2Mh-RjkaFRcEMTkF2rV5ASU7O2OY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام مقامات یمن به پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/665812" target="_blank">📅 09:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665811">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=hLc8TpQDZFhs2h1bMQTHcXdL2LgKOLwCt9pvqzaf8ixJgxk1KTXfO2vJB5e3oguhHS_w-YUa6y2QWg-TAZjs3RK37ub3S2E1I92KP2NU_LLVVNgGRKrmfmQMKADmWx0Kso9h1E9BlQSTKG-uk5uCFfo3I_DceiZlqRTuoT9Cjfh0k8soLGKtk8V5Vp3bQrsiPM5v4spXG_zS7HYI9gPkDklfw5LRRZ5IU0JCD1pGIKX1U1WXvSvFAUEromHKmmA0r1kqcKq_PhRFy8l-9VG0WMYaBJOHA8FI2O2Bqe8b5uyrBqkvf1N5mfj9GbWNKBVeky8RsgtKIaK1XEWyd8TzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=hLc8TpQDZFhs2h1bMQTHcXdL2LgKOLwCt9pvqzaf8ixJgxk1KTXfO2vJB5e3oguhHS_w-YUa6y2QWg-TAZjs3RK37ub3S2E1I92KP2NU_LLVVNgGRKrmfmQMKADmWx0Kso9h1E9BlQSTKG-uk5uCFfo3I_DceiZlqRTuoT9Cjfh0k8soLGKtk8V5Vp3bQrsiPM5v4spXG_zS7HYI9gPkDklfw5LRRZ5IU0JCD1pGIKX1U1WXvSvFAUEromHKmmA0r1kqcKq_PhRFy8l-9VG0WMYaBJOHA8FI2O2Bqe8b5uyrBqkvf1N5mfj9GbWNKBVeky8RsgtKIaK1XEWyd8TzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سال‌ها آرزوی شهادت؛ سرانجام اجابت شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665811" target="_blank">📅 09:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9688fa726.mp4?token=ZnjS5hhC6HXQaaF2uLqTj-rD5nx28Jhn69AevMgRmd4gOw4eATp5BQ8l2horA8mbTCvRnbvN407KxBVlR_4EUqVhV9q7XJMlzgz3qYWxg8_iaTn5qdKCF9YDY2Bct3K4ybrS8vomr3yBVYJCEVcTwyVNlnCQygcZ9ecLSx2yrIVn3a2aoYdCo7VShyF6Ja8vlN28JL-t-HVeRSx1j5t1rn6-XxJpWp6jBXNQAq0_jXT_OGQ-lBohKJ6Rh00JVf2B3qJaqSIPiWMJtFCm6MbzGCwASBAEYHppaPbx63CeGm8n1_AbiioyTNZ6iFTS6qg71JCLeS3ZhXt4HyY92zd4aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9688fa726.mp4?token=ZnjS5hhC6HXQaaF2uLqTj-rD5nx28Jhn69AevMgRmd4gOw4eATp5BQ8l2horA8mbTCvRnbvN407KxBVlR_4EUqVhV9q7XJMlzgz3qYWxg8_iaTn5qdKCF9YDY2Bct3K4ybrS8vomr3yBVYJCEVcTwyVNlnCQygcZ9ecLSx2yrIVn3a2aoYdCo7VShyF6Ja8vlN28JL-t-HVeRSx1j5t1rn6-XxJpWp6jBXNQAq0_jXT_OGQ-lBohKJ6Rh00JVf2B3qJaqSIPiWMJtFCm6MbzGCwASBAEYHppaPbx63CeGm8n1_AbiioyTNZ6iFTS6qg71JCLeS3ZhXt4HyY92zd4aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام شخصیت‌های مجاهد حشدالشعبی عراق به پیکر قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665810" target="_blank">📅 09:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnqbF_aDhtkHrAA4dINB4nTKCP-16p7xf6DeabwhHF0lmt6cO0SaBYqYadCHFrPnkL9oDY5yROSxjn5DTyL1hU7sRL_APdKgu6TVYm59709EbeXRnRWP2GWgKTsDlMqrPIUoe7uqvqBJ12sBise3AqzokT-0esQly4BbK-68CuLThiOk_t5_eAqE5tTcfMrIVp5umtP8EHjyLo1_hVc5IIZdxUYcEyz-ujzpTrVYCrLMKCEV2H0Wzpw_CRcHD975jMQ4qG8OVS4W4SRiQtuNVigHr2xNCPTVGsn83Eax4dxY38Kamix0IdZ_mMh332uAkiL2LI0E4z8GnrluCwFG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc9OmoV3QoQ5O85uRnHLrR7KJEePSYP9s8fSN32eKDNb6MWMDUZfSrUoFVZliUj4LHsoU4J5p-Pyo64ogNvvzcAbCPQbKz1JGt6pc2le0F61go50Wcv6Nylfo8iHLezBgLuLgQSa4q8eR9mOuRx1UoLtSSuc8QASbMOziJTcTxC1optPWoZQmmEnfSd9U7cHpRJkbD7Kl_j_Az7tXSSyYUZ5vGVVFJVM5GE-mlLfGvwDpoKTVMwXFfY8wwZgwM_ibYzU66N0gOE7VSxrdzDMlrBz14QTcVqII0RQ9FKsWUymQy2YIU_LHDQzU6AIYa6sPt688tn9NMH2obgItz9A8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcUerNrD-1npkYLoD0KtikvqZyi2zzRn6M9uDc-BISFxAZcWyNb-z09CTuQjXD1jPjisR083RC6jxXRsNRSjqsdQW92BEL5ow4XXW3UOUtSwZ7smsDZWm07ph3gsSFlyFI9gmdf0gxfpYZ-NdBKG3soDQWMnmVsinVywSnr-3fBpkjFp4K1YMnGYEL2aJtnhQVhcZLOTzPDjZvfOSf-CzNheMXjtE6B8AkTx0eRjUrsMdOoHc4Lm90b6Jwz8WacWJIZEFgaE0P2_ZVOru2ss0AegI9a17yeBJ2LyK-6libcwegHbeEEcwLKO4eFbt1Sky1lZ1El7HMyAzLaJ-Qksvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار معاون کنگره خلق چین با قالیباف
🔹
«هه وی» معاون کنگره خلق چین که برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب، به ایران سفر کرده‌ است، امروز (جمعه) با محمدباقر قالیباف دیدار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/665807" target="_blank">📅 09:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7188c59e7c.mp4?token=WfDE7FV7_dyxPZxnx3ZnV0vCXN3n_gAKa2wyL1VfJsXcbPoWu94E7WwKBMJwpxDYHUkeohbBSeZ6B0c6pQawbjJ_CHIksg92F0GXXBAU6cJSTIGUI0swIMJkPkdkkgirniIbwOm4NYSINQRiPzy3i2JEOv135WKG21MZdR0ViMTk1cQjC7RL_8x_kpOKDMFIVxxy290aLUW2Sh96kUZEoXRpCrNTmyPhcT7p5QdBCEipzjCfYscE8HAgec3dQhtIwhK2SQedBH7EOaSD7LZbCRVqZlnTsVrvxBXMLrbkboOWc9m6EhubdYuOh39Qyt0zIRm6eUI6wKqm4XW6KN738w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7188c59e7c.mp4?token=WfDE7FV7_dyxPZxnx3ZnV0vCXN3n_gAKa2wyL1VfJsXcbPoWu94E7WwKBMJwpxDYHUkeohbBSeZ6B0c6pQawbjJ_CHIksg92F0GXXBAU6cJSTIGUI0swIMJkPkdkkgirniIbwOm4NYSINQRiPzy3i2JEOv135WKG21MZdR0ViMTk1cQjC7RL_8x_kpOKDMFIVxxy290aLUW2Sh96kUZEoXRpCrNTmyPhcT7p5QdBCEipzjCfYscE8HAgec3dQhtIwhK2SQedBH7EOaSD7LZbCRVqZlnTsVrvxBXMLrbkboOWc9m6EhubdYuOh39Qyt0zIRm6eUI6wKqm4XW6KN738w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئتی از مجاهدان و شخصیت‌های کتائب حزب‌الله عراق به رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/665806" target="_blank">📅 08:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKgTaqwTo1wTqpvBd_XGETgcJpSdM-FkETWfX7dBKV8YmNQsFxqu8Q7qCDuoi_sYVpJl3682vEJYxxHkeZlzzbDoxO_TPZ_XPAF3J7fvkBGF9cKdu8Lv4aKnklLsWMm-U5p7n4rwoC-4H0VTHOu8aSOBfznHMeiAtklG0-1vYfu0Sxp8YuXCgVyQQ2JpVVXG6YT_T1K9QkhyU2cJrs5dRxlHLojrRnuNjGf2okSPt-DM_cfyohogQ1Q_fwcLrZmyr7M8p8nfqQiyqLxN82oS03_tB-eH2X3tOyYrmesBa6J_BJDal97snldiLMFZ8nPJnMcyCqq4SASK0_oN1zJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار جام جهانی بعد از پایان بازی‌های دیشب و بامداد امروز
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665802" target="_blank">📅 08:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNZWiLR3BtFDBiKU6LRIzHGjN7WWksDtXBbLy5cMZz3qV4CxgaT0GLW2bdRpKkCDeRiAjbK1VCRHgUTO0faD_XpciXTd7aONfIWANh4GshIUuJ8Te0qetG8qYknfOz-bIwa8AA1BiletqWDkdyBtYyeLd7CHKxpMbf9CVux2Yh9h6C35gzJMeiZaGEittcv96tM2ntJGJrH5CgHYhmBujcNE5HA2qnG-7014UD1PZXuSCKVLSfJHfYWsCIJUfnA5VXuImZ9XHVOhlxHnJbfOu4DBTZdXe1t-oz2yDiTeTZnDnkJYdI0cLRTuJJtehXCGJbFs91xg9QZJhpknlDCR6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epX9HGenDRM_y_K8b29g9AQRtqwsXqwGCl3gFZ8HADbS0660hO8w7IcCJ3VdFH4m3KRTGGRVoCpZ0CJwVqA_NQqCqsQouf2dvjsq8boXNfjKLgHf-dW0O3tFrVsIN-X_6lroysTdkiLB9fYVaJULI994uGV99wUduCFhtn6U8PdN57CUbKC-VG3sAFaBqcOAddZveY3z7ltQxzCPU2sRJpwJiCGxZU9X3iFolLOWCVkKDm4tRvxShk3Hc8IPLxoAvwdc_KPnMZm-Ha4PU1z6Wh_-WGUnc7ShtZ6N0E1P4hUkxSAHwcHCu2PFEOMiAcagNogktt-rXYHsiZ1bXHiB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFhArc6_cXXl4vr77KR1g_P7nukpEzoNGbWuo8GVZgwABXyQI9a6OBTIWu7YSPK9Q5L5YNPMtQoIUUlFA66-tuTlH9vtNq8gAVwZQqHulYYsGKvTHgTdL6aw-7PZsFMQSDPbi_Dn6X7FZREo4U2RcUEOVwA72Hr19GpnvRbsrizmujPfQWPKq9z-U0B4lpZNrsDQtlWWa2ZgDKBgAXRhgXjm8PB4kvX_C7ZuUfzK3LuL1QXjH7z2narIxipfG8Pvf5ZtfGV8Uy6W72PQ6FpN8HskUx_tcmIlnJ9picAB6rd4URaZF6FPGB4CVOYLuOEd9r6fdWjkF0MQKUFsKiG2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVIWWNBilQdDSmhi6Ymo2JfHk6H9iLPR24J1WMKEI7QlzO4UYwsoA695uQWduBWbNtw_wGkr01I9FSyNjc9T3qgAwQhHAPu-JXhCkkHrRl2rLr3QnBH2_lN9hKGTZwnPGTEGPzdB45xX4tYWzTjgmitUh5mZZKM0lMwtYKk8flvINyiZFD-vkAxihmSdz0kA8a-DozVkGRrBclcoiLiH5MdbAuY80zwpNIVo95O3H69Bc8RTyAX6ThziL1V45K7uTIDT0vLLrJE_YlmJwXyd580Eul1Pfdgh3VZOpiCs5ILG8amoMWsaqtnUASotyJz38LoZVa1ThNTYLCu85HHe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co2DkgYASiF1lBOiay2HHN6sDOLKU2wuseLC53b5X7Rsm8WE_chjmD0mrgBHQVMl_p2RpRt58Q_gdbwZxAvq013wDOam7P5FRTxAbtrVgL19YSHXMFhmrGXcbco6_HbsABjL72XMPyFUcU_VnpuDJfMaznyGS1Vv2g-4IAJV_7yPHVmXFtm-R7IL1hApfZj2fkStMNuP3cregEL06Sbwi9crsQXzi4b5Hiiseouw6IsDTjF-kiqzRwmwgsh_9EyRa5Zpc_PSH-8nkHgRb5ws07IcPKIl3JuItCXVJcD-gGJMid6Jcyt3QB-IH3B-n2l1C6JNKRyZHXahWBbw5WLHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حلقه‌های اعمال محدودیت ترافیکی برای مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665797" target="_blank">📅 08:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ddf75733e.mp4?token=DU_Kg9qOEzLmSfNgmM8imjbjLhh7sVAa4vWHwWEqL1B1sVzRzR9XJsCUfa-YfTpx-goHqFklLmJkmMbAeCx0CamxDtTz44zIcSdwlXWcL9PBF1ZhdTEm67orkLlMlCN8U4mjLRPezLJZ-5ZVBoeh7xqKHcMMETRTeenNiWceFT0Jm6EO_dJZ-xzG7dg6wZ4s2i46X35b6fmsFkHf84L1itzgF8NCvuVoxrweNmNiGJ-KYQKS1Fm50DcyK1MDeefdYhjx_OvllZFmdbriN5_QOO4yTriUR9cTxJIocOdG5Vq0pYNR1rMX0ZLOgnonApFc7fO4DAy7_oSEUz8X6qd5QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ddf75733e.mp4?token=DU_Kg9qOEzLmSfNgmM8imjbjLhh7sVAa4vWHwWEqL1B1sVzRzR9XJsCUfa-YfTpx-goHqFklLmJkmMbAeCx0CamxDtTz44zIcSdwlXWcL9PBF1ZhdTEm67orkLlMlCN8U4mjLRPezLJZ-5ZVBoeh7xqKHcMMETRTeenNiWceFT0Jm6EO_dJZ-xzG7dg6wZ4s2i46X35b6fmsFkHf84L1itzgF8NCvuVoxrweNmNiGJ-KYQKS1Fm50DcyK1MDeefdYhjx_OvllZFmdbriN5_QOO4yTriUR9cTxJIocOdG5Vq0pYNR1rMX0ZLOgnonApFc7fO4DAy7_oSEUz8X6qd5QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت‌هایی از روسیه و چین به قائد شهید امت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665796" target="_blank">📅 08:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665795">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/702696af3d.mp4?token=rPjTw8ctNAuB0NdZc0Yh5klj46bohr-ERGc1O41uldstEETgbcOaiEvWkUz_Wjx566LBULix6g8Cj3rqQ0zEh2jNns13YAUC_ddWjcAnDLXSidsp84Bqy8mKSpOBj9P3Sf8II72j4o1SNfEAVaNB993sy3KoMFuseJ4JYqm_D8F8_km1LcLhrZDOCuNMbWZfqVohBarhf9kzXs2CNFz6ROaaryRZHpO46m28fmuM2e8pbDWif9pHrgCHGn0P5wywkf2Z8fWyNBuoQVLja8TmC1waz-pHPrKGULyNGrjjK7RJIYgUdP-sVLggyDGVoSpGZa4V1YPX2zyFI0dwAZWmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/702696af3d.mp4?token=rPjTw8ctNAuB0NdZc0Yh5klj46bohr-ERGc1O41uldstEETgbcOaiEvWkUz_Wjx566LBULix6g8Cj3rqQ0zEh2jNns13YAUC_ddWjcAnDLXSidsp84Bqy8mKSpOBj9P3Sf8II72j4o1SNfEAVaNB993sy3KoMFuseJ4JYqm_D8F8_km1LcLhrZDOCuNMbWZfqVohBarhf9kzXs2CNFz6ROaaryRZHpO46m28fmuM2e8pbDWif9pHrgCHGn0P5wywkf2Z8fWyNBuoQVLja8TmC1waz-pHPrKGULyNGrjjK7RJIYgUdP-sVLggyDGVoSpGZa4V1YPX2zyFI0dwAZWmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از پیکر مطهر رهبر شهید انقلاب در مصلی تهران
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665795" target="_blank">📅 08:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ul5RVfKAR9bP_VTSSFjxTAPBzB-RcdCHXjKQlwgsSNDPinYvlCCygE1PjyyoL-hXi-TJFa5piJOVo98vpI80VIgTes1nCAHcrV2EP30SYxQixZ9e47lUGryXyvte1bg5XHTC0XJCkV5ImF7Bmk0FApDTdA4nhCzWdMuxdr0ayx2PxHSRmsRm8ZtOyusi0EPfxBBj-E-GlDRGDpw1TJ42Iu_TEB3BablXZyIgLaNhqs6TisJrwz_y_9twk3mB_MlW-9U1IFuWG7CmyueGdmo2YppLnf59YO2V9nSZxHlIjeurstKmQRoti_TxorPnBB10-FapI6aoSzm4AVUZsQHr7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از پرچم مقدس حرم حضرت اباعبدالله الحسین علیه‌السلام بر روی پیکر مطهر حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای رهبر شهید انقلاب اسلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/665793" target="_blank">📅 07:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665792">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2b0644df1.mp4?token=hDwVWaIbAZqMl11WoFklkKW5Ox02ScBEV3vHZtBBRW_86Dp3QNl9DLTZpz9s5x7tF-NxrZ73ghveDvSPHOkSKbiAurxVFjxGOd5ry2T9Zb0Cm-7nUounb9dnrOCWGDqgLwPFcjhllqfkEgjaOxQusPyc9Kw6bobp1YsSkPvdJMWS6F5Nif-G6oULKoanc6cDPp25l7AXJVFZgz_11G5N90kUAxJ0t2krqMpAgIemsrVnjWF_2NrddZwPeSJLo7fh_rEzyIU_8n8vd1cRietBauwTVCnnzrfy6uQ_aTKuSCbcNcI_yFrrxoc3jYyHkUC5fS_kau-ezRFrbuT9tLiBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2b0644df1.mp4?token=hDwVWaIbAZqMl11WoFklkKW5Ox02ScBEV3vHZtBBRW_86Dp3QNl9DLTZpz9s5x7tF-NxrZ73ghveDvSPHOkSKbiAurxVFjxGOd5ry2T9Zb0Cm-7nUounb9dnrOCWGDqgLwPFcjhllqfkEgjaOxQusPyc9Kw6bobp1YsSkPvdJMWS6F5Nif-G6oULKoanc6cDPp25l7AXJVFZgz_11G5N90kUAxJ0t2krqMpAgIemsrVnjWF_2NrddZwPeSJLo7fh_rEzyIU_8n8vd1cRietBauwTVCnnzrfy6uQ_aTKuSCbcNcI_yFrrxoc3jYyHkUC5fS_kau-ezRFrbuT9tLiBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام هیئت فرهیختگان و فعالان فرهنگی رسانه‌ای از کشورهای اسپانیا، برزیل، آرژانتین، کلمبیا، اکوادور، بولیوی، نیکاراگوئه و افغانستان به پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/665792" target="_blank">📅 07:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665791">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ad31c42c.mp4?token=bGSOWqydlBor8N70xu2orNIoYd6PDWc91ObMBOtAsVkN8SYyINxS5PGYcy3giUHerDirvjYNVB1SYln4x2Nj-vdkZk4lp9kN1JrSJBTJx-7hyWt20Hc_T_7bR7OWJz3QCQ2XGYtmRqOIfGfyC2dNQ4uxb-VJpCZ626r3JybY6YoLH0NeyGeStaRDIk1tCSLnkhvkbUYPD7l_beGot2XxceIR0vA7HYOqNzOktTs6uOc12thaPz_Y4qal3l3byXioEtitkbYsggFqe3oIehuP0Gd5RDgmU79E4RXUwll0n3efBg5izbYUm_Q7lfAJeJ6IvkU-xlETgSiQvUmCma3RZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ad31c42c.mp4?token=bGSOWqydlBor8N70xu2orNIoYd6PDWc91ObMBOtAsVkN8SYyINxS5PGYcy3giUHerDirvjYNVB1SYln4x2Nj-vdkZk4lp9kN1JrSJBTJx-7hyWt20Hc_T_7bR7OWJz3QCQ2XGYtmRqOIfGfyC2dNQ4uxb-VJpCZ626r3JybY6YoLH0NeyGeStaRDIk1tCSLnkhvkbUYPD7l_beGot2XxceIR0vA7HYOqNzOktTs6uOc12thaPz_Y4qal3l3byXioEtitkbYsggFqe3oIehuP0Gd5RDgmU79E4RXUwll0n3efBg5izbYUm_Q7lfAJeJ6IvkU-xlETgSiQvUmCma3RZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود پیکر مطهر شهیده «زهرا محمدی گلپایگانی» نوه ۱۶ ماهه رهبر شهید انقلاب به مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665791" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665790">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b127043fb0.mp4?token=GcMVSFN1B_A-n5naNPUSOvPVqUKqgJ7SgiIwA5k08W-BwRd-3G6BNLpAIaZi9U3yZFMqoqHm9g_S1FYGZ1Ac9PVShR6_gY4BRyAl7WQ7tQjVvZRoER3Rl_l5q6sHsEiIquwRonvifh_40rddrevlXr5ntRouOL9pSixE4PcAKR1UdThUj6qr9qqxr2ZGmK6zd6RCePXFbGZcWI0yA4ookJTFlpsFnWk8Z7sDw9Tgcbbxqm751GOakzH91TAU_5v6x6l42WtI1P1eRNjwqj8i0zT0bAKdeoxqRuIuZV33Ziywt0j57VaK39DvcIE5Aet7gM6tU3o9GxtlBqGfiWufIhoRzL1oR2_lyCLdjklRpXiqUnfW_Z--Touepx92saz5Kx12PIj7QhdG_3u1vY91SGDKGdqZbRdPTmmo7BmdIH99slXa25nPnevyQi48-jf3KTEmFsS3MyO2EU1NJj2mXpLSN4xi3D7xX1nSiNWXGF6WN63B7uzbr3k-Ijrk8nAK2z1hsVfyJYgP3vMxA1CUz2oWP1yCMfMrOyHXlgBiYHatH19nODyPd9pu5ef8hILRdvog6esPmZJAkkteegz7JN1i_opjX10dxwElN4AkH1Fp2BN9r_GZmZBHjFSUURsIboP8jG8WUchJdDzzuh-QqbOQn13qJJvvnnug7WJpIhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b127043fb0.mp4?token=GcMVSFN1B_A-n5naNPUSOvPVqUKqgJ7SgiIwA5k08W-BwRd-3G6BNLpAIaZi9U3yZFMqoqHm9g_S1FYGZ1Ac9PVShR6_gY4BRyAl7WQ7tQjVvZRoER3Rl_l5q6sHsEiIquwRonvifh_40rddrevlXr5ntRouOL9pSixE4PcAKR1UdThUj6qr9qqxr2ZGmK6zd6RCePXFbGZcWI0yA4ookJTFlpsFnWk8Z7sDw9Tgcbbxqm751GOakzH91TAU_5v6x6l42WtI1P1eRNjwqj8i0zT0bAKdeoxqRuIuZV33Ziywt0j57VaK39DvcIE5Aet7gM6tU3o9GxtlBqGfiWufIhoRzL1oR2_lyCLdjklRpXiqUnfW_Z--Touepx92saz5Kx12PIj7QhdG_3u1vY91SGDKGdqZbRdPTmmo7BmdIH99slXa25nPnevyQi48-jf3KTEmFsS3MyO2EU1NJj2mXpLSN4xi3D7xX1nSiNWXGF6WN63B7uzbr3k-Ijrk8nAK2z1hsVfyJYgP3vMxA1CUz2oWP1yCMfMrOyHXlgBiYHatH19nODyPd9pu5ef8hILRdvog6esPmZJAkkteegz7JN1i_opjX10dxwElN4AkH1Fp2BN9r_GZmZBHjFSUURsIboP8jG8WUchJdDzzuh-QqbOQn13qJJvvnnug7WJpIhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز مراسم ادای احترام شخصیت‌های خارجی به آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665790" target="_blank">📅 07:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665789">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1K-a4r2eaAfQiF-zg9Qbt4FX5eSVC8pY_-ctwlR0P71U8TjSJOT7iK8GyKMjRunsmaktIZ5MT6149UNxxsZNEnNZoiPlR02nc-FV3O6P3KG4OYi7yXUrd_LQ6tQEmHFN1m2eYZySobrdVek5DtMM7qYPNFMpwPAI6Og6gwlpXy2_mdUO85R8quaHKrJBbkk8-XacojkyMykVRq8-727gwfamaWQEhTNXOLRakY0_js2F0ZJGUeggKs1otOxGWSu5gye0_tj51VlctvamjbNqnHC4Ngw4uGDWVUEofhxb7eH48FcOGgdVpvKpTI4qPZARXV804JK_pOtyirtC7D23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۲ تیر ماه
۱۸ محرم ۱۴۴۸
۳ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/665789" target="_blank">📅 07:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665788">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvheAHAc30ZSndG-jwv2to63jcucdC46pQQjLirxzZlNBkMHebqGuNsHOSkb7ngTIURBaxWFQ_FQ_5rDCUvwYtetMcjiJDBVkA1mt-DVGN2cAi16E4ie1RzX_yiKYW9idLu3D2MedgAq8tvTyai9NiovoDI4atJAwhbsRKAmj45Ie_io9KKllMXk-yOv6qqXOzkXsvja2LWwvm27A3k1-vYJjlSaCBMb2oljAIBAH0bsbpvpzVTdYwtOBeqNnfzuWwOLx1bOVpGpWpRpA9jODmeHMhTmav-enYlIJeWWfRrdE_QSRaCodjhCmU_szySdYuj_2fiGpRJZd33D4ebDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
سرمایه‌های کوچک، پروژه‌های بزرگ
هر پروژه بزرگ، از کنار هم قرار گرفتن قدم‌های کوچک آغاز می‌شود؛ کرادفاندینگ فرصتی برای مشارکت در طرح‌های سرمایه‌گذاری منتخب است.
🔰
شروع با سرمایه‌های خرد
🔰
مشارکت در فرصت‌های سرمایه‌گذاری
🔰
انتخاب آگاهانه با کارینکس
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#کرادفاندینگ
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
کانال فرصت‌ها
|
لینکدین
|
تلگرام
|
وبسایت</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/665788" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665787">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCAkCwB-uaJZ__BlqhhF-xxyB5d-UtBvKUht-VuhDTMOolfvOWKNTuTowxKTqMA0xfLzkB_Jg6uwj8ig1iBEBGtDvfL4_NJqCawUwXCf-3GFevdlR7H2BxAZMvROmpBoXlKsFMsbHQO2TJkMVjLL8ou1T9hkU1ZP7iJHH24HvgKhkRLnq2yuwqFyUfhWmdjiNEqElsQmJpnh6CZQPuBU2gkTqO3peS3wNkglg7HFZm8m3IMFrHihhkLomPN_nqZzNVmPga_eDYdRraT_CV884WUOa-VhtoNPNS2rD56OveiNZF60QdYPuw7o2_1mNqS1HLKwRjB1b2FH5Dp2Oy4llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی؟
🔴
تریدری ولی همش استرس اینو داری ضرر کنی؟
🔴
یا کلا ترید بلد نیستی ولی میخوای سود دلاری داشته باشی؟
هوش مصنوعی TimeTrade این مشکلاتو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و به صورت live و روزانه درامد دلاری داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/665787" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4VNXjqivyRyijTDumWMyzHTWD7S4bWHij8y1R7vgWA28BVTRz9kJ6ByTQtNPIl24cME9us66-ebC5YIBFwqxgNEMOpVBIKssWmiaC_jDMm6NcfOwc7ZZ6_zRmxDWug50OGlb0gDnG7yYUAY60G1UQ0WysQAKaGb9t-qOLJKUtJUhBDgM46bVAGPkY6A49WVCkhY3bzBAM4VuG2gQhL4o8EjfAl7qxMTy97wVN-QNAvOIBQMjq5ykSY_bPYk6Eqsn2UTfWINbT9oMIRSj1JAwqKqO7bwg42FMiEXYavgxA1lX-mO09KPP8NZn_Jf_qB_2eYT4kj9E5l1PWk9t6BtGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙️
بسیاری از کسب‌وکارها مشکل محصول ندارند.
مشکل این است که صدایشان به افرادی که باید بشنوند، نمی‌رسد.
بهترین خدمات، زمانی ارزش واقعی پیدا می‌کنند که دیده شوند.
محتوا شروع مسیر است،
اما دیده شدن، مقصد آن است.
دست رسی به گسترده ترین شبکه انتشار کشوری(کلیک کنید)
#DigitalCast
#MediaAgency
مشاوره و تحلیل رایگان
👇
@marketing_mn</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/665786" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec6ffec7cf.mp4?token=eijocKIwnfCjvnPCzMzdOLTp0hHeHdmD3tAOnKwKcSpH5n-_0duu3gVQfqLgcP7pDcRwdqVtyoZfU86VMafovLOb3flqHHOK6DVrAHuT95la27NSZ6TF0nfQqvmG044vgm_p-OmJuzcCxz1nGQ8uU7586fAITkxF99trrgwRXwZn6FRmSt0o9MqvOtXGqB-BP7kkg313CT5_Qqm5LXxoYhH_CsXZw6MpGhlOTH28DQxTjEuuMf8GCfORKF5E2YEOlmaXAPupYs_G7yce0X7e67Qrng7iYmAi18ZE0_oqCxCEtDeOd4BQf-AGemKQL0kK6Ppvahm_PNa_Ru0JkQSdTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec6ffec7cf.mp4?token=eijocKIwnfCjvnPCzMzdOLTp0hHeHdmD3tAOnKwKcSpH5n-_0duu3gVQfqLgcP7pDcRwdqVtyoZfU86VMafovLOb3flqHHOK6DVrAHuT95la27NSZ6TF0nfQqvmG044vgm_p-OmJuzcCxz1nGQ8uU7586fAITkxF99trrgwRXwZn6FRmSt0o9MqvOtXGqB-BP7kkg313CT5_Qqm5LXxoYhH_CsXZw6MpGhlOTH28DQxTjEuuMf8GCfORKF5E2YEOlmaXAPupYs_G7yce0X7e67Qrng7iYmAi18ZE0_oqCxCEtDeOd4BQf-AGemKQL0kK6Ppvahm_PNa_Ru0JkQSdTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترک اعتیاد (مواد و سیگار) در ۵ روز
🏆
🟢
بدون بازگشت
🟢
بدون بستری شدن
🟢
بدون درد و خماری
🟢
بدون عوارض و وابستگی
یک بار اقدام کن تو پاکی بمون
✅
جهت مشاوره رایگان، پیام بدید
👇
☎️
09388403141
☎️
09388403141
لینک دریافت اطلاعات شما برای مشاوره
👇
https://survey.porsline.ir/s/uic3tg60
https://survey.porsline.ir/s/uic3tg60
لینک کانال ما در ایتا
👇
https://eitaa.com/joinchat/3149399356C76d980ac27</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/665785" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16002524fe.mp4?token=PSLJj9SGj0kRxf4AB95c2f-FwzY2ThdoKns6mxSJWZR38E9X5w6ChsRJkCVHSAzrAfvDbNqeqsRddnd6PVJDuhzujxISiOFGSrvP5iMevl8fjPod2dbLyABw82lHMSy7em3s1_lgZZDbTE0Y0eGGvDKBg9SAnhAE-U3sQh3ozySUBujPEY59Swj-kBEtsFFpfZia2f5NLluztycp1WxP_VDim__JAmeXCr5C9WVKaT8BOQ5f1EbzRu349KPgiNtoshUQbMLSjuz0kHNuZ1vsWGOQ66CuFIOGtUGDz8vMGZLgFSnzjlsVt61mUt63d-xJOBd4HRDbtVfeYnA507hw4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16002524fe.mp4?token=PSLJj9SGj0kRxf4AB95c2f-FwzY2ThdoKns6mxSJWZR38E9X5w6ChsRJkCVHSAzrAfvDbNqeqsRddnd6PVJDuhzujxISiOFGSrvP5iMevl8fjPod2dbLyABw82lHMSy7em3s1_lgZZDbTE0Y0eGGvDKBg9SAnhAE-U3sQh3ozySUBujPEY59Swj-kBEtsFFpfZia2f5NLluztycp1WxP_VDim__JAmeXCr5C9WVKaT8BOQ5f1EbzRu349KPgiNtoshUQbMLSjuz0kHNuZ1vsWGOQ66CuFIOGtUGDz8vMGZLgFSnzjlsVt61mUt63d-xJOBd4HRDbtVfeYnA507hw4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی جنگنده‌های صهیونیستی به جنوب لبنان
🔹
منابع خبری از حمله هوایی جنگنده‌های صهیونیستی به شهرک صدیقین در جنوب لبنان گزارش دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/665784" target="_blank">📅 01:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665783">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
لحظاتی از وداع مردم با پیکر امام شهید انقلاب در جوار حسینیه امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/665783" target="_blank">📅 01:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665782">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای ترامپ: ما موفق شدیم ۲۲ نفتکش غول‌پیکر را در یک شب، تحت محافظت شدید و با سکوت رادیویی کامل، خارج کنیم  رئیس‌جمهور آمریکا: امریکا هفتۀ گذشته سیستم راداری جدید ایران را از کار انداخته و تهران در حال حاضر فاقد شبکۀ راداری است./ خبرفوری #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/665782" target="_blank">📅 01:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای ترامپ: به دنبال تغییر رژیم در ایران نیستم، بلکه هدفم جلوگیری از دستیابی این کشور به سلاح هسته‌ای است/ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/665781" target="_blank">📅 01:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
باید تقاص پس بدهند آن حرامیان
ننگ بر ما اگر از خونت گذر کنیم
🔹
مراسم وداع با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره)
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/665780" target="_blank">📅 01:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw8XQrvSwRz1kocCZK1u-im6EsZmX5ts8lmHJoeVtkDXBmTP23y5KC3Sr4Lsa-xC_d__Qic2_bBWAq6UXtmwPdvKOfj_x6P8EVZ12Z3Z5ReXZGC9kf9t5kAPUe6WZcmg6p7dBTjlC4udp4TpG-60R9gvUz7ZmRPZWvPjnIOmAQ2LKi9LuEnJGnLxYuufO97757tyf0fyVwtdGFpoyzVjGmC1zE6F2Jpvr9Ld1_YZ802YKGSkn4fG_CRfJznfcsMKkyMD5j1lby3pFfQq6dQvM-V5Avyue8_mnAXtERpBNx0gA93YJb-k2MS4UjD1jA4v6kNMCV8v_hM3POm0W-aXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: شهادت رهبر عظیم‌الشأن ایران، اندوهی عمیق بر دل آحاد ملت ما، امت اسلامی و همه آزادگان جهان نشاند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/665779" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای ترامپ: به دنبال تغییر رژیم در ایران نیستم، بلکه هدفم جلوگیری از دستیابی این کشور به سلاح هسته‌ای است/ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/665778" target="_blank">📅 01:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79ff51089.mp4?token=JXVryjrhzRQbnmbc2cqDJ_l0OdbONzq6M1Y7slmJK5bfYF9pNWzSobykM3O6tRM4PlDWBojYxNG1y2hkvRypEzdZwEGzP-o_d91RsVKFjLhu8V0ob1etIZieG6ycudi3OW4cZVUoB5GuhqCs1jlGX4iXaybHDOkTYMhpyY_o64pn9-H0NE962HwIG6tp4T4UYGzv1yxLLxI32vS3CTfgGkbBipbVQzh8pERdJRDLeKTbCpzvlSD8Vr9CSgg-Y1ddG1w1DnqwI1Xk_jZpUjvOdjOlN_kilrgDujvrOLIYTqqpMrH-lBdBKw39hiQKXJvEtE8qTw0_nsNrqtcPklrYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79ff51089.mp4?token=JXVryjrhzRQbnmbc2cqDJ_l0OdbONzq6M1Y7slmJK5bfYF9pNWzSobykM3O6tRM4PlDWBojYxNG1y2hkvRypEzdZwEGzP-o_d91RsVKFjLhu8V0ob1etIZieG6ycudi3OW4cZVUoB5GuhqCs1jlGX4iXaybHDOkTYMhpyY_o64pn9-H0NE962HwIG6tp4T4UYGzv1yxLLxI32vS3CTfgGkbBipbVQzh8pERdJRDLeKTbCpzvlSD8Vr9CSgg-Y1ddG1w1DnqwI1Xk_jZpUjvOdjOlN_kilrgDujvrOLIYTqqpMrH-lBdBKw39hiQKXJvEtE8qTw0_nsNrqtcPklrYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ متوهم: ایران را نظامی شکست دادیم/ خبرفوری
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/665777" target="_blank">📅 01:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ترامپ متوهم: تقابل با ایران، عملیات خلع سلاح است نه جنگ
دونالد ترامپ در گفتگو با شبکه CNBC:
🔹
تقابل با ایران را نه جنگ، بلکه عملیاتی برای خلع سلاح هسته‌ای توصیف کرد؛ وی با تأکید بر اینکه دستیابی ایران به سلاح هسته‌ای غیرممکن است، گفت ۴ ماه است که هدایت تلاش‌ها برای خلع سلاح این کشور را بر عهده دارد./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/665776" target="_blank">📅 01:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbe1af175.mp4?token=ZcLNJCaqsmpAwPNZjzBdINqkkaRmw8l2MtlEGexACiQ26m3OdVy8umPwC3Iasw1kZgWa1Y0thXVWHmvCBg2AB_HxqXBgh5hZz2BgztDtlvC18ywKUQdW2KlBvHJ-jMWI78XvbIPU2UeTflH8iBTGXA9W8kPRICpOSqhCypwS3TFiO2owdHndRx2kCmKTf4f9D5fRFVCBd-zI6J9diPnupQPp7YjF0KK2FaHu_EUZMtVy4ktIqEKW_TLvHgoFsIiRwJV09EQZkx1Q_t2fmOOYypRpvlGVm-RFeRZdCTO2tNDowD5A_U7r4OHR-XMbdz42TTwfR3fDvh713uZ4TnKkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbe1af175.mp4?token=ZcLNJCaqsmpAwPNZjzBdINqkkaRmw8l2MtlEGexACiQ26m3OdVy8umPwC3Iasw1kZgWa1Y0thXVWHmvCBg2AB_HxqXBgh5hZz2BgztDtlvC18ywKUQdW2KlBvHJ-jMWI78XvbIPU2UeTflH8iBTGXA9W8kPRICpOSqhCypwS3TFiO2owdHndRx2kCmKTf4f9D5fRFVCBd-zI6J9diPnupQPp7YjF0KK2FaHu_EUZMtVy4ktIqEKW_TLvHgoFsIiRwJV09EQZkx1Q_t2fmOOYypRpvlGVm-RFeRZdCTO2tNDowD5A_U7r4OHR-XMbdz42TTwfR3fDvh713uZ4TnKkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: برای جلوگیری از سلطه چین و دیگر رقبا، آمریکا باید در بازار رمزارزها پیشتاز باشد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/665775" target="_blank">📅 01:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox51ZfYaA2NuSNnIpax09cqdQxfkv1t6Y-1fatR7h7jt-sYlmo5ZmNzhfAjJCzrTezbtpmMcjE5Cw2hhHcI-RNcAWO0a7OWggGTaMVlJ7eLsQ5RzyJkDm4bpRKn4SmtC-2M8dQ7B-mJ1t3NbWz2gX2hnTEh3QQ9xKt1ZiM8cN9M36tx59v6ZDuyh17EZmQK6m8z-L1xQjntx3vjTPHkoPFKpgdZeTYCI69WJbyC09lMuLwsb8lL2Uovcadya3cxY5-XqxBil4srz3dTk9rTw4IM_WjCFKks78JJaMhVQ3UmgHeUf3X9wq-KxDb4avb622hYmR2SenFILqzqfGzBNsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یحیی ابوزکریا: آیت‌الله خامنه‌ای میراث‌دار عزت و مقاومت مسلمانان بود
🔹
این متفکر الجزایری، آیت‌الله خامنه‌ای را رهبری کم‌نظیر در تاریخ معاصر خواند که با وقف عمر خود برای اسلام، راه عزت و مقابله با ظلم جهانی را به عنوان میراثی جاودان برای مسلمانان به یادگار گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/665774" target="_blank">📅 01:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665773">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
هتل‌های تهران هفته آینده نیم‌بها می‌شوند  جامعه هتل‌داران تهران:
🔹
تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/665773" target="_blank">📅 01:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665772">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngedKiNnm-fLLzDGuiovh1gLii6BEmCAU8xNARPGLnW78Ih7sadDt0L6vD14EvhGkKIAUf78O5CpgMFgXH8nMtKENPSNiJUNEfRWXEnNtKfnborQY0gpUeLXokz756dOgfRPMjpJAWNMXpsmcaRHAy7fNS0TRQrQ5RSc8nQm_8OLr-Fn0GTfZcHE5ACzK04aC3agkX_0sdM2d2FTiKksoPdMhzbeUUa2rc_sxWP5W9dHfOryNv796nulmOTEABPhLx-fuw39woPzgNGoi7GdiRaxRatKVPN3VlbE27vMVFLPp-2rsdD2QPG3aOIZQC67EQdyBHVYT85aHmYlGV2j8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله قایق‌های جنگی اسرائیل به سواحل غزه
🔹
منابع فلسطینی از آغاز موج جدیدی از حملات دریایی و گلوله‌باران گسترده سواحل شهر غزه توسط قایق‌های جنگی اسرائیل خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/665772" target="_blank">📅 00:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665771">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/665771" target="_blank">📅 00:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665770">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397157b218.mp4?token=PvyZ_U5UQGGHuEPg4o4eIGbHpV_Owi6tcioWH91KS418MxDUO6O8gWZm2O7rvm3tj-8DRp4QnF1I-Y8AUfC_ze5YHVB7bOAUUzdimY1SeyllphvAPwwgrcAAzTmJWPttXEMPxU63VYcl0jHxAAHCNywI7f7UYVSpjqLuuNeXlm3T8AH94MVHi1ZcbLWUphjlR_m24rE1RzW8Nx810zBedWR7kPF6aMOrK8IhetLHdhVV7S__0um0Fk9Cx7zuTDxdP_0tc1rexKgpHGCaOgx24uAuP_Qcc-7bEKtTMUQMXZSJaxgX1rDaAvXG2qU2pdRTaL7oVyZF6UdoZmzeKNdw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397157b218.mp4?token=PvyZ_U5UQGGHuEPg4o4eIGbHpV_Owi6tcioWH91KS418MxDUO6O8gWZm2O7rvm3tj-8DRp4QnF1I-Y8AUfC_ze5YHVB7bOAUUzdimY1SeyllphvAPwwgrcAAzTmJWPttXEMPxU63VYcl0jHxAAHCNywI7f7UYVSpjqLuuNeXlm3T8AH94MVHi1ZcbLWUphjlR_m24rE1RzW8Nx810zBedWR7kPF6aMOrK8IhetLHdhVV7S__0um0Fk9Cx7zuTDxdP_0tc1rexKgpHGCaOgx24uAuP_Qcc-7bEKtTMUQMXZSJaxgX1rDaAvXG2qU2pdRTaL7oVyZF6UdoZmzeKNdw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌ مسلحانه در السویداء سوریه
🔹
منابع خبری از وقوع درگیری‌های سنگین میان شبه‌نظامیان دروز و نیروهای امنیتی حکومت جولانی در شهر السویداء در جنوب سوریه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/665770" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665769">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQsnzImZFJ8u2fqWDLKZPstzOiFsNijRjoJu276sUjc0gq-nvWtRlOC2rnkUrQbmsxluV0fuiQx9qK4xVf4WfO8uqt1k1UA8kV7y19hQ6P5601AKND0otLtg15s_9cM6Ry7NWWxKF30kX1u6EJ_QLnzXNYERNvNlR440u78UNSJ8d1z8kBUuyopfDE__HrcKZTbAtksFCNRWL2x3UBhIgkLa5ZMji6qJFjthg0r-a0Hcpf2wBVRO2De-De_g0xEp79jsOnQSAJTfU9w4hElp0A10qXn_Jw0q8TcrKUlUbasOb94mcYsKxRWegF4rTygrw4v0N57qjfIotIndpUbaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: شهادت رهبر انقلاب، نماد تداوم دشمنی آمریکا و ایستادگی ملت ایران است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/665769" target="_blank">📅 00:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665768">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdbTqIektWvdOlDdppdspVsFAmDto0HjLJhnJj58th7WwA3-Iu5hmiB9NmRv7CWkGd5wP85pRZPnCpNSsehWtq-C7YzUea0GKQodT_l1nS-ItBBIqPydsSP6z1IKdzdTKqdMZrwrb6NUml13kXmjEY_DUKSoLAMAblA6sPZHAFK40tPi6gcpl3As7CLu9p4nxYaT5Fyd1C4-NaQfdaO1poS4EPYmYwGWfVyfHAWlHi9qPleRljwGx2tzzV95VVZcYUpHXOXo-8TbCQ7OFitTmqDeiLwTsaQjIdFcrXXQ_UW6sMcjYCqSmrKfPwbxR5rJA9nJmrM51JDNWbAMFl2NUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسدودسازی حساب افشاگر معاملات مالی ترامپ در ایکس
🔹
ایکس حساب افشاگر سبد سرمایه‌گذاری ترامپ را تنها ۲۴ ساعت پس از فعالیت و جذب ۸۰ هزار دنبال‌کننده، بدون توضیح مسدود کرد.
🔹
این صفحه جزئیات گزارش مالی ۲۰۲۵ ترامپ، شامل درآمد ۲.۲ میلیارد دلاری (از جمله کسب ۱ میلیارد دلار از رمزارزها) را منتشر کرده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/665768" target="_blank">📅 00:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665767">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f53a3d8358.mp4?token=ZTUW0zzrFHy2mHLog7S49kBAljgrrseP6orLTKc4s0wCjo8egbrjvs3DsQnWXfT83sl_b_06GOd4bSFOAraizJz2DJotrUkvj1B4DaC-mOaDINWAGcJ53N6CAvh-DbzTEH_WFI6rEgoRxwfP0X-_pYN5pCmY8aHor0jEOqphVYWViAM8bZJS_MAIH1A__t9ApocKpXSh7CXSCfnIQLm0rqzfnzHueZ5rBfmh7el1ooUmwbKiNxkWr5kv_rVJKuGxwV7_hRnHQlljYPX3qziPFm_HfDNX3RLVvHKqvSaP6nslH-d4_Q1ov45QoMm0j1-D4kXIJGfbyY9o0B1ARlvPkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f53a3d8358.mp4?token=ZTUW0zzrFHy2mHLog7S49kBAljgrrseP6orLTKc4s0wCjo8egbrjvs3DsQnWXfT83sl_b_06GOd4bSFOAraizJz2DJotrUkvj1B4DaC-mOaDINWAGcJ53N6CAvh-DbzTEH_WFI6rEgoRxwfP0X-_pYN5pCmY8aHor0jEOqphVYWViAM8bZJS_MAIH1A__t9ApocKpXSh7CXSCfnIQLm0rqzfnzHueZ5rBfmh7el1ooUmwbKiNxkWr5kv_rVJKuGxwV7_hRnHQlljYPX3qziPFm_HfDNX3RLVvHKqvSaP6nslH-d4_Q1ov45QoMm0j1-D4kXIJGfbyY9o0B1ARlvPkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم اسپانیا به اتریش؛دبل اویارزابال در دقیقه ۸۹
🇪🇸
3️⃣
🏆
0️⃣
🇦🇹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/665767" target="_blank">📅 00:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnzVTBGYDEgdDhp5S2CXwJmxuwVU3AtAF8tY_xFg3a1QIE4thoClrqp4PHFVYCT51GtjsTo26rHUji4B40JFXGVGXz5l1WB7L4K53jkP7dKzC7-FcXfQ-CTbbgi8vSp3mJX80D3YG7NSx7POzPVkAxVWNMIQ8Z1SHqr7tSAr8RSdMoIbsYT4Y-UyLfUDFtpTyM699i4TIY09rmB_V7y1qzjEQj-OvxE7TnO3qGILW8vTmpQhJ8SIiDtWJFjtion4GWsLnA8vR_TWbjYNeTIUoBWnvSsedCdpW6uWO0ZKzjG0xn7qbEzklossRL7ZAaTbwR7momAmfT69HdMu7hsn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYyq1s5qOgVI2MzPm0xfGyI9YiLaLy8vPYNUOVf5AQ5wnLAI2maXjGRKkTToGlCChFeovN1QLEEtid0K12GU1yKp_6Q4kqSa8p1kYP9NvusxOP6tC1VsGC6k4czjSWl0VVicKU9wP_0DFP19NhjEpMNPEJK7qo8uM-xV7-Cagw4el_SjSj1ZONWElxvEXs9FDuY5sj5zXznFi2CjCugJrPyzaGpbHjhvkKkfH20dido7RnIUUBwGQ5Fnkw3c4piNyj2PejwfR2WVkW9LJnzEyl_WkSHndChvRkbQpqAY7kqmZKcjZYS8AS_R0YWXWyKTMKkqCuXoARE4M0DdRotJBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سردار وحیدی در مراسم وداع با پیکر مطهر قائد شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/665765" target="_blank">📅 00:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8435478b2d.mp4?token=j4G1y4C1UNQ4xLM6In7f--LNCnGBT03o-1-QGhy87awHV3V4HxRXH8vU7aCgI1XjaAqkchPeM1lyoYEnu8krq6qTk-iGxIvYdfIosfpmOoqxiLVI3oUhbQi-i7n9xWej3NGEl3m_TOp2rnkchrygVqmDs7kLntPoCGDR8NJsLWXjpv3I01O4qdTSSmCWcQFAgowW3tAFa0xhNIvdBPC6NSzHQNOyywYIAlWkO_h67dsFvnPG2yhljhaOIBKaUn8kbXhrT8p17CSUx_EVcqtIV8AI06IszX7TX5diQHIIQaDrDgoys4VM_Zx2ZBq8qSPZewL-iNLApSVElbamOuMFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8435478b2d.mp4?token=j4G1y4C1UNQ4xLM6In7f--LNCnGBT03o-1-QGhy87awHV3V4HxRXH8vU7aCgI1XjaAqkchPeM1lyoYEnu8krq6qTk-iGxIvYdfIosfpmOoqxiLVI3oUhbQi-i7n9xWej3NGEl3m_TOp2rnkchrygVqmDs7kLntPoCGDR8NJsLWXjpv3I01O4qdTSSmCWcQFAgowW3tAFa0xhNIvdBPC6NSzHQNOyywYIAlWkO_h67dsFvnPG2yhljhaOIBKaUn8kbXhrT8p17CSUx_EVcqtIV8AI06IszX7TX5diQHIIQaDrDgoys4VM_Zx2ZBq8qSPZewL-iNLApSVElbamOuMFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیست به شهرک «بیت‌ریما»
🔹
منابع محلی از یورش گسترده نیروهای ارتش رژیم صهیونیستی به شهرک «بیت‌ریما» در شمال غربی رام‌الله واقع در کرانه باختری خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/665764" target="_blank">📅 00:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بخش سوم - روضه (نمیشه باورم که وقت رفتنه)</div>
  <div class="tg-doc-extra">حاج محمود کریمی</div>
</div>
<a href="https://t.me/akhbarefori/665763" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نمیشه باورم...
🖤
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/665763" target="_blank">📅 00:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNnmCjvr39WaoEkVPT0eHXkzsj-REi_l_SHFAAA-dbp4VpVhPmwRIAm8JCs6SghlQ73nOiizgOf9CCBYVfOoru-BvY6FmzCkrTzHIzoiTQ0e57PleYSslF2WFJk1fB2sr7rKuJdabPoA2bqKT4inHuyy-BoO-IpViAa_giLG0CzzllPb725mm6GxzUpIF1t2bBYDeysBVhvBNcLEznXv8jYJwjTy9nb6okFhDitLHAixsCsNUH43hRrO1nMl3XetOHkcfABCXu1JUw29A_xo628_IRHQ6YSIPu_Sa8ZFul3sn2IygsJ7sYrmqAXILUB8Gr3RpTS5h6SGE_iFGkylNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2oVPo-xkRIzqZH0VGg12sTrB4Jxv4LUAAoUN0v7-HOloOdtq0Z9CWS3jgoAQ44BbJFsDtpxlz5HMBRwbiFMGGzGVbHUYT3OwlFKpv6sXyfTJ97qQZgpO6UntzAd2F3vr8ZPiUKJtQBeiqxsA-6H3YpPOgbZbozmOZU_85DGmKCHMbQVj2pftuzjWwCifuLbzcnM2zpnyIh9oKTmTiLCSvTfrRnYJvqgPV3b_tJq85Q2mwFx43If067kUbCNuA805ZKVymLqO8p0PSMV65QsnnKG8UmlPs-l4NAW-Fmqdu_OHipx4UNdNZwAO8fGisRSP0dmBMr3-IhmpNpN343QCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdrkVxuj-WHh1u9bSFzKKkRXEiWcknVfXhrM0YEzqbyP6PelzWcJ7LgAmjl21jp7F7Dc-HTr2zV0dvsy7GfPZKq_yl_jTRkmmHbRnQQ5M1qbWUu3S_r6GNdsEseWAJCh6pqF_7YfnFyo8cXal5HekWty95mtgtj110Z58ddHx4lVBNYGqRGQm1jZi9BESgSTI2iZzl1eYFFLuxpgurSI5654c3UgcvnWkhU0hoPHmY-p2uv5rxX4Tqw9JrLdxvl7C2S-lSkOsxKOHYcAAZYpsL62wFHFf4aSQm_TdhIKO4sSy0Ag-lhZoRs9MmdnZbF9m_HhnY00_AVIDauwnVjpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVQopyXOlPTo4qSMnzCCCXhstoSC2JF7e0dU8Sv0y4ilMsqboAlRGqjJgHUk4oo_aceL1z4-0Ku3l-pWiQHJQAYHSyfCHiReb37kQt2iDK1iAzC91U056og27m94GIqnmbSJp5McmPqUWEBMUwJPsKe-p_nQF6uVasHoMYpmtLLeRfiTpx6LOuP5v4P3BNAFjsLtQRrVnbC7URT21RsrVR7ddHRGVfll7fbhtGLpyVap3yUBUPFWElvvHGR4QsRnQl5e8bAsw9SJGrAtWVpDJcARGHvQeC2s6JFcJmNj65bS57MlkmpwnHiiUQb3xVSxNFC_HueHZBtMVRnNsuQ5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uinePd-g_Ie2Zl_ys5SIRKvYsC1M-JWJkAZ8VgjDgoxGomeHfccY6SAi-peo-v4pyYGaawyJKEK2q-VUfr9NFOUDYCKU_J05thyvuTexxMq04xQybTuEEwtGWuIDa76syy3pFO7aMwzExnRgUQw9OOVndvQHatUymAbkx8A7HTL1m6ktF2ibdbXX2BlnEvuVu8jnN8nqZ0ZHaeugiovHYQuviR5UY6TpdzPZmoL_Qxfbavr599YXw8XhmNPfPXNDpXMSHIw7ZAUpUogtGLziWAfFpYJNsOG4P3bUe90kE6YXyMAA2Nsb9IYrdllzt7KLTArQiUY6ZaH1931viXe9Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ توصیه راهبردی رهبر شهید انقلاب به دانشجویان
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/665758" target="_blank">📅 00:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba79e01e9a.mp4?token=CcGf4JccHV-qs6wEztsykK1ONbBStA846ny7l9QkHgY7vQAaPYXTRqz0cFrpM8VP_NbvBv-daVWVnJFX_eVVp4s6npBMAvZ4FhGhDbinPOxMHqvyB3V75r7XdGw_y4HmqFT4FA6b8hSwRL4G88lACpOZ9MdZGAZicd1t4aTxal3ZdLXMnzbOfblPkvpbSNHDph1g0sDkDvJIMzANCrG0gX54cxXDzgGUX3rTYr9_edsm6hpCW4PTyknCJGgduYtJ2fec8WV1pajGWaMaH0Mw2gj1Y7rHHMLBDvjcSDiR55ndNme9mstMl1msT3RYNNitVgqKoxfynDuKN9z4pBrv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba79e01e9a.mp4?token=CcGf4JccHV-qs6wEztsykK1ONbBStA846ny7l9QkHgY7vQAaPYXTRqz0cFrpM8VP_NbvBv-daVWVnJFX_eVVp4s6npBMAvZ4FhGhDbinPOxMHqvyB3V75r7XdGw_y4HmqFT4FA6b8hSwRL4G88lACpOZ9MdZGAZicd1t4aTxal3ZdLXMnzbOfblPkvpbSNHDph1g0sDkDvJIMzANCrG0gX54cxXDzgGUX3rTYr9_edsm6hpCW4PTyknCJGgduYtJ2fec8WV1pajGWaMaH0Mw2gj1Y7rHHMLBDvjcSDiR55ndNme9mstMl1msT3RYNNitVgqKoxfynDuKN9z4pBrv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم اسپانیا به اتریش توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇦🇹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/665757" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
کشته‌های گرمایی در اروپا از ۲۱۲۹ نفر گذشت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/665756" target="_blank">📅 00:01 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
