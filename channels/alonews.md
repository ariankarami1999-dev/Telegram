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
<img src="https://cdn4.telesco.pe/file/arViCvswGiuJrbxt5iQoBfah-JJsuKylYbupPHyKDhjc2m2-jRGgl-T-27JmeP0R0CXMfi1tfMGHQJzMJfX0sRHLnyvIw4yJwett0aYqSA_4nr0Jir6NfyWXzXl1yTba65iSHubQ7uFEFcsdY97sYjYkKPXR4IPnQuSkkEv1Fl3t4cBgbZT3z3desD_6vEP0WnfuhzRcFznbyy_9XVI4cIQeCeD2n8yytOhVGMonyiH4a9vgqlWK0pqFvuFFuVTkVreLf6FbVSROsw9shOSYwsZ3GexcThtCAFQaYpD0W3nvDEH8NnI9nnXzc0qBbjPnfiLIE5tsnagw3ibCg7BTzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 914K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-147353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1d39d99a.mp4?token=Okxo-9yxae8xOBkmLpysvoH8huKVCSj9aB9NyL0YqA_7oR5enb9bN-POHpFKl1WGX3ukvz-RJGOGiqAIUiR4wC1p_cvdmbQoC-V-X3DN1fW8FEotCIDqdXGL0eTOXMKGuIroIu99QuQIt43_vyXTyg1sooQ3hx9mMr6_jx-iViKpyJo9EuwkPj3HoLH8gNmIUNyu-kOVcDRO49Gg2vIgdCpLoAquizFQyqhvQXJ4L8Yvx_XDlN32-IXpbPMaMbvdGgDHMkUdrckR7V95SpQ_wj6dkDAs_jJeGjVkwxsO27_Iu1pPlfESU-_jWcrr-qUfu3Vpiz0d78KjEGY51pK_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1d39d99a.mp4?token=Okxo-9yxae8xOBkmLpysvoH8huKVCSj9aB9NyL0YqA_7oR5enb9bN-POHpFKl1WGX3ukvz-RJGOGiqAIUiR4wC1p_cvdmbQoC-V-X3DN1fW8FEotCIDqdXGL0eTOXMKGuIroIu99QuQIt43_vyXTyg1sooQ3hx9mMr6_jx-iViKpyJo9EuwkPj3HoLH8gNmIUNyu-kOVcDRO49Gg2vIgdCpLoAquizFQyqhvQXJ4L8Yvx_XDlN32-IXpbPMaMbvdGgDHMkUdrckR7V95SpQ_wj6dkDAs_jJeGjVkwxsO27_Iu1pPlfESU-_jWcrr-qUfu3Vpiz0d78KjEGY51pK_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: زیردریایی آمریکایی توقیف نشده غنیمت گرفته شده و غنیمت، حلال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/alonews/147353" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9e4ab0539.mp4?token=dLHWrifoenQdwjsZnTm9RK05qePbZ11dPscFZv32QaMyyp3RO9lJxUkrbvsgFp9AZJjJBsDRO1Xp6_pP5WKGZwIggctUnczafi2TtPd6b3o5h075bs6WKFdg5g5zx2wvCZYPAzlQNscDU51eyFeOqkVNr8MBqZ7YqXjmTocOQHWDi4Z5e9Y0TgEAZVnzIiyQm2AgyhOuBhHhtwjK7DBurdvejTKvZs829nm_b2rBMjquhBUk0DyHtbKr2SMQLf-NYCwcvJwK9KoCaR6HwYgRizof0RJrIPMpllW5yxGDqFIZy93PT6Szw2cec4YCHNC8-P3NEVep_QjKYSKGfE0QsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9e4ab0539.mp4?token=dLHWrifoenQdwjsZnTm9RK05qePbZ11dPscFZv32QaMyyp3RO9lJxUkrbvsgFp9AZJjJBsDRO1Xp6_pP5WKGZwIggctUnczafi2TtPd6b3o5h075bs6WKFdg5g5zx2wvCZYPAzlQNscDU51eyFeOqkVNr8MBqZ7YqXjmTocOQHWDi4Z5e9Y0TgEAZVnzIiyQm2AgyhOuBhHhtwjK7DBurdvejTKvZs829nm_b2rBMjquhBUk0DyHtbKr2SMQLf-NYCwcvJwK9KoCaR6HwYgRizof0RJrIPMpllW5yxGDqFIZy93PT6Szw2cec4YCHNC8-P3NEVep_QjKYSKGfE0QsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «آیا ممکن است جنگ اوکراین پایان پیدا کند؟»
🔴
ترامپ: «این موضوع مطرح است. قیمت گازوئیل به دلیل دشواری خروج آن از روسیه در حال افزایش است. اگر این وضعیت ادامه پیدا کند، به جهان آسیب می‌زند. باید جلوی آن را بگیریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/147352" target="_blank">📅 11:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8Emiyp0ECggmUdRWzLRwpxB9aSeyPPeRPLBUsoYpagonN_vgM2K_L-QGx5QZ83pKJ09YVlH7gzf99Y6TBaEtog3T2u1y-w6pbxhNKv3rnGCDAAl4LmDL8ZBXgCavGf6j61S5TfC7UVfuJEQXSy-do3IYgNSsQrQ4yGTefjq4kSq0R7YVzVih6hwMS_Xda-rccFeB0cI1-b6BSNWlW7HMZqC8Ri0_wfwYhpD0AuccuqVR2sOtaEm2HU_xKQ8BGCe1geaj-gi1RtmN-Z4JiL_f-RZPOye-1u0b6D4XFXa9XT1v3RVNw1TAKLZglJedhm42FeCAel4sNARUzJXJNRNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: حسین طائب بدون اطلاع دولت و فرماندهی سپاه، دستور حمله به سه نفتکش را داد تا توافق نابود شود
#یلخی
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/147351" target="_blank">📅 11:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3c56a710.mp4?token=kdzj2EkWkSoJqqvzC5uOvT1tdgHlordii7yoLTOn92WGZhsWdgIsrt835ZjcqcfhQaL5ZYC9tlHkoR1Ecv7-0lvJuY0VraYC3qhClxgSEPdB9MbUaOHG8fHwJhcfqT4X9eOx6XWO9vph8LRv7QFDrCrER-VcuSP95F6Ai6d3GySqN4JDrD9Dt82jw3DTLWcflr2RblNkgbtrywjElYYzG9tZhxmAM-J5SBHnnvRtnFv3TMnOIUTwcj0gjxo1qTdk_7dSL93g_nrzQLtZDEu3lptCzTf0grtujbZ9pf6ih1CChPEvjETsDld2B1flGlQVVvWlM1qVE0ZoeSeCoBtFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3c56a710.mp4?token=kdzj2EkWkSoJqqvzC5uOvT1tdgHlordii7yoLTOn92WGZhsWdgIsrt835ZjcqcfhQaL5ZYC9tlHkoR1Ecv7-0lvJuY0VraYC3qhClxgSEPdB9MbUaOHG8fHwJhcfqT4X9eOx6XWO9vph8LRv7QFDrCrER-VcuSP95F6Ai6d3GySqN4JDrD9Dt82jw3DTLWcflr2RblNkgbtrywjElYYzG9tZhxmAM-J5SBHnnvRtnFv3TMnOIUTwcj0gjxo1qTdk_7dSL93g_nrzQLtZDEu3lptCzTf0grtujbZ9pf6ih1CChPEvjETsDld2B1flGlQVVvWlM1qVE0ZoeSeCoBtFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه بمباران نیروهای ویژه واکنش سریع سپاه پاسداران که به دنبال خلبان F-15 آمریکایی رفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147349" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b168f1f6a.mp4?token=KIfF1hV-si2f-HqUJj3L_j0zbwYPSg-P_4fKR5jhwZ-to76_qaatbr1xpM92S708zUPVvYu56CoVbMWgMjhS-gU_a4i_aAWLP9VvHYrZTDaagyVXNAZXZ45HF-QygYR3NCLmt20AQzgT655X-nRmMXHfOxRlim1KbMUGAbF1vRmaVAXQuAlOOiv1qMmlGyQmchzKniyF0fyLpIc-mggFCkDar_lf0MuaC3bjmdip3HLz13ao9s3VB2I032LPucP6BKVR95h337c8jjiQXrYIE7iXDf0dsfEZyH0UTwCDYzLJ_fbxWrLtRJIZ7by3DIZ8HG_lT-RpTGenC-5rPu5jwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b168f1f6a.mp4?token=KIfF1hV-si2f-HqUJj3L_j0zbwYPSg-P_4fKR5jhwZ-to76_qaatbr1xpM92S708zUPVvYu56CoVbMWgMjhS-gU_a4i_aAWLP9VvHYrZTDaagyVXNAZXZ45HF-QygYR3NCLmt20AQzgT655X-nRmMXHfOxRlim1KbMUGAbF1vRmaVAXQuAlOOiv1qMmlGyQmchzKniyF0fyLpIc-mggFCkDar_lf0MuaC3bjmdip3HLz13ao9s3VB2I032LPucP6BKVR95h337c8jjiQXrYIE7iXDf0dsfEZyH0UTwCDYzLJ_fbxWrLtRJIZ7by3DIZ8HG_lT-RpTGenC-5rPu5jwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: چین میانجی جدید نیست؛ پاکستان نقش خود را خوب انجام می‌دهد/ هیچ وقت مشکل ایران و آمریکا مساله میانجی نبوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/147348" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA_SgKVnBjuKCq2G0t2Gq9slnmr4xhdcwrNoia-CpQTneWQVAb3ICWaVGFb7yFoGSAlg3gbPGUoYlBUTzM1-m2EBxwDExBVKFhhvU8iUrz4v6KIbkgY7m9RXAdTV2_Hr4GGWnJiIRgWU3SS7lV7hSOeYmrTkJTVNVHQOiKqPwTVpBw_UOWAtdnsn7lPwp4s4FTWcdRDR3lp4Dysat-EPLFK70FX9G45wzs0WDQRhmiUXrERLcgGL44x69uzhh5RKVE7RsBpobSI22sL5yheAwaUpy-3650C2o_YnIVwos18UTHk8aB2Bj_3QxRUhEDERbABHBlKLDgPWQKOYCjNUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاله مرزبان که برنده بهترین بازیگر زن جشنواره ونیز شده بود مورد حمله حامیان حکومت قرار گرفته! چرا؟ چون از حکومت دفاع نکرده
🔴
در تفکر جمهوری اسلامی دو حالت بیشتر وجود ندارد! یا سمت مایی که وطن پرست و باشرفی یا سمت ما نیستی که بی وطن و بی شرفی!
🔴
شماها رو چه به سینما! همون برید تو شب نشینی‌ها پرچم تکون بدید به صرف چای و شیرینی مفتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/147347" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تهران در تصمیمات یمنی‌ها مداخله‌ای ندارد
🔴
انصارالله طرفی مستقل در یمن است و بر اساس مصالح خود تصمیم می‌گیرد
🔴
تصمیم‌گیری در مورد مباحث سیاست خارجی و امنیت ملی، تک‌مولفه‌ای نیست.
🔴
ما صرفاً بر اساس یک مؤلفه، در مورد موضوعات بسیار حساس و پیچیده مرتبط با امنیت تصمیم نمی‌گیریم. (قیمت نفت امروز افزایش یافت).
🔴
بنابراین شما نمی‌توانید صرفاً بگویید به دلیل بالا و پایین رفتن یک موضوع، یک تصمیم را بگیرید یا نگیرید.
🔴
تفاهم بین ایران و عمان، به عنوان دو دولت ساحلی، نهایی شده.
🔴
ما با مشورت عمان در مورد گام بعدی، اینکه به چه شکل این تفاهم را اعلام بکنیم یا ثبت بکنیم، تصمیم‌گیری خواهیم کرد و اطلاع‌رسانی خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/147346" target="_blank">📅 11:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/63f407f3a5.mp4?token=G0nAjXUdhuSzhBZ_F_BLhLD9IUMKgcIDg9Yw_ieTyyjXJYZ3XPAqdqOYknk3T8VEzHAMyuEebB3MS9cvZRpCUs_9Xlp3-jZFWAGVM-lBB5sBD2SWbTN92EzNtm1ZR5Qiv2G2Tw3Ymo6mzPeKqYXUx_3W7PqHg5sAMc21Js107wwePhYmVPVooeJN2ks68swEN9-b113dkAzng2JyoLl6zvjyhSHbbRK6p1PWzhE4jHfBESRdxHHmA-CRCsWJQh4iOFYtAqorF5GTwgdbb-ukfikTM_vMDf356WDvk5ptwCzjJdKzMNDhBqsxo8RABaot8_nX9akv7tbLKBST2GvibYyONZ5j7dG35cDNRCXVWUrx0iDAJ8Z9X5AHDEYADrHlBwDBqrA8nw1Sr87cVXiSlJhJ8XDlvNCIBmDEsn2GZU_6CXlyiVeWSn1Ox95Thn4ZwZLby__89TdDf15sL6tpg1H2WXVQlJJ2dQSEw7yAp0bNwfuP1pi68Pxw97KMMt4UWKWHHw_TED5GP6IqKS9IntacSBX-9wO3YzocJYlR3hvch3Xj5QMt3nRjiEEp0MDs174_9emLEcXrbWRUqCnvVEa7UzoP3le8_Dc4F2ipKpoEah5qpVSpyMhBF-llJUCr65Vr86OVWeXTaZaj4y5udEj3pPNeVP8orhmYcUN5A14" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/63f407f3a5.mp4?token=G0nAjXUdhuSzhBZ_F_BLhLD9IUMKgcIDg9Yw_ieTyyjXJYZ3XPAqdqOYknk3T8VEzHAMyuEebB3MS9cvZRpCUs_9Xlp3-jZFWAGVM-lBB5sBD2SWbTN92EzNtm1ZR5Qiv2G2Tw3Ymo6mzPeKqYXUx_3W7PqHg5sAMc21Js107wwePhYmVPVooeJN2ks68swEN9-b113dkAzng2JyoLl6zvjyhSHbbRK6p1PWzhE4jHfBESRdxHHmA-CRCsWJQh4iOFYtAqorF5GTwgdbb-ukfikTM_vMDf356WDvk5ptwCzjJdKzMNDhBqsxo8RABaot8_nX9akv7tbLKBST2GvibYyONZ5j7dG35cDNRCXVWUrx0iDAJ8Z9X5AHDEYADrHlBwDBqrA8nw1Sr87cVXiSlJhJ8XDlvNCIBmDEsn2GZU_6CXlyiVeWSn1Ox95Thn4ZwZLby__89TdDf15sL6tpg1H2WXVQlJJ2dQSEw7yAp0bNwfuP1pi68Pxw97KMMt4UWKWHHw_TED5GP6IqKS9IntacSBX-9wO3YzocJYlR3hvch3Xj5QMt3nRjiEEp0MDs174_9emLEcXrbWRUqCnvVEa7UzoP3le8_Dc4F2ipKpoEah5qpVSpyMhBF-llJUCr65Vr86OVWeXTaZaj4y5udEj3pPNeVP8orhmYcUN5A14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره گزارش‌ها مبنی بر ارائه تصاویر ماهواره‌ای از پایگاه‌های آمریکا در اردن به ایران توسط شرکت‌های چینی:
🔴
خبرنگار
:
«ما اخیراً گزارش دادیم که ممکن است برخی نهادهای چینی، تصاویر ماهواره‌ای از پایگاه‌های هوایی آمریکا در اردن را در اختیار ایران قرار داده باشند. آنها همان کاری را می‌کنند که ما انجام می‌دهیم؛ تقریباً همان کار را انجام می‌دهند. آیا هنگام سفر شی جین‌پینگ، این موضوع را با او مطرح خواهید کرد؟»
🔴
ترامپ
:
«فکر می‌کنم او رفتاری منطقی داشته و ما هم رفتار منطقی داریم.
🔴
می‌دانید، وقتی می‌گویند چین از ما جاسوسی می‌کند، می‌گویم درست می‌گویید؛ ما هم از آنها جاسوسی می‌کنیم. ما هم از آنها جاسوسی می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/147345" target="_blank">📅 11:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2c6047d82.mp4?token=JJJdl0NotY24-641DMvwqCUkI7d-jic9qwR0QGC-BPkE0lVhVat80YRIED82-bZy3vn5cWMKbH_vjz5rFj56UrTDG9uprhBTtDSr0RQHpSBVDctVfT5RpN1a6KOwc3sdzVJ-XjNyIFDvkQ36aBl9Vkuo54CGfyNSDmUdY_rND5c5RPBLuJdfDCEDn5ooP4ZAxeO2e1EdOZNkTYa7vEAksq8nqqoNRG3pukUgHDxRT258blP3SDYd8amch8ctuF2R7_w1bfcKythqGuYIN5t63Q2olZ7AE34u9Yt82gFYQ0i5NoGQDxCldC0T8XGQSDDuhmbQwhTolYQDD5rvmnD8SB7uo5lvJEcTpxnPyub7-Epzw2fCNNyakBCiXfnhMOwGE3Di42BB_aDCiWL1HcaxfNOjqDfL533s7RA-ytMlJSnfXl2pwdo9VuerVO5M2AiuKUQQQBDdf6ASGM8IDhy8l9a00p806NXRYEDvwY96orxiJ_Gl5khxn-2XW1_cUuYqe_oS7Zsw-IqmOgcWOjcich57MLYbwlv-Iqm-T2QoTgmA0Ehnc__RwoTKomJGM3kYjyelQII2o7KO7f0w5R1EEznBaxb2wlHaMi7dz1va-gk8st-95STbGnBVdjO4Z6W4Z75dyaharxg_Bl-7ld9vAnKWJiDNIT6BR6Dq8Q8aVA0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2c6047d82.mp4?token=JJJdl0NotY24-641DMvwqCUkI7d-jic9qwR0QGC-BPkE0lVhVat80YRIED82-bZy3vn5cWMKbH_vjz5rFj56UrTDG9uprhBTtDSr0RQHpSBVDctVfT5RpN1a6KOwc3sdzVJ-XjNyIFDvkQ36aBl9Vkuo54CGfyNSDmUdY_rND5c5RPBLuJdfDCEDn5ooP4ZAxeO2e1EdOZNkTYa7vEAksq8nqqoNRG3pukUgHDxRT258blP3SDYd8amch8ctuF2R7_w1bfcKythqGuYIN5t63Q2olZ7AE34u9Yt82gFYQ0i5NoGQDxCldC0T8XGQSDDuhmbQwhTolYQDD5rvmnD8SB7uo5lvJEcTpxnPyub7-Epzw2fCNNyakBCiXfnhMOwGE3Di42BB_aDCiWL1HcaxfNOjqDfL533s7RA-ytMlJSnfXl2pwdo9VuerVO5M2AiuKUQQQBDdf6ASGM8IDhy8l9a00p806NXRYEDvwY96orxiJ_Gl5khxn-2XW1_cUuYqe_oS7Zsw-IqmOgcWOjcich57MLYbwlv-Iqm-T2QoTgmA0Ehnc__RwoTKomJGM3kYjyelQII2o7KO7f0w5R1EEznBaxb2wlHaMi7dz1va-gk8st-95STbGnBVdjO4Z6W4Z75dyaharxg_Bl-7ld9vAnKWJiDNIT6BR6Dq8Q8aVA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ورود خودروهای چینی به بازار آمریکا: خبرنگار: «آیا در دیدار پیش‌رو با رئیس‌جمهور شی، درباره خودروها صحبت خواهید کرد؟ و آیا اجازه ورود خودروهای چینی به آمریکا را خواهید داد؟»
🔴
ترامپ
:
«من این کار را نکرده‌ام؛ این من بودم که آنها را بیرون نگه داشتم. تعرفه‌ها آنها را بیرون نگه داشتند. من تعرفه ۱۰۰ درصدی دارم؛ از ۱۰۰ تا ۱۵۰ درصد.
🔴
برخلاف اروپا که خودروها در آنجا در حال نابود کردن بازار هستند. صفر. بنابراین، تا اینجا پاسخ
بله
است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/147344" target="_blank">📅 11:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8edb1aff.mp4?token=muidXlM-CF_vtdblnZxQbg-rFG6SWN8ZD4-M10vfKCSqhXeDscM78Ucef-Ax-j3BPTskhczLuGBEiVGPJASWjb9wuKf8GkDqEtkF7BrGXQZHvbfO3Wl7Ul_ZMB6twEezSife2tcKR_05FgzPEZcRNW02oyNYismJGi6e5gbd0vsdsO6D_-aqAkeGd1wc96RN3d_kgeUsTtYadQhWcRWCTJ95smo_eJldAOVBTkxrP7b879YUFvwafGVqwNiUKXuuulcLIAlqD4xylHwsCz0YPTV4RbeIuMtUxQyrAP17oZZkNVJrS5lgGDxhGoZ_dYWWVt6W7uQT6KyU1eWQSCXO9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8edb1aff.mp4?token=muidXlM-CF_vtdblnZxQbg-rFG6SWN8ZD4-M10vfKCSqhXeDscM78Ucef-Ax-j3BPTskhczLuGBEiVGPJASWjb9wuKf8GkDqEtkF7BrGXQZHvbfO3Wl7Ul_ZMB6twEezSife2tcKR_05FgzPEZcRNW02oyNYismJGi6e5gbd0vsdsO6D_-aqAkeGd1wc96RN3d_kgeUsTtYadQhWcRWCTJ95smo_eJldAOVBTkxrP7b879YUFvwafGVqwNiUKXuuulcLIAlqD4xylHwsCz0YPTV4RbeIuMtUxQyrAP17oZZkNVJrS5lgGDxhGoZ_dYWWVt6W7uQT6KyU1eWQSCXO9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: عربستان درخواست کرد نشست عمان برگزار نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/147343" target="_blank">📅 11:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147342">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650fa3987b.mp4?token=Bj-lWOYaIHThf1CZBpwH0Q7UGMmOxDn5nwzby2ysxwUJiXGYICVJKj2VbvQuQS-t2IAnoe9zRUyi-SzceXXI20_YPjAOyP-5PIqpd8WkuWmu1c0TY6DDn8HYcuZl8GkcSOqfqPz3WHqOaLLDxp4_30PVhSo-NxjZBeXPQuTzo-qXUOxGOWXHK34slZZ3rdW9jZFvfuFxT1wQlyVxB2WIWEixVFUR3asw5ETg1jsOB5lqgdjCoO8-uxfDW5e261p8VL6OhqYhI4FncCD4DDp5GSYDN7CnccmC7g0tjL32jMSNYd9mBzxB_9CfZuCK4KoUXsH1P7PSz2H-J6PyoVKS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650fa3987b.mp4?token=Bj-lWOYaIHThf1CZBpwH0Q7UGMmOxDn5nwzby2ysxwUJiXGYICVJKj2VbvQuQS-t2IAnoe9zRUyi-SzceXXI20_YPjAOyP-5PIqpd8WkuWmu1c0TY6DDn8HYcuZl8GkcSOqfqPz3WHqOaLLDxp4_30PVhSo-NxjZBeXPQuTzo-qXUOxGOWXHK34slZZ3rdW9jZFvfuFxT1wQlyVxB2WIWEixVFUR3asw5ETg1jsOB5lqgdjCoO8-uxfDW5e261p8VL6OhqYhI4FncCD4DDp5GSYDN7CnccmC7g0tjL32jMSNYd9mBzxB_9CfZuCK4KoUXsH1P7PSz2H-J6PyoVKS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنایه خبرنگار به ترامپ در استفاده زیاد از هوش مصنوعی برای تولید کارتون
🔴
سوال خبرنگار: آیا خودتان تا به حال از هوش مصنوعی استفاده کرده‌اید؟
🔴
ترامپ: بله، من از هوش مصنوعی استفاده می‌کنم.
🔴
خبرنگار: چگونه از هوش مصنوعی استفاده می‌کنید؟
🔴
ترامپ: می‌شود از هوش مصنوعی برای خیلی از کارها استفاده کرد.
🔴
خبرنگار: شما از هوش مصنوعی برای چه کاری استفاده می‌کنید؟
🔴
ترامپ: نمی‌خواهم این را به شما بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/147342" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147341">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری فرانسه: بازرگانان ایرانی که حضور مستحکمی در بازارهای قدیم دبی دارند، باور ندارند پیوندهایی که طی دهه‌ها میان قطب مالی امارات و جنوب ایران شکل گرفته، به‌ راحتی گسسته شود
🔴
افراد فعال در دبی توانستند شرکای خود در ابوظبی را متقاعد کنند که تجارت، فارغ از تحریم‌ها، باید ادامه پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/147341" target="_blank">📅 11:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147340">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رویترز: دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال ماندن ایالات متحده در ایران و «برداشت نفت» را مطرح کرد و آن را با توافق واشنگتن که کنترل یک‌پنجم ذخایر نفت ونزوئلا را در اختیار آمریکا قرار می‌دهد، مقایسه کرد
🔴
ترامپ گفت آمریکا در نهایت ایران را ترک خواهد کرد، مگر اینکه تصمیم بگیرد برای نفت در این کشور بماند. او همچنین مدعی شد درآمدهای حاصل از نفت ونزوئلا تاکنون «چندین بار هزینه جنگ را پرداخت کرده‌اند.»
🔴
ترامپ بار دیگر گفت انتظار دارد جنگ با ایران تا پایان سال جاری پایان یابد؛ احتمالاً پس از انتخابات میان‌دوره‌ای آمریکا در نوامبر.
🔴
او افزود پس از پایان جنگ، قیمت بنزین «مثل سنگ سقوط خواهد کرد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/147340" target="_blank">📅 10:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147339">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArAOhg7He-IuAS3G3fezhvIdUBtSlV7iljOWet54OlY-isiOfEgjxV-_mT89oYIBHx-T6PVHnygS8TGI6jyNd5QPrpsH7EUQUw-ZcQSvSdssvB47sWPNFYDtw7KUxjLBOEoj3Z8GWAP39TJ1yeKx3JOKHtehh53B6XblV50juxWyo2lBh-nYquz7kRldpBiXYYN8wjFbBIEsIYw0VVx4p40gC722VDSAp2py3LKSEsK2o1_4pR-o1u6UZK6Aybmtg3fZz1ldsC5TXzexTP_UQF0JtSxLAAntQ8RGlSxvBJNBN_LrpXCmGyNbnarlWpW9rzpxMN6nbEVWUy9-MZCpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش‌چشم: یه موشک جدید ساختیم که مخصوص ناو هواپیمابره و تست هم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/147339" target="_blank">📅 10:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147338">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نیویورک‌تایمز: دولت ترامپ قصد دارد محدودیت‌های فدرال بر انتشار گازهای گلخانه‌ای نیروگاه‌های زغال‌سنگ و گاز آمریکا را لغو کند و بدین ترتیب بخش عمده‌ای از مقررات اقلیمی دوران بایدن و اوباما را کنار بگذارد
🔴
انتظار می‌رود لی زلدین، رئیس آژانس حفاظت از محیط زیست آمریکا (EPA)، روز دوشنبه این تصمیم را اعلام کند.
🔴
در صورت عبور این طرح از چالش‌های حقوقی، اجرای آن می‌تواند تنظیم انتشار کربن نیروگاه‌ها را برای دولت‌های آینده آمریکا نیز دشوارتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/147338" target="_blank">📅 10:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147337">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3abb489.mp4?token=BYEQE76cPotCA0ItvCo4Mb1DTivhkflsKSArcm-NgxjfIVbSYwgrh4VJPWDLe9VlKW0BrR2ZpGCnAMij3yJ400ACUQPoDaIUEnLyvNDV-XCH3RoYNWMOlLBhnF_Rm0q1lw2B_1naTP1wpGykV3B5rmaPv2nFmt_rQnP1axVj6Z0ZIKAj-XvoTtnifMZWxeF4Bq9pa65o5riAA8Dx7s_O1l_HMEV75weMG_qiILZ-z61jStbh8wpURsHdVvY9m4--qvaMg3bBpRBqv-nChcYqHaOVLBlTaTEsZs6H-61xIhMOC9xYf6IDxlnDJ119wqx12Jl8yjSjRax53-6WJA1p3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3abb489.mp4?token=BYEQE76cPotCA0ItvCo4Mb1DTivhkflsKSArcm-NgxjfIVbSYwgrh4VJPWDLe9VlKW0BrR2ZpGCnAMij3yJ400ACUQPoDaIUEnLyvNDV-XCH3RoYNWMOlLBhnF_Rm0q1lw2B_1naTP1wpGykV3B5rmaPv2nFmt_rQnP1axVj6Z0ZIKAj-XvoTtnifMZWxeF4Bq9pa65o5riAA8Dx7s_O1l_HMEV75weMG_qiILZ-z61jStbh8wpURsHdVvY9m4--qvaMg3bBpRBqv-nChcYqHaOVLBlTaTEsZs6H-61xIhMOC9xYf6IDxlnDJ119wqx12Jl8yjSjRax53-6WJA1p3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: نهادهای چینی ممکن است تصاویر ماهواره‌ای در اختیار ایرانی‌ها قرار داده باشند
🔴
ترامپ: آنها اساساً همان کاری را می‌کنند که ما می‌کنیم
🔴
خبرنگار: آیا وقتی شی جین‌پینگ برای دیدار شما به آمریکا می‌آید، این موضوع را با او مطرح خواهید کرد؟
🔴
ترامپ: فکر می‌کنم او رفتار نسبتاً معقولی داشته و ما هم رفتار نسبتاً معقولی داشته‌ایم «جواب دقیقی نداد»
🔴
ترامپ از انتقاد مستقیم از چین خودداری می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/147337" target="_blank">📅 10:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147336">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-lZOfakq-5_k-bVpmLYzCVWkm9TbGa8pr7cWeW98pgpOdIlUa1dmCeEn_Nil_VxoJzse1LoR9gVmmRaqwSwQJSwasIt6WQqfG7MkDZGlxysJiL0xea20fkrB9iD4AtxHBXOZEUN07vbaupUyglgqakTsEhPP6LlDBmuSwQnTAihXNNDd0NCKwvTHoy2IfpW2WMszuLytJfKNpGHShcQXhtmcSRitHYQOVLAN78_CebZIgnlOcjYiU99wB6XyvNf8yUdZKH-AFEKwKtzzqAu0sL4SlqJkMxyNYULcQoxhcZ367dZHuqzWl0q6yYJe_5B-A4woA0SsbzZASP6YrVVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای سنتکام از چند قایق تندرو مخفی شده در زیر درخت‌های جزیره خارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147336" target="_blank">📅 10:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147335">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
در مقاله‌ای تحلیلی در نیویورک تایمز آمده است که ایران تشدید تنش را مسیری کارآمد برای تقویت نفوذ خود در مناقشه با ایالات متحده می‌داند. در حال حاضر، ایران و متحدانش بر دو مورد از مهم‌ترین مسیرهای حمل‌ونقل نفت اعمال نفوذ می‌کنند و تهران در تدارک دستیابی به دستاوردی است که می‌تواند جایگاه و نفوذ این کشور را تقویت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147335" target="_blank">📅 10:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147334">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: هرکس به علی الطاهر نزدیک شود کشته خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147334" target="_blank">📅 10:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147333">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سی‌ان‌ان: واشنگتن پرونده هسته‌ای را جلو انداخت؛ هرمز فعلاً اولویت مذاکرات نیست
🔴
سی‌ان‌ان مدعی شد برگزاری نشست به‌تعویق‌ افتاده عمان می‌توانست نشان دهد کشورهای منطقه حاضر نیستند وضعیت فعلی را به‌عنوان شرایطی عادی و دائمی بپذیرند.
🔴
به گفته این شبکه، مقام‌های دولت ترامپ به‌طور خصوصی به کشورهای منطقه گفته‌اند ترجیح می‌دهند، مذاکرات آینده ایران و آمریکا بر پرونده هسته‌ای متمرکز باشد، نه بازگشایی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/147333" target="_blank">📅 09:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر انرژی عمان : تنگه هرمز باز خواهد شد. احتمالاً این وضعیت کوتاه‌مدت خواهد بود و افزایش قیمت نفت و گاز طبیعی مایع‌شده (LNG) پایدار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/147332" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سپاه: لحظاتی قبل یک فروند پهپاد پیشرفته MQ1 بر فراز تنگه هرمز منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147331" target="_blank">📅 09:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df64bda39.mp4?token=i3g3n578DyRmUQow8PADzvWO63_zbskL6CbkmFlWrrnTjODnM1NZO2OtjxEBl8vsm6p5EaCxTM8RM8ORI8FIw22XlyQHRrPJZDZiDZYL32TzKVPNlTAX2oKvfKvlmLXePN4IbCaG82FqNoW5V-dPxa-LoO0BA88RocPmWL_aQIthp4wXZjE982oE7j_DMJzJqidZZtcVKTvAbpb0fN9OA1bTgaIfeMUtYkoyhS1AecOkBsBsUpM8JBcCuANlxN8FWxouVpHVwxWAs4aaHaggyI0KwPUYHh1805-SJLt_6GreUyyG43SRZTDbFepEEWLMhCNB_QCX4ZFu8-yN5M84GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df64bda39.mp4?token=i3g3n578DyRmUQow8PADzvWO63_zbskL6CbkmFlWrrnTjODnM1NZO2OtjxEBl8vsm6p5EaCxTM8RM8ORI8FIw22XlyQHRrPJZDZiDZYL32TzKVPNlTAX2oKvfKvlmLXePN4IbCaG82FqNoW5V-dPxa-LoO0BA88RocPmWL_aQIthp4wXZjE982oE7j_DMJzJqidZZtcVKTvAbpb0fN9OA1bTgaIfeMUtYkoyhS1AecOkBsBsUpM8JBcCuANlxN8FWxouVpHVwxWAs4aaHaggyI0KwPUYHh1805-SJLt_6GreUyyG43SRZTDbFepEEWLMhCNB_QCX4ZFu8-yN5M84GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای خسارات گسترده به یک ایستگاه پمپاژ در نزدیکی
الذِکره
، در مسیر خط لوله نفت شرق-غرب عربستان سعودی، پس از حملات پهپادی اخیر که
از
خاک عراق انجام شده‌اند را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/147330" target="_blank">📅 09:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/147329" target="_blank">📅 09:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
استاندار خوزستان: در شلمچه و چذابه از جهت تردد مسافر مشکل خاصی نداریم
🔴
تردد کامیونی از امروز صبح در بخش شلمچه آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/147328" target="_blank">📅 09:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1-swAf08RDSZC4oBTRSm5N6X-4yN_OFP5d5RiA8x02yE_sgGKTLaDNGTCi5C1YGpC8W5Qhx3qDXP02cHMvtUZfa7l-gYfWGbtRfGxeKMGk1AOcUPB9qaHsblad_f0rvR_eyoEhvj1BGyVtQT0kkladgn-rIJUOMIpnFOIB91puYEXTJkM1jSLNOmfXAE5QmgMRIkBJMyGQGPkVAqFmV0GajTl9FSKBBSLRbLWJHj8g8rkWKi-zsBZN-jDu9SIeCT49nNGMJukeiqgAo3T0JIdEmo47gWm-pQ1lPpuEo3wwyCgP_3gZHD1lmj06dRPyQk_xyw4H2KqJD3gJSH6jsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی منطقه‌ای در اطراف شهرک المنصوری در جنوب لبنان را هدف حمله هوایی قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/147327" target="_blank">📅 09:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxTgbkJTp9ofM9rhBk5y45LdxiPQeJVVIAtVPQ8fnGHkIaruwe8BzCvUhG2YLU9DATjE78pkDkBE1eI6sX48OCAJCZoLQWaCSiYeW1cCIZuiF6ykPH7xrWaPOBO67964WXS7IFAbcZ2d--4s7mFJ0bkNngyKhQkNjh5qSBkJd8PIDel4tqpu_0XuYDcPSfV9lbyYIbJq36zYGstuPFSk7q-T8CJijqd6Qhfg4Hsf40x5y1gtST9eD6_U_q6LQ9iKBaApr5XRpjLJzwU8J29bbPM30Sr0oJX5uh5edBfO7V6C_1a8N59EURhVaf-V1xMT8P7MB4AXjGcDVTlTp2u0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: محمد اسلامی، رئیس سازمان انرژی اتمی ایران، از حضور در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منع شد، زیرا اتریش پس از فشارهای دولت های ترامپ، از صدور ویزا برای او خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/147326" target="_blank">📅 08:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBTQ4nzM-9RJcgKEQOnI_oTAQKkPSBHE0PH--LedVm5doHyiTTdLhb-oFbKDAt32GnRLd1CzA7WVEu93oMPgJ3Rzs8Yk3Hzj_Bd7H-dkIcTvEq6tKiPqKaDOQymflB_aguZvu6PIn0dJVGgoP9qJ1DtK7hPO804BUQirJiMhD1LowhNL9KiLHK7Q0PHuDmZ0vWMVu_LQU9YV0vo0JFksgDoRcu9VKDrqM3uU5cjr4fzn4DuvfeErADj2A3XZqcw0jmEMMQINaD0wgRRM-12-mPN4RtMYEel_kr348wAcNdJso2yetCRHnMYjw-qDggGsjDJY5BLNaq59YqQej7W-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهش ۳ درصدی نفت؛ برنت به ۱۰۸ دلار رسید
🔴
قیمت نفت در آغاز معاملات هفته حدود ۳ درصد افزایش یافت و بهای نفت برنت با عبور از ۱۰۷ دلار، به ۱۰۸ دلار در هر بشکه رسید.
🔴
نفت آمریکا نیز از ۱۰۲ دلار در هر بشکه فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/147325" target="_blank">📅 08:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خبرنگار اکسیوس به نقل از یک مقام خلیج فارس: عربستان اصلاحاتی را در پیشنهاد عمان و ایران درباره تنگه هرمز ارائه کرده، زیرا از ایجاد وضعیتی جدید در این آبراه که قابل قبول نباشد، نگران است
🔴
باراک راوید، خبرنگار اکسیوس : یک مقام خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در پیشنهاد عمان و ایران درباره تنگه هرمز ارائه کرده است؛ زیرا ریاض نگرانی‌هایی داشت مبنی بر اینکه متن پیشنهادی می‌تواند عملاً به ایجاد یک وضعیت موجود جدید در تنگه هرمز منجر شود که برای عربستان یا دیگر کشورهای شورای همکاری خلیج فارس قابل قبول نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147324" target="_blank">📅 08:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBIYx7F5Jpo6gPLOkWFq5FqxwLhHELKOoNSqU8VqClOa2ka07KC-zPAEio1qSUmo4ERZA-eGB7CBT3sNBAQUw_rc1J91UXhv85tq2Mqks99k2GgDtjtqoryw0eHkGeCaedOXgu2R7TgVsa23KA4gfcje0A-v56MMUNliKOdGFRx3Eda_v4nj9MqYAXdtTIyKiOXtlDfvGJssURCpivNnKngRe-zIwa9DzMqusjYXMygLFBEy2F27zv7XO9Hn4WzrKzjP3dVL4zBoSx4W8p4qXk-f2Aa3I7JnR7oHAqvO5mM873ZeIQr5EpQDyhqtfSjdh8j6Z5BlXYr19lSZlwLgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QU_fqgpsH1MFXnpVRYMsGUUbGZ-tJoBiyB34mOuS1Iu59-3evfJ90Me6IbNhBchjr64ptcbpQ_MpIYDwjxtK1VYqlYDV4utQaXtUdyPee19UqQFIgl9klhpvRZjHZqk01fkh4NdAzJd-PzpeYuKpJthBljdZXZmS5E6Dwc7pgaJqgp-jelruWSCSPXhGicvcCkVKBUoypVY_O9dGtK-8FvKCgq5WRNoSDFe0fD98C0Gm1z2cz1SenojflZaLZBIRt3XX8Ga1_U1tg66XpcCGR5mSX2RUcl009d1tQDzdSJsAVIzDrvtFTO6JXCtxfxrhKDfQHJ-v_UBg-yeuA8DHMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
به نظر می‌رسد که عملیات محاصره شهر تعز در حال نزدیک شدن به پایان است، به طوری که نیروها در جبهه حیفان در شرق و منطقه جبل حبشی در غرب پیشروی می‌کنند.
🔴
این در حالی است که نیروهای یمنی کنترل زنجیره کوه‌های کهبوب، که از اهمیت استراتژیک برخوردار است و مشرف به تنگه باب‌المندب و رأس العاره است، را نیز به دست گرفته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/147322" target="_blank">📅 08:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147319">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdd3f977d.mp4?token=cXRW971AZ_sm124Jc0PC76plv3t2rwNz-NIVBTwOlduXvcj7GFhTkjLwavCSJGW15DSiU7nStqmhva2apbhwgcdY7SijTU2jJvkYFSetYjkPA5uX9cuIqdVflXUyc6HHM5Q4ifJey_iuA16i1l56OTiKbdCk6jk7s7qeJBgpufikAZNU-1O7yqO343BUhhmgi5Lw2xPFEAd7SIb4c8c1CX3l5Gft1H5qofdZo2GKfgjx0n3ms_DnNq2rtjlVB9pztAlWEn1jVNxjlhSE6sKY_C4CrjPSSqu6tW7ls0Ie8gEqmUwJ0-dFA6asyN49pl-Sut6HdToUoQl4VvL2RafnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdd3f977d.mp4?token=cXRW971AZ_sm124Jc0PC76plv3t2rwNz-NIVBTwOlduXvcj7GFhTkjLwavCSJGW15DSiU7nStqmhva2apbhwgcdY7SijTU2jJvkYFSetYjkPA5uX9cuIqdVflXUyc6HHM5Q4ifJey_iuA16i1l56OTiKbdCk6jk7s7qeJBgpufikAZNU-1O7yqO343BUhhmgi5Lw2xPFEAd7SIb4c8c1CX3l5Gft1H5qofdZo2GKfgjx0n3ms_DnNq2rtjlVB9pztAlWEn1jVNxjlhSE6sKY_C4CrjPSSqu6tW7ls0Ie8gEqmUwJ0-dFA6asyN49pl-Sut6HdToUoQl4VvL2RafnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس آمریکایی تصاویری از لحظه نجات خلبان آمریکایی که پس از سرنگون شدن یک هواپیمای جنگنده F-15 آمریکایی در ایران، سقوط کرده بود، منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/147319" target="_blank">📅 08:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147318">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmjA-u8D3cPzp5Ir0UMzWHwbmOuDfOPW55TaNsvQD79kEPTTLYBro8KOKNntty22jSCiRiFkVQihn4k9U6rayNlu4XFAvENMqk20GMKhnvLDVcWxVYFfHcRKafw_6x0EeF9D_CxkTfr0TEGVnLmGFxyCMhHrhDNVzoVDrmqc4jwrat-bG35SS0fJwUTXAcO0s5Vjg77zQPYmLQQtDBFmIlX-Ile4MqN-vEpnG-ZomAWnCE4Jw2lJYEBPQftMBVZn2B_zECwJNdy4gIIFqKeFrPm-HHojzT367cHE-pnKXFEU_TX_lCf2l7i3hyD64Y6g4UFVcQvIJ5K1DbzI_pNriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشتی نفت‌کش «ال گايا» متعلق به امارات متحده عربی، در تنگه هرمز مورد اصابت موشک قرار گرفت و در حال حاضر در آنجا متوقف شده است. از این کشتی مقادیری از نفت نشت می‌کند و متاسفانه تعدادی از ملوانان هندی و پاکستانی آن نیز جان خود را از دست داده‌اند.
🔴
ایران، این نفت‌کش را در تاریخ ۴ سپتامبر در فهرست تحریم‌ها قرار داده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/147318" target="_blank">📅 08:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147317">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c38UXYSKFhreE4yQtJBv4JUl0Z2MdE1dms83o8jJHxRIEnHnNeR4MIYZqWrU-uaoz5kQb-zkzAGMMrnqI3c-JY1PQpgDqgx6YGQTpe5EaUE7Pn1sO0G5s9gzjMCCOTuxfmR1wMsf8Pff3qgIWcnc58-hk6-DhxuTR8wJiQVhuEBfkAfY6cYPO3YomxSTpYeH2uGXRo1IgbBWVBenygIn5_AJDm1yZI3qMsHd5_NO78aGIZf9fxYKpqo5Zb4c7LtLB6LZ70JOjftOqDzEJpnkQKSpbRA7VtmVZjpBndTlS1nnTgkhEnJo-0EjOlqfEC5NWcqnC2lSBH8VmCdUYVLFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
ایرانی‌ها با کمبود سوخت مواجه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/147317" target="_blank">📅 02:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147316">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرنگار: ممکن است نهادهای چینی تصاویر ماهواره‌ای در اختیار ایرانی‌ها گذاشته باشند.
🔴
ترامپ: آن‌ها در واقع همان کاری را می‌کنند که ما انجام می‌دهیم. به نظرم او معقول عمل کرد و ما هم معقول رفتار کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/147316" target="_blank">📅 02:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147315">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5G8oMsWSk5R9KURAoATuKL8R0q1DDq5oR1i6ASQ4Na8tCphiKlv5v_TwSMS4UjgAj4nUjGg8IUhpZdBVXFtIYTZIBC3AkbmtG12CWI-vtp5x_p5_pLxoKeqz6IE8eU13IzPdRX-aV_NqFCDlerjdJc_wwe1575FFHVmfstHpgLsr3vFPZzpqh_QnsIpohV4Kunr6Py_1fBCtYjMBRJk5S4E906kmx9MhVX9w1JpP-IXHh4ZOt1xqnIUDmduCtPg-7JLbeG6t_hgYaftkD5gEY5svq2Sdu0hWOMfjMEmTJKyGZdy1oLOMS-4241nHP4-pn9JojbwIYKF5Od5B9AXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
جنگ نزدیکه
‼️
🔴
قیمت هر بشکه نفت به ۱۰۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/147315" target="_blank">📅 01:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147311">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj5EgW8ZwSX9T8iZAG4kKoNwhJW6Ss2Y9y7pEgpT9tiHR5dWozBMi4j1Oz_jCyOv1HTBYjtp95z1lY9bC55v_HGpxb2qySuu5EkM1HRaxOLjSQbzdqq3aIl0h2ZNSW-s-nHK22R_WeXPwYgUjkdVSoO23UgsrWT_bQV_sBCJTuFmjzVS0IZ_r1wjNlEaeOKWqqIKXMw4TFQSHgzWFGX1m8wRR-8PYG_-fyGOayUril5bg4AN7G22nyb8rIQkJV0xQrpsBjzRaBKUXG6C5LcN9IQ3hbub5H5aUI5dk8wtFe7FMsBUiR6z7ameSxdTCImgH0NEhlStOn5MP9-IWuK7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b21bcfe4.mp4?token=ARTqF6jpzFy4uLALs3wxqypFqWpRdTtHJYaG75790ub1nUJsD-yKhvrJgIM5vwr5YxtXRrfCTSXENwvoSAR0-8HOcYKMbZpbC-od1kzV-IMrNczYKbnDjgmqHvAprPpXlk-ecz3YbCLVixtXfC45KMqThRXinwEyOEmsa4EQPjkHhb2NO1CFwgg2HX3ZWUWCGaLWOn1sz-Hhj-zRnFu3rEq0_weVqmY3YbDxE6jPeQCAkwy9zr9kG8fHqvRzZLgMP5GPOeXmxaMsXJZGZIhzgiA7B_Pz-nY2flU4CTSEHSpz2YEQf4LhKQQxwzzUBkNQGTC8dVF2WiOJgx9kb8n50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b21bcfe4.mp4?token=ARTqF6jpzFy4uLALs3wxqypFqWpRdTtHJYaG75790ub1nUJsD-yKhvrJgIM5vwr5YxtXRrfCTSXENwvoSAR0-8HOcYKMbZpbC-od1kzV-IMrNczYKbnDjgmqHvAprPpXlk-ecz3YbCLVixtXfC45KMqThRXinwEyOEmsa4EQPjkHhb2NO1CFwgg2HX3ZWUWCGaLWOn1sz-Hhj-zRnFu3rEq0_weVqmY3YbDxE6jPeQCAkwy9zr9kG8fHqvRzZLgMP5GPOeXmxaMsXJZGZIhzgiA7B_Pz-nY2flU4CTSEHSpz2YEQf4LhKQQxwzzUBkNQGTC8dVF2WiOJgx9kb8n50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات موشکی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/147311" target="_blank">📅 01:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6317df925.mp4?token=Dvvm1AM5nJoiwgJphOZ0HsDJ2E2znmZqV22RTGwF1NJI7Uo2TrJhoNQTWjaShJi8e-Aeuwdycj0Sz2yiwseoEfPjfx6gEmv6oajtS_CceD8P9MnUWUzlFSVAn6CUdK0yYu2r-tbEEieejXepsTzgX88fYJJcRnkwk85U04XMqJNh_EFYh3Blz5pWBgszKHz2Yu5ygrSYLgcWuZPkVAWW6c84CvEAOE-RB0wHFBdPE4iYqd5wEJOHsZ3H2vGhrG_V9_xcI5Tf6NJiPhvN68wWSUHXBs8fSgcPIsrFicjOCMYCkVVJqUaOQgwXW-iTj4BK2Bua3tOt9o5vgEpRYuGIgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6317df925.mp4?token=Dvvm1AM5nJoiwgJphOZ0HsDJ2E2znmZqV22RTGwF1NJI7Uo2TrJhoNQTWjaShJi8e-Aeuwdycj0Sz2yiwseoEfPjfx6gEmv6oajtS_CceD8P9MnUWUzlFSVAn6CUdK0yYu2r-tbEEieejXepsTzgX88fYJJcRnkwk85U04XMqJNh_EFYh3Blz5pWBgszKHz2Yu5ygrSYLgcWuZPkVAWW6c84CvEAOE-RB0wHFBdPE4iYqd5wEJOHsZ3H2vGhrG_V9_xcI5Tf6NJiPhvN68wWSUHXBs8fSgcPIsrFicjOCMYCkVVJqUaOQgwXW-iTj4BK2Bua3tOt9o5vgEpRYuGIgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از موشک شلیک شده به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/147309" target="_blank">📅 01:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/147308" target="_blank">📅 01:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLEO5lxQvZINMhDRz9nzVvojELdk6Zewp_Lpp1y25F3GQGEQbtKIMSxAXHa9V7nOnLIxL6UFpx28cvQSpKC32yqyjzexYg6TFIYI9pBa2oth6ybWq6H0ix0oCnwEoMbhkKEAargmY9cVgLwPJn9Jytbv-sj4gkDeavfP0f7myxnVtHvKxRmapPIUBYWeC3PvA_nFWuhMb7_ErjFcHwNjc5mYP8rhxtVcfB1Nvl8ar57i1vlR2pfiKNXYxtK4fwC7g1dliNXEE9d_IckvxmLEBVjlJ-zwyOjkU2XVPWc6XkTd0RohP6kC_hrnGXWMcxCgGVhagg7o8VHfCsw2ym_0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقتی یه ایتایی تریاکی رو میبری توییتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/147307" target="_blank">📅 01:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvJo260vWb2e8w6gF27Ng0vTrw6RBMRQQKwP-dphx-J8hppsWNHRKDa3aBGyOL2styIPNpxzXP233iFIDUUgEV824Dl3rzXftLkNaq2k6qZ_nX_aqzg1bHqgYVUpjsCaOyteuOs8o-GV0lnIZ6Xu1wZNxuAXSe18uODYqZ5dQMjSMzj_nmngh99bksvWjLNAYRKOXwEgw1XuvFtCk1jjrljUtdQuqzaJo2hyzs44gs1ikLYvr4wG5GMTtUS5p4dMvRL3dX-lxKfkTWifoC0VgDHXGPJ-RPemy_r1E8mqtouAMOksszh0dJjRhv3oe48UsJ5y9ZDqacSk0OC_IehOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قالیباف از سمت مسئول ویژه جمهوری اسلامی در امور چین برکنار و مخبر جایگزین وی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/147306" target="_blank">📅 01:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147305">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebsAboGkNJfKPzfBnK0RyPgZtejAKvkqVUpMetQ27sO9i2AhEMcx_6KTzk4TimPNPHavDhlJ0JXROkIcEK3vGXf6FuFWLXUrHymEpGSHy4-4PUArty6mDfPcJ366LLesmyiBbNY7txgCHgJCDAx6DhyH3a9lXuQQSwCfHhkRMjR-e0n7cd5Ipbr33UoXIhfrEtdJ5qncJuLFaq7aZ--z0ccn8K764uX5JZi4iApHhQ1mtfl-HHFDqwSh4LmvU2yggrNT4RwiOee1dCXN8Jjky8uKahlS06sfLv5pME871smvrK9j2nz3yI4gD8ZXq16VwU-oTiNy7W8_sKZgAk927w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اولیه آیفون 18 از 665 میلیون شروع میشه و تا یک میلیارد هم‌میرسه.
🔴
آیفون تاشو هم از یک میلیارد شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/147305" target="_blank">📅 01:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147304">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ به نزدیکانش گفته باید یبارم به ایران حمله کنم احتمالا برنامش برای تاسیسات هسته ایه
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/147304" target="_blank">📅 00:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147303">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شوک و بهت در خاورمیانه
‼️
اسرائیل هیوم:
🔴
رهبر عربستان از موساد و ارتش اسرائیل برای مقابله و کمک اطلاعاتی برای حمله به حوثی ها درخواست کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/147303" target="_blank">📅 00:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147302">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bljNJwCmz8ApDJSmrUj9CbPDJNdakQOKckDnAAFTPJERsS6BjM9MnoHmsU9qBNfPXJgbyUosO4_TkGsaBG0Gr7CUWzJcH65EZnPSrV_liINauGu5cnH9FC4xA-kcmsgNLFMMsAc_nzr-zqGHkFCkC5qBsxU7JcHK1DKyP5NFlR8ODT430oHEII-FaFZCONiyRuDXaH62jgFKNnqalDQUQhZUbnO9ZiQ0STaxAIHDY_jqKNV2TAzx88vMYpLC0quTM5eBeVmRfUFv7ENUQCkE_G18NZPIEz_ZbsqH_9x4i1Thn1_iaNjMpQwk88ykNTcKpxzeXf5mYr0KJTU9iY2cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادان: شرایط جنگیه، هرکی دست به اعتراض بزنه ما دست به ماشه هستیم، چون تو این وضعیت هر شلوغی یعنی کودتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/147302" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147301">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWcsnU17J0FsCUG89FOFjS8C4vwdY9QsbWvYDDPfQFCDx72x7AbeZGhomem1ogHl56OfT-oieJkavxNEBdwcriROxjmUPmKJ-EDy-HYCrgdrZDW6WRpI0vSh6_W89PEzGSoUvFt7Q5prvALpPH4Uz-NB3mTZb7wE1eEsxhqpAhlRT9qgIBjvTs-7sGRdL5-FaSPw69SszdXeLvv5nzfx41DTCgKEmGlGurV4XJBe3ZwgCHHF2VUYfzlLibFrM1YGlRU_5sAdkrX5jgq8T3BneCw_ZsRNYYixFuK9SMTWfyvCKHIJHS8g4VWMW7kxsd5tlDqORnB78EBbxGTsHJF6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر هم اکنون 232000
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/147301" target="_blank">📅 00:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147299">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کاتز: تا خلع سلاح حزب‌الله از جنوب لبنان عقب‌نشینی نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/147299" target="_blank">📅 23:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147298">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سی ان‌ان به نقل از منابع آگاه: آمادگی برای بررسی پرداخت‌های داوطلبانه در ازای هدایت عبور کشتی‌ها از تنگه هرمز وجود دارد
🔴
بر اساس چارچوب حقوقی عمان، پرداخت داوطلبانه در ازای تأمین ایمنی ناوبری و حفاظت از محیط زیست پیش‌بینی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/147298" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147297">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیران خارجه قطر و عربستان درباره تلاش‌ها و هماهنگی‌های مشترک برای کاهش تنش و تشدیدزدایی گفت‌وگو کردند
🔴
وزرای خارجه قطر و عمان درباره تلاش‌ها برای کاهش تنش و تقویت امنیت گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/147297" target="_blank">📅 23:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147296">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوووووری / گزارش ها حاکی از شلیک دو موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/147296" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147295">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / گزارش‌ها از وقوع یک انفجار شدید در نزدیکی ساحل سیریک در استان هرمزگان حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/147295" target="_blank">📅 23:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147294">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرگزاری واس گزارش داد وزیر خارجه عربستان در تماس با همتای اماراتی خود درباره تلاش‌ها برای مهار تنش‌ها و جلوگیری از تشدید اوضاع در منطقه گفت‌وگو کرده است.
🔴
دو طرف همچنین بر ضرورت یکپارچه‌سازی مواضع در برابر تحولات اخیر و تقویت چارچوب همکاری میان کشورهای شورای همکاری خلیج فارس تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/147294" target="_blank">📅 23:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147293">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
محمد علی بک» مدیرکل خلیج فارس وزارت خارجه: بنا به درخواست برخی کشورهای منطقه و تصمیم مشترک عمان و ایران، نشست وزرای امور خارجه کشورهای ساحلی خلیج فارس که برای روز دوشنبه برنامه‌ریزی شده بود، به تاریخی دیگر موکول گردید.
🔴
ایران در رایزنی نزدیک با عمان، درباره زمان مناسب برای برگزاری این نشست هماهنگی‌های لازم را انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/147293" target="_blank">📅 23:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147292">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
عمان نشست منطقه‌ای برای دستیابی به توافق درباره تنگه هرمز را به تعویق انداخت!
🔴
بدر البوسعیدی، وزیر امور خارجه عمان در بیانیه‌ای رسمی، از تغییر در برنامه‌ریزی نشست منطقه‌ای که قرار بود فردا در خصوص تنگه هرمز برگزار شود، خبر داد.
🔴
وزیر خارجه عمان اعلام کرد…</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/147292" target="_blank">📅 23:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147291">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWI1uCH-csefv73GuORUigRRHeRIWO22WlSI-A-tECVb99MSh7v8SECfYvKk6u2ZEqJ1PvYijeyoy2S7uGgaKy7HLi4zGKKYrhRDgCJEVAmuHvzEiJoFPxOO2MolEHoHCKei3oq5H1GFxF9RQf1viyW7-fkWX32kY-CxIDkpmPzyexvmAETavlEEkYcl6gaQzxiGI2tuilpCPCnxyQE4Z9RnWW6hBG4OXI8ILdfkzPieRfYufk1sIkGlQjsqL5h_PIfGdH8AwGSXFTpYo6O-qkt3FVGXCOUxM6Qj-bk2lrT1lweyC7S9YPDV_B8z08E_f1OsmJQbYgbqhGKQcGpNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عمان نشست منطقه‌ای برای دستیابی به توافق درباره تنگه هرمز را به تعویق انداخت!
🔴
بدر البوسعیدی، وزیر امور خارجه عمان در بیانیه‌ای رسمی، از تغییر در برنامه‌ریزی نشست منطقه‌ای که قرار بود فردا در خصوص تنگه هرمز برگزار شود، خبر داد.
🔴
وزیر خارجه عمان اعلام کرد نشست منطقه‌ای قرار بود فردا در صلاله برگزار شود، اما برای تضمین دستیابی به توافق، موعد آن به تعویق افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/147291" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147290">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6de5b369.mp4?token=DEVw3gH8Xs-ghvK7aBFJL0mxh7z8CD6wNkO_LY2c6MZUY03wO579jB9y8zeFiDci49ZosCRul8HNwFtKQbw37RFP4W8_s07gA9QhWnijDEYgbqU3UEjVKPuJ0MSnG0vvunjn11zSoyghI-6Ra2hLsklnMRdy9CewIRh9hftTDbKGcr8EDr9mPNBZuRFrQ7sG5ELjE2FkYKMFp3tjXX7tCdLXutcziuWNPTBmIaQZLm_niPShuiSB5mphK4hlrwLSdmrJebR7RI5DCanz5SlbzixDgOiYfqC3SzSxvDoIdgbSakTCnXyZZFOAqgUYmQQUH76Igtn2gTF_aOMQrL8vYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6de5b369.mp4?token=DEVw3gH8Xs-ghvK7aBFJL0mxh7z8CD6wNkO_LY2c6MZUY03wO579jB9y8zeFiDci49ZosCRul8HNwFtKQbw37RFP4W8_s07gA9QhWnijDEYgbqU3UEjVKPuJ0MSnG0vvunjn11zSoyghI-6Ra2hLsklnMRdy9CewIRh9hftTDbKGcr8EDr9mPNBZuRFrQ7sG5ELjE2FkYKMFp3tjXX7tCdLXutcziuWNPTBmIaQZLm_niPShuiSB5mphK4hlrwLSdmrJebR7RI5DCanz5SlbzixDgOiYfqC3SzSxvDoIdgbSakTCnXyZZFOAqgUYmQQUH76Igtn2gTF_aOMQrL8vYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران اعلام کرده که یکی از کشتی‌هایش شب گذشته مورد اصابت قرار گرفته است. آیا این کار توسط آمریکا انجام شده است؟
🔴
ترامپ: نمی‌خواهم چیزی بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/147290" target="_blank">📅 22:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147289">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b85cbdf7.mp4?token=N7tH6A0Ooktn1C0qAaJf9W1h3Njvu46_EMro_WaX7au5cGlNj7W9ukzaDv0Az52ssdEOMtb8KauFFk1dPLbBNyiKdH-EzbpyrzKW0jbqwuzpBDH-FvNUucAm1AWa_BoDxBLCWXb16wBQPu8VSPyS1CNAaRTjQfLxhY2u337ombzo8BWAO5Ud8XIUYg-CO-wfgljvinautqfyhlmQgYWHlYiqee5GOWLJerzdFfL9Mn2P-mEY5AxRrOA4p4morruPsJPm_3_J-nS-MFIJXH2Gzbeyi3Twde3O8GG0hFwiWLNwMO0NwjmTgvoXDA7jsvVsGl-IEfLqbD30rhdSiZdHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b85cbdf7.mp4?token=N7tH6A0Ooktn1C0qAaJf9W1h3Njvu46_EMro_WaX7au5cGlNj7W9ukzaDv0Az52ssdEOMtb8KauFFk1dPLbBNyiKdH-EzbpyrzKW0jbqwuzpBDH-FvNUucAm1AWa_BoDxBLCWXb16wBQPu8VSPyS1CNAaRTjQfLxhY2u337ombzo8BWAO5Ud8XIUYg-CO-wfgljvinautqfyhlmQgYWHlYiqee5GOWLJerzdFfL9Mn2P-mEY5AxRrOA4p4morruPsJPm_3_J-nS-MFIJXH2Gzbeyi3Twde3O8GG0hFwiWLNwMO0NwjmTgvoXDA7jsvVsGl-IEfLqbD30rhdSiZdHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا شما آماده‌اید که در سال 2028 از جِی. دی. ونس حمایت کنید؟
🔴
ترامپ: الان خیلی زود است. من فکر می‌کنم او فوق‌العاده است. ما افراد فوق‌العاده زیادی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/147289" target="_blank">📅 22:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147288">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7989307a6.mp4?token=NlECgj8yV5VidgjsY7b9d6kI0T_JGZf3Dwyx6OU7_ZLvU3BS-23MythQjMXgQ5lmWXbpeBBIU-bIGsygnZiOeCJpauUNK9VDLtSfLH63FkygAx4p0sevE6niKihLAJZPkKG8Wjyhs47oMUnRnjwlF_S2tYi7ASr9KS0NxsVk7ukeOVjaIfhW89EiD92JAgKxNUToopBaVJecl36hBONxb4t4bT_kgHTBr70LFDqhX7cIpQguz3eWz848fPKozq2fj2S26JcwalzDH6o3JZRNGtdgZiKC0CmMtI-8NQTK0gHdnBJKonuSl47mdUoHKRBOAGwqxiFLmmtSFmc2KRepiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7989307a6.mp4?token=NlECgj8yV5VidgjsY7b9d6kI0T_JGZf3Dwyx6OU7_ZLvU3BS-23MythQjMXgQ5lmWXbpeBBIU-bIGsygnZiOeCJpauUNK9VDLtSfLH63FkygAx4p0sevE6niKihLAJZPkKG8Wjyhs47oMUnRnjwlF_S2tYi7ASr9KS0NxsVk7ukeOVjaIfhW89EiD92JAgKxNUToopBaVJecl36hBONxb4t4bT_kgHTBr70LFDqhX7cIpQguz3eWz848fPKozq2fj2S26JcwalzDH6o3JZRNGtdgZiKC0CmMtI-8NQTK0gHdnBJKonuSl47mdUoHKRBOAGwqxiFLmmtSFmc2KRepiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: خانواده‌های قربانیان حادثه 11 سپتامبر از شما خواسته‌اند که به آن‌ها کمک کنید تا دولت عربستان سعودی را در قبال این حادثه مسئول بدانند، و از شما می‌خواهند اسناد بیشتری را منتشر کنید که ارتباط برخی از تروریست‌ها را با افراد در عربستان سعودی نشان دهد. آیا شما آمادگی انجام این کار را دارید؟
🔴
ترامپ: من این موضوع را بررسی خواهم کرد، زمانی که به [کشور] بازگردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/147288" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147287">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72265eb413.mp4?token=Yd4WIfyMNtg2cQB3yeAVsTmqMksIYHFPSod8MnBirOeUD7yKifT3_SynRnymZ88BxTJYnHXSqLhBcK0RhtcKZOF9z0J6eLEp6MdzDzTyzTWP12opCXkgQSaOpi3DsjNZq3ZozUXaE6Hl8Pt5J1c9JnpM4R3Vj1WVwmJ_Ns-2qxPAPbPMe1OLEhLg1dXKqLq2Gnayycl0cE8aIwDOwHGAk_NSw_vLLjNcP03LnWWwv9vSzM4z5zZ5nzksGr1X70DczIeQsAbuUF8Iw8RvW3qhKif6qw0UaWjPteSjxye6K5BQkG7L5kFVzOsOGV-Uq5yx7pHGZDIh8LeBFGMssBUPDKlKDLHmwd6Rt_-vxWIYm1pdPiRF4XAc_KyHyRVDnO6dVWNAYQkAmOadCc7cWAGIc4pemv2bjnqkECw6h241BbhR3KQsA9waFePJc-EMeEhX5o4NCVKjCDoKlvlLAuDFynOzkxB94_ilUAlY1WbYTdbTNhJNrbS6zltXPrpDprT6jxMGGl58qp2JdE3fadfEx-dBElQf6f9kUBRcWHPJV-yWTpBHJfEme9IavdaszcSnCGMLoeBjo2lqDlAxH2GTjNI8iDNDk8HitAOVQI-q8_YUWqziEp235oHg5isAoioctGOkdiDm2Eb-SRIJ08puqw3FX2TnjS4MrGj1ol5RBMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72265eb413.mp4?token=Yd4WIfyMNtg2cQB3yeAVsTmqMksIYHFPSod8MnBirOeUD7yKifT3_SynRnymZ88BxTJYnHXSqLhBcK0RhtcKZOF9z0J6eLEp6MdzDzTyzTWP12opCXkgQSaOpi3DsjNZq3ZozUXaE6Hl8Pt5J1c9JnpM4R3Vj1WVwmJ_Ns-2qxPAPbPMe1OLEhLg1dXKqLq2Gnayycl0cE8aIwDOwHGAk_NSw_vLLjNcP03LnWWwv9vSzM4z5zZ5nzksGr1X70DczIeQsAbuUF8Iw8RvW3qhKif6qw0UaWjPteSjxye6K5BQkG7L5kFVzOsOGV-Uq5yx7pHGZDIh8LeBFGMssBUPDKlKDLHmwd6Rt_-vxWIYm1pdPiRF4XAc_KyHyRVDnO6dVWNAYQkAmOadCc7cWAGIc4pemv2bjnqkECw6h241BbhR3KQsA9waFePJc-EMeEhX5o4NCVKjCDoKlvlLAuDFynOzkxB94_ilUAlY1WbYTdbTNhJNrbS6zltXPrpDprT6jxMGGl58qp2JdE3fadfEx-dBElQf6f9kUBRcWHPJV-yWTpBHJfEme9IavdaszcSnCGMLoeBjo2lqDlAxH2GTjNI8iDNDk8HitAOVQI-q8_YUWqziEp235oHg5isAoioctGOkdiDm2Eb-SRIJ08puqw3FX2TnjS4MrGj1ol5RBMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کاهش روابط تجاری با کشورها: من این کار را با برخی از کشورها انجام خواهم داد. من هیچ انتخابی نخواهم داشت.
🔴
ما نمی‌خواهیم با هیچ کشوری کسری بودجه داشته باشیم. ما می‌خواهیم مازاد داشته باشیم، یا حداقل به تعادل برسیم.
🔴
این کار در یک بازه زمانی انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/147287" target="_blank">📅 22:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147286">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38762dc8a9.mp4?token=duWAiRGoLhLB45OiZXy8XnAAOK0jzTw2oC6Cl8rH2BBkvE1KXjyk0DyfI3qr_Io4PRutTB32bno9J3z1UTGgInHS32oQKZPzjSjEIwf-7DvD5NbqVaZ5u3799LFwUcZEFpijvbeOF3sYDC9uhlvIu0n1odYd2iLpOxsGQ-eDFuHVfWsgCiBPkRHY1I5ROP_eqE7RBdfTZKLw48BkGxGT-G_jUf2JO8gk81IFr3wbrpy1DQ-FWiTMFVJWr7AhUnHwREoNMLzKci2DKkHJPcn4fICWlwKMrA5cMTfBZJYMZXog1tee1XB_CKJrexuvzBKeczfZamvyrB4ZgpeFXQMGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38762dc8a9.mp4?token=duWAiRGoLhLB45OiZXy8XnAAOK0jzTw2oC6Cl8rH2BBkvE1KXjyk0DyfI3qr_Io4PRutTB32bno9J3z1UTGgInHS32oQKZPzjSjEIwf-7DvD5NbqVaZ5u3799LFwUcZEFpijvbeOF3sYDC9uhlvIu0n1odYd2iLpOxsGQ-eDFuHVfWsgCiBPkRHY1I5ROP_eqE7RBdfTZKLw48BkGxGT-G_jUf2JO8gk81IFr3wbrpy1DQ-FWiTMFVJWr7AhUnHwREoNMLzKci2DKkHJPcn4fICWlwKMrA5cMTfBZJYMZXog1tee1XB_CKJrexuvzBKeczfZamvyrB4ZgpeFXQMGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، نظرسنجی‌ها جعلی هستند. میزان محبوبیت من در ایرلند خوب است. میزان محبوبیت من در ایالات متحده عالی است.
🔴
مشکل این است که فقط نظرسنجی‌های معتبر منتشر می‌شوند، همانطور که شما می‌دانید. ما عملکرد خوبی داریم. کشور ما عملکرد بسیار خوبی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/147286" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147285">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28945f0ed.mp4?token=I8GU62T6LkrxsTx9n-qo7nLZLbKT5btqtsEm4D2JkYrkbbriv4Pchq8fSoVTy4ESl2ogLbsKMrQwi_sjNMv078eUQqwLjG3viSehLA4JJ8TZ69g0_S9UdN2ZJ6FBsC2GX9dqcPGG8EKv4jaQtJRZToqqQhf6a8aovfG_1qbyO51WWhdJ-jff5xyjfsZGJEyVINcVJSdqMBGIRDXlyv87yUutsd9qYxVp9ChBrpY5sIh8esgyguXx4gFCai5VNlPVifueLGIHru0KuRlM0sq1v6uHVY8Z1tus-pcVGcdHdIrq2C0ug69-MNbx-AuBTqAN0AM3Cx9PiI3j4AkWoE_gqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28945f0ed.mp4?token=I8GU62T6LkrxsTx9n-qo7nLZLbKT5btqtsEm4D2JkYrkbbriv4Pchq8fSoVTy4ESl2ogLbsKMrQwi_sjNMv078eUQqwLjG3viSehLA4JJ8TZ69g0_S9UdN2ZJ6FBsC2GX9dqcPGG8EKv4jaQtJRZToqqQhf6a8aovfG_1qbyO51WWhdJ-jff5xyjfsZGJEyVINcVJSdqMBGIRDXlyv87yUutsd9qYxVp9ChBrpY5sIh8esgyguXx4gFCai5VNlPVifueLGIHru0KuRlM0sq1v6uHVY8Z1tus-pcVGcdHdIrq2C0ug69-MNbx-AuBTqAN0AM3Cx9PiI3j4AkWoE_gqIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان آمریکا، درباره ترامپ: ترامپ ایده‌پرداز فوق‌العاده‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147285" target="_blank">📅 22:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147284">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536ffda598.mp4?token=hmGCDiWd6XNnCOKKT8W81C7Lbva5xWI7LiBL3pQIg84sn3nv_Bo9dXN72jIYSVfukgkHy31BG6einDnHDvwsBXehTnXqCeMVQCVAucl5gb-tlk5aOcxvrge7rRRL9tYnev6mMRJdUztd1HxYC-4kuZnT5NHqV9ZvP5821yjeFXoOn3ZFRCckgzuyQW3tp_RgBLedZ0x4d6iG1otfaM1828Kop5CPpFHEYUnpxuZSGoMeU9WsYullUP8jbvylv0SZyhos8cOKwbiRBECdjd4h-hU0Vi3ASR1j2FkVRgq6Pcad8-26h4QYujhz6qgVxkCbiTtxNsW5xwPQQuXnRGgJ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536ffda598.mp4?token=hmGCDiWd6XNnCOKKT8W81C7Lbva5xWI7LiBL3pQIg84sn3nv_Bo9dXN72jIYSVfukgkHy31BG6einDnHDvwsBXehTnXqCeMVQCVAucl5gb-tlk5aOcxvrge7rRRL9tYnev6mMRJdUztd1HxYC-4kuZnT5NHqV9ZvP5821yjeFXoOn3ZFRCckgzuyQW3tp_RgBLedZ0x4d6iG1otfaM1828Kop5CPpFHEYUnpxuZSGoMeU9WsYullUP8jbvylv0SZyhos8cOKwbiRBECdjd4h-hU0Vi3ASR1j2FkVRgq6Pcad8-26h4QYujhz6qgVxkCbiTtxNsW5xwPQQuXnRGgJ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان ایالات متحده: به نظر من، این ترکیبی از کشورهای متحد ما، دوستان ما در ناتو و سایر کشورهای عربی خواهد بود ... که با هم متحد می‌شوند تا اطمینان حاصل کنند که تنگه هرمز باز بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/147284" target="_blank">📅 22:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147283">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
تسنیم: حذف سهمیه بنزین ۱۵۰۰ و ۳۰۰۰ تومانی خودروهای بالای یک میلیارد تومان تکذیب شد؛ سهمیه‌بندی مثل گذشته ادامه داره وق فقط نرخ سوم بنزین از ۵ به ۱۰ هزار تومان افزایش پیدا کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/147283" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147282">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ed9b90c6.mp4?token=NA-wvq2MMzl3qs3kvuaALR70vtvhOfo9NWR8DxLr3ae6eF5Pw1JFwg_0nTfz-3Ty4YDzSuCCUm42rpY1BltnxTceV8jN1C-qDI9U2YKzOpMv9d7LAm_fpFhlqFbQnTSUkXRy8KKAxy_FGBExjGuqacZ14-5ZyPzRK6YMMaC-pYL6801jhRpBudb5FbIwISPzJCJtxb7HxFLvuk9-Rvo2c9_B298om-MAglmrOASR125jXLxIpDairHPOdtBpsl7KCm6t7lEJWlVGgNAiV3mW2oatydhT3E73PzkhUlEUsWFUbrPn-K_zfHb80IlNbonErfmNK-6Y-yZEF7tmnNqsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ed9b90c6.mp4?token=NA-wvq2MMzl3qs3kvuaALR70vtvhOfo9NWR8DxLr3ae6eF5Pw1JFwg_0nTfz-3Ty4YDzSuCCUm42rpY1BltnxTceV8jN1C-qDI9U2YKzOpMv9d7LAm_fpFhlqFbQnTSUkXRy8KKAxy_FGBExjGuqacZ14-5ZyPzRK6YMMaC-pYL6801jhRpBudb5FbIwISPzJCJtxb7HxFLvuk9-Rvo2c9_B298om-MAglmrOASR125jXLxIpDairHPOdtBpsl7KCm6t7lEJWlVGgNAiV3mW2oatydhT3E73PzkhUlEUsWFUbrPn-K_zfHb80IlNbonErfmNK-6Y-yZEF7tmnNqsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا:ایران‌ها شرکای قابل اعتمادی در مذاکرات نیستند. البته، آن‌ها هر روز دروغ می‌گویند. آن‌ها سر میز مذاکره می‌آیند، یک چیز به شما می‌گویند و عمل متفاوتی انجام می‌دهند
🔴
برای برخی از آن‌ها، این بخشی از دینشان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147282" target="_blank">📅 22:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147281">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/147281" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147280">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyQIGCwAHe-4u298UE8Wk6GZ_wFevSwRb_JU56rQYW0etRYFTZ2X6XZHpFSiRNoPzMF4Lb_YX1hiPDc3kO4Of4hrhDrTrZpYX5IbSI9-24f_C9qQJciuwmkYBUTPDgqdRCiAOc_A9YbF6DCNxSta_7Si4UUstBFxWD9DZMhYB9JlO7K_I8lZ4Ydqd3SA_gq908XWBMeXCfaMfh960Xw_r2uHynizPQFUuAd0JWkaFRX03GVar4Z4r1om3zk4iUCPAwAY-Qgw-EHBj1H_6np7EEK1hj0d0aaga9TgCMzBRfIqZchzjtgUqIJ7Yg65wH8dHB6fbmpbSrQpU9-FoodM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فانا: مدیرکل دارو: واکسن آنفلوآنزا در اواخر شهریور و اوایل مهر ماه می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/147280" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147279">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
شی جین‌پینگ رئیس‌جمهور چین ممکن است از دیدار در اواخر این ماه با «دونالد ترامپ» رئیس جمهور آمریکا، خودداری کند.
🔴
دلیل این تصمیم احتمالی از سوی پکن، اعلام تایید فروش تسلیحات جدید از سوی آمریکا به تایوان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/147279" target="_blank">📅 22:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147278">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=a2cXxNX6aRTjEu1GGDWHI8kv1s2-BFvZDbk9wGcvODTr4ZkBjQAANMH33iWpuX6kCi1bv8AM-aZx0k7RYuwN1s3eN_gxwwGtz8YGhVIGbdDs2pEWn_YhchtCBmqcyNqYXSyd_b0EwfQvqT25IYwNw3-551tF3P3So_OlqU0ffI8p7ezyIuK5rLk7tdk86O_hQCWms0gwVjsK1KS_e2xLAhcNuXTP5tiHK1Dd8GyM3fOh8NVQxDjrxUX2RR2Mp9JXMld2o1Fj96HgmGa36TpBgvwQt2IbRHJgrWypnXkr8kUE9H0G5kUSBqPWfRF378KP15e0YNEsgvqnHK4PFWr3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=a2cXxNX6aRTjEu1GGDWHI8kv1s2-BFvZDbk9wGcvODTr4ZkBjQAANMH33iWpuX6kCi1bv8AM-aZx0k7RYuwN1s3eN_gxwwGtz8YGhVIGbdDs2pEWn_YhchtCBmqcyNqYXSyd_b0EwfQvqT25IYwNw3-551tF3P3So_OlqU0ffI8p7ezyIuK5rLk7tdk86O_hQCWms0gwVjsK1KS_e2xLAhcNuXTP5tiHK1Dd8GyM3fOh8NVQxDjrxUX2RR2Mp9JXMld2o1Fj96HgmGa36TpBgvwQt2IbRHJgrWypnXkr8kUE9H0G5kUSBqPWfRF378KP15e0YNEsgvqnHK4PFWr3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند : شطرنج، پاسور و سودوکو باعث احضار اجنه میشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147278" target="_blank">📅 22:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/147277" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سازمان رسانه‌ای اسرائیل مدعی شد ارتش اسرائیل به صورت محدود از ارتفاعات «علی الطاهر» به سمت قلعه «شقيف» در جنوب لبنان عقب‌نشینی کرده‌ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/147276" target="_blank">📅 21:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خبرگزاری تسنیم: از روز سه‌شنبه ۲۴ شهریور گردهمایی جانفداها برای آموزش کار با اسلحه شروع میشه و بعد از آموزش به گردان های نیروهای مسلح اضافه میشن تا برای جنگ با دشمن آماده بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/147275" target="_blank">📅 21:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b41b26dc.mp4?token=kxzGuE4cxtetqVpJA04Jce9IPb-k3nQTDHhQT3vgVxjK0tp0WtwG9RXHLLc_oEVJ5QvdvkhSpdrcemDDzLPkALQ1ERiqRQB_WUxAAtOEcbAE13Mo-vlyedoWuMQ-NO4EFWDi2SNy4GGn5mn9PXMH8gVl0Uo4UzU8GaCMi5sQD8FWeoVt6R_TWUlyr2VC-BvOa0DUE0LiwJqZs_6lP1nZVVAuwMPBfzZ0yj-MzwfRFM2FzKtVMq2uP2S3Wj4hp2yEns4bgZVixYRunT8hv81kgTyVDPuJ9ogPOjq84-9580io5mPMfy-jLPxv0FvYowCKmVqb27nw5RNf9bJPBaAKsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b41b26dc.mp4?token=kxzGuE4cxtetqVpJA04Jce9IPb-k3nQTDHhQT3vgVxjK0tp0WtwG9RXHLLc_oEVJ5QvdvkhSpdrcemDDzLPkALQ1ERiqRQB_WUxAAtOEcbAE13Mo-vlyedoWuMQ-NO4EFWDi2SNy4GGn5mn9PXMH8gVl0Uo4UzU8GaCMi5sQD8FWeoVt6R_TWUlyr2VC-BvOa0DUE0LiwJqZs_6lP1nZVVAuwMPBfzZ0yj-MzwfRFM2FzKtVMq2uP2S3Wj4hp2yEns4bgZVixYRunT8hv81kgTyVDPuJ9ogPOjq84-9580io5mPMfy-jLPxv0FvYowCKmVqb27nw5RNf9bJPBaAKsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف در واکنش به قیمت ۹.۹۹ دلاری سوخت در آمریکا، ویدیویی از سیمپسون‌ها منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/147274" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJs77_WJ4QfqnqkN986s7pAfl66gMTjh8Hrb0YPkoRcAVAwkAe-0iZ3-zwuMao1GzRhVXsnvi8gMyg6FjDOVxmghSdb4jl8WXlSu2S3fq98ytZ3GDOPjXw_uCSB2GXxJmZFHEDqB2leEzS7j5-88q4mIs-fkoJRcdvgGKpb8V3A7v9t-ze9KM4q1Qi7w5SHdtcraSBtU7V0-hUWKEGXe1E1ALvtkzTDe5a2nA3BusmUhA-Gd7d2cUsXLEZpIf4AOEdSUJrd_RhGW6RMjuhoyLvkO6nkHzahwVdocNO2Z_-h-4K9EzhJ2sjv016m_JTr8h0u2sU18J2c4EgDhSXd28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار بمب مقابل یک کلیسا در شهر حماه سوریه
🔴
یک بمب دست‌ساز مقابل یکی از کلیساهای شهر حماه سوریه منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/147273" target="_blank">📅 21:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: پیشروی سریع انصارالله در یمن «قطعاً یک نقطه عطف» در جنگ منطقه‌ای است
🔴
حملات هوایی به رهبری عربستان به‌تنهایی احتمالاً برای بیرون راندن انصارالله کافی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/147272" target="_blank">📅 21:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که ائتلاف تحت رهبری عربستان سعودی در ۲۴ ساعت گذشته، ۵۸ حمله هوایی در مناطق مختلف یمن انجام داده است که این حملات مناطق تعز، لحج، الجوف، حجه، البیضا و صعدا را هدف قرار داده‌اند.
🔴
این حملات توسط جنگنده‌های اف-۱۵ که از پایگاه هوایی خمیس مشیت عملیات انجام می‌دهند، صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/147271" target="_blank">📅 21:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سی‌ان‌ان: عمان پیشنهاد ایران برای دریافت اجباری عوارض را رد کرد و پرداخت‌های داوطلبانه برای ایمنی ناوبری و زیست‌محیطی را پیشنهاد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/147270" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سازمان بین‌المللی مهاجرت: حدود ۸۵ هزار نفر به دلیل جنگ در یمن مجبور به ترک خانه‌های خود شده‌اند و حدود ۲۰۰۰ نفر به جیبوتی رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/147269" target="_blank">📅 21:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
لهستان: اگر روسیه حمله می‌کرد، فورا شکستش می‌دادیم!
🔴
وزیر خارجه لهستان : ما در قدرت هوایی برتری قاطعی نسبت به روسیه داریم.
🔴
اگر اوکراینی‌ها نیمی از ظرفیت پالایشگاهی روسیه را در شش ماه از کار انداخته‌اند، ما می‌توانیم این کار را در شش هفته انجام دهیم و نیم دیگر را از بین ببریم.
🔴
اگر روسیه به ما حمله می‌کرد، ورشو فورا مسکو را شکست می‌داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/147267" target="_blank">📅 21:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سه منبع ناشناس به خبرگزاری رویترز گفته‌اند عربستان سعودی در بندر دریای سرخ خود در ینبع تنها به اندازه پنج تا هفت روز ذخیره نفت دارد و مقدار کمتری نیز در مصر ذخیره کرده است
🔴
توانایی عربستان برای دور زدن تنگه هرمز و ادامه صادرات نفت پس از حمله به خط لوله شرق به غرب این کشور به‌شدت محدود شده است.
🔴
این خط لوله روز بعد از حمله، به‌عنوان «اقدامی احتیاطی» متوقف شد. این مسیر، تنها گزینه اصلی عربستان برای صادرات نفت بدون اتکا به تنگه هرمز محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/147266" target="_blank">📅 20:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=jGp9AjyPx41S4eiSQoA33gl8JkiYbv8z5jK2Yo9i2KkYUYCH4ASK_FD4PoXXzDA_uBfECA8VLnNRdNq6DS-9wBoaKiwFrvjUYAaSoibMmqD81kW8hIknFzoR3yy-4j1Ck4vmh6hvsNL_sMGK1S36EE8cmh4DP8hsoIJb-Gljm5TlWP2F76TRtwI-UoLX-oC4KfEtEm9C-HAbYM75ecPF5m2mmaHpJmcht2JYninlzpXLwyBPUypSQqswMRBdLokpvJXX1boheY36ECZZZa5izWFoKDyEUi7sf6BrzCS0l4ClaXVXwS6hdulM5GmzW_45rCUKhX7a4sQ_hBGeqpA5cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=jGp9AjyPx41S4eiSQoA33gl8JkiYbv8z5jK2Yo9i2KkYUYCH4ASK_FD4PoXXzDA_uBfECA8VLnNRdNq6DS-9wBoaKiwFrvjUYAaSoibMmqD81kW8hIknFzoR3yy-4j1Ck4vmh6hvsNL_sMGK1S36EE8cmh4DP8hsoIJb-Gljm5TlWP2F76TRtwI-UoLX-oC4KfEtEm9C-HAbYM75ecPF5m2mmaHpJmcht2JYninlzpXLwyBPUypSQqswMRBdLokpvJXX1boheY36ECZZZa5izWFoKDyEUi7sf6BrzCS0l4ClaXVXwS6hdulM5GmzW_45rCUKhX7a4sQ_hBGeqpA5cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147265" target="_blank">📅 20:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147264">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fa531cab.mp4?token=lHQ81s4wVFJ1lNvrd08WrGg1I7-R4R9blip8fJY9QW_SxxFxjbpUzOkP1iYhnze0AlltOt7aWmxYLRuY0jGn7MsNctS1Tb9ibQyrHewDZymNn4gRucG9CtpslRpSUrZPemtC-h43zGLGie5TytOTtLt6WlVxVLnRDn7tnUg0ILGt677m6k_CcElXqs3Xz3hTD8JNmvPZ4mPQ78XxMEOPzH4mIFIXONaekamgfx_Cz0kwGlyiB7CsiWskGmR3lrGgwspyDPCB98ZUZHNv5rQ2uNHW3bXFESEYMlWXnVYCECu9OESfDCE48MwyW8srP3rooi7oa5o_YMD9K9Z0GuzsGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fa531cab.mp4?token=lHQ81s4wVFJ1lNvrd08WrGg1I7-R4R9blip8fJY9QW_SxxFxjbpUzOkP1iYhnze0AlltOt7aWmxYLRuY0jGn7MsNctS1Tb9ibQyrHewDZymNn4gRucG9CtpslRpSUrZPemtC-h43zGLGie5TytOTtLt6WlVxVLnRDn7tnUg0ILGt677m6k_CcElXqs3Xz3hTD8JNmvPZ4mPQ78XxMEOPzH4mIFIXONaekamgfx_Cz0kwGlyiB7CsiWskGmR3lrGgwspyDPCB98ZUZHNv5rQ2uNHW3bXFESEYMlWXnVYCECu9OESfDCE48MwyW8srP3rooi7oa5o_YMD9K9Z0GuzsGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده مرکز فرماندهی نیروهای مسلح ایالات متحده (CENTCOM)، ادمیرال برد کوپر، می‌گوید که نگرانی‌ای درباره کمبود مهمات نظامی ایالات متحده ندارد.
🔴
«ما به خوبی تسلیح شده‌ایم و برای هر سناریوی احتمالی آماده هستیم.»
🔴
در پاسخ به پرسشی مبنی بر اینکه آیا نگران تهدیدات آینده است یا خیر، کوپر پاسخ داد:  «من نگران نیستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/147264" target="_blank">📅 20:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
با وجود عدم پیشرفت در مذاکرات مستقیم دولت لبنان با اسرائیل، سفارت آمریکا در بیروت، از دور جدید مذاکرات دو طرف در ماه اکتبر در رم خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/147263" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147261">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: تنگه هرمز اقتصاد جهان را «بحرانی» کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/147261" target="_blank">📅 20:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147260">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پرسیدن دلار 235 تومنی خریدم ریخته؛ چیکار کنم؟</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/147260" target="_blank">📅 20:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147259">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
قبیله بنی حشیش علیه حوثیا اعلام جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/147259" target="_blank">📅 20:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147258">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مدیر سامانه هوشمند سوخت گفته خودروهای بالای یک میلیارد تومن دیگه سهمیه نرخ یک و دو نمی‌گیرن
🔴
پ.ن: خب قرمساق مگه الان ماشین زیر ۱ت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/147258" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147257">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا؛ جنگ علیه ایران ادامه ندارد و اقدامی که اکنون سعی در انجام آن داریم، حل‌وفصل جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/147257" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147256">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147256" target="_blank">📅 20:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147255">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oli15fAwx43cem4pbw4iamLvBRfmVSTmdLffhLL5Cy0TE8r0b9yYWdRCpVjOJMCjlFE6X3rb-6nUEb-ajU4FeKY0SvIP8qK5MSQM69EPewb5IFoLfJIjzPqHnrsf9M94kwCueDtrcY4xF3wdk2CYsSBuuy9R2mvj-rrICEkBabEOr_6RTovpnn9I_k0lhw8I4Ic9lgreDBCylDjBOCOK3ErTKYtzDP-DDKUBzQ2hZasm2XCRU5sY6dpy9_W3hYNuRWR2ea1oGayGc1x4ywQuZ6anKxOP_mVApwgOOLcVSBSMtOymXc27riCJcjX8xlOHUkAuPo0XVu1NeG4glen6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی به منطقه‌ای بین شهرهای زوطر شرقیه و مایفادون در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147255" target="_blank">📅 20:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147254">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ0lWxTndRS1diFLv-ruamDOulIZD83KSJXfXCUe2IT9QtaqPLlfBCagvCqXHJcQ0V7hvPLXThnxaBCElEFkiEArwcyOQuCiFoZ27H0ls9VYQCG42_5Xv0T-ccL49dfH_7hIXZO7152ViVnT0rqqwjUvYmE-maS-GVpX6oZvdex57fpdA_iAMiQ0_Tr7gcqT8RRlIl4Ye0bkf6Jrk46WCDS4e288649foiGtWMlivfGz0Xd4hyn_h2egPzQoz9gROMYS5Yh1mdQCJKlU85mQEgLuoiTgYllS-U1nVASiSgVa995rKl_ZMQNGDedCc9FtxPtKub5NAobGfcs2J-JMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست قیمت انواع موبایل ریجستری در بازار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147254" target="_blank">📅 20:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147253">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه رای‌الیوم: اولتیماتوم سخت عربستان و اردن به عراق؛ گروه‌های مسلح را منحل کنید یا منتظر پاسخ باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147253" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=v3EnAxxRwArDetU8cJVQuOmRE1VeT11BA0lqXVxQx3896n17lscaTCq2cWPHqK4Mp2y6LXduCbPTFEgIhfBAF9WNZdNQ-tYzWYp2-kYPwDhtgxG0WU_oweRkBXISw3NMM5eZxxm6TtKD3HC5RSvdKxzHK_lLb9ztGGV12sFDVEdyFOHhr4ouR6TutwJxZvvE14JMPA-Ye6FGDCnlVUsMpBSI-sdDw4NXphIi0xY7hM0MxYr3XKBKR72KXy5pfjng9suUx4bAAZtfiss6Crg0PY-zGr3ghMBaTV6-hhQwJfK5SjL25WU5O8XTcPm7Q89xNZRShQ6Tx-5hDq48eOqExlcSgHOEI-kIlLISzfyyTfNBOO8lX3KMc4Fsy7uekp7RKiZ9nr825PgJLin9h6XqNxx0mZWbWQrUE-SCumMfUV8Cm56Ju1Yg6u9XXag9dBHJ2CBXz4-MkrMor7vpZVLR2dnT8O4InAkDCvI6r3TeaOQ1m_-q5w77SDY6zeE5UIf84kJKLKyaRTFcSCyQ11K5iSW1k4ZK92j7t_GGZb7-DO3-7j6rcDITL7JtMdCtL-N3Yf2QsMOzKUXiBHN-SX-vVgeHz8weJnJO-8oyFFxnF_YhrLH_ggrk8Uk5-6EMh2W3pBhjl6eu9xid2FBlqZewdP0qWU9vVnWBy1VQmWaNt2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=v3EnAxxRwArDetU8cJVQuOmRE1VeT11BA0lqXVxQx3896n17lscaTCq2cWPHqK4Mp2y6LXduCbPTFEgIhfBAF9WNZdNQ-tYzWYp2-kYPwDhtgxG0WU_oweRkBXISw3NMM5eZxxm6TtKD3HC5RSvdKxzHK_lLb9ztGGV12sFDVEdyFOHhr4ouR6TutwJxZvvE14JMPA-Ye6FGDCnlVUsMpBSI-sdDw4NXphIi0xY7hM0MxYr3XKBKR72KXy5pfjng9suUx4bAAZtfiss6Crg0PY-zGr3ghMBaTV6-hhQwJfK5SjL25WU5O8XTcPm7Q89xNZRShQ6Tx-5hDq48eOqExlcSgHOEI-kIlLISzfyyTfNBOO8lX3KMc4Fsy7uekp7RKiZ9nr825PgJLin9h6XqNxx0mZWbWQrUE-SCumMfUV8Cm56Ju1Yg6u9XXag9dBHJ2CBXz4-MkrMor7vpZVLR2dnT8O4InAkDCvI6r3TeaOQ1m_-q5w77SDY6zeE5UIf84kJKLKyaRTFcSCyQ11K5iSW1k4ZK92j7t_GGZb7-DO3-7j6rcDITL7JtMdCtL-N3Yf2QsMOzKUXiBHN-SX-vVgeHz8weJnJO-8oyFFxnF_YhrLH_ggrk8Uk5-6EMh2W3pBhjl6eu9xid2FBlqZewdP0qWU9vVnWBy1VQmWaNt2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نظر علی دایی درباره مافیای خودرو در ایران:  کجای جامعه مافیا ندارد که صنعت خودرو نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/147252" target="_blank">📅 19:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147251">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم به نقل از منابع دیپلماتیک منطقه‌ای نوشت محمد بن‌سلمان از طریق آمریکا با اسرائیل تماس گرفته و خواستار دریافت اطلاعات و کمک‌های دیگر شده است
🔴
به نوشته این روزنامه، هدف این درخواست جلوگیری از بسته‌شدن تنگه باب‌ المندب توسط انصارالله بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/147251" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaifjZ7xsbO4WGmMbHEqlpJneZOoPxuSe5R2w6vPNbTUHP8qK0JoPf7CWRYUKg2_HQ54WkHSiCGGORJIL2GfzdgLKOaC4g0iTByhrWprD1VlPdJw2Dq-nlujC_bwegilskqx1-HzJX8xgUCnTbrM-ArYVra3C4dD2215Wu3kniltg1p6uc7ngwz4eb67QaG5VjoArsWg2wOGUbbty3ybLnJXAHs_WduESTUCJcdEHlQl4dUGZK4q8bKQddX9M2SpsJzoCZq6KG0IBeWs1iKAzrCptXU6zCqi3h0IoCw-tO35BKux1k5z5qP3ubRHK8Of1_yDdRfoEZqNXCXm2spNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: جنگنده‌های سعودی جزیره حنیش در یمن را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147250" target="_blank">📅 19:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147249">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع ارشد ایرانی:
نشست روز دوشنبه در عمان بخشی از برنامه ایران برای تقویت اعتماد میان کشورهای منطقه است
🔴
با این حال، توافق به معنای بازگشایی خودکار تنگه هرمز نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/147249" target="_blank">📅 19:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147248">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtFKrFVsw-t9-jFs1vOM-OqK2en6WeFHEA64XvLwWoy6u4U4B8QCM7jKX3T3_X3fJiwhyzAY3RVcXjKtOrb-ss5kO5L984qTxIFylXab3y9hMXDZXMXoNCU2AGizEdh3-pjJI0qcAYNLHSOiQUoUcN65vMIJLbOfi6N9BXJJGDCKqlxd-o25IMbrsTwbbVk2FIfnlDs2F5HMKnF8rm0CB1zcApb_6fA5ZJOzSUd_IvOlMpbUT07TUyV5F01JHEMFDMuW542PO7N7E46XG7MsXgg0vZM1ckgkptd8QSwr_vg4YEKw9zPbE1C3A5pIy8Xa_JyZDa1-bHS9EXaaGMBL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نقدعلی:
رژیم آمریکا رفتنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/147248" target="_blank">📅 19:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147247">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6466153e9f.mp4?token=kXJ-dzYVl1LTMgbheHpi3mGpLvew7EfAWKCaHMp5ZS29hoI8iukaWxjrSRWwzVrmqLTH3vgcfzbw8vzfylo0DF6zM7lRNlQwq2IIugoqw5oEnw_e0VD3bqjW5TjCVejmEhwb8qQGeEa-_U8UojcpagTRGWExYXDstAlNOdHCI1mLXRta3ueC0UNSSF1MTpbZ2SS_bX0ICuTlFwfoUi8cVKeT2DUMtydVSF3-csFXWVgW245NuVFkEwpZhs4wS7J7-YJjg1HNubsBK-qmJM1eyk3Twhs7AIN86b1EzRgZCULrMwA89UwknJmblwX4-qmPNBmhT6TquZlpBSpeUkMK3lw7LR61PYPrKV3TECOdmNNiHkvwNO19wR4DUcMwgVz7Mu3Dm8U7FtWdrACnQTRw8VXWkXCUVHNJz2cKQUKXUrNDDv67ZLDBIABRfVvssvO6gcH4-yDHaiBBBezjmKdQ8DMyYHEPI60uZYa9kPrNhqwrL7Vcx7a1tmmHbpOfUz7WtA5riUVR3nMDD9FZi5Zk98GANfNzPCVaFTo-2NMlboPu2n6GrCSmQ__GrW9mO3nsanOp2gTAfvBNngBv-utUBMkcQeXZIkAiql0f3uxuWqvxFMfQpoOka79sQhMcwn5S0EmNjbtAOqqA9K_-XViBEoLK-IQhWuUL3IF_mxLw8Eo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6466153e9f.mp4?token=kXJ-dzYVl1LTMgbheHpi3mGpLvew7EfAWKCaHMp5ZS29hoI8iukaWxjrSRWwzVrmqLTH3vgcfzbw8vzfylo0DF6zM7lRNlQwq2IIugoqw5oEnw_e0VD3bqjW5TjCVejmEhwb8qQGeEa-_U8UojcpagTRGWExYXDstAlNOdHCI1mLXRta3ueC0UNSSF1MTpbZ2SS_bX0ICuTlFwfoUi8cVKeT2DUMtydVSF3-csFXWVgW245NuVFkEwpZhs4wS7J7-YJjg1HNubsBK-qmJM1eyk3Twhs7AIN86b1EzRgZCULrMwA89UwknJmblwX4-qmPNBmhT6TquZlpBSpeUkMK3lw7LR61PYPrKV3TECOdmNNiHkvwNO19wR4DUcMwgVz7Mu3Dm8U7FtWdrACnQTRw8VXWkXCUVHNJz2cKQUKXUrNDDv67ZLDBIABRfVvssvO6gcH4-yDHaiBBBezjmKdQ8DMyYHEPI60uZYa9kPrNhqwrL7Vcx7a1tmmHbpOfUz7WtA5riUVR3nMDD9FZi5Zk98GANfNzPCVaFTo-2NMlboPu2n6GrCSmQ__GrW9mO3nsanOp2gTAfvBNngBv-utUBMkcQeXZIkAiql0f3uxuWqvxFMfQpoOka79sQhMcwn5S0EmNjbtAOqqA9K_-XViBEoLK-IQhWuUL3IF_mxLw8Eo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:‌ با ولیعهد ابوظبی توافق کردیم به آینده نگاه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147247" target="_blank">📅 19:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147246">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۴ اسرائیل گفته ایران داره آماده آزمایش بمب اتم میشه  قبلش هم میخواد از npt خارج بشه!   البته ممکنه این بهونه حمله به تاسیسات کوه کلنگ باشه.  @AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/147246" target="_blank">📅 19:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147245">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzUOWSaL_iYgHlnn8jV1Saj3n6v0MVQaWFlktjC0kztlrGAF57VEeiN0EjfuO-Y5u4aM6-6FWQi8jt0jyAKRAyUfRMuonkslikW2tbBT39InUgAxTRtkxymI6jDzvChkg1CnB3xtCtVKLH1YrG4iN1DrXkCc3Kp9fLEYeB4fZ2-7x-P9mX8Rxixe-Ix2aP9doUIubHOfX17bv51vTw4HfeD5vMSI7eJWrHMaz_qyk_knULDmQFqioOmE442K499YM88aupTwcIczRnE91ZPkORqRUarkvontNGTCWhLKMCNnU9ebDdINb50uRptnvabWS08sLVzDwfDx3C0l3RgJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر خوب/استاد خوش چشم که بخاطر تحلیل‌های کصشر و اشتباهش ممنوع التصویر شده بود از امشب مجدد به صداوسیما میره تا مجدد تفت بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147245" target="_blank">📅 19:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147244">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
فارس: اگه جنگ بشه، جانفداها میفرستیم‌ جلو
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/147244" target="_blank">📅 19:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94a010ef6.mp4?token=gq3sMwr3evsLKVu5EIPV_RHKJtr0qfgu7YNdhd-Jnhy4D5j3qIRnMxnH11TsdH54_vAj2JEgb-JUx_oBlsaKxSKohUTBMg2Q3DvclLIxG8002q7mT0mWnglzR5kz1SW9XUoeEDoKV4PpZajfH347PfKDwFcc38U3m3WTYHivEO3G3LWMpUGLIamaQPO3uE_KGEfR86fqWnHv_cvZVm--3jKkZBvO44soWCIf7D6zgZtitEYLvJ4uGwIyoURc4QlpnFWHwDh9ulzDNj7arjvq7XgOwlaPrMCOH2tEeVLacgKczkn2pZAoLett32OhiTyJ_CnCDwxS6lSKWtB8hePDYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94a010ef6.mp4?token=gq3sMwr3evsLKVu5EIPV_RHKJtr0qfgu7YNdhd-Jnhy4D5j3qIRnMxnH11TsdH54_vAj2JEgb-JUx_oBlsaKxSKohUTBMg2Q3DvclLIxG8002q7mT0mWnglzR5kz1SW9XUoeEDoKV4PpZajfH347PfKDwFcc38U3m3WTYHivEO3G3LWMpUGLIamaQPO3uE_KGEfR86fqWnHv_cvZVm--3jKkZBvO44soWCIf7D6zgZtitEYLvJ4uGwIyoURc4QlpnFWHwDh9ulzDNj7arjvq7XgOwlaPrMCOH2tEeVLacgKczkn2pZAoLett32OhiTyJ_CnCDwxS6lSKWtB8hePDYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رؤیت شده در شب نشینی‌ها؛ عرزشی‌ها شعارهایی علیه حسن روحانی دادن و گفتن «از آمریکا تو دل بکن، خیلی خطر داره حسن».
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/147243" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
