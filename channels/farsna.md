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
<img src="https://cdn4.telesco.pe/file/eII8z0bwA8bBVUD34swM21dNMax7ssuvKq5jcKkAROwb9A3JpiJMILiGSlOdQwlcFxdgVxN1ZgP6W9oDQrwA8oA1fHhtQtjgBphbCb6GR4KTfQCwxxC2ztOHf7FWshAE-V3yT_3huTSb3cHzSK-Jj9X6-6hJKRwlS2ktj4V_RpKLiwWRT4rPqhohbcVVdOxa9X9817-Ag5yVeAZSMxUZ2jg8oph7uiYa9jVWAqPbbbdTWSOv-_pa7aFFVcxvoiMli-x1FIK4X1a87PpcgzZ9W0bx01_c_aY22Xq9ZqSDdsLOD--oI6UDBJVPEzjhobjS3tLS4qIJ4Rl28a8mfxYIVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-460468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a99eb7647.mp4?token=vKltj5Au5v8Qo93TmjfAXkY-EM8nv1EmULTFI6FvDrTq6R2U69zqPoeX3P5VoCkGrVt6kTzmzjVvWtH5jIjW312ugr8gg-cQev1_ZdcALvgn4RUveACuw-jOUhnQTPpgp0ygHEL5FGzU9fhp0a7odldIUgfettk4E4dmtZt2P2UrcdHWVQMpc2cOae742ZIGrL1hvv32SnnWJaLDPHD5C_7ff4ByWG947QZhzMvWU9_FkcbHAIBSYnqxF4zRRrBOisYxVzMpLujxJFA3IvMiUFFeZAMLqjZ4OR10pnPIS3ZBhSCDEqeQ0xuJOcTjKKHGl9p47yq0_xEWPj0BJLAwlTkGtoTyoWXeldk8Wm5Ma8qb4t0kSd1v1WFqbdEfOx7VX1yIGLUlsyZt2gzghhj6f4oP_X6ibSqgiVuL2HRvuJsSYG6n4Rppfe5oo_915XkjjZSh4KWbHX-vcDnBhUOC72Kajvta1k3Rr8yG81lCAGacJL-93JoQOQPIacbcKrTpYhq9pJ9cL7TY9JvErhK_quUNnNMrbzvBzcGFjId7r2BNH-UCE2EsD8Mjhs__G4-T1-3Fnyqhc-QexWvFt3QRFHLHx5DawtTq_e2R41ch3cMINatEfLlYW_qHyB_dSNCNlecpsjsxZORQ42uhWLyF7jkYAKjWMctjB8mj6qT34a0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a99eb7647.mp4?token=vKltj5Au5v8Qo93TmjfAXkY-EM8nv1EmULTFI6FvDrTq6R2U69zqPoeX3P5VoCkGrVt6kTzmzjVvWtH5jIjW312ugr8gg-cQev1_ZdcALvgn4RUveACuw-jOUhnQTPpgp0ygHEL5FGzU9fhp0a7odldIUgfettk4E4dmtZt2P2UrcdHWVQMpc2cOae742ZIGrL1hvv32SnnWJaLDPHD5C_7ff4ByWG947QZhzMvWU9_FkcbHAIBSYnqxF4zRRrBOisYxVzMpLujxJFA3IvMiUFFeZAMLqjZ4OR10pnPIS3ZBhSCDEqeQ0xuJOcTjKKHGl9p47yq0_xEWPj0BJLAwlTkGtoTyoWXeldk8Wm5Ma8qb4t0kSd1v1WFqbdEfOx7VX1yIGLUlsyZt2gzghhj6f4oP_X6ibSqgiVuL2HRvuJsSYG6n4Rppfe5oo_915XkjjZSh4KWbHX-vcDnBhUOC72Kajvta1k3Rr8yG81lCAGacJL-93JoQOQPIacbcKrTpYhq9pJ9cL7TY9JvErhK_quUNnNMrbzvBzcGFjId7r2BNH-UCE2EsD8Mjhs__G4-T1-3Fnyqhc-QexWvFt3QRFHLHx5DawtTq_e2R41ch3cMINatEfLlYW_qHyB_dSNCNlecpsjsxZORQ42uhWLyF7jkYAKjWMctjB8mj6qT34a0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستم داغون شده، چون محکم زدم توی سر شوهرم!
آشفتگی روانی و درگیری شدید در بین ضدانقلاب به روایت خودشان:
فاتحه ما خونده است، دیگه به شاهزاده اعتماد نداریم، سلطنت‌طلب‌ها دارن ریزش میکنند، زندگی ما داره تباه میشه، این درگیری‌ها به‌خاطر نبود سیاست و مدیریت در رضا پهلویه
@Fars_plus</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/farsna/460468" target="_blank">📅 16:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phLBmOmYiDt0cQ6oYYA_XEp7zv3NotdgnVyAVUpahLqgl5apAnOFiUrbUHIlQk_T_rLMA_z0EXV8JfoasOeYXkXHT8KRMr-pGILtChciAI-2__6ygsarLZ3jjbrVL7VKKspgmI1B9giX3A1B-nnp8IoQ_AXink2ijRm2eLMwD1FXWm8P3IX_Pk47Dyd9XxyaVK3CAe8fe4xeqwnHz6xctISYJZTjdj8d6A3eKj0XPKqdmrXMQ7w6RVcIPnsKr0TVbsm1LwtH2yBpaBNoLmha8S4PuRkdHZXowGmsXi7oDExYxEZMRpRhKmyZdAENXwQvKEQCa-gw1BZQ2AlRzhhFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری تیم مسلح ضدانقلاب در استان فارس
🔹
طی اقدامات سازمان اطلاعات سپاه استان فارس یک شبکۀ هشت نفره از عناصر وابسته به گروهک‌های ضدانقلاب شناسایی و دستگیر شدند.
🔹
این عناصر با هدایت جریان تروریستی سلطنت‌طلبی و بصورت محله‌محور، اقدام به تهیه سلاح و برنامه‌ریزی برای کشته‌سازی در اعتراضات احتمالی نمودند.
🔹
این افراد در اغتشاشات دی ماه ۱۴۰۴ نیز با حضور فعال، اقداماتی نظیر حمله به اماکن به‌وسیلۀ کوکتل‌مولوتوف، آتش زدن لاستیک، انسداد معابر و تخریب اموال عمومی را در دستور کار خود داشتند.
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/460467" target="_blank">📅 16:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460466">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phm8z5ZNvGFqR0eNfW2aaweebBAuO5jgGFQG0RVyPQdrBTVSr1-G-11_75Sce0Cqc3y6kchRPIzOwJI1TupExQXRDkijtwcAdka84wt7Zutpq18NSobFD4Pk92h6xXJo_rQjKdv54-KCwsWhbj1f356AP6la8Mbkty6osYcUz5uh8tK1hxxrXwGb6edHdTnPKKewrwgbnDq5MBkCmDyn5axdWs5MFoRPBg-wOvLQHRt1-XlxgzieEDgLpaRCyREfZDvGAWxGE0KyQf2EsNIeuNcywzhawzd8TN6ESP7JGkUNdRE9bE9ZuffCSIlEu0Iw1zTlU1L4xBeMxwqEhAAalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی پرسپولیس: بازیکنان می‌دانند غفلت کنند، نفر جایگزین آماده است
⚽️
بازی با ذوب آهن برای ما مهم‌تر از دربی است. از فیروز کریمی خیلی چیزها یاد گرفته‌ام ولی چون استقلالی است الان نمی‌توانم مشورتی از او بگیرم.
⚽️
چون امتیاز هفتۀ قبل را کامل نگرفته‌ایم محکوم هستیم بازی فردا را ببریم.
@Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/460466" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460465">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCTFcYQSvIQv5Uu71znSHfUB5GHbvt2JNuuaS8ZIejZpluN7YaN2YJcr1DAsj_5PH154Mce2s2nyPjiKFlsVO5dbMbmTyjVQrH1_T7aQyJ75sfQDrsNYqfTRwRozFf6CY5MlcA5cg6Z-1-5HZzqu4L4uhqwNA4Vq9OdiROjbwxZYp7SEKvtF6d7HQk4Es7vVsmx2EVRgiIexHsI53jFS7CnwzF0xdz-Ke8sVH7NFv4bLJEYIKiG8f9TSX6xKhY2OhMH-B2ARXdQx5sLx0UPBlivnpv4LFI63h0gbxKNB6X_kB5xqjF9rE60-y8natQDvrlqdFTSExHdxA6lVwB43oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا ایران، آمریکا را تحریم اولیه و ثانویه می‌کند
🔹
ایران با قراردادن ۵۶ نفتکش متخلف در فهرست ممنوعه و هشدار تحریم همکاران آن‌ها، تسلط خود بر تنگهٔ هرمز را تثبیت کرد.
🔸
این اقدام با رکوردشکنی قیمت گازوئیل در آمریکا، سقوط ۹۰ درصدی صادرات گاز قطر، کاهش صادرات…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/460465" target="_blank">📅 15:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460464">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e03c17e53.mp4?token=HMgvtO88Wzs74u8I6LYkT8qXbd_60lhYsEwfoJSgY0s9yOu2VyT7wc7K2PofR7GSRqRVpLeHxFgnrYc5shgsD0dp2aJxaoc_J3CaasF-iIX19bgGeymisEC5f8-GwqkGezX-BESmyaEr0bOexP9Du6ZEPHouJNvxj79JOiUFKx6RDN18PE7WNDYQ-1fgjxlUxooBODoQ7SJyOW1W3yuVIelf9vQbf3m7cYEyPZo4FJRml6wKJC3r_fEBoicyDZou191I-EPGm5pO8ILHCtGRinQ_y1NeweZLVXif1F3LBZuqMCAeq0fmdNpyQ-dXD7qbYaBjSoimDMpcNHqsY7f8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e03c17e53.mp4?token=HMgvtO88Wzs74u8I6LYkT8qXbd_60lhYsEwfoJSgY0s9yOu2VyT7wc7K2PofR7GSRqRVpLeHxFgnrYc5shgsD0dp2aJxaoc_J3CaasF-iIX19bgGeymisEC5f8-GwqkGezX-BESmyaEr0bOexP9Du6ZEPHouJNvxj79JOiUFKx6RDN18PE7WNDYQ-1fgjxlUxooBODoQ7SJyOW1W3yuVIelf9vQbf3m7cYEyPZo4FJRml6wKJC3r_fEBoicyDZou191I-EPGm5pO8ILHCtGRinQ_y1NeweZLVXif1F3LBZuqMCAeq0fmdNpyQ-dXD7qbYaBjSoimDMpcNHqsY7f8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال‌های ارتش آمریکا در آزمایش دروغ‌سنجی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/460464" target="_blank">📅 15:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460463">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPToJ7tE5wF0QCP-q59I0gbfeT7LQ1HyiMtAQDKBr65w7ymzyxYcUy-MIuFKmk37k_geZCi7OBJk17UqJT8EZrBPHcFldjF28bbooXgfYCSddNMZfAIXHHwquCCJ_KH-yZq1jb1Z2tPCyTWJ8XkC9vZQ6Hbr69-HurFionR5WqsUlhGhWy7mVLwCBSZhPy6Ly0Bf9RXJnCDnC8SHCY1Ufob7BcD0TtQsz4NKcUrqtAzpMSw1kQ-TeGsmgnVebngwn0LTirpvdhTkAz8Q_FWOqIaWTs1jH1OP3UXJVKukH3adXFtj5XbnSKMY36QgdxKq4W4MbzyZMQBOeaaDJUDvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سهم بانک‌ کشاورزی از تامین‌ مالی بخش‌ کشاورزی، به ۶۵ درصد رسید
🔻
بانک کشاورزی در سال ۱۴۰۴ به تنهایی حدود ۶۵ درصد از کل تسهیلات نظام بانکی به بخش کشاورزی را پرداخت کرده؛ این رشد عملکردی حاصل تلاش این بانک برای تقویت زیرساخت های امنیت غذایی، تداوم تولید کالای اساسی، ثبات بازار و پایداری سفره هموطنان است.
🔻
درحالی که کل تامین مالی بخش کشاورزی توسط شبکه بانکی درسال ۱۴۰۴با ۴۰درصد رشد نسبت به سال ۱۴۰۳حدود ۴۵۰۵ هزار میلیارد ریال بوده است، بانک کشاورزی با پرداخت ۲۹۱۰ هزار میلیارد ریال تسهیلات به بخش کشاورزی، افزایش ۵۱ درصدی را از لحاظ مبالغ پرداختی در مقطع مشابه ثبت کرده است.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/460463" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460462">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsUHpsz5cOvUVFDyDsUNdQ7AKCvxfCgZyRoICDfT5VLokWZ2w3zDznSxj5RO9Lr7E7ps-0-YpXN_6XGH-qGUL0NRQCWXGtV-bdWX0YD2mfyEJgcvkItDgdvvUH5pp3IFa6KvREldDmYQV7gDWCIsQe8NuqUjPW9_GZPZj1SXVi4JC0cUYw91dcYueZHsvHmyxgm2jtwjbMWAAM8YILRbwII2Cr1dKQxcEGsDXjWL-fvt9ok-KQ1REREetXS5KeeKFvMKEjmaP1_srsxZIrocYJR-CzDjdFFjYx9Vfgpu7r9nBdDILySp-5MMEIrNXdEoaLQaMW6M7iLkQEkGFzso4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
سامانه فرارفاه بانک رفاه کارگران به‌روزرسانی شد
🔹️
با هدف توسعه بانکداری الکترونیک برای ارائه خدمات مطلوب و متمایز به مشتریان، سامانه «فرارفاه» (مبتنی بر سیستم‌ عامل‌های Android، iOS و PWA) بانک رفاه کارگران به‌روزرسانی شد.
🔹️
ثبت سفته رواق به ذینفع بانک رفاه کارگران، انتقال چک دیجیتال برای اشخاص حقوقی با تأیید امضاداران مجاز، انتخاب نزدیک‌ترین شعبه هنگام افتتاح حساب غیرحضوری و امکان انتخاب تعداد برگ‌های دسته‌چک از جمله قابلیت‌های نگارش 1.19.1 برای Android و iOS و نسخه 1.1.7 برای PWA است.
🔹️
در این به‌روزرسانی، مشتریان حقیقی می‌توانند درخواست دسته‌چک ۱۰، ۲۵، ۵۰، ۱۰۰ یا ۲۰۰ برگی ثبت کنند و اشخاص حقوقی نیز امکان انتخاب ۲۵، ۵۰، ۱۰۰ یا ۲۰۰ برگ را خواهند داشت. همچنین محدودیت‌های مربوط به صدور دسته‌چک مطابق ضوابط بانک مرکزی ج.ا.ا اعمال می‌شود.
🔹️
برای فعالیت‌های انجام‌شده در برنامه فرارفاه امتیاز در نظر گرفته شده و این امتیازها در نسخه‌های بعدی قابلیت انتقال به سایر مشتریان یا استفاده از مزایای دیگر را خواهند داشت.
🔹️
این سامانه در حال حاضر از طریق فروشگاه‌های اینترنتی رایج و همچنین پورتال اطلاع‌رسانی بانک رفاه کارگران به نشانی
www.refah-bank.ir
در دسترس مشتریان این بانک قرار دارد.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/460462" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460461">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/farsna/460461" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پشت‌پردهٔ رژه‌های تبلیغاتی منافقین چیست؟
🔹
پس‌از انتشار چند فیلم توسط منافقین در ماه‌های اخیر با عنوان «رژهٔ کانون‌های شورشی» یا «رژهٔ هواداران»، این پرسش مطرح شده که آیا منافقین در داخل کشور از شبکه‌ای گسترده از هسته‌های تروریستی و هواداران برخوردارند؟
🔹
بررسی پروندهٔ تعدادی از افراد بازداشت‌شده نشان می‌دهد که اکثریت آنها از ارتباط این اقدامات با منافقین اطلاعی نداشته و با الگویی مشخص فریب خورده و مورد سوءاستفاده قرار گرفته‌اند.
🔹
در مقابل، تنها تعداد انگشت‌‌شماری تحت تأثیر شگردهای جذب این گروهک، با آن همکاری کرده‌اند و اکنون باید به‌دلیل همکاری با یک گروهک تروریستی، که از جمله سنگین‌ترین جرایم محسوب می‌ شود، در برابر قانون پاسخگو بوده و در دادگاه محاکمه شوند.
اما الگوی این فریب چگونه است؟
🔹
سرپل‌ های منافقین با پوشش شرکت‌‌های تبلیغاتی یا بازرگانی، جوانان مستعد را از طریق فضای مجازی شناسایی می‌کنند؛ سپس با پیشنهاد و پرداخت مبالغ قابل‌توجه، از آنها می‌‌خواهند تعدادی جوان موتورسوار یا دارای خودرو را برای اجرای یک برنامهٔ تبلیغاتی گرد هم آورند.
🔹
در مرحلهٔ بعد نیز از سازمان‌‌دهنده می‌خواهند پرچم‌‌هایی با شعارهای مشخص تهیه کند؛ شعارهایی که ظاهراً نامی از منافقین ندارند، اما از میان عبارات و شعارهای شناخته‌شده این گروهک انتخاب شده‌اند.
🔹
پس‌از اجرای برنامه و ارسال فیلم برای سرپل، منافقین تصاویر را با عنوان «رژهٔ عناصر» یا «هواداران» منتشر می‌‌کنند تا یک اقدام تبلیغاتی طراحی‌‌شده را به‌‌عنوان نشانه‌‌ای از گستردگی و نفوذ داخلی خود بازنمایی کنند.
🖼
سؤال اصلی اینجاست: اگر منافقین واقعاً از شبکه‌‌ای گسترده و سازمان‌‌یافته در داخل کشور برخوردارند، چرا برای ساخت چنین تصاویری به فریب و پنهان‌‌کاری و استفاده از جوانانی نیاز دارند که اساساً از ارتباط این اقدامات با منافقین بی‌‌خبرند؟!
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/460460" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXmR9eV3ykqZfMKwwrLOJ4u-fdXwqcsGd0AFcRQ9FW7bWUYoD6lRM8UEsdHnP2ecO-z9WhHX15Dk5x2fWVGAvtHZJjp6PiHxF2yu1OW7X7ICSdO9Jp4w0F5ZsCzuPkTxa5DucQYZ9dm8xQAGfhvaSIV3ZFQCRPYvIFF8ehsyeiOW4y2y_p1IvMCA3OMvieO8IIIV_90AF1zI172cIZ7iL5co-WNRk80B0puMbPkIE1DvPTk3v6UfP9LCYBMltLAWWZuY5K65E9VoDz2oYpRw9rhCrZlOaCKpQZeaFFHhvYrJbr75kFl0a1yaMT8trfbtIbUz10v0c6wz0fo1gAt2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gxe1S94gkG9FSi_h9JBS8EvJMGhlI17elH0EHf_kI1V1wBmT8vYSshwTAKUZa6ttw8qw-cE-YNAKHhJdebMzVxgPYXepR-L6wWTCe1wiDqbClEmANgGmYBQ3ccizBduwHBQ7J-wm5FdVUK3HhS3glkIGlZB7XjimlG5ajLYU0-Io_Agd76SKI-LrnnpXYJioktTkHJdkh3UyDrQsY8T8dawS8nVq9cVnrAfEtRD0gb9DUEnkwAgO-deIyaEGTvqz491DmQDz74n9WTohSXTXXcAaAuv-Vntov7oqy8Q3T4tV3oBzQl7dnck0hGqvU-JP6LvZeA76nCtQuE98Zqd86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UF9WuS-eaR8_6yeWc8QlMHDqDawpV5Q0mAPgl2AY1IW5p7-42dKidabDTqxo99A-meFJA8vroMyjq4VkYPnfUf0xJAtECb6jrItP0e2-mKDhNIS0uWusqABXzBChT_pguLhRyX9NydKojf6m45ZJsGCcJoQw9i45gAC-THsq1w7Awj14HP_it0hSKQmwtEckcUWMG9uEPWwfL2_t_WbueLydQ9eAkjyHACqjO3aRMPq5fk12zU4aS6wdUeuaUFrs9SiND8bLnsoUN_Atb-N-35Yt0bhl8QDvJ2tOpC722-FkaOZmCYvPPkTdZiX1FLm8X3j5VgbhhzAQs9Q7dMXOiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXHC4DMFg9eKNrCc9MY_MVMznPrLUcmlRy8FsneM-R6DZkdISS0Gx84gd-ePhs56mf2s1wR7Uqh187nWbN3t4sV6xsFmsK-2B9JQ0eC1MdpTD4I5peVHoYtT620Rp3ttOACLrXaNrD5JGUnGKwa3QI6nk_53L5gsl08jUNQ07tr722oFQ-EoZvWkZYhvECxI41k1p3nviKcq70e0kUofHVGh1fXdtCfkYCOBZfNtdcS03drdqiaPRcNqudgidOoNk_PAEMZqCj_8VdgTbscUdBZYgLfOBqQD4eIVXy1C9OYEGzOBUbqnQWKbwQP68UvTytP_KaRtWKygdilXt1_-og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: تصمیم‌گیری‌ کارگروه‌ مدیریت مصرف سوخت به مردم اطلاع‌رسانی شود
🔹
ضرورت دارد آنچه در کارگروه‌های مختلف مدیریت مصرف سوخت تصمیم‌گیری می‌شود، به اطلاع آحاد جامعه رسانده شود و ابعاد مختلف آن برای مردم تبیین گردد.
🔹
می‌توانیم از ظرفیت اجتماعی پویش «جان‌فدا» نیز در راستای مدیریت مصرف سوخت استفاده کنیم.
🔹
تمام اقدامات و مراحل سیاست‌گذاری در حوزه مدیریت مصرف سوخت باید از پیوست رسانه‌ای دقیق و شفاف برخوردار باشد.
@Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/460456" target="_blank">📅 15:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89cd5fd076.mp4?token=QldtYV55QWzvz6KIW8_robJBY-hp9KkBHvf1kis6hnlp1zRMs-n2WcXOkCCd8JH3xmy9H_oy1Rb3CJM5JTmA3rKO2hMunrUDcRwLHTnMzD9x55Mbw4JkKobPP6KfJZWaY_3HoKxa_QSHNwJ22GadIdbipcsksrrlXF_1hOvbqWHlcOsn7Q21bOZmDI58dtmKTUIaGaYbUxm-rKhSR_BhMNLKy6TvQpy0A4qbXil5hL340Mz1IEBN0IH58KYHPrM1p3zue4fIkcypnjhHWjZdX1OCJJIoXEMoD8zmy524BoLAHJDajw_Al7vlciqL8yo9rmzJgVKqxH_NMfWg53xm9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89cd5fd076.mp4?token=QldtYV55QWzvz6KIW8_robJBY-hp9KkBHvf1kis6hnlp1zRMs-n2WcXOkCCd8JH3xmy9H_oy1Rb3CJM5JTmA3rKO2hMunrUDcRwLHTnMzD9x55Mbw4JkKobPP6KfJZWaY_3HoKxa_QSHNwJ22GadIdbipcsksrrlXF_1hOvbqWHlcOsn7Q21bOZmDI58dtmKTUIaGaYbUxm-rKhSR_BhMNLKy6TvQpy0A4qbXil5hL340Mz1IEBN0IH58KYHPrM1p3zue4fIkcypnjhHWjZdX1OCJJIoXEMoD8zmy524BoLAHJDajw_Al7vlciqL8yo9rmzJgVKqxH_NMfWg53xm9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنوب لبنان درحال‌حاضر در چه وضعیتی است
🔹
برخلاف برخی ادعاهای طرف‌های وابسته به رژیم صهیونیستی، تپهٔ علی‌الطاهر اشغال نشده است.
🔹
در ساعات گذشته نقشه‌ای منتشر شده مبنی‌بر اینکه ارتش رژيم پیشنهاد کرده است از مناطق مختلف جنوب لبنان به یک نوار اشغالی در طول خط مرزی با شمال فلسطین اشغالی عقب‌نشینی کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/460455" target="_blank">📅 15:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHlsQgJMRfgs11Ck7Z1bZK0LEvahhcnN3cl4fvSS8Gd5moNTbdeZmccYR-9doWG0BW_5vuCG-VsK8M1gWTAQT9igtpmmBLCM5KMdhy2WkDvW3ewG4v4cc6pxj5FPs4xeJnep8iPq2tbR3ySpsPbx2knGX6dKqL1XzOGNKIXJ9yMU054hDU1wSREWQgi3Zp6OTHaH53fGskWQu6c-hMA0jMGT0gVtZ1WxeQqycIvuHQxLKYH-o1_-ryb4GNpJHEgS-vYxXsx49eL8LMJf4VQow3540F0mjYt1VUYZO0AY3_LyRvhOhP-RpG_fK2sN_xJ17URfuR5VLHiMFCStTgQzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور ابلاغیه برای خداداد عزیزی
⚽️
با اعلام کمیتۀ انضباطی سرپرست تراکتور به‌دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف ۴۸ ساعت دفاعیات خود را ارسال کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/460454" target="_blank">📅 14:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450dcf8c32.mp4?token=GroQQBe4F70f7a-LA-6UdmIDNJJVckjEL8C_wsSByxbZXphosa_g_u8lyy8Mi90U6xwTQFNsqGFi4Q1AVHHN7YUgZnCYxDJnK3QGIXmngPMjMqQjx8LKzxRt5kxtOKe7W0DudaTjEnz4raxyrsDXWbkalzNA-MfIFMzlLmtfh3apauIu2K0jrCvII5SqnVIWsatVZ1bIQbMEb4uu7RSvLniL4be6roUvDAoDXmIBVvRpJmhO4zFswo4lJ-W2L9Jw_aS2cXyjhmzZtCa3R6_6A7A22dcfAyQakhC-tDfd-TSlpoP_Ne9M-KZqWrR8g2JtzfnlOhY8o_FUrTJWUTAcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450dcf8c32.mp4?token=GroQQBe4F70f7a-LA-6UdmIDNJJVckjEL8C_wsSByxbZXphosa_g_u8lyy8Mi90U6xwTQFNsqGFi4Q1AVHHN7YUgZnCYxDJnK3QGIXmngPMjMqQjx8LKzxRt5kxtOKe7W0DudaTjEnz4raxyrsDXWbkalzNA-MfIFMzlLmtfh3apauIu2K0jrCvII5SqnVIWsatVZ1bIQbMEb4uu7RSvLniL4be6roUvDAoDXmIBVvRpJmhO4zFswo4lJ-W2L9Jw_aS2cXyjhmzZtCa3R6_6A7A22dcfAyQakhC-tDfd-TSlpoP_Ne9M-KZqWrR8g2JtzfnlOhY8o_FUrTJWUTAcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامهٔ عبری معاریو: شمارش معکوس برای فروپاشی اسرائیل آغاز شده است
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/460453" target="_blank">📅 14:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f2cbd25a.mp4?token=mtdj6hkoP_cfqNSRctLtJvkk8fLasJtw521oK5YumjPPI-QVBAxzkch6tryO0aUz47RXsJMSrOWs3OrrYANIj1o-1sK4W3yatNkGSNENezkVlF8ABVQpPyRFnT1sw6zEiECOBVMh3gtIvEQaPuFWzHp1rWbGgRvwHIDQ_xLm8pdqYSdFbwPLhXzHFDZQAbxGbHBwKb064DH_etaOu8CZaQFU8w7XDSl89IkoBpkE2QwX5m5fLkq_-6Y0bJSbWP6R2PzWOa2KlJPcIMYp63XLUY3BrgBIDXxF0zK3U8XiAtLQjSGP8weQilZXp4AwEM5iOZuprfOrqq27cI0-WCx6dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f2cbd25a.mp4?token=mtdj6hkoP_cfqNSRctLtJvkk8fLasJtw521oK5YumjPPI-QVBAxzkch6tryO0aUz47RXsJMSrOWs3OrrYANIj1o-1sK4W3yatNkGSNENezkVlF8ABVQpPyRFnT1sw6zEiECOBVMh3gtIvEQaPuFWzHp1rWbGgRvwHIDQ_xLm8pdqYSdFbwPLhXzHFDZQAbxGbHBwKb064DH_etaOu8CZaQFU8w7XDSl89IkoBpkE2QwX5m5fLkq_-6Y0bJSbWP6R2PzWOa2KlJPcIMYp63XLUY3BrgBIDXxF0zK3U8XiAtLQjSGP8weQilZXp4AwEM5iOZuprfOrqq27cI0-WCx6dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: حقوق و تجارت مردم نباید تحت‌تاثیر طرح مقابله با نفوذ قرار گیرد
🔹
در نشست امروز مجلس، طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور بررسی شد و ماده ۷ و ۸ این طرح به‌دلیل وجود برخی ابهامات به کمیسیون امنیت ملی و سیاست خارجی…</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/460452" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164ee20272.mp4?token=fITjk-6Pa7tA0HWCeJ8HBORUwX49xSlt6KwcQAUOzz9AcpuWdNjYnVmh-5HPf9ytOx1AxvULXqMfMlJSib-vJutswIEgZDIpDS1mhj3zkpnadkj-kQQbGuSv4nRbN0RYEGyI0IXYTa15dmy-pymqbfXc7WtA-uqh-fnB4YRaJ_rfnZj9LX1QO3LGaektb1ohEKiH15859j70FOw_0nt5HJja5Ut3y9lOFjm5yijXs3v80v4GAf-2Lqr1j57lfAgawveqRmPfl__-DtmtnJpQnb9OPfJNFqr7H-IJ-_5V8qBhZeKCcxCenMg4mT47-naih8BIJ5lviryfyeI3DeKOFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164ee20272.mp4?token=fITjk-6Pa7tA0HWCeJ8HBORUwX49xSlt6KwcQAUOzz9AcpuWdNjYnVmh-5HPf9ytOx1AxvULXqMfMlJSib-vJutswIEgZDIpDS1mhj3zkpnadkj-kQQbGuSv4nRbN0RYEGyI0IXYTa15dmy-pymqbfXc7WtA-uqh-fnB4YRaJ_rfnZj9LX1QO3LGaektb1ohEKiH15859j70FOw_0nt5HJja5Ut3y9lOFjm5yijXs3v80v4GAf-2Lqr1j57lfAgawveqRmPfl__-DtmtnJpQnb9OPfJNFqr7H-IJ-_5V8qBhZeKCcxCenMg4mT47-naih8BIJ5lviryfyeI3DeKOFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۹ جایگاه سی‌ان‌جی جدید افتتاح شد
🔹
مدیر طرح سی‌ان‌جی شرکت ملی پخش فرآورده‌های نفتی: به‌ازای هر ۱۶۰۰ خودرو یک جایگاه CNG در کشور وجود دارد؛ درحال‌حاضر ظرفیت توزیع CNG کشور بیش‌از ۴۰ میلیون لیتر مترمکعب در روز است.
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/460451" target="_blank">📅 14:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb5fc4cfa.mp4?token=Q71d99wmS7RAG2V_xJY5456eIY_lFAIVwJFH0-XypVQg72PAAuzzeIeIMjctyxEBqZ9SwpOCPGtpdf9mc0zpE-vhBxcF9zmW0UE_hCX8vGHgklLBRMUtjU1JovEIW0hu_viVJyxnNXtRtXahTxRaQXQ8bsB3I0WcVZqVtGBME_D1OIRiDxb5uPu_LuU2dSO2_szHCx0CiNF3_mPyT9ey4A7gIWumVlUDFk29rDksHLQ-nqaYTa-yTGwVVWeeRFUyFBOWz4udGNN-1kozyIIvz4U4r-Tvrgp-HrKTEa8aRUmas2vW0z5bVgO5TA0Jia921iAdA_yticBpaf63HZhlfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb5fc4cfa.mp4?token=Q71d99wmS7RAG2V_xJY5456eIY_lFAIVwJFH0-XypVQg72PAAuzzeIeIMjctyxEBqZ9SwpOCPGtpdf9mc0zpE-vhBxcF9zmW0UE_hCX8vGHgklLBRMUtjU1JovEIW0hu_viVJyxnNXtRtXahTxRaQXQ8bsB3I0WcVZqVtGBME_D1OIRiDxb5uPu_LuU2dSO2_szHCx0CiNF3_mPyT9ey4A7gIWumVlUDFk29rDksHLQ-nqaYTa-yTGwVVWeeRFUyFBOWz4udGNN-1kozyIIvz4U4r-Tvrgp-HrKTEa8aRUmas2vW0z5bVgO5TA0Jia921iAdA_yticBpaf63HZhlfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ نمایندۀ مشهد: قالیباف ادعای عارف دربارۀ طرح نفوذ را رد کرد
🔹
نخعی‌راد، نمایندۀ مردم مشهد در مجلس: «نیکزاد، نایب‌رئیس مجلس اعلام کرد ادعای معاون اول رئیس‌جمهور مبنی‌بر اینکه رئیس مجلس با خارج‌کردن طرح مقابله با نفوذ بیگانگان از دستور کار موافقت کرده‌، خلاف…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/460450" target="_blank">📅 14:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVi8kI0SwCktkDudjMe0KMTGwgW0O-vii22raQYSIrm_yzSlYruEaswuMxaxU51d0GMeoadb4bLHbJhxduS-sQngp9ZdiS_FiVSWF_1cHuIpDNSHPUSmTclxMJfhu7t2Ok4x-zZf-S7qpCV7R12p9PSzhmZSfKX0FpHXrFqTX3jRblFjL6PXaDBRldPBhAYnQU00gpdxExg4GrTU9R5QoAWpeu6v5VvVgHKUUhhq7w1aOKo1JC-xn8mX_a8a3V22J1m9EUCdyy_FVk_ZQrDa1d7F-DsQ2HT9Tld4nt6_JDR9rSurCskRBR4OFS4bwvYFWpDPDA1sszHx08qfPR9c_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: آمریکایی‌ها از ۸۰ سال پیش تا الان فقط از ایران نه شنیدند
🔹
رئیس ستادکل نیروهای مسلح و فرمانده قرارگاه خاتم‌الانبیا: آمریکایی‌ها بیش از ۸۰ سال است که از هیچ کشوری جواب منفی نشنیده‌اند و انتظار و تصور غلط آن‌ها پیش از تجاوز به ایران هم تسلیم این ملت بزرگ بود؛ خیالی باطل که هرگز محقق نخواهد شد.
🔹
دشمن تلاش می‌کنند خلأها و شکست‌های راهبردی خود را با جنگ نرم، شناختی و فشار اقتصادی جبران کنند، اما در این عرصه نیز قطعا کاری از پیش نخواهند برد و شکست دیگری را بر کارنامه خفت‌بار خود در جنگ نظامی علیه ایران اضافه خواهند کرد.
🔹
جمهوری اسلامی ایران به‌دلیل اعتقاد راسخ به ارزش‌های الهی و ملی، الگوی جدیدی از مقاومت را به جهانیان ارائه کرده است.
🔹
دنیای آینده با دنیای گذشته متفاوت خواهد بود؛ تفاوتی که به نفع ملت ایران و همراه با افول قطعی قدرت آمریکا رقم خواهد خورد.
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/460449" target="_blank">📅 14:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f84cc0c8.mp4?token=spsETta4QwizB6GjvYhgGU45K31wLXybzpYw4oda-1Vrb47EsBxNPWj3QiFQJsMM2sLs4iiEB6zoIyDb4HvoyNKSGqWg8WymeydsCQTeDp9PenYFuC77fq6SxcWouzUw6MQo2sSWqRLc6kbreD24Mq4PVSHET6u7ld1XJe9F0N7OxCm64IIRZhDYRmZbsnfpFkyFuedeyr6UusCUOcpW_v-TySe_zQWjGdW5ELI3WGjekenTEqNddLpSKN7bTimsyL-GtsODiiCSCL7Zb_gKrfLpnpFPoZOFmXhRxvnEwvy-iIqsY0L9sx7rEl72KW1CnHi04X3WnpZrhAoeko7RtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f84cc0c8.mp4?token=spsETta4QwizB6GjvYhgGU45K31wLXybzpYw4oda-1Vrb47EsBxNPWj3QiFQJsMM2sLs4iiEB6zoIyDb4HvoyNKSGqWg8WymeydsCQTeDp9PenYFuC77fq6SxcWouzUw6MQo2sSWqRLc6kbreD24Mq4PVSHET6u7ld1XJe9F0N7OxCm64IIRZhDYRmZbsnfpFkyFuedeyr6UusCUOcpW_v-TySe_zQWjGdW5ELI3WGjekenTEqNddLpSKN7bTimsyL-GtsODiiCSCL7Zb_gKrfLpnpFPoZOFmXhRxvnEwvy-iIqsY0L9sx7rEl72KW1CnHi04X3WnpZrhAoeko7RtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: همراهی‌نکردن کشورها با دشمنان ایران باعث شده تا تولید و تجارت در کشور ادامه یابد.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/460448" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08343fb206.mp4?token=Z2PmJwfndZNO-rIfIBC-WPzfzcVC76_Fh-qMKBlQ7OODynHL2selsUg23ONl-hDwUlJMVmc78PfZjJTFOl4nJw6xpQYq20lHFveG25ru9220xg8j-6UR5EDVkNYVSZDCoIy5EKGlLeWKy3WpjzAGIMymY5FUw0KxKHCXlbQdpe-UntEYLuWICWR4pIyh-38y_1F-Djr8eGyoPMbNBFqyAGW0H4T0XwYURJTzUdUSOH9YjbcR7LCRhSAMAuyn8QFBHsxs8kcNzyVEHGvDY_2Ud3wCpKkwEPiziH4VsHOrhIPdMSsofqjcq-W5FutPso9IikCFrviOg_HE0u6bksUPew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08343fb206.mp4?token=Z2PmJwfndZNO-rIfIBC-WPzfzcVC76_Fh-qMKBlQ7OODynHL2selsUg23ONl-hDwUlJMVmc78PfZjJTFOl4nJw6xpQYq20lHFveG25ru9220xg8j-6UR5EDVkNYVSZDCoIy5EKGlLeWKy3WpjzAGIMymY5FUw0KxKHCXlbQdpe-UntEYLuWICWR4pIyh-38y_1F-Djr8eGyoPMbNBFqyAGW0H4T0XwYURJTzUdUSOH9YjbcR7LCRhSAMAuyn8QFBHsxs8kcNzyVEHGvDY_2Ud3wCpKkwEPiziH4VsHOrhIPdMSsofqjcq-W5FutPso9IikCFrviOg_HE0u6bksUPew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: امروز بیش از هر زمان دیگری به عدالتی نیاز داریم که گزینشی نباشد و حقوق ملت‌ها را براساس میزان قدرت آنان اندازه‌گیری نکند.  @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/460447" target="_blank">📅 14:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460446">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0PojgHC6oW0-GfGgIUNYZSozaOeXvVvKCXqJkQNy1L7hEfVzbEw-_T22tAOOq325_iVHdFXdlxHuQxtQirvj7ISPDi1geBX5t787dVlI95cA77g0d2ne1hwnD_wENyMzTlleqt3qCm8uSswnMQDWYHkzhK9MKIyYCu98AbJrjI7FhveDp8lA_ZoHns1_7P_ttsqf5MCTqJ3wk7IruchMwJllnW72JKeTIkROYn-RZ0Gzzv42TVoD2JQW8y1JFBWGf4T3AeMKn_H7zh9s7nUf-M0uPEkE1__9gbJBG5rabpt1Z3sk4XyZhfE1Lk8RsK5TdvO077syvKLJd3_39XkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آهنگ: اظهار عجز برخی سیاسیون عامل جنگ ۴۰ روزه شد
🔹
مدیر گروه اقتصاد بین‌الملل مرکز پژوهش‌های مجلس: نمی‌توان مقاومت و تلاش ایران برای حفظ استقلال در منطقه‌ای که همواره محل رقابت قدرت‌های بزرگ بوده را رفتاری غیرعقلانی تلقی کرد.
🔹
جریان ساده‌ساز تصور می‌کند همین ابزارهای قدرت ایران باعث ایجاد درگیری و در نهایت جنگ شده‌اند؛ درحالی‌که واقعیت چیز دیگری است.
🔹
آن چیزی که منجر به جنگ ۱۲ روزه و جنگ ۴۰ روزه شد، نه اظهار قدرت بلکه اظهار عجز بود.
🔹
پس‌از ترور سردار سلیمانی، این انگاره تقویت شد که ایران در برابر ضربه توان پاسخگویی مؤثر ندارد و تنها واکنش لفظی نشان می‌دهد.
🔹
در نهایت پس‌از این جریانات نتانیاهو توانست ترامپ را متقاعد کند که حتی با هدف‌قراردادن رهبران ایران نیز هزینهٔ قابل‌توجهی متوجه اسرائیل نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/460446" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460445">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J704HQ4jqZh4DTmgQjMWIvNm4M4HrIoXiod019F_R8sGjdiEWNpc9t5tieD2qExrP7RVhDkH38DiJqQ1eDclJw5e7i9NwvH8kvuPuBf9Pain2mf6S7G4-VdkDhZdG9lJOB3F6FTLkZYaz_hcT_lB_ysEfnJ_nvfNxF3peZ_DuwI_NOQgseTHh0EuNWf5KPQw1l2WdQqu7banNlEzE0vstPlyirNEcYYXuIs14mhTpNGecBN1uMkU0hv0ls87d5vSEnFZhMwcXMthjuPsimjqSQtHOxLmkzE_99rMm4arOztwHGx-SsEPNVtt78kVESCs_cf2DDLvdEGfj2ylS5F8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تناقض در اعلام پایان خاموشی‌ها؛ این استان فردا قطعی برق دارد!
🔹
وزیر نیرو اعلام کرد که خاموشی‌های برنامه‌ریزی‌شده دیگر در دستور کار نیست و از مردم خواسته بود در صورت مشاهده هرگونه قطعی برق، موضوع را از طریق سامانه ۱۲۱ گزارش کنند.
🔹
این اظهارات به معنای پایان…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/460445" target="_blank">📅 14:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0793651a.mp4?token=TpaIta0jtP0bMhaDEmtMkmu_IC-yIg0aE7xr-XHgf3ZDgXW6zpY6AJKAAak9063GuYB58zX3wSeqGYtAHipW_V_T4s4pDNhsQPbW87OR64N9AW67TjzK8OPKDaYq0xgek00H2uyXmcP4iFxbwnoW6r_Lx14n-7q7UDXas5y_F_5GZzVLFkrVDFqVmPlDXICiRgyyqgTNVXEReXay-YBOFH3nJwAYJcGXfy8fX7eHJO7aRV49Zur7-UKxilXjjWzB6wMEyEEyklzB53fgio9mlZs3xCWvlLOa-84RaZhmACPnLkmYKPBkYlTv9q0GiTSNGbkHcdpzCDejwG1dh0Y4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0793651a.mp4?token=TpaIta0jtP0bMhaDEmtMkmu_IC-yIg0aE7xr-XHgf3ZDgXW6zpY6AJKAAak9063GuYB58zX3wSeqGYtAHipW_V_T4s4pDNhsQPbW87OR64N9AW67TjzK8OPKDaYq0xgek00H2uyXmcP4iFxbwnoW6r_Lx14n-7q7UDXas5y_F_5GZzVLFkrVDFqVmPlDXICiRgyyqgTNVXEReXay-YBOFH3nJwAYJcGXfy8fX7eHJO7aRV49Zur7-UKxilXjjWzB6wMEyEEyklzB53fgio9mlZs3xCWvlLOa-84RaZhmACPnLkmYKPBkYlTv9q0GiTSNGbkHcdpzCDejwG1dh0Y4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ دستیار پوتین: مذاکرات با ویتکاف و کوشنر سازنده و صریح بود
🔹
یوری اوشاکوف: ویتکاف و کوشنر متعهد شدند ارزیابی‌های پوتین دربارۀ حل‌وفصل مناقشۀ اوکراین را در مذاکرات خود در کی‌یف مطرح کنند.   @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/460444" target="_blank">📅 13:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460443">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBlM4pfXNPv3-kh0ENv9qQDVjhQ35eDgvRvAe1BI_GRqndfaz4oGeCtF3klxMxfZu0Nicm9D-3EITQOzgIaxAApkJL9_4igOZQ_oKRft5x-jnyxTmw6-StkPYMxPBDWgoJvdJbBqtl7sEH7NB7J9BEXAwPn5oobH9uYmugumUURDwXrnEgEgsGHQqcfQgAaajBhzIzyDFrAOJvX5eIxGWshe_RoIYWxZUO0mngFjoMP2nw3tO_kn9uSWCuoGZxfaD3VbDTJlSzE2HpXFBI7OE_Y5Dzf5wZEmxUb7qTENCTwrt_RvhCJ4L0iY9V7T1LCWXEdGwn38tuyCQJZBmaeRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری سیستان‌وبلوچستان: با رفع محدودیت پروازی فرودگاه کنارک در امروز، پروازها ازسر گرفته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/460443" target="_blank">📅 13:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عرضهٔ ۱۰۰ هزار سکه از ۱۸ شهریور
🔹
بانک مرکزی: برای اولین‌بار عرضهٔ «اوراق سلف موازی استاندارد تمام سکه» از ۱۸ شهریور در بورس کالا آغاز می‌شود.
🔹
در مرحلهٔ نخست ۱۰۰ هزار سکه با سررسید ۳ ماهه عرضه می‌شود و دارندگان اوراق در سررسید می‌توانند سکهٔ فیزیکی یا سود ۷ درصدی دریافت کنند.
🔹
همچنین امکان فروش اوراق پیش از سررسید به قیمت روز سکه وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/460442" target="_blank">📅 13:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AN5ALIRo0-tDQ7yyipRuC8QRnHqDgIZa62iIiDZ8eFiZ3DuIZVnOOPqJlyY-urZEkAFtGbXa9bLvTtc1DM30fp3eK3d05t64xgh0FkBKdWQSwZmnY_iiOfL12mrh4BxJuYvoNMDR8A9NoMyWKvpR8QWz9JSZqPqMMDfat3SGnu9zcRvKJYcAgDb3CJuHcnJ9NfoFBg1Q-WCCFCQtZ41pEn1MBZhB6c8fDFJYgTD1LVO-A693F2kbAau-3RQrDKRy4dC_1Ofb81QNE1-QXUoN8OHONbAlocdrDg_YD_8coPWuQSzo7kAw8EEK7CxdjFI5IO4_vDxsmbEA8JKs803PJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/460441" target="_blank">📅 13:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460440">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53de44c1e8.mp4?token=ae9xOdrvTjCFM9U9JoyhZsxW217AtBNAxfjVx4QoDDL_qCJqfLj-8_nTFS2jFod3utFBLl6WWii1aVCFPFOHBSdaYO6_egwxnDzsWMky2gZ8bnM3WIFnj6HnLR8KDhWwTv91vNNhsPOayy_-UbJLACMeGvHbwaAHt1ctnIu01VsnwcwUZARcx6rQUVnVm69u2AF4ao0z5WljdWTG5ECZyfJKzQcw04pV8vf8RHHId1LcEsXK6iXDjI_rrM1gbGU5FqOT3g2FWMA2rdjA5qW3Jmt85aU0E8xetYKLllLWVvCXNDo2vvakmKC4o3ollUpyqJk2iMx67TjBPMB7z6T5qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53de44c1e8.mp4?token=ae9xOdrvTjCFM9U9JoyhZsxW217AtBNAxfjVx4QoDDL_qCJqfLj-8_nTFS2jFod3utFBLl6WWii1aVCFPFOHBSdaYO6_egwxnDzsWMky2gZ8bnM3WIFnj6HnLR8KDhWwTv91vNNhsPOayy_-UbJLACMeGvHbwaAHt1ctnIu01VsnwcwUZARcx6rQUVnVm69u2AF4ao0z5WljdWTG5ECZyfJKzQcw04pV8vf8RHHId1LcEsXK6iXDjI_rrM1gbGU5FqOT3g2FWMA2rdjA5qW3Jmt85aU0E8xetYKLllLWVvCXNDo2vvakmKC4o3ollUpyqJk2iMx67TjBPMB7z6T5qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: سامانهٔ بارشی جدید از یکشنبه وارد کشور می‌شود
🔹
با ورود این سامانه در روزهای یکشنبه و دوشنبه در اکثر مناطق شمالی کشور شاهد بارش خواهیم بود. @Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/460440" target="_blank">📅 13:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بازداشت شهردار رینۀ لاریجان به اتهام اختلاس
🔹
رئیس دادگستری مازندران: در پی بررسی‌های انجام‌شده دربارۀ نحوۀ واگذاری و انتقال تعدادی از قطعات زمین متعلق به شهرداری رینۀ لاریجان، شهردار رینه بازداشت و روانۀ زندان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/460439" target="_blank">📅 12:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460438">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOclXDyQt3Z3PHVeqno7Yvjxv1rw0uXOhqPf3gOjPVRJcyyZEXYDsIO_oQ69uC9FMKwGmLvFoik72PI_RUAdQYS8gwLnnEWSX6VOFqoqWzNTc18T4_BEvb4kCbCNStfROcpT7vkUKbhNJcsXqFo0s4VyVe7fnpxkHY2K9Rh8mwOpsNy8gOaV9GnbPSoSNXh3d8pt_QxS4kfKkHTz0gOps9nfjQnf-X6tfUIiQj8BbPKClknhFT5L3S5POJd4ALjxrYG8VCCnNxDchndVyt00ca8Fjp6X6tdbxVvnLA6SmP5ZJB0EyVn9jIB2dYN6qrb7HGkuHXMAao-xQXvCtnomwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال دیدار سران روسیه، آمریکا و چین؟
🔹
در حالی که اظهارنظرها درباره دیدار روز گذشته نمایندگان دونالد ترامپ با ولادیمیر پوتین ادامه دارد، معاون وزیر خارجه روسیه درباره احتمال دیدار سه جانبه سران مسکو، واشنگتن و پکن حرف زد.
🔹
سرگئی ریابکوف در مصاحبه با خبرگزاری تاس اعلام کرد که برگزاری این نشست سه جانبه، «منتفی نیست.»
🔹
این مقام روس گفت که چنین قالب‌های سطح بالایی سیگنال‌های مهمی ارسال می‌کنند اما جنبه عملی آن به نحوه تدوین دستور کار (سه کشور) بستگی دارد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/460438" target="_blank">📅 12:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460437">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc1768843.mp4?token=gSzB-gpVV8yLCM91-Vho95RyU138hmPPE5euzNIx8YuoY89MffCdQH9aKuxjlMpPyrc12gVPP9nC5o-xLWD8bIYvEjETeBJLuWiH_kVpNfKHxRtic9Olf8XA6wprF-ngwxMua5ZWvZtF4yYWSzWt73Y8eMx2pAG9bvlZD1OvjNkj2ydmYkTmY4rNdE3XLj5zwOcpO2rQcUKh6eL3w9UWWyQ5u4hmvmj8xs5ZTa5F7O9OHlcIU8yQehrC-5FGte7kcw1oxAA5SguPQuu5UilgYpXSY0aQ355PHQGJP2JZuMZLWToBR8mTNCIdcbvBUxHPRix5EkfBJecVzD6qQajVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc1768843.mp4?token=gSzB-gpVV8yLCM91-Vho95RyU138hmPPE5euzNIx8YuoY89MffCdQH9aKuxjlMpPyrc12gVPP9nC5o-xLWD8bIYvEjETeBJLuWiH_kVpNfKHxRtic9Olf8XA6wprF-ngwxMua5ZWvZtF4yYWSzWt73Y8eMx2pAG9bvlZD1OvjNkj2ydmYkTmY4rNdE3XLj5zwOcpO2rQcUKh6eL3w9UWWyQ5u4hmvmj8xs5ZTa5F7O9OHlcIU8yQehrC-5FGte7kcw1oxAA5SguPQuu5UilgYpXSY0aQ355PHQGJP2JZuMZLWToBR8mTNCIdcbvBUxHPRix5EkfBJecVzD6qQajVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: تاکید رهبر انقلاب به پرهیز از ضعیف نمایی، دستورالعمل راهبردی برای تمام عرصه‌هاست
🔹
حفظ «انسجام درونی» و «قدرت بازدارندگی خارجی» دو ابزار مهم برای مقابله با دشمن است و هرگونه سخن یا عملی که به تضعیف این دو ستونِاساسی منجر شود،  نه تنها خلاف تدبیر…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/460437" target="_blank">📅 12:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460436">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f24840d9.mp4?token=FKehWaMmq86Mcr5oV00pkawi-VYgMd2d_raOqDriZeX4Hk4GJXR_bRPL3XSdQQ-hh9jrfUBghAZXiPXU-fgGXY-3cL6GfY0vSon9R-1UFmZVDXTz4pTUyIBSi_IcvlHdHF-kzjPHbm07hBRqCGvCl-20MX3PkL3Zwt7-wQZICtH7BDjkCPzVf_kkmwCHcVdilO5DBl-Ipo03qhRQbCvYM2q4q2QSByn1XH2im5MYGJCYqVXyglDkmugKqKADped_ne4ut6dUvrp-GEGAFB_yuzejRjFjvL77dfCq01PuouSCRb2pjRwePlWWRF7WdOe3Gaoy3vez-HThDxiUnZj_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f24840d9.mp4?token=FKehWaMmq86Mcr5oV00pkawi-VYgMd2d_raOqDriZeX4Hk4GJXR_bRPL3XSdQQ-hh9jrfUBghAZXiPXU-fgGXY-3cL6GfY0vSon9R-1UFmZVDXTz4pTUyIBSi_IcvlHdHF-kzjPHbm07hBRqCGvCl-20MX3PkL3Zwt7-wQZICtH7BDjkCPzVf_kkmwCHcVdilO5DBl-Ipo03qhRQbCvYM2q4q2QSByn1XH2im5MYGJCYqVXyglDkmugKqKADped_ne4ut6dUvrp-GEGAFB_yuzejRjFjvL77dfCq01PuouSCRb2pjRwePlWWRF7WdOe3Gaoy3vez-HThDxiUnZj_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: در کنار میدان نظامی، اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است
🔹
مردمی که تا پای جان مقابل دشمن خونخوار آمریکایی ایستاده‌اند، سختی را تحمل می‌کنند اما سوء مدیریت و کم‌کاری را تحمل نمی‌کنند و ازما انتظار مدیریت سریع این میدان را دارند؛ و…</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/460436" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460435">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/628cd260b7.mp4?token=a3h4bnmf5jGPFvdaSISs5_Mo5eui8kTscRviTwq3kZsR_hfj_8oW_w1UakFpP4T6HOEhzNLfVEz9pB2K3TNLZinzi1ffJl3k6TApo7mBXs6FctEbn3QtfAlqq3Bd0QZ-WxFxLCiDyYlvk4-54_Q6LNEtPCZS2pkpPanMSLl43DdJMfjcTcWEVjVEhNXI_WvEkrd01DOQWd35RfO5kcbAqgzXr7lKWw8wWkL4EUtDOvMgo3XR23Vd766Kf5dyKvuSfy-ZmJUXwI9eu6Pn2A2Sut6MetOGxqP1D1ki9RGevuJTmcqOiuOvZLkBfW3yu8l9aQOyxydh7sCr-Pjl9wQ0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/628cd260b7.mp4?token=a3h4bnmf5jGPFvdaSISs5_Mo5eui8kTscRviTwq3kZsR_hfj_8oW_w1UakFpP4T6HOEhzNLfVEz9pB2K3TNLZinzi1ffJl3k6TApo7mBXs6FctEbn3QtfAlqq3Bd0QZ-WxFxLCiDyYlvk4-54_Q6LNEtPCZS2pkpPanMSLl43DdJMfjcTcWEVjVEhNXI_WvEkrd01DOQWd35RfO5kcbAqgzXr7lKWw8wWkL4EUtDOvMgo3XR23Vd766Kf5dyKvuSfy-ZmJUXwI9eu6Pn2A2Sut6MetOGxqP1D1ki9RGevuJTmcqOiuOvZLkBfW3yu8l9aQOyxydh7sCr-Pjl9wQ0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است
🔹
هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/460435" target="_blank">📅 12:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460434">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90cc48db21.mp4?token=CqkyaQ9Lcdlez7XAs0jNGtfDZDDPEOUTwACpXuSy09_vnBSp-xOC5R0QyOZBOG9AUrCf-82e4Wq8_X8UMozgYHInHo88XhDbgCvEgertTyWkPE02zoHMfWsrlz9eKplODxt3VmqtS5bQEmj2UZRvLQiJbmgc1yNrdlW98tQ3OCdD9Y7j00Z-Ry7sd9Cjf9S7x6GZvHIFi1MDOjiShtNVbx-XeMGErRpr5ar1ENMWwWAGINcvtVprZbAzYMMrFUi70LbO0Qy9qyrpe1PiHuKpmMUKD6u4xNjEBVtxp5INUdxn28ezEST_sRK9I_OiI9N1dsI-RHendgyUJSScySX7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90cc48db21.mp4?token=CqkyaQ9Lcdlez7XAs0jNGtfDZDDPEOUTwACpXuSy09_vnBSp-xOC5R0QyOZBOG9AUrCf-82e4Wq8_X8UMozgYHInHo88XhDbgCvEgertTyWkPE02zoHMfWsrlz9eKplODxt3VmqtS5bQEmj2UZRvLQiJbmgc1yNrdlW98tQ3OCdD9Y7j00Z-Ry7sd9Cjf9S7x6GZvHIFi1MDOjiShtNVbx-XeMGErRpr5ar1ENMWwWAGINcvtVprZbAzYMMrFUi70LbO0Qy9qyrpe1PiHuKpmMUKD6u4xNjEBVtxp5INUdxn28ezEST_sRK9I_OiI9N1dsI-RHendgyUJSScySX7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف:
آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است
🔹
هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/460434" target="_blank">📅 12:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460433">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psYH2WsSlSl1QfFc4qGuQWDb9HrgNGc6uWOeBWv45VXeDEZZj2VE0XsmN3ZdZBEDiWeF5l2hQ19kNmWgNHkKzuhhsX-WfaJvnkn4ZfU4q13OBdNxs2q413WUma5_SRc0RtLXjkgavIm5Di6BqJqt7nDC_vdYvdk-sFTcB8lVvQHIFPR6UD_Uxw_O5wt5CqwLy_kj_D2kpW6wlUb7PEtLP6t5gBlyf8Ve3PMgY45YAAM_Ayq2VwddbXQzNGqtXJJ6pkhE2xDsE0DcOn9UD11tjYGenE3nDXcegm5t7qHzoRru1OJDjUfbfvi5jb3i7pQgNh9RxdflHzG2NDfIuTlOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس رکورد ۶ میلیون و ۷۰۰ هزار را هم شکست
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۲ هزار واحدی به ۶ میلیون و ۷۲۴ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/460433" target="_blank">📅 12:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460432">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEdxEeXY6n9UBXsFTKQfCNY81Fynlr-sfbgYf1PshpcfRzNABQThDv6tpDvziD6aGB1H0VRcpqmbTn2HBO7jIDXUcAGQ4IgtBOOwIKDfenv6J5YtFdtIUlS-hGEQhyp726cYQS_NDxB4Y8KRzoZVfq9ozsLSo1XgfRg3_fbaMCy5Q-IXgVndeXRaRFEfK0y5ScBgNSdexv7DxpSCU3rOXQJXYpr0hHxUt-sjfY3crzaVI7OTAvr2Z_idXc2lh1OYOevnLa_zpgpf09bNadrx8WXDXKf6Jlhc10iOR3oxmmzROXuXPcx5e4J_ZrOLrZzXMa07K5NVt4JdtHVHJnTr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای روحانی، دوگانۀ اصلی، «مقاومت و تسلیم» است نه چیز دیگر
🔹
اظهارات حسن روحانی دربارۀ اینکه آیا مردم حاضرند «۲۰ سال دیگر» با قدرت‌های بزرگ بجنگند، با انتقاداتی مواجه شده. منتقدان می‌گویند پیش از طرح چنین دوگانه‌ای، باید دربارۀ تجربه ۸ سال اعتماد به غرب، مذاکره و توافق و همچنین بدعهدی و فشارهای طرف مقابل توضیح داده شود.
🔹
علاءالدین بروجردی در واکنش به اظهارات روحانی تأکید کرده طرح مسئله به دوگانۀ «۲۰ سال جنگ یا راه دیگر» بدون توجه به رفتار طرف مهاجم، صورت‌مسئله را تغییر می‌دهد.
🔹
عبدالله گنجی نیز از روحانی پرسیده «راه دیگر» برای پرهیز از تقابل با قدرت‌های بزرگ دقیقاً چیست؟ آیا این راه به معنای عقب‌نشینی از حقوق هسته‌ای، توان دفاعی و موشکی یا پذیرش امتیازات جدید در برابر مطالبات طرف مقابل است؟
🔹
جواد بخشی‌الموتی، استاد دانشگاه هم  تاکید کرده که کسانی که در گذشته به‌دنبال بستن با «کدخدا» بودند و امضای کری را تضمین می‌دانستند، امروز نیز به جای پاسخ‌گویی دربارۀ نتایج آن رویکرد، تلاش می‌کنند با فرافکنی، افکار عمومی را از کارنامه خود دور کنند.
🔹
محمدامین سلیمی با اشاره به تجربۀ برجام، لوزان و سعدآباد تأکید کرده نگرانی اصلی، مذاکره با طرفی است که سابقۀ نقض تعهدات دارد و مشکل زمانی ایجاد می‌شود که پس از توافق، طرف مقابل همچنان فشار و تهدید را ادامه دهد.
🔹
محمد اکبرزاده، فعال رسانه‌ای هم خطاب به روحانی تاکید کرده: اگر متجاوز وارد خانه شود، آیا ابتدا باید از اهل خانه پرسید «دفاع کنیم یا نه؟»
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460432" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPfRXZHxQ42hH_rpm-g-OfEyQ8QZ_hjiQqYowUPLCwiY2_L2EqQSsgQUocjnH134ixxebo2eNGWyUHFvdG1VdwYmvhr9NTg2Q6aid4nMG0Jp_ChlDkKqiJs9jS0cP1P8WwKFTyj8DI7mmesdUKAXf0GFv4IoBIte1jBo98MU0QlGf0zv1PXeu4XSsQ-JctfBy6i1N3vQL3R6Qv-0cmO02SeS7zrFbFaSbT8WolY3Ak1gpXG9xxsBsz5FamRyOS35_TVfL0PHcb1KWg5OIF9Q5wAabpyLgtYT-HK5_1UTdFHmidp1_ef7vOPpky-s5JW6v-IR0xMkjKZ1fcGfMr5pJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان از استقلال شکایت می‌کند
🔹
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت می‌کند.
🔹
پیش‌تر آسانی در دو بازی اول لیگ مقابل مس شهربابک و نساجی هم بازی کرده بود و طبق اخبار منتشرشده به همین دلیل شکایت‌هایی علیه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460431" target="_blank">📅 11:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnP-C6D_ynVeCPIWkZrPvm0sF-lZR_2__hqccbHhc1IlvmPrIhq6ZZcBZCTDWVyFM8Uw1ntG6IS1u2sot_S6mxJNPFUddY1-FxOl3KftPdZGbHHYp8Uoyy7RNkiRyCUeuZqSpRAXY0cniJPrknEfMHGYGFDG-OBy20SpJnjiWXtDYzdLCsNKz2_teacSTm4fiKlCTNzOw_3CFIGxcNABStZw-7j_Ij0eUct1EdfNroaiLhlcIA372LeOVWF_sM2WTRfOgG8mxZe0_LMRT8BFR_R54rHpyedRCPjqs3oMTRwQjkt7var_6lGHSXBlgLaDplfxViiNEEYbiKHB2FruHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت مرغ کاهش یافت
🔹
براساس گزاش میدانی، هر کیلو مرغ به ۲۷۰ هزار تومان و ران مرغ به ۲۰۰ هزار تومان کاهش یافته است.
🔹
وزارت کشاورزی اعلام کرده نهاده به حد کافی وارد شده و بخشی از آن توزیع شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460430" target="_blank">📅 11:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcQN5RN-XscTwLa9RNOa_eAuE7kMVw1sGvDzxJeeJw8BEWF5Ic91Q4RQO6zvdnisPJ5eyj6C-IjUK45U1qhNkl-KbMwuu0sZCjMO_QNdlLvabx_uKLD9sM6Ula9w3DwFmHcV0stiRRlAYE15FphV0dnhVjL2s81Kr9k3OAsSQvOQbsk2-9mIMtjW2wnRstQpLh0JXl-_yKMkVUefmbiWBD-Ob2GTzWx1MAFD-rdaKfw0d0vF5LjprI1A9-MUlnKH8h9u-zpKTi7wvkU2MKhUl2GTQNHwdytGler7SKx7Pyxf0explgVCIKR8tF2pVMfP5PkMtEqePF1ihRxWHlkf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور ابلاغیه برای خداداد عزیزی
⚽️
با اعلام کمیتۀ انضباطی سرپرست تراکتور به‌دلیل تخلفات رخ داده و بدرفتاری در قبال مقام رسمی مسابقه، باید ظرف ۴۸ ساعت دفاعیات خود را ارسال کند.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460429" target="_blank">📅 11:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_ZwDpHPESNz3qJofmdPjHCUSSxnCtwfMTdl-htfYGeA27Zgqi-tGscmzow7_N3dCCwC0ZVH7X2ldxVRCYi24XSgSsSClIdac559DiCqE9yLhRImDXfF92LUrfLn6gMVOQNx1Nrkncbko46EtLMVe1sKXk1naZTszvFklLYuTGD9EGpDBKc1AGC60NSPOYw5aAwVZL62JIj-mMB5A9nlN-3S0qMgQ-t_E2Q7D_TB8cuH9e2QFmrHf7cLOua67wFt-v1C4A0RvslFgdpRUJlFNxbGoLcp_lWJGxsB-zxwdQEzVl6JwZvuNnHHDeLMzu_HhMehDaqbIjMUQeH1PhDd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نهاد مدیریت خلیج‌فارس: فهرست شناورهای متخلف بروز شد
🔹
برخی از این موارد با اطلاعات داوطلبانۀ مردم به‌دست آمده است. @Fasrna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/460428" target="_blank">📅 11:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چمران: متروی تهران فقط تا ۱۹ شهریور رایگان است
🔹
رئیس شورای‌شهر تهران: مترو و اتوبوس‌های تندروی تهران تا ۱۹ شهریور رایگان هستند؛ ادامهٔ این طرح به شرایط پایتخت و تصمیم دوباره شورای‌شهر بستگی دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/460427" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvZmQ31PJb_EuvZbVnWFRAMB1tlUj7pfTQ-rVyMClUS4OcbX5gwSTewrzg58tzG6fwLndba-jtqai5AsRqTC5xdRwRIdhtZjg58gLnNoEBkHsqxPAQhJK2xbqI6JCn4-Ic7MIvVbcNuCarMvfEbZ7ewK38rwBXjp02y7xgfMaKdfxdYSF5FksgV1mpvBojzbIbOzmy4g3NvtVUU7inKF97EKK2HqJmSJLDWR6iBwMbh2GGzEgu1zSx0Rr-U-eeI2hqicIZtLnUr1rOLTjKvmQQ_96_FSSTPrAqVUd0k7dbiNIXqAgT0UxT-FFz4T2VPsceupzOLse4u699wNfKwikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن ۱۱ شهروند سنندجی در آتش‌سوزی تانکر سوخت
🔹
رئیس مرکز فوریت‌های پزشکی کردستان: در پی وقوع آتش در یک دستگاه تانکر حامل مواد سوختی در پلیس‌راه سنندج - همدان، ۱۱ نفر از شهروندان جان خود را از دست دادند و ۵ نفر نیز مصدوم شدند.
🔹
به محض وقوع حادثه، تیم‌های…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460426" target="_blank">📅 10:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شهریهٔ اجباری مدارس ممنوع شد
🔹
آموزش‌وپرورش: مدارس دولتی هنگام ثبت‌نام حق دریافت هیچ‌گونه وجهی ندارند.
🔹
مدارس غیردولتی نیز تنها مجاز به دریافت شهریهٔ مصوب هستند؛ فعالیت‌های فوق‌برنامه نیز باید کاملاً اختیاری باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460425" target="_blank">📅 10:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GorMMSFkdAzG4gOXEeC-2QDxLt2q3QUQaC3aZVBSDdYyWz5M6sNp5q20l1Eij5oqoOa1fejFtiGC2MqqH7WtD_S2DJYTIpm3FB0RSmqZQAaCKJmMzvPcTM4AEFl6k4czhhBNMp2YLGZcYVJB8X60GNCmTyI1b1aueBOO8YV2g0mcldHCPEhAxApCzJ9qp9KbVDFkoB4pj53P1p8hYixMZ09c_gftyrlE49ypD2s7uktDIW2pe87jsUAm4u1qSjMe2eavnzTBG9DjqtrN_Ux495f7q7ITpa9sHeiQYrvirWZwqOZsqb9ftSH7c7rI2clK9Jo2Pfnjnmwl2ED1M8U8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمسایی: با تلفن و سفارش، کسی ملی‌پوش نمی‌شود
🔹
سرمربی تیم ملی فوتسال: برای حضور در اردو بازیکنان را براساس کیفیت و شایستگی انتخاب می‌کنم، نه تلفن و سفارش.
🔹
تمام ۱۴ تیم حاضر در لیگ برتر را از نزدیک دیده‌ایم و هر هفته آنالیز ویدیویی و جلسه مشورتی برگزار کردیم و به فهرست نهایی بازیکنان نزدیک شده‌ایم.
🔹
به‌زودی بازیکنان موردنظر را برای حضور در اردو دعوت خواهیم کرد. شک نکنید که خودمان را مدیون حق‌الناس نمی‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460424" target="_blank">📅 10:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147a8f9b1c.mp4?token=Gej-g7DBn9y_TiXiVOW1uPr1sRCkPOkmnpAR5c9H3e1a76m-wLRbB9kSW4j-eB-SgqXH9BUl2ftcKBIbdhu3OLwH3JsGoW34nVyOfL2x25xkD--s_qEvvlE2CgbjlGBAoJkoutDgfgbsF-gDVUgA7y7YASPHlSOV5jUZCet1zNNJmZkJaVrS9xDk3HFuABaWzHFILVcDliLtMca7FxqtzKhEsTh6i_rBxJbLWUKmGmid8zUgANbM_SGmMmL0zZ0me1GOnqjZ7xaPcunjgPopJ6mxluQDZI5M_lvNfWgKdPA40bWvBH94-Q3G6UV8W-n0eAlk0qJp6omV5U0ZU0zfaqowg9VD0UHuyxwSpF1CnjdIkf5ve-fRrXnZHvz7x4wen04DSVw4QrhKng51jMlNHcNRtiUjwsB4jIIXyx_HJMi17kuim20Th-vW-41jLjoU6lJ6ZVWDXW30cGq6HjUhj3DXsxBQvY4A17Do9ZtugI2uXH2hlHIF16i7a_ecsip6hqf7qt7evmVmZNQHzcMQwBJ4J0w0gg00Qq-kT2TsRFFofU7OEcyJNsxn7xu9LjV4wbtEy0T6v_vK5tJrFjdAoPTM9s_8J3ISWwn8y2d6GrJz0oXqRLWV5N2Kx3bypfOMpSIYLhuNrg4dFKtfh1NMHWDVG-8BnYJi4HcTOUyi3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147a8f9b1c.mp4?token=Gej-g7DBn9y_TiXiVOW1uPr1sRCkPOkmnpAR5c9H3e1a76m-wLRbB9kSW4j-eB-SgqXH9BUl2ftcKBIbdhu3OLwH3JsGoW34nVyOfL2x25xkD--s_qEvvlE2CgbjlGBAoJkoutDgfgbsF-gDVUgA7y7YASPHlSOV5jUZCet1zNNJmZkJaVrS9xDk3HFuABaWzHFILVcDliLtMca7FxqtzKhEsTh6i_rBxJbLWUKmGmid8zUgANbM_SGmMmL0zZ0me1GOnqjZ7xaPcunjgPopJ6mxluQDZI5M_lvNfWgKdPA40bWvBH94-Q3G6UV8W-n0eAlk0qJp6omV5U0ZU0zfaqowg9VD0UHuyxwSpF1CnjdIkf5ve-fRrXnZHvz7x4wen04DSVw4QrhKng51jMlNHcNRtiUjwsB4jIIXyx_HJMi17kuim20Th-vW-41jLjoU6lJ6ZVWDXW30cGq6HjUhj3DXsxBQvY4A17Do9ZtugI2uXH2hlHIF16i7a_ecsip6hqf7qt7evmVmZNQHzcMQwBJ4J0w0gg00Qq-kT2TsRFFofU7OEcyJNsxn7xu9LjV4wbtEy0T6v_vK5tJrFjdAoPTM9s_8J3ISWwn8y2d6GrJz0oXqRLWV5N2Kx3bypfOMpSIYLhuNrg4dFKtfh1NMHWDVG-8BnYJi4HcTOUyi3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی فرمانده سابق سنتکام به مجری ایرانی صدای آمریکا!
🔹
ژنرال دیوید پترایوس، فرمانده پیشین سنتکام و رئیس سابق سیا: شکافی در میان نیروها در ایران وجود ندارد و رویای فروپاشی حکومت شکست خورد؛ راهبرد استقرار پایگاه‌های آمریکا در منطقه جوابگو نبوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460423" target="_blank">📅 10:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2CQ9mhzPogWcPv-UvRerFvDQCQA8ehM6T98lnr6zkmggyMqCwkl9b3KboCjODN6FPGA7mmTfjyaEeVsap6KJ_COR7XhGKXbnDapLK33MnfT0Uk8XYbKz3XZTvmNp03u7UB_p0ad4prU84g_EszB_J-v9__3DWcpgnAMHeTrko_J4aMha6dVA-w-4xncyqoFatwW1ih3zCgmopDash1HC_XApATI5Dt1R5QETbe4MGeESPTamoWnYabsynC9PzQ1uL7cchfvzXJAa5kRdXiasIoSecabx4CiK4zKYAAl2fM_1oFmA875ACuCAdsijylv5J4I0PZ21Fq4oPfS3B-w-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بار خداداد را سنگین جریمه کنید
🔹
پیش از شروع مسابقه تراکتور و گل‌گهر مشخص بود حضور امید عالیشاه در تبریز، با توجه به سابقه تنش‌های ایجادشده میان او و هواداران تراکتور و اتفاقات جنجالی دیدار پرسپولیس و تراکتور در سال ۱۴۰۱، می‌تواند فضای ورزشگاه را ملتهب…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460422" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc4adf04c.mp4?token=phl8vdL76HZvBYMdCCJv4DMhvuJUjH-qLWq1eg2UGd_ItGZ2C-efotibctFwjstl8g88pmaUKOikqwEgSrlLIQEGe3Yk1iFql3T-6D_WFOmVkhGX4x9041O6QCAjkFJ01kpmtQWesUxdEe0DOPMZLNYpDE1DKNVdzrJIUQHHjEMTl-YvT7khgP_TnRS1TX26wbocRXeP1V54WbN5VqTiFpovmgvV7YIqAx-Mifgvwj5isBvjVyt5FK-QD5KSTwzvb8h1xmqM0I1pIemqZfy-wFqbs8XSZJtD0RLqDug0WvfRBRSbMCJl4gp2BFdEYubbYb1OpQRdhnWOW4A-8ILx3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc4adf04c.mp4?token=phl8vdL76HZvBYMdCCJv4DMhvuJUjH-qLWq1eg2UGd_ItGZ2C-efotibctFwjstl8g88pmaUKOikqwEgSrlLIQEGe3Yk1iFql3T-6D_WFOmVkhGX4x9041O6QCAjkFJ01kpmtQWesUxdEe0DOPMZLNYpDE1DKNVdzrJIUQHHjEMTl-YvT7khgP_TnRS1TX26wbocRXeP1V54WbN5VqTiFpovmgvV7YIqAx-Mifgvwj5isBvjVyt5FK-QD5KSTwzvb8h1xmqM0I1pIemqZfy-wFqbs8XSZJtD0RLqDug0WvfRBRSbMCJl4gp2BFdEYubbYb1OpQRdhnWOW4A-8ILx3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قبل از خوردن انگور خواص آن را بشناسید
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460421" target="_blank">📅 09:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460420">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqwDp_NEsoOqRptnEr19I3WrDKYf_M42WI9SQM6DSBkIylOO5Kz0z3FvEur0Xf-Tqmw7RPCaeJOtAp3Nv6O_RS8hF_Kam-iqvs-x-3yT0Yr42pJkqW2O_rfm_Jgsq5Q4Uz_TFAHQQ1AdirLdviWHulof70XtOCF95SsqDireYBSGuxZmcBliFzl1ydW3XqWurZ8s5IL3YMzfrL1YZxZiuYwncEQZlqsyGobYYIhl9I0Bni87Kc7JNVDdFM0eWU93I4g9Ub0HB7Vm9lDLoiGsaKznTuHZTYI1HWXQ5kqlUGdWmnkd9MBwW3iz_Udw4X3-limUWaZEp1qOnaijZYcQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشدید حملات هوایی و توپخانه‌ای رژیم صهیونیستی به جنوب لبنان
🔹
ارتش رژیم اشغالگر دور جدیدی از حملات هوایی و توپخانه‌ای سنگین را به مناطق مختلف جنوب لبنان آغاز کرد که منجر به تخریب ساختمان‌های مسکونی و مراکز درمانی و شهادت دست‌کم دو نفر شد.
🔹
بامداد امروز، جنگنده‌های ارتش اشغالگر حملات هوایی گسترده‌ای را علیه چندین منطقه در جنوب لبنان، از جمله شهرک‌های «القنطرة»، «زوطر الشرقية»، «نبطیة الفوقا»، «نبطیة التحتا»، «وادی السلوقی» و «دوحة کفر رمان» انجام دادند.
🔹
گزارش‌های میدانی حاکی از آن است که در جریان حمله هوایی به شهرک «کفر رمان» در شهرستان نبطیه، یک ساختمان مسکونی سه طبقه به‌طور کامل تخریب شد. همچنین حملات متعددی به اطراف نبطیه و شهرک «عربصالیم» گزارش شده است.
🔹
هم‌زمان، توپخانه ارتش اسرائیل منطقه «نبطیة الفوقا» را هدف قرار داد که بر اثر این حملات، خسارات گسترده‌ای به «بیمارستان غندور» وارد شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460420" target="_blank">📅 09:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQrBrnryay0kdGrXJ51tFHlCJ5Rz7928n4pJ-yvZncRH5BQKmyc_OawhQqS1GAtqy2OupM2d87qf8Tvzjqa8iv1ZaLemMLQkOPcSOJiRZeHm61hX5EJGN-SQlraLJVqNoVRg49SHsgWqVtqgEf7E2rABpdF08IlT8lKr1eM0rC2J-1n2V_4ZPERjp2AobWgm3JA9yiVDRaait2kn4sddTtSgZmnRtMjPQiH2G0EYbwRI9Wm6RCYqnzrEDp9ylZhyLyK8rvd8xZHstQnxzGqOiXOHLk9HQh7Ok4EYvZcRPoEV8QJmYJjzQOvnNjBXQ-afHevZXvj1dJUPOe27e-r9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460419" target="_blank">📅 09:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goJBAj66MgJkT6vJuZJDhxZ5AeZITHGbN91Ialvo7T4ZEOWWc0AqslzA-5QEfzMayBPUVjT8fJNVodbQquL_s9Xk69viZrX6M-ZUgmjS7J8aIThxW9oa_I-jlSZVHmvda23PL2F6yGDBdIVdQC8XBIOArOzFKPTq5moXDvA6vK63xJLZp5d5e8qcHQQ4N2ky9mWHp2Y4_sr6Vygd3xbiLjS-Th-iUe-15PIIxASlavshi-wCZNU50-vQsyt7jkcKilc5LzF39Je724LDIBX_TJE2RPymPfywLKXuy4Y0TKEf0w8A4yfSOYsGvcMh95QDp3iFzp1MRjk0R1PpIg5_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسهیل ورود پلاک‌های بین‌المللی به کشور
🔹
گمرک ایران با صدور بخشنامه‌ای، در راستای حمایت از گردشگری خارجی روند تردد خودروهای ورود موقت دارای پلاک بین‌المللی را تسهیل کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460418" target="_blank">📅 09:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4309078e57.mp4?token=hEK6NPH7SNKb0BzZUuQHIYMW_1Zn3IiEq1Pxn4tB6rAQ-PNd1svUWmnLZpz9vyiHvcWPtoI40BDhZsYOG_OIgWjLObYWVxTs8X495NjKrlIclrGU8aBNaMXfBitQXycNH9QZL6cZiBbyqmbCM6PhzB42WQpiuzz5Bn7paeYBywC8e3Ubt7HqDdOxjWbTCrkyP8LvY8io5jnX3t7DcIJqyV3q2n7RhKJ9b4F4UJ-lTg0ECu7pXIqJ4121TifE8_XyDKmlNPvEbuonKUig8JvOUWKrVVlKbM6TiLGy5pS_PPofSGKIVulR5LJN1NUhjmVDf2brOqi4scsqk4ZkAjQBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4309078e57.mp4?token=hEK6NPH7SNKb0BzZUuQHIYMW_1Zn3IiEq1Pxn4tB6rAQ-PNd1svUWmnLZpz9vyiHvcWPtoI40BDhZsYOG_OIgWjLObYWVxTs8X495NjKrlIclrGU8aBNaMXfBitQXycNH9QZL6cZiBbyqmbCM6PhzB42WQpiuzz5Bn7paeYBywC8e3Ubt7HqDdOxjWbTCrkyP8LvY8io5jnX3t7DcIJqyV3q2n7RhKJ9b4F4UJ-lTg0ECu7pXIqJ4121TifE8_XyDKmlNPvEbuonKUig8JvOUWKrVVlKbM6TiLGy5pS_PPofSGKIVulR5LJN1NUhjmVDf2brOqi4scsqk4ZkAjQBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود سامانۀ بارشی از شمال‌غرب به کشور
🔹
هواشناسی: بعداز ظهر امروز و اوایل شب سامانۀ بارش‌زایی از شمال‌غرب وارد خواهد شد و در نیمۀ شمالی بارش‌ها آغاز می‌شود.
🔹
دوشنبه و سه‌شنبه دما در نیمۀ شمالی کشور کاهش می‌‌یابد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460417" target="_blank">📅 08:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O19JBmvRgF8ITQHNX3orlQmmxY0yyHNY9N7hhe7xxa93-BmZn8jg5GGC5Ew-OrKU2P1DcJeermsuRrP2UFMhYRjSSSJTFy5VIfmjIqY89jq_w2F1DpXSGO__DkTWLwmy5UDbkVo7zbwFT0cvkLBJjzLpUAjuWYvknfmELO8zeesKho-tMnc0P4vnAyIDHZELVDgKVg81HftjiVAPkfQScTinaF_0lPFlO6mw-O3P558N3BRXoupBsChwcjvX8_w0RNVNGySwUF4yTglOo7N1HCCaEoPE3efwe4Q7k24-TZ8V7Qp-8NdYP6xbOKoYrP5qeJdZ4hGGgsq8sIFSm86tOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگ‌ها را کشتند که رضاخان بدخواب نشود
🔹
دستور مستقیم رضاشاه برای شلیک مسلسل به زائران حرم مطهر، تیر خلاص به نوزادان در گهواره و مسابقۀ شرط‌بندی روی دویدن مردان سر بریده؛ این‌ها برش‌هایی افشاشده از جنایاتی است که رسانه‌های غربی امروزه با سانسور شدید، سعی دارند آن را «عصر طلایی مدرنیزاسیون ایران» جا بزنند.
🔹
در شرایطی که دستگاه‌های تبلیغاتی غرب دوباره پروژۀ تطهیر دیکتاتوری پهلوی را فعال کرده‌اند، بازخوانی اسناد دیپلماتیک و تاریخی آمریکا و اروپا، پرده از حقیقتی هولناک برمی‌دارد؛ حکومتی که دیوارهای بنیادینش نه بر توسعۀ ملی، بلکه بر سرکوب و وابستگی کامل به بیگانگان استوار شده بود.
🔹
محمدقلی مجد مدرس مرکز خاورمیانۀ دانشگاه پنسیلوانیا، در کتاب «رضاشاه» می‌نویسد: رضاشاه هزاران نفر را حبس کرده و صدها نفر را کشته بود و بعضی‌ها را با دست‌های خودش به قتل رسانده بود. در نتیجۀ این حکومت، وحشت بر دل مردم ترس افتاده بود. به کسی نمی‌شد اعتماد کرد و احدی جرئت اعتراض یا انتقاد نداشت.
🔹
ویلیام داگلاس، قاضی دادگاه عالی ایالات متحده، در کتاب سرزمین شگفت‌انگیز و مردمی مهربان و دوست‌داشتنی، می‌نویسد که چگونه نیروهای نظامی پس از ورود به چادرها، هفت‌تیر خود را روی سر نوزادان در گهواره می‌گذاشتند و مغزشان را متلاشی می‌کردند.
🔹
داگلاس از زبان یک شاهد عینی می‌نویسد فرمانده ارتش، مسابقه شرط‌بندی عجیبی به راه انداخته بود: «سرهنگ طاوه آهنی را روی آتش سرخ کرد. با شمشیر سر جوانان لر را می‌بریدند و بلافاصله طاوه سرخ‌شده را روی گردن بریده می‌چسباندند تا جلوی خونریزی را بگیرند و شرط می‌بستند که بدن بی‌سر چند گام می‌تواند بدود!
🔹
جان گونتر سیاح آمریکایی فاش می‌کند که حتی سگ‌ها هم از قساوت اعلی‌حضرت بی‌نصیب نمی‌ماندند؛ وقتی شاه در سفر است که البته بی‌وقفه در سفر است در هر روستا و قریه‌ای که شب در آن منزل می‌کند سگ‌ها را می‌کشند، زیرا او خواب سبکی دارد و هر صدایی او را پریشان می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460416" target="_blank">📅 08:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هوای تهران در مرز آلودگی
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۹۸ در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/460415" target="_blank">📅 07:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بانک مرکزی از نظارت بر پلتفرم‌های آنلاین طلا کنار کشید
🔹
پیگیری‌ها از بانک مرکزی نشان می‌دهد بانک مرکزی قصد دارد «سامانۀ ناظر» را که بر موجودی طلای پلتفرم‌های فروش آنلاین طلا نظارت می‌کند، کاملا در اختیار ستاد مرکزی مبارزه با قاچاق کالا و ارز قرار دهد.
🔹
این یعنی بانک مرکزی مستقیم بر فعالیت پلتفرم‌های فروش آنلاین طلا نظارت نمی‌کند.
🔹
با اتصال پلتفرم‌ها به سامانۀ ناظر، موجودی طلا و دارایی هر کاربر به صورت آنلاین قابل رصد است، اما مسئولیت آن با بانک مرکزی نخواهد بود.
🔸
درحال‌حاضر یک پلتفرم به‌صورت آزمایشی به سامانۀ ناظر متصل شده، و به‌زودی مابقی پلتفرم‌های فروش آنلاین طلا به این سامانه متصل می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460414" target="_blank">📅 07:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
الجزیره: جنگنده‌های اسرائیلی در دو نوبت شهرک النبطیه الفوقا و حومۀ شهرک کفررمان در جنوب لبنان را هدف حملات هوایی قرار دادند. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460413" target="_blank">📅 07:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926651fb9e.mp4?token=GGCvX5sVdwxbHmo4Mb6uoGzFXD0ZHLvwI5pMBsOzv_ouX1XEsG6E7JLBhbWFcyachJzDq9UKTq25-n6ghMPUl2vNlySXHWi-7NTDBF9jAqt2sR_2Upm_FQng1pd-1oqpuUvUuICiXi7hbFtiHcxgXB4PM9fkSv7zDPhDjpvH297u5Aa8L3J4_mgCEMR2n9Fi_NRr2OpFIrtP7MPPJxFV7-63z9CNHYaeDtfXPd5ipfTA7gdYWYlx85Kg7DzMqoUePBsJ-tgQ0o_tXPnDcypuFWh3e18dsIPpvkkuA4erLWV5oAPZspUKaK4FH0-lJ5LToENTIzX1P2Fm1fE7v7-gdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926651fb9e.mp4?token=GGCvX5sVdwxbHmo4Mb6uoGzFXD0ZHLvwI5pMBsOzv_ouX1XEsG6E7JLBhbWFcyachJzDq9UKTq25-n6ghMPUl2vNlySXHWi-7NTDBF9jAqt2sR_2Upm_FQng1pd-1oqpuUvUuICiXi7hbFtiHcxgXB4PM9fkSv7zDPhDjpvH297u5Aa8L3J4_mgCEMR2n9Fi_NRr2OpFIrtP7MPPJxFV7-63z9CNHYaeDtfXPd5ipfTA7gdYWYlx85Kg7DzMqoUePBsJ-tgQ0o_tXPnDcypuFWh3e18dsIPpvkkuA4erLWV5oAPZspUKaK4FH0-lJ5LToENTIzX1P2Fm1fE7v7-gdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوران آتشفشان در اندونزی
🔹
بامداد یکشنبه آتشفشان «آناک کراکاتوا» در اندونزی فوران کرد. در پی انتشار گستردۀ خاکستر آتشفشانی، فعالیت پروازی در فرودگاه بین‌المللی جاکارتا به‌طور موقت متوقف و تمامی پروازها لغو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460411" target="_blank">📅 07:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
الجزیره: جنگنده‌های اسرائیلی در دو نوبت شهرک النبطیه الفوقا و حومۀ شهرک کفررمان در جنوب لبنان را هدف حملات هوایی قرار دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/460410" target="_blank">📅 06:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbqznMDq20sH7VhmMyhmVK091JXv_kK1ySI-Tf2QgDO-UOy7JUtgFMfQVv60VMwotGhr_lQtNeoxSE48SomgqH_oLqeGGv2vPlPAmTPPJoA5t7OZUHNr_RQLv52eIqLYm1WmlXZoBG4hEVL--Dy_JXx9fcmlCMOjnu8W1Q0LfRbx5uPV24o2bI1WizmAFIWtVZXU4aHEBc1JapzsV3wmY-M5yHRsc3pxfjTBSze0MmE0ScK6aFzJEr_tUrZgOmxcHKBebx9iU7OUmsm7OhPjYlopGeJYOSdZvQHdpr3mttRnSGpVfTh0c6WKcXFXc98hwWAuRNAcTm_yjIcRrnAZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ ۳ گروه شارژ شد
🔸
سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲
🔸
خانوارهای تحت پوشش نهادهای حمایتی
🔸
خانواده‌های نیروهای مسلح
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460409" target="_blank">📅 06:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDEQuotNHtQq40bOG6W8qZnS5rG-Sy3FErVlZXbnRSSEgbMBaYnpvHu3vUDdJ6tRHHwxPYyOAPoDNI1usOEJ9LCNQF86S8-8sRI_aJTr7xDCmou_fvc2WJsZuednInbSouHFyZq1tIkoO7pPLe8oPNp0wmq_TLdiao6YogLWJ1WEimkW3fgLn10BPpEAw8IAoWhEbFjEa20LkC65A-n31PUMqO0EAlP38f4iRJy6IcluUs4176wB_jlbQaYGQtuSS_kmynQM4TZQPCJpmmrGX11mPgatXoDxL1aEVKbat1oFKbyFj_Cw1dHDF0i7_QeZnUBM52_YrebB9s58YJ2UZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اشتباهی جنگندۀ سعودی به مواضع خودی در یمن
🔹
وبگاه خبری «الخبر الیمنی» گزارش داد که یک جنگنده سعودی روز گذشته مواضع نیروهای «العمالقه» را در استان تعز بمباران کرده است.
🔹
طبق این گزارش، دهها تن از مزدوران وابسته به ریاض در این حمله کشته و زخمی شده‌اند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460408" target="_blank">📅 06:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
سپاه: ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا مورد حمله قرار گرفت
🔹
روابط‌عمومی سپاه: نیروی هوافضای سپاه پاسداران انقلاب اسلامی با چند فروند موشک بالستیک، ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا که برای کشتی‌های ایرانی مزاحمت ایجاد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/460407" target="_blank">📅 05:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460405">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_oU0qstf6QhF3h8JEp1EtMFl8fkfRCNzoOP0nU0r2uNT2t3V68ygQC9vtMJBCAOL_0uIKnA-fF8Qm1Z5_zgqTdz3fkwnAfHzZdQEOprDMlRjaYC6qJP7SeWJWuCVkc6LAFqYPEbhsn9RwmhyyuiJkaJVIiZgzfhX3wTs4SWlMUGibrQKXsZmX23KfLt3aXDLLqCgrfKncL2M0qixAwgoohuqe9Xnpkbg4T5ElITO8ABf7chb4mh0U2CIiBgK0gS4C9yqQU83mICe8lbyL7U8bWjj5jfvKAISODF-_rRnKQciu874WivIeP_FEjQSFi--11AvfQn7XGdvsheDQdUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5654e5d.mp4?token=Jyoff_o__2LPAPpaGunLTK7BZyJQPplNHDx1bPW0eyR9bSS33JXZgDn6Wsi48d8UdnC7PUqbYY9TQ_OtHMFKcyzLu1blqSGz2Ml7BB6ugL6g1bqO8D-BqV-v39wfWgBwcs0KoL5cnXwU_BXVCJnBMOHnASnFj-fzmzUYW3-PWuoXoQL8A200qedkwVd8NNgsg_oi7NfpPiQJtm8__vk5NPBBcVLuMEKj5SgPhwCh9epuZ5BajS2cycCUkkrtuWK1nE56l-tJvDx_A9nEP57H4hG7UMeLjGXdQydc72UNN0f0jnIWabjgPnWBAPKRXc5pTgqv4eUJ8mvr_vsWxfNLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5654e5d.mp4?token=Jyoff_o__2LPAPpaGunLTK7BZyJQPplNHDx1bPW0eyR9bSS33JXZgDn6Wsi48d8UdnC7PUqbYY9TQ_OtHMFKcyzLu1blqSGz2Ml7BB6ugL6g1bqO8D-BqV-v39wfWgBwcs0KoL5cnXwU_BXVCJnBMOHnASnFj-fzmzUYW3-PWuoXoQL8A200qedkwVd8NNgsg_oi7NfpPiQJtm8__vk5NPBBcVLuMEKj5SgPhwCh9epuZ5BajS2cycCUkkrtuWK1nE56l-tJvDx_A9nEP57H4hG7UMeLjGXdQydc72UNN0f0jnIWabjgPnWBAPKRXc5pTgqv4eUJ8mvr_vsWxfNLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به مواضع دشمن سعودی
🔹
منابع یمنی از شلیک حداقل ۵ موشک به سمت مواضع عناصر وابسته به ریاض در شهر تعز و بندر المخا خبر دادند.
🔹
گفته می‌شود در این حملات همزمان از چندین فروند پهپاد نیز استفاده شده است.
🔸
بندر المخا از اصلی‌ترین معابر ورود…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/460405" target="_blank">📅 04:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460404">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به مواضع دشمن سعودی
🔹
منابع یمنی از شلیک حداقل ۵ موشک به سمت مواضع عناصر وابسته به ریاض در شهر تعز و بندر المخا خبر دادند.
🔹
گفته می‌شود در این حملات همزمان از چندین فروند پهپاد نیز استفاده شده است.
🔸
بندر المخا از اصلی‌ترین معابر ورود سلاح و تجهیزات برای مزدوران سعودی از سوی دولت ریاض به شمار می‌رود که در هفته‌های اخیر بارها هدف حملات موشکی و پهپادی ارتش و انصارالله یمن قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460404" target="_blank">📅 04:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460403">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU39t3xbwJXi6Ihjpj_6lBhWaTepYlInj4NBIE-BMQ2ju4jRNeSfiuYBcEmZUChf-E1ek7ZxP09KOaEZVqXxcnLBX8ycgVTX0HmhXYvqq4eQebmzh-Cc77Z0Fm3MtdCQOb9LaGhO8KPVoNydsFYlYsl3XON_sqHJ18yUQy0H41Mc0Bn5ygkHXTaPSfy720Uj3oqWW37eVRxmWoSpuDAKKNvByxXAcfWl_BvCNEg1taAvamkjV2qqWmFFwmzw4EPbewLvXwy_NR0JkK41aP0UoI1KN5WuvnK-2Da-5RXa8hUkYZ66xk2MrdDDpnkn3K8swbUvHf1D4u2IbiMvmLLfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۵۰ میلیون تومان کمک بلاعوض به کسبۀ پاساژ جنت پرداخت می‌شود
🔹
داود گودرزی، معاون شهردار تهران: علاوه بر وام‌ یک‌میلیاردی، مبلغ ۵۰ میلیون تومان کمک بلاعوض تا صبح یک‌شنبه به تمامی کسبۀ بازار جنت واریز خواهد شد.
🔹
بازار جنت، بهمن‌ماه پارسال بر اثر اتصال برق…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/460403" target="_blank">📅 03:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460402">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S490FfoiBgci4WDXKsGv1ufoV0SRPVJfSe9hwMxweTyby-okU-smgg539Ec_C0IKvEFoT9iDJ_FdwC81lCcR-OWX3G1fET0TLpe0U_-KZLLBBunoUL4FvV3d1s9g9PUWBmTZT5mUyC8vNmyQQnMawJ4PvLT9CwBZ46DB1C8QsaU7OpXgMYs8lN_WiQ2TV2edt97tOKHGMPuKSA3sd6_a-ZjfT-gjsiYmrBBxfpDxSj9usrkndLmuC0Gc_7KOYau4sc6YazFIAlPioce4GOXLn9o7u2VpA5xTajWgMVL1tuN-wkLvX3RaJXzQyzwWXDMiNmzb-l07-ibfRXMxvr4GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی زیرفشار دروغ می‌گوید!
🔹
پژوهشگران هشدار داده‌اند چت‌بات‌های هوش مصنوعی ممکن است در برابر اصرار کاربر از پاسخ درست خود عقب‌نشینی کنند و اطلاعات نادرست او را تأیید کنند.
🔹
این رفتار زمانی رخ می‌دهد که مدل به جای پایبندی به شواهد، پاسخ خود را با نظر و ادعای کاربر هماهنگ می‌کند؛ حتی اگر ادعای مطرح‌شده نادرست باشد.
🔹
پژوهش‌ها نشان می‌دهد تکرار یک ادعا و فشار برای تغییر پاسخ می‌تواند بر تصمیم مدل اثر بگذارد؛ مسئله‌ای که با افزایش استفاده از چت‌بات‌ها برای دریافت اطلاعات، اهمیت بیشتری پیدا کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/460402" target="_blank">📅 02:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460401">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سپاه: ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا مورد حمله قرار گرفت
🔹
روابط‌عمومی سپاه: نیروی هوافضای سپاه پاسداران انقلاب اسلامی با چند فروند موشک بالستیک، ناو هواپیمابر و یک ناوشکن ارتش کودک‌کش متجاوز آمریکا که برای کشتی‌های ایرانی مزاحمت ایجاد کرده و در محاصرۀ دریایی شرکت داشتند را مورد حمله قرار داد.
🔹
این دو شناور جنگی پس از وارد شدن خسارت و ترس از حملۀ مجدد، مجبور به فرار از منطقۀ درگیری شدند.
🔹
دشمن متجاوز که سال‌ها با غرور کاذب وادعاهای پوشالی در منطقه جولان می‌داد، امروز ناچار به اعتراف رسمی شد که دو ناو جنگی نیروی دریایی آمریکا مورد حمله قرار گرفت. اعتراف سنتکام مبنی بر تائید این عملیات سند زنده‌ای از شکست راهبردی دشمن و اثبات قدرت تهاجمی سپاه پاسداران انقلاب اسلامی است.
🔹
در صورت ادامۀ اقدامات خصمانه و متجاوزانه، رژیم آمریکا باید منتظر پاسخ‌های سهمگین نیروهای مسلح جمهوری اسلامی ایران باشد. ما قوی‌تر از همیشه ایستاده‌ایم. پیروزی از آن ملت مقاوم ایران اسلامی است، و شکست وپشیمانی، سرنوشت قطعی متجاوزان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/460401" target="_blank">📅 01:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460400">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مذاکرات ۳ ساعتۀ پوتین و فرستادگان ترامپ پایان یافت
🔹
کاخ کرملین خبر داد که مذاکرات میان ولادیمیر پوتین با استیو ویتکاف و جرد کوشنر پس از ۳ ساعت به پایان رسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/460400" target="_blank">📅 01:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460399">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMM_pR-0SjKqfNQ7f4fDrqFzvNKrViGFI3gcHDj46ZfEmvCRW6Gto1FkoKC8uo_OxIp_cXu9eSzwji7qdKOgeajxxgmvfEsErQsfDK9pszPN4li5_Lq9-CLaYVgE_zkJMi1AuSOWbwJPjDWoZRUs4q2oWBCM_BAhnq2JFkMeNWhjy7OVPIPYFYdD8sc3arrsGBmTEd0NQpB7MtU5qAUhfuFSF2E_euguBARhlCxahyRQFcHx2KvooYYbYy--HzjK9T1dXLr1zivZdXsBrA9K8nMLSw0qJRhiWiOjbS_yY2leFvODvnl8PlNMxomGw5JHgISuEK2QLsmLfVcKgBGexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بار خداداد را سنگین جریمه کنید
🔹
پیش از شروع مسابقه تراکتور و گل‌گهر مشخص بود حضور امید عالیشاه در تبریز، با توجه به سابقه تنش‌های ایجادشده میان او و هواداران تراکتور و اتفاقات جنجالی دیدار پرسپولیس و تراکتور در سال ۱۴۰۱، می‌تواند فضای ورزشگاه را ملتهب کند. پیش‌بینی‌ای که خیلی زود به واقعیت تبدیل شد و عالیشاه پیش از آغاز مسابقه با شعارهای توهین‌آمیز برخی طرفداران میزبان مواجه شد.
🔹
باشگاه تراکتور پیش از شروع بازی از هوادارانش درخواست کرده بود با توجه به حساسیت ویژه کمیته انضباطی نسبت به ایجاد تنش، از هرگونه رفتار توهین‌آمیز پرهیز کنند‌. اما اتفاقات داخل زمین و پس از مسابقه، ماجرا را وارد مرحله‌ای کاملاً متفاوت کرد.
🔹
پس از اعتراض عالیشاه به داور در پایان نیمه اول و در پی صحنه گل تراکتور، درگیری لفظی میان او و خداداد عزیزی شروع شده و پس از اخراج عزیزی نیز این تنش در رختکن ادامه پیدا کرد.
🔹
خداداد که مدعی بود عالیشاه در مسیر رختکن به وی فحاشی ناموسی کرده، با حضور مقابل رختکن تیم میهمان با این توجیه که امید یک بازی ملی هم ندارد، الفاظ بسیار زشت و توهین‌آمیزی علیه امید عالیشاه، خانواده و حتی شکل پاهای او به کار برده که هرکسی از بیان آن در یک محیط ورزشی باید عذر داشته باشد.
🔹
باشگاه گل‌گهر هم عنوان کرده صدای حرف‌های خداداد را ضبط کرده و به ارکان قضایی فدراسیون می‌برد. حتی اگر ادعای مدیر تراکتور صحت داشته باشد، از یک چهره پیشکسوت چنین رفتاری پذیرفتنی است؟ اگر قرار است با بی‌اخلاقی در فوتبال برخورد شود، چرا نباید یک بار علیه خداداد عزیزی حکم قاطعی صادر شود؟
🔹
خداداد چهره‌ای بزرگ در تاریخ فوتبال ایران است؛ فردی که نامش با یکی از ماندگارترین لحظات تاریخ فوتبال ایران گره خورده است. اما تا چه زمانی باید اعتبار فوتبالی گذشته، مجوزی برای عبور از خطوط قرمز اخلاقی باشد؟
🔹
فوتبال ایران سال‌هاست با پدیده‌ای به نام عادی‌شدن توهین دست‌وپنجه نرم می‌کند. از سکوها تا کنار زمین و حالا حتی رختکن. اگر هر بار قرار باشد بعد از چنین اتفاقاتی، چند روز جنجال رسانه‌ای شکل بگیرد و بعد همه‌چیز با یک جریمه سبک فراموش شود، طبیعی است که هر روز شاهد اتفاق بدتری باشیم.
🔹
کمیته انضباطی فدراسیون در پرونده حرکت منشوری عارف حاجی‌عیدی، هافبک سپاهان، پس از بازی با استقلال، یک جلسه محرومیت تعلیقی و جریمه ۵۰۰ میلیون تومانی در نظر گرفت که در قیاس با این تخلف منشوری به یک شوخی شباهت داشت اما اکنون ارکان قضایی باید درباره حواشی بسیار سنگین‌تر دیدار تراکتور و گل‌گهر تصمیمی قاطعانه و بازدارنده بگیرد.
🔹
این پرونده نباید با چند تذکر و جریمه معمولی جمع شود. اگر عالیشاه فحاشی را شروع کرده باید با او برخورد جدی شود اما این بار نباید از محرومیت سنگین و بازدارنده برای عزیزی شانه خالی کر‌د.
🔹
برخورد همزمان با هر دو طرف در صورت اثبات فحاشی عالیشاه به عزیزی، بهترین پیام ممکن را خواهد داشت: در فوتبال ایران، هیچ‌کس حق ندارد توهین کند و هیچ‌کس هم حق ندارد به بهانه توهین شدن، از خطوط قرمز عبور کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/460399" target="_blank">📅 00:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPooPVEWk5l6Y4wiNCNIlPeUemMiLC-ppL6z2SrpmX_k5uXwLapbrrekyD2S0Xw1zwxP2zjvT8U-_QYy16lYH04bCVc28qZkIoRJiwOUm5PrqLQ6Gwa0UNNPA5t1IeIJep-GALUd64ssaKyXKMpKt3pizyAauadF4JVayGsIPpocZP7SEUOv_YuCZJo63j2YYIdEB8Yt0FYAz30q232eptSBAsM920BQjORtGcbW5b0FB7BgMyFhJxJAvi7u6GZ05_gwdhBI_bwxP3fgoBvzUp8XoNYpvEbIMkXXh-pthaSZVnSHasT0rtCLadZ03JTclRmabb55sg0OXSCWVHNDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyVxJtmCp7RM1aYGw7Dt6MqhfN0BTV_Ow0R8yzUnOJr3lzjVl3v9aA638ryExWMiaK4N99aJLHcVsmXxRGIZeejLsXSMeZtOS0bHgHHW5Ptz6SOh8w-xvULDGDX_xS5RGekRmmAy6p0F15WVhvFwP4dV2CT3JsHFc1dglCgFoi2rJZUs26iLQKkI2wP1EJmlgJOeCdZcURFwsIHRFn2QrtPfg1v6T8TpZrVw4fDtzCaS5PKrptTjB-kKbHu5r4wdiQDcXoXYT3JQjpe9oEfJOqr5s9dhRDR827tQR8fVqUfpoZEGuTS2JmNaTuH6mHPpfWEtTPvI_ayq8rq_7LOmCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cL4JBcVwtkOUJvb4j1joNROJ8w_eY8xkgfOUg-LUmSG6go3cniXpEXF1fHZhKO02pJNMv-N49p7pgVg61yRxABIhBbaV9tdk5yYg9dvuesNPZu4xbupjHrNndklcdF65qCx1YdNADphuaKJWaHc13800LQ-Dhqo6TGu1xvGM4i9r8FqHombTwAePSBtetKKhSirPX_doCf9VOkli7gUQrwScPbcszz3YSx6gKW3dF6pRpNgcch35ckrgFOk7uf7A5szQI66NVnbhZeT_qslR4QnfuU2gxzyoAMghVGvJtH6dz3NTkWz609EsTeYd1WYjBFd-cz7NdH4ikVIiRtrZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaI0ULCtM_E7O8LUMEjEM3uefvo0HfA0huolrKVMJrTmdro81M24WzqBRVxOYWbj34xE3a0tAcex2YjNr8tt_269woLRsY40UJBvXMCoG1DneYyPRC8RbIn1iVNanN39q5cl3qgtk0fM6hyNiraBWgQBJVUSPXcOP-1EuGbT4s8JCljNMZvHscd_Zyo2whfepEFLWqq4m6VgV2PXECG-lYz8bG5Ovb0RPRd_nXcLYv6--ehStNGUniOrSHjqsVzO1eTSNLb0nnrC-Fsq4waZ02_BVSpjXkweULsf3bo-ReD0ng6OLwbHOooRbagcQDURzkS-M35W_O6477Q1Ck2zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSaKEK7boJVnBmtUONCFDa3_ZXzle534DgaeH4LCLpFFX_0ItMbnkM0UCsnp9VcfQGPQtJGLuwXHHQVCGNZtlMeKJSzNRipQnUWCmmdjmNn_yg9H3fwTjRr9hMpi76MthTpK-Sm96vqEmdEcNtFFR2scFLtkV5mk9Cefa0EQQF-7CFQm6vMERDV_8mmcVReX9dyqesivukzZanpX64OSvvpQYjzssRdzdkJmJClIFUMapNL9qxIJlYcpQBwLTOdi1cDwH4sjTcVPgjyvZaIqiTlqhb6uwPcvs-v_qEtYZDV0PITqQWxQOqXJkdR80Kx0f_GGFqm-1PVYyAj5HklJcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۵ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/460394" target="_blank">📅 00:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmwxO6q5vxJBvPznzqdv1ss4PrBFU2WydOiUAmFzHBQrBCeqekt7RapnJzAxXj_GyVjwxlmh8sQvYfM6zHYJ6YG_BzN6D8OJbLkzzI8tci5gTiO4gePb7_69JEFjaN9B_TLEJ0nezMQVJ0Xk3yujAGqZCuha5XhRvs4R_equshrSLX71swi9WaBQ1_fBvEp7m-_t5d0qu57uJM1cBTw4EtMSObQZ1POu5hTNwaFw-_XhdLLpTybuKPUlflqLOPqgl2YrhFtXQDkifDsFZ6_aB28xE3UmywitmvOR0YQg5Pt_uQlx4aCVWqbldOCdwn1QcaPmcKrBqVztz6Rvy1zfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/id8YUHRi9v1vOuMKniwUYrp70IgEEbL6_BLpQSAi2Au-_B7M2XRGtiX3KvSDTqdARdw1484klzOIEaJfF4ZVjHVQh0m7GU_O34iCogdmMUIxA12X4dS4n0ElA0MCKw9EwmeBX-erKSvC4kF9YDY8ClbLHBc7vwf0avVqOWWykT0PmO6aNuZo6wAso1u9ndI5CoKDcWa6IDmNASqCR_Zn-7s836kKunqe2LW4L5Zg4FhncCrs1oz3-RIyLEftXHmaCGu4DDYStS2g05qC5zP5qy37wT2yZG0ktnwagSFaZPqBXXiiLB-V7NACvS8oxfjCXBxpbPb470c0kz3ZUaT7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdoqAXTNSRYJuckk9e6LHHDN2JiMG6DCcj68mucQ0ic3JOZHeA0LxIJkTs0jfO80Zwl6aK-d_ZSxZVYvUTz9Xb9mvXEZWxzzMogfADzlcC5PhQTLA612xb2YWfq9o-uPPsB_zY7kfP-NjgHoVPds1GXyko9J9OKAXSdghzcNzj4c7aad7S4v2O5N78rODRQw34RLX_Bs5VhB7GMQZuuJT6MMxkYfQOTjVBYQB2FwxOHlI6RRdFVNByP_z0R46q8e4vOgePHt0J5O8-q_K7Yj-Z8kGyAx3ikKxN_jNHlWVgN3lyoSnvia4OvARHgectC4AiiXcGnZQZLHbwxHHcc6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnBr-IF0-6D8RqtVuSR9_MCgvwK2DrhcodugKbDkZSEzs-_VIXcldJYAALR-175rQ8UuhTLYvfmX_dleQQWNh8OXFhUJyPRGBCtxX8t0R6iDil3-z0850nbNHB6I-1zNS4yuualCZSrLprYMILcFqTqdrPgsk78uJN473rHHP-Khd_Dv6DVhcOlOFWqC3zOwyolysS31gUZVt3OIqnyY9h5_CO-cgWJEYoUAbfF-aDPOzCmMlzZGJDo9tGSlZ4Eny1QklxiOKSE3zcaHMJCXZuobyIBKqbK4aR7360jgqTFGQTIp2SaqTZbQ2mmUCz1k9eiZYrzjRZTn6fx5LEXUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtyBvRXY8mOveQjThTXf1BTfdQZ3nN2hk83dDdScHJzG6G8t4HpXR6FoVFqb6RqbYl5hR43BFt1R6fZetusyt1Buj8_jNlbegxAUlunXnfM32zrILrIPKU1EDrDmZj4nRFmIBrNw7gg5gL9-vECigPJpkS9XranwQ1_K3ZjsS9aF36MVm4TtI4h6BBRoirzBEyihsz7ttwwygJWjhkhqGyvR1_AlaBm-aq3yjs8psogGKDTtSMP1nOSZe_pgo0-5eWe_OyUKERiAiuFaPLE3HIvv8q1ZmWLBcT3EmpDua2js_NvosMB1OE3l5zlLgmGhj4kWxWzo3LlfxNmGRsBK-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhHo34jtiT6qarxG9lLlwKki-AUAjG1lodoLP42TU_lecrAqBIX_nMY-lhEaxPhrb7RDOHzepZ04nxWvCJOnYgbdrDDpcMqZuM4JloqSoB1bm59zxQBDEPlYcx6RVFe5CROgDVYvZ892OP6yCbwplTs-zWKXg1sXZviid2J7J_nLw-sjSS7eNN08TFXLBhRCYXyVFF54JyHXpIECYjUlshwWucVyLzJ-igzqeP0PiK3fsJL0j-Wz3_RX9lxwoGAtOkSwB6Rnv8WAs5jX4f6sCNcSnLwNCL-IJWZs6ekul8kO-M1M-iwlUR472CoM3Cu8aPhnOsmPT10VUmgarCwCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPq--blqLk_on59Wnukp0PFsvI3Q_EjYPJgyHUexApbra99JenPhYyYtVFmglDZeumzfexAfDZ2P0EpfsDpZ2RakKno3coAq0sOHCHmwWYWQQI00A_5y6jTGU3hII_fEGQcMEQHYoBShH2ddQniARGgLTHdA0aYgsBg5iqARmxx6qdmX0LEv-BJ00URn2rqwgsQbpMr4mdJMRexNPpTqKRMJHRt5McC_oTOO6oTnGITwBNEig1KhGyDUh1Sg2_PQN-bbH9c0XNL0CnXsQKdWRJmqrEHn5T8TS6baXSiPuLX10CzjHipXLHBbm-kNNFvA-dVCUqiL9MFhQ--j5i3kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0aHVvUVSX-yEtAE1R4vPsX7kX4Ud5aNjARVmJDwIWkzuVMl35HAI4LD2ipZ1CvQjG9GLqW2cBR6XFO7BmUz0-nb5_JEWpbP-xsTVyn59m2ZPR1HW744U0rRxtImMp6xEMx2bOzmGtf4h42ugwlQqCTVL_uz7tZnz2BqOR3EnTte80UDcFPykxsgEVTJ9xedumxZB6w08lIvb1kY6_CtGBOtfbyuTh2u_1hkMHUNc6blnblgek7lIvhjWpG8mXz_rCx8w-BHmAcZnhgxVsluWwMlIyQzG5HS3c2r_J4AEzu-Y_oTxRKGM0K5AxOgrCatIsfy-la_oKdsrjfrVpExnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2XcxWJywJdfRuj2S29fxv_ykEzDlqWgOqmzR_zpfRHY8U_TvqYW8YadQrXcXfSf0XV5aoL8oyLwk7LTrZJx8YMqZJbJuivx7wIZeluOs4biRcXSlIXwd0EVMXHvn04G0dgrOhn3QopgNGt-ULCa1hCFniUcdULvrJPcvceMlxFuLHMYPMqB_agu4-T__axsEXgCWE7E4bMdVZ2MNh22bpQOJWJVq132OLysy8vszsXVKTtMRgxDN4AZ16HLCaUGiESTkmxRdeAEp5yXvo9qAMjFIjSZSTZm-C5LK9KnA2vXHLJMOltjn7hXPN-gQkvvkUTdEcabMDaMNjnt0cWc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Odh_NfHl4hxp_BBgWRzZMyo6GdtsDBYXi5X0U4_ocVAqjSF4X9UUuRxcVXW-REXAFzmZPnqpGFzDgEEJHEiJjQbx7a6FsJMXJCSSxSLiF977DHu9J8CnN3a-YiwSnbtCj5lpEy7_dQwRzG_-rYknXmZ0W1qfiK8FxfCFSaEkWRrKUkS5Wcbfo78y7GsWkCL2290RfTVsOGG6xL7i02w-XvMuSapdTJRLnru-ik9XymnS-SwO37TzSjma7v1pjN58KmEl8RliWjN1SfuCkOi9BoFVvlaoDja0C8XMi75JDT7OrJp0VJf_qFi1Zi2b8XnkZSbrZRHJS-lfOJFZV3hbtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460384" target="_blank">📅 00:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عناصر وابسته به امارات در یمن تارومار شدند
🔹
منابع یمنی از کشته شدن حداقل ۳۳ نفر از شبه‌نظامیان همسو با امارات «العمالقه» در حملات نیروهای ارتش و انصارلله خبر دادند.
🔹
این شبه‌نظامیان برای کمک به نیروهای وابسته به دولت عدن (وابسته به ریاض) به استان عدن اعزام شده بودند.
🔹
محمد سیف المحولی، فرماندۀ یک گروه واکنش سریع در گروه نظامی العمالقه، جزو کشته‌شدگان است.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/460383" target="_blank">📅 00:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec89aea0b.mp4?token=i43X2W70ce4pkUovuJdeeaRELALPg_ct7nbz7VFluSgCP_wOPYFWwOjEIyKGi3DkWkFXL3Doerkli1LgijJCqVn3IMeJfTVQHkjdl9qjzP6kYHq_UlmnVKWCluT0qjJNXlKuYibgN1K_bDRb8V1KYbOCVV5ijLe6_HM4fkJFBfcwr_79xG63So28spSjbYG6fqPY7ALq_bkdZ5hFzCQVwNb3F6Xn3x8SDtiaVoLEv2hGtBxaKOQfJJkVGpwflV1VEeScOOn-fZQXLA_8zJQNQf4bBEDkeTz_In4fukv3feDirysldCBXbI_P1aWo3tD3Eo3W5v4NM7n83k9me22guw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec89aea0b.mp4?token=i43X2W70ce4pkUovuJdeeaRELALPg_ct7nbz7VFluSgCP_wOPYFWwOjEIyKGi3DkWkFXL3Doerkli1LgijJCqVn3IMeJfTVQHkjdl9qjzP6kYHq_UlmnVKWCluT0qjJNXlKuYibgN1K_bDRb8V1KYbOCVV5ijLe6_HM4fkJFBfcwr_79xG63So28spSjbYG6fqPY7ALq_bkdZ5hFzCQVwNb3F6Xn3x8SDtiaVoLEv2hGtBxaKOQfJJkVGpwflV1VEeScOOn-fZQXLA_8zJQNQf4bBEDkeTz_In4fukv3feDirysldCBXbI_P1aWo3tD3Eo3W5v4NM7n83k9me22guw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه تراکتور: اعتراض خداداد عزیزی به عدم اخطار و اخراج عالیشاه، دلیل اخراج او بود
🔹
باشگاه تراکتور اعلام کرد: خطای شدید امید عالیشاه روی پای امیرحسین حسین‌زاده در شرایطی رخ داد که بازیکن گل‌گهر پیش از این یک کارت زرد دریافت کرده بود و با توجه به شدت خطا، می‌بایست با دریافت کارت زرد دوم از زمین مسابقه اخراج می‌شد؛ اما متأسفانه داور از این صحنه به‌سادگی عبور کرد.
🔹
در ادامه، خداداد عزیزی، مدیر تیم تراکتور که نسبت به این تصمیم داوری معترض بود، با تصمیم داور از کنار زمین اخراج شد؛ اتفاقی که در نوع خود قابل تأمل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/460382" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460381">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مذاکرات ۳ ساعتۀ پوتین و فرستادگان ترامپ پایان یافت
🔹
کاخ کرملین خبر داد که مذاکرات میان ولادیمیر پوتین با استیو ویتکاف و جرد کوشنر پس از ۳ ساعت به پایان رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/460381" target="_blank">📅 00:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460380">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
تصاویر جدیدی از رصد و اقدام نیروی دریایی سپاه علیه شناورهای متخلف در تنگهٔ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460380" target="_blank">📅 00:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460379">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i62wDgwl16IuEKrGuaGxa_6ganiJUKbiQLJuoKAWu6qsAcDTLeXComWMuZK9QaAmMiqBULC6E5SEQLhx3WvDmlAVKApd0n8pjL6ydGGVB3pVKltXJDPxIrS4SUfAfEox6wjATk_AwZfFWtx53sx2JL0OtuOMkJH8KNaj3Rb7WfvyHhJ_9OSTjE3GG0uqB0FvYthu7eMHVXHEFkIXVHch-Nj74llntzvo0HH5yp1E0ch0ec1uIzalSm2etvWEp58g6LOsJYK-Cu2AGLVQ_e4Sz6lZo8wpn55EdSKCfOcQUQ8-cz_w62EYo_ar6GpdxuE4mHeJ63-3_sxXQy3pjTlpWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هیوا»؛ تازه‌ترین برگ از یک پروژۀ شکست‌خورده
🔹
افشای انتقال یک یوز ایرانی به‌نام «هیوا» به مرکز تکثیر در اسارت و  ۱۵ روز نگه‌داری در این مرکز، بار دیگر نگاه‌ها را به پروژه‌ای جلب کرده که بیش از یک دهه از آغاز آن می‌گذرد، اما هنوز نتوانسته حتی یک یوزپلنگ را…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/460379" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460378">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGbfkY5CafsbqwLsA3hw-EBb3tnKlT_kc7WwqmsswtyRbPgbs9m-8feead3toTsNkneM9ZEK9dzjjATgxHtE5BU0OSRHvO2PeJb65AljmGW3MUCuCBdD-5BQR_W6HgzZK0ULrLKdfsvCd0y5maxcuM2n1HzsT4-TXhMo0VviiTs761sHVdGDVZZFDpIPtdW8B0rjyUVy9DVI2vHp_LsYcDSfdXh5nB_9iILlTqjeHpQtb4IAD_cDhnYZrNzw5Mp_4zI7NVHQBuk6F_t2z1mMBVdBshCAUQCz9rRNmI0lWkh9FyQGrp3SlM-JqE_TQwomhszmjO36eMTthgn-oLbTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
🔹
طبق اطلاع خبرنگار فارس، تمامی افرادی که در این کلیپ حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/460378" target="_blank">📅 23:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460377">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f867ea1e.mp4?token=aAf0mlcW9Svjh7odjwznEoXNte6MhuulvU80SJyiiWy4KpPaCFnrV6Ncrg6pcDuBhL01WS0szAbxbStvLfDzV2QRU1l-EdlgnmlxPUMZeSthj6-FyKtzCwgMfxHNRqWql1iKr5kYjC7khLrnta5QxTYQ3Ygvq_NYM_VHzbgh72Xp4bjkHzljbn4UHS2LifSCGYjMzt4ERNXvgvUswqiK6GWdTxt3JR5lV5SRuB1G2x8dLpmTrlFhuQeHFHEGnpB8q3IfGV2dU8Z1KPGl62yqn86t_4jErwpFNtaLSzMhyAMSZtAPha42MGeY-JFaGCIFDaEIBx4l71sPJOebdS3yOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f867ea1e.mp4?token=aAf0mlcW9Svjh7odjwznEoXNte6MhuulvU80SJyiiWy4KpPaCFnrV6Ncrg6pcDuBhL01WS0szAbxbStvLfDzV2QRU1l-EdlgnmlxPUMZeSthj6-FyKtzCwgMfxHNRqWql1iKr5kYjC7khLrnta5QxTYQ3Ygvq_NYM_VHzbgh72Xp4bjkHzljbn4UHS2LifSCGYjMzt4ERNXvgvUswqiK6GWdTxt3JR5lV5SRuB1G2x8dLpmTrlFhuQeHFHEGnpB8q3IfGV2dU8Z1KPGl62yqn86t_4jErwpFNtaLSzMhyAMSZtAPha42MGeY-JFaGCIFDaEIBx4l71sPJOebdS3yOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌ جزئیاتی از حادثۀ خونین بلوار وکیل‌آباد مشهد
🔹
رئیس پلیس راهور خراسان‌رضوی: این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
🔹
این خودرو با یک دستگاه خودروی چانگان که در…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/460377" target="_blank">📅 23:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460376">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a5fdd274.mp4?token=XkGrS7TGQHTOSb7LrGM-ZtTJid3fQIDeIps8Sq7-82q-ERay-ZKUiRefewysty_1NUz8vSvMzF6m1V5WDEmpiOjmkXJBRICFja8HgFSvfq6WmPuDKijD1c96CfvgtvMkcvTi9tgE6J-HZIxCwwtHVXa4il7zHT52D2rtYBc5JaYpGReoyYPm_kVb9mwbDPL-ZVLCitl9aAqaMOOCJBjl-ocoVixm9KBGrgeiwBRu4ORHZXdHGlcWMvMf1V53e5mgRX69665yiKYeVGZ034SFa2aDK362xLHvbggVx8gkx5b73ZCo1b1qyA7LyWv4saJPCSNbwE6vYAeFjH0uitCPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a5fdd274.mp4?token=XkGrS7TGQHTOSb7LrGM-ZtTJid3fQIDeIps8Sq7-82q-ERay-ZKUiRefewysty_1NUz8vSvMzF6m1V5WDEmpiOjmkXJBRICFja8HgFSvfq6WmPuDKijD1c96CfvgtvMkcvTi9tgE6J-HZIxCwwtHVXa4il7zHT52D2rtYBc5JaYpGReoyYPm_kVb9mwbDPL-ZVLCitl9aAqaMOOCJBjl-ocoVixm9KBGrgeiwBRu4ORHZXdHGlcWMvMf1V53e5mgRX69665yiKYeVGZ034SFa2aDK362xLHvbggVx8gkx5b73ZCo1b1qyA7LyWv4saJPCSNbwE6vYAeFjH0uitCPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی پزشکیان آسانسور را ممنوع کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/460376" target="_blank">📅 23:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52e71799c1.mp4?token=HPZDeoL0aahsFzrTfmXacbhWbbGBQ0N_AoN_9-40-MqwWA55stnEvyGCWPiszLwKsPnAdiXz-GVuf4pUfv3LbuHeG10srCf0qFjw3RP_7MOxPbz_WDxNbRtN9iWPVPe-xb8Hj4Gmmesd5kXwIPOZ21sBpT-kdoROWDNKOHsGnd4xyZQzSaqmCDWO0dP4ZBUSf1u-GxPZfRJShcPTtii1zOkLsgr0dTXdAB2zq8SDcTpaZtKEmx62cWtsIwN7gSfnT1CD2LAVaDNsmNYz_w5xXzFcBMQysyCYgY79GgbiwCZ_64ip2bJQzK63teDUBm0FsR-ws-Lu3RBMaTQsNCqFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52e71799c1.mp4?token=HPZDeoL0aahsFzrTfmXacbhWbbGBQ0N_AoN_9-40-MqwWA55stnEvyGCWPiszLwKsPnAdiXz-GVuf4pUfv3LbuHeG10srCf0qFjw3RP_7MOxPbz_WDxNbRtN9iWPVPe-xb8Hj4Gmmesd5kXwIPOZ21sBpT-kdoROWDNKOHsGnd4xyZQzSaqmCDWO0dP4ZBUSf1u-GxPZfRJShcPTtii1zOkLsgr0dTXdAB2zq8SDcTpaZtKEmx62cWtsIwN7gSfnT1CD2LAVaDNsmNYz_w5xXzFcBMQysyCYgY79GgbiwCZ_64ip2bJQzK63teDUBm0FsR-ws-Lu3RBMaTQsNCqFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پای کاربودن کاشمری‌ها در ۱۸۹ شب ایستادگی
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/460375" target="_blank">📅 23:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460374">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108f6a8d6e.mp4?token=ajtx3K1Jd_jg29thMbcRsKilkPzfX8CxAeoBm662nfxMl704fMOJnAKKhRWbnhKY5yxzCbXu3v_CK13eZ1w9EDcbnbTkx7FDqNiul9wcAz0Pht5JSzq79LOksigsi19U6Q2jWQBnJQY5-YKsgPfmx-aSNUiqgky0CzWgQBLPdB7Bg00JKZC7SQ3hgfY4DDrbCdpCJYIbySDk2lKFWrx3Xw3ukxWAb5xAu5WAXNOfo7zy6MRoHbDp7FLQ5yfFXVfMksrBUMiSdulUF6OTSEG21AZZSSbQHyzpwqBZ7RMSFGAc4Dn3N3GO-VRl1gVQgK3PnV_1zpDYFqlbg6GTUfG-jWyjOnpTt9dTrsV1Dle2ki9wjCzbh9O-1_KUI3vO92zFSt9o50_bLCbbqzeLaErm8t64EWffGp86SoMit6Q_-2CLX7BzEMOBCezYwmNvkPfQ5IV3HzXqHJJtqkU2C0oJMm8smxUWmukB4AWTYBw944DHOrY37gKx9fKYX_Ed41_p1cC26aONONul97wgtJUVsSVcg_g8hxNcNZb0VX4SnE-gdWjDEZd06r90yuaNx44CX7zxtoW4OcAkI-EKVOyi862UCsq27gmQyMRaXRUxhfMHotqqFk6DodoDTM_pEiIljnQihOPeLGOClx6yvjFkR_Qm6dwtdvQr7S96k5H8l6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108f6a8d6e.mp4?token=ajtx3K1Jd_jg29thMbcRsKilkPzfX8CxAeoBm662nfxMl704fMOJnAKKhRWbnhKY5yxzCbXu3v_CK13eZ1w9EDcbnbTkx7FDqNiul9wcAz0Pht5JSzq79LOksigsi19U6Q2jWQBnJQY5-YKsgPfmx-aSNUiqgky0CzWgQBLPdB7Bg00JKZC7SQ3hgfY4DDrbCdpCJYIbySDk2lKFWrx3Xw3ukxWAb5xAu5WAXNOfo7zy6MRoHbDp7FLQ5yfFXVfMksrBUMiSdulUF6OTSEG21AZZSSbQHyzpwqBZ7RMSFGAc4Dn3N3GO-VRl1gVQgK3PnV_1zpDYFqlbg6GTUfG-jWyjOnpTt9dTrsV1Dle2ki9wjCzbh9O-1_KUI3vO92zFSt9o50_bLCbbqzeLaErm8t64EWffGp86SoMit6Q_-2CLX7BzEMOBCezYwmNvkPfQ5IV3HzXqHJJtqkU2C0oJMm8smxUWmukB4AWTYBw944DHOrY37gKx9fKYX_Ed41_p1cC26aONONul97wgtJUVsSVcg_g8hxNcNZb0VX4SnE-gdWjDEZd06r90yuaNx44CX7zxtoW4OcAkI-EKVOyi862UCsq27gmQyMRaXRUxhfMHotqqFk6DodoDTM_pEiIljnQihOPeLGOClx6yvjFkR_Qm6dwtdvQr7S96k5H8l6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان خاموش‌نشدنی شاهرود در شب ۱۸۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460374" target="_blank">📅 23:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460373">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vACTbnZrrI14_EHN-o1_cloOign2zJwjcWhdsP8BqUQGJCReO_-AHJeAZPAISktvAH-Tgz_QDqD8Bra9XWgHJLNmBJMb8xlLuc7ngSigGO76XabhBN_taTfQO3_1UDspVwv7wFyHSZPL9BGkjUlke3Xc32u8RwzlGKO_Ln77UNZW7bjLDEsOcTgTkvrkLH--0F_aYFvgiOhi6RfP8m9QOkvFoYu4ynMUJeniNCSWsedTNnvVwcIIHU1pv-0arVFStDTHCgo4rqtnr2qJeVN376TIR4g6l5TabkVqHBhbauhjBtFQBlM2_IIrpZNVm20tP0j2wyhBX12lWa9q891MkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه: روزانه ۲ تا ۵ شناور در تنگۀ هرمز هدف قرار گرفته شده‌اند
🔹
علی محمدی: در ۱۰ روز منتهی به ۸ شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.
🔹
حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل ارادۀ نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/460373" target="_blank">📅 23:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460372">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc4c5204a.mp4?token=K7udbajEcq5v-PDC7IG-ld0cStkYhFsCiZ57-SQBZvsmTsJuuYCrXrQ5WziqMRrDf_vW8_vyjS3WomWqcqby73vMUCvGMQQL5ZYAGJy73He8MEdL1N2D0DE34JIFWZZZAXMaDdB7h48GNMzVyl44OC_C7fdKurPhqvuXEspXs40kLhgyzee3gRa_Lx7ePb8OEYRFLIMEZ1HPxZf_O7sINTV5Oz0yrV4aoEdcU-zZBAUGpLQK-qNJuM82y1xcgu7Pwl0RladoKpuoGSf-TAOfvXARtIxVMrnJRIFbhgLqW6dr8q6zNlhkCgu-q4P3gZNY1gvo3QAsP4qe7tzNwHFaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc4c5204a.mp4?token=K7udbajEcq5v-PDC7IG-ld0cStkYhFsCiZ57-SQBZvsmTsJuuYCrXrQ5WziqMRrDf_vW8_vyjS3WomWqcqby73vMUCvGMQQL5ZYAGJy73He8MEdL1N2D0DE34JIFWZZZAXMaDdB7h48GNMzVyl44OC_C7fdKurPhqvuXEspXs40kLhgyzee3gRa_Lx7ePb8OEYRFLIMEZ1HPxZf_O7sINTV5Oz0yrV4aoEdcU-zZBAUGpLQK-qNJuM82y1xcgu7Pwl0RladoKpuoGSf-TAOfvXARtIxVMrnJRIFbhgLqW6dr8q6zNlhkCgu-q4P3gZNY1gvo3QAsP4qe7tzNwHFaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌پناه: ماهانه ۵ تا ۶ میلیون تومان از حقوق رئیس‌جمهور صرف مدرسه‌سازی می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/460372" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646bd8b55d.mp4?token=uSpcauPgG3xMEm601Hfulj83wJvjkZtReipPU8EyoqniG6fjHrC3EqpZFTne3AGzqeR11HAxkkoIDOwCTYnCNgj6cGtZkBqi4F6_Azy3Q25VTCv-H4c7rTRQBjrzbqr1vtQ_jlPq6ClOROkCnOy5ER3Ycgn3HzeIxoGNJV9eDuuDAmXVZRjkuFMoPE8_z9MQds0Xzm3cYPZXYsR2Q_wSr1AdS2mMG08Ubcr3AA9UCCB-TF1T_m8oITH0jwIzjmw6cefmhPeSoaIr9JoLmirgaWH_D6POTIr1hSZOTjUaFEt0vmEeNdBkViDHVegPndmQP8gwdpk7DQw1YIny-hwSjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646bd8b55d.mp4?token=uSpcauPgG3xMEm601Hfulj83wJvjkZtReipPU8EyoqniG6fjHrC3EqpZFTne3AGzqeR11HAxkkoIDOwCTYnCNgj6cGtZkBqi4F6_Azy3Q25VTCv-H4c7rTRQBjrzbqr1vtQ_jlPq6ClOROkCnOy5ER3Ycgn3HzeIxoGNJV9eDuuDAmXVZRjkuFMoPE8_z9MQds0Xzm3cYPZXYsR2Q_wSr1AdS2mMG08Ubcr3AA9UCCB-TF1T_m8oITH0jwIzjmw6cefmhPeSoaIr9JoLmirgaWH_D6POTIr1hSZOTjUaFEt0vmEeNdBkViDHVegPndmQP8gwdpk7DQw1YIny-hwSjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه قضائیه: مدیرانی که نسبت به اهداف جدی نباشند از دستگاه عدلیه برکنار خواهند شد
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/460371" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FV29y4Dy2q7_sn6jhi_0t--DFravQ9t6dC5yXgmS3SFYeSl7tISh0f8fqC4BARN7HwfSc8APG5TlFoeL9hgbTucRxHSoWJqnR6R9p4Qy-vrvUz5RwIJgrpQ6Zk-YNREFI69drZFknUiVfPWJpYQSZuHuVFDfGZ_cW8Lv7v28lkWpo3EZYbGfBodoJG-srtkB0Q9oQGu0kCEt24g5QHyvZo1S-_ngZiYD9rXEJB7cVksbvnvyxdYaP81ZHOga-TDrmT-QtCgNb2pz8yweuw8gI4-l2_ZhtyI3ChTHRvFY3Ae6wdXyUR65ZXYC5mo7iuXgIu3pFRYovhk8IsfJAkgi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnmMuXd6PpJUHByAWWZ37-p3UnE91DRCfWwTBb3f4FyCBjEzV27A9Knsj2ErorgasmkfX8sjrR9r8IJ5LzqQNCCJ1i8BESrQEQ1y0MdxdXtUnZRWhMTEI9st7eKMWhT2pa5R1LJq4Nd3FesFWUJ_jEzs8sS5MLE5_dZWjTAeiyDcuplXJEZZan5EttXhinaZo-Kul7d0PUUGhrLRwRa7u0W3omEXcbuF4bxdWdhl0V6Ep_mkal809yDfI8CE2SMqidFOwsJn5KkTdpacCsbOqW-x70qZinb00ejCGPIdbkIbixj-QcqYssSTglFbDWpG_bvGkhxlZ7F41g1fhG_hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOP3CdkR8iYV2zGQwF-MYJGBvYUvcx1G6zPonzlMgmirwYlvApU3jHfpWCmHBh35_yCGDOKlOfmhXcLz2yYR61FWkkpCEUrhgcgeUJpIE9rwbW7O5wm4K2vsW8fxSNd-lY3c6_w6RGgPF8sCa5oEEIdBIPxahw55G8tr8Q1jJx39Uadm75qQQWVP2caNaxBupyDB7xIZMkLTN0FS8EAOpThV2J6LwGsQ278EYhxUTUbGW1uEd-lE4ohZ7i9p68PK4b772lq6UYuPEkW0TqMwOwohTgTuVb1JbrkJzshrI4qn0nERtsborVn51Vgcit80aGd2QFHeAE1IhJ7yrwum6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وزیر نیرو: دیگر قطعی برق برنامه‌ریزی‌شده نداریم
🔸
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند. @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/460368" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2L_z2u7VBAp922DpOFIx2DAjVXP5TsRotZu2ShKngnDA0KvH5LE7dj2XmrB0aopslETsOA8x6Sy6DEoHV-Ee44zRi-eeqpa-ZA5gHBmLLpXeS-4YFsK13QWNeSKuhnqLRRw2YxaJbjTZDs8gCKZ3IZu2JbQNeWeE9tOSAWfFgXBPvetwjKDRVIftagMCGP5TXpVvnf04BgwrXVwBomjaE_5WgfLYNxHnDg-fhoMEAb3zp9rQg6W4GSyajkxNhmvFou9BCMhe97lXaQaWxSAO1OkGM9nDXfA8pJWuCwGBuJJtXUDDG6P2J2AZu45kVLEimndwVLWpElBWibWC96WtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcf35c0a4.mp4?token=NFrF3nelmy9tOwb3NA71zSiZ8dMbrmTEu8PrlTL1oxEuCzwzMCk7PY7K1DSZaZ5lYREVFv0QwtGLcOtxT_GQiy_roWjiq0gUjfcyjK-8i7LuiSBbscHUxbqi2h27wPfYZSYpy0IMqG_kxtuk4zxmpyv7812NfGw9nIXgzpwdjJKAr31vdeqhoweSzlwqdPz47ifGoP5iB7kTEyGiT5VI7vg-dUgMvPJFlA6OFgtrnWQS4ekmZLc4Em5VBFCerOwbaSw3W_NxZMw5SQ4lEaP1KRy8yCvqv4FGm4lYGT1jkkSA-rqo5R5rOR4D0V0jO3OXEy1cVLyRMVzNHhX5XU_ikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcf35c0a4.mp4?token=NFrF3nelmy9tOwb3NA71zSiZ8dMbrmTEu8PrlTL1oxEuCzwzMCk7PY7K1DSZaZ5lYREVFv0QwtGLcOtxT_GQiy_roWjiq0gUjfcyjK-8i7LuiSBbscHUxbqi2h27wPfYZSYpy0IMqG_kxtuk4zxmpyv7812NfGw9nIXgzpwdjJKAr31vdeqhoweSzlwqdPz47ifGoP5iB7kTEyGiT5VI7vg-dUgMvPJFlA6OFgtrnWQS4ekmZLc4Em5VBFCerOwbaSw3W_NxZMw5SQ4lEaP1KRy8yCvqv4FGm4lYGT1jkkSA-rqo5R5rOR4D0V0jO3OXEy1cVLyRMVzNHhX5XU_ikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده نیروی دریایی سپاه: فریب آمریکا را نخورید؛ هر تحرک مشکوک هدف قرار می‌گیرد
🔹
صبح امروز ارتش تروریست و متجاوز امریکایی در یک اقدام وحشیانه و از سر استیصال در بسته‌بودن تنگه هرمز به ۳ فروند نفتکش ایرانی حمله کرد که خساراتی را به بار آورد.
🔹
رزمندگان نیروی…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460366" target="_blank">📅 23:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZMGlIJ2XsspU4Ol887K2rOQr5RXEDEbGpzxy3devN_1_zQT21PaS45VRSDMdf6kUy76YBXsB32XWOvfenzpP9eJ1eNgLoigo6PF1RIuGIia6FPhJD69xF1VqD15aLsQZFnVc2kFHkQsSK7nWrfWvQMlTWUE84i12GUFMtAWzF8pWLNzwUINATEtUdZraKUiSsiV3HgdVI5NlH7CFXTk_8wPYkAFWlD1qM_CjsgTw4EzZae2UFvkjymjEPcsDH-JCYKJ66YcCLNEIwg2VZ8Wq5OrmDxpN_2ImxgmgWaqPfDPuOjuY-TvER7CmNozcQAeW9UV7drnLh28CUnFpGzCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی دریایی سپاه: فریب آمریکا را نخورید؛ هر تحرک مشکوک هدف قرار می‌گیرد
🔹
صبح امروز ارتش تروریست و متجاوز امریکایی در یک اقدام وحشیانه و از سر استیصال در بسته‌بودن تنگه هرمز به ۳ فروند نفتکش ایرانی حمله کرد که خساراتی را به بار آورد.
🔹
رزمندگان نیروی دریایی سپاه در پاسخ ۳ فروند نفتکش در مسیر غیرمجاز تنگه هرمز و ۳ فروند شناور وابسته به امریکای کودک‌کش را در مناطق دیگر مورد هدف قرار دادند.
🔹
نیروی دریایی سپاه درپی این اقدام به تمامی شناورهای حاضر در خلیج فارس و نزدیک تنگه هرمز اعلام می‌کند:
🔹
فریب ارتش تروریست آمریکا را نخورده و از هرگونه تحرک مشکوک به منظور عبور از آبراه های غیر مجاز اجتناب نمایید؛ در غیر این صورت مورد هدف قرار خواهید گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/460364" target="_blank">📅 23:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1986a916fd.mp4?token=Y1DEX9XM4CSmpuaFw0P0E3uOthx1Uz0uR-dpgyh89XHxaW-hi3uuy6wUSmTvmt9f0hTSKWbigo8Wu4RRVjKd2NFdKm-tOew8SRkl05NAIKnKVjVDSJs91_6nW4_5OFsbozZWlaMtFTryC3rQxGj0KE09oOX-ZfxTTSo4lUq_YD0gJ3TPMokA4EXiHdHh55_IsqP09jwZEfWrmOQMSnuNdSWMyA1Yb4rvIdvfUExF-Q5oqpW7Sm6pgPYv_UK8ZkWH_DUTrZHzV92CpBZt60jUcFaerHHrBbBofvtVqMZ3NNpYu8ekN1O6dx7djLUIfNdXawUeot3BBTzj9uqW9xvo9xSqN7zMcYhEIO9ej1VFuV7viI67bF259sTsjyhSLCNKCcv9drC5CVbdtOvCMsyq40HChDz3EsnMDkL1AqOYreP3lyKsyNUW54dKlm8frN_3plQoWH8gpJR146u2pY4OUO1-tHVxrHz3wT6RiTTntQdjU6qXOIIICW6SgnjHAF4Kts1-ieEpMRqGOd40RrOAW1syGDLRiugPtx2mpnJo-3qC1e87axejjDL2oVo51Rs4X5mwC7_3T3FEN_UwkArQIdZWFBI0fIdX_QnI_ah2XYSTCoUtyUxkl1w9gltU2HmuKcvvA-doWhDeZen1Tq_2km7Om6GLgpR3E-kVBpRz4tE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1986a916fd.mp4?token=Y1DEX9XM4CSmpuaFw0P0E3uOthx1Uz0uR-dpgyh89XHxaW-hi3uuy6wUSmTvmt9f0hTSKWbigo8Wu4RRVjKd2NFdKm-tOew8SRkl05NAIKnKVjVDSJs91_6nW4_5OFsbozZWlaMtFTryC3rQxGj0KE09oOX-ZfxTTSo4lUq_YD0gJ3TPMokA4EXiHdHh55_IsqP09jwZEfWrmOQMSnuNdSWMyA1Yb4rvIdvfUExF-Q5oqpW7Sm6pgPYv_UK8ZkWH_DUTrZHzV92CpBZt60jUcFaerHHrBbBofvtVqMZ3NNpYu8ekN1O6dx7djLUIfNdXawUeot3BBTzj9uqW9xvo9xSqN7zMcYhEIO9ej1VFuV7viI67bF259sTsjyhSLCNKCcv9drC5CVbdtOvCMsyq40HChDz3EsnMDkL1AqOYreP3lyKsyNUW54dKlm8frN_3plQoWH8gpJR146u2pY4OUO1-tHVxrHz3wT6RiTTntQdjU6qXOIIICW6SgnjHAF4Kts1-ieEpMRqGOd40RrOAW1syGDLRiugPtx2mpnJo-3qC1e87axejjDL2oVo51Rs4X5mwC7_3T3FEN_UwkArQIdZWFBI0fIdX_QnI_ah2XYSTCoUtyUxkl1w9gltU2HmuKcvvA-doWhDeZen1Tq_2km7Om6GLgpR3E-kVBpRz4tE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تروریست‌ها چه نقشه‌ای برای رسیدن به مرکز ایران داشتند؟
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460363" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJLmti2CjHBYviSdDL6CHBTb346gTK74k-T4o-4iUqjzwBYywKfA9o00cdqC29yiF6v9XrJANV5DJHMw3k1WA9PkSWtvMPltvGMunokE7BvH6IvUqaHTyJEOdEqmHGFcFsByJdKLVI151RpoGZBeFfNxdRs89_YAyEp_zLOBzy5wf9haBuGzp1B3HZyTDptXa8z90m_HqpvetJLO7UC2k3N9nXCwSF2ejNAqQph5P2hl43fOQAcUcDhyQeoaGoRQrqYBPtVrFF-xPqEVPJFUJd44LtZCKl27DWeAUsKP2QMBiQ9RXW-iychgjlf_Vx09tLkhKR-l1vzqJmlq6gW-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحشت نهادهای امنیتی آمریکا از گسترش جنگ با ایران
🔹
شبکه ۱۴ اسرائیل شامگاه امروز اذعان کرد نهادهای امنیتی آمریکا، به شدت نگران گسترش جنگ با ایران هستند.
🔹
این نهادهای امنیتی ابراز نگرانی کردند که احتمال دارد نیروهای مسلح ایران تصمیم به تشدید و گسترش حملات خود بگینگرند.
🔹
یک مسئول آگاه اسرائیلی که در جریان گزارش‌های مراکز امنیتی آمریکا قرار دارد گفت که «این ارزیابی، مبتنی بر واقعیت است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/460362" target="_blank">📅 22:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460361">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9oAU93J9AopzGjY7rBFMbKInjkFIBykZUWqWBCmEmj3TQLerX8cStgcYWp71vLYYqXRJnF7LH4FVAWiamxVW6TvvO0HrshNoTlCSztF-kYnhaYNed0YqR3RzCzuW8JEMImTDqaOsmorwnrJJJqxrqeE6hunVmAHdV8suqiMBiRBJLexvDqM-Yl16L3hJt4yyXLn9DA3tPrrRfYjnH-ADngoCshMa37aMDAD4ytLkt_DK192wPbX_PamoGTVFK191xW4JS0oM9nvbNoKNsSlFW8Wre1y8wPI8kb29gQvSgWHhjPoYJSGfBNu8KQm8uNhvFY1Nzg-TLA8owigGGfegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌  ۱۰ شهریور؛ روزی که خبرهای خوب از راه‌های مختلف رسیدند
🔹
«بسته خبری امید امروز» روایتی است از اتفاق‌هایی که شاید هرکدام به‌تنهایی یک خبر باشند، اما کنار هم تصویری بزرگ‌تر از حرکت، ساختن و ادامه‌دادن را نشان می‌دهند.  پروازهای عبوری دوباره به آسمان ایران…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460361" target="_blank">📅 22:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460360">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1931c9227a.mp4?token=U41nFbLZkeaGtHvasw2w--SEA-weS5terArXYEWQ6hOSoOMTY-Y6OV6jfp5ggNlTZo-G8nPIwEcOYcym68lPcCFqS4Wjat6iA8aMjIEk3-5VI2mMd54bX0C6cZ8qS-JaNk47_IK2oeIlgjBzGYChl7mbjKnpovnX31S6pLj3QYmWvPynp48T4-fCf7zdEFXScZGfKhZG7CPRz9-aG0am1Ayd8QYQ02F5De28xyGfJKL79nPSWIduYSonHYSw-39PoyUlVdl80u2P9rX-u6SIEWxQJnZdNLchJqgJJausMmJEJwBlgtZ-BzcVh7gMogdpJ15j80wZU1VLuW2Zvr9WilhPqLXWPFs-gdlfyXhXXko8lqaE9GkxGv5w7ej0ZI03i5AYuoO4TSHC24UM0YSV50mjG4IPvi-cvOZy624BhAg2464R5ixQ-2U9Dt8Y68iixhzfTd4q4hMqr1rxpQODL4SJhUuMnGHaAFtdCkkg9Q7X_yCKzcoraMphgRHHbE_hnRIoSKZGRpQgXXG83Fks76PyVh1DSODUUNFNA8sHyvK_B9ao2AsJazy0C5a10LbH8grk3W4WbfeOoTxxd5FpyxehJMZdaO-5UIFoB7dWR34MDgpfF9qI6SXS4Vl_oqvyZ5Dd7uSR_A7V3zCEO5JpefFbeoENjn4bXdkyrtP5Dag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1931c9227a.mp4?token=U41nFbLZkeaGtHvasw2w--SEA-weS5terArXYEWQ6hOSoOMTY-Y6OV6jfp5ggNlTZo-G8nPIwEcOYcym68lPcCFqS4Wjat6iA8aMjIEk3-5VI2mMd54bX0C6cZ8qS-JaNk47_IK2oeIlgjBzGYChl7mbjKnpovnX31S6pLj3QYmWvPynp48T4-fCf7zdEFXScZGfKhZG7CPRz9-aG0am1Ayd8QYQ02F5De28xyGfJKL79nPSWIduYSonHYSw-39PoyUlVdl80u2P9rX-u6SIEWxQJnZdNLchJqgJJausMmJEJwBlgtZ-BzcVh7gMogdpJ15j80wZU1VLuW2Zvr9WilhPqLXWPFs-gdlfyXhXXko8lqaE9GkxGv5w7ej0ZI03i5AYuoO4TSHC24UM0YSV50mjG4IPvi-cvOZy624BhAg2464R5ixQ-2U9Dt8Y68iixhzfTd4q4hMqr1rxpQODL4SJhUuMnGHaAFtdCkkg9Q7X_yCKzcoraMphgRHHbE_hnRIoSKZGRpQgXXG83Fks76PyVh1DSODUUNFNA8sHyvK_B9ao2AsJazy0C5a10LbH8grk3W4WbfeOoTxxd5FpyxehJMZdaO-5UIFoB7dWR34MDgpfF9qI6SXS4Vl_oqvyZ5Dd7uSR_A7V3zCEO5JpefFbeoENjn4bXdkyrtP5Dag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم وداع با خلبان شهید حسین مهدویان در قزوین
🔹
شهید «حسین مهدویان» در حملهٔ اخیر دشمن آمریکایی به خوزستان به شهادت رسیده بود.
🔸
مراسم تشییع و تدفین پیکر این شهید فردا ساعت ۱۰ صبح از امامزاده اسماعیل(ع) قزوین به سمت گلزار شهدای این شهر برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460360" target="_blank">📅 22:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-doFwmyVM4ibopr65Vj78jZDF_MQyc7n25KbYfG0cQaHMaKaudIdir4DUBonvBS8YKt9Fkr_Xs3rkTXGjCI94djz1Mao97yCfPLMWFmwLOd7u2Tf6QQmfPRHUQgmNInkZXqJ0uFmzdxUi3rb6u7PeHdXhLCySOfU2QoWRNIC6aLJZq21ax7HRKGhAxu-_D5gSN-9yE0J7gd2R8jAnHe5tpIU2qx9z_BptsJpwQw4wucrNASRi24t7ae0lZR8oD17ELCz5igBnLVOPcYlZJeOepVXyMCLmP4KTEHQ1F1vBvvl2HJJrMYjnwhzJVYRM7RY4Imfpm6u-xy5LrzfKg4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند خرید و فروش سلاح جنگی در دورود
ِ
لرستان
🔹
فرماندهٔ انتظامی لرستان: مأموران یک باند ۳‌نفرهٔ خرید و فروش سلاح و مهمات غیرمجاز را در یکی از روستاهای اطراف شهرستان دورود شناسایی و اعضای آن را دستگیر کردند.
🔹
در این عملیات، ۷ قبضه سلاح جنگی (کلت کمری)، ۲ قبضه سلاح شکاری و ۵۵ فشنگ کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460359" target="_blank">📅 22:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPjA5OsN2YjuzDnC_SiLn8ls5VJ0QYin6JvgHm69GYnJpicXlQDLzTmctwMOArOnjmA0MZInhgd_2HG-akbuQvH1EygBsxTGD47QVlJOWwDeIflCwUGiFDxjmAq_5wfL56ydNe8TMsUGvt5RqK3hihgTKnAGWQW1PSc09mz7zGeJDUBKeekvgyFxcOUvoreenu69kCcwdEmq0ex4pAs_CviSrpQUpwokMLjxoVoIV5BfWKcm-8GykOLysNh9z5iDxbVD8zANKOcjZ10m-01qDpux3G4SpyEyRol1F7WjuOP3oN-JqUum0KkWGXKtHnfn1FIoaW7Q-trwD7n-kiLuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پوتین با نمایندگان ترامپ و کورسوی امید برای صلح
🔹
نمایندگان آمریکا امروز به‌منظور حل‌و‌فصل جنگ اوکراین به دیدار رئیس‌جمهور روسیه رفتند، در حالی که پوتین در این دیدار مسیرِ صلح را «راهی دشوار» خطاب کرد.
🔹
به گزارش خبرگزاری تاس، این دیدار هشتمین ملاقات رودرروی پوتین با ویتکاف و سومین مذاکراتِ داماد ترامپ با رئیس‌جمهور روسیه درباره مناقشه اوکراین به شمار می‌رود.
🔸
ترامپ در کارزار انتخاباتی‌اش مدعی بود که یک روزه به جنگ روسیه و اوکراین پایان می‌دهد، اما اکنون بیش از یک سال و نیم از دور دومِ ریاست‌جمهوری او می‌گذرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460358" target="_blank">📅 22:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d3efdffc.mp4?token=vbnisEOzmrAoxQ31VBsfcA1Icqx9gHy7jDlF-GJKOaBATPufmpBJ_es3ZD6RNn7niq6WUpOXY7ZWcxEDgNWD6u5Lq6nUwXcrDJAuYNLyYAKBP2eWindRTjXDVXDAuziUXQN8THuF2iaMMPdOXoCsEkAMNOSpiT02KMvXO_YqrrLd8XngXpyDjZ3atH3yRU7s692SikMftyphM1lzfaZJKqx9aQ2cB8xtJyKuPwkLA_0iKm_nXNaiTCGOaONDnI8lHbh6jS_O5OOjBKXiku6kIfaflFJRALsjItCjhwoQqcl9w67oiQxbqVdmli3KdiNRMhK9HAcWTPsetDuY4jAooQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d3efdffc.mp4?token=vbnisEOzmrAoxQ31VBsfcA1Icqx9gHy7jDlF-GJKOaBATPufmpBJ_es3ZD6RNn7niq6WUpOXY7ZWcxEDgNWD6u5Lq6nUwXcrDJAuYNLyYAKBP2eWindRTjXDVXDAuziUXQN8THuF2iaMMPdOXoCsEkAMNOSpiT02KMvXO_YqrrLd8XngXpyDjZ3atH3yRU7s692SikMftyphM1lzfaZJKqx9aQ2cB8xtJyKuPwkLA_0iKm_nXNaiTCGOaONDnI8lHbh6jS_O5OOjBKXiku6kIfaflFJRALsjItCjhwoQqcl9w67oiQxbqVdmli3KdiNRMhK9HAcWTPsetDuY4jAooQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی بروجردی‌ها در خیابان به ۱۸۹ شب رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460356" target="_blank">📅 22:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
من سال گذشته پیاز کاشتم و کیلویی ۳ هزار تومان فروختم. با این همه هزینه و مشکلات، حتی کود شیمیایی هم به‌سختی پیدا می‌شود؛ وقتی قیمت یک محصول سر زمین به ۵۰ یا حتی ۱۰۰ هزار تومان می‌رسد، باز هم سود چندانی برای کشاورز باقی نمی‌ماند؛ چون هزینه اجاره زمین، بذر، کود شیمیایی، کارگر، گازوئیل که باید لیتری ۳۰ هزار تومان خرید، سم و هزینه برداشت، همه بر عهده کشاورز است و در نهایت چیزی برای او باقی نمی‌ماند. چرا دولت جلوی گرانی بذر را نمی‌گیرد؟ چرا کود شیمیایی به کشاورزان نمی‌دهد؟ چرا سهمیه گازوئیل کافی اختصاص نمی‌دهند تا کشاورزان مجبور نباشند گازوئیل آزاد بخرند؟خدا به داد کشاورزان برسد.
🔹
داروی متیل‌فنیدات (ریتالین) در کل استان آذربایجان شرقی کمیاب شده است. به‌جز دو سه داروخانه در تبریز، در بیشتر داروخانه‌های استان این دارو موجود نیست و فقط هر دو سه ماه یک‌بار، آن هم به تعداد بسیار محدود، عرضه می‌شود. این در حالی است که این دارو تولید داخل است. چرا باید با کمبود آن مواجه باشیم و بیماران مجبور شوند داروی خارجی تولید سوئیس را از بازار آزاد تهیه کنند؟ قیمت هر ورق ۲۰ عددی این دارو حدود ۲ میلیون و ۵۰۰ هزار تومان است. پزشک برای پسرم روزانه ۶ عدد تجویز کرده که یعنی حدود ۲۰۰ قرص در ماه. من کارمندم و با حقوق ۳۰ میلیون تومان، چطور باید ماهانه حدود ۲۵ میلیون تومان برای داروی فرزندم هزینه کنم؟
🔹
لطفاً پیگیر حذف اداره و رفتن نیروی کمیته امداد امام خمینی(ره) از دهستان طرود در ۱۳۰ کیلومتری جنوب شاهرود در استان سمنان باشند. در شرایطی که خدمت به محرومان باید بیش از پیش مورد توجه دولت باشد، نباید اداره کمیته امداد از دهستان حذف شود و مددجویان، به‌ویژه افراد سالخورده برای انجام کارهای خود مجبور به طی مسافت طولانی و پرخطر تا شهرستان شوند. تا امروز اداره کمیته امداد در دهستان فعال بود.
🔹
با وجود گذشت ۶ ماه از سال هنوز معوقات فروردین و اردیبهشت بازنشستگان تأمین اجتماعی پرداخت نشده و زمان واریز آن نیز مشخص نیست. لطفاً برای تسریع در پرداخت این معوقات پیگیری کنید.
🔹
لطفاً موضوع کارت امید مادران را هم پیگیری کنید. با وجود گذشت ۵ ماه هنوز خبری از صدور و تحویل این کارت نیست.
🔹
لطفاً پیگیر کپسول‌های گاز CNG خودروهای نیسان آبی باشید. مدت زیادی است تاریخ کپسول خودروی ما گذشته، اما به ‌دلیل هزینه بالای تعویض  توان پرداخت آن را نداریم. هزینه قطعات خودرو و لاستیک بسیار بالا رفته و شرایط مالی مردم سخت است. خواهش می‌کنیم مسئولان به فکر رانندگان نیسان و هزینه‌های سنگین تعویض کپسول‌ها باشند.
🔹
از پردیسان قم پیام می‌دهم. لطفاً موضوع قطعی مکرر برق را پیگیری کنید. چندین بار در روز بدون اطلاع قبلی برق قطع می‌شود و کسی هم پاسخ‌گو نیست. چندین بار در سامانه «برق من» اعتراض ثبت کرده‌ام اما متأسفانه هیچ رسیدگی‌ انجام نشده است.
🔹
برج ۱۰ پارسال از کارخانه سایپا خودروی اطلس با فروش تحویل فوری خریداری کردم، اما با وجود گذشت ماه‌ها، هنوز خبری از تحویل خودرو نیست.
🔹
لطفاً به وضعیت پروژه گل نرگس اصفهان رسیدگی کنید. ۱۵ سال است که این پروژه بلاتکلیف مانده و زندگی ما را نابود کرده است.
🔹
سه سال پیاپی از کمیته امداد یاسوج درخواست وام استیجاری می‌کنیم و همیشه می‌گویند در اولویت هستید ولی به بانک معرفی نمی‌کنند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/460354" target="_blank">📅 22:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7c44040b.mp4?token=XPxZDUb6PvQ7fJy95HWQHh-pgnlz-IYpXPlhqDjD7Qi0EN-c5rjU4mnPSMdlC2-eX2yL-qRqWRUxoL1555SkqwVNlg7sry3PBjYkAmW1aGdi6_q8NDs9FHBYYXpNQLpPM2upDFHluykIKEi6yLSaiRzpJbna0Cj6mRXqKzdvI-3Or0hrAngVhME5VI8bpXbr-CLC134mbiXYb6Sd1bcIrY97hXtJHg7gf0eM5Ad1NoQEJ_oO-q4TvsZOn5SLlPuVh36o4Kz99htLEdsgc6k-KNeBZyDI0WjnXKLEVOHXhQ_R46kOqntR4zvcrfvjceUbkUan_4fo8xkrOsY-36THow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7c44040b.mp4?token=XPxZDUb6PvQ7fJy95HWQHh-pgnlz-IYpXPlhqDjD7Qi0EN-c5rjU4mnPSMdlC2-eX2yL-qRqWRUxoL1555SkqwVNlg7sry3PBjYkAmW1aGdi6_q8NDs9FHBYYXpNQLpPM2upDFHluykIKEi6yLSaiRzpJbna0Cj6mRXqKzdvI-3Or0hrAngVhME5VI8bpXbr-CLC134mbiXYb6Sd1bcIrY97hXtJHg7gf0eM5Ad1NoQEJ_oO-q4TvsZOn5SLlPuVh36o4Kz99htLEdsgc6k-KNeBZyDI0WjnXKLEVOHXhQ_R46kOqntR4zvcrfvjceUbkUan_4fo8xkrOsY-36THow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: دستگاه‌های دولتی را ملزم کرده‌ایم که فقط از بنزین ۵ هزار تومانی استفاده کنند  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460353" target="_blank">📅 22:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b961cb87.mp4?token=MdUCJ14UxGU_WIFuOdelLsF6Z-4TMEx2nESZqV47kWjsF65WZjVa4b6kJfVabOZAvzRAzyvMrQNa2JVRntpCFYbrD4akxCfoSDzAowNNLii_7bxZPTJjuOwvPhMOHocq4A03NDMc0L9FjxQ22985u9Cxc9m_y-pZWBj8n6HV4XG3E9a8Rdlfc_i7QNZZApzhfb_vVpWNDnSnQFNJjrCcTbHdMrJXPsBiCi6NM--rghoravytWpDw5P9s-eDtYW0OMaH5iOdVNnzoHdi308EIpaR_a4LoROow_8S_IOX_sB9ubfEzcmCUSAo5ND63sA4UODMPW3SN-LTiHCkEkgawpWukpH7qmlTgMRMNQTRDhwWRg6lXXDSr_89cX4MHQSOPRKjUq49TtcNO21zHptl88En7hkxzu4_vkgLSl-0wF3_CJFYVajkHG2A5k8XVQUHyv1CCJ-i-axY6Taj6OVdPc2kAWc8geXj8BNPV7Q1RFwsHD84bBLBpcX7yElQyp74KgnRgUJI3Trv1juhP8PhJnfmGXse4Pmyiio_eg2Fgud7pBkiXX6dvBUIKLPB55oXqvSR8mLLVQzCSsVg175UDxRaAu9ksFlCQcDQ1Qxx_CdQJrQ0xLEWPxoskSJGimGRCvClcTVsc1Kvj-dprxayBz4W9VoJwmIMpAFBen5_sGRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b961cb87.mp4?token=MdUCJ14UxGU_WIFuOdelLsF6Z-4TMEx2nESZqV47kWjsF65WZjVa4b6kJfVabOZAvzRAzyvMrQNa2JVRntpCFYbrD4akxCfoSDzAowNNLii_7bxZPTJjuOwvPhMOHocq4A03NDMc0L9FjxQ22985u9Cxc9m_y-pZWBj8n6HV4XG3E9a8Rdlfc_i7QNZZApzhfb_vVpWNDnSnQFNJjrCcTbHdMrJXPsBiCi6NM--rghoravytWpDw5P9s-eDtYW0OMaH5iOdVNnzoHdi308EIpaR_a4LoROow_8S_IOX_sB9ubfEzcmCUSAo5ND63sA4UODMPW3SN-LTiHCkEkgawpWukpH7qmlTgMRMNQTRDhwWRg6lXXDSr_89cX4MHQSOPRKjUq49TtcNO21zHptl88En7hkxzu4_vkgLSl-0wF3_CJFYVajkHG2A5k8XVQUHyv1CCJ-i-axY6Taj6OVdPc2kAWc8geXj8BNPV7Q1RFwsHD84bBLBpcX7yElQyp74KgnRgUJI3Trv1juhP8PhJnfmGXse4Pmyiio_eg2Fgud7pBkiXX6dvBUIKLPB55oXqvSR8mLLVQzCSsVg175UDxRaAu9ksFlCQcDQ1Qxx_CdQJrQ0xLEWPxoskSJGimGRCvClcTVsc1Kvj-dprxayBz4W9VoJwmIMpAFBen5_sGRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفر مجازی به مدرسه و گلزار میناب میسر شد
🔸
قالب مجازی مدرسهٔ شجرهٔ طیبهٔ میناب را در
اینجا
ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460352" target="_blank">📅 21:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1ec93d48.mp4?token=MIY6N_t429PP6oAyRMUOdxdrBb_7hy0fVtN0-jOQN_ykBKljUjZ-WUVIH3VbTS5rmLWsEtXXwer-VInaOBLEYVR59a-vf6M0aEkZxLmThFXxqo9Gj2ULxYM-aJoKfayDLQ5H0dogh-Yu5vyDRQC9R2GrrfTdtmWDP5jncUap5nZKjVftFfI1rkvdxJO7bujSeJeB3ZHxepcDmNj7XDtX2WXJeU9sT31Nx3Ngo-mifEo72TTsHYkt0WnXwogSwSeX8H_YGRZnTQSxqPz3v6Pnd7nzOw4ReYBDFaqL8QIGB4oXm25z9SUxBEVTuzEbhljod2cOQcJ1D_33OvxAsA49-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1ec93d48.mp4?token=MIY6N_t429PP6oAyRMUOdxdrBb_7hy0fVtN0-jOQN_ykBKljUjZ-WUVIH3VbTS5rmLWsEtXXwer-VInaOBLEYVR59a-vf6M0aEkZxLmThFXxqo9Gj2ULxYM-aJoKfayDLQ5H0dogh-Yu5vyDRQC9R2GrrfTdtmWDP5jncUap5nZKjVftFfI1rkvdxJO7bujSeJeB3ZHxepcDmNj7XDtX2WXJeU9sT31Nx3Ngo-mifEo72TTsHYkt0WnXwogSwSeX8H_YGRZnTQSxqPz3v6Pnd7nzOw4ReYBDFaqL8QIGB4oXm25z9SUxBEVTuzEbhljod2cOQcJ1D_33OvxAsA49-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌پناه: در یکی از جلسات استانی یکی از حاضرین به رئیس‌جمهور گفت «استعفا بده» اما ایشان با متانت پاسخ داد
🔹
نگاه رئیس‌جمهور این است که حتی مخالفانش هم بتوانند بدون لکنت‌زبان با او صحبت کنند. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460351" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460350">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmFAuGwYFptb7MrlyiZEh_7wQR2Xbagw3rif55AtQTPAP6E3b8JTD3QC9oUjWtb4YB7hclMShddmrIhClrflnhtuveKpxAqd9D0vf_aDv_PZbATaCKDzd7y4R-f30--ArTxmz2cAI-s4uHR-yu6pHor4hdEPs7wbnHglSq_Q8Ta36_hlzJK1qVRQVfkE0nq3cJDxbXUgF7nWDkQeJfSEAaQfSh8cyFWGF1MvF2xJ4nOEWoiVjb3gcszZ5exnsWTFPVbiSPKeZHj0U-GUFATDWJS2EjrbPz0EeBj2l3YIGWr7Qr-QOmkGL09d_MpceYRPgiAhHqFTqlkCONrMeoQonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460350" target="_blank">📅 21:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e633fa345e.mp4?token=Gmcy6wURon9N0vwGWphhoFpHCauEU0mHmOxP296su9qdLq6rlPDrVR2i7ln9rUHlVC5wqYRoq9-IpzrDLAih-Pc-NpM12lRvU5K_5xClAy-ppli9cy5puu-CFr1MGkD8x4UCcGfmgIu3SBcPMxWq_guRO51USsmhoc1VEe2jo0c5CYOH-jB1NTeB-MvaeSBLDwcSTU9AXRFLDNKsz7GHSjNITVzdgbAKVHXCcYZpLqZjgcWBf988BYCTV3nz9imKDIhhzFkX8xQOHVtxlf5T3SbwU9vVsNBtJ0pjiGGR25v6SNL5p-ubdn5T_NgYYni4Uv6TlabphT8SjrKtJdbsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e633fa345e.mp4?token=Gmcy6wURon9N0vwGWphhoFpHCauEU0mHmOxP296su9qdLq6rlPDrVR2i7ln9rUHlVC5wqYRoq9-IpzrDLAih-Pc-NpM12lRvU5K_5xClAy-ppli9cy5puu-CFr1MGkD8x4UCcGfmgIu3SBcPMxWq_guRO51USsmhoc1VEe2jo0c5CYOH-jB1NTeB-MvaeSBLDwcSTU9AXRFLDNKsz7GHSjNITVzdgbAKVHXCcYZpLqZjgcWBf988BYCTV3nz9imKDIhhzFkX8xQOHVtxlf5T3SbwU9vVsNBtJ0pjiGGR25v6SNL5p-ubdn5T_NgYYni4Uv6TlabphT8SjrKtJdbsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دادستان تهران: به دستگاه‌های مسئول دربارهٔ کارت‌های بازرگانی اجاره‌ای تذکرات جدی داده شده است
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460349" target="_blank">📅 21:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460347">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51287f30a.mp4?token=lNdgB_JbyWqErAiWcDiFygH7COt1elVX-zSL_QsPJwN2JA_SaB407qZVULMUvOx2bbaQhuXFTGG_CRUuzw-pL_eK4ueYvwf3bbU9o-j3yotqJlkDp355nShEGHpvWCHaen5FlE9vA_ucXQcsJQ79ph-ZkGwD3U5woJmSv6m4UewAluyW1LGGlp5NcblQ1H6VmDqveh6VLIVe9-mcF74WMVDaNGCxg3UYj-ERfZSNcJPICqrB9Ch_3sojeKUFoBhYTgYaEXbfrahhEKeyYRWors16eJlPjljPDjUqBPa2P4FCdzODkFfO1kXEq3ahBMzaMYoO2AJrUKpOnm0znsNkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51287f30a.mp4?token=lNdgB_JbyWqErAiWcDiFygH7COt1elVX-zSL_QsPJwN2JA_SaB407qZVULMUvOx2bbaQhuXFTGG_CRUuzw-pL_eK4ueYvwf3bbU9o-j3yotqJlkDp355nShEGHpvWCHaen5FlE9vA_ucXQcsJQ79ph-ZkGwD3U5woJmSv6m4UewAluyW1LGGlp5NcblQ1H6VmDqveh6VLIVe9-mcF74WMVDaNGCxg3UYj-ERfZSNcJPICqrB9Ch_3sojeKUFoBhYTgYaEXbfrahhEKeyYRWors16eJlPjljPDjUqBPa2P4FCdzODkFfO1kXEq3ahBMzaMYoO2AJrUKpOnm0znsNkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت وزیر جنگ ترامپ از حملهٔ ایران به ناوهای آمریکا
🔹
هگزث: اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را غرق می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460347" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460346">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkESVi-XngEpFT-UfQDvoReGAXIHPHhCD6i99zUVkZsGQu4-2fMOBqgGJi40SOR49O6WyKzAy44tkb3AteAHY71mTJNYbmN3r-X1mjzou1srUeacwjd939HtK3N3E71jV-H5cWtd8McYyUDPN6F4VelQirx4jMPAyWFSC-5Od22BRRLBEQoBny1UHX1BffIk0QypTRikn07Uw5ffJ_S6BGLDmePYviB8JUxkkliftf63u3-78EkRvSHVRjDlnh4Ab8intnoDOYAqtjXVe5DDBCCUs9MzWAM_D56lA1sHZCyYqJKzIXd27NkU7HM8k_3ydyuR66kdv1EaDcNp7Iu1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت وزیر جنگ ترامپ از حملهٔ ایران به ناوهای آمریکا
🔹
هگزث: اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را غرق می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460346" target="_blank">📅 21:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460345">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9327dbf73f.mp4?token=HKITowcC-3nzlU6dqNjElOiYM6Je5d_ocDAh_xQYzfcvYKl3NtzgLmLjS_haGOUfR-g8oyHik_UaHkuA0Wg4B5XrMdzwTe6XQEDx8ONQOtrm5ExPQ3mTtuBn-92Cq6HuCjNDEZ8bV1UUK93hNBAY093PvAW-gN42eIYZNpTBMiG3z-APyUguc0DzrIims2WwBUgYzXrZb-lBVu7aQCZImqnVpFoXOObDRAisyLhkhNJM-zV-G4WXEeMTR2yCTin4Dvl3M7W912rXnKlAYcdkdLntCic05ktywL2ZHs5rnndEnXsEStqIaTek2k4_r3ND3nwaDGh7V-oSPsfk6tlDGkhPcnfodeJF_uYZRKHt-FCt9Dn2UkOKPXjcRvzU3UyH_48L_H2lzoHgm1XU6Le4Cs3pkKBQqX02rdZIM9ySwLN_mTBT-cpecDwMBgs9dfJ7pT1rw70qu-1FrLN-fvQLKjxax_bk16h5PAbiKKOxbQYemCskfomdflMrFJrgzaqfrU2AIXi7Q_lrG1Au9XiAhAGimmnUh7EWlGKmjcWQ38JwhKGDuGP13AKNw8jwinsVLhKmoejf4LfbEqEnC8P8qiJGEYmAx1mr__LCaGROhO1TOpUq5tCWkG7p7oAEZl5NsN83yofbKWZMBhZqzH4FxnJq_dMYfEBmfaBL4gpfEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9327dbf73f.mp4?token=HKITowcC-3nzlU6dqNjElOiYM6Je5d_ocDAh_xQYzfcvYKl3NtzgLmLjS_haGOUfR-g8oyHik_UaHkuA0Wg4B5XrMdzwTe6XQEDx8ONQOtrm5ExPQ3mTtuBn-92Cq6HuCjNDEZ8bV1UUK93hNBAY093PvAW-gN42eIYZNpTBMiG3z-APyUguc0DzrIims2WwBUgYzXrZb-lBVu7aQCZImqnVpFoXOObDRAisyLhkhNJM-zV-G4WXEeMTR2yCTin4Dvl3M7W912rXnKlAYcdkdLntCic05ktywL2ZHs5rnndEnXsEStqIaTek2k4_r3ND3nwaDGh7V-oSPsfk6tlDGkhPcnfodeJF_uYZRKHt-FCt9Dn2UkOKPXjcRvzU3UyH_48L_H2lzoHgm1XU6Le4Cs3pkKBQqX02rdZIM9ySwLN_mTBT-cpecDwMBgs9dfJ7pT1rw70qu-1FrLN-fvQLKjxax_bk16h5PAbiKKOxbQYemCskfomdflMrFJrgzaqfrU2AIXi7Q_lrG1Au9XiAhAGimmnUh7EWlGKmjcWQ38JwhKGDuGP13AKNw8jwinsVLhKmoejf4LfbEqEnC8P8qiJGEYmAx1mr__LCaGROhO1TOpUq5tCWkG7p7oAEZl5NsN83yofbKWZMBhZqzH4FxnJq_dMYfEBmfaBL4gpfEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح نخستین مدرسۀ شبانه‌روزی هوشمند پلیس با حضور رئیس‌جمهور
🔹
ایدۀ تأسیس این مدرسه که در ۲۲۰ روز ساخته شده و به بهره‌برداری رسید، از سرلشکر شهید باقری بوده و به گفتۀ سردار رادان این طرح در شش استان دیگر اجرایی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460345" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460344">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f33bddeb2.mp4?token=IADoSv2p0AIpzYaLchtUmROIYWv6f-d2jFGZZsptRuBxPzthi4jGUXyI9cVJ8X0uFftdi2_kCoSGmsoITqPjxgSEYT77J0Yn_D5Nq-7jRfrMgukm0fwdYvE1GpQpNamTmrnsle_hsRwR5FRrjvau4k9rGR0JxccgLJopmm_6thW9i7lRu-UYRehrqMr0_4C_5OuQ_riB5_3wGc0BeBy9Ul1GZARYEm-JvLZ2ZvwHEhqryTYFaxIR02o8LBrcxCpmu0-rXg50EY2JnflF3ZoiGauKDIY6fjjVdNpXPn6xkXnvXXnNXgNTuO9Mrn3SApkAssrbBKYbd9gLsL4kfHrPBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f33bddeb2.mp4?token=IADoSv2p0AIpzYaLchtUmROIYWv6f-d2jFGZZsptRuBxPzthi4jGUXyI9cVJ8X0uFftdi2_kCoSGmsoITqPjxgSEYT77J0Yn_D5Nq-7jRfrMgukm0fwdYvE1GpQpNamTmrnsle_hsRwR5FRrjvau4k9rGR0JxccgLJopmm_6thW9i7lRu-UYRehrqMr0_4C_5OuQ_riB5_3wGc0BeBy9Ul1GZARYEm-JvLZ2ZvwHEhqryTYFaxIR02o8LBrcxCpmu0-rXg50EY2JnflF3ZoiGauKDIY6fjjVdNpXPn6xkXnvXXnNXgNTuO9Mrn3SApkAssrbBKYbd9gLsL4kfHrPBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا با این سربازها می‌خواهد قدرت‌نمایی کند؟
🔸
کاربران فضای مجازی در حال دست‌به‌دست کردن تصاویری از سربازان آمریکایی هستند که تیزرهای هالیوودی آمریکا را زیر سؤال می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460344" target="_blank">📅 21:15 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
