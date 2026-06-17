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
<img src="https://cdn4.telesco.pe/file/t_JGijPVxfoAic9UHVfeniCbkNjhuumzMhPmE6MZlNq-oMSvyaDOmQ2J12JlMXbCCRGlt4kvg2zVExm-5S5IHuS9bECXYXnP9wYT4cGFMsLpfj36KYMOCiPtontSKq8pmHc78wImwtFMY-JzzfW10gCB4NOm4SUmIEB95Zl9hWiUfU0SX9dJJwo6ehn8iAeN3FJU9zyTJWn05wq57Zb21VJpLFGF87pbS5DglFKgFestckVkC1KfcCkhyoSCNzKvD_a6NOz4eFgWQtvb6mfLIlJPWNiIOMx5L9BHBvRPRjdQDnSnTNWx2qEHnOliQZC2HPSS4x-0hs1l4ewDT9e2wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-128759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک مقام کاخ سفید: به همان اندازه که ایران به مسائل هسته‌ای پایبند باشد، تحریم‌ها علیه آن کاهش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/128759" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm_z8W0f_6N_4YLU9ExbjGAcfM2MR_PVhf4WGMt0jK2qmrYwN18P64d_9RYvlKBYWdzgsy20WJrZVaJmei7SU8CR91GUpCH7sPw6OhjglDHn4yhFrYyz0HBuwN1Qljj6oP_NLG21da4WGJPcuTr1KgvT4QHF7kRSuE_srPfDPxK2b_3wjB7QEQ9CfjZ7x8x4UOFi022FeP3kKxXqrDBrD8l4IP4xly5LH0HdP6dz_GDhj_9Q65C5YDo-7GI_IQworSs3gwjUiXlag80LGi3XjubWgqqdzzFmrW5oDSpO73Ty_CosxzPY3VG89YnwTqvq94Ywyza6rCN47vA5MiPmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا گزارش می‌دهد که یک کشتی در ۱۰۵ مایل دریایی شمال شرق عدن، یمن، امروز زودتر مورد حمله قرار گرفت پس از اینکه دو قایق کوچک حامل افراد مسلح تا فاصله چهار متری نزدیک شدند و آتش گشودند.
🔴
تیم امنیتی کشتی پاسخ آتش داد، که باعث شد مهاجمان حمله را متوقف کرده و از منطقه عقب‌نشینی کنند. خدمه در امان هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/128758" target="_blank">📅 20:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری / تسنیم :گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/128757" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f24117a830.mp4?token=fr3s8bXAOeDqMRt6tvctC5BhDNzF4D33DXOIESDOvhhjkPupIy2Rq4wR3BUfu7EIWkhAMwuZ_fu8_cAunDJRBgVyBwyQdhjTKj1oGmoeVobRKPndwCNHM8KmqWYIQq0wctRB2VVWVXqn_8lC4uVatkrM6HJAePQNybo2DrCJpxbuXjNQdMWQ77ZSrJh7lbaLh_cIM4k54TLK1bH6HYn-r-t324Y_dAdgci74fKI60W3loeLHkHXZhC2OTTSDLeXWZ865KNOAlrx4fTvOYqvMTv0u_uLuoZUDgU0rV7E1g0ELgvzWJS8QqH4q4Z5nt16242s-JaxPN2llvvoxKwvC7X-eO85QHkz42kou-fGmtRwuAvCedH4m8LnWX1ql4Jcu7maAKqRpxM9ri2t1aj-tXM8jLp2n30EpaB7PyIf_akYvk5UHIeJ4ES2jXRZwDAwZ_7rlwX14dwJ_kIl9Q4GWoJWW7RtSb5UZuoCQn_tR2J1ZSwdfZBDUyt60SqZdPkJc5G91JiUDSrkr2BFz1Uh1ccIKntPAYo-GUhCK895Ob8d9Dk0zOeG6AITGeR_YAB_69rV5ijMdMb8lisLE50JKDtGdeKEg1HQM88mhonI0b9xZyX87vFJdm0RrmV4xE7TqAsHlKeKfhnsHFt4yRPuO9GhXBN9N6QWiRpuvuIQmfy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f24117a830.mp4?token=fr3s8bXAOeDqMRt6tvctC5BhDNzF4D33DXOIESDOvhhjkPupIy2Rq4wR3BUfu7EIWkhAMwuZ_fu8_cAunDJRBgVyBwyQdhjTKj1oGmoeVobRKPndwCNHM8KmqWYIQq0wctRB2VVWVXqn_8lC4uVatkrM6HJAePQNybo2DrCJpxbuXjNQdMWQ77ZSrJh7lbaLh_cIM4k54TLK1bH6HYn-r-t324Y_dAdgci74fKI60W3loeLHkHXZhC2OTTSDLeXWZ865KNOAlrx4fTvOYqvMTv0u_uLuoZUDgU0rV7E1g0ELgvzWJS8QqH4q4Z5nt16242s-JaxPN2llvvoxKwvC7X-eO85QHkz42kou-fGmtRwuAvCedH4m8LnWX1ql4Jcu7maAKqRpxM9ri2t1aj-tXM8jLp2n30EpaB7PyIf_akYvk5UHIeJ4ES2jXRZwDAwZ_7rlwX14dwJ_kIl9Q4GWoJWW7RtSb5UZuoCQn_tR2J1ZSwdfZBDUyt60SqZdPkJc5G91JiUDSrkr2BFz1Uh1ccIKntPAYo-GUhCK895Ob8d9Dk0zOeG6AITGeR_YAB_69rV5ijMdMb8lisLE50JKDtGdeKEg1HQM88mhonI0b9xZyX87vFJdm0RrmV4xE7TqAsHlKeKfhnsHFt4yRPuO9GhXBN9N6QWiRpuvuIQmfy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا بخشی از این موضوع این است که معاون رئیس‌جمهور را می‌فرستید؟ اگر جواب داد، عالی است؛ شما به خاطر فرستادن او نابغه به نظر می‌رسید. و اگر جواب نداد، تقصیر معاون رئیس‌جمهور است.
🔴
ترامپ: این ایده را دوست دارم، حتماً. به این ترتیب، اگر جواب داد، من اعتبارش را می‌گیرم. اگر جواب نداد، تقصیر JD است. بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
🔴
بله، این ایده را دوست دارم. فکر می‌کنم ایده خوبی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/128756" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=O94S9aOxrsEsbiUAc4tj2xXRUYIxFtlPFVkZn6PRpyXhKkDJ9rqPhn-Nys_MeqOixFI6ISykyFOtmUWgSMBpdC9ZQ2zgqIaYR7E-mwV4xY41LXoba3_7Ns5GF0fpqoSVFnf6ETQ3IyKQptDE9qM_YyZEYiaVtEUVPRhsC2QDl5IfqKlw95EJ1z9PLItjoiyrYn459W89FHcLdTiapuTffh7wNjjMrIe18DHcVnBlwg1Gc2hjfQHtF48uRf_aDTvCWTgoeG0BFk0P8N3msZ_IaZ9P_YeECXOEE-B_ITRYbofMaP5afeI1S8b_fDgQO51GS9Urn49mfJzD_DkI8QS2BirdT7VnHSZh_LYGSZKeefd78snBIe-Q_PmdzW5bdcIXnndxzR-SCRlEHzS04iLTh1sXmP9DOvne0XO-VM8lbkypoiVLCC51hrZ5tpUT4oEdQDdkuPlS-YVXn2Id-cQZYIHke89yELa0LNZnMrdg2aYunF21Ha1TdPv4cbaGvAjbeY_fEtnksJYV0aZJcR8kCwRG2w7Nxxc_FYMvyK5xs6LkWVKbm4ZWq5uxo3fOvY7j6ZxP7e0QLjhUbfrYoM8LWxGweHp9okc63j8gdrgFKAuFUzn0pVfaNtFNvO9T2tLpI77xHhFMvtkJrcNghx5GEqxXrPbgigQy_BBHdIAUUW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=O94S9aOxrsEsbiUAc4tj2xXRUYIxFtlPFVkZn6PRpyXhKkDJ9rqPhn-Nys_MeqOixFI6ISykyFOtmUWgSMBpdC9ZQ2zgqIaYR7E-mwV4xY41LXoba3_7Ns5GF0fpqoSVFnf6ETQ3IyKQptDE9qM_YyZEYiaVtEUVPRhsC2QDl5IfqKlw95EJ1z9PLItjoiyrYn459W89FHcLdTiapuTffh7wNjjMrIe18DHcVnBlwg1Gc2hjfQHtF48uRf_aDTvCWTgoeG0BFk0P8N3msZ_IaZ9P_YeECXOEE-B_ITRYbofMaP5afeI1S8b_fDgQO51GS9Urn49mfJzD_DkI8QS2BirdT7VnHSZh_LYGSZKeefd78snBIe-Q_PmdzW5bdcIXnndxzR-SCRlEHzS04iLTh1sXmP9DOvne0XO-VM8lbkypoiVLCC51hrZ5tpUT4oEdQDdkuPlS-YVXn2Id-cQZYIHke89yELa0LNZnMrdg2aYunF21Ha1TdPv4cbaGvAjbeY_fEtnksJYV0aZJcR8kCwRG2w7Nxxc_FYMvyK5xs6LkWVKbm4ZWq5uxo3fOvY7j6ZxP7e0QLjhUbfrYoM8LWxGweHp9okc63j8gdrgFKAuFUzn0pVfaNtFNvO9T2tLpI77xHhFMvtkJrcNghx5GEqxXrPbgigQy_BBHdIAUUW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دووسی از فاکس: برای مراسم امضای توافق صلح ایران می مانید؟
🔴
ترامپ: شاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/128755" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: رئیس جمهور چین به دنبال کمک به حل و فصل اوضاع مربوط به ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/128754" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/128753" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: به محض اینکه ایران اقدامی انجام دهد، تحریم‌ها اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/128752" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=aSpK1nLgXoMLsPJqqeskY9XkccTulMB0q9JFo5Q_82jgYU6gmWFoiI2Y-RKUxhL28xmU4tbF0_XGTdDFRwNHc41nVCMkVxPjATemTpUoFtGVueFW9cBYe9r0bQISRyL7Gj93SOyLEZCyQrpQno3lB9Ja3KWecZ2Td7O9PFrHr--Xc9dJoSY4nDUKJw70xg6OoILZ9Y2hWfAYolOsSAObH5EM3n87irnA23x0MPDwEpzOkYglQxk8oT7QkABIn2CVsNzqJxNn2LiXczEkwqj7Eu2OVXcqB-UCJNyUiT3DZE2VrUvOVsRdA4PeYgi5eC1DPL1_XtO18rXjbBU3PyPz0mRldA9gS45f2MK1_IGZz3ARW3LlAPNpjfDKtBIM8TY4s2FZV9q59aG95H2WnU4dOZK20cgeSvJBvJ58m3Xk7SUZOIDYyWuiMBe-BvotBEbXo63ziqZN3kLX06c0O63b_dM1tTwrKKkETds5QiV9jUinO4sMs3_oqxentyGHNfg7YfbrNvFO-oHB8QY1x3iE0jHiS9qZbEB4NVt55q4OwQcJbUpsjhLuQorftfjG49xdmkXH9UrwH0RoxMojj7AQsFHinGJaNUH5xAk-TroEeptFVEK9eBZW3ilOEGVx919jyuh9u2IdnFZ0oFf3xOMgTVND31qVnt1X1acMCppopxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=aSpK1nLgXoMLsPJqqeskY9XkccTulMB0q9JFo5Q_82jgYU6gmWFoiI2Y-RKUxhL28xmU4tbF0_XGTdDFRwNHc41nVCMkVxPjATemTpUoFtGVueFW9cBYe9r0bQISRyL7Gj93SOyLEZCyQrpQno3lB9Ja3KWecZ2Td7O9PFrHr--Xc9dJoSY4nDUKJw70xg6OoILZ9Y2hWfAYolOsSAObH5EM3n87irnA23x0MPDwEpzOkYglQxk8oT7QkABIn2CVsNzqJxNn2LiXczEkwqj7Eu2OVXcqB-UCJNyUiT3DZE2VrUvOVsRdA4PeYgi5eC1DPL1_XtO18rXjbBU3PyPz0mRldA9gS45f2MK1_IGZz3ARW3LlAPNpjfDKtBIM8TY4s2FZV9q59aG95H2WnU4dOZK20cgeSvJBvJ58m3Xk7SUZOIDYyWuiMBe-BvotBEbXo63ziqZN3kLX06c0O63b_dM1tTwrKKkETds5QiV9jUinO4sMs3_oqxentyGHNfg7YfbrNvFO-oHB8QY1x3iE0jHiS9qZbEB4NVt55q4OwQcJbUpsjhLuQorftfjG49xdmkXH9UrwH0RoxMojj7AQsFHinGJaNUH5xAk-TroEeptFVEK9eBZW3ilOEGVx919jyuh9u2IdnFZ0oFf3xOMgTVND31qVnt1X1acMCppopxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره افغانستان: ممکن است تمام تجهیزات را پس بگیرم... افغانستان دارد به ما چاپلوسی می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/128751" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=W-6vfFR_Iyr0BzpdJcScMExJfbEEYr_TNRtTvVe-gc3jNfIzmzRB0awJRH4dsOpEYoX51tdfyKcI_XI3L9ByI0_1rwjuuqR4me61phW7UO91rEyXBcJWiKLg1Qxhy8GCP_R8Ywy9wnbyuSQsuoRBPU9zFe_-MUz5v-GjtmYy0KLbo2QX8vcynOqK5St-FbOJEcPL2HtcvIlsO1n6VIpXFpRY4sVPt-_IIA8XNOP58oGXxBiUBTCUxdhRnNiJ7nPDIDHsZEwte5OuoeIWSTf2v-uRt7yKJ1cj-O9fos9vluM713R8azvgqLJ2-fV0YdINEsdbcVtoIM8kp2ahnC6X0QtU33Z9jfCi1qoAEiF2fMeRn1w2EJfWg5-Sc8KdmRmqkwKrx_mNEDudbf0CiCbeXykF2WWaA03a6m9a3dSjfm5Z7uW3sSwpMB1u287GgIbVKuHYOeAc2Yvg_qrQUss6nDpKyQLdrfaoFCx7FpxB2PqeG_Sdo5VixZ3OlK8Ymcv0kO6fYUrBwnb8kdKELrlkIgttlba_Vyk4Kr0tYxrP-NV4VweJtvOaK4rQ5GtliEZ-MvLr2gBB1ehz94cbmCnlW057FIDXxGNP74xO8i1VE1lB93ypetYvFrFmEAE_Y1oyd-KSO-XTgshT5N_cnTTW-1jFhghRZUI_UNMx3Afa7KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=W-6vfFR_Iyr0BzpdJcScMExJfbEEYr_TNRtTvVe-gc3jNfIzmzRB0awJRH4dsOpEYoX51tdfyKcI_XI3L9ByI0_1rwjuuqR4me61phW7UO91rEyXBcJWiKLg1Qxhy8GCP_R8Ywy9wnbyuSQsuoRBPU9zFe_-MUz5v-GjtmYy0KLbo2QX8vcynOqK5St-FbOJEcPL2HtcvIlsO1n6VIpXFpRY4sVPt-_IIA8XNOP58oGXxBiUBTCUxdhRnNiJ7nPDIDHsZEwte5OuoeIWSTf2v-uRt7yKJ1cj-O9fos9vluM713R8azvgqLJ2-fV0YdINEsdbcVtoIM8kp2ahnC6X0QtU33Z9jfCi1qoAEiF2fMeRn1w2EJfWg5-Sc8KdmRmqkwKrx_mNEDudbf0CiCbeXykF2WWaA03a6m9a3dSjfm5Z7uW3sSwpMB1u287GgIbVKuHYOeAc2Yvg_qrQUss6nDpKyQLdrfaoFCx7FpxB2PqeG_Sdo5VixZ3OlK8Ymcv0kO6fYUrBwnb8kdKELrlkIgttlba_Vyk4Kr0tYxrP-NV4VweJtvOaK4rQ5GtliEZ-MvLr2gBB1ehz94cbmCnlW057FIDXxGNP74xO8i1VE1lB93ypetYvFrFmEAE_Y1oyd-KSO-XTgshT5N_cnTTW-1jFhghRZUI_UNMx3Afa7KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128750" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ درباره ایران: آیا اجازه می‌دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/128749" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گزارشگر:  چرا اکنون برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
🔴
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از سایر کشورها دارند.
🔴
ما احتمالاً ۸۴-۸۵٪ از موشک‌هایشان را از کار انداختیم؛ بقیه زیر زمین هستند؛ حتی نمی‌توانند آنها را بیرون بیاورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128748" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ZSzXmGUzXMFJOs-RGpUntrh9ed00kH9CS-MPi0AKJzm8LAD94ZdUwjCGtGkpf8we5c3Lcm04qMD8bfaRlELIXuye_AQNe-S3ijdE4art32z57jvgn8EhXwU_CqiDqrHfAC2MPGcE4s3i2dRYSVxwiMr0eJdwgSN7HHg5BfxND1kGr0gmggAKTy87Bk_QwbD8le7sAItF3G0VJYdqvaXVPjqzHjFbVQa9L_cWL1-SrwJtzMO6Lh4IJBHPDAbn0gCsf2kCykI2EIMA3y9GHEP_VPsCScfmcBosZxo2W_Ry8pafOGW06nT-E6N0mLMtl21vyEULlxzlSjLH-gh8cmWApxbwi0vrzMPVlvvHoO52dvBOLaYoL6RZjhFiPR9p_sl_iaewEteTQ-8Cd-tVP00S1Q3RsssoDRahLOTQRo0YxewAUFsWX7XmTp6SZCK3sLQGwKEG7Xc_c0FOinhzWzqfVGt0oCM2xyMAlu5rFLTsvo-3z5MM0XXzCIjKZkVea9mWixxRox-zm87768OUJ5bVvnJEw0N0Z3FVX25VpcI8Mv0wAT9T95IJEBdi7u7tQDheoTV4bYCDX95WtULE0AQfOXAWmBnu7QeJTYBo5bYQpgJ4zUEC8qFFC9lNADCFhkwwD_xqco7GbKQmobgz9zb5a0m6ReU5czL8i38pOpqvRHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ZSzXmGUzXMFJOs-RGpUntrh9ed00kH9CS-MPi0AKJzm8LAD94ZdUwjCGtGkpf8we5c3Lcm04qMD8bfaRlELIXuye_AQNe-S3ijdE4art32z57jvgn8EhXwU_CqiDqrHfAC2MPGcE4s3i2dRYSVxwiMr0eJdwgSN7HHg5BfxND1kGr0gmggAKTy87Bk_QwbD8le7sAItF3G0VJYdqvaXVPjqzHjFbVQa9L_cWL1-SrwJtzMO6Lh4IJBHPDAbn0gCsf2kCykI2EIMA3y9GHEP_VPsCScfmcBosZxo2W_Ry8pafOGW06nT-E6N0mLMtl21vyEULlxzlSjLH-gh8cmWApxbwi0vrzMPVlvvHoO52dvBOLaYoL6RZjhFiPR9p_sl_iaewEteTQ-8Cd-tVP00S1Q3RsssoDRahLOTQRo0YxewAUFsWX7XmTp6SZCK3sLQGwKEG7Xc_c0FOinhzWzqfVGt0oCM2xyMAlu5rFLTsvo-3z5MM0XXzCIjKZkVea9mWixxRox-zm87768OUJ5bVvnJEw0N0Z3FVX25VpcI8Mv0wAT9T95IJEBdi7u7tQDheoTV4bYCDX95WtULE0AQfOXAWmBnu7QeJTYBo5bYQpgJ4zUEC8qFFC9lNADCFhkwwD_xqco7GbKQmobgz9zb5a0m6ReU5czL8i38pOpqvRHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند، «سپاس خداوند را، دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است؛ ما کاملاً تسلیم می‌شویم؛ کاملاً دست می‌کشیم؛ این جنگ تمام شده است؛ ما شکست خورده‌ایم»، نیویورک تایمز و سی‌ان‌ان و چند رسانه دیگر خواهند گفت، «ایران پیروزی بزرگی کسب کرده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/128747" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ : ما یه میلیارد دلار بمب روی ایران ریختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/128746" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: حادثه مربوط به حمله به مدرسه میناب در ایران هنوز در دست بررسی است و اشتباهات در جنگ اتفاق می‌افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128745" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=nZN30oqSiFXm0cJIrDoNv4Wj8FL7zPaIErIqLY_TSSSd4q9FAVgts8lS21L1z5VB30wp56B4piJ4kelVy50hpXxIEubuLBx9Leai9-7lOiC9ucK7bAbDhx9FsCtuhPbn4kLOZZgNGOHBz_HEoDP2JdDl5uI_B_3kwEvodKbxF6MQCCjH_XzWmeyywTQYZuVFRxkaaSwQzLZNFZP1oNJ0MEPgVb9OQXZxlHrilefmcdx-V1ClHMP0YHCzWIaUpCpdjf7w6LVMm9Q08wBZxxkB9WN38Qdk99nAEPHw-jhGNxhozrI7XZx5GHNmKrNyZuuFGbH1axYFomNeHuLN6WANcX7mS49psv4WzdZZKKvWxDTXldXdZyDPAXytjRaOiZERFBzrMMQLe8UkbtaqJtM0keGqQVw9_-tPHYwvd8yLgF6iMckm0qYCvbnTXLKEW_ugqx677QheMQfvOsLIqLQO7-2xEMeCgvgaomLokeSa-rAEkEpY5kN5upa8dxxY2VBMkvGFDlUKzK1vm48umC_3_sA_kL3_V2bNrdR5AUvlCp0ZFxOix8nE0kMTp1UdMqxiYrNx-ZljJGzIk-Pq-i9ubDKT8AM4VmaZkcOKBQwvQH09gtaA_Y7aDFrlmiPnnPJ-3UU_uUu4RC0iE7kl12agGqn6JRtO6RmrTwBzc4KZymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=nZN30oqSiFXm0cJIrDoNv4Wj8FL7zPaIErIqLY_TSSSd4q9FAVgts8lS21L1z5VB30wp56B4piJ4kelVy50hpXxIEubuLBx9Leai9-7lOiC9ucK7bAbDhx9FsCtuhPbn4kLOZZgNGOHBz_HEoDP2JdDl5uI_B_3kwEvodKbxF6MQCCjH_XzWmeyywTQYZuVFRxkaaSwQzLZNFZP1oNJ0MEPgVb9OQXZxlHrilefmcdx-V1ClHMP0YHCzWIaUpCpdjf7w6LVMm9Q08wBZxxkB9WN38Qdk99nAEPHw-jhGNxhozrI7XZx5GHNmKrNyZuuFGbH1axYFomNeHuLN6WANcX7mS49psv4WzdZZKKvWxDTXldXdZyDPAXytjRaOiZERFBzrMMQLe8UkbtaqJtM0keGqQVw9_-tPHYwvd8yLgF6iMckm0qYCvbnTXLKEW_ugqx677QheMQfvOsLIqLQO7-2xEMeCgvgaomLokeSa-rAEkEpY5kN5upa8dxxY2VBMkvGFDlUKzK1vm48umC_3_sA_kL3_V2bNrdR5AUvlCp0ZFxOix8nE0kMTp1UdMqxiYrNx-ZljJGzIk-Pq-i9ubDKT8AM4VmaZkcOKBQwvQH09gtaA_Y7aDFrlmiPnnPJ-3UU_uUu4RC0iE7kl12agGqn6JRtO6RmrTwBzc4KZymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: مرد خردمندی یک بار در ژانویه ۲۰۲۰ گفت: «ایران هرگز در جنگی پیروز نشده، اما هرگز در مذاکره‌ای شکست نخورده است.»
🔴
پرزيدنت ترامپ: کی این رو گفته؟
🔴
پیتر دوسی از فاکس نیوز: دونالد ترامپ.
🔴
پرزيدنت ترامپ: آها، فکر می‌کردم می‌خواهی همین را بگویی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128744" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2ObcdBq1P9Xx2TmqbKAZIRqjeAcial3gSKb5EhUb35QG4Z9FFDn3UDYdoPBZLTSKHXentJtpG2J4-ZylFB9jm4h_X7d8q5GlqzO8RsAhu7h7hac-vQD_7p17tftaNCotbNMToPHR8CE1NM0f5ZkwSC7-f0BlfeZHiWCQ2ufaB7GJeqtVeaE44fDrj29dW3WQvSVactaCeVrG8p5lRhcIkunTUlCFkrg2dessm4tmLoMG3II0u9RTfdzrmrcGkgoHz38-fTwMw0Yt03lH_Ewbq0PEa8elDlJck6B8R2-KFztdhIP7TkaLPsC-gVQ-hVXDJuWylknEuPus015f1sJi2e9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2ObcdBq1P9Xx2TmqbKAZIRqjeAcial3gSKb5EhUb35QG4Z9FFDn3UDYdoPBZLTSKHXentJtpG2J4-ZylFB9jm4h_X7d8q5GlqzO8RsAhu7h7hac-vQD_7p17tftaNCotbNMToPHR8CE1NM0f5ZkwSC7-f0BlfeZHiWCQ2ufaB7GJeqtVeaE44fDrj29dW3WQvSVactaCeVrG8p5lRhcIkunTUlCFkrg2dessm4tmLoMG3II0u9RTfdzrmrcGkgoHz38-fTwMw0Yt03lH_Ewbq0PEa8elDlJck6B8R2-KFztdhIP7TkaLPsC-gVQ-hVXDJuWylknEuPus015f1sJi2e9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خنثی بودن متحدان جمهوری اسلامی ایران: می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، با او بودم و او خنثی ماند، کاملاً خنثی، و من از آن قدردانی می‌کنم.
🔴
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار خنثی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/128743" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ: حمله اخیر اسرائیل به بیروت خشونت‌آمیز و غیرضروری بود
🔴
محاصره دریایی ایران از بمباران مؤثرتر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128742" target="_blank">📅 20:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: ما کارت‌هایی برای بازی داریم و ایران باید رفتار بهتری داشته باشد. درگیری بین اسرائیل و حزب‌الله باید پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128741" target="_blank">📅 20:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / ترامپ: اگر ایران درست رفتار کند، می‌تواند در بخش نفت سرمایه‌گذاری کند و ما هیچ پولی به آن پرداخت نخواهیم کرد.
🔴
ایران به صندوق ۳۰۰ میلیارد دلاری دسترسی نخواهد داشت مگر اینکه رفتار مناسبی داشته باشد.
🔴
آمریکا مقدار زیادی از پول ایران را توقیف کرده و در مقطعی مجبور به بازگرداندن آن خواهد شد.
🔴
این توافق به کشتی‌ها اجازه می‌دهد تا از تنگه هرمز عبور و مرور کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128740" target="_blank">📅 20:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea5008dc2.mp4?token=aFgSj_H3YuCaaEm-H2mGkkpWjXSWXwJLs5VFjhxeJsOqnEEOnSUc3aLR1wd7KmlcCdikxwx5nPY4lpVmGiN0_4Cw5qcynru75nhfsmoXpxfz-xc6AL0ABzneIi7YwAAOJ-r2a5g2nRYn_5tLu9SM1IDY1El5zrZzq9GpgOdWw0yTyVvg_9Q1LAyFdsFoKMZtOxSSlDk5ZkXSWApQ8V6yL8DSoodYgRRVMfU_F3TfeIvpurIX-08-MGRggNYfBn9x5jdkWq7vH_DNtpLLoyF4uZZI3I6qSEx0pKTrdFhAXULSB92cJD79xngsFuoR7G6C1FfxOdpP4dJqnG55jAYGkGRCQrmPx0QC9_DM-EHvJG6gMF8bvMIDkG6jQtq-OWc-muXYXYT6Suprt93OWXgo1neblmCxOFZmtzRK-hBc9HvdtAGMEizp9-aCVxip7deUy56Oeq2wizmr_uVUUq49M-3SvntPu2h_YWCjSsp6voz4mpoozpp1NP9ceN6jVpsmGpEspauleKtcL57vcBZsHdZd0XT2BXxwYoMVhXOte9rI_Xl7UP7lnZcedQQYEiHu64BOdsPXdvVmzgv3GfrrlDuKng695o8oOyujRNnSSsvEgawAYMf5PbjZUX5tmHDvSzOLbQbSEs7vLQYNK4iaArYyk2m3r-q7dIcfviFiDf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea5008dc2.mp4?token=aFgSj_H3YuCaaEm-H2mGkkpWjXSWXwJLs5VFjhxeJsOqnEEOnSUc3aLR1wd7KmlcCdikxwx5nPY4lpVmGiN0_4Cw5qcynru75nhfsmoXpxfz-xc6AL0ABzneIi7YwAAOJ-r2a5g2nRYn_5tLu9SM1IDY1El5zrZzq9GpgOdWw0yTyVvg_9Q1LAyFdsFoKMZtOxSSlDk5ZkXSWApQ8V6yL8DSoodYgRRVMfU_F3TfeIvpurIX-08-MGRggNYfBn9x5jdkWq7vH_DNtpLLoyF4uZZI3I6qSEx0pKTrdFhAXULSB92cJD79xngsFuoR7G6C1FfxOdpP4dJqnG55jAYGkGRCQrmPx0QC9_DM-EHvJG6gMF8bvMIDkG6jQtq-OWc-muXYXYT6Suprt93OWXgo1neblmCxOFZmtzRK-hBc9HvdtAGMEizp9-aCVxip7deUy56Oeq2wizmr_uVUUq49M-3SvntPu2h_YWCjSsp6voz4mpoozpp1NP9ceN6jVpsmGpEspauleKtcL57vcBZsHdZd0XT2BXxwYoMVhXOte9rI_Xl7UP7lnZcedQQYEiHu64BOdsPXdvVmzgv3GfrrlDuKng695o8oOyujRNnSSsvEgawAYMf5PbjZUX5tmHDvSzOLbQbSEs7vLQYNK4iaArYyk2m3r-q7dIcfviFiDf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره محمد بن سلمان:
من چندین بار با ولیعهد عربستان سعودی صحبت کردم — آنها خیلی خوشحال هستند که هنوز... شما هم باید آنها را خوشحال نگه دارید، می‌دانید؟
🔴
ما از فرودگاه‌های آنها استفاده می‌کنیم، نه اینکه اگر نمی‌خواستیم، آنها بتوانند ما را متوقف کنند.
🔴
رفتم آن کوچولو را بگیرم. اما خطا کردم. از خطا کردن متنفرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128739" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a52031f13.mp4?token=UEgs2z21Od3fURX8di_OYMXXs2jnWvKLCD_J9x-7SAL63LPrU_mVN125RMETYdDYrEG7DohUIGMK4QtPpOlumYQI4DvhByB3_1pzofjSI4dArE-NUHbkTsEP3AVOKmkiSiqsSj6gUvedZAj3xjRE-9EkeneE7-XcfYsTQDhZoIW8S1slB4u4I8naykNJ-yWKhDnsN8Na5z3PK0F6gXhTRLxSNMeUu7eeLO7UL-CqGuB6ShOjxMmRQKMMUwSH6m8K6YNUL9rBbQrZxanwsJHlhTiwK11VbmF5hCDb0egekuvt8X3svaF1vtMhx_5qRnQn1pYzzfI93AoSfQ4JV_8jVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a52031f13.mp4?token=UEgs2z21Od3fURX8di_OYMXXs2jnWvKLCD_J9x-7SAL63LPrU_mVN125RMETYdDYrEG7DohUIGMK4QtPpOlumYQI4DvhByB3_1pzofjSI4dArE-NUHbkTsEP3AVOKmkiSiqsSj6gUvedZAj3xjRE-9EkeneE7-XcfYsTQDhZoIW8S1slB4u4I8naykNJ-yWKhDnsN8Na5z3PK0F6gXhTRLxSNMeUu7eeLO7UL-CqGuB6ShOjxMmRQKMMUwSH6m8K6YNUL9rBbQrZxanwsJHlhTiwK11VbmF5hCDb0egekuvt8X3svaF1vtMhx_5qRnQn1pYzzfI93AoSfQ4JV_8jVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مکزیک: مکزیک کنترل کشور خود را از دست داده است. کارتل‌ها مکزیک را اداره می‌کنند؛ این ناراحت‌کننده است.
🔴
رئیس‌جمهور زنی بسیار خوب است، اما زنی بسیار ترسو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128738" target="_blank">📅 20:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5ef35f0d.mp4?token=EAddveU3WsDCA-ajBBahkbbpdQzcm-5-UAwp4XcyKVXWdUiZVEzAE9N-ON8Mrk0KCZQ535Sa8kbEu9DoD-tW68VqzcuDBkPEs9P-HUz6Y1iqlmiNMn4kXTm7snXdux4ieXF-H5_JXfvRbJI1jI137PDVXpKfm0dxzRctkru08_NmCn_m7-xlN-ejXLgyA4spwbZrekoqVkUWL0g5TONkeZVsmlnyMmoo5X7IZaZ6ZLFgETMHKpv_hM9hFZF371O0DYdkDDqEY6ivnVD9SSwx_HBPp87DUed3touVgcWMJTuMrdVUHVrF9ZgyX9o0LqnjkYVQZHkC61hvlUCIjTbTy6DtQvUcliyF7Yly7lizMvFblqzJgSTj7_0h4TW8SaL02W72YejQ6LONoDDjO46_OKc-u56kbwIaihK5Bs-BQGzRA7XbJBCoATCP-dqjY_29ZzTXA3VH8eZRidBfr8hhZu3gi4z-DsbSzkbG3X9SjN9O2jQUGs4u5MA5uvIO_MIyKBJeQPT3xS0uELIh_20WqWF3sTlU0vKsGFwSD0x3mzW7pQJXTfZ6JFzMpF1FfMh-lpLcD7TM6-WsIfQSE7pfbz1sjnGqK3HCrmK9Vz7A-fuU6V1rEeIGUyOA0-8y9JDoIqnRSuQcutAiuALCBF2adHfY9hvnapWBJ9gWyhsdJ7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5ef35f0d.mp4?token=EAddveU3WsDCA-ajBBahkbbpdQzcm-5-UAwp4XcyKVXWdUiZVEzAE9N-ON8Mrk0KCZQ535Sa8kbEu9DoD-tW68VqzcuDBkPEs9P-HUz6Y1iqlmiNMn4kXTm7snXdux4ieXF-H5_JXfvRbJI1jI137PDVXpKfm0dxzRctkru08_NmCn_m7-xlN-ejXLgyA4spwbZrekoqVkUWL0g5TONkeZVsmlnyMmoo5X7IZaZ6ZLFgETMHKpv_hM9hFZF371O0DYdkDDqEY6ivnVD9SSwx_HBPp87DUed3touVgcWMJTuMrdVUHVrF9ZgyX9o0LqnjkYVQZHkC61hvlUCIjTbTy6DtQvUcliyF7Yly7lizMvFblqzJgSTj7_0h4TW8SaL02W72YejQ6LONoDDjO46_OKc-u56kbwIaihK5Bs-BQGzRA7XbJBCoATCP-dqjY_29ZzTXA3VH8eZRidBfr8hhZu3gi4z-DsbSzkbG3X9SjN9O2jQUGs4u5MA5uvIO_MIyKBJeQPT3xS0uELIh_20WqWF3sTlU0vKsGFwSD0x3mzW7pQJXTfZ6JFzMpF1FfMh-lpLcD7TM6-WsIfQSE7pfbz1sjnGqK3HCrmK9Vz7A-fuU6V1rEeIGUyOA0-8y9JDoIqnRSuQcutAiuALCBF2adHfY9hvnapWBJ9gWyhsdJ7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره روسیه-اوکراین: هر دو تعداد زیادی سرباز از دست می‌دهند، روسیه بیشتر از دست می‌دهد، چون آن‌ها تهاجمی هستند و وقتی در جنگ تهاجمی هستید، بیشتر از دست می‌دهید، خیلی ساده است.
🔴
من فکر می‌کنم هر دو (زلنسکی و پوتین) می‌خواهند کاری انجام دهند، فقط نمی‌دانند چگونه آن را انجام دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128737" target="_blank">📅 20:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ: اروپا با مشکلات زیادی روبرو است؛ در حوزه‌های انرژی و مهاجرت وضعیت خوبی ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128736" target="_blank">📅 20:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128735">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: به نتانیاهو گفتم که از طریق این توافق، چیزی را که بیش از همه می‌خواست، برایش محقق کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128735" target="_blank">📅 20:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128734">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ درباره سوریه: من مسئولیت زیادی در قبال آقایی در سوریه داشتم که اکنون رئیس‌جمهور آنجاست؛ او کار فوق‌العاده‌ای انجام داده است. او این کشور را در یک سال و نیم جمع و جور کرده، تقریباً مثل کشور ما، یک سال و نیم، اندازه‌ای تقریباً مشابه.
🔴
آنها گفتند، «لطفاً آنها را آنجا نگذار؛ او مردی بسیار خشن است، القاعده.»
🔴
من گفتم، «خب، من یک چیز می‌دانم، یک پیشاهنگ کارساز نخواهد بود.»
🔴
و او در واقع کار بسیار خوبی انجام داده است؛ او دوست دارد وارد شود. می‌دانید، حزب‌الله دشمن اوست، و او وارد می‌شود، اما هر بار که می‌شنود کسی هست، ساختمان‌ها را خراب نمی‌کند — فقط با دقت می‌رود و او را می‌گیرد، اما نمی‌دانم مردم این را می‌خواهند یا نه.
🔴
شاید نخواهند، شاید لبنان نخواهد — ما باید کمی توسط لبنان هدایت شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128734" target="_blank">📅 20:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128733">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19e4e6a48.mp4?token=G8a-TnONC1t1SXCMuRLDedeiSlFBXWKTW-8Se5MWxlMPU6uQSS2H2_YrM-Stq7T2SoUino6EWAbK_Kyah6oqoqAih42CjL_XrATcHR025jX-u29Om_ysaCaPNqPn7WQ8YTfT8WwEPJgel5e0Cty-ZqxfrkqYOwla9_EpNgVTUDBU9Tt626dPlidaIKt0HIIh2j0w-uaw2NdzAwB25pvvkw2fnDFR7EO_b9cP4tEw9KAuGsuR-KM3ja4ToT-UA26vK7k09ojxqUcm9LMX5K9sxkS5JsbqiWjMZyiiqoHmP0mHncPCpaPjXBYdEqwE8EkcQj97sndZHb5bjHOJF8B95I2W7qcx8VBv-b74cNrhO8G7otKuW56pZO-OJeMPeL5xGZ1HYX15Z8iv9HM3HpeviojIqr-k8MkxQBkjveoy8YnPduAdv9LOV-J7oXiM7uNXXnybdBJtnOOCSRI5EnkMQeQIkxF9mXPdPJNdwSA2OXcqQp6sR4RHBiLBBhWbcJWsyw5b3GGcrt4SRuaonLp1wijIx-sQXFK3QBpN98Vu48BExtcxjLVjza1QAvTBRTShiIZMwVwyNqRc5yYpPRPRhcYs6NyQkSdugrGPM44inDbC0g_9ihfSpEdMpgB0fRgjY_uyByafd-MNeSQ-YRCrhTsslGX-qR_Cx_UsFjziSAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19e4e6a48.mp4?token=G8a-TnONC1t1SXCMuRLDedeiSlFBXWKTW-8Se5MWxlMPU6uQSS2H2_YrM-Stq7T2SoUino6EWAbK_Kyah6oqoqAih42CjL_XrATcHR025jX-u29Om_ysaCaPNqPn7WQ8YTfT8WwEPJgel5e0Cty-ZqxfrkqYOwla9_EpNgVTUDBU9Tt626dPlidaIKt0HIIh2j0w-uaw2NdzAwB25pvvkw2fnDFR7EO_b9cP4tEw9KAuGsuR-KM3ja4ToT-UA26vK7k09ojxqUcm9LMX5K9sxkS5JsbqiWjMZyiiqoHmP0mHncPCpaPjXBYdEqwE8EkcQj97sndZHb5bjHOJF8B95I2W7qcx8VBv-b74cNrhO8G7otKuW56pZO-OJeMPeL5xGZ1HYX15Z8iv9HM3HpeviojIqr-k8MkxQBkjveoy8YnPduAdv9LOV-J7oXiM7uNXXnybdBJtnOOCSRI5EnkMQeQIkxF9mXPdPJNdwSA2OXcqQp6sR4RHBiLBBhWbcJWsyw5b3GGcrt4SRuaonLp1wijIx-sQXFK3QBpN98Vu48BExtcxjLVjza1QAvTBRTShiIZMwVwyNqRc5yYpPRPRhcYs6NyQkSdugrGPM44inDbC0g_9ihfSpEdMpgB0fRgjY_uyByafd-MNeSQ-YRCrhTsslGX-qR_Cx_UsFjziSAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حماس: وقتی به دنیا آمدند، با یک تفنگ ماشینی در دستشان بیرون آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128733" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128732">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: امیدوارم توافق‌نامه ابراهیم را گسترش دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128732" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128731">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ: ایران حزب‌الله را دارد و این مسئله باید به نحوی حل شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128731" target="_blank">📅 20:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128730">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397b3f7778.mp4?token=lXuaT_IG94_q-1tutiKC7cYtxEpDxtc20odiDKsNEmEDy44za8t1rL6L7-RMQpuzr7Xk1RzzXXCYkkOr6fy_Irok4Z0ypHeQOHVNAKWuSnE3VDEnGzxDLjbKMbPMWI1UEUS6Jy6lfRggzUszsG1kcGhj9CaNfe5FJpyz2ouoVE6iBhQQuKWXzXf40GUVQ2YVUwYBZbNkFGwKI1cAZa7anly7epHrToD9V1lynpJPto5d-n-jaEIP4pcaOSQu9QEalhN8beco071RkwvKgTHldjQv--v4DJm6CkO57gQTXeXemu67dNff8twythdc3D6ZGxqOf4HdKZLumI7IWWEw4AsF4PJdzvBkTD-gyjLbP8zlUK-KE145796550QMK4jsPHNiY1POPGfbtDI3usTJyAIg_V9MpYQ3PgvMeLVi2k9FCMhHThbxVj2PPgOoBeXnhPmHF507ajG3oW1FmJvL59DCJq8pG8yGt4sSFUpkpJSKZqCAkaqQnomSktBhhdkac_sYraYO5x9scMdB_ztg8Fiwp6BJIiuBqhB6VsUzv849n_WcOq-35_KHQkOqFQY-EMwcGToBSzdt4Lj2c079DA4IBTU2d5RLdPzCicIYg1bN95ujxvvyFsRC2fNWTNdS346U3PeSLgFkS4YuxcLhaS90VMUic9c7POErAIwmgfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397b3f7778.mp4?token=lXuaT_IG94_q-1tutiKC7cYtxEpDxtc20odiDKsNEmEDy44za8t1rL6L7-RMQpuzr7Xk1RzzXXCYkkOr6fy_Irok4Z0ypHeQOHVNAKWuSnE3VDEnGzxDLjbKMbPMWI1UEUS6Jy6lfRggzUszsG1kcGhj9CaNfe5FJpyz2ouoVE6iBhQQuKWXzXf40GUVQ2YVUwYBZbNkFGwKI1cAZa7anly7epHrToD9V1lynpJPto5d-n-jaEIP4pcaOSQu9QEalhN8beco071RkwvKgTHldjQv--v4DJm6CkO57gQTXeXemu67dNff8twythdc3D6ZGxqOf4HdKZLumI7IWWEw4AsF4PJdzvBkTD-gyjLbP8zlUK-KE145796550QMK4jsPHNiY1POPGfbtDI3usTJyAIg_V9MpYQ3PgvMeLVi2k9FCMhHThbxVj2PPgOoBeXnhPmHF507ajG3oW1FmJvL59DCJq8pG8yGt4sSFUpkpJSKZqCAkaqQnomSktBhhdkac_sYraYO5x9scMdB_ztg8Fiwp6BJIiuBqhB6VsUzv849n_WcOq-35_KHQkOqFQY-EMwcGToBSzdt4Lj2c079DA4IBTU2d5RLdPzCicIYg1bN95ujxvvyFsRC2fNWTNdS346U3PeSLgFkS4YuxcLhaS90VMUic9c7POErAIwmgfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: مردم می‌خواهند من پل‌ها را بمباران کنم.
🔴
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
🔴
اما ما آن پل را بمباران کردیم، شما دیدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128730" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128729">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17a88534a.mp4?token=c971YnBoqJ8HkfNCEpmsDbEwT1jhA54cdbUj7f0ECMWbHZxu9rK6vUcZiZmhqzsZl_xfvpAQI5HEIyXL8Gw0L7kbUbFed9SOz6viXp5jYuBeB_M9PfWQdFMmdaLNPVSdoBvqzX50WYDbc55MMAmNjWhD9XjR_X6j7xl9f71u6AGm59gRMTpcPqI6h7dB4n1EVxwGfuK37WnLcWoRckF9VU99iNWQNGr_hVYyIzzyit3bHhcpIXa3cE1mdSLqOHNuu7tLvje0kTNmAi6v1Oh_L48ofJ79QFjv7JIFmykxfo3l6PtC4pkdtwHPdavBDO_6VyTM9hr66hf0-dwZnu958TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17a88534a.mp4?token=c971YnBoqJ8HkfNCEpmsDbEwT1jhA54cdbUj7f0ECMWbHZxu9rK6vUcZiZmhqzsZl_xfvpAQI5HEIyXL8Gw0L7kbUbFed9SOz6viXp5jYuBeB_M9PfWQdFMmdaLNPVSdoBvqzX50WYDbc55MMAmNjWhD9XjR_X6j7xl9f71u6AGm59gRMTpcPqI6h7dB4n1EVxwGfuK37WnLcWoRckF9VU99iNWQNGr_hVYyIzzyit3bHhcpIXa3cE1mdSLqOHNuu7tLvje0kTNmAi6v1Oh_L48ofJ79QFjv7JIFmykxfo3l6PtC4pkdtwHPdavBDO_6VyTM9hr66hf0-dwZnu958TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره توافق ایران: توافق اوباما راهی به سوی سلاح هسته‌ای بود.
🔴
توافق ترامپ دیواری برای سلاح هسته‌ای است که سلاح هسته‌ای نمی‌تواند از آن عبور کند. هیچ‌کس نمی‌تواند از آن عبور کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128729" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128728">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1993599568.mp4?token=RKym9jqS9cGHv4zmc92menSMsRLh5B3hlUxisaA90LL7KJk8WJFbGGJDQtmzoSPz7-843hCj_yEL9o8R8Q9epHgcOGanrlUxt89lvaBE0rD-VI4wjhGHA1mx5gdpQff4otTpUtIozDCk5RjNZM9FIeFQv_nABAl1-VKNQQ2j87OhDk43f4wM7L24RMBemhuI7M7CRk5K2OWnKFy2YtU37JT9y1Q-c1iNQD2Qw3xizbzuQzvDBVQYCviNAQZ_Ysuz1Xk52qdp8H2qW-Q7OBGGKb6h_6upfeVnyzco9SbB8mNUoVfOJ0c0HOb0lmLRESoGd5dbEu7MrB1rdJldwdLtiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1993599568.mp4?token=RKym9jqS9cGHv4zmc92menSMsRLh5B3hlUxisaA90LL7KJk8WJFbGGJDQtmzoSPz7-843hCj_yEL9o8R8Q9epHgcOGanrlUxt89lvaBE0rD-VI4wjhGHA1mx5gdpQff4otTpUtIozDCk5RjNZM9FIeFQv_nABAl1-VKNQQ2j87OhDk43f4wM7L24RMBemhuI7M7CRk5K2OWnKFy2YtU37JT9y1Q-c1iNQD2Qw3xizbzuQzvDBVQYCviNAQZ_Ysuz1Xk52qdp8H2qW-Q7OBGGKb6h_6upfeVnyzco9SbB8mNUoVfOJ0c0HOb0lmLRESoGd5dbEu7MrB1rdJldwdLtiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره محمد بن زاید امارات:
محمد در امارات یک جنگجوی شگفت‌انگیز است. هفته گذشته بمب می‌انداخت، من گفتم، «چه کسی لعنتی این همه بمب می‌اندازد»، آن امارات بود.
🔴
او یک مبارز خوب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128728" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128727">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ: خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما حدود یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
🔴
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
🔴
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128727" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128726">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق پایبند نباشد، احتمالاً بمباران آن را از سر می‌گیریم تا زمانی که به آن پایبند بماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128726" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128725">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: از شرکایمان در پاکستان و قطر تشکر می‌کنم؛ آنها تلاش‌های فوق‌العاده‌ای انجام داده‌اند
🔴
امیدوارم این توافق صلح آغاز یک توافق گسترده‌تر باشد که خاورمیانه را نیز شامل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128725" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e52341e.mp4?token=iaVn5k7ZcaX3dmx3Ealb6RYClpcw7g41HSDRM1wIkwo3a-hiEYyW_XL67YbePh51GXnFWEeugeW1uQnGVGfevWGqfl2qBOsyJeKWFgb9VX0Dd0kAMiRVy0J6AH2oWT6bhvQrbT8FkYsu_CE11LTq0-0WB_YOhNcTB46THB_VpY83WloSjRLBlysnopkORdhC201E5M_VGbZPB-G_PEgYeb9xgmwtPyl2rd9GeKTiN7Cl-E6z6nZvqmwzp-NJAWhkCiPc36bJBdzlweqbnDCNhutv1wtsLABC6z9vakVzG8La7Ob4OCXfu2jVF3Ccgn3v5zKqHSiFXVsjTSSf4uUILIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e52341e.mp4?token=iaVn5k7ZcaX3dmx3Ealb6RYClpcw7g41HSDRM1wIkwo3a-hiEYyW_XL67YbePh51GXnFWEeugeW1uQnGVGfevWGqfl2qBOsyJeKWFgb9VX0Dd0kAMiRVy0J6AH2oWT6bhvQrbT8FkYsu_CE11LTq0-0WB_YOhNcTB46THB_VpY83WloSjRLBlysnopkORdhC201E5M_VGbZPB-G_PEgYeb9xgmwtPyl2rd9GeKTiN7Cl-E6z6nZvqmwzp-NJAWhkCiPc36bJBdzlweqbnDCNhutv1wtsLABC6z9vakVzG8La7Ob4OCXfu2jVF3Ccgn3v5zKqHSiFXVsjTSSf4uUILIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/128724" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128723" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128722">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: جلوگیری از دستیابی ایران به سلاح هسته‌ای، در کنار باز کردن تنگه هرمز، مهمترین نکته برای من است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128722" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128721">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: این دستاورد بدون فشار فوق‌العاده‌ای که ما طی یک سال و نیم گذشته بر ایران اعمال کرده‌ایم، امکان‌پذیر نبود
🔴
ما با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای مانند موشک‌های بالستیک همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/128721" target="_blank">📅 19:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128720">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84cd4ae6c5.mp4?token=Yf1YXkPapGxVPXOQjndRpJJcIffAPXLBnHtyXUZjmCj-egQi5bTt8KFzXdwmd-X7PYM7yf5N7KHwqEMupCEGBD2je8Ribav_A_bnjzbkNeoSxXaNYYrPLCHRQU9XHg3Ap3vNBOx0VtAlFvfxxdh0PH_DbHcJiW0sMK2Za-ysi2j9-d815Vdfgrg-hPsrv8vQ2NdNwcla_HCT60p4jkozKTaw8fFzelNzCCeMPuRZRi8lOPWhHgX1AZ9jfOrAbo2FaXjxtPZai2XZfVGJK5q1xeiko1eQFLqh3Pjru51dCd6-_GGhlvm0QqFJ1zcW0tLTri9s9WdVxwwFOrrHTdKe-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84cd4ae6c5.mp4?token=Yf1YXkPapGxVPXOQjndRpJJcIffAPXLBnHtyXUZjmCj-egQi5bTt8KFzXdwmd-X7PYM7yf5N7KHwqEMupCEGBD2je8Ribav_A_bnjzbkNeoSxXaNYYrPLCHRQU9XHg3Ap3vNBOx0VtAlFvfxxdh0PH_DbHcJiW0sMK2Za-ysi2j9-d815Vdfgrg-hPsrv8vQ2NdNwcla_HCT60p4jkozKTaw8fFzelNzCCeMPuRZRi8lOPWhHgX1AZ9jfOrAbo2FaXjxtPZai2XZfVGJK5q1xeiko1eQFLqh3Pjru51dCd6-_GGhlvm0QqFJ1zcW0tLTri9s9WdVxwwFOrrHTdKe-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / ترامپ: ما یک نسخه از توافق ایران را به اسرائیل ارسال کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128720" target="_blank">📅 19:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a1ea2a6a.mp4?token=r_BpRUb-bRzYvQ5J5-aSe15WE7M5CyFOJhBYpbdQvyFbtAVCGLTNU2H9Bjl7LUjWqBCdPz47wnFc4nBj-iYDYj8oS6fMJmoUlp4IezkUdVFZ--Xa8yLTxwou--50azuqKXW9o9SeYXM9brzKuQ3vCLA-R5yd1Exej8mS5VN_jeQya7N5GtQSy01XTgyO55qSrPEZ7O80K2zMfQePJA5aEAGzlwByISsn29llTlJzqbPwL66WN7Xh4Sbj7biW9E2QSwEAWEDu2BFXNclX6eOUPfNOK5Z9txGb6hxcprdUJsXLUaxiPMp6IkyVcWN5Yr0-0bqkl3yN7E_D__za2oXTmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a1ea2a6a.mp4?token=r_BpRUb-bRzYvQ5J5-aSe15WE7M5CyFOJhBYpbdQvyFbtAVCGLTNU2H9Bjl7LUjWqBCdPz47wnFc4nBj-iYDYj8oS6fMJmoUlp4IezkUdVFZ--Xa8yLTxwou--50azuqKXW9o9SeYXM9brzKuQ3vCLA-R5yd1Exej8mS5VN_jeQya7N5GtQSy01XTgyO55qSrPEZ7O80K2zMfQePJA5aEAGzlwByISsn29llTlJzqbPwL66WN7Xh4Sbj7biW9E2QSwEAWEDu2BFXNclX6eOUPfNOK5Z9txGb6hxcprdUJsXLUaxiPMp6IkyVcWN5Yr0-0bqkl3yN7E_D__za2oXTmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره نتانیاهو و اسرائیل:
ما شریک بزرگ هستیم و او شریک بسیار کوچک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/128719" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128718">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ درباره نتانیاهو: نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد.
🔴
او گفت این می‌تواند پایان اسرائیل باشد، و اگر من نبودم، همینطور می‌شد.
🔴
و اوباما به او گوش نداد.
🔴
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128718" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128717">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: هیچ پولی در ایران سرمایه‌گذاری نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128717" target="_blank">📅 19:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128716">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: ایران با ما همکاری می‌کند تا اورانیوم دفن شده در اعماق زمین را تحویل دهد و زمان در این موضوع نقشی ندارد.
🔴
فکر می‌کنم اسرائیلی‌ها می‌توانستند در مورد حزب‌الله بهتر عمل کنند
🔴
نمی‌گویم اسرائیلی‌ها نباید از خودشان دفاع کنند، اما نیازی به تخریب ساختمان‌ها در بیروت نیست
🔴
از بابت لبنان خیلی متاسفم
🔴
مذاکرات فنی در مورد ذخایر هسته‌ای ایران فوراً آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128716" target="_blank">📅 19:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128715">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / ترامپ: توافق با ایران فردا یا پس‌فردا امضا خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128715" target="_blank">📅 19:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ درباره ترور سردار سلیمانی :
این یک همکاری مشترک بود، همانطور که در کسب‌وکار املاک و مستغلات می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
🔴
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او در کدام هواپیما خواهد بود.
🔴
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست که ما او را سرنگون نخواهیم کرد. آن‌ها بسیار باهوش هستند.
🔴
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
🔴
و به ژنرال گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ آیا دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128714" target="_blank">📅 19:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ : نتانیاهو گاهی اوقات کمی از کوره در می‌رود، اما من با او همکاری بسیار خوبی دارم
🔴
ما به احتمال زیاد توافق را امضا خواهیم کرد و ایران خواهان آن است؛ آنها به طور مناسب عمل کرده و موافقت کرده اند که سلاح هسته ای تولید نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128713" target="_blank">📅 19:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: من نمی‌خواستم "هربرت هوور بزرگ" فقید (سی و یکمین رئیس‌جمهور ایالات متحده آمریکا) باشم.
🔴
من آن را نمی‌خواستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128712" target="_blank">📅 19:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128711">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: ما در مورد لبنان کمی با نتانیاهو اختلاف نظر داریم، و او می‌توانست تحمل بیشتری داشته باشد و هر بار که یکی از اعضای حزب‌الله وارد ساختمانی می‌شود، آن را تخریب نکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128711" target="_blank">📅 19:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128710">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a0d76d44.mp4?token=MjdV1mjRGBv2nn3H0JFc-gBVFr4quyqxBV1JQWffAL_0wgefhbbgRVWzODeVgjnIWSuLpCMkZknxiQNSMCuk4lLEKD2q4qWLQxqkzU2fVML96xk5-1RJDsf3emzTsnw_KJ4MGxnhOzJ7o6EDohdlFVTL0I1ZsU31yYy_I92ldaHf6A1G9aXG1R4ttoxojqRunJ5PEFy8OIWT11TE4_UHinCvRSg0gLm81HbtogsH9FwYFdWQMe92mkmfi5nvCNZlkN5RrdAhXwu0FXrh42RzyhSDca5SiabY2MMBznrSJd6at0TL-3OpZCCd7cQw9veHlVFuhzCyFFO2JGUIzLFGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a0d76d44.mp4?token=MjdV1mjRGBv2nn3H0JFc-gBVFr4quyqxBV1JQWffAL_0wgefhbbgRVWzODeVgjnIWSuLpCMkZknxiQNSMCuk4lLEKD2q4qWLQxqkzU2fVML96xk5-1RJDsf3emzTsnw_KJ4MGxnhOzJ7o6EDohdlFVTL0I1ZsU31yYy_I92ldaHf6A1G9aXG1R4ttoxojqRunJ5PEFy8OIWT11TE4_UHinCvRSg0gLm81HbtogsH9FwYFdWQMe92mkmfi5nvCNZlkN5RrdAhXwu0FXrh42RzyhSDca5SiabY2MMBznrSJd6at0TL-3OpZCCd7cQw9veHlVFuhzCyFFO2JGUIzLFGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
اسکات، آیا بازار سهام از تو باهوش‌تر است؟
🔴
وزیر خزانه‌داری بسنت:
خیر، قربان.
🔴
ترامپ:
این یک جمله وحشتناک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128710" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128709">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: توافق با ایران خوب است و این چیزی است که در متن یادداشت تفاهم خواهید دید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128709" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128708">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: اگر من دخالت نمی‌کردم، ایران خاورمیانه و اسرائیل را نابود می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128708" target="_blank">📅 19:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128707">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ درباره ایران: بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
🔴
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببینید، ما قادر نخواهیم بود توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
🔴
این به شما چیزی می‌گوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128707" target="_blank">📅 19:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128706">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: من با نتانیاهو در مورد لبنان اختلاف نظر داشتم و به او گفتم که مودبانه رفتار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128706" target="_blank">📅 19:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128705">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم.
🔴
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128705" target="_blank">📅 19:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128704">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128704" target="_blank">📅 19:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128703">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: فکر می‌کنم رهبران ایران رفتار بسیار متفاوتی خواهند داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/128703" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128702">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: دو روز گذشته فرصتی بود تا درباره جزئیات توافق با نزدیک‌ترین دوستانمان صحبت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128702" target="_blank">📅 19:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128701">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: اگر به جنگ ادامه می‌دادیم، تنگه هرمز هرگز باز نمی‌شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128701" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128700">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: من در اجلاس گروه هفت جزئیات توافق ایران را با رهبران این کشورها مورد بحث قرار دادم و آنها از اینکه به توافق رسیدیم بسیار خوشحال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128700" target="_blank">📅 19:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: توافق با ایران هر آنچه را که می‌خواستیم، از جلوگیری از دستیابی این کشور به سلاح هسته‌ای گرفته تا باز کردن تنگه هرمز، محقق کرد
🔴
قیمت نفت پس از توافق با ایران به سطوح بی‌سابقه‌ای کاهش یافته است
🔴
اگر ما این توافق را انجام نداده بودیم، تنگه هرمز باز نمی‌شد و بمب‌ها همچنان بی‌وقفه می‌افتادند.
🔴
دو روز گذشته بسیار سخت بوده است و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافق نرسیم، برای دومین شب به بمباران آنها باز خواهیم گشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128699" target="_blank">📅 19:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128698">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آکسیوس: حتی اگر زمان امضا تغییر کند، نشست هیئت‌های آمریکا و ایران به ریاست جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس ایران، طبق برنامه روز جمعه در سوئیس برگزار خواهد شد.
🔴
انتظار می‌رود دو طرف درباره آغاز مذاکرات پیرامون برنامه هسته‌ای ایران گفت‌وگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128698" target="_blank">📅 19:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128697">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qga7hZHxPNdh4UGWEWM2bS2rgP4GdYGwGiQwISsZ3S_V30C7s83tBKbsoG74bBq_icQxCM9VUwGtEYfPmW0h4R9YD8ee6yRImQSFuo2sDMcSM3T4PMq2nIuE0zU2FL63GD8AYE-_UpFXQjf1cbmiGI3lwx-C0qaBOOczaR1z4t8pS30004I4zXjOk20tWNmz74-j-TFezaLNdMNk5jMkEt1tU5W4VMQOsixFpkgI7efyXyPmT8LEb8i_Icvw1b8tFCjQt1M5WiePEk_omwoY2tTy7K3LzbAR7LqKtEm73ta1p2-drfibrX4aJAF0pJBV9g20Qc7v2VJmASu_ucZWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش وال‌استریت‌ژورنال، دونالد ترامپ که برای شرکت در اجلاس امسال در سواحل جنوبی دریاچه ژنو حضور یافته، چهره‌ای به مراتب آرام‌تر و ملایم‌تر از سال‌های گذشته از خود نشان داده است.
🔴
این تغییر رویکرد در رفتار رئیس‌جمهور آمریکا، توجه تحلیل‌گران را در این نشست بین‌المللی به خود جلب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/128697" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ایتامار بن گویر تصمیم گرفته بستگان اسرائیلی‌های کشته‌شده را به عنوان ناظران رسمی زندان منصوب کند، اقدامی که با هدف تشدید شرایط بازداشت اسیران فلسطینی انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/128696" target="_blank">📅 19:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رویترز: تهران به حزب‌الله وعده داده که با آغاز ورود منابع مالی در پی این توافق، حمایت مالی بیشتری از این گروه خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128695" target="_blank">📅 19:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UloXT2rvyY5vaE2ymNQkr_-SZbvtg8u2DMaXF-lDlq9wPLSrzXjTu4eWVnWZplTmV4QJxJCQM9WlO-t3fXMmScpYJJRVavWasO5rKNGinqiDT8IBmER09xBarl4KXE9lxJhxvuRIqpz4Tc8-AVWC6VwAWlSSNmdAdKBCYi294AChESLzCSg5--FZVsXNa8oZE1tDAnGFIR6vUuEThRU_W7NF3suwUOmfyq4bvooVhsmGr8GyG1hc5WoTy8o_9DYNu_ghSGZLUL0qmj3CtUH5uqx6J93TOh5SasCiYvXx3WA2-kjxxv93OOoG94nwiVEWNcMtjzX-mLZyO-BO15I5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال دارایی‌های مسدود شده ایران را اعلام کرد:
🔴
چین: ۲۰-۵۰ میلیارد دلار (بزرگ‌ترین)
🔴
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
🔴
عراق: ۱۵ میلیارد (برق و گاز)
🔴
هند و کره جنوبی: هرکدام ۷ میلیارد
🔴
ژاپن: ~۳ میلیارد
🔴
آمریکا: ۲ میلیارد
🔴
لوکزامبورگ و عمان: مبالغ کمتر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128694" target="_blank">📅 19:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
آمریکا در حال بررسی صدور مجوز تولید موشک برای اروپا و اوکراین است
🔴
دونالد ترامپ، رئیس‌جمهور ایالات متحده، قصد دارد از شرکت‌های دفاعی آمریکایی بخواهد که موشک‌ها را تحت لیسانس در اروپا و اوکراین تولید کنند تا کمبودهای حیاتی در پدافند هوایی را جبران نمایند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128693" target="_blank">📅 19:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عارف، معاون اول رئیس‌جمهور: مدیریت تنگه هرمز در دست ماست و برای خدماتی که به کشتی‌ها برای تأمین عبورشان ارائه می‌دهیم، مبالغی دریافت خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128692" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128691">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57b5fc0a8.mp4?token=lu4GbTax6vE0CujrsDxjZNmmGv1tlJJppqZ54nc5-UQOXH0mgp7Qt5n-RKFFAs9KefGtAvl5XjiXtkbG4UH-Z2denlfW5UdjV_q2p9zAzqRJZeNdnX_UFKIYNAuq3dg7PBHsC8BywXCmUhDxFbproetgwj11-iCpXX2XHqse7_oW255l7c9vFWQdYnKVs0EmQkoKxI6zpW32B8i23RI2oWPrLhTq0AW5jRiC5RB3iFEWO5LzE39oP_EKdGq9sYxrZBHJxPE60K2l8IIl11yyQGvSqVpSmNR4gmWIFAHdT0HuBT50Qpcl8pEudXVqO5uMYJf-MmWwZyqe1XCNv-Ef8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57b5fc0a8.mp4?token=lu4GbTax6vE0CujrsDxjZNmmGv1tlJJppqZ54nc5-UQOXH0mgp7Qt5n-RKFFAs9KefGtAvl5XjiXtkbG4UH-Z2denlfW5UdjV_q2p9zAzqRJZeNdnX_UFKIYNAuq3dg7PBHsC8BywXCmUhDxFbproetgwj11-iCpXX2XHqse7_oW255l7c9vFWQdYnKVs0EmQkoKxI6zpW32B8i23RI2oWPrLhTq0AW5jRiC5RB3iFEWO5LzE39oP_EKdGq9sYxrZBHJxPE60K2l8IIl11yyQGvSqVpSmNR4gmWIFAHdT0HuBT50Qpcl8pEudXVqO5uMYJf-MmWwZyqe1XCNv-Ef8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون درباره ترامپ: من همیشه به رئیس‌جمهور ترامپ اعتماد داشتم چون ما همیشه بسیار صریح صحبت می‌کردیم.
🔴
وقتی اختلاف نظر داشتیم، آن را بیان می‌کردیم، و وقتی او به چیزی متعهد می‌شود، به آن تعهدات پایبند بوده است.
🔴
و امروز، آمریکا و ترامپ به چیزی متعهد شدند، و این بسیار مهم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128691" target="_blank">📅 19:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128690">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SugH_zmQx_rGI96R2CLbAXJ3Yg7oeg9Wt9sXYBCArjBZSOal1BRkxs5tS528QTpRGJFnEGSi9aiL8O49yYNX_jxsDQhrs2IHG5F9tYq_ZArVzAMwp36GO7VzXVPh0LEn9UtclVgZoFoPoCyDgW1FsxkMDhf7FWO-YD6OCig2ej5KXeMAIkdkzFa5p0RYbgD--oj2zsfeeE9h7-LOeowWuYS2cFpcwqkgOH19NjTyQzv44tLHCBnYCkEXbekeB9V3ndOnyaTxYCB4NZpfAjZVAjzH1RztNrPiPn1G30yPgFmCwrS5QEqPgqOeImAROE3pBrWcjfUflKRGMh4gjgwmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ایالات متحده، ایران و میانجی‌ها در حال بحث در مورد تسریع امضای تفاهم‌نامه هستند که در حال حاضر برای جمعه برنامه‌ریزی شده است، و شاید حتی امروز آن را "به صورت الکترونیکی" امضا کنند.
🔴
جلسه مذاکره‌کنندگان همچنان برای جمعه در سوئیس برنامه‌ریزی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128690" target="_blank">📅 19:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128689">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سفارت ایتالیا در تهران روز جمعه بازگشایی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128689" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128688">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه امانوئل ماکرون:
من فکر می‌کنم توافق ایران ترامپ معامله خوبی است.
🔴
البته که همه چیز را فوراً حل نمی‌کند.
🔴
اما اگر به مبارزه ادامه می‌دادیم، چه معنایی داشت؟ این به معنای بسته ماندن تنگه بود.
🔴
ماکرون درباره لبنان: حزب‌الله باید در لبنان سلاح‌های خود را زمین بگذارد. از سوی دیگر، اسرائیل نیز باید این کار را انجام دهد.
🔴
نباید هیچ جنگی رخ دهد. آنچه باید اتفاق بیفتد، صلح است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128688" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128687">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مقام ایرانی به تسنیم : سفر تیم مذاکره کننده به سوئیس لغو نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128687" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128686">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c6252578.mp4?token=U0jjBXbn7TqmXf_DqW4-w8M01pviZ_cDfjOKLptPjprtPxoKOq-ZAR8xIgEmmgwY6dXuoLpp7Q0hnJqTucTAbN82qRFYNjuJq-SKdEvfUgI0NoiQtqdAUtZrn6dwCnzEQcntYz9MCwHOqKpMtsTERWx8Ntx3cADwzPf1ATu_tovYz8B0A6B1SOzZ6Jmly5TWiElzwkB9KBwhRO9kdFjDtJA7AgZHQAngwxCVHaK0V8kqZclG6gkiso44-n-hHrQicbOT9csVfHkMCViN5ULeeOzu3F6uEcdzhFIzIydNOJ6ikxyeD8lZW2vJYUKWqfDAMxq2kGmlLNn1pOUQATM7bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c6252578.mp4?token=U0jjBXbn7TqmXf_DqW4-w8M01pviZ_cDfjOKLptPjprtPxoKOq-ZAR8xIgEmmgwY6dXuoLpp7Q0hnJqTucTAbN82qRFYNjuJq-SKdEvfUgI0NoiQtqdAUtZrn6dwCnzEQcntYz9MCwHOqKpMtsTERWx8Ntx3cADwzPf1ATu_tovYz8B0A6B1SOzZ6Jmly5TWiElzwkB9KBwhRO9kdFjDtJA7AgZHQAngwxCVHaK0V8kqZclG6gkiso44-n-hHrQicbOT9csVfHkMCViN5ULeeOzu3F6uEcdzhFIzIydNOJ6ikxyeD8lZW2vJYUKWqfDAMxq2kGmlLNn1pOUQATM7bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره پرونده اپستین: بدون مدرک نمی‌توان کسی را تحت پیگرد قرار داد
جی‌دی ونس در واکنش به پرونده‌های مرتبط با جفری اپستین گفت:
🔴
«صرف اینکه فکر کنیم اتفاقی اشتباه رخ داده، برای محاکمه افراد کافی نیست.»
او تاکید کرد:
🔴
«تنها زمانی می‌توان افراد را تحت پیگرد قانونی قرار داد که مدارک کافی برای اثبات تخلف آنها وجود داشته باشد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128686" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مکرون: ترامپ، مانند همهٔ ما، موافق بود که از سوی روسیه هیچ تمایل جدی‌ای برای برگزاری گفت‌وگوهای صلح یا مذاکرات وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128685" target="_blank">📅 18:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128684">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: من وارد توافق‌هایی شده‌ام که ۱۰۰ درصد قطعی بودند، اما عملی نشدند؛ وارد توافق‌هایی هم شده‌ام که هیچ شانسی برای انجام‌شان وجود نداشت، اما اتفاق افتادند؛ فکر می‌کنم توافق [با ایران] انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128684" target="_blank">📅 18:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128683">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=sA4MHM429lRrxNZvhQrU2nOti8zT6PKjxwPm81cgdawBS1-N3ObVaTLTuidTy57vYtCcBSWy10K529Im4iY8uscXHcmtpkoTgte-6cZ4RpY36bPpVan0wkwEMfahmlB4u48Ll78LfQE0ehMHXNwJ3t8dGME6AMZpEfgJbNTtNMZkehNg45DB8qXdtSLvhbc-c-KO-vnWSlJs80JVRQEWA58kcJ9GdnbWaOlz3wz4irygTCfRY3F0JxDZxebnuwI3s2owgFSVAGnpioZJ_b9qCqySxFiZAJRWwY6B9so3R5_WspSz6z0MT_l2FNrh3XLWJ6Inz5tB3TT899i3cx0exg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35d9ebf38.mp4?token=sA4MHM429lRrxNZvhQrU2nOti8zT6PKjxwPm81cgdawBS1-N3ObVaTLTuidTy57vYtCcBSWy10K529Im4iY8uscXHcmtpkoTgte-6cZ4RpY36bPpVan0wkwEMfahmlB4u48Ll78LfQE0ehMHXNwJ3t8dGME6AMZpEfgJbNTtNMZkehNg45DB8qXdtSLvhbc-c-KO-vnWSlJs80JVRQEWA58kcJ9GdnbWaOlz3wz4irygTCfRY3F0JxDZxebnuwI3s2owgFSVAGnpioZJ_b9qCqySxFiZAJRWwY6B9so3R5_WspSz6z0MT_l2FNrh3XLWJ6Inz5tB3TT899i3cx0exg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اروپایی‌ها به ابن نتیجه رسیده‌اند که حق با من است
🔴
خبرنگار: ما در این اجلاس شاهد برخورد بسیار گرم رهبران اروپایی با شما بودیم. آیا فکر می‌کنید آن‌ها دارند با جهان‌بینی شما همسو می‌شوند؟
🔴
ترامپ: خب، فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. راستش را بخواهید، من معمولاً همیشه درست می‌گویم. فکر می‌کنم آن‌ها معتقدند حق با من بود و الان حس خوبی دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128683" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: من معتقدم ایرانی‌ها یادداشت تفاهم را اجرا خواهند کرد
🔴
ترامپ : ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
🔴
شاخص‌های بازار سهام به لطف توافق با ایران در حال افزایش هستند، در حالی که قیمت نفت در حال کاهش است.
🔴
ما ایرانی بدون سلاح هسته‌ای خواهیم داشت.
🔴
ایران ۴۷ سال از جهان سوءاستفاده کرده است و توافق فعلی من دیواری است که مانع از دستیابی ایران به سلاح هسته‌ای می‌شود.
🔴
در حال بررسی تحریم‌های جدید علیه روسیه هستم.
🔴
توافق با ایران انجام خواهد شد و آنها می‌خواهند به زندگی عادی برگردند.
🔴
من مانع از دستیابی ایران به سلاح هسته‌ای شدم و تفاهم‌نامه با آنها بلندمدت است؛ من معتقدم که به قرارداد تبدیل خواهد شد.
🔴
اگر ایران یادداشت تفاهم را تکمیل نکند، دوباره به نقطه شروع برمی‌گردیم.
🔴
ما به ایران رفتیم و آنها را در هفته اول از نظر نظامی شکست دادیم و من می‌خواهم اسرائیل حس قضاوت خوبی داشته باشد.
🔴
من معتقدم ایرانی‌ها یادداشت تفاهم را اجرا خواهند کرد و اگر این کار را نکنند، ما بمباران را از سر خواهیم گرفت.
🔴
می‌خواهم اسرائیل بتواند از خودش دفاع کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128682" target="_blank">📅 18:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: اسرائیل مجاز است از خود دفاع کند اما من می‌خواهم اسرائیل با تدبیر عمل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/128681" target="_blank">📅 18:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdEEGewj99fa2m81sl0TJGXBFl3b5TJ42pEIJN1We_obuKj8EcRutVqZ-1et3y_P-XjuK9bGDDVEvi0N6kDcQZ46qSzAUQiVCUlsKurx3J9DfmE8iZt4AyEXJnfq5jqAY6CsjaDIy002VVR5a8N4ETH-yvtIBAGOrQLnIzH11WXdXLQ77xMFHpVf7DKivInmLe3pFng-uHvAxEgxiU383Uc-aC0p5agAiBBzFmCHl-wuQroRAYQ1uJ4noO35OiFZvpUc2LU_EQ0hVU9pw7YmDXh-wvHESuf4l6qakakbRM462TAyBPJ08kb3Kkg2OuUms6E81EZ6fOVa75miP_Zt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
من در عرض ۴۵ دقیقه از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس به ورسای برای صرف شام با رهبران فرانسوی و دیگر رهبران اروپایی خواهم رفت و بعد از آن امشب به خانه بازمی‌گردم!
🔴
این سفر یک موفقیت بزرگ بود، اما عمدتاً چیزی که همه می‌خواستند درباره‌اش صحبت کنند این است که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد!
🔴
شاخص‌های عظیمی در همه بخش‌ها برای اقتصاد ایالات متحده وجود دارد، به طوری که امروز بیشتر از همیشه افراد مشغول به کار هستند.
🔴
بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری شده است، با تمام کارخانه‌ها و سایر موارد، اما نکته مهم این است که شاخص‌های اخیر بازار سهام به دلیل توافق افزایش یافته‌اند و به همین ترتیب، قیمت نفت به سرعت در حال کاهش است! رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128680" target="_blank">📅 17:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOINsKBFRly78CN20JCKB9pS1ToZhyPnoKdDE9zPCoFld31if_Zah-jADn0VrY4sX4DqGcYILPeJYys4z-8YA9sQhnmmLpGPsmfWAiWmVOpMymWmMg6JxHDeW3D9Ju6W1Ekq7Tj8HAqO3ettTlCY3fI__m_B7kl4kROyzoY1SeDKas6xXNsZNbx_5762hpZHaRX4_Uhn0KAjtibDqTFeaKToMNf2wVWDxMcBxJzxp8LbxYQf61jU-NdA5co2L2mOZ5-pAV1w4JitHciwkebLqrpadi3L3IAo0GIu7gV-apRyrEWLxjq5zZdggLHUJkWEtzXsamnelEz8hwkBjXcMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128679" target="_blank">📅 17:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
🔴
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128678" target="_blank">📅 17:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c64bf468.mp4?token=CsEdxD9BUTWNMzFy5V6lTjGD35xjhk4ZrhHN-A9ZDIyAUqX24NCx2aaQM_eZdb9Z1CF6-gMfxMllKK4KIvGA15-FRqRVhDME3d7fHIxY3FKQ5twGZiFf-YuSSMwHJceDn7j15JKKGgByh5gDqoFzJeQkXpZrIx6AZtw6CRUsjXDpL36ReeeaDmk7Qg2v1d3VN7On0Q2bKzgD-e_KUxDdzuT8XUT2nvZokEpMEiiOnZN5-Q6a6KAUsL6GwKwpvtRFSeHSayzjWUHicZH1qw5gn086HvabZuTy_8IN77eT0X9w6ocF8dZXa4SgMxWzN35TpwtSrG5SLeKlnr2Z5z6KxpAyjTHj2cXWcDIs6tn3OsRxB59qZSGUht6vul876FH7PUZtAXqL_kqz2S8A5YlkdW9lAGnorq0b286ThoFDqhja5273cdonbsje2EpWPdr1alxYoiEzUyQOemS_ziKmfMx4Gfx8OVqKQVRdNjj4c__YLzSuZ5a-f-P8qjPKCIwviVEfWOjAtgajtC0NcKWoqncTxHOC4tYIRmNeulnzXBwGr9RPFeYr8dYk_OhnPMMQERJWtG03XOrd0QLKOrE6GRphCgSzyec-AoVNTVyYMRTldE2qRdzu9nSeO7zYVjmUkfwrnLmUqYd_LZUBojwifrDc5KdWxYBf1_2q_QLR8YY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c64bf468.mp4?token=CsEdxD9BUTWNMzFy5V6lTjGD35xjhk4ZrhHN-A9ZDIyAUqX24NCx2aaQM_eZdb9Z1CF6-gMfxMllKK4KIvGA15-FRqRVhDME3d7fHIxY3FKQ5twGZiFf-YuSSMwHJceDn7j15JKKGgByh5gDqoFzJeQkXpZrIx6AZtw6CRUsjXDpL36ReeeaDmk7Qg2v1d3VN7On0Q2bKzgD-e_KUxDdzuT8XUT2nvZokEpMEiiOnZN5-Q6a6KAUsL6GwKwpvtRFSeHSayzjWUHicZH1qw5gn086HvabZuTy_8IN77eT0X9w6ocF8dZXa4SgMxWzN35TpwtSrG5SLeKlnr2Z5z6KxpAyjTHj2cXWcDIs6tn3OsRxB59qZSGUht6vul876FH7PUZtAXqL_kqz2S8A5YlkdW9lAGnorq0b286ThoFDqhja5273cdonbsje2EpWPdr1alxYoiEzUyQOemS_ziKmfMx4Gfx8OVqKQVRdNjj4c__YLzSuZ5a-f-P8qjPKCIwviVEfWOjAtgajtC0NcKWoqncTxHOC4tYIRmNeulnzXBwGr9RPFeYr8dYk_OhnPMMQERJWtG03XOrd0QLKOrE6GRphCgSzyec-AoVNTVyYMRTldE2qRdzu9nSeO7zYVjmUkfwrnLmUqYd_LZUBojwifrDc5KdWxYBf1_2q_QLR8YY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: من شاااشیدم وسط ایران مذاکرات و دوقطبی‌ای که میگید، مذاکره اوج بیشرفیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/128677" target="_blank">📅 17:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNEFYhwQfiLTQH_cLsEFZlSvh_KbyGKnEWtQoxU32ABtOxG2O7vrikwlUQxdlMtXDhATEHSy8y0Vd1PQQJEgOngAnQjeje5H0ujtk_FX5N-Cwxp5g54SBspXnqPc8PbtzhHLVucjDOs0H4moG32zrGoGwAsjqJ1C_pqOFv4_UJuB__0ofxiNxVKOO60bpc3rGHYEaa-g--QXSZ51qF0NbiD023eJSL0YVd23C1zjdRwNNS3f1SriFX5maW8OUfTYxlqX189hsx6gylj0rvAcENPU2PHMh0mq9PdGF2QQg9TvlzcU5L2WAo6UoRa80hTpi3lSgQa-RciWtUm6nFb6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایرانخودرو بازم قیمت‌ها برد بالا
‼️
🔴
ایرانخودروی حرومزاده الان که دلار و طلا کاهشیه و ورق فولاد هم تو بازار زیاد شده چرا بازم گرون میکنی؟
#فساد_گسترده
#فساد_سلولی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128676" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47c77e203d.mp4?token=Z6QzojwPBPncfGeh5rW1PvplePvbVxiQ7ORqBrbuYaJBRByP-zRnimALRIDCq_6M8semvQXpZSzJFxhstVqf-0XnYyFE_gYNGyBhNgDNYsm7SwRJ1l-2V2MSpmS44JnobZdFlQ0jBxeo2EXdKVvcF0-5ucEwgB9yyWrlcqzL70OyIYSovIv5S5r0-z7hIS_1J4VwTAZHZJL0ujXhpaCJ70ZdUNA_6gp9-YhcKcBxGu4M7yOALx_icsEhobLrtEbd7aU0cAXonsssXUQwVn9ku0cVI3ph8dddSAt2EBVaOMlxhCPtXfyueFeaeRPbHeIGX4haPEhbZ6spU4mNH7TFxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47c77e203d.mp4?token=Z6QzojwPBPncfGeh5rW1PvplePvbVxiQ7ORqBrbuYaJBRByP-zRnimALRIDCq_6M8semvQXpZSzJFxhstVqf-0XnYyFE_gYNGyBhNgDNYsm7SwRJ1l-2V2MSpmS44JnobZdFlQ0jBxeo2EXdKVvcF0-5ucEwgB9yyWrlcqzL70OyIYSovIv5S5r0-z7hIS_1J4VwTAZHZJL0ujXhpaCJ70ZdUNA_6gp9-YhcKcBxGu4M7yOALx_icsEhobLrtEbd7aU0cAXonsssXUQwVn9ku0cVI3ph8dddSAt2EBVaOMlxhCPtXfyueFeaeRPbHeIGX4haPEhbZ6spU4mNH7TFxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما : شماها دارید با کسی مذاکره میکنید که به رهبری تهمت همجنسگرایی زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128675" target="_blank">📅 16:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68014de410.mp4?token=cDahsA0sJvFtOUEIpZ6RcfgNLl0nGKiFCWIi-T7bSTNUAkRaomDQgUTdqLCHU6oN0QKUrN4vmrCznfKwaJpcvehKbaufd-jSlUVcgDu9ZTEeIke4gezlIztSOivBsqUMXn6hmnFvZX_X8VxHO0P4dpsnYGfmHzcVzq4Tg-J9vf44VXhxUhIULvdM_Byy3Zy7cHZbkqgGZ9uFD8LTB8MSoc9u2IrjwMGQpw8A7XTqo1KUGSt9lKUHFwUDk1XgF9RKUCdunJMyyX_fD-pq4vqEED278hR3T--B2VSFx9pg8prDn_mbIpRP4StElMZC4kfQbETOvZPsP__fvLyLgzt2hSXx6dfqPcIRF7nRqurQ6EN_V8hCwcJJM_x1BkwqZ8DJCXnrbi6dbIPAEDwJKywxwIkzYAUbtlwQUozElLvOF7ytorXg31WTLrA9AopjOzUH9kpSPFBP2LufhLDqha75lkf_zZenreOzlnzHVq5sCzeQHsOkBqKjN7ktMcgRRZLL6p_ytGyN6FfR_NXgw6IXYrbosew6m-ILTALlF-I833qbpYT4fs9Uwd66zd2ICUKTLhKsX2KQFsuefyBchfg6Piqc0jaET2yGe7hqWZfiZ4NI96Waq-f4EkyTo7xtK9VW89kQsEpAsa_4hiKdE8XPlGBdFhbPDUlErrJOLV0JnO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68014de410.mp4?token=cDahsA0sJvFtOUEIpZ6RcfgNLl0nGKiFCWIi-T7bSTNUAkRaomDQgUTdqLCHU6oN0QKUrN4vmrCznfKwaJpcvehKbaufd-jSlUVcgDu9ZTEeIke4gezlIztSOivBsqUMXn6hmnFvZX_X8VxHO0P4dpsnYGfmHzcVzq4Tg-J9vf44VXhxUhIULvdM_Byy3Zy7cHZbkqgGZ9uFD8LTB8MSoc9u2IrjwMGQpw8A7XTqo1KUGSt9lKUHFwUDk1XgF9RKUCdunJMyyX_fD-pq4vqEED278hR3T--B2VSFx9pg8prDn_mbIpRP4StElMZC4kfQbETOvZPsP__fvLyLgzt2hSXx6dfqPcIRF7nRqurQ6EN_V8hCwcJJM_x1BkwqZ8DJCXnrbi6dbIPAEDwJKywxwIkzYAUbtlwQUozElLvOF7ytorXg31WTLrA9AopjOzUH9kpSPFBP2LufhLDqha75lkf_zZenreOzlnzHVq5sCzeQHsOkBqKjN7ktMcgRRZLL6p_ytGyN6FfR_NXgw6IXYrbosew6m-ILTALlF-I833qbpYT4fs9Uwd66zd2ICUKTLhKsX2KQFsuefyBchfg6Piqc0jaET2yGe7hqWZfiZ4NI96Waq-f4EkyTo7xtK9VW89kQsEpAsa_4hiKdE8XPlGBdFhbPDUlErrJOLV0JnO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اوکراین، میخایلو فدوروف:
در حال حاضر، ما یک فرصت طلایی داریم و در ۶ ماه آینده، برتری در میدان نبرد خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128674" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
قالیباف: رابطۀ ایران با چین رابطه یک مشتری یا همتای تجاری نیست بلکه به معنای واقعی کلمه باید شریک باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128673" target="_blank">📅 16:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128672">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9370552a27.mp4?token=Y3ijc04zRLab9cBXlTx_PDY-A5dttzsRXjlIeGZeHFNK90o-LalLZCx9Y_3ST4d4tX51aS18WFMBQ0GoxQwEw7w1n1g9cGZrrv4yxCUnxwYctsJ14zPu_Xo_LV1rqf49GvJusboHeEvjlfZYWyWIn_ZMgwDx5L01iUDJIe3pZdaqkwx3qH9oIprqGvj-Bs92Z88bZojiHzOaBPUh9XTWcsQ0N8vasrJaUSH09fSOwcs5dQlf-22W5Asq-O-_WZUhhsBHFDz0LI_b3kVYPlx6xBP_zKER2pEpRY-e3EEk3RsHzPAmQ7uDqTSXR7fqn2SF2FGXr1LV1E2WqPlYFqwllEkHMZnCGdbBglZ-uX9L1MyUa4VupKhJsnxCjnpi3vfJUQBYWFeZYzR6YRXBfhmsFsjkUrUh7kxSajM5FxlajIZihiqX3s58gvdcp72QkEyAXSqC_Jv7rHm_8DeTXTGlr8GhTpgztihKPEL2wQyEEvJ321pak1DQgzAvORxSezeTlUGsKu4xg98v_v_rqJCI5yRFVEJkimF2vlB0E1d6QhCSd8KHFTTzj9zSTLN8AN48vPgLjT1185eZMQkPOBx879Mq4VcbmmiLOPn89AgaHdQq_sGpUI7ssk44smF92kUdIWn7vH_Iht7mSY7wC_g0BKbCCYTYvt2FsU8paVNocWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9370552a27.mp4?token=Y3ijc04zRLab9cBXlTx_PDY-A5dttzsRXjlIeGZeHFNK90o-LalLZCx9Y_3ST4d4tX51aS18WFMBQ0GoxQwEw7w1n1g9cGZrrv4yxCUnxwYctsJ14zPu_Xo_LV1rqf49GvJusboHeEvjlfZYWyWIn_ZMgwDx5L01iUDJIe3pZdaqkwx3qH9oIprqGvj-Bs92Z88bZojiHzOaBPUh9XTWcsQ0N8vasrJaUSH09fSOwcs5dQlf-22W5Asq-O-_WZUhhsBHFDz0LI_b3kVYPlx6xBP_zKER2pEpRY-e3EEk3RsHzPAmQ7uDqTSXR7fqn2SF2FGXr1LV1E2WqPlYFqwllEkHMZnCGdbBglZ-uX9L1MyUa4VupKhJsnxCjnpi3vfJUQBYWFeZYzR6YRXBfhmsFsjkUrUh7kxSajM5FxlajIZihiqX3s58gvdcp72QkEyAXSqC_Jv7rHm_8DeTXTGlr8GhTpgztihKPEL2wQyEEvJ321pak1DQgzAvORxSezeTlUGsKu4xg98v_v_rqJCI5yRFVEJkimF2vlB0E1d6QhCSd8KHFTTzj9zSTLN8AN48vPgLjT1185eZMQkPOBx879Mq4VcbmmiLOPn89AgaHdQq_sGpUI7ssk44smF92kUdIWn7vH_Iht7mSY7wC_g0BKbCCYTYvt2FsU8paVNocWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم آلمان، فریدریش مرز، درباره تولید سلاح‌ها: من بسیار سپاسگزارم که رئیس‌جمهور ترامپ و کل هیئت آمریکایی تمایل بالایی به همکاری نشان داده‌اند.
🔴
همه ما مشکل این را داریم که در حال حاضر تولیدمان بسیار کم است.
🔴
این مشکل می‌تواند از طریق توافق‌های مجوز با شرکت‌هایی که ظرفیت تولید لازم را دارند جبران شود، و این شرکت‌ها هم شرکت‌های اروپایی و هم شرکت‌های اوکراینی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128672" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128671">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: ترامپ به اعتراضات اسرائیل در موضوع توافق با ایران گوش نداد
🔴
امیدواریم که مذاکرات فنی هر چه زودتر پایان یابد و صلح در منطقه برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128671" target="_blank">📅 16:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128670">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ایران امروز یک تفاهم‌نامه با شرکت سهامی خاص هلی‌کوپترهای روسی برای ۲۰ هلی‌کوپتر سری Mi-8/17 امضا کرد (۴ تا از آن‌ها قبلاً قرارداد بسته شده است) که باید تا مارس ۲۰۲۷ تحویل داده شوند تا برای مقاصد اطفاء حریق، انتقال پزشکی و نجات استفاده شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128670" target="_blank">📅 16:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128669">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ادعای سی‌ان‌ان درباره مفاد متن توافق ایران و آمریکا
🔴
سی‌ان‌ان مدعی شد از طریق یک مقام آمریکایی به تفاهم‌نامه ۱۴ ماده‌ای بین ایران و آمریکا دست یافت و محتوای آن توسط دیپلمات دیگری که این توافق‌نامه را دیده است، تأیید شد:
🔴
آتش‌بس فوری و دائمی بین ایران، آمریکا و متحدانشان در تمام جبهه‌ها، از جمله لبنان، با تعهد هر دو طرف به عدم اقدامات خصمانه یا استفاده از زور در آینده.
🔴
هر دو طرف موافقت می‌کنند که به حاکمیت، تمامیت ارضی یکدیگر احترام بگذارند و از دخالت در امور داخلی خودداری کنند.
🔴
توافق نهایی ظرف ۶۰ روز مذاکره خواهد شد و تمدید آن با رضایت متقابل امکان‌پذیر است.
🔴
ایالات متحده بلافاصله محاصره دریایی را لغو خواهد کرد، ترافیک دریایی را ظرف ۳۰ روز به سطح قبل از جنگ باز خواهد گرداند و نیروها را ظرف ۳۰ روز پس از توافق نهایی از مناطق اطراف خارج خواهد کرد.
🔴
ایران کشتیرانی تجاری از طریق خلیج فارس و دریای عمان را ظرف ۳۰ روز به سطح قبل از جنگ باز خواهد گرداند، از جمله مین‌زدایی و رفع موانع فنی.
🔴
ایالات متحده و شرکای منطقه‌ای یک طرح احیا و توسعه اقتصادی ۳۰۰ میلیارد دلاری برای ایران تدوین خواهند کرد که جزئیات اجرایی آن ظرف ۶۰ روز نهایی می‌شود.
🔴
ایالات متحده متعهد می‌شود که تمام تحریم‌های ایران را تحت یک جدول زمانی توافق‌شده، شامل تحریم‌های سازمان ملل، آژانس بین‌المللی انرژی اتمی و تحریم‌های یکجانبه ایالات متحده، لغو کند.
🔴
ایران تأکید می‌کند که هرگز سلاح هسته‌ای تولید نخواهد کرد. مسائل معوقه در مورد اورانیوم غنی‌شده، مواد هسته‌ای و نیازهای هسته‌ای ایران در توافق نهایی حل و فصل خواهد شد.
🔴
تا زمان دستیابی به توافق نهایی، ایران فعالیت‌های هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا گسترش حضور نظامی منطقه‌ای خود خودداری خواهد کرد.
🔴
وزارت خزانه‌داری ایالات متحده بلافاصله معافیت‌هایی را صادر خواهد کرد که به ایران اجازه صادرات نفت، پتروشیمی و خدمات بانکی، بیمه و کشتیرانی مرتبط را می‌دهد.
🔴
دارایی‌های مسدود شده ایران به تدریج با پیشرفت مذاکرات آزاد می‌شوند و دسترسی کامل طبق سازوکارهای مورد توافق دو طرف اعطا می‌شود.
🔴
یک سازوکار اجرایی مشترک برای نظارت بر رعایت توافق نهایی ایجاد خواهد شد.
🔴
به محض شروع اجرای مفاد کلیدی - از جمله بازگرداندن کشتیرانی، معافیت از تحریم‌ها و آزادسازی دارایی‌ها - مذاکرات در مورد عناصر باقی‌مانده توافق نهایی ادامه خواهد یافت.
🔴
توافق نهایی از طریق قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تأیید خواهد شد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128669" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128668">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
استرالیا امروز سطح عمومی هشدار سفر برای بحرین، اسرائیل، کویت، قطر و امارات متحده عربی را کاهش داد و از شهروندان خود خواست در مورد ضرورت سفر به این مناطق تجدیدنظر کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128668" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128667">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
اسرائیل در حال آماده‌سازی برای فروپاشی توافق صلح آمریکا و ایران است و به نیروهای نظامی خود دستور داده است تا به توسعه بانک‌های هدف ادامه دهند و برای تشدید احتمالی آینده آماده شوند، معاریو گزارش می‌دهد
🔴
مقامات اسرائیلی معتقدند این توافق احتمالاً پایدار نخواهد ماند، اگرچه اذعان دارند که اسرائیل به متن نهایی شده به طور کامل دسترسی نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128667" target="_blank">📅 15:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128666">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
تسنیم: اختلال خدمات بانکی ادامه دارد/تجهیزات شبکه فرسوده هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128666" target="_blank">📅 15:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128665">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نخست‌وزیر آلمان، مرز، در مورد ایران و لبنان: تنگه هرمز باید بدون هیچ محدودیتی باز بماند، بدون هیچ «اگر» یا «اما»یی، و ایران باید به‌طور دائم و قابل‌تایید برنامه هسته‌ای خود را پایان دهد.
🔴
صلح باید برقرار بماند — و این نه تنها به ایران، بلکه همچنین به لبنان، به‌ویژه جنوب لبنان، که درباره وضعیت آن به‌طور مفصل بحث کردیم، نیز اعمال می‌شود.
🔴
آلمان کمک خواهد کرد. در منافع ماست که صلح برقرار بماند.
🔴
ما به یک خاورمیانه و منطقه نزدیک پایدار نیاز داریم. ما به شفافیت و آزادی در مسیرهای دریایی نیاز داریم. ما به قیمت‌های پایدار انرژی نیاز داریم.
🔴
کمک‌ها ممکن است شامل تعهد نظامی نیز باشد. دولت فدرال زمانی که و اگر شرایط لازم برقرار شود، یک مأموریت مناسب را به پارلمان پیشنهاد خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128665" target="_blank">📅 15:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128664">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نخست‌وزیر آلمان: همه شرکای G7 مشارکت نظامی و مالی خود را به اوکراین افزایش خواهند داد.
🔴
پیام به روسیه روشن است: همه شرکای G7 فشار را بر مسکو افزایش خواهند داد، از جمله از طریق تحریم‌ها.
🔴
این امر لحن جدیدی در وحدت و عزم اقیانوس اطلس ایجاد می‌کند.
🔴
توافقی که بین رئیس‌جمهور ترامپ و رهبری ایران به دست آمده، موفقیتی واقعاً بزرگ است.
🔴
ما همین امروز می‌توانیم آن را ببینیم، برای مثال در قیمت نفت که همچنان در حال کاهش است. این نشانه‌ای خوب است و روابط تأمین به وضوح به صورت سیستماتیک در حال بازسازی هستند.
🔴
اکنون باید این توافق با مذاکرات بیشتری دنبال شود، به ویژه دور دوم گفتگوها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128664" target="_blank">📅 15:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128663">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ درباره سیسی مصر:
او در هتلی بود؛ من با او ملاقات کردم و ما عاشق هم شدیم، عمیقاً عاشق.
🔴
شیمی فوق‌العاده‌ای داشتیم. من دو برابر مدت مقرر ماندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128663" target="_blank">📅 15:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128662">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: من مسابقات جام جهانی را دنبال می‌کنم و کشورهای مختلفی از شمال آفریقا مانند مراکش و مصر را می‌بینم.
🔴
آنها بسیار با استعداد و سریع هستند، اما جدا از هم هستند
🔴
پرسیدم: چرا کشورهای شمال آفریقا متحد نمی‌شوند تا یک تیم بزرگ تشکیل دهند؟ اگر این کار را می‌کردند، به راحتی قهرمان می‌شدند!
🔴
این نشان‌دهنده کمبود رهبری در آنجا است. شاید بعد از اینکه کار نجات آمریکا را تمام کردم، بروم و برای ریاست آفریقا نامزد شوم، ما خیلی راحت پیروز خواهیم شد و قهرمان جام جهانی خواهیم شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128662" target="_blank">📅 15:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LvqUjzx0ZF1QXLGnccdaQAcDabeY95eU6RRjcWVCCK-HyxT8-8UqTWUOodzdxFDj5UlQ6NakwL7jbLzf4DNl7VrCFuzuMvcHjweeqfuMiYLFZT-i4bBK2dmqzg8OKN7vkG4o2OaYiO01ZXmN0dH9-8KnlKodynb1kDE9TpQ5yXr5f7qb45VgCk34mK5D0YNJlD-bxNeVrnFDNBeUjioXZCa_qM0qRgW2To7TjfN3SCeMsWoiSaQYm1Q9-FGGXBkjj1tkbJxCn_DW__mKQMVleK0b7n5JVZo-6QwEr59Mme7iBrRRtY9dtnT0MHSymdhbm93t5XZTf0HgybyN8oPqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/1ed7b41643.mp4?token=R3JQoSS51X_pJR5f_5WM8Xk3-oQVCZEwW0vsQnHh4AIwguPKD6-C5TIUutKGqhjErel2MGp526b_6IAhvtAkk214eXNGi0O_EclWfclYKsydlxFx3Z-cW5fqy2sap8J3UwEz4xA3mpcVqHdtXyDD6QO2IGgB6ZcaJKfqI2Rp6-NcTuOOXWnTjR6fHFZ7AJpsIx9ZKh4W4iVWeTCRMi1jcFG8TQXYE8dCpN-sxlnXgimB-5qIZLa2yUsV4X2KdaIS1IVpnDYfUGyKwCuSIsGSbcsBUEHoVbGJTS4d6oJLSItDO3JxeAekKFskt_-Fb3tWY8eA0j_YoVpaUf4JQ1xjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/1ed7b41643.mp4?token=R3JQoSS51X_pJR5f_5WM8Xk3-oQVCZEwW0vsQnHh4AIwguPKD6-C5TIUutKGqhjErel2MGp526b_6IAhvtAkk214eXNGi0O_EclWfclYKsydlxFx3Z-cW5fqy2sap8J3UwEz4xA3mpcVqHdtXyDD6QO2IGgB6ZcaJKfqI2Rp6-NcTuOOXWnTjR6fHFZ7AJpsIx9ZKh4W4iVWeTCRMi1jcFG8TQXYE8dCpN-sxlnXgimB-5qIZLa2yUsV4X2KdaIS1IVpnDYfUGyKwCuSIsGSbcsBUEHoVbGJTS4d6oJLSItDO3JxeAekKFskt_-Fb3tWY8eA0j_YoVpaUf4JQ1xjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملاتی را در نزدیکی روستای کفر تبنیت در جنوب لبنان انجام می‌دهند، جایی که درگیری‌ها بین مبارزان حزب‌الله و نیروهای اسرائیلی ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128660" target="_blank">📅 15:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: من با رئیس جمهور سوریه در مورد احتمال جنگ علیه حزب الله صحبت کردم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128659" target="_blank">📅 15:07 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
