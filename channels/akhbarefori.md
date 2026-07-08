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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-668582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حضور پرشمار عزاداران در بین‌الحرمین و کربلای معلی برای تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/668582" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aozAba08GG8d9j7CEB_oZ0S9BUhuqZ-VDunnE6Nc0AXPDTGi3RxtQvJYUHNZSuvjHvr7bZq3B1-2K__84XWoigMHXA1Ba6KQlOf2Xeh0n5mDTCgyEuxKmvywU3w5BQ0jDtcRp_fgZxOvgBfek_8152Y96wETKEpfl-sKngVHSdH__KMt621ovswHQE8H-GbOtBJ9rRY63TfUhudZlfFWy0TqXkGlxKMDHjeV85oRYbTgO62XDk87ysb5bWGWX35fUMDCkYPDkXwMOuUnxezF8wlukkF0hSSjxwJCICGfWAtJEhE3Nn2jd73hQZkzKtwgLqF0A2V2gIou5pBO06tOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور مسیحیان و صابئی‌ها و طوایف مختلف عراق در کربلای معلی برای استقبال از پیکر مطهر رهبر مسلمانان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/668581" target="_blank">📅 19:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpRfM_6cd_2CU8r6Y-u9Vs39Lya4dyyZ97xvj0yTThp_VjZbtK8FngAgY5AZ8xB1Fmsql3x7VEX7_9Ysy5ELK89S_INj-lxbXsFUeN2pAZLln3dIqxSWlTawYNlJBHOKxWtqY69FIQr2uwg56v56xjzCnhojGvSINzsYbfHjSNInD3EloKZjcREJj23dFs48rjd8Fv5zmwc115hrJpXyde_1Z0jXSOqV2wSDwI28RkdLy_eRrXlrvxe8NnIJEJX0hflRjEuIzdx3hA8NGMBdzXyEK4OPZBSjJqh7ESCRlqVlvhCkOwjQzICvAaOGnXYSVweqf4vNJQLChaQjrp_voQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خامنه‌ای ادامه دارد...
🔹
تطبیق اصول حکمرانی امام شهید انقلاب با پیام‌های رهبر جدید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/668580" target="_blank">📅 19:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بی‌بی‌سی: ترامپ با وجود تمام لاف‌زنی‌هایش، گزینه‌ای بهتر از مذاکره با ایران ندارد
🔹
تهدیدات جدید ترامپ، قطعاً حرف آخر او نیست. او بارها درباره جنگ و تفاهم‌نامه اظهار نظر کرده است.
🔹
اظهارات امروز ترامپ را می‌توان به عنوان اعتراف دیگری تلقی کرد مبنی بر این که رئیس‌جمهور آمریکا با وجود همه لاف‌زنی‌هایش، گزینه بهتری جز مذاکره ندارد.
🔹
آمریکا همراه با اسرائیل تلاش کرد و نتوانست حکومت ایران را نابود کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668579" target="_blank">📅 19:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUYLVSf3mxj9Oydq9zNNh0YLYlm96dXHbR8mTdSBc9YBOQU0N53BfhTUPEZtZVICJ12CD--zV3JfysyYTKFcCfiroUxqtACCNRWiwpqrhbICRkAPbW_4kmFyvyPzK_RCD8CkMwGyTyxVyxF_PssJdoQ3bEZ7A6KbGZNxDXNTcQLF4Bmcudee0n2XFVi18Cn9vtkSYZKuH_RUqnDWhQ35sBqAVPmTkTqIQU1egS_KpxnswoFLGalLyZ4hjFqSNIha2yNhKBd4hTmnQ0_C7hHJr-8lIHZlwzaV0nzTx-ZbbDQKoxJrHZ0oQpq8NDjBnGkcoyF468e9D1SVUpdipdaK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛒
فعالیت ویژه ۱۴ فروشگاه «شهرما» در مشهد برای خدمت‌رسانی به زائران
هم‌زمان با برگزاری آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۴ فروشگاه «شهرما» در مشهد با عرضه اقلام اساسی و افزایش ساعات فعالیت از ۸ صبح تا ۲۲ شب، آماده تأمین نیازهای زائران و مجاوران شدند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668578" target="_blank">📅 19:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای تاس: مذاکرات ایران و آمریکا متوقف شد
🔹
رسانه روس به نقل از یک مقام ایرانی مدعی شد که به دلیل نقض مکرر آتش‌بس و تهدیدهای آمریکا، ایران مذاکرات را به حالت تعلیق درآورده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668577" target="_blank">📅 19:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f87b03e2.mp4?token=VjemKpDxaZHxSm1Hz6ZkrS1EgrNrJDZOVS0VnW6IjhIJ9YiwM5BPDRV6skc5MK825OIajMQdXvua6DfsHXsP7Lcoa_L4tf_KwA-0-EPr4SdcLx-oKyKtAJdZifaEE8rOd0hMTqexqAvnYZZ6jgtho30xr_oATuPS0KEEpY1rrbDZkieo8zICKqf79MfszYhujCgk9QAdH8taqkQbGT1VdshFKjhy5MKcc_prjSZI5eB1gPpMuhqmJa3AnkJmzctG9Dlm1-2Y-4vspZ3PumeimP31I7lYWz-ikFwrvx8ExsLxkTTdpuBS9tJTzE3LEccQfMxD4yOrTRl9P40nJgnoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f87b03e2.mp4?token=VjemKpDxaZHxSm1Hz6ZkrS1EgrNrJDZOVS0VnW6IjhIJ9YiwM5BPDRV6skc5MK825OIajMQdXvua6DfsHXsP7Lcoa_L4tf_KwA-0-EPr4SdcLx-oKyKtAJdZifaEE8rOd0hMTqexqAvnYZZ6jgtho30xr_oATuPS0KEEpY1rrbDZkieo8zICKqf79MfszYhujCgk9QAdH8taqkQbGT1VdshFKjhy5MKcc_prjSZI5eB1gPpMuhqmJa3AnkJmzctG9Dlm1-2Y-4vspZ3PumeimP31I7lYWz-ikFwrvx8ExsLxkTTdpuBS9tJTzE3LEccQfMxD4yOrTRl9P40nJgnoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل تعیین شده برای قرار دادن تابوت رهبر شهید در حرم امام حسین علیه السلام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668576" target="_blank">📅 19:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a11958c8.mp4?token=kSZtZXXRE57QPaBHTuoeARulELCIonF6S9hQzAJLt0i5LTOfQ5zd34hm4oMQNIxlxGpyxDu40pxK_aCnBS3unEz4pRVXTfClmPjcI8pYCrHcJfF5A2z1T8RUC-NExJdf-SN8XFo_C_diA4loyo5KMjx8U5ptNAMxM2hf112MlJT8ZiCNisQBwYEG5ZRAQ0Gw4DVs2UhSZiqSsT0Or9TkqK0ruuncE5TFNsfoP9fsIR1d6mmB29OzvJSy5tY4BTD_O50gKrgLJiF-SNqlGcHL4eDa9mknUkgZnSlxjYVc5ar6zZJi7D88zi-UxG8L6neWrgjyovJRgHSa42fl21FUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a11958c8.mp4?token=kSZtZXXRE57QPaBHTuoeARulELCIonF6S9hQzAJLt0i5LTOfQ5zd34hm4oMQNIxlxGpyxDu40pxK_aCnBS3unEz4pRVXTfClmPjcI8pYCrHcJfF5A2z1T8RUC-NExJdf-SN8XFo_C_diA4loyo5KMjx8U5ptNAMxM2hf112MlJT8ZiCNisQBwYEG5ZRAQ0Gw4DVs2UhSZiqSsT0Or9TkqK0ruuncE5TFNsfoP9fsIR1d6mmB29OzvJSy5tY4BTD_O50gKrgLJiF-SNqlGcHL4eDa9mknUkgZnSlxjYVc5ar6zZJi7D88zi-UxG8L6neWrgjyovJRgHSa42fl21FUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار عراقی‌ها: یاحسین علیه‌السلام پسرت سر خم نکرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668575" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=u9YNovL-I6bPb4NV2jOeAdlC6vOA_onjAap-3a6LEmFu-IW3p5B_yyBpiFt1e1Oc--Py5EIaqIM-eUKdAysuaMvsyloicyxz0fpMIN4qTuosvBXGSUvuuMGQQC8pOAJnWRhX5mpVDgT4z9QfzYsB4H2zGb_ujywcNgnAUxtC-22l1nlsqcY8BIRZUnXHxZqePqQdorMFXA6aMuLNo-iqe3bF-kJ1M52XT0Wt_fuVGJqn8XbvyfR-9kWdHJIA6Zy-aWUguZ9ldPF1zqYZHrnJPhV41wBbnYAe3_ZmlBhPfEGxG9T9-mkanC7efeT3VzXKuTWVezSqroEO3QGH1tTI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=u9YNovL-I6bPb4NV2jOeAdlC6vOA_onjAap-3a6LEmFu-IW3p5B_yyBpiFt1e1Oc--Py5EIaqIM-eUKdAysuaMvsyloicyxz0fpMIN4qTuosvBXGSUvuuMGQQC8pOAJnWRhX5mpVDgT4z9QfzYsB4H2zGb_ujywcNgnAUxtC-22l1nlsqcY8BIRZUnXHxZqePqQdorMFXA6aMuLNo-iqe3bF-kJ1M52XT0Wt_fuVGJqn8XbvyfR-9kWdHJIA6Zy-aWUguZ9ldPF1zqYZHrnJPhV41wBbnYAe3_ZmlBhPfEGxG9T9-mkanC7efeT3VzXKuTWVezSqroEO3QGH1tTI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مرجع تقلید شیعیان کربلا در مراسم تشییع پیکر رهبر مسلمانان جهان
🔹
حضرت آیت‌الله سید تقی المدرسی، از مراجع تقلید شیعیان در کربلا به حرم امام حسین برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب رفتند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668574" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxTT_c9kEAXyLHeKRMnvnIcnzHX4SlR_1eL6LwIAsLct6tRRtOoQ8Sfh7KJrqgXtH3SG0xaXinpbzHctRTxZ5z5Z8uh71NdNok8ePaThZtMjWdXAF567kJPYigNZhT0F1kaa5eJwr54A_jx4KA236Mcw4W2IBEVj2q9hL0jWUVADsH1w8znG163j3c-q-CpZyaeaFWuHGZZP2taCvee5tSSwqb2Een-LPG6FeKZrhKf7DIaA3ToNwKURlidRi6aRbwIxnqOf66xAampPyUSoVcuJelzlvgpG2XKZtnygCIJICgasA5k2Rnf9A3EC7GSQZOns8tsf2gaRVwwDaNXLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش: به دنبال حملات بامداد آمریکا،
۸ نفر از دلاورمردان ارتش به شهادت رسیدند
روابط عمومی ارتش:
🔹
در پی حملات جنایتکارانه ارتش آمریکا به مناطقی از جنوب کشور (بندرعباس و بوشهر) در بامداد امروز، ۸ نفر از نیروهای هوایی و دریایی ارتش در حین دفاع از میهن به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668573" target="_blank">📅 19:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آموزش‌وپرورش با تعویق مجدد امتحانات نهایی مخالفت کرد
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
پیشنهاد تعویق امتحانات نهایی به وزارت آموزش‌وپرورش داده شد اما به دلیل تداخل با برنامه‌های آینده و کنکور، با تغییرات کلی موافقت نکرده است.
🔹
دانش‌آموزان و داوطلبان کنکور ارشد درخواست جابه‌جایی امتحانات برای حضور در مراسم اربعین را داشتند که ما این دغدغه‌ها را به وزارت علوم، سازمان سنجش و آموزش‌وپرورش منعکس کردیم، اما مقاومت‌هایی به دلیل تداخل با برنامه‌های آینده وجود دارد.
🔹
توصیه من به دانش‌آموزان این است که درس خود را بخوانند و به امید تغییر قطعی امتحانات، از مطالعه غافل نشوند.
@TV_Fori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668572" target="_blank">📅 19:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود.
🔹
خوک زرد
:
احتمالاً سوریه را از فهرست کشورهای حامی تروریسم حذف خواهیم کرد.
🔹
لبنان مشارکت در مذاکرات رم را به عقب‌نشینی رژیم صهیونیستی از دو منطقه آزمایشی مشروط کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668570" target="_blank">📅 19:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به اطراف یک بیمارستان در جنوب لبنان
🔹
رسانه‌های لبنانی از حمله هوایی جدید رژیم صهیونیستی به نزدیکی یک مرکز درمانی در منطقه «النبطیه الفوقا» در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668569" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjGcUtRnADQbgi-IVe-JtNboDeXJ9CErkshxWvabWWtXas5mYMqCSyanvJBha5-d3uwK1cA7SoZTvcoM6jdFBOtfn0otxNNrIgk1TudfMCpvL9NstRwbigoJHQol4KcmW3oHfHVt4n689P0YaGMPETMLTlAb-9EXv2J0rYYymIwp3di00pEmttxg4TFW4LysJGvjlBV3U8R6rYdj425LOACImNrhaaaHTWobOJBJNWuxk_KB6dTCN7Pn6Mv3UNJRGXwyqbKTTTNyfPyqHmKrF8vETjUt-UabYYse-b4XgLgxFBQLlEiG80hheziKWgEAHgBUZ8Xen3cg7bJHyrRQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش زنده مراسم تشییع رهبر شهید از نمایشگرهای شهری مشهد
هم‌زمان با آیین تشییع رهبر شهید انقلاب، پخش زنده مراسم و تیزرهای هویت بصری از ۸ نمایشگر شهری در نقاط پرتردد مشهد آغاز شد تا شهروندان و زائران در جریان این رویداد ملی قرار گیرند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668568" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1SFOCgHrv79N0y6Asmn7CeCCBLL0415rf-0S4O0-UyIqvhgofB2r8GOo_ld7hwgmrjCjSb4kUDyGPlRD2YX3RY7OF9ZHyP5OoQcawNB39_4H-2YlLxbxGCXdpmC2s2KzAjebr3eWMfDTmVUSwarQaSanI8vIs_A482aQOn4ab_DdWL6CzVjHj43aTKPkKl1ohdHN7LgiNoFu9mGJQSSLNHkHu4XgzHlboJ4HltEgD-qee3Du20kf8VQYVlHtSU1KpMqbtdkt7W-AeiClgqKGyedxVh24SgTYQ2NnXnb0jOTYbxIy6cAisRI6Oir7prJiwBRVHLnWO2anXZ1m0FyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668567" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGU89VyKw-Z3plC7oEWybI_PeX7JL0n7FjE7m56lhWLf-6qHft8vnwKEWGuB7MMSHtX4mBG0gHRbrEVLuE2TCkWVUA2T7dC42QEpfHDiukrJXqgamrQsL8JoSbBCx4dwtnVqOBoX92dEr5F3w_TW8WSBar8kVrV53kom9snITT5rXvCqkatT31G9ZN8JouGwCKvQ8wqtIZWMqQQVxkMT4TYwwgyJjaqm8EH3NtvqcovPUJDUbyLrtML-awkj-n1HRrbSAcuNvu1FqlPgj-r2iEJ7CPjdYY0U1khiikX77pAmXUCigmjGdKA4aZ-FYcVyDLaiuhVYlwiziaAi7xNElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت دوباره از مرز ۸۰ دلار به ازای هر بشکه عبور کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/668566" target="_blank">📅 18:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc185bc0cf.mp4?token=KUQqTQq3DgXtc9OSOVDnMLCHJLRJUW1Vxu7aD-ruvDm2UYtAY_RgaV8vyaF_DCfSNTyp9EIc6PwN9EMcXINzN9cpjm8rXrqu7KqAZHxbSxPxwS5JDl5y_lV4Fa8_NMRFgf_cZSrrxya9z7TSQFsXnwdBqLbfQcZJKjtdet_-wrZkRGYVWyDhEF9Sif9o7zQMu7pC66dPesV33BKAU7bJVkJ-uZcwA2_mqNlKL0oY0SEzC29v51Mh85q271Cp9A-Q-B1J2fldxhUmRiYn5MpSV-E0ZaJ1LZRzLz5WQHl1GWcr-ITSdN-4zAV0C9apyfQzjYQQsQjGmV6J2vnDPsNdFAwlFBq8nQVncTIFLqToAxlkR3rVW_aG5WW2h1F3eBdx-mzeUsvZySEKBWvb8gw0eWmxEIyq059q3qIleUPLv3opG1-TA4J9V5HNmqIE0XxcyFYgmA9lE-5IpLi3g3JNNwSD6x1gz9YUVsY_-fvpIR7unOdBfWD2U9BObL5gF-PO3jeGv_S9Zpusm4kCZTBPYkrP-3kpWDsPj7RjF-ZK2zgWWT8FEuQnMFGiq2H2mHvPfvTx4Y2ziLiCfkgF251fFJ-vQizsovGE0Bfny-6Lfrax8iZsnvh393HebxGGjWqtlRVId6G9bu6DOT2X7SybHdMptEImVA406zVkvf9Udv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc185bc0cf.mp4?token=KUQqTQq3DgXtc9OSOVDnMLCHJLRJUW1Vxu7aD-ruvDm2UYtAY_RgaV8vyaF_DCfSNTyp9EIc6PwN9EMcXINzN9cpjm8rXrqu7KqAZHxbSxPxwS5JDl5y_lV4Fa8_NMRFgf_cZSrrxya9z7TSQFsXnwdBqLbfQcZJKjtdet_-wrZkRGYVWyDhEF9Sif9o7zQMu7pC66dPesV33BKAU7bJVkJ-uZcwA2_mqNlKL0oY0SEzC29v51Mh85q271Cp9A-Q-B1J2fldxhUmRiYn5MpSV-E0ZaJ1LZRzLz5WQHl1GWcr-ITSdN-4zAV0C9apyfQzjYQQsQjGmV6J2vnDPsNdFAwlFBq8nQVncTIFLqToAxlkR3rVW_aG5WW2h1F3eBdx-mzeUsvZySEKBWvb8gw0eWmxEIyq059q3qIleUPLv3opG1-TA4J9V5HNmqIE0XxcyFYgmA9lE-5IpLi3g3JNNwSD6x1gz9YUVsY_-fvpIR7unOdBfWD2U9BObL5gF-PO3jeGv_S9Zpusm4kCZTBPYkrP-3kpWDsPj7RjF-ZK2zgWWT8FEuQnMFGiq2H2mHvPfvTx4Y2ziLiCfkgF251fFJ-vQizsovGE0Bfny-6Lfrax8iZsnvh393HebxGGjWqtlRVId6G9bu6DOT2X7SybHdMptEImVA406zVkvf9Udv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فاصله کمتر از ۱۲ ساعت تا شروع مراسم؛ حرکت کاروان‌های مردمی مشهد به سمت حرم آغاز شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668565" target="_blank">📅 18:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حشدالشعبی: ۴ میلیون نفر پیش از ورود پیکر رهبر شهید امت، در کربلا تجمع کردند.
🔹
یکی از کارکنان پایگاه هوایی بوشهر در حمله تروریستی آمریکا به شهادت رسید.
🔹
روزنامه فرانسوی لوموند: امارات مخفیانه در سومالی‌لند برای آمریکا و اسرائیل پایگاه نظامی می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668564" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WETvRAOkOMxIbdeUo2_lS5etG-XV_T64GsFPScy4KyUp3-Q1BHYnV2oiuTPqQeEhNIQVLKkhyjdxOMo8dOQygK2qFO2toqUn7V52UJ_fCZNbghHXLts0hjdeNT4lEpvsLLVbtH3yQ_FyjvfvUdZYmxEtAvK-Ceub05BzDS6wmQWQ6NVAyf2rW5jtDSTIRK9ZeneUSaBfs7MxUhC2ILI7aEtyMqH0AaJmkVHOdlCu32oz_JBmk4cjeuvXuaLZWk2mcsMKmSFB1Rvskp0rBYo-t29BN1GdE35BmDZwB1Wjl1fIWpUrsEvPC54UDq1RCJs6BtWCLTC5QCk1JunI6EJ4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس شورای سیاست‌گذاری ائمه جمعه: از این پس، نمازهای جمعه «خونخواهی و انتقام» اقامه خواهد شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668563" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ایران «قطعاً» دارای تسلیحات شیمیایی است
!
نتانیاهو مدعی شد:
🔹
ایران در استفاده از سلاح‌‌های کشتارجمعی هیچ ابایی نخواهد داشت!
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668561" target="_blank">📅 18:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهر غزه
🔹
رسانه‌های خبری از حمله هوایی رژیم صهیونیستی به خیابان «الجامعات» در غرب شهر غزه خبر دادند.
🔹
تا این لحظه جزئیات بیشتری درباره میزان خسارات یا تلفات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668560" target="_blank">📅 18:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maa3iuBlSKAgrlDnRwm9MO3EwZFRWjoE52999GKkvuF6AznHcw9IGIOlxcHTzAE-3BMCFK-p7frWZFMm3SkgVcroaPbvfxs3phe56GAKGPAYHnnklQo3djb4YVZIbasUSSJe987YKTqxaSzPMil5GIQdlN8BwjBGYSrey53-JhHRgLujtb4MY9eUVcnPgu5JfzGRfMEKyZJOemXclNHtlrFhP0iGtn_mQf4A8v3OG5jSiW9CV8EBRw0Wdz-DCq9TPJTzTuAlucy9LN7VwHqryFefWEQnm6TEdguk-puQgIJB1-5NKGFVnNxJVkFSYVwWUe2t0fBo_0YSpC__PApfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزند ارشد رهبر آزادگان جهان در کنار فرزندان آیت‌الله سیستانی در انتظار رسیدن پیکر مطهر رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668559" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rmgure5C8UolSGikSXspjHOv9cXmobg4XPVYqO8EZep092iCOr88-SP68jloe3YFH3nB1IdE6DR3CPxJqffWGmVugyUHMAuHQWaPy1JDw0Dke85Gq2T5ODrFb_8G1h8nnACFbhFkldPqfcxIJE3b2-jRxNuuD9v4q9tQCKZ9CZ1do5jsNnrZAwkI7R2yA6LUNRBDSk50FJW-ubJ1mgJ7_QMiZROlAyMWfLmIicgIzhKVnD3CkvrTajfJqOMaEa8vux1bUpJdZ33Cok9Rg_P5qAecFqgh4VCmN5PrrwwM-PmBjQuuMnqz9LMvJBsSk85YWXsO3oydoKdXHIAa3kcv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به مرز ۸۰ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668558" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سی‌ان‌ان: توقف عملی تردد نفتکش‌ها در تنگه هرمز
سی‌ان‌ان به نقل از مؤسسه «ریستاد انرژی»:
🔹
تردد نفتکش‌ها در تنگه هرمز عملاً متوقف شده است؛ بر اساس داده‌های شرکت «کپلر»، امروز تنها ۴ نفتکش از این مسیر عبور کرده‌اند که این روند هم‌زمان با ابهامات پیرامون تداوم آتش‌بس ایران و آمریکا رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668557" target="_blank">📅 18:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdc8e6ccb.mp4?token=bRybzropB3b14lEHiX_bnnpn9weA9cHDc45D0XoSNMRY93yoHFP_Z8GdVYa5nYpPbxO9bLR0Yxa0wglRrDVQjF42LRgnp5zkwI0HJdzAwPBgscVkSw4K41rZf0B7KTnJ5Y_YMQns0XybdouDKkIncXkgngpqGMVtc9I2DWszOxOBn8yLM845riGoeEPsdzFqPOihsmj5qdGiGmFe4X78h62OZsc5Aa3UgHF5XAVWIFEaFMZmQYOvBzp5jOcfSoBrDDAMqEOnLxLPt9PHqTn_81mGoGM05K833VB7weN7USJ8OPM5zcsU9reUoHdvcHu3n39mGLIuQWv91nhZEQljXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdc8e6ccb.mp4?token=bRybzropB3b14lEHiX_bnnpn9weA9cHDc45D0XoSNMRY93yoHFP_Z8GdVYa5nYpPbxO9bLR0Yxa0wglRrDVQjF42LRgnp5zkwI0HJdzAwPBgscVkSw4K41rZf0B7KTnJ5Y_YMQns0XybdouDKkIncXkgngpqGMVtc9I2DWszOxOBn8yLM845riGoeEPsdzFqPOihsmj5qdGiGmFe4X78h62OZsc5Aa3UgHF5XAVWIFEaFMZmQYOvBzp5jOcfSoBrDDAMqEOnLxLPt9PHqTn_81mGoGM05K833VB7weN7USJ8OPM5zcsU9reUoHdvcHu3n39mGLIuQWv91nhZEQljXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید در مسیر پیاده‌روی اربعین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668556" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Zl4Z8s4-iBISZ-PPcHJZ7zqAHKC6lXueR9X2kpMw8gnrlarTZbwA0PT2QqyMjyjpjmSYfCEhZVuzmJRebY_XFlI6glqd4zHpASHhNEVLMk9WZA_B28suKsM_Yp4-SLTAotKCk0_iOzYKRitqnGNhVIfODhVee2wKzJJiMIzHfUFmJuxG92jytLRLRWNYErLswDI619p5YdjlY5JG2Q8vius4QWP9Dof6tyGpQBnRLzYkS98aYDb5cfU3DS9laga9bqZ-fO6hB86LkWF9ayNOlJgnn5acH2WPFno1KwaQUg4P9dyfKNKJuMx6I9ovKgGtUZs_FWvh4AcZSKTaVdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان  ادارۀ فرودگاه‌های پاکستان:
🔹
این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668555" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e7da8d03.mp4?token=GhSTC5aVHW--JZpBR2_XP-lO1qMeJ9N30DlOSyzVmZxOB-3Tcy-AS4P_YKhme6LSMLgh3GJXfpQsDfxtSwrp_mV3NsgTpbUdZIzTdh3BNMXONvej2_hXNfS8j3Io5dqMFirw25moAVToFx9QoZed0JhqC_hMWvk2wmcLK6y7JxVUZsaGdqhJXxY9EPW7aYcwTRXjFOjsEI6rWBpBTJfRlS6R52XdTWMl3ORKKHf_B-VBnbmUAf25R9nFm085_Ui4pfmHCyKed8zVvp9mZHyTCGkUBTrSazmpDQ_QaxTW2I54Fj01ulCNlN28up464ImQaLN0X8-i1eMrQLLf9s1Esw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e7da8d03.mp4?token=GhSTC5aVHW--JZpBR2_XP-lO1qMeJ9N30DlOSyzVmZxOB-3Tcy-AS4P_YKhme6LSMLgh3GJXfpQsDfxtSwrp_mV3NsgTpbUdZIzTdh3BNMXONvej2_hXNfS8j3Io5dqMFirw25moAVToFx9QoZed0JhqC_hMWvk2wmcLK6y7JxVUZsaGdqhJXxY9EPW7aYcwTRXjFOjsEI6rWBpBTJfRlS6R52XdTWMl3ORKKHf_B-VBnbmUAf25R9nFm085_Ui4pfmHCyKed8zVvp9mZHyTCGkUBTrSazmpDQ_QaxTW2I54Fj01ulCNlN28up464ImQaLN0X8-i1eMrQLLf9s1Esw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668554" target="_blank">📅 18:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تعریف و تمجید خوک هار از الشرع
🔹
رئیس جمهور دولت تروریستی آمریکا در دیدار با احمد الشرع، رئیس دولت موقت سوریه گفت: او آدم استواری است. او رهبر بزرگی است.همه به او احترام می‌گذارند، از جمله من.
🔹
به داشتن او در کنار خود افتخار می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668553" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328871d827.mp4?token=J64WH8N3FtfHQ5bb_nqPXBDA7j0mcKtu8QD3FKOdYLdn3GhRQA_rAC24-U6HeGoxWWD1UlBCwnnOww1Gi6XR6kgwpruwcvzpwyfC80rwqbVIV92S_JK9lDDf8pN98nRchd_jlJpwlnr76x3wCk19WNVTmsqGo6ha6YtQFBAib10ucY215N1q43lJG4pxH6haLyU2AHmuTLFNoc8nYfRdS8dcGNPwXMlcRoJwhBkqvf6EVWkdHcHmiUxCDthSuFTGuBJChQIeTQfppHhlL_HXXnYLkBw48el_QR0sdDvg1snR6A1vVUIbEKrjnzSqSbeumf3Uwwy0szK_xpNO4FcblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328871d827.mp4?token=J64WH8N3FtfHQ5bb_nqPXBDA7j0mcKtu8QD3FKOdYLdn3GhRQA_rAC24-U6HeGoxWWD1UlBCwnnOww1Gi6XR6kgwpruwcvzpwyfC80rwqbVIV92S_JK9lDDf8pN98nRchd_jlJpwlnr76x3wCk19WNVTmsqGo6ha6YtQFBAib10ucY215N1q43lJG4pxH6haLyU2AHmuTLFNoc8nYfRdS8dcGNPwXMlcRoJwhBkqvf6EVWkdHcHmiUxCDthSuFTGuBJChQIeTQfppHhlL_HXXnYLkBw48el_QR0sdDvg1snR6A1vVUIbEKrjnzSqSbeumf3Uwwy0szK_xpNO4FcblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای انتقام، ‌قدرت تو را می‌خواهیم یا مولا؛ خون در برابر خون
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668552" target="_blank">📅 18:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2p_jhttze3YMAdT8yy8pBYKb_Hgv0KFjCQnmXZmwLMIUWHHsohg96vCW5-4DV31FEUs4FUpyUp93UhK8u8rSBb7d6B4mkCoQb6xTEiWg5Qz0HOtddawPu2L7Yig3hESiMTnHzrkF7aiL_rYSw8-C6N9BHm_z-9QjwH2qdx95nywSgQOVQWbKTBBcXTuzl-wtpI_fYmmZxPWqJE-tVl2KYPxf3NCRpexv8wMkLBJJbTEXdSVBecedWoDJGIxQi_-3Cg2dHPSCSXrqltKo6wX_4NgBfpyyHRzwUTHoIjIT2mLWr06oa2_UCqI2Dz_18sozMp1Q_PtqS1VITXqP4uR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر رهبر شیعیان جهان در دست نظامیان عراقی‌
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668551" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
خروج پیکر ابرمرد تاریخ ایران از فرودگاه نجف پس از مراسم کربلا
🔹
مدیریت فرودگاه بین‌المللی نجف اعلام کرد پیکر رهبر مسلمانان جهان، عصر امروز و پس از پایان مراسم تشییع در کربلا، از این فرودگاه منتقل خواهد شد./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668550" target="_blank">📅 18:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e731519fe9.mp4?token=M5HY7xmhtPkZm2km1lzROsaqNAB8JqB1NB0nltscX-7O1z4nFWIKlX5_d37oulwOTSDwIlodw4B1pr13ePT2kDU6b1o5FDrqnx2-IK7GP4mtQBegtQuW-2_sT5Fz5abpGzuhckTgsTX2Myf2Cf-bh40mteCMvRYeqvKCG7iCKK1rZxiya3o6xqPWJ0xQqc_elQbOAHlggNOY8mECO7Li1l0I3R4GzPTv3vZAz4Ixk4vTe1bt9mJ2nlgU7p3XQjyVATmLh9GvPbqfRLiTsNN6LyOMJZ_6OeYYJtvQRaC6nxBB4xWnwxc5lnaK-Bo1nyzaN4_K-O-usIjWV1hGazM3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e731519fe9.mp4?token=M5HY7xmhtPkZm2km1lzROsaqNAB8JqB1NB0nltscX-7O1z4nFWIKlX5_d37oulwOTSDwIlodw4B1pr13ePT2kDU6b1o5FDrqnx2-IK7GP4mtQBegtQuW-2_sT5Fz5abpGzuhckTgsTX2Myf2Cf-bh40mteCMvRYeqvKCG7iCKK1rZxiya3o6xqPWJ0xQqc_elQbOAHlggNOY8mECO7Li1l0I3R4GzPTv3vZAz4Ixk4vTe1bt9mJ2nlgU7p3XQjyVATmLh9GvPbqfRLiTsNN6LyOMJZ_6OeYYJtvQRaC6nxBB4xWnwxc5lnaK-Bo1nyzaN4_K-O-usIjWV1hGazM3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعریف و تمجید خوک هار از الشرع
🔹
رئیس جمهور دولت تروریستی آمریکا در دیدار با احمد الشرع، رئیس دولت موقت سوریه گفت: او آدم استواری است. او رهبر بزرگی است.همه به او احترام می‌گذارند، از جمله من.
🔹
به داشتن او در کنار خود افتخار می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668549" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aed159197.mp4?token=He_Rdki0_N42tkHMjo8rtp-hbh1aGqPigJG6Ztrrib2csyxw78GvlzSMhTXZhfhxE6y9HPzpvTvvWa95Yy3oxCflXVf3ezCC9IsCtjT8yshv3VUNJRoSjhcHr7NILXIeByrIsu5d9L_lZ3c9434cJuobwHU2FyXU4IWS-3zzDYIEoqwuCjATCkmNF5G8TES0WUlY2S4ZNS8UN-MA0-WiudferZKzIJhwXmDNA2N4gma_foz1SfA9K129G5MOXUS8Q5nm-js8X3Ne3bduSJjFwV7nNyhP2S2fyJc65IQvxNuEBgbJuT39ci7AUqls4KBHsac1f8vD9_rcxc62KwnIpLneAIb50CWlLfRWJwQRQ7IqSQC-coVaghDTcNkmRu3tOgh3Qt6enF92jBzKrKatCqGFL4TY-UJsuRst1UwYJY0sEXpAAxCxBMyLtHABy6btruHy09V47jyfUR-4K7g5cvEKUrgBazt-qowy78UFNedILaXR5UmiuBSzVO_oBAM3oZLxtmJMDa9dUbtnRTE5yVOHCtRIuTuBxwwyU4Jq6fR7UPIWYmApAmjlbc7zzJG9Q04_XAlidlCZcu_sv7g1xZbMYkPosn3GDk6FjjvLCoxEUvBF01PxIGLPfWGX5HDwsK-CI9usBkm1YzxaJmRaGXcEnaJh3p7YyF1cbvBPUUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aed159197.mp4?token=He_Rdki0_N42tkHMjo8rtp-hbh1aGqPigJG6Ztrrib2csyxw78GvlzSMhTXZhfhxE6y9HPzpvTvvWa95Yy3oxCflXVf3ezCC9IsCtjT8yshv3VUNJRoSjhcHr7NILXIeByrIsu5d9L_lZ3c9434cJuobwHU2FyXU4IWS-3zzDYIEoqwuCjATCkmNF5G8TES0WUlY2S4ZNS8UN-MA0-WiudferZKzIJhwXmDNA2N4gma_foz1SfA9K129G5MOXUS8Q5nm-js8X3Ne3bduSJjFwV7nNyhP2S2fyJc65IQvxNuEBgbJuT39ci7AUqls4KBHsac1f8vD9_rcxc62KwnIpLneAIb50CWlLfRWJwQRQ7IqSQC-coVaghDTcNkmRu3tOgh3Qt6enF92jBzKrKatCqGFL4TY-UJsuRst1UwYJY0sEXpAAxCxBMyLtHABy6btruHy09V47jyfUR-4K7g5cvEKUrgBazt-qowy78UFNedILaXR5UmiuBSzVO_oBAM3oZLxtmJMDa9dUbtnRTE5yVOHCtRIuTuBxwwyU4Jq6fR7UPIWYmApAmjlbc7zzJG9Q04_XAlidlCZcu_sv7g1xZbMYkPosn3GDk6FjjvLCoxEUvBF01PxIGLPfWGX5HDwsK-CI9usBkm1YzxaJmRaGXcEnaJh3p7YyF1cbvBPUUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های فرمانده ارشد عراقی در مراسم تشییع پیکر رهبر مسلمانان جهان
🔹
«ابو حسام السهلاني» فرمانده عملیات شمال و شرق دجله در مراسم تشییع پیکر رهبر شهید انقلاب در نجف در کنار جمعیت میلیونی مردم عراق به عزاداری پرداخت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668548" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">🌺
گاهی خداوند رسالت‌های بزرگ را به دل‌هایی می‌سپارد که رنج را شناخته‌اند و با امید زندگی را معنا کرده‌اند.
🔅
امروز پهلوان عرفان ناصری را به‌عنوان
سفیر افتخاری انرژی و برق معرفی می‌کنیم؛
جوانی که با وجود بیماری خاص، هرگز در برابر سختی‌ها تسلیم نشد و ثابت کرد اراده، از هر محدودیتی قدرتمندتر است.
🏆
عرفان تنها یک سفیر نیست؛ او نماد امید، استقامت و مسئولیت‌ پذیری در قبال آیند سرزمین ماست.
🇮🇷
در روزگاری که منابع انرژی و سرمایه‌های طبیعی کشور عزیزمان نیازمند مراقبت و مدیریت آگاهانه هستند، مسئولیت همه ماست که در صیانت از منابع سرزمینی، مصرف درست انرژی و حفظ ثروت‌های ملی سهم خود را ایفا کنیم.
#عرفان_ناصری
#همدلی_جادوی_توانستن
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668547" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngfXAWA8OHAByhn3BvZ-RL0oOCy6-qVpAtp-9el-B-Scyc4YBEOQAp1MiRrZa0lneJkOYmO9sCJ4hj7ch6c_hDcbIqx5y5cZ6n6EA89u8mP11KCuvaNnSMxMUk9gETC2XJheMESzeax-bP3zkepYSbceRM8OdMlQ0Jn24DvEkLE0bDR5UULSGbuwwA48qM1r7oFf7SlZRzVfhpmh1tgaCZKd5uOXXpJAbp_yk6RMvp2mLt9Po_P-8xzFLza2pKlVA3C01p05g65vBZjGHz30WC7_eYCVdIap_dGXubk-veLuG8R1jZcDididRfaZ3IjzSmVzzaBTWWbclxx70fmiuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚻
مشهد به ۱۴ کانکس سرویس بهداشتی سیار جدید مجهز شد
در آستانه برگزاری مراسم تشییع رهبر شهید انقلاب، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد با خرید و استقرار ۱۴ کانکس سرویس بهداشتی سیار با ظرفیت ۷۳ چشمه، زیرساخت‌های رفاهی شهر را برای خدمت‌رسانی بهتر به زائران و مجاوران تقویت کرد.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668546" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=WxdceFCrhykzCRO3GA2MQaD9z6POF28-mJ4D2c-EoqaUbecJdX_fDhCUJql8l_1O8_UZzAWTh-m8alNS6AaZNQ67GKW_Nwkxq23_J23CQ6ueAlFo2eh-x47ZnK15Xb228F47IUu_JsaYA0k3BpFy9w6DgLC_SZoNH6n-sDAvHyhIUrkqLfhkS8zHq8lbj46o_4uAWHZHDxOPfe6C8hQsSHIv3ewzDh7UDzG_t7FwVJpdL43-N7wsSQTYCkgjD7dKxt0Dmi59ysNRmLLbXAwgrXBNqHSBQ49TWfqYBDOsr9god9QvegnBZveT6hutZidOnMJhualZj8phjtQVx0qRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=WxdceFCrhykzCRO3GA2MQaD9z6POF28-mJ4D2c-EoqaUbecJdX_fDhCUJql8l_1O8_UZzAWTh-m8alNS6AaZNQ67GKW_Nwkxq23_J23CQ6ueAlFo2eh-x47ZnK15Xb228F47IUu_JsaYA0k3BpFy9w6DgLC_SZoNH6n-sDAvHyhIUrkqLfhkS8zHq8lbj46o_4uAWHZHDxOPfe6C8hQsSHIv3ewzDh7UDzG_t7FwVJpdL43-N7wsSQTYCkgjD7dKxt0Dmi59ysNRmLLbXAwgrXBNqHSBQ49TWfqYBDOsr9god9QvegnBZveT6hutZidOnMJhualZj8phjtQVx0qRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر شهید لاریجانی در دست عراقی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668545" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
باید برخاست؛ نه فقط یک شعار، بلکه عهدی برای ساختن ایران
🔹
امروز، در میان پرچم‌های «باید برخاست»، خانواده بزرگ صنعت، معدن و تجارت در کنار مردم، پیمان دوباره‌ای بست؛ پیمان خدمت، پیمان تولید و پیمان ساختن ایران.
#باید_برخاست
🇮🇷
برای ایران؛ برای تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668544" target="_blank">📅 17:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=ZPa9BqD2cp9FY5f8M3ccFRwm03VVAUWPwBt7OJTCqjmk8_NMZsggaEx9ORhODNGAAjfT5KOR5bjtgI_MAaYgpSi-0fNwcOM6VV7paBR7-8lyTuXxTeycGaMrga3cHGXUDgtQKQXqKZuDXtCeIS8JJijU8688vXz25edPV9QWX7WD2XLbC5gIR2ZtSt1C1PyALR70Aqy17uqZ0be9pt-4Rb5UgVW8jOHUAfJYWLwWCkAIWn6BOUUjUesRQGGuwqA6splldopIKWTHCR_U9uABIYdJgHbjQ7lnXjJUuteBYE3PNblb4emeN8a-7NpAnbpx08W_sCm9ypfmc2dVFrsvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=ZPa9BqD2cp9FY5f8M3ccFRwm03VVAUWPwBt7OJTCqjmk8_NMZsggaEx9ORhODNGAAjfT5KOR5bjtgI_MAaYgpSi-0fNwcOM6VV7paBR7-8lyTuXxTeycGaMrga3cHGXUDgtQKQXqKZuDXtCeIS8JJijU8688vXz25edPV9QWX7WD2XLbC5gIR2ZtSt1C1PyALR70Aqy17uqZ0be9pt-4Rb5UgVW8jOHUAfJYWLwWCkAIWn6BOUUjUesRQGGuwqA6splldopIKWTHCR_U9uABIYdJgHbjQ7lnXjJUuteBYE3PNblb4emeN8a-7NpAnbpx08W_sCm9ypfmc2dVFrsvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته‌شدن پرچم «یا لثارات الخامنه‌ای» در کربلا
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668543" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حاجی‌دلیگانی: مردم ایران برای سر ترامپ ۱۰۰ میلیون دلار جایزه تعیین کردند
حسین‌علی حاجی‌دلیگانی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برای تأمین هزینه‌های خونخواهی رهبر شهید در عرصه بین‌الملل و پوشش رسانه‌ای نیازی به بودجه دولتی نیست و مردم هزینه‌های آن را تقبل کرده‌اند.
🔹
مردم ایران برای سر ترامپ یکصد میلیون دلار جایزه تعیین کرده‌اند تا هر کسی او را به سزای اعمالش برساند این مبلغ را دریافت کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668541" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🥀
فهرستی از بهترین نماهنگ‌های منتشر شده در کانال قرار مداحی برای
#رهبر_شهید
▫️
جهت دسترسی به هر یک از مطالب زیر، روی اسم مداحی (آبی‌رنگ) کلیک کنید.
داغت
ستوده
مشت
بیوکافی
امام شهید
نریمانی
خبر دروغه
رضا‌قلی
یاران رفتند
کریمی
دیدم که جانم
رسولی
امام قبیله
لیثی
امر فقط
نریمانی
مرد خدا
بنی فاطمه
اللهم لا نعلم
پویانفر
کشور دوست
خالقی
وارث خمینی
پیرایش
رهبر شهید
بیوکافی
کجایی
رمضانی
آقای من
خلجی
شهادت نامه
سلحشور
خداحافظ
طاهری
نامه ای از آقا
رسولی
امام امت
رسولی
یا لثارات القائد
بیوکافی
عزیز ایران
اسداللهی
یکی بهم بگه دروغه
رسولی
خداحافظ ای مهربان
مطیعی
روز دهم
نریمانی
بأمان الله
طاهری
زاهد در دنیا
ستوده
راحت بخواب
رمضانی
رهبر من
عباسی
ای مقتدر مظلوم
قدمی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668540" target="_blank">📅 17:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae4c6fbc6.mp4?token=iZYj3Ho077XKbVh1dZZqk6drr3v4IKTRWOOkOGzB2_eIKUnLIGzkLMkZDxeIigdX9853kAtxCj_d13MuQolzIvmthmuZyND_KbzsZWbC9S6EDXTKFhNNUrkVNQBRsD-Sf380VBDdtgB6skyXtnxbROIX3ditnfsyjqFzOcY-hlBXa6dwac0_RvlyNuYATWhKr8fTBSlIOtuN6DnBAmrx89AXTjgokhhBq7JTxJBcm17JuQC75cDuJa0-1imHcrns3YVQ5rhDZBEmC2XSULotIJnvV3LzseVgondgOFsTMo6HYMpYupZUuO7h0jwB6VPp6hDJjlvMdvt3yOvCqIsnlwR3RrExNqvZmIRfz4N38-Ohy1fBqaPo-w_l21cZyEDpY-78rxoL0dFHtje0EvJj_2eMCN1n5E_Fdj7FoDZNOld21rnvfBrL5ZqYniqgaxJVJv5Jzv5m2pJTeWtrJ00HJdhz3V95USllvcG63oiiymt3sBoy6UNbrwc0FgdhghEi-QJAIdWx_KzBA0CFwJiN7UTPUx0V0eBm7VzFyhaevN04Ll0wZKdePWPpPT-txTHssdVXYau2DbwDroyRE4--DV9LE8Gwfy5yfvPYo2wkvIzUFKvmBVjzp1I-lzorHLm696CG_NxDb7WdDgF767pnJemzfhkpr3gxkmCmrdSBs6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae4c6fbc6.mp4?token=iZYj3Ho077XKbVh1dZZqk6drr3v4IKTRWOOkOGzB2_eIKUnLIGzkLMkZDxeIigdX9853kAtxCj_d13MuQolzIvmthmuZyND_KbzsZWbC9S6EDXTKFhNNUrkVNQBRsD-Sf380VBDdtgB6skyXtnxbROIX3ditnfsyjqFzOcY-hlBXa6dwac0_RvlyNuYATWhKr8fTBSlIOtuN6DnBAmrx89AXTjgokhhBq7JTxJBcm17JuQC75cDuJa0-1imHcrns3YVQ5rhDZBEmC2XSULotIJnvV3LzseVgondgOFsTMo6HYMpYupZUuO7h0jwB6VPp6hDJjlvMdvt3yOvCqIsnlwR3RrExNqvZmIRfz4N38-Ohy1fBqaPo-w_l21cZyEDpY-78rxoL0dFHtje0EvJj_2eMCN1n5E_Fdj7FoDZNOld21rnvfBrL5ZqYniqgaxJVJv5Jzv5m2pJTeWtrJ00HJdhz3V95USllvcG63oiiymt3sBoy6UNbrwc0FgdhghEi-QJAIdWx_KzBA0CFwJiN7UTPUx0V0eBm7VzFyhaevN04Ll0wZKdePWPpPT-txTHssdVXYau2DbwDroyRE4--DV9LE8Gwfy5yfvPYo2wkvIzUFKvmBVjzp1I-lzorHLm696CG_NxDb7WdDgF767pnJemzfhkpr3gxkmCmrdSBs6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری زنان عراقی برای زهرای ۱۴ ماهه شهید جنایت ترامپ قاتل؛ هنگامی که پیکر او وارد حرم سیدالشهدا می‌شود
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668539" target="_blank">📅 17:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
استقلال و تراکتور در لیگ نخبگان؛ گل‌گهر در لیگ قهرمانان آسیا ۲
🔹
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا ۲ شرکت می‌کنند. #ورزشی
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668538" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
استقبال شیوخ و سران قبائل عراقی از پیکر رهبر شهید انقلاب با بیرق‌
🔹
سران و شیوخ قبائل عراقی بر اساس رسمی که بیانگر احترام و تکریم است، با بیرق‌ قبیله‌های خود در انتظار ورود پیکر رهبر شهید انقلاب به کربلا هستند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668537" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: «امشب، اگر لازم باشد، به دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، چون این بهای کارشان است.»/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668536" target="_blank">📅 17:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تعطیلی فرودگاه هرمزگان تکذیب شد
.
🔹
الحشد الشعبی: تعداد تشییع‌کنندگان قائد شهید در نجف تقریبا به ۳.۸ میلیون نفر رسید.
🔹
دبیرکل آیمو خواستار خویشتنداری و کاهش تنش در تنگه هرمز شد.
🔹
سفیر چین در ایران: پکن از بازگشت وضعیت تنگه هرمز به شرایط عادی حمایت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668535" target="_blank">📅 17:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG2i353WD1rSs5bNSwjjDe5yi0fNa5XNWszwdqZ8X1N2ydeWjDuAdnoOkGRJzPpg2H1pASyi_VmuK5V02JhGzgqQBEvXZbKvesOLSbKEGDuZE3y1PCKtO670RLkkVv0pWb3TGnx4TsWBp1vam4a_iVMqLjRu_qPlg49cNfiQxCsn9ha600aJ9L_JjUBgp4Hh7sfGKvbL3JJz0B2dAtW4mXYh7FW2_Z9S7DnprOS2w7tXOE0XyP4rPdfNm9-dHbB9ZCjKrlv4_y4t3OV_XC0Zs8IdmFyrik3oUGFypvudDA7TUh2lHyX3JUyEjTHuZafDOpP-cdOzE1sCrVMYXPxcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPTNJossDYgtOrY0kF7NsJwQtsAX8NcZjlyXYHaNeQAVcq2XuRy0PYfFVgoG0BRVK0WxyjTccSk6VgRE3qFW7rvmkLjsVCUoUW3ENu5lx2ZQsibxDzZI3Kr_p6veHy_CtQHom4sWJbVewiJqo7U6LDj3kJT9vN14fR8W1hTDnZXZkpA1IwdzXq1B5ytMUepOQh6uKBoRHcPxhhuXC-pwTXaOE5eCO53xPaEzfPLxqT_eZTPobLssciYlh-cfck-u7gBekgpblXxF4dk6pFJmg_l1dl-c1vA0oOuemKDAzAKmn2Bj4mMOGJzNRMJ5ii_lB2ZdlwueMYFpXSR2-uPEgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران، چهارمین کشور جهان در ثبت میراث ناملموس یونسکو
🔹
ایران با ثبت ۲۷ اثر میراث فرهنگی ناملموس در فهرست یونسکو، در رتبه چهارم جهان پس از چین، ترکیه و فرانسه قرار دارد.
🔹
از مهم‌ترین میراث ثبت‌شده ایران می‌توان به یلدا، آیین‌ تعزیه، هنر میناکاری، ردیف موسیقی ایرانی و بازی چوگان اشاره کرد.
🔹
فهرست میراث ناملموس یونسکو شامل سنت‌ها، هنرها و آیین‌هایی است که نسل‌به‌نسل منتقل شده و بخشی از هویت فرهنگی جوامع را شکل می‌دهند.
@amarfact</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668533" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c24bf90e2.mp4?token=WsIMkTQJNM3JPn5WkMjjCVaqeVDSKYWodndK99VL8o6ACIcbKrdWr6FhJ1CV6-Ks_0v4qNmxoTfSKWhT9G6TF2RtkI7RFDnAv4qc9ALHSkT_IJr0FfryedMtUiJ8LSAAqPVucs6t3SjdO8COy7oG26qcE111MlsDh36RlmVASn1x5zNqhvibDKjXOM5-6K4u9MMwjOP1fQebC7zGHA48knjuUrHn3Kc4DTGL088FbdEidiQaDhxHQ8UXcqv_vtoMBcN1uc4LgqxrZ8QvuKgg3iL4P-1HeLzBe4FamYL-CrXvIwGBIKnIb5z8HxHFksrm8J7rLpCFQ1i0O7UcqQBLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c24bf90e2.mp4?token=WsIMkTQJNM3JPn5WkMjjCVaqeVDSKYWodndK99VL8o6ACIcbKrdWr6FhJ1CV6-Ks_0v4qNmxoTfSKWhT9G6TF2RtkI7RFDnAv4qc9ALHSkT_IJr0FfryedMtUiJ8LSAAqPVucs6t3SjdO8COy7oG26qcE111MlsDh36RlmVASn1x5zNqhvibDKjXOM5-6K4u9MMwjOP1fQebC7zGHA48knjuUrHn3Kc4DTGL088FbdEidiQaDhxHQ8UXcqv_vtoMBcN1uc4LgqxrZ8QvuKgg3iL4P-1HeLzBe4FamYL-CrXvIwGBIKnIb5z8HxHFksrm8J7rLpCFQ1i0O7UcqQBLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت نویسنده لبنانی از استقبال عراقی‌ها از پیکر رهبر مسلمانان جهان؛ بیعت با مکتب علوی و حسینی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668532" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeLJ-RcOK02jz0CoQYcUd9iJYlhLzo0UGcJns4pmi-0IikmbIF8SSNfPQaodtBrRgG7R9GXicLkJeF9UJGkeKgquZqFDyw3ygWCLv9TpdtxB78MgCjC4M8JWSWazRVk6uttNai6Lt5FMJVddliXdQzboiYChO0R42207BhSMwfzpvXgtIOhhVaHq2w-MJOLvO82-V0oaJjc9BcNL2rvXVSpXLETQz999iluWF7fC-4xWe1ZeHFlY1BAqCZU_SnYSOHS_v3mQv4zk3n8I_jAlrCOFnFAavaY6Gf6-QZrFa5_hlHpDClBibiM5OQIa4vQqdE6YNdSpwrSAwqiiVWjoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کودکان میناب در بین‌الحرمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668531" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602e87144.mp4?token=dvGezUEwYCMjV4JNMWqHKEBPVsnUzmTKCDylTT05WMXtk34u0T7p2nRxC3jr5DvyJkPPjaXucAlTt9m52hT2gFL6KDSUbTLVfoPYCn0mLG9_eZfqujTfIq92QK4yXcPOrUH_ZCnsFTQmyas5_cHFlVqYQBl2V4iLGdiPjqAotBKoWXUJ1YmRswoSTAkOkrMhx8462CH6xR4L-xxH4gp64xqevreSUXNmW7i1bK72blWQwcdsqDPjow3AwCNL3fz4z1FtFSXTTUenFw8Xi12gQp0RH6-96iwzAVdBYuUYtDvLy1HJ388kB5-x-04zvLI8SSjDYnrWw7Z64PtSdqbrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602e87144.mp4?token=dvGezUEwYCMjV4JNMWqHKEBPVsnUzmTKCDylTT05WMXtk34u0T7p2nRxC3jr5DvyJkPPjaXucAlTt9m52hT2gFL6KDSUbTLVfoPYCn0mLG9_eZfqujTfIq92QK4yXcPOrUH_ZCnsFTQmyas5_cHFlVqYQBl2V4iLGdiPjqAotBKoWXUJ1YmRswoSTAkOkrMhx8462CH6xR4L-xxH4gp64xqevreSUXNmW7i1bK72blWQwcdsqDPjow3AwCNL3fz4z1FtFSXTTUenFw8Xi12gQp0RH6-96iwzAVdBYuUYtDvLy1HJ388kB5-x-04zvLI8SSjDYnrWw7Z64PtSdqbrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار: دیشب ۲۸ تا قایق [ایران] را منهدم کردیم؛ احتمالا امشب هم همین کار را بکنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668530" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سیره رهبر مسلمانان جهان به کتب درسی و دانشگاهی اضافه می‌شود
محسن موسوی‌زاده، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برنامه‌ریزی برای افزودن فرمایشات و سیره رهبر شهید به کتب درسی و دانشگاهی با هماهنگی وزارت آموزش و پرورش و وزارت علوم در دست اقدام است و مشابه وصیت‌نامه سیاسی امام خمینی که در کتب درسی تدریس می‌شد.
🔹
فرازهایی از تدابیر رهبر شهید در حوزه‌های آموزشی، اقتصادی، فرهنگی، سیاسی و نظامی در کتاب‌ها و مراکز علمی گنجانده می‌شود و جنگ دوازده روزه و رمضان با دو ابرقدرت ارزش تدریس در کتب درسی را دارند.
🔹
حضور میلیونی مردم در تشییع پیکر رهبر شهید در تهران، قم، عراق و مشهد نشان از پایمردی و ایستادگی ملت دارد و همه مسئولان باید راه ایشان را حفظ کرده و در تبعیت از رهبر انقلاب کوتاهی‌ها را جبران کنند.
@TV_Fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668529" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rN1FWXcrnApur-Kft_kOIiTzBLwTB3oLpb0MfqBstXy0y_MnmS5YF_Jcbs8hcDP30II6U-hLtqgzcSsdX5AMXNG32noBgl1WOj4UdX06m5ffZGU1hUHf1dXHaoQYTiRyKi9pprhK1zAY9TIP2LLG99vyyH0I8Ku75mpfVyCPlS2oP1lSbOvg2-kfzbHewb3T-TKc0TnouhNnSWDjvoTusvMW5lM-jpD5y-xbKQow2MKLqWYMQq0_UA8Z-r5x1az-JRllREHUGef9YSsEG9vQOIzFptLeQzTHeSeDPCYvRfRzEH8dskYRI3qUi-YbgjYRHnwDICXUgyI-XinbIVoedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/db2yBPvIKj2nt1sVfvT1AmkDaIAtFbWKSPFuXn5PDewXvyQiAyGa1Zwaxp-VVa0JT9DKB1sDalf-mMGCgR3r25-27x_cZG6Vjg3DtDk-dA3kzCh1Qh2ZRLjHJ3-_kzwPzm_kAaagCPMcywC97YGknUqd755o399rF8v0ll80_Nf4hOxxOsiIqzA7wfe4f_26RXLYjctkRfH2zZKLNzWhGrr1put8_MzGfrmeqYwKUQ7aaAnT1PbBtK6-hHp8Njsd0Lx9XxTilRftiyRZbtM7PRyP0PfJMQ8ehfPnFDZsH608djbc3Eu2W6UklL9V0romt4-e9xJbozospEH-KENzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qguLmgfDxEAR4nZQIHVZrYng9CRCe1RAxtFfjTTB-KVqas_2x0fJcGVtxCbCZtuDXtUP9Fh81hLNZqU2IvWtaZWSkVVSXgebI8hDERSFTb1H329_izvj2KSKjziFiUcoyEEYiP5vWSJX4ng_h2t1LKkbmj02wYXnQKkKKgIpj65gX77kfleFijVozpMG3pw769hieXdbpUrZJypXoascp1iuT4-kor-uQ3lxh_RsUGjWzByKxBUeiey85QK6IkfDgbGEA86zGWdCNI8CbY6ksxmr_sNo82Ep1JPj0gD6gS-HjOp7oVhY1hO9unlFlGIR7lU7rZy0Y63q1n0PRTBdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdvAef2CKnQLVwPFYK9auZdpYI0uFYXWT8HBZX0-82CR2rMqnqb3RGWJ33gPtiAueWK84BhXdyo_-psjkUVD6GL4o-Ox4WrC6arYiMAT88AiK8suyHWrmeYybrzTy7LZ6wXLpGo2Dp8ZV8oSqgykFAdCwPi4LEIPzu8sCT74QJficxW7J9XVB6H2yJYlAe2_RhO6mbnhLqWNknNgumhzlJ4x_TRnHTxgoplesU5oPtSLh5FsKra1ZQoD0VlAhcJS349i3xajrHPZrmVZtsHyxhtURLuD_X7OdgxWaJyfmuL8KrnqzeyJmkb0N6jw95Lpu5JhZ0hVHZzZ5gZTxAeQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d68zs4tIlobbqejVL0HaWagyO1R8vydFLUftHyEhqVGpfBIDT9bIMNtVqplz09edRN1Br2AYhcgkwEHdAMu7JCkuEQuIrHEsvOS_0hI0cWMEWmdrEy-xTTHziL8NVtG3LzCRJ-MfhjlT3MitByDJ9sNiruOTyH5jc6Eo3bCDoUJTPOCMoY_UVq6U6AF9iWMmUJ6Kn6sLy15y3ZXkPy8IDbbetoXUnHX-ECGQK_reF4ZjRLbPqkUHMPl3H3x2xLWwKDXqREsGTJdxeiuEF8Z8FrjNep4G-p5w4ZqfJIaiCKdpPpiF5ws6KDPOziDUBzAxXg7RUEexEuSwKT4j4Vb8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE7H9-GlWEUAlAW3c5EkGZ4U3OHyrvfHhgSvJNqXa-4wCWcId90mRIETkWBucpEfYVdu-eP00xB3t4ZPWzMFDfGZ69xrt-qs-y8uqYEChqcZkEsZisuqYJ-0eKFm9iQULw6MtGmtJoHux8NMbNbtZlN2sUQ5NLkw03oeQYuhoW6hn8NrDqX51J-HZerFSaSrZzopYfX3O70JSvxnZ7AIOVTvzZuRsQMCHV4YrZ9xrENIqBvHBtME7wkCiE9tRYza3QrrQicVYLF75sVHJzqXcBdoMPitrvs9DHqSVM2iD8hPrEy1DbgFVS_vauFLngH9HUMyfSeUi2IVXJMy8JQE-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین قاب از زیارت ابرمرد تاریخ ایران در حرم امیرالمؤمنین(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668523" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71800c2585.mp4?token=RZDjfyraZoHTywgUIi1ksX3d5xbjD2P4WqxmA_eydl-D-ogUJhQ68dHd2eHiFfJcHA9k7oFXnZNW4xa6OD63mKiH4rkrXDaefDv-pPectBEMOByyAFn3HaAzg9IFgt5Xgro9VlgYP9WmUWQY4t2NVSj_D5qXWUKUjeMH-opd3CPgs0MH_jvokyyDLG9Pc-ywnggxmXM37H6zbuyiRop8yAq1sy0F17TmDTKYMZxOjjXIqOL9Tpz94Qp9sK3jOFHqlkny4L5lQeTh-kfq5CccpKdZdYvHvF1tdUheivUKGYtLCbJaDS1ZQkRjSHk3CO9UhLqSi7Hlhm1BJnxqUVUuiA71wnaXeTEcO3U1744KsF5YUPJOiC1hVl5VjNaBTK-NTBpMqpE3O0pc3AHFzPoazdQxjIIBPIhFfyXmMdvDFME_tmeR5LVWBhnKbAQy1aR0xnXAtIFMos4AV-xG-yaBIn83VJ9VXS3cbOHrf4T2zDOIg0WdApWOT_aSTBM2eLZyvktg-9RING0-eVFC23Gpb5nkt9NfBxM9zHT1P8kp0MpZ4ld0DPo8to5sN8RDRl192rRG84TaAKJkxIx4Un28QwpS2HScd2tQ480tbAOvlo9gF0kCjc4oVGSQpV59On0J5rajyoYelQxnGntbcnaCDapvyZ9GDJfnh7-Wx4rdZO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71800c2585.mp4?token=RZDjfyraZoHTywgUIi1ksX3d5xbjD2P4WqxmA_eydl-D-ogUJhQ68dHd2eHiFfJcHA9k7oFXnZNW4xa6OD63mKiH4rkrXDaefDv-pPectBEMOByyAFn3HaAzg9IFgt5Xgro9VlgYP9WmUWQY4t2NVSj_D5qXWUKUjeMH-opd3CPgs0MH_jvokyyDLG9Pc-ywnggxmXM37H6zbuyiRop8yAq1sy0F17TmDTKYMZxOjjXIqOL9Tpz94Qp9sK3jOFHqlkny4L5lQeTh-kfq5CccpKdZdYvHvF1tdUheivUKGYtLCbJaDS1ZQkRjSHk3CO9UhLqSi7Hlhm1BJnxqUVUuiA71wnaXeTEcO3U1744KsF5YUPJOiC1hVl5VjNaBTK-NTBpMqpE3O0pc3AHFzPoazdQxjIIBPIhFfyXmMdvDFME_tmeR5LVWBhnKbAQy1aR0xnXAtIFMos4AV-xG-yaBIn83VJ9VXS3cbOHrf4T2zDOIg0WdApWOT_aSTBM2eLZyvktg-9RING0-eVFC23Gpb5nkt9NfBxM9zHT1P8kp0MpZ4ld0DPo8to5sN8RDRl192rRG84TaAKJkxIx4Un28QwpS2HScd2tQ480tbAOvlo9gF0kCjc4oVGSQpV59On0J5rajyoYelQxnGntbcnaCDapvyZ9GDJfnh7-Wx4rdZO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام عزاداران عراقی در بین‌الحرمین برای استقبال از پیکر مطهر رهبر آزادیخواهان
جهان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668522" target="_blank">📅 17:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668521">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
شیطان زرد: ممکن است محاصره را دوباره برقرار کنیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668521" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668519">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b630e7e6d.mov?token=OKxLu9J3yGJlYJyjiVnrUZbHoJ3RiPe6rPVL8zN0bFbLDZH-JXxxKvOUifBRr6HFKcUz8GgpogIu8QPR0m2rSY1NIyMGH7bOFHiL1yrfpQ4_n9RRwsoEnUHubkuXzkwwwUM38TlgIcRCanS2Pz4aq70XtMPDZ7Wvb9ipkzxY0i-ilfTxiAsRQUNXoOYbMfhlzprcZDoB7ULRErfyAHXp9ECYP2tnJmbaPucCy0pky5ekFpkw9csUaFHAzfI-3uwhh662TuBJav6IzbVeWMp1S-8iqFuB87gYmL-saGGstrdI5cmFuyRY9HjrRRnJ85UkEM4w225_nqWAERhPOa8eBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b630e7e6d.mov?token=OKxLu9J3yGJlYJyjiVnrUZbHoJ3RiPe6rPVL8zN0bFbLDZH-JXxxKvOUifBRr6HFKcUz8GgpogIu8QPR0m2rSY1NIyMGH7bOFHiL1yrfpQ4_n9RRwsoEnUHubkuXzkwwwUM38TlgIcRCanS2Pz4aq70XtMPDZ7Wvb9ipkzxY0i-ilfTxiAsRQUNXoOYbMfhlzprcZDoB7ULRErfyAHXp9ECYP2tnJmbaPucCy0pky5ekFpkw9csUaFHAzfI-3uwhh662TuBJav6IzbVeWMp1S-8iqFuB87gYmL-saGGstrdI5cmFuyRY9HjrRRnJ85UkEM4w225_nqWAERhPOa8eBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد عزاداران عراقی منتظر پیکر رهبر مسلمانان جهان در نزدیکی حرم امام حسین:
🔹
ای حسین، فرزندت خودش را (در برابر دشمن) پنهان نکرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668519" target="_blank">📅 17:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257bcd9e64.mp4?token=mOOjKS086KvY3dGvWkac7JRsBiC4GWHhMDaXm83bfAqkwDVUZofGOygYCz3SKNcZ5Gw0GKUxUyOSumyj_Yrtlx4ez5bH5Uyr89D_Mu81UODWGL-di8wHB155m1NVJMdM6RkZODvkDuZpKvWkq1IKwYiNipnqkulzuX0WJr-jDRBhF7d0ecgwA_rRUGWX4Q0CMswfMyMqIciN6EMIa9tJa4E-c3iYC60YOM9PnDaS5m7H7gCH1eWrb54-WSeZV1Kb_6kIoWvxuxz3zSH7QIwcjVakkBYJjnO7CDCH1QxdgzFQFr1dAK3CczyGVP5Rwk4sniH-3PRIxRGvYpY9vtL7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257bcd9e64.mp4?token=mOOjKS086KvY3dGvWkac7JRsBiC4GWHhMDaXm83bfAqkwDVUZofGOygYCz3SKNcZ5Gw0GKUxUyOSumyj_Yrtlx4ez5bH5Uyr89D_Mu81UODWGL-di8wHB155m1NVJMdM6RkZODvkDuZpKvWkq1IKwYiNipnqkulzuX0WJr-jDRBhF7d0ecgwA_rRUGWX4Q0CMswfMyMqIciN6EMIa9tJa4E-c3iYC60YOM9PnDaS5m7H7gCH1eWrb54-WSeZV1Kb_6kIoWvxuxz3zSH7QIwcjVakkBYJjnO7CDCH1QxdgzFQFr1dAK3CczyGVP5Rwk4sniH-3PRIxRGvYpY9vtL7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ممکن است محاصره را دوباره برقرار کنیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668518" target="_blank">📅 17:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=tU80WkTy5O4Es8hfC_wJwRkrmmj4sZUh0X-p3tl4VxrqsgJAAN6SPj1bviGTdDc9UiDXsruPsP1O7nhMy0h9mOa6q6LOFYUrOQtnhb54IZplHHcW3fOrzaT-mrcIEephM_B_2NcHMi1QWIIy8l2aO77_tesdRtK5M1XTU8aGKVxpQV07bpPWfyCYPRN6dzwlc_DzvudOfLMB6M0eNgPAXXuXqsvLaijwh8bwk6V-fr8bwijjzH5bZ0ZMdePSWkZTnXW4bltwL640RZdgQN_zeK1RoCPY1WQyxc5UfdxvWPUB1I2m9HAEaVVrdYkJidkl8VbHC4gkWS_lU2lN8nNZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=tU80WkTy5O4Es8hfC_wJwRkrmmj4sZUh0X-p3tl4VxrqsgJAAN6SPj1bviGTdDc9UiDXsruPsP1O7nhMy0h9mOa6q6LOFYUrOQtnhb54IZplHHcW3fOrzaT-mrcIEephM_B_2NcHMi1QWIIy8l2aO77_tesdRtK5M1XTU8aGKVxpQV07bpPWfyCYPRN6dzwlc_DzvudOfLMB6M0eNgPAXXuXqsvLaijwh8bwk6V-fr8bwijjzH5bZ0ZMdePSWkZTnXW4bltwL640RZdgQN_zeK1RoCPY1WQyxc5UfdxvWPUB1I2m9HAEaVVrdYkJidkl8VbHC4gkWS_lU2lN8nNZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: شاید جزیرهٔ خارگ را تصاحب کنیم؛ [ایرانی‌ها] هیچ کاری نمی‌توانند در برابرش انجام دهند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668517" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
شیطان زرد ایران را جمهوری اسلامی ژاپن خواند!  رئیس‌جمهور آمریکا: جمهوری اسلامی ژاپن ۱۱۱ تا موشک شلیک کرد. این موشک‌ها به سمت ناو هواپیمابر ما شلیک شده بودند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668516" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a339293d8.mp4?token=Ew_Rzd2i0L0jlqPBJ5IjkCiDob06MJTVAWaeDgLDSJgVOi54KCb-nKlmw8FNV0C2vIzk8sjkgZ1K-C-1s3v07hloFP5HcVWX8wuN1W0kmDBl8bnBoTdcOCHWsytGrlBDMBwD1URYN3MgUCu9wj4oqXB2uZIyJmDjQ8wDe1QLV7kKcj4bQoiOKiVwa7G5NzNkYEvT12DSieik4gLLxBHHbWo9TAV_f-5H1FE1zptPd8BIW0leIvk36ZMgk0mB6J8-2uGLVa8gnYQWGPiJSqZLPpY08wH52o0fSkZs8M-k6f8eoscd-6j3JdBU0DDgKzse2y3KYbPlAfz-Fn5JXLXf5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a339293d8.mp4?token=Ew_Rzd2i0L0jlqPBJ5IjkCiDob06MJTVAWaeDgLDSJgVOi54KCb-nKlmw8FNV0C2vIzk8sjkgZ1K-C-1s3v07hloFP5HcVWX8wuN1W0kmDBl8bnBoTdcOCHWsytGrlBDMBwD1URYN3MgUCu9wj4oqXB2uZIyJmDjQ8wDe1QLV7kKcj4bQoiOKiVwa7G5NzNkYEvT12DSieik4gLLxBHHbWo9TAV_f-5H1FE1zptPd8BIW0leIvk36ZMgk0mB6J8-2uGLVa8gnYQWGPiJSqZLPpY08wH52o0fSkZs8M-k6f8eoscd-6j3JdBU0DDgKzse2y3KYbPlAfz-Fn5JXLXf5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کاروان خودرویی و
ماشین حمل پیکر مطهر رهبر مسلمانان جهان در مسیر پیاده‌روی اربعین از نجف به کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668513" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مکرون: آنچه من می‌فهمم این است که نشست‌ها درباره ایران به عنوان بخشی از آتش‌بس ۶۰ روزه ادامه خواهند یافت.
🔹
هلند: آتش‌بس پایدار و ادامه مذاکرات ایران و آمریکا تنها راه دستیابی به صلح در جهان است.
🔹
جاده چالوس یک‌طرفه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668512" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbfTVNZAbtXyaUAa2adAB0eyY6n5eQddapIGSWdwGMxruANSuiKdkfHP8kfuULC0rXWHuu9uimHqEgukQ9TeL-oeVfkxPBHcqDWx3d1IthJ7ubwbBvdW2jm77f9kiNBnvh4KBx9-8uDRY2hAygEUln0RoKE6fPdl2L3wIGS_PqPNN6Gp_DsgPi2n2H4NUo26ReTAqa8txlsuq6TKzoPcPLNtOP_uP69BbFn0iJZefotm2PAcff8Hwad7sz1XAUtgZDDcabA7NCZpCDwV34AgfcmIrO3Yt43X2vKHWuYRo2L4WtdOAvBp3KIITntdP2bSvvwX2rsBOwtJShpRcxvgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
۱۸ بازار میوه و تره‌بار مشهد در خدمت زائران و مجاوران
هم‌زمان با برگزاری آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۸ بازار منتخب میوه و تره‌بار شهرداری مشهد با هدف تأمین مایحتاج روزانه، حفظ آرامش بازار و دسترسی آسان زائران و مجاوران، آماده خدمت‌رسانی هستند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668511" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXrG174K4lvO5fIJ2mOFLI8GFwOfFh2Nwse5JcE_dvLsiJabznesmuvMhXfvFhF8sczEvyfhEh8cOBoPhexXduZdufDqunAQi52IG96qpLTZ_QAZ63Hz_Ko7VrZsFuu5SF1JKF40H7K-7LQrWQw1OKPDArJuRxf9VhJg7ETweICmMhm7FboytlM1Qoe6vskS0bEoaGNbdgarNlBB6ilbPLSczPNjCng0aejpGhyCR9eIczTpXXFTlA9E68xzLYp4G_G3Ov2vrKsgy2mfeeK4KqAXBeIPMubfy0lorHx84M7ChD5R8QogMXtEH3N_Wgn0x8GInbDFNCqV5spA1nMtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: به ماجراجویی‌ها پاسخ فوری داده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668510" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmT4olRInMzLnmZszmAnr1-ClUEIWQd6CVyrWXJxYauB9-PfJSc53i83P6xgMSs6bXaJbOuFsTBbgYfVertBwLWA3seSIQgEyKqI0P5niUg6iD_70REafE2v1-ieDrcDTAae7ZxKX_jc0RhFSJ9u5gN5fC8YcKsUFG3erz9HVjGH2PkWFn81R9D3U09-uwA1rxSjSVL_bosn927sbI99fMBjrYS_wyWGWgDcn1yDiDJ0Qj7MSMjhzLhFwTVMZaw5BCuwsZPEfw4lApX92MNch-JCynbo1HdRvGYxkjOCLNmbnIfxCA8nKa2nS3w6E_GUu3Clk_gy9vJZMOQln9yPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668509" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694c471948.mp4?token=d5ttwaBPkCc33696OLUVkW6x1EVX-eW0IHhDhUy1yxldNvhFyuNzPvn_dUp3fJEDwZGMUl0IhLkf82ou0DLTxV1ac6kWwWosIcEhFZ9MrDAlXhIs0adPo8a2dq733Afq2a6i2y3ibMEWlXRSwMnuqKk1w6fH0Yg985c-QfE3_hS9-TzVYhzBn9aYis1Vh-zPJ7AZ9kTBFX5msg1leMtGqDLJIeua5ruZpRvW2aRITo2OXXXaoMsWK6gt9zl8t47pyMr9GH3_hQGUMFrkYhIVLbDu-dnrdk2O1TQn-5nGBl_4z8fu1OzYmjobkDaeyVcTW45LdmOyGuVRb0bs8tYrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694c471948.mp4?token=d5ttwaBPkCc33696OLUVkW6x1EVX-eW0IHhDhUy1yxldNvhFyuNzPvn_dUp3fJEDwZGMUl0IhLkf82ou0DLTxV1ac6kWwWosIcEhFZ9MrDAlXhIs0adPo8a2dq733Afq2a6i2y3ibMEWlXRSwMnuqKk1w6fH0Yg985c-QfE3_hS9-TzVYhzBn9aYis1Vh-zPJ7AZ9kTBFX5msg1leMtGqDLJIeua5ruZpRvW2aRITo2OXXXaoMsWK6gt9zl8t47pyMr9GH3_hQGUMFrkYhIVLbDu-dnrdk2O1TQn-5nGBl_4z8fu1OzYmjobkDaeyVcTW45LdmOyGuVRb0bs8tYrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرد عراقی با پرچم قرمز: برای رهبر شهید خون‌خواهی می‌کنیم.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668508" target="_blank">📅 16:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=lJ_o6IuP-buP7NqjwNV-G0Jt-RMYnT-0dXYWBDDnfoqAeYX4_GpG83evRInBwOrnYbCrqrnNkyr2kJYw41_rtoHxekTddC6ZPjWtAWqdA1xEQyhdQy7fXaYKjS5ZxrlzzBXoinpdWi2SeBNQu9f7RDdCNDF3E2zklnpv64WeS0JfY3T6uPg8LiMv-yE6xvnC_vNuHB61QxXj8yeWwdEq3o0yHX26ccGen48Q--bz4s-UskfVvBeYMzWFzNThc78ReGRWnY72FDFga2YY5OO3YC51WI-Pv9EOnluopTmvYWgpfn7-U5LpmZdEpESbNlb0HoVpPPkryNzrkLcs6G_zFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=lJ_o6IuP-buP7NqjwNV-G0Jt-RMYnT-0dXYWBDDnfoqAeYX4_GpG83evRInBwOrnYbCrqrnNkyr2kJYw41_rtoHxekTddC6ZPjWtAWqdA1xEQyhdQy7fXaYKjS5ZxrlzzBXoinpdWi2SeBNQu9f7RDdCNDF3E2zklnpv64WeS0JfY3T6uPg8LiMv-yE6xvnC_vNuHB61QxXj8yeWwdEq3o0yHX26ccGen48Q--bz4s-UskfVvBeYMzWFzNThc78ReGRWnY72FDFga2YY5OO3YC51WI-Pv9EOnluopTmvYWgpfn7-U5LpmZdEpESbNlb0HoVpPPkryNzrkLcs6G_zFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد ایران را جمهوری اسلامی ژاپن خواند!
رئیس‌جمهور آمریکا:
جمهوری اسلامی ژاپن ۱۱۱ تا موشک شلیک کرد. این موشک‌ها به سمت ناو هواپیمابر ما شلیک شده بودند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668507" target="_blank">📅 16:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای شیطان زرد: مسئله به تغییر رژیم در ایران مربوط نیست، بلکه به سلاح هسته‌ای مربوط است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668506" target="_blank">📅 16:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd3c1064e.mp4?token=Mob9lF300IUY09kfvi3F8ipuaPSPO9O3rkBkfa2k-4NRSrngM5Uuk0HErPFyKwScYVsHaGmKuiZ2UfCpighw48MwwIi4Z1UbapAZhJntiBflr6flm9PO42tuKas0MFs31gZbUq52GZ_StDmZ8L4ofE9IEIACf7Gtq5lhsGaSQKojG0tz45WOzgjweueqznch_eul4G7DOD0H-LJh9Y0qAQJcPN4sZ-c2Ai3krzV_Bqy6PjjNk3UF7k_1DgiWgP_tdjcBITLWvQU2yd_LYVg_nTO76PCzBLtUENAEPU-AeFNMKU6x2Q3XUFdWaRj_nip2EqYF4GZczoPjYMDRE3qaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd3c1064e.mp4?token=Mob9lF300IUY09kfvi3F8ipuaPSPO9O3rkBkfa2k-4NRSrngM5Uuk0HErPFyKwScYVsHaGmKuiZ2UfCpighw48MwwIi4Z1UbapAZhJntiBflr6flm9PO42tuKas0MFs31gZbUq52GZ_StDmZ8L4ofE9IEIACf7Gtq5lhsGaSQKojG0tz45WOzgjweueqznch_eul4G7DOD0H-LJh9Y0qAQJcPN4sZ-c2Ai3krzV_Bqy6PjjNk3UF7k_1DgiWgP_tdjcBITLWvQU2yd_LYVg_nTO76PCzBLtUENAEPU-AeFNMKU6x2Q3XUFdWaRj_nip2EqYF4GZczoPjYMDRE3qaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از روند برگزاری مراسم تشییع پیکر رهبر آزادگان جهان آیت‌الله سیدعلی خامنه‌ای(قدس سره) در کربلا معلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668505" target="_blank">📅 16:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgumPooGAu1eQqWgAlp64hmOuDZC_05984N7fRjVe8GqVF1mIvqpc0oC6QeEA3xL7DZrjAtJOj1AY_Ou7cyDtd69uRASNhLlUtj8_Ke0pciyJBIdLNnf5xlGx9oLNNwSbQ56oHbslaAe2aVCGoxBglyCR56VW8WS14Ai4nlBjwHWr6D_f63BcELSpOJ3L53-twroh6CxaiHM-HIVdg3OAjFUDG-AOvIBHbqCx5c7ChBbPqg1oRcbDq8mHuP__oK-UobeRQ6D67axQg1N5hHUUd0iRmHImG3Kt5IOBNVVhhIxiMUKwOOQNf926TWONUp-VhSC_An3m76qihAP3RsBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکسی از یک نقاشی بر روی دیوارهای غزه که توسط هنرمندان فلسطینی اجرا شده: سیدعلی [خامنه‌ای]، ای محبوب فلسطین، غزه تو را هرگز فراموش نخواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668504" target="_blank">📅 16:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
قدرتی: رسانه‌های خارجی جمعیت مراسم تشییع را ۲۰ میلیون نفر پیش‌بینی کردند
عباس قدرتی زوارم، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برگزاری چنین مراسم عظیمی نیازمند هماهنگی کامل بین دستگاه‌های مختلف از جمله مجلس، قوه قضاییه، شهرداری و سایر نهادها بود که با انسجام و همدلی انجام شد.
🔹
این حضور بی‌سابقه معادلات قدرت در منطقه و جهان را تحت تأثیر قرار داده و دشمنان را با واقعیت جدیدی از پشتوانه مردمی نظام مواجه کرده است.
🔹
رسانه‌های خارجی جمعیت مراسم تشییع رهبر شهید را بیست میلیون نفر پیش‌بینی کرده‌اند و این حضور بی‌نظیر پشتوانه‌ای عظیم برای نظام جمهوری اسلامی محسوب می‌شود.
🔹
این حضور گسترده نشان‌دهنده رفراندومی برای حمایت مردم از رهبری و نظام است و در صورت ادامه مذاکرات این پشتوانه مردمی قدرت چانه‌زنی ایران را افزایش خواهد داد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668503" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8802b304b8.mp4?token=bBxti1fE_umUuU71SSNlYwKCTvP2AMmbG0m3uy6lBgwntyMUMpbXFmECkbT7mYMu4lJkDKcPKcXKZR2n0J7WcFrPxNjOfi6lTb57l4Uex-HUJdnP88lR_3xpE_AByAq6N64CQlFih5QzWJ-6YgX7Q2jVgpuMiGKHdGVXHWR5HORbGOOgbcWwHvJxOiiFROehNsF8Rb6xnSPZSqBZbLQZ-8GtH5Tt_QBh993kw-nCRLziYRqzaQ7w6ImnjAVFV7wH6fgm3OeNi5N8xmOXzZjgdgHQ1ZBemJReWZLl4f6UjxaDBb4D7PEebjLvVkiV_FGn6Gbb1LTuFdJmWyWpXHh3vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8802b304b8.mp4?token=bBxti1fE_umUuU71SSNlYwKCTvP2AMmbG0m3uy6lBgwntyMUMpbXFmECkbT7mYMu4lJkDKcPKcXKZR2n0J7WcFrPxNjOfi6lTb57l4Uex-HUJdnP88lR_3xpE_AByAq6N64CQlFih5QzWJ-6YgX7Q2jVgpuMiGKHdGVXHWR5HORbGOOgbcWwHvJxOiiFROehNsF8Rb6xnSPZSqBZbLQZ-8GtH5Tt_QBh993kw-nCRLziYRqzaQ7w6ImnjAVFV7wH6fgm3OeNi5N8xmOXzZjgdgHQ1ZBemJReWZLl4f6UjxaDBb4D7PEebjLvVkiV_FGn6Gbb1LTuFdJmWyWpXHh3vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بستن حرم امام حسین(ع) برای پذیرش پیکر رهبر آزادیخواهان
جهان
🔹
حرم مطهر امام حسین(ع) در کربلا به‌منظور آمادگی برای استقبال از پیکر مطهر رهبر شیعیان جهان مسدود شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668502" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ادعای خوک نجس درباره ایران: احتمالاً امشب دوباره به آن‌ها حمله خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668501" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تشییع باشکوه قائد امت از خیابان ابومهدی المهندس در کربلا آغاز شد
🔹
خبرگزاری رسمی عراق (واع): پیکر مطهر رهبر مسلمانان جهان به کربلای معلی رسید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668500" target="_blank">📅 16:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رویترز به نقل از یک منبع: شیطان زرد به متحدان ناتو گفت که می‌خواهد آمریکا همچنان در ناتو باقی بماند/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668499" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=g32yG43UCMP3C-3HJ0rlN1LqYGS6XTsY1-f4r3D31RlDMD5bhaZcEiV-IA9DxF8jfPp-JcoNiudScx5_CjJuVxpS51KEGuSTuHxwJc1Lm1VdRm6hcsSWTiev9UGJBXHKXKrE7oxBpeDAPZiPKWX9Pe7Z7fSp2Nqo1ceT5m81On3_VWbsmA-Z_CNTGlctNdBDQN-i9_npcEWWv6KII3mY9poyRnkZWuR9qPuE8zl1c3oeR-bwuNVmHx792Aq22ROir_nVKRUYH7oHaWtQJa-sq9cOQclvo4VOFRkyN4LaOGH4XGxVgtCQONAZIJcRfG6rMQEge8a5i-gOLbPDhoPSJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=g32yG43UCMP3C-3HJ0rlN1LqYGS6XTsY1-f4r3D31RlDMD5bhaZcEiV-IA9DxF8jfPp-JcoNiudScx5_CjJuVxpS51KEGuSTuHxwJc1Lm1VdRm6hcsSWTiev9UGJBXHKXKrE7oxBpeDAPZiPKWX9Pe7Z7fSp2Nqo1ceT5m81On3_VWbsmA-Z_CNTGlctNdBDQN-i9_npcEWWv6KII3mY9poyRnkZWuR9qPuE8zl1c3oeR-bwuNVmHx792Aq22ROir_nVKRUYH7oHaWtQJa-sq9cOQclvo4VOFRkyN4LaOGH4XGxVgtCQONAZIJcRfG6rMQEge8a5i-gOLbPDhoPSJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین، مملو از عاشقان چشم‌به‌راه امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668498" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b0c59b01.mp4?token=iLE7ISTIFqP4lqxZVSzCyerhlO3pGhaGI9KU6ME4DFHf20JfYwWxRaBN_qJsRexHJDNXeh8MeMeGKmmNLEHZgr9U-0p-vuGlxOUd94aVR1hsGQn6Qfv2EXjdcaCL3K_B0VVYFkOCI1UR46pF4IQm_DLoH9EGCWPvLFDh9rWlIF4ewx3QAGEmSltQ6hxFlJ-KXZjUgEQJVy6n8HU08pF3nHVmdll0HmjAWhJxTALdvktvGpPwsgoPemi-4WfUFODv1mG5-Th9p2SXwW2H3cYzfFxjbVh8vDsUWEPQCaNCclcy48564TT0jKruoLEIMEq-joVccsiOFoT3H17oyo16Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b0c59b01.mp4?token=iLE7ISTIFqP4lqxZVSzCyerhlO3pGhaGI9KU6ME4DFHf20JfYwWxRaBN_qJsRexHJDNXeh8MeMeGKmmNLEHZgr9U-0p-vuGlxOUd94aVR1hsGQn6Qfv2EXjdcaCL3K_B0VVYFkOCI1UR46pF4IQm_DLoH9EGCWPvLFDh9rWlIF4ewx3QAGEmSltQ6hxFlJ-KXZjUgEQJVy6n8HU08pF3nHVmdll0HmjAWhJxTALdvktvGpPwsgoPemi-4WfUFODv1mG5-Th9p2SXwW2H3cYzfFxjbVh8vDsUWEPQCaNCclcy48564TT0jKruoLEIMEq-joVccsiOFoT3H17oyo16Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خوک نجس درباره ایران: احتمالاً امشب دوباره به آن‌ها حمله خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668497" target="_blank">📅 16:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609a13bdb6.mp4?token=qAc4nc8U-pxs6KJWAnuHvMAi9lsOt4jfgovlQXpGjNtMRJPQ936O1KiBZwmK_clJohDZnuuS6QMYLqzvP2GXWZQVaSxQl2Qn8oxk9lrMdY2OibT7jSlqbDG3ZrLoGVcO9xKFadnM5tPvuEEHO8f6hnSEQrhQdZRatewY4P5Z2lMxqfnPeGb5n47wZsw5IsnglOLrBFyGmBTy8r4ZSbnElSlkJdhObd73Y0wLVlrC1DuM1iJGIsfBHpl9yJWpsFlc_MqqPuKq-znhQ6X9XBhqe1lciHRP28Y2DK_TgtWPkithE8LY8xCfBPq4WK3KLUakv99QfN9zlYwNR3Ty1ceeJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609a13bdb6.mp4?token=qAc4nc8U-pxs6KJWAnuHvMAi9lsOt4jfgovlQXpGjNtMRJPQ936O1KiBZwmK_clJohDZnuuS6QMYLqzvP2GXWZQVaSxQl2Qn8oxk9lrMdY2OibT7jSlqbDG3ZrLoGVcO9xKFadnM5tPvuEEHO8f6hnSEQrhQdZRatewY4P5Z2lMxqfnPeGb5n47wZsw5IsnglOLrBFyGmBTy8r4ZSbnElSlkJdhObd73Y0wLVlrC1DuM1iJGIsfBHpl9yJWpsFlc_MqqPuKq-znhQ6X9XBhqe1lciHRP28Y2DK_TgtWPkithE8LY8xCfBPq4WK3KLUakv99QfN9zlYwNR3Ty1ceeJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری آمریکایی: محبوبیت و احترام آیت‌الله خامنه‌ای،رهبر آزادی‌خواهان جهان باورنکردنی است
🔹
پاتریک هنینگسن، فیلمساز و تحلیلگر مسائل سیاسی حضور گسترده مردم در مراسم تشییع قائد شهید امت و احترام و محبوبیت ایشان در میان ایرانی‌ها را «باورنکردنی» توصیف کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668496" target="_blank">📅 16:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بیانیه پایانی سران ناتو: بر لزوم نرسیدن ایران به سلاح هسته‌ای تاکید می‌‌کنیم.
🔹
خوک نجس: اوکراین و روسیه خواستار خاتمه جنگ هستند
.
🔹
وزیر خارجه آلمان: از آمریکا و ایران می‌خواهیم که تنش‌ها را کاهش دهند.
🔹
اردوغان خواستار لغو محدودیت‌ همکاری دفاعی میان اعضای ناتوشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668495" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b4dd63cd.mp4?token=NDF6aJeQU_26d84IlztbWH830Z3xnTKm2lraxQv857ekcqii70FEIjURADMDhx2KbquO4YQoQfKtzELKs0nnRaNU0V-yMeNe9ETO6Lge7oxgEN76VziibgDfxQ_BxcMrgv5mqpwQtSVAXRgHkLuDyyr1YJmXVSwzb1iQyBalwyoBBcxacsUOgA9vhIBuI2CKgiOIo8FSuzPZF6o-FYtDGgZktYEyKuTKo56_ulrXEtKsSFO-Og-gnrv2Esp8JovH2DWg1PRo_aJEYEEFXO6L2A0PCn-kuI6ocGhAiqcEW_Q7dK3iOLDARngx_V_WLxn1Xe5gkyjjAV0POklNNgx_Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b4dd63cd.mp4?token=NDF6aJeQU_26d84IlztbWH830Z3xnTKm2lraxQv857ekcqii70FEIjURADMDhx2KbquO4YQoQfKtzELKs0nnRaNU0V-yMeNe9ETO6Lge7oxgEN76VziibgDfxQ_BxcMrgv5mqpwQtSVAXRgHkLuDyyr1YJmXVSwzb1iQyBalwyoBBcxacsUOgA9vhIBuI2CKgiOIo8FSuzPZF6o-FYtDGgZktYEyKuTKo56_ulrXEtKsSFO-Og-gnrv2Esp8JovH2DWg1PRo_aJEYEEFXO6L2A0PCn-kuI6ocGhAiqcEW_Q7dK3iOLDARngx_V_WLxn1Xe5gkyjjAV0POklNNgx_Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین رهبر شهید و خانوادهٔ شهیدشان توسط شیعیان نیجریه
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668494" target="_blank">📅 16:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668492">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkgswmMnCtsEf1uXR1vOJUpcQv2AkMIMHkFdfxea6xnyWD1qvJw0cDEFP2svcO_YQNt8uG_9EK6wI37XTeJt0wuV0donstdlZpR309NUT6r4GwFKwAQl7-EKwr-1RIhPH5cchUICCVYDTbRwGkJ-CTFBIIzVN9cEAgb0SiDN0p9_L5U2qenzu_jSV5MvTJmx66Dmc9QeMeVEbuJJH7M_AsWa62QuB3eAlOhE1kK8xutfuS7e7a2_fyMPRkmjuErQ0OF3c7CZTfdNlguyADOQULQkkouy7j0UFTTrAr5KYgbYOXqwKhhQslK-vuuerAP3rZyLMrmKflmccUlglPVeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خارجۀ آلمان: برای پاکسازی مین‌ها از تنگه هرمز به توافق با ایران و عمان نیاز داریم
🔹
قیمت انرژی در حال افزایش است و این موضوع بار سنگینی بر دوش تمام جهان گذاشته.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668492" target="_blank">📅 16:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4L0ovi2U6bXn8rIqnL3_btfP_7KUl4VlpHmDpfqwrJfmJsKmiWjNb9Tb5VAveCDblWQGje68Hl2_blZyhlVFgG3jM4AzAT9BS3eWr_EcU4eGrr7rxH1fvhEziP7HEyCtv6i6QGyIuMP-g7XgbMLlfuT6CL6WGHNAjVYWVjDXqADYdDANRKfEE6lN5-Ed48PVXqSMfntNlmqzj86ZbPYf7xtS09NEaFhd00Q_UXnM8lA1GZDs4w8rPOyxfa0RQdi0GO7qyZQKhzlzv2W77_tDj_QAKbJBwe7ZHbAPFnoxbNxSBOVDZCDxQCoOJF-qH3N4b8rR_w9j-g6SnEYCCwYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e05c1b71a.mp4?token=chXd5vAdL8vdcHChtxXOOioTqAquZBylCslGImwbslEnoIAuIlJz_LFUZn8JFaCiIa_MQj9zfkJAISoTK8cZHYhzPCefpUA3-_r0NS0mR9iBgTMoKZd1d0i91ufIYnzI13pxls2RotdHA7GquWCNY1IxvB_TuVR0DEBq0zZxWnptG0I9dQHIQEndfLpSryID6vIGODlwIPBXy9a4U3wfMDXfmSaoZ0VBgzjUXDFUrXUm8EMy09WkOKM6NzDUsDxz_wvlwsTzZiV9Wv65M9rDJytfW_O9UrOUYdYeHK02LrcasI7sDt9FTZAnMnhzu0VXSEsGK-WqGWpCXJADalWNZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e05c1b71a.mp4?token=chXd5vAdL8vdcHChtxXOOioTqAquZBylCslGImwbslEnoIAuIlJz_LFUZn8JFaCiIa_MQj9zfkJAISoTK8cZHYhzPCefpUA3-_r0NS0mR9iBgTMoKZd1d0i91ufIYnzI13pxls2RotdHA7GquWCNY1IxvB_TuVR0DEBq0zZxWnptG0I9dQHIQEndfLpSryID6vIGODlwIPBXy9a4U3wfMDXfmSaoZ0VBgzjUXDFUrXUm8EMy09WkOKM6NzDUsDxz_wvlwsTzZiV9Wv65M9rDJytfW_O9UrOUYdYeHK02LrcasI7sDt9FTZAnMnhzu0VXSEsGK-WqGWpCXJADalWNZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم تشییع باشکوه رهبر آزادی‌خواهان جهان در برلین آلمان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668488" target="_blank">📅 16:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/YKxkniyoPge8E6D0-KvHrRfiZJel1J2rjIxdfHLMrcMDrd1kkeIGjF00ciOB36duT6Fk_zQHBacqYDnLfWDWw7Mg0a7VDlKPRRWj0NYYdDgYaDKhipwvCxAumx7aCd7OklABF0rT6srJbG5GjwvCie2qnK8QbeXff4wZlpwU9hmixSjR3vEE4I9f2ck_OB1ajUhzQDJ-Qo6Bp0W5DTt9wRQWCIUrQQTZfx5UndQ-LSiJ14RhS3KcSD33spk9SSpQDm8RWBsTnDUP4ENepnhvPqaM96Y7OUJSZyCfV4tNiHX5dyD2tlh3uGDdZxw-z_NfShFPAIEMj8j5Kk1PTOYG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/bIUPQC9kDfXUcozShVnXizo65kZbiG_Pb7u7pDHfHCfxZh7Xo2druaPJxnhPHjAH1WvMZr3D2P41aSaPRNVznGX90qfEMvhJopt7GS2m6_Ixd8T94Tp5RcoUZQSSne34hMFaodzddl2ip55Qw45FhByU9QZt6hI1EOxVD_2iN67_GDEgT-Zq24jAoPZcUdx70UWBSL1c4p6z4nR7HRw0mgUwFgJs2c2Z9DJPAXwNoegVW7y7vJNwRiI9jKV0VUSPguPhNlLXWr2VtSUHBgT03gzXCdixrgMp4PEMjSnMvqw_yDw-pKyfpxWTKfxryD7EfUnHaGTN085VD_Yt4j0Zjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدارهای رهبر مسلمانان جهان با ماندلا و کاسترو
🔹
دیدار نلسون ماندلا با آیت الله سید علی خامنه‌ای، ابر مرد تاریخ ایران در ۲۵ مهر ۱۳۷۸
🔹
دیدار فيدل كاسترو رييس جمهور كوبا با آیت الله سید علی خامنه‌ای رهبر انقلاب، ۱۹ اردیبهشت ۱۳۸۰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668486" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
محدوده‌های ترافیکی مشهد در روز تشییع پیکر رهبر شهید انقلاب
🔹
بخش غربی: از میدان فردوسی تا حرم مطهر رضوی.
🔹
بخش شمالی: از میدان فجر تا حرم مطهر رضوی.
🔹
بخش شرقی: از محدوده تقاطع مصلی با کمربندی تا حرم مطهر رضوی.
🔹
بخش جنوبی: از محدوده پایانه مسافربری تا حرم مطهر رضوی.
🔹
مسیر بلوار جمهوری: از میدان پرواز تا میدان ۱۵ خرداد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668484" target="_blank">📅 16:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXl-udu3ASo_714LmC4JXUAUBGQCxJgfwbwp1dE6hPgQzPKQCZAt43IOx9qhJqJDRlwdytBTGRHYq7Fmu40KwzMbBpL7d4CsYp-BZcNmdyDTUO_TrUTw9z-9UjkgRJwb8k7oG1mGx07cuysfmHmDb883yxBPpNvIDNTodJGpKzA3km4qXFsU_rEXnklBUXIIMvd2IN6ImF1FuGS_JP1RVMQFny0WCQSiTAWj0N51CRRiPlCn-KA5TS5PfyiUVT9lwhQ1n67SW1rsu3z1FLwpbsiQoNexJHenEIzwzTSegeLgVbnxBs3gdf2exse5wk5uTV_GzqLnK2In9AnJhYMpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛒
فعالیت ویژه ۱۴ فروشگاه «شهرما» در مشهد برای خدمت‌رسانی به زائران
هم‌زمان با برگزاری آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۴ فروشگاه «شهرما» در مشهد با عرضه اقلام اساسی و افزایش ساعات فعالیت از ۸ صبح تا ۲۲ شب، آماده تأمین نیازهای زائران و مجاوران شدند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668483" target="_blank">📅 16:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7MDZAdl6iJ5qEpe2CScpZHIHmM2ozKIBuHglpEGgwDhnhs5Z9hsdHEvEJsIZ4T0vkLcPCvQj2qFDBQLYO_QYO_qVmZI-VPcZD435Z556Go2jWadH-E_J1D5DWgcuZshc9WxXiaX4nN-hF3O2XwXsvOrdsl3BqPUlU7bqT91Ckye5r22nIWExHXDVeGtf-Fn58RElTvvublPrx8SktG_Yeqq-o5LZOXj3x_QsEUEP1fmh3Z6Ps6Igh5BZ-6NQyh_2MbBXFW_b64KJgxEqpqd1Jwc-C2yOyDnwJT-IWMsiyTdJ-0BwDQRGeL_nw4DS0SCsw6xqt5JYF5Y6J9zjSvyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سامانه وادانا دانشگاه آزاد از دسترس خارج شد
روابط عمومی دانشگاه آزاد:
🔹
علت از دسترس خارج شدن سامانه‌های این دانشگاه را به‌روزرسانی آن‌ها است.
🔹
برخی رسانه‌ها از حمله سایبری به این سامانه‌ها خبر داده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668482" target="_blank">📅 16:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLTXCA0GjJT_Aq0jbYPMvkJceTrFxArkhgxWNxxeTUQcDfqGxgKTavD68_W5pEkQb0eTMlMHOABvQSdZVYW6dEElUU1Vxa9SKfOZUkYho4w8baM2olFnFh6B2Zq40Y_Sx7-IyAOjSucnM4fuw_kuZcxHZTsT_vljl-KfzWYBVkfoKQkNoMSpq3ENqC9KaeVjRg-NXZqQjHNmEcSZo7LY1dsGsDxwnN1exIkN_oEtUsNki2feEG96Yvs9kbo13mO1G6y1G7N842VwrV0Srwqz0rXFrnDqQysncdvryZHau9NHLAFcAv1qKeT6IatEpRJcet0RER5fNdX272DJDyxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی از یک نقاشی که بر دیوارهای غزه توسط هنرمندان فلسطینی اجرا شده:
سیدعلی [خامنه‌ای]، ای محبوب فلسطین، غزه تو را هرگز فراموش نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668481" target="_blank">📅 15:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
برت اریکسون: در چه دنیایی بازگشت به وضعیت پیش از تفاهم‌نامه منطقی به نظر می‌رسد؟
مدیر ارشد یک کمپانی تحلیل ریسک:
🔹
اگر لغو معافیت تحریم‌های نفتی ایران باعث شود که هر دو طرف دوباره یکدیگر را محاصره کنند، جز اینکه تهران اهرم فشار بیشتری به دست آورده، چه چیزی تغییر کرده؟
🔹
ایران در این ۱۹ روز تقریباً دو برابر میزان معمول خود نفت صادر کرده، اما بقیه جهان حتی به سطح عادی صادرات هم نزدیک نشده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668480" target="_blank">📅 15:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668479">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
رئیس جمهور لیتوانی نخود هر آشی شد!
🔹
رئیس جمهور لیتوانی از حملات ایالات متحده به ایران حمایت می‌کند و آن را «جنگ ما» می‌نامد!
🔹
گیتاناس نائوسدا، رئیس جمهور لیتوانی گفت که «کاملاً واضح است که این درگیری ما، جنگ ما نیز هست و اگر از امریکا انتظار همبستگی داریم، باید متحد بمانیم.»
🔹
ناوسدا اعزام حداکثر ۴۰ پرسنل نظامی و کارمند غیرنظامی دفاع ملی لیتوانی را به عملیات بین‌المللی با هدف بازگرداندن ناوبری در تنگه هرمز مجاز دانست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668479" target="_blank">📅 15:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668478">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
یک شخصی هست که ۶۹ ساله حرم امام حسین نیومده......
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668478" target="_blank">📅 15:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668477">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
درب‌های روضه منوره و بخش مرکزی حرم امام رضا(ع) برای تردد زائران بسته شد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668477" target="_blank">📅 15:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668466">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWj6tgbnmVT1u7WOgZ-L3V8ugWRHSDF-X1z8l1KZKx3UKgCftxbsOc_QfWciwTjG7iwOvP5EGAxKEpMm3jaZz1HmSICRbrEaJGR8h2QkvmlOVgCjk5aCPeGoiR36pSf4aMJJXmxiHdOnOuCUEkxV95E2JNEDIaag0Rq3vAF5vgkwOtCZLVUskaPXQXJJPSnsjGO_nnOG5wnsq54yz86d6dxx67RyHLn4M5fCI5n8ps1sZQy1bh7yFG6MvOhpS0FyknFKpaT_B374VqrN6kCJ9zz3usCq_fmMDVKUBE9vPV58UZb0Hfsy2N0u3NfZ97lNSm-7-2DiARMBFMOr6ebIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDbC8X8Z4aoG1qp533CpbTJeMR9f3ywKy2e2K9nEbcx3eQxEl3PMePdrz7mgl3B_XQFadDICAob6aUIxti8Jx0q8G7i4g8N2YVurr0SILyrSye6ibNrORqe1WuBvYg3fKirSIX1px2VTfmZ9CybPpu5JG8X6opDri6R4B85c6JE9faTJbnKjTZl6D6Um79GHx5UPlPEtfoI77EiSsy0JBAT2xAf3jn0koVWgS0McZe97ayY8OK8VeVsSGS9BS2OtB2VPLvN6hs_RQyqd6xPNARKV7dQhRA5P1RUZZodr4N_JmuES7vYBNVIC7PmTjB3LKZp_C0WjVaW8vyoU2shpTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYEk0Y86zirxzcZc4i4OS5xxzhf3byiss5-k9f22So8fta-oX8VBI1SU4slsQ5va-MFcWbdR6iFBvWOSxMHmmDPV2M2Z-cM3gSW3IPbjvm6rvENNSn6mAPv_RhikdkFL__Fq11md3HL_KXe76puMsl8Hf6ehuljfRuDSStChSu1AqNYvdCBaB_n_B0wBM0XAUkLzERNDT39IrCbJ2daGRVPu9EqktdKTB7KTlhdMcZGdeLkslGt1We5d9GO0h39zyOmdDeoaSuJZYBs4enS89XbUye0bBdGk_BQf_0pbEYhotwiW6jTV9bBlnw-oQlnoVbaHvUXHiXe6cbqXC0agsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdtGaY2xtbgv0cIqpHBUFoqRlUNm1nVCX5TDStRS9BE9gqjUm0Nz5vRaqblzg5x4Y2NYYgsr5j3CjNceVGvyeFWeZnze_9ZoAodHCsH96zepy8aMpf2tMNYilZAliqVFESF1PdtcFfGyJ2yOLJnl6J_oh5Ny-KRNsGKsMD82g0JTtedZYwnykMYkjCPsWTLpiVKeidQ0UCu63-XTYW0aENqIq7x22tbRTl5a2FPTlXnYAlz0e3ej1KSXokfsF-wmp730uMehti0PtwHvCcBJYzHH_FBZ2RdSAeyUxDHnKYgeghHiwADkvWJTjr8omKZSuTozILH2eQOhGi97ZL_1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSYsSNvAs90S_lOFr2_FVviJknLRDu-68jsoDA4P7C_HOwPQdiWypNGaUxvDLdY0w3nua-kJdyEVPdgky-oBKpPg_KVCIZlVtsMYe3DuzRKaq9Os-z62pekxSDv7h3uMJWZaaiZ1EGE4sEbLK8DbNPTzh9zob80snfeBuA4pswgvExsxT0XuSHaOAsUrt8whDON8g-BWCK_szjL8YB92PGhm4Qzcwk2KV69LmhLwMbNuPOEFqnaBt-lSt3B19lCNlODRw6SI6oIFL30vswihXUWXliMzPFmpZy59X7Hj3Abc6SCgFGOq9aYwlb_HeTl8ajem6ZKorzKzp5u4yWINBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJWByL7OIQSRsPQ7t51IjtFTw-VYu1prlGuM56HNryrklno_dSKDmY0gBiYI92o63tAyZwbAQxcX3KQWg5803VwLYRfeYZSj19QQ_t2ibFxGf6FG3QmaGVoznuFXlNjhBhJ6zVvhx9vduPYJ43vFa3S2b3hb6KDhfAwJyllrIsM9gICjaZH6w8mpSeEmfUdVeegAgQ7-GVvbkUz3iWYiAGs1184PXKPw5EUkqpdvjwbcXB18ApI8_9Z9B8ZM49jiQtiGhdN4oo-RgG5scz39rYWQ47EhfYzDU6lofVm3yLRIkfh-ZQ3IT_tHNmIe9wWMKI5YO7QEbxxi1OII2QLTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8dqVwYaCjb61vLaEPG5kU-qPHTKifQ2qyhzzxaak1a7LlCuNO78QxtX_-3LW2jGXOSR6cLEMdCCR6Q3YDrgBFuhCAKYZCJor0ONEqubTIh0nazSoM7yGynonW881_ilKdXi_towhhAgIKekIOqBmyEKllZMOiXgmnCLVECcR9CMmvnmE-zunfcLDAPiKw8Z0ODAvKymGGESjtTiEvYGTyymnTqqS3k6UDYnBY0kVQMqbwy3QfEHMAWw6Osk3mV2N0Bwg1nmBwwsTkVOs45B7HmwKEUIBcc23GmuBE0YN9EcHy655qdpcEGIWmFCPL3UiEdU2eaZTy1qaR1y-ZPGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-Eln879ZcROjouWY1N-6lGC7VXRUkR4xELhUWy2qxq72D3ay_y4StozuVs1xc4D1pipZZQbo8pq4bB8JyF1ms2qKafSJ2rRCk7voOOpE69I30HgRhNPpeaQUWjcYfgLpdGnYj3agC16T0lDNyPddV26u67V0mCfKdG5gdBKSQVFGUIy3hTQbqhxbIwUp8giAbXzFPpuItKBCtEE04vz5rylE8pyTH-upervIiJrxKFyLHf0dsghY8m41xuNnRNccVFIxV5tY1a2ZIRdLscQ1BJFmIh4ouHPmwOSgTttp2Y4BqqXeIMRJiHPkoZaSKqkWE0pYhO283taucF6jFD9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHrXmlHlZUYfKrx5grcYGWjdNot9Sgm4t2hjKUWM9JNy0TPZT5Av3WszfkogIs8u5Ny7TLGKVm3yN9b6lZSxCJJw4iebDwC4tO05fgbiGSB-p_EJhAP4cfkWfjxMtgl5lvyTioFsHWgc4MW5AXYp6sxbdDx5O_TLf3EDJksKDMWkwZPoVxQiOZI1aOTfCHcExOfuJUtJd6KFLZrUeWyM6dCut5yBNe0cMmCbLH05blSqw1llN80NfNXFVmFXhzYbtv2bLMH1vDBgK1pyxLsjDawSsKagZyicSiCZXRZoMFRMcvKomardpoBvKhWnqICosn6KFV_NXLmufrAG4DcCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cb1ag8iEZTzAA39pqKwUs7aKHh_HjJsIgdFa6sfTnTdwLamjQKJQswcCYofjz8Y5zm0JsI-tF_q9hJldFJbGdkCnQQRdWS4690VN4IfkRZlNhexy7-EVmg8nSVDqcdZq1FjykSbm_-NDw6Oqftx9Ck6aoU5rsljeV1ZDek-F0vVK0NmFKWFDQdGtpT0bI6m3V7ra-DavWt4_eF-Y-an2RJK2RDbsc-iiTR4rn_eCP4e_ZGxuisw5bBSG3gtkaeAVyGxMcQeai_rVvlF6AhgfYiEI0Qf213yk5Pg9Bm68El5qF92xQFrxIO-2NHBoOHPW-stQ5TU_LFjNJ3ePCZ6A7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش «مچ‌بند سرخ»
🔹
مچ‌بند سرخ، نشانی از عهد، وفاداری و ایستادگی در مسیر شهیدان است. در مراسم تشییع رهبر شهید، با بستن مچ‌بند سرخ، پیام وحدت، مقاومت و خون‌خواهی را به تصویر بکشید.
🔸
تصاویر حضور خود را از طریق آیدی‌های زیر برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668466" target="_blank">📅 15:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رویترز به نقل از یک منبع آگاه: ترامپ در جریان نشست ناتو، پایان دادن به توافق موقت با ایران را تکرار نکرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668465" target="_blank">📅 15:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLZ0mSOmGjwbDvT8g9F10FnSytlzrixluEFeZ6cDhNr1FDVNHtH4mF-MhgxL2UTq-BeX7iCy4t4FicNDjOKH4DwWL_Gi9jNPAf3OPz7v7ob86OBm9buMvX64SPjYcv1HOGAnckxNa5JSV8-UmeoxiJmYCMAzmxcI9JpyOIj5Fmf8SY4ixDnUQlRa4O8Pxdrx--qQZ94YM8tTmK0lcUCJmEOf5LxNVvrHkx7yQCLgjJ3GNl5SU4D1Q_U4ISuLNXSXEGh-n5zx_xjEwAk30d5YmrC4mN3rCm6qXoY0lNtU8kZkwPhY4R7WJFMnXk2yu0gyNGz1s_Lobe2RbycfvX9bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری متفاوت از پیکر خانواده رهبر آزادی‌خواهان جهان در حرم حضرت عباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/668464" target="_blank">📅 15:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مترو و اتوبوس در مشهد رایگان شد/ ممنوعیت عبور خودروهای شخصی در خیابان امام رضا (ع)
🔹
ابوالفضل جلالی، مدافع فصل گذشته استقلال، به پرسپولیس پیوست
🔹
بانک مرکزی: بانک‌های ملی ایران، سپه، ملت، شهر و گردشگری آماده فروش ارز به زائران گرامی هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/668463" target="_blank">📅 15:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
حمله پهپادی به نفتکش امریکایی در دریای سیاه
🔹
دو منبع فعال در بخش نفت اعلام کردند نفتکش «یاسا پولاریس» که شرکت امریکایی شورون برای انتقال نفت از آن استفاده می‌کند، امروز چهارشنبه نزدیک سواحل روسیه در دریای سیاه هدف حمله پهپادی قرار گرفت./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/668462" target="_blank">📅 15:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awSkiV7ejLPB4rYItFxJqo55y5K7tWwu6U6gGlZTg_R5UwLJVHJHAYJDaZbATEsQ1zdvd2CrjTLwP07vbRAWWlVQHjZw1bEXY8-aLXM2qtjDs7oyRbN6BWIUh7MUNYNh8uaFUWZ8nu7WMkXUEZqmjBo1cWrEBfnM-U6IjR3Bygwk-Qh9ow2lKnTCjbgtpwNvTEvv7Mu2umO4YqluXXMvImtiQf4nLaPnPTlPoXHpXyx_3mjcIoyWs3-w93dsYGs790vRdPtEU8luekiBhy2sZVBE4CUGXKXvdMzGXc0aGVYhL41WpQqmDN8_izMAv-OsnewH_HVJG3yEsfb_Cg2-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترافیک دریایی کریدور عمان در تنگه هرمز به صفر رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/668460" target="_blank">📅 15:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1999fdd529.mp4?token=Rh6-JilyrY3KgN2UhBNxTOc2GIveMSGeiweI9U-zXkaQEKie6xv-5seVqGtETwabWgnodkejJKh3KxSee6dlFhSnC8H58ZdMbHgRzr_4-wvDWPIybP0ZBulTqp3-749ocJmmcfqI73BUKKVvdWyosCThCz3mPWCVYhEB42Cgpt_6B1HiRDQlYhNDOoiwsE8qnMzEhviJoBUgyb2Bhlkh6a0zQfgXYgCm7IYUBng_h-83qLPAIEDukd8oF0cAcb0JPOS8OP_j_VlRfqxARtFy8puL6Ksay1CEgogSZseCTlecE_klZ4QPwaj90-iEm2Lf5L_8eN23WgAkeN66CcbAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1999fdd529.mp4?token=Rh6-JilyrY3KgN2UhBNxTOc2GIveMSGeiweI9U-zXkaQEKie6xv-5seVqGtETwabWgnodkejJKh3KxSee6dlFhSnC8H58ZdMbHgRzr_4-wvDWPIybP0ZBulTqp3-749ocJmmcfqI73BUKKVvdWyosCThCz3mPWCVYhEB42Cgpt_6B1HiRDQlYhNDOoiwsE8qnMzEhviJoBUgyb2Bhlkh6a0zQfgXYgCm7IYUBng_h-83qLPAIEDukd8oF0cAcb0JPOS8OP_j_VlRfqxARtFy8puL6Ksay1CEgogSZseCTlecE_klZ4QPwaj90-iEm2Lf5L_8eN23WgAkeN66CcbAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویر دیده‌نشده از حسینیهٔ امام خمینی در بیت رهبری پس‌از حملات ناجوانمردانه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/668459" target="_blank">📅 15:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
بازدید دادستان عمومی و انقلاب مرکز استان خراسان رضوی، معاون محیط زیست و خدمات شهری شهرداری مشهد و مدیران دستگاه‌های اجرایی از روند آماده‌سازی مسیر تشییع پیکر رهبر شهید در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/668458" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تکذیب شایعه انفجار مهیب در شهرستان روانسر
🔹
فرماندار روانسر با تکذیب شایعه منتشر شده درباره وقوع انفجار مهیب در این شهرستان، اعلام کرد این خبر صحت نداشته و هیچ‌گونه حادثه‌ای در این خصوص در روانسر رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/668457" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شبکه المیادین از حمله پهپادی رژیم صهیویستی به ارتفاعات علی الطاهر در جنوب لبنان خبر داد.
🔹
بر اساس اعلام دانشگاه آزاد، همراه داشتن تلفن همراه در جلسه آزمون پایان ترم مجاز شد
🔹
سید علی خمینی، سخنران مجلس ختم رهبر شهید در قم می‌باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/668456" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668455">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پاسخ اولیه سپاه به تجاوزگری‌های آمریکا؛ ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در منطقه هدف قرار گرفت
قرارگاه مرکزی حضرت خاتم‌الانبیا:
🔹
مبداء هرگونه پشتیبانی از ارتش متجاوز آمریکا برای تجاوز به حاکمیت و سرزمین ایرانِ اسلامی، هدف مشروع نیروهای مسلح خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/668455" target="_blank">📅 15:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668454">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z437mOJC8YYuhK8LjA5JSaTD8xSggURq6uh2oAvGBTRU0duVfFsfIuwISDEneCBaQsgrbzTzMKsrEh1W9kxhX49rhSvCaygwIRnp2wTt-yeK9Qdh_j8zRGRz8SECrwc-vdPmh-AezN7qH8ERLHgfKpl-2Obx1ZOQU5PQuZzU54rureRM13-yE4UD-67Nz58cdaa61kU7ywKJrouoV1bi1ep-fLOpA0PYmDdxc6b4Of0VgRzoipb_ckQ9ui0QXrgIFPAJr7ZJZRCTc3n75stbvzrI2Bu_QHA56WCySvGL9z-t-3AdPLXUqTLUDhNhzvGeJ6vQMBjQklI0wS7dLbYbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ووزینیا محبوب‌ترین دروازه‌بان تاریخ اینستاگرام شد
🔹
ووزینیا، دروازه‌بان تیم ملی کیپ‌ورد، با عبور از ایکر کاسیاس به پرطرفدارترین دروازه‌بان تاریخ اینستاگرام از نظر تعداد دنبال‌کننده تبدیل شد. #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/668454" target="_blank">📅 15:02 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
