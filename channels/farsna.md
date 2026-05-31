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
<img src="https://cdn4.telesco.pe/file/JI9FzIr-8Vmh9ACDwmBaOWxaVxmjYLmuTwAlJGyk1e4kYnuNgCxPMD628W1I4O12_UklTbV3aXMwllqF5zBuWOqYCxpIGubDK2bIhx-zvX8-3zz0qpyPp3pYuPpvZz10i9WJvLoCI_xPD60XIp2btMaXli7O1T4FY7Ax6HUSkrEw621PvIdDPWM5FqKw81STcUikf3LugpUrD-NYIWtjme7HvZ086pubjhiZhCzaz1CxLGNZqxf9uyoTNLfxVTwZwz6PtpYFHn1tbasOZCq9sETnaa26zhuwp20pcnn0-tLcxNmznlLRlDFd9J9YSCQ4fIYxQMepk0vQnLDSGfY-ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-438971">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3425e9770.mp4?token=DO1o6rT2fOeyjUueOpalLNj-eeyvRF4-diwsRxnMk55phSUKoR-dODZXXh65i9rHzXfrOYnUrqNe9cGxZPHgf7HN-_Y5u8833EAzg8ZSU6qpHKAF_p6t2NVAxZocGIHyEyKw4vmbAyT_QEL6GtKMfjRtUtpk6gfYALeH7GZJzeJA07WNJgwEfiV9zM4g6F-gilJYX_rSiXLHyQeIUvZ8Bwut0m4r8XfK4XXtpZ7OG0-JTZz_RpJGyunc7OB9MwJkxKerU98egazpQxU8sBt96FGDMoWWaO_ekZLcKTuBk8GTCIvGY9yQup0yT0Zn8mwRIX-WWjzHaz1SWHJyeNUAXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3425e9770.mp4?token=DO1o6rT2fOeyjUueOpalLNj-eeyvRF4-diwsRxnMk55phSUKoR-dODZXXh65i9rHzXfrOYnUrqNe9cGxZPHgf7HN-_Y5u8833EAzg8ZSU6qpHKAF_p6t2NVAxZocGIHyEyKw4vmbAyT_QEL6GtKMfjRtUtpk6gfYALeH7GZJzeJA07WNJgwEfiV9zM4g6F-gilJYX_rSiXLHyQeIUvZ8Bwut0m4r8XfK4XXtpZ7OG0-JTZz_RpJGyunc7OB9MwJkxKerU98egazpQxU8sBt96FGDMoWWaO_ekZLcKTuBk8GTCIvGY9yQup0yT0Zn8mwRIX-WWjzHaz1SWHJyeNUAXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: اگرچه از دست دادن امام شهید برایمان سخت است ولی دلگرم به مدیریت و رهبری خلف صالح ایشان هستیم
🔹
هر سال این روزها که می‌شد دل به دیدار صمیمانه و راهبردی با ایشان خوش می‌کردیم و برای یک سال تلاش و مجاهدت در سنگر قانون‌گذاری آماده می‌شدیم اما هرقدر…</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/438971" target="_blank">📅 13:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438970">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e83b13a7.mp4?token=hDU8zuu4CnWpOuv7Dzt4V3B-bi5VhWUQlblo5sZmSrDpMwyDSmwU8alacEIJQRrRU5iEs42mi6gK0aMYci_9OPdrBIPAlklrLOJWN_dbjTq5lapILZ_L2sPUHc1KLY3PmGrBbzTlgYovpzFj_-goT7HL5rHMwaGiWjAHcsdUCjmIcJFLM8fP45GukpOo9B-ZbhsvR3Prbo9jqi-13pB8YEsXa0lhBp-iw99TOEmiuAysg30u8WN-Zch0iz0lUsrEV1RZW4vfXq9S9pzGmZIxWvw7nkZWz9WI-hfnjdbLYwTd63pCXTgm9Bb131g0V5518McMZ3p_6szOukcnUMkt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e83b13a7.mp4?token=hDU8zuu4CnWpOuv7Dzt4V3B-bi5VhWUQlblo5sZmSrDpMwyDSmwU8alacEIJQRrRU5iEs42mi6gK0aMYci_9OPdrBIPAlklrLOJWN_dbjTq5lapILZ_L2sPUHc1KLY3PmGrBbzTlgYovpzFj_-goT7HL5rHMwaGiWjAHcsdUCjmIcJFLM8fP45GukpOo9B-ZbhsvR3Prbo9jqi-13pB8YEsXa0lhBp-iw99TOEmiuAysg30u8WN-Zch0iz0lUsrEV1RZW4vfXq9S9pzGmZIxWvw7nkZWz9WI-hfnjdbLYwTd63pCXTgm9Bb131g0V5518McMZ3p_6szOukcnUMkt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌مجلس: در حال عقب‌نشاندن دشمن در یک جنگ بزرگ و تاریخ‌ساز هستیم
🔹
سخنی عرض کنم خدمت ولی نعمتان خود. ملت عزیز و بزرگ ایران! شما بهتر از من می‌دانید که ما در حال عقب‌نشاندن دشمن در یک جنگ بزرگ و تاریخ‌ساز هستیم.
🔹
همان‌طور که رهبر انقلاب هم تاکید فرمودند،…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/438970" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438969">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b880b794.mp4?token=QeVj5arbkfeRnXaYMRU42HGO9xpJGp-AUzmhsQt0Ndyxtr0h04NiZlBLJ5XRkLco5jehpgiDhzkCxJUmB5z9uP4z3Vzb_Z7n7ZdzSAPMRje7Pb1e6QB4fZGa2lYfV74a54iQo58CJdBNwigMIeHyDNE-IvY88YdWIFYP5Al5TtY7qKRt4m7-lGUHxejCupMJTcObOxfxOY2F1sA-VHUvsZfi6-SQ6mbpTKqP-tD0yFiEX2cTB_m4MaseFXljVJb8eBksWYMFVZKhsKxGlPihyNCnEPhakkQbEOSfKTRc8PtemdiAGN4eddm_d8ISBfFz6GFYIXg96rwWNJRcjl3tM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b880b794.mp4?token=QeVj5arbkfeRnXaYMRU42HGO9xpJGp-AUzmhsQt0Ndyxtr0h04NiZlBLJ5XRkLco5jehpgiDhzkCxJUmB5z9uP4z3Vzb_Z7n7ZdzSAPMRje7Pb1e6QB4fZGa2lYfV74a54iQo58CJdBNwigMIeHyDNE-IvY88YdWIFYP5Al5TtY7qKRt4m7-lGUHxejCupMJTcObOxfxOY2F1sA-VHUvsZfi6-SQ6mbpTKqP-tD0yFiEX2cTB_m4MaseFXljVJb8eBksWYMFVZKhsKxGlPihyNCnEPhakkQbEOSfKTRc8PtemdiAGN4eddm_d8ISBfFz6GFYIXg96rwWNJRcjl3tM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: چک سفید امضا به کسی نمی‌دهیم
🔹
ما فراموش نمی کنیم که در شرایط کنونی کشور، دولت در میانه‌ میدان مدیریت مسائل و مشکلات ایستاده و نیاز به کمک همه از جمله مجلس دارد. توصیه‌ رهبر معظم انقلاب اسلامی نیز همچون قائد شهید، هم افزایی با دولت و سایر دستگاه‌ها…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/farsna/438969" target="_blank">📅 12:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc18d99fc.mp4?token=ncPDJrCZogJ8njm8nbuOItP-P_QOlKj1UHkRcXPr6JAR2OcNN07xcL05EHkIqLqoPHvWplVVBfVFDdLr3qc0NuOycmtFWXZmgelHf7Wn0EvyOJ2oP1p9vdAmSRR5ICbcJEpvf28j_RJKw3S2C_02W8_akqaE_U6Q5gfNaaq2qu5UhRstQ7Jl4AqsTzLGLvgd9aThMBkDXuxpm7fszQM-7Qho9guphnvN_h2Z7oMOXW1d-5HKH0E2G0cVJHpWc0GStpb2OzPDL28AllTdEz8KcG4BTN-_9V___lAkvSGe3ocOLea_H4EOUdgoX2V_wikM3Ydq9Sg45AthU0A20Y6a_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc18d99fc.mp4?token=ncPDJrCZogJ8njm8nbuOItP-P_QOlKj1UHkRcXPr6JAR2OcNN07xcL05EHkIqLqoPHvWplVVBfVFDdLr3qc0NuOycmtFWXZmgelHf7Wn0EvyOJ2oP1p9vdAmSRR5ICbcJEpvf28j_RJKw3S2C_02W8_akqaE_U6Q5gfNaaq2qu5UhRstQ7Jl4AqsTzLGLvgd9aThMBkDXuxpm7fszQM-7Qho9guphnvN_h2Z7oMOXW1d-5HKH0E2G0cVJHpWc0GStpb2OzPDL28AllTdEz8KcG4BTN-_9V___lAkvSGe3ocOLea_H4EOUdgoX2V_wikM3Ydq9Sg45AthU0A20Y6a_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌ مجلس: اصلاح برنامه‌ هفتم با تمرکز بر بازسازی خسارات جنگ در دستور کار کمیسیون‌های تخصصی قرار گیرد
🔹
توجه دادن مجلس به مسائل پساجنگ توسط رهبر معظم انقلاب حاکی از دقت نظر ایشان به شرایط سخت پیش روی کشور است.
🔹
از همۀ‌ ‌کمیسیون‌های‌ تخصصی ‌مرتبط مجلس ‌می‌خواهم…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/438968" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438967">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVRrD7hbMQBXcgW8cKbsEZn7uBtcTxp2CT4YPeFYbESLHoAUymWFz4gyuFRcy1MqWDGR7I2udTyKQLKYOTq08aH3djlCTtnKc9o4XuBg4Pv8iXPfwcxFfQ5kcZ8V2F2X9E7LDGyxm7oCTf0bxAbPCBs4a84vqfESSOUDuzXD9qQKHNZokpGbqusbwovD0_mmlCtAr0vTBWnyToLu_PaFRmuJPcLjJT1jbJHNFWhJpHwPBNjtdO_-v2dkUJaz8q2kIMfoexP3N3GVI63Dz4IXe1KKigC3OLUL4CtOLWXKZuL_CRDdKKwlWOgpotlyRQpcPRNG7AZj4br70Fs2l6sJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعضای تیم‌ ملی امید برای برپایی اردوی ۱۲ روزه راهی آنتالیای ترکیه شدند
@Farsna</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/farsna/438967" target="_blank">📅 12:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ad04a2d9.mp4?token=Wmzu_RFp_xzLDnS14nc0OpnjEReyRaHlGXN_-7AWqETveHGsZlAaOA6e0gB_0zdAs1UxG2aT-G519OENxSpAEE_IoHFVA078uc2wWkYgpi7H10uWoS9O663IXfSVKWHsL1xAfAa-luE30u7mZEWC9wsENH0mYrumSygIVxGv9PrOJZ_njbod3PDFevVexaF6_LblvxI6bPb5wKPBsjsei1ls3FGfqTouXuRCotWZyIAoW2LfBK80DvnMapVQ_76XlmUSx1KToUhJDl0fWAvej1OBfUstSPspVDVrvf2AJlLf-5R62PEqaX35YuOwW-f60UNqe3K9RURagne7NzfZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ad04a2d9.mp4?token=Wmzu_RFp_xzLDnS14nc0OpnjEReyRaHlGXN_-7AWqETveHGsZlAaOA6e0gB_0zdAs1UxG2aT-G519OENxSpAEE_IoHFVA078uc2wWkYgpi7H10uWoS9O663IXfSVKWHsL1xAfAa-luE30u7mZEWC9wsENH0mYrumSygIVxGv9PrOJZ_njbod3PDFevVexaF6_LblvxI6bPb5wKPBsjsei1ls3FGfqTouXuRCotWZyIAoW2LfBK80DvnMapVQ_76XlmUSx1KToUhJDl0fWAvej1OBfUstSPspVDVrvf2AJlLf-5R62PEqaX35YuOwW-f60UNqe3K9RURagne7NzfZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رهبر شهید جانفدای ایران شد
🔹
رهبر شهید، پایه‌گذار ایران قوی و مستقل شد. رهبر شهید به ما آموخت مقابل زورگویی با مشت‌های گره کرده تا آخرین قطرۀ‌ خون مبارزه کنیم.
🔹
رهبری که ما خود را جان‌فدایش می‌دانستیم، جانفدای ایران شد.  @Farsna</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/438966" target="_blank">📅 12:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f357f1c9.mp4?token=JeCNbVzm9U77CNbwJoKp8nIP5R_ZtKd25GPjWE0_BvKP8GyQOj3hmJlDreSFcq4rilrEFXEZmYb0bk2_BC9Naw_3BnvD85zHV0xvLun2kMeFuSBv1lNKERthcyEXIojct_STj32F8giJedhdFsEBfr07daVY3S8FZbpZVtQUCL60_w9ABMNJ3ec7NyBf6JEbqFQUNVRBHk6Ycd_6hnBiCw4lDVUg0a0vCHYWCCOisipCeAIbLLYCM93DcROXH_atLt3JZTTItbfAT0v4K-7Fc_JwryAmlNcIp2uvHbjJmBanbja6hwUhgeah1VvaU4lryfT6E0HS5Hb9yS6vqE_BcqJK1lN2XrVCFTGU0jSouDEjjD-Mj6F8xEfw7VHdyxr9l7J5gGkV3CxY5jCqhgNq3kx7clnzzID4ku7S6F3bbYyG4UgUZe1c6zgxIQRlnyHgl18HXPxyicLZL_WE9IwEl9MfR-N0VOQ1lQW5dkEd0A33OniLNDH301SoKli5Rb4x0K1HFotTr5UKyMsupQxn0XLHNuJJHIIvp1v-64SsFUlPQ3V3tI7wVNqZ20d-gB_o_HfrIuhuOSyyubOd9Itwx0rETglYTZFVmnkE-1HhfSjkyXQqlDRHxkS0DE-mFrxbyryx-V7HwBkZJVXmJva3Mshu2wjd3kFAt5lWY71vk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f357f1c9.mp4?token=JeCNbVzm9U77CNbwJoKp8nIP5R_ZtKd25GPjWE0_BvKP8GyQOj3hmJlDreSFcq4rilrEFXEZmYb0bk2_BC9Naw_3BnvD85zHV0xvLun2kMeFuSBv1lNKERthcyEXIojct_STj32F8giJedhdFsEBfr07daVY3S8FZbpZVtQUCL60_w9ABMNJ3ec7NyBf6JEbqFQUNVRBHk6Ycd_6hnBiCw4lDVUg0a0vCHYWCCOisipCeAIbLLYCM93DcROXH_atLt3JZTTItbfAT0v4K-7Fc_JwryAmlNcIp2uvHbjJmBanbja6hwUhgeah1VvaU4lryfT6E0HS5Hb9yS6vqE_BcqJK1lN2XrVCFTGU0jSouDEjjD-Mj6F8xEfw7VHdyxr9l7J5gGkV3CxY5jCqhgNq3kx7clnzzID4ku7S6F3bbYyG4UgUZe1c6zgxIQRlnyHgl18HXPxyicLZL_WE9IwEl9MfR-N0VOQ1lQW5dkEd0A33OniLNDH301SoKli5Rb4x0K1HFotTr5UKyMsupQxn0XLHNuJJHIIvp1v-64SsFUlPQ3V3tI7wVNqZ20d-gB_o_HfrIuhuOSyyubOd9Itwx0rETglYTZFVmnkE-1HhfSjkyXQqlDRHxkS0DE-mFrxbyryx-V7HwBkZJVXmJva3Mshu2wjd3kFAt5lWY71vk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: از پیام راهبردی و دلگرم‌کنندۀ رهبر معظم انقلاب به نمایندگان مجلس تقدیر و تشکر می‌کنم
🔹
پیام رهبر انقلاب را نقشۀ راه مجلس دوازدهم می‌دانیم. تلاش می‌کنیم اقدامات مجلس بر امیدآفرینی و آینده‌سازی از طریق ترسیم مسیر باثبات در اقتصاد و معیشت مردم تمرکز…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/438965" target="_blank">📅 12:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c566d07f9.mp4?token=pNqoDVyPR0y_rgBbs2_DofDVIP1PbXJhYqZvBuu2g1ZCtFb0zGrhThUnjQOcJUk2hz9cWdO7Hn7yAkDD1T7Qg0vKZPiCB1C37Pfju5sfiOBHo6_GOekwnaexvqJrDDpIwyJxvdcy_ms-2hV1WxDAZi8X2-ghKzGZnJwCzBD_fD_5DgtO---yAgQkXsxZvSuZpwqDT7TiXlykYHsNTM3EwtQacwW3ClljaFbLJ1sVYmuhBz74c8OVZT6AQ_4wWPIbh1EEc780db4C6MwyKVIJLWer3RhBJuXw6TCw0tdSz37RL1KM1rZvjc6pMUAei12PHNqlZKqNKb11M2Plp_P3A6Yx0U-BIlgr64tik3y2Gs2JoHP0I-KCc3udTRQVYTasK3DBMMy4e3UjVZwXgMo7GS85U_LmBTWzA7RWHbIjgiOzOW4PzRZpjlQBVieiWG1JJMmrQbazrKed5B9sLf_xIXgBSxdW8gVpMx3AxcMPnhtHCrt4SXDTQYSHDR6PsuMqRY0VYyrbqd5KcI7EvyZtBXfm-zYYLNlXENEMIJeapEf2FyyP3SvwnSh45xZQ64NKC3xAfZRaSN30HAgd0_qDLZ0-r0Gpw1_28StSIro9rx9uUNBgnpRMqrBw5q2kW-ylqAa4el1ZpWgOho_trmXjOY97e3DRAlEZZvQ62QkJWuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c566d07f9.mp4?token=pNqoDVyPR0y_rgBbs2_DofDVIP1PbXJhYqZvBuu2g1ZCtFb0zGrhThUnjQOcJUk2hz9cWdO7Hn7yAkDD1T7Qg0vKZPiCB1C37Pfju5sfiOBHo6_GOekwnaexvqJrDDpIwyJxvdcy_ms-2hV1WxDAZi8X2-ghKzGZnJwCzBD_fD_5DgtO---yAgQkXsxZvSuZpwqDT7TiXlykYHsNTM3EwtQacwW3ClljaFbLJ1sVYmuhBz74c8OVZT6AQ_4wWPIbh1EEc780db4C6MwyKVIJLWer3RhBJuXw6TCw0tdSz37RL1KM1rZvjc6pMUAei12PHNqlZKqNKb11M2Plp_P3A6Yx0U-BIlgr64tik3y2Gs2JoHP0I-KCc3udTRQVYTasK3DBMMy4e3UjVZwXgMo7GS85U_LmBTWzA7RWHbIjgiOzOW4PzRZpjlQBVieiWG1JJMmrQbazrKed5B9sLf_xIXgBSxdW8gVpMx3AxcMPnhtHCrt4SXDTQYSHDR6PsuMqRY0VYyrbqd5KcI7EvyZtBXfm-zYYLNlXENEMIJeapEf2FyyP3SvwnSh45xZQ64NKC3xAfZRaSN30HAgd0_qDLZ0-r0Gpw1_28StSIro9rx9uUNBgnpRMqrBw5q2kW-ylqAa4el1ZpWgOho_trmXjOY97e3DRAlEZZvQ62QkJWuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگند اعضای هیئت‌رئیسۀ جدید مجلس با حضور ۲۰۱ نماینده به‌صورت مجازی و حضوری  @Farsna</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farsna/438964" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
سخنگوی شهرداری تهران: فقط اتوبوس‌های BRT و مترو رایگان است
🔹
اتوبوس‌های بخش خصوصی در طرح حمل‌ونقل عمومی رایگان نیستند.  @Farsna</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/438963" target="_blank">📅 12:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0w4umw2MP7Cn-1iJ3Hjr6MiPyTscBKNRl7edtZfnlfQZOgSg-j3T3lZcB0onHKNV_nHnvyYbnP5rlsRNaNoSO-ZThNKkev0rzfzo8Uhqi6UkzqKs5I-0Jlyr9ODthZSxZ8zqVxUTFly7fLD8NbNeTW9SfBExU5boI8WxilcaGKrAkNkLw-K3fubCz1fpukfIf47Zfrp0J6OQLw6K9k-yW2oazxddjEw2oEANkzTvZvxT6zTW4aKooNdfMX2gRmkzh_oTS9aCnKlmMceScLBVhByx3mU_0HqZia731IrF-5PL2YrVlkuOOPVoIBp_69vYpkcBP3Jexq5SMK3QG9ecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای حملهٔ پهپادی در نزدیکی نهاریا در شمال فلسطین اشغالی فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/farsna/438962" target="_blank">📅 12:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5536fea9.mp4?token=Ya5Lggv0MoMTff6_DiGdqogrdmjc0Vjq0SQn4D6-nrs7Qs6s1tnM081I829EbJLd-N2QFkIzJj7C_OWDUVLXUgqGbH4rM_V1rFKy6UYX32LpYz92d4TMAsh8AXp5ugQyoNk7vI-15mPwkg_48LVehEQ6MFSzbSTS4GLmGX-7VQ97XInT5Vxi3fjqK_2g4o8ruI75t_Zz57eJJAPHhMbggG3yOw5pqj6SLLOdFmoN-V0MbRw0DEXq8RxZdo-jfPIyB1M_buuDgETAqzCTIKHdE8qRjzeb9zYsE8P7TKBxJDztrhNL3LDanb4FxbujFPggkQPMlnf0DbiI0Rg2i0hnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5536fea9.mp4?token=Ya5Lggv0MoMTff6_DiGdqogrdmjc0Vjq0SQn4D6-nrs7Qs6s1tnM081I829EbJLd-N2QFkIzJj7C_OWDUVLXUgqGbH4rM_V1rFKy6UYX32LpYz92d4TMAsh8AXp5ugQyoNk7vI-15mPwkg_48LVehEQ6MFSzbSTS4GLmGX-7VQ97XInT5Vxi3fjqK_2g4o8ruI75t_Zz57eJJAPHhMbggG3yOw5pqj6SLLOdFmoN-V0MbRw0DEXq8RxZdo-jfPIyB1M_buuDgETAqzCTIKHdE8qRjzeb9zYsE8P7TKBxJDztrhNL3LDanb4FxbujFPggkQPMlnf0DbiI0Rg2i0hnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات اولیۀ حملۀ رژیم صهیونی-آمریکایی به مناطق مسکونی لامرد
🔹
در حملۀ رژیم صهیونی-آمریکایی به چند واحد مسکونی و یک سالن ورزشی در شهرستان لامرد در استان فارس ۲۱ نفر به شهادت رسیدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/438961" target="_blank">📅 12:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
عبور ۲۸ کشتی از تنگۀ هرمز با هماهنگی سپاه
🔹
روابط‌عمومی نیروی دریایی سپاه: طی شبانه‌روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینر بر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🔹
کنترل هوشمند تنگه هرمز به‌طور مستمر و با صلابت و اقتدار در حال انجام است.
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/438960" target="_blank">📅 11:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqqGlQYrrqQHVIhuWlXqJKyKVvM69g4lbUYQcEJLQxq7tNG4Jwccqes6tktjk8o0yeXXOxQlpNpw-eRe8Amh2oCxZYUsI2AFGKSfuAAeEu3bWRqg8vC8TYSgxfPf6G3CJtAoq3M4HOHUkv_YajVFnSn-2zP_wiBui5U-cKqHmno0TNsH01XY5DD9dPTJ6cb_eDLDez2YlMb0X7piFbVJIzHHBF_EZK20EEgiEKZJZ67xSEdwyGClNoMJMxO5MyaedeiAgTnyFlWpMqf8p9vBnyWziJHkb8KQO8XWpULFUo8evTwQcEmMb_b-GVdZQYo9SItFQo6fHI4LOiS_YoRSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7hmKmO-NrXbnBcM4zglO2JB-CErcyuv8oxzHIodVZgRBQyyfFRgAw1TGDmw-YrInLeZR-2-t8OudWGOnFadvvePpNqqvGoeKRl1btU3yA1kpjdhhsi4K7U_m-mP1QvM2j-S92s8hQrvUe_eol2AGbQ2iIp04LUDmf5b6s-WucEAEqCvorEeEXGPeEXRzcBhPPO5rmGWiLgA3yZpNNP6wJo1JmrSjAm7JhxlGlFW4j3-bSieStcqolBFTddsGEvoK87-if4DEwCcOpAOZDvrhVBT2eoUHIYlZVARnJKaWWL4gfJR76cxpwotfxDJjEw7xtUkpOpJUyzyQ_VnFtCC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAO3KOgtKHy5f_H8P7ofhM90mt1259M6XjSXhZyv0FlCisveWH-i2Oli4CKPjXJuAcTRXQQBfwPuXMZ0rp4qLymUNXH4cJPRqw1f9m2e8EqxWCDREQNQSgdLe7Rm7W5YJK8mi-HRe3oyk_pDnVXQbko_wqNTpH15_6UV7Jdt4_ALQWtjXMc8L1Xf_W8qQnPsX2IlqqagaFbkCj2hbXa7ZVsDY6mWoZRnAMEsmEs38tRfDEw0HupJXTooztTiRoQu_U4gieXMEcz2TUsDYuoqgr_fr0CrqcOnkwazW32jyp_fAb3ezElfbMzoQbojPfqLwJbrXeU1cF-ASIAf4RxQxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4652b1decb.mp4?token=FiRjltehSNmMSGZCypp6NNhzpRwBsXCV2hsWaFPF-E0KxeDl86p_rWwgy_XG5nNR7tKb4-CGkp-_VaWqXyhhK-LAEcDyXgUgr_BpucvNx34_sUrMzqztIDWUO_FJm11sJlE2Cl1VH-9ADSFhXoipz0nbUO1satt1z-lvGZsSj72tAp927pFvtWXBye6jDjHZMnFIJhigXFelXYplrt9VowYQDFm4iTVRmAusXDbopTstUdfNwxJq5LF80sHkZd8gSdca10_8cDcVQXXg_qHl4yB7rkNGkBncx8LmbxCD8riAcVvMwpZspMX1lz20F7JPjDMWkwdIM5Hbn9dK4oZ45w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4652b1decb.mp4?token=FiRjltehSNmMSGZCypp6NNhzpRwBsXCV2hsWaFPF-E0KxeDl86p_rWwgy_XG5nNR7tKb4-CGkp-_VaWqXyhhK-LAEcDyXgUgr_BpucvNx34_sUrMzqztIDWUO_FJm11sJlE2Cl1VH-9ADSFhXoipz0nbUO1satt1z-lvGZsSj72tAp927pFvtWXBye6jDjHZMnFIJhigXFelXYplrt9VowYQDFm4iTVRmAusXDbopTstUdfNwxJq5LF80sHkZd8gSdca10_8cDcVQXXg_qHl4yB7rkNGkBncx8LmbxCD8riAcVvMwpZspMX1lz20F7JPjDMWkwdIM5Hbn9dK4oZ45w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما ایرانی هستید؟
🔹
«ایران سلام... سلام ایران...» صدایی از میان جمعیت مسجدالحرام مرا متوقف کرد، برگشتم. مردی که چند متر آن‌طرف‌تر ایستاده بود، با دست اشاره می‌کرد.
🔹
خودش را به من رساند و قبل از هر چیز پرسید: «ایران خوب است؟» گفتم: «الحمدلله، خوب است.» لبخندی زد. انگار منتظر شنیدن همین جمله بود. دعایی زیر لب خواند، مرا در آغوش گرفت و در میان جمعیت ناپدید شد.
🔹
گاهی فقط گفتن دو کلمه کافی بود «من ایرانی‌ام». پس از آن زائری از کشوری دیگر سراغ اوضاع ایران را می‌گرفت، بانویی از الجزایر برای پیروزی ایران در برابر آمریکا و رژیم صهیونیستی دعا می‌کرد.
🔹
زائری از اندونزی درخواست عکس یادگاری داشت و مسلمانی از فلسطین، یمن یا حتی چین و فرانسه با شوق دست در گردن زائر ایرانی می‌انداخت.
🔹
این روزها که مناسک حج به پایان رسیده و  ۳۰ هزار حاجی ایرانی در مکه هستند، هر کدام از حجاج روایت‌های مشابهی از این سفر دارند که وجه مشترک همه یک چیز یعنی توجه ویژه زائران کشورهای مختلف به ایران و ایرانی‌هاست.
🔗
روایت‌ حاجیان را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/438956" target="_blank">📅 11:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d7616810.mp4?token=ZOypN5qiy1S2hRKoI0I3Po0cgjduvJ67NLaV-Hp2BK2KFb47-QOHzz6h1gdeZcla-7LzrvfID58sT-vgN3s0wPM-djEObo4Tfy2-GbIiMOpEOJPCGAzY_rI7oRLXfh6MX5o2y2mU2M3lcSngDr0UiRuv7ZyDg3cn4_YRV-KLKseOV70aXK7LgjOinIeno6UCG9sR5Xp064P5xcM3bbKOllgovLM5kTMLLLUwpgKGzBT1dyNwj1Zin_2ebNhcJ67GFZYQ7-UqV6TKLhxcNm-bKVyKWvjh7lT0WrsjHaYYmYW0JctCy_qCKVA9W9nPwPYBEhi-MsgVUGYe985HOGFvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d7616810.mp4?token=ZOypN5qiy1S2hRKoI0I3Po0cgjduvJ67NLaV-Hp2BK2KFb47-QOHzz6h1gdeZcla-7LzrvfID58sT-vgN3s0wPM-djEObo4Tfy2-GbIiMOpEOJPCGAzY_rI7oRLXfh6MX5o2y2mU2M3lcSngDr0UiRuv7ZyDg3cn4_YRV-KLKseOV70aXK7LgjOinIeno6UCG9sR5Xp064P5xcM3bbKOllgovLM5kTMLLLUwpgKGzBT1dyNwj1Zin_2ebNhcJ67GFZYQ7-UqV6TKLhxcNm-bKVyKWvjh7lT0WrsjHaYYmYW0JctCy_qCKVA9W9nPwPYBEhi-MsgVUGYe985HOGFvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای جدید هیئت‌رئیسۀ مجلس سوگند یاد کردند
🔹
جلسۀ مجازی صحن مجلس به ریاست قالیباف و مشارکت برخط ۱۸۷ نماینده و ۱۴ نماینده به‌صورت حضوری برگزار شد.
🔹
در این جلسه که اولین جلسۀ سومین سال مجلس دوازدهم بود، اعضای جدید هیئت‌رئیسه سوگند یاد کردند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/438955" target="_blank">📅 11:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438951">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roxUznvAdYggtnnZMadmgwvzcjq3VwuDJPly8fxkQ1AWjkQEzS68weGzYeR222C_rGpxV9kNLtU2nydgpT-qeOoyddLVSGNkl9F84G-gGbLbXyDkOgRW26uSy1K4CNreM0E0ByquBCdvX0UvkDSb0eVVVFWUazWspQTfX1m_3UTcfbPGHhqJjHG0x73krllKhCOikT1l2l77vyPxBcZsPJVc7ivjYqMjv3lKXk7xS_7qRlZRuTVPAglhbjIk9Ry5u26lpIqm5zwag3e4hHs2MYgb6tQ41ENAFx5X0tu7_ra1QwibdllEvHswyVGYuQcVBzzFjx7sbS_hM1QufD3llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlzaT6YgFpqVgZqEH5oA_fKj5UZWep9Sfzxw4NyMcHE4XOu8l2rphzFoaRxCVJIEArPxQ3ktqjLiSOCecYS3lPQAl53QG-GZsSjtTMXCn4V5MeLAI8ML8n3QykMyhzbzo7J1tXjGM61X21TJoZUeGCFZIwXH5CDzILegNHOvWcg8CRt5NdeU1bQHXd8uYoILEUxtT0dffjw5XVe9T-V-t7dvFejY7IrBtmBflug0jhnicuxcubHdcEyTsT1b7CS4oCAjpnjX28kKQ1TOr1T65LdkisQZDeDSMakkTWoxLZ3MsDX8emMyJiUdIiVmT8QosEMwH1ZdtPWr19X_6s14mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVRDt8KElLTTCTFnbYgo5KAKtlDLTuJzCXScFM6oNFSazdxnQ3OsNodT6Lh6sWTCW7n2R8cLABYrEZ8isx9sntGutzbwwyLGmkgPFvMaZWenkEUNAqA2tigjJF-mmFqyxtOTa9g92Nk21YWB5eDiMpdDZMUedFwiM_Smr_nnYdWeWMfM-frbZaaO1iiXTdkyseY-2eYBhoc0i-YStrdXFgM79_F6K8Mho2gXKVh4gecrZMApObl1Y7y_Xz_7g2xKZa70TSPuXHbIcEyQH-WNTFakhGZyl5UtjGu4o6noib60fqkB8T8rouj9utCkYZXlrPPLGI6-yJjELPIT_WjotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Il7Pn5zou5cdfIbyE09bLE30nwapQrxxPOCxdCYARFZDYxG4ju_x5U7D7oWxLkC4RXCNl5Qx5EZNG-tzm2T6cHu50TWYWm5dJOZMn339jBRJpbv0gb3rQ9-Tjg-QEETjP0xSlA5nDQN1S27QIeMjq4qHceKaDsAgMpwbUqfWaxEE1YhlpxTV5muJG7dl68nqbEqksouwqSef76KaP6DQUPi1o6qBspUezelKIkldjATgu-pkTZFNlxsn0TRfFIEI0XN6x-M2isrhKEK060QRfn9R1gPW238A4FiCXobsuD3wJlT0sBockHPAfJo6OP7jgYAVoHZrJUvLO17GDi88Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دانشگاه نباید صرفاً محل انتقال دانش باشد
🔹
دانشگاه نباید صرفاً محل آموزش و انتقال دانش باشد، بلکه باید به نهادی اثرگذار در فرآیند توسعه و حل مسائل کشور تبدیل شود.
🔹
امروز تعداد قابل توجهی از مراکز دانشگاهی با خروجی محدود یا فاقد اثربخشی متناسب با مأموریت خود مواجه هستند.
🔹
در چنین شرایطی ضروری است نظام ارزیابی و تخصیص منابع بر پایه عملکرد واقعی، خروجی‌های علمی، میزان اثرگذاری و تحقق مأموریت‌ها بازطراحی شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/438951" target="_blank">📅 11:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438950">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2e779489.mp4?token=s7fuqAF72zL8-R2pqFON0rGe5R8IckAggGFbPezBDpnAhdTwxZybmsMigJ_qV-Bhm6wawFBo_6jN0rBI302E1cy3PVWAqpd_fV1Fbj1JHdNXSiu6DL3YwCM22EYZtZiU60uru7maXfIMJxRjM3zATLMzsekUUw9gBYvwopusaPjvbs725ttidBrew1JZnzs4LuuYBAxcMj8cgyqRg3b3fTi0btrDoTOZqSqF9K2uPeSVXd6PCSbO1z7Su8a732DXG6edQ0VIS49b-hezUFgTfbnOott2DWrdfYXpi7610bN1NMRHCxrXbFWeTPAT8EpRN5YoaHSp5Y-_41CXk49z8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2e779489.mp4?token=s7fuqAF72zL8-R2pqFON0rGe5R8IckAggGFbPezBDpnAhdTwxZybmsMigJ_qV-Bhm6wawFBo_6jN0rBI302E1cy3PVWAqpd_fV1Fbj1JHdNXSiu6DL3YwCM22EYZtZiU60uru7maXfIMJxRjM3zATLMzsekUUw9gBYvwopusaPjvbs725ttidBrew1JZnzs4LuuYBAxcMj8cgyqRg3b3fTi0btrDoTOZqSqF9K2uPeSVXd6PCSbO1z7Su8a732DXG6edQ0VIS49b-hezUFgTfbnOott2DWrdfYXpi7610bN1NMRHCxrXbFWeTPAT8EpRN5YoaHSp5Y-_41CXk49z8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پاک، خبرنگار مستقر در بیروت: اسرائیل خیز بلندی برای اشغال نبطیه برداشته و در ۵ محور در حال تلاش برای نفوذ به شهر است.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/438950" target="_blank">📅 11:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQ1bB3BdlxgeaMDzmw_oXBmtXvWZwsg6WFdYROjZOH3d22T2GBZs8dHUHL2pFg-Inf8B3n0CUS62zSHEu6o-Yd_akPm9bs-ySLVD5vS8e8NGqELUWCMtvIKF0IN_hAQHSUaRBdyAWpnf_3Y5bwyXJuPjV8sotouTCxRzrJqFoomNxibyCfCLyToDH9BweovxnMRMWrOh192UlhY69qZQUFvypKOsGpeqNky3XHH_z2m3yoCVwFzTbefckZ5IhHgnDUfgxQ-IMUqiRkgji4y95k0y2Hbk3WjAKsfF5yEQMV-9g-Ha4uifJUEYUdsXzXSX8viGuhjcQBMIfASTuvxFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DelckAlV2SK37HJB4CzRKDRVAQuvNmbGAeVrFzGj5nDY5WiJ5X5gE0OjaTDE32XcqVFq5Br27Rp56STCbC3YHKOf1rdIpEsiUq5IjqSdnUdjWI1gtlb-9IKhPmqILAgWh8LMl20_cXtBkTtDbQyBiDMMnyDiOXTJe4X0eWQcLxiHgnhcYqie8XDKFjqziPISwSLrkGEsAdRkK_NisKP_6ZOPmuHbBrQR4vsxak-YiSDjQQxy2KKdGGncCmYDVZGV8JliELkpvwy8kjeADIBymnuWkza-ee7BesqAPKbOt6oa7cYTdps56-VsRxs3MJGJ0DowT8XpEL1hDaja0LdWLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتخابات هیئت‌رئیسۀ مجلس به روایت تصویر  @Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/438948" target="_blank">📅 11:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438946">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
داستان‌های ناشنیده از زندگی جنگ‌زده‌ها در هتل
🔹
مجموعه مستند «پشت جبهه» قرار است ناداستان‌هایی از جنگ رمضان را روایت کند و دستگاه‌ها و مشاغل مختلف از خاطرات‌شان و مواجهه‌شان با جنگ بگویند.
🔹
در این قسمت به سراغ «هتل هما» رفته‌ایم، جایی که مردم جنگ‌زده را در هتلی پنج ستاره اسکان داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/438946" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438945">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac478d7f61.mp4?token=BF0xXICqa9_5tGnA3nUCN_LvZy4yZDAsRCM_uxXEHwnPzhe5XqN7_2gafBBK2wVEELXDnOi4QewM2AZNvHQiX6rw35dx2RBfaa9LPccLSoNtmIr_LGfOFkg_gErmK7r6pJMqY1uMcKZVVXD7Qz04Gkm2N6ucmNFuWHh3BWU6o8bYOXHklYwXqkIuxwtsrmGLivEO9eA1uIRzr-7M0rm80FLTjxuCuoCqNmzGi6-AYqO3itqampucOOtyIbZ9okwkEE-McuG7EZOLk3jKzy_YYVMOIY-MsVYF3L0Lwba_Eoc7MdxtzMPpCvwrcoYk_qmvxTPZLfW_UZpstpcPNm_Lfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac478d7f61.mp4?token=BF0xXICqa9_5tGnA3nUCN_LvZy4yZDAsRCM_uxXEHwnPzhe5XqN7_2gafBBK2wVEELXDnOi4QewM2AZNvHQiX6rw35dx2RBfaa9LPccLSoNtmIr_LGfOFkg_gErmK7r6pJMqY1uMcKZVVXD7Qz04Gkm2N6ucmNFuWHh3BWU6o8bYOXHklYwXqkIuxwtsrmGLivEO9eA1uIRzr-7M0rm80FLTjxuCuoCqNmzGi6-AYqO3itqampucOOtyIbZ9okwkEE-McuG7EZOLk3jKzy_YYVMOIY-MsVYF3L0Lwba_Eoc7MdxtzMPpCvwrcoYk_qmvxTPZLfW_UZpstpcPNm_Lfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت عضو سابق حزب ارادۀ ملت از دلایل جدایی از جریان اصلاحات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/438945" target="_blank">📅 10:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf9f3f6bb.mp4?token=Ayqwv38o_WONsnmr2sMAENhApDLnuuAayUoX90Z_9Y98BlhX4MXEJND3rxsxTkqhBsXZtXtaaZjRwtmyPLXi-oy_yqGYRCBpgESIgmHw1IyS_bzcqxSjJE5gMcxK3gqBpOnxmknsF-_yVwZyxpsexj8DqHlHGhZwLh6KB1U39QoiMurIJGaekM13a0IfR8IiLChwRGIbNNMSfeszD6o8TiuHWj9JQ5HVx6aGPETMzOW4HMswKjoiogNvb2CWz6jhOcoMa9Q8_oRHEXp704OXaqptidXLp6Xt5ocwmv8COYg2P-3aAwZkULHsyg2W8xxyDOf_D4NwjA7V-xdjM4-NjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf9f3f6bb.mp4?token=Ayqwv38o_WONsnmr2sMAENhApDLnuuAayUoX90Z_9Y98BlhX4MXEJND3rxsxTkqhBsXZtXtaaZjRwtmyPLXi-oy_yqGYRCBpgESIgmHw1IyS_bzcqxSjJE5gMcxK3gqBpOnxmknsF-_yVwZyxpsexj8DqHlHGhZwLh6KB1U39QoiMurIJGaekM13a0IfR8IiLChwRGIbNNMSfeszD6o8TiuHWj9JQ5HVx6aGPETMzOW4HMswKjoiogNvb2CWz6jhOcoMa9Q8_oRHEXp704OXaqptidXLp6Xt5ocwmv8COYg2P-3aAwZkULHsyg2W8xxyDOf_D4NwjA7V-xdjM4-NjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض‌گویی تازهٔ ترامپ دربارهٔ ایران
🔹
درحالی‌که رئیس‌جمهور آمریکا در بخشی از مصاحبه‌اش گفت «ما ارتش ایران را به حال خود رها کرده‌ایم»، لحظاتی بعد مدعی شد که «آنها ارتشی ندارند؛ ارتش آنها را نابود کرده‌ایم».
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/438943" target="_blank">📅 10:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j95E8w4iZb3xWVAYq1jKz09jfszMf4yzqth00frqKfPzmgDqijcJ8AwUKwqkz6p43Q2ehYyphxFwWIpyYDNQBGGdvRsymhPtKMeGWskZTQwBFBB5C9WCXz5v2sgToE-mLFZgAOuMj7Y95_BX9QVz_2qtK2Nt1ufceJrQUtQ9x1RmcoHpNvEUjvC9Sqx9uKPPEyFQ7jxMvARkkqGXI0Qa2cF0UjSyTFy21cKcXCKIIxp6FeJ45ESRdiKkUjmtUFuFizeQDNqPi78dlPihLuTpVVq3LJnl9IuRWO46Omvn3EksXKRkyeYt98cm061G8mGtPag5UxJVcN_kyPWdsjy_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VULDxH2pt3Y9bdUCLur4O_PytaNl4DBRif5GLKAXWsfdV49dz6Ik7fIJ6rL5h5f-Gmlw8xLl_lbX5X41lUerANEpQ_IvuOWCMz6j4A7om-H0I2pcfxOLbkKXwJ9y43DG04s_zrsYxfDa19sx55kyQcPitDlu_046s4DOkMm2u4KUcXaXW8tLhCcQ5q0eZvWP5Lj14YUCK_km9aokPLxzZcZnCdlLGnEG6CrDWIl6Lf6vUBFxoxyP3XhMqKWaoV4eFNf9P3A-6uj-e6uhGoKVFA-6lqFg8zTudzU4rHCHKV5hT1B_h09lAP9-65dGeBmvWhUVcK3Dofrq2kFpZNDJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JvS_FKsHBuKzCcRyoh05SMsB0szmg3Up_rLJaykZZFo8o2pEpdFFzEjNIgCKmTS_b4T0qMVHu9OTbKKAjsvdum1Z4-WlTPpeFrXomqjCOO7J--msj0CykIwTpv7ya4QweS5N1kpuJEiyhzAl8mCLQVMimwGzbxGKpDJCW3a5M-t-6Xl0UAVoJbosbAGWTWn8uowY9WyHJrhcf_wyE92eEixc91L8VNznrzp1Vwh_Z70cFM6sHUpo42t4jpPYmb1B3BYWB0bGud05c1yg9OiLH3gQiLoMi9Q6M52OUADfl8xoyFCVyddVGiR9uPrXIDFq3HWlSKtNAfDVAszFCf6GUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JeU_0bT4voTAvOc3oY9UpheLjBbqSxOqW4L_HO-VMmD51DDtcEtlbvlG5QdIlxGbiII6bt3u8LCU5TJhvPKrubSFVmlQtq2bd4OUB7t9a-w213uVk4arFvKYT8tgg8wNsd7nhEkPn47phcdVw4-8hKwrTKe13p4IwD1RqwEAC2L6HXsEzDY6c2dTLx0P-VlPEJQkZE8FSvXCxWPg8XU1aMch9s5nWGVdgPVxPXVwYz1i8frMa8egBd1Mwj7nunbWkxPmWTNScedwzob9Nk-70qoXMt_lZQ0qH7fcsGHpRjZCWY385iAXP6Hfz3DphXc8GT83iydOEVbwmFYNcjlUUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LfbJXettVNG5p0ssMrgnWJIidXY-MpPDc4ue1TWbZ10lVcV1z8_Jt3utVGt86Cz643GVeJsHhMQnXNm0KG3NoHzPJNMwTo8sM0KOT_odyoRhQ38N6uS0FvriJg-xVgiyJvPD94AZP_yRUE1vBC3A39aqA50XJj4b_iDyO5Wy0xQ5-PM6ttF1sYqQPqZrW8MBhjTFJF5gFDtFRjzn_wT0XUJrVeMWxH0varjMmEF2Zp7kpATeFwKi46LzzJ9zY7Q-HUQBDjsaC0IEauzeGZkCG_yec2crsp7cDigXT0hGLgM-Ix0YGORXjZWWDoyBF7Wp_qZL_O1ajpnq8FY6fjJ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v-iHE3ccOtlDRNdSiI0rndX4-wpREMwl_HcA440qb_ypoTw6U32M16jXbYs2YCNf45J7yEQJko10Cwh5mWf_1u1xBJcOLZhwzDTa_U3cLMz6vS4dsqSmzzymDJFSnp56Pn7AhBNetvkSLzDClC0zXGgq-3sF3t1gYURZL5xC9zsozjswif6hPri0pMSzHugKOLtaXFx5emyBlmDrDVCTDLYhZdFw-XHa5b0uTIT33-myo0DR6wME3j15qpj1J1OPef7bn5mAU0_p_uZOo31AO_ZaHSQqM_8OrjhxTIY8baVlAGJl6SYE6NvhwXhujDVFtYT_VoZcwO3sVgHCl-cqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OSeOXiWW928Af1-abxh23kuiPz9Y0-NAkWjeTvVO5tOXXfh367Atwslu8yQW4CAacTmKDZoX_uDOGWmh2ZqC7SQv48pLO0mxa9of_5ErurulCsHlSGDotAettInuo-g_2xRRoH_x9oqoIXl5Q0WU5Nh3TunoIISO595fWFGH8mQtmjFPpeIvf5Xxbib-IHzHFz_5UEjncif4JcrMN8ZLMJ1mtG-Uglwp5DMFl_NfQMK265Ql5zwyfnRRriNYI8W5-NUVMMFcSG1UMx_iBRd5eVGtN7H4u2ARhfKjLiNkf1bWFTuujXNUCwaZPim8Kh1SgEROVidzcDqhTONqsDZ69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lfqMGqtaoCG6AsTUTCL_2tmMEtpTyAlIi0Taum2ENILn9rF3eQTpp8dyKh3G6LxgH87gygE9dir8Wv4WS2aigMgnmdrDL3_a2g0XRcJu1PCWeC5JJPp5F_XkwN1djPPt2k62ARCd2kJeYxjC8P0mNnF4UEDAPMperHn9s0gqaOUUtsqdaFtfJFlzjcC0oIXme6YoEi4fCCP-UrxA6wzELFYEKZG-yCPtu4ddrI0AkwhwoC75bUBEdTzrMaCeNzdJUYIjX_MckdSTJ3j_NPuZwlmFxU7SGY_yWyJj_rivoaZFXc5AJJDoY45s1FjkB39tL_HUfx3UrkVIPp-jMCxXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BuhBF827gv60WuyTQIMAeCkbuLb0adX0n6yoZ3BpYxF-bekVY7E58SWrriKD131xSmFkNFe5kSL7shLQVanhXwcHYUEgc55ziJR9RSj-6EVXaEyftqu1Hp8paPwqCnzo9X-BdOS0ry-uKvmdwFApCgDjqQ-pxm33dyiNR0pOLP6KNSjSoAc751EH4LUv5M1QLHeTUtd_z19ayEL14j5vxVX9DPfhPoDEzRL1s5tZR_ajPq5TZkvyMZ6Du6UkCycaPsKq41WGrY7kjrnkYUC_8GPiXoig8DOhXv0V7YyvAp-cY_v3wmN-YA8MVOvtfb7ibA-YvHsLoNJFJpaTR6Iw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AtqgUAHpzpqVgYVspKiK3_OmmG4KPGKt4usL5iiibiWSxY80CH4Wz25canpNeKCV1wdV77yHN1cSPPbXVniK5Ye8SBaHpDVk3Z5RD_jJSHq1X9wesNldnsatrm5ui3b9PLDvsm_oFXvzn84xvXppefqppdsmD8qUtLjz7Qyp3Uq3tNakVAs_xH9KID_ks6ZPUCLy20jt4-smeXEs5P96cKP59cBnJjV7fdtoUjvBznEc0vNHcowkxblMhRIfYvh09afOR_4IsklSF2Xl0C56q-4eB12axiMS6Uw6HjY5gT3zb2t1KV2zIuowEMmvsU4gfsTVafn3yS7VZB2kKGScOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نفوذ حنظله به مرکز پشتیبانی از قربانیان هولوکاست و انتشار ۲ میلیون سند محرمانه
🔹
گروه هکری «حنظله» در پیام جدید خود اعلام کرد که در یک عملیات سایبری، سامانه‌ها و پایگاه‌های داده مرکز پشتیبانی از قربانیان هولوکاست را هدف قرار داده و به حجم گسترده‌ای از اطلاعات این مرکز دسترسی پیدا کرده است.
🔹
این گروه هکری تاکید کرده که تمامی پایگاه‌های داده، اسناد، ایمیل‌ها و مکاتبات محرمانه این مرکز استخراج شده و بیش از دو میلیون سند، با حجمی بالغ بر یک ترابایت، در وب‌سایت این گروه منتشر شده است.
🔹
حنظله همچنین اعلام کرده که بررسی این اسناد نشان‌دهنده ارتباط و حمایت مالی برخی شرکت‌های صنایع دفاعی اسرائیل از فعالیت‌های این مرکز است.
🔹
در بخش دیگری از این پیام، حنظله با اشاره به نهادهای امنیتی اسرائیل، به ضعف آنها در حفاظت سایبری اشاره کرده و هشدارهایی درباره ادامه فعالیت‌های خود مطرح کرده است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/438933" target="_blank">📅 09:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLoWXYQ9cz6CxaIWnKm_o34KiWHl7IOyHX9SKDHE5EINaSHmD4fFg_HdfloulZ_XDGhK8zFUbv207o3737gQi372tgPCECzV6FeF_6uCQILsTmaOcy7ZMVMpTasNpBa08kly8hrp9H1U9ZQJ-8mhTt_0h06eQLGzOMhXXjZfkrsY_zK4bZH0vxR5350lxFQGmBXvlqksCyAla-5HmQdYu7Ftq2b2j2Cp90ZMXkF86X1yi1HLQf75Ufm7B_uV5z_TuhvbI83LHtxAeXas13uBQP-u07njoJble3fufxWQBubclFCyYLYzNGqKSq3K_Ms26zUCHoPfK1r1V5tauAlwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلمب کافه‌ٔ مروج شیطان‌پرستی در تهران
🔹
پلیس نظارت بر اماکن عمومی تهران یکی از کافه‌های نزدیک به پارک دانشجو که گزارش‌هایی مبنی‌بر فعالیت‌های ترویج فرقه‌های انحرافی در آن را دریافت کرده بود، پلمب کرد.
🔹
این کافه با برگزاری برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار و «تحرکات شیطانی» فراهم آورده بود.
🔹
مشتریان این کافه در وضعیتی غیرطبیعی و با حرکاتی عجیب که از آن به‌عنوان «شیطانی» یاد شده، مشاهده شده بودند و متصدی کافه با علم به سن کم تعدادی از مشتریان، نه‌تنها مانع این رفتارها نشده، بلکه با فراهم‌کردن بستر و فضا به تسهیل این انحرافات دامن زده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/438932" target="_blank">📅 09:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438931">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987f2bb483.mov?token=jDhnU85nfIWqS1OA_z8LWEKZ0GGO53XtSU_zgTQMGCX5pFRKC1F9BgSOkw5IsCrtCrLespE4VXoehCQvcLUDsC26oA1ljin0OxJmOvtmifOANuOU4bBSXIyci3m3p0yuuPpdpbuE5fRIxMK19Q4fWl8UCHbDK1v5efqtaqvK4UZxQsDzGy9MKaQp-b3BzCzwGOvPleSHcAw2VbYKeEXGY8at7L_XCKvTxk74vYzB3AsJTG_30gvcs-ftJWN0DWzjcsMq-hZQVSap1p_lM4utnyHx7z7m8HDEPdnGARut9yxdFYhFx7xsPGzvOEDd2n8c5QUyhsNdNTck1od3pNNHRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987f2bb483.mov?token=jDhnU85nfIWqS1OA_z8LWEKZ0GGO53XtSU_zgTQMGCX5pFRKC1F9BgSOkw5IsCrtCrLespE4VXoehCQvcLUDsC26oA1ljin0OxJmOvtmifOANuOU4bBSXIyci3m3p0yuuPpdpbuE5fRIxMK19Q4fWl8UCHbDK1v5efqtaqvK4UZxQsDzGy9MKaQp-b3BzCzwGOvPleSHcAw2VbYKeEXGY8at7L_XCKvTxk74vYzB3AsJTG_30gvcs-ftJWN0DWzjcsMq-hZQVSap1p_lM4utnyHx7z7m8HDEPdnGARut9yxdFYhFx7xsPGzvOEDd2n8c5QUyhsNdNTck1od3pNNHRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبۀ ولادت امام هادی (ع) بر ایوان طلای صحن انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/438931" target="_blank">📅 09:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">«شاخۀ نفوذ» موساد چگونه افکار ایرانی‌ها را هدف می‌گیرد؟
🔹
گزارش روزنامۀ اسرائیلی «اسرائیل هیوم» به‌نقل از یک مقام سابق موساد از تشکیل شاخه‌ای مستقل با عنوان «نفوذ» در سال ۲۰۲۱ خبر می‌دهد؛ بخشی که مأموریت آن مطالعه افکار عمومی ایران، شناسایی شکاف‌های اجتماعی و طراحی عملیات‌های رسانه‌ای و روانی برای اثرگذاری بر جامعه ایران بوده است.
🔹
این مقام سابق موساد می‌گوید راهبردهای جدید موساد دیگر تنها بر عملیات‌های امنیتی و ترور متمرکز نیست و عملیات‌های مبتنی بر تأثیرگذاری اجتماعی و جنگ شناختی، به‌دلیل هزینۀ کمتر و اثربخشی بیشتر، جایگاه ویژه‌ای یافته‌اند.
🔹
موساد برای پیشبرد اهداف خود از شبکه‌های اجتماعی، رسانه‌ها، حساب‌های کاربری سازمان‌دهی‌شده و چهره‌های فضای مجازی استفاده کرده. همچنین هوش مصنوعی برای ساخت هویت‌ها و شخصیت‌های مجازی از دیگر ابزارهای این عملیات‌ها عنوان شده است.
🔹
از نگاه موساد، افکار عمومی به یکی از مهم‌ترین میدان‌های نبرد تبدیل شده و خبر، تصویر و روایت‌های منتشرشده در فضای مجازی می‌توانند به اندازۀ ابزارهای سنتی اطلاعاتی و امنیتی در پیشبرد اهداف عملیاتی نقش‌آفرین باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/438930" target="_blank">📅 09:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دستگیری ۲ مزدور رژیم صهیونیستی در ارومیه
🔹
با تلاش سربازان گمنام امام‌زمان، ۲ مزدور و وطن‌فروش وابسته به رژیم صهیونیستی در ارومیه دستگیر شدند.
🔹
این دو فرد مختصات و نشانی مکان‌های مختلف از قبیل مدارس، مساجد و حوزه‌های مقاومت بسیج را در تلگرام مخابره و پس از بمباران از مکان‌های تخریب شده و آسیب‌دیده، تصویر تهیه و به دشمن صهیونی ارسال می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/438929" target="_blank">📅 09:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swq9Qoiz2DDV443OXAsN-XEj5uLt_7Q58uUhXNFJQOB8u2b27Fhb0xTq739n17hvtTtTnrMLSwUOIiI1izxw_B3dyZyhg_5WQ_jzDGajAs9R91e7NyOqTHsNqmu7SOv5SlcZ5XZIyP2P8fdHhgmTpI7CknwWQQEF0OveBcwXNtL9iocGQ9oWhqJZ0vefbFwwhuGFnlMp30N3n8RqDx1Pyw3k4dtAUmhtfEF4fW3QJSPjVnt2B5i_ccPUsLmqn3UYoe37dWHyu03uDYS7a_iLTMayxKKfkFzWEZL_LPuq6TcjbcS8hBzkf_RtwTpuAt3CeCMjtyPOIeIhqaGr_iaPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای حملهٔ پهپادی در نزدیکی نهاریا در شمال فلسطین اشغالی فعال شد
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/438928" target="_blank">📅 09:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دادستان استان مرکزی: اموال ۷۵ نفر از خائنین به کشور توقیف می‌شود
🔹
این افراد با اقدامات ضدامنیتی خود، تلاش داشتند تا ضمن همکاری با دشمنان قسم‌خوردۀ ملت، فضای آرام جامعه را ملتهب کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/438927" target="_blank">📅 08:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5333088040.mp4?token=jbyk3ZY0i3swtt3dJutW0hwWAd5Hp1qO2fDQxW92RXeSGgWnoZ7xgSVv81tmV-VpHB6k4pjJ58f0slSLBQW9nww5H6DLVgtm0i84CE-0TQRNgbQcaoO_jXEoqvQwEyPsLgG1FoeWeFTq3_TEXNxkycb5DA4mlV8GiWtuOPS7GE0ZqI49BkJbRnRto_TJKOrWBUGlnpRy7YUiqw4jmpG5le7X5F4fWD7l7G8byKWjYxZrC5vBn0zmYsQfHv4Pfgf61xRnDdklnysCF8SBbyOXKFlNEOxGP2AOPTW5ip-W1q95WXZiueHDIhJIKQULP2zXPpZoOxNiQWdQTSgGTJ0a2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5333088040.mp4?token=jbyk3ZY0i3swtt3dJutW0hwWAd5Hp1qO2fDQxW92RXeSGgWnoZ7xgSVv81tmV-VpHB6k4pjJ58f0slSLBQW9nww5H6DLVgtm0i84CE-0TQRNgbQcaoO_jXEoqvQwEyPsLgG1FoeWeFTq3_TEXNxkycb5DA4mlV8GiWtuOPS7GE0ZqI49BkJbRnRto_TJKOrWBUGlnpRy7YUiqw4jmpG5le7X5F4fWD7l7G8byKWjYxZrC5vBn0zmYsQfHv4Pfgf61xRnDdklnysCF8SBbyOXKFlNEOxGP2AOPTW5ip-W1q95WXZiueHDIhJIKQULP2zXPpZoOxNiQWdQTSgGTJ0a2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: دما به حالت طبیعی خودش برای این موقع از سال برگشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/438926" target="_blank">📅 08:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d339c5a7ad.mp4?token=qnxOG9B_qHuHoHQAtUNGnfAJNyxmrcsrA84RSgg2qsMc6q_jI4qZ3dFpMjWY7OHdhHPZ2ikloLdyWabTOmnQgUpjeCmnLToM_TEIRUVQj_Q1jjoit6mozq3-In9nD_vK8rdqmVxxhleWwJm-WjNE3_OCSAUONrisZlvpiBmVuvwov7kpCkCFsbpwKWcUQa3NQkydsFVgUlRB86BzocT2kPyf_O6SJSSpwpI2q6KMlTnNa_gDU2McRvCTH3AEhpu4ttYcz3mrUX_i3SmqpR9c-zDs4Y4OQCM_e7sxZSXE0wk3F9SuBk-8eb-6ZyjEffaPfJzedYVTVTHXo893t9U5CmKWUV6-2rkU5o5F_-AVIDzuhkCFU2oGOucZ6TjYI18-e7Wc217zOS-LJ4Co6HTGW5_eM0dPxDOY_fEurlnoaABaH0smEqc89znzf4NIXzgutGDIGLVvotHHt6gy7TO03ygelzl9r4PR0Ljh6ivlleAzCrqqNorZTNeVoePsOjeHF9RRC9YJup-4o9CUY7xSw8eIkX2RhIDoVz9pk5cfzDOMUglN4ZD0VQ2xAtALziIXhwcLk2vuGMQeO3SYxAtDoCNyQNjaSrMnHxZERuTwO7cMZEpB8iX7pLAFtQuZUNy-wHeFT5eQ8NEP_Wn3f9XAW2i8iSbg1BBbqC_uU29El7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d339c5a7ad.mp4?token=qnxOG9B_qHuHoHQAtUNGnfAJNyxmrcsrA84RSgg2qsMc6q_jI4qZ3dFpMjWY7OHdhHPZ2ikloLdyWabTOmnQgUpjeCmnLToM_TEIRUVQj_Q1jjoit6mozq3-In9nD_vK8rdqmVxxhleWwJm-WjNE3_OCSAUONrisZlvpiBmVuvwov7kpCkCFsbpwKWcUQa3NQkydsFVgUlRB86BzocT2kPyf_O6SJSSpwpI2q6KMlTnNa_gDU2McRvCTH3AEhpu4ttYcz3mrUX_i3SmqpR9c-zDs4Y4OQCM_e7sxZSXE0wk3F9SuBk-8eb-6ZyjEffaPfJzedYVTVTHXo893t9U5CmKWUV6-2rkU5o5F_-AVIDzuhkCFU2oGOucZ6TjYI18-e7Wc217zOS-LJ4Co6HTGW5_eM0dPxDOY_fEurlnoaABaH0smEqc89znzf4NIXzgutGDIGLVvotHHt6gy7TO03ygelzl9r4PR0Ljh6ivlleAzCrqqNorZTNeVoePsOjeHF9RRC9YJup-4o9CUY7xSw8eIkX2RhIDoVz9pk5cfzDOMUglN4ZD0VQ2xAtALziIXhwcLk2vuGMQeO3SYxAtDoCNyQNjaSrMnHxZERuTwO7cMZEpB8iX7pLAFtQuZUNy-wHeFT5eQ8NEP_Wn3f9XAW2i8iSbg1BBbqC_uU29El7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای میدان انقلاب در شب نهم خرداد
🔸
از ٩ اسفند تا ٩ خرداد
🔸
ايستاده‌ايم با خروش‌وفرياد
🔹
رهبر اگر فرمان دهد تحت‌فرمانيم
🔹
شش ماه ديگر در همين ميدان می‌مانيم  @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/438925" target="_blank">📅 08:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هوای قابل‌قبول پایتخت در دومین روز هفته
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت هم‌اکنون‌ با عدد ۶۰ در شرایط «قابل قبول» است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/438924" target="_blank">📅 08:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌ عدم تحویل پرونده یا کارنامه در گروی شهریۀ مدارس تخلف است
🔹
ممانعت از تحصیل دانش‌آموز به هر علت، از جمله عدم تحویل پرونده یا کارنامۀ تحصیلی در گروی شهریه تخلف از قوانین آموزشی محسوب شده و از مصادیق جرم قانون حمایت از اطفال‌ونوجوانان است.
🔹
در صورت بروز چنین…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/438923" target="_blank">📅 07:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c2a41f90.mp4?token=izerF5WJSkwokuyHaV4zwwOBwbwlsZtEKa2NM-KVPH2fGnmpDqh2cA0pOUkj7nNSqGsdm9llaqm0yCs2RAIxmAy6w9g_GLqiQoRbuW71k-iFGvFVatAbaN4fJK0ks8XExem3Jyy6ZewGbrP9IMYXL2UGId59gIK0ux3YSz0kRZGpezcwa8nC5c1cDTSS2xTPmLJN1wpgtXRmTCLrUHlaYg8f2mc1sfdDM2RuAugAYSsaNnQv5yd--TSOSBrODtIpRLgcsc_8WPs0K_Pv8dp8tZgXUqFoKE90HYYVnj0trtzLK9D7XoUDu8fTs-NlOKpWSZ72Xb_1MFTEMmHiwPP0O4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c2a41f90.mp4?token=izerF5WJSkwokuyHaV4zwwOBwbwlsZtEKa2NM-KVPH2fGnmpDqh2cA0pOUkj7nNSqGsdm9llaqm0yCs2RAIxmAy6w9g_GLqiQoRbuW71k-iFGvFVatAbaN4fJK0ks8XExem3Jyy6ZewGbrP9IMYXL2UGId59gIK0ux3YSz0kRZGpezcwa8nC5c1cDTSS2xTPmLJN1wpgtXRmTCLrUHlaYg8f2mc1sfdDM2RuAugAYSsaNnQv5yd--TSOSBrODtIpRLgcsc_8WPs0K_Pv8dp8tZgXUqFoKE90HYYVnj0trtzLK9D7XoUDu8fTs-NlOKpWSZ72Xb_1MFTEMmHiwPP0O4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاری‌سن‌ژرمن دوباره بر بام اروپا ایستاد
⚽️
پاریسن‌ژرمن ۱(۴) - ۱(۳) آرسنال @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/438920" target="_blank">📅 07:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ ممنوعیت آزمون ورودی یا شرط معدل برای ثبت‌نام در مدارس
🔹
به‌استناد مادۀ ۴۰ آیین‌نامۀ اجرایی مدارس، برگزاری هرگونه آزمون ورودی، مصاحبه و تعیین شرط معدل برای ثبت‌نام دانش‌آموزان، جز در مواردی که مصوبۀ خاص وجود دارد، در مدارس دولتی ممنوع است.
🔹
شرایط مصاحبه…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/438919" target="_blank">📅 07:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌ ثبت‌نام میان‌پایه‌ها بعد از اعلام نتایج امتحانات
🔹
ثبت‌نام دانش‌آموزان میان‌پایۀ هر مدرسه، بعد از برگزاری امتحانات نوبت‌دوم و اعلام نتایج در سامانۀ جامع دانش‌آموزی انجام می‌شود.
🔹
ثبت‌نام دانش‌آموزان میان‌پایه در مدارس استعدادهای درخشان، نمونه دولتی و شاهد،…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/438918" target="_blank">📅 06:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔹
ثبت‌نام پایۀ اول ابتدایی از اول خرداد آغاز شده و تا ۱۰ تیر ادامه دارد.
🔹
ثبت‌نام پایۀ هفتم از اول تیر آغاز و تا هفتم تیر ادامه خواهد داشت.
🔹
پیش‌ثبت‌نام پایۀ هفتم مدارس شاهد نیز از اول تیر آغاز می‌شود و تا ۲۰…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/438917" target="_blank">📅 06:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جزئیات ثبت‌نام دانش‌آموزان در مدارس سراسر کشور
🔹
ثبت‌نام پایۀ اول ابتدایی از اول خرداد آغاز شده و تا ۱۰ تیر ادامه دارد.
🔹
ثبت‌نام پایۀ هفتم از اول تیر آغاز و تا هفتم تیر ادامه خواهد داشت.
🔹
پیش‌ثبت‌نام پایۀ هفتم مدارس شاهد نیز از اول تیر آغاز می‌شود و تا ۲۰ تیر ادامه دارد. پیش‌ثبت‌نام پایۀ دهم مدارس شاهد هم از ۲۵ تیر تا ۱۵ مرداد انجام می‌شود.
🔹
شروع فرایند ثبت‌نام دانش‌آموزان پایۀ دهم با اولویت الف از ۲۷ تیر تا دهم مرداد، و اولویت ب از ۱۱ مرداد و تا ۳۱ شهریور ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/438916" target="_blank">📅 05:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنان تکراری ترامپ: به توافق با ایران نزدیک هستیم؛ آن‌ها نباید سلاح هسته‌ای داشته باشند
🔹
ترامپ در گفت‌وگو با فاکس‌نیوز ادعا کرد که واشنگتن به دستیابی به «یک توافق بسیار خوب» با ایران نزدیک شده است.
🔹
او در عین حال همانند همیشه زبان به تهدید گشود و ادعا کرد: «در صورتی که این توافق منصفانه نباشد، آمریکا بار دیگر به «وزارت جنگ» برای بررسی گزینه‌های دیگر متوسل خواهد شد»
🔹
ترامپ همچنین گفت که گزینۀ دیپلماتیک را ترجیح می‌دهد و امضای توافق می‌تواند به بازگشایی فوری تنگۀ هرمز برای کشتیرانی بین‌المللی منجر شود.
🔹
وی مدعی شد: تضمین اصلی آمریکا در هر توافقی، جلوگیری از دستیابی ایران به سلاح هسته‌ای است.
🔹
او همچنین ادعا کرد که «طرف ایرانی پیش‌تر با عدم توسعه یا خرید سلاح هسته‌ای موافقت کرده است».
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/438915" target="_blank">📅 05:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nUPh9ZBEtW5sETbofSX480BRhpefNcsEZXMAE5L4_6SuvCd4UFh5MJ_F5j114sDzMG68IERdaMydlSRbp27_2g0aPqC1zCnbb6MYNGaKhLKlPitk7W3yUEmzaDuTUI_SS0LcEogXXKDeABu38cvl10v_pQtX2r_-vTcYJwXpGqp6I0xlqeURNPPSnUDs-nEqbPaJXialFysKu01YXOtBF25sWuytlxuNmocSeubTJBK7GjFLejd3ORBP4mdhzZJ0DdFapqS7TZFflymJVm82LUXL4tGNquxq_vhblu8rcrqzsunQnpb4R5Z69bRuwhuNyFLGsGCoLTJr9eOwVubIhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnQMEUV-KWZyLZiIwxdZxSiDll603-FQUa8TpMwEJE7vO_4kbs0iDmQVR3qXHBuOfTe2jyQ6HxHSzgG4Q_RkD0WDXUfTsSdg_-Pl2aKAEBYdoGLWsUMaAI3pMyIyU84qkDhlslDS6NfbTtfsF_pwpS5ZMqoFQwGp5d4m-aAnIQ9e4nwHaWj8hqH-DIi4RTBTCRcu3rWT9eh00siWoDrUYrYsLKNUIVgvOxdp6wiEnOUY8W_247GiayV0LinUCB3ewPe4aJ01TWrmlyGgAIznhnQeRTCv3nhiTqTTvLpogDoEzWUQNQn1t8IN7Wd0LUxVVozwXiIiYofQwY2AQfUhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3mUnzElp0xrLRVJp0yZx3dDl0JIvuvzz3P4oauNuS8FY-X0pI8jEHy20n7j3JlB-ysPpLzv0OHfEwZUebZsHsze9qinfYIJq-PtV90K8Q1kVlK1aNaSdo0AcEBsWBBP7IPoPba-CaDaCKvqB6-g86lFSMS7rFU6MSIyk3qdEfPyuajWcIT7NgYFmn36_FUMCVYLpbeqiIN2ChIfQJ0hYYRe7nKT9aSYE49pAcu1LOqgPkblcqstKH6bZ0ScPXzuw8Y-RZJ7k5f0fm9203bqbh_tupY8HDKuSwIla_qjlG77LTLujz234rRMrrcIE4BaCjf_bNUjqbNH6oCIW6Xl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kG9dLlpHwRsmNVTjsEjHGZ6bdk9iKZ_oMe2B28nx2cAy0sCRVcaP4d9AFhqhtxUuT6NE35u-_Za8jsijCl2dp2Ha202TH69gkCl8ggzpvwrUIbUomBwAkNdKpPJ901Zya1apYkdnGgYc_7ZTmbP_0a7VfcOvkm1c_IyWKD6cuQGfPt89-avMSj4U1abMOnYzTcgcwB1AAdoBUdxlg4jw2S5PpVt7PGBH4IK_aVWFzlHpkDQo6d-vkCVcIEC2h8-aV4JQLDsI4TsrlnTXKOm97rk24cvOVi07SDIhWQI4jO6avXUrYP4eRKRehI5txTN3DdiBU8GDxEzpIB4DHxdYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOqKkAIQrhmr5GHxql0vxoHyGbaKgmNixCSdsEhquTk53PNNHKDd0YHPapZOf0iVXa7L1UxhQORhhbdZmuLZY_g_JOaBY-7Zz9J9ESZBXsOsNOJxLDlrrhRq35qnhngSb22ppm5-LxDwuYqcMppR03c61MW1NDkXMig8IF0lHXAPDk6TzXpUPgYM9GNfeCZWNR8JTopiYsQLA4ID0HRHWxOwDNzyKdu0UZUIDvWHKV2e2k__cYsETydYbEnU9eDwAmrMhn4GVmFFRvxqdmiUWf6JbjNlPR2D0jA9KUDqhRuvVFh2CdKeGKY59HemVpaum42KuoSS5wTO2HNXBGIAVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چای گیلان دوباره لب‌سوز شد
🔹
با افزایش ۳۰ درصدی برداشت برگ سبز چای، رشد بیش از ۶۰ درصدی نرخ خرید تضمینی و اصلاح سیاست‌های ارزی واردات چای خشک، صنعت چای گیلان پس از سال‌ها نوسان دوباره در مسیر رونق قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/438910" target="_blank">📅 04:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc2FoPhJtp7LGagmEZYZwJy_cS6_7DOLQ7J7uPxb8-7VFZdzGnILdZWCUyDFU_pNlOxQyDBTBpCWupDsPrk0TVdrA8LI_0-hEnRQULobXOY3ngcAFBYKzj6KTXfbBnOAvNp59RL0w5WKG1Fk4owa4IydofIatGstJQVRLDljCpGI3EAGOktbKtNckUAcf8zRDpNCyOoTaq-1d6FSNHRxC-slA_3HzP-UxC31hA9Q0_qMSGys6BCE8z4dIbUK-hbQESLrc1Y7EAGNM66eXwKmfDJkzmL9M4E4rL71nkVxEf9KNotHkC2gtoItu-91ajxuqeQ75C2VDRoCISuHvTNevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ترامپ شروط سختگیرانه‌تری برای تهران ارسال کرده است
🔹
در ادامۀ روایت‌های مختلف از سوی منابع آمریکایی در ارتباط با یادداشت تفاهم میان آمریکا و ایران، روزنامه نیویورک‌تایمز نیز گزارش داد که «دونالد ترامپ، شروط مربوط به چارچوب یک توافق احتمالی با ایران را سخت‌گیرانه‌تر کرده و اصلاحات پیشنهادی را به تهران ارسال کرده است».
🔹
پیش از این، انتشار برخی گمانه‌زنی‌ها از کلیات یادداشت تفاهم میان ایران و آمریکا موجب شده بود بسیاری در آمریکا، آن را یک شکست کامل برای ترامپ توصیف کنند. انتقادات گسترده‌ای که با تلاش ترامپ برای ترسیم یک تصویر پیروزی از خود در همخوانی ندارد.
🔹
بر اساس گزارش نیویورک تایمز، ترامپ نسبت به برخی بندهای این چارچوب، به‌ویژه موارد مرتبط با آزادسازی دارایی‌ها برای ایران، ابراز نگرانی کرده است.
🔹
همچنین یکی از مقام‌های آمریکایی گفته است او از طولانی شدن روند پاسخ ایران به پیشنهادهای واشنگتن ابراز نارضایتی و خستگی کرده است.
🔹
این مقام آمریکایی همچنین مدعی شد که هدف از این اصلاحات، «وادار کردن ایران به پذیرش چارچوب اولیه‌ای است که پیش‌تر به ایران ارائه شده بود».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/438909" target="_blank">📅 04:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQo-UaE5i3-uzOjAtzOlwcJPkYZ8KfQJS_gf6l1TOs-flOjqqLVnJ3H6Cx8GI9iX1kPk0Xiy0Rb4y6P0PmvdIvgLsTgaNlvOS9JHO5CBu04WwCgwmwIsDAd10cPW_rXaRSxIdh3CQv3fUtXnT0KFzwzandnkNWHTlZhXbSGtKrRvS-_UUHqRiIpGv8Dv-xOQKgWip3EJEtO3MWUlaUQpHqY0lTwRLZZA4UhpSfX_4-65gkREeONNHFZ1hm052JdDYjLgiv1ELnyr0dP03S9aoWS3O4Ca2Zb0wDcJqcP6whBS3f9SigC0ZXrdyqOPrX_CAshfCpbaJlUljk8uSsAjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران آمریکایی:‌ چرا پسر ترامپ به جنگ نمی‌رود؟
🔹
برخی از کاربران آمریکایی با انتشار تصاویری از بارون ترامپ،‌ پسر کوچک ترامپ نوشتند که رییس‌جمهور و اعضای کابینه‌اش که مدام بر طبل جنگ می‌کوبند، چرا فرزندان خود را به صحنه‌های جنگی اعزام نمی‌کنند؟
🔹
چرا این موضوع باید فقط فرزندان خانواده‌های متوسط و فقیر آمریکایی را تهدید کند؟
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/438908" target="_blank">📅 04:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
رهگیری و انهدام یک فروند پهپاد دشمن در آب‌های سرزمینی ایران
🔹
سپاه پاسداران: بامداد امروز یک فروند پهپاد MQ1 ارتش متجاوز آمریکا که با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت، بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/438907" target="_blank">📅 04:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438902">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5igkKwXO8R3rbe-eeP9cZTrv5OKBU4Gmb09CS1-LVJlbGLahKEojGpfPMwmK5gX2u7Tja4sIAKslbFVwdn53aTFPBhUVMuo_quWUmFYXaCgyU69hcI1AWTt4vne2BB6XOKBDvyZ9NjH-k9R7d3THfSwq_QPSQy6QV0AVv2Uw1Kr5VC_rHyoH99OU4MHkjw_nfgxrels3Jh2G54RM0uGD6Gq7yn8x-xaAHyEYOKsS29ZnAPJP27V8aa3PgZXyEI0_-Pnm72y0MnRLHQsNBS5uC8Qt6h_fvpYkfIhbn2AUKb-Q4wusIQFqReHN8ixfYdHpmqHYP_O-GNzMckGdVoW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAyMvV8C8nGWwDx_Mi8J8D8D4xp8ps9UgCssWkX74qOl7UCmYvW6bIFZss-jDrHHc9o6FyHj7ofKM5gjVhWF4bmDyOZXEydPljEgDuOHYvpryam9oMUdsDzbPrI9HKR_fE3VKCW9Y7QSAK-t3H0Tm-FX1uCuCVQKBq3Dbfs5_2ds_4pN1hzbvEoTKe9XLlOEps5HuP8Lj_u8fThLo4YfINEOf3SsutQgP_ysVLqhO1JhqU7ETFIEThZ0VlWO79DPW6yetjipxxFH8tYPPJu3-V5VGZBguW7l5pWFcQGzXFZOPexgUJWG7wAeYju07vZ17b4YQfeewBJXEdnbedTxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQtjJkmPPicaAZQC0BYpWcmDaVQF5RR7Oya_Mo_04PXKdOUfXNEhKPDfYLsG0LUCEscdowz4V-8hdDe9fPap6-QBAdlC1N_5yRFuRKLWY9VgPmvX-_6NoR6T9VOhHtSU3IAEczydQTjN3FHUwa67d0Fqb2s4ku1VJIASbIdwUMY4fWoKHsxXeKP40ued8RvUePotQ9dMO2aRw2JSfUCOohrmDG92jqjrRY36-mBEcSsB5jPqjAO0vGLCZpcJkMfucFDeDqiIS-w3YgBN3RIlqmq7TeRXZSLGy7DcwJgOL7GtQ3iNtkZDMWzGp7nRIwtB9mbjPeqn1h4mFaUSuvEX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQ9wBq9YrPQOPD1M1nhXjzsybblF1trXOI5X27Q_zX1PYHn2kLFZDheXzu7yYkaWfKQ0wrlSgLbncOKrGi8p5hg1AzfjYYsuCHXR2PcX-4oBijglU93zpQT1IHNK5VCa_SiJCILUFCNnuAgq-XMNsdvcSwBNBJWKYwLn8X7fyW3jQSBM6kbhiKkSHVw0OWQXjZMRmgeNvIGHh7H2JfYYpED62yzuKmgqKXOZw6OwrxcsYiB8O0tkFL4_WFfkTHyaTW94qACwo6N8M0BVI6UTpRFj9d264IEZuJ59rLD8zNW5t__uHSMiZ-WVLN34reZhYNyTYBdCkYzPEJAdoehIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o85c64qerupJ1EaEMrTAYPo9bLPEpUhwjANeIev_Gy8vYK0apfaIVsgr5Uyf8t999IJKfV0tpqAA9BK7MoYXkmB8fogDlNQdRXx7A9QjQmbdeUGtjIBrgPS7ISEFnmV1Y8_q40tCxOpH4cx9ID9MDScGbaZ5V5UeJ2-jaMcqBjq7G-PIKWbaJ1pTRUAr2pk9mWKOlTsXS3xSjfJboIUfLI0netqy-1z1JD6hJXyPCmkFG6twweoEcE-S85-qVbsv6XC_6MJQx8z86yr-0HBJjEZLEqpOgkcwKt2nUtpmEArzFvkCOHvTWPbeH64917Bx2rTFqVHqQBK2DU6lNE-McA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بهره‌برداری از ۵ نیروگاه خورشیدی در دل طبیعت
🔹
پنج نیروگاه خورشیدی جدید در شهرستان‌های بناب، هریس و عجب‌شیر استان آذربایجان‌شرقی به بهره‌برداری رسید.
عکاس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/438902" target="_blank">📅 03:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438901">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSHXFA0Y4DYTY6UBhbSVTQgsBQHmloE5wcBv6nXpYFi4BL-ystfP0i1yl_xL4k3oAgQjBFtmDGwqqoj4l9LWiXy8VsEnpvA0rUB-t1Hubh0JS1IZ-hcEgthK0HCJTYqeGRie8FAL5W0lfCY0IWoc41twabM1k69OFrs49Imsv6QZhskGi2lIG1Dg7IEqc2KdW5APojc3vkp7xPQm0ezhWk3XAqajMjvxSskMQXewbbp1yWG9wfKupPlxIkIyDeGnoqEUYnbo_RKpQL7V10d6Vu55umxizD_0tgAt5HdHWSm1AlrjGakZiAbgMJCeiWBW5nrRzrCWSQiLE6ooJ3YNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم اصفهان به زاینده‌رود روشن می‌شود
🔹
با توجه به مصوبات ملی و استانی برای افزایش خروجی سد زاینده‌رود، از یکشنبه ۱۰ خردادماه آب در بستر رودخانۀ زاینده‌رود رهاسازی می‌شود.
🔹
این اقدام جهت تأمین نیاز زیست‌محیطی رودخانه و توزیع آب در شبکه‌های آبیاری مدرن و سنتی، و تأمین آب باغات و کشاورزی حوضۀ زاینده‌رود است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/438901" target="_blank">📅 03:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438900">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZL9u6j4t11WifbcUHkGB0Z5knlV7uROTWpj5MxoUy8hvXfwxHDNzipdaOjBPeEr_U8sj0KC3zQPRbrOma8vuQ495GX6dDc-dVHC8u23dD6E4xvcRoNMvRm0-yEywr7n2vXATk2eyafxf7KT5M2Cp0ybPQG_67S55ovCJrxtn_ECv1UvLuHnlaEXVSmK83EcdTYmb72HKAfu6doecTG3UKzJkWFCKB-70uRUp8kfM5Up0B4VDv40vCYSRIw2A3I6R_oBgMmjxoL_l6N7U8FHCTEXdrVIVKDFLAeVzBgLi5U7mKFsj2kZu7L-b11WBAOqCKYXvczSOuF7UDD2PE6Imw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان حج و زیارت: پرواز بازگشت حجاج ایرانی از دوشنبه ۱۱ خرداد آغاز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/438900" target="_blank">📅 02:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhNA9wbQ8frd-G-UF5OgmI4GsXNznZGQFfuTvfvb6PVjYe7z8GN7_F-hO8TFx4baJ9HaZnTR94mhm6huCu_-IsVwt5G_Yhokx68S3eNl-69xjnKEXHESoYS5wuzePHpfhaYrsfMMLcylD5VPJ9j7mAIaptQhmEFioFaZ8edJt3Ux30RLEJBnJUNygRpEU1u9sfx8yZnFhI-Sg9K7nMXKAqQnhduhcP2zEzwmGF_JyWk5pepTO8mS5keb9B2rQ3Tjo_EHCB6VGGNJv7wb-9AS7kKeAqWjoHdZEX1Z1KYkgbXm_ICqtDza38_uZOCU080qUhClR1HrQEpvp7Amf6ToHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژۀ نظامی دیگر آمریکا به ایلان‌ماسک سپرده شد
🔹
نیروی فضایی آمریکا اعلام کرد که ۴.۱۶ میلیارد دلار به اسپیس‌ایکس پرداخت می‌کند تا ماهواره‌هایی برای سامانۀ دفاع موشکی و پدافند هوایی «گنبد طلایی» بسازد؛ پروژه‌ای که دونالد ترامپ از آن حمایت می‌کند.
🔹
پیش از این نیز نام اسپیس‌ایکس و شبکۀ ماهواره‌ای استارلینک بارها در پروژه‌های نظامی آمریکا مطرح شده بود.
🔸
طبق گزارش رویترز، در جریان حملۀ آمریکا به ایران، پهپادهای تهاجمی و سامانه‌های بدون سرنشین از شبکۀ ماهواره‌ای اسپیس‌ایکس برای دریافت ارتباط و هدایت استفاده کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/438899" target="_blank">📅 02:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eljM55BYV6uM7OtHECL_eFa6hWyH5lix74jVC9mV-Pv6dUESOdNlEDtEhtKpxuUrd-uCVrQrRudyZWsXs9bp4v_QMcSuHelsNtGAoYvvViZJPLT3Xb3xbsmUDLqRPaNIYLNe0OxCcwqFn0LbZBqYdCWWtspYh5GWvT52yQ3PIsq4h4__jEXzlTpH_zf5VqfofEl3Vim3K54xFgEkNU48D47-0vyxuEVtGVluzz5EFtOcbvanFGP033DVGMAEcmzFYTzmi2TH-u0WPq1LbGWhkoDB2hxpjRzLJdzB_Oyb0xaYPvqXYpJbdXC_rUgNk4-Nj50YYxBj6uqSc9L3yr8JrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی شدید رژیم‌صهیونیستی در جنوب لبنان
🔹
جنگنده‌های صهیونیستی بامداد امروز چندین منطقه در جنوب لبنان را هدف حملات شدید هوایی قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/438898" target="_blank">📅 02:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
«۲۷ رجب»، جدیدترین شناور هجومی ایران
🔹
جدیدترین شناور هجومی ایران با نام «۲۷ رجب»، با سرعت خیره‌کنندۀ ۱۰۰ نات و قابلیت پرتاب موشک‌های کروز بردبلند، به عنوان نماد جدید قدرت دریایی ایران شب گذشته در میدان انقلاب رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/438897" target="_blank">📅 01:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">نایب‌قهرمانی دختر تنیسور ایرانی در تور جهانی
🔹
در رقابت‌های ۱۵ هزاردلاری تور جهانی تنیس «مشکات‌الزهرا صفی» به‌همراه هم تیمی خود از ایتالیا برابر تیمی از قزاقستان و ازبکستان ۷ بر ۵ و ۶ بر ۲ نتیجه را واگذار کرد تا در نهایت با کسب عنوان نایب‌قهرمانی این مسابقات را به پایان ببرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/438896" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ سخنگوی شهرداری تهران: در واحدهایی که نیاز به «تخریب و نوسازی» دارند حدود ۴۰ درصد پیشرفت حاصل شده است.
🔹
اینجا، پیشرفت به‌معنای انعقاد تفاهم‌نامه میان مالکان و پیمانکار، صدور پروانۀ ساختمانی و قرار داشتن بخشی از پرونده‌ها در مرحلۀ تأیید نقشه است.
🔹
۶۰ درصد…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/438895" target="_blank">📅 01:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438889">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sc36kGRsbOBZhC8o6LgBA2Rlb5PuJBaQxUYPmADedXHSdySzKSy7zaKFcW0iXq8FhUtUh5t-J9wQ-zKsq7VHtQDjkBctDqXHFn-MAVnaxf9wtaef0J9UfEpi-R3tE3ef3WIB0HJbHjzxsBan4l6Em6cu4EK-FsAqz7foLnPkdFDZxt1C3oTbS-hJMyH1L53kTwGC2h2TfgnsYR_-OYgcwPBIVjOrkk7GeYTYwqASICNaTIm45k3Nca34axiWe3TgZdB3GPr7029fFt0Oah_yxVFO7ljAzAVcGpCw0FMH-fr_Opk4gM7cspKx7Hi3WX3-aV5Xe2TNVLEIzk0Ldjy83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1AHOhJC17q4Dk1yNV7SCcNo6Eokd2hRPoVY6OjWCCsVxBqvPwu6KD6KySlFEcKesUFcKJJBibkE-AkIY55V97BfwJbZI2WVCIugahrrZnrkbA9ihxQSvAFdACEwPbXgI4J8HYJO9XXmPc2IYfrCfv3UDEb2EzrukNaqcV6AuGXqpT74IHAS_vIRR45Wu-e3JsqGmj1Zu9U_MkDazfpxIbFnbDMpe7Crh8vLgzcz8bj7DS6Eo-VCYZiOgxDeYDtLPmuJRNkl4u_UvOfpXxI8V_6H6EFD7o3RsSyyK5M2vVJ3iHvcGiBCV4T363vAxqxt3449P4IoIbBgAddDWpftrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC9gQUr3KZV0p3YcHdd8RDRtVZrnTLH9_KJFwVL_8yfWVAsTBqd8RgXGKtoihc51y8xYGiTEOy25zDosCpBrlY8ZCBaBwUV74H_H5NXR7Yl9yLIZclavyXq4_B9jVKxKgRK2uhSqEgNekHt5zoOAPZ_g8hnA4ziYpXlo3YxsGPwADisTndEhmMNNRrygkNnFUQ3qjcKoB0C7-ZChb_1m0U9c2AfcwZeHzybTl53V24WhCuAOg1q1bxdl_SQRUuJ1eiFK8_Ts0GwuAna8s5YflqNc4lOFew4J1XP1zHDX7YComGB5S6Gp5WMkEaTpwkzBMF3V9t2blpviOsSznYCd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kzq1jqoc2VGHxLT71xxFBOA5bR43uUuF5sGrhqEyB9xdlDNrPspdUnkA8CjVlERXdRSJbPC7i_IgU3j8WW-rzktFrfMlIe-I0QDGqeZWz4Zqy5DVp7KADHUtvp8Kfkj2cQ-zh4IkBQWiwwe2urYqQYpxLHHTJLZXge_jFx1W7EYQMplpKYI-qN3-kxIep1QiEdEtruvIRQM69RFk3T0YLDs6y2TQ4B4j9VdBURGEV4KQzdl7iDUVffoPjI-bCVPvduGOSgG_K50jkhdIO5Qd7-l3xW7LFjw6CQB9gMtf4yRLQRVOjoyAjr2MPEGszvSHNNIV8QOQ257xsyTvn5pnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZsOAiUNdzevVz3XVTMRz3--N9x1AVB3_46eZFm-DWsqVRan4cC1RTzt5ICcilLupgXXkybyDBrUu1QYujMQu9MI0wNUC5uk1BvCOQjj7dwbKkFi8B_ogFihHiub8kViHuBhGv_WAs9cjU2AlgbHJPPrqpmduSiGSMH9Kr3ZnEJBvFerUkuvcWBuQzLZTftg3_VOHCtPXtTnispwgRsSBfFAc4iL6fQlH0n2SOwKJSBdPtm-QXrYPYr2HnvhhgoVWLC7KHFeroBB8DW8mex7H-Ocpat5uD3p6QRAbsFqx2B8DTWAvNlVM6ZScQ5E11OBnPgJ78Z2EHXvKvKgDwqW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nx1LMrIltIE5qggcc37-3tKXBddxPjS3LXERopCKE-vloX_IScOb0Jk5iYqX89-Rk7NRpigar64Sqd9ZHQk6zvos0eQ6K-HLYmo2YzGaLiiVykf3IUYd2ebylbGKBj6w3lxB_qpQr4YxRCFL6Z2sDIzYDwyQ9hbz6TNzgWzdvY0CDZ_ffJ6s0thglCAW7CTIVMSk7GIxUYf8oxuIgzT6llk5BQ_4GbzGoDDVZ3Fj7Q0rShG89e7d5FetZZ054WzubiCtyLP959Ks7gWLa4EdNHZpZKIbf-_HMKZSzpr9MTclj2RmsZWYcqYGC11LTrUCsfpGEALpHUmS9hbzIaKhjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/438889" target="_blank">📅 01:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VD5GnkD-tJNmhhRG7zo0CmGkwyv_-1E_FmsUKv7luCWrUJiNtrJ5kP5g52VMcZSuoSNHpZF2fm81qe6dhSTjeRMn0wKTvKWl9ZXbn1V-77FCTgw5ziszL0nrhMMsV9JIGKhI_b9oW0VQzMowBKbE0CZuU5_QkjTv4HUCtL-ey4gyIVN1BjbtZE-chDXtSTUa0NjMTouFS65F_KyXTO68yfQxI-rdtETPwCI8JxfEt2Fq18qTZQNdslvTV_EGTpetSC_mlrzgA3YUEoN97hiXV-XiwsZONeZG9CDixbLosUFZ_PZWe_Erul9QaTfHjAguMGFrnvr4YdadMFOiDs6FjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooRjh44RMmC0WPW8hU5My-7_Qlg3U2SA2e7pVCxx60HeDWR8ORY0pjFSaqHiCID1PjH4dE3m0ZpnskMfVye2TErR5wzAir1nBva5TbL1BShbXLOQtQdb3A-hyM3b_NjnGVC50Y6yUTg5-CkeSLQpszYnqQQsZQEf2ZEL7bpAZvq6cf418vn_nyUHOEReLlbVmBaG4FZXgSs6nsL1iG6dH_90oumWN-TKnQoQ9p8qWkoQEFH64t3VQ555Pn5PdG14nLD5shst8HL2j7kWhRh8OmAU5JsUeDxVbdXRyAq53P_yDoejo4TqxRkL0yW868nTb_EdS155OeKhyndkzWJKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUBnNTBkC0mB2GuYikxerWE8R8Nu2QI1QxWOMp9EvU2hh0wlrRpPAPVlf5-S0BZto6FAj9jnZICZK0U0SeWSBYI7qJs1733ivICFXWIT6VALCIKdAnvMiuxDbzgvhoL0VzNP2LgZEMtlmgzAhBohO1Lr9e8LouyJfYqIwuLuAjQDyiBwyNZjJuK3GF1xFGoGHh4s5ytvEBU5gvx-mW5W7OiSDsuZjRigAkVLH-i029D9RjP4_60F8OHUxeTJCIk_eYMMlIO5SnoSSV5ah8i1XKaEAhzYojtMWZlG7LUoZc39mOCTQv3vTm906Fz0-2dHML74h4krV4AcceYbDsZ2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yptl5PkI7vcQjrQlXOBaQwGa_YGOIrzq4mt7uSoOKq-KAu3qIopwOTvW6_ysyFYH3gm87c0cW8RnIoOZnzHKImGF5l_jWNw69yVVDzBFvsFwqSfaRYudFWc3Q0oTohxoFPl2KZd8eNi3tz2luIplDZITJZplnMKMCbzr0-TxO6p6eye6PdYGOYmZBLFfXx9g5uRdde1lLtZQLDLA7Ag1Cc4RrpMGQZK5KJBBIGejX4goUnhmqx0RyoHcgLFrn2hZhfMoYxq2CPmW_1B32KuO8KLd72uZjh_Av25GIKNzllANYk5g3SOTPGX6YbDwm1XWZqMxug4fVg6VjKPvRoscPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWGSzspdHv7XrseDRKdhmlZelg2b_-RfDd4aAL0wkLIurKqf8raH54nuQzP74FqddzJIVi_hIxFjaI3l37UvtyxMh4HTkV_VIs4XnCrGDfC3ttQ-ufDPrcs0PsTsCTznWMO0msl-W2XaXzVx_oHxU3DR5vzmbkz-AJ6_VpAXrTJo5YzHY1k-0KA2uC8sNCJmceJ-ea3PGvY4epmP8eUgjUpUaeX1ACd1VcynskSUgARHNE9Sl-Mgdl0fae73MuM_XUhHk5fGh74MK9XXr-Z_nvahN1sjBzwQaq2fqHIv7i5GG43xwbh3Osj-1aEP0rbkbFydeJZqJaionGwNaToSww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPMhElt_SXwTf0EAs5auYojI0KwhBb7LwYKyO2wAA-fl63pU-zeQoBBUH8-m61DQnxL3rnLOPLS2GSZpVvWJWrwmTqqWLJyGEb2UwIY-ftixrOgd_nUGSj-M80LnIahwXTMeA5Zj0whxvivdHL_0BYTbg47Pqj-bh87Mi1kws1fQKLxXK9xX0649oPqR4Qm8muRw3TmG1I2aIJiqrbK3IJTFRgGxJbAJkihI7bWQy7dc9ednTQhqjLTqR5ZLqSmBGPL8DbZibfeiNzx40hdBM-_CRjDk6PK3SZyzhM2PCrTyiSkiS923dic7ka0TF7-ByA2iHYfTxklgVsbDlBNHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3VuY_ckd-087S44IXgzQWyeBSMAO443nH3NJun4V3LTQgL2O9WfWZd08qbzBsk4AGXLEHRuvGLsbjV98u7q0Cwrj1q5J9w6fodiNLxMxSydH_DWL_W_egh86qyXpc8hMCsSJG2e8-DH47qbhuCD2zv7wEyLPMQuC8ozz2rFuwLO-JgIvApuEhlFuGmbW4fTttvWK7VI-k3zAFa9NVcYy21QJWJV4zdQJA1yRQ8GObpV9chuyFKU8DEb59kffXNeKHYCs0PLlRZxg7-emI5uufCQx5JXoAAmrOE1z5LufsfD4YMcf9JD0oJNS6rLXadc5sNDvy70MQREcyF_ZEDUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghqXa6PVfzwjhJMxk24Ws8JrV8jPpGp1UH6VZCQJbHiZMjAzKWfyg9vJw-ZlOneZH3AiNNvut2Qplltkezb_RjSlY53K8mguMwwnSzFZOLs4WpzLdEb0_f8jCDCQc95ptcStcsWD4f3FXEQsJrPGLrA2SuRv9-0kXwnsAoZlQ6rso57yRNgjQ5cMfr_pZgRl7sPrOm7aIVpSXxgTMX9tGUhzi4KX30v9EI6KDKYsC1IQmX_baMXzXO1i8Uu_rLIxi1-ee5yBRGyYSpPMQV3k1_7sZMZ60ePyPimnRQqMVOXJBwaHf-d0WGzjelMzdyN7x7-758FuWU-oJC2L4Rn5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LU7XwWgaW3TuEB20Yf5x5TS__imgDBtpWpY_HpEccbmwGaLXJZxz4PSiejEA31AV1fLIv0vbT8LHz1eyRFKWBn2BMaG0RFN4-Arr4zzdFJnq6j17SCqqGBa4GtNpi2EG72oMvwJ19VGbS2Kf-uCapcLATL2HlwxjEpYwUt_GiwlPo8ZeSsdaP1-qhRTfJ4f8TnTW40vbUFPe8jSbK9GuMYUZewr9Wt5lORjN3-NCNZQGUcQJ0zrR9DufDrU5m-TQ8jYeey7-auky_eJilfsYOamdEI14BnnZdbT5DaKLE6e3q1jGFBJY2kSM2db5eezHf3HoshjSXKDQn6_NmEVoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKQ1m8ADHGDywaOQW0RAUuLPH0Ahr6RELQQTFjj2XwnH2zlWZ8sN4CNm9NycWPXZiNPb2Y_Od2qxTV_QQvmQrfN_62qIVYEUUrJAaC7cnMs87PCHzAe4s7sY16ZnmFQtTOF0qk9N1-Z5qyVzQElIfvQoZKt1iPrvxJ67DOqLdoOJore0wWazAywQadOSnULAeE4lNsLWNLBgTRQ_hvU-7RoCqEP_zq1RHm5Bd-akgpcCIE6IgNcbMEq3wer2AzgWjkuxQTzSxP4pcmOs648_iyGW6D9Z8IJ0qM2LNqHcvLSPW0pljILreM0wvOa11MSPRp5PmYa4TH2Q-Fgm6PsqTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/438879" target="_blank">📅 01:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438878">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هلاکت و زخمی‌شدن ۶ صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از هلاکت یک نظامی و زخمی شدن ۵ نظامی دیگر در دو حملۀ حزب‌الله در جنوب لبنان خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/438878" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438877">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هلاکت و زخمی‌شدن ۶ صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری از هلاکت یک نظامی و زخمی شدن ۵ نظامی دیگر در دو حملۀ حزب‌الله در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/438877" target="_blank">📅 00:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438876">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی شهرداری تهران: پروندۀ بازسازی خانه‌های آسیب‌دیده تا تیرماه بسته می‌شود
🔹
در بازسازی واحدهایی که نیازمند تعمیرات جزئی بوده‌اند ۹۷ درصد پیشرفت حاصل شده، و احتمالاً تا پایان همین هفته پروندۀ آن بسته می‌شود.
🔹
در واحدهایی که نیازمند «تعمیرات متوسط» هستند،…</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/438876" target="_blank">📅 00:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438875">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02a1117bb.mp4?token=P8Z7LpK6M9xoonJDOglh1VTV2NprpEiE5WoWLIbIDzSCBLcI2QmGsPyqRztldr-Es7TcfJJh_Rp3Qx-PGRs1mk51F20hRjZrSDt070nRCflRty-0-iqUmmZ5Xr3Lyn-0GGYDH1k-0kvlsxsWeBrpsOtzBCeW578ON-0Nm7BxeypupTLVLcU95hhFybcNCvwUpxi4KniWwabuZJGoyvkUYc6Ow3wg3eXjwIz138qNOEDQb3ZhccYiEUzKKNhiT_WU3GutF_YMvmlDrBfGWx0_EmGqAvUXDUX2DmFyNwqcACZCMVSklrj-LoRD-zSXfaBCcgP3-tR0i0PhEwk-6ZiJ91ZkW_ik-xFHYOTkCDYWopgTwzuTj8f9HTixLKC72lWk8fiZRkI9YPO_9vB8Gl3ibNoZaKikGPK9whlAfwt1vosfnksuI0NQ91XTCaWX6-f1Smy8kVWUKt1wI1FK0iKRwyYSUdPEv7D6dOqEnkOiUQJUN0mKMdkXbKQLXQa__AK8_3Y_-UZyxRpkydAETgATN26v5z5tJ2rk0MKrZlFC_rzhry3XK1JPj0XqT4PgZ6eccKFTbqNyO1ArpI5L3KyQh9wPWdGNYI5lfxWzkxyYEHYVU7qE4l6WG3bILuMfoKGA8PDpT6FO2NFyE5pgOtH5WvVHhzDxBwdnP8sjsw7_1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02a1117bb.mp4?token=P8Z7LpK6M9xoonJDOglh1VTV2NprpEiE5WoWLIbIDzSCBLcI2QmGsPyqRztldr-Es7TcfJJh_Rp3Qx-PGRs1mk51F20hRjZrSDt070nRCflRty-0-iqUmmZ5Xr3Lyn-0GGYDH1k-0kvlsxsWeBrpsOtzBCeW578ON-0Nm7BxeypupTLVLcU95hhFybcNCvwUpxi4KniWwabuZJGoyvkUYc6Ow3wg3eXjwIz138qNOEDQb3ZhccYiEUzKKNhiT_WU3GutF_YMvmlDrBfGWx0_EmGqAvUXDUX2DmFyNwqcACZCMVSklrj-LoRD-zSXfaBCcgP3-tR0i0PhEwk-6ZiJ91ZkW_ik-xFHYOTkCDYWopgTwzuTj8f9HTixLKC72lWk8fiZRkI9YPO_9vB8Gl3ibNoZaKikGPK9whlAfwt1vosfnksuI0NQ91XTCaWX6-f1Smy8kVWUKt1wI1FK0iKRwyYSUdPEv7D6dOqEnkOiUQJUN0mKMdkXbKQLXQa__AK8_3Y_-UZyxRpkydAETgATN26v5z5tJ2rk0MKrZlFC_rzhry3XK1JPj0XqT4PgZ6eccKFTbqNyO1ArpI5L3KyQh9wPWdGNYI5lfxWzkxyYEHYVU7qE4l6WG3bILuMfoKGA8PDpT6FO2NFyE5pgOtH5WvVHhzDxBwdnP8sjsw7_1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای میدان انقلاب در شب نهم خرداد
🔸
از ٩ اسفند تا ٩ خرداد
🔸
ايستاده‌ايم با خروش‌وفرياد
🔹
رهبر اگر فرمان دهد تحت‌فرمانيم
🔹
شش ماه ديگر در همين ميدان می‌مانيم
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/438875" target="_blank">📅 00:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">درگیری شدید و کمین رزمندگان حزب‌الله علیه ارتش رژیم‌صهیونیستی
🔹
منابع لبنانی از تلاش ارتش اشغالگر برای ورود به شهرک «دبین» و مقاومت رزمندگان مقاومت خبر می‌دهند.
🔹
درگیری شدیدی در این محور گزارش شده و نیروهای حزب‌الله چندین کمین علیه ارتش اشغالگر انجام داده‌اند.
🔸
طی درگیری‌های امشب، یک تانک مرکاوا هدف اصابت پرتابۀ حزب‌الله قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/438874" target="_blank">📅 00:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438873">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD_15k7WWXu7TBIulVvfvb8vFXSn-BhgIwVLCv99M11z7JPccNE0Y7HTFAsTPUEL6RQthfQYrxYusdKtIovYY-P7NeXh2LMxwaMaPHsdbEuNXPECApGF848CHhDuVxTLY8nrsENxc399PysStR_U9i1sQ77z8dMGwlxbn1yEEOFfXt4Gt2Ko7Obxtos2f7JbSBbaLvUNeospvtOReKW1NKHNllQSW2KBLufnoAM80YeceJdiDepiSr4Pb8spczq4uBNnPnnbXxxLOE_vZAtE5Lduh-UW9Gya8QgSUF129IAzylordd0_FjKkWmt4PS7P_KZoi21hWZDXWjI30WKWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: پروندۀ بازسازی خانه‌های آسیب‌دیده تا تیرماه بسته می‌شود
🔹
در بازسازی واحدهایی که نیازمند تعمیرات جزئی بوده‌اند ۹۷ درصد پیشرفت حاصل شده، و احتمالاً تا پایان همین هفته پروندۀ آن بسته می‌شود.
🔹
در واحدهایی که نیازمند «تعمیرات متوسط» هستند، یعنی آسیب به جداره‌های داخلی یا بخش‌هایی از منزل وارد شده اما اسکلت اصلی سازه سالم است، ۸۲ درصد پیشرفت ثبت شده و تا اواخر خردادماه به پایان میرسد.
🔹
امیدواریم کل پرونده بازسازی‌ها در شهر تهران، در تیرماه جمع‌بندی و تکمیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/438873" target="_blank">📅 00:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZCiggKijGcQFnn4aeZ3AgIxg20fVhDvLw_tY4pT8cxCQXtAPqOZQgvVMlQywbUcswA0-YlS-2ycUDMkuIaWRtD-p6QQ9WGupKwpKJOuJ5T6e0mZqVmc8fHtMjKnglyLUFVupu2-8GxZJ2RMTuihSEiIfEJ32ioiZjmEKgII7vw-y0-qYfeXUI4uJqOt_aP9-Y1KGgU9NFjJAhAe4YD0_ImjfQqkqtH4V-Y5TSHeq0zllRGDdhGKTR6a1-VSc_F6gVgIlsy5Rl0XyVG-3mCHnC9OEZRp3oUAuE-Wj3d6wyNiQCHtT1iK7eA6P5o3lWZixlUGz_jkldXYniLuJ1Du4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسب‌دوانی و افسار غنیمتی
🔹
در مسابقهٔ اسب‌دوانی، اسبِ مردی از همه جلو زد و اول شد. مردم یک‌صدا شروع به تشویق کردند و فریاد شادی سر دادند.
🔹
در این میان، مردی که در میان تماشاچیان ایستاده بود، ناگهان شروع کرد به بالا و پایین پریدن و بیش از صاحب اسب، داد و فریاد و خوشحالی می‌کرد.
🔹
صاحب اسب که از این همه شور و هیجان او تعجب کرده بود، جلو رفت و پرسید: «ای مرد، مگر این اسبِ برنده مال توست که این‌گونه شادی می‌کنی؟»
🔹
آن مرد گفت: «خیر، اسب مال من نیست؛ اما افسار آن مال من است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/438872" target="_blank">📅 00:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWZaNAiPVJxuC_ck69l5jBsM45QPQOMZzKiyeK3cbUBdm3_blpxxTlXYCm4nygaZprGzZ87k_tPBZnwzaDCaTrcgaTdAn9rwWR7fPoDbTQsskY7Im6nEERjEAamPD8eWWS2J6odrEzNGUfb0E-ar1fCgnI9pofXdnVWEUkvLzBuzjIclSIzZ2_xmlZEuxd4oxlHLlZpSsi51UMRwetEydw0ZLWIYgFKWeRxkTwYar3mIf7uJ2EVTo_1b3bG0Hn0ZLR3Dh3wBw5NwJBXh6t6nxO8xsDh85CKWZoMWAq8luSgGpxVWuYdOy4vzaGIHkPu4LN2jxivjiQhxxm8XaGLqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ چیزی که هیچ‌وقت نباید دور بیندازید!
🔹
مدیریت پسماند برای همهٔ کشورهای جهان بسیار پرهزینه است. علاوه بر اینکه پسماند زباله، مشکلات محیط زیستی را هم افزایش می‌دهد.
این ۷ وسیله از سطل زباله، فراری‌اند!
🔸
۱. فلزات مختلف
🔸
۲. لوازم الکترونیکی و الکتریکی
🔸
۳.انواع شیشه
🔸
۴. مواد پلاستیکی
🔸
۵. مواد چوبی
🔸
۶. انواع مواد کاغذی
🔸
۷. منسوجات و چرم
🔹
اغلب این لیست در خانه‌های ما پیدا می‌شود و ما بدون اینکه نیتی برای آسیب‌زدن به محیط خودمان داشته باشیم، همه اینها را در کیسه‌زباله راهی دفن گاه می‌کنیم
🔹
این‌بار بیایید بادقت بیشتری پسماند را جدا کنیم و باطری‌ها را به‌عنوان پسماند خطرناک، و باقی چیزها را در دستهٔ خودشان قرار دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/438871" target="_blank">📅 23:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📷
دیدار سخنگوی ارتش و سخنگوی وزارت خارجه  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/438870" target="_blank">📅 23:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1zANqRRXflK1vN4HFkDtY3Q4ntIV38N13OFXWMsvStPYoGGCNeEcG2RQtPefHkFP5GtOR0PwCw0rechfLV9JKcGO0DWdrcniAeqlUxGh6aXYWl5xMLnGOkETYVgbNnHol7PRLS04NEONXqxpEd0gQra7adVUJBxXqwrdCdYcgomd-6S5W5NdWkBDhZtEkpi3bdyqV_hiHbnMhLz59fp0LvCEB2S5Ic3eEBsLjokegHWmvh3FhtFAGcHqdBTQ_NjRBW75adOmMryCZZKEQY09J-t42LAo-PAuidoKaRrLXVG_EokYA3whs8Fy-_ZvT7kdE0V2ETCLvAmg5o8LG__Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار سخنگوی ارتش و سخنگوی وزارت خارجه
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/438869" target="_blank">📅 23:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
پشت همه این ماجراها موساد بود
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438868" target="_blank">📅 23:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04ca94d83.mp4?token=d5La8j9fa5KXpPno_gt38wNXhat9bQ_PAKI_2mSp9Hq21T3xk9jrzex6kMiSzfNAFWd17rmejMOoybTNlqiy4Dj52YptMfYVrY3p0TXfPJiuXqfF_mLZ5aQ9YeqvS5vObBSrUlrceVXiWtm0-yUFVAJcxxbhS6TRax0Slc31gZCXsNbK0yt2NaFNdkBzR-2AfZf47kGHtwa6SU5gKHdCjb4gWW1JH-463A4oq6LE33vOPw5H4FvkqrnJGea5s-285gz6KBRDksg2toMLPiRETGyY5HMtXY3887KHdyPqqz73RYuiUAy3zl-DG7ApecpIFZRCUKu3VpJ3Yevst25AsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04ca94d83.mp4?token=d5La8j9fa5KXpPno_gt38wNXhat9bQ_PAKI_2mSp9Hq21T3xk9jrzex6kMiSzfNAFWd17rmejMOoybTNlqiy4Dj52YptMfYVrY3p0TXfPJiuXqfF_mLZ5aQ9YeqvS5vObBSrUlrceVXiWtm0-yUFVAJcxxbhS6TRax0Slc31gZCXsNbK0yt2NaFNdkBzR-2AfZf47kGHtwa6SU5gKHdCjb4gWW1JH-463A4oq6LE33vOPw5H4FvkqrnJGea5s-285gz6KBRDksg2toMLPiRETGyY5HMtXY3887KHdyPqqz73RYuiUAy3zl-DG7ApecpIFZRCUKu3VpJ3Yevst25AsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی آرسنال سوخت؟
حیدر سلیمانی، کارشناس داوری خبرگزاری فارس:
💬
این صحنه کاملاً پنالتی بود چون مدافع پاری‌سن‌ژرمن دست مهاجم آرسنال را کشید و باعث سرنگونی او شد. به اصطلاح ما مدافع روی مهاجم آرسنال خراب شد و داور باید پنالتی اعلام می‌کرد اما انگار تیم داوری در تلاش است تا بازی را مدیریت کند و ‌بدون جنجال آن را به پایان برساند.
@Sportfars</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/438867" target="_blank">📅 23:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8817f3ad8.mp4?token=KC_LEGJboSxlGetSxu7GJX_muLBJ947kr2BkJB553m_A2nyAGQTR0-5JbrrMbJXFrkq-5GFuypZ9rqCnxwst4UlmhBTVWNVIosS2rUQNd4vOJZBpy8hIMyRzi0swI2iWOon-73-E8ZCtRljBVEVw3hDAshUAKpyd-bF1DI7XOLvT0x_DhTeXrqmiTCmsUYY5Yj6Ikh4G58AsQT0X3FmMrxClR68JkVWid0Unu3ea2lNxxh7UKXbgz-BqfpvnFRCpmuSyMeP6Mt0FEPU5-90q80n4ZNi8On661E3Ui7R8d1kG_yxZkggntwyPU4D_S90m3WatbVEaOdpn-n4ue3L5D5ealaWdA8hsGKs1ndiULEdM7bDjUd7jpkSKWx5HRE1BgjV_HiukOhD4bD9Vn_dldY0HA6aC9Cj7rnLU-ge1EllDou7ysD1mKyDepOls_JYiWIf-JoXhRvMr_tEqD0-F1SX2_zZQMHMnohwXBe_BYs0dEWXH7VIs1l5QjRVlYOpGcABAtJ6h5jOs_N1lsx3sHyo56MD41hWkE5ObdPEUXYVF8IUyJHY9vFq_nhrUYwi3FnzHnKxsL4vivmdxCpUVsX5L5XlY0h5QlrUSFY213LiXtjEq09ODQHBL3wHPwIRUlbBLA59up5Ax1vDddBmOXEdX1OVfxWu4vRXyNRI4qqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8817f3ad8.mp4?token=KC_LEGJboSxlGetSxu7GJX_muLBJ947kr2BkJB553m_A2nyAGQTR0-5JbrrMbJXFrkq-5GFuypZ9rqCnxwst4UlmhBTVWNVIosS2rUQNd4vOJZBpy8hIMyRzi0swI2iWOon-73-E8ZCtRljBVEVw3hDAshUAKpyd-bF1DI7XOLvT0x_DhTeXrqmiTCmsUYY5Yj6Ikh4G58AsQT0X3FmMrxClR68JkVWid0Unu3ea2lNxxh7UKXbgz-BqfpvnFRCpmuSyMeP6Mt0FEPU5-90q80n4ZNi8On661E3Ui7R8d1kG_yxZkggntwyPU4D_S90m3WatbVEaOdpn-n4ue3L5D5ealaWdA8hsGKs1ndiULEdM7bDjUd7jpkSKWx5HRE1BgjV_HiukOhD4bD9Vn_dldY0HA6aC9Cj7rnLU-ge1EllDou7ysD1mKyDepOls_JYiWIf-JoXhRvMr_tEqD0-F1SX2_zZQMHMnohwXBe_BYs0dEWXH7VIs1l5QjRVlYOpGcABAtJ6h5jOs_N1lsx3sHyo56MD41hWkE5ObdPEUXYVF8IUyJHY9vFq_nhrUYwi3FnzHnKxsL4vivmdxCpUVsX5L5XlY0h5QlrUSFY213LiXtjEq09ODQHBL3wHPwIRUlbBLA59up5Ax1vDddBmOXEdX1OVfxWu4vRXyNRI4qqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم مشهد با شهید مدافع امنیت عیسی عباسی از کارکنان فرماندهی انتظامی شهرستان ایرانشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/438866" target="_blank">📅 23:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438864">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00b65b542.mp4?token=oP8AxmIaq4JWUQ79Fpbi65zKyoV-qqMi3-CViDvhMExXHFk1S5mdRY4g7avzZDolvNW5dhpCTlncWqYp_VzRX6a3EFP7RcmHD7ePdWt6EYCg_DV5V0Sa6hT0bL98yHPlow3jp1m-0nAdu4VowOZVXMIQ7Y43sRGpskXVmWFhodLMGf1dRQGbYp6KH3LI4v4rprsDb6NfumVdz6YPwv3_R_qD8s2MDV3LaOtzSma5W2R2UJnRWZJTLKxvGeazXgbzouR04P0t0WvdmuEor370f_vMTAC9XtXbpp4kB3w_XUuTeQfTheJIaGOclba5xb_nlBBmBlzdmB9jBnmCSiImnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00b65b542.mp4?token=oP8AxmIaq4JWUQ79Fpbi65zKyoV-qqMi3-CViDvhMExXHFk1S5mdRY4g7avzZDolvNW5dhpCTlncWqYp_VzRX6a3EFP7RcmHD7ePdWt6EYCg_DV5V0Sa6hT0bL98yHPlow3jp1m-0nAdu4VowOZVXMIQ7Y43sRGpskXVmWFhodLMGf1dRQGbYp6KH3LI4v4rprsDb6NfumVdz6YPwv3_R_qD8s2MDV3LaOtzSma5W2R2UJnRWZJTLKxvGeazXgbzouR04P0t0WvdmuEor370f_vMTAC9XtXbpp4kB3w_XUuTeQfTheJIaGOclba5xb_nlBBmBlzdmB9jBnmCSiImnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از شناور تندروی هجومی جدید سپاه در تجمع میدان انقلاب
🔹
این شناور مجهز به قابلیت پرتاب دو فروند موشک کروز دریاپایه با برد ۷۰۰ کیلومتر و قدرت مانور و عملیات در موج با ارتفاع ۳ متر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438864" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438863">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50739c202.mp4?token=WTTZE_98sUVuL87l-jw8djpdPG_yHAmxmKoujAbC76jK7h98IQWyZv2LYH7LJsYIp7wyYM3ne1T2CgGjzxk_M1za40B6dudf7N_p2SgMDZr0462GiffQrft_y1bpMkLIxc5qXz6thyHgy3C7YDcxnN3gpRPjWpB-OUtOtou_CWJPLraMZsvSuAPrcY4mEotLGB1kHHZDMz849y3FooG8cC4qLupH5rTRkNhU5WQpU32oLJuwIkVhFlx-7Khh4e6WnD1oGZ6bfdr4lg0gXDwFgCqYH-F1C9ba9QBmixFgoqStmf4UC3ZrLEpm8tQfRAT8Sg_eINOp6xFsTsD94kr7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50739c202.mp4?token=WTTZE_98sUVuL87l-jw8djpdPG_yHAmxmKoujAbC76jK7h98IQWyZv2LYH7LJsYIp7wyYM3ne1T2CgGjzxk_M1za40B6dudf7N_p2SgMDZr0462GiffQrft_y1bpMkLIxc5qXz6thyHgy3C7YDcxnN3gpRPjWpB-OUtOtou_CWJPLraMZsvSuAPrcY4mEotLGB1kHHZDMz849y3FooG8cC4qLupH5rTRkNhU5WQpU32oLJuwIkVhFlx-7Khh4e6WnD1oGZ6bfdr4lg0gXDwFgCqYH-F1C9ba9QBmixFgoqStmf4UC3ZrLEpm8tQfRAT8Sg_eINOp6xFsTsD94kr7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی شعارهای ملی در یاسوج با لهجۀ شیرین لری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/438863" target="_blank">📅 23:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438862">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad67a09368.mp4?token=TRxWEV75Dx_gVsXF75MMmvVZNrlfMlep5uXkBZ3YTDCluYP5j9PwaM5lWwV0bQryOQXyzBNdw4kMnvrXs6HPdp1GUYF0Bw-IfAMV-zXC5doyLKuo-o9sPEOCrCpCoJMgwFf6L2J5w4ee2lSXZv9v7Df4rRq5h_eFXYz-rUj56Tt5BCE6rB_QpdaVGXbjNbmUlHj-qfs3qtf0Oa6OfhJODP9gghQZphvUhfCpE5f_ph8MtWlrC0VRCwB4ZAxsgM3SUYpsLTDkd0ltH4vfwbculU7ssQmLElGlMEdoqdzJ-vgr9GDR4bsTviw-HAaURPgn7TRix3a4iCVIQ_TM2LiSEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad67a09368.mp4?token=TRxWEV75Dx_gVsXF75MMmvVZNrlfMlep5uXkBZ3YTDCluYP5j9PwaM5lWwV0bQryOQXyzBNdw4kMnvrXs6HPdp1GUYF0Bw-IfAMV-zXC5doyLKuo-o9sPEOCrCpCoJMgwFf6L2J5w4ee2lSXZv9v7Df4rRq5h_eFXYz-rUj56Tt5BCE6rB_QpdaVGXbjNbmUlHj-qfs3qtf0Oa6OfhJODP9gghQZphvUhfCpE5f_ph8MtWlrC0VRCwB4ZAxsgM3SUYpsLTDkd0ltH4vfwbculU7ssQmLElGlMEdoqdzJ-vgr9GDR4bsTviw-HAaURPgn7TRix3a4iCVIQ_TM2LiSEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربات پنالتی که با تکرار قهرمانی پاریسی‌ها همراه شد  @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/438862" target="_blank">📅 22:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438861">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e002a8710c.mp4?token=MpJp3BsFY96tVu8QP7Nlm1FCY6coreKSdby9apmW7k9hLEZOTKXsUc5nK39bV4WWVTAaW_Fmyr-LYRr3Gz8y-zKDPfqL41-7ooEJnaT3l9tp9hmohBm5gOPZV_RB3DCXvu8Bun19cLwhF5jaCU4VWDMiPzjrVmbtEiaSb4hBWh-LzBkZm4V4kfuQgntUJ11W2HxjVD9xLrvgbw0tRaJOC-kGD6QcnkCeF8N4uLJuO_JBf5UcQEHlkxrr21wDgOnZhLGi9PXjC8VYtAqxLYDymCt7zXr9BXtKspYvbct9BHPtwxc9VAuh5fw3LBwEiRrJoJcSQA-KiP7TpQyZvS1v0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e002a8710c.mp4?token=MpJp3BsFY96tVu8QP7Nlm1FCY6coreKSdby9apmW7k9hLEZOTKXsUc5nK39bV4WWVTAaW_Fmyr-LYRr3Gz8y-zKDPfqL41-7ooEJnaT3l9tp9hmohBm5gOPZV_RB3DCXvu8Bun19cLwhF5jaCU4VWDMiPzjrVmbtEiaSb4hBWh-LzBkZm4V4kfuQgntUJ11W2HxjVD9xLrvgbw0tRaJOC-kGD6QcnkCeF8N4uLJuO_JBf5UcQEHlkxrr21wDgOnZhLGi9PXjC8VYtAqxLYDymCt7zXr9BXtKspYvbct9BHPtwxc9VAuh5fw3LBwEiRrJoJcSQA-KiP7TpQyZvS1v0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوشش بیمه‌ای ۱۰۹۳ دارو که افزایش قیمت داشته‌اند، بیشتر شد
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/438861" target="_blank">📅 22:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438860">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1756c1018.mp4?token=E-eMNkd36UFFIXzOft3bcyYtldcYOlCfwCFEGfG7SjtTyLbibM4OCUZ-feks2ElOxUYDdizz31hwC5ywg88vi7EV58OOp7zOAY8Y-PLsVbb9yAhJ5grQnSrDrA18UOugEUXfunWiRsFZsJeLNR9W0zcnRMxphDqQJV4PyLCSRX2d1p3WFVm59x5NsGorGAXw1vqBkQTljYupVImZtrgGrFMVc-fL9jR-TwvJBLB3GR7SmPLNsuPyAfvXLiO6S4WvxMKOYvQM-_6YvJgELADAQuDmUxdPJGg42swvKf0QYZ1vDr-zieAG8nn1r-CGfFYVFXUeRR0KJyTFQMtt4uZiLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1756c1018.mp4?token=E-eMNkd36UFFIXzOft3bcyYtldcYOlCfwCFEGfG7SjtTyLbibM4OCUZ-feks2ElOxUYDdizz31hwC5ywg88vi7EV58OOp7zOAY8Y-PLsVbb9yAhJ5grQnSrDrA18UOugEUXfunWiRsFZsJeLNR9W0zcnRMxphDqQJV4PyLCSRX2d1p3WFVm59x5NsGorGAXw1vqBkQTljYupVImZtrgGrFMVc-fL9jR-TwvJBLB3GR7SmPLNsuPyAfvXLiO6S4WvxMKOYvQM-_6YvJgELADAQuDmUxdPJGg42swvKf0QYZ1vDr-zieAG8nn1r-CGfFYVFXUeRR0KJyTFQMtt4uZiLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری باشکوه مردم قائن خراسان‌جنوبی در حماسهٔ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/438860" target="_blank">📅 22:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاری‌سن‌ژرمن دوباره بر بام اروپا ایستاد
⚽️
پاریسن‌ژرمن ۱(۴) - ۱(۳) آرسنال @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/438859" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438858">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6AKyHbRKYC5oGwFrrOhaMnSGHoFevyLpToINWvR2CdE21BjR7b5MR0CPpz5rsd-G8i3TAA9qQ3TupGJDPEXrRvyhyNf1667e8FiS7dNFN5fGnTfcXAI4OmpfAZJxvvRU-dh40B6A8vy2pUEPJnYurhPbB9_b316vx7ZKeFJEK_fCJbywmCd56q7km2iyPVy84eHipj8Nrr9bOp4RXxVmZH-ftv5IbVjeEm4wH3PK-nxYZKgLI9byIzd9c1qGftEE-Fvn0LhqNjhqCGPVlrB1HloLByalHdorFk4gt2hmoeJMz7fDkM2nmRZiOI7n575kTnulHAa7i9PYeAGCaNd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل تساوی پاری‌سن‌ژرمن به آرسنال توسط دمبله در دقیقه ۶۷
⚽️
آرسنال ۱ - ۱ پاری‌سن‌ژرمن @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/438858" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8849fa944.mp4?token=QMGAVjuQM1aaIf3ZXR1P58N6L1TpD1k3jBxWVTHguadne-LgaAMu7HKyQzdaC8PNdJbzpz7KWd56ng6Us39tZALD3wItEcCqZmWqEj_ALMqgkmzSfGtbAT5e5cPSV6Nm0FPGbiFSHNFB2d37bGaATAc7UvCUGyd1C0A_6UYLhQ0anqjlvKt3f3EUdNeySGrXhhkRs0Ap7RLyFIsAEmmo3tYGUh3SRdORB8XbRhWOT2-uRUOxMHJNsUK_H6Dfnf5hPYH-uOu4XgPqtOe3soDCIU1pmORM7ikfe_vm3fSJSoeYYiC4NaLZ-1KnY9htvZGE2FK4ce1Ok1HU0E83dQ27nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8849fa944.mp4?token=QMGAVjuQM1aaIf3ZXR1P58N6L1TpD1k3jBxWVTHguadne-LgaAMu7HKyQzdaC8PNdJbzpz7KWd56ng6Us39tZALD3wItEcCqZmWqEj_ALMqgkmzSfGtbAT5e5cPSV6Nm0FPGbiFSHNFB2d37bGaATAc7UvCUGyd1C0A_6UYLhQ0anqjlvKt3f3EUdNeySGrXhhkRs0Ap7RLyFIsAEmmo3tYGUh3SRdORB8XbRhWOT2-uRUOxMHJNsUK_H6Dfnf5hPYH-uOu4XgPqtOe3soDCIU1pmORM7ikfe_vm3fSJSoeYYiC4NaLZ-1KnY9htvZGE2FK4ce1Ok1HU0E83dQ27nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلمی دیگر از شنیده شدن صدای انفجار در بوستون و رود آیلند آمریکا
🔹
منابع غیررسمی از احتمال برخورد شهاب سنگ به این منطقه خبر داده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/438857" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb9f4b3dc.mp4?token=NglPWuwWcF8hb4OVsyAdmTPKZvz4qEooW1Ou2qYKdyeazy_PqiFsvycX8FXmQ6ME3Bsue27Oy8ulGdJJcGdgDR9p0ITzyfrwWv3Fr080fx5QCWaGwlkw1zdLvKlVLOtQ259rC_qbsm9Ozqnh4IiGFXhsplC7noVBVqXDgX1Uhfb5NM_72wzFl5dfE4scDkdo1IGxZhZvMzfuTtFkTo49SOT9NvmOqjtPvWNTXHQH4lCg1B8rpeo3kDo9G24yhYJLeMZB_MOWqsu2R0k6PjarSn7elv5a7YqhiOLHzi6y8qWpR1_nKwKC-vO1tE5vWMrpINASBRey54stTS_3YD2wGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb9f4b3dc.mp4?token=NglPWuwWcF8hb4OVsyAdmTPKZvz4qEooW1Ou2qYKdyeazy_PqiFsvycX8FXmQ6ME3Bsue27Oy8ulGdJJcGdgDR9p0ITzyfrwWv3Fr080fx5QCWaGwlkw1zdLvKlVLOtQ259rC_qbsm9Ozqnh4IiGFXhsplC7noVBVqXDgX1Uhfb5NM_72wzFl5dfE4scDkdo1IGxZhZvMzfuTtFkTo49SOT9NvmOqjtPvWNTXHQH4lCg1B8rpeo3kDo9G24yhYJLeMZB_MOWqsu2R0k6PjarSn7elv5a7YqhiOLHzi6y8qWpR1_nKwKC-vO1tE5vWMrpINASBRey54stTS_3YD2wGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش‌ها از انفجار در بوستون آمریکا
🔹
رسانه‌ها از وقوع انفجاری در شهر بوستون واقع در ایالت ماساچوست آمریکا خبر می‌دهند. علت این حادثه همچنان نامشخص است.
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/438856" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb147db4c.mp4?token=kOSx93iIwXD8fpui7ntnwoX23HtotdeuRxF8hK1a9-tLD3Xivsb6lKeCWwb35JiTXlES8fAMCAJlWeku1jagpaMl1eKSEcImxejhzAOdZzxhx_g9Nt7FyXSoV_noNwb8cjxt8vL8SJ5x8RK011h5TOX9ormYEkqLurapMifeWKfArkEv9qUJ5C_fYqQ9PAtI0wfqorB7oc_lvaZcwwtpPMjcWOujzYp4O9FzFRltvMP__gwxGnOvGRuKjtB5veMqPeosHCIwP0kvuCvQhc6ozftQ1-ME3FthPzD-k4vvl6iuHCY95mtqj8pMLzGOqJ8PqyZkhrYkMK2et89mnfG8Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb147db4c.mp4?token=kOSx93iIwXD8fpui7ntnwoX23HtotdeuRxF8hK1a9-tLD3Xivsb6lKeCWwb35JiTXlES8fAMCAJlWeku1jagpaMl1eKSEcImxejhzAOdZzxhx_g9Nt7FyXSoV_noNwb8cjxt8vL8SJ5x8RK011h5TOX9ormYEkqLurapMifeWKfArkEv9qUJ5C_fYqQ9PAtI0wfqorB7oc_lvaZcwwtpPMjcWOujzYp4O9FzFRltvMP__gwxGnOvGRuKjtB5veMqPeosHCIwP0kvuCvQhc6ozftQ1-ME3FthPzD-k4vvl6iuHCY95mtqj8pMLzGOqJ8PqyZkhrYkMK2et89mnfG8Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت صمت تأمین نشدن قطعات سایپا توسط کروز را تایید کرد
🔹
مفتح، قائم‌مقام وزیر صمت: زنجیرۀ تامین قطعات وابسته به شرکت ایران‌خودرو، باید براساس قراردادی که با سایپا دارد قطعات این خودروسازی را تامین کند، اما این موضوع انجام نشده است.
🔹
از بهمن پارسال هزاران…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/438855" target="_blank">📅 22:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05cad0fa31.mp4?token=NSKXE5bm5qvuByA1FJ0WgYZ1w-lOgD9PpIbScktOIWvMrW8Dhf2RqpdZl64m1aC9L_fsBA4aHM6-zDjHvLysvHjU0aF2YLKbkWrzaquSgyElgjNYc8PSc-AVbbx0Ld5iHdmZWIDYZnwxErcM4YpObVGmLd1CnE1w3CW3AjSXUH-14KbygW99AOBluMava4FQ3H8FGVADRDgamYK6tcPWHwuT0VBsK80XVKsbqsYfTSM8FMXQca7LgZ0zSXsrTlyADoyoDXXEIiIxScjwAOsT0CcFNKLFVvbPQ8-n6Vrsx8v13-OM8Pbe5SPZ2PaoM_qZReXTBgqQEilljx4_ILlvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05cad0fa31.mp4?token=NSKXE5bm5qvuByA1FJ0WgYZ1w-lOgD9PpIbScktOIWvMrW8Dhf2RqpdZl64m1aC9L_fsBA4aHM6-zDjHvLysvHjU0aF2YLKbkWrzaquSgyElgjNYc8PSc-AVbbx0Ld5iHdmZWIDYZnwxErcM4YpObVGmLd1CnE1w3CW3AjSXUH-14KbygW99AOBluMava4FQ3H8FGVADRDgamYK6tcPWHwuT0VBsK80XVKsbqsYfTSM8FMXQca7LgZ0zSXsrTlyADoyoDXXEIiIxScjwAOsT0CcFNKLFVvbPQ8-n6Vrsx8v13-OM8Pbe5SPZ2PaoM_qZReXTBgqQEilljx4_ILlvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلم لورفته از پشت‌پردهٔ مقاومت در برابر آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/438854" target="_blank">📅 22:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261e43d697.mp4?token=jdrcoaidx3-FVoydjLFGWsXKHqwLqNMjJa3dQFwXfp1Pra2M3m8Ih_4CPqKXswSaQKn3SYTkHa31qp3YEWfK6MzpMpvXMMt15Er8k-iHStC-TNLEbL9i78xtotbof46XepirVhZemXSkT6MZSAV5jILDsE8L0dU5N76eT51TvbfXBCZeOicpO3CFD672BMbYnXnPwrx6v7FYfKdQfmv5MzsRG6kEHE9LaU3b6fSNuFWRihPZIfa1CR7VyCV5JJ6uIlsUjgWbyF3veuGP0q4HVLDOnPJB8DE7oMYhYpXKpp1AkZlI7RrnSSjbVFa0hBiLUWtcwnQVk0-DasbkoxQo7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261e43d697.mp4?token=jdrcoaidx3-FVoydjLFGWsXKHqwLqNMjJa3dQFwXfp1Pra2M3m8Ih_4CPqKXswSaQKn3SYTkHa31qp3YEWfK6MzpMpvXMMt15Er8k-iHStC-TNLEbL9i78xtotbof46XepirVhZemXSkT6MZSAV5jILDsE8L0dU5N76eT51TvbfXBCZeOicpO3CFD672BMbYnXnPwrx6v7FYfKdQfmv5MzsRG6kEHE9LaU3b6fSNuFWRihPZIfa1CR7VyCV5JJ6uIlsUjgWbyF3veuGP0q4HVLDOnPJB8DE7oMYhYpXKpp1AkZlI7RrnSSjbVFa0hBiLUWtcwnQVk0-DasbkoxQo7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران ایرانی در کربلای حسینی یاد رهبر شهید انقلاب را زنده نگه‌داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/438853" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYxQTfPPuR8DQSDSQ0fne2VAbuAUBehB4QfbKNv0ijLHv8Oqs7BXgQVWQu0tGB7fIDBV2KAiU-hwzQ5_UhcB5P7qWqW3RHbIiE2AG6Fv_ynxYrLrJn7nGnbjmOsxPbkvUbdH1NcqOfD_cO-97YFsWwzeqkid_2S19_GNjXcmkRnwgJS7i3Wt2C0g5Vs06Oc9nFUv8dL7zzDCjaG4iYPE0bBJlkdEdBfKVPRwT07nqkCOtUdNcyPsFYj9pPJzJwDBWymxZ9WiM7KPP2ye3qxx_RMX0yd5B2BQQAGH15nZM-c8JoMyuH4_iH6ccSMaGCBNBixiRhEF97t2u9fVTgYAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان مشارکت در برپایی مواکب برای آئین وداع و تشییع رهبر شهید
🔹
علاقه‌مندان برای مشارکت در برپایی مواکب، ایستگاه‌های صلواتی و برنامه‌های فرهنگی به‌منظور پذیرایی و استقبال از زائران آیین وداع و تشییع «قائد شهید امت» می‌توانند از
اینجا
اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/438852" target="_blank">📅 21:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438851">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e186ff4263.mp4?token=KUn343VlybK1r0pYvZ5CIqjl9EzJdTttgcofbKi3n1ssOFYif-jg9bgS7J-pDzS1MmzEtjKNGqAzdJ4qtW39gnVAsMdb2IJbUUEJnlafN-CrdLEKPep8TPsDM9X05zUdDh9_JyD5djEh-vE3rUrAWNUUQNqxH1_pETBm6ZLGovMu9bYfn1YBpemWrCr3x1eXxJ9LBx-GKIOS_1i8Nx9Lnl95lqCn04_zlwXkzh3rBHmothRIzI7PWv8gPQoXIWzXu_FQzGy1BPjRAGS1KLWU3YhJjxBFnyygUWplem7h2hu06c_sXqv4uiaFlUBlm9nWCO5gwrOE_8yLx5G5mRkiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e186ff4263.mp4?token=KUn343VlybK1r0pYvZ5CIqjl9EzJdTttgcofbKi3n1ssOFYif-jg9bgS7J-pDzS1MmzEtjKNGqAzdJ4qtW39gnVAsMdb2IJbUUEJnlafN-CrdLEKPep8TPsDM9X05zUdDh9_JyD5djEh-vE3rUrAWNUUQNqxH1_pETBm6ZLGovMu9bYfn1YBpemWrCr3x1eXxJ9LBx-GKIOS_1i8Nx9Lnl95lqCn04_zlwXkzh3rBHmothRIzI7PWv8gPQoXIWzXu_FQzGy1BPjRAGS1KLWU3YhJjxBFnyygUWplem7h2hu06c_sXqv4uiaFlUBlm9nWCO5gwrOE_8yLx5G5mRkiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع نود و یکم مردم بندرعباس عطر غدیر گرفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/438851" target="_blank">📅 21:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438850">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8d222832.mp4?token=HSWfnn4B5jsNYQ0s_eoHx6IsXtxc-S4LEHktF63x2TmA4xn4n77F6-tTPVyl4YBxDLx1l_iebL6yyY3H8O-2bzqe5fmNz8qRauPaSEGBXKVnVUTDWid8rlNljoJo_jW59rgvsYUuhfZpoUsfvYuR-z9hc-VAwZVAomEy0LmhOBY-k9bbDaYHxQCz0U-J9xwtHitU8PC3PrSdbQahi2j7Y2c3fxIG7XdKuOHlHd4-RWuNDSWM1-cHarvJfw58jw9H_BLn9uskPnmZRKiokfwQWW18DpBonLETZyJFRX59WpN5J-KRQiBg8btsjqUYynZO9eYzQX8zceNN0Nxqu9vSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8d222832.mp4?token=HSWfnn4B5jsNYQ0s_eoHx6IsXtxc-S4LEHktF63x2TmA4xn4n77F6-tTPVyl4YBxDLx1l_iebL6yyY3H8O-2bzqe5fmNz8qRauPaSEGBXKVnVUTDWid8rlNljoJo_jW59rgvsYUuhfZpoUsfvYuR-z9hc-VAwZVAomEy0LmhOBY-k9bbDaYHxQCz0U-J9xwtHitU8PC3PrSdbQahi2j7Y2c3fxIG7XdKuOHlHd4-RWuNDSWM1-cHarvJfw58jw9H_BLn9uskPnmZRKiokfwQWW18DpBonLETZyJFRX59WpN5J-KRQiBg8btsjqUYynZO9eYzQX8zceNN0Nxqu9vSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی پاری‌سن‌ژرمن به آرسنال توسط دمبله در دقیقه ۶۷
⚽️
آرسنال ۱ - ۱ پاری‌سن‌ژرمن @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/438850" target="_blank">📅 21:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438849">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5747870e0.mp4?token=XtJidSvFSujfWiExh_a7hrOeb0IRnY4TgqJ4vB8eA9qoeIaLkrDc3bBbP9LOuLie8ALeb_ti91lQhYqiJpBKezn-zJhkfEc9xUFnBZnMsxTNYZsz9oXEoz0vvnqdNhq4JK-ZDjPnTEbpFcjzrtP34Vn6RJmgZ5cwxy2C736wl5m_3K_fI_fXtTCobB3fkSHss3eIF_avUQdzkdAaBnfy1gYgRPHcrkSSjihXGPkgy1CF05jgwlvAtjA21kA3-wKf-meZoun9dt7selyXA5n5fsgv6R6swZyxL_vkyIjnkKx4IDXkaRElw1Nt1TfTa_vdWm9JwSKt5uQYoMz--zCaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5747870e0.mp4?token=XtJidSvFSujfWiExh_a7hrOeb0IRnY4TgqJ4vB8eA9qoeIaLkrDc3bBbP9LOuLie8ALeb_ti91lQhYqiJpBKezn-zJhkfEc9xUFnBZnMsxTNYZsz9oXEoz0vvnqdNhq4JK-ZDjPnTEbpFcjzrtP34Vn6RJmgZ5cwxy2C736wl5m_3K_fI_fXtTCobB3fkSHss3eIF_avUQdzkdAaBnfy1gYgRPHcrkSSjihXGPkgy1CF05jgwlvAtjA21kA3-wKf-meZoun9dt7selyXA5n5fsgv6R6swZyxL_vkyIjnkKx4IDXkaRElw1Nt1TfTa_vdWm9JwSKt5uQYoMz--zCaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه ۱۲ اسرائیل: از صبح امروز هر ۲۲ دقیقه صدای آژیر حملات موشکی در شمال اسرائیل به صدا در آمده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/438849" target="_blank">📅 21:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438848">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837a69b9b6.mp4?token=aoudzo08cPdAdIkfeek4iRrVQPr4CWdpMDlR1EyYylyWAo89Y11urnJXCX5mlrtwS50KVPGzbwjXula3N1kCcfueuUzn6oMMxMatHcG0fFV8Ovm6vwM-fvKNWl8nnATLZsYUEkgaYA4Z-4NhGxAnE6t00DBFMboDDmnfcDlcx2wZfrKWdmz0OK-_5E1s6PRe79z-yF9SV1eWiJn283cU1s70YE1ydxi3rWOqFbIm4LAzdTmVtFDcmfRP6rQN8jggRFkTMTBocudOl_oWDn-wxgvu_0uNNiYz0Q85SO_hiKPcINYXXDWsh9hpqAReKdHJTqD72Sr4cugLxftpr2ihgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837a69b9b6.mp4?token=aoudzo08cPdAdIkfeek4iRrVQPr4CWdpMDlR1EyYylyWAo89Y11urnJXCX5mlrtwS50KVPGzbwjXula3N1kCcfueuUzn6oMMxMatHcG0fFV8Ovm6vwM-fvKNWl8nnATLZsYUEkgaYA4Z-4NhGxAnE6t00DBFMboDDmnfcDlcx2wZfrKWdmz0OK-_5E1s6PRe79z-yF9SV1eWiJn283cU1s70YE1ydxi3rWOqFbIm4LAzdTmVtFDcmfRP6rQN8jggRFkTMTBocudOl_oWDn-wxgvu_0uNNiYz0Q85SO_hiKPcINYXXDWsh9hpqAReKdHJTqD72Sr4cugLxftpr2ihgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریخ‌سازی ایلامی‌ها به شب نودویکم رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/438848" target="_blank">📅 21:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfe0b7103.mp4?token=rN6EATdOVpud5YTb5r3n_u-5OoWqA2VFzofqAemJ3bM-5ugN6-S1DcI8e2Z1ug5QEEtRzx-q2Qsj1KTLtH8O3kepzgML9F8hoUaOKa8ONBcWa6F0uWjpHW9k-lLAeGNIbq3B6v_rzAXYPU_rlZCeYWc-Od-ZJWVaaZyJLfG8-IP9LbcH61lCGpMgVkUHLk4MB1jV7nqLiwAfUVIv9wmohQ0xtPTbZAU5qllPlAFEuvLDFDyEj_EFhitrplaLY5r_pAFH9ObAl68d6_dZXJ4__4fe37k3idDAjn24KXW5MrOuFad_B9s5ZnkeDzJ27GezzqTtZiL0j6lQ4i0aHM3w_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfe0b7103.mp4?token=rN6EATdOVpud5YTb5r3n_u-5OoWqA2VFzofqAemJ3bM-5ugN6-S1DcI8e2Z1ug5QEEtRzx-q2Qsj1KTLtH8O3kepzgML9F8hoUaOKa8ONBcWa6F0uWjpHW9k-lLAeGNIbq3B6v_rzAXYPU_rlZCeYWc-Od-ZJWVaaZyJLfG8-IP9LbcH61lCGpMgVkUHLk4MB1jV7nqLiwAfUVIv9wmohQ0xtPTbZAU5qllPlAFEuvLDFDyEj_EFhitrplaLY5r_pAFH9ObAl68d6_dZXJ4__4fe37k3idDAjn24KXW5MrOuFad_B9s5ZnkeDzJ27GezzqTtZiL0j6lQ4i0aHM3w_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرسنال به پاری‌سن‌ژرمن در دقیقۀ ۶
⚽️
آرسنال ۱ - ۰ پاری‌سن‌ژرمن @Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/438847" target="_blank">📅 21:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWf_z9HY_3uooAWWe94wpvXvi6oAD0lw-Ln0hU6wa8kNvSIAUcc0TUP3vSH1MN5kQeHAthoZfhK6ra9mhW-PH92WsjREm2v0Eds89p6YJJqWizSnyyDg4cETKro2nW2B4RrdxkA0pteMblOHVJ6jecdkWH44QfGRZGspT1wU0qc5UFiS-2tCaYNA1mBiJx7PtHppOcrw1vQuMovK6ku7xsXFH1pQl7fXTIRpgyr2biPPu132D01oaGlHtWIktXyUBhEsx3F2FcOq3dWxDr6AbltpivDEDHFbleUNgMOdjAzSNnc5fWAl_qS3SG4w_Sc4T0kHCStR8Gq9VOi4DGfVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار‌ وزارت بهداشت درباره نوشیدن قهوه در تابستان
🔹
مدیرکل دفتر بهبود تغذیه وزارت بهداشت: گرمازدگی و حمله‌های ناشی از آن زمانی رخ می‌دهد که بدن قادر به خنک‌کردن خود نباشد؛ از‌این‌‌رو وجود آب کافی در بدن اهمیت دارد.
🔹
نوشیدنی‌هایی مانند قهوه، چای پررنگ و نوشابه می‌توانند موجب دهیدراته شدن و کم‌آبی بدن شوند و بهتر است در روزهای گرم مصرف آن‌ها محدود شود.
🔹
مردم حتی در صورت نداشتن احساس تشنگی نیز به میزان کافی مایعات مصرف کنند و منتظر تشنه‌شدن نمانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/438846" target="_blank">📅 20:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438845">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51323067c2.mp4?token=RfwznwCwERZtcs4ZlJTt9h3HEpLAKAG_8jP70sCsx72RE8UJl9wQYlAx8iOrQfoeRnJhU2qP4Rn2Naw6-x7XUt67BlzdWRFJDX_lWixIwAucO9P1GNxm6DPt_OhxI29R9gfT4Wov6AExRmdD2zbGw0lFSLlYzh6hVEukQ6IsdcmH9pkFy_tlxqPiJ603cReNtbOA9Gkzh_YeHHg7CQmuxzLkjQeBhBeMLrtHEwjezY1ZlY7poppiBq0UUzHljFXm7Bs4m80x9ckxPQh9crCF5hmkkOGpWlbvkLwmWWR9R5xZbu60mGiq1KRozK6KesIQAliLoycTKSVd0pLPPSBrTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51323067c2.mp4?token=RfwznwCwERZtcs4ZlJTt9h3HEpLAKAG_8jP70sCsx72RE8UJl9wQYlAx8iOrQfoeRnJhU2qP4Rn2Naw6-x7XUt67BlzdWRFJDX_lWixIwAucO9P1GNxm6DPt_OhxI29R9gfT4Wov6AExRmdD2zbGw0lFSLlYzh6hVEukQ6IsdcmH9pkFy_tlxqPiJ603cReNtbOA9Gkzh_YeHHg7CQmuxzLkjQeBhBeMLrtHEwjezY1ZlY7poppiBq0UUzHljFXm7Bs4m80x9ckxPQh9crCF5hmkkOGpWlbvkLwmWWR9R5xZbu60mGiq1KRozK6KesIQAliLoycTKSVd0pLPPSBrTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری اینترنشال: اپوزیسیون تنها رؤیافروشی می‌کند؛ باید گروهی مثل جولانی در ایران تشکیل شود
!
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/438845" target="_blank">📅 20:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDQyVdFebdcSKhPI6nkMZ3L0KCv4tJOe-9pzDzQ0aLqgwO_04W7bvkTTvLivM2o1WXx3j5_rSdfvAQ_LGNBRpB118bcrFnrj74i24Ya1uwAjC1D6Fi2NyFHKSbDyVUnKcBGlgpR1x6TeBRwPs_3mBjEoRXvUPA9dO3wE9TPn_FLdj9N9S_befnuD6EAZAmF1CRixJvxrt80JBrlP8gYzZYwfFtmtw2iF84weCBBSpxET2Ufx7xMeyl5eut75_OOp_GDW5494UZ4C_gKX9QQT5H5wTNaDzm5SRv_iIDYmsxMiix7HVQEf4_Ejdf3BBAgFmZyPHVDogrjICSoeToIW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI2BSFBvgpsUH_wueHBTvLqEwMBKvgYA7PrpoOwwMujr-yj7kiZ5Xi-xplxGRGhplGkT3IES24aaLzSPAotYr6TWNEJUyIShr9wBni6t-MkPHles5z-zRufAxUbX4n6DUpYKahcuHz5XnzerS0GTZe6PPwDp6mBRmEM86uSogQ481Z-d-V6BAdA6mQFS7PkFByr-R5v3zcMR5AC8QitvOA9Hx3HL0XSrpv4f8Ae4eVvw-3j6pGGVFIficgemUYRBznVQ1zxHsiGykw0UWj4s6XKyhfc1vKx_SlFtENdwg_WXeBpdBY0jkp3lSprVEYRcaUNhbbM7-KyXX25dI9iqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwzi8c4ACINAYAO66Gy6r8miX3CVkcLOP-BWxOBTVahjnuyJ4UdF6QwVv9rEXI71DCBlOg4OPMvMm5RQPPFQhIbFJvfO0q9OnG4_e64GjfJa81sJ5UkL7u-eZnWWmed6671MynJmR1OWp-KT62vGrpIvreZfUps7WJZWMJisOZ8w-jzZxNwzuXd6jKCX2ctSchhdvcm24AAg9KZMSvunnYarQSiJCBRvKJk5W8Nojlgkn1mkV6FlPNh_Aij_3Hk2vSoiw_Qj73Wh9K6blUb0igklneNusbdM7O0SvPgHbpyUEIz963kpNbbaW3-hEP6S7cM1aTxHtgq8-_hzKjUtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf_Q7HzieyY9ItZ2yNLQ5bUSA7t2aGzRDARbANO2C9BQo3eMNqALYHWwa1By9S6uNGDNYWsy0tAAANCtU6HffzubQX4oWdn4JfBMvyPFn0Lkfi3cspgfznNoEh1sLbK0h8IPX0nSoJVqwk2IhYlNdmvXTbJhOHaa4ChhxkTDCwiGSSxmsH99EiwJAkpbGa3pAJR62S_lxyoxjQBaf8-3mGPqbP4tgjHs8tYcn3X7r4SNhJDhntdCXnML1vkjM17TbW7k2mGALZaERrhsvgVTf3v6RgalbN-0TtMuCs1nTpT7PMiieD56pusZyfd_bWzVo2p9r9S1F8Up3TIXdfhlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKoAE9X84qpv4uoFHhvMN7wdJiUO7sRTi0ncjC14C5yRr71c9bwWSpFGMD4YQGKb94L0RJRezk57c8SL45e2uswLE8QzrSkXf-s3TI5uOM1RJVC0nIEeGeiX6K-uc7zO0PyhmGOLx0NbxyqHlRFl612F2_lrr1D6RvM39anDR6b9LVD9s-kX7K82mrGxsdlrJENordSylHYH4HFv6DochQgJTFa1rqq2n8hLUqjDsR7ivIxKFCwQIqNHsxHDYs7oLVfG9LD1AnONZDABzkf4-b4nNDLjG9xIFjwapI7j2zNlwHoVMYSQuNzA7rPdP-p6yDt3Ir04OUJiwlDSPrxxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeOyBwamN9TF3tC6n-UtZOYQmU2nK24XpKG7P1bvWJj5XzSYkIUr3CzVLFX5cjlleHIoOWWFd-xLCVyOpGklTuLDZepX0KOA04LAWr-78CnbHqu-Rz0sJKKFk6RRi14r5YC_-5eA4zTHdhtfPtcOPizTOK_IoI2UIHabmy6uzGn1Ke5e3ilxPvOMxUeqy438HwuRG3N5zg8MutvojnLihWCO_HzM7zsbvd9FXpi4DsIyUpkLHFQRJBl7Sh0HB74In4zqrK3QgrqHZWAxk9o2z8uS3rR5E-lE_zAW0kx2WsO5NCjDiq2MshtILzPVAywzibakwgxvWW95Tum7_rHA2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رئیس‌جمهور برای مدیریت انرژی کت خود را درآورد
🔹
پزشکیان امروز در نشست مدیریت بحران آب با تأکید بر ضرورت مدیریت مصرف انرژی، از حاضران خواست به‌جای پایین‌آوردن درجهٔ کولرها، کت‌های خود را درآورند.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/438839" target="_blank">📅 20:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJE4RkImuXaVYy6NgKpxUfHrU___OMdWoyMZvyTM3H1pbKlND9SNbwtAzJ2KeRBHE3iG5r1pypilvLDPuyHX8hSuMWWHr9ETN5gF_XGeaXywarHhbQWpIqOf664sppUwgdY3mgJqxq8nXAKXj9ljmMz-gU93sItP4xLeWdVH-5DKiKWXtrc2KBtVYa4j570EjvV9cpclOHXmSsqtd3IePkda5dUP5JTewHJX6q0o-FJYAK2eQB0B2vy3wnKhVijMuZEvTTRB2YeUX_gPZIlS2nXcHMznIlFSGznmDP7tRfPL91egm5IuPap9CE4CqCPxT6_Usx_zno-r8YKU4zRTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیاتی از وضعیت خوش‌حسابی مردم ایران
🔹
از حدود ۵۳ میلیون ایرانی بالای ۱۸ سال که اعتبارسنجی شده‌اند ۲۸ درصد در رتبه A و ۳۰ درصد در رتبه B قرار دارند. باقی افراد حدود ۲۵.۲ درصد در رتبه C، حدود ۱۱ درصد در رتبه D و ۴.۸ درصد در رتبه E  قرار دارند.
🔹
با این حساب، بیش از ۵۰ درصد مردم ایران جزو افراد خوش حساب محسوب می‌شوند که برای دریافت وام هیچ مشکلی نخواهند داشت؛ در حال حاضر بانک‌ها برای اعطای دسته چک باید حتما گزارش اعتبارسنجی را مبنا قرار دهند اما برای پرداخت تسهیلات، مبنا قرار دادن این گزارش الزامی نیست.
🔸
سابقه بدحسابی مانند عدم پرداخت اقساط و یا عدم وصول چک به مدت ۶ ماه در پرونده اعتبارسنجی افراد باقی می‌ماند بعد از آن در صورت پرداخت از سابقه افراد پاک خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/438838" target="_blank">📅 20:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDf2s0_W86phsMD6Q5CNqDwheqvywPHeLkAWfggmNccr1oYO8v4xX6BlO2ZmnNb_MYbIOntIepJM0eq4zIRWFmWXzwLLodJrgY2Vc4h2cDMPWnFXbXHBfZ1LWAJ5t2uk7rmXgEKPym5QySK1EbDWoW03WyIxXoTY84OHDElLcmCgEKUkiRQMDa4szwpKuh5hq74ar3NcZ5bNeKpyEEdkvK6vV26d4rlgehI5-XxlcwCtkwqj-7-DfjLVZeHKy6MIQ-Jk2H7hGBqvm7pSFixzXvfqS2NyjibIXg2aVs62qRZxeanRyXzV1dwTjT_5ntQFstxBs4C6Es7eJcO2UlOEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی نخست‌وزیر لبنان از خوش‌بینی به مذاکره با اسرائیل
🔹
نخست‌وزیر لبنان: آنچه در جنوب، النبطیه، صور و روستاهای آن اتفاق می‌افتد، دیگر تنها علیه مکان خاصی نیست بلکه سیاستی برای تخریب همه‌جانبه شهرها، روستاها و الزامات زندگی با هدف کوچاندن اجباری و دسته‌جمعی است.
🔹
دولت تصمیم گرفته است که مناسب‌ترین گزینه را برای محافظت از لبنان در این شرایط دنبال کند؛ آیا تضمینی وجود دارد که مذاکرات به نتیجه برسد؟ قطعاً نه.
🔹
دولت از هیچ تلاشی برای دستیابی به آتش‌بس، عقب‌نشینی کامل اسرائیل، آزادی اسرا و بازگشت آبرومندانه و امن مردم به خانه‌هایشان و بازسازی مناطق آسیب دیده دریغ نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/438837" target="_blank">📅 20:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هشدار سازمان بازرسی برای استرداد وجه بلیت‌های پروازهای لغو شده
🔹
سخنگوی سازمان بازرسی کل کشور: برخی ایرلاین‌ها و دفاتر خدمات مسافرت هوایی، با وجود صراحت قانون و بخشنامه‌های صادره، از برگشت کامل وجه بلیت به مسافران خودداری کرده‌اند که این امر منجر به نارضایتی…</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/438836" target="_blank">📅 20:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vChUr0GIE6G1BrZScoY1I1mumZrnf7O1R0ZFSWWpmeWgvRArmO5h-0FAiKnUQNmqswnH68my_maJXkPbQ5j7en3e0d0UoYn0pAVZlmS7wBz6t-KZIPhdvmhIzEpaPwzLLX4ZSJdIhNuxqSF0DxGI3J1pWn_9p68GmnSbTyVJ2RZEmOEFlafPNrLZp33EMRK4Fe-UAqnAo7TBk3CFFN-lEGqeaKcJqOBXNKcuV36XKN0t_33ezQ2v1epXhrJ9lLGiTfSSDiCTPNjHDxeFoFN3Xv_avDyM2_nyGmTJxeI-Fm1WSxLdlQZdHIq6DdLH9FuUQRckS9s_Fy_DpvsKgQtVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWm06clmkAHqIV8sqNXg18H3vcvQHGGoQhbiJK35LZMoJG63M7GFxXXWW7KDoFrFpakAOt6ROZAgRGz71N3p7O_6_qf-5a7u_oW4Ih6zNX8E5W5RnID0PeSWywmiNAqfRXalXZzMBNwDYnk4ZWbkNwjV5MqUBKY3vWC4si9QttTtw9M3EUrRfjsHF7sYVRXZjQbpqTMHbehpM3qwSpMBmKxZxxiibXsaAXDRHbQtQN9rfgMgl0Of0UaNepGJrwty01LSvwxihzhPDDVHn1cnr5twGZg9Ha-Faz2fp2kSzwZF0zWKxKJEYoV2Xgz80Xz_kG76hpvjLH0X3N9S90GWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkJqCqQNVLPx1RzivNKb0rHVFk23lOZYyKRw0Nn4fFYNKNqiyd-KuS3Wml4LVQ0pfgU3pnz0WjJM_qf9Qjd_XDsigvLATCeVMpIeWk4oQd1Z_a7PyHJp-o7tjYCNCcJiXWVdIWcM_ZQIq2H6ftYX-6BRzRmA5hNIl4VcgmM6AOb3k2N54QjX16T_tG7ZwrQrQiAGDj_h-SEzg4kVXH9e-vA5GDEtecZx8gjfRjQ_QmeD4oge94x8HysFUbBT3VQeELU6HmR2eZxCByUKWxVCmmdsSMn9064yxDHbPd7WuKbxtN_dCYcG9b_bQdK7HPCRbWolNXPVjI0K5xzk9q3Spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsgY8Pv8BxPKudnwRMOqDJAg-F448ACeteMlgZE7pDa2-D9huoxjG-bE20Ljk7j4OSoFUUpTmmdkRoHLBQP18fAhLD2UWOU_TxcR1cNfQ7LGCgQaR-WpEKXtxGbMX5ne7i52-XWEDwGo2VP5wf9RS-S2QANLNEJNaaGAb9Ca7gkNenzLZjVuCuj27g_1ToKjbBEBewHYfXgaUBYeJufKdOw9fTuv1G6y4Gbg6DrLqUIZi102LPD0OGvZvfnUbrKnJWl0A-yTE4lwsph2sQZXYbaj67PKYGinrKrpB9xoKVUayDZ1Ih1VCGcxRPjxko4cgDC9iBYIFR3dOSSJDBrFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LP8sROcD026x_Tz4fNCeatduSJmemhro1LHYnbi0-Iw2cOcCLn3--9BTXJxx-TuinfmZAWaX-8Gcdq7CIJjM0_hLGi8bLBHiqTRwgWcuwBsnKkBacr_GVyFhTAghidzqyohJ7ZX-3p3NIYbOvgu4MDnzi9TB0thTy8Lfi9JacRW6w5CSKe8-kn0RN46mcnzjxIQaz8tQp7qTwXycsQkpwIthjp8M6bXnafEZL_M4T4miNWoOdedEUbtB6_AoZ76sBNda4zd9PfHSGKekKSpivRuO2_kj__EC9DKhixXnpZA1Mrc8tqrlH6z5h97vlwG6lYqfKSPjk_o3-PErRD9Nmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCGEmcs5DC4IdcbK2kKvEER9x_tFCOWZwxDiBrd2g6IGDksDpT2zHcE6VZ6m3gaSReoN92k1L12Ff40-cZcmiZOX7Pv-I9-8PkNM6i5jhLbB2KNS7lcaaXAlCYSlg7WaaGk8586qEJwDuFnQABqD82RBi8szt_1J1FEaVR63VZNIvAd8DliyAqmbvgNrt637HeEJaoaE2cWgCYbNO8bYGgG125rt0xVveJuPaYTZQ3HYlI5wPyw22YSPNFQaUni6pX6aRCrN2iQh8FsAIu1VX-hSC4rD4CDenCSNiwAcvMrB5bfDNEJjLIUQCGHAKIhtz8EmIOalyQWd3LhLUM9-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zqo0xW7AAoRnDyMyc2Ge67-5jeAO3xlzfuIFkXXzR6ZbCUzAhL2bGT75BNO3SS3puHuPiwjVlf6bo2V6xLOyPSkm8v-e7GnrnVI7TloQPru1IqwkfL0br-3f4QZNNAiTeR_-JivFWoBFoJbbREs6Zyx0A8aVZs8O8JJOIx9ATmiRAflc5i0Tt84yngb-6zt5y73V5xFkUPvfAFfOgMz9h8v7r-X4K5G6mYU_TNdp01sxbnvqZaGe83u2-7S36X1foIasy7RmnN_kG10l5xDvu-ji4W5uhmGRqo5g5SwbE0r3WWLmjNxDZLtab6nKquyoVquGbMV_9YoxwI5T8Z1WZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گشت‌وگذاری در بازار مریوان کردستان
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/438827" target="_blank">📅 20:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">روزنامهٔ معاریو: اسرائیل در آستانهٔ شکست مجدد در ایران و لبنان است
🔹
تحلیلگر نظامی روزنامهٔ معاریو: هنوز مشخص نیست که آیا توافقی بین آمریکا و ایران حاصل خواهد شد یا خیر، در اسرائیل، باور غالب این است که توافقی که در حال حاضر در حال تدوین است، بد است، در واقع بسیار بد است.
🔹
زیرا آتش‌بس برای ۶۰ روز دیگر تمدید شده است، در حالی که آمریکا و اسرائیل عملاً هیچ پیشرفتی در دستیابی به اهداف جنگی خود نداشته‌اند.
🔹
یک افسر ارشد نظامی اسرائیل که هدایت عملیات علیه ایران را بر عهده داشت، به وضوح گفت که اگر حکومت ایران در قدرت بماند و اورانیوم غنی‌شده در دست آنها باقی بماند، ما به هیچ یک از اهداف جنگ دست نخواهیم یافت.
🔹
اکنون مشخص است که تنها یک برنده در این جنگ وجود دارد و احتمالاً آن آمریکا یا اسرائیل نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/438826" target="_blank">📅 20:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ecba9eb1.mp4?token=qE4H_BPrTaFyAOHh8-aKZalRkTH3RybSzSwi7K7pFKrQsHW9b_S18iFRq4YPWFoUH_rq1BNzVs-3qH2YuRgWf6MAXhCU7rjtkZK7c_eZRUDPlP41uW3zvYjokhFqPowSDCXh4m0joSxxUgdtN7_bMTqHcWeJzxjGB0aLqzr0f7qPDbY14Nb0SwEo_dM-lLZ_A9YFUBo7oPPS6sTSszSoXihe1UlK4UjtVVX6RF1JwnNQ_EXb6Bwc_kU7n4BFBIsmz6E8e-RM8vSmylZ0w1CEDNCVWWQIONs_rCqfGyKxbO0akrzb8XD68SQWe3lG6ZHlxiJGbzI7hg76xTSMSXdp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ecba9eb1.mp4?token=qE4H_BPrTaFyAOHh8-aKZalRkTH3RybSzSwi7K7pFKrQsHW9b_S18iFRq4YPWFoUH_rq1BNzVs-3qH2YuRgWf6MAXhCU7rjtkZK7c_eZRUDPlP41uW3zvYjokhFqPowSDCXh4m0joSxxUgdtN7_bMTqHcWeJzxjGB0aLqzr0f7qPDbY14Nb0SwEo_dM-lLZ_A9YFUBo7oPPS6sTSszSoXihe1UlK4UjtVVX6RF1JwnNQ_EXb6Bwc_kU7n4BFBIsmz6E8e-RM8vSmylZ0w1CEDNCVWWQIONs_rCqfGyKxbO0akrzb8XD68SQWe3lG6ZHlxiJGbzI7hg76xTSMSXdp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله: ارتش اسرائیل در هیچ نقطه‌ای در لبنان نتوانسته مستقر شود
🔹
شبکه المیادین به نقل از منابع موثق در حزب‌الله لبنان: دشمن صهیونیست کوتاه‌ترین و نزدیکترین مسیر به مرز را برای رسیدن به رودخانه لیطانی انتخاب کرده و با توجه به ناتوانی در تأمین امنیت نیروهای…</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/438825" target="_blank">📅 19:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b3b30263.mp4?token=Vu1n47pVcTh-i_HNyo-jo4VdQN4bwnGbF1ldL9bSOBjSshYg_6cF55ojr6ibNEtWRGh20nh6z3GYDGdYOZhVeGarNUvgq_WYPym0iuHBZvjFJ97jhYBd7c63qwm7D0y12sGitd7wwMTQ95oJ12u3NkHj2FuQMfHrMSZDZRxTOXZmXkrBqNy9LZct03yJdjlBlLf95hENFNBh6s_zqC1DzMISEp7N4gKO7XSzKiZZXfe5ge0FhhqjqqIsayRqjEcm73sO-W-r50e6JzDYxXtOam2_c1Ish1MtUj72a885l6GRW6DgqVAbO0lujQmZQ0lmMnDBSSrVcrG59U0vbIAhpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b3b30263.mp4?token=Vu1n47pVcTh-i_HNyo-jo4VdQN4bwnGbF1ldL9bSOBjSshYg_6cF55ojr6ibNEtWRGh20nh6z3GYDGdYOZhVeGarNUvgq_WYPym0iuHBZvjFJ97jhYBd7c63qwm7D0y12sGitd7wwMTQ95oJ12u3NkHj2FuQMfHrMSZDZRxTOXZmXkrBqNy9LZct03yJdjlBlLf95hENFNBh6s_zqC1DzMISEp7N4gKO7XSzKiZZXfe5ge0FhhqjqqIsayRqjEcm73sO-W-r50e6JzDYxXtOam2_c1Ish1MtUj72a885l6GRW6DgqVAbO0lujQmZQ0lmMnDBSSrVcrG59U0vbIAhpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول آرسنال به پاری‌سن‌ژرمن در دقیقۀ ۶
⚽️
آرسنال ۱ - ۰ پاری‌سن‌ژرمن
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/438824" target="_blank">📅 19:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌ ‌ رشد کم‌سابقۀ سکوهای داخلی در دوران جنگ  طبق نظرسنجی یک موسسه نظرسنجی وابسته به دانشگاه تهران:
🔸
سهم کاربران فعال سکوهای داخلی از ۴۵٪ به ۹۱.۶٪ رسیده است.
🔸
روبیکا مهم‌ترین مقصد مهاجرت کاربران از اینستاگرام، تلگرام و واتساپ بوده است.
🔸
۵۳.۸٪ کاربران از سکوهای…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/438823" target="_blank">📅 19:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌ مردم دربارۀ مذاکره با آمریکا چه نظری دارند؟  طبق نظرسنجی یک موسسه نظرسنجی وابسته به دانشگاه تهران:
🔸
۶۲.۳٪ مردم از پذیرش آتش‌بس توسط ایران حمایت کرده‌اند.
🔸
۵۴.۲٪ با ادامه مذاکرات موافق‌اند.
🔸
فقط ۴۲.۱٪ احتمال دستیابی به توافق را بالا می‌دانند.
🔸
۷۸.۹٪ معتقدند…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/438822" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آخرین نظرسنجی از ایران پس از جنگ
🔹
درحالی‌که جنگ روانی دشمن بر القای فروپاشی اجتماعی، گسست نسلی و انزوای سیاسی ایران متمرکز شده است، داده‌های پیمایشی یک موسسه نظرسنجی وابسته به دانشگاه تهران، تصویر متفاوتی از واقعیت‌های میدانی ارائه می‌دهند؛ داده‌هایی که نه…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/438821" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آخرین نظرسنجی از ایران پس از جنگ
🔹
درحالی‌که جنگ روانی دشمن بر القای فروپاشی اجتماعی، گسست نسلی و انزوای سیاسی ایران متمرکز شده است، داده‌های پیمایشی یک موسسه نظرسنجی وابسته به دانشگاه تهران، تصویر متفاوتی از واقعیت‌های میدانی ارائه می‌دهند؛ داده‌هایی که نه در رسانه‌های معاند، بلکه در دل جامعه ایران و در میانه حملات نظامی و رسانه‌ای ثبت شده‌اند:
🔹
ایرانِ پساجنگ؛ افزایش غرور ملی و انسجام اجتماعی
🔸
۵۸.۸٪ مردم در تجمعات مردمی یا مراسم تشییع شهدا حضور داشته‌اند.
🔸
۵۹٪ مردم نتیجه جنگ را به سود ایران ارزیابی کرده‌اند.
🔸
تنها ۱۰.۲٪ آمریکا و اسرائیل را پیروز جنگ دانسته‌اند.
🔸
احساس افتخار به جایگاه ایران در جهان از ۴۴.۲٪ به ۶۶.۹٪ افزایش یافته است.
🔹
این اعداد نشان می‌دهد جنگ نه‌تنها باعث فروپاشی اجتماعی نشد، بلکه به تقویت هویت ملی و احساس تعلق به ایران انجامید؛ در همین مدت، تمایل به مهاجرت از ایران افزایش پیدا نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438820" target="_blank">📅 19:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فرانسه: استراتژی امنیتی ما مستقل از آمریکاست
🔹
وزیر نیروهای مسلح فرانسه: پاریس بودجهٔ دفاعی خود را در دههٔ گذشته ۲ برابر کرده و به افزایش هزینه‌های نظامی ادامه می‌دهد.
🔹
سیاست دفاعی فرانسه محدود به همکاری با آمریکا نیست و فرانسه توافقات دفاعی جداگانه‌ای با امارات، قطر و چندین کشور دیگر در خاورمیانه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/438819" target="_blank">📅 19:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CL1xAHqjsEm3VB2FNtLplOKlih0e_icumV15KS6O7OWJosSnGCqrxCSPLL7gliMu_S8kXeqXy3seYPziQPLc9NDYIFa_aPjHzFec_xI_iohRl_2bhfxeBx2ltaXjH2Wu0Q_XApytgQqxycXD3-hD1QMspMgM79FpUTQdnm2lFUyedRYWzCR-4sDI15XHQ-r-lT7GybLEtENowjjh6-nA58Y1kaWkYDylpfGfIlI4oUJLOdyuwhA2ya9mtMcWxH-vt9yWOQeL_8eTGXSdhYoj_DV00p7OrZmRjlBZXISKXJ5hx9kmzZfwsGowSQMQCz2Jx8S9aq57Z1tDM63A948JLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSnXX3MKbUiWCn6pimGh_4pzH1rY6eS9A9xqM0PcEOPWZU38wswJGopFCxA7E95ISZgJiDOelXWxM_lBjaHBuMB7YcMmhO6LmVbk4whI8_7wDoCoui7rD-tZCd0erOX1N16bWAs5OltEC_fgh04VHx6WSyl8XZ9U_AWeZKW83DgpdC5CVJFMyZji2Nc6hZqYsPuTX6naIBjI2FZ7bK11urhuN2sj0X29k3VwswJ9BXlcDiahCFWVRvvsQ_L7LoVyeHznjpeVq9UsQeMSfKf3Po0yeuaxpyrqO0uUkW6gVQ8FB4xYom-pLqv2UoHzRWUP-i2srGNplxPjFqhIvwsddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrSY6SQtxkamEGb-rJl7sNx7z0NTm_BManQ8LAbs3zyBaot3MSUlkmJLPmUgiKHEMaJ_vwheLAVcSLAIa1DTlP-wyI4uTMihjI7C5OX9xwaqLngnrB8YSbCpU_eUoEYc0ZfdhcFVRi7SwJjZsEufkR19SdhqsJbJMouzChjw15Kqb4yRHInt8Rqv7ACy8u2zNb5Mi4Z37iqKHxQmkZD2RtvjZN-z0pGBjaUTtPF34xjsbcbsIkFsTIWRLQBqHW23OMgc5E4Of4RS6JtWoUXkL7613lSvrOvshYGxC2228v42QcGAxHop2FR_taTcxPb1sUe8F9yQ1DE9g7L8BGl7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4o9fOXHk96BtoJ0Z9alciCWKZm8Z0hzUX4wpP5c7krRxTcQFwB1IjCcf0RrlZXjWYGPNgXjt4brUT3yvy582ooyP4NMBIqbalnI-LtDA0NfJPYtz6cYYM5yiFW42bIBAN_uTzJeYSEfBtD41Jy2IdgQMqdfi0w2Ht6G1NTSvfoXIpuYMuWhAeunQkuf6U60TofGFq2ixt5bIBDiiuyrCyTF5IrWUinkay93swQq1Bb8XHGD8a39yszC83SM0aGyJTdXVrjwMaozenChjvt03ddkty1zcdhaWwq1HpBqeTXRSEQsKAADWqx9bAMhIeUhV-Km8p8GQxS_JhMhR4Siaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Apea4_ljmWMs_Fgulu4vTVIB0LUj1wCnxbLJKT9Lta2wVeARX_l4C_B3k3jNzPhuZuBO8ZUu-ttb1nv6OWEn3RPtDgUsnUbUhCfgJR5101IFJ_NqjdgjEa5WqbspVrL0EPz-D0m5-Xvcn_85bVEmbTZyBYzrR2YrUV7tf0ePD5x51gTeXUzRIdazZ9rWZPeoTTtvYfAuJIRQ66TLYZrtNAoMIZBRpyo6CCR0NXqR3WuWPNrl7Syy4JWK-yvXcGCneCe4p_cwG6eErHJQQHW0Ado80wLEqNhH7MdL7K_sTCDoUQttsvzdhJe4grwjnRMtqu_wrS1fxtiywJTNvEjnLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
مدیرفروش سایپا: تعهدات معوق ما ۱۰ هزار خودروی شاهین و ۱۵۰۰ خودروی کوییک است.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438812" target="_blank">📅 18:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا: مدیریت تنگۀ هرمز توسط نیروهای مسلح جمهوری اسلامی ایران با اقتدار کامل اعمال می‌شود
🔹
با توجه به یکپارچگی این مسیر، تأکید می‌شود کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفاً ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران انقلاب اسلامی هستند. هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.
🔹
همچنین هشدار داده می‌شود هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگۀ هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی ایران قرار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/438811" target="_blank">📅 18:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438810">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfefdfd81.mp4?token=tSWF6Uwx7T2tdhlKmLnWqFDQNK9GF1aiqzgcl-Cock4zyI_pkyq6Y9yVsbX3CGc60ia7L4hR-28Iwl-gm0wtXVFIZkHP4aNbMSPlTwCbGpN1WCMa1fCGqtrB76lvP7cpB4hStotjI-PCgucB_qCWj-E6bA0asqeZOjofNcjgDhd8Nuh7MrNvwpitRU-wYZH8U07TDGKU8AmXiW2C6XMiX_PeNCO_3isiVI_TtBurnDEZsZhEHyUcvUGXJEElZrwW2Xdb9mu13NuduSzJt6QtVou846fxuLqVYAFQsR2mBiBk17SAuxBpW8amzlk-_UHBQw_EIQFYtDFAYn8L-DSlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfefdfd81.mp4?token=tSWF6Uwx7T2tdhlKmLnWqFDQNK9GF1aiqzgcl-Cock4zyI_pkyq6Y9yVsbX3CGc60ia7L4hR-28Iwl-gm0wtXVFIZkHP4aNbMSPlTwCbGpN1WCMa1fCGqtrB76lvP7cpB4hStotjI-PCgucB_qCWj-E6bA0asqeZOjofNcjgDhd8Nuh7MrNvwpitRU-wYZH8U07TDGKU8AmXiW2C6XMiX_PeNCO_3isiVI_TtBurnDEZsZhEHyUcvUGXJEElZrwW2Xdb9mu13NuduSzJt6QtVou846fxuLqVYAFQsR2mBiBk17SAuxBpW8amzlk-_UHBQw_EIQFYtDFAYn8L-DSlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فراستی، منتقد سینما: دوستان سینمایی ما این شب‌ها کجا هستند؟
🔹
من و مردم حتی یک شب هیچ‌کدام از آن‌ها را در تجمعات شبانه ندیده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/438810" target="_blank">📅 18:42 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
