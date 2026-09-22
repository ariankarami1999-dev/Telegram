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
<img src="https://cdn4.telesco.pe/file/T1l153eRC7HUg4l-nE7IVlI36daV8HIJJOlY5_hlO8aQJs47VmMpbPKt2J0viwLWtRFy5cOe-pGz6zbby0qgiig468RKeNLHjdQc4kI8nQWpPmRMO2wZ6xd2K6dwoRbWuQnIoLtdhrREDrVqz3dP0AKawDnQCtd145smfL632J4ludbtgUrnnQJ3zlxZzfkEtwnGlGBNE35Q615Vp23YVJ8cabR4GSgDdjY_WgOgDY_gx9b0JvAFTZDnBYxK6Sda8bp-_dS0yaEI63A-4KycdYsAgQTcyhk3pO5X4ZUk_gHUfHBbEBusc_uwLe-Jd8qynQLv1viLlPzF5_cvQbU7gA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 454K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d07f32a5.mp4?token=gOG8xxoUgS76GKMj0uP6LZQtoEiXUmntk5QceoSDk_qGnC95k_mvMkdi6agUBjNxLYLq3M_caLvm9Xd3N8TbcQ4fP-wYn_i23pOBq-inipreMd5lMl0UDiAaqmelsoMhMfFw9ggOXyDE2NJ-JDYhn2EF1l1Q9sKliC5u-EIt6j8lQqUCXoDPO-PuV-n1IRFik2mzdig0shQzP4KWIOMlzFJvqSMi78lG7VKWYrxTKp_2fL7UZh18B0Tl9r7kxoELmSxXrIcoVMjKTJlF-4SBcP7lSj4bDNvUwoPBj3KGLKpf7Dbm0_rN5u4FQqGdsc9m5HWHcnB6N3ok869fQ2WURzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d07f32a5.mp4?token=gOG8xxoUgS76GKMj0uP6LZQtoEiXUmntk5QceoSDk_qGnC95k_mvMkdi6agUBjNxLYLq3M_caLvm9Xd3N8TbcQ4fP-wYn_i23pOBq-inipreMd5lMl0UDiAaqmelsoMhMfFw9ggOXyDE2NJ-JDYhn2EF1l1Q9sKliC5u-EIt6j8lQqUCXoDPO-PuV-n1IRFik2mzdig0shQzP4KWIOMlzFJvqSMi78lG7VKWYrxTKp_2fL7UZh18B0Tl9r7kxoELmSxXrIcoVMjKTJlF-4SBcP7lSj4bDNvUwoPBj3KGLKpf7Dbm0_rN5u4FQqGdsc9m5HWHcnB6N3ok869fQ2WURzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل : پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کردند که تصویری از نخستین آزمایش بمب هسته‌ای «واقعیه گرم» ایران را به نمایش می‌گذارد.
@WarRoom</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/23778" target="_blank">📅 13:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کیودو نیوز ژاپن به نقل از یک مقام ایرانی:
ایران اعلام کرده در صورتی که آمریکا گام‌هایی برای کاهش فشار نظامی بردارد، تهران می‌تواند
تنگه هرمز را ظرف ۷ روز بازگشایی کند
. به گفته این مقام، این پیشنهاد از طریق میانجی‌ها به آمریکا منتقل شده و ایران خواستار ازسرگیری مذاکرات برای دستیابی به پایان دائمی درگیری‌هاست. این گزارش تاکنون به‌طور مستقل از سوی ایران یا آمریکا تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/23777" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر دفاع اسرائیل، یسرائیل کاتس:
«با توجه به برخی نیت‌ها و گزارش‌های اطلاعاتی، به سازمان تروریستی حماس و حامیان آن، از ایران گرفته تا اردوغان، هشدار می‌دهم: اگر حتی یک سرباز یا غیرنظامی اسرائیلی ربوده شود، کل شهر غزه، همراه با خانه‌ها و برج‌های آن که محل فعالیت‌های تروریستی هستند، به سمت جنوب تخلیه خواهد شد و بیش از یک میلیون ساکن آن نیز منتقل خواهند شد. با شهر غزه همان‌گونه برخورد خواهد شد که با رفح، بیت‌حانون و ۷۰ درصد از مناطق غزه برخورد شد، تا زمانی که افراد ربوده‌شده بازگردانده شوند.»
@WarRoom</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/withyashar/23776" target="_blank">📅 12:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">@WarRoom
DorDor</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/23775" target="_blank">📅 12:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/23774" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/23773" target="_blank">📅 12:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st8uf8GJzaFR7u8bNnIYS8YuBKRNIv0wcaVFw_152eFiNNDPob-DwMRLZwyxvcYnglewCNzyJQu9aaCNHvvP7p9xEJNxQAHr3pn3tNryv3SjtVrtFq5jM5uX0dDpZfCfH4fvC8uyrTJC14jY5bteUfvWcHq5Zimwr26QoEptgvKgBZS7ENh2GU8dJwBrU6wCgstRl9h6p8HLLdBDmBiRMgdDOrINIdkG15qmrILlEC7mqWlfFIFWJb6ZxbnuYfD846Pko4eSIhhBQykjnoTpOgJuiS5O6058p_rZVQP6vdE-lW2Lj-ob5t1aX40SWIHIciSzZR_txC1b45qd9pApqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه اخلاقی : تو کار خدا دست نبرید هر چیزی حکمتی دارد
😂
😂
😂
😂
😂
@WarRoom</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/23772" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روز گذشته، گوشی یک پاکبان زحمتکش در مشهد به سـرقت رفت و یک هموطن با حضور در منزل این پاکبان، برای او یک گوشی موبایل تهیه کرده و به وی هدیه داد.  @WarRoom</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/23771" target="_blank">📅 11:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d0f93a54.mp4?token=SM2ILR2Kzqn4j52GFTlpjHjDzcbqIKapRhhUKBhAVksmEDVW9bSdIBPgt43DZSeziTDc4tIYgKf1ghCvHh_RQW23o1GYzvZ_s14c7xx_C9BmpGXsm25fScPZ4tpnYAlv1RdDT_VvwP-3jGnihXvKRjArIys33fdeb5Sn1U1mfL-Q2T_Ct262LU7AA1903axoUA3O3tS9ysDQQaoRQuie_wmf3V1yFqQN8Dsy7s8A78v8vNRABqj0PBrVo5jHHqeWAS-RF8p5FVZ6bJCBUIQ3_yhhgcNKfF7yr7lpX2SoldAJViVx0c7WEY8DtZjGOti2OHbauY9jiQW0jGydQcimMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d0f93a54.mp4?token=SM2ILR2Kzqn4j52GFTlpjHjDzcbqIKapRhhUKBhAVksmEDVW9bSdIBPgt43DZSeziTDc4tIYgKf1ghCvHh_RQW23o1GYzvZ_s14c7xx_C9BmpGXsm25fScPZ4tpnYAlv1RdDT_VvwP-3jGnihXvKRjArIys33fdeb5Sn1U1mfL-Q2T_Ct262LU7AA1903axoUA3O3tS9ysDQQaoRQuie_wmf3V1yFqQN8Dsy7s8A78v8vNRABqj0PBrVo5jHHqeWAS-RF8p5FVZ6bJCBUIQ3_yhhgcNKfF7yr7lpX2SoldAJViVx0c7WEY8DtZjGOti2OHbauY9jiQW0jGydQcimMDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز گذشته، گوشی یک پاکبان زحمتکش در مشهد به سـرقت رفت
و یک هموطن با حضور در منزل این پاکبان، برای او یک گوشی موبایل تهیه کرده و به وی هدیه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/23770" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آسوشیتدپرس:
شی جین‌پینگ در دیدار با ترامپ تلاش خواهد کرد آمریکا را به
توقف فروش تسلیحات به تایوان
متقاعد کند و به توافق مشترک سال ۱۹۸۲ میان واشنگتن و پکن استناد خواهد کرد
، تایوان و ایران
از موضوعات حساس روابط دو کشور هستند , باید دید آمریکا چه درخواستی دارد
@WarRoom</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/23769" target="_blank">📅 11:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رویترز: ایالات متحده قصد دارد یک پایگاه نظامی متعلق به دوران جنگ سرد را در منطقه نارزارسوآک در جنوب گرینلند مجدداً احیا کند و همچنین در مسترسویک در سواحل شرقی، یک حضور نظامی جدید ایجاد کند؛ این اقدام در چارچوب توافقی میان آمریکا، دانمارک و گرینلند انجام خواهد…</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/23768" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز:
گروه هفت از ایران خواست
تسلیح و حمایت از حوثی‌ها را متوقف کند
و حملات حوثی‌ها علیه عربستان و کشتی‌های غیرنظامی را محکوم کرد. G7 از حوثی‌ها نیز خواست حملات و تهدیدهای نظامی را متوقف کرده و به روند سیاسی بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/23767" target="_blank">📅 11:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d93d52cd3.mp4?token=UmQcdN6xkd13NBs18XRquh8EcWh8tMz3UIDeAgQhHOeXs_T2JCK_y8XlOqSAse5rpOT_Oh_-BsFXoLwnbFLZ109SVRLUWHXKBt2KjiQ495IPZ_PwH46zyj3AXvC-LZ05FzLSbm_t2TlRsgDMoAp26v7-Ngat31qal1zZyteJ8NnvGG7MlbXun0ELHPHLsrjjIacLWnFJ1f26pI1pcz0CLkAbHHqFt42pHvry7QpE6m5REyC5PFjs4xnEGhtkYcRBnm_fmc3U5fKY8fKH7x_TxUopM4d9F3dS5WcO_e1-eJvXvyp_5Ymk10sygI5jTn1FOEbqNSTvq70CQ_rfWPJwMSzWwITsiRWFKNi0pZarUyUdkOe5G3t_uSxPVHOR3Nsufjypr1QVewEidGJ66mWL8s6Lqt990QdvWQbi0b0jtWLmCu8hc6EkzZsnRpn6LGYW4UAQToCHhat5sPaAiVjIXViR8O8PWc7wBUzKk9eufnZE55SYj9tLqMLZ2VDQEPBneb8ME0WwDr02THbdusY9-SY6PdPnf9umaN6xI8hF9tGO_LOdqh0qNSDBcM5HLrVXCLfZ1ryAOrEMdWwkFptgvRpq9zJzOeSt9sh1U1qkRkgH39XKmrrfHaTIA2yuNkhl1dvX4qySVRf7gN3wCo9s133GDJ5vfOjIEt6QtVgsRUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d93d52cd3.mp4?token=UmQcdN6xkd13NBs18XRquh8EcWh8tMz3UIDeAgQhHOeXs_T2JCK_y8XlOqSAse5rpOT_Oh_-BsFXoLwnbFLZ109SVRLUWHXKBt2KjiQ495IPZ_PwH46zyj3AXvC-LZ05FzLSbm_t2TlRsgDMoAp26v7-Ngat31qal1zZyteJ8NnvGG7MlbXun0ELHPHLsrjjIacLWnFJ1f26pI1pcz0CLkAbHHqFt42pHvry7QpE6m5REyC5PFjs4xnEGhtkYcRBnm_fmc3U5fKY8fKH7x_TxUopM4d9F3dS5WcO_e1-eJvXvyp_5Ymk10sygI5jTn1FOEbqNSTvq70CQ_rfWPJwMSzWwITsiRWFKNi0pZarUyUdkOe5G3t_uSxPVHOR3Nsufjypr1QVewEidGJ66mWL8s6Lqt990QdvWQbi0b0jtWLmCu8hc6EkzZsnRpn6LGYW4UAQToCHhat5sPaAiVjIXViR8O8PWc7wBUzKk9eufnZE55SYj9tLqMLZ2VDQEPBneb8ME0WwDr02THbdusY9-SY6PdPnf9umaN6xI8hF9tGO_LOdqh0qNSDBcM5HLrVXCLfZ1ryAOrEMdWwkFptgvRpq9zJzOeSt9sh1U1qkRkgH39XKmrrfHaTIA2yuNkhl1dvX4qySVRf7gN3wCo9s133GDJ5vfOjIEt6QtVgsRUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خزعلی: شاه به قم آمد و به همه آخوندها گفت دوره مُفخوری گذشته است. هزار و چهارصد سال است که فکر شما تکان نخورده
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/23766" target="_blank">📅 10:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1192bf611.mp4?token=qmgejNvprTkpPrSeBwjVnL9LzGjYN41Oe3WVGUQiI9bG9OydnQ14S_JHZwXRD2axTJjLR-ogrmAd-xPSbzfdPNXNpSXSs90JnKz5cIj6wwJr_jIUuE6FKNq14j0ssEF34CdGCvrB7wIGKdFP8aQlallgqq4fskcvUA63bla2mfZuv0uIz4YXuOF8ds4L-bttnY3Vzhe9dSXbJ1x8kNhiPcnnxgX9tmkxp09qxOh6RAm_Ghf19ecaD4gCT82O4t1DnyZlMekKEZ2WNAi1ANGBJbV21I153z6qBaLAxrtWeDdy2x5AyNE-4IufTQOA5YZ9BIYUsubboNm966lco3kcmG9L9hTkJuY54-kqFVkfnkoh6gX4tomZKG_FhlXIOeZLoR8cAePU-XdwyHnIdjCZK1debOQkL1DqUMx9naRTfVuS1sKJ5Nua78gQZ9AXy_3FuRjy-5t280XGSD0HvUxCuO9EsYXfCjdc8tbdJNFQDD8owo_a5zZf3RypZ6cXGTVbpM3EQnnrFZEim7zL-t3rqxGoiSEt9WJ4ij-BvIeLkZwg5hNRJyL_cZ1Wnxqi4F9AeW03DahI5NRkQS7WB7_lQnMJHj3uqduQq0Mb2c1sg0CTHB4pWumWZtya8M-iyVddzP4lP4j7CKTsJ6rNXdF4KK4GsSr7eyNl5vjNvwgiPJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1192bf611.mp4?token=qmgejNvprTkpPrSeBwjVnL9LzGjYN41Oe3WVGUQiI9bG9OydnQ14S_JHZwXRD2axTJjLR-ogrmAd-xPSbzfdPNXNpSXSs90JnKz5cIj6wwJr_jIUuE6FKNq14j0ssEF34CdGCvrB7wIGKdFP8aQlallgqq4fskcvUA63bla2mfZuv0uIz4YXuOF8ds4L-bttnY3Vzhe9dSXbJ1x8kNhiPcnnxgX9tmkxp09qxOh6RAm_Ghf19ecaD4gCT82O4t1DnyZlMekKEZ2WNAi1ANGBJbV21I153z6qBaLAxrtWeDdy2x5AyNE-4IufTQOA5YZ9BIYUsubboNm966lco3kcmG9L9hTkJuY54-kqFVkfnkoh6gX4tomZKG_FhlXIOeZLoR8cAePU-XdwyHnIdjCZK1debOQkL1DqUMx9naRTfVuS1sKJ5Nua78gQZ9AXy_3FuRjy-5t280XGSD0HvUxCuO9EsYXfCjdc8tbdJNFQDD8owo_a5zZf3RypZ6cXGTVbpM3EQnnrFZEim7zL-t3rqxGoiSEt9WJ4ij-BvIeLkZwg5hNRJyL_cZ1Wnxqi4F9AeW03DahI5NRkQS7WB7_lQnMJHj3uqduQq0Mb2c1sg0CTHB4pWumWZtya8M-iyVddzP4lP4j7CKTsJ6rNXdF4KK4GsSr7eyNl5vjNvwgiPJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چک سنگین شاهزاده به صورت موشتبی خامنه‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/23765" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز:
ترامپ امروز در نیویورک با تعداد زیادی از رهبران جهان دیدار خواهد کرد و
ایران، اوکراین و یمن
از محورهای اصلی برنامه او هستند. همچنین قرار است با رهبران کشورهای خلیج فارس درباره حملات حوثی‌ها جلسه داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/23764" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز:
در یک تحول سیاسی داخلی روسیه،
رمضان قدیروف
بار دیگر به عنوان رهبر جمهوری چچن انتخاب شد؛ نتایج رسمی تقریباً
۱۰۰ درصد آرا
را به او اختصاص داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/23763" target="_blank">📅 09:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز:
ایالات متحده قصد دارد یک پایگاه نظامی متعلق به دوران جنگ سرد را در منطقه
نارزارسوآک
در جنوب گرینلند مجدداً احیا کند و همچنین در
مسترسویک
در سواحل شرقی، یک حضور نظامی جدید ایجاد کند؛ این اقدام در چارچوب توافقی میان آمریکا، دانمارک و گرینلند انجام خواهد شد که قرار است در نیویورک امضا شود. نارزارسوآک در گذشته محل پایگاه نظامی آمریکا با نام
بلویی وست وان (Bluie West One)
بود که در دهه ۱۹۵۰ تعطیل شد. منطقه مسترسویک نیز در حال حاضر توسط واحد ویژه دانمارکی
سیریوس (Sirius Dog Sled Patrol)
مورد استفاده قرار می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/23762" target="_blank">📅 09:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آسوشیتدپرس:
بریتانیا اعلام کرد به درخواست عربستان، برای چند هفته
سوخت‌رسانی هوایی به جنگنده‌های سعودی
انجام خواهد داد. این نخستین حمایت نظامی مستقیم بریتانیا از عربستان در درگیری جدید با حوثی‌هاست و لندن آن را اقدامی دفاعی عنوان کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/23761" target="_blank">📅 09:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پزشکیان : دشمن در تلاش است تا تمام راه‌های هوایی‌ و زمینی را بر ایران ببندد تا ما را مجبور به تسلیم کند.
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/23760" target="_blank">📅 09:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الجزیره: نیروهای اسرائیلی به شهر الرفید در حومه القنیطره، در جنوب غربی سوریه، نفوذ کرده و اکنون تعدادی از خانه‌ها را تفتیش می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/23759" target="_blank">📅 09:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fffc1acfa.mp4?token=ARbeTyMWXFOAAXc1iCwMB2-NsCUOcLKU1kNOGOwPnUSv2U2K95tBCLqxYqyt6U68U0AH2v8xBJtbHbbvZbFf5taGr_SIuWhvXcdIC-fxXf0Mk8v7n2JqgfTAMHD3LTLl3s74w8OiNkDCkCfUdvP8_6IMbUCXzKNr3iABoqSyywIrHz1tQR92NSWfefzUSXf5yTgCVULFGSCSrhx0779da9T2V_IeFqAEv7xG3LIX7jlxF6kIVGsmJMWj3K00LCERTelq-ZRYsMeAh_8STe2JRsRtrV8bR4EKoFu8lwXq-Tv9nCs4TAKKfzkteHFr6stbOOB55ckP70PNs17LSHuO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fffc1acfa.mp4?token=ARbeTyMWXFOAAXc1iCwMB2-NsCUOcLKU1kNOGOwPnUSv2U2K95tBCLqxYqyt6U68U0AH2v8xBJtbHbbvZbFf5taGr_SIuWhvXcdIC-fxXf0Mk8v7n2JqgfTAMHD3LTLl3s74w8OiNkDCkCfUdvP8_6IMbUCXzKNr3iABoqSyywIrHz1tQR92NSWfefzUSXf5yTgCVULFGSCSrhx0779da9T2V_IeFqAEv7xG3LIX7jlxF6kIVGsmJMWj3K00LCERTelq-ZRYsMeAh_8STe2JRsRtrV8bR4EKoFu8lwXq-Tv9nCs4TAKKfzkteHFr6stbOOB55ckP70PNs17LSHuO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس:
«فکر می‌کنم بسیاری از آمریکایی‌ها می‌پرسند:
چرا قیمت بنزین این‌قدر بالاست؟
دلیلش این است که
ایرانی‌ها همچنان به سمت کشتی‌های تجاری موشک و پهپاد شلیک می‌کنند
.
این موضوع، اساساً
به ایرانی‌ها مربوط می‌شود
.»
@WarRoom</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/23758" target="_blank">📅 09:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJJXVSNRzYUurV2hHBMWb21vetPaLUe1ROy2EqHE7G9ubgFO-YLeIT2kEsPXhaCMRJIPeCFnM3lMo58vuKlndwDktRHslhbP35KkeZDE9ULM0nc4aU-n81CEfUEk68cXaQyU7Oi5gMcGW8Ry75JkSTasUpCFUd2dCtZksTH9UkFqOTUX5mKOO3nK8-gHDU95uT-osPnV9K-2PBa2osCqxGQxfkBpunZqOlt8FoQHKxN6CvFPiPxETPAg3Be48_R7Ovhydqb74jFhgMz4w_PciAYVGClnH9eAX0uQty_xbbuSK5ij-v2JWL0n3wrPDlAscKR-t-l5BnSDRj365T4YjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان راهی نیویورک شد ، خلیج فارس همچنان در کنترل انبوهی از هواپیما‌ها و پهپادهای آمریکایی
@WarRoom</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/23757" target="_blank">📅 08:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e96acdbd.mp4?token=MWeDEY60H8drwqDUwf4P5tbXpAZ9IaZGbxU_Q1jkG7FTVZpvfAXQPYaYCF2kNjVaF1O2lkM45XgTeuQLoVwseStY105e95HBs_dk3chXtdxIb9MWitOjs0y8YqNBlFeUdBQAduugxd-RaEevLS9bf1uLRf2PaTCZeDWgWFI5wjxSaTNg-e2H6w3AufvxpcjgovWmnJ3Y_eGaA1lr_XCFYHGx6m1BJ1eTOT-NimBF4X4iaABy0nF_YcTOTuTmib9jNLujFoHKzjxHLRq47nT2NoZckFoMaXgz8do_0D8sLAzyJN95okPwprgZHzIfWNGF0TTs7GhS5tRzRGTAyfaRxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e96acdbd.mp4?token=MWeDEY60H8drwqDUwf4P5tbXpAZ9IaZGbxU_Q1jkG7FTVZpvfAXQPYaYCF2kNjVaF1O2lkM45XgTeuQLoVwseStY105e95HBs_dk3chXtdxIb9MWitOjs0y8YqNBlFeUdBQAduugxd-RaEevLS9bf1uLRf2PaTCZeDWgWFI5wjxSaTNg-e2H6w3AufvxpcjgovWmnJ3Y_eGaA1lr_XCFYHGx6m1BJ1eTOT-NimBF4X4iaABy0nF_YcTOTuTmib9jNLujFoHKzjxHLRq47nT2NoZckFoMaXgz8do_0D8sLAzyJN95okPwprgZHzIfWNGF0TTs7GhS5tRzRGTAyfaRxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در‌نیویورک
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/23756" target="_blank">📅 08:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Geu8Rz8OskgLK4jSTmoVKtAp38GMUFt8fC1Tkk2rCQb39NIfutbxYAYe4pT7Y-KaCYDa2tEku5mjS1XCmmjiXI8baE1OBGNZp0Av6RroqJ9oB1_4BwHOC3SopfXxPayF5ZLxQfpq8Wa093BkI0Me9qtZY_g3ZsrlccHjmXqa3OK2LmTcFdH2JXU0Y2JJ9TlZrfoggrbESFdxblTpvVuAbgqpEXWqkNKeCRU16ALQdcY4qYGHVVP8vHK8J7Ujk97TGl1DHzqXk9r2VTZr1AKbWFAZJESzZ6i83ybqgWhdx_JmQpCEYoAlk-oiG_20wikdCmTKmqkrqHx-oCVTeEkAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ شبکه تلویزیونی خود را راه اندازی کرد
کاخ سفید : «ترامپ تی‌وی» (Trump TV) هم‌اکنون در حال پخش است؛ برنامه‌ای ۲۴ ساعته و به‌روزرسانی‌شده به‌صورت آنی که گزیده‌ای از بهترین لحظات گذشته، اطلاعیه‌ها و جدیدترین و مهم‌ترین اخبار دولت را یک‌جا گرد هم آورده است.
همه لحظات مهم قبلاً از تلویزیون پخش نشده‌اند، اما حالا این امکان فراهم شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/23755" target="_blank">📅 07:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏جی‌دی ونس، معاون ترامپ، در گفت‌وگو با نیوزمکس: ما تاسیسات هسته‌ای جمهوری اسلامی، به‌طور مشخص سه تاسیسات هسته‌ای را با یک حمله تاکتیکی فوق‌العاده نابود کردیم. علاوه بر این باید اطمینان حاصل کنیم آنها قادر به بازسازی برنامه هسته‌ای خود نیستند. @WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/23754" target="_blank">📅 07:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏جی‌دی ونس، معاون ترامپ، در گفت‌وگو با نیوزمکس: ما تاسیسات هسته‌ای جمهوری اسلامی، به‌طور مشخص سه تاسیسات هسته‌ای را با یک حمله تاکتیکی فوق‌العاده نابود کردیم. علاوه بر این باید اطمینان حاصل کنیم آنها قادر به بازسازی برنامه هسته‌ای خود نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23753" target="_blank">📅 07:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «این را به صورت زنده در تلویزیون‌های سراسر جهان به حاکمان ایران اعلام می‌کنم؛ ما می‌دانیم حساب‌های شما در جزایر ویرجین بریتانیا و شرکت‌های واسطه کجا قرار دارند. خانه‌های چندصد میلیون دلاری شما در سراسر جهان را می‌شناسیم و قصد داریم همه این دارایی‌ها را از شما بگیریم و به مردم ایران بدهیم»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23752" target="_blank">📅 01:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش ها از برگزاری جلسه اضطراری فرماندهان نظامی ارشد کشور های عضو ناتو.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23751" target="_blank">📅 01:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شبکه ۱۲ اسرائیل در مورد یک مسئول امنیتی ارشد اسرائیل:اسرائیل برای یک تنش احتمالی با ایران آماده‌سازی می‌کند.
وضعیت حساس و قابل تغییر است، و در صورت شکست مذاکرات بین واشنگتن و تهران، ممکن است تنش‌ها به سرعت افزایش یابد و اوضاع از کنترل خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23750" target="_blank">📅 01:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0c485c05.mp4?token=L76gwMQr6x3eGAU8Ft1LyBjE3oyWKP8IyuWpBhl-tfRkHZJ5NoWZpQApjyLqagI0LamlxNtZFTbHDcw4CZwMQLHqsGWezJJDTL7lfdXCLeQ_nd7flpo-qw2cHEI5LgdIc8z6OxSMuH_41c3qKMo-lV6YAYIlS3nfAx0HsOf_F2Bi1lOBtt-BwdL883tFs0SflyYCTeI6C06Sby0JbldRsvQI2uaNdwmP0IdFmlMc1AIEZbqBxafyyKYuxmCk9AAgkCvo3_2FdliSPnagYDG2uk6ZtW7Z-uf2FF37bKm-NMI32P3sREFpeA9hqBKTIn1vG_nPtKWvbQChKUPNWLbeWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0c485c05.mp4?token=L76gwMQr6x3eGAU8Ft1LyBjE3oyWKP8IyuWpBhl-tfRkHZJ5NoWZpQApjyLqagI0LamlxNtZFTbHDcw4CZwMQLHqsGWezJJDTL7lfdXCLeQ_nd7flpo-qw2cHEI5LgdIc8z6OxSMuH_41c3qKMo-lV6YAYIlS3nfAx0HsOf_F2Bi1lOBtt-BwdL883tFs0SflyYCTeI6C06Sby0JbldRsvQI2uaNdwmP0IdFmlMc1AIEZbqBxafyyKYuxmCk9AAgkCvo3_2FdliSPnagYDG2uk6ZtW7Z-uf2FF37bKm-NMI32P3sREFpeA9hqBKTIn1vG_nPtKWvbQChKUPNWLbeWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها به سلاح هسته‌ای دست نخواهند یافت؛ بگذارید همین‌طور بگویم.
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکرد آن‌ها بسیار ضعیف است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23749" target="_blank">📅 01:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ7mED18b0E2drjNdDbfD8XrhjJsTo6zW-_ondKBelIy_OqmfYn3586jbnIseyvdYW3I2tRx2xkcj8inHU7alNNB0AP0rJIjM20Uy3k03vUdnJqPcl4hEOyyV7VH2oloWeWT2YPhZ04SOVuUyB6EcJtdRgNdI6y5N_SujYDFcdu7-ZI22UjaPKU7Y6-s5cPIeC_VAMpzkh0EHjUTnc-L_pEmQtp6ox4_tgG4Aw6987_FJ7JJH7PDttaaMDW7AJAWmLdnwoPToW2Pf_yZjp52fPcn1MzFOaU5zdGXadnglNropsB1P8wd8PVzRcV8O3r2CsNRVyUOJ7C-NhaVImwjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصاحبه آیت‌الله خمینی و ابراهیم یزدی با مجله پورنوگرافی پنت‌هاوس، در جلد ۱۰، شماره ۱۲، سال ۱۹۷۹ ، روی جلد هم عکس مدل دیان ویدر است. هماهنگی مصاحبه‌ها را قطب‌زاده که عامل کاگ‌ب بود، انجام می‌داد. همان‌طور که می‌بینیم، این رژیم از ابتدا بر همین اساس بنا شده بود. ابراهیم یزدی بعدها در آثارش توضیح داد که نه، ما با نیویورک تایمز مصاحبه کرده بودیم، ولی پنت‌هاوس آن را پخش کرد تا قضیه را ماست‌مالی کند. خلاصه محتوای مصاحبه، محور صحبت‌ها بیشتر در مورد انقلاب ۱۳۵۷، شاه، آمریکا، حکومت اسلامی و آینده ایران بود.که واقعا آینده ایران مانند پورن شد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23748" target="_blank">📅 00:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فاکس‌نیوز: ترامپ، در آستانه
هفته ای سرنوشت ساز
و دیدار با رهبران کشورهای حاشیه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، در حال بررسی اقدام بعدی خود درباره ایران است.
ترامپ به فاکس‌نیوز گفت: «من در حال تصمیم‌گیری هستم. سؤال من این است که اگر و زمانی که تصمیم بگیرم، آیا کل کشور را منفجر کنم؟ آنها بهتر است رفتارشان را درست کنند.»
او در حال بررسی گزینه‌هایی از جمله اقدام نظامی، ادامه فشار اقتصادی یا تلاش دوباره برای توافق با ایران است.
ترامپ به فاکس نیوز گفت:  برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در این هفته آمادگی دارد، اما در حال حاضر هیچ دیداری میان دو رهبر در برنامه رسمی قرار ندارد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23747" target="_blank">📅 00:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏منابع محلی نزدیک مرز ایران و پاکستان:  تعداد زیادی از افراد مسلح بلوچ وارد منطقه رادیگ در مند، شهرستان کیچ، بلوچستان شده‌اند و طبق گزارش‌ها، در چندین نقطه ایست بازرسی ایجاد کرده‌اند.
‏گزارش‌ها همچنین حاکی از آن است که یک اردوگاه نیروهای امنیتی پاکستان مورد حمله قرار گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23746" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک‌تایمز: علی الزیدی، نخست‌وزیر عراق، متعهد شده است گروه‌های شبه‌نظامی مورد حمایت ایران را تا ژوئن ۲۰۲۷ خلع سلاح کند. طبق این طرح، ابتدا یک دوره ۹۰ روزه بدون حمله میان شبه‌نظامیان و نیروهای آمریکایی در نظر گرفته شده و سپس تحویل سلاح‌ها تا ۳۰ ژوئن ۲۰۲۷ انجام خواهد شد. شبه‌نظامیان خواستار تمدید این مهلت تا پایان ۲۰۲۷ هستند. الزیدی همچنین گفت عراق به‌دلیل بسته‌شدن تنگه هرمز حدود ۶۰ میلیارد دلار و ۶۰ درصد درآمد ماهانه صادرات خود را از دست داده و ایران اجازه عبور نفتکش‌های عراقی از تنگه را نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23745" target="_blank">📅 00:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">BTC 84,100$  @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23744" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیروهای مسلح لتونی کشور اروپایی: آماده باشید! به اطلاع می‌رسانیم که احتمال وجود تهدیدی در فضای هوایی لتونی وجود دارد.
حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است  فعال شد.جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23743" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز گزارش داد که جان راتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، اوایل امروز، بدون هماهنگی قبلی، در جریان سوخت‌گیری هواپیماهایشان در فرودگاه شانون ایرلند، با زلنسکی، رئیس جمهور اوکراین، دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23742" target="_blank">📅 23:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تحلیلگر آمریکایی : ترامپ با یه مصاحبه و جمله احتمال توافق، قیمت نفت رو از ۱۰۷ به ۹۷ دلار رسوند. عربستان هم به دنبال بازگشایی خط لوله شرق-غربه و با این تفاسیر دیگه نیازی به تنگه هرمز نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23741" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چپقچی وزیر امور خارجه برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23740" target="_blank">📅 23:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23739">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیروهای دولتی یمن: تلاش گروه حوثی برای نفوذ در جبهه "العنین" در منطقه "جبل حبشی" در غرب شهر تعز را خنثی کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23739" target="_blank">📅 23:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23738" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23737" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.g</strong></div>
<div class="tg-text">یاشار داداش انشالله اگه ما تو این انقلاب شیرو خورشید پیروز شدیم
شما ایران میای؟
تکلیف چنل چی میشه؟</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23736" target="_blank">📅 23:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">از گزارشها اینگونه بیان میشود که از حدود یک ساعت پیش سامانه میخک واردات خودرو را بسته
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23735" target="_blank">📅 22:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ماهان‌ایر: از امروز ۲۱ سپتامبر
پروازهای خود به استانبول، آنکارا و گرجستان را متوقف کرده است؛ مسیر تهران–مسقط نیز از ۱۷ سپتامبر متوقف شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23734" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترکیش ایرلاینز: طبق اعلام یک نماینده این شرکت،
تمام پروازهای ترکیش ایرلاینز به ایران فعلاً تا(نوروز) مارس ۲۰۲۷ برنامه‌ریزی نشده‌اند
و ادامه آنها پس از آن تاریخ نیز تضمین نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23733" target="_blank">📅 22:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الجزیره: در چند ساعت اخیر گزارش شد یک
کشتی دوم
نیز در تنگه هرمز بر اثر برخورد بقایای یک پرتابه ناشناس آسیب دیده است. هیچ‌کس زخمی نشده و کشتی به مسیر خود ادامه داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23732" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : باز هم برخی ادمین‌های بی‌اطلاع تلگرام اشتباه کردند و نوشتند «هلیکوپتر جدید مارتین وان»! اولاً نام آن Marine One (مارین وان) است. مارین وان اسم یک مدل هلیکوپتر نیست؛ به هر هلیکوپتری از تفنگداران دریایی آمریکا که رئیس‌جمهور را حمل کند Marine…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23731" target="_blank">📅 22:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای نخستین بار از هلی‌پورت تازه‌ساخته‌شده در محوطه جنوبی کاخ سفید استفاده کرد و با بالگرد ریاست‌جمهوری «مِرین وان» از این محل به مقصد خود رفت. ترامپ در پیامی ضمن تشکر از جیم تایکلت، مدیرعامل لاکهید مارتین، گفت این شرکت کمک…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23730" target="_blank">📅 22:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df0feca14.mp4?token=mXYJs3ZxI-_Cf14GvPtipdn1p3yag35zSqUvfL2kJwWt3gwN-jbTsdry8WeeEk3wBuolgoPMNnoUezLftx6XZ1GLDr8CLGFRmmMB9yQMakeMCmCCAMUVe9_MVRvQRrEfSJ2M8wE1pMGxNtX37NY8APn0-bM8YNnh425dvuUFN0DmozxM4UV7hyeSUzMqF4veRcIMzVooehYT-ocYzgifFgCUXO1IOdUHYcKlM67pmbFzJ1OwUiwFZkv_3EupWK_-_7XCspJFPCqF58HT_GbQfz5UEN4BWHaSstSMnSTa-BzDwZmk8MINN1WYa-0IYyJfuwBYSowm_TG61BRbNGYgPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df0feca14.mp4?token=mXYJs3ZxI-_Cf14GvPtipdn1p3yag35zSqUvfL2kJwWt3gwN-jbTsdry8WeeEk3wBuolgoPMNnoUezLftx6XZ1GLDr8CLGFRmmMB9yQMakeMCmCCAMUVe9_MVRvQRrEfSJ2M8wE1pMGxNtX37NY8APn0-bM8YNnh425dvuUFN0DmozxM4UV7hyeSUzMqF4veRcIMzVooehYT-ocYzgifFgCUXO1IOdUHYcKlM67pmbFzJ1OwUiwFZkv_3EupWK_-_7XCspJFPCqF58HT_GbQfz5UEN4BWHaSstSMnSTa-BzDwZmk8MINN1WYa-0IYyJfuwBYSowm_TG61BRbNGYgPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای نخستین بار از هلی‌پورت تازه‌ساخته‌شده در محوطه جنوبی کاخ سفید استفاده کرد و با بالگرد ریاست‌جمهوری «مِرین وان» از این محل به مقصد خود رفت. ترامپ در پیامی ضمن تشکر از جیم تایکلت، مدیرعامل لاکهید مارتین، گفت این شرکت کمک ارزشمندی برای ساخت هلی‌پورت انجام داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23729" target="_blank">📅 21:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تنگه صدای علی لاریجانی میاد
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23728" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3SrkxSDcLXTDIcNvKA6r1-7FpmJEss3WEwuoOvoXySl-uhvWw7jr9vX1hcF2EtpWv3oMO8z_pnoo9XSgxWuwGFzupVpF_j15ftF89l17-DyK0zfSSZ2HHOfrjgd-_swWNjKA_9Ae7-uXzDB-iicSGz3NoYzJhM8QwFntwQwVxPmm7xjlpNtczRs-ecZ3Y477NJgWpFb8pko_XjoUN6GVaTtrt6c9aUArz0-NQd2k598oMyp-xDR-et8R8__-SlYXEDp4giNvysehhI4JLdYab4EhROgElM1yxXMREG_zkl5rZIeAkkFi6MBD3YXa9LMVe0kVs1uaGddNR96pHWVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرقت موبایل یک پاکبان در مشهد @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23727" target="_blank">📅 21:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرنگار الجزیره: ارتش اسرائیل عملیات سوم تخریب را در مناطق تحت کنترل خود در جنوب شهر خان یونس در جنوب نوار غزه انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23726" target="_blank">📅 21:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23725">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بلومبرگ گزارش داد بریتانیا در حال بررسی گسترش حمایت نظامی از عربستان سعودی است؛ ریاض از لندن برای مقابله با تشدید حملات حوثی‌ها و حفاظت از خاک و زیرساخت‌های نفتی خود درخواست کمک کرده است. عربستان همچنین خواستار حمایت عملیاتی و دفاعی بریتانیا شده
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23725" target="_blank">📅 21:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بلومبرگ گزارش داد ایران به یک محموله دیگر گاز طبیعی مایع‌شده (LNG) قطر اجازه عبور از تنگه هرمز به مقصد پاکستان را داده است. بر اساس این گزارش، یک محموله دیگر LNG قطر نیز در همین ماه با مجوز ایران از تنگه هرمز عبور کرده و به پاکستان رسیده بود. کشتی حامل محموله جدید قرار است فردا به پایانه واردات LNG پاکستان برسد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23724" target="_blank">📅 21:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کان: منبعی در شورای رهبری ریاست‌جمهوری یمن گفت تماس تلفنی ترامپ با رشاد العلیمی، رئیس این شورا، چیزی فراتر از ابراز حمایت احساسی از سوی رئیس‌جمهور آمریکا نبوده است
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23723" target="_blank">📅 21:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0a6a7ba3.mp4?token=eGgazauh7mVFHkNBgNuL_Wd8JGKfNucCS53Tbz0lyerW5YlB1pHCfM8j7jVISFCjk-zMGMJRWyq5lyGP7pea9irsRUsXH-3euVuSVz1nG26X8QQcc001QQGF3JG75o84lLn2wMYRySFpgI3lgI78LhPccZwp2V6wUI1PMjqsAREbAfI_8KxSRNBYN9mBikdggEtAncNiA7m-HtzSQ4-N1RxPZ0jEw-ZUHEoCDkGb7nyi2PB1UzpuvRotLyea9wzu7c-FO-D9U3OLMRJdoDbvlBFQCMwbfHqJJASYKAazRaordXnd83fz4I7otLWEuW2Chkgn4I9oaSGTNgEQg6ApFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0a6a7ba3.mp4?token=eGgazauh7mVFHkNBgNuL_Wd8JGKfNucCS53Tbz0lyerW5YlB1pHCfM8j7jVISFCjk-zMGMJRWyq5lyGP7pea9irsRUsXH-3euVuSVz1nG26X8QQcc001QQGF3JG75o84lLn2wMYRySFpgI3lgI78LhPccZwp2V6wUI1PMjqsAREbAfI_8KxSRNBYN9mBikdggEtAncNiA7m-HtzSQ4-N1RxPZ0jEw-ZUHEoCDkGb7nyi2PB1UzpuvRotLyea9wzu7c-FO-D9U3OLMRJdoDbvlBFQCMwbfHqJJASYKAazRaordXnd83fz4I7otLWEuW2Chkgn4I9oaSGTNgEQg6ApFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی وینس، معاون رئیس‌جمهور:
امسال در ماه نوامبر(آبان)، سرنوشت‌ساز خواهد بود. یا باید در برابر این دیوانگی بایستید، یا با آن همراه شوید.
و ما برای ایستادگی در برابر آن و مبارزه با آن اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23722" target="_blank">📅 21:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj-5yqnPqdmvK4P3NYPjQGhdUmRa5qqIBRf5CfP5S8hW9nBGcrvjQuHZ9PSTQCzK7VUlZbU8OqGO0ga8ray1QUmOps9fchn7zu2XDxjI1fbFsNcnDOeBaQv9D3eKEUob2h9p5jT4006JnSHFcFMeeC4AO5UQFPFdmumdIhAibthUD2tEl6YmQhQYqGjKR304YPRgAfFAHBTsabc1cXbspEOBYaLAeKpmh0FPO5E_0yJMc2m6yM2MBzbRcdYYA-IejrGn4JNGey0xRPDjR13bBBRA4JkFn2wq8dQ9163fMCZdhcWryImskCe3NvBnSSvdzv8zkhflN38CGlh7HlLHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت به زیر ۱۰۰$ آمد و حملات موشکی جمهوری اسلامی به کشتی ها تأثیر خود را از دست میدهند. قیمت در این لحظه ۹۹.۵$
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23721" target="_blank">📅 21:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23720">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ما ایران را
بیش از هر زمان دیگری تحت فشار قرار داده‌ایم
. حدود یک ماه پیش پنج اختیار تحریمی جدید علیه حکومت ایران به دست آوردیم که حوزه‌های
هواپیمایی، دریانوردی، رمزارز و طلا
را شامل می‌شود. از
۲۳ سپتامبر
تمام خطوط هوایی ایران در سراسر جهان تحت فشار قرار خواهند گرفت؛ به این معنا که در صورت فرود هواپیماهای ایرانی، ارائه
سوخت، خدمات فرودگاهی یا فروش بلیت
می‌تواند باعث شود ارائه‌دهنده خدمات از سیستم مالی و دلاری آمریکا کنار گذاشته شود. او گفت آمریکا شبکه‌های تسهیل‌کننده انتقال پول به ایران را شناسایی کرده و در حال متوقف کردن فعالیت آنهاست. تاکنون
سه بانک
نیز هدف قرار گرفته‌اند؛ از جمله
شعبه دبی دومین بانک بزرگ مصر
که به گفته او بیش از
۱.۸ میلیارد دلار
به حکومت ایران منتقل کرده، یک بانک ترکیه‌ای و شعبه‌های خارجی
دومین بانک بزرگ روسیه
. این شعبه‌ها تعطیل خواهند شد. درباره چین نیز وزیر خزانه‌داری آمریکا گفت واشنگتن با کشورهای مختلف در حال انجام
گفت‌وگوهای محرمانه و پشت‌صحنه
است و در بسیاری موارد این روش را بهتر از رویارویی علنی می‌داند.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23720" target="_blank">📅 20:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز: حوثی‌ها امروز تلاش کرده‌اند ارتفاعات راهبردی یمن را تصرف کنند تا ارتباط مناطق ساحلی دریای سرخ با بخش‌های باقی‌مانده تحت کنترل دولت یمن را قطع کنند. این تحرکات همزمان با گزارش‌ها درباره خودداری ترامپ از حمله مستقیم به حوثی‌هاست.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23719" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آسوشیتدپرس: یک مقام ارشد حوثی امروز هشدار داد کشورهایی که در عملیات عربستان علیه حوثی‌ها مشارکت کنند، ممکن است هدف حملات قرار گیرند و گفت این گروه فعلاً قصد حمله به کشتی‌های آمریکایی را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23718" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnLn_1B1SEEZw0tqzR_PGH8NrvvTuRg9dsgSoUJJurt8XgG1IfehR0uSqGWW2CgvlrKyuDie7p7cDCpDZi5BgtC72GaHs_aF1AUsy2e82zI60k8QIrP4v8JyMju8Ut9xuShJXV2lPYeJmaum1fHGQCyxb7zYt5NLS73cq3lyuV0AEGsfLn0wC2L_I62N6zMxDKwroJDu57W8fwK0pClTdTZpzp95egCxdyRGFAEdxUxie_AFVf2cjq2iqDCfCLebDrPVmZoJy2TJ4Mr6Q9lkuoBGnHq1pAYZhoHa-zBO6yMEtYSxy1mX8NTbA1QO4WH27G1mc96rF-ch4KwNtcdt1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تنگه ۷ سوخترسان ۱ پهپاد و پی۸
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23717" target="_blank">📅 19:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQd0VOt1H7W3kyq9p_MtFQ5uamKlW9Mzpcyvh5jcYmIX-Eb80_og4QIUjt4xG1I9evgkUb6GwMCxg9q7itKyUyiRaeeTnvny6hfB6Rwt1VRoWIyGgEuvS9mFt3XCnaLsuMFlCwHxJ-OBcrjC7d93z4vzGFs-ZK5GlbyHDIWrFGOkzRsvdY9Nqk2RYYiVS1hH3ddPXzzYzCIK_SgVtzryBsBY2SvmEE_PTK3Rnl1LEsTi3pQ7F5nsBKcBkEr5ApROjfEk5hyQYf5nunjABeOTkqZ93d5qxyBQeGhzX-1Z2X8p_xLAukn6Vm9cvR0XHnfzcQb18KHALiPwKfbgCWFRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش حامل گاز مایع (LPG) هنگام عبور از خروجی تنگه هرمز، بر اثر اصابت بقایای پرتابه‌های ناشناس آسیب دیده است. طبق گزارش فرمانده کشتی، تمام خدمه در سلامت هستند و هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است. نفتکش به مسیر خود به سمت بندر مقصد ادامه خواهد داد و مقام‌ها در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23716" target="_blank">📅 19:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM_bwRBS0f3TvkRewbMdEfAqCalBdIx9Ks-nL7TRVmcTegZASEq8KWsTS2Uqm8zkJutWG3x6AGcM-JZWJ_dOimERlQ3wdd1tpKfH0-NMJYRyAA-ggf3JdH_ukijIPCDF_Yfu-nIjnZTQswfKMKFQm9Cn2lXToEOJQtzDPfQulmjqnBm_1ZV8Fu0itfbU5tccV7J1g2lJtvvrbi1SlffnzZZ-nmAXUJV6md4Ef3zvSi6AkG82O5cucB9Xz7RpuuUJHqye6SFet029cO9F73e8O0kU7lXXmKXzYMud1vbjwIRO98PosTjueMtS7z4hF-VfXNq-XXkaaol7Cm_YxMEp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، با انتقاد از هشدارها درباره خطرات هوش مصنوعی گفت: «همان افرادی که می‌گفتند به‌دلیل گرمایش جهانی تا ۱۲ سال دیگر همه ما خواهیم مرد، حالا می‌گویند هوش مصنوعی ما را خواهد کشت و ربات‌ها به ما حمله خواهند کرد و همه‌چیز یک فاجعه است.» ترامپ با رد این نگرانی‌ها درباره هوش مصنوعی گفت: «هرکس هوش مصنوعی را ببرد، برنده است! ما اکنون از چین و همه دیگران جلوتر هستیم و من می‌خواهم همین‌طور باقی بماند.» او افزود که نمی‌خواهد رشد هوش مصنوعی را محدود کند و معتقد است این فناوری می‌تواند از انقلاب صنعتی یا حتی خود اینترنت بزرگ‌تر باشد. ترامپ در عین حال گفت آمریکا مراقب خواهد بود و وزارت دادگستری و سایر نهادهای اجرای قانون در صورت لزوم مداخله خواهند کرد، اما او همچنان از هوش مصنوعی و «ابرهوش» حمایت خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23715" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibMPr7GQxBcDnD9lBfpz59xUbylCcvsJtuRLvQAaba8fxrJKuJ8xnTr6m02-hh3qWlcmpXkhLOa_2Z2il127ON_2dMlZjpMMfKUnyJkhVNtvB8dGveRpjol6A3B-ZAVWiJBHrANPOytv5N3X3DeNFMi_d8u-e5wfo_a7HOc78BDVIp--TUyfsXI_kaVBlQyqxw8cqi2FIfUKKsHYkFO1oCuE5AdvE90iB_2M-iW29hN1WVF8IRkdJk5mkk09ehQ0AG5m_2cieOcJnpAN9FVeBH12FigpMNq4FrLHWNWbW9nqwAwi-d3MkzrJjNTSTvbf6WYiuAGkPTgoIPchvScRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای نشان می‌دهند دست‌کم ۲۵ هواپیمای سوخت‌رسان آمریکایی اکنون در پایگاه هوایی العدید قطر مستقر هستند؛ این بزرگ‌ترین حضور تانکرهای آمریکایی در این پایگاه از زمان آغاز جنگ با جمهوری اسلامی در فوریه عنوان شده است. این تانکرها در اوایل درگیری به‌دلیل تهدیدات موشکی سپاه پاسداران از منطقه عقب‌نشینی کرده بودند و از حدود ژوئن روند بازگشت آنها آغاز شد. هواپیماها به‌صورت پراکنده در پایگاه پارک شده‌اند؛ وضعیتی متفاوت با استقرار متراکم تانکرها در پایگاه هوایی پرنس سلطان عربستان که می‌تواند نشان‌دهنده تداوم تدابیر احتیاطی در برابر حملات احتمالی ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23714" target="_blank">📅 19:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سنتکام: نیروهای آمریکا در چارچوب محاصره بنادر ایران، مسیر ۱۰۹ کشتی تجاری را تغییر داده‌اند. این آمار نسبت به آخرین به‌روزرسانی سنتکام در روز جمعه، ۴ کشتی افزایش یافته است. @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23713" target="_blank">📅 19:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فارس: برخی از کشورهای منطقه با هدایت عربستان در تلاش هستند که با فشار به فیفا، فوتبال ایران را در آستانه جام ملت‌های آسیا تعلیق کنند.
مانند کاری‌ که با روسیه پیشتر انجام شد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23712" target="_blank">📅 18:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17908a60d.mp4?token=hEquQvc9pZIcZk0kNmJpRm2LTe_6lFZFq8ZL4GNPsRsCTEHNRAXPTE-FXnivu7KoIZjShovkkSjI9BxuVGcVzgJIo-98YCT5oIr-55xgRIF9eLyHbDngSgErRIqsOTZdGXYwFphwrIGw9WwcLehqdiDuBX1q9ef9yf-PAt4nBiyFWl5rxddzyc-46M-jnWWZJgC5dsE4QYXYE2M6GgDhrzLAYSKBKTd70fyPC8KLl6q29a9Lm4VRdujTt8B64df9iRYFDOUz4JLDtM3oQnX83-lucs6huuZa7JqWrb0s9qdKv-L-XaVJi978dhUhtf_AfsZ4qt5ieu0IYZ_xcC7DJ6rlzPdQOf-_uXXZ7cZ48mIjbtnRtLQPZ7iOD4ruv9DivO5uuZFzr5EwZZU1Xyr8qx70F-mJ7l0PaCRJVGBKs49Npsn2reo1NOJp35j_8Mk9Eo0AH9ODtFhoYJaA5Ray3MbNEElBQdiX4GIuEVntCwi4I6eXZk8B-GFR1Ej7HS-PLv-2UuvxKNcrJr_uchqtRv3_7uJMKFH9i5kLfljDMgkf__a5TmAgyfYzEgc1TJS4hdCbJhFxruz7p_0aIzpr2wuQT6UnbgzYxu3f2-W-C7sEVI_2Di1QxujMmh-TIsOYiNl4bNZGX8dk_AUGjr8t0Jh4q8MhTdj34K_JOEqrhec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17908a60d.mp4?token=hEquQvc9pZIcZk0kNmJpRm2LTe_6lFZFq8ZL4GNPsRsCTEHNRAXPTE-FXnivu7KoIZjShovkkSjI9BxuVGcVzgJIo-98YCT5oIr-55xgRIF9eLyHbDngSgErRIqsOTZdGXYwFphwrIGw9WwcLehqdiDuBX1q9ef9yf-PAt4nBiyFWl5rxddzyc-46M-jnWWZJgC5dsE4QYXYE2M6GgDhrzLAYSKBKTd70fyPC8KLl6q29a9Lm4VRdujTt8B64df9iRYFDOUz4JLDtM3oQnX83-lucs6huuZa7JqWrb0s9qdKv-L-XaVJi978dhUhtf_AfsZ4qt5ieu0IYZ_xcC7DJ6rlzPdQOf-_uXXZ7cZ48mIjbtnRtLQPZ7iOD4ruv9DivO5uuZFzr5EwZZU1Xyr8qx70F-mJ7l0PaCRJVGBKs49Npsn2reo1NOJp35j_8Mk9Eo0AH9ODtFhoYJaA5Ray3MbNEElBQdiX4GIuEVntCwi4I6eXZk8B-GFR1Ej7HS-PLv-2UuvxKNcrJr_uchqtRv3_7uJMKFH9i5kLfljDMgkf__a5TmAgyfYzEgc1TJS4hdCbJhFxruz7p_0aIzpr2wuQT6UnbgzYxu3f2-W-C7sEVI_2Di1QxujMmh-TIsOYiNl4bNZGX8dk_AUGjr8t0Jh4q8MhTdj34K_JOEqrhec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره افزایش قیمت بنزین گفت: «کاملاً آگاهیم که به‌دلیل اقدامات ایران علیه کشتیرانی بین‌المللی، قیمت انرژی افزایش یافته است.» او افزود: «هر کاری بتوانیم برای کاهش این قیمت‌ها انجام می‌دهیم و در عین حال تلاش می‌کنیم در این دوره فشار بر مردم آمریکا را کاهش دهیم.» ونس همچنین گفت یکی از پیشنهادهای مطرح‌شده از سوی ترامپ، تشویق ایالت‌ها به کاهش یا تعلیق مالیات بنزین برای کمک به مردم آمریکاست
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23711" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
زلنسکی
:
اوکراین و روسیه حمله به تأسیسات انرژی و زیرساخت‌های حیاتی یکدیگر را متوقف کنند
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23710" target="_blank">📅 18:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6244aa6423.mp4?token=PqIomLpCgdE1qIZjvm4uZRajvNyH1qMO_41YbbNlKJu4RsPNKGgFO-vYvl15pcySHRWJdpdcC5AMur-Q66P4l_Y0Vd1eclcrKdsZZx-bDKZEiwNIwbhVbr0_gfQi_Z1SO0HBHN-_aEy22KlHYFJNH5gzEQjf_bsSZWBak6ku30sJ73i_d3ht6cqYrIR6jSgo63iEJq3Zibd_voB1tjFj5Ujn0Sem_FKxOvpIyMAH72tqAPMM0Nma5AL1_DrGDptYJKuml-ie2ihtp7pkPXi_8-4YKRC-836cPv-bqTCahWIjKGb9cEO4HkNm2Na8HJ5UXrE1R3ncTaMTYYQs_SgimQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6244aa6423.mp4?token=PqIomLpCgdE1qIZjvm4uZRajvNyH1qMO_41YbbNlKJu4RsPNKGgFO-vYvl15pcySHRWJdpdcC5AMur-Q66P4l_Y0Vd1eclcrKdsZZx-bDKZEiwNIwbhVbr0_gfQi_Z1SO0HBHN-_aEy22KlHYFJNH5gzEQjf_bsSZWBak6ku30sJ73i_d3ht6cqYrIR6jSgo63iEJq3Zibd_voB1tjFj5Ujn0Sem_FKxOvpIyMAH72tqAPMM0Nma5AL1_DrGDptYJKuml-ie2ihtp7pkPXi_8-4YKRC-836cPv-bqTCahWIjKGb9cEO4HkNm2Na8HJ5UXrE1R3ncTaMTYYQs_SgimQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس:
ترامپ رسانه‌ها را تحریم نمی‌کند؛ او می‌گوید: «اگر در آنچه عملاً تبلیغات است مشارکت کنید، به شما دسترسی ویژه به کاخ سفید نخواهیم داد.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23709" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f489a66f.mp4?token=ga50WqhudBMewoNPb3Tq1n2b2AvROJcPCDh1phaK7ZTJjq5dH1vRbkwew9tGInNir2Iduz_31jPIU9wnlwK5c88lUf10xDzJpM0uw_X36XKkwwn2FME2fhTAv_xS2-l4kUXjGXDGUHzsEtUs2l8ZXzRCDhLRsPG9Dtehsz9TWj0CkvyL3Chg36KADJ1i-h1ma2xuAduST_vZ0vjvMlSXGOi6poXwjsqGfXPR25eMIvr8UAlZTPketzL_as-AN-c6k9KzTw5sOmF42e9FDoiAGH9PY8vM30Q5pvsCWgemotIx0ar1Gs0aFIZtpEL9PYiMzG-HxQUYvN752dGnwn83yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f489a66f.mp4?token=ga50WqhudBMewoNPb3Tq1n2b2AvROJcPCDh1phaK7ZTJjq5dH1vRbkwew9tGInNir2Iduz_31jPIU9wnlwK5c88lUf10xDzJpM0uw_X36XKkwwn2FME2fhTAv_xS2-l4kUXjGXDGUHzsEtUs2l8ZXzRCDhLRsPG9Dtehsz9TWj0CkvyL3Chg36KADJ1i-h1ma2xuAduST_vZ0vjvMlSXGOi6poXwjsqGfXPR25eMIvr8UAlZTPketzL_as-AN-c6k9KzTw5sOmF42e9FDoiAGH9PY8vM30Q5pvsCWgemotIx0ar1Gs0aFIZtpEL9PYiMzG-HxQUYvN752dGnwn83yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس معاون ترامپ درباره ایران:
ترامپ گفت ایران نباید به سلاح هسته‌ای دست پیدا کند و برای اطمینان از این موضوع اقدام کرد.
ایران هم در پاسخ، حمل‌ونقل دریایی بین‌المللی را هدف اقدامات خود قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23708" target="_blank">📅 18:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پنتاگون ۶ فایل جدید از یو اف او ها را منتشر کرد. در فایل اول که مکانی در خاورمیانه است و در یکم ژانویه 2025 فیلمبرداری شده، دقیقاً مانند بشقاب پرندهی است که دیشب مشاهده شده
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23707" target="_blank">📅 16:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارتش اسرائیل: آژیرهایی که در منطقه المالیه در الجلیل علیا به صدا درآمدند، نتیجه یک تشخیص اشتباه بود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23706" target="_blank">📅 16:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سازمان بین‌المللی مهاجرت: در طول چند هفته گذشته، حدود ۱۳۰ هزار نفر در یمن آواره شده‌اند، این در حالی است که ناامنی‌ها در این کشور رو به افزایش است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23705" target="_blank">📅 16:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تمام ایرلاین‌های باقی‌مانده ایران تحریم شدند. وزارت خزانه‌داری آمریکا اعلام کرده ۲۷ ایرلاین ایرانی در فهرست تحریم‌ها قرار گرفته‌اند و از ۱ مهر (۲۳ سپتامبر) مجوزهای مرتبط با فعالیت‌های هوانوردی ایران نیز پایان می‌یابد؛ اقدامی که عملاً تمام خطوط هوایی ایران در سراسر جهان را تعطیل خواهند کرد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23704" target="_blank">📅 16:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کلیه مدارس استان هرمزگان تا دوماه آینده غیرحضوری شد بر اساس مصوبه شورای تأمین استان هرمزگان کلیه مدارس استان هرمزگان تا دوماه آینده به صورت غیرحضوری برگزار خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23703" target="_blank">📅 15:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کلیه مدارس استان هرمزگان تا دوماه آینده غیرحضوری شد
بر اساس مصوبه شورای تأمین استان هرمزگان کلیه مدارس استان هرمزگان تا دوماه آینده به صورت غیرحضوری برگزار خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23702" target="_blank">📅 15:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX54RiQI3J_k85xWm5TIngOBe3CPxF6FHqXJKPdikTy17lYFyOTOTX72DQsvtx_pT2U4HTDn6eZLR891yoSZG_La0I4j8GB1Mxw2YwncZPJXlNz4wXcabB91CQZZ6LCA5Qd-s0TW3MZ412PkCFNgR5OOMRWdGxerEi1jFwqi5LTjT_fzOmUGrq03JdVkRDPwJ5umF2oPLB5AJf4iYPQ8biX4OjHLB6TAXCGiQ8mNP3P7bEVWYCVmXqAFDdwrQahs_rH0pxTUFXRLxejlWPpBipaSVm1pcO5ndSJo1Uws4tYlgNWSc9v3gr3bhDyi4ChgYBcQz95g_m2oo4KzVuG5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : «روسیه متأسفانه به دلیل جنگ با اوکراین کنترل صنعت گازوئیل خود را از دست داده است. تعداد زیادی از پالایشگاه‌های گازوئیل آنها هدف حمله قرار گرفته و دست‌کم به‌طور موقت از فعالیت خارج شده‌اند. این جنگ مضحک و بی‌پایان با اوکراین باید پایان یابد. تمام جهان در حال متحمل شدن هزینه‌های آن است، چرا که هر ماه حدود
۲۵ هزار نفر، که بیشترشان سرباز هستند، کشته می‌شوند.
چه تأسف‌بار است!»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23701" target="_blank">📅 15:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نیروهای دولتی یمن : 5 حمله هوایی را علیه مواضع گروه حوثی در جبهه الاحکوم در منطقه حیفان، جنوب تعز، انجام دادیم همچنین یک پهپاد متعلق به حوثی ها را هم در کوه جرداد، جنوب غربی تعز، سرنگون کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23700" target="_blank">📅 15:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پست جدید پرزیدنت ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به کاخ سفید رو نداده @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23699" target="_blank">📅 15:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بیرانوند دماغ به دلیل خالکوبی خواستار بررسی معافیت سربازی به دلیل اعصاب و روان شد. خالکوبی به تنهایی دلیل معافیت نیست، اما در صورت تشخیص پزشکان مبنی بر این که خالکوبی نشانه مشکلات اعصاب و روان است، امکان معافیت وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23698" target="_blank">📅 14:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کرملین : روسیه هیچ اختلاف نظر با کشورهای اروپایی ندارد که بتواند منبع درگیری شود
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23697" target="_blank">📅 13:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eba0f5326.mp4?token=fH_4l07M0ZWV0PdfQxq4oA-_OQLLJAxEtiE51rqTmloaVH5HSK_FjAVLrPxXwOhXxLb7CLVfdLO_ieYNDZ8GFWvVzrvgP-_rk8I9gNWbnQJf9MKw5MwiX9ZRZpG1f8xbK0Es3lyjAZwNfmvklsIle8DhMtBG2PloyZ0U8qHMthxcq4qbV6c3uCHOFZgQyXpLPEyrEcngSJsh_cMQ0cAaJUiCPxf9atHD6GSZMpDGq8kcop5JHNT7X62gyBIGoFKmTk26amuWie0pvSeayAF5VZYYuf5bB4NdW_q9F8_g7AeDQ4PoTiccF5_nlpWc6bYu76qLcZtFZs4Ivq1kp9YPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eba0f5326.mp4?token=fH_4l07M0ZWV0PdfQxq4oA-_OQLLJAxEtiE51rqTmloaVH5HSK_FjAVLrPxXwOhXxLb7CLVfdLO_ieYNDZ8GFWvVzrvgP-_rk8I9gNWbnQJf9MKw5MwiX9ZRZpG1f8xbK0Es3lyjAZwNfmvklsIle8DhMtBG2PloyZ0U8qHMthxcq4qbV6c3uCHOFZgQyXpLPEyrEcngSJsh_cMQ0cAaJUiCPxf9atHD6GSZMpDGq8kcop5JHNT7X62gyBIGoFKmTk26amuWie0pvSeayAF5VZYYuf5bB4NdW_q9F8_g7AeDQ4PoTiccF5_nlpWc6bYu76qLcZtFZs4Ivq1kp9YPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت موبایل یک پاکبان در مشهد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/23696" target="_blank">📅 13:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جماران:
آمریکا برای
هیچ‌یک از اعضای تیم رسانه‌ای همراه مسعود پزشکیان
جهت حضور در مجمع عمومی سازمان ملل در نیویورک ویزا صادر نکرده است. مدیرکل تولیدات رسانه‌ای دفتر رئیس‌جمهور گفت قرار بود یک تیم رسانه‌ای کوچک برای پوشش سفر پزشکیان اعزام شود، اما با صادر نشدن ویزا،
هیچ‌یک از اعضای تیم رسانه‌ای رئیس‌جمهور نمی‌توانند او را در این سفر همراهی کنند.
آسوشیتدپرس تأیید کرده که برای پزشکیان، عباس عراقچی و کارکنان ضروری هیئت ایرانی ویزا صادر شده
و هیئت ایران امسال با تعداد کمتری از اعضا در نیویورک حضور خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23695" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قطر ایرویز
به‌دلیل
جنگ ایران و افزایش قیمت سوخت
، شماری از پروازهای کم‌سود خود را به حالت تعلیق درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23694" target="_blank">📅 13:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-bK_r3Eo_qEuxsbI5-3Cgyb_2yHfH8u_E-ysACLMw5-KYAh-eMbbAxbtcbnSOHYZiVjM0Z8LJemk3LG0Nx7C2gw8JhJp69Jm46XGj44h4dS22eeBwuxHZxC5PrnJLcZdIxMidVuw9AtTzYipE0wU5GWDBYYZ6PUIY5eG7mCQ3MNj5nn78V-Zx1n-6kOP_i5ZJ_9oaMsvqlmaUkL8aLCei4h_XMuU8PxLa5nF5zjBy6C8LnyDCnrYqhYfSOTLVnLg8pGBoAm-KDmkUjuLUF8f-2tgtUzXwKu6qUck7Fw118lwndf7junpOhJd1CEdtT6jkEBuqSeVtEXyrVmYPB8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏هم اکنون آتش سوزی در میدان آرژانتین,  تهران
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23693" target="_blank">📅 13:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJt608LXUx0NidOpnrE_3kVupr3qujIbEo5e7o7haXOb3H2aQeao2O2LuESlhdBk7j36sxgq5MGTxyX1xeqpSI92p1FPNJ-38iu-9tB_fikTW1MgCkdq1jFPbCQu8MJy3MDQ_U1h2yPZOBS0huERLTnGK_zMM0ssE_Ymsky1X9tAb2rLw8-rhJWR-5UTP1ExMTBqMkFXU7d_LdUubCZZ_Y0Tm2OvBoA5AZAvdq5VHJB2FijlJCB_ucb8CxnBA2Oza0iF6EmfodfefWlFvGdmqXtCuAhlhKqpEdfkqQD3XzDwUdNWcjSApStDqJFjeN49euUM2tiLH_ry8KYgUOVYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار ما دریاچه چیتگریم ی صدا اومد الان  پاشدم با این صحنه رو به رو شدم ی بوی باروتی هم پیچیده @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23692" target="_blank">📅 13:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23691">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرتاب موشک از گرمدره ۸:۳۰ دقیقه صبح امروز @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23691" target="_blank">📅 13:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">BTC 84,100$  @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23690" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23689">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAW5nD1kll5L-lUw7uXj2s-PrlGUqMyEPpmgSxo5BDUZiqDH1-NRWtHB66b8R6-4XHy6K92_HhWIicNWUNSOkJniet9V0asjTax0IYAEC8r2RH6tuMpntBw78VImneRzjzChJP4q6dYHYFKRQYPAVSKF-yoW6EFqiRPLlgLlXtQTgjVcHNZsp9sbxvCAFzllKIhQs4IQMyXRn5AA80qxWB8xXGyJTOCkN4Y3qrbobzqFYeyC7iKiJYA-m3-M-ij0i2osEBE1Sat6FcD3jGKRTIi-9fdWThhh2LgogXqkzWIt5LHAzUvsFRQLeo1baPex_u-pUcp8LzgHTWpJgZyifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) به نقل از مقامات نظامی گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
دو تن از خدمه دچار جراحات سطحی شدند، اما شناور همچنان با نیروی پیشران خود به حرکت به سوی بندر بعدی ادامه می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23689" target="_blank">📅 13:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23688">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23688" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق CIA:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!! صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند. این‌طور بود: «در این گوشه…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23687" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک شاخص مهم تکنیکال بیت‌کوین دوباره فعال شده است. گزارش امروز BeInCrypto می‌گوید بیت‌کوین برای نخستین بار طی ۴۵ هفته بالاتر از میانگین متحرک ۵۰هفته‌ای خود بسته شده؛ Galaxy این سیگنال را در چرخه‌های قبلی با کف‌های بازار مرتبط دانسته است، هرچند این به‌تنهایی…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23686" target="_blank">📅 12:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز:
یک نفتکش عظیم حامل حدود
۲ میلیون بشکه نفت عراق
در نزدیکی فجیره در حال انتقال محموله خود به نفتکش دیگری دیده شده است؛ این یکی از روش‌هایی است که برای ادامه جابه‌جایی نفت در شرایط اختلال تردد در هرمز استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23685" target="_blank">📅 12:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">استنفورد:
پژوهشگران پزشکی استنفورد روشی ساخته‌اند که در آن
مقالات علمی به عامل‌های هوش مصنوعی زنده تبدیل می‌شوند و این عامل‌ها می‌توانند با یکدیگر گفت‌وگو کرده و فرضیه‌های جدید علمی تولید کنند.
این پروژه برای استفاده از AI در کشف علمی طراحی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23684" target="_blank">📅 12:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3147444cd0.mp4?token=r-Wp6Ww5HAkh_O-z8uIwqUb4gmEYThFfnNKUBFAuwT_qqBCm_TavmS7_PtP5QAOa1DuXX-Ant1NEdeIq21k4CQ8FJycXLKS0jft0zkN351VK_X3odFvYuSjY0ADYdbfo3s18REKo8avb1lOLAtJ1cwH49TSIHZPadsIA8-EpemV_hGgio5nnIwNwxYUoT6F-SOUbpS15SmRNojJ3OkCyB_rWKXwuxX_JZW-qzP1FWXhFKUmYFjlA8AOqMlTYiP0Jus-NgZMNsIvZOoL2KRynQWRin-xUqB2Tx275oLYSbFSfhrJ_h-87jRSD5z6kCwcY-PEaCrw1v8r9g4kHmuCFuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3147444cd0.mp4?token=r-Wp6Ww5HAkh_O-z8uIwqUb4gmEYThFfnNKUBFAuwT_qqBCm_TavmS7_PtP5QAOa1DuXX-Ant1NEdeIq21k4CQ8FJycXLKS0jft0zkN351VK_X3odFvYuSjY0ADYdbfo3s18REKo8avb1lOLAtJ1cwH49TSIHZPadsIA8-EpemV_hGgio5nnIwNwxYUoT6F-SOUbpS15SmRNojJ3OkCyB_rWKXwuxX_JZW-qzP1FWXhFKUmYFjlA8AOqMlTYiP0Jus-NgZMNsIvZOoL2KRynQWRin-xUqB2Tx275oLYSbFSfhrJ_h-87jRSD5z6kCwcY-PEaCrw1v8r9g4kHmuCFuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از گرمدره ۸:۳۰ دقیقه صبح امروز
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23683" target="_blank">📅 12:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">BTC 84,100$
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23682" target="_blank">📅 12:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e4ac1ec1.mp4?token=Xtw2WyHRQmAyRSN-Bjk_aOfCqa-k0cKNjj38JnadwOWIxVaQdEkIiuTgA6bGsWdp0i1i1NlRne_QGzSnsZ7p0Ic3mIgUmS8aZKt5rTuj9KiluYErmOHSLVUZwJamoA9v0fSHDH0Z88oxqeQpBMYkBzI5uQoKwjDvubxSGFIawV8OI78MQWWFF7GM1qdVw4yWzBi66WcYBv9iDatjK6s1ikHjgGtLpvfo3GHjemu0hKAsz6A2B3z3mCBib5DjfX16jfnAen43tOAqwGYvCBABxGwKsaestmcZCowKSxDyaFLgPhglhY2l9sjWeHxlAecER8ow3nt3hfdRuzkMdIt0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e4ac1ec1.mp4?token=Xtw2WyHRQmAyRSN-Bjk_aOfCqa-k0cKNjj38JnadwOWIxVaQdEkIiuTgA6bGsWdp0i1i1NlRne_QGzSnsZ7p0Ic3mIgUmS8aZKt5rTuj9KiluYErmOHSLVUZwJamoA9v0fSHDH0Z88oxqeQpBMYkBzI5uQoKwjDvubxSGFIawV8OI78MQWWFF7GM1qdVw4yWzBi66WcYBv9iDatjK6s1ikHjgGtLpvfo3GHjemu0hKAsz6A2B3z3mCBib5DjfX16jfnAen43tOAqwGYvCBABxGwKsaestmcZCowKSxDyaFLgPhglhY2l9sjWeHxlAecER8ow3nt3hfdRuzkMdIt0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی عجیب یک هم میهن از چسب محافظ پنجره در برابر انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23681" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e81b36f52.mp4?token=Rgla55MCwS6otpIaYg9B1gmuH6sxclCdRSnCJ3sB621asC8ybfozz0kJTvqD-2kQ_ZTw0cM18LZQGBpAFRqZPg3nYUbOIQW5yKHghDYnNf1lUOIhavjNoYT9ryQEbM4DABCklx6H0xopo4zxXDulNrb1bD8U-NrcrzMlKj31nS8LLiJwsKc9JghssJyScEdZj6ixUTt2j6DFp01iQ1PFWvxA7ilrva0qGJOuDW8T00MaD4AtD0RnPfsQb80UV6wAsIKLF7fcikLprv8NWBOTnze_FtGrcuABRMbUQdfHQsw_Pg9hXBpI2GfB_uV_-a9gd-d5-RwFqKLSX_GxBk-rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e81b36f52.mp4?token=Rgla55MCwS6otpIaYg9B1gmuH6sxclCdRSnCJ3sB621asC8ybfozz0kJTvqD-2kQ_ZTw0cM18LZQGBpAFRqZPg3nYUbOIQW5yKHghDYnNf1lUOIhavjNoYT9ryQEbM4DABCklx6H0xopo4zxXDulNrb1bD8U-NrcrzMlKj31nS8LLiJwsKc9JghssJyScEdZj6ixUTt2j6DFp01iQ1PFWvxA7ilrva0qGJOuDW8T00MaD4AtD0RnPfsQb80UV6wAsIKLF7fcikLprv8NWBOTnze_FtGrcuABRMbUQdfHQsw_Pg9hXBpI2GfB_uV_-a9gd-d5-RwFqKLSX_GxBk-rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق CIA:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!!
صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند. این‌طور بود: «در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار. اسرائیل هزاران نفر از این افراد را استخدام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23680" target="_blank">📅 11:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC_o5i_mlaic2LUYz3MhBJbtP6dC3qaNaO7Wz5rhVUf9YuqzNLhVRnv50WGxS6VwbQjR4BVBYxWrasHeiYwNalIANP5lNzvXt6jxS0C3B3wTltiZErpr6mXBp1tM7L0t5ruSA1PS9Scf3BZV6W7PKbjV2Lk72nXnJAJ7aO5J4odfjFE0iCTannB8FVlcXaXkGZ-6ApTfFjOucl_-dLj4Huf1n4SAot_q1KN9UQr2D6N1hYRIsBwPebQAG3DHujdT6j-_BnWNS1wnCrv0A2Wh08eNCV7TTbJPq3gCHptoqykOVe7_kIekkIWOYSaprbOrZ2sQQkCcWEfNVIwcSndPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23679" target="_blank">📅 10:54 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
