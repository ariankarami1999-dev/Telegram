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
<img src="https://cdn4.telesco.pe/file/a2l-I55Ldkag-wHHYKEQHBH0oWbmialpkOhQxDpMyvgobnGOQihjm7ziFRgChQWESm6OCrvljtDrzTgtnWWWsrj4NG54Dz4Jkcc64JIUpAyhuqxo3_Uem_qfgjzlb6_zRHC4L4EqaHq7xLa8lMjBKHA07RtJYYa5hARBpv475b9nNXqF7kJfCUi5-Vcl7HD92saZIAZUtXZ1zhkg-_xShS1UwKarI-iGAjuhOmTAoimML2FAYLaMtbZnMJ1CldfIQsC_8CXypo3PrA8RAFTsaz2_DJEOBX77-xg7Yw1Vr9JUOxsWP7odACHJzRn4yyfDll9nIA_Te85u_bJGNnB3AQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-664545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90205e642.mp4?token=BFoRLmSHTmIdowIMGtzjq6lvUbQorQVEK1p-AyMQaJNbqJw3bSPTZFlaLvA5RGs7Jr9wEjikwPfXTAjwpMbUcL5PjNgmsD4naFJxC_mUHtt0c5n2HoBe83g2tf6RAXdmZ8Ll_xFPHog9EWX3xI8jA0Xnq-6kA_eAEo7S66lKdFt4-q0B6fnRLIwyrPa0zA90CJ94TY8RU5OKFnRgUEhLZcJlh8lcv6ZypCjHIr1A7_hIBCRfAteTtCXswgKru2bm_yoShoQ0HGE5QfJ6AepmwdO-idXh6IW0vnVm5u_b2_2V4mjy7iwG7OGvZL4javy58ACXfG3HrFjeMW2mHqt6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90205e642.mp4?token=BFoRLmSHTmIdowIMGtzjq6lvUbQorQVEK1p-AyMQaJNbqJw3bSPTZFlaLvA5RGs7Jr9wEjikwPfXTAjwpMbUcL5PjNgmsD4naFJxC_mUHtt0c5n2HoBe83g2tf6RAXdmZ8Ll_xFPHog9EWX3xI8jA0Xnq-6kA_eAEo7S66lKdFt4-q0B6fnRLIwyrPa0zA90CJ94TY8RU5OKFnRgUEhLZcJlh8lcv6ZypCjHIr1A7_hIBCRfAteTtCXswgKru2bm_yoShoQ0HGE5QfJ6AepmwdO-idXh6IW0vnVm5u_b2_2V4mjy7iwG7OGvZL4javy58ACXfG3HrFjeMW2mHqt6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۷ سال برای ایران؛ روایتی که باید حتما دید
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/akhbarefori/664545" target="_blank">📅 13:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664543">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
غریب‌آبادی: نشست فنی این هفته برگزار نمی‌شود
معاون حقوقی و بین‌المللی وزارت خارجه:
🔹
نشست‌های فنی کارگروه‌ها این هفته برنامه‌ریزی نشده و خبر برگزاری گفت‌وگوها در دوحه تأیید نمی‌شود؛ رایزنی‌ها از طریق قطر و کشورهای میانجی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/664543" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664542">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4543ba32.mp4?token=ama8Fpn_YUQgTpJzXrIec3y7QZUdxOR3vKPXhyOEbHcxB4u6gCBw3dLiVBZ5dj4EXoCvAdKll5CkSw8krexjJLPz5O57U7I3i0AJawA36nVX-u6CHQ0G0BWBfzH7pHc2vbameQNB7DLlGUIkCpQD9L_iAneWvR_t5T4ULqZXpFtkHNEIcmHl3ej_udxl_rUvzLmO7cWvyaeapYO2AYnVXmv89OInCvgoGc6C7eW9jG5HVPo0PLzA0SBmy7yOhYyF8JGZhLi3KfXFJxpA-ZOxr9p6oZZEpOut6Kk4md_Nd3LLYLQFgevNrBqKRujrosyl6NIRvkAJfz0CDJi17B39wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4543ba32.mp4?token=ama8Fpn_YUQgTpJzXrIec3y7QZUdxOR3vKPXhyOEbHcxB4u6gCBw3dLiVBZ5dj4EXoCvAdKll5CkSw8krexjJLPz5O57U7I3i0AJawA36nVX-u6CHQ0G0BWBfzH7pHc2vbameQNB7DLlGUIkCpQD9L_iAneWvR_t5T4ULqZXpFtkHNEIcmHl3ej_udxl_rUvzLmO7cWvyaeapYO2AYnVXmv89OInCvgoGc6C7eW9jG5HVPo0PLzA0SBmy7yOhYyF8JGZhLi3KfXFJxpA-ZOxr9p6oZZEpOut6Kk4md_Nd3LLYLQFgevNrBqKRujrosyl6NIRvkAJfz0CDJi17B39wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای جالب یک دستگاه سی‌تی‌اسکن بدون پوشش بیرونی و اجزای داخلی آن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/664542" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پیام اژه‌ای به رهبر انقلاب: خود را ملزم به اجرای فرامین واجب‌الاتباع حضرت‌عالی می‌دانیم
رئیس قوه‌قضائيه در پیامی به رهبر انقلاب:
🔹
رئیس قوه قضائیه در پیامی به رهبر انقلاب، بر الزام خود و تمامی اجزای این قوه به اجرای دقیق، سریع و بدون تنازل فرامین ایشان تأکید کرد.
🔹
وی با اشاره به تعیین سقف بالای انتظارات توسط رهبری، بر اجرای برنامه‌های تحول و تعالی قوه قضائیه مبتنی بر سند بازنگری‌شده تأکید نمود.
🔹
همچنین تضمین کرد که هیچ وضعیتی مانع اصلاح ساختار، انتصابات و بهره‌گیری از فناوری‌های نوین برای کاهش پرونده‌ها، سرعت بخشیدن به دادرسی و صدور احکام متقن نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/664541" target="_blank">📅 13:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664538">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0482cfac.mp4?token=cxVxcloSXFpvKB3uvyHJn0DXJZIAKCpZ5omT-zRwwau0kkVLvD_Q5S0Lq-l8LvMq50Bcjla6PCzp5OHJKyMZwkwp6sjSj7yN8OBM2KMBnJ_VlkKM-3pWU2sXxxHuySoJCVa1Zhgn1c46cXZH1msb5URYPQG4zrcwh0GwoyuCSdcBkmG8GQ2hICY-YC3OH_DK-DgJSSNaieXuAI00adV4NKLeYZdaJknYddurYQCWuRpk1_a5dsPuoI1iDJPR-Tx7ILtd2Ux3cqlghB8Gjv9EAameP1c2z09ZIdNr-0tDaLdwj9shMKt3Kr0WC029uKJyguQZlWtNSf7guL9dQPezPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0482cfac.mp4?token=cxVxcloSXFpvKB3uvyHJn0DXJZIAKCpZ5omT-zRwwau0kkVLvD_Q5S0Lq-l8LvMq50Bcjla6PCzp5OHJKyMZwkwp6sjSj7yN8OBM2KMBnJ_VlkKM-3pWU2sXxxHuySoJCVa1Zhgn1c46cXZH1msb5URYPQG4zrcwh0GwoyuCSdcBkmG8GQ2hICY-YC3OH_DK-DgJSSNaieXuAI00adV4NKLeYZdaJknYddurYQCWuRpk1_a5dsPuoI1iDJPR-Tx7ILtd2Ux3cqlghB8Gjv9EAameP1c2z09ZIdNr-0tDaLdwj9shMKt3Kr0WC029uKJyguQZlWtNSf7guL9dQPezPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی پاکستان به سه نقطه در خاک افغانستان  ادعای مقام‌های پاکستانی:
🔹
این کشور بار دیگر مناطقی در داخل خاک افغانستان را هدف حملات هوایی قرار داده است. در پی این حملات هوایی ۳۰ نفر جان خود را از دست داده و بیش از ۱۰۰ نفر دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/664538" target="_blank">📅 13:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664537">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL_K_9giA6TZ14GGMkuhWVNB7CYK6GFZ9WnlfkxuCLGOyc19OUZfB2BECN-a7JAbgb6tzYzwcbdTqngzgiEM3Igs5FULkYZQ6xaeusoUGm8tnpYzQZ6C_c3x30loyLA-jZQB84kYDCte__5FmKER1jLoNKhxjlAoudb_iNqi4D1TOcB2iVoytlOhQKmx6cmU4Ds7_w-5-k4eojbq0YJPkLWPlUtSLJDWaU8mhbtv-yS8ftDhkGJZ0I-y_oI1qz6_BuZUiVePTFiddL-bHJb_5nKEzNP0UMV4MemcxEpJTE_-6_VUV8aVLn2_i0DsINj4mP-AOa9JLOSGPvJpLw-_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مهدی قایدی بعد از حذف ایران از جام جهانی
🔹
عشق به این پیراهن، با یک شکست یا یک حذف از بین نمی‌رود. ما کنار هم ماندیم، چون دوست داشتن فقط برای روزهای برد نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/664537" target="_blank">📅 13:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664536">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره محیط‌زیستی اتاق تهران؛
خدمتی برای افزایش تاب‌آوری کسب‌وکارها
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی و رایگان در حوزه محیط‌زیست، به بنگاه‌های اقتصادی کمک می‌کند با مدیریت بهینه منابع، هزینه‌ها را کاهش داده و تاب‌آوری خود را در شرایط بحران و پسابحران افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲ (۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/664536" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664535">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiO4h3KgBaAm9Mzc0Y_1gYiVe6cUd_yHbqPrhTNOj62798i4DO2fqtHTE1RgqnuKvyb6hiSrqe2ySRwXvu44pv9bIaoqORBG6gHbI330_DeQCwLX1ZzMvBifnZuEPX5I7q4ntADZPr6tLFYB7MfR17WxLkNW0Kjz9vL1RU6x1okxPngCLeyD8rbWN2y4WB4CSiTizAxzTNGEp7s40je5ti-FwXzSZi--xWIwioS5jb31k95K6yXnoIPHZHH1iWfkqLa-xinyVPUzLqgBSsjk18NrHrwIqlJ9tu6uUlYDJvOp9CLry5w1d09l5g-7yvHtMBgoscQaGEkxVtB43tezlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با حضور سعید عزت‌اللهی از تیم ملی ایران
🔹
رتبه‌بندی فیفا از ۱۰ بازیکن برتر در بخش دفاعی پس از پایان دور گروهی رقابت‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/664535" target="_blank">📅 12:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664534">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1e624ef0.mp4?token=d4OR1T6O-FV_rrGD0v5k9wrdb-jI0GzJkQRVgAXa0rSDARUb8Z11EaZ3TqZTeltcec6N2b06kBU-W3uKncifWTdA1naEIidCLAEDPE6LPhdjxnq5qAlaqqyTfL-YMuxGWnTzQop8W4QjqSSU4ooXZnFjVHQklS8wvvcp8kjI6faWyOveVd5iy3tqKFXs59NHzTIc5HvoeAHEa4c1f5nTyuBBjXl9zGwuSG66SgYqOV7gw9S_UsmtejRwbAdkGReNTg9Zw7HlitMkd68zEEXLZ16Q_MpME6nnWnh_43AY0KUITGK2d7804e2liHLb96i4BWPgnEWbtLg49kln6nvOKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1e624ef0.mp4?token=d4OR1T6O-FV_rrGD0v5k9wrdb-jI0GzJkQRVgAXa0rSDARUb8Z11EaZ3TqZTeltcec6N2b06kBU-W3uKncifWTdA1naEIidCLAEDPE6LPhdjxnq5qAlaqqyTfL-YMuxGWnTzQop8W4QjqSSU4ooXZnFjVHQklS8wvvcp8kjI6faWyOveVd5iy3tqKFXs59NHzTIc5HvoeAHEa4c1f5nTyuBBjXl9zGwuSG66SgYqOV7gw9S_UsmtejRwbAdkGReNTg9Zw7HlitMkd68zEEXLZ16Q_MpME6nnWnh_43AY0KUITGK2d7804e2liHLb96i4BWPgnEWbtLg49kln6nvOKDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور ترکیه، اردوغان: آنچه در غزه رخ داده یک نسل‌کشی است و اسرائیل قطعاً بابت کشتار کودکان و غیرنظامیان پاسخگو خواهد شد؛ ما نمی‌توانیم در برابر این جنایت سکوت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/664534" target="_blank">📅 12:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664533">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتانیاهو: درخواست‌های اردوغان برای نابودی اسرائیل را جدی می‌گیریم.
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۱۶ هزار واحدی به ۵ میلیون و ۵۹ هزار واحد رسید.
🔹
آزمون وکالت ۱۴۰۵ در نیمه دوم پاییز برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/664533" target="_blank">📅 12:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664532">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00387c6b1.mp4?token=TUJ3BuhWmeemTYIdiiZQJePV_fH-vuCdfaYY4gXhM5wphrwLddXbefz_6T_DgfnrYDNO4UwW-K8AhdEikMqbNb7OnB-B60kpICe0AiYzBoBYUIrXvjaU1omPTiL90KKeCYNSxKTYyfmB9GMNXMFlnv-Jb2eI6EpizCq2udckWSL5AAGCLHh7T4-YlN6VjgpSPupA_H5xhBxQW0ODVTEMBriE9Aja1HHNAXuQNPPJScVLPuzmWlV_Lw2PEijybOVYjpCEls9YdVlk8pkNK7Uhd6mxD3o5ob_AbB1tf6YDPJ2XQMiUUdywdVSgdpgsEQDfFDXVzWnfBwOOvuFlh0mLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00387c6b1.mp4?token=TUJ3BuhWmeemTYIdiiZQJePV_fH-vuCdfaYY4gXhM5wphrwLddXbefz_6T_DgfnrYDNO4UwW-K8AhdEikMqbNb7OnB-B60kpICe0AiYzBoBYUIrXvjaU1omPTiL90KKeCYNSxKTYyfmB9GMNXMFlnv-Jb2eI6EpizCq2udckWSL5AAGCLHh7T4-YlN6VjgpSPupA_H5xhBxQW0ODVTEMBriE9Aja1HHNAXuQNPPJScVLPuzmWlV_Lw2PEijybOVYjpCEls9YdVlk8pkNK7Uhd6mxD3o5ob_AbB1tf6YDPJ2XQMiUUdywdVSgdpgsEQDfFDXVzWnfBwOOvuFlh0mLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بنزین هم در روسیه سهمیه‌بندی شد!
🔹
پس از حملات اوکراین؛ روسیه در برخی مناطق بنزین را سهمیه‌ای و سوخت‌گیری را به ۳۰ لیتر محدود کرده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/664532" target="_blank">📅 12:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGue9mktf_kTLURL1NLnacIPDxgbCvRaQ7M_HyKkYQCVLmqrycqz16wFcJkfksO-faVCplKuPDbH8YakMMm8VK-bwOBJX6MZr4OTyquhmKvHwVWT-sLAhhyEeQb7Lj6tE6u4XR08oZ1EKwDhGLKqpjEy_m5-Wn3v4SWSSKLHCwh5Fr_yX0jv8nGmL8VD3RGEWCr1onH-66rvHvzMyBg1qU7urFuzvQS-vngJm0kFyCWtoKdBnJ34tNhZ8BWdlsx3Hte0ram2KsTQI1EgBzNSI3hQZh2e5S_SnUBbZjUn635WB0zW-kwfD7zSQI0cN0SDcJiEHYcZ7X0DLMoDQ_ViPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBFF1k0OZMDT3NeLDSeP6cum4Ywf9N9ZzXwzRATcO8vK_eWV43kjmZAecRxauMVq8NUs97UT3PKWqcXhD1fILbNwJc9GLmZgOH1ZRKpoTAPSqI4Xo7ZsgGABzzqkGzteQQHMLIzjcTLOoTGq1_dJq8fEWBZPDxlfMKDwsPYEwAZ41p2FaTEzoE94689wUe33SbxktsDVq0-kdonJXv26Cxd-_3fYnjZ8vpCZGhksoFmIn39rK6oQSblbmGCGy4cWP-prgrpc6aXXhUpifzpo-GEEqwL50nfazDZaJQlOtbI5D5FKZQR8-I2Jr-ngSqxnngeudOs9vQK_u5s9xyokOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCt6oZXoNMRzgPl6Z--zHqf2l8bw5vydAxCv7Dg9iDCJcmJGE0UF9bJBcRpGvXe7rzD5Zbvq4UVMdu3qreGrLNAe9w6RlB6k60EM3YRyMV1-KKT2uOCCS6bLJJjwKbXsV3bOrwzPGaBayKisn5wZkGJIbwKYzk-Db2lFaAa-IXRsQcVwLY4LZrCbbqxEPk7D-AwBpgLDLuamk2dd4dAujynCRDYX5LVMvvTH37FQQtxG9-w2UWT71TlktS6r6q5Uggz3tWcY96eS-Z0nfl9T_vG5ctU0rifpr9dzZeKS2G8wIJMCJbCEjzf45Cw8mP8sWpSfp4uPyZ8ZV7AUf7t_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL8jMJAOSoXp_EnARC6C4JEjospsx9vMmIOqIq1VSSSQ-asQuNysLOvS5IipXclmMel_gVw3NcVVtu6iNgyEvWltExbqV03v46Avq66OUNDWHyPgSFAbEPm-TrOkQfkLHWbLZRg1Hbpizgf7BnqTInpfWqDqXf_nLOhhCcmnOPmQ1FtWzLjoaHCuO7pzgdMNBamuYvp1eppoIIBbX2XmqibHNkXeAgdHypL50riU06R7wXBiLgj3S9C5aknifCD-Zeuo83eGd_u04pMk1UB-CUS8yEpI8DLIXFV4sCjuL5p9zv8IjLA5UibB4JCi558eJ_bVGVpMMDbdr-iEp-4ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiOSRsJhcsirItK_Ejd6Z6cubRl0PNBCpBoQbHK1bWUpRi2To3aUt6XOZGrxTNeYyoSZunUgd-wPTFg869TWj1raYYXJR69nX1rM3wq0oUHR8KA3y7-tyC2OPdWuk6OZLKmROI5VhFcoLmjpBic1-7xBGDdx9-7zd2mMpZs-n0mKzz_mowvpyME50wdyObwF4lti1YoG9iW-6splF_pTOuMGRI13JXdMeMSdHvwfKWQ6j2JyPs-q4EveD1rdanYcd91j_9liFXpZf-zPr0ediYQhhSp7LjZ9MH_d9RGXWMF59sOF-msonUnJyjOpZkfgTJVY7J0w8ARYk-VPYw_Nbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKlamH1Brhw7fM4b3QFZaKH1uALb6aczPPbl0ALDBJ9QjznMvoXtuFCB6uWK3bp55HG6J04P2eIiBCJcgu84cSRjlbTwYcF7GLyEcJH0P-4X4DHAFlfdLxdt4HcqieYTBHI9fQSHnDqg6OJ_Y980_vgydh4lnKq2C-wCw1XUacZa3ysp7gsr20ndZiCdaZH5GivPFOStmWg6WFffd2EFhX304mIhEmZo2mmX0wWEipvp6F10EOGUbMeHiq0zDi9qylV0I1RjWEoc0THeqS3Bwj0se5SO8eHDWpNiALf7eetB2Id1Nh1D47NWtixvslu7rx95zYxKL62Dhd1Khh2MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbzh2SBwJfmKmpCaqZPLHx0lav5zJY-aCvdlajDYDoNJvBqaZSN37OP9aqJD7tpWU5p8LMCN_pykxxrT5u7kckAZtyA1e3PpmqxYzKVPg8DR_Kuyh8zSMHY8VO8-LWSXiX1u9thjtyAGrmZf-uwnLrjlESuSygOCjlrfa4BDj_SvmilqXR6RCreeNW8jg0_i17afxA8r-zSYs729uBEQC9JYjGCjl98V6P8nKb2hx8fwD_JfStKdGm6WBLXJahUmDy_lfk1wbJZioD0UC3V8iJZv2cImFlxqte9F6576CtcL3F3xOWOetfRC6JGBcxE1daj5xPHgxsslFOcyxlpQfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
قاب‌هایی از شهر شما؛ خانه‌ها و کوچه‌هایی که با پرچم‌های عزای امام حسین (ع) رنگ و بوی محرم گرفته و جلوه‌ای از ارادت حسینی را به نمایش گذاشته‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/664525" target="_blank">📅 12:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae801529a.mp4?token=hYj1YrMl6hm5bcxcm32X7j8mhQ1S8keyN9IKmaMtzeYo9O-XYodr3c8YOEd8x_XvBUbJpPiQrQA2wv1-A35UEo2ZiQCBmZES_VzG90Q8Y9YNOYF1o_Q0shO9ItNd_hIc5o5j0mzQL7OegnUEO0EJibLn6ZF-LI_BrxQRlKN82VhN-UWQha07tNXJlT2cSpGaDeKzsxrAiGgOEgcqH60iqbxXCS_i55DvNLrpxM84Lo3vJPJhxu489NX69vLOQiBYA-MBMnZLKeg8DcsU_fEfoX3tfdXw7iC53iMzg3itDstuFsicdsSCqKZFk52qv6as6Nzlx1RSBuX8-n5OmcqnNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae801529a.mp4?token=hYj1YrMl6hm5bcxcm32X7j8mhQ1S8keyN9IKmaMtzeYo9O-XYodr3c8YOEd8x_XvBUbJpPiQrQA2wv1-A35UEo2ZiQCBmZES_VzG90Q8Y9YNOYF1o_Q0shO9ItNd_hIc5o5j0mzQL7OegnUEO0EJibLn6ZF-LI_BrxQRlKN82VhN-UWQha07tNXJlT2cSpGaDeKzsxrAiGgOEgcqH60iqbxXCS_i55DvNLrpxM84Lo3vJPJhxu489NX69vLOQiBYA-MBMnZLKeg8DcsU_fEfoX3tfdXw7iC53iMzg3itDstuFsicdsSCqKZFk52qv6as6Nzlx1RSBuX8-n5OmcqnNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از پیامدهای غذا دادن به حیات‌وحش و رهاسازی پسماندهای غذایی در طبیعت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664524" target="_blank">📅 12:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آغاز پیش‌فروش بلیت اتوبوس مراسم تشییع از امروز
مدیرعامل اتحادیه تعاونی‌های مسافربری کشور:
🔹
پیش‌فروش بلیت اتوبوس برای مراسم تشییع رهبر شهید به مقصد شهرهای تهران، قم و مشهد آغاز شد؛ هیچ‌گونه افزایش قیمتی اعمال نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/664523" target="_blank">📅 12:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mteA5hPbaMgAmdkuWgXokHjiQQ44I_Ix-519p5kodZgVm6LnrsKVcsqXyoL-K4CmsACZLWnzhyyWnjUdDVtswwuLj2Ld2H3Z8M984z06MmNc6U-OLPf-URwaZF4vaWwMRD5VgV3bBhaKmU3nA9KReHOGwpRfTDkGm1RXxfvTmFSQfiEhwnrn0FCYSlRHMwlm33JnKeF9382biaaRA_BzcjjhDLzNn3ws3vBOMeuMBcKZbPgbqgblxqvI_6Gp_vhpkX3_jS5-B9QrbCClrkcUeGdDI9VweIba6ZA4KN5ZPjphDPPk_LiavYD6MI6uidJHvWcw8aFGbE6DgEnkRQc_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای رابطه جنسی آقای مدیر و منشی‌اش/ دوربین مداربسته همه چیز را لو داد + عکس
🔹
رابطه جنسی یک مدیر با منشی اش سبب یک رسوایی بزرگ در عراق شد.
اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3226323</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664522" target="_blank">📅 12:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdeLzSIGZ6hj67PHIMDoIjbIqtSuLdM_SyxNKJO7jjmzcMpYmpLZUQ2hv_RkF7bQfSIyaR2GiIHgRr2ApALm0xxpvt0Z0tYSlsIvZjPzGKeZ_AOQGdbHLXxD5Wba11B552xBOWXBR-vHJvzsykawD2Oil1ZmyT2t05ry1Wl_kFCkZ_9grZ-bFtTQoYSnU6tM6VWKnwmRz6nYi0i-wCRJF74UPaYOAF-CRrak55IFoKZJeUH219uCMGIyvZeYJDTXv765A6NrvR129f69kcK1WWiW_f5nd5KJ1tiDjXrj99LoB2NmJBTP157YotsMNcNnDb0R7ngagjWQUEWlZTOM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از یک پست تا یک پرونده؛ ردپای دیجیتال چگونه زندگی ما را تحت تأثیر قرار می‌دهد؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/664520" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664519">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رویترز به نقل از یک منبع آگاه: گفت‌وگوهای فنی ایران و آمریکا به‌زودی در دوحه برگزار می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/664519" target="_blank">📅 12:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvCD8zKsrQKFIfzBCm6ci2atBSifF6D9zwfO1xnYxbCoS62T0KFe-tqeUEwVSLKij7x_5K01MewalReocNexOoN1A3s0tixaMfbjdVErMXOUUA_J5M_TfQkiO0OHeWD98pWBBl748hz3TVX6Y3OXnfUdORfW-pKj_vJqWk2_pYZVGkI0hFePHdCSEnHUmbymcTWAUorvR9FRG-Ky2OHkW3wp_b_T3aDBCxehrI18SjC066ErRqZoiXu56zm4IPmPT5rTHhkBrrCorYOtF21Bagh2RcO44AEcZG_RZMXlRsTjajUPTJz_SVkBGlTAuPBFSKwR6wMqWyZA21Ll3JSRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انواع آنتی بیوتیک‌های پرکاربرد و موارد مصرف رایج آنها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664518" target="_blank">📅 12:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238aa4c3f2.mp4?token=g7PwQu4HQlPZGO9WpDPBySsVdJJzggqzlOLK_OQiF6hlbbp4mTodQYabH4xni_kefNfR05Duy_mu2X0V7rblLv8IqG0P342CNE6aM17ehhBPMmsqqfHYTrPiZlzuMHJvMs7E_MkFg1pH_IyDpo-EB5Eq76HEjv9LH1ize8_qj2SC3d5z5TN7yhkqHak-73OhacQmbP8ivKo3v-XWt5Hn2iyDAKD_5ExPbYACuM40r4gFWkHlAo74vTUFNFc8aN6KJ2xFAwyo06F2-sWFR4WIqKck0D288KG3g1buETX1FprIhyxJYzfpOc9vya7AvLiKuXK3Izd5Lj2hnphQDn1yRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238aa4c3f2.mp4?token=g7PwQu4HQlPZGO9WpDPBySsVdJJzggqzlOLK_OQiF6hlbbp4mTodQYabH4xni_kefNfR05Duy_mu2X0V7rblLv8IqG0P342CNE6aM17ehhBPMmsqqfHYTrPiZlzuMHJvMs7E_MkFg1pH_IyDpo-EB5Eq76HEjv9LH1ize8_qj2SC3d5z5TN7yhkqHak-73OhacQmbP8ivKo3v-XWt5Hn2iyDAKD_5ExPbYACuM40r4gFWkHlAo74vTUFNFc8aN6KJ2xFAwyo06F2-sWFR4WIqKck0D288KG3g1buETX1FprIhyxJYzfpOc9vya7AvLiKuXK3Izd5Lj2hnphQDn1yRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: حملات اوکراین به زیرساخت‌های روسیه، هیچ تأثیری بر جبهه نبرد ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664517" target="_blank">📅 12:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رئیس مرکز ملی اقلیم و مدیریت بحران خشکسالی سازمان هواشناسی: تابستان امسال در بیشتر مناطق کشور گرم‌تر از حد نرمال خواهد بود و احتمال شکسته شدن رکوردهای دمایی نیز دور از انتظار نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664516" target="_blank">📅 12:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9521654c.mp4?token=VPFsxAfoI0DOOeLDZIrBnvOv-pqWkd_lfEZWyOquAfDC9DkxJ5JOQKvUUE41rZ5Gp9y_wc8hkQuHoM3Xj3qwZVqruSJXNVkBHWtiuvVQEaxYI8qiVX0XFbD0X9nJuuV52Psd8Cyr-7SxNUdvmafvIDd_I-pTYUku2vHCPco2XlGbgGqvK3adlNhdiiQl7QxOuxTzf7Sy3mVG4YKnVk3AX7i6jmhersidaK7ef20Q_u4xoQx49io_N_sACW3_pNdHXMWcyuv7H5DQogneCZRZPerGdRPO4x27ZRFBhTUmAq6dR1ReWeUE0xfzHFgUkpi8oijBPp4zRYbuB5w-_sAPoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9521654c.mp4?token=VPFsxAfoI0DOOeLDZIrBnvOv-pqWkd_lfEZWyOquAfDC9DkxJ5JOQKvUUE41rZ5Gp9y_wc8hkQuHoM3Xj3qwZVqruSJXNVkBHWtiuvVQEaxYI8qiVX0XFbD0X9nJuuV52Psd8Cyr-7SxNUdvmafvIDd_I-pTYUku2vHCPco2XlGbgGqvK3adlNhdiiQl7QxOuxTzf7Sy3mVG4YKnVk3AX7i6jmhersidaK7ef20Q_u4xoQx49io_N_sACW3_pNdHXMWcyuv7H5DQogneCZRZPerGdRPO4x27ZRFBhTUmAq6dR1ReWeUE0xfzHFgUkpi8oijBPp4zRYbuB5w-_sAPoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرمربی کره جنوبی، به این شکل بدلیل حذف زود هنگام از جام‌جهانی، رو به مردم خم شد و استعفا داد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/664515" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_fIF6tOXK-LIQa86zj571T1tme6qrLt76Q0QoCvcYQSa6OUmSQafwjJAbrEuIiqCVvXm1wFzGJYePpX3FZ2HoSahEZ01z6VIZCFlvQmvz5tlUAbVI9z9892LJHoR6bzmHeXVcZsp6dAm49QJNUGjiMeAczomK9ESn3DecbQnYZ1GwEPKEvJ3riL-qSkgERF-lKWdXhKeCDO2APfbVH506CM8d_u43zbDy_HEl7wU-a0TyH5nzQI1FYIJOxikGqz0RTmJLAQXdx3ap96rg6Q8nQreDaYm-tfIaLmqENMCeXreMXRLCrqdaFK6uKVLUOmv16sDx43WCaP9fkD_77G0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcC6AMy6J-a0EUDTazBdTQ32OAGw_V7B625E66f_isMxOodSjeGdtzTNMm8MnaJnJPs77Pe1QyktlBpXJid_o0sHtpjjMPP4zV_KbbD7A1zp4NwlxNptjJmy_bUkQ3tIbOmFepVwUlv6YexifunK892-enZTKyCmoK9xA_PUU4UDSbR1U7K2xaNwkhdH30OvQKWBFYQtmR3A9lmmG38zU6CSkJV9EueaHcnQRxbAFpZzgmTHyCmCafvJ6_bB8wTAkgX-1mmo8RDY7-gv278qUqJgt71J81PkKVSl5ROtJY9WRLgA4Ge0UMlF8Y4oTiI6-dn7mgRk5prpoI8M2oGicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvJ9qfqnxL_doLkbFcGngtJAWbBVOT39shhwYZUytea4-dotwe5DyaoDRHXFkvcrVbbGDx7wsY4zxqponTB-C9NC86GWbU1xeAdUxjXp9hsu7Pq3nJ-GeDNXzHgK8flERDpAD5P2n7nFBwzcAoYN5DsG4R1nxjp_dmHuujHcjO8jj4vfnc6-9WotquiuCIUjkdxAxeabQ6oK9noHQW9rOcTrWQQQwiYJnB8Cj5PMj-cB07g1xS_hvehzJtIIChScChfmzopalC1UWw3jUqowMk7PXYN8Feag81zGINlYTx0asenCJZtJme_CFJ1mwYnO2mbHUVfNXy1sY4-NyPX4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diS54rSJanZxZFfmyAewuUXMVCNr7VNQmIXGySur8hsAfraCv6MIMTOT1k9FBTYu491dp3GmBqDHuQG3EKD6AQ1rP8G9OasVHOzxMKDQI49pqDfR0sMzo-vQHoiHWsKit3gjg-M-5j_v-mYZIhoSUsV9bWn8xN6AEVXwmg7ZcbvgsNk1VIC_4IrHeljGHEKRmROr7JpiY7APONo_fzUDpgo1bcrQzH8NZ3COPdiOOzEDBUBytWepY9-ksBLyHduRNctuA-CTe3nbYTXEdPWwQer_GE93WhuoISLeiAp24Jw9TPNAKsfm0abbLGwSHf2DhwT5gbfg_8-NRzikNhyU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJ_4zCxvBadJqKU0nqxzcahqrcwWgURL1wW-iL5uzQjiOtgEer66br3rZFBv2Hlq3rXwzokUI23OKJXndBhjk-t2GECZYT8aCfb4deGsEbra_q_T-R1oN2_zv1cUaq5I4qBqwQZS4e5P2Qi_qVnuGTMRBRlG0WKisCDBDsrBwREKtKymgR2kQqYuTxrGNIAtjqpb7rTHz_wBFEJ1wNHjg351x3ps-Vb6IBYX28T7-DYdiHBGZ3SBOu3uR2XDFBAnZVBXhi7g_WrznwzTPbQhpCOcQhJUXFPbfhzKcOgsRAXfsu2q4jcen6I8NZp7WNFGUjodwfPjuJPzRm5FWfxA9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hp1AEJncLG1Cfi85_-GDV0dpdLq6DpVBJVrAysPTAVZ2QKl4DqW-Nv-CYzmvX8FyIEUAjBnImrZdk5nygqdA-ihNVB17LGRynGaJct9dsVBTAgDj_5CDWsHPtYm0XHYvDvas_TlcfG6G7N8zbanOABOYK1JVFoxWLVJSMZUU_bOMwvGGX0pQ1FhOz_qZkqu8x4JDc3goaTspBOp-dj92jp8TyamvI1LWJSCaWB-_aLFLwwO_eBmDsbVYIfbXxKbzXCZCcB_ZMETRXQCV5OZBuLMUzyT681cT_cONXfR-hzvAOVMD0mO7VzgVOegaPU5sjf9IC0w5QXrxdUNgHv1DAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خاموشی‌های بی‌اطلاع، موبایل را هم خاموش کرد!
🔹
همزمان با آغاز خاموشی‌های بی‌اطلاع تابستان، گزارش‌های گسترده از نقاط مختلف کشور حاکی است که تنها چند دقیقه پس از قطع برق، آنتن تلفن همراه و اینترنت نیز از دسترس خارج می‌شود.
🔹
موج خاموشی، نخستین خدمتی که از دسترس…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/664509" target="_blank">📅 11:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d185513f48.mp4?token=WPpwhEvGFtBwXF5PZ_rQd71Mr8MH-TNubezs7vDtDgNkqkD-gl_u7ddj2AVrA5Ya4Z6bJMdk5PSSIWojtnI7ooycfc9xiRs5T_2vLKtK8e-6-Nu2lq50gJ4yZaJHYYsUT3GPcHHtnvnPAST3cFLt2vpYaP559yBcptHWY6CRLXUQTWgvW9YSKDVELQRplSpTJdkIxDRGJPlzRrlLfqrWOBYlplj2jfOgrRkYs-K4xQzrb9Es6VDaMImp-57R2kfcIozMeicpUcXhY0QlYwDKjXuDB3EBnX6iknK6DCptRNFZjwebADnqSQQZ0DAEpDkevX2b6IadjM5zNJLKgxrLaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d185513f48.mp4?token=WPpwhEvGFtBwXF5PZ_rQd71Mr8MH-TNubezs7vDtDgNkqkD-gl_u7ddj2AVrA5Ya4Z6bJMdk5PSSIWojtnI7ooycfc9xiRs5T_2vLKtK8e-6-Nu2lq50gJ4yZaJHYYsUT3GPcHHtnvnPAST3cFLt2vpYaP559yBcptHWY6CRLXUQTWgvW9YSKDVELQRplSpTJdkIxDRGJPlzRrlLfqrWOBYlplj2jfOgrRkYs-K4xQzrb9Es6VDaMImp-57R2kfcIozMeicpUcXhY0QlYwDKjXuDB3EBnX6iknK6DCptRNFZjwebADnqSQQZ0DAEpDkevX2b6IadjM5zNJLKgxrLaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش سوزی مهیب در مرکز بغداد
🔹
منابع محلی از وقوع آتش سوزی گسترده و بسیار شدید در منطقه معارض النهضه در مرکز بغداد پایتخت عراق، خبر دادند.
اخبار عربی را از کانال زیر دنبال کنید
👇
@AkhbareFori_AR</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/664507" target="_blank">📅 11:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57faef6195.mp4?token=lYiv8lUamvLFX6yZxwxClxLsxIoZW51FIko41F6b64n-m5kdSXZowbPeBc8AZdZ84AzI1pWMeimV-ykQz9rqcHvmRU5IlHCmh8aZ2uOEVxRbOFPLdk32MoouZrM-roxktSyzGht7_PkNLSXzAz9zv3JDfR6u5KuT9Harv1kyLSomNqFg-T8KRDz-s8Ki39EvXVPAI7J3Vkc8_k_z4rp-LWaLE_qJVP5tCsnQvf8YVaM2QH0d9S23K6ORfDjFg3hKkNJZWdvCRooGW8lcOod0OuXIK95RtHx2qLtmLW_LmS2iyh2fawOHtxLGYQKsHOYf96bhyqbccMoNhCWqn9IgKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57faef6195.mp4?token=lYiv8lUamvLFX6yZxwxClxLsxIoZW51FIko41F6b64n-m5kdSXZowbPeBc8AZdZ84AzI1pWMeimV-ykQz9rqcHvmRU5IlHCmh8aZ2uOEVxRbOFPLdk32MoouZrM-roxktSyzGht7_PkNLSXzAz9zv3JDfR6u5KuT9Harv1kyLSomNqFg-T8KRDz-s8Ki39EvXVPAI7J3Vkc8_k_z4rp-LWaLE_qJVP5tCsnQvf8YVaM2QH0d9S23K6ORfDjFg3hKkNJZWdvCRooGW8lcOod0OuXIK95RtHx2qLtmLW_LmS2iyh2fawOHtxLGYQKsHOYf96bhyqbccMoNhCWqn9IgKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس؛ تخریب کامل یک روستا در جنوب لبنان توسط ارتش رژیم صهیونیستی!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664506" target="_blank">📅 11:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ab6f123b.mp4?token=YA9Gp00w1cEw2XipYZeggKU9iU8flcj6QU_r9RL8KtMHKCy9BS0RivmDMXSYYQatNPrA2UyJftiNwpHLr7UPuT614MHekvmy8PPB2nqdCfYqNcnZvJOCfjeRsY6zA4tcn4uoQxiG4gNb8g790DCSnijKiw5Y-gZqf2Vzd8ijfNWxcJrzbmPeqI4iEn0pdc82Egfeyh4pM0ZlF0RKw-51MvwD9y6zijTSs25Zsup0-zAtkVQS_kk3pfP6MwzvOVYgLCmWS2ZsJvUxH-6KDj7t8EUFDTwxRMEZDBC9iECGlkUPhUY3nT_tuJG_hRMT_VQx5Wgc5RsfugCLhX40TEGwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ab6f123b.mp4?token=YA9Gp00w1cEw2XipYZeggKU9iU8flcj6QU_r9RL8KtMHKCy9BS0RivmDMXSYYQatNPrA2UyJftiNwpHLr7UPuT614MHekvmy8PPB2nqdCfYqNcnZvJOCfjeRsY6zA4tcn4uoQxiG4gNb8g790DCSnijKiw5Y-gZqf2Vzd8ijfNWxcJrzbmPeqI4iEn0pdc82Egfeyh4pM0ZlF0RKw-51MvwD9y6zijTSs25Zsup0-zAtkVQS_kk3pfP6MwzvOVYgLCmWS2ZsJvUxH-6KDj7t8EUFDTwxRMEZDBC9iECGlkUPhUY3nT_tuJG_hRMT_VQx5Wgc5RsfugCLhX40TEGwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری مردم محلی سوریه با نظامیان صهیونیست؛ اهالی درعا با سنگ به استقبال نیروهای اشغالگر رفتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/664505" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm_0o9cOaoARXFJfYBNqreYeuE7TwipBbZPj3vNO41BzZVZnoQiBuzorf75YpaIYCw9SC-RwoKM8oNGjbaqbSY1-DJNY8Dzt_kUwTD-9dq421bzGRi4Oib9EQMQqNCtHD18hqVCuv1WliMJwtoPwIIXk5TMZq8eaJAV62uWl-xWC6NAYOk3L4F_sRHVwT-RCVadB3Pds2VB5Fw5Jsngv1aijbF2Q4qLPdZ2eKrpG9w94XZo88CN5eklaw62nwAd3SxfTwdfICAovWl07G462IE7UCggOYJ5QgKnEGiSY-z2LIVQdi0V19gmDck0G_DMf4Ny37LBtYY9upEVsCzLpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با چراغ روشن بنزین، چند کیلومتر می‌توان رانندگی کرد
؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/664504" target="_blank">📅 11:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نشست آمریکا و ایران در دوحه    باراک راوید، خبرنگار اکسیوس:
🔹
مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کرده‌اند که حملات را متوقف کرده و این هفته ملاقات کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/664503" target="_blank">📅 11:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxiLhxc9NgQFhlAB6UMwLOfJ0fh1R96aJwfI-PIF4AGOEDgF4CZhEz-nfJxZvkKQI_-hztIjszMOxdh7i6iF-DTCdg9ea3xITNXBgnW4dXh2WMndLVO-xlXGOwqX4Nydiu7ejg3VZFa2q27-U-tBRLzO2o7V8gVFtAjSZBX5fcy7l3CvSUAItjVTGkltC_2_dkm7_-Ye6Ky3jpm-JTZwxU8jqLNQS9jv-G2VeZaN457CrRYgjnuVghaHqi6lyydDurkN30Po6aA_Z9gAbpVanCho_GELejxYh3Jqp_2HGl2mOvWXmWUHE3eSJVoSv4fXw7RWtK9L7pliG0qvqgrrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌ای که محقق شد؛ عدالت ایستاده است
🔹
گفته بودیم که هزینه خواهید داد و حالا این هزینه، تمامِ دنیایی است که برای خود ساخته بودید
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/664502" target="_blank">📅 11:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niZdAqCvMHq8NHGWHyitQoXcWQQ5Wmxf85-UyKBbL_KZrfYSnSIM9uean6ScnHPZgVSrmKLxg-UlDzoQqi61IVbDqHs4HVIdkHuRsUqFfD5WxnmTenT2zrUpcAhT9OTGviNPDADYMlRSm4jS92hQvx4HowqH_ftfPP6UBNuDET7tqNK5E1pIzYF1VFOXO8V-JoVOjC5nJ7O8mQ5l5BNrI2SVGrE7b__ea_ZbidPKLosuXKeKEaXFDUcH976kYriqjwTWjTbGpVdUr7JSpN_RRcaIv35wP4NCPv4FC6iIpXPiO3ucdS-AKyGhRNN_cDC3CWGNlgJadWdm9TsR7mcOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gub3oLkzGUK7KGcmkKO8bGS4-TEPNAaFb8iZR1176EdCGUtd2OHEQlFhTyeaZ9de0GgIqeHgFacVQ_7MDINVRQVspO4smppbysQcAR8UVX2UaiQtaucRU36ymSEQ3r8mLenr7qEhkvQyUIC7iGLAsAIQctO9o8mMpfQZFkrdVEc3BSWp7Jw0InStw4xtCGFoYRDq5pxfkESPCV7FUQ4p0us9IKf8k1thnkBUwXEa_qvo-ZBwZgaz1UkFSbhaohgl-2aVWfCirmLb6RtN_iwKwUcafwpp5yX6_-PNcMUvxxmNBgkRPGbctFEFQqG3mtzFZt1iz0PG4UT4OO6SGv6VWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnCp10Hl8t4pC6E-5Qgp7_W9_OZOOISKVfMtAn9gyElKpvA8gJUxUtHSwezkZ2q0GF-VhyrfrKGe7NQgoGu2yd0-664v3zht7uHlXm7E3FVWm6U1DT8eVL70QZXZNXZ5ph2kfN7VPG2_5yfoq-0z4OYY2R0UHXJXhZ5qI9oK3z1Ha3pa-d0sZbi2qwkmxJm2LqSZ8McaEZUi_9HeEI3a2dgyi98blX8E9_7QWi2_fxvkjovBN7gYnCiG7WDfg5zc5mrXOiH1vR9GsipzKTZmDzrpmedIroaJC8ZF4I1xkjHWQLYxBSCR-WE78eURVME6pkZwxJa155YTu4653SmhIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPdJqOz17NnmMOpDXYXnQ0yYcQwNvlMZ5Wk17y0gSCUkD0LamjjO-inbSUefjEkmSuXUX8AzIOav51FZR20_cfjbaepZL1NTEQeUvU9PYtWAtErwF_N0zcqMK6NeoWfqnI26DvMwqSkzvaWKu0FEaJINL8FoPUKruMu0yrfdjsuxjeCe_QeBQQEQg4frexvDD0TgoqKD3IeG0CwXFn1TJxS-dUOZ-9SX11kiRBae6NrrwCvWnfmZwuEsxNUXUeF2XZw1gA_xWMBUSl9pE_2CKtr29mjdTY5yeRuNxysdndJGWoxR1lLOvyGIvm1o6xQCziQB3P6Oo-F4wFl1oKb2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRQhMk8etsday7dy-FBRP3HO2vSOIVL-BQ-h-mvj_oTc_3o-yTjL1D6gRDLfkrRmj-TqAe8sSwKz8wan4js86fP0G3rAUCQUAyyyD6XyIaf1WO-s4QGO5vUfVKg9R9Kn4KlDfu7W1opjKk26JJkiqmJV8muxlqKKM6Ga6MMM90SDVRHjddVPlrTKUjPn_6Eh590vg6ohNgFmqeDqKghKnRzrWfah6nuDlW3E7uEWDKbXQJPAX7C9LDYFhtugd8Ctf5JJ-pFYnr5NDwLNqlGTecn2RD_mXKEKEwcNLbXX13s6g6m6NX87wh6DEq_2To0lLjn3mKK2-Kh2HQM1eUYc3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حملات هوایی پاکستان به سه نقطه در خاک افغانستان  ادعای مقام‌های پاکستانی:
🔹
این کشور بار دیگر مناطقی در داخل خاک افغانستان را هدف حملات هوایی قرار داده است. در پی این حملات هوایی ۳۰ نفر جان خود را از دست داده و بیش از ۱۰۰ نفر دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/664497" target="_blank">📅 11:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcVKZYc2EfWePyn9Y9qAjT7pYnQMd_vPT62aIfqoLVGj8O7Y6l5HsGLYeWLhEhI3TLbVyByAKQdCITAUD_3RN9XfZJFDkiqHIIKSBVBKk7bxBfMpaNUMnqOcZ8bRPGrmwt_zj56b44aESOxC9ZPQYTDP4enInTQJwev39m7Ux8GJC60dFfrG_Zxi5BSMiGcpRwjY-S0SNdMZ7r3-K8E0LxwPOKSaha9NT-3T8QNs0Lg9Sxh6-uOy8Y-WFScickO-3y5TlPuoHmBnQnHxK0xAJN8xjCPHWvkqlpvB9BiBrJzbTeF_tlv_CJNnMZBDjHgH7DLygzWUYjQf6jDZpZElfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و سکه امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/664496" target="_blank">📅 11:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رفع اختلال در سیستم بانکی تا آخر شب
🔹
مدیرعامل شرکت خدمات انفورماتیک ضمن عذرخواهی از مشتریان بابت وقفه دوباره در خدمات بانک‌های ملی و صادرات: تلاش می‌کنیم این اختلال تا پایان وقت امشب برطرف شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/664495" target="_blank">📅 11:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پیش‌ثبت‌نام حج آینده رایگان شد
🔹
پیش‌ثبت‌نام حج سال آینده ۱۲ روز دیگر آغاز می‌شود و امسال ایران ثبت‌نام اولیه را رایگان کرده است.
🔹
پارسال متقاضیان حین ثبت‌نام اولیه ۲۰۰ میلیون تومان علی‌الحساب واریز می‌کردند و هزینهٔ نهایی ۳۸۰ میلیون تومان بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664494" target="_blank">📅 11:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtfUbg9K7-jUH1kZrOV14xWX1Mpr1OU0T09bkL66YThqWtunBgfbKnW4lXUvNxirBz3P6TGev-Ajr8C1V2HRzw1sNn55Nz6lKMhfi5E54MQ98bK1ez5pshSWN9XdhaAwKTuRGh1yFMo_qOtD_HioKfO1ILlSXFjYiElbCiZbdjxf1v436JBPf0RYpsdRt__fs_DlswQsxPUIQGVC28eOa3MpLQgr0wWm-aU3WQgXT9ToslLBHu5POUqh18A7d9Xl0ZmeHQE6C5eKFuMMnUinwMMol_BkJwHkIt1LMx6iHykOYG-RprmIejWKQO3qcNt9ZmMhJmb9aIrQQ5Zl8OuyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه‌های مهم برای سلامت کودکان در ازدحام و گرما
🥵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664493" target="_blank">📅 11:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f533fe061.mp4?token=e93794y-RWU6B7hZQhlreFTRFVumRN2e5TI1bEKfkxJueoTQ_EJNjR5IpplBnE2Am3K1nPGfrGzUxHmYQ-yqXd9hqRkUAN1mAQ6R3fr9Fpl-LkJ0LRjy6leQ65aXTY6WlRWrsdxxnjVuZ3poZqXoqXG51M73OE4fhcqmwIDRclsok7dAkoM5qYkAHF9NiBgPHzxuUd965R7moCOccPPSGanVZ2NiEoNQ2hm5ybFYIspbTtQIjwke1nY_Gy1efphVzlzZHOs7bLpshcRcNX8k-n8wvtvKPpsYXBeKt6UrzBNeTq4HU-Etm370G0DrTputn55IK_h_ebWwYwxdw1VMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f533fe061.mp4?token=e93794y-RWU6B7hZQhlreFTRFVumRN2e5TI1bEKfkxJueoTQ_EJNjR5IpplBnE2Am3K1nPGfrGzUxHmYQ-yqXd9hqRkUAN1mAQ6R3fr9Fpl-LkJ0LRjy6leQ65aXTY6WlRWrsdxxnjVuZ3poZqXoqXG51M73OE4fhcqmwIDRclsok7dAkoM5qYkAHF9NiBgPHzxuUd965R7moCOccPPSGanVZ2NiEoNQ2hm5ybFYIspbTtQIjwke1nY_Gy1efphVzlzZHOs7bLpshcRcNX8k-n8wvtvKPpsYXBeKt6UrzBNeTq4HU-Etm370G0DrTputn55IK_h_ebWwYwxdw1VMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بومیان آمریکا در مراسم گرامیداشت صد و پنجاهمین سالگرد شکست ارتش ایالات متحده، پرچم این کشور را لگدمال کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664492" target="_blank">📅 11:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رئیس‌جمهور: ۶ میلیارد دلار از منابع ایران آزاد شد   رئیس‌جمهور در دیدار با آیت‌الله العظمی شبیری زنجانی:
🔹
بر اساس برنامه‌ریزی‌های انجام‌شده، ۶ میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664491" target="_blank">📅 11:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5836683886.mp4?token=BFpHDwc6Sa3Xk3J4fodtVbbU23ctv5JzFrQU-ql4b30DY7NskJZs5anCgLVKB6LrsjU9MDMVN5DRdOorNxvlwHt2M-LukO2bKIHrd5WjVZNiwDk6TYifP82LbBIX7Gv8sGYtGT1yM-0mtTY1nQzPXi1hRtln-DBSuz2Est4gQmoiUc2TtpC1FjMpPYkkKkxCOsD4EIIJ7c6v9uL5uhj_2ArRmBEpKsNIr8QtXU8NXyWnlSknGnNOg3HouCrGpxHTjUlvAQ2vYJpjDi8bMqTCA0EIxV6oIigdMu6vqkYHeikBAiRWteGyw4aIVs1vXlmInDjcroFc4XMKr03ZrgFDNVNEPSYQRFZAdhPdcJ4YB931A8HtwZikWCsXQSwMgTLjlz_OpmvuhUl5dkCvwWpO0saTzSeLpH-_ZHGzOcoE4tQpkjtKauJZDsAZltIN5TX0xyRSc_H4keT9LRJgM-w9R-t7HCHr1gbVF1ZAkvqPYRDQthC9gTjVfKsXy2FCsT7IpmeR4Y_vVElhqG2QnncNuxdhRyaGHVAcGhID3_R6NPxLhhYCjX4PN5lh9GVV9TEWU7ghUMVq2ATEOfAslNeQ8G1KYuZjS04U5iBvmzHEW1PEpVEHJSC4dV-b5ncOA9bZByKUgo6RehsA4aEk5nlYOO7TQu9h9_LHJlC_DNfDF_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5836683886.mp4?token=BFpHDwc6Sa3Xk3J4fodtVbbU23ctv5JzFrQU-ql4b30DY7NskJZs5anCgLVKB6LrsjU9MDMVN5DRdOorNxvlwHt2M-LukO2bKIHrd5WjVZNiwDk6TYifP82LbBIX7Gv8sGYtGT1yM-0mtTY1nQzPXi1hRtln-DBSuz2Est4gQmoiUc2TtpC1FjMpPYkkKkxCOsD4EIIJ7c6v9uL5uhj_2ArRmBEpKsNIr8QtXU8NXyWnlSknGnNOg3HouCrGpxHTjUlvAQ2vYJpjDi8bMqTCA0EIxV6oIigdMu6vqkYHeikBAiRWteGyw4aIVs1vXlmInDjcroFc4XMKr03ZrgFDNVNEPSYQRFZAdhPdcJ4YB931A8HtwZikWCsXQSwMgTLjlz_OpmvuhUl5dkCvwWpO0saTzSeLpH-_ZHGzOcoE4tQpkjtKauJZDsAZltIN5TX0xyRSc_H4keT9LRJgM-w9R-t7HCHr1gbVF1ZAkvqPYRDQthC9gTjVfKsXy2FCsT7IpmeR4Y_vVElhqG2QnncNuxdhRyaGHVAcGhID3_R6NPxLhhYCjX4PN5lh9GVV9TEWU7ghUMVq2ATEOfAslNeQ8G1KYuZjS04U5iBvmzHEW1PEpVEHJSC4dV-b5ncOA9bZByKUgo6RehsA4aEk5nlYOO7TQu9h9_LHJlC_DNfDF_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بهترین تیم ایران در بدترین جام جهانی تاریخ
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/664490" target="_blank">📅 11:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رئیس‌جمهور: ۶ میلیارد دلار از منابع ایران آزاد شد
رئیس‌جمهور در دیدار با آیت‌الله العظمی شبیری زنجانی:
🔹
بر اساس برنامه‌ریزی‌های انجام‌شده، ۶ میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/664489" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4479807805.mp4?token=BVhNemPCzBpwx_T-3gZ_aim9gnb2IPJlvTEXchQ66ule2T9iQoBpw9j6e-a61Ti8tWd11DRmJpFnNOafcP0Tjwk21q64_mpTXC64vlrvXBJbvOYoazmcnP-MefpBoEDi2xBP176_UZ_KUZFLx9PLAmrkuNmKqgtA9qFpnEUwzK40ABKtg14HZBWMCUrTo8S_2tC1ZSZpuOovBf-NeLr8C3tvOyRfblOaTTqytQuGtngiEcdviCsv1oqI0lfNMjknDntpHSxgrpSrd9gKgUy0ZZp3WlwBABwrsVuKl2BSlIKDG-K3m7rq0INefWqt7lOrarmkhADunWiRKarnBty8Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4479807805.mp4?token=BVhNemPCzBpwx_T-3gZ_aim9gnb2IPJlvTEXchQ66ule2T9iQoBpw9j6e-a61Ti8tWd11DRmJpFnNOafcP0Tjwk21q64_mpTXC64vlrvXBJbvOYoazmcnP-MefpBoEDi2xBP176_UZ_KUZFLx9PLAmrkuNmKqgtA9qFpnEUwzK40ABKtg14HZBWMCUrTo8S_2tC1ZSZpuOovBf-NeLr8C3tvOyRfblOaTTqytQuGtngiEcdviCsv1oqI0lfNMjknDntpHSxgrpSrd9gKgUy0ZZp3WlwBABwrsVuKl2BSlIKDG-K3m7rq0INefWqt7lOrarmkhADunWiRKarnBty8Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال زائران حرم‌امام حسین (ع) از عراقچی
🔹
زائران عراقی در حرم امام حسین(ع) با سر دادن شعار «علی ویاک علی/ علی نگهدارت باد» از سید عباس عراقچی استقبال کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/664488" target="_blank">📅 11:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=Jc_0LhHn-ZTqv8aJZjUp59XW2yRjvKzPQGwtzkjYExnJFz_oAHhKi4d9MdSBvlZMtfG77DpNtSWPtASX560p90SzKo_sXIfHy_YicnrKq_Pnux38I4KZda9QNic7WEG7ptUG8yrw_-YEMyzcd43SEH1IYKLaxutV-P2B0zTBXEOwesMHG78EzV3q1R-Qb9qYx1Y4d2AWhkXmluvS0X486BbnkWyTFoTZETLyb6zbAHZwAo3K-gSmQpIKEY0QAoCL1gL3r1MBmjFJGiiYXGxYNeKvrguZpjkdbDFPaBTasotD9deN73Qfzq35-7ZNQZRLVjLrblD7DboT-P80JiPpy0rZUpiizrsEzr6FPwDvbhE0mhyZnYeoBkPLQZHqHxI1dlPzLBaGUWEJpCZmRakGVH2uzlXMJiyFr8Qth1_0NtuIDYEMQJWRmcv701pObyWoP9k3S9Oaafj-3zqJ-_wYEgO7woUuLbK-mPovnoZxPWA7FTVACPYBywDGQVopK1cHxzh6gy-keSkKhULuDT1hOIOYxyf1kxW8lxlFkD6nb_klXhYWlDozQAXMD9pdvXiWT8hmV9fYAKiYoIEjRDqkWM_yk3fLwms8MpCEGHNMkCVL02b2b0L0640LWFQsM_YhSaqtIWQicaoRVCIsR10u0IRIz-a0RLzA58Ai2GtZ6RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ce213c07.mp4?token=Jc_0LhHn-ZTqv8aJZjUp59XW2yRjvKzPQGwtzkjYExnJFz_oAHhKi4d9MdSBvlZMtfG77DpNtSWPtASX560p90SzKo_sXIfHy_YicnrKq_Pnux38I4KZda9QNic7WEG7ptUG8yrw_-YEMyzcd43SEH1IYKLaxutV-P2B0zTBXEOwesMHG78EzV3q1R-Qb9qYx1Y4d2AWhkXmluvS0X486BbnkWyTFoTZETLyb6zbAHZwAo3K-gSmQpIKEY0QAoCL1gL3r1MBmjFJGiiYXGxYNeKvrguZpjkdbDFPaBTasotD9deN73Qfzq35-7ZNQZRLVjLrblD7DboT-P80JiPpy0rZUpiizrsEzr6FPwDvbhE0mhyZnYeoBkPLQZHqHxI1dlPzLBaGUWEJpCZmRakGVH2uzlXMJiyFr8Qth1_0NtuIDYEMQJWRmcv701pObyWoP9k3S9Oaafj-3zqJ-_wYEgO7woUuLbK-mPovnoZxPWA7FTVACPYBywDGQVopK1cHxzh6gy-keSkKhULuDT1hOIOYxyf1kxW8lxlFkD6nb_klXhYWlDozQAXMD9pdvXiWT8hmV9fYAKiYoIEjRDqkWM_yk3fLwms8MpCEGHNMkCVL02b2b0L0640LWFQsM_YhSaqtIWQicaoRVCIsR10u0IRIz-a0RLzA58Ai2GtZ6RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از آخرین وضعیت میزان آب در سد کرج
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664487" target="_blank">📅 11:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZr4BfXTawOVIhKUT4VvFgJFIY4kF_lsUhK5jJRUxTU4McpLPqhILm60M9VUyjCqzYf4uuknY8_qt0oDbFJ8GFwmrRxCwGEUdrJf4t_r76kk5WKL_OA23tQjlJOtAaQO7PVquSiVM7GdIUnJk6w2jPUIiglD64H97UdB1J23Jd6mph6aMkSFSssbpKbDwjqe1FdoMjuJt6Kb7ZC55HPhu6ZjMDcYlvNhjznfUCsnVNYKEB2k2D17DPRqpVQuZaV9_V_86Qt3zeOonD3Dbh6tWQDEyH8NfvmLTLM08IybQy0EWWPgnq8xpPLfI5_2Fzki6Ap3h_ylf47m79jnSToFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kxe9iVTVp39XhgaRAfn4ybvFHowqGiNatAMYBYiHb-pPFtAkI1U9ViGxUTqh8Ci8_hUhLndHOGKIdS2PpbkaEoiL2baQHs8KL60yzfFMXi8CVk8G0GtzKCzc6LCsd68NGECyQ9oL6lWQutVyxsq7r0PeY-XnyTYeXldXEXER7iVVx79dDGbOQa-Qbqfv7pNWwWw1XnW5OFEuPryKtaNqzq6rFxz05TqeTKXq2x7SKkji1DXSgNaX7LUQYBGMf4zKNO2sihcsei2GoZXP82fyNXAOdwEc4fcf-7RYky61XsnzpsLG6nJz17tOzoC5b2ZJOk_xxSsiMdL0fW4PKXATww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbGDtAmsbBUTnR1TbmmT5vFBstXdqY3P6a3xNc6lFG8wDH-olc03np-ob1FeyV_nENfyglIST_dm4ZgFs0HsvRZDrzZs2eZp1Fi7izUsNSoqVOUTPlrwgCAR2AG-ItSLEuV6Gsbm2cr452wOCebndOTHMmJuFeQu5Qks-bFWIv0T5knk_Kr2HDKbl2F8dfJNFPwdqscXe-JksXwu6m6EMNHnYo5K1oQ__rSdr2H2s7CGU9rMBdQKzKZi6h0TgrjDBqc6_RQg5XELTp9G5cgZhSZ_38LaDZ6_gNRSky4CGUDpytoacdcHaO8-JqgCTZOI5Y6nwT2HW3tqb37YpkvhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW3FMz1xdnkNoEgNA1Q06zAy6iCqH5DLJ-MVHG1Csc3M-c7VGjOMwrrUUvzlpVgJuG50PNnN8yQ65iAzslPBRVuuzMaewfjRO2XztQLP4v6glxHBcMXTzJi_t8BJclb4oSMsNVFTDDdLPmLGZWN3Pyw1VnFitj6XIhuHv9zzF9OW_GCEgkPsmsE5GgLN4F9mougJFZfE3OQGCGGIsGIYd2MOZJZNx2QQh65nOZVSOwT2trH6IF-a26ilcBisLPlriWQ_0y0gs6VM6i60BG9PuHNW8Z3YCmVJ4uDS92L4iVy3VavpIOXwKu32y1WIlPkRlmMezOcA48FQBysSK4nPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISvxRPXOkyuCRAHS2DhQOiApdrw1xa8JFXmlywGim9G3N4XrRDWSLUUH9ByVppOtfjCaBiR-K_hx6oerIn7vXP3vRzGEh0CkuF2hcA8sBE-ZBcb7rIqKWigNVzasgXQfcNVuTv48M1VQDV7jptproci6WaLytEb-X6keHOd_jKDUr727wAXn1XZt_55g8hj_U4Zsnx4CW142jnUsRel-sIEwd9W1WyPxR1mdokkITEqGVtlTCfQctN-wzgW0NT0iGU9BnA-ru4WLI2c3bJlKN8o4mt-uPwPtwjfnOHwwujCQBqYyJf_vfL2umV1fF07M-FocrDeCnIDA9jariT5f2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGjNAN4cZ-Bz-03ldSD58ZlawPtfO5ZDu9rWxGhP9da33-ySO_2MOzNPn7QGpvOKSZXnzZ-A0v6k1Gryv4Ywh4A0za8YGogI3Bf3RC-6KUH4i3u9Dv0u3F4wagjaa8EOy9-vgJLtjtvzIbA7wXplYvPpgz6GMwCQSaJ89BLE6ERBDyDue6ruZO_H0-Bqc9J5rgbRn1EleHBGUbSYt3-UC-MqoX3NtYRcZddeaBDp7FvYURalqx1Ww2iZubVvKfuK2nob2A62b69JL9lZcSDmUZ4KIeqdW3aJzOLlqQPgn5rk2zO9fITw50Jh5O2tj_X1cpTWlWl8964fP8Du0IWLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJwQUS7kPuzRud4_C7458CkguwtjLygfIXuBrVC6lERqUKzYGOmzMcEVy2apCjff-khMHevU-wadM0ib4QGUpjcOYF255GSn1M7cIpVpDxwWMlTJGRvlHbxCUQB7EcIuTTnOE84k4qH67tcW0KLaBDhrnUZtP0bnqTSbdYRBrh_KZfApovRYdEm04ZD71eiXUNxhQk_ygyfc3teZQSjj0qzYfWmq9rba96KVgs43lMI9ZD15DInm6AYM81CrK3iuOwFCBZ5x7Zqyei3c0_RxDIf5iLC5uei3rAwwNzVL0uT-tryrRjUHCJF5w8SIsrb-sIa3BRjpqCNQEfGMdYw-ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷
مدل سالاد جذاب و پرطرفدار
🥗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/664480" target="_blank">📅 11:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
طبق اعلام مرکز آمار ایران، نرخ بیکاری جمعیت ۱۵ ساله و بیش‌تر در سال گذشته برابر ۷.۵ درصد و نرخ مشارکت اقتصادی ۴۰.۶ درصد بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/664479" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383515186a.mp4?token=lRhAPlOgucleNZZJWBOJHlWfJJ58UFVgt1gg_hDt0mVDBWvjleEMYG_t0a-TxyDiFaYLgG8oYYOo2nehl5c-u0uSHodbJCaeaaKSbveCATtKDpqNH5d9umaV2Xrv4zadO2mbp85BmVqETZAomi2ttdDFRy5OH0LlYC6wN_lkRZOW3fhBvUIE7gc5Rkc2vJBRyE9Uv-y23fA7XPTdfy5sgmZV-L0Jmo5Fz5bLRCZdRr6N7Ji7pv0uxpd13kRpmyqu10el85XibxIHfuoM3XwdYsb8vmRSv_zPVUVML4PQL_Ezr-22A7cvUMoYWFTlWxovnbjOVWZFH7Cp-jgBhkBxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383515186a.mp4?token=lRhAPlOgucleNZZJWBOJHlWfJJ58UFVgt1gg_hDt0mVDBWvjleEMYG_t0a-TxyDiFaYLgG8oYYOo2nehl5c-u0uSHodbJCaeaaKSbveCATtKDpqNH5d9umaV2Xrv4zadO2mbp85BmVqETZAomi2ttdDFRy5OH0LlYC6wN_lkRZOW3fhBvUIE7gc5Rkc2vJBRyE9Uv-y23fA7XPTdfy5sgmZV-L0Jmo5Fz5bLRCZdRr6N7Ji7pv0uxpd13kRpmyqu10el85XibxIHfuoM3XwdYsb8vmRSv_zPVUVML4PQL_Ezr-22A7cvUMoYWFTlWxovnbjOVWZFH7Cp-jgBhkBxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بد جوی شهرستان هیرمند به دلیل طوفان و ریزگردها
🔹
به‌دلیل تشدید طوفان و ریزگردها، ساعت کاری ادارات و بانک‌های پنج شهرستان سیستان امروز دو ساعت زودتر پایان می‌یابد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664478" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ea84be9b.mp4?token=d32EhD5nbgv9y9YSBERqp-8Q4X5omjZTf6csE1Vkws9IBfe6hv5eKbm96UA_rI1rg_rNZtElq5O04cNvX3mlXrITL-JkHWAb1sBMvtdQOZaZr2gzVNy1C9odwdEWO_-I2RPUTAMGdmgMEU3PvVVsfUse-LmEouMrU2KQmC01rTGNc2MyQxtM5sOinohQ7IVwKtuQr1c718xYetkRnvYdytP9Wbi5aP1BLg_rTuccm6_FJuJHpVxfElc4pyLMz5TDZWiJpWrdko2n3XATCgwhZ3pqSMiA0w1d4lPqzlwd7Fnk-ff2e6OCFp03MhVai3L0xNgO_anoGSx0bTAo4AKWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ea84be9b.mp4?token=d32EhD5nbgv9y9YSBERqp-8Q4X5omjZTf6csE1Vkws9IBfe6hv5eKbm96UA_rI1rg_rNZtElq5O04cNvX3mlXrITL-JkHWAb1sBMvtdQOZaZr2gzVNy1C9odwdEWO_-I2RPUTAMGdmgMEU3PvVVsfUse-LmEouMrU2KQmC01rTGNc2MyQxtM5sOinohQ7IVwKtuQr1c718xYetkRnvYdytP9Wbi5aP1BLg_rTuccm6_FJuJHpVxfElc4pyLMz5TDZWiJpWrdko2n3XATCgwhZ3pqSMiA0w1d4lPqzlwd7Fnk-ff2e6OCFp03MhVai3L0xNgO_anoGSx0bTAo4AKWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژ ماهانه گران‌ترین پنت‌هاوس‌های منطقه یک تهران چقدر است؟
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/664477" target="_blank">📅 10:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teyzJgIbE6Mo4QWrY6_fwuEhRYmVe_n0fR-lxiDB6pAg6NRhxf8hjmI4qnW8QHHQYt7R12NEs9XoKjbHBSCjapHz88S7nCyUzLDad5S-DtxouzlX8OjXN9ktQpfn6DQnRPMkH8iPneP2MK6RHvdfdyiY3S10oDS4tU9gnI5ohHRu5-b9Q6X7BGR_bzPwVlzS3tzQp378cgDPXTJ0zEKugsmHh8q3l_iV-YeKkJ1c9sG8jmf4HTyMYjgQbWblcTH7fdbhAjlCWx2YJZQaUyJZlP2wFPEP6hTkwPKzD0--Q8kTvLwDoBcQx5NK3rJPZqBmU_NpekaGa6uXF4vICx4DxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دردناک از تشییع شهدای لبنانی جنایات اسرائیل در الدویر، جنوب شهر نبطیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/664476" target="_blank">📅 10:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc7DslcP3-xynyM61AKE5yh6XXPzgjUqlNX-L8n5XzUMTtTXAnSDSWS3wGIj70e4yC45ZBY77jLx4fdvPx33O3-USMiJDMwQcVWQ9lDN-Dh3Yh7lVNwqmRC9EdYC3ypye78mANPjNGbV74Ft5ZYjHFhIEnUkTY3Bwj2c_EJ8sbFBfcxrwDHD_HAiWJPA-hKDkncb58GK1mED-VlHzXlMGaz2QCNzYEJFExj4RfLKrYh2Z7H05_yhAhWJtj0nThgDImgiYYDHDburGUMyrGQ4Dzikb_UFneQSRjQfR0RZVDvBgosAw7J1VSjhJ50giZ95tpXkfAJI6BijOMtEuMxxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثروت بنیان‌گذار بایننس از بیل گیتس فراتر رفت
🔹
ثروت چانگ‌پنگ ژائو، بنیان‌گذار Binance، با ۱۰۷.۷ میلیارد دلار از بیل گیتس (۱۰۵.۹ میلیارد دلار) پیشی گرفت؛ هرچند ژائو، برآورد فوربس از دارایی‌اش را دقیق نمی‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/664475" target="_blank">📅 10:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای مقام صهیونیست: حملات سایبری ایران علیه اسرائیل چند برابر شده است
🔹
حزب‌الله: توافق شرم‌آور دولت ارزشی ندارد/ سلاح ما با قدرت باقی می‌ماند
🔹
توزیع برق اصفهان: برق شهرک‌های صنعتی اصفهان تابستان امسال بدون قطعی تأمین می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/664474" target="_blank">📅 10:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بیمه اربعین ۱۴۰۵ در یک نگاه
🔹
هزینه ثبت‌نام:
۲۰۰ هزار تومان برای هر زائر
🔹
سقف پوشش‌های بیمه‌ای:
🔹
درمان سرپایی:
۳۰ میلیون تومان
🔹
جراحی و بستری: ۲۵۰ میلیون تومان
🔹
فوت عادی: ۵۰۰ میلیون تومان
🔹
فوت ناشی از حادثه: ۲ میلیارد تومان (شامل ۵۰۰ میلیون تومان فوت عادی + ۱.۵ میلیارد تومان غرامت حادثه)
🔹
ثبت‌نام در سامانه سماح با پرداخت ۲۰۰ هزار تومان، این پوشش‌های بیمه‌ای را برای زائران اربعین فراهم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/664472" target="_blank">📅 10:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgkUN-DzjgsIpxynNlKpa6eO_woSdRS-TJItKszMvxzKwrh6FRDgoFttS-ZkpB6DWDqqWEja9q1ndgmTREYrCS_oh8TDe_8lRSrjZ1ipbpbLzvM2k-k-goDWvBXmyT6PhnzRd92RiFjiTI9hMRvib7nQ6y6pChSBQI1_XOGOfMYbNXF1Vd1-9uYjJmXhNaLKGYUSeh5ylceuA3Apa7bQVBWhoJQFqTuZ86r32xrgd3sqZp4BV3dSsM3V75q7WEhTEkXAele8mruFz-sv6bdXtvR-m9IoiWaRen36l9QFy4gu3Qg254rTjcPc46L8hmRfTO4lcbQglA8aUKd8Kzj1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاموش کن؛ زندگی روشن‌تر می‌شود
🔹
گاهی یک تصمیم کوچک، می‌تواند آغاز یک تغییر بزرگ باشد.
#مدیریت_مصرف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/664471" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOft3QjjC_PNsOnDVi3DQx8PkU6IiRRwtw1lTrUEf85PpHCnqEZx1yW-87f2J7szHJV33Uf0TsJPUL0cufPFDYBAl4hw52Q1MvnKf6zGw-ZzezUpUznlYOftaj-m_OoZpypjRIWXFeEzsL8u5eatBLbAEu9yaa4sP8MSQr5WRXuL5GQYV_uraJtRkRBRm69xAVNVf-QnSzRMgQHEHrYgBy7NaEh1BdtyaCOXkV5gcO98hoq3nWsOIO-kamtFgWsKklQLXsIyR_rcPsa58V3RGtP4Rbrp7hxdRUlLEHk_aY6rb8y3kl1wSjJkFxhOQfTD83awtDgiPpFgqqXtNKxCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e05be977c.mp4?token=gCiSTE61ycRGKEQQtgqsYZMaf5fOEv9Jom4Gt7xqAkHOINglSzBHXxL-T9uTR8mEWFrc96jiQsAjIMBQ3DrqDqIsI19ytjLO7kyVvl-v-9ngLlfgFKy7ROESDFYiGFgYqEGeSgi6nNJJW7hQyMCfoSQm0ePRNmmcHdGjPcq-fjtp6KmIlqowO-EZvGPxIJD8OU-KjwiNKUKCgWaG7bzIWAXPDxa7o1EqBA9_gIjtxDM4pNl111fdYNxBDs2Wo2XznUQ-C4DPZ2zatuKnFle1wF01o1gewM1N0eY0oznxZQV_MmDx0LveAqKZefLUY1OC3nhdvQcuOiPU4S5LdoSP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e05be977c.mp4?token=gCiSTE61ycRGKEQQtgqsYZMaf5fOEv9Jom4Gt7xqAkHOINglSzBHXxL-T9uTR8mEWFrc96jiQsAjIMBQ3DrqDqIsI19ytjLO7kyVvl-v-9ngLlfgFKy7ROESDFYiGFgYqEGeSgi6nNJJW7hQyMCfoSQm0ePRNmmcHdGjPcq-fjtp6KmIlqowO-EZvGPxIJD8OU-KjwiNKUKCgWaG7bzIWAXPDxa7o1EqBA9_gIjtxDM4pNl111fdYNxBDs2Wo2XznUQ-C4DPZ2zatuKnFle1wF01o1gewM1N0eY0oznxZQV_MmDx0LveAqKZefLUY1OC3nhdvQcuOiPU4S5LdoSP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی کل پولت خرج پیامک بازی میشه
😁
🔹
در بازی دیشب کلمبیا مقابل پرتغال، یکی از هوادارای کلمبیا که کل پس‌اندازش رو خرج کرده بود تا بازی‌ رو از نزدیک ببینه، به‌ جای تماشای مسابقه، تمام وقتش رو صرف جواب دادن به پیام‌های دوست‌دخترِش کرد و بازی واسش زهرمار شد
😂
🔹
پیام‌های دختر: تو فوتبالو به من ترجیح دادی. «می‌خوای ولَم کنی؟» «اینه؟» «نمی‌دونی چطور انجامش بدی و می‌خوای من بگم؟» «اینجوریه؟» «بگو دیگه».
🔹
پیام‌های پسر: «زنگ زدم بهت که بگم دوستت دارم در حالی که تو چشمات نگاه می‌کنم» «خب جوابت رو دیگه می‌دونی» «ازت خواستم که بمونی بازی رو با من تماشا کنی پس...»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/664469" target="_blank">📅 10:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664468">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7df23a12.mp4?token=oEM8fP0huRuBzdazhl7GpZjlt1Er136n8JKCqVGKOJaAm_piPu-MvpJSK-nHqbrATev_yjOAPMENug0PitLKvrozNa6lv5hZ4OkTnl5Tt9u7cdOmhgJ3c-qVsikeARBGnwHf4Kn124Z-1TWeiOVzgacGVGYBpYstikKOjHpodKwC0_601GHG3DYIdcSPpHUdgDkD2iMc0UXJg2uhiSZFULo_OetLHDPLiiHO9YezfuiBX30lKEfNC6qqZu-1j50379v4Wh9KhTyQkL12fFChITZJpD5QI4wvIR4QHbygAggxy6ennrZb97LCW1_SYIrNj-q3v_QkQ7wOMkpvwcUmxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7df23a12.mp4?token=oEM8fP0huRuBzdazhl7GpZjlt1Er136n8JKCqVGKOJaAm_piPu-MvpJSK-nHqbrATev_yjOAPMENug0PitLKvrozNa6lv5hZ4OkTnl5Tt9u7cdOmhgJ3c-qVsikeARBGnwHf4Kn124Z-1TWeiOVzgacGVGYBpYstikKOjHpodKwC0_601GHG3DYIdcSPpHUdgDkD2iMc0UXJg2uhiSZFULo_OetLHDPLiiHO9YezfuiBX30lKEfNC6qqZu-1j50379v4Wh9KhTyQkL12fFChITZJpD5QI4wvIR4QHbygAggxy6ennrZb97LCW1_SYIrNj-q3v_QkQ7wOMkpvwcUmxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه رانش عجیب زمین در هند
اخبار هند را از اینجا دنبال کنید
👇
@AkhbareFori_HI</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/664468" target="_blank">📅 10:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664467">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آیین نامه سوگواره بدرقه یار.pdf</div>
  <div class="tg-doc-extra">260.6 KB</div>
</div>
<a href="https://t.me/akhbarefori/664467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
آغاز ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای «بدرقه یار»
ثبت‌نام و ارسال آثار به سوگواره رسانه‌ای بین‌المللی «بدرقه یار» آغاز شد. این رویداد با هدف ثبت، بازنمایی و ماندگارسازی روایت‌های رسانه‌ای و هنری از مراسم تشییع رهبر شهید انقلاب اسلامی برگزار می‌شود و پذیرای آثار فعالان رسانه‌ای و هنرمندان از داخل و خارج از کشور است.
علاقه‌مندان می‌توانند پس از مطالعه آیین‌نامه، از طریق لینک زیر نسبت به ثبت و ارسال آثار خود در بخش‌های مختلف سوگواره اقدام کنند. همچنین در صورت عدم امکان ثبت از طریق سامانه، امکان ارسال آثار از طریق شناسه رسمی دبیرخانه نیز فراهم است.
#بدرقه_یار
🔹
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
🔹
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/664467" target="_blank">📅 10:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664466">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxpab5NQTa2KI7gZT0rpIGd4MGA-r-3xG2ueXUZy5SxJkAiRLKmZMmqL7HDl3MQXi7iG-9aN_4AI6T5NdUfSQNfFyuGhugM4Vyo0zZADTS3ji-XxBCtIU_GlebwhYjSX_DMm-k3UoU6eCy8jq2-qYI117hvq3VwNagklG_qDkKsuofWaSH0rgCngM64B0XpYvnoe_8FkJHny3TAaMoWBRCL1Uaczss31SV2WTDawdOEM1MCHqiVGtyaCAuwND73sozmvJtimrmaSAr0lGRKgc_za_UQu-L2sKJg6QjpEcArwsbn0xsR_baW_ZK1mHDgi60BdJQx1A-FP4SLrQJ76Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر فقط ۲۰ روز افکار منفیتون رو بنویسید، چه اتفاقی برای مغزتون می‌افته؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/664466" target="_blank">📅 10:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664465">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc4e45b02.mp4?token=uFHhHGRX_2Jby2-sJQwlpN35Js9Bdyt4Tdprx81hrsrXOCciTF-lW3KSl2rzXrpTq_frmDqbt5eQ3goS3P0D00vBGWH9YgLZmPPMv2wsPAeIylHQPIT43z4FCxdB7SYEDmAMMezBH0p5jgezF58u0Q5wWeYVVKe42WaS8GtA4F7UX6Zo8Cz5k2KG5GtNYg6vE1D5P3rqGS0AMbQF_hWBtY-nAh0X0sHb5qQglYroXFNpwqZHM5hFGcLnbFJ6CBS9OestYh6DO1Jb7kvp8pXEr34AW_-JBnwkY8ym6y8gYc1dN91OzcdOEaWFt35GuVHZSzgvXjMokO4onKQthdvdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc4e45b02.mp4?token=uFHhHGRX_2Jby2-sJQwlpN35Js9Bdyt4Tdprx81hrsrXOCciTF-lW3KSl2rzXrpTq_frmDqbt5eQ3goS3P0D00vBGWH9YgLZmPPMv2wsPAeIylHQPIT43z4FCxdB7SYEDmAMMezBH0p5jgezF58u0Q5wWeYVVKe42WaS8GtA4F7UX6Zo8Cz5k2KG5GtNYg6vE1D5P3rqGS0AMbQF_hWBtY-nAh0X0sHb5qQglYroXFNpwqZHM5hFGcLnbFJ6CBS9OestYh6DO1Jb7kvp8pXEr34AW_-JBnwkY8ym6y8gYc1dN91OzcdOEaWFt35GuVHZSzgvXjMokO4onKQthdvdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری و کمدین مشهور، استاندارد دوگانه غرب در برخورد با تیم‌ ملی ایران را زیر سؤال برد!
ترِوِر نوآ:
🔹
عجیب است؛ بعضی تیم‌ها فقط درباره فوتبال سؤال می‌شوند، اما از بعضی تیم‌های دیگر می‌خواهند درباره تمام اتفاقات دنیا توضیح بدهند. درود به تیم ایران که مجبور است این بار سنگین را به دوش بکشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664465" target="_blank">📅 10:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZYGKF5vFfCg80k0EBmSuzOxg7RqqDk7fK4veUFKYXDkEGnWbhJHHbeaP-Fz4KBIrOiYZ7zvtt1NvnnqKmRk6pKkJVpr6WW8WVARPqfdLMJTTWrELin4cK1AN0ujxwUwtiP38wYdP5oE9ejikHOcZICefQ1Iwy1MZMu-2TcXHnyQ5TulK_pA98qXfrKF-NPYb88zXgE0kQ_iiCBmsH4QKh4Bl8vGX8IjwpI2QhwdB8CqyTm3yt7IOuoiPcQ36yXBS6BbGl-wRemX-7e_mlvpthr2NcD9CZ9pcz8IuQGL9NRF52dzuVu6QobadsJ8OsyAb88hZh3AGcuY5-D-krklgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخبار توافق و مذاکره را چطور بخوانیم که فریب پروپاگاندا را نخوریم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/664464" target="_blank">📅 09:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33605d2c04.mp4?token=cpuTJZzUx0NAPIeQ5vtaMu930xYijnIF1HaeBE8W4h6chyG7wIyNnE7zkcbXTo7Jk9KakXhXN3j7XtdoxQS4nN8ynoP1ADTMiUO6wUvfIGB9Gd1yBHOW6R2vjwI1VGCO1OeL0c2lrMcmyXVgJ7LO9K24p4bJHZ5_pOSLRt-zC2nNnpdxeHXXd1B15OUsePKgn5UqsA_u3tZNhn7RdKSej31-eT04-bMgLUtqIWz4wpwa-HQlS_oGuOHESn6f0Eq-FtFJO0celfgp7rX6jSStzJ74M_X7YM5-0d-EdXVuN7neatu_gAWU2hVvfzHCBQVtr3HE4Q7n4222wnVUvEbLhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33605d2c04.mp4?token=cpuTJZzUx0NAPIeQ5vtaMu930xYijnIF1HaeBE8W4h6chyG7wIyNnE7zkcbXTo7Jk9KakXhXN3j7XtdoxQS4nN8ynoP1ADTMiUO6wUvfIGB9Gd1yBHOW6R2vjwI1VGCO1OeL0c2lrMcmyXVgJ7LO9K24p4bJHZ5_pOSLRt-zC2nNnpdxeHXXd1B15OUsePKgn5UqsA_u3tZNhn7RdKSej31-eT04-bMgLUtqIWz4wpwa-HQlS_oGuOHESn6f0Eq-FtFJO0celfgp7rX6jSStzJ74M_X7YM5-0d-EdXVuN7neatu_gAWU2hVvfzHCBQVtr3HE4Q7n4222wnVUvEbLhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسروپناه: خانواده نمی‌توانند از قاتل امام مسلمین گذشت کنند
🔹
قتل امام مسلمین، طبق ادله‌ای که در جای خود بحث و اثبات شده، حکم قصاص دارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664463" target="_blank">📅 09:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664461">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwtRko5wAVTz5SrL4yfYP6kD-OYOcIp2WiAKgsyajdupKJcRIIzNV6ti__CLCtNQQzglRCd5x1f9m20JhW8j2h5-AR19JwgkBEKaQkS0jubA-Wt1kFWNovAzCvj1lppExwpPWpd4_DFbzASLpDJPb455ySsdJmfBIIUq3t7id62f5LoovCa5WcYOR5kEExt_q2cYFnooxTwVCk1XzyDSYSlzc6XcaY7JorLjzO6dHhAPQcnSEPohpOx9CiYZUWJimIGrlnRneVA0BUoVUHgkQLmtufar4V9nN4JhzrkMfM-lu-0Jb245twVXtIwVT8KI9wanoNlxpZam5h0TCQZjjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg5Uf_IN6D2VCtJI96vELZDFz1oAHRTuoX2bDGowFfqSFKu6xaTaQ13XipbCsqhUZk-wi3UbhKHQOiIaK6fb_l7sSb0-vTXr-GUgcO1yvQ9g4odzchAoHLAWTmh3I3bE8-MMV0fAcd3cMjOqxCK_25gjWob4364qfMxTVk0d2SkL6WPebvYwH-jPj27am1cKo-YhNUYLbmsh1oTnqgKzN64uXzMQR5_AepIyDf0P6IwvFJGyIv6kPtt7F3lT7qdavhT04U305ZyciG4zgx7YqxPKvNFPuWsob1531oG7kPiD90misbgLBMqO12jIMFvWQpkFWJbmOhve0-EIkI-vEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
علیرضا بیرانوند: شرمنده‌ایم که رویای صعود را محقق نکردیم؛ اگر ثانیه‌ای حالتان را خوب کرده‌ایم به خودمان می‌بالیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/664461" target="_blank">📅 09:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664460">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769989de98.mp4?token=iwJnAE7CXxbAnzW-QIAcjk8r085x_uuDx6O0qdMEfP9EjAv5nqujJcc_n38tDNP-cVzG5tt75naVw3o4rkxCbjV7WH4L_DHt1ZQgq4-wxQ4gJl1n9ezjSxklVPKxDLo8t-OYXJGHGizcf_wkgsu8IaXb9gRoyjo59vMLcwClfhEF6IiLge7hyRwMP0Iz8HDvUfTvsusrsgHnMBfJ39nbuJoWGFRIiWZ2w5j4X4WJC4ZWCeEx0UBC2_ot3NlbCOcfXDYfsLzqnuu_G_5X-6TO6aTqeCF8Ux5DmkmnCK4Fh92s44P9V3WSAkITxaqUBrZR4hmNINvR_RC3BfW_4dpoDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769989de98.mp4?token=iwJnAE7CXxbAnzW-QIAcjk8r085x_uuDx6O0qdMEfP9EjAv5nqujJcc_n38tDNP-cVzG5tt75naVw3o4rkxCbjV7WH4L_DHt1ZQgq4-wxQ4gJl1n9ezjSxklVPKxDLo8t-OYXJGHGizcf_wkgsu8IaXb9gRoyjo59vMLcwClfhEF6IiLge7hyRwMP0Iz8HDvUfTvsusrsgHnMBfJ39nbuJoWGFRIiWZ2w5j4X4WJC4ZWCeEx0UBC2_ot3NlbCOcfXDYfsLzqnuu_G_5X-6TO6aTqeCF8Ux5DmkmnCK4Fh92s44P9V3WSAkITxaqUBrZR4hmNINvR_RC3BfW_4dpoDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدام مدل گوشی سامسونگ ارزش خرید بیشتری دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/664460" target="_blank">📅 09:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664459">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
روزنامه هاآرتص به نقل از یک منبع نظامی اسرائیلی: ارتش تاکنون هیچ دستوری برای عقب‌نشینی از هیچ منطقه‌ای در لبنان دریافت نکرده است
/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/664459" target="_blank">📅 09:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664458">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvoAA3M2wrPlY1_fpTlAPdAHg4CV9p6XBG2RFo08Sq_RCBpJtSyLfJ3K9C0V8ufwnQQ_gDhQksH3Pgu2bg1HCzjVhVD8uTAxGXhsgfncPnfidL2AJWa4r7NCuPTfqIzL9cOL40SRyFZj4RV8_5L3UVQMWhaMP__aKjKzMN3WCzgu0rNclJZ-EODmKkBGJxI5UiY0Hlx4I0BJMpba8PMyJCqFiqrjaJYvXlcA11u9DP97rqEKDo2Nb6G9u91V2aT6Mq3YnNRbZxy6hJZGTxiAsFm-lxsoXvPFHF21gizoAzm79tLi6km-necNKK9SFyaqChCAT8V-6FZMin332_9Wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتشکده ساسانی زیر و رو شد
یک کنشگر میراث فرهنگی:
🔹
چهارتاقی یا همان آتشکده ساسانی «رُهنی» در فراشبند مورد تعرض پیاپی تاراجگران اموال تاریخی قرار گرفته و ساختار آن به هم ریخته شده است.
🔹
کندوکاوهای غیرمجاز قاچاقچیان درون عرصه آتشکده ساسانی بی‌شمار است و بیانگر نبود نظارت مسئولان مربوطه است/ ایسنا
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/664458" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664457">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bb3f50a0.mp4?token=dQax8haSP9ui3rHlP_wR5geJVVErTYXnMExJQn7H1Etob-PLSR1xcMxQarK-xErC0_LQgraOgx3TZFifSCt4PowFPNXJYp5tfn8JKTRpYLDp5X8swILPhtryUhJBIdLlgRoGWbzV1_WDXk-AXmgIRUW8gYQ3HiqWLzZ5-V4ZCbKSiy8iQYoK6yCKPWe-pLj-LFvdJv0pDC9D1KstfDRCB_4n4JPriB2RJ7JSAJHu4DduVaMnZPqM7mfHkxgVk8fpA8HNwtdSIFQTeeImq5mvwULm-_b88l4viZ_jttwBbz-mc6jQYrLUhTsd0tQrRVVrCjzf9dfn2ANIAN8jxpDuMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bb3f50a0.mp4?token=dQax8haSP9ui3rHlP_wR5geJVVErTYXnMExJQn7H1Etob-PLSR1xcMxQarK-xErC0_LQgraOgx3TZFifSCt4PowFPNXJYp5tfn8JKTRpYLDp5X8swILPhtryUhJBIdLlgRoGWbzV1_WDXk-AXmgIRUW8gYQ3HiqWLzZ5-V4ZCbKSiy8iQYoK6yCKPWe-pLj-LFvdJv0pDC9D1KstfDRCB_4n4JPriB2RJ7JSAJHu4DduVaMnZPqM7mfHkxgVk8fpA8HNwtdSIFQTeeImq5mvwULm-_b88l4viZ_jttwBbz-mc6jQYrLUhTsd0tQrRVVrCjzf9dfn2ANIAN8jxpDuMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوادار یا جادوگر!؟
🤨
هوادار عجیب غنا در جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664457" target="_blank">📅 09:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664456">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تکلیف کارگران بخش خصوصی در تعطیلات مراسم رهبر شهید
وزارت تعاون، کار و رفاه اجتماعی:
🔹
در صورت اعلام رسمی تعطیلی از سوی مراجع ذیصلاح، این تعطیلات مطابق ماده ۶۳ قانون کار شامل کارگران بخش خصوصی نیز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664456" target="_blank">📅 09:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664455">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f18d83442.mp4?token=rQO3myvllcFPS7eTeDUT5nYLpyrNu5v69mhgtljCqc6KORbjRfXNlkxms_ojtYHQAHliopeD5iY5sFIaod1Izae8W0gixaNos9-5h2Z3heRVq4MPs3004HZGvvii8usEtRnTrDdWoUXifH8kN03Jma81YTjdCuHcBrVPQbWL_fQ3cf0U069Q7bNDd2ADdstQLkvwoRQkUNbTblyj9lYvQ1SeGYIxtzgN6snPIQWxvupk2YBhAGrcfifEkxYpiWH9vI0VBaA-ig6Di8Dtfgds4-fcFaqH9jUHGEFPBQ6B8ic68CK-RVE_ixf7sh9zoK7ZSqND64VPojp-eKmT-NDnTRrfKSu6gjmPKVlarc0euvL0-QsmLjsKhcS7cYGLoWftLdA4RUdc-AHhrlqk7XzCkbbV7u87sAxUZgkejO2yrpzpHwK9mt3c-F7riKgMpjER-jbR9Wq8qu2W0tGUf3BJDQu7BQ_e_QT-sm2-wGII2_Ef6F-_F1PJjBiMo8gT_TR3GyOPWgnufaPpMXaKudbmslpez4NST2BxleR4Hl2CAU_R2vbFB-JC_-oJLefh70eCMw3cZkQOC_LAXZlDuBtQ8QPYzkh2EkmdLC0xpCe_c5Qrn3PTFTv6fpejqCSRxV2egU_e6xb_RUJsbM8oJRCF03Gl5rPOng_dEu6IGMTvBkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f18d83442.mp4?token=rQO3myvllcFPS7eTeDUT5nYLpyrNu5v69mhgtljCqc6KORbjRfXNlkxms_ojtYHQAHliopeD5iY5sFIaod1Izae8W0gixaNos9-5h2Z3heRVq4MPs3004HZGvvii8usEtRnTrDdWoUXifH8kN03Jma81YTjdCuHcBrVPQbWL_fQ3cf0U069Q7bNDd2ADdstQLkvwoRQkUNbTblyj9lYvQ1SeGYIxtzgN6snPIQWxvupk2YBhAGrcfifEkxYpiWH9vI0VBaA-ig6Di8Dtfgds4-fcFaqH9jUHGEFPBQ6B8ic68CK-RVE_ixf7sh9zoK7ZSqND64VPojp-eKmT-NDnTRrfKSu6gjmPKVlarc0euvL0-QsmLjsKhcS7cYGLoWftLdA4RUdc-AHhrlqk7XzCkbbV7u87sAxUZgkejO2yrpzpHwK9mt3c-F7riKgMpjER-jbR9Wq8qu2W0tGUf3BJDQu7BQ_e_QT-sm2-wGII2_Ef6F-_F1PJjBiMo8gT_TR3GyOPWgnufaPpMXaKudbmslpez4NST2BxleR4Hl2CAU_R2vbFB-JC_-oJLefh70eCMw3cZkQOC_LAXZlDuBtQ8QPYzkh2EkmdLC0xpCe_c5Qrn3PTFTv6fpejqCSRxV2egU_e6xb_RUJsbM8oJRCF03Gl5rPOng_dEu6IGMTvBkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش زدن نمادین متن تفاهم‌نامه توسط یک مداح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/664455" target="_blank">📅 09:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664454">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crxqJGKgmP4SpzIY-juEp8Rai7lbxK0CFaZyYUNXL3Gxi4ntFLct672c-uVzwFEZ14zDBaQCKbEbdecVRi4Z_Nt0Hz9AkVUQ1Awc1oHzXFCU8N4CCTr9T0wx0gUNJnV7tsOuWYsKKqjLiTAEpBHglR5N7rkosVDLUWkd1koZNaUaAGN8R-JPbwEvChkEdBnNmAyKno3QIAGavpabpkVVfFO7beRWoiIeCLQgPIlM96PLgklSOhuF2_dm8gR1io9pJl3IYbnGy8ejA3pHEfe7PXAz2UUZklQnqiCWXqy3orvOuOeUiBlXTaTfww-XnHVCYzTZUuQS1uhnPSc3qdocjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لیونل مسی به اولین بازیکن تاریخ جام جهانی تبدیل شد که در هفت بازی متوالی گلزنی می‌کند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/664454" target="_blank">📅 09:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664453">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
۱۰۰۰ مدرسه تهران آماده اسکان زائران رهبر شهید  وزارت آموزش‌وپرورش:
🔹
بیش از هزار مدرسه در تهران برای اسکان زائران آماده شده است.
🔹
زائران بر اساس تقسیم‌بندی ستاد برگزاری مراسم به مراکز اسکان هدایت می‌شوند. #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664453" target="_blank">📅 09:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664452">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8430e98b39.mp4?token=dcW5LO7bth-iddqP7JVp3Ga9VMdcUMXDYw6ikosQOKDwJ-xSn4JqJUVNj4ACD60PSEvWIaTdNo_ZyzwVh0ZQ5pj1dg_Ee2K6bjGqcFKy8AOFSMuimDATEpwAD5E59BAaDWuFr2vFJpQT1u0OVmQ6T37CUJjXi-OY0QV4IK_tqKvmQqxvE8bOtBogHeTVY0psXTe2g8P5dEWShzgRhaEgCKtwADa1N0bASsKL1u2qMkoloLvsC_7QdkKUq-8XKuQY4QPzRXfFai--i5tapcum2PJluN5g-iOFVbcWLu7yJMqBbTUVyBZ5-tzOy21xYeaMoM8-YiNouD49IlpHjucLZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8430e98b39.mp4?token=dcW5LO7bth-iddqP7JVp3Ga9VMdcUMXDYw6ikosQOKDwJ-xSn4JqJUVNj4ACD60PSEvWIaTdNo_ZyzwVh0ZQ5pj1dg_Ee2K6bjGqcFKy8AOFSMuimDATEpwAD5E59BAaDWuFr2vFJpQT1u0OVmQ6T37CUJjXi-OY0QV4IK_tqKvmQqxvE8bOtBogHeTVY0psXTe2g8P5dEWShzgRhaEgCKtwADa1N0bASsKL1u2qMkoloLvsC_7QdkKUq-8XKuQY4QPzRXfFai--i5tapcum2PJluN5g-iOFVbcWLu7yJMqBbTUVyBZ5-tzOy21xYeaMoM8-YiNouD49IlpHjucLZ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز مهندسی چرخ‌های قطار؛ چرا مهندسان آن‌ها را کاملاً استوانه‌ای نمی‌سازند؟
🚂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664452" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664451">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1q0PVs6HHqwlv__nb9MIjGacWui9c1syWk4Gk3RkPHED_n2XmrBEfS7AgQIafFXV6wWkAFZFtOoStE8n7KYHOI27lCSt8girwU6MT7J6iglr30CZ3O2T2yeu9liPqoj6WdJoADsVz58feidxq_7ZuhSFsulMmbwVTREXhccBZIbTClLP0DBXUh9po578LZGw7Im8UxWOY3drZe7plLceFPdGqgT1gcV9Xl_KPXRtso7Mc1RgF-G-cBC3D0rWSedueeaeAeJ1ovvfRp0nmJ0EBasHMM1_q1-YaQfgh30SiRO3akHJF9c0rGWFl3w0amSndcaVolfSA9w5WdTcIkWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه پهنه‌بندی استان‌های کشور در مناطق ۲۲ گانه و مبادی ورودی تهران برای میزبانی از زائران مراسم تشییع رهبر شهید
🔹
بر اساس این پهنه‌بندی، زائران هر استان پس از ورود از مبادی تعیین‌شده، به منطقه اختصاص‌یافته هدایت خواهند شد تا فرآیند اسکان، راهنمایی و ارائه خدمات با نظم، سرعت و هماهنگی بیشتری انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/664451" target="_blank">📅 08:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664450">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq9ObgmKnxah4vxtKN0jMswysSiWF4wweSDAnToQc5nfXfG1WlcjNUwgd7kKokoxHOJDJAdvB6ETyiZYl4P2L-HfVbpmAx4qj7IZh-SDUvHkwxy5Jg4Rm9Dni3f_7nxf2PKTqoNMgk6vaB3-UmIHJg4aD6wKBw3iGerlmqBp_qtcL1l2-0d1c8NbtCNjt_U-7KysBRuXtWTBq7ChXmlHgrtuR34dvPPgWdjrSE-6nz2BgQDSmJ3VUVDKnNDMkzSALW5yhSWZ8OZ95hW295JlwL9okLeg_rt93343jN6APIlRyEmY4nQPqFog2hehAc1PKHdzTV1hfRRkmoSopLzKCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قول روشن، سرزمین خاموش
🔹
وعده بود اما تاریکی ماند #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/664450" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664449">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dbaf0174.mp4?token=IPQ7tyiCLY3KIkOc2aOjwDeOFVy0HZqyFnXxunY7rjXBcMemsRe64xApNt7dKi84n9YA5QwjEXaAX4gDwNUvslow5p7qpai8DLRff8E7eGl_xWdHYEhsqHMNnV0UjLlszKOynTQeUyIlti-RmLHQG0NEwxsXhlBEP_XLw49SKiQb-ViCpcJaXkvxLP3af2UDfL1kQXhl8gYIxvvBitAVyWp78TpWp3Nb-9JmCMy-HTHNJtXbugX_F1oHAZDqwhrBHzAy9LiZXIc4sCxOraEd6biaVe5bmgJMqok43M3h3SscAy0o31ouHVQ0g1Wt_N0kmdMDgqDOuZASEt4fNHQlLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dbaf0174.mp4?token=IPQ7tyiCLY3KIkOc2aOjwDeOFVy0HZqyFnXxunY7rjXBcMemsRe64xApNt7dKi84n9YA5QwjEXaAX4gDwNUvslow5p7qpai8DLRff8E7eGl_xWdHYEhsqHMNnV0UjLlszKOynTQeUyIlti-RmLHQG0NEwxsXhlBEP_XLw49SKiQb-ViCpcJaXkvxLP3af2UDfL1kQXhl8gYIxvvBitAVyWp78TpWp3Nb-9JmCMy-HTHNJtXbugX_F1oHAZDqwhrBHzAy9LiZXIc4sCxOraEd6biaVe5bmgJMqok43M3h3SscAy0o31ouHVQ0g1Wt_N0kmdMDgqDOuZASEt4fNHQlLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت ونزوئلا بعد از زلزله‌های مهیب چندروز پیش
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664449" target="_blank">📅 08:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664448">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyUGiCNNj4QRrpUeDOJb8g4CflM_k78PviqK5jmL0zeWTF0Kgks-wicxhfqs-YKcS8fi8FtU9IypFedEbOCjOfDgE1Cx7Ih4WaadhZZHkXLlzo593ozZ9_-nwa2EA9xYzAyX0BmNg4uQyNtIHHyrEpfiOy1lyNSKwmylp_Ea-tDax6lThq2_JQEUoJOZghIfblRzeNNdeXMSMDBoc3DeLTkf8tBpbpM0zaVlN-aJd2xRWTvsofb8IClVkaWUAHhXTCy09fPLo3EUWSIINdfhRc3hSIsW3ioa_3NM-C-wcmWVrLYTX33UDV2ZEcTzzZG6_xztGnPvPyEp-X2gcJ9zRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب اما واقعی
🤔
🔹
دانشمندان می‌گویند موجودی میکروسکوپی به نام «دمودکس» روی پوست صورت بیشتر انسان‌ها زندگی می‌کند؛ که نه دیده می‌شود، نه احساسش می‌کنید؛ اما سال‌هاست همسایه همیشگی پوست شماست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/664448" target="_blank">📅 08:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664447">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شریعتمداری: ایران نباید با ترامپ مذاکره کند؛ باید عده‌ای از نمایندگان کنگره جایگزین او شوند
/ کیهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/664447" target="_blank">📅 08:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664446">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مرد سرایدار: همسرم توقعات مالی بالا داشت و چون نتوانستم برآورده کنم، او را کشتم
مرد سرایدار (متهم پرونده قتل همسرش):
🔹
سرایدار ساختمان هستم و درآمد زیادی ندارم، اما همسرم توقعات مالی بالایی داشت. با اینکه ۲ فرزند داریم، مدام از من می‌خواست پول بیشتری خرج کنم و همین موضوع باعث اختلاف بین ما شده بود.
🔹
روز حادثه هم بعد از رفتن مهمان‌ها دوباره بحثمان شد. عصبانی شدم و با مشت به سرش ضربه زدم. بعد هم دستم را روی دهانش گذاشتم تا ساکت شود، اما وقتی به‌ خودم آمدم دیدم دیگر نفس نمی‌کشد. تصمیم گرفتم صحنه‌سازی کنم و مرگ او را سکته قلبی نشان دهم، اما نشد./ همشهری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/664446" target="_blank">📅 08:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03dea2b515.mp4?token=kp5Dz22efXg5gXoZBjjXRM4godD0H_8kYgc7CziuCzYuEXpz-DeDZzt5mJXyc84apOxWDWY_4R5gBy1JyDzBf97MvcpeJfQJ0SI-jSFyWooSGjqZE2PJ2AD3PsgHulHJHdbYfTAJE8W0FHKXBvrs9mGYJvXZMqk3qa2DcpwZKRYJISpV2uT6q8hBVgv2g4umKUShUViXU-NbXlpkOaBOjsGYPsCWzlZ-VpbmbnTvvmRGZszEn8q2i5hn9ekMtxnJ1fC2ysR4h7Dx3oGl3a-cVBRQwvWApYahGH7PSnjAdEYXcxYP7v9nEwEIKg6lm9y5dOGRNIjZwjoENPHGGiJ8k3EhLD5nYcrC3jfNgsjltbkMipzdYtuDtWLb8kH1YvIJVzXdGZiGx9tcQoef2__yiI4N_Tr99VF3g6tYmE0Ras2uUiBJY4TSsBGS7HwlXwDdzya2WeF7L4s0LDkd9uONnLgkIcbSBCKSsAo3oCv_Wk0dYDffIsLnsfPNy2TSEdYPbTG7JR_tZQxj3lE25HNxdeZQnGVtOQzB7vdb-JB3KElaZDcoqhm30Dt_ye-bxAFtYohcDQvcEnqIqv5OtWw92SmMBMIYon5SIQdIdCqdogoc0Y_qJVwvhcYGt4JgMJSAyYGPAaHU-lZlAyJj_LnFy5d_xScwf-GdzxVbBj53guE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03dea2b515.mp4?token=kp5Dz22efXg5gXoZBjjXRM4godD0H_8kYgc7CziuCzYuEXpz-DeDZzt5mJXyc84apOxWDWY_4R5gBy1JyDzBf97MvcpeJfQJ0SI-jSFyWooSGjqZE2PJ2AD3PsgHulHJHdbYfTAJE8W0FHKXBvrs9mGYJvXZMqk3qa2DcpwZKRYJISpV2uT6q8hBVgv2g4umKUShUViXU-NbXlpkOaBOjsGYPsCWzlZ-VpbmbnTvvmRGZszEn8q2i5hn9ekMtxnJ1fC2ysR4h7Dx3oGl3a-cVBRQwvWApYahGH7PSnjAdEYXcxYP7v9nEwEIKg6lm9y5dOGRNIjZwjoENPHGGiJ8k3EhLD5nYcrC3jfNgsjltbkMipzdYtuDtWLb8kH1YvIJVzXdGZiGx9tcQoef2__yiI4N_Tr99VF3g6tYmE0Ras2uUiBJY4TSsBGS7HwlXwDdzya2WeF7L4s0LDkd9uONnLgkIcbSBCKSsAo3oCv_Wk0dYDffIsLnsfPNy2TSEdYPbTG7JR_tZQxj3lE25HNxdeZQnGVtOQzB7vdb-JB3KElaZDcoqhm30Dt_ye-bxAFtYohcDQvcEnqIqv5OtWw92SmMBMIYon5SIQdIdCqdogoc0Y_qJVwvhcYGt4JgMJSAyYGPAaHU-lZlAyJj_LnFy5d_xScwf-GdzxVbBj53guE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس وطن‌پرست در آنتن زنده اینترنشنال، مزدوران موساد را رسوا کرد!
علم صالح، استاد دانشگاه ملی استرالیا:
🔹
این آمریکا و اسرائیل هستند که با ترور کودکان مینابی، دانش‌آموزان لامردی و بسیاری دیگر از ایرانیان، مجرم و جنایتکار جنگی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/664444" target="_blank">📅 08:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664442">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_ttKZwosamUE-Gl3fWC7t9ADEN3XCalcB3aYVzvp8ZMDSIi-QbnejPWV6FV6GC4nexVgbSm1wszsRmf3vxLd-3BSmRWn_piXfOJ6kZdmBWs9a16BfbEVEWTD_hXM5llr-yTzUk9WBYF0mHTs1G7BoQ3vQePV8ljqgC4LukCePz7or9eF62_P7m04zYBFJ3atxnUiFHZITK-ALjkU2Qhhno_cd3XOSN_WoDiJ1exOYjkzLte0mBYDfnF2X67HjTVUOQD0iWtG5B3wpVNTTTd-HW4KxyrT93p2UXOXYNrb3pFXvYDFj9sRloNoI2SJLAEzKnr22yQbjDNVcvw4Et0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرحسین صدیق برای بار دوم ازدواج کرد/ همسر او یک هنرمند نقاش به‌ نام ساناز برزگر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/664442" target="_blank">📅 08:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631f75a19a.mp4?token=K0HYayFXO3agyNfED9uu5W5M_uaewXCcS_BhJQsC35A4OxAO1WvwuA44aqI076FHOsq_hX5AwOPy_PDdHtkfMuAVUire_n1BbPXldNvj3EEMwA660kaRcIvU-ReM7ClT2ZuBf6NS_UOJialI6aqfU7dzt06PkSV3Dn15xlVD_tnerUsZTolQsC6Rb5JJmnvwD_CUT70t1fRwdVMJApPaZCWVEr7xi50rrOyKaJ3uAlxFpbADfBBhlrdvvZOGM3Fre8WRhh_Ae1INhSN4qXQ10ULHuWEtKd6yI9MSwqH0_XOVU3UohRsQ0E4aAFaCUV6BwkOLb8usJmWvAJat8zl_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631f75a19a.mp4?token=K0HYayFXO3agyNfED9uu5W5M_uaewXCcS_BhJQsC35A4OxAO1WvwuA44aqI076FHOsq_hX5AwOPy_PDdHtkfMuAVUire_n1BbPXldNvj3EEMwA660kaRcIvU-ReM7ClT2ZuBf6NS_UOJialI6aqfU7dzt06PkSV3Dn15xlVD_tnerUsZTolQsC6Rb5JJmnvwD_CUT70t1fRwdVMJApPaZCWVEr7xi50rrOyKaJ3uAlxFpbADfBBhlrdvvZOGM3Fre8WRhh_Ae1INhSN4qXQ10ULHuWEtKd6yI9MSwqH0_XOVU3UohRsQ0E4aAFaCUV6BwkOLb8usJmWvAJat8zl_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین برای تقویت زانو و رباط صلیبی #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/664441" target="_blank">📅 08:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSjrz251K_OS6QY2qrlBhb5Q0SiSBB4sJ23mC5KzLgcf9xykN-T_JJLZhGiJaqJ-UWOr5Xmec4xxkIcLobwNiPhwepPSP3ADUx9JABIMqOnK6I1hVM2HSHCdf6n8bJjxpyekXcv2LzYBxRrUe3WPbGlZ-nEyzrXA7iPkQA_E0Uz3nWrt6Ge7j65EwTDIs0ClPy__PZL1R-3wEzTWBxdWAuFFsY7HidwMuiO1DUv5JIdCgbgPnhlSLNddo17LdTdQ4UG6auycKLQUmxiybucqCMnRhLI2jkSmu0bco3HJDCVV5-2mk3nLyp8gLUZvKCjSziylRQZSW7Ci-hPaH9Oeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم سالانه با افزایش بی‌سابقه به ۶۲ درصد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/664439" target="_blank">📅 07:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664432">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
فردا؛ آغاز ثبت نام زائران اربعین در سامانۀ سماح
ستاد مرکزی اربعین:
🔹
نام‌نویسی متقاضیان سفر اربعین حسینی از روز سه‌شنبه ۹ تیرماه در سامانۀ سماح آغاز می‌شود. زائران باید گذرنامه‌ای با حداقل ۶ ماه اعتبار داشته باشند. با اعلام بانک مرکزی، به هر متقاضی ۲۰۰ هزار دینار عراق به‌عنوان ارز اربعین اختصاص خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/664432" target="_blank">📅 07:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664431">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK40AGEI6eEOFcCEbqjd46bsggmcFQtodiuD4VoYbIdqiMPV13cQaNGBU-2hLhZRhkX3xpXTqB_dJEHlUmrfQ4gpUAkFGEp7HJU2qvR0fb6blCs9aJ-GUIAWcgdLng4yzcxLUeVQGzrWfN4wYQfuCMyddEK_1d2bTAZKp02JFdtc9szVrtXk0dZF6QoGwfpnBLzOZxHuKShXSAEcRjHgo7uuu_RuQfpNUns9fkyC7leh-8eUvrJ79OG7MxC-CT40ayu6S7llyqYNlMqPPhGkXY5EWWRvvhLQulQu9mGXqAodDdRenVkLqLGz2NPQ_80bmTCVqNEM2jQ33zin5ahfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۸ تیر ماه
۱۴ محرم ‌‌۱۴۴۸
۲۹ ژوئن ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/664431" target="_blank">📅 07:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664430">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoZgkO6RL9ppFOF0lqfEM2eMxiRtTcI6_NsSIOVoWCgPv7flbtMCbKjGaFUjgSuE4_F73f4fHZAtrBfv9NN83mNg5P9vpFS2i6_9MBq7EGxAZZ-C93Y5JQJr4737rnRTSFTwtXr3J5IZKNXXn4oxkh_dTlY1GPRKbVaL9Y60J81iBY94x-YzJqurkbzebjhKqPZ8_Pn77IsM6DcYvhGvKfojMAEAULtgR8leHHvbo599S0_FOiH6LOKXRKltL6dBs-S2GIPR3l1-ESEkGStih4CRJWdkflMvKHB1p1YHZE4KuGkpPqXSQJU9mUAojGDLUEF-S6ICVTzN7ormE8RvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
«بازار خوابیده است.»
اما یک سؤال...
اگر فقط بازار مقصر است،
چرا بعضی برندها هنوز مشتری دارند؟
چرا بعضی کسب‌وکارها هنوز دیده می‌شوند؟
و چرا بعضی‌ها حتی در همین شرایط در حال رشد هستند؟
👇
جواب این سؤال چیزی نیست که همه حاضر باشند بشنوند...
ادامه مطلب کلیک کنید
👀</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/akhbarefori/664430" target="_blank">📅 01:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664429">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5GzaCm0-BYZvCw3-kEpeIttjd0O53aIRjnH1BzeHvjkWwX4yB-ZYFFG1rT2JbkG3ID1FD9cCuQkSMn5GZwiPhaMnHVPbfS--huV4eDDZbza0cor_OsisObqtmiVuu4xPlGMQ6vbGRGagkWKPrP_-yh3Itp2TyXHJbni6GEFwtJw0vcIbPtPpGu72YAVGjd-EYndjia2S8n6MKWNBdZiZ7k6xnxv_LVh-0mV7PByNzbfe_TweAbV_LsIs3TFc38jPTUEh8vnFrUlYp9IHyogtJRjNuwKRHY_SRFWDH6zlhZczTmq8_yQqkfGL8xsK2zThVjRtvL4ZiWFqAebGB8jrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
توپ تخفیف در سوپرمارکت ۴۵دقیقه‌ای دیجی‌کالا، ترکید!
🎁
کد تخفیف
۵۰۰ هزار تومانی
💥
تا
۸۰٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
همراه با
ارسال رایگان
امروز از محصولات سوپرمارکتی، شیرینی و تنقلات تا پروتئین و میوه رو با تخفیف‌های ویژه سفارش بده!
کد تخفیف
:
TT551
فقط امروز
⏰
بزن بریم خرید در سوپرمارکت ۴۵دقیقه‌ای دیجی‌کالا
👇
dgka.me/Wcjhnscdl
dgka.me/Wcjhnscdl</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/664429" target="_blank">📅 01:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664427">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eN-rBfaQsLLAJ0hvjdvzaz3zjWKOyjh9q2JPbxEOYeVNBIlLlJyZe07BKN8nOWWTrzL-kfjIpHZj9FEtLPOgUgowdXDr3QCOp7cLfN91ZENyGHY5816D7UuAvaDiRzZfZWihw30ppk5HYWgWG3mO_YKfpTuN207YFq5NO9lFvQsFYat0tKwOF9zbGOm9wNsFan-HTy0g34KcKIZfoUcFy37p_nsTgJi_CWTuQ8PlGaa41ujTVr7gCukhlWzUwl5grx1ACu_9yZ1sEwBEdWd2Kj-hD8obECJsuyQjVsP7BVCXVjn5NrK3C6Dbp9K_xq36WccMo8h-NkQ1Feji5dTFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/777c44dcf0.mp4?token=OzBLin2DV2WgpV74mj4makBCl4lP48WXki8Qas-LXzZb2N6kxs5N_V9V5PWBzNZEIJqhOfHOD5_lF8gXtOX2LNsOXD3ZBtK6vivjVX_RTiDakKJ-nYMNjfyqm16nvK9J9cDidwT7Q2QUeSvPds4odDOJZVjzIeGbMU-84HEA1gl_RabxTJUE27xJBE68jAgms6wxv_f1tPEUoChJD4-ZLciwAmJdein5NkREghTwvexHJpk34rsrEpReeHsdtSasXCwWbWHn3z9wBRBESVHntFMb29riDHxxng-TQH18Vfun9wAPExWT94PuSSPnAWngHxE13LNgb74HBZBvt0v9ng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/777c44dcf0.mp4?token=OzBLin2DV2WgpV74mj4makBCl4lP48WXki8Qas-LXzZb2N6kxs5N_V9V5PWBzNZEIJqhOfHOD5_lF8gXtOX2LNsOXD3ZBtK6vivjVX_RTiDakKJ-nYMNjfyqm16nvK9J9cDidwT7Q2QUeSvPds4odDOJZVjzIeGbMU-84HEA1gl_RabxTJUE27xJBE68jAgms6wxv_f1tPEUoChJD4-ZLciwAmJdein5NkREghTwvexHJpk34rsrEpReeHsdtSasXCwWbWHn3z9wBRBESVHntFMb29riDHxxng-TQH18Vfun9wAPExWT94PuSSPnAWngHxE13LNgb74HBZBvt0v9ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت نماینده عراقی؛ کشف حجم بالای دلار در خانه
🔹
نیروهای ویژه ارتش عراق با یورش به منزل «علیا النصیف» نماینده پارلمان، او را بازداشت کردند. همچنین گزارش‌هایی از کشف مقادیر قابل توجه دلار در محل منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/akhbarefori/664427" target="_blank">📅 00:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccecb9bbb9.mp4?token=Q88UaCzy0Q3xxubQBFWzMZsjL2D3bmZmbaUDSqyQSqTi63dxTcW7WWHQty37Xh0sVuEXBnmRvKaE1XUebHacSd_Y6D9q1uTcnYkE9lcHOv4YydrxmlWbfr2kNeZx5g4oyGO2QwnPwszYMMUb8aaa84U1klBwTcHDSk6Ig8ZYLbwwAqGdOP1FXTadboW-CRTfp8XjBKQScS8hNFeD4sV6NwxdFytoDWnZaEF8RFOvu9eBjcqvqsKg-MYNnvIhPk9fw1HhnAT9eygc5vW31sKVqxtTAI1zb3PI0rKWX5y_hdR0kqSBRP2sU-VCFTdKqQMEv-r4mRV2BteJOJ99P0DUW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccecb9bbb9.mp4?token=Q88UaCzy0Q3xxubQBFWzMZsjL2D3bmZmbaUDSqyQSqTi63dxTcW7WWHQty37Xh0sVuEXBnmRvKaE1XUebHacSd_Y6D9q1uTcnYkE9lcHOv4YydrxmlWbfr2kNeZx5g4oyGO2QwnPwszYMMUb8aaa84U1klBwTcHDSk6Ig8ZYLbwwAqGdOP1FXTadboW-CRTfp8XjBKQScS8hNFeD4sV6NwxdFytoDWnZaEF8RFOvu9eBjcqvqsKg-MYNnvIhPk9fw1HhnAT9eygc5vW31sKVqxtTAI1zb3PI0rKWX5y_hdR0kqSBRP2sU-VCFTdKqQMEv-r4mRV2BteJOJ99P0DUW4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶ برابر ارزش کل باشگاه رئال مادرید در دستان ۲۲۵ متخلف ارزی
رئیس دادگستری استان تهران:
🔹
۲۲۵ نفر تا پایان سال گذشته ۵۰ میلیارد یورو به بانک مرکزی بدهکار بوده‌اند؛ رقمی‌معادل ۶ برابر ارزش کل باشگاه رئال مادرید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/664425" target="_blank">📅 00:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1ba0e245.mp4?token=Vq6D13wLhG3zDvd9TWCBBmNvkFdgmeXMUfEpdLvbD7WSNITW2YRgdkhXY8WMiyP-sE1t3rET0ElNcI-2QEcnVcQDhp-vLzetgBo2ISqGIESZ8E0hf5gvrPybmWTAJMPIh6iIFSszMDKMsVRXkdCoR5UBFbhfbj1iZ2yC_OrdM85rUP4vM9kmaFypGi02P_ePWlT2CBheT2dO9_-FwCOOlHouciigxAfixcyCLZm6gO0Vg9KTcB7UxsKJE9O5cXHOdYW4T05KxoX0P_yAYtD_j__le7zZZ5BEG_0o1PSAi2ONYA41729GbY6qDnitFPaR6S74w39fdlqpxGGtUxL1tUz0G1lodUtQHV4lc-TdjD9AAKu4f4Jk1waT3fn8XNWgzInQTI2wEa9GbD-NURRA_9k30P8grXplHkQNQV1ZqpUUBKhwWMDHPpd8QeJ9JCBAOf6FI_Iqkms39GM_B5spsBNNLRRPWuT0Xe9y7JU5SJ2yXUgtnci05qCptBbSjvBzhGGG5kqmUdoj-5FD7LIS3Bp6HDDNIARtW8VRmvzQVQcWHkslo6ir8ewIqYJKMQy11bIAH4mBDRJeVA0KENQxRRDoFsPNEQcyv0NnLyJgZpKH_gcv014QFMpCFZvHSb3tykD2GWLaLjIbSZ2Lc-KoxkLZQKkypVj8QshRY_dfXoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1ba0e245.mp4?token=Vq6D13wLhG3zDvd9TWCBBmNvkFdgmeXMUfEpdLvbD7WSNITW2YRgdkhXY8WMiyP-sE1t3rET0ElNcI-2QEcnVcQDhp-vLzetgBo2ISqGIESZ8E0hf5gvrPybmWTAJMPIh6iIFSszMDKMsVRXkdCoR5UBFbhfbj1iZ2yC_OrdM85rUP4vM9kmaFypGi02P_ePWlT2CBheT2dO9_-FwCOOlHouciigxAfixcyCLZm6gO0Vg9KTcB7UxsKJE9O5cXHOdYW4T05KxoX0P_yAYtD_j__le7zZZ5BEG_0o1PSAi2ONYA41729GbY6qDnitFPaR6S74w39fdlqpxGGtUxL1tUz0G1lodUtQHV4lc-TdjD9AAKu4f4Jk1waT3fn8XNWgzInQTI2wEa9GbD-NURRA_9k30P8grXplHkQNQV1ZqpUUBKhwWMDHPpd8QeJ9JCBAOf6FI_Iqkms39GM_B5spsBNNLRRPWuT0Xe9y7JU5SJ2yXUgtnci05qCptBbSjvBzhGGG5kqmUdoj-5FD7LIS3Bp6HDDNIARtW8VRmvzQVQcWHkslo6ir8ewIqYJKMQy11bIAH4mBDRJeVA0KENQxRRDoFsPNEQcyv0NnLyJgZpKH_gcv014QFMpCFZvHSb3tykD2GWLaLjIbSZ2Lc-KoxkLZQKkypVj8QshRY_dfXoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی به زندگی خوابگاهی در دانشگاه‌های آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/akhbarefori/664423" target="_blank">📅 00:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664422">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fdc5a08.mp4?token=XIw91tXhLi67qtqW_NzUsGE2BLvvuJAbyG5U_YU95Q8G2ecxV_GfNqplvXjKceZrkP0kgjpVwZ80roEAPDz3CwtO242gtTGtx5dfz7WTIZ4U212Gx9w-6Ee84sITg0khQZjz09s-SpzUPMvkw9RBdxxHl1awEHi0MpSC1HsWSDOh1FX7OvLWt-d4pSk8y86sLtYKGbe-biefoLGc0oXXH7YRBrWVm9XAW6grsNaAnKG98CzIf2GPpXxMUDoxd5HVwD7HPqXnjhTeJgKSUGvy-Hj56J2gUJ_rKrao7X7IRNqU0guKRTnH0dhMyjdHdiyOzzzS6Z19mJmdXBa64ugZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fdc5a08.mp4?token=XIw91tXhLi67qtqW_NzUsGE2BLvvuJAbyG5U_YU95Q8G2ecxV_GfNqplvXjKceZrkP0kgjpVwZ80roEAPDz3CwtO242gtTGtx5dfz7WTIZ4U212Gx9w-6Ee84sITg0khQZjz09s-SpzUPMvkw9RBdxxHl1awEHi0MpSC1HsWSDOh1FX7OvLWt-d4pSk8y86sLtYKGbe-biefoLGc0oXXH7YRBrWVm9XAW6grsNaAnKG98CzIf2GPpXxMUDoxd5HVwD7HPqXnjhTeJgKSUGvy-Hj56J2gUJ_rKrao7X7IRNqU0guKRTnH0dhMyjdHdiyOzzzS6Z19mJmdXBa64ugZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان؛ ارتش رژیم صهیونیستی شهرک «مجدل زون» را هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/akhbarefori/664422" target="_blank">📅 00:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbab2c972.mp4?token=a0OGO9tktggZRbYfhUCJMCA5xu_ZQe2U7F4PDd1LvX0w1sDbNiXcBhyRP2IflMf8SCm1vnr3rgVQzAUv4iNMN_FrypLd6YIbPxRUJ-tp47qMP0LVOG0t8I1cp4wOnwodvXaZw2O2O4yv-R3gFWFH6ezfkuUrQivoXqeCZViTgdDuMyQ4NlcZuC7l9Z4vkRqxqmPMjDcWrPtWjNlszef9CTlVa1_G0CFQi4hRWHP4jR35-4ByMP5bFBwLCD2LEgX8jSVCu8aqgFtUEQYGiwTLqZHZvSbGorg04uvWPzOClthOVZeJ2YX3B_gnKdIjJMoDkP7m9UWnz3yzn725I4zJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbab2c972.mp4?token=a0OGO9tktggZRbYfhUCJMCA5xu_ZQe2U7F4PDd1LvX0w1sDbNiXcBhyRP2IflMf8SCm1vnr3rgVQzAUv4iNMN_FrypLd6YIbPxRUJ-tp47qMP0LVOG0t8I1cp4wOnwodvXaZw2O2O4yv-R3gFWFH6ezfkuUrQivoXqeCZViTgdDuMyQ4NlcZuC7l9Z4vkRqxqmPMjDcWrPtWjNlszef9CTlVa1_G0CFQi4hRWHP4jR35-4ByMP5bFBwLCD2LEgX8jSVCu8aqgFtUEQYGiwTLqZHZvSbGorg04uvWPzOClthOVZeJ2YX3B_gnKdIjJMoDkP7m9UWnz3yzn725I4zJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسرت بزرگ تهیه‌کننده برنامه مشهور Top Gear: نتوانستم در ایران برنامه بسازم
🔹
چندین بار اقدام کردم اما اجازه ورود به ایران نیافتم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/664421" target="_blank">📅 00:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
حملات هوایی پاکستان به سه نقطه در خاک افغانستان
ادعای مقام‌های پاکستانی:
🔹
این کشور بار دیگر مناطقی در داخل خاک افغانستان را هدف حملات هوایی قرار داده است. در پی این حملات هوایی ۳۰ نفر جان خود را از دست داده و بیش از ۱۰۰ نفر دیگر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/akhbarefori/664420" target="_blank">📅 00:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
نشست آمریکا و ایران در دوحه    باراک راوید، خبرنگار اکسیوس:
🔹
مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کرده‌اند که حملات را متوقف کرده و این هفته ملاقات کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/akhbarefori/664419" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5993005a.mp4?token=YrDFK63ik3RIFdUTKncXUjWhPLLOKKm82wAdZOvGRa2RJ5g_QrJ5ysqfNtHM9KMraUK4_iyEivx98df9-krVhgMx2vX8z8Yz7frmP3FWinqLP8OisjGFiThBY_dB0xSgDmyCDdpUobTNW50wFOa_8p0iiM1OxsmtUlJ5feVDYb2n-3lc2WLWb35_7qO9yfOh0fC5mCecn5Us3ibZaTssvB1YUdmtWHm1KbpFBrn8A_FzY2vB8QKOdjDE7C-APZRCBwZgABwZYcJe4ACRQpj25088i4Q4qw8IzIE47RuYqiQD5NzSAZ-cDcw5eZ39JX79ZKFgyZ1CCHnBR6b34YvtUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5993005a.mp4?token=YrDFK63ik3RIFdUTKncXUjWhPLLOKKm82wAdZOvGRa2RJ5g_QrJ5ysqfNtHM9KMraUK4_iyEivx98df9-krVhgMx2vX8z8Yz7frmP3FWinqLP8OisjGFiThBY_dB0xSgDmyCDdpUobTNW50wFOa_8p0iiM1OxsmtUlJ5feVDYb2n-3lc2WLWb35_7qO9yfOh0fC5mCecn5Us3ibZaTssvB1YUdmtWHm1KbpFBrn8A_FzY2vB8QKOdjDE7C-APZRCBwZgABwZYcJe4ACRQpj25088i4Q4qw8IzIE47RuYqiQD5NzSAZ-cDcw5eZ39JX79ZKFgyZ1CCHnBR6b34YvtUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«
هالک ایرانی» برگشت؛
سجاد غریبی پس از ۳ سال دوباره مارتین فورد را به مبارزه دعوت کرد: «تازه شروع شدم!»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/664418" target="_blank">📅 00:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b479ed2ef7.mp4?token=C4AXRn0P1AZHK_E1RA_CLICaBvM7SDsSf0bQ6ic9O8y_iykEM38YDk79fVNI17YOiLRXBczWFaI4NvsY3xHcHjrKHGzku95E8qcjkf_omc_p1H9cp2e8HPA0kqVZ_D1W-0IBydFgh2wrff6oQyPugJTZAzuNJNlcT8u8R0ImfDUf47WvUjxRRcxqw5ZFT2v939DqxsjeKCn-U7CehcfOKNoL-tkgTOa4JQB3WNQviIr7NN7-JrcL3Mjvg1CmQ8H_GGrXtjKmqBoKeMsvwn2vzPYlWSj5NOqPcBqxwFhiRZQI9cI3aqf_1P9TJdh6879pOxeqkfXYHVRbSkP9Pzoq7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b479ed2ef7.mp4?token=C4AXRn0P1AZHK_E1RA_CLICaBvM7SDsSf0bQ6ic9O8y_iykEM38YDk79fVNI17YOiLRXBczWFaI4NvsY3xHcHjrKHGzku95E8qcjkf_omc_p1H9cp2e8HPA0kqVZ_D1W-0IBydFgh2wrff6oQyPugJTZAzuNJNlcT8u8R0ImfDUf47WvUjxRRcxqw5ZFT2v939DqxsjeKCn-U7CehcfOKNoL-tkgTOa4JQB3WNQviIr7NN7-JrcL3Mjvg1CmQ8H_GGrXtjKmqBoKeMsvwn2vzPYlWSj5NOqPcBqxwFhiRZQI9cI3aqf_1P9TJdh6879pOxeqkfXYHVRbSkP9Pzoq7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایالت کنتاکی آمریکا زیر آب؛ سیل شدید جان ۴ نفر را گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/akhbarefori/664417" target="_blank">📅 00:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA5-a0mZUqaUDSGjKXL2jU3W7GUbNqf4c6ZJ9Y9TIhyZbWQ7OzXe5zK7WBML091_aosYZ2xaHeBamJbilrCdIyV8PGPbLXjcYzNGKa1pRuwGMCNr0rErWYH95KHFAnrS-YeQh-nUqX3siz2Y2ajKzoNYdFTFl6l58wk5EEcUH2g-_QXAvcPOdA4ahADLjzV66OmgFm5ZOaJk9ax2wX7fqEXP87abzCHEbCSlsC7KJFEhYHS3X9nXbvcpvsXz_ZMzwvUakzdPIUdQriAW7I37tCloqq5YsSdLPeTojP7OHhaQe0BfS9rqCwLrZZUC8W9eVSjNfH5C2m6uGcX6tScdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاج بر خاک، تخت در باد؛ آغازِ شمارش معکوس
🔹
تاجی که با خونِ بیگناهان تزیین شده باشد، جایگاهی جز زیر پا و در میان خاکستر ندارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/664416" target="_blank">📅 00:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04ed2bc321.mp4?token=fjocHiHWnhY9kWY2vp2si1TS2YSyr9VzVE7IPpd8KydwyiZ0-N-osCpuSW0hE0YZeSTmCdMC4TtNgIrvc0u2cBDifoaQtlvJEpM7qJ6ROC8hSyQML31rbhGIj4dWZmsNDi2TSbNWUWYeslKJH7G5AuUNWJ1ZcSiJzTO4A9ao4Hs9zDLlVvTGvK4HDnfgtApUtgj7JOFLATOPyLPLKhq52FLieMmB4OjA2cfagn6LqyyMW-dWnQ2600onZ2sagPxRsg13MpZy56uCeR90FXpZsjPTKe1_0Ga0zxKAm-Z4lrEPVf0gy3dNMeIhe7pTGr5tGnkTSI9DpWuAhxtg_W2iVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04ed2bc321.mp4?token=fjocHiHWnhY9kWY2vp2si1TS2YSyr9VzVE7IPpd8KydwyiZ0-N-osCpuSW0hE0YZeSTmCdMC4TtNgIrvc0u2cBDifoaQtlvJEpM7qJ6ROC8hSyQML31rbhGIj4dWZmsNDi2TSbNWUWYeslKJH7G5AuUNWJ1ZcSiJzTO4A9ao4Hs9zDLlVvTGvK4HDnfgtApUtgj7JOFLATOPyLPLKhq52FLieMmB4OjA2cfagn6LqyyMW-dWnQ2600onZ2sagPxRsg13MpZy56uCeR90FXpZsjPTKe1_0Ga0zxKAm-Z4lrEPVf0gy3dNMeIhe7pTGr5tGnkTSI9DpWuAhxtg_W2iVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیب در جنوب لبنان؛ ارتش رژیم صهیونیستی شهرک «مجدل زون» را هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/664415" target="_blank">📅 00:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664413">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ff4662cc.mp4?token=WHVzzad4SQBVQmWBu9e-pi66gfnOUhWR_c30XoA2kr7NVYduNfULVKEQDBxU32-bRuuu3h6gCWKrfKaDvAYy8zAQr_GLJUO4p_F8hXCjd75DM53ZwYN5Tzq3pcOrzIbJKh4Agoac75fbIlSHpck6Uov3pGM6YWM21jYmRXnXs3zCLdebVWSS38wfqom6g4fXdXQlW26Fmpe1WKurpcu2QJ81GGx_7ttzf9tCddjO00-Ir5n18VXtwGas_NWLBfrDPqcPJ5dZ5-1EwMl7ZSkYfmTVfHdUEtcqktc8HXjaAIOAGmAc9zx1g-dkgGJyyMvnHBgv_6z9xs0wEm4vPzDQRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ff4662cc.mp4?token=WHVzzad4SQBVQmWBu9e-pi66gfnOUhWR_c30XoA2kr7NVYduNfULVKEQDBxU32-bRuuu3h6gCWKrfKaDvAYy8zAQr_GLJUO4p_F8hXCjd75DM53ZwYN5Tzq3pcOrzIbJKh4Agoac75fbIlSHpck6Uov3pGM6YWM21jYmRXnXs3zCLdebVWSS38wfqom6g4fXdXQlW26Fmpe1WKurpcu2QJ81GGx_7ttzf9tCddjO00-Ir5n18VXtwGas_NWLBfrDPqcPJ5dZ5-1EwMl7ZSkYfmTVfHdUEtcqktc8HXjaAIOAGmAc9zx1g-dkgGJyyMvnHBgv_6z9xs0wEm4vPzDQRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در هر کشور چند روز باید کار کنی تا بتونی بازی GTA 6 رو بخری؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/664413" target="_blank">📅 00:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664412">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8u5wmHJL9FSLHZe95OMlIqwLKVUG2bDXjDJaZm1JBtyb10vKEkZ0DT_gnK9pIYXx0Gj4ZYVnYB6I0Pr6Nv4MYh4MUSmlqJenNU7Nn7Ih3kkne8CaWLOSArPOuJoiomJ8q2Y2QFzr8JM-DPWwAmPp_IKVRaLr1bCOApk9boz-4MdRKU1i2XoDGCqT8OX-TvFu_e7YqRwXUQQ9NIKkfyaYavJzf__gF_YCqiTdmnbTriDsuxnUPllQwgREMcy2GX8toxpl45EFF1dPTr2dpgK8rR3kyAAkE509dIkCQeQ9lpzR-w7LcyEQVkcqT9XirWu7JMC5wg5h5gWrKOq504_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: مذاکرات فنی ایران و آمریکا با وجود تنش‌های اخیر ادامه دارد  نیویورک‌تایمز به نقل از یک مقام آمریکایی:
🔹
علی‌رغم حملات اخیر، مذاکرات فنی با ایران طبق برنامه پیش می‌رود و تبادل پیام‌ها از طریق کانال‌های ویژه برای جلوگیری از تشدید تنش همچنان…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/664412" target="_blank">📅 00:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664411">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-toZcGt0nDKjG20dhponc_71caWgA83ctT17gxH87tEJVhceSkxCgPYwwTlQyndUJPEuv2AhTP4ewhLuEEaKamcUz4TZWAvHS2b_4xaMp5hLnt2ltG9mvk5ySmwqgUI4n5kdsbpp8UlRR8W96YYF6L5lC-5LUuLR1u6fqNTaNI_JtjmJhwI7aQMPy7GVZCvotFZmYbHY-Dnu6jQg2LLyzzJZ5PSR8EW86W--lRFs9XTbQbzjEROgjoYvOzpzhLPySjebB_LtznyGcLcCDOMJL7kb5x6hKAM3MgauxhWUbacfUKbmayfYt-wZYr_7EcVtMugEWdV9sy7_qCFGeCnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/664411" target="_blank">📅 00:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn-LoyljgLVQSqq1W4l9_tX6fAOi38Lz7jFLklDcirObhFxba8UIfiDS5ycHsiUw1xmNJtt11U7bUOl8iBNMZsQ1nqjl66xOq2pzAhX4MKHxaeU-FPhv08ZmlAVMVjbHEjXet0Ib5X_5ZFTZIIbLfkNrvOR1xoIomYPYCrOr5jCDTpOiRfejPwQ_5n2GqGJxJUNinpWz0YVoUVtOACG1wgtkqIJ7lFujvPoQb0ijR0_nb2nAIyGvQ1SkGJpT6zHrVNEkAFh0Z2dFXUcB2kWkwCROYCpQJl0WJdKhBFqP5A7so7Atjfp55sp7_7gDZLK7bcVl_Sqmjfj-lBG65tmdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گریبان جنایتکاران را باید گرفت
رهبر انقلاب در پیامی به مناسبت هفته قوه قضاییه فرمودند:
🔹
یکی از مهمترین مسائل حقوقی و قضائی مربوط به همه‌‌ی ملّت ایران در این برهه‌ی زمانی، پیگیری و احقاق حقوق تضییع شده‌ی آنان در اثر جنایات مجرمان بین‌المللی و مستکبران و تجاوزکاران جهانی بخصوص در سالهای ۱۴۰۴ و ۱۴۰۵ می‌باشد. از خون شهدای مظلوم جنگ تحمیلی دوم و سوم تا صدمات و لطمات جسمی و روحی و مادّی و معنوی وارد شده به کشور عزیزمان و هر یک از آحاد ملّت مظلوم ایران در داخل و حتّی خارج از کشور؛ از کودک‌کشی‌ها و جنایات جنگی بی‌سابقه در میناب و لامِرد تا حمله به مراکز درمانی و خدماتی؛ از کشتار نوزادان چند روزه تا کهنسالان عزیز؛ و در رأس همه‌ی‌ آنها شهادت شخصیت بی‌بدیل، گوهر بی‌همتا و یگانه دوران، پیشوای مجاهد عظیم‌الشّأن اعلی‌الله‌مقامه‌الشریف، هر کدام پرونده‌ای از صدها و بلکه هزاران پرونده حقوقی مهم را تشکیل میدهد که در محاکم قضائی داخلی و بین‌المللی باید با جدّیت دنبال شود. آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند.
🔹
هفتصدوهشتادوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/664409" target="_blank">📅 23:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ddcb5c72.mp4?token=m7zKV5cI9z6YWN6QX7iURVRNJaLXSQa6svKpyWNwGer2pGJitSfiHF2n5iNUafl9eZkCto4F2YuyJb4cJ9eyEjhPg5-24xnfIRP-7QdAlhFRSJRxyb06FP0_GhirzAw_GDai1YpkAsSjcq4vLuzWZ_zTlJbmmfOjALSqy5JuOhXgTQYZFz1UXP8KJf3KYSYxlm8GwwXOkH6vMdv3u0eVSl2Nc6RM-p5WrOYY06W-cPgMcDYGSC2UIWb550yyKlFQ1eMBPVMrqRcgKvkwGUp2uLHOO19G5uRr-zGe4ZDHkXARuLV7x9Z2ovlIdPQ9DJeAGMbBDUa9K5zMVlLffSuwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ddcb5c72.mp4?token=m7zKV5cI9z6YWN6QX7iURVRNJaLXSQa6svKpyWNwGer2pGJitSfiHF2n5iNUafl9eZkCto4F2YuyJb4cJ9eyEjhPg5-24xnfIRP-7QdAlhFRSJRxyb06FP0_GhirzAw_GDai1YpkAsSjcq4vLuzWZ_zTlJbmmfOjALSqy5JuOhXgTQYZFz1UXP8KJf3KYSYxlm8GwwXOkH6vMdv3u0eVSl2Nc6RM-p5WrOYY06W-cPgMcDYGSC2UIWb550yyKlFQ1eMBPVMrqRcgKvkwGUp2uLHOO19G5uRr-zGe4ZDHkXARuLV7x9Z2ovlIdPQ9DJeAGMbBDUa9K5zMVlLffSuwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست اینستاگرام اکانت رسمی تیم ملی مصر با کنایه به شجاع خلیل‌زاده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/664408" target="_blank">📅 23:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7adc36fdf8.mp4?token=qI6SeVZ2XPc7kd4hqVaa2Yd7Nmd-MkZlEENHqeboYqffS0Dy7lSfBtf6d-Sh_E1ow-pLJENDqS0m3ZyiZMiFpq9fqF_tnTgt1eaTQko1kfcCK3PqwIXF5wv6ZH1X4iWEParVR0yyY39Dh3TdtLYJ_OhWCAWmoLzsx2E0OOJg1BaXuBV6vD0LAHitTkaTMvQT14EWw_4khDH5P6jOE40R026WRWzwggExaRPtjpQMY6wFzpaQ3kmEIkhApbaVgmq2GqcWp9vZcEpE0cyMCHr11cZFS8cvh3eoaw4r4lH_TP8Oitx87IB2iSd-w_xa9CZ_1QmCbamCe9TuOCGAFkgxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7adc36fdf8.mp4?token=qI6SeVZ2XPc7kd4hqVaa2Yd7Nmd-MkZlEENHqeboYqffS0Dy7lSfBtf6d-Sh_E1ow-pLJENDqS0m3ZyiZMiFpq9fqF_tnTgt1eaTQko1kfcCK3PqwIXF5wv6ZH1X4iWEParVR0yyY39Dh3TdtLYJ_OhWCAWmoLzsx2E0OOJg1BaXuBV6vD0LAHitTkaTMvQT14EWw_4khDH5P6jOE40R026WRWzwggExaRPtjpQMY6wFzpaQ3kmEIkhApbaVgmq2GqcWp9vZcEpE0cyMCHr11cZFS8cvh3eoaw4r4lH_TP8Oitx87IB2iSd-w_xa9CZ_1QmCbamCe9TuOCGAFkgxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابانی
: رو دستت تتو کردی "باباعلی" ، یعنی چی؟
🔹
نورافکن
:
اسم بابام رو زدم.
🔹
خیابانی
:
اسم بابات "بابا علیه"؟
🔹
نورافکن
:
نه آقا جواد، علیه.
🔹
خیابانی
:
آها ، پس اسم مامانت چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/664406" target="_blank">📅 23:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664404">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
خبرهای داغ را هر لحظه در وبسایت خبرفوری کلیک کنید
🔹
🔹
حمله دوباره آمریکا به ایران | ۱۰ نقطه در جنوب هدف قرار گرفت
👇
khabarfoori.com/fa/tiny/news-3226210
🔹
پشت‌پرده تهدید ترامپ | بلوف یا هشدار؛ آیا حمله بزرگی در راه است؟
👇
khabarfoori.com/fa/tiny/news-3226385
🔹
قالیباف به سیم آخر زد: بعضی‌ها هیچ غلطی برای انقلاب نکردند و اسم خود را گذاشته‌اند «سوپرانقلابی»!
👇
khabarfoori.com/fa/tiny/news-3226201
🔹
ماجرای رابطه جنسی آقای مدیر و منشی اش | دوربین مداربسته همه چیز را لو داد + عکس
👇
khabarfoori.com/fa/tiny/news-3226323
🔹
توقف مذاکرات واشنگتن و تهران در سوئیس| آکسیوس: آتش‌بس بین ایران و آمریکا می‌تواند به فنا برود
👇
khabarfoori.com/fa/tiny/news-3226441
🔹
صفحه ویژه اخبار پُربازدید ما را اینجا کلیک کنید
🔹
http://khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/664404" target="_blank">📅 23:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664403">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teNTufCG82mLraXif_Dq6uOOIEauRa3SXugMjCWyzjLZp9YRH74EfkDZzqptGgmEvD0aTNv130Ix7ANCTLDQ7TqP4eL0h24bLJePmLnhR_aAZtzN8ZeqPPExqCUUoGAqHv3m6vzgiE6FDhf07v19Pvd8OfRsrA1OnvleCJdKeZaykUb7WryLmtToJgObRyiPtAy8TmFJjYHwQR2OiHH8qULxBBggsL2oz_-P05FOTiPPeXDbstT50KjCIb2AfXZZd2cRitvBNMezZSPv8HXMDYq8EmRKPXvgbh7L7CRrvNsXwtCyfxarbHsA1a7LPymPDh1hpxy4yMwUw3CaVNXekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدام کشور شمار مرگ‌و‌میر از تولد پیشی گرفته است؟
🔹
در کشورهایی مانند ژاپن، وضعیت رشد جمعیت منفی است و شمار مرگ‌و‌ميرها دقیقاً
۲ برابر
تعداد تولدها ثبت شده است.
🔹
در چین، روسیه و اکثر کشورهای اروپایی، تعداد مرگ‌ومیر بیش از تولد است.
🔹
در نقطه مقابل، قاره آفریقا و کشورهایی نظیر اتیوپی رشد جمعیت شتابانی دارند، به طوری که آمار تولدها در اتیوپی بیش از
۵ برابر
مرگ‌و‌ميرها است.
@amarfact</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/664403" target="_blank">📅 23:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664402">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/664402" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/664402" target="_blank">📅 23:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664401">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/664401" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/664401" target="_blank">📅 23:41 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
