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
<img src="https://cdn4.telesco.pe/file/CYmjr-x9uLu12tVcN89f4EPKRSCW-iJ0vcLSZoz6WpS4YEE4r-P40kipEEVDx5Zjel7R83iyHKQ6g_zhbpQPN9SdHGSYhxAiS-N45iCfY3bK_6AdPYRGVodCQPJmtx04sUTGNTyYfRxx6IlIz7UHd-VHiyULVgbQjApRS5zHM4PgTUg4HQBTlV41MOqWAU5vrOBGL9dh43s6aGTAGDgmXyevds8eEjcDi0GcIFKmLS5zWCETgwvOpNIXMEp_LBNdOl8xs0Xgz39GOYm2d-FG0YyB7wH4Ys1CcM-UJJ67rHjxyJL6rkO1ET5DMr2Wk1-qT3SNXua3lj-IP1cSU5m9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-655696">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
هزینه اخذ پاسپورت حدود دو برابر شد!
🔹
در شرایطی که هزینه اخذ پاسپورت در سال ۱۴۰۳، طی سه مرحله از ۴۰۰ هزار تومان به ۹۰۰ هزار تومان رسیده بود، در سال ۱۴۰۴ این هزینه به حدود یک میلیون و ۱۶۰ هزار تومان جهش پیدا کرد؛ اما حالا هزینه اخذ پاسپورت بین‌الملل به دو میلیون و ۲۰۰ هزار تومان رسیده و همزمان با افزایش تورم، هزینه‌های خدمات پلیس +۱۰ هم افزایش چشمگیری داشته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/akhbarefori/655696" target="_blank">📅 10:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اعتبار دومین مرحله خرید کارت امید مادران شارژ شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/655695" target="_blank">📅 10:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXU3mBTie_CgkNuaaAUc9wI9ixBbFcDTHxDiOE79WCBV--KIH_z38TIilPCn4e--w2zM5vnGfNnAafBCfpCsM_r5k7_P1nvYG-zDTdiqFSHiFE3Y7CA7wi3-kGulW-rmnCO5DXGEox2zTTtaw1hEGcL1YBONJ_Lsz4D0msr0OU6sG_I8M2ExOUoTiaxLDYJnLJKj0wOlGdfsE4GogrlAHi-jJFbkLOkUzQEic_JNl36viyYWJDFrxV_sxvC8fhmUz8wCBPOdV4EkSE3CDE_2UiGDK4ZQlovWGSQRKB16GweY_-aQth1bsmjSmUYXPd2FsitIfAd1LKSydsGji3dtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثروتمندان فوق‌ثروتمند جهان کجا بیشتر می‌شوند؟/ آمریکا اول، چین دوم
🔹
پیش‌بینی می‌شود تا سال ۲۰۲۶، آمریکا بیشترین افزایش ثروتمندان فوق‌ثروتمند را داشته باشد و چین در رتبه دوم قرار گیرد.
🔹
هند نیز رشد قابل‌توجهی را تجربه می‌کند، در حالی که لهستان، قطر و ترکیه سریع‌ترین رشد درصدی را خواهند داشت. این روند نشان‌دهنده گسترش خلق ثروت از اقتصادهای سنتی به بازارهای نوظهور است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/akhbarefori/655694" target="_blank">📅 10:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ-3k04-DFfFLaNM-OXXDFKUbTQc1L0y-VFJHvuZTCQyd9cxCGCKqR-xoSSC35ZLF67q91BoTf3qInWCV8CbIH_mhIxd0gl-B77-sQofEdd0URZdGJmM-31HKw0ZWdBc7P0HI-Alt-rxtfVlLpYQhuusWPIIclG4fPtqc2kuEeheuSQACT4FtU8s5koSVMZhOMB5wPIaIFBQJ988y-mv_wwC8pRv5gfOrZhqDfTvtlx7PYDHv048KStpc-JUwCkpN70IwKZV7q9H-KO8QcwVMxKOTMl1spMBx8grPgVnMcaRN_rfMC4Bb6DahsQjFPtMHt4vEsmu3QyvpLsDK36Cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بارش‌های سیل آسا در راه ایران؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/655693" target="_blank">📅 10:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893412ed0a.mp4?token=TKu8IZtjNYysEWik7ACWLoQ64h6KW-jzHT6Znwratcc83bK6J9n6p-FFKcXiFmD-a03nesb8HkKxz9SI1uOpLlrpeIZ8nh58VUjN_K26QlQqUxaeDlr7rukoEmCyMThAHfPYqPWS4WR1Q-oFJrqMOfFoQEclBuq2mAhpdpdshi_CufmAQCW7kvLSYcLydGIEPoLOXRWu1yxEdQ2x6a3J4mRKqZkjwOv3gCul3cjM0T3EPW3DaHCC-IXTUvsGwx5qihWNmy2f0QSMbKYaDPY95v8m-6n2D7nUImFY-9YpJnonf4OSRXebf5_LoVqB7ZhyWeuuoWmbhKmnebjtp2mxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893412ed0a.mp4?token=TKu8IZtjNYysEWik7ACWLoQ64h6KW-jzHT6Znwratcc83bK6J9n6p-FFKcXiFmD-a03nesb8HkKxz9SI1uOpLlrpeIZ8nh58VUjN_K26QlQqUxaeDlr7rukoEmCyMThAHfPYqPWS4WR1Q-oFJrqMOfFoQEclBuq2mAhpdpdshi_CufmAQCW7kvLSYcLydGIEPoLOXRWu1yxEdQ2x6a3J4mRKqZkjwOv3gCul3cjM0T3EPW3DaHCC-IXTUvsGwx5qihWNmy2f0QSMbKYaDPY95v8m-6n2D7nUImFY-9YpJnonf4OSRXebf5_LoVqB7ZhyWeuuoWmbhKmnebjtp2mxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احترام از «خودت» شروع می‌شه
✋
این ۳ تا عادت رو کنار بذار تا نگاهِ دنیا بهت عوض بشه.  #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/655692" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
بحرین نوتام(ممنوعیت پرواز) صادر کرد
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/655691" target="_blank">📅 10:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiV2D1CByginRXIPImjjuI6qEyfOkdduSMo_ZnNP2SS25EzNnUeyk6NJ7UN0FbTE0WPZBC5uH95V81Xzs4_Ek1E3EohcWPbRhGFGAGmaY6V5C9btfQ_iRveO2Kiz7zQQ4crwfIfZI_CvWaYH-v1z1ciHGm2vB0JjH4Kbk8vSkdAn3Nqd5Fac5APik5dwd70v_wyoxPS7TwP0Kujp-IdyE1FbgRxQ3mAuV82tr3ASqSkCFmhES71YAw2YJARa963FCaCutrB_edhVxQvU8oxhfFzvIpSokenKMQJpc2uJEgiQiWuoexX6ZrcpT_ruxSbCiot9AdKFZruWW22-9iY27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
نوشهر
📍
چلک
۱۰۰۰ متر زمین
۶۵۰ متر بنا
تعداد خواب ۵
استخر داخلی
چشم انداز جنگل و دریا
سند تکبرگ و مجوز ساخت
شهرک معتبر و برند
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir/</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/akhbarefori/655690" target="_blank">📅 10:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cf92e7e83.mp4?token=ZBJyEXksW1AW6HRl_3gTCgpOfC_qyyq7XaXlLNU-bxjupDwdwnEGPAVPeWjXMK5PKdKrkq4xQFQ1GPxUdORi24B21L3v4GMlECYiZLeLTSjYDbv5Li3Pc6iKlAcD8z7d22hmG9crtQv3p5sFLDdoYiuRoK0ZwhE_R2HYnxXCy6gvtYM_KbFslpXTCGp6zlGf2rg-pFsQDEXMo77gObUxHpVy3rsERilbt6KJaWbFYtNWuDrQcxYpjJgONN6o6mi2EK_yMnxH6N7L9unIqkQ4VvZtGy2F6I39S-4USi-I7Geq5fTROMUA5Idsgafg6Zj8wNzvs3CFTe256zOcxrpmnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cf92e7e83.mp4?token=ZBJyEXksW1AW6HRl_3gTCgpOfC_qyyq7XaXlLNU-bxjupDwdwnEGPAVPeWjXMK5PKdKrkq4xQFQ1GPxUdORi24B21L3v4GMlECYiZLeLTSjYDbv5Li3Pc6iKlAcD8z7d22hmG9crtQv3p5sFLDdoYiuRoK0ZwhE_R2HYnxXCy6gvtYM_KbFslpXTCGp6zlGf2rg-pFsQDEXMo77gObUxHpVy3rsERilbt6KJaWbFYtNWuDrQcxYpjJgONN6o6mi2EK_yMnxH6N7L9unIqkQ4VvZtGy2F6I39S-4USi-I7Geq5fTROMUA5Idsgafg6Zj8wNzvs3CFTe256zOcxrpmnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله خرس در ژاپن؛ ۴ نفر زخمی شدند
🔹
در حمله یک خرس به دو کارخانه و یک منطقه مسکونی در استان فوکوشیمای ژاپن، چهار نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/akhbarefori/655689" target="_blank">📅 09:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f56cfb493.mp4?token=I5r1gp1F2LvNz3m0n48Vl5nYajyB9alRF25E3Yi1CmPd5KfW4C4F_yjQiP1IxoKW4X0_ZqHUywIqsRnHG1xYThBv9I63iA-KtjjHwbmRUm9F0hE31WzgBZn47r1YPSgi-FM2hXsbbnheJngY2fWlscLYWjLkIAziZrqs5yFcPkZCLiTYljf3UXDType22rQidytSu_HxHXDncOLZbrKQOAkEakDZJJV4ISPWv1yspNH3PMYIcRAHtL24l40PaZIGcXZnr7xNeJEBchR4N60_mkj81-Z3vqt2q3zSE-rr5BJpvnuvp1MtxXXeiwYAbqVP6JxZ4E0a4zMw2oHd2Ry0i4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f56cfb493.mp4?token=I5r1gp1F2LvNz3m0n48Vl5nYajyB9alRF25E3Yi1CmPd5KfW4C4F_yjQiP1IxoKW4X0_ZqHUywIqsRnHG1xYThBv9I63iA-KtjjHwbmRUm9F0hE31WzgBZn47r1YPSgi-FM2hXsbbnheJngY2fWlscLYWjLkIAziZrqs5yFcPkZCLiTYljf3UXDType22rQidytSu_HxHXDncOLZbrKQOAkEakDZJJV4ISPWv1yspNH3PMYIcRAHtL24l40PaZIGcXZnr7xNeJEBchR4N60_mkj81-Z3vqt2q3zSE-rr5BJpvnuvp1MtxXXeiwYAbqVP6JxZ4E0a4zMw2oHd2Ry0i4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروگان‌گیری و تهدید به بمب‌گذاری در کالیفرنیا
🔹
پلیس بیکرزفیلد اعلام کرد فردی که احتمالاً جلیقه یا کمربند انفجاری همراه دارد، چند نفر را در یک شعبه بانک چیس گروگان گرفته است.
🔹
نیروهای پلیس پس از دریافت تهدید بمب‌گذاری، محل را محاصره و مذاکرات با گروگان‌گیر را آغاز کردند.
🔹
به گفته پلیس، تاکنون یکی از گروگان‌ها آزاد شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/655686" target="_blank">📅 09:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بیانیه کویت درباره حملات هوایی
🔹
وزارت دفاع کویت بامداد چهارشنبه: ما تحت حمله موشک‌ها و پهپادها هستیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/655685" target="_blank">📅 09:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
طلا روی ترمز افزایش قیمت زد
🔹
قیمت طلا در معاملات روز چهارشنبه بازار جهانی در پی افزایش قیمت نفت که نگرانی‌ها درباره تورم را تشدید کرد، کاهش یافت.
🔹
قیمت هر اونس طلا برای تحویل فوری، ۰.۳ درصد کاهش یافت و به ۴۴۷۱ دلار و ۳۸ سنت رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/655684" target="_blank">📅 09:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655680">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAxuM4TnJzLbLm6MIqVrwlmZNk_-qRevSnxysPjgKWlxU569biQGsNtCkgUaXkBuIoUc71-pi_Xnvpg_iqzCAwwxt8qcJRKj9xVSo-ZO6VQ8zg_4pSzDN5xHRcPaqCNdB4kUJGmEJztgh9_DBY0KEDm5a00OVThbtjqAn6PffjtH0tC5n0cbXyQroLI3c6zhdmxtQYzgyDpAIg4I_lMoE6ANJs_g0mDdLFFwer48oaF8OjmVMCKnY_pJPJ6COAXsIBIYdY9wPGhwX3m-nvV4D7HHLlRtYNKNZhXgauhxYylF0wcudkHoevkFrruEFSxw5esIygvDzH2pl6bBwa6g0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghZIQjQign8HCxdqI9H_rg7xsL5-GMAEWcIAf1WcQSLEZIeQSMbY8UgWaxu_bSL1eFbfE2gJF2VXotrTg_Dy6KAXDhmfvJBNNxSF8lBaRgJBq7YP8eTVH4D_VYINFKyi_wB9-Wr1JnjU7pJu8R1Bqe6MNyyroOaV6mP551AKotNiaWY6vMGwlwzhEWA_w3go-TNfLJx8Bou1R2XnD6mG5Ui161zpL5ITtHUIB1TcOQSdNl6Nth4MDsQKQuQMKjZZ2n5S3ER6rJ7UUO3zmNE_egfQBRJGN5syeZkHRWyG7s_GJRCPdLI6uTOTnPLGZ30PfKZlrd5RLp5xfL3iXTnPVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5177ee38.mp4?token=IxsrNWPPS9kQTNn7pC8o2aXaw5ztmXxAponb9dw2Hj_l8-k63Tb8kisM1QtYF-fjw8IXGqWqYNk-xtZffxZ2yP772FQaEQFA0fPAwhXrSlC8RgbDCNmW0oEnVIb5AldB4ycgqwjf-TFd_dItc39GrMQKw1WK2phFYEWwsdBmgx5W4ZfIqsvtSuvlf_9diZf6alxMS9WXc4XLkpNzYigJ1nVXvBQsn2YHIiUBvsFgbEeVxk_K1NGQztqRUKYkdIrszJhonR_B80rxvq0iBUIJI9DCt2dWrADonEG4gTTYSxZ9DKFqTAJJYkXp6BDd5wRnF1bHCwrpTCMBz9koDordmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5177ee38.mp4?token=IxsrNWPPS9kQTNn7pC8o2aXaw5ztmXxAponb9dw2Hj_l8-k63Tb8kisM1QtYF-fjw8IXGqWqYNk-xtZffxZ2yP772FQaEQFA0fPAwhXrSlC8RgbDCNmW0oEnVIb5AldB4ycgqwjf-TFd_dItc39GrMQKw1WK2phFYEWwsdBmgx5W4ZfIqsvtSuvlf_9diZf6alxMS9WXc4XLkpNzYigJ1nVXvBQsn2YHIiUBvsFgbEeVxk_K1NGQztqRUKYkdIrszJhonR_B80rxvq0iBUIJI9DCt2dWrADonEG4gTTYSxZ9DKFqTAJJYkXp6BDd5wRnF1bHCwrpTCMBz9koDordmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه خودرویی کاروان تیم ملی ترکیه به جام جهانی ۲۰۲۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655680" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655679">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=AVX6pj_aF-WejQw45HdkjgSREKPwDfgQxvF3FX1uz4C9YSUfSg1pV0nJA2ffwFJ6H5wAQin27yw9QRxlL4VTQc3z6sCfrJ1QpD9w3Jz7UDVCtX0EshkPkgL5O38sS-FzXFmV6a8I2FqXdfGamujGd5Fy0fA4i3BpaF_Ba3hxvYIylVvjSW4XHsY3TJU23PNyu5KYmDrLngIewPlcCrrp4hJJO3pMPn-ImbffuafcGCpvP8WegI6WxW33qwmd03wc3B3Bl5xckdwgsMuI_QjtYAsJcWlVsEn2jk2Aikw80DHl1SXJyR152Nnvrynty6qhlzuvY8b3lY0KMAjDWrZ2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=AVX6pj_aF-WejQw45HdkjgSREKPwDfgQxvF3FX1uz4C9YSUfSg1pV0nJA2ffwFJ6H5wAQin27yw9QRxlL4VTQc3z6sCfrJ1QpD9w3Jz7UDVCtX0EshkPkgL5O38sS-FzXFmV6a8I2FqXdfGamujGd5Fy0fA4i3BpaF_Ba3hxvYIylVvjSW4XHsY3TJU23PNyu5KYmDrLngIewPlcCrrp4hJJO3pMPn-ImbffuafcGCpvP8WegI6WxW33qwmd03wc3B3Bl5xckdwgsMuI_QjtYAsJcWlVsEn2jk2Aikw80DHl1SXJyR152Nnvrynty6qhlzuvY8b3lY0KMAjDWrZ2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه این‌مدارس در ایران است؟!
ویدئوی بالا به هیچ وجه از دست ندید.
دبیرستان دخترانه هوشمند مدبّران برنده جایزه بهترین سیستم آموزشی خاورمیانه
"مدارسی از جنس رشد و شکوفایی"
🟢
این مدارس توسط
دکتر علی میرصادقی (روانشناس) طراحی وبنیانگذاری شده است.
✅
همین الان جهت ثبت نام در آزمون ورودی و کسب اطلاعات بیشتر به آیدی زیر  در تلگرام پیام بدهید:
@Modaberane_Barsa
یا عدد 4 را به 3000909030 ارسال کنید .
توجه:این دبیرستان ها تنها در تهران دایر است.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/655679" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655678">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae9_CgCmvG908dpHjwMlFbvb3ZpzwfnUHtQL9JA4nLA7Lthu42E41sk6h-nK7X5iqpLjsxuUI_6yyqsbpK-AOi0OjFQbda3iqS2GymslaspP4aVxkHp2pw8optqUZX-ed1RIwqOQmiP_sYBjtQaJoUvrfXBU85fjuMh2_4LeCSWQv2suhDhFkpWFpVR0NJ-lQy6-CSUOAV4QTgNOT9uMXaDWL34zmtV8QdsetKCCmrX0FoM0HD1XRT3NAwctBSPQ6hNKboB1CTF5JlC0SFDuuWe3VIDzuit8p9k1oKRhWJt-ULXl76QGBTgrri1Aldwp6UxKV-P829XqsOZJzElUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حراج پیراهن پله در اولین بازی جام جهانی ۱۹۵۸ به قیمت ۶ میلیون دلار!
🔹
پله در این بازی دو بار دروازه سوئد را باز کرد و جوان‌ترین گلزن تاریخ جام‌های جهانی شد. این رکورد هنوز شکسته نشده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/655678" target="_blank">📅 09:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655677">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هواشناسی: کسانی که می‌خواهند به شمال بروند، فردا و پس‌فردا منتظر بارش باشند.
🔹
سپاه اصفهان از احتمال شنیده شدن صدای انفجار کنترل شده در محدوده جنوب اصفهان خبر داد.
🔹
سازمان ملل: وضعیت تنگه هرمز معیشت حدود یک میلیارد نفر را تحت تاثیر قرار خواهد داد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/655677" target="_blank">📅 08:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655676">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1vNWTs1PK34gWOGqnkFPV4Eo2tYVrR2OcBx44noi3ac1o1cFhdJm_HoMAHlPC3RZuw-UZoPBYVatCFZT6lDmqrPuOnON6arca_Fg9iwzC4VlZiBwUOHMp2K_YHMjLs31ROchD-nDNQYuWIMHFLqixbTfbgEVRrTEZxCL_H_okocOeLiug9effzXjURteXwB4zjzLJntPzeDFvqDoGmov9hsN25qeFXS7PC_jneijwFeMo8QvLYxFl8whqWw3lLzxXG5Wa77iTXnCGuVKkfqfqx4iyq_AjCMRUeFht1nSYLLcmoTO79N4uBZVh04n9BBAVCFBNZ1EQejUAvE3QuBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655676" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655675">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/549228439c.mp4?token=ipvfcRDu9JGwC0QRuKNYXgL3vKpILCgNFXp2f-XaV-TGOiFS-hFzUEhnA-I8759UppVcWyIFIxmNbOxre1Ql_2anzkkXvRfxvxWFrBpiKEmX2VlXLbRxR2Tl0uIFxYKy3YOcmAR4BTOHGtvwEwAPKWgBb-AT8jc-Vo_Qfj8bS7NrP0GMBcKuCZPr-f_H6zszEYqg0Rz4wQELC08O40B2jGhb3c5Xrt4A-YbdSLXy9N9Wc_iv8dAdHz5CfK5kalDx6jbvZyhgT4zwbP2mRMrWBZdayRZqPDAsqAwuYYJo58hVlcDj_DnYcElphqJN8mrIoAo9z2hishvttCGtHHf6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/549228439c.mp4?token=ipvfcRDu9JGwC0QRuKNYXgL3vKpILCgNFXp2f-XaV-TGOiFS-hFzUEhnA-I8759UppVcWyIFIxmNbOxre1Ql_2anzkkXvRfxvxWFrBpiKEmX2VlXLbRxR2Tl0uIFxYKy3YOcmAR4BTOHGtvwEwAPKWgBb-AT8jc-Vo_Qfj8bS7NrP0GMBcKuCZPr-f_H6zszEYqg0Rz4wQELC08O40B2jGhb3c5Xrt4A-YbdSLXy9N9Wc_iv8dAdHz5CfK5kalDx6jbvZyhgT4zwbP2mRMrWBZdayRZqPDAsqAwuYYJo58hVlcDj_DnYcElphqJN8mrIoAo9z2hishvttCGtHHf6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده در شهرک تبنین در جنوب لبنان بر اثر حملات اشغالگران
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655675" target="_blank">📅 08:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655674">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d8d8d73b.mp4?token=pe-72xqAESYQhieW4ghD78cOpZO17ZJs_4uYusOWUqBmgpNd02SHkLmbwN1ZBhaGjsP4-RpAKE2TLAFmV9FaZawGqo5v7g4JQewM1G_5F267uO_EkQJpQuw7NIjyTULNVJHmS39yVz0VurPVfHqdnv_q1OraPrJ6SeMYxPVMjNcFYO4eISTO0Muoel49E9LcM2y8Oi89DGMSWiqYA5vgrfc61rX9CAc3oOISEf5bx5CSl6ZfCG2APnRpUNAUI4OhtP3Udro_lJS82kpfbSFwkTUPGQNmHjXIRmQQ1f20EHR9rNZO7k2M0ohbCfU6aE8zZa0HtHzZH63bs5ODYeNfPkcsH2Q08ckyDr0WZaBtd32P3LxStwPstr4L3R3wDawaPhEagGT7Tj0q5X5bSSog9FjZT3N9kY70un7ffz1N67LZchfImPPFshXLTWbLcZ2GjudKxdCuXOC9ZGZ-409rpXUKbhI3hPGjCMz8pjCqLd3mSh4yHKbKE8j7I8PaK05z2jAZrF4ka8_-hRwD4XyVwAfekVa78WTzyMrDZXLppTRQ15yTx9s6oZDpgHpRcHfQ80DieKpCfCWdxC-4DgJ5KH1MYK7NwCZWN8OT-7x9BbV0oDLkaqeAYXFfg3b2-tzGDyQPkkd2bKUMz06qkF7mA-3HjH0EGBrQ3LI1_UJY_KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d8d8d73b.mp4?token=pe-72xqAESYQhieW4ghD78cOpZO17ZJs_4uYusOWUqBmgpNd02SHkLmbwN1ZBhaGjsP4-RpAKE2TLAFmV9FaZawGqo5v7g4JQewM1G_5F267uO_EkQJpQuw7NIjyTULNVJHmS39yVz0VurPVfHqdnv_q1OraPrJ6SeMYxPVMjNcFYO4eISTO0Muoel49E9LcM2y8Oi89DGMSWiqYA5vgrfc61rX9CAc3oOISEf5bx5CSl6ZfCG2APnRpUNAUI4OhtP3Udro_lJS82kpfbSFwkTUPGQNmHjXIRmQQ1f20EHR9rNZO7k2M0ohbCfU6aE8zZa0HtHzZH63bs5ODYeNfPkcsH2Q08ckyDr0WZaBtd32P3LxStwPstr4L3R3wDawaPhEagGT7Tj0q5X5bSSog9FjZT3N9kY70un7ffz1N67LZchfImPPFshXLTWbLcZ2GjudKxdCuXOC9ZGZ-409rpXUKbhI3hPGjCMz8pjCqLd3mSh4yHKbKE8j7I8PaK05z2jAZrF4ka8_-hRwD4XyVwAfekVa78WTzyMrDZXLppTRQ15yTx9s6oZDpgHpRcHfQ80DieKpCfCWdxC-4DgJ5KH1MYK7NwCZWN8OT-7x9BbV0oDLkaqeAYXFfg3b2-tzGDyQPkkd2bKUMz06qkF7mA-3HjH0EGBrQ3LI1_UJY_KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب کتیبه عید سعید غدیر در حرم مطهر امام رضا(ع)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655674" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655673">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUc-sGCL5N7BAZeBSQEpvz1ON3oO8ZW-tB6i5ToTblCke06iIOuf5Q8qTKwYIp_9ZKdDuC6WRFaUbBpZddDaapipkQ0GSp6SX_nVA-QEddl0g6Pl55ZxhtAAoHon4n7SmF8kUy_PfXzaYtDToVIY-t1r_q9ouTnP3bxxy8uUike8Ve0ZM2rRFVQekXDHi3MtqbqQ6yFqNEIL2ty_CJ7WSArNKOGKDSChRsjfqjRPEtvcrzc8TEH8r-d6JjiMKeW1_0sGM1TdE9ee6DzKsV5_-6Zcfc_WQ606sbt480OQFVxoPNzB_jSPzdd9vnmbKXQwiRBmn3l_O3fmGCgJJ-e25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین سنی تیم‌های شرکت‌کننده در جام جهانی ۲۰۲۶/ ایران دومین تیم پیر جام
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655673" target="_blank">📅 08:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655672">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پروازها در بحرین، کویت و امارات تا اطلاع‌ثانوی لغو شد
🔹
رسانه‌های عربی گزارش دادند که پروازها در فرودگاه بین‌المللی بحرین، فرودگاه بین‌المللی کویت و فرودگاه‌های دبی و ابوظبی تا «اطلاع‌ثانوی» به‌حالت تعلیق درآمده است./فارس
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655672" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655671">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcef435e9.mp4?token=cr3P2nZr4xR_sR75SktGdxo4yUh8m76Bpo1OuNY80As6E1v551Vr9NZfkGjhTlb-mobn7t0Q7KzZ7tNGRSYNKKRf4WRaGrl6QMD1Ng80VCyIIbXYncm3ZcIUm-nhNJfJ1TKU_dURQ8q7gxAbLHcPGvnnzWAhtUH7yoZrMYzekDpmEcUClY2xtY9E5BadpLn_o1dlGgKkiOaKKxEEuKEzms2JZdfZTFeh8zPdOXiCZYH_Tv1Bl5gcglM-oqyecIcg3jvJG48VySNH0m1ldAGCYX4jsI3UghSVSfpJfw8sN6tlC0P3Co2ByoZVyMP6d7gn5-LESlv591Xd6EIL2BSwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcef435e9.mp4?token=cr3P2nZr4xR_sR75SktGdxo4yUh8m76Bpo1OuNY80As6E1v551Vr9NZfkGjhTlb-mobn7t0Q7KzZ7tNGRSYNKKRf4WRaGrl6QMD1Ng80VCyIIbXYncm3ZcIUm-nhNJfJ1TKU_dURQ8q7gxAbLHcPGvnnzWAhtUH7yoZrMYzekDpmEcUClY2xtY9E5BadpLn_o1dlGgKkiOaKKxEEuKEzms2JZdfZTFeh8zPdOXiCZYH_Tv1Bl5gcglM-oqyecIcg3jvJG48VySNH0m1ldAGCYX4jsI3UghSVSfpJfw8sN6tlC0P3Co2ByoZVyMP6d7gn5-LESlv591Xd6EIL2BSwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید باور نکردنی شنای تایسون  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/655671" target="_blank">📅 08:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655670">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a9afa507.mp4?token=V4p9zBA2T9iK5XaspUJee3kbW80P3L1yX-rBLNIknWJCeRBl9wn1EVoNamA6DssNUU7yZicOg9hAa0G41HIhWubU8ZNw14YIPx3sF93_jDvTDQmv7AWNdukxVgTEABod7rqZURZNJTH8HXI0k79hIv_7f7lWsIoFichKwTKqIYS46jYuY63wBPC51pRLUkocpnsftOcgHJ6zha2z7OmAWUwq76xjVALlFzP-7JhYicZ_qVIZ-uJLJkrnxiP8nVuw4tOis4cHHxYYLjEUR2_dt31p3XMdeezDTa87kv5zNA3QBAWalH1VQrQ-JGxZoIwPKBlyd1puh_yFLIKmLA7efg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a9afa507.mp4?token=V4p9zBA2T9iK5XaspUJee3kbW80P3L1yX-rBLNIknWJCeRBl9wn1EVoNamA6DssNUU7yZicOg9hAa0G41HIhWubU8ZNw14YIPx3sF93_jDvTDQmv7AWNdukxVgTEABod7rqZURZNJTH8HXI0k79hIv_7f7lWsIoFichKwTKqIYS46jYuY63wBPC51pRLUkocpnsftOcgHJ6zha2z7OmAWUwq76xjVALlFzP-7JhYicZ_qVIZ-uJLJkrnxiP8nVuw4tOis4cHHxYYLjEUR2_dt31p3XMdeezDTa87kv5zNA3QBAWalH1VQrQ-JGxZoIwPKBlyd1puh_yFLIKmLA7efg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار خودرو در پمپ گاز اتوبان یاسینی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655670" target="_blank">📅 07:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655669">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
توقف کامل پروازها در بحرین، کویت و امارات
🔹
رسانه‌های عربی گزارش دادند که فعالیت فرودگاه‌ها و تمام پروازها در بحرین، کویت و امارات عربی متحده به دلیل حملات هوایی متوقف شده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/655669" target="_blank">📅 07:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655668">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پوران دخت</div>
  <div class="tg-doc-extra">پادکست کافئین | قسمت بیست هشتم</div>
