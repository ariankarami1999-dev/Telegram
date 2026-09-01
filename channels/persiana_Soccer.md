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
<img src="https://cdn4.telesco.pe/file/Ei2kjxsPx73bAWGtPL7ObjXUjndd30NzswBKv_fF3Ey88Z3SRHpF7V_QUtSNZvufbiAMwW7zizIXOtdtQqfSdvf7wqJgaM2IaGQwQJDm2aajJBZXZ7Nq3Y1suLJaomKSIa-mz5ruunCVQZ4CslCDMVwNg2MAVTMd3AN0rxdoGfUhHrl7Qsxybe5hK12J2gYCReJjt_UlSV6i15H2TSKWW8n9NIu-LPnwKUsarwoUCBc9wiYQ1WIhVqSpokPOQXCNoK2xU7Pus1EJYIu9k484xAwc-Tg695wGR5J9aoOE-U3cDe8X6mAefvkWppzdHZmsZOGPhUAPx_H54sOJKVs5-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 09:31:03</div>
<hr>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=LV5oz0VWWEvD5CSG6oLO3N5tK1W4i5FujN-4CbHqdkvlAwZeQ5JH-svd992EbFsRVBC0sCYCmqxRoTjBb37xZqVFSQhEGmZEF6nCBIF7ubCKtLVre_eo9xEWpQEK5nB6gqKqm5wID11NdgXVVHPCaS9Gv0CNtR88vh2VWX8bwh8-oHCg82Frl14S5Cderf9usVstjfiaS-guEbZm0GUEccsVZmYmavtoP8alZ4Yyr1aHEd2fahNRMvzfIkqZSKC1rHGT801hdU3HY0EPoqGM2ZBUBb2h6CAjc3pCxKcxVBtOyKzDNJN4iClCvXuCpiIa2SsK84gXakNbjCOiiGMBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ddec47474.mp4?token=LV5oz0VWWEvD5CSG6oLO3N5tK1W4i5FujN-4CbHqdkvlAwZeQ5JH-svd992EbFsRVBC0sCYCmqxRoTjBb37xZqVFSQhEGmZEF6nCBIF7ubCKtLVre_eo9xEWpQEK5nB6gqKqm5wID11NdgXVVHPCaS9Gv0CNtR88vh2VWX8bwh8-oHCg82Frl14S5Cderf9usVstjfiaS-guEbZm0GUEccsVZmYmavtoP8alZ4Yyr1aHEd2fahNRMvzfIkqZSKC1rHGT801hdU3HY0EPoqGM2ZBUBb2h6CAjc3pCxKcxVBtOyKzDNJN4iClCvXuCpiIa2SsK84gXakNbjCOiiGMBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJz2Tgw7Bmzk8glrivRv_B2iLmZEiozTBeTnD5NTc61X7qGE01iEKzISsequ_U4sdxzhWbk_tUBfU9kUgwhDC8gHA7XeJyAO63p7Ym_n-mbxyp3MVH5WKUkkqzlQD-kFCIyQlqjSblc7ZeFNVqL6E9a_IY1hgnTC2kR_SwOKH2dN7NS1d5LNvV1oHVsglafLhTOSDrB7JV1d3Yx5P9mW3eOuXPIn5z9fdyIxpQzvRi7ddQktx6fOBWzYqeBsRwMeJXwR-BdzUFUmbn1Nve4CoKiS_F2yKwBm41ll0ccW9ecHav4_-SSsY-amooSVCfjfFPljLYCe6f-61Pt19UQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_s1A9yxL0xl8nDzU__r7GfyrwRs0OzsBD3faDZjw1WfxDeMQCl6qUErL6r3CiVt6Q261qSbenvfSdMn8ci4ONpYfgYLobLD6Snul6PwXYFnXyqVz9Kt9oiCaVmNqJt0u88M83ivCe0IepDlpOODurOwa9aezayDCQaAkRgJcsMFwuhu-Ii8QCmUnG02V0mCEMe2biKP8YC2_hAcD89Ne25vPs8vUpNYUZWSyduoX-Xwkr9RxrwlZRbul7miqHIbqvfZrHR5GjHfTYJpzAmSoEJWoWnkEldaTF87ufwa22JsVEX9oovAY64-hMPYgRGp7bPMiK2dqnHrJ8lFMMKcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=H709zl-ePUXCdXitsYO7jjG0AXNwOVU1v-6PiyRoO4zixKzp6NNj6sUh8D8IMnDbpR5J-Bi74M35l8frVsYACugLR-AywvBFzbRblxDIX1HJlCIdrw8uWbKdVHC5NEOB2UrD9OYtx1E5lLJZNM2Yj1ANFRQW9N3oev6mKXgM4Duox5q0d4t3wrnwbYOTRxhbV7m1Na4xE4_Y4f8egggIyDBOgHMgE4yuZ1Vc4U8hrQRJkSv8miy479iitypmHiGHdDXfM2XkUyR2Iblgf5-qKEY0z7F2EcL4SLbUt8y0-MHCi1oqKsGqGVRk1gbVPHr_7oTgiVPe4Zuk3pBlsCi_vYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd806e1b22.mp4?token=H709zl-ePUXCdXitsYO7jjG0AXNwOVU1v-6PiyRoO4zixKzp6NNj6sUh8D8IMnDbpR5J-Bi74M35l8frVsYACugLR-AywvBFzbRblxDIX1HJlCIdrw8uWbKdVHC5NEOB2UrD9OYtx1E5lLJZNM2Yj1ANFRQW9N3oev6mKXgM4Duox5q0d4t3wrnwbYOTRxhbV7m1Na4xE4_Y4f8egggIyDBOgHMgE4yuZ1Vc4U8hrQRJkSv8miy479iitypmHiGHdDXfM2XkUyR2Iblgf5-qKEY0z7F2EcL4SLbUt8y0-MHCi1oqKsGqGVRk1gbVPHr_7oTgiVPe4Zuk3pBlsCi_vYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jib6kRr6GDZShsHdd_8keR7XITVQKsT_WCNbBXuKFUecfoMQpsOb1nyZ_JpsiGZiSLI3cDlKq_1eFKb7cNneBaBjFgmXgrQEvBErdFG0WH7i31Ajwj9cM4Y1caX4v-C1_hmvFsiiqLI0mRTyRV5mEGKd1twjd3GCcfUpei8cdfMDKHxG8w-kPSx4fwO-yTmGhLVG4rRODQHAhhifZ8m28-KkwruEi17YUFYVRTuLOPQfQ8amhw7e6ynj4aCzgvRq_k-6VFR8yXNfcizBwxnTAFBuW75YtdW_DfPN5yuWd9PjGAsEGGIsIWtdtrwlAokg5fGhKrzho5gKXn6gEz8Vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لالیگا|شروع طوفانی بارسا هانسی فلیک در فصل جدید با زدن 12 گل در 3 مسابقه؛ پیروزی پرگل آبی‌اناری‌ها با درخشش یامال.
🔵
بارسلونا
5️⃣
-
2️⃣
رایووایکانو
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3AaF3QcOIWgoJKlO2TpiBUlHrxQ22sU7DgCFh-ujy2-W6aeJMkZMe-A8FPk1DS9DZN4Z3dhj1MRrnliAkcJsFRcUKxOCFSr_9nOHNW-t-rVyfsvJpjiPlnh4md8moaQ2i0dNDYzH15fn3J8E1JHiRZmxQqdPl6jwQmc2O8FxqQQej1D3DSRYdQSfi1UV1iVdN9X3-oT91n7PwUL7DxUigUhz6cYP0XzH4Taw97FSUGZ-DYu2fHGzSbcU5JyAU6GAEZsveOmrKLLy0XgiQzUMOm1cmmMfgo9pH6Qxaafj4Ulg2rDPJTt4d3tWGuwz6iOYzbVaJOgPJfe3C_xSKep8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=g3AM8GOx5PwOs-8qPHj-ewYmQF07El_nZRkseIXRPNuaHRz2cWe7pZ2OSJTgU1G8V5UssCFZzUTSR7PXiSlZ7nKqJ-5-SOXur_dT947RL2meIk1kuA0wh4S4ueQHvzgp588-4hIHDIyVl7jZ4O5KKr0SFJ-I5cXc3ETnKN21iSgaBJcPrvXwEyEOlnMm7f6AqRFzlRtdqZrsYP3fBkioedwxmp0cmpCzE0T4Xot7g7WWV9C52gCTlr2qBsShBaQoAwbvfiq0oogmIOPWd1oLLj_tBEIj7Apvmf6PF0iFIOlsxid0q2yANnpUKHZwRvYzclqx2s5pshBsA2ciRnopqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f678a57f6f.mp4?token=g3AM8GOx5PwOs-8qPHj-ewYmQF07El_nZRkseIXRPNuaHRz2cWe7pZ2OSJTgU1G8V5UssCFZzUTSR7PXiSlZ7nKqJ-5-SOXur_dT947RL2meIk1kuA0wh4S4ueQHvzgp588-4hIHDIyVl7jZ4O5KKr0SFJ-I5cXc3ETnKN21iSgaBJcPrvXwEyEOlnMm7f6AqRFzlRtdqZrsYP3fBkioedwxmp0cmpCzE0T4Xot7g7WWV9C52gCTlr2qBsShBaQoAwbvfiq0oogmIOPWd1oLLj_tBEIj7Apvmf6PF0iFIOlsxid0q2yANnpUKHZwRvYzclqx2s5pshBsA2ciRnopqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه سپاهان از باشگاه‌استقلال و هواداران این تیم‌بابت‌حرکت‌زشت و زننده عارف حاجی عیدی عذر خواهی کرد؛ این باشگاه همچنیین موافقت خود را با قهرمانی باشگاه استقلال در فصل گذشته رقابت های لیگ به فدراسیون فوتبال و سازمان لیگ اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0zOpSE5M6aaDpt1V7H4l0YQiX9WzMzARqMcFJcJoSJNG7wOqM4dZDPrimolu6MGJtXzb1qHVib-JjBOhsUgEF3VmF9BRUa-kxb5wQzJUlCaauneIUk2LJSYQMSk3sGz48kTixlEMdjcXYqe6-XfJWY7KYQ3mEDcBL8F0nz5SxPi7KCaoivpGtvJSUTV8_ve3G9ZQ6co4X4OSp74N-IXcENLz1-gLrArSXaeB9Xn0QNFw6gMGKopFmEvZA8_fRckbf40160gq3R1ssOVvgtOQ2FG7xIzAZLa1NHFtZl32bl9Iveq6jOclCvEvctBI00ysHx40KBdDLAC8yooRZZbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجامیتونی‌همچین‌آماری ببینی؟فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET
@HUNTTER_BET</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/28827" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFpGLog-T938Klzm8OXXEVDMdaRz8vA469MI23T3B6B_KVIA6uL79pp6L8U4WVfZgBc1HZyxFXdyfihhhRdLzB6RedE6TRk19NWPjIkYLg8Kgt70uBxu3-ez5KFJ2Ug_slLt5zkzFMExrvCBTiMOwH224iritsYp-H6e397hPazR6zVIT7K6WWeAfNt5GxDqeqloQk0fQ2uI1xZFZyaj-jMSo0k3phAFR4WIxQf4r5t-WRkneMBUJRtT7z5TnXJHNeUGTWK5WNW6L0ojSxT_v140v71fKBVuBpJSkwn63zWL-kW9lsX-8XZzVZEDLHYApFqe8jwpfUPCLrRrQKTu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c6848cef.mp4?token=cUdwX-FrD7mi_EPgPDksyJrGuUhS05hx24-hjQgl8yHzAemzKWIjo_UUf12ryWUvw0Pcz360g8wEv2nm2nx54r7NOwAzfGRwACFNQpq-yCmppMjRvKdtiD7-f-u3aY13CU-vKgrdxyROkcmlgRgczHw7mkzYNum_oZ8urIQfyxoQ4-lGtmZzYS7AEomXOSEXcqVV54VpXWZubqrzDUlk8qGndfrhOVijIrWqBMzwpihFIaVdokezn66UgPYjJmTxdgttEi9GZFxuIcjb06HICcO9SlrNkC95zQ5obvyd8DzNNaX0Vvj-J9lbJCYqirt_dxItb8BYe3QTC_hzO2f1nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWLFJakt-SW1oux1dtT2Brdd1GaJSekGePaHHqkJwY2XuYHs22mRXbkYdmBSqCkdjn-ryOjeiT0-BE4KbAaLGDAysSbzsk4ZKsFAWWf2g0WdWNuPBZiok4-T3TMW87lAWls1VVdCfe1T9bzw_mXhKrywWaPExwYNTGqfWFu7FE14XXIlkuxwgSj15JqcYXNTRyT_shjMLeCkmK6FA5EaLwLApi64MhfZcsbiwadyzkcs2SQHwteIfLky0RkSVM9cDFFaGle54nn4_aUkSWG3klkidldMfoECJbyG8AjyaVzqEpxzk-TLYDC9Pd-PEYJ8WNClzahvao1tELuRNHRxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F16ULvQtNLg_dmxy5vZX1uLSU5ErYJh3SdiS3lg1rnuTSFtQ8KI0jf4BtzgPOP_XfHm9UVG8vZioZ6qV5TWoi4PW1A3JRRjhDoYeVYQiOP14nm1oguR1p2cdBfW14vSbg_4i5KOdUxsq_LCE1p1sNRHAERnWJAg3-b3TkyxOd36DyvKhK4Ie2W9fLmiG9KEwC51rbjNz5oH_cMQFWNRGWSZNaAWWTcAjo1pMiyGLPLY7W4I9HuU4swCzfG3jS3DDY79Wpt59Inq3AiS1LQ5LMBDGZag2LaXU31dkUpb7BGU7QecUMRjT91eqUlyvJsxo3BfrEropG6jVlb6J8nOTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rab4EWM-tanhytoMLb8IqSYb4_l0B6TtD12GYGEstxeJ7f1l2KHQYMEPQwWDC9lCGLilQ_RE0TTh9OBRYV0SwYHhZA6maPnxt3_OamYHVICEMqd7tkHP0K4xVyVaCS5-REuoGhMPGmgqc-oo7QfSicXl0uR3_9GKEaWo8cdG2w5MEyvTyT5-5E54O2jo1Eu_uujLPWQu4aHTNFvSYNTCNQjy330S8xfBRFRIoGGaWG6_6072x3guJrrnLUEBDDhs-66JzlU2MYju0r07YzW5Vb8FmjSfnk9IQ5cs2fbbdzAPou-8CIeozxBR2z69OH8s1pxpih8QIV8uA2QZ0JgywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=fptYgem_sqFIlU7slgqPL9EStUkoxqMoePrbtO6gNQCHVhexUsCAu-OXsFi-qXjujVUm3r42cktruhZnesjorcjb3eepyP_P0tnkVcTXLL0RdZXwHUZGf7M6cppgIYFq0-9AQDLlkWKUTVjb6CCZ01DpHVWGGlD-pGo0WocU3Njm0i1sFdocUIyJD21Xa2ajRiTMHVEs4no8sK64FsvXaPMiyQ9XKvj2sSJA6p5hUvHr-fL7UZ2XUIqQXSz0no1Ffk9KHy_fwdoxO6pDdrverUd4sfh3zSHDE3J0evRFgy_xXwVJrlpoL8Tv3cCId1VjiseHVC1WRguSN5N-71vK-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=fptYgem_sqFIlU7slgqPL9EStUkoxqMoePrbtO6gNQCHVhexUsCAu-OXsFi-qXjujVUm3r42cktruhZnesjorcjb3eepyP_P0tnkVcTXLL0RdZXwHUZGf7M6cppgIYFq0-9AQDLlkWKUTVjb6CCZ01DpHVWGGlD-pGo0WocU3Njm0i1sFdocUIyJD21Xa2ajRiTMHVEs4no8sK64FsvXaPMiyQ9XKvj2sSJA6p5hUvHr-fL7UZ2XUIqQXSz0no1Ffk9KHy_fwdoxO6pDdrverUd4sfh3zSHDE3J0evRFgy_xXwVJrlpoL8Tv3cCId1VjiseHVC1WRguSN5N-71vK-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7g6t1_psYj8uPFRPLG1MA0vOxgc9h8RnbCOGWoArWcQOlqkLMCnrNWBrwsRNjyysqEoBgA_MW2cVbVJHIHT7odRctOkxMOM7pg722E0sdcTL6byZu6eCd4ghQcW-sfV8WyWBEh55xaFPkYD4TBLwRTWU5WYfdldrVtC_InTdiwj-5kUElZXuMN9hXcChnwDucYAYWbc8kYMk9CzhdtIiyUzlEB5RW-Kx8IVfNff-Eegy20aVpDc4T2gRmPDSSuGPkLBiCkZr6r0q75C2nKmBheZYg02LrGsYD3VKzxeoC0RmBYNzGOhL718LBp6sHdusZ2cXx41NlKYY8ctUXu4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PID26wGtTtVjIDhRbPfiH26aXeytkKF3HErlNUeBsgm0XE_O8dhsDe21RDJaO9iLxgLi748JLqHiVygb-qht5TqKG0jrRvdCKJ7IAWBiv2L0WfT5Q8hSBwlS06z8UVycwm2x-VVq5hSN2Ebp2YmvlMbHXhKtmAoYE4FBElFqYTLbr-BrpqrljQfC1OZMB4Mh_4BiR5HDzK5Zvt0rsGuCu6GyLzgQUFzQzhZagJ1jwscmQ5_RMTXSirwQ7txwGIxIiGgvcAW56xcDfUowqrOcMSqFUuJ8YEv9nwqRBZcYOTbzL292rKIRi85_mGm5XkRh_VqXWhpJnjwrBMVxmW8Nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa9U1tfgY_PeIwyevoXUoLIapfeGLwHLBWOuQ0c0dMAXRB5LcpqFX8H2TQcOIoxBj1gtDIM8Fqc3VCcJxUVdsjVqtGfeFS7rqlNpdAtqrWYjn5tCHWwsBnEk9UXymSk2EH8uC0vq41Pf7oIkJBIEXke5-0ldZb3WFlbbNtUSrrLHy7D_l0stApK5CxbSM7v1BaNSDD_nOslPhdRQ7tRNWzp3_SRrN52d1ur0CYzvVrPGcLkTOWDXtlzw6KL8SsTX-15Gwq5e7NlAIurwJfZZI9sG6vsGHKgbf890EFbIvNAN_oXQKwC6xowIFBXTKNxMjGQYewFNmgbUsO5wNdP-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQaRiiFc4VfLf0GoKSg4RQXJWk_nv66Guy9I9hCm9xDdNI5-fkXdYRdOwmWjs-DoHyZO8Cu5xPAWo4Y-0Q-mZ6zi-MSDzStN_7ug5vIEMzDT6bYLJZiDPtP0HkuABliwWDroBG4yeedRiBBq100o5Tz7k1820qdgub0pmD8HVX9cuJm8TL0IzcVpwXA8z1V3QoxcDsxfMx3Lg4X-IDn-f7XwZWAgRvn0abPb7-eyzVY_zGcaaTezozKCJs-e2rSj6C72j4EWD6GCPeKlG9J0MiFudrSZgwnGeNHstajjFhlxa9pRz33Yp8y56CXQFf2n73qGkQcsA-NShX63ZqzH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMz09ju51dynKcg9cRskpinO6XD7X_4mvcI8PlinurCiukaBQ34V_qrl27-P5g3tWzcnVmewBSw5_5TKeXT0LsYoBEW2-OCv5G_obD19_CY0ibzmdL2tX7fMaKRwV9_sfELpBGT-C6jN5EsrKGT6v7X7Z5PRb3f6kYcKdPNjwX0cdsecWMBoKg4KG5d_0uFD4igr3uG8-57qo6LR3sRcqoJa_y6wRJTU2YH0fnIOkljUWzuhCTqkr_SG_7jmpSaMTKFObMO8xdYTl3OYe9I7Et4XwaV8mSS08KnpfxRqM7FqGETroNexKQ5ryga3cOCmg5A_n6jRgt4-VIl9q_X41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIVZ44xKGIFXsRO1ChLVrCS58ZvldZlUWD0-l6qiqMhGMq3WQB-D1q82cwshbeZB7qCCG4sCVTGa4GL5PrZUMdYkL8HnBix5fcM4pm5T8k49UW8x15WZTzqSlJV04VD3JKJHdiS6S9S0pdLlK_uUcytGm8BCkMeWJimx9bLdHOybPQ76MEOh6zZoXF5qPlx2GuQ2I6BCDVPNncED7yYG9kDi3uDCwsivmjFcLjnHfeNLBz9o4wfpD8jgfTQhyVp96-0_MS3dqeniQWuFRI48omf2dfoIcsgd542cGXBiOsQPmQ_1gskJQfU5ntZPfR2Hl0yC8ubnJPij1GfZ_t88XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg57VC2dl6MDdldvXFnUME54tg5EPOCjAcPXiSa903HPfqYmKNdVrusgyeVz5wBFrvEKuasSfL42Iqy_OstvKHPQZ1-DgVLjTAPEDskmisGyGz4BtgkNlrQuSrahMU2pmWtpM0sn54aJSdL-IdcxcJDbB9gM1HPuXJ9BG1-v4fWKKSOfyFXjZpK08KBMgkyYCBpxxEYDgoBJvM873Ar_8NdyDCwyv9bH3efUr-g4H-ILNJvbBzKivAkji_btzL6isMVuxdeUfTQQMnyFTd7ubdQ4HIJYzhAxT723uXjaGX627RxEkr_y0GewZf7ZE9iek2hjIRA6kBd6K7Rb093oEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYbAmjL4sNKBornsB6Fh5S_Gwp7qnwMRSLtzuaZv2LsrlncxzF_ety4gFFeUdHYBaaroLKCZdABp0J2BQbHfgDi-j9ZPfThXCj1RLf21ioOyEz3-HJzvLdX_5dFjP502fjCBLTs4cG48XakK7tFoSehsOSuClGw27j6Iv5N8FOPHITl2jLuymYRvgUHjP3qHFbVT3SuMoXhxCoszTC-LpBcTir9AJIaoAd43dH0wVvwK-c33pQE-LlPINEe1p_d6p1dP-Dk04jGJ5O_EaR4OpQv9pQi8nWmCkc5EYcCOjbFzfZZPNSfQ_HX32G53pzz0gtLARKce8H1CT7emdBaKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOmYQLjhilLCFm6eghSEkm-I_970Ah4LNnMs_Hsn39bbQcQyHhwrU7wcxglVJ9mxUcAiyiiljL_lqmZ4DtHvBicvqZ8SxnIRmo22xNuAt2zPRT-VzebVo25P_fbbiZm30qvQBVqG1W_wIX31LM4tOOilDbdRy22S24j8EI49wlweNrjvlV5YGTZKuU92JvaVDtIz1oW6YCQ84ggMhj-PH65ALRvhWwAEVkbeBnLhM19Vjnqu7rkKIc6bl1Y9uyP7EplCicB9hSHdnNlihm_I-CIUhatuxJxqFHe8tW9Jg9M8-V7-UfjgaVNurKihRtnThLu4DpN8bsEFAVvuaP2nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYIRMWM_kHJcRZJ1Z88sriSTGIp0UMWE9gq7ji47Q_TzdxWZBa8YIniYKsF_XFZypJu_G6qlluhtjzmp-V3aoXKZq9J8Ev8fKMdJgnnBFALpxFOALd-NqzAnqkJ3vyczJtWp8LHn21yKgXn4mP1jpgM8j3s3BZUO7ev6qbp8cy0Yeot_jMR5RhLlhphM5Yl168mFQ8vIlEkfswD8FgH2p2-EBopBC0n7vBGkr7w8QV3jlUEKByut9sW9xHm07tjEteRVhFy0-pS5VsgfBJrZ11DJZzq_wjF5imNVyY_JDqUg2T_YDNKVatNLMMt5-y_kxibewsGkwEZolDdiOhbkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال‌سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت‌استفاده‌از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28809" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW8VcLzZCFpHKb-HSLIkR_y3a-q3OQ0LRNg6plybqBOalU-wdR5n-GAcNkCf9xxGGIslomlVaTmF1EEnt4aogaQMYzqgKIXYbqTekvDpdiKaVV8Dp20NMktPNUgzFsUFWx9VGXfqwVOoF0DCE8Adt9FVLfWZYv33ql-Rjh0ZMSNDcizMbP7Tq2zD4cIIcBPOB8ilD2kRlDktuVmPDPsn-cf7sxqgzS-KOVmcYuO81cJKdFMxGgTtXxH1ZDiMXyMQcQpmM8xf1u2qz0pPAKoccIMxbpOJBwv39GcGCyEQ3lhk94pMnVFuKl1tAFsPu8Yh2ju1No9bQSapZKSNLUlshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=ki1JU2urNp_N1AZ_JDNFx981sauce2SxkBQ-n6lJWQLoQeAoEhdz7l-dbfeO9ZGBgkmZF6mYP2p8zH7wDIQ0FWsXgOf0K-XxzSYm_FLFzeWHSTkwAzAURkvSRCE9l-GEEfyLQs7nc1frI46MZxBPmlGxoehePeA6fOeKqrg8-xJ2bofGleGXxD4IceVIVnIh4QkecWCaKBHWCeLLxZ-uciwW7XY4LjSpDKCNHL7fGqMW7qBCmLKPINSwpC7gwb7eWKSC-LLFTmqVKRGmRISLvr_1T1v9RIhtBFYGx42PXcv1LHyLi_BHYlUW7NKLDDPe15vUR_YeeMiS5kKwFgDMTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=ki1JU2urNp_N1AZ_JDNFx981sauce2SxkBQ-n6lJWQLoQeAoEhdz7l-dbfeO9ZGBgkmZF6mYP2p8zH7wDIQ0FWsXgOf0K-XxzSYm_FLFzeWHSTkwAzAURkvSRCE9l-GEEfyLQs7nc1frI46MZxBPmlGxoehePeA6fOeKqrg8-xJ2bofGleGXxD4IceVIVnIh4QkecWCaKBHWCeLLxZ-uciwW7XY4LjSpDKCNHL7fGqMW7qBCmLKPINSwpC7gwb7eWKSC-LLFTmqVKRGmRISLvr_1T1v9RIhtBFYGx42PXcv1LHyLi_BHYlUW7NKLDDPe15vUR_YeeMiS5kKwFgDMTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXFexPfyszIisonRZmTB5grUmmM4V3LaUXYgFbBJZ8C8cDIfkttQuXqULf67QOqnp6QIN-vKngQoXqdk5yRRddJ20l72hfNJ4PtkD_q5DVkTpEGLU4l9is-xDE0ANsIENlMvqCWFmUZSJj8pdI3TS_HFdM4ncKoe6vY6bQ9AmVcK1uszRaS7KGlnKR83RpmSoaLZOSg-ZbcFfr0J7ParAFSqAnXHw4DdUvgoyy2nGeYinz1k_ks6eB1nMGXcFXvRBAHyzfdVqDxBOYUlEpMaHuoiHW0ltjYoI7HfS2Os-Z3Dmwczp6x5drWcgHWhGGuta-ItYNN8-RGDzp7xpMjKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unM8SJMHC9QAKVQJ7KqJaK6tai2arE_0hEA4ZZPHwZDENi0_NMVPl1YxN5p7siTIeF9eGncdy2IrA98HGKzBSQy2SjzD_8AgzDoxgCmNHE2Hz-56bel9QLXOrJyaM9VSdKMhtn6TuI72V-ZssftPKUEoZ7CbXMh4oKZDSDzhaRGCwDRQz-BMkx5REF5M1e34ikvO9zEcaxivYtUvYWC0SsOjbzFTI3TLWZaik0aCecPGEHgyjwBzTEy3wZ1TAB1UpVY9Qw9_f_vG-isJ0G22PmBx8jjwn4_EzAcPr-8N7xttuzkqqG8mz0eevtOdnwJVph7mjMEbpcx1vdsDzZDvAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5joGjoYFkE-vO8cK_WLYvSDarCKqD7THQ9UM_iGOzTTrCAiibK08kLbkwQJcEbDi_30G7iUvv6sNTYkfP4rOyMU2q6SEDi6glQLeKtXijnJ1gkhqZJtNjAeyyWpi2Glat23IPHpCVuXn9nOPYVRGeZ79-TillczDWye6db_UGHHQ0tkEBGSPUn902n_ejMAqe34YIyp9K5e3Bh0Dc7i_M65OpOB5nYotnRR3M8jLNcZMygxDyUGl3KALNX4Or1XLAD-e7LFWeR1LvqLuf78VlNmlm1lOXBZdbSklRAZzE9XBYMQwForMp3f97eUZhwJoLhVxFdZWWTwtYhN8F399g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6Zrem8i5oBQrfsP52HTY1BX3hL3VWcIv8SbcTLVADiY8tbBrNnwHdinxgJ_DhZcoEHzM0o99UFbMGOn28YTkqxvkVfGjdK2PtKCOtUi_SrhKkMJ5ZnCWCtjKD3Ss3snvGZnpTfIQP0avXrUX4RN_fhFOn-wPV95bxzIllXekq7NCRVo6hVEfVRv0Yz4D8G3qjRPiipIBb8ccUmY1cHqluvDTzzN0xBUiEoPcjkaXlBzQy81htSZUe_dSg6IV1dHYCVZx5L4tNGIFCefIGGKj998p96EgwsJXFALp3cb46GfHsDFuN6qpQwwpJOuSz_s5JPA3SiPNEmOAGpseWu5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiE_CleKzn93ZChQXjAW3DYoKCnt0poB_GV7vs9AOHl3wRiD1FurBVilS0fXCtvBLNZi8smYtnyKV4avwCNbCXMhOhP_dOhITMTIPp927kzY-gkmzV6rZV8VxVRNCBqRBnVFsLaRh4eD4PiTqr7mR-5UiqUTbEC1BCcELdpJQJ5TRpYDkg983mNvNSgLImwMOha3guqfJbMNdjmgz11T2c9NZipq-ibQH-e157P8ob7bISYhy11wK3cPYxk7WxXMlaM8jv_9y_BZZ8u3zgje6eVfltpnYimnM6HUXzg1utkLUslfE1NAWJqLXAtVLuSgt89c3PwxST749r9892Cw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlnvYBHV28krSJ93fF8Eo32VxGyAuJ7N3jUUu1YwWe0AfDAfOWQYeIGBJhxwcXzGqP8T7IVzWp0r3SiqOGFlB1cGW9hpwc6eu-btL1HXlPuAFaSk6-pWMKqjD4-MwPmoXqEsWg8lokYaLu80fhlRa7DR0uf7W9nhVicmAK23gng_m2mUHLoWSaCBGRu5PFscInTZoSE-W0KFQcSHG4zdMVh-hBzX13igaRPR2ru4KGjNrIxPzP6iIRBtt_U7L6J9OmL6ErxdKw88A3X4q__OLdCANQmj3l9b2HeNseMyze8Tm6uAr8UkiXPvI52fHkVj_DY6QGWXoZmixmIyACwTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEVnewy415aCTKgIuNy4kKYVqYT4VjQKe_RvVDoNNRaJOQ1qwAb_9RGmutOT0gKTU0zmybgcGiTq-l-9XYEtFfBJsI6o3ATlBPK_6nxNaXB1u5lqJiijMtHkEhkw7WPjWg6YZmbauu5hLsDmhn0gsR9JdmGGDyql2E110VVbIKNNX1m1ZqYjgaE0JfR6MieBd_NztgC8xNMG6y1zNSicNzPN_ry1iRUV6JXjd9qgjIOkWTIurDr4YVsOh2I_DmwtLXApT_wmQjXiWyp-QD6xxtc-A92lBqa1EuIf_yQum2xt7JIL_o0ZZFD4S5TmeC_q7ukKW7Ng_SzdJ8PlxF-MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=OxxyRO6qg5kG-S52gj5c7ja3gX5g3twdzjVFb5BO1WR5Z-lrvwXCkw7VxTusZQ-4818GOl6GRi-xRKmjZjsBCvjXcvANPjwLRk0vEimQ8ahYnlNXFIdxrv41VxruTDE4TNriWL8cJ-win7mC53u5f3WdxeXgTRUjaDBpmb6Cqxd_b4R4n7fEC6R-4_qqN07bmfLlfcJpBrfhuJWyBo3Pw6px5H5tkkl5E-ZsnOPNBj4C8wA-slu5ISkuSot7OzKJI8T6na0fgOYoj9uLqR0XZxDbeNRd9WiPrjHtYOzQoSRJRqs7D32M1p-yQbGgiMnmQ1ACA4pWcCy8JuZ1h416vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=OxxyRO6qg5kG-S52gj5c7ja3gX5g3twdzjVFb5BO1WR5Z-lrvwXCkw7VxTusZQ-4818GOl6GRi-xRKmjZjsBCvjXcvANPjwLRk0vEimQ8ahYnlNXFIdxrv41VxruTDE4TNriWL8cJ-win7mC53u5f3WdxeXgTRUjaDBpmb6Cqxd_b4R4n7fEC6R-4_qqN07bmfLlfcJpBrfhuJWyBo3Pw6px5H5tkkl5E-ZsnOPNBj4C8wA-slu5ISkuSot7OzKJI8T6na0fgOYoj9uLqR0XZxDbeNRd9WiPrjHtYOzQoSRJRqs7D32M1p-yQbGgiMnmQ1ACA4pWcCy8JuZ1h416vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVUWgh0jG6iqBlgQ_pjTfYSmLD6XssK5NXJ_m0ZjX7L5vZdb3qfQj1ARFQYt7EaMbppPCSe0dUeYkrqn__dCkvOAxAx-Q_isWVoJ4foiJ-5_8A5-wq9tpr9fWzshfdCxFmHfOW8Cj14xao8GOQeMjXW0Ix_bDgJTJBTvBuliaeMWFGU8JFvf_Mp7SxAaQR8ixsTEd-0p6UVOHtyHkx1_thdpiovgy9Wj4OrnqaOsKf4sCatqmYY-su9XRmwdLNewgeXsvAEqQU83eu7Zy13EZ3aTSSH7x3O3433FKZSckaZbE-DsItmD2xFVNhri4CiogKIBmEkJ3_EDIZnFiJ4vw_IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVUWgh0jG6iqBlgQ_pjTfYSmLD6XssK5NXJ_m0ZjX7L5vZdb3qfQj1ARFQYt7EaMbppPCSe0dUeYkrqn__dCkvOAxAx-Q_isWVoJ4foiJ-5_8A5-wq9tpr9fWzshfdCxFmHfOW8Cj14xao8GOQeMjXW0Ix_bDgJTJBTvBuliaeMWFGU8JFvf_Mp7SxAaQR8ixsTEd-0p6UVOHtyHkx1_thdpiovgy9Wj4OrnqaOsKf4sCatqmYY-su9XRmwdLNewgeXsvAEqQU83eu7Zy13EZ3aTSSH7x3O3433FKZSckaZbE-DsItmD2xFVNhri4CiogKIBmEkJ3_EDIZnFiJ4vw_IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGpSWvtq5KXFNdhysuERKVPzQg1Qvx4GJpxB6jZx7LpCQnSCT7UVQG9cN9wf3EfDq7aor00MbPYfujffOCZ1PiIUEECT_9MD-XtF3pWn_unknfldC5xjQ8QCg-Riq-fru7MmrlbFid7f7TiNuID0xoyyfDK_FMlhbqBQzxYxlS61EqGgZYHXrjCmJOdXUXsOZhFVSxru_bM0pIWL8OOupPkjBGXc1MYJvmHqGEjT7jFnD2xnXbSRYU5Me9vbZ0edK0Luv9cZnYldY-4gyFctsPoGkrtLfGOxWDF8O-e_MaDiSEDLjMgOWu8Adv-OcEO8kELxLOLh3LyMmwYYvBzi7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKrRO8S-gDsLpiVYn3fXhKAZjOg89GZXgv8uqCBJbZjGTlSrBRNQc4CD0000KW01BEX4vQf7iNXDst9m9WRLuRuReCuqg256PhpvkNnj9_CfyK5yqTG7CexMnMO2jhLE6xcE4WCSPgwfCMYjlP6MRVPwcwHxT052tBNLEiOoqc_rVF-tyri7lgqZcdRUHe5rGQdVi_bnn4OaiUs9XE78J2p5vDdwwcgHU4WtI8OtX13xJ1u65MUDJfyz6IqIXYKttzFW8K96gS1NC32Rk3Rucr-e8mefdE3dhsvHq2nGWyvLr7ez77Yc0wa_t5W3zID5vSsvPsiU7kCrMgmLk0WajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdCe0164fl6WAJsvmB5FcUNofWzAAwFBWCyzLSdsE0JMt60_Q_qGMRfVEHM8tnAUHDMuq2R0mQlNPXm5IuEKX0VP41YHbpXpW2v-QD1k__OCioosnxlx_ULMnFObjURAdVcNW5P2jfp7kiz2e1KttcRTgjbBcqwq-taBs0XwfpuI2PmeEIiUDD1wbd_lhFQSbvtk0nE3f3JQB2ki9cajWYCUtWt0lrMVV8mW-7L9Fv-BGM1pMbd2YYCHXDh_D7g_e2Ci7CkmU2tM9aF7IpdC9Ec2cA9kg4AbED3B8a5XYZWNyEiKfDxc_wJBZ7-YxabpWmZkm4L2sybPdpQtqFBIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8HT2LaGlrYPbAwcGB9G5TjqFyR93dWLJ10z6uPQclaTFFEVg8gdyl_dfkGGUXwy1Gu66eS4mQa1gCjOI0ppui7sjcPl_lP2dYU9NC6uGiD_97vfXqlVZGkxDoiDoVxLB0B5d-Tdxrvy_5TYltGF4I84E4LZP8n881GOxkMLW8BVBAHmLv12OliPK0c_MnBvQp1L4GnZO80m_KiK-cLoeQMAGrNJmCUihVBOHvIFW_2C0YbifCqMT2T-e_Y97GwDAMcpirE9H3bAWZ_80jIL04Ww6z9pMhNJPlrPrHqHv0ZuXvtZ8XbyPpP0ftvDE1kGb2F47d6rXaAPm8dR3t6nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctki0RBBp621oBJZGlXAr_BlzVVdamscVf3g-5-2Wpum7RsSoDsHlG-_RGAfxsRtM-Ag7ZjNt1TOh5TalJOH_eY2EDlcTLcNFsh_Fjuul5Sc5JrKAxUWu4-BlHP9xix15xlqOPGeCilzdOkmsgyaNsL3_iAggvrlzSgsMgDZXQolqncxb9MTA-ahXHYSigRVAoffreWBGnzzfXxNUY2RGtr0WEyYS7tJPfBzLezt0ltWw19M5rYo8XUZIdZJygc2Jr2x2PWvFRZz9r6oNvG3RYGHiCtYuT6_GMkgK5mwfufXtwG8qTW2o3SIvAbhgBngCHRyNjYjCQ1cih5in-Dvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=cRr2FuMxQ4vaIMrA5cztB6RzMfJQ8SZjdpHHTPA6m50BAKEO4jH8pdH0gtt-Tjn3BgyTHRbcqSpPhjSRqtV19ZrOHONP4SkR5CWdsXM3LlmPIdInHl9Tge4UCF3EJkOYXmGGkDHLAvi22FSPxtg_w8cK2rmKD8N8vsHenHhY7J0balhxT8Lbv1fPldkMi4Lx7PjidL9-k5YLBE9s5gEFasaBZznirMkTc0lShSopEJetC5htC5C8cfEOOXaAZADFM-HD8Ao4_myKwnTHfqzcLYBxQ4kQI4i1vQTvC8qar-YHivBjMCtU0L-GMGbxWHYAzRyIDpVvpR4yI2HPYoyyVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=cRr2FuMxQ4vaIMrA5cztB6RzMfJQ8SZjdpHHTPA6m50BAKEO4jH8pdH0gtt-Tjn3BgyTHRbcqSpPhjSRqtV19ZrOHONP4SkR5CWdsXM3LlmPIdInHl9Tge4UCF3EJkOYXmGGkDHLAvi22FSPxtg_w8cK2rmKD8N8vsHenHhY7J0balhxT8Lbv1fPldkMi4Lx7PjidL9-k5YLBE9s5gEFasaBZznirMkTc0lShSopEJetC5htC5C8cfEOOXaAZADFM-HD8Ao4_myKwnTHfqzcLYBxQ4kQI4i1vQTvC8qar-YHivBjMCtU0L-GMGbxWHYAzRyIDpVvpR4yI2HPYoyyVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVrM35XLsjF28jmtGoVZi-koGk89zRWw-5SLbj93ReXXjA4at4VALZGoCrtHW6w2bFfdIecEecVCoWRnGwFMQicqakvl6TDhdjMtetwP4G7vwt9w8zQpxRT3E_8Z4Yt-N6_rZQ07wwl792IuUZVedexgeqTwI8qFDz1x4khZvUxSPqgVjkIsKaSQgUcOemwi1kiwG1Kdmo-U01KKBD4lmJp_l0vf1wSL4GSB2lm-xOwsA0efL01bdqMWIr60LLNeOkY21U7gvH8uNHIKXAEjg4Zl29RcDEPlk6bVQvigaU1qS7kPQctrS9aqDSiPRXsv8dXg6q2M_za4PsmYJSt85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXJSoBrsmszdoVzI8ZT7Lo5sLGGHKvKL0XqqGgQNoHbbAZdfFIvY1-GT07rR_eIQQ7os6VdfReHXFVKZsQnoPdBbAVfpiLhp1-sMXkTUfiEZrxHt0Q-1btKQDZCJiCJXp0hDYd_Gdt5a6q8SIsE37dPemh9zW9_GF_bS4Us2mArrCTZPCsV7W_B-BKKbNaJfSRGvCMHbTbovHjis171gqe_Lz1E2sdYl4668LEhxLzeQBcGxv4j6B88LcX5Ke1FOy4PKakIfZ1nQdBHgq2EMyPxUl2mozij60C1KZikQrKnuJ9axEybkk6gsFtbiKkX0spnsV_dnQL4QL-IgkfabxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtqxZWBc8W2PPBYv1r_RD2PQ0O4FRQinjcSOtw5uCREeG-ZO4cg7Htuakw2dh8IeTZViRWvTCQ0GUgHrXniDs7HW6ut_9a6aJir9jBgzD7Ik0A2InFvUB3gcEYfaH6_yIv8vG1UV0sas0ep35CcejXcs9OHhWcYQAFLVf13AefZEmwtJee6ASXlH_924a4qE9Bg73JcgfCOjSuHrJIdZm2suDWb30W0FUTNbkUp-jaB8HDAzM2m2AQ-yHAfWKL0UAVdpvTDReeWH3h03WKs0itBPgAiAyfhEGnEIgt--cImbZ1VbjQmCPYn9jz_661CvKdFVUyGvli9ZFub7v5rLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-sODR8ETopMqa89Aqz5SCDWAko1_ezVjrbln30TFayQuM3A1-KiUFy2P1WN30bkXfwdLR2ueYModry33sY0xNqgJ9QBnbBDYFjHVw9cDgDPJAEtiRWypB47HtVAfPGzR88DzJB6hoWaqkXHOSKCs-rcFY3fiF0Lkx-2wzctXP2QFuIvuCjz8wxtl0epNcUImEESGYcOAULckacKNi_NyHWC89ZjnYc-Bwux-TAn0UWriZu-XQ9G-2tKXKUsIAkqoY6GdKZezrX6GKk_sr2XpE3_KQD5z_6stqzTIR51sHThJWsAc77CFIve1UJWUXwAmyl64cAL3Occ-zeNu-8o1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqYycztowjz-UV5T3EUQmg08CkDKAtNwuFP78fyxQdK_4qtAzwuGQeZXCUhiGQRoOawmhKD4h1J0CYS-PaLERNZZCYunEJnXkjGeSvwDZSjmoTxgI3C9Nk13bfY4h00zQSGWpPYrzqfVv6v72ReJuNoBwJP-wRwp5cEInuR6PDOMUu96Eynic759zfTe9_eyYnm130YH5nRM9R6uDdoHUslnsLeIsojHoAZnjFeHEGapFwwZ4z_9oieojFFLxcdjxWKnw76SIrMBL_cv0YimyTPbHrE2aY8NnSZPqIyM9FbratVzN4QNeHXC5MRnbkMco_cuNCNUlf5sLX5TXP-7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRXVna7QKwHekkX3uumDSr-b8vmo7U90nWAdgD51AlnHbdwn1tP_wMxBUQ2OlfO0IlNEDSc7IQUAwzUfB1kO0uYVKy4Pq8at6rT0q36oUVqGCVLnlZAQPQvQlAhmJFGkZDClatWulEiosK-HZtEH78Kp0XkauuTin7DWgvoZlR9nVdAZX81FFKXMyB1pmyxGiMrllaQ4fgoS5XARr0yuq7cFCCYgYqNSTkmvnV2VDOTDRFIV6iViSou1CSDKdS9QJFJ3twDBMYIUnnNNnBzPgsqXUksrK1BsGED841RtUwKIR8Rj0BvvXYgAqs4I6zoXq99GAS5EGxXxVJA6kqLynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28784">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXlukjuRF-yIGZ06wsBXwjlclqE_gvuJOI-g3_S54YkfwvKir9LSKf5vHLUo37qkzqeupXGg6yOQaxja4YXZvHRhB5f0fc-Zhxb5ZI16BHTxfzkIOSCgrrxAylY9VTtZIoUAkgHRy176k4mR0Ikn3grsbikcblkwZF5MdK3okhNUyOY-cg2BmMMDvptg5ICE4nbDU71ulHQ1ekl2gZF3yeI4xdqvxXl626f8OH8fj4ZsCKrW2MqKm14R08-bbCSmOPgfdtkBhnLo49sHrSYxNOO2xBUCwnmke8dlqT2SYBc8UNK-i95aQYuMZq0We1Wpo5VRx9mvvpYoON7I_5sTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28784" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZNOi11T1lvhnrZwFV5sqeg8Rwkjsncjb_1TMb5aaJwOBb92A5g29eJ1Kx3O-T_hn6vUuJgHomL9luedIA33pFLMeyZGmrPYaIad4XcTJ2N5TM3DRfZ_V83Nh017kDguRLFjeOk9JE13th21Ur-vzGUwdeKvB2pPGu_toeDE3YN_S_H8Q-4bldenMpcfgmoF5F6F_xbAoIyjdITegPZeXTB1q6sTLP7SER-BF_ZLexT7yTjFu6L0TU18hBv5NGR0iNSSyLF8LNeR1XCAwZpw4ZUdo9R09qLAx1iNfwZD-Xgib59UDb5SBwdJLEgW7dizDuP-2JuzFfXcSA-H-1bgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=P0g0x3ULGmm9N4s-DG9WDxVinc-hTbGR-o4da5shObdKFRI9Lo1mEnoy-wnp36-HBKzB5SnLRHG_WYzAV34sTl_LUOJSeoJeoHhrgpuGMxXIcmRBFA6z2HXMrA5kfVb78FLLmvfFcVTrGJEDtrhCO8x7fxBs0wYbfdx1GenMMLUMWPwuR4VQNGswjwlkEOu-SsNeNc9JYf9hV7wITcukN43djRkf960ns2r6STiUAuRk5HHxxzYvb4rZ6kwWnCtp-mbeepu9SoiliD-qicDgKA5NvwK-M9Pm_3e4u8FlwbIubw52PzH0GcWkjz0WZrUqHCFdPM3xdVs0gz6MXelgLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=P0g0x3ULGmm9N4s-DG9WDxVinc-hTbGR-o4da5shObdKFRI9Lo1mEnoy-wnp36-HBKzB5SnLRHG_WYzAV34sTl_LUOJSeoJeoHhrgpuGMxXIcmRBFA6z2HXMrA5kfVb78FLLmvfFcVTrGJEDtrhCO8x7fxBs0wYbfdx1GenMMLUMWPwuR4VQNGswjwlkEOu-SsNeNc9JYf9hV7wITcukN43djRkf960ns2r6STiUAuRk5HHxxzYvb4rZ6kwWnCtp-mbeepu9SoiliD-qicDgKA5NvwK-M9Pm_3e4u8FlwbIubw52PzH0GcWkjz0WZrUqHCFdPM3xdVs0gz6MXelgLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1vkoXtRHANnGO0nUUsPeuoAv8jH-1JEbdi2bhn7kLrX1b3Sfk98_9IKxqjuA-8zJhD_Wu3sgJ0KTiBB30gVZekCM9VkFGs-0TNiVVkG2jkuREA797LmeKgnxSl5oNTF9b6fgLXMZ31BLGhOsT4yx9hiynDZ-a8TBemXW72RNdqEE8hrvt_UVXDqb1wwS6eGbNAgwWEJ5Tk5t3CYMqN0njvxjCpsYJBbGAhfeVR--lD7YMNWfHdh0NaeXz3zvx89zrzLhpzR7jT3e9qpDMl6kb0VW5UHi10J_hyIkYiT8-GlQmtQCY3_aWUjtvjpdD5vBjXEhJagR2E2DzyzyCeGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=SHkGrcGcDWFB2PnEGuczu6BxrXiUBAdfdcIRSA2Hv6AoWYuPqN3JfO75aLa8a6TrqYMIzK48JhM6e9Ve1XODok-29Rg9aCukCKwZ7wZeKE37lQCFRD_JKHVSPJ0WodhesRs4YlhZX0rth8GYnsTBuLileYATx0540WvK_hxY9HqjkJGkz1nRY_N_rnBzPmlLSWOd2sBpw8KJKHbjdxJA29tD_xwK2VtcTO4-4zQplXrUjMfnErxaftT6Zoo0otHJO7jpzsTZETqn2JiOhTlT6v_HEe2NlgDigSfelCs8ZGWiwR1_-_zgG71ugyes8600i2pdL2QOqQ8AkYETHDLbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=SHkGrcGcDWFB2PnEGuczu6BxrXiUBAdfdcIRSA2Hv6AoWYuPqN3JfO75aLa8a6TrqYMIzK48JhM6e9Ve1XODok-29Rg9aCukCKwZ7wZeKE37lQCFRD_JKHVSPJ0WodhesRs4YlhZX0rth8GYnsTBuLileYATx0540WvK_hxY9HqjkJGkz1nRY_N_rnBzPmlLSWOd2sBpw8KJKHbjdxJA29tD_xwK2VtcTO4-4zQplXrUjMfnErxaftT6Zoo0otHJO7jpzsTZETqn2JiOhTlT6v_HEe2NlgDigSfelCs8ZGWiwR1_-_zgG71ugyes8600i2pdL2QOqQ8AkYETHDLbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=iSSOIIveyGf9EJYjeiMJuRkP0RQfOsn07pruc-4RyJ0CBhumQQFdRwG9oqAoqK2qvVEmp4x7RmvnPjBDfQi1j_qAl9t96WSMyd8kjqqWHopHqpOxMkHX-5DMHD0EWZZLlG7poskqm7ti2smp4a5a-vaz-8E_qZaBNuf6CqLBwK1MCDU2wicQx15vzPv8xSkU9j1JX70HXdYUrOVHwpxb63J_AIje2e9mzt5VOnmlrRoZaR9yBqfnrCiXHMpsLvIPRy3vDV6DY1NqSphcY8oeD-bmtViSKnHuKxmUtDWJzO4thBj68z0s_e_zqXjq3xd8211oTseFgz37z6aF5kRwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=iSSOIIveyGf9EJYjeiMJuRkP0RQfOsn07pruc-4RyJ0CBhumQQFdRwG9oqAoqK2qvVEmp4x7RmvnPjBDfQi1j_qAl9t96WSMyd8kjqqWHopHqpOxMkHX-5DMHD0EWZZLlG7poskqm7ti2smp4a5a-vaz-8E_qZaBNuf6CqLBwK1MCDU2wicQx15vzPv8xSkU9j1JX70HXdYUrOVHwpxb63J_AIje2e9mzt5VOnmlrRoZaR9yBqfnrCiXHMpsLvIPRy3vDV6DY1NqSphcY8oeD-bmtViSKnHuKxmUtDWJzO4thBj68z0s_e_zqXjq3xd8211oTseFgz37z6aF5kRwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5sC7aS2LDyBfLFMu_YuKxtk_cdwMAFHxhOcKXT1huKtqGR7vJAMjbt1OdfYVHcC4h-YPICY6f9jajBUwOOqXhhA5yunaMZrRKBOEYnxMit5tl-2yJF66yPDQq_K3Pnf6IgfTOX_MgVG8yFc3KCN8GeE0xAa6yrBANXqzu2C_ntsiEXsUry8Zne26fi-ApSE8JZO7zwvhDjXLm2WbMkTT0HUGhzWLw1Any4G55EuIZo3mLfNXleLEFdojmUDxPQlHivbgj9DdPD89gAbEe3TUKRZ56uXGcLhIi0y-jNEozlZOCApkcpQOJbBCw7B8ss32ZB1Hj68-79kbJUZhEra4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpJNT3lwBUUpwQjOSv4EayVFXDxR5sRGEXcMg7bN_SyK-turHXx9dqMKib2FcCFxicTWEWQJ0TvE7SYrZsJO-HCScHrOvSoxyP0pLQanMGULXUNDevBpmt0Wu3XaIh6MeVuR-wqlH_xx5FykvkkokyEGFfbAa_En2p1cKbohJiOLeiaNMVI4Ujkl2t_rr3uG8E8y9Xai8HuATNhzl66b4JoP2gg2rw6FWpYlv4uS-aYWHomxFv7ohSWi_0vyinIr8DRIekWzkHt5EYR1L5Wfo5Fpdq86X2AUk_2bbPNTjlcQlBzA9k2A1M2OE1XPSpBCWD24g2xxoo69er3hLMmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ZrVpYdmFTifHxknPW0xQs_mglviK7fTOKMJHWT4oW0fXvafXh2kLfXXobSjaXcMmdd4p_ofzwlPrp0rzMyQAX_60UhLQ0gP0JUgtsWWzEnS0cCfc-LK6AYiO26SMv6yDtlzfIF1IdNLgpiSlwZFqpyYwwh7pFCihM87MvOBpFLJrHG8xaa4Bp0dcODDTAkLtmaM5uvBRvR6a_FdVHkGsdlkOvLb1d850BfmQ8lxTOptfQNDCJvzyl863Xqem0HxfgjCaWu82aXl5eyxEpdXBeIhtY7zHS1uHP81_TIDWLi2phiLTi10Cuaw5txkoYwXBoKI_ixikKWPDjFojZkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFekkDb67Hf7u6REd4vOf2S_tKSINZJ091r6izWocb8J2801agmWSvs6Jbp1qmijk5sYAPJzoIjHKMlMeWSWR4HXzQHDqMh0oEOL-GJsZCvlnc8dvtkEz6-HQR0izMXvPbfo7uMpMpz--4b17PyiyPED3Jor-5vtTK9gthNqIcYVlbqUwZMJQKX_7QjfAwtoAtWnbaUfqn0fBBX6DPujctmB9RV-2bMUM48qcmxSKbuvR9LYpUgvmkfszE_iJkfon8Qnd4nROm4cBi-ctpNO3RLvFnJBLL89igps05VE_Gu-Ls5RSOZ7iE6flGwrAoy2d5Z0rBAMadpjBE4cGFoIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM7U-yK15UvpHNh4AKCw2A2002iN9uHBPRIVTe9FJ9ly8Daxjax8ert01NWYLOX_UVep0AEuhMHzwbQpP6Fj1rGBcBPrdIIpt0nMvPpcJ9Lio7zjavMdvVKfEAFI9l9JbnajJX8CXPvZefnCFVL2x132564KXNlzMVyKttg2Z2q4z8qLgef02jzXUTFLXgUUSSvm35_cMArMWFTs_1EgOyEe07VOAhFUCM_sNAynOGCw3J7mHAG03u7JKaNtaSVVQbxt1Oh6LrsDK1dS-JWg5T72df34j74bw40hNUimz2hnyaRXPw6HQ17co34lBN0nQGIlnErO9sd7z98vKt5DTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKz90Y91NL4PLvibcMqf0MZlDU-BXm8zVu4mJbs_HE-PlujfmduFUaw8EcONMWpn896BnIUymfugDJeOEctfqG0vmfEc_1E4ICtbv0JDK3e38zDPjthI3MQtOJIaO1lPZpZPKHMqyX2E5yxAPwrv4GXrJNDN7Fo9Sn12RT_oXYCwDhI37ohTROEjLYUn7Yu6qnQfFIKQjAzhkaxd60Sk8CE3cRZ2CX4V-1HD8OJ2I86_je-c3tbA8HUHlVNr8qzTEZ9CLJgY0gI9SgLyj6At2jk0jVO71fwc-IN9dWIf8ulNwrl_XIdRzwjDROFlgJ7S-ui0PqEV7VnxmerA3kEpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn-P9ClHSgdBEn2YBfU229N56hL6Zi6ZQdVZJ1SUGz00E0LyW3nb0KfjvAo5ZeKA0w2cVJ_KWD4PGtY8tJTd7Zjtpe-a54q1Avv7Jl2E3oFVMaeIKp7zIRB6ZjMMMrZ4lR4M-wS9EUZa9Mp2eja4hObE8owrdDDfgSyROnLhKQcGjDg-OQOoGtLg0ZLDmiCCLKJu54gYWRGorL0H6kbi5qPv6Ueqz7SiPTTssKPwkVieI7dNu0qfEDDcBRCb-dosTwcCanK7p8878IRRa-W4UJDydhSLNiJN2oQv7B0bQ7G9U8usZFub4SDlgqnILVsNDUnTPPSl-Oo2FwzNaF2upA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Tk2c_nMJFKforT4LZFsgqb7iDYhMNWbeLlDNVr_4ljrWJ8_KzZfg6V4s-5oSvm0pqhKdTOHdERI3wtk8J26dFBcDjQ_GZkSSZJaUnXqO258gKnaUDCn11GsDsLZr1Ywjy3KGGTeYQXKH_CgWoNITKMUVL5LCx6asDfVQvUw95LmW55DJoIcT3x1zMCQdDZhLdEpat84mfhGZPB-3eEZ6FgYrl81xD2G01stLca1fVrUpQCHsZ0CDi0afiVEu2FWui_O0uUWw4KRlTELLRWQ1cN1sV8VDyAR_7qCdR9iif59ODf7LbfHwmDhhmA3vKSJqO0ncDJXBXi0-osLcO9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBbulRFI2kbGjkaA7giGklg56fEYI-n8NyNBoaNdsivXwSRH2DFCeO7XpDiCHUxZWeCBKViPUXtlYa4Huy7pI09yGTTkGvmVW9YTxpqhMdR8Sh-7Fet6Y_5a8985RcU2IxFchrZpfuqj42PrWaVAqg2HVhuAmWs-yVwVyCeMq2fb3KIP_0RJuQX4PrmTIGq9uyAljRulURyYXYloz3GDlnvojv0ynX9F7ro7eABfyWiQARC7b4fcdzSAGVI8W4Zj4NYed0CTmZnNtw7tMJhLjo6D36erCD8WoQOJiJGODAHY6ao_4RtK5oyc0UijnRd_iQ5ToYesnJWOW6BuQ8hKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwz9IQqDPFrqLuvFL585slubPFVlHQJzXItyBnvdQap2weCe8fDgrYfsxuJ1V2uDE2jzcw-afWHHwXtmJJjeIhLLvrUv1wLEdQoQF3py3ytZEIwwqWml3XR9eSC1vHVZxrXKmrP6tk4MdUSnQnxLs7oMzCXAom5syi2EkKRGstI85ikzrsX_lFcyyyRmum3B9jaW4UiKfpg4zG-6m34eUtygSfz13jwibkSSNB5ppeDYG6OxUjOV2B1dLl8a9kR46uWyX9FiQq2l2oWg_gl9ut02hV_a89cLj9Yl5Df7lwzMsIXP4hwycNLmhuXyI8vgxwiG3st9mNPWkQIomk4Qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=OsfWXSFLKsTjLj_ksvQ3fyNpbdJcXaSoxcSauqQBfoIS1wqSr99rnalyaG0urxck-la9Emoccs-OcXDVg47WBhwqAZ7WHn694I12_IE8euPIPe3hTpGu_RRuxZKjgQMH37wTOJnmfMTGGMzZkFo8cwRl7oJ6WOUNIqFIFktWmt1w2OQ2zhgyfZq2Kc4YLt6ewY5qAUvBBh8GlPoiREQ36-GEs3W_skecQgkeeeRm3E7P76zTGG9tBNomTm7yLz0E4eDWmwAlfWQM1Ss6fD3oxD0V5FT1rDusNZjOaEhQYwDY4qIle2eFHhaMGwCKECg40jwW8E-iJRGWZNGomsBidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=OsfWXSFLKsTjLj_ksvQ3fyNpbdJcXaSoxcSauqQBfoIS1wqSr99rnalyaG0urxck-la9Emoccs-OcXDVg47WBhwqAZ7WHn694I12_IE8euPIPe3hTpGu_RRuxZKjgQMH37wTOJnmfMTGGMzZkFo8cwRl7oJ6WOUNIqFIFktWmt1w2OQ2zhgyfZq2Kc4YLt6ewY5qAUvBBh8GlPoiREQ36-GEs3W_skecQgkeeeRm3E7P76zTGG9tBNomTm7yLz0E4eDWmwAlfWQM1Ss6fD3oxD0V5FT1rDusNZjOaEhQYwDY4qIle2eFHhaMGwCKECg40jwW8E-iJRGWZNGomsBidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaHzamyHs0UJMM_KQQcgI4X980g9BlDbx0bNrJHEvmmIk7jB0I9O_g74TccYrapl8zXuB9LT-4ebyZJrYRBW1fskho0fK3W8WLsCVGx_wPqwmLFPHIFBDq3J13Hzp4xfVwI43ol68U-ZnozS9gOZQW715DjHTKmisJrLY34Nm35tJytm-tbZJjLU-uIJxAi8LkCzdC7jvzUamVVFA3_iroDHd9UR4RRv4mqz0hWk23msAx4LYP9IVyZQgmgFWe-syR5oVS9ThGu2DShtFqa70rbIbnHR57xxAzsDlIW0a95EzRs9XSHR3Z3In26PlqJu6xzXlCNuwfKhRoAXA_RHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZjYvQyT64fYvY-OvmGUyHndAHyuXqOFcLFzTE_OG_RyBvYI6OcYg2H1M4ssqiYa3-o54IPwNDEG4DeyJDPHrkLud7knYWgrrdZ6NVW2MUplJFbZHtNZakyZjEsPgmH4GZuFVVpYknWPe20fsKlca2eg-EX1LZnCo9lPPUhrKr8hrcVgLupHW-9dlE2Faxj2h84T3V4Q3JX4L3a5ELyehIIWolNj4RG71RdQ-FmRAcWCfOmeKHe7O-sCtXMnD1ufapkeY9pHTT61CcvGmPvAk1ZfV17LgT77ZIE_zFeet0nby33q43bI60xEZQl0jQBdgTO5gWkPAHOiC4SFAMSMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=HL72nDyKvbYqP5dy0nGcuY9_bywcD6kvn-QEni7X5A3d-TKuA_28elw6YFAs4SMRZ7hYNRR17d1n-rvXSlCpFCXDwxtVsmGh74Hnvo1jU078UmtVKY7r-5QLXm1wKiU2lfCsL-7lihjxLkweWAi1c3nmpfI48xDSVeFfBQ8tK_lhT2vsgwcGISeFdrC2AKv-_6EgCocypp2d4fxz5cyhoPb66hj-20zsKwvA2p3h9mtfbOnDR-xbEHsb3iLFnex7G9wXBRZ1NMkeqClMa10kzML9wOgz3qNBWbPwlFAmZCxQh--d91LgPZWlDiEM2K1ROS3lPdqsZXwhoVBIIuienQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=HL72nDyKvbYqP5dy0nGcuY9_bywcD6kvn-QEni7X5A3d-TKuA_28elw6YFAs4SMRZ7hYNRR17d1n-rvXSlCpFCXDwxtVsmGh74Hnvo1jU078UmtVKY7r-5QLXm1wKiU2lfCsL-7lihjxLkweWAi1c3nmpfI48xDSVeFfBQ8tK_lhT2vsgwcGISeFdrC2AKv-_6EgCocypp2d4fxz5cyhoPb66hj-20zsKwvA2p3h9mtfbOnDR-xbEHsb3iLFnex7G9wXBRZ1NMkeqClMa10kzML9wOgz3qNBWbPwlFAmZCxQh--d91LgPZWlDiEM2K1ROS3lPdqsZXwhoVBIIuienQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtvH6Hb7OLKXpWU4j68Otyx85uiNIKeIDGsXaBzfIsM153Zmn0ggovbvTzfUlpIJsedbKtYqFVZjJpJD1EBauxl3kS4_pagGh0WQLD-ngH8ZfbiiHuJ9k2soM-8yNZRcttX7_CeSCXyIdssdFeVXXtT2shYxvnymnyQc6_7zgFBdXYn_jwQD3m0VDhPNdjj97Lfk4beSRwn-cg52yM9Fwb_xQbhGywhrBAVs-E_phf5SXOTsUE9O9MoZRmJwLa7z92H9sAdmtmo4n-LWoyN73HoEiFSCskdxeVD-JIVFLzNbNklH9Sa-vk2CRt6svYdDvLo6PyFzyxPeZVFOg248hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUmvdivHkyQ5V0PkOOVojiPgv7ecc-YSDmUmMtuYyxTGrrnVWKX_DpJoAJ_4PeBj6Q3NmIHl3y5SU9BZjzwB9JaeJR_nbtRTXtccaGb-GjEAO330773FlOP77hemOQadk_Wzx_8U0zCIwvDC2W-z2ll9jvU7r8YExZ7NWSSKe6qJlGoEyWe6xQ1KcrbF3XqxxNJnnOtVriqO2YV15Fg7Sd7TIU7p8nFtemhVpDTdA029IAwhHf1_8dQyIJRmNyRbjNn7rUuPKhcg3vBLdCuE5v5zGqL4muLHPNOtKui3YRfxmOfyUsElnVWvzdJCLYq3JZX8AJ63uCXENBT8eSI91A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=dDQWglvvHLEnMsu466Drg4TOvYfqEn-2oqB9-GDvRip8wmtr_T24BRCJdMrMthlGz6sYkiy0SDDCL9p8cjWI_nxXuQAh_lZ3zaq34p_Ldic3w72sOrGnKOBvw8YgeZyDtk-egug2ZxvahwATv_BFw_imokXcrvR7V-5qKEHbcRghjtbDtbH3jY2egdSYSkhhxMh3yCKSZNIKWp03AZgj5JZ29RFCX2B4IuVtULNRiIN5TS9m7gzwh7y74fH01pgFz1vnoNOjtC2-mMGmS6UHjb8c2JcvFfDH6pVaVUCJbc4NMLjUhHSUtwTq17YL5LwoAQsep444q_4MOFyGf79weBRB3CHCqiimtlLN_PKRoQrRnxX7mEwa5ffRUjE3zlc2rPtN9-XeqDlRsSCPzu1FEl7Q4I12OMpulS5zAO1xhuzlbd96_FAZ0ONRmdMV57e-2RILmNfYz4LEI6hPlNDz_xX2q8K87HOsSlO6Hstu1h0OFPowsu7Bb5EypjVpvtv7C1V-8WsbXA69nqXUdCLWTuIJ-i6DS1cdmCGQGZg6l7DyNm65TAvRfXFjcV83ZHFPOtTVXULqv0tYmgGo7Hcicc2gE1pUTWpiLZrfJu1LENZBFyCt_eOHSUdepGbqPv59UnviEN6lD_Ic6Ho55u-aZAoxRpTGjBGvp5jbASyVsEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=dDQWglvvHLEnMsu466Drg4TOvYfqEn-2oqB9-GDvRip8wmtr_T24BRCJdMrMthlGz6sYkiy0SDDCL9p8cjWI_nxXuQAh_lZ3zaq34p_Ldic3w72sOrGnKOBvw8YgeZyDtk-egug2ZxvahwATv_BFw_imokXcrvR7V-5qKEHbcRghjtbDtbH3jY2egdSYSkhhxMh3yCKSZNIKWp03AZgj5JZ29RFCX2B4IuVtULNRiIN5TS9m7gzwh7y74fH01pgFz1vnoNOjtC2-mMGmS6UHjb8c2JcvFfDH6pVaVUCJbc4NMLjUhHSUtwTq17YL5LwoAQsep444q_4MOFyGf79weBRB3CHCqiimtlLN_PKRoQrRnxX7mEwa5ffRUjE3zlc2rPtN9-XeqDlRsSCPzu1FEl7Q4I12OMpulS5zAO1xhuzlbd96_FAZ0ONRmdMV57e-2RILmNfYz4LEI6hPlNDz_xX2q8K87HOsSlO6Hstu1h0OFPowsu7Bb5EypjVpvtv7C1V-8WsbXA69nqXUdCLWTuIJ-i6DS1cdmCGQGZg6l7DyNm65TAvRfXFjcV83ZHFPOtTVXULqv0tYmgGo7Hcicc2gE1pUTWpiLZrfJu1LENZBFyCt_eOHSUdepGbqPv59UnviEN6lD_Ic6Ho55u-aZAoxRpTGjBGvp5jbASyVsEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNuY84aY5OFydlIbh-wvmTU5V1g68f2RowJ5m-2NuIzqRtlbWW36VfZvGe2edaOJIkMgEXK1HiDb9IyLFMrXV4Or_RfDBhIOSfIBUleVg9CfxlgOlEnYyQEBHdIHaiw-2K9hicAD-iAHjcF1ArPdu-0HBGHr4JAe09Yw91MWmyUzbBZfzdAxFILmfFhxwY9TYOasApM-hyt8n4yNcvWa-auduMHm7wVpnSEQFJL55Cw1XiKASVdQVdmWp727VoxfjV7jc9hqxp00KqRkcuMU8HuaRTcQA6RWFuazArQKpjsAaQnbsbVEPOore8T0h2mn1iSuxfkzT1LxQUrpgVdMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=AdB7f9yYxHlNtCMulRoRnwjZL0SzXT59ZhOjExc5nUPbZ4kcYDZujJooAoN_S_yLc3xaFnBJtmAtIGrQeaEXYvS6ogNGTUTWu_lYSsduaTxg-zQ_AMiwxZ1aMjJxXNcrdVc4M86R1A8VC4JdTsvrs-zVel-ZeOLN-znsydlMHLNR8CXLbMr_MYGk95shHYOz7ccstEXmC8-lWjBPhBUhJ5GiYY5eRhk2AHw8e65lVd5IbVJn_6AoRg5j2bhc3Mz2bGktIKu58Y-PcksXq-hxre5DXBqwe76WG78QfnR9cUNc8rBY2BYwtRxptWWPCsnQ8pKoWcN4p1oCB00iA295sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=AdB7f9yYxHlNtCMulRoRnwjZL0SzXT59ZhOjExc5nUPbZ4kcYDZujJooAoN_S_yLc3xaFnBJtmAtIGrQeaEXYvS6ogNGTUTWu_lYSsduaTxg-zQ_AMiwxZ1aMjJxXNcrdVc4M86R1A8VC4JdTsvrs-zVel-ZeOLN-znsydlMHLNR8CXLbMr_MYGk95shHYOz7ccstEXmC8-lWjBPhBUhJ5GiYY5eRhk2AHw8e65lVd5IbVJn_6AoRg5j2bhc3Mz2bGktIKu58Y-PcksXq-hxre5DXBqwe76WG78QfnR9cUNc8rBY2BYwtRxptWWPCsnQ8pKoWcN4p1oCB00iA295sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا؛ سومین پیروزی ارزشمند و پر گل شاگردان مورینیو درفصل‌جدید با درخشش جود بلینگهام و امباپه.
🇪🇸
رئال مادرید
4️⃣
-
0️⃣
مالاگا
🇪🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzfuEBlVhW3ONawUi0Ah8gvhiuIAqOXJncnD_2Y5KdtK4QNWI2KUaAT3XOyWXZK2hfRmHqQQhpjiadF7V9IuZhcVJ2urTc8Z6wgzJa5Nv7JkpqRi3VpozfWcLTP8WP_TwyPuSjnKuS33Veqfx-4NPa1VEb9ULHQ8UUDJo78ga5yrzXPkQux9kxjSo3BSlkpmcswNhpF9KkaDiTV4dkiam-ALRMi5MZCTQxDcJe5BDxRDBFIvWuRnIeo1Uy70C-3tRaU3jnadXW_Wvk8Ie1EYV35BI_kAEzowBe1UI-jezScV1eosoMJLX9SGZXj4lj2QvY0PrwUgwXojY38Uc0VF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTMc-zlvYOwujJLbgM29UCR1oOD-klRbkk6GWGBACJAVjGrZE7ZVW9947yItZEqqMPFM0ae58gQKobdVhdssaiIgPScvpyTokJFS3bWC5pkwRQxRb-0EqBxxf_HhoPt9xujjjU1bXVH0rzJ71VfcGJSULWtDFAmfluUWdx8BhVwzDdF1NqOkuwZ3v2jzwn-bpWcmDIUpB5tl8xHX2vSQ4myBjcPr08pg5P3J5ASVcWhxX-xxkII5r9z6U6cZx3DKcyXTnULX8MdMZyna_UVU40Cc449b1nP7T4rLpe-gx1crzh0NA3HYVuMRn3e0UJ3G3OlsmgaOneGHBL3Crc1bdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd4gqin4c3G2Q_O2ZDUS_W8NWR6NOGFzvC3RdL4N2ORyJuOZS5J3QhBOf5y7uyYtp3DFzoHq_c9zeKbt8-gH3mSNyrM8A_jeqqZNYoxLZ_FYHohwNYAfw9VHOAHt2fHqChzyKc9MuMb7exNNZwDE1VkgSGvfAnLuV6FbF2ne1HVNxqvhP27dvZVbz8QKWNopMIibV6P5cVzLfkk5pRFuhgZQ85A9_gEY5ZwzAfpCruLeOrAFB74yuqIh7OvAwjguVVr7y9IVeZZF5wurryn93DKo5oucfO-qp_-6cqXGwu0LS_b9UYtzNiVVqlnKbav1HQKslRN6v4eSwE6QIKweiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_6T6muNFu5lggb7mBCjyA-IAbHw_6DIO8bdLkznCgyP1o0QkKAhMldgB-D4ka4nAuIO1oXAU8y7CoNFUplyZQbOLnMqCHaCz6d8nDuX4xr9QDge4v9Kn2aIhMeX8SfdYtTwOzRibu3xHqhjpvF1892OhuHJZUJLO5NqM3KI3SR_l4qdUpmbAiXWB2XrYaEuGVWKnRD0vBUWNTtoOUZ0BAkqgTaO6eClDwtR_CF90S-UVMYjCxE6x9MDVa2Y6Fv1C5NkHVWikHPPALs7-cGbEQG0gXkgkVYdO3Hjw_NC3P-i0qsMRJwDuwKvQj0w-ZDnrf6dSlLG_Sli4En8wPEKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=uwDsy-VF3Mbv6UA6ZULu6dB2YPY0InsGluNiMuAb2kTGOI9MfrQI6X9HYoNh-bHdB3Byyt_UUCUQwoymCXY6IMN3kXcPU3YKzHemOAirT6PlFudx8Bq63liZ63EW7W_uSxJl_02wBRx9-0xxeXliV8K2OVTJ5902HFvP9L38cbk3MDx06Sbc-pQHrnbKtdMmolREP1cDcOmhVguTjDxezjwynHdrtisvz9-6W1jj_f6XBxzACtW7bHUvHRgj-6axisHzGUVu1lTvRbQIWm2EqgNslMRz5bbjTzr7JqySM8oRxaOwvnxGLiYLdkzI5gffL5rOnUs2Hz9rKLxl47qxrIVo8faHH9NcrodFhF2ucbVObAtn-BCM4Xlhfp0ErouBTl8oaLF8-3PoE47zmNN0ZTNSZfo-_jYRh1BShdabzhFy6sAPTIq6R_2DuPqYGTJYx9mRbqPYSS3E08Wf-JEy9l0i0a6ZSBp5qo84ioHdNyCS17EE59xrmgoxetQs4AfxSqF7604L1CHXMIv3D3ttucZAqOw26dMXA0foigZLGHa9usW_x_zwkN9ZpILGcUrn582Pv7hWAXh82LvoPT0J36m-4CVxzG-s_cV2KqnPGR--iBhro_OdTwy9VnJO_VBJslIKobc7xOVcQggC3HHMTJTCuDRV2_XXrd1gTEpJk0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=uwDsy-VF3Mbv6UA6ZULu6dB2YPY0InsGluNiMuAb2kTGOI9MfrQI6X9HYoNh-bHdB3Byyt_UUCUQwoymCXY6IMN3kXcPU3YKzHemOAirT6PlFudx8Bq63liZ63EW7W_uSxJl_02wBRx9-0xxeXliV8K2OVTJ5902HFvP9L38cbk3MDx06Sbc-pQHrnbKtdMmolREP1cDcOmhVguTjDxezjwynHdrtisvz9-6W1jj_f6XBxzACtW7bHUvHRgj-6axisHzGUVu1lTvRbQIWm2EqgNslMRz5bbjTzr7JqySM8oRxaOwvnxGLiYLdkzI5gffL5rOnUs2Hz9rKLxl47qxrIVo8faHH9NcrodFhF2ucbVObAtn-BCM4Xlhfp0ErouBTl8oaLF8-3PoE47zmNN0ZTNSZfo-_jYRh1BShdabzhFy6sAPTIq6R_2DuPqYGTJYx9mRbqPYSS3E08Wf-JEy9l0i0a6ZSBp5qo84ioHdNyCS17EE59xrmgoxetQs4AfxSqF7604L1CHXMIv3D3ttucZAqOw26dMXA0foigZLGHa9usW_x_zwkN9ZpILGcUrn582Pv7hWAXh82LvoPT0J36m-4CVxzG-s_cV2KqnPGR--iBhro_OdTwy9VnJO_VBJslIKobc7xOVcQggC3HHMTJTCuDRV2_XXrd1gTEpJk0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛ برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA3Quy4no9RKGD-wv2Ug5U2tIuH40gDsn5hThBUmT2uXbiGyGuZp0wac6JmTnLOghWij75JXQzqIc8Y5rhM37uug49XLfzamTCE1MMnM3LdT211P-_f9XmcrTFaHnmNK-jwKMb9K24aUdg06fVlt27rQC28WHziU7oEO5EusfFyLjeega-XT50Qdm0Ma8irJ9xNWJeOymT7b4JnAwW_0DI4-BiFBK5TArfQFS0qdra1DXiaBRSFFP1l196-qZFfCl7i6KbhpvYcYvUd6gi2pfpIC_STLBJPWGUN9pO8U_uv4A6l14fKuOSio8ThLMERv8fwm-1SR9878PwCJFrROVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plhiYqNNxAPWAxmsslokCoSnxahUpJaX_2p4Trbbl1kCTtu7cZRj1vUh8z6oR50sfPOA_SaIxiC1Y5yDugVJp5gAScMJGf_0HKsQh1G-FRT02qcYr90zMSQcjiOfwjp_JR9MyJnBw7KvnRR_XqoXUkJdByUzxhjJMwRM-v0hZd2jn2HQ6cmntXSiMZ0d_sgtNBr-OhWDa__Gk1nTlQ6zOvh7vKt4F2NIBEVeZHEPyJ2kaAx1HWvidfgvpSTDUadr0mSfjx-tVM8f0uj6pyijR4QDunWhdrX1uhEUNRpec5P66xSbpelcgJQfvkdlTVAjOfMB_UmErQAwQzM4xJ_BbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28747">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWHCl0bdZdxsw1rmGaZCJ3Juz1e-PR4LKQ2yNynCd6l3kXcV_I7mbpHgiOHKfyik42TQyWSSBoo8B4cT3NwIoywxiuEiGHx90CDtkgCiQ-OroGB0r0b4JTfz2baS3RHgxOdioRgR1orPhbihjp9WwaBKa4YQnquE8zGvkr4jiiQN0Vdzsrm1rWIWJG7n4I_FrLxyW43p-fsmTK9JmUUsTaZwSH_ovfSSF8m41tk8CwOtqxdXBdBnHaeySC1Y5Te_2M-wKiwsM29_n5hlDX0MBsIeDN29zn_9G0A8CCV41VitlplIf-ZTjC6QHxEwKMCB3pX0TfJnH8yzkpva4gAdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛
برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28747" target="_blank">📅 18:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28746">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=YHNOq-9kZ2wK_QyJWtyObqJKULrLOv_2YbFNpqrrwZ2gPvzctNoJRwjDmzvLJGBUUq7GlMKEVBluav-wF5JrBJxJr9Js7BI_WcuvrPb9POavx61MSiZVqFbr9LazMqcetPrPTNep9FiCFi-bvnT3weawMHnDhnFI01LQHzG7GHB_1nPGXTILTRURI0GYKVV6e8EgSLfvWehjmKR98KKpMuGWzx_evi4wCju3C9OpXGTerbkySucZiOP7QXDVSXkiCOn-R--5Z4PSQ2Cnu_vBjw78smfhVHk_X6HrDUfIceXZ6G56ZFafMSAC8NAnNs5XSAK_CAk7C0CVCzyHzMJ7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=YHNOq-9kZ2wK_QyJWtyObqJKULrLOv_2YbFNpqrrwZ2gPvzctNoJRwjDmzvLJGBUUq7GlMKEVBluav-wF5JrBJxJr9Js7BI_WcuvrPb9POavx61MSiZVqFbr9LazMqcetPrPTNep9FiCFi-bvnT3weawMHnDhnFI01LQHzG7GHB_1nPGXTILTRURI0GYKVV6e8EgSLfvWehjmKR98KKpMuGWzx_evi4wCju3C9OpXGTerbkySucZiOP7QXDVSXkiCOn-R--5Z4PSQ2Cnu_vBjw78smfhVHk_X6HrDUfIceXZ6G56ZFafMSAC8NAnNs5XSAK_CAk7C0CVCzyHzMJ7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28746" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28745">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il5Wj5DB_zrSRGswFdI-W0qgspXZuvdBt_RtLvob7x69GE_I1bc6qDd5t-hiAhD9X6XC0Oym2_mIGBSi45ZTlELja6W2eedyq0sWhiu-xUvmvkAnFDOjsSpPgJYjHxLl6R1EgLRMfj2yWfKsWSKB7YTPpGFp_uuAk1MsCrHVPB6ddmD8QxdHlAFMJQqEJG7AT_fBBTqHcdJcT-daDkQ12dUePhktjwvHMQLrqORsJ81Z33hsUMvh2xYw6vSNMb1yi3oAcd9weH9XE70ISQe9U_A1W_T4SjSYmfUYTERwdxTC97tYuQ6HYJOXmZoXGn_msCvIo8dmIN6ezhGYJ3TvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28745" target="_blank">📅 18:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28744">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUrvvTAtPyYy6pzTzNrdZYyXPBciVWhPGn2HxuDX7D9BUteGcejhBzJsKAYhbkb-MeXoIiHl1nD6fKvgZwRjVHc1MjVmABOud71Fis22bxWJXb9P9zELzMJBEiqZiZ1xAgSdPWnzc-egpkzokjBKItATkCql_yxKTD1tTQUgVmGqlF_Vwp-TEFK7BNlmf32iasZ6aKKG-gku0d-l-I2DKroIhVVUO-WvIK4l9jMIB2-czr4aIWrzoPVOb3_3MbX5ZQBKAWmMLZa2rvqQWMOJ4OYlKXGtFFBLDDMJc6tQpsalXVVZJyu4t0xLrp6bJZjMQSbNzvAR-0Jac9mi31jfJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28744" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28743">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do58Sw5mQfHvm7IKAUSxzRHA81HClXffVTrCbWnYoGMSqJ56yq-FRznbQfLPDEskp8n4JFyQI123c89kY7PVz_8Zsk9d1AgS26G35zrZPAtKmJ9g2p7oPlj7GEy1ABrOvPkNk5b_tXMeWxW5y10bHpUNytN5Q0e-oPFNXDi7qQLuA2ot2SCn7R1tad-XaVjNlN5hADUcXZODLmkfHEi9ROIlac7R-3rlT3Eszs8YOyUWMhBo1ZkVnJk_CS03d9_7AiTyQ19gQxBprDnb5wWzxijStmgBqOEVeVo8Eo4BFyienlcQOf_gMZhYVw8_rJ5VXqWmoYz2OgesxH97QoWQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28743" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28741">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRJh9rrQ4Ogqy9hDc45zPoXdZrrET42b5t_UowC3RV_FbUiL7ZNL9K8TV0olI5YcXbEi3HllVm60sABI0tyhrLeFdt1P_sFvJYnZj__8Yl43N12VQLnQqV6MR0nXqg27qC5ylSXet-5AXqOf1AkW6UlzDIg6dF-byEMnH6YtqpbW-EWcTW7X_beTJ9lWVmqZWE88YKKgs6m2_0Gg4gjbLyxx83tCI7CnHQZX5AFvBJqUufASvl3BVAxMni6rAiOEL0Sp2Yk35OahnRsf9u8bvtMSdbfKMh1Scv6MuMJLp7aj_EjQhg6CGmr7qeA-QderGbNmcvR1vywzKEKACBcQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
؛شماتیک‌ترکیب رئال مادرید برای دیدار حساس‌مقابل مالاگا؛ ساعت 18:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28741" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT-sCRxA6hA2KVQQFgVYfth3jAV-9kZ8oFKmbPp7hiS9tFVieiBzzaoOkRFqQSXxaL6abjfmcM9IT2gFz0GtH3gabvhgmoEIWGcdea60i6syKgmyZaATgfszWWcRDm1AqDxS8OoHUqh4E73NVCUV9hkuVPry1lhxiT0PIVpMOqGEjsWbfhJ21ZJ7j3RTYkwpli0DNwtq1ShFrjWEEwL92yqA_V5GI0okkB2PUHRXN8NLp5AvMxIyvDD9iK0T5YFBgSdH2cn_jBVeiM2C9b_jDUMYDvTSTNr8lGhtcQkfBNfcPN-dWQN_nKLB4xQ0zBvALq_R5E6Nb7yEd0sLYqqmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gplA4EDERLYBsWcrxgl73SclCxnxJ5VLey4_m-pRNegCOxmQbSR8IeeHeDT-FIuEtmLRGUJgsd5nzjrwl2t9V74Ka-wZlFGrIX88wngNbM8m7CUc6OCA3L6eeI2DXDP4JEDOozGgRGlhPf_TF5WlVkcpekugPq2j9mi8MzDsYkyDhH1piS0WTCJpnVP3ngHlgqRTaRXPp-Nhq-9URwvpsxmGwXCSinYSM6Qorvhp989Wp2F3QiFR3pyKw6b35hO0qr3jXk6WXq62N0q4T_YiRRrHBrHdSgOQJnv-IUpv5dR-14kTizsuRFyIbylRcAjOzbKDVvVtkx0b7EkMgf0lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgwsk8SyLDrUiJKFL-5_Gfaeuc3x07IuU41AY_d0ZYZdJTC2YEa_RMPDS9-IHHSK4fmVAJmEOkcoHI169chnA3m4aKRP1e-eHAohAiCzpccDbF6y_aiicTbB0YN769pHbSjtapK3ZuNnN6hUlM7FJwonFqYuBkML5OqozPaJmJr8LezRo0XpQW-TH1Qac-6WlJxcO8WBbQ2Otx0a0AR4QK7GWDyHmubJN65CcFdH7cGuUnAiVGfmcnKH-LrpUUPQfLC1_OOinH3lC5989ifkWg25E92zyNE5As6Ur18AN5xEGu4hPmvhV1ChVKA-IX6IXN1IuGJYEy0t8vvC0-rjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErxGOOGpi5h33fFy_qOGScBWs3fQ6rwrtXxqiqddF2XeplmVz9eoiTgYSzHlJXV8L9DWV-ybuTYXmmz7dE-7-ROtcefK0-bOJk9VDffSWWSa5-1YcH5yghv_fnztKDqSVzJj-nQvagCcTm7UH_W7n_QGTTI8F92Xlc3vDzCEhUbHVece3XqUpn8kshV5nic9uG-ulOzIinI9IJEMNV_3TLAKiW2KEpmFRblUulfNcJvffeEpaAf814_nugkUv53pCUhIGex6ylXvr5cwDi_Ow9-RhlrJeQRJyJySWVtObF4KbIZaW_Fv4bd9iaxsIIszB3wheDhRVXgYzpF4KqqQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfCy1o9wXkEouvDSWyoP6sFXkYPBn_A8lDujK9XOfnAEIT9HoMlkprfy2ksaXGkHJrV9QGPE_jmrWnhdbtizejWJ8dEX34tu0DvT2xRqC9zm7R8CA9Y2Ve02tYTzSpNogt6Hykw11Vjbaesxpb2-RsF3nfmPBSSWWgE2YAQatxKLANSl7dc-yRwbrdvtmldmUSa28REGoDLjaMmAV_HfQF5_9f7wavczHrj1HXy3S-X9aBrM6_3tPNyTAsddKBO2-Vchqffb8ZcyP7EZFrI46bbaS0SvWQwlHaljEnIYgmS00q2txqpa53OsuW45EvMC8-qLBlEWSPVRIQxA43uBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEIwkZ8LLDHLgE5lndPc5AlFZruLt1hsPZazDCh87DBChSs0jW6WjFtZfUdiXnzaD9AzGHAgnEnr2NW1DhY9ULh6elqQakpSkpeUka1Y9_XQv0aOELpHK2vgVs29jqS9en_u21a8OLyy2vz38D4jdl6Pj2sXSB19-6MXPMlsqg0FWhkfkEAmBEXbNeHwfxMj8AOg5pHJnl0WmlL50AxAcxfm7TygwCWmXCrkhGTQtqQi6qba0U3578D99LM0XC7JDKslhwBcAHX8qSY7Fz_iuD-4HttCTqqVc67z_jDe_BEAzfp_knpNHcNZibT-Zw4dAMIAntbeWo-diqO1Xgsnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgfdBo24RKCQea2PijPHRWfG3_WIsBPMBNO5KcmqVA4vi7Z44lO10pOfSx9dUh_Z-JIpecvVSQrBXN-w5Jywt-1Hp9QDgffBrWsFHzG2p7tetDQTEIeKoe7zVHbex_GEv6nfEK76pxNt0oEiHRJUFKKmgyOg_C_0FdrOdGO8dwSZ5DZ__w7lDTyCBifkoXNm4fvGRY5MLD6hj4wrVIykCxCCIqKQKBhgToktKtnVA7ZFREi_xqqAdhPP3ZOADObp7jcyB0XgaGNOQkbFlR-WISPqRvABI00OHSNT9ZzO0Vk9OqXNL_TMoTDzwnIWdCt0gDsbq4w6thfnzSBfBShT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbe0Y_wkMhvE1QkJD3kwrx732KM22oDkNRy5-PLEOZqA1T3ImjgVt7mdHZff4GHaPCuQDFE9UuZ_mdXNC-_6WG4_Je3bBlUbV8h-yiyQZGta-WQ3XyY77elUNt7FWF2U5zbybxKRdwnhA0c8temBrY1S1hIBeBiRbjRMDKA6lDfBtoXK7qkBWA-80L6s8RYxhsVKypdYTX7jDV0K-ZWALk4_su92J7NpRPcAQeMzr2VN5X8TVDcI3LWhnjwd6G20-LJdOJhkxKaHDw_F_D0RIqlPqfEplDASHrnwjdvHc8T28ZBUYQZ7BN1UDprmFS6qzWNX-cP9hOxmUUSNHZGjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvEA4SCMWm3Hv0KYtUcFe8MAstBPc82IRssSvTUXpdfmQ5TgKpZdXIpuLBC4uiQkoDKrBkl-GZWonRzxIXdkj-iaBrlBpReqcQCHClh7_HSEE3ZS9vLTxuaeLzoAs3OMR-VQO_gD6jGMfsZBYBaV_RvPzzkDHQJbNOqEayYqWy8cQjO1ZkgAu4Z6EAr9smjM-jq2N09uPayM_REMe81mVmHz0g7HdskLEXaM_npNDIn-F5E-Qg9mA8yxCrfceeguQGf-C9jF6yY7tIYNlYw2KMKFDsGXWHz_-ouNKNpOA2r4gTYZfj3RcyRIyRuY3WJKQVe9eXTMLXrc_SY8SF74kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5hcauHXTgMrXh1iepXDPbt1ZW8pdLhGKTUTe6CyyA-imfcR5rqgIfKbKDAqVQTBermlquYL30bjWY4RZ7bdUkn8vMZP--af7UqFHjZRnXxY0N_SEV45fPU5GViVYVKdfukVv1Vi58tOMpqzs202yArSNRuaOo44alcmU9GZcl9bkOxzUk9kBp0sHAQnxjAct_z0FkvdkltJQM_rU6cVN4XXgUyD3qCARFdCWC4glLhubnDcApqrLkFVnYOj_O42HKphtHFjDpLqRh7JVqBolvqCSyT90NMWcCCKEjz_N-RjkaJmujd4BzamNBI1xk385UgIGL6wRk9bmZz0nCDqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_yOcFoZKYumle2ph8vEqSxTuxabfKyMfinypCGKoY6efqvcw48zC_dxukcQ4Tz7xuQV8jtWUhPc_9vfbCWf7dLKCZeXCcOxkMpjTs6f5GpyluemPka6jhx1Kr2kaZ_6s5mBnmitDMXEfFh6ykjXo4ZLarg7NjuEcMf1PJQiMpjWiDPEbyKAXAGEaT2G8p99qolpiF5CWJgppgsScqua_JahqOKL0Z373yPGIxhmM-zA_xOpo4uAcxbGIwmadVb1YHSlUmVb8AVs3ih7BWWfl3Qeres7n6MuA1XUbkZ62nHU4ODakX9yplRSa5i5oAmAjcEEKo0eh5j5q3aNtZEyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9bmql5f-uztczo13DAvfaLM92j1fckVYTH-vt_dPzLaeR7IomPIXOsxs1hl0xZJEbH-HqEm13AJOzGs0ES-1YIvs76sZ9BeSYu6D_c_Ywx5qRKbx17Nu8dEsz5wP79Cf2hsDE3TCm48p6bwWZoMiTAATNQGJcjyzimWtGcfNLuYGUKWx9dVAI1WhwtHd1kSrIHS_PgThkJ8tZUuzqgNl-bPBuHgRdcvVGEWRPok6pwc6IZwsvbvLIuii3eyx8YGk9O08LQUNHfcRKH69lCasml6f8ng616kMFnkJUoNAjaQFdKMHXinKsiNhGizPD5AR28ApGwsvqUkRpbB09NujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=kMMOE2CqtscaUOghq6PS3xgtaHACF_Xcw_anl68z2fkSituS53Aa4OuwqLNjxaD5i-eJ8p4xm4iw6gM3FAJb5Gc5OLvk6ZABehJ5sF3kBl-en_sjO4wEtyYrh1O43sjBFncz5H5xDA2y3rvY5tPbCxYmInVRCc8S_27nvqPfIITGAGk7m2uDnc0dgC0ma_DdKFkA1LDza9jPfDM-_i4zNLoN4zO_q9p9Zn06LtnyP1s-gM6Yn8CQVmzjMwPekQthIcb1QO1fLJKcE6P_e2n6n_UeLfee7SHXtycaHBsUqECbiBPjIbSJvb9GLaRmfSdx7Ugj6sqA4AdnL2xmyrpDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=kMMOE2CqtscaUOghq6PS3xgtaHACF_Xcw_anl68z2fkSituS53Aa4OuwqLNjxaD5i-eJ8p4xm4iw6gM3FAJb5Gc5OLvk6ZABehJ5sF3kBl-en_sjO4wEtyYrh1O43sjBFncz5H5xDA2y3rvY5tPbCxYmInVRCc8S_27nvqPfIITGAGk7m2uDnc0dgC0ma_DdKFkA1LDza9jPfDM-_i4zNLoN4zO_q9p9Zn06LtnyP1s-gM6Yn8CQVmzjMwPekQthIcb1QO1fLJKcE6P_e2n6n_UeLfee7SHXtycaHBsUqECbiBPjIbSJvb9GLaRmfSdx7Ugj6sqA4AdnL2xmyrpDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
