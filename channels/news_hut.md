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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 16:19:14</div>
<hr>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVa4pik5EfxKduS_tZMDPZQZmR0FmuHUqNZPwjLmzCTCysUaFlXvbWe9RtnOeuVecweDvbNo3EKJ8SLNa7ceVFmHrIFwEVNDOc2umjrie3zAPvMAFKR7QdzrJPJMh5RKfv0xTbQgSfKDXqarxmMNjCNyLVv55PEj8zabG_ekIBddlfA9saLnlK66DJpq36Z_wN38m37rArC0WTewgzyp5Tqx9BMNe9QwUWVrNy0qvdTE2R89ZYgKFbDjNB0D7d3MlZAPF2jrJammzPL45Oaep72HtyB-H9aehmyqH9Mvxob2tmRJoTMebg8rBfYBvQc4WJxq3FPwHEi9AD2tRJPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuNBMKsztCCxFntWtE9Go0oZWamr6oy5ffPJtq5HdcUq-UEjFzsAxZ8y0cN6RbDWeMPaechVP0Wq9TG2WCPyRWvGopbkkxyLkBeK2Fk44Fz25d2zkcBO1qxH_twjufgsTgR1jOQeUQmk9BaTpgzQDPcZlYOq2snXt0HuTjwNxOK3r64k3oR8Bj0xo4oYp2Z_1V4WHJE3-ZU8PBrjSyA2Y3txDaX_dV_ogvyNUPtF888E4mtdZJW0chxhAUCMKznSIEs_on04KGs9zib0mErS0mNeA7iR01ZASabG_uxvwgWCXbSRfside9smgBQN5c69kMCtdYfb9zqEGzt_mY8-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9aaPmD8ku8QCo40rkUEq905DJ2ziQVyszLEUyicimOw6V8amyCfeYV7tGEHA5OhmlnE8C89S9TIPohj962MKvDZNQMk6gizwKprQHRuB5y4QGhTDAYF2r5T4p0JS4A4vQUQBIWxMFgQMay41IPPdeCgUM0bPscHOcgWb8nTXeXHU5x3tlTS5fvoki7WDL9xPHQbvl5DtmTdEQBjQ2zsoJAG3U7fc6_xdmbBt9IyDKIY4lcxjjsEL64j01qYPmr3ilhGLPVwKwAWuZCrNnKXMqW8GOAlNbUL74IlqzJcNoG2Ew7Y5z3719QT0B9SBZDOTiKiM4vB6pkO7WMaTVB2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=WBxU2xlOo3kDw0f7uhqn6_52q7_DBia9fBoq-dibORa0vlzm_B65iQK4h9NwGjZiNta_mvHamVkPLFLkCs2nhMfVKls_FXHHvy8SHcVwCwBJLZuaHOYc0kttbha_rqTWlOc1pB3FkQXtA11fDdVTzRqZLJG06WxvhPYGR8JjqEeZcP6NkgiIGvWeRLIiyvFgTlicb-a765ygwvnLctmC8JgWZ8taf1eL4wAps0sJKUnUHWO-Q7jFbz1Iw1b6TDZBH2op2suvSuUBA0wsaNE_OuMIKjaXj_iUF8airqvllbx903BOgvYiQwSDHEL0ypJ_ZC7oYhN6uvDaUZtg_gwJHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=WBxU2xlOo3kDw0f7uhqn6_52q7_DBia9fBoq-dibORa0vlzm_B65iQK4h9NwGjZiNta_mvHamVkPLFLkCs2nhMfVKls_FXHHvy8SHcVwCwBJLZuaHOYc0kttbha_rqTWlOc1pB3FkQXtA11fDdVTzRqZLJG06WxvhPYGR8JjqEeZcP6NkgiIGvWeRLIiyvFgTlicb-a765ygwvnLctmC8JgWZ8taf1eL4wAps0sJKUnUHWO-Q7jFbz1Iw1b6TDZBH2op2suvSuUBA0wsaNE_OuMIKjaXj_iUF8airqvllbx903BOgvYiQwSDHEL0ypJ_ZC7oYhN6uvDaUZtg_gwJHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7by9ovzNCTUuzuvljDnvOkYW3BIh-ojVhpQ5213QTSXuRx0nSVc1c9o1GvDiITFKjIPEQ5EkZ0zpI66cW_0QBczIb1wxO7XOAU4dJ7EdODBQkKBV93MTsuxYttCev_GWcrFgzLGBTENDnFzUoiWWVLH_r7Yugcz8Ajr14hQLU8znLxW6gAgjhAMVT5HlCIPnc6_3LdjKTFaJ9ro-mRduuAIVEtnpgITq1k1aiZfrvIdS-4DIzojBG7yqIvCtt_cZiNMS-SgF1YbGYTGlaTGW0P4HC0PSvjEOl0Jxs0SlrBCYVbcT9VtNLKSfxBKN5V0DAAQ4XVqinONC1olcGYIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em9QgdkgE1mZs0nx7KW0mryOpbrAMF3ePO1JrhcJZGxhNskKO3Zn9aJgb1Z7AGbvfahd58-BEI-6MyKpPLxe_o_H5G2TXFsyrUI3JQF7qolp45vEO1Rhoeo9GPdzfEONZ2tQ2r-pq6pXknTLsgakYqJLPkwNvYXfKFEO9qDdi3ChOfBHvK04ODr-47yv42DfDV6SPXLkb6L4MjtIVnmvcTdm5NMVGXLSGBKhb9JuRbuk1N2uqKwf29nY37BK13xRCetlLIn5Uc2rF2CNOvgxsu3WohAqmYh-rLQwqtYOo-jdHin9FhwDENkH8FRTc4RvNyFGJ9bPhGpviRv7rrngaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX_HmRSX9JVBrDsBvGmnRKXm5s-bHJHxxcHULsz7usbeMS_w9L6TKb_JDdqBNYry8uGzajIMaCqIFfxccmCi4Ri28VsP-4Xor7elc_el-qUFjFTyFcRcJXsQmZ4hLZBWfm986r7pL8PsK1N3BIB22LHBOEmpqA0zt8cArzoH1LEPPx1V3nOINp8vKNn3NMuAnoX1NgZ_UQr8qiAkR6xSv96WCS_IQdSsr-EFsxVt_uxGmsb748IQNMpDVb15X3IwXygWUk7KLj1TwAOJA9Mc5yb35PN8u_Buxk3h3qCsNvrUuo7KrHYm67hQw8Z2IamPeatTEcsCqEW-9wc376sTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feSEBeohk8RuvDHhSzZYC79S7Ap3XlF-D7yAjslT5mRcNvLFcEQmF_yw3XUDEntT-j_UCnbPGU8l8ZGqqoJdGcg-XfWT0xjV22UzOe6cVz9DeB8WyO8v9ZkVEWPxF04-ahsdzGwKnlcV1SPv6976l_CPnIUkIrVCI8aIv8MUgm6QK2KcEdMj211xGYaNl7fyAHxSz7ebh_Bh9cQct05N5ZKAAkUFu4jqJyTfoUd1yAhmEtNxEIuR4wLMLUPGCN91tgPhkvu_GA4BGBbIoDsYU8BmEXqxGZPwco2sE-feeQofksvB7GjPfu4ruzdabEqjJ9w3jB5vVRVW-H8j6NcngA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNKGdqSnziT3uHxSf01xFMVaF9hTs4tZ4odrOjXK0XksIlGtHJGNj0KCW2WnS-9g3XUwOpcdc4oYhAOZZfwJjvdzEb4ZGZvuQPG9gfYhzsdevSep3Tso-myCx2iLWX0YB4WTTfm1O7siWP2gZwjvqPa8Y7PNmVPlYAIdoLT4ndPmJx3bVM0sRbqUmTiLSxtafu_yd5TUdEYf08lLoTh_ZjsZOXd1s_ojmwlBHJ7xsTfaY4MMm94ZfR23B05dGJUCtj7-GFxliVAqZ2VXm1GhxQtEq6dZBYBpPpFBucFtJhgkZwPYN3SP7NyqU0oGmYfkBzadkBQ2C2ObTcAWpUL__g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3NEtd7C0bGRTxlOvlc_c5XWlUacu3s11zCKAB9qLbjlXSwq8cdCN56efLOILlULGYfEj_n2MkCx7OicX14XIQEokGRAJQ3xNacTHKKj0YwmXu6OqexMOt1O8x4rWNgfoUdyNIGXwk4xERFeMLMyoF-ou2ZSs4kn2PQLgit9IFDmcibxB9uWf2SUcHX-NvhlnAgum-5XsERRkLgeJavBrYZyybfPbMY_DTGDsZy0i8nvHafy3IOMQO8mRskBoVugYKJldSpjzFVbaghpCgdtB_vihGBRv7kMlJyxzdaNXNzRCrrvKh7upXoBRzl3MlkkjmAqz0HRradHBsc3zF63Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahEI_Rr3jd9c_NNoqxlHwjt5dJTTq4F77bFf3vTv1Or483gExhp4tHtVBweYRE1_ktmZFrJB2FRdMwmOa4_0aiiRf33OAWYpJENZwTiENGqiRSwmSrV1ZMXaiEYCmmanm7rdY7uCOCtAe5cIv1tWysSH3x0Hv86rsMMcfuDGi5oLszODiOjN5khmuIMoy5JAY6qLkzqy8Sp1h4Aw5t3bBN6TdxxF7THjpIpzPeCDaTgPJC6VRe6PJdnS58bkSWLKRK9tjIePDoVrIHOzfzbzvY69BwMteryy4Z5B-RJ2YTL_4nBdfQWD2CUBMnBbfS3zJ5few5wvF6RKl288tmdIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=cFDmMbm581nVyOw0qYIdm8Fa2VOwFaxT5LZQW7UnKraDZdVTS1KlSn9Q1ZxdhVq5tkPuXp3oi9cKNWQxZZX47uKFuo6KNWegkf4KccbwOiKbuDf5T3DdUYNmLh32nnD_sCjGINMQXCGK1PiN-En15doSGgYCRLEVdz8efESsmHvaSmr0eh_4q_d6TNsbknjcsHyYa-mOPbRpcTWsE_oBcMMnP28cMkO1WYlvBY7FJQ3nI5NCEWksJUbUmLbWkmWhSu5Wc3G85xHRmaPI9gbbA2LAlfoXRnvS0hYW2qfgrHH4-ZmDOjcEeB9vOZ6w3p8ln7quzGPajlisJey2qv2k1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=cFDmMbm581nVyOw0qYIdm8Fa2VOwFaxT5LZQW7UnKraDZdVTS1KlSn9Q1ZxdhVq5tkPuXp3oi9cKNWQxZZX47uKFuo6KNWegkf4KccbwOiKbuDf5T3DdUYNmLh32nnD_sCjGINMQXCGK1PiN-En15doSGgYCRLEVdz8efESsmHvaSmr0eh_4q_d6TNsbknjcsHyYa-mOPbRpcTWsE_oBcMMnP28cMkO1WYlvBY7FJQ3nI5NCEWksJUbUmLbWkmWhSu5Wc3G85xHRmaPI9gbbA2LAlfoXRnvS0hYW2qfgrHH4-ZmDOjcEeB9vOZ6w3p8ln7quzGPajlisJey2qv2k1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C98YtkMndUAntWkQ_wRwZPFO6g-DzcVUina51SatAUxL1CcpqmbAFwyTI8U9pJkrEQBIhmtOlLGIbpg9v95MorXcUlOGYi5yjvNhrclzSCRmc4v4Lvy4rh4Ektol7NMDF-oqJMVlY-bLkHSUUlGh44UOHi56klekyWHkhUKLHFvAeUCNLWq313eJGcBUdStmA1_SXiC0NygVLCahSLTIrD-LZrD9VRwQhPDcYFDuxz-l02Vbz5zNFYpGDVeGC-UKqr2VXNM7lSh3ny7H_szm8RbMhTtCkz48eo4I8uXFAEJP1hNHPVZkrSix04VAD3VNFCn7l6RGWcgqMXxGS19MxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=Lfy1-6MZMAQStP9DgN5SdhzCwDwIuPC3hd9OYqRAzjsZOwOzYHb_xdNTuD15uiyXqUOV0ZvTaxpep79yBTkJMGCV0N6nrhPXbVl2l4PYOw05bxwIGO1GzxURcbOB7Q9PuOSXAtRTd4GOfbbCIp5vZEdnUTqGjIhgWvS-Kb7ErQjpSDce44jyEWyWDrPR4IkZ591A4B-47X0hjNvtQAT1RhUlYQCXLHQTRpJiKEeId-WGpTNqBe7uu8a9ouIupfCyro1OwgeH-ZGq-jBk_W2UZHWfDrwAibf2Pc-U-wBt8Jq9AoTX2N2V-pGFLO5VWP2u9ghR-aFm5loqjONkjuuayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=Lfy1-6MZMAQStP9DgN5SdhzCwDwIuPC3hd9OYqRAzjsZOwOzYHb_xdNTuD15uiyXqUOV0ZvTaxpep79yBTkJMGCV0N6nrhPXbVl2l4PYOw05bxwIGO1GzxURcbOB7Q9PuOSXAtRTd4GOfbbCIp5vZEdnUTqGjIhgWvS-Kb7ErQjpSDce44jyEWyWDrPR4IkZ591A4B-47X0hjNvtQAT1RhUlYQCXLHQTRpJiKEeId-WGpTNqBe7uu8a9ouIupfCyro1OwgeH-ZGq-jBk_W2UZHWfDrwAibf2Pc-U-wBt8Jq9AoTX2N2V-pGFLO5VWP2u9ghR-aFm5loqjONkjuuayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLrAGMLPwrEvkjGF4JkVY_rv8Vyqq5hssWp-jjWw9RsaVjaYsUwtyvlCIiUe29l-BK4Lp5TB2lCVXDoFGC1-1SYwiM33nYWthJqP6SMNuN3dca3GfSAWUvvbcYhev-QaNh7aaFknV1cSQWZBPmhMlQPyYwzYqASBYHVjUcx6kSulbldWKELBUiEkSNHzZnK72pz5M-goGkCO5E8DMw627dXdlSVLB2yBzL6-jL3kgu38Ag469TlrxP2zJz3gEY3P11ADhx7IHaHO7Bb8R1VaskzLE_WSWHwAjwMidHrjb9QERht1e8gzt23ZwbDBEgXPfYWdY1km7-gB1YxAC0nunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1oZZYxKnN1AwIu4g72suay2fkPdTtIo05GSgWzPFHsdTfJzvc9L8I9w5EKLcwtNipVAzmGOzWiZMV1inaEIoCJjsXQo9yWgcpGTyJixCylOyHPbUcKb5S9Rj3EQpO-izGCP8ePgFEZtz8yoA9_dGA7MVzevYCqRQF7R2spzkTuuQ9zAZrdnV_6xFof4qx97v6-EAF_Q5LxrxA26xpUlTbvhhyAa5KkETxRofxXP2Xi4uemzHkc1VAmeigwSekPaVCUcqrM9N5CToTqxSJ8qDmkT8Khs8YDKkMNAQ4PGB8jrJiy5likt0SIPHdGQb2qoyWK5dEdIWwSaJKaeAJ1smw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=nAlPNwU_EJKXILIeRgfxePXhEPInPYOpUA6xAlAousCikhgyuejCx68SRiqoa_6hmwvkKSZZfWHKLj1GaXDDXOM_A_-bRUNd7Xb2sskABFdKxyEMfgLPDaOeVXN41InPQ-e6syAK5Aqh3S_PuGJz9U7x3sNpNkEBndJEcTc2VwbCFB9UWe3XIVet6RGDKxeyMgmTCmFxv6eD975iTHnOSqlsk47CLcpIkigFliYOg41UWwAk4Pno2IDm5JmjcTF1JPHLoXgSSEUnDiBLEz7o97tHoS0RFcSKJuRXqQy6KE2nGp1NYTnNDwezH_7Al2hDbGxQ7yoEllWh_gICTXVTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=nAlPNwU_EJKXILIeRgfxePXhEPInPYOpUA6xAlAousCikhgyuejCx68SRiqoa_6hmwvkKSZZfWHKLj1GaXDDXOM_A_-bRUNd7Xb2sskABFdKxyEMfgLPDaOeVXN41InPQ-e6syAK5Aqh3S_PuGJz9U7x3sNpNkEBndJEcTc2VwbCFB9UWe3XIVet6RGDKxeyMgmTCmFxv6eD975iTHnOSqlsk47CLcpIkigFliYOg41UWwAk4Pno2IDm5JmjcTF1JPHLoXgSSEUnDiBLEz7o97tHoS0RFcSKJuRXqQy6KE2nGp1NYTnNDwezH_7Al2hDbGxQ7yoEllWh_gICTXVTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=N9Fn6quCku3BJY6zuWQktc4Hrd7FfbjVIBNwA0mYU8mYXUB2YOxuWDooXvPaDGF1W-cXLNr_NEC9FdFCKZVP1rl792cAhuTDejQurtON_I_5kO-4XzdMAHmP_VQgYrBkntdVwGrA_PrQBQ_fv2Flp8DdOrDNbBeeTQN3GMk7r9xoq79xuJNR2UdINczVaFPSCUiOnU60U86JnvRs5B9eyRXg1Z4TBy3fH_hl_NKZr5CsWwdHcZrj2INr_GP2Enl0hJiGiE4NYtfApN4b0mf54Ll4jAikLEPwd1zIHcz1Mv-_inaLqLcy55yk985cu7t9WCoUO4VeR4W4ifAc6sebbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=N9Fn6quCku3BJY6zuWQktc4Hrd7FfbjVIBNwA0mYU8mYXUB2YOxuWDooXvPaDGF1W-cXLNr_NEC9FdFCKZVP1rl792cAhuTDejQurtON_I_5kO-4XzdMAHmP_VQgYrBkntdVwGrA_PrQBQ_fv2Flp8DdOrDNbBeeTQN3GMk7r9xoq79xuJNR2UdINczVaFPSCUiOnU60U86JnvRs5B9eyRXg1Z4TBy3fH_hl_NKZr5CsWwdHcZrj2INr_GP2Enl0hJiGiE4NYtfApN4b0mf54Ll4jAikLEPwd1zIHcz1Mv-_inaLqLcy55yk985cu7t9WCoUO4VeR4W4ifAc6sebbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=GQslQ7EerTRkf-lxWdonyTijs2S7AcL4EQ2OQ29w5QQtCNqz2G4Y9Gje16ZuIU_ZziA9ZIg5KnXucv7dfFYUPoXDFyZ1rQSD9GYtmWeQ9Ckan5oU9MH4NR-_CWwfW58aPadyHxD5-F1Nr6NEcbuejSmati187qPMTjYkkPMI1j1uBHiYtSdBms3dBZyjQdCHnnozcMhnN2QcpI4OvI0mfUqmoFqylQ_-19-ZRF7c8KJ0mu1M8lxw4RQdPXfNpw9J8z2wC_ZcvCFs33ykWsqZQn4rS22gzl17PgL-e8cCqy4P9Yh86lmIsnwfMEOryNfJT70QC0q70GEROwY8zBd8-Bi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=GQslQ7EerTRkf-lxWdonyTijs2S7AcL4EQ2OQ29w5QQtCNqz2G4Y9Gje16ZuIU_ZziA9ZIg5KnXucv7dfFYUPoXDFyZ1rQSD9GYtmWeQ9Ckan5oU9MH4NR-_CWwfW58aPadyHxD5-F1Nr6NEcbuejSmati187qPMTjYkkPMI1j1uBHiYtSdBms3dBZyjQdCHnnozcMhnN2QcpI4OvI0mfUqmoFqylQ_-19-ZRF7c8KJ0mu1M8lxw4RQdPXfNpw9J8z2wC_ZcvCFs33ykWsqZQn4rS22gzl17PgL-e8cCqy4P9Yh86lmIsnwfMEOryNfJT70QC0q70GEROwY8zBd8-Bi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFpiBoWLrMpPNow1UKdnLNW3gG5R4KHplfXZw-xAmyEE3LJhPPi26Tamcoeukitf6aVRMbdTsUdmRMrk2YZH565u1g5T7YKt2V0HBa708MoL24Ecf7NBWmHljoiimled_SxXxXlOuy32akJeQZYVdYYGDkt0NfB1AwE6xGlNTSR4Vzib7PvekVyYuJGQmrtpJYowb6zZmA6GbtTlixJfQ1zfLSWLnk8zia_TjKAuHaNM_mbPat_ULNJSObJRMViZ8YnPuu3uP9Aa3WMh2ymRn7AMQYlu-3SAjyD1vR7qoMwcVqp79ltyNBFMRuw3orIMVWQorKrEIo-557P4zSZ6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=eGORY-wtFguA9_7uZVF5WBrStuTbiLmPjioGNEJyuMO4a8OP8lgTEu3sdhn5qAC1bNRqZvFCUaQFpehD221C5MMJSNzu9F6E9JOgPRfguQ7FBKtOX3hndQh6U1OpgtTX2ByJW4ztTzm_o4IoNmX5Bio0A2pW9CRRW-Bbf1NBG4dLB6QkqypiiJDSNUOsj9Z8G3jr12iy-VFQhV9NoAmuReT0lY_P_cOGydQxkR5kH65it9snD20nljnCNQD5yAfV7th1FlQ9H9k9M3fPPsAaV_CBTggMSnB2n60kF0SLfJH5Pclft17iXtV3uI2cMWtfSLHR_j7Epxi3ER-STRHqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=eGORY-wtFguA9_7uZVF5WBrStuTbiLmPjioGNEJyuMO4a8OP8lgTEu3sdhn5qAC1bNRqZvFCUaQFpehD221C5MMJSNzu9F6E9JOgPRfguQ7FBKtOX3hndQh6U1OpgtTX2ByJW4ztTzm_o4IoNmX5Bio0A2pW9CRRW-Bbf1NBG4dLB6QkqypiiJDSNUOsj9Z8G3jr12iy-VFQhV9NoAmuReT0lY_P_cOGydQxkR5kH65it9snD20nljnCNQD5yAfV7th1FlQ9H9k9M3fPPsAaV_CBTggMSnB2n60kF0SLfJH5Pclft17iXtV3uI2cMWtfSLHR_j7Epxi3ER-STRHqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=cvxiq6sK6aJWCPS1J5frX0jB47SnO-RK2LRx9FiCohN3z-DcQtafRkojM89tkeUdEoPsg0gddiU04DaPMqmvjFtMzEFrfPTsYCxMCA1UwwvllEANj7FEaJEOqFjMwrFAq9mDVqI0m_ZYXtqv4wi_tWN8OJJ8tDgF9KVCVKxe47s2nmRWYxjM7kWIrfcRayKssAyU_Bt7F3t0EzqyXF4gYL1pOTTktF3EKXOIFhBkZDnM5iDMrtehyaC3ztxFgr73E9PPm6o5cpRGnB0stxIKHh4N-8liUq0ohHb20bhAazY1E8ztK4Y1CZKaQEIDGXyLfznKxeuZFFXBz8SY2Yc9Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=cvxiq6sK6aJWCPS1J5frX0jB47SnO-RK2LRx9FiCohN3z-DcQtafRkojM89tkeUdEoPsg0gddiU04DaPMqmvjFtMzEFrfPTsYCxMCA1UwwvllEANj7FEaJEOqFjMwrFAq9mDVqI0m_ZYXtqv4wi_tWN8OJJ8tDgF9KVCVKxe47s2nmRWYxjM7kWIrfcRayKssAyU_Bt7F3t0EzqyXF4gYL1pOTTktF3EKXOIFhBkZDnM5iDMrtehyaC3ztxFgr73E9PPm6o5cpRGnB0stxIKHh4N-8liUq0ohHb20bhAazY1E8ztK4Y1CZKaQEIDGXyLfznKxeuZFFXBz8SY2Yc9Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=BXPtNN5ToOx56AJzC0JWjHW-XupCnR2rAfTCzfly3uD_s7ujhVYflI2Ee1wyXiz78NT5DGHhQSDb9LJf3dQjKzRrnc7bsPOIkscMYEJ8e82XJM7_viuv7L_0D4g2uqHmO2ox8_vT_koiZ8e_3cA_roOPWjzPrgP9mg_2ZStKhUXgwVjPqSLyFBEP_aco3IEpE8PZUVww7EU56EjySL-CrnDwdcS1ukAODXDGUu7SV8cQI67Pwj9zpKY3aDmU8jdETy-14fQGmvIFUBdh-h3rivgdAvI_XYCNtE1UPu_dAwT_aCIL50bDXh0THqKEIY39fE4UMtVOM06_IGGGDFuvdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=BXPtNN5ToOx56AJzC0JWjHW-XupCnR2rAfTCzfly3uD_s7ujhVYflI2Ee1wyXiz78NT5DGHhQSDb9LJf3dQjKzRrnc7bsPOIkscMYEJ8e82XJM7_viuv7L_0D4g2uqHmO2ox8_vT_koiZ8e_3cA_roOPWjzPrgP9mg_2ZStKhUXgwVjPqSLyFBEP_aco3IEpE8PZUVww7EU56EjySL-CrnDwdcS1ukAODXDGUu7SV8cQI67Pwj9zpKY3aDmU8jdETy-14fQGmvIFUBdh-h3rivgdAvI_XYCNtE1UPu_dAwT_aCIL50bDXh0THqKEIY39fE4UMtVOM06_IGGGDFuvdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pm0ypF8Yu6d5f35b0NKddNcOLf4TJFAZU9sztBbwrgtc7IQkeC-scKxboSGDQgkGCM6LsFdVNmKt6d52BHJGUlQayxhWIF0AOjsNNhrDBl1k-IeJIvM-nkdZKSUN6Ilo8jUODSr1sMJM3ji4jPo9VNq5ztPQIUZuImhRoCi2RTHKB7I-BO6TQ9holwFaPe7_V1gV-HxnrUmb4GVdgGMMtme4Tb54MlKF8cFAG7EE4mnwshfnebnIwK8SElfj0d9KEga4ebsLr8YyXIqFGbi-p-w_V1ZJrGuBnZJirV437h4bsUolhxoV7aGJuH9obqVYsydXXt-nLqXmk3SZyVXwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJXEo_UaUPu77FhbrAwgitOYjcQPrUmV_Cg-ttcab-yRLCKxJ7zDnBl3TeghiVy7mjZKuukfvmQoU2-LX0n6qR2lH-78nULtyL6q70jIIggL7idslHYof-8nXMOb4wmody9ijjCJXjeNLWpsm1r9fcD9990RL9NFpfsu8vw4RdRTH7lwqVAps2iDlTtF0iG8AHjUKzwqfnSvXZB3OIv6F4jNnhB3WpJo7FGlbqaGRQQkhXgWiIOtfIPEgvu5VAAahh_CM2k7W8DMH8tPUCKxoUBBnPMuL9mEwlPcENspDCUDDog5zNRWprr-15jb3Emi6TWr4RjNAegkH1__8YcfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMzAjFpgcUvOgM5CjBWbWumQjntTAmOJzRu_CIPQUE96gy_e5qj86RGtotJxqrn5gBGomLhR8XDHL0MkgqUHNFdIowFiQCGPqMZ8ffN4Om3cXuTKNQzqvSollUOwBipH8mhq0P_PO6bGoUwPY1qkAA394K6QfA_xwsj__7H9RMld3XNROKUnPSixCS0HgyuPFOLiK4ONS6gDvJkcTsZcGjWA4XN5iNcRIFZuvGrEwUrBavB_vqs9xv06kt_jgGqMlZKQoN0YyCs1aWzz0JUeLomKEx2mZ0Htf7WduFOxbtvtmm4Id6Tgfpb0jH-sTxQHjexLdcE7g-mknCjQKnpTMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=BJ3IbHBGvVv83ie3jVqClOHqCsyEWDtt7N_GRvz3vItEf2TrjSwafmtwaD9dvZro82lmTJbfNxLCae7t4_3t45pS2P0KtlFgtd1TtufXmP5ZIK1hwLShdTprNFUb3uF7vBd0dPRjXH_NYjp08ksrmA1G-llJCFFZbR6hesLPgVrMxGvGCrPASRy2pGZBmcA4s_tvhuTWqifDIA--bc2eL4o77-uNY0FPBLCtuIILtXw3IcIfVdH5j19f4EPKlgEF3qZ2VK8i_1WtkSU6k_owzegTwe3uoWzW3UDkXRfYSiYV9uQSJ9Qv3FW41IegGaRwb2JGaUvCkYvuxR8h9kB6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=BJ3IbHBGvVv83ie3jVqClOHqCsyEWDtt7N_GRvz3vItEf2TrjSwafmtwaD9dvZro82lmTJbfNxLCae7t4_3t45pS2P0KtlFgtd1TtufXmP5ZIK1hwLShdTprNFUb3uF7vBd0dPRjXH_NYjp08ksrmA1G-llJCFFZbR6hesLPgVrMxGvGCrPASRy2pGZBmcA4s_tvhuTWqifDIA--bc2eL4o77-uNY0FPBLCtuIILtXw3IcIfVdH5j19f4EPKlgEF3qZ2VK8i_1WtkSU6k_owzegTwe3uoWzW3UDkXRfYSiYV9uQSJ9Qv3FW41IegGaRwb2JGaUvCkYvuxR8h9kB6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaUJkj6rb36PyF9P5w5UGzYdnjcW7sEPqhmyoF6uKWLJA7NKDC9I5GdMyHfqzAVPz38gqr4m1mR61JG-lCcQtWAnmD1TcY_F_LhITavE1TAEoWytSLz0MkkstJdVuO8UEj_bCnBHKT2eQtKbryJ4jszG1ggn_SuyZKOsVOGGGuRi1ZGEl1jzVIjzd4Xxqz8JqrbUsD548Dn3u6iaPKXCFAI7s8y38AYR9N8fBwA5FvRUtBPUrSgjukt9-XZsdUu1dgtx1HvDmdLn2V3e98-esEcHqlJkPelEvQSzwTCgdlf2jN2U3A32ZKWYeBnK0Jawk5BwS_beGkCV6hoNMRCZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=MtMIsMNYO1cZp2-kuL50yqUhHXkjBh_Gm4MI2CfA3oGwIVbY0NYYvnyQsf0SdRWzRPdjdxAGSCUu57EEay3w-U95nmWUMXvp5--dbn5wK6zfTlL8TzR6KAS_lvX9iq3Jb8eEx2GMO1NWk0DeE-Jp-4hYKpfQ6VcTOIBgWpKkylSToQ1RRg8rpYFJrdC50cplMYrUCux7fqmuIMSIBjUEHM7GF_alr92bBbgLlaMAi9744lesU4VpaP8tq_nvYkxJuIfPSp0q3xB-R2xRctCxk1rdbpDRIgpo8TS2C1LPguaqPXicSy8RqcuJaC4hVgdkm4sVgPweJIWaUbw37eSmSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=MtMIsMNYO1cZp2-kuL50yqUhHXkjBh_Gm4MI2CfA3oGwIVbY0NYYvnyQsf0SdRWzRPdjdxAGSCUu57EEay3w-U95nmWUMXvp5--dbn5wK6zfTlL8TzR6KAS_lvX9iq3Jb8eEx2GMO1NWk0DeE-Jp-4hYKpfQ6VcTOIBgWpKkylSToQ1RRg8rpYFJrdC50cplMYrUCux7fqmuIMSIBjUEHM7GF_alr92bBbgLlaMAi9744lesU4VpaP8tq_nvYkxJuIfPSp0q3xB-R2xRctCxk1rdbpDRIgpo8TS2C1LPguaqPXicSy8RqcuJaC4hVgdkm4sVgPweJIWaUbw37eSmSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=k-3DsHVWQH5I28jRkacewkCMNVA8-xd4iXGM_PQVx-QN354SZfLRUxxBb3M0sgr-B4oO0HvMKuzt_iotWEbmVz-yZRXBzGzLiZIBmrEpgNmHf9AS8sXssw_C0WKzgVjUdecIV2vTf3WmBv_AsbZq-dMA1GVMTiPH4zVzsPQmEXR4xraMtOUwQWJwf9yXHkHaImWmFuuN5s8-qRUq4VAmP5nKutAM7pYIhoaOvtNJqLEzqTgroQlbCJYsRb6ZH0fU28IoDFZVwLfIP8Pffs2YcXSh0adzD3drFZTKebmKVdQUml4drVQPMYoAtWlhHnFyGyFkQwr3FgBulOurbWM7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=k-3DsHVWQH5I28jRkacewkCMNVA8-xd4iXGM_PQVx-QN354SZfLRUxxBb3M0sgr-B4oO0HvMKuzt_iotWEbmVz-yZRXBzGzLiZIBmrEpgNmHf9AS8sXssw_C0WKzgVjUdecIV2vTf3WmBv_AsbZq-dMA1GVMTiPH4zVzsPQmEXR4xraMtOUwQWJwf9yXHkHaImWmFuuN5s8-qRUq4VAmP5nKutAM7pYIhoaOvtNJqLEzqTgroQlbCJYsRb6ZH0fU28IoDFZVwLfIP8Pffs2YcXSh0adzD3drFZTKebmKVdQUml4drVQPMYoAtWlhHnFyGyFkQwr3FgBulOurbWM7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=aVMaFDFVoN6Xn5dB3YSpUdKU3VQOKcpijVKpt9I48-2nyH0e7MYvw_zyNJfMt1LAltUfGDsrrhUTzzg7GT1XetUVTPbhUGdJ7X5CmBvTzYOKiMKP9Qi5sLJHS-1I3VoH9ceFUxh4Zh7OgpD4YMFWuk5DG7lFwSrnX8TrtKBNzADDMqbUDtQ1-_pSURm5bNz3mJk7fgbbceUWKurtHc1XzTkrv7EqNH8li_YbcSCcm4yjyXww97l30ivfyVteFYVB9h6StXxjqyd9DMsapry-yEErILXl4uUW4rD6AOjmN8BoZZDho4FdUDlIPbV9FL_Kxg1Mb6WtguZaR5sOkyLZyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=aVMaFDFVoN6Xn5dB3YSpUdKU3VQOKcpijVKpt9I48-2nyH0e7MYvw_zyNJfMt1LAltUfGDsrrhUTzzg7GT1XetUVTPbhUGdJ7X5CmBvTzYOKiMKP9Qi5sLJHS-1I3VoH9ceFUxh4Zh7OgpD4YMFWuk5DG7lFwSrnX8TrtKBNzADDMqbUDtQ1-_pSURm5bNz3mJk7fgbbceUWKurtHc1XzTkrv7EqNH8li_YbcSCcm4yjyXww97l30ivfyVteFYVB9h6StXxjqyd9DMsapry-yEErILXl4uUW4rD6AOjmN8BoZZDho4FdUDlIPbV9FL_Kxg1Mb6WtguZaR5sOkyLZyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuQ40vEEgvdenuTbijcgpwLKocu0597tmhnngEh4E1BbrUbktOVECHVeq-dBc6etQmp400w6BRpulbGwIxfLQKi9DEl1wsYFJHwvou-cpP0QfdTpIbIMXcCAurxfOth_sUXMYp4veS1wZTlca8Vi_DwR2b6_lRQpQlX1CzDC5wo3YS2_XCQWNJcLhk_sQEZkopwUL2O424ycaJvSFk_HdkHd6k89XZTuqsQCEk2qh5fKyvt9k_eiEEBdV5jenTEgFo-DK7JZIdKP8JgusOvvM6vwgfBlbgYWwkyW60Fs4F6kOfyynxiVq9SRHx7X7Y941Gj7mqD_z1Lc80fS7JtYwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK6VC4CC9zZj1-FqYknF1p00KspOB1pTH30zZgXWI1QRQ60YN7eNDogXzYPKm5vma2PKIOkU9qWNBTYnNA1UbQT6zTUXZTBwj-jdH5ZLTSCsjTTa9cjrtbl7SLLr82kXT-ZxE0x7FSs1uTj6wr2VDlL9QKLY-M8R2Ig_M76eRRsX5EQ2yh90Nu5g2NK-qqSOwDEc2QSStkXBe4-723oXoUaswSUtoxPj1g_LPX85kBcbp7T6FzwHGQF2879XIlP_Epvm-EAPPKXyPs3irlyYHHP2LDq1PlckjHAgdlWUAEyA0IIz0nzBGC_xln-PNepagrDqkGEq3xwBiPbZ3DJXUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBYQhp1765SxQ0a1lYxRPTeEPXpZ-iC6mIf6HA0r_moIqh7GpTNYjf0Fuc9v_Yb3YvKeeCl-SaHgMTZFE2hGfBjCdZWFcp6pT6p8-KEjfMiruT0pmenfWd9AZLOOdaRu6DXGtSwEtr6cTxY6R12jG2DBSHzuuOkBYgYHRvAyiOjCx0xF8d88h-gZOvvtDJYqHzycvw6XQSM5p7w5K6_CioxfFXCzKh_5aNrKzi8lEfQv8z-oyGNiO2wqlw-JP-TDb5fXohMrrLnpxVXF6ocae3aqCM47jmUX2pRKs5P86WhebRFdP9M-NpHycrbqrfyylBmHW11rqU2OC1UP7Uhcjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG3pcXPzmv6ndO00IEpbFI8Njkv-S4lCNvRtwznEQEm8vGX1ri83r8MzVrqfe_RB-Whqu4dhb17P7euEj4twbRKHiX1qj2rir3DphR-tk0H9gl0Hb-igMPAJKhl4sEqo9vBQ4Tu7a6ImKZUeYk2UN8Rl0Hw4KU_zqkpzZ6d9tzk_UgInPfgQJZUoS5Y8t0jBzwqKEi116gghZdn17jCz3P9JUvcw4FjR2YTMqL3WbqxIwTGH7cVI8gcenuPo-sKMK_Rze0QCgfrJ8bRvINwQ3jmkFFL11ol6K0NAYwAaGVfFcv08bfd5heabCVhvDdkg7hfKVZF9T38Y5VGzuDSpeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=EcOdHiN5IN042jPG4TKlXfTw10IlARcXKDekssbLzA16k8VFIhdFMrieGgKb5cthbrIu7Usvtgh1IFK-tgS1abtBfdRseDTjM5kP0-V_vKEtwLTSLbK44t-A9bI_qTloXAV00kYj_Fyaw_4g-eWITWgsYZLa_Zz3_8oerSt52klVTiOl3auCNtOGLdoVfHkzIqAVbUFwJ-V8QijD36QQYvoAu97cxBWhZ1AY9DNUX1adkKE_2N9kElLTr_VWuZiztqbKqOZJdvbSDmoEStn4f3VINJHZ8-yss2oYCFxqFLZrGeWcYdbowwm30y3BAxDA6kSdzIVsrczpRynLqwx1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=EcOdHiN5IN042jPG4TKlXfTw10IlARcXKDekssbLzA16k8VFIhdFMrieGgKb5cthbrIu7Usvtgh1IFK-tgS1abtBfdRseDTjM5kP0-V_vKEtwLTSLbK44t-A9bI_qTloXAV00kYj_Fyaw_4g-eWITWgsYZLa_Zz3_8oerSt52klVTiOl3auCNtOGLdoVfHkzIqAVbUFwJ-V8QijD36QQYvoAu97cxBWhZ1AY9DNUX1adkKE_2N9kElLTr_VWuZiztqbKqOZJdvbSDmoEStn4f3VINJHZ8-yss2oYCFxqFLZrGeWcYdbowwm30y3BAxDA6kSdzIVsrczpRynLqwx1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=d75fZ9u2iSYSrXWvW9thHAgaLKKZCEwi1coHuhZxuS3b7cGL2bTrturptVEmiYMF_oqKWDQeh9g7qzztmAEGzy--ebwVxs1myHG6HWZIRWDpAHD-ADlIW-hrphKR2mrEbDHwETTBxmwNQWxL7vzk7I9GN4h0bQRyicBaCDbq2AylM6whmogub3jXYspu5wfnMxdvPL_5_IwFkJlCqOlw5EUs1_gzqCxSq4tl5vq3xRh6DDcBoLGx9FbID_TkAIZW9Q-VnCC7mWs8OECdoqHx7A-etQvidItQG-7G3D6aRXiuizGwSHGodVnS8v_THXl8EdiDQKap2zqXDZLU332Kxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=d75fZ9u2iSYSrXWvW9thHAgaLKKZCEwi1coHuhZxuS3b7cGL2bTrturptVEmiYMF_oqKWDQeh9g7qzztmAEGzy--ebwVxs1myHG6HWZIRWDpAHD-ADlIW-hrphKR2mrEbDHwETTBxmwNQWxL7vzk7I9GN4h0bQRyicBaCDbq2AylM6whmogub3jXYspu5wfnMxdvPL_5_IwFkJlCqOlw5EUs1_gzqCxSq4tl5vq3xRh6DDcBoLGx9FbID_TkAIZW9Q-VnCC7mWs8OECdoqHx7A-etQvidItQG-7G3D6aRXiuizGwSHGodVnS8v_THXl8EdiDQKap2zqXDZLU332Kxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh-h6HDjv-ryEngG4iRbStjmWLK960-qgunAKWSbWO8Xf5de2K15wAMZzrkTsGlrSOYqk7wKcDm3LwS-xmBvWV0BTTThscxmXiD3_QnVhpW4bciqftJBybsvMUdP5tvyNVo3e04skWCSgRYG6r24WTdVhE9yEnXJ9p94lalnS2SqyD3mzfyloJloM1pr54-YlX3kwl9s4HiLAKRooNngd9cQqhy56FrUKNeG1sVXzu8_ZdwDZIhhibtSIkPf4VdRDUvIEqfj-iJL1p7FR-ff9MLKLYqSTfj_aZIYL8-Tz6wY1-W7m9wnrD-N1uoN65akYCKCmK9nckpGBU6cF8W5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=DXx0RobfX25VQ6LJHqMiJ8Z_WQE_5TufeXQlZ7sfF9C46virSfDTzG6AlhpUcE8ua9Bc2Xj1pQzVdy8NkPm62HQSBIagbteLv68Zd3ZrsMZ2GrXHK-DenOZfVPtl23_4p9dMTEqCGu78kimQoJRcwuyJmU9Yol_9rY1Y0WS77k8-2gWAXp1KxdZDrd2Jn5PbsJC-5nmZiPL_A5sFTkwAgMlP2JsqWRPJp2OBcu-EVbfSGpLBIf4mLPzk1QLoYL5292fAQRoLkEQzwG_vjdXshXAbIESpaQqQXmkI5H_9BGmbR2RAdIskfJRnhpFTxtNtNZhpq7ulhsI4pZgdlIrI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=DXx0RobfX25VQ6LJHqMiJ8Z_WQE_5TufeXQlZ7sfF9C46virSfDTzG6AlhpUcE8ua9Bc2Xj1pQzVdy8NkPm62HQSBIagbteLv68Zd3ZrsMZ2GrXHK-DenOZfVPtl23_4p9dMTEqCGu78kimQoJRcwuyJmU9Yol_9rY1Y0WS77k8-2gWAXp1KxdZDrd2Jn5PbsJC-5nmZiPL_A5sFTkwAgMlP2JsqWRPJp2OBcu-EVbfSGpLBIf4mLPzk1QLoYL5292fAQRoLkEQzwG_vjdXshXAbIESpaQqQXmkI5H_9BGmbR2RAdIskfJRnhpFTxtNtNZhpq7ulhsI4pZgdlIrI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=eaKpFzTIJW8ZPMROmNh17zw5RUwqn4mqZloGPeRwCSSXPXgkaS0fHp-C-xrM6vC_NymBES2xPfF4yGjPelc1NALElQhPadl_PrkD9NehgY_XU_6g-GQ_3n4lxweDodft9JECOsIsbkwnXcw0ubYckLDQYsSy6gszS4W8p8AkpbeFsqPPnR2BrqiYicNnvIf7ACwT-gz6YT26S1sAPf7bPrSwAN4pQW_gldL-p7MVXqJJkskb2m-l83e5QENuCchRNWKza4RzUGb67VmMA9KUuJXntLe6I8N77XhQ9mu-utl8bpnN386T4i1C-cFNsiWzMwfLtyhzBEL-uZcI5zZy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=eaKpFzTIJW8ZPMROmNh17zw5RUwqn4mqZloGPeRwCSSXPXgkaS0fHp-C-xrM6vC_NymBES2xPfF4yGjPelc1NALElQhPadl_PrkD9NehgY_XU_6g-GQ_3n4lxweDodft9JECOsIsbkwnXcw0ubYckLDQYsSy6gszS4W8p8AkpbeFsqPPnR2BrqiYicNnvIf7ACwT-gz6YT26S1sAPf7bPrSwAN4pQW_gldL-p7MVXqJJkskb2m-l83e5QENuCchRNWKza4RzUGb67VmMA9KUuJXntLe6I8N77XhQ9mu-utl8bpnN386T4i1C-cFNsiWzMwfLtyhzBEL-uZcI5zZy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMJv-Pal6DGCafUpliabmeZw-HASK7y6NKNmzPemPGqY6MAWjT35wQqMfyApbiyYSFMFi4lXO25uTquZWy1D1k33UTdyouONOwo-PHiFMn4LuWp2NMH1hiVG3gzkm_V7RnWOv1DzVLsjgzVLwNNUlGOl5lm4M6CCZ0Zk4Nza7Vzc2kKA9JUcLdQ9iDwszfjpw6N3quA19N8laQpvVWO-gCHp2QLubpPGI73rNsvE-XUrgFD3WhlwwyONjsQIMTpbTUloP8pISY5kYWZuxAdhxp7sn91kbEvaAsQ6MC4_zvqky5WecN0Jkz-rbn_RQ-Nz9fZMRjMIK-ndCgkIRsBt5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=oZQGwaO1WxSarUeQwLGvhtMuX5j9Km2zgwugapauzfZKuyI4fRw89GEhV7WFtdWhpew7f49iosV2G86F5rCSmUCsn6dqREoNUq5pu1kD2N7-9CEyxOXhqA-m4PpNvT59u_vOG53whwP9M8X7-AuAJBq3g2mKxCfbsz-V_fCsabnuS7Iu0PQw6efsRpWMZWFLzuWtooIP28Yg8x4LvsubaiCmkoqz6PmpmB8XxyNEKW0szFtr5zL0AfTp4vn1Fucal9-7_Kn84n_yWB0DVfTXevi6FccNOmj94ZvuURN4aKoa8GuOrOCOH_tP9Ws5DnkKMNZxWIHfz86O4iOnH9YB4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=oZQGwaO1WxSarUeQwLGvhtMuX5j9Km2zgwugapauzfZKuyI4fRw89GEhV7WFtdWhpew7f49iosV2G86F5rCSmUCsn6dqREoNUq5pu1kD2N7-9CEyxOXhqA-m4PpNvT59u_vOG53whwP9M8X7-AuAJBq3g2mKxCfbsz-V_fCsabnuS7Iu0PQw6efsRpWMZWFLzuWtooIP28Yg8x4LvsubaiCmkoqz6PmpmB8XxyNEKW0szFtr5zL0AfTp4vn1Fucal9-7_Kn84n_yWB0DVfTXevi6FccNOmj94ZvuURN4aKoa8GuOrOCOH_tP9Ws5DnkKMNZxWIHfz86O4iOnH9YB4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQjp3aHyCkNO04FlcN-Z8FnUZ3VtzoDWh53-xBbNrM0JzC-AGq-RQMYwacfQ6MgtYoFrso5PSGuwIcRcOGhusohrP0ggYcvqkL7rlQz6v9Ib4ihat9Kxulp7U0m5Obn0pAy4u5fvelcIOZP3maLJXz2f4WM0Xf5_GsbssnYnfuigfu8Oo6HYhaVs_rsyxLVGZ8dkPTSGtNQfKHNMfK83jQq6ZOFy5GSkE35LAXYsBDlnmPuigonjptjuMCmHgMs5G4BNGmP7uRfStDbYAABQDT9XBWMY8-sy0yDye25rQVlfQV7U4QSrzJGYzoNwbhOECuhl5AJBc-qHaKraql-EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dptRR8XdeZFEy_db7kqNhFMt58tpjQNU1y65_zZIPGECHndc2bXliTW-DyYzdmIkjuR3XJ88oO2My91ey0FflZhiCwGUj-M42HlCWCX7yzJHEJUjsGWSfc3kOIZUJlYT2nBMDNNUyzJwfZKT67PQXlrD8WTRKfteDWzFMpOkrodqZ8enzciJR5g9fnUAXzHc3DMmsS9E3Shn3PyA-TqvjW-MBBsEVhQxX5kAa4zfEk_4B6gr_E_ZlQizQ1ou7rBy1MwRCaSvnr1Ol_Nzp7wuJW6NeEYMDGbY53FTTc1xhEC7KnJReH2sx-BeyBv0ckBbs8q5uinATycbErU71acFGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=jPPZBIBVGkAjTJlFsTrE3VPfgYJDvO7oylnf5pIhxqw9qecMVh-ss5xAUNIlhHRi991r43X4eaby6fhFCOWofCWmfiBfVJGlmJfu_CaGHu-QFWpjF249jmhe8RazE7fSoqzJ54XiRYmgmLQ0FaqXuTa1NCJM2O6n8BAiXeaSXdirBDHt0gQad5Ym40ChKec6tlOxsS7Pgu3urm9BIR12RbsUWEu0Z2kOd--AKNi7JYqpMS451C72D9_HLed0o6EMBhgT2QNUoKNMiHzbqhFRxa1_E7FP6jrJviqfUAPSiO2GxS7BMtAcKOJccbl3TLkHiUhkFawnd3vNxDcG1q2pvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=jPPZBIBVGkAjTJlFsTrE3VPfgYJDvO7oylnf5pIhxqw9qecMVh-ss5xAUNIlhHRi991r43X4eaby6fhFCOWofCWmfiBfVJGlmJfu_CaGHu-QFWpjF249jmhe8RazE7fSoqzJ54XiRYmgmLQ0FaqXuTa1NCJM2O6n8BAiXeaSXdirBDHt0gQad5Ym40ChKec6tlOxsS7Pgu3urm9BIR12RbsUWEu0Z2kOd--AKNi7JYqpMS451C72D9_HLed0o6EMBhgT2QNUoKNMiHzbqhFRxa1_E7FP6jrJviqfUAPSiO2GxS7BMtAcKOJccbl3TLkHiUhkFawnd3vNxDcG1q2pvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=SLzUW0kTdZ5v8CZEEjFGEa7AReRTqRkIb5KFZzivmWSavZYhTA2WgRR4HSZeC2yMmqoUsXtZZOgZsGue0VPo3vC70iEznQsIcn9aKZ5DtOWEjN004cFRO9BILqNCPcd88ohY7bG48ZpT75yCB_zOfxkxirXPRlJYIoXapFpQJSrgc579dnDOxKtxsgvBoPrHkFOtk8NozMh_xLVFUgUGr5eZ1Q8p0O0CO7b_CJlO_MF8oEJK9bQNFMxC5Ax-tRsNmezrlgaUU1hyEX6iDfRN2Pr9Subbe2UfbiasIvmqBhygO_Fiapw_-hy_c7ENvcuiaNk5tbLTqHfc6TFiuJNPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=SLzUW0kTdZ5v8CZEEjFGEa7AReRTqRkIb5KFZzivmWSavZYhTA2WgRR4HSZeC2yMmqoUsXtZZOgZsGue0VPo3vC70iEznQsIcn9aKZ5DtOWEjN004cFRO9BILqNCPcd88ohY7bG48ZpT75yCB_zOfxkxirXPRlJYIoXapFpQJSrgc579dnDOxKtxsgvBoPrHkFOtk8NozMh_xLVFUgUGr5eZ1Q8p0O0CO7b_CJlO_MF8oEJK9bQNFMxC5Ax-tRsNmezrlgaUU1hyEX6iDfRN2Pr9Subbe2UfbiasIvmqBhygO_Fiapw_-hy_c7ENvcuiaNk5tbLTqHfc6TFiuJNPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjdNxL8hsMENwqHpzNIzoiT9t7sjfwtqg1InIoBXs-bHhMxdC1TTzFoUuM3NIN-gJEplIGsce9Z2cSu7UwsxgNB9O0-CoN0O4jjyi1H1OTPwawjqRBEY5ehIFWxw5ogjf60TJb317QDrc6N6iIkQK7KEUPH9xwR5qX-LS6nuSRCKp8i3Ol1gMYMzSP3rlBdQqJbhn81zvh0ijbOKvvXXDVBVyMNfxWyS2eKvFKS0ozN7O2yzbzmBxD9ktKr2GNbthwepRKJq_31gV8veozi84MUgI7RL7QBOMEY-S4WDjWsAVkhVLEPovdcbYD7ul7mFYhiExTK07URETl4pLhunoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUkrNRcXG4rAAAgUQYWDGbohCp90-T4GKgDUDMCgDTHYSp8zLv55rn2x8qRjzCjejkJvWJ8DJ5ij-NoM_qJ0ZI0LjrbZBY5PuYxqLLYberF79yxwHP2zrLDQC0fybu1osi3w_3TtnTGCDmBnECC5zzgb6sDtl8OPZAOAxfh_zHxz0ed0CBUUkD9q_mBZ3SC4jKLL8IlYHR-bqgKCXTNDh2Te7bX8EE1x2CxbPfSL2FQ98IkMIspQQfj7dwRU-1ryygEkl9xghzXtNZYAW4edEc2emHx0Ow3i8HiQGn-R8a_NpH6bZc7xaaABYiegATC9CuKadCctHvLjmIQnkJhyMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=k33nljpCxoHVpGzm8x9nlJ90JunGC41oqtDuzJhLffH511NPR4vYsLPuZIdjXLvHcllYdM-lJ1IbJfKTq9fzDT1CXBW53D0HxOiUn3Snism6lP76ThTmrLHRN7vK3JwI7y7Ieqy8kxtmkm-U0yPl6OAH3Dgs2krDZS2Iei2WROchE7d7Uog-E0300rbSOKuobgXRc6h701ZP3BsWaHmoi0ofK2ROSWhIm2YfuhwMBdC3win8EuXl7Y24yHB61NE1W2uT8_6xaU0t5gkjEBE3xRx63qpiHgxFViLhs-dEEL4BeMrrcCr8TTtEcXALEV1HkHhJbsDL8IUhAWc2gOdXIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=k33nljpCxoHVpGzm8x9nlJ90JunGC41oqtDuzJhLffH511NPR4vYsLPuZIdjXLvHcllYdM-lJ1IbJfKTq9fzDT1CXBW53D0HxOiUn3Snism6lP76ThTmrLHRN7vK3JwI7y7Ieqy8kxtmkm-U0yPl6OAH3Dgs2krDZS2Iei2WROchE7d7Uog-E0300rbSOKuobgXRc6h701ZP3BsWaHmoi0ofK2ROSWhIm2YfuhwMBdC3win8EuXl7Y24yHB61NE1W2uT8_6xaU0t5gkjEBE3xRx63qpiHgxFViLhs-dEEL4BeMrrcCr8TTtEcXALEV1HkHhJbsDL8IUhAWc2gOdXIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=FhvexuCnm9L85ZPxYSc6HFmYoKsB1bMhNZovnTHbJSdC8fOLNNWJ_ZGq5uVl2yD2ui8G3c_DcdjOzm2BBHlporUYJ4CzHZvXbtSVUIzP8SJS0f3nf2sxio6S2qd3_nxPqUswe5Jokdrvi_q0xFWq-BVXafU_NArMq6coX3Hr_qRJ0GcDGQt4rE9d-8FJEGv_8zGgelyi-tXa94HD3vmwQilMRuC_W0E3LTdU0Ff4YiBt5_AYdqy3zo3CM5BXWLnHsha2Zqva8NVEx3XK0ZTq_Vmog5DlPeW78it-PZ4TKzXBnE4M_2oUfjE-yJcT6QXwspNRLXRcseteEdX5v3DGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=FhvexuCnm9L85ZPxYSc6HFmYoKsB1bMhNZovnTHbJSdC8fOLNNWJ_ZGq5uVl2yD2ui8G3c_DcdjOzm2BBHlporUYJ4CzHZvXbtSVUIzP8SJS0f3nf2sxio6S2qd3_nxPqUswe5Jokdrvi_q0xFWq-BVXafU_NArMq6coX3Hr_qRJ0GcDGQt4rE9d-8FJEGv_8zGgelyi-tXa94HD3vmwQilMRuC_W0E3LTdU0Ff4YiBt5_AYdqy3zo3CM5BXWLnHsha2Zqva8NVEx3XK0ZTq_Vmog5DlPeW78it-PZ4TKzXBnE4M_2oUfjE-yJcT6QXwspNRLXRcseteEdX5v3DGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=W3GzunJRA7SO0xhwpcx3sAHqchdh6sfDEg_mB5_WCpZK8CkEJidkJBeJi5XdwM31b0MbtHAbFUP-WtmU6Y8C2DQouw5sILeBdmICx46MbMSPHhLLBl3LZyOwiUFRl_2Mc6lsHwPMoGO0TZrsCaNfUEnJtHcWFwJwhsYFNQpLAnEjPGgp9OAjL4Bdb9JiuPreinZrdXLQcCsoc_9R15acc2BqXyhK5TAF23MIq-hQT3LcTuJeURCuoFJJ45cw9M2p2NEi4FAAuU43nYbGSsE6FaXbLhvOcBMn_R6lTbMB3zNjiV0JFrdjSlDmtJ2wcAPwA-tq_UU3k9OF1ZTnuOiTPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=W3GzunJRA7SO0xhwpcx3sAHqchdh6sfDEg_mB5_WCpZK8CkEJidkJBeJi5XdwM31b0MbtHAbFUP-WtmU6Y8C2DQouw5sILeBdmICx46MbMSPHhLLBl3LZyOwiUFRl_2Mc6lsHwPMoGO0TZrsCaNfUEnJtHcWFwJwhsYFNQpLAnEjPGgp9OAjL4Bdb9JiuPreinZrdXLQcCsoc_9R15acc2BqXyhK5TAF23MIq-hQT3LcTuJeURCuoFJJ45cw9M2p2NEi4FAAuU43nYbGSsE6FaXbLhvOcBMn_R6lTbMB3zNjiV0JFrdjSlDmtJ2wcAPwA-tq_UU3k9OF1ZTnuOiTPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=N_lo27g-KvVdwTw0J_9qDIh_X-2fVhrY6UNB1u3XJdO1X9cBzVDX8K8bPgQly9bqAXoeFp1nRrTnAkJ9Gvfuk0oe9RTE8VXmWq10f7KJDy-VuXbuVJKjRtXNxkjvRS1jQgpKEhUomww87dshcCoVWtKrbilH4x-gsLRha86UbIaCLa_uPeQheiuzWhs9809e5ihU_tTc_wt-zduuRZy2GTId4yuwDGSaDNcP7JZ0wNUeBoVFO0b9596dPyfNdyhX4O7q3rfs92WE_1lc19GFlT6dMpvHONFxIlFNl0tDseO-mAsOAk5tsaikFRrABl3HTQeRhp-qhJYkwR8KEjqY7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=N_lo27g-KvVdwTw0J_9qDIh_X-2fVhrY6UNB1u3XJdO1X9cBzVDX8K8bPgQly9bqAXoeFp1nRrTnAkJ9Gvfuk0oe9RTE8VXmWq10f7KJDy-VuXbuVJKjRtXNxkjvRS1jQgpKEhUomww87dshcCoVWtKrbilH4x-gsLRha86UbIaCLa_uPeQheiuzWhs9809e5ihU_tTc_wt-zduuRZy2GTId4yuwDGSaDNcP7JZ0wNUeBoVFO0b9596dPyfNdyhX4O7q3rfs92WE_1lc19GFlT6dMpvHONFxIlFNl0tDseO-mAsOAk5tsaikFRrABl3HTQeRhp-qhJYkwR8KEjqY7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO3ImtHrMu9JXFimOvGB8xcRJwc3aM9WlbV35ZslGdU2n-AGVqO98qt-3u6H8Md1ZXVV-3g5nzaRQwRt71Xvk3BbvDx43Q1anF_dmsRIZNLdzftZfxLi2R7LpyyAF5yAKARyg5smgn7XZmJjb4GzZk1aKzbEUc7jPBZDh-xlTje76gvML8uNv8HqAetwaPaVityJooxqRqLPW_rMLECRNt-N_bmNsCF8UVL_Xd-zug5eFo9uWGbDmy1-XiTQV1tIe3R53hrtxO0aax06Cx2cFPuNBUDs3x-jGMBc1FXtsMKjqmIjO2aNEedHGjMLKcJSHYVrx7PijghKBd2C9Z2Phg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=el_znYx3yK2lAhZ_fDLzUbozjBUVYv-3ZWRoU0fqLjXVY5R4I6sfvRIgTRdn0J8Nuv0z2TUJOwc6b-zxySy1lY_HmzL50gETHhzvcng3B6Sl6QrjSYv-oH0P390e0SSZsQayZ6fuPSl5Rve2OYrPgY4Yr1RuDPxoQOGWiYZdR9DqC0o_XvnEppYXjV8oOENYMu29NUzfLldBX4kE69KrbsYhyBwhItVLKhQ9_eZZp8T94Ks9nsrtUGQL02ez6ahjrN5y6EBdk8qG4yKynPCvKHIzd3UL-Ij18dfcVnUOOIVvEpsZzLmbTZvXTtRYnWnMrhnITd1EB4o_O8G6M2AwMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=el_znYx3yK2lAhZ_fDLzUbozjBUVYv-3ZWRoU0fqLjXVY5R4I6sfvRIgTRdn0J8Nuv0z2TUJOwc6b-zxySy1lY_HmzL50gETHhzvcng3B6Sl6QrjSYv-oH0P390e0SSZsQayZ6fuPSl5Rve2OYrPgY4Yr1RuDPxoQOGWiYZdR9DqC0o_XvnEppYXjV8oOENYMu29NUzfLldBX4kE69KrbsYhyBwhItVLKhQ9_eZZp8T94Ks9nsrtUGQL02ez6ahjrN5y6EBdk8qG4yKynPCvKHIzd3UL-Ij18dfcVnUOOIVvEpsZzLmbTZvXTtRYnWnMrhnITd1EB4o_O8G6M2AwMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsoUQ1oqo25FXD1kGFs4KP0J5egKj3fm0Vo40mGmxIsmUGavFrLjKGqn5NMAEKDXmuTe6jA3jyeSnnf9Dt8kPSk00GkIe-MxHhHvDCE30q3TeRZoJa1E2pVTgXVTLWLpLpvWVqKkmfG9SWnpcy0OXrRJvqkXBPLyGA_vHJvWXpZBreW-t_Po2NsctHXQ0qAucBzS1iB2jEPJVIE9cjNjffKYyMo2TbMuNN51tv5iBDbVJvI0vI859ADpOUR8S02lgmxC53Tq_jK2UvedWevSmuyrae4QCXU9S1QfdaPy5jKw1gpNMopDfNc0vZStmsLdJw586uraH0YrDZ4Xe4UfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=HNLR3SqKEo20vgjkS1vhM6XQnYZu-lgqOYSvCGsxQTcBIjZVx9wQXmxkmEGDkvREJv-ThYhOnOiBjBBxZazZuPuDGVabK2D1TMzEgI01iF8MjdoOMWyKkZINGTUtQPIMnmAXhyz4dq8et_yqTgKoAxStjRumoXo345aE8vLlC_RhpXTbkxRzi_pMkyVJB9XJmxR2mUeohxUEuC97GCPWG4qN77ijXD4CsmQRPpQe_uOj59oJybrVtK-5bdQfLK0-ZVdSCZlaTlh2gJ1pQdsvQhGVkiHOPgi2C09wpryCEUeVngO7iLFQuclRrIymSlBxgpIqoyvbN1UszkDlpI0xqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=HNLR3SqKEo20vgjkS1vhM6XQnYZu-lgqOYSvCGsxQTcBIjZVx9wQXmxkmEGDkvREJv-ThYhOnOiBjBBxZazZuPuDGVabK2D1TMzEgI01iF8MjdoOMWyKkZINGTUtQPIMnmAXhyz4dq8et_yqTgKoAxStjRumoXo345aE8vLlC_RhpXTbkxRzi_pMkyVJB9XJmxR2mUeohxUEuC97GCPWG4qN77ijXD4CsmQRPpQe_uOj59oJybrVtK-5bdQfLK0-ZVdSCZlaTlh2gJ1pQdsvQhGVkiHOPgi2C09wpryCEUeVngO7iLFQuclRrIymSlBxgpIqoyvbN1UszkDlpI0xqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzEoe0C1YSflvIt-G2fSPhVemrwWzxBvvYPWXOFPVMyBngnLzgB3dgaXPOAsFeTZFMmBI4xleTjnigcvvcjZQSu32IM8j-RKDurNwnL5cDZxwNgRjKJLYBUhrrVXUleCyC4SD7iP7K5BXxM1poj8pv-cPpaqO-hRa2qNXlTRsf991KXCsr2Y2mdJJGJ7KYSsJaKwDahNv6Jov5RYWZDjdl-ANckeLaLbZPnWOZyMqTEhxE6g3j0oRJ29tb-OC0sR303RBMXqzGSJkOiLKfS9gr5OKuLamA8d7t_xxXcVGhIKHISa6rJCUVJNJVW08imlJv4M7g8oVjIyPAnkQbBrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=vtL2naZUgMpDlst7Dh6HXTDC1sxbzwgwPgMLDXuBx6GNmxOIZ3fwiyZa1q4x15Ty7G7py_WONBiJUlMQWgGA6_j7ClZefJChAdansUWqu-BtCkzqpP9MOKyCUV4ZOGSONjlPpOrDkhsS8M7tkYqpwuHQjN55ognJy5k0WEW8AlGsNnix2Inn0C26CwX_947AoW3IbMJBlMbpUos2AUMsmBvC4KHf-Q_W2esCfa2es9s5CEbY00yCMUQCuZsFa4kdW8-ZZy3cT7p2C-aEdoD3SR40SIfx14gVZi31ic1dmyc5ekM-AmsH_nEBXXb0HE6alKZs-BNheK4_mjmm2EGNew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=vtL2naZUgMpDlst7Dh6HXTDC1sxbzwgwPgMLDXuBx6GNmxOIZ3fwiyZa1q4x15Ty7G7py_WONBiJUlMQWgGA6_j7ClZefJChAdansUWqu-BtCkzqpP9MOKyCUV4ZOGSONjlPpOrDkhsS8M7tkYqpwuHQjN55ognJy5k0WEW8AlGsNnix2Inn0C26CwX_947AoW3IbMJBlMbpUos2AUMsmBvC4KHf-Q_W2esCfa2es9s5CEbY00yCMUQCuZsFa4kdW8-ZZy3cT7p2C-aEdoD3SR40SIfx14gVZi31ic1dmyc5ekM-AmsH_nEBXXb0HE6alKZs-BNheK4_mjmm2EGNew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1I0OoirvuEjgrIORGDhROULgl-0TELEYoG2TBLoTx3EeTJ4OTSU2At3blJVTJ9E5Hjq2eHxbWuc6HJZ3WttTVq29VAR8IQRo8XyGApN4dfLx0dNgJlV4SgrRAGoPqH84SGByuFkXZ5bJJKOu-ok8bTSaiY0TgS6-GY7uLbY4ByGKWPCog_MjPHgnAgs2O1CSsENrvfiL6HTB8Cr_V1YxJATZcJqSCA4H51MZJv5LHB-YbXQ9l63At5lRBQ1cei3jJjc3nV0YVH8HEyn_mAdFE3gsD2qoNHxJkarQHC0Z2YXoNJcZqXqlQeNIE9whWCcKPS7CpdCGI48KdrRFz-EIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
