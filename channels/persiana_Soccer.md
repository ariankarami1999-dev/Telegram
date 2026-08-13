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
<img src="https://cdn4.telesco.pe/file/PZCHdZ7JwV1hCeruZ_KRGAZPiN9-BRZ18wsiVT-A4_X5b7aQo47VCK0OtaFF_gPiei7LhQ6TUWQ3v5xUHHwTtJLKJf_g8ZHX71zT7SSwaseoAJOKbXMmKLJ1cjSb9C8x_otTbepEBWcL5JUF-e6IEmIG9VUG48ZsWVGZH_31ize4S2VSzb6t7vszVF50nZnnuEi6VxK2dSCRX-8Zv2M50FVNodkIwTuGAkNmt0q7Lcg4L8hXwi2tfFc19hU4lHVXKHAuo7v3C3JfBgiH6ivaG6jbsdp_U_NL3x_AaoEbVNQ3bcXnKHWbEf_sQnCMys4WsMwPfDQwFkgpSxRWpTZoBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 639K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 03:02:24</div>
<hr>

<div class="tg-post" id="msg-27679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=H-lw-0i4-LeY9TC23FjGrDvEb-AR0Bl9WSpnzc8ynAjQWsVGN8fV1nLmK_lBbqvpVKYpIuAtmZugom86U04OkmlF_RxULOYqdi5W-c9r8qnZ9UIyh5pnGsfLt9S-Yc-15CHruv9WyKi6xNpeg_YkTe0neKW8sSRvh3rHC-NnM6-7u4-E3zbcsqIrmdgiQ4rguZCAh2zIBL32rGhnIDShxLWq08JFAd498VOZ2hAVyl51Eyr0QvIhGdeDwkZNdvgZitwDstTKcSj-03R3UufSpa6H-z5kzpDFrSOZhrjqksMnEJcBNK9rkHhGAQ6ufYTFX-uQGz1zyvtPf-0i_cFRKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=H-lw-0i4-LeY9TC23FjGrDvEb-AR0Bl9WSpnzc8ynAjQWsVGN8fV1nLmK_lBbqvpVKYpIuAtmZugom86U04OkmlF_RxULOYqdi5W-c9r8qnZ9UIyh5pnGsfLt9S-Yc-15CHruv9WyKi6xNpeg_YkTe0neKW8sSRvh3rHC-NnM6-7u4-E3zbcsqIrmdgiQ4rguZCAh2zIBL32rGhnIDShxLWq08JFAd498VOZ2hAVyl51Eyr0QvIhGdeDwkZNdvgZitwDstTKcSj-03R3UufSpa6H-z5kzpDFrSOZhrjqksMnEJcBNK9rkHhGAQ6ufYTFX-uQGz1zyvtPf-0i_cFRKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌‌تند رضارشیدپور مجری‌سابق صداوسیما به‌‌طرح عجیب بنزین ۸۷ هزار تومنی:
هروقت درآمد روجهانی کردید بنزینم به نرخ جهانی حساب کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/27679" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boeMnTu2CmcsTUsWrzvZw9X8puSTpjxu0q1Wyqi5yPtA0VyAzrGxeIFQk_9mhvmh20Owa_GmrAhkJ3gouPTCPKiIbZF6yeAk0Ss-jKlcaICNY2mmLG_RtCVcRov0i9JDACRMZeDBO2z4xfLFygsao9CczHRg318L5P3a1Wa5Qgv2BcdegyjmkbC4sVtG4TldXDgcpi_EEx6PtNVwJ1hMWymJT3RJoJlTjeSMWcZOYg2tZ-2-vvhpcZqEzNO5v92qzM1fDb1XyAQWl72ZUDmTjTYH5BhF9hPlcqKNafKzos-_cYQWRD9AOlb9Zv5dbrdB2PL4QNStQqZtUseCT50Mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/27678" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoH33n3uJSgjp_KPNg6F5BwMY0J5Vs22k3mMMNr4_HQ8uyewGfMWcrZKQjTuzdQLqw5esa6CvDzcisWY3B3T8Y80gtqdcd3yd_SpX2ydZL2vPINOOTyIOeghYTX5JyTzCRbjhGxcHto1v7OZocDakJb3raicqK-GJ6eZ5F3LwbFR_y5CbFGcLVXLAdUcwTd_cHdsjcKS0uBoKw5EWmlJWQuJna00VeiqCLXOGY7YM2q1SMmc-hGpVpPJWfoA75GscuJCDVFwMwWjCdwuYZiZRTd5KXmfAtlxAAJNg-wrCa2OrKG8G8bGPoaT5fjNt8UPrii_uknfQ1uAyy1hALrpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
حذف‌زودهنگام اینترمیامی ازلیگ‌کاپ درحضور یک‌نیمه‌ای  اسطوره لیونل مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/27677" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H625TuxEfg_UCV-cN5WyvVM0uEvVqzgrFq2S8R_66LSM4qxhlJ9dP8F95hdmHTFQ8ipEzQlxKCCXz-z316DAkWSAsz8ugNIKa4pUYo6YVHwvEbqOsF6SNZGovvWbbks-DCdTjBUwBQd3niOTd_W7r8vJfkOGN3N1tgIRH7y7FUcMbirEmGC6VJMW_iNM7NOJ3kkj3gUQ97m7TEqHtDKzp73GpnALyv8XejKd2dPDhMIpYJLrtxpxE8LXXdrsZeYyi6PbWSIqKj4nAOtiPaoAMAt1DFR3YMpO3wxhSTlnheUtLgQk7OmY7I6sF--7iXmiCePjaNRUQVx6zq2kyiZGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تمامی قهرمانان لیگ برتر خلیج فارس در فرمت جدید؛ هنوز تکلیف فصل گذشته مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/27676" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr_hUEl7lteLnpFL8N5CjZ3cTtCI-dVjacb3UEO-NTB9_6N-cXop6h54RMkubnaAJ2xpahrYuK29F2EvWuz3EkpZMx5E9s2xbMbnCI7kVpZB1ZiHGcxmBGmYvB-Xrk8bwSOZhqBJHTeOcqp3f-ipbcp-QQQuwmdm9WLQFCUMiD1PiU5-UQxSPpk-ZsxxGD-e36JDhazL7C3nGn7mBaeIpCq5NS8j8Rpb8CH1bWtWd1ZaSA3DXpoGHZXxwqNcyobvzX6gEPCFVnSSxQpSznTkDFGEJSYy3QPhoS_1bU7r3z-eP6TjzpJD4gk8AUzzM5UXESTr_f7DyqbS9F5Rdb1XXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
شروع‌هیجان‌لیگ‌برتر ایران با فری بت
🤩
🤩
🤩
🤩
وینرو
⚽️
✅
باشارژ حساب کاربری و پیش بینی رقابت های لیگ برتر ایران درصورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری بت از وینرو هدیه بگیرید.
🎁
امکان‌جبران‌همیشه با وینرو برات فراهم میشه
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن وینرو
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa22
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/27675" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQOjHerl6sJkQNhXYCNZQDi6pPv9fEqny_IJQMZhf2BUlskSnmrbtoVaDB4LG8yCgTiUFpSAgWiDBJ2hEYM3pMmrneTpta9CKvzIAEFzWUL2ORffZipkINCRi0NPKqfajzUxEuUxrTqyAkY9QA33JtN5TJLLcDJKDNH8RKB_u3J9yS9wXl5qAW71q72JSrVBH1vYC6BJ6g_9kM0oHYGJoi5P7Y3k2Xj2W50t500XzXuPp37KUsfwzWnYOgupvxCaDDmhdWds3QGhrsvX70VPiw-q85U5WOUOuLupEPeTLQGQonjBPWYUpb8cBDDhfYxLmJ25qxQyJ_BJzWTfhsVWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe1ugp_URsnAPZJvhEtJZXbpS2cl3oi3cOYih-q3QM1zqO8C511vPPRyOStuqq3Xlg8iNR4OkYVCsOGBUhygOoq9Ccydv2pt4-SPid8sxVSyg_yMOiwuVvj-yTcUfJapvne6KSJ9t6DUNmTzGDs5KGgeNFDTz8u89RCKFSfTxyJ2P-kLzW9Il7YoOe-7XiajYMaSFFjMFka86-ciGsurGSk1aCiWSzUcL80-wkCy6qtjbBHprPzjhtWHduTJGxDgfXbSq8OJ7he5Eg4EGZzPs2_2oKYQIV8TZmLPf5LRjG77FziFfR-wVXDU8nIo1qAmPnH9rF05Chmr7r2NzGANJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم؛ سال 2024 در چنین روزی؛ رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/27673" target="_blank">📅 01:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27671">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op-8QU6u_byo7HFWRN4IUAkpdFuQWR2qDaHdnBNKo0jqMMJ-hIywM6YkumJUbG0FxIfd0qIfvV-GgeCsh79GsKLjjVutt3pU_rzglJMYsRAsIzXgax9IfHhX8sGrofiP5dWuWWoiI9mTX8wgGQlMtuAJO6bkbkWA8YUDPkEw_b54WUf1sF8GlcTUpOyEUzFB9GjDhKXjmJt-MRosuJVijWPVRjibMUh5clsVPJyv6wXd0FMkB9ZXbJjLVbtJaSSiA-MCYZLiPJlN24I8arcQhYZ8MnrnjqEqhc35Xat9VBpTfB9VAi0gOa6_V6f0JzbQwj0OkUsUALQeyU-pvVne7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=g3By_mQ4Kps_YdNTJo68OTaLz0ZJ2KWwYt9KzbNEbim8asMEgT5n8QsRhNyD94Fy6ibs4QgqBN_sHkAfWnQ_9RFR7jDWK11hKe7oPMOCezOkV-ldrgl9t8Qt2bCM2TWVFOhi3ySw533sQmH81bEn6C_54TMVMO5HgsiPl1AeqOdX9GYSuxRPRRO51TTeEWgzv6PHhxIbVVKTv-Ek2RXrDmttcG03QjmEjd_QWVfofDA4WygHuLUzg5b1WMEMOMB0nRpoOkxdmbvtlLwmJgsbrkGAqoJw9nNg6ZNIp24gvJqUsatwpfhf7vKuX0ueDuBrVOqKFCvmEjZUbxsJ1ni0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=g3By_mQ4Kps_YdNTJo68OTaLz0ZJ2KWwYt9KzbNEbim8asMEgT5n8QsRhNyD94Fy6ibs4QgqBN_sHkAfWnQ_9RFR7jDWK11hKe7oPMOCezOkV-ldrgl9t8Qt2bCM2TWVFOhi3ySw533sQmH81bEn6C_54TMVMO5HgsiPl1AeqOdX9GYSuxRPRRO51TTeEWgzv6PHhxIbVVKTv-Ek2RXrDmttcG03QjmEjd_QWVfofDA4WygHuLUzg5b1WMEMOMB0nRpoOkxdmbvtlLwmJgsbrkGAqoJw9nNg6ZNIp24gvJqUsatwpfhf7vKuX0ueDuBrVOqKFCvmEjZUbxsJ1ni0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2024 در چنین روزی؛
رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/27671" target="_blank">📅 00:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27670">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnRl44Ye1Vcy_5EkBJCL4QM0FRDkY5UAb51hmpqxKXCzbspAkjwkd1xdj-DmSq55AXiLw09qIdyMUA9MJdWsww_SraN58YkLBZXZSeNujxCgdZkwCy0vEYyZYX_BafFkjEtt9wxO348KBqx5STsQ-z06q30PdlfuOhMNNoKrtd3FGPpSWST3XDs5fRZLyy9YoAi_NSNpgjDmcdTbHEUFkEE1-YRAJZIALgo29IzxuM2M9KOkRwmZD3ThKPSlsjLkrh8a6AtsvkGN8-X0evA-t_Axn-wdKKmi_o-rvdVVvNAHgvluIJVEVIlnO8PyksbdLS0pkjbGtQlyFBZCypX4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛باشگاه ریوآوه پرتغال یکی‌از دوپیشنهاد اروپایی محمد محبی ستاره 27 ساله سابق‌باشگاه‌استقلال است اما رقم پیشنهادی این باشگاه 400 هزار دلار کمتر از رقم پیشنهادی تیم استقلال به این ستاره ملی پوش است. ایجنت محمد جواد حسین نژاد و محمد…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/27670" target="_blank">📅 00:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27669">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=IPu5QO3xD7ukBfXH0aA8y72UyKhe9OWsOzUP9YdXnsqQejMeyXSW2qhSV12FIe4jojKY0-imlpa_4rjLJ98hqZpEFf6FUklZD0mfL8GlcsqfUwj7qrd_VEaUhkxYmH6L9PpX6ybGki98U09wOUQsWXY_mN5TiQZIdZz0TOs2MPbh_k6atUEac54TRb3faft05OCMAq0QBI649MJUvABZtJZL3nCam00n4k9S0II1p76tGFaGQKyDyCW6YW5A-lXZgTp3qYK11a7eApUQa5XxMBqULydLwvXA57WudKHpoLCrm9xASn8UUETmGSEqNvjQGKlHHAdnE_pMEaSsKBuQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=IPu5QO3xD7ukBfXH0aA8y72UyKhe9OWsOzUP9YdXnsqQejMeyXSW2qhSV12FIe4jojKY0-imlpa_4rjLJ98hqZpEFf6FUklZD0mfL8GlcsqfUwj7qrd_VEaUhkxYmH6L9PpX6ybGki98U09wOUQsWXY_mN5TiQZIdZz0TOs2MPbh_k6atUEac54TRb3faft05OCMAq0QBI649MJUvABZtJZL3nCam00n4k9S0II1p76tGFaGQKyDyCW6YW5A-lXZgTp3qYK11a7eApUQa5XxMBqULydLwvXA57WudKHpoLCrm9xASn8UUETmGSEqNvjQGKlHHAdnE_pMEaSsKBuQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استایل‌ومدل‌موی‌جدید رونالدو بعد از ازدواج رسمی‌اس باجورجینا دوس دختر 10 ساله‌اش؛ ویدیو ریپلای شده هم ببینید خیلی سم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/27669" target="_blank">📅 00:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7E0k3IOPn5uasSgIAOTkIXU-cud2vKhrTWuWvDLfXwgRA9iKud0VBxzDEYrzYyrB75eUcHNOrOrg-vJ0MDAa0tHNwpbHUOYXPD5p7YdOQL3dejc9MLORhrY8T_PocGQyhADFuxVg_eY6dMgYxdSIUH7hhLJtfXj0hLC898pCStF7WMfYCBNu2mnRqCsOYVuz2N-M9XAz_4z8anzHPZC3JWgkfZnUqisWUY2BGvsUmvSTvog-268OpciFHY0UKGm9kHlRcYg6sAHtSet5jXDqe9__sXcVYznRBfZvTpf093JxL7emRLIkBmOHb5sIKK8Ap-CBk-vJf0uy3pNnKQtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/27668" target="_blank">📅 00:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDfPv9T1DEnJ7LZUH_fhe2-fTY_DMqL4hgkPNQ6gr8UN7Jg0Sd1Rd6pnQQujaJ3JfdBk5pvn78wBHAxUgcBEY706KDGtFVdEBflp1-w5NWVK9iWnYIJGccdGE733uje27Y6iqAx1MPmB2npO4nsT6LziuSkkTLoS395beIRGkV5kaisSW1sjhaY7DNgtv3-4jLwJ2vbseCp8z9PS-j3lhXAYGbJCiIy-PQpSEYbu9eGjo5Mx4cfyN9Yqh0QkvXs6vSwuqRvoYgBwMHigrE6NRW_qPuNuSPehWIfgBkIXi-SElGc--AKv447D4MhiOxH88tJRkwXfzPMMRoSmxYl1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/27667" target="_blank">📅 23:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید خود برای فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/27666" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keXq9xARmGHdew6ssJt-3KPiyuAb-1jgdKCJ41SKwQlgA4ZpSN98ylad5EMqbQtKj5XD5gXXfwaOXNEHTcMYGP7CGPNnKGBiatkYxNSAreqSCD1UmgxDe1mUPgyBYgvKd4xSrkCzm-lFfGV8rIaLqRtqI5Rnjs2IG1q81lo1jlWC02LkpaYf_CX-3xFr0AIOcUfS_Ov7o1x6_cNCK4jxQJjZzRpsRvHQWWcYND40qEsJoQFv-HW-YjQvqErxwawKjNrWL4srjM6bDZtmLD8wFiBpKuXdO_Au9M9dH3iGmoYfqLre8hVKXHvO3QIR5f2zx5d2RQGjtCAMEoRTM1KKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/27665" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUTNmP4uzyx4yz5WLz_VE6lTLv4F-BdBBwjHcpwTM-hv_RzlZv9qwo02hCQQah5XK7s3qm8l6zJE7vIoZF-ixcsABgLD3vnxiTAblShfJckM62MgHPCLltWoekoc8BdMvABWdJ6tw1Te4cl1KCW52Gd01zp2KPIIZw1h1VKZ_lmNyu9XFu2awxTMQFepsi4aK0preZmQXJTh55Aw_A0GyFWlKOTqsYQV-3q8fUwjRVlrdHu8T4u5pYMVCr7BIsS6-yDL7XD5Avjd1iCpqlZOjZv5jb-5o3RRaHVCPOZA4cG0ExzzIz05WBrbp2-ktQ2DcdOWCaex3WD2jBB4mrzOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/27664" target="_blank">📅 22:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5zes3r8-TlX6nXhEv-0T-Nz9JUOySDyRKTiro80yS9UJdl9z3w2WhvDjV5jfFLjMNsUDA9ytkwdgQpvMk4TWTj74xcP2wzuFM52KECpn1wCVRxUt6BdrYifjShYKum5lhQmna552wtY7imZlQrrorejX-wuvwRPxLv67yZTnyJG4FB4GrqxJ21y-CnBGxtJ-DfGeoyFogxB8mQPJgTrdMosUN6Wk3d8CUXk-ALD3h2ldpXsDiBenSywCOHXrG3kvFVFa7TQCsyFpVx67rof_-Uto-0Iblv7UInTg81nZG5U-jsTQGJBWBGlN35Kxs_tSJkKevq6E-g6d1RLyVYkXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/27663" target="_blank">📅 22:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27662">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b52oxodRmveKFgVC49Xgvk32x2RTIfDKghPA5MCoQB9iy7wz4sZK-JhG-yCqD3K2Y-mO1VdqOz7T5nG40B8qYyvz_uInk_spOlHmQt7CyxFX2ezQS5mPhWHFdUCSDOIvGPWtbkAErqK4ooy1NzwNwwKDlam0I5MxDCAKYpI-UeGlMnzKOlHYvp5fMVvE5pZg3dsOC_5LuwhgrOz8WKGUoywALx-4lygMYobQSOJByfGd7szX6mXmuG9dfyn6BaU6cVVBRcTFtmrXagwrB9edfRmQ_AiGkjbmR3eB0or-Z30zV_s2KSBvfUz_jGjR4jTAsURFcQhHbfyNcZjkd3ttNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌برمهران‌احمدی؛ روزبه‌چشمی و جلال الدین ماشاریپوف دوهافبک باتجربه تیم استقلال به احتمال زیاد دیدار با مس شهر بابک رو دست خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/27662" target="_blank">📅 21:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27661">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A60wUiuRGYW1S8N_XQOvv3sQr27-eGihb4dNOr35mJHdmMl63dOA9jJfq0mdCjVnsma2fZyQbTrMHsytkGj7l1GyEBZYgpFmevkrlGeziwZR_rVdbsiJtgYpAwp8xmuO-6lBY9NIlokdwlCjGe7c3vEVAJXpHVN3RETdWX3_Zfi3uXvppHglYaOdyfXKtB1jtutyW7shHnqnzDdb9x6MeEH5RKhZoqnC5D2WQdYWQaSVnq6Z-4YIcbnP6ZrPJJnJKD7ldcwViCaWlsl6vRgcSiI_4DkNhJKIixssbUWbEXuFIkY8mXF15GzErmtMg1IDMEtR6vZGzR-q0z3Q_3sb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
#تکمیلی؛ فران تورس مهاجم 26 بارسلونا با عقد قراردادی چهار ساله به پاری سن ژرمن پیوست. هزینه این انتقال برای پاریسی‌ها 55 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/27661" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2QPsjuD4nHc5UCd0h_UqxTXNe3q058f2h9kea19dWDRWQgiFcnccmQMtyXJBZ4-cFVml6_YEEfklJXo9XUT9Yjp84n8PMeAiimLXWLPMbrNLWKMOO3K0GOmIaGVCfxhQy1zwk9x1M7p-XjLS_iGc5RgIDV1_BA6QZ0mW8Flk3YSVRKFyGELXobfnvvpX6Ni0FOK3d7zAhYx9XdcByEL1GIpJMEq0csLYVqoFLF2PJgxE9645Hz3b0syB5cWdNr6ULvWJbewOW-JHzlkxoxpDUIhtRqdgJQiyfpvE1ROuAPaOeN-N_aFxQHe7hGTGwfDMGzYEG9wxuVZO-TScy7TSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درانتقالی‌برگ‌ریزون کریس رونالدو به شمس آذر پیوست و برای ماه عسل جورجینا رو برده قزوین.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/27660" target="_blank">📅 21:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAHPa7nztbqw8rfv-mShEMK-gIm0KNCoh2QRhn3cr5TjfZUlqnSHGwLURB81jJIpcuTu401lZPCLY7Oq4qXZT2wGWdELWdFVbAHL7mGod-2h58cbGkJILld860cpwcfGZsjP3F2pJxOrbB-EOspognstB7ZTHPTWOCyY75254biwtKfVUAe5WF86Uvtg4QCc-tNY8qwrGplhVo7Jyp_6LpwVnz81cYVOuVEqEpjOsFWIRkxAbk0VD1SKFH5yWdSv7mmTB4qeY8WM_8LFeqgUmU4Memh3o4_jAJdqSU04n1dzFk1vBJr59aIhv61GHG37zRSjqlJsYmSCsepx8jCJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی رسمی باشگاه استقلال تهران از کیت اول آبی پوشان پایتخت درفصل‌جدید رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27659" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=u7istISCszOqVftUcD0Jhh0S7sS-fxHDObheQVWy3QIO9pmeh5CFcGeNuR_d4UoSplqseJt75N75fQ-Y9PkbwT6MCFZ7vgm4rSMk0J0WtsiPozOLeUdfGDL976bJoQmYJUWoDmAzWpYRCamyk7WKkrt5eHBJ5_8bZzcvnvGdWwJ2VW1WK-mWvyNrA2TB8R8sAfRXogQgNHmYUFyU04_2fZjOcDCuI_yXpGFowSVQCBTE9Vhoy830MnDb7MQ6zU0LP_l0MRK6cOW5-rt6-FC3xP1B6TWW3DTu6Y1MqJamVBtwULdzUyddANlLZ5zTnltq4wpmy2NPCds3WdoCQeCTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=u7istISCszOqVftUcD0Jhh0S7sS-fxHDObheQVWy3QIO9pmeh5CFcGeNuR_d4UoSplqseJt75N75fQ-Y9PkbwT6MCFZ7vgm4rSMk0J0WtsiPozOLeUdfGDL976bJoQmYJUWoDmAzWpYRCamyk7WKkrt5eHBJ5_8bZzcvnvGdWwJ2VW1WK-mWvyNrA2TB8R8sAfRXogQgNHmYUFyU04_2fZjOcDCuI_yXpGFowSVQCBTE9Vhoy830MnDb7MQ6zU0LP_l0MRK6cOW5-rt6-FC3xP1B6TWW3DTu6Y1MqJamVBtwULdzUyddANlLZ5zTnltq4wpmy2NPCds3WdoCQeCTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
کل‌کل‌جالب‌مهیار حسن و مریم ماهور برسر بازی پلی‌‌استیشن؛دختریکهPES و FIFA بازه‌اگه‌زن زندگی نیست پس چیه؟! تو یه بازی هفت تا زده مهیار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/27658" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=UwWJ8EZ5cgQO8INg-qWal1JPizPghfMyY4arTj-PXbGM3JLT3LRynF4EXCSl_fkGCmInEOj9XA1Dp3m-x6jOxJgs4RHNwEk1UMndCQobcnedq9M_TEm2RMLlHO_kbg__yHTQfVuvsV0WwPsFSR0Fi61MLq0gnPeSWDvH0NcrPqW9w8hSWIlfHhn8_Vpb3hW2JM5DfvBaQyTujqjku42PCZMmFiSLh05owz0mUTVvfIUVASo2Mw5nU3lfDJsYZS-d7QJR8PgY0oh-DidV2sOcszdprO92MqHx42uLSuSmSWK6g9m7RPivBNW6Z7DPBLH_GtF89465Q4NcphFe6_q35yBYNAL4fba-S3G7a8UfAHRCvDMw9bQdpzAgihJuV6Ryl6wbMMIOqDfX5cTNiMbn2r-9WGlHn8EviVtJmdHNLMOlGHtvfxRoWN3i7_tHEVpkPI1B5t7vvSH1w6oCrdKIhlTMbHDmmCf93UKcIEMZ4KopSGCLRpUjHo0hlzyX7aqCHhJmlHf4pj9neC9rQ4jZ-fkbAi5jpg4uSlaiiAtOVna-g8nLbqW1AfKZTUXn4i6UgKlOMfZTNZeMy1_aOB8_6pxRSMryDI9fWdqhj5U5SfTbmwwlVxe50xF1YwOXhz_51fSrV8Q5AVUKL2yicVSBXfbUd-KskqBfjzzdQgPbr4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=UwWJ8EZ5cgQO8INg-qWal1JPizPghfMyY4arTj-PXbGM3JLT3LRynF4EXCSl_fkGCmInEOj9XA1Dp3m-x6jOxJgs4RHNwEk1UMndCQobcnedq9M_TEm2RMLlHO_kbg__yHTQfVuvsV0WwPsFSR0Fi61MLq0gnPeSWDvH0NcrPqW9w8hSWIlfHhn8_Vpb3hW2JM5DfvBaQyTujqjku42PCZMmFiSLh05owz0mUTVvfIUVASo2Mw5nU3lfDJsYZS-d7QJR8PgY0oh-DidV2sOcszdprO92MqHx42uLSuSmSWK6g9m7RPivBNW6Z7DPBLH_GtF89465Q4NcphFe6_q35yBYNAL4fba-S3G7a8UfAHRCvDMw9bQdpzAgihJuV6Ryl6wbMMIOqDfX5cTNiMbn2r-9WGlHn8EviVtJmdHNLMOlGHtvfxRoWN3i7_tHEVpkPI1B5t7vvSH1w6oCrdKIhlTMbHDmmCf93UKcIEMZ4KopSGCLRpUjHo0hlzyX7aqCHhJmlHf4pj9neC9rQ4jZ-fkbAi5jpg4uSlaiiAtOVna-g8nLbqW1AfKZTUXn4i6UgKlOMfZTNZeMy1_aOB8_6pxRSMryDI9fWdqhj5U5SfTbmwwlVxe50xF1YwOXhz_51fSrV8Q5AVUKL2yicVSBXfbUd-KskqBfjzzdQgPbr4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27657" target="_blank">📅 19:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiuKoeAeKX27_iuRKMYt3iPTAhuHwhE9kfwpcQTpLKLqtLQOfTg7Essg3vN7YmDg_TRDN16GqTd489RChFuVS25OwkE0WLP3q2SKD47Qd9QKmy_GV8wPu-XGfBaB7snDH3Qog-UZYmr2U2RS-ZbNgiOMYzw2Hax9DX9iowU_e5Aleyb7DfDy3zxgkaLzQ5Sp7bjMMUy1dUH-faKHuEIkjJrkXxQs8xeU31qyGl57MqangdLTp36Tr_zRvIUPO62bqKq-BRCN3yj1NpnFg5ZvO8k3gFB-JqzogWaCbTIuKEypM9MBSHDQTNwi92p1VzkyxCeus9hfdOo2rxJDLLvHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
طبق‌اخبار دریافتی رسانه پرشیانا: محمد محبی از دوباشگاه اروپایی آفر رسمی دریافت کرده و اعلام کرده ظرف 72 ساعت‌آینده‌تکلیف باشگاه جدیدش رو مشخص خواهد کرد. حالا اگر با هیچ کدوم از این دو باشگاه‌به‌توافق نرسد احتمال‌اینکه با استقلال قرارداد امضا کند و قرضی راهی…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27656" target="_blank">📅 19:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vm2GcYA2M1yjlpEGSeYCDSy-uBgbcyoSeVYfz5yLwGTfmtRGUnIdyiI1S_DKBXTZHvsBwJrTW15bIwbVpxHxxNpCIaCUXsKgEWyVXSIF9xis27jifZE5xaZYSfu1erd377CTntTEcAb1giwyrtSxtX8-1vR_K2qNng7ElrAJzMpT6zBgrjDhJgLIl83IzjIGfTAo76YpnkWJoN6M2ncVWONEQh7reSeI2nCKycGAlhrc6P5QLYoaTJm-pyCaTJyxMwVVSnexLqFZzbnJA7xZu_qD6wep4HPG76al_bTBQJXFYEqKVdzFScDT_7KzpShauMDtI_I_2IXb4gJBN55IqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/27655" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27654">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjc98Obbh6ePppQ40-vIQaFzSM1M129TARZlF9UFBcyDEfldwKCnhjYYM9j8fsrUIDFH8xwloebXQ_TrKiDMyS0D0M1ih7yxBq9c1CeBWJeflYyRh6a5W9jRo2S3_-p5LUQzZCBbkj7TT0qQ0ul77ZHTANwedMu-vRWBORh_pmhf_md_T5W7RescK4YhxjBZVRvMSgSpsOaxR4-EjR-lmB9CZpcTkS03oZAfdgntKEXtfjvxj9E9w76VZpr-TqthjqoIx4KEFNua5Jj67GDtu1R6sw_ETVvnHAalMSTQBGCj1S1CewFQOrjPrjxIGFh3LmFCPDKngdyGxJ2UQNNvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/27654" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27653">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di83Yb9TSq-AGGLM2QwPUShd754UX4KOPzMFb_jmTS3diiBUWso8aYRu4_5e80bU_U_JngrPLjw0Gb6zBNvrVzAiPu1heywicQRbFbh0qjj81-__7LYpdCICBt_SuPgduvOlGzIY6SGLNoXo5oS5PdCV-VBSja98Qm39cWfmbCr-qy2c4QugGtjr5ekDjPjrCxt9H7GToZYx_moUN3HoLSvcI-XDO4IqFV5HKdCWpGOv6f467-3KeapWdFOR0axxSsQnBSJUH5P2bvPY-8cVeHgSSenlhv9QDr6r1yW3Vt6GKysheH3ILxULzmQXaJUHcjODt3CCGpgtYR2JX08zHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش ها رو فقط نبین؛ با تحلیل درست دنبال کن!
اینجا قبل‌از هر بازی، آمار و شرایط تیم‌ها رو بررسی می‌کنیم:
✅
تحلیل پیش‌بازی مسابقات مهم
✅
بررسی فرم، ترکیب و انگیزه تیم‌ها
✅
تحلیل زنده در جریان بازی
✅
گزینه‌های جذاب گل، کرنر، BTTS و آندر/اور
✅
پوشش لیگ‌های معتبر و بازی‌های ملی
بدون شلوغ‌کاری و وعده‌های الکی؛
فقط تحلیل کوتاه، منطقی و کاربردی برای فوتبال‌دوست‌های واقعی.
📌
برای ورود به کانال و دیدن تحلیل‌های امروز کلیک کن
👇
✅
https://t.me/+q-sIylsuFEtlNGI0</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27653" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27652">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxG6dj3beASdCYE7rpXFF5ZE_ew6ZQ7FXQM9cR-Jc95zy5b_TskkBAGFH06eqYOu2Aq5a2HcPZCKuFYZ1Ub9is4FZYc0xQmSVUXV2LjEqwhtbIZfSXXuqpFqdMcNvhsPbVAnW1R7qDWVT-bd_60BSeHd-fxjMo-IrpTwYlooXlEZYS8eGhjwvoBdIuCT8D6QLGtXJnrULjysM-UbnCPehmL_twDY8DZ_2iTPVNr9fz3-JWu0BceF5GQa7PkapnWQpuvk4jTBmT4OrgBrQGBqNO0EoPgWpUfOAXd1pmSfVrWqmxVD6XenclriYml1WHnErzd95AcBHhErvjtAmHIzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سزار لوئیز مرلو:منچسترسیتی‌پیشنهادی 120 میلیون یورویی به چلسی برای جذب انزو فرناندز ارائه کرده! انزو مارسکا اصرار زیادی داره که این بازیکن رو به هر قیمتی به خدمت بگیره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27652" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27651">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPrXwspJjOuSaBeuTA11bkU9hT6ZOJNE1qKJsZF8ke-alimKNexe7guloFERaJWwGeJFrR8QeV2wjM-FZBCktPAaq1LyOJ3AM_a5jpF5W754kbc5n2dzlZ9WkQOj1kAGKnA_XwXs3_ilYTtEU4mITv7Fu-SzXJAQ_PkA40qpElI6xfyh3i54OEpcB6SQMcILeZGUWMVKFStZ2EIWeCtXxdRq5J439I_RoUipyw5jaNqIjNiqM_7hJ0zjpGUaMaNA99r9quAhzfO7pVzg9elPZDJbbH39JHQQd2ORb5PiMtA0iVHvwTSK12EnENV0Lk7VmPmuJTQ158YvhdA4j6KKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27651" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27650">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8DzldtRrFIa8dgYtX8iVzEV2lGvncd_PQ_ofWAmj6yDhQHNflmABW4fLFfzGcRHluhyaYAK8ZoY7v2ZaE4nVlAPa9adbiKHL5xgpG2WmQLhtFIkS2B-hmZvVDzxhJAi2hpULR8KcbuQ4zzEk3KSoAs88M402FoHDoUQ22tws0L8B5dBa4TUJdEw29OdJWhIhsD5P9pvwvaWZ9gH8eKpIGAhWTiy-swVPWMjip0w8wREbM6bDdMki3z9Yc95aoZP-K9jzlkzMDzAqa3dNBXG8JjtOpiHkO1Tqg95Axv39lfJH2anADTMNGI9IT4DTArwYkHEjA8fKNsVNYZGABjicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرکت یوسف جامه به‌عنوان اسپانسر فصل جدید باشگاه پرسپولیس انتخاب شد. طبق توافقات انجام شده قرار شده این شرکت در سه مرحله 550 میلیاردتومان‌به‌حساب باشگاه‌پرسپولیس واریز کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27650" target="_blank">📅 17:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27649">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nci9eVcE7zX63PitpOqdPdVHrvgYSqqi4upB6npR5hFfHduQ6q1itbT9keSGukbT-T3eQAkKNqfI5YAYFaVGXHJmivCtbCJfp5d0UkJ7D5vJMnQVaKjqxMu13aFpkMYiVt6oVYzGrEEjTBr5O0ZK2oIHdMQf8STN_mms_zew0UUVm-qTB3nmn4dNl-wLQE9_oIl_E7lbW498Ti8MftJrFw_Zv3Sx6K-C6CJ0EO1kmP3Jkm-cY_Z5vqSSQ_Y_51NlYAPB6U6w8BjbCGLCEMN9d-ZOW-eF42O6Ns4G00bMoJKvwp4SnjlNsBF4G1an1yaBrWooOw9200F8D46g4yDytg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
دوست دختر هکتور فورت ستاره 19 ساله  باشگاه بارسلونا در ورزشگاه سانتیاگو برنابئو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27649" target="_blank">📅 17:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27648">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5X0WAualvu-as-1cmu6l1g3iAnv1doDHPoNFmrJSOO7vdqKHWnriyYMvITccV2VV6-rp7fYxNGeikYDQU2QWPNXuBTJyyPAlxgN3Jn1EzPoJkNvoFZseyTkkcw2UEkk12_roY-S6SlV8KrNgWkakE-ApvN6u53drFuM8CgwZFVaMuKfYeP68mzGsP1zJ4iFu7nhr1W7YyFxe6x7hgVpFXCgHAHdGgR00m1qwXLQxReJ31CgkwPgeVs8wNtsJ3fngvVredKDC_e6D3sWj4q6fsx72WPYTrN6QI_4Iu_U6OGoRIxEiyXgSEebiR3lxWs3XG1_i3LxeIS8UVgVDl3TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27648" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOL3GAfVRFU6jofPoH3SxfOacmoeN_G_HvsjrWZA1w7WNEV1W2U6JWdtAdoEdb0HUWvVdq5tYHyWJWXJ_43SLszqQ9EevpFX9m0qBD5rFi9VqYpM-Lx9_ugQ-N-b8wFOSdvHWbC0426VWOPAbcG36qZjKtkKF7mr5cB8RcjGfJwS1n_lKL8VnyHv4tPDNPahpvf7mtIC9cExf7CVoOOIYyFi2wQX-rtozW5MOw5m3jDFCrO_LG-GugRAnRvz4zahpNepGar709Mz1VW_a9NRC5EFOpBG4aymvZsFddb9SUA75CCF05mK_Lyo1ip2LOcb-Liu_DuBylQDQneO8Pbu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27647" target="_blank">📅 16:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItkbPw8FdaN8bJRCqe2Jc5YDNy3DlOJ2uEHWy0vZ_JRfp6eHXZzfhF8SyQlDFbT5jKj6yU-iSni9V9KsQx-6u0A0xfUyf4qAnw5-4uaLi9945wosHYGcQLFwAtaUFMT2Azxwgw-GsV4xCsKObP3NVgHvHOXJIPOm-ZXX51VjTqDJTS73WPYU49ifgxned-7guxyWtVog9mIUY9vpTKO5-KhDU6ek6OobG_Bs-L0S62zHzam_nSQrg3geuzACDdNU67jvuUriyzYNyO-z98IDO3A9qwwJvMftkfc3fBOQTbTlQRfUeQfIbcX47OXkLNj1TefGBvrmF6aoDYGra5a9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27646" target="_blank">📅 16:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHsOsCSLL_Nc4e7KT0YN54tRN4OoHEmnoau8GenEhVBxnUcURBdQmX-6WbDjGzaOIZQErvneqG6R6PfT-kl7PT-0ZjoaVvXHjrZE9RzoJGuaQvIWC5hxzJKRc0rD635yOIwt7pbk3Ez-OeACoiQJV6i7i6U5W734yzZfkmfr3T-PlltsZA2n0AwajYQPxgaqkRxcEfDRXusUjAcCkG2StTXQ5agdIk5xjD5_6sPfen3jiiqfl1utIFkxudN6aBnyS4JvpiiRKMPinZlGm7VOI6xW-CqnMzporPDJlvKyJgTBK9TLDpboeulccN8ny3PnpJTbdZxEuQfkI7ci9Xstig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27645" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27644">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOIzxUaF1K5g3XAz2CqUixx8qYxFTOvx6ms3gHyMomUJ3UIL59TZvoPiw9efWpJTgixPcETsHHoUSqpKiqKwAlj_j91tTtyBVypx82pJPGSD0VOvqsHvpFM-xC9CgtygFra2N0pDBHWYwwetWsUGnSZDOWdtN2GIvevPm2mdblruB0djYpxqCXpk-z1sTxG4diAkPyj8_N695WLEVkGc_MqkSfiDAGBNR7g1fNas2CycGXUmEzLLf2OTIj19pw9TcOgbm4Lmb3EHNC7f3u_gsvhjNIo0ez3Wb-nD3P-FkoWqVCqkI1gTvtCBfKviRmUD9vOESAGmuye725neAthCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود رضا بابایی ملقب به "بچه" با لابی‌هایی که داشت نذاشت باشگاه‌های ذوب آهن، مس، پیکان و صنعت‌نفت با نکونام قرارداد ببندند اما نمیدونست که زنوزی و حجت کریمی به یه ورشون هم حسابش نمیکنند و تو جلسه یه ساعته با جواد نکونام بستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27644" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27643">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUh9VhvlBRj6cg0yD5VuM5e1Ws8Ua4zNM7gjqWhE2IURyKsXSMiLBRkxoFvtwokBnnMNcLeqx9geMBuTjnFUEb3dxSTOmE9GQkLaPJO1d5gR_Orj_GaLUq_L872ZTD0VGsMPPxHujAZPYO65-G_fRWTKQ76gQ7ijJ7-eR_HvKIjvz8OukuYyhWHr32blU6ti5N0nMWAFksOj13u8GRSDIbw_4NQl8vZ7UPbmDP5YaQBUcQViuJeTnLY1z9ivTtrY8IoE4Y6RNTbBQkJ9AaTG2uVIcWndJDf81VRH4Rbi1zfX4wmaKeJmRn35uxtHS0en6UorqTbgCQZsF5osvJ4rZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27643" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27642">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDPbviQXoZA9V_lcrEgjP3eAm5VbkQQ-iJFe2u2691M8-0DksQ01RRdeZWEHDB3KivW2xG2Zrx5ifCWeJ15raLut2C0iCmnoIVnPIb38KdDRLC3UWFpVGDHR3k0bpDTU3792kO-3rfI-RcLs40Xllmdau5yYC9r_iqBySY9smbJ7Cz233Dhw0nSv31G9q0LTLIj6-LmWvAuaSpCflY-yWq2qT3lttGqtvZ1MEYXGzq7HckCswIQ9VEvH-Cxsc8n0d4x0jtt0_lMA2IURnPmk8rd3U42p-ufXU3ichZGXIhNfyuWgykdq3laxzSeJLNJts06ViNBczbgvmdktD97bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
لیگ حرفه ای عربستان
🗡️
الدرعیه
🆚
الاهلی
🇸🇦
🗓
پنج ‌شنبه ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27642" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27641">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnFPPNxV8OGGfrZ1HgMALmRd_wkBDPXlyHoXhJ0a74IgaUhNH8olUH3HBkDWVV1ayztNSaM4bSrvufAEAXG3pDYWDRX6XVvuOYYsua20HjMBQnpMQzPe8ErhI2yjOQvNP3-m7lsNBM44TUmC-0do7PHHEws0ho01LfbRqhpWOvCHUdXOfMaHcdCQ4BQyxflw_nncMHQH6ccZ-RPyqngc4PCvQBO5J3z8zzjnoOKui65pvcDDY7BSbS--4eVrLUq7BLAJeCuZ8-aQTH6YoNoQvqNls1VNos0aHsIaE2aPOTvuTY0-L8MhK33SD1DcNY2JIRwNWyNq2dIuLFmUEQ-3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد وینیسیوس‌جونیور، عثمان‌دمبله، رافینیا دیاز و کواراتسخلیا در بهترین فصل فوتبالیشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27641" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kygKyc_wjw9-uhMFLtJ9jIVJV-u2FlZ50uxDHrwMvUruZzmx3MK2gSzr7K9t7teMhs6uFy1CTFVlo5j5gGynbFJkY59UUNQX0t8DPk8_3R72gvOGExtWtOZcmpB3_BYt_j1U0s13w_69c7jMmGTARBvQwMzFJ6qOXIthakERd-QO7Rq76HZYee-J5Ll2RjLr_01rLMcNcjGChzzjtZbGNUtsBiOpFkWjEJQ7Gv_OaW80dgrHPODZuaAJi2H4f0rMG66XgDvf22C5W8AcyZwcdCJVb-lMO3JlD1P0I7i7WOvsxoOE4u6VmDHSAgKfqPrSPsvgHOKv1GVmtMMInhXbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ طبق اطلاعات به‌ دست آمده؛ باشگاه تراکتور در روزهای اخیر تلاش‌زیادی‌کرد تا محمد محبی ستاره تیم ملی ایران که بازیکن آزاد است رو به خدمت بگیره و از مدیربرنامه‌های‌او که رابطه اش با زنوزی خوب شده آفرمالی بسیار بالایی رو به او داد که…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27640" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTH2yDTSL4cx1ar_AYUl8YYdjiwJC8iKJn7Xn8YjpVEaoNmKwrYyq1bTPaXOvlFoLAknTuBKqn0pqDQ8IsqfsEplhjHwoukBCB0_rBs50NqAlKhSRuc5P8_PsktVBoI3IPK2EII8GT0lAotgGo1qI7AwmYwj7MoKuM_hkS1BKutYMy9hB6AMsaqC8x6pg4UKxwtxh7M_nHMvZJpS0k_2eANTjuTh52mEpSO5rNXli_sz0yzwobnx_5icBBNvUzO12txbmsmlb_HkTIXTT4UVi8R0e7YBqRslRPKK-Vk-QHvh8l8YglA0yd8bSMZwx-aPM5P2YDpFrM7DlFSMrCWWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27639" target="_blank">📅 14:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxPI1amraCwr_eNKvQNzq-47I6P7Awa5xbT7V8A27xQ8ZJaDV6wDGSkxs9C225TMlLM7E_J6iY8w3xdX0DAKee9M816YoYvIMrY-igM8LZhUSdP9bdhKuC3fsnphzB4NZOIdHU2N3cONgTQ1qAcZ1ZXy81PVfBWZto3-p88pcRCt2vqgENfaeuh9PW4CSYJlwvHuUgLn9Ow8hAnpx67EYNutHUD76i8QmQB3lpdR6O7iudovLD8JRrRIMoBKudDMh_AB0lE_FnroDI6UVwyE8Z1PieTv5ua7NhSEoujTH2WSS7qPBI2QITxwKd48cfVA1AxzXXPFUQQij8aK5BGk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27638" target="_blank">📅 13:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmiAdwAqO1eAluUX9Flw7RuIPbPJBsvtgVS-78WxZXEX1Pva3YaxauqVzu2unLFyL8t0yeA5K5PrLVD2X3AOZYdKKpa4_pmtZL1Tso3Q9mkd5CJpfhXhTgki2UXZUPNkAYvRQvFDBvbIO0Z6zhDdSOwsUZ-O4eLt4u0bzeSpM68CUkXfTpBZ0jsgUoUuemSUG_R0Q_VOKOfbK1R-mOr2nO266Rgwg0r7QIn2rHaDsrtkoYQfYQhQCH2pqrd8icWapmoJATSHDx4i9RJV2qjHuKQDDqhiu4kyOKBLez1wGtrZ4z7G9yO2Sjr0DizritN3IvefywBTYm5hY8_m5wUc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27637" target="_blank">📅 13:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBbynJz3Zxsr8ASW17E6iRf7bJQYTnEKuXVGGJlbRSA0_BUU5MXKVS17Q4c_a3aIzi3NZelDuzyZfzJm0l7udGg0gXzN83s3MTGGcT-mnTVwS9yTe6sF8pE_96ZbuaoqV7DI0XSZ_ODCZYE3RHm3yIGI-QZJ4tzOVmwAJBvCBoyn-aa9HArw2aWA_hpZ2TiL1LXqifGUp2TOJCvEiz7gukBLidFJOpS-fuDlGvok06R0Sd2rRORRiCNeFDJV0anGH5FgZJ7QlbRwFwn6YvdInOyGbkOpRjge64WjKqiGe0g7JluPuVzOl8-leDhI2HB_gMSefR6J1gYPKVrY3YQ-BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درحالی باشگاه استقلال تمام کارهای اداری مربوط‌به‌اومدن خواکین گیل به ایران رو انجام داده بود و حتی برای ایشون بلیط تهیه کرده بود شب گذشته‌ناگهان به باشگاه پیغام میده و میگه تا زمانیکه آرامش کامل درمنطقه‌شکل‌نگیره به ایران نمیاد. بدین ترتیب حضور…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27636" target="_blank">📅 13:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428e46d461.mp4?token=rAUKMLFfNKYr9zYen2N6lFRPXg3V08gUgw-rTPrpT9HkHIPSOxCMs2RLHKtf2fYXaIpa7vJWSIkOEWIeOgFD_n8LY2iBYaEREj966XLhCkIBi3UBNdb-T98KTBigdj-yZjMj8ngv8mO1GaAZdGzPUjGfsDuS86-ESPMAjBYuLLRGBMw5QkWoRj6zitfJc_sgh-Uy_T4ls8ryDQZNVx3ZAPgpmoR8EGHVY98VjffmjQomR3LZbAfiy2qGxSqAIB9LYNM_Wnk0vbRcUS3u841NiK7k8f_DJ_KQ-LPsJiMTveaMoZ7UNMZG1R2erkV1Dq_1Q-JSeKTinUIFj4uAld6XVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428e46d461.mp4?token=rAUKMLFfNKYr9zYen2N6lFRPXg3V08gUgw-rTPrpT9HkHIPSOxCMs2RLHKtf2fYXaIpa7vJWSIkOEWIeOgFD_n8LY2iBYaEREj966XLhCkIBi3UBNdb-T98KTBigdj-yZjMj8ngv8mO1GaAZdGzPUjGfsDuS86-ESPMAjBYuLLRGBMw5QkWoRj6zitfJc_sgh-Uy_T4ls8ryDQZNVx3ZAPgpmoR8EGHVY98VjffmjQomR3LZbAfiy2qGxSqAIB9LYNM_Wnk0vbRcUS3u841NiK7k8f_DJ_KQ-LPsJiMTveaMoZ7UNMZG1R2erkV1Dq_1Q-JSeKTinUIFj4uAld6XVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27634" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27633">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9rSX26HxQZBkOTzWEjHk-SsgivZoTOCVw07ObpZrYoivwFFTpFh69WcYppMP3DTkMDQlEY8gieOmmNm4hMdCiZdGhDY30kz0UsEYuI2aStqFy7GgQ1Ad_EN5w73P-F5oXhkc3YilU6Dd2yXIuZBfBJS_fMlQJJmLjc1zVI-sdm6OTA0e_JyoSRVe1JY0sLf8ejaS5dDJPxmC3k4ExUl1rZwXD8RAZWhKtiDdvyTR2ktViteG9wnnrvR3BEQwVlzQOYdF7_IWlnhFVw8HS_GeDI4iH2Q-0qrhiAH8V1_G9dC6TPIwxnNAWtmIww5Xx5BSA4FCYk1lWEI9zxGnkR_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی‌از کیت‌اول تراکتور در فصل جدید رقابت های لیگ برتر ایران به سبک باشگاه‌های اروپایی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27633" target="_blank">📅 12:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2kmlNc0h1WAqhsyP7M7tsdvN2kj91mFhh4rcLCzlfWlstvsesdwIB8RYuuR4jgkOgldhqXrXQ0qnmiRUv1pPdNU4ymfFudA4PnrtFxODaahXytoq6Zz_yq2JhbtZEaHE7VvYBC_elTPhi6Xmu_D2G7JuFOS8uxjI7IoknYj9kdJfmbkhsFBxhDLjkDtmcblxtk9_pltqsjbHBLthSltGNSzx5Ywe92LK9Ml4eBtMgf7XUoMsxpdZFM766mizry0HbuPCfT39GILGiAP5pnq0TTwPIzbTMQZnAp7r9yKY3SXHMh3B41sLs2D0gi3PgbGJwXL7rxk7MocSAYFLd89zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27632" target="_blank">📅 12:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdD17D9s8aUjIp7SI0yZBn3-pL1-NFXkNuOJZ8lordBUsLJcxMw8sR97DP-qIwuxkjqLswXnV6A2NnTMvffmjz2fru4UvThrN0QozMq3hQM7JW1IR_Zkm-PJ-KUdpHQoLcnbPEkCtUm8yjmuRcwDzMbzttaIxJ2H9K9Isq1fxF9K6fcUVggflK8ikRtbKlyX77MwpYJtNZdVG35lB2BwtgicJbQWbYKTkNH1QBCX49f4kj7y0FNguM_4htnk5t-H3a9Tldu9O8_8cfERMZrfyO2bxCJUZYlbNmPQlIh40pScLLyuQ1GT2ZGnk_tn2QKbcEhjo-_DBO3-ElgeykuWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27631" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNoxsJmN7bquMm9FVVtWSo6F0-dYB6wJD2cMrHT3QWSwR7_6obNJZ54IGo4yMAbSES3MVxU1GhQ8SwVifphG_-BHkl6M42ubm_W_-wmw5gB6U7ZI-GYMMSwwV2AmAKBXTphaQ2Evf7cg_Vm7z620vDAY1nx9mL3kX1UOgARnueZm8GwY3Q1OrBnM_EPE0WJlHfiTnFKzmslBp6qNDBN6dbTTWG2fC3Q7XA0B3kWpnr7vHQOhSwBjyMPYHbrBa_YJaeIKw8I-M7KakY1BEN-PQY6vrdmfOkI5C4NZ4dRqxpoPXY6WEGSEwqG47rjz2ofZD6V1ASlwUZjc2Q8ZgaRi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27630" target="_blank">📅 11:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qD3dewM5ryQyD3norViDn7Po9EhUxEbzoBH-6LRihTeCOqBVe1nMuMiaPmvKgvN2pPL4f_VTvDtoWrFEQXYuKl_BVh4dLdM6DXxiCtyj-ufgYGv2mL61Sm_ayfZJaoHptnivW_xl2A2x5mhBx7lXl0HKsusR0qyIiUDg84Lrpxzh0QP7PsfB1cRrj9n2FardBT3CW1AXa27SoUqIAAxZ4NLk3OLEnWGHPk99Or7JpU4t-C7gQk1lrBy3lXwovBnGcEXxDqZJOwmEv0aevLiP0nTvtmtemypnW-0zBgI4Py21O9QMIcIcppX9hWBfuUY4zmTdHjqipTfUEoukYg3Pvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27629" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zd2-5N-_zUInyPdiVzqXVfzoK6EaYVFaqEcIhvNFCfaMW-2_pxy-eiCBMnOaiBsFVpNpjxlKCpGEO8y8Kw_q9jBuDvFwFpQLpLspzimr1S8jQjijuEoslHWknN5jnn2rxqBXNCWUfpEobOQlgJsrzYnhsmV0no32SMBU43bt3O6sK7wpCQgdBEBqF4Z996aBiouWWNzU5ryHkLUf9jJtR_W2Xdnd2hnMatDtEax5y1m_kTwsGJmR524OwCzZq6Gji_5sAmpLo9UqeHp1M8X5e8NjplDNdX53WxPXD27kfPADh3o8iCf_GwSfFWlbBsoifYmCpBo57_0eyyAxJWaBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوپا آمریکا هر چهار سال یکبار
شد
؛ با اعلام کونمبول، جام ملتهای آمریکای جنوبی به روال قبلی خود بازگشته و به جای هر 2 سال، هر 4 سال یکبار برگزار خواهد شد؛ دوره بعدی سال 2028
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27628" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27627">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxx7hVZwMLFGJSnNcbKVhZiNZc7_5dlxW3pjIXJcxXD9XBuaPrylJh9Ma37DQxQ8g8o4_65InDdDzNhfkWP5WMww9dzbKOnhm8xQYOXjRaWd3N57-O2HB1Htp5vsyux-2YGGAGvV8picXz1BJmbfBWzFqx1ogL15_HisESlQvN8SR--A5JEVLBkVnCOwlGkyTS7XJ0JiZFARi1TsqVKWkBu6SACn6kHqSvAXG43NqFGfk_owxjLZmDq5Z0XoeLkRLJ2krFYq-wTYfYzINdFFVF2_BcpR046QlIaHPZfgwYp8QSjPi0NKC5ty5mWt8__GOnWKLBgDSzqHMyd3EDoorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر دروینرو شارژشو
🎁
به ازای 3  واریز اول در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن وینرو
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr22
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27627" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27626">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE2ekcm6VsTFzuKA1zoq2za2dFZKRmxTrw4anjyUmbcdxKDOfeAVBSJpbhf1lqOCZCfliTZWOhRTQxWDpol6dkqii6mAshVYgAORLVZV7R7IIqOh17q-6KnRjbudeuK2RdrVoNXNZ9DY9DleEWUnckb1RVrfY_lvMs2P78qoxOWIwk2viz7PPdzaoIwTVmsh92kiWanuMZbS6nb37VMMZVwPmtDGxUj8MNA-nXD_eT3lvxgfxOC4k7DFVRWVnE1Qf85KHHinnDUTMRwt7sGeXALP57XwBd2YDMgOlgjoZMPwuxRLKAMaSxxqSj9AsocSswbKkBrmRgS3RA9iUyd4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای‌اخیر گفتیم؛ دنیل گرا در لیست مازاد مهدی تارتار قرار گرفته و مدیریت باشگاه پرسپولیس در تلاشه ظرف 48 ساعت آینده توافقی با پرداخت مبلغی با این بازیکن فسخ کنه. توجه داشته باشید اگه رضاییان تا قبل از فسخ گرا با تیمی نبندد احتمال بازگشت او به…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27626" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27625">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIXuLuWc0IzOSIJVPRAFMT67QjqjIF-f5WcaJXu99HQudZnEb3o6MvmTrxsRqi4WZHNbt6ViCLg6tkSDdVWLowWr9TJsTH3Gtc-v2v2cnMUxmKKUn3Y2--vSbeuOTO22kmLjPepK9rSDBpdXRKSjpx1ilr2ebBSJfCGpjQmeLgpx8QA1yRM5skARHj-WDmQ3wX7ApYT9hu8xQR_bjPn_ykbG_tPsa9Ina_7oOmvC2fJYtQiVOujUHdXR4IIAjRl9FOSmztIHyp1i12DIeBIrsJJ12K_bfaYp8kCjvS7aZJ7wa1WXcNOaErYm7thYmTi6vX9W4NjRDaLzDD1z108B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27625" target="_blank">📅 10:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27624" target="_blank">📅 10:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=M8NNDm2y69RdHipBwqMupMdDh-FO2TjFueQyxAnn4luJE5_am9e8suSGF0JfUxdDkwNCPCDww4PsnW9aGbkkUYIGgYb6zIgRjaIxbq-hHAUzDrs-dZBOOIe_HRXdzVNUbVmlcKcMAm4ouZhzVns54s_iRVrqDVYO3D4HLTFzp0_Abs4QrohlgIl780465LUCrj-Nspvbj7vjvhvGq0pxEblWWsKRdzunvOVQ1qicupVvPtqxF4j7Rs5kXFv02jGbg5xej8SuE4wTCRqq1fTi2HdB7xrP8LPFjNsTQbdt__2piTwl4NucrjzlMFY-duMR6GRq-AKgJfda1FC7_3f7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=M8NNDm2y69RdHipBwqMupMdDh-FO2TjFueQyxAnn4luJE5_am9e8suSGF0JfUxdDkwNCPCDww4PsnW9aGbkkUYIGgYb6zIgRjaIxbq-hHAUzDrs-dZBOOIe_HRXdzVNUbVmlcKcMAm4ouZhzVns54s_iRVrqDVYO3D4HLTFzp0_Abs4QrohlgIl780465LUCrj-Nspvbj7vjvhvGq0pxEblWWsKRdzunvOVQ1qicupVvPtqxF4j7Rs5kXFv02jGbg5xej8SuE4wTCRqq1fTi2HdB7xrP8LPFjNsTQbdt__2piTwl4NucrjzlMFY-duMR6GRq-AKgJfda1FC7_3f7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پیام لیونل مسی به مناسبت درگذشت پدرش: بابای عزیزم راستش باورم‌ نمیشه که دیگه پیشمون نیستی. درواقع من‌نمیخوام باور کنم که تو رو دیگه ندارم. لطفا از اون بالاها مراقب خودم و خانواده‌ام باش. مراقب نوه‌هات باش که راه پدرشون رو برند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27623" target="_blank">📅 10:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=RtjldEr-vGRx5YCZTcmaiQJ1LxE-hBGz2RJatpbmy4OOuE3hQcecAfpPdR61vnZdL9H7GKJcy5TePJK_K7wIfUx64-9Wqk9JsoS-mFc0-SnI8-qPWxESsDThvVaxDU2gS4d3cl4FQCbmLDFP-OBDhcgVxLqYvpMJgmJDy4AJgV4Ca0pivITRojZkKSvC5J7k46tmw25g9V5e25lime6aMWuoecYDKww4-63y63yPAsSIJdj4TCV6ISNIAYozzuQn_huLBR6MuBvtd38vH7CHoer6nHR09hM3S5bVuWZCLK_a_O5iW7fkrCv9YdCia784TyTss4t_JKusIo_yxga50g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=RtjldEr-vGRx5YCZTcmaiQJ1LxE-hBGz2RJatpbmy4OOuE3hQcecAfpPdR61vnZdL9H7GKJcy5TePJK_K7wIfUx64-9Wqk9JsoS-mFc0-SnI8-qPWxESsDThvVaxDU2gS4d3cl4FQCbmLDFP-OBDhcgVxLqYvpMJgmJDy4AJgV4Ca0pivITRojZkKSvC5J7k46tmw25g9V5e25lime6aMWuoecYDKww4-63y63yPAsSIJdj4TCV6ISNIAYozzuQn_huLBR6MuBvtd38vH7CHoer6nHR09hM3S5bVuWZCLK_a_O5iW7fkrCv9YdCia784TyTss4t_JKusIo_yxga50g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
#تقویم
؛ 9 سال پیش در چنین روزی؛
در سوپرجام‌اسپانیا، کریس رونالدو بعنوان یار تعویضی برای رئال‌مادرید به‌زمین اومد و این کل استثنایی رو به بارسا زد و زمینه ساز قهرمانی کهگشانی‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27622" target="_blank">📅 09:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf7bR-q6KBfe7stGPm5bbKEAYrcwyvQHGjehBlCW7SsZCTEfPEgB5vpG7NCXrcKTm6_6TVCBiDACJz-lpEZ8MDsaB-Ue0__pQy5g3_oE24fYLvr-LPMRx1bATS5iv8_5s4nxKr8Gtl9ZSVb_9-LvkwyUcG7FZW-llKxCu-TesDA2yVgmx6hMnWRRG92dvCF8v3Xk5fvp22yyjHlT8UzhcuZAaEWsHrgpldTKsfYzkTu1T6IrITA-ovpQo2J6jgnbEjDhKimdYS2Mt8tiz9KNtzOZTu_MMlAOL2nzJW3TGEf8tSpQORMW_f2UrYSvH5T5rRLkk9XZ5dVYlmDE1Iwlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیرو خبر شب گذشته پرشیانا؛ امروز صبح مدیریت‌ باشگاه‌استقلال 50 هزار دلار به آلمدین زیلیکیچ بوسنیایی روپرداخت کرد و پرونده‌او قبل از شکایت در فیفا بسته شد. مورد بعدیم طلب 25 هزار دلاری جوئل کوجو هست که‌طبق‌گفته مدیریت آبی‌ها فردا پرداخت‌میشه. باساپینتو،…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27621" target="_blank">📅 02:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6NPxgbZBOWgjzm43qg63zms70D4XflF9rgYLyctHY5yCbAjtmmds0W3s6_s1vFTB3Eli6xpwkWbW6R2RRxmrdUmUsb68KUOkVwkns72CsN14D258LxGT7Kkmqfm4dPPFK5fD488doU1DfD0qcwyuUwO4iGOFmYdJRoVj58QrgJXqJgkQ6RiTb7O0ByPHTHZiEMRIZ3Ibk5FIc2yKw6omvOKjQNzPhfE5CviUB2Cym-dZxDFv9TQosuJv4wIu8gCE_3RrIu1fpcRKURFTP4_O-2bkYsqES6lRw_vnN5EfOTwETw8Ky7UUuH6vfJSPmN76h6zWzUbeFu34Ti4FSIgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/27619" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuqiQ7kMg3EyRrRxn1oQcV9e2hJPkTE_ccLan95vk_nwgedduAkNkGjHmTCubuOcRYw92IQiC4bxQ3_khofAtHxdlGSzepAvMkTLL0e5NbkNF9FylwLYnylj-ssFsaQBVo3lWLqv1CwYt-cxriflM27GZ4ANrk_syoqoHwRAQ8JFgp5XE9d8TTT1Yx4fxFtVW3IJ7fX711jP2Fy1mvSt-yhyf3uPPt0ePnArakrPovdDH893u69XDYFseCzd5YWorMwtg6bwJbhmlkZANXJPHRuinpxq3h_Y7dnhN0WEkfTOy01DHIdDz0WhHsOXaj8zgnwQ5DniZnSNoeCzNNfMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
هواداران‌پرسپولیس‌وتراکتور در زیر پست‌های این دو باشگاه اینستاگرام بشدت فشار اورده‌اند که محمد قربانی فوق ستاره 25 ساله الوحده رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/27618" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSibVVRnx7PT9JuJS5-uOGl4_wf27Rcv3UBdyqDy7APz6ojcoBj8SYfnTUa9vSPaBcls85IckdsrhVxynKIAtBzjUlfGUpmRjfoR6IZ8ASOwdmLflNmkAhZGsOUWxxSLpMCH0ZtKiJheQEBrunkUATYcpYraKByr2YtR7nFcKpvr2XtVaa7C5GlkEcL-m7E8Y7S19_qg3of8hngGlefPQ4KMhh66iQ4JYmtWIDz4zADBLUBGkEhjYuEvl7WS9krPKVOnaujsE8itDlCGm6HPz5Y2sNUsDkLj-RyUkITu_bf7JmK7WCFKy9CMM_v9r3FhSFZKzAODWd-Anu2wwvgTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌بازی‌های‌امروز؛
ازبازی‌اینترمیامی در غیاب مسی تا بازی برگشت پلی‌اف لیگ اروپا برای اللهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27617" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMo0d8g-kiSzJ_eVdTIodvBBhGnxLa9uW4hasl0y-DyG4_dacpLxxBGqhSOn5c_BC6LpFmfHFONQZQVQDZbpX_Pj9tki472JqIduIDYs1nlNgkcr9kikXEolgFqNVm3-WoxvUb79VQR7bCMOR-kWEfOOojU6JdcFNAdQFmJS5CnwPGEk-pruTGQfbDKHBLhdoqxhFEZrJ_sSPvDydsnGCqgy6zzzf7QjXfxahnBeqXNL3yDhdAG8XtVQmO2xmWFbA6SnbtdzFp8PSqSeZlMZ9DAAsnsYtvMaMBINnVDgUzr0EujOrrGVvA4l-kB79f_Nt_Tehs6Ija-TJ7W9zdI7Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
‌دومین‌قهرمانی پیاپی یاران انریکه در سوپرکاپ اروپا و برد رئال با پاس‌گل لونین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27616" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULh-Plug_ZpeycyAJWarciSzIiou8lhrMf4sy3qZlKoM_v1Lpj-4ME3suzPtDBam6AcDE2xAKJsBkesddPSjzLAdFi28foxzUiqJvl29WmDrieD1A5oG4mCL3MSZyiPeLOV5D-D5-wuZs5OFKpCpxCgJDZxF5SQSpPX0_VZH3HgHk4N5F2ls75x5LnDa178r3vt30J7G28hSSattwfUEH--47FFNDoIlBRg1pE3d9pftDA561_oond1MrVE2v3Xbk5BnL9IKL_ZQylVKA0SNlSep3vvzEIgwwBW8_g8B1d5J4WZL8T6-fw3aU735vJw6K__iV5Ld9tDwO6Qxds6nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27614" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpkZ_X4JRD7uCx54M5kSm_yhSnT6PMMFj22TgQLVCDBP44nEYCzGlPLpo_BRiFxmP85GJU7I0ihtTr5rcj-ch93iba37x8iFH9AU0at4XkcgiywfANudf3zCpDe8KPT1CGPyPPNTeLLT1LrFTeJzmyxUimoIpmh8Q-0n5IlAUnYZH9srOiDsh8uA6MSqJxi8xUQdj0ERnP8QAeY8MQIIiEFMsHWxvgdRv0DFapWlqayL_E5Z57Svnl2wCFQC-ygKUWcWXz6W8nQBw3gvpxps9-DXICnajGBPiVPkhi9rstvPxktsH1WRm05fydIo9ArUpth10aghyQXiphdmIFxMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شاگردان لوئیز انریکه امشب با برتری دو بر یک مقابل آستون ویلا قهرمان سوپرکاپ اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27613" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5nnL7ZkhX_Tvu8cOoScrkBNwbF6cdtFltV8HYjDX4u7MLg4lXokPSkPbC62Tt1mo6DVWUSThq98h8iOIPMlN1w18JxLeNSd7fGOguWi4XOe16SpPASGr8Lu8mPIPrL8Oi6GxFpzZFftyaD_phXW1NNUN2Dp9JcZ8CyOFYmvj8pq-GC0YKcGxt5US5ytIGvY6K2cKI0nxMs7DiWxCHMSaWa3vL9YoPQnQ-D0udQgQQ1Cmb6sqUH42s9KHvAZmHet0LDx7PbTpvLF8dljLjVUxVDE7TirjIBev_0lPf2iiT47oG1zDRLYIeggNi7PvHNFhfdv5T7FHsrEV2E50ZUwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27612" target="_blank">📅 00:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27611">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx75CSmZyU9boxEphmZhXAcqzI1vwZsbK_XHRy-4rXVmQihbef-_SkBOpq1qlFjAFI6LR_-lNHn8egVT-wMr1NkVg_xttstfmRu96gkF_m8AGLlzDCOC4l6OQGO2PoGBDuOqNekIPIGWXygnLQdAKAmpCxsnt5q_pM7aLLq9xMFJlzidNezfHpUYnUsYaks7M-Pzal8fMWTFMagRk0L3GiZVIjbfPEKH_yPX3RpAJcdLNuWzXEofp32yeMbvP4rBz3n1DcpinLUCGv5IFXil5fg2Vc8kk8VxM2qWsrZr2u65b26V9A12kPPIY4pnnYzjCc4FEg6TmE7CLy-V0LcUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27611" target="_blank">📅 00:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27610">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgUgz8GJoRNJbcNwH2wpUekU3r1MeN2oghI0_wrvdhBBWw0mU51-W8mIOagCOTtDwQgq3Luo4Kx_Mpow8E8cYf0AZvGDFoTlnsyB7G-1M2fu5M5uuo6n_Ob2afQHv_jhaM_6CjqPDz4x0G_Tvjy8vNajUf9lOoD1_9FkicvklhZxUnqA7tQXiieX54j6ZYOXdOYI2kxyoju_UgQcjF5SRTEvrSzBBJYLqSQGSfGqf4tp0-3bVjnvgjXjSMW5Cv4tHNVRC0NtN4B256V_c2q4FsVTxiD_cpMEyq8yYXzIhtn86xwYJm232pFbKzwC9pBmSF6oxirbCbRsO-26Eu-rqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با اعلام باشگاه پرسپولیس؛ کارت بازی تموم بازیکنان این تیم از سوی سازمان لیگ صادر شدند و سرخ‌ها با تموم نفرات به مصاف شمس آذر میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27610" target="_blank">📅 00:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27609">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmbEcKLQWji5RVEv3ovMD-ybVauWrswttBzzXy-sGx0xVSdufWuMYsXj5LyllheV70K-2r0U9ZQatDlvdOAWUr1VUldrnkJKrNQk1j401D7bHdMXPur3IGl1It-ynAOOUEbZFPBn6mtye3l7hObY98tZkQUfI0YGrZjUAsKXIkdPeDZq_ud1BY82b71hEF7e1J08qA0QF6kTkB2FCzsSMUHyKtHL92-eE1eIkhHzIlnKmV5VI0pD9_ctQRawnBe1ufC5ylZszvkyYTWFP010r77KDpi_Ile2D9o0R5s2fVLDWOhUiY3cztDn6_o2-9JIyzx3k7dL4TMeadwYMkPl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو اسطوره پرتغالی تاریخ:
🔴
اگه من جای امباپه بودم، می‌ رفتم و ویدئو های کریستیانو رونالدویِ مهاجم رو نگاه میکردم، میدیدم چیکارمیکنه و همون‌کارهارو انجام میدادم، کریس رو الگو قرارمیدادم و سعی میکردم چیزی مشابه به اون در پست مهاجم نوک ارائه بدم تا بی نقص باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27609" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27608">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEas_qwrapiq7JyH9XQOCMwLBDq6JbSmkdHNNh1rVkNNY0zSpgfa51vb0PrOLB8EbVyJg5SmPEXk1STNGuSaXLfA83hnrkWOZp_RW-Mb61j_TAkWVKrlQuq6VLgOoU4L6VUI84r9eH2bTpoSoNJN_MbJtqF6tArePQlc0QcwL2O1ce00ZrSHEvV2bNJ_3CoKlui0BWbxxKVg1S7N699oLxSU2ygHB4jEOYGO0qZzzjSS43UGfSizu0aFdwWTtP7SpydDWhtNNo5v_RRXa1CcXYUo_lPO07zvofOlhlt7VEHPEt51PdrpkpVB0GntLospNt61aQvgNngb6xgzjcU8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه شروع فصل جدید؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27608" target="_blank">📅 23:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgmD-zTqTcOPXLPF35-h4zYRbZWxbdta_Gp6BrOrfB6Hgon1Y0ESX6JcO1YasZposADMMoSMkcsnxAOlwD8SnT0pFriKeUdCDh7v8m46udWW-mnVPr0glsaGkmIOqj_WCj75TW_R6FJnMMUPeZeyRlQMTTKMvbTxFLxDe-GA4KNvbcAW3xVfvfi0OOZBm-hqiAwH-qh0CzmT5OFB4m8OQo6h-GTCWqWB2fSP6ak-W8PirbbQmd0z_8sXoTVS75dYPcrs-l4RQRnZYa9Japz2gdtGbzqR3HccK1VHNEMQQTwFva26A95aNYcMBhwKiAsQE3BpafGH1wVXRbkD2CV_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Epp71Q4pqdcondHQe8lwS1J0bsvi8ZCAeyTqPFqnxqucIf9Euj7b6OKZ0IM3Dlv6-FLZD-njKwOOydQuQiY5RwrAu9iXVcYG_RRpC5gbZthOwLkyOxEUXCHFMlZDZSivyJqtWbNn3XUhhND2q5OBi1jCeeo5O8EZDHi1K7qFvgzqBbJ-BEXdoAlB0fX10CYctsrbe2T1th904X5MOK2NG3OOyeCQu_ovv_n2fdG3Tb_ZzYjltD58GMcl5M1131K5rC-tDpHrwjWxMX1a4fnXNitWim5eKCwYM5c7-C3tJGg5lhLJCU8ZlX1VFkP-qH1cXqSchFle1oJRWgKi4guaEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به بهانه شروع فصل جدید
؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27606" target="_blank">📅 23:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfiJY1-NJW6WJoC6CibFAysFu82CAY3zte0ZCYFxd_9TZyjc7Ngm5FjYJOUhv3gW6HEtagAXIKUzQdf8ouiNhUfTIDaIlsizdnB98k95whCA_X4IvV4hnwmwOio6Ku-iBc6Zj-HQ0l2e_qWulYY_Ujii453GGPzynpnxakrfDNAtf5HhxmNGuot7sdh1aXkCmBNH5TeKOA1BQQSc1493LSMdaG-QJ-ISXB8feTw8tdy6DWgoZZtRnbY21gIDALXLevOBVBCrF2_FYK4dQfUay9SGpGXGjk1yvO2BkN6DmJhdq9zg7bB9PAUoHtEWDlSjmFfcGl-WMIX6jZqT89_2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛ برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27605" target="_blank">📅 23:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=TmaknbGZUaRCJBb1yrfz3RXjAEULlKKVD6A_-YR7R5gJYcWNmYJylXPY9TY74FUayQfO8o0nYx448Kc56dHy1fpGQ3luMietiHXJIx43qpkYUjNQdI_hjK-xuPRvu3z_r0QO3vwd-F9_psZ4iWfOCaxqQTt4yiA2e2yfxLq3DdXusj_F2yKOvY9-nSgjxhKaMBN4uv0ve0QI7E6RLTj3G7lekBJtt6uM7PSxc3aOCUKxOszuinjlRq4RAZKFuahlpjZYCa_pNODYBzeW2wqqbOnyohxrYAiW0GhHohTOMcexhz-6cXN94K85SPR2zuamOScvmwpVRUNngq-zEAKQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=TmaknbGZUaRCJBb1yrfz3RXjAEULlKKVD6A_-YR7R5gJYcWNmYJylXPY9TY74FUayQfO8o0nYx448Kc56dHy1fpGQ3luMietiHXJIx43qpkYUjNQdI_hjK-xuPRvu3z_r0QO3vwd-F9_psZ4iWfOCaxqQTt4yiA2e2yfxLq3DdXusj_F2yKOvY9-nSgjxhKaMBN4uv0ve0QI7E6RLTj3G7lekBJtt6uM7PSxc3aOCUKxOszuinjlRq4RAZKFuahlpjZYCa_pNODYBzeW2wqqbOnyohxrYAiW0GhHohTOMcexhz-6cXN94K85SPR2zuamOScvmwpVRUNngq-zEAKQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27604" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQM29IfsfWZ7ABKV9n2WyVHIgC2yBk3Vx54s1dgwAM4gMiqzEulr8RpwG0K9l4DmTFPDSdPocp6xnkufibKSOutJ7Uz3zI5wSeKaGUqPBAokkdzglVLZU5l9OaZp1UDlHj1WXjnCRfTv45Ncmp-F6Gk6fbtG9-RSlxsWClZMJUZqIUrojdG8-0x9oOqzYgmZurjt57Rrq7xHE1EtM4WECv530RmH38NceqBx0cTldSyB2C5v_VksOOkFQ5eHt1ULbmULRv07gtvAzntU7wfKmXj5n1kSrQ9dZmsDYxtZx440fGqkuPGBRlA8NVB63KYyClsV5EMRJbIILv7z-V6jcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27603" target="_blank">📅 22:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=JhO2XCF0VW6MxO_B5Js8JRbz2lTW_Px3qKvvsGeOR4K17SkP7SWpHAVtQDuBbZqjS8Zw1XOS3OLUeIENaVKq1Rootvem5XogirAmq0Fn0ebwk9-vzmyBBn47devI0-B5MSTVHgERexCKhkTp0KpYofZOoA7TqCcqGWGt2EAa3rKHmvakKUiofPI37EBCSo6culy_QjfASRYfAwEnUrMz3gi_xazDz4q8Vap_DrOm6KwnDrHpV5yWdl-agHbQGjmYqmuoC7vvKlow2jW1sQw8DREuONZfJMqlGH4lzR-toocfl4Uh3xsrkj_y50TJbW3bpG3ih4bZWjsPLnbBWTjjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=JhO2XCF0VW6MxO_B5Js8JRbz2lTW_Px3qKvvsGeOR4K17SkP7SWpHAVtQDuBbZqjS8Zw1XOS3OLUeIENaVKq1Rootvem5XogirAmq0Fn0ebwk9-vzmyBBn47devI0-B5MSTVHgERexCKhkTp0KpYofZOoA7TqCcqGWGt2EAa3rKHmvakKUiofPI37EBCSo6culy_QjfASRYfAwEnUrMz3gi_xazDz4q8Vap_DrOm6KwnDrHpV5yWdl-agHbQGjmYqmuoC7vvKlow2jW1sQw8DREuONZfJMqlGH4lzR-toocfl4Uh3xsrkj_y50TJbW3bpG3ih4bZWjsPLnbBWTjjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27602" target="_blank">📅 22:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Trwl4KKbXxIk9vUCCqPDUHonr1frkXFeNCASXc7Yg53FwYdWTavSiXk0lppeOIPSOovCQSW3MxTCd88Uzed-n7BEBYTtzkjyjTskylU0o7PsU9gmiqdiFaSgpuZNyG9jQfW2iX0F0fX3KypWnzuAenCZBzG55-jKlaPCiFNWnbg6UqYbLUCoHLELcp1c1oSwNfJCRG0T48hiGBTR7Eqz8lg4aqDfmNNFx-8O0xqbPmCBrOKicV03Pnj2WErlfwPTDVPhxRYx5MU9GcwN5e_QQi6lDWYIGyK0ZZg5_2Advkxx8WJ75TgXSVyMTlURYhx1aXQ6Of3RI_GtNSRX0mLHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
باشگاه‌الوحده‌امارات: دوباشگاه ایرانی برای جذب محمد قربانی مکاتباتی با ما داشته‌اند و بزودی تکلیف نهایی این بازیکن نیز مشخص خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27601" target="_blank">📅 21:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GasOFCxSXKDTRvLDq9pO3k2wkAhYYIZnELcm-Q5Wo4CSWI6arHgwQyeaqATnBmgpzzwMC_m9ikc1_26Aqigl7kdS89wLITbjB19vt-_3zd5c4KRN3oYuiqj84sHi3wlgLD9e78vtnBsiYxOGl5_S5QCInzjkswkQ0KGcxpl7fptmaioKNwIYLT25ekXMRLCjkvx9WM3AJn3ki5IvlAyKpjfktb7TsYB08L1tVwmYMKeSkc7pweonEsDz6IzSObwPzfMtf473RmTVHQFNRdHosElkPiW1ze46gNuZdmKVS9xfiQInRFARj7uZZdwZkr6Viseei084e33PpgFkluJctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا
؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27600" target="_blank">📅 21:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csHs9QRELJz282v1qgOzaE9hn8Vg2HK-Ls3UEoTCYCWA511lD11rrNQsixsk90bjbRBiZ1G4yzLcEgrQpC95zSw8pkux4M1jDlXR5O3CjgmcQVNxuZM2-MbDDOxGqqT_g1IG5Js2TQI-ArxLtIVy19RHlwXIBUhDAphwnDc0r9CcX4UPdMMWGAdlZtuAhLr7s-bWnG5nTrlCcvk4dP0aUwHNMj87n0FJL6oQTKMu84AxQIQsTfOiZDj1cRkMfevTQcqQbd5fAVTsFeEEBLJYU0ok2klCZiOBdH4UGPcjtj6_72mTf6m9wtb6WiBiQhNeQVL3aKIXQg7kFbR_mz9WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
حمایت‌قاطعانه‌عادل‌فردوسی‌پور از سعید کریمی کاپیتان ملوان درباره‌اتفاقات اخیر مراسم ازدواجش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27599" target="_blank">📅 21:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cU6GLPmfJm8Tfd8dMbK3qA7r3jaHViGFfT6v6j_dhSCp_st-KRGkRWdm7qlk1D1bZEj0f9lDbyUxMfe4pZh1BbP-_n2YVx_K3mugyDP7csqnQ_-E6XatR21RvyV1SY_xrsG-6-uVHh25_W7ITSEgc_HKT6tYtH6Wi9pgGFLwSkjqhTtDt_5wVsgfJaDivmsgKg-STMsgtVO8hlQ2tTZ99cOxBanVAVckIts0fC59cSt7i-l3J3nwssF60y4sf8JNlBLZIHom5lhH6uqTwySIDQvburJriIK6Swr-3kZG3zf_l3uuS0AxQ3UG7HKEaXAcpDJjIDXr-RQFjHcg3zow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ طبق‌پیگیری‌ها؛ تا روز یکشنبه هفته آینده تکلیف‌نهایی‌باشگاه‌ جدید محمد قربانی مشخص میشود. قربانی بار ها اعلام کرده میخواد جایی باشه که‌فیکس بازی کنه. هرکدوم‌از دوتیم رضایت نامه‌اش رو پرداخت کنند میتونند با قربانی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27598" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27597">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNg9YSShZFgYEbJ4m_VxP5QRW942SaZNeQJZkq33DraEkwl3bon99ztkh6byb_YIHsIO_puOBVsjbJXUaOEUSQLQRPv3Xlvl2_y91wiTIl7C8KgalZGqL2UU8m2ORtGvGvEHTtdFKfurmPCg-ggeQ6aXBa6YmWBt8vfY1RwYnn-c7znLhweTOtbskcDKe_lFdy9d-x7KNvyrZPsc83EDI7iEugLHuzGnWJztkP8ADx_d-WeGdLxIRBwYXUNaOxgYkF3QsWQiNhS6oXarmYSBgeyFEgDTH5D9J8rSTxHjLoZQGqkrGRUbt9PWTrtRPZO9fhGyYzZeV6pENj8kbHrJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ تکلیف محمد جواد حسین نژاد و باشگاه‌جدیدش تا پایان این هفته مشخص میشود. طبق‌گفته ایجنت این بازیکن حسین نژاد حداقل تا پایان نیم فصل به ایران نخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27597" target="_blank">📅 20:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWfzo1a1UTV9IhI7yNkNF5lMs_YcTjxJJyGXaAQgkoZpyHJrzaQawuVPEd5AxJlmBJbPfSz429z6dIDCvReoyMzrDGWm3bdAzKcloR08Fg9uSqTDNQPKUregAT_YTR2k7yHPnXOvPYnJrjMQHvMzh0q-77j9podOMmtiKEmw7pAZJNl0jYv1Ynal9kZMLXk0xzaV8PN65AN05WpnulBYWNo-NLxcwXDSqwtoGQmBWjuXE-9mnPEbMyQBLmNy6WxoEi8jgN-kvuQQGEbSFYYynuBo5z-3zXSpI7PjVlMI0OGo_kqeuvmNRfijCICJ89Lr3d6ruNKb4J3zQcReTpUKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27596" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27595">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=FmymkN_SF0Rp7FozdltYmY0KGo1BTwTlgeqPcK5p7K9zg63oCQxH5754WCEfQGti38PKiTeqJv33KS0Zp7jcaaOtu_OSkVrMWyWqmi-Ksn96ZozRzwvzHA-Jz51qDEBT0PjGt_2GLTLLZzlIEcVCdnDT_pnL5wT0WxkTcO96A5y7dUNT5e8ZOB6x6Y-QvqShJL4PlCnwSBA_npIHnZS3ZXVWrH3dFgxzVpYnicd043LaSzRAXhp0ZEYGOMhZ1TTlMFX2I2m7ZXlSI9x8zNu4D33neVl9Uzs606bRe5987WIis1AlgZAGu5m-sCCMpvn_IRqS8jFg7ghQsatQJlLRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=FmymkN_SF0Rp7FozdltYmY0KGo1BTwTlgeqPcK5p7K9zg63oCQxH5754WCEfQGti38PKiTeqJv33KS0Zp7jcaaOtu_OSkVrMWyWqmi-Ksn96ZozRzwvzHA-Jz51qDEBT0PjGt_2GLTLLZzlIEcVCdnDT_pnL5wT0WxkTcO96A5y7dUNT5e8ZOB6x6Y-QvqShJL4PlCnwSBA_npIHnZS3ZXVWrH3dFgxzVpYnicd043LaSzRAXhp0ZEYGOMhZ1TTlMFX2I2m7ZXlSI9x8zNu4D33neVl9Uzs606bRe5987WIis1AlgZAGu5m-sCCMpvn_IRqS8jFg7ghQsatQJlLRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27595" target="_blank">📅 19:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27594">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRKH2wvUfk5BqGXVUtwVPNoTwUkGHCIFgyE0jkHXP0ck8mvAFAnElDB1puBsrpviZ_ezTML83MUQBQaWV1w7lyuMQbfRXzrXgPQCffM28CI4v7GiQ2iiUiHTMckw5ZtWGGX0RRTTHaDo7ALvr2vgXS8qNge7Lbct-HmK0RqKrsE98l8hmLuOQEjLr8DBBDRQTrxiixOcpTf1Yydbhe2z4t0M1c1svKn-4LXTnzq_a2WvJWXGhKozIQmnVa2BYei1CNxSwDLMV7zPmSNHCuhVmfQR1U14vwNqFT8NdZTU8Mjtx9zu07ytihYqVkh2Iwt2CbjYleIcreVOZ4Ef7639AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27594" target="_blank">📅 19:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbfmaBNna-oF-bkQSZM-ftOsJF0JnG1v34I-ekkpIlC2OvYATKR7aO7HaUswBdAsnFA3MVdLCerTcZB8Ud_9rkPTX3y4zcGLnq6akJ0pLpze4qa-JaWq9sSimAaKlYDdfsmjmWOMpFAu9Im1ocOVr58J1r9bFarpiWun-HjXomW8zHiuJSmnsC6nGL6p78Ddfi8sJT7LcIeW92XZM2MXEX7X5Lt8MJHLX5iANq2GFK1vNCO1WG_JxSP0AnGtuBBZNn8-PA1hyVfjnNn-CfY1erkbtcbSDISh4v_j19bDmnocMXAUEaWO_VumPmzHIblvn4KBShszS3WXOA1_YHPo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛
برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27593" target="_blank">📅 19:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27592">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU9bLOy5vWX2ot1CGNkDI1kP-jj5JHgGug2yKnhdjrixwpLasu0dMNOubUagOZqcyGnZaBfQ-fgC2YpOjeWf3MJTzikq4JbLpMgBS-Ev1NqJSlK1SrOEt0RWfQDZ3Df_iqR3HGKuFtjpyDHINPKVRs9Um2y1MX-R4bzEarNLGhpRLloBa4_1HycMBrBQ93znvwM_yaIGV1A-xh-5KCj09cR1XslOjV2JaJ0fFqSo2h2kZvcvR2MGPE60C4UU7r-7mQfwupVlDcnHIVqcA-4y5DHdqd0aCuXuxMrMVANeuujTxoAEY6yk2-z_Bu4aLNa8U08bA-Vt0YY8rl_AHqNhjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شانس‌باشگاه‌‌های‌بزرگ اروپایی برای قهرمانی در فصل جدید رقابت‌های لیگ قهرمانان اروپا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27592" target="_blank">📅 19:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27591">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puF7X0FgBmj-PC1mwQHgDC674aCnvVeYEslX_Ocm6X3W3_um_51eW8hVZFkQ0C2nCdvq_l7kcYMvogrpyEe2IYZLrgaoz-E9G48IbidcQce1YZyJAysw0ufgmhkeSfUHO7PtXojvhfmzKWOSnbL8NyVrCLquhT-2foLZ5x_RlBVwr3G9y4EIwkJP4UYabjCS9BDTZMZ3sm4RMEYG3kbqQZwDvr25JvLqD3ih3u2i6Q7EO65RXnz83J3tBKWWs6MMSPF1id7dsUr9U4AZrFmGKT7vUjZA4M74PTg1bqnD3fBeMs21oLifnYXlYCuETnvqXWU2SlXfrej6uibXtA-xNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27591" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27590">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfnT4EcRJyayfuG7Fat-kH_MbezFFyx08hV9z5DMrqtyYXVcwuSKQGw58E2W_N_IbqbWYHFC_lsEV4WW1iKfvXGkqGJtFK7mj95ltVz367LUiGKzreehnm7d_Xwz_suz0RVxbrguYteonYPYsxl8IaJA_ayTaD95sw5-lOmmBbPIze-0ZOowTsyYysXDOxOKCVGqHjCv3QqHzsTaa5jF4vtjH5GwCHp9G6n05TbEs4jDZsgwzjfn3wAFE0rZvw0e2fYMTzAa1ett4P1OjzjThU5VO2l4uez3uX2Mp75LFYhrArYK4-CrtjIJeYzCIxyLqpRVTfDyAuoEeqdSP6P4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27590" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27589">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq61NsEFK2XnMD9-GsJoIaq1kBWWd80J3BnLE_Kfhg4p3FI4rUwY8i-3fCC8eSW9HigocMzMc0gVoDXtqdVHvMF4WFWi2OV06BDszflKOuNgTnaEYPCctUvErJb7kWLp7Sa-He3-xEJwrZVyXndgpMeziFaQ2TAfvtMpBwWxYaNK2UPU6iJI3O7RB6yM-IjpCL1rboFgCGeCtknhzywjAk3yxO-1ZK3VSCjy6bdC1qF0XqXYKOZDltoPfenAjBATZSZmgeHzet0AQaX_f2o1YYTIEbVW6q-9PthbpWwsclC6dVDBBQd6jnf-S1snTwhVhoHymvwCwXiJFrXxpFxBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سوپر کاپ اروپا
🔵
پاری سن ژرمن
🆚
استون ویلا
🔴
بیش از ۴۰۰ آپشن متنوع برای این بازی در بتگرام
⏰
چهارشنبه ۲۱ مرداد - ساعت ۲۲:۳۰
🎁
هدیه اولین واریز، ۱۰۰٪ بونوس رایگان
همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram
بهره‌مند شوید.
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27589" target="_blank">📅 19:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27588">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDjKQsCw10sYpQOyK6HnnRVDFsJLVOIPzddxKwJxYlt2YEQgaXjXEVsdTPpYoflp2fNRnMnbMXsTEQbtsiHypXuIvDzpDy8y5v_Q7wetQpUbpo_6KM56vcq-UX3NXxZ3qOd1hgLkiR-ctuKPby0ib7zQnEVMS3n0jYmzvHKucgRBL41UIZHJH9j6V7rA29_AO44wXF6bEjs2oFHZ5HnGatQcldIYNQZtMf0NVOS0gPjjZJ1lSd5-SvhkRvKf_KDFXPPV7IfvbQW4QnsgPZTPW7F_tSurM5uyRhmPx7wRzF-c3K-mtn5aNfF-LWn-L4drHlB5OcTc8Br7zY0QqXBnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغام سعداوی برای‌خدمت‌سربازی راهی ملوان شد‌.</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27588" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27587">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK3szXKG3xbIsfI1HRkiJTDZpcjL9s6hkFe31O7cMHAwSoyf3YosgOpbocANulPDxr5TPGYJwTrvi8OEfLe985RVIHcKiNQ2JbRSraXE_IG1s0856m71eLumfLzM0kkb_KgGFpcESjeCwBfgYXCPOn6erT4bZWYEBVkznw465tgrbu0m4YLh_EDfCrAIo64NvoX3Scrc37b2h9zUO9hyhhAYS2aK3ZrYk2iktcww6yi7ihN0EBWl-0m6d98f-5A5HFSgitm_8BRGpnXOuOlqaAjZ-rVmNaNW9cnNvDbe5Rdkg0wLF8Uw43xx3SuWuUC9cy6y1yPsbYOAyG_QDI6zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27587" target="_blank">📅 17:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27586">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzPwA7WZeQ5KHuKrW92fph_71XEtmacaLPDlYLPwEV1KbQekQEnHDpRUISvjZVRorGEGlbDeRfWn3Tyj46Yczlq6Uv4yhrWXZmo9ytkA0Ebi0Dlc24qXKUMzSOkgx9atGL3Uw7c40VdgUKIIQ9UTbaz63Ogg0SGwpNoAfzXMVYEaOKNY2upJP7HZbDnxhpbYn2LooVivgtm43FC9GRBp65EsBvM2yNWyzrSsHPhnPsnug447O5uIGk2ycgSd8kfP5xbMa9FHvry5ykKrop3C0qSn3cCoT5UlXxVG0xuVbXyzkuWlN_Kqf6JVOfdj2ePHkys46xqu2FdPN_xgOP3B1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27586" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmPB0aQ-S7-bIwtFkQBnbpdgS9kVBWItKhIgbRMMQGdOzpVmSWEQ0kGiR5unGKIPQw-qPG0rxP6L4BanQm603xRhxyTOvefpKSPxCgL8lOy0q2s3MfcIw7LlosKNmFbiR20FtIUtlQ_S9xskANzQvldPiZtSgbfqoaa3aMdL8pMpFsFZRGr2BhJyXOg2W2oTYq99VVWr1yzlbPSa3hoMghaZBa8Vwm5M5FEB_pCFBBBpjnqjpaJKLjfqHDIKVb5TlNxueHkO91pVHjTXLqpPhL-iDhJ-dq8JA8SFyNmrbzyP1N45IMf82oiblKLJNXdYCUFW2NmxrisSJZ8s0qyjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه اینترمیلان برای جانشینی دنزل دامفریس هلندی؛ جِد اسپنس مدافع‌راست26 ساله‌تاتنهام رو به خدمت‌گرفت. هزینه‌این انتقال 31 میلیون یورو شد. اسپنس انگلیسی فصل گذشته 44 مسابقه برای تیم تاتنهام به میدان رفت نه گلی زد نه پاس گلی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27585" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7TWYaAEx75oxisMrtmKwlH8AwBGcdjEOOClIUv0nHwQ2wzrAyLqJZA_sU2O_6FW-q-iLLXeiWrqAeSDSJ1ZMkYDHVl7x9M0-lMnCYKEIcZz3tlhmxXqDCKCw7u7e3mXSlK1CnLnXChTwhAqvLL7Tc3YIYidztf4rR41ABsPMk1vfpFy_HvUMNkZwHRue4VjORAzqP3xqhx_39eApfF0Wqz4h6S-azgmA70K__VGrD8N4dqkcBMRZ33dxdghMqwseRrkkI08mTidQD4fsvsXGtt5CHCqUZsox-8YUz3TbVnuhyDe-8uAXnlGH7Az2nazGBg1i6S0ngSpocgfP6DPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27584" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7ta5aeCWNDCDBwuppn-zHJ3NL5-j2fOQYKCZr1XmziSQar6IEgt6Am1YjkEualJXGnbgPmANjaSZYHxPMQ_aKi_zl7aTZvA8AMi1O39ax38o0eDfjJIZXgBLjcp2n4ZLTp2p2WxjEJiTy1yKLcCn8sWwhyFIYLl5X6xYKZoCZzACFEYza0lOQurcs-9qKefZ4FM30a6hexhXFClL8ni9Mcq2yI2VFsRDi3x791RBjYTqdJlEMTqMVbiZua0-K9ycfU9Qnse2OT8B-EEVKo_P_kW5aEwhD6JeFB6UrPWeu4TiFf7RHUa8A8F5vqbjKDaytV8jz263BiZI-i2-rVxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت:
«در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27583" target="_blank">📅 17:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRYfu9RN41yBE8WLBHmO8UXbgJpkFzwK_PxYCCb1uCXGzhDi6C8Tkzw4VT4LCZh9Unt5kF84zb9ZDJ_PmTdUQne3k13usCse4UZVJsxSkc9PjfXpCpYLnPhpHClRQefkY9WQ4LldkIAB3VD5azZUQQhlFKFCRJU4n6zUiGzFUrd6xo6paSO_BSVU5rBz7uc1br0uJ_gVPVAWhya2LM91aOUjmyWoYdVfgdABASPBdW20HpmQHmZM9VZ8UefKi-YrCExq8Wo_PA9E1AKdOXA8epOujAk2DzKzgIx43dPKAairylHPADAvFHPYDJAIjV7BvjxsUIhOVA-T7pENdYvReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فیفا کارت‌بازی یاسر آسانی ستاره استقلال رو برای فصل جدید صادرکرد و به مدیریت باشگاه اعلام کرده هیچ مشکلی برای همراهی آسانی وجود ندارد؛ باشگاه بزودی نامه فیفا رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27582" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyTGgj_3JejpzxTMsyBqIEz_CSafKZx5cTc85qB1bmmAZ5TXiGYaF3pzPG9SXlD226D5pBrN5ju61JpO3jGnZukY7NO_ceOq2qDr9kkrawM52NKdQ_tdM8IyW6CJC0JNeGUO0cU0OJ2nAtr9IKQSKP8ue1Gcg_RDSaACf56miJJxFLVIsnY4x9Ydgf5zukzF9Vqk51ve64OM2R3XtMyYJ4LtxUBR0t2PeafQf-YFT95HtqwDdBKyXuRGtSiDiE0f4jfPGYg7Hu5IDN1eCxtdfY0UCJogC4yyNTSZqxM4UbPIcLUfjY-I2sCHTevBeDO0FNSurlvBcZxGXLwyYj4s9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
درآستانه شروع فصل جدید رقابت‌ها؛ از کیت سوم دو باشگاه بارسلونا
🆚
رئال مادرید رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27581" target="_blank">📅 16:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGFIkoe22L3jVmFRXF9U5TdS9uocmgF-B3kdMZ-g5_VFwAaLwahgS5Ng5Fu1-o-UfJER_KmY5vkLVQCOltVm3rAxG6SRCixGfm7mrAIIzf03ZaS2zncoTR05p6mPh7Gx5dJbpImRbpaAFi2p38JNEQUOgc7ALfdfc7xR23GvPmmb7mt-u6NYmb3IjhbTDqiHbeJheyD1WkX0PtkhVVqiOfmjaHaqjvFOJ4-0kKHt8L5Ji_ul093HIL04i3LaQqI-v1W-KE-BWsMA0ahNCgIUqvqYoGc6Acg4FsVNKapzF42bTS4Dg7ymLFRHccgaepDAIuSzGz63Rrw7lgRgbts5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27580" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOaevlLIDABPH-F9EgnyTvLG73CB62ZSeLY52aUzopZv0q72BTBWHMTiJDY_dwZcaIREMBdmCpGQLImY2Y6Es20rHGErcMWu-MHPaJWVdRzlXZXFVpNMTBnmnMGsjChoL5OFV8vCjqj30bYtZt2WWmgbXVnhidEKUPy0IBtftB6qaeJbLbI2QEnQgpM9bLsK-oh77ZR3noMRq5Hu_U7mBLipzxzdija8Bjm1ya9rsihtm4Is-5bOHS-bX8-twinj1lh-6koNCF8-_za-bHU7Y9DD8MlK8dr58-JNzfZ6vPPO6dxY5mnZoyhnDrSfoDJ3O9G_qeM8KoTD5YJefItq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
چنین‌روزی درسال2014
؛ تونی کروس اولین بازی رسمی خود را برای رئال مادرید انجام داد. او در این بازی، اولین جام خود را به دست آورد. این جام، سوپر جام اروپا بود که در برابر سویا به دست آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27579" target="_blank">📅 15:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27578">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj-PybByvxtIfSLqOCMYB6L4tWgKzemu4Ncw3X8lEBWt6o1JnjM95NMEIYo6dZGKcExkvsgD_0CsULENi7MraQKyhZMz2dQKP8JSBBmW75vRuo91b3lLYJvKkEJVWHufh__Sq8Ha5Uh3ZWPh_zFE7oqkXIAEbZapdtPraAe72tNbfTqT7oEXYzTOfuMluvh6dA2OHZ1TKWHmjfyqX5kAyg7FfDeJf7eE3jYZg9JOxe0C7lysj9osuF9Y6nwWBJjwA8Qs-FBp4w7AvA90qSwTKleYM106ohzp9Dckz-u_ZfUFmTndL282TEXdu3TM_j5C_x4kUXgxj-hUXE7emCc7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال طبق قرارداد بسته شده باید 200 هزار دلار برای فصل قبل و 400 هزار دلار برای پیش پرداختی فصل جدید به داکنز نازون پرداخت کنند. بنابر این نازون چه برای تیم استقلال بازی کند چه‌نکند باید این مبلغ به او پرداخت شود. اگر نشود‌ باکوچیک ترین شکایت داکنز…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27578" target="_blank">📅 14:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27577">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTg7XFtB7nCbCI1XwpXqJSdddjKB1iyL0Ay9KIJkkHarKKQWe3r2y-Hoomxdt5wDwVAmJJl2Z2HZ7kZBCeIZBqP-9NweiaavWskZ0sb_qSrN_O1uI5Say_2oqerEyiN-eq1kjNRH9RPBcpZk8Jicf4l2tnLVysWItag_IiFW5Av9780aO9oDygX4mj2giHC8-useOpRqa-OWd5dbqMGl8aRQs8-ZJ7bNjNQfljo49jxwo8pUJ7cVXHgpt6LzFeIhIUmzWS08WDLg0MTwKEe9PkiIS4qS_phY8gU2j1aoAhvKhbzAKYn_U6nY3uL2YhQRe9_OoWhiY-hKl43wldHg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27577" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbvWJrOHmGC5YwARkxQY2UsN2-KoGZaszPpSomEFlA6w3i01zr2hmLxjtytGMmRcHwNVxWWo0cR3H6O8VvvXSR4RBzCDhu3zpznM-C1b5KtLJcyZ2xUDk_vhtw1Sd8dBS1ohdtdaiXHGWJrmEBMFqV2CEnsMbvLejFFJ8t0gWv2wI_1dRT9cuTpDI9ko3oXpjnHsYDUPK3p4u8yMaZsR18PYQ1_Tnwd81vKbAaiGZQw-U5M42kZpOK-wM6FZLzCbLpi8iP9RxWAuNRwMlf0rtTN4HHKxgG3oZczF5broNA-aPedosag4Azb1vOElDs0j00GsRM0_d3u9BEi27JQjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4MNcH1s9U2ymeW8lqocRI81D2xxwjWwDyZVPYJOza_qIHdlrHaDDzNwVwiJruUmNHeGEF3jGq-eSqMqt3vWtfEMeYvGNug5FAWKOHDfsIcQA4uUehNPFcBEAi-ZeMeXzMM9rlEdTDBDHgqx6ebKraq5moIrbOP4DdKlpN7mR4WyMxrla-s-33S3NRDV43Fii9wFjIuT2Mi0h_vD4XQFqeHxctN4pJYS7Te7TEwIHN1srGNbApd4NX-h0ZDgqhlVvgox6n6HC1leOlRVjUjIqn_ufuOgC2luWmUvQ157LilUKcybeLFAJI3t8wm8c4Trhdwb7LDYbIlKgRADeIPdRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_0105YDZjCsDZFduxOj13edQC1-2mdsmbH5XNnwHAS-LVcpCpekqX_xYTXHPjJEyUw5p7x3uKpEdm7eahoUL4RhiSSyH7EThWkkrGVlhkrQElRobRh5bpsREzeQ0ypunewY963kFGusqY-_x4IICd7Czc5f6mPmaprhM0w6wg19SFjAPR57PKjcydy9xRf6eiy5qf-iQEezu55EuhrDiCT7JvzBkMq3Z3RJ7PjOHwFGAhW1Gnl65-OO15-pQMfOiGmF16pBjGf2KkeaXDxs5tX_OPAB9itOx5zo29TtAQA-Ob1PdfPxLuL3mevGbBpL-2NYuk4yngh6albFygN1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
