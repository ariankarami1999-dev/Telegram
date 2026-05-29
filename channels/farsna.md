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
<img src="https://cdn4.telesco.pe/file/Uvw97F-ziHL8j6qzVbl1Ow9kc_zD6959PREcpDVGDUxITFwM-o-RyyDm2b1K60DQaR10eJ2V_N8YMpfeAlDeMuxfvLuLXBy5_honBAq1x0LY19dUAPfuwVFd3AvqD6FsSKvDZOc9MKwk_Md9VAMeU8bRyIKj8WKj_pEUir2wL3L1g75U-zoiXpiKmsFxeGrILjgZ_b9sLC9kxSkW18ehsJxTxmav2dhzL6vTsN1LKaBrnwwosGDxeh4TAGlbRK4UUvIMrLlqGh55D9qMYDlX9lMe1azYb6YAQULwsj8pA6SVW7XDm-HXvEElThpXpQ0MjsEti14e452b6_VTyqTzqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
<hr>

<div class="tg-post" id="msg-438583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CduUUNkJtCYbAwxeXFJx38MMT0u2SlOitcJy_tJryx98ek3vX_19l7k0W4PvppF-lRM0rD3812z9i8aGYvggE8ZOCtITDjo7ZIMHOEnTigm_TvsiF1eJRlLUuYMiJr0YO1TtL_zwhw9tGHSq1H0rMUmJtY0UJaSiHJm0Bt1u-T-cKg79-OphE8PUYfUaNYWX-lpKOmWGwORqtigP3KfxBXW9p_vGqZN5OJhrjMRxX2umPVKgM5XRwytOtJOp2QaW574gf9kLHoIdnAVyl8lWW2DXC8Pa3p6btB8sP7fq3OJxZT0CikaolJO6SZ55IJEWi4wB1vXkKOhZn9zAQtj3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبعات جنگ‌طلبی نتانیاهو؛ یک سوم اسرائیلی‌ها به روان‌درمانی نیاز دارند
🔹
پس از ۳ سال بمباران بی‌وقفه و جنگ‌، از نسل‌کشی اسرائیل در غزه تا جنگ‌ها و حملات علیه ایران و دیگر کشورهای همسایه، تحلیلگران و پژوهش‌های متعدد در داخل اسرائیل به این نتیجه رسیده‌اند که جامعهٔ اسرائیل به شدت تحت تأثیر «تروما» و آسیب‌های روانی ناشی از جنگ قرار گرفته است.
🔹
«تولی فلینت» روان‌درمانگر اسرائیلی و کهنه‌سرباز جنگ با اشاره به افزایش خشونت خانگی، افسردگی و اختلالات ناشی از استرس می‌گوید: مردم اعتمادشان را به جامعه، دولت و نهادهای خود از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/farsna/438583" target="_blank">📅 13:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a550993e97.mp4?token=LXlKamRaQn7_XRgycGxJrMvoeZT_c2cWkso7MSLIpsndRBiACEBF5oHOnzIFyM43UkikqOZ6u4TehRKcdNJfF1PPHmKSzdVw5f_pjXyp5Z8p2ZISbDABD5rEIY57sthZJwidC6nmq9EoenlVtMpTqAnL74Pvy7EaGTySpz0WA467BzMkjQte3iY-sWXm77VKJJbzvIGqYKtuAuX2jw7ojHmjEi_plqT6y_IcYUi6HPsWQllvD0VDlr2WadsrUZai6D66RiKhD5PkjR91Kd0vd88JTFmZXMQYN_zgeiTY5KbGG5gsBIae-HxXvNxBR-bmeSwGjgduXezifhgxUwJzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a550993e97.mp4?token=LXlKamRaQn7_XRgycGxJrMvoeZT_c2cWkso7MSLIpsndRBiACEBF5oHOnzIFyM43UkikqOZ6u4TehRKcdNJfF1PPHmKSzdVw5f_pjXyp5Z8p2ZISbDABD5rEIY57sthZJwidC6nmq9EoenlVtMpTqAnL74Pvy7EaGTySpz0WA467BzMkjQte3iY-sWXm77VKJJbzvIGqYKtuAuX2jw7ojHmjEi_plqT6y_IcYUi6HPsWQllvD0VDlr2WadsrUZai6D66RiKhD5PkjR91Kd0vd88JTFmZXMQYN_zgeiTY5KbGG5gsBIae-HxXvNxBR-bmeSwGjgduXezifhgxUwJzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل در رودخانه فرات، در شمال شرقی سوریه
🔸
به دلیل سیل گسترده، وضعیت بحرانی در استان‌های دیرالزور و رقه اعلام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farsna/438581" target="_blank">📅 13:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7080a368e.mp4?token=k8jEh2PmEPNW_7AZIRjTLC2Ri1SqvNjmiGiTPV8fYvs21ZCDsodpXM5f4ifJksBtYhdU8JvIwAIXhyyWCguTd2pyEETaxikWJXiM5ZBit5fQdJSHWYhMCT6-8JaKRoNQ29qP4cxtbFahe_k1JLygcQUvQ4hnkMVS2OemuHdv2waoaVx5Zq6H6_gpI1NJaLMON9-QTh7DH7do7GFPD3n2Rgam4bXJfy7r-MVFJP_vffkfEsOG1JyEmK6a32Wo4JemsLin0vQxc3whVBN5uGt5p5xfS4N07GeVj6_6t2irZbQiKaGGaKxFPjRSuQFhA4PfAJZ_s_zqJVbSLhZ2ztdOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7080a368e.mp4?token=k8jEh2PmEPNW_7AZIRjTLC2Ri1SqvNjmiGiTPV8fYvs21ZCDsodpXM5f4ifJksBtYhdU8JvIwAIXhyyWCguTd2pyEETaxikWJXiM5ZBit5fQdJSHWYhMCT6-8JaKRoNQ29qP4cxtbFahe_k1JLygcQUvQ4hnkMVS2OemuHdv2waoaVx5Zq6H6_gpI1NJaLMON9-QTh7DH7do7GFPD3n2Rgam4bXJfy7r-MVFJP_vffkfEsOG1JyEmK6a32Wo4JemsLin0vQxc3whVBN5uGt5p5xfS4N07GeVj6_6t2irZbQiKaGGaKxFPjRSuQFhA4PfAJZ_s_zqJVbSLhZ2ztdOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند شهیدحاج قاسم: خانوادهٔ رهبر شهیدمون زندگیشونو وقف آقا کردند
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/438580" target="_blank">📅 13:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf3edc94f.mp4?token=UaboxfsOrmwLKYZLq2zeUSoHSmzkAeQXXtQ-jMxYntIVxNYzlztLDfYtXqyu21qM8E2X-ZAXZcjW0EZ9h7b8dATf6YQqdgRNC7LztumYewBunhCc6Jzew5I3ZqWC7Ew-BV1xWFjQoIJxK3FJ8n5tr1HC2EsKHGQoJZNvnAGbqzGxcTs8n1Ra0NVn_hhzBawtcW_ZaPOCDMTiV9Szg6Df4kgUocITS2hnUWtgCPlodhonne0zdQ-hpObRoBULWjXCtu24cjWNgDgZZA8nRBtMvt4zASJ8kmqmMJVwC2NndFBdDpEmCXRb0BDSzGHNaCklyvG3R0WIa-tEyGu53PSxMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf3edc94f.mp4?token=UaboxfsOrmwLKYZLq2zeUSoHSmzkAeQXXtQ-jMxYntIVxNYzlztLDfYtXqyu21qM8E2X-ZAXZcjW0EZ9h7b8dATf6YQqdgRNC7LztumYewBunhCc6Jzew5I3ZqWC7Ew-BV1xWFjQoIJxK3FJ8n5tr1HC2EsKHGQoJZNvnAGbqzGxcTs8n1Ra0NVn_hhzBawtcW_ZaPOCDMTiV9Szg6Df4kgUocITS2hnUWtgCPlodhonne0zdQ-hpObRoBULWjXCtu24cjWNgDgZZA8nRBtMvt4zASJ8kmqmMJVwC2NndFBdDpEmCXRb0BDSzGHNaCklyvG3R0WIa-tEyGu53PSxMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشتی‌ها در بخش عمان تنگهٔ هرمز، یکی پس از دیگری لنگر انداختند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/438579" target="_blank">📅 13:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_p0o-V7Q34M1YRpkkeL7AktU_xYK5I_womBNKvSXd3hFi9DRyv-TJNl5ZezyDqUdBi69PXt3LDIR79moyckoiqz6GCeGZ6iqSpTcAVWmBNzoo7Iy3W5aNYRgj-CUhPtJ8pITe1Zscqe2r_bt_HWIQ3SRa_on0D-WxQKnCSu4YI7E4ShJvi2YoSDTypPtTDu7JZIy7Z6aA4vMN-fmbTbcr_Lcsq_NJMFhtM0sJR3eIWx8D3C7B2hSQsFc5mqMuaOKDn7G-zui6gzYbg1uQr6UraN_BSZw0p-dzYf_M3O0PO8FqlYFfcxu-feWu5AekCx1tU6ODhaWe3ArMzj-mpXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محمد معتمدی: چند رادارشان منهدم شد و حاصل شد برگشت آب به دریاچهٔ ارومیه
🔹
حالا فکر کنید اگر کلا شرشان از منطقهٔ ما کم می‌شد همه‌چیز چقدر پربرکت‌تر بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/438578" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9ZcUF9679tM-DoOWhkBtbXJn1mJISh1exilXO0QvBF-ADB-r9xsxb4jnK2-EEuhE45KgS9Ks5qAXP27xLEfqNus3s9sNbX9kvvY-0KUD-D0buvYQtYM6otjOjULqHqmmlxxw_vMN48XyI7DE4e3BuOZuD01AwnUhtzEJ1Hokkdh7w67t-Fmf87CLUf2Op7mGTbTHQFn-ESOnQ9yqudnjArvz9Qe-PkmYGg5v63OhEOoQlvLZvjHgQJsFY9ZcEznvjNZ4qNCc-2vCca6SaY_Arz8ktSe1KU8Y_hWMpoiIr5xP5gpF3n3A4C4yW_awrNwgXrnzjhaH9t-yJhciXfiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس مجلس: پیام رهبری نقشهٔ راه مجلس برای تحول و پیشرفت کشور است
🔹
حاجی‌بابایی، نایب‌رئیس مجلس:  پیام رهبر معظم انقلاب، نشان‌دهندهٔ تراز واقعی جمهوری اسلامی ایران است.
🔹
این پیام در تمامی ابعاد دربرگیرنده این حقیقت است که جمهوری اسلامی ارتقا یافته و تراز…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/438577" target="_blank">📅 13:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKMFA4ef2sjneuBHreJeGWbNReizvacm13_5J5xfyAe8UliJQGCeDIN_on9FigGzMynrSnUnKyG357Rk6Zg85cYzr9r--McdxDfdPQj1tB4RF_TzKzA6K6PKseECmZ6SfsXLpOArOFpd1G-bOcL7NwOoqaYC43MmXJdlMfaG1MBIlrjxB6WP97IaVrcfT0JN9APS0u6jLjznz5M2j3OGt3FH17TIVGxK_P5feXsoXwpyW1d6xMxw9pKksEHNxNYtTnGro1D7Ln-qYybL_ICD4BuLk2m3kuqUVhTw91lu_ugTaGo6AtWwKUEwUa8-u9YDO7F3tiA0TWujdOXt3EW7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب نماز جمعهٔ تهران: دشمن متوقف نیست، ما باید در مرز دانش و فناوری حرکت کنیم
🔹
حجت‌الاسلام ابوترابی: تعرض آمریکا در سحرگاه دیروز به نقطه‌ای در حاشیهٔ فرودگاه بندرعباس که نه خسارت جانی داشت و نه خسارت مالی، اما تعرض به آسمان و زمین ایران بود. این تعرض از پایگاه هوایی آمریکا در منطقه انجام شد
🔹
به توانایی اقتدارآفرین هوافضای سپاه پاسداران انقلاب اسلامی، پاسخ سخت و شکننده داده شد. پنتاگون هم گفت که آتش‌بس شکسته نشد. این یک پیام روشن دارد؛ یعنی ارتقاء قدرت بازدارندگی جمهوری اسلامی ایران، یعنی تغییر موازنهٔ قدرت به نفع ایران.
🔹
این قدرت بازدارندگی باید در مرز حرکت کند. شما فکر نکنید که دشمن متوقف است. ما باید در مرز دانش و فناوری، در مغز قدرت دفاعی حرکت کنیم. این قدرت است که ما را در جایگاهی قرار داده که آمریکا را تحقیر کرده‌ایم.
🔹
امروز دنیا فقط یک زبان را می‌شنود، آن زبان قدرت است. باید اقتدار ایرانیان، اقتدار امت اسلام، اقتدار محور مقاومت افزایش پیدا کند. این راه افزایش ظرفیت‌های ملت بزرگ ماست.
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/438576" target="_blank">📅 13:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🎥
روایت عکاس پیشکسوت دفاع مقدس از ماندن در پشت در بیت تا هم‌نشینی صمیمی با رهبر شهید
انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/438575" target="_blank">📅 12:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVDgV-WOfzadqQ49nfGDqUQ8LbuqJfuNfdoHJ3LZX8qGRJppzfUpIUBOJ5wkOvNje9d80UehdjnZ2X3X9fKeNRSXZOn6VXHvYLornUFtflaglef4TaJUcYWMgg65Ua4H9NJbSPsukEmfKu-tJwHSnkNar8kK62cWiJGjnpg95AgJ2appe30zUUq9QKl4g-jwC-x44BeIIN0axIG73IHojPJ_actSbAJNmNX_MXxiTD_C_MXb-IrsnnOd3EtJnRAQrQkyyEsz7B9F1pHOaCwGkRNOO5VFW3BFRn9bpjxjJnbYij1dmYm6lzIZeWUmq0lT31maCltb0MlxjTo-nDtzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت ۲ عامل اصلی آشوب‌های دی‌ماه دره‌دراز کرمانشاه
🔹
۲ نفر از عناصر اصلی آشوب‌های دی‌ماه سال گذشته در منطقهٔ دره‌دراز کرمانشاه به نام‌های مجتبی ویسی و میثم ویسی، روز گذشته در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🔹
این ۲ نفر از عوامل اصلی اقدامات مسلحانه و آشوب‌های دی‌ماه بوده و در شهادت شماری از نیروهای حافظ امنیت نیز نقش داشتند.
🔹
نامبردگان از هواداران گروهک‌های ضدانقلاب کُردی و به انواع سلاح‌های جنگی مجهز بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/438574" target="_blank">📅 12:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5da1685e7.mp4?token=WAVNxDhNLLdNllnuDzuE-yEc1Gcd0UTvV1yPtqKxTNuTdGS81PPTGrfyGIoCaRsUdi3Kn-GzB8PPnkQBBeRnpqw0lxB6yA_WXPnpwA_XJu9-zGvS5HGdlAh1FhmtTxkh421p1ogRgk5_QOs_XwfkQXo5gJbovvtSndHQRY84YaNS1I_rBMCXooVR6RwxRFLyv_aqVI7zcwpZ60E5_p1s6ZprHf1ZRan1Gy3rm5XhjyJ4YhLM5Z0Pjk0SavLUZ5P4DR8hQgo8TG0h_bBpXZLPTMoyNChxmqj9P6A8O0aXUANr4hQkxZUT5PJj01vy83gnlp2Od5CXquPULctp2K-AQijpfv6Te8-rm6vxNP9ZbpD7Fw6RV5Jam5zVspGG_xghvMUhYETI8iI-2QebtSf1AsVErfYkUGuVOxTBTEUxI2e_UuIn25rgYtZ3mXpFVTzxrnxrLV8q-o4UaF6GEpn4FUh449J0vm4W8ogX_pX-khhl67LEBs6_MvD0iYBujVnQfs6jqtIb7wZnRvtya-ExboYM-HuxisilUBThxGiVBFDq-R414J20yb8FCMKOEHabeMQbiiYLQGeZ2a1-s8t1HdmQNhBB78iUj3naNW6S1UuMLWtjaNrRDeBB7xvJj8tow6uwSSz-Tfqx-XrVYM_iz5a7ZVhpmTMDOvwL84Mt7QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5da1685e7.mp4?token=WAVNxDhNLLdNllnuDzuE-yEc1Gcd0UTvV1yPtqKxTNuTdGS81PPTGrfyGIoCaRsUdi3Kn-GzB8PPnkQBBeRnpqw0lxB6yA_WXPnpwA_XJu9-zGvS5HGdlAh1FhmtTxkh421p1ogRgk5_QOs_XwfkQXo5gJbovvtSndHQRY84YaNS1I_rBMCXooVR6RwxRFLyv_aqVI7zcwpZ60E5_p1s6ZprHf1ZRan1Gy3rm5XhjyJ4YhLM5Z0Pjk0SavLUZ5P4DR8hQgo8TG0h_bBpXZLPTMoyNChxmqj9P6A8O0aXUANr4hQkxZUT5PJj01vy83gnlp2Od5CXquPULctp2K-AQijpfv6Te8-rm6vxNP9ZbpD7Fw6RV5Jam5zVspGG_xghvMUhYETI8iI-2QebtSf1AsVErfYkUGuVOxTBTEUxI2e_UuIn25rgYtZ3mXpFVTzxrnxrLV8q-o4UaF6GEpn4FUh449J0vm4W8ogX_pX-khhl67LEBs6_MvD0iYBujVnQfs6jqtIb7wZnRvtya-ExboYM-HuxisilUBThxGiVBFDq-R414J20yb8FCMKOEHabeMQbiiYLQGeZ2a1-s8t1HdmQNhBB78iUj3naNW6S1UuMLWtjaNrRDeBB7xvJj8tow6uwSSz-Tfqx-XrVYM_iz5a7ZVhpmTMDOvwL84Mt7QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از حضور مردم عزادار در مراسم یادبود خانوادهٔ امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/438573" target="_blank">📅 12:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXLkaoTNMtaAVIIuvk-Gc69jnR8fkejFZWwFU55S0PytbSfhYJ8GeUjGh6U_9AHMY4Ch_1yBGoNbeaTIqQtC2S1dzPXtvgd-1d2Say4r7iA2bnqlXpZMaR0HuhWnCtri4aKE5K7nC_bJAp5Xsxjb0AhGIo1KqsrMrQGGVPWgU3d5BjblQFJPa8gDdoab9q8a34QO57dZD-0941RzKrDxXYUtqt7bmxnAPxPK1vzQPIy6Sdmu5UrCyXyvie1v1fCnFs_4QQROamuDItB0Oj3x2xRUBIo0fZfzmes3K8XVRjzjKeGv5y1BviwI3N7pG7gW37s26eCayjAYp400JblN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰ درصد کارکنان دولت سوریه بیکار شدند
🔹
به‌گفتهٔ تیسیر رداوی، رئیس‌ سابق هیئت برنامه‌ریزی دولتی سوریه، آمریکا در ظاهر تحریم‌های سوریه را لغو کرد اما  ۹۰ درصد مردم همچنان زیر خط فقرند و وعدهٔ رونق پس از بشار اسد به بن‌بست خورد.
🔹
در دورهٔ بشار اسد، علی‌رغم تحریم‌های شدید و فشارهای خارجی، دولت تلاش کرد با اتکا به متحدان منطقه‌ای و مدیریت منابع، از فروپاشی کامل جلوگیری کند و شبکهٔ تأمین اجتماعی حداقلی را حفظ نماید.
🔹
اما پس از روی کار آمدن الجولانی، نه تنها این ساختار بیمار اصلاح نشد، بلکه به دلیل نبود تجربهٔ مدیریتی و اولویت دادن به مسائل امنیتی، ناکارآمدی و فساد اداری چند برابر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/438572" target="_blank">📅 12:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqQdKeXvTnMKmjI5TEUfevFLNnCbCLK84yN7jGIfzye9ODhuGWuYmYCq8MrMszeKoLx063H4SbxpP7Y4YBB0XFU5K7E_NGRCTGZhpcj3orCBm4khvNgsAVd0ySpa6d3lCOR5NPMYS32HpgfeRStwL0wLU0I6To6E6QVYxTK2DP25LTY2gaw4R3gPw0KMOivXiCKtnQBfacGub2R9H8eKe6P1I-Y3hthF27N5I4DcrL4nW1TOticOAdDfbK19RzIRq1WthaAfJG5z2JgVR0DcYHH54Wti6U1e-TJwB9f3POz0u2t_scAHJxrhnaGjuKQNO355WBbyJfdam-CiVZQIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخالفت رئیس اندیشکده استرالیایی با ادعای ترامپ: تنگه هرمز جزو آب‌های سرزمینی ایران و عمان است
🔹
«تیم اندرسون»، رئیس مرکز مطالعات ضد هژمونی، ادعای دونالد ترامپ درباره بین‌المللی بودن آب‌های تنگه هرمز را رد کرد و تأکید کرد این گذرگاه راهبردی به طور کامل در محدوده آب‌های سرزمینی ایران و عمان قرار دارد.
🔹
اندرسون در پیامی در شبکه اجتماعی «ایکس» نوشت: «باریک‌ترین بخش این تنگه تنها ۲۱ مایل عرض دارد، در حالی که کنوانسیون ملل متحد درباره حقوق دریاها (UNCLOS)، آب‌های سرزمینی را تا ۱۳.۸ مایل از خط ساحلی تعریف می‌کند.» وی افزود عمان این کنوانسیون را تصویب کرده، اما ایران و آمریکا آن را تصویب نکرده‌اند.
🔹
به گفته این تحلیلگر، بر این اساس، تنگه هرمز کاملا در محدوده آب‌های سرزمینی ایران و عمان قرار می‌گیرد و هیچ آبراه‌ بین‌المللی‌ای میان دو کشور وجود ندارد.
🔹
وی همچنین تأکید کرد که ایران در حال حاضر عبور کنترل شده کشتی‌های «نامتخاصم و بی‌آزار» از تنگه هرمز را طبق عرف بین‌المللی مجاز می‌شمارد و تنها تردد کشتی‌های مرتبط با دشمنان خود را محدود کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/438571" target="_blank">📅 12:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2zTLIB9eUFnkbPUrGwNLOUVDF3XQloz0hhubH9B-5qIZsHCr2Xe5ZH1nZyxH9e__5HQSYcUUP8j7nacrCHcCTwFo4YT7lc9OTKX6Llo2hvQPZwsU3EXtSPeoka4gOY8xaKLNRotTTHylPg9ffPTtyo0Zjja4oXPkIOpV-qhPlHDQA2vssnn0f-yhAT9GpHl1dv-tUC26BzsuHii8eCmK4jY21qyyW1VvP6_E57wwoV227knSdAbH7DIYSm97OU7kE91TQi20vJBVBLVmuhuY1WT-aFRlYMZDtAQy_uBwgP8es9ss64ND4uq2bTxRN48MVihkNcT2HYTa17AEW-AUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس مجلس: پیام رهبری نقشهٔ راه مجلس برای تحول و پیشرفت کشور است
🔹
حاجی‌بابایی، نایب‌رئیس مجلس:  پیام رهبر معظم انقلاب، نشان‌دهندهٔ تراز واقعی جمهوری اسلامی ایران است.
🔹
این پیام در تمامی ابعاد دربرگیرنده این حقیقت است که جمهوری اسلامی ارتقا یافته و تراز آن در سطح جهان تغییر کرده است.
🔹
رهبر معظم انقلاب فرمودند که باید مراقب بود اختلافات چه موجه و چه غیرموجه به تنازع تبدیل نشود. یعنی همگان باید پشت سر مردم حرکت کنند و در سطح جامعه، یک‌پارچگی و وحدت حفظ شود.
🔹
نمایندگان باید پشت سر مردم حرکت کنند، تراز خود را با ملت هم‌سطح سازند و با حفظ انسجام و دوری از اختلافات، مطالبات مردم را در قانون‌گذاری محقق کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/438570" target="_blank">📅 12:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438569">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
سرویس امنیت فدرال روسیه: یک حملهٔ تروریستی در شهر نووروسیسک خنثی شد
🔹
براساس اعلام سرویس امنیت روسیه، یک عنصر وابسته به اوکراین که قصد داشت یک قطار مسافربری را منفجر کند بازداشت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/438569" target="_blank">📅 11:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438568">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13449f07bf.mp4?token=j1RnSv-o7viI682befvpaVm3xZ7J8aJqLUeADKgXQwuguMXZNwzJzkDjwOCOsTqJ2sXxsAqfiUuDUjj7hVH44j6JxxFuGQ_8fd5hKqYroFUFhZAqipMx0shWTFo4MAtJXFfbSqNeUTrlXTFEu4tlQ_0zT01U_tgGvHWUg76WiM0dcdD19Jd5kMMcWBLt6LI2Egg5N8ScO1KB1JTXrZ3rpoHDgPDytilIyJIH7k4tA7VuefBdjFElrZywQNG8QngcKlXJRecUy8mRbvzhMYTtopN9X-3GAtUUmJRfJ4BL3BY_KjoXGBNjLNWwsD40bpKGtqgRPrG90fUDvjft3AYH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13449f07bf.mp4?token=j1RnSv-o7viI682befvpaVm3xZ7J8aJqLUeADKgXQwuguMXZNwzJzkDjwOCOsTqJ2sXxsAqfiUuDUjj7hVH44j6JxxFuGQ_8fd5hKqYroFUFhZAqipMx0shWTFo4MAtJXFfbSqNeUTrlXTFEu4tlQ_0zT01U_tgGvHWUg76WiM0dcdD19Jd5kMMcWBLt6LI2Egg5N8ScO1KB1JTXrZ3rpoHDgPDytilIyJIH7k4tA7VuefBdjFElrZywQNG8QngcKlXJRecUy8mRbvzhMYTtopN9X-3GAtUUmJRfJ4BL3BY_KjoXGBNjLNWwsD40bpKGtqgRPrG90fUDvjft3AYH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت پرندگان مهاجر به جزایر دریاچهٔ ارومیه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/438568" target="_blank">📅 11:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJNVx_Ui1Wl0hNdIpSyPXeVDwn0f9I87YOOv_N9Crt7P_tFfDjjH9QmsTt1Uiq9ZnoQ6zHP6AEPyyjz85pvIKQUbSD0qWBxzUF0qhqXQQBFt-__EfcmLQSqjXBoKhaAoO-hQwKRA35kkPjQ5DPYEr_3C9OA6HxUQOL7uP_jF_85jGonolZyPYMnYyXauq9MVBaBrgxDS_YbV1UYfhGBcXZYADvgboTSlcIvHaSyqwzN_4zVToNkRrKubtxrgD9d5noS6qsMa53QHb_r8S0OAE5kEfncxRqiDiJPpEZG24XWJB3nTsF1mPUpzmC3HLZPPOye2ervjvAbjp_M0a6983w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش‌وپرورش: امتحانات در پیام‌رسان‌های داخلی ممنوع نیست
🔹
رئیس مرکز ارزشیابی آموزش‌و‌پرورش: مدارس برای اخذ آزمون‌های غیر حضوری می‌توانند از انواع پیام‌رسان‌های ایرانی با اولویت شاد بهره‌برداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/438566" target="_blank">📅 11:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
همه آمده بودند برای عرض تسلیت به رهبر معظم انقلاب
🔹
مراسم یادبود خانواده امام شهید و رهبر معظم انقلاب اسلامی، عصر دیروز در مصلی حرم حضرت عبدالعظیم حسنی (ع) برگزار شد.
🔸
همچنین این مراسم امروز از ساعت ۱۶ الی ۱۸ در آستان مقدس حضرت عبدالعظیم حسنی (ع) شهرری برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/438565" target="_blank">📅 11:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAFTZn494BX0hc7waegOLzpyb6WE59Cl569-LUu_pUfrhffcXs9J3CiMyD_zbCBEy_lwpY1mlj0_Iuoiw4YwQfejkZstbdQL3ApUUIuD1HdptcBh-3D4-ONRa7cjduRUOaI0Fe6WJf4JRx2abDkJPbMR5S2kEl3AjTc08g1aBTb58GciAvMQShuK8au7QVWpNm_q1dH_X1FW0jRNcLzbtnCuhOe3-1EpR91x8U8R7UMBCHZJGJA7j4PHNRQmRCdp16_uJqP38GeKPgus5CtkqZVgVUJQ5cTv889rXtpItus-5zr3B46r1oOmN7GfUeHZYIQ5GE82LS1SFyGcl5c1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار کوبا دربارهٔ تهدید روزافزون تجاوز نظامی آمریکا
🔹
معاون وزیر امورخارجهٔ کوبا امروز دربارهٔ افزایش خطر تجاوز نظامی آمریکا به این کشور هشدار داد.
🔹
ویدال، با اشاره به افزایش فشار اقتصادی و تشدید تحریم‌های آمریکا گفت: خطر تجاوز نظامی آمریکا علیه کوبا هر روز بیشتر می‌شود.
🔹
این دیپلمات کوبایی گفت: جنگ اقتصادی که بیش از ۶ دهه پیش تحمیل گردید، در ماه‌های اخیر به طرز بی‌سابقه‌ای تشدید شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/438564" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f691a6ba.mp4?token=B0jnk2A5NrUVtUAU28aYQbvpeYjAx26lDLST4YQC2ZpGvizTIQlz_SOgIKOp_I4t9LeCtmH37O3ibOFn3HJHJgltbYvD8x5F4Uumn3CSqCU-ADOsfH5ep3zjddvs4XqDhqhgOHXB0yUJPStBVWgOryVgkXMqZy-AOf8cvfz_plZIN20UsRSoUXl_naxkA6oKupr0NeZpFYEJ9y03K_ddfsXsdhWnJwmRY1zbfedu2VB3Jg545m7V-Bpotxda6A-UX5DK6sK2RzhxEaspy5COgqPvIYsTHyd7TVFD4gXnndUkO8yFMQy6Yily_yhZiTBJqrOye3Lj67w76NgPxWOJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f691a6ba.mp4?token=B0jnk2A5NrUVtUAU28aYQbvpeYjAx26lDLST4YQC2ZpGvizTIQlz_SOgIKOp_I4t9LeCtmH37O3ibOFn3HJHJgltbYvD8x5F4Uumn3CSqCU-ADOsfH5ep3zjddvs4XqDhqhgOHXB0yUJPStBVWgOryVgkXMqZy-AOf8cvfz_plZIN20UsRSoUXl_naxkA6oKupr0NeZpFYEJ9y03K_ddfsXsdhWnJwmRY1zbfedu2VB3Jg545m7V-Bpotxda6A-UX5DK6sK2RzhxEaspy5COgqPvIYsTHyd7TVFD4gXnndUkO8yFMQy6Yily_yhZiTBJqrOye3Lj67w76NgPxWOJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرسپولیس پیگیر جریمهٔ سرمربی استقلال
🔹
پرسپولیس درپی اظهارات اخیر مطرح‌شده علیه این باشگاه، شکایت رسمی خود را علیه بختیاری‌زاده، سرمربی استقلال، به جریان انداخته است.
🔹
مسئولان پرسپولیس معتقدند صحبت‌های مطرح شده از سوی سرمربی استقلال، کذب، توهین‌آمیز و خارج از چارچوب حرفه‌ای بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/438563" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1805f0696.mp4?token=COTEUa8gy6YLp8hxT0AEbGAj1eNba-k81b2ePgbZ7imb8lSTYel-xBy32MCiBLBw0mJOPBTluvvYqNGY1s3sRzP4OHzEWSgMUBXDj8-1Jz7Rx1oJ814n-JPLU3mGUraCKyK_XerfcNstxHVXd23TrX9M04PK5mZlPYjZOW8KjSy8JLaLtb3lir0q6NqqG6YgSnAAk2MrU28rF-urrh9p9G7wuVTfZmExaA8ZEdQCimyOHbFipQA1i98Z41gQ-cOM6t86ejiHI9tCK0JXpePTPDnbZpqFO2-c4EKMIm2k_MogLnAxgGT-tJzZOEKm-D0tdjdzkBjFlq3fT-WL1Ll_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1805f0696.mp4?token=COTEUa8gy6YLp8hxT0AEbGAj1eNba-k81b2ePgbZ7imb8lSTYel-xBy32MCiBLBw0mJOPBTluvvYqNGY1s3sRzP4OHzEWSgMUBXDj8-1Jz7Rx1oJ814n-JPLU3mGUraCKyK_XerfcNstxHVXd23TrX9M04PK5mZlPYjZOW8KjSy8JLaLtb3lir0q6NqqG6YgSnAAk2MrU28rF-urrh9p9G7wuVTfZmExaA8ZEdQCimyOHbFipQA1i98Z41gQ-cOM6t86ejiHI9tCK0JXpePTPDnbZpqFO2-c4EKMIm2k_MogLnAxgGT-tJzZOEKm-D0tdjdzkBjFlq3fT-WL1Ll_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: آتش‌بس با ایران همچنان برقرار است
🔹
ونس: اگر وضعیت فعلی جنگ با ایران را با ۵-۶ هفته پیش مقایسه کنید، به نظرم کاملاً مشهود است که آتش‌بس تا حد زیادی برقرار است.
🔹
در زمان برقراری آتش‌بس گاهی تنش‌های جزئی و پراکنده رخ می‌دهد.
🔹
این نوع آتش‌بس‌ها همیشه تا حدی پیچیده و بی‌نظم هستند؛ گاهی اوقات نیروهای رده‌پایین با مقامات سطوح بالا هماهنگ نیستند و ارتباط درستی ندارند. بعضی وقت‌ها هم افراد مرتکب اشتباه می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/438562" target="_blank">📅 10:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مسیر جنوب به شمال کندوان مسدود شد
🔹
پلیس‌راه مازندران: جادهٔ کندوان در مسیر جنوب به شمال به‌دلیل ترافیک سنگین از ساعت ۱۰ صبح مسدود است.
🔹
۲ ساعت بعد، از خروجی پل‌زنگوله اجرای یک‌طرفه شمال به جنوب را خواهیم داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/438561" target="_blank">📅 10:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gqg3l1tkDeVJPAC_Y2aEJ3mKVj6ywrglXV9tCiIt-HIgtD-paFROAsmviegAXBW2eG_LI7fa9z_lEiUGUFiJ58nhggwpVAp6CLdAYwPdmNO4DJ2wvT9EX19ktqnodp33JVIPKzaVhwOmwmv6dkHk3q0UbmHiU7MdsaWvnbOe4m3bBwBM5IeTRzhYOF9ipEd5ONAb9vNaeHLZ7zdOa1F4cacnkP1KUWpATZm7rfVshu8Hq2-p7S3EyS-sjfS2SFgOrZ_eAMm6oR_Yvf3_KHk9fvpK8W3p1fcY_MHtOAMAcDzdvUKlJftazjZZ2Vc3yWx901hmgwfgSIuMMx4ZFkN2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1EOIqieUyJu1i1k27V0wTaGfgWW0Pag_Q1FnmQABdVf7ay3uG2Hub8y2oE_S6p2GtbU9X7DNtazCvcPdB7dCVvbH312KhI_HlM2UcFkjuecV9lVkB_TXtugE9pppK5TlSyz5-G-8EWklz2hclZKMQz2oV2ZvBsK2ZdVbmd5f1O-1oP13dJ7O0ic5gd-9g1kFjyTwWmJC0bguFsZg7RG9IfYjVj0_sLlMItcW9iucBlYz25_clcea0Zq0x0gNeWsK51fl3GuEGACD2wxLCBTMHy544srJa-t0SpwcbMTugxRi7yafQuhiUSCd5hkIp_PCzyuEeSCzn8BT5EbdmZruA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرواز هواگردهای آمریکایی در خلیج فارس همزمان با شلیک سپاه
🔹
سایت فلایت رادار گزارش منابع ایرانی از پرواز هواگردهای آمریکایی در خلیج فارس همزمان با شلیک سپاه پاسداران انقلاب اسلامی را تایید کرد.
🔹
فلایت رادار گزارش داده، تقریباً در همان زمانی که رسانه‌های ایرانی گزارش دادند سپاه پاسداران انقلاب اسلامی چندین موشک به سمت «اهداف مشخص» در جنوب  شلیک کرده است، یک هواپیمای گشت دریایی  «پی-۸ پوسایدون» نیروی دریایی ایالات متحده و یک تانکر «کی سی-46 ای» نیروی هوایی آمریکا بر فراز خلیج فارس فعال بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/438559" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f155c68e68.mp4?token=dOMai_8PgKmDRhPnWBDshVpPDvhk28mdakjmtQymkDY76AWTNf9hCBwfvraJo5D5kb5JrdoL55mnsXkuiksXye61PSnQXAJEMMJGInAxtqx3F8Y7OfsWKeR251dPyqYByrLEr_eRVkjQUFN0JOPPGCVWEulqpIB89Yrlgs4ia5_71RW77Zf11q_iKOBCXLujw4or033JhdGQFU7heGvdLj-3jqUddTjdS7x3KJAoldd08xOy0kTg9sX4TY--Eci_B56IYs-ee4BT-EopnBg2EhaDUFAkAu7xeNytoHVmbdervs1fByoC-XhD3lJP3AQbaIerELuMoBPEgvtbnbTqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f155c68e68.mp4?token=dOMai_8PgKmDRhPnWBDshVpPDvhk28mdakjmtQymkDY76AWTNf9hCBwfvraJo5D5kb5JrdoL55mnsXkuiksXye61PSnQXAJEMMJGInAxtqx3F8Y7OfsWKeR251dPyqYByrLEr_eRVkjQUFN0JOPPGCVWEulqpIB89Yrlgs4ia5_71RW77Zf11q_iKOBCXLujw4or033JhdGQFU7heGvdLj-3jqUddTjdS7x3KJAoldd08xOy0kTg9sX4TY--Eci_B56IYs-ee4BT-EopnBg2EhaDUFAkAu7xeNytoHVmbdervs1fByoC-XhD3lJP3AQbaIerELuMoBPEgvtbnbTqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله: مخفیگاه‌های دشمن اسرائیلی را هدف قرار دادیم
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/438558" target="_blank">📅 10:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAHCToBeQXVOQ8twmVuA6Rw5c5fOSHxtpaRZlZpEq-_xpwizgnZtXKtoCwVahr1ivju_vJy8pU_C1Px0YsyMw4Jh9u8xHtKKvf9e1Mw4xMCmA37hBqfo2D_hnNbWJ7jylglfOkpOqyueR04BiCTCL4yb8CVyTJ_s3p-7uMrGV0i0-TalR5u4qJcR5YF0JMKDbGDtw2YJRVPe7DYwoyvRWzUc1ci2Z8tRXDQYr_uC1ON2BbUesOcVB2gLWMYrI7AXxiVVgBAzRiqgAEXmgag1z4lUOxx3-5tWxqHiEYE0ZHQ8svSuCfuW5kca3LzJEsaMNbbZYaJ70FfsxkutQ591lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأکید سخنگوی وزارت خارجه بر همبستگی ایران با لبنان
🔹
بقایی ضمن محکوم‌کردن حملات رژیم صهیونیستی به مناطق مختلف لبنان و ضاحیه بیروت بر همبستگی کامل ایران با لبنان در مسیر دفاع از حاکمیت، عزت و استقلال این کشور در برابر حملات توسعه‌طلبانهٔ رژیم اشغالگر صهیونیستی تاکید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/438557" target="_blank">📅 10:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7db7e8719.mp4?token=PvF9KpyLKhRpWAmD18jNuAhvqM_kBZn_HKp0kRfCtAN3_Uy2gSeNibVCXKlWw49lrg-gEOKi_cG3DWE8_ko8iakj_Or2IxcRVXDDe1LAEmabpOVU19oWLLDVXDHvJEqKjalqiiOMtrpyQ5sPYcK8xw5TlRa63_xhHHH-YNvIu52hdsuWfKhAVPGcFwjPBliLt9tbRj1NdaG4dx1LMuid1F1aINggdpZz8GJ6dWYXObfamnjCUBNo1Si3MR_azmZrM-MA7LtZquLdCuXJcQlbWY-TDmH3IbJOCrsyAokLj48XZIgaRFBSC2AvwvkP0IUY-3rz3otl0wWrCmmFXryZ8Xcc0I_JQ5jkRUV3dJq4yMvkse36cpvim6kxWJT9MySBf5JGR0wtxdJvRMNu6J5fm2tADRSD5K3a_MMTPqgjTcBvbFTf6IhvOK2Jx5rPG5ietk357w4-3v4MQG8uAlx9JzAVMRxau3sBiPHSgzMGVk9_X1OfaZbYJGuMmSDhJrx63ytqjCXriISP6BpQ8pap56Fc1o7vTmflI2cRnejs0HOCRByqmL5me__4gjXz5jPcUS8mhdPPXIv-6hx193sCrU2016uMMW_007jjI5yNcDSNYmTk1UmCt0UEq2IzwgYgRQ-T1EmcrunuGxdPfqDruBp9PFR3zGBKNDRIzysM9gE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7db7e8719.mp4?token=PvF9KpyLKhRpWAmD18jNuAhvqM_kBZn_HKp0kRfCtAN3_Uy2gSeNibVCXKlWw49lrg-gEOKi_cG3DWE8_ko8iakj_Or2IxcRVXDDe1LAEmabpOVU19oWLLDVXDHvJEqKjalqiiOMtrpyQ5sPYcK8xw5TlRa63_xhHHH-YNvIu52hdsuWfKhAVPGcFwjPBliLt9tbRj1NdaG4dx1LMuid1F1aINggdpZz8GJ6dWYXObfamnjCUBNo1Si3MR_azmZrM-MA7LtZquLdCuXJcQlbWY-TDmH3IbJOCrsyAokLj48XZIgaRFBSC2AvwvkP0IUY-3rz3otl0wWrCmmFXryZ8Xcc0I_JQ5jkRUV3dJq4yMvkse36cpvim6kxWJT9MySBf5JGR0wtxdJvRMNu6J5fm2tADRSD5K3a_MMTPqgjTcBvbFTf6IhvOK2Jx5rPG5ietk357w4-3v4MQG8uAlx9JzAVMRxau3sBiPHSgzMGVk9_X1OfaZbYJGuMmSDhJrx63ytqjCXriISP6BpQ8pap56Fc1o7vTmflI2cRnejs0HOCRByqmL5me__4gjXz5jPcUS8mhdPPXIv-6hx193sCrU2016uMMW_007jjI5yNcDSNYmTk1UmCt0UEq2IzwgYgRQ-T1EmcrunuGxdPfqDruBp9PFR3zGBKNDRIzysM9gE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با شهید سراجی‌نژاد در حرم بانوی کرامت
🔸
شهید اعظم سراجی‌نژاد ۲۳ اسفند سال گذشته در حملهٔ دشمن آمریکایی-صهیونی به منطقهٔ مسکونی به همراه همسرش به شهادت رسید و پیکر او به‌تازگی کشف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/438556" target="_blank">📅 10:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWE-_WT_Bvl8QyJ4Fbnk7up7dN3MgQIXmVDtUhXyaTHlyuafA8EyOMELpOC5-FKLVL9WdGomQSSfl_xqGMpne9pFa7eipFt37uBug0-B5n-lxPOpf4612YTioRJGmdPBCtDgpjTykr-ieBEzjS7MIgpX-RrTcxGp_xqEIfkyXcQrmr7JnuFXLalIFVkgOHCJr5Ivobqq5mGVGpdMweh0VO8JpqNxr9UYt6fWfDI7FrrX62yfsPmpC2ajcihYcYG2Gh7kY46y1ytkJ_Zh3uheSXguLaRRcOep9qCMDVXpQbWRqnPUbxWdXR9FfdYnXsj5wte3rBB4uduiA7_GMAaidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری فایننشال‌تایمز از بحران مالی شبکهٔ ضدایرانی «اینترنشنال»
🔹
روزنامهٔ فایننشال‌تایمز در گزارشی از ابعاد تازه‌ای از بحران مالی و ساختار پنهان تأمین بودجهٔ شبکهٔ «ایران اینترنشنال» پرده برداشت.
🔹
براساس اسناد منتشرشده، «ولانت مدیا» شرکت مادر این شبکه به‌دلیل زیان‌های سنگین، ناچار به دریافت کمک مالی و بخشودگی بدهی ۶۵۰ میلیون پوندی از سوی سهام‌داران خود شده است.
🔹
طبق این گزارش، شرکت مادر اینترنشنال طی ۵ سال گذشته بیش از ۴۱۰ میلیون پوند زیان ثبت کرده و تا پایان سال مالی ۲۰۲۴ نیز حدود ۴۸۲ میلیون پوند بدهی به نهادهای وابسته داشته است.
🔹
فایننشال‌تایمز فاش کرد که برای جلوگیری از ورشکستگی کامل این شبکه، در اقدامی بی‌سابقه بیش از ۶۴۸ میلیون سهم جدید صادر شده تا بدهی‌ها به سهام تبدیل و تراز مالی شرکت حفظ شود. این اتفاق درست یک ماه پیش از اغتشاشات دی‌ماه ۱۴۰۴ رخ داده است.
🔹
این گزارش همچنین از انتقال ۵۰ هزار سهام شرکت مادر اینترنشنال از «عادل عبدالکریم» (فرد انگلیسی-سعودی) به یک شرکت در جزایر کیمن خبر داده؛ شرکتی که تنها مدیر آن «صالح حسین الدویس» از مدیران ارشد «گروه تحقیقات و رسانهٔ سعودی» معرفی شده است.
🔹
فایننشال‌تایمز همچنین اعلام کرده ایران اینترنشنال برای دورزدن قوانین رسانه‌ای انگلیس، با توقف پخش ماهواره‌ای در این کشور، از نظارت کامل «آفکام» خارج شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/438555" target="_blank">📅 10:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-lIaaOdrnP_gtn-2PmWchrzvKMXKhj7J8ADUrSf-eGLgBezNwXENSxSS_Kc33f_BnLkLP79Zoj8rld5PMR3y8DnRGlvEF6Rq1P63Nch3FavLJH3m1W9qHOL5CUHVjuCIC6T5Y4eOLLiaMrcBSdrIWXX65hR8eKoSLktSe4HCxIbqG3YLq35XHz6rdQtsem_ZXyqyA6cCEuGRGyXwTBKzgULEydE9kw78mWeRFQap9OW7Yw8xyzR_iqQB3e6J2NTuk2ecKvpMeu08R8iBWrq-xQ-UwM_P4YBEuoht_eI6sF0LeiOjPbpxqCNXPRMSkoPN9OLeIQZEAAsOoZbx2H97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ عبری: ایران شکست نخورده و حزب‌الله فرونپاشیده است
🔹
معاریو: ایران شکست نخورده و حزب‌الله فرو نپاشیده است. در این جنگ تنها یک طرف پیروز شده و ظاهراً این طرف نه آمریکاست و نه اسرائیل.
🔹
۳۵ درصد از افکار عمومی اسرائیل بر این باورند که اوضاع امنیتی پس از جنگ علیه ایران بدتر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/438554" target="_blank">📅 09:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKs4x0CZN7tR2AoMjQorucfq1IOEbOd_0KdFw6w7mYlgt4AklCMCQ_DcR9RBytQ3LL2eTvvvIKS6fr0UaQG-FQWGORPCPoHykcAD4hNEkBk6QQBBRcU7AwSO7bROtwq1J1NS3cm9gaMYkUHrNEx9APHsc71OOkVE9EmDt_PNpEbrzvaEaT3GhVVdCXWlJjpqdA1ETohKXRM3DzGFNLsoAqBfIhOWRRZDwefyPv_oiY2AeBjNN5Vc0CoN3L4tSfxyM9lAxDpZTgJIGhiQiwpxiN19iRFCYQk1Izyb-hVWhQUEZ7LRnqnGu7ks35W3e-6naSUlNypiZ-YjlPFrsl0AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۰ هزار زائر از مهران وارد کشور شدند
🔹
مدیرکل راهداری ایلام: بیش از ۱۰ هزار زائر و مسافر پس از شرکت در مراسم معنوی روز عرفه و زیارت عتبات عالیات از طریق مرز مهران وارد کشور شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/438553" target="_blank">📅 09:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs3IhCkVwQCd9xWAjTn6olmy0BCDbe7sMz2kw2-0Pst22qKliLVgTVZvx76l3QkWgm4ct0OUJoXxs6Zrn2pWNinF3ZNSrD0EeXP0HwvcYr2UyWrhb-dfMdcAiSdcZVJNVuLqbCIyveg6ET50oUwFOUR_POx87-IVq7HGmQ8S_Nxfm4d2CwwGURnCpEmMl5FRHNJVT5VVBdcRcWpyeRPHysjPin-j0okl0l8ovvhBBD1xbU71zAbEHOgh8yy7pypgUsRAYyGWx9DamCDAVMFqC-DvpXkiAxv74JQQ_hBTxt5v1hKT1X0r99y6-d1CuCB979QPcINmazpNf34BUB2QpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمرهٔ هوای پایتخت قابل قبول است
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران شاخص هوای تهران امروز در روی عدد ۹۵ قرار دارد.
🔹
تهران از ابتدای سال جاری ۱۲ روز هوای پاک، ۵۵ روز هوای قابل قبول و ۲ روز ناسالم برای گروه‌های حساس داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/438552" target="_blank">📅 09:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مهلت ثبت‌نام کنکور تمدید نمی‌شود
🔹
مشاور رئیس سازمان سنجش: مهلت نام‌نویسی کنکور امشب به پایان می‌رسد و این مهلت تمدید نمی‌شود.
🔹
داوطلبان برای ثبت‌نام باید تا پایان امروز به سایت سازمان سنجش مراجعه کنند و ثبت‌نام خود را انجام دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/438544" target="_blank">📅 09:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=uWiJfrkr6OrGdpCGuPx-IW6ltmn3t1LCWYn1YZRx__wH50kf_14wQqqdHUSorKYm4KhBqIA9GBZIaPJC1koMIhvGE4we6EbhYFTHu4CA4w5cRkfupkfYD-_4HXcDo0lF4Ys37nBB5d-SlF_xwXh4WJ7pacB8BOIZB1qrM7rPCkA-VCAb1RW2qWG5wpTc__FuUHLhtQBStPFsZ_p1uA6UsmMIrbPsSMB_C3HSSR9kgUw2vmzliH0nWHKxyR5T4TmNarLvNCneSxJ9kNeQh8ZN0OBSLyV7KO-OoHn8jSpIlCI-GS5DJhq7xTI_EMugv5pYpJ2iqjcsvkRcnJ8nJgs25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=uWiJfrkr6OrGdpCGuPx-IW6ltmn3t1LCWYn1YZRx__wH50kf_14wQqqdHUSorKYm4KhBqIA9GBZIaPJC1koMIhvGE4we6EbhYFTHu4CA4w5cRkfupkfYD-_4HXcDo0lF4Ys37nBB5d-SlF_xwXh4WJ7pacB8BOIZB1qrM7rPCkA-VCAb1RW2qWG5wpTc__FuUHLhtQBStPFsZ_p1uA6UsmMIrbPsSMB_C3HSSR9kgUw2vmzliH0nWHKxyR5T4TmNarLvNCneSxJ9kNeQh8ZN0OBSLyV7KO-OoHn8jSpIlCI-GS5DJhq7xTI_EMugv5pYpJ2iqjcsvkRcnJ8nJgs25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راکت غول‌پیکر مالک آمازون در سکوی پرتاب منفجر شد
🔹
راکت «نیو گلن» متعلق به شرکت فضایی جف بزوس (مؤسس آمازون)، در جریان یک آزمایش زمینی در پایگاه فضایی فلوریدا دچار انفجاری سهمگین شد.
🔹
این حادثه برنامه‌های فضایی آیندهٔ این شرکت را با تأخیر چندماهه مواجه خواهد کرد.
🔹
قرار است این راکت در آینده، ماهواره‌های اینترنتی شرکت آمازون را به مدار ببرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/438543" target="_blank">📅 08:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7njao9RApmVY3ciRRUqpxTBTbIY95XHIG5TKdiztPR-pHwqsAkb52UVBQUZNOCUeoKWeY1dFhykKs3PA0v4WZ3SuAbvEtAtEj0ldAcYFuZcn5QkSe70-u_htY_I800qAIFVl9j-f3uoqDpp8iFj9B79TJkMfFuzGImEjUyrV1LENZGkAj3ex6C1IjMQh8H9NLabZvVusU5fxFsAWvJ1ANCMrXhBSYqVL8BuH3IvWnW5tyIwpVESOSGbssXFgmiH5ouEYS8BvIpm7fg-dOd1JxaAjUlRct6TeSBIB60v8sDNY62hBGOMzl1ln1GYMj2h1g4biehEiyMpv4sZlNiPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران ١۵ پله بالاتر از عربستان در جام جهانی
🔹
سایت مارکت اسپورت به پیش‌بینی شانس تیم‌های شرکت کننده برای قهرمانی در جام جهانی پرداخت که ایران با  شانس ٢ درصدی در ردهٔ ٣٣ از لیست ۴٨ تیمی ایستاد.
🔹
در این پیش بینی جایگاه عربستان به عنوان پرهزینه‌ترین فدراسیون فوتبال آسیا با بیش از ٣ میلیارد دلار هزینه ١۵ پله پایین‌تر از ایران در رتبهٔ ۴٨ قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/438541" target="_blank">📅 08:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438539">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7rXvRM4tBWmo9KVSC01G-xC2EmqWw7Z-XLFRD_23EezJzJ7Sz-2xVBvhYM2BrTd_JJaYpZV0u2Jti_HIizhwVYEHjlReAqXA16jMj9vB7kGZ7m3b1blkgdE-632JPmjgi-Rhf2L_WWeecgKqoa_1f6cN2BwlumG9lghLecRwYrGb9JhbmWj_KnY5Fq7WajSGCK81jx92Xc8lviq06sZergQI3wetBpdssIkJ69VsfeoVYeHQ-JmcY9q6T-nJOi4UJo4BOrStO7Gc24U15L8sJXE9i1RsiKNmtA9IxNiQhpxi-WioL-uoH172Ieq9grJGuDUCnprArdzqGkuRMW-dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: سیاست ایران گسترش همکاری با کشورهای مسلمان و همسایه در همهٔ زمینه‌هاست.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/438539" target="_blank">📅 08:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438538">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5ed22e97.mp4?token=dKQfzNqB4cm2GENAnVWXBhfTbXU6wh5JssIyML5kX4ktdrWs0X-rArWwDEt10Sb8CUB4M9mjT7cMw2beNqPLeo7AMbAc16oUYC4_LjefR4lAU4w3L9hmCRG0VVFTXqjyLQUdIZFPbhKdwbkcMSaboAR2RSVt6Qz6qdqAcdLBPEWKgh6HQrQQ8qmCMcfxVUcqSJhKS9gi63gIbznVZwgYdV0vOd7vIhiUlMgkQdnND_RF4OdYKUOolIkJ-UaxBolw-JFmmooPt-P0WmylaX5YGksMazxP0BHc5O4u2g9LfW8mblJfB1iArlzaZMONQA2JcGdVAcB55CHMP4AtG8KEpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5ed22e97.mp4?token=dKQfzNqB4cm2GENAnVWXBhfTbXU6wh5JssIyML5kX4ktdrWs0X-rArWwDEt10Sb8CUB4M9mjT7cMw2beNqPLeo7AMbAc16oUYC4_LjefR4lAU4w3L9hmCRG0VVFTXqjyLQUdIZFPbhKdwbkcMSaboAR2RSVt6Qz6qdqAcdLBPEWKgh6HQrQQ8qmCMcfxVUcqSJhKS9gi63gIbznVZwgYdV0vOd7vIhiUlMgkQdnND_RF4OdYKUOolIkJ-UaxBolw-JFmmooPt-P0WmylaX5YGksMazxP0BHc5O4u2g9LfW8mblJfB1iArlzaZMONQA2JcGdVAcB55CHMP4AtG8KEpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره حامد شاکرنژاد، داور برنامه محفل از اولین دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438538" target="_blank">📅 07:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438537">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران ممنوع شد
🔹
براساس هشدار هواشناسی، از بعدازظهر جمعه تا اواخر شنبه ۹ خرداد، وزش‌باد شدید، رگبار، رعدوبرق و کاهش قابل‌توجه دما آسمان مازندران را تحت تاثیر قرار می‌دهد.
🔹
به گفتۀ مدیرکل مدیریت بحران مازندران، اسکان و هرگونه فعالیت‌های تفریحی در بستر و حاشیۀ رودخانه‌ها و ارتفاعات این استان در این‌ بازه ممنوع می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438537" target="_blank">📅 05:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438536">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">اظهارات طوطی‌وار ترامپ درباره ایران
🔹
رئيس‌جمهور آمریکا دونالد ترامپ در مصاحبه با فاکس‌نیوز ادعاهای اثبات‌نشده‌ای را که بارها درباره ایران مطرح کرده دوباره بازگو کرد.
🔹
در حالی که دونالد ترامپ موفق نشده اهداف نظامی‌اش را در جنگ علیه ایران محقق کند او مدعی شده ایالات متحده ایران را از نظر نظامی شکست داده و به همین دلیل «همه برگ‌های برنده» در مذاکرات در دست آمریکاست.
🔹
او تأکید کرد که هر توافقی با ایران تنها در صورتی امضا خواهد شد که «معامله خوبی برای ایالات متحده» باشد و این «خط قرمز» واشنگتن است.
🔹
ترامپ همچنین بار دیگر مدعی شد که نیروی دریایی ایران به طور کامل ناپدید شده و نیروی هوایی ایران هم کاملاْ از بین رفته است.
🔹
وی همچنین گفت:  «اگر نه ماه پیش ایران را با بمب‌افکن‌های بی‌۲ بمباران نکرده بودیم، آنها اکنون صاحب سلاح هسته‌ای می‌شدند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438536" target="_blank">📅 05:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ec776bf7.mp4?token=NQCz4G3HQjVEtiECpReF2MVJ82C8b-XwWeob6oisGQWB7tMhDLSuNwFOIXREhQHuPX9hkMsJXSnUbbi1-lx8wZ9EC40WLE-sANK9M5WfFw9e5pMFaY5uNdCVjnLNifiwDR8gs5NQuufwsPCq8uxhNJK5yOoEVAYYhnCG0r8vsOaglhwPZbcmAN1n0w9xGFr59mhqacbkHzoy73SWd69wN8_Vg2ZePi77eZr6Pr-KdzJGeHxUrQKkGJk2OhitPxsq-AjWQR4cbArCqYrmKMFqmxOUWcB7TGT84Wvl19G1LyW5Y-nQA0ygCbhUFkaL_2RlK1wBzBIALxvSCUnjhwWIwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ec776bf7.mp4?token=NQCz4G3HQjVEtiECpReF2MVJ82C8b-XwWeob6oisGQWB7tMhDLSuNwFOIXREhQHuPX9hkMsJXSnUbbi1-lx8wZ9EC40WLE-sANK9M5WfFw9e5pMFaY5uNdCVjnLNifiwDR8gs5NQuufwsPCq8uxhNJK5yOoEVAYYhnCG0r8vsOaglhwPZbcmAN1n0w9xGFr59mhqacbkHzoy73SWd69wN8_Vg2ZePi77eZr6Pr-KdzJGeHxUrQKkGJk2OhitPxsq-AjWQR4cbArCqYrmKMFqmxOUWcB7TGT84Wvl19G1LyW5Y-nQA0ygCbhUFkaL_2RlK1wBzBIALxvSCUnjhwWIwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌سازی قمی‌ها در شب هشتادونهم
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438535" target="_blank">📅 04:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s18WrRaOzCsLgHyFPFk1p0ja2exGl0xriXde23jdtrmH_wYOZopuMzGUyqIwR-HqP9Jbw0p-z9m5EIx5_Oo5XS9OMEHR_Wb83FpuZhmhk4-i6pDbu5ctf-BFPPct5EW8NSQ79X_w5g_n4oOVZWifobPMnDFgj3b2-ZpYy5NWu-oirUHPOn-rvvGfvviNtNVE5ld0gkyuHRM38QUm_FjRkWcRn8TO-fy-HpgmWOvH3ebAC6iM1bk2jyUWDz99G0AQT3rbMIUdzKuOohbWeUc1JzkIy4m_zMRiY0U01F196hR7_tuHLj6N4oJzjbn2SbJh4CzKuGBoLIQ7djgl8ySc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاس بیش از ۳۵ نفر در مدارس ممنوع شد
🔹
با اعلام وزارت آموزش‌وپرورش، در سال تحصیلی جدید تشکیل کلاس بیش از ۳۵ نفر در تمامی دوره‌ها ممنوع اعلام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438534" target="_blank">📅 03:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808f313e66.mp4?token=bVu6udAB-V9WJYsPhblt8CgPsc1IA6GYII7ESVRJWuuEHZv-pTmzqoqXcY9-7v1wLMxcAqcsQaGv5_GbBFUp1RptjoI3crkQqFNGE3juz670aQC1v93ihyDhWMfkatHtP1UkNVFE4AacSKfYKkVypjMMFcAGtd96IY1RdZqnVmCtDkPMmQDjLJMLDd-s_xCb8aiGkIshxlSVwBv4pTTrfzVv63At2jGsaHyYEfvvCpwTtbAJDeuOYJ4slU4JDo7H6ctHP37FMUziM5tb-VpGBSFVcX4wGfFDFar2zwK9MPgNsd-Uvswkk2NbCKzYtMYdSF0312fqDvDxIxqtWpMAlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808f313e66.mp4?token=bVu6udAB-V9WJYsPhblt8CgPsc1IA6GYII7ESVRJWuuEHZv-pTmzqoqXcY9-7v1wLMxcAqcsQaGv5_GbBFUp1RptjoI3crkQqFNGE3juz670aQC1v93ihyDhWMfkatHtP1UkNVFE4AacSKfYKkVypjMMFcAGtd96IY1RdZqnVmCtDkPMmQDjLJMLDd-s_xCb8aiGkIshxlSVwBv4pTTrfzVv63At2jGsaHyYEfvvCpwTtbAJDeuOYJ4slU4JDo7H6ctHP37FMUziM5tb-VpGBSFVcX4wGfFDFar2zwK9MPgNsd-Uvswkk2NbCKzYtMYdSF0312fqDvDxIxqtWpMAlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستور نتانیاهو برای گسترش اشغالگری در غزه
🔹
انتشار ویدئویی از اظهارات نتانیاهو در شبکۀ ۱۲ تلویزیون اسرائیل از طرح جدید و گام‌به‌گام تل‌آویو برای گسترش اشغال نظامی نوار غزه پرده برداشت.
🔹
نتانیاهو به‌طور رسمی اعلام کرده که به ارتش این رژیم دستور داده تا کنترل خود بر نوار غزه را به ۷۰ درصد افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438533" target="_blank">📅 03:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzmPWGI_5I8fgggf9jTJ51wJkSCmIKUvNeK9PIps87DlplSO5JstXs3_YbKvP--9QY8f8P4eUZD8u4UmHZZFUEvWADOJBJ206oiC6Tv_YqJBmRP4TpZIgAfEDb_GO8N_75xcxAqwy7lZFvb-mLS0KC6zs7TXj-ljY2YjWsNxQkV26-2cA0kxskpAI-9D5mAmYKn_mARIks10xUMOs0NYT2_ZlSjH75ipx-rshvNZ_oXYD_6Ns73WW-5aCfIZL-BsBn-VbtfSWTvcOT0Kd2QPPJxWeD5D-m0Gvu2YZayXrFaDK4epPpfsLAalrDxFB7UUQ_SFGI2qhWwW2o8c0WU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار اتحادیۀ فرودگاه‌های آلمان: حذف پروازها و جهش بلیط در راه است
🔹
کمیسیون اروپا هشدار داد که اگر وضعیت در تنگۀ هرمز بهبود نیابد، بازار سوخت هواپیما در اتحادیۀ اروپا ممکن است با کاهش شدید عرضه مواجه شود.
🔹
در همین راستا اتحادیۀ فرودگاه‌های آلمان اعلام کرد اگر قیمت سوخت هواپیما به همین منوال افزایش یابد، تا پایان تابستان ۲۰ میلیون مسافر اروپایی پروازهای خود را از دست خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438532" target="_blank">📅 02:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای سنت‌کام: هیچ هواگرد آمریکایی  در نزدیکی بوشهر ساقط نشده است
🔹
ستاد فرماندهی مرکزی ارتش آمریکا سنت‌کام در بیانیه‌ای مدعی شده که هیچ هواگرد این کشور در نزدیکی بوشهر هدف قرار نگرفته و ساقط نشده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438531" target="_blank">📅 02:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C81zeq_IjcgL5ZW4IBPbq14vucDjKvsU6SYdlPhjjP1P7-GGM-_-1YZPPFl3wam8belH2tuqZAU_mA_zLa_mOn2oH1q-Hxbi2EZVwMb9449JBz3lkqJtoS0Qkek_n_2wdC2Z7-XvdTEvM30lHGaGtZcnCHUBBnVbZblaRUTTaJXctxXNKmbXXnBQrPTe8Vm-EFsedPhuJullY2NnBGhOw456Nfg3FDbGStDNWPk6fYVHLJUNw8vEmKfpnPYWMyt6pop0HgjQVqwnUMFmmxQN6SH2usKOaimTaSSaJq45M0rlp7y-DQjrmqVKIZbnvB3H1nsLzBFDHcwREvtan9xVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yv-1Dy_uvp6cnyLrlT0TwJ-JIcXNcjFUKkYMB-Nfq1QPFYuxIkBgQpSeQYT2y1oe0gfmerZG7K92b110KlkRQgpZfUMfUSolXENIKtM6mLYfdKnUx1ejWKFiuBsocqALE7pqSu1ID-va7aOv8hENfbHA1PoFYuKPpeTRlKYY-mx11KRIiqu1MrJ6rW_KRaCJWe-k6Wy5tI_idm_3fzTFQFepmRIepsPHjjnFg7Vr4dsmw001tM855Hv7UDIv17wFIuVDMnt-Zm-TzlKFX5DNNwZGh4w6FEeKMCRjOVxrrQ9N8BLrmY3FMS8J4AXSNT1K6kQ11_CrpOIekUmzePgYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o536YyaT2NHpYCw2CaYKWqeiGzE758adaZRfrDVXu0GGbrM7bN3_rYvpw6viQpGet8c_KUV9RD1W2Z2t1uy-KKkA-n4mDwXgzM93xGGCBhIv4II9UAvSOnj3QbADDFWlmRY1whlnm51hE-Xjz4FI9dcds96uhsy3cjSemDBzdfcgCpmkcfjuobLg_9hq17ADDKVF9ckzqKQVYtik_Z7H1jpCfJMr7yROjdxRaZL9buywYNzqZ84aD352huCD8_7jBqZpjK9qmfVbPeWk-HSJQchpxMJJO9JxWLMQwcIGic-s-Nchh0leAwGt5tGpet8zqnIAeWZ4LKHcsFbGSirdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcZ_bGDD9mOnObmVgGEiZVEk8ipsTOxxTU_wrq5R9D4fuZRNSIA9fhJ8UuDWlzJkdjg8STdwRnPyQCSWidU7LGw26iu6BURwbg0h0G3_kINaokQVrmxegT8Eyhqha_0z7fvYMhsDgsRdA3JS4kp50WGqqmmgepPJTaEJNF1TLX5Ty4jQeFqn3sMZfwxbq-gdswlrzfDvV50tiDeUsHGVzbq9zL9QmDrw_b3BOJMKdsZTd9sz-imAFvBSnWu2Cfk8rz2HIDckCW9bQ11dau78GCFkJdpOeRZzsRu8_9pfsk1shN0II7uIfjhA6_Ttt9NoFKSgHqwfGvvCh67HJEwq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fl6nsgLnIrIc-r-35Gb_C1oOddGS6E_86-ZcBThVFx3eBk1j1fe7MoSHIgx2dBR-p7eeBLlAvinvlt7WAGN1_yyS8C7nZmCoMTbBJ_3TZSWVChyyjlpulK4OXBDxfqKjB0whZC6NHG4prYLS4kBFuzrLY255ytrYTOF8anXtbn3j3L4RguegVLSin0UKHtiS_pUlq2fRMccA6vC09L5MrTb6bMLvFw9wZ_aQ-7relx_vDHRr5sETaQoEeEb3AL10qKN-CCK3tRMj4t8U2z4PRQ3SUYCJ0yCFJt05EWZmJWYkzxXeEIbkhsvA3jJ73Z7cfERAw18gX0FlvbXH8zo2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/il4FDuc4FXPQS8YHzUGW7mGfd54vs7Q9PoI1wh0WE2pXJYrcSIe_xVorGKVx0Ch3B2-duJgZ6ms99n4BIvYHaxyUPdCJkyHxMZuyoO4OMOr4QG-9a5DDnpggnGBBV5yfVK9QLVlraA5L5GLUXdvgVMGYrKrsuKIK-KpCzvBDhh80zUKg0ULCaNPsx2DPBa_RvlNNGh3e60pTrA0VZP_RSxkQq7Q6ynJLXDzSy_0dThFbEaUbSsBtuLVA6BPGjqnUhPbvjTRgSJNOhmPVfQ7YFKccJL3RU9VtJhEXRLKAhfTxKsR5VQhXdO5HL8C09tjNeuEQrJuwdMXU26gfF-1YTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nY8_p_XiNle_D1PgnFVefRjIM2Qmetpy8zof8NoFy1uUz7EurhU69-dvGa_0O8DGYKFX4sJJlfwGTErVmeInQy_x7U82AdjTdqMjI9bGqggK5l8Se4wHwVNrU_tljXnUD1K1i1ZpQtLPRTGG2pKjOQWgeaD6wd_VmKLrzJlMy8UKHY_LaqG1Zls_q_aW935cbQpOj5ZEnYwn6kuNPcZJnVOzhM0t_kxHfrHg29bxfaUeGycdkVZg41SNKgmkZN_UzgSj8vAVhzcLWbaE5DYJ1yYJGZz5LCccIzLUbcbXsiROttCmv_-iU5cwnfHrnuZ8c33iC80owmeF-NAjlQWH_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم یادبود شهدای خانواده امام شهید و رهبر انقلاب در حرم حضرت عبدالعظیم(ع)
عکس:
محمدحسن اصلانی
@farsimages</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/438524" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
حماسۀ فسایی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/438523" target="_blank">📅 01:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5a5cfdb7.mp4?token=jBjQwbSpzMtqMtj_2-46An927EiWB4dEtmuPg1Bhl_GccN3e1EHjJVN5U4MLGVe--O1nVe4lEaF7yleGy59lYt-I-zNdsf8euOAn23JSU3k63GU1omR0ZrtOVs2EKOAtCiTZXBGNwo6J57jnOaOzcmiTzjRwmiEA01JpAIfPzwvFaNEnkF-CqLm5g-VpLPRWgtKoqJ5pKhhhvM-M4LGW4miAOBJIKwkt4z8r0c8eqTtTjbAJQb5AXja0T4oUCwbPcvbOPWQOsuTKJwelsxH9frTqcVkSMSV2bQjkcBh79KgwvGtdyHIn0SocYqTj96B4yd81TvJMd_72DN-ZYNO3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5a5cfdb7.mp4?token=jBjQwbSpzMtqMtj_2-46An927EiWB4dEtmuPg1Bhl_GccN3e1EHjJVN5U4MLGVe--O1nVe4lEaF7yleGy59lYt-I-zNdsf8euOAn23JSU3k63GU1omR0ZrtOVs2EKOAtCiTZXBGNwo6J57jnOaOzcmiTzjRwmiEA01JpAIfPzwvFaNEnkF-CqLm5g-VpLPRWgtKoqJ5pKhhhvM-M4LGW4miAOBJIKwkt4z8r0c8eqTtTjbAJQb5AXja0T4oUCwbPcvbOPWQOsuTKJwelsxH9frTqcVkSMSV2bQjkcBh79KgwvGtdyHIn0SocYqTj96B4yd81TvJMd_72DN-ZYNO3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای نشستگان در مقابل خانۀ خدا، به ایستادگان در مقابل دشمنان خدا دعا کنید
🔸
ویژۀ ساعت شهادت شهید حاج‌قاسم سلیمانی و همراهان در فرودگاه بغداد
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438522" target="_blank">📅 01:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438521">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC_mruw_H0mG1TvZGbSnbyT3m5GQ-QNBXKIKrBZCuCBxqJQiF_Tq2yL1U8am5gEYsAG2NWzA6ALo2usVOC0I2AKMmaTBMqM4UrdAEm-P6R5QFJHdXFohkjc2esCauNsSyzjRpNEXXdcoe1GUb1BlomjI1WEEXiHhcj3cyhh4mhbTwIL6eBTuXD9sbncP9OS1PgpKk3TOrwliMG3JEb9jgwfeZz6sYenwdVF0nAGZ3MYY3zuLw2d_ZR11WGBSdEPNQx3ZkuJltDkCJcQmHFWGTNpWCAryGexLkjLV5k0lU8QM5LmDhYl9yxVTywrejsW0TzsrLWnacNiMuwGIvMWEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز بالاترین تورم ۳ سال اخیر آمریکا را رقم زد
🔹
تازه‌ترین داده‌های رسمی وزارت بازرگانی آمریکا نشان می‌دهد که نرخ تورم در این کشور طی ماه آوریل با شدیدترین شتاب ۳ سال اخیر افزایش یافته است.
🔹
دلیل اصلی این تورم، افزایش شدید قیمت انرژی درپی جنگ‌افروزی آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن اختلال در ترانزیت نفت از تنگۀ هرمز اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/438521" target="_blank">📅 01:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438520">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjAtHPkAF93M46Bb6AWcz05651Ez4FI3zqLvSKwd4RBbpLROv-sb54okkVYUnn6XItj-9bnNtw3NNjZzWXhuTgIQUYB-SrSw2Q0M7YkvbIoXkdO5Ag74jzKb0tRljL9Bdmrt7F32mUmzAlzleCDFtQBR03ei0_homE_v63QefVLmY2F4c8Jb4QBvncBvaOnHCdwEcRxH2-7Mow3Ik4RJ9mHb3Ui4eXtddPI-J1uE2a0_pgQqyUNvhtbIIwIxQbXnJkwpUf3vwOPlIoKAZ4901hF54qCiba4TrTjvGsWkImD-HlKV1t26mbmaNunp-JbQGDULMXFOz-eVRMBJ8bROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه تهدیدهای آمریکا علیه عمان را محکوم کرد
🔹
سخنگوی وزارت خارجه، تهدید وزیر خزانه‌داری آمریکا به اعمال تحریم علیه عمان، متعاقب تهدید قبلی به «منهدم کردن» عمان را تلاش برای باج‌گیری از یک دولت مستقل عضو سازمان ملل متحد و نشانۀ دیگری از ورشکستگی اخلاقی سامانۀ حکمرانی و سیاست‌ورزی در آمریکا دانست.
🔹
بقائی خاطرنشان کرد: تهدید به اعمال تحریم علیه عمان به بهانه‌ای واهی، اقدامی مطلقا غیرقانونی و مغایر با اصول بنیادین منشور ملل متحد و حقوق بین‌الملل است و جامعۀ جهانی می‌بایست با واکنش مسئولانه در قبال این رویکرد، مانع از عادی‌سازی فزایندۀ نقض هنجارهای حقوقی بین‌المللی شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/438520" target="_blank">📅 00:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملۀ موشکی حزب‌الله به محل تجمع نظامیان صهیونیست
🔹
حزب‌الله اعلام کرد، محل تجمع خودروهای زرهی و نظامیان ارتش اسرائیل را در منطقۀ زوطر شرقی هدف حملۀ موشکی قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/438519" target="_blank">📅 00:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی از جنوب کشور
🔹
دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
🔹
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
🔹
برخی رسانه‌ها از وقوع انفجار…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/438518" target="_blank">📅 00:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438517">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmN5XMW0dGEGGc6bYZmH3FGIk9T1HiE9BDAWSrGxE5ShxCWBrwmWkVVbFrQOnA8TFtFqdw_5kB04g_pF0PLh8ltHrcmkFABkRV6Ni4s9HLdHSO0llzLxhqH2U4HoUVu3_gpyEjoteil5BUN6AZ6xMjIZeNuKKMnKSJUYr1_QELqH3swGDeOS7T__NKSFLXwSv74THtkZGdZhlDQ_u5-vhERUQGzs_jCcgQ8ZF06BZJHnH0a1VjNRhLBy5XVUkIpQysZzqRtxSxcfbMWImCdnI2bxNg3XH5D-8s5Af0IHLfnTEg-GAf504GZKfYGF6At-89Wc-gRWZWAHSVmg5N-F9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرد مغرور
🔹
روزی مردی ساده‌لوح به سمت بازار حرکت کرد تا برای خودش الاغی بخرد. در راه، یکی از دوستانش او را دید و پرسید: «با این عجله کجا می‌روی؟»
🔹
مرد با خوشحالی گفت: «به بازار می‌روم تا یک الاغ بخرم.» دوستش گفت: «بگو ان‌شاءالله!»
🔹
مرد بادی به غبغب انداخت و گفت: «ان‌شاءالله دیگر برای چیست؟ پول که در جیبم است، الاغ هم که در بازار فراوان! دیگر چه نیازی به ان‌شاءالله است؟» و بدون توجه به حرف دوستش، راهی بازار شد.
🔹
وقتی او به بازار رسید و در میان جمعیت و شلوغی چرخ می‌زد، یک دزد در یک چشم‌برهم‌زدن، جیب مرد را زد و تمام پول‌هایش را دزدید.
🔹
مرد که بعد از مدتی دست در جیبش کرد، دید کیسهٔ پولش نیست و دست از پا درازتر، بدون الاغ مجبور است به خانه برگردد.
🔹
در راه بازگشت، دوباره همان دوستش را دید. دوستش که او را پیاده و غمگین دید، پرسید: «خب، چه شد؟ الاغ را خریدی؟»
🔹
مرد با لحنی مغموم و پشیمان رو به او کرد و گفت: «ان‌شاءالله پولم را زدند، ان‌شاءالله الاغ نخریدم و ان‌شاءالله دارم دست‌خالی به خانه برمی‌گردم!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/438517" target="_blank">📅 00:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b478ab8c6b.mp4?token=szYHnieD1ftxEyrO-Q2JFQcRL6s2HODAzxgLU-gqC0fSEhkKXAbWiQRm1kZyyxTs4A_bEU_61fLe3SogUz7iziSK1ibuvsHTd9kQxMvAFiJS1tCu7crZo5Wjcpabk9D1NJdImIx6NV4I8nctV3LM-bv-O3iw66a7Z0rBpIZKM4V16bfY3TREip2SGQ9EaYHv5ZKyc18L6RkOAtUwshxt6jceqmSuSLCa4cT1huP4nBI76_2oVT913uoU5-4ToOnTUvARtsERS3iJnlj9umEO_YR6dKXU4kQzWu-OXwG9VfyKE9yedopHN2gQd5vZ6I9PR7sT82ioAo6KV35bQ3gXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b478ab8c6b.mp4?token=szYHnieD1ftxEyrO-Q2JFQcRL6s2HODAzxgLU-gqC0fSEhkKXAbWiQRm1kZyyxTs4A_bEU_61fLe3SogUz7iziSK1ibuvsHTd9kQxMvAFiJS1tCu7crZo5Wjcpabk9D1NJdImIx6NV4I8nctV3LM-bv-O3iw66a7Z0rBpIZKM4V16bfY3TREip2SGQ9EaYHv5ZKyc18L6RkOAtUwshxt6jceqmSuSLCa4cT1huP4nBI76_2oVT913uoU5-4ToOnTUvARtsERS3iJnlj9umEO_YR6dKXU4kQzWu-OXwG9VfyKE9yedopHN2gQd5vZ6I9PR7sT82ioAo6KV35bQ3gXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستگاه ۸۹ قیام مدافعان وطن در آبیک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/438515" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438513">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
شلیک موشک‌های ایرانی از جنوب کشور
🔹
دقایقی پیش نیروهای مسلح ایران از مناطق جنوبی کشور به‌سمت اهداف مشخص موشک شلیک کردند.
🔹
هنوز هدف دقیق این موشک‌ها مشخص نیست اما برخی منابع از احتمال درگیری بر روی آب‌های خلیج فارس خبر می‌دهند.
🔹
برخی رسانه‌ها از وقوع انفجار در استان‌های بوشهر و هرمزگان خبر داده بودند که بررسی‌های میدانی فارس وقوع انفجار در این استان‌ها تا این لحظه را رد می‌کند.
🔸
بامداد امروز هم پس از تعرض دشمن به مناطق شرقی بندرعباس پایگاه مبدأ این تجاوز مورد هدف نیروهای مسلح جمهوری اسلامی قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farsna/438513" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438512">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acd386934.mp4?token=pcqtYxwzZ7IZ-kMA9tGdnUIK-OeByW6rTrFnZQ56B_WO67QmlWGNSbRi7rGHGnNLLtWrL_ULFhLVP4JL-ORULO9TVJSlsheAYdWCynoePZmLkN3yvvU7t0Cz0r1kXdROPbICYPc9JXn18weGMdrOx7pe3DxyfTdvIbWSJGbhFV2VvBKWPT7fjZu7ycqxnueVXO0xgSfA3cZm7la0AIG_CBeWB_eK4w9L99ahAijlo3Tp8Rh78xrx0D-M3jgycp5U2uW18Yke7U4OG9zMOBLa2ud6ZfmFsuAUJtPpJeThDGDcbh_ojrfPtn8S-0GBidfx3N8x9Rw1CXUt4wkN8pX1yRdxA7B8es3KOycwPD-NRSJ9lWsLMcf30AVJ-ggj1ipIvKsapNbJ0eandP540rY4Eklwq4YwX8tl80cb482iyBjhtAZ2a1awRA_oe7pPSLUqQudv-2FsR24VPY9ZjIs9_lEP5as-pcLBCSD1b0TGdQ2j-EWmXnQrHdxRxuvRJEnk8545Jb_PS6vVaBcWWLp8REzlw83YD687g5uvn1PWIMMIkYCPBubeopRTcNox0zEcUw52ouoP5O-1tUB9T7wlUXSdQANuOyVnDmjwYhRId4je4nShEfTGduO3Qx42E_wDMf7PNYgV9fYSvsS3f-ysnzA8FKhdigx8HAj33SSjiWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acd386934.mp4?token=pcqtYxwzZ7IZ-kMA9tGdnUIK-OeByW6rTrFnZQ56B_WO67QmlWGNSbRi7rGHGnNLLtWrL_ULFhLVP4JL-ORULO9TVJSlsheAYdWCynoePZmLkN3yvvU7t0Cz0r1kXdROPbICYPc9JXn18weGMdrOx7pe3DxyfTdvIbWSJGbhFV2VvBKWPT7fjZu7ycqxnueVXO0xgSfA3cZm7la0AIG_CBeWB_eK4w9L99ahAijlo3Tp8Rh78xrx0D-M3jgycp5U2uW18Yke7U4OG9zMOBLa2ud6ZfmFsuAUJtPpJeThDGDcbh_ojrfPtn8S-0GBidfx3N8x9Rw1CXUt4wkN8pX1yRdxA7B8es3KOycwPD-NRSJ9lWsLMcf30AVJ-ggj1ipIvKsapNbJ0eandP540rY4Eklwq4YwX8tl80cb482iyBjhtAZ2a1awRA_oe7pPSLUqQudv-2FsR24VPY9ZjIs9_lEP5as-pcLBCSD1b0TGdQ2j-EWmXnQrHdxRxuvRJEnk8545Jb_PS6vVaBcWWLp8REzlw83YD687g5uvn1PWIMMIkYCPBubeopRTcNox0zEcUw52ouoP5O-1tUB9T7wlUXSdQANuOyVnDmjwYhRId4je4nShEfTGduO3Qx42E_wDMf7PNYgV9fYSvsS3f-ysnzA8FKhdigx8HAj33SSjiWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بسیج؛ روایتی از ناگفته‌های جوانی تا شهادت شهید سلیمانی  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/438512" target="_blank">📅 23:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438511">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290a136232.mp4?token=gud4CQO0nSYEs5RLtn8JOe0Kx6fJlFC3N2PSh1P2CcX8bL2mk5yGZ1U-Bjp2nY6MNCLNTmoA4NApKANNDFqeJ528vVAgPmqdWnflJrTR43UIQy3HAm7dR1_U9XfZu5KlKbHqDcP6oO-HK-y9gMbtnr69U_Y64DE0OY8kPEbK_7XhZpmpflXU03tK696mFZ7DL8Sw_mNSX05Tg3_6UGzB2hLolo7h8vjTXy8A2nwD-QbnkHjCpawTejt6BjwT0DNAQa0ETwCVNOA9sojau7FXsj2qtGku-I17d1JF5hOFSFEhGQExB_pC7afwRX6pS1uTUEtcvSSKaLPUHbPxtZUy7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290a136232.mp4?token=gud4CQO0nSYEs5RLtn8JOe0Kx6fJlFC3N2PSh1P2CcX8bL2mk5yGZ1U-Bjp2nY6MNCLNTmoA4NApKANNDFqeJ528vVAgPmqdWnflJrTR43UIQy3HAm7dR1_U9XfZu5KlKbHqDcP6oO-HK-y9gMbtnr69U_Y64DE0OY8kPEbK_7XhZpmpflXU03tK696mFZ7DL8Sw_mNSX05Tg3_6UGzB2hLolo7h8vjTXy8A2nwD-QbnkHjCpawTejt6BjwT0DNAQa0ETwCVNOA9sojau7FXsj2qtGku-I17d1JF5hOFSFEhGQExB_pC7afwRX6pS1uTUEtcvSSKaLPUHbPxtZUy7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌نوایی خرم‌آبادی‌ها در شب ۸۹: حضور در خیابان به جانمان پیوند خورده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/438511" target="_blank">📅 23:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438510">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e475c738dc.mp4?token=iINJksz0OzufTFswz_OsWnqpc9gDueAzr4CC92cXkJ4GYAQ4ll0A-XI5VwjH_0Y88iYUJlR7Y4mSr896TVSj1UDf_Eb-hNVTD8ZkCA9ZosPOCktxH9BbqnRNuuZJ73tnyNVYoBe5dkO1Gq6_ZIhzlXr2CWI2GJvcAs3rguu_4Xb6kTfmnQak0I1n7ClHb-A0QWM_eSJxCOLthgqGFtmwFQvWNmiPYsPLsCN7J7sc7MGmIrVHcbXa8yDkJfQp9JIbkNWpob3Qx5ufgpdMZUl-aVWstnC5ooXOhLnhg8HyW_iNl7i2CO0_Npg92MmGL3tsu27yLQCn-ZKadkYOH91_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e475c738dc.mp4?token=iINJksz0OzufTFswz_OsWnqpc9gDueAzr4CC92cXkJ4GYAQ4ll0A-XI5VwjH_0Y88iYUJlR7Y4mSr896TVSj1UDf_Eb-hNVTD8ZkCA9ZosPOCktxH9BbqnRNuuZJ73tnyNVYoBe5dkO1Gq6_ZIhzlXr2CWI2GJvcAs3rguu_4Xb6kTfmnQak0I1n7ClHb-A0QWM_eSJxCOLthgqGFtmwFQvWNmiPYsPLsCN7J7sc7MGmIrVHcbXa8yDkJfQp9JIbkNWpob3Qx5ufgpdMZUl-aVWstnC5ooXOhLnhg8HyW_iNl7i2CO0_Npg92MmGL3tsu27yLQCn-ZKadkYOH91_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی دختر دهه‌نودی در اجتماع مردم کاشمر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/438510" target="_blank">📅 23:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438509">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شهادت یک مامور پلیس در سیستان‌وبلوچستان
🔹
پلیس سیستان‌وبلوچستان اعلام کرد که ساعتی قبل استوار دوم عیسی عباسی که در حال عزیمت به محل کار بود توسط افراد مسلح ترور شد و به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/438509" target="_blank">📅 23:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438508">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f137fb22b.mp4?token=BUwAJRVZ4HsWlyV2gZz87ON1eu1P3Yx0aPRayWUyA9rDVP03pHr9o2-kEDZbcpdzIi18LJ2bvLrYDfSWCT6-JBCDlXNQHpUFXe54J63kBYQajIzu44p7q5fED3Rh1_WaIpdujFezSicUlV2UsBAB4rAx5D1BG7_ijqi8mU3T-NFfklQNg0E9yx7uk7OgXTsg_QocT4vtuAWCELKfJG3Di4DL9kv_r6vQg23a9rIB2IJFXVLAOEyBg_LnpDYGNryWWxTJ5Ax0JH2C6Fc87z6b5dV722dGy59lWqK0XiEwcrFLrgkMyXliujCdN0xHpJB-__nLL4Mr-Yf01z6mwwlEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f137fb22b.mp4?token=BUwAJRVZ4HsWlyV2gZz87ON1eu1P3Yx0aPRayWUyA9rDVP03pHr9o2-kEDZbcpdzIi18LJ2bvLrYDfSWCT6-JBCDlXNQHpUFXe54J63kBYQajIzu44p7q5fED3Rh1_WaIpdujFezSicUlV2UsBAB4rAx5D1BG7_ijqi8mU3T-NFfklQNg0E9yx7uk7OgXTsg_QocT4vtuAWCELKfJG3Di4DL9kv_r6vQg23a9rIB2IJFXVLAOEyBg_LnpDYGNryWWxTJ5Ax0JH2C6Fc87z6b5dV722dGy59lWqK0XiEwcrFLrgkMyXliujCdN0xHpJB-__nLL4Mr-Yf01z6mwwlEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸۹ شب حماسهٔ یاسوجی‌ها در میدان اقتدار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/438508" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438507">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e9e55123b.mp4?token=A_UzUWhkPxjwjjOhZI_W7tRL-Il7NVvFSZj0Y0VtfLkd3tYS7irg6eyFBEHkWyr65XSLWM1DPR8ankMzg4bz1_MuGKQ28XUdMA-8d0alA2lfIGWChfRdoYwxzslN3f6VyBxsh3Npqnh1olxeSKB0Ban7EQ1Xa1LCBFUpdC1MJNR0uzlFvspUL3WTqinWC_890SOsDief0Eplw-BQUcOx5HfADnxfyqT4zVVvcuUM8H_vVDoYpAUN-KOjjAFaTVn-BjC6Ea1vVoqiITW4k1wOy0tx6WompEUbGeeq-kDZv3Et2XkUgYbpVvC9oP_VR0KObHEFly977OMnaWcbv4ML3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e9e55123b.mp4?token=A_UzUWhkPxjwjjOhZI_W7tRL-Il7NVvFSZj0Y0VtfLkd3tYS7irg6eyFBEHkWyr65XSLWM1DPR8ankMzg4bz1_MuGKQ28XUdMA-8d0alA2lfIGWChfRdoYwxzslN3f6VyBxsh3Npqnh1olxeSKB0Ban7EQ1Xa1LCBFUpdC1MJNR0uzlFvspUL3WTqinWC_890SOsDief0Eplw-BQUcOx5HfADnxfyqT4zVVvcuUM8H_vVDoYpAUN-KOjjAFaTVn-BjC6Ea1vVoqiITW4k1wOy0tx6WompEUbGeeq-kDZv3Et2XkUgYbpVvC9oP_VR0KObHEFly977OMnaWcbv4ML3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۸۹ حضور مردم غیور لردگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438507" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0a90505f.mp4?token=IKdViU08fQOJKbkJznz2rYJZcX7ICidpyXW1GRpkWicZ0RqVOi5eyfmW12n7UPH-56qh0k_B-cQdcxvkldnKBVfsTRhqH0o3mLSD5qAhheESm-xXbQ0IDhAz4H0CvCSodd2sH36ly8lpUAtX1ofrTxP-DvvFA9Tnv2eLagMPkABC12kZOdXe4TT2ELuTT3meiG7SjfI4HMq_cJVAaM8pae9jeYQjHC4jNNOoSBifKmVbs4uMhTOO8PCIl3T4_CdfakAUrLqmYExfmuZX5fVz4aVPOvEbVxQL_RlLUyxvoahuPt7xZXTSC6j5unO1xlc9Gw2XDyC9PUxYxIhxKIsftFhozOL3uNfx5sBRKPgnNYgOIF7IOd6EDHDIHfwUTlRwQdAmdBnTjgwtD-88KOaObb4BoG54SKJo3P9NmkPXDFoq3cP0sN9kLEs_buXLxqNHkmvp8SAH8jeKe-51LxYvQPTAbLzNe4S9lbG0Um34lOFoVX7kphg35eAK3RHqM3D4IcCp-Yp1lbnCRTuoUzV-o1D74Sk355UVCrxo1jT79K1V8IeMGj8vtIGzc25nLn4KKqCiIMszHZc4fgQVJ9viGx8WMJJpPGuyaRZdtO2fQCU47lj8pFV2hy7fNYfFyF2b2q0YKb-DjOMgKMTjvaWdBMS9BRiPNVip5Kh9BGme7-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0a90505f.mp4?token=IKdViU08fQOJKbkJznz2rYJZcX7ICidpyXW1GRpkWicZ0RqVOi5eyfmW12n7UPH-56qh0k_B-cQdcxvkldnKBVfsTRhqH0o3mLSD5qAhheESm-xXbQ0IDhAz4H0CvCSodd2sH36ly8lpUAtX1ofrTxP-DvvFA9Tnv2eLagMPkABC12kZOdXe4TT2ELuTT3meiG7SjfI4HMq_cJVAaM8pae9jeYQjHC4jNNOoSBifKmVbs4uMhTOO8PCIl3T4_CdfakAUrLqmYExfmuZX5fVz4aVPOvEbVxQL_RlLUyxvoahuPt7xZXTSC6j5unO1xlc9Gw2XDyC9PUxYxIhxKIsftFhozOL3uNfx5sBRKPgnNYgOIF7IOd6EDHDIHfwUTlRwQdAmdBnTjgwtD-88KOaObb4BoG54SKJo3P9NmkPXDFoq3cP0sN9kLEs_buXLxqNHkmvp8SAH8jeKe-51LxYvQPTAbLzNe4S9lbG0Um34lOFoVX7kphg35eAK3RHqM3D4IcCp-Yp1lbnCRTuoUzV-o1D74Sk355UVCrxo1jT79K1V8IeMGj8vtIGzc25nLn4KKqCiIMszHZc4fgQVJ9viGx8WMJJpPGuyaRZdtO2fQCU47lj8pFV2hy7fNYfFyF2b2q0YKb-DjOMgKMTjvaWdBMS9BRiPNVip5Kh9BGme7-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مردم جانشان را برای اسلام و وطن می‌دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438506" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438505">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6436e2ce.mp4?token=KZ3iZsy5Ee09HJyOtT4FD-kYpsEYiKgJQ7NcG2PDiO0B97xGTpcCyQqul7hbL8dmTn7LUv2GUp-G9FP08RBYkNGOoM3ELC4thcoJFT8qG04rZqqhZa0hChYo9ISvQS1-iS2So5C7zkLdfzA-GTP5nrLBAaSoQ1yFxqVhuVdeik38AR5q2EiNZ5fkrySfDsywYhwZ-A1JzxzQXXjE5ilLkvaCh-vxogtLXnthdZKI3M-1nbncjDsNdZXr7zL8pgb9mlZD6UhdTcS0ZR2CPaOWx3cIoXxkpIWW8lOOwrCvsT_-R3rXBoRNNyWn1rFVSBNowf1u5Coi39UItENCBlZWTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6436e2ce.mp4?token=KZ3iZsy5Ee09HJyOtT4FD-kYpsEYiKgJQ7NcG2PDiO0B97xGTpcCyQqul7hbL8dmTn7LUv2GUp-G9FP08RBYkNGOoM3ELC4thcoJFT8qG04rZqqhZa0hChYo9ISvQS1-iS2So5C7zkLdfzA-GTP5nrLBAaSoQ1yFxqVhuVdeik38AR5q2EiNZ5fkrySfDsywYhwZ-A1JzxzQXXjE5ilLkvaCh-vxogtLXnthdZKI3M-1nbncjDsNdZXr7zL8pgb9mlZD6UhdTcS0ZR2CPaOWx3cIoXxkpIWW8lOOwrCvsT_-R3rXBoRNNyWn1rFVSBNowf1u5Coi39UItENCBlZWTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار هشتادونهم مراغه‌ای‌ها در شب‌های دفاع از میهن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438505" target="_blank">📅 22:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438504">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c835b11e79.mp4?token=gAb9EX-x0qJBRC3bLY8PdzWT2EPG-jtBF9cjRd4XCZgoubRHV-mha7Uc8fak5_2HatA7MfQH5nhgM6asj3kTcIyqx5u2YOqCoHBf8QbuvuJolKRTjf6iMRE3E-3NlImTU1AQWUZZ3d4n3I2jAcgVMYguzBeT0YEvxKZbjnHCQr_mLKK6qf2QzmK_12hxvAi4nC2DqmEi8qwstei_uGK8VjZ_EtjEt7hFFxlR_afA6RZSynVwFPJHg2yKA2IagpbyAF70ruhfejTdCdae-taGSxmnlS50fugGhL8FbxlERb2gFqKssxc1mBzfou8l4WO6bOb1reLCzXvWuSlxaqqI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c835b11e79.mp4?token=gAb9EX-x0qJBRC3bLY8PdzWT2EPG-jtBF9cjRd4XCZgoubRHV-mha7Uc8fak5_2HatA7MfQH5nhgM6asj3kTcIyqx5u2YOqCoHBf8QbuvuJolKRTjf6iMRE3E-3NlImTU1AQWUZZ3d4n3I2jAcgVMYguzBeT0YEvxKZbjnHCQr_mLKK6qf2QzmK_12hxvAi4nC2DqmEi8qwstei_uGK8VjZ_EtjEt7hFFxlR_afA6RZSynVwFPJHg2yKA2IagpbyAF70ruhfejTdCdae-taGSxmnlS50fugGhL8FbxlERb2gFqKssxc1mBzfou8l4WO6bOb1reLCzXvWuSlxaqqI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب:  نمایندگان مجلس مطالبات عمومی را بر نیازها و منافع جناحی و گروهی و منطقه‌ای ترجیح دهند
🔹
برای ایفای نقشی در تراز ملّت مبعوث‌شده، مقدمات و الزامات گوناگونی نیز مورد نیاز است که در این مجال مختصر، صرفاً برادران و خواهران گرامی را به مطالعهٔ…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/438504" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484727e1e3.mp4?token=jReFCtfomL-afZC2Vm3Ja_uFU2gH1xGX8VVn2wI_C1ELp77mIHskg0Gl8g3-2HWhFc1-BR632n9ooyXxICXLTpKR8JsHzZcD92uiM5LIvsXl_ffBCsNtlwemNa5dLh_Q6obAkPpSsFZf45erIxEqs04nmj8PQcDDPhlj9b3kfIHqo3DqeJ-R8FY5cOm4Hv17xHUADOX0J3HjXLJ1-LSmGsfVBQGxGsbSx60BEJeBgMrTFdhqyIlXB5mS8qqwqzkK4z1HW55Xk3hlpQ7pwPgzL2OpR4zC-m7BOvcdwTxynAbSrTQsv7eeqrwgYVVVVvivNnTHihZnqxF-ph0vGY11fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484727e1e3.mp4?token=jReFCtfomL-afZC2Vm3Ja_uFU2gH1xGX8VVn2wI_C1ELp77mIHskg0Gl8g3-2HWhFc1-BR632n9ooyXxICXLTpKR8JsHzZcD92uiM5LIvsXl_ffBCsNtlwemNa5dLh_Q6obAkPpSsFZf45erIxEqs04nmj8PQcDDPhlj9b3kfIHqo3DqeJ-R8FY5cOm4Hv17xHUADOX0J3HjXLJ1-LSmGsfVBQGxGsbSx60BEJeBgMrTFdhqyIlXB5mS8qqwqzkK4z1HW55Xk3hlpQ7pwPgzL2OpR4zC-m7BOvcdwTxynAbSrTQsv7eeqrwgYVVVVvivNnTHihZnqxF-ph0vGY11fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلزار شهدای میناب، میعادگاه جدید عاشقان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438503" target="_blank">📅 22:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حزب‌الله: طی یک ساعت ۳ تجمع نظامیان صهیونیست را هدف حمله قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/438502" target="_blank">📅 21:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cc809c60.mp4?token=VbyF5FbHWlogAL5u5PjXuSojI7LP0OE19ry9-M0ctgkutR5R0iE4sp07xmUlkA82c97sKSylHFd6Fc6zukssQMv3SrIcAGTGxpUQnQEAtXP6a5kCj_HsNXxUeXgjGDGumdoH1R6Rtvu3vv2aS0NUq_UXmnPOXYuAZ1W-rU5Ehk-C9HwzgUkp88oTNg1RCKRPZj3os53ViwPpvUxeXBeQP29E5c69mfbiSMp06hmovvqxtyOKqtrrLViNr8eju1zrJzFUL68ClgyeunxXan2fsTS0RtFNBD-P9Yk1K8NxApjXdyoTgQVv94fXsejLkdpr_Xio8PyXrsaorKG_Uj-JBAVQ2LpUpiF3Z4rE1ikrhAU7JIxOf40OA9KbQsG2PDPNbhYLHKf0Fsty33BUD9RHRjsA94DfnFPaCaPmrp397Qw7eEU-cXg1jUtiXUM0CEPMBwBdu_AnO0cyp_pechwNqsAEJn0G924GTVEMcdJ_M1os3R9mRI7Degt0mNE-n5EHZm6izAhDH2BOM_6t_Kkd4YYiCubtpWsvEHkQ6TXq3atNA3Zv9qtz4eaW-Wx-PfW3HCZ0JSnf755HIWcLSlUlZH7U91f4Z4J6ItBEYf17q83lGSn0aTeGJCJF9C0MSvEU5Q26SkipoxbrDaTXtSzKEgJmOOMUqsJKA8u55_NQdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cc809c60.mp4?token=VbyF5FbHWlogAL5u5PjXuSojI7LP0OE19ry9-M0ctgkutR5R0iE4sp07xmUlkA82c97sKSylHFd6Fc6zukssQMv3SrIcAGTGxpUQnQEAtXP6a5kCj_HsNXxUeXgjGDGumdoH1R6Rtvu3vv2aS0NUq_UXmnPOXYuAZ1W-rU5Ehk-C9HwzgUkp88oTNg1RCKRPZj3os53ViwPpvUxeXBeQP29E5c69mfbiSMp06hmovvqxtyOKqtrrLViNr8eju1zrJzFUL68ClgyeunxXan2fsTS0RtFNBD-P9Yk1K8NxApjXdyoTgQVv94fXsejLkdpr_Xio8PyXrsaorKG_Uj-JBAVQ2LpUpiF3Z4rE1ikrhAU7JIxOf40OA9KbQsG2PDPNbhYLHKf0Fsty33BUD9RHRjsA94DfnFPaCaPmrp397Qw7eEU-cXg1jUtiXUM0CEPMBwBdu_AnO0cyp_pechwNqsAEJn0G924GTVEMcdJ_M1os3R9mRI7Degt0mNE-n5EHZm6izAhDH2BOM_6t_Kkd4YYiCubtpWsvEHkQ6TXq3atNA3Zv9qtz4eaW-Wx-PfW3HCZ0JSnf755HIWcLSlUlZH7U91f4Z4J6ItBEYf17q83lGSn0aTeGJCJF9C0MSvEU5Q26SkipoxbrDaTXtSzKEgJmOOMUqsJKA8u55_NQdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروهای نظامی صهیونیست‌ها یکی پس‌از دیگری شکار می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/438501" target="_blank">📅 21:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438500">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743ec3e77d.mp4?token=ojUzpHJRmsjYCeb8qmeO_56tVNspbbnWQLfh7idYJwBJAAj9Lscg0F5aYEZ8NN8uk0d5Sn1VTQCtG7EHXd5eM-0Cp-HFb8XXv1XwkkO88OiS4btIJ3VBLLikkWHNCR8p8aZ0u9f0egRYxtwFJ3-eOBwBi5Bdjl4BCi128whxFKS27sO3qIqxeowm1C4sTO9YIklK3E2e2MfuKwg5TFPKWHENWbOOBGEKBLSOl-yi0gm25O7Y-7dprG-dRcTTWVhkprR6z083ZqyLZ3iYCiiKQ5_V4pNmJ9I3S3DTaSgwkms2YbqdCxdVhpdwueSRGqlviwNwWl6LQgjQxn2SUeoVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743ec3e77d.mp4?token=ojUzpHJRmsjYCeb8qmeO_56tVNspbbnWQLfh7idYJwBJAAj9Lscg0F5aYEZ8NN8uk0d5Sn1VTQCtG7EHXd5eM-0Cp-HFb8XXv1XwkkO88OiS4btIJ3VBLLikkWHNCR8p8aZ0u9f0egRYxtwFJ3-eOBwBi5Bdjl4BCi128whxFKS27sO3qIqxeowm1C4sTO9YIklK3E2e2MfuKwg5TFPKWHENWbOOBGEKBLSOl-yi0gm25O7Y-7dprG-dRcTTWVhkprR6z083ZqyLZ3iYCiiKQ5_V4pNmJ9I3S3DTaSgwkms2YbqdCxdVhpdwueSRGqlviwNwWl6LQgjQxn2SUeoVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین شعار مرگ بر آمریکا و مرگ بر اسرائیل در پایان مراسم یادبود شهدای خانوادۀ امام شهید  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/438500" target="_blank">📅 21:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAPb_uqW8KW_nri4KI-kmQlKH4_FGKsVuIVEnNydC0f5jnIO4I2rhGWYa14aEHUGwbXUxJVYGZshl2bMfc5kTubQC3SuKTqIzX13jwGWHD-S_keS8wzja1PSe8nqlobuK5f_rK6_FkjfSHPD-GMnOGr0LqGfw2hwN2u_oEDeQjsAKh6IyChQhKV4EYzdglumNRJeCGSQUQ0kJbbAwAFhvkqW9Wjp8rFQe17-OgrbWRPL0vYXHLw7ACgFQp_0Z6WRfIdLV6hlnRftAyEBP6asULQ8g7L5LMlF2tVQuYfSt2JMZeuYdmx0pJ-UfDQcVZ-D6-Rx1CAbNgGw4SX5N7B-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N37b6hXUbUCOTRGqCS1ik2SG8LxLzna7HoZUPAJXW6CsTg86WAq3dAlD1HwqAiOeUSwEB7rQyqgvvPXmesV1UfLjHqmpCIC69FR0pGianprJ_ev0ZDhLyZ4Yzs9-MIC1ePSE_VrqFTdxjlHEKOPpA_OU__5v8D6jjOF55CM1lKKr4f0jUsy6hW-xQ_Pj3wwTi7E0n5Yi1c5zGCQN5_BL3deXUq4d7vAreIXJjpgGQHcQTFocq3_QMcg4Qy5YuKP3g9d3UnRcmuOAjRI5FBc-8L8Xk_VnSu4u3XICXFlMMM3_Hq0jPmt-XLG_VeW53b4Ep-0OqUKG-hxl9XyoVQ5OMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3Z-xC8n61VgxHmfhnnJseGFrewslhSCrz5zHW308LZkD8ozUQ_d8g68k8SsPj8JYJnkUVHg2NrLkqO_fS9wzdvZR86zJP8h60PIRvtaPU_lnELj2EsOjHga_s0CkQQAz8ooD4eSuDZ1sVgbTILVHumstFG4j-MqcpT86HJqzxE4U1pFrQAK13Hy0CITkxt4f9nQluCqKYNbynr2rPrn3VCp1ZZH8e4HcrIgRHGt_dbMIcd4seJ4oDvAjoIkZPylu6nNTpdeILlxWDUwqC3LgI3OrRh_9cH7IREWtkdoZp4MfhHWXd6msM8FtFZ0WZJkMeukNv0sFg9BpW2W0b1pTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orqpGy3VkbUyLnjfn1z3nRorYUjZpdTcAhiLp8lqEEthWD518iS5wkqM3zbJqwbFlfaHQMgrBb5JsuCPfN9cMOhELhEyrFrPGKXx9m23Z27TavDw2qMg93aTt74JgAtPXHv-RJOAxNYLNFKOIxyn6ZYpF8UUoAtaZN4M_ZEh8qsQrgkzqkXECeBi1z5QDO4xL4tanAMw9isGQXoo66NldC2qZX6rKw_TScd2ER16jm7kLdztZYr8HtkEvuL6EVflv3oh4a9GGV0D544mibOfVfxzbiLdDQaQtlHmoQ3rm9lFJWVtcRjBZMqzgAGlA69MJ1awbUUnYahVvj4Vr4cCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fs5AxfG06eFCwkkhIVewm1_YGmbIeKRqKeejfr3tPFPEilgRzCsvCo4r0GvATEFSMgXNoRF3fxQiLbsyIdXNLSQjL5qr0YeEj3wj5jVfe9kYJbSRgGd-wiruHYnGX-Pu4UB8Lrbo0g7nCcL_eR6u4uBuge2eKAwoUSoHoV92fPkvO91NWADghlaJNO6hXObJ360aureLUh6XDFytNHBGBUfWamdeEKGPxvuw7vSrACWILS7gUjGcZWLqBkWT5v7mS9SovovT7qqYXrBHw_K-T1gHL1KwUasGS7UJcwYQnHPa60W_WOUGY80KP33hCh44nlSPHWwv_UidxRwvxk4I6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH8tDRWBe8f3MCPr1fDi5_1SvQ1eLX3LCZ3GAvHJtG4KPE6pWkIS100dCUkmGPqIr1yGWYyCi205Z5AyKgdawd8qeSaqIdkjncQLA7KZlYDDystk84Ux7iHPHNShGY74_l7UCo68a7Jvsg6h_P_BD9yaIS8VPNJ4Y28xHp21bpaIBSleZ2Po394xyjhnRrq9TEpOLtoeVzRrDmWlqYBxSlWgH2lBwaPsioAUsy4ZvDz15_kLDFtEySMlqp2OTRxH8Ybzi7JFlaYNAdOjpQAfFzZW6K2g4ICViGHO9HiTQxIx7k1Dm80-q7EFUW81YCsfX_GeCzr8CcksrOpv8eH2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVto8uqRnn4EQW2xRLWoOUzeIZyH5NOyRwNcN89io91syZkZxNmYRYbfcm1PDHKurYS9RYxpeRlaqqzRSoBIqsCA2h3LdCtUWIUQm4vbP5hFbOeR4HQWmJ5DVoPd43Itr1AfzKezYfYvBDGiC_GVpC1Xy3yizbDcGm0T_TrkXNU1-2gRJnIEtTRgom-20OTyMucQgetqKThLwm1IsuoaxWTynCm4YcVcCDbcnZXpd4Tq7N7Xh2cDZp0bNdblXxkn4WRrP_ENPooodZ4vscUMkbcmJOam-EArtlXxffMVRbo_0vc5if9-UWiW4B03iq9Y4tlONZrM-3F4eppT0igmoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت سردار سپهبد پاسدار شهید حاج محمد پاکپور
🔹
مراسم بزرگداشت معمار امنیت پایدار، فرمانده سلحشور، خستگی‌ناپذیر و مردمی کل سپاه پاسداران انقلاب اسلامی، سردار سپهبد پاسدار شهید پاکپور پنجشنبه ۷ خرداد ماه ۱۴۰۵ در مسجد پیامبر اعظم شهرک شهید محلاتی تهران برگزار شد.
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/438493" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esGj3DmITrBRFBxqTDyV_qDVHLgRu1BTgrbf4FoRW4g-YHDIEUgeP14WeKJRsY5oyWHMUit83gWBPNu45S9xwPTmcZFOlAOPDa1oZ2_15MBPFprPKRUVShsXvxiPGpKh0oW6fav-ythALNsup9RJIPwE29P--IO-mYXtkuh_A70itErZYNHYJNokdY0XNLlkBaJdNtiAL4LtMC_CPdIe8Q1NA9f5YPdetb35TnNK9umyqTaAFLnaufiT_smBIRj-vVZ_xLg2oVjMFXkNJ0AX8luWLnpe8HnCUNJqg1SKR6h1yJoK15k4b1yG9jLhewQTT97W5WZ2BFi0BkcrILqCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ارائه طرح‌های اختصاصی بانک صادرات ایران برای تأمین مالی تولید و اشتغالزایی در بازدید قربان اسکندری از شرکت لوله و ماشین‌سازی ایران
🔹
همزمان با بازدید قربان اسکندری، سرپرست بانک صادرات ایران از شهرک صنعتی شمس‌آباد، طرح‌های اختصاصی این بانک برای تامین مالی بلندمدت و تقویت همکاری با شرکت لوله و ماشین‌سازی ایران به منظور افزایش تولید و ایجاد اشتغال، مورد بررسی و پیگیری قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438492" target="_blank">📅 20:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438491">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ef50a486.mp4?token=dhRV4_EEhgKLxaiNzLiBObYJrJYUL5qWnkbFL4dfppac2R517H0JL4d5IKLQgfQF1yl-lFNzyk8qYCzLfdDOCpwhUw00oRJzuyJMfWtv2DrfwQOBsT1NwGK39bfhPaqwytuEWS-bqr3pp5I-2iPxU8T8gsSYLXw6nZLy8gRCrAyrp5g2m8v1W3qEG_7vdHYIigi1u9g_IUEB4SHzLiud3JOSyTkFfCRCcIgu7oNmg3THd-Ycv8qbXwJWyefRBg9xaTuI-kZijhtNkqayKdIkSJ7Gq0nAX4uwlhZ513XPz9A50ZPM6Ftjt_JLKEs8gksm2_GAmMkfBznjU-_sLPf8LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ef50a486.mp4?token=dhRV4_EEhgKLxaiNzLiBObYJrJYUL5qWnkbFL4dfppac2R517H0JL4d5IKLQgfQF1yl-lFNzyk8qYCzLfdDOCpwhUw00oRJzuyJMfWtv2DrfwQOBsT1NwGK39bfhPaqwytuEWS-bqr3pp5I-2iPxU8T8gsSYLXw6nZLy8gRCrAyrp5g2m8v1W3qEG_7vdHYIigi1u9g_IUEB4SHzLiud3JOSyTkFfCRCcIgu7oNmg3THd-Ycv8qbXwJWyefRBg9xaTuI-kZijhtNkqayKdIkSJ7Gq0nAX4uwlhZ513XPz9A50ZPM6Ftjt_JLKEs8gksm2_GAmMkfBznjU-_sLPf8LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک تعطیله؟ نه برای ما
😎
💡
پیشخوان‌های شهرنت بانک شهر بعد از ساعت اداری هم در خدمت توئن؛
از افتتاح حساب و صدور کارت هدیه
🎁
تا انتقال وجه، مسدودی یا صدور مجدد کارت
💳
و حتی خدمات صندوق‌های سرمایه‌گذاری
📈
همه‌ی اینا، راحت و بی‌دردسر، تا ساعت ۱۰ شب
🕙
بانک شهر، همیشه همراه شهروندان شهر
❤️
برای مشاهده آدرس پیشخوان های شهرنت
اینجا
کلیک کنید.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438491" target="_blank">📅 20:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438490">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438490" target="_blank">📅 20:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438489">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab3f20a4e.mp4?token=hSVi_NWFsM7ZaQb8MG8owa2R_WMnnSy9c3qJviNzj9S1AedR6EDf45tO0sONBKLzbPFeZyF3UG-bx2XkRpYuYwkn2Z0FmwfZ8IcqXvb_4yZB6cEJHxcppbpItAvMq6lKhu8eWk3hM_xx1A4sJGz3GGaJW8QRS9G7GqIMU3FbKpIGDoPGj2uYx1ID_uERd1hoQSDl-6rpdRfz45lIkVFx_DST7aFhr5ZwjQJIT9Tq9yuniV3KK5H7xtuM9G5XeXNrBUsaznbDWQoGjjSRDTVCM0nKB2xsWXTLsGMv3xZeXO_tqdsgVwBwiZvHHJqk4YTW8TXeSRM7SuBtCOpAST-DjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab3f20a4e.mp4?token=hSVi_NWFsM7ZaQb8MG8owa2R_WMnnSy9c3qJviNzj9S1AedR6EDf45tO0sONBKLzbPFeZyF3UG-bx2XkRpYuYwkn2Z0FmwfZ8IcqXvb_4yZB6cEJHxcppbpItAvMq6lKhu8eWk3hM_xx1A4sJGz3GGaJW8QRS9G7GqIMU3FbKpIGDoPGj2uYx1ID_uERd1hoQSDl-6rpdRfz45lIkVFx_DST7aFhr5ZwjQJIT9Tq9yuniV3KK5H7xtuM9G5XeXNrBUsaznbDWQoGjjSRDTVCM0nKB2xsWXTLsGMv3xZeXO_tqdsgVwBwiZvHHJqk4YTW8TXeSRM7SuBtCOpAST-DjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جبهه مقاومت باید با فشار نظامی، اسرائیل را مجبور کند که از لبنان عقب‌نشینی کند.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/438489" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438488">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=VJQAamynF4Ro5H_rhMjbe7L8IivDK7cNlN8qJetH76GOSjEsne9FRNiC1ip8fwi7guCD2oOSre-IBgv-x78ZvyAot-r66uOk1Q45q9VRmnhSVEqlPYe6WpfQ0Dq4f3jU0bPEyuz4KCRM7tfu8nofgpouEDZCEdY7mdkNB49FxYj9CEXCVm17vbbNnPciz4mqUAextD92KAkhA7hkfso5IBVdtt4dqITVQ63jnNZQLt0ks54gT6JhqGwDV7EKbRAMJZwc2Y5puq5iyCkeyH_BEHUBvipPFNRDKJYIJXZb_lPf9nRRcfZ-Sph5-WQJWLgTORk3QBzSebVoUHg7IGVkRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=VJQAamynF4Ro5H_rhMjbe7L8IivDK7cNlN8qJetH76GOSjEsne9FRNiC1ip8fwi7guCD2oOSre-IBgv-x78ZvyAot-r66uOk1Q45q9VRmnhSVEqlPYe6WpfQ0Dq4f3jU0bPEyuz4KCRM7tfu8nofgpouEDZCEdY7mdkNB49FxYj9CEXCVm17vbbNnPciz4mqUAextD92KAkhA7hkfso5IBVdtt4dqITVQ63jnNZQLt0ks54gT6JhqGwDV7EKbRAMJZwc2Y5puq5iyCkeyH_BEHUBvipPFNRDKJYIJXZb_lPf9nRRcfZ-Sph5-WQJWLgTORk3QBzSebVoUHg7IGVkRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم
🔹
تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438488" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438487">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d043550950.mp4?token=bOs7IC8BIU6CBQqHR2-KO9PFWRx-pihHej834BGCGLhrwuaH6gthK5xd82Jfml-ycIF32e2SrqLPvBAQZRI0PdnDsQ1cvHv1etUlc0D3pu-B1q7yGXsLiGkdqi-MtZHnT-_3XywWTdPPWIyYyr9Wt_HC0T4wCBZkrabA9UNH5db_WQ3BEVGfY36zhG13dqiPv0W3Of4PpPMUvPj-9KJPRRdZu2NJyNuz4WqFmtHNrzXQehA7Xof1MpAU6i-Dk2PREtXLlH5SswoX_KWO4eSVYE60IHATa5NyYQjrYueE77nl7oP6_ThHVPRVzGrYsTPn0hsMo91hKuRHbDrQRnRWUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d043550950.mp4?token=bOs7IC8BIU6CBQqHR2-KO9PFWRx-pihHej834BGCGLhrwuaH6gthK5xd82Jfml-ycIF32e2SrqLPvBAQZRI0PdnDsQ1cvHv1etUlc0D3pu-B1q7yGXsLiGkdqi-MtZHnT-_3XywWTdPPWIyYyr9Wt_HC0T4wCBZkrabA9UNH5db_WQ3BEVGfY36zhG13dqiPv0W3Of4PpPMUvPj-9KJPRRdZu2NJyNuz4WqFmtHNrzXQehA7Xof1MpAU6i-Dk2PREtXLlH5SswoX_KWO4eSVYE60IHATa5NyYQjrYueE77nl7oP6_ThHVPRVzGrYsTPn0hsMo91hKuRHbDrQRnRWUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله تا داخل محل استقرار نظامیان اشغالگر رفت و آن را منهدم کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438487" target="_blank">📅 19:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438486">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248fd81892.mp4?token=MZeXZFyQU_eu9hv5D_KWHtZJZMl7B3c1Oc5BQcAHL7coAZjVjC4_aF8DFaOnpKdYb0JcBBLvWycsv-MhbYg0QdTi477_11TjFDjs2jRupnZDc-pn2cYKLgk1zV0eHJubo2oe7cgWKyR6DrXGA42VxSfuJ3TZxNNr6L16O_GqzAmDJ17WFir0SQsIuHEBrZx45PMtXc27BcWXzJriagN4YDCDrDAqi1ejHEFJHtd6MnlPD_A270jcU_v5jpD0Fnoc33NaaW_bYjFyryVwAKrsFcRQEgAI4ojdFZTzILIX9ZIirGy8N0swlHpwky8-F5ojxwRntTS2hGwXqJwUXNGmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248fd81892.mp4?token=MZeXZFyQU_eu9hv5D_KWHtZJZMl7B3c1Oc5BQcAHL7coAZjVjC4_aF8DFaOnpKdYb0JcBBLvWycsv-MhbYg0QdTi477_11TjFDjs2jRupnZDc-pn2cYKLgk1zV0eHJubo2oe7cgWKyR6DrXGA42VxSfuJ3TZxNNr6L16O_GqzAmDJ17WFir0SQsIuHEBrZx45PMtXc27BcWXzJriagN4YDCDrDAqi1ejHEFJHtd6MnlPD_A270jcU_v5jpD0Fnoc33NaaW_bYjFyryVwAKrsFcRQEgAI4ojdFZTzILIX9ZIirGy8N0swlHpwky8-F5ojxwRntTS2hGwXqJwUXNGmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🔹
طرح و نقشهٔ کور دشمن پس از جنگ تحمیلی و فشار اقتصادی و محاصرهٔ تبلیغاتی و سیاسی، ایجاد تفرقه و تجزیهٔ اجتماعی برای جبران شکست‌های میدان نظامی و به زانو درآوردن ملّت است، و لازم…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438486" target="_blank">📅 19:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438485">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96a4b128c.mp4?token=oT3o-1C0vkz3nq8m3_4UGgYqemXbVciJkbSeppLDnHbaAp3WJxVdeMevj0V9ErzfuxkPwMrVNenWrWMOUA0WPkJj8I6hDSFxjwxI9xFjpzIWqMNuDv9Cyr18ajmC4UNy1uQhunh5EO14iK1y5d-HUpqqNQoFyWNrqC4K-EzvKLBh_Rv-oUVQRptycYjwQDv1CUB5Gpvih5E6sfAa9T_Hqy4qXGd6bht1MAN57p-qpUDArYPhkhlBYUdR0_C5Uhrmj-xKa6isKETUhum5xwTkaOFeZi2Th5BmfHiHmoEQm0Pbp1LiX4Tfi1jUZsUvMeeFGqAvv5UGBXqHYG2K-4Bibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96a4b128c.mp4?token=oT3o-1C0vkz3nq8m3_4UGgYqemXbVciJkbSeppLDnHbaAp3WJxVdeMevj0V9ErzfuxkPwMrVNenWrWMOUA0WPkJj8I6hDSFxjwxI9xFjpzIWqMNuDv9Cyr18ajmC4UNy1uQhunh5EO14iK1y5d-HUpqqNQoFyWNrqC4K-EzvKLBh_Rv-oUVQRptycYjwQDv1CUB5Gpvih5E6sfAa9T_Hqy4qXGd6bht1MAN57p-qpUDArYPhkhlBYUdR0_C5Uhrmj-xKa6isKETUhum5xwTkaOFeZi2Th5BmfHiHmoEQm0Pbp1LiX4Tfi1jUZsUvMeeFGqAvv5UGBXqHYG2K-4Bibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار ایرانی حاضر در لبنان: دشمن در جنوب لبنان بزرگ‌ترین ریسک تاریخ خودش انجام داده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/438485" target="_blank">📅 19:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438484">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74263a0709.mp4?token=IlR3coMJa3IaSUG4yRuwwl_oJd99-T37qwqp6meyJ94Rsxq2NkwEBRp2PnaC6MbS88ZfunB8oGBouD6SfolbrUmoOGBpzsVS0Db5TxUEmh69Pjir-eX1-cE-jVXcwF-N15yTciqK8TKJz2W8HVpArCm_mp2xGxc8KQOvb2ywsuByiyKv6qSV_2VAnEnEshhD1XLXpT1_jkk6A_BYPTDnY0Zm1J8dGiOq_n_qPnxsEgjzxGLHO33AZA4moLFoVxeBPJbIKNlLGljABOqJQYNWH8OjrvYWtA-KAxx8G0Cv16hGN2H-FkWk3zO-Yfu8TA2_2WrplDZ3gmdVdOD_htlCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74263a0709.mp4?token=IlR3coMJa3IaSUG4yRuwwl_oJd99-T37qwqp6meyJ94Rsxq2NkwEBRp2PnaC6MbS88ZfunB8oGBouD6SfolbrUmoOGBpzsVS0Db5TxUEmh69Pjir-eX1-cE-jVXcwF-N15yTciqK8TKJz2W8HVpArCm_mp2xGxc8KQOvb2ywsuByiyKv6qSV_2VAnEnEshhD1XLXpT1_jkk6A_BYPTDnY0Zm1J8dGiOq_n_qPnxsEgjzxGLHO33AZA4moLFoVxeBPJbIKNlLGljABOqJQYNWH8OjrvYWtA-KAxx8G0Cv16hGN2H-FkWk3zO-Yfu8TA2_2WrplDZ3gmdVdOD_htlCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمود کریمی: حامل ۳ پیام از رهبر انقلاب برای این مراسم هستم
🔹
خانوادهٔ رهبر شهید در ثواب این روضه شریک هستند.
🔹
میدان و خیابان را رها نکنید.
🔹
از شهید صادق زرین یاد کنید. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438484" target="_blank">📅 19:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438483">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e199577f.mp4?token=cndeqr0Xg7mtM6V9aIvrF-W0dzUYKbmkJBIcOjr5OXMLG6YKjmlR6Ae_9RtXZIGiN2mEBIZc3ttuGQkgsNIpVj06Us9wupkwE-gMp0sKgm0nyU70rYrIyEmztTe8-yV_xWa7x2XRk_UJ5oqCKjje25ON3wYQ32R4-1D2x2w_6w9R9BkbIsU2hGYWIrLGdde8asYQsMS56R3Y0oGs4iOWx-k4T_wQN1Jinm35-89tiQvMS33E_7D_7GeowT5OOS52RE5jk9epcnhvnGiacqM4E7SBeXGbKRVFmHfSrLpunRyEGq6ZptnnyRhUvsU_s1cHQKmk_mVxIQ75Wgwm0q_5Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e199577f.mp4?token=cndeqr0Xg7mtM6V9aIvrF-W0dzUYKbmkJBIcOjr5OXMLG6YKjmlR6Ae_9RtXZIGiN2mEBIZc3ttuGQkgsNIpVj06Us9wupkwE-gMp0sKgm0nyU70rYrIyEmztTe8-yV_xWa7x2XRk_UJ5oqCKjje25ON3wYQ32R4-1D2x2w_6w9R9BkbIsU2hGYWIrLGdde8asYQsMS56R3Y0oGs4iOWx-k4T_wQN1Jinm35-89tiQvMS33E_7D_7GeowT5OOS52RE5jk9epcnhvnGiacqM4E7SBeXGbKRVFmHfSrLpunRyEGq6ZptnnyRhUvsU_s1cHQKmk_mVxIQ75Wgwm0q_5Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جنگنده‌های اسرائیلی حملهٔ بزرگی به بیروت کردند و خط قرمز را شکستند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438483" target="_blank">📅 19:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8587c2b060.mp4?token=iibpne0Qzkf4p3pGanCjhpO8TdSZUoryRvq8B04paE8aKiZOi4tIv4SXDaRcZ9WSHA4v9Xkf5AOkDEav866Mjh6GDFyRy6pfhOsKZ5zFleHcETBivqNjI6UKFJOetzYrMqrzgUFvHbMvXR7BsE5ZJPuiq17dV8J21ubasXnF7FjBgvZ2eUVhhrj5WonRV43X85IOJh9aW7-sFz5jNekRr8e6miWXgXSgn7LCw_mZ5S_YySeCO4G0j8GZmJYpsQAuavb9a5jUZEnSTkE03Nci6T1ZlNLHrgUZRdUwxrkv-eB428VOQzlwOK4w_NArbo_WbqJ7JrxCp3NEzzAFmj9P8ROQv1vldqpLnKkvuPA2zKiVetoVRn62sIyNSMSDcyYMNNmYkybXfChNMU5AVIFeGPH-aDRIo4Yot5OA3bh1abt1FRJzAEOV2rzFMAh76vArNqkHiOtI76e7LOE6ol2ZxYZh_ABCGS-sVR2RWDChv0hYe964mzSII5kX2gc9E6y_G9eAhaLPkG6YjwNP340KRlC_GQ2NZInyxBZvvuhmY_4teaPuicVqlC1iE7BllzlEq7C5dCR9s-Tl-q-3SvSzyYj7sMd-ppx4EhL6qM7syYLSHdQRMEEY8yQc4mK9_iMGp2k2t35I1qQGjnnYfL84HBgWDEqx2SCebiBegjPcAn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8587c2b060.mp4?token=iibpne0Qzkf4p3pGanCjhpO8TdSZUoryRvq8B04paE8aKiZOi4tIv4SXDaRcZ9WSHA4v9Xkf5AOkDEav866Mjh6GDFyRy6pfhOsKZ5zFleHcETBivqNjI6UKFJOetzYrMqrzgUFvHbMvXR7BsE5ZJPuiq17dV8J21ubasXnF7FjBgvZ2eUVhhrj5WonRV43X85IOJh9aW7-sFz5jNekRr8e6miWXgXSgn7LCw_mZ5S_YySeCO4G0j8GZmJYpsQAuavb9a5jUZEnSTkE03Nci6T1ZlNLHrgUZRdUwxrkv-eB428VOQzlwOK4w_NArbo_WbqJ7JrxCp3NEzzAFmj9P8ROQv1vldqpLnKkvuPA2zKiVetoVRn62sIyNSMSDcyYMNNmYkybXfChNMU5AVIFeGPH-aDRIo4Yot5OA3bh1abt1FRJzAEOV2rzFMAh76vArNqkHiOtI76e7LOE6ol2ZxYZh_ABCGS-sVR2RWDChv0hYe964mzSII5kX2gc9E6y_G9eAhaLPkG6YjwNP340KRlC_GQ2NZInyxBZvvuhmY_4teaPuicVqlC1iE7BllzlEq7C5dCR9s-Tl-q-3SvSzyYj7sMd-ppx4EhL6qM7syYLSHdQRMEEY8yQc4mK9_iMGp2k2t35I1qQGjnnYfL84HBgWDEqx2SCebiBegjPcAn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ هدفمند رژیم صهیونیستی به بیروت  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438482" target="_blank">📅 19:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438481">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/149889b796.mp4?token=j-41FzQtM3Ygc0YYScZjQtJXGic5Ee80ivYLqlCRsLr6dgRXr4L5zoHfaQBur_JNWElrI0uTYMevCgx9vwrNx_kR9nY5i758uCvclkdWRnl2ShAG_iMM-MgbD8glIgop5DdE4QVIUDxtzzro_-5tV9BX_HVFNKjobFVYnj4QezZ4rMxFQUKXjf9qTseXy81RG4b4YrZ5vE7CNFf8Agh57-6KwkC6PtHWFlQ5lbiEr1vjgoiXFXeTxh7mlRtPS5U_3N8h60np_tir2_-N3yNon6dPa6P9xqU6bkMszKvgP3XpkRMIWF91Rfrhb6SqaOC2kGxJtFKiGLiQZ-KPRRns1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/149889b796.mp4?token=j-41FzQtM3Ygc0YYScZjQtJXGic5Ee80ivYLqlCRsLr6dgRXr4L5zoHfaQBur_JNWElrI0uTYMevCgx9vwrNx_kR9nY5i758uCvclkdWRnl2ShAG_iMM-MgbD8glIgop5DdE4QVIUDxtzzro_-5tV9BX_HVFNKjobFVYnj4QezZ4rMxFQUKXjf9qTseXy81RG4b4YrZ5vE7CNFf8Agh57-6KwkC6PtHWFlQ5lbiEr1vjgoiXFXeTxh7mlRtPS5U_3N8h60np_tir2_-N3yNon6dPa6P9xqU6bkMszKvgP3XpkRMIWF91Rfrhb6SqaOC2kGxJtFKiGLiQZ-KPRRns1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکی که با آرزویش در برنامهٔ محفل همه را غافلگیر کرد!
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438481" target="_blank">📅 19:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjzMVtXX3AZ9HCUFNXbQNJ6W9N2Cx3fyP0nv6lLLqeqixqZ78S3Yju9s6NmFPBV5rYzg7dLvGF69J240Pfda6vlafG-ErKiqdbNpgirYV9MDxycO3uRc4ZcBMw59otEe-Loj53xgenwZfGw7aLPrHP2nE696O-bbxdaykHWi65g_Rs_uB1VJ6OBmZJYMlzY1eiZVRIfGvOKk9NbaNTpUKaACI9vVaNDVzczy5O569hBxNjeJYbPEsDPE-nNCc_G0dqKA7nxtsQNf7rmP96G779jVQqgKnU4ITrWhnJmUT8zbH-S2INlMBfRKkYbQzk1GR9q0pM7ONpk7Czxepv-WEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج‌فارس، در فهرست سیاه آمریکا
🔹
در ادامۀ دشمنی و مواضع ضدایرانی آمریکایی‌ها، دولت ترامپ از تحریم سازمان تازه تأسیس «نهاد مدیریت آبراه خلیج‌فارس» خبر داد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438480" target="_blank">📅 18:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438479">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d011e645e.mp4?token=bdDojDcRaNsmDt9kKEzTc5EPHQBs0iUIsb0cbl0XM5_LOywsH2i_0ChksrZqCTWwep3dIgdQdPa6DQpF69oBhMug_DkE7QeSseFO95x1ijiFC9k78xDDHGxGGMZ6JkDZpKNUUQ4-xBQBL7YKu7GtVSDOfrX3NlAphse-JJkHIQrFFlcNBbbto31KvWzbvVBcxpq6on_LkmvgwtB6B0ReiGUUT__WU2NhAE7SqRRHZn3XIuTT9o_bBwEUSXHQIhb417P1EjyLUxrIAiCg1b2MBH9fjfzE3nkPjh1NclGDCO3T-TR6BjeoFAR-1dbG0arHOb7QvIvB5yDRs5ZsUeqRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d011e645e.mp4?token=bdDojDcRaNsmDt9kKEzTc5EPHQBs0iUIsb0cbl0XM5_LOywsH2i_0ChksrZqCTWwep3dIgdQdPa6DQpF69oBhMug_DkE7QeSseFO95x1ijiFC9k78xDDHGxGGMZ6JkDZpKNUUQ4-xBQBL7YKu7GtVSDOfrX3NlAphse-JJkHIQrFFlcNBbbto31KvWzbvVBcxpq6on_LkmvgwtB6B0ReiGUUT__WU2NhAE7SqRRHZn3XIuTT9o_bBwEUSXHQIhb417P1EjyLUxrIAiCg1b2MBH9fjfzE3nkPjh1NclGDCO3T-TR6BjeoFAR-1dbG0arHOb7QvIvB5yDRs5ZsUeqRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر خیره‌کننده از حضور بی‌نظیر مردم ارومیه در تجمع شبانه
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438479" target="_blank">📅 18:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438477">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-48.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/438477" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-47.pdf</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438477" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438476">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0520652d2.mp4?token=TpnVRbj_ohsys1Fdem-9TTTmao2cOjoggU7PTXQ0QAW-GKH6DAocGE8zz1R-8hbWcPKtEvZGh8SFd-1kb74o8rEsS6mgwnx3WEBlbJv-fs35QzlOpk8GJSYlwQzVMhGbGkAB_R4KwXhrkx3jQwOsN2Hep8WXGNv-BEXnAzjR16K8aI-MZqbQa6KxbnUAbiQs42WlShI3Qm0xlUMjVn8FhTtvLiKBKU04g_LDuasUwGpbfKkcuRE7uHwB1-XkkTGk1a8VZjqczVX-GvSKDbXIruteej2v_bw-eKJigszgL-3vrO1HLFb7sJ2cEfDxR4qZD3cGGhFMB_ryQojpC6BemQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0520652d2.mp4?token=TpnVRbj_ohsys1Fdem-9TTTmao2cOjoggU7PTXQ0QAW-GKH6DAocGE8zz1R-8hbWcPKtEvZGh8SFd-1kb74o8rEsS6mgwnx3WEBlbJv-fs35QzlOpk8GJSYlwQzVMhGbGkAB_R4KwXhrkx3jQwOsN2Hep8WXGNv-BEXnAzjR16K8aI-MZqbQa6KxbnUAbiQs42WlShI3Qm0xlUMjVn8FhTtvLiKBKU04g_LDuasUwGpbfKkcuRE7uHwB1-XkkTGk1a8VZjqczVX-GvSKDbXIruteej2v_bw-eKJigszgL-3vrO1HLFb7sJ2cEfDxR4qZD3cGGhFMB_ryQojpC6BemQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌نوشتهٔ سیدمحمدباقر حسینی خامنه‌ای، فرزند رهبر انقلاب و نوهٔ رهبر شهید خطاب به مادر شهیدش توسط یکی از هم‌کلاسی‌هایش خوانده شد  @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/438476" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438475">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b107b539.mp4?token=RA265Cr8KR4Kgtjq54OHqbCwHfMLJaVcCIVSgpTEnZ4ZNAHBmgvBDBP4X3jwBPYmrk9gnQcuauFYuhwIEyhVqILOi3xBKLqO-_yKpP43iCThh_OqsrL8DOG5s6kq8QXvJolgQWdiqgdpr7yjUHaAUZDnmLV22Cc3RVqJzE_u13eKAH77_Unp2Q0QpynRWmDz9xWm6nbRZbe0yW3c0f9kGPfZZMx4jZb1z6IS5PPWKoof5gImF3xITGAA5CZh2Pa2pKxa1UsALXp2vTQ6Pzr1IfxEoQdqhLR_jpHRCa9DY8YRuo9ttKqLX0gXspJyCF5UthHCj6a0KNN2Nq3rMGYSTZIYk1tVHdWPA31lLQL-j7SF4vw8cZhLsSR35yO2Fl4eYwefdxRbTLfQQgH9RZtcZuqD3u2n__EG8gr807VziLLliXAPMrtbkNpDNt8gHEXzL8wwpzJ8mim7SvbfnaPacqS9HMMTt5zAwhJPhYzDJWCj07ASBu8FU-8xJiA_i-UsyAG3qOmccVPavxMuXKBSSNrpGHU7tKh-htJwqIJ0hhhmfHlFXIeFsyNMKFJVYXQqVT-llNpLETh3yC3zS19GF3ZtJqBi8E1V9-4CjkXAG2AhjHEzK5xGzeCpQWfJUsvwISZ45jpAQB2_EdsT67RM2FXJjli74zWQfc7iQgNV3-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b107b539.mp4?token=RA265Cr8KR4Kgtjq54OHqbCwHfMLJaVcCIVSgpTEnZ4ZNAHBmgvBDBP4X3jwBPYmrk9gnQcuauFYuhwIEyhVqILOi3xBKLqO-_yKpP43iCThh_OqsrL8DOG5s6kq8QXvJolgQWdiqgdpr7yjUHaAUZDnmLV22Cc3RVqJzE_u13eKAH77_Unp2Q0QpynRWmDz9xWm6nbRZbe0yW3c0f9kGPfZZMx4jZb1z6IS5PPWKoof5gImF3xITGAA5CZh2Pa2pKxa1UsALXp2vTQ6Pzr1IfxEoQdqhLR_jpHRCa9DY8YRuo9ttKqLX0gXspJyCF5UthHCj6a0KNN2Nq3rMGYSTZIYk1tVHdWPA31lLQL-j7SF4vw8cZhLsSR35yO2Fl4eYwefdxRbTLfQQgH9RZtcZuqD3u2n__EG8gr807VziLLliXAPMrtbkNpDNt8gHEXzL8wwpzJ8mim7SvbfnaPacqS9HMMTt5zAwhJPhYzDJWCj07ASBu8FU-8xJiA_i-UsyAG3qOmccVPavxMuXKBSSNrpGHU7tKh-htJwqIJ0hhhmfHlFXIeFsyNMKFJVYXQqVT-llNpLETh3yC3zS19GF3ZtJqBi8E1V9-4CjkXAG2AhjHEzK5xGzeCpQWfJUsvwISZ45jpAQB2_EdsT67RM2FXJjli74zWQfc7iQgNV3-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزار مرتبه جانم فدای خامنه‌ای...
🔹
مدیحه‌سرایی مصطفی سماواتی در مراسم یادبود شهدای خانوادۀ امام شهید و رهبر انقلاب اسلامی  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438475" target="_blank">📅 17:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438474">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83d18d28d.mp4?token=epYeTwisuPXYZKlcJbDJMXbY7Lc8WQ9lAsaPmy8LPQEyYwVSySulAKkEhJV1en_0NsigZjL8PlR3FDJobbudZ3Ya_txJEV431GuI0Gw2OagGdWRERSwuTWMyeBWE4vuJ8l3v1Z0TpvyjK2jzQroiMCZQweUmNCzCe4EPvoUKSHp_90tFdp3OwXxcFfb5V-aTPStVeQ0JGUPRvza90Gk4nnbFFZdBhc1SKzvUCTAyhtIw6yfVVkTuxHYt6tcmhIZvGJn98rw7Lwc8ixa4Z4x0XJjRP3E2qdHQ7nkd-ihQsyADRvbuEUI2n1B5jfz16-OkHvTJloTGY86tj11JQeXkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83d18d28d.mp4?token=epYeTwisuPXYZKlcJbDJMXbY7Lc8WQ9lAsaPmy8LPQEyYwVSySulAKkEhJV1en_0NsigZjL8PlR3FDJobbudZ3Ya_txJEV431GuI0Gw2OagGdWRERSwuTWMyeBWE4vuJ8l3v1Z0TpvyjK2jzQroiMCZQweUmNCzCe4EPvoUKSHp_90tFdp3OwXxcFfb5V-aTPStVeQ0JGUPRvza90Gk4nnbFFZdBhc1SKzvUCTAyhtIw6yfVVkTuxHYt6tcmhIZvGJn98rw7Lwc8ixa4Z4x0XJjRP3E2qdHQ7nkd-ihQsyADRvbuEUI2n1B5jfz16-OkHvTJloTGY86tj11JQeXkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امنیتی وزیر کشور: شهید پاکپور میدانی‌ترین فرمانده تاریخ ایران بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438474" target="_blank">📅 17:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438473">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm0ytBfOM3MPUek0AdXhziLUECneeYzg8jkPF2qk0NDnxD7TnimxNT7BpsBNjSkzQLwMT5BJUf5wHul6OCBrwWx1JeIBJyCWeGzRhc--gsuDXsxYXWGaQNTWEfNqTlLIZ4A0kVsYk8T5k3FZrT62r3UsQKH0dA6Pd_5T-9DSQrpMxYeSPcwb7Ag-9rHxI-VD1Rewb0K8ZsH2Q4_zUz-wVwXiH7bPEKsNGTq_spBi9tYcJzlXgg8jzj7pwDKUkMdyrnMLqMTqdqDtv2diT1EdUHOO-hqnZMtkKGUoS2NU2VyuTMLbtuhVJRAj73ZhZYhoWSkNleWTaVsbJa0zOZsbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان روز ملی جمهوری آذربایجان را به علی‌اف تبریک گفت
🔹
رئیس‌جمهور در پیام تبریک روز جمهوری آذربایجان به رئیس‌جمهور این کشور نوشت:  ۲ ملت مسلمان ایران و آذربایجان دارای اشتراکات فراوان تاریخی-تمدنی، فرهنگی، دینی و زبانی هستند و این پیوند، دوستی ۲ ملت را مستحکم و استوار ساخته است.
🔹
پیوندهای گسست‌ناپذیر ما، سرمایهٔ گران‌سنگی برای توسعهٔ مناسبات میان ۲ کشور فراهم کرده؛ جمهوری اسلامی ایران پس‌از استقلال جمهوری آذربایجان همواره از توسعه و گسترش روابط مشترک حمایت کرده و خوشحالیم که در راستای خواست و آرزوی ۲ ملت، امروزه شاهد روندی پویا در روابط ۲ کشور هستیم.
🔹
امیدوارم که این روند پویا که طیف متنوعی از موضوعات دوجانبه، منطقه‌ای و بین‌المللی را شامل می‌شود، همچنان با قدرت و شتاب بیشتر ادامه یابد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/438473" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438472">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c1eea896.mp4?token=QJXytk0HIqhdzlbPVllBgSLpHMlTM9AMrZfQFjMUr2GaV0rG_XWVEsUeQJ0bghIo7CkbZmjiPdUwUsK7-pn4bqX5qQdVNNKJ_kzAsPobq8Tt16msJqKh10SmsLy5ERL5mDP5_bKytPOm07-LgdPPHAvEw6dKNnRjdPRtTUhsDLofaRHlQVeos1cKui3A4HaXoAZJ7TKljxZpZRVhc6YRc0SNn97IdF48JKZt5oemK82m8hDrJ0m8FgCmN44J9m23cvyU2yLCkuqkUQgqLN7S9ajHUyu5OfDnv0xuGfLmgQwsOnLeue6ZKuQBiKsFyNsF62n2SCJTUj2hfdCOeWwjgjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c1eea896.mp4?token=QJXytk0HIqhdzlbPVllBgSLpHMlTM9AMrZfQFjMUr2GaV0rG_XWVEsUeQJ0bghIo7CkbZmjiPdUwUsK7-pn4bqX5qQdVNNKJ_kzAsPobq8Tt16msJqKh10SmsLy5ERL5mDP5_bKytPOm07-LgdPPHAvEw6dKNnRjdPRtTUhsDLofaRHlQVeos1cKui3A4HaXoAZJ7TKljxZpZRVhc6YRc0SNn97IdF48JKZt5oemK82m8hDrJ0m8FgCmN44J9m23cvyU2yLCkuqkUQgqLN7S9ajHUyu5OfDnv0xuGfLmgQwsOnLeue6ZKuQBiKsFyNsF62n2SCJTUj2hfdCOeWwjgjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون هماهنگ‌کننده سپاه: شهید پاکپور اعتقاد ویژه به مردم داشت  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438472" target="_blank">📅 16:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438471">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9834fbae49.mp4?token=dsiVdTDZS1FOW7Jzm2zFirJRW5wytRupuP5wVL3yYq_oCwnxTR2AF6jba7f1siQ_-_MxPR1UuofQ6VNVZ_nYFe3LqkkFza3-_XxbJ5mi3izy3fyFE4ooL_gFy_OaTq9GFa7ck6U2Fkg9FrqOBEVLTdcaxMD_nLjr006LCq7TcopjP-cHQf2-4mWWboEbWqTLvXXm1Chbneeex0WUvELyVS5iOgPCk56nYP1l3ygUJcxKqIssD97M1wlIQm4eC-tiBHoX6MobAFSe6m8yGZMRWey3b3mctf7RBN1trPfAPkf1I7QfyE4yZlaTW4W8FaYKC2v5K2kTyVeKD6zOnAzgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9834fbae49.mp4?token=dsiVdTDZS1FOW7Jzm2zFirJRW5wytRupuP5wVL3yYq_oCwnxTR2AF6jba7f1siQ_-_MxPR1UuofQ6VNVZ_nYFe3LqkkFza3-_XxbJ5mi3izy3fyFE4ooL_gFy_OaTq9GFa7ck6U2Fkg9FrqOBEVLTdcaxMD_nLjr006LCq7TcopjP-cHQf2-4mWWboEbWqTLvXXm1Chbneeex0WUvELyVS5iOgPCk56nYP1l3ygUJcxKqIssD97M1wlIQm4eC-tiBHoX6MobAFSe6m8yGZMRWey3b3mctf7RBN1trPfAPkf1I7QfyE4yZlaTW4W8FaYKC2v5K2kTyVeKD6zOnAzgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📝
مجلس يادبود شهداى خانواده امام شهيد را در پخش زندهٔ فارس ببینید  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438471" target="_blank">📅 16:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438464">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43311032d1.mp4?token=iBAZd3Mrs_JGcnXjFml6FerMLmGWZeFX6ADwf03rqfyIYPK1nAZ5yrvvSz8sV4EALQwrwwu3VqUi0X6zRqX7XGrC4_vvoj3Qw4c3VbN1wLI7hXtdAJT_68RoysXwPMP0csCnAN2kHdVk2gQyFO8Kp-Xr4D_haqPp3VOaU3X51TEv2jkYEfU1f2yml4TbC2F43nmoRXHZi24fftts6IfH9Iw0asThnaCV2P78hV4PBzJAWjAMQSe2JMlU26kled8HURvM_6Bni5HArdbVX16qI4E_2iUA7QXqT4JcqpaidzOk4J5yOZHXi7MSwTOMUcJIWNJdzBtk3U9yGVtfWG3Skw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43311032d1.mp4?token=iBAZd3Mrs_JGcnXjFml6FerMLmGWZeFX6ADwf03rqfyIYPK1nAZ5yrvvSz8sV4EALQwrwwu3VqUi0X6zRqX7XGrC4_vvoj3Qw4c3VbN1wLI7hXtdAJT_68RoysXwPMP0csCnAN2kHdVk2gQyFO8Kp-Xr4D_haqPp3VOaU3X51TEv2jkYEfU1f2yml4TbC2F43nmoRXHZi24fftts6IfH9Iw0asThnaCV2P78hV4PBzJAWjAMQSe2JMlU26kled8HURvM_6Bni5HArdbVX16qI4E_2iUA7QXqT4JcqpaidzOk4J5yOZHXi7MSwTOMUcJIWNJdzBtk3U9yGVtfWG3Skw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام جزئیات اولین یادبود شهدای خانوادۀ امام شهید
🔹
آستان مقدس حضرت عبدالعظیم حسنی که پیش‌تر از سوی رهبر شهید به‌عنوان «قبلۀ تهران» نامیده شده بود، با نظر مقام معظم رهبری و بیت معزز شهید، میزبان اولین مراسم رسمی یادبود شهدا خواهد بود.​
🔹
این مراسمِ مردمی،…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/438464" target="_blank">📅 16:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438463">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55a46cd00.mp4?token=Iv3BkoTy7utUSVA-8N5mn--uqvmk11qdbNpIn_kFeE6MHrjkjf6jUL2SeO17z__Lt0dgRg9o1xnIUQH9qbuxVv3qgdEBzQhTNKPhrcHtsduO_SpTuZqBgBudDSgtl2IjyfTgNLsVpTsyVu_28OgKjmFU6H-R2sbUdn8XIqXtgstDsAXoObIXyWsliQh4EvyPqu0WOavFApLU0UzUc08-bkflRExHzPy0CSnSWTW6mGb2IUrdHHCb1HLyZu1Smd0m7MbZyMO014xajjlIHBdfXWxu_w6Xr-AYDM9PwXnwE9Qnhy1PKc-yLN7FU8bBvuZV4yYtencRK8676qX4nktIVQFR2eCpg7ynGxBuP36fDnML9ETaWDBDMWrxlNs--nd4o6U3uVotw2PXWr_IRtGryjz7evotkZZobdhw_a2WolJc_ipkUmFXzceavWUbAubT4sN3m0fDa969rYHeJq6J7SYh0Yt9WQjjKOFA3DDuYWJF4DqfG203giLxXpAriZDHcqgTFade3lrQXX0sTFSvFQCBPjhlgp73ax0YdEH0lpHg6Z53dkBHlu2Q-HLHR1TbEPG8iu46RBS8W4JsMIR3mLgpLdATitoiBEPSTGz343nCYrK9MTMKgu8JkwUrderyjGKvZqKFybBCqS-9SJ4NiSbCHpThvn27YYr8CZnMV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55a46cd00.mp4?token=Iv3BkoTy7utUSVA-8N5mn--uqvmk11qdbNpIn_kFeE6MHrjkjf6jUL2SeO17z__Lt0dgRg9o1xnIUQH9qbuxVv3qgdEBzQhTNKPhrcHtsduO_SpTuZqBgBudDSgtl2IjyfTgNLsVpTsyVu_28OgKjmFU6H-R2sbUdn8XIqXtgstDsAXoObIXyWsliQh4EvyPqu0WOavFApLU0UzUc08-bkflRExHzPy0CSnSWTW6mGb2IUrdHHCb1HLyZu1Smd0m7MbZyMO014xajjlIHBdfXWxu_w6Xr-AYDM9PwXnwE9Qnhy1PKc-yLN7FU8bBvuZV4yYtencRK8676qX4nktIVQFR2eCpg7ynGxBuP36fDnML9ETaWDBDMWrxlNs--nd4o6U3uVotw2PXWr_IRtGryjz7evotkZZobdhw_a2WolJc_ipkUmFXzceavWUbAubT4sN3m0fDa969rYHeJq6J7SYh0Yt9WQjjKOFA3DDuYWJF4DqfG203giLxXpAriZDHcqgTFade3lrQXX0sTFSvFQCBPjhlgp73ax0YdEH0lpHg6Z53dkBHlu2Q-HLHR1TbEPG8iu46RBS8W4JsMIR3mLgpLdATitoiBEPSTGz343nCYrK9MTMKgu8JkwUrderyjGKvZqKFybBCqS-9SJ4NiSbCHpThvn27YYr8CZnMV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون هماهنگ‌کننده سپاه: شهید پاکپور اعتقاد ویژه به مردم داشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/438463" target="_blank">📅 16:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438461">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c73bcbed.mp4?token=Tfe-FYcCXtU6PYq_P_XlDvuvP9Er-3s6XY42bA9pnfdN8yxJAlgaanJlHiFnRQKaVZ8P7RPHdb4fTIUvQDiEjVBgBauDjXxutSKbGTQVrW9hcdRpStTRuqpnwUv3xtyTkcG6xFcv4tzbGCC8-4YIpNGH9Zw2RM5mZLKU4ykcp1K7kO5usjuRQ2YgieSZX7_HhkvSQOVFDJw_0DxxLOYC3akpHEpUKKV0pcyGFV-_dI1dzhdUuGzZlxcELJuJGKX6f4TM56E7JQw_GM6_uHSRoy9WxItYrkvAQ5vuFDTxapaIh6lskMF-0q8Es1xFObcsPlfiiTQG8LPreJ92aoplPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c73bcbed.mp4?token=Tfe-FYcCXtU6PYq_P_XlDvuvP9Er-3s6XY42bA9pnfdN8yxJAlgaanJlHiFnRQKaVZ8P7RPHdb4fTIUvQDiEjVBgBauDjXxutSKbGTQVrW9hcdRpStTRuqpnwUv3xtyTkcG6xFcv4tzbGCC8-4YIpNGH9Zw2RM5mZLKU4ykcp1K7kO5usjuRQ2YgieSZX7_HhkvSQOVFDJw_0DxxLOYC3akpHEpUKKV0pcyGFV-_dI1dzhdUuGzZlxcELJuJGKX6f4TM56E7JQw_GM6_uHSRoy9WxItYrkvAQ5vuFDTxapaIh6lskMF-0q8Es1xFObcsPlfiiTQG8LPreJ92aoplPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژهٔ ارمنستان با سامانهٔ ایرانی و پهپاد چینی
🔹
ارمنستان در رژهٔ روز جمهوری خود انواع تسلیحات و تجهیزات خریداری شده از ایران، روسیه، هند، فرانسه و چین را به نمایش گذاشت.
🔹
راکت انداز توس-1 (TOS-1) و سامانهٔ جنگ الکترونیک Pole-21 روسیه، تسلیحات هندی شامل موشک‌های MLRS پیناکا، هویتزرهای خودکششی «سزار» فرانسه و سامانهٔ پدافندی ارتفاع پایین مجید ساخت ایران، از جمله تجهیزات رژهٔ ارمنستان هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/438461" target="_blank">📅 16:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438460">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEEuBC9KInFZVImAe5oR1zWcQUM9FccESwdjdxEZmvcHelKZo3cZ7_6dgVbyLy3X3AeMtJgNuTB8f1c2uZUcizOK1dAqJgffSm03AEFQr8x14Da4zNxI-aJMWA_n7SE9lx4O2sdorXFIXT13MQX9cm-__IYN4ClkoODp8sDUPTKXOIUZIEsBoCAuLVR61nj26D2w8v_zk9tAwSaxOx6vbXuP5KQLVUV5f1NQbomrXWp46quTBTy4uC6nltvmnP2Pyr0xi9CWUyY5HMCOLhf2CdylolZ_V3bmIKKSoKVf4KmKLiZ1RwOBZaY9h-OPOayDKMaOz-TpXRzrl7YcywTkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتارهای ضدونقیض ترامپ زیر ذره‌بین روان‌شناسی
🔹
این روزها مردم جهان از حرف‌ها و تصمیمات رئیس‌جمهوری ملقب به «مرد دیوانه» بهت‌زده مانده‌اند و او را با دروغ‌ها و ادعای‌های ضد‌و‌نقیض‌اش مورد تمسخر قرار می‌دهند.
🔹
برخی‌ها نیز معتقدند که دروغ گفتن ترامپ و تغییر تصمیماتش در کسری از ثانیه، سیاستی است که او برای پایین نگهداشتن قیمت نفت، گول زدن جبهۀ مقابل و درگیر کردن اذهان عمومی استفاده می‌کند.
🔹
فتحی‌آشتیانی، رئیس انجمن ایرانی روان‌شناسی: ترامپ، شخصیتی خودشیفته دارد؛ با تمام ویژگی‌هایی که یک فرد خودشیفته ممکن است داشته باشد.
🔹
خودشیفته فردی است که خود را کاملاً قبول دارد و دیگران را به‌طور کامل نادیده می‌گیرد. از دیگران سعی می‌کند بهره‌کشی کند، دقیقا مانند رفتار ترامپ در برابر بسیاری از کشورهای عربی، مثل همان تعبیر معروف که می‌گویند او در حال «دوشیدن» این کشورهاست.
🔹
اگر برچسب «اختلال روانی» به ترامپ زده شود، مسئولیت کارهایش را تحت‌تأثیر همین اختلالات تفسیر می‌کنند و می‌گویند رفتارهایش ناشی از بیماری روانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438460" target="_blank">📅 15:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYUfnlbsin793WE8SomymNXL8LJ9EBxViZNojwQSPG3_jI7q5e_ZRCVzPP_jtcLrZ1STrGk8KwnYm2WoVKDT7eB3XfOSdWrp77IFaZ81iw1kRgDOhZQzxmTw4f4Ayu_ZjPaxj6RONGzNDxApF4ZYTWIbg6W-YYcrLQLVsBLqv9POsDeRC2G0eiM8RPmOpPUvKEtKYFTXDWzJSnkoKtfFeFLecWqHfQon4JWjd-xB-9-QVsUBpto8qYGrVsNM1kdCsJDMxmPzsU6sg6P4qx03ckGDszE2jUgvMd8ER_CP0PlRggdXsZoj1VzjuszE2C1NUSmEpGlXlrQj5lpotyQtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je4yvLe7heGAXpfQDis37NfHx6--taqR6CrG4978Rgg9ZhHARWnCt-yTI_3MZJLF3jSLwuE-u-yiVc0yjveatNVDeW8jeo2268WK7ZypU2X-2bAuJWVFdrwhaUjoFIet7__Uovl7sy09g1FYuWXDJREvAbLqmcov9jlDRyKpDJBu56znoYYmPhjnR0nFbM2QW9_O6mgC-lvvaVvLaPIXR8cQVogQ9Mk-H9p0SSiyTf1ZiTVqTV4nW-DUw4_xPgFoeCzgh7YSRCF-ITtJZUubCqevRShVEtAAAihuLk2Zyi5CFpII0me-tF09ahQotg-_h1JwmXbxCOcWc30XXXAo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YH7FWZ4ADqIwCxmc2LX2fVW5sGpgeOJWYvcv_ML0nAYe04QOUsiEUvTicW8OTVQtT7uJvFaLASuJNuSLfs64_lvLPfYyRZzcyBj8M6UV28saox36gfceKVGeS8rC6qA-5kiHSxbPqCvEIzv5eYzPb5rdVKD2u6cb-Upskh4rf-XiNIj9KXpkL1BUMQkK_n18abfR20mQ3-re-o51PsQuDpdfwQi4BPvHU7WynJ1uTeNWIDImWi3I3XvpQZzQiIIkcG085xS6Yb2cQLCGDobRcy54N5vvNm-ijziR-z1sRMP0r_IZN0KhhlF_igyVabC1i_UMS1uLEiOCUaabd1UBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1pd7l7IMUNW-iNA4Qxx_x1ApH3D5q4iOqN_pMdhd41Eb6Z2p-fm6INpifZySGGjtG7HrmW9e0KGnQd67vx3ryCUUZc7B6jC2_1G2g4nNq8qkR9h-lBKNQFal6htnwVSkFKDknicUioU_guTG1KxHc7pgmnP0UFFWiPRqrVFElNjQiu5XTqPUY6n7c6tU4Tc6FnVya5nE0JuImwAtV2YMO8PshPRGHMOLk4gIzZRIxI9dOUkBI0b30OVsq5tq4r0qr-4bilr2NmhQcWpWELnEKHJIs1VSqGkn6tq6vrAqIfOhFPGNn-Qo9eTY8eO0cE6cAhfYtSVHgydAhyuLCgrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rU-RLVVs-N9UarNo8vUzorsBbKE_NI_KCWHaYImkUpMm87WcvBT9qymQFyZN7RFXJmk8NfcPOStKwvgig0n2KhgUZxOnt-Z12CdbRLw6_S5Wo9uxJrvCo1mBc2wWamRsivAHY9iL2zrvTId0gwe_xxZKuEtUK9X1q-o6mnmDksd0p9cAhgXyXFv165MgfmPmySbQVqjzqdyGTmJlV4QPhpwUckXK2Nt_PstAzx5YmicsRk7DkCqmLxMMIqwH3JRDyuL2DO3BEhTwcILFcsLlsEMCxWIk_raLwjtwZboGmdOt8mKMhlminmvfr6egU2DJOGbqAgqoh-7ziqLULNv1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juYVaplwhIxaVfLdKIr1cnFWfPqgdGyif26AidoTFbjunioRedcqowQr8ThAtXedNjDfBi9qS8BT-dmIar8CMk__zmoyUaLWKSeKbmFqd8F-AVR6bP6453HOsdqmvHb73xX4pbk9DL7Kzcsm9YHnIyK_39YpinM7Wh1fJLYYqNNz9-qXfaTS6tk7IN9511UxV8slXhOGUE5lFd75ceucd_fDLp5EWbV5WrBarI-m9kvIfKd8vvIxh3olU9Vd4ae105JifOVKceDMR1qb0iDFWAeHLatHHdhmDO9CI6Q7qlVJJwe91mIZPu1f7VBx2amaIFhMRvwhXYLkR0MXt1oNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftA2O_cuZFVazQ0fyEyteQBZ_M6N-Kee2RlWHJW08rJSleYNh2rhsePnX9LICN2YVP5sZSAwOEyYCaNsWMCvSp03fy-bbD5yygJBVkAuRLFMHDbnMWjmOrxI0931TvGFVfqGSU9r_GKsjlvOyt7TaJdPvhpncBE6YmN-rLwjFAzmh3DYYaA-CAEFVcNIiXwfIy7F2gq5rnZXQ08VPaTJ2b42cLWqcRaLz3zg62GgaCybP6pbODQUTIpsIeFcxWEXRl-Pmy6KzLSgEUj8XZyMlHRjFAcHZItEuQAliRSCjQjMHYpMTm2EUXblDOu1oeMSo7cquAGrbCEijEKeygfNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
«اردی‌بهشت کتاب» تمدید شد
🔹
رویداد «اردی‌بهشت کتاب» که با شعار «در هوای کتاب‌خوا‌ن‌ترین رهبر دنیا» در باغ کتاب در حال برگزاری است تا پایان فردا تمدید شد.
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438453" target="_blank">📅 15:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0370276cb1.mp4?token=hnle2TUeWBz6vPtw802bKz48durmASeqSw9kccpBGHNDt6RWJQE0yfva9MS43WU_FiWDIIhnUzL03mzX4fL74r0T_DRm6LuW-bnVDIgfQAjo8MZNa65jzeyE61YjUld0dXWWq6UV1S1romS-b7jeSv3PBefhrB2w30Wsg785aTqhq1OMmM0YLpZAAhowtNInE2anOiEtSMSGRAEnUJo0gARtQyXkgT5DwfCrMBriXrVg-yrX-aIE68weM27dfAPZCDSWiEw4nexA4OV8_yKu5d2SycKSr8eQfZVCcGVNGvPK1PwSib8kvWrJpaEHkeSxm12pBi9wS-fr6AYg4ceE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0370276cb1.mp4?token=hnle2TUeWBz6vPtw802bKz48durmASeqSw9kccpBGHNDt6RWJQE0yfva9MS43WU_FiWDIIhnUzL03mzX4fL74r0T_DRm6LuW-bnVDIgfQAjo8MZNa65jzeyE61YjUld0dXWWq6UV1S1romS-b7jeSv3PBefhrB2w30Wsg785aTqhq1OMmM0YLpZAAhowtNInE2anOiEtSMSGRAEnUJo0gARtQyXkgT5DwfCrMBriXrVg-yrX-aIE68weM27dfAPZCDSWiEw4nexA4OV8_yKu5d2SycKSr8eQfZVCcGVNGvPK1PwSib8kvWrJpaEHkeSxm12pBi9wS-fr6AYg4ceE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی: در حال حاضر، به‌دلیل جنگ آمریکا با ایران، وضعیت تأمین موشک‌های سامانهٔ پاتریوت پیچیده شده است
🔹
دراین‌خصوص به رئیس‌جمهور و کنگرهٔ آمریکا نامه ارسال کردم و در آن چگونگی تأثیر تأمین تعداد کافی پاتریوت‌ها بر پایان جنگ اوکراین را تشریح کردم.
🔹
اروپا باید در قارهٔ خود، از تمامی ظرفیت‌های لازم برای محافظت برخوردار باشد. ما به پدافند دفاع موشکی بالستیک بومی اروپا، به تعداد کافی و با قابلیت‌های لازم، نیازمندیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438452" target="_blank">📅 15:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">شکایت بین‌المللی پرسپولیس برای تغییر جدول لیگ/ قرمزها امیدوار به ۲ امتیاز
🗣
باشگاه پرسپولیس همچنان پیگیر پرونده مربوط به دیدار با ملوان است و مدیران این باشگاه اعتقاد دارند استفاده از سینا خادم‌پور در ترکیب تیم ملوان غیرقانونی بوده و این مسابقه باید با نتیجه ۳ بر صفر به سود سرخ‌پوشان اعلام شود.
🗣
مسئولان باشگاه پرسپولیس در روزهای اخیر با ارسال نامه‌ای به دادگاه عالی ورزش، خواستار توقف تأثیر امتیازاتی شدند که تیم‌های استقلال و تراکتور از بازی با ملوان با رای انضباطی کسب کرده‌اند.
🗣
از نگاه مدیران پرسپولیس، این امتیازها به‌صورت مستقیم در جدول رده‌بندی تأثیرگذار بوده و تا زمان تعیین تکلیف نهایی پرونده نباید در جدول لحاظ شود.
🗣
شنیده می‌شود دادگاه عالی ورزش نیز دراین‌خصوص مکاتبه‌ای با فدراسیون فوتبال ایران انجام داده و از مسئولان فدراسیون خواسته توضیحات و مستندات خود را ارائه کنند. گفته می‌شود قرار بوده فدراسیون فوتبال تا امروز پاسخ نهایی خود را به این مرجع ارسال کند.
🗣
در پرسپولیس خوش‌بینی زیادی نسبت به سرنوشت این پرونده وجود دارد و مدیران این باشگاه امیدوارند در نهایت یا امتیازهای مربوط به دیدارهای ملوان مقابل استقلال و تراکتور دستخوش تغییر شود یا ۲ امتیاز به پرسپولیس اضافه شود تا به اعتقاد آنها عدالت در جدول رده‌بندی رعایت شود.
🗣
بااین‌حال، هنوز هیچ تصمیم رسمی و قطعی از سوی مراجع ذی‌صلاح اعلام نشده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438451" target="_blank">📅 15:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سپاه پاسداران: جز با محو رژیم صهیونیستی، منطقه روی آرامش نمی‌بیند
🔹
بیانیۀ سپاه پاسداران به‌مناسبت شهادت دو تن از فرماندهان مجاهد و غیور حماس: شهادت «مجاهد محمد عوده (ابوعمرو)» به همراه همسر ام عمروو سه فرزندش «یاسر، یحیی و جمیله» در حمله هوایی رژیم صهیونیستی به شهر غزه و نیز شهادت «عزالدین الحداد (ابوصهیب)» از فرماندهان کتائب شهید عزالدین القسام را که نزدیک به چهار دهه با صهیونیست‌ها مبارزه کرد، بار دیگر پرده از ماهیت درنده خویی و شیطان صفتی رژیم پلید، جلاد و تروریست صهیونی کنار زد.
🔹
سیاهۀ جنایات حدود ۸ دهۀ رژیم جعلی و غاصب صهیونیستی بار دیگر این حقیقت را به جهان بشریت به‌ویژه مدعیان حقوق بشر و آزادی ملت‌ها تأکید می‌کند «جز محو این رژیم کودک‌کش و اهریمنی، از روی زمین، منطقه غرب آسیا روی آرامش نمی‌بیند و طرح‌های موسوم به صلحی که رئیس‌جمهور خبیث و قمارباز آمریکا از آن حرف می‌زند، جز کشتار، قتل و ترور نیست.»
🔹
شهادت این فرماندهان سرافراز نه تنها مقاومت را تضعیف نخواهد کرد، بلکه باعث تداوم جهاد تا آزادی فلسطین و قدس شریف خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438450" target="_blank">📅 14:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه
🔹
نیروی دریایی سپاه: کنترل هوشمند تنگه‍ هرمز با اقتدار کامل درحال انجام است و طی شبانه‌روز گذشته ۲۶ کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگهٔ هرمز عبور کردند.
🔹
دریافت مجوز…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438449" target="_blank">📅 14:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bac5da19d.mp4?token=MQMZ2NyQCYrrXWQB4arEIS7AuxvgH66W4xlef1GhwS0AFtqYXxf1U82pnE29WNdvnaIfrfRjxXAIQbQuS3vzvB8987HF5We8CBey6WXSksnSbYMToS-dn-VXE6LoCiphQH9yOkLYSItoSegrwQ7VltEiwi4Aam0VtpHGeuA16je07r-fkvvA6GlZVJKKcGHtdvhRwEM0xblVrKq1MEnSHwVu28Gs0yOlNufBmj6P5lksvxSTha3r_K_0UAoHWF_IKTauTDqcde0gda4qNmoy2A5uMZC5MuhWO9k8_lctYIBK6d-TjbuqrUkXhUyronkVd6IqDKX1DLU_NNZzOpV-sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bac5da19d.mp4?token=MQMZ2NyQCYrrXWQB4arEIS7AuxvgH66W4xlef1GhwS0AFtqYXxf1U82pnE29WNdvnaIfrfRjxXAIQbQuS3vzvB8987HF5We8CBey6WXSksnSbYMToS-dn-VXE6LoCiphQH9yOkLYSItoSegrwQ7VltEiwi4Aam0VtpHGeuA16je07r-fkvvA6GlZVJKKcGHtdvhRwEM0xblVrKq1MEnSHwVu28Gs0yOlNufBmj6P5lksvxSTha3r_K_0UAoHWF_IKTauTDqcde0gda4qNmoy2A5uMZC5MuhWO9k8_lctYIBK6d-TjbuqrUkXhUyronkVd6IqDKX1DLU_NNZzOpV-sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش پربازدید نشریۀ آمریکایی آتلانتیک از علت شکست ترامپ در حمله به ایران
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438448" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeece2279c.mp4?token=Q2TwiciSAyAny5KZWzbmA8qOwT-5M2v2prOPrjzMarcOyrRS_tqbK73fVVUeX5m3-V7wbsBB_NJCo1X2HfWlchYrAvyLz_ujAoodfCrAhK53va41-xejCxErdJJFz-JyzVhGVLU48uOolvrfgK1ES-XueDwdOjd00UG0W41IFHu5VFrdP7884FardnuF2UDn7G_Ob5B19-a1WZVs89GsbpNLr23tPOsZM-zn5ppXH1pxFy9PbVCi1prwvT3sVrILeoXIeBLQb2aPebXzdXfbcpWw9mlt6Hopke6rN9lvv7QEml0KPPD76eW8I_2cngTjoxkT9zMAlH0HUEg7tFTo8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeece2279c.mp4?token=Q2TwiciSAyAny5KZWzbmA8qOwT-5M2v2prOPrjzMarcOyrRS_tqbK73fVVUeX5m3-V7wbsBB_NJCo1X2HfWlchYrAvyLz_ujAoodfCrAhK53va41-xejCxErdJJFz-JyzVhGVLU48uOolvrfgK1ES-XueDwdOjd00UG0W41IFHu5VFrdP7884FardnuF2UDn7G_Ob5B19-a1WZVs89GsbpNLr23tPOsZM-zn5ppXH1pxFy9PbVCi1prwvT3sVrILeoXIeBLQb2aPebXzdXfbcpWw9mlt6Hopke6rN9lvv7QEml0KPPD76eW8I_2cngTjoxkT9zMAlH0HUEg7tFTo8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ هدفمند رژیم صهیونیستی به بیروت
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438447" target="_blank">📅 14:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaQ8HStdHxVXoSCRLNKdaOYOjV9z0tdRScNdSx8BAvwxTvkrAkZIXhxbdICCJIxtFGrDhEOL3BR7sTCxBJtABwdZS21DsNf1vaxXlhyApWPw22Z3mD18nNdqZ9QbtMf8TWac6Sig0Xdvqe6BqG0IhJJxN3EHsR8yByLql0NQN-Xr7b-b5HpH-RD13raLDKbP_TTxQp2bD7Lvru74jckW3-bkDDsMGoWX5gS7Kk1TJHoN47-iNiZ92gsDfdEHn-drRgrMTs2ewDRxu_CSP84mDI7scZilGdcb-x4GAoVHaaegkFb1aOyNZLYszS788nzQ0ITpUt1oLU0ScM1_DnCS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فراری یمن، در ریاض درگذشت
🔹
رئیس‌جمهور پیشین یمن عبدربه منصور هادی که پس از تسلط انصارالله بر پایتخت این کشور به عربستان سعودی گریخته بود، امروز در سن ۸۱ سالگی در ریاض جان داد.
🔹
یک منبع یمنی به خبرگزاری فرانسه گفته منصور هادی در پی یک بحران ناگهانی در وضعیت سلامتی‌اش، در پایتخت عربستان درگذشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/438446" target="_blank">📅 14:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنید
🔹
طرح و نقشهٔ کور دشمن پس از جنگ تحمیلی و فشار اقتصادی و محاصرهٔ تبلیغاتی و سیاسی، ایجاد تفرقه و تجزیهٔ اجتماعی برای جبران شکست‌های میدان نظامی و به زانو درآوردن ملّت است، و لازم…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/438445" target="_blank">📅 14:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfb4011b3.mp4?token=UCrm1e_ILjs8FO9HqsonP_gX-ZUSktKTpoCpSa2xjEHDooMNN3_YaR2tG-DnkOq7foaRn-hWWSjZ70pWVTRNgSVYj-XN5tRjwCLqB-fnRiQG5PwOdniCd21vFNgD0Q1AlDN1ogMoXFXOuWDJnXP9xhzdATIiJj6HKmJfBE9dP8vjnFc3JR-Er-dvysha09xdtugk4_JmUz2ZCZjCyJDylz-RTWC9Nn3F_daHFgHQKP4iS6979hH_hHGn3pmVlKAqOE_-_r4A1do-ETPTu75z_hLZy6Oqv2RT4ST2_VpHxqwJrAq8wNzovxRDekhtBwAIbVOChhq-Cwn5c2t21r_vNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfb4011b3.mp4?token=UCrm1e_ILjs8FO9HqsonP_gX-ZUSktKTpoCpSa2xjEHDooMNN3_YaR2tG-DnkOq7foaRn-hWWSjZ70pWVTRNgSVYj-XN5tRjwCLqB-fnRiQG5PwOdniCd21vFNgD0Q1AlDN1ogMoXFXOuWDJnXP9xhzdATIiJj6HKmJfBE9dP8vjnFc3JR-Er-dvysha09xdtugk4_JmUz2ZCZjCyJDylz-RTWC9Nn3F_daHFgHQKP4iS6979hH_hHGn3pmVlKAqOE_-_r4A1do-ETPTu75z_hLZy6Oqv2RT4ST2_VpHxqwJrAq8wNzovxRDekhtBwAIbVOChhq-Cwn5c2t21r_vNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور ۲۶ کشتی از تنگۀ هرمز با هماهنگی سپاه
🔹
نیروی دریایی سپاه: کنترل هوشمند تنگه‍ هرمز با اقتدار کامل درحال انجام است و طی شبانه‌روز گذشته ۲۶ کشتی تجاری و نفتکش پس از کسب مجوز با هماهنگی نیروی دریایی سپاه از کریدور ایمن تنگهٔ هرمز عبور کردند.
🔹
دریافت مجوز و هماهنگی برای تردد در تنگهٔ هرمز یک امر قطعی است و همان‌طور که قبلا اعلام شد عبور از سایر مسیرها به مثابه اخلال شناسایی و با آن برخورد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/438443" target="_blank">📅 14:28 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
