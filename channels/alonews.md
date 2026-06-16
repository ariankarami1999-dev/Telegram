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
<img src="https://cdn4.telesco.pe/file/Q8DLS9piyvS5KkRcN0ZOwf2xfmJ7_WOrPC1rTkPuH6KNVj-ggMWwXuf2LEVVMKzJBhKDdNQer-4T--stbuTY7UkvSI5qCbxwkE-dUt5UpmQ28Tz58IbkuhiOf_Qb5fgdPVCDSgGqO15TlBCEz5jmNBLGCtadCkw2inUHc0IoFNrJTGkZW--bJCFJkHwQrF4dm7XBzD0J_ziE1kCY92XLHEb_jB3zObGkgRNXqSD3t8zLibLER-lGb174SItnOVq4vV8PiiEGIQMBj5Anos57bjYzpzXWMouGYfGMC9zBZXjpoGNjarDbHId3X1ZpncV7BTmBJ-Pq4tElkM31d1vYhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 973K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-128409">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
حزب‌الله: ایران الان یکی از ابرقدرت های دنیاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/128409" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128408">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تخت روانچی: در سوییس پس از اینکه مسئله امضا ( تفاهمنامه پاکستان) انجام شد، مذاکرات شروع خواهد.
🔴
درباره جزئیاتی نظیر اینکه چه مدت در سوییس باشیم و چه مباحثی مطرح شوند، صحبتی نشده اما این مورد تایید دو طرف است که بعد از امضا، بحث‌ها (درباره توافق نهایی) شروع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/128408" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128407">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e565b291e7.mp4?token=ne18efqZbLRX9FnfVP6wkUopVXt8aZYOTieO8NSyogi6cQbRWheM1CWrP7g7PQ73iyptl583DT_7RCLbji6ayg5Y3fQ_Qv9WpOdUtG6ZVvH9oIN5qCqVm5LKDunZ4QClyKRFsQh70a7LMSBSBS7SWnx68vRowt7zKS9-QewmXzjlKzC_C6c4pgQdjq1oJhVnteeU8QLNZUVrWt58HzueBXer8ayb481NaHiq-2zTVfX6sdJH71BWZYngih_78RZJHEn0P6OGonliDPgtocgJYDxbaWZrzEGAXCiDyQNS8D4ije77gaz54FISqPWpqm8n5ZyQ84gjs2MmYq8SLfVfQy0JtZcQAWlARPi2auQ2YtOpnk2UivfZGyTacId1ba-uwMwUe8tLtd688AbzoyL6SgAOsCB00HYX5xJ0loRVAfslDqO7b6pzPparKHV6FBfX1S5OO9ZObsL9KJf0cjSMPA5G8f8CNElSyokHZuXap4YUZx2gKs9JzWMGL-KgzbzNtIvIqOgfL-BGscN4H4QGt8uJhlQRivdMOZGze_JOD4uxTadtiiUc8ZvBUKpdOK6E0UTOqRYnLaACj4qGJDW_MB_MAdG8Xx5IXbdwTVP3f538R3JgTtDHbMe8JR_QC857nT9LnnlbXA2Tyur9ax1Drro5i9rf--5X8Pbe4koF9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e565b291e7.mp4?token=ne18efqZbLRX9FnfVP6wkUopVXt8aZYOTieO8NSyogi6cQbRWheM1CWrP7g7PQ73iyptl583DT_7RCLbji6ayg5Y3fQ_Qv9WpOdUtG6ZVvH9oIN5qCqVm5LKDunZ4QClyKRFsQh70a7LMSBSBS7SWnx68vRowt7zKS9-QewmXzjlKzC_C6c4pgQdjq1oJhVnteeU8QLNZUVrWt58HzueBXer8ayb481NaHiq-2zTVfX6sdJH71BWZYngih_78RZJHEn0P6OGonliDPgtocgJYDxbaWZrzEGAXCiDyQNS8D4ije77gaz54FISqPWpqm8n5ZyQ84gjs2MmYq8SLfVfQy0JtZcQAWlARPi2auQ2YtOpnk2UivfZGyTacId1ba-uwMwUe8tLtd688AbzoyL6SgAOsCB00HYX5xJ0loRVAfslDqO7b6pzPparKHV6FBfX1S5OO9ZObsL9KJf0cjSMPA5G8f8CNElSyokHZuXap4YUZx2gKs9JzWMGL-KgzbzNtIvIqOgfL-BGscN4H4QGt8uJhlQRivdMOZGze_JOD4uxTadtiiUc8ZvBUKpdOK6E0UTOqRYnLaACj4qGJDW_MB_MAdG8Xx5IXbdwTVP3f538R3JgTtDHbMe8JR_QC857nT9LnnlbXA2Tyur9ax1Drro5i9rf--5X8Pbe4koF9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی، ترامپ و مکرون برای نشست گروه هفت رسیدن پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/128407" target="_blank">📅 12:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128406">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تخت‌روانچی: قالیباف و ونس در روز امضا حضور دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/128406" target="_blank">📅 11:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128405">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
در دیداری میان نخست‌وزیر عراق و فرستاده ویژه رئیس‌جمهور آمریکا، دو طرف بر اجرای طرح خلع سلاح گروه‌های مسلح خارج از چارچوب دولت و تقویت همکاری‌های اقتصادی و انرژی میان بغداد و واشنگتن تأکید کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/128405" target="_blank">📅 11:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMxW2hJkFC-qviKJHpqDLEWawZbNKAE8VbjFAQpUcKi1kiJdan24LsD11dXsa2DjK2p8fNGYFUd6a7h4uLZyDhUleGPvWx_Blrow6fbkIua0hX7ZHnpxAfzA1KXVStZ4wqvIbo8Gb4k1S9HVNrmVJdBYgAr1dg08HiM2idS1LRun3DGf5en1NewAqI92rLjWdqVAH1QEa22s04xLxR3PSX1imdP0XakA5ju9KxoA-WAzAGgkysrp_UUrmCrbWmRvGZE0N75_tAPSEOnpU1UVXcA70urdy4_ohI8FDYraz0kuxdUf_bfD3ovcjCAWWT2elCiDHzUu1GuC7vHUgnoU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPUKDJyPLnMEadnG5UFDUJT5v4FTRSPRYW0DJVxh7z752Y5nP5xqOzCTuca7-7eua0_ttPZze5rtrzKl5X0-6n7-9O0F-n4gPnN979ZVqEd0-2fZiciSizVONczO_ROGXxbCRjBFcYUKeGyOFMjAdZc79vsYcJLdu30-ShWUI5CwcZxeycoM6aAAkKAB0idFgYTi-C5QP-KII_2RlW5NTsgNxrpv6ccJYNrBRpp7ERVZaB204-DSNq8_-kOMcv1LVYfgTm0TTaLyGN44WWCtfM8-68tFfAzTbU-cm3IdK1LXLs4-9CCW6zgwbnq14SarsCcAAW0buWDisV8cn-wJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyOkdb_z6-ePN8IMNtrgAXcQVxmm78K8rY_ChN7OVkWQ6j0q9kew4RaTSKzHK0IpJ2rLwvjd3_Y4N2HQb10W8_iaPi-aA2umwoCElGaOL5ogwoO9fasijefhG4n9gNlbal0UyhWgmACCIKHvYwn9WAziIvzGM0YMP_lXZh6qQbA-l6UOteveZI8s39BHEvqtR49L_1meP5SZqaCRpFaSed6WH7pDqxMoq8C8GkQl7TiQzY0brTO7uG67o_RAwpec4T55SZv39zWtZSqw5QF8zVy8jaRExl3CKpTKuqHjdc74klnHlwzE2MRyqFpoIU1Junq7alXrSgCgksuNjdNUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6necl5uwbnhOAXfjomCfLxXvOJkBbkiUoNbXS47jGwRmIVAX_DGZOok2Jb-VyQHyUSEi43zCSm_LZ-b0ZIOH6wJmszLlNO2Y_DP6mgYj72DKRcvlsmhZHvUjwQb9ZFHbWGIJvXM_jdhdTMKEomCljJ6o6z4_4Zud3fcr14SxyFqUabQ6s6RLG-ms2AUS5zTKhPMEd3WrocW96GeA5bMpaH4lSgCgUL5yZS5vPuQLdI8Pg4VD8LCznR2jtF4SzN1YlQaIQIRjtILdsJOaVzp-EN3I3SSPwPY2bhsnP_3o8k8KYEh_EW477DnlabNqFvIAPMi63JGuZuUqGXeVuvtvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صبح زود امروز، پهپادهای اوکراینی به پالایشگاه مسکو در کاپوتنیا، روسیه حمله کردند و باعث آتش‌سوزی عظیمی در این تأسیسات شدند.
🔴
در چند ساعت گذشته حداقل ۶۰ پهپاد در منطقه مسکو رهگیری شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128401" target="_blank">📅 11:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOdwiOTZwidiw91geNCwTfYuiZqT9Z03tm08vfj2ypTmkGjv_E1MLPyOJAdhtw6bW2Aem22bxZOB6n3FglDZjny9j4pJ2eCDzPzPNKSXybXl-OBpoeX0VY52wmdUDmqmZA6OK53BqNC6O021YTRh96l2P7mSb2kJtTd6Ai0VK4vR2mbcGdssbh-eCqgSInAGx5IU0gNDsQyKZUI4vAqs9TinBxujVm2UjIRFoIMPAs_BW_7DZKhEpDS3_6nDxXhTNwq6xvsqPQjQLC-1VLClGDJzrEr8iYgcgMt6Ph8T4co_1IyHyHstalM8BG8KXd7TMqoKvXjLjA9tuUhSIu9hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا برای تخلیه بخشی از هواپیماهای سوخت‌رسان مستقر در فرودگاه بن گوریون آماده می‌شود. احتمالا حدود ۲۰٪ از هواپیماهای مستقر در اسرائیل منتقل خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128400" target="_blank">📅 11:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عراقچی: دو طرف این تفاهم‌نامه، یک طرف آمریکا و اسرائیل و طرف دیگر ایران و حزب‌الله هستند و خاتمه جنگ در لبنان، بخش جدایی‌ناپذیر از خاتمه کامل جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/128399" target="_blank">📅 11:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76adb99a74.mp4?token=ZaqdkiFbiYCw0iBDTni2f4IOnsBGFSUfXb-jyAjGQdlUM9HPNuBnO-OwHMz9ho7l5nmuK4yhbMRjn3-MTxdLAv1y6YG2lYBASn_wM_8jR_7smmcKiH2-37Z9sKpnKxO-_q3M0IjZI6zqhVU_9g0kTu9NwheAEWJhiD8gwQNru9mPM2YAgEMfA6kTwftqBk0NkcXBVTdpGWQy6HPIxY6AlVuooF4UvMajgdaeXtRlg-ef8wG0-8CqXtyEnAG31C6MYDJbSyNEyQh6MHtyDdB649szYUVyXLhIFRC_6gnFP1CSDvUPgR_UPbpK5L-JhtVQxeMwkalaPwpCZEVx7ia5plfJi6y28rcJGlEujM52WYfj5e_QZrCzXz7eKrQ_XrcaSw0KiUAWnyyBM1qrLQ2MtnUIkNbOuALUo_KokgSAJGTE9RzfiXRycp14IIlxT9eIu9kap3zEN_MMjkyCjyN66AJKXB6223IuCm4ZDVLEVzM0zu0opftC9Jr_ZfTMi9W45o75BzJ8hOYVCWkmlVstLx0mrgwHiSYhsFmkENN2CE4MwfKKJFr2lfpiBl0QEQS4SiEP6B8EKFpcKd3yv7eI8fVv15Xw3AQVfa0GOugM07Ii4SMP3Nxr5CmsZ3vd8h8uMI9ukSzO0wXXKMtunYbMYge9xTn2xXlwz7t7_pH4MFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76adb99a74.mp4?token=ZaqdkiFbiYCw0iBDTni2f4IOnsBGFSUfXb-jyAjGQdlUM9HPNuBnO-OwHMz9ho7l5nmuK4yhbMRjn3-MTxdLAv1y6YG2lYBASn_wM_8jR_7smmcKiH2-37Z9sKpnKxO-_q3M0IjZI6zqhVU_9g0kTu9NwheAEWJhiD8gwQNru9mPM2YAgEMfA6kTwftqBk0NkcXBVTdpGWQy6HPIxY6AlVuooF4UvMajgdaeXtRlg-ef8wG0-8CqXtyEnAG31C6MYDJbSyNEyQh6MHtyDdB649szYUVyXLhIFRC_6gnFP1CSDvUPgR_UPbpK5L-JhtVQxeMwkalaPwpCZEVx7ia5plfJi6y28rcJGlEujM52WYfj5e_QZrCzXz7eKrQ_XrcaSw0KiUAWnyyBM1qrLQ2MtnUIkNbOuALUo_KokgSAJGTE9RzfiXRycp14IIlxT9eIu9kap3zEN_MMjkyCjyN66AJKXB6223IuCm4ZDVLEVzM0zu0opftC9Jr_ZfTMi9W45o75BzJ8hOYVCWkmlVstLx0mrgwHiSYhsFmkENN2CE4MwfKKJFr2lfpiBl0QEQS4SiEP6B8EKFpcKd3yv7eI8fVv15Xw3AQVfa0GOugM07Ii4SMP3Nxr5CmsZ3vd8h8uMI9ukSzO0wXXKMtunYbMYge9xTn2xXlwz7t7_pH4MFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری موافقان و مخالفان ج.ا در ورزشگاه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/128398" target="_blank">📅 11:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/128397" target="_blank">📅 11:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128396">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d16e6d68.mp4?token=ZKgW-E0ar3kkGAVP-58vhjUiHKjXUhFGQuxxsXtpU10gryGf4GMzmSUVLtVN3jhSOoOhGwFZSyz8bXkdkkbggYv5sAyVN-69ETuzdYSK7IIOtTDLvbH5WhkOs4PgIK3eNSHmh1vopOpC83KfYLTFAgr89FpfwEwvR5vhomIifSwfIReIhVE5ZyFHMPsbtUD0_qGmcPcxpcj4Pfogkhwd6QPqsXqZVyatCbHj7MPGshO7I1Ho3BR_mcTslGbS07DRQnTBau-eubSyY-eHUN9j-11YuUCudWaA-pt9eJs-58WOhdKN4Q6CKDc9n1QIjXkUQFafobKmJHat9WEfz04ThA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d16e6d68.mp4?token=ZKgW-E0ar3kkGAVP-58vhjUiHKjXUhFGQuxxsXtpU10gryGf4GMzmSUVLtVN3jhSOoOhGwFZSyz8bXkdkkbggYv5sAyVN-69ETuzdYSK7IIOtTDLvbH5WhkOs4PgIK3eNSHmh1vopOpC83KfYLTFAgr89FpfwEwvR5vhomIifSwfIReIhVE5ZyFHMPsbtUD0_qGmcPcxpcj4Pfogkhwd6QPqsXqZVyatCbHj7MPGshO7I1Ho3BR_mcTslGbS07DRQnTBau-eubSyY-eHUN9j-11YuUCudWaA-pt9eJs-58WOhdKN4Q6CKDc9n1QIjXkUQFafobKmJHat9WEfz04ThA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ترافیک گیر کردی
اون زن چادری پرچم به دست:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128396" target="_blank">📅 11:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی: روز جمعه دور جدید مذاکرات ایران و آمریکا برای رسیدن به توافق نهایی آغاز می‌شود.
🔴
بعد از سه ماه مذاکره توانستیم مرحله اول را نهایی کنیم.
🔴
در مرحله اول مهمترین موضوعی که اتفاق می‌افتد اعلام خاتمه جنگ است و بنا به تصمیمی که گرفتیم از صبح روز دوشنبه به وقت تهران که این توافق نهایی شد، خاتمه جنگ هم اعلام شد. ولی شروع رسمی تفاهمنامه از روز جمعه خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/128395" target="_blank">📅 10:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اختلال ادامه‌دار در بانک ملی و صادرات
با وجود گذشت چند روز از شروع اختلال در خدمات بانک ملی و صادرات، سرویس‌های مختلف همچنان با اختلال همراه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128394" target="_blank">📅 10:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128393">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">از بین ۴۸ تیمی که در جام جهانی حضور دارند، رتبه‌ نیوزیلند در رنکینگ فیفا از همه پایینتر است؛ حتی از کیپ ورد، هائیتی و کوراسائو.
🇨🇻
کیپ ورد - ۶۷
🇨🇼
کوراسائو - ۸۲
🇭🇹
هائیتی - ۸۳
🇳🇿
نیوزیلند - ۸۵
@AloSport</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128393" target="_blank">📅 10:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128392">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128392" target="_blank">📅 10:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128391">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd2ad4863.mp4?token=G818O1XX5hRKsnvGRm_Ev1xFMOdQnhj-K1yaW1MSqrDAUpxTzukFTGsCwmcrtPVXS2axLD2OB4GWX7rp5T-QgCu-ddxF6uSvXHi6ILfCNPUhkQoXzcctl7si_jxJLyH_pMz5R1zq-AzIQGIEHKIcpK5jQJtvLAHV0Fd_czgbTXyVJyojx58_IoM4c3FHQ9fkagF0SZOzfLwi4uL-1ZnBYM3iskBeDBx0uiqdJ14MvDnlKFcYKnR5fevGWqDiKesYd3EQZOTSHrRhPWXqEZlW8GRG5WNnYW7hLbRKHoDfANSlPH9ARdsWEVd7Ejp4bDVw73VpAeu06k3xclmnimEUOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd2ad4863.mp4?token=G818O1XX5hRKsnvGRm_Ev1xFMOdQnhj-K1yaW1MSqrDAUpxTzukFTGsCwmcrtPVXS2axLD2OB4GWX7rp5T-QgCu-ddxF6uSvXHi6ILfCNPUhkQoXzcctl7si_jxJLyH_pMz5R1zq-AzIQGIEHKIcpK5jQJtvLAHV0Fd_czgbTXyVJyojx58_IoM4c3FHQ9fkagF0SZOzfLwi4uL-1ZnBYM3iskBeDBx0uiqdJ14MvDnlKFcYKnR5fevGWqDiKesYd3EQZOTSHrRhPWXqEZlW8GRG5WNnYW7hLbRKHoDfANSlPH9ARdsWEVd7Ejp4bDVw73VpAeu06k3xclmnimEUOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی ایرانی ها خارج از کشور(تورنتو) در لحظه گل اول ایران
🔴
وی سپس در توئیتر می نویسد: دیگه دلمون با این تیم نیست، تیم ج.ا و ...
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128391" target="_blank">📅 10:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128390">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ویزای مهدی ترابی بعد از یکبار ورود به خاک آمریکا منقضی شد
🔴
فدراسیون فوتبال برای اخذ مجدد ویزای ترابی اقدام کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128390" target="_blank">📅 10:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128389">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی دولت طالبان: توافق ایران و آمریکا باعث چشم انداز و پیشرفت خوبی تو خاورمیانه میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128389" target="_blank">📅 10:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128388">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1f670914.mp4?token=IuQfR6vIE3-tA-hOQmmxJ9isn1sO2d2-D7x19f6LPjtqHXjDmNLr5j6EdHyemcJDsdfZj-MuVs4mNSm88_vGNLmEDLMDRDi_y0MrBpAZv_CPy4sRGmZdCR_b7jghMQUo-_a5S5aAhjtOpgBK6SwmmEBSesLk1IEx28z0Cxnb_GzBAE8PaXGXN07LQbINXGbfhTmoKuVX4Ad_A3AhvorB6uLEyDlssvqZ6mPDdsHQr4Kq1eTjd57LMhsKH60hBaZTPQMwXuaSH2YRECATFwXaIlq2OQszOUFjh4Pi2qHZYZAleufY-sbdQoGYrgGBdOniGTWSPiPFkraf81QD-RT7wSS9F3DVmhy7tsdG9tk1ntC7GMMz__-rwBoF8-ZyIFTqBwyE_BvZ-I8NcVbdCPmb_SHFQUHBgvww3KdrCRKzHG6GhX-1n8SDcHsamb6vESfKmDP4_A1iEZrDSOAQF2eIoviQrdRr5Lyil3gAk6KT5sLJu-mcy44ly4Cw8zAvZ9MQh9sdZstyxC_2p9bNLrYPWQTQR4ijLpq4DryLzZKvDxe4DTTYmNea6lYhPUtoxDSEKWbrY5i3-ooY64w-pki4-maDplgv7Esy3NAg9ChJMQtHyHJSVRz_8dzMIy0Rgplz8gwVuNiCjgo5UbsuE1IfSUanrUT29BNz0X3bqDHziUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1f670914.mp4?token=IuQfR6vIE3-tA-hOQmmxJ9isn1sO2d2-D7x19f6LPjtqHXjDmNLr5j6EdHyemcJDsdfZj-MuVs4mNSm88_vGNLmEDLMDRDi_y0MrBpAZv_CPy4sRGmZdCR_b7jghMQUo-_a5S5aAhjtOpgBK6SwmmEBSesLk1IEx28z0Cxnb_GzBAE8PaXGXN07LQbINXGbfhTmoKuVX4Ad_A3AhvorB6uLEyDlssvqZ6mPDdsHQr4Kq1eTjd57LMhsKH60hBaZTPQMwXuaSH2YRECATFwXaIlq2OQszOUFjh4Pi2qHZYZAleufY-sbdQoGYrgGBdOniGTWSPiPFkraf81QD-RT7wSS9F3DVmhy7tsdG9tk1ntC7GMMz__-rwBoF8-ZyIFTqBwyE_BvZ-I8NcVbdCPmb_SHFQUHBgvww3KdrCRKzHG6GhX-1n8SDcHsamb6vESfKmDP4_A1iEZrDSOAQF2eIoviQrdRr5Lyil3gAk6KT5sLJu-mcy44ly4Cw8zAvZ9MQh9sdZstyxC_2p9bNLrYPWQTQR4ijLpq4DryLzZKvDxe4DTTYmNea6lYhPUtoxDSEKWbrY5i3-ooY64w-pki4-maDplgv7Esy3NAg9ChJMQtHyHJSVRz_8dzMIy0Rgplz8gwVuNiCjgo5UbsuE1IfSUanrUT29BNz0X3bqDHziUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میثاقی: پرچم شیر و خورشید، آشغاله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128388" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128387">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بیرانوند قبل بازی:
دروازه رو مثل تنگه هرمز میبندم
🔴
دوتا کشتی رد شد و یکیش هم زاویه بسته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/128387" target="_blank">📅 10:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9jc4itaVIeaMNllw1xDho7iagg67khVLVKABzNtQBAmvz6Lam9rv_35HX0D0_AzFuyOVHNO05nApKu8ifZvD56DuqtEO4tJRjZn4iOaQoGTtrorc4QEXRAvqq9JtXyFaaJPPBJGoJs0ZU_QfZwj2F63TbllPlkzWG_6Km-MyTadcxR9Yt57gq9-a4c3IQ0P35QQWKmwbkZ8kNJvATZ6IkgrpvcRLXqZ3iu44jd5bdBmK_OWpKux6sX75vEhy5NA_Ha3X2vwPvAT44F4LuqDfa_ma-HhFeEC02NIq3JJ2tfkmtnOmrY15CMitfEaH2TjywWD5I_zFVZA15hMD8Vnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de38edfb2a.mp4?token=ZV1ja7GbmqSyJCGsg8f7JxUmM_gadjQ5EWn3RPDZeHPi9lON45CDHGIQYldUwm1ElDHQbkYU38vVq1WZMUoBq3yu5_n-Pmbi6yCBiF3ssNkEvTm3FIJMDtsZA_rMVp2QmZh-iHFxmkDHfzPiRvJA_Al8pBd5Ihng1f9ESARLVDr1Lbf6vvRNDHAwlxdbVEc6QLvzskJXQk8NwMuCUOUGcs6_an5CDTYUnxIao5SPaydXdtM7q3Jbt_OSwPg26EYp5MDb3MkQuhMazByEFqZRCmLRzoHwT3o9nyBdZpDpS6KwLOX6mpik0MGogw6ERErgkFwHL2GltKNrfV3Q_7Oluw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de38edfb2a.mp4?token=ZV1ja7GbmqSyJCGsg8f7JxUmM_gadjQ5EWn3RPDZeHPi9lON45CDHGIQYldUwm1ElDHQbkYU38vVq1WZMUoBq3yu5_n-Pmbi6yCBiF3ssNkEvTm3FIJMDtsZA_rMVp2QmZh-iHFxmkDHfzPiRvJA_Al8pBd5Ihng1f9ESARLVDr1Lbf6vvRNDHAwlxdbVEc6QLvzskJXQk8NwMuCUOUGcs6_an5CDTYUnxIao5SPaydXdtM7q3Jbt_OSwPg26EYp5MDb3MkQuhMazByEFqZRCmLRzoHwT3o9nyBdZpDpS6KwLOX6mpik0MGogw6ERErgkFwHL2GltKNrfV3Q_7Oluw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شادی گل بحث برانگیز «محمد محبی» که با اسلحه شلیک کرد سمت تماشاگرا.
خیلیا معتقدن به سمت کسایی که پرچم شیرو خورشید داشتن و عکس جانباختگان اعتراضات دی ماه رو داشتن شلیک کرده.
برخی هم معتقدن تو خاک آمریکا به آمریکایی ها تیراندازی کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128385" target="_blank">📅 10:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQhO5KFLYbvoiIzVTk8eOQGYH-QMK5adcrw7obvoVB3ToRV7jPi-8ALIVctFCs-FSijBCsfxv8ROePLP2QGMk-emCILfip96N4kOsapdLbN0M2j9k3df6JzYvwbfjmDsFoITp4h6BlGdqRZnxxf3qoKirUXgR2onxS9JohLKjj1wRSInUsuyWLw1h2Ycv-aBrPuvA03-ID3M34qGZxTvYl8M3gWJliY8rcDSqZArVIDxgoptwe42F6aM0JctvLziQ0IfYAmgG9MrHP21jdxdcdG7tZCdsUkwsvFlMGlB3nQVwlzFOxH_2VDhoC1aB6lgO0UX4aPUz65nfJu8GQaK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحقیر پشت تحقیر
‼️
🔴
تیم ملی ج.ا بعد بازی بدون ریکاوری درحال خروج از آمریکا است اما طارمی و الهویی درحال بازجویی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128384" target="_blank">📅 10:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60c66f257.mp4?token=ipvfIQm4pIj3KfT5SsW2JBobuoe8iSvGmuHT6hyXEtczAPd0VvIStEv74F7Y-A_n57XWFfQb28IxApfIjKfTfdb_zD1-_svWamupHo5Cr7dCQn_etyGFTXxscoIYQqVQbE51J-4Zf1kOWcKnE4apd8KUee3j4Bm_N9yEqzG7rzqvlHyiM1EIlIruV4O32RoT2_j_kw58htG6kkgQxJaYmW8ixRcPxkuoBpS2XQSVUncr6izy18GEVhyJAYJXZ-lSDHzjCkujTEXBANfSRH-0JEGQHBhDGoOH-snlh7SB1_EVZa6qylDD7TDm8NT3TC7l9_Dta-BpanDrDbG_4d_o8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60c66f257.mp4?token=ipvfIQm4pIj3KfT5SsW2JBobuoe8iSvGmuHT6hyXEtczAPd0VvIStEv74F7Y-A_n57XWFfQb28IxApfIjKfTfdb_zD1-_svWamupHo5Cr7dCQn_etyGFTXxscoIYQqVQbE51J-4Zf1kOWcKnE4apd8KUee3j4Bm_N9yEqzG7rzqvlHyiM1EIlIruV4O32RoT2_j_kw58htG6kkgQxJaYmW8ixRcPxkuoBpS2XQSVUncr6izy18GEVhyJAYJXZ-lSDHzjCkujTEXBANfSRH-0JEGQHBhDGoOH-snlh7SB1_EVZa6qylDD7TDm8NT3TC7l9_Dta-BpanDrDbG_4d_o8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از ابراز علاقه هواداران به بیرانوند
@AloSport</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128383" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mla52LUxWJ27GNRQcu8e8dQJ-FBmNNLJfRsK93N7LD2CAFNSRLE6S5Zrf7izISQJPVYk_nDI75jk46A_qUQdCEQVX3iAI8U8DkhYiv4HJwnO0z2XwC-pVMnMq4CYXzmu34ZPqMTOwgxmkdyYhxI-Vx7ydmgI3MZaFiHdZwajp8B9kLDQHUxVHAr-04ERCik13pSMX4celq-POsQEqBnuz3s0KQaZfur0zefw4nkwCsuZtQyKGZAZ0seuyDrkiBf3Aj6hGAZv8emh8zoTInqDM2RNrxIL7SIHDugxljlEX2QwQrtY0mUreLN13FEvuN9exnLcSoGczRTxO6JnodO7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیرو هوایی اسرائیل درباره جلوگیری ترامپ از حمله به ایران: تمام نیروی هوایی آماده شروع یک سورتی پرواز رزمی عظیم بود
🔴
عومر تیشلر: ساعت‌ها قبل از دستور پرواز، با کاهش زمان آمادگی، انعطاف‌پذیری استثنایی نشان داده شد و کل نیروی هوایی مسلح شد، برنامه‌ریزی، آماده‌سازی و آماده حمله به صدها هدف در قلب ایران شد.
🔴
حمله در حالی متوقف شد که ما فقط یک ساعت قبل از پرواز در حال توجیه اهداف به اسکادران‌ها (گردان هوایی) بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128382" target="_blank">📅 10:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ در ازای تعهد تهران به ازسرگیری مذاکرات هسته‌ای، با رفع محاصره موافقت کرده؛ این یک عقب‌نشینی راهبردی است
🔴
توافقی که رئیس‌جمهور آمریکا، دونالد ترامپ، با ایران به آن دست یافته است، بیش از آنکه یک پیروزی کامل راهبردی باشد، نشان‌دهنده عقب‌نشینی از اهداف اصلی واشنگتن در آغاز جنگ است؛ زیرا آمریکا در ازای تعهد ایران به ازسرگیری مذاکرات درباره برنامه هسته‌ای خود، با رفع محاصره موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128381" target="_blank">📅 10:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تسنیم : دقایقی پیش، ۳ نفتکش و ۲ کشتی حامل کالای اساسی ایران از محاصره دریایی عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/128380" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
صدای انفجار در دزفول ناشی از امحای مهمات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128379" target="_blank">📅 10:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سپاه: احتمال شنیده شدن صدای انفجار کنترل‌شده در جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/128378" target="_blank">📅 09:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ونس: ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
🔴
جی‌دی ونس، معاون رئیس‌جمهور آمریکا اظهار داشت که رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128377" target="_blank">📅 09:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d96af772.mp4?token=XygyOw487i5VdI92-y-2M-cqy1EIV1H-UppTQQTJgilc6r3M-2XI2J2NgU8WxC04KknaV92Ewf8TqoFdVgGDoNTA-4ZSMPbAOb9qclSQeKZ6u7GmJZvKuaDM03mlR1TPVP57fMuLAqBlw7QD2q4l0dyIqSdjQzBhIT5pegt1PUiMWJH9Ysp4ZY3Wb7J7FLTTUR4p7PK64BNsxOrCNpxu1U2rZ3S-GA45FEXPWEzxejiH1imQyWx75aJVTRjdY-IPRugyDrYhbh51s5FxnrF_I4OyHl5U80_WeRYOi8Ku6JZ1KLdtCxpgjb2fwyaHNPJbPzgaRVr6Az4myljLymA0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d96af772.mp4?token=XygyOw487i5VdI92-y-2M-cqy1EIV1H-UppTQQTJgilc6r3M-2XI2J2NgU8WxC04KknaV92Ewf8TqoFdVgGDoNTA-4ZSMPbAOb9qclSQeKZ6u7GmJZvKuaDM03mlR1TPVP57fMuLAqBlw7QD2q4l0dyIqSdjQzBhIT5pegt1PUiMWJH9Ysp4ZY3Wb7J7FLTTUR4p7PK64BNsxOrCNpxu1U2rZ3S-GA45FEXPWEzxejiH1imQyWx75aJVTRjdY-IPRugyDrYhbh51s5FxnrF_I4OyHl5U80_WeRYOi8Ku6JZ1KLdtCxpgjb2fwyaHNPJbPzgaRVr6Az4myljLymA0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: ممکن است در این ایام با حملات سایبری مواجه شویم که نیاز به مدیریت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128376" target="_blank">📅 09:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
لیبرمن، وزیر جنگ اسبق اسرائیل: این توافق تضمین می‌کند که در نهایت کار به یک ایران هسته‌ای ختم شود.
🔴
من هیچ ادعایی علیه آمریکایی‌ها ندارم؛ برخی انتظار دارند که ایالات متحده بر اساس منافع اسرائیل عمل کند، اما واقعیت این‌گونه نیست.
🔴
این دولت ناتوان طی سه سال گذشته فقط مشغول حرف زدن، اظهارنظر کردن و پیش بردن دستورکار سیاسی خود بوده است.
و از سه سال پیش تاکنون هیچ نتیجه‌گیری و تعیین تکلیفی حاصل نشده است؛ بنابراین آن‌ها باید فقط خودشان را سرزنش کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128375" target="_blank">📅 09:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: «نیروی هوایی آمریکا تأیید کرد که در پی سقوط یک بمب‌افکن B-52 در پایگاه هوایی ادواردز در ایالت کالیفرنیا، ۸ نفر جان باخته‌اند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128374" target="_blank">📅 09:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN7RP_d-EroKXNDVYqht4OWMDe481jqFrhYCUQuOmV-o4Y6kItck_gOSw_sjkg5vMBVfD_ijgsSRlUIMRWMHFC-hejp5EYW8WSX-VTsYweVrWGfi6fAmaVvGqOsNTDFiXI93pl4sIXJijSE7D_djtOvtEz8QPRDwJ09k2y-KUhZwTGj8ifzMOMzAmqUo2rA_ysH75jk1iotWRvoDP4P4Tz4aUxop7hMfCQ7FyZFw7829sMCp9dge1h4fbLBq_qihb7ezZ6-pGsCGxrCOLISY0hrBvpnHibBjxwqaB5rm9v_-E88y2C1Xzqw6LWN_hmQhZ4ccFwlskPxGeeVtieJRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص بورس ۵ میلیونی شد
🔴
شاخص کل بورس ۱۱۶ هزار واحد رشد کرد و به تراز ۵ میلیون و ۹۷ هزار واحد صعود کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128373" target="_blank">📅 09:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maFD3TadCC31xGyust8T52RbA5V2G9L8ldizcJCjsDTB8bTfXxZGeDwvQzeECyXWvajGlovJUq2wegK3MyXUd_T2lSeTgBHoR3hDmtwwVwv9f3fPrSPqH5Yr3Y0dYaE5fNUlRzoYaC7G_777To6rc989_SPsEalYfLsxHxAzl2el6rkXvfQaICzkrLBOih0JTSLvznt0To3oPIAcskK0sNalaB7iVg3JcFGQH1YbU-V9GqZtUWspBh-Rsb6-huRWmBQunUI9GgPF2PS8IsxdwVMGzWVzEvMZS76UeA64dHpfjL8tWzT_gSq2M2NcBmhySGrs5xKlhzh_H3T29AeFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو رسما برای انتخابات اعلام نامزدی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128372" target="_blank">📅 09:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شبکه خبری المیادین از حملات توپخانه‌ای اسرائیل به اطراف شهرک «العیشیه» در شهرستان جزین در جنوب لبنان خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128371" target="_blank">📅 09:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40eb697b4.mp4?token=oLXONFr40sTuCBzTacdncJsZ_ZfIQiDI3m1BBmVLTwqvW9OALbv7WpKkywtNvyfuv-1Nz52w_TatYnSM3tEkQ1Etkf5UsZPiGn4aYwSvbhE7kdicKvI5e7YBa_LseWWRQIeCm1C5ut4oplWP_VrgVrbTAmZAgM2xeiKNAp_ys-4LoTQMSod9K273Z-OF9sIgKKw5S-nHFH8C0BmkjjUOjlO-5jgS1Y9Wh19ssNJnI-YSspjkYixRXBl_l-gPzkQ7y6bHiIzZ8l3Y5rfLqJHvhkbiCyDtJlLqMHnseYfAMwdGksdxB32gu7-v7XZuqoilfYj_v1gXNYdx4YIHi6Ndtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40eb697b4.mp4?token=oLXONFr40sTuCBzTacdncJsZ_ZfIQiDI3m1BBmVLTwqvW9OALbv7WpKkywtNvyfuv-1Nz52w_TatYnSM3tEkQ1Etkf5UsZPiGn4aYwSvbhE7kdicKvI5e7YBa_LseWWRQIeCm1C5ut4oplWP_VrgVrbTAmZAgM2xeiKNAp_ys-4LoTQMSod9K273Z-OF9sIgKKw5S-nHFH8C0BmkjjUOjlO-5jgS1Y9Wh19ssNJnI-YSspjkYixRXBl_l-gPzkQ7y6bHiIzZ8l3Y5rfLqJHvhkbiCyDtJlLqMHnseYfAMwdGksdxB32gu7-v7XZuqoilfYj_v1gXNYdx4YIHi6Ndtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر بهداشت: سالانه ۲۰ هزار نفر از جوانان خود را در اثر حوادث ترافیکی از دست می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128370" target="_blank">📅 09:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vie8GSmgw6kEfRIGm0JeOM2dxPRUEf3XI0dLa3wMZm8YcKHaUMy2wZE01tAqK0Zj0-O6SJ8m-vnVshuAvCYDd9Vt3aPJbwHguPn6GWKo6ShZELGFR3apDzplRenDjvcBLe1ukKjwxMluxkN5LmUzsQVOoXDcrwyKDTY4AHsiVf2HeFGK_lJVnPMykdmLw5Z7ySSt0j3-wpE6jJot_6oyIym6RMK3MZxU0Pm18mDtgXRC5TFXcC2hwp3VOyr2dehbEcjYI0pyl3EIsskoGbVUk8SjS_X2hlQrPs4MnEJciO3Msw1y2ggbsKSoKwxYI7zK08XvQiEk9dapp74ff75oyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94357192f3.mp4?token=svCq7wVzR183dOdgvZcQsRnsbg0Jv3J1szvJhJgWHs1yCdaFua9DnZ6BBKpeUoPVPUA-TUMWoFpJM7IcLWzF_wSNM886lYEPUZOMl4r782dLnn7eTnGCxOGvjY7uUDXo4HBFj9vIH5JhEj8q4wphja_DWwbu23M9BbkNkBAl_UajrnzFP8vRsEUejOD5oLpP5na8aevVISW1vGocjnpZ4pdft_s6s-507biBDHsoeRsnjTibjOaxgNXnQpn8od9nosZf_N5oWECCOGbep85FN27lZO670bqB3-1YtUI0hGQDuH-LAxHyXj3G52LKv0MuV_tSau6o_7_lmdeIQt7SMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94357192f3.mp4?token=svCq7wVzR183dOdgvZcQsRnsbg0Jv3J1szvJhJgWHs1yCdaFua9DnZ6BBKpeUoPVPUA-TUMWoFpJM7IcLWzF_wSNM886lYEPUZOMl4r782dLnn7eTnGCxOGvjY7uUDXo4HBFj9vIH5JhEj8q4wphja_DWwbu23M9BbkNkBAl_UajrnzFP8vRsEUejOD5oLpP5na8aevVISW1vGocjnpZ4pdft_s6s-507biBDHsoeRsnjTibjOaxgNXnQpn8od9nosZf_N5oWECCOGbep85FN27lZO670bqB3-1YtUI0hGQDuH-LAxHyXj3G52LKv0MuV_tSau6o_7_lmdeIQt7SMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه‌های مسکو بار دیگر در مورد حملات پهپادی اوکراین قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128368" target="_blank">📅 09:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128366">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ysm_zNEM2tcZ0t1_LrIl3oTVVGf5Qf34odrIUo0fKguzKeNQYky5qnhwH7vcIURH2UTlgeyvmHlA_CgIaEuFi9VQ7yHp2ikVisVendNpMp_iXld6rRYpA09fHZ6EP4fyfSRJT8a77AZ2ViIOzq3cKTJzBiNbSgogiXIoTkvOYlxB_Dw0mI-uoO6w0VW6ql4EUg-1rC1IPjOtyJ7qHnCsfwf3dK1DuKims4eInSoJ4tz77slJexXnYizylZ8oaOaR1hdRkKjUZ0TTdVbzwlW2XmCsTByLcLI7f2Ncfth5-4HqNd3dClCqhjZ9l9cPPDrEYq7TOQ0MbEJKH6Op4qEyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتظار می‌رود مالکان کشتی‌ها از ازسرگیری عبور از تنگه هرمز برای چند هفته خودداری کنند تا زمانی که توافق آمریکا و ایران به عنوان یک «ماده» واقعی دیده شود و به طور کامل اجرا شود، طبق گفته مدیرعامل شرکت Mitsui OSK Lines، جوتارو تامورا
🔴
او گفت: «آنچه باید به اجرا درآید فقط یک توافق ساده نیست... بلکه باید واقعی باشد و به وضعیت‌های واقعی در تنگه هرمز ترجمه شود.»
🔴
تامورا افزود که ممکن است «حداقل چند هفته یا اگر نه یک ماه» طول بکشد تا اعتماد بازگردد، و اشاره کرد که شروع‌های نادرست قبلی باعث شده اپراتورها محتاط باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128366" target="_blank">📅 08:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128365">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX-6i-L36itnoV4TjpbX7zKMOPXbQCsHlOVpO4U_CPDdUctQ-gSg-2X5QNI08sDDPu-dGqln0-DnePivJ6PVy6Q8ctq_WNgbBrxAtWf0dK8SA6AHsr54HMSQ7bj9xBrIauP52HrAywtIN61A3_aF_6gU2w_XrTdjngnYLJrK3IX4fXGgUN-NNg_jAh0HyUBseqJ7JYnnB2df0q8oxjMKJpeIdp-b1ne499mC-k9OtFL8m-0Grggj6ZW2trbG1mF-CFuS7D-hyhWVXk6BdCATp7FaSykICgDDtRHU-Qh6AC4R9U8hupZBCAHDSHHwXuOGFO1eU_YmmtF5WSliH1BTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، بن‌گویر، پس از مواجهه با مشکلات در دریافت ویزای آمریکا، سفر خانوادگی برنامه‌ریزی‌شده به ایالات متحده را لغو کرد، طبق گزارش هاآرتص.
🔴
بن‌گویر قصد داشت به میامی سفر کند تا در عروسی دختر یک تاجر اسرائیلی شرکت کند، اما این سفر در نهایت به دلیل مشکلات ویزا لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128365" target="_blank">📅 08:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128364">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyyoG4TlWbssKqdjwjrw2yTS2t8AwILBImKyHne2A-Agy0NQ6lwoRC_cPz1Q-ZUHSaYEhxv3gkpKg1yDlrwNBMiNXgx7QKaA_el6aIEVF3U_DWRFPo7Tf3maA_J7QbuE61NfN8xiPclFkafKaxwqK42I5S4HlQwP5A7kJuEdX37kEBiVI2Chdg7SGOSHFPt82X7HyCs7iKj4Hw2BMMCKe2DPC7svAd2HdQGRH3IjZkUA2fVSEZbF6MRThYtBKODFVPh06uURBw7IXC21q77uKh5ZUDTyM4d0gOfVM-6WtNrV4nkFmiDYawVmklO-42_IXSPfSN-2tBWmcFD774ZVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس : جان راتکلیف مدیر سیا به ترامپ و دیگر مقامات ارشد گفت که اطلاعات آمریکا نشان می‌دهد ایران قصد ندارد در صورت رسیدن به توافق نهایی، به تعهدات هسته‌ای خود پایبند باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128364" target="_blank">📅 08:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128363">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
اعتراف هولناک مادر به فروش ۳ نوزادش / از شوهرهای صیغه‌ای باردار می‌شدم و فرزندانم را می‌فروختم؛ این کاسبی من بود!!
🔴
مادر ۳۴ ساله: از ۱۶ سالگی به‌زور شوهر دادند، به مردی خلافکار و ۲۰ سال بزرگ‌تر. بیشتر وقت‌ها زندان بود. بعد از طلاق، در خانه‌های مردم کار می‌کردم و فهمیدم بعضی‌ها چقدر برای بچه داشتن حاضرند پول بدهند. همان شد جرقه کار.
🔴
تصمیم گرفتم به‌صورت موقت ازدواج کنم. صیغه مردی می‌شدم و بچه‌دار می‌شدم، بعد به مطب‌های زنان می‌رفتم و با زن‌هایی که حسرت مادر شدن داشتند حرف می‌زدم. می‌گفتم شرایط مالی ندارم و اگر کمکم کنند، بچه را به آنها می‌فروشم.
🔴
بابت ۲ نوزاد اول بین ۲۰ تا ۵۰ میلیون تومان گرفتم. نوزاد سوم را ۱۰۰ میلیون فروختم. فکر می‌کردم با این معامله هم بچه‌هایم خوشبخت می‌شوند و هم آن زن‌ها به آرزویشان می‌رسند.
🔴
شوهر صیغه‌ای‌ام فهمید بچه را فروخته‌ام. دعوا کردیم و من را کتک زد که کار به بیمارستان کشید. هر مادری دلش برای بچه‌اش تنگ می‌شود، ولی آن موقع فکر می‌کردم چاره‌ای ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128363" target="_blank">📅 08:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128362">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سخنگوی سازمان ملل: ما نیز متن توافق ایران و آمریکا را ندیده‌ایم، اما مشتاق دیدن آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128362" target="_blank">📅 08:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128361">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNSV4SGJL8YDi8uf7IGTvaS06Ia_9hruTW2PHf3QFeu3yVAlsMk3uypwzpEGAdk4GeO_WwCSWPCrXdFI2ioQVZWna-rsgLj2OPvTVDD6HzWyfjJyWflfSJkTfImK8f7sDviBKZUPXY_GX7KBDZYXqVAd7f5P9XOGFYCfp4Kxjtynij5OlYKzebTB-VRl6_Ol_V8aA2aUk22Qplaxv_aMhZsUy_dVi5tPvCpTbk6UTMjdUK6T1Zn8FuhC7boF1V264AU2WfEB1h3dA_Qx-A9w9fhdjVLuH74fywUoNkrS6Ho6w2DPJilWcNbS1_wv-e7BxDeY5pRABzu3InhA-6j-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همتی ، رئیس‌کل بانک مرکزی عازم مسکو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128361" target="_blank">📅 08:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128360">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
یديعوت احرونوت: هر عملی از سوی "اسرائیل" علیه ایران ممکن است در واشنگتن به عنوان تلاشی برای مختل کردن توافقی که ترامپ به عنوان دستاورد شخصی ارائه می‌دهد، تلقی شود و قطعا به نفع نتانیاهو نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/128360" target="_blank">📅 08:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128359">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارش FT: دولت ترامپ آماده حمایت از صندوق ۳۰۰ میلیارد دلاری برای ایران به عنوان بخشی از توافق پایانی جنگ است، مشروط بر پذیرش توافق جامع هسته‌ای توسط تهران. یک مقام ارشد آمریکایی گفت واشنگتن درباره رفع تحریم‌ها و ایجاد این صندوق برای بازسازی کشور مذاکره کرده است، با این شرط که ایران توافق‌نامه‌ای را که قرار است جمعه در سوئیس امضا شود، رعایت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/128359" target="_blank">📅 08:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128358">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8miuoo7bd0R5Ve5DAlLf9Nki0Jvn6QiPwvh_Wmfk2omkze2xVbrOCViSfq4lqReZteOPTIzEeNWRMv5nOZUJ5Os1NKAJ871UbokJo6ROLDOekYwWUMXCFMmlUYye0Ou8ZGpwk8XJS0Dzovf3IkBZjcJy-wMxvNxWF7NVo1YE5jVlZZmOhxJkzxLNN6D2xSuSNsMGDZO9A94pyZxfZRnXhri7Sg-zhLO6PYrL57klo2CrDm9qDLxAsDHh0PDmvVKVlwZXXlxqDIGJUrZ690ZA8DMGHw8PGom5zDpJHPV0JaEe7PZXl4d1AJy8TxJsmvHID-AUeRqZHGTxMMyPE7UrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت عضو کمیسیون امنیت ملی علیه سخنگوی کمیسیون امنیت ملی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/128358" target="_blank">📅 08:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvQFQrd09QjOduXEquOpSMrwxa6Ldb_Lixh13xw9d3MtqYFZwZIyjfvDJ8k_pwYprrwajqZkHY3WPH-hnPJaO4GClcjIJHGyNbGPn3b9K5UjeSKlBQyeooPy4a7HcRU5Y6BF2_RdgvbPeOvzMXeQyqfCIlKTQ715q_2R-PJMzjhGCi11F4cnKjT6Gv-O_wHnhzUHV_dMXkSkT_Uef5QoUYvCPsiVxuSnatQTg5sSJSjPQcwgUlUcx6Ypqi9acdZjWB9hZrunRaYItPPIORZ8EnQmRPlagCNSUb8sjhIld16Fn0zcG8a3AO38Z2BlQdLNsiCThWdAQKimcP1vt-cUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد.
🔴
داستان پرداخت ۳۰۰ میلیون دلار توسط آمریکا به ایران، خبر جعلی است که توسط دموکرات‌ها تبلیغ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/128357" target="_blank">📅 02:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مسئولین امنیتی ورزشگاه So-Fi (محل برگزاری دیدار نخست تیم ملی) دارن تمامی بنرهایی که عکس مقامات سیاسی کشور درش هست رو جمع آوری میکنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/128356" target="_blank">📅 02:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rLV8ireufCibsPgVt7WWfZjuePROIOKUuDc4xaxTaUCWs04C7uybD2U8bCxRBNKA53K5l3hohEk5ZRhm_aPPZA6RFkI_oRzauNlK5S9xPYl4re4oMtx6_C57T-QiswwIbAAdB2vS9rztIrlP7O3wTEYdIIzLiilAPom_Vp1m6o1VDLDs1enDyrNuHvGORozHrqFZEBoOatMQrNJtV-Mi2aAK8Zs35AaNdejf-kkxuSo6M3-sfZD_ajESDF5AQr_-EBY35UZZDLRMFARnR-X_-834Oey0vIF_fW4km5cZ8JxHRJU1ssV4VIt6lMHgJMlV_KUxZuv5hIB_I1a5FxRQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V7ebOT-2yGsh26_AMGjNytu3Fi3nKC2mEj9_sjtxVGqg0nCmtdYw3liF2_xowEHUCDt-m_gw1DpKn-nbKn28wS17pqDttcSTMzWVTGVUAV5U5kUmGKULuCB-D1brLGpiLiAkJJzsvoYi6226lzwZdsQk0LGER73-uu0zTppcrJf_vlYb9TUv6R8T6rnryMECfhErmi9pwfXuqUoScY_yVJITrYBEc3CsCkj-Zau_kSV6NUAxsMg0xfSEA7OGGW69FyY5fEPreENlM4H1myAK9mgmytt2Sm-lqeif20BToqAPKxiKXTGJKIMkKCsqpnXhXk_v97o_qYdNEB27eNKdrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا این برنامه قراره تو استادیوم اجرا بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/128354" target="_blank">📅 02:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67b749fc7b.mp4?token=M3_yiO_ZEv8RcfoMGU1YncLlQGRXjDiSOFU50aHlOsZOk7n64-UdwEcyLtC5iaZDa66LR83-cgdvQpxpnCMM8Pea3BTI_fg5ikgmcYiSRp7EF_1iefZpNFmgwmJPNCiIRTcHEG9QQOCx_JgIDcAg1JVfS7c2NyW5RugCse5Oki5iCUFr4-5kIhvKLv9nHWJolgR5Nw3lOF51OwSvQ2x3cl2o0hpLdPZHyU0p0TTTjKZVNk5ydetx22OL-tDUV6uZ2lOwtw34NAb9Pz_qRqxd47tKMtaLblAYDPuPnK6K-Zg1_aUFzvSaDxQjswwPkYADj0W8ZeKuI4iMU9OCIxfRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67b749fc7b.mp4?token=M3_yiO_ZEv8RcfoMGU1YncLlQGRXjDiSOFU50aHlOsZOk7n64-UdwEcyLtC5iaZDa66LR83-cgdvQpxpnCMM8Pea3BTI_fg5ikgmcYiSRp7EF_1iefZpNFmgwmJPNCiIRTcHEG9QQOCx_JgIDcAg1JVfS7c2NyW5RugCse5Oki5iCUFr4-5kIhvKLv9nHWJolgR5Nw3lOF51OwSvQ2x3cl2o0hpLdPZHyU0p0TTTjKZVNk5ydetx22OL-tDUV6uZ2lOwtw34NAb9Pz_qRqxd47tKMtaLblAYDPuPnK6K-Zg1_aUFzvSaDxQjswwPkYADj0W8ZeKuI4iMU9OCIxfRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع ایرانی‌ها با پرچم شیر و خورشید اطراف ورزشگاه
@AloSport</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/128353" target="_blank">📅 02:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8e3f17e9.mp4?token=PL_-Zk9wwyP-R8YmwJU6NBMxpuNwWvreQoWNEHDeoPGd57Go1OadpyNtbTuHzb8ZvTdCZH1C053rOeNd7MkCxFncPlX5uOX4_FDVQGsjObpc6VQxg_RZRt2RvqjvjjWcyFU6DynM84SSU1A9dk57U2rQSSb42L4KAbw8wt4Nmng8sl4xhO4Ln-3BTYMWBb1Wp8XAZuvJtVRnVuze7aVyPvCWYLF3iaDA-P7lV9zaLHYh07Rj6caCWGYiaA0LfrUTNWan3MmIUpwDqR0NDdZKuzbWi2WIMtCcYn4h41e9DClrZBBQyvlqyPzPD7DYhRwB0yJObVv72HF0OooMj78wKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8e3f17e9.mp4?token=PL_-Zk9wwyP-R8YmwJU6NBMxpuNwWvreQoWNEHDeoPGd57Go1OadpyNtbTuHzb8ZvTdCZH1C053rOeNd7MkCxFncPlX5uOX4_FDVQGsjObpc6VQxg_RZRt2RvqjvjjWcyFU6DynM84SSU1A9dk57U2rQSSb42L4KAbw8wt4Nmng8sl4xhO4Ln-3BTYMWBb1Wp8XAZuvJtVRnVuze7aVyPvCWYLF3iaDA-P7lV9zaLHYh07Rj6caCWGYiaA0LfrUTNWan3MmIUpwDqR0NDdZKuzbWi2WIMtCcYn4h41e9DClrZBBQyvlqyPzPD7DYhRwB0yJObVv72HF0OooMj78wKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارهای مخالفان جمهوری اسلامی در اطراف استادیوم محل برگزاری
@AloSport</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/128352" target="_blank">📅 02:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128351">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اکسیوس:
در تفاهم‌نامه‌ی ایران و آمریکا بیان شده که
ایران با عمان برای ایجاد چارچوبی برای اداره آینده و خدمات دریایی تنگه، با مشارکت سایر کشورهای خلیج فارس، مذاکراتی را انجام خواهد داد
تا به توافقی مطابق با قوانین بین‌المللی و حقوق حاکمیتی کشورهای منطقه دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/128351" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62ec6f238.mp4?token=YGTaz3Lx-sfeCViFGzQth3eyZhr2Nd7FGFXJ1dTV0b-9AvwMUkWuv87LpegYmzOo3bwMAzd15Q_Ldj7Km3-7tJ4dq2AXgle9wwjOC2qFpuAei4yr04kda4NftXygtLRu8cuhmW_MzUfl23KnVL6Qwwuceduhrz2IsYg4yilKeQEcXzcHbAoHaPNrSjzI7vrMwQ9hDyvbyEOT8PBLyDqfuTeCgg-vFICntpmpNdJMDSz237A2pBcxuXM23q9uVyTGUemTu4EvxJbpKnphqsHACtV_JGANOlByrqdHQrXY31pFc3CipXl-wKq0Aah9CnAuil3sG8MVmUgp-q0w-FHIMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62ec6f238.mp4?token=YGTaz3Lx-sfeCViFGzQth3eyZhr2Nd7FGFXJ1dTV0b-9AvwMUkWuv87LpegYmzOo3bwMAzd15Q_Ldj7Km3-7tJ4dq2AXgle9wwjOC2qFpuAei4yr04kda4NftXygtLRu8cuhmW_MzUfl23KnVL6Qwwuceduhrz2IsYg4yilKeQEcXzcHbAoHaPNrSjzI7vrMwQ9hDyvbyEOT8PBLyDqfuTeCgg-vFICntpmpNdJMDSz237A2pBcxuXM23q9uVyTGUemTu4EvxJbpKnphqsHACtV_JGANOlByrqdHQrXY31pFc3CipXl-wKq0Aah9CnAuil3sG8MVmUgp-q0w-FHIMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش سی‌ان‌ان، هشت خدمه در سانحه سقوط بمب‌افکن بی-۵۲ در پایگاه هوایی ادواردز جان خود را از دست داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/128349" target="_blank">📅 01:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS_HDsV4-9499--7pCHYU-t3HaV4tW_9TGMPYRnLS-38tK1BY7vfdcMY76vaenHCLMaYmUOgegzKFBdBGzyUhjo3GE28OexyonJr4W50VooTvxRZiK2bpTSWbI4UMFzJzb7mgsJbnV3oRXryL3Z-loPvOwEqeUoX5R4ljdGaaO5QtdVw9Ja1PVKrRs90cZx1MI6Bma8BE4eIkvAsrQ0JeXUnx8FlpLUj-VGdo4zlOJilLZeq_Ipy4ZchGTlKsMkHXyJ1i-uheQG-0OPsc-P1pfyTndxvupa4m8BfqHmLMkjfoXsMnLtMagFLX-pyjm6GuqqoJVqH8tl1aTaI434pCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش فایننشال تایمز، دولت ترامپ آماده است تا در چارچوب یک توافق نهایی برای پایان جنگ، از ایجاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری برای ایران حمایت کند، مشروط بر اینکه تهران یک توافق جامع شامل توافق هسته‌ای را بپذیرد.
یک مقام ارشد آمریکایی گفت که واشنگتن درباره تسهیل احتمالی تحریم‌ها در کنار «یک صندوق بزرگ ۳۰۰ میلیارد دلاری برای بازسازی کشورشان» بحث کرده است و تمام مشوق‌ها به «عملکرد» ایران در رعایت تفاهم‌نامه‌ای که قرار است روز جمعه در سوئیس به صورت رسمی امضا شود، وابسته خواهد بود.
این صندوق تنها پس از یک توافق نهایی و پس از تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و ادامه مذاکرات درباره برنامه هسته‌ای ایران تأسیس خواهد شد.
این پول از دولت‌ها تأمین نخواهد شد، بلکه از شرکت‌های خصوصی علاقه‌مند به سرمایه‌گذاری در اقتصاد ایران تأمین می‌شود و در صورت لغو تحریم‌ها، کسب‌وکارهایی در اروپا، آسیا (از جمله کره جنوبی و ژاپن) و ایالات متحده ممکن است به آن علاقه نشان دهند.
ساختار و مدیریت این صندوق پیشنهادی هنوز نهایی نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/128348" target="_blank">📅 01:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7cAZEDpPQ8xnmcCnm-jtp_0s2WUgXObPATgdx_F-_wSEJqfuB7_i3InuHNLftOaoQI-6xMGGOQXL7xhd7hhvfitPNdRPO2r2NzzJSF9_dgt8bnpynNiWaFbRtSu0kKfPAoaT05MOBl_uDwb8i6CNy2VD55AJoR4WyoTnqyZoVN-soumeQvc916D1yOgacOUvi03SkvhcLtwj-AaHp8DAka4Eswzs6Q4TtJ-Xfmzs_PNODF24mQULWcy216xv2cNVPFzOtTpuku1EqgsMi_pyx9vZhb3t3Wa8h4b_vFnAo2NLLky09ZRnFY0CQddXX7uxf64BLn_ga-j3JYlCLhodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
11 جنگنده A-10 در راه برگشت به آمریکا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/128347" target="_blank">📅 01:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 دوست دارید کی ببره؟</h4>
<ul>
<li>✓ ایران</li>
<li>✓ نیوزلند</li>
</ul>
</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/128346" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3033df34c.mp4?token=PjpCtna2ur58QgD1AeBtcJOHiqCUftLAVjqJ7iyNjCc_wrSkEIKWU0F1I1GyhifT9XXkjj1TSIyF65BlfMr4N_a0QP_51IuXO8MHRaRv52pxnS6JOueFTANTL_gWaRALxBloNS6bnx7lGxm3vGH_aARiGxhN4dnalSFHohGfkwy8ZEptK36C2rTjw-3scSubR4B4Mf2WtDXD67Tv8oT1gmzQMM2j46uB_rEJzPONAMJINWZfP1M3hbJrNWHIarKkl0_nMH0NRASBQNknJpOE_MjppZ_t5ffDF0-6FIW7xkROCxMCqAZqSDy0waa1aichI3HPfWsRU1hBMkJeE2o1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3033df34c.mp4?token=PjpCtna2ur58QgD1AeBtcJOHiqCUftLAVjqJ7iyNjCc_wrSkEIKWU0F1I1GyhifT9XXkjj1TSIyF65BlfMr4N_a0QP_51IuXO8MHRaRv52pxnS6JOueFTANTL_gWaRALxBloNS6bnx7lGxm3vGH_aARiGxhN4dnalSFHohGfkwy8ZEptK36C2rTjw-3scSubR4B4Mf2WtDXD67Tv8oT1gmzQMM2j46uB_rEJzPONAMJINWZfP1M3hbJrNWHIarKkl0_nMH0NRASBQNknJpOE_MjppZ_t5ffDF0-6FIW7xkROCxMCqAZqSDy0waa1aichI3HPfWsRU1hBMkJeE2o1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : هیچ دلار تخفیف تحریمی یا پول بلوکه‌شده‌ای، نه از آمریکا و نه از هیچ‌کدوم از متحدای ما تو خلیج، آزاد نشده
🔴
این امتیاز فقط وقتی بهشون داده میشه که به تعهداتشون تو توافق عمل کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/128345" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
درگیری عجیب ایرانی ها با همدیگه درنزدیکی محل برگزاری بازی ج.ا و نیوزلند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/128344" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ونس معاون رئیس جمهور آمریکا به سی‌ان‌ان گفت: یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
🔴
یادداشت تفاهم چارچوبی را ایجاد می‌کند که به ایران اجازه می‌دهد در ازای ایفای تعهدات خود، مزایایی به دست آورد
🔴
ایران باید تامین مالی سازمان‌های تروریستی خشونت‌آمیز و عوامل بی‌ثباتی در منطقه را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/128343" target="_blank">📅 00:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuC4y-NHYUURGzX9lC3YZhiz-4ikKG0SSAbepu45WXKICUqHaYAl71eBAupDkLEGK4nAT_Q4seR4EAJg6XYaZ6XvjcMVkQyhXpmGhak2PnYBsbfSZT4tb0OqeFcb9HWqxtqGiU4bavxcBh4AfteaWJM_G65voF-1xzU3s55aSlLgT7sjf24qmXVOhtAWiL1KmjQxAPn9oeDO7n593ZfMgaA3S-TpXF1gVLPe2ITwM2yAj_FsrEUkmDfykJA3taMgnzcawLcFJmuTnMjxc5CXAgjrBXaaks9sSIv83EGIOOuJBOi6e-PvwWbhhYeIoG1ABi51mBjXix9FcQTFysJxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شجاع خلیل زاده:
ایشالا امروز پرچم جمهوری اسلامی عزیز رو بالا میبریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/128342" target="_blank">📅 00:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj0O40JclRZfMsEb2kZ8xp6gwY9EdpfrOduKgUGWExTJaldp6xr_7sZY9LrRS0GN3qqF_pdPlhSMJsgs0ZpvVyRqwW6mKYrY-HBDqeO4QGDWedh5P5j-hzFV0bTWREhrf73y1RuTgMiYZa2_xAogoRjdGdkqfDiceuc1AwAy5_imjgdtHaycXUF_fXmEtkoSbngquuSgyzu7YLlk99Kd_7OE7oqpcri_Qq_PQ1PnMVe7xMpo0msch8_s_h3ZD6zM9q7k6o8dq3_5FKM_PJMjbqZZdUQnXlu9iTCQpW_yk2hxm65QJKlTJ-r9178DPO73FSydVc1t7qOT2rtaz2Ki8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در خبری عجیب و به گزارش خبرگزاری MSN، به مارکو روبیو و پیت هگسث گفته شده اگر با توافق با ایران همچنان مخالفت کنند از مقام خود برکنار می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/128341" target="_blank">📅 00:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">😁
هنوزم ۱۰۰ گیگ و ۲۰۰ گیگ رو به اسم نامحدود میدن؟!  اینجا نامحدود واقعیه
😎
💯
🚀
یه ماه کامل با خیال راحت استفاده کن بدون استرسِ تموم شدن حجم
💎
❤️
فقط گیگی 5 تومان  نامحدود هم 200 تومان
❤️
👇
👇
👇
✅
@TurboVipV2raybot
✅
@TurboVipV2raybot</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/128340" target="_blank">📅 00:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUb_peLu0E-gPlbqCqrv5dTZzQPLzqZs2_CnnbBuD4QrSxB4LqgkDqCpw0tWlt_lTwbLzAY1JPgD4mpPcT829R38OpNqREtFvqGGsxgYMlUjKH2tSVK7JUEIkYgv4dI4NBrJURnCHRM6rKbu4jB5geevEVMvIFYp5FjmMWVhei4XKlPdjJERcNFQdlnw-Bry3Vk_KVzxTK-uuEP7MS5Ssu8F2WCxN1Q0Y9F9VuQZXax7AzCVk3S2IS8WYc_Z_ZB2bbzaKu7wpo7manrQ4Rb_TA1whBOgi5IWfJYfN8FwVaq0XweovYVeMkdlDN5w3PpSIjTbbS-CWdCEf1_HufzFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
هنوزم ۱۰۰ گیگ و ۲۰۰ گیگ رو به اسم نامحدود میدن؟!
اینجا نامحدود واقعیه
😎
💯
🚀
یه ماه کامل با خیال راحت استفاده کن
بدون استرسِ تموم شدن حجم
💎
❤️
فقط گیگی 5 تومان
نامحدود هم 200 تومان
❤️
👇
👇
👇
✅
@TurboVipV2raybot
✅
@TurboVipV2raybot</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/128339" target="_blank">📅 00:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMJzPfZw71h0zNXV_2K14VFKfI93fOr4Cz1vpuhXfwSulUlr00b6htRL2d0CV2zvP-KSX7JkaAXe3WyziOX80kZNR_Tj5y7UfCbXKHD2-ucUv4okcZ0GakfVdds68mC4JNW9-JoYa0RFoGjeH6Ly5u2841OCqt4yLMK9xxayC_l3kH5qgvjTd8z2rD7U5yN4DdefTM2LLxPMWiTI9M78CJBSql_ATbbgipIszKiG3ab8W1Ted9Sy6hPH5KnzMb7SXjJ0FSfmwUXIxot7Pa64kX792eoXOlXpPaOqLz0ECJiILhkr5FbEJU3uvmzQdF4LalNw7JKvhc_U1NtVkzpvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو :
من هیچوقت نگفتم هدف عملیات سرنگونی حکومت ایران بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/128338" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG3Et_EBVrUU76GjeS9WdyDHC7ATGE7z5gZ_6PP0NEeECRAVUiqYZ8tfEFgup7_sjGlU4LV_lfn4zzr-4aHOdKUHl6GUUKPr4zGybbgzY-Tnz_xN4LHxCd3Zc_MQ0FcaWK61diIxMIDntHsV3fusfMLlnSyj8vnLpxecUbAvobSEIP0x79Un4HSKCfPujdJxUN5fgY_NzRrHWVfLYq17m5cHPbtjJjo7dlQRiVymIAP-It_UjaL9CFol23YdSWGv2QJMKgyFEZsVlDhcAeAAFcUShFYF8GoDFrafSkILHlH_7w1a2KtYHqOjbBuZ-lW2MelFFDT6cef3L5OgyBXxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرس تی وی: ۳ نفتکش و ۲ کشتی با کالای ایران از محاصره دریایی عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/128337" target="_blank">📅 00:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / خبرگزاری تسنیم : رفع محاصره دریایی عملیاتی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/128336" target="_blank">📅 00:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZGBJvzI13zdIph0Jjsf7uisPgrJh5XEoQgdgs74QXV8a7gdten34tAAf7JVtFwnWr0daX_YLe9ux4JVAxLyRyTRF1k449YBSsA7npwKEg5WLQdajHBcpYxXUvBpzRyd-qUnayPY0tqQb2rCoDc8B3m1vrDT6yR1Z_tSwyPt1ZIKpavzZ4Brthkc6Zuht7gtaw1QMnnvxCm4cqn41rmyJMb9ppb7EtJojqrZO-3SF637wWt7zBAKIX7NA14mbxDYSyo7X4_Jjeahhx9whVfS24XqIvegdSAOEgD6P_ls0MObCqineqXnRZRL_0d4Vh7WbbiZSorqD2ilap3Fi_Lfxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار بعد از مدتها، هیچ پرنده آمریکایی در آسمان خلیج فارس نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/128335" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ گفت تنگه هرمز تا روز جمعه باز خواهد شد، در حالی که یک مقام ارشد آمریکایی به خبرنگاران گفت که بازگشت به فعالیت عادی حداقل دو هفته طول می‌کشد.
🔴
ترامپ همچنین گفت که متن یادداشت تفاهم (MOU) بعد از روز جمعه منتشر خواهد شد اما آن مقام گفت ظرف ۲۴ تا ۴۸ ساعت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/128334" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
الجزیره: اسرائیل بزودی برای نابودی توافق آمریکا و ایران اقدام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/128333" target="_blank">📅 23:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128332">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVOeRGeE6oC2F_VAAJNqT8CqCwW6FIHreU6-tnIiqJFIS8brxtEI3dxM-8MjlkrPUXCrM6-DdN_JVVdfaCcG9jBK02jFmwQRzB-NtMFJZ0OkcOjuvwr33FP5Vb-jhCQnakVSjw9SGWzGBWlEdcFpOJ3lSBVV4vyQ_ePy5ikdqIRNP1mUKOklbpv9IF_pUCH-Kfoy7949CcOREBX3YYVLAxHIkqWoooX2FwDkLRdxn7aEzG1mAo13cQ3x7z5C-NIBI9ZF0yKcQBav7rbjOaaYS7OCAf1zohEma9KfcelgiZ8BHmtuL8fTALdQg9eVbdccRS-bkQsXshhV0XxMVM5ypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری ناراحت کننده از وضعیت این روزهای عمو قناد، مجری معروف برنامه کودک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/128332" target="_blank">📅 23:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: تعجب جامعه اسرائیل از این بود که مقامات ایران قبل از دفن علی خامنه‌ای با قاتلینش توافق کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/128331" target="_blank">📅 23:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حمایت ویژه سردار قاآنی از قالیباف، عراقچی و دیگر اعضای تیم مذاکرات
🔴
فرقی بین تیم مذاکره کننده ما و بچه هایی که پای لانچر بودن نیست و جنسشان از جنس مقاومت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/128330" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/128329" target="_blank">📅 23:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل قضات دادگاه نتانیاهو درخواست نخست‌وزیر برای کوتاه کردن جلسه فردا را رد کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/128328" target="_blank">📅 23:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نفتالی بنت نخست وزیر پیشین اسرائیل:
بر خلاف دولت فعلی، در انتخابات جدید اگر رأی بیاورم به صورت خیلی فوری اقدامات اصلی برای تغییر رژیم در ایران را انجام خواهم داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/128327" target="_blank">📅 23:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سردار قاآنی: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و اگر لازم باشد برگ‌های دیگری هم رو می‌شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/128326" target="_blank">📅 23:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128325">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سردار قاآنی: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و اگر لازم باشد برگ‌های دیگری هم رو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/128325" target="_blank">📅 23:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdnPmEyP9AB_kw4nJEQCS1KaYTB84uSzqbkbHYyHB2-ueJUNzPSSbOmK9Cd45jjMDrO1m5NAZiptwcTfxKJJSQeyFXcrJauF55_HUml_3Sx698n-5X6LyNFDSvsVtON5Vxod6pduXEeBi17CIBACxBlUFnYTPwr5tl-NpIKtq9HXoTWoPPfl4VS6C4T7V_4zUE6XUPpMDNiQvXwDuJemMVpsmZwuARMr_EtZ3WXpkpbtokJecXry45qJYFyrufbJykZVff4Z5r8Ac-u4i44DLl-XqE-TX1jfJmGpv1Mk1SLgEIffQlg9m1SssyrQy771dYUMS3JLmrDxPgA073oDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان از قالیباف و عراقچی قدردانی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/128324" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی کمیسیون امور داخلی مجلس و شوراها: انتخابات شوراها به دو ماه بعد از اعلام رسمی پایان جنگ موکول شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/128323" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آکسیوس: توافق ایالات متحده و ایران روز یکشنبه به صورت الکترونیکی توسط رئیس جمهور ترامپ، معاون رئیس جمهور ونس و رئیس مجلس ایران، محمد باقر قالیباف، امضا شد. اما بسیاری از سوالات حل نشده باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/128322" target="_blank">📅 23:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/128321" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128320">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی ارتش: ایران در دوره اجرای تفاهم یا توافق نیز به تقویت قدرت دفاعی و بازدارندگی خود ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/128320" target="_blank">📅 22:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9EVlUthK31FlNIHSd3eGO0BaWYvhdidgTUWEG9jFoF3E931fm6jyNeogo7ouoP2m9FAlHpxBLfgHYHafknb7tYmCJQ4fPuksd9MwwYLEyguDHEfPXKVAXrfofduoMWjjcINFq1bUVIq6IbVUbrW8_J-t5GiNVP-XZlWTf8pIfMavKfrgd-44gtmlPUuWofkEHYZJ4zAnbyjq8SCRKgqn1AVkBWp_DEqut6LrWsmgJp60LGvIMZu3ZDYHzprka6Hxi99rLTNzZPSYqWbLBaMsObWhSnhE9cQYoP6zrY8C2ne0XuQ92KLHr1ToMeSNUsJz-yDdfRQkfqGp-Kz6JVmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceLwZDgXkl3LHxFOK84L6GHmLWwxZknbpKc9m_PEXKQMHmkdzhXH3QK9UMoSNj_A3iBKs7KlEftJJyyPvP3fjDvrQJWH158Nvir9Vx8lz5EpMtpSaA3lu9CpYLfW6bJqcGEZu2Cc737w_LmzVeuKpQ06ANjIKM1MNEA5olnXQDsX3AIQoHdmAU_igYUbsFoJPbUpxGWeq2v6nQaNS9ATsjK1yh-z1ad6y9cVklcSpx-mm-eKPPFaoHeiEqkyDEEk3k8p1c2Ezxjz8dcWVkRf5uXym_iSBJj4qKt7bT3MGxvZsFClh6nO3p41qXve0kcvJuCsVH1kJrfqRIzplxK2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPJ1cmVlF-kV5X-Vm1fL7Db2KxPNcPjALAmXo0ciI4VDF9ibZitp29k_6da3K0tqWR_hX0oQ9FZ4hyXKM1lLvvjmHp4zi-BoZd1_NanzvUXSDD63PbzlKVnttUZ32dBYCc3X5y6HY4qm4T4p7qN2SRa7il3n8jNj6Qs0xyIZpmSkVnXZ_vnxNr-k3HCwnPtL9XVeNL2nmrwOOs6fJbqEBI2VJSE8eBvJ555ZGzM7aoJcrkrtot2MDUo1gQ6HjZrJ8A2xMT39R0MzsUSU539Hy_j3dTYzbx1icRhGx-KrMl0xn2NhtEWlsFfponVO5c_rILZuIQ4uoX2rp-1cDtKzig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
🔴
جزئیات تلفات هنوز گزارش نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/128317" target="_blank">📅 22:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fea3f1828.mp4?token=UjriWRZqZwFQ9_AW9Iz1BcuZK5sUxywyeiT0n7IHDgIIqzCK7YNd23lrp9Ta7A9duMhAB0qcCaJquypdDlA9cxvf-MqKO8MFWwueZ6uhQTII8SdByrpyLcBXm-SswLuHnNrDDUcWqIf0FpfHubB-nSNP3pdIh6VdzSddbZjE6rLismURHRPtAQCMaDu-DDtA7buGMNDChC115NVuKcfwq7n9cAYHklBmAE7rq8PZys_AusAiJucLbMGIEHuk4rHjOIIoDZ2iBU5454udsvAkJMO-APJ1LPBNJe0gBDPyjmhMDbn2LFL1z9NTlrXsnNrX8xTS7_U9TfgtSK2W90JMNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fea3f1828.mp4?token=UjriWRZqZwFQ9_AW9Iz1BcuZK5sUxywyeiT0n7IHDgIIqzCK7YNd23lrp9Ta7A9duMhAB0qcCaJquypdDlA9cxvf-MqKO8MFWwueZ6uhQTII8SdByrpyLcBXm-SswLuHnNrDDUcWqIf0FpfHubB-nSNP3pdIh6VdzSddbZjE6rLismURHRPtAQCMaDu-DDtA7buGMNDChC115NVuKcfwq7n9cAYHklBmAE7rq8PZys_AusAiJucLbMGIEHuk4rHjOIIoDZ2iBU5454udsvAkJMO-APJ1LPBNJe0gBDPyjmhMDbn2LFL1z9NTlrXsnNrX8xTS7_U9TfgtSK2W90JMNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
عادل: اگه تو مرحله حذفی به آمریکا بخوریم میتونیم ببریم؟
پیروز قربانی: خیر!
@AloSport</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/128316" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری/حملات توپخانه‌ای اسرائیل به ارتفاعات علی‌الطاهر در نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/128315" target="_blank">📅 22:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bdb7c0670.mp4?token=cdGz_0vGx9Qu1vzSTvsSF1S-QPr6og8OOVvEG7gW4HgUcSfxSTc6LrAh5E5OYkBwhSLhpzKpkvhFLkOhryAgDfhAWYYEG-txM44ZIfz9HT_QHqBRHsDuIunSfm6CIagOTxkfXxVOB4lXiD6IEaMA162qR13dZFynwDOjv4Ro0rjt8DW5mjpBvjtVZWEBytRXgsaOELf1-1CFMeYjRBOKrsAHbBGmHEXrkIOLr_-VaHVLVLK70elJIMlkgQ1mVSmIYtA90gjdy2bVlrfO7jpL-mNK33nGAUuoB0Hsied1UpXuziro6slB16OUNgHjpb4tPLgbj1AiL6XRW4BihMN4Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bdb7c0670.mp4?token=cdGz_0vGx9Qu1vzSTvsSF1S-QPr6og8OOVvEG7gW4HgUcSfxSTc6LrAh5E5OYkBwhSLhpzKpkvhFLkOhryAgDfhAWYYEG-txM44ZIfz9HT_QHqBRHsDuIunSfm6CIagOTxkfXxVOB4lXiD6IEaMA162qR13dZFynwDOjv4Ro0rjt8DW5mjpBvjtVZWEBytRXgsaOELf1-1CFMeYjRBOKrsAHbBGmHEXrkIOLr_-VaHVLVLK70elJIMlkgQ1mVSmIYtA90gjdy2bVlrfO7jpL-mNK33nGAUuoB0Hsied1UpXuziro6slB16OUNgHjpb4tPLgbj1AiL6XRW4BihMN4Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده اف/ای-۱۸ هورنت از پایگاه هوایی MCAS میرمار در نزدیکی دریاچه ریمرک، ایالت واشنگتن، در حین تمرینات دیروز سقوط کرد.
🔴
خلبان به‌طور ایمن بیرون پرید و سپس توسط یک معاون شهرستان یاکیما نجات یافت.
🔴
سرویس جنگل‌های ایالات متحده به آتش‌سوزی ناشی از لاشه هواپیما پاسخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/128314" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128313">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c4ddc193.mp4?token=p6bGodMVxnIZVCPBMzsac4F386gje1ISRoyrIayswGVeByFjEWnF_mJkPjSQCQi1uNEB3cEj7CkTtJExhI6XM3HBw7EIFihAycvuBzx6Bu1w656Qix9QXkcFriQ0SFehTgdkq8J77UrXsyI8vm_PMw7afdsgALDxBwurzkqA66zjyrtqWH3I1jMMRJZto48HW0njJDaLqpm7Grg9kYDIUryGTuKSRSU3HKzJjsWF9DxMp4Kqm9rBd4PoNIEwoSjPU8FDalAQIyJlY0PL122bDdjYBrE_U1uW72ENI3AeBTRX_T3ppNhRsl5mIk0H9tF_YZ5yjnsMoAoQTDJymV6qAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c4ddc193.mp4?token=p6bGodMVxnIZVCPBMzsac4F386gje1ISRoyrIayswGVeByFjEWnF_mJkPjSQCQi1uNEB3cEj7CkTtJExhI6XM3HBw7EIFihAycvuBzx6Bu1w656Qix9QXkcFriQ0SFehTgdkq8J77UrXsyI8vm_PMw7afdsgALDxBwurzkqA66zjyrtqWH3I1jMMRJZto48HW0njJDaLqpm7Grg9kYDIUryGTuKSRSU3HKzJjsWF9DxMp4Kqm9rBd4PoNIEwoSjPU8FDalAQIyJlY0PL122bDdjYBrE_U1uW72ENI3AeBTRX_T3ppNhRsl5mIk0H9tF_YZ5yjnsMoAoQTDJymV6qAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر صنعت لبنان: درحال پخش شیرینی
🔴
خبرنگار: «مناسبت چیست؟»
🔴
وزیر: «آتش‌بس»
🔴
خبرنگار: «گام‌های بعدی پس از آتش‌بس چیست؟»
🔴
وزیر: «از سفارت ایران بپرسید»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/128313" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تسنیم: در صورت جنگ یا ترور در ایران و جبهه مقاومت توافق نهایی انجام نمیشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/128312" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری /شبکه ۱۳اسرائیل به نقل از یک منبع: تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/128311" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نتانیاهو:  توافق با ایران توسط ترامپ انجام شد، این تصمیم او بود و ما منافع خودمان را داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/128310" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نتانیاهو: همانکاری با غزه کردیم با جنوب لبنان نیز خواهیم کرد،همانطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست حزب‌الله نیز در آینده نخواهد بود
🔴
ما در منطقه حائل امنیتی در لبنان باقی خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/128309" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نتانیاهو:  من در انتخابات شرکت خواهم کرد و قصد دارم در آن پیروز شوم.
🔴
گاهی اوقات بین من و ترامپ اختلاف نظر وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/128308" target="_blank">📅 21:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نتانیاهو: ایران به سمت دستیابی به سلاح هسته ای حرکت می کرد و ما توانستیم برنامه های موشکی و هسته ای آن را نابود کنیم.
🔴
ترامپ رئیس جمهور آمریکاست و من نخست وزیر اسرائیل،من مسئول امنیت کشور خودم هستم.من از منافع اسرائیل نه با غرور و خود‌خواهی بلکه با خرد و عقب دفاع می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/128307" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نتانیاهو:  کسانی هستند که می‌خواهند دستاوردهای ما را کم‌اهمیت جلوه دهند، و ما به دستاوردهای بزرگتری هم دست خواهیم یافت.
🔴
ما استقلال خود را در زمینه تسلیحات تضمین خواهیم کرد و نوآوری‌هایی را توسعه خواهیم داد که به خیال‌پردازی نزدیک‌تر هستند.
🔴
من بر منافع امنیتی‌مان در روابطمان با ترامپ و ایالات متحده تأکید کردم
🔴
وضعیت ما امروز بسیار بهتر از هفتم اکتبر است و ما محور ترور را در هم شکسته‌ایم.
🔴
به وضوح می‌گویم تا خلع سلاح حزب‌الله،اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/128306" target="_blank">📅 21:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نتانیاهو:  ما نصرالله را کشتیم و از حمله به جلیله جلوگیری کردیم
🔴
ما کنترل مناطق کلیدی در لبنان را که حزب‌الله از آنجا اسرائیل را تهدید می‌کرد، به دست گرفته‌ایم
🔴
ما دکترین جنگ را تغییر دادیم و سد ترس را شکستیم؛ ما ابتکار عمل و غافلگیری را در دست می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/128305" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نتانیاهو:ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/128304" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نتانیاهو:  ما خطر نابودی اسرائیل و ساکنان آن را دفع کردیم و آن را از ویرانی نجات دادیم. مبارزه ما هنوز تمام نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/128303" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
🔴
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/128302" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دلار 155000شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/128301" target="_blank">📅 21:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
یک مقام آمریکایی به رویترز گفت که خروج از لبنان بخشی از تفاهم‌نامه نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/128300" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