</div>
<a href="https://t.me/akhbarefori/655668" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
پوران‌دخت ساسانی
🗓
وقتی هدایتِ یک سیستم پر از بدهی و اشتباهاتِ گذشتگان به ما سپرده می‌شود، آیا فرار می‌کنیم یا برای «مرمت در دلِ ویرانی» می‌ایستیم؟ درسِ بزرگِ نخستین پادشاهِ زنِ تاریخ ساسانی برای مدیریتِ بحران‌های امروز.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/655668" target="_blank">📅 07:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655667">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285776b7c.mp4?token=OHgtFRv1BcfO6CtSTtsBgoblG6mLkcNBDr1Cu9rWk-IN_AQE6j3BoM8dqdhO5DtWCSNeDRJA4flccjXM5mPusaQLNbk6drGQkcTm7OWhnc4CwBzAHIGznYMG1aEvvICHv3OK9_o03V2enN78XXcX1mKvmS64tAZDdIl4Z5sG4qOIFAAwiek-PC2CLgSrb27906mRoWLZ54Weqelk4uwBrN67Sg9PjhH8piaAjNk3uXAx51u5JVlvCzcsRgxHAmElAf9FYHewPTH1zXIXA_eFgNc5jbAr42SiWxAumTLlehkOTXvLjCtDwdXrIB2EuNtJog4tPhR6xshbiKLcyIwfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285776b7c.mp4?token=OHgtFRv1BcfO6CtSTtsBgoblG6mLkcNBDr1Cu9rWk-IN_AQE6j3BoM8dqdhO5DtWCSNeDRJA4flccjXM5mPusaQLNbk6drGQkcTm7OWhnc4CwBzAHIGznYMG1aEvvICHv3OK9_o03V2enN78XXcX1mKvmS64tAZDdIl4Z5sG4qOIFAAwiek-PC2CLgSrb27906mRoWLZ54Weqelk4uwBrN67Sg9PjhH8piaAjNk3uXAx51u5JVlvCzcsRgxHAmElAf9FYHewPTH1zXIXA_eFgNc5jbAr42SiWxAumTLlehkOTXvLjCtDwdXrIB2EuNtJog4tPhR6xshbiKLcyIwfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوران‌دخت ؛ نخستین پادشاه زن تاریخ ایران
#پادکست_کافئین
| قسمت بیست‌و‌هشتم
☕️
در این اپیزود به سراغ تاریک‌ترین برهه‌ی تاریخ ساسانی رفتیم؛ روزگاری که بوی خون و طاعون پایتخت را گرفته بود و سرداران در حالِ غارتِ کشور بودند. در این اوجِ ناامیدی، زنی تاجِ پادشاهی را بر سر گذاشت که با دستِ خالی، ماشینِ جنگیِ امپراتوری روم را متوقف کرد و به دادِ اقتصادِ ویران رسید.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/vauuzfo
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655667" target="_blank">📅 07:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655666">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMb5HcSMdEBiuiOe43VGpbB8m3-0D_TeWPr2HITb7qWXB24dczIuKSZNB6lxxxYhO2-7hTKZajye3mP4Sp0VgRiyPmtKCdgWx31It9_e1hlsgr7exJDRLxvMNnyxUUmvzDl-HCUmqKOE7TOdGNoxmbN50Fu7Q-2EswBXMgeswAZM-5_7j1niVr7v29vH4zGWSEeIrdDm8gTGrPtPpdL1RKpbuO52GEde1GBM1i04JSEYvc2D7pKH7kwxgs0B3O-Y_vrN95RANYTnJbhVoYbFBo-wGr0D0jrKy8OJxXOfj14aj39OxYPI2tvVO6T0PrLCZzCY8fjjXsykl-ydfAvCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی هر بشکه نفت برنت از ۹۷ دلار فراتر رفت
🔹
درپی پاسخ قاطع نیروهای‌مسلح ایران به اقدام نظامی آمریکا در منطقۀ خلیج فارس، قیمت نفت برنت با رشد ۱.۰۷ درصدی به ۹۷.۱۱ دلار در هر بشکه رسید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655666" target="_blank">📅 07:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655665">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce24ae559.mp4?token=DzJudBRRYKew0-3mX436zpKVTxYbrjG-YdF3TDFXAyb8nEuDDJ3kRlWiFQD1og2J-7wsgN1Lfb3Fy8Go4yTdpR4VtQxPv_ooBltJR46ZT2ej4cbSCBuC8XqUZAUCXDkzOR6KYpVfXhd8gCaI6C81GN0NSPLibg74B5JDRDZsLjQDqZHLn3EdFrYYkuqBNY1DD_TeoPxy3bBpQCVh1VAo8CBYkeNarOPCsA3A2xG69nSACrU0JhlU7xfchmQCQe61SCAY8edcZJqS9V9kV1noWCPc5Dx22bdtFiWw5ABHqyHXuZs_XQmdyD8ZHHbqpwV73bDg6tWZTQQ1v7GJaIolWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce24ae559.mp4?token=DzJudBRRYKew0-3mX436zpKVTxYbrjG-YdF3TDFXAyb8nEuDDJ3kRlWiFQD1og2J-7wsgN1Lfb3Fy8Go4yTdpR4VtQxPv_ooBltJR46ZT2ej4cbSCBuC8XqUZAUCXDkzOR6KYpVfXhd8gCaI6C81GN0NSPLibg74B5JDRDZsLjQDqZHLn3EdFrYYkuqBNY1DD_TeoPxy3bBpQCVh1VAo8CBYkeNarOPCsA3A2xG69nSACrU0JhlU7xfchmQCQe61SCAY8edcZJqS9V9kV1noWCPc5Dx22bdtFiWw5ABHqyHXuZs_XQmdyD8ZHHbqpwV73bDg6tWZTQQ1v7GJaIolWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر منتسب به لحظه اصابت موشک بالستیک ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/655665" target="_blank">📅 07:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655664">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a2af85ea.mp4?token=amcVjDsEe3dPEZkrgsquRcAjJvN6CX7bzlKZTiknTCPHET3OpR0D_mdoxYgsEuW7c3n6wC2wOp8-cyDVElrNGGZU-xsKgYh3T3Po0wQlaHGVTCvG6mFmRuz0b0ASiToCOrvyO2dkqbPs7YB9InkRnYwY70-Na75cS-zIzbRc8rRhkGmEOGp5BKjioWh3oBoY4iIejdCz86JaTOXXPrVckGy8yMTddPn6M6159RAw0fUDTtyds2vrMBI6PsFQOxGnUcDHfwgAyo-Boyjg-aJnYUBTHzUrJpRYNA9y9IoayZ3rKuf7QgdbiPDCFlYaYKa94pYQBVNfxbfLDT5cUEkKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a2af85ea.mp4?token=amcVjDsEe3dPEZkrgsquRcAjJvN6CX7bzlKZTiknTCPHET3OpR0D_mdoxYgsEuW7c3n6wC2wOp8-cyDVElrNGGZU-xsKgYh3T3Po0wQlaHGVTCvG6mFmRuz0b0ASiToCOrvyO2dkqbPs7YB9InkRnYwY70-Na75cS-zIzbRc8rRhkGmEOGp5BKjioWh3oBoY4iIejdCz86JaTOXXPrVckGy8yMTddPn6M6159RAw0fUDTtyds2vrMBI6PsFQOxGnUcDHfwgAyo-Boyjg-aJnYUBTHzUrJpRYNA9y9IoayZ3rKuf7QgdbiPDCFlYaYKa94pYQBVNfxbfLDT5cUEkKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکمیلی/ گزارش‌ها از حمله به پایگاه «علی السالم»
🔹
برخی منابع عربی می‌گویند که انفجارهایی در شهر «السره» در جنوب کویت و همچنین پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی رخ داده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/655664" target="_blank">📅 07:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655663">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kofguKDhazFzZYmGoWG9nXky42ZYuwSTZDYz8PeMYwU_ta6xXrivQ9OeOCt8v-yxbsTEZ2XYxBNPAxKN_CSEAVcleMVyQoWbIVIc5g81e9dH4bWLg8-j5jcrIJN2jhB2675fEuNbIYnMRPoaTSdC9Tz2X_-wEkh3gKB7oh3Awm2f98Fuh5ZUY9RqXruIM-Eu2IHGcbKtWDbXOicHZGAbIJYPtLudsfv7wh-Iijgju3U82cNPLg8oA366RPC1u_eAqrXUte5IwvOMNTOrpiytgEirY9UQLXiaB6n7Fc_Rjg9zLO8UE4Juqxop_GkflQq525jDhxke-J5njiFDXztImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۳ خرداد ماه
۱۷ ذی‌الحجه ۱۴۴۷
۳ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655663" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655662">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoFMy8UkxsXFM_HpKGV4IIJ_Fwhv2gswAnhqv4R-np6wNuYpbgB2jXbsALfGjyByy2k0NmMHHX09UOrPC_rF8vl7j_dmPB5naamw6A2FuUc-2vvQAgOXVYW2_guiG4Edljz5OBbM-PM7Xu69iCgT9sk52A8fA8BGvoER-qtoMLcm0Xwvb3uc0BEch52n9KKMNEzXUYVliLaN7GbR9stZLebqRmMtbH8xJJweAvVIAu72v1BCBpPYkeRuxr9oicOAbzQatgf7ZExGLOB6QsWtkbuD21lllCj96gvK8NLiLTmdoQvgI_ftzMkIhclR1tnGzQs4gudSPwq1uP-FpNXZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مانیا، فرشته‌ی ۶ ساله‌ی همدانی، مبتلا به سرطان خون، برای تهیه‌ی دارو، نیاز به کمک مالی دارد
💔
🥺
پدرش، کارگر و ساکن خانهٔ اجاره‌ای، توان تأمین مخارج سنگین درمان را ندارد.
😭
❤️‍🩹
هر کمکِ شما، قدمی بزرگ برای کاهش رنج‌های این خانواده و بازگرداندنِ زندگی به این کودک معصوم است. نذرِ سلامتیِ عزیزانتان، مانیا را دوباره راهیِ زندگی کنید.
🙏
😭
🌹
💳
شماره کارت/شبا خیریه: برای کپی کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
| برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/655662" target="_blank">📅 03:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655661">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_oVdnmc9hIQSjJHjAf8B9vBa5dDbixdU4-npRv1EMLNXqjwsUfmr950j0m9Dr9gwyE_IyAPLxsPZV_M44EyU5zQd5iQL2QRIuf75xWOIE8JrXLr0KqNmdiWMAe0J629wknDnkmW-RqteIRCdQiotM91ZR2WKtqDz9p2MqY_-Dj89R1NpKb7SBmF6UcQaQTephBcVNNrRV1R5fbcycen-OyAQ-otVYLJ1LxY_wbvrlA8r7G10nL_roh0lpuwuGHVtqJRjkJvWj2P9v_h_hDjlldKDxrENJ0wsJs45adB6n1O95NFsvfsAoGlUXjTz24ifUjRlCHrUJF4GXmBtZEgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦷
ایمپلنت کره‌ای با روکش
💰
فقط ۲۴,۶۰۰,۰۰۰ تومان
🎯
ویژه ۱۰۰ نفر اول
✅
ثبت‌نام و استفاده از این شرایط ویژه فقط با:
عضویت در کانال تلگرام
و ارسال *نام و شماره تماس* به آیدی زیر
👇
📩
ادمین:
@robindentalclinic
📌
کانال:
https://t.me/RobinClinic</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655661" target="_blank">📅 03:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655660">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا، از جمله الظفره، الصفران و المنهاد و بخش نظامی فرودگاه بین‌المللی دبی در امارات متحده عربی هدف حملات هماهنگ و گسترده قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/655660" target="_blank">📅 03:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655659">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
صدای انفجار مهیبی در شهر قامشلی سوریه شنیده شد
🔹
هنوز مبدا و عامل این انفجار مشخص نیست.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/655659" target="_blank">📅 03:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655657">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند  روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله القاصم الجبارین فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
در اواخر شب گذشته…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/655657" target="_blank">📅 03:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655656">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
‏گزارش‌ها از عراق: وقوع انفجارها در استان اربیل
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/655656" target="_blank">📅 03:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655655">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
منابع عربی از پرواز هواپیماهای جنگی در آسمان استان کرکوک در شمال عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/655655" target="_blank">📅 03:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655654">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سنتکام: ایران پایگاه‌های آمریکا را هدف قرار داد
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که نظامیان این کشور در کشورهای حاشیه خلیج فارس، هدف موشک‌ها و پهپادهای ایرانی قرار گرفتند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/655654" target="_blank">📅 03:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655653">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سنتکام: ایران پایگاه‌های آمریکا را هدف قرار داد
🔹
ارتش آمریکا بامداد چهارشنبه تایید کرد که نظامیان این کشور در کشورهای حاشیه خلیج فارس، هدف موشک‌ها و پهپادهای ایرانی قرار گرفتند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/655653" target="_blank">📅 03:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655650">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔹
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
🔹
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
🔹
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
🔹
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
🔹
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/655650" target="_blank">📅 03:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655649">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
به‌ ادعای برخی رسانه‌های عراقی، شناورهای نظامی در آب‌های نزدیک سواحل امارات هدف اصابت موشک و پهپاد قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/655649" target="_blank">📅 03:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655648">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
فعال‌ شدن آژیر خطر در امارات
🔹
به گفتۀ منابع محلی، آژیرهای خطر حملات هوایی امارات فعال شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655648" target="_blank">📅 03:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655647">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع عربی فعال شدن آژیر هشدار در عربستان را رد کرده و حملات را فعلا محدود به بحرین، کویت گزارش می‌دهند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/655647" target="_blank">📅 03:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655646">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSRK0f4q1WTyth3BCbUA9Vc5q9zC8b1hU1abSpVPk4Nz-W6YQhZnDPGx2M0qm5Ru6f5VZ4WH3xADnaHcuSk_qrBmUjONwdAx9QXuoa5_XWQrbXtCKj-3uNDVpQmX_jakjaicfU4oFLTs7KSnBX3yHfjBoTBclofABPGWDVZsOQMePf1kAIe9Uk-mtbFSf2RJaOb1HWbehUiSWB3RS5JTOZDi5QpDK6Ze2svNmcRCnu44_-Dge3Alpgwg8SjsJeHCqRiChwFeUd0rKPs7atYmDdWeWjE2i4_s-GXrLn6vr9g2ujH-Phr_nRWt-DDoTsbvf54BMeST0_XRxBDwaGksRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدای انفجار در پایگاه‌های آمریکا در بحرین
🔹
منابع عربی از صدای انفجارهای شدید در پایگاه پنجم دریایی آمریکا و پایگاه الجفری بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/655646" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655645">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
توقف کامل پروازها در بحرین، کویت و امارات
🔹
رسانه‌های عربی گزارش دادند که فعالیت فرودگاه‌ها و تمام پروازها در بحرین، کویت و امارات عربی متحده به دلیل حملات هوایی متوقف شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/655645" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655644">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای رسانه‌های عربی: به فرودگاه دبی حمله موشکی شده‌ است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/655644" target="_blank">📅 02:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655643">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
آژیرهای هشدار در دبی به صدا در آمدند/ تمامی پروازها به فرودگاه دبی نیز لغو شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/655643" target="_blank">📅 02:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655642">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
آژیرها در عربستان سعودی نیز به‌صدا درآمدند
🔹
منابع محلی می‌گویند که آژیرهای خطر حملات هوایی در پایگاه‌های آمریکا در خاک عربستان سعودی فعال شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/655642" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655641">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
صدای انفجار در پایگاه‌های آمریکا در بحرین
🔹
منابع عربی از صدای انفجارهای شدید در پایگاه پنجم دریایی آمریکا و پایگاه الجفری بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/655641" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655640">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حملات به بحرین و کویت ادامه دارد
رسانه‌های عربی:
🔹
حملات موشکی و پهپادی به محل استقرار نظامیان آمریکایی در کویت و بحرین ادامه داشته و آژیرهای هشدار قطع نمی‌شوند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/655640" target="_blank">📅 02:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655639">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0969cd4eb.mp4?token=Vib-Rz96Qsgo7Jj0vkxrLQqgNArRE2XojguKWgZIzJhDbPRatKLheHDO61HzZqNoiszqaFqt8puBYJ6SOK5LegOOkAxU8OoGXDkdjVmLiDHCDg-hEzOyOlriTZBC2Puglus0qHd163-hEvLAxHZiWVBEHFl61RZvesbyq49iplEteV80TBi6Xuz1WGaql2k82ThLCvmbk-YY4JsPKV7MpA2Lx9QRvqQXUkApGw_6Fb_fqDVZhs4f9yn0y15Qx8HcJ7W1gnrECk-2vinQuOAVu07bG0pFnHy8gr-3q72WEnSpJej85O6bPDPgZ_7d1T6dcNXyy9olKfUWa4aKqMnoyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0969cd4eb.mp4?token=Vib-Rz96Qsgo7Jj0vkxrLQqgNArRE2XojguKWgZIzJhDbPRatKLheHDO61HzZqNoiszqaFqt8puBYJ6SOK5LegOOkAxU8OoGXDkdjVmLiDHCDg-hEzOyOlriTZBC2Puglus0qHd163-hEvLAxHZiWVBEHFl61RZvesbyq49iplEteV80TBi6Xuz1WGaql2k82ThLCvmbk-YY4JsPKV7MpA2Lx9QRvqQXUkApGw_6Fb_fqDVZhs4f9yn0y15Qx8HcJ7W1gnrECk-2vinQuOAVu07bG0pFnHy8gr-3q72WEnSpJej85O6bPDPgZ_7d1T6dcNXyy9olKfUWa4aKqMnoyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جولان موشک‌ها در آسمان بحرین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/655639" target="_blank">📅 02:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655638">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
دفتر آیت‌الله دکتر محسن حیدری با صدور اطلاعیه‌ای، ضمن تایید خبر سانحه رانندگی برای خودروی حامل این عضو مجلس خبرگان رهبری در جاده هویزه، از سلامت کامل وی و تیم همراه خبر داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655638" target="_blank">📅 02:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655637">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
منابع عربی: آژیرهای هشدار برای بار دوم در بحرین فعال شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/655637" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655635">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09037a0fb6.mp4?token=lzotbB_NvgUGtAGrlh1tR-tYkmWcIYssjOzB9OVCPlgIyqGyUPkDh1nZxI3C76HrMpcXfe8XmHJiBl7rXo4S_2X2dfmQkP3CGqanvicLlKRoWoxwUomUio_0TyNYJgyDwqd1xMG4dymV1QBdvT-R1xSFZ4JqYrBfGd4iivjAJH0NmluJJFk50wWL7s_HZnfKCvM9rSru21zasDrXxh9DVgbYiH1A09uzgiQ1FORjzuRlfAltLfF9KoN2hNOdWn9ac3zhROZ2ZiiI0y2z700Wa2kujH25sZ6mSnCoT6CyPlZSwPxm_NSbBsNOATiWPEsCpoCVEw1TnrCxF2UYRSGNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09037a0fb6.mp4?token=lzotbB_NvgUGtAGrlh1tR-tYkmWcIYssjOzB9OVCPlgIyqGyUPkDh1nZxI3C76HrMpcXfe8XmHJiBl7rXo4S_2X2dfmQkP3CGqanvicLlKRoWoxwUomUio_0TyNYJgyDwqd1xMG4dymV1QBdvT-R1xSFZ4JqYrBfGd4iivjAJH0NmluJJFk50wWL7s_HZnfKCvM9rSru21zasDrXxh9DVgbYiH1A09uzgiQ1FORjzuRlfAltLfF9KoN2hNOdWn9ac3zhROZ2ZiiI0y2z700Wa2kujH25sZ6mSnCoT6CyPlZSwPxm_NSbBsNOATiWPEsCpoCVEw1TnrCxF2UYRSGNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای چندین انفجار شدید در پایگاه‌های آمریکا در بحرین خبر دادند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/655635" target="_blank">📅 02:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655634">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7331c1131.mp4?token=EfS1yF2mRpBrnFHTf_2LTrvW-RySI5NuA4bv71P2anUPb-qzeZnG729hfSATWjfH72djWsSwn-wGDFu2kVFk6fwpSPQpsuLO7-wfdMV3NPz1jvj-6QFYGANZMUeUMJVK1_reLzC7ZigX0dn_vtpfbDPLn_854WUzE6IftbHOV1gJ9EnIZP-k2v6penNP1dfXIYqoKVlUuCbDWNO6jEGybGxPqjfb3UGxffPmnsTM2V_eOzA8VAUtgAFGv6ZwgVzNh-uBHk1q8Am6umJyn6cvRUg5L3TxwtBcjU54ea9wqJZrlzSg3KwVgyZ0G7NyCogh6mNdYLvkAe9P-ueRtjzJng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7331c1131.mp4?token=EfS1yF2mRpBrnFHTf_2LTrvW-RySI5NuA4bv71P2anUPb-qzeZnG729hfSATWjfH72djWsSwn-wGDFu2kVFk6fwpSPQpsuLO7-wfdMV3NPz1jvj-6QFYGANZMUeUMJVK1_reLzC7ZigX0dn_vtpfbDPLn_854WUzE6IftbHOV1gJ9EnIZP-k2v6penNP1dfXIYqoKVlUuCbDWNO6jEGybGxPqjfb3UGxffPmnsTM2V_eOzA8VAUtgAFGv6ZwgVzNh-uBHk1q8Am6umJyn6cvRUg5L3TxwtBcjU54ea9wqJZrlzSg3KwVgyZ0G7NyCogh6mNdYLvkAe9P-ueRtjzJng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از کویتی‌هایی که هنگام رانندگی سعی دارند از فعالیت پدافند هوایی فیلمبرداری کنند و با ماشین تصادف می‌کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655634" target="_blank">📅 02:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
منابع عربی از به صدا درآمدن آژیرهای هشدار در بحرین خبر دادند
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/655633" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
منابع عربی از به صدا درآمدن آژیرهای هشدار در بحرین خبر دادند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/655632" target="_blank">📅 02:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
منابع عربی از حملات جدید علیه مواضع امریکا در کویت خبر می‌دهند/ حداقل ۲ موشک‌های جدید گزارش شده است
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/655631" target="_blank">📅 02:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
منابع عربی از حملات جدید علیه مواضع امریکا در کویت خبر می‌دهند/ حداقل ۲ موشک‌های جدید گزارش شده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/655630" target="_blank">📅 02:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آژیرهای هشدار در کویت بار دیگر فعال شدند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/655629" target="_blank">📅 02:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
مشاهده شدن بقایای موشک رهگیر MIM-104 PAC-3 پاتریوت در کویت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/655628" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
‏گزارش‌ها از عراق: وقوع انفجارها در استان اربیل
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/655627" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
‏گزارش‌ها از عراق: وقوع انفجارها در استان اربیل
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/655626" target="_blank">📅 02:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اکانت اوسینت تکنیکال: حمله امشب به کویت به نظر می‌رسد گسترده‌تر از دو حمله موشکی قبلی باشد
🔹
ساکنان محلی از چندین انفجار (بیش از ۴ یا ۵ انفجار) پشت سر هم خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/655625" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23967e641e.mp4?token=A8SddDRbdrplj5yntrQm5GGtTx2H_6NatiXrLZEXGcrAUnXuzIneHDPSCFn1byL-5KRzQVkppenHTnxk5E_VvHSMT0i_icsZy_ODsGtX9XYtIMjImriU-cAO_7iU0c9fi0Y5sL1hAmefwSSr7z6IsSH5KNiz1wE24L25LIwB2T-MYjLMa5Szfg9Yu_C3Dkr-Wq12D_k2iiMJJw0EhZvP-LkCOk-895cR1rGxDEhRgmWwDmVx-JLiVvbxol7_IbqFs04cZQT1PxcwEzBg015rb22Hq6dgluo4vVqZ19g4raE6gQDlJ4ZnSwGDHvWT6qR72ndMdQYBtPLFvpKjvnE7lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23967e641e.mp4?token=A8SddDRbdrplj5yntrQm5GGtTx2H_6NatiXrLZEXGcrAUnXuzIneHDPSCFn1byL-5KRzQVkppenHTnxk5E_VvHSMT0i_icsZy_ODsGtX9XYtIMjImriU-cAO_7iU0c9fi0Y5sL1hAmefwSSr7z6IsSH5KNiz1wE24L25LIwB2T-MYjLMa5Szfg9Yu_C3Dkr-Wq12D_k2iiMJJw0EhZvP-LkCOk-895cR1rGxDEhRgmWwDmVx-JLiVvbxol7_IbqFs04cZQT1PxcwEzBg015rb22Hq6dgluo4vVqZ19g4raE6gQDlJ4ZnSwGDHvWT6qR72ndMdQYBtPLFvpKjvnE7lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده شدن بقایای موشک رهگیر MIM-104 PAC-3 پاتریوت در کویت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/655624" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی نظامی و انتظامی…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/655623" target="_blank">📅 01:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
صداوسیما به نقل از منابع عربی: انفجارهایی در پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی رخ داده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/655622" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf52095be.mp4?token=QknG6FsphHwzxTYd_xzyephGOh2yfVQRJZP9Jv94bR7dni2cFuFIqsvpQ_SBxDlfHN9wStAHBwFc2p8UW6InawrK8W9GF_i7RkikLGwpVdfu4Eq3wyxvR7nTtc0LiysTCxZ4cfWLbiqyxwiiFmk2pB4tn9CW4s5z2mLxMQafr9M0zm6xS7D_zWU7p0n5Jw24vAOlTO72ey3rJt_V20IYQR_MNJDram-4E3coj6gC_5cYq3kRNWHBxel3lIGXUe1xRXp3E-Azt7orK2ZnJr6WUrT9ZePbgQpnU8c7RPaADq6NEoS1hkLFzclF446a8HMEbjUPK94BUR3kUxwHkv8g9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf52095be.mp4?token=QknG6FsphHwzxTYd_xzyephGOh2yfVQRJZP9Jv94bR7dni2cFuFIqsvpQ_SBxDlfHN9wStAHBwFc2p8UW6InawrK8W9GF_i7RkikLGwpVdfu4Eq3wyxvR7nTtc0LiysTCxZ4cfWLbiqyxwiiFmk2pB4tn9CW4s5z2mLxMQafr9M0zm6xS7D_zWU7p0n5Jw24vAOlTO72ey3rJt_V20IYQR_MNJDram-4E3coj6gC_5cYq3kRNWHBxel3lIGXUe1xRXp3E-Azt7orK2ZnJr6WUrT9ZePbgQpnU8c7RPaADq6NEoS1hkLFzclF446a8HMEbjUPK94BUR3kUxwHkv8g9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری تایید نشده از رفتن موشک‌ها به کویت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/655621" target="_blank">📅 01:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d593af6ec.mp4?token=amH5yJ7fZOSiqP0TZ5dCpz1uMzi9B1cJ1s8r1YRmwjYVkF1jinOlk52RQSTf4q2l-MNxFKjOYRGiyEAVpNHOPPlTR1JVOIDwwKi9LtFfCJGO46OntKsWZEzLXmhyNsprfybu7JJuAzsZZB5Tc8f1NqqgHQQz8HD_pBt_8HlgVtCL4UnRhMM-CmZiHGTcPb04BcSDRz5GWEaFDtcnOMh3TQnK7jdEtL3SDmykiEUUA9PiT1ySqQcLgJJv7hxnV5ZWx25jyLiLAIlGABcW78yM2rbseS0HZf4z7vFsVcBnY0hp19iiaGQKOlqdFSXo4CpolL74ChGBbeJc5EiGgYYXsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d593af6ec.mp4?token=amH5yJ7fZOSiqP0TZ5dCpz1uMzi9B1cJ1s8r1YRmwjYVkF1jinOlk52RQSTf4q2l-MNxFKjOYRGiyEAVpNHOPPlTR1JVOIDwwKi9LtFfCJGO46OntKsWZEzLXmhyNsprfybu7JJuAzsZZB5Tc8f1NqqgHQQz8HD_pBt_8HlgVtCL4UnRhMM-CmZiHGTcPb04BcSDRz5GWEaFDtcnOMh3TQnK7jdEtL3SDmykiEUUA9PiT1ySqQcLgJJv7hxnV5ZWx25jyLiLAIlGABcW78yM2rbseS0HZf4z7vFsVcBnY0hp19iiaGQKOlqdFSXo4CpolL74ChGBbeJc5EiGgYYXsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: مردم محلی می‌گویند که چندین برخورد در پایگاه‌های آمریکایی کویت رخ داده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/655620" target="_blank">📅 01:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
تکمیلی/ گزارش‌ها از حمله به پایگاه «علی السالم»
🔹
برخی منابع عربی می‌گویند که انفجارهایی در شهر «السره» در جنوب کویت و همچنین پایگاه هوایی «علی السالم» محل استقرار نظامیان آمریکایی رخ داده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/655619" target="_blank">📅 01:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای ما یک نفتکش خالی را در خلیج‌فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند
🔹
نفتکش توقیف‌ شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌ شده تمکین نکردند. یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/655618" target="_blank">📅 01:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بیانیه کویت درباره حملات هوایی
🔹
وزارت دفاع کویت بامداد چهارشنبه: ما تحت حمله موشک‌ها و پهپادها هستیم.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/655617" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuXHvBJiMhZJldjeur7QXLPCsNdo5L-7IzEff4zeTVrsZKgB1Ze6aj0EuDwQeAdAMJGwMFsQLxxGmQgdk_1O5doWMafeTWwQZjFz5POJCMA9TSlAXWfY8FZpI2pm-cUgmaXBGfP4tcXMXT0wPtAMVAyE_ABK_jfACiEkJNypWtMPkKzVQhyDUbqwyg3rNH4UJzv1hwuP3LaKfsgQDUSYOZ4_z_tyQ71r6YRVApxqh_1mAIsH8RPGfrYEYyMNzljffRUVQHHo2yxZmmWpWZISAWTmOJiRGU0gWzT-VGAsHte-1xQLMV1C3mSDFTlZzD4oy9aNSNybXSG57nN975vJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از فعال‌ شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/655616" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از فعال‌ شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/655615" target="_blank">📅 01:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده جزیره قشم
🔹
بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
🔹
بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند. پیگیری‌ها برای کسب اطلاع از ماهیت دقیق این انفجار ادامه دارد./ مهر
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/655612" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruxcfhSNEMFbX297pfmESOTUeC2t9SYflLL7SvfQTC5GksA4YOOwvnYfUWEPNMoffJ-m2KK5FVp8lBEdzkLrZNW7gRfWZoK8EZzpeI2BTqqk5oK8SjP1G-fN_dqdeGDorOZPtXBErij-i6GeShKr_JNT3N4ddK06vInYe0sYwGAcWoFBRy72zw8CSAJ3J8DhcHPV865RRgRfGLS3J0V1gq_3knO67ABgPBP62qQdSZ5n7uycP1C5NUrLYJo-yD4OLnCIn4Prl8eHzxqWd_rdvYL-e9nx6HB47mx0dSNkawWBvGs3sOVjSkCrgDQnWlwmvrWkSuU-itOcsrzY5EjBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متوهم
🔹
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی در کنگره که از سوی ناظران متوهمانه و دور از واقعیت‌های میدانی ارزیابی می‌شود، مدعی شد بازگشایی تنگه به‌تنهایی نمی‌تواند زمینه‌ساز لغو تحریم‌ها علیه ایران باشد. وی با رد هرگونه گمانه‌زنی درباره کاهش تحریم‌ها در ازای تضمین امنیت تردد در تنگه، تأکید کرد واشنگتن تنها در صورت توقف غنی‌سازی اورانیوم و رفع آنچه «دلایل اعمال تحریم‌ها» خواند، موضوع کاهش محدود و مشروط تحریم‌ها را بررسی خواهد کرد.
🔹
هفتصدوشصت‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655609" target="_blank">📅 00:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB0peTdfZCmGgyPtYyoVyx2Ndn0iaUPd0c8T_ASHGivlf3OyLqaSBSuZCHqiAgg18TSwLbF2rclrgWQkHkyRM2lS1zrXk2gAEG7LJyz8jpx44NjQaufwhwHx-T2iyXLcv-EYChYAegqMNusfx7do0Dc5sjjFC3G6x0mYB_yEdPNzIYSjAYh2AjzxSB0wEfV2L8WoKWq4225P77xIYZ8Msux6BC-ELhjsbJeJqsjmeg3xHG--eORSLqdtipochXCeMQyVs3vvUwIZ5qGmjtVf1xiGOCoZnp6k31r8JseKeOQ_MAxXfVdpC4MwmLWHcvgHvvyk5L5XKQ8X4ARW5WoQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/655605" target="_blank">📅 23:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا: ما بزرگترین پلتفرم معاملات دارایی‌های دیجیتال در ایران را به دلیل دور زدن تحریم‌ها تحریم کرده‌ایم
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/655604" target="_blank">📅 23:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655603">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا روز سه‌شنبه اعلام کرد که تحریم‌های جدیدی علیه ایران اعمال کرده است.
🔹
طبق بیانیه دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک)، چهار فرد و چهار نهاد مرتبط با ایران، به فهرست تحریمی آمریکا…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/655603" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655602">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
العربی الجدید: مذاکرات لبنان و اسرائیل در واشنگتن به پایان رسید و قرار است فردا ادامه یابد
/ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/655602" target="_blank">📅 23:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655601">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وزیر امور خارجه آمریکا: ما به ایران اجازه نخواهیم داد که هر کسی را که با سپاه پاسداران مرتبط است در هیات اعزامی جام جهانی خود بگنجاند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/655601" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655600">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تعداد خنک‌کننده‌های ایران؛ ۶ میلیون کولر گازی و ۲۵ میلیون کولر آبی!
عبدالامیر یاقوتی، مدیرکل دفتر مدیریت انرژی و برنامه‌ریزی امور مشتریان شرکت توانیر در
#گفتگو
با خبرفوری:
🔹
بر اساس اطلاعات مصرفی ما، قریب به ۶ میلیون کولر گازی و حدود ۲۵ میلیون کولر آبی در کشور وجود دارد.
🔹
از مجموع ۴۳ میلیون مشترک ما، ۳۳ میلیون مربوط به بخش خانگی، ۶ میلیون مربوط کسبه و مشترکین تجاری، ۲ میلیون و ۲۰۰ هزار مورد مربوط به مشترکین بخش کاربردهای عمومی مانند ساختمان‌های اداری و پارک‌ها و...، یک میلیون و ۸۰۰ هزار مورد نیز مربوط به تعرفه کشاورزی هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/655600" target="_blank">📅 23:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655599">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
یورش نظامیان صهیونیست به حومه قنیطره سوریه
🔹
منابع رسانه‌ای سوری از ورود یک گشتی نظامی رژیم صهیونیستی به مناطقی از خاک سوریه در حومه استان قنیطره خبر دادند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/655599" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655598">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
میدل ایست آی: مالک برجسته کشتی‌های یونانی حاضر به پرداخت عوارض عبور از تنگه هرمز به ایران است
غول کشتیرانی یونان و مالک بیش از ۱۵۰ فروند کشتی:
🔹
این عوارض می‌تواند «خسارات» وارد شده به ایران در اثر جنگ آمریکا و اسرائیل را جبران کند/ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/655598" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuV1BqYc6oqY78Cdr7IgfFk44Ktw5z_bjeFwNtIfu2xJzn7wcqwvbwdvlBVN6mclRstPxbT7VDBKo0L--qM8BrGK1-rKU9eS4JVWfUvduRq1g5LjsWkdRqLFyXrY-af8oo5xy1bewdjzjkxy1lvHXXxpeuJrrW9CwJTs_nAplPJtpy3vd9BU1EeoG0AuBtl7xJ1K-suXBN1sS7PADa_iwzp-JvqAiSsw3gc63zRynFgFoYT9-NrNwKV8T8UbCx7l2NsWeFDLwJUXl-OqSdS0SVEaAKhNz2jvtiDGTY4WRWGRU6EXkg8awYb1G7i_A3mMW31rhPa3KueuHINNr_3-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVtZq-o4weV1ILwgECW6_FMpfaz_T04E5b2ZiV9WSDaRFYV0yHsBmBNj7vSdlyW5dofWAdFpFe4BILWJ4_E4vEhFgLlNuUHioUHYz1RRf_9XEb5udbpJL7PKMu6fi_ZEUKZaWMEvLN-Mn_rdhSzKKhekFCrGgm1xQ1jdx2XGyqMfDYEeFDMxG1ufgGzV6FAUnfCsrBZnvNMFu5M5aiFYVChglzNC2DjIJrAjG7EP8D3trM0eGg1OR8aspY27m2FLn7YIYlJ9SBcTuUb5LA7sHm0TOMz2G-QuVKt67Kq9afD5IGBwXRT94H8LMkbQGkHWJHsZPAtoOtgMAfHzofcXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svZkRAHUhdFaEllHoA3b1_raiXFuxFQBJsnwZp_CZjjcDlXRR3OVVmDCzjO2f3T2Y5Q4W_Z0x4aXXcH0EfjqRHCxZfNLfZ5JKJpr4vVxcvT_QtE_823P8Qy9iqk1v7p-ob4IZrdA2S4t0lemFEyMWnKNMCuCnPWJBfuN1QxgevG7d3QtV6-zh55xuPLLdidWjVxrXvyNwAJ1eJMZGQkwqXMfNO8DQ-_TUArBFVxm6-DbV8DrJWz8cj537lQcY6yqeL9UrcCE3BeYQ5rOJU4K9Xm0V8xjzLooRmP2TVLpXlynaTGdipllN14KRj4Bpx8kh97hXYGiitBXiNdtqSXYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccq0C8JCMIFRtKqOOXWP6PJwT0d4vfetjbfTizGwbfFBd0_CLFxuGwQOlUdahwZJFBRkg6RBY1mBI0AAPi8ZaJR-MDLsFKdHHqc7GDbhcLQm6LPtiXSVopo4rxqmaeZcX002-sS5fHR_SWVHzJ_1zKFmVtU7uoutfwkmTxpbALUzsHzG-L3W0Hu-E2WtaUWOnsaNRIn9Qvm-vRiOaZp0V_x5UU8MLzUBSgNnb7EJJIy6Bp5ss11fk4mO0gGckE-j0Nc7adkG0dgMU7NIzTA6iql8gmRF45KF2UOHFa92KFktjcujQbRp5FVvWePpSwuNxHUsE4Jak0Zi8QFWKIZaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePgDJQQp1XhSw5FAZxxNcRSgymiIH64tR4Q6HzJ7OFb2tZlqz1NdubQwYJDQWkiVCm09p7SHQbDJUbDzP9PXL9b8t1FoGghe9Nc8jGAMKSEsQW_J87ustVzuzQ_k_eB-W1vEtcmoHvbVWewFsa36Ol1flVYhJNCyMN5Irxzvxjftau3cP3MTOOm_et0PtzPJB84FDhwIkzBOk6oABa3PyWs8Ap7rovvVKzjNvFwry_FvFC5FcaILI6nknn1O20ANoIajYocQCoJdTtaWhrxC3XxhrLWJX0grS5PUSi5AnUdiVLDxyrOrbPPHBJ-7wpIJ5tTX6VmmYaIAJmXqNiyoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au2xZ8Tm8RQ2hcO3rsw-WG0Ec5eiZ2_zeEkMHm7sxKZQgyknYXHRX_44j0p1dJC6u8-g34Q-cEkddwTxBEJ7HSLrDbtMYzgoG_eG0xavjjrExlkxYkJgV-8O8PMbXLlglYUL4Hybb6jX1PsB_5fsyB1asthsV6RZAtLu5jmuZeTLkooG5YDIKUruptHCcf_bsGmhD8bsXjGSfxNGoXgP1X0tyj7nHmh363Isaweq9m4IJj8cjG3RHg6HirLacy7EyE5fTAVAeoSxR16g-tvx8xQz-KKA0KGdz6KWszN821S3gLNnQaZYtbGBSwpl7MuJxfq24s0CzmgwL_p0AHBnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Simh_iveBEfwrQfftHeh9dDNqhc6HnSkS5PijmHyliTdhF9Bzq_qnLwy_xInVwALILLrW3tr_0Jn7I-n3zBR-SI9jsI3UMMbc_kJSNkOvXm9kbf0m0ADcm94i447vP96sg6JBFWMvz2RWhafXaHHW6t-OA3uzNIasXenXp4jUKt59apNldWGpysHW1aaTMrwzyXokwX09pX-lOyodk3sdr9STo7olj33Ibq_1tN7-z3qhkU2_ji_AEbESpOLqI6ufiDpqt9au9yWNvQYacbYobXUMqORwyY6L4p67QYcxaMKrXF7u4zpYOGo-XLTpPdHJSPILrB0UQmkD2mZK_TLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbMl0pkAaVlyF6jSM_DWV39740pAP_5cCeRCieP_619liIZVgrb6fTauDFVycja284DVIC8mCvHuwOmzd8zDzhWvi0dUIAUBKw3ikAxEtOQW8HdF08wAu800PM_PUDyFYZqB-TtQ-KghOSnw37Xc3nUle6GC7XgTEsy1-R3T3ICa_hQDS3uPBUBUnMVxEC-p8w0jRxHmfbpuOs0-0dg6XKgPxZ0Az9C9C5siz9QPtPKkE3V-ZTQskl4joKrBTYwWsA82Yz3mG0MJJ4_dWpeG_GTGAtdsVnlT1FP8HWRBtLxT30ZEx4k90S9nmU_eLkjcfUsUCgm-nQkPQxNDbRCzYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWOsptmPBXZIuSKV2UVdLYFOYQJMZiBMrv0NertyHuscdE-lXjbIX9QFWCVn486qrbh7CFdS-DcxdklezfJJ9ULvy5yD0r15XRB__1oKusZhSRbvD2bBPbrl4t-C0vwkaMsB6LZ0IvRmvI0v_eFIDDkKx4g8iZ_kOL75KldVBPfpdkzz2Z7WAqSTKAB9dMeI6_sjeNZ8ra8WyOHkXelcgHgD4nJe9Std8JhU68_TtIQuW19DvnTsKtC-7WjZ7CPmtaVWIUkoC4b_VetspImCXyjFYZ7gy5xsnuznX-h6irXoa4RbJgHDM988rSnN1npsC7kLslO7ZloPLgrQ8nCJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak70l-4JfQUO3LFwsKQAZdo-O0D20gehLDLdBIf5blBSvIhrMCPN1Jh3oJxdzuhW-eHXRmaZ8YbeuVCobnLZEtpp7n7_gHy4ZqUrKQ_rsVlx6fKVa95omyxR89aL0LkVJbzYjWhk8sY5SDx819oh48wLvYrlM4eDZhope4YXZr1gJF7uKargycmfETHcnbznN5sj0-35RGOM8ImDBFAwMAUF-I3gO4t8Mkr1SOq8JxjMURbhwVxB3GgIzeMGxchGz1UCcFyxARLAdYUiJqGyAn2M9ro2-LjzFOPbrqmuo3Ojh67kAvs2EZ54z7rfizn_hRn_2kXx0KNaiZQeucaizQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قاب ماندگار ۳۶ سال سخنرانی رهبر شهید انقلاب در سالگرد رحلت حضرت امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/655588" target="_blank">📅 23:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
افشاگری آکسیوس از تماس تلفنی محرمانه ترامپ و نتانیاهو/ تو دیوانه ای لعنتی!
👇
khabarfoori.com/fa/tiny/news-3219715
🔹
جزئیات ادعایی نیویورک‌تایمز از پیش‌نویس توافق تهران و واشنگتن
👇
khabarfoori.com/fa/tiny/news-3219710
🔹
آیا کیم کارداشیان می‌تواند رئیس جمهور آمریکا شود؟
👇
khabarfoori.com/fa/tiny/news-3219908
🔹
سود هنگفت سوریه از جنگ آمریکا با ایران
👇
khabarfoori.com/fa/tiny/news-3219965
🔹
همسر بازیگر مشهور سه‌ ماه پس از مرگ او ازدواج کرد
👇
khabarfoori.com/fa/tiny/news-3219631
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/655587" target="_blank">📅 23:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655586">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اعلام زمان دیدار تدارکاتی مردان والیبال ایران با برزیل
🔹
ساعت ۳۰ دقیقه بامداد روز یکشنبه ۱۷ خرداد به وقت تهران تیم ملی والیبال برزیل به مصاف تیم ایران می‌رود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/655586" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای یک نماینده: کالابرگ تنها کفاف کمتر از نصف کالری مورد نیاز مردم را می‌دهد!
حامد یزدیان، عضو کمیسیون کشاورزی مجلس در
#گفتگو
با خبرفوری:
🔹
در حال حاضر با نوساناتی که در بازار اتفاق می‌افتد عملا عددی که در قالب کالابرگ پرداخت می‌شود کفاف کالری مورد نیاز مردم را نمی‌دهد و شاید کمتر از نصف میزان مورد نیاز است و باید دوبرابر شود. مردم به خصوص مواد پروتئینی را به خاطر افزایش قیمت‌ها کمتر استفاده می‌کنند.
🔹
یکی از اتفاقات بد در سیستم وزارت جهاد کشاورزی تغییر مدیریت‌ها و معاونت‌هایی است که به‌ خصوص در این دو سال گذشته زیاد اتفاق افتاده و عمدتا نگاه سیاسی بوده که موجب شده است ثبات تصمیم‌گیری را در زمینه واردات نهاده و تولید دام و طیور نداشته باشیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/655585" target="_blank">📅 23:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOzs6rotKj6mEcXXupYVyp6TptUmuyAvt8obzEz3JdNva4Q5prutuGP4fknHOUNY9KmLlcJDssaFAFZyr7JbkrdISesHk2fxreTkWcqRoNbBQ3Xutvz0hXixv6J8PnckI3SI59WsR0bly_IQqXnE-HyFZJEgGlc0VySlcyUIjioRS799b48zBRXOHQ015U-ZrrMCurrCusulBeTjsBPr629_TACGJbK-mIiIBWEzM8_-J_89rFWHhF4pS4sXTGf8g947OSbAQD4VFjEoIrKyMNNbUromCqqZx_80mCE3kFgeNg81NuHQJzv1iEUMXxfvKVlgrpMCL7kQGb_H_n7ZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط آزاد قدرت خرید وام مسکن از ۲۷ متر به ۶ متر
🔹
قدرت خرید وام مسکن در ایران که در اواسط دولت احمدی‌نژاد به کمتر از ۶ متر مربع رسیده بود، در سال ۱۳۹۷ با افزایش پیاپی وام در دولت روحانی به حدود ۲۷ متر مربع جهش کرد.
🔹
اما از آن سال به بعد، تندباد تورم مسکن، ارزش واقعی وام را در هم کوبید. به طوری که قدرت خرید این تسهیلات در اواسط ۱۴۰۲ دوباره به ۶ متر مربع سقوط کرد.
🔹
با فرض میانگین ۹۶ متری خانه‌های تهران، وام مسکن اکنون کمتر از ۱۰ درصد قیمت یک خانه معمولی را پوشش می‌دهد. نسبتی که در سال ۹۷ بالای ۲۵ درصد بود. میانگین بلندمدت این نسبت نیز زیر ۱۴ درصد است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/655584" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655583">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گروسی: توافق برای پایان جنگ ایران بدون راستی‌آزمایی و نظارت بسیار قوی بر مفاد آن قابل تصور نیست
🔹
مدیرکل آژانس انرژی اتمی مدعی شد فعالیت‌های هسته‌ای در ایران، اکنون «متوقف شده است».
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/655583" target="_blank">📅 23:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655582">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
گفتگوی تلفنی وزرای امور خارجه ایران و عربستان
🔹
عراقچی و فیصل بن فرحان وزرای امور خارجه ایران و عربستان درباره آخرین روندهای دیپلماتیک برای کاهش تنش در منطقه غرب آسیا گفتگو و تبادل نظر شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655582" target="_blank">📅 23:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655581">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc167b19f2.mp4?token=TH1PxQ8rs9hUrT_yUmq1edQuYJG6Cfi_grYyvyUNS5I0KwlNP0Ze4AK3gRH87Md0LHXgNAPfwz_UOe1AZ5EoINux_7hv2oz99eUWKjcyP7ziSdf6w3lcBgwhp0dmz07sH37Pc1ndg2RRbf5EnnBop0SRB5ycog5vfHj-11nCyzdxoOaOLbhBxGT9JG_xy0ADcWtBOLEZJfEuk7lzSCvRo7heTAsY4yEl9yRZiu1-RYkSjixh9GBrz0YFdxO20LbmTVPLasaQessWG9G0FqD7oCSgRnNW8kGHXCAivq-sqBbja3sRrNJk8lxmfuvwuPkhgKwifw_jzPoI7EBqClo79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc167b19f2.mp4?token=TH1PxQ8rs9hUrT_yUmq1edQuYJG6Cfi_grYyvyUNS5I0KwlNP0Ze4AK3gRH87Md0LHXgNAPfwz_UOe1AZ5EoINux_7hv2oz99eUWKjcyP7ziSdf6w3lcBgwhp0dmz07sH37Pc1ndg2RRbf5EnnBop0SRB5ycog5vfHj-11nCyzdxoOaOLbhBxGT9JG_xy0ADcWtBOLEZJfEuk7lzSCvRo7heTAsY4yEl9yRZiu1-RYkSjixh9GBrz0YFdxO20LbmTVPLasaQessWG9G0FqD7oCSgRnNW8kGHXCAivq-sqBbja3sRrNJk8lxmfuvwuPkhgKwifw_jzPoI7EBqClo79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور معترضان به نسل‌کشی در فلسطین در جلسه استماع روبیو
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/655581" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655580">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
استعفای فرمانده ارشد عملیات ارتش رژیم صهیونیستی
🔹
سرتیپ و فرمانده تیپ عملیات ارتش رژیم صهیونیستی، در پی آغاز تحقیقات علیه خود، از سمتش کناره‌گیری کرد و خواستار پایان خدمت خود شد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/655580" target="_blank">📅 23:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muF3l0ni7g7hf_Oy7kLr2O8LaZDONTjcRpu9CGUcbiuA423I7xyVJTnMIv9F7oXdvC5bX7C_9k0itpe_b8AcrZKQYaJOwomwYrOtfZhQVY6Z1P9So4n4K2xzPUiamwgQE3fjlmt2PA9fikTiPyQ4HgARNNJlrHVUmEUuU4YuJ7Pf817FojhWE-PVuinDhatrJmZjU_EF8ZgkT_ZHDdLWqMPW4h8Ys6xSfkDAfpD0CLeH3LgjRmG2AP9KZ_EBSN-WxtZ0gjjVMOuTFTmC60o0Bic_BTsOzkniHm3fyiGaZuWSkrdejoSAb1j6LA4QitgHHSugTXoaIY2A-VvINooaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfChISFEtcz3-D7bDj3X3zbK0eLxg_8ErXvmTNLJsrw2V6tKSy8D-CbWF7IqE9OcnIjfKOQ_6SEJvpC_JMC9GhW8hPnBvt9urwuo2JJyQLM4PXYK7vRKAy7jCFbUSkRmqaxXtA9D4s05TtRy5psUGGPlvIK3s7kFjBXmgyt_hFQFI3r-X4pzOn5G2QEG1SNTXJePMkWVgdLIl1ltXPOr3QyuFY_M_SLJ_WVYC-lSih5c94jWHieknznuLpWMosmr55E8fqUS3AR5VEI8vVmihoXdqUXNLQulZTPKwJFtn3O7uBWws1k2VxBDzBgutdXwR-7SHv1ZWrho3_YcNCf6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkCuqaHtk0hRr_KIzuBW7p8NY9m3ecBPLCs24evrzLPnyIQ-U0ZKHrgcCLbHQxYW-oGOKAVYaZi5gdrMmCNX5grVy5AOl_9SbWBg0YKrgDy1EGr3PmPpeU4GclMNfprGogW-rLPlZYOz_OGxUsUVkDzobdaBP-doKxx2PPmh4JZ0UYdmtyl3OkIOSHb_IHkYZPCLGWA7vVBSCgUFUlItnrDaPTT0O6Bf54_9yNJ46hpzX_eOxeXxFXmLqGi3MVlaXgSz2PM-x7zeq96KjCsZlucelS2M8UfmqAtJpeduUua8wMX2gM_VTO2uCDqgh-1FebZ8xvoxuFHAbRPxfRWqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnbVnuAqNwZaQuD9vaHmuYLkuvPYQeBdlmifpQ8laV1yCVoKzep7TyWZxaYvAbdZRAmIeiWNs7e3p30h0VpMl9AueI4MBSQVhtOwXMVHZvd65bh3O15bgjn0N0lcZwCl1wx3q2_lW7cJbPzy4tjUDFImkfuwvxCMxhrZN1bHtAGibjP-t8xSfYKO86SQVUPX2levO1-HU9BXMH_LO6Bqj3faAtfMIsbNczoUZpEL48ykOmPtH6Mq90BPNz_E8X2T0_rwHFo7Brs56c5pZfj3cyPhxD8zjUGPcXcPL1WKZea6mArnGxvcg1NVIWr5yKFpsP1lhwaw8EpyJ4QROJAxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqtqWSWmMTlC3pfIchimreSjvz5-Jb7iVMxH9D5mDgaQXheNHyeG4KI56O5DlFWb42P9fFhIrQcA__JhTnBNGWkoe3L0TjLBWEclGSU_4Ibr455hhID7df4cMTzSXndOwvyWdV7JqTu_pJsv8nmfzMNZBn5lxvr929zdPgE95OPFzzEGloCW2ChjIP3GMiXbSiZ2S3xw0V9O4Sf72VjZ8tohaxv8JI2x5PD_wgTsw1wEdA0KPq6yqMG3C1WU9lelRj-42vjfKONUaZoejOclvHf_-eObtGqKpA6uXJC9B4eWtOwG5cldKm3iv2gsMcnQVythhFnHiuaHTxUl61k1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O21XBnReZLULgX1K1jjaf16icnbB_qk8rt5qpqtyzd0ZK3-h6029U4M0GRkWTtNSZVpYoifL_T0mapRtfIfSzg02I-kj5-OtVuQ6MmU3HdskpoR49L1eKUSHrSA8y2rc3jm0NJ3i5AL8zEVCV43RHmBkonHOOiTSOv3UxMx6w0jwilvT0M9DHQMJTBZZ5bTDP0InvNDlmGBaPKS2qhjT187uPCcx5Cus20J6BN8p_hO4-h_Fwjcaitr6MwAIhrGeerfS0Sa8eybAlPwpXF3NTJ-ylwkBdF8NkcgIWmYgFWYzynFuDp7dblRkgqEp9m3cNKoGbUGuPTbnHtq4EXwW8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند نشانه از یک اعتیاد پنهان و خطرناک در کودکان
🔹
اگر کودک شما بدون موبایل بی‌قرار می‌شود، هنگام محدودیت عصبانی می‌شود یا مدام صفحه گوشی را چک می‌کند، این اسلایدها را تا آخر ببینید.
🔹
اتفاق خطرناکی در حال وقوع است!
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/655574" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655573">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
وزارت خزانه‌داری آمریکا روز سه‌شنبه اعلام کرد که تحریم‌های جدیدی علیه ایران اعمال کرده است.
🔹
طبق بیانیه دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک)، چهار فرد و چهار نهاد مرتبط با ایران، به فهرست تحریمی آمریکا افزوده شدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655573" target="_blank">📅 22:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655572">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqZ7-Z5ym1yNNZtvp07E7QQCtqE_5JVGoFP06gKO9_fzdn9CPXswUbjhaLTEDcKEQtd4e4Mt39SqmJgD-1G6SVps3farGIoXp4ozsP5hSziquYB6jT9G99vXNgbrzZz-rU04eK_NMtQYKg7b3WRJXQOjwHVvAa_Mml_OuUoFkAAoDQatbJaUjO_9AhLQODUla-VGAJHMBgMcpPOR2F80Ywk6SjgC3jJ6KcWrNiQZhbgZVLCYBOfU6vkQrOPGgsCMA7PITbnWHKTCSvt_Hz0_JxY0inuOSYOvwwfqY9IyDJ8AesEIx6sX-IXIMrBpXEy8woecDcPvt_rmnbmtxEP72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این علیِ جوان را نمی‌توان دوست نداشت... شجاع چون شیر، اما با وقار و صداقت و عطوفتی که شایسته‌ی سواران نامدار مسیحی بود.»توماس کارلایل، فیلسوف و مورخ اسکاتلندی، این عبارات را در ستایش امام علی (علیه‌السلام) نوشته است.
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/655572" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655571">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ0Gyrdftzy5N2k5FspN5mDRyspeqnuaecS8C6SpB0Lziwdag3W8TXpH2wPFFPIpZjTcuRS7pl32UpNiKX2g7O-onVtp95DT8rx4zb_7abHWIu4MLlAHRbcJp7Rw99peiQX2TWOFmRXWKmkImogzigUBtlcmEDHzJioOh7CxyanJjBAF963SMEWyKwF0_Z9dbJIDVfYWbwGtspsSp8u6mrv-BkWGCRPnJQj99L3Q-eAR1GqIhwenlBOnwv-RjlcQKcxtrFer9AsKJ8URYrdYWz1U28ds3X13nG-w6kyVsCFi3_uUW1NtXPkA8DkGobYXEdJyT_5knMrD9vULa-xHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ناوگان پنجم تا تردید راهبردی | خلیج فارس دیگر برای آمریکا همان منطقه سابق نیست | پایان حضور آمریکا در خلیج فارس
🔹
تحلیلگران حوزه ژئوپلیتیک معتقدند تحول مهمی در خلیج فارس در حال وقوع است؛ تغییری که تا چند سال پیش بیان آن دشوار به نظر می‌رسید: دوران حضور گسترده و پایگاه‌های نظامی پیشروی آمریکا در خاورمیانه شاید به پایان خود نزدیک شده باشد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219954</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/655571" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655570">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFkShfk2jP9hzH-Z18K7F7uQ6cyRogVz5vkE26pG6nTcmuXb_tD_liqZbMa8RB7TS57PQQ2A0aXgtQdUT2TTMIBMGlclo_MEpS-7tH0D5sMDrSYrs3xD9PNNKKRc_L31V3P24g5j1CRac3sUHwatmsGUf85Msr21X_xuZzqOjTgv1C2z08GhNLb3IHpPNj4p5T74_dbE0hKfLE2aAywziEFQQIQS-4tiwOk9t_BVrPG4dDcgr_PJcLRplL2M6-Qv-5Mb2TRgLbyqYLj93IFTIvYxSaaCDXorfMfm5LoTN8aNXaRA6TqrQFg67bc4_2feW98uGCYxoQ6MQMjoXFbmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت و ماندگار از حضور شهیدان شادمانی و تنگسیری در آیین پهلوانی و ورزش زورخانه‌ای
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/655570" target="_blank">📅 22:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655569">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0eztgqVoX8b7p_ObCO8Iy9SC_ghbA4SuRlw7A6pCxP7bGIRThYDCsBHblR72LEz6pRxxnVoiYhiSQCB5hZjyV_NBvfnpC4dS6__jcIER0M4QEhW6FYJndzY4RULnKeVeEJRaEaYTijSg2_AD9oc7Bqyg0lvH78wstXYnIoGJRmNTGgcZqD7j9fAOawYRbHNRxkvfI4gNz3ay6-youfMYEorpELgKs8kFaZorAlZ3d2HCPVLEjw_pJvnA8HyB1wJgJCfgf7V83RB3a29QYQuWwmDtnkLhPvIhBuMuBqom800Y48tmGlXl2DNvZMhLNOUCwZ00VuBx8Hw_Sp-5BTGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام که شوکه‌تان می‌کند!
🔹
آدام موسری، مدیر اینستاگرام، خبر داد که قابلیت فوق‌العاده تله‌پرامپتر از اپلیکیشن Edits به دوربین اصلی پلتفرم منتقل شده است.
🔹
یعنی هنگام ضبط ویدئو، متن از پیش آماده‌ شده درست جلوی چشمانتان اسکرول می‌شود و بدون نیاز به حفظ کردن یا تکرارهای خسته‌کننده، می‌توانید روان و حرفه‌ای صحبت کنید. ضمن اینکه امکان تنظیم سرعت حرکت متن با ریتم صحبت شما هم وجود دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/655569" target="_blank">📅 22:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655568">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZbrqHqoCqrkYEQ9oxYFdfp_TLQKLANMaVQSiFyeZkBD3HamR-WVLJRleFG4-2g_xzcUk0Tzc_7DxHR87QtCpal7kcvlaYiSUCsqsry250Ta0r6Wkzgsc9XR6JuStvrPlGmunfU5h9AqVSyvLiYxATf91w3iaCmeGjh2cK8UYv7otvZBCSaYyn76ZhuUUT73iIOzHmhXJDpDhjZKTOMitj4ac6KcezP_hSHnkdqfp9Q6S_AvOKvjc-zaaoSD4ZRSd16_3u-STLaOprc7KwetFecnBMxMBJMv9av9tqc_08jFans2c3wm_v7OtO1xnI-dn6-GrM0zXN9km31qpd4uKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برپایی بزرگ ترین شهربازی دنیا در روز غدیر تهران
بزرگ ترین شهربازی دنیا در مهمونی ده کیلومتری روز غدیر برپا خواهد شد. برای درک ابعاد این رویداد نگاهی به بزرگ‌ترین شهربازی‌های جهان بیندازیم. مثلاً خیابان اصلی «مجیک کینگدام» در دیزنی‌ورلد حدود ۱.۵ کیلومتر طول دارد، در حالی که «مهمونی ۱۰ کیلومتری غدیر» بیش از شش برابر آن است.
«مهمانی ۱۰ کیلومتری غدیر» با ده‌ها قلعهٔ بادی بزرگ، استخرهای توپ غول‌پیکر و صدها غرفهٔ متنوع، به طور همزمان میزبان میلیون‌ها خانواده از سراسر تهران و شهرهای اطراف است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/655568" target="_blank">📅 22:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655567">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قدیری‌ابیانه: نتانیاهو فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد
قدیری‌ابیانه، فعال اصول‌گرا در
#گفتگو
با خبرفوری:
🔹
جنگ آمریکا علیه ایران قطعی است و این بار گسترده‌تر از گذشته خواهد بود. هم تهاجم هوایی و دریایی، هم دریا به ساحل علیه جزایر ما و هم تلاش برای ورود آمریکایی‌ها و عوامل دشمن از راه زمینی و نیروهای چترباز و ویژه خواهد بود.
🔹
اگر این عملیات را انجام دهند، هزاران کشته و اسیر خواهند داد و این میخ آخر بر تابوت حضور آمریکایی‌ها در منطقه ما خواهد بود.
🔹
علت جنگ آمریکا علیه ایران این است که نتانیاهو علیه ترامپ آتو دارد و فیلم تجاوز ترامپ به دختربچه‌های کوچک را دارد و نتانیاهو این را اهرم فشار علیه ترامپ قرار داده تا هر کاری اسرائیل می‌خواهد، آمریکا انجام دهد.
🔹
ترامپ بین دوراهی اطاعت نکردن از نتانیاهو و انتشار اسناد و برکناری خود، یا گذشتن از جان سربازان آمریکایی و ریسک کردن برای موفقیت، مانده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/655567" target="_blank">📅 22:20 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
