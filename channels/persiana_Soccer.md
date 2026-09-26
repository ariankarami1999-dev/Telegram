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
<img src="https://cdn4.telesco.pe/file/D1YSc4QyUKLklhC20sbDWv_i2pa16qmPt4GYYyagysRe0IoQ8KtpKeTMelgNiGB-9kZi1Z5ZH1a5f6wy0D6oVLaOi8kUrcZxBeKPeN8ow4YKzi5ZQAQR5rqzJyLuhwH0zPqyIPI3bVqKKNjanr8G8so55RIUCQjZWfCEFQ247M644ixQn3692bSmlemN4J5a4c6XwDJSRW_luFHLPG4grZKUZUNWYMpG6oM7SPBaapAdLGfJ6pSSgiEviXYErblEoJnT99rSwTsPY7GEe64IBNJzyZokj1vR3W3g7ew9ri5eU3Fg5ppDDfNNwsjaQ3bANHPl7zcyS5orM5qQ1eJW2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 446K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 23:30:39</div>
<hr>

<div class="tg-post" id="msg-30510">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLMyPVImZjlIun7YN2JpiMdHsQXRykUqW5SJGJTnuAcqsU387FtwzcAZcXzmUOb7qgnsXOeFn3EDd4HfcfgoILv9sSI7wBI-i9PsZkhTvBZE3MooIcYvpAqdAlWDpCVctDgC-dHJUzawcWc61m12vDSfyM2WSGV2uLeYhBjBiohjHKolbP0Vr5QCFSPsx1u003jog4bhLwclFHIfx6VAdkTxuxHegN84C5XCj8s4V7qWGBMXgPNscN06RIiS-XHtY9Ncb-GR2rNJyrT1yg3lzwW_kPWUZc5pDEeKIkV8HD5Esp3xXsAjaEt83kaJ3fHFj2NuMT6wCgQ94D6n355xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/30510" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30509">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igkozzQ_wKlCj0hs6rUn8j8IjgPARTsY7PXj1GaI_BwXRds2VD7TAZkmhMymyLuZKu0NWelaXQqC0YxStHEps-_tqFvUJfTFa7wcR347e1KMlbYuJULtjjZq_d8_XzPhWKwAJrs_MT3yBoFwhgINXxhZsiQecpgvJLb_SWknqS-zICLoJv7Az5eo6jlBu3SaI5xWy5w0hJYVlMiBIRUBFniVgHvbefuEsZ8T0PY4i4KHLaXZ1SkBCvF57b1oU3Dwu3BD3GU7q9YUBR4I5DInIOaW49ma1n7yrMjSnuHr9Fjp9-walJhi7FHhMdU_B1zY4rXuD2zLwecBN0eBJYow_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/30509" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30508">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSQEroSlMuSrvOdmBXHHmJqccqzwFRPBhBj_46PQCGZP8VjSTv4KHDYGMM3ZCkegTKf4FH7sSHdwwQ8r8fkJScO9QOOVn_SyN75K07Gw6upIAZm02oTTvo5aEa5wWg7oKmslK14Cz8lXzRifQVLb5v7Z0xTs60fSNeW0UKye9jiFGIFebPlihw3w0CSGulAIzHL3P_B_tJKWLruqBcKel4BW6oKwqGwVrFoxEfJE9u7GaWB0RySQ9Edo9hVFcOMCrQL3CYaCRBLygBOssOfIR9mpvlqdM4NAzm4Q2ctwYAcBP7jH9Ttbq5rR3dbjv26FcDfEdXPhXhlnZsl5ucZvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/30508" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30507">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMdKsoQCEKYBld4ct-0QSaFewYUwGZc1GNmNdiEdSUVm0Ub9dFkMFKHFi4C11GL27s9bH5ef2Ldeogr24uYqt9QqeTXsPlvDAlozTHyVCB4nM_Y_br3QMOSGX645_Jm3DftdpBT5eX6vw0gee5orcrKr4IEj9TKBQwVq5YkLZfwKA85ORJtplDkfXGrAiDwe7vEHk3M7vZTw0LsE0vAYJBB_E0GyQ53aobe4DRHqt-jR1kPfcFtLNbm_F2CFAOP5Oyzubwx1Y7DMHshRFg1az_7SaZ_VoGiG5y7NDUNaZ6_tLRlRPWlgn1Rc8kljykrb3CMIe7BphNYQuyq16fwJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا دبیر: مهدوی‌ کیا یه گل به آمریکا زد و از سربازی معاف شد. حالا به علیرضابیرانوند که ۳ دوره جام‌جهانی‌بوده و پنالتی‌رونالدو رو هم گرفته و مقابل بلژیک آبروداری کرده نمیرسه از سربازی معاف بشه؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/30507" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-ZWPwSz_hMImVtKapUChW4TzJoqGlcFu2jfA1EbX7-EOFWqNXU3edE2xN7B1vh_ZrbTXKfu7NCSJR0r5tnDE6hDIbV2F4FCgTID97Hgq-mqrDwC7wcBul8ZjTszSSPXrri1hDM6BGINE0gadfeeiH8RMMB3Wo0XpRms-5UR7CEPMrA4hUJBzUbES0iVT_WYd2c3AKGsemxN95UM0D8jlAz_Nt5zB5Q5QDZo7Rt3RfAJ9MiZ3jiFxDruROaK-npmKLU9QwHJcO7XK-magUKCKDV-ScP0eeWTZkyZrN8dVE7Jy09ZnN_aapIkrguymhSXAY_iFryXqJrlDfaQDlfB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFHr03HlYp9NqTezkeUf-k_K0yhQvYBLNxGqe0Jvew70OGkfbrKW4t64GsqUuluzu7WDQVW2fB7rURTVspSjb-mail0KbtIzU2eI-_8VgESbM8aniStFq_GZuflhoulRE8-1-nYrklx8jqQNlXccNAUinn7KuIbAeri8RDVJ5Z_8rm9DFsMezRzGyl04iPFLSBhiTxD9KDJTfMRrCeLQX8Wz0zKC290e2HRR5_4rdC3d16-V2HY3BK3A483Op0KDr2xZw5Fczijq5dBN0Sxv12bXOIChQYY0L4_RD9DZA0BXoD1qJrqNkKA19m8qJGKfxZkgBBw816Rh2CVcs38WzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/30505" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vruW-sC8zfnD2KQn5yMl0M69jOzMMdzQR7Uys7wXlI3998dAgg-qMgKQIuBM4nFUxRBtUa5pWkN56myAn1p4wwpQopImjjS_Va2Tqxx9dwYG2yg73lPAWf2kiL9gtADm04zaKba4O_kjaIzl3wmtv265wJcHqJrbQ1hNe7HXYB3ZLCiyx2TryvBu3Jl9nPiekDi5_A6Ho_bmNFUEHzp0IwG8E-DAyVIlkcQ4J7nN0fVERVv2Fn1-X-UdmfUCm1dQBFB-i6oTjfdo3wVPk9G9bbtFIb7s2diPXn9bQyYS-5yyKKI50WlNBJ4IYrWZuc23nvdgJ09ogoSgC9x9z8lhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/30504" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaBonKpR7E0-TaHfTIgUbS7o2mHTa5B0fGTF438bcpejlCZLArFqt6roZbNlzusjcV8JfswY8PrxpdmDDgRkPgVl9EkyAJsJlA3Ng8XGTCojiqPRvtOQ32tdcKiaWgAFM1VOh1bUCHRh6vA_bB7iK2Acx8TW8ZrWkztQM_JzwXWIRvNU4OP8_ZYliH6tP5KjsBeTxPW15vzuVm4JsKLkUrZDQXEEHfriiV9ZBV-zmsVvPmUAPlSXsWt_vX-ESnKJuB9DofZ_OSvwVW4DxpSK3Qhv8TOXFAppB2Rma3nKQuvEgkQQuGrKumkxbQY9tzE31TU8BuyxgecPc8_ryFRIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30503" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=oNKCPYWqBz-W_CE8TgUFloeYtL6w4cUTikkvqVbIE61Ez25nGHmEFVgDuWIWiYUQxOW5FQqV03KopV-rk9hAlkac_4wFQspmsrsTwEwcM0ro2EOXRNiiDA4UcMK_XnOiWftGL-iS4CDibSV86FxB0UZCZQsdPqvuPpjgDb83J9vr7azwWYy9UgGzkVWk7T2cSCrHbGOH5cUZ9l-cJ7b9eenJxpn5X4VyAuujbmErmxq4hh4xJTm0PDRFzFoXhvoZmxq-Faip4flQyzLXD_74ScPVae-Eb47aNt_4Rjgcf8x00S7Yi6U-yFbGeYoaBi57W8ELmhoAD7EpylyNRMyT6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=oNKCPYWqBz-W_CE8TgUFloeYtL6w4cUTikkvqVbIE61Ez25nGHmEFVgDuWIWiYUQxOW5FQqV03KopV-rk9hAlkac_4wFQspmsrsTwEwcM0ro2EOXRNiiDA4UcMK_XnOiWftGL-iS4CDibSV86FxB0UZCZQsdPqvuPpjgDb83J9vr7azwWYy9UgGzkVWk7T2cSCrHbGOH5cUZ9l-cJ7b9eenJxpn5X4VyAuujbmErmxq4hh4xJTm0PDRFzFoXhvoZmxq-Faip4flQyzLXD_74ScPVae-Eb47aNt_4Rjgcf8x00S7Yi6U-yFbGeYoaBi57W8ELmhoAD7EpylyNRMyT6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک گل فوق العاده به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/30502" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USBlGe99JpedingO2yElkolvCGE7TVNWNlq7zKgRAr0F0KQ_9UVGsCCsmC6YwIu1Oe3br9dUpxJpQoUqQwEej9dF-6M4tLq-nCPHLjjoSP5bqpp-Y2oNq_C5FIrCMsG0NmpE-a_qWp9EhY2eqsGhEpcn2wIisrRh6Hyj4RiE1CiYUXL3h0Au7AVJznpJAxwVhSn0yfo1FDVm5Dvdp4FsR8Q0Jagaa43_5GkHyieCAdo_SdosAkzrYHK8jN0jQXulS7AYPn1Q-autnwUFXXXOj9kmGksWB9lxppHaV8Xzmb5nCXlaYDKp-ZNNu2A5sTN3YaCkr02JJMcNwIMLxn_VIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
خیلیا نتونستن از فوتبال تا الان سود کنن، ولی ما امروز با فرم هامون
400% سود کردیم
که نتیجه تحلیل درست و تجربه یک تیم حرفه‌ایه
👌🏻
هرشب بالای ۸۰درصد امار بردمونه
✔️
میگی نه؟ یه شب
بیا آمار چک کن
😄
فرم های مطمئن امشب فوتبال با ضرایب بالا از دست نده!
👇
👇
👇
https://t.me/+laf8I3RIuq42MDk8
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/30501" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEGRTWKkmdNG-Xv7xI1L-JXxEw0Rv9YGFD7Dg8GBuG4nUMeXLzWBzyQvrVQYSbcnj_FZw5TfpLsF_vPwwGRmk5sGzDsiJh1ilQuYQ9dvPDnFLtdVxUW5hRm15v_4YZSQAgL9Xlf6E4LTMpDLwS0eYaMV3PtWbLRW9dp-fbT4a8zyZh8KKL2O-QgOJbLlgWuy8WyM3cwfrEeC4Box3XhhTUovtCcxwu7p9Cu7JigCoVUD9jJ5moVROZMPeKwoSQ6VbZZIxon6hKwFLraXxVVsICwWG9scYDQ1KOIHmR4MHMkLCn3UzoVAXCmeOWIFULjgjZnL2I0QtIpS5liioZbVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/30500" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITWkgojcOqkkhdUZ7XciR6xfm_V9VZYWOnWD0vmNmAa1ZQ5swuC7IkJPUbrithkXE2Z9krPhuQKU5oB9ZosgRCQ9lDoAMI3ZUm-oS3X9suLcYLKWQmCr73TQloyKtxnxm54V040rtAsCEz8p_oI9azp9bpG1LwaY6Fpe4AtckQuDUxGYrarPQWA1XqKVy2R1rJE8wljogZRqFhXxsIWVF-WlX_9nowc6D2XZHbwVb7eaRNebL4XjuNcs86QVvZHR70ErNhgs1OwEp_vjRQly--cAlfiNwInjWCy0yzjD-0OuiHLh4Ngp_OTz6LW_XJC9en5Fd2d78pemjj_kQZKsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d92fMGvm-C6iJ8RHYkQR4TsbEJENv7x2EH6TNMjAcQIV60I3Xa_r1UiigKsATjrSV7eiOVIaEgDOLuzFKHQz-y7w79PuiRhNuO6s6LHZPtlx61ms8MNvHmNKsHsnqyjkdF568n2MmcmBLz0-O_lmEq4t-PKRo4S96d-KeUtBn-zysKk-jFH8THIf2R33cc5SAk1oHTtOuAPylZvsJivgM6726K-I4eBkdlg8kmEIZLhfqqGjI3oUnxoDYuPV4iECHaOfH9n3cMvn0_sUj-3UiGn4vxs3e2Pu3cabNMq0rWBkgigGp7VLC1xYZ8vez80gC_890MT_z_YbKMwAgVKPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=d-OpZZX8pUpFnClSP0KHrvoNAFWdi54_xAxVdM3tbKRlMO893fQXf7NO4xvutiBzI7lL1MjdikrXf4Cqf1Mcydcs9E8lpNMZNvbick4eQy_sJqFbD7Z1_UK-zmH29EKuCMHYf1-_sGypDdTqvMDRoQa4MXiOna8uvrocY7Aah4r6loPtYr5zOL7bktJ0WjgpiPkEh-s-vSBuBvhvRbmiHioUXAbSfaNMaAzwlHNKs0mS3yEipi1j5GPBjc5uCoTBmXaToSQztjeYSfLYv9D8Bj8S_sjiTsRBhrHRFRZKcWHK8gx2XU0OjBnMp_sm3XrWZK8niQqoD2XDsC_p8XyGQ0vyLZt4-HG1QOnbIvEq-ZUP_FpAb7FoRPuBLpirS1rx3P50iG2FjS8w6YOcDJdv6t6IXm8FzgMvajB_771Pw7oU6fDCR7n_BMWaS0AOx0dUYA9_xz3j4tBbWri-RZHBvH0o9L84av0JACuSniWuiURLIwfCNbvrRzgjvmbEdZ2KdckApeEaBa9tPBuyQOJ7jdbqI3kAJTkKmZXfm8DBGz19oVCUAzvKkxwZF4SvlJQaf2FvYVCiDAnKtue_BNYSSjBBL948tOA1e_Eq56Z8T6t71GuaykaWOPQQvtd9m7E8Fh75hKY3jY4nzD0tebyNgFU-CH8f43j5dCX2XmzErgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=d-OpZZX8pUpFnClSP0KHrvoNAFWdi54_xAxVdM3tbKRlMO893fQXf7NO4xvutiBzI7lL1MjdikrXf4Cqf1Mcydcs9E8lpNMZNvbick4eQy_sJqFbD7Z1_UK-zmH29EKuCMHYf1-_sGypDdTqvMDRoQa4MXiOna8uvrocY7Aah4r6loPtYr5zOL7bktJ0WjgpiPkEh-s-vSBuBvhvRbmiHioUXAbSfaNMaAzwlHNKs0mS3yEipi1j5GPBjc5uCoTBmXaToSQztjeYSfLYv9D8Bj8S_sjiTsRBhrHRFRZKcWHK8gx2XU0OjBnMp_sm3XrWZK8niQqoD2XDsC_p8XyGQ0vyLZt4-HG1QOnbIvEq-ZUP_FpAb7FoRPuBLpirS1rx3P50iG2FjS8w6YOcDJdv6t6IXm8FzgMvajB_771Pw7oU6fDCR7n_BMWaS0AOx0dUYA9_xz3j4tBbWri-RZHBvH0o9L84av0JACuSniWuiURLIwfCNbvrRzgjvmbEdZ2KdckApeEaBa9tPBuyQOJ7jdbqI3kAJTkKmZXfm8DBGz19oVCUAzvKkxwZF4SvlJQaf2FvYVCiDAnKtue_BNYSSjBBL948tOA1e_Eq56Z8T6t71GuaykaWOPQQvtd9m7E8Fh75hKY3jY4nzD0tebyNgFU-CH8f43j5dCX2XmzErgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=kstWO147ItG8YDyl7QN-lR4g1N6Ow6brXsTRj_FJUuB6EzokQKeiKVB95HjJ_eCUgXoEBnU1pW7ibK4XtWg5UMClstB8nblu5SV1iatk3B-L8HTItA-O2Rlx3qvk6tvVQ44uABwfQTAxyQrxUwO-bG8i1AGjrnyxUd9m5FQfI8lpBGN3oY_AgWCAwtcq6GS_6SMiouNv2j6LTMfKhYxOMMgQbo-G8ISBfR90wsE00dqeeVJmWNxdlprOmAMnRut2nybO3IC93UEO7RJLFYNQE33Gyuvfiyo0L68BM6lkMK_Bx4AAiowuNbjh2lT9bDJztF6OKWNffJhq1AX-9vy8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=kstWO147ItG8YDyl7QN-lR4g1N6Ow6brXsTRj_FJUuB6EzokQKeiKVB95HjJ_eCUgXoEBnU1pW7ibK4XtWg5UMClstB8nblu5SV1iatk3B-L8HTItA-O2Rlx3qvk6tvVQ44uABwfQTAxyQrxUwO-bG8i1AGjrnyxUd9m5FQfI8lpBGN3oY_AgWCAwtcq6GS_6SMiouNv2j6LTMfKhYxOMMgQbo-G8ISBfR90wsE00dqeeVJmWNxdlprOmAMnRut2nybO3IC93UEO7RJLFYNQE33Gyuvfiyo0L68BM6lkMK_Bx4AAiowuNbjh2lT9bDJztF6OKWNffJhq1AX-9vy8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED_EKO70T3bOSE7_qvxspN-1dwemei5jY4krxihXNdYB98xpPibYvopMQaP2M97J9pgHu7WjXesXxq0SDdRnTyenP5KOvVpoJCe74rnoSaWFdyD5q0wclTVWzjiSSsJ02TH08KPS--Tl-qbuWUdeGXjYbCtv6yyKJxH9zRa2w_zyj8Viee8JiDZx3Jebj7Daal27WwXqwmklQpaDvpFkmnO-Q8i-v4fZdLLNnu-atdkfJ97r54DkC2EWfLSNuvEji6y98jV22HNYWqHUIOnTjVidwp5Grn-FQ6aSCTYnL0g-BYMq6PaJ8iMqa0Mf3w9A1jzNaHjUPJrStCqPsS3TDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAbI6ifJfmAHlO2nRyNFYf5FWj3Y4k9KEVyNs02VJEJJM_vcT4Dc0r6d0Vc0Z6WJ9X5XNuFtjbOXAzvmxtxcjept92fHW-3Mqzkfz4zEoGD3dQnrHiTBEQrlLVaj-x_bgTDxH9pOXwNedvWuabJJ43ENFte0gCc9KjNyguBbbabmwd9e7tgitNhMG1SussA9dujf3q8TckkdpQvqfLlNTdsSTUdLyL7Xa9nxsuROwD34xRHOyN7HpP-ge2xoct65vbOENSVk_XSzTB_8EM-xbPscjYYScHcMwWuj8aqJCYoJvPyw8Bh8WgeadE687Fzrur-InMQ2wWyvsCMQy8m4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg3aLT8B7IL6k2nYRZm9FBQJciH2P79vgLQB9jtAqPZuHSF5TqaTUx8Agx1X8m9YE9A-4tO3GRIZf9BVzeDjvc9_zQu0wj08Lk_1EkzwZLbEo1Z6pl3XT4ar2Kd6H5Z145RlbuCMVPjseXGUMDSSRI6m4n0XDp-KWDYW4EJKV5K-htfPB3DqPXknhf8B2giuz0qRNmSQrl2r9ylhOmSRCzP3Wyg6bTVca4tcF5CLuHka9vqaQn7bU0j6IDqEvdT3YqjqPX5D0p-YG8meSlIiV9dyiooK8xGjK0boSJrltVD-oy1vkXZnm4sWfofIgYPE_wtRgEI6cRIuevZNxk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN0mztnn54mq_EFbb9JePTnc6MBVF4hxwmK4ofwxALseS1zjCDfhvsNirUlbpDQthjyReOEpADbyofsyWPDjmVasHHa_fDpC8bDdpVh6TtwZOqDT3ISfigYJqJHs4HoVfrjxGl2s15VwOnnA-xHqH9fMMxTTP9m7eveq55Q3tVdY5P4QZ7UbTRxEhfeaaLSwCQ17EdDpkVp_sZvGaEMhMSnKLZejxA08pvTwj-M12lhvgJokz7jwHkTtwynlI8_qAgSXiaU_TfDauoc648SAicN_slwogSS4U9AnoHpu7oGMKyVJVhsyH6Y0f6xVyFVJfxfzoq3nTrzoWDEVUlV7IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flxYzUcghegMrOgCdbBoxzD4A1zc9_0FhReQNvjfwjPiF1fa1vAHJHtTNPvIcN0Vo8S7VVt-NWax19oepqHlPaCWjwjaA1xADLBNUTEmX1d9WCzCYlREHsDdoldEyE-P9xlVMvDd3IgMmYIMpr4xxr1L5SgJhm3vBs8a97alAvdm8rPj5VBqFz5_NsLUbBGrBWKlmB8x-DE6pIRKEQz1q7oaOizFBCiFxJIhNqc22G2OPk10RGvVLGjuUAeRT-6TWegMSAMHyzDJgl73g48s28v6AkWaQbe6RJCDI1g8Q-dJa4rMiKBOun2c3wxYwukXGH-R2byftgJhP4-7OcvGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30489">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5IarIu6hqSVP4cTgGiUtIBQLSOeNYN2T3bJpR5tTdajg5Oz4j0SKvk1AECkC1scMp-lA1CWSeLI4lh0mwkXIRQO4EkIIgt8scDXGbKKUk8HzLuZ7YNljJfXWKTjLabRSVrD8UXAZtkPHPiXIG0wMqrFIr9CUgiQc0S-U0IenFXlM1rraircKmuCm_RvdXkB8weZq1vmIZGM72PJBJvZYgIAa0QUZNcaPIHXRvpyRkrY2Xawi1S31UEldHwvpYwvoCxDyRYQmQGEfx7vnq34KfiB7PHcpl1p5oqRsiAHmqW2OBT9Ra-eMefNkCh9e9xRWqFd0xayv_SCKCp_krlCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بی پولی خسته شدید ؟
🌹
به جان دخترم قسم اهل دروغ نیستم
❗️
وقتی حرف‌از حباب‌شاپرکی منابع‌دار میزنم منظورم همچین چیزیه
❤
۳۱میلیارد موجودی ناقابل مشتریمون
🎉
حالا بشین فکر کن ببین با پول کارگریو کارمندی کی به همچین سرمایه ای میرسی
🚨
با گردش حساب طولانی مدت راحت و بدون دردسر نقد کن
✅️
تنها کانال معتبر جهت ثبت سفارشات
🫰
💸
👇
🗨
https://t.me/Sales_Bubble</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30489" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5roCUt0B3pT8dyjilvwoaO-PWklojVQkHjXUYadwUIFiXYuGpQYOyBU7b98dLpmQvnSvT9lXMXk6xxNHrtzQ1ZWIJSABSuDGFitEvQLg8Mz8UJHmGEDUlhfEEJyC954vwp6BDZpEYQ1CSG_dnoRJ-T9veFfcRR0QhUPrE7CJJe9TjqkAQZEXPSbcx1ZAkyJheZBs3J_HGjGg86YE5Xp5cxiz7O9TxhTdN8ssogKSB120KtGO-wUrZG3eq4yEKHhRPxxRA_j1EE5pziaKC-f_EcvFU_M3yj2mv1FqVCSmA5MTjeLKFfdc379O6k0k9oc1m5_zWwES564k0sq1oEGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_yUByA_N8d0fOFr2gLvVeOygbKUUeproHmgpqIeBEvLm6CV-S4P4GrY1j5V4mdTHR-QV7PxSHm2WoMyijyPKniJpshYaWl4C_iMhy_7VvlpbP8eS-0AfS3FlVFr9eGXDw2kukgmzJiJ-UdVmKexSsk8qNDwtKGYCYn03y4tgsWl3JRlwfEwe_CL9PzUdttWsi7gTz5Z9kCeW89Kb-YA396dS6W5ngtIKTnRIkcLP1mDIV6x6WytB_Vt5lcaq9oaWw7T2PPVXbyuCAnNxP4vHW35s5x9yk9C_TF0SUm06Dyi2XVpoWeVW56kxiMgd_-Owkud_FBcre8rtZ0Xv2Q0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30486">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC-sivyCsdULjK8eLnTwHqZjnJX50B3OLXiOlKotpijyG1-Y2M2YZCCUa6cAhnY8o1sfGTw25IvucP2jZlmVzmEY7LPoWm-sI1CLi8wkI37Xv_TgWMoe1UpI08hr5IGSQnMoCL5fXsYVAGcDQynHMSGJbxXoCPGyGGfLiPx0Piffqnbm07j3akNgXNnI90SQwAfbcgQaBOuAWJkaBvumvh40Eq5MCJPmQrhwTrmvgoJpWlzADa2GuzjDb3DqKML4Nnc7jf6p4S6keY1-tTSn3a4Rcb_U_ewZQ5BqyroQGJ0V0LBq7rLTL5bfp4u9T2qEr0KLbMUfRbOrsOgdC_yfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/30486" target="_blank">📅 17:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30485">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd7l1zZ6votKCueJAefnguZ3oP5MVV5K52ZWoyWm4yHkj8wb_8HP7FZz2fvmiluCsHqLB0jAKC8ZwYMxDESlHLONYzwHS_1V_CNVZv4K6YUQ0opCn3791UBWL_xJli0p1KfTUwnhbglEfKGSbTgDJriaRHUaS9nB0ctwK3WTCk09Os_TlDYy0XZ7CHgHlrMQkzdO6gLmkJllhWi7VGkQZq_oXbwxBr2JiLy-K-GSbima77InbPBAkXy_p6wWTU9mxVBMiJI8eBtkWDwYrAJ2NXUYjwnWVeStQxzic3HUYTULBXRI6mzgLt1lffBT90fG9cteA66S-1ni2tZ1EqsSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار باشگاه‌فنرباغچهه که امیدواره هرچی زود تر انتقال کریس رونالدو به فنرباغچه نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30485" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH3QUxY5RsWlc5HNS-Gvn1s_XggF5U_WUkR0MCL0K7BbqG-zqcT9DmEfoYsaNPhrfk9nPVj9fqvfFoB5BTsnoh5VbgcSbhf1Het1Zhis0YpaIQ9sru0Sh6SjkYKnc9RDtJd8FGHfeLS9HN32mpK9RSppIrrpgDUkLY4AxBEgaZOa4DE0KCnh_6Ub60aWUaHEAL8HxyVosD9xg6eWPrG1QpT8-6iw7x1Ku9779itKmajOzjXgQhRCic7tQGTE5Lx-xCJQRHwXlwNktb5bbVvKIRCNSGRPnC3RdJnCZWyY_w-UqLAd-ngWdNO8YeDD_VnOgeg2TnJfbNziV0Ak2jAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHuIG5Ink5lj_m7LGvj2Ms4zYkFiLsTBLBuTbVtvn_ZLbD8ilyXzPsKpb06TUYEX-fuXG4_6h_vGHUCvoQxiTNLmC7z90xmgHA15ckZl3gk13aIA3YeSSP3JL01tNyp2_hWF2e8Ej_7BBYYu1GEjFTuDVVpBnBtDt6ht4Zqh8WdWbmkacQp25Gi4bpDZcoP5BGfdKyopP2Ro3Gu7FhNYN7TVrP5369Ua9s0AEpLENgararLb2Xod6fc2_885yQN-L1maFRALps_jwkV7khyTOwMpyuPJfalRLnghID-Rnj_nqBwsSTO55jn2XzK0keyLPWXvH0aKQcpwzc4emf6UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh2ieWo2NgAdsyTzn2d5GRpv_uSUuAnbEJCf6msrTzg8RWi5dC1DVzHfOgJO6cNBJZ_IKiHUfthXXRaI6_Wl7BdOiPRAEpv1CseDejwm18qoiOssF92kFrd0oz_VjBiKZonSAYx7hlLdBP_Jhk_TYk25ByADTPT0eT7jF11QyJkqQxaI_Cmvth2suJ6WleqRVcY7OTfp64fa3Xk0LE9TXF8bnEiuhafZqYryZkWdNw9oI1tDzgAsRm9fKkJDyLXJ3Q0RW_hygSue-BL5mpW1nIcjjX5E12DgcW-Khod_D4pAUXNDQSYB8dqSm2mYDd5ZFe6e6KpJ6NRZptJbPzPTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpn6ZpjOdzXzD7-YpTTE1mNk3t1QOd0BKxSjdUMFPJLSctM8CjxKKKbitjAk5v1OrXAGx2I6kZGDrI4rXHLVxH1uZX1BXXPgLou9VBapD8vVc9f_VEND6tgwuMHeJuwL-yBwcclIQiQV_XN4BdWXOym5KCYcNStVp5_f2fYCZQgYBhpjL4gJd6hSGTX9J-3FMK5j0pB-0ZgIKDbQSQxQdJx_wrUKnHyPSYxtcTiZBBcsSsqsGdiypnQnNlp7j0nErsC2jRTAy8f2yyYoIqhPrD3XGUx2uGstIbce6qS56XfiR6bhlIl-ocVcmhZOpuDj8p1xau9KNiiOYTOu0Yfo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6y8HI07bKyh6812-ShlO5TJlFSDi4ffDf8yHYvHRIGgnLcTqmMGk8zyAdffYCkG8UbCn78KGM4BsDDP-ZI4W-JpvxBe8_Ch3ZoqknWLITFcXuRsfR9wTYEvnSQ9YKODwamHMc90wom-FwkkWDIuk53ukzGOAQdlhwOoXH2oz4ciBdA_fgfL_Au6R00CFv4rXWRSDf0ZrW2pW4Q11lFdLOgOOs3HjTSil3is4xjuud6fltzFnnKlMAvaq7oNFaPXxiVFd7U81q_3hKHOo90N3lNW1QXZujcEIhip5lOvPhY6SDXQMnkEwM-MkRi0mfwbSUw-UVLapafD9qhFdQ_gwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcFV7W5GGSHfJCNjmE6K_5AXcoJM1d5ZxbgnyEAx-AqlYtSZKEhckJDxggrO-mkMHSvMIbHcL8EEXZB80lnCSakQstXh3l2SGZFEQlC9csj0V3F7dX90ISyJpxKAl_KTrO_bqp9UsF36fH-vEiKB_13sldIdOKmopqNT01dmHj5hxmQ6TjVL2HWqV9DCxR5H3_ejpQiCC5M0RjTHXNFr_UUlB5tbN0CveAgAzoC8lT_4UwlX_OIovlmrnKfihsJXN1GFkplneSSzFU6d4G4mlceA-DAecwSC7oqZqd0fJoonMVPzcFAwEbU82SBM-vyQLO0hfAI6I-wAfo1pefk1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVPrd_jzvmTt3RTKhFIPfEWPE2zNM3zyMGqwhjOTQvt8-yAh7Ai4Ebt7ZJSf0F_j4yGL7awf-nbgTM8jk-7JrYeFYsnsouKIfJjS2Vs8yaOyMQSEKxjC_YEg0Fs0DOfS-X5mM0YphP3LdZj_WqrR71_X4pDu_7zblaqmbdqrDcTSELOreuoXbQtL1bYEx_K_8H9aXXXe7Tp6kPhhSQg1dIqZ9Uf-SsNE9dxvcpzQxjGkv0EqtBNW17mhC2BEJYE9VsmsTf04dMqZ6h9PZbOxcwKwfIbl7tLvIZODvr6QX_y7nSJN7X1XVssr8vnibtSTemYOu61SJ109MmwzZVmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USHWxtuDroylHAab6NSFB4VhXb1OsJCRfS9t6a6IbqulKh-Fg1FgsSyMnFw21S2ck9FF6DFVEskSURZHYq8A70xGHPr_NMBUYyCFZj34KSF3YV6cdVWLrEvM9sHJ17yKlZmevWzT1rWiCwyril7mRZQdWY8vrHtp-qBFnXz3gmpx8C-6txdhHusTFb5s_xNhb_z7EopZduN1RvBXVafFnl7Ow6nRqtWzRDs9TMeWBIhkklkvb_EwJsMO9mpDIx7aERDiRy2N_UZzVv1zBkNJF2HLLmc0lig5DUB3oZUHmU9aFy075HNBdNM1LEP6LTlsheUKGlkoR9tgxTGHHJX7uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30475">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📌
قیمت روز خودرو/جهش قیمت خودروهای مونتاژی در بازار امروز
💢
آخرین بروزرسانی قیمت خودروهای پرفروش پلاک ملی طبق استعلام از نمایشگاهداران و دفاتر فروش خودرو تهران،/ ۴ مهر ۱۴۰۵
⭕️
این رسانه هیچ نقشی در تعیین قیمتها ندارد، بلکه صرفا اعلام کننده قیمتهای کف بازار…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30475" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30474">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am0fX_DxTTim3BLMVjZbIDs49BPC8NuKtVUTO1zcJdQeZwRG-RLR2wSorSGhbs6LvDnq6vWWopZeb6qf0rriaRvS7RAYyoflgD3-o_5P9y0H-910-DBu-hFHFqYBlg6dZct8JfF476J4yDZIvxZEWOf7gNT_jCqlfvZyyR6xdBmzLeJeOKmyBnP1wCx2LzDXsBLQLSL9UdTLglRDRZ_Dpx45NphQAnmvisgEjryipBlpyzRV58E4fxpb6YKz9_IZ70MHKxlKeJhd1YJFZx29USrwMPD6GGwzZgysVRSL2pA-ATNyd2Pk6a82tj71DTZArMOrFmEnrmjyvZiEXxW8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30474" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30473">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIa9rh6lgi_pWyaG6Uyj4_QnDD_eI77fV7uX8ZOBAkeH59HBY1TaG26rvOj0BUEVzAbrs0sTdsXFSCPKEjLK3kF1_r0NTD6NYcLjffLBhxbi7_kOY2t0peD_iONnjmpdlahKPA6idDcu_T_j--E0XFKax76eWO9ao6mgFVztSCR3LnGmxDfW2rT6aIJz8TDqFiafMkjNa-QTFqHP7qF_RPfOIRp1IQtIPNCGSqCtYdwkRprrpHD3r0HRo0Ttzcay9DeuzN37VMJLFC8K57zZeX43RSAvHq9hOPdwVJMh1Dfu9BXc95sQ1cO6I3hBxbkwQWhhBsdV6qLmvH0zYaKvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🟡
#نقل‌انتقالات|فلورین‌‌ پلاتنبرگ: جیدون سانچو ستاره‌انگلیسی منچستریونایتد درآستانه عقد قرارداد و بازگشت‌دوباره به تیم دورتموند قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30473" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30472">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی آردا گولر ستاره ترکیه‌ای رئال مادرید از مصدومیت کیلیان امباپه در جریان بازی شب گذشته دو تیم ملی ترکیه - فرانسه در لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30472" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30471">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3tDiZ7DZfL-anynF8tZhoQdDnVfoJTZ1nM5SSf5HrDlb4fproAf_eGH3qv918u2KP4jvb-89TJEkq9Xha7odFqNMtXkkUinLVBKlUa8ZWIO4aXP5E0EbmmnvWlZ9MO76QerQ6ud6jjs_veF36GVHuWr6Crh-FMGSi_PqZzDFRe9hz4Yc3n-wIzj__ZzCe9hEyXO9i1Kfx2pT-UA-wLj1k7qKM1F_RPXror26GA3EIoc97wMOm6I8ir2_LkO1hp4MiWP-JcNlXtGNJ9lxfwQ3H1mMJQ2uRwDAbxhqliMDY_Q3aI2ZIKTSHnpczrW_fTSJrg5vVMd18ZcnX2tiIlkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30471" target="_blank">📅 12:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30470">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWI77XTPzH9cMwdPZR5wNUyIK1lWal3oK3QYs5c7zMRlEWYA41XvwyKsyPCqXEdU4fOYgD4HNG3GwAUJs-WeeY_atx2OmqGzz2tkgr2cWeX-z-YxI5LhDqeOebOrSlY8_LQY8I82Oltyf2nSPdu6jhZb0I-_hhKF-TuT08ruPWmke3TNUtReE54wwYUyF0rd_hRaCfaSE6zp1qbG9ewgnrlNbn1stUGLhgqf5770ePM12PMb0NkHMMt-2nb8Xdo1Dc60wzyhWgoPWg_eGccmYYoK5CIp9IgJIcahdxmOClWHO_GlECa8PV-gh8v6tFY9aNzKRCXBCH5mODAEAba26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30470" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30469">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWbo9fcojbNGxB0XZ_ub-OAhJoRRO_FfzhGVu8ott5-ByX0vOUUPMvCr94iXH4KlieWNp-izmRG0mEuXOW6VVJMNLumwBbzYGZf7Vs9ZAWhbwCSX8JwoWz-Omsadg1bRqMlCHhymiVo85teK9GCUk24_Gvo2TKLFqJI0vrTe0Lai3FHE7eZyqQ99KeDpC87sKBG3NKYG_-zvMsLqchdfS42JAEAYaQc4Aknbf46tKirrDXEex42uPwBXhS9vuYuTNAkMVGREqTmECVr_lxbrJC9Tn0qdTvF1anypn8L4-Pxw00fuX1JaCdzxVWx3NTyrimUlZ8fJbP3KDNzNgvBuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/30469" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30468">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
تعداد از کاشته‌ های استثنایی کریس رونالدو فوق‌ستاره‌پرتغالی در دوران‌حضور درمنچستر و رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30468" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoQIDkzcTAB5A3Ezn4z_od1C92uvyQhvk2gqFUgH_NACKu8-A89KXj0ImZT1xv0dDtkuzurl8Y5NaFB-sRse1yxUR2Z0-ELdz7xyiiz7cMl38cFFuzNv6mzwm9Y7LHCkovpOtY-hinrCgxF-Sm7anjfLOSyapbGkuNVnTEJuIsARHJlO7-j8C2empbpRBQeKC4KM3c87n5Lrj9IjKePTH34hzwE9zDCjLZ57kcZmcqYzuRyjQ7iNtEEwvyu-3AFL_m61-2ucv4mvUieGzJ5yreLQdRIxCktE63hyVeZaQR0K6EaC2XEeYxhEj3Fhl8p9T2w3FX1ejCezMM2csDcM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0TplsJ27ZIn23ScXfZ9FirUCYIUBRJgzftVAViqKRGYG6Frt5bUJDRSh2Z0YPWfBpMzq9KdFpLkZvh3AR54JHMJXJu3xVv7bII3ilefxGu2zYItGi8K-2x4uehZ_NCVJmVaunhjUywEmUh-OE4iBDIfxS01ZHSEYdtKKyrmNOpA6LP4y0pqRmxEqFDx-agKQ7L8BXQs4CGbTjcX-vx5NvF8Utkl5Na3wvE7AHeVBuwjc7vjJh1I6--V2efPCsSxDrU08C4Hkhh-qJAmEWUbzPUcgQIc3FoMo1G-fs6FH1dZiaJBEAshyozgsSGYrE_4mcnUWsICLZ9eb1-ImnN1NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=XLJfWScQCw5B4zfvWKfZJWR5k6jSdhNehY8uFmfxoz733Ix4PAGhpws9TzMER2Si_A1-0ND3z1ghdI8zjiJrI8GuXCKKYPVqpoemjsJkIF9BZuw03Iv2zVVCIi_k3Aa1VNa80TSSdNglUFxjgNK4HqoGDQMhU42HB763DgZmyhQnKXaitfSVCOOeCb54ZXQV7SH5Ix4_JYSJDXUeVyAQwX6wH3hkCg1WMQgG50U0VOhbLdEO5SmoAvdEOfCkCqWPkuP2933SUH6bWpi4bV-4ilxZ3LV7Gmpfg9pHuY5GgzNYRfxBfXPIZ4VaWAfmmbLY29_m06B51iz408omL8fqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=XLJfWScQCw5B4zfvWKfZJWR5k6jSdhNehY8uFmfxoz733Ix4PAGhpws9TzMER2Si_A1-0ND3z1ghdI8zjiJrI8GuXCKKYPVqpoemjsJkIF9BZuw03Iv2zVVCIi_k3Aa1VNa80TSSdNglUFxjgNK4HqoGDQMhU42HB763DgZmyhQnKXaitfSVCOOeCb54ZXQV7SH5Ix4_JYSJDXUeVyAQwX6wH3hkCg1WMQgG50U0VOhbLdEO5SmoAvdEOfCkCqWPkuP2933SUH6bWpi4bV-4ilxZ3LV7Gmpfg9pHuY5GgzNYRfxBfXPIZ4VaWAfmmbLY29_m06B51iz408omL8fqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT2vXESX6hIBByGJNd95TeErOTTcmiNKU3E0AuzuL4zjj6tQuV28jIpsroM8FY3OA4cSAKTIl3QX-jnLzKEt3IiFbIYY_6jH9hrakpfzPXIisee7YMufIiZ2AYO1Qo5DkGZBaNvJqj8KGQjzO6mvGmlGDdL5RawOoR5hJN_a_ou-e8uJTmSiqg3m5xIu3QOvxqM2eNYqxjdd7hlvNFT-_SDOC7JXl_3lfPr4fj5TamHeto02KT5tfG0YVlrp2gfkuQVS1OHFMfI7XB7Z9cAEw63T4k-vIX23eg2hvAPsol4sg3SFV0O6zswvH96c0aaUpiUWm17mNPlYkuSLy6Gxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLxhnGwp036NgmvRXDacvaZGdgIt73PCaRmFA_VNge7yXRrmR6TmYzHo1jk5Qcrl0g0iVF8jDu0inv9UwiCdScd8YVO_-0MQFwhwcYtJ0eGvSBw-phK4Cye3Zczm-tSsR-GarWDdOoaJWzFOuvJWvXIO8pQ6-kXY-aAHsongQecHXZLbLfmy1BngKoJH8iYBfFGgV4lzmHsoCXQPb8dg7JCI7eUl8PTOrKKt9Me16hXsn78LdFj9WG2Dh43fLDDYEYXEhRRhOA5rE5kxmDpqSw_q9S2C3JkXBMQdb_JbBp1oL4N4n5B9TGu79vAHWhi0qAmQVUz7N6p1PjD1XoHOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30456" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPepFWcOaVkU6spaqFmB159X3LtsYyVmUgHPFGpzWVQ9hguiFlMvGqJRvHIuU8lRF667bmTWuD3jIdXdTfs8dusW4AdhahkwZ7rWAKs1PSGUXy9QdHf0c54gIFcdUJbLzqYAz9IlMJv29HK6W2oIDgLtQEYdaiYbL1Q2IWS5pwLQRV48_Zf9QL2BeSHTJ2RYWCmHdsi37b5siEwX_hBZ3naC6gvgTmXLKHaMVgeQbCadXwmyQOdGHtrnyXMUS5etNCSNvB_dbTHMzNiK2oGw_hcbiKDInfqi-JTWdiroFQxUkgardcoyccOdn6YhRZDhiM1v-rSPdPOchUhgL_FGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یو ووچر پرمیوم ووچر_ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30455" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=lymRA_YQKC8WaRZR9j5fTNxtnWaM6qAV3S2ddM7yLuwokUOvh-e3fQpyrioW2h5Drt9ZmiDtgRR01jNMoXWSlQy9Qp-VXak-6Nw7Qhj0skPdvR_CNl30z6WEVRRliXo_vpd0lqDwa6nM6Ecs7qNR8XhDcZYH9WSIUz8r5M2NgMcWhPV2FAAN5tiJ2qR-KkViJS6HnTugSZIPOrKkaVXo2yOQIkTYHcmjNz5zHCIeUVvkheUow45Lb3CAzlPCEI36aDScgUK1UxZ_bJSsO-RqNTd4_lfiPURrjgVytnaMJ5_2OWwJtZmS6xZ5u836sPNgfYf0cODlEY9fSS6tCW3AqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZWSES_WUkL0iFK9Ynjn8MMaamHnmRvTDGOY8M1psFbIvLhrzlD0vFJnC3nSSrve1A2Wr44B8rNW3fsuEFTjBjSDU6XZO0ZU05mAl5lp5AFijITQl-5_IpoMlpd5QbKy0biPBCJ36u3irjwTEBt1Y5RThFUnPVBkxiKXzAz6IcjGjluZLb7Qto4ovNWTyYBa1Y40cDrqUhvlTkgEg1cmqBEPuqPrlhbPuPpfqGKnmCw-sfb5F747fu23PUEW1YT3KOcJXBSHKe-7g4A7IOP-1LVZMcoVBSk4HM6vKqvj-BXHbZzJiCrYcSjugP8x5XJdRHR6IpYLvg4W8oZTj-tR1Gbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZWSES_WUkL0iFK9Ynjn8MMaamHnmRvTDGOY8M1psFbIvLhrzlD0vFJnC3nSSrve1A2Wr44B8rNW3fsuEFTjBjSDU6XZO0ZU05mAl5lp5AFijITQl-5_IpoMlpd5QbKy0biPBCJ36u3irjwTEBt1Y5RThFUnPVBkxiKXzAz6IcjGjluZLb7Qto4ovNWTyYBa1Y40cDrqUhvlTkgEg1cmqBEPuqPrlhbPuPpfqGKnmCw-sfb5F747fu23PUEW1YT3KOcJXBSHKe-7g4A7IOP-1LVZMcoVBSk4HM6vKqvj-BXHbZzJiCrYcSjugP8x5XJdRHR6IpYLvg4W8oZTj-tR1Gbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWfY4K3GvHNVY9HdAORJ-AOHf12lzLVJGSeqfjUn29R8YJjdjafgwOozofsEOTlmarmAsyTZ26s0tXdwwALkRfqum2Smst_SFs902wf0Rk1NBOWbGWlmsk7VFs4tT3qdjyiDWGxrr6cHP-5DqVLcsKxEfUi5nrI4X8IatNjTy1Uf1tpRCsQWG41tRA4HPzda1JM_ReSQjwVU_lZGY4OSUleuzsPdOwIBogisGY5rLgq_rSGRuf3-av0fMSTQRw9O-tAVEXd73rzCM5Wds_eA1bkSxMRZ4PzHGxy0xsCb5r7Jd_Zgdywbdb5YJGF3sDTKrh5PA4vtWRpEGENoWwuKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30452" target="_blank">📅 09:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th76l21XZsYjIqECtQQtOxKs9gOBEvPk3D3YrA3i3kAiMTxY6zVs5se2LGa6kT0OfI38O5TIwHWt7Dtw-V6CY4_HqLbFgsbIQUGN0XWFVKdqx-I5gCPwZIxeo4Q_OJrXohKt3ES9OftCU8qIJ_pQgKtJdvnTCigiIz1w43w9ciL_9QQ76ksBD8EAERRXIWBYxKxvIg5wXqiLcxmPcLXisO8-9si9gn7dFqjq0eONiupxVrSZDYvjRNWRg5orvYBAjm4BFx8UQovRgt_aDv3zFwiokRyjxk0DEh1e1F67FC7qNhVv0U1kBu42t7XJrvTyC6a6YwP3unrj7a7i_U4D9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
رسانه‌ های بارسایی در حال مانور دادن خبر انتقال ارلینگ‌هالند به‌بارسا درتابستون سال بعد هستن و قصد دارند بافشار به‌مدیریت این انتقال در تابستون 2027 نهایی شود. از نگاه اونا پرونده انتقال آلوارز به بارسا تموم شده و این انتقال هرگز رخ نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30451" target="_blank">📅 09:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W04LDYGbaNrdC1C0Ozay2sbMUDQEQ_llchIrfhN-BdvWy9z5eyHrIQCsAemST-fBJhoNLFDq3GcQoG3IdGp4Qwg8G5CvYxjE3VWCqf4bYJn7kwFqsGttbqSHYinp3Q0EfX70byhit1IfEiq8Z6gSrVSZE2ZmhM-eHgNe_BriP2hCR_8dYKYd5bz626AJmEHXZ9Mdv2yYyE30sMSy7txoKUf-KoqdRKNldD7AF13oQltou603StpEDO7aDsEDPpTiedd4NNLj1vn8EI0hsEr8ayTLrCnoQzmY9EffoAKAKLa-doHLqQ5eglFjllP2ld5pya-Ke7EEvca03uSKRvorRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=p53ytFCq85T4aJ0aeAdwWPaDhiyIhicyqdA-V5NKS2VCWfEUZ0FsHwImjsfnGcNBLCsc-8jwrKLhcLqoDSybbyKWR5utfYEoIuxj78QtCn7F7ah_0lEbUs4NPDocuwxrqcypS9dx-VKwGcVV6KnZiSjniGOPjM8JuNkP_Xh1rx5Aj6IjOP1scz1I-OuZbvJdC6vVrhsMKjMAPgYhr2JPdLtxasDlka-4r8SDP8MLGrJQ1v6rJXRy_pq7DJSnKqyUoMUvx39LKIZoWzRe9zc-8W3k4aNVGNXxZEmRDscXKVyF0MxL9Pp6cTeyivbEdJVXgvAlcHbe__Dl8oszE6X3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=p53ytFCq85T4aJ0aeAdwWPaDhiyIhicyqdA-V5NKS2VCWfEUZ0FsHwImjsfnGcNBLCsc-8jwrKLhcLqoDSybbyKWR5utfYEoIuxj78QtCn7F7ah_0lEbUs4NPDocuwxrqcypS9dx-VKwGcVV6KnZiSjniGOPjM8JuNkP_Xh1rx5Aj6IjOP1scz1I-OuZbvJdC6vVrhsMKjMAPgYhr2JPdLtxasDlka-4r8SDP8MLGrJQ1v6rJXRy_pq7DJSnKqyUoMUvx39LKIZoWzRe9zc-8W3k4aNVGNXxZEmRDscXKVyF0MxL9Pp6cTeyivbEdJVXgvAlcHbe__Dl8oszE6X3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv3kX-mRPiB5Z73rPfgu0DgWIEAufVcVHzbNo6rMyAD8w8mM2u51G2curwJJ-BF2lw1wDzv6RZnVNC7TXuqDc5UL0qYpXdVB4jg7Qwi41qw2BIE3ghS6BVGdDg8SObxljbi7XKyaywSQ7VtcsHVz4zjmAgutrryQBpcVwneThcxHt0244q_Yi2-DW_NDpBqsOTnvAdZ3F0ydBQNgrzjtFv8yvmqZRItX139TWlt7TvMvT8waGSmax-4A4TH1twu6Ao_oFHLgl44qS4ivknv5ZerAcU5wJbfaTRiBb76tJlF4lZEaRquJIYE0f0QUU06JQjxOsVKNEGSIPeQbznzPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0H56iuMtR3gyfp111CtVZMmA26OpVZO6jFginTl1kfMPN94dS4g6TmMkO8Bq56esVe2hEN7updjJc8SawDqekypJ52TTCGAH8iYjFQY_Nb_y6FDhtwvq3yatCOBhZxe4ftJIp71YE58ZlrRnrpu94DJNcbe2phFCx3fUnDxVXPpIht1PKe_O9pNPbVUFSsanxID030QvjHyHyfSJurF663hYDgFMRWwD0wzN4MPoVhyToqJe9-rnsCxIIvg8wp1H9Q5hl9sLw_ph2UTqw2aJS6nzTdEK23f6jKY6j_0wSWOWtYkHthJ-CST4oW9p4D0MOoZBxI8mdDiKKo20ebh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAcZNPd50o9qvfJpdL_XaNfuGvXwTLqwf9d7rve9QqdUoNET0RFY0FmT48i1TZ2XXjZelBAo0Kha_S3BLcFuEkIHEh4qZU5ADA-vB8LJTRptpUcfjM5tCMrsDhe8jwHDrpMkARRA4Gmzl8lMa3Le0FcY7pjTy9jX-XQZyyb2Wz3_5291md59feGEs1EswmKXGHjQh0ITxQtBh4bxVwodLObQ-Xi5hSYiGmT2YcWJD9994kcJC-8qoCQ7JF-kaqfCcoCL56GxchqIJ4zHSP1jOhAQIruDljlgrpn382CUoboAGWwT5roCin5Q4_M7MkxDlHaAG3-HQyfh_Z1QETToeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOIXUPB7UJ1KRtjCWaJ-Rm4XqIOnudTLm1giMFnIec5TlLu_5V5l7ZLQ0_puclg0wn50IyS8r9gbau5phNVqxhSmHndaGtgOHMcyLllzfiBun2Nz4y-6q-93CEBquHrYUZgCbZyDbZaqs_j2kwL4KIxqyj4Z7E2fbaLg4jIVzKyZ9b4foUuKAZGV12HT56e0FziamKc220a1Jn_S2fke-rR3nH7iflwtGnmRQY64FcqFuryYOLbE8whl5nY_C_7nh2MreUYrwh1HIaycbPq7sz4vnauSRVmWjg8HFQM8zC7ZRaUO3o5dYRoQXS0GNWJo1BAMwAcMMKTbFBStgRa1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx49y0Hj4_yc1BSn4KnWliVI5qrdmHwO67VyDXhiXkTbXb4PTA1PMMBaQeSMJ0fI8jsvCEH3WXnwGQpwoI39lnqzhK-wd9MxGxHvz4rxc1XZq7jZqsVDiyp-JHRWWgtjFDm8uCtrxrRbvbFSJf05mRvpjkfbn91K46SpAcsGjrwna4EUMPrFGcbVVDF1RBczaSHLAPGyyUDRZTWy8xoVGUZyshMa1027q3eLIr8FVN8Wt7IRLkYChKkqBGNC0ZCIeCCfR_ScMLWgJb6eJ6aFGG7VzwI5eD6tpKT3ZVBGC2cpMoycqdcG0jnHGJhWQbw_NvTsgZqHrnOnuVo3jnaZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL0p0j7RX-WJSqmzzhky2bOZc4XHPfLqm7FdIELFOYOL8pCF0pQ32qrGqoNqWi6i2CutcNyoGf_nEi2iVGyqPA37uXTh5cKnu9C8MGRz3SPB9p3Mu4rbDGVm5QDjD91gXPOXEs0FVq2erPoskusbXPg0f73ZxHNzW9C6bAIOViKQyUuFTyXlFquwJCR_N5IiZN_C3SGL3fgtyLeJ-dIOb_n_ZEfG-t1wvlhuFIQh2CR65FhE_ETjuEPJDaHiUsxjWY55zqkFZyysVWIFQvK8XCvo8ujgs2kCOtpPMcduTOzmQd6-nYNvv24RE-Hpe-I2-45op6OIDaviowFaCa_ZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0-dEZU1RYH4-870Kf278i3JTzw295WgUU0iYVt4sqf_-J75jm5MiABWEAKwvUzU6NfiaiLqBIs7WetlVFEevjSFKCgrOvO6a4Sg6z32k-yA24_pfK4fUGu0Z531qtRdmCkgujbp8ar7cbwY5CPnRIkIWnfMOMnIoMNspOV06z5AkAtRYY78sAQo0uRoI7Rr2QNm_9aYAMGyj68vY9WBVDH_SLllDfDtuEZw3Li4Y48C5AiXJbiSgcYTQscwwtWa9DxEVrVsD78_z714QEENMtPLZG-oEez5EMwfizreMpsJUKAb2c64gbYPQhAOiuk_OOIPmyWVghlEDLKiH-AGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWQWuscvYEtYt2ABhSL8xfB4FsQ4Da3UrN3cZ_7NfXWjJ-UO-oWMYT-FE-XWOuUoqmkTq5PS9OnRMUs67AtnHhN2aIyEZaT6ABSlrP-MNPldwe4E6X2X1-HB-H2DzP_JnSlGjOYxo9ctLMFIxScinkto2JN_ByGHxbdZkia4C1HhWE7FG3BOw0wVYzJuZYKTsu1O3wr5PmW_eu5jcqezyzN9XM1d72GTwQb_E2_jWQoWEDYQsZzaO8QAASHSh-YeEKy4T2xjgI1f0s-rfVME682kMcqjj5qBzCyZ5LVTpg2vVKSoIOPz-jd2PsEUygzth_Vf9UfsdOZ7AYLwWHyOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY4mfJSxU-WknEnJVxPf80_BcMVWz4mxW5HXUzQXYzvibavVyMUkQwkbggsT2QtLfFkQW__-kWK-OkANnjyCmj8NRO3OvI1zYYaF2PtiBPZ4L8S5HAnwijcle60yT1bQxI7j2J8Nnljut3dxjl9MHmFX1U41PyQlyvMvb_xBD3HDhFAP0VxtnbXSXslVaXop94Qy4lso-rHz-QNGARO9dbshitIr29QA7qNdJj3_N0mq2m_2NRjToO4aywVsM2YiSWBNryqYYYRFuk7YMRdVXUE9VtM1ylG1QIpfebBokSjPGvYlu7a_irgfRpMzFFaw_GTkxowlgDVL0jzQ7tR2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr3AEXl7HHZhvu1rjkdPS4cdt7d7-WdyJ69-qkNYoBmctW_e1CJyy_alL8RgiUnbQ81CWhibIQ7pJhKefu9eb2SEBmj7nqSBH_klcN5oDLBEzs1Ti-pv05G2YRNCxkidLAEylFx1ccm7qNaOtr2fRSwUIlq7yIH8YYvRTs_hQQO2UF_gFO744OhOcXkoqAXSpt74DWQeR0AwsaWPUJ2z4m3xVCMZSBHfOWeCLvgcdXOIf9mNi_AaA1MEx6v3AstFiBkAhLuDP8KmGmZgI33TlZkYE8cfqn2L-j_j8mo9KXKCtUbEsQd6mMI6tp059Nqt3Z4LpxFTkgimSryR9TyuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfGFaJIw8Z8BYaMjfS_9boOg5rsQsx5rva7J-4_glF-PE3NLnC_sbR9w2b1j3jtXuSeejpM_Xc89FbkB5zfusAnvi9EHUpssciPWP1RAS7O5V61gYxqyBl01ZUJBYYWIvEXq7-YMFwdhi9lqRlNezU2B28duDqqp0JbUXnPPkLYGVfCxFNdxvE5L7MOli6xeRqUHHvU_y_A0JPJ_dLtJ5mh_1GG87jRDI00VeBC10s_0Nd-AWgb_P83X9UERvx3OUdlqswq9c8dwUtVgPfH-Q-ipFUAHxhya5jIdBYCAJ6mmpENRreQ5R5XAKmaTNjjk8xeBq6_B4bUQtfaqr1jY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny3tgB60FIwlvMX5wyC5JkY3OO4Qlf3kAlAKUpabu3nNhqUQU0bpr2yPofAsqDcQqxTdWqvXCk8PhyRUOm5_RnIEGt9MmEXDZ4zjqh0hqRBWCdK3SdmaWtc1-XF9_duhGtdwUPi9GcozLzP9WaeVSE7KFpOya5G9PDDA5_oUCr2clV4s0zQhDb9tvFwvohw_z_h7JjjcVuvt_r0Qj1XD96vxC5oGPhgnleFNiXOQrx0vBa78uLIXgifZBHuEtaKWvkiVa1o0O4pFeSCI9y68MsCNp0sXS37ZPjO8mypeVQlRvoFPprRRJp1zEQdQirkkwYvVK-zY13bbKtzf_Q0lZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=u0YfQIzGmda7JFtSqShUMGuzSk2WxBAw5qPpa747320WgwPef4LoJoH3fpPc6-CAJon0owWM35ImrwThQZtbgHVbyGQ6vTbmsqE-FlacS6x5M_nD9WgE-tHOum-FgdizZFRcCI5Qe2r4vbQrLuIPTG5XivFmlNErqcK5IJGH-_R8W5xP_6uU-ZZvJBo_2SiizgtFClp8GAQOkrOdOZ3l0wMO2qrdru7cf8N6V_-ga1Rt4DIb3RGoC_EqEEpCDSXXRlU8_QNScP_194bvBn2cHQ34K1S98KgJUG0Yat-TXoG3vLDizKC2rFlOoXRBpzgs4AvU1tsqCXFvpWuLYdqZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=u0YfQIzGmda7JFtSqShUMGuzSk2WxBAw5qPpa747320WgwPef4LoJoH3fpPc6-CAJon0owWM35ImrwThQZtbgHVbyGQ6vTbmsqE-FlacS6x5M_nD9WgE-tHOum-FgdizZFRcCI5Qe2r4vbQrLuIPTG5XivFmlNErqcK5IJGH-_R8W5xP_6uU-ZZvJBo_2SiizgtFClp8GAQOkrOdOZ3l0wMO2qrdru7cf8N6V_-ga1Rt4DIb3RGoC_EqEEpCDSXXRlU8_QNScP_194bvBn2cHQ34K1S98KgJUG0Yat-TXoG3vLDizKC2rFlOoXRBpzgs4AvU1tsqCXFvpWuLYdqZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGvBcyoSZA7V3pwLW-g6Ya5XSrBdTZMkvO28Z8hLLCxE14hzWWj0nw9tlSk4l8hJY509JoF5QILbonh72ZyvKxa8jXlIlUSV1RynqB3Zm5-3Lr5d_RtTSKtqepohjkFtolpq4RcTl5y2jGZLibrTIt_q_FtMvG6N1uRWmskAujj3BsgKARaWZTlGyKWkJusU0JFTSWIhYLD4hOBWN-xGRyP1LOTk9fdz490vVA13h3B6LM15Gk7s2Wb4eik6V5LdQui8ytPMws-TeLfiTg4ukGXMaKIvMBKmU1C8zfMoepbf2_fUaicWKcfNuFOh9jGNPc8AL-tsauvn5y1XA6r6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KygFtUltFs1r4jMTX4aWThbiYByyddQXcqUmkesTnjsgG8YJ14hjSuDxLCHb9geZGQBd3kWWwdzDEJmLm4AVb9gpyQUCZxl91mphQzSvn6c6qeEnrdTNiMTrqmgPHCiLw44mp2jneMN2yGVTU0IAzZ-B0j9-93c_QqCICkTpsy4_8yIrfvhLr0BjHOHfTlkrwaKzyDEHJZzxCqcEEl_AemWzPy6rB3Q1CMdHqPJvnwsotIwcDZEXM_yYrzc-Mfz0BQsXa_GrrYKU-KdCA75N2F_w3Qj7AW-KbY7zD8aXYIXocmiWyebs4XrB7mvT2t4TjJXr8GOtAKnkGWlR_Xpa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=kRnWSEKpi3vhYnZpzQo_tSzM5zMgdQAig2JNnu8WRnlGnQnnDENutYlhAQSN6zVmDJyuzeNrUKb43aNi-Jht17COWXxdc079Ah6OChRLXR3IKJxcpuZ-oWgj9fuu1xkrAoaTiYmH_EEkqEQ7_UYWwmp7RPSYqA--_edVoyL5zyOMXBI45Jclq9U7hm-Qvt15LYmwMLBiUKUxmfbr2R-DvMAzQj6cXE1SGUFlD8B758qJyPMNJupUsHIxT4Y5lDI2f6bCO4lPvhActB86ptk3q19HdMM8_hJtUGuTl5hW1y-_do7ZuI4HvX9iUGX0Dm84Z0S4rXONJXsgVmP_oFR1aWrEILJpV-QLpDIsuhFwnnLk7PbFJBgJN1UywKgX-vKKnN6bD1iqiQTcRvQ0nZoonHe4eZjbe_gI9Zt_0O1pSWFOoRWAb5Y1brQ6EAnuDJqlDQ5HIdFzJ7mIavSomerBc2l_g0gdU3GP_ql3RHtwE1RJCqL8DVUZ1EKl6HUQ0D6vxRBG0e17oQM-2oecvVSmIdjBEs-NLtQ2Z35X9pyzfqN_eeGCRbx_52Qh16w0tK5Mj9_hh8lMtr4Z6SGRMLDoUWrsd5OhjqWR2bkZf9wbSdUpRYLpCAdVktYr74YQYj1zXSUtvjAJ4ihZXch9msSUYBqK_h53CiN1gFdZ5KcC-z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=kRnWSEKpi3vhYnZpzQo_tSzM5zMgdQAig2JNnu8WRnlGnQnnDENutYlhAQSN6zVmDJyuzeNrUKb43aNi-Jht17COWXxdc079Ah6OChRLXR3IKJxcpuZ-oWgj9fuu1xkrAoaTiYmH_EEkqEQ7_UYWwmp7RPSYqA--_edVoyL5zyOMXBI45Jclq9U7hm-Qvt15LYmwMLBiUKUxmfbr2R-DvMAzQj6cXE1SGUFlD8B758qJyPMNJupUsHIxT4Y5lDI2f6bCO4lPvhActB86ptk3q19HdMM8_hJtUGuTl5hW1y-_do7ZuI4HvX9iUGX0Dm84Z0S4rXONJXsgVmP_oFR1aWrEILJpV-QLpDIsuhFwnnLk7PbFJBgJN1UywKgX-vKKnN6bD1iqiQTcRvQ0nZoonHe4eZjbe_gI9Zt_0O1pSWFOoRWAb5Y1brQ6EAnuDJqlDQ5HIdFzJ7mIavSomerBc2l_g0gdU3GP_ql3RHtwE1RJCqL8DVUZ1EKl6HUQ0D6vxRBG0e17oQM-2oecvVSmIdjBEs-NLtQ2Z35X9pyzfqN_eeGCRbx_52Qh16w0tK5Mj9_hh8lMtr4Z6SGRMLDoUWrsd5OhjqWR2bkZf9wbSdUpRYLpCAdVktYr74YQYj1zXSUtvjAJ4ihZXch9msSUYBqK_h53CiN1gFdZ5KcC-z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJL8kfQFXWyK5NmlXj-lf5a4RJ7dVCEaJJCYYcIr9JZO9zBwpILg1m_w1LTW6BPQxKLCiO2mMXhhFAqi2CCtJv_ClWBp81d6Z7CZS2nzk6PZM5IsDgryEgV91LXevknIBvLCBlxKyxxjEAF198YWmP2kLeXK2BtLVXXr1ot9tg-ecgB8Lynlo3bXFRSSBBQ88o2qfXo_yyEpxIZZwngPf17WZ_oxmDvBLe_IfoQmvo3zNe-xKt_sEJjVtaIqfmMCAH5XG6HUAQvu7LzFfke4ZEFvsHD6CndJYpbbrDW8cYuzYI37y9uhbpuzPzT4G-yB9IjxCg84_YjEfnnBTbkRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkppN8UzKPzK7VC93UL1_im-4BOXQVMlOc1hCNlyd-XhcgjXNpSEmkeh6B0u5oMWhgDfcQjTbYi1T57yBT7rctjHJpUwepbGet60RVeysYup4xtUrzMHhxseO3qjA-_lwsgFLQBopRGgnNEGVOZVGv2oE0ddME-pbdzU16Uboe65O6gp7W-dWPtGM3DzHfWqidHEgJ_uJ5NEqXvB1_IQZoPuYqCVUusP6Sx1nPMWTVeeGAdyIfCt4d39tzCAYyPuiylMLZl82oaOyWDIhk-Zj4CE6LaO93ml1T2N665EiZCOQjg7l3QTOUw3_bLC0B-eS4hs1jv8S5t-mx2ZNzYkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdFOUiN9fwDbPzI_6kqhWFEb57IQNoknTZFGWHnbBB16e8xlKpMB-iN7JiJrc5ss7IBrpYkr9Ry9WbJuL_opLBEog5yszlTkd6MsJ36V97Ag46u47YZfpqr_R1oGq10yKxrjFBapRH4y8HNghpl8vbSdACmBaYwA-dWaXLSrhBq8-_TUx00p0zZdmf5NUBkX5ZB4RfJFk7qs2kNDiWCIuvsBRQ9NOIfOyvUuNGK0UmnPiwmQfCZQhAWvevXEBGGjsPGTg7jJ1fzmetZfNShEh8wqZpis2svWNBLlOUs78vKjPCS0qkis_Pg2naAyDF1SWhuoC44hnbF230-HN-OrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYTLCCg78UTEXmuPy37LjKJlBM7rQOYIDbw4nu773vdBHGm_81pRNMsTWwlbHGxwk67XI3ydTroYFimLP-MWEQ8iiW9HCOYUTYIqx1lYdM5B0WcHy2vK8xxob97_I0CL3JfvpFKjIISfUBEm-rdmaurmTyBGfl_VL6k9zNTnxwUVNfo2nVy17mSLSw0q5In9rBqMfc9h8jggfm1lRMwbke_sw_iLTD_xmzUgi7ONXHsS-SHpft3IJrK0AWz04dMw56vn_fiFBstTfeER9M26QvhH--Ln7hXWsfhYeCyHR4Ggx_nG0HFf3_BMgPu3-GwPdEO7NCyuiE7nCgohTvRUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqcAq3BdRnPqef_zeoNAZRCP6_6lnbLE1CtK2JhNW7cq7M5cqE-8NQLIijF67oY04ABPY3nbeL9i2hVpnsN3usvbp_4yb-OsbV1aRoAoM6_8BpmTY96sABxEDASmS1Trb0wo7p4mWyDtqT78nxieNQ3FyYqa4R3fG1aRD73NPaq4v8fmIlfRB0vN5zmuh9sIx7lTw8iwVKkylqbRInmywmjD3Uiv1l-IvdU3PwuUjxT4M8oF1TngaBYxmuLxM49r-9i4zhpC7MHfeRRh95aKqMLoSt5EdyDnJGFewYxmxEV5tl0U-mdt7GjBOVYYg2NgJ2E37fbKZkC3AjB8Ig_4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCD14RvSEU1efxeIJmo6pCm4EAOsbZr-fdpBfyms_gOFMJCKP9bDQA5AxnF74Vr4Apk4RIGWKio-UGJCjW_7x1YrQ4sH1Y85oPZlSawnDYNwYqze7B5uW-lXNKkHzRsY2oCiYeFNajwPkhqNXgRKmhWfZQEt_OaGDMfbRdWtUHN_jw41Ty8hPvlQNnUVeRSmeWcwTP6ZxQVOkiXle4p2kpKtfOw3_wdl6rW6W_VLE6pEaDV4-zUiyBoNKPVOetRwdAlv2mJh1NqQszFyhtvT2M5vkQBDo70BLddutmIWfPmN8Xv2qZGBknYLyoC9nWDLXqkG53bOn4Yv5tFID49_2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6fHVy_7wUrYJLuJkB84zT3UUaJFZdf7ZpL94gkxphvkszaYeYAKBGSYBI13sI824DZDj2U-mqRT0EdYt6YDb6tY13JM14AECVaJtqN1ObENW_Q4dacc9COBSYoGYU85lAZTjePgCqwWl3HyqQ6W8sDXJt0Po38q1swBlwKmEWAAnCnA9NzCSPOFnUHenVsAjdLXKq8X4li1USmlMzGU5xEbdssUPrnMalRnqFq2OqNpo23IoppxTA1izdeytOkgbJTGgez2pO_Id3TyTyougmJZQfrIYmfyN9OppFV7KkylNn5qUGj-kFXyLsXtRFrgZu1DnscM1kgWItjtAQg_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhdixtxNH9u6onqaYpFBpxgqyotel0KyaO0XxbDPbrzbPnLKdo6FTUjaFR2bfWXv7AV2UA1lmSdN-nTd1QI2jHted9gmbGZKswiAhsUKgOKJhwJ580-DpsNMEJ_OJ6X160SbrqJ1YzMF35g9S7muiAsVG0x0qu4v9WRKcRHUXehU9Bgv7uDvllU_DikC3DjoI7IJtOkLxyt_q47ZPh9zgpFMUMqdQnCLliKy2lFZ0KRhUKU1VZR_OPY057psU-QZcObeN-HzxgIK6CYrpOphf3qX91N5D54Rk5ZcuOy7m46nIfW27eso_Dn10pm5I4R3TN07RsIDKIpajwAtCsCYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9GGOcqp4AudYK-7wj4tV0e51c1x8hMO_MGnsXVGmljEwsqV9AihDXoY_tfm6aQs_8Loy70h9g8HETPzfAtiF35-zKALXfoV9hUiaebpsBet9-YkiXzmS48LsrrMma3fzYMfY0-c4cD7mRSzev5ejIcet60QUY3Nh1ryyzKSdbmtM_4kobdTEkxf1hZgrVzY4VBRogDWu6QhbavEx_w4GbPzZQdlpVix_PkMwiERLTKaH6nJduuIqNUKUVJPYGJtNh5161S7vjRDD8S-XBWr1v5wiM_JgtKltvJK_2hM7eIFESvBXIQSScMaU6Ma1U9fLog55sf3zA8Bs1ZzLUhHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snL9YtahaJ6NP6x81T1sZFxKIE0mbUc65-9X_JQeCiUbtghoQyL9Jk_DvEyGtqvEB85jKZVTJWPXuQoL8v8FE9_BNhHOz6SIXqew4QTsg4WCBrns_1qkaT429YB-M1OqbTEPdoVU4hIJiZFyqAFnsSEMqrN6cIolRxp9VDXwRKdlfjtEmEhI4kgum0tUwuzGLCbmSPx3NT7mOiWA2yspnhJLl-YhrztwFucOPB8s6XrFNfFhlOEovYt2Q4KuWoKU84q3yk_ehThay5w949UHwFgemXabzSRYqHImcGMn9WOAhhLT2wVcIttrwiuq4eNVtX9KopJZE49WOQLP8KLljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf3kP6EEXdNU8DCdLR0bvOqMKvPQeluq-eWlxFcXdkBBSKAKA15JILyqxTxz21X5JqspZp05tUVVoFspNuC96z0fdhUrVaiw3EyRFAALgj2GsSYcP-XVEV-MWaXEup08h08PHJngnzJ8ibhwU2IXn1ndP49QWHGkfx74vFWK_gnPO9nNBRR3kyBEO7PwTYkn3t7WRXdlknxu1Ks0r_Oow67S8ScKumqrKwe06RThb3j3ecpsMC4sCTyrALSnkNsdPhQau68EbDQ6WOgZHUInnMSQL6JUipNHvXwXhKcktxzLBrqMc_NQm9bc-BXszseIlgn4t3OC3R-RQ6v2IZdzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=sBYavKqpNJtYvhHsWO2mMD-BltcNBb-3CxujxEDjWEWR-6C3l6ETMpYVLaVqBjUg8_oHuD7Shru1r-bxnOilMuAAetlmlmgAyqelmR-gbSW3_iFJxSvOErj41DNXwTxkyKz2tLOj9_3X-6oz8J2NqE00wCOLLy_2JUhl9guJnmrAJaCXaNq9yY5ElCvRkxemXDjI7YKWnOmu-kZWG85wU51t_NKBsUfEv512L-yL-h_-GEFwpN4H8unuJV6_8fwiBi460tEljhHH6OxDtGsx22uz11NF8YRIOvIrbq3ncJRJPCgd5z9hmKgoHzIvpIL9y1xymm_OdrkWfEZH41WFWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=sBYavKqpNJtYvhHsWO2mMD-BltcNBb-3CxujxEDjWEWR-6C3l6ETMpYVLaVqBjUg8_oHuD7Shru1r-bxnOilMuAAetlmlmgAyqelmR-gbSW3_iFJxSvOErj41DNXwTxkyKz2tLOj9_3X-6oz8J2NqE00wCOLLy_2JUhl9guJnmrAJaCXaNq9yY5ElCvRkxemXDjI7YKWnOmu-kZWG85wU51t_NKBsUfEv512L-yL-h_-GEFwpN4H8unuJV6_8fwiBi460tEljhHH6OxDtGsx22uz11NF8YRIOvIrbq3ncJRJPCgd5z9hmKgoHzIvpIL9y1xymm_OdrkWfEZH41WFWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=lUDtLzZo1fUBLdTRy4FvPxRA2a8Ltf8SYt-m4LpLhe74k1vHQ__XO5nacXVVRjZ3PBVPFLLdzeR0GZCJZ4h_OTAL5hFVm8U0j7Ly-VxT3F_moNi9a8Th29rvXoukEKeivE1Y2wpRhBYhDTI3GH0kY_XRbNGuSLwS83GmoesXzhlADQQlvJ1jl9QCzSaJP997kQSdbuQ79WGqGCCu9LG_N1Eitl92q0X9MFgqwWYqqSFGLg8qTlrEYobNGmyHj3FGvlEtFzaVauvlzBQI40i_HVgaCKq7oWkZfqBmor_pB_Gp5dOGYm_jr1rbI2AstgvT16MqiE66Or7PrI8Iuelsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=lUDtLzZo1fUBLdTRy4FvPxRA2a8Ltf8SYt-m4LpLhe74k1vHQ__XO5nacXVVRjZ3PBVPFLLdzeR0GZCJZ4h_OTAL5hFVm8U0j7Ly-VxT3F_moNi9a8Th29rvXoukEKeivE1Y2wpRhBYhDTI3GH0kY_XRbNGuSLwS83GmoesXzhlADQQlvJ1jl9QCzSaJP997kQSdbuQ79WGqGCCu9LG_N1Eitl92q0X9MFgqwWYqqSFGLg8qTlrEYobNGmyHj3FGvlEtFzaVauvlzBQI40i_HVgaCKq7oWkZfqBmor_pB_Gp5dOGYm_jr1rbI2AstgvT16MqiE66Or7PrI8Iuelsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmunKI093WfGd9vu118LxEraZi0wyZRxsK2gbirUsjuLjqMaV9yyP1tHyG7siVVzy-a-nsVKDW4g-mGVLCJhBTSyTyUMMBlaEy-zQQWc4Z39sLGBLP1Ogllqzxde-QC0gFcyBrQ8PT9jprzDKefmgnac6jUKmS7LH1IVaT5jUNN2qGr34R3j-zynAg6QcnhGqfcVTpjZX_VUJP3eGf6btfVDNrYX6bGLcBDl_LxzZj98okQf1paZTaj-X-hheaKZ-GN3zcW6TRDEt-OqTh0CLCslzU1N6-C3xGgeTl0ntkMfYMU2j6dOe6O--n4jnnHSuZcv__qmjCH-06U2-Yt2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iN8jbzMvKpw8zZ8rheLBGzB8prIbBYs-0ELTBPLPrnO1UFqnXN0Yr2l_aYissPSCv5jBjHZeQTGTOabD4BcBT0yuL3Xibegs3VhJSYBwYma70_eLQlxZNQO8nOLZuXmt5nUZJQLISOguMLp1x4wGlVdkKRhiMV8cGcw77N7hmsR3MYrQfTRDi-GdxA-yIrpDLu45mkPPbTPmWPtT3VH3r_NFcKQJQgfyU3ku3FDYSIOkrJ2ZH8nHlMEttCgRPRvhAFhBhzxs466xOJxb-Pp3R-40EnvcMuuuw2erD87IAPATp5iMa-YzhqtkldGOUWqjMF9TtCvXZKEIEBLpb26xvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=IqE-KAe5Y9oD4nPKQkYAkBjEO-4U55MQ_rriFVySoTZsGMMuerymWI3R-BNGHztBOSqAV4XPt3UxTIxBjLI50EZFgevscgSeGm5wvm3vNakd9K0SE_ZOjbrpETjz1FnBakS48IRXKdT_60yOoo1iobcAebN8WZe9XhW0-9pEPFulLwcygbHxhN3Ey0-8_W9eTv32nM_LMJtZb_OBq4TRXmYvSSe5avjgWgKSGPmiJvTnUBqGZUbwmHP53s9aIR31V_ob7jxFFLpex-c0MNSFebrjW7NKVkVcoSsDEC74R2B-A9EayXxf1h0P9aWe_-BugNmRhUCWsW4mkSo3ai5Qvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=IqE-KAe5Y9oD4nPKQkYAkBjEO-4U55MQ_rriFVySoTZsGMMuerymWI3R-BNGHztBOSqAV4XPt3UxTIxBjLI50EZFgevscgSeGm5wvm3vNakd9K0SE_ZOjbrpETjz1FnBakS48IRXKdT_60yOoo1iobcAebN8WZe9XhW0-9pEPFulLwcygbHxhN3Ey0-8_W9eTv32nM_LMJtZb_OBq4TRXmYvSSe5avjgWgKSGPmiJvTnUBqGZUbwmHP53s9aIR31V_ob7jxFFLpex-c0MNSFebrjW7NKVkVcoSsDEC74R2B-A9EayXxf1h0P9aWe_-BugNmRhUCWsW4mkSo3ai5Qvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=wBKOfwXo_Ca8u580zRKRZlzjK4WjoonHE4MUP0ic8e0Jta5_IODT5UN-5CkxhJQgpsT5rgnze099CZAgqMduF0_N3DBXEZjebN_4Jdz-LSCs8ApeDBfQbS-eEZ33hpIyFZbkel6xFwGWU-JlS7E9hJpKyumkjgPLImcsWlg1GQkiu6HAbwKNREHnDHohk1BaVmSD3u1M1bG3li_Ck6KL82uyrcvBrxRHx9Vwx7sHhkKCFqiLaB9-uxqH5adgd4BLqPZtkYI5wi7I0RSR7To_DJI0QN9LfMJ4bjPTYpWEWA3oWY7-wFDUpnMk6oksBnMlH2XLc5Utm6b-esVqyxlAw0shPI-TyO0o4OMwzyfl0dlAsWMytTrKtrwtZNF695demEo2shDTsIpaKcUmCi1nvqs0rj-8ffOLJV6q4zTvtMAMbZAAQC2E3FGFevfz4PqNytAGyWuzMNIQSfaBe-RCcyofVzpWcz6kcRtPR97wbSwgRRm4NxU1_920VNqGwxORbeAzz4UErfMRMtgALz4P2TH3jlkJDpQ745mxrcyXGnh4lFHkKVAk8C_FGgHNf8QP5ZcWDwaerEgAf090yaF5p9NBvLAhAIoaKuRnxXwswlD1Y7zwFZs_34D8-CxSc6HO7idOficn96eYHJE54xY5kilaVN36LwwAdF9mwjZgl8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=wBKOfwXo_Ca8u580zRKRZlzjK4WjoonHE4MUP0ic8e0Jta5_IODT5UN-5CkxhJQgpsT5rgnze099CZAgqMduF0_N3DBXEZjebN_4Jdz-LSCs8ApeDBfQbS-eEZ33hpIyFZbkel6xFwGWU-JlS7E9hJpKyumkjgPLImcsWlg1GQkiu6HAbwKNREHnDHohk1BaVmSD3u1M1bG3li_Ck6KL82uyrcvBrxRHx9Vwx7sHhkKCFqiLaB9-uxqH5adgd4BLqPZtkYI5wi7I0RSR7To_DJI0QN9LfMJ4bjPTYpWEWA3oWY7-wFDUpnMk6oksBnMlH2XLc5Utm6b-esVqyxlAw0shPI-TyO0o4OMwzyfl0dlAsWMytTrKtrwtZNF695demEo2shDTsIpaKcUmCi1nvqs0rj-8ffOLJV6q4zTvtMAMbZAAQC2E3FGFevfz4PqNytAGyWuzMNIQSfaBe-RCcyofVzpWcz6kcRtPR97wbSwgRRm4NxU1_920VNqGwxORbeAzz4UErfMRMtgALz4P2TH3jlkJDpQ745mxrcyXGnh4lFHkKVAk8C_FGgHNf8QP5ZcWDwaerEgAf090yaF5p9NBvLAhAIoaKuRnxXwswlD1Y7zwFZs_34D8-CxSc6HO7idOficn96eYHJE54xY5kilaVN36LwwAdF9mwjZgl8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcTV0sVwq78shPsMXPM3wK6ATS5MXwXD4LINRXv2Ct8FbB_6XMoSdPX74h50KKjohtioJGrd-FjO4VF7IJe9iYf7b4SMRnCVQgSQFhlksyedE_1eaAY1yFduJCCSCVpCDEotp7lGJa4QnkWd8VLXmTV5s7tGKmURVnpFsibqj7PF4RcJ6xmg6We6AD-BnWliMEkkTuZgTQIMu3AYPgS064V3OHLEPeS8PmIaQ9FvofcuH6ijBW29DpdOh2lD2ktKCnPvxOEOuDi2T2608uWbYsjE6uSOL_lgAWNuFuc4L0H8G51MeIMw1C4eICoMGVcMtsBikL3JmYOUIQjKDI-t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsWvu4SDZy31j1RmbbGwGmXf-Z1yTgK_6y6CJoO6uZkivvqrbbqLU20J6PNbld_qKxnTqxVbQTc3Brw_rdZ2PPhDjvGN_tbwQOxlcewIHRIR4ntdw5u8HJVaBfcMCWkIjK8vttzjJbMqb4Ah3H4FuKgv9Xf9NWKMVowQ0eVB1Ha8H0yqicd51GGaK2jUxRbcFuW2EA_L2c3pmxhhw-A_rPXSY4PcANqU9r614jc3xrz-aJa5b8Py-X2k3pinAdwG5syzW5U2VB2Tf6voyaaYvRLJPFwE6Rv7tGrl4U8AgSa5q-dJznv4rOcxOEzfeu17QJyW2iVcHMlUCSrkGvGDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUNNCD-YuJ_rKY0hbYepApTZ8Qg3S8ZpoJ2uKcRL_jk_JDoSzydbAtv2rf6pJAORdFK66PgfyP8hE3MN1tBGw7Wjc81GqeHWSwBYEBlt7cmjoiY-EiUgiAa5Ir1lOcM-O1B0jA_O8drBfsx0ungffdYOM2NC6gDOJzSY9A4nxjUAk84GS_3ZAKUbnxiuFzUUpevzRme04oqC_U19kGwlvD4gxD-aWBy2EpNF6j0LGmYV3ZtTK0uAx1NtAM_09chiXJv4Gb5R-eTpbgFRGp_fTcNC-RfzpKSvs5XrhufB9J20pOqyumjiF2OSIsQYF6bc-zQNczVKVeBB6XApd9kU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8OdLICF4w0d4pS8HcT0PlZ8zBP_Gzx3iPrZGU02NbDswDYBjlmW7rdaOWpJ54Wn7gGADGrKq8Tah7PE5wLxUHIygtEYN1Ze_AJAEKHzDl9pbPc-Qg2T4L4jLO69qoMgtYdThGsHr7pBQGRZVVZ8SKGRgDsTxDWdiAkSqI7BwGEnyvDemD7uSclfn3XiqKJG7WhrWdb2wZcFq8N9GYU6unwZANkmnmm1T3F1w4Mvcdh6peKh9lWWjiCBTlC4L8-cv-81qZlc-PtryKK66bOi0W71OkAKutN7ExfdRceRXY_4qTEqB4NtQ8OwgaqtCzJVOZDKM9kxzDKwh6m1ctx81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTWA0m9ptowiDj3ldalCsHDj5qprCWXl2phbYI2zDQVFPKxnqRzBLtUpJGwtINmZy4uumOhpZaTuoVJG3XdSltp9OExJXv0ErNZd7kY6pYVVDKgV1ir73sJiH8omoI3_l4XBf_8oJOHBMwasJHKLNuQG_ZI3tMylaBTtXTH0eFGcYYfMtcGdudd86AQMbcXm8m3KFmVs7d4OSOpXvsN0QeLBXrWbOSGzj-p3l7GM9OlVas_kKB7kfFE9mvLUTqS5xNibB6S03CTrTZKYfwHo2XIQkWbSMB7GAGJfltv7yarbjdM6oMEYRgwT_nORpUUO_VSI61ky_7zq-5LjkmkV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhxdKlEPZri17ST8GhMjnL7ZZSAWOd0o97WdKQNGNKCoQWcPD3aVQ8HutMVShH530ZRJmngxWaqVYFt2fc-yXvII0-G0JUAw8uSch3tgzqFdMuZqgS60MXqKofNKwcL9fq17Pi73FHYjStQeFMa2y94zcYzBdxH7xmQc8pEWiuqkm4576qjnXLic_40A7WJNA-SmztaMcPIK7dnJMRy3KIKsbIp8ekc8TmTwYC9KddDSARLintzQV5RlKsfVUY3qNwt741JsIsqP8Zt9r0dPYnsAxEK2Du3ddA4n6ISF8z6fK29ttG9NulpdGa55qzB-GmmMZpwwYCB9D-2ZpRO24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKLHx1nNTTXIwg-U3DQ4ClcjJWAthl40T-LdNTyWnJXEqbV0hyZiyuLJF2pdU27BGeKds6TPBvsFRkgCINFdBhenAXKheJBEkwKn9bt-l2BtLqmKvzxV_t61aQhRYPfbYucpSgULHf1QkWDlevXLK6kx6KAetjU6UpQJJImHCr6nAG3YrDOgEO5i_8SXW8uvftJRRlq5-fxxeMqaxTcn_eMQrOYapr6j6tlWurh9yI50zivEHW2QJSdPXheJuQQsYMhWjgMOOKKw9zNQ6uKBFG1fx-2ELwUKQINMLYfXgKvYk1w56MOAtqJ3b2zIcuxN0Ebm8KKC3R4egxKrhFgqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp_u72d7oB2MbEodFrQOQDcjNuiEfCuYWgx2q5ZBVOx8Su6LILOtZuvXU2x3_1MqnAvTVd77RQv7HmA-ZxjqWoV42NyYJuyFSmQUoTVm6DgyF6miffy_4YQFSvzhkeOkaP_JIZ9mURll5tRX9qKLs7Y3zat-HPncHXJ0_yBwmEccQ1iUkvJwQLCXEqxaBAyONQ6Y_l4xfe51PX9hswygrOmubtRym51B0VuVGsNJ7JpF8YKAf6v89FJusAK9IPnUxcc7m3jnim8pSKs-x15f24tOtRnjR5jwoxjonMVxUnLZaJFo77ElijEbWqN4GCXxvr3jXfcnspTfDszl2IQaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyA3ezshc5sN9oVqCiA6UTK6e1vZ1Nxt5wCby9NUUDVr2tMFUj1nrDAE_cAgDs2zGyEcfkiWweUMkNF2GfL5JmEQrBer_1QKuIghLF05BuEfvhhSARsHHon53KKe4qWMG08K7qXWYuGZ3DbzGCc6_1C43s_h3KQeNq0-BqlTZUpsGaP6unv1Ozhal6_VXuXRTXjMDa5DpvTeuS4w4EPlGk30scL4NbcXfYATKBJH1BVRAB7d6jGwiWuvih4abDZhxtpyskfdncjRAgKLlLMe2-3K8ywctov57TR72iMPTZJDlBtmHdu5dnO7LKzgtOaxjhSwvxl1537SAS0bKK87ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=QMVwEMbCAu5eE2VxDJMOhU1LVmOIA86LaAj6D3W7-7O2Bl4McIvUjrSTL1fG0xU8_4Osjg-8Zxfn40tO0uHo7mEb-XxMbHSWRZz-8pfzOc_gv0G1S3zP0WvA-W11X-5LUZNoGKyhzMxgV23DuiGlR__42GMKe0fDKKBK5Htq2Ivp9WBMufGb_tsZro2rfvZHc7zDGTF_ZtXgFvQKZNFMRr45W_-WmxT6JJdZ3AkoLO2GfuOPS8sV3an4A61kPX7PHOhIKmcmCs2Kp9HE2_9DDyxGQAPuRO7jqHaIw3phQ6BUTKtZcoMtzX_ayqLCTvPhH6E1gAM6638t3hDex-7btA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=QMVwEMbCAu5eE2VxDJMOhU1LVmOIA86LaAj6D3W7-7O2Bl4McIvUjrSTL1fG0xU8_4Osjg-8Zxfn40tO0uHo7mEb-XxMbHSWRZz-8pfzOc_gv0G1S3zP0WvA-W11X-5LUZNoGKyhzMxgV23DuiGlR__42GMKe0fDKKBK5Htq2Ivp9WBMufGb_tsZro2rfvZHc7zDGTF_ZtXgFvQKZNFMRr45W_-WmxT6JJdZ3AkoLO2GfuOPS8sV3an4A61kPX7PHOhIKmcmCs2Kp9HE2_9DDyxGQAPuRO7jqHaIw3phQ6BUTKtZcoMtzX_ayqLCTvPhH6E1gAM6638t3hDex-7btA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW9N1XvNIjI2eloJqa-bk7pTketYsFH37bqjX6_ZRHqXub3WF6GczHs2pzwLTspqkPdv5yel6gLcQiruiVH_DHHCuGTVNAY8FCN70NL25_HP7h6TLvHdgyaKKxzkH9ijRImhrs_ck50kmg_BSJ3iDuxAmZNQkV9aVjWGKZi8MEl5RiUcOwoqc1KWndxFDEivpXiY9okNoSZfXsJCr0vhNDyTzy9LDoU4Uc8SgBl_sMvpZ3Voi1aeC5k-Bnv22PRUkgvGLEe19k6AHuykNjTxSJirZ3LetJg6S0Meq9KgtDYucGSEmCS5PJzy5q1VXuw7E5v6ZOfu-M8wrCPyT_vtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=bezp451_Mw47adKGCkOixqX4SdO5vIfCOlJjXK6bRQtsaE02FfX_VIa6U7hBFc10oXNCY-OriYrOtjM9WsvPNxVeGjSciAgpMZp7o0Oo1Ua20tEEnwxbe3hMrkeJy6RtAGQc4YawOFnJ7-ivcr1XP6ufMFshBLLaVzXib7l3eTHTLmPAdAPYqBj48S6Y5fjHLVlbD7fsqlqi46ClWpf_tPNHQARwz5nuTPdgF-pQcDxBbF07qoyk1PZmgiB6nxGuVqDosUu6HKTti71Jpyw10lfPXqhXqs2BUvBvWR8T0gfKrwYU9fxs8cpHwesSgRGoAXqPHHz8OSSCEQv97799EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=bezp451_Mw47adKGCkOixqX4SdO5vIfCOlJjXK6bRQtsaE02FfX_VIa6U7hBFc10oXNCY-OriYrOtjM9WsvPNxVeGjSciAgpMZp7o0Oo1Ua20tEEnwxbe3hMrkeJy6RtAGQc4YawOFnJ7-ivcr1XP6ufMFshBLLaVzXib7l3eTHTLmPAdAPYqBj48S6Y5fjHLVlbD7fsqlqi46ClWpf_tPNHQARwz5nuTPdgF-pQcDxBbF07qoyk1PZmgiB6nxGuVqDosUu6HKTti71Jpyw10lfPXqhXqs2BUvBvWR8T0gfKrwYU9fxs8cpHwesSgRGoAXqPHHz8OSSCEQv97799EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
