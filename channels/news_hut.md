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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 17:53:23</div>
<hr>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVa4pik5EfxKduS_tZMDPZQZmR0FmuHUqNZPwjLmzCTCysUaFlXvbWe9RtnOeuVecweDvbNo3EKJ8SLNa7ceVFmHrIFwEVNDOc2umjrie3zAPvMAFKR7QdzrJPJMh5RKfv0xTbQgSfKDXqarxmMNjCNyLVv55PEj8zabG_ekIBddlfA9saLnlK66DJpq36Z_wN38m37rArC0WTewgzyp5Tqx9BMNe9QwUWVrNy0qvdTE2R89ZYgKFbDjNB0D7d3MlZAPF2jrJammzPL45Oaep72HtyB-H9aehmyqH9Mvxob2tmRJoTMebg8rBfYBvQc4WJxq3FPwHEi9AD2tRJPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhYx6bnAVroOoIUDEcnLljcxhNe8hxDSN1CsHaSeIenouILd2uBxEN35iOLtpwLBgQVSzJMde5AH3J7FMHeJ17Be6dXf9BsSXm-C3mRE7cjvwDuYjnyS18WMB-dGdCOBZ1PxcT8VLXofX4q1b7vUE0MtpBC30B5-stb7jF2QVPu_4iiiL5GIK5XGS1WUmDCcTYZNQKs3_ofBbD4CUCQ5tDtvhXbnD5XY9lENJNB-W9OlMw9Pki8wrXx4_RpAMTxyu6GOlcFLj4JOm9JuviODvCFzBZCqHyP9JFXuLOF4FTVOhuoJf9hV8bSgMtydZu9z5ZLmagKHKtwxvugnth73oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJJn9gM8OEL-Wy9GzVzbXm_kop0eBm6ncb_RsketF2hyZE82D59rBZuX2DTCRAwl5lAx6bgykV23BhUPxBXz1Yg_NXFC3o53-wSYdp-T7iqzOP5TfM9BWIpPydXFF2aEchRdowAAJzRW0eT1KPlYWnmUDrYuq9HH3is-WWsCfqWyeGwL1noKgenMWLyt_UCaD1zm3K34Hr7wn5QQQXgo75MiL0_ATLhWGQUp_HKZvak2Sax24i0xX0xfJM77mHL15_5eqLSsPc-3Gm2hR5Fc_gvl-8v2Z5KWWDpgVKRGbThCIZgnyCZF-j6QWD99rZz4SFPKBwWfolhmZx3m2Z0rcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuNBMKsztCCxFntWtE9Go0oZWamr6oy5ffPJtq5HdcUq-UEjFzsAxZ8y0cN6RbDWeMPaechVP0Wq9TG2WCPyRWvGopbkkxyLkBeK2Fk44Fz25d2zkcBO1qxH_twjufgsTgR1jOQeUQmk9BaTpgzQDPcZlYOq2snXt0HuTjwNxOK3r64k3oR8Bj0xo4oYp2Z_1V4WHJE3-ZU8PBrjSyA2Y3txDaX_dV_ogvyNUPtF888E4mtdZJW0chxhAUCMKznSIEs_on04KGs9zib0mErS0mNeA7iR01ZASabG_uxvwgWCXbSRfside9smgBQN5c69kMCtdYfb9zqEGzt_mY8-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=XhvxPJEmhgn-76YWVC-XEYzi62ECdFEhGWsdiKAMiQGpKiZCY2lBBce1b7dIjtHfSE-X9XFsw7zwFhdIoQUXgc4faE_l-LwmyX-7fwS6CKYF_TzG9eDpshwsoQ_K88dcOyQbmE-28fYY2-7ieHG4xpPvpP_Xz6516i--8LqsXXpJ-ppab7zLBlxlp1Kriyje5EakWFKduzEFgE4pBlyq5_Eg_dmqmeiRf_PPM6QGD5CXLSzEwynKfWmKBszdgSNv5F0onDl7oosMnjo5XX6oZaJVv7dI_JWF4islQPaZkBFhQFXgQe0T5XT01Y0oGk3cBF_UjWeNYpQDr0MIfeG5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=XhvxPJEmhgn-76YWVC-XEYzi62ECdFEhGWsdiKAMiQGpKiZCY2lBBce1b7dIjtHfSE-X9XFsw7zwFhdIoQUXgc4faE_l-LwmyX-7fwS6CKYF_TzG9eDpshwsoQ_K88dcOyQbmE-28fYY2-7ieHG4xpPvpP_Xz6516i--8LqsXXpJ-ppab7zLBlxlp1Kriyje5EakWFKduzEFgE4pBlyq5_Eg_dmqmeiRf_PPM6QGD5CXLSzEwynKfWmKBszdgSNv5F0onDl7oosMnjo5XX6oZaJVv7dI_JWF4islQPaZkBFhQFXgQe0T5XT01Y0oGk3cBF_UjWeNYpQDr0MIfeG5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=NxDv2qsU88Uht_eMdoupW-SKbUj4Ut1TasWu0b_Adhtjicd6CDZi2K80c7T7UF7MEEFxMfCkGQEt9Tqn2fQ7sfnBKM2OPrjumx94MBHqtLycjmGV5hbNfeZfajmCqkLhtromXXjyXFjjWOcm8gQmkIwMHQmZyXNan5tYlaqp3Bgai2yAzpKQjUkfHRy2DHAJz72E0e8WrJ_fPj3PJeXqCND4gZPwhu6SAsKf413wTAwr6LW0E3GsIQlYyXsUnMp30N21JXLynW9BkFFs0Ohb_VZtAhDh1ylp3NH1cUQx8JRVqN8LA58ysvU1Po0XEiUIvdTk1A4VafRVDcJJtoeHDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=NxDv2qsU88Uht_eMdoupW-SKbUj4Ut1TasWu0b_Adhtjicd6CDZi2K80c7T7UF7MEEFxMfCkGQEt9Tqn2fQ7sfnBKM2OPrjumx94MBHqtLycjmGV5hbNfeZfajmCqkLhtromXXjyXFjjWOcm8gQmkIwMHQmZyXNan5tYlaqp3Bgai2yAzpKQjUkfHRy2DHAJz72E0e8WrJ_fPj3PJeXqCND4gZPwhu6SAsKf413wTAwr6LW0E3GsIQlYyXsUnMp30N21JXLynW9BkFFs0Ohb_VZtAhDh1ylp3NH1cUQx8JRVqN8LA58ysvU1Po0XEiUIvdTk1A4VafRVDcJJtoeHDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrO7cSrShcbA7oEVSGy5OWRjzxGLCxF-edMDWKn1RPt9HA9KJVM3fXvMWYGyOQsPlN68UOuZ0g8AHCZgyZ7L3BWLKZtMlLzsQSY1x0O0QdGP7qSCPQLv0GaI9GUDiVk0GA1dmY-QquKn3M2ufhxBj6mgV7dTo_P12UOu8c6qVOv6_vBlLp0jPzhbm7XZCQh1DPPQ7kSRx7BqnELKKgbLNgcJHjiavAahFoarTXpMkfnAlxY3UENbDS0V1bja6AbgWFiYB539GxTZ0SpjFhldfLt2L2yEb19ChY_es5VRk8i1QiKevT7Ghc24Xg_jMvOSAxlKKD6nFUghENAHiByVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=umKYYqs3xCmoi4bzDn6Y9PrP8qaq7p2JatnN9NwnTpqq-wNll8a_j6yqnguDUBoW8DtZBMO5IXnxaX3S_sDITELshCoPS6UFKi-AktfNFvINzqOHzcMXPLl0WFziG06RlafOaw5S2U0gOmEDj8fy4Mdmi-PwD4nwHfKDkBGqkWqWjpnYnlhoSKLtXz4E0meV0072Yx9DA7fyaAHoTc47MJrH6r6pDtGCT46bdklBXO3B9V39JPYdvHKyN4eyzcpBt-iseDcDfn8RXzNvcjVQVg1P3AnzqUkqMSyr3zgizZpxYkdpc9thbtFWnMLEMqs9nrdPOE_X4DABV00S9h9O1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=umKYYqs3xCmoi4bzDn6Y9PrP8qaq7p2JatnN9NwnTpqq-wNll8a_j6yqnguDUBoW8DtZBMO5IXnxaX3S_sDITELshCoPS6UFKi-AktfNFvINzqOHzcMXPLl0WFziG06RlafOaw5S2U0gOmEDj8fy4Mdmi-PwD4nwHfKDkBGqkWqWjpnYnlhoSKLtXz4E0meV0072Yx9DA7fyaAHoTc47MJrH6r6pDtGCT46bdklBXO3B9V39JPYdvHKyN4eyzcpBt-iseDcDfn8RXzNvcjVQVg1P3AnzqUkqMSyr3zgizZpxYkdpc9thbtFWnMLEMqs9nrdPOE_X4DABV00S9h9O1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6bycQ0H_-bQHyYXuerZVIJXGJPtf5k8WsGXCSgJHv49PhG4nmXW-iQu-VJCQd7kWV55iEoHQ0ZOChaxQNIVrTDcT--J8rDU55g_m26OMG_NMnIZpPd0f6iFRIYFHk1nhbD4p8gvzjIjALxeOz3IOea9vWUXvSrv6ZeDqWRxgCcmcWD1rM8_Iz5Vsla0ptPnx77bdiM0EkQ-flrpXVVYi0HCEmtenVkLCLPkeQxFy3QSW0F96Jw7YioerOXieHpnIekFPoqu2AwO902ThPjSxMerVsP40LwQyS5TY0Q2LN_-f6eQZJKXTU804dKwVekKZ_IwRG4Ibo8HGvTu62LO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=rxpyersb4b-EBpf3nChAtKoH7_dkgV9bpB0bXz3ggjqAQwh_LDmTes51EhPGJFg8lQm0RDxmLhKshpsqjv6pMfF32raZG2J49D-ulCMgJy5ED3hcabn6MbdljaMEM6utKdpk1ptGXQjtNdzo-Nt_VlLrmRWCem1dggPfxH4r48D9coXBL-Amb75UOwrdVbNa9ahMLSCy5A9LxTgwbuvsAok23cmxPsw4JGNRD-T2eh0ZjuLKP8coHjlmtkVSmkNJvUEahdEMDp6FUR9m6UxUgN4YMVC6E-1WlWRFXnJCq3AHNMO8WrBNKf0A_M_ZnNVufw3UHOPLNtmp3tF6cOdG9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=rxpyersb4b-EBpf3nChAtKoH7_dkgV9bpB0bXz3ggjqAQwh_LDmTes51EhPGJFg8lQm0RDxmLhKshpsqjv6pMfF32raZG2J49D-ulCMgJy5ED3hcabn6MbdljaMEM6utKdpk1ptGXQjtNdzo-Nt_VlLrmRWCem1dggPfxH4r48D9coXBL-Amb75UOwrdVbNa9ahMLSCy5A9LxTgwbuvsAok23cmxPsw4JGNRD-T2eh0ZjuLKP8coHjlmtkVSmkNJvUEahdEMDp6FUR9m6UxUgN4YMVC6E-1WlWRFXnJCq3AHNMO8WrBNKf0A_M_ZnNVufw3UHOPLNtmp3tF6cOdG9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=LuzLlM-ESWl8Jc2CH-cWDbRbq2xv2onUZpmN7clJc99xktQzk6Y8vw-FitaRovWTAWeRUDCNuLAIHcEY6BKWgQrz5g6tO9lOBTh8JhqL6F_KuHj0_bhbnDTmnEIt26d0cZiLScjDcSOIemOT__P-4FydbqQca9t9dYQhg9welXN9rEuw-ouVjAKCNJawQv-EfsM6MM788-Hcpmo26IRux-bO83jy87ZFmOKPKUUfae-v2YLssphGV1niGfOd_rLv41ekLv_1ULetqsHQqNv5pMzv2h1GDH_cj1u5MLQrkE1rr1k91v_wq5PMvRVsjIOD9u07rWYSiZq752FM2IYVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=LuzLlM-ESWl8Jc2CH-cWDbRbq2xv2onUZpmN7clJc99xktQzk6Y8vw-FitaRovWTAWeRUDCNuLAIHcEY6BKWgQrz5g6tO9lOBTh8JhqL6F_KuHj0_bhbnDTmnEIt26d0cZiLScjDcSOIemOT__P-4FydbqQca9t9dYQhg9welXN9rEuw-ouVjAKCNJawQv-EfsM6MM788-Hcpmo26IRux-bO83jy87ZFmOKPKUUfae-v2YLssphGV1niGfOd_rLv41ekLv_1ULetqsHQqNv5pMzv2h1GDH_cj1u5MLQrkE1rr1k91v_wq5PMvRVsjIOD9u07rWYSiZq752FM2IYVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=UDrKenJXXo2WmxxdinEg3VeEJdExUDADJ5rrIIBSr8wQrGiEVEdjaW4RKp1FdZGYpq3fCOsSPhKBt6xENgIvzwl5I2acwUpC4UFdccnsCswR4Ap6FEv7vV6EmmYYVetqqpl50Sy9cv5SYF4vyywy9IxlTfr6NXOoBQwllg3TcKK0npMC7ajDIKQeerF4BK4FeSbzCuCVh3nNV0gXmuXw1Hue6vuCcH_i59COO4JnGt9ypJahzVcbZJpGvEnvoyUtuyKjsN5bOC0eCXr_EPAjupemUBcPtqt3wsB8IqjtL_3dC_A5ImJMEMYSf2xPZPY9nJ0pRiluMr8pzLym_xbR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=UDrKenJXXo2WmxxdinEg3VeEJdExUDADJ5rrIIBSr8wQrGiEVEdjaW4RKp1FdZGYpq3fCOsSPhKBt6xENgIvzwl5I2acwUpC4UFdccnsCswR4Ap6FEv7vV6EmmYYVetqqpl50Sy9cv5SYF4vyywy9IxlTfr6NXOoBQwllg3TcKK0npMC7ajDIKQeerF4BK4FeSbzCuCVh3nNV0gXmuXw1Hue6vuCcH_i59COO4JnGt9ypJahzVcbZJpGvEnvoyUtuyKjsN5bOC0eCXr_EPAjupemUBcPtqt3wsB8IqjtL_3dC_A5ImJMEMYSf2xPZPY9nJ0pRiluMr8pzLym_xbR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIvAtVKWQrCTZ79Vzsw2MchdGpUsl9tVnCaUpy2achFD5nKZ9onCI01c2FYfouv19UwYAWJynGpEcNgOwERx0V-M_ZztSOQk_ySL23pgjLJIQvQOT0A7FwHCv0ty975tcjFuCUN72LTJdPsbQ28CjQ-BsrEA-JEmHVi0p_wX_ldOemjsndxvHBWjxJmyoyB-f09_UmQio6xTXO9STIxSrggjIZbpI2w5UC14JOaO8J1xEb36k6cPDqg2j2QJOd1ep2zO_CPAWaj3hZZOtJGEFG87qWOb040vXu6iOzHYCtMw3GEvkYC3INCWO2llEkkYrBCO-fR7o6r1hgDehEzsfA.jpg" alt="photo" loading="lazy"/></div>
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
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=E6bCdDRjVVwEjTDPTrvVnkbN8ZLXzxoHsQGmL0rYAtxi7rWv35V9ZjtnX0X5qjRGjrEjrfIK0ds4SC5EFYqSJajrqKByPQJ05ljXWQwIg1dl3nQKnu10BndBlGSvOl9O9BMcxFZ0DhEtfU4sZhGx8_fXpNFQJ1rBGyZR0tDD2u14L3jlvODO5FaDc3BVVjPdQlbwISUqYYBKWj8iEqnwrzD5ADPyShI0GUYdbCNu9fMA38i1kwaEdm9XcG7P4UwrYoAqEbyJPPKP-_qC65VINsCuJt4DR4jXDvWT5A63ixYfolW_NgfvnAA0gUeg9vCgipuQg96LE1sJl3OjJsZECQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=E6bCdDRjVVwEjTDPTrvVnkbN8ZLXzxoHsQGmL0rYAtxi7rWv35V9ZjtnX0X5qjRGjrEjrfIK0ds4SC5EFYqSJajrqKByPQJ05ljXWQwIg1dl3nQKnu10BndBlGSvOl9O9BMcxFZ0DhEtfU4sZhGx8_fXpNFQJ1rBGyZR0tDD2u14L3jlvODO5FaDc3BVVjPdQlbwISUqYYBKWj8iEqnwrzD5ADPyShI0GUYdbCNu9fMA38i1kwaEdm9XcG7P4UwrYoAqEbyJPPKP-_qC65VINsCuJt4DR4jXDvWT5A63ixYfolW_NgfvnAA0gUeg9vCgipuQg96LE1sJl3OjJsZECQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9p-xBA6vytr5jkxNFPTi32EMazfaMYdIve8mDA1iAAGqnszh2AWR1g8XQUyShyw5puTtwZiMYjGZqNGjzCu4muYDnlVrF8kbBW2hQeE5j7WKQp9_2E45Bj-NI2uLzhPXiNH8Y3S_6G_MvkzCqkxv4kxsxYdIxVNOuBOoFucYj678uHezuVb1QWWe6FR9D3isCYVqVa7eYXYOOyr2-iHgVDzySiEJ_x0uaZ7aSfjPPL0FpCXOEvjHhisEIkx9kIJiMtN5_PUgr0PWheh0MGywZAQLn98YuquOHsl6c0juQt9-qAomDp5kPXuI8gRg3CGX7OrmanK0G6liAeftQNiSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=UyE9jiQLVTOaYCnbNLbnppsX1Le8XbNRaaQ-msYwCeklaGJK_DfZ9zPyaKc4SIM7YTdj5_575HR_H9DINfaA3tlf0Peen-wZNfGRTj_hRdBbTA5Njok0on5cKAJLHtxd_ra41-NWFEwyHD8DgC8I1litUoo-pmjFz9j_SEeFDjMBDbtAobQQeNCKNr5FNtt-Ynutf6VecU-BYufKGPM1DY-XKhC1e58r_9pDO-CNxX5SbWD5CrPu62-jKa0CHx-KRWhEh_gDY1FMgw6QgqJyaKDTlHlZOOYrow0SW6tBndgFCXn_30JrdvPNrF1lY9SwPBjzpzVh7Et7pptByCgO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=UyE9jiQLVTOaYCnbNLbnppsX1Le8XbNRaaQ-msYwCeklaGJK_DfZ9zPyaKc4SIM7YTdj5_575HR_H9DINfaA3tlf0Peen-wZNfGRTj_hRdBbTA5Njok0on5cKAJLHtxd_ra41-NWFEwyHD8DgC8I1litUoo-pmjFz9j_SEeFDjMBDbtAobQQeNCKNr5FNtt-Ynutf6VecU-BYufKGPM1DY-XKhC1e58r_9pDO-CNxX5SbWD5CrPu62-jKa0CHx-KRWhEh_gDY1FMgw6QgqJyaKDTlHlZOOYrow0SW6tBndgFCXn_30JrdvPNrF1lY9SwPBjzpzVh7Et7pptByCgO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lievNzdTjBqLCq3bISKSGOw4zZBDeIfYxq6gmBZyXO-w_OCt1WlFZSftjfLC7Bljg5CwF2y4LLJKF1i-iFBUI5jCWcoe3lWRTW72Qiu-gBLzRzPjVRK2Xq-3H5i73z6Kub6DKFYIw6zWGrf2IlTf9V8UyJ_xn3J-KvMNfBkGSdZW3jxr2hlbnbOcFYCmdaTfZfSACYXSGszHw54SVwpJJ_CHcYiz0AfVzhv7Kj79Djb0GAS_d25QMaOE4p1sobNUJeH-EVThFDWFAs3Wr4TcyChfd0nLwIsOTQJHJah5VGJsr0rfZ39rBksaS1y-S3pbDEy8uvET1J7vckxzcA9tLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opEonX7O9msLDpaVCCsVHTAgQFRxUMZIyYjAgpCCx8NE3Ni_UQmwM3MCbzLsI_O2m0TQIuuLEbdWWsEVCCwNce0Sv7fsOFsuBIAhmPnRDcGm6KzZkN3GOjrM3lAmvreiRNzRAVg1YY47Z_ZLe63CGXLkNQlOvWVjk0xPNImzED5OUnQOQJSCJgdM9oeKt5KiglhahWwrYC-kHdPMbqY-2OVXHvJtDx0Bj_uwlgkJar-74TANqCv6FTVMAPNQgW2iHAZ-ZhRdyS81yOwpHtFCHp7S15f0rCLJdSqHpDsIzDd-XUG68kGQvX8jg-9Fv9vuFTWBSEYSLxcuhxV-HL9Uww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtrzXZJoTOTFGsyweSQorRy7IAWPR7NcNgl2pIE20pfeob_8T4QqgNzIJzSbcU_aMdXGT4W9czcUfkSzp7eoYHOZlvpahVQFMGCDQFrIkOqp2FBoZRJ4iHZEFiFdz9RcY_0vyU4hUd0zddTiQw-666rs3gSh-C293-voHoA21qU-SOjCExdPILuOdDIzP7cr-n4l9Q-w1T_wtFB775og8DicTkoVeUGnKSGdJuZgm98Na7BwIXIqLh4shwftGk2i9_Nd82nYHAH48JgyMFE62GPRd17bqGJSNULfnB6DUBigrlKjsgWAZFjtHehonRHqL3o4sRVbXLKItkt9Jb7ZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tm1qDPmebYsb90AJOBVXtA6gNfzbGBbf2qCe30ZB0GMKOeVe9DLGPPcmvZmkF2VidzGUGosUi5e0i3FfRmR160tvhZ-_mJU8mafns2LVWN9aVSg24ou5hdSfxyXjIGFVZyPdCjhy6enQw7EeE2AHw27bNF-le0CZZ4Lf28PrR_7KiNT3GGrpMwntQNIqkoH3hNP_6TvzvdmkReiDQMtyFYCWQcAFulRdPU-UNGrNYblhdf2IqFWVAOFOCsKSxA9Juy4yoyeL2iEUAATI0384QYJHH8niYWqx58iYlgKM0p1TqczMuLiY95aH8392KnRYyL-FgOW4CKijh1sxMC-cDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao98MGLKwel5zQqzGo3IzlHUOC7lm8V36iBz_zCOSfO5Cfk0_N4Ti6i_ABWUUMp_k-SLKNhJt5lR1Z_FWALlwaAJ-B2ZIfM_1wtNyulb6YCkhP85G3OFoQzFMI07aW0VrJGgiWfd6NgmU_506Ma3RqtSJ863cEeFOquvAXHXT66qjqTDjJx0gl5-zSjzMT8q--1cGthg37l_J35diFETp6LZrwCFa8VWVnsEy2vlwceeS-CiS9fHiW1zjqHz3nUc4KmwvA0lFMJyXYnzoY2eIEsZ35wwXrPkHu-nPp1rDfVarpRvbUvzIaST4C8U01b2r9tFjQcFlGTB2bQ0k5JWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebISzYVS8KqOc1wj9JstSIsKVME3v5CcF3E-nhJpiiTZCL0Qhh53Llu0pQ1lXIZPzG7Q_VCCdr2sk9JpXMj3KeosfFMub-fjOFvd8vZSNAIDKs14Vot-DvifFxl9RHgKclJajAoGbQJF8QQRjMNrCOB7tcgUQGXlYXh-6AQ0NZ_sHe98IqRb0ITnbFKOHbvhD4McEPJwNYWhb8iVQsvpUOM9AY82XItGD-4vA5f6-Xu6Xz8yce16ZU_d4DfxdXrhI8dyOeiacsOQrqsqnTf4NbAfzmAlL3H2mYAs6wrAHEswolm0etsrlpZ6icOLyHhqempL2Dt-haxaOHAH_x4jIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAESC7mWD-S8w6wqqKlbum3Qj1yGdkpES6dnKE9pDRxe6w6rgb0VE_bqNLm48dPZ0puQlZBTWNkK3Rd4wAANUUOaYcnqMMV2HDyUECH9KYrsUqg9V-r8LO4G4Mt_XSmFwcgDFXb8aNQj3CsvliHA4moH1x2umsyeWoBDPww2Jv50DJD-jfvLfFI-haJFMg4rr-pweRf920NB4-B64NS6SF90WggbDmFdsug-qFCkDFfsD16l8PjVRSY_nczvTiWih8Fq_pvtzGA_JAaduNmDxqpwVW3z-cCgJyOsisVvRLBoBJZV8oW-QV7d34-inaicf428Fquu5_1Ig_UZtGwH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=l8L8IxntZYVtQVNkvx5-Nq_GwBNyxe5doU5w0iICV7TDOwSSHT3dnuN4YJy_n_h8uYCYdb2lYTK6qxOooPM4DOvvl5jGICXYUJnERG4f9BEfS50mbnY0yiYBfn5ZIltGvRaXJ_8ij7BAbk2v3tJ8iHIi-KHaR47w7WEbnorn_q5EbesK5GJb0rU93dQPZa7_YquO1wb8s2xaGfi-C6r808JHEuNoqZhiV-9AxuesgG_wgwJCtKr6BWueFo68Mvti9pIRqqsWBgzTBUCSzZMXbiZvUTJj1xczc0U3chw5iwWw5FY3JvvZKAUQWjbuwYCE2q0xZRBVgXPjL5cBc28s3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=l8L8IxntZYVtQVNkvx5-Nq_GwBNyxe5doU5w0iICV7TDOwSSHT3dnuN4YJy_n_h8uYCYdb2lYTK6qxOooPM4DOvvl5jGICXYUJnERG4f9BEfS50mbnY0yiYBfn5ZIltGvRaXJ_8ij7BAbk2v3tJ8iHIi-KHaR47w7WEbnorn_q5EbesK5GJb0rU93dQPZa7_YquO1wb8s2xaGfi-C6r808JHEuNoqZhiV-9AxuesgG_wgwJCtKr6BWueFo68Mvti9pIRqqsWBgzTBUCSzZMXbiZvUTJj1xczc0U3chw5iwWw5FY3JvvZKAUQWjbuwYCE2q0xZRBVgXPjL5cBc28s3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVAxwbpRuEmMu0iACb7NVJM65G1FxADeSfM8v-jNnZU9WAqV-trgy-hu-ktDco2aPafA8dSZHpkQFH26OfWiKST8hCVyR0pfLRzukVmzl77mXelvfmQVlxJVOGB0s7yKgqdM4iUe_eCrRRaPlg_-OaSHuM613JndYchTRiLHnISsGddNxjq2C61vXIKh1FbjZbSDg8SJ5B17UX_nRo44iM7Y6JYXxjdLHbAWGhf72iKj9RXEi0lYeX4_ZaSp4WcRP1jmljXYlGnJNpZQzI_-xQGJ8-O5ed0R8Tb3qU56xnutRdYViZRQd52EFFCWLgftTERcP1aSrGg8Ke2QHPhxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=RZvMYwTO7d9yoNSXr_A5U0i2xePuYAjL0wKsDhUGC5UTZN1FEyR9BGQRS3fJRYKr8EjNIJXc0VGlqD8jtx8SFrgVmwqO1WnjCs9QN_SU6ZNe5qD8cnIHWH9m8eHockZS2owIxt4XvCk23Tlf0C7URfzAXJBaYi-sABWeDK2oskKbaZdmDe3HlR0EhQeuGhFXzZdtCoSk5TCwwLQ3GlTO2ss2toZsopOeGh3ECINoeiYVn6qXpLbcCKpZj2Z65OddSwGL4eSFQw-2Fdxvw85NOxilsEQv0tjr_R-UohZvAZ8p23pmGCtXSPuKzvWVopqLYQIT5heMnEtbcnaUzXApiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=RZvMYwTO7d9yoNSXr_A5U0i2xePuYAjL0wKsDhUGC5UTZN1FEyR9BGQRS3fJRYKr8EjNIJXc0VGlqD8jtx8SFrgVmwqO1WnjCs9QN_SU6ZNe5qD8cnIHWH9m8eHockZS2owIxt4XvCk23Tlf0C7URfzAXJBaYi-sABWeDK2oskKbaZdmDe3HlR0EhQeuGhFXzZdtCoSk5TCwwLQ3GlTO2ss2toZsopOeGh3ECINoeiYVn6qXpLbcCKpZj2Z65OddSwGL4eSFQw-2Fdxvw85NOxilsEQv0tjr_R-UohZvAZ8p23pmGCtXSPuKzvWVopqLYQIT5heMnEtbcnaUzXApiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-WL1Z_AkE9_xbQrkCXAlItno1RSu7tyCnkkvyCEIynbrjkjT9gEIsG1CRBPXcFHCq5rnXTY3-NfYjZZR-Rm1IkIk3aYMs6yRPu7leVWjG2Oo1lzgqy18pgLsj3KJb_GPTupgUL2X2f2VXvEOL3d9bJzONoKxwLXpMr2MtRCMqVCo8yDWZyWmv-C74wCaoXrAiemIxY-sjROlwmNVvyUDt2c-SHWUOfS-5253--SOAd5aM_m1y-O8lhsQu6tFUNXu_IaFaHjCMHVYRxLPXkgBYcUhm2PShA8feahmaT5_ZehVw9e58AHTq8ENxy7k2IYMO2l8i0dOmx2boTO_v2c2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anIDTqmIorVAqVqu2rCfVJLUjZ9HgDibwxKG9Wch-512xQtqwd7xpHcYjlUydew1nVV9Rj7sXnd9g3yLUhreadnxDG8snOehZ7mOLL-n5O2D9iX5UBFCAA-caYdnXw6dv2VolMHC4v517Sk92A9HeRP3pYU_YVaGsK10H-KJGz8aXnLGLWiZIAspCAItGJlSRicSlTnFx_PnGsvrZhwTQAaR0uy2e7YRvXffJv6e_TnzNjaz6rJb5wp_YKQqBArAEu4QRdndcTB1VRdnq7l2PMnCialUqUuQVw14BQJXHxxWodb_bhMRz6EOkQ3KDmmsxU-oZInV0wkZ8rcd8i25HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=So3bmr6kmAv6Co6zvA6IOWZX_YOaMTQyjvdu_ipZTedxCuqCYkO4aLUgPU41kNbdXBG_1tk2x75jpHkFFSulwYLh7OHRSznPevM6BOwOio_dDktD9Z_f-D0QFpcuD8lO2JHgzzn8v2uo9Zwz-BsbfW6Tho13G0HQEVTV1uEAbqEbHQEGnSfWZm0lrNJADV_nraWCSZA85eAiLFs1tNrbc67-zZCa9nMV0spSXl4Eazg73r-j1WKvAjk0mGD0oB8t8sYLTdEad6-NKni3jAJGuUy_LCT9uIpKN0yDZGrdrB4wvOLxyQaw2Fzfv-ujDNBvjspO7Shf_Qm-VcIMAQbcCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=So3bmr6kmAv6Co6zvA6IOWZX_YOaMTQyjvdu_ipZTedxCuqCYkO4aLUgPU41kNbdXBG_1tk2x75jpHkFFSulwYLh7OHRSznPevM6BOwOio_dDktD9Z_f-D0QFpcuD8lO2JHgzzn8v2uo9Zwz-BsbfW6Tho13G0HQEVTV1uEAbqEbHQEGnSfWZm0lrNJADV_nraWCSZA85eAiLFs1tNrbc67-zZCa9nMV0spSXl4Eazg73r-j1WKvAjk0mGD0oB8t8sYLTdEad6-NKni3jAJGuUy_LCT9uIpKN0yDZGrdrB4wvOLxyQaw2Fzfv-ujDNBvjspO7Shf_Qm-VcIMAQbcCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=U0CvTZ3xPgcKbOMI1gR4rj7w3qD6FPYPpsqQ2VA48m65b6PSitt49RFSW0KXV57Brv0xwX-9TcsvpweQgohhgO6VGCT4EXGtqPO5-l0VchjNFTVflTTJ6O1Kj_by45ELTalhdlWqKMTCl3BJj6tEXaYO2cWcEwlhxNKbglKvlKe-ydfv0akVcW-mz4m6PCPM4V_a0rIXpzHTo17eiB-XxzbFVlcIW7dgjyLwuoiPZDMHeluMmGivY_hCMfmz1yBxa0SqgI2C637dRw55Ba9-fmsMmhd0jYlx2lUF8FafFqjHVVgmYvcVHrbxePDeJyjDOE_jq4S-sMOk_sthPiGQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=U0CvTZ3xPgcKbOMI1gR4rj7w3qD6FPYPpsqQ2VA48m65b6PSitt49RFSW0KXV57Brv0xwX-9TcsvpweQgohhgO6VGCT4EXGtqPO5-l0VchjNFTVflTTJ6O1Kj_by45ELTalhdlWqKMTCl3BJj6tEXaYO2cWcEwlhxNKbglKvlKe-ydfv0akVcW-mz4m6PCPM4V_a0rIXpzHTo17eiB-XxzbFVlcIW7dgjyLwuoiPZDMHeluMmGivY_hCMfmz1yBxa0SqgI2C637dRw55Ba9-fmsMmhd0jYlx2lUF8FafFqjHVVgmYvcVHrbxePDeJyjDOE_jq4S-sMOk_sthPiGQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=eUkkRYJml9NsGiIw1NiKfZPIm1rPoDNwTj7jBmW5J-eslmGlOZmgErWe8GZ82Dj8zu_gB0W6MZcCgBBiHBOYWKTUHZvrHrGNiTMVoclGOMMdxtL2vbhXzzcnonqV90IEGDXGgqdWRah69tRpaflHQiYUbFgFryz9cTj8mFNgb3Sggc64RBYTyxR0VGztAZATuAanOqTl4PJrC-BE9g1FKun1boRQyRiM3bYNYSKswnmL7fusbQ8xbJslWbgtB0TnZK4zDDMKxEiVyN12kIsHz8naNbE3jrkfHr9Rac3qTysyn-LelpO6ezRuw4CpvKPuVI2IHcTKAVH8xd-g6rCtEZUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=eUkkRYJml9NsGiIw1NiKfZPIm1rPoDNwTj7jBmW5J-eslmGlOZmgErWe8GZ82Dj8zu_gB0W6MZcCgBBiHBOYWKTUHZvrHrGNiTMVoclGOMMdxtL2vbhXzzcnonqV90IEGDXGgqdWRah69tRpaflHQiYUbFgFryz9cTj8mFNgb3Sggc64RBYTyxR0VGztAZATuAanOqTl4PJrC-BE9g1FKun1boRQyRiM3bYNYSKswnmL7fusbQ8xbJslWbgtB0TnZK4zDDMKxEiVyN12kIsHz8naNbE3jrkfHr9Rac3qTysyn-LelpO6ezRuw4CpvKPuVI2IHcTKAVH8xd-g6rCtEZUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiI1UkGTx67UfzwqsBshwAwcPj8IJbPjl3w05YAcoCThnu13LCzmIaQ-3_QBKwa-dWxRDsRM_ATDYpo46R7FKSLQ55vagYjit1I9Fxh1hQjUS8RwAsKbWs-aIkrSBVVNl0wZG7UUAMi3LKMAn_voNWmgD0RUZBLstHtzTPDIemS2PTkBDj1qifxHxvM6dfnjQpDoJt_TZuwzQnbDr99D-wQR_S1w1lWFkMhUG8CYYcvY_AtHZZy4A65LmejdmNwMg-CfDV9u_9N8j9XOYIcncZX72L8ziIFdBfG7swzqjpvip5-HzVf9RSroBt3gw5JMlTFOKSldWkFKClOnW9UPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=aMspu0p63H5RIYhjeWeWowq5I5VlRVJnnh0pEgCXqUmnU3isqm8cL_sbXYtSC8p97UKaX5OHYqswCcP4HLf32Pj6oydpxQw_ZMySAaAI9fsi6kPMs8KCxnmxtlH6wBwlcpV-3VnQmSYwTgwO4UpBNqNVe92SuPTXfXsL36DR_DnwuuX7wDMZwqo8JgBeQpRUke0sGMPh43srieW4rE2_m6U5vo230CMj6PsRZHAk-UPi0enj8X-uNbb6nTz6uJ9Oitg88WKsMMGuL8mZw3TMYfYXKf6gjB8v_PRs7RbNKPzSqgYHjxnUOoW02RRLIlDVVqs2rFmMp-6xzVDIvLW-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=aMspu0p63H5RIYhjeWeWowq5I5VlRVJnnh0pEgCXqUmnU3isqm8cL_sbXYtSC8p97UKaX5OHYqswCcP4HLf32Pj6oydpxQw_ZMySAaAI9fsi6kPMs8KCxnmxtlH6wBwlcpV-3VnQmSYwTgwO4UpBNqNVe92SuPTXfXsL36DR_DnwuuX7wDMZwqo8JgBeQpRUke0sGMPh43srieW4rE2_m6U5vo230CMj6PsRZHAk-UPi0enj8X-uNbb6nTz6uJ9Oitg88WKsMMGuL8mZw3TMYfYXKf6gjB8v_PRs7RbNKPzSqgYHjxnUOoW02RRLIlDVVqs2rFmMp-6xzVDIvLW-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=EYnOcGF27KpvbOvohb9Yf2d2PpQ8mjXVBvMC2OV_5EfOv4DPBsWTptfqL_tozLiMjELvAMOIWmf59-EpeTZLj02kUsFf6qdXjK8c6eK2o4NvgHtiSLh1SK-s0CFQOoiRctDu5tlXJOVGM63j1PpOZJmn22TRAxHty209Z0cFnMg4RbxxqpIeumo3jS4cPHBVsBCFF_tmULbjKDupvsFShHhHUm4LOV3-lA0pVpnkKfgaJAvSvxtBVA6cKD8JJqm4MO098k-IWk9IHXkEWs7pq6Q7IIIJ1fuVyN7vhlwx8lijp7af4SuHj3uXXDLjhhW4KeumIvGKYVQS-52GexGbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=EYnOcGF27KpvbOvohb9Yf2d2PpQ8mjXVBvMC2OV_5EfOv4DPBsWTptfqL_tozLiMjELvAMOIWmf59-EpeTZLj02kUsFf6qdXjK8c6eK2o4NvgHtiSLh1SK-s0CFQOoiRctDu5tlXJOVGM63j1PpOZJmn22TRAxHty209Z0cFnMg4RbxxqpIeumo3jS4cPHBVsBCFF_tmULbjKDupvsFShHhHUm4LOV3-lA0pVpnkKfgaJAvSvxtBVA6cKD8JJqm4MO098k-IWk9IHXkEWs7pq6Q7IIIJ1fuVyN7vhlwx8lijp7af4SuHj3uXXDLjhhW4KeumIvGKYVQS-52GexGbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=UcnbZvqqlXo75CXNp78B9V3bYVmtI_lhvqihkPPZXsXAsvuX2KnyxchC1ewROLQGLcyKaA-kmzolKKxdODVe_bdTVlAUHxHxotnIg9tPBMw_n7s_cSryWyfeaQCRDJIosb-xWyPnLR-F7uoUZYzprvjVqagwB171u50m5nIyutvkJs0cTd1J4VUVjlsox0L4iAcXa4s4jIJwkx6q_SxhT3FcEAANEv8-X3o-z9wl3JOpo-gy4h1aemD2fL2-J4gyFx8X6DClKqNkaVMhwFkAYTbcYDprs_bZc5UXuuUoNPQZ0DSxbZ6ArnbaYVHbfxd-E6ICBFaRCXFf-wPLMg8biw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=UcnbZvqqlXo75CXNp78B9V3bYVmtI_lhvqihkPPZXsXAsvuX2KnyxchC1ewROLQGLcyKaA-kmzolKKxdODVe_bdTVlAUHxHxotnIg9tPBMw_n7s_cSryWyfeaQCRDJIosb-xWyPnLR-F7uoUZYzprvjVqagwB171u50m5nIyutvkJs0cTd1J4VUVjlsox0L4iAcXa4s4jIJwkx6q_SxhT3FcEAANEv8-X3o-z9wl3JOpo-gy4h1aemD2fL2-J4gyFx8X6DClKqNkaVMhwFkAYTbcYDprs_bZc5UXuuUoNPQZ0DSxbZ6ArnbaYVHbfxd-E6ICBFaRCXFf-wPLMg8biw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftjO7hVaaIsFaAEXKqKywmMiiYVrSxgGT1MssZBs6FT5x-g2GITtoYif6M4ZLZcgfBiIo1665xDs8fPjsmIB_1Hoh91Gz1p7EAKH9NoLJrQnVbou-lCdem5cwaBQqtRXuPPobBfOeBiJUGuWGzU5NIULkBjfIAEIM7EkkEYcTMshLhL3CVNp5EMI2nb7Ui9XhcgbLfPN0rOyxVFhMYTTShWkLdTc4ncklGOMFi1DknnRtFd7VfpKdVbw6jQUSZoKWZgwdFSP90AJXMd06AuqA4QLCRdnWkX98GKrgicLE6tyoa5h4Ft2hiB41tNH79n2gYLVXgM5Z2_Vum2krUeZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giW3u7t882_5oG9rIZlMmWVFil5__73TDMOk5wc_gSxU_KhemGvsjIlpbVt7p966Io38FAgR2n9rM2rnMf8hotf6H-BUWhi0kGgr3sAvh7D0S68xE8t5dFvcIQVpiZskXAJXaqHFX1zdcRN1qv-rnZMlg4-pibXK5dX2IhTHKNhyZS5agDg6hJdtU9vg9SVD5B_mR_IoNX5djtDbV8l-KGrjpM8oLoprhLZuSYvwP_FWzL64LKpx_agkn97AgCkGu2_oqpX6KI1uZin8ioGa-ggj7uKuHUox6uVvdWl5tCg5HaMhJy9h-4m-TqQNZ4XqAdvlu1YN0MjPYKIvmE-SvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0o03F_T47qdMWPkDbOZ6GD1BmgBqy9PsBRReVz24r_3jPs8qX_OLi0-Yl_irisEzxlrmdgXFn_f103Ti_eMyG8YOr1tjW9gmq9TSY1dDBpJOfVJ3OtjyMt9gPkUSALaHzF8iAo5syr4csbkPtpcuwmC27slUrqH3eFGtGbDzT7Fxm0wQX9amFY_evSM8GRo1xOBiIpVpAKM690CLnEhC1r22eMUkTOMj3dGty7U2gshxMxTr3wOdOWYznEYMd20uIxG2Enf6YrxBzgnc2PfXnRoJlGRDjFbxfEkqOicosq4j5hHT_-d9Kg2bszSRMQnh8dWnt4R6fqPqHRCRrlyeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=sFu7NOmc2IyYFxdR0hhlzaXv8Op9fzfKR5lOaT-y4sJ92IYGD07B58z8zcXSte_J2lSdE27-p0Gpx8gyjL0uagw62gXJvzkZRj5xMhMV-W5R1MqleYBPWMt8Hg6LWc8Q-GtQWgpg8HiLjMS5FR_ulKz3I7mLKl8emo2kOuSPPd8DL1jfMn5_eT45IwKxDHACKyNRKvUO9ZDkwq4xAq4ABfRa8oUt-wR9Q3BaZzWdTbNyK3wH4Ykhi6C2f1oTgCbCOepm7VfjLbY9BN94xiR5IMx_cWsvgmdGlAAfTn95xNH8F_4r7dmFXMGDg02LCs8wOOAECDEwWAi4bS_NDuNB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=sFu7NOmc2IyYFxdR0hhlzaXv8Op9fzfKR5lOaT-y4sJ92IYGD07B58z8zcXSte_J2lSdE27-p0Gpx8gyjL0uagw62gXJvzkZRj5xMhMV-W5R1MqleYBPWMt8Hg6LWc8Q-GtQWgpg8HiLjMS5FR_ulKz3I7mLKl8emo2kOuSPPd8DL1jfMn5_eT45IwKxDHACKyNRKvUO9ZDkwq4xAq4ABfRa8oUt-wR9Q3BaZzWdTbNyK3wH4Ykhi6C2f1oTgCbCOepm7VfjLbY9BN94xiR5IMx_cWsvgmdGlAAfTn95xNH8F_4r7dmFXMGDg02LCs8wOOAECDEwWAi4bS_NDuNB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtAiWme5rNo0Ki8VAlkVjZQ3SMe8R672HtwZWgM69lvFRjBPLltrQWkyCc6ayjAvQuQCU65a7XrDzbUTUHqAHjGCQ8e_x--KmcDKu1F4xswxx7P2fPNMiGfNxE3JDvxnSILuGLRQO9NJPixc9L9Sefo3B9pinvBSLGCIsdY3et-qKC9BM4qCEwwFdWA6mY_likmh2lPsU0STUsHY0O47GBA6s7rLgIez-bQM09d9lmRNmFugUEsPIwoqiCkhcOLQZ5wbeItpfsFfnDMqSkMbhix-jHvDP8MSgVIEIyeTBY-kTo7ksauiwnxAOwpKd7xHEvu8Kj86Hfy9h2vv9so4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=oXL1XG3Vk3GNMGu4IcsNNqNdl-7f81HBxzPO56TFFx9yBwNnny8n9g9wQsJIPmuyfQOcZ2UrkBRrMfTSyPFEjztKkw14L7hRE1QtJkbaMC4lZHAqX0487LWDxzPbNgi9uWxkbs0wPyY-hsuhcki3CazX_xlJ5S2Q6gOeaOqETqaCrNIkLLryaWaR8D586h4MAMSxILGgosWJvfk6O8SFLoM81UK7j_fkLUSbtn9At8X65CESwKq0GoLjtAlxnTrFb9IQU6MMjuZGBSEKN1x63RBSGtoVGMF2bB6rA__GpSHtzKznqVUiuSDeYOIOugtRcn0h3o4vp2lJd7yM0co83g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=oXL1XG3Vk3GNMGu4IcsNNqNdl-7f81HBxzPO56TFFx9yBwNnny8n9g9wQsJIPmuyfQOcZ2UrkBRrMfTSyPFEjztKkw14L7hRE1QtJkbaMC4lZHAqX0487LWDxzPbNgi9uWxkbs0wPyY-hsuhcki3CazX_xlJ5S2Q6gOeaOqETqaCrNIkLLryaWaR8D586h4MAMSxILGgosWJvfk6O8SFLoM81UK7j_fkLUSbtn9At8X65CESwKq0GoLjtAlxnTrFb9IQU6MMjuZGBSEKN1x63RBSGtoVGMF2bB6rA__GpSHtzKznqVUiuSDeYOIOugtRcn0h3o4vp2lJd7yM0co83g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=ZyU05lb5Gla0tyv81ispHydMNCT_XFxu7Pc1gi3PUmPDlg1ZSn9UzhnuhDkeDNDQjXDJ_IuarCP8Q7Bcor4Emm4XTIwmLXIdJcPWLUosTkpnqlX5olskEtEdAbCzl5Vc7sr5JrcFPESj0mL0D_0CE75QXim4BqUSxS8SuiEYXv47b7bjOfTPxNaBjsIuFsvdk-Sg0T3hLq2YbkG6XGC_1R3O_hQdft6IlCYgVnjssigyBZANT1Wp_ZBzmSmF4uC5swowy0d510e8mS_SPuIWbOaunDK_NTWwT4q2N99arzKAh9XVINWK3OzSdIlRZPCQjgyy_DsbHZ7clg4bv2dmzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=ZyU05lb5Gla0tyv81ispHydMNCT_XFxu7Pc1gi3PUmPDlg1ZSn9UzhnuhDkeDNDQjXDJ_IuarCP8Q7Bcor4Emm4XTIwmLXIdJcPWLUosTkpnqlX5olskEtEdAbCzl5Vc7sr5JrcFPESj0mL0D_0CE75QXim4BqUSxS8SuiEYXv47b7bjOfTPxNaBjsIuFsvdk-Sg0T3hLq2YbkG6XGC_1R3O_hQdft6IlCYgVnjssigyBZANT1Wp_ZBzmSmF4uC5swowy0d510e8mS_SPuIWbOaunDK_NTWwT4q2N99arzKAh9XVINWK3OzSdIlRZPCQjgyy_DsbHZ7clg4bv2dmzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=ugN-eEaMwIN-YkWJIucIZ9YSSMcJ33G3loJrtmKj2v9z_K_22_Jw0sVgR0IM8InQd6VN_zzpFWf67NaTLw7GqUSGqCROQuWRAccSzW9JxgryUG9sNZZZdqr___wkBRMMXBaGU-VYMnQzuQledPYanwzcKgij4SJG2haL0dmG1NwzBaj941LD3hVeRefFVua78SWImY7FnUIRdbl9Fp4nFf1GqpFeMIMyMVaAZpXgk_J0RNgq0oQTvJ50ckrZbmeaCkVljaFxWXRDdub1tu0BY2aMVvJ30AXHq0gqrUQEy7RnxaKRBovEEtuW9GpeH2TkSCTv94DR5bG_FhjYoOjdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=ugN-eEaMwIN-YkWJIucIZ9YSSMcJ33G3loJrtmKj2v9z_K_22_Jw0sVgR0IM8InQd6VN_zzpFWf67NaTLw7GqUSGqCROQuWRAccSzW9JxgryUG9sNZZZdqr___wkBRMMXBaGU-VYMnQzuQledPYanwzcKgij4SJG2haL0dmG1NwzBaj941LD3hVeRefFVua78SWImY7FnUIRdbl9Fp4nFf1GqpFeMIMyMVaAZpXgk_J0RNgq0oQTvJ50ckrZbmeaCkVljaFxWXRDdub1tu0BY2aMVvJ30AXHq0gqrUQEy7RnxaKRBovEEtuW9GpeH2TkSCTv94DR5bG_FhjYoOjdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhocnnVqAH9gWsWjW3GHMQuJtRfv8H1HIoexTYUq7YgrAQfiJvr7QwIeoIl4thRqcqqJzxM78UKz7uKDHednI0qjfT5J8YvttClr7sjjS5fcSxoWpj_BkdYjvDw73KLGzf6VGYFYUCvvQXL8XCmkB9JCyPlL0lVEo-_Rzi0XhfQkDN5FW2FePVHBcRVgJS5_KpzqcCyKzMSmrw2MksjgQMY46zf7jcfLU-Drn3-8WT-eUXtm3EF6hl8FPW3UstBEUUuJYC7mEFCW_HqnXVV4ln82cSeWWH9XqU_QBjJow84vBB5VPYealRN0ISlg2-NRNKDG8b3c1sdvg5YgGsD-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHYH1bys8J7XqAnphfOts-PW9NCMkewgVqW6p4vSo4IsUDpm8xOI-L1TkC7LI6cAhWPYjNlYVrWexuf0kqz5F3ygrfjSps1dKZ1Q_7rY0xNypzlP1pT-w9jZ62O-JlIztDx1szEvkspl5vDgONdlOhQFuauKI9UXzz9TcqeFjaZURkid0HRAnkioP2VJGPi_D8JJmbFadpbkdvG3dqrXGHl7lJGQbtlGvs-64hs4dKfbqzQPLZri1QdGi5wBpEmzyJRiA6IYI1WT5F54sOvGOcdJokjiTeQQ0WyIkL0JSn68ypi2Af_niSU1122F7A-U0knDpIwDvxYuedoGwYQ3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHUnrXKyzrDxsBssVvF4GZmtEFFxhe69nVhcxFsti1A5Jjm783vxVE6sl-h-DQp_UjOZAv2AFzTfGLzvmGtkVdlQOvvj4LxI2-xwMUDp2W-NFDAiUJq-ZDyC9iT45HMLc0mwHkMYGixpj4SbP4gv0fxbClNz45XqrOAzNoTivACHUvu3xeFqQ0tXsmPtwTrO7ddOLojqNS4q3JMzqi5JfWS6xU-1xNJk8-29AOOG5nKApBUnkJj5UALKQqAF3go65gs_ueYup_paVUMgFB3uQKxXxHm0I9NXj6QPhIKWo2-x8Y2XnzDmngxJvmXGNere0iPrDV784r1yueeKEgQ8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4YvDulYa9ErPDejrsLRgyukHP_GeVmP_i-S87oO15HXTXEPiaGCh1gH1Rx1SNaZh-vLGNZEUNOt5EIzImEtOvfMtfQ63ok1nrPu1DVo_EmDMx6kL2_OsCpxPrJbF6mcs5urrNhMx4Vuqyhj9VD7UO_HdNWqmUwC6_PfGd6T5PuJdisEsefOV41k2f5ynedme-4-Uz60aQhfXWMGBHR1ziS8L3K089rtqyn9THrmOJznZG2CGhHZP21W09BD8xT6vj6c96GfTwzZT5s-TI7abCsmQ89YQXEmbSJnKeR7kRuWdK-jxG-bqfA0R78U0zzt_F-a0BC1bAcq_MPynQRUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=ROWVRgXk4rz7HHt5UKD0rXL8i1QhXe6KHG4izSiI6vjSZXCXWURvWJCMzVImQM3-PtF-peF1mep85NCxQqV0GcHU6HYXI8u67_WXQZwlRB1VNMIRrSzeAgVlN1opz5pFUFgJTLm3JHEYkg-ghlXsw3s8jlW5nJPehg_4ag8makkL14qMChnH0qpHF1Nrh_kSKilmrn6rFRmBRRmFwSa4R11bOWOwjg98lWPzSAH9wsOp80VTqt1gAGF0VtjoMcYJYMPq-QqTFT7vDy-Q1BTLbVITRObvZc54jvwA7QXczpFJ-iaSgOYCOGsPEkpQbWejzdZKQEuRfOT5e-A9kcLLHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=ROWVRgXk4rz7HHt5UKD0rXL8i1QhXe6KHG4izSiI6vjSZXCXWURvWJCMzVImQM3-PtF-peF1mep85NCxQqV0GcHU6HYXI8u67_WXQZwlRB1VNMIRrSzeAgVlN1opz5pFUFgJTLm3JHEYkg-ghlXsw3s8jlW5nJPehg_4ag8makkL14qMChnH0qpHF1Nrh_kSKilmrn6rFRmBRRmFwSa4R11bOWOwjg98lWPzSAH9wsOp80VTqt1gAGF0VtjoMcYJYMPq-QqTFT7vDy-Q1BTLbVITRObvZc54jvwA7QXczpFJ-iaSgOYCOGsPEkpQbWejzdZKQEuRfOT5e-A9kcLLHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=FiVk5vX61xVgvULQx7C3L3F2_ijO7uzfEfmzNvBosSxs2lH3jxF0YLWhV45fD1aiCuu5DYuxeF_sL_FQTQfxgj5s9V8BAZPAen7emkfxUuacYojqo1K9FaPaq0TFoa4mZQJ24oq3V-17ZHUIxfxAkCSx7hBRQyuShFobnrPFpaX5Jz7GeyONgj47dsu7TVaDPeY7yW8L9eiOz7XVhbZiWufxS_H7mvNtblFgQzJjTJ1lSJCN5goe4iVgNLB23b0wBela6l9wYxHWm1JDKunHSu4LGMcs21-O8_167TVk0O5yZHmHxf8Q5tpGQ_QO_YV-wZj_16thZeuGIzGGdcCqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=FiVk5vX61xVgvULQx7C3L3F2_ijO7uzfEfmzNvBosSxs2lH3jxF0YLWhV45fD1aiCuu5DYuxeF_sL_FQTQfxgj5s9V8BAZPAen7emkfxUuacYojqo1K9FaPaq0TFoa4mZQJ24oq3V-17ZHUIxfxAkCSx7hBRQyuShFobnrPFpaX5Jz7GeyONgj47dsu7TVaDPeY7yW8L9eiOz7XVhbZiWufxS_H7mvNtblFgQzJjTJ1lSJCN5goe4iVgNLB23b0wBela6l9wYxHWm1JDKunHSu4LGMcs21-O8_167TVk0O5yZHmHxf8Q5tpGQ_QO_YV-wZj_16thZeuGIzGGdcCqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=CKqp4Rnr4VXpNbNwkCm8DI0xq6mu2odFfEgIT0dZjGbB7onQLtzjua_ehKCR4VM7Nek7i08CfdkmPhwmYOszLfiJ0yyTEmtrEVjIrh1FJRqb6q_z4ZQvaYkxsQ_PB5pavhJE8-vWIQpY05WfUY7n_xuMK9XXKTkbUpm-X_F8kYJmtoygpgJ63Mp3bNrSoAR9ZNM3Tt4wPlKndUdIOSJyp227Ee8_6qJ50_vUeeKbWXHu290h3A2qI9dlZQGSahKqeELUEBM9i1KDaEn9HWSc91AF6ar4iS8eDBop3KKjmI80QQuVLycjjUABees4_uHxKRa0I74-pqOwJg38COidyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=CKqp4Rnr4VXpNbNwkCm8DI0xq6mu2odFfEgIT0dZjGbB7onQLtzjua_ehKCR4VM7Nek7i08CfdkmPhwmYOszLfiJ0yyTEmtrEVjIrh1FJRqb6q_z4ZQvaYkxsQ_PB5pavhJE8-vWIQpY05WfUY7n_xuMK9XXKTkbUpm-X_F8kYJmtoygpgJ63Mp3bNrSoAR9ZNM3Tt4wPlKndUdIOSJyp227Ee8_6qJ50_vUeeKbWXHu290h3A2qI9dlZQGSahKqeELUEBM9i1KDaEn9HWSc91AF6ar4iS8eDBop3KKjmI80QQuVLycjjUABees4_uHxKRa0I74-pqOwJg38COidyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR5Ub5RVGvPlEheB8frdr0y9OhG_-wSxNicovHTu1926rzx_1lLzCrdgZfTIihSGG0UffJ-KPf1q8ECPPR9dI1pUdQtMg9el0URWHMmBEwuVOTn5ZguUFF9QbMBQljXeDr026FoV_SwEYiLvG6x_w1YuE2cHp6FUEnlE7FXq6UlyfFUifEpF5-GJt3GsD1l3X1jYcWEN-tpafwje7kFf4phnPrBK7YgjIyFxz3z7g4ONF1RB792V8iQY-FoHXtvFO64VF0b5W4U668LU2bWzO7lNwNWiN9WH2jy4mZQo8b2xXho-cG9Bzj4pQmkH1kmVi9e8zfhHwI2CrnknmL73ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=IxAgNTcRR9WRNTj_4VU2O_l3IJi5A-kUA8RcfYa7HRc-cZ-t1QxzsP0lsBMXJwPm9EOl4sfu4HNcshN01q7ToVwD5AQYTDwQG7PJbGqWerib7r_ppp0pAMYDQ9qMsa2_S4U5ZBZzyGgHj8HbhPgDAhWOxzUohtZpaQ9poU6ThHgTGzQJu9kF0KiEtg3ceYvb58e0TZEBTjJpK2hYBrkq9KllVx-6qYa1tx6FCVrA4vVizvkUpMFtfTYs5fPM0mM0HIByHYOrifswGJvNkY7wzYcH6Adjinm0IBTVhyMKODss3K0qX9zUqvR3zCSOARFkx8jg0Png2-eAqQrkeht9ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=IxAgNTcRR9WRNTj_4VU2O_l3IJi5A-kUA8RcfYa7HRc-cZ-t1QxzsP0lsBMXJwPm9EOl4sfu4HNcshN01q7ToVwD5AQYTDwQG7PJbGqWerib7r_ppp0pAMYDQ9qMsa2_S4U5ZBZzyGgHj8HbhPgDAhWOxzUohtZpaQ9poU6ThHgTGzQJu9kF0KiEtg3ceYvb58e0TZEBTjJpK2hYBrkq9KllVx-6qYa1tx6FCVrA4vVizvkUpMFtfTYs5fPM0mM0HIByHYOrifswGJvNkY7wzYcH6Adjinm0IBTVhyMKODss3K0qX9zUqvR3zCSOARFkx8jg0Png2-eAqQrkeht9ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=vDRjVY6EBks91q-ckVtPSlY1uQkBgkF4hXv2k5sQahnMxBAZfvC9fWF1uKubl_pe8zlyTzTWYyvZD4G3ghLdCOkrJk2KlG34CVq8W2WBTimfIbUNjqVDca2l8Z4CiU89axbK3HKDywwnyrn4XhJNU1XzYoWJ0pxLe6ewJg8wDgOJniZzIHZTMNgvOarHSewho-7qGLJkqJT8cOLR8unc2QADi4FuNq6Sm2PZdL-P7UpoMZ_AQONZmq4FOYj4E2nSgBsy-HcVQApaKfvLfr6hDjxTjxL_whqe5-W4NCV4yh-gw5Bpx_mZmjPz4QC5339uYXa0Y34lC7vXEaHeGyQFHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=vDRjVY6EBks91q-ckVtPSlY1uQkBgkF4hXv2k5sQahnMxBAZfvC9fWF1uKubl_pe8zlyTzTWYyvZD4G3ghLdCOkrJk2KlG34CVq8W2WBTimfIbUNjqVDca2l8Z4CiU89axbK3HKDywwnyrn4XhJNU1XzYoWJ0pxLe6ewJg8wDgOJniZzIHZTMNgvOarHSewho-7qGLJkqJT8cOLR8unc2QADi4FuNq6Sm2PZdL-P7UpoMZ_AQONZmq4FOYj4E2nSgBsy-HcVQApaKfvLfr6hDjxTjxL_whqe5-W4NCV4yh-gw5Bpx_mZmjPz4QC5339uYXa0Y34lC7vXEaHeGyQFHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_vrMyQbMrbzztSTvKdQZddg2COlAjmbdDK1LCrDjBJ28C3BYi3jTOt-AP0YZfgQ9P-HIkx7nB-Md8C0qRm8kOxm1Ij4zdLk_Lw9McGwU4SuFrv4BgxC2UsgTvAHE5PFD8mqjRZFYnUackluXOB1EafMpyYaM3UjI3usOuzEYESL7ux7ClDivPmAonq-_FrERhnRfgb5TuxONiHfkMx0okcOv7UIsnJuKQ2RBrQlonJUZebuz-YrXWZYEab2HlLdVHspgmY08todewaMKRDjWNiOxVqaepY91Xp0lpiBs3wC-x31OYypxG9SdKpEQoB8KklUJFU2C5UU5r56C9AYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=Ycd2PgjW4er4LtsdlpHNFOA5TMy9GX96yKeHJ6j7N-szFxkX8CRSbYH8vMnZRWCtk170Nid46Uf3v2AEQWQq_Dt_06KRIfsLXCx6dvyltnStxyVCud7Wap28WtpBXpibmChCnGRTZOmXsjiGNkPhdCa9-5g3vCL4RpEathdIi4t3XlvsKE2Kh-f59osLbjXroJrSJIoucH_YcQQB9_zKCVrQdf36l9LPD05eVGOxg__IkXZxnfua_0PLPTmTkLjiEWhbZF-V4LIGtkdquuCEYP9L_pZFuezNJL5stqUWT5ibSkfxXsrKoL1tVQCAYhqfi-VZvze93bvTgA46Hxw6vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=Ycd2PgjW4er4LtsdlpHNFOA5TMy9GX96yKeHJ6j7N-szFxkX8CRSbYH8vMnZRWCtk170Nid46Uf3v2AEQWQq_Dt_06KRIfsLXCx6dvyltnStxyVCud7Wap28WtpBXpibmChCnGRTZOmXsjiGNkPhdCa9-5g3vCL4RpEathdIi4t3XlvsKE2Kh-f59osLbjXroJrSJIoucH_YcQQB9_zKCVrQdf36l9LPD05eVGOxg__IkXZxnfua_0PLPTmTkLjiEWhbZF-V4LIGtkdquuCEYP9L_pZFuezNJL5stqUWT5ibSkfxXsrKoL1tVQCAYhqfi-VZvze93bvTgA46Hxw6vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_DJKpN-VrB6yR_IvpTjST-1O1C2uJIMUG7HqD-xkjPh7pKRy0ezHvwxMJBjlzDsM9UKY0EYfmqmyZP0eJONXdS0EXWPI5thMlXlu6O0UFrypI_3uplEMtl_OTmSlQYl_ZSF0i4Z2M0oWIwAqPnUIUq-GZVkb17QdEnfwRyEtTiBGEUh7jaLxCzD2kMasv8e_gYryYACZUSMnt8VvChXtglFARGa3vTvhPOyLSMphXyhY4E5m-vzZKujyxTEufW2xbMLofqlgF8DOD5_uMvL_LBkqTxcEucNVnu5yFoLdEaG9nkY-5f85aWfANYTMHWfE6xDwc7KC92CR6BuimgcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5k3JuEda9XB4imJEcFPxmfv1tYNrWnoTkdka4EY3RFRt-PZKw_S7F1cFM6xikj7TUbC4ubSrv67WbLWYcmNiLBGpU4lCHq9rQG2VTJKFpIC33lRV8pR5ctKSwRD_YXmLSYpz7fMGC5h7SoRwewOSuoTNzrumlrGaNU_016g0Youm_0oclSyFLOgB8H-ZPsUtQXbtCNb2-fUrn2g_dABv3DNgxhIZMgMVMdYqbmBBUooF4Cm86jQ7ja39v45R-aIj3zvd_cjMlHbqtMqD4hmL_zZG60OHsQf_gQiI022t2R-dOePoIwRTHTDOGjjDNQVggB5UyovoDQ3xdyJMv5tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=Pw-SJM9QPhLLNAGFuFEgFAkZ1SsBlRqMvh3NgoEsbqCPUpcAHNJ44KFOWpTIpB_OhstAdx_TbauvOccR4AIyVyPlvb3pkmGud9-OOWCvC0i7qtfC-yhMeQTgHgmJtpEFtN7fHdZOEZP3BgtqL0Dd473RxvZPBRNr-L--8mzxUXftmE_f6avSPduv5Y9vbhR-B6l3JSekjbXckm3lYDYtB0oit5QDW5vx3RMXczZOL8chh6ruznu8FcqS6P79NAucmKD2L5nh7EfUZ54iR2nYE__9GeVnKIEgDsMynvQFLfOwRQ_ltwoLlNaxxZgynEKRhSyeQpDNujMiW7wGb8gxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=Pw-SJM9QPhLLNAGFuFEgFAkZ1SsBlRqMvh3NgoEsbqCPUpcAHNJ44KFOWpTIpB_OhstAdx_TbauvOccR4AIyVyPlvb3pkmGud9-OOWCvC0i7qtfC-yhMeQTgHgmJtpEFtN7fHdZOEZP3BgtqL0Dd473RxvZPBRNr-L--8mzxUXftmE_f6avSPduv5Y9vbhR-B6l3JSekjbXckm3lYDYtB0oit5QDW5vx3RMXczZOL8chh6ruznu8FcqS6P79NAucmKD2L5nh7EfUZ54iR2nYE__9GeVnKIEgDsMynvQFLfOwRQ_ltwoLlNaxxZgynEKRhSyeQpDNujMiW7wGb8gxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=HTiyf6DDbItVTWcjryf827_AsgV_Wl-zhoONi4iN2y4h720COq3CYvH6B9-yPmLram2zUqhL1GoIb4fpBnkrbDQ68PFfDJ3ZaIPGr8Y_uhDHxyForct-ZnTRg-ZeFso2blAaItyWTg4OcrbXZFSLlSdwI_CWGQe3LslTI-5lgwJbFUgH-Al6PkB2y9eq3ZG10wQxJzOsXCR_yaTVhYN2W2jcnXuUZrgNtnn9McFrfP42w0gtVkHYZ4CfV1aHp4n7G-e3yTzvLZu9B4eceF0ZOEWoREZhpm8CQEmqEBu0ruaTx_pT6MTzZY2fSQmwXrpDgkinaGBLkeHjmrYq0H5HLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=HTiyf6DDbItVTWcjryf827_AsgV_Wl-zhoONi4iN2y4h720COq3CYvH6B9-yPmLram2zUqhL1GoIb4fpBnkrbDQ68PFfDJ3ZaIPGr8Y_uhDHxyForct-ZnTRg-ZeFso2blAaItyWTg4OcrbXZFSLlSdwI_CWGQe3LslTI-5lgwJbFUgH-Al6PkB2y9eq3ZG10wQxJzOsXCR_yaTVhYN2W2jcnXuUZrgNtnn9McFrfP42w0gtVkHYZ4CfV1aHp4n7G-e3yTzvLZu9B4eceF0ZOEWoREZhpm8CQEmqEBu0ruaTx_pT6MTzZY2fSQmwXrpDgkinaGBLkeHjmrYq0H5HLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #12</div>
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
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0tpy2LDVCgtC8bMTpGdbzqhY6_XXWr654ivJwnzftnPgA1omTgsprL1uzY4mHfLK0nLhJfT4QuoKH6ZjAsmi7rqSC-Zk4NSF6nevuipJmgFGMJS4jUjgJAinvsG10tmetML6sO67DLQhxQ5xq9vm4jYRXu7TPgtIX8xIXdZmRrnqdKZX9py8DY7hMgCXVnnKTCkPSZC1x5S-n9rL-xa2PUyaGIXw7p5XEwH5LzHXdv1Y0Xl6-aaTquEcrwRKYwflKPHKLU6t25f5coPxn69XsjSgQo4lAUJLAHoXYJ3VyLRUsQSXVdpU2-QosTkjTnlbXzBqs4Yr_f2P6XvyXcpqg.jpg" alt="photo" loading="lazy"/></div>
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
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJju7VWE1IU4pOfAlM52bpjSTPu-7vzaDdzXp5aRnOjW2IaVoicTfUz3uBgE37cuqjsiJYVMekU6BkCVsjvZPu7uhKd73VYsr2rehuQhjCEuZ59OqsGLgJps4zV-rBs7FzMlv2DwmTvpZBnN-F2lFmerIg1WGZ3k2lCRwh9pqGhCRkHlQYungMuu8UR7UoKtOxbGa-5wtXhqZorWJLN9h0YrTmUzkzsz3cJ0TRrKapTbNtW_rvaVAHml1ucL05p047eawtYi8PyDCi0xlK8TapbbC4LgeGsXSLkYatWNyIRdW5LD1yl2rwmGF0smT4bR36clTz9qD5ENU6CxUndbaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=neV9xn2V4c00mudkVFojAdKwcrIBkaW59kIGMmi0EgCrQk1cwTp4LOzTfSMYxYPxTIisgOB0s-8kMZk8ykqI1ly0EmxeLWULuo83cWO4sYX0wCBKv3CPO9Pg7UrmxfzxEypW17L2XkjE94FjgmYdyqSPNIMn1PsCnhLRt0kvBUySnf0Y7fba5NBFcA25Ds8fh67oD-OgIyYiGr12jNf8IFOqbccrTm-LAXbdep0JJZcDpKZ6GKLPzHPA89f2r8ItJFfuUS_MlV8pfP7JW_cp0Fexb5Rk_XdjXXfqLGsPhSwnJFqNyBpC0hWfC-NMQQNUhn2iyrcvYBwoG2T1eS5nEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=neV9xn2V4c00mudkVFojAdKwcrIBkaW59kIGMmi0EgCrQk1cwTp4LOzTfSMYxYPxTIisgOB0s-8kMZk8ykqI1ly0EmxeLWULuo83cWO4sYX0wCBKv3CPO9Pg7UrmxfzxEypW17L2XkjE94FjgmYdyqSPNIMn1PsCnhLRt0kvBUySnf0Y7fba5NBFcA25Ds8fh67oD-OgIyYiGr12jNf8IFOqbccrTm-LAXbdep0JJZcDpKZ6GKLPzHPA89f2r8ItJFfuUS_MlV8pfP7JW_cp0Fexb5Rk_XdjXXfqLGsPhSwnJFqNyBpC0hWfC-NMQQNUhn2iyrcvYBwoG2T1eS5nEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=R2paFfJhzQs393XHehaiifg3FxlnPumAA9zcuz6UgSXwJyvEVfTnq0juIor8FHcLmliX4hS-AVZcSUtnQWWE0U_oRTMjmUCE0bTp83Qw5x8IdwqH-i5IzAtgImeQCgkQUEM5qiVOafQESf0JIYSBDP2uzQh0BmrVwD78As2xj5j8dRWogAvu8x6zlfcDxDop1NREfIfhigo74BW4-QAGqaqwwcUii-USVahkV4vATM3st-89vNPxxs8YXtAXjDZNOYhSu6JFAu20yCMbsjlRoaeZ0w2NRiEnPy_lNsQCLxY_Air4MMtGRV_8bVNhPjjxQzDFjihYzNX688Zqi5asWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=R2paFfJhzQs393XHehaiifg3FxlnPumAA9zcuz6UgSXwJyvEVfTnq0juIor8FHcLmliX4hS-AVZcSUtnQWWE0U_oRTMjmUCE0bTp83Qw5x8IdwqH-i5IzAtgImeQCgkQUEM5qiVOafQESf0JIYSBDP2uzQh0BmrVwD78As2xj5j8dRWogAvu8x6zlfcDxDop1NREfIfhigo74BW4-QAGqaqwwcUii-USVahkV4vATM3st-89vNPxxs8YXtAXjDZNOYhSu6JFAu20yCMbsjlRoaeZ0w2NRiEnPy_lNsQCLxY_Air4MMtGRV_8bVNhPjjxQzDFjihYzNX688Zqi5asWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=Pshmo_xadnm_ayT8FSWAIKxKmQdJ2eoo3-Mum-O0y-OvxXKQYLe5jLcZHTf2H0TEzhOgTaBDNX2jwPHpgrfGc7IxTpJukeHiuBBvehREu_ftOKExpndrKp0-VV5wFDP4aR82TxlZifYk6EQvZNfjtaVPspITr3F4DMEobatnHn73EOOuhXU8rQFo24Lria6XcIKl4HtSfzieyz-Przk848JSuNZkRx59k_ai9ZU-mf4vHDze2gMYQsheODbXw8tU-Zlv7yH7w6kgeLWKOD3nWsU_qWkldHYvLKpigrPFj3TS8Ht8rn65Np1eqvgEdZ3bvpcCcVTau1qpmEzdyA3D2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=Pshmo_xadnm_ayT8FSWAIKxKmQdJ2eoo3-Mum-O0y-OvxXKQYLe5jLcZHTf2H0TEzhOgTaBDNX2jwPHpgrfGc7IxTpJukeHiuBBvehREu_ftOKExpndrKp0-VV5wFDP4aR82TxlZifYk6EQvZNfjtaVPspITr3F4DMEobatnHn73EOOuhXU8rQFo24Lria6XcIKl4HtSfzieyz-Przk848JSuNZkRx59k_ai9ZU-mf4vHDze2gMYQsheODbXw8tU-Zlv7yH7w6kgeLWKOD3nWsU_qWkldHYvLKpigrPFj3TS8Ht8rn65Np1eqvgEdZ3bvpcCcVTau1qpmEzdyA3D2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=SJ4H9ATffmsOEA0iJFTkvfTb6RGjAeQcY-7Ci8MkSIGvZqMjnM9_vwcb-XwjKLhsOalUI7VSy_nr5IJ1lYLxwwD0UFPDfCWR84fKTr914TMAAAEGJV7UKhlROscJe-TQalEi_nli_VYStBhlW9TeyVdtGpsdkFJE165AfacGTLW_yCDQYdTbJnm17s6U7lmHkvOaI9AQYq_qPrFTv4mJn91gyuYmLO2GIKWkS5vVk2C3LYrKvoORKr-tNdHNeWEjUsyYgNVDcO8ZwhWQKnnf44Lh9_Gbls573luKxpZsW0dnhL9hRpkWSYwuGJOO5ty0xzvNU0LDFuoiHpAwFO1k7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=SJ4H9ATffmsOEA0iJFTkvfTb6RGjAeQcY-7Ci8MkSIGvZqMjnM9_vwcb-XwjKLhsOalUI7VSy_nr5IJ1lYLxwwD0UFPDfCWR84fKTr914TMAAAEGJV7UKhlROscJe-TQalEi_nli_VYStBhlW9TeyVdtGpsdkFJE165AfacGTLW_yCDQYdTbJnm17s6U7lmHkvOaI9AQYq_qPrFTv4mJn91gyuYmLO2GIKWkS5vVk2C3LYrKvoORKr-tNdHNeWEjUsyYgNVDcO8ZwhWQKnnf44Lh9_Gbls573luKxpZsW0dnhL9hRpkWSYwuGJOO5ty0xzvNU0LDFuoiHpAwFO1k7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alkDr8CJ3D4dWBXZYyjTP6bn5I4zaqZw87uTEp1yiSxVPlb76_cN9pogldKuMd6go1TJXJPhU56NgzVS4wJaYQdol0OlKnNgfJXVZK_YYMe4ZhSn5IgGU5QbDGhRzPBQVVINUlFP7BDEGQqXQL3bpp4ampffhnHcXR35Us5GhwFeoFA51sEWA-87kv7hPtTH-Q5lC4wMgA1dQJCyryZgMJpcPPJsK_smThfLSFnchL7Fau-sy1AX0uGTtWcXQ4jdQ4ltYux4kLgvm66prVpMt0Q5PjK5uUIkQ8IuAq5FtxAjb3uCWBHdSax5KnXjExdlW5I2IeJmJrPqjp7xHH0b8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=E8eIvtz4I7kl1xQMJNPv-5UIW54BuBzpu-GpCNemhZejLUfEdlYr9nHkmsvSd3eCDFBm4gKyBAi7L3DvX7Ci18lAntslAY0yGuFJM_0CQC-iCyIPLy6yPI9GbcHgHWSwafxF6ULdhpDLVIv4Ro1L9skGwlZmI0w9gk34H0WQWAu8rimGVp6OUb9sQ_Kegg0jq9FtNVGeYqcW_u8ggTVjupXw10TkMdr-7qmD_neZ9xT4LlEbnmVRz_xW8Tb_IvicmuX-qvlQDBHAFOixVZgLaOUhaNIkeNlY7md83GVzD3ThhhKUtry0m2fTqIoakp2jWaivaG-6XzHVkb2gb2KqljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=E8eIvtz4I7kl1xQMJNPv-5UIW54BuBzpu-GpCNemhZejLUfEdlYr9nHkmsvSd3eCDFBm4gKyBAi7L3DvX7Ci18lAntslAY0yGuFJM_0CQC-iCyIPLy6yPI9GbcHgHWSwafxF6ULdhpDLVIv4Ro1L9skGwlZmI0w9gk34H0WQWAu8rimGVp6OUb9sQ_Kegg0jq9FtNVGeYqcW_u8ggTVjupXw10TkMdr-7qmD_neZ9xT4LlEbnmVRz_xW8Tb_IvicmuX-qvlQDBHAFOixVZgLaOUhaNIkeNlY7md83GVzD3ThhhKUtry0m2fTqIoakp2jWaivaG-6XzHVkb2gb2KqljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2rqwa4oe75rTBiGlvFqaCyA0GnzgbvQ2ZN1TkcDM27HUZY03D3Np8xfO_wgLzXvDuQ73xBzj1exNPZUw6EfbwJiShCYhitpbOuArDk4dU6Zpr_qZ7r7gqaxquaaJJtTAfBLV3WXqBdum16zIyyEy-mk94Tha8ZadXsVQF2fizF-6K-Pk8YssjCMMqIIYj9MT-hkZ42lCmbPnsjocXfJbg0jmXXqyQfYqZ2XPd5Ogy917h0XGdfFIm0gHszVDxAHGOYT54J6d_o01v39HlQYSa5jeTWiuAlVvRm1LM9nsy-yMBVWO8JoNLVLNEcxeH2piCugyBFTdi-brJ2mkT509A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=AY3Pe43cCr4eSkC5bvByTwheppYIyGAmEZXo-b-4sOSzwUMATcahxDQwdM1efLG_eK1PszRTghM9Oyq8MXzPYrgKGdgxNGwlVkZoTFodpMeWHqm9112tXUZ4jyDilJQZdUlLw0d_mTuaw04u_Cl7mHjlRwBSrtdhxTQOu5aRNuDIfxeDutyMt2XEqu0SHifBGWkK3ojtRwdvJOYUG0zMK98X07AdSg_BAa_749TvrRpXevKV26d3PWpNBjDs0tx5vgJeH64TIEp4c8R5idVvAYwnmuKHem7Bl4eMxsC7rodc8yYuvsCtir2iDMOdKmP8i7wB9PnBWDpcDxaKbU8sOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=AY3Pe43cCr4eSkC5bvByTwheppYIyGAmEZXo-b-4sOSzwUMATcahxDQwdM1efLG_eK1PszRTghM9Oyq8MXzPYrgKGdgxNGwlVkZoTFodpMeWHqm9112tXUZ4jyDilJQZdUlLw0d_mTuaw04u_Cl7mHjlRwBSrtdhxTQOu5aRNuDIfxeDutyMt2XEqu0SHifBGWkK3ojtRwdvJOYUG0zMK98X07AdSg_BAa_749TvrRpXevKV26d3PWpNBjDs0tx5vgJeH64TIEp4c8R5idVvAYwnmuKHem7Bl4eMxsC7rodc8yYuvsCtir2iDMOdKmP8i7wB9PnBWDpcDxaKbU8sOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of7JDOYje9bPgCV8CATr4HIhrbPZ7zr6EPdZl-fYwc7vGTOVYByncJnzZxGrI9_8FgpWA_lp2f4vAQmEDjACQD0viajmm57xrEr24dYg_IJt8GbU4BIWXwRTATToP0MohhhwT5dTsDhz0b-0JAtyS6-tdVY4I8VHswthlUqn-34wPIDcXw1U3Sw4d3PZIzbAGqm9g0ZHOpM09pt6-gu7if4knbGzoFIsxdXagLKScE4kxMMFItunwL6xAiAC4CKvvPFiGA5PZqh256U5Rlznbv4j9TYkLZtFuHXiGQ7KbeXC0UqhECGtu9Vfms9bl2OwN-h_S3WczPnFdcNbHJWHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
