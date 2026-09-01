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
<img src="https://cdn4.telesco.pe/file/kfHfrG-F7S42UZS4SkgpODQGFGeM6JtXVwaLEKrXz2mdlO-Cgb-pfo67mIceLgv44P1DqBVtlh6fVs5GhuWwu4GLWV7Li3W4MPlH9EExvyV4Wk4s-l74tje4kov7EsM33sLMjq1l8bTfH7cyWyJVWSJQmuvuRhFpf-3VMEK9fDYjvgVKsxIyNrnCfZxLlvscXVSeKm3ylgQRnz34821peSBPNmDQHaDTmjr4XZrkrQw_wnbKqc05FfDf0ATgongMfsOLQuZY_WrGhnfRYctuDDFIV4thZVHi-s2R-se_A7zBVHEFJ5acOXQEjh6AQyQQ73pRJySHt-Irw0FjCnwQmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 610K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUe9r5Nx9OkhdBPIa-Z_RINC1Rf0uVPHHSKV2EW2T_uJ67bObwaZf_riiNcORHV9gjYnpYD6CXn43SxE6F2t8ia0n6uJGe0oEo9i5bNqRi6xiinXwECIGaC5Al0UMfQQ2yABcwiJabZFiPZdmVQfcMx09CNWtVvMgYV_Lt5ZmOWlMfh2Gu70PYrTU4iuiFrO7RaI-AZiVhsVCfaSU3n8AXa2GcIiOL7UMORGLGrzO9f2vXD5-aObQ92DVC8Iuv2YQ9C3KcfB5GL5BmHO8o7RWsJsBaX7zXoTyW10XapKhfPrY0SVj0Ux54vAxaV0KrVrODylo7NfcYAhr-vPn2YRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgnXGnXoAZoQwYgfGtgs7p_kudFYvRtgGfd154HGWIJfRnK9W4dce5pfjz79RE4nrCoonl7SMWOk6XUzIfQ5Z2BSwlenhzCHX5LaaNm1dwv6wjBrs-w0dKcwwXEnPleNoeQ-pvMnW_YsyG6tbg2nCBR0M_HiKC3r3kIE_A6qJR-v6R9Qv7zDodxpO8ColjXhfrAfYaMnzSNPX_yI642vAbIchvJTi4LUzpaSgTHfz-F3tfKdrB5OTJIu_y3SvlZ6yHgKPBdKFl6QGQZJKcavJ5H6PbffqYt8EtdJVorXItYLlhT7oKragTiZ11UfRel4kjzCyjuDzi3GV1MfFZSnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28856">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqRJcT8GqTZew6Wp2CiaEb0iV1FBvINymOI4s0RfzgtXkL82forWNBXz5_c2Q5X8qMmiOAbSxcpeYn7-vXzV5huj07tFjyaExI5T5cXp-HdxACagZcUBCWvicvMtYGC6iTS8GScDM8LdcTwY-Q_tFqc-xZAWkixA7WDg8fj5IG40PlCFiZ7SgfwgJck9xBB1u961at2i58B9-9NZgLmSGieD7zslupo0tmD2TXQHU7rHfEe7zGqLVlbBHDeUmST4Vb3oif12Hrfs66ERO2SBgJavfb_JCwjbWRZajLW0Yh9XfELTBwoxIYd9I8BIV4rsUuj44KIxJgjQjcujltX5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته پنجم لیگ برتر ایران
🟣
شمس آذر
🆚
تراکتور
🔴
⏰
ساعت ۱۹:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ شرط رایگان بر روی اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/persiana_Soccer/28856" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=o0B3wGuJmN-dcbcPsuUS1U40LVMuWYCHqOBCybqKfSFn6yWUNRwyZznWK-kwufSQ5u7FPTRsugofLJyhm3fYCXAxeh2-GW8sPR4Qyfph4doUmO5AX7LKFQUk7iTPRoDEMhDAe2IZ5FcEg2CcC16MizwJZ-mLTWyGhMZcGFeLWz4BaJomfql5dE-HU52jYNhkqpmFy94zObMkES1R8cKAk4Mi3RfJyVHhuvKdwf-_BSIjOk5CYQu7pJZzNqEarweMIJxRqgjlYeePNoKuVVJ13Z6ZldC_NSKdjEA992NjRc7CfEqstxV99Bd-3GAUw4Oz7sSGjxN4gOQLZS7OQ_pVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=o0B3wGuJmN-dcbcPsuUS1U40LVMuWYCHqOBCybqKfSFn6yWUNRwyZznWK-kwufSQ5u7FPTRsugofLJyhm3fYCXAxeh2-GW8sPR4Qyfph4doUmO5AX7LKFQUk7iTPRoDEMhDAe2IZ5FcEg2CcC16MizwJZ-mLTWyGhMZcGFeLWz4BaJomfql5dE-HU52jYNhkqpmFy94zObMkES1R8cKAk4Mi3RfJyVHhuvKdwf-_BSIjOk5CYQu7pJZzNqEarweMIJxRqgjlYeePNoKuVVJ13Z6ZldC_NSKdjEA992NjRc7CfEqstxV99Bd-3GAUw4Oz7sSGjxN4gOQLZS7OQ_pVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28854">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbM5RvReRumIRbolKdAwt6_3JuC5YJDX_KuPh2xa2YT9yzti0-XzOVFJkiiCtLKkHpjhWqROrui-TgUCWjmjLAsX8UkZAqcBvUTkXXpoMO6LLrlGlEmpmURHB-lhNxsnKYrUzkst4DgccAEK0ps1YCUYBrR1kJ-1hB0Pgt0sBMMBOpvDGkw9OqDkVrSo3X-1NCfHOtjlzHBG7D4Qm8pkNCUQYbhG6EvNP2Er1TkjRsjjfV6zgyOymY1fbG8WRodEGtjvvNwv6NE2O8bw-fEmxg38SUXiGtFDj-foUvkpdgGoJ226A818xAUC0SmVTJOKqkMfdN34SppdM0JtC1igbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/28854" target="_blank">📅 14:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28853">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔵
🔴
درفاصله کمتر از 48 ساعت تا دیدار فرداشب استقلال
🆚
پرسپولیس؛نگاهی بیندازیم به زود هنگام ترین گل های تاریخ این تقابل بزرگ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/28853" target="_blank">📅 14:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et6Zkbem1VhsdbHLEzWOzlCMpGOKTgxiRJ2xsNw9AaKLSJsVOydpSMEiKuXz37H5JtdKJnxR7XMQBocodZKMuFthVa30K-k0S4I1N4YqT8ecrDxwh_hXY1tukKnDEtUue2KEOkNXuGqGzTIkWJ06fevM2-zeFEguG-6f3CIEB4X6309Jx4e7tLpVht9N0NNtPBl3VItyMFTrnbrVsrqnZd20Vv7SzkHTnbHAjpMccBu2N32UnVGxTZXsa8bXJTdjEOpAimgyD9d3tT6o4V2SeUR7NAeNsae9asPdG3iUFwa_B_NRNfncf90LKbUESBcXvZDzQwhBIsTCdwZfHtOV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B16do5TEAKQTOwdX_LgctMu8G_oPLc6mydLjUuwxn91z6iOWuhQqHKA2KhgLO1CEMljwaQaV86oKnzlYiZ4b_ljVKStsmU6e5twIyNAWoXTdvLP0ls28iu4p-PztayserQ_7TvbpgMzbJ27-upGDg1ZbRdBeTc2RH6jhv-oDjtbIHvSauHqNU2i26-3ba0MCKOk49ac7Z5goZSHIup3yKZEzxzNGAaPAfG01KVmeGsl96wj2BdzjJz4Ky39YYCxiCWLVqQbFv6YDJi9VZaMzt7uLe2PmNorU2Rn1LdvbQsM-AO4c5IyzevYiA2_7VaYENqNCrlbJSYH_xx1Yse2Cig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/28851" target="_blank">📅 13:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28849">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxjRZs-U0-YKEmH0W-d_JHmsbl59j2faGKi8AhwE72A6vrt2m1pFb4VGXfgbFNhCOoA6EMdc343vXhyV1N406ee_NVw_4LPznq8sTxftBNocEOch-_vtL7upkcPSUhAc3IawzKSqzXnNn2Gza9UHQAb1IsRlC7o9afRHOwDwdDk3e0pPuODMcllSxT8UTRqoxCQDVXUC-nkQA8OQmTHYah5c6tVBoFg05OagPEYyEUjR_0X6Ou0JsJsyffWzQciMBpFepjFpAqIDzmCmfWfs1PkqHBXpKmr9IFUfNsUgSJQizaw52MD5vkBthWxZUFnG-XguoABJ6E22wwLgdFMyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cF8kko-gLUY7g8-rWSDgLvS4MqybXYkXee5YaJoJx1pLwFhR_ZUsFU2ICzjXQhrxtFs0-vPICpxtEj3nmTSQVy5oKDG1ikw0OBn-V7GPySb9RmobIW7R3QXS3GpqaP6yEdm1qvOU7ybsnd_IJYWUrfACUVPjFQbuXhW0Yk-QjPLTIk7KusRSvDM6ECl0_33NkkYlrFi0xjty9USTaTdCFYwYCFdtltc7lwBiADiJrYm4BTdV9nwbzsLcw9tT2itxZIpFajPRvoeHoz_GWMvzC4kMuNFNShauBg2fDUwIlCFWyeYv4HsZZC5HGofrwkz1kKuTiOJxxl_hDLMF1fQY_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
پوستر فدراسیون فوتبال آفریقای جنوبی برای پیتسو موسیمانه سرمربی‌جدید تیم‌ملی این کشور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/28849" target="_blank">📅 13:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYDRTBKXKsSZxy_YTTpSUy6b28GaNodnETOO6swwtnJqT1_B2aOGcb51jslQQ18aSZOD5Ry4E1ID8lpjpixyltRpSKBKu7fTCvtiGfUzdlBK1PNOBOdkUorKY3OVOiwYZ1mRMANfWvJSYSrxDCV5TjtDKCHqZCakfPlwE0wcjLCnPURgy76A8EdSSmu0YEDLpLx1rcI-4sYA5TRacAjyLRce2FGNwKlUCrP8KiPj1-XgToTBmVwOeagbXhACWHqbXTsBSfDo3yT3GyfwKO5rrOO9K4Nt99uqGymjWGsbM3XqMopg9IddOvcWdqgWRMKmNFl6UFHQIWQh1tB08pvx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
فابریزیو رومانو: انتظار میره تا فرداشب که پنجره نقل‌وانتقالات‌تابستونی بسته میشه انتقال انزو فرناندز ستاره چلسی به منچستر سیتی نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/28848" target="_blank">📅 13:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj-c0eG-n-ZFuOCiJ1WQowOA3U7-kD8dmP9GmVN6u7HjidTFK7gvbDMqY-RVDnhLfuDicgVDveIpn-Ei_d7s0DIbqJ9fy-LdWjZ_kWP1ov6HGN7QopSbY0tMEu9YND7rSxMdL7dnkku9_DvOHrvw2Dx9wwLNlHkOtgQDlrT4WjgEpExPqoxOVsp5Ge8pCYKQGCUTOB01nVlTGiZ3doM1-jh74LSrdu5tCsavWT5fTQCo4Ujj5cyRFjVdq7wq0X_3FIi3dfry2h8p4MhCRaiw8WH8Ch0Sf1SkXV0GNo6hmUV8hatSced0uthvgw0T57eqF5KP87FAELMFY9O1aArWjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مورد جذاب گابریل آرتتا پسر میکل آرتتا اینه که چشماش دو رنگیه؛یکی‌ تیره‌‌تر شبیه‌ پدر، یکی روشن و شیشه‌ای شبیه مادر که توجهات بسیار زیادی رو به خود جلب‌کرده. جالبه‌بدونید در دنیا تنها چهارصد نفر چشاشون‌دو رنگیه‌که پسر آرتتا یکی‌ازاین 400 نفره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/28847" target="_blank">📅 12:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28846">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEntTZ-1Drb6yVAmO3O5gnaug4968cKFjZlXxtQqw7-50881wSunOMuFVAOiHuFm2r_uW8s235fPpOhPMbrVsAeeE0clivEyqNFC0RH8yIKbDbi11OqphdkCTB--PBh0j7uIoXe9kQrUTmP1NSsxAZreuUpzkw9M41e6plakLTwYN6TB5N-f2Kph04gBIorhoWx_UWq5MU5CAThmIwXX3W4rreKKDqBzpvWhP9ddgUhO6R4ASZnf9c3ErRb3oZ5B46s0E0PDZY3mA2KGus8m8JUoz4TxczkxigXeliqr1UIdaySXYYnYJJQrKiUNdHYXcxvo_ZQE0QNFz9X4ERkE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
نشریه‌مارکا:خوزه‌مورینیو ازوضعیت ادواردو کاماوینگا هافبک‌فرانسوی رئال‌مادرید راضی نیست و به فلورنتینو پرز گفته او رو بفروشد. پرز برای فروش‌ کاماوینگا رقمی‌بین 60 الی 80 میلیون‌یورو میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/28846" target="_blank">📅 12:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28845">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
ویدیوکامل ویژه برنامه شب گذشته عادل درباره اتفاقات اخیر چهار هفته ابتدایی لیگ برترو افشاگری‌ های عادل علیه فدراسیون فوتبالِ مهدی تاج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/28845" target="_blank">📅 11:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28844">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZpM5Z8HS-_U3D1LW6X6hOuUH5e4yIDbcogNzPIDeAfAYRR5gkicW7uH0aYKWS6fCphOxHbw_A-Tgu1uKz2nBGuqdo0_ybjdtPyNOELgI3SmFMAtrOy0LqBpe4Q_Neo1Y8Z758e3dyAym5lFsfAzMMf-wTIIj7Syv3PleCNwHk2vOoXPlexEwbP6Kk4CvjNuXxUqijmukEfQo956Hlzp-m4XujnWmYUxUdqz61PtBlpfhPiftHF1NKeFbMtlZoBnN-K2-Q3-a7UVzBLBnLCLozUKwB6W_2qHQpSVc7X2A9ehCQ6Y0cO1j9uhIYXqeAcHY3GnjSxL7kCCbuJ7ZmaKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
دستیارسابق‌انریکه سرمربی تیم کره جنوبی شد
؛ روبرتو مورنو سرمربی۴۹ساله‌اسپانیایی‌ودستیار سابق لوئیس انریکه، به عنوان سرمربی تیم ملی فوتبال کره جنوبی منصوب شد تاجایگزین هونگ میونگ بو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/28844" target="_blank">📅 11:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28843">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeXSB8kks4L_3rKvM4XQ8Jn7MFeGL6P8Haicw7ySSXqbP-VolS7mcsi8O3w_P0zYGRcbNPNALcJ0k8xAxw92kIPs7-nAPJOUXVed0m4GF0ukRzHF-gJI0JYR3HTVuiF3fuUAzjMhV3NUyMcWQxmICSgwqnfaiqldaZHU6--TrR3HOPdMJfub227j4fsKTortb9ntGpfuPsRNKAgx66bXRmiCRXKlzCHN_07-AjTpCjseetIACm6JyBpRcno-4N38ITGZJG8E7TvuD3i1cFNbGhEX_FQD-IrUiDjpoFTuL4doE14BJbhUnPd2oHu-JMjvIf2pVHswbStnqymYELI9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌کمیته‌انضباطی فدراسیون فوتبال: بعد از برسی‌های کامل مشخص‌شدکه قرارداد یاسر آسانی با استقلال قانونی‌است و او مشکلی‌برای‌همراهی آبی‌ها نخواهد داشت. بدین ترتیب پرونده شکایت باشگاه‌ها ازاین بازیکن بسته شد؛ خبر ریپلای شده هم بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28843" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28842">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=TFPFfbxiSoWdkPkdjCwv09KINlMWwQhcDqOZHJxwxWLTohQlc2AAS5rDQY53NpngP91YtJQ5kpWd46e-A2CGkQPZQssMMg9_F6LuF7r9JmK0OQFup9wECN-N29t1rwKoVJbvSm4cnAb9EyqkwdLVAgpvBB3gKtlf9fdrGyREXv_7aRhxNOSUHR58Y0pvnIOdyiTC8z2Tcdswa1zRC018IT5VmGy9DR96rtjcX5Nz95z4sVnF4tKpUuBGuS7MRUoQ1SkTsaTJ2otnPE_V6eCtUeblho2wOfof1UlPGLOKNZswpuN2jmgkFUsig139VS8Adf9yOEHnT4-gHURasqbeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbdcb0fd.mp4?token=TFPFfbxiSoWdkPkdjCwv09KINlMWwQhcDqOZHJxwxWLTohQlc2AAS5rDQY53NpngP91YtJQ5kpWd46e-A2CGkQPZQssMMg9_F6LuF7r9JmK0OQFup9wECN-N29t1rwKoVJbvSm4cnAb9EyqkwdLVAgpvBB3gKtlf9fdrGyREXv_7aRhxNOSUHR58Y0pvnIOdyiTC8z2Tcdswa1zRC018IT5VmGy9DR96rtjcX5Nz95z4sVnF4tKpUuBGuS7MRUoQ1SkTsaTJ2otnPE_V6eCtUeblho2wOfof1UlPGLOKNZswpuN2jmgkFUsig139VS8Adf9yOEHnT4-gHURasqbeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های جالب کریس رونالدو فوق ستاره پرتغالی باشگاه النصر درباره سختی‌هایی که کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/28842" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28841">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYb_8v3cGHwgfUVpNaGkTnSQAzjYIhTfceIQs7XpQ6zVZP7yWVGmqqzFowIXkjdUb8pdOsim6Ho-fwhjmkD4RDpxSBPiD9GNN7q84VY-vV08uI3cGRPNYjCZeBvsN4ZJBnhwp7QEVYgoJbhpAAL9dnR59cvfUiSqMkcSwV3EYJcS9nAofy6jPynEJUoCnvu4HjvR30aoHfRhCCHk8vXqmiG9pDTPMzzjd7tKkcDoYECYSZMkL2wJhncdXtThWfOt_nvmeJTIVvHrrmhauTgruTNOHUOneJGzwgt2tkldJbjP5iOzrZtxTF3w3S1wuRVbTsl5RX-bN6l4Np3DlPk77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/28841" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28840">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXEvf-aZ19lOdw4Rld6n1qTbZMjFR5q8dsv7VKjTICAqJ3pnNJbONFIobYWuusL4CBQqL0jA8nnvHrVejY39f1SbId5J2AP_006nCMeQ8CdFJme0pRTaZqGso42gjSQ-v-zDzE1_hkBcZG0q_uQC1faTjud-lLP7w2REMl8R1Y0r0r2uoNz4WKxp_xR-mwhTg3zmrdiXPH9t9k5JvZwKWbJl3ILIvLBhx8ik8JQc9sHAM6cd4rE2JCzQx1h5D6IMr2AJnl8dz5YGyvVm_M3SvZGtWE3SX4ccD6dPeaubKlZof4h1co0rEQtgoUo1ADLiwv4r5rsyHRDHAOWkeV6fvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/28840" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28839">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0z9MnqsFB7R4rq8MT-0y7Mb9eyr9Dce2jwHvaBFJ40uc5Cz7bQ1iiIi5d7wXS9X0RRIbwCUdz7ECLb2hfNpzMcKX3CmXBa16aj6Ik-ipMEwPQYETMeseUSDK4S9_6NJBp5vcYliA-iov7OtzhDGspSPKZRFMOyDQCnAztlccSZ3IxgqGBwOvx6-H2t62snW-JWeYddqaZbaK01xgZs0Wbd_iyYMhI7tk5Wg-78NjE9aTEmhbzDWPO1-rwH9gDzjtrRFUGLef33rximFudU6K0UDKXwEc0OaBr0FCpsPQdyFka56Z4SxzuKkWEYpLl17_zQsscLSYnqnWLQ6DrqFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تکلیف نهایی داکنز نازون دیگر بازیکن خارجی استقلال نیز ظرف72ساعت‌آینده مشخص خواهد شد. یا به جمع آبی‌ها برمیگرده یااونم‌توافقی فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/28839" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LudwxTjVbOZWjMI4DnNKUCdP5Gifk02athY5HWJYwysTWl86rwaddJdqLkrYCmEr83Q0CXKfGJH3RQ2ak1a-dbTr7x3SFEkG4KHOk5gCddMnawbNHkXS-jsLLtcaqjp_TTEVcxKaCTeCa04Ildq_cO8pJClcpKwJCNn2byhKdCLNBq_h8eHGZLyaahXVGMVAbgJLIY3TUjll2oWsSdSgN4JDkVrfAiCs-bMZYueXl22xpRs2x6vKasSI5lBUxs56PQavVSoNHIBi_ZajsL7WSvein2A_qu8VAgNQyQ4PaKwc7Lfqlt6kUqdglqZy8FpCoaXm0QQHx6lpXPXV7hHLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو خرید برگ ریزون و فوق العاده الهلال ظرف 48 ساعت‌گذشته؛ گابریل مارتینلی و اولی واتکینز دو ستاره آرسنال و آستون ویلا به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/28838" target="_blank">📅 10:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb_TG5_A_FGJ3jn8s6_YF0Wmll80wJX5pdo0VQqFHFoaoNEAY0QldJS23tsUzFniNetunGIs7dUlMYgl1n6oDH1d8_DByKyM_KeS7DvVpP7oa9znyQe3XpoQKk8SSRoLRA63ZSrH03rHh-6CMcsfhkn5H9OkJ0rKzWGNxObVzppU07FE7nQMZ9PAdfkUPvaDEmtw8WjkIPAe19kKmgt2a5Ib7oLLGUUbQ3QSOryd5C_Fma2JTH9s6xoDJ_2mka_3HaxWa-TIeeeqG6G6lwjObyffd82FE51wfyigfuK2WONuN4CGy9OEpAvUVGw6P1CQwdEPuuQTjG6DQExyB7kM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فاطیمه یوسفی فوق‌ستاره 21 ساله فوتبال بانوان ایران هستن که با عقد قراردادی به ملوان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/28837" target="_blank">📅 10:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eyq8X9vb7Q_oS5DYe2-saG6wy6z4qlwuJpBKt_RH7ggYiSQU76_WjIO56jk5HZSnqtJfJmgdDBmIkFnO8upm9sHGBoOl-TGIBqrwrD7REfgOd2WoXM-o0rzHFpEjhYz6buFkW7Tz5d4Ke54mqC5KGGWCTXl1EkSiE90fgzgVdP2u4zXGlTh5RYoXeR9W5eVUcFIKgxn7GSIclEaTxannO46SZOsSEfZKWPaFBeZA0sCX4AelhUABo4cS0H33rBkWaJp0qyM9PnCCq6FKEcyo7FR7iiaFKiwKKaYUqSuO5yltb6LZ2xSvLM8hTXyfUsphOTeBDmYdRktaM4CoDwUr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌ساعت02:30 پنجره‌نقل‌وانتقالات تابستونی تموم لیگ‌های‌اروپایی بسته خواهد شد و از این به بعد باشگاه ها میتونن تنها بازیکنان آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/28836" target="_blank">📅 10:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28835">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28835" target="_blank">📅 01:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcJz2Tgw7Bmzk8glrivRv_B2iLmZEiozTBeTnD5NTc61X7qGE01iEKzISsequ_U4sdxzhWbk_tUBfU9kUgwhDC8gHA7XeJyAO63p7Ym_n-mbxyp3MVH5WKUkkqzlQD-kFCIyQlqjSblc7ZeFNVqL6E9a_IY1hgnTC2kR_SwOKH2dN7NS1d5LNvV1oHVsglafLhTOSDrB7JV1d3Yx5P9mW3eOuXPIn5z9fdyIxpQzvRi7ddQktx6fOBWzYqeBsRwMeJXwR-BdzUFUmbn1Nve4CoKiS_F2yKwBm41ll0ccW9ecHav4_-SSsY-amooSVCfjfFPljLYCe6f-61Pt19UQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛شروع‌هفته‌پنجم‌لیگ برتر با جدال یاران نکونام باشمس‌آذر برای حفظ صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28833" target="_blank">📅 01:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_s1A9yxL0xl8nDzU__r7GfyrwRs0OzsBD3faDZjw1WfxDeMQCl6qUErL6r3CiVt6Q261qSbenvfSdMn8ci4ONpYfgYLobLD6Snul6PwXYFnXyqVz9Kt9oiCaVmNqJt0u88M83ivCe0IepDlpOODurOwa9aezayDCQaAkRgJcsMFwuhu-Ii8QCmUnG02V0mCEMe2biKP8YC2_hAcD89Ne25vPs8vUpNYUZWSyduoX-Xwkr9RxrwlZRbul7miqHIbqvfZrHR5GjHfTYJpzAmSoEJWoWnkEldaTF87ufwa22JsVEX9oovAY64-hMPYgRGp7bPMiK2dqnHrJ8lFMMKcew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
برد اقتصادی آرسنال و جشنواره‌گل بلوگرانا بانمایش‌بی‌نظیر رافینیا و یامال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28832" target="_blank">📅 01:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28831">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28831" target="_blank">📅 01:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28830">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28830" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3AaF3QcOIWgoJKlO2TpiBUlHrxQ22sU7DgCFh-ujy2-W6aeJMkZMe-A8FPk1DS9DZN4Z3dhj1MRrnliAkcJsFRcUKxOCFSr_9nOHNW-t-rVyfsvJpjiPlnh4md8moaQ2i0dNDYzH15fn3J8E1JHiRZmxQqdPl6jwQmc2O8FxqQQej1D3DSRYdQSfi1UV1iVdN9X3-oT91n7PwUL7DxUigUhz6cYP0XzH4Taw97FSUGZ-DYu2fHGzSbcU5JyAU6GAEZsveOmrKLLy0XgiQzUMOm1cmmMfgo9pH6Qxaafj4Ulg2rDPJTt4d3tWGuwz6iOYzbVaJOgPJfe3C_xSKep8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28829" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28828">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28828" target="_blank">📅 01:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFpGLog-T938Klzm8OXXEVDMdaRz8vA469MI23T3B6B_KVIA6uL79pp6L8U4WVfZgBc1HZyxFXdyfihhhRdLzB6RedE6TRk19NWPjIkYLg8Kgt70uBxu3-ez5KFJ2Ug_slLt5zkzFMExrvCBTiMOwH224iritsYp-H6e397hPazR6zVIT7K6WWeAfNt5GxDqeqloQk0fQ2uI1xZFZyaj-jMSo0k3phAFR4WIxQf4r5t-WRkneMBUJRtT7z5TnXJHNeUGTWK5WNW6L0ojSxT_v140v71fKBVuBpJSkwn63zWL-kW9lsX-8XZzVZEDLHYApFqe8jwpfUPCLrRrQKTu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت رسیدن شهرآورد پایتخت؛ مقایسه ارزشمند ترین بازیکن دو تیم استقلال
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28825" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28824">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28824" target="_blank">📅 00:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWLFJakt-SW1oux1dtT2Brdd1GaJSekGePaHHqkJwY2XuYHs22mRXbkYdmBSqCkdjn-ryOjeiT0-BE4KbAaLGDAysSbzsk4ZKsFAWWf2g0WdWNuPBZiok4-T3TMW87lAWls1VVdCfe1T9bzw_mXhKrywWaPExwYNTGqfWFu7FE14XXIlkuxwgSj15JqcYXNTRyT_shjMLeCkmK6FA5EaLwLApi64MhfZcsbiwadyzkcs2SQHwteIfLky0RkSVM9cDFFaGle54nn4_aUkSWG3klkidldMfoECJbyG8AjyaVzqEpxzk-TLYDC9Pd-PEYJ8WNClzahvao1tELuRNHRxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌رسیدن شهرآورد 107 نگاهی بیندازیم به افتخارات دو باشگاه استقلال
🆚
پرسپولیس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28823" target="_blank">📅 23:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vit0DJ2_inHr6XHWjjKkEcUyYkH6r0WtrjbNjTASGgncseYT6Z02QIIrME4_U3h6nXxK2IIK6MSu2Nw7o1NMDp9tSVlLkhPrhwazO8CrpaCcWJ2nflALga9SR1Uf_OA14Fo0x3XgwJWb8iacIfx4vsHkjtT2Vp4U3Kw2iogxv8dzRuDCWWDkEdGYs674uLnmC5rXUB9P3uAhGcd03xR2lMpZMWf3xoaQ2PV4yoZ6aeKykO6sX_VZCerUFmj7H0vqRBkWIF1EaSh2taV7KAXQ_REEQZsOqdGsMJwQy8SNcBg59IRqdp_WeBFF-x5tQMuumWw6mdYk6JeMNW3yyKfZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی؛ از کوچه‌های‌روزاریو تا قهرمان ملی آرژانتین در جام جهانی  دیگر لئو‌ را با لباس آلبی‌سلسته نخواهیم دید. "خداحافظی‌ام را در تاریخ ۲۱ ژوئیه ، ۲ روز پس از فینال جام جهانی نوشتم. امروز ، پس از فوت پدرم بیش از پیش به درستی این تصمیم اطمینان دارم"
⚪️
…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28822" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_IOqhaTPC5p-b0w50ahDwaRdTf-3dg9-JZ05fz-7kamXgiA62mj5Iy5Mbh0nChfHhVlaKuRWcU39ynCHRY4LHj5gzX9XtaVsDaxnsKO3SQ7gDt6Gib-n6WlIa5PIn74W40E1DJeHgikC5XLvXIJGdw_WslWZPMT62huzLsqyT1WQTrN7D5XxeLPH0IP3ZWbe4_qTC45UoxEnNtRtwJnHkV3pyZCB7e0tHPT0e8bDwZhqFH4C3JwrsIxJLGhgPFtIdCi4q29Mc2Qemc9d0vxrqmCYP8GqPv1YsgosGzPnSxMiTyloJTUbuaFILrXn_G3GmVdrneJ3jd_LIVAs8eLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28821" target="_blank">📅 23:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=cdUjODUVSP6lOgikHts44MSsyY_SykdfKNhRpZw8R3dSChTKTi94cj7kPMIfxZcnnTP61O1HntNNBaoLvSePwYprMCSe20NdzTqA7uAURtR7kHLeL8eiX1lRq7HMMj_RuJU3V__XYRJokvC0y5wdqJdzY7zHCsU8DIppL7Wrq1BODZF9728Xxqx3raObEmC27Sv4Wou8qXy8alIpdS5uTedXt9M_HAutBOLEMy6C18siPEhAv5y-Pa1wp6-1XaNMJmw8sw3RoABeayvm-4L2P8WVCEfsBDxyjGPDu_AOZDxWRj--554ltWB4KF2eS49mTMOokh8zRFrDTwLzn60oXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d24f702f0.mp4?token=cdUjODUVSP6lOgikHts44MSsyY_SykdfKNhRpZw8R3dSChTKTi94cj7kPMIfxZcnnTP61O1HntNNBaoLvSePwYprMCSe20NdzTqA7uAURtR7kHLeL8eiX1lRq7HMMj_RuJU3V__XYRJokvC0y5wdqJdzY7zHCsU8DIppL7Wrq1BODZF9728Xxqx3raObEmC27Sv4Wou8qXy8alIpdS5uTedXt9M_HAutBOLEMy6C18siPEhAv5y-Pa1wp6-1XaNMJmw8sw3RoABeayvm-4L2P8WVCEfsBDxyjGPDu_AOZDxWRj--554ltWB4KF2eS49mTMOokh8zRFrDTwLzn60oXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28820" target="_blank">📅 22:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7g6t1_psYj8uPFRPLG1MA0vOxgc9h8RnbCOGWoArWcQOlqkLMCnrNWBrwsRNjyysqEoBgA_MW2cVbVJHIHT7odRctOkxMOM7pg722E0sdcTL6byZu6eCd4ghQcW-sfV8WyWBEh55xaFPkYD4TBLwRTWU5WYfdldrVtC_InTdiwj-5kUElZXuMN9hXcChnwDucYAYWbc8kYMk9CzhdtIiyUzlEB5RW-Kx8IVfNff-Eegy20aVpDc4T2gRmPDSSuGPkLBiCkZr6r0q75C2nKmBheZYg02LrGsYD3VKzxeoC0RmBYNzGOhL718LBp6sHdusZ2cXx41NlKYY8ctUXu4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28819" target="_blank">📅 22:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io5uacqjWqQkmEPYyy44upzhB_f-9bloLaC3z8SAD37TiQM0TYoPGOKpciA_KxXm87nZIm7lO9o_hk75DJVmQvQqJrAG6RSGZyepmb2OGXq_rUJfeNi27YqrCGZaPuLk_XbifNp373QDPwysB1g9E1rLMYOY3wd-hdOoDCfdzogt5S_d3lorOmyofUVbtZ7kmOqDJoXIlvbl8LeE4zt-C03OBuXuwkF4eDkqHFOWLrWIGR3NYgmdnU82u2m_h2ekv3LpIfvkLykYcNFdkRL64Rs3JYsXR-0ZRdNVRIatJNgkgnPdB4dcq5TRY7IXzahLUwFVfM7kGxZZiPzt74auDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ایلیمان اندیایه وینگر راست 26 ساله سنگالی اورتون باقراردادی 5 ساله به منچسترسیتی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28818" target="_blank">📅 21:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa9U1tfgY_PeIwyevoXUoLIapfeGLwHLBWOuQ0c0dMAXRB5LcpqFX8H2TQcOIoxBj1gtDIM8Fqc3VCcJxUVdsjVqtGfeFS7rqlNpdAtqrWYjn5tCHWwsBnEk9UXymSk2EH8uC0vq41Pf7oIkJBIEXke5-0ldZb3WFlbbNtUSrrLHy7D_l0stApK5CxbSM7v1BaNSDD_nOslPhdRQ7tRNWzp3_SRrN52d1ur0CYzvVrPGcLkTOWDXtlzw6KL8SsTX-15Gwq5e7NlAIurwJfZZI9sG6vsGHKgbf890EFbIvNAN_oXQKwC6xowIFBXTKNxMjGQYewFNmgbUsO5wNdP-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
|شماتیک‌ترکیب‌ بارسا برای دیدار امشب مقابل رایووایکانو؛ ساعت 23:00 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28817" target="_blank">📅 21:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQaRiiFc4VfLf0GoKSg4RQXJWk_nv66Guy9I9hCm9xDdNI5-fkXdYRdOwmWjs-DoHyZO8Cu5xPAWo4Y-0Q-mZ6zi-MSDzStN_7ug5vIEMzDT6bYLJZiDPtP0HkuABliwWDroBG4yeedRiBBq100o5Tz7k1820qdgub0pmD8HVX9cuJm8TL0IzcVpwXA8z1V3QoxcDsxfMx3Lg4X-IDn-f7XwZWAgRvn0abPb7-eyzVY_zGcaaTezozKCJs-e2rSj6C72j4EWD6GCPeKlG9J0MiFudrSZgwnGeNHstajjFhlxa9pRz33Yp8y56CXQFf2n73qGkQcsA-NShX63ZqzH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28816" target="_blank">📅 21:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28815">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
به‌مناسبت‌شهرآورد 107 استقلال
🆚
پرسپولیس نگاهی بیندازیم به دیر هنگام ترین گل‌های این تقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28815" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28814">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD3TMkeAVEI2dHcVmoK10Bp8IExouUXDpSS_aB0tDy9iBIQgMgwh21vEtKalXmOwy0mIsElSF6yzHrKZBcGs04MLnzeLld5dXOHcpcOomOfIHQsio0jn7d1cQWt8T_vDX8RRNM8tDdYZKkk1RQ-XBhDsrZU4BvgFS0QDMQYgJq9m-gzZLpRsQUVUZSKZ0K4_A9MTWpi9FCEI98oSemNK9BqzrRAemSsn_ejKP3_gtzyFdu4QNR3pO2bKC2PelGQqMehUALI3C7vTgn0X1chXei9OGQdvJpMumfqWFGMgCMMPEVx0CkeOxO8PLXgutBuJjT7DFP3QP707EOZ750GFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌اسامی داوران هفته پنجم لیگ برتر؛ موعود بنیادی فرد رسما داور شهرآورد 107 پایتخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28814" target="_blank">📅 20:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28813">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIVZ44xKGIFXsRO1ChLVrCS58ZvldZlUWD0-l6qiqMhGMq3WQB-D1q82cwshbeZB7qCCG4sCVTGa4GL5PrZUMdYkL8HnBix5fcM4pm5T8k49UW8x15WZTzqSlJV04VD3JKJHdiS6S9S0pdLlK_uUcytGm8BCkMeWJimx9bLdHOybPQ76MEOh6zZoXF5qPlx2GuQ2I6BCDVPNncED7yYG9kDi3uDCwsivmjFcLjnHfeNLBz9o4wfpD8jgfTQhyVp96-0_MS3dqeniQWuFRI48omf2dfoIcsgd542cGXBiOsQPmQ_1gskJQfU5ntZPfR2Hl0yC8ubnJPij1GfZ_t88XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
جای‌داوروسط و داوراتاق VAR شهرآورد پایتخت عوض شد؛ موعود بنیای‌فر بعنوان داور وسط دیدار روز چهار شنبه استقلال
🆚
پرسپولیس انتخاب شده و سازمان لیگ فردا این خبر رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28813" target="_blank">📅 20:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28812">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzLkUmujffMcQ9QEYeo0EOUA9XlRfY6kq8M5A-yk4b75XdwwyEqkWJUfK1HItV0A5NLCEwsWPcesb3r62cdJYLD1zaaWTuSfl4-P4We2uI2u9EIMsBgcTK4hQyw4cEzJppVKuBs1Q6gChNg6oTzSOZJT-98bjjf8TTZAcWHvA2PGKeZ_l18982I6lidSHv9dsazjVXT45ulhFIGhSscnvuAqlicHxfc7XjDZ-2fpmyRKNBnBnWifrt0pT7NBKNtn2sL1UzjlIhC0SLHV74Xeoxx7L54CFbSFYhICN4qXUXF7OV6a1hZ-63eUNpHnylyoTiPXwVG1_9Gf1364o351Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیوآدان دروازه‌بان‌فصل‌قبل استقلال رسما اعلام کرد که بخاطرشرایط‌جنگی به ایران باز نخواهد گشت و مطالبات فصل گذشته اش رو نیز بخشیده و هیچ شکایتی از آبی پوشان به فیفا نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28812" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28811">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUD12vqwXAYAC-3JIHMQC2RWvxUrqy62yyGi2ZhTyp7LRnhtJjNvuHgwpkG4MKtTDuWkASR0HQBN9pgcWiZ_8Rs8L_hkcyivl8ZjflU8gw-KEADqSNk61_36RGqIVZohj_4EGLhCZ9Zn82Cp9-QgrR2MaQun7UhbiOTLASEJj9Zg-TiKaGRn4O0g25mCMR-oHiyOWxfo4M1YA8qbMINXhRwON4TgvLTydzhJ7Uh6kocCLDZ3BQcK4yNkIZ-U0sXJshzE1qa8QXhgRWVUmsHUXregtHTT5Zvt3iNTCN2wexGeQvy4xsUsn9VKtFYjGhKKpq0qoO0Y7obeC7-Ez6qmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: اتفاقات‌مثبتی برای اهدای جام قهرمانی فصل گذشته لیگ برتر به باشگاه استقلال رخ داده و به زودی اخبار رسمی دراین باره منتشر خواهدشد. در تلاش هستیم که‌زودتر آنتونیو آدان و نازون رو به تیم اضافه کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28811" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28810">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOmYQLjhilLCFm6eghSEkm-I_970Ah4LNnMs_Hsn39bbQcQyHhwrU7wcxglVJ9mxUcAiyiiljL_lqmZ4DtHvBicvqZ8SxnIRmo22xNuAt2zPRT-VzebVo25P_fbbiZm30qvQBVqG1W_wIX31LM4tOOilDbdRy22S24j8EI49wlweNrjvlV5YGTZKuU92JvaVDtIz1oW6YCQ84ggMhj-PH65ALRvhWwAEVkbeBnLhM19Vjnqu7rkKIc6bl1Y9uyP7EplCicB9hSHdnNlihm_I-CIUhatuxJxqFHe8tW9Jg9M8-V7-UfjgaVNurKihRtnThLu4DpN8bsEFAVvuaP2nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی چهارساله به منچسترسیتی پیوست. فابریزیو رومانو بزودی هیر وی گو رو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28810" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28808">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2y7fIEhej2K_7sgFjI9VHbxocxtSGL7Vc_LAgs0KbFu_pOFihwxf08g5-2EHYbGXr6UB_qTAxggD72w93VWrwVnla5fr9EeDfuauqy0glMuHKWrQH-Ba8FeYg_IQ_CqObcaZ-r0M6nsxzCucRD4HQx0Um8ZJxi0Ltb18fYhhyH4qjGsDPEu7JD6suFrDRv5Byy1dfEY2SFNHipEJPfQUelpuSQfjgAg6l-RDndS-fl1FKLgWAxda244qEsFmBCWnQSoHwMoMZk5_df0ce3xzZTrszGx2LuMQVr7EMqT4e2eyqanDV3SavXwoqqvz9VLt-9h6tPVkxu_M5-SAtlTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28808" target="_blank">📅 19:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28807">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=SDAG0cegFOI_jEC2FuNE08Gir4XU94le7-kvUzvL4YCB-2JKfn7XK2PDwOyp4YB3ANGnDh1GF07ZkXhhsj41UGzoffwSqULNbuk88peqAkN6kluk-7pl03PcdmCvjpG_QEswiPZpY670Tu5zSwthlzPbQYc2wMZUGH7pXxHAaXHa6zF6JPVoHxh0fyK411yMJZ-OEMYsaGl9eB29dGfozKhVazCMe1SrkyRIMCdjAQiVVyHbU8fHGUtLMefDEFCTEgUk3iLZBFJX9lDQ5jX3A4jZQ1hONwNVTH7Xe2fgyRitWmR0eWBPjAaPkq3dU-_wk_1l_CevBuND1A_qX3eRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cae4f4c53.mp4?token=SDAG0cegFOI_jEC2FuNE08Gir4XU94le7-kvUzvL4YCB-2JKfn7XK2PDwOyp4YB3ANGnDh1GF07ZkXhhsj41UGzoffwSqULNbuk88peqAkN6kluk-7pl03PcdmCvjpG_QEswiPZpY670Tu5zSwthlzPbQYc2wMZUGH7pXxHAaXHa6zF6JPVoHxh0fyK411yMJZ-OEMYsaGl9eB29dGfozKhVazCMe1SrkyRIMCdjAQiVVyHbU8fHGUtLMefDEFCTEgUk3iLZBFJX9lDQ5jX3A4jZQ1hONwNVTH7Xe2fgyRitWmR0eWBPjAaPkq3dU-_wk_1l_CevBuND1A_qX3eRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28807" target="_blank">📅 19:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28805">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRikZX29O52KrGXOMDI_7Cmel6aMS1A1gVuYn3VOGT0Ps5NHbmvbDDAdT7RDnd2uMO6g8y4Yj53kTuKoyBn237vzsDiPTrUQY3joHYsc2WzrLllNnZGhL7rYimS_B9pz8qpoMmAoKFXzHqpFHbyV0QQuyz4DOXLw100Ux-r9NO-mkqLhA1gadgtoI1iTe8HRWT5Bbtlv_Cw9Dht5ZhYIp79iMfyCkFoelF5cKsZ72CHFtxoCArgY-VR3YD-66zmjfWCRY1ky3fCtS9mZLD_dqxE4Gvgf12Rzz_l-HugG78tO4_zQ-UhJYroNoPb-Zg_DbJbMW1ULi-rbzuFob3987g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXaXGPJsp1ss_o2bEK00QjQT9V8cQl6ErUECpY1hlNTfkubauAwiiTH4f1eBmtc9Y60rIndjfjsmD5g6ScLi-vj13o1D3W8hfQfFcMHNdFZrQHHc0YzldGPEDXk4ehxfpExWAISfr_oU6enz3UCcmGVCLPIuHPbUTnV9Ew2NdqV0DbSYYi7QkwCj_AvYpHVhQTHK8-dmrTi69mzsHNqUeiScJNBPCO0mNgbmQpaoaF0pvsZxnaCZ4GiNbJcEEI6Rsm9h-n6RdyGVO0VmCq5yUZWb24G2HdCZYsvxm_PfTialSFjABV-TNA5ViGHwlRjNy5GOR2otuWb-2D0aRZgI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🤩
لیونل‌مسی‌فوق‌ستاره تیم‌ملی آرژانتین با انتشار پستی رسما از بازی‌های ملی خدافظی کرد و اعلام کرد که دیگر برای تیم ملی آرزانتین بازی نخواهد کرد. خبر شوکه‌ کننده‌ای بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28805" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28804">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDo37TsF3na8FJO7nhUJewwTake_ieB_JnSQADBwZ0z7su3PpyMpImclV5NU7IXH3oODxPb_wCa6W6CcKUn_QU2d8FTeUZSJk2nDzswjx9zMW6zlJtf_FwMrSTW5WOHV7oqAR8hDZT_3ug_mqieWdAO1WfpAfxn1B0zomI2UrM_lSu9VmhoBn4DxWESs6aYqswA8JTy3UZO0boxBYzOkfB4Q6UnsBapjzlGFlJuHWTEJ1ssCHljgyiQBezjNP_HQmd4ckIbQfLHJBmSvw5gU_f7j9kRAXZaHq2whwluXfCdfVIbtieYQBrTNmo__P-p1UfFWhNRvYRGtHJYhFVguSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف شایعاتی که امروز مطرح شد؛ همانطور که دو روزپیش‌گفتیم‌تمام‌مصدومان دو تیم استقلال و پرسپولیس یعنی‌مهران‌احمدی، رستم‌آشورماتف، جلال الدین ماشاریپوف و سیدابوالفضل جلالی درلیست دو تیم برای دربی قرار خواهند گرفت و مشکلی برای این مسابقه نخواهد داشت. حالا…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28804" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28803">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1X8AcvqVbyD6jbv0hSOPhkIfjeL_QO_595h2ad7xNgMANx6iMN_dz-yOzlp_b_HMRWlxNKOrb0fppOaKVDO8c50bnzdI8145u4MnBgEbTtWJy4vRv-fc2yzekrezUM964pZ3MyWiu_tkk-aJU9wIpG0hZRzQAR5KRxWd6jwhkDeKH659qRHDe_eoPnktpG9m1Zt3UNPdF8GQSeFCjyR3fg7edCYsntY3ERrdXX9T-57aztGVtUE3g9bqX2xainQcz_xb4BVXcLNx-icq-3oWVqTe0xiJliEM7JZIlNRC5mt_YX7cEDBMYkm81ky5zGyrCKWWiHGm0FKYGF1ohqKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
عملکرد فوق العاده لیونل مسی 39 ساله با پیراهن اینترمیامی: 98 گل‌زده درتنها 111 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28803" target="_blank">📅 17:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28802">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttt-kXTkt2UYebhreqvgPaYKwLvcHilV9dHDlI6JyIRCaazq-OTrPQcwbc0FEXCJQGSe3NEvpLSOd0FZdKQQb1jtpFn4flzb4wofDOiTF3TqhKcSl_TGsx-h-1o-Ru07AKxMzEB_JHBtfk-wXxOLIF1JLckQFKeLE9sRiEx4MZ6Q4mAsIToPaXsz3R9q3Ikxq7E3V4ApxApfn-mcBbzKifqkX3prFAFPvvwc2Jce2PM6TPTNETafEi6MsItLbW5Crgmc4k0CxT3_tkVYOy_EjYg0gayBwuofEBTkCFborXFB2E60dzj9xhmsIZl6IQKKoI3XG4ozp-rlh4WHN64lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تکمیلی؛ سانتی‌آئونا: کریم بنزما ستاره 38 ساله فرانسوی‌قراردادش رو باباشگاه الهلال عربستان فسخ کرد و رسما از جمع آبی‌های عربستان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28802" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28801">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9eu_vpzs7X7JhPAbpuyC-5j0tMMx_iTTOehD7ZWPVqXbEeAqTFtxaEMP5lMkZpY6Br11Cgn2-bV_8GhGFGZYHuRXNsyhURmHMFV4EyCYp9w6UfghPwCnFtw_YXbQfgL0CIkq3dP3WUFI_hCq-wVRT6md4i5SO_g3gebTw2mnPO81BE9dEwQCZuovUjOOFiEJ_sa6e2yd2YnaibxoQ0-o5aK4nzWhsRfnAMX6BcLXeur7VV8IKD5pBwnUZMpfIDIoX-DZOmjcOIL-NIjxOUAwqRzOUEeB0LHVc8F21oMoAfZYaMctqpk_o7DzwOkFTY7vXMA0neB5xxIUo1iw7I4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28801" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28800">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fq4cTATEJXAvX-uw_d1NuuIa1iR5v3iJgzPFKdm27_ZRiURMRe_KYPCnx1rNTJjeJNISoHC33WrZHOnanwiPpZOPgIJjUJWWpGuibQuK2E8ZKR5qNAwfb0eXiLGiGWWZu14C7Bgrl8AQxEa7hfjx8mf3YbetJ6mArzMPJo3MDpPxS2SFyuJC6ZyA2GhrNQaoPhWtTGukfZuNo8T-ho5OB7s9hBMVK-NytP2PR8VPReXMGjd5TcZHe02TOyupuzgOW3ZsZQyZrPLSLTZabw1mQoYBrA5lS9Atphctf9BrJAGB4MK1-zcfLRLIkQa7U4xtx2x_GDbXe43RW1WRs3A6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی رسمی باشگاه لیورپول از بردلی بارکولا ستاره فرانسوی جدید لک لک‌ها. لیورپول برای این انتقال 106+ 17 میلیون پوند هزینه کرده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28800" target="_blank">📅 16:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=PaFUZxAiJeoJs9bcds_UqCZdazrQCOwTxWI1sTIquEobFVC_7vtP1r6bcLfwEAci7FndzNBXO0S28Wj-K3rxaMcQFm0DD2XWJwzJFR9ju5P8LdgVMsxLn-z8stV1N94ICfFTUgsqHMKFCDaavWZKQHnVu_9o7iHhm94cw0QPoa-kkzz2VdJYJat7FabGgVFyUeXeyJXxnBtG5YVWzXupTRE4UQnMHiXjtcYvEwiQQANKXqEioCeYpC-x_ZkiY0dI7zntybwF4CY5grUozCCmIba9zyrTb8X5S8gUyDjD7f2z8jNfcBjqx7gRxyuWNt0HZPFNmfoXwtgb5AKhtcVctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=PaFUZxAiJeoJs9bcds_UqCZdazrQCOwTxWI1sTIquEobFVC_7vtP1r6bcLfwEAci7FndzNBXO0S28Wj-K3rxaMcQFm0DD2XWJwzJFR9ju5P8LdgVMsxLn-z8stV1N94ICfFTUgsqHMKFCDaavWZKQHnVu_9o7iHhm94cw0QPoa-kkzz2VdJYJat7FabGgVFyUeXeyJXxnBtG5YVWzXupTRE4UQnMHiXjtcYvEwiQQANKXqEioCeYpC-x_ZkiY0dI7zntybwF4CY5grUozCCmIba9zyrTb8X5S8gUyDjD7f2z8jNfcBjqx7gRxyuWNt0HZPFNmfoXwtgb5AKhtcVctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌جالب‌از استادیومی‌که.دولت تاجیکستان در عرض دو سال ساخته. اینجا هم ماشالله با وجود حدود سه سال هنوز ورزشگاه ازادی بازسازی نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28799" target="_blank">📅 16:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVUJU6bbNY-nrwTt3jytm6cTx8DagqX1e5O41HBAO5ofQ9HBeJ4FsuFPVCKb055cj1dlCMjBJx580F8v9j_uPkF_YxiSHrwg0rdsmVnqflNiBSre7Usr7mzOKpZTTbl_8Uq6mXC4uzln7jszfPBx28tXmWH_vA_y39Aa_ETCiuwM2crGnn_0S31iJMRTNwoW9gjCTKz2hqCvOnyWLpJD-ccLxDNaz4RK_AKtE6xTR8QCAlraGrnPtwiOGfCBFknBZxLdTrP1KYNahM4xQDuYzhAbMEG0nemZG3Gq_ErnNSQRn582mP2Qj-IMFspY3kM1q0IexVTsyaIzvLV0tSAESQoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb0b6b1c.mp4?token=rG-AgfKgteHKNnLGdxUNO681F21BJoA2u1V6Ad3K6uaTCySNLxbjVH_DY68x0t9u3hl_ioXYNdQPtMYFpQWutbqVP3t68g2dEw779xvfeccWuuosJlGX4xkhhAcH-WUs_rwtRWQPRqKUNSqNSkZwhDfxUYDDUNAIWlw1c9qHOSM5d6esKS5kExGK8rCxprSeDYLJLLaz934CUZtJaGQqDiATDDg-RfmX172UimfRVZJ-36fxY5_uTcYJ1-uqYgooTWHsUqhabn-2m9clwP0NZo8NzICLM2EM0mN7qnUSl9b9H8IYYElbOKB1VDklTamDYKEC1w3quQvTQuKI-q3WVUJU6bbNY-nrwTt3jytm6cTx8DagqX1e5O41HBAO5ofQ9HBeJ4FsuFPVCKb055cj1dlCMjBJx580F8v9j_uPkF_YxiSHrwg0rdsmVnqflNiBSre7Usr7mzOKpZTTbl_8Uq6mXC4uzln7jszfPBx28tXmWH_vA_y39Aa_ETCiuwM2crGnn_0S31iJMRTNwoW9gjCTKz2hqCvOnyWLpJD-ccLxDNaz4RK_AKtE6xTR8QCAlraGrnPtwiOGfCBFknBZxLdTrP1KYNahM4xQDuYzhAbMEG0nemZG3Gq_ErnNSQRn582mP2Qj-IMFspY3kM1q0IexVTsyaIzvLV0tSAESQoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه پاریسن ژرمن در این پنجره با فروش پنج‌ستاره‌خود 335 میلیون یورو درامد کسب کرده‌. البته انتقال بردلی بارکولا هنوز رسمی نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28798" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID8jc17_sImL83WOlANyFYzmXfpgKmtbyjTUeVkXtK8vW6XW3pTPVgpQQoSWpyDRV-uV_RVzzPdv3LQL05JzHgOdQgPQg_j0cj9u25yW5L_PJ6TGfxX68Ln59Z9qeiSwqI0eVgws8ggWd7RPs9H57gPrpQHYc2RTfYaregX81Xt2F_wycGc_o78OBS8Ye6etK9HY2QmXXJ8Wz7IfIC61kjram94ZbAAOB0CzgIBnwF6uUejpc8jPMo5trDYPZr2HF5Sv2RjefjmYQidEFCG_lgpmfpdehmBv7zuLzNs5yK7sZZFVB7qgwbKyhNGD6DRkptv2ryBBDW8x9k1v2IooPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
خبرنگار رسمی باشگاه‌گالاتاسرای ترکیه هستند که معتقده این تیم امسال قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28797" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28796">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A02_3ggeTbtbpSB2xXkVVLLwhb4SCvvaSkLFQYUfeYAtMEwq35LAz5wEnP7zMeuRIBTWq1Hl2doukR7v9isuhFs7WAdVv0q8a-YT5CIWaL5BRkQO7t1LR5I-ilF6uxnFEV5BfU5GQCNZEAqU568MbREE49_p5gS9wJIQpfA_YQHFLcZtSxkx3gy1BnO_8nAxAAmGAMTWUKwCwevEdgPV7Ty7uh6uGrhv2MV-xzxynVDIkQkI0tr3zIOIvl9YbKGDEDsrJ3ESbWnNdPwNNP8WuRLwC4a6c8l1_0QYE2Ub3ABfnqHmCNrFuPcW1pSkkMwZDxhdrU9CEfArh8Lr8I8HEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28796" target="_blank">📅 14:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdgBBkZb3sze9jE5we035_zEu4eRcmRSAN43WLVOTFTw0zCT_0w8OhInnKpA0GtOtixxODsVjdY7XGV3koyR1Sfj2PW1MzoQRosFbXDxzy6yCDxCcP4HCZxRxhmlCP8XMUsxgXlpsRNIgLnVxDZmpotpqCfFmDJ17pnP6LHm_6by1hLDcNWDnIndkaUbeGczc0oIEACWcrnJOfwGeEr9dWMIfJYmlWO8HlF1RH5_twWlTWFVD_N78nTR-ng94UGj-6A4BFK_hgvn0R7KM1DAk1hiySOU_uE81edDpqTjDa4lsP7T98GFtzS-gd0o_9Tb4_d2-t2SxX-sfov1jAHLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28795" target="_blank">📅 14:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔵
🔴
درفاصله 48 ساعت تاشهراورد 107 پایتخت؛ ویدیویی ببینیم از زیباترین گل‌های تاریخ این مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28794" target="_blank">📅 14:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28793">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvF_WvgHvJyTnA9N8XzQdKEQDS8f8qq7Bs-IzffnUb7Xxdh_Sre9W6peaHXwp88EAbGdjOgKV6qMEnlX7dgK7W_6bh1F2uSfqF0L_wvQLpDBF9yvxmzM4CIvgkfDLxDrZhrHRsmQdEGZVP1087l3DELpSsxBgnQJTtPF5SlnDH2HbYYTJSLH8Hoh3DIN7GI82-ownllcUtOlosgZ4vpd74fso6yBjuujGfacoILl5g8qwvbqgwurt-wfVa17khUzGMrU2Kalmak4U0tqcVk-17TOYtLFf6z37sqpx7xW1wUk-pcv_aMcICiJrnFxOR3VYS4Lwg-onVAw_8E5oSylqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های کرواسی: آفر باشگاه رییکا به محمد محبی دو ساله به ارزش 1.6 میلیون دلار بوده. یعنی سالی 800 هزار دلار بود. پیشنهاد استقلال به محبی برای پیوستن‌درنیم‌فصل سالانه 1.2 میلیون‌دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28793" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28792">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJxELSonNbCtXRtpJ33DDikp1ElyO8qOd_ojzVsOrRYLVzs-pEKoJOtZLk5_06Q9OxH2HCbOsz4ogwq2pRXdr3F4B024NrX-rfThNmWDcp7kZjMWXfgnBabQGXIYDPBb7az-LeeqhYTIF2PjayNS44G3oXvfPunuBmjUqhX7GoASUJjTswIFEJ8Dqe2MixpXpVO_tDLpTwc4xIWhV5ST_sTHdI4oRpYGegkgOX1jTJXFQb1PBzBKoF-pbxk5Q64DfSGfvpDdr8n0oUHKSo9ww6VZGCtL_dvhz-1UDuPBB7GxdJe1rUuZ1z8tpgY-MZPSLP-iR5Krnk4p8qM9DNYz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28792" target="_blank">📅 13:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b425286.mp4?token=AxqdPMmSQz8wj2lJiK0Xnbr46wh8D5yqiU7gA9nvOX1pCg4Jh75pHxuQKyjs6yQaxkXtzZg1eQwKUcP5wwqX9kGmS4wDH-KZmga2NBZkudoUXbZAzs-ieqHfVVAOyMFypgSZLTNgMPoKgd9HNao7slNc09-l1y6EjNnn92umR5vp3dQ_rWyjZxezuwDEWE6ciUCPqtmYvv7w_IghO6UK4MANYYjhVr5uueA7hmw8XvrwTsIXf1pzNoJkBV7b9kieX6ozjXv4Zu8Bhw1J1fs83bpAiioi93on73Q15YyQRExtwtLh672MiSGZUedBOGTFQHRT6dIXxB_CdrzC2wYfbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b425286.mp4?token=AxqdPMmSQz8wj2lJiK0Xnbr46wh8D5yqiU7gA9nvOX1pCg4Jh75pHxuQKyjs6yQaxkXtzZg1eQwKUcP5wwqX9kGmS4wDH-KZmga2NBZkudoUXbZAzs-ieqHfVVAOyMFypgSZLTNgMPoKgd9HNao7slNc09-l1y6EjNnn92umR5vp3dQ_rWyjZxezuwDEWE6ciUCPqtmYvv7w_IghO6UK4MANYYjhVr5uueA7hmw8XvrwTsIXf1pzNoJkBV7b9kieX6ozjXv4Zu8Bhw1J1fs83bpAiioi93on73Q15YyQRExtwtLh672MiSGZUedBOGTFQHRT6dIXxB_CdrzC2wYfbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
بااعلام فلورین‌پلتنبرگ: میکل بازا پسر خاله شانزده ساله یوناتان تاه مدافع آلمانی بایرن مونیخ با عقد قراردادی تا سال 2029 به بارسلونا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28791" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfQ1dsdAi4hCA_ddN1ki4oOgB3d3_d29KGgr2LVYK1A3Ms8utcE2_VqZfn3sfSNXCsb4igxfUwu9YkbQV4uqtBA0WULCcdcI5FjkWhFAdmdLcdbl7GiwTygNmZkRB4voSXHcLXDNiSmPiyTF1zLXtkiLiA4rEI8z2BBz3IqJ9vwNCf00JFKpzrCaB3-B1doIncJbJ5RT-UalltHhFME3eog3zRhlwFbyS8YzvGGz2Yx_NoxStVoBIFwyYoHRR3lcM5Nc9oAR7sTniHIAhnfkan71n3KdFL8K4ZJ0oQ1KV_Z3HvjJtLwbuCdJ-oI9k0f0CKH2Qa4ayBu9mVx8dGlgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت فوتبال تیکت اعلام کرد که بلیت فروشی دربی از این‌سایت انجام نمیشود: بلیت فروشی رو از طریق باشگاه استقلال و سازمان لیگ پیگیری کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28790" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28789">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCxqhglmuzpFHYKrwAOhus1VVGqrzrNG7LY9hPUmPxfK0uvfFlWgNzdkirmvwmi0OMlSt8Y3j_DOaCHkhUlNn32UtWTzHD-8RYDpY_0q4Ffz9tMz2iICA7ofoEcB1WlKuPnLNf2Ea71pgi3ezYsftQ6bTqKYMpbzktH_CjMsIw03dZPuEqyVkSIY0H585Xi59YcbCR35RXhU4a8Tq35qnOjresplPS_4RfpGIw2TOUOqCbN-X4CJ01XpeS3kuxQzAHdgJO5hbDdA-xjr2giXnwQTZvPv7HIstf8-t4ikWMILj3A38sUxZgXHFPEzHyNfJotmudaZatH7L3KFuq6SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفت خرید بارسلونا دراین پنجره که بابت جذب شون مبالغی بعنوان رضایت نامه پرداخت کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28789" target="_blank">📅 12:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28788">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkcBCEtujw1nAY3mjMw3G0uOFJvVIGmcof4H6h49LFBXByFhFN4OzcvYx4OSviFyt3lN4lvjFbmE4qZ_gVM9xcnrBB_D4ifpJyV1G4Nts1TvH4zXTNyKCYAyEICMT841NOL88KQjh3O6yoRJHC0xkBAXTnmhn4JIM2B2JSebhEjDaGN-_xP5NewHhDX49kpwa8L4FxXC1T6ukq5pIJsYmeg8TQnP8QJXpCql2Hjh4araIzzqPkMA2i2c6T0TCQIBAy0OylOh7LaZwXQOvqqgOj6sbBFy_7TNsJH8131IHjFrQ-zSPDL3erICICoD9rzCuhyBvWp8bZBXpVuY6Nivsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28788" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2A-WaG6NHit1Upgjv67gxNl_RP252ma749S_PlawpNzavbd9sON5QXRMINGTuD53JAJEe9CR9plWViT3veRgFw_ZrXwVvAWnLCSCzBJY3nPXlk2suAkn-A1lqG6oEIBjrJaZwQjQxqmywo8-dI5FcvGtQ0tsEddurHw5s8jrPiqdI4LT1xixJk6DVmlzx8H7a91lxIoE1rrwSIoiZe_zWVdDmLAHgLDoWQUXQeUi0DbLMlmd9AE19PUZ2uX69S5_7ktL09RjyIXxV45nz6696vfiQ8jfQNQo4oyOCPfiu0sagw8OMqLviDx27l9CR4zLpQ2lCXygjQ4_y6E2YZypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
🔵
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ درصورتیکه‌هلدینگ‌خلیج‌فارس‌تاپایان این هفته 400 هزاردلارپیش‌پرداختی به عزیز گانیف ستاره تیم ملی ازبکستان پرداخت کنه این بازیکن قید حضور در تیم تراکتور تبریز رو خواهد زد و آبی پوش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28787" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8i6-xNIMnDNtwGVjk0RjWb29BRsQPIQxd8g4-kbX4arUjdG6GZ-oiY4QWiEwgT6dqjC9gIV4Rz8KDFjMENCNXWz_cXKLwHq5PJIO3fsyJo0druhy6-m-Z3Qr9lRRoxXiOs9cWIyR0na9P_SA5rsr_eGSmIJUVRAyo-TwD_ZhZkDYLtWqikbYFhx2NLZDj2ODcTheVVuHVAejfMn134Yg757NMy6mo1NJoTCW_v3JNxOMT3TFbrxRqnBvQERWhG6dNKlv5AB5qtj_3fsY6HrCZTuvwM_eIV2KB0naWWNfpkoIMGMLRSS9DZN4roZhfsX9ryyaXyKAxzBrLIKqyo6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب جدید بارسا درفصل‌جدید بعد از پیوستن گابریل ژسوس ستاره سابق آرسنالی‌ها به این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28786" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADwAHSfUkzeXvRmzdErMP8LeIFVa-rOauSpOK5NrJavWGiGvp8QSy9H-LDxvUdDOL7heDB4D9YBmiHHR08SuiwVT_A_lYgcO1tlvLbylEvTsgPQBsqY6iS1-nPYSLmoIDOYeO2ae1VOPijzcA_Dtgkk0AaHVRGxn9NSOmi2q498nfhrXghP2iqAZ3irVkTvKzyD2LJUzX5B_UAZnTtfrN6-N8CvTiNJmp7FNeZWP9mepRS5fzuCaRiTdkNeVx06k86OpeaqiN1xMPttbEJJTYEXqscMesv3RAL50lsoegBlas1ORZCXbKEY3ApcVfiNfrKQHsoqpxtqfBwQB3Yr2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28785" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3pBleeIl44mqMSH9s3fvr1suVFun_JoKWuM3tUh652QVk8faoej72XMSL2ulxEwRoITJQhDEtPMCYupAW9l2QP9URV3uDoNKgGsk3MCdwd6vf8KojmJxmea_YZb1s4kmMbPDzcWGgLwQTrL_ueh_5Ku-woNXZbm2qmeobPzJiw2BZqGIzuqUAOkJT0js_d2MxIo7VJCeecBRoPUT8cnuqI3iLEktparJE37sWEzCYj1EmRWCq3KibbSydny06HcvaCYZouS3Hl0AEl46B0F7mTN9c1XBA5KTJCtG1rNEDKoVyrGxyOJjjiQoyf7sJu2DxCYdlEVCghV33MduZ-rsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28783" target="_blank">📅 11:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=HcBmtbxGOKIC846WdFadkIUqj7XckltJ-WQ94PwLNNLGnJuPbr4FIfZea09HnTR4BPb5sUqR7abb1pnX_9w3T1pU9GksVSJ0Ywp6F1jVNiBGlrgDfWacMrKUNE--ZOhOH7curotmgFYeJRHoKFT0ql_R4ej9rqoYGK_2ZpRTUFVDQEllVIoc4cwbi3ilfvxEOL7QeZ0x__Fm0tP6VLMcTddlzfSR-Z_qD5bXc9HAI6ty_KqE3luKAZ2vrWl3tnkN_xXwk_uit8Yt2wMb-OJsh3ox7F1NLMotLULexWkJLL9g6um2vLqs29_2wox3GWYT1OHIgk47hqaewz83YyEFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf70d43b37.mp4?token=HcBmtbxGOKIC846WdFadkIUqj7XckltJ-WQ94PwLNNLGnJuPbr4FIfZea09HnTR4BPb5sUqR7abb1pnX_9w3T1pU9GksVSJ0Ywp6F1jVNiBGlrgDfWacMrKUNE--ZOhOH7curotmgFYeJRHoKFT0ql_R4ej9rqoYGK_2ZpRTUFVDQEllVIoc4cwbi3ilfvxEOL7QeZ0x__Fm0tP6VLMcTddlzfSR-Z_qD5bXc9HAI6ty_KqE3luKAZ2vrWl3tnkN_xXwk_uit8Yt2wMb-OJsh3ox7F1NLMotLULexWkJLL9g6um2vLqs29_2wox3GWYT1OHIgk47hqaewz83YyEFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌جالب‌از سبک بازی خارج مستطیل سبز کول پالمر ستاره انگلیسی 23 ساله چلسی انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28782" target="_blank">📅 10:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇿
🇺🇿
هایلایتی‌کامل‌از عملکرد درخشان عزیز گانیف ستاره‌ازبکستانی مدنظر دوباشگاه تراکتور و استقلال؛ همانطور که شب‌گذشته‌گفتیم درصورتیکه آبی ها این هفته‌پیش پرداختی رو به او بدهند آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28781" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28779" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdrqP1gh_dA3CouGYtM9-ERlMTU0O_BglSHx6TsSfx2rJNjZScjEeNZIw2slBTmRbReskYIsapR3M9G7EmnsoD7QWKF9fVuZTWAtQtxh7IcQRvfD7tKwKwgZ0ON5S2-EcU_o3DWGNxv09jdZIng9Z80S5H5LLFqL37yh8rqAnO--ngNu-eOuFSHL0hZBBvTRad-gU7PFmjT5x0tU3XkDe-xvQQLKd9nBedX1JiNOsXFPVcuXg1pwH9TdA7ASiz450lXpotoj_VdLnTXcw-WODkv_UL1U3ah0hYL6lVu-tqY45Wcb_sJXZDVQFu-UUVNAoRJTpc8RiAQq28XEmpu6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28778" target="_blank">📅 09:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=IUmaz2CUU_SKGI6_lMeOdVFiBPY6j5y2F8tRBz3NdrcMzRuMstvllaVZeyr4FSl3r-M_c7oxFq5_U0kZhTLoUkDxZ0B72M_uetFN3gZK3HFmlP0-zNaY_5AnqLUfIUrbxt78gPe2N5u-8grqWHEPQNKgTsFJgwz8RhA5oEP3sYZSj1RGN8DZCdJmMPfysXMb6SrSIvs0J--oVcALE2NYh0BdwoAY34QY8WxsQMJmFB4yYwzxCF1nUYv1JYjACZvsWNOLkA81FkaXZk6qJC-ueJkV1C9wz3KhTvPyCliyNZqgQC6IKoXN8LAOnI9vCeeDY9ShZv-9Lr7f6h3u_i39uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edcdd5b47.mp4?token=IUmaz2CUU_SKGI6_lMeOdVFiBPY6j5y2F8tRBz3NdrcMzRuMstvllaVZeyr4FSl3r-M_c7oxFq5_U0kZhTLoUkDxZ0B72M_uetFN3gZK3HFmlP0-zNaY_5AnqLUfIUrbxt78gPe2N5u-8grqWHEPQNKgTsFJgwz8RhA5oEP3sYZSj1RGN8DZCdJmMPfysXMb6SrSIvs0J--oVcALE2NYh0BdwoAY34QY8WxsQMJmFB4yYwzxCF1nUYv1JYjACZvsWNOLkA81FkaXZk6qJC-ueJkV1C9wz3KhTvPyCliyNZqgQC6IKoXN8LAOnI9vCeeDY9ShZv-9Lr7f6h3u_i39uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت گل کیلیان امیاپه به مالاگا در بازی روز گذشته به گل دیدنی CR7 به یووه در سال 2017
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28777" target="_blank">📅 08:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=gmLHJlR018B3upeNN62X0s_0JVUFvVGCXW_1zXHMej1Nl6LWCd79JsrgLyCtcEASKuMwrYH_KxtSn-Y1kvZJpJTkVxiQsPP2Om4XmEuppsdMrcWoyBrxsXuD8a3ayllFWbIowexZzpulGij2YR_xsJP85nnFK9rwxzhcNesavwqKdYv-3gKRp4w_wWmeJVskDctllnN3z-lzNWEcemi-GKOF_tBAv-772Ub1vasv0HT2P3F0chDtfxoItNJRu8Y7xfU8xsUiLTNATELJjCcXdzHRs7AmoGr_FVgAWCAWvKGbfmvEtiMCiJXKie5qnAkEmNGCqW6vdBV6IHoOwSk2_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785816e6f.mp4?token=gmLHJlR018B3upeNN62X0s_0JVUFvVGCXW_1zXHMej1Nl6LWCd79JsrgLyCtcEASKuMwrYH_KxtSn-Y1kvZJpJTkVxiQsPP2Om4XmEuppsdMrcWoyBrxsXuD8a3ayllFWbIowexZzpulGij2YR_xsJP85nnFK9rwxzhcNesavwqKdYv-3gKRp4w_wWmeJVskDctllnN3z-lzNWEcemi-GKOF_tBAv-772Ub1vasv0HT2P3F0chDtfxoItNJRu8Y7xfU8xsUiLTNATELJjCcXdzHRs7AmoGr_FVgAWCAWvKGbfmvEtiMCiJXKie5qnAkEmNGCqW6vdBV6IHoOwSk2_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌بسیارزیباوارزشمند ازهیجان و استرس مادر برای پسرش حین کشتی گرفتن او در جشنواره کشتی امید سازان المپیک 2032. عالی بود واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/28776" target="_blank">📅 01:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28774">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejVqHSdSizD_zLJSXySTPI6thazlTNiw_DPhEZibIzFWPL57QhTc6_cikY_N73tIwWc-vy6r8tELlUerSr3qxUS6fTbZ1DMTw5BImh--P65cdQVysCMwO0tLeIvgyp8hjyObxfInulBverXVn-beMrK-Gwo_fsIdkb18bPDIrssAbBPyDvfI0JOZMtv7_JCQOrzpafNvameDwWSUvIaQR2H_x0TuHuEkgRSHjTWbsba84i2_1A-fWTfxjTUoQWX_03iVdfrqgTGt5WgSYaCdNa9MJe3B-S5qiqQgyhQ5Mfw307gvbdws76TlFOtmtElMb8p4n1ffa1dyuFOrJ6-dZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ درخصوص عزیز گانیف ستاره تیم ملی ازبکستان؛ پیشنهاد مالی باشگاه تراکتور بالاتر از پیشنهاد باشگاه استقلال است اما مدیر برنامه یاسر آسانی در حال تلاشه که گانیف 29 ساله استقلال رو انتخاب کنه و با آبی‌ها قراردادی سه ساله امضا کنه سپس بعنوان بازیکن‌قرضی‌راهی…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28774" target="_blank">📅 00:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28773">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXFI5Et1W7oVnuglIXbua-GtaHpA3UsZLCWajezunkzh3eLxZySa9izqxaMKf8e-ZdyZ4FJvzyLNJG_FjmrglwMUOOBzsiFp_vLZF-mIsTugg-5Ro_bVm22GDkPO845UcYr3UMIU4zG7l1azrhUjThSmbYaM9nnUMndDW-SM3h1lyQAv0BCjh4yJChX-4WWZJYPKLsEPTfwTd94hOLRbFRs7eFjXv1l-R18Xw9gq6KtYhIwrLiMpsgPi3aiolBA7ZMGiqg0aYt9i2Wg6seIP86uhWL168stOMoxgvNdRyBSBcU4v5i_hwhJnxgKzGBWe-Ac4NqXCdH69BLo8v3RdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛دوئل‌شاگردان آرتتا و امری در ویلاپارک و جدال کاتالان‌ها مقابل رایو وایکانو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28773" target="_blank">📅 00:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28772">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns8Hlxi9zA4yYPeTjtrw5prpUxZDGZeQE9DB5i70lIydSlgpejAnGGHD2q0DjzOo5_FUU1UMXdm41e74dETAqdyc3_X78ikDgCF9LX4tZqMokBRGLjO1Yk_ssMHiOI05aDOvibC5Ik1Iwp_Wbmeco_4YmKUtM4s1BQkYYZYtwKs8DjUYl09mE6tqaSWIHP5Nniiry5F_FrFlcPViuAxMYLLMkoHlvot81PF9p9X9jusAvZkXBUEEYUBdbBg45zvdvnjI_JSpM09E2uzz2p2EZoOgf1LaGxGAplijkHUxAzqGu0eqfQjPep32YPGG7h2wCIoUULXumoyTMgLaApGJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
از آتش‌بازی لئو مسی در MLS تا برد دلچسب یونایتدی‌ها مقابل ایپسویچ با هتریک برونو و ورژن آماده کهکشانی‌ها با ژوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28772" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28771">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfaKnD1ti-WDtfPEXKqHCYIDOKM94RQ9HJwKCz395yfZYjZGMetx1zi5XRvQWOStnTEirWVkzMyAnFHOG1E7I3HnGdmvtAqp7dsx68dt15J2QNCWDyMcknDEiWElkEC3zyoo1cWuAJA6TUlEScL2u6K6loKbmjOUHSENiLR1MEGD9mNxAx6Vyf7nC7hAh_UQpDmgTG4F9YH27yjdGYMQE5C2wM5683IlYxyw-3gGHrMEu959ifuXXansf1Vsd-P8nHG-yVfzmZz4_V6CCBuUxBBhDiuxsO8_7IqnQ6wMaEsK-m2EjN2DLNi69nsi6cBl2H12Wc3D39ITxud5adZKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28771" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3X_F2aMrbmu7S567A1a6oHRPxfGkEcL2pvaAB_IPEXYsb4Wb6CiZ7dYxa-a8m22j99lutW_ITLt---BMr249NAe5bWG8hFLHIObslI6-aVF2dJV3VW07ndO3ZtcLWd0OvyG9FRiDrnuJnYOt9ho_hN0noZDa9fBr-ZVYYJrMrRHkdCzRg4GcdmF_NRKCfYJFULmmZu_tlJq6ixozir9NEP9dlwhjm99Wu--xWz7wscLbasdLfvAhtUE_KPAnB96M3N6WnroySgfaLUNoLUQHXlqj418YaXlU-CZNkkyJj89wPfNaJWniS6W--OYev_WWUR9FAcRiV8hgFukpTyHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔵
سوپرگل‌استثنایی و برگ‌ریزون هاکان چالهان اوغلو در بازی امشب اینترمیلان در هفته اول سری‌‌آ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28769" target="_blank">📅 00:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bz0SUnMm2QC8mjKMuGhz53SVFNfZRROb6GBipRrqE4s-o0XiZDj9CvP_5Lq-pP1oYMkAbwE4HB37yL7AclA2d42QedHBvlq_MDOw-fyQzJ9VE_xAllHzgajoAhJnSLcdgbgEU5SAqpnI1N-OUgDUHge2kqVUJnAtsQxOyfbl_NTD44z0DCOEvJSkwr2dZLntp7_Rru_GZOmcebsQcy-rYA44qkikVbt-8rK0qp7YQ-JTNpVGvJYMOm9xfeXMEm5rR-P3GEFoTPdhMIoxKtSsmGVozZSkSdkmLpGXf5e3zFw96YnmFAqo_RbL16Sg8VF_qCnbrTIEU-jidPqKj0hHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مصدومیت‌جدید مهدی ترابی ستاره 32 ساله تراکتور مشکوک به پارگی رباط صلیبیه و به احتمال زیاد ترابی 8 الی 10 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28768" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28767">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx8v0eKK-k-sXmlDjWXrB_tdnqzSTB_Du1Y_mR8O5oO1ca3ZO7id4IJe7k135JARtjGLDWezXqJme2lcP2yZ9WUB2fqncHEk-w59-ig3j3WBDWmDJZHTjg-Sy6C2-ac73Jk_mifKltHkTRdC6nvimkONEmlCvmhaTmJevzIjSx6MRm6z8hcQMwbw3xA2jq_sM61lLAh-yvmCY3x7b7JJwM6NYxI7yKQGppItI5LrJ8AfD8Hx3CRzPeOL-CP31OOqJffrbnHVk9QnaDnsoslgrTAY8uBkRTdUlWF1ufqMN1IEiTRtRZ__m0MT35ehqTjhDcaaAaGtEgx3-7OxEB6Orw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هلدینگ‌خلیج‌فارس و بانک شهر پاداش ویژه و میلیارد برای بازیکنان دو تیم درصورت پیروزی در شهراورد حساس و حیاتی پیش‌رو تعیین کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28767" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28766">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyZyfVJfSHiUmbEfgfGJoYNi-BRVKhn4Nu5Nma3HNPw-MR78MjTGR5Y-vE2ryN2Ad2NFngRU6Yt7JrIWJdnXVM1PCFtsjxj7QzDpClZeBZiNJghGSUpAZZJ4LL77QetLXDNdlyrzOGK-dW6r_DUC6s7HSh5kyhPOdiHEv0v-XD2k2ASKFHoig3jC4xayYQ7vsSOGWwB7Kdpdy5CKX-kHETZi57ee1Jm5WH3ZFDIcj9T-Yhqq2BixGlXlA6sfKP_nqWynNUIGcXMv4fbb9x_5V9GlmQxz5FkcmmduEYnmU6w8TGkwLlzvXwV29h7iDrbpTPB-7E6v3zaXo9dSCv5v4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
گل‌ های دیدار دیدنی و فوق العاده امشب دو تیم منچستریونایتد
🆚
ایپسویچ درهفته دوم لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28766" target="_blank">📅 23:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28765">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcMfATM4ALnnlIzZyOvGSjk35o6RgSdcpyDUodE4T8XL5FAksM7SgColdBXVp_2zS8E4Yh__x8mueE8gfERi5zp5dBETw7ie8sZoiC_HUtuNLRxffoYKwRcUJ4oZWyhlw-ycjhytGCTSoTHCcPC_m065o73sOYAGYXi3fGvt6OB-0dpz-GraMQF0sy3yBk_gHLldN2sG07YOLNAaPDf65VyCEyXirIWB1OjddYC0nQtwWTr2gBzRZbUC_HavdkMp24r-jyDoJALAHjd02oJTEJyZcZ1wYp-9r_LpoAXG0t_ofITC8DPTowQ8sMXVpp-NrrLXlgcauTP5Tffgz2nDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ امیر عابدزاده دروازه‌بان33ساله سابق تیم‌ملی به نزدیکان‌ خود در تراکتور گفته درصورتیکه جواد نکونام سرمربی پرشورها از او بخواهد حاضره درصورت‌جدایی‌علیرضا بیرانوند راهی تراکتور شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28765" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28764">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5ArjXWgglJsbGIA9WIZz693PV2v0kThKjmdLCWNOhF0KKTg2jik07nLe47ZtVXbJ5GUH_dsJN3L-EN5CChjzICyqPvQOVBm5NFRNNQHGhxoTDADCtVYlOFiReqh9T8BOrPoS_yN6fcSsTpPXupls_Qe51b-woXnA9jLz9RVnVnspZHzhEHGU-D4cVaNAhs6HC4DSew8mkQctsLsRsFPpivyozDRQuFYrOOp-_9Gn9JEmaSRMlDBWwClP7pK6Av-owLfoLNwlx2JjnxNynudq4gP0eMm1hz0mvR5mk-0qbKYqVHyXPOl8k1C0B5NzLVMgwBhQgdiE7IH5zqQeMS_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ به احتمال فراوان موعود بنیادی فر هم بعنوان داور اتاق VAR شهراورد انتخاب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28764" target="_blank">📅 23:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28763">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c007350.mp4?token=vDHwFFI8XVAS60zsL-0uB_TA9XWwO1oCVryXCde-Bho-WYjQAeNgXfrRTARNJUI7kPD4IpgKNWBhwCbq895L2KIzGBC2lbfDi-G86UR0a28FKiROqa7uIyWVXbsnH-egE90eAyPjKGQggYmPra-2NXMLe73KeyOoDUOSqhMSYKhOhgvuBxkh-dXp5sZhgnMW32STIHIdcm_PPZkTn3TXRBJd7FDM2RF6NNaMXOAYfQ9QNyc7vicYyiYmIND3P8JzgO9iD5MWzgGOyd3n7zJ9dsrbsRmotL0XhdF3D9mkyxjh0fnt1I9vCfyDHwqUAc1igick6MAwNHpCggApn5Gkqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c007350.mp4?token=vDHwFFI8XVAS60zsL-0uB_TA9XWwO1oCVryXCde-Bho-WYjQAeNgXfrRTARNJUI7kPD4IpgKNWBhwCbq895L2KIzGBC2lbfDi-G86UR0a28FKiROqa7uIyWVXbsnH-egE90eAyPjKGQggYmPra-2NXMLe73KeyOoDUOSqhMSYKhOhgvuBxkh-dXp5sZhgnMW32STIHIdcm_PPZkTn3TXRBJd7FDM2RF6NNaMXOAYfQ9QNyc7vicYyiYmIND3P8JzgO9iD5MWzgGOyd3n7zJ9dsrbsRmotL0XhdF3D9mkyxjh0fnt1I9vCfyDHwqUAc1igick6MAwNHpCggApn5Gkqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28763" target="_blank">📅 22:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28762">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fxhj1r-S0nPJIfxXoXKNguZmwQ7eKWFzBgCNdXTfOiOvelRdA6A12-joV2PMdcK3CDo3VHbxmlIjSVyYAUvZc6sG17l0jWF2OouEzM7NkJI3uVjlwwFl-PWRJjvvHRJSLEcTpNX80B2nxRp_6akmfCdM84XWoZr-A4Btdq8z2I6S4X8ZqR8TC3HnEz5x4BWEL6O3jo-NZixQPqrJlKKykBLYUzTighBBBu3U_ct7Xe_YH53bQxGS43woLu6jS216XpEhd6YY_E2G-IMgUymYPqyk28yf0D8JJy9nqP2CsMjI_yGrXtqek4XLDo-SyyisXa02MgJ3sWrEx8WjEmb_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛ کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28762" target="_blank">📅 22:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28761">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMs1gdQArZ2KeNfKFNyDv7OSn7-UpDLIZPPLnMOJZCtE572Idxfy0mVABZrxFxO0qu6ixtyNimL2UiyVUX6p_hCLMT96O0ckPbhWu50PTG1CHlauFIA7w5g533YMsCJyaLBBnvRr46XmhQV-r2TrrN2mi17oCTjRtEXhPpuILCDszKU19RGTQy2GAHVUNEntzo0wKNQfZxj7jGNSIV-AyzY0WLKk7QLwF-w4vMy0W_v6aa4ntJOplDWmGbf_hI5MjOBYuVKFBIZtio1OL9Zoup0LB3EDFgAe3FyG9jdnatjid2s-4NNeoLwYi1IlYpZruyaOLqDd9wrYzBwlluAJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28761" target="_blank">📅 22:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=TfAUzvM2SALH0TrWJLav8S10IELSk-kq9HzINJyewMnmxRyn1WA3Diat5O1tX-O1f0KKd6dmqlgW6wwTnKJwcNtqiH9akadqjeew5mkkk3Ekp9YavXlJcPRcLJhMoTswL3V0JYW5I-axTOwZsvgvGyoRIYaUIXWLiwRjiBx9imDwl6mJyo3OOiFxLJ4pYWwsJq8CThqy_hjgNu1qgx1Vb1KySJkvI1tdfsY0Kuz6XdT3hGSajPn9NR_XBMsOmi0mrCK-woMcBlKPcaMmQyAQ1SFG71ZHvuCEWgEv-wuvb4SH8jeSqQdI14vrtqaU2QspKH6y_YVH72gRRNweTXbPIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b5db2489.mp4?token=TfAUzvM2SALH0TrWJLav8S10IELSk-kq9HzINJyewMnmxRyn1WA3Diat5O1tX-O1f0KKd6dmqlgW6wwTnKJwcNtqiH9akadqjeew5mkkk3Ekp9YavXlJcPRcLJhMoTswL3V0JYW5I-axTOwZsvgvGyoRIYaUIXWLiwRjiBx9imDwl6mJyo3OOiFxLJ4pYWwsJq8CThqy_hjgNu1qgx1Vb1KySJkvI1tdfsY0Kuz6XdT3hGSajPn9NR_XBMsOmi0mrCK-woMcBlKPcaMmQyAQ1SFG71ZHvuCEWgEv-wuvb4SH8jeSqQdI14vrtqaU2QspKH6y_YVH72gRRNweTXbPIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
هواداران چلسی یه ویدیو دو دیقه از عملکرد سانچز در فصل اخیر لیگ‌جزیره ساختن فقط آهنگش رو از ثانیه ۳۰ به بعد گوش بدیم. این چه سمی بود:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28760" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28759">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXxXM3FR99tNMVzCc8OBPI6SeI59wkY8UbaEwcvYVNSpLGrU9YtvbBflKB7L5gOdypqkJSP5nVH1oWe2m6FfTM2phZ67FHrZIB5uEyZWuMmPXQef4W3bzdXvQeiRKALW4zkTNVwVNt0Zq_n5-iBMLUkT7RXeuEX6dO_oN90muibBaJoKU9HnbsULZbdVB6aiPFAUeLeveQgLVusW1Cv8IAE4fI-dkcHscL6u4plffvGSkgjwiKjVX1fnmJugzFcxVO0QJU0DRcuR_3dQbtl9YUEyPHP7Kn2w67HTcsOeAULa5BGUk8Cmojtsqyuj5Qn7sk1DcBhfAPuqckAhirlijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
گل‌های دیدار امشب دو تیم رئال مادرید - مالاگا درهفته‌سوم‌لالیگا؛درخشش فوق العاده جود بلینگهام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28759" target="_blank">📅 21:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qngEwePIzxOI_Lcm3XVmvTqcD1hQ5olUHCK53VCoa1QcWMMEi4zQJUERiHysfs0R5goCpgFeyLAVmkl93cG3E0Q7_9CtUF1y7tMsqs6TYN_lvgTqbDa7YogPrxfPmHYcfJUeS8rWl67Fka7BOG5XBC3OSldpKF0wHzfQFICOodBX_BLrQCA-88CSahqIWjPTx1MlUS1y3GfUketZuUPg1a1kkFYHe296tyMGc9XS1J25pUptih8r3KGplpAwwfN_toI-m5_lD-jmjg7ocXUYApnSzpfmnzg_rXhB3uikPYr56LeLhVo8TOgQJZaFRcKhrp8LzT3JDiSGP3qeGNOOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=dmkJZS2NPIEld1NmsbS6TP6_rUEOKmHjnSMuu3qpy_Gxe6wTe61HnfZbock70QmtpqaScPYh-wACGKjeAtpbcH9P-vEhhnrhuD7ODH1iBU_CQrkzDVyrjjq_MsM1TcHNuKX6LC_0ZMMBXURSC9hH6TH2DmhsFCGdaiDIgxMkmZWKi5OsqSdJrIYL7phMMi-YyeJ_UHk-5dqBqjl51-6OdbaG1vmG8Z3D4seNOwn4yHnU1ESJtzafKUxUacQ8xGbEiPMX3wbh3WG9uTSbqkq4NsWKayDuEbF5uj8eBGkwj-jemz9-JPlXDrTYw51o9v9NI7qzPfsSS9Gvl-t3i93aprrP_dmD1Wz7-7V3Ln3l2KOPfS9uy-tMO4xNE9z_uyeCW5uJciZ79TC0tWinaDDL8JgczlxhyAN0neENaLI3ogQeiXAtOzNkT6h5tNEy31bORaGRjx2QLdsmOzqS-bRzo22gMaraGPH-RbtR2m7OuymTp-VF-TBFCM0S6Sq_f_aYmNF2PAp-zBkUw18xAoGmEuUr5KpwPn63DB00t1sDD84-x09vTgCkaIqtWyETEBn3e3N69srw5KrAuou6ilyMlnkePFgNobCIH81hMU_gD3TwFQytvlPkGE9tEC6KKXxaHt_8xJArWbIv8ZDKuXC3OucLURXa6VQ5oRwRn-cBuMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=dmkJZS2NPIEld1NmsbS6TP6_rUEOKmHjnSMuu3qpy_Gxe6wTe61HnfZbock70QmtpqaScPYh-wACGKjeAtpbcH9P-vEhhnrhuD7ODH1iBU_CQrkzDVyrjjq_MsM1TcHNuKX6LC_0ZMMBXURSC9hH6TH2DmhsFCGdaiDIgxMkmZWKi5OsqSdJrIYL7phMMi-YyeJ_UHk-5dqBqjl51-6OdbaG1vmG8Z3D4seNOwn4yHnU1ESJtzafKUxUacQ8xGbEiPMX3wbh3WG9uTSbqkq4NsWKayDuEbF5uj8eBGkwj-jemz9-JPlXDrTYw51o9v9NI7qzPfsSS9Gvl-t3i93aprrP_dmD1Wz7-7V3Ln3l2KOPfS9uy-tMO4xNE9z_uyeCW5uJciZ79TC0tWinaDDL8JgczlxhyAN0neENaLI3ogQeiXAtOzNkT6h5tNEy31bORaGRjx2QLdsmOzqS-bRzo22gMaraGPH-RbtR2m7OuymTp-VF-TBFCM0S6Sq_f_aYmNF2PAp-zBkUw18xAoGmEuUr5KpwPn63DB00t1sDD84-x09vTgCkaIqtWyETEBn3e3N69srw5KrAuou6ilyMlnkePFgNobCIH81hMU_gD3TwFQytvlPkGE9tEC6KKXxaHt_8xJArWbIv8ZDKuXC3OucLURXa6VQ5oRwRn-cBuMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqTpKqAV4j1O-cLhhx-IZva9SI1X27OKuURNRm9weuGlIPf3-PqrMx3IZuKT539zpmvjm12rrfmt2z7egQudUyOgtOicP3pDA7rV2JgPhZq_Oej7yFZ9cFkyrTScJ7TGBcM31_Pfn1D_LsqaGnGoLRnWdYN3mip-CtJRxextkgWgf5zpvtJCfvp0WjLX1G2ih8CEUlhH7WkTYzANZo0b0KajWbEKYrIThW6TxgBDXx1eCuvgIEJzDjy_JcNLe4vOmZp20dXp7mFlhvN10fCqO3aDQPYeSStwOsNsaubqeRQJwMjw3HYZ_BZ6bwSrD5jtk-wBJt2sZOAmwyCVxZ5VnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=BVFoiu4BbFlS9-woVBFWjn-0ENOPeHFI93yarzL_5tzXOjA55MsMstW-hpNl3MQOLJBSwGSzknvE36PBj42WDO0nynTT1NCaCm6TLnjCF93Dh6BBR6qj3PEkb2nmzILJuUuEPeNKM_MFkCwNKV5xG_raMUzEX9-eBPSqJEi4sAQ-kzjtfC1dCoVC5R33E0iUc0TKJOkcaaC7WYLmOTV_iDyhfJ0ja7KF5Jf5PxdnIG5wpqx8YeG0AlbPV5gdWvMGZqs8EX9jjzyjZb8LT-0h16OcLwiFoXEnk03H2dkI3vf5Isn0b6_yzogCwevGfUOSMLdqlajgt29Tbhsy5MHlsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=BVFoiu4BbFlS9-woVBFWjn-0ENOPeHFI93yarzL_5tzXOjA55MsMstW-hpNl3MQOLJBSwGSzknvE36PBj42WDO0nynTT1NCaCm6TLnjCF93Dh6BBR6qj3PEkb2nmzILJuUuEPeNKM_MFkCwNKV5xG_raMUzEX9-eBPSqJEi4sAQ-kzjtfC1dCoVC5R33E0iUc0TKJOkcaaC7WYLmOTV_iDyhfJ0ja7KF5Jf5PxdnIG5wpqx8YeG0AlbPV5gdWvMGZqs8EX9jjzyjZb8LT-0h16OcLwiFoXEnk03H2dkI3vf5Isn0b6_yzogCwevGfUOSMLdqlajgt29Tbhsy5MHlsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZTvGdvDFVzOi-8goe1BamLRAYKMxTlS3_5vddf50h34e7dg6H-SDG6W6cys7Ictr3yVhFkoDmgdjwzMhSz4veJkeBAtCm1kg3B1Oa1Dr_lanJUskR0sGm4fIFdQqkvcLXCu-039PvlaIRwE6cAPnEB1Agu6Mp4NCJNgLNlU5lWf4E45omAdepmxBgKC2N7RAYZ20jhd_tOWAClv9Sm7Mue9eLZ2Ot75CqCNXlt4k5jKYnaCXT-eT3iy0JLoQiF9Jcdjm7XZTMDt56jAfuZV3KCbuHHJJPb1AZAzDbghbbN1mdWXYz0fZerJH27F6MVjqeAO8XDh3MaLy09uq8Xlfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMzxG5vRvmKRvrNF-FvEsVZuazjBeiISwgb8_ulIpL8bzKqaDIEQASWEt_vsh6rZ4S6Ma6Afukrpj-8Xrwcf7M2jwO3Zf_dn_1tshhNcJ9VghkU4i_pYtEyb-6GV8OJd255ZSlv5A5R2-nXIpxuqGjVatEhX_rtykpK06b7ep79Vp1i2s2zFT2PGmRteH_Y_Xs8cUpgUhGGOpvnnrrPrWeOAx2kBOlVD2ZuDaAJhSI6jIaCarQeT_K3SiMGnoVenddgnF3wbaaDN_xyD18mfW5SWGPmczHhMJ0lsysnrktyojKfq6gdR7lYLNhABLEtzw6H2pLLs9hH0Acb0Yl4QrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdvPI7Eh2NYcCCMbYO9KBKPC5QhIoY3rJa3ywUQfyOzq-jwDvx18DoO_a1ExZBK-V38DbgwWfnh5ArnDTuSkHWNlNKu7D3eWbIUXYNZPE4MwIGweUf0mHTvgbnKjaBgwCH-HYx8pNeC597nsIHzKyZ_v_ZNP5oYBZ3Nt2-7p_h0Qo4bVPEH271AsnIbERUvfGApluHArz9UHaSFIBfs5DGOB36vgwen7LQprRoHtM6COlam0s1a2wqKbrr-6U5flOQv84OhvKSGce0bRISBS4cw52cQXZL-kwaiDglfM_rLWraJsNvHacKaiynh-Ho0WWZYkussUJXhI1JHxKKcVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO7HB3T7Hfdno5gSED4Wd23I--cedU2Ga2g4OsA6jm9kk4TXsTjAlDNFRVOJnbSawEy5EBCyTnEFO9gRfcyqwEEUxf1SlmsZ3XkFfUA1dUpA5C8bBMOY5EmTW4MgUZOvUwiUhzJPGS_egLbUYug2YRLK9cUZC-yzH5ljfY-z70wMVe2aHAM8GmSC8dR7Ld3RD6sdPrz0nn6gUEtbRjN8KRe_gZq4wbACnkaS7_xdKJTPNGlVDNWLnmCkT2MFQ3bsobarfpI2wPrLzTYOkb8gR5YCmuK2g80INeCA-uPGDPUNCj15_bxtCjAi96JTAQyTieJDKyKya3A3FBYdu9VbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=ulP_hMHYvdYTJP7Z5VsWMO5_8ufWvC9qABqsWk8cPsjxoL_zHGFAy8it9G3pm1owZ35a25zJYdue43Zlk3ymcc8_NKkJCx7ZZij7eKLYbXsj1gDiDeJwWYzVvYaBmuAHSZUHydxXdf-VIYUcbxDwIgnIcHNjRtbMCUAW-FaPw4HJmdCAeyZtyOkmpYeCohdQBfdNYe2j30FYpoQYPRd5uGcI6sRo0Rs-lnl-QY72Zo4D-dTDB_4peV-kb51haAu3iL7ZT5_ztzqKUhevKZMvrFjr6v4p8JOVQrO3RVk6uf6wCrIbXi7ujLBK5DwpwDCwHfdsleEA6PrAMhoryAR3XT3yOeuRcXSokB1dmxI0WgK41qxpdAwOZc8snLMx7TbdsXets6MKESCN3x19eKIp-UmqBsSuvD3aDJIQP_1phdhgo4pSPzN-FyW1D4bO0PJYwsHFWQ4K3K5J1oAwvpxo26tmF-7VecONmoSoav9dt-vHvulg7gMG9VoXFLxFF3IhgltVD2spK4wBTf9izOBounEK-Vvf_9W3rYVTKcnV1yta4KD5ypvH3mNkN06yfmk1U9DXcOHM5Mn-6Wcmo90EsjiHRVfFXnGo5GfVcK_JxbPiqL5joJbOhdf1RY3gMpwEzqePdzJOr3ZcJhnVE_q_sxBIrNHcDUMDEN-VOrtZu7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=ulP_hMHYvdYTJP7Z5VsWMO5_8ufWvC9qABqsWk8cPsjxoL_zHGFAy8it9G3pm1owZ35a25zJYdue43Zlk3ymcc8_NKkJCx7ZZij7eKLYbXsj1gDiDeJwWYzVvYaBmuAHSZUHydxXdf-VIYUcbxDwIgnIcHNjRtbMCUAW-FaPw4HJmdCAeyZtyOkmpYeCohdQBfdNYe2j30FYpoQYPRd5uGcI6sRo0Rs-lnl-QY72Zo4D-dTDB_4peV-kb51haAu3iL7ZT5_ztzqKUhevKZMvrFjr6v4p8JOVQrO3RVk6uf6wCrIbXi7ujLBK5DwpwDCwHfdsleEA6PrAMhoryAR3XT3yOeuRcXSokB1dmxI0WgK41qxpdAwOZc8snLMx7TbdsXets6MKESCN3x19eKIp-UmqBsSuvD3aDJIQP_1phdhgo4pSPzN-FyW1D4bO0PJYwsHFWQ4K3K5J1oAwvpxo26tmF-7VecONmoSoav9dt-vHvulg7gMG9VoXFLxFF3IhgltVD2spK4wBTf9izOBounEK-Vvf_9W3rYVTKcnV1yta4KD5ypvH3mNkN06yfmk1U9DXcOHM5Mn-6Wcmo90EsjiHRVfFXnGo5GfVcK_JxbPiqL5joJbOhdf1RY3gMpwEzqePdzJOr3ZcJhnVE_q_sxBIrNHcDUMDEN-VOrtZu7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhbfeBbrlniPTTG-gxtfOqaxq48uptv-8D4IBz-mkX3EsYN48puqCwmk4uAOifRuHtYjzA-3DtGdvvWxgHsLHzvVV53sJRs2k-cPQT2a7tCOquAbSzFSrHyGEOVDej9qWBnDuQWhOUrkld4xZxDKmH2wTSklX8bu5KMgFDbw-FMceWaVv1LD0n6dnOo8FNymNCGVoIEON8lbHdJb4YS7lbe3ary-ptHJw5logvUyeIA97mvd49cCLDkwSB6O14-x4oAjlBdtH-QbZB76eJ0SGSiqhzL18hW-CBofXpRVW4HKmqW_DnfJgdfn6-juXvlXiXI3ukGjZZ8GtM5ze99W6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjMWp-cN-nGIjkL4LAiP7UxjhPTln9qxFsrK1guH0cf9KDV81hm0la6dlpL9p4ntf0PQH7Dn1IJfsDDn9MpvtewJedIjRy2uY8n4dRCpt7zQKIDkCeu4CU7RFGiWSar-HNKcax_nI0m-ICj1KOHKzRT4SPkwDN2xZS-1RbqyIgF7TjMbbhf88V74ZWjp9hvGsqhlID77hUIsLqHZaYMLb95FpGM8COmMlqrUcFSmJBeEoSoaeq_Y_n73lwlzIG_vkPpenJLN21KtUTTqVhBRjYNpmolKz4a-UIuvS6YvAWqFLT4ObDeCRrOd5gLRtTSYZwyPuwIkSnD1ItQ4gfH1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
