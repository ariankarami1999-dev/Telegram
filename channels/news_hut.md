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
<img src="https://cdn4.telesco.pe/file/VWEoZD662VwS5MFA_hdjxbyFzA64jvPeUQxmYjezodCWXIgnK3yNoMpnXAIXsS-USRWlql7-8xSr_EO5TOX9UDLMv8KznbrryFCSHsP_8RBAN3x_KU43GhVufbvbmD6UkSZa6VvTWEYlEZ4QrCZe5NJsVhaoAN7XEvcHsbDpwPZPKXkdMFuUGu0vSxc7pZRtj11SvZiMP-KjfXM7Dm6viNc60YJ3IQAnfwDd_ecO3YdaANLFgvGQ7Ih_3RY3WGsLIdFvWvG5VjdJuywk48_6TJy8rLRKqePBmYJUl9dWa-CWWeFMajSg8COlY1NaGuRlG1Gk21Ef9lUgVzgvqz51rA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=gh_vgEleK9PDhlIPePwuNVg1sFNEx60K0zP75WKMGW9BU7CCOIs-WQFmlsoLYWGRKaYmnAfc6dppjZmK2H_md_Bth9B3xMH-LaTfL2tsl-ViWGglpXL-Fhgn8JtNJhVX33ZSKSBQX8n-niSgjgbwRxx6mgM_Qz2A-u8fGOftxpgLu-abtqLo4a1CgRtJMRvu0n8IzjPRqZMmaV-b-fcKVEmV6cBM-zF1MTYp40fuX6ipaxl5uwp_KS3EpwkFyc2-t6CsBrutVqR0pHLh0QYYYmZvHQxdKtYtMyM1bk86DQkj_PANS3or8wdax8dBCdiOqnuW2ykHgHMX93gdcB3yXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=gh_vgEleK9PDhlIPePwuNVg1sFNEx60K0zP75WKMGW9BU7CCOIs-WQFmlsoLYWGRKaYmnAfc6dppjZmK2H_md_Bth9B3xMH-LaTfL2tsl-ViWGglpXL-Fhgn8JtNJhVX33ZSKSBQX8n-niSgjgbwRxx6mgM_Qz2A-u8fGOftxpgLu-abtqLo4a1CgRtJMRvu0n8IzjPRqZMmaV-b-fcKVEmV6cBM-zF1MTYp40fuX6ipaxl5uwp_KS3EpwkFyc2-t6CsBrutVqR0pHLh0QYYYmZvHQxdKtYtMyM1bk86DQkj_PANS3or8wdax8dBCdiOqnuW2ykHgHMX93gdcB3yXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=IxeGcJTwyLE3h_5tlr91t26CA78q9okw4T4k9YNM5XBF8Wqnc-EsHqDDnr3DR9k4pdWy5Mpu3na5VXZ5yW0nWfR-9MHthBW3oIJMGUOY_qz4rcT6MV0pnFRI3eFdKd_zV5ywqMDdEo6mgk4NTnz4GCuWOLeN_p5xGRNa7VSm1DwlkevO9bcwK8pO_XUJ1D6oKh3u34K_J3RZMkfOFEwjCGUe_q3AtQFJ5cVQCb7z1sxsHdWPHJW3euOzl-0kCPupYBWXohygE8yY6dHxAob7LFK5L5LNanCc80kABd3qChpO_teJLBXyFNZIum4Ncd5Q8YP7-obfwC006h2rDxeHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=IxeGcJTwyLE3h_5tlr91t26CA78q9okw4T4k9YNM5XBF8Wqnc-EsHqDDnr3DR9k4pdWy5Mpu3na5VXZ5yW0nWfR-9MHthBW3oIJMGUOY_qz4rcT6MV0pnFRI3eFdKd_zV5ywqMDdEo6mgk4NTnz4GCuWOLeN_p5xGRNa7VSm1DwlkevO9bcwK8pO_XUJ1D6oKh3u34K_J3RZMkfOFEwjCGUe_q3AtQFJ5cVQCb7z1sxsHdWPHJW3euOzl-0kCPupYBWXohygE8yY6dHxAob7LFK5L5LNanCc80kABd3qChpO_teJLBXyFNZIum4Ncd5Q8YP7-obfwC006h2rDxeHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=FoCh1zPsQvHDErfkYdkoIdlR_Xg8WAq_a4vPbHpPGk-1KCtuQjGXf2iqdCRd6h5l1Se3aT-7UkIseqpryC8-fcfg4nGsf4ktGyT-lSP85L5nxNLVCd4strlbEuUrgIVQ4_EGUvdW0-flShC1tHu0Fhyljb6gTnqORQZWcaMv5S6aa7EwAYii0qVnvH7ZAoy7Oo2olbnuTZaeM2psrUjSz5sm3MN4i28AkGoMQy85Q-xfaJAVuclC8Y2sNIle4hE7H1vbtmPUh6QdF2Sbo09N1_07fk7C-968f3-jy6lHVLMYcpBaAvV4fjc2Vc3CfoCteerf2tueDbHs5sK61xiIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=FoCh1zPsQvHDErfkYdkoIdlR_Xg8WAq_a4vPbHpPGk-1KCtuQjGXf2iqdCRd6h5l1Se3aT-7UkIseqpryC8-fcfg4nGsf4ktGyT-lSP85L5nxNLVCd4strlbEuUrgIVQ4_EGUvdW0-flShC1tHu0Fhyljb6gTnqORQZWcaMv5S6aa7EwAYii0qVnvH7ZAoy7Oo2olbnuTZaeM2psrUjSz5sm3MN4i28AkGoMQy85Q-xfaJAVuclC8Y2sNIle4hE7H1vbtmPUh6QdF2Sbo09N1_07fk7C-968f3-jy6lHVLMYcpBaAvV4fjc2Vc3CfoCteerf2tueDbHs5sK61xiIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=R3UdkNKxNnNO16vrueJ2HTlUvF5skl0f3hJRqD0nFjCbLgzAinVYwqqDDZTpM0cf8y2GPpja3mc1xnKT69enBtq3qdLMOot_HABeBuuRpi0h5TFsI7yXnxbEaKacFk9AN6nrw9bBUphylyITxy_GN4TWLYvN6HO7dgRyilt8c0IkHu4kjqIqpqQR0yasSg3GgIBF_ZwBtInt9pWpwRuqwbADU9onyv7DeU9mcsHJbiar9mIesljKtgb0D730QgiIavGF8wU3-23SAKKJdscGZ4qyH1GQ8rwZz76axQwxf0T5DR7SJfI9DTgDDNjlD1SQ_qBE2CGvrAW9zs4lgahOag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=R3UdkNKxNnNO16vrueJ2HTlUvF5skl0f3hJRqD0nFjCbLgzAinVYwqqDDZTpM0cf8y2GPpja3mc1xnKT69enBtq3qdLMOot_HABeBuuRpi0h5TFsI7yXnxbEaKacFk9AN6nrw9bBUphylyITxy_GN4TWLYvN6HO7dgRyilt8c0IkHu4kjqIqpqQR0yasSg3GgIBF_ZwBtInt9pWpwRuqwbADU9onyv7DeU9mcsHJbiar9mIesljKtgb0D730QgiIavGF8wU3-23SAKKJdscGZ4qyH1GQ8rwZz76axQwxf0T5DR7SJfI9DTgDDNjlD1SQ_qBE2CGvrAW9zs4lgahOag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gXevtbUCZLup8ddudij9gyfwcF83RhbGYJrDPg3rrlPImG3Cz1EWfVS-BZkzZRG39Mb2GwzDnlfLA-s3AvEuAx_QiWqmd-pxRxvCBQKZc0770x1WfoXebA3fms5kbv_qnaGYKX-8ZODDrWrPh7y5C9IYQZeZNmKsl5KRNqbX-qC9kuIUsjv-vlI76eZ9cokOuGfhS4WHRdgETzt7wcUOO0hkzBOUZZ7bdf2rXMS_HW61bbq8pbSPehDN49qoSwbSY4aefhWcIROdx9Af2B-Kmb3nHv8Yi-xGtxT_8NMuRy5R1AFSBUmKadvsvaqktsrXKDwZf0nJB-kZ3JJgl5cYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=iiBpzuFc5u88hVvbNcFEotyMfemY5DiZzS5fYV-NIoKnRHu_Q0LjNdy3s1jkhRKSpoEBdN95qvftNA6QU9kCM5UD5V7W8W3gCgIWgjMFic4a86arATx_lj9E_PKmX1zpQTI6Oodfhi64S9w2Ggr2vpexA9alfj_gPZuGZPBFUTbVOqbSv9sNpEPR-EY4CKMDh_xJ1Rjy2gGLOeNjYeBkUd2LbKPkgCx30IjDdfPWB1KidWyxOwTmBhwBhHkiOpPagWZfKv3jYbypbfMtir0-zjVvRdVF-d_G4dNcKOIOCGT-kbZSD-wn9hv33yFVldrKtumzcEqezZ7t8ddCMzv_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=iiBpzuFc5u88hVvbNcFEotyMfemY5DiZzS5fYV-NIoKnRHu_Q0LjNdy3s1jkhRKSpoEBdN95qvftNA6QU9kCM5UD5V7W8W3gCgIWgjMFic4a86arATx_lj9E_PKmX1zpQTI6Oodfhi64S9w2Ggr2vpexA9alfj_gPZuGZPBFUTbVOqbSv9sNpEPR-EY4CKMDh_xJ1Rjy2gGLOeNjYeBkUd2LbKPkgCx30IjDdfPWB1KidWyxOwTmBhwBhHkiOpPagWZfKv3jYbypbfMtir0-zjVvRdVF-d_G4dNcKOIOCGT-kbZSD-wn9hv33yFVldrKtumzcEqezZ7t8ddCMzv_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMy3bGXOQNAwVS0M4Sjg1o44SeR17hsSO7Dac63Nb02m3t1E63kOkIdmgw64KMTipyEqDD0qCt2uw0RDqHr8eznrt-GMMjYAWMMtTH2L5skpcw925vXHjjt_kfV4i2gdIR3YhhlTjLhsApkzSVANbXKRr3uglPLXnNIY2u8NQwYp6PPLvaPtbqay_xFEjINkd2dmOjG5LVZeePTfMshP2Vx65QgI9GMfp6TLwnynLtxfdscqhK1IaEZhNIWiH9a--_CI80QAXQ8tcJ5NzCn5DxpaOoF634Ca4R334rXUdN0FZduylxhnbhIRa8Qvhy3JlSMQ9HR9RCWQz2t_VdRodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=nGyAO2axLPWIzsUdUvB41CnD7FeaYxXbNeFY1X2CG-MvEi8VnfSzyY3xLtI7psUXqnx5ZKuokbc42JCnIygz6K1gdcptIzlq4MynQdD3YCItN6FjWwbfNSjjMcwkv_KoUtVfMaOOyuPU3vQcBvhnWCH46ktnzDCIAVVW1kGZVlDa0nfZ3rM7uv6-eXrWXz4UGYMFM8e7qfx8MohK_VuKk7Uq8kSjeamgd_ToaSjsdeG_djlzjhtANAngCxp8VhXqEDuMqr0ntu0sxmMqxEIkrX6eG3Kifvuc75vOAZNq-NHXpiDPSQdZn8zh6JDqCX3Bj-CTqykBfnc5vC-r6I5C1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=nGyAO2axLPWIzsUdUvB41CnD7FeaYxXbNeFY1X2CG-MvEi8VnfSzyY3xLtI7psUXqnx5ZKuokbc42JCnIygz6K1gdcptIzlq4MynQdD3YCItN6FjWwbfNSjjMcwkv_KoUtVfMaOOyuPU3vQcBvhnWCH46ktnzDCIAVVW1kGZVlDa0nfZ3rM7uv6-eXrWXz4UGYMFM8e7qfx8MohK_VuKk7Uq8kSjeamgd_ToaSjsdeG_djlzjhtANAngCxp8VhXqEDuMqr0ntu0sxmMqxEIkrX6eG3Kifvuc75vOAZNq-NHXpiDPSQdZn8zh6JDqCX3Bj-CTqykBfnc5vC-r6I5C1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=O_0x5fqpbTmwC28imlEKbicFNHxcaJMFYikh-KEUK08jsGXy2FLdlMOrJV-DPnXhlh0Ky_Dj0ed_Enn2hlXR_HhlDbm8WKxakxQkeK-hOvRwnRHWwI6_8o5dvcMbxadZ2VbQZ_W4OECxd9mThmLQxYsg4lsMq-wsvFWXhLl2De0xKxsOCOiDaejXPMRGX0_iMJFmOAHH3Bkz6ZYVgTPR_dKCNQjmuwEV6ROrE8gEQzohWL4iJSLyOAabJhUExLPHCXKAAu7D_4BDD5GYV8JJyZWTifNH0BzMjCQsqSO44JYyZ3D0Vjbf-_v0p1-xPoNNsvAWU-fprwRYFWr34PveYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=O_0x5fqpbTmwC28imlEKbicFNHxcaJMFYikh-KEUK08jsGXy2FLdlMOrJV-DPnXhlh0Ky_Dj0ed_Enn2hlXR_HhlDbm8WKxakxQkeK-hOvRwnRHWwI6_8o5dvcMbxadZ2VbQZ_W4OECxd9mThmLQxYsg4lsMq-wsvFWXhLl2De0xKxsOCOiDaejXPMRGX0_iMJFmOAHH3Bkz6ZYVgTPR_dKCNQjmuwEV6ROrE8gEQzohWL4iJSLyOAabJhUExLPHCXKAAu7D_4BDD5GYV8JJyZWTifNH0BzMjCQsqSO44JYyZ3D0Vjbf-_v0p1-xPoNNsvAWU-fprwRYFWr34PveYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=aMwwZBJKzYQjbiqfSRRhx4duHTjWlLTsTnoNXozo1kZWgx4ydnbh774WbSSXvIAkrdzKjs1dyx_XstzdIDUIJ_nbCzqzFIjxgDePQXoxYmm99C_XzcvPZfB09ecaCF2Xnz9zyLbjPpd3QKseo26gGTEn-cODgdgHqyQ3ji0ud1JOkJlvJqMvbWT5vSCf3vUo522o-E0wLt5XaMlyyQ0kVZEBZlS1RsIU68B1QGjLgrxyLtKIoubCo5MhpjJK18j0Vu2sQKbEQRluGiX-jgEq_DhT-EJWim1DoaWtVuFKqIjNFv2EBuE6DYfv35wS8oUBecrH84ndX2B0nt-RkzlGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=aMwwZBJKzYQjbiqfSRRhx4duHTjWlLTsTnoNXozo1kZWgx4ydnbh774WbSSXvIAkrdzKjs1dyx_XstzdIDUIJ_nbCzqzFIjxgDePQXoxYmm99C_XzcvPZfB09ecaCF2Xnz9zyLbjPpd3QKseo26gGTEn-cODgdgHqyQ3ji0ud1JOkJlvJqMvbWT5vSCf3vUo522o-E0wLt5XaMlyyQ0kVZEBZlS1RsIU68B1QGjLgrxyLtKIoubCo5MhpjJK18j0Vu2sQKbEQRluGiX-jgEq_DhT-EJWim1DoaWtVuFKqIjNFv2EBuE6DYfv35wS8oUBecrH84ndX2B0nt-RkzlGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XG-3OnWOpt9kc0R6Ax2ayWPU3hKJlBLRep6r7kAHewa4kFico3wWiA1QqeIw-VHpL468OrDehVSbxp57rLPjDrJxcR3ClZgdpqoLoOJE2bIrAvBUIUBG2tewiE4LafoUncIdNiqS-ixJ-XZGwKOsfRT7xGbrpTf1I_9kx-s00IGzmwdNbvVwjc4tKVSqnEjZ8QzgkY7ZDvlLJiv1wrd6nW3Az_b9J76plUzA-Me11KpbBqpNnaEBr-8D1KcwJqQG0et4BV4maMuQ7-0hcdoeVaMo-uSjvkLyqdq2zL8H6OBxdJxdwIPUb0WaXkOoPrr2l1ywWuu8QQpODnQDXxZGFrlUn9NhDhkIZx681qJqBiIp8G2DO9kHLAHJIIyiDZnhLbMV5p8Ku64fYEQ2B1mrHui3wUjg3JmginW1PV0cXFtLFV-r8-oZcS8CLx4XEBN-TCWrymUTscVrCeDiPV0cAR-PiVzEbPFW2SYnRJ94Mw4gHv_6h_h5T7441Jtk4hjgV6a4vvK9VE7vLdez8ORQWuSSU_jx8pZKctUNuKL4ZnX88YTdQWkXqmajy_GgrKGyYF8YBnWDvw6-ZmMDBQS0qapjQYE0NwRGwQqpyC2gbOuDQyxDUpmLIngosAxD_NpFDXD55IhYPdGmaAfpsqgZFCCCu9HlseuFHMi32batOhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XG-3OnWOpt9kc0R6Ax2ayWPU3hKJlBLRep6r7kAHewa4kFico3wWiA1QqeIw-VHpL468OrDehVSbxp57rLPjDrJxcR3ClZgdpqoLoOJE2bIrAvBUIUBG2tewiE4LafoUncIdNiqS-ixJ-XZGwKOsfRT7xGbrpTf1I_9kx-s00IGzmwdNbvVwjc4tKVSqnEjZ8QzgkY7ZDvlLJiv1wrd6nW3Az_b9J76plUzA-Me11KpbBqpNnaEBr-8D1KcwJqQG0et4BV4maMuQ7-0hcdoeVaMo-uSjvkLyqdq2zL8H6OBxdJxdwIPUb0WaXkOoPrr2l1ywWuu8QQpODnQDXxZGFrlUn9NhDhkIZx681qJqBiIp8G2DO9kHLAHJIIyiDZnhLbMV5p8Ku64fYEQ2B1mrHui3wUjg3JmginW1PV0cXFtLFV-r8-oZcS8CLx4XEBN-TCWrymUTscVrCeDiPV0cAR-PiVzEbPFW2SYnRJ94Mw4gHv_6h_h5T7441Jtk4hjgV6a4vvK9VE7vLdez8ORQWuSSU_jx8pZKctUNuKL4ZnX88YTdQWkXqmajy_GgrKGyYF8YBnWDvw6-ZmMDBQS0qapjQYE0NwRGwQqpyC2gbOuDQyxDUpmLIngosAxD_NpFDXD55IhYPdGmaAfpsqgZFCCCu9HlseuFHMi32batOhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWABbhDsaGTni_MTDHJ59CaOtNJ3Y_IVNEzPAvLjRwIZowaZPKhK3yE7wNLNRvEmRBt-xUJ4YlXa5dkWAGj197IL5jZ11UaxZZaaGC_o7Ws5NRo3EYXtOAufgnDhf6Sp77Z1w60UxrVZTaSDHqxCSy8cnA0WxNEMDH_zhWL5gJ-FaEg4Bqv-OgukqttZfA7axVjFw-a80zr-sV0rXfCTT4IThy4YQ5oi0DsT3oJVaNvcJ-ruKxccapoO4KV-ezbqIdoOVr87Uy5IJ6s5Jd_cqa42ZXRn9WHwHYBIfemp6MZWyfNImQhIImDUn19hPTBYBqC-_HkFKxuKg9IIdPRuHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLuXNtH3SxQKdK4xMw9Qus0bXok5Z21iEoyMTRz9wpFNZvc4tHOo7EMrrMOClkAIOle7FXLXasgy0LVLgSo4QoK22g89XAZ_psy5KG4lawjtPLCPBIxgHp2gcQNzby98jrmYrxZXk86cIclMgdCssMWD_XTFQ1SeyaQG_me_Xh5gFFIU3SXIAUo0uSV8ne7FReIeKH8bGSUTQ9sT-c4J-BN4GUVjAuVeQBy77miyOlEhmJx4mzE_Eesfzb-UidoEsCW1ncZmhB6yy0nIcBldAiDx-CwGL0Utu7UPeBnJ8SekGfC_l0KuO4uWgVJi82dtQJ6z_HRrCGpTTIpSB2iccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=Sjbo6WJ6Rw8hiFjZCjd5EjgF_cgvitDDSV4bYj2Plcbdh6G10E9N5jkFsQp4Z7xzt-2TL61GMyvCdp7xw2uxd35jYX8LGnZetlXQ49uM2abgHWqm7kJkUiC_d9h5lKZpem2pdHiGXG1HVT_2d34iGCFk9KfG6m8VB1LC4JoXgYg-KpU3ZVqriCNkA8B2DIbSAyZ6wzSfgYCV1mR8IhEP1db-0iWIDuPbFR7SAw4j4idy7v2gEeYmIzUWROvElP5lKMzRl1we0eDPrdtt6qDKVH9r-8b2YNuUeU3jTql_ml3RjPSLdBzpsb0xOueUZ2iLuywp2oQL2KX1TDqVcNDTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=Sjbo6WJ6Rw8hiFjZCjd5EjgF_cgvitDDSV4bYj2Plcbdh6G10E9N5jkFsQp4Z7xzt-2TL61GMyvCdp7xw2uxd35jYX8LGnZetlXQ49uM2abgHWqm7kJkUiC_d9h5lKZpem2pdHiGXG1HVT_2d34iGCFk9KfG6m8VB1LC4JoXgYg-KpU3ZVqriCNkA8B2DIbSAyZ6wzSfgYCV1mR8IhEP1db-0iWIDuPbFR7SAw4j4idy7v2gEeYmIzUWROvElP5lKMzRl1we0eDPrdtt6qDKVH9r-8b2YNuUeU3jTql_ml3RjPSLdBzpsb0xOueUZ2iLuywp2oQL2KX1TDqVcNDTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NW1HGq1uHDrCFu5-usfpivvdx7qlV12H5GPlQtzeiYO7K7a6dbVVGoDXrc7ZbotVMNld8Xf8SypKcVSB12yRxLejKVt9iGExDjvwF-R62dBRfYXbJ28ucF-uNECizJriwFUPjDAVl8T3uEKZjAWA74P-VniZHJAQqijAHycQxb1tUan0hl0nF_jybosfWxt2480lrCT4omHAr2tvH6Ht9Aa5B35OdgTIRzI4d3H7WJ1DTk03h46jgb-QD6Sx_Ra_bqloH9ufD8z6J6J1Rrb9gveHc3btnkL7EmM87FwTDALzGcJl3J0R4NyrV6ptkSHjFaSMB-eRibw_9KEViIdndQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=NW1HGq1uHDrCFu5-usfpivvdx7qlV12H5GPlQtzeiYO7K7a6dbVVGoDXrc7ZbotVMNld8Xf8SypKcVSB12yRxLejKVt9iGExDjvwF-R62dBRfYXbJ28ucF-uNECizJriwFUPjDAVl8T3uEKZjAWA74P-VniZHJAQqijAHycQxb1tUan0hl0nF_jybosfWxt2480lrCT4omHAr2tvH6Ht9Aa5B35OdgTIRzI4d3H7WJ1DTk03h46jgb-QD6Sx_Ra_bqloH9ufD8z6J6J1Rrb9gveHc3btnkL7EmM87FwTDALzGcJl3J0R4NyrV6ptkSHjFaSMB-eRibw_9KEViIdndQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=hiwRwwhq3Om7IiFHWeH0HH2Ov6xsf4SbVmpYV_nK1gkhINBWHn6_3K32MThN1mdPuHrEIM1rVwjSdUOj_RekC3Y2ZpTWEM_7QgIWFjwQU4OEGYqls-Is6sMPPlO8bH3NUMv4307FaH6Ps2gSwsVDBw_59MjBFMUODOoDW3c4VCUye3yInYRinbF3tozawxgwA-4Oqg1bD9gBpX2gtizgBuBrdtMhhT0PXqAqq5OGM55m6yKpnBgrFj6BiQGPlb3OdEPtUtUWVlDAl_JCBxRy0T07tKKtGjzKOaj7xkrYMEQ1V-ZZYM3M6ahz3SacbrqijmgL3hHRSa0AqGE78NGxC1xLvULcNZQNfSNt8dtG134uvzgUcCsku7ERyvL5jldw4ya5ak6WZX7mkqmpcpLzsrRBPflm4vhlvkJh1U6sPHFkAZl_86jT-mr1EGh6mFTTkh-tF9k_ylyN_eB9ZeI8FrnN4pejvRJpLZqdq0PgufsYLAKDRFbBWmdE-vvx4V2MAUmmY-5RSs9Cy2Wai7_toSAR2FYvj7kootMa4MQewE3zV2TLj6ypG5E3o14SIf26AvO4rBvxSB4FvFCXFCIt3Lat8TdZUYhAypG-hAiwq2qp4UnbxzLIuULPtEcEi9RYX-Q78ojb89dz_oW-f7KMCtBLHHqelIDlZSaxRGOfpV0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=hiwRwwhq3Om7IiFHWeH0HH2Ov6xsf4SbVmpYV_nK1gkhINBWHn6_3K32MThN1mdPuHrEIM1rVwjSdUOj_RekC3Y2ZpTWEM_7QgIWFjwQU4OEGYqls-Is6sMPPlO8bH3NUMv4307FaH6Ps2gSwsVDBw_59MjBFMUODOoDW3c4VCUye3yInYRinbF3tozawxgwA-4Oqg1bD9gBpX2gtizgBuBrdtMhhT0PXqAqq5OGM55m6yKpnBgrFj6BiQGPlb3OdEPtUtUWVlDAl_JCBxRy0T07tKKtGjzKOaj7xkrYMEQ1V-ZZYM3M6ahz3SacbrqijmgL3hHRSa0AqGE78NGxC1xLvULcNZQNfSNt8dtG134uvzgUcCsku7ERyvL5jldw4ya5ak6WZX7mkqmpcpLzsrRBPflm4vhlvkJh1U6sPHFkAZl_86jT-mr1EGh6mFTTkh-tF9k_ylyN_eB9ZeI8FrnN4pejvRJpLZqdq0PgufsYLAKDRFbBWmdE-vvx4V2MAUmmY-5RSs9Cy2Wai7_toSAR2FYvj7kootMa4MQewE3zV2TLj6ypG5E3o14SIf26AvO4rBvxSB4FvFCXFCIt3Lat8TdZUYhAypG-hAiwq2qp4UnbxzLIuULPtEcEi9RYX-Q78ojb89dz_oW-f7KMCtBLHHqelIDlZSaxRGOfpV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=CxdFB43ay-SGPw1JWB382d-xLrIVENNUXO3JRU4s7bL3nV0LLkRaeXHGmracmDGaCmtHBra0x2yvzr7Egfel2ycheMDQEqUzJabUy0tpvn4py4ctPXtf3_2HG8eu014rznO9dA4lGhBIDWUjqoSZDaFeAuu7C6EotX56h9AW3zpTf1ugHf6-hF31Jz-w0lS1SrapcbZNrpalpeepGw5jNKQ8uqHAYeHhAbXKVnv4Yu4RXlAzp_LWV5WpeiTXAkZGuvR9fn6_CGGomz0KXQPQjS5qVc0QM49yzRFJ1qDPmnBmNIOrRMeGjn95jECnzgHXeWUxg5t5Yyht9fti37Kxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=CxdFB43ay-SGPw1JWB382d-xLrIVENNUXO3JRU4s7bL3nV0LLkRaeXHGmracmDGaCmtHBra0x2yvzr7Egfel2ycheMDQEqUzJabUy0tpvn4py4ctPXtf3_2HG8eu014rznO9dA4lGhBIDWUjqoSZDaFeAuu7C6EotX56h9AW3zpTf1ugHf6-hF31Jz-w0lS1SrapcbZNrpalpeepGw5jNKQ8uqHAYeHhAbXKVnv4Yu4RXlAzp_LWV5WpeiTXAkZGuvR9fn6_CGGomz0KXQPQjS5qVc0QM49yzRFJ1qDPmnBmNIOrRMeGjn95jECnzgHXeWUxg5t5Yyht9fti37Kxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEj7oGqDsriQVIOS7bnZ8sC2xLccwoKf0FYZRvf7MIczUi3tqmky-_nb5QqUf1-fx5uJDF1R3fYWbJk2GnuDQIvxMlyyvNvw2PejR7DI1trnMS_Rem8gcBKX4eyDsATFrI2-UiaAlz4HHY3pj7qgfEP7OvXF3mKpkhIKyDKu6_3oH9EdynVu19SBCKz_K4qdNKymmhvjLQ6ZK9Aj8uUvAsmAHqskvwfBOp50rC7QPX617Mpe2fsVAOLIO5GT74vvo9VMd_3-Z2nUb-Z5d67tBQufwwpzKHhGtnBDXLF0LYZ3pSHgQwiCZe4xS29iJ8xYz7Ju00Cnb9FJsBGv6ytdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcZcph6ic5KNvZ1NjU1--krUOSHdLfuuc8R_KgDiZlNUc5_CYv41yfFLmGWZmOkLIS5YEyhQcM7tWdY4gYX4YZgcAhAIVmxwKDwm7sNqic0feLwxw617lv7vvqr6siXHNsBrdYC56j1FoE8xV2pRD8amVsvCOm64BGZY_644iXfHSryDnHUQL2FThoFocwVy8tOnCseK-5w-SErZC7JGy8VftQSyzoFbyl7VbErEYSZX2NF4OJJsnMuG5-UkC8yd3LgDLhuyuinTShHTL9Z_PREcIRWwv67Q8uSJYcX6ICaWsmYtgDNc-L6SP-K9zVkksxL1rpsj7VuToGoE_4W-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=iat0vwfu4gqFJv2-gHCyJlWZq7e91NlNJxljrnBNIrreuTw6WYOtc0FU2rBsqb0Qz-_r-6zhlGcRgYom8YdDftqOjA_pgHpjtXOsf0rMApX1vzOMjFc7LlpqgAGR7lhywAA_OgV_nymE4n7uKmgJgR5xz9UCxybzhByNk6-mAgS4hhofVRR70Hn_37PxPBifGTORHcFpU3L2NZJumBJuoIcbS1JqTXLIfUAPogKigUTOFO-9lwwWcJeLH6MIA3AHJUaXin9GeUovGpWQV5jPI--wlthuStbHiJktBmoaQgVdbhmvsOgwbyPRtjm8mWflkLLmYvT66fadFSYtKaEzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VucblGlJFk2Kw3-qtym2oWkaxWsnnby5Mj_F7fBcP_dkXMAhXBKbxqo2O7n0Si9M-yTN_cHUHmn-TfMFf0dvP8cPqeTNP2RmN-8sGQYyyM_B1y2osdD8sus_UHOnJuC7R-Slznu-IVz8H7noUueoYBKlXXbZnn5AwNClGX1QJZs2W9JI7pLTbZ84_pXxSLixoRhRpXRGkTs7zI8ftR5fBt8IHc5c_z_uy-XFUNmb8theQHnfdD3TTAGvXECKjCRYoxUj87_9tOKP1Lfnkj7EYEcVtoUolJ0H08lkmUn0oS4n5wYklXgNQe6JlJFxGF0auxzZpD4hDJPIo1KcdlZvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VucblGlJFk2Kw3-qtym2oWkaxWsnnby5Mj_F7fBcP_dkXMAhXBKbxqo2O7n0Si9M-yTN_cHUHmn-TfMFf0dvP8cPqeTNP2RmN-8sGQYyyM_B1y2osdD8sus_UHOnJuC7R-Slznu-IVz8H7noUueoYBKlXXbZnn5AwNClGX1QJZs2W9JI7pLTbZ84_pXxSLixoRhRpXRGkTs7zI8ftR5fBt8IHc5c_z_uy-XFUNmb8theQHnfdD3TTAGvXECKjCRYoxUj87_9tOKP1Lfnkj7EYEcVtoUolJ0H08lkmUn0oS4n5wYklXgNQe6JlJFxGF0auxzZpD4hDJPIo1KcdlZvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=lv2x5XDiPFDruyyleUCPr0d1LSoafX4XyNq6DtMFWJcPGFctpk7NGstIu9IfKHR5N0rdFFLy68ZNf3mppbAoR9PEHIhsbHnW4-ruargved9u6a_2pItNEzucmBjLtgmB4sD0MqGnqthqm4I9cObYjnTTdIrCxO2vCt7VBvyKYqhTfMdOeIUQYNg5UMUJjrXAjJe9BbW-MicUSPa9l3ttVcrCs_IaWCTL-6WUNClDVHBdZuP8OsKQRghd4JaLqYzmI8AwKr9xynVQpCUS3xHIOKxQjJ-yscxBkRxGBG0BhxPpmY-ckzn88HqQNIOW46D8HBCQUuE_WnwMj_JBX2EpjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=lv2x5XDiPFDruyyleUCPr0d1LSoafX4XyNq6DtMFWJcPGFctpk7NGstIu9IfKHR5N0rdFFLy68ZNf3mppbAoR9PEHIhsbHnW4-ruargved9u6a_2pItNEzucmBjLtgmB4sD0MqGnqthqm4I9cObYjnTTdIrCxO2vCt7VBvyKYqhTfMdOeIUQYNg5UMUJjrXAjJe9BbW-MicUSPa9l3ttVcrCs_IaWCTL-6WUNClDVHBdZuP8OsKQRghd4JaLqYzmI8AwKr9xynVQpCUS3xHIOKxQjJ-yscxBkRxGBG0BhxPpmY-ckzn88HqQNIOW46D8HBCQUuE_WnwMj_JBX2EpjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=D0Z2iX-zqX6EHNgQzUUM-l0sFO6hbiaUkgaLKD-yDXQIGUfDizknrnYIA8SsdwGo_RFT5UShwkLGyVQ8A7zPvhbGRw--mwThlM0WSVZS5WEd3sLNZDNCt4VSCj8QJ8RTqxKwfspasqy4RwhmBFw5RRRWUzp4djzpOAV-5NF-RLdUbwN9bksG3eyRMUczhBClm3wr7jOvkZLUWN4PsLo9UyUauuc1dX78NWX1wg2BJBrDoitakASrK_Vrs-LnfkorWedKCH8ZcTn3OY3ndvTIV_BpTi_1pMqmdbGPHr687DfLB9D-NBeUjb4JxSZy9SZ_3Gt-A-3N42X9OJZGruf7fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=D0Z2iX-zqX6EHNgQzUUM-l0sFO6hbiaUkgaLKD-yDXQIGUfDizknrnYIA8SsdwGo_RFT5UShwkLGyVQ8A7zPvhbGRw--mwThlM0WSVZS5WEd3sLNZDNCt4VSCj8QJ8RTqxKwfspasqy4RwhmBFw5RRRWUzp4djzpOAV-5NF-RLdUbwN9bksG3eyRMUczhBClm3wr7jOvkZLUWN4PsLo9UyUauuc1dX78NWX1wg2BJBrDoitakASrK_Vrs-LnfkorWedKCH8ZcTn3OY3ndvTIV_BpTi_1pMqmdbGPHr687DfLB9D-NBeUjb4JxSZy9SZ_3Gt-A-3N42X9OJZGruf7fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=S92OCLHwMxB6R2tnTg8Q49YulMAAVZl8vw2bnBzAOJNXu0mkrl6uA67fW9po1YTrqV51hLh2slszWMv0rNlAZoMxUtM9wKb7SyPWK8Fnv3v7NUABcBj2Ofjrv4Eny_9RvZCDGs_-YoXyAhznVOl2JTUFKPpD1c19IFKax5gCqR8WP1cXW6GIPfu4_g-EqrZBQZOUp6-lvvnO6wxVvecpZ5wyfwsy7aAV5TKEmdcmYsT-OPdOsDHTVVIKgUZI6cDLujRBZnrf8QISDr6b718jP0bVOwloFm7dfvd2FJdPWqCS0PNJ-scE1Uqp2sQtxS53a4u3qO86_br2T-5_sWtjVWDOswl4r6BVIKI-6IZ_BWPZBhUMuk5i9URVftKxoyuNm0ttyYj9XLIpR94jm2zQ-CrKLiLk5FPi-EQ2oLHr5_QH5U-jLyJ9fvJdqW9JFVTyJVcoUWewrO0FAnCbQn6HCxFDgw-HxIZ1K0Spho5AmXCxn3zrryqYpFAhO0YZ_Ab4aPjcrQxA-ctO-YhE9VkrmgPHA4yyndZVrTCUbLS7clJRzCvDfTlQ46gJAfpCUTWU7MgEgMrdevUUPLbwB1zZLXZfjrCO3CEVA2H1MhavYeSzPmc0byRgtUC0TB42nwZnwDfnlkF6BUQbi0w-Sk4C3GZjrv_aySSILahIIRJcj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=nUtOFnnqsd82k9GWaeL71sdo8xZsJNW2h-tz_wZgNUZuHH52aiK50Z-tySnHpCEBn5OJxCrXBejfNxSNRjaUYnL_BDrsSgRCdjNdUeJvxQvfi6nf4mqWL8GuYEw5WYz47saopmAG9QkOHEhEdmpxztxJ2k8rvdu-g5nx9swwdmgWCjJ3l4O9ikBUdFQvv8bK5vRBINsHnyFbrC3yY9i-R4krmsDwOO25wPvgLK3k5oWm7EO2mudKjR9SRQNfMv5r9FP6vML9l7M518W0ioQlGx5KdcI7X7yMG3nf6D6o_VZU312APuDxUtD_LQs29JYHYKdZz7tjBULXbXRWYVUKeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=nUtOFnnqsd82k9GWaeL71sdo8xZsJNW2h-tz_wZgNUZuHH52aiK50Z-tySnHpCEBn5OJxCrXBejfNxSNRjaUYnL_BDrsSgRCdjNdUeJvxQvfi6nf4mqWL8GuYEw5WYz47saopmAG9QkOHEhEdmpxztxJ2k8rvdu-g5nx9swwdmgWCjJ3l4O9ikBUdFQvv8bK5vRBINsHnyFbrC3yY9i-R4krmsDwOO25wPvgLK3k5oWm7EO2mudKjR9SRQNfMv5r9FP6vML9l7M518W0ioQlGx5KdcI7X7yMG3nf6D6o_VZU312APuDxUtD_LQs29JYHYKdZz7tjBULXbXRWYVUKeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=GRr_O6VqDY0xwA3h2hvhJCgGD8BoAnJ6fdaAba60tbiL3YJddj-3TLzVvqysMYp7x_96Xlpcul9vnZHc-dvBSequ2U40gtHVsz8-iUNfLG9DlXWeYft7M-55vsYBir3l_Sa3Vw_s3B40sj7BF_CqDNo0jxLwHWCqBG-LzXDQlXsOvLCHbrF9caNxqrhd5tb6O57PO9fITCsR9WjTLH2uE-uO9w-CMGBg_FY6TiMI2-SHgc7UrNq0HMn2OShYj4E0nowjlWQUiNNRFXl4BMDJGo9kGRXn8h9vRyuJedLJ0tuWL_YHqL7YcXTfSy_J9btLpmRmfuRZVoLYLuzjHgj3gx4YIA_4Zw97d6_6v-LaH0oOpREag6L9pGgTNwnMAeUYhx0_q8bx7FufNth8J0XjinASdxTBZBNCmS7Bk3OxgK1x920g9Ghi6W5rKtlxICfPgRq4MdbPemfq80eMBa6DAIG_diUEtDT9gzdRN8KOe3Eu-RY_Twc2YL2Ya1eYezKfrmjzr1NxwZV1DDE3ncArutHC71jJhtKh3nHhHKAStQA5-jazs6cKTXhy-urFY9ZF4RdWUuGPo3gPNYVBx9wE4j8Eczz5hEIa9vzj0EcYgl13EEYYptUe0bZasiAqH-0tEICFCiJjPYyHDGWWpkDxDQZUeFS9iUGnWQJyLL7gM68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=GRr_O6VqDY0xwA3h2hvhJCgGD8BoAnJ6fdaAba60tbiL3YJddj-3TLzVvqysMYp7x_96Xlpcul9vnZHc-dvBSequ2U40gtHVsz8-iUNfLG9DlXWeYft7M-55vsYBir3l_Sa3Vw_s3B40sj7BF_CqDNo0jxLwHWCqBG-LzXDQlXsOvLCHbrF9caNxqrhd5tb6O57PO9fITCsR9WjTLH2uE-uO9w-CMGBg_FY6TiMI2-SHgc7UrNq0HMn2OShYj4E0nowjlWQUiNNRFXl4BMDJGo9kGRXn8h9vRyuJedLJ0tuWL_YHqL7YcXTfSy_J9btLpmRmfuRZVoLYLuzjHgj3gx4YIA_4Zw97d6_6v-LaH0oOpREag6L9pGgTNwnMAeUYhx0_q8bx7FufNth8J0XjinASdxTBZBNCmS7Bk3OxgK1x920g9Ghi6W5rKtlxICfPgRq4MdbPemfq80eMBa6DAIG_diUEtDT9gzdRN8KOe3Eu-RY_Twc2YL2Ya1eYezKfrmjzr1NxwZV1DDE3ncArutHC71jJhtKh3nHhHKAStQA5-jazs6cKTXhy-urFY9ZF4RdWUuGPo3gPNYVBx9wE4j8Eczz5hEIa9vzj0EcYgl13EEYYptUe0bZasiAqH-0tEICFCiJjPYyHDGWWpkDxDQZUeFS9iUGnWQJyLL7gM68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8QKkTdcknoQi2x8kQzdT1Nuh1La0ffMkowpyDqydCvY9H1yjPpbHOcFOD9CTbOHK0V9SImiv473Nb8WX5s3rlqVBLXqSK30BfTDfpmU6rcficOCDVBstV3R-7tyOqcpe7Zq3JJDiG5aWMsQEKkLIbC5JVtRTaGOIzRoqoF7AOTzxFAcwXdwrjwW16GPZC7eIS9SkNmP6HvGYX6C4_EG8wAdSZ8xs0rQEtYqXzncA03biWfEVJx08exsDOa5UfFCO4GMTuXoA7GKsZEgSAV3ocKJDiBv7ZVa6F1fevqRYu4cN80L5Mq5SFUCofPxaxaZdwVUu6hrlUH-j6vQUroVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=HoY2VmkIu7bG-56WzyeG92oSLVvbPgvoKiw6eziJT6tub2ly-QPG9k7mHrho3DyznwPS7zLfEQSZnoolaM5arn9LGNih7vzD_d49jFc3QHM8Rb8mgrOEbOiLmyMcyaUt0P-8zznu09h4MwCt-wtDoSNA0N21LQH5S6yOq5BrxVhNqelx0d1kmgFq1raE_hwt3BtKKoLqC2Cj0zCxLdaV8qfSQB2aeLJMfa0k6psXzSYG5c9coi1Ah8CaWxmId1Rt76lJkSkKCjpS3lefW4QlbNL3kJlclKP5iSv7XDUQZiGcISGB-jZwPu6BxnIT3SBRkxXrhO0-AZEHvViWJnN7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=BWS61yyzMPjZdzFvUuiHVrkz2QZN5KMFA8bhLTQ3kabCzJ8XplUeh7epc9nq-KETWgKhsvCipeRGMFUGSoEo3ZM5ZlnPdqdPdme6a-WY9OdofeYxErL2f-pRPIDOcgIUi2TVwB4xWER57TQnahUDiqHYNu9RTsD_TOjrCACCP6iZD8NBGaGWQh6geq-xxYR3_knHkW57vrm2mr2Mkl-iMMzISBNLlCkni52PSEOLNGEEcRsJv0-5zZDgVFX5T19g9t_dBCMiU9cwPuu4Z2X3PBbGf6UN-jPO4rSpaXP9FKgJ7oB_yBCMYCD1sKckAyIXm2yvhwIxyfFkP0LpaJYU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=BWS61yyzMPjZdzFvUuiHVrkz2QZN5KMFA8bhLTQ3kabCzJ8XplUeh7epc9nq-KETWgKhsvCipeRGMFUGSoEo3ZM5ZlnPdqdPdme6a-WY9OdofeYxErL2f-pRPIDOcgIUi2TVwB4xWER57TQnahUDiqHYNu9RTsD_TOjrCACCP6iZD8NBGaGWQh6geq-xxYR3_knHkW57vrm2mr2Mkl-iMMzISBNLlCkni52PSEOLNGEEcRsJv0-5zZDgVFX5T19g9t_dBCMiU9cwPuu4Z2X3PBbGf6UN-jPO4rSpaXP9FKgJ7oB_yBCMYCD1sKckAyIXm2yvhwIxyfFkP0LpaJYU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=m3JaoJQg5pj53Jl9vuL-S9_ZuZgnDO6i09BqBP6K5aaOYej5ejNDl3fHhbOkLv2TkEpR--1W4o7F0yEbu1qkGiG1sqYXUZZaOFZQI1VfZFRDQX0rykG1A7ls4UKsABppU7N0R2lU46lYOahtzwo3VxV4ASut-p0yG4_MTKtCtBi8iyHNX4owoa8eVd4q2TMspD5QGlvaAg1odwrbKVRNIpGGZSirovD-UnE6gz4MBE09Y6FVKTrTTwvvapVsPGd2fboHd3C56yeV60BrLMr8z0jXUjEUznbqEuB3AreRn2DQPe8yd2esP7f6bDCtspNuH289s3EmQn4RzN628kgSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=Zto5xFimVJtZRFIH3Jo07xOAktW3e839kBIz_TrKSvYv9uIWC4rTObIEPSiYznpqR8OaIpcLGmO3am3smgmq1gZntfLpPT-RS0VeWeg4O6H4vVaO-ek-MF-VFAK4tlYsZiBgoi2puLC68AHXvfeuWpZ8Oa-lfKKhmiFZraFn1zAaX78rMtRvWwyNjQLC7f4ndTBxgbdwizDNsvMFUCcVKC5VrpgwEZ5qItJHjJI3WdgApVl1cPSmvrzqb61qkv2KktyS3RwBgJh1DxL8rl4qBtmXBpX5iobqOSvhBpMRpU66fPqUAsaLfzIxYl83-IfzTbPKleoey8ayvcq5o9GOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=uWGAYmz9sdVaV3SAcEn44-N_BMTQMAim_qIxGdsGF-Cq7yWflyf3Ms7nscWcMIDJ5sOcdcX2SOEqPwjQ8FK7OFLmQtsJT1vc70GtyAuKzycwsfMkUpqCl7RHEqn0V8IVo1zUjYDRwfRasfrMcyk3TZYhbmK-lafFkguWamJyrugvSOphCxesh61hj7QIAtBH-FeSqvObUYqr-FhCTjitcnsg_uW-DxWUDQlyJXuRiX5Q-Q1kAAZZoj1VLXrgKChjLD2hV4yac0z-aUtumMjR-Ibgb-i3wH6Q1vgqvF4cYppHOKFkIxjkg_h4RyDqgVuZpuL3CP29k5H62Tp1hl8lyDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=uWGAYmz9sdVaV3SAcEn44-N_BMTQMAim_qIxGdsGF-Cq7yWflyf3Ms7nscWcMIDJ5sOcdcX2SOEqPwjQ8FK7OFLmQtsJT1vc70GtyAuKzycwsfMkUpqCl7RHEqn0V8IVo1zUjYDRwfRasfrMcyk3TZYhbmK-lafFkguWamJyrugvSOphCxesh61hj7QIAtBH-FeSqvObUYqr-FhCTjitcnsg_uW-DxWUDQlyJXuRiX5Q-Q1kAAZZoj1VLXrgKChjLD2hV4yac0z-aUtumMjR-Ibgb-i3wH6Q1vgqvF4cYppHOKFkIxjkg_h4RyDqgVuZpuL3CP29k5H62Tp1hl8lyDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=nadKyBYCtKVEEQo4hT5KcQth_n_GwYOG16Wl0JKjASW0yMevgOsaYu9WqmqeGDpkSfBh5fQEVak0glNRyaH2GNR-P2Ioq8-d5liQMH0r7YZxU016TyzMQVhpFERE3OQbW8PcAKcBuN0zP5rEzrXWcW-N0XNp9c6EQRX3nYL0vli30GBraMkLyK4Rr-QsvQaHV296AUalyP4oDoDOKq5rezAxAkUha2G9gxF_Hr2ujF15wj2pCqw4lQ-WPTK04lQg13bcytmmP9Kv8fFSlcjss7WK1AEVRX2bvO91OSf5egGrlL_Bcox91GoVKakdmP8DxRFZ_lPLvmxYW7_sndakxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=nadKyBYCtKVEEQo4hT5KcQth_n_GwYOG16Wl0JKjASW0yMevgOsaYu9WqmqeGDpkSfBh5fQEVak0glNRyaH2GNR-P2Ioq8-d5liQMH0r7YZxU016TyzMQVhpFERE3OQbW8PcAKcBuN0zP5rEzrXWcW-N0XNp9c6EQRX3nYL0vli30GBraMkLyK4Rr-QsvQaHV296AUalyP4oDoDOKq5rezAxAkUha2G9gxF_Hr2ujF15wj2pCqw4lQ-WPTK04lQg13bcytmmP9Kv8fFSlcjss7WK1AEVRX2bvO91OSf5egGrlL_Bcox91GoVKakdmP8DxRFZ_lPLvmxYW7_sndakxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=bl7ffhF1NJs86aJaR7yWfA1pFk1S7Wley3P9lOLaGCW1BOydISJh68K6Qgj8JPqeySP4cT-cHE1pUt3QGjjW3_DC5n3YS_l8NED8-Vzmtsfg1FTZAbFa9xdyYL3mw5T3J82YFF_Epy0ac-nTMDPzISfxzK31jDTe3SPhnx3xBlBd445Sr0q_LbVB6PUzMZ7-SWi61kU3n8i9FV6S2drgwtCgJStBXyADlDXdhMfvme2AIpc1s8G0ZzoBGFFIamKofO5517Wbg6ZgnSSnvAZVyB_ZKTXbIliBDKWIVDNzc4V_aAdx8tgtbMnYTwaF2bQCuqkOoGEQqXJQdcrngJYlxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=bl7ffhF1NJs86aJaR7yWfA1pFk1S7Wley3P9lOLaGCW1BOydISJh68K6Qgj8JPqeySP4cT-cHE1pUt3QGjjW3_DC5n3YS_l8NED8-Vzmtsfg1FTZAbFa9xdyYL3mw5T3J82YFF_Epy0ac-nTMDPzISfxzK31jDTe3SPhnx3xBlBd445Sr0q_LbVB6PUzMZ7-SWi61kU3n8i9FV6S2drgwtCgJStBXyADlDXdhMfvme2AIpc1s8G0ZzoBGFFIamKofO5517Wbg6ZgnSSnvAZVyB_ZKTXbIliBDKWIVDNzc4V_aAdx8tgtbMnYTwaF2bQCuqkOoGEQqXJQdcrngJYlxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=AgVCrL0i1MsZYdonU1TjMC-GziXwGEcQUzZhCqBJGRTCu6gGij3ttfYtFNLr9IGcFyzG0gxIpW7cVHDlK9hSJzxyRzw6HgtsSovolRHG85EMH7PLJLejhDiEESNonOCKr2QaWfskAXZojab-EA8Nb4IjojPmU-zL33wUkyk_s1ceRGpI92P8FGGVzK7EEO_q1UpTPxgVp_44Sq6RGTo619RksG6wiBiFNS884c0pVBDAzgVn_HbOLd-5xkmJ8THrxg7S8K-13hXd-ZMuq5hOdOcK3cnXunVP6VUQIEHB2vc2tqbdlNuNW8Bl80YyDooXUXXUBnTHmtgC-By5_RB3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=AgVCrL0i1MsZYdonU1TjMC-GziXwGEcQUzZhCqBJGRTCu6gGij3ttfYtFNLr9IGcFyzG0gxIpW7cVHDlK9hSJzxyRzw6HgtsSovolRHG85EMH7PLJLejhDiEESNonOCKr2QaWfskAXZojab-EA8Nb4IjojPmU-zL33wUkyk_s1ceRGpI92P8FGGVzK7EEO_q1UpTPxgVp_44Sq6RGTo619RksG6wiBiFNS884c0pVBDAzgVn_HbOLd-5xkmJ8THrxg7S8K-13hXd-ZMuq5hOdOcK3cnXunVP6VUQIEHB2vc2tqbdlNuNW8Bl80YyDooXUXXUBnTHmtgC-By5_RB3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjNEl3EW9cEreBiwf403UcMkXAn7B_VqwXmow14zgY5Hn1K3MBalphmOpetbyNKIH7u15l_w00FzF8eCpGp0-uwHVPjqx2o_p1Y4A9rNRzojIaVqbYIoLvscx9PrGqeDIilM6LUkLB_4NnYiIyp8-678Ud1xNTXhc1oNTv2Y4_3m9K5d5NcKcGkRjqRl6IGuKRWjPhRxm9t1B01vX0qI7G5D9x8YHOgMngcksmkEFKCNZStKGIYW3uDo57Yyv_Es34xNok59mlqLJPg-cgH7S7lAI9m7v6kgn92Lw2tGMP-iUmDL8RGRxj6bl-VmZEvu55mTkDkzitNUqHkq7lxy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=TMYBm1_Y1dlIemtsdO8wNP6CJQhfoqKuCKtWjNZnI4nazt2_ruacMb5ynLpGqyxz0XfIzuUQk2Bto5ebQlcrYj-o1vURIJNe2QUjUAl8nSbVef66TE69EEhcnJVA_4CGcDOlbQkKCmg33nPQbl18A_GK4PfVNOxuLMf7UYDLxvA9gfjQ1Ng0zDTbVZXDI2MDSNtB71MRjBOgGNIC7_kXS0-11FJo91VUOLTV0cP5WmOaH2_y8xBZfle3RfeaC2I9IMxOd97L9IHwwpQmyiFbUPIvj0_C5FQdjZj0OGtA8ZAyAd2T0jntnMKnVmvXCgjqrLBvhZJuGDR9xyjtGNYk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=TMYBm1_Y1dlIemtsdO8wNP6CJQhfoqKuCKtWjNZnI4nazt2_ruacMb5ynLpGqyxz0XfIzuUQk2Bto5ebQlcrYj-o1vURIJNe2QUjUAl8nSbVef66TE69EEhcnJVA_4CGcDOlbQkKCmg33nPQbl18A_GK4PfVNOxuLMf7UYDLxvA9gfjQ1Ng0zDTbVZXDI2MDSNtB71MRjBOgGNIC7_kXS0-11FJo91VUOLTV0cP5WmOaH2_y8xBZfle3RfeaC2I9IMxOd97L9IHwwpQmyiFbUPIvj0_C5FQdjZj0OGtA8ZAyAd2T0jntnMKnVmvXCgjqrLBvhZJuGDR9xyjtGNYk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WMRmUnv8AgqhCXsTzpuEiHew7fCGlAo8yFzeFku41raqPhjFjtnzC4_lZv-v9DQnv2raNegGRKlx3U1fttRY-yz-B4UY1TSyrDYFmDW_VlU7C-mwAMIOcJ0L932G4mbjlGaUfM--ucnAqXRT6zm3nP7Nrx5V2IseF-clDl_Gyw9r-5tXr5KwTvwSH7Wf1TIkaJFIkBd61pPG7RMOutQthSX7qE74REraZuOSS4v23H8NzO2OUAqU0zBHd_DtC3U_oPKp0O3ZNVdA9K3lx-Td4QTPcic5doNkNDhbBdN0uP0w_BRgsSsJSACYw9Vs0eAkWiJh0C3w8zW1B8d4FNjY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=bRU_7Dd0AZTuJsUYYuvxfSErPKDHFuuH_eFCbyZ-hd9AkCK-BFs7WYx1hHaTzBuTkCLOafIpIjx0GdeJo4iiq4ErbJsuafJjDZIejj876J9uVTJM5QzaQNFXLvJNI0psGJX6R77rMufijZ3F-GRlXls-9WEqe9RCCnCQ5Mn4EipE9OAzmOlIfGnAzBszVjOpMz-eambTPaJ_tEJ6l97XCX7blRhpzyS7kYJTBEHGmaCQBrrIPIBcLsnmr1G1990HTV18jF3QMZkHzneoqk8NonWunSK4Sr3JVQ0rj2F_AnOiUNguPWiXR89hwQ6GDr1-GojtefPZLXOV4fG1r7FYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=bRU_7Dd0AZTuJsUYYuvxfSErPKDHFuuH_eFCbyZ-hd9AkCK-BFs7WYx1hHaTzBuTkCLOafIpIjx0GdeJo4iiq4ErbJsuafJjDZIejj876J9uVTJM5QzaQNFXLvJNI0psGJX6R77rMufijZ3F-GRlXls-9WEqe9RCCnCQ5Mn4EipE9OAzmOlIfGnAzBszVjOpMz-eambTPaJ_tEJ6l97XCX7blRhpzyS7kYJTBEHGmaCQBrrIPIBcLsnmr1G1990HTV18jF3QMZkHzneoqk8NonWunSK4Sr3JVQ0rj2F_AnOiUNguPWiXR89hwQ6GDr1-GojtefPZLXOV4fG1r7FYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=X43KyxbqifdqLj0ClWlp3ikTVt1sF4CTKoMZW6eEIUO6HfwRbo4iPOi2jphnGP5ViPq8-wrayuoM1fBrW-3paTlse3TxAdgYw9qpDGQ2p49P_1J7JC3yekUuP4W6wMaF24qXW-Cik0XmYZd-2W1XiR1d8Z5v9C56M_issJpyjhdV7c1ixNGeJklhPI7hObqXlw77SniXC_9MD_uxihNCLzd7fLWyTQBe7ZbXfi1_I4mkIux2oNgKXvvRy5BpUIoOrjGr7Ddr77BMDeUSouzd48BvtRrJoutbrRnqq7Ox5wpqZEBbATb8FGbJtlmnBiT-uKV-9WmihwBACBWqJZwkVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=X43KyxbqifdqLj0ClWlp3ikTVt1sF4CTKoMZW6eEIUO6HfwRbo4iPOi2jphnGP5ViPq8-wrayuoM1fBrW-3paTlse3TxAdgYw9qpDGQ2p49P_1J7JC3yekUuP4W6wMaF24qXW-Cik0XmYZd-2W1XiR1d8Z5v9C56M_issJpyjhdV7c1ixNGeJklhPI7hObqXlw77SniXC_9MD_uxihNCLzd7fLWyTQBe7ZbXfi1_I4mkIux2oNgKXvvRy5BpUIoOrjGr7Ddr77BMDeUSouzd48BvtRrJoutbrRnqq7Ox5wpqZEBbATb8FGbJtlmnBiT-uKV-9WmihwBACBWqJZwkVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=CaNWaEC73u2ULMKSOuhR15N-fadNtNkx1Gb4kHqRJBfNZdCI3AmmGmy6ARd92MuGIjm21Af-rDqEdl3w9uCfu8Br1BmtPUzvKDjsqpDeWt-nZFG6awIFXVLGMLCrxlNCvLdePU8LO5gBRGA_4EQnLHQjJnUy1Im1rALaixXdjHo6LEo8civPfcIL4utNczTXzH05m7-53_AQkmRo5muI74IS0owetV6nhlzK40NtaSyftTA-OC7qpnew2rMulBwF96NhOcrjWBsANxbgtO-8jLTrXkYbGIvmfk0IziGcc_MZtAIpiWZoQWtKnZ3OD8wkTS04XDP8x0Easg9brRbG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=CaNWaEC73u2ULMKSOuhR15N-fadNtNkx1Gb4kHqRJBfNZdCI3AmmGmy6ARd92MuGIjm21Af-rDqEdl3w9uCfu8Br1BmtPUzvKDjsqpDeWt-nZFG6awIFXVLGMLCrxlNCvLdePU8LO5gBRGA_4EQnLHQjJnUy1Im1rALaixXdjHo6LEo8civPfcIL4utNczTXzH05m7-53_AQkmRo5muI74IS0owetV6nhlzK40NtaSyftTA-OC7qpnew2rMulBwF96NhOcrjWBsANxbgtO-8jLTrXkYbGIvmfk0IziGcc_MZtAIpiWZoQWtKnZ3OD8wkTS04XDP8x0Easg9brRbG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=HIo1Rri7vH8BMQdFCbHoi8XDKDT0AaZau-utaUcnB5ddXcxlBqY84cGaCJbssBNomiXAJUhCSoEw6ISi-gYEHd8AhZSXI_fig1_lz5lZ_-hFHv26MOMfGvQMbbkNtLiuu4W3GMrsEl23STsbBT23EDrQXB_9kZhn6oAPyR0bMPoewEJ3APsoWPmX0XGrj809XCSF_Q0xuUP2wZ59E8c0MpNMhSsPCFeRjcAkwHCcjANg-SmbA-Gjd7HP2ipKVN-WswtvOnLYOBtwVnYxFPRoSzjAstY54ZhxEywRvxj8AVxUg9vn8o6bykerSV5gPrljS2R4pshSIhu4p0iC39blJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=HIo1Rri7vH8BMQdFCbHoi8XDKDT0AaZau-utaUcnB5ddXcxlBqY84cGaCJbssBNomiXAJUhCSoEw6ISi-gYEHd8AhZSXI_fig1_lz5lZ_-hFHv26MOMfGvQMbbkNtLiuu4W3GMrsEl23STsbBT23EDrQXB_9kZhn6oAPyR0bMPoewEJ3APsoWPmX0XGrj809XCSF_Q0xuUP2wZ59E8c0MpNMhSsPCFeRjcAkwHCcjANg-SmbA-Gjd7HP2ipKVN-WswtvOnLYOBtwVnYxFPRoSzjAstY54ZhxEywRvxj8AVxUg9vn8o6bykerSV5gPrljS2R4pshSIhu4p0iC39blJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=PGldITzkx7R9BxQWI12RX6pdtvgOWtYqOgzF3c8B650bwcHoIhD3VT8KT-3nJ_i9epJC_R1Zc0VWPeLrP3LogtDnn00CSzr5mf2er7sOhSr-aLh-jjVEr-9LaZLwwDKuYo1o7wTnY-cc10J3Tl8KTnYFe5XkPZveNtNPTyxQUicOw3cCEiadSHkyprlt-6wy254XiUP9bxYMKTytzP5effau3CTkkqq37FhJcmp0ux7lveDHBhqAcS9F3mHM0ibuu1hX20Rf5GgS7inb30YI3iynAFwyLPjFDdWY0QBur4B6hdhuRWWwF6XZynxaK_PqxOig-7i0pRCw9woV2fBA3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=PGldITzkx7R9BxQWI12RX6pdtvgOWtYqOgzF3c8B650bwcHoIhD3VT8KT-3nJ_i9epJC_R1Zc0VWPeLrP3LogtDnn00CSzr5mf2er7sOhSr-aLh-jjVEr-9LaZLwwDKuYo1o7wTnY-cc10J3Tl8KTnYFe5XkPZveNtNPTyxQUicOw3cCEiadSHkyprlt-6wy254XiUP9bxYMKTytzP5effau3CTkkqq37FhJcmp0ux7lveDHBhqAcS9F3mHM0ibuu1hX20Rf5GgS7inb30YI3iynAFwyLPjFDdWY0QBur4B6hdhuRWWwF6XZynxaK_PqxOig-7i0pRCw9woV2fBA3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBv-aEewbGYrnJic-ltN-OK338crjK7vpZAsc4PYoYZlcUsMKY1aEtS48QXh7_XoyYwKMRD_iHPpl-6MX9cTwysaCVjZxMSB9hgAX6Jl-K-KAcDuWCU_zhxDtJHmOuUhLY8V6ONbWtEAlsJh4QTZ-eT8NO9Ztg_SGrc5HfK_2ulZIK5AYlO6PUUK-6mYigrGxoezRLRXYVu3gZfh3IX9_btYNNE-vhaKPbjyosNHzf8Jqh3PTijmPJ8j-aAZx_5lB-BcsOxvilh-uZDvxeQ--W9YZZUYOv7M63MKksXYpsac5NCXn-gTxcBMNQE4t56jmFRBD_ZDnuMDcYxYmsdekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OChWvb539HNlx6FuTlbEAtdPhEIgd8CCbWlh42_OXoGgTOIqhYLS2pEPl5a2xsRn0Q0tjngnBNRp8H_4UtrSOcdx7qU3Ya-GcTudLbUkAl_jW7FrjElvKwu4JdyfjWj43mTluyM2Vjf2QhtLcBQgRVNXLhvsJgCDbjaonJofbPY1-zUUx7dqe5Ma0tGLRcg1PMCNl1yvC2LrgM0dehmbxlTYWt9OVbiAMo4rpdbn40MrVMqIm7rxng59ipM7WXGOzpyT_ubxHR9pgtsS2OdQUH7B7hG1_awpqnK5YCEpEZBv1QXcDakQOmFMFTScRQg6BbQ43Ncri5ptIlGy-m2t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=uzs0hYXm7b9QcSZCX8g9qenth1Ygj21fXcoNirKtHbiCaU4w3VdMbSgS9Ala-pm_wIwkBl1X6av7P0WL5xK9duOhnBVkyjeG9C_Zk5_NxmMBL7wrYtXgRraCqwcp2zJcDHm2GoNEoCMgLTpFQD8aKlnDnmj131Zo1SC3HZ7bE8G5BzBSAWfv9CctXBSxhVDhTfHIs1-J0pcOXDBbMbw8mWHbQnypMPRZbJ4x-N1plW8AXc_hohcYe8rMPPF_6wEy2u14K2UmhFbObA0R5rylixmZEYtYScnb6aFzGyOUYtmhiHWoVqWdf0vHGeCHkj5yOlNP4x7bBH6BXpB412Dc0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=uzs0hYXm7b9QcSZCX8g9qenth1Ygj21fXcoNirKtHbiCaU4w3VdMbSgS9Ala-pm_wIwkBl1X6av7P0WL5xK9duOhnBVkyjeG9C_Zk5_NxmMBL7wrYtXgRraCqwcp2zJcDHm2GoNEoCMgLTpFQD8aKlnDnmj131Zo1SC3HZ7bE8G5BzBSAWfv9CctXBSxhVDhTfHIs1-J0pcOXDBbMbw8mWHbQnypMPRZbJ4x-N1plW8AXc_hohcYe8rMPPF_6wEy2u14K2UmhFbObA0R5rylixmZEYtYScnb6aFzGyOUYtmhiHWoVqWdf0vHGeCHkj5yOlNP4x7bBH6BXpB412Dc0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cwS50B3pHUhmLNXxC1-RJdgVJlhmhq5-1spN-R8kCYGuAC907T4fP_wQeWHARdJUk6DuoF49ouxjWbuFZcR3xnmxVvd4q76CHeM-H4eBvWdyyo-4EKkxx8vPg8s4ia5sh4JjeW-ykUip2bjcUvMq0Ao_-ykWk9ehwlZ1a2TK97GMG8Ny8Ngme3cmCU5JuShsVe83ZzIE5JcNalOCD22N_XOYXch4V5ArtQ5fgeEYPYU2hz3WUm9Rl-BM-XcZ_uBOU8Ypf72V-fMe2n_RVr7cFOktTnX-4ZIHgUq1qTJHKmw52aw8EyltX6RNUi8mn7iS6eqBJhiRInRx8bHsr71A4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=cwS50B3pHUhmLNXxC1-RJdgVJlhmhq5-1spN-R8kCYGuAC907T4fP_wQeWHARdJUk6DuoF49ouxjWbuFZcR3xnmxVvd4q76CHeM-H4eBvWdyyo-4EKkxx8vPg8s4ia5sh4JjeW-ykUip2bjcUvMq0Ao_-ykWk9ehwlZ1a2TK97GMG8Ny8Ngme3cmCU5JuShsVe83ZzIE5JcNalOCD22N_XOYXch4V5ArtQ5fgeEYPYU2hz3WUm9Rl-BM-XcZ_uBOU8Ypf72V-fMe2n_RVr7cFOktTnX-4ZIHgUq1qTJHKmw52aw8EyltX6RNUi8mn7iS6eqBJhiRInRx8bHsr71A4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=RsHFyvoU67OAy5u_y5O4loSHLrbdyclbvsa4dwpwJWXqnl_54V-ZFGvx4IGlVEmnMppcWLJ1mkvG3EY8Wz7MeY-dOK4zlT3VCPs76op4hfUiZ7yMM5qpOsAwq7vEh1C94LfN_NUZXcxvKjUPoiRyQHO9b9yDhMBJMDdqEnzkACdk_rzsgXQPkXflUSR44nFNaACL09HXm1i106Em7vv9hcNvAam74kl79tqZjrz9eANLXuzxj8AWlyYRcVwo0nSIz8IXsBrakItz5nxfwNMlRlgEPbh47mH3A7Ppe1DlrSYgIsnidtIZVpRUl0s1D8ym9HnfqAbbMA6vwC9AHZVeHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=RsHFyvoU67OAy5u_y5O4loSHLrbdyclbvsa4dwpwJWXqnl_54V-ZFGvx4IGlVEmnMppcWLJ1mkvG3EY8Wz7MeY-dOK4zlT3VCPs76op4hfUiZ7yMM5qpOsAwq7vEh1C94LfN_NUZXcxvKjUPoiRyQHO9b9yDhMBJMDdqEnzkACdk_rzsgXQPkXflUSR44nFNaACL09HXm1i106Em7vv9hcNvAam74kl79tqZjrz9eANLXuzxj8AWlyYRcVwo0nSIz8IXsBrakItz5nxfwNMlRlgEPbh47mH3A7Ppe1DlrSYgIsnidtIZVpRUl0s1D8ym9HnfqAbbMA6vwC9AHZVeHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCyUOIUnGBXOpwOFHXTKpqsI-RRi20PR4jCOWMAx-uYVk4236uDZ4KSMlSd5KYjyarlkLf_KHu8181xiQC09FLNzpAMokShcdrh9KlDvF6cwdNDr2HdLN0MKFqMu0SFCMrx1avZ7pPdOEWzmRrbuQzLpgmobWOk3Lu3y_CfgqnpZguNuSvsS5dZU7nyUkV4jvTIAnjn2P4fyXQiGYUhFQMtoqIoT4OQAFaxVQ4nNLs4UD6JiaU87yedTogWW8dZ-uNBRoPKftrJJLJYikDNORM0MClNTBgQagyTbpZbF-9gID5I224A7zEQgU1JSY9149aZeNFzrCWdgD2Dbgz8Cyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=KEaW-cRC1OHVJyBFqCgl9CZhzcpQ9WOWsex6F_GAsqs4da7cfib01pMRtFURK4n0Kjblp-F65bQQmKmyZEtMner0DFk466oYTnovu2s2S_qDCmeRb_wRSjrXiVCZ_vFINdCEgkS3C_ZXDIVdS1r8Q26ENgzEexhr8aG2a1qsQAeWmEXirvdOdMv-sZQ1ppXLFcr3jHcEBDP3Ecackg4bA0K7NOxQboE0D7OUrXgQzdFkTD5KGkl4ng_fPkCGpZ4drYtVfi86wfUgaEEAC4GJax79udWAZcHxwWCwS_EM9EkuGn-jhelaFjdwRjmITy-rMS1h5c0zh6-dkK5Wz1pkJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=KEaW-cRC1OHVJyBFqCgl9CZhzcpQ9WOWsex6F_GAsqs4da7cfib01pMRtFURK4n0Kjblp-F65bQQmKmyZEtMner0DFk466oYTnovu2s2S_qDCmeRb_wRSjrXiVCZ_vFINdCEgkS3C_ZXDIVdS1r8Q26ENgzEexhr8aG2a1qsQAeWmEXirvdOdMv-sZQ1ppXLFcr3jHcEBDP3Ecackg4bA0K7NOxQboE0D7OUrXgQzdFkTD5KGkl4ng_fPkCGpZ4drYtVfi86wfUgaEEAC4GJax79udWAZcHxwWCwS_EM9EkuGn-jhelaFjdwRjmITy-rMS1h5c0zh6-dkK5Wz1pkJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGwVh3fpK6YesAXTFuAKnvECOvKNMmhqohSRPCGBLLudYyaA741QmOd3yerI7rolgfpEeG829Q3okt-Fn6fLZ6Hj-VBcSqL6DlnMjnAbg7Ro91C4FKyAf1PHMWNd7yiP9tgQZPneLsOSzUxEFBSktS4Q6T9RiZF98cR4xdBIffMXHnUQCMkfYcReBOB_RWt5jhMWuHQPBXs2pm_nmziJNGT528Hk_gSrftKs0cM1k_d5urylQCJwa05ZAPzDjOENYjOG6ivo0IUQA1xVTrQY3aH8i_5vQU57VGshm8NwO0iMPwWtsogo7tjLqEGzqWMTdkTYFbZbeQ6BcF0v8t9uWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LAY4f18-VoHGGrUlI8W7ECvpSipW5e53lWnrhHv8zzH44W-c8mr5fkzqtaltLbqcvHTRK7wIufNhPb7PUqS8PyDxm057G4SwQquVLuDGPBaxWHJSr6FPbNuO8GNBr1uB1coKCUF46MGqYVGqvZtEmHUS78phC_QDMFz_wiQ9ZrZA1SV8v6jrm4Q6SesDrm0GVRwnNrS1q0NJmT-Qz-6JdNnQxxqw4Dc_A6epu0Fc-93Ys16gcuVpsGgW-FE5T9kowA82waYrTfVJGckQ6-hn2YwCKCrI_MoiXIFBnxnVLYnIxc1vdfw2AWYsHmDvxugdqBdXWRoCpATcXfS44_c1PTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LAY4f18-VoHGGrUlI8W7ECvpSipW5e53lWnrhHv8zzH44W-c8mr5fkzqtaltLbqcvHTRK7wIufNhPb7PUqS8PyDxm057G4SwQquVLuDGPBaxWHJSr6FPbNuO8GNBr1uB1coKCUF46MGqYVGqvZtEmHUS78phC_QDMFz_wiQ9ZrZA1SV8v6jrm4Q6SesDrm0GVRwnNrS1q0NJmT-Qz-6JdNnQxxqw4Dc_A6epu0Fc-93Ys16gcuVpsGgW-FE5T9kowA82waYrTfVJGckQ6-hn2YwCKCrI_MoiXIFBnxnVLYnIxc1vdfw2AWYsHmDvxugdqBdXWRoCpATcXfS44_c1PTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=vErI1x3MuE27Uy-yHvySjP9o1G7uLV5Kyf62MfgBwYPRjNJjFP7-fOaWs56QsjmW_Sc7ajs3WO2XHZ8gxIf9wZmXUgQON4luBPKWMfSo7cnVu71_u5lSBDh674Ae-mPJciY2wyGHgR46kdhIl4K773YX2guLHBc9vpObebmwnbF6Dgo7aN7ptgc1d4A64orDAMqjPRLonnt5-eYuBQ5tP55TXBSWiOMxWSzETgLPQHBsMPCtfvoqAAPmjWbQWgpdJi2slDc6ZUXutPc84Jhs6ZugHlWivf2QiQxSOXDGogpv98O67OnRIrp-p-ykz4gYGQYUv3z-6lNtcRGbt6jklQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=vErI1x3MuE27Uy-yHvySjP9o1G7uLV5Kyf62MfgBwYPRjNJjFP7-fOaWs56QsjmW_Sc7ajs3WO2XHZ8gxIf9wZmXUgQON4luBPKWMfSo7cnVu71_u5lSBDh674Ae-mPJciY2wyGHgR46kdhIl4K773YX2guLHBc9vpObebmwnbF6Dgo7aN7ptgc1d4A64orDAMqjPRLonnt5-eYuBQ5tP55TXBSWiOMxWSzETgLPQHBsMPCtfvoqAAPmjWbQWgpdJi2slDc6ZUXutPc84Jhs6ZugHlWivf2QiQxSOXDGogpv98O67OnRIrp-p-ykz4gYGQYUv3z-6lNtcRGbt6jklQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=tcTmaEN787eJmohhCbaW6ce0V9yYpobnnlXjD13MPgZ8IbJ8K8Tv4T30xfDsjV5p4qMd9sjkmTR6N6-QH6HKw1AFmF2UrERAMDMYEhsi7o0UEOjh5CckGeefv1rKGdmTVoVK3DAuz8a0IUnbbl3mQgMlufTiY-00AN_OVAo3S2S8wPB-eicfzniT4H5FNt4NDUTkKq0Hfjl6nQ8Y6YWfiR5TWtINmu6-3J1RyqrmWqZvmFgkuTbvcz1iItY5D9DhLJrZ3ph2gXflMlbTg19Qi6Vm1WSYsYFT9y2JO7CO39N60CqCgWqsIPdCMcxMCh33A_xELWVlH-xAklVwIVmHIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=tcTmaEN787eJmohhCbaW6ce0V9yYpobnnlXjD13MPgZ8IbJ8K8Tv4T30xfDsjV5p4qMd9sjkmTR6N6-QH6HKw1AFmF2UrERAMDMYEhsi7o0UEOjh5CckGeefv1rKGdmTVoVK3DAuz8a0IUnbbl3mQgMlufTiY-00AN_OVAo3S2S8wPB-eicfzniT4H5FNt4NDUTkKq0Hfjl6nQ8Y6YWfiR5TWtINmu6-3J1RyqrmWqZvmFgkuTbvcz1iItY5D9DhLJrZ3ph2gXflMlbTg19Qi6Vm1WSYsYFT9y2JO7CO39N60CqCgWqsIPdCMcxMCh33A_xELWVlH-xAklVwIVmHIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdLcw1PewVc8Yf7hzDvJ_fQuWueAjFW4UmW5VjJ-dIAVAZ7NDL_ag2xp3S6xe8zn-qexbfpdqHU1mZDnSk5f_3ExmjMXp5RszIL3VN93QdYbVtBcoGmtUNx0d-EwDbTlemHSBXJx2sBZ04qiHcS5u8TM2ffwsMPrPYBt5g5RKOdCEQehzYAqfKyqeJgn_JNyWx_tnIxu0jYUlUIJSyZ8q8w4yJTGS9C69KUgDZ0yU3YuM0dkY9l7lGOEN42lf8V_xFMz2EPjDF0XNRhoeyOAWLMSQPUQHNesG8btd1A2pda-fxvDEstc3DEMUSq9zaLbyeNmJLHq9xzBsqnQ6cKAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=th_Gs5pS63hpsthhAbX8_JQW3tU_w0qW80zcJIXjY7HVSnKjuNRMWAOSyzTmILpZ_I8LsK9aJ6ddXWEXrY0ZlsIo6CptM4Jv1932cIOWn9qe3Dtu4xaDWQ7_euAxG8j1Ux5hwoDzGhRz7O-q8U_KYNgV3cBem-odbIBp5o7o0TAgpdV6p0L5skOjZfrwaJAZVv7oxhveeMabIWhVibhhsQB5RBzWj6x4z96_PRcs1NAtEh0FSSh3THfJrim5TjRKjtlxhGPJEQ8E8ipa1PFHhEKwRUTZBYpZXAdbep6yZfYYbn8p4eiYUtM3OQztV6RJ9GJ8v-S8M_MpzOWTvSvOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=th_Gs5pS63hpsthhAbX8_JQW3tU_w0qW80zcJIXjY7HVSnKjuNRMWAOSyzTmILpZ_I8LsK9aJ6ddXWEXrY0ZlsIo6CptM4Jv1932cIOWn9qe3Dtu4xaDWQ7_euAxG8j1Ux5hwoDzGhRz7O-q8U_KYNgV3cBem-odbIBp5o7o0TAgpdV6p0L5skOjZfrwaJAZVv7oxhveeMabIWhVibhhsQB5RBzWj6x4z96_PRcs1NAtEh0FSSh3THfJrim5TjRKjtlxhGPJEQ8E8ipa1PFHhEKwRUTZBYpZXAdbep6yZfYYbn8p4eiYUtM3OQztV6RJ9GJ8v-S8M_MpzOWTvSvOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=EE8QHd7bePjf3_aJVMz0LkYThFEeGzDpTapbZSdouLkkZMGpD9ZbNNb01-O-XWw1WaAdyJeVgV2uJsTeD_gYia0Et85iAGp0NQ9irU5cvdkOarOFFxVm2FHdBgzheuiTxakxKvtRejJJB82UbZSS9UddSg1iPscLmdQDg7t3tIJlBRlE-EUXbJDYgxczKOJxiuNYej4E-WoQNXE4VBDMhdyX9rN24V8tAKOnM4IPqdIuR_9nMrgvyi5VNQXY4mgM8hD5fsqc1gtY2KVbkzcZimy6_Ce3mJhbcnGqUGFXTENdvA84ty_A7doKUWHyC1_1z_bEmWUl7ztAWnjqkOa_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=EE8QHd7bePjf3_aJVMz0LkYThFEeGzDpTapbZSdouLkkZMGpD9ZbNNb01-O-XWw1WaAdyJeVgV2uJsTeD_gYia0Et85iAGp0NQ9irU5cvdkOarOFFxVm2FHdBgzheuiTxakxKvtRejJJB82UbZSS9UddSg1iPscLmdQDg7t3tIJlBRlE-EUXbJDYgxczKOJxiuNYej4E-WoQNXE4VBDMhdyX9rN24V8tAKOnM4IPqdIuR_9nMrgvyi5VNQXY4mgM8hD5fsqc1gtY2KVbkzcZimy6_Ce3mJhbcnGqUGFXTENdvA84ty_A7doKUWHyC1_1z_bEmWUl7ztAWnjqkOa_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEH4eUqfS0BJaxG4h9mbrtjEU0JY2mEGJq1RwJJ5z_43yF0uQ2LwrgJliKumg_ldITqUOq7B4Lc2VNV_gNhndEsZbBK7IsyrYwaM5Bsbhbza28tsuXuK9MTpeJSsfgC_q-RNhKr85Rwq7Rb2p2YAT6OOj3vwL_DrsAfwMSt1F2bDnXj7MEzPHJOiQudzXfGopr_UZrNwMmlHbvyGLYrZlCayH3u7MhXGF9E81KtcxfTpnHKZoGFJOcGkBD5RI02eLcWsAmnBlC-6121Lf2aoSl8Zvee7XIEEanSRQJOBDHfUELeE9iKKAajobgpuFTs6ARjphBWEzoHIdMs49o8m6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK9P4Ge0mxW1Zk2PR_ImMUlI5NvqPBCoJHoNFPzxJjBSNbI1L0DlJSNaSviYsfuWnApApiwMFBg82KE3kx6D1KHGekJvw0dGRPYYDpLV9T9zisCgQfdbjtwTgg29ozEaMFk7jGwGAH7DLwjJ7yLUHfjlc4-XZBmE3JphFk4rKO8Yydbw6z_9AWumflu95bNTFjgWjkBVMMlIURTGIpNLTmQCa3iXMF1AytFer6rSgtJqx4GL6nDiz2ZKHrSL9uAyoJlx0SMKy8EeaTlD8dUjveBd2PMJ9qphDy7Hglmn0t9suzg3ttqdklM35RFijaHxN4aEhRg0jJ4C87R23bM6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2SEEUcO5VoSsVbpio5K9qhx6_NZBpkHIOcWQ2MDtGLeF0GAaJaR2FE5hPG5Ap0O3meEw2yURY9xA0Fxc6HEmmmScaTm5LLL69RYyNE5LefXKGKIAfEfLevZcalfOUibfwfjOIIB8fJpGx6Bynt45-3kBkHPpGreo3joA5UW70ZdaV7AeKVu1f1kHQA99ZR9Qs-35dbqbSMHkt2-no44rmHwdAgroPgtcJsJm2lo7dhkAYIu1lESiddmte9DVvUi6NwxlrkQil-IeGGi47tAuTxkTxAq5LpAtTwxpOD-9PREB2PQdtUJzQCTWqEJdwZaGcKrlE_59dlm9en34WYCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=rf2JB4z9i8nKIODZN5Eze2bX7JPUTVWoCVeFm3sDFhEiVm_7iAfp9G5rpNXUu5zItqaDF_c14BYCTiRukaj7zGe90cKa0baTz3KCIJYreN6zENsdnj6OOKlj4sNZg8MkzeWGnpavMe4o2Mxys_DGbmUPdmPDBRsUeaZn4lc0I4XGOR4yTA7_WNgCuWFT2K4dnP2MVMV-cp7ltLEsVyEFa1Xn4MLPxZKX20XHeg6bsfxR3bMPka2LSsFZ1M4VBe-RurD1Nh2c81jUigCLCS31jl2Tj9gbd5V1CQJEIHI3X52icbh1fmnnkrs_PEygmr4CIST_1Ifm7QrKSBaXqyHeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=rf2JB4z9i8nKIODZN5Eze2bX7JPUTVWoCVeFm3sDFhEiVm_7iAfp9G5rpNXUu5zItqaDF_c14BYCTiRukaj7zGe90cKa0baTz3KCIJYreN6zENsdnj6OOKlj4sNZg8MkzeWGnpavMe4o2Mxys_DGbmUPdmPDBRsUeaZn4lc0I4XGOR4yTA7_WNgCuWFT2K4dnP2MVMV-cp7ltLEsVyEFa1Xn4MLPxZKX20XHeg6bsfxR3bMPka2LSsFZ1M4VBe-RurD1Nh2c81jUigCLCS31jl2Tj9gbd5V1CQJEIHI3X52icbh1fmnnkrs_PEygmr4CIST_1Ifm7QrKSBaXqyHeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=pw8aVF0mIxaAzaONqvgawP5M-rhz7IyIlAqRoQ_NLVNPovhnExdLw8FMgtP5XSfCi_tb3I-Z5L3okhWZcgYR4pI9CVPmPbaTgrtUFL31Ln2r9l3yMzYpPp5iqkh44XryRJol5NYvD3nLUwvhrQ6WubRmGTKG7udSRDMBMZUD7KP1eiqYDXfiNdOJk9jGwG5yeTj038u5d7gN0OtApRPZkkFadQ1CsmKfN4C3e1GC5gTILi9wmg5BmJWKAfxzsyM7bWJbh8V6PDVdy9Vc-ERHgxHJd035VhXqwnzHSG9GQecTlZZcDX6VIjeDYh5mTFsLk6Cmp7GpVTO9CeH0XMcloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=pw8aVF0mIxaAzaONqvgawP5M-rhz7IyIlAqRoQ_NLVNPovhnExdLw8FMgtP5XSfCi_tb3I-Z5L3okhWZcgYR4pI9CVPmPbaTgrtUFL31Ln2r9l3yMzYpPp5iqkh44XryRJol5NYvD3nLUwvhrQ6WubRmGTKG7udSRDMBMZUD7KP1eiqYDXfiNdOJk9jGwG5yeTj038u5d7gN0OtApRPZkkFadQ1CsmKfN4C3e1GC5gTILi9wmg5BmJWKAfxzsyM7bWJbh8V6PDVdy9Vc-ERHgxHJd035VhXqwnzHSG9GQecTlZZcDX6VIjeDYh5mTFsLk6Cmp7GpVTO9CeH0XMcloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=lhM3GFW8f1kDhI2fc8LDbZ6PjL5xvXQ1517HnSayLvwCTNhz_foMHk_Zb-7dvAqpOsRCqV6Ej_g_At-OPG2Cw1oKKOzEhWYQpm2jNBkCCR_22Yelv1DOxELiZhGlADL1D9es4MhZWzxN2WcWjuSQq_9rakat49XUPVd_urjicJYCYKbfp8Y68wZ0cL7VFkmUBkGPTIYK5AO7MVaoAhZs1Ipg1Rtn9XqmJRX8qjtdl7AYczFzYwEIoTjHSoQ-ylSMIYYvq8VrmDx2vJwhpNyXWcH6W0kISpH2cdaS71whCdwom4FVdDj00ZkzsgUPPYvikwVsCacc-EpqRiDLwQAWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=lhM3GFW8f1kDhI2fc8LDbZ6PjL5xvXQ1517HnSayLvwCTNhz_foMHk_Zb-7dvAqpOsRCqV6Ej_g_At-OPG2Cw1oKKOzEhWYQpm2jNBkCCR_22Yelv1DOxELiZhGlADL1D9es4MhZWzxN2WcWjuSQq_9rakat49XUPVd_urjicJYCYKbfp8Y68wZ0cL7VFkmUBkGPTIYK5AO7MVaoAhZs1Ipg1Rtn9XqmJRX8qjtdl7AYczFzYwEIoTjHSoQ-ylSMIYYvq8VrmDx2vJwhpNyXWcH6W0kISpH2cdaS71whCdwom4FVdDj00ZkzsgUPPYvikwVsCacc-EpqRiDLwQAWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=Gbc1bKKSDuOgG0nlE0oBIX8NekksMclXNKgr6PYTbky2kVj-o7rCiv5nyg3oS6doAnjBUYHdPQsATHGWvUqgJUiqVT5tNXsoaGDLnVtSIj7i7gW55CRZR_mYOK6KrGD-T3ktKgZexwZ92KJ6FvljRt_0lZQE-bZbmHLltrVtbCyrO1YMolviiafYMYGimJYFkiI1FrVixC05aT_2e1CxEGJfpXH3PR5NqKSIOo0WqqR3RVmPb0qa_xvTFznmxrq0mVa2g5ZMriFR3Xw3rkkwPq88hlZFuISqf-d7R-yr5mM1LpcwD9LmHv0HPGb5L-eqOcoH8k7OAJ9Bg2rXMIHUAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7913d873f1.mp4?token=Gbc1bKKSDuOgG0nlE0oBIX8NekksMclXNKgr6PYTbky2kVj-o7rCiv5nyg3oS6doAnjBUYHdPQsATHGWvUqgJUiqVT5tNXsoaGDLnVtSIj7i7gW55CRZR_mYOK6KrGD-T3ktKgZexwZ92KJ6FvljRt_0lZQE-bZbmHLltrVtbCyrO1YMolviiafYMYGimJYFkiI1FrVixC05aT_2e1CxEGJfpXH3PR5NqKSIOo0WqqR3RVmPb0qa_xvTFznmxrq0mVa2g5ZMriFR3Xw3rkkwPq88hlZFuISqf-d7R-yr5mM1LpcwD9LmHv0HPGb5L-eqOcoH8k7OAJ9Bg2rXMIHUAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ در مورد پسرای زیر ۳۵ سال که موهاشون سفید شده، در حال وایرال شدنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71048" target="_blank">📅 15:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKVE2FiyqVFTzEx8B2YqzJeTNgj5jnym1g3Fzbww7HUW6ePJHH-46QsqeYKrqdVGw_BHWcL1sHBvgKsgr5t-kcqIp7tRuVz4TmjKSvCcJ6oLgI62vp6EdJ30gQA3okmT2szDS2hDUx0h4c6EUj38nbT0VAk0w6v983kGawOtWfbgc2zOCNOEOURSwah81xMLQLRotoEBAtcuuN7Mqefbq4xe5zScBKP8Mx2GncdkeorJ5-6tCIhQ05qptRIHOI8PLFXhOtKwmiTkrnJ_TGwvzOzVekGae5y_L4Yizm4CjVcffckJd83Ja1JAtLAcJeRWF90syE-e8Dxno__4cmCkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خبرگزاری میزان وابسته به قوه قضاییه، روز پنجشنبه ۱۲ شهریور ماه اعلام کرد حکم پرونده صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، در دیوان عالی کشور تایید شده و او به ۱۲ سال و ۶ ماه و یک روز حبس تعزیری، مصادره کلیه اموال منقول و غیرمنقول و محرومیت از اشتغال به شغل کافه‌داری محکوم شده است.
مرکز رسانه قوه قضاییه این پرونده را مرتبط با اعتراضات سراسری ۱۸ و ۱۹ دی سال گذشته دانسته و مدعی شده است که متهم در «تحریک اعتراضات و ورود خسارت به اماکن و اموال عمومی در استان قم» نقش داشته است.
صادق ساعدی‌نیا، فرزند محمدعلی ساعدی‌نیا، کارآفرین و نیکوکار ایرانی است. محمدعلی و صادق ساعدی‌نیا در جریان انقلاب ملی ایرانیان در دی ماه گذشته دستگیر و اموال هزاران میلیاردی آنان مصادره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71047" target="_blank">📅 14:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:  اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت. ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71046" target="_blank">📅 13:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=wAE0e4i9FwOECspgLFcFg_7JGFFjUCMhYLpjmy5BDpybZ03NmAash9Gk7UrfWmGDoQROq47OsS9HMk_85HNvkXHGbMZhn_xShkUF5ILc0ZSES-J9P6JWgVuVPHRfUpWtHuVXQmL3EAKg7HEshsG8ENEh6kpyJQ6S1t353Yhi6aNQORoP49P0II7y6RX0kkP1ibOGyyW8LAJNF7L1XV-lYWJsklT4vI538yGheShFR3Yu7e9k6CSkXB-YQjFq34bhCpZBinpIRXMVQtXTLQq0h495W9b_N5nxV3mEgXEhdq_DWZegvfn3Ap_ZSnheMPu74Ac_1MYZim4NRFMCZjlQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7750e2ea67.mp4?token=wAE0e4i9FwOECspgLFcFg_7JGFFjUCMhYLpjmy5BDpybZ03NmAash9Gk7UrfWmGDoQROq47OsS9HMk_85HNvkXHGbMZhn_xShkUF5ILc0ZSES-J9P6JWgVuVPHRfUpWtHuVXQmL3EAKg7HEshsG8ENEh6kpyJQ6S1t353Yhi6aNQORoP49P0II7y6RX0kkP1ibOGyyW8LAJNF7L1XV-lYWJsklT4vI538yGheShFR3Yu7e9k6CSkXB-YQjFq34bhCpZBinpIRXMVQtXTLQq0h495W9b_N5nxV3mEgXEhdq_DWZegvfn3Ap_ZSnheMPu74Ac_1MYZim4NRFMCZjlQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
اگر ایران به دولت اسرائیل حمله کند، این اقدام اسرائیل را از هرگونه محدودیتِ موجود برای حمله به ایران رها خواهد ساخت.
ما به تمامی زیرساخت‌های ملی، نظامی و غیرنظامی ایران - از جمله زیرساخت‌های انرژی - حمله خواهیم کرد و ایران را به اعماق دوران حجر و تاریکی بازخواهیم گرداند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71045" target="_blank">📅 13:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71044">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=RtJyIQZPpOkRuPl8BMv1UX37Cn7mnM1ZPmthKOE1SdnuDyQhJKXSpwK5szyWUysL8r64esPqcrkbQjicrvRsMBNrILnHm7TE9iPLOjBIQ3FBpV-DXlroVe8sbs40SZinc-hSv0AQu4nMG66MDAo9LCsz2KSaeQid45zJohKiqpP38rSoPEsr8rwJ3uzLh-Rl2NAzmxXWq-85zQ3Wm5zv95LkboelETCE2_ZKj6auowkDAPGbIgynds5Tg8wUrVPtCN8MFWbMJFUnHKrm_Kl-YUnpuzRM14iShSLfaygzFELd-faNXLGUDjKmhFdbspTgYO0nxNFfENaWvY02Y08mOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b05262cb.mp4?token=RtJyIQZPpOkRuPl8BMv1UX37Cn7mnM1ZPmthKOE1SdnuDyQhJKXSpwK5szyWUysL8r64esPqcrkbQjicrvRsMBNrILnHm7TE9iPLOjBIQ3FBpV-DXlroVe8sbs40SZinc-hSv0AQu4nMG66MDAo9LCsz2KSaeQid45zJohKiqpP38rSoPEsr8rwJ3uzLh-Rl2NAzmxXWq-85zQ3Wm5zv95LkboelETCE2_ZKj6auowkDAPGbIgynds5Tg8wUrVPtCN8MFWbMJFUnHKrm_Kl-YUnpuzRM14iShSLfaygzFELd-faNXLGUDjKmhFdbspTgYO0nxNFfENaWvY02Y08mOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
جنگنده میگ-۲۹ام‌یو۱ اوکراینی یک موشک اس۸۰۰۰ «باندرول» روسی را در ارتفاع پایین با یک موشک آر-۶۰ منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71044" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71043">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162568634d.mp4?token=HtDCYS4ZugFBVckJnnA6YlnR6IkfGh_RdfKTBe-8sgx_9R_VKWoRGWIsz9-x58pSH1uL8XbMIpaUQEefte44Y2V3GmA7ciiVfaV7KKiVJkPO3S5OUHLuP_i9flFs5aRJqblTDxt9tlEmfKN0B_0l8jEGd_QoIpoBGPHSN-NvBgHPmEEHsSTqk0wB9r60YiOnLv6hiJDcRmfr9y4r93XLdpknugq0xl-s2npDUAWai9ZOX2UFt1oGAyQAack5n7kbWAZrzcBXFa03t8V_M5S0kz_GuN9P7cjzNrpvQthdJHNqEdje-_aBBEsZBoA8PzD0PnYSZaWEJWyRQH6nC079EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162568634d.mp4?token=HtDCYS4ZugFBVckJnnA6YlnR6IkfGh_RdfKTBe-8sgx_9R_VKWoRGWIsz9-x58pSH1uL8XbMIpaUQEefte44Y2V3GmA7ciiVfaV7KKiVJkPO3S5OUHLuP_i9flFs5aRJqblTDxt9tlEmfKN0B_0l8jEGd_QoIpoBGPHSN-NvBgHPmEEHsSTqk0wB9r60YiOnLv6hiJDcRmfr9y4r93XLdpknugq0xl-s2npDUAWai9ZOX2UFt1oGAyQAack5n7kbWAZrzcBXFa03t8V_M5S0kz_GuN9P7cjzNrpvQthdJHNqEdje-_aBBEsZBoA8PzD0PnYSZaWEJWyRQH6nC079EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
روابط عمومی ارتش:
در ادامه سلسله عملیات‌های صاعقه و در مرحله سی و یکم،  در انتقام خون پاک مردم بی‌گناه و دلاورمردان نیروهای مسلح، بامداد امروز، ارتش جمهوری اسلامی ایران، «سامانه‌های ارتباطات ماهواره‌ای»، «انبارهای تجهیزات» و «آشیانه هواپیماهای جنگنده» ارتش تروریستی آمریکا در پایگاه احمد الجابر کویت را با موشک‌ها‌ و پهپادهای انهدامی، مورد اصابت قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71043" target="_blank">📅 13:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71042" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaUGnNzqNH9alUKJ4hwIa7tFPraMBWU-jy2dD241jLfsB3GOKDe9IAchbWy9M8rvKHOfDQPBTvKIds69hVqISyaySn-zuJaEwJ-dObZ_4437bNtTmDZ6G8BblzZ1g4GPJWcBzGEY7QvGnk66oRETfO3n5GEHRA17Kc2FN462eLwp_QY8tu6c9GqpKcU9eKKA4k7gRwdVvbrh55J6pRxBWxGCDvsMnALN5mjR2nsAbgIpfTIFTDWPFrAIlTzdovERt2yP0vZXMxcDz1A9g6PLPeGUpn-TUgBDpEDEGOHP54iqyFoup8HunsLs4cF3G9yFQdiofA1bAkmVozBs8x670w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71041" target="_blank">📅 13:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=UW3iDDtOvtQ9uV_OzSUKgT1itV5DK1WskZLpbuTkwg7_fxLQlL5tRqAzBpUb4CIDRBRZ-T9D0Lfa6z3HjgegBVO2l_ytumj57YYiy7rpYTrljWYJtjkDzf0ZdjclZF0mJw7TEg445gqHgFe3vse1YsHjGvbyB3LJFtuWnj4cfioAvCa0vSFEYJivCkYHwt8ZcG-YXj_9OOKoP6vdfDnPOj87zJxsWnOJhFeSr-9Uj0cQLej4-vs8yQACWL0eSiJYI1B0cnJJHNuCrsvCrmH7gJciARayWmO8zALTsWxR6lnJbGFZ6mvTHGEBOBh-owgzQ6XVB4DTtgn1rfX36Vh0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2218c2694e.mp4?token=UW3iDDtOvtQ9uV_OzSUKgT1itV5DK1WskZLpbuTkwg7_fxLQlL5tRqAzBpUb4CIDRBRZ-T9D0Lfa6z3HjgegBVO2l_ytumj57YYiy7rpYTrljWYJtjkDzf0ZdjclZF0mJw7TEg445gqHgFe3vse1YsHjGvbyB3LJFtuWnj4cfioAvCa0vSFEYJivCkYHwt8ZcG-YXj_9OOKoP6vdfDnPOj87zJxsWnOJhFeSr-9Uj0cQLej4-vs8yQACWL0eSiJYI1B0cnJJHNuCrsvCrmH7gJciARayWmO8zALTsWxR6lnJbGFZ6mvTHGEBOBh-owgzQ6XVB4DTtgn1rfX36Vh0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تو میدون تایمز نیویورکِ آمریکا، یه خانمِ چاقو بدست بعد از اینکه یه مرد و یه زن رو از ناحیه شکم زخمی کرد، بعد از اخطارِ پلیس‌ها به سمتشون حمله‌ور شد و به این شکل بهش شلیک کردن و کشتنش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71040" target="_blank">📅 12:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=Tj039WK7l5GviV0X-b3sGvsb5Fn1S6OaFIstBeXRURCq_xkfvEdD7DOPtgRCdTltniTjon56JnTdbjQ0MoaCO9x3dkNBj3U3dcFhSxVox8edqzX9n9qkHXV9uzZmA3giU7sV-uWvnctzUsYSwd9CGVO-7cLa35g9_tF_wX6O16iCbY2QeBB_DHg5BNR45XiZuLmw_fexbw4tQEHwMaLspkYFC8hKPHy8o2Omf2GI8WaZGCnCmO0MymQmnyDz4TC8CwWI3P33LJ8LH7URfMcnKwBmldVFHJixWHbIH55k9bgb5rnNZE96q8le3FizGCEBYTEm2Iv5ggrNpP0HM4vW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f52d28bc.mp4?token=Tj039WK7l5GviV0X-b3sGvsb5Fn1S6OaFIstBeXRURCq_xkfvEdD7DOPtgRCdTltniTjon56JnTdbjQ0MoaCO9x3dkNBj3U3dcFhSxVox8edqzX9n9qkHXV9uzZmA3giU7sV-uWvnctzUsYSwd9CGVO-7cLa35g9_tF_wX6O16iCbY2QeBB_DHg5BNR45XiZuLmw_fexbw4tQEHwMaLspkYFC8hKPHy8o2Omf2GI8WaZGCnCmO0MymQmnyDz4TC8CwWI3P33LJ8LH7URfMcnKwBmldVFHJixWHbIH55k9bgb5rnNZE96q8le3FizGCEBYTEm2Iv5ggrNpP0HM4vW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سایپا تو ماشینی جدیدی که زده ماشین با اینکه راه نمیره ولی براش کیلومتر حساب میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71039" target="_blank">📅 12:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH_DMNFTl1rFYKzS4muroRMcwLCLBkE3cTKeRFQP2Dhoxn-JRl0XyrQMRU_XOVz6sCB0boFznJ0eO-_KysxcplZ35aE7gchEk_qHcIPXiLa1UgF6BdSs3MM5WaEeomLbEdd4oDXzvihAiv0RJyX8Q1PDpHhVdKsdhrYi_HiAHR9FSexZZoDA9J19eBBkhkMdwbVOv7N8sYoSkdDblsJJowOnPUzx21IX2hThfQB35LrGubxNe0S2hx6cc0oV_K7cYDSUcCTxW4HatrXvyair9jvt9nsIcXlIRKRex2rfMUaJOLn7AkPT1ByDSKXhMXUzZjxYsExzFllnYAeIsC267w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس:استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته در ساردینیا با شیخ طحنون بن زاید آل نهیان، مشاور امنیت ملی امارات متحده عربی، درباره ایران دیدار و گفتگو کرد.
این دو مقام درباره گام‌های احتمالی آتی بحث و تبادل نظر کردند؛ چرا که دولت ترامپ در پی بازگشایی تنگه هرمز و هم‌زمان افزایش فشار اقتصادی بر تهران است.
امارات نقش کلیدی در تلاش‌های تحت رهبری آمریکا برای عبور نفت‌کش‌ها از این تنگه ایفا کرده و در راهبرد تحریمی واشنگتن، کشوری مهم محسوب می‌شود.
مقامات اماراتی به دولت آمریکا اعلام کرده‌اند که هرگونه کارزار مؤثر فشار اقتصادی باید شامل تمامی کشورهای عمده‌ای باشد که همچنان به تجارت با ایران ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71038" target="_blank">📅 11:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به بندر سوچی در روسیه حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71037" target="_blank">📅 10:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef77017317.mp4?token=hIVAI5Uhnayg_q6mN2SzTSPrZ7icajo4mAOQN8tkCsw7GH2sRjTSXxCF0g02lPDjBvWsEOSJFkqxoMy0MJzo2-WbtCFiWhKZAdCj0jSZLqNITMMUvk4xKf9c5ONlqszkjXeX4TiksBMDCHBqHDgS5-trZkwz93-G1WA-YngPbs7FcJ5kUYy9q7VVQL8UiunnnOmov2e_bwpBP5nSzwO2ip4vcDtNd9-Tz8aZ_dRvO7CIFkY9Ress8mQgBS3Wk4OKWxk9Jw7-qERvqYlciiUcjzD6DBwkPc8HS7FgUTUL54h89zlCSHVPrfLyueM6p1AR50OwyEk-BXNGKJiGupXB9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef77017317.mp4?token=hIVAI5Uhnayg_q6mN2SzTSPrZ7icajo4mAOQN8tkCsw7GH2sRjTSXxCF0g02lPDjBvWsEOSJFkqxoMy0MJzo2-WbtCFiWhKZAdCj0jSZLqNITMMUvk4xKf9c5ONlqszkjXeX4TiksBMDCHBqHDgS5-trZkwz93-G1WA-YngPbs7FcJ5kUYy9q7VVQL8UiunnnOmov2e_bwpBP5nSzwO2ip4vcDtNd9-Tz8aZ_dRvO7CIFkY9Ress8mQgBS3Wk4OKWxk9Jw7-qERvqYlciiUcjzD6DBwkPc8HS7FgUTUL54h89zlCSHVPrfLyueM6p1AR50OwyEk-BXNGKJiGupXB9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی وایرال شده از پسری که چالش گرفت که تو خیابونای شهر از مردم درخواست پول کنه(نفری ۱۰۰تومن) و اکثرا قبول کردن و در آخر هم پولی که جمع شد رو رفت به نیازمندا کمک کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71036" target="_blank">📅 10:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=BWU-98ZH01JArWAB_Rz68TD-5r7X4sgcfD8r3El5xwCsll6ZlzsJOHjCIZiGAiMjEsx9amKbPkOI6qquBzXKR4YB2n36lWwREq3fLtWr0WNAcgXUu1MYaoKW7F1podBOYUrhw7JG7UOnMe7AFjAtOJPNre-9d5ZM7sI9SooMzk4jhWsJs4xKhv4bUifCDunmTJ-A7ouYXCOGKgw3kCaqH2aqBHQjNvd3Ew0Ih1FhAtohzwT7hk7Vrk41EOEXN2FYKZ03GdUTuLkQDBX97lECywtOh2-FOIytVG0YqpRgNC6fNPmcnOBNsKdToJO4yEiO10RnRHaje5cFu_6UJ9gi8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de7f7edfa.mp4?token=BWU-98ZH01JArWAB_Rz68TD-5r7X4sgcfD8r3El5xwCsll6ZlzsJOHjCIZiGAiMjEsx9amKbPkOI6qquBzXKR4YB2n36lWwREq3fLtWr0WNAcgXUu1MYaoKW7F1podBOYUrhw7JG7UOnMe7AFjAtOJPNre-9d5ZM7sI9SooMzk4jhWsJs4xKhv4bUifCDunmTJ-A7ouYXCOGKgw3kCaqH2aqBHQjNvd3Ew0Ih1FhAtohzwT7hk7Vrk41EOEXN2FYKZ03GdUTuLkQDBX97lECywtOh2-FOIytVG0YqpRgNC6fNPmcnOBNsKdToJO4yEiO10RnRHaje5cFu_6UJ9gi8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ویدئو جدید از پرواز هواپیمای HC-130 Combat King II آمریکا در ارتفاع پایین در عمق کشور به دنبال خلبان آمریکایی جنگنده F-15E
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71035" target="_blank">📅 10:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=Yk5FcRCfZq8uuDpH_n2Tf8neNPfWO2jHPddxlLWunA6r-LAE-IheMGZn7n_GzAYRM8wfEM33DVOwM2wtz-P6-__VTWY82lUOd9xbgUr734fRxB-DEEF9cvd6RuDs7TKM_bPOXEyUOr6qp_EXol1geCltU32FIKy153uktOBsCNkSLDawU7a_csOo-Bw3FK0nu98p9Ir3rwpqXQdZZBG2KNwBuHygE7ATaEj8KkB8-UehL-EKDRY9qy1h8_8n7KsvkrBfnEpv2OAyytXFMsz2yRw3t288ZXDYC8IoH3wNAyLM8Q6jz_ZKhai1ZLjq-Fva-l62yjZkxTmVDZp5fFvRDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58d044a.mp4?token=Yk5FcRCfZq8uuDpH_n2Tf8neNPfWO2jHPddxlLWunA6r-LAE-IheMGZn7n_GzAYRM8wfEM33DVOwM2wtz-P6-__VTWY82lUOd9xbgUr734fRxB-DEEF9cvd6RuDs7TKM_bPOXEyUOr6qp_EXol1geCltU32FIKy153uktOBsCNkSLDawU7a_csOo-Bw3FK0nu98p9Ir3rwpqXQdZZBG2KNwBuHygE7ATaEj8KkB8-UehL-EKDRY9qy1h8_8n7KsvkrBfnEpv2OAyytXFMsz2yRw3t288ZXDYC8IoH3wNAyLM8Q6jz_ZKhai1ZLjq-Fva-l62yjZkxTmVDZp5fFvRDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
تو یه فروشگاه تکنولوژی تو روسیه، یه ربات بعد از اینکه مشتری هلش داد، شروع به دعوا با مشتری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71034" target="_blank">📅 09:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=sKj2EN0lhRCz-hy7qeXD8yQMbKy-V_iiMlCIUQz-DN0GEMcjSAZN7cCrlbKk12kp0kMjJxPkXtOuIPIWawPEs9h9aAB2dGz1I7F85a0aezEkhLmW7PoYxT_xnAzCqKVD7nS72HdlkpZp_h3wdZ-dOPjr79CxN_Wzo_jahOk1zm1a08TfcR7OIpNMpyeY9v8McRxi5mCww4e-G4Ygt-um4VUKeX3XAK2DyXhdDgXFUcrwLkVGEK1L-kcZ4iWDbskpCYDukVQ2_E-TbqZxYLU6j18eGhUkbCLd2fkMaXAm0HA5bBvTrS1muIHIAWWTEZ13osV81av6D6WJ3C1KHGwYEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73b2179fb.mp4?token=sKj2EN0lhRCz-hy7qeXD8yQMbKy-V_iiMlCIUQz-DN0GEMcjSAZN7cCrlbKk12kp0kMjJxPkXtOuIPIWawPEs9h9aAB2dGz1I7F85a0aezEkhLmW7PoYxT_xnAzCqKVD7nS72HdlkpZp_h3wdZ-dOPjr79CxN_Wzo_jahOk1zm1a08TfcR7OIpNMpyeY9v8McRxi5mCww4e-G4Ygt-um4VUKeX3XAK2DyXhdDgXFUcrwLkVGEK1L-kcZ4iWDbskpCYDukVQ2_E-TbqZxYLU6j18eGhUkbCLd2fkMaXAm0HA5bBvTrS1muIHIAWWTEZ13osV81av6D6WJ3C1KHGwYEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح عباس حیدرزاده مداح درباره‌ی وضعیت مجتبی خامنه‌ای :
تولیت آستان قدس رضوی گفت که شب دفن رهبر؛ مجتبی خامنه ای ساعت ۱۲ شب اومد حرم برای دفن پدرش و تا ۷ صبح اونجا بوده.
وضعیت جسمانی ایشون هم عالیه، هم از لحاظ ظاهری و هم از لحاظ جسمی؛ حتی مسئولین هم پشت سر ایشون نماز خوندن.
همچنین ایشون نیم ساعت کنار قبر پدرش دو زانو نشسته بودن و گریه میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71033" target="_blank">📅 09:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71032" target="_blank">📅 01:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWqqmR0GieHOTkk2SKsMsLFlTUIUQUtRmEax_CReRPzN4W4RX61310CoyzkU2_5E3xhNURu69UcsqSl3aOHY1Vn5xRthq8yB08PDZWEl8ECES4aJaZYfMl9XE1_LrRJV_9Z-SrXBrNmEuHiJusgQoHqL1b9Unr2LH08DszYaXkLZ943l7kBIn7KazV7dkFqYPTpslArBZ2NfzfjGairnKPSMnBHInSaGFsLTDAp_F-BchgusAcaWjn15SU4gdFk7BGt02b2H8EUqijMBmZu_G6kEmj6m4hkQDBIF2PntDH_aWcxWGEu9bQfZS0S6xwVjpyhuosNFyp9dj2ePPYVlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71031" target="_blank">📅 01:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71030" target="_blank">📅 00:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=bY2cK-XRTilWJ97ozbcvdEbarUZTDmC-qwibKKoCb8ufaDmdCvnLrcW6n9UDDPXTscrMuX5rQLm6eBogiT0euvoyxDUeKo8wk9sdsMplu4H0JqZmOBgvF8LEwx-AMPb-g7eC17kIHhUioNu8LOwycppRdO0BQ39neChGT5t3i-Z51etkC6V43t_8FTlgPP1w1dye7Dw87TRNOaHolxJKw8KMOGGjOE1W3AMocKIPtRbsUYRV4UfUAcTBjUagQ-TIMEFCjS7dLO-bBsiGUHWJBWXHLNDzVpr4NowlhzObUanxMM2WDbJLaD3NdtgSEaoiagYUs7rp7qGWUAW6R3MKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa78544f7d.mp4?token=bY2cK-XRTilWJ97ozbcvdEbarUZTDmC-qwibKKoCb8ufaDmdCvnLrcW6n9UDDPXTscrMuX5rQLm6eBogiT0euvoyxDUeKo8wk9sdsMplu4H0JqZmOBgvF8LEwx-AMPb-g7eC17kIHhUioNu8LOwycppRdO0BQ39neChGT5t3i-Z51etkC6V43t_8FTlgPP1w1dye7Dw87TRNOaHolxJKw8KMOGGjOE1W3AMocKIPtRbsUYRV4UfUAcTBjUagQ-TIMEFCjS7dLO-bBsiGUHWJBWXHLNDzVpr4NowlhzObUanxMM2WDbJLaD3NdtgSEaoiagYUs7rp7qGWUAW6R3MKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇹🇭
ناو آبراهام لینکلن تو پاتایا - تایلند پهلو گرفت و ملوانان و اعضای این ناو برای یه استراحت  کوتاه مدت پیاده شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71029" target="_blank">📅 23:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=gbeZ0Zz6cUIHF95WZ7EJOcL75uPzeISXHGsAYtqUfbJHimkNW4YSugATiKaEfrKKbWJRDV88p1FSxtFnxkagoCxLALW96cGGN7GxKnG_9Ogg9PXUuJsTTnkrVc9ccv1t5s3OVTgz4w2IsSYtBnkfEVyAn6iLT-vs9PgbVO43Kks5AFdwYkZYm6DDuFzMAutNXJ26fb2JGLaik8jQAVm6v_WtHK9taXxbQZtZxLkXAFvX_GSBlaG78RhwvQUFkJfZqo0pwl5VYr49Wk6gQZ1LQNv4iKWa2u5mC01T49zXvlBmubGHYCYCDFCNb1NstZQutit0QGaA8dGTXmNH6CgadA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14a1d4faa9.mp4?token=gbeZ0Zz6cUIHF95WZ7EJOcL75uPzeISXHGsAYtqUfbJHimkNW4YSugATiKaEfrKKbWJRDV88p1FSxtFnxkagoCxLALW96cGGN7GxKnG_9Ogg9PXUuJsTTnkrVc9ccv1t5s3OVTgz4w2IsSYtBnkfEVyAn6iLT-vs9PgbVO43Kks5AFdwYkZYm6DDuFzMAutNXJ26fb2JGLaik8jQAVm6v_WtHK9taXxbQZtZxLkXAFvX_GSBlaG78RhwvQUFkJfZqo0pwl5VYr49Wk6gQZ1LQNv4iKWa2u5mC01T49zXvlBmubGHYCYCDFCNb1NstZQutit0QGaA8dGTXmNH6CgadA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
ملت ما با قدرت جلوشون ایستاد و اگه بخوان این مسیر رو ادامه بدن، بازم با قدرت مقابلشون می‌ایسته.
ما تو اون تفاهم‌نامه چیزی بیشتر از حقوق کشورمون نخواستیم و الان هم فقط دنبال همون حقوق هستیم.
ما همچنان به تفاهم‌نامه‌ای که امضا کردیم پایبندیم. اگه آمریکا هم به همون تفاهم‌نامه برگرده، ما هم طبق همون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71028" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
