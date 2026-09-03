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
<img src="https://cdn4.telesco.pe/file/CJKez4UFnzyEdCrmiybPJqZVvF7eUVfFXZHlkfo7pUAAGHmiMOIICndFs2IuMVihonSOUuEBcugtUZJO8sdBBJMo5dr-a8Nctx90xk85oPQjnkztZKXnJd3WvBbJzzO-2d2HsuyUVNfAfu3mPSWNHMST-WL4rOdnyRV6OhPe9eEktQxJHMp2_HPr-4wUwAz7GY7nE0No9yeqbjKatPlZnDFm13XhiOeCmL_Yc4C9sOJuY2q99b5wAhufjf6jgOLzZBfXsH85r-nimJ83Suk1SO8i7WhwbYgNeRTViqEyFs2FDG2lghmhdvSwdzj7oi-E7JnYYvvNHJYFqJQ0wKCoqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/20503" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آزمون های  pte و mcq  هم بعد از تافل و GRE برای ایرانیان مقیم ایران لغو شدند.</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/20502" target="_blank">📅 11:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SBoxxx/20501" target="_blank">📅 11:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟  افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.   اما اگر رشد نرخ‌ها از نگرانی درباره…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/20500" target="_blank">📅 11:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjUcP8PqE81kNu_H0SD99-UdKtuh4ERIBcyR8A0kdA28Ed3RSIJMNyh0TWO_iMT4W9i7KpQZ0us3Bmce3UOkJ5RcTIMv9UJAZl3keXr625p5N9XT1I2Xqq-YI7Mi4sbXPtFif6Ptz0uWisdK7rZHDV0Oq7Pc-QtOig9L2C1KthGnbrhXhqRQkH1br9vf84VYohLfLGmvjsT16MM392HDz5cXzYitNb1S5J1TcM5CmH5yj2_YO278NgVqHxfOcDuLNoy0v3L1AvUgubFwNFheOE7bu3eDb4bnLPdp5-_oVdsbvnR5SDVe0MOGzd4qKVszuwb5XikOSAEIHTRw7tR7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/20499" target="_blank">📅 11:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWRfz47hrY3cbsy3b-FmW9qrxlHEE2ggkRED4iUv2rWtPk79ROJPPtokM_pLstzAqCGYzejDeCcsOmHvr6JpHKCyfTRLdYGJ9EHxNUxqoO53GXvgDJZxGtz-bXCYIDoYVrmQiHT4kHJZm_ch9Tyq1-yv2vivgIBU9KngMnNOlc7ZMBfW1ky79YIOzT7zXzUHtZIRyiKjAkaGchpvLTXi83WCiwvmsHVagVyTLSMna6q7a9YvGrHVCHmvcR8TKC3G6DVWcTxq_OC5g-KmPEF7s22a-NVbuSxBz10R2sbP_e6sbRNwFyfiK47GvYMDQQ9ANzBQci3ewuCZJym0L28yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نرخ بازدهی اوراق آمریکا در آستانه ۵ درصد؛ بازارها آماده یک شوک نرخ بهره می‌شوند؟
افزایش بازدهی اوراق ۱۰ساله آمریکا به محدوده ۵٪ می‌تواند فشار مضاعفی بر سهام، طلا و دارایی‌های پرریسک وارد کند و هم‌زمان دلار را تقویت کند.
اما اگر رشد نرخ‌ها از نگرانی درباره کسری بودجه و پایداری بدهی آمریکا ناشی شود، معادله می‌تواند تغییر کند؛ طلا به‌عنوان پناهگاه امن تقویت شده و بازارها با ریسک بازقیمت‌گذاری گسترده مواجه می‌شوند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/20498" target="_blank">📅 11:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf2OSRw8ZOResD8QYPRHshkCHv2Z8iJAfHHjWmVtelMZKBmvUA0Co6TLhkiuOsQd_JFQHBBOJqjxMvdcmpgvzB2shAuM2Azy3bVbz7nUaZcSeNyBO4I05JRtZKlGhroA3kGI0PMs89-GzHTjQDzjYlNT17v8Pd6Vj_eAjhl4P9vmwFudMEaMQnGoN_qHXHX2Bmgz7aURhtyKSYS2srymvhUt8siKeuqXquI1ayD7rhsuciWP-IokLuoS425_heXT6Ga2txNkuX_EKwFps_GVvWG5GYm27ATlvVatlA0Ej_yUrlc7Ejkl7Y7Ws5MljEJ4IP5CJcip7Cr4EP46y-pqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد و پیش بینی می شود دستکم تا 4385 شاهد افت قیمت باشیم.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/20497" target="_blank">📅 10:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1aZcqqfhN1WeCZEHlzvST9jpDS32rJJK8jBUZdWMG2UMYdOpRFu-Yp1w0aq0enk6o5_dt-Rzyaf4M-Iq9hXcPkpnGN2pSQX1hrGTSG1GGxf3q7NsBlRMN1JatjszGkwv-WFGNoJ3pGt2_PPl3isl-prwkirg_MjR778NGxM2By4POW-UGc2pVMhsJchfzoJwoUNmvMBIhnHK7RN_pHbIbOXpy_tb62HRArcjN_Vb88eTsRZy_mz5wAnsJPRtTPP2S--_KVFxMWSOSBfRjIzSXx3UM4HcUpHrQkUVf6gQOeHV0oG-wgJ41syz3JebeFP4OBUYP6zg3EquyE2pX-ps7WOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0447727037.mp4?token=CYgSB3bZrdBciu7FyVtZG5TnASum_fyVvf6T_biDUnIYd7ZvkIUZuxI2kwov8Ek54fTuHSH5lMmN5aqnghKkgeVfisN3cvctCRXY0v_QNHbL6fVQgKTBeejheOxFa-ydfyAa2bEvEUdFwiiZ6q7tWVfN-l5AAAzHlVqZIbkbkBAkrBGnVhrHCV9bZF3Xco2-bSxIFuC5PMeVXRfdDyMNokgopg3WxV50SUcRd3AzpY4Y-exU9ZAYoOA6vo068TnCIhwqDMgec2RUkktpykteOvDKbiIKaFk0Ry87TQJ6-IjV4I1OmyHsy6K4xBeL-9ZCcqLX4hJv7enV8MtdHub1aZcqqfhN1WeCZEHlzvST9jpDS32rJJK8jBUZdWMG2UMYdOpRFu-Yp1w0aq0enk6o5_dt-Rzyaf4M-Iq9hXcPkpnGN2pSQX1hrGTSG1GGxf3q7NsBlRMN1JatjszGkwv-WFGNoJ3pGt2_PPl3isl-prwkirg_MjR778NGxM2By4POW-UGc2pVMhsJchfzoJwoUNmvMBIhnHK7RN_pHbIbOXpy_tb62HRArcjN_Vb88eTsRZy_mz5wAnsJPRtTPP2S--_KVFxMWSOSBfRjIzSXx3UM4HcUpHrQkUVf6gQOeHV0oG-wgJ41syz3JebeFP4OBUYP6zg3EquyE2pX-ps7WOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف طولانی بنزین در مملکت دوست و برادر روسیه!</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/20496" target="_blank">📅 10:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکا در کویت!</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/20495" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twjNhn_3gCJ9UMlVUSpi1eURJYsL9HYoLWa4tSw6kdarqVLPyIpuZG45va0_nXSaQnbocbGgl-fnMSwno6Alr1L15aJF3dV_RYTB2bO1ggScF34LM5kmnIdlJSTsCEBSPtLvszS5AHfLObFofD9aJ5eMSeBDBZJXHK4N5_kUOiFUjE6vT_YILjx9i4QcyAbj3uMtGN90NJm9E76doX7VmS7wRN6-zJkGz1VQX_nQ1Kmc7jMmLlbA1Glr3WoeNGalxvm8cmrhA97nG_j4JKADg5eP1K4BpsXdqIJypnt-6FhjnXlEbl3Kr9xaVd4WXLO6JLrysElZEFSykEOBcZGktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20494" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20493" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انتشار اخباری از انفجار در میناب!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20492" target="_blank">📅 01:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جمهوری نظامی ایران.pdf</div>
  <div class="tg-doc-extra">257.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موسسه معتبر مطالعات جنگ (ISW) در
