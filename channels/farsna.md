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
<img src="https://cdn4.telesco.pe/file/MMiBcX7SbWP4nLRHFmLrq9qswXnoneZZhpvw8kfiwCd5jiBhwP2m_lyXnuPZeBBA-aYPtMpdcw4JaiiVLdvCO17bdBRZVLDJ1X1eV2h7EruB7aXrHqHc-RHYGaJLjBx7VQKk12W8jLbSW4A1OchjzjK-t9VB8Bwgxf_onNWexUypb4ZStaZR1OgLA69xlOiYG9m8ds8O6e1-9zo3kRMUhQmJurGlNoScaUNts7p0w6TySmf9Mpi5gGlgE0I4drUvBepwK7cQf9IpNIM26SfD6p7WUxQxRj5PNkJGCxwqV0pEBjWlxCJRElNAumsB0JcdvWI5AqXnUGAMd9I7V_NOKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 15:41:26</div>
<hr>

<div class="tg-post" id="msg-450876">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ba45eebb.mp4?token=lgK9yY6MkMmyfFCIUOduBI0GWzHiD32lL7CKhtt57XiJ7OWmXATGL0oavPYawG3Zf_C_LOqwDNFE-_Rh8ZOKfK0qvSJ8OnY66VkWJk5nBnjBRVa9W38YH8NRrsrifhbuIlPUIvoCoXCQpCzqrguss3tTH9LkDV0W_8xw_k26eo8veECclIaOK1g5qbDLbOaZ_zv_7nR6fz5JShwewjpbm8waLj2mmXVbDaVh3QePNgW8YEAWCNpb56ceY1kd0T6gzJ1JwbH1iFotuuPT0bTaF5YwWdbt9fjhrX_e7NQRu84gHQyeJyJgX_uDlkRKjrtwITYM1VOIoFS8C5ckMwDCkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ba45eebb.mp4?token=lgK9yY6MkMmyfFCIUOduBI0GWzHiD32lL7CKhtt57XiJ7OWmXATGL0oavPYawG3Zf_C_LOqwDNFE-_Rh8ZOKfK0qvSJ8OnY66VkWJk5nBnjBRVa9W38YH8NRrsrifhbuIlPUIvoCoXCQpCzqrguss3tTH9LkDV0W_8xw_k26eo8veECclIaOK1g5qbDLbOaZ_zv_7nR6fz5JShwewjpbm8waLj2mmXVbDaVh3QePNgW8YEAWCNpb56ceY1kd0T6gzJ1JwbH1iFotuuPT0bTaF5YwWdbt9fjhrX_e7NQRu84gHQyeJyJgX_uDlkRKjrtwITYM1VOIoFS8C5ckMwDCkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
🔹
معاون حقوقی وزارت خارجه: آمریکا تمام تعهداتش در چهارچوب یادداشت تفاهم اسلام‌آباد را زیر پا گذاشته و متوقف کرده است.
🔹
ما هم تعهدات خود را متوقف کرده‌ایم، در حال اجرای آن‌ها نیستیم و مشغول دفاع از کشوریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/450876" target="_blank">📅 15:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450875">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی قوهٔ‌قضائیه: دادگاه رسیدگی به پروندهٔ شهید امیراحمدی آذر برگزار می‌شود
🔹
پروندهٔ شهید سلمان‌ امیراحمدی که در اغتشاشات سال ۱۴۰۱ به شهادت رسید در دادسرا تکمیل شده و دادگاه در آذرماه برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/450875" target="_blank">📅 15:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450874">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/450874" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450873">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a7eb5536.mp4?token=MKFwUHOjYUDrgmdpBMb14N5mxYEtg3Kp69QEwpdgFvBBT2dmUjlHnag3bU4Lf5zHcTAbkhqEZK3LwRuQ9ZqTxWbsGNFZeXD4MGTLfvThLK_dhP-qfQ0gX5-H5bTro4XxrCdWhpq4Gr7M9iIisieJx_qWSewgwV1C5Xa9SSKgv_S1YUKdILjRMz8PjYMWnVEXViwqNjPPSJPPGfN_riv3FAYPPE0DSQeyGKJ4V8EQYXFgeaZbCuaNkH0kRzAWbYO6bMLGU5f2qF417Q5ZPUjPMX4bjsSFPMD9WsvR_-K3mf0ENeAGDogbo-Hv01cNZNm9D3jfkLjqnDCuCE_wYPs89DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a7eb5536.mp4?token=MKFwUHOjYUDrgmdpBMb14N5mxYEtg3Kp69QEwpdgFvBBT2dmUjlHnag3bU4Lf5zHcTAbkhqEZK3LwRuQ9ZqTxWbsGNFZeXD4MGTLfvThLK_dhP-qfQ0gX5-H5bTro4XxrCdWhpq4Gr7M9iIisieJx_qWSewgwV1C5Xa9SSKgv_S1YUKdILjRMz8PjYMWnVEXViwqNjPPSJPPGfN_riv3FAYPPE0DSQeyGKJ4V8EQYXFgeaZbCuaNkH0kRzAWbYO6bMLGU5f2qF417Q5ZPUjPMX4bjsSFPMD9WsvR_-K3mf0ENeAGDogbo-Hv01cNZNm9D3jfkLjqnDCuCE_wYPs89DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمعاتی که پر از خالی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/450873" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450872">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7c7e6a3e.mp4?token=fDPNv6KUB9HoRR0uDbszN-NdKFwE0LKjJF3upaeFospejXN6TV5Zmh_NPpqvYkJ45Cxh_OwsHwSSaLGNqYkagZdhKaeDRuq0Q6kHxMWL7u0XWoM-Ohi9mahbthXnGSrbgVAWH06Gl8ruSUrNtHBvosPEo_XtaG8qEdyR8z9EOvpaaDiCox4r0lAfiunupDU-G9KbyRJ4diRZjyJXbFu439__5u8lPuYFLAdbC3v2BTObXHKUGcP1wnAqMdrH9Tlt7WBr0l45ZqflNacm7gBg44CzNlpt0MOnRYgA9P9zSX_IQ99BIR0UNHDSH0wfbyfB6HudYucfjiTbPp3rkMrVt7XFoKpdjUrFnsW9qAvJ7h7Ouj64FYkEthgqFcnGDZD5SxBsTPTy-Cy3EpgRDBWraSmjlLb9-HNmwn1P2OTo8o2h29fNub7ee5q04nUD4HRZPSPE6JedTkuSh7WfFqHXgs6fAZY8k4q4MyOJIXhO9aHppVs6OCohkXDbPj-s6w0AZsklfc2hScOiXvBEc1BaeasKxV9X65r_OrHkl2Mij5VwrBUQdlyBFXVJugdI9ydA4ds8_k5znfL4INpQTk26uJe9EBr2fAlPDaMpr7SD1ZdUjuF_pAG66RD6pGqCAsBNdMzaZoiIjpRcskuX5AZ_Xf8U31OrVDsHW4UYE5FVlN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7c7e6a3e.mp4?token=fDPNv6KUB9HoRR0uDbszN-NdKFwE0LKjJF3upaeFospejXN6TV5Zmh_NPpqvYkJ45Cxh_OwsHwSSaLGNqYkagZdhKaeDRuq0Q6kHxMWL7u0XWoM-Ohi9mahbthXnGSrbgVAWH06Gl8ruSUrNtHBvosPEo_XtaG8qEdyR8z9EOvpaaDiCox4r0lAfiunupDU-G9KbyRJ4diRZjyJXbFu439__5u8lPuYFLAdbC3v2BTObXHKUGcP1wnAqMdrH9Tlt7WBr0l45ZqflNacm7gBg44CzNlpt0MOnRYgA9P9zSX_IQ99BIR0UNHDSH0wfbyfB6HudYucfjiTbPp3rkMrVt7XFoKpdjUrFnsW9qAvJ7h7Ouj64FYkEthgqFcnGDZD5SxBsTPTy-Cy3EpgRDBWraSmjlLb9-HNmwn1P2OTo8o2h29fNub7ee5q04nUD4HRZPSPE6JedTkuSh7WfFqHXgs6fAZY8k4q4MyOJIXhO9aHppVs6OCohkXDbPj-s6w0AZsklfc2hScOiXvBEc1BaeasKxV9X65r_OrHkl2Mij5VwrBUQdlyBFXVJugdI9ydA4ds8_k5znfL4INpQTk26uJe9EBr2fAlPDaMpr7SD1ZdUjuF_pAG66RD6pGqCAsBNdMzaZoiIjpRcskuX5AZ_Xf8U31OrVDsHW4UYE5FVlN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن شب، آن بیمارستان
🔹
با اینکه خدمت‌رسانی دوباره در بیمارستان شهید بقایی اهواز پس از تهاجم هواییِ آمریکا به محدودۀ آن از سر گرفته شد؛ اما آنچه در آن شب رقم خورد، از خاطرات مردم خوزستان پاک نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/450872" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450871">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۱۱۶ دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔹
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/450871" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450870">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cckDhqideT2AYneSjyre6Igp5BsXAhlAq8eBWHIDnDt_tKusUCot7ELNUWo5fV4YA--8wvCLjwPSkS5Db-VNy635jKCie-BOc6duUHswffB94QXPAhwitgAyq9IIi72naA0_aH9oSZG6VJDNNmbsStNyf3LmSIkRz-mD-0PN__As7vfNIP7UFSQDuC56lo2KMw_Yi2YD8OC0KR61qf-Co1X85dLXbmRZlHmRdKHmFfqFNev4oUualBQAgnQ8PAvz796E60KjQ-xG0Z6HYGR51Qo-UPTExudGRdZVDxhHrTSU6pys0nYKPNr6BC4mWaC1AA6IDYBSz9oQW5H_oZO8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملات پهپادی به مواضع آمریکا در اردن
🔹
درحالی‌که منابع خبری از شنیده‌شدن صدای چندین انفجار در اردن خبر دادند، ارتش این کشور مدعی رهگیری ۳ پهپاد شده است.
🔹
منابع خبری می‌گویند در این حملات که با چندین پهپاد انجام شده، پایگاه‌های آمریکا هدف قرار گرفته…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/450870" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450869">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238bd6396.mp4?token=OJC3ygIWudXbbf7kbVAUA6AQmN4gSvWAVDMw-AtCdrscY7DEtwxvhiIiF-REmLpE4-ns7V2GPYzu4wnykJXwIyqzrxAJ--QzsoakOr_01Y_xsp4pcXqzX4-jjCTBsmCsPnGciRcYqov-hNlLivO99y5-UNqobFEwSKs5-9Wx9mIL3BI-kCAfhnjZlu0UPaVDp9YQo62_7rsmqQs2zllHp6yJ96AGtz313LpAXJ6mobGfryXnuANOisQW5ESR_eISS_r5GbHWba8-pjgOPCkIfhQITfiK4_H-i2iCsDJIYNIkX3hiUqkDmDCGBjgPfNfBFR1kRXZHm21Gpdk2U5wo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238bd6396.mp4?token=OJC3ygIWudXbbf7kbVAUA6AQmN4gSvWAVDMw-AtCdrscY7DEtwxvhiIiF-REmLpE4-ns7V2GPYzu4wnykJXwIyqzrxAJ--QzsoakOr_01Y_xsp4pcXqzX4-jjCTBsmCsPnGciRcYqov-hNlLivO99y5-UNqobFEwSKs5-9Wx9mIL3BI-kCAfhnjZlu0UPaVDp9YQo62_7rsmqQs2zllHp6yJ96AGtz313LpAXJ6mobGfryXnuANOisQW5ESR_eISS_r5GbHWba8-pjgOPCkIfhQITfiK4_H-i2iCsDJIYNIkX3hiUqkDmDCGBjgPfNfBFR1kRXZHm21Gpdk2U5wo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار هرمزگان: با وجود تهاجم به آب‌شیرین‌کن‌ها در ۲۰ روستای شهرستان جاسک، اختلالی در روند آب‌رسانی به مردم وجود ندارد
🔹
در روزهای آینده آب‌شیرین‌کن‌ها وارد مدار می‌شوند.
🔹
دشمن فکر کرده با زدن چند پل و تونل می‌تواند در روند ارتباطات استراتژیک بندرعباس…</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/450869" target="_blank">📅 15:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450868">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=hQ-GVjjwfRdEDx8zhZ06pZRZBaV00wPwhOqdRREIQIvJ7FYXo_-9-b5msYoCahRNytoB07TXTMahnqJJRskR6dNPxGs2Rpkb71FN5S4q7F0o4wQF7rhA4FqmVooixe2R6U-umW7Fmva-hy3Jx4hpDO6Gga_My2GuLaqinC7twq5R-8VgD33e5gBeBBduRNRaAqg2FDqYxOToB7dOrhRpgbyRu72orZN9QMRQ1iC33B2trbfXO6chBPgea_b-2rVQL64DUOd0zeTKogsqny-fX-5rygst3TJns4yZ4eyfjtn_yJfPF6j6WeCvUcPWAlfeO6S4Egwh4iX2TTOmN1gStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=hQ-GVjjwfRdEDx8zhZ06pZRZBaV00wPwhOqdRREIQIvJ7FYXo_-9-b5msYoCahRNytoB07TXTMahnqJJRskR6dNPxGs2Rpkb71FN5S4q7F0o4wQF7rhA4FqmVooixe2R6U-umW7Fmva-hy3Jx4hpDO6Gga_My2GuLaqinC7twq5R-8VgD33e5gBeBBduRNRaAqg2FDqYxOToB7dOrhRpgbyRu72orZN9QMRQ1iC33B2trbfXO6chBPgea_b-2rVQL64DUOd0zeTKogsqny-fX-5rygst3TJns4yZ4eyfjtn_yJfPF6j6WeCvUcPWAlfeO6S4Egwh4iX2TTOmN1gStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی یکی از تونل‌های آسیب‌دیده محور بندرعباس-سیرجان
🔹
مدیرکل راه و شهرسازی هرمزگان: یکی از دو تونل گلوگاه شهید میرزایی در جادۀ بندرعباس-سیرجان بازگشایی شد.
🔹
تردد خودروها از ساعتی پیش در این تونل آغاز شده و عملیات تخلیۀ ترافیک این مسیر درحال انجام است.…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/450868" target="_blank">📅 14:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450867">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
شرکت نفت کویت: صبح امروز یک مرکز نفتی مهم توسط ایران هدف حمله قرار گرفت و خسارت‌های زیادی به آن وارد شد. @Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/450867" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450866">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d8390497.mp4?token=oFZIZS2kttlzOCwrdGVJxvRT_9PoccSw2ceGQQc3kpHYE1Nu_ItvCAFFNk3QTvUHJxrapeWz6QPpoB3YYacHvjbdXrIh42MC8lBsMp4ykSmsBtWrzAaOF_b6Z1gO8r-Aye3osl24bYCQ8ORRgPH-LJ0CijRNXVSrvmqjEl-99reX_c5Q1L1Vb0Eh-fi4_gHQqkhzax5YtZkl7q3YFfDfVuOicyIHzddI_vIulqZKSrA15TxuwRGvly_SAfvOVTqQ6TXWeQmj9DwtzN1OyyqahfwpbG48GfXznN_w4YfHV2gz-1EKz8LbenNoFou0Un2V5KMqzYt698wSmGHLKMR8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d8390497.mp4?token=oFZIZS2kttlzOCwrdGVJxvRT_9PoccSw2ceGQQc3kpHYE1Nu_ItvCAFFNk3QTvUHJxrapeWz6QPpoB3YYacHvjbdXrIh42MC8lBsMp4ykSmsBtWrzAaOF_b6Z1gO8r-Aye3osl24bYCQ8ORRgPH-LJ0CijRNXVSrvmqjEl-99reX_c5Q1L1Vb0Eh-fi4_gHQqkhzax5YtZkl7q3YFfDfVuOicyIHzddI_vIulqZKSrA15TxuwRGvly_SAfvOVTqQ6TXWeQmj9DwtzN1OyyqahfwpbG48GfXznN_w4YfHV2gz-1EKz8LbenNoFou0Un2V5KMqzYt698wSmGHLKMR8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ شهرسازی هرمزگان: یکی از ۲ تونل گلوگاه شهید میرزایی در جادهٔ بندرعباس-سیرجان بازگشایی شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/450866" target="_blank">📅 14:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450865">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfad249ab3.mp4?token=t85RYeIoWrqsZ5nijah6h0M13eXmp05r2CZVipQeNkkwGPaao1PKrk09toptCCa8hTqx1se8tcx2cIEn7bXp3KV9umKIypKkP-y3UYpFMv6tIyR35_L2ADXlMSWI3u97BieRmUTs_xRZjWzcm3Qww2pZWZ9artV8Sd1ppCbeysSwl1GlG6xyPxktYM_VlpHIKjMEH9ZUrqHEO9XaDmL5uDXMtHk0jQOeda4mwhEkG0b6W3ENVTREIp3MHUGE1iZA4MLjPXVrq78lhkby_Ku5la5hUIYr_oHMr348hnVbyDM9AIx6itejnNusUnKwL1-oDgvj40VjK0MmhzICTrKjqHjEwSGTV16QaS-_tFDK3rfsXu5mtXpjpBQ54s5e_5AgM0lPJcVVYEJ3xhbk3X9QOCUdlGI8fXMa_sa7ZkImwtFpFQJSaTaIB_djthifzIOSttCvqbZ4gWTJ0fcgB0TjUznsJ5oSktPMOlGv8A5WCNmFvxLWMIHtmbcC6KroU3RuDvSNjHpCrniJ4Q3xVwLgOLnJs74ZKDPnnMEL-iquBpI1LfDk3dqmUjRMk9wjyOuUs6WiWoSUKxm7UzQeqRO4TVmeKO1j2CGA_xQU9ljN8iBvp1nfXwYeMwfRo02X48c1YvcZp9oT5HH2qWymTsALo_UdJCMeiHoOJpeP8YdZ_68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfad249ab3.mp4?token=t85RYeIoWrqsZ5nijah6h0M13eXmp05r2CZVipQeNkkwGPaao1PKrk09toptCCa8hTqx1se8tcx2cIEn7bXp3KV9umKIypKkP-y3UYpFMv6tIyR35_L2ADXlMSWI3u97BieRmUTs_xRZjWzcm3Qww2pZWZ9artV8Sd1ppCbeysSwl1GlG6xyPxktYM_VlpHIKjMEH9ZUrqHEO9XaDmL5uDXMtHk0jQOeda4mwhEkG0b6W3ENVTREIp3MHUGE1iZA4MLjPXVrq78lhkby_Ku5la5hUIYr_oHMr348hnVbyDM9AIx6itejnNusUnKwL1-oDgvj40VjK0MmhzICTrKjqHjEwSGTV16QaS-_tFDK3rfsXu5mtXpjpBQ54s5e_5AgM0lPJcVVYEJ3xhbk3X9QOCUdlGI8fXMa_sa7ZkImwtFpFQJSaTaIB_djthifzIOSttCvqbZ4gWTJ0fcgB0TjUznsJ5oSktPMOlGv8A5WCNmFvxLWMIHtmbcC6KroU3RuDvSNjHpCrniJ4Q3xVwLgOLnJs74ZKDPnnMEL-iquBpI1LfDk3dqmUjRMk9wjyOuUs6WiWoSUKxm7UzQeqRO4TVmeKO1j2CGA_xQU9ljN8iBvp1nfXwYeMwfRo02X48c1YvcZp9oT5HH2qWymTsALo_UdJCMeiHoOJpeP8YdZ_68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زندگی در بندرعباس، اهواز و بوشهر جریان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/450865" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450864">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr6vbDn8-jtet7ewqICY9cHwC1QtDNqeT190CUOVD_BaO---YfVpP63_t6-KF87gly9zLnZ73tJners47v4cyb0jmxehUQmWqqFcwJxyNY6gfTIW8C4QmcAJwlLFPrxPKsMhX706OjxNTTWsrOaBcFHizu4ctTzgPkqZM5a9dDA0VegDXmIHFi34iQYEdAm5MvJNA8eT8ZxCldaF85EmYzwMHKafi-JDiSNFkXV-zHVHKeossSXyqdU2aQ4Ta8UPLvRq_T0lpgaWYahNe2U4wztqR-AuRaww9seWVCCna70Hmfi1NaH7U7vRDk-1nL-GQv0zPak_bOOSm99kz1dPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سانسور کامل تصاویر ماهواره‌ای در غرب آسیا
🔹
درحالی‌که آمریکا مدعی دستاوردهای بزرگ در جنگ با ایران است اما دولت ایالات متحده از تمامی شرکت‌های ارائه‌دهندۀ تصاویر ماهواره‌ای تجاری درخواست کرده است که به‌طور نامحدود انتشار تصاویر مربوط به منطقۀ درگیری در خاورمیانه…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/450864" target="_blank">📅 14:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450863">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قوه‌قضائیه: رأی نهایی پرونده کرسنت هنوز صادر نشده است
🔹
مرکز رسانۀ قوه‌قضائیه: رأی نهایی پرونده کرسنت هنوز صادر نشده و پرونده همچنان در مرحلۀ رسیدگی در دادگاه تجدیدنظر قرار دارد.
🔹
در رأی بدوی این پرونده، تعدادی از متهمان محکوم شده‌اند، اما پس از اعتراض آن‌ها، پرونده به دادگاه تجدیدنظر ارجاع شده است.
🔹
تاکنون دادگاه تجدیدنظر رأی خود را صادر نکرده و بررسی پرونده همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/450863" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450862">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انهدام ۲ باند سارقان مسلح در درگیری با پلیس چابهار
🔹
فرمانده انتظامی سیستان‌و‌بلوچستان: در جریان انهدام ۲ باند سارقان مسلح در چابهار، پس‌از درگیری مسلحانه ۳ نفر از سارقان مجروح و ۷ نفر دیگر دستگیر شدند؛ ۳ کلت کمری، مقادیری مهمات و ۲ خودروی سرقتی از متهمان ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/450862" target="_blank">📅 14:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450861">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=J-tWf1z4T2cWbmuAWY5Yd-pUMtrcZ-VAYU1GyvbnbM7Ukr5QKS8GQsnCurx1Yl1WgNlH--gCGG3GReQXG8w2e8JVklW2YmRQYh0C_Bqv9cFtGUvu37SinHBen96Qjl_fRGZLVV8uBYlC89yRraF1cKIlVkFpdouP2IwmNtA3-8kI1V1jHRHIX4a1RkDLdgmBwzxLYUV-DtYKEZd-Y21FUt4plwOTXouojPeVBgUr0IOHnt2xGiTpr8cI8NDxguqF0w1j_CGjiupM_Q9jOO_VYFcuoXsxqsJlIh-arZEH4FUDGPR68UFBmJvysESJsHcO9E3UaxfEGs41Lw8IzdBmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=J-tWf1z4T2cWbmuAWY5Yd-pUMtrcZ-VAYU1GyvbnbM7Ukr5QKS8GQsnCurx1Yl1WgNlH--gCGG3GReQXG8w2e8JVklW2YmRQYh0C_Bqv9cFtGUvu37SinHBen96Qjl_fRGZLVV8uBYlC89yRraF1cKIlVkFpdouP2IwmNtA3-8kI1V1jHRHIX4a1RkDLdgmBwzxLYUV-DtYKEZd-Y21FUt4plwOTXouojPeVBgUr0IOHnt2xGiTpr8cI8NDxguqF0w1j_CGjiupM_Q9jOO_VYFcuoXsxqsJlIh-arZEH4FUDGPR68UFBmJvysESJsHcO9E3UaxfEGs41Lw8IzdBmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
حمله کوبنده و همزمان موشکی و پهپادی به شیلترهای جنگنده‌ها و یک رمپ بزرگ توقف در پایگاه آمریکا در الازرق اردن
🔹
روابط‌عمومی سپاه: مردم شریف و ارتشیان غیرتمند اردن؛ همانگونه که ۱۴۰ شبانه‌روز حضور میدانی مردم ایران در خیابان‌ها در حمایت از انقلاب اسلامی دنیا…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/450861" target="_blank">📅 14:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450860">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1w7hh-C0ZpVHrrmAB7eyBbMJxUA2i7-CokaGSPk_O_IJOHp3xobWz3_4qJoIBj_CF3mXKeu2kgEacbNYG1EE26BZv7vMAYi6-tbOFwJDsYC2oy78vOSB2nCI2z2QWdeZ2w2OL-MNZzJkoL54LV8sN80TCFE7gUCNtr6FI4ktXrbRuuhmrw3ZKTc6NGieeJiTXcbZc5Ss4lbR_etC9aOnrA5a39F9jKANLQcYddoVZZOp1ps-3z64y_BtkRHIOL6DADFNr84CWzMKo8St3F5tDyPJByP1Pd3Xj6gV9xedL18h78Ogt91rfMonf_4Rox9NJSRCEiDZZp3yGQXYTFXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انسجام میان سران قوا بی‌سابقه است
🔹
در طول تاریخ انقلاب، چنین انسجامی میان قوای مجریه، قضائیه و مقننه برای پیگیری یک حقوق ملت ایران بی‌سابقه است.
🔹
آقایان اژه‌ای و قالیباف با تمام توان، ما را در این مسیر همراهی می‌کنند و این همراهی شایسته، گاهی حتی با نقدهای غیرمنصفانه نیز مواجه می‌شود که جای تقدیر و حمایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/450860" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
گلوگاه شهید میرزایی بندرعباس که دیشب مورد حملهٔ ارتش تروریستی آمریکا قرار گرفت، درحال بازگشایی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/450859" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450858">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=qIINTEdVQj5dpp0m-zGDw0wxY5sQNXRb9bAST5jOSnm3vkX6sB7EE-LvuHc8CUk4I71c4t4Yoj_Ecjywu8pGxYn442YxpPr3shpq4-HwhAjWKi8JvrStFBjEll1yVLvQo1eAbEil5IGKTeKFAlSb_gjjGr6Rg009ucZ4LijKFHGicLggWcs0ZacisjB9-XcOLy3QWolQ-gZZgkj4eAjg_VDsHTWxDTjjSE_6g0IkAUVc5QVmKM1Ty-TWLseUpFPxOrFhRBCYKGuf6XL4Oj77PGq16wOcNjH4lOQYhLSz9Gmywue1Bogf_4IYDfVu4u7zFUr8tNueY1EAtvuHfi7f5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=qIINTEdVQj5dpp0m-zGDw0wxY5sQNXRb9bAST5jOSnm3vkX6sB7EE-LvuHc8CUk4I71c4t4Yoj_Ecjywu8pGxYn442YxpPr3shpq4-HwhAjWKi8JvrStFBjEll1yVLvQo1eAbEil5IGKTeKFAlSb_gjjGr6Rg009ucZ4LijKFHGicLggWcs0ZacisjB9-XcOLy3QWolQ-gZZgkj4eAjg_VDsHTWxDTjjSE_6g0IkAUVc5QVmKM1Ty-TWLseUpFPxOrFhRBCYKGuf6XL4Oj77PGq16wOcNjH4lOQYhLSz9Gmywue1Bogf_4IYDfVu4u7zFUr8tNueY1EAtvuHfi7f5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهارمین سوگواری آیینی محرم شهر با حضور و اجرای بیش از ۵۰ گروه هنری از امشب ۲۷ تیر تا ۱۲ مرداد از ساعت ۱۹ تا ۲۳ در میدان آزادی برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/450858" target="_blank">📅 13:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450857">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=WWaRIuY2KFXwzBcoZl8vgjisHnt_DD1UjY98fsOlM0dP8eW2ySEZdiowNC5Mr1sT4CzZXROOz7GQ5Cr8AlQWh43AhlpGfE27MfLg151IbMsAHQ4xoGWcvsLOxte13irmnomvq0pT0uuAKtpd-crExz2KLuB5jcPxHWqKpGF4LxoB7W8o09DJ4mXVY5TqoeSc0XxU-_mJ5Wzgbpg86vWlEXqGYq6ijGi9GwyVLDUijAeGgQS4S3_wITxsvJ4QzIXPrmWKBwMoQZ-ufhAykEHDjD1ZJ9VqGAtRE2OFUWNzq4PzgJHhQrmFSeovTeKDnUtF6PVeY3qeBKD2aT-1F07Tdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=WWaRIuY2KFXwzBcoZl8vgjisHnt_DD1UjY98fsOlM0dP8eW2ySEZdiowNC5Mr1sT4CzZXROOz7GQ5Cr8AlQWh43AhlpGfE27MfLg151IbMsAHQ4xoGWcvsLOxte13irmnomvq0pT0uuAKtpd-crExz2KLuB5jcPxHWqKpGF4LxoB7W8o09DJ4mXVY5TqoeSc0XxU-_mJ5Wzgbpg86vWlEXqGYq6ijGi9GwyVLDUijAeGgQS4S3_wITxsvJ4QzIXPrmWKBwMoQZ-ufhAykEHDjD1ZJ9VqGAtRE2OFUWNzq4PzgJHhQrmFSeovTeKDnUtF6PVeY3qeBKD2aT-1F07Tdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/450857" target="_blank">📅 13:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450856">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/450856" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYj3pkaRr2NFNnKqqzTYn9PaWu3ioz4rhpD9mG9Hl-0C-nNzT-6inp-ER_7K-5BdVvtswMs2FqU9CfBzalEh40KPTXnjGlOYSV76ijB7RmYocCzb5Kkdvbi35WPtalOIAQ6vYL1Mr9fxrIV11Sm1U78ClvTYn2eafMsYfIA98NojEcFcnE4umFj30pYwW1o8SedAklBJEx6kplscYRvzDrF4vQ_EC1g69tn7k1kdQvkCqTO8WPcldgY567a1TRfdo6aLSrR0lO5FGJiw9qxqvsn2ZkYtDyP4f-osY9uiqr7lpogvbZ_Mi_v-RL75uugkZEI88CMpxzID5bfg76v2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان جام جهانی قربانی قوانین ضدایرانی آمریکا
🔹
خوان کاپدویلا، مدافع چپ سابق تیم ملی اسپانیا و یکی از اعضای نسل طلایی این کشور، در آستانه فینال جام جهانی ۲۰۲۶ با مشکلی غیرمنتظره روبه‌رو شده. مشکلی که ریشه آن به سفری ۱۰ سال قبل به ایران بازمی‌گردد.
🔹
قهرمان جام جهانی ۲۰۱۰ که قصد داشت همراه خانواده‌اش برای تماشای دیدار فینال میان اسپانیا و آرژانتین راهی آمریکا شود، اعلام کرد مجوز سفر الکترونیکی (ESTA) او از سوی مقامات آمریکایی رد شده است.
🔹
این ستاره سابق فوتبال اسپانیا در گفت‌وگو با رسانه‌های کشورش توضیح داد که علت رد شدن درخواستش، سفر او به ایران در سال ۲۰۱۶ برای حضور در تیم ستارگان لالیگا مقابل ستارگان فوتبال ایران بوده است.
🔹
ماجرای کاپدویلا در حالی خبرساز شده که در هفته‌های اخیر موضوع محدودیت‌های ورود به آمریکا بار دیگر در حاشیه جام جهانی مطرح شده است؛ از مشکلات صدور ویزا برای برخی اعضای تیم‌های ملی گرفته تا انتقادهایی که نسبت به سخت‌گیری‌های مهاجرتی مطرح شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/450855" target="_blank">📅 13:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
کویت مدعی شد در جریان حملات موشکی به این کشور، یک نیروگاه و تأسیسات آب شیرین‌کن به‌شدت آسیب دیده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/450854" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450853">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اختلال در آب‌رسانی ۲۰ روستای جاسک به‌دلیل حملات آمریکا
🔹
آبفای هرمزگان: درپی حملهٔ دیشب ارتش تروریستی آمریکا به آب‌شیرین‌کن بونجی، تامین آب آشامیدنی ۲۰ روستای جاسک با جمعیتی حدود ۱۰ هزار نفر با اختلال کامل مواجه شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450853" target="_blank">📅 13:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450852">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای انفجار در کویت و اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/450852" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450851">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای انفجار در کویت و اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450851" target="_blank">📅 13:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450850">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امتحانات دانشگاه‌‌های ۳ استان جنوبی مجازی شد
🔹
وزارت علوم: امتحانات دانشگاه‌های ۳ استان هرمزگان، بوشهر و نوار جنوبی سیستان‌وبلوچستان به‌صورت مجازی برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/450850" target="_blank">📅 13:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450849">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شهادت یک مامور انتظامی کهگیلویه‌وبویراحمد در درگیری با افراد مسلح
🔹
معاون اجتماعی فرماندهی انتظامی کهگیلویه‌وبویراحمد: درپی درگیری ماموران پاسگاه دمچنار با دارندگان سلاح غیرمجاز در منطقهٔ عشایری زنگوا، ستوان‌یکم رحمت‌اله سجادی‌مهر به‌شهادت رسید.
🔹
در این راستا ۲ نفر دستگیر شدند و عملیات برای شناسایی سایر عوامل این حادثه همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450849" target="_blank">📅 13:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450848">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت
🔹
سپاه تهران: به‌دلیل انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت، احتمال شنیدن صدای انفجار ناشی از این عملیات تا ساعت ۱۵ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450848" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450847">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkvBlWNggjYBYm4LDKFK89FEPS6liOwxjoQUSOqccHxdxH0PZIVcl9iRajihYVAqOsb8ppuUtroRun53m5AuzorIYi1ME6BtWSN8NVFC5OFins-3-onQ4e7JY94pOHtvvgg7u4o9s45q16_BWpkbCRgqVNNg4z3PM_qU0-V3ElkAo27In6c6-r5HEG69cKMmQC2coPTlGFoIFLlvxazkNK1PSW5cVvT0VRhojOd90dinRVkNNAyxfAC1IVQ3SH8YjZxuTWRbna09OnvgPYEMpoFugP1Xd4KGoo6PcNWxNtmap-gwju0JF4r_XDk3-qYhBikoq6Sf6T55F407JcgWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با ریزش ۱۱۷ هزار واحدی به ۴ میلیون و ۷۷۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450847" target="_blank">📅 12:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450846">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2OvBxEx2f9NEBN3sJ3ZS7kRDexjkHWhtUPzQQmwPx3JVNmQ0PYyroPBD2SuXhgz6eXDsI3VDE3lakipGqQeASgrenNMxP8-CgJm2MlJAKjguOAi-YzkJ8twODblx6ddo_Ijbj-_3DjJCXYAUVmHGq9MwgMCReJ5f-viBqeskoSCid3sAQj17_oQ-G6utfpn91NnXVH1OCmBDs5rEB6ywcZ0-eWPdqRRsJ4KFSnbH4T1E4FyTXzKeUYmFM-yMkBf6kiNKl7pq90YMTm1bWSXUrdPyJ7SkAQrEGtadDQQc8-0pvkbyR9Ky7eoZIohqCUG7l9PcCJJ5yvehlXSrXxpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدوس برای پرسپولیسی شدن رقم بالایی می‌خواهد
⚽️
پرسپولیس برای تقویت ترکیب تیم، جذب سامان قدوس را دنبال می‌کند. مدیران باشگاه نیز مذاکرات اولیه را برای بررسی شرایط این انتقال انجام داده‌اند.
⚽️
یکی از موانع اصلی برای انتقال، رقم بالای مطالبات مالی سامان است. گفته می‌شود دستمزد درخواستی قدوس نسبتاً بالاست و همین موضوع می‌تواند ادامۀ مذاکرات را با چالش جدی روبه‌رو کرده و حتی باعث شود مدیران پرسپولیس از جذب این ملی‌پوش صرف‌نظر کنند.
⚽️
هنوز تصمیم نهایی گرفته نشده و سرنوشت انتقال به روند مذاکرات روزهای آینده و احتمال نزدیک شدن دیدگاه‌های مالی دو طرف بستگی خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450846" target="_blank">📅 12:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450845">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8LkYiNzL-eDqLaKWC7mLS1M-SZb3NlWssy-eFv0rMkFDqYzjERVaRBzqU8Gim2ssE7d2yKVRwBz42_e8Tx_WQEBBK3VyU6G0RgowsTD-4oRHSBXg2ie4vZoU-ylccor6GbCjsQdc0L0ztOULHTlbQZhpnm4oQ6GdcalH-PYtTYLxLcmQHbMxPXdJGuUppNOSvUXrPjfZtPuLt6wa2eeFfBOl9rkTJn17_jPpkxB60Na2DrwsqJxYDjVdfmIdN3sOUHuj2FW_Rs_Zy80xFmy5a19MmNkzldSjxvzZGLgH4yVu3cZDgAMLVvNpyy5pqOBwKNuhI0uzZi_GwuKMAleOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال تمامی بانک‌ها برطرف شد
🔹
داده‌های اتاق مانیتورینگ شبکۀ بانکی نشان می‌دهد تمامی بانک‌ها از جمله ملی، صادرات و تجارت به چرخۀ خدمات‌دهی بازگشته‌اند و وضعیت ارائۀ خدمات بانکی از صبح امروز پایدار بوده است.
🔹
طبق داده‌ها در نمودار مربوط به بانک ملی به‌صورت…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450845" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450844">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL76porOXQpjhquHhbCbjTqJeofI9T4MjsO8T5sWri75tyxaQB9V0CING2dXXx8qL2bZi6Booem4PFThj4fNNawSNFXeIbkRyzvw16F7SwEnj54yeF7dA3VnouheaISzJclc3WpHXXTofcobjVfA1Ct25hG4UWCJHVEtxBM7Woma-E6c82b--6C-GOLAVFEXwHWQYDhWNeCwRP32yzXqea_ZxCN3b8MuuFBnJ_j9-jrsK2B4ywcwiCT1c6IvoGMUHh-tm74wFglh9fRpqSnEgtkiYtB4gmnA-8ol1kuWM0830sN8xS5h8URL4kXpA27nBaNEK-gan0CvJ-lAUqVRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قوه‌قضائیه: بیش از ۲۴۰۰ گزارش تخلف اقتصادی در شرایط جنگی ثبت شده
🔹
براساس گزارش دادستانی کل کشور تاکنون ۲۴۱۶ گزارش تخلفات اقتصادی ثبت شده که از این تعداد، ۴۴۷ پرونده برای رسیدگی به دادسراها ارجاع شده و ۱۹۲۳ پرونده هم به سازمان تعزیرات حکومتی ارسال شده است.
🔹
پرونده‌های ارجاع‌شده در دادسراها و سازمان تعزیرات حکومتی در حال رسیدگی است و پس‌از مشخص‌شدن نتایج و میزان محکومیت‌ها، جزئیات آن در نشست‌های آینده به‌اطلاع مردم خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450844" target="_blank">📅 12:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450843">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f470048b5.mp4?token=ic3rkNatD-cT4K83IwZYoqzXrI5hCEfCBZWP5BIU5lv557SlixMCeYZ0Sri0ZzotzT7WNgptYXq0aEbyh6vFGUqkvywwdV7uAty7uN6DXR9UhaNlWrH-uJChuhQvC5IcGF30VewAMbMro7F8K7JNV6mvENbaRkb7_9WFhh600OUxphqn4iizLXg0XXhGt-LiVGM01QiTsWIRJckehXyd7k_3D0zF2ntsmgaatAsxvdq2WyvuhRl0u4SC-BY5aplqfyc89b5mb0SnjZ14zcknFi1PHHhshUFcSRk3o0oGIcM362no3gyndmlfLSxDiIh8m6Dn8LLeBkxZTHJSTboHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f470048b5.mp4?token=ic3rkNatD-cT4K83IwZYoqzXrI5hCEfCBZWP5BIU5lv557SlixMCeYZ0Sri0ZzotzT7WNgptYXq0aEbyh6vFGUqkvywwdV7uAty7uN6DXR9UhaNlWrH-uJChuhQvC5IcGF30VewAMbMro7F8K7JNV6mvENbaRkb7_9WFhh600OUxphqn4iizLXg0XXhGt-LiVGM01QiTsWIRJckehXyd7k_3D0zF2ntsmgaatAsxvdq2WyvuhRl0u4SC-BY5aplqfyc89b5mb0SnjZ14zcknFi1PHHhshUFcSRk3o0oGIcM362no3gyndmlfLSxDiIh8m6Dn8LLeBkxZTHJSTboHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عبدی و روزنامه اعتماد مجرم شناخته شدند
🔹
سخنگوی دادگاه مطبوعات: هیئت منصفه دادگاه‌های سیاسی و مطبوعاتی با اکثریت آرا عباس عبدی و روزنامه اعتماد را مجرم شناخت و آنان را مستحق تخفیف در مجازات ندانست.
🔸
پیش‌ازاین، دادستانی تهران با استناد به محتوای یادداشت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450843" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450842">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصادرهٔ ۳ همت از اموال قاچاقچیان مواد مخدر در گلستان
🔹
دادستان گلستان: حکم مصادرهٔ ۶۳ ملک متعلق به قاچاقچیان مواد مخدر به‌ارزش بیش‌از ۳ همت صادر شد.
🔹
همچنین اموال دیگری از جمله خودرو، طلا، واحدهای مسکونی و تجاری و حدود ۷۰ هکتار زمین کشاورزی نیز در پرونده‌های مرتبط شناسایی شده‌ و در مراحل رسیدگی قضایی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450842" target="_blank">📅 12:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450835">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbp51FVG7wASvqfRVc4mcxLNa5AycxdE3YYo8rLSEt7Me4ZEDUNAPoVGHKVDWpsRcg9PX09eRru38xiSOnE8upEdZwXrnsToDaebebh9HSz3VusbSSN1gxeT0VAejPw8NebbicNrAJdTVWTWdqMmbZCSDh8isXkhICJa4GcxaVR81haJOVWeHx3D8E7Yv9ErxsANid4HsWuj2P3asHHzEWpcKg1zZvUQoOtNiwQY02e2vh9cacdxSSLu1-gKnFIakeIna6VxpYJmtFfWaJlaKgfUZPBfDkd5MC7QsdRzi_tZALLP4tqHQjB6zaurixNnNvTtlmsinRO6pPR48e1pAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnIv_jf7s1ULsRwHC-TOHqP7OiyJSvBWawn29jUW_tPDBsj4mjvqTJcKR_MNVe5wwF6o8CuBTvEAVHEIrhlmOQbJz6dxGGVdS7L_d8nJ6PAct00Qjt8ysAVOZMaI5aXnx3uGvQjHhiYuNTRnkCa6KgBvOEimRu96AMle0eJztBUCDqXTOzMMVzkrJvVCEHVinR2uq6o8nW3jZWq5eBFLsU0Pg2a2EgWQCjQMWgCGKgXQeSYJldisFECGalRgMcbOYoxKPCgTA9-zpQfOEy_5EHagZ86mYSbqhN3eX4hNzFPfMW_CbCdlPfRpZ-pFQo30A2puAt9RI4hRRJ7SK3dUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQdBfwvZxuTCXr-hiyLLBVN_k6gvWw6KdhHZPRSYNIRuOc9EtzIasIsnhvNcbIdJeYtHThRFMzzJG0RSVmgc7kgGPDnyh-ecUnEjJckRByG24WBraYgz0VQ0WNez4N54gHkhBpXJOiSuEso7mxGwgo7XwwM5knH1cfAeB3wqofusMd0EMqZK0uSryxRhUqUiqEBdhMZknQTJGCqohJPdP8JP8xpWXJ98o4pttE9qV_LiU5tZbUG4WJFmaoED5ZgDb02SeRsTsuH80TsRVmtnIT_4b8Us6y8lH3VM9MojOR757aYdqCQIEIYjuBBfbostsgdOQdhthvUWzE365OSlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klyEpylQLvNR0O9H_YgIEmxhwV5l4Q190QFiAROk6OZ4RgDudWCD_atlC1Ys3BKjpdeHFiiPGHd2iNx4MJBmCLXNqbZz76xtjgdGqyxVQYXCaK3etGnZGSAWw4dm1UAMb9KvS2sA53bsdIPO8BNjFDlHD4WIBlCBU1whTqeVljKKym8ZGGX0l8c-jHhgAHKfFZVe3eQOf9hvErOAEoSKpwg_wY-vp6EE9o-hFi70_nKtoadxeE6ljvDqcmCuiskNilc18f895cUCP4rTGVsXr93LA5nv6mmq-TJ0jkxIhjHRpkuPdTeOy-V36OPpUX4MUFaR7XifoN9lELzsSOiCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BF9hma0qGBGj33BMpRmT44DzeMhHJcasZHW9_zooPie3kA85Xd2clrZR-AVhZw9WxXKu6ZIWKSMvTq4CmbCmBrzS5o6px3Nkmgx5eq3Iiu_kKSpQOfUO3Ohe8hfUNHefULRUqLYlsB0RAZwk4hdXSV9OrZT4AQN1eaivo3ws-66qeNFv_i1B2IHOE9X3fsm3BZiZzGmgkLyEazqE9_IkT8NHztj2pm3AHKpxw-CFuY1Yjh3rcMh-G-WXxudElhCwq3k8sfzV_W-xGbbxsf7TG_m0g3VjmvYlcGf_h7RDXUSpcpVVhvFYYHtP_FY2b6YJ9xnIZNdcq3ouqRyKfPyPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW8isozASiDz-rKyRvEZdKqj2EZtdLwbHSHUr1iarRML_eMJV5afQVG-OpQcQF6GFs99MOv2qLc445z3zFB59bFaKNne7NrAerUfHeoS0idClPXbtcHZDKRBeDxJhP5gBZk1T9z8Mla6VCxCDTKaM33K3etGc0QekugzyUg5Sdsy6TJbZlCVLhnh3ESD0ElAu17LF9keuYjSgMU_55DG3vfg8c-1CbkiH9vXy6eacZarB9nWNtcXNZxaL8M4QadF19VpRZQZ3Xg0axdRa3y5OdUHwbJCqaICWiVQ72aD4Y_mvLHeludrBhWy_HQM1k5AJHbeeZeCfd4rtls7RIUbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ni71K4TpfII45QJCSjuwmPIBdb9LbxdjFRB954c5opB1TDDq1E0Sz-E7wbDajYdpmF5y7Nws0TBcGkwxo3UUF_jqVb25xLv5WHHBDw__L5SgE9y0UyXgXDQuw4r8UOEThdknDIdoUK7Vxo41LtD2O3wKBSMojknhLkcpBUYPc0xCXPJcYX4Udloh_BhkalOHj_UwzDcV0R4DFyJgNRtxZ3pP30nbm5EUj8fXUfRK-1_pLnHrO6J7Qhv5A6q-tA0-DSTwf5dhL8mGq_ofKsD9BqHqaV_wQ3Yj2b8e9dGkctfKVVF1dsxfFfLDudvitU3WWGstCxB56d5whiz_JgQ2Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنگهٔ هرمز؛ میراث ایرانیان
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450835" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450834">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به انشعاب راه‌آهن بندرعباس
🔹
استانداری هرمزگان: حوالی ساعت ۲۴ ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی مورد هدف قرار گرفته است که متأسفانه در این حادثه ۲ نفر از هموطنانمان مصدوم و به مراکز درمانی اعزام شده‌اند.
🔹
این ایستگاه…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450834" target="_blank">📅 12:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450833">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2574dccf.mp4?token=NasgGxlvHMlXo0cEjM6aPfAuOZcSzb0DSYVFDI12hip-pmmnXJxh9VLPqQUhh8EHzXilY0NqesdYgYRBnd4YMoQVh1D-hYkKI2lumpq3f81o0l0MqH0OBlDrcNRiEIWsEAgCiD1PpJyRVLOgIxNW8TlfcIH6Y--S0n_BCVZguQLjHCFyFevxtrh2Etoczzf2rvF9YV2JTwO2d9wNnkDGyLmByxnxMXXHKq_Eu0ZUd6VKjhzkVYGXLlqpJTdUBX_0K7OPVTXsU0yjPbdeLr-tK1ABwI8098VNL_SLhnjQIwZ8dYXWcaDQvwgBDaab1XZ7BIYf3M0NO3ZH-dUd_D5qGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2574dccf.mp4?token=NasgGxlvHMlXo0cEjM6aPfAuOZcSzb0DSYVFDI12hip-pmmnXJxh9VLPqQUhh8EHzXilY0NqesdYgYRBnd4YMoQVh1D-hYkKI2lumpq3f81o0l0MqH0OBlDrcNRiEIWsEAgCiD1PpJyRVLOgIxNW8TlfcIH6Y--S0n_BCVZguQLjHCFyFevxtrh2Etoczzf2rvF9YV2JTwO2d9wNnkDGyLmByxnxMXXHKq_Eu0ZUd6VKjhzkVYGXLlqpJTdUBX_0K7OPVTXsU0yjPbdeLr-tK1ABwI8098VNL_SLhnjQIwZ8dYXWcaDQvwgBDaab1XZ7BIYf3M0NO3ZH-dUd_D5qGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای مزدورانی که با دشمن همکاری کردند و خواستار حمله به ایران شدند، پرونده تشکیل داده‌ایم
🔹
این عوامل شبکه‌های ترور راه‌اندازی کردند و به‌دنبال بمب‌گذاری بودند؛ اتهام آن‌ها در جنگ‌های ۱۲ روزه و رمضان، «همکاری با دولت‌های متخاصم»، «اقدام…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/450833" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450832">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0SI0U2J-IQdwzKesJyQCdZfIoauCaPhK53VpbUU8SKRyClWccieejoUCsM_MEHLK7oTpkhefTSZVf2eR4-lB-jWfyjD1LtjCKoh8j_M16djZP2s08j8oh9ltn3QoOsJw6VMpmQ05jRza8L5skbgMNakR-7sYa0wv5P0vtiNyU9Wmnudb2PTwGMjxWOk7OHnSsM3oPMq5K_qagrNp7r0xy5PmEk3473mbFgcnCxwEbBg4iyZhQg187OLe9CYDanvysyBGv23JHZR9Kkah6tJu6J5Mjb2i5vvQ4Omiw61bVOp-hDHgHaMFaQPfH00aA6OxV53gAuNqf-TYd38KJPJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدارهای امنیتی آمریکا به اسرائیل رسید
🔹
پس از هشدار وزارت خارجه آمریکا درباره سفر آمریکایی‌ها به غرب آسیا، سفارت واشنگتن در تل‌آویو هم درباره احتمال «تنش‌های پیش‌بینی نشده»، هشدار امنیتی صادر کرد.
🔹
سفارت واشنگتن در تل‌آویو اعلام کرد: «ما به آمریکایی‌های ساکن منطقه یادآوری می‌کنیم که همچنان باید احتیاط کنند و آنها را تشویق می‌کنیم که اخبار مربوط به تحولات فوری را دنبال کنند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450832" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15960123c.mp4?token=NmKHkgM_iMLhtBX0imO2D__hr6tdGo6LbrAvz8AY3UJm0K2HkZB5RZRB_ijYTcx8AXX2PquiAWMLbK26lPkll-iZkJSl-6qfFXyv_4m7KHzKQ-aC8o15U6W4v0guP1h_K2eC_uLc1F3Tjl1swdFFUj0a2aPXXElr6Lscfh6krkRiTMIty5RZj75txa7a4YYXLBYU3OXyh6RBERpZxUloO4RNH7fTPXGwDGP4YPpDqN4akSVSFAxYvQshW93CuSZ7YTSqwfXSPUzZWI1y_uu6DKVS5oayHJ6ZZH0XNQN4aSgED_Lg8nSWHm7NV5XQl_w4EGUMyoRlwguX66mSsxyMpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15960123c.mp4?token=NmKHkgM_iMLhtBX0imO2D__hr6tdGo6LbrAvz8AY3UJm0K2HkZB5RZRB_ijYTcx8AXX2PquiAWMLbK26lPkll-iZkJSl-6qfFXyv_4m7KHzKQ-aC8o15U6W4v0guP1h_K2eC_uLc1F3Tjl1swdFFUj0a2aPXXElr6Lscfh6krkRiTMIty5RZj75txa7a4YYXLBYU3OXyh6RBERpZxUloO4RNH7fTPXGwDGP4YPpDqN4akSVSFAxYvQshW93CuSZ7YTSqwfXSPUzZWI1y_uu6DKVS5oayHJ6ZZH0XNQN4aSgED_Lg8nSWHm7NV5XQl_w4EGUMyoRlwguX66mSsxyMpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
پروندهٔ رضا پهلوی، فرزند شاه مخلوع به دادگاه ارسال شد
🔹
دادستان تهران: پس‌از تکمیل تحقیقات، دریافت گزارش‌های مراجع ذی‌صلاح، جمع‌آوری مستندات و انجام اقدامات قانونی، کیفرخواست پروندهٔ رضا پهلوی مطابق قانون صادر و پرونده برای رسیدگی به دادگاه صالح ارسال…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/450831" target="_blank">📅 11:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450829">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303c1c6f25.mp4?token=O2uUpeMVC11VxcaCiZjqDxDgBSYXAjZs3fUiuz9AIMui0xfdaBJ_bW2Gn4YZwR7plZpw6bvlH5kHiDkZZ7QyDF5uGYdqMQxYNaOrqH_VTOgbvNQVX1azuIdTsdCehAYSlSV93Tsk8ssctQPfrUQsMXGC0TjegB9OL83-SMCkl5MgwiNNcz69v9yzu1qMbPqVTNdvg7RHfv44rjZPLeS31yITK1W__4t29BuNbWEc0vT2K0hOf4VolPlXQ3AvkanMsNHuAnZ13lzqsM4s0Eb6GkCjnAXMGVntj0MhjX8sJSPd-B3Y0F8mtNgIemXv52ykvAtEQUavfGA7msLBJgCNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303c1c6f25.mp4?token=O2uUpeMVC11VxcaCiZjqDxDgBSYXAjZs3fUiuz9AIMui0xfdaBJ_bW2Gn4YZwR7plZpw6bvlH5kHiDkZZ7QyDF5uGYdqMQxYNaOrqH_VTOgbvNQVX1azuIdTsdCehAYSlSV93Tsk8ssctQPfrUQsMXGC0TjegB9OL83-SMCkl5MgwiNNcz69v9yzu1qMbPqVTNdvg7RHfv44rjZPLeS31yITK1W__4t29BuNbWEc0vT2K0hOf4VolPlXQ3AvkanMsNHuAnZ13lzqsM4s0Eb6GkCjnAXMGVntj0MhjX8sJSPd-B3Y0F8mtNgIemXv52ykvAtEQUavfGA7msLBJgCNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450829" target="_blank">📅 11:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450828">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9179bbd562.mp4?token=XpEfaY61toLUvx2EMe6f9v1n6Wd-Kni01TSc8uB63Lce2A96e1SaKRlhjqG0DfIH4HzWbAYL2oSQc7jms-g25DzTMzhoIkx1gk8kFvtnEY6-odvmm2R-ur9ge5AHPukpX9m57fLMXapHGbtmz7N4aTXigH9IsNDl-0tdtn8lHus5IMBVrfvaU8zv7mq_efdzOhQJz-em4yD2-ZGdZEsm6L8L9s2MYcMmLksUdTWK_6ysN2gftXPV7-vR9qQpQT1BjjAGa4g6KwwuDMMILy4L3FUsAbec1ZJ17NZ3QXC7OhX8uOPVN8-jPxmXELiTtx8eAIWeE2xzf3Yj_S_kmudJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9179bbd562.mp4?token=XpEfaY61toLUvx2EMe6f9v1n6Wd-Kni01TSc8uB63Lce2A96e1SaKRlhjqG0DfIH4HzWbAYL2oSQc7jms-g25DzTMzhoIkx1gk8kFvtnEY6-odvmm2R-ur9ge5AHPukpX9m57fLMXapHGbtmz7N4aTXigH9IsNDl-0tdtn8lHus5IMBVrfvaU8zv7mq_efdzOhQJz-em4yD2-ZGdZEsm6L8L9s2MYcMmLksUdTWK_6ysN2gftXPV7-vR9qQpQT1BjjAGa4g6KwwuDMMILy4L3FUsAbec1ZJ17NZ3QXC7OhX8uOPVN8-jPxmXELiTtx8eAIWeE2xzf3Yj_S_kmudJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تاکنون ۳۵۰ پروندهٔ حقوقی دربارهٔ جنگ ۱۲ روزه و جنگ رمضان علیه آمریکا و رژیم صهیونیستی ثبت شده
🔹
در جنگ ۱۲ روزه ۲۶۰ پروندهٔ حقوقی در شعبهٔ ۵۵ دادگاه حقوقی تهران علیه آمریکا و رژیم صهیونیستی ثبت شده که بیش از ۳۰۰ هزار خواهان دارد.
🔹
همچنین ۲۰۱ پروندهٔ کیفری در دادسرای امور بین‌الملل دربارهٔ جنگ ۱۲ روزه ثبت شده که ۱۳۷ پرونده با شکایت ۸۰۰ شهروند و ۶۵ پرونده مربوط به شکایت‌های ادارات و سازمان‌هاست.
🔹
در مورد جنگ رمضان هم تاکنون ۹۰ پرونده تشکیل شده است. مرکز وکلای قوه‌قضائیه هم مستنداتی را دربارهٔ خسارت‌ها جمع‌آوری کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450828" target="_blank">📅 11:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450827">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdktHF2IPmJBerZCym0rM6B5r8ThOPeIi7-_P4tPU_qHq0ua3Fe2-TKwp8TxkPfhfCfGy3KeilMKALoqFo5viXlAmH6DOCX5vkjqpJwla7seAhnIaGgv-x21aRxCYpWYMfVjrvA5RsQ8MWZLxm8csb86tc01JTRNPIMjPZ05WPsNKmwpdySpj4iStfmOly-e7IPDdGkwSTOHjTgYstMQZ56g-a8J4uDuP_49hLCY0TWnq0d-DjgmKl0G_OJiSfth2myv0ajwuqjm1F7YqPM52qxuCukI7-8wwwMmI4T12yXGSFSKwJtse54Hsyvh1MfpzlvXdCVYGQ9T-B_F2qwQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلافوئنته: یامال آمادۀ فینال است
⚽️
سرمربی اسپانیا: مسی بی‌همتاست؛ او یک استعداد فوق‌العاده و الگویی برای نسل‌های جوان است.
⚽️
اما لامین باید خودش باشد و بهترین کمکی که می‌توانیم به او بکنیم، این است که اجازه دهیم همان لامینی باشد که همه می‌شناسیم.
⚽️
…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450827" target="_blank">📅 11:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=rgOGopjhHSDgZSQ-L5K3KEZfVRCyP8wH_lk2OE78uCLRAnsPdmz3joBnUCES2Dza1ZF9QnJNXX-KG5TLOSkfZTgWHJF9el4KQDzdDVcKBtl03W4c7aKTRO9eMP0Mvn324gJHnLEUVSwCTtsKiG_drSnzuhLSjfgNFukaVixb2I86AD06G_j2g9RxJWz0jnGvWMLhWp1zMAxG10rntz1RIkq_yrcskIgPV0yuzkVWDLETQDoOnNhrL-nNzAcOTymz-BjidATuxZkymJyahpfXgrNIOT7yY4m4AjKkNOffrEKgm1vbRQIgQlEkbYnwgPGanrYF7YKkx-qYJlJI8dnfBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=rgOGopjhHSDgZSQ-L5K3KEZfVRCyP8wH_lk2OE78uCLRAnsPdmz3joBnUCES2Dza1ZF9QnJNXX-KG5TLOSkfZTgWHJF9el4KQDzdDVcKBtl03W4c7aKTRO9eMP0Mvn324gJHnLEUVSwCTtsKiG_drSnzuhLSjfgNFukaVixb2I86AD06G_j2g9RxJWz0jnGvWMLhWp1zMAxG10rntz1RIkq_yrcskIgPV0yuzkVWDLETQDoOnNhrL-nNzAcOTymz-BjidATuxZkymJyahpfXgrNIOT7yY4m4AjKkNOffrEKgm1vbRQIgQlEkbYnwgPGanrYF7YKkx-qYJlJI8dnfBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450826" target="_blank">📅 11:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌‌
🔴
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450825" target="_blank">📅 11:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq5SPEKHoGkN6hox6A2yYdigkchMS7OgbTovYikZIAohkMB-lsKUUkkDYgwi8Bwy6ULBuusif_Ztq3IKegTGv8mcnrUK-NvV5MYRBCBQ18I21kVFDWkl9R2Da_PZMIaGWFoLhNE4hulgbr6fcPnmm2yE6PiJvlDL3OocNhs6_eax4BnpEIr88Zb3B2C4AhyFflou_z-6-U4mBh4TLDXRJ09BHgPW3Tm90ZvipcoeXFyIqOgsDyWuMXqArlVPzOl9_XGXIRHTZdOeI9nC2Zj4Y8IeVfe92zVZ7Zmwo9KtscWWNxz-FJC7UVUBbSWyCTjCh2-1jT1ssmG9Xo43PrPV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکلۀ روستای بونجی هدف حملات موشکی قرار گرفت
🔹
معاون استاندار هرمزگان: در تداوم حملات دشمن جنایتکار آمریکایی به نقاط مختلف هرمزگان، این‌بار تأسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکلۀ روستای بونجی از توابع شهرستان جاسک…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450824" target="_blank">📅 11:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450823">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b936586a88.mp4?token=iHt7vuEuPQRbHuXrHoCDZlAEJfKBAgSmf0t2COR_TRsWeWYeqm3ZfFyCMaPAmo0fx8uBijMk8ht9nEYwkuxkcAgHNWzKO-hORGuJqVOwhZnjFl4va70WMip4lj2bdiY7UF3cKt4mdiJipL6ZZYKVJcM7mxZsVfaBaBYSynlmjPlU--ZEVwLCOosT_MImKs4AUZKw40o_sLaAvGfaKeDdiDeCbZ9lZ2yHe5xRroDqb92Gt-CI0h5eycc9Q9BF3MSGUtuaRyU2XCkiDLEaef144S03G22x2NU_Oa2v528N5ObxhAOJzIkEaj_T2iULcYkFp9KJ_SHMD3IGtDN8xgCUiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b936586a88.mp4?token=iHt7vuEuPQRbHuXrHoCDZlAEJfKBAgSmf0t2COR_TRsWeWYeqm3ZfFyCMaPAmo0fx8uBijMk8ht9nEYwkuxkcAgHNWzKO-hORGuJqVOwhZnjFl4va70WMip4lj2bdiY7UF3cKt4mdiJipL6ZZYKVJcM7mxZsVfaBaBYSynlmjPlU--ZEVwLCOosT_MImKs4AUZKw40o_sLaAvGfaKeDdiDeCbZ9lZ2yHe5xRroDqb92Gt-CI0h5eycc9Q9BF3MSGUtuaRyU2XCkiDLEaef144S03G22x2NU_Oa2v528N5ObxhAOJzIkEaj_T2iULcYkFp9KJ_SHMD3IGtDN8xgCUiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
کویت مدعی شد در جریان حملات موشکی به این کشور، یک نیروگاه و تأسیسات آب شیرین‌کن به‌شدت آسیب دیده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450823" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450822">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZtJtVFeVW0EbY3L70n6vipSPhjwBkaq2QqZ4SawSBInk7VfjGTchVEqmw0xvCBNT8m_61FacPLK0wzFWHWVB4avpKLAS7h0JoSkQ_8usY53WwpHZuzfExFErpv5MSQb8IoQDeMkUS_MlffeLsMJMJUVJ75zDtwug8b_KDVbNUogWAmLC20T0Fsn50zUdYwRJUfh3ORuEk6IM7l16gq7VKP-7yCgbLAzcKD1fDC6_OiFo-eTIE0qrU7mQjMIgpHK9olecWycd3CR5RIEygs4-njP6JMYMN7hZT5iI8JosZD3a9HR1YdednIn1mQ96nZ6UyvtHP8C0JbGWheTW9NV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌خروس‌ها پرواز نکردند؛ صعود مقتدرانه اسپانیا به فینال جام‌جهانی
⚽️
اسپانیا ۲ - ۰ فرانسه  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450822" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450821">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d7c808989.mp4?token=d9kUIPX_fHmFwbSN6aBZK46DxP3Wk42oz87tg2QtWr2CXlhHiXRYVKEXUCLTKi3-ZCyJVsSJbDJwRoa6VU7jkx-rTryGZQGWKx0gBgq7RiszOFruIfngZnY-E_eSmtKk2nMrbsRBJAqZzTLhAUUy8DPJeFmJH5h5G4mf7a7AA5di01FSJI38AOAYKa-QebuVdI2ys-FSNTmGxNbPvVUN3xHBlNjl0TiaOq4EvT0VaKX7KbJQqhVLBCGr7g4bpb5SDV7MIbLGQLCuKEhBcgKfHCbxpeNRiOSEPD-G0y2mCBI45goCm5fo3cxRHSITRczwJdksPhtA9MUjLZpGD3v4yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d7c808989.mp4?token=d9kUIPX_fHmFwbSN6aBZK46DxP3Wk42oz87tg2QtWr2CXlhHiXRYVKEXUCLTKi3-ZCyJVsSJbDJwRoa6VU7jkx-rTryGZQGWKx0gBgq7RiszOFruIfngZnY-E_eSmtKk2nMrbsRBJAqZzTLhAUUy8DPJeFmJH5h5G4mf7a7AA5di01FSJI38AOAYKa-QebuVdI2ys-FSNTmGxNbPvVUN3xHBlNjl0TiaOq4EvT0VaKX7KbJQqhVLBCGr7g4bpb5SDV7MIbLGQLCuKEhBcgKfHCbxpeNRiOSEPD-G0y2mCBI45goCm5fo3cxRHSITRczwJdksPhtA9MUjLZpGD3v4yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشدید حملات روسیه به کشتی‌ها و بنادر اوکراین
🔹
طبق اعلام مقامات اوکراین، ارتش روسیه دیروز به ۲ شهر بندری اوکراینی در دریای سیاه حمله کرد. مقامات اوکراینی گفتند که «روسیه در یکی از این حملات، به ۳ کشتی با پرچم خارجی در شهر میکولایف آسیب زد».
🔹
وزارت دفاع روسیه اعلام کرد که «ارتش دیشب به تأسیسات بندری اوکراین در اودسا و چورنومورسک و کشتی‌های اوکراینی در دریای سیاه حمله کرد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450821" target="_blank">📅 10:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450820">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450820" target="_blank">📅 10:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450819">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e463366e51.mp4?token=nHLJ1kSlmaL3EyqNm_eo45lCYB4GEvnuMXYpCGWk0iiaInEHSNeu43yI6DlMls2shfyKh88z_VfZU0aYT2H27_-sq5Ld3AQaui-sclRWLcFNkt60N5aN9vHrOiRomfVhHtTYK57LzYQanIhDk4rdpfudhwCq1CXQfji4dX23-qfNl7kky7HsfI5W5nzed5L9zbO8zX9VWt7KnnWmf3JDQ015GNT3ij7A8ZphmN8vvVf-hGEnNLiVwMl-jMiOhjPofmsZ-Mmw_Tjy9FbgSoCbn9j1xpdGdMQMdbtSoa5I_Kx3nXQSaV35m_8xjp1PpfrLaZ8NaYXvVBp5nJh9oJzhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e463366e51.mp4?token=nHLJ1kSlmaL3EyqNm_eo45lCYB4GEvnuMXYpCGWk0iiaInEHSNeu43yI6DlMls2shfyKh88z_VfZU0aYT2H27_-sq5Ld3AQaui-sclRWLcFNkt60N5aN9vHrOiRomfVhHtTYK57LzYQanIhDk4rdpfudhwCq1CXQfji4dX23-qfNl7kky7HsfI5W5nzed5L9zbO8zX9VWt7KnnWmf3JDQ015GNT3ij7A8ZphmN8vvVf-hGEnNLiVwMl-jMiOhjPofmsZ-Mmw_Tjy9FbgSoCbn9j1xpdGdMQMdbtSoa5I_Kx3nXQSaV35m_8xjp1PpfrLaZ8NaYXvVBp5nJh9oJzhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اچ‌اف‌آر: تنها مسیر فعال در تنگهٔ هرمز مسیر ایران است
🔹
موسسهٔ تحلیلی در بخش نفت‌وگاز: آمریکا در صورت واگذاری تنگهٔ هرمز به ایران، این کشور را به قدرتمندترین بازیگر نفت جهان تبدیل خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450819" target="_blank">📅 10:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrHp5JM74JKPrBr4RWgldHc_bg3SLbxFapQy4cgpPTkkQAPkn1LJ-gjma5P9EkomIM259Mh7JybtWtULRBACS6G5qqThyytkdKvNoRVdBruCqcWsnBVN44T1pCR1mBV_4e78asgsk-Hb1Nhs4bibDgm2YV6014IVUiEVHxFCH6y-PV2FiiG2vnZ5KH3N8VcC8B0nngcZe25mK-3sj7vyJs2pHj8bRh06CZ3rxQgRs7H3lwd24ErgrB2kBgZdJoow9WvbVgu-wmtk1346PkE71XfTgThqExqNw0mdcu4kVQj4xWi1IIUvsrzQS9AmVNjJVdMLpDstPVtrx8IQ0LjqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ جدید ایران برای دریافت هزینهٔ خدمات محیط‌زیستی در تنگهٔ هرمز
🔹
رئیس مرکز امور بین‌الملل سازمان حفاظت محیط‌زیست از ارسال نظام‌نامهٔ دریافت بهای خدمات محیط‌زیستی از کشتی‌های عبوری تنگهٔ هرمز به دولت خبر داد و اعلام کرد: هزینهٔ این خدمات براساس نوع کشتی، ماهیت بار، سوابق شناور و سطح مخاطرات زیست‌محیطی آن تعیین می‌شود.
🔹
خورسند، رئیس مرکز امور بین‌الملل سازمان محیط‌زیست دربارهٔ پشتوانهٔ حقوقی این طرح گفت: براساس کنوانسیون حقوق دریاها (UNCLOS) و معاهدات مرتبط با آن، رژیم حقوقی «عبور بی‌ضرر» برای تردد کشتی‌ها در آب‌های سرزمینی کشورها تعریف شده و مطابق این مقررات، برخی اقدامات می‌تواند ناقض اصل عبور بی‌ضرر تلقی شود و به کشور ساحلی یا کشور مجاور تنگه این حق را بدهد که بگوید «این اصل نقض شده است». در چنین شرایطی اگر سلامت، امنیت و محیط‌زیست کشور ساحلی در معرض خطر قرار بگیرد، می‌تواند در چهارچوب حقوق بین‌الملل، اقدامات قانونی لازم را برای حفاظت از محیط‌زیست و منافع خود انجام بدهد.
🔹
درصورتی‌که عبور بی‌ضرر نقض شود، کشور ساحلی می‌تواند در عبور و مرور کشتی‌ها مداخله کند و در قبال خدماتی که ارائه می‌کند، هزینه دریافت کند. در این زمینه، دو سرفصل مجزا مورد توجه قرار دارد؛ آسیب‌های بهداشتی و آسیب‌های محیط‌زیستی.
🔹
اصل موضوع این است که تأمین امنیت و پایداری تردد دریایی مستلزم انجام اقداماتی مشخص و پرداخت هزینه‌های مرتبط با آن است. امنیت تنگهٔ هرمز بر عهدهٔ جمهوری اسلامی ایران بوده، هست و خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450818" target="_blank">📅 10:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در مهران
🔹
سپاه ایلام: به‌دلیل خنثی‌سازی مهمات باقی‌مانده از حملات دشمن در منطقهٔ رضاآباد مهران، احتمال شنیدن صدای انفجار از ساعت ۱۷ تا ۱۹ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450817" target="_blank">📅 10:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توجیه وزیر خارجهٔ اردن برای وجود پایگاه‌های آمریکایی در این کشور
🔹
ایمن الصفدی: آمریکا هیچ پایگاهی در اردن ندارد اما سربازان آمریکایی در چارچوب همکاری‌های نظامی میان امان و واشنگتن در کشور ما حضور دارند. @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450816" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
وزارت دفاع بحرین از حملهٔ موشکی به این کشور خبر داد و طبق معمول مدعی «رهگیری حملات هوایی ایران» شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450815" target="_blank">📅 09:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تعویق آزمون‌های نهایی ۴ استان جنوبی در ۲ روز
🔹
ستاد عالی آزمون‌های وزارت آموزش‌وپرورش: امتحانات نهایی پایه‌های یازدهم و دوازدهم در استان‌های هرمزگان، بوشهر، خوزستان و سیستان‌وبلوچستان در روزهای ۲۸ و ۲۹ تیر لغو و زمان برگزاری آن متعاقباً اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450814" target="_blank">📅 09:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
آژیرهای خطر باز هم در کویت فعال شد
🔹
منابع خبری گزارش دادند پایگاه‌های آمریکا در کویت هدف حملات ترکیبی موشکی و پهپادی قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450813" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرمانداری دزفول: به‌دلیل انجام عملیات انهدام مهمات، احتمال شنیده‌شدن صدای انفجار از ساعت ۱۰ صبح امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450812" target="_blank">📅 09:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMN9eNkee14zukAu1Y8iuNti-m6pucN3xzfHjn5LvLF6_v6oYbHuqCRBw0DI2ZEN-XcKXNIoUvz5Mt2nueNPloxV7p8y1-qkrKxxE4c9I0YNN3978zjZ36kTeyLrTVUCxr6qp5zoTsBKJF7iBG8xdYrXNJbKKb5WmZkoD0XG5245oWfHJOZMU05oWJuhsLFdHoZJOV99EIdvTTWTZHryWe9_uoVwhUJuIb3esxzqWHZ7GARDuG1VwG9O48B3ZgAWLh7v3wVVdOw97HPD74nJPhETpvj8StM9OHXrKBgvFLbmWUt9lfhxhAFyeB4OWKuYrr01RdhjDZ1EeMAxv5ipyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQmcsZ0Sv1POB40gRKn57FMkbxsg3r7sAe9CN0dy9dvsxLftf87XcTVQ2FdmYa-h57dQw1l_HwbeblSOBNUT4J5azSn11pSzX4LNT4MfjoYkDvfBJFXezK3aAPRcp9T1Gsab3rC3LFFn4-1gQ1xo7LjImIPwQvpj4jyGsNh852XBA1GrDZ1VuKFe6LIl66QzvMU0edzwPfSkRsBQX7IRJ09Lx5gJ6_trTglVFpDI-OYIgVffQAh0DL1pu_Jl4rKHGrBZ3tHhCeOTUaJDLrK9l9W6uN8rupEBSDlAIUC1HSoh5sudUcM6ZMKOwdXmx6Lh2KW7NtGpNOL2vUYV5Z2jyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8181cca6e3.mp4?token=nCLdM84gMUHgfC78l9C_sG9-aIym9Uvgotc68WNsAvlWbPoVo44ugdULmvHSirZFDgdK2ot8tp0r0HBE0tQQjN9sdRpJDNqjKJL2F_Snr1315Oid8Cn4ury1wezPod1r56Gtuv9AJK0khkL1yDOire84qx7qrojFgoeN-xQtvhzNqTEiS2UvIZSlaPxu4qTDLHZyQs3suc2_LyGRUFub2FPOPg717OeZO30s2aoxpIEtogjajpoYoUwsE9-BSiB_Mg2QTG-_nUMlAbw5y3lQccs_MRB5kc1grB3GZtphxDqS2BMb42_irfbfI2Gu4txNXP3jv8uuz7U0YJz3ips-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8181cca6e3.mp4?token=nCLdM84gMUHgfC78l9C_sG9-aIym9Uvgotc68WNsAvlWbPoVo44ugdULmvHSirZFDgdK2ot8tp0r0HBE0tQQjN9sdRpJDNqjKJL2F_Snr1315Oid8Cn4ury1wezPod1r56Gtuv9AJK0khkL1yDOire84qx7qrojFgoeN-xQtvhzNqTEiS2UvIZSlaPxu4qTDLHZyQs3suc2_LyGRUFub2FPOPg717OeZO30s2aoxpIEtogjajpoYoUwsE9-BSiB_Mg2QTG-_nUMlAbw5y3lQccs_MRB5kc1grB3GZtphxDqS2BMb42_irfbfI2Gu4txNXP3jv8uuz7U0YJz3ips-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انبار نفتی مسکو در حمله پهپادی اوکراین به آتش کشیده شد
🔹
ارتش اوکراین در ادامهٔ حملات پهپادی به روسیه، دیشب زیرساخت‌ انرژی در مسکو را هدف قرار داد. رسانه‌های اوکراینی خبر دادند که در این حملات پهپادی، انبار نفتی پایتخت روسیه آتش گرفت.
🔹
تصاویر منتشرشده در رسانه‌ها نشان می‌دهد که دود سیاه غلیظی از یک انبار نفت در شهر نوگینسک(واقع در ۵۰ کیلومتری شرق کرملین) بلند شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450809" target="_blank">📅 09:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع خبری از وقوع چند انفجار در کویت خبر دادند و آژیرهای خطر در مناطق مختلف این کشور به‌صدا درآمد
🔹
این منابع از اصابت موشک و پهپاد به مقرهای آمریکا در کویت خبر دادند. ارتش کویت هم مدعی شد که درحال «رهگیری موشک‌ها و پهپادهای ایران» است. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450808" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450807">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
منابع خبری از وقوع چند انفجار در کویت خبر دادند و آژیرهای خطر در مناطق مختلف این کشور به‌صدا درآمد
🔹
این منابع از اصابت موشک و پهپاد به مقرهای آمریکا در کویت خبر دادند. ارتش کویت هم مدعی شد که درحال «رهگیری موشک‌ها و پهپادهای ایران» است.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450807" target="_blank">📅 08:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450806">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
سپاه: اسکلهٔ پشتیبانی سوخت ناوگان آمریکا، محل تجمع پرنده‌های جنگی، مرکز داده‌های اطلاعاتی و یک مرکز سیگنالی و مخابراتی آمریکا درهم کوبیده شد
🔹
روابط‌عمومی سپاه پاسداران انقلاب اسلامی: مردم قهرمان و با ایمان ایران! دریادلان غیور نیروی دریایی سپاه در امتداد حضور حماسی شما ملت بزرگوار در خیابان میدان رزم را هم به صحنهٔ نمایش عجز دشمن جنایتکار تبدیل کردند و علاوه بر کنترل قدرتمندانهٔ تنگهٔ هرمز، در موج ۱۹ عملیات نصر۲ در پاسخ به تجاوزات دیشب ارتش کودک‌کش آمریکا، اسکلهٔ پشتیبانی سوخت ناوگان آمریکا در بندر الاحمدی کویت و محل تجمع پرنده‌های جنگی دشمن در پایشگاه «شیخ عیسی» بحرین را هدف عملیات کوبندهٔ پهپادی و موشکی خود قرار دادند و مرکز داده‌های اطلاعاتی دشمن در بحرین با عنوان باتلکو را در هم کوبیدند.
🔹
رزمندگان نیروی دریایی همچنین یک مرکز سیگنالی و مخابراتی آمریکا در کویت را منهدم کردند.
و ما النصر الا من عند الله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450806" target="_blank">📅 08:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
برخی منابع از وقوع انفجار در بندر صنعتی ینبع، ‌و پایگاه‌های آمریکایی در الخرج عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450805" target="_blank">📅 08:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYRKgS-T-vWe9c3WEhyNIzja8Z8vxnOgg7Maf1Xd40_H9ul9hxeClno9OZXP8B9zKJFmbvW1kD8y-axEIlc6RAWoWg0Izcc0ACETSvXmGLuHCO_NMrUoMLMg2tz3rGbSftPs2dDRx6lNstQ2UM7vu-VATBtoMWLp5yGQzgJ100RbRUMCFweJ2_IqWg2mFZ2mHngigOn2Q17EG1rB52sXhdJwTkNlc6wCRTX1frYh8cWBiK_IldsNuxFaLEUvs0IIcdZbAKVHWjIgCnJOIPwbWLQwNkY-ZBom1kFLGW8QEzPRD365WMb63AaEHoXj51DQBmRo9dyFYiS1YIxJ3ldOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیفیت هوای تهران قابل‌قبول است
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای پایتخت امروز روی عدد ۸۵ قرار گرفته و در وضعیت قابل‌قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450804" target="_blank">📅 08:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450803">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: در ساعات گذشته ۴ کشتی متخلف متوقف شدند
🔹
در ساعات گذشته، ۴ فروند کشتی متخلف با حمایت ارتش تروریست امریکا قصد عبور از تنگۀ هرمز را داشتند که طی یک عملیات ترکیبی موشکی و پهپادی هر ۴ کشتی درجای خود متوقف شدند.
🔸
نیروی دریایی سپاه با قاطعیت…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450803" target="_blank">📅 07:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
منابع خبری از شنیده‌شدن صدای انفجار در کویت و اردن گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450802" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
صدای انفجارهای جدید در بحرین و کویت
🔹
منابع عربی از شنیده‌شدن صدای پیاپی انفجارهای شدید در کویت خبر دادند.
🔹
براساس این گزارش‌ها، پایگاه نظامی علی‌السالم کویت آماج این حملات قرار گرفته است.
🔹
شبکۀ الجزیره نیز از به صدا درآمدن دوبارۀ آژیرهای خطر در کویت خبر…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/450801" target="_blank">📅 07:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در محدودۀ جنوب اصفهان
🔹
سپاه استان اصفهان: از ساعت ۸ صبح تا ۱۴ بعد ازظهر امروز احتمال شنیده‌شدن صدای انفجار کنترل شده در محدودۀ صفه، بهارستان و اطراف وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450800" target="_blank">📅 07:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
منابع محلی از حملۀ مستقیم موشک‌های ایرانی به تأسیسات آمریکایی در بحرین، و انفجارهای مداوم در آن محل‌ها خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450799" target="_blank">📅 07:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450798">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjIty5AcYUYj9_y_izEP3sl1BIcw4GZ7H92NluAIeZ-mzfqY4hvEDZl85B7Xwz08OUL2FhTDtdlPdJbKa0vB9kvzmlQ3D9t-FBL62P3QJMjm0eIPdGd4BQkgAbmsgNCApUGvxR0SdDlqH5hym6qYRl8iJ_1OTbKi2saMJOejnPmzh0NmmcEkFvnJfcBwVThQbh550WxRH0Or1fNh6zLlLJgvVyDerhahSfCx3QW5OwKIoI3jPz8sy1JOvYbt1zohBFziYnvvxWxYI9DURQl68KDecjQEuvhgIdv2YU85jDmTuYFgfe0SZgXczBNXJFzkU0T-U004T3UrMjWOgc0n0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویر منتشر شده در فضای مجازی از برخاستن ستون‌های دود در کویت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/450798" target="_blank">📅 07:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz0rhi_1hML4NDgiD_C0XGonLMsLbvP9OaNq2YJBbYcg1bxC2rqEvUy56kVBDcaxqTCkr5AD71aTXY-hzq9-3dJjNavp8ESmvIzRoZclOvNXpNaiQraH0s2TnmM9K6obY6hQVmVb1p3Y1n6lG0PrhL39FhfY_qPVcFk76RMzNBHmy9lWZmPkKFXpUt7pLrOflb_q0gViAlweGaE5OjxmcbUWQHsa2I4wHUwySZlUIjYyqRtltYNXnjXYlhCmfcQOjZpu5IQj7f8M5kSKvis8opj_JFIEF4Uv_ELPRrT9VSyx0Y0AidJVlE9sYiDfalsPf-LwEofY-IgvNM_YvdODbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر، صبح شنبه حوالی شهرستان بندرخمیر در استان هرمزگان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450797" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
رسانه‌های عربی: ناوگان پنجم نیروی دریایی آمریکا در بحرین، مورد حملۀ هوایی شدید قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450796" target="_blank">📅 06:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450795">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd1266d40.mp4?token=nusexP2ATpDOiodhp8i0MeYbXRoYCLIc97Xz5p1OUMjevRVi1MAK4BgNX8ed-E9rGx2WfXssLjv5vFjLBGx4BvZWAWwH2nCBwy6i6wB1B5nRf_HEpzrXiFsv5Y_etl9Ul14-tmo48QikD8wxg3jsNoVYjxYtTSz1KkrVyRMzwp9LiIJ7PkTT3qiUKYIl9EVIYkhyeGrvmGBGP3_agkqDbHRhQepCgprPfz5a-wLp2EKgsKTm22ypTF0GRFd-rRre4EsouWRpBlIl-q-7kBUCZfgdsvFn9BnwgL-vBgtTDGwVFXZBsLuUNKP6Pqo5yAi6REChvFyaZrBvYxN7b4YqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd1266d40.mp4?token=nusexP2ATpDOiodhp8i0MeYbXRoYCLIc97Xz5p1OUMjevRVi1MAK4BgNX8ed-E9rGx2WfXssLjv5vFjLBGx4BvZWAWwH2nCBwy6i6wB1B5nRf_HEpzrXiFsv5Y_etl9Ul14-tmo48QikD8wxg3jsNoVYjxYtTSz1KkrVyRMzwp9LiIJ7PkTT3qiUKYIl9EVIYkhyeGrvmGBGP3_agkqDbHRhQepCgprPfz5a-wLp2EKgsKTm22ypTF0GRFd-rRre4EsouWRpBlIl-q-7kBUCZfgdsvFn9BnwgL-vBgtTDGwVFXZBsLuUNKP6Pqo5yAi6REChvFyaZrBvYxN7b4YqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در اردن و کویت، آماج حملات پهپادی ارتش
🔹
روابط عمومی ارتش: ساعاتی قبل، پهپادهای انهدامی ارتش در مرحلۀ چهاردهم عملیات صاعقه، انبار مهمات ارتش متجاوز آمریکا در اردوگاه العدیری و ساختمان‌های ستاد و انبارهای مهمات این ارتش کودک‌کش در پایگاه…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/450795" target="_blank">📅 06:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
رسانه‌های عربی:
ناوگان پنجم نیروی دریایی آمریکا در بحرین، مورد حملۀ هوایی شدید قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/450794" target="_blank">📅 06:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای چندین انفجار در بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/450793" target="_blank">📅 06:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450792">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکلۀ روستای بونجی هدف حملات موشکی قرار گرفت
🔹
معاون استاندار هرمزگان: در تداوم حملات دشمن جنایتکار آمریکایی به نقاط مختلف هرمزگان، این‌بار تأسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکلۀ روستای بونجی از توابع شهرستان جاسک هدف اصابت موشک  قرار گرفت.
🔹
بر اثر حمله به این تاسیسات، آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است.
🔹
بررسی‌های اولیه برای ارزیابی میزان خسارات و آثار این حمله در حال انجام است و تلاش‌ها برای پایدارسازی وضعیت آب شرب منطقه آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/450792" target="_blank">📅 06:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
منابع عربی: انفجارهای مجدد پایگاه‌های نظامی آمریکا در بحرین و کویت را به لرزه درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/450791" target="_blank">📅 05:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
حملۀ هوایی دشمن آمریکایی به جزیرۀ هرمز
🔹
استانداری هرمزگان: در ساعت ۵ بامداد، نقطه‌ای در جزیرۀ هرمز هدف حملۀ دشمن آمریکایی قرار گرفت.
📝
جزئیات این حادثه پس از انجام ارزیابی‌های اولیه و جمع‌بندی اطلاعات، متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450790" target="_blank">📅 05:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
صدای انفجارهای جدید در بحرین و کویت
🔹
منابع عربی از شنیده‌شدن صدای پیاپی انفجارهای شدید در کویت خبر دادند.
🔹
براساس این گزارش‌ها، پایگاه نظامی علی‌السالم کویت آماج این حملات قرار گرفته است.
🔹
شبکۀ الجزیره نیز از به صدا درآمدن دوبارۀ آژیرهای خطر در کویت خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450789" target="_blank">📅 05:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به‌صدا درآمدن دوباره آژیرهای خطر و شنیده شدن صدای انفجار در بحرین
🔹
منابع خبری اعلام کردند پایگاه پنجم نیروی دریایی آمریکا در بحرین هدف موشکهای ایرانی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450788" target="_blank">📅 05:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
حملۀ موشکی دشمن آمریکایی به حوالی جاسک
🔹
استانداری هرمزگان: در ساعت ۴:۴۴ دقیقه، نقطه‌ای در حوالی جاسک هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
📝
جزئیات این حادثه پس از انجام ارزیابی‌های اولیه و جمع‌بندی اطلاعات، متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/450787" target="_blank">📅 04:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
حملۀ مجدد دشمن آمریکایی به حوالی بندرعباس
‌
🔹
استانداری هرمزگان: در ساعت ۳:۵۰ دقیقه، نقطه‌ای در حوالی بندرعباس مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
📝
اخبار تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/450786" target="_blank">📅 04:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450784">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
رسانه‌های عربی: انفجارهای متعددی بار دیگر پایگاه‌های نظامی آمریکایی در کویت را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450784" target="_blank">📅 04:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450783">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef9c760ee8.mp4?token=uVtPTY6dnINctPdHzgmUN521bz04WNzUhMxB5vCnc2CWU-nTmbObQGVuNVjttVLyAtTQqI72uGg8nFR8d_6-3VyMDyCCm5GZobfeFUhOlwAxAMo5VD0zeVNMEqhPNHdzGBLAWorciBZg9xQO-c9Wqio5BzEEbi9-JZAePhI-7k1KYIP9LaXPuK9jWT7HZxy1e49mepDFWxvjAPQOCQgxgJnwajsGbH2WFaig_0e32OlIwcLlDqvsj39kcFxDqGgYHeY3xzw1a796XLWKsxeogjM4Ss4_iTG_QMAJFboVSPtfNCtB1M2YJpL3vDjQIhnPgXRwrs1BHCSv86DizkVrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef9c760ee8.mp4?token=uVtPTY6dnINctPdHzgmUN521bz04WNzUhMxB5vCnc2CWU-nTmbObQGVuNVjttVLyAtTQqI72uGg8nFR8d_6-3VyMDyCCm5GZobfeFUhOlwAxAMo5VD0zeVNMEqhPNHdzGBLAWorciBZg9xQO-c9Wqio5BzEEbi9-JZAePhI-7k1KYIP9LaXPuK9jWT7HZxy1e49mepDFWxvjAPQOCQgxgJnwajsGbH2WFaig_0e32OlIwcLlDqvsj39kcFxDqGgYHeY3xzw1a796XLWKsxeogjM4Ss4_iTG_QMAJFboVSPtfNCtB1M2YJpL3vDjQIhnPgXRwrs1BHCSv86DizkVrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی منابع خبری می‌گویند که سامانه‌های دفاعی آمریکا و اردن نتوانسته‌اند هیچ یک از موشک‌های شلیک شده به پایگاه موفق السلطی را رهگیری و منهدم کنند.   @FarsNewsInt</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/450783" target="_blank">📅 03:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450782">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
حملۀ موشکی دشمن آمریکایی به جزیرۀ لارک
🔹
استانداری هرمزگان: ساعت ۱:۲۷ بامداد نقطه‌ای در جزیرۀ لارک مورد حملۀ دشمن آمریکایی قرار گرفت.
🔹
گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/450782" target="_blank">📅 03:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450781">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552459cf22.mp4?token=KGYEVWEJ8T46DqTMiIcL5BHnv72DO6o3yq1SUdr-n0uXOmtxDoKNrbYungRzSqINvi_Fxnmf8HMexrtxKYQ93PezUHf3-nadwhxdmmC4-jfx__t8Xhya9waNmYUp8iQPjgIahyNzRz4Tt9DYCYMkd7Rwaj3FYFgqXXC-7-HWmxr5xu16gnpX0ysTzlmB9sEsC1f8aZ8aVWoq9-KUMITTDRPJvKsNeT89-gf-n3J39QlsfFRDe8tjFe-7J9YVkxYGFZJsun-Hg54kQo13DW9KhJql05Btx007-9-jaqU3SlCn9AQpcJwOlpm1WWlP12eTGXE3FoePey0CSnyQADhD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552459cf22.mp4?token=KGYEVWEJ8T46DqTMiIcL5BHnv72DO6o3yq1SUdr-n0uXOmtxDoKNrbYungRzSqINvi_Fxnmf8HMexrtxKYQ93PezUHf3-nadwhxdmmC4-jfx__t8Xhya9waNmYUp8iQPjgIahyNzRz4Tt9DYCYMkd7Rwaj3FYFgqXXC-7-HWmxr5xu16gnpX0ysTzlmB9sEsC1f8aZ8aVWoq9-KUMITTDRPJvKsNeT89-gf-n3J39QlsfFRDe8tjFe-7J9YVkxYGFZJsun-Hg54kQo13DW9KhJql05Btx007-9-jaqU3SlCn9AQpcJwOlpm1WWlP12eTGXE3FoePey0CSnyQADhD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی منابع خبری می‌گویند که سامانه‌های دفاعی آمریکا و اردن نتوانسته‌اند هیچ یک از موشک‌های شلیک شده به پایگاه موفق السلطی را رهگیری و منهدم کنند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/450781" target="_blank">📅 03:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450780">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=cXhRnW-n2hAibgB8KLWgdVdLgBWetRSNYMx6nL05iGC-PMGH3hjCEytyzLjE4fRgO6LNzUC2GCaWW_Wg1E2w7h9AynKElnPbUoq2GjiLMT0miP5B4K8K8ij3-X8rK5k2bKOxhLjJaZYBKDOiK4wX7CqbNlp5BUj09HZ-vNTas1DyyUacW7YJSowAiOo341M3ZQWdFgc6OXycQ2bmwVF4lbrJFNUuvoAzw_2m6Jgb40XEL2GPb7OwRTco5iDT6dbpnzHoEX48nNR6x2PPk4h3UdaqiPEmk1WEQGIlGBXW9wsI3FPbS31xUziQE7Z2ggAsKDjzLedTXx_2l6ypBMWNBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=cXhRnW-n2hAibgB8KLWgdVdLgBWetRSNYMx6nL05iGC-PMGH3hjCEytyzLjE4fRgO6LNzUC2GCaWW_Wg1E2w7h9AynKElnPbUoq2GjiLMT0miP5B4K8K8ij3-X8rK5k2bKOxhLjJaZYBKDOiK4wX7CqbNlp5BUj09HZ-vNTas1DyyUacW7YJSowAiOo341M3ZQWdFgc6OXycQ2bmwVF4lbrJFNUuvoAzw_2m6Jgb40XEL2GPb7OwRTco5iDT6dbpnzHoEX48nNR6x2PPk4h3UdaqiPEmk1WEQGIlGBXW9wsI3FPbS31xUziQE7Z2ggAsKDjzLedTXx_2l6ypBMWNBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پایگاه‌های آمریکا در اردن و کویت، آماج حملات پهپادی ارتش
🔹
روابط عمومی ارتش: ساعاتی قبل، پهپادهای انهدامی ارتش در مرحلۀ چهاردهم عملیات صاعقه،
انبار مهمات ارتش متجاوز آمریکا در اردوگاه العدیری و ساختمان‌های ستاد و انبارهای مهمات این ارتش کودک‌کش در پایگاه علی‌السالم و چند پل ارتباطی در کویت
را هدف قرار دادند.
🔹
اردوگاه العدیری، از مراکز مهم پشتیبانی و تجدید سازمان رزم نیروهای آمریکایی و پایگاه علی‌السالم نیز یکی از بزرگترین مراکز پشتیبانی و هماهنگی عملیات هوایی آمریکا در منطقه خلیج فارس به شمار می‌رود.
🔹
در ادامۀ این حملات،
مخازن سوخت ارتش متجاوز در پایگاه الازرق اردن نیز
هدف حملات پهپادی ارتش قرار گرفت.
🔹
پایگاه هوایی الازرق اردن به دلیل موقعیت، زیرساخت‌ها و استقرار تجهیزات نظامی مدرن و سرمایه‌گذاری کلان آمریکا، به یک پایگاه حیاتی برای ایالات متحده تبدیل شده است که برای کنترل منطقه و عملیات‌های نظامی در غرب آسیا نقش کلیدی ایفا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/450780" target="_blank">📅 03:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450779">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
همزمان با حملات به کویت، عربستان و اردن، منابع عربی از شنیده‌شدن صدای انفجار در بحرین نیز خبر داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/450779" target="_blank">📅 03:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450778">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه‌های عربی از ادامه‌دار بودن حملات به کویت و اردن خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450778" target="_blank">📅 02:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450777">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌ رسانه‌های عربی: حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.  @Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/450777" target="_blank">📅 02:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450776">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رسانه‌های عربی:
صدای انفجارها در پایگاه‌های آمریکایی اردن به حدی بود که در مناطق اشغالی شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/450776" target="_blank">📅 02:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450775">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
منابع محلی از
حملۀ موشکی به پایگاه‌های آمریکایی کویت
خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/450775" target="_blank">📅 02:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450774">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
حملات دشمن به هرمزگان تاکنون ۳ شهید و ۸ مجروح برجای گذاشته است
🔹
معاون استاندار هرمزگان: در پی حملات دشمن به برخی نقاط استان هرمزگان سه نفر شهید و ۸ نفر مصدوم شدند.
🔹
دستگاه‌ها و عوامل امدادی و انتظامی از دقایق اول در محل حادثه حضور دارند.
🔹
گزارش‌های تکمیلی پس از جمع‌بندی نهایی و بررسی‌های میدانی اطلاع‌رسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/450774" target="_blank">📅 02:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450773">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌‌
🔴
منابع عربی: پایگاه‌های نظامی آمریکا در عربستان سعودی، هدف حملۀ موشکی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/450773" target="_blank">📅 02:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در امیدیه خوزستان
🔹
دقایقی پیش اهالی امیدیه از شنیده‌شدن صدای انفجار خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/450772" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/450771" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450770">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
رسانه‌های عربی از
وقوع چندین انفجار در عربستان سعودی
خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/450770" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450769">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
برخی منابع از وقوع انفجار در پایگاه‌های آمریکایی اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/450769" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450765">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6QNIoL_qS3d1gin-efmWjqYreAjVJFQJRIqBdGVHjC4nPZjS5GhHA8QNnHbtLSNzJ7ld9p52Ju-X73RJiItg148dsHLDVivmON4knvlDifuN4hpojapQZl-WjAeO2N9xkNIum_C9Jo3WHVonq6PZ9LuZFumiikjABxQm5uY4rmSH2TZLS05CB8PRsA58kNH9TRKo-b64eA7AG54p5Pa7HXQzLk8cEUTg1TI7vnR7OD8LcK-7Fd_JgwW6SJCcVl9viONbyHDqsz8Hqqr3hiJxEEA5OIFQ3wRxaf37Sqtxnc9HkwdMlGQv3O0iKZ3fCCPnZlYRaGClrTjXB-OpDsHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GS3e4n5LjFo5zzH960u7jGgwz6lfk86_QPF7MsE9iYgJt1487u9mEh8vb28DbPL4mKPEFjG2ZRR4J751ThEj6xKBUgOnfBDwbfWDG1KHigcFlOkvO1jrvRfMAGOaMWh5QSMehkRc5HYmGxS1mYrHC-LIz4BcGl1kfqsUwL8DWDvK8pQTdiF5TX0kTMo0fbo89u-WmhoMz1ergBzzbYL167QLc-Cfn9qguC7p4NDMFnaxNt35fED5uCpTG7wtMh4A5N7w5A8B9QsaHLAZNLPQQuZRkOIkuysFN6fkeVB8n6Xc3Z52eXFQfZYXg6cv1BWAMRjkmjcb4kn_2YY4tvTquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbJITzmxRvzqR1HtmQ31nVk550gO6M6E6ZFLK_u6hboGdtb3jbfQXN067AW_EDR23acGxn4gNLshgTIKT-UnzbuSNo4rJLY-4h0R7qF2Fclk5152EB_izGWCdp240B9IXEDw_a6POsID2zz9RTl3Z-SReOvpoAU-4ayBnxn6Rn_hOzMTJQ0yg3NtNLCHfGC01TPb3xDOXT8FP3L561jeQKdD1UrgugCcd46QaE67YbBOYi5QJkIaetn4F6uaiDshNSnVJJ58gY7NuYSNjpS8z3nF1TGVZpYVnK7ajXIiyeJinpgTCDtkROb7PER0nVeBwNeA4fL15J3ToRbm34HDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-w0nZL3e70aasuRVU5a7cu_D3kGnL2jY1_ASftKHvSIxoquUx2HDezEQOaaO3cPv3xCiVVK6wmOFIuMiqAkafByi7uHtemT7sDaJ61Dg-OJThltn6X9m_-XjZBBQYGaxDN9E1UHni130Je_HvaK4CXmIpimGBfSRNGc0hsGABsjHAjqsiJfPkP7BWUfXkMnbJcJ09f1LbPhAVNRNAtPblJzY83MTzS4CWAzz_PoaaD7lPKwq7xc6mQb-IaShBvyOj8ea-aVsuNVUUXmH0wY0xKY6pH1X51yDohSDTyn_DbdbBDn8dqHy6MQ6cqIkL1I30UTFbRAFGmTGihU2JXfZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۷ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/450765" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzUkdG2PpF5OYJ1eYbUGyRaUHLvQtfTpXhRb_10a8atlYeNjWps-1bWkVBhL62Mix6IECQ6VZVR57tnq_r-z-VzUOlpdjfziwQlwB1Bqu8LvJJ-e-tMXwlOQCOeexqy_p7fyjExIZav1DWKcNrwt9FWDcFGQwOQW64o-Lh_c41hBJ8WZ2_2Z4Jq_DXQyHkYxBF-le6Zxqtl92EIn42vD26_vVZBLYBATVDbLzi5UtCl-ZVCp_pZG7C7kGDBAEZKVhCrY1xHu1kId8ZST6i5itLhTkNSUqL0s6zcfaa0JSyPQ9g3V0ikj-JVxKG0AH9wN4VtOET-1wFBa4r6dJ1sivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ylE_H9kbtqskpbLVihMt9Z42BLFPYuHsIJ0PJydr6FJEwAfVnTyEdGr5E7zZZucoT5zhf3ExfDDd4aWXlfpbEYHSYshnUoM-IA2Fr2VusRa6wZjIoTCOWcCrc8bXA4nCUWErv1ocyHJvDuQCuUnd-nyV_htFuTuwe2GvrdG2QiZAgDdA036__tYpOQ5y5ubJ4phx7-RHMY4-P4CimRVkDrZDx58ynYMESlKMCuZRCc_6cavZ0JzzfBoSAfZe7V5qKfJOOhkObDDxgWlc4Pw0t14OJY1kBGXa0-gQBQS7wMDmBwzMpsWcFXSlGxJckRMcSk9LnSnngUsC_2vwr88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nE43XmQXhPWHOX8YeDf30ZrFtJWdKBRIwiZc5-pdxzPqoAX03aQw39FcXLlF7gDLR04gsszLpiiT9Xjk6KMAMtx1-_FArIZDOFkkP1pv4j7chkfuil0Bv12iVS6Cw4Vs5pYvns0m-jYmXIIdTUWxCFpHbp6Nu1Uug44cLKixyZhM9onlgg6D37zyR2H99RdktHSdd4Ldv7g-u2LsWrj8jxvyo3vGNxjvuBdwHXHn-3Wy3yMVbqaLPaVk5JBP4zdgCppVU5K6Tt0afQh07_6VMxDMWz-CVrxkDmghAL63begi05QBmJQXGTNawT490ufLWPwlMquqhyExveBf9pm5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf2zSil8UxErE_vksbyn9y0OmLIyj-X14t7vABXW4euiFSrPXMr7cKFj6pWCvLmfqBPhMGtG3Ff2wYWf16eq7hf3HKli0QH0_hNQspE5WqrZIuT7CgbakuGD-r94XY2ZVH_m7o66j8zIZaLMptFtPjL1GGbt5FrQZS9YUbjrFpo2qWSJB4RF53SVWMuTlM3efSJmml0huohE7ooYvbXPAqIOPt1MBo1w5H3bWRs7hl5f59EYpu2Oe89XqSjGYXE_DUMlw4u27YQ0wYBQPt6kPJUGZ94SyfQwT_thE0WhRGxr3sTy18pY5jc9_NblPYNkMA9ystag7Y9M_1MKHZX95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNp9GrycFHLfjhUqgc9kb0gOymD3hvAFjSRiN0G0OojsMoe0wVBIAYvj5xumHATteQW1zOR2QDzKcLK4J5DWd87jMClbvUbByXpN-35kuPykYHBS_b3r4oDZkMblygVN-cnxUidwCUPl05jAhDOTj_oNNSnwaZdgWoW-SA44PnvcmKrdAt63L90820-nLXAsTS8Cq98i0P9pxk3LWKS6TWXIvgK35YZ3plDqZttGw5jxYl1KI8NNKEyKIBbszF45-5ESTXwoMude8_GM2p0gGhug8piGe7tqpK1jtboa7HPxAfWIKNcvaHLnjqCFAqboNkSSVrQAFTevhKEbd5ZHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsx5h-lUiPolnYigo13vhPtgDFJDpY1VZrOHF_YPTqOuDTvODVzWW0tPA-6dkecjecPXOWadNWlhrIkzHmNXkSfjSj5rxSVI0tQdZ5LomuBNh3KYjNtqE5K2nQkRQJuDFnSneRR71YZVjUxKy2ex_eJXIezvpp3zjNXlihTFPfoY3twf_DtmAuel1YQ1Seh-Zb9WKR7mbGkW4MUcNXk1Abgqh8p7AfQI4dNDAqtVGiprRJFapJrFIW5ie3sIHCF4Vce2Ea3NVUXozNTCmOVUtyt6Ecjw6jZsKYMjNUvEidXVNM5C0SfHW7_ff4NunQHMlX-lrGd2iZ3TXqUm6OhorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vd4_XzjamMaUEhzsru5eodtwYSIvj7JpJVzdpH0CMJkgrSkfXsYnGfsSbRrhvQSRKzZuGPtB7JsSUbzUA4xlObbpP2RrMHtopBmgL-0EAp_upME9Lacmaat4oVybYeOtbxBBNnaGe3o-mToetgwExme2TOM-qhKM3FBSuXFX4YCwWAN_OLVQ83s-gVNUyGJj3wD_QM0dYQvFR7L_MDwo10GgZcUf0CIfyWwZTRK5aI_MdymyinXLsfcdouG2WXV8-xx0_hAyh28stz7dR6T2sXQl0D--SB6CefIqijbNcBTbW5VO-CBUslNH4-unPL9LzgZT1gTERkEYQohdVLzDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQrfMhdVKZTtd7eVWzsY5ssDzdMoc3_WiK6rtNLX8EbaRBk-b4K5ZSZpIOEzlsjnjV-fGICwYWt-MxYRy0zAR-Hn0xkrTx-n30dQPmnVMhLbVYDzsn4hv8m0f-LqQ6_h8D7EDVyYAb72zqLQmRZexZ5VqDURkTAzHamJHed1VQFVReEuE_JWjrAevaN1yQxeIBVBmYapHKhsN-d2HcqrAonoRkBiCw4ZJqaYua6EpF_l0khIcJpbe7lR618J1pFIlowLGrd1Ap1TYdTqnDQOy1y84kGYSELjjaMIpD--RRSAd54VraIjbrhg2xWROoqHDdr6_WGR_IRKW9ZKn3jlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy-0wMkPiyMURMgP2abBf_6B4NikMlMadn1qWtWmeeygRcWDuzpNyu4hY_Z50sJrqc0MaU-DirfANXEOl1-oY5s4l7M10aJk-l5QrK-L-1VOncuzxhCsDTvTMo22urMkcWuCguLPFmjsOOFvCATRhtC1K1_pUA5dQFzW24g7La8TrPFfmyuBKNFIdDh4EEiaosGf43tv6nIH4Jb7tpQzv_aklUK2tIHSRBEqNEnEuvpdNpnRf_vC24gS8EVnGxcIfvLQDbQo1hECuHgnN3-GYmYclsQycKo-HhjdO3y6gPVeVYYwEnNWwCryofjgLNYTN2OEqKsDDIqhViDFJ38Sgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450756" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
