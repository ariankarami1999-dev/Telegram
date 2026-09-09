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
<img src="https://cdn4.telesco.pe/file/XiKqgOxOCO4w1wOIsavJGlrfpoiq2CAB-EntSWY7NXCmjYXeI08svO_xwhnjn_BZix3pUKxj8ukN21PaGfgUq9PV9S7vqwuYMCdsHLVXvxHqMzbrL7vBTkLWwDnbPk7EBC6h0cDiL2CRHfzxMEiX2wNiw2x_gFQNNPWV1eR690s9w1SXdCDHdFSv0iJb73uwd1ZoPsgSYXipchQilsdBU51ROqsuK0zIkMwNzuTE4bJmDYVe5m7Ao_Lm7uRr3_aPeEDJwyOensE_mDnXhcx2d7a6l6bcFEZ-mmTnrNoJShCLiGmWPry_llhdI3RIXgMP64nhkB8NEodk6qf4h7E_GQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 19:06:53</div>
<hr>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ5VIxSxqxc7nREWa-5mF-OLog8ah8kHR4F9ucTigTLGj22H-hrkesWd8msTyhEhHE5ed_lhhTF-lmZ3siQGQ-WXlEUNQJwjD886F7w2eiW40u1rgQdWKQpPXX5d2QfW87YAw_8Urw1NJq3z6l856KAYcq8P1fukubrHBuayWuTgeZaVpCK6m0CC5eZjeVldBVvy1BU4Oq5-o-sqy149ZcKZZFDoF35u-MFBKx2jjVrXHO1MbaAEpDCFcGWYKqKGcllumGtQdkKrEaYPLSYv_Vz4wJvnNc8f_untELyyLmrAzp4v9dLuKRaKT-kqrD7T-I60y6iCO_drHZFh9UsP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRpvDdA6q-gwmD6f9cqIwfxt42z1dvksEXGQTeWdKTmkUlp4Vk3gP6BNzFlcJ0GDqDnA590SpyPfPuTE2KMCngO3QfrSqXdMpRNZ0VU3DNifChZI5ubLcoqjgWasD8vOgUBuYLmjVW-M16gyOUEZederx294HAkJDsQicJOB3G1S75PvVRx3ROTi4Xw7o3N6kGYDDrZGB1ndimNT8hybc0GeISfUp7tUmFAfeHCG0hy8qWWP8d19WO9QjZag3m-50MFBm_iLScyrssQSeCxkdcWNT3189ISKW1lqp9w8qyMbsvhcD_w_S9icbwLfTN0OuXyQZB3BQBhxROENkCUY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به این حرکتا، همینکه تاحالا اتم نخوردیم یعنی هر جور حساب کنی خیلی تو سودیم پسر.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/83204" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565302292d.mp4?token=W0nTfNnvn-O2MJtirn3HoPaWMhFlSM0ebfbup6WWZb2-StZqED_tY4c-ogGMqiarwCEgpFWjwnNyMn4vJiQH8ExOyKhkAfJJ8f7zYEEHOGhRKuj6kDDzpqxjBgkzzV1NnQj5xR6UJtIQpVn0lsr6gt4UcdvGDcucYa2SXYpbeJdjSNUutVpsNU2ZUEd_HSW7T9hK9daLkvdjujqikZwf7rZkKhUU8SkRQJIV-WBAbCd7hJS3RaHmgNc56RfOmWATXtGAApNBWx1trfTnnrEfB7j0Vv8zyAr0gc-wVACkzhVv-McYLpawvUYI9ex8Jkvt4ellp42p3nfZRvM4CC8tIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565302292d.mp4?token=W0nTfNnvn-O2MJtirn3HoPaWMhFlSM0ebfbup6WWZb2-StZqED_tY4c-ogGMqiarwCEgpFWjwnNyMn4vJiQH8ExOyKhkAfJJ8f7zYEEHOGhRKuj6kDDzpqxjBgkzzV1NnQj5xR6UJtIQpVn0lsr6gt4UcdvGDcucYa2SXYpbeJdjSNUutVpsNU2ZUEd_HSW7T9hK9daLkvdjujqikZwf7rZkKhUU8SkRQJIV-WBAbCd7hJS3RaHmgNc56RfOmWATXtGAApNBWx1trfTnnrEfB7j0Vv8zyAr0gc-wVACkzhVv-McYLpawvUYI9ex8Jkvt4ellp42p3nfZRvM4CC8tIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فان‌هیپ‌هاپ در گذر زمان:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/83203" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/83202" target="_blank">📅 17:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=u9WBUykGO81AjIxxkKhRr0mfv8nULRvWPLxMnW0NWltIoSTQR3q9_XazwOLNauVGz6lu8cQqGvtdphn8HIvPd3KrGJs0jwH6xj8mSvsTqW0eUxjl6mUCotP-OCsom-Wlik7X-Jaxq6YVt4XXeuLXiUmZh-DO3MXesQDNH1SyNzPmZdhsR-Oj7bP1ugh0sXd43NonAXUR6YA0sBd1TZwNIA994O_7TkWXQuQ7i1Nv-FfTKzPRiy6vDsvI07HOEI36PoJovJMZQSRi2ms2Jajwdo4FLofpUXWtglEYG0rfn9cKU2Bqt1NaeCRAFon-rHK5943UqikjbfCz5le_VvgATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=u9WBUykGO81AjIxxkKhRr0mfv8nULRvWPLxMnW0NWltIoSTQR3q9_XazwOLNauVGz6lu8cQqGvtdphn8HIvPd3KrGJs0jwH6xj8mSvsTqW0eUxjl6mUCotP-OCsom-Wlik7X-Jaxq6YVt4XXeuLXiUmZh-DO3MXesQDNH1SyNzPmZdhsR-Oj7bP1ugh0sXd43NonAXUR6YA0sBd1TZwNIA994O_7TkWXQuQ7i1Nv-FfTKzPRiy6vDsvI07HOEI36PoJovJMZQSRi2ms2Jajwdo4FLofpUXWtglEYG0rfn9cKU2Bqt1NaeCRAFon-rHK5943UqikjbfCz5le_VvgATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ویدیو دیگه از عملکرد قوی سامانه پدافندی پاتریوت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/83201" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMMI1h72hmD68p11C2O74OWGSUJ-xoCD6xNwckdc2yk-DlxZ5hYllGZfaIL4_9_YDxH3brWpnpuo5NzzcGO1vfd_jyAMXDX1xMVu7xENC49Trtic5EkqhzTrhbXvV0cu0lQDYlDCB7zqHHdsPieAYH32i73Z5pnpIhismGDHAe9YFUgNf_aavwpt3-pzdpYP3d6Vgnbr_DcReYvyNagARIHi74RZuCy5Y_j_7xVV-1bHRKSVVIRRkXrBNR6hIVOyfw8okXljnWLYgKxJ2xpqEGHZI3maJ_N8M21ADReQYjpyAqG6iSJoUNXqaaFfhxQdzEoVVlbxoq9NLsTA-2aZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد محجوب ۲۵ مهر ماه قراره با لویی سادرلند فایت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/83200" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/83199" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZj6C-SxsXHoW1jbwqG_NzJpOXa5FE9Aarmc9VgpwkzbXR4n1h3Wr2OfRDvaVrsp4qdzeQoKDieu4ornm2Lsjg4yvsSniB0pqWnCPDBbz6AFWj4UjIVMs7jhYQRObPaU6tyqFphIoXnvAab3LcD2yqnWAw8xGsNy-VA-Y2dSyZ4Ke_IZd0PSXTaFGUWdoe0ztsbkA1V8bUU6121EQ9wIjXy1L-EktwtJexAhpEn9n_SnB52nyruU_6Hd6TxUJJB8sBQobUVvxqqPArgz6InFQlCXbJAFT7QWyUoX-74auncgyJj0lm3jkHN2m8I98f5X-Nx7cs4dSPVQiL1fxVD-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/funhiphop/83197" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMRS0z7OMUwQ_T06MZeXhrogCsouSmdawy3IVrgkZSGNXFIENtuxDYLcfaCNsIoLAjTzy-Az4T_njAQ02mLNW7K_XUpquNd0_w50H6DVi5l3mXyVCPetuUf9IaUO2o5ixZdD3yaEfCfDXGwGgbqekdCIl4GoTk9VRuP5vWvoBEmn44Y4TGb0o5Wm9HAKE_QJ5xjin29ZsKHzYv4kkoUL37XbKPdiW9TMbUv35f0DGXuiqt3_MGkSlYhsF1zVTPKYxMsn0GaLIniBr3lhAtRsGQnsjRmntB78jzL4jZ0Jozrv4JNvIayonLvsW_PSxX14xGXXED2cBvDz-HxmBEL1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/83196" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTxf2e2K3r-i_kvR9JSUpB5fOuvYROPAKtf9AK-yckXfqOuXM6EXrYOMF0aHIfJ7dfhnweearYKCxJWL829fqaVf5NEv2Z8-01_IacXn67f2avB51zOoBeGl-HH3iuhHk-2FR4DNqvRewkyxfkJzjPniyE75MYYfUDp709cVHhZY9jM_KXc8D4hEHLjTdceMzX-JjY3ApHhc8AfLuj9ANwhFPsHhLXMi7HcYAI-iLhaAPOdZSB5zOWbUHg3WOlJH9LKcmTLXpre9fplqgoY5mvk6MkuARf-tShG-chHW0FhuglYVGkOom0CJJ9XcBXsUeHSUUhrVwH7xB9ZeyaGFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ های احتمالی آیفون ۱۸ که میتونید با حقوق ۳ روزتون بخرید اگه قاچاقچی اعضای بدن باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/83195" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHxWWWEZh39oUR-HMDlm5DsMh9vRFrCvfLQacKEc6RZCWjrLsjBua8mt5byOow63V5gXJtvFO6NBawTvn3ToNbcKjagh5y0O1QfOhvcowBssrsUKCjV0NMLrkmVQSx5e_KlnIdS6zzrzjNiZFnMu9TheJ2O-3JWR6pYlmWZZZFyx83v8qHKZtHBvH0rJ3YWTQVUv0bLI8XhbpkblWMJV9BKILS5yLi5gnHtZFoWy0-d3ANZoroCzd_hAz0vzNu2BxNI0vHUhhLuoSUswZZSkOdodSbMZYdg8cY8YMsGNz1fkRiABs7U5xFuYp3kyPgVhkDgmxu-gq4CozwN-Ua7Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی وقتی دلار ی میلیارد و هفتصد و بیست میلیون تومن بود.
(اینو چند سال بعد بخونید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/83194" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=OOFA-9C2tPO-vtUtbizRJJU1C61UB6pUefdHMm78g3JJ9SKYSVi_AqE_1mMyB9Aqp3tC4hQxWsdrp7J9vOYoRa3X9m16eqD18i5ewEZJv71-uxYOk-SraiHQWovzu18cvcXa2MDj5zPWDZkwGfJIUPnmTK_Bo2ngHaGTrcnRCGCnpO60avkOX8d9RAW6PsUUJt8t3Ibwqj2u8qkTLrRIiL3DsEsPoaNA-nsUvTSf2g4YnH7jUF-XcxUzZWLvKJfdA4WQiCTukrHPb_6JBht6Td_QxmC-DYwHDnz_FOXT1Zi4HJ5t4uRKtXPR9GqLl2UCGvHZqK4fcFDYppCaUucAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=OOFA-9C2tPO-vtUtbizRJJU1C61UB6pUefdHMm78g3JJ9SKYSVi_AqE_1mMyB9Aqp3tC4hQxWsdrp7J9vOYoRa3X9m16eqD18i5ewEZJv71-uxYOk-SraiHQWovzu18cvcXa2MDj5zPWDZkwGfJIUPnmTK_Bo2ngHaGTrcnRCGCnpO60avkOX8d9RAW6PsUUJt8t3Ibwqj2u8qkTLrRIiL3DsEsPoaNA-nsUvTSf2g4YnH7jUF-XcxUzZWLvKJfdA4WQiCTukrHPb_6JBht6Td_QxmC-DYwHDnz_FOXT1Zi4HJ5t4uRKtXPR9GqLl2UCGvHZqK4fcFDYppCaUucAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دانشگاه سمنان درمورد اتفاقات چند روز پیش و تعرض به یه دختر ایرانی توسط دانشجویان عراقی:
از همه دانشجویان عراقی‌ای که هیچ کار بدی نکرده بودن و یه دروغ بزرگ براشون بافتن عذر می‌خوام که چند تا دانشجو ایرانی که حالت طبیعی نداشتن سمت خوابگاهشون هجوم بردن، ما دستگیرشون کردیم و کاری کردیم که اعتراف کنن به کار بدی که کردن شما خیالتون راحت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83193" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ما تو خیابون کسی با استایل دهه هشتاد میلادی ببینیم مسخره اش میکنیم، بعد شما میرید عکساتونو میدید هوش مصنوعی اون شکلی بکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83192" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کیا مثل من نمی‌تونن تا شب صبر کنن تا مشخصات و قیمت گوشی آینده‌شون رو ببینن و پیش خرید کنن.
😍
بیاید بهتون قیمت و مشخصات احتمالی رو بدم تا از همین الان آماده باشید.
😉
این رو برای سیسی‌های ارزون هم که دنبال آیفون ۱۸ معمولی هستن بگم که آیفون ۱۸ عادی فعلا تا بهمن…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83191" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN6LNatek0C9KNMe0hkiEfH2jQuck7h8-gxYDPl-obG9v0Wi0MNFreEThbXHDV6Aza5Ppg1lvhhJ-raITjhDsT4wdEDW1_BfUxaVTu0tg-ubXcumATzdixxTQZiWoJxmPIL6dUIDAJur9sJ6hIy1TsuOCP3EvgypHYtWKn-bR_6-sQ3Kt4RVKmm0CQVVTrtZWP-HGBUbwKpdFZUtTGyUsYBpG8XvNhU_0L-hD66xNzF896GGQHs-d-0A8XEFzlOpugi2_YzpT6iIgLqjzF9sv0RuAO15RKGIKnxQkItmgWmkasNr3i33tRtiiOw_vXDHUN9nOW73fTzVyvkNpHmUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83190" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حاجی من از آیفون ۱۳ به بعد دیگه باورم نشد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83189" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلار ۲۳۱
درهم ۶۳
طلا گرمی ۲۴
خدایی این وضعیت برای کشوری که میانگین آیکیو جهانیش تو رتبه چهارمه اصلا قابل قبول نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83188" target="_blank">📅 12:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روبیو وزیر امورخارجه آمریکا:
از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83187" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=MCBcInv3aylKJ3Cg1bAPf_oeg8LR2hxyrDWRVMAxpkIyhuYb4ULRE4Iay7CCCrW7l6883oxnzh-1ovQqsQBiTjXzFBv3Pk1QdK31hiYH91x2uDolj9mGP05qWY-cmEI9NpoExW5WtxvWeP57YOFDZHSCmGujTUWU3wtBU5JE5vhsbi4Y5k0FEJ-yy1NPHgNzpq1uFXjJfgVqHplrVCf9ipgdmnrApb8MYXFr8nCX6WwGURJRnU6sM2MKbhsgt4SFX2NvBIqq_5K3wZuQdPFEHpNtr_3FA29_j1NppW6vf7efg1OhnesWagtfrrAdmVh8jKwYSIqlkVev9aNebi_nkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=MCBcInv3aylKJ3Cg1bAPf_oeg8LR2hxyrDWRVMAxpkIyhuYb4ULRE4Iay7CCCrW7l6883oxnzh-1ovQqsQBiTjXzFBv3Pk1QdK31hiYH91x2uDolj9mGP05qWY-cmEI9NpoExW5WtxvWeP57YOFDZHSCmGujTUWU3wtBU5JE5vhsbi4Y5k0FEJ-yy1NPHgNzpq1uFXjJfgVqHplrVCf9ipgdmnrApb8MYXFr8nCX6WwGURJRnU6sM2MKbhsgt4SFX2NvBIqq_5K3wZuQdPFEHpNtr_3FA29_j1NppW6vf7efg1OhnesWagtfrrAdmVh8jKwYSIqlkVev9aNebi_nkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83186" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دالر ۲۳۰
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83185" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUdXO4KeKMXE8hezLMZMjpRnxZhrG4pYRJh9KJFV2jl1TyLdkW4QP6r3rJMoG1YY_NyZ_t3H7CJIOKvr5rqJPtW91Uv48VHhd3DOXzGBxrqsWsmVmxdvrRjewkeSf34UNtgNS4pq3IGi3P5Ybi9iQvkDwSLsqZjWIZ101A8QPt8EWcvXhXPnMa6oUadnlP6PYKMzZ3dmJH6XZKqUmRyPBepQjLKT4MI5VldwOzjvwBJKVXyT8xxJgP-5VDmcih7eHfaQZm_DRC2cJkh3PwlYzzAtsI2PJfihwVjh2KJmuW_oyT_q83FLFpW_2uTWAFWYNPmtg7yBzkerXhxY1DrVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83184" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=awVWULaTaVc23KZJo0qKGi-9gUXHjYag2PSa55dUoTlfg8jjB9buUv3HjgJ2H0eVTTEdO3kFC3OwuympcmDeRAKcUSFQoDB3gN1Rjb6xYBepI-e9mXPgqQB6W4M4n8su7HBnWdszwL86IUlKB8fisFCXFT34pnt2IslTYRBCPcJa7-RQpBsnGi42RDVNkBz9VALA_Gz_FQeuf_x3-5NY9slZnDv0eIiJGWovblMDbicmmQ7CJcNncjFhpFVDxLGpiFAbGSLr481mQ78sqTHzf1kENc3ccJ9QkCAqAx2ZsrMjB5kM8f_7lcUzJyIuhaztniLQ0gAxhZFo30t44nKbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=awVWULaTaVc23KZJo0qKGi-9gUXHjYag2PSa55dUoTlfg8jjB9buUv3HjgJ2H0eVTTEdO3kFC3OwuympcmDeRAKcUSFQoDB3gN1Rjb6xYBepI-e9mXPgqQB6W4M4n8su7HBnWdszwL86IUlKB8fisFCXFT34pnt2IslTYRBCPcJa7-RQpBsnGi42RDVNkBz9VALA_Gz_FQeuf_x3-5NY9slZnDv0eIiJGWovblMDbicmmQ7CJcNncjFhpFVDxLGpiFAbGSLr481mQ78sqTHzf1kENc3ccJ9QkCAqAx2ZsrMjB5kM8f_7lcUzJyIuhaztniLQ0gAxhZFo30t44nKbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب سپاه بزرگترین حمله موشکی اش بعد از ۱۷ فروردین انجام داده، این وسط هم پدافند پاتریوت آمریکایی اینجوری داشته موشک رهگیری میکرده در صورتی که اوکراین بدبخت بخاطر جنگ آمریکا با ایران دیگه ازش بی نصیبه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83183" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83182">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83182" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83182" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83181">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgTAbFxaO2deGfJV1m6EyspEM3tlRNSryYhazIQoqX0tQdrbrVMz2QeEINLbLG29S6gt3aWj-pMyw4F66Joi-hevJF4iNSUiECdt65nAQR0JLXSjWtfOTnTF6c5JTV25aVSkZ3BRWaZC42v-p55fEpQ8qGwP-ZTBNofS6Ia12AqRD4DIn5w-R8lg8cPh7Q-2iyKgDIP3GoCBMUtv_M6pvGSMJgloBF8QY21N27XJO6JANzGfHOH4WxI80rs9RmC6xETf4_81cgvx-ofkFuwqVY4VqO_xp8eA_MLXgqg_-o-q91EO1tMI0ppWc-HWE924Y8REWqmKM0QVEQDj7UVrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r18
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83181" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQWb8DKgeM10d2yvZUesNwjBR-GJuYk4iUmpM4iAhnsqUyhL67r77TSoRRp8rfuxjauzo61JGzU8O_ZHCwK5_TP6D2uYxQH-ddOgNrKuk-gbKoAY84tIgP_4ECVqxAL-70HVPTUypqte69uP6CEPrpKyXGwN-tfLphYYXFKeCLrxHLSkG68gaNPcPcQyv7mtlwKKMH_PXdULEBlfLV9VaqmQGSdw9JtCbIc6YW_PlO0jBmtb4eUOu_7H67O8Rw4rILpqMwQJy6_-kf5JLB1JpBrhU_kQ296Q9Kw_1D7_4rtCNAtHbNPwIfIA_6KH3kj5cSwit3zOD_toOlW5-xOtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ بابا جنیفرلوپز ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83178" target="_blank">📅 02:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی از این موشکایی که میزنن اردن کسخل شه بره بخوره اسرائیل بخندیم</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83177" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آمریکایی‌ها مثل نقل و نبات دارن پاتریوت شلیک می‌کنن
به زلنسکی که میرسه میگن نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83176" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">من حقیقتا دیگه بکیرمم نیست چی میشه، ما که بگا رفتیم چه کمتر چه بیشتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83175" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83174" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83173" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جمهوری اسلامی هرچی داره تلاششو میکنه قبل انتخابات آمریکا جنگ شروع بشه و هی حمله میکنه آمریکا هیچ اهمیتی به حملات نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83172" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP0hmfxp5l8yVbRDTA0wkPzd-dkSF-b0W6RnUuhKqbUzS-C63J3VOaw2l5AAGO-eZ0ZkbDa7R6TGDuiX9R0Tbn47JDgJPV6W00vSI17Swhjwx6558sbBfbiWLU6TahII3LeGGp88Npk74s56gfYkpk2S3bY1EKT3ZsaKiolSkc0bIo7-H-nLDldDWB5ZamxAn2U-WGEg01MzkVbR4qBDkWo-is8OnVhb90WshoqmFU7eFAYzeaVoPhruQX5dtXfvvA2eD-Dj-WQz9HdphxWEY95N-0hHFTxxHmoteZl05NKPWnMp9lbSx-Xm0ZBJGNxjyJUHW6rduD9O1cSCAv1edA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیره جان افتاده دنبال کون مردم از کل تهران فیلم گرفته، اگه قوانین کشور درست بود الان باید دادگاهی میشد بخاطر همین فیلما.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83171" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار فرم های امروز:
🟢
2.675
🟢
2.104
🟢
1.696
🟢
1.77
🟢
3
🟢
2
🟢
1.26
🟢
1.56
🔄
1.9
🔴
1.62
🟢
1.616
🟢
1.416
🟢
1.4
🟢
2.4
🔴
8
🔴
1.5
🔴
1.3
🔴
1.6
🟢
6.7
🟢
1.856
🟢
1.57
🟢
1.74
🟢
1.495
🟢
1.28
🟢
1.2
🔴
1.52
🔴
1.736
🟢
1.925
🔴
4
🟢
1.43
🟢
1.89
🟢
2.485
۲۲ وین
۸ لوز(۲ تاش کاملا ریسکی بود)
یدونه برگشت
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83170" target="_blank">📅 00:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHjR4kxzvqRjGm9u7qvF08SRUnw44Tw4r2PFrb17exHMr4a3I67WrGzdpjvW0yj_oYNkeJHB8Iy12MlmvL38aoUvBjr4vFUQ-Ah15-EFG2f66Vvm242bXw5UqvUExG44u_lO3qQ1arZQdxXo1HRs_umq5ANnsCusosLSW5MT9SJjt_b6A0a4CuOTTLkrWVGO1dvdFzPZ6HdwcQXj9PNhOi7yF6NjEykoxWHSRGFjFEZnY-5gOmaXq918xmSDZuROD-79HWUqOn5OlmZN1aRCMnPrOf_2Z52PvIIwlBy9VOS7l_RyppumRpoCMba1Q6NQEH6uadvtH10Aa9140JpWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایزی وین ترین فرم زندگیم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83169" target="_blank">📅 00:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از کی تاحالا پرس از بالای سنگین و استفاده از اشتباهات حریف شده حرامبال</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83168" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وقتی آرسنال حرامبال بازی میکنه ریده تو فوتبال
وقتی رئال حرامبال بازی میکنه میشه کشنده، سریع و فرصت‌طلب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83167" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83166">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من بشخصه فن هال سیتی ام، چون مالکش تورکه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83166" target="_blank">📅 22:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">واقعا فنای فوتبال عقب مونده ان، مخصوصا فنای بارسا و رئال، یکیشون جودیو مسخره میکنه که تو ۲۳ سالگی جزو بهترین هافبک شماره ده های جهانه، اون یکی پدری رو مسخره میکنه که تو ۲۳ سالگی بهترین هافبک ۸ جهانه، تهشم این دوتا که هیچ وجه اشتراکی ندارن رو مقایسه میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83165" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX4sZ_jeO44GZILHrq-mXSRR16rCvZSYJG-I1SNcTG7FcC69-xCgewEAm6JqxMXX0trDCs7gjenfukNcmClu44tpjR6qQO9Kgr5IKCz53_kig_XlcD6aUSJJUSGqVTUhwuZnlG9gn3NjWCD6VdOvO82yywWOGl0U7hfJBb5uCslaJyj2_-KAlzEibp8DSjNzWzbP3bEloSzMlVlpegQgCTL0OrXJLsS0p8Nn72HG9971lTMi7BAnI9nyAqX02AlcXEL8FJa4MxGg0OTh-olmF_5LGhEj80i-TfggOQI4D8Mympghdr6_XHtzhmRNrdww-NSXVT3NrHlvbLct-WvcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من فکر کردم بخاطر بارونه داشتم به خدا فحش میدادم، نگو باید به ارمنستان فحش میدادم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83164" target="_blank">📅 21:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83162">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به گفته بسنت ایران رسما از فردا ساعت ۳:۳۰ صبح محاصره هوایی میشه و دیگه هیچ کشوری حق نداره با شرکت های هواپیماییش کار کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83162" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83161">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کم کم داریم به فصل شاهکار هودی نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83161" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کم کم از ارتشی که قاسم سلیمانی تو خاورمیانه ساخته بود داره یه خاطره میمونه، همرو زدن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83159" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRTXKDXt-yU_3J4DPynJGQL43QSaICR81oUPOcymwrB2zONQy0nvV7E_OXD2Sur9wcu0PThCy2oRYi6HjaJr2xUjpGuDuYfTOZk6k7M2zLuPalIf4Z96rJirkTBU454CkIEQ7ZkPasxDh5YRXHJV7aSesgb8_l0uAMjgaSE5E-I5WfN3rJ0jlJ6W_nVkn4UFBM0otiLKhMC_ZwbnSs6s5WF7u2Ea9iip8RKRunviabjv7JKVgZgzvVoC3tt4xb5KGl8ydctfXBPaRWghWaqq_Axg4mQLfW-0YBnjRmOnUmVPSgbVvXQSXI_J4-beepuwXcjy-bdW_m7zgUbKmyOQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بین نتانیاهو نزدیک انتخابات اسرائیل و محسن رضایی نزدیک انتخابات ایران تفاوت خاصی نمی‌بینم حقیقتا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83158" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCgYhI95hQAgOccw9zRG3hkLz8XMB4XHRQJeYRZFnscuO_nFU3O-5jSEafnHZzDcepNi8-xMwGRl7kOye9w24F5m4xqW-BJogpo9mRylUarkJZrJOcsiHUNIXU3mI3bnPfOpsRoHf3_jesRA3_US8EJr4SOI_iEv2WAK-LTlyN6DhWqFANnHFxoEOArQkCXOi0dqkRVV-wxPGsXAeOSePavJEXQthgcE7LH6qQFDoCK3RPywseA8UCpzEOAq3kV45OhFu-3jksh8l6I4oqIbehslon5Li03kS9IXSSYnVmEa9f-aibOoH31bS55wM-ss344CkOL7Z12KyR-JHoo9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83157" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شنیدم رافینیا و فرمین و پدری کاندید توپ طلا نشدن، دارم میرم اونجا امیدوارم اشتباه شده باشه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83156" target="_blank">📅 20:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsTmopRTqmLC-HX2_Gyzk2jjaFzgUsIcIwt2GxwAvXtaC0PHq1OlQ9kM52qH2QNO_eQBXaBlY5HkJNV1SF_yfS-__NLzvArY4mjPkbGL1z6S6Ca4kvwYABUsvmk6QfuExkegaCTbZrPS9-6_bLTA9IW1Iklg4V1_NxY-GSI-VTDf5mwdyDG2ERss4N5ICPDalZZJejgHgbCNt5hAUoxT_ape14yQyGNEuLONmlDFgWQ3ln1FfPJVbr5qJ1w9LxhxDuIbgUbWACnfV5DCaZ7JYAuP9IbL_TNSWsYbTdPM4TItQfGHSscgeX5avfpc_5j3yz0b36dLd_kiNxdUCHtXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83155" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حصین بنده خدا دلش خوش بود که یه دونه حوثی‌های یمن از محور مقاومت موندن که پانچ خفن ترک بعدیش رو با اونا بزنه؛
ولی متاسفانه خبر اومده احتمال داره عموهای یمنی هم تا چند روز آینده توسط دولت یمن و آمریکای جنایتکار با نوار مشکی به صورت جدول مندلیف برن رو بنر
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83154" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83153">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83153" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83152">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzNT1iVHq3cuGjLhro-pgFwort7rkS2iJ22TLbe06QMpPMEM_w57B3hQHt1PfWhUg69zmxLRYuuoPZjxoPzlBQ_P7HgBQshdb0xmoTt_a3GOqjICyD8ZN2hVPmT44EtRUK0a2bOhmZZ-iNpuHTgPI0bxqk4Rdun8gRttJcP08MBSwErRFtzBHDqNSCwQ18tK-wpmTZVb2_n58QWk6FoR6EIJsCQ_uX6apeNnmyUhyWGyO6H3hRUanvZbvosrFLspU7lEz5WgFZYfLIB7Y2SKSzXX2Elfhq_C6p8s_ca2TUZ1h7lznlTO_d4jlD1l_LrO6WWyvE0g6zvglAYuVckf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
g17
🅰
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83152" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله اکبر سپاه پاسداران انقلاب اسلامی: با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83150" target="_blank">📅 18:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83149">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKPtw8jd844G-77mLDHpY4Ccj1HQBOMxyCCJYTLSrzr4EzSdaPXZdOZJl48nZoNv7D2RallsgHC5FMATcF8xnXRXLFrQyUXW82VXhRiaIVDNKaaR1xoa1xPLIdg_RtW7TPKlNGl_pvXoTavzZD1J6U-epa_vhdKdIxfVn8Vtd4Bs4dJgJokVCTAiIuqlgHubZPAvHKGsR_h-iqk5OSEfmrHbpHYdin57qJ2W3UqEH-NlpFNEInr-AoQofzyRXnymOIq7RoHQTsairdOzL2qubHzcViePN3IwPOScjzO2kVRDM9QK1rUqitpfk9z-JwqCJCunBLCKkD1WlvprXcT6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اکبر
سپاه پاسداران انقلاب اسلامی:
با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم بیرون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83149" target="_blank">📅 18:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83148">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKElmenJdk_CI3e26qdyVdN9IskPAOGVldkNbx-NpunfCkWt4Zzow10rdpVqZzInLlSYSeEZqhkc55hPCIpwUjARjx9KZe8KwQchQTMM2zjuzkhERV2P_OUQLy6RsD-VfaAOLDUFmkf7HB3IHquJnGiD1CRnoc7LFgNab7IXaVXHyx89rVd0-Z_XEx5HcxLeV3QRzP8M6z9X34ldFFuGbN_vy0gr4FGji4Cx6lGD1gNTYAI-if6DMvNjf1OlGCUI8ipmMeil_U_EkM2zD-0EonfrrGEuagSbtbjJU_anxgkvT1B-Kk_hRHs5ZWy34ECiQHJ9IfkzHfG-8FQ-ik438w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه می‌خواید کامل اثر بالا رفتن قیمت دلار رو درک کنید باید بهتون بگم که با این قیمت دلار الان یه Gulfstream G650 ساده اگه تر و تمیز باشه حداقل 10,350,000,000,000 تومنه
💔
🥀
(آهنگ ای غم بگو با جوانیم چه کردی اثر استاد شجریان)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83148" target="_blank">📅 18:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83147">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5G_K4TMtKV_7yLnfSPA485l-TqO6Yny3ySfNb4RPk8w54NFlpIoN-oLqEhk196nIelw8DoltjJcfAHtVqql-3ZUt-DQ7TNfe6wBEaShpmI1_rL7mgf6pjgqslp-fgBWUxoG8K4R4ef3wqDekMuN4zRumSZdvnCxrT5WQohMeDj0odnSVuwUBndSuM_T5XEXifcJpaESR0kSqd2PkIVnnlknR6mWLH-mC6bdk0ByhcSAZKWC5og7kWWLo0jXmnsXU8cFE-XPb7uawRg_vs3cRV87mRfGfrhXgZ3WfxkquP2BqNMLY7B7QHSqahHDzPVZN8VcFe2pHn10cIKOA4Nz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داکتر بیرانوند حقتو خوردن ولی تو فوتوشاپ جبران کردیم واسط
❤️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83147" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83146">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83146" target="_blank">📅 16:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83145">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پزشکیان بخدا ما خواهان انحلال توییتریم نه رفع فیلترش</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83145" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0xV00n_vB1eK_LhKR2qooI_gAx012rKtEfxgifwwsSjyBGjLmk7qlmkOxiH7K3GjxEHPCgNMY55sYAoAhN85085UwtpoRTPSRjR-EdMANsAESlPlU5fwyQG7hvXNJgX87ZbItgelzKDcFGtqEfU03gCLOP83AORQNUn-79uH8OErzDjTl6EHhwXuj3sqMu3bfiNALvIziMikjOz2zeVz470Fxq4m2SzWjuZTq1qLMSTnJQ7SkxFBQF92KlrLzVzTz96PEQsS3Iix26wdM6uQ1DEgqefdAi5WpIgYepEREquI1AACknPLbWxmRaY_Tfsj0_22gEBQXK8P3gRtc0tUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج این تو کون نروعه رو هم بستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83144" target="_blank">📅 14:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxuVxuilkdmrH3JiEWsJsvVDrg9tT8Xtt6Q4ObfPZB5kXDp952CsQoDHmBWBt0xXMJDKz9nriwYiq2QY1AfI4v3fnAg_qWX4Z0Fsu3TL7PLIgYmdIl3Xr4l_ChleImHyWjWXq37eAXga_4Ry4_FA1su-2ilkucGDP3y_fjG24qHTHTzAgsi4sEyyd6pqKGQb7rA1YiwXkhGuBHnIbFJq-cLkcLaKmvgog42PnZZb5D6BbPJfMgpDXEXMP7ElekdGW0mv3H5jmVmP7j1XXCVIMwddsEqdzaX-tJ__N0vCHkgLy15emKb9JZ-rt27Xke8D_wOd12b37Z6ZDZrlpA_pHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگانو بزارید بالای یخچال دست گوشیش بهش نرسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83143" target="_blank">📅 14:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سامان ویلسون درمورد معترضان به وضع موجود و حمایت از دلال‌ها:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83141" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فلافل قسطی ام اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83140" target="_blank">📅 12:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83139">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=vJK3PD6e2m4TyqGoEZAvromOo6fUInhvPN1tAa_xTGnEJtjDUtq1R7Fg2RimxC4KFYwk7iIST6g4de8CSXuJqVnMuK4KpE-JoHLKLyYtp4Xx-l3anAeQLdze4qidEJhjPS87McB710cDcd8_EzjfSA-t6G_1SCOLSThW4IjjnHSWzp9dCm-51utGVEXXt_k0wdh9OeGTPnAbjW6nf968HDcXqMDHXOObJpPHXXEW9Va4wu54u_ic1R6MzEzFEx0_m3VhP84ozEXgP49rD8bXSV1LcdXtJdOf_y4hA3A-qXyg-lK_vyKkawbAwPWdAhZ5TPK8Z12JENXxTMS5256lxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=vJK3PD6e2m4TyqGoEZAvromOo6fUInhvPN1tAa_xTGnEJtjDUtq1R7Fg2RimxC4KFYwk7iIST6g4de8CSXuJqVnMuK4KpE-JoHLKLyYtp4Xx-l3anAeQLdze4qidEJhjPS87McB710cDcd8_EzjfSA-t6G_1SCOLSThW4IjjnHSWzp9dCm-51utGVEXXt_k0wdh9OeGTPnAbjW6nf968HDcXqMDHXOObJpPHXXEW9Va4wu54u_ic1R6MzEzFEx0_m3VhP84ozEXgP49rD8bXSV1LcdXtJdOf_y4hA3A-qXyg-lK_vyKkawbAwPWdAhZ5TPK8Z12JENXxTMS5256lxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83139" target="_blank">📅 12:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83138">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور: فیلترشکن‌ها اشراف امنیتی ما را از بین برده‌اند. در جنگ‌های اخیر از این مسئله ضربه خورده‌ایم. تحریم فناوری و فیلترینگ در فضای مجازی نتیجه‌بخش نیست.باید با فرهنگ غنی اسلامی و ایرانی در اینترنت فعالیت کنیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83138" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83137">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83137" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83136">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydz6HB6CLjE_QOofxDEJBfZwbjoC41YX_d68KKmO1N7v4UVgECKnDbMIMrNEqV2bvwTr9S58E8MqWyCrsLV4Iy-snvvzV0Sgfl9I8x38toxwZCj2QVm_dtWXf7yDjzkO7MQHkHOUwaNbbtXQ_UVG5NQdtHS3-B1Z9iSiM9vJ06p8EzpuLTGfb_5zYQB__aS5pMfXMU_ytEai0YtI0sVRxT-SLZVg0JT2sR66VzQEvp6jiVCIKf4j4WPh_RxsVhxVq44iaTo626HEMoSu7py5JHKrTNMvZDyuPqo4Swlcm1KX5oJGjicS_2uTTBvHauqiUpFq26reSp2qVJCBVyCUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r17
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83136" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83135">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40085684e0.mp4?token=leMJMmY31SIhmaZQr9BOlGcLmBS2c0KbbxTgdK5tOzlYytl4-NhEhpNpKzkb-yaj4gPJnQ3HH5VfGN-UyRAlJ4RuF0R_HiDx2wb8T0OEPjcLI2PKKn6FJ3VfDznEKXHjbkenrZO9vVIFnhgajBvGBsAHfNjjUVpFRaiBFyqQ7rSH_nwKk4NJmzU05iCZ_zf6GruXWQHdfJ4XlBAKeGgBtqm2AM52ITzk-Q8BPaFOwzzrS_OHuL0DNBnE5ybmR-nwf7IxJhlZj_8UqOvAf3JFRze4t-k-dokIYHSyLWhPq098EwTiBn74BCsJKGxlmLZjja9a9sJ0C0oAboOwqfbBYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40085684e0.mp4?token=leMJMmY31SIhmaZQr9BOlGcLmBS2c0KbbxTgdK5tOzlYytl4-NhEhpNpKzkb-yaj4gPJnQ3HH5VfGN-UyRAlJ4RuF0R_HiDx2wb8T0OEPjcLI2PKKn6FJ3VfDznEKXHjbkenrZO9vVIFnhgajBvGBsAHfNjjUVpFRaiBFyqQ7rSH_nwKk4NJmzU05iCZ_zf6GruXWQHdfJ4XlBAKeGgBtqm2AM52ITzk-Q8BPaFOwzzrS_OHuL0DNBnE5ybmR-nwf7IxJhlZj_8UqOvAf3JFRze4t-k-dokIYHSyLWhPq098EwTiBn74BCsJKGxlmLZjja9a9sJ0C0oAboOwqfbBYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بخدا این چیزا تو اکسپلور من میاد ناخوداگاه یاد رضا پیشرو میوفتم وگرنه دلیل دیگه ای نداره که اینجا پستشون میکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83135" target="_blank">📅 09:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83134">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4_vnNlX5UzDHxPREzEICvcPz6N4_dAIpzBGF8b3k-n04NgTn8CWCklktPKpBqYV856zWFVKosT0ln8XQNMT6B1TfAcDZr0zlBWmIX13CgNb7BSyDxuvLfCoDkce_f02Ve6uDWIuJlyJ5j9zp_yTMopLUI8pw2f9L-xoOXavNsrVkOyGNak22iO02kKzv1n2hyJk9wiget08xwkYIE5pz3eX1IpjX8ZcOopeiIdYc-q3LoeyDFErbFlqSDh1bpRUDd-sV5Rfbsww20FTBurzGar_Nu0Ba-s-sWPLJ6-rRZyoJs1KCOFT-kYmba179RCsZcOGcQgreooCy8iw70CWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83134" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بنظرم که خلوت کنید آقای خمسه اس</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83131" target="_blank">📅 05:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=kVNqIr0F5FlO3MAHj_K8nDE6s0Xyi52BbVnC2Oftz8vKWN8WX97DcbXS0r4BS0h461fubXy8wfXjo6VHErAWkgM54qKzNbvSxTB_-sehnEaXt1vY5OwJNHXkQacZ0ydWaQdL6MwsbkVDMyHabCBO7an7Lq1JB6Be5R5puJiadaqexp1L9ub69bS_qb3Q13mGF4AmXU_8H0ZqUsmsqzZVgBmPm_pQFcG7pm3bhf-Z3HHJyyibJUCAYknfDeNLtLUE3mBcfsKVbPW-acVbqLnVUyKBJCnQnIcRcegWUr7M_pqVumWLyF0kKUyXcdX1t3rNe4Zlbj7uFpVJHUP0yrjJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=kVNqIr0F5FlO3MAHj_K8nDE6s0Xyi52BbVnC2Oftz8vKWN8WX97DcbXS0r4BS0h461fubXy8wfXjo6VHErAWkgM54qKzNbvSxTB_-sehnEaXt1vY5OwJNHXkQacZ0ydWaQdL6MwsbkVDMyHabCBO7an7Lq1JB6Be5R5puJiadaqexp1L9ub69bS_qb3Q13mGF4AmXU_8H0ZqUsmsqzZVgBmPm_pQFcG7pm3bhf-Z3HHJyyibJUCAYknfDeNLtLUE3mBcfsKVbPW-acVbqLnVUyKBJCnQnIcRcegWUr7M_pqVumWLyF0kKUyXcdX1t3rNe4Zlbj7uFpVJHUP0yrjJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83130" target="_blank">📅 04:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83129" target="_blank">📅 04:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=jT-cVpt_5-MhbZfpcFjpM_Jh9pRz_45iw-tHdpfOjmp81hh5zZHwxfu_NqCJrk5amT7cF983mNxRoWX9anHxaKNAkVbpELS2DYpTOz84-V_rtDhX5A-f2ujiXdv-6rYJbIpBuB1uAnoRYWpavzm5o1nDpWYl7MqPaZ4FbXNH8h9mqQ9_uucrfCpd-CwlCuXCINHtlyA_9kthNbt2JdZLC6rDPpBYEjAeRpeNtG6c5fv3wUb_D9jFLvahY8TBj1n6ZZWWbgGNf_IpCV207Hqz7cIR6FO_KF-4pnObynrjMxdrKAiTbss5a832nJtjDTtier7c52RCr1xa9lUx8s_vFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=jT-cVpt_5-MhbZfpcFjpM_Jh9pRz_45iw-tHdpfOjmp81hh5zZHwxfu_NqCJrk5amT7cF983mNxRoWX9anHxaKNAkVbpELS2DYpTOz84-V_rtDhX5A-f2ujiXdv-6rYJbIpBuB1uAnoRYWpavzm5o1nDpWYl7MqPaZ4FbXNH8h9mqQ9_uucrfCpd-CwlCuXCINHtlyA_9kthNbt2JdZLC6rDPpBYEjAeRpeNtG6c5fv3wUb_D9jFLvahY8TBj1n6ZZWWbgGNf_IpCV207Hqz7cIR6FO_KF-4pnObynrjMxdrKAiTbss5a832nJtjDTtier7c52RCr1xa9lUx8s_vFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که این ویدیو رو درست کردی دهنتو گاییدم
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83128" target="_blank">📅 01:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83127" target="_blank">📅 01:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83125">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83125" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83124">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d524cae959.mp4?token=YDxnMzbvZQcWiThW1EjlQ9jBsFnEbxeIb3sDAiAz6_QXiH8v9cFz6laWo0nap9hmt6-sSAhGnG4yH7tED0assGUbh9MdV8DLCyJDiAuwZnHOQRLGzhdVp4r-lRlOzajpbNNlNOUM6QNQHbcS8mpGReq0IN1aWk8QtPYA7RYF4tQM2S_oVtEfV0KeXgFrjZ9WZGUupt_64DdJINKA_3IaXENg0uwg_aJiO31JmLXgxPBvfuJR0DCvsN5u9A-balXvI-zsMjz2_VLyK9ANeldKoUPsMDSGj_-fM9IMXJmblVUSZFbH_9ZrAoN7NPKwEmfmcMa75LimZL4Ldjm5Q0SVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d524cae959.mp4?token=YDxnMzbvZQcWiThW1EjlQ9jBsFnEbxeIb3sDAiAz6_QXiH8v9cFz6laWo0nap9hmt6-sSAhGnG4yH7tED0assGUbh9MdV8DLCyJDiAuwZnHOQRLGzhdVp4r-lRlOzajpbNNlNOUM6QNQHbcS8mpGReq0IN1aWk8QtPYA7RYF4tQM2S_oVtEfV0KeXgFrjZ9WZGUupt_64DdJINKA_3IaXENg0uwg_aJiO31JmLXgxPBvfuJR0DCvsN5u9A-balXvI-zsMjz2_VLyK9ANeldKoUPsMDSGj_-fM9IMXJmblVUSZFbH_9ZrAoN7NPKwEmfmcMa75LimZL4Ldjm5Q0SVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینهمه هزینه کن زن بگیر، تهشم یارو بیاد برا اکسش دابسمش درست کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83124" target="_blank">📅 01:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83123">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83123" target="_blank">📅 00:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نرخ سوم بنزین رسما شد ۱۰ هزار تومن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83122" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید هودادکا به نام "دلی بستم" ریلیز شد.  SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83121" target="_blank">📅 00:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6Z0bIUAG75u0SKDBGAzHA_fjpq9RGP7SMYnxK_Q2ZTwymjIoOvBoYQS_dVjVnzx3bNpr_RmbtVCxGQo5t5XG8VvFzJyS20FSRWdOkWF0p3L9TQ9AqX-QGvdNX1u6gHyQwdeLrSXjCBq9alaDpCyEaSAEY66H7lKTk9g1mlQZcWxl0NB8DDuOr-ZxgNXS75cQmDUipFwAwsn_qqDI_3g_vraFSwmn-j5N15XtroP9IwRGqidPKHUnMwUgiTCaB2k-lEJ3SvE9N8c3fEAN2EinAyyBm2S8sHj9dBlXMiZkYV2H-PQdf2yTGtEvB2woU5pkyHaYnCOwibkDBuAW8QhHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "دلی بستم" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83120" target="_blank">📅 23:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83119">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7248d185ff.mp4?token=jWTspi-YptdwC_YP3MEqDt9-sxs_6mWnq3ThBEr5Kb-DHoWcPBP1Fr2OSRQEmaKZUNwEdM9i5a-p2ReE-sM_SR7lZuqfe5MWBjeSQhVBloaHH22TUDKtSD_mDtII61BnsigsDbwv26SokmTobT0kUFxkdRGSYEkikVJXqhy8240LYmdZuU5Z-7PkNqsqQMUd3CdASzQtLKNRjNQExClVeatiVi6VAdxeFQc9TtcBy1xj62jY1aHQyZjJNsPKPw1mcA6j7Uz-QFNupgTTUY2jrVRJ3ZSFJyCDmD5aTva9TbIAam-I57twuwq4MhgHA-wuivWG3_tOECza3REgm_AbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7248d185ff.mp4?token=jWTspi-YptdwC_YP3MEqDt9-sxs_6mWnq3ThBEr5Kb-DHoWcPBP1Fr2OSRQEmaKZUNwEdM9i5a-p2ReE-sM_SR7lZuqfe5MWBjeSQhVBloaHH22TUDKtSD_mDtII61BnsigsDbwv26SokmTobT0kUFxkdRGSYEkikVJXqhy8240LYmdZuU5Z-7PkNqsqQMUd3CdASzQtLKNRjNQExClVeatiVi6VAdxeFQc9TtcBy1xj62jY1aHQyZjJNsPKPw1mcA6j7Uz-QFNupgTTUY2jrVRJ3ZSFJyCDmD5aTva9TbIAam-I57twuwq4MhgHA-wuivWG3_tOECza3REgm_AbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر کصلیسه رو یادتونه؟
بزرگ شده ریش در اورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83119" target="_blank">📅 23:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83118">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzASvzJGNFrDwFaGHwyt3NVCx7BM1vqMmzoVD-uLXbkvAP7HkpuaGdSipBVjEserq-3eGb0T5yi-5LN5teAnKHe4CWduLKOGeSlfRxQtadgFlERzmeoh6Z_e_Iulp6njqin6Udfbsrz3CmX8KYF6-YKRIYx-5QuPaBO2mLMOtOAfVHaV2QF0KcmrvtVohRa1MeQfTB54otIk0_zEkrbr5QdLoyrWJF3u70ec4WHnaBhYZZljlmRUvPqW_5sifOEYCUVdVcGPn1LqEOzgtqoZjNCySpcW5lFlZjM_EXrj3Jla4VWBc1eEHFY3vdAUk_qNF98HMK7RbDKG5AsCw9OQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ناراحت کننده امیر پارسا نشاط
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83118" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83117">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYVGo9CYbHPvM7LmZ4DIqo_1-ifAnhovupawqcZ4lnROTxZa9AUg7oQJihQBAEucgSlAbv4a7cDgxI4MTSm1Jhy_1id1xRN8PGiwb-1RPX9cVDjxYwc0iVJTWTwTklQhup64-LDPuLLU3QpVcQKmy8Z5JQyLIwMQ9T7MTF4Nn-dHTCHmigFN2O6I1sFkWFy9EomzpPpyglBD0vZosQ8hDPBeHnWKKxzvVKAW0XzJ4gH2UoByD19rfx97-QzPlL2CfjfxVeVuoRnHn8cVE-9CntWZkRO6-lrNtF-1hX9j39_GvCBCeKnIdNi-EmhOMBWnXuxR5eC13Hsths2r5Xr8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایبرلیک هکر معروف بازی GTA VI اعلام کرد نسخه کنسول و PC  از بازی را استخراج کرد و بزودی منتشر خواهد کرد.
اف‌بی‌آی همچنان دنبال این فرد است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83117" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83116">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مارتنیلی تو لیگ عربستانم کیریه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83116" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83115">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbtin🇺🇸</strong></div>
<div class="tg-text">کیری کیری کیری
واتساپ برگرد تلگرام گاییدمون</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83115" target="_blank">📅 22:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83114">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تلگرام جدیدا خیلی پر باگ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83114" target="_blank">📅 22:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83113">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWh-jvd-WAr5exDw-8_n7D0XX7mIkab6i4af-go5M29RhEVrWsJi7VnK0jZyrBLL1Cx1ZLWyLPf1jEuRXN6NL3Da3wLBP-XsP3wNN68HgIDPUIbgi5uXjC9PNjskLZ_IDDnn7WK7ifapVhRgTx9-hShy4Z10H9WgEU_6fHqYAHa6MixGcrq28tVFavN1_SzQ9o4Q3H-5Epwh1y5DgoXvF0TkJGGsnSqfCinB4I-8nf2pffm9NmloPNqHtWpv2Opx1EmUIA1SXrv-i8vv10EmM-YP9-lZOwICu9Pwv6u2ZorP0HnjSe4FIr_erS_h59vEDyXh5cHR467R2uEX7TovrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا از ایران نجاتم بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83113" target="_blank">📅 22:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83112">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ffc27d84.mp4?token=i_VMk2xB-oMckTyYSKhW5gp3PKlFdxrksLVUqU8WU2jZBrs643ZzuPdPz_UYxIxR7-UZApm4E7cmimjLYrP2nP65ASBngUBdjrlW8Kgtpd-A50EPtwjValKjBMZcvvXWIkHlgdm29I7O4rtFZYYeUFOHmyawRX_0LfgyFTshlGieFgI5YPmvibRcmKodjQtZis3GRAi7fg9UXkdOLs7CweJA0BIcpeQwlz8tI-3z7swgxzI2CW1ttNMGKBNU-gZs_iD6Ee_To53_b95qzKZzD0GrpVLhw2psgqgqnm1-77W6aV3CCsk3vr4KeiDjpRy-fe2K1LEiMwZmPBtY7FTWEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ffc27d84.mp4?token=i_VMk2xB-oMckTyYSKhW5gp3PKlFdxrksLVUqU8WU2jZBrs643ZzuPdPz_UYxIxR7-UZApm4E7cmimjLYrP2nP65ASBngUBdjrlW8Kgtpd-A50EPtwjValKjBMZcvvXWIkHlgdm29I7O4rtFZYYeUFOHmyawRX_0LfgyFTshlGieFgI5YPmvibRcmKodjQtZis3GRAi7fg9UXkdOLs7CweJA0BIcpeQwlz8tI-3z7swgxzI2CW1ttNMGKBNU-gZs_iD6Ee_To53_b95qzKZzD0GrpVLhw2psgqgqnm1-77W6aV3CCsk3vr4KeiDjpRy-fe2K1LEiMwZmPBtY7FTWEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.  کصکش پا پرانتزی
😂
😂
😂
@Funhiphop | Menot – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83112" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83111">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB-KGaz7riqxidxJRIGkBaZhycekzdq299BfaO8jLV3ssWMYM_PrcHqoB0wA-uskVJnutyJnT4hCG9EWb6J2TFDWWMIhZP_IxjfAL-9JZ8A_-5tDksnHIugsoFbgAMs3aR8ufWpLL_lbCjDeMfV8X5JO3Wk8Eqietf12rp7VZkg0g9K2246yTCzW8hkAfzqpLz1Pod6msP4qrsGcaMTEAbawnKicwOUYAQIfL8ZR2XcSE5r3qG61RiP-s0nk5IJTfjpWPQNL4rtJOAA6K1ItJorvfZKpGlN7O0nEimrmS4K4a0yDqtvAbcGzei0yTZKMrh996660LGuePu5iH7R-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو با این قد و هیکل باید خیابون ببندی، نشستی با بلاگرا و رپرا تاک شو ضبط میکنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83111" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83110">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چرا از کلش آف کلنز حرفی نمیزنی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83110" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83107">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حالا کاری ندارم ولی آدمی که نفس میکشه قطعا عقب موندس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83107" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83106">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMpMV9AS367TIaJ1q_nUKgWTruvzigTU5OnRTnV05HwR4ROv1PxhIT_WaaKDlUQHzMRpFlX6B0EE-akGbg8TSBhOLKEhtKIphlxp_tGX2EldWBDt1yeknU8fdtSwoh4muenlNdevaX8DO9taWcJQlPrH81E_ZTqlg67LPuOa4T8jsaJ4sKfKVFaBIeKbH-UaTIiEWCr2EMNHiKq3USb7_11INmDfxSzkFDKNdrs3zMA-a_b8MjD0_fg8UGQKJGUkf0RGw5DiycmzAMyQPOwny48By4EMiK0sBWDSRlN8HzjGQOe9eHF3R__fWptvxc97cA4S36DZPaCz8iJRp7BsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب مونده واقعی این پیجایین که از هوش مصنوعی کپشن میگیرن میزارن زیر ریلزاشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83106" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83105">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZl67GCYcoe6A908dhP3jApd14WQPgUDKZK_U7hIemPyXO0P4HItOTXz244SRMKX6-Js8QbQJlJ7AzTzAxETlbmkkaT-loLTuOOA82xNnsW0eUk2pk1UEi5kyGkgpIHn_GbU-0moIox48y-xTNgIV3nYo9gzvJCbO3dZfmmBZMLLaqJTclmrzvNFZNdHivRjFHTJ4Kd-sx-yW8kL06-o98waDSAA1kMcpu9KenjBXqwyOawANgFQOJEWBDS3d4TiMvgL6-uCPh5SzbWJVxxl_qIXIA5YSk8uqKq3Ib2fSERNJGiYzcP1G-1QTLglEx8svSMNIFNpc_sa-UE826dgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت: پسری که اکانت توییتر داره و خیلی جدی توش فعالیت میکنه عقب موندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83105" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83104">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=hcXB6IB19KpcZXV8bIal5ljfHWr-iCMig6V7afKCrk1ZdMGMb8ba5_g2hWe_8Hqf7paTQc80DY2FABaNT8oQp2c6Gtf9h9cVYGxNNLGcoSWJrtODgM1FcV9FQbxm1co5CiqAFcXcaxzKjZTTQaVyhKrmErguLzv7FjO0opvI0jjaYOO3NvgZ1mtUVk8JUMx_fkP8troWd5uASfAUJZSlF0YPTrfOY9dPuWNlhsw5L3rowbWLUu3gF_FM2KpGj-ofAAdDoW9RFhpJdMEcD_qYHB7MVtphoZJA4astIiVofTcngR5hKYUuLPdRa-C4cjmdKCfPYHOevkHdAeDTqYTy4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=hcXB6IB19KpcZXV8bIal5ljfHWr-iCMig6V7afKCrk1ZdMGMb8ba5_g2hWe_8Hqf7paTQc80DY2FABaNT8oQp2c6Gtf9h9cVYGxNNLGcoSWJrtODgM1FcV9FQbxm1co5CiqAFcXcaxzKjZTTQaVyhKrmErguLzv7FjO0opvI0jjaYOO3NvgZ1mtUVk8JUMx_fkP8troWd5uASfAUJZSlF0YPTrfOY9dPuWNlhsw5L3rowbWLUu3gF_FM2KpGj-ofAAdDoW9RFhpJdMEcD_qYHB7MVtphoZJA4astIiVofTcngR5hKYUuLPdRa-C4cjmdKCfPYHOevkHdAeDTqYTy4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مگه ما اینهمه شهید ندادیم عراقیا نریزن تو ایران و به ناموسمون تجاوز نکنن؟
هرجور حساب میکنم تو ضرریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83104" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امیر پارسا بگیرمت کردمت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83102" target="_blank">📅 17:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شین:
پرتاب موشک بالستیک در هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83101" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83100">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAIMTzDa9aK8apK1OQYrzU208v9bZtBy5F9EWt5x6glrgRifokQqsmRivKGXGRTbiSSHRGCEXlK1R61NBHMIjW30kM0YrrGu_l5aKBqCf1r2N8TZeRc2ifsSetRhIYnqFWpDBPs7tsZ1Uhbe182uRQzHMSxeO-ZkEqbT5gsbT4TYuWs_O6S0DptnTCpXczWvmIw1HuGD6T4jiJoQ4R1VrdwVX_1cFQ7DORdP40LT3Wh-WgzIQxMOXGjNGQsyKheAfQMXhNDXbTGxF6NZzFbEyJb3T2jz8Hc0eScVDsms_nkbL4NtnnUt9d5lNhstjeCQYOKvSPNgAuRLq1zgpyUqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان بد رو فرمه پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83100" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XU07-xJeIkCuSi3qR40YzQ-dJ_YqP8pmOQYSR4npd8B7PU0A9BduDAW6hvxp8VF4gXhrhojLJrJybY_i1ZPA2dLmLVQdnvxhKnmO6wAzp7JQf-9G8ud3uyCz2Tbd2vFY0WO67YBHgXRqFuX4FHq4zB6gC4hzpxBaVr_2poDrPZjYgktfnIIe9QclbzeGCQDX1KI2ECxP7OKxS9RRD4Ci9XjHpfsm-RBl9VZTyXjOQkqttm5mv1b2IZH35LmXHRXHcWyJvcV5mfwhag7d6fncSe_cj4CioRr4SvUM0kl8Zx6zyPcco2bZ4Y0kDK-YalJUNwJk3sLW76rstZz2Qx8yJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان میرزایی، هنرمند و معترض جوان که در دی ماه بازداشت شده بود، دیروز مخفیانه در زندان دستگرد اصفهان اعدام شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83099" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ناشکری نکنید، درسته دلار نسبت به دو ماه پیش سی چهل تومن بالا رفته ولی نسبت به هفته بعد مفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83098" target="_blank">📅 15:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ویس جدید علی دایی و کیره خر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83097" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ویس علی دایی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83096" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=cB5JH5zm2OJ6D_sHOz2S8zzkQtYvTxu-CzwLc5hEPvrN0db33HPbFBwkZIlZvN3Fb2Kn6MsrXVLFF272Nd8FnOHGmeYHBrM-UQrYtTKhCkkU8NuzLlsbx0MbimQPz9gjcOD5Kism5q2f7pwH-QQIoTHwxX8mOYAnskpkCXXp4WoHZnuub0UnS1k6_2_kvR4VFZC-stF-MPzXd-bCGynl3aDS2MsQr2zdy0uRmwAz6q9Ay05Cggk9WCkJasF6jT5Zmug1ukBfWLftUBBv1FtzvmjhVxnuRBRc9bu_gw5ZtDXt2M58efPJ71g3If25vX5XCU1tGIUldU0YDL-lkGQPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=cB5JH5zm2OJ6D_sHOz2S8zzkQtYvTxu-CzwLc5hEPvrN0db33HPbFBwkZIlZvN3Fb2Kn6MsrXVLFF272Nd8FnOHGmeYHBrM-UQrYtTKhCkkU8NuzLlsbx0MbimQPz9gjcOD5Kism5q2f7pwH-QQIoTHwxX8mOYAnskpkCXXp4WoHZnuub0UnS1k6_2_kvR4VFZC-stF-MPzXd-bCGynl3aDS2MsQr2zdy0uRmwAz6q9Ay05Cggk9WCkJasF6jT5Zmug1ukBfWLftUBBv1FtzvmjhVxnuRBRc9bu_gw5ZtDXt2M58efPJ71g3If25vX5XCU1tGIUldU0YDL-lkGQPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83095" target="_blank">📅 13:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رپر عزیزی که دندوناتو طلا میکنی و میای تو خایه های دوربین باهاش فلکس میکنی و به دشمن فرضیت فحش میدی
بخدا نه تو ترویس اسکاتی نه اینجا آمریکاس، بزار درتو</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83094" target="_blank">📅 11:51 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
