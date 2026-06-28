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
<img src="https://cdn5.telesco.pe/file/K5KdHhrqbYE3bN8Xqoz16yQipHvGbIU501F09ppmQ5BVP_FyjxoxjHVINnFfTkgOVd5LGo2qhKgDtpYbkTPV1lHdlKG_vUl5zKeR51IwQ8JLqOxRMRzDNkXbk822GMzPU9lq9zQhxd0XRybI50iUYnB3iXkyqxxyr-5A3n_OtngYmTJR2oJ5nJykqYO6hor6Lt5fIsGP4MzzuHlMdLnLJP7C_3Fwrrdk5aUmCrlsWoez7WDOfDbLsujT8zDiDkoUW9ev624_IV2qPCEAunnjQ2wMXfIIXZ0askuf_XPUNuggih5o4Irct_TAGrAJoTcnIYI73cFl16fAXSKsKWb1Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 695K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-96658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vo4McMsm6DDst9ABZBvqIit5x268PPu5aVIMzs-Q-bihQ0MraujsuC5B25OsODvpCfwtsTOY206MwxXjdnhvKh218NgdlVI6J50ljeWn_G6KP1dk-KhltLtnH-2Q7dDcg_kXThxMlOrwGzI1ShgGKsW2Keb3gN74kU4R0Q5d3NPhbRu6f8ScQmgTDHKBTtSTCTnUFSFy83U8IFRWvi2Cg5MQMWvvPm471-ZT_w3rM_6Np1BITJWDGhON-E7arFNl73DrQ3Mv6yGSpBjBO7UJS5dEipyXB6bUE2hFT7BdOZdhCxj4cH_06TXt3l_ARBEJfmrrDXPkOFe10kZaIkUQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myoxrrvRZLoG6WC0X2IW-dLRUZmd9tKQGmHIJvsGZaHTBp-rOyN_KY6a2BYPdQ7mAxMzyQa8_DfjweRDvg5LkNKQzCHPOLitWAUtPoKXGCSJRzej7-y0jOjltTgoO8QudILFdZ0f0bxpfx7GLfJ0RA7tEwAChlos0G-3A-aXBYua5dV1OarS75FMLHdbmXkYb-fgeMA0aqlz93bVqVNJbQe7M46mcwW3EhM2_SSBzMAvO1Q9WQRZqRSLE2ES5mue-ScHnZn-ZpjkYn-J7R4rRYpQVYGGAN0kTsv5BLVxQb47Qo3o3AzPj8le38BW5uAxWSYui4vd-_FXYfFbEMTVnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یورگن کلوپ:
یه استوری از سادیو مانه دیدم که عکس تیم ملی مصر توش بود و براش قلب گذاشته بود. از اون پست اسکرین‌شات گرفتم و برای محمد صلاح فرستادم، فقط برای اینکه مطمئن بشم دیده! اینا همون خاطرات قشنگیه که همیشه بین ما سه نفر وجود داشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/96658" target="_blank">📅 17:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt456INXgWqIQnrZufnjZv_HQLpAE1F6Hpcdw5Pl4KlHvi3_VXvQu_bnbGBpit9vx3eodRVGbb2JxfvPH6YM8SQLnf1J0X6p80d29h3Jj-4quc69rGmJWvmkq53XbKomJiuUzPpssTpZZgfQj5arr5EtZ85XiOHgo80BfKEKYAEok7avPr_cFX7s792-_veXJdBJ1Uvau6nNHSdP8gO45gHUp98h5gUDg93dSeotaXjq2urMe6Cd7OlOAKiHt2oUugeBTky5zDaK5pPt0kPg-tn4yFB4bvy_FdrVan-aOB7dmbdLmQattG6-fORpHnC7Eqdj2yAYX4DHEFPO-vvd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیووار:
در بازی کلمبیا و پرتغال یک فاجعه رخ داده و گل کلمبیا که 100% صحیح بود، مردود اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/96657" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDpUqeTBeuLDPZwMhjgO059FR3hEchi4ZlgJPf9E5tIrbC5K3QdQ6n3HwA8BwQBwNZ3YcycqIhn-5XVjjlLMTvA2fUiJSxxM9Zkc9zqCfGu4ZG1dXxq0QkClGWwJ6fn554g8nr6k6dFj4JipAGkqDTnunjIQqx-avFEm8EutaxdkKT7Wbd7VesCedP9F3vmSRes5epqCaEqWfjLNod0iDq2vzyKisRY9oeBoGJa-omGtLv_u9b7aBRBdcq9O_DV1nX296e6rfEJMhZfve8vZoQqpvYzWfQ0u3kXQ-gRJGT4Pzm_9F6uV38nlnA-zplOdkEOD46VrawkKDAf7s2X_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان والیبال ایران و کوبا با برتری شاگردان پیاتزا
🇮🇷
3 | 25 | 25 | 20 | 30
🇨🇺
1 | 22 | 21 | 25 | 28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/96656" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjUn_7ZOprzf36HeOK9M7rhXi8pDVBO_SwRzHjYxyH_K9pHCYB6C4PxlaVKt0pd3BhjAC_vuqg6Ib5iVt5F4z5vlweFmoOO4lrk-W6Z6z9AVC351xXwdfyzT2_IBbetwf4OAo9tmnK3TBA779qgxgKX2aJy4Vau5tghwx23s4jP8kkz1U_OR21DGgQafMVFh-4dAMUv6X2TkKgzpLyeOszmAOlIOnAzY16BaxLkCZRsHR5r3VhFlEiezOM6ahakiFinX9IWit2Ql4xc8UR2l5ipPBN_vKNZS5iYCzYVTFyiwzo0pCoaqN3P7Jel_KirIenLgni0SHM33MJG9cb66AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سراسر حق محمد خاکپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/96655" target="_blank">📅 16:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNEM1RBZQtcPAcvBJf_YRVAMOrKCYjj_7X-7gHm7oWZZ9nr6wJQLyqrm0OzfEaQxbsMsqN5GZ4Z_u4tfz2-zQNH8OasOAYWSZnfh5Xxh2wKGIlWrF8uVwpW1W4Ethac5XtoF67KWpyX5e8zAOZQuf1T1pBqHlVzE5fj-nIgtcsgfuaJa6yDijG-O3Uhhgzh7dyyMmEPEagZbt0HA8fpfWM9N4MWHLniOqKtWcc2KL2hDCqvHFpCbTjhni93qnob2SvVJs1Jd-_8ppSGOZQqp_aHNYYuDKiSdOc2RR9r4y_zbmX8E4ybLiEYwAyUNEkph1Sorpy84cA79IhBPg5MTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
ارلینگ هالند [
🇳🇴
]:
🇫🇷
فرانسه خیلی خوش‌شانس است که امباپه را دارد، کاش او برای نروژ بازی می‌کرد، او خیلی سریع و خیلی قوی است، او بازیکن شگفت‌انگیزی است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96654" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😂
صدف‌بیوتی و رفیقای‌شیرین عقلش وقتی صحنه آفساید شجاع خلیل‌زاده رو تحلیل میکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96653" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZxgULz0fmfE5dFU37i3WEYzsAtEl4phWgM7nz9XD-yFx0Zh4O-mlLuz0IBQMIMTWmv9tKe6v2lVuixOGZwcxI23A1bqSVpHJK_TKmPdTBQEwB5dVud7ipKKsomXl55RihmsmejIL-ONJE58PiavJzL0guJ1ctHGvN1xxhO_R37IxFtwcbHq5mAcbBBYqxVfXDDJhlxzWnH9XGS773-S-Fx68v3jS2kJTreoJWj_87HQUq-fTtKPYMOFX1MoJiKDNhuhruDbK7TKciZlVqQNaYM9FxsxdL2mom40dMj0EMGziI1-nv625XJ2m8cJUhjZ2o6DFQpXD-16iCqiwqqgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌛
پست جدید اینفانتینو تو اینستاگرام:
تبریک مجدد به تو لیونل مسی؛ تو رکورد جدیدی شکستی و به اولین بازیکن تاریخ فوتبال تبدیل شدی که در هفت مسابقه متوالی در جام جهانی گلزنی کرده است. تو در دور گروهی عملکرد شگفت‌انگیزی داشتی و امیدوارم در دور حذفی هم بدرخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96652" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه مصدومیت وحشتناک والیبالیست تیم ملی کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96651" target="_blank">📅 16:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=v2rVY7t9CByWlE0ZUZe91qFHMN-BcHxrlg5sgKW4xy23XOXH2Cle8m0ae_P6I5R_p2UUl9SZcKW7p7wAuy4d6AQ9hkIQwPLPVCOF95Ge54N3hg-yqcp5f4ck_7ufkLD8pAf66DX9OY3wza2sbqLfpTY_HOW-IhWoEi4YizWI939dA_05xIQVYKXKnxJJGQstANNXKkpTZJ3svem3Zwutj8mJbO-dLW5GErdsV0j0WTIV-S9YgVqRtzxocIt0t_P9rbuRb9ajbr3i0HnZGMN2bWhBbsdCApkjwapRvdzrTiC_awjmqiV3Jx8ffqqP5zfWOhxrLAWkl46rJ8XZnnMshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=v2rVY7t9CByWlE0ZUZe91qFHMN-BcHxrlg5sgKW4xy23XOXH2Cle8m0ae_P6I5R_p2UUl9SZcKW7p7wAuy4d6AQ9hkIQwPLPVCOF95Ge54N3hg-yqcp5f4ck_7ufkLD8pAf66DX9OY3wza2sbqLfpTY_HOW-IhWoEi4YizWI939dA_05xIQVYKXKnxJJGQstANNXKkpTZJ3svem3Zwutj8mJbO-dLW5GErdsV0j0WTIV-S9YgVqRtzxocIt0t_P9rbuRb9ajbr3i0HnZGMN2bWhBbsdCApkjwapRvdzrTiC_awjmqiV3Jx8ffqqP5zfWOhxrLAWkl46rJ8XZnnMshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗽
تو مرحله گروهی که واقعا میزبان شایسته ای بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96650" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxneN4wqOXnTwdqq_kRiJMYDwn2v4qcyLJpZBSnCyWHzJKwjiYQeGeM1Q4kBi3fhNcshPHKgkhxytjbDauauZQFavuUSo-nDNC55xSKE39Uyg5oLc0beiqSkoBDa6nItg4Ry0S7gCzKzQcLfEYpaXFQALTgKG6x4OlSixDd_98SXZf2RKxcXKwK4x-rNuzL9JMhS-WbDJkmWtDYp1szC8-G1-RNafTpaCLCsT7xovqgT7HyUllDPTA7yhA7XNOVqnCSe6SnAAKPgh7bNNq8e3Fyju4wx1BTe04H4DY73s1_YEOBICYa_lLv1vstVa4TR0oPuJR5uB8JEw56hxBXdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله گروهی جام جهانی ۲۰۲۶ از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96649" target="_blank">📅 15:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQm2ksja9yh8liEaGAjxb1W0RfWYhniyhdyPkesGN-Rv8avDClk3g1UNAhiTGwC2K19eRevUfG2NCh7bkbH9fuMFMBSFeRjPMjEYhTDoNap02BFssG3cLU5z7K1O0GS6NkfK-gbDZkcr6PqjPEjh87UWbEBg5A4bylmn59OMZboi2HCB3LMTWXpBWT1YyltNRjDXsPZD91zAWF1R-KCB5_x6uBLJ_L0UeCvXx2nMJ7UrY536JY8TKirCjiemwTFZsMdKEL8RR5oScBCSR0WTPjb807RNDWMVhAREwVMogdgwMQV8ksFtRzwKhkQc8__v2vDv9d3p8mZ_mu_u0mxKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
رونالدو بعد از بازی با ازبکستان گفت "من برگشتم"، اما کلمبیا تو بازی دیشب بهش گفت: "به دنیای واقعی خوش اومدی!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/96648" target="_blank">📅 15:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=ATZ9DKztYBfdbjfrl_ZT1i9iK_RBaqNgUmb4LUqPzOM70VgpdseJFP905WzQP12QaE8D6uj47I2sL1rvFn770V7h3KtY7XxRqVpmiy2rTCr-VH4370BSydFDaex06cGp7WCE5BkUWz99dml3ILGakfJCirHfr06L2LZ_p9HoSYzSnx77-VYxB7ExJtzKkNv2wBEuC6orTbL_ebr1SEd9Cxg3G8fjwAvtz0PC2VJd5cXYLmGyAnb4HYhV6Us1Ro2oBbiiYtSnwNJ9FKX-zGre_E_j8cUFBIqqD6LYsiJ3RIAfkL7dC0N4V0UGd974G8jOgBC5R3o6fioJhnAHywiG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=ATZ9DKztYBfdbjfrl_ZT1i9iK_RBaqNgUmb4LUqPzOM70VgpdseJFP905WzQP12QaE8D6uj47I2sL1rvFn770V7h3KtY7XxRqVpmiy2rTCr-VH4370BSydFDaex06cGp7WCE5BkUWz99dml3ILGakfJCirHfr06L2LZ_p9HoSYzSnx77-VYxB7ExJtzKkNv2wBEuC6orTbL_ebr1SEd9Cxg3G8fjwAvtz0PC2VJd5cXYLmGyAnb4HYhV6Us1Ro2oBbiiYtSnwNJ9FKX-zGre_E_j8cUFBIqqD6LYsiJ3RIAfkL7dC0N4V0UGd974G8jOgBC5R3o6fioJhnAHywiG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
خلاصه‌دیگر از بازی ایران و مصر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96647" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbgAXvV2Kc6BbywqXxn_ZUW1TGo7A5Qhs-Y6xSEyx7Jp7xX47jr5BtO4ml6GpcnFNqTfyXY7umGA3Y5QlWg7m_QDeJsdEL8Tys0-dx-gjmP6x8LHRGdYGbx7U_O8Cz02Oa49NJ3fUa_huxFOShwRoinBlIJMUxw8CHRhJ22PFGJd4U_ZM_Bp2qzk0-o1q0pqY2o7moL1EchqMRVwex9aVqb1pMWpd1Emabh15DWNg5miRRHiWTSv3bSpdM3ZMsLdwWCTIiRj_b8DjVDf12OClg8bJoz7tX_tgmMHaNGvK4UMo0EQN-3LS78AMv8GAQC6IGG04lz1Nxbe67zwDi-jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر چند هوادار ولزی : ما اومدیم اینجا و به همسرامون گفتیم ولز صعود کرده به جام جهانی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/96646" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg4bOqmbqdzrpiX575JkTBGele2OrbBuuZi67aRofjXTjbtWlfe9mp8jYtsvgwoIwQcSMsdaSz0R1qEd9l7gzC64Cy-1bZq5qqDKxKkFk00WSSIOZenqpwFA0-aXT04sKCel1clbz_RB9Db-UrfyqOz4-Ac3Ym6wJs8bGcg9bWtRpbt_jcBCkZyBg_81-rveXFDMoxXdCK_wNoFPnIJB7BudDs8PObTYZI64zw0Y_8CWGiFQcjjXrAY89UfBTXloXHUNN0I0OodbuNgHgv0iqbuClxCKJFR7JgDIn1VY-vD-so6KlV-k1jBGyz9swl0aq-C7wKzfbcbGOmWoptdB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
مصریا بیخیال کون شجاع نمیشن.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96645" target="_blank">📅 15:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
🙂
علی‌نظر محمدی سرمربی شهرداری نوشهر رو مشاهده می‌کنید که درحال ماستمالی ریدمان تیمش تو لیگ‌یک هست. این برادر بزرگوار سابقه طولانی تو ریدن به تیم‌های شمالی کشور داره و داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/96644" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=Dbuo_aAwWyhLYpt3B9xIMFXYnZ98f2c7TVcT56Iii73O_tAV-i9sqfQp57M-5l-tTaO3v-7giZ-410EZWGO_1VNmhT1a6UZbdLmZcavK-lG63vxYK5-UXIKKtkOEUjbpK3oxlEkS1bwB2Lh903e-Z3sgSgT8YdzdREtFxizdjlJCLh4phnK94gXvmMhEa5dP64Ly5V-TLlDonl2_veqPGnXCnSnWn6pV0O24Gl5wBznHIzuXop3tTIi0PZWXiN16GeAibAtOHCPWOjCGcAjm_TLuC2etS5NSh64vALKjJXYjJ7WHqHTSZECOqOM0UgM77yedFW39Z0Xv2MtGILY4jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=Dbuo_aAwWyhLYpt3B9xIMFXYnZ98f2c7TVcT56Iii73O_tAV-i9sqfQp57M-5l-tTaO3v-7giZ-410EZWGO_1VNmhT1a6UZbdLmZcavK-lG63vxYK5-UXIKKtkOEUjbpK3oxlEkS1bwB2Lh903e-Z3sgSgT8YdzdREtFxizdjlJCLh4phnK94gXvmMhEa5dP64Ly5V-TLlDonl2_veqPGnXCnSnWn6pV0O24Gl5wBznHIzuXop3tTIi0PZWXiN16GeAibAtOHCPWOjCGcAjm_TLuC2etS5NSh64vALKjJXYjJ7WHqHTSZECOqOM0UgM77yedFW39Z0Xv2MtGILY4jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
اسپید از شدت ریدمان دیشب رونالدو کلش کیری شد و وسط بازی از ورزشگاه رفت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96643" target="_blank">📅 15:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVZAgKRBMaSdqAoQtGNIyPyijScRZRB45-5Do0sO_RoT-a31_HVB6-LxP3GnhP9l6VK_1XDrTG3br5X5GRDqyXJJnfT4S3x-uPU-seoy0-KrOad0REp5ZRDCaZEQuyVb17VbOY5VKLz9c1B4e64KO5qVQz_1GeYeglD-G2SVuH9u6KLmdUUZRX0HQFcDVkaqmCYPvQXS_g2D-TmSq95hdduRbDTWamFxwaxJrTHHQoHgyTeq3paZvaGgYY-XV3IpFtsKzr5M73QoI_PDCpK7cjk2Rpj3uPofcGmlz3laRne0Yrrxw6rp-CLDVYvKu34GfGRSv42YGlJ5EZPNEQhUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇺
🏐
🇮🇷
اعلام ترکیب والیبال ایران مقابل کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96642" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=HIIW148jcOJXU-uE6wDHOfw3whQyFZXFUX4X4r7orfFL7T_d8nKd1kqZnIEJKMDnmLevszKHrPjKpGCcP0DdJg8KfoOSLStkBUQ10HYOBwpST_l0yT05o55-_vX1p4ostmOTEdWfJj9qqm6RJvPJiAOxta38EGiNmBVtPVL9iVpfAJQyrohTyoSrjQxaKpBfc_iUzeKTdtqsrcZv6AsrrffJxQKOOPIC9qrVbuivmR-ttT5Bp76-0Hs36xi7JzU4QaY3wmjSDMxJWnx84e_ziim4uAf4UCoU9V8V0rqzGuxt2FsottV0KtGAPReNWf8CPhgdbDQNKzsbPFCfwlZSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=HIIW148jcOJXU-uE6wDHOfw3whQyFZXFUX4X4r7orfFL7T_d8nKd1kqZnIEJKMDnmLevszKHrPjKpGCcP0DdJg8KfoOSLStkBUQ10HYOBwpST_l0yT05o55-_vX1p4ostmOTEdWfJj9qqm6RJvPJiAOxta38EGiNmBVtPVL9iVpfAJQyrohTyoSrjQxaKpBfc_iUzeKTdtqsrcZv6AsrrffJxQKOOPIC9qrVbuivmR-ttT5Bp76-0Hs36xi7JzU4QaY3wmjSDMxJWnx84e_ziim4uAf4UCoU9V8V0rqzGuxt2FsottV0KtGAPReNWf8CPhgdbDQNKzsbPFCfwlZSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت ایرانی‌جماعت بعد ریدمان اردشیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/96641" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzFOC5usqJss6dW5JXW9T8ZZpexorEo6pQB5jFUnPs57ghjVpeMfKbXuUa2_fdxW20IG5S_AKMQebLxTtTSmT5KJsdXb5J4FM8J5WFBWRnkNjz0q5cf1g84Fq1nv1oM943GusOwj6PqK2NL9p1EJXTzv4mW6SpFI5xhawi6e8-mxLnoR9waEso3TVXKXw_0WBF2dwQpuCMzZr7P4nvdfbGgfQJE2m0f9xe52JP5f6-OR23S_vP5tTOXfv-JSuR4AaAuttqy-8A5en8WwYVlgsVbeqXSa9GRGSbNiNJb_O7Fk-I1UhPmDpQkJCJZPAhxZs0VHZrsVFPmUVGe1CdStag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
فکتی پشم‌ریزون از هالند که نمی‌دونستید
👀
مهاجم تیم ملی نروژ و همسرش، ایزابل هاوگسنگ یوهانسن، در سال ۲۰۲۴ صاحب یک پسر شدند، اما تا امروز نه اسم فرزندشان را رسانه‌ای کرده‌اند و نه عکسی منتشر کرده‌اند که چهره‌اش مشخص باشد
🇳🇴
در دورانی که تقریبا همه لحظه‌های زندگی در شبکه‌های اجتماعی به اشتراک گذاشته می‌شود، هالند مسیر متفاوتی را انتخاب کرده؛ او زندگی خانوادگی‌اش را دور از حاشیه نگه داشته و از حریم خصوصی فرزندش محافظت می‌کند
❤️
👶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96640" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96639" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iRyaHBJmJWGSFzvcPOSzIjaxBvn-gPbj-jqXnGsGcsnN_c_6CNHUg2MYzrzxhxhGIZGi8mio8FP3fFLF_XWn8J4ntxVA3pZcYupI-20_i0tf_5xInFEkQUpUWS7aO5O77FtPE2HNJrfWonkQ3GnBUGlN_jPdyC-6GI15-i57VM6mLt_z37wW_PjHCAFGDux2GKn54gOdv5V-ttJhlpdGqLWdpLlHBvJmPn3Zc6415z_C9zDlHyFEvba8ib3na976-taX5n9tCjpz8838vra7DrDwHl-jqF3HnpJU4HX9ePnpTZ2h4hfYoHW-waXD8VMfHQ_axy-XO9l6EjiEen4Ktl_bf9JIkvZqmqNcy7BTT0ePWq_1f1IRZ5YcPX2xFhndpN5Zoc208b7FVERMH5k4wIK-6BiLZpdwr9dOBtv0HdRpaCvclZDd_GHrYMfOQxjGT65Tl2UOvhdj30Us6eAeceOdsxLakhfodY_jL_9b7bT7bRmwkq-IyJDtZDSdpY9Xw21W-WEYMJQlYdiSykSgg4F5JFHDWEKfGFML6iBQiRaawllF7v_5eCej0K629-jwwSZYdzHDWjUMai5PqHVcKBSSEm30B1HdR7TpQlXzY6cDktCsdJsLxHDaSnr1tF_VB5GfXN0ogC8aZ_e_sD-e2WGOnNznjSZCisGG-phFZ90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iRyaHBJmJWGSFzvcPOSzIjaxBvn-gPbj-jqXnGsGcsnN_c_6CNHUg2MYzrzxhxhGIZGi8mio8FP3fFLF_XWn8J4ntxVA3pZcYupI-20_i0tf_5xInFEkQUpUWS7aO5O77FtPE2HNJrfWonkQ3GnBUGlN_jPdyC-6GI15-i57VM6mLt_z37wW_PjHCAFGDux2GKn54gOdv5V-ttJhlpdGqLWdpLlHBvJmPn3Zc6415z_C9zDlHyFEvba8ib3na976-taX5n9tCjpz8838vra7DrDwHl-jqF3HnpJU4HX9ePnpTZ2h4hfYoHW-waXD8VMfHQ_axy-XO9l6EjiEen4Ktl_bf9JIkvZqmqNcy7BTT0ePWq_1f1IRZ5YcPX2xFhndpN5Zoc208b7FVERMH5k4wIK-6BiLZpdwr9dOBtv0HdRpaCvclZDd_GHrYMfOQxjGT65Tl2UOvhdj30Us6eAeceOdsxLakhfodY_jL_9b7bT7bRmwkq-IyJDtZDSdpY9Xw21W-WEYMJQlYdiSykSgg4F5JFHDWEKfGFML6iBQiRaawllF7v_5eCej0K629-jwwSZYdzHDWjUMai5PqHVcKBSSEm30B1HdR7TpQlXzY6cDktCsdJsLxHDaSnr1tF_VB5GfXN0ogC8aZ_e_sD-e2WGOnNznjSZCisGG-phFZ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/96638" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee3960474.mp4?token=g-1tPIywVuw9BnF7tGqU9RW5gl1xbAMtL_pwLhX_FfGr6q82-60aD2xRB6Rv5Gs88v6WT3tw9c7wfw0eTdqHAZgcpoDmVHKOVJDwkQGvU8Nh-Fpp5NM-PUkHCwqUPn40IQVbZsWeXSCsU0ouPySprI4K9TKo6Jyc4dFeuLKMZEFGmjmo6k0EovHsZ8KpyfRT7HKvxb8Fep-xYNh39NcH4sMU6WOwLy-UY6Q3nU0aLuyb22wNIK13NwwACJDiyyPnGyys99bz9wFVguRrwOPdP7amt2f9AiUPVF4UaHGfzw9KQOWMOYAFGLZA5riQXXP5q2rEkXIWqrDOGZ-88HprPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee3960474.mp4?token=g-1tPIywVuw9BnF7tGqU9RW5gl1xbAMtL_pwLhX_FfGr6q82-60aD2xRB6Rv5Gs88v6WT3tw9c7wfw0eTdqHAZgcpoDmVHKOVJDwkQGvU8Nh-Fpp5NM-PUkHCwqUPn40IQVbZsWeXSCsU0ouPySprI4K9TKo6Jyc4dFeuLKMZEFGmjmo6k0EovHsZ8KpyfRT7HKvxb8Fep-xYNh39NcH4sMU6WOwLy-UY6Q3nU0aLuyb22wNIK13NwwACJDiyyPnGyys99bz9wFVguRrwOPdP7amt2f9AiUPVF4UaHGfzw9KQOWMOYAFGLZA5riQXXP5q2rEkXIWqrDOGZ-88HprPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدادی که فیروز کریمی تو بازیگر شدن داره رو هیچوقت تو فوتبال نشون نداد
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96637" target="_blank">📅 14:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhGFN7x3RiZsIo9GUYOzc4dDF5eWIcAfal1MaS34AIhm6VebtMmd7QUzJmm-snjpN6kC2HjlNncRCadvPCdlWNPU6xdO_G0Xo0I53xqPYpeBlOZSVLLVEWrLA9CnXphRV9krqyxedzMYoApWEzE18wuN5QgmdYSZiFVqloa8iyES-UAK8LqfzTJjlYATZaHOhrDI32MGBVKkBq4wiStxyDgyaM859f6TP0HQc7ssuDynJjcjYA_YsnJBV7a_3rN-joGrh6GwyLH4sCrcmM-mwHSlht9doAgRWLCENriHTurvbF3geQdogrNYCAiWMWO_SydVHC-ac8KYAgZB08oI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL3zV9QE4KNG_tw-XnV-Z5ERfkeURLXmHNpqcE3tsWADnAC_dviMlA83MC-ZAUdlzH8iaqBhgZWZukE4ZJLlD9ROFrOuj_wMYlRuRqnGgCoLs9vNGUbZ6CJcSpVlA8WbbXuTDl4uTMJ35SfngLe0pXUTcBrKm-LgFHHE4skO1AyPnIAc-yKtLMoF5lH5YqaLZF3VMuEQCe3_kgKFXM91w-EeHMUb8b3Nz8w3fPk4uXqiKjUIYj3z6oA0Mu2kaI3AtKcvRXUOoV1iGPv5dusp_Eyh2riVlN-5JQedosdzBfavSx27kB8C5tdW3c77p4_Wv3qQXhfmXoCe2CvNYxiZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruS0srm9o8yB_PniWhMBm0gRNUvhpwE47GXObZncUbUmSmPzE5gBEP5Gn1LiiX1FLGPlq7UcUDVYcL6L2RhE4Ho4jl5DG2Ra-1U3v3xMkZkk42wuqfz91PhA-E0NBFW_Kk74168TAZ3OACgzuQ0bJG0GTtM9js8KzHFooI4Rg2GFp0n4bxohqJg29xOxMxY9fBX8TQQvJCFGTAGKxTz2xjKYYBSfYFCRIWVvU849e_43s4qyTE8zKbXDDiElhCxr5-FJ9g8_gCkcKnX7kwHSkW8kv7TQ2_sOxNHg5kZn1gl6erAYYQ1naaTdt725OI7y9yjVeGIyb9VplBW0OpKYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NybKXU4kg-8rep4TgR4MD-u0ASz4GzaWJ26juyl_kWoSUqEzANPpetTC9yely0SDfliSVal3-r5SmGOP3bk_PLOcOUk5F1k1DW-OLTUeFydwUIGOgs7CEiy2VGnEPYbTtfyON3VGIzbXQiNl0fyiLw9slhFaQIXyyLe-4RVbz1QGSBx4oEKMjkfmfMsfw6QOrm27ySuQ8RzeZfREMb9OuX6KKUdqtcXWzwk1KP05gPwkPru2SnjC8sOtrrCn_JitWEeD0wWRdXRmae2GLzim7XYa3vO3MPqJBASBW4v20O_ElCTQAi4s7FdDvIbuOZhcP2epNv1kmJkT_9FL2GsjfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس بگو چرا کلمبیا صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96633" target="_blank">📅 14:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6330122b85.mp4?token=U78NYvdWSBJnvXV8YcADaj9Oz3x9VfGqrZS_Sjm3qBH7a5Gwx6AL0tbP-WvWqilkOo3r8VcwcwrEOGqGS8gaiopQxkOz3BExbQBX73KMr_oU-yJ5pbpHLZhFTkJ_iswmGUEEsJxCm7SKFiJGTTOHp5Wrar93uWNgWhlyno6cAlgHL6ZtQ7NDGzzrTGqnqXJWAUjnDRndM9jrl5Toaht1bzUArE1jTnLGjREbeaWr4SCPw1mMWeApF-hqmxXhWWK5PpmeooldAvGZkXOiICFZZ_ACXI6ansK9lhHkkElQlduob-WLFUMxvE-T3VIk6Yyg9knCdRDz3MDg7mbtSoduMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6330122b85.mp4?token=U78NYvdWSBJnvXV8YcADaj9Oz3x9VfGqrZS_Sjm3qBH7a5Gwx6AL0tbP-WvWqilkOo3r8VcwcwrEOGqGS8gaiopQxkOz3BExbQBX73KMr_oU-yJ5pbpHLZhFTkJ_iswmGUEEsJxCm7SKFiJGTTOHp5Wrar93uWNgWhlyno6cAlgHL6ZtQ7NDGzzrTGqnqXJWAUjnDRndM9jrl5Toaht1bzUArE1jTnLGjREbeaWr4SCPw1mMWeApF-hqmxXhWWK5PpmeooldAvGZkXOiICFZZ_ACXI6ansK9lhHkkElQlduob-WLFUMxvE-T3VIk6Yyg9knCdRDz3MDg7mbtSoduMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
وقتی کله‌سحر تو ایران فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96632" target="_blank">📅 14:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=WyQv9XgMpZQCd71SJyPmN-Ptk-giqNZJTl3-6QPkhRBALJYYytjSEpjyUi1TH5nqccN4thoLe9L74qLK56ep3HCcgdyRKdWOUAqw3DxirhtmkmkjBf14XPFmMchtlzz8o5l9sDFHU0jzEieHuDOg4lh_mo9XNpGpdZowDmmPSNdxRNbrWCm9Ctw7hDttaEQSvsPSiTSlrT0DD4rpf3XZXEB2IQ2tvlNSMJH2yff3jt884FRlmjIcF9rV-lWgpoWdYPxaXIS9ESERBHMFcDTDcwn-bTfoijhO15VT7nr8-1A3GrjvmZ8bieuNCQTxGdbyZrbqeNGee2bFalqgSZ_XIIqC9O8QuElyT6IEKlasZf267n_sDJeKHnmxHlLvsk0p3Pdj35FCjUYfDZ9lbH5qYxwSw1lCDsbS_b4MW-X1HF-xwdNLZLdFNJX4LyTb2n5SmW6jx0uXgnWzQh-81Z-NzE0tnHjeFrUY3RMMp5i7kXVNKd6PZrmbe95gGYkShpByHoCRBA2TiKJBqECblVMRtTfx1MLdrI36FxML6a1y8Lhf3xlEYi4mFVtWP_xzhQSneTF6AS_GgGD0ruN8LTLubhABNTPBFdV3tQ7cfUARsr_BvZ-iqhIEacqE7TWzjjlLzAB3_ihp9JjrphMc0AWmcUCupEn_RNm8tHSN63Z1KWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=WyQv9XgMpZQCd71SJyPmN-Ptk-giqNZJTl3-6QPkhRBALJYYytjSEpjyUi1TH5nqccN4thoLe9L74qLK56ep3HCcgdyRKdWOUAqw3DxirhtmkmkjBf14XPFmMchtlzz8o5l9sDFHU0jzEieHuDOg4lh_mo9XNpGpdZowDmmPSNdxRNbrWCm9Ctw7hDttaEQSvsPSiTSlrT0DD4rpf3XZXEB2IQ2tvlNSMJH2yff3jt884FRlmjIcF9rV-lWgpoWdYPxaXIS9ESERBHMFcDTDcwn-bTfoijhO15VT7nr8-1A3GrjvmZ8bieuNCQTxGdbyZrbqeNGee2bFalqgSZ_XIIqC9O8QuElyT6IEKlasZf267n_sDJeKHnmxHlLvsk0p3Pdj35FCjUYfDZ9lbH5qYxwSw1lCDsbS_b4MW-X1HF-xwdNLZLdFNJX4LyTb2n5SmW6jx0uXgnWzQh-81Z-NzE0tnHjeFrUY3RMMp5i7kXVNKd6PZrmbe95gGYkShpByHoCRBA2TiKJBqECblVMRtTfx1MLdrI36FxML6a1y8Lhf3xlEYi4mFVtWP_xzhQSneTF6AS_GgGD0ruN8LTLubhABNTPBFdV3tQ7cfUARsr_BvZ-iqhIEacqE7TWzjjlLzAB3_ihp9JjrphMc0AWmcUCupEn_RNm8tHSN63Z1KWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
کنایه‌شدید مجتبی پوربخش مجری ورزشی اسبق صداوسیما به افزایش قیمت‌نان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96631" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOd9KRGmY96oYWOpgx-F8DfTo_ouHr1EHlwnKSsfTwPYzdYiw9-zPrdH7iz2YICXk6dmehl1wW-MqpdoT_H2OnVAz5VM7uw1VSHUqCAkMKK7mSD5A-8G-1gaHTqyZDLvDVSHOPijKnSs3ROz1zfPAu8ZmCJtaijXzXKjfffcKJJanGcf9HRDZ0xWIO5Srb_IKdvk6wOnrCVWRq4mIaueJtzhx7SnLLSKziJ7HGg8MfmbMiqOfCrIzOhqhkhVRxlV3i7MMwuorqSbh2pPD0Qk-G6xheiZDZ4URW8yh6uF6jsUFb0FKyQ6LFVyPrsIjzpS4ZUKQnREx5WySA7XgfxQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین گل‌های ثبت شده از ضربات آزاد مستقیم در تاریخ:
۷۸ گل —
🇧🇷
مارسِلینیو کاریوکا
۷۴ گل —
🇧🇷
روبرتو دینامیت
۷۲ گل —
🇦🇷
لیونل مسی
🆕
۷۲ گل —
🇧🇷
جونینیو بیرنامبوکانو
۶۸ گل —
🇧🇷
مارکوس آسونسائو
۶۷ گل —
🇷🇸
سینیشا میهایلوویچ
۶۴ گل —
🇵🇹
کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96630" target="_blank">📅 13:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OgWmP5jaM3V1NhuZcaVgMcFD71p-pWc5POq35dSlUELkNz5qEpW06xBp1-AWGXdfUKM_l4qYf5bl0wBqCHHreTjm_QuhngAUxWCkPhKisDOIvAyle7b9V_bfu1L_Yzb-y81YrEDjNdGSJdfyiU8cpPgEy9rzT5EMUBx72bRUKk0x8lUvPH1FDAsCJ9_jbihhlplvPDmjOVQSY7X4wkzi_O_LRCwEqHVr0gY5P0aBGt8uX1s1Uo9D7QNhXKtryZIweFyqoM5Z8f3fjFCXxgrNyuy_NVxsfnI38AcpOPacTC9g4-caDq9cFrhZ6IXhoB5VskjXZopdGHWfQvnjhGJwbIvGls5fMMW_FuZfrTLG79IVS1SYeTzQNHMhzoVCf_E3lZk2PnhpvpvjaTIyxIxSTDHIMTYL-plwJlBphLMwNJCyb9fIgcFdKxhBxH3Tp3PW2aqbT4sLgt7PPCPzKGWS8OKoQeMASAIL-t827mFF65HryvRJiQ-lpE-7JbAhevzJIrFGAYfQMdmQLMoW5Oa6TyE3veMq53od_AsI-KNlk-Eb0-iOQ398XEreo8G9hssdAYCtWOKD-4hC2MoY8G_F5_Ia81ZEtmAsWErobr07YJfAwhEgLNlCDHl3-fihUwFbYVg0IercbjyS_32dUy4-FZ2v7iWX-D0pKjHt-nIQ0lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OgWmP5jaM3V1NhuZcaVgMcFD71p-pWc5POq35dSlUELkNz5qEpW06xBp1-AWGXdfUKM_l4qYf5bl0wBqCHHreTjm_QuhngAUxWCkPhKisDOIvAyle7b9V_bfu1L_Yzb-y81YrEDjNdGSJdfyiU8cpPgEy9rzT5EMUBx72bRUKk0x8lUvPH1FDAsCJ9_jbihhlplvPDmjOVQSY7X4wkzi_O_LRCwEqHVr0gY5P0aBGt8uX1s1Uo9D7QNhXKtryZIweFyqoM5Z8f3fjFCXxgrNyuy_NVxsfnI38AcpOPacTC9g4-caDq9cFrhZ6IXhoB5VskjXZopdGHWfQvnjhGJwbIvGls5fMMW_FuZfrTLG79IVS1SYeTzQNHMhzoVCf_E3lZk2PnhpvpvjaTIyxIxSTDHIMTYL-plwJlBphLMwNJCyb9fIgcFdKxhBxH3Tp3PW2aqbT4sLgt7PPCPzKGWS8OKoQeMASAIL-t827mFF65HryvRJiQ-lpE-7JbAhevzJIrFGAYfQMdmQLMoW5Oa6TyE3veMq53od_AsI-KNlk-Eb0-iOQ398XEreo8G9hssdAYCtWOKD-4hC2MoY8G_F5_Ia81ZEtmAsWErobr07YJfAwhEgLNlCDHl3-fihUwFbYVg0IercbjyS_32dUy4-FZ2v7iWX-D0pKjHt-nIQ0lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشین قطبی: کارما در زندگی‌وجود دارد
یک دایره ای در زندگی است و هر اتفاقاتی که رخ می دهد بخاطر تصمیم های قبلی در زندگی خودمان است و سرنوشتمان به دست خودمان است. گاهی فردا بیشتر به خودمان فکر می کنیم شاید پنالتی طارمی میتوانست باعث جشن صعود شود و حیف که این بازی را نبردیم.⁩⁩
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96629" target="_blank">📅 13:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=UaCg0u4sbCtzihLN2HaXxuTVJubL-X9a2unwwlS_YbLAF-XqpGaH25NQx8nBYqrQsH77P2GJYWyq4Ah-rlHtYedNt4i3G9HjUAezrkJACoBEfT4jkyWUDSf7mBFeqddZalBzVg5jdA8JF7x8SPEIKPxTX8RqvRG6FANLayHcYVsr73pXzJyugzeNkOL8uai5loPiYGzOmg8J62ZxISwAk1YR5WmzqkbO-3AenY3dED4W79brncjTTokMiG-NO3xvbdhnpJG8UMJbow48PDYrxu6qtJd2aIrpONI7fcU9cwPejRx3SvR59zNDdge4UQeAsl0PAkZPfNIg5npfsKFJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=UaCg0u4sbCtzihLN2HaXxuTVJubL-X9a2unwwlS_YbLAF-XqpGaH25NQx8nBYqrQsH77P2GJYWyq4Ah-rlHtYedNt4i3G9HjUAezrkJACoBEfT4jkyWUDSf7mBFeqddZalBzVg5jdA8JF7x8SPEIKPxTX8RqvRG6FANLayHcYVsr73pXzJyugzeNkOL8uai5loPiYGzOmg8J62ZxISwAk1YR5WmzqkbO-3AenY3dED4W79brncjTTokMiG-NO3xvbdhnpJG8UMJbow48PDYrxu6qtJd2aIrpONI7fcU9cwPejRx3SvR59zNDdge4UQeAsl0PAkZPfNIg5npfsKFJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇪🇬
مصری‌های جذاب بعد از تساوی با ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96628" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=R2vb9FDSmv3r8QWTdnDcPEt5RtBz_ehjHNaiKuwqBGEcLN3z3Vj0HPnh7PPljGkOotYOftMZJc0pssv8KHKkibGoJoa8yeiVTf_CqViPz43tNcEPfncGzpMMnIBVGgYLaS4kbBitt6xSqmOp8mmV6GbNhkrm3m7lguQ7Q0NgiVH69kMgFbTiMDrF2FXW5_hyptBEH7PBUHGCfSOakon_tB-l9zIoqUyDp8Rc4LMhcpil7T-oemtX1z-mHD_MoL8LpSxeAA9fOlMr352Rz4WwKFj7kLHf-h4PD6cgyNqOL6AaFDK2rxMnI1kI0xhol9n4v15PapQdMkGhMnkRl3lFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=R2vb9FDSmv3r8QWTdnDcPEt5RtBz_ehjHNaiKuwqBGEcLN3z3Vj0HPnh7PPljGkOotYOftMZJc0pssv8KHKkibGoJoa8yeiVTf_CqViPz43tNcEPfncGzpMMnIBVGgYLaS4kbBitt6xSqmOp8mmV6GbNhkrm3m7lguQ7Q0NgiVH69kMgFbTiMDrF2FXW5_hyptBEH7PBUHGCfSOakon_tB-l9zIoqUyDp8Rc4LMhcpil7T-oemtX1z-mHD_MoL8LpSxeAA9fOlMr352Rz4WwKFj7kLHf-h4PD6cgyNqOL6AaFDK2rxMnI1kI0xhol9n4v15PapQdMkGhMnkRl3lFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
حمله شدید وحید قلیچ به بازیکنان پرسپولیس بعد از تساوی شکست مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/96627" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1rO4nWOAP_zsnmFqrbyvwyL0aJPumoL2iCR-zbIoBsgqa9wUJ3-PDWYwWDWEzXy0y2CXPC5T0OeCeWg3yF1lE356pLlmiM-modiXEqVjkgu6-hgn-pufR_WbWvCLx1_xAt_bOuuFOp5Apig7o8wWGQSS3B7tRKRIv5t-sMjT-5La16UZkIIE1l_OUQCvfQyqfIxzLpOQuVZp7XWvh33vu6pUppo7FQa9hVjkTsRMGVjwItsMUdQ52T5odSU150rB12SbRpM7GjPwk2yq5EXONMJspUwKWsukfJpHjvK7kj0sLfwXnS7dTqfNlj31u2n5HFMRlGwUkdtpFA546oHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ابرکامپیوتر اوپتا:
فرانسه قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/96626" target="_blank">📅 12:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ4q9Me3yt71Vmj7_FxbjVKVYSUrViBwWB5DQlJ2oRMnBmCZOvgZVx0HEW3LU9iDwc8FFvzfxCL-Pj6p48CIyGBj8Y2s_7M0MtqCpJjwzwHZWAXfIiSYqzeGfYG70M0y9_ijJCT9Qida-lg8ho49w0687OHJa85PoDIR8MfIwfAz_UVP6S7hEMTS4QVKXbcOn-SOpCFlz0mMT49wqkCMwoMOpgUjmG00UaeJyUBMU4YIX_JNDbRaNp29AZcF8g-Y3MwvgCN9FQelfx8DiN63UnFI0G5trmPlr2PlGmN9ff4xipVotmy8GQCnHHwGUET-0aZX3oe3aWaav0B1t6xNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇦🇷
🇦🇷
مسی در مسابقات جام جهانی:
‏تا سن ۳۴ سالگی:
‏
۱۹ بازی
🏟️
‏۶ گل
⚽️
‏بعد از سن ۳۵ سالگی:
‏
۱۰ بازی
🏟️
‏۱۳ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96625" target="_blank">📅 12:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bk_g5iM9jjua4k1NcPBNzHP0YVA0i3VeJs72itwi77SuHJHXasW99LpGfHXQ2opsWz56IJ-p688FI8SRwNTAnv4DQKPOPiA89fVtHAKQDzL3oLdHhI9ayUAV5LpJ-bZvEY0z0qAwRv_nsnw_bNiWEcQN13VTQKXzInvMSGAlVNbbHe5rUNaY6DHxIuOMf-58nl7SI8XZBysdGg4ulM7ICrBHVd7ltzYEOgcqNyf1b4bm87mAlz-DY6R0Y_7bG2eV8pfvGOK_I1qK6JKYbhSB_hYYqqjQSY6CXo8p4u1VMS9L7w07RIyGBedDKFH7IP_A84IDW_r_XKDuoFENnWPQgAe1-eMqZ2exi_RisUDRpEdlNCPpDcbv8Umz5fYHAc-zX8MwRfeU2KSw5WD95f3Uxo8f00aOJdPpY1VrUWQABmYmCm7VTPnetUz2oJk1KVmGPmcrzhABNqt7nOEocKHEUJ7fqpVzBzLzg65yEOdJ_8A-wuwlLLbkIsd3WvgKxvNfeTSX1E9293-EPzMuwBWSwnw-W4V4N31D3TuyNSTKPvbdypzK_3Rl_jklOtLVxuknkCbI0NREslU3aYx1M4u9NNO0ESWHn3AlmJxuwxZmrrgYQTKaJ0200o3bMzSBAOpp5If_ml2Z6irAoklWZSMOLwmjgwNmOyQXELAazUk--VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bk_g5iM9jjua4k1NcPBNzHP0YVA0i3VeJs72itwi77SuHJHXasW99LpGfHXQ2opsWz56IJ-p688FI8SRwNTAnv4DQKPOPiA89fVtHAKQDzL3oLdHhI9ayUAV5LpJ-bZvEY0z0qAwRv_nsnw_bNiWEcQN13VTQKXzInvMSGAlVNbbHe5rUNaY6DHxIuOMf-58nl7SI8XZBysdGg4ulM7ICrBHVd7ltzYEOgcqNyf1b4bm87mAlz-DY6R0Y_7bG2eV8pfvGOK_I1qK6JKYbhSB_hYYqqjQSY6CXo8p4u1VMS9L7w07RIyGBedDKFH7IP_A84IDW_r_XKDuoFENnWPQgAe1-eMqZ2exi_RisUDRpEdlNCPpDcbv8Umz5fYHAc-zX8MwRfeU2KSw5WD95f3Uxo8f00aOJdPpY1VrUWQABmYmCm7VTPnetUz2oJk1KVmGPmcrzhABNqt7nOEocKHEUJ7fqpVzBzLzg65yEOdJ_8A-wuwlLLbkIsd3WvgKxvNfeTSX1E9293-EPzMuwBWSwnw-W4V4N31D3TuyNSTKPvbdypzK_3Rl_jklOtLVxuknkCbI0NREslU3aYx1M4u9NNO0ESWHn3AlmJxuwxZmrrgYQTKaJ0200o3bMzSBAOpp5If_ml2Z6irAoklWZSMOLwmjgwNmOyQXELAazUk--VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
جلو جلو ذوق‌کنی کیرررر میشی(قسمت ۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/96624" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=tZF4Tjis86VABTMwDUqvluKLMvaOn6O7duvrQ5JlNazdHJ5CdIvKb0pR3dlg3AztiwZkyPNWmIwO_YG1iNBrHI5Jo4Tx-P5BCBwNrIilme5vPMXfbZDE5S2vaWshBPIR_CBIxX-4CDsFPw8y39Xc-O9klduvjSsjCxnfwjxxO3RxoJhgYhnFRkbhvguv4obMMmOdOHAW1Da-7lC2JvQ3Y0xn8pbhYs1sXs_lTo5xi4-LnjJlmNfJFeSvPovwmS1vXbcRAIoUqB3lD1jPVIOlIkyKsv_UIqfiXhC0bYfFEFYiYz8RkjqGAMrAChSynblZZ5VlI9a0xP0PjiKsQnrvyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=tZF4Tjis86VABTMwDUqvluKLMvaOn6O7duvrQ5JlNazdHJ5CdIvKb0pR3dlg3AztiwZkyPNWmIwO_YG1iNBrHI5Jo4Tx-P5BCBwNrIilme5vPMXfbZDE5S2vaWshBPIR_CBIxX-4CDsFPw8y39Xc-O9klduvjSsjCxnfwjxxO3RxoJhgYhnFRkbhvguv4obMMmOdOHAW1Da-7lC2JvQ3Y0xn8pbhYs1sXs_lTo5xi4-LnjJlmNfJFeSvPovwmS1vXbcRAIoUqB3lD1jPVIOlIkyKsv_UIqfiXhC0bYfFEFYiYz8RkjqGAMrAChSynblZZ5VlI9a0xP0PjiKsQnrvyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
ایران رکورددار گل مردود در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96623" target="_blank">📅 12:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL3FR9dOyEGRJ9kaebl8bY8zE3C9IVwhZkjHTb0yfUVrCi4dlGkNDwcvdNBkG0i9WOmn4_HqCjkqElIWcgGarrpooB0gEmaa83euEiMyvwksrgTNU2UIBM9GRD0KLgE4EGTDfMDdUWBqOsVBUlS22M-CuKnKph9TbKkAyxgkpMXG1KRJG9rSlBoXqGc83UjezbE9zBKHBn--_Anp-qIOgVJNRO0Kq0Ji1eBehSOTSJ2h_VC5dr7GEBBKvg2Tv8zBWAo8VCnIVsCHc6J2L0lqHCscZvuUme0qOonHrs_kTtBFOJbDyvWfVeTAGTrM8OQziD_q26seWehaD-Y4o2MjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری:
قبلاً گفتم، مسی رکوردها را دنبال نمی کند، رکوردها او را تعقیب می کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/96622" target="_blank">📅 11:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKyuHS1ASZ2K5GfWG81SZscgv27hP0SRZ3Glq60IMPVv8dmpqVnOnnuLwlM-XSxhYAY3maLfcKg_8jxX28RGnCVhKkDusJESiRGq3-4ph4_ZsfWb9bin45_LmLXCj3_t2xNIk_sAeneNbWfO5aHQRMhXvKqMyQIUODPoxikQMn3ayZBAHyZUet7LYAQPII8wu4chOoUNdmchr-IkbsjSFx4dTJr5vyYvMkQeq5I19IOgaPY4Zf3WOnvwvprJgQKqAIcZvRyaZpD8w_Li2Ha_2-pkX2w2vfSPQu9TNYMURTkAOJWSJfyzsxb3RIG0KUuwwD67C7F201qPK9nF6e5q6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
مسیر تیم ملی پرتغال در جام جهانی ۲۰۲۶.
• مرحله یک‌شانزدهم: کرواسی
🇭🇷
.
• مرحله ⅛: اسپانیا
🇪🇸
یا اتریش
🇦🇹
.
• یک‌چهارم نهایی: بلژیک
🇧🇪
یا آمریکا
🇺🇸
یا سنگال
🇸🇳
.
• نیمه نهایی: فرانسه
🇫🇷
یا آلمان
🇩🇪
یا هلند
🇳🇱
یا مراکش
🇲🇦
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96621" target="_blank">📅 11:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2KCaElwpX4x9MGg531PRhBB8OVMnSKC-ZZijwk8TvIglDWZe5i_TzD1PoCCQQvJlykh7F2AFvBwFr_ikeHDbeVGJ86iltsb2oucpIog4R5Xs1nyLYDx0hXhZRiNyRS6o12MG_gD-4YPPy6DQYqNDkXVNusy7AB5W3u7YxCsIgVDn1nY7I0Gef1sOaBRhEvLvK4P0TrHkOL4asroJb3_MI1Kp_hA4aSqMj-PLu9sogyxZo1wDhvf4yduwDukvNKuiH_KwcHk__SoEuDUx37B4EmopbZVp8mT82MUPPIHZSMqmPE1Uug_6c_fud6jbsPNwGYwPZn4VwcapOUKkeaR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
ترامپ: مسی دیدنی است. او تنها بازیکنی است که می‌توانی بگویی بهتر از پله است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96620" target="_blank">📅 11:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957600e824.mp4?token=NnyK_QdAxZB_k-mRktWAa6orzNk1BqmPFI_Mn6vhhSuQNyiQDVghlfE8OGtRvhVLDP0JozbKyhHqbVMYuWiVNs8wdDahMoNfIIsReZ1KXiftrKhUjnU8jaJ5c8xo9vQemQpGWxPa0TWfuajDOZ2_FKkU4LhLIKXs2EaUz68_ViCcmbeNAYcp9Mxsj4XVUGNAO7_Zt15EmP7q70Q6CrBbtDytKV2fU0Xz4lEawYPyWD7_Y-Y-7O06cmkkgRRfYmzx_eTQum6cTXqUsVqx4AQ6R2KnqdBp_DF2ruzd-2NtM5I3ehzN2v-WqJY07MEP2zhh1tsKaC736MOycitV2NxPFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957600e824.mp4?token=NnyK_QdAxZB_k-mRktWAa6orzNk1BqmPFI_Mn6vhhSuQNyiQDVghlfE8OGtRvhVLDP0JozbKyhHqbVMYuWiVNs8wdDahMoNfIIsReZ1KXiftrKhUjnU8jaJ5c8xo9vQemQpGWxPa0TWfuajDOZ2_FKkU4LhLIKXs2EaUz68_ViCcmbeNAYcp9Mxsj4XVUGNAO7_Zt15EmP7q70Q6CrBbtDytKV2fU0Xz4lEawYPyWD7_Y-Y-7O06cmkkgRRfYmzx_eTQum6cTXqUsVqx4AQ6R2KnqdBp_DF2ruzd-2NtM5I3ehzN2v-WqJY07MEP2zhh1tsKaC736MOycitV2NxPFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مصاحبه چندماه پیش استاد مهدی‌طارمی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96619" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29e12c0b7.mp4?token=vYrNo8-AswufMliw0vJeIOvon6S3VSJAkcgUEaVo_ODsDQVFkH9O_dxYBGWw9beh0jyuOzrlcwD-ATUIXt9PTtpVgtY4aETzb2S6W_xq_U3ckazks2OpIDNZMpHrOO_sRGzxMtlqfAGY6_muc37KDj2q97neWO5K3BEXryxEzdmQUGbT_5CJ-3ckVP4SjzqbYi3kAojD8fICp32PSTqxmC6CYpUTi2v9hyvLAyXEM07kPV0hB-Tyc5GfBgPpa1bCNvt39DYj6Z-E2gYgwYFGu-MrrKv9nWsLaPziTilSDqVG5AEeNW-Nkw7LPIe8g0BJrqSg5_rVulbsfbpT_Qu8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29e12c0b7.mp4?token=vYrNo8-AswufMliw0vJeIOvon6S3VSJAkcgUEaVo_ODsDQVFkH9O_dxYBGWw9beh0jyuOzrlcwD-ATUIXt9PTtpVgtY4aETzb2S6W_xq_U3ckazks2OpIDNZMpHrOO_sRGzxMtlqfAGY6_muc37KDj2q97neWO5K3BEXryxEzdmQUGbT_5CJ-3ckVP4SjzqbYi3kAojD8fICp32PSTqxmC6CYpUTi2v9hyvLAyXEM07kPV0hB-Tyc5GfBgPpa1bCNvt39DYj6Z-E2gYgwYFGu-MrrKv9nWsLaPziTilSDqVG5AEeNW-Nkw7LPIe8g0BJrqSg5_rVulbsfbpT_Qu8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تصاویر جنجالی در حاشیه بازی ایران و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/96618" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‼️
درگیری شدید هواداران ایرانی بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/96617" target="_blank">📅 11:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🥲
🥲
شادی‌ عجیب اعضای تیم‌منتخب ایران در هتل تیخوانا پس از گل سوم الجزایر به اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/96616" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt2XTfEM6tJ9wc8Oy3vQmdtctvfWENo11ZmQnXuD0hMqiWWSI09ffyU1FJ_b5PRtgxSijJqQeZc5V-0bsGkvZe0_f-bz1hz-MLWRDhPlDk6FzGOXE1jdAduD7tnhFmTXzN4WkMrwFEmDpkIbN7LMZVDcfwOx4_oDfmLnlRph8IVqmRoy_ONhkrIZTw12s7_JcgBD7fy0lTT5iHW97Yocoz01_o4KFQs0qWrTyrhBdvj-VdiECR7nrlmJ0DKdrKCuMvaiMosIOCK5gvinHwGv34cgatWU9vjNJsY68aBsLgV0R1y-Y73BuaMsm9lotkW-pzdb434C_KrbnyKHIkyQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇦🇷
اسکالونی سرمربی آرژانتین
:
🗣️
لیونل‌مسی امروز با من صحبت کرد و گفت میخواد نیمکت‌بشینه تا فرصت بازی به سایر نفرات برسه. این نشون دهنده شخصیت بزرگ این بازیکنه درحالی که میتونست به رکوردشکنی خودش ادامه بده اما تیم رو به خودش ترجیح داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96615" target="_blank">📅 10:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a4bb6889.mp4?token=Rp14jKrCLkjHT7VEiJdrH56INK2eF4is9D9CkSrBoJpBlosZJObVk2oXgYp-PIH_x20OOZRNStIqBAU_bkeLx8TxbuX5t8THeCVSsjfoeXmC3UTnjQ1TziVUpT_wYNnwANoHON75dvsMHPH7acEQLJ9FePi1pDO6bdR2qooH9j9eZlPufSVP_Fx2LScVOqZ1SFjle2IIqDQV_6WrIxd0id7-C51xXlTSQz7jYhpxyLDimYbJzSWOsGP6-CN43b1vo2vMyFP9BJdNBHcfinH3tXeZm1fvY7Y6L0DzjoVkqRAOEnOTHadv_ck4JX9PcNxuEPy6ZbWPqHn9AxyZu9yKA1h_6JPEL7IlqVXF0ehqfFvEDh6SDpY8EwGq9YFS3cePDoiueNum_iajth_rIRmUKU5yeXFI-QbmxIlB82GgC3iIzAqM93NQue-uRaACR660abl9QR7mRdWEL8XkodnmWEA4WBfbCJNGj3cHaJKVB2MW0IIj372fgU9mif9pXbquW7eyGFcJUgNUTwH2PVlLGeFORB7fLelBGtgv7S0RocKtfKlRE6wwo6s0UDZZQWpTJ4xpuX3l0ZRcxwblVgTGtaIKwwJjzevSMsRPOgDuTtZo1so9PZ2OUGpHDuKLo5ZQurxkW9U1UeZNbZLmmKzONa42Np_IFIeWeRFucde_0YM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a4bb6889.mp4?token=Rp14jKrCLkjHT7VEiJdrH56INK2eF4is9D9CkSrBoJpBlosZJObVk2oXgYp-PIH_x20OOZRNStIqBAU_bkeLx8TxbuX5t8THeCVSsjfoeXmC3UTnjQ1TziVUpT_wYNnwANoHON75dvsMHPH7acEQLJ9FePi1pDO6bdR2qooH9j9eZlPufSVP_Fx2LScVOqZ1SFjle2IIqDQV_6WrIxd0id7-C51xXlTSQz7jYhpxyLDimYbJzSWOsGP6-CN43b1vo2vMyFP9BJdNBHcfinH3tXeZm1fvY7Y6L0DzjoVkqRAOEnOTHadv_ck4JX9PcNxuEPy6ZbWPqHn9AxyZu9yKA1h_6JPEL7IlqVXF0ehqfFvEDh6SDpY8EwGq9YFS3cePDoiueNum_iajth_rIRmUKU5yeXFI-QbmxIlB82GgC3iIzAqM93NQue-uRaACR660abl9QR7mRdWEL8XkodnmWEA4WBfbCJNGj3cHaJKVB2MW0IIj372fgU9mif9pXbquW7eyGFcJUgNUTwH2PVlLGeFORB7fLelBGtgv7S0RocKtfKlRE6wwo6s0UDZZQWpTJ4xpuX3l0ZRcxwblVgTGtaIKwwJjzevSMsRPOgDuTtZo1so9PZ2OUGpHDuKLo5ZQurxkW9U1UeZNbZLmmKzONa42Np_IFIeWeRFucde_0YM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
این 3 دقیقه هم ببینید جالبه؛ گزارشگر داشت بعد گل سوم الجزایر خودشو پاره میکرد که یک کشور مسلمان به داد یک کشور مسلمان دیگه رسید. به دقیقه نکشید بعدش الجزایر گل مساوی رو خورد.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/96614" target="_blank">📅 10:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949f56bccd.mp4?token=sPhwVxrwGKJ14kxWEaMHNK6RDUiiQvJCV8BPGoU6qNy0I7naf8XCulUm4OJWjLwWuBao10czZSHuFDyYPHzfXEO5WiuXe6R4S-OpZTRPFYat__yNfBo5SLaY0gAKuFZ0gyEBa8JL_tyfHL7x8cstD4L4OI1Eodjff54w16NDPXz6LyRpSUw1VSJpjJkGx9Kp0LyWuq6h1X7SxogqiFWFhRPDL3_nUk-4qZIKMAMm-qNw94XlumqcrnrUzXVazWJ51eSp_MOAO3EvfZh6vvz2yOE_4RrNGhcV4nmMDgKMrJv1pusGAr4bkt8RmDVFH_I4IqyA0e5DmfpsfeX5unxOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949f56bccd.mp4?token=sPhwVxrwGKJ14kxWEaMHNK6RDUiiQvJCV8BPGoU6qNy0I7naf8XCulUm4OJWjLwWuBao10czZSHuFDyYPHzfXEO5WiuXe6R4S-OpZTRPFYat__yNfBo5SLaY0gAKuFZ0gyEBa8JL_tyfHL7x8cstD4L4OI1Eodjff54w16NDPXz6LyRpSUw1VSJpjJkGx9Kp0LyWuq6h1X7SxogqiFWFhRPDL3_nUk-4qZIKMAMm-qNw94XlumqcrnrUzXVazWJ51eSp_MOAO3EvfZh6vvz2yOE_4RrNGhcV4nmMDgKMrJv1pusGAr4bkt8RmDVFH_I4IqyA0e5DmfpsfeX5unxOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
آقای‌طارمی حقیقتا خاک‌تو سرت
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96613" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFZOYUMo_h8KnyzoT6eVDsHy5QFaUYKzRbWVtam54b2Yh8J3O2sVZW0mo5QmorsAKLTXlLjBDULMj1Jo50JUCI7krCXAzBImiwpNGo9UVzj6srWkmpXKubId6arN0QlRgo9jrOLUCb6niaAuT3kGgJ4AB7SP2M8qTFbNZu3RFJz20dYGkEeuARAXWMVQQ6lv4GV2TobbvuYRf-GGcZ2IPAXnSMQxqKVfi8peNEzQHmNL7pO9UySMeX40aUkzllB6uaWhy0oD87R1TNoqqBWxEbJBkxsuWg1CVzLtopocvho6AjHoq6jDVo-SWCZU4UJUae_mKHulR2MVRZDlNb6FoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rcAOPSz0_ct4MSt-Sqc0mkPsWaaFs6KCO0MRuRXJwlmQduIDIUGbd6IH83uOzUi1E96k4TjTz7sKtC30zdO8ChAQkfQUSoLzf28kmFUDmMJl2y4ReOzZSavDuI7AbiyloIo_Xfy0tcx5lr-Zl2BxPUtm60M1fuiTtI-rkwgtECr_OlnGOkSrjaBja0w-0yZsTUbFsZhqwHRNzrOzdTzaq-iipTulXXnLW3LnO49c5n-3tF2ngnMTuSfDYWcb-R9KX1Z0ofW0bLSDXVbRQ872MOY5ESlKiAg-PG630ASMQA8M5AK_Ig3az0kvLKYaHIcPddbmq1lObc5rsdKMmsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdDeRHU_KiG3NkaZDvesO_gl3KNl20jUhxmTMUcquEZ_Tl8JIjcEHmo78vzjgV8rTWoW9mh5ZDIQt-tYJ0q7DHbjNnJpSR23dS1d3lCn2_gC4CsLgFOHH7O70OkKqf7rjA5647WNEkQmnJwAasDrRpz3U8xpco5I6Tm-RgQWNb7IUySBbBfEIT4_A-Cb3kvwreOuslSlosLHg7iubjzcoUBwX9X-9EDANcPqoIlm7NUnI2--iXFBy1Bsuaj8b2Yy0j00PZcJ0tNh-CRZhEl_Zt_3jj0ZtWFRsQE8KQfZYsNrZBPlUDRcwljLuRBOZeOv0dd9vVYKomR5TlaAV5G3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2GWQw10QGZnEsjfdwnVrHJvt-jqKKh6CNLtX5tcCr0kuveLaW8fB-XD7KhbycZboqOs70wYgLqqEsfC7GwMv10KjrWk205-W_leZh29hvJF5qKI6qqjAL8Ea9vOyp3zTLNhGcb109aeVQzMwIkG-drlodBh69OGFTbUqBSzfJWS3UBG9ap2BYQguwJ-wwiqpCyeCh337Pio3k0iuXpvPk2ON6DlGbwLO9Sw7R9lXWZxZnx8YkdPUoXaWF-sFBilj2_twKk7VaDdcBdo-DC7fQENIR8RZ1nMmeKLLnCpjzfzSTL0_4hnoNnppcsG_veNBsPi6L5sqoDPWWvMyybAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM3MlzlVxaRvaVh9oi1Bv1iCB5CalGbw-okOqvg1ldkLbcAwXf-1FHCOl1bEogAIBFhqJgP63lufX5JcligMUUQUPEo7gh7-KhRDoPqvyqoIgq9t0ySJK3WQhXJIbF4bfGKD6ek21wEfz4McLUwKBMD6wS3usKrTQ4pbtvCOhIdCTUjz0bunQsCtgl4SzldujLEPUFiNKJKB1w1VXOoZQAXu0QrUVw6Pby-h1YaRbhSbaXHMdeeZJT8KeVw5F9j_PewroOZGgeGRJc00uFMtpX8Xtak58y7XnBjq7eBOqOcsMke1V_RaYC--lBILgoSLn0GQiLBT6s7-VuHRxFdBFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇵🇹
دوست‌دختر زیبای آقای ژوائو نوس تو بازی بامداد امروز کلمبیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/96608" target="_blank">📅 09:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afef79198.mp4?token=Dqi7znXa60CRjp446pBcdJwRDYN7NO0mEF_Hd9cLzJIB5eTsrm8dmRyZG1gegt80CE8d2q2C5-iphroHcYzNI7jqRIGa7Esm4z0jy3XOrAFAeX25TvvpYbaliLKwkq9PL6LuAZKwO0Sz6-xNHlrucKdMQBG5DTABpHrzQHcK10UOW-EpN4_DCkp7zaDxFkuAS3wQdNbTitrIDuOJdEBh2a-nUVZQo4AlFKFQqrNlTQXsAzONeldbKCZy0A4I6JLIN8Dl980PJhKFz83xFcP2RSlzGEfA90OvMrR0n9XGDoFb8-cVI8-uJhD17-EN4bTxqFr4BSDMSN2RA0H8ketMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afef79198.mp4?token=Dqi7znXa60CRjp446pBcdJwRDYN7NO0mEF_Hd9cLzJIB5eTsrm8dmRyZG1gegt80CE8d2q2C5-iphroHcYzNI7jqRIGa7Esm4z0jy3XOrAFAeX25TvvpYbaliLKwkq9PL6LuAZKwO0Sz6-xNHlrucKdMQBG5DTABpHrzQHcK10UOW-EpN4_DCkp7zaDxFkuAS3wQdNbTitrIDuOJdEBh2a-nUVZQo4AlFKFQqrNlTQXsAzONeldbKCZy0A4I6JLIN8Dl980PJhKFz83xFcP2RSlzGEfA90OvMrR0n9XGDoFb8-cVI8-uJhD17-EN4bTxqFr4BSDMSN2RA0H8ketMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اثرات نبردن بازی با مصر که کله صبح باعث شده مردم اعصابشون کیری بشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96607" target="_blank">📅 09:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4378d23f3.mp4?token=Po-zYqFkVswBelMrp8QkS4MD6Sp2wjeDPbGRTIqMaMWRhbQZAEtgFamUWfiucsBeO2cVEtUqlQLnTOsJaC6NwEO0zwhbIHayT_2SrlEZTnUnogEs1gH58ug1WRRiKEHppDI58nkvUcqJ2___IuUJJOiHQO4Gu_kKoEaLgwbuJL942cDPYe3fhYJNgvTGT3HhpFKals2-xUMfF_hvrTcZG5eBijnEI9mpJAtlw90ibEHUaKmI8m4b6kM9w67wuPwgtGLnNj5GI6x1tJtOY48LL_rTx2UZMcrB_4Du8rMz4oXOeJtbIvYF0JGNbb6Htn-2FsZFK_Ccl4p7ehO1zaJJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4378d23f3.mp4?token=Po-zYqFkVswBelMrp8QkS4MD6Sp2wjeDPbGRTIqMaMWRhbQZAEtgFamUWfiucsBeO2cVEtUqlQLnTOsJaC6NwEO0zwhbIHayT_2SrlEZTnUnogEs1gH58ug1WRRiKEHppDI58nkvUcqJ2___IuUJJOiHQO4Gu_kKoEaLgwbuJL942cDPYe3fhYJNgvTGT3HhpFKals2-xUMfF_hvrTcZG5eBijnEI9mpJAtlw90ibEHUaKmI8m4b6kM9w67wuPwgtGLnNj5GI6x1tJtOY48LL_rTx2UZMcrB_4Du8rMz4oXOeJtbIvYF0JGNbb6Htn-2FsZFK_Ccl4p7ehO1zaJJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
هوادار ایرانی ساکن آمریکا بعد بازی مصر خطاب به امیر قلعه‌نویی و بازیکناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96606" target="_blank">📅 09:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XmOOvH_kab3F_2Ce5wibqLcpWQULajPgUe46D6HYlY0TXm9U7LoHwErkC3huEVlt9OIJNHj9jFPfC7zEOeS_8G88G3VKqTAt4LPWuqHXJf8LuWLxQFV2jaM-35hI6NmzBU5RzuoiVaFawYAUtJb7P4PUERLqXJeJS8q3XAuZoMV8Ah3ElLivWiJ7Vw2ehY6NTH4lo695ntlaAPZOV5Cnvk1Ki8nvy4LfquvgEv9LJF_LSkoG3gKZc4buIOnl47nMFyyO5eYA2OgFnhcOjdEQednG9uhtGXUhXgFX6ryPJ294RT_414R51dizzTiSF3yhVwpGBNeQBXbIMMqLsfyWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bUScTUoVpSbDezrybew5rmnYobu-7KME77OxmdTsp1F0vKwJJNhw8S368ekmHKktZhvwBXM2GAEvm8zws0hlHIy4NphFnKUqDW_Wi4zYiFovlDoy_c39AVj2fSQRJPnYDw_jNtTdBgajaDBVTnUk6tLhQeDn5MSgACO4K4Lgq2kL1s3Ym1EbZDodOZwWnypy-IIAwSyeAQDZ5nsq19MPB0rZxQJ8v_OCD3U3s_nC836h9ZL8dyqVmgVU5M9epc0zXAifztuw18ENK1oVejnS5_H8p7uu8Lu4PtpgyBCXQwMmMPsOgLMY9LVVDLoiKU-VvOsFRcD9ROmCjKhSBRT94w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
📊
آمار از سایت StatMuse:
۷ بازی پیاپی با گلزنی در جام جهانی
😮‍💨
🇦🇷
🆚
۷ بازی پیاپی بدون دریبل موفق در جام جهانی
🧐
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96604" target="_blank">📅 08:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
😛
😛
میثاقی: بازیکنان الجزایر‌ و اتریش به شکل آشکاری درحال تبانی‌کردن بودند اما نمی‌توانیم به جایی شکایت یا اثبات کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/Futball180TV/96602" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8kWqroMHQ-FQWcEeEwQ0fwpgMeYDO652ZvgvL_db9TnphD6vi_5rwFoIfjQcNatiUiWy3zAU9LygRm9rathKazjSivaxt-Q4h22KBuxuJmPHVr7dUE0Txllyc63BUiQvBTNJMOHOWO7KF32ZjuW36d1CntdKlI3eW3uF9JYIlu_czNj4-SFQcqajxtkFWdKJTSyk0YITiP3-82N0X8LrKKtP9ejRBrBgFDU6rqvsrTeEguASvKZSsZdLWnPy46XncHMzDXSCPLWh36gr2KxpfG02Ph2t7yMdE-Z5XZZ_zMDxNWgIBEyqlH1K6MBglPnZ2yKsv-i5Z69wqxK1lHdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏆
جدول بهترین گلزنان جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/96601" target="_blank">📅 07:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWjT_vikeMvgwmSCG324Y3Kgqy6FyrjB5ICJKnGpiaYF1r2SRB2T5nE_sCPDxSh4TeJMeLWM_63rtCfqyslbYRlE0pb0d5-xyjoabVPzr8IDJRGA-jqUdeNnPBdO3bVqOvO57Jw2I5mGcH3BdBifQmH_FkMba2J_tfBfAN0SJeB_BRLoaZUkCswON6JXJ4danQs4XGRYCgmh-WG8e-f8_RwmKakKZq65y_LT73LZenyZsusvYuNdW3PYE9SC59rDATtnPVSi8sCQBJHZHMp8UbGg7jMDauzkCOv7_RCXBn2cU-RyBBK2EqSUqShxQ5aq16vTCDcfocfAeTVtIPzccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج تیم ملی مصر به شجاع
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96600" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjtUeprLKcE_tdNUQ_K_tWp0BArpwx3BLHV3X7yw-IHLMCMRo06Vg1aeBwPC_Ux-SKLwF5ajmAq8AP2WDwc3uUwI4RyPzAhadNWSd-RtYao6FbnhaCtk-Mae_-AUv6oDTYtwZL6ZoHkeIXfUVQvbif9tpzO87iDYWpGe3z3VOlONU358DwZAnK8NwpdqTF8LzGqxywrXwuMGCGcyylM2-7viZGGHaK-tA2ZisdWGhojReg08v_qiZthc0Hi6xwc7QDkCAyx6Rqo3owEigf8uLdQm9JOm_ohjLzgGcIyn6MZC0NFyqatxwwytNznS_-0DMlnGGWbJzMl9WqUehaoatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی تبدیل به سومین تعویضی تاریخ جام جهانی شد که از روی ضربه ایستگاهی گل میزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/Futball180TV/96599" target="_blank">📅 07:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXeKHqWsGmMLeKU7wtagOkXBiCJZjznS9Zpmw6uUs7ZD8vbARI3y2IzjwgU1WkAn3bCmP3HNPhdvE9sGvC2Xv_fF8R6OC0cNuoUSSA34zBGr0cekg6w1e9g-Yv3TKcypqLYuAGCLN0ielAPUsoQe2pC2y2e_Wt2p3T6BJfY350KPMiHtYsmCDmTLd2YFH0JLh0eDSDOZ_fvJ7_O-nRLIn7fp7Fjz7bO1FywFDkSsu9z95BuLkbQ0P7e0t5SWTWPs23YUoprFHsEoJErqPP852NKM2tg2bfOQ0yydTdfJ-w58GtDMGAajZBb2pC1eroqpjcec6INKKACmiciZvif8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مسی در ۱۰ بازی آخرش در جام جهانی
🐐
🏟️
— ۱۰ بازی
؛
۱۳ گل
؛
۳ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/96598" target="_blank">📅 07:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/96596" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTPm4KVxjbJLfKTLE-m7qYABWXToHF5n472dm6WXve03gtydC8v4ZXuJYhY2gT4wAxquEkjc708hN3KID64oNH7OUiVgCTjGnTdlTgPTWB2Q9COSu0EOmW4DhjAUTQ-qClsd4vJfgrVVtDP7XJipB-cvbY5zhiUwK4yYnUjcYDq2Ia5Hs0M0I3wToQOKh-SJ0GdFsP3AWCmLerKzy1IvNnTB4kX7lSwg5GH3xGAhrGz3Kqk2MML7DqH5g9siUHMlBRgOh3Md_RdILEDgvWbFrxTks1KIsE3ExItwkW-icqJySdks7wGFG0V51x-E0ybB_NORs0at_KBmxpcRZD8big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96595" target="_blank">📅 07:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
ایران رسما از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96594" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قشنگ قلعه رو سکته دادن</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96593" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پشمام عجب بازی ای شد</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/96592" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتریش مساوی رو زددد</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/96591" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96590" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چه دقیقه ای زد</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/Futball180TV/96589" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پشمام الجزایر سومی رو زددد</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/96588" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96586">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EgKzbpfzvt4NPFL4Q2mfA6hvmTSBGbQdJR2_uhphL3_pGspL-iQIrREA5NyA4uo8_rz9OOvb8vmvaYifGTQ6tyy9Huac0LR4-qfjo4mC5eqHGNXF6t8CvZSgMTqF4Nrc4WX0iwFJUFq3Csq9dRMpUU8gi8D6dcyLMEhNrysmnbigIk33pDnora7u-8n4SCMrWSDTibV_ubbWnOv-jrQW3BgeU-6wzBYdhQNJNOGaWxLd0nl8JNtqFvGa4nHHmIU7yxAX10f3iHIqEaHG3DUE4q01j12CXX8fA7-uM-EVKtX2U-YMPUTQRkhHuYdEuNr81emxsVlJ1bsQcCC6Ynnj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HFKjhkUaSudenRFKqusI11lYA2A7E_tElRLa7DE89K1QgHpc4boQAU5szIyXnIGuhTgaVx2SsMUpmEDkUi8WAh7YxQXoNXHvKzVNK5Np8ozDidyu1_GNnk86QolrjNDwwqLIECSN0MgZr_UM1fcbftB_set28XgT01h_SXp_4lavPjs7rgm5YYFTJVbKDfZ--heQ9Gnr9-a9egKFAt2glgfYs2Ijce1__6yhmwa2_QnISqkg-rGkRRVSiO7amnHW00O6_h7x6gVxCPlZLj0CtBm4diDF7ZA4CfqczumxDB2IDv2p0oKQr3bcgtu6euO1fACFqs0SpfIYJpxRcoJ3Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی مسی و بانو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/96586" target="_blank">📅 07:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHezYqdEY11DmNJJLGCWz-ppwp1qpzbvCypS1Tr9XHN-ur7sv5LlqvMaGoAmTtrreydUA7nqDrvi14ClNRhRB1uFxDEMS9UD9LQKz3MNlAB5WM1hnvjGv0lO_CqGiZ8JcCoqcK56VYHW5BJgcVGgLzkeOmpiQpFGiz-X280zlQSTiJTRPHosLWelkaRKCYK71gMNnaiPHHVKyxnAlhcu4QLg9ZlOYVZpkgorkZD5MugGX8iocsYABbVhiD2SFzIqW08Rj8srx9mxaMQaU13j6xYVfui2CadwUQocruKa4RGnVI1QScSETqZgTU5Io2NsaAZa5a_aai9TryIkVuGh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
1331 GOAL & ASSIST
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/96585" target="_blank">📅 07:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96584">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=LxjRpFZPW7WHp9563XTnzp-MDIZqsdU5lZ-DRkACeHmnv5crbHmUJ0mIlUBTnIFvZcyUMCnhLrOao8GdoUIAj-Svf8AlFYqEQtqB1ujIFPnJcTjLWnVFLgv-x_B0V6q0KdBGZpOswdlpy5OxcFJjHCVKw2O3pUDCfBJUraktAeYe8xROMOmQCXq6_uyD6rwnXhJs0L5AlnuWOoWpq6mdq3935q0l8myHwVNljUbepYrG7iB_Fs2IIkoJxnWZULGXQk4uBJFtCSHnaBg60rAzEhangyeozjI3ktQbZqXVmu4vvzHWt_4OZYBl-6c2pre_cu4MV2K6xnSych550YOSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=LxjRpFZPW7WHp9563XTnzp-MDIZqsdU5lZ-DRkACeHmnv5crbHmUJ0mIlUBTnIFvZcyUMCnhLrOao8GdoUIAj-Svf8AlFYqEQtqB1ujIFPnJcTjLWnVFLgv-x_B0V6q0KdBGZpOswdlpy5OxcFJjHCVKw2O3pUDCfBJUraktAeYe8xROMOmQCXq6_uyD6rwnXhJs0L5AlnuWOoWpq6mdq3935q0l8myHwVNljUbepYrG7iB_Fs2IIkoJxnWZULGXQk4uBJFtCSHnaBg60rAzEhangyeozjI3ktQbZqXVmu4vvzHWt_4OZYBl-6c2pre_cu4MV2K6xnSych550YOSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل لیونل‌مسی از نمای تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/96584" target="_blank">📅 07:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96583">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udv7rfXWdlWEh9ojT8tS3MxCfrDA6llhwai28FPVecKH3SZp6q9GOMYbwjuyE2lwuq1CtWxe3pxUEyeyCghhZRF79J1HLzOXXAWTsKjfDpThX6eBvidJdWwn9-cn-sx5VHKyOyAyFNnlqUeABH-Lsi4pzs7QdmK00TUM4MWXTt3NMGp3aDN3QW4e9UCkUFst808iZQ7vXUfWjQuaXLHomqz8zp7FjRjQNFrfSDS3hb4pendKnzpXajUgLJ56Z0ydVISog-M4LcJ0VctlNCcqDxaXeX9wVIQt9ra1YH8tQRItkTus6CM4zt6IRyVx0uvJ7xp8ONQbP3KvsrJe1dgwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل مسی به اولین بازیکن تاریخ جام جهانی تبدیل شد که در هفت بازی متوالی گلزنی می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96583" target="_blank">📅 07:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96582">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=UQpRCpGhUtEjeLU-B3UqW7liSD4LnuNhn62DddT9rWBYhbSTAg4ZBohXgbbakY2MqXjlOyXuzdJyENncQT5KoH3nPWUyM0bx0YFSLw3hZ9nI8BXzW0JaAt6ywj-g80rKzw7-DGSUXUzDjB9GubF4jwK1dM75iSU9xVW7BUgs-RUo-_FmbAPTuPHd1ZIeg269wsiTIHTKV4bm0y2tlPqkBi6p1_afWqwflGwqMG03l4Wmh3Vr_XGlVOQ4gt6O5Nt71Uvw5tADNRhIKw045vvG4tTDXBaRYzBQTrGtRxgIFiy7lueYbnlK6573yoX1WY_AvG-X1CCikDwl0rPde7IEDqdzBuzKBM5k9uuAuRlim7UWc2hFHD-_QEm72J_-IrHBJayF_TghQadq4wdbJbIbaTL1Dq882cY610ayuHpwJCerDUa0npYNXv0X2QXPvfgFd2RoEEqquakhHR1rwCGLZQ80uZRYxq9_hJe7sdAhzck8qcZuOwF_WuIpqjRz3UQooR9YYXk9rvVw6sU3UcJDzwr3BKjYOceeDiLT2BIiu4YV9kNPXnyuQ807sN_7O-HgxRyiSnskMkHolKcNjrbcurXY-4SEkSbq60wuMe-ZRZEE-hCJgr2vzPmHYmsC5T7_rwsWbeSNFU094wMRyNrPNov1Tpyhe2SQi2U8Uj0yyYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=UQpRCpGhUtEjeLU-B3UqW7liSD4LnuNhn62DddT9rWBYhbSTAg4ZBohXgbbakY2MqXjlOyXuzdJyENncQT5KoH3nPWUyM0bx0YFSLw3hZ9nI8BXzW0JaAt6ywj-g80rKzw7-DGSUXUzDjB9GubF4jwK1dM75iSU9xVW7BUgs-RUo-_FmbAPTuPHd1ZIeg269wsiTIHTKV4bm0y2tlPqkBi6p1_afWqwflGwqMG03l4Wmh3Vr_XGlVOQ4gt6O5Nt71Uvw5tADNRhIKw045vvG4tTDXBaRYzBQTrGtRxgIFiy7lueYbnlK6573yoX1WY_AvG-X1CCikDwl0rPde7IEDqdzBuzKBM5k9uuAuRlim7UWc2hFHD-_QEm72J_-IrHBJayF_TghQadq4wdbJbIbaTL1Dq882cY610ayuHpwJCerDUa0npYNXv0X2QXPvfgFd2RoEEqquakhHR1rwCGLZQ80uZRYxq9_hJe7sdAhzck8qcZuOwF_WuIpqjRz3UQooR9YYXk9rvVw6sU3UcJDzwr3BKjYOceeDiLT2BIiu4YV9kNPXnyuQ807sN_7O-HgxRyiSnskMkHolKcNjrbcurXY-4SEkSbq60wuMe-ZRZEE-hCJgr2vzPmHYmsC5T7_rwsWbeSNFU094wMRyNrPNov1Tpyhe2SQi2U8Uj0yyYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آرژانتین به اردن توسط مسی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/96582" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96581">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسی ایستگاهی زددد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96581" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96580">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96580" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مسی هم به بازی اومد
🔥</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/96579" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96578">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=FuY_0BHz_z9eJ8JJJQsjTyuWNsB110y8Tsyiqo9ougvwywJpJPwxcXWfNKS_mpMbIIF3aPfR88b4vqvFNXeaQ9MSSEB7NhYHmc-n54va1lb0D8zO8y-rQL_ZP2CLBImugYb0LuwCNzDX3sI281yusurTERPVy5TJxGyEFwZ4at0eNQnT4134eBg3n5gIeS9zZJorNyi_jYwFZJqQvN-aLJ_CGkPXKMLVxn76WEoUEFiXnkeEXutZhipSPi1PusXZ8sxoZU0aZxxNxitH4LtDmkOo7KFfdBaEyUIkrA8igra5gfHV8dDSuT5j8wYotHXpwZw57tls_cWIsi5JtdwZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=FuY_0BHz_z9eJ8JJJQsjTyuWNsB110y8Tsyiqo9ougvwywJpJPwxcXWfNKS_mpMbIIF3aPfR88b4vqvFNXeaQ9MSSEB7NhYHmc-n54va1lb0D8zO8y-rQL_ZP2CLBImugYb0LuwCNzDX3sI281yusurTERPVy5TJxGyEFwZ4at0eNQnT4134eBg3n5gIeS9zZJorNyi_jYwFZJqQvN-aLJ_CGkPXKMLVxn76WEoUEFiXnkeEXutZhipSPi1PusXZ8sxoZU0aZxxNxitH4LtDmkOo7KFfdBaEyUIkrA8igra5gfHV8dDSuT5j8wYotHXpwZw57tls_cWIsi5JtdwZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
گلللل اول اردن به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96578" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96577">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الجزایر گل مساوی رو زددددد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96577" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96576">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=ga1QEVY7n2JMg-y2SoV_uX_nKFIwzOSmtz7YczgvJTEobFQXj0KkMTP3gG7zkeyXExUOWRkAClMy04L602tvtN6UeviMoL_BvkmMCr3RWiKXetU36rIRCJDpnxBCRjAeeBg6C_cYMEuvdWcNMiqFCJ5BfMidVzhpIlSC6P_RRyCyYf0gQ1T86ifnQx5nQtkNpCAQMGog_dBhduNzfjPx-KGCOJUeUWFrsPVHaRRyV09VVhE_kmkPjYeD_r568HdIMeD7k6MjP2siFVZenFylGjVMzHJJ4Gpozc4wtqP0j8wcd4AsIA0m7XYrqhKFR1HGePauw9zQzPtWPBFQqRLtPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=ga1QEVY7n2JMg-y2SoV_uX_nKFIwzOSmtz7YczgvJTEobFQXj0KkMTP3gG7zkeyXExUOWRkAClMy04L602tvtN6UeviMoL_BvkmMCr3RWiKXetU36rIRCJDpnxBCRjAeeBg6C_cYMEuvdWcNMiqFCJ5BfMidVzhpIlSC6P_RRyCyYf0gQ1T86ifnQx5nQtkNpCAQMGog_dBhduNzfjPx-KGCOJUeUWFrsPVHaRRyV09VVhE_kmkPjYeD_r568HdIMeD7k6MjP2siFVZenFylGjVMzHJJ4Gpozc4wtqP0j8wcd4AsIA0m7XYrqhKFR1HGePauw9zQzPtWPBFQqRLtPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل دوم اتریش به الجزایر توسط سابیتزر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/96576" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96575">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/96575" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96574">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سابیتزر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/96574" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96573">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتریش زد
🤣
🤣</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96573" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96572">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/96572" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96571">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اردنننننننن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96571" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96570">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/96570" target="_blank">📅 06:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96569">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96569" target="_blank">📅 06:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96568">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUk6vOZGhxl6sBcwuSu87U1VTKMvcU7nXnffSjAbHxP1OPzaJxkShC2473x-VRfoLVUcCMN63wq7pfGVLTUzP7WlIgg8DHvoJencjpUQ0YxzkEVRN1_NcnwKxSh4SiCByCiJTK5Ob_AaCXCsC2VRL8QEQu7KeL-Ky38gGJe81xyQwQlDe8hkGPrrcUowlf6Y5fu_hlPWHzKiNu0ScAqXP9t9wquRKCD8W9cD8ijbtj7-J3Pvx2nN5CyLqCxdJ_Zq8x9GKrwXlwNrNy7vF055bPUjjaUpWrrNupW46q-z3X0TyT8QXDeoVttpyVdmkkYCOeyF9UIeKz-ZkGp3lqzsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی داره گرم میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96568" target="_blank">📅 06:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96567">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سومی آرژانتینننن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96567" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96566">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سومی آرژانتینننن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96566" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96565">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گللللللللللل</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96565" target="_blank">📅 06:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96564">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNVkXNCqIci2JWR7LB8bQsVCt97QKGqRNqu9-nawA248X_W47iy3wyYDYyaQxcHKfxSw1HzCxuLuYE_xWn3WOyc8c0j-LERfvwUsoiL0qfMND1Xh5hK3MWz2wuhRfC-E_IVnnXHD9XaOC50wsJkdNy-MciylxCzs2EofQ-lgALsLQkJecsRHDgP5ks7OoXKuhdTEHUTqVcsDwdkJgtoju3uiTcREEhHhsFepQ6xclfl-x_LriejfhJmGOriDnNd_4zqJ27tF7xOmGKuLIW1hVA1R3hd1mbrxs-c49iBbFzDxwF0lJR2v2tgLAkEJ4cQ9yCYPRj4qmX7hTSfSpwPncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
آرژانتین در ۱۰ بازی آخر خود در جام جهانی ۷ پنالتی کسب کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96564" target="_blank">📅 06:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96563">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوست دارین شاگردان قلعه‌نویی صعود کنند یا نه؟!
بله:
👍
خیر:
👎
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96563" target="_blank">📅 06:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96562">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پایان نیمه اول بازیا
فعلا با این نتایج ایران حذفه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96562" target="_blank">📅 06:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cc68fd1dc.mp4?token=TsIsWL7VdJqNhrbuBZABWXWuta5B_qd6FGE31InwI2fPSfdifafTgGIB8307qvA0pLux2GtcRox9PQt3uEqQYuQI9j5pnnavhdOxA7TngXD_uD7CYvMTNbbX_si49HmJnyh_HS29zQMVfhhTKp6FXXuj9ZUub3s0HZbKCl0TDBdSOwrk-wRKaUnhvfWqVw7Eb2HyfPS1CPntYZNTYj0dNqEv5yPIRnQMb0YBiwJQgi-W2FcYrvdI5RtIgZ_x4oa3b1wbNB09L_vqCU-Uv6sX9nYbqqTE3FR_bY6hfLmVRo0DXvJw-G-mbYC0BV-U58cA7FeBkp_7-QdzwZryW5PDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cc68fd1dc.mp4?token=TsIsWL7VdJqNhrbuBZABWXWuta5B_qd6FGE31InwI2fPSfdifafTgGIB8307qvA0pLux2GtcRox9PQt3uEqQYuQI9j5pnnavhdOxA7TngXD_uD7CYvMTNbbX_si49HmJnyh_HS29zQMVfhhTKp6FXXuj9ZUub3s0HZbKCl0TDBdSOwrk-wRKaUnhvfWqVw7Eb2HyfPS1CPntYZNTYj0dNqEv5yPIRnQMb0YBiwJQgi-W2FcYrvdI5RtIgZ_x4oa3b1wbNB09L_vqCU-Uv6sX9nYbqqTE3FR_bY6hfLmVRo0DXvJw-G-mbYC0BV-U58cA7FeBkp_7-QdzwZryW5PDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل اتریش به الجزایر توسط آرناتوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96561" target="_blank">📅 06:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96560">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توپ خورد به پرچم کرنر برگشت.
همون توپ رفت تو گل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96560" target="_blank">📅 06:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الجزایر گل مساویو زد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96559" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96558">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ریدممممممممم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96558" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96557">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieCSpSK4mlZyucI-2eqXi2qz-HsFgaJyeoSCjBUt-LF5Z5ctimaTIQZzQDx3eEjJENJRO9T-uQnplb_30CmdE00ipSvJRkBaP-fhDOOS_XKWF75pMwKAbNJPGZJPIA8xYvMDnq3cz0OvlkjEQMdFrLt8Gtb-478B3K2FPxYmWXbYAXs_JjL0ACNQ5zqK2C9KIQbe9ly0xzsUMzz7SVL2QVI72YPUhk-ermeWy2MOcv87wB_fuIxMzQ5H_DlbQPx2_jGozobBoZNufJITZBqLa0nLb1FeHW4DdV3DgrdD0lAgZvomNRU41E888OncJslZoVIUxiZzGBjTXXK8_9GutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هوادارای آرژانتین تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96557" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-vlZSjo4BF2105mLW5fEMtcoywoF5vyt6tIy_0Ph53JnbayYI42ddEsB87KpLBJBuAcMgoOkxByRWIQwGJa2EAjlXalunP1mELNIaIP-UTPF6KceZUp0YkPDXb5v1SHYt_wgcU_GCuHs0Bw72dTuMcO49vtoZZa-phXQ79b5Si1NNJLgvrjOzxmEIaXnG2A-XNF8dnj1-K7CTvl0cwjgt2OHmPiEcejoH-DGLhjCe73bsGDyt3Fv1WUgKh5ITl4qecTqwYJz-j-5vwtjYXdnNs3jzrAEhu8jGFuv8s8q7kkzxKCA33P8JtsvDwBVZf57cPEwHNdh8qdlK6XqWKOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neA6VU2THo90UaIoo26o4rcwZdfJv2dajd7qucy-2c4PIXew0E81Khf1_PS8ImgEWWuGvSBprx-5oC-kL310TuGG9q7OgqEtdIiq-S_IFNjUc1IOIp45k4UArxxj8vXqrJ2t0nznydQt-gqWUC_bckrc7TAqq7ndNck6LgJGQmqPZ79Gp980KmBZu4Mcaq5bwL3Z9iSkd38_gBYRsCFs6kb1M36lpZv2suD7BOKfFfnjKkfapa0BniYlKRV8O4Cma4hMp4SSjmx1X2oUAqWkOh_yWLZwRodB6qyDFRrT2VHatec-K1XF5t5TWOztkEDMTUFhXzBSwlRUOJ8_dM_JYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🇵🇹
کریستیانو رونالدو مقابل کلمبیا:
🔹
0 گل
🔹
0 پاس گل
🔹
0 ایجاد موقعیت
🔹
0 دریبل
🔹
1 شوت در چارچوب
🔹
2 دوئل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96555" target="_blank">📅 06:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385982be9b.mp4?token=CBb282aNggBy9q4WCzW9Io2YuG1bVA5KdYWXUGYfE01rLMZC7KHXNPCdCjaaLb7hlFGGg3OR2W9gD1t9yVQ_IpjVmyJ5UgSoXqAoqdzWS7m4mvJmUOQTUHk9OS5iwq92Dg5XwK88p_j0_SZguUH9J8GmsR0vvSwPEzrwkWWvzgW53dopybY9gvpao27HvHU8_MjJ18iSpWv3HS_ypucIGoN4nZZvNqDWiSIt2YFmi6FVdn5ecaNsaxZWFtmGF1ZlkEHh6RYwxbwte9WFsRR3agh6hBYV03DSlev1qR1Upk3Bd7GZAvAYvKF4mDUQmoD6HGJmWyGzBdlnA0YOkDb2Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385982be9b.mp4?token=CBb282aNggBy9q4WCzW9Io2YuG1bVA5KdYWXUGYfE01rLMZC7KHXNPCdCjaaLb7hlFGGg3OR2W9gD1t9yVQ_IpjVmyJ5UgSoXqAoqdzWS7m4mvJmUOQTUHk9OS5iwq92Dg5XwK88p_j0_SZguUH9J8GmsR0vvSwPEzrwkWWvzgW53dopybY9gvpao27HvHU8_MjJ18iSpWv3HS_ypucIGoN4nZZvNqDWiSIt2YFmi6FVdn5ecaNsaxZWFtmGF1ZlkEHh6RYwxbwte9WFsRR3agh6hBYV03DSlev1qR1Upk3Bd7GZAvAYvKF4mDUQmoD6HGJmWyGzBdlnA0YOkDb2Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گللل لائوتارو مارتینز به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96554" target="_blank">📅 06:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4889a222.mp4?token=SVMTGbVill_XA-evln5ZE91Yrhz99__FvyGS1leLBG-ic2KQyRmK_9RDPM7ghfTgJfYXtaAKqtgeQU3B9vgskBgTIV8QoAjyPM4z2O79twVsPtI1cye3rlXvMdiqkUgFMUKWZwkNraij2Mp47N6PCIjCMqxMTCC22YK_hZ9YjAD6GN1B9Ckwq0I-2Gw7x6kVYi1RkSV6xtJJVhdywet_W_4hWRAesFm4PEjvYlSEtnXBTkyb5arzXFUawlipwAZNb5dPXJe6ihVfkaaHO8s8mYgjzzMnmvJ4IRdaonDN-6-iz7JYZzvDjfLr609z8HlZ5ch_vXmwDODhVJu6aFdFhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4889a222.mp4?token=SVMTGbVill_XA-evln5ZE91Yrhz99__FvyGS1leLBG-ic2KQyRmK_9RDPM7ghfTgJfYXtaAKqtgeQU3B9vgskBgTIV8QoAjyPM4z2O79twVsPtI1cye3rlXvMdiqkUgFMUKWZwkNraij2Mp47N6PCIjCMqxMTCC22YK_hZ9YjAD6GN1B9Ckwq0I-2Gw7x6kVYi1RkSV6xtJJVhdywet_W_4hWRAesFm4PEjvYlSEtnXBTkyb5arzXFUawlipwAZNb5dPXJe6ihVfkaaHO8s8mYgjzzMnmvJ4IRdaonDN-6-iz7JYZzvDjfLr609z8HlZ5ch_vXmwDODhVJu6aFdFhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل اتریش به الجزایر توسط آرناتوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96553" target="_blank">📅 06:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96552" target="_blank">📅 06:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لائوتارو پشت توپ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/96551" target="_blank">📅 06:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پنالتی برای آرژانتیننننننننن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/96550" target="_blank">📅 06:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آرناتوویچ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96549" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتریش زدددددددد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96548" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96547" target="_blank">📅 05:58 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