گزارشی
به میلیتاریزه شدن فضای رهبری کلان جمهوری اسلامی پس از جنگ اخیر پرداخته است که ترجمه این گزارش — با اندکی تغییرات اجباری — اینجا ارائه می شود.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20491" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش هایی دال بر پرتاب موشک از سوی سپاه</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20490" target="_blank">📅 01:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 دکترین «دفاع موزاییکی» توسط کدامیک از فرماندهان نظامی جمهوری اسلامی تدوین و تببین شد؟</h4>
<ul>
<li>✓ محسن رضایی</li>
<li>✓ محمدعلی جعفری</li>
<li>✓ رحیم صفوی</li>
<li>✓ احمد کاظمی</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20489" target="_blank">📅 01:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20488" target="_blank">📅 22:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20487" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
خبرنگار: آیا شما سازمان سیا را برای مسلح کردن ایرانیان اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم این را به شما بگویم، مناسب نخواهد بود</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20486" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20485" target="_blank">📅 22:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20484" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20483" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این گزارش های آژانس هسته ای و اظهارات تند ترامپ + نتانیاهو شرایط را به صورت قطعی به سمت جنگ می برد.
مراقب موج‌۳ باشید.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20482" target="_blank">📅 22:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا سامانه‌های رادار و موشکی خود را بازسازی کند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20481" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری | پیش‌نویس گزارش آژانس بین‌المللی انرژی اتمی: ما تأیید می‌کنیم که قادر به بررسی این موضوع نیستیم که آیا مواد هسته‌ای ایران به اهداف نظامی تغییر یافته‌اند یا خیر.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20480" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فوری | پیش‌نویس گزارش آژانس بین‌المللی انرژی اتمی: از ماه فوریه، هیچ بازرسی از تاسیسات هسته‌ای اعلام‌شده در ایران انجام نداده‌ایم، به جز بوشهر.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20479" target="_blank">📅 22:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا سامانه‌های رادار و موشکی خود را بازسازی کند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20478" target="_blank">📅 22:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20477" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فوری | ترامپ: ایران در تلاش بود تا موشکی بسازد که بمب‌ها را حمل کند و ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20476" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">— نخست‌وزیر اسرائیل، نتانیاهو:
«حکومت ایران سقوط خواهد کرد. ما آن را سرنگون خواهیم کرد. این حکومت اکنون در آخرین لحظات خود به سر می‌برد.
تمام سیستم‌های ما، تحت هدایت من، برای سرنگونی این حکومت عمل می‌کنند».</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20475" target="_blank">📅 20:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم:
کشته شدن ۱۸ نفر در حملات دیشب آمریکا
وزیر بهداشت: در حملات شب گذشته به استان‌های مختلف کشور ۱۸ تن شهید و ۱۰۸ تن از هموطنانمان مجروح شدند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20474" target="_blank">📅 20:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20473">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ:
حالا که تنگه هرمز تحت کنترل آمریکاست، آیا باید اسمش را به تنگه ترامپ تغییر بدیم؟؟؟ مثل خود آمریکا، این منطقه «داغ‌تر» (پررونق تر) از همیشه خواهد شد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20473" target="_blank">📅 19:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ایران:
ما اکنون تنگه هرمز را کنترل می‌کنیم. ما آن را کنترل می‌کنیم.
دیروز شب ۲۸ قایق، ۲۸ کشتی آنها را از بین بردیم. ما آن را کنترل می‌کنیم، آن‌ها چیزی به دست نمی‌آورند و ما کشتی‌ها را از بین بردیم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20472" target="_blank">📅 18:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا می‌گوید که حمله نظامی به کشور ایران ضروری است.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20471" target="_blank">📅 18:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20470">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بر اساس گزارش شبکه NBC، هکرهای ایرانی در هفته‌های اخیر، سیستم‌های تامین آب، مخابرات، انرژی و سایر زیرساخت‌های ایالات متحده را مورد هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20470" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20469">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXHsaDtQPSaa02TeZmL9pd1Il6xoNvXy8wA8-7VtSfIbzqeFUnPQXM5oOzcRgMvQtqdgVTeOzsRit1SJX2RYNQ_GGMvM84NQHDN3oAaeP9kWAJHNqyYzrVoZi5Bma1jWHXijVcyjlPoTFjY4N_-ZQeQmvEJ63dl4J4sbummOiQW4fIN4MzvCtl-9BZXluRWLTm1qoBl-2CQpDUcc0rCoSyeGaQXFtCGXB97c8Vs-DSKfO4h91tW4haK1vKK4AYxyZqWZSpS6QSNNihCo0MPm8hiaQGRq23GnJOxXKPXzpXCUSPE-2RxgkmPE7m-h2h7FWN0X35ydob4sm_ItiXOiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20469" target="_blank">📅 18:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20468" target="_blank">📅 17:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20467">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بِسِنت درباره ایران:  ایران مقداری از ملزومات خود را از روسیه تهیه می‌کند، اما اگر خطوط هوایی ایران را تعطیل کنیم، که این کار را انجام خواهیم داد، میزان واردات به طور قابل توجهی کاهش خواهد یافت.  آنها واقعاً از روسیه حمایت مالی مستقیم دریافت نمی‌کنند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20467" target="_blank">📅 16:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20466">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr5Kk_cPt7Yj69u9H_Bjl2QBQeVyyia582mOSQjykPVTkGOZweOccJBZPzwFnSeIiF0_PbTbhNCqaJRLFbkEtuKKyYkYm8j2C5O1Gc4W2lnpfwG8iag3VeyWL5t6NLAfBf4TVFjC9V03vP9-lZiKfRy2NmwzTqrSP1VET3AB5OVjHiwVj9VpTfviN-UTH0qPSNNlY-qXhpMszSIWuMk0A_DZi1hhRuYPbrWkZxn5X8d6YIV4dVUHPGcc3p0QjQ2_DwLI3iSFX2tJaDVjY1T5wBTICZQNfHTsJ8F0J7o_2C5j3PwvIm0T3N3jIaM4ynWP8JX-pTlELNFGIyer83R12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20466" target="_blank">📅 16:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20465">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA1ZXd8vZU6nFcaCoIyWLCfThB-SQv1GSXhKwBXWoZ8Fdzxsg97RbSu8pXjKHYpopuTouvlTIBgN1TToCqWXiEz3n0ZZfg32b_nAzMKfPbKwaFTqcvB_SjHUB2hVMthro9_x4fKQlF2CTBTzYoLMfbX92GD6G-KmY1CuFboyqML4MzauXIP6yl9mjfWzTCspJxi2Zij2eEJCcFvIDf6io5Bxy4rD9OHcwMlm0-ubmN7NcQtfbyR0SV6fNToLZB7v6ORfZXEC6aLhog8WsMYNZinfc20aKiCtPAANlAq6PLxFQoma_1k8A-jtl-2dQpGIo7dk07BeZgaVBK95iUbpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20465" target="_blank">📅 16:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20464">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20464" target="_blank">📅 16:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20463">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAKTq0Rzmd2rm7etG1Lx-qraQTVD1-xfbrDttfVyOge3vFlJmEc-XslaqwXnlV7dYZXQlnMoza1UjD6rakdJSldTFMaTZ2w_6yD18kJo2cOrIUhaCLZDBt29t-10HEsqgvq60g6enhsD44dcnqadkBf4VZz07Z0MOnKWPYFy_KNwUtZiA5ay8ottXg59UZs8jl2-VCKPRw5qL8FSlMzA2MZQT1kMtaR9pvJwsDqNcVUzSqrUTqHE75GQdOIheKMCh7J6HmhxgjedeN7UTpXu9coIruo9FGLkdz1KQlqgfQaIjTTDDCo6_DWAE2eHdRYsFMunKnW0J5rcCDTPGW0Ozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی خداوکیلی این آمریکایی ها ترسناک هستند؛ شما فکر کنید هوموی مفعولشان اینطور خشن است وای به حال هتروی فاعلشان!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20463" target="_blank">📅 16:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20462">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!  از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20462" target="_blank">📅 16:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20461">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">میدانستید این بسنت که اینطوری اقتصاد ما را به خاک سیاه نشانده اساساً Homo است و آن هم مفعول؟!
از دشمن هم شانس نیاوردیم!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20461" target="_blank">📅 16:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20460">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20460" target="_blank">📅 14:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارزیابی موسسه ISW  از وضعیت توانایی های ایران برای ادامه اخلال در هرمز:
ایران در اول سپتامبر، در واکنش به حملات آمریکا به اهداف نظامی ایران، از جمله رادارها، در همان روز، به پایگاه‌ها و دارایی‌های آمریکا و متحدانش در منطقه حمله کرد. این رادارها می‌توانستند برای شناسایی و سپس هدف قرار دادن نفتکش‌ها در خلیج فارس مورد استفاده قرار گیرند. فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که حملات اول سپتامبر علیه این رادارها پس از حملات ایران به سه نفتکش و همچنین نیروها و پایگاه‌های آمریکا در منطقه انجام شده است. مؤسسه CTP-ISW جزئیات بیشتری درباره حملات تلافی‌جویانه ایران در اول سپتامبر در گزارش دوم سپتامبر ارائه خواهد کرد. فرماندهان ارشد نظامی ایران پیش از انجام این حملات و در همان روز، آمریکا را به پاسخ نظامی تهدید کرده بودند و سخنگوی سپاه پاسداران به‌طور مشخص بحرین و کویت را نیز تهدید کرد.
به نظر می‌رسد حملات CENTCOM عمدتاً دارایی‌هایی را هدف قرار داده باشد که ایران از آنها برای شناسایی کشتی‌ها به‌منظور هدف قرار دادنشان استفاده می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، در اول سپتامبر به شبکه فاکس‌نیوز گفت که نیروهای آمریکایی تعدادی نامشخص از رادارهای ایرانی را که ایران در تلاش برای بازسازی آنها بود، منهدم کرده‌اند. ایران از این رادارها برای شناسایی شناورهایی که از تنگه هرمز عبور می‌کنند استفاده می‌کند. CENTCOM اعلام کرد که این حملات پس از «تلاش‌های سپاه پاسداران برای حمله» به کشتی‌های تجاری در تنگه انجام شده است؛ بنابراین، فرماندهی مرکزی آمریکا به‌صراحت میان حملات به کشتی‌رانی و حملات علیه رادارهای ایران ارتباط برقرار کرده است.
حملات ایران در روزهای ۳۰ و ۳۱ اوت نشان می‌دهد که تهران همچنان از ظرفیت‌هایی برای ایجاد اختلال در کشتیرانی از مسیر جنوبی خروجی تنگه هرمز برخوردار است. چندین سازمان اطلاعات دریایی و نهاد ناظر بر کشتیرانی گزارش دادند که در ۳۰ اوت یک پرتابه ناشناس به یک نفتکش اصابت کرده و در ۳۱ اوت نیز سه پرتابه به یک نفتکش بسیار بزرگ حمل نفت خام (VLCC) به نام
Senegal Prosperity
اصابت کرده است. یک شرکت دیگر فعال در حوزه اطلاعات کشتیرانی نیز به رویترز گفت که ایران هم‌زمان با حمله به Senegal Prosperity، یک VLCC دیگر را نیز هدف قرار داده است. رسانه‌های وابسته به حکومت ایران گزارش دادند که این کشتی دوم از مسیر جنوبی تنگه هرمز عبور می‌کرد.
این حملات نشان می‌دهد که ایران همچنان قادر است از سامانه‌های پیشرفته‌تر خود برای هدف قرار دادن کشتی‌هایی که از تنگه هرمز عبور می‌کنند استفاده کند. ایران کشتی‌هایی را که از این مسیر عبور می‌کنند هدف قرار داده است، زیرا مسیر جنوبی جایگزینی برای مسیر تحت کنترل ایران در بخش شمالی تنگه محسوب می‌شود و در نتیجه، برداشت موجود از میزان کنترل ایران بر تنگه هرمز را تضعیف می‌کند. مقام‌های آمریکایی در گفت‌وگو با Axios در ۲۸ اوت اعلام کرده بودند که نیروهای آمریکایی در حال اسکورت کشتی‌ها از خلیج فارس از طریق این مسیر هستند؛ اقدامی که موجب شده حجم کشتیرانی به حدود نیمی از سطح پیش از جنگ بازگردد.
حملات آمریکا به رادارهای ایران احتمالاً محدودیت‌های عملیاتی بیشتری بر نیروهای ایرانی که تلاش می‌کنند کشتیرانی در تنگه هرمز را مختل کنند، تحمیل خواهد کرد. CTP-ISW پیش‌تر در ۳۱ اوت ارزیابی کرده بود که ایران با محدودیت‌های عملیاتی در توانایی خود برای ایجاد اختلال در کشتیرانی در تنگه مواجه است. ایران اکنون مجبور است شیوه عملیات خود را با هدف بازسازی و تقویت برداشت بین‌المللی از کنترل ایران بر تنگه هرمز تطبیق دهد.
مدیر یک شرکت مشاوره و ارزیابی ریسک در ۳۱ اوت اشاره کرد که سپاه پاسداران برای شناسایی کشتی‌هایی که از تنگه عبور می‌کنند، برای مثال، از شناورهای تندرو تهاجمی (FAC) و شناسایی بصری استفاده می‌کند. این روش در مقایسه با استفاده از رادارها و سایر حسگرهای تخصصی، روشی
بسیار ناکارآمدتر
برای شناسایی، تثبیت موقعیت و در نهایت انهدام یک هدف در دریا محسوب می‌شود. اینکه ایران ناچار شده به چنین روش‌های غیربهینه‌ای متوسل شود، نشان می‌دهد که با محدودیت‌های عملیاتی مواجه است.
همچنین، حملات CENTCOM در ۳۰ اوت علیه سامانه‌های پرتاب مین نشان می‌دهد که نیروی دریایی سپاه به‌طور فزاینده‌ای به استفاده از پرتابگرهای راکتی برای کارگذاری مین در تنگه هرمز متکی شده است؛ روشی که در مقایسه با کارگذاری مین از طریق یک شناور، روشی غیربهینه‌تر محسوب می‌شود.
با این حال، سه حمله ایران در روزهای ۳۰ و ۳۱ اوت لزوماً به این معنا نیست که ایران هیچ محدودیت عملیاتی ندارد؛ بلکه صرفاً نشان می‌دهد که تهران در این سه مورد توانسته بر این محدودیت‌ها غلبه کند. CTP-ISW همچنان نرخ حملات و انتخاب‌های تاکتیکی ایران در هر حمله را زیر نظر خواهد گرفت تا مشخص کند آیا ایران هنگام تلاش برای ایجاد اختلال در کشتیرانی در تنگه هرمز با محدودیت‌های تاکتیکی مواجه است یا خیر.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20459" target="_blank">📅 14:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وال استریت ژورنال:
دو مقام آمریکایی می‌گویند تاکنون هیچ تلفاتی در میان آمریکایی‌ها بر اثر حمله ایران به تأسیسات در اردن گزارش نشده است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20458" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس:
آمریکا برای نخستین‌بار نفتکش‌های دولتی ایران را هدف قرار داد؛ سیاست «تانکر در برابر تانکر» اجرا شد</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20457" target="_blank">📅 12:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملات آمریکا ۴ عضو نیروی قدس سپاه پاسداران را در کرمانشاه کشت - تسنیم|</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20456" target="_blank">📅 12:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT9QyjNMENh0eb-R81TwcQa6QbuVpjtJEndiEQU2i1MMhLRnGETGxaJBXte-10Q0YDRhsaZql5FOrB25tFCR0JU60JUv7OC3erH8Vu3FmtPGmlGDx6azaxtcirRSzZdtvyrkbtuzUbq5l6Ux_kR00jN1oRgOFHZe1t3i4TenfR5lZlr2jEJjjtKkc37puP4gYrsZSMv7kCHtzFNHSgXfc8Cm9OmeUazYHwlAboc2DEZAsGTK0i5LrXO-l3pXNiEvXn3ElkcBCRTiUlqO2KrJP1BmX-vgtnALPnBx1t_rRmmDm9E57yhZYCbA9ZW_cU_uKqJoaYtK63VbTuqfA4PA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20455" target="_blank">📅 11:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حملات آمریکا ۴ عضو نیروی قدس سپاه پاسداران را در کرمانشاه کشت - تسنیم|</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20454" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3dt2Ic4Dhsa47leBSgT1c3CLJD_SLThkSswJlrcXVYCy0NnFr1Q1vCsS_fWKbhW9KQGyyERfL087ZokKedkTjhvQHXCMKFhgwBeUZKBh5oTj88EXDvRqCmOdOhma-4HKVO1K4bX35wiKz7IIrshwKXt1RfX0i-_VlawlR64VgAU2rEACrnBNySZIccMW20Sg0efxaAyC_nOhJfBo7soYZ7CjIMwyEt0yvQyAQDKRCZ-G98AOdFuhrlTppB59XLQC_EJJ3N9ZvPhhlfys7xJr3-dd8AT-dBUpl_xEqmHar7qoA50CUzPhvB5nEn1jEIW7xsw6PVmRv9GWK8AFjmgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه ای قرار دارد و با توجه به بیش-فروش بودن تکنیکالی، امروز احتمالاً یک اصلاح رو به بالا در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20453" target="_blank">📅 11:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حملات ایران به بحرین و کویت1!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20452" target="_blank">📅 01:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyrHEWNo8XgTC55gsrFP_5CQ16rPSdXl6TJ_EzyxrdfC6_dr1Cq3g6d3tk2JFQL41H5LeLgZPOjatMPaclpAZx9Unn927Ak7VNwJyn99Ev2Kt0gy0y6eJXNrh3ErSSEQuZvN6aMDljKziobrV8xOqqQIiMmO0AhvRtlgE6exq4UI9Q-Cu9CAbW19i84krhwfR1UaUFrOqRmBS50gZmgPp12Z7E6rdkoOFVXUSSeXDwGn9yQtIF-L02MnPLlkQGggaVyn08KqbzKJ8bCuA3u0zgjsqZQUaLEUgZHB3lkj0Yi26QDI3m4eM-kg3EKj8riaeTlCqrIVmOye9ZcEy7m1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سپر آشیل»؛ ورود یونان به عصر دفاع هوایی چندلایه   یونان و اسرائیل در ۳۱ اوت ۲۰۲۶ قرارداد تاریخی «سپر آشیل» (Achilles’ Shield) را به ارزش حدود ۳ میلیارد یورو امضا کردند؛ توافقی که آن را می‌توان یکی از مهم‌ترین پروژه‌های دفاعی مشترک دو کشور و نشانه‌ای از تعمیق…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20451" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20450" target="_blank">📅 00:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20449" target="_blank">📅 00:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بالگردهای ارتش آمریکا برای انتقال زخمی و کشته های خود در اردن به پرواز درآمده اند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20448" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20447" target="_blank">📅 00:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsVciyuOYsJeXIGXFSdqG3jmoI3quhNPaAHjoeqrf-aHa3qvSlIfIaNtpqUv44xn_JH3CuKRj9QDy_-PXmiqye05weG6BigoZ_TR8fnvLUpfJe3uxnFLKGplPLcewQwHkXE-3W9HDGehyofBi3nrCpMxSPdoYM2yyP4sacnD8S8kv97J7KhNJl-YZn5sb-HHJ07SgHxEjJU88WFh4Rqe2Ilyyq-ZPm6tEIpB5cl7tk-SWryJ_b5EJdT3OtbRHvm2d9Vv5UMIJfAJEpDH-TzuBT1F969I1OJTwGw47pxnKIMHYqwYlAfTNSVvWuNoxJfU7VYoOqWR4ujC_SrT1AerUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20446" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0Eg6gagDv6fsWnFAA0LrxP3ewHrT3FvMIdLOK940e90-8-xqMxkMn61wyGX__BHXwwz7kyBjbnNIPMx2wNvAD4kdskg0kXf5ciP915GEykNZSJFPqs4-Aiyujb8TtI-V1dM56V5y6Ot32yZ2jfT1ECPi_4Ok-GWiqv5kbOHWyY5vnMP1XguCgXR_RAorcpv3dWUoGSwjgppu1Hckaxry2Aku2C_KSaO2PbTnUZQnv3Qy-2CMLhI01a6iehaazFSYPu9OGF2u1TuifHZ91m0EjblrUR1lu9U0ykp8yNAY9hcPKDT0s-3YnM2RdkQFlTIRXzoBiyftMA4hxVU4lzfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=gsbo34Pg-8xuTqBmlqo8sQQGWoC_m2rGDTlA9l_4QGlL0PPit6kiHmQ9B5ovn1KcQRPVlT6VG6Bx5Z20RfmFV-QQs-OfkJ7fuedBrW7X6OLUuaGFZP7_Dx7t_k8W3aLsXnBqCm6zpyGte9w2dQFcouxIT1z2VI-XWl5vkzu9Ectrk_8MI-i05fvp33-r_LDBQksrZJ_UZS8p_x0mn4B8h2vEB1rnbJUHecSX2OVYm0QiShHugwXfaaO9qIqCwxYBtqjveIba5aMtlWPHA66aPxlEXyuFfhhMLP3zRewAMfC1o_z8uHthXY3RdBuGM-swGtFRSHcwUKbeLBKtzblOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=gsbo34Pg-8xuTqBmlqo8sQQGWoC_m2rGDTlA9l_4QGlL0PPit6kiHmQ9B5ovn1KcQRPVlT6VG6Bx5Z20RfmFV-QQs-OfkJ7fuedBrW7X6OLUuaGFZP7_Dx7t_k8W3aLsXnBqCm6zpyGte9w2dQFcouxIT1z2VI-XWl5vkzu9Ectrk_8MI-i05fvp33-r_LDBQksrZJ_UZS8p_x0mn4B8h2vEB1rnbJUHecSX2OVYm0QiShHugwXfaaO9qIqCwxYBtqjveIba5aMtlWPHA66aPxlEXyuFfhhMLP3zRewAMfC1o_z8uHthXY3RdBuGM-swGtFRSHcwUKbeLBKtzblOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20444" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0lEa2wjtaTYWR7WKAJrJh-Ucp-dVYzLlwif2SHwhQqJarw2JQnv11xZxStFV0vaM9_jXcRgyitzH7i18Tvz90xcAYyO2HqyeJdaWo7nd4fp5gSaIGfinYN88Q_hOHh9mJtzIDvG5CFiWG79FXSYs5TmIFL1sFJz8LhcfWj24pZCVs2DJjGoHgbAy4L0z2T2EkDrF1b9nowaJgK1t-LsE24vG-9oPbBN_balbp2G5lhTcwkweSeD5qQnI4BoAyvL0eq7MW6MmfCV3VrEFvSC_xktgggna1mgSx8XxAOJ3XRc7DiwBFYmm9qFSVBg46uoeMtf73QXeivpXObxN7okPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20443" target="_blank">📅 00:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCEe4t7vAT_pEKZEaHNurYdHs856G8qlezVC42NnBc3cHA4uw3rcTw5XKCF1lkBN2g-PMvV8_eO_vdlx6itn4nyu2uqkJpUo7f_Ds05j2amIiZW7cwGiZb5ebmBUAE4clyW7AUpQXgMzjPNBnnFRxi5HEXkgFv0ZF-IeFQxKYv7h9xiVH2km83DnhQkBFAzO93DRDPJJfw0GS4k-UQtCwbV9RHl9EsJogWzdUzs8y0KzpZaQEP7wAS0oiAxiL0KbllLtvG0wOhiSvz6rg7NlvLVYPZ_5FAyATtVD1nyVd9afJ9RKw39XG6Bc22m2kClqp_i6B0AZSF1SLKz7PgNP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20442" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
ملت قهرمان و بپاخاسته ایران اسلامی،
ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)"
با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه
، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام
ادامه دارد
.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20441" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باز ما یک سفر آمدیم همه چیز به هم ریخت....حتی سفر درمانی ما هم بی عوارض نیست چه برسد به تفریحی</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20440" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساعتی قبل یک خودرو وارد تجمعات شبانه در خیابان اقبال لاهوری (مشهد) شد و جمعیت را زیر گرفت، چند تن نیز کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20439" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20438" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار فوری | اخبار جنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=CLXXMUpdaljEbm-Pg8eMG2T5-T6HEYdXzHABG_L5h-2eYFQMDCL8Kd6g_xXtdDA7gKuDN5zajXoUU8y_DG0fc-720mCPuf2rqZPJvlZN5neF5RXr0VZePjS5R0q4XUby77e1-8vQ7L2VOkoWugMqahIJMyC89-MIanIrWA75cEKgrcNDDsCfEaRQG_cg4hFGwKdFNql3M3oNGRfR4dqh2VZBc55sg0_DoG0cTiFVgcSkTf5J9gRo1WpEtklN269OEuGvg487M94eQbos5xfWb3QxZeuen-6vfhjrd9OiddUJc88_riJxDD1Bnw3c1dAb-y8sGci8nqb9GcTVka-zXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=CLXXMUpdaljEbm-Pg8eMG2T5-T6HEYdXzHABG_L5h-2eYFQMDCL8Kd6g_xXtdDA7gKuDN5zajXoUU8y_DG0fc-720mCPuf2rqZPJvlZN5neF5RXr0VZePjS5R0q4XUby77e1-8vQ7L2VOkoWugMqahIJMyC89-MIanIrWA75cEKgrcNDDsCfEaRQG_cg4hFGwKdFNql3M3oNGRfR4dqh2VZBc55sg0_DoG0cTiFVgcSkTf5J9gRo1WpEtklN269OEuGvg487M94eQbos5xfWb3QxZeuen-6vfhjrd9OiddUJc88_riJxDD1Bnw3c1dAb-y8sGci8nqb9GcTVka-zXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20437" target="_blank">📅 23:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه کویت مون نشه؟!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20436" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مرندی ذوالاکتاف:
با توجه به اظهارات ترامپ و بسنت، به نظر می‌رسد که روزهای رژیم‌های خانوادگی عرب در خلیج فارس به شماره افتاده است. آن‌ها نمی‌توانند از جنگ پیشِ رو جان سالم به در ببرند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20435" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جهت نوسانات رو شاخص درست تشخیص داد (رو به پایین) اما شدت ریزش قیمت با تحلیل ما سازگار نبود.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20434" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mblNvV9ImmGWdg5VoOuSgLYi3vVpFXd5PtI8PlzG8PF2JDG8VG7pWQCNgRXw8MLmPf-34X-Ddqsx0qKbnoXUnlEe70y0bahPvNVP-GG4PtxO5g6wRDxC_mNT_nH_mitDC3OXO4L2roWhZ2MXuxEg4jNgESuxzAZpqIwTf6A04uS9MMvSasu3CBBSgJwQraOuH5gfjt7y_L5FEEptv3YQjNSRs__Wr5DDMDNW5o6twZgQalM9Ls9COaRsVZuEbSF7pMYV9qGW4wxL3dyfNZ6QhWnCo27dDr-H_egv9itwnK6Y3uO5GwxD09em4xNjc3v6MqPhdnIDTCrisKcRSM6Hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.  با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20433" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شلیک موشک از تهران!</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20432" target="_blank">📅 23:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پزشکیان:   همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20431" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پزشکیان:
همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20430" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20429" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حمله ایران به اردن</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20428" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">معاون سیاسی و امنیتی استان هرمزگان: در حمله به یک مراسم عروسی در سیریک دو نفر شهید و تعدادی از افراد نیز مجروح شدند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20427" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سقوط یک پهپاد MQ-9 آمریکا</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20426" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگر آمریکا باز هم به تجاوزاتش ادامه دهد، خمین را با خاک یکسان خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20425" target="_blank">📅 23:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله آمریکا به همون همیشگی!
سیریک
!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20424" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20423" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20422" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حمله به عسلویه!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20421" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گفته می شود بقایای موشک در خود خمین فرود آمده</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20420" target="_blank">📅 22:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آژیر خطر در قطر!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20419" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRWMlQKFP4sHyyVXfP0Rxj2vRyCMDImyv_8GDn9IlUm2KhIYqHRpREhSwPqi2HOLahYG_DbobPe_LFOJBfiEqgNtKm3vmhZeaEzdejCsioxLhm7YkNZP8l_QnOmCK1LK2mRJqao9zA522j_XEGaxD7SNloDr-4jCciG29M1UTexqdraS5_guBvTGqqjExHqvHIDEX12JgnQqACVt8d4K_bjVWUM2glGQdqHL4JD4Dq83k4OTpmXJWfq07ZyWYfr1o1hnReJXfWtpjVt3DY_eK1kSbBjk9FFzFe5mVrNN-EHil6SCqg8mFmSlyLTyBOavKQLaekz36g7_MUfC5YGj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن دو هواپیما نیستند پس احتمال حمله به تهران هم هست.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20418" target="_blank">📅 22:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">‏ترامپ:
حملات جدید آمریکا سیستم راداری ایران  و کارخانه های تن ماهی را هدف قرار داد
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20417" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!  کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20416" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20415" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دقایقی پیش فرودگاه جیرفت مورد حمله هوایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20414" target="_blank">📅 21:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">منظورم موشکی است که از خمین بلند شده بود.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20413" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">موشک های بالستیک از ایران شلیک شدند</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20411" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «مجازات شدیدی در انتظار متجاوزان است.  آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20410" target="_blank">📅 21:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«مجازات شدیدی در انتظار متجاوزان است.
آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20409" target="_blank">📅 21:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
«ایالات متحده همین حالا در حال حمله به اهداف ایرانی در نزدیکی تنگه هرمز است. این حملات گسترده و قدرتمند هستند و در واکنش به تلاش ناموفق ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه هرمز انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (تمام مین‌ها کاملاً پاکسازی یا منفجر شده‌اند).
همچنین در واکنش به شلیک هشت موشک از سوی ایران به پایگاه نظامی ما در اردن که همه آن‌ها با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه، اقدام تلافی‌جویانه‌ای انجام دهد، بار دیگر و در سطحی بسیار شدیدتر و گسترده‌تر هدف قرار خواهد گرفت؛ اما این بزرگ‌ترین حمله از همه نخواهد بود. بزرگ‌ترین حمله همچنان در حال آماده کردن است و هنگامی که به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!»
— رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20408" target="_blank">📅 21:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دور جدید حملات آمریکا</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20407" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تسنیم:
برخی منابع از شلیک موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه خبر می‌دهند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20406" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">– گزارش‌های تأیید نشده حاکی از آن است که موشک‌های زمین به زمین دیگری، احتمالاً HIMARS یا ATACMS، از بحرین شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20405" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده شروع به حمله به اهداف نیروی دریایی سپاه پاسداران انقلاب اسلامی (IRGC) در ایران کردند.
این حملات پس از تلاش‌های اخیر IRGC برای حمله به کشتی‌های تجاری در تنگه هرمز و علیه نظامیان آمریکایی مستقر در منطقه صورت گرفته است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20404" target="_blank">📅 20:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به نظرم نیازی نیست چون خود آمریکایی ها هر هفته چند بار پیش دستی می‌کنند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20403" target="_blank">📅 20:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">— سفارت‌های ایالات متحده در اسرائیل، قطر و عراق هشدار امنیتی صادر کرده‌اند و از آمریکایی‌های ساکن در سراسر خاورمیانه خواسته‌اند در میان نگرانی‌ها درباره تشدید بیشتر منطقه‌ای، «هوشیاری بالاتری» به خرج دهند.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20402" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
