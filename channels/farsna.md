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
<img src="https://cdn4.telesco.pe/file/Hvpr_Q44tgiHuR9qmbd4gTcOw-QR_Kp4XkfnFpWhnjLi1nzgIoI58xuIzBZl4gVeWAPYuCVSciwmy6a_KHxQLa_1VKpNyqPdzF4Rg93ONN46p0w7F0vRQtdMYsc87BH6UeXXLfgzTvf386FOcx9zqGWlqXySvKprXJjWU89C0mp5RHxQfImLCLDFGZCJVOEPHlyCOjwkI2X_G5EtvvoGnHSf0p14ud-hBnkK8cajbTYeDNbeyiiYYg0Fsbj2--fjdeZwHmI7dwgLd_JZelhZ_eYVW8zoepXkuXnrbdA_unlFUnX1wXK3CNsYNZx4Wh2vwy58LrYXx3kkIsEEgW4ajA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 01:05:37</div>
<hr>

<div class="tg-post" id="msg-466151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmxWRlQKoe07kkOsDbQMSJt6pS3_6KnNXqvmg-bjXLC3X5XTyJE8YVMhrhgocwT2iucd3TDh8rv_cqXuQKUc1WMXcfUdWRKKs-1FOTwxIcIm899P4XYy2IQsWpr0AwJwge8wsmrFz7ov8Poqe6ns1pPvwaGYPTS95LMu0zAfnLIwe5h46yKjCvz6Vt44z_qixmhehAOQ1-qz36tiZ5ZRSlgBtlBWWne7EDWbR-PZhiwOX_duNX1CUskiVzfA_Lpd_xqlLc9tVqPapRDaaWy8e0vM4rYC-At_cdyZXtO53mzevKfOhvf-kgaCtzBgVIFER3rD97De1JtFKIDESAILmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l67fR0SWgASohK5dO2J7ev6xmc7bZu-UUB2tI5A9OYVzm7C-PLNFAJFEXhpUMaOtBPhzPyjjOpHAR2L_7v4OEQotUxPG-z92hndSOMKuolU1mEBDInitJlOkTy3rSMrqlzqD0VEpAjxnDtOyAxr7efcJ59eyRlJPjBQ5rfYW1VIxhsydyImuwxEs4PkXu6oiDd0E9DrcEzBrjpKThHwet9xM1OMKvByrhu4eg8mzBsqgEcqefeN52x50iCnkzwRXo7PMB7Mw6IixRkmg8GYBQn6yWcaJqRbHg1oKbIuEQ0fTRNuiDw5LTj7TSSNp48SITm9W3hFNwh7aAY4t3byVmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69445dd331.mp4?token=tMOQ3hUcxc6jT4P4b7VCUJggZAPDsUq5DZnGubLS_-l5QslXsH-_apSV49Depfglr_AIq9-U7mLSntzSHnRWmFaGZppltiYuR9I5nK_6jBDIkczjDRuObAAh0Sth6obMfKxz7ydE_fhtHcoM859GyrUUwMivJgmaBIuMtm9_d0QUZ_kAenwZ1dd-bpcxrDWek1BVKv_lZ4IIKUb7bJs-cAuAyubJvHZzYjEWge-AX5MpMjvq3tnrrbAC_QBBS9_THv5AH6syWkP_3jKINCK-YzV-y7zQMFlh5IRI7Q7XDeQhJ07f4ge7Lo6RSLoRk2ux8bm2jNvslLb1XAsdGdTjrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69445dd331.mp4?token=tMOQ3hUcxc6jT4P4b7VCUJggZAPDsUq5DZnGubLS_-l5QslXsH-_apSV49Depfglr_AIq9-U7mLSntzSHnRWmFaGZppltiYuR9I5nK_6jBDIkczjDRuObAAh0Sth6obMfKxz7ydE_fhtHcoM859GyrUUwMivJgmaBIuMtm9_d0QUZ_kAenwZ1dd-bpcxrDWek1BVKv_lZ4IIKUb7bJs-cAuAyubJvHZzYjEWge-AX5MpMjvq3tnrrbAC_QBBS9_THv5AH6syWkP_3jKINCK-YzV-y7zQMFlh5IRI7Q7XDeQhJ07f4ge7Lo6RSLoRk2ux8bm2jNvslLb1XAsdGdTjrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ بمباران صنعاء توسط جنگنده‌های سعودی
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/farsna/466151" target="_blank">📅 01:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
سیلاب و آب‌گرفتگی شدید در ایذه
🔹
بارش‌ شدید باران در شهرستان ایذه استان خوزستان علاوه بر آب‌گرفتگی معابر، ورود آب به منازل و خسارت به شهروندان، موجب قطعی برق در برخی مناطق این شهر شد.
🔹
ادارهٔ برق ایذه اعلام کرد که تمامی اکیپ‌های عملیاتی علی‌رغم شرایط نامساعد…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/farsna/466150" target="_blank">📅 00:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملهٔ دوبارهٔ جنگنده‌های سعودی به پایتخت یمن
🔹
منابع یمنی از حداقل دو حملهٔ هوایی جنگنده‌های سعودی به شهر صنعاء خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/466149" target="_blank">📅 00:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=K049TxKY4dudeQm2g7HCyr6yICK5hgoFgQjVekBZkSQwy2yV7AQyTW4-2cIHbuZ5f70cNoChSRYL_4yZSSChyEiQQflCuLeaTD10JsGS5ox3L_bnJeVn_SVCwhWmXm5sp-EZBDXR-VmQKpltKSi-wzwaNsThwbTBJGpCSUDcT744USbfN-j52wv47oV79B-EWH_L34wr5L56BSxwSYJQvvFl3OQW6wb6rzy1wl2PxuPFI8Fx8qBf1lWFXg_mEN1P0ax0NBroQ0T80twPvT-8uuKCC6zMOvaMk6oJOKMaGD1mWRKPVl92r7eVGoMGJqsxTn6MG-UY9zYZFAjOQDfY1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=K049TxKY4dudeQm2g7HCyr6yICK5hgoFgQjVekBZkSQwy2yV7AQyTW4-2cIHbuZ5f70cNoChSRYL_4yZSSChyEiQQflCuLeaTD10JsGS5ox3L_bnJeVn_SVCwhWmXm5sp-EZBDXR-VmQKpltKSi-wzwaNsThwbTBJGpCSUDcT744USbfN-j52wv47oV79B-EWH_L34wr5L56BSxwSYJQvvFl3OQW6wb6rzy1wl2PxuPFI8Fx8qBf1lWFXg_mEN1P0ax0NBroQ0T80twPvT-8uuKCC6zMOvaMk6oJOKMaGD1mWRKPVl92r7eVGoMGJqsxTn6MG-UY9zYZFAjOQDfY1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب و آب‌گرفتگی شدید در ایذه
🔹
بارش‌ شدید باران در شهرستان ایذه استان خوزستان علاوه بر آب‌گرفتگی معابر، ورود آب به منازل و خسارت به شهروندان، موجب قطعی برق در برخی مناطق این شهر شد.
🔹
ادارهٔ برق ایذه اعلام کرد که تمامی اکیپ‌های عملیاتی علی‌رغم شرایط نامساعد جوی در میدان حضور دارند و مشغول تعمیر تجهیزات آسیب‌دیده هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/466146" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYMtuWGBqmwfOKLUSOxZcSbwP7yJVdc-RGGr3u0s18ICR3rT4W0eIxuEokiLXBzsUpo1gh7VQ4WH65s4beP9zI-fe6qDNGvUfwZ83pQdiYUlpVL7dML_dPdSo7QXNUKomb_ZKZgf4zOSw9sGCuwAz5jsfcoiPXDuftfP94-lzG3x0SpXdR7rfRr-lPiFkbhNC5-G5Wj-FYWSkJBCssv3vkHk2qt3QUqOfSTONyQoeeeRwaY4JMPBmaZqyMShn19Ioj74sPdcdoeUbWDq56lV2iS06x390zi5mktJv1TpVv1Ks9jdnfWKH8VB9jAjT1nstfbSIU_wA-IQkcRWml8HYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1_3_Y9eye0LNWeYeasYJFKcjLZnuoTDCqf8CoIyiXMwUEOqxb1Pl5i1riUkPcOO1PmKt26jz3xnUuVnX-G5kB4ewNp6aqjtPc6Q71RlObk4AQ48xztViF96D65ltbj0j47I8a2dDVtvfKhXO6rvVftOf2UqMiM4g6p2P2GwWKj5CojLwviPw3-MqgGmf-rrETXBAxJarGuIJJxKlft365Gr1Rfm5islGktVALugM9w-OrGh5KeFj0kxOuAHIW-ahDvVEGH78gz4T-IcU5BGXwE1_fXIS7y8Ss6Z0I0FXQ-BRESRtdp2yl6jXW-C42uZywK67GkPtm1q63-Aw4G22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FN-abKFHLs8cckIPA_k16TNeLXSi1bWeHDh2J7p6PktARf7PEPlFiYtnWJ8O2YbsN5YgQXw6-3RrhGWkxDtr_uLbJLoUAbhbjPqISJoxl0g9zSYZbRbQc0f2eI9-D1qzs8mZSmIaaTib1p7NXX9rGQ9zowAUvnG9RFdiwWU0fY36DrbJRYIZw6xIu8TINcMnkO3kmmzYiB2-i97H2qoSE9JlFu0l9FjH0KD7Yte9AzPRp7BBW9pV_z6SeOaXE7SfeKpNCbkinBrjSMIfHB33M3y7AfbZeKNqJ_fyOZCvh3pIZk1SzLUVqd-ek7Lit2b3Rs7Ilkjovlq8A7crHtcfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERu3efl-cbWxmeYTBrSYzLFNe-POE0iAq4ZfhOJmauvKgOmDfwpgOjP5is6-JaPVzImjyRIy7PdNUBwBGSeVCS_xkrs0clwp0v_Pk7m5OEbWGZ1LFmQqGfQ53PXscTm_ccEFenrAW2k_7WqSt8BS3HecKevnTIm6dvujithUuoQlJKQPV5Cktx-xsixhvfTq_Ue9sv3UzOqV-qiWngUiGHkTFw5zw-RwMlaB2tBxzdPm6Hok-Fa26AbMyQFlCjCUflirpzXmn358pVANI5RGa-QoA9n3P_OnP5M5yqMw6EiWfqlA1qAUP2F-f60t6eZ2lPwms0DWOoIybG1IUMopNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر جدید از خسارات ایران به تجهیزات آمریکایی در عربستان
🔹
تصاویر ماهواره‌ای جدید منتشرشده از پایگاه هوایی «شاهزاده سلطان» در عربستان سعودی، ابعاد تازه‌ای از خسارت‌های واردشده به تأسیسات نظامی و هواگردهای آمریکایی مستقر در این پایگاه پس از جنگ با ایران را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/466142" target="_blank">📅 00:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466141">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۶</div>
</div>
<a href="https://t.me/farsna/466141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۵ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/466141" target="_blank">📅 00:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466140">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1LPVgbucWoO6QuNXzOqJG3DWpDUyRXsBkFvLJC7Xmb6ZvFJN0vcLZE2jMXr3M-2W-MkAOqSD_9Ji1vHDqLTZOlcq7bDnzNtNIchRdD7hr5guMzE0_NXfJ65yOrApIX8H2yQVYet-977vouP_ZvXvsUcRu44uNwt2ChYgAHs7SbKXmI6k_fdiSS_d2u6ueSXow2-aY2cZmtPqCeonw6WAxTYmrn36bUyjc3U_ChqEyZcTPg7aCNZ8p9_3mBm6SSOP8YI7EYhkbNmGVQOHRPTXlRdiNT8J9e0X6JOKJTXoLOo5SDepSALBTe85ge8P5YD-SQjbGpJcfd5aC64ijmQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرنگی ناشیانه
🔹
مردی دندان‌درد شدیدی گرفت و پیش دندان‌پزشک رفت. پزشک گفت: «۲ سکه بده تا دندانت را بکشم.»
🔹
مرد چانه زد و گفت: «من بیشتر از یک سکه نمی‌دهم!» اما چون دندان‌پزشک کوتاه نیامد، مرد قبول کرد همان ۲ سکه را بدهد.
🔹
با این حال، برای اینکه به خیال خودش زرنگی کرده باشد، عمداً انگشتش را روی دندان سالمش گذاشت و گفت همین را بکش! پزشک هم دندان سالم را کشید.
🔹
مرد بلافاصله داد زد: «وای اشتباه شد! دندان اصلی آن یکی بود!» و این‌بار دندانی را که واقعاً درد می‌کرد نشان داد تا پزشک آن را هم بکشد.
🔹
کار که تمام شد، مرد با نیشخند گفت: «دیدی می‌خواستی پول زیادی از من بگیری؟ من از تو زرنگ‌تر بودم؛ کاری کردم که دندان‌هایم را دانه‌ای همان یک سکه حساب کنی!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/466140" target="_blank">📅 00:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466139">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5QLzNPl7oV5-fpkdqqXytFUY1oqrjfAjOfngT3gMEZB4snnOAN_4HKYLmvDUR4Ueh52eUIQUrzvhF31cN3rkFsKS_fyEUA22eHZ72gJts9gv-u2O-gmwmJWDTrY3v30FyFZte5EOpDhOdm52aF0ZJ0mzTEEw9BeQMk3TgsINm7eaeQ54oUs7Ogjh3X-4jdHUj6RIrSm52HZUDhwNxXgzqeal6E8sWpMhpVKtotDMw8N6MyayFD8sIMc9fKDdtJGwI-jZXu_Nl0Yj2j13ICzT10S3NlznclIiUaTcFyQSRIW2IXOJ7prGzpNEYk1df-0SuG9o0hW2_EXjMBP9vxbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/466139" target="_blank">📅 00:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466138">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-text">🎥
فریاد خونخواهی‌ مردم شهرکرد در زیر باران
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/466138" target="_blank">📅 23:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466137">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP82H9Ike6eM4bLLvrpCGCumn7jR4E2tKlz4VpYkKAk_GANBxsmcwemCUncU-QM2Oq6ntlyoPXRFhHyN5raBjURNbFT9X59w4B6SgOLoPvSTJWn0DkXZJ8fLxr_qiktZecAUDBu0jsHCP-DIKH7H6oDd7tAXPHY7nrCDrmpxE4URBK_IFkESkzxk7HVUQ8A21Zvcoel-wSqI05Ek3ffEjqe7mjI7P9572CfQonQAXrwDcczjuo4qeoA2csXbxZg_1y-G99LDEm-5iB-on2aMPi3rgxZD4KmO0UmT3E6BpgmPWQVPzm3EVglUx92tB1IsF6tlPZLulTckHRS4VT8VXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح «تورم صفر» با ۱۲ قلم کالا آغاز شده و قیمت این کالاها ۶ ماه ثابت خواهد ماند
🔹
برای هر قلم کالا متناسب با بُعد خانوارهای تهرانی سهم مشخصی تعیین شده؛ برای نمونه، هر فرد می‌تواند ماهانه ۲ کیلوگرم برنج با قیمت ثابت خریداری کند و خانوار می‌تواند از میان…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/466137" target="_blank">📅 23:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3b281464.mp4?token=P0HrWMs8z1NevSKGuocqzOnGg8x5WoZF9RL_Tm_48ojg-yuNZi5QnIa6pTN7wO9TpbnUmxQZVEZ_-P0_gu-H7Vnv2hai8p6GD9wiGkez0tT0Q74Rs9uT3jq8A0S_jISDCSIL_aUJU7aZsoI46AO7xXXpv44ShCJPLiKyNAHevHwewgWBFoqAHf4zXOPOPYjND7Sul71DZLKlz-NYYjpk1bfJhLpCzRFIS8Mib_INIInEVintwvtc1LfMszsGAnSY02w5c6UYU9EscgHr0rxT5MXOx7EP3US459mO5bch9wlglnWsCMz4x6ADYAcINnB807UqzvDaimtXKqcOtLFi1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3b281464.mp4?token=P0HrWMs8z1NevSKGuocqzOnGg8x5WoZF9RL_Tm_48ojg-yuNZi5QnIa6pTN7wO9TpbnUmxQZVEZ_-P0_gu-H7Vnv2hai8p6GD9wiGkez0tT0Q74Rs9uT3jq8A0S_jISDCSIL_aUJU7aZsoI46AO7xXXpv44ShCJPLiKyNAHevHwewgWBFoqAHf4zXOPOPYjND7Sul71DZLKlz-NYYjpk1bfJhLpCzRFIS8Mib_INIInEVintwvtc1LfMszsGAnSY02w5c6UYU9EscgHr0rxT5MXOx7EP3US459mO5bch9wlglnWsCMz4x6ADYAcINnB807UqzvDaimtXKqcOtLFi1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب در البرز ماشین‌ها را هم با خود برد
🔹
درپی بارش شدید باران در عظیمیه کرج، سیلاب ماشین‌ها را هم با خود برد.
@Farsna
-
Linik</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/466135" target="_blank">📅 23:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICKA-4E110HRuujvDdkWhY4yf35jRF455zbMFFsUagkXO8OCiVi_XNs_S7xDxUXcLKJ0GT-uEzJ6wki88fTmCJk4qvn-O456twJVt19w5FjgmBTMB5ApgOk1s2qIUfcDjDhp0L3CAbevB-p-4zD2L-9M-LmRQN7827SFASo7Yrqbb7cHU5xG7o6IPw7peUsZTSfWXrYAUWJGaRNOINizG-ukZqgQ59ym2uok42ykNnbS1ElkZO7v7CBkabcXTx6vX7MPSfiKWmpHAyYRaXEZBWT2Eab5ZDjwS4mZoSsEAoUrIlDBGJ_i2T3vSPyL5XBoSDfLmmbCFRv8Euooi4PV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناکامی صهیونیست‌ها در ترور جانشین السنوار در غزه
🔹
ارتش رژیم صهیونیستی از ناکامی در ترور علی العامودی، از چهره‌های ارشد حماس و فردی که رسانه‌های عبری او را جانشین یحیی السنوار در غزه می‌دانند، خبر داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466134" target="_blank">📅 23:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73c4ab7fe3.mp4?token=u3-E-YlgVSG0dIpt3q0VJ6LT50yRefCOS0LRh0IpnBRsZ49JvMU8Fu02xNtklB5WmxOxX4Qx-iia784YuVHAA_Z1NybS87gtp6HbupIRUGK1qmJblgnPLqzF0r66qrOzbmk_tFFfzgvxIZav0loTQWPBeaiK8wDsNof75LDMEziwU3bd_ugZZH3qcY-igvIRR4Sb-dntbh-dkDpivhAaGkzauiAX5_1dpskzpFNTeoPy4ekviMNXSrUHTpHhD7I0wxjdOOLnZSNJ5o018d3llmV2sgdaH8d06JyN7ZY1KgTpAZlyrZDIdE8TaLka-xyUiZZj8hT2fwz29eR1067TMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73c4ab7fe3.mp4?token=u3-E-YlgVSG0dIpt3q0VJ6LT50yRefCOS0LRh0IpnBRsZ49JvMU8Fu02xNtklB5WmxOxX4Qx-iia784YuVHAA_Z1NybS87gtp6HbupIRUGK1qmJblgnPLqzF0r66qrOzbmk_tFFfzgvxIZav0loTQWPBeaiK8wDsNof75LDMEziwU3bd_ugZZH3qcY-igvIRR4Sb-dntbh-dkDpivhAaGkzauiAX5_1dpskzpFNTeoPy4ekviMNXSrUHTpHhD7I0wxjdOOLnZSNJ5o018d3llmV2sgdaH8d06JyN7ZY1KgTpAZlyrZDIdE8TaLka-xyUiZZj8hT2fwz29eR1067TMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از حضور شهید سیدهاشم صفی‌الدین در کنار شهید سیدحسن نصرالله
🗓
به مناسبت سالگرد شهادت مجاهد شهید سیدهاشم صفی‌الدین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/466133" target="_blank">📅 23:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466125">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0VRECxiHeKn3Jwe8DQ70PGLUau94Dh9kn4OY26gOstJ2Tp3aGW4_P5zTRbdcJPtwafnWOkb9hA3vw_QweOez5skrTJKY1469G4naxSPB7YHHRYEeSyPAyp545Ofwgn_uUSqpvM4TnkaDkPOXd-srW5-9QhZrBJkM1dn5azQKh6RDXjVGo_IpXxQCpmu1EBnZCLWbNDUtS_RcYLU4BLeCZa3SB_XE_goL6KdXZXzW3-HYVQhJYHMpTSWjV7u_HG5AXOoAMiktu9EoV2Q-P7PuFH2CBbkfAardq9_8_sDvho-YWqy4ZXhck8LiNWR2e8PBxKYeARnUpBkZtyaifaB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBS3KUYDpDcuCMsVdwW-7tjRdOp4rNzdOxm2eiNcCDOzXyyLb55mytk67jMgjiPn1Fx75y4FwEO3YoIyw8D1SZ25AshIEc0G0CMI4AHmkBpxZC-MyAXIfuKuP1bDvap8ji0Wlvt7qmkfQLl_RkQRj7MEukGy9nn6hTduRoulXZqvdBDfAXlwkkp9XC8isvndWIMVoB7lWaLWZp6qbGIHJGuRem1q6GBl47nio5AFjJunAJJGyIIOS2a2fsCRLuE8YNPuGuqdlTtv-Uv84OUDsBq1K9KPixunrnQqF-_mfUFDsmNZMyR4oTfWtNH_zleiqESOK-McOlnByVJ_merITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9-b03muA9gVg0XJmuprm8Ip9tkpP98QUbI2vy29SW_N3twN883y0ufPOfuqOSfHcsk7A7VKb7SyYWwBdrnzQOHdJLdrxOlIz-sLXo8GpVUbIeFbkAMVxV4HQd-Wmfj3TbtkprJNyaExAZg39TCk9owp6PZu3FJnlCJ1X2C8I7Mpt2M5ov4FtANM-BC0a6z9Woqgt21OdfT_SmaOoBJOSAPI2DdS8sUCAcmhbtel55-QaNSkGWn9CxRn5m2piDxUFyGrT92pKNHdjLcNdiukW6tiJtIVqH-jARd7JuDBs-G2q4uris8yBTIL4hwsPgsQGeaec1zGCSseOwPE4GLIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtDy1n1mbQqG_qtn7a7VJ-70nzQNMdbRih4EeMMBk9YGnjcNeDAItmAWRt6IQ5XQOuzIw7bs7VwXf5bKRixq7h_SH96V3JEXy9yRbQ6aUOk5ESQjaB1h8Bx9bcZC-rLtMUKWnwmAbpN6SCudV0pGMSICRxJJ4GoFhhc26te05vA5KHq9bAhsOesvqqnMrf5jKj49tzhHcnkr4QpC_Js7ZebrbauLYMGOF6pGoeUbDl0g68Vhmpd7KpQPHSv05bLDNX6df3XBccGXI5GAX50mHaEXzdMbmkNyli6zKHea807pwcmkqz8blg1WdwuQbrtYIvJKDHgUB7yXq7juuJLinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9nCxYL3LctS2xbLejnrchoLkaeDUdbxkwX-EDBEra4jUzRoMf3tEXPTkf-KorfHfMdiG5feNtsHjUIvl6ea5vxG6BO0-wRhqLP7p23Wya1O73p4r4TzitUUxKFKfQE4eL79MeOhOkFaszuvUoYUfZRYq8EkzM2On1szgzRopMkjkdyk2WUTYOo8GWDh1BzXvZcjEZdIVWMfoRkE-_S_UQV1trqe43Rbnd_T8xSgqgli-TJ85N02C3dPBEpSVZktRHg1h3pvt4P8RDmAwIid3LgfsRDyHaleU7m6sDh0RplmWxLugKvoAPVfi-BncneOoFjJp36HiTxUTsX8BDgEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCWSRAj7qPDuFF1KUTclAvcbbLhj-KO8LLtnr_qLeKaM3F3CaDA95BqDRWPan2yk7Veq2usW5ZwkcqRVicY7O9n8gO5hWty8RKdGON0arDRa-83Zmu_ckK-244m2AscMlFXN9jh-0X0zBZfHN4lKduFYaoWj-tgm8pklFwoH8b3oyQNLH4NMoNsT1ltoJcRsweTQ59Y5VrDMv9Dmn64OPkTQXg38veygM3n3EgoZzPP2SvhhbQKfYcYQx1Myyqne6ESZuQBrPPVVWKFpjWNexwDJ-KaJE0DJkjcBJPcUThh2cgr5s_QJbvbK31kNbEvk0GR9Vu6PvWmlP3ALhR-hEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyVx3CLTGZmzZvUCXXlTEA4wV6KDC-41gA6T71c_K5fDLxPPnXQuMS-LKSJcNpe0RDxyIhMBZAaB-mkiGfmP8B2CjdNLU96lso0fcyoaWQYHXWN-XLn8SoY54DyZy6ZnRVb1W8j5eS0WTgO7O05Fj52jOND2xFAmTGj-kyLLCsl_lzvKEEGfVNraX2lLcnIkvtqNNvOPCNIgr9JjJxbtZiUxOIrd7o5kgnJXrikiMuz60Hia3bJMoIHanFdR3FmAjIGuGFJVr4KE32Zx3A905zzIQNuxWTrz1M4woFIZmumwpaJoqfLEX6WDT_OIZN9WUhIz5T-cp7QZysFm1xCC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGJJ7oMpEeEwYged7hqeIdY-M-1bXJwe598dV_XWr5ucQCeQaqpTzsncKYWb7EYdr1C-TwZ9VcfgBPbAJUCR8Wwktq_OVMELwCd-soowl-EhnJ8ewXRop2s2vIuZD_GhWfeE-fYLOBeITSfYEOhsG7v0vJnUV7K_zt8JsehUR8QO_PIXbjdr_ACA6I2iliHcuywHmEtotn6Bbz8jxuTQibBBffPbbRBY2AB49DRXGVa1Z_vQRhcXFdlxeOOHNyZGG1kvt_JrVxWyza4vAcfbxb4vWyVdOAm0PwZmq0f_7zG45Dg_NbVTjU4fnSYQfbtNtaFouM-S39rGmGc2I_pfiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
«میدان هفتم‌ تیر»، دومین پایگاه آموزش جانفدا در تهران شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/466125" target="_blank">📅 23:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466124">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioM4iTm3K5wX78ylnVScA2H3buUXt2KRarVzfqyEI5YFvNuH4kK1vyaTsQvEaGtfzIss6uNffY1yVfhOFB0faCleUAy5TzAi21f0yV-8-f9l4Xl9WHLXBndkpCRRX5o4HcK5PR15o3wJOHvb3eJeP2BMla6taN2gHXu-Ow7-7nVfed1WNlUl1I16wQVoQF3GbiwDbHKIai83uRYHQtGSCfdwuupl-4geKLWIwSrPBIqt_7r4tRJfsVPhsGw1-G-OuaAxzukNkT9w7onqzuPDRjKIGhx7kAb42JpJi1PVS5TAxtGAamth_jCmUaKSrfLuAOzQgpoZcT5W7beRDCllag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرایش جدید اقتصادی دولت برای مدیریت شرایط ویژۀ کشور
🔹
در جلسۀ ستاد هماهنگی اقتصادی دولت، آخرین وضعیت بازار ارز، بودجه، تجارت خارجی و تأمین کالاهای اساسی بررسی شد.
🔹
در این جلسه بر ثبات بازار ارز، هماهنگی سیاست‌های ارزی، تجاری و مالی، مدیریت انتظارات و تأمین…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/466124" target="_blank">📅 23:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466123">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123aabdba2.mp4?token=JQhndHwHZwBvM51Wv02sY0adHwMSizNvSwXesRl8IBcI_kNhY-2XSU_9xL-K83e21T1Tfj97NMzCn1Qy-SMn1rhjS_Wtom1JTxefiGK4cJNl8mFmuZ7Oy4rQyWAAXFP4aeU0Uwu_AxDFw2QxPdwJ_RGs_1aYmZhfjFao6S_JYX5bIg5ozGItM1xqr5IREroekHgH0SB4Gyf7kka0w6WPx6eSUDkXJCAdqZ108nWQC8irhGAK5Wo_O8Y3abFgWQ7K66QQY8YaDMdDBYOMpAq1hdSfKOjlMBMTOmRfHqq0XKQqfsjWHUcR62fhB2XQ-ffkkAlYQ7Llc6sXgkdsubQjaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123aabdba2.mp4?token=JQhndHwHZwBvM51Wv02sY0adHwMSizNvSwXesRl8IBcI_kNhY-2XSU_9xL-K83e21T1Tfj97NMzCn1Qy-SMn1rhjS_Wtom1JTxefiGK4cJNl8mFmuZ7Oy4rQyWAAXFP4aeU0Uwu_AxDFw2QxPdwJ_RGs_1aYmZhfjFao6S_JYX5bIg5ozGItM1xqr5IREroekHgH0SB4Gyf7kka0w6WPx6eSUDkXJCAdqZ108nWQC8irhGAK5Wo_O8Y3abFgWQ7K66QQY8YaDMdDBYOMpAq1hdSfKOjlMBMTOmRfHqq0XKQqfsjWHUcR62fhB2XQ-ffkkAlYQ7Llc6sXgkdsubQjaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/466123" target="_blank">📅 22:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466122">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd1b422ba.mp4?token=bVTepXLaSQlIgP68qrFASErGB9cFOB_JrS06w_vTBWp2rZYwXTgs1Q7b68a0PLBMeSFTjBVaU5zq2yLTdH7gM7vN-0YVG_kHJJIt_GzAz0R_90ESaYow88apPVgUfH6L4yKFf8-9DYqsL00-ZBvJszn9yEWqdJQzdwqkv03O1imLX_LDJ7R_YvKsjM2HiLviHf9Y6q0pg_1s_Q5MtfQrrBK-LVug6yr-33hwjA5vB-KODRZPfpEwkkP54jdL6NdVjzi0eSMlO0cC2vzLvXFJ2IQtoRfAChVQrjbd10-mRYOENz4XMdiz56cF9jC0uK1tgKXd2qZ8MhsNwIVPXGwEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd1b422ba.mp4?token=bVTepXLaSQlIgP68qrFASErGB9cFOB_JrS06w_vTBWp2rZYwXTgs1Q7b68a0PLBMeSFTjBVaU5zq2yLTdH7gM7vN-0YVG_kHJJIt_GzAz0R_90ESaYow88apPVgUfH6L4yKFf8-9DYqsL00-ZBvJszn9yEWqdJQzdwqkv03O1imLX_LDJ7R_YvKsjM2HiLviHf9Y6q0pg_1s_Q5MtfQrrBK-LVug6yr-33hwjA5vB-KODRZPfpEwkkP54jdL6NdVjzi0eSMlO0cC2vzLvXFJ2IQtoRfAChVQrjbd10-mRYOENz4XMdiz56cF9jC0uK1tgKXd2qZ8MhsNwIVPXGwEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: حملۀ تروریستی اوکراین به کشتی ایرانی محکوم است
🔹
اوکراین دربارۀ این حادثه ازایران عذرخواهی کرده اما نباید به این عذرخواهی اعتماد کرد چون اوکراین تنها زبان زور و قدرت را می‌فهمد. @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/466122" target="_blank">📅 22:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466121">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6073a1e14a.mp4?token=skHTaQ5VArM1q36g0eDjxKAECkQCrMIXxm5SRkiH7RrXPhjtZS5aa7YkH-GXFQr6BYhB6iUm5IpY6qQKfATvva9YAr2tX0BhbVoRqDtlQ5i-aYnQTK1Il5Wn-sm7U5RdJvlA6yrPehWq2zdybGGmh0fUdSpz_P76IzRuygM7Onrw35yKkJpEIT_D57Osig3gZzEx_u3Ws7zY2UvaaVPR_PBQ0y0CIE5GqGiLgyf1ZdqVbh6kX7ABurC89siZB-2bX36H2pQzStoIr9cqCZe4fYq5FI8k2rgqh4vcAByWMKTjEVcSVLb9C_JpP38-NhXiK-WBV29DB31JB5-2PU1pAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6073a1e14a.mp4?token=skHTaQ5VArM1q36g0eDjxKAECkQCrMIXxm5SRkiH7RrXPhjtZS5aa7YkH-GXFQr6BYhB6iUm5IpY6qQKfATvva9YAr2tX0BhbVoRqDtlQ5i-aYnQTK1Il5Wn-sm7U5RdJvlA6yrPehWq2zdybGGmh0fUdSpz_P76IzRuygM7Onrw35yKkJpEIT_D57Osig3gZzEx_u3Ws7zY2UvaaVPR_PBQ0y0CIE5GqGiLgyf1ZdqVbh6kX7ABurC89siZB-2bX36H2pQzStoIr9cqCZe4fYq5FI8k2rgqh4vcAByWMKTjEVcSVLb9C_JpP38-NhXiK-WBV29DB31JB5-2PU1pAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: این‌که کشوری با تاریخ ۲۵۰ ساله بخواهد به ایران با تاریخ چندهزار ساله دستور دهد، عاقلانه نیست  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/466121" target="_blank">📅 22:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466120">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8cc2ae01.mp4?token=ixYyQxdvt35UVBZhkIGhljQefaQNk9Luk-dF0OH5wWWAOm8Y4VgldD4tuzgTid0FoDb9jsRP3PZnbJ1FXs_amj2ms4DVVZKGoIsblnLAuGVjdeBd7yknDwK5943zi0HCKLmfQXeqbyKXiJYMuQhjdNDckP8p4J5oZ0QRMcHE4stwJh2zAOzAR2E-JZpmN6WuihJzGqQbSLmlaEdDICc-5fZ9eV4V67-GvtqEZJz8ePpLcJoKcVfle6AXLAlGy-TxHaBIsziHkuf1ixwo5njgCcJc21qEzWAoWtCyJz71vXrnHmQ0CPpTnPAtDLQtBQ-00iIfp4wIrvRhWv42zvm9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8cc2ae01.mp4?token=ixYyQxdvt35UVBZhkIGhljQefaQNk9Luk-dF0OH5wWWAOm8Y4VgldD4tuzgTid0FoDb9jsRP3PZnbJ1FXs_amj2ms4DVVZKGoIsblnLAuGVjdeBd7yknDwK5943zi0HCKLmfQXeqbyKXiJYMuQhjdNDckP8p4J5oZ0QRMcHE4stwJh2zAOzAR2E-JZpmN6WuihJzGqQbSLmlaEdDICc-5fZ9eV4V67-GvtqEZJz8ePpLcJoKcVfle6AXLAlGy-TxHaBIsziHkuf1ixwo5njgCcJc21qEzWAoWtCyJz71vXrnHmQ0CPpTnPAtDLQtBQ-00iIfp4wIrvRhWv42zvm9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: آمادگی داریم میانجی پایان جنگ بین ایران و آمریکا باشیم  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/466120" target="_blank">📅 22:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466119">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWwMnCNsfe1s6Nam_LBu6Ndv8BUulXu-eQM9XQ8rsmi4Qihj4smpxBZqlZANF8NldeqSyR3IfBV-vkhN7Sqxm_KnZT1bmCplAWXOyLmFtW7PLMWx_QqJ0pvHHeuVfPG86jv7sCPF1F5K7tZ3wH4OyDRImsJOubxOY4pFU7bYvKjNWrnqnnCG1WvqItx52HHqFIc3IRJ61sbk73ytHAhrdw1jt4eC-KvGBvjKK-dJPaNnXxUWeomJlY6LqlWYoCQvGpnQqD6r9ZdZ51l5t97WuUSwt9zv-GOpkryyP5IjCz9FN971cff768d6yznscyvdw4zPAw2_WXpNO-hK09szWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام رهبر انقلاب در پی شهادت سردار نیلفروشان  بسم‌الله الرحمن الرحیم
🔸
سردار رشید و اندیشمند، سردار سرلشکر عباس نیلفروشان رحمة‌الله‌علیه در حملات رژیم خبیث صهیونی به ضاحیه‌ی بیروت، به لقاءالله پیوست. سلام و رحمت الهی و اولیائش بر این مجاهد فی سبیل‌الله باد.…</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/466119" target="_blank">📅 22:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466118">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135a3aed0b.mp4?token=qoCp03DNFA3gSh-FLgh1dXa9Wn-yGUOz9i_ziDxQQOZpK4NCPISvchCx62r-FbV3VWIFYgj7QOLNkfvHdzfi9ekFbvQabaIFKF6D3SeE4hsJlWC2tVD6qk2RptFycEQ8bkPyWhQBTLsUU1H0Rx-8O_4Y_Zv4SmdxaD8aPm3vxjHFo_HBUpumD3mPH-AUeSUw5gCbzWG6AM4cS8qYNBE9meqpYxTMP307_Xf7fX7hTZ5pOpOntMl1XBEx1K6SsbMXoFZEfgCgWskGion5uipTPSKtggjbu3LQatxo1Mwl0VSygsF0trjr9kUZmtcJCQrfnrxIh8jF-HYfwVPko6sbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135a3aed0b.mp4?token=qoCp03DNFA3gSh-FLgh1dXa9Wn-yGUOz9i_ziDxQQOZpK4NCPISvchCx62r-FbV3VWIFYgj7QOLNkfvHdzfi9ekFbvQabaIFKF6D3SeE4hsJlWC2tVD6qk2RptFycEQ8bkPyWhQBTLsUU1H0Rx-8O_4Y_Zv4SmdxaD8aPm3vxjHFo_HBUpumD3mPH-AUeSUw5gCbzWG6AM4cS8qYNBE9meqpYxTMP307_Xf7fX7hTZ5pOpOntMl1XBEx1K6SsbMXoFZEfgCgWskGion5uipTPSKtggjbu3LQatxo1Mwl0VSygsF0trjr9kUZmtcJCQrfnrxIh8jF-HYfwVPko6sbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: جنگ علیه ایران فشار زیادی بر مردم آمریکا وارد کرده
🔹
مردم و رهبری ایران در شرایط بحرانی اراده و توانایی قابل‌توجهی از خود نشان دادند. @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/466118" target="_blank">📅 22:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466117">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1652d66fe.mp4?token=QKP1QqKOoJUw-FEZzPSDgbXC6ayBI7LvPkhsVzDmf9Z-FoOklhN--msKgsDkMQAZmzliyBvBpFLs_uK_uoEFdCGTL2CT-ntV1YFeH8IDBll0d46yQfO7A4f8ZpC9x7-Dk3XXTnYkO7FzAJHpdeCdsBizcG1qwfkhogBXOYr3MaGzzL2Yxjve2dSxhIuT4qBSaTYNKIzbL7szoBNhvqarEJG_8NhRYzwCL8A2sh4CTFgp9ypD6ziShbm3iN4rxnhsqBd3P05Uuf5gBjxGWrCJpQ9MoqR1lVomcANt6iGOdwOGHQsgr1nSKVU49rCseBQ-6snfXmk-sXhItfRAx89ztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1652d66fe.mp4?token=QKP1QqKOoJUw-FEZzPSDgbXC6ayBI7LvPkhsVzDmf9Z-FoOklhN--msKgsDkMQAZmzliyBvBpFLs_uK_uoEFdCGTL2CT-ntV1YFeH8IDBll0d46yQfO7A4f8ZpC9x7-Dk3XXTnYkO7FzAJHpdeCdsBizcG1qwfkhogBXOYr3MaGzzL2Yxjve2dSxhIuT4qBSaTYNKIzbL7szoBNhvqarEJG_8NhRYzwCL8A2sh4CTFgp9ypD6ziShbm3iN4rxnhsqBd3P05Uuf5gBjxGWrCJpQ9MoqR1lVomcANt6iGOdwOGHQsgr1nSKVU49rCseBQ-6snfXmk-sXhItfRAx89ztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: ایران بدون سلاح هسته‌ای هم توانسته پاسخ قاطعی به آمریکا دهد
🔹
تنگۀ هرمز یکی از ابزارهای قدرت ایران است که امروز به نمایش گذاشته شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/466117" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466116">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEEUo3cCY3egEaDvpI_dxvTMd2D6SDMyqOpbb7DdcY1jovvAO2zurX2iTQub72w9aT9rDzMDeZfTafLQWmk7BmQ2fDdvqyImB0ZIJE0zyKHF6ylBR2JYK00se7uwY_fLJUNTwmbQZeJeaRkWh1_mTs5VHnrJ-7-EAgLouCqqTJwQQCTMwzWx2PO36QPgM_R4Ur0G3zAQcrPIhd6qNcjh1CXWInXk4r1G0LzvG5t-annVtvUl-EDosxwBtt4VGadEzKd1wQVwouVxco67_TMhGEWskIggE5KiAxbPB_ZfxwDJrQ9-m2R_zlHOz4pVQ9JrJFNSI2Mfzk-t3Xtr0u8rjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام ترامپ در شرکت‌های آماردهی تردد از تنگۀ هرمز
🔹
برت اریکسون، تحلیلگر حمل‌ونقل و امنیت انرژی، با اشاره به تصویر پرچم شیر و خورشید در پروفایل «همایون فلکشاهی»، رئیس بخش تحلیل نفت خام کپلر، نوشت: «اگر کسی بخواهد به دستکاری داده‌های نفتی فکر کند، کپلر…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/466116" target="_blank">📅 22:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c2d626cd.mp4?token=ltgSWvj5ynzNpF6A1OF9rsXKh89kocWRFmsODp1B5nR_mz_4mCekJezaKRWphaz4iJDapc_U-x9SceiA0gFA1Uo76vq2hZLIBNw-rR82Td3UjRk2fV5KY551mReBcXuXtzfXpYlDxDtxRogJ9h9fP78s6ds587qFhzs_MqSw2xc3EdDrqqtCvoBxK6eAYw4SwWIUs2SOUgqHtdoy46aUfBkdwj2PCQzl8p9_HWIxdrY8z-QHMreCgtmjR8ds7-RIAm7MXCJzOaiMTInbKgYERK9altQpN2teRVjVnTg9fwyBsOkvlodV8wlhHSLLjp7J8TP4ZE_P1FPqEgyZ1E3uag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c2d626cd.mp4?token=ltgSWvj5ynzNpF6A1OF9rsXKh89kocWRFmsODp1B5nR_mz_4mCekJezaKRWphaz4iJDapc_U-x9SceiA0gFA1Uo76vq2hZLIBNw-rR82Td3UjRk2fV5KY551mReBcXuXtzfXpYlDxDtxRogJ9h9fP78s6ds587qFhzs_MqSw2xc3EdDrqqtCvoBxK6eAYw4SwWIUs2SOUgqHtdoy46aUfBkdwj2PCQzl8p9_HWIxdrY8z-QHMreCgtmjR8ds7-RIAm7MXCJzOaiMTInbKgYERK9altQpN2teRVjVnTg9fwyBsOkvlodV8wlhHSLLjp7J8TP4ZE_P1FPqEgyZ1E3uag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: جنگ علیه ایران باعث شده کشورهای زیادی به دستیابی به سلاح هسته‌ای فکر کنند
🔹
ازنظر برخی، دستیابی به سلاح هسته‌ای می‌تواند تضمینی برای جلوگیری از درگیری‌های بزرگ‌تر باشد. @Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/466115" target="_blank">📅 22:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۸ مخزن نفتی آرامکو در آتش یمن سوخت
🔹
تصاویر ماهواره‌ای سنتینل ۲ که امروز ثبت شده نشان می‌دهد که ۸ مخزن کروی‌شکل که در کنار مخازن ذخیرۀ نفت در محدودۀ پالایشگاه ریاض قرار دارند، درحال سوختن در آتش هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/466114" target="_blank">📅 22:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466113">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726689bb06.mp4?token=c3mTrBMFQ_GqhfRBssEgTQbADTr11MAmETPfnubnoLbbO3NnHsABmQ6kk5r0tlwox4WL1dchmbW4F7Dlo7kKfaNyLREkdjyQo9USesOIcEzHseOTw-u_UlHsCtPO_Uh6JLadtT35LdfKb9qju9tXvkWMS_iLAfH-xmfILhil7TF0uYh5lRmWfDXHMIqhJ5INa3-TmSUFj6mNVQAgBNE5o0-TtUl0nfd9SanCo5rUpR_4_AdsF3_DWnQDJF9GQYvtN7smqvfUYD0oaUenoNp5R_ynbfF2ZTnhcZM6ERJyXKvHOdbCbUqWKyq8I1CuZvNVgiwyoeExHouUbneISpITyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726689bb06.mp4?token=c3mTrBMFQ_GqhfRBssEgTQbADTr11MAmETPfnubnoLbbO3NnHsABmQ6kk5r0tlwox4WL1dchmbW4F7Dlo7kKfaNyLREkdjyQo9USesOIcEzHseOTw-u_UlHsCtPO_Uh6JLadtT35LdfKb9qju9tXvkWMS_iLAfH-xmfILhil7TF0uYh5lRmWfDXHMIqhJ5INa3-TmSUFj6mNVQAgBNE5o0-TtUl0nfd9SanCo5rUpR_4_AdsF3_DWnQDJF9GQYvtN7smqvfUYD0oaUenoNp5R_ynbfF2ZTnhcZM6ERJyXKvHOdbCbUqWKyq8I1CuZvNVgiwyoeExHouUbneISpITyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدودف: پروژه راه‌آهن رشت-آستارا که با همکاری ایران و روسیه درحال احداث است می‌تواند از موتورهای اصلی توسعه در منطقه باشد  @Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/466113" target="_blank">📅 22:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466112">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52eb8aced.mp4?token=HXeuBXkE1JA3_exUFm5jvQfVR2a19_cWE8K8tl4NtuSUfS6mheueA9vDPlV1GgoJMAyMbi3B5uZUqOnSSShCy0vXWSPLVk_T-VN5uEHpkeL_sFbZFlYW0mQtwtqGUNyXLILDDGUhMkEJsyMziRmB4hyvjmiUYRHijoVK0x4OeSs8V9J8dY93FKDNUeC0SDrOHxKDcW6Pbwrrgk_ztMQwigzYfdAmu5EbX6KoaK0X0r_rQLYr0fML-Y_cP190gI0B1CYPHw5Ku9UBtgX9U44yYxMctdDFKT9mA7X9XyaLjocS640nyafMpEuYFIZaD_yo1AyCUlDrVcjCF7coZ3o8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52eb8aced.mp4?token=HXeuBXkE1JA3_exUFm5jvQfVR2a19_cWE8K8tl4NtuSUfS6mheueA9vDPlV1GgoJMAyMbi3B5uZUqOnSSShCy0vXWSPLVk_T-VN5uEHpkeL_sFbZFlYW0mQtwtqGUNyXLILDDGUhMkEJsyMziRmB4hyvjmiUYRHijoVK0x4OeSs8V9J8dY93FKDNUeC0SDrOHxKDcW6Pbwrrgk_ztMQwigzYfdAmu5EbX6KoaK0X0r_rQLYr0fML-Y_cP190gI0B1CYPHw5Ku9UBtgX9U44yYxMctdDFKT9mA7X9XyaLjocS640nyafMpEuYFIZaD_yo1AyCUlDrVcjCF7coZ3o8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طبس و شبی دیگر از روایت یک حضور ادامه‌دار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/466112" target="_blank">📅 22:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466111">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a3757003.mp4?token=RAywMSsqhUljojOotnpOfWkEYEg8o3sX0apnedw7d1ByZaww5pPJ08RrqZBBFUNlXtmrdri_O1jQQ6pC_gw7ANzdshHBbBIsOqvDaWZTBRVmvfyeUxcrHRwc30I15DoR17Xr0BQCdKofLooEVjSu4VXwlRUZ6KTkZTXarDe7PL-746ve83HpSebKOXnyK7Il_bKyAbWdW2SsFomqxX75K2qTk9dLk91IgaDfcSaLq-RJ39Yti2ODJJ-7E9pjwuzzLf22mAaoF_BeyGDRUxEDt3QZsgslp9_SIbr93fYn-MIutaisJBjTRC7V59QjsKq32udBg29p1Y_YgjNQLTASag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a3757003.mp4?token=RAywMSsqhUljojOotnpOfWkEYEg8o3sX0apnedw7d1ByZaww5pPJ08RrqZBBFUNlXtmrdri_O1jQQ6pC_gw7ANzdshHBbBIsOqvDaWZTBRVmvfyeUxcrHRwc30I15DoR17Xr0BQCdKofLooEVjSu4VXwlRUZ6KTkZTXarDe7PL-746ve83HpSebKOXnyK7Il_bKyAbWdW2SsFomqxX75K2qTk9dLk91IgaDfcSaLq-RJ39Yti2ODJJ-7E9pjwuzzLf22mAaoF_BeyGDRUxEDt3QZsgslp9_SIbr93fYn-MIutaisJBjTRC7V59QjsKq32udBg29p1Y_YgjNQLTASag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شورای امنیت روسیه: برای ساخت نیروگاه‌های هسته‌ای جدید در ایران برنامه داریم
🔹
روابط ایران و روسیه در بی‌سابقه‌ترین سطح خود قرار دارد؛ سال گذشته حجم تجارت بین ۲ کشور ۲۰ درصد افزایش یافت. @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/466111" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466110">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b8a863e7.mp4?token=BLmTkeEjM3HrFSnawi5NfyIU0jZoggmEg8ZHXdysWE5eRyunH8TD9a43tGBzCfBuKqt_48Ga2Db8Q_vz-DwBYLMuhFuEY390nCvab4xBjkjONvWLTOYKjb36KlvOAtC4kAMkCEHIRBxqzNSZhnza1LXuMsbCIWbGDeRlVMpJEVkPOJEtE2kdFxEk6ipiIGMX7o_SAKUyKy3o2izLH_BKrbNgxY2NQbrBxSbDvf4aEmasF4ZAr1Vxc9BW9wFq3tTD-ggXl1QEfFSc1fYYdHnjugYkuuai5-t9BpuddicyM0FPE4_YJLymNOE56HA2uFM0Jv1hzcfnQCK666RSkeNtDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b8a863e7.mp4?token=BLmTkeEjM3HrFSnawi5NfyIU0jZoggmEg8ZHXdysWE5eRyunH8TD9a43tGBzCfBuKqt_48Ga2Db8Q_vz-DwBYLMuhFuEY390nCvab4xBjkjONvWLTOYKjb36KlvOAtC4kAMkCEHIRBxqzNSZhnza1LXuMsbCIWbGDeRlVMpJEVkPOJEtE2kdFxEk6ipiIGMX7o_SAKUyKy3o2izLH_BKrbNgxY2NQbrBxSbDvf4aEmasF4ZAr1Vxc9BW9wFq3tTD-ggXl1QEfFSc1fYYdHnjugYkuuai5-t9BpuddicyM0FPE4_YJLymNOE56HA2uFM0Jv1hzcfnQCK666RSkeNtDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدودف، معاون شورای امنیت روسیه: با شرکت در مراسم تشییع رهبر شهید ایران انسجام ملت ایران را دیدم
🔹
من در سفر خودم دیدم که مردم ایران علی‌رغم همۀ مشکلات به زندگی عادی و حمایت از کشور خود ادامه می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/466110" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466109">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شورای‌عالی هنر و ادبیات تشکیل شد
🔹
هیئت دولت با تصویب تشکیل «شورای‌عالی هنر و ادبیات»، سازوکار جدیدی برای هماهنگی و سیاست‌گذاری در حوزۀ هنر و ادبیات ایجاد کرد.
اعضای شورا چه کسانی هستند؟
🔸
رئیس شورا:
معاون اول رئیس‌جمهور
🔸
دبیر شورا:
وزیر ارشاد
🔹
وزیر میراث فرهنگی
🔹
۲ وزیر به پیشنهاد وزیر ارشاد و تأیید معاون اول
🔹
رئیس سازمان برنامه‌و‌بودجه
🔹
معاون رئیس‌جمهور در امور زنان و خانواده
🔹
رئیس صداوسیما
🔹
دبیر شورای‌عالی انقلاب فرهنگی
🔹
رئیس فرهنگستان هنر
🔹
رئیس حوزه هنری
🔹
مدیران خانه‌های تئاتر، موسیقی و هنرهای تجسمی
🔹
یک نماینده از انجمن‌های صنفی ادبی
🔹
۶ هنرمند، استاد و صاحب‌نظر؛ با حضور حداقل ۳ زن
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/466109" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466108">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d92c4693.mp4?token=bXnC7t7ZYX1jCBijzlvRm0ulu4noudFyjWPhFtTVhwzHIstbRmPjQJ9YJ2JpP3hYjLkVwA5geYzd_a2RYDZetNOefFveJzyplD2YDQo_MIJg-mnuyxkf8S8rl9c526TWRhXIunadkyppFsOSusXFyR3V4hk6YSH5zJjELNTUbvgFdCInESdrSCi8R2KWhYq5go16UTgoOMlW-_DMjPTHCnvKGCWZiaEmdvbCnqW1mHUv1y417rNe4QerHJzqttJEbfYAWBFlhAufe3AJnr-KWqTEGEBzxitJ0Hd4pWGQKKCCcN3u6Yi-ap3TD1ImpCX2q3WCrGOVlWWitvEz8qtu0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d92c4693.mp4?token=bXnC7t7ZYX1jCBijzlvRm0ulu4noudFyjWPhFtTVhwzHIstbRmPjQJ9YJ2JpP3hYjLkVwA5geYzd_a2RYDZetNOefFveJzyplD2YDQo_MIJg-mnuyxkf8S8rl9c526TWRhXIunadkyppFsOSusXFyR3V4hk6YSH5zJjELNTUbvgFdCInESdrSCi8R2KWhYq5go16UTgoOMlW-_DMjPTHCnvKGCWZiaEmdvbCnqW1mHUv1y417rNe4QerHJzqttJEbfYAWBFlhAufe3AJnr-KWqTEGEBzxitJ0Hd4pWGQKKCCcN3u6Yi-ap3TD1ImpCX2q3WCrGOVlWWitvEz8qtu0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدودف، معاون شورای امنیت روسیه: با شرکت در مراسم تشییع رهبر شهید ایران انسجام ملت ایران را دیدم
🔹
من در سفر خودم دیدم که مردم ایران علی‌رغم همۀ مشکلات به زندگی عادی و حمایت از کشور خود ادامه می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/466108" target="_blank">📅 22:09 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466107">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a447c7e62f.mp4?token=mX-0wUbZPtjY7vgnOl_gyJ-QiMBAYtaBWxpHEGlHMcpQeImeuVtHF4AJXIbIdvMw28m_8nFy43VCHFlUTrV7fjx2VHzAT8KrDuKl9sMtW7Ot4h0cZVLNa_XN3mn4Zp1aCD4poUx7X8KOptATM61oPzmYfqFB_IdRcLc2yyKKMx0rSwG4Xf4dA3hmulmTb6m7Yxhvjcp0ksRr8duQkREngbpRd-vFOwNP4tzMG0JiwkGnIhxUS13QFPS-ujFNwjsUfqYPwCvWieOpQWm5VBnD0JVC5hZ-7dErg_4B1PmiFVxYhMfOo9bQAh1JjX-x3U_6_PzwGYMoVi1uwnfzSbuMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a447c7e62f.mp4?token=mX-0wUbZPtjY7vgnOl_gyJ-QiMBAYtaBWxpHEGlHMcpQeImeuVtHF4AJXIbIdvMw28m_8nFy43VCHFlUTrV7fjx2VHzAT8KrDuKl9sMtW7Ot4h0cZVLNa_XN3mn4Zp1aCD4poUx7X8KOptATM61oPzmYfqFB_IdRcLc2yyKKMx0rSwG4Xf4dA3hmulmTb6m7Yxhvjcp0ksRr8duQkREngbpRd-vFOwNP4tzMG0JiwkGnIhxUS13QFPS-ujFNwjsUfqYPwCvWieOpQWm5VBnD0JVC5hZ-7dErg_4B1PmiFVxYhMfOo9bQAh1JjX-x3U_6_PzwGYMoVi1uwnfzSbuMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرکل هواشناسی استان تهران: بارش باران در تهران تا اواخر وقت یکشنبه ادامه دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/466107" target="_blank">📅 22:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466106">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THE-RD186MR8ZNLAG17M2-oiWxBbmv7U6gIPR4NG_Ag7hoCksreRqOP_VR-lXc6-raypNqOSr5x6Xfjt0IZ48y5lJVLHHrIk8w8jWOqBOBJj9HtPPQMQYrOdUlz8CO80zfnz_DkQkT3CIhTDV4HnKcPPLCYqnPoinO9FFRrZLJgDLGd6MuPw7V-m01MLGkN6KD10s28MUlUyk_WDah3Vc3Y8rHAqvqZ4bCFhBgPCW2Sil9VO-ZYcJkGfimENuwvrYXzWjNetX9gvLDuKt1iMQLGt63w5YtMe7pEEnj1Lw3xblKtvWCegDlBAVBWP09VHy-OJ-fxvXclbdBybT8Rgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت ۴۸ ساعتۀ یمن به مزدوران سعودی در تعز
🔹
نیروهای مسلح یمن در ادامۀ پیشروی‌ها در استان تعز، به نیروهای تحت حمایت عربستان هشدار داده‌اند ظرف ۴۸ ساعت این منطقه را ترک کنند.
🔹
منابع یمنی می‌گویند نیروهای انصارالله تاکنون بیش از ۲۰۰ کیلومتر در تعز پیشروی کرده‌اند…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/466106" target="_blank">📅 21:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466105">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2146fb73.mp4?token=ojGJwlSFoGkcp7Q1rTAC2-oBBBSnGk2w5ndbjIFZM4KHHUFiMckj0y6DMgjzfpqWXqWrpEglmve7YBbap91dsOeLrxoluN59Angi8VjY_9G9YJDtwPPW4kd-K6ePVKWk0CiZ4XPOnAWCUbwF97a9Y6qa8oDAoiRRs1G967ZocJwOSdskndjn5DhcIND_yWkWxbdM8FPnCtDl_Uo0gArXSjK80y-2ij2pe44yDStg7ZA0gKdaWDgD3GqHJuBbGyz6bWIWhe5F5eBIvGm9y3GZ40GsfzTyEbYGhKVLeCC7OC7W33iCAzjgflhbxuPDoR2lCCgfvJZLr9OEmgvduVbNSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2146fb73.mp4?token=ojGJwlSFoGkcp7Q1rTAC2-oBBBSnGk2w5ndbjIFZM4KHHUFiMckj0y6DMgjzfpqWXqWrpEglmve7YBbap91dsOeLrxoluN59Angi8VjY_9G9YJDtwPPW4kd-K6ePVKWk0CiZ4XPOnAWCUbwF97a9Y6qa8oDAoiRRs1G967ZocJwOSdskndjn5DhcIND_yWkWxbdM8FPnCtDl_Uo0gArXSjK80y-2ij2pe44yDStg7ZA0gKdaWDgD3GqHJuBbGyz6bWIWhe5F5eBIvGm9y3GZ40GsfzTyEbYGhKVLeCC7OC7W33iCAzjgflhbxuPDoR2lCCgfvJZLr9OEmgvduVbNSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برجک زندان رجایی‌شهر فروریخت
🔹
در ادامۀ تخریب دیوارهای زندان رجایی‌شهر البرز، برجک این زندان نیز تخریب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/466105" target="_blank">📅 21:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466104">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM9uJf8s8fkR8ch3Iuy2Is5sxGPVRiYCrcSItEvZJnyZ3H5BRvMVT2Y3wGu2JqELarIVj-t01GPuRZWbTwywpFC8J7zMtUE3Kjgnl21_PGX7DTHG1Jem4IqhtwBHWYj5x_obYYhJREpm90JXxngVaBujLyWUUiddRR49J2Q8Ckqr0Ner8Qoz3hnLf82CfO7EGCUuiICe8ZT_kWzSqBy6FzDG_vEfGOhf_Yp8XUG-3XR6hJc2Nr6Pd_JAdvO8p7slPJ5ibMVNsD-uMebjUriu_PgCEJi03eGTm0wE1RoKIM7lmB7osNiBqXiWxhjNWhBbEGNRf7H5L5cTKohZJ1ue_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست رد حزب‌الله بر سینه ترامپ؛ مقاومت لبنان مذاکره نمی‌کند
🔹
روزنامه الاخبار لبنان به نقل از منابع خود گزارش داد، آمریکایی‌ها از ایده‌هایی صحبت می‌کنند که «تام باراک»، سفیر آمریکا در ترکیه، اواخر ماه اوت گذشته مطرح کرد.
🔸
باراک گفته بوده که باید «حزب‌الله و ایران در هرگونه توافق یا مذاکره مستقیم، باید مشارکت داده شوند؛ زیرا صرف گرد هم آوردن سایر طرف‌های لبنانی دور یک میز، مشکل را به‌تنهایی حل نمی‌کند».
🔹
سخنان باراک موجب اعتراضاتی در داخل و خارج آمریکا، در منطقه و لبنان شد و این مسئله باعث شد بعداً مواضعی در جهت «توضیح و رفع سوءتفاهم» مطرح کند.
🔸
الاخبار گزارش داد تلاش‌ها و پیام‌های متعددی از سوی میانجی‌گران منطقه‌ای و بین‌المللی و هیئت‌های دیپلماتیک برای ایجاد کانال ارتباطی مستقیم بین واشنگتن و حزب‌الله صورت گرفت.
🔹
به گفته این منابع، حزب‌الله تأکید دارد هرگونه تماس مستقیم با آمریکا به نتیجه منتهی نخواهد شد و هیچ تضمینی در این خصوص وجود ندارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/466104" target="_blank">📅 21:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466103">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbec3e0c1.mp4?token=g7KoRZMBH9k9ue698mAH9GgJ92sOJQRkYLXSWAB-qKY-iquaupmzHdPJsz9adwFCZCmSp9pZvjCOdZWaR1I2yK-Z1AgPlxMl5ZdeZfAeTFcPftcqsdZElMmdQkm3ja20tbF_40-IewKA8KCxrmfStjz914MFZUbAu16wPDQEe0Y7C59nW8dzIiBNWmQ-CApQZMef1L5viE7XtnpAGaj7tWgvejpSgY_-Q4DsCEpf8OH7usqzbklIVkPD6xHK5HzAdeJt4tIezDsBKXBkL3_wCl5DCx0Zu8lTmlECXlKleI0t4xfxOwHsXDg8EkkQn44hZwo6gyyNs6OnYlILJaL9lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbec3e0c1.mp4?token=g7KoRZMBH9k9ue698mAH9GgJ92sOJQRkYLXSWAB-qKY-iquaupmzHdPJsz9adwFCZCmSp9pZvjCOdZWaR1I2yK-Z1AgPlxMl5ZdeZfAeTFcPftcqsdZElMmdQkm3ja20tbF_40-IewKA8KCxrmfStjz914MFZUbAu16wPDQEe0Y7C59nW8dzIiBNWmQ-CApQZMef1L5viE7XtnpAGaj7tWgvejpSgY_-Q4DsCEpf8OH7usqzbklIVkPD6xHK5HzAdeJt4tIezDsBKXBkL3_wCl5DCx0Zu8lTmlECXlKleI0t4xfxOwHsXDg8EkkQn44hZwo6gyyNs6OnYlILJaL9lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی مجلس: ذخایر مواد غذایی کشور ۲۰ درصد فراتر از برنامه‌ریزی‌ها است.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/466103" target="_blank">📅 21:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466102">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce2b222702.mp4?token=EKgJduC0HOclTv3xuP1c-ue7Doa3yjzV49A5XHnkzs-ar6fiVd0QHAQOIXWIRJhDflelCdp5_7IcrTT8T4E0jsUOtBLtxoqZ5TqE0HRd7LUqhicu3glAbqAeRYp3y0C375ZYGQoR9Spc6j0rQqHRKFQ-WrzUrzwXeMmgNAD_WIx0LI-U29EoJYUUzP9tnbXTe3sUG7rcEKFV8kdILlS9I4p6jnSp5HtVzMV0mwV5cb-YVwMJVYrxslwNU-ov9p0fMxuNe60dAX1BkerL2u6lMHATyDLC2NWllb041ZDKBaZgExAnemC8BDFFlM_QbjiZxOay1M8blK6k6Ef70k55UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce2b222702.mp4?token=EKgJduC0HOclTv3xuP1c-ue7Doa3yjzV49A5XHnkzs-ar6fiVd0QHAQOIXWIRJhDflelCdp5_7IcrTT8T4E0jsUOtBLtxoqZ5TqE0HRd7LUqhicu3glAbqAeRYp3y0C375ZYGQoR9Spc6j0rQqHRKFQ-WrzUrzwXeMmgNAD_WIx0LI-U29EoJYUUzP9tnbXTe3sUG7rcEKFV8kdILlS9I4p6jnSp5HtVzMV0mwV5cb-YVwMJVYrxslwNU-ov9p0fMxuNe60dAX1BkerL2u6lMHATyDLC2NWllb041ZDKBaZgExAnemC8BDFFlM_QbjiZxOay1M8blK6k6Ef70k55UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
محل‌های استفاده از طرح «تورم صفر» شهرداری تهران را بشناسید  @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/466102" target="_blank">📅 21:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466101">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ikMJxSPAt0JOpOa5A1VouVst3hjbl8zNUWB6XXPeLjeEs_WRizT0rVpTE6aJgu4_jBPrFyun7QjGPY3wzzVJqWhA9tblDWRR-tvtlXUx7h02NiaxYvNsVM5zZHsBX-0JKWWV1vniEyRnjMx1WouZm62GCMu0XYkgE9HRInT6hCxXQYrfD2044TF29BKlU7ZPoM40xdaiRD8RCceKCTguOAlsjb5GTTsn4fZS56t-bCJiTU7zfPNT24Hp1gtb_D-NNX6_VC25Y00qlj3rFSLSK6zxZPpN7gj2AzvYywc70MfactDtHV6EYMDBX2ebIH6ExQY7ACM0K8QopN4kSefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نتیجه‌ای عجیب در لیگ ملت‌های اروپا؛ کرواسی با ۷ گل مقابل انگلیس تحقیر شد
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/466101" target="_blank">📅 21:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466100">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انهدام تیم تروریستی مرتبط با سلطنت‌طلبان در فارس
🔹
یک تیم تروریستی مرتبط با جریان سلطنت‌طلب در شهرستان نورآباد استان فارس توسط سربازان گمنام امام زمان(عج) شناسایی و منهدم شد.
🔹
اعضای این تیم علاوه بر تبلیغ و تحریک به خرابکاری، در حمله به زیرساخت‌های خدماتی و تخریب اموال عمومی در حوادث دی‌ماه ۱۴۰۴ نورآباد نقش داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/466100" target="_blank">📅 21:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466099">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnHeAMZrYL_NG0kLn3qkt9NwjsFUtwcqQZMYJm-K7j58ZVy3AYsau7_IiKNhO8XfhQ6O5dohbu0kmLLcdMjRAnW7IRKfK1b2knWYGY4j1KyKpTEu4rT0XT-SqoEunJFn4q880HRuUAHG2rSiqPp0dov1V3j7nmgYs4lkpzEUkUt89jUl7C-m67mOZqJT0-ouE5imljYiYGIQeEFckf2Y64RzsRZ7MQs2g4PKP_aIVl9I65AAHamghepTi9qiELa3BpoZNOFXXZX34UNMDsi5p5w9cm9eCaFxWXGajXjQ6XIoY26zph7chqay8rfNR-EtSSej1_Hj7SlPBKxeZ1UqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعظی: اختلافات داخلی، دشمن را به طمع امتیازگیری بیشتر می‌اندازد
🔹
محمود واعظی، قائم مقام حزب اعتدال و توسعه: دشمن بیش از هر چیز به پیام‌هایی که از داخل کشور منتقل می‌شود توجه دارد، اگر احساس کند میان مردم شکاف وجود دارد، جسارت پیدا می‌کند و به امتیازات بیشتری فکر خواهد کرد.
🔹
نه دفاع از کشور را جنگ‌طلبی بدانیم و نه مذاکره را وادادگی یا خیانت تلقی کنیم.
🔹
دشمنان با برداشت غلط از وضعیت انسجام اجتماعی ایران، تجاوز خود را آغاز کردند. آنها تصور می‌کردند طی ۲۴ یا ۴۸ ساعت به اهداف خود می‌رسند اما ایستادگی نیروهای مسلح و همراهی مردم، محاسبات آنها را تغییر داد.
🔹
مثلث بازدارندگی بر سه ضلع؛ قدرت و توان رزمندگان، حضور و حمایت مردم در میدان و خدمات دولت استوار است و این سه ضلع، ظرفیت کشور برای دفاع و تأمین منافع ملی را تقویت می‌کنند.
🔹
گاهی تلاش برای حل یک اختلاف، اگر با شتاب و قضاوت عجولانه همراه شود، خود به اختلافی تازه تبدیل می‌شود.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/466099" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466098">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b171e0ba8e.mp4?token=Kwa4rJX9gVzkBkudHjgM3j__1gqQ_WL4zpgmcvgpxRJOwe-yGY6S_cXAgAV-UnpwWy-WEewLoAUXalJjM1H214XMGasLW3oW9FD5Gw1qwyUp8ZnPBsW3CEQEQeyKiZCCne1ie21CyEWHf43wrRMF4Y3lKfbvCQEFHoy0rRDXrqpvWY5FYJU3FWC6JiOIjcUHlPE17s6Zp4UGfpvzRdSG8z8lpxMBugHOy-0hLuvIPROuF8VTw2VJDM3-EYoVOl5VBT1EKjVkB3JN6IVQD56mOIb_B6-cHkXZnmyEDX1xZ8CyxbWzAzUe-7uuEwCf8pFI40VCFKfLJBNJUonwu7T2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b171e0ba8e.mp4?token=Kwa4rJX9gVzkBkudHjgM3j__1gqQ_WL4zpgmcvgpxRJOwe-yGY6S_cXAgAV-UnpwWy-WEewLoAUXalJjM1H214XMGasLW3oW9FD5Gw1qwyUp8ZnPBsW3CEQEQeyKiZCCne1ie21CyEWHf43wrRMF4Y3lKfbvCQEFHoy0rRDXrqpvWY5FYJU3FWC6JiOIjcUHlPE17s6Zp4UGfpvzRdSG8z8lpxMBugHOy-0hLuvIPROuF8VTw2VJDM3-EYoVOl5VBT1EKjVkB3JN6IVQD56mOIb_B6-cHkXZnmyEDX1xZ8CyxbWzAzUe-7uuEwCf8pFI40VCFKfLJBNJUonwu7T2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج افتخار از ناگویا به تجمعات تهران رسید  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466098" target="_blank">📅 21:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466097">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9266b5859f.mp4?token=ZFGZFCNIoibLHeydx3p4__ulj9NMygZpEJtvZQ1gq3xCR-V5CTSGjz3t58Ne9Y-hNghiktr-B5gea3SV4q76c47see9wjGSTOMsUO4-SvFMPE91772F-yxtUKif0DY8d2LTL-jWe65MHjClYktfqOHT-GZ2vZNYJIDkZUM1qZc6fvICGTH7sZYS4qtPKRC4xetki5goS-S78fHxXs3afkkzV4YQEeByE51HQR59TllcBq-qFNf_-dwMOpvBmSksiKh-udfmOVmc8oK1zM3sGB7Bra7vLx2FvNVnW1pvRO3Ay6c1MEHJRZ2nK_GDQn5F9R_mlCChf1l3iCXVQZoFBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9266b5859f.mp4?token=ZFGZFCNIoibLHeydx3p4__ulj9NMygZpEJtvZQ1gq3xCR-V5CTSGjz3t58Ne9Y-hNghiktr-B5gea3SV4q76c47see9wjGSTOMsUO4-SvFMPE91772F-yxtUKif0DY8d2LTL-jWe65MHjClYktfqOHT-GZ2vZNYJIDkZUM1qZc6fvICGTH7sZYS4qtPKRC4xetki5goS-S78fHxXs3afkkzV4YQEeByE51HQR59TllcBq-qFNf_-dwMOpvBmSksiKh-udfmOVmc8oK1zM3sGB7Bra7vLx2FvNVnW1pvRO3Ay6c1MEHJRZ2nK_GDQn5F9R_mlCChf1l3iCXVQZoFBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/466097" target="_blank">📅 21:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466096">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfbb2d99f.mp4?token=APVDAjYHzrloQYMGxb8nnU0B0hdhfRbaRLX5saiE1Oig3WWVafYxw9bffixj0Q1q2q-Bznxj8DaiS_YhBvPon_V2zxuGTvOK7hWGfkjXLBO9CalkCbCQmf23wZpITXsERqEjLCClvuYs-asCYbq4dvfWJxMRLmM_5ogx1WTKn4h8oUEnzJh-YR7zJRsytBKY-U7cxTGmJLZNgPzZjREbX1S6LJxM8YZ3tq_r4Eai6hOj82rzR-mjHxQT7kxQsqB0rC1NsHWWZy1DlEj31ukNKlsCp-ytk9KCQXKG-Fa7aQoWRYs5G1O8ElEdwYblQU-UN6rY2ordHHty30RpE_O56g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfbb2d99f.mp4?token=APVDAjYHzrloQYMGxb8nnU0B0hdhfRbaRLX5saiE1Oig3WWVafYxw9bffixj0Q1q2q-Bznxj8DaiS_YhBvPon_V2zxuGTvOK7hWGfkjXLBO9CalkCbCQmf23wZpITXsERqEjLCClvuYs-asCYbq4dvfWJxMRLmM_5ogx1WTKn4h8oUEnzJh-YR7zJRsytBKY-U7cxTGmJLZNgPzZjREbX1S6LJxM8YZ3tq_r4Eai6hOj82rzR-mjHxQT7kxQsqB0rC1NsHWWZy1DlEj31ukNKlsCp-ytk9KCQXKG-Fa7aQoWRYs5G1O8ElEdwYblQU-UN6rY2ordHHty30RpE_O56g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدافند هوایی نوین نیروهای مسلح کشورمان در قشم موفق به رهگیری یک پرنده متخاصم شد
🔹
مردم محلی می‌گویند در جریان فعالیت پدافند دست‌کم یک هواگرد در آسمان قشم هدف اصابت قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466096" target="_blank">📅 20:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466095">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00f18bbd6.mp4?token=rQfTH3aKJL9Y33FyBeX-QOg4JiP6RKm7SENd8SQsafSIrLEoNhTdP0qi-nM9acEWWkaMMyrXdnzc_WPCW7gefHWWtpraEDB407AmeeXbPfd1WPJD1C8rN6oVbJZUrHARRSwY_Eiyp1NVZlqCbHk6yAiFYhi_3WzX_p5qhvG2Le13EA57orV_r1sWWeVdD5Trw_nY56XZH1gE1WU8ToXbXZEvdfXdz-vsIQtoK38fiPYZvpRhEhw_mQcXpVn5eZkRtYhak2fWVL93s-rHlGnTnaYGJrV51oFBqlxxcG5GxdGO0wRNQ3LggXdFuDYGKHNED-7v4i3-wDSXaoCg7lI3Fw6hQyfBNbQlZEdBD5K5TgxIUfNo1LAYDHaX6oUlU9kNKMc5o9cYdAiitBACaSaO0oJh572_qzFhmJATWTyoHm3_GTrwkGRJluSgOrbg3sTF1f3PracH2AXsOG4Wlv6YTen3ypck4vh1J-hj-kwKxgrdGv0oP_ZHfE_wE0OCtb3zIYCqy4thJ8RUZGMu_MEn6LMiq8sOzun9A13fb_tAoL-w-TdBjnoujX8hHmUFgszpi9X77UMhIh3pybe_wIFn1N66RpW0GyCRhGKu9xibmLauGUz4w8p1RRPyFDFOaMe7BGE9DDPlIk8roTrxJpoIOJI5f8AEeBY0axGRE_8PtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00f18bbd6.mp4?token=rQfTH3aKJL9Y33FyBeX-QOg4JiP6RKm7SENd8SQsafSIrLEoNhTdP0qi-nM9acEWWkaMMyrXdnzc_WPCW7gefHWWtpraEDB407AmeeXbPfd1WPJD1C8rN6oVbJZUrHARRSwY_Eiyp1NVZlqCbHk6yAiFYhi_3WzX_p5qhvG2Le13EA57orV_r1sWWeVdD5Trw_nY56XZH1gE1WU8ToXbXZEvdfXdz-vsIQtoK38fiPYZvpRhEhw_mQcXpVn5eZkRtYhak2fWVL93s-rHlGnTnaYGJrV51oFBqlxxcG5GxdGO0wRNQ3LggXdFuDYGKHNED-7v4i3-wDSXaoCg7lI3Fw6hQyfBNbQlZEdBD5K5TgxIUfNo1LAYDHaX6oUlU9kNKMc5o9cYdAiitBACaSaO0oJh572_qzFhmJATWTyoHm3_GTrwkGRJluSgOrbg3sTF1f3PracH2AXsOG4Wlv6YTen3ypck4vh1J-hj-kwKxgrdGv0oP_ZHfE_wE0OCtb3zIYCqy4thJ8RUZGMu_MEn6LMiq8sOzun9A13fb_tAoL-w-TdBjnoujX8hHmUFgszpi9X77UMhIh3pybe_wIFn1N66RpW0GyCRhGKu9xibmLauGUz4w8p1RRPyFDFOaMe7BGE9DDPlIk8roTrxJpoIOJI5f8AEeBY0axGRE_8PtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر درگذشت حجت‌الاسلام قرائتی نادرست است
🔹
پیگیری خبرنگار فارس نشان می‌دهد اخبار منتشر شده در فضای مجازی درباره سلامتی حجت‌الاسلام قرائتی نادرست است.
🔹
این استاد بزرگ قرآن هم‌اکنون برای حضور در اجلاسیه سراسری اقامه نماز در مشهد حضور دارد. @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/466095" target="_blank">📅 20:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466094">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfX8YdsD1lSXuVPMOd4p8J0Qnr_a-tfL1o8u1yNSeoJyDOxehuT_VgTuZ0BdRT9235ssqxLwKu13Mdy-rnm51zteT9czuxesTt0KLktHmCmWmJ9PZHjOHEIeRTqfOn8p3VbkhczFkw2_DxW1ywXKfzSX5vTtY2VKqdgHaQ7OsIWM_S4B1YR0h5J3fvBzKa3lnGAB6cyAyE9PTpbZeB4fGJD1z6uWQptztabcjxUAkTRakXtffK7Jnz3GBC-7dwOm9yphVaMg91YvZ3i80J2HFYsjOy6DdRX_C2mVioOs3S6Y-XmSGhZjaQKLrGapCrHu3kEZOGFDdVRqtH57AeSSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کورس دلار آزاد و تلگرامی در اولین روز هفته
🔹
قیمت دلار از ابتدای امروز و با شروع هفته بیش از ۵ هزار تومان در کانال‌های تلگرامی افزایش یافت و به حدود ۲۶۸ هزار تومان رسید.
🔹
همزمان صرافی‌ها و دلارفروش‌های اطراف خیابان فردوسی نیز نرخ فروش دلار را بین ۲۶۵ تا ۲۶۷ هزار تومان اعلام کردند.
🔹
آخر هفتۀ گذشته قیمت دلار در بازار ارز فردوسی حدود ۲۵۳ تا ۲۵۴ هزار تومان بود که نشان می‌دهد نرخ دلار طی ۲ روز بیش از ۱۲ هزار تومان افزایش یافته است.
🔹
بانک مرکزی از امروز عرضه ۲ میلیارد دلار از طریق بانک‌ها را آغاز کرده که در ابتدای عرضه، قیمت دلار حدود ۲۵۹ هزار تومان بود. سقف خرید نیز برای هر نفر ۱۰ هزار دلار اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/466094" target="_blank">📅 20:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb15d2d6d0.mp4?token=unDCTcMOoQol28p1Da_OkXVH6RR1wcyhkYq3zBO9SRnWWIiMkpHEfTMYSfsrHf89P_uPUI8PTpurz30iPRmY9vYmLbDRIucNvVxUIjBqjhl7my_tbJYLxb-sM9Nj2h8u2fMSMs--Nw4EKQsWNjz1UjSMamAzH2xXFl6IIKYT4fFIN-GAOierMsdQY4IPLBhm-XT1VjxOrnemP9MjTk1agJHPI4Te-R7zBhy-8k4elqwomm8JOSBYMOqjrSDmQJmNQ3YY4IpFNZ0rBzc0rdCfuFhG6P3_qoyW3jhSi0uzfCjNFfVOHI4tC4BOUCRmeZMtCbi_5V21Bk68VWsjlhCubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb15d2d6d0.mp4?token=unDCTcMOoQol28p1Da_OkXVH6RR1wcyhkYq3zBO9SRnWWIiMkpHEfTMYSfsrHf89P_uPUI8PTpurz30iPRmY9vYmLbDRIucNvVxUIjBqjhl7my_tbJYLxb-sM9Nj2h8u2fMSMs--Nw4EKQsWNjz1UjSMamAzH2xXFl6IIKYT4fFIN-GAOierMsdQY4IPLBhm-XT1VjxOrnemP9MjTk1agJHPI4Te-R7zBhy-8k4elqwomm8JOSBYMOqjrSDmQJmNQ3YY4IpFNZ0rBzc0rdCfuFhG6P3_qoyW3jhSi0uzfCjNFfVOHI4tC4BOUCRmeZMtCbi_5V21Bk68VWsjlhCubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خراتیان، تحلیل‌گر مسائل بین‌الملل: سیگنال‌های مذاکراتی تلاش یمن برای افزایش قیمت نفت را خراب کرد
🔹
پس‌از اوج‌گیری قیمت نفت با اقدامات انصارالله یمن، سیلی از اخبار مثبت ایجاد شد تا با «خبردرمانی» جلوی التهاب بازار نفت گرفته شود.
🔹
یکی از مواردی که بازار نفت…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/466092" target="_blank">📅 20:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آرایش جدید اقتصادی دولت برای مدیریت شرایط ویژۀ کشور
🔹
در جلسۀ ستاد هماهنگی اقتصادی دولت، آخرین وضعیت بازار ارز، بودجه، تجارت خارجی و تأمین کالاهای اساسی بررسی شد.
🔹
در این جلسه بر ثبات بازار ارز، هماهنگی سیاست‌های ارزی، تجاری و مالی، مدیریت انتظارات و تأمین ارز مورد نیاز بخش واقعی اقتصاد تأکید شد.
🔹
سازمان برنامه‌وبودجه نیز یک
بستۀ پیشنهادی ۷ ماده‌ای
برای مدیریت شرایط موجود و عبور از محدودیت‌های پیش‌رو ارائه داد.
🔹
وزیر کشاورزی اعلام کرد کمبودی در کالاهای اساسی مورد نیاز کشور وجود ندارد.
🔹
همچنین پیشنهاد ایجاد ساختاری چابک‌تر برای تسریع تصمیم‌گیری و اجرای مصوبات اقتصادی مطرح شد.
🔹
دبیر شورای‌عالی امنیت ملی نیز اعلام کرد شعام آمادۀ هرگونه حمایت و همکاری برای پیشبرد امور و کمک به مدیریت شرایط اقتصادی کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/466091" target="_blank">📅 20:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466090">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW90_dj4kZPWMApOZBGTiXOc_WInGoJG0JlHyoc-niZHnVS0hRDzTJKfkn7ksEk0W487LSwQ75bbvFPCgDMhQfngnWE6AHjV3dds6_j9ApKxIe5e4WmisG4eQdE4adgRB5cStS-gd2tiiURFzYDh1AqpjLYTN5Cyc-GwXr1btH8bnmA1D5KXtXpAVX9aX590Y37XmZrgzTcDK1JH40-_i8YKy_k9tm-IIZxOs8zZ8lvoRtpbLHM4w54YKpuz60r2GFzViPXozAytpo_5JkmM0he3bQFCeC7aqgu5FSocXU-4YsfnYxTN1jHBFnLVFkhkRBiAWy6yuNs8SifLOchszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواپیمایی: پروازهای ایران و عراق از فردا توسط شرکت‌های هواپیمایی ایرانی و عراقی برقرار می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/466090" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466089">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgopmHtVSf16iR4gITfpiphHfiZJ_POEgxlrA_h3uvRToiMlYuiPkxm0DrLU4U1UTDIL3lyly7zNHao-vHdJaP3ReYEhL8B9mFOQlPROu6LKFjsqfWbsWeyXnzPZNerQGmi01WGJx6Od2NLsVhZ6k4CxKVp77sscLcBUnLnCjD526dOautNbXeQmzt00WYBFVAHSgWtuamPDdfkPMUMqTI5on9ZxBOZOikmsBMQp2UT38LXI59-oujB91RStcdEwcIJwKANmgwrqR_ZM7refOqQ2rhrfsJYg7BkZFM-WlgD1L9D48CGTK7-hJa5gBBHn4R-zXEXkj5_nkjtE3JqgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر دولت پرتغال بر سر پایگاه آمریکایی
🔹
دادستانی پرتغال پس از شکایت حزب «بلوک چپ» این کشور تحقیق دربارۀ قانونی‌بودن مجوز استفاده آمریکا از پایگاه هوایی لاخِس در جنگ علیه ایران را آغاز کرد.
🔹
طبق توافق دو کشور، پس از آغاز خصومت‌ها، استفادۀ آمریکا از این پایگاه به موافقت پرتغال نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/466089" target="_blank">📅 20:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466088">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d70b79c1.mp4?token=I8XXentCHsKf75G5Rjoji8mpOYWyQ1SK-KHLjLynwQ-BvQHdB4OOOzG6lJz4rcGEF_zm3qciey6je34E2IsaR_yxQBHUY_NLUSSqvPIc2d_yacfPrzXP4VNqO9IA_tHe74qxEmYalWUTd3PyIbggrJpToe7hsvO7EYLy1e_ZxPfJFTkYEiGJtagj_0j_Donu9X2_NVMQqImTlTuFMCyZ4nBHZG7R42ke4LDewJKIJEZq9RRbO1y9o9WJ-yFng6W3hCEEmcDOEDtwPZeX-vNjc47Hbo078v6fgraLcBl77ip0PFmQEnNxWL8oen55d2WoavOTiTTDCBr36AyG8AX0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d70b79c1.mp4?token=I8XXentCHsKf75G5Rjoji8mpOYWyQ1SK-KHLjLynwQ-BvQHdB4OOOzG6lJz4rcGEF_zm3qciey6je34E2IsaR_yxQBHUY_NLUSSqvPIc2d_yacfPrzXP4VNqO9IA_tHe74qxEmYalWUTd3PyIbggrJpToe7hsvO7EYLy1e_ZxPfJFTkYEiGJtagj_0j_Donu9X2_NVMQqImTlTuFMCyZ4nBHZG7R42ke4LDewJKIJEZq9RRbO1y9o9WJ-yFng6W3hCEEmcDOEDtwPZeX-vNjc47Hbo078v6fgraLcBl77ip0PFmQEnNxWL8oen55d2WoavOTiTTDCBr36AyG8AX0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خراتیان، تحلیل‌گر مسائل بین‌الملل: سیگنال‌های مذاکراتی تلاش یمن برای افزایش قیمت نفت را خراب کرد
🔹
پس‌از اوج‌گیری قیمت نفت با اقدامات انصارالله یمن، سیلی از اخبار مثبت ایجاد شد تا با «خبردرمانی» جلوی التهاب بازار نفت گرفته شود.
🔹
یکی از مواردی که بازار نفت را آرام کرد خبر «نشست تنگۀ هرمز» بین ایران و کشورهای عربی بود؛ نشستی که هیچ‌وقت برگزار نشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/466088" target="_blank">📅 20:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466087">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d4866c8.mp4?token=SltbG-_NhuNHXRdSLcSBD7zXnVF3ojDrn_ku5ur0UOeyLXvkBkJasO6vqm2XFxzZEvR5hyzuDGlvj6pUs5wCAcLmz9LOVomiM1W7esyfkKtCfxk9jzmS_04K6Xh26qslKABXl0m4rqN-WYoKYc1HupRDVBp6TnCEwIfDGJb2Ot8vAT0pPHXdtI0I5DyfqDhVbYIshyua2oEKAC2a12kYQUCJ3fT3A_qpRjqYSFNR-f1-e7Tyxu89XbiEltP7m6dYHgSn9WGzsmThKa7HYFiinjyz6dltX2360i-mbm8b6YSrzwgVQQfqi--oha1Zrcs1kb0lGMFJ-sb-seqeZVnajg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d4866c8.mp4?token=SltbG-_NhuNHXRdSLcSBD7zXnVF3ojDrn_ku5ur0UOeyLXvkBkJasO6vqm2XFxzZEvR5hyzuDGlvj6pUs5wCAcLmz9LOVomiM1W7esyfkKtCfxk9jzmS_04K6Xh26qslKABXl0m4rqN-WYoKYc1HupRDVBp6TnCEwIfDGJb2Ot8vAT0pPHXdtI0I5DyfqDhVbYIshyua2oEKAC2a12kYQUCJ3fT3A_qpRjqYSFNR-f1-e7Tyxu89XbiEltP7m6dYHgSn9WGzsmThKa7HYFiinjyz6dltX2360i-mbm8b6YSrzwgVQQfqi--oha1Zrcs1kb0lGMFJ-sb-seqeZVnajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط قیمت نفت هم‌زمان با سفر میانجی به تهران
🔹
هم‌زمان با سفر وزیر کشور پاکستان به ایران، روند ریزشی قیمت نفت شدت گرفت.
🔹
پیش‌تر هم، سفر میانجی‌های مختلف به تهران زمینه ریزش قیمت نفت را فراهم کرده بود اما هیچ پیشرفت قابل ملاحظه‌ای در پرونده مذاکره اتفاق نیفتاد.…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/466087" target="_blank">📅 20:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfqNxQs6rn4gR_rDgcG6oKUJxPpZnNf_EwiVAzP0sVEH2DZZBjFtjg-GaLRIWHvPiQ7MhDaHC16ANTTfUMk9nnt6M9KCqcxyk7Pd0fD31E7xQn5Lvipel20ipReK5H0OApEvoQQp89HVhyktPy0wUVI0FsiRC534wUi1MaaS-e2pETeuNgaxdtnlS0WjxOTVh-h_M1I_cRrVTjde-OUoevUh0Hvg-OXz9pbc82Ik0FJ2lrpIjfbFmeauiHhMVHjE82FdWXWTfRQDJJ0RhenPNn4mN6sW3Zl0_fEgLJoYPrL1LvFwtlEJ6Pe_QE-QF1CV2-ELSaG98TaYb-oHHNp44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اصلاح‌طلبان به زاکانی به‌دلیل همکاری با پزشکیان؟
🔹
درحالی‌که شهرداری تهران طی ماه‌های جنگ بخشی از امکانات و منابع خود را برای کاهش فشار بر دولت و شهروندان به میدان آورده و اکنون نیز برنامه‌های معیشتی تازه‌ای را آغاز کرده است، هم‌زمان فشار سیاسی و رسانه‌ای بر علیرضا زاکانی افزایش یافته است؛ وضعیتی که یک سؤال را پیش می‌کشد: چرا درست در زمانی که شهردار تهران بر همکاری با دولت و کاهش بخشی از بار آن تأکید دارد، حملات علیه او شدت گرفته است؟
🔹
به گزارش فارس، اختلاف سیاسی علیرضا زاکانی با دولت مسعود پزشکیان موضوع پنهانی نیست، اما این اختلاف دست‌کم در ماه‌های جنگ مانع از همکاری مدیریت شهری با دولت نشده است.
🔹
شهرداری تهران در جریان جنگ، مسئولیت‌هایی را پذیرفت که بخشی از آنها فراتر از اداره روزمره شهر بود. اسکان خانواده‌های آسیب‌دیده و پذیرش مسئولیت بازسازی و نوسازی بخش‌هایی از مناطق خسارت‌دیده از جمله این اقدامات بود.
🔹
در همین مقطع، مترو و خطوط BRT نیز رایگان شدند؛ اقدامی که علاوه بر تسهیل تردد شهروندان، در شرایط محدودیت سوخت به کاهش مصرف بنزین در پایتخت کمک کرد.
🔹
این اقدامات در کنار فعالیت‌های عمرانی شهر در دوره جنگ بارها تحسین منتقدان و ناظران از جمله رئیس جمهور را به دنبال داشت.
🔹
در روزهای جنگ علاوه بر پروژه‌هایی از جمله اتصال‌های بزرگراهی، تقاطع‌ها و زیرگذرهای جدید حالا دامنه ورود شهرداری به مسائل فراتر از خدمات متعارف شهری، به حوزه معیشت رسیده است.
🔹
زاکانی هفتم مهر از اجرای طرحی با عنوان «تورم صفر» خبر داد که در مرحله نخست، قیمت ۱۲ قلم کالای اساسی را برای ۶ ماه ثابت نگه می‌دارد. این کالاها در ۱۰۸ میدان میوه‌وتره‌بار و سپس فروشگاه‌های شهروند عرضه می‌شوند و قرار است تعداد اقلام طرح نیز افزایش یابد. شهردار تهران گفته است این برنامه با استفاده از ظرفیت‌های قانونی شهرداری و همکاری دولت اجرا می‌شود.
🔹
مدیریت شهری همچنین از بسته‌های دیگری در حوزه حمایت از خانواده و فرزندآوری سخن گفته است. زاکانی اعلام کرده برای فرزندانی که از سال ۱۴۰۵ به بعد متولد شوند، حمایت ماهانه‌ای در محدودۀ ۳.۵ تا ۴ میلیون تومان پیش‌بینی شده است. او هدف مجموعه این بسته‌ها را کاهش بخشی از بار اقتصادی مردم و دولت عنوان کرده است.
🔹
هم‌زمان با این روند، انتقادات از زاکانی در فضای سیاسی و در میان برخی اصلاحطلبان شدت گرفته است. این هم‌زمانی افزایش فشارها با ورود مدیریت شهری به طرح‌هایی که بخشی از بار اقتصادی و اجرایی دولت را کاهش می‌دهد، یک پرسش سیاسی قابل تأمل ایجاد کرده است.
🔹
اگر شهرداری در روزهای جنگ برای اسکان و بازسازی خانه‌های آسیب‌دیده هزینه می‌کند، حمل‌ونقل عمومی را رایگان می‌کند، فعالیت عمرانی شهر را ادامه می‌دهد و در دوره تورم نیز برای تثبیت قیمت بخشی از کالاهای اساسی وارد میدان می‌شود، دقیقاً کدام بخش این اقدامات باید محل نزاع سیاسی باشد؟
🔹
پرسش زمانی جالب‌تر می‌شود که دولت مستقر، دولتی است که جریان اصلاح‌طلب از آن حمایت سیاسی کرده است. انتظار طبیعی در چنین شرایطی این بود که هر ظرفیتی خارج از دولت که بتواند بخشی از فشار اقتصادی، اجتماعی یا اجرایی را از دوش آن بردارد، دست‌کم در همان نقطه مورد استقبال قرار گیرد؛ حتی اگر مدیر آن مجموعه از رقیبان سیاسی دولت باشد.
@Fars_plus</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/466085" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a5ec1fd8.mp4?token=lTNN3AbKPSN665z3CXRO5qU4pbt4_GlGBCkCtv79kd5K4vUbDo2oTTHSO0t7b21h_3eINuqEBA7X8v6S2ekDSpB7W0aVNOO6MC29tZQLldF0RAnwvBnzoXrCbzb-3PFnnq7J75BknaYIjOr8izngLwslnZ9RzcR1HHHEsr_mAtfrZ4Hq1ykM1evpjb0DlYjaUUKFrRMEdptt6nnRLd3tPR-ys_n4NL4EdUon8zJShaF9TKxWxRe4q3gmYsuLlvpkQeRADV737_9dE_AG9MvUD1F59JHwfZNba5FeNQtQxOjCWqXcsIlTKpJd9eGXVvWvm2DxnkgdDqfTnllXpZfPQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a5ec1fd8.mp4?token=lTNN3AbKPSN665z3CXRO5qU4pbt4_GlGBCkCtv79kd5K4vUbDo2oTTHSO0t7b21h_3eINuqEBA7X8v6S2ekDSpB7W0aVNOO6MC29tZQLldF0RAnwvBnzoXrCbzb-3PFnnq7J75BknaYIjOr8izngLwslnZ9RzcR1HHHEsr_mAtfrZ4Hq1ykM1evpjb0DlYjaUUKFrRMEdptt6nnRLd3tPR-ys_n4NL4EdUon8zJShaF9TKxWxRe4q3gmYsuLlvpkQeRADV737_9dE_AG9MvUD1F59JHwfZNba5FeNQtQxOjCWqXcsIlTKpJd9eGXVvWvm2DxnkgdDqfTnllXpZfPQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسوایی در کپلر؛ آمار نفت ایران دست یک سلطنت‌طلب
🔹
مسئول ارشد آمار نفتی کپلر یک ایرانی سلطنت‌طلب با نام همایون فلکشاهی است.
🔹
عکس پروفایل فلکشاهی پرچم جعلی ایران بود اما پس از رسوایی اخیر، او عکس پروفایل خود را تغییر داد.
🔹
کپلر پیش‌تر مدعی صفرشدن صادرات نفت…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/466084" target="_blank">📅 20:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c08f93b8e.mp4?token=GAZlABn6bqlXjKEj-w2sgMEiOa38GoMg619UhLi5t1i3X-aDyu1GBpKsShazATej1ucQAcm7eRrvCJYbnv89X5IAnOaCYtj6E0-CtW0RAOFzbaDAdrrjoMvtORtS3NDczEFsSQc7zV5q0I05Vw95o5rkYXPa0kTm47urup2WkYGEEAZR4lOHPSM91queTeLjog9FNNkdKb-KPO4w9zWV5Ro2P06GRB5XUMWfgStrFK3q2njPDdJDZGY4Yw40430RynL6Adv5OAk9hYfc9OiWjgBXkqnOItP-xIUhxPTESPJp4kEgdC6cUDYRtyVOtM9axcu7vwv8wu4Np7xd94peskJx6OiZzaolVqgLaPCGMwQDU-qG9DNO0TT820b949Exbuan3eq1htnr2Xo1kPaJnkD-W1xE-BOmu04eeeUWvlNHlvFB_El75ifIlFRVl-KcPiYrSf6BXvLU-uqp7pKd1QfXd6V9Wy4BEiuGBkXKiyOB5t3FG-UO4ncrxwbavXdYyYSzDKzyIe-HuhGO7J6Ht1PwmBkHQfaeln9uJGifzHltm8Hop90neHbB9AJ6HZfhQq3W1ebmyI5TgwXYh2sasGc0TZVRsrRLSZQiqZCC0EsIID6T05XrJRt0wR6nxKi2oo7d3teymqrh6Azqaew3Rmylu6VaYZ5DYsSg9ZA6Oi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c08f93b8e.mp4?token=GAZlABn6bqlXjKEj-w2sgMEiOa38GoMg619UhLi5t1i3X-aDyu1GBpKsShazATej1ucQAcm7eRrvCJYbnv89X5IAnOaCYtj6E0-CtW0RAOFzbaDAdrrjoMvtORtS3NDczEFsSQc7zV5q0I05Vw95o5rkYXPa0kTm47urup2WkYGEEAZR4lOHPSM91queTeLjog9FNNkdKb-KPO4w9zWV5Ro2P06GRB5XUMWfgStrFK3q2njPDdJDZGY4Yw40430RynL6Adv5OAk9hYfc9OiWjgBXkqnOItP-xIUhxPTESPJp4kEgdC6cUDYRtyVOtM9axcu7vwv8wu4Np7xd94peskJx6OiZzaolVqgLaPCGMwQDU-qG9DNO0TT820b949Exbuan3eq1htnr2Xo1kPaJnkD-W1xE-BOmu04eeeUWvlNHlvFB_El75ifIlFRVl-KcPiYrSf6BXvLU-uqp7pKd1QfXd6V9Wy4BEiuGBkXKiyOB5t3FG-UO4ncrxwbavXdYyYSzDKzyIe-HuhGO7J6Ht1PwmBkHQfaeln9uJGifzHltm8Hop90neHbB9AJ6HZfhQq3W1ebmyI5TgwXYh2sasGc0TZVRsrRLSZQiqZCC0EsIID6T05XrJRt0wR6nxKi2oo7d3teymqrh6Azqaew3Rmylu6VaYZ5DYsSg9ZA6Oi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی جفری ساکس هم از ادعای برخی جریانات ایرانی تعجب کرد
🔹
به‌جز ترامپ و برخی افراد در داخل کشور، هیچکس از احتمال «سوختن کارت تنگۀ هرمز» برای ایران صحبت نکرده اما این عبارت هنوز از زبان برخی کارشناسان داخلی تکرار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466083" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekJBzh5aDeRJz03sc8jbFY5c9DM5s1YM4qPxd-TQ8bjEeBSuuPZctLETQP4RGWjEYmIe6Pnup3tRVauDccx9TxYintBVPTTHdmM5bHcjr7UK6gkSAqiYli8agvqrQG-zI2ezAWpp0o1C9Y9A7lBAXX8f2RIW7AlDQWuexhDIpoOlupyuhg2eiA0UuANT8M7rDdl9pNi6cz-PUDWxE_ffhbsuYtAsrQj0QJpnWOhUz8u-c_AXnIUFoC96p4wmqMMRHkI1gXHkNMOg2WvH7CuDecfJRjYPZn6bOHb3X0-Z_NEdKl0BgCqz_Sx3phcwRSrx_YxSf20kDJy3XXj96c1A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم حبس الناز شاکردوست در دادگاه تجدیدنظر تأیید شد
🔹
شعبهٔ ۲۳ دادگاه انقلاب تهران، الناز شاکردوست را به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیری محکوم کرده و به‌عنوان مجازات تکمیلی نیز ۲ سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری برای او مقرر…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466082" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9685b35a01.mp4?token=JpoejihadRn_8K7fEHT4jnboXptRsZAQpRFkDwUCgd7rrJdhuy_d-Un7O8nNVGpkAsf1bfk31UHqwxl0rOXUG0ofLVyIPM068f3FKXUJ-ljJgg2PDpZbqWPo57TzTAiau3dxaR-3MMuXptpR2inH-ODCuoToSBgL9IEkyybGscKQ5lCryB9IREKFyytccHMXv3ZwHBZ_cqy6ShoEAwlW8pYerkeL8rFrr4v6lDd14Vsql-g8c1z3ZUDtdys632u_o8W650ELvcn4Z-vL8wbiQNzTg7479Utx2VsGk6c370nLu7LXTM2AXF9ip8FuuVCcSHUzv0dsrs3fz53jDcxirQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9685b35a01.mp4?token=JpoejihadRn_8K7fEHT4jnboXptRsZAQpRFkDwUCgd7rrJdhuy_d-Un7O8nNVGpkAsf1bfk31UHqwxl0rOXUG0ofLVyIPM068f3FKXUJ-ljJgg2PDpZbqWPo57TzTAiau3dxaR-3MMuXptpR2inH-ODCuoToSBgL9IEkyybGscKQ5lCryB9IREKFyytccHMXv3ZwHBZ_cqy6ShoEAwlW8pYerkeL8rFrr4v6lDd14Vsql-g8c1z3ZUDtdys632u_o8W650ELvcn4Z-vL8wbiQNzTg7479Utx2VsGk6c370nLu7LXTM2AXF9ip8FuuVCcSHUzv0dsrs3fz53jDcxirQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان قم را درنوردید
🔹
طوفان و تندباد با شدت ۹۰ کیلومتر بر ساعت به همراه گردوخاک شدید قم را فرا گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/466081" target="_blank">📅 19:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پیاتزا: بیشتر از خودم برای مردم ایران خوشحال هستم
🎙
سرمربی تیم ملی والیبال:
🔹
از همه مردم ایران حمایت‌ها و پشتیبانی زیادی گرفتم. واقعاً خوشحال هستم، بیشتر برای مردم ایران خوشحال هستم تا برای خودم.
🔹
من در رویاهایم به یک مدال دیگر فکر می‌کنم که به نظرم آن مدال می‌تواند از این مدال مهم‌تر باشد.
🔹
من در حال پیر شدن هستم و زمان برای من محدودتر شده و امیدوارم به این رویایم برسم. در ایران استعدادهای بسیار زیادی هستند، اما باید بدانیم که استعدادها را در یک مسیر درستی قرار بدهیم. اگر بتوانیم این کار را درست انجام دهیم، می‌توانم آن رویا را در سر داشته باشم.
🔹
امیدوارم صلح در ایران برقرار باشد. به نظرم صلح در کشور از موفقیت ورزش در کشور مهم‌تر است. من دوست ندارم در دنیا جنگ را ببینم. مهم نیست چه رنگ پوستی، چه نژادی و چه کشوری باشد. ایران منابع زیادی دارد و به همین دلیل معتقدم که می‌توانیم در این کشور خیلی خوب زندگی کنیم. در کشور شما همه چیز هست، خیلی‌ها ما را حمایت کردند و تعدادشان هم خیلی زیاد است.
@Sportfars</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/466080" target="_blank">📅 19:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2S2pyKzjjSGm2RFd3EtRLyIN9xVTw4XfXkUPseHEvQdgw0sy00pH-Umu28yq47xUCXY5PG-bGfw3wB6GEiRwHSh1r6Drz_FJcJD0aXUq9vxyzE2Zjww2doGJK0Umsn3L6bUQHwCD5UZRankMsIoNYmdcA9by3e-IIJwZOlhY6SyNu8H5eWfymXP4NDD6sy1PhJqtVcan_sCtc4VjAWupC-n7T7e7XDVqHQ963SwbEVIh408RFZS1HdzWWZEoOnR71gDfja3saS7kOs_h36UVO9Gm5GUun9y3NzMOcSpy_LA_Gd5G8GJifyFSU8xPaq7x4vZh21oaE9ylXXlnSAvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام ترامپ در شرکت‌های آماردهی تردد از تنگۀ هرمز
🔹
برت اریکسون، تحلیلگر حمل‌ونقل و امنیت انرژی، با اشاره به تصویر پرچم شیر و خورشید در پروفایل «همایون فلکشاهی»، رئیس بخش تحلیل نفت خام کپلر، نوشت: «اگر کسی بخواهد به دستکاری داده‌های نفتی فکر کند، کپلر…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/466079" target="_blank">📅 19:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f1cbb697.mp4?token=Kx8AgnF__rrXS7SdpHCQT5ARGpkdZ_l-_24eAO4rdtLhGmCfeibjbeqF80K_X9LBxLRwszy8bBwIz6mJvlfwj10VYwTHVulPtgglnUlWq_1mmtc2Sa0RcCPnUAD0n6nQA4Xt6Q_JGt8ZerScEnFJwAV-lWJerMl4LgCbqappseumrEfpD85zods8TyXt-UsViQoIi5-BJFmwuPVcVieU4otDxH0pLgmF2J386olVDc2TS1vopZuEBk17SaC4AjFsuw3K8wIt1GS3py8In7N9h0Rj9mlhQsrnCsA3rtGWCZl5cjeqvZev8fOlW8h9qwA2_qh7l-UVgvo0v5KcKGj0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f1cbb697.mp4?token=Kx8AgnF__rrXS7SdpHCQT5ARGpkdZ_l-_24eAO4rdtLhGmCfeibjbeqF80K_X9LBxLRwszy8bBwIz6mJvlfwj10VYwTHVulPtgglnUlWq_1mmtc2Sa0RcCPnUAD0n6nQA4Xt6Q_JGt8ZerScEnFJwAV-lWJerMl4LgCbqappseumrEfpD85zods8TyXt-UsViQoIi5-BJFmwuPVcVieU4otDxH0pLgmF2J386olVDc2TS1vopZuEBk17SaC4AjFsuw3K8wIt1GS3py8In7N9h0Rj9mlhQsrnCsA3rtGWCZl5cjeqvZev8fOlW8h9qwA2_qh7l-UVgvo0v5KcKGj0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌گرفتگی در جاده اشتهارد پس از بارش شدید
🔹
درپی بارش شدید باران، بخش‌هایی از جاده اشتهارد البرز دچار آب‌گرفتگی و سیلاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/466078" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d6303657.mp4?token=HejE5KMPpxvdjmukEm42lPVQUspqtNqlPcslvghXCA4aGF6w51FmQP-6s4saHkb72ueR6kpU2gpUPSWEgn_7-K6pFamz1rMFp0LmngggFnjaryEvPSREJYNIyP9-wgVjucrape-YtekjlMj6XklBJI57YG_WO_5fsgZ7e07oWCjuAbDXEREKRSZnZvRlFTGA7QiXxPqAi-MvTOKUrQVdB_Ww10IZ_QySNwSXwHscoKi2ydtrzL4Lj96xj4P0Fzod-YaqRHp7tq1QHTRLMVBWWn32o6yFHcVjgP406vrUZa8-g8My3AoKB1_8M3z3arI6XyDwfXl6Xct9f1sGmYL6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d6303657.mp4?token=HejE5KMPpxvdjmukEm42lPVQUspqtNqlPcslvghXCA4aGF6w51FmQP-6s4saHkb72ueR6kpU2gpUPSWEgn_7-K6pFamz1rMFp0LmngggFnjaryEvPSREJYNIyP9-wgVjucrape-YtekjlMj6XklBJI57YG_WO_5fsgZ7e07oWCjuAbDXEREKRSZnZvRlFTGA7QiXxPqAi-MvTOKUrQVdB_Ww10IZ_QySNwSXwHscoKi2ydtrzL4Lj96xj4P0Fzod-YaqRHp7tq1QHTRLMVBWWn32o6yFHcVjgP406vrUZa8-g8My3AoKB1_8M3z3arI6XyDwfXl6Xct9f1sGmYL6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش در آرامکو همچنان زبانه می‌کشد
🔹
تأسیسات وابسته به شرکت آرامکو در جنوب ریاض از بامداد امروز دچار آتش‌سوزی شده و به‌گفتۀ رویترز، پس از ۱۲ ساعت همچنان دود و آتش از این تأسیسات بلند می‌شود.
🔹
رسانه‌های منطقه پیش‌تر از حمله موشکی و پهپادی به تأسیسات آرامکو…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/466077" target="_blank">📅 19:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD3h5HY-hoCoiYhkhV4qb-xYJ2Zxf1CBug44eC70XCa7sqKas8lrTjfsZ4ffGXuQ9Ry_qSdB0cZhxt8PgwyBzQsC07_q_Gr-fqpRPOZ-inT0SgoNpjHtxF0AcD8mccr83Rm1Fb6lX8MmuSdvdMs55OgCVZjzUzFuqui1wO-54NKGb54kppnJZ1fII-ARi4Ssp97NcGuxctUdMzOviCbkxsxzEJPgBHoj4h9Gccmf4Tak2gJAwYMFxZkYS54oDqOK0fp0SkzVbTuhBDYqZCT9IaWs3IJN7W3HSKv2xOo2jY_bpqX-XgpZ1iiC3oawcZFLeF7pwfAXdahw0BiI-dSb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466076" target="_blank">📅 19:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf47e0e13.mp4?token=gHrbi0Apbhgjwi4LjegKAmNCZ2BXS9yEVEpxRh5F98Hl3nE7gJ3IJPxe00IXCY6WzBPjiL0JYRPsv3DZuG1MY5WZnBwj4nhH-44FmfbBBJuF1TXlp6tqzEb99KX4eM2jqISoY39MucQUOSym6iFlf0JXB1URT6PXA6tOmUUx5I8x2YkaKTaN3Sz5YTFRRAWglQlhH_oieVlV_1uJLtdO3pZXQhXAviZe4R_w3Cl2_LKRt8XF43R398MiueeXAjs_XpS9BXBbpSGJHzIV_s68ntVES9jGMAIBms6HGBgkkVZ9xYj-HvBTtdqNB0u44DedOdwkzpg0lM_9ShW9Xcac5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf47e0e13.mp4?token=gHrbi0Apbhgjwi4LjegKAmNCZ2BXS9yEVEpxRh5F98Hl3nE7gJ3IJPxe00IXCY6WzBPjiL0JYRPsv3DZuG1MY5WZnBwj4nhH-44FmfbBBJuF1TXlp6tqzEb99KX4eM2jqISoY39MucQUOSym6iFlf0JXB1URT6PXA6tOmUUx5I8x2YkaKTaN3Sz5YTFRRAWglQlhH_oieVlV_1uJLtdO3pZXQhXAviZe4R_w3Cl2_LKRt8XF43R398MiueeXAjs_XpS9BXBbpSGJHzIV_s68ntVES9jGMAIBms6HGBgkkVZ9xYj-HvBTtdqNB0u44DedOdwkzpg0lM_9ShW9Xcac5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان قم را درنوردید
🔹
طوفان و تندباد با شدت ۹۰ کیلومتر بر ساعت به همراه گردوخاک شدید قم را فرا گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/466075" target="_blank">📅 19:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8ea1125f.mp4?token=UA-Qq3EYk1rOOJ728eac24LIaLR09T9QirCHfxIg8hAXWqT76Ri5JYaP65Nxvdi-RYED9VrhqIVEzNj3r8IuHD06aQ0KK2q42IlQ0iZzxn7x59Ez_V_SWp_R0BifhAInQvQUUjaKO0sxapLEvZoVaDoM5oIX6L5dgbesAydSIMQWp_nAy8qDSb-VOkRPcQ-K0SWGliKy3YP9GEG44j29YYJH_vH22-wP8aSoVD7XO4nXJfH772Ua4-4s3nRWfyQb2rK0q750WxaLTGARJ36BBcxofwMhmXLF3Iv_UDyMwS8MKn_JabTeKMiTjpxcRn-Btcp7VvgnFWIBCPlXUFB2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8ea1125f.mp4?token=UA-Qq3EYk1rOOJ728eac24LIaLR09T9QirCHfxIg8hAXWqT76Ri5JYaP65Nxvdi-RYED9VrhqIVEzNj3r8IuHD06aQ0KK2q42IlQ0iZzxn7x59Ez_V_SWp_R0BifhAInQvQUUjaKO0sxapLEvZoVaDoM5oIX6L5dgbesAydSIMQWp_nAy8qDSb-VOkRPcQ-K0SWGliKy3YP9GEG44j29YYJH_vH22-wP8aSoVD7XO4nXJfH772Ua4-4s3nRWfyQb2rK0q750WxaLTGARJ36BBcxofwMhmXLF3Iv_UDyMwS8MKn_JabTeKMiTjpxcRn-Btcp7VvgnFWIBCPlXUFB2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران، بالای بچه‌پولدارهای آسیا قرار گرفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466074" target="_blank">📅 18:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmik3mGjD7oRj430XWIRABqZ-t41Dw70mGoORX-0OMC_96su3Z1ONoRy9uV8ifHh-y7NHbjJvJEicycngXwU1X85bKRhTt1yvPx0-X2pnVoLGDKUlsgTpTahdAVynSBdj55QqebUElTd04GS1Be3h7RdVmmiRI0tJETdOi15DEiTY6OLrWSGJAIadAhakLTCEsa8QGPpkJqLQEGUeCmnNzLkwqVBwiyhjSZj1anlHSZvl1O4hB5zKtM-o7bDuzm8AG4oBqo9d_kn0L1EXsOH6pm21y_zoTReGJbNksz4kZ8osvHwmenIlYItB7W1ec686gty12wrZfdtwbFBiry6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZ2UGha1WJFhshAxWoNwnT07UmJa1UpIDkbq30Yj8FK14p4dLjUH4LZVijRJHl5nZkuJ7-jYrJlZEJdqNTa4l7lFU__YuGHZSjS2LczO7NapbWDCxaM12cFdeE-FQb8HsYMmPvYV7OALp5fyHQ-CTsI2wZoFqpOePMXf92L8PcI8yuXldaLsFlTtQgWc1hiFXmAzr5Dnp5dUKi8dWgq3CVQxbo_M6rUl_RVxerQCoADRdgz7VdmCjJAbX9m5wzuQ9APIMMEHjj_099iZ6aS2OrjcKDOX4UW3Ps14PfLztH9qcvruOfFoSLwXEiqji45iLZBTFCvAzBKUFiYRcwRKhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والیبال ایران با قهرمانی در بازی‌های آسیایی از ژاپن انتقام گرفت
🏐
ایران ۳ - ۱ ژاپن
🇯🇵
۲۶ | ۲۵ | ۲۱ | ۲۴
🇮🇷
۲۸ | ۱۹ | ۲۵ | ۲۶ @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466072" target="_blank">📅 18:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466071">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e99023fc.mp4?token=R-PFG04yEdtCVL9DUXCC03f-4SWEId6HIt91QcfSuBcap-OvdBxS9mPexCy_LaCgO2bAPsQx0I6DLKJTpWc1Y--R5lSPqgUDMl1nXfHsLEZUACb3oNb2WZtYmg8HxgQg44Gk4h7wlZ1FQpI6KBFGV73qnlTRwVbw_ihDKG1vzO8iqi3Ao1nafL2t7XTzSOo8eOrtoSmRxutfFUmddYP86yBaym1oQ-kqKrnSGzV9odKR0IYMGTGp3sDaeYBNrZyERGIQcGNq0Vkinq4FPgPGaUGlaPZMLKsyNDxgx8uBMoV4j0M9lNBaQ2q_GVpzAUxtIJ-Di2_Nsyz7WCxOxJVi4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e99023fc.mp4?token=R-PFG04yEdtCVL9DUXCC03f-4SWEId6HIt91QcfSuBcap-OvdBxS9mPexCy_LaCgO2bAPsQx0I6DLKJTpWc1Y--R5lSPqgUDMl1nXfHsLEZUACb3oNb2WZtYmg8HxgQg44Gk4h7wlZ1FQpI6KBFGV73qnlTRwVbw_ihDKG1vzO8iqi3Ao1nafL2t7XTzSOo8eOrtoSmRxutfFUmddYP86yBaym1oQ-kqKrnSGzV9odKR0IYMGTGp3sDaeYBNrZyERGIQcGNq0Vkinq4FPgPGaUGlaPZMLKsyNDxgx8uBMoV4j0M9lNBaQ2q_GVpzAUxtIJ-Di2_Nsyz7WCxOxJVi4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران امروز هم مهمان تهران شد  @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/466071" target="_blank">📅 18:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vujnH0ShjRw5QD50WgNyz3PeXcz2_mjh9SSxXY2i8vDEw4pElKilzMRVON_guNZbc-MtZwgJyQp0S5Gu0bmtVa2hOn7QWECJPmJJOfvbHjaT188hMOg7ldvQl0MS_L2ZuqQP1gF-ytDd_uOffUBtt_nan83x_O-YwWxZYJX5Hu6lOLxIaFsaAhboGiK0cqbq-TssCS6mxVLj-b7owt9NmH7hybZ2ctK1JXvOhtRlXKM05myXeoBwPKUM8-EEOOaULE0mXMF_9esq7hS25VQKw21gc4ZMGLCazhIBAW2GlJZRVqvVEKvZAzL3RqtYJOavvs9a7Cdk_Y16-CfPl14frA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: کشوری که عمرش به نیم قرن نمی‌رسد دربارۀ جزایر تاریخی ایران ادعا می‌کند
🔹
تنب بزرگ، تنب کوچک و ابوموسی ایرانی بوده‌اند و ایرانی می‌مانند.
🔹
تجربۀ منطقه نشان داده است که امنیتِ وارداتی تاریخ مصرف دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/466070" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466069">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIztK3JKykuMQNlrU85o_-o2kj54fbspcj7gk5OzuniQExdQcQYHYgKDXlULwy0a2Tha9XjIGd2uwxoLpSfoxwkxXDyxGQ4rtCKOcQweovWy112cRvIJbBpuS4qgqD4NcNqRe55s9FqRTe1eI-3cqXN7gOJUj4-H3iA3SfCsuTAQSIwQftjl-OBF32WY33NwhX9QVmmqMhWkQd8y5LPEU676bRvPts9nvlkObPD-Nbg_t7kKuYf7yRT1CppR8Ywqj3gqzX_gCxALdAkf4hYXNILDqnpIclo6pdmoSaUCmBdfhm2GT0aVFirSNvo74zntCNmonSyzpf_SYkbv4tcT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیاده‌نظام ترامپ در شرکت‌های آماردهی تردد از تنگۀ هرمز
🔹
برت اریکسون، تحلیلگر حمل‌ونقل و امنیت انرژی، با اشاره به تصویر پرچم شیر و خورشید در پروفایل «همایون فلکشاهی»، رئیس بخش تحلیل نفت خام کپلر، نوشت: «اگر کسی بخواهد به دستکاری داده‌های نفتی فکر کند، کپلر واقعاً این کار را برایش راحت کرده.»
🔹
کپلر به‌تازگی مدعی شده صادرات نفت کشورهای حاشیه خلیج فارس، به‌جز ایران، در ماه سپتامبر به دست‌کم ۱۶.۵ میلیون بشکه در روز رسیده؛ ادعایی که تحلیلگران با توجه به ظرفیت کشتی‌های کوچک عبوری از تنگۀ هرمز آن را زیر سؤال برده‌اند.
🔹
آخرین نقشۀ موسسه واشنگتن هم نشان می‌دهد که حداقل ۲۰ نفتکش در یک ماه گذشته در تنگۀ هرمز هدف اصابت قرار گرفته‌اند. در همین ۲۴ ساعت گذشته هم ۳ نفتکش در مسیر عمانی آتش گرفتند.
🔹
رئیس بخش تحلیل نفت خام کپلر، چند ساعت پس از انتقادها، عکس پروفایل خود را تغییر داد.
🔹
اکنون با توجه به تناقض میان آمار کپلر و گزارش‌های میدانی، این پرسش جدی مطرح است که آیا گرایش سیاسی مدیران این شرکت بر داده‌های منتشرشده دربارۀ تردد نفتکش‌ها اثر گذاشته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/466069" target="_blank">📅 18:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdzfRIrieons3v3r15No2dTlf_WvFI4faw2gLQNX5sY06NE63yopTtzcdIKS4yP2azg8vJG3orUR6JRBejbm4GCjE6bEQHE24JRWr1yCnBLtycv2LgI6yuJr-MeAHplzlUP0BBPAHySVgo3SM6Vyg1aJ96nbYcrGkLKvqsB0gydJ_WpitEJ41e4Pk49Iphk8p9PUC7-ekSQ42iR9x5Klj9_kgwgPxpyIL8e6ibbcYbqf_ciWm4lassOqZ5zNgAidswI3s4P9cZLCW7m_nfUL1S1Nh5BATy0C5JkFrTdb8WJS4ujpcD6v6mwVydCfeIS68_ELiNc1MhXvJnHfF6z1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک نفتکش در مسیر غیرقانونی تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد که بامداد امروز سمت چپ یک نفتکش در فاصلهٔ ۴ مایلی شرق عمان هدف قرار گرفته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466068" target="_blank">📅 18:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f843506628.mp4?token=F3R5entoxRJv_GPHEMDIurJUdLaXxP8I02dOGm06_MdL11x1CUdYGyfID13Iqbrkq5ldsaP-6EZSzEyO7UCnRYCWnWRwVZZvlsM01C-7OOw6QsBEQ4LIht6mTw9Clk-dhBCIQPUYDZBexki17uvRhlEI2nyGrVas70O_Y4nw6Vz5Y5MW_Se4SqJSNWfKyOxjDq0g0blcS8yDfqRxUxso17-6GaLOm7sgWjr57L1psUf3fvKxxrb1D4djSAKj97aaf9Gm5SGNmHbcjaC5zE-YIWd1FC_Soc4yb8DlxftsQfgOHiev9nTG503k8JIheEZZRWRPfrSopBwDht1Sw7xgwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f843506628.mp4?token=F3R5entoxRJv_GPHEMDIurJUdLaXxP8I02dOGm06_MdL11x1CUdYGyfID13Iqbrkq5ldsaP-6EZSzEyO7UCnRYCWnWRwVZZvlsM01C-7OOw6QsBEQ4LIht6mTw9Clk-dhBCIQPUYDZBexki17uvRhlEI2nyGrVas70O_Y4nw6Vz5Y5MW_Se4SqJSNWfKyOxjDq0g0blcS8yDfqRxUxso17-6GaLOm7sgWjr57L1psUf3fvKxxrb1D4djSAKj97aaf9Gm5SGNmHbcjaC5zE-YIWd1FC_Soc4yb8DlxftsQfgOHiev9nTG503k8JIheEZZRWRPfrSopBwDht1Sw7xgwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«میدان هفتم‌ تیر»، دومین پایگاه آموزش جانفدا در تهران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/466067" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b6addc4f.mp4?token=cATjXKOv-8QoTxD019F5KGCnGrLtQy_0b4P7K3d1FKsi4cdPfPq6UBg_XvIg50jpsX8Fe3X6MniUOnIKIJpNdmeejUIb4mHeazDXQW4uOMyY3cDEHvW5TlazgGVz1SE8lcqCwzMTOla4XtTQJQIKqoh7OM0LLrFA8HamLuyqiFHJLlWXi4uL3i4r9tOjOBkRFMj7CGdIg01UxBfq53YwG-ZP5lyhxg-6M4sI1aYt26pwtuyqAlEHy1qwOghQHL9tCd2sa5REaoxhDdLOBU7TUYgU7LVfcnZordw0XC0KNtstUkiNNcFiwlWsw_NRxHzZBkQxAYH4TOU1-wvhRgjZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b6addc4f.mp4?token=cATjXKOv-8QoTxD019F5KGCnGrLtQy_0b4P7K3d1FKsi4cdPfPq6UBg_XvIg50jpsX8Fe3X6MniUOnIKIJpNdmeejUIb4mHeazDXQW4uOMyY3cDEHvW5TlazgGVz1SE8lcqCwzMTOla4XtTQJQIKqoh7OM0LLrFA8HamLuyqiFHJLlWXi4uL3i4r9tOjOBkRFMj7CGdIg01UxBfq53YwG-ZP5lyhxg-6M4sI1aYt26pwtuyqAlEHy1qwOghQHL9tCd2sa5REaoxhDdLOBU7TUYgU7LVfcnZordw0XC0KNtstUkiNNcFiwlWsw_NRxHzZBkQxAYH4TOU1-wvhRgjZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید تگرگ در دزفول خوزستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/466066" target="_blank">📅 18:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466065">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqmg7e6BY2Ghh9F13aubsa8biQj9HFZ03jtbZHKthPnabbzyKzwAJRAqzUAnyK7hAinoFDr2VlBOGefNqslZP_Qfcjvjl0nVouoHc0DB_TdPumnC6iSsYOYNPTbhGHTV-Sy1_JMbHZZQ1GQBOSdr0PFa1zhkB2QQ7hGX7Fs1kM-PoIo3JbQRi0GftgBKQ0b_k6oT193eM4YR8Wv7zraaKOzyuJT6Uy0tQILZvQRXcMqlHRiCA9K329KUNsDLCaj_GnXk21yZN8CIaHwobIg08VgLF2yukaNKrdGKu3bfd138csycHikY_m-1fcB-DiiL4QpObIckoRm2ALZeaU64DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله: پایتخت را در برابر پایتخت هدف قرار می‌دهیم
🔹
حزام الاسد، عضو دفتر سیاسی انصارالله یمن: حملات عربستان به اهداف غیرنظامی در صنعاء، مانع ادامه عملیات نیروهای مسلح یمن برای بیرون‌راندن نیروهای تحت حمایت عربستان از تعز نخواهد شد. پایتخت در برابر پایتخت…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466065" target="_blank">📅 18:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwgw0YO27eVPXlhA6NrsXAyKZJ3hrv4Zx_-vcqJYa2X2JYYMjNWadadFMWJmRDQJckk49M-CUg8yTslEU48yYo6nF9fan5X6Fb0JDCB5ia28QaqYxL9uA4yQ49yhgPBoIgugfk6wn0qmnA2NXYTYM3v6RfM3lWRHQy60RwC4t3MVhO_vhwFbMpv3ivxSjvcFunm9i02WqQu4yuUV-7Gce_hAQQnr6oTv2x6IEYE59mWIQ9h4-Sqa4Hyy4_YfKhVagnUNpGKvpb8YHJfISDpLJz9vynu73SvKBOhKukX6AWid9QHV6_HSeSq7UNRYBIGW-mGDUkyB9nXbi0-VKsjr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ «بدیم بره» اصلاح‌طلبان این‌بار برای تنگۀ هرمز
🔹
تقریبا از زمانی که تهران از مدیریت ایرانی تنگه هرمز رونمایی کرد و اثرات اقتصادی آن در اردوگاه دشمن نمایان شد، برخی از چهره‌ها و رسانه‌های سیاسی سعی کردند تا از اهمیت این آبراهه استراتژیک بکاهند.
🔹
تیتر…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466064" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ca0ecb9e.mp4?token=Ze5L94PIdI_a6pS_JqNfGqfw5mUxTw1O9byEhDOqvYHl0I3d0VgmLqv0LkVITEUmeXfYtti1n0KJdpOe81CCYGJTOoQBR-1ucmGWmqklN95Nx1MNhaKCFVjC2rptIaou3QkmEAfd5H0HiggQRhG0it3vp0PyNSKxfoz2SZHopYaddvAalmGMg-ndhJW3d66aSXSxi8PjkRnZ2G81OzC49QVVc46__5gXGfCtwDcy4A0Gp5ZREmgdcQ8e77Ay1lvszq9y-ei-iFWIeSAxOKUdctupwVKH0QhEmlf911N-FF06jZ5D-jt0oeWM4wD8j0oKq36FXZzTcaScavy1waLwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ca0ecb9e.mp4?token=Ze5L94PIdI_a6pS_JqNfGqfw5mUxTw1O9byEhDOqvYHl0I3d0VgmLqv0LkVITEUmeXfYtti1n0KJdpOe81CCYGJTOoQBR-1ucmGWmqklN95Nx1MNhaKCFVjC2rptIaou3QkmEAfd5H0HiggQRhG0it3vp0PyNSKxfoz2SZHopYaddvAalmGMg-ndhJW3d66aSXSxi8PjkRnZ2G81OzC49QVVc46__5gXGfCtwDcy4A0Gp5ZREmgdcQ8e77Ay1lvszq9y-ei-iFWIeSAxOKUdctupwVKH0QhEmlf911N-FF06jZ5D-jt0oeWM4wD8j0oKq36FXZzTcaScavy1waLwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران امروز هم مهمان تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/466063" target="_blank">📅 17:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce2245da0.mp4?token=o2CUrk-zid4wGTF2wxbDeozbj14VZuBqqlxazoqplZr4SuvfSoaPTIyKkk6oQwICmrZYVl-V9CDd2CQDnaSvUwX1PmEyf4JvZtVAGLeZOIhj4WA-IToplXO7GIt4cE-buMYsgE7AkWS4o3Jg0muWVpITuiPjCrn9gq5E4xo3-s-LAHz_llVaSsXlOldNZ3wLx3xpH4nLahBxoxFNkTZod0he03Uuqm8G8TP2C2m8naaIaFipXd7IXDSMDRut-7aYXnugrOruPapYJ8Ryu5gXF0QBwdAYTylsys-lUiKSH54pR5hiG65bd4_XvKs8YcD7-QbUaKqXrs1pDB96airgKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce2245da0.mp4?token=o2CUrk-zid4wGTF2wxbDeozbj14VZuBqqlxazoqplZr4SuvfSoaPTIyKkk6oQwICmrZYVl-V9CDd2CQDnaSvUwX1PmEyf4JvZtVAGLeZOIhj4WA-IToplXO7GIt4cE-buMYsgE7AkWS4o3Jg0muWVpITuiPjCrn9gq5E4xo3-s-LAHz_llVaSsXlOldNZ3wLx3xpH4nLahBxoxFNkTZod0he03Uuqm8G8TP2C2m8naaIaFipXd7IXDSMDRut-7aYXnugrOruPapYJ8Ryu5gXF0QBwdAYTylsys-lUiKSH54pR5hiG65bd4_XvKs8YcD7-QbUaKqXrs1pDB96airgKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض به قیمت بنزین، سخنرانی ونس را مختل کرد
🔹
«بن براور»، نامزد دموکرات مجلس نمایندگان فلوریدا، در جریان سخنرانی معاون ترامپ، با فریاد به قیمت بالای بنزین، جنگ با ایران و پرونده اپستین اعتراض کرد.
🔹
او با کنایه از ونس و ترامپ تشکر کرد و گفت: «ممنون بابت قیمت‌های بالای بنزین و پروندۀ اپستین.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466062" target="_blank">📅 17:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCJR6CuOSBHWImlb1yowILvAHeezQs2-O-jhTUCFeGLhiBPnqKpoxiVISajNbUHe_X4T71cXldVlVUodz6AyB_OVRUgPej2Z2KC_ofonLWg2ORBTxN3ckYEk0h56DY5majF3fr_BBqBpxUVN6WjNOjnk3kL3R9ak6o2yg7lSsOEYoVQwBrYk9KsFkQWvmhySNPD9zQJ7_ShTOSpLTKJYj4spO7LBh2j_D7QBhwQSQBllzsB7Nb5MZ9JMuW6n9PK1_oIuRkYUofIOfjYFDA6XwqeUfAqquhZdEKMjLh_SSRAwijtq10wO4E_WhoaqhueMJrGfTACZHN_mCKMQrBF2Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبگان سر قرار همیشگی حاضر شدند
دکتر افشین معاون علمی رئیس جمهور و جمعی از نخبگان کشور که هر سال در دیداری حضوری با رهبر انقلاب، پای صحبت‌ها و رهنمودهای ایشان درباره آینده علمی و پیشرفت ایران می‌نشستند، امسال در مشهد، ضمن زیارت مرقد مطهر امام رضا(ع)  در جوار مزار رهبر شهید گرد هم آمدند تا سنت دیدارهای سالانه را در قالب تجدید بیعت با ایشان برگزار کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/466061" target="_blank">📅 17:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXOuXcDdw77eo8SezzrYZI5ICDD1YWcyYXLaDFdWvfWFu7HCDTSPgkcOwg1v5erflrp1X-qjI1-DeoXTnkdtF0B2xoEPOkiiJQyx0SZIoZgL0401xQmA7Ljbeufmw0_RkPGfka07FdTd_8Be0OiEwEuH5qxo34rxgN_9g_ymWyMa1C00-BhpqmrslJOX7mzSqeoqbmVFee28Wx0gC4V-OyBEka9AicTgGa2ubywDtzCfp-DjUpHqNhXn9V4JDikit_D9MEN9JK-s438Z1aW0aFSSwsn6z7DtT6jdD-5xsqHu78GGaviDSLv9nzBVMoQQ6uxUh8wsIU8yFHwmK2F4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/466060" target="_blank">📅 17:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466059" target="_blank">📅 17:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNLiUpJ9IfsYZXQ--XYuAJ6B66aIgk06gCase3eP6Md4_5ngo3tgtGCpMXZMoJVGkqwpADe5fymgG8wiQTFErK8vkx40krPt2vLQer389mZ26fybHW51QiLin5OnJr4cjCQhlqu4qnWFOcOLoUeQXnfoxNoviHkyQYEFS6rABif4yzA4iroCwlCbaHcN-R5ZK7mu5M_H3RvdPd-Pm2kCWg6Kif25OtqRIO1nMKn7pvQDHu0AJhX7q8D-GWXzH7FlkmoeGLTTeeJw0EJ60g7TkLVWajAIoLox8Lr34hwJG4Zu7pRyhyCwQxUpfov3I15Og6ZfHAu222lJ0t8WCCbC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی معاملات شبانهٔ تتر در صرافی‌های دیجیتال
🔹
طبق اعلام صرافی‌های ارز دیجیتال، از چهارشنبه ۸ مهر تا یکشنبه ۱۲ مهر ۱۴۰۵، بازار تتر-تومان هر روز از ساعت ۹ تا ۲۱ فعالیت خواهد داشت.
🔹
همچنین در این مدت، سقف خرید روزانهٔ تتر برای هر کاربر ۲ هزار تتر تعیین شده…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466058" target="_blank">📅 17:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34379a9399.mp4?token=rrfJ7nRsjwB2M9v4Zobxo-E3Em3Rr2UyjMD3Ao2MocoX8wnrFB3alsYIZZPa6nOCMGq3gCScQxS9a1Fk4QZWOWIcK8ekZ1w5aQUr6cJliTxCYIqinr0kPzva20oRWAoLesTDsJTMz7iOuXA2XYV7UKwGthE6DciO1eSIVr-e3J8t8vDdtvsFiovWb81t4W1bdrabSh4L-UdvETZ4viU4iXQYEJY5PIb3EJkBI0VlNpTNs9B2iGe6Pa25m4QE66Q5XCkTQcYVjoygKqpjddulrIMGxiMo8vXxZiRcC_VdwUp-XlZ5wYK0CfFCTAYpgKHMktHS-EbNhFc_tONA6hb8Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34379a9399.mp4?token=rrfJ7nRsjwB2M9v4Zobxo-E3Em3Rr2UyjMD3Ao2MocoX8wnrFB3alsYIZZPa6nOCMGq3gCScQxS9a1Fk4QZWOWIcK8ekZ1w5aQUr6cJliTxCYIqinr0kPzva20oRWAoLesTDsJTMz7iOuXA2XYV7UKwGthE6DciO1eSIVr-e3J8t8vDdtvsFiovWb81t4W1bdrabSh4L-UdvETZ4viU4iXQYEJY5PIb3EJkBI0VlNpTNs9B2iGe6Pa25m4QE66Q5XCkTQcYVjoygKqpjddulrIMGxiMo8vXxZiRcC_VdwUp-XlZ5wYK0CfFCTAYpgKHMktHS-EbNhFc_tONA6hb8Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقف پروازها در فرودگاه ریاض به‌دلیل انفجار
🔹
همزمان با گزارش‌ها از حملات موشکی و انفجار در عربستان، فعالیت پروازی فرودگاه بین‌المللی ملک خالد ریاض با اختلال مواجه شده و پروازها با تأخیر یا لغو مواجه شده‌اند.
🔹
برخی منابع عربی هم از حملات موشکی یمن به مخازن…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466057" target="_blank">📅 17:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc2-M2HPT9GJbztM5C6DuTf7twMqhhI1V450V9pt8VjQ6njAoPI4tTW_s6x8l6O6_rWkOTifAZW-3PUxDuXjgoUlj7bC8G6cDaCVKDdedfMHCptjQgzNdPQUNZZ8babuLyPicfOxQkVLPXjn3XzFcGyrctie7FIeU-yAZ-_DxzIE1B655yT9Qj9CxFJZnU2_YfRsSxNzaA6DaCCMfNp6TcCBmmXUwS382zdsyhRs3dQR28HL2gZVq60lHBy1uL2Qk9yzcmhHH1Nwu6LSsxd5PzUIT7U4saq-Dh3N8UjnNDoZB-UMIA3TBkcfURsYNsd7Q2qs0Rg2lG3Oo6QIP72NAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466056" target="_blank">📅 16:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXGCpY8aNzMarHYYloMbofqfkLnF65-IrJX9kxMUJLxY75h1kjzik_tenmoeSWOm6SSCaOREM8Wa1esD8gbcKt7gWLUGwPPd_epbGvDm9X5APXrm7_belbIs7RchpygRfpTm4lQtstRYVNPi-4qujhkvCoHROWpkcYkiYTCAOXY1vcwvzMwbmmmWfLkTc5PuHEz2Ra0l0c21nG4aJTIjNnWlb8l_dyy3GpBIwCR5R9RN9co47l9CHExBvnpWGQ_HdbPXlbgNY09Us-SzCsQF5GfrbdGLtUdwk2NtBQREbwCGEJxfn8CTZ0hFnaCLJ9qK9baljtyD4bo6wKqOomVjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
المیادین: عربستان در ۲ ساعت گذشته بیش از ۱۰ حملهٔ هوایی به پایتخت یمن انجام داده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466055" target="_blank">📅 16:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQwfqaqOsyW1DMSoL9ajZRuYZZ0p8Zofp-TdH0bRh1HKIiA5siMxQq8dcCWhwO--N_3WyVYGD4DkztZkuYZGhc2CaRoRE409v1FmOLpnc1owrb4onfSRAEsdjCvi9vPL7-dYma0YdNaxh4FIS7NHCuTWoq7FpoMoiWbmpWRZ8Qtfw61wqBmrq_1yJ-sEQ8L66-5yEhY-tQNCovYAo3-wD6S-Wv7owv-UR9QJAZ8MoTd4-zdpRGMux__vxA1ydugaognvJpHc8ZV8tXz0wlgxw46BiiyXX1rFywiYllogT-aQqH4IvjcHfPSWtLDlYy495Z9DVkyX-jXzmj1B34QZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۳۰ هزار نیروی پاکستانی در عربستان مستقر شدند
🔹
اسلام‌آباد در بحبوحه تنش‌های بین ریاض و صنعا، ۳۰ تا ۴۰ هزار نیروی نظامی خود را به عربستان اعزام کرده تا به این کشور در دفاع از مرزهای زمینی‌اش در مقابل حملات نیروهای مسلح یمن کمک کند.
🔹
یکی از مقامات پاکستانی در گفتگو با رویترز تأکید کرده که قرار نیست این نیروها در عملیات نظامی در خاک یمن شرکت کنند. به گفته این مقام، نیروهای پاکستانی از سال گذشته به تدریج در چندین نوبت به عربستان فرستاده شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466054" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=NFTYB34wjEsBWJPSyu5_W7hdBrUWGgcNM--Z3wo8ZvwlyLPi6erkNALi9Rkf2JusxqM1zyYQHyx5axrpElonNPwxW6M5lOsVrHCuaEGHor2MGwQY3GRW8_cfitdIVN_nK9c-Wcl4ieIDd1e3hqAQ3rk_VsS7lhT2Yoo89L8rKWt1SdQJHikJ47zvqfHSouN0OPceNJWrWcLllVhwqSnMrmezOCmUSjDroJbDppSNq6rgIlfmso6suabHrLPQdlWxFo30PLX5ZaMRO5MbQkLG2bH8wcgCHKmfQGJ2scC4DwWbfayeUQHsUolHPCZJfe7SWkVtNZzQdOtjeMnMETSBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f2ece7cd.mp4?token=NFTYB34wjEsBWJPSyu5_W7hdBrUWGgcNM--Z3wo8ZvwlyLPi6erkNALi9Rkf2JusxqM1zyYQHyx5axrpElonNPwxW6M5lOsVrHCuaEGHor2MGwQY3GRW8_cfitdIVN_nK9c-Wcl4ieIDd1e3hqAQ3rk_VsS7lhT2Yoo89L8rKWt1SdQJHikJ47zvqfHSouN0OPceNJWrWcLllVhwqSnMrmezOCmUSjDroJbDppSNq6rgIlfmso6suabHrLPQdlWxFo30PLX5ZaMRO5MbQkLG2bH8wcgCHKmfQGJ2scC4DwWbfayeUQHsUolHPCZJfe7SWkVtNZzQdOtjeMnMETSBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های مادریگراس اسپانیا رودخانه شد
🔹
بارش شدید و بی‌سابقۀ باران در منطقۀ مادریگراس در ۲۵۰ کیلومتری مادرید، خیابان‌ها را به رودخانه‌های خروشان تبدیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466051" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/179823c671.mp4?token=HkWDAIv75pflCrBKn3JmikM2KqzRVMOFG3RjOk9sj9Z7rtqrUpGCDTBQfITZHXtpKKt0m5vkmVzQn0_xD8hyb852FgnVTV0PwOOOxSWEujBZ0PZ3hpq83h3oDC6NXAXJZigUiXKXciXBPYVyBA8GwWfsFabfHQu5DOWVQB9TbgeC5CRAWu8dkq5IxuR4WQft0gTopBB1ihoQLeQ2mhx4IZAmtgQiCutxMT43QKLKXmH3RbUMUO9x_NLT4OarEq6Q_ehFiEEUuqLR9-2Hmk2lm-9dasimRW6GNdRMGJ9WaIfMCXRR3IxdgfDg3UeaNucSbWJs2QaZAaUbhn5LbN6UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/179823c671.mp4?token=HkWDAIv75pflCrBKn3JmikM2KqzRVMOFG3RjOk9sj9Z7rtqrUpGCDTBQfITZHXtpKKt0m5vkmVzQn0_xD8hyb852FgnVTV0PwOOOxSWEujBZ0PZ3hpq83h3oDC6NXAXJZigUiXKXciXBPYVyBA8GwWfsFabfHQu5DOWVQB9TbgeC5CRAWu8dkq5IxuR4WQft0gTopBB1ihoQLeQ2mhx4IZAmtgQiCutxMT43QKLKXmH3RbUMUO9x_NLT4OarEq6Q_ehFiEEUuqLR9-2Hmk2lm-9dasimRW6GNdRMGJ9WaIfMCXRR3IxdgfDg3UeaNucSbWJs2QaZAaUbhn5LbN6UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمانی آرزویمان این بود که آمریکا به ما موشک ۱۲۰ کیلومتری بدهد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466050" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKc3ioZLavwttrsRD15INKyo0GZtEQ7u6ekkUN2Em1KeIzhRkrMTyk-UhAuQ4sooG1IgWqWEUvpoaeMSizy26sY05U4PSd8Yyhuvt_Vvm6rCRRCdHPkAShKIIbDPyefhUADPE6t5yam9y6b5KtbGikdnZ2wBTpn7waAbXBT0ouA1CcTFwbT4rTkAHQ_CA5Hp396cBYgg7aIv5jt_K-MTv04WqfTdNPvghKbh8-yr0oXMi86o9LUz3F1dZfCMgtr_FJ5THfM0FQyFjOKKK9ThZJUMr2YFMCA_9BGMWpXNBpAan7nt3rqg-bMDHXpQKBcLsqKOHN7QDwB0f_-3Dmt-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طعم تلخ وابستگی را از عراقی‌ها جویا شوید
🔹
گاهی برای فهمیدن معنای استقلال، لازم نیست سراغ کتاب‌های علوم سیاسی برویم؛ کافی است به کشوری نگاه کنیم که برای برقراری یک خط پروازی، دسترسی به درآمد نفتی خود و حتی انتخاب نخست‌وزیرش، ناچار است ملاحظات قدرتی بیرون از مرزهایش را در نظر بگیرد. عراق امروز یکی از روشن‌ترین نمونه‌های این وضعیت است.
🔹
استقلال برای یک کشور، کلمه‌ای تشریفاتی نیست که تنها در قانون اساسی، سرود ملی و پرچم آن خلاصه شود. استقلال یعنی کشوری بتواند درباره سرنوشت خود تصمیم بگیرد؛ یعنی دولت بتواند در چارچوب منافع ملی خود تصمیم بگیرد، حتی اگر تصمیمش با خواست یک قدرت بزرگ همخوان نباشد.
🔹
درغیراین‌صورت، ممکن است کشوری روی کاغذ مستقل باشد، اما در بزنگاه‌های مهم، اختیارش محدود شود؛ آن هم نه الزاماً با حضور سرباز خارجی در خیابان‌های پایتخت، بلکه با ابزارهایی به‌مراتب پیچیده‌تر؛ تحریم، دلار، نظام بانکی، تجارت، فناوری، امنیت و تهدید به قطع حمایت.
🖼
اما تجربۀ عراق چه درسی دربارۀ معنای واقعی استقلال به ما می‌دهد؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466049" target="_blank">📅 16:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQTFKTWyzYT6A_55XER9RQDrh8cNo6qoRZHBa2W4A6hYytUVVYJJIHpkxS_H6e1OB8kVtO9bmXfjQehZJWppqplK4EHoSfbODAJuq5jymuP6Vju7g9UQPQz8vZMWesnHkrJH6A4wV9OwROmMgZPX_EG1uxsXWg17Free-qGECoO0w5RJnjYiwtIxROOZPOysLzrCNK9TFEMaHMQA25CAn0N864I3Dt66-KK0mAtN_4t7v_hj-7oa_8aQ3-JdN6XUzZLp1qhNSrruwnJq-FGW9AP4p5m_Rd882Wj8cckiRSwOx_HEu_dmv_ImWO6Uw3yElLzEQsliUWOhyX8ww0deKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روسیه یک پل مهم کی‌یف را هدف قرار داد
🔹
خبرگزاری فرانسه: برای اولین‌بار «پل جنوبی» که شرق و غرب پایتخت اوکراین را از روی رودخانه به یکدیگر متصل می‌کند، هدف ۲ حمله پهپادی روسیه قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466048" target="_blank">📅 16:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
حملات شدید هوایی عربستان به پایتخت یمن
🔹
منابع عربی از حملات شدید و کم‌سابقهٔ‌ عربستان سعودی به مناطق غیرنظامی در صنعا خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/466047" target="_blank">📅 15:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d42f08273.mp4?token=h8B12ioPj1FjU7m9boezvFdHoMwWWOInuZ5FN8mamxDgU1DI481fanmdO5HHlFzbmghSXkG42u73qENd66R8_MNYD-dnAiscjZCXDXyYhNhsPBhwZ_oqxBEn5M7JurYgKhXYeb0_oOqmfp9OLCHvmgdpKyg7PNHtBgKXo5XlquVM26p1GqUnV3m_jYcjFZKVdAuQFCnv9Mx6q9x69mYkf18vXbqwNlnM8nT1mqn2X1EeYdProY5N1ZyCHHDMJRx-dI9tusJvS_XP0yRnl26SVvZf4P8ST4NjTfbVbt-0qQ_jG6h-x_M_6thRHzmIvkCnfcyN5IcTp43ofBsTHIBlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d42f08273.mp4?token=h8B12ioPj1FjU7m9boezvFdHoMwWWOInuZ5FN8mamxDgU1DI481fanmdO5HHlFzbmghSXkG42u73qENd66R8_MNYD-dnAiscjZCXDXyYhNhsPBhwZ_oqxBEn5M7JurYgKhXYeb0_oOqmfp9OLCHvmgdpKyg7PNHtBgKXo5XlquVM26p1GqUnV3m_jYcjFZKVdAuQFCnv9Mx6q9x69mYkf18vXbqwNlnM8nT1mqn2X1EeYdProY5N1ZyCHHDMJRx-dI9tusJvS_XP0yRnl26SVvZf4P8ST4NjTfbVbt-0qQ_jG6h-x_M_6thRHzmIvkCnfcyN5IcTp43ofBsTHIBlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران با قهرمانی در بازی‌های آسیایی از ژاپن انتقام گرفت
🏐
ایران ۳ - ۱ ژاپن
🇯🇵
۲۶ | ۲۵ | ۲۱ | ۲۴
🇮🇷
۲۸ | ۱۹ | ۲۵ | ۲۶
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466046" target="_blank">📅 15:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
رئیس سازمان سنجش:  فردا نتایج اولیهٔ کنکور در تارنمای سازمان سنجش قرار می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466045" target="_blank">📅 15:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466044">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0485d5cbe3.mp4?token=jPjQ0_MpdYdmw0qcIKhXT5SY-BLByH2_QgSQx2FQ6yRvAcUUfW4XmDbTqRMTSpdAm6Y8Q0B9ciJ6_m1zhTHzIa-qD3kaGAF8bm1Hktbq2LhXw6Elo2qnk4PNxj2m5CoCajg0k1BD0ixBuiJwG3OQ3Icv6fRQsq3PgFrR6kpUQt-3xyL5wu0QYMybnDxZnzE_ZE3LnerDmYG1cGXsNHBZMci2ve-XzWG2EWgFVnKRN2U1x7P8zbzaUz-5xFkfx4TMHo36SZddcX0mkZ8KbwcZKGbhf9buR8w7ypIGv5oLT-ere8ObacstEdV8-OqumYmf09Pmnf6hYPQmIQCVET9qjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0485d5cbe3.mp4?token=jPjQ0_MpdYdmw0qcIKhXT5SY-BLByH2_QgSQx2FQ6yRvAcUUfW4XmDbTqRMTSpdAm6Y8Q0B9ciJ6_m1zhTHzIa-qD3kaGAF8bm1Hktbq2LhXw6Elo2qnk4PNxj2m5CoCajg0k1BD0ixBuiJwG3OQ3Icv6fRQsq3PgFrR6kpUQt-3xyL5wu0QYMybnDxZnzE_ZE3LnerDmYG1cGXsNHBZMci2ve-XzWG2EWgFVnKRN2U1x7P8zbzaUz-5xFkfx4TMHo36SZddcX0mkZ8KbwcZKGbhf9buR8w7ypIGv5oLT-ere8ObacstEdV8-OqumYmf09Pmnf6hYPQmIQCVET9qjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار آذرپیرا با پرچم ایران  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466044" target="_blank">📅 15:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466043">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvfsoXZcJWJQd1RqBQVpKO1X8k7ctEedW3zA_IF21i9f7sCvZWt_m6FmjM2md8LrwWHBfJIRkB6v3rfyFNtw9CpcKF4_bSTtV3j0ebEjYfQkIsbQhsH5OXrLaH0o5Sr2bxKiM3LTHgLZb8sheZRrXBni5FXQx3x9AjB6LJr47dEJwOhfbb_FjqQC7n6WYFNQOS8gdrT7y_sR48aUKTCnUDLrOsQYgiSdz2c6K08jJafHS3RP0aJBBmOYKWKSAqDTLFUc_vAE-rqrlMyqJe8sT2WM4L0rz-qmj_wlbRr-fKLaRkdjKVACyIPOIFE5Hqj8oIYPQjjpD42MY9BDebxA0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کهن‌ترین درخت گردوی ایران ثبت ملی شد
🔹
مدیرکل میراث فرهنگی لرستان: کهن‌ترین درخت گردوی کشور با قدمتی حدود هزار سال در منطقه کهمان شهرستان سلسله لرستان، در فهرست میراث طبیعی ملی ثبت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466043" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REKQGXGwbSjhD5hQdoipXFi5N9Dal2-dqrE5WL2Tu6Yw95K8amW09W2st-6lzimJIjTrpUGQaZraCGqdj1sznZvQZRDRPd3TwClHBU6Iy9VmoC1ui-JhIt1hMzTITLz5dGfZI4-utGzb_A-wsF0y8sS_EZocI2oVEO2SQ7XfeFmfwQ6HVIfHnLcv_JMXmwMECRF3AFsqARfkaMIh9fTJqQAH_MHjEmJlsBh0wX_WgKy_ZkjKW01Q6aE9jqhEuwOQql2R6X7o3XdR_6mgT9mm16nNsz82O5ntuXlwx0n3e8PXCpGtCmO2Eh3A_A1gKrbdRG8HhdWh8MqWZBeEQ_4U4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پدر و مادر رتبه‌های برتر کنکور چه شغل‌هایی دارند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466042" target="_blank">📅 15:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRMtM_hSp4iFzsiXTg85a1y3uNIZCGGpGMRLhElTKAvVewOg9QZ_iY7LXm7iXM44ErukoZRI8tflYXiJXZ7ax57WaDT9OSNgO82w-GJRVGnE_7xbpWDmY6K4pb6NeucutQv0RiUS4iBo8Lc5DulbSKLhD685FcxtF4nnmMdH7kdmOC0OZKyZyGAeWEDTidHrN4oyMLZihUCHWXedEPWem2uZdYg97zXJQssL3CU5tvaTwmHKIJlBB4478ymelOOfeeleuE2xaMxyEFWjCkS_yl-P5LnmF-A9m1oyv3hMHQfDBcy0-Us5a04J7cIpVxzMBYfJO6ARmd3aTREukxUEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZcxM7pDKy0UX2P4uHbtBvRKj6w9XjfcDjK13knSpdETcfOHUK8AtD3Vpe89t16DjPrbq0AZ7YlEWDBhEXM-AF5BPKs1t2AIJCKlJ6-1Unh2GrUxhA6tHZ766sc91-xPPVAM8RYOQih0dVxcLpHv1WdaJwd7vFzgig0hhuEU72_6zwz4yS02NHTeLyPKED19JmiNFA_Nay_-TF2xxlnoJtNPxENR0hRr4sy9kol-mDheIdc_7h27bjjnGPleCHrCq9Y5sJH-OjPk2rOfuKse_8fV8N-AIyk9IXH7VW8padC3jZ86Bp4U0gA4THc2Aic-QsVVXIeBRq8h86MPRQsduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiZkcb__ZHsCDO8uUNT-AW30Z6ryds-ssf8V_GL4zlRDGfGp6Mk0lXtCJ03VieWS3d7uOymJhFRfziEtyG4m1Er9SJZmHxv9hJyANnYsR7jzsWcREeBVp3Hgg-_Cyd1xYfj5QX18NhBBIus6SGbakuuzKEi6OaNPuM_wq91EuSEHzsA2NzByEhkLOJSBudBkRlF17SFZHAByqy4k_WZ700-VQdYiTkOVGCWCJB0bwFUzcFmvkol6aoO1OG5q27GoRnFlhX6ZtW2HriHhTByHofRPpN8A8jKv6UBpN1OyaeTuxwZ1Enbl0SVlh8f9w6QhKoZbSOfiwa78BkRu-tEu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4PeYp_n2HCavGA4G2OrdQyVA2763G5A_gdJ6TwEv4siueTDoYyQMj6jXMH_4upvR3PNj_WWNRoJBMyMbtrtjRLRGHjEtX5ydoFJllVil5KtGnVLxhhKup_p_Ac5EZLO62esclwBLNwql2XZlkzZBsYAV8cRIEnT4b7eUEzuwK20-H13bFPB-JiFHl1D2MYxYJmSSM3o87Z1V0MGILbu1w4LOlQPgWWjg_qtrFRMlJFPxuWWe1Zy46aJk-AexSwZnWCEHYa1TAhCOaiMLWXmUTJbjjntz_hQGHqsAcrs7CMvfFZRVWIGkVnCiqH2QTR4QYFskT9pD-heyMQEoJBOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5SVBO-fmu0DvXv1_0VI6PmNeFiwBBflZaQ6D14stBHpLbNbJEblPvPqVU_ZvBk6vTAYuoj6DXWxX2EsSPHPzCOnkENaUCR8mfz34akdv2ZXt6ia6zIGdnDlHhnpHMA1zYDPt4ibfmwMvKBmBWlwQtGKYsW_DATVp9zKsHUhMOMfiDbyJTqU0DyWHtkdoT-jVbgceztrN82eEOjebSbpq5RI6vJwyRr0Ame-ETpCTEiPlLvcq6bccis4ndRVIq82q4aC_pA5GsDuVdUP_3-dNVOk8id6FoOJRCEsYoA6D-b80VCi0wx_h8QWI9HZlmaLtyApWaugFEZzzUmvKwhraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pA3bLomA_0S0K9fRdotlhJ3q-ammiREbuOUJotytuBSS8RRyhW0NjglD5KT19miOVYiVc77sqySx9NshsSU3RjeZICU9LKw7CW_thC1pLYZkbBPVWW8tjlS3VMM2J72LpHCeoad54zf-UgjtxDhWgm9SttXi6zu5RPiLmW7vCyY5SHhjPSN8l5hR0exXmltuqXWN25aPgt4LYbgmgNeZvQLfmewhATehF7CjU_SYuQajxuX4mNmcrhmIRqroxBotBW8kGpVGzqcBBAEdiPtx8VzsEmFyQQDnZSl4ujgkFNRMM3N6h_JhFID_KFCkLE1F4pwyZ2WGT7ghHlW5venKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8CRxBlvn32TQEJqgl8sXcDIOlxnb3biH6owAZaxzBzhHUI4LxhY5gk8JpF31dqL1ketKQ_owDuY44iM_YDl9zwfJb6JrD6f_RKr3srROLbV1GIwvcgzhkkJn0f6TaL3KxLkLfGLOVkI3aCgpdh-hWJRMeTU89MOAc8J1chEzqDJpKAMqhcIkin6d5D5vuX8_zNaxG-EWlHCcc2EbkhP28OzEaVaB0_7PSCJsW9i8tCT3WahlgPhKgObl7C6Prh33mdCElZDf3bVZm9_qt-5t__G9nZDBiXcbFWmVwmRHzB4knsv36FHtiAyiHqdRIV0Bf5NxGfzZZA8XgS1L9Msww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای حرم مطهر رضوی و رواق دارالذکر؛ مزار نورانی «آقای شهید ایران».
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466035" target="_blank">📅 15:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🥇
اهدای مدال طلای یونس امامی و بالا رفتن پرچم ایران
@Sportfars</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466034" target="_blank">📅 14:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8bfc45069.mp4?token=K30CVEULnVqQRu51zjVZ_HjlAEqcZEh3CNj0Jz3o3pI1F1n8YmY08885h2vaZCP59PmFYPvNa9flFLtHjradj3-euJ3eJqp0d7BYIKH519gyyz-uHP-cMvgYHPXRTgWPOtcWSnDdBY7y7Ubb0V9pcXi-A9tuoZ6iLN2HNK8AWlWnvRag_A3-WSwvipTA5-JFEU4b8zU_2r0DSWNA1ff8RtwSAN5YGXmnDbDoUgCBtGugLywQybCd_fIIE6zRPbTjmEYpnA_uqQxHXdWKWkBZDH_2ta5MZ4WDCGKUO7WTkjOIZ_FUh2F8v4hTWT_NXLcd8LolLXBekigqYhBSG2yq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8bfc45069.mp4?token=K30CVEULnVqQRu51zjVZ_HjlAEqcZEh3CNj0Jz3o3pI1F1n8YmY08885h2vaZCP59PmFYPvNa9flFLtHjradj3-euJ3eJqp0d7BYIKH519gyyz-uHP-cMvgYHPXRTgWPOtcWSnDdBY7y7Ubb0V9pcXi-A9tuoZ6iLN2HNK8AWlWnvRag_A3-WSwvipTA5-JFEU4b8zU_2r0DSWNA1ff8RtwSAN5YGXmnDbDoUgCBtGugLywQybCd_fIIE6zRPbTjmEYpnA_uqQxHXdWKWkBZDH_2ta5MZ4WDCGKUO7WTkjOIZ_FUh2F8v4hTWT_NXLcd8LolLXBekigqYhBSG2yq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌آذرپیرا طلایی شد
🔹
امیرعلی آذرپیرا در فینال مسابقات کشتی بازی‌های آسیایی ۱۰-۰ حریف ازبکستانی‌اش را شکست داد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/466033" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi8YzB2l7wJZFIEDs9NEeSxyLp1qOIOq_brU_pD2nv34V-uEHThoZSwC8_H00UaApfCs7yyePckRqCBB6y-bK2ATS6g_SQb6f4MBtD_flqa0UdpYB_gV7WfYAgkfKwO471Hada2BE3fhQklidNTDSS-5IL5_mUh4QRksUV5pAQQDUbJ_JGVtgnG-zpcf5zIQbxi_i68Px0fjXCxhA5_VtmLnvU0HFEamuFkM5nxhEiwz0bhhQ1Zb-cYasYBYg4NDsAd70pScIMpHdDP9COLoyKOkI1q98ExpQ9RKmCT7gzzWh2FMhF09iXwH1VgCIWJm7r7bShj0yuSTE8zWMz-dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا اصلاح‌طلبان قواعد مذاکره را رعایت نمی‌کنند؟
🔹
مذاکره در سیاست خارجی صرفاً به‌معنای نشستن دو طرف پشت یک میز نیست؛ مذاکره زمانی معنا پیدا می‌کند که هر طرف با اتکا به ظرفیت‌ها و اهرم‌های خود، برای گرفتن امتیاز متقابل وارد میدان شود.
🔹
با این حال، بخشی از…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466032" target="_blank">📅 14:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌ آذرپیرا به فینال رسید
🔹
در نیمه‌نهایی وزن ۹۷ کیلوگرم کشتی آزاد، امیرعلی آذرپیرا ۴ بر ۳ آرش یوشیدای ژاپنی را برد و به فینال رسید.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466031" target="_blank">📅 14:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0fbc8d7a.mp4?token=N3xxE1B_OTBnw7Oh6oagfQHcqssc_jIDlMNZg29OYB2HyPAb7HM_3zxmK0IrsR4C229YGW0TTZ69T6P72AX7kKNKFNb_937hBbpOKjym1kMJMVwkiV_dMbWtAqw7ytxrj52BPQA3wNjYgH2P7Zj1PAh_cDzCZhROy2O3Nsgm5szL7dfbbyjvEudAwhpcpDDiKsaugOwqGRbQjB_aRkBfGYo1qltLjgpsQm_K2TxRfAfIbDq0uynwR3Quv5HFB2GeYaD0tR5LvPM77StZlwnnOIGtHTJVJCSERy82FC8sJt83K6rjUlO9CBbo5UMUqlBcusFkErZr8ZBMR7Ggk0H5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0fbc8d7a.mp4?token=N3xxE1B_OTBnw7Oh6oagfQHcqssc_jIDlMNZg29OYB2HyPAb7HM_3zxmK0IrsR4C229YGW0TTZ69T6P72AX7kKNKFNb_937hBbpOKjym1kMJMVwkiV_dMbWtAqw7ytxrj52BPQA3wNjYgH2P7Zj1PAh_cDzCZhROy2O3Nsgm5szL7dfbbyjvEudAwhpcpDDiKsaugOwqGRbQjB_aRkBfGYo1qltLjgpsQm_K2TxRfAfIbDq0uynwR3Quv5HFB2GeYaD0tR5LvPM77StZlwnnOIGtHTJVJCSERy82FC8sJt83K6rjUlO9CBbo5UMUqlBcusFkErZr8ZBMR7Ggk0H5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دور افتخار آرین سلیمی با پرچم ایران پس‌از کسب طلای بازی‌های آسیایی
🔹
آرین سلیمی در دیدار نهایی تکواندوی بازی‌های آسیایی با برتری مقابل حریف ازبکستانی خود شانزدهمین مدال طلای کاروان ایران را به‌دست آورد. سلیمی در راند اول ۲۶ بر ۴ و در راند دوم ۲۰ بر ۸ به…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466030" target="_blank">📅 14:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCsjAWSRdtqaVtnuL4d7ErQoLGpbOWEycGcnUhY5Wb4QwgJOzHyWBM8Tt3GWl8dzQnzzA42ucZSDmtQp48URsECxpRS0a554F9EtTQRvD3UYH-6ZlOzAezLnApo5bke8OnpxMKRMrGTa_ve__t7doDXcnUPLitn4ccldF7GFZ-quGGjNQlQs9da0ncTuxtqZH_TBksXW_UVb7ViMGoafbKSh5mclmVPKxRZxQarctbcDScjilBzd-jjM8BI_GZ9lwwCUTM4rTbGPJf9MSYo4hirBCKbQCRncstc38O6BD7plsUX3yncjrjqxdY8r4u1sFZ6jp5wQphObflBqvn68eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حملات شدید هوایی عربستان به پایتخت یمن
🔹
منابع عربی از حملات شدید و کم‌سابقهٔ‌ عربستان سعودی به مناطق غیرنظامی در صنعا خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466029" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466022">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5mUc2vKc7Vf9NplBjuYWq30i9M4AvvwPeujy5LhE-5_GJOZiISAQOl1FMmQ_vGcTaA-aMJzMmZNjsgmdNRdqPuNM47l5xUx-yicDuv7PlZt2x5ji_4WjzS8etFBaF5NqNSdUllxEhKLA2bxLYl05P-gXDrQwb53NW8MFYskxfo3r4VMmuUmLjwVfGbsGK_PM6uZtYevE1LOjOIFzcFRIWdKAvQuu7QVRh9vLVOKPAlkFultmI_ReqsqOPDWaYUD8Hvnhm_PafMB-gKqdwB37Sc90SyOmfsRyPeUjBDhyW-czm9zWB3n2DkEmTtk83TJ97EEy1y-_kg4eNJVqR8jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ml-1HIbP8VHtCJZ5Jjp2txe4sDBl4J0Y_gm5BJocFCxfue-EVp9ShCD475Zxfdm7H6CXQHDR6-cvfKMk_nv39IfeHMsjrj7ht9uFqEYckNsoYDbduxFDNBX4dXAQnsE_l0dYVs_oWNa04via0cKQR3bh9XNeYZmREB2z-cGk6uQN9EULmTcGYTsHUGQLg1FhmTooAzQ97gwr2FgRdIMoqoE8qILOMxDuDXikH6qHCRsw2IQi6Q4O-UMoU8vldGDvb5CL7Ko4ufb3-hOQJ31GNzE4A0lFGsfpaJcgsqxKdAShMJDynTOuDcjc3gHIJJ1W3s8MrcbEahZc448R8L-14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlaixRhP3uGBrBgcKymfUhRZMssc1NEoTixrfZzcvdqgBckcOcJAG5Ee5XxnQutNpCrvh1f4WbAt4RPxq4rG3GiN3G0UhnZQGITA-CRzZJjmhNb4fMszWQLlcnx_PFRPgH9VKIt7N8sLMjU7ooP4gDOyQem_znrbtlk6OTJl_YDjT02xi7ce4wOaPonpAj8oUtSnWNpGdiPDwxr2ZuZo3mmMoTUDAft9H9OslVIoIfNrklyzExdI2Zu8m3GoVdAhMKkno0D5b3k1cheuRDwodwGdfp3W7-BCAgOBLkU204M988MNM4A618MWPz-y5okhNjmreipPrI6t6UkxokNsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ZBcdlIy0zx217Ku_Z0C4-ow2oA-mtpSCdUyVGmIvhFgcChtvTbsHmfOXZnbYoFi6z4cYr9eUhB0WwhjaoPn1NO51DBiZdP3ijRlBBdkU3fRgRZx4diq5aAhP7W87ga1ewfhQyVJUuVxzpqGsITKy4WhPOX_wP1rQmN8zuuOrJMlRk6nEuCR83YGzjqe4QXkDJ1GMigPkRZTGYxVO8DDSa6mcucn9JvwiXHsQ9UBCTnbdb1XUxgYf1DgRsWpb6TK70InxAug02Kxm2wu5_uBFSZbFsn6vbSeifG-Paqs3yxIJageEPCk4AvTRIpWeHht1oIUZ17wAXmJ2GHOJkUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btBHvWd9Zb2C3WTlXRuZsM5loWbY6AkywLQhPxu_KSVhg3db8uL-z-StvuGsXeb4u4018U_TfbeVXjDjkIea4fAQuM7rNjlr8F63Z89lBWekOVwNBgtDNOFpuMDBKJ7fyQX3Lf5woCsH26UFMmfLTG2StIk23vaZmQtWdpsWh0hugupxCmp0k1AQnGsnHqPl0l9uEtTPGrHKbvE6QLV_xIXhFSWN4EHsaDEUQPcHqiigFGAsGNL96F6bsliiENzS_NctT3zdo4UUkIyPisjd8dMuEgug8vy1ixVjIFhwQOSUCOYQs0v1YENajqqg8xQ8izf38gAkGuOk_vtISFDhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PezgJfH0DRDDO5_3UNNfmIZAeJRn-CQprzMxNhG1u9xxVX3xZh3HyelTPQIccoysBLDt761Ts2EACxuM51JY_0SfaGaeVs5u8eE6Z_AjwSd9OA8fBXeznJAMzS0Bx6XT6H07BLZuZCIdI0v_wSjQY7dKX8DfGeMPjegdFl6WiUzomRVg4-WvpH9xbeGGcjPk3XVoiONQfj0oBiaXlN1S3ammxPGyBfCtcwNRGbf_qneYAFiX8inZuDjz8e3zaZtkat7oF1A_oeSiCgPojGuXdYfCsKNSIxXD9cpP2aX8kEJezyrvUcFLj5DXX5oyGjU0cpukvM84yifnda2sW0Y4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OpsZLDoOCwuHQWxI8SwHHZX1-kRQroWik9UteFPPrLMRI7FDvocHm9TBUVsBepLSelBUlNx_alJc-5nAueuxv5GCivwd8XJ8n7E6hLq_prYXJ948uIhzFi1u-_XD9C9EORLYhvik__LD1Dc-L9gYPZhZvAYQdEJPtP0-SrIecRTALEluO0Pp7QAE_HimwLFLZ3ey4dGKzpbQIn9GOs3hB7mM2m4H1HnAwq522IR8QZHhOkLVdy_RtGtUFRN21Nkv5x1bemqg9Tlbh-KRkQiHm3HodmECofPAc8vkRvrNuu5VGzjv0UDG3Y346yIBe2Xn7uR41hpjm2BTQhb_voYwMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت گردو از باغ‌های خرم‌آباد
عکاس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466022" target="_blank">📅 14:03 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
