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
<img src="https://cdn4.telesco.pe/file/ouquaWHB3DBYjZAOPjNOk-eGU45xnRTuqpdNHtRoPeu-4L4BcLctl8Gbw7MQBj9cHX8Ua5aCa9JrqHQFUIPOsXZD7ncSouyUhi2HbtgDUt9HMH6ad_RSwVqnIj2kT-AOkMvkMo9oO_SKr9ZmaSKyw_elSW_AIYwzzJFeCTiPSPxSyf7Mt1cB_4kspi3kPf4ry75ejHCmJYnGuW5Q8Pv8DaU8eUf1Nwc_W3cGxsHh7NEEyJl-2qLooy_nDTXBDzL3jXODjaNEWXBWAvkgnpxuHieX_9CVbeSRqG-VOEMQ6NvYynPYA6zc0zNEmv0Xf86TU0SsYk5DSKvaqyIJ2XQnUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 12:57:05</div>
<hr>

<div class="tg-post" id="msg-455477">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXNH8oyDzdKbEE3OCyU1WBv5pbDtHnyzs1F6ey-cjo46LBaTy8TnKfek3gGWTxOunNHNOwGxUxlyKv0eFGgtbFJjgzS2OEl41a8KYl6yJQer2LHxLgggQNaW9kcoO8A0xfDa17n90drvUlBK3DEksr5d3ysVKZwijchNaK9wf4-Zq0RN0ZHyI_otgR96a7sEKseF6lTPQJbDfmiQKUVHkSZwZtwFaTHtI9CIxGxIoxiie9aN_2M5PSVBqjUEOktjB9J3IHB6UO-BX7g0oMyJq3LQepKrbEHtJhH1WMWw3jSVhXPOYjeUEX6swknbI4tc56JJSJTBFvVMmu16a3oiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی ملکی، قوی‌ترین مرد سابق ایران برای ۴ سال رئیس فدراسیون بدنسازی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/455477" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443634235b.mp4?token=mttvVIPOjG-6EfAzRb6bjoVJFqx4ZDIcOqWgM-DjlqzkDu_iKshzbvYLeU2ayP6SuAqDm4Mgl171sizII8sStP8_nrt934AfVF1mn5wEudC17JgXJXdP_UWm56k4_3ariP7_kaMozqzYpBFs__gt0obSRBBVe2J3uNkKdr3lBzSxusaf5RRlVrxpZVZDY3sSv0uJTvwK5FKC32mji96XAnHRPeRVAAPPO1NhCiSiiQSthLp1cA1clA0mjvIKGKnwrXahyuHmAfxEFOtgDBINwBS357JxJLPVKdbr23hqwvPWv8ocRpRbc95GDZctebqQdKMUuIi7AtGnF-Kv0GTk1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443634235b.mp4?token=mttvVIPOjG-6EfAzRb6bjoVJFqx4ZDIcOqWgM-DjlqzkDu_iKshzbvYLeU2ayP6SuAqDm4Mgl171sizII8sStP8_nrt934AfVF1mn5wEudC17JgXJXdP_UWm56k4_3ariP7_kaMozqzYpBFs__gt0obSRBBVe2J3uNkKdr3lBzSxusaf5RRlVrxpZVZDY3sSv0uJTvwK5FKC32mji96XAnHRPeRVAAPPO1NhCiSiiQSthLp1cA1clA0mjvIKGKnwrXahyuHmAfxEFOtgDBINwBS357JxJLPVKdbr23hqwvPWv8ocRpRbc95GDZctebqQdKMUuIi7AtGnF-Kv0GTk1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورابراهیمی: قرارگاه خاتم‌الانبیا باید در حوزۀ اقتصاد تشکیل شود
🔹
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص: رهبر شهید فرموده بودند «جنگ ما با وزارت خزانه‌داری آمریکا است» و امروز نیز محاصرۀ دریایی را می‌توان مصداق این جنگ اقتصادی دانست.
🔹
در شرایط فعلی، مقابله با فشارهای اقتصادی و تحریم‌ها نیازمند هماهنگی و تقسیم‌کار مشخص میان دستگاه‌های اقتصادی کشور است.
🔹
همان‌طور که در جنگ نظامی میان سپاه، ارتش و سایر نیروها تقسیم‌کار شده و قرارگاه مرکزی خاتم‌الانبیا تشکیل شده، در حوزۀ اقتصادی نیز باید چنین ساختاری برای هماهنگی و مقابله با جنگ اقتصادی ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/455476" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTwzPV74ljCspebEMNB2geo8zTp7jC9NZRb1enpTG2_cKRDXFyBKDJkchMhl4oEWDG_hCG_6lAl5-AiKbOirN4Ichrh-V_akfuxldMZeADmwpROI7KvIeg500x6xXdhJAz1Kuw5bQ4fLgQGJaL9Rjkimvu0wAq0MoRd0yL_n6rnEAXJX-ceOwb8elr8XFB-ps7tkrLlznor2OMp9K8ijpUuS4ebIngM1k7fWS3JVODHw7SHOMoeiPE0opOCPe8Z5OlBgOZR2IbX6foZibBq1weJGPyY2K1yD07ezaVpdL8w6ii_rCOswh8j-_Z6LQnxJTevxQURntXgm4LU3CaogWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرتیپ پاسدار احمد وحیدی</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/farsna/455475" target="_blank">📅 12:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqxT81UQ3rKEQPwl1qhBFwiUga7PANtIayHTw7YvD85zE6f-DZEt1LeptwoVXLhExwpsZ3YynMD4kX7jSbENH8IrSFPV53lwWTalyc5_DKNoSIaOAlQyXGvwQq65HNM5IqneRHH0_w2MA4x2v0Ac2guJOhp7aidoIq1cjoWcfKvOVX6-pUIGwPi9bkCzDoqv0fAKrE4iqwDx33WprA_-ezStKNtnjajeQHhOk6tdMKSvrdOF1JcNbe6F0SGNcF0yypvrg7XUj-bLMWRk6DuAWEt-sP8X_PDEMyaMG9gZbVwkSwBAk-KEO3_BVcVu5D-ag63UC7A0j7yP_ia0rd5wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلیت تهران-مشهد پرواز کرد!
🔹
همزمان با موج سفر زائران به مشهد، قیمت بلیت پرواز‌های تهران-مشهد از بازۀ ۱۰ میلیون در کلاس اکونومی شروع می‌شود و به بالای ۱۹ میلیون تومان در کلاس بیزینس ادامه دارد.
🔹
این افزایش در شرایطی رخ داده که سازمان هواپیمایی هنوز واکنش رسمی به آن نشان نداده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/farsna/455474" target="_blank">📅 12:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699cf9fe4e.mp4?token=qEFZwN1k-l1i6hHGAUpWaUzBhz-otALHY-Qh0wOYdaIwKv80aVdKVUebbTnY3bN0dak7-Ih0XyKn7g-LHknKfbUOFsUgvJeUtCw-JRB8UZ56nZ4mPUM-kwoCd-viqjOQbg46u6Huvb0xr3yPVDYwFC5qw7mP0IK22STtx7VTDzBj8Rtkex_F_lO4xYRkNimabeNGI00CHmgs7XQukDmPlSFkJADNIKmBPulo3mXgixeRekm1FVMq0D1VdLW654rf4KvhabpyVM6FDPpFXkl2cPB5CyRmHZvv1_Wmo_tLZUkRqJioWFTHOy4qNIEiQDdTaKT8nx5j_YLfAx1uSbbpqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699cf9fe4e.mp4?token=qEFZwN1k-l1i6hHGAUpWaUzBhz-otALHY-Qh0wOYdaIwKv80aVdKVUebbTnY3bN0dak7-Ih0XyKn7g-LHknKfbUOFsUgvJeUtCw-JRB8UZ56nZ4mPUM-kwoCd-viqjOQbg46u6Huvb0xr3yPVDYwFC5qw7mP0IK22STtx7VTDzBj8Rtkex_F_lO4xYRkNimabeNGI00CHmgs7XQukDmPlSFkJADNIKmBPulo3mXgixeRekm1FVMq0D1VdLW654rf4KvhabpyVM6FDPpFXkl2cPB5CyRmHZvv1_Wmo_tLZUkRqJioWFTHOy4qNIEiQDdTaKT8nx5j_YLfAx1uSbbpqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی امام رضا(ع) ضامن شد
🔹
مراسم آزادی ۴۳۷ زندانی جرایم مالی در حرم مطهر رضوی برگزار شد. این طرح با دستور تولیت آستان و با مشارکت خیرین به ثمر نشست تا ۴۳۷ زندانی به آغوش خانواده‌هایشان بازگردند.
@Farsna</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/farsna/455473" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455472">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7107Rn_5Boq4Qo5kd05AGnyz5orP1ay8BeNDibYkjcJjNL7_QSr5_3jqYzVzcsdzLIq1h7xd1IXIEDkOq8-WaemjEiIUs03Y9athFEQpzVm2TKcvs8lrl7Hmw-9Zz1QIkM9FVraVWey-47P8YrpEh56gRTOpE0WLoQ9Gkj-0rahjim8F8D435r-NjjhLyJUbslmeeekh69XmddDksO9ZY2yIvrX8DON2FCfFLS-ol1CKkzmwUP4QKlkt6OTJwo9UDBvhyF7ahHP_aoi2r6ccUGnW8HXn0HPvOoUWnwY3Hvv4x1VY7JYo7znJr6HH6_4-2LsDrCh5vUQQwttTEzvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگردان پیاتزا حریفان خود را شناختند
🏐
مسابقات والیبال قهرمانی آسیا ۲۰۲۶ (انتخابی المپیک) قرعه‌کشی شد و تیم ملی ایران با چین، هند و نیوزیلند هم‌گروه شد.
🏐
تیم ایران ۲۹ مرداد با ۱۴ بازیکن راهی اردوی تدارکاتی روسیه خواهد شد تا پس از برگزاری اردوی ۱۰ روزه، برای حضور در رقابت‌های قهرمانی مردان آسیا عازم ژاپن شود.
@Sportfars</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/farsna/455472" target="_blank">📅 12:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455471">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCRUYqh8jiPByc-1SCFjxjM8laiFE_Yuwny6B88Ilf-rTqe8n6LbXWlQ7m8M4JRQFZXFAq-drIq8-PvB8TG48DUDhw96oFPHcqJYAP2V0lIfCPRyg5J_LUA55vnVOJok3yaa2-Hu5bcJ3kThezxOegcwkTOcuEv8QoagQdAJpHMAL573RzU363blL8FBdz07WYuxsrlRMUKR_Lrkr6xdqRL8ITdd6zuxD1jmjbMEUgw27sHOHn-_bQXkSDdutydr9Fbb-E7urxG6PWE-qBy2fINXme29nTx_tLdiIZTRCVPv-sgF3ug5HU6QMo7tNtVRvePJ7v8qNUPGBzeu7B9d1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: تحویل بشار اسد ممکن نیست
🔹
سفیر روسیه در بغداد: تحویل اسد به هیچ نهاد خارجی در دستورکار نیست. او نیز تاکنون هیچ‌یک از شروط پناهندگی اعطاشده را نقض نکرده است.
🔹
یکی از شروط این است که به اسد اجازۀ هیچ‌گونه فعالیت رسانه‌ای یا سیاسی در مسکو داده نمی‌شود.…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/455471" target="_blank">📅 12:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzIPI3MB6P9HzfRmHytKP52FF6pIuHMVvOnz7G4gsyaCrPwJ9Ru_yDTDuz-6XWDF5RWkeSf4tqpyNz0cLyO2HUEzzTz4bReBBXsd2XPKPUs7S1B2WVYpf4jv1J5CeT3L_wTMirEl5DduCiZeflr7zjV31-e6uRcoeZlwIBfEwDEXKvJDt2wBsOVgE4QLxOk6Bxrm85JvwwR2AK6yOgPxQbWwnNDnpcGxP2B-oakTknAQD-yYwAR8kOj1tGjHr-aRIi46tWG_ht4UwRJKxG3-nt3fSUo-jrqyBO2NtaNqx6deidogJqd_fUlTep4A6XEwoxRxAraQh9HzkdBV6RXcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدید هفته را تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۲ هزار واحدی به ۵ میلیون و ۷۳۷ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/farsna/455470" target="_blank">📅 12:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgpGjdDLbo6nI9FbjHJ_LiC_vkfUqivmav93BTzKwCRWvqQXGx43dHNSr8n2ZaLGKF2KH-Eqq0thFdFztphlJrapcqmUtxaadymqk0wHtk3eZkiVkhLfkR68d1htubqS1Pxv3DlemShJtJe0WaRdfD40YibxKqR200vSryLbUkjJHuoWp8uBFkiIkCggBa9JEQTvIyT4KzzGoFDKNa7olZuwOmhl0maIr1UOgc5yI1nA-3hte0A0L0ErgF_dK6JBixNoaCadsRXn5Kd0SP1nDYfEh4cojM1Pe4cJQZzoLNWI38l1Z5dwkBMADsyJTgFj8GMkY6HXkoWqnUQ_egbmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری خراسان‌رضوی: ورود ۶ میلیون زائر به مشهد در ایام دههٔ آخر ماه صفر پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/455469" target="_blank">📅 12:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرمانداری سیریک: انفجار کنترل‌شدهٔ مهمات امروز در بندرکوهستک انجام خواهد شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/455468" target="_blank">📅 12:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73ce01548.mp4?token=rzDw9_zLD1RO8LyoRmRVTE1rkPvllUgG_-zcgcrQCJ2rTCmJZra2gN9vS3qHRd1HN_0xVnqSWirCaQwCIxS9gSMTvQwBqmr50XMvPePIadnhv-fiOv7wOHyPLxXgCgGZD-zbFkqvS9g-YjZDHP7xTzHLKS6I9BClgIz1S81n51IaR9Z9gHXx4rWXsqxQWBROsxO0dIjhjLC7pGkmu8pv2aWz3zSP8McJEgfTPN_qkCnapAmAPUna4naeBSyAmIydTvgZxxWUWdEsuLFB__26sMt521CXi22YB7Um3jiHb87J4-TGJm2UwqxKqykyHDotpUvo_dekSaObB3StwVvTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73ce01548.mp4?token=rzDw9_zLD1RO8LyoRmRVTE1rkPvllUgG_-zcgcrQCJ2rTCmJZra2gN9vS3qHRd1HN_0xVnqSWirCaQwCIxS9gSMTvQwBqmr50XMvPePIadnhv-fiOv7wOHyPLxXgCgGZD-zbFkqvS9g-YjZDHP7xTzHLKS6I9BClgIz1S81n51IaR9Z9gHXx4rWXsqxQWBROsxO0dIjhjLC7pGkmu8pv2aWz3zSP8McJEgfTPN_qkCnapAmAPUna4naeBSyAmIydTvgZxxWUWdEsuLFB__26sMt521CXi22YB7Um3jiHb87J4-TGJm2UwqxKqykyHDotpUvo_dekSaObB3StwVvTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تا جایی که ممکن است اموال، مدارک و وسایل مردم را کمتر نگهداری کنید.
@Farsna</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/455467" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4dZJrfzzcvODopQ-FiC8g_RHsUFfYBwlF6g87DKsRHYwY56pfaiO_nhNeWBVUrhGGgu04JjjHxGDneK8Y8j3QOIRVKqYyPPec_8H3cmKEb6cYkFZqU0wXd5d9m3vj6B1ElMlSwQRBU98Vf2-0KKHnDXKKFuV5LPGSGNMepdcb99OdOdM9CI_i9MMa1dR6hStIEJfE5UaQr8uvhrR1f61nOPqFSokCuW0XFFc2VxBT3Imu-uPfu6FIJ2LzbopTCJPtvzx3jMp8jmCoU2PCJZ33s_0PWdTD9DbLJjwLLor0a5tlirGpkJZ6yJAQRBSRB3ttzyUval00MTQuaxL3lqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس اوراسیا: پیامدهای کنوانسیون دریای کاسپین از واگذاری بحرین هم زیان‌بارتر است
🔹
برهان حشمتی: در کنوانسیون رژیم حقوقی دریای کاسپین، فرمول ۱۵ مایل آب‌های سرزمینی و ۱۰ مایل منطقۀ انحصاری ماهیگیری پیش‌بینی شده؛ یعنی در مجموع ۲۵ مایل. این محدوده به‌هیچ‌عنوان…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/455466" target="_blank">📅 12:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frZsWl3u7UIqWF06IwpjqjxLEMWFRuFGJQ8QeEY7pqp3fVVUL_GEqluqV1LP4VJvSVgrLLarM0cuPljfVumhBnb8vhdUtMdW8xNJhWXW0rFZ8zTQoDn6dB2Nz4iagrvz25vmh0GDep7lIpZ_OjWaY9oh2Q4NazIS3YRv5GlS0V610wfmxB4fGOLIiqBHqNtZrk5hcXqd_EI_3Mu2BizAoQ_OQbvXkv7eCgnCxMSnar7U0Ie8WzHfnG3AYlTM2Vdzeylj73n4OgQhmSeVdF4nNALnIMv8uLyIxJl_IU5-EGxzbleFxSzL4QGh2yimHXL3YXlVVNnIMgwu-M615--g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ قالیباف به پزشکیان دربارۀ ارائه لایحۀ اصلاح قانون بودجۀ به مجلس
🔹
تاجگردون، رئیس کمیسیون برنامه و بودجه:  رئیس‌مجلس در این نامه از رئیس‌جمهور درخواست کرده‌اند که لایحۀ اصلاح قانون را با قید فوریت تقدیم مجلس کند تا هم دولت خلاف قانون عمل نکند و هم مجلس بتواند با توجه به شرایط جنگی و اتفاقاتی که در جنگ حاصل شد، قوانین را متناسب با این شرایط اصلاح کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/455465" target="_blank">📅 12:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDoX-d1ADCE_XU1FJY9tG8czq63ccFtnM9fF7D0ANbDBpjbNTZnuAZyfU8ZW4b2Wdgu2Hd0omG7vG81sxs_lyydZPTcyBrwRjXWkjMmK7cdU_zh4JD8jhGBODqubLs2tOSK-cImP3xZHnOe8xE3v3u6T7W7LNuLCmwVUErsjcVH0sIU76F5pMWCBs5QFtPmmW145czDMMpap4e6-z1TSPTuV7Mv4IH-F0cca5gdD1J0iRRDLFRSZGb9U5yVQHZyMf9F4ISxhThcBZSca14C_OrFJQExUjoRohGxgIed7VYn7XQlW2I78-e-PCPLkDIk8kB3Ok1qwASIsSMr75opqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ماهواره‌ای از وضعیت دریاچه ارومیه
🔹
جدیدترین تصویر ماهواره‌ای از وضعیت دریاچه ارومیه توسط ماهواره کوپرنیک و مقایسه آن با مدت زمان مشابه سال گذشته، خبر از بازگشت امیدها برای احیای این نگین آبی دارد.
🔸
میزان بارندگی سال آبی جاری در حوضۀ آبریز دریاچه…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/455464" target="_blank">📅 11:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51a74e04ca.mp4?token=K0de8FkFg1ytkYuvw7Kc5GINrtAEODjh8USiXT-9xgN_Xkjk1RsxVv-X6hBi26MzYhzC7cbvn5_7wK0iV4tIxX3Lp_gcw1NCZ6wqK3v9NgREBYuBak4DZO_noMO49bemMPTEgNiHNFHwYT-9PuoQUZ4jq-u02sEMwuWBIm9Tkqd9hbN7y3jNjtYYKHPeBbyORzqRGyW1706LKjWMZuwP2PuROf5ySp5YINtsR8VZcn3weNvpVPFg78NpXPuT5HaCGgYCGR4L2vrIDlAczWKlNlVo29Rtxfzxnhgh9Fl7F9Rxi9kI1bupebSx3oI7lP7OuQTlM6PmzkBhWx1z0uKW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51a74e04ca.mp4?token=K0de8FkFg1ytkYuvw7Kc5GINrtAEODjh8USiXT-9xgN_Xkjk1RsxVv-X6hBi26MzYhzC7cbvn5_7wK0iV4tIxX3Lp_gcw1NCZ6wqK3v9NgREBYuBak4DZO_noMO49bemMPTEgNiHNFHwYT-9PuoQUZ4jq-u02sEMwuWBIm9Tkqd9hbN7y3jNjtYYKHPeBbyORzqRGyW1706LKjWMZuwP2PuROf5ySp5YINtsR8VZcn3weNvpVPFg78NpXPuT5HaCGgYCGR4L2vrIDlAczWKlNlVo29Rtxfzxnhgh9Fl7F9Rxi9kI1bupebSx3oI7lP7OuQTlM6PmzkBhWx1z0uKW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«دان خوابالو»؛ هشتگی برای ترامپ
🔹
روز گذشته دونالد ترامپ، رئیس جمهور ۷۹ ساله آمریکا، میزبان یک رویداد رسمی در دفتر بیضی شکل کاخ سفید با موضوع سلامت مادران بود. در طول این مراسم که با حضور مقاماتی چون رابرت اف کندی جونیور (وزیر بهداشت) برگزار میشد، ویدیوها…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/455463" target="_blank">📅 11:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692ecf877c.mp4?token=ocMaEZGjAaDLG8cDuUaIrJ5miDD2cXPnY62i4h0urNQa9M3ICihclV44goUIgyZSk_5pGhGhfuNRZG7cFinDazXMm2vo9YijYaD_OnCx3asoY7BIkI-dRNP6MtfIVYDe1dUy1jZdzPfapWTNFqzW1wJOLGevoMoff56SLnpzMUmJAJX4xRrxnO6AgAMjdss4gQJdjCDYYptiI3pKby_LxG4KpiFm3BV61pBCcwMiMSMwHSlMDI2W0DGOFDYt3jG8ovvuzggiyEQyEPw3CWoUOEsJdeNRu4323UWgmkNbsar-O9wo8N0hOrTJ4mBmqd1NeL6ebXrRjI9fllceXOmyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692ecf877c.mp4?token=ocMaEZGjAaDLG8cDuUaIrJ5miDD2cXPnY62i4h0urNQa9M3ICihclV44goUIgyZSk_5pGhGhfuNRZG7cFinDazXMm2vo9YijYaD_OnCx3asoY7BIkI-dRNP6MtfIVYDe1dUy1jZdzPfapWTNFqzW1wJOLGevoMoff56SLnpzMUmJAJX4xRrxnO6AgAMjdss4gQJdjCDYYptiI3pKby_LxG4KpiFm3BV61pBCcwMiMSMwHSlMDI2W0DGOFDYt3jG8ovvuzggiyEQyEPw3CWoUOEsJdeNRu4323UWgmkNbsar-O9wo8N0hOrTJ4mBmqd1NeL6ebXrRjI9fllceXOmyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/455462" target="_blank">📅 11:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9001b587af.mp4?token=mOyKRoWx6mnhi_MDJEqiwlIkoxadOrSnWnNs1Y8afcvCZR2WoVGkjQsvZ_K7NP-dTdEbpxn-gTDCx9GzyKxnJpcTmGHFF4K2uVrbFIRDWBJXdnlhozUqXO2eLmkAM4amFTXmtFSr4t5MR8pgFJiKEn0uLofSuKZkV6Dhp5aFeiP6PitNhCBCxoEh5n81sCjfs78i9J-mrOnEOSgDqTX0THREH65IKWXD_Cea-BepHW_vKl-siA8Or9seAu_BkeI_A8dGNvIR0UXYYWFVs96Ajz6wzGsQ7PG6wMxtypsg7xwyoSYWRtYDIusbiiUBZBsmq0x6xeuaUe495u2A2WLp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9001b587af.mp4?token=mOyKRoWx6mnhi_MDJEqiwlIkoxadOrSnWnNs1Y8afcvCZR2WoVGkjQsvZ_K7NP-dTdEbpxn-gTDCx9GzyKxnJpcTmGHFF4K2uVrbFIRDWBJXdnlhozUqXO2eLmkAM4amFTXmtFSr4t5MR8pgFJiKEn0uLofSuKZkV6Dhp5aFeiP6PitNhCBCxoEh5n81sCjfs78i9J-mrOnEOSgDqTX0THREH65IKWXD_Cea-BepHW_vKl-siA8Or9seAu_BkeI_A8dGNvIR0UXYYWFVs96Ajz6wzGsQ7PG6wMxtypsg7xwyoSYWRtYDIusbiiUBZBsmq0x6xeuaUe495u2A2WLp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: جنگ‌های ۱۲ روزه و ۴۰ روزه صحنه‌های بی‌نظیری از جان‌فشانی مردم داشت
🔹
نیروهای مسلح ما هم توانستند بزرگترین ارتش ظاهری دنیا را شکست بدهند و عاجز کنند. جمهوری اسلامی ایران نشان داد که یک قدرت سرسخت و شکست‌ناپذیر است.
🔹
مقامات خارجی بارها به من گفتند…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/455461" target="_blank">📅 11:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4478836b.mp4?token=hsJf5CpM3bjsVh8IBU_G8smAK5ldT_zoTXQumWzYF48R3y4I3Lay-hc79E-HV98SZ8Q62U3n3KkJ1TGUCVOTS6UJV791QbUQThOXPMhv-1hvJOIl45Qnulj4Yk2yXIdiPGVk-30xxpeGE-Njrfno9oYv0XxE6Tftr4E0ne2AG1ctwiapx9EcV1FjQ2rPmzUYjnah6cIw5HX1EwX6Are-y1O1g3RQfgSBHaGzvFA_hT3rMimpFRKmK4b8OIWBL-_6OblW8nT-szzrBnfpqiGT75DegziRCnSzEAZ6VSAkcS_ZIU7TGlziUQHxcF0Rt-1-K2EFXH-ZO6nwEe0uKweGBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4478836b.mp4?token=hsJf5CpM3bjsVh8IBU_G8smAK5ldT_zoTXQumWzYF48R3y4I3Lay-hc79E-HV98SZ8Q62U3n3KkJ1TGUCVOTS6UJV791QbUQThOXPMhv-1hvJOIl45Qnulj4Yk2yXIdiPGVk-30xxpeGE-Njrfno9oYv0XxE6Tftr4E0ne2AG1ctwiapx9EcV1FjQ2rPmzUYjnah6cIw5HX1EwX6Are-y1O1g3RQfgSBHaGzvFA_hT3rMimpFRKmK4b8OIWBL-_6OblW8nT-szzrBnfpqiGT75DegziRCnSzEAZ6VSAkcS_ZIU7TGlziUQHxcF0Rt-1-K2EFXH-ZO6nwEe0uKweGBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامهٔ همکاری بین وزارت بهداشت و وزارت خارجه برای بازسازی زیرساخت‌های آسیب‌دیده در جنگ، امروز به‌امضا رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/455460" target="_blank">📅 11:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef60d75d8f.mp4?token=Wa7aZ9ATjNDc1bIe5NnHOjhbFCo_peF3I-fr-vSogohnrbMoagV9N1aG0bjFqg6nj58R2s_wq3b6N_UIAMBuSHSxhl0REU9TXcPj3MDpSVlGpp1z3bAFqjez1wImFs3qnxwkoMfIYf8KZDrqR4llfjv2yw7wcjKo76v0B9FNcfs5n0aZCEEi1QAol9JqZ1AkuABGBAOAuzITcENvZMnc8kctqD0gvmh8qI_9ANgQRcZpK-nAnqikpSv4bhpMEtW3N0F_pHWgqYry0w2CxSyVbVVASpbg1hiDfm8GjQcTy4d2wnWTJyKpojieRookD1ods5lDdj40QupFVZk_NbDsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef60d75d8f.mp4?token=Wa7aZ9ATjNDc1bIe5NnHOjhbFCo_peF3I-fr-vSogohnrbMoagV9N1aG0bjFqg6nj58R2s_wq3b6N_UIAMBuSHSxhl0REU9TXcPj3MDpSVlGpp1z3bAFqjez1wImFs3qnxwkoMfIYf8KZDrqR4llfjv2yw7wcjKo76v0B9FNcfs5n0aZCEEi1QAol9JqZ1AkuABGBAOAuzITcENvZMnc8kctqD0gvmh8qI_9ANgQRcZpK-nAnqikpSv4bhpMEtW3N0F_pHWgqYry0w2CxSyVbVVASpbg1hiDfm8GjQcTy4d2wnWTJyKpojieRookD1ods5lDdj40QupFVZk_NbDsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: سال تحصیلی آینده حتماً حضوری است  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/455459" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6rlKGJ7zXgtCD0iI4AI__9KQcfTOWsNLJ5HEBJaxUAVL_fI-77H4mhidC0Oc4c0UpRZQyqDUIm4vhrRxC7RkyVEbgp0klJbRYSW3DScTqqq1yDVeH0EEF9B2fPxwxCR-f8hYuA0E7iaa0orQLnTmbN1vCrR4o6yhxLVslSJsms6wOW7eIbXz-YvaUQ4MWjaTUC6JCwdIpI08-kXSw0lO6vIx4fZwm3UJyOqoxbGYFMpQCfjzHQEFuyJzgqCfFOHA4yKoGHsR2pEQa-7QthJIFVvAH6_nhfv_ED6U-Kc_Jw034sMMyvl9AAmtsD-JeGTx8HIujeNEsU4VIezcFFtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامهٔ همکاری بین وزارت بهداشت و وزارت خارجه برای بازسازی زیرساخت‌های آسیب‌دیده در جنگ، امروز به‌امضا رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/455458" target="_blank">📅 10:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/455457" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m58nxusrlc5UGmUs9oOyHWmr5gVXASbkB-senwrNOwwgrC6Ly_tDnfa0tds_1WgC7pXidVD1jAosCuOzTQ1alk5tkIf2fntNgJHhuzHNS7YYwZT1DmhBs1Iucw6Gjj1yRtw0iDYl9cizPh06knFqMPeBaMIY5FuUKNthxSBr3HJHwQ5csQclfxyChSf5-dyuapC5ffnSo_wmBd_mjep5TaoL1Iwy9Lj07vKCfOD8zlmlREY3ANdogHZcXNMFe2kGJH9yLSmDzdBmSPV75cft7s7eP9lr4Yh87gQk3vshEc_Z2cyq4BlGEFvHbjFQfhivevmX2ajBNVFiN-WsMts8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیال‌بافی ترامپ: تنگۀ هرمز باز و در کنترل آمریکا است
🔹
رئیس جمهور آمریکا شامگاه دوشنبه با ادعای اینکه تنگۀ هرمز را به‌صورت کامل از مین‌های آبی پاکسازی کرده‌اند، گفت که ایران اما هنوز می‌تواند مشکل ایجاد کند.
🔹
ترامپ در پاسخ به سوالات خبرنگاران در دفتر کار…</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/455456" target="_blank">📅 10:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منابع غیررسمی از حمله به یک کشتی عربستان در باب‌‌المندب خبر دادند
🔹
شبکه «الجمهوریه» یمن و برخی منابع عربی از هدف‌قرارگرفتن یک کشتی عربستان در نزدیکی باب‌المندب خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/455455" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مسیر شمال به جنوب کندوان مسدود شد
🔹
پلیس‌راه مازندران: از ساعت ۹ مسیر شمال به جنوب کندوان مسدود شده و از ساعت ۱۱ از پل زنگوله به‌سمت شمال یک‌طرفه‌ خواهد شد.
🔹
همچنین در روز جمعه از ساعت ۱۰ در آزادراه تهران-شمال محدودیت تردد به‌سمت چالوس، ساعت ۱۱ از ابتدای پل زنگوله به‌سمت چالوس و از ساعت ۱۲ از مرزن‌آباد به‌سمت تهران مسیر شمال به جنوب یک‌طرفه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/455454" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302f3b2287.mp4?token=LKCU54HFJETVmO8eEi89qgm54165XodJHCvq8lYE9OU-I_huDBbGN7VpnSp0CzPrWRC_mRix_WcZJ0VUvQtZUJln0hZ_wuMcSZtt89kE6oWa85zY6uSjRmfXxn8add4mbjO0aeILEhmSckY0L1jHBYGwhVtK-JKznw6iaWxu0C0UqXN7jGSJL20lUzPSJbgHU-adUBVa0PmT09Xl2HYVD-YUGuHni8-ZlaT55paYBz0W6ICBF3CFTUhVb7UEaDq6ZMNUc-O80EgJhA9dUpG3pirSCl5yVx54kkdI6d0HMavZtpR1B5eub9JTBHx7c8huEAjcj9xDvtxH5gZOos3k4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302f3b2287.mp4?token=LKCU54HFJETVmO8eEi89qgm54165XodJHCvq8lYE9OU-I_huDBbGN7VpnSp0CzPrWRC_mRix_WcZJ0VUvQtZUJln0hZ_wuMcSZtt89kE6oWa85zY6uSjRmfXxn8add4mbjO0aeILEhmSckY0L1jHBYGwhVtK-JKznw6iaWxu0C0UqXN7jGSJL20lUzPSJbgHU-adUBVa0PmT09Xl2HYVD-YUGuHni8-ZlaT55paYBz0W6ICBF3CFTUhVb7UEaDq6ZMNUc-O80EgJhA9dUpG3pirSCl5yVx54kkdI6d0HMavZtpR1B5eub9JTBHx7c8huEAjcj9xDvtxH5gZOos3k4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروگان‌گیری در خیابان ولیعصر تهران با حضور پلیس ناکام ماند
🔹
پلیس تهران: صبح امروز در پی اعلام یک مورد گروگان‌گیری در خیابان ولیعصر، بالاتر از پارک ساعی، با حضور مأموران به آزادی گروگان منجر شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/455453" target="_blank">📅 10:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbb-ys07oHLfkFj4CvzUkgr6rpkZ33f8tm888SYIyg5YbngLgGUZlidRQQ5JurW469U8YHQE4OqlHOny-2MQAlYu3jWDE8feiBM3AWNudpKun2AinuKUd0wHgzk0vjCSdS0br46kSG0kdLRvR0EpYFRKsxHFIN7WY30sQFsfN8kmi2iZ9wR6WUYqh3njsB_nBC3q9hnP7QTnbPut3kMdqA38UCzP7dgX2Tnp0FcOXgJm6LGyOVeoj6miesLBPjrUsR7dx4Ewaof1Y9oCIFZg6tWZFBhOh-pknLTaMgxMD2SdpCGPJvlciga9Gqf2otyq2fHITn2kkE7WsRF5zpe7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروگان‌گیری در خیابان ولیعصر تهران با حضور پلیس ناکام ماند
🔹
پلیس تهران: صبح امروز در پی اعلام یک مورد گروگان‌گیری در خیابان ولیعصر، بالاتر از پارک ساعی، با حضور مأموران به آزادی گروگان منجر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/455452" target="_blank">📅 09:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqzgc-OSzCpjc6wxUa5NRq4VolwnMHYLGg_enKoiv6o9rRbxWpYT1WhHNPeg0RUFBjFOWrE54DQ2vzoBksTbYQB16nx7Ygzt3qOkuch3sQtW1nJPY28nww8il14I9R2UckgQsjX7D0N--isfNcK9zWBgPhrexyojnTolMeRx6OvzfB3j1kAarQ9dKKYX0VWa1llYr8IwMwr9mnDe1hECbdzrBYSzGZGXdD5pbinNJsgP107j1DnEwViRxILif_STrzPYKs4w0Ekua5sElFth3cCSTjdYt_w_8gGFKxzIfG_PUHd7EF2UKw1FYvgSvhHRRumjBjC52-A2x9uQYpU8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lhn2JdaDZI1mvBc2Y1vjpNBP0pYV2Tp-di8wqbtdIXrNHaQsLzM8wjK3sJoAgVC9ZJkMsbuuktfzg8xapTzIY5A3xgJMKVDSmZ8m8Bv7oHAy_83gZl2Oopm5ZbLFTLE0i-5nO0CUop7wWfytKTYWP8GYK39eKLatKAJTGH4A-2evM5xpbp2i-MEzgrUMCtYZq_wKP4WgVhw2FnrPAJelW1ry4WhV0SGv5kEnjh7ird7mes4NcW7ESnUGvSD66c5rxqH_o42YRC_z6XbVE1I9DCSH73hm6HZaHVT9PBCImaLDGh2foLmcg6Ru8oklDLkTvdXDt0kXFShgHCgnWruZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7fnSBgmOLG0yJAA29-UNO6XU5XZHm9sa3kWiGKgRhO8rkiGa2e-nouRwWGihqFLFv_zLEN6QnjJKLlNv5Mm-u9KxQvzpW3PlQNoPmED5yzs7fxuJlv8owk7T77F10XR1w_ZCPJL4tnBiN5Ps33Dw2beCg98tZYBfcjA2IRKo-I_eowhQO-orMliKnNa5RNQWRLYCHi58-Jfitfqf_NxIhouu6dqPNgaTPdn-Q5hLiFq87ZqEYl_1pgilVrWEtYFTqGY8tSD5-QiNuMtrC5FDNjQ8fDZXg79KNgObf0Asn7lPPI0WaRFsa8eWcfhvAZ0caLNse1aFqIzREOerOyqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFtpwvhpOpa-T4fxTDIw3TUkQrQRdw560aL4g6Wf2HoWUymXTk5TQ0TO0o8iBAYN6udIFrKbMah9q2NilHochni1JerKzV9Vj0VHs9ATSbljGHK3vwkpuG_fWveUreCWt8LKDv-JBKFuFc9hrlmN-Py3p1u8NWx8jGhYzDEpbjI1tcqKH3n5qrWDnK9IZBOW9YrArwi8ahn3iFmfQWSqztWlG35fkopWzP3KtNVb0Tts3IppdJo7sO9JzIEj9XQG6bmycaMOIqe1iXA2t6uQxCJS172wNnmQHlKTR5GKa4i7HCor5o42r-Wh157a2a6e-HpGZHSAAIx39LNpgvPTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCqxiJV-vGbbtRNSvzEf5lBJF2PW7nyXZyFQJ3mpebdh8icpEZH7wNuMls5TauIfkoCqsPWGvr3iBvXqEtdcNYUhQ6OMCZWMaIQLuaZC6efDeOecB6hlUa5lDwbg5w8yxCMPmvrA9RkT3zDsCK8ijfDq6UNmPpmcHwu6GJuABeYm1WiPyFfyNsTULOG7Vj0W4l2VMh9uMYiOoDF2MLlh-hg5F2pdpUDLdU5-vatGkdWdX7ehTTca9JZrNIEMLC0UjG-6uebGeBR_GM7OWAGuSy1ZVDFnkl_Rj7zLK_OTulHocYjsFvfacPwpq3oWIbVuBF22iPQzVQ84fb5RBt4Naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICHRlqD6r1RBZ1RyJ2ShApOWmZQT-x9an_6T7GlsItOMZ-YUo3TUeMVAyIkdQCHhiHn03FAQkdfrWRNQIar-s5Z8vw_eIllAmkdPNdzPPLImz5R1UdkzRI8CISH2-eylEWwvEADEcIcNHRRkwfMR-y_KAN1q8xrvsZ0e3tQ6l-NBvuG-mCVL1hyG4aoRczkrR8Cc738gl_5YqDCdDhLuU_byi0YOKf622RGzAE6PiQKzcmnwX0WmRbOmx6vqyA6F7IiSfxN923YW_YTTcE5BZGJnc_Txsh7QmbtORLjp-xtF8WaJlzPpG4Gh5DDr-UT0gkV3YRJy4pjOkpVy3618LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VniQZwWctvqXbmuFsSviApbYnVxZpH6aa96_3aRkMhM-rXpFzHuuMcPoFPWEEJTSD1qMkSGmYNYPORxyay8iPA8VBJhhj8YYiQXK-uZQKF0mNmOQ1Tk82Kcc1nz5S41ZXNAaya9oI3wxGWncEEiZ1QAENGwAmItCpO18U5Bv62ZKNxXk1lsE2fi5FX6YF9Lqw3NCVC74V0Zg0ZRFAh_ugLhASU9ylWJ1EqUdOFb4gjs9RrmxWSf1CD-91NiFOrWmFcF6TuT7GjLSfO9g3pFbzVQbHNwLMnFD81A6_TDaEqCGmU5iLM57wJWDaMyzmNlWfNUYqaabqWjEjvTQQaPfFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جاده‌های مشهدالرضا، میزبان هزاران زائر پیاده
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/455445" target="_blank">📅 09:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb0nCqRuybtCs2kiGB1rMgHY0iUc8-_q111BKEMMW5fVRr36ktdyRyPd4hst-tTUVJyoMhRIvQ8XotXEnXBV8YAdNt4ZIMHlYwpkUCWZqr8_--dubRwYIrVBkliucLKqMpKMoFk2ZZH3Qno-HSkcfyUgpqo_rQ5qWp1fE5580sW58QmizJ9RFMzTHixrEsDPv7BUvWFh9G3VSJKP76KHj86M8U9Y71naBRxYqH86ajEtodfEGupKNU8PNCWq6ZAV0RNJ0bPDaaSTpdOYZeugHxr-K0MlkB7h3kULNx3IaAKTjK2cU3SzXW93qJW0YDjIkpBL2cvvsP-YVWQRu-bSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سرنوشت‌ساز برای طرح بنزینی سقاب
🔹
طرح سازمان بهینه‌سازی برای اصلاح نظام قیمتی انرژی شامل بنزین، گازوئیل و سایر حامل‌های انرژی ساعت ۹ صبح امروز در کمیسیون اقتصادی دولت مطرح می‌شود.
🔸
پیش‌تر رئیس سازمان بهینه‌سازی گفته بود که دولت قصد گران کردن بنزین را ندارد.
🔹
طبق این طرح سهمیه مشخصی از انرژی به هر فرد اختصاص یافته و هر نفر باید مازاد نیاز خود را در بازار و به قیمت کشف شده آزاد خریداری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455444" target="_blank">📅 08:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1760a6e3cc.mp4?token=e5YOuSSI9cJegvZG762IfJaUgzliQV4JfE194DSHipYb99nZK_cg8jHdTjD_i3zsVY8CmlhrXK6HS8mHPazFwdAJ5PCmrqMZyW0RjPsh62RYPQA1yMGVSm0_wV5oUHQOfpdL1IkfR5TH-5X05owSHJzzHN3VGmMPN2iFA_Bia7NN5LpbficJycFSnuNDRCN3vF3h3sHYaDikJMBtCUgMbcNh8UulV50r97B3sXSRVQFZ8RblpWXuX6R6fFIXzghDIcdPy93yCG8OE8HyrVDpTv81A3IGzJ1K-1_13JAQ3CVtsDZsPiopVhAOP3QrfQvjc3pJM4bVof7_K6rXItaAeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1760a6e3cc.mp4?token=e5YOuSSI9cJegvZG762IfJaUgzliQV4JfE194DSHipYb99nZK_cg8jHdTjD_i3zsVY8CmlhrXK6HS8mHPazFwdAJ5PCmrqMZyW0RjPsh62RYPQA1yMGVSm0_wV5oUHQOfpdL1IkfR5TH-5X05owSHJzzHN3VGmMPN2iFA_Bia7NN5LpbficJycFSnuNDRCN3vF3h3sHYaDikJMBtCUgMbcNh8UulV50r97B3sXSRVQFZ8RblpWXuX6R6fFIXzghDIcdPy93yCG8OE8HyrVDpTv81A3IGzJ1K-1_13JAQ3CVtsDZsPiopVhAOP3QrfQvjc3pJM4bVof7_K6rXItaAeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج‌گیری اسلام‌هراسی در انگلیس
🔹
بنیاد مسلمانان بریتانیا: هر ۵ روز یک مسجد در بریتانیا هدف حملات فیزیکی، تخریبی و آتش‌زدن قرار می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/455443" target="_blank">📅 08:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616dbe674e.mp4?token=JewBQCcY8eJkjWCk5naEH8iIak8wzxiwOO5H7czuoWrtfvWN4s9n1mI72dUt5nyPiO45H_tOeWc6J4S310jac-UBm2sh0n7M23OOH4Qa80G5OLRuUgRSMml7EovI7aZTiEBDd_WL2Dokj3LAOuvFztG1t9abU1ryXvHiqY1_l_e8ZWFp6VGaSoAyfOCmOk33SXcKKVhBSerdULPpxs6cLDBB4hZSRT68vJi61v2h0S3Gv2GYv8zp8KyH7Y1pZ4pnEYjqglU8Zq9VPoiKglswECP43aNhRZ4rsn2FBLg2UdhEYPwhhPpLlOwq2qEhE7ZpIEdUijMNNp6CqQufwOVuSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616dbe674e.mp4?token=JewBQCcY8eJkjWCk5naEH8iIak8wzxiwOO5H7czuoWrtfvWN4s9n1mI72dUt5nyPiO45H_tOeWc6J4S310jac-UBm2sh0n7M23OOH4Qa80G5OLRuUgRSMml7EovI7aZTiEBDd_WL2Dokj3LAOuvFztG1t9abU1ryXvHiqY1_l_e8ZWFp6VGaSoAyfOCmOk33SXcKKVhBSerdULPpxs6cLDBB4hZSRT68vJi61v2h0S3Gv2GYv8zp8KyH7Y1pZ4pnEYjqglU8Zq9VPoiKglswECP43aNhRZ4rsn2FBLg2UdhEYPwhhPpLlOwq2qEhE7ZpIEdUijMNNp6CqQufwOVuSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان: تا چندروز بعد از بازی با مصر از خواب می‌پریدم فکر می‌کردم صعود کردیم.  @Sportfars</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455442" target="_blank">📅 08:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE5mZ5YnB08KvK4qHna9f9eKsIylWe6CzP5iYEgoy1fKC3FW5JOOPRZReJqYRzacRVZmjuEscXcU7orTu3PKcQIgUE0SzeSn-6h2P1448az4VLbhBv5pME1AbTgXozqXQOlR0i7UCPcGfOAIjIaO2rO4Th33rrjpI0_DDzovN3wDe-13kq61HmX7CcJGRAxVbj1HXsPLSKuHGlWOBQtuSaI-C8ba7T3XSk07jFvoNqChRsSQJNjbIr-CEDh1B-IKj61WTRgHrERIO2DLcm8LIxjxjYOIi35_EA4QYUIiJ7N9umugdvXOg6w_nq3hALdTlutnXLGSgabjTM3VcpYtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیدر معروف ترکیه‌ای، قاچاقچی از آب درآمد
🔹
پلیس ترکیه شب گذشته از دستگیری صباح‌الدین شیرین، لیدر معروف اولتراهای گالاتاسرای خبر داد. صباح الدین معروف‌ترین لیدر سوپر لیگ ترکیه به شمار می‌آید.
🔹
حالا منابع ترکیه‌ای خبر می‌دهند که پلیس هنگام تفتیش خانۀ این لیدر ٧٠٠ هزار یورو پول نقد به همراه طلا و جواهرات به ارزش ٣٠٠ هزار یورو کشف و ضبط کرده است.
🔹
همچنین پلیس ترکیه یک قبضه سلاح گرم بدون مجوز از خانه این لیدر متهم به فعالیت در بازار سیاه بلیت‌فروشی، قاچاق مواد مخدر و تبانی کشف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455441" target="_blank">📅 07:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای امروز پایتخت روی عدد ۱۱۳ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455440" target="_blank">📅 07:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455436">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNNLKKGmjMY4tItR52JZKrLZQXH9ZUujZppG5r75WTaY3K9KbTgpTXxHGENHCM_sLhu2X3nNMdqnrJW-iUh6X0avRdRoHyti6Y9q5S-cVk02GdbDGXYOwpbF02e8BxJAifh393B4NH3qGuXrQ2SjjYrd2H81WHhCfz6TeLCGBCAOLYRsbwhBktUnGH_5XpkgYqZgX7XDIoo5VOhN_ewvplplbZ_7WtNHPUq0RBO7QUw9sxMRmUVRyLHJxxMoXkwagg2yOpy8Ha_JRL5lZru2mhmtFroqQ2ffNTYMOVaYkiK4xJ0brUb_RC1VVq5xkcIw4njyu0gVDW_cBk8y4EtobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EI5HQpH4hsfDX5D6t3iyZRpO0sq8wGRjr8fX-0O0l6nlqZsfd48vcoJT7h03yuQbI5_LbjHvUfl0zviqmqV8wDtcCVBsaR9qEHgTNIcn7tQqNVcrx05yarK_v0FBk3Y5BfMBwjpwmnVGpoLSdUnz1wNnksDYIqgftJgfTdPFkPQNVULprRin_oY-_9ocfIOGMU7gnAKcw9o22BxqMfcMXK3C1VBXQ1tEq5uU29_MJbHVe2KfhiRjxXjQ6F9WEx0rHn38cbyG7XyrTWk8QSnxiNsZ51Fcux2bhsQHj7-se8IclisBTr6Mt8wd2OIKPkV7acEkWjNmh0ae_bqBxOHg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZOu_uPd8wokuoquGMouv7e4uJytXSxxEklqrlKHHn8CptKthmf2yo45XJ5dPqeiLXQExyCX3ADI5Yv354AUb1dMkbrqlf11p6QjDp1Ws7QNjN8mk3ZP1yaj-Rbp3EBZKMh-Ibojq895cwrmvyAHZBDGB7nymBkpg8SgcgXPhYnjaEEY_nNiWdK-qTCV8nTGFsmPHWneD0MQzDrNNKdY74p3UKiT-GRCfSZo9tGF9WFdfDIzV2f7pNAcixBRGTwm9CzdxX1_DgVxUgs0GNeObuDGBTZrcKLK3c217lLEFovv8J2d2LdKZpiI0TUTwpHYuanlOym5Ho8xjJmKl36uLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac632d5b91.mp4?token=L6rif___MmHkZI07hBKHvQ0I5dDawcKZ4EbwyPDoJh4DOdFvFiPUpFJV7oggsWIMVrEEWf7oOVbpqJ96QEdUlF2NJNtpKF8213FT4Qco7NLw6qukYs1GTcZ7vJoLB-B2o7sXDvY7FceYkt99OLomdogxemq567bm8U3IEmwKHmtJ1GndoJtOEbsxfaGy3IKLJljOPzc1FoJEx_-Q2lNztyp5XfOhCT4P96p6oxsqLWdpoTrsO8Ow6s9vkV7AD0waZXvp2O0apXlpPLI-sW04lum5J4_fV5Af-B1iV6OYyUOpSxj0E_vAPVAJ8qasxNo3baibu2Hh3LaedW7GOgJHrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac632d5b91.mp4?token=L6rif___MmHkZI07hBKHvQ0I5dDawcKZ4EbwyPDoJh4DOdFvFiPUpFJV7oggsWIMVrEEWf7oOVbpqJ96QEdUlF2NJNtpKF8213FT4Qco7NLw6qukYs1GTcZ7vJoLB-B2o7sXDvY7FceYkt99OLomdogxemq567bm8U3IEmwKHmtJ1GndoJtOEbsxfaGy3IKLJljOPzc1FoJEx_-Q2lNztyp5XfOhCT4P96p6oxsqLWdpoTrsO8Ow6s9vkV7AD0waZXvp2O0apXlpPLI-sW04lum5J4_fV5Af-B1iV6OYyUOpSxj0E_vAPVAJ8qasxNo3baibu2Hh3LaedW7GOgJHrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: زلزلۀ ۷.۴ ریشتری غرب کلمبیا را لرزاند  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455436" target="_blank">📅 06:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455435">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سقوط جنگندۀ اوکراینی هنگام شلیک موشک هوا به هوا
🔹
نیروی هوایی اوکراین اعلام کرد که خلبان یک جنگندۀ میگ-۲۹ هنگام شلیک موشک هوا به هوا در منطقۀ اودسا، کنترل هواپیما را از دست داد و باعث آتش گرفتن آن شد.
🔹
این حادثه زمانی رخ داده که جنگندۀ اوکراینی به‌دنبال هدف قرار دادن یک پهپاد روسی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455435" target="_blank">📅 06:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455434">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71faae8b44.mp4?token=uuhDH9GcsbRAwPuya1StqYKELpV-7_c6Ldx4MfuJ5qNFn_n6ZfgI1uS3Cq_kezVL8keFasPmEtxHDWL39BXhFZfMqnBj_SVjP1AQS-HFOSeE_N_HnBKMMvc1bvhvXyKpimeEICUwwr4O_fl6oi9PdtneH3p_9-NiQpklsejCCF380hDj-RB_osAh2LF6wBGsvutdoQeGBpePyogPo1jzcJaaraS81kGJtSGmo1BT2aVz3D_fh4a3nzOkuGiMc7SIQ4EFv0u-glTMmtBVQepZc9WUgO8NDbMvnEQGmMxtW8ngcWo70SaSS_AZ9iwnydBDlfTLu_AI3PRVTuCpKpHKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71faae8b44.mp4?token=uuhDH9GcsbRAwPuya1StqYKELpV-7_c6Ldx4MfuJ5qNFn_n6ZfgI1uS3Cq_kezVL8keFasPmEtxHDWL39BXhFZfMqnBj_SVjP1AQS-HFOSeE_N_HnBKMMvc1bvhvXyKpimeEICUwwr4O_fl6oi9PdtneH3p_9-NiQpklsejCCF380hDj-RB_osAh2LF6wBGsvutdoQeGBpePyogPo1jzcJaaraS81kGJtSGmo1BT2aVz3D_fh4a3nzOkuGiMc7SIQ4EFv0u-glTMmtBVQepZc9WUgO8NDbMvnEQGmMxtW8ngcWo70SaSS_AZ9iwnydBDlfTLu_AI3PRVTuCpKpHKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی گل عجیب با پایانی باور نکردنی
🔹
یک جشن گل معمولی در فوتبال برزیل به صحنه‌ای باور نکردنی تبدیل شد، جایی که مدافع کوریتیبا پس از تصور گلزنی و دویدن به سمت هواداران برای شادی، ناگهان داخل تونل کنار زمین سقوط کرد!
🔹
او پس از سقوط توانست از تونل خارج شود؛ اما VAR پس از بررسی صحنه، گل را به دلیل آفساید مردود اعلام کرد تا بازیکن برزیلی عملاً هم جشن گل را از دست بدهد و هم با مصدومیت مواجه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455434" target="_blank">📅 06:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455433">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6XVkS9BxHnJl9cmriFU3jHRSSTJ5pKJc_MIhAd5XEzIsNUKjCD8Z_sBxxd7xm4BqMxCs6tnTe4LwHbVdl5JUKqonk2RPfSDNjOpsBOrANWPqdWNhDomvEhcHXeQzvFm7QmLJXjzAIBokzhLq2OLq5_LWwRnXKvSuevcoWEm8PE0MCUJuS8ua1SHXTeOtAO6kAIj_4sqm9em-tJE_Du3fnY4T7wbPvfuEi5TAI4TdZ5-xbaoAaHb1rO1aNLKJ4VOBGvPTvJ3Kn0N2kzQyRIbnv_gTFv2a5D9L2HlwWuiknYmDHsc2bQs01exzKbJiwIPN2PVDKBk5o3d7S7fP5rpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ آمریکا به اکوسیستم تنگۀ هرمز
🔹
تصاویر ماهواره‌ای از نشت گستردۀ نفت در بخش‌هایی از جنوبی تنگۀ هرمز خبر می‌دهد.
🔹
این نشتی از نفتکش‌های متخلفی است که با تحریک آمریکا قصد عبور از تنگۀ هرمز را داشته‌اند.
🔹
پیش‌تر ایران اعلام کرده بود، خسارت آسیب‌های زیست محیطی را از کشتی‌های متخلف مطالبه خواهد کرد.
🔹
طبق برآورد تصاویر ماهواره‌ای، سطح نشت نفت در جنوب خلیج فارس ۳۹۰ کیلومتر مربع برآورد می‌شود؛ این رقم معادل نصف مساحت شهر تهران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455433" target="_blank">📅 05:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455432">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajXOQP48l0m1nPSwaMJhQQFHMellJkHII45Fqcsdyd7eWhhUL6rDPPrTXMn-lWNsOxric-feei2WsbF-Rq8MZUPBh_Ups6MYuklHMNhLI1Ugkd0v8dVxhYTo8Xa6KPF_J1NVUca1oifyzpN-ObU0o0816CvezQLlDqLnS38OjrJal1SkL4NaQR96Wx7b1r7IY0dSeCKj44izxQAAB3Pubrf3SnJesJFUsjIytheCvZ5WgwL1U25J1ZRIYnGcQz6pzo7kt-xnzCJenajKZBAfM9lZQdJCsSN7qX5qMTYT9pAhBkXzZCwKDkilrDjoJqsrsCgvpXe3G0bN-jyPkntQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادر بر تن متهم؛ احترام به حجاب یا اهانت به چادری‌ها؟
🔹
انتشار تصویر متهم زن در پروندۀ قتل حمیدرضا رجب‌زاده با پوشش چادر، بحث دربارۀ پوشش بازداشت‌شدگان را دوباره بر سر زبان‌ها انداخته است.
🔹
استفاده از چادر توسط متهمان را در گذشته هم در پرونده‌های مختلفی شاهد…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/455432" target="_blank">📅 04:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455431">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8319e8a5be.mp4?token=LQEsupL3cQ7x9HatzvLjXIvG245I0s_DJRZeZ3NOjPMVkrYqDs6X_3hFMANLpwCRHErj4u3XuIdXk3m3O8H15ZOrSU2HPxWyd64_2k6LJZ-zJmyjockTO_mLdQw3XPJ5lyISOrNE0diHHzMVCmmEJnL6drAYbO05CAiIi_9OioM6LpSgyNqz0d5r6tkPhInEkyhel25IYszsfsdMXPFazaOR4S9YtsTLItNl-pnidho2GqPHR-aBVsu6ufdNyysfDrpqQ0MOPXCoaArU86rGTB2_bQV03O4Y_46ah5BqGompkjMvj0Wqkhobv9PkvhHlSqhrV69tLry_U1xv1bNX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8319e8a5be.mp4?token=LQEsupL3cQ7x9HatzvLjXIvG245I0s_DJRZeZ3NOjPMVkrYqDs6X_3hFMANLpwCRHErj4u3XuIdXk3m3O8H15ZOrSU2HPxWyd64_2k6LJZ-zJmyjockTO_mLdQw3XPJ5lyISOrNE0diHHzMVCmmEJnL6drAYbO05CAiIi_9OioM6LpSgyNqz0d5r6tkPhInEkyhel25IYszsfsdMXPFazaOR4S9YtsTLItNl-pnidho2GqPHR-aBVsu6ufdNyysfDrpqQ0MOPXCoaArU86rGTB2_bQV03O4Y_46ah5BqGompkjMvj0Wqkhobv9PkvhHlSqhrV69tLry_U1xv1bNX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): نادان اشتباهش را نمی‌فهمد و نصیحت را نمی‌پذیرد
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455431" target="_blank">📅 03:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455430">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyXXjdFVneO99mJIMKOkQCtizcFSZ7xQkpRy3LHYIeI6EK2WMUZqrIWXfXZRX0u4ncol1DUNqFsKTfCBENf42Zp8uu7wywOQgbBeNpl6eVA5AWIdyweAvCW8kDGm17hIfTmfKnK1yw9IKiPfAlWK8vm6xZi5TUy82NBGFoZfsBSfGOVjgAP3ElhKm-9UlBkxHvNyiPb0IKm2uhY1iA5ShiEOpwsJigKUuIrzQ5OJpcWhV6LBxUAmQwQluNlPKNOYoMxk7G7ZaNb6je610ZfTh5yPU8da7vL4GYDRTcBBxA_HvdVTEMcWzwKQZY72L1qvDMbMF_dXyca9_x0fbZGUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک فاکتوری ایران رونمایی شد!
🔹
رسانۀ تایم گزارش داده، اخذ اطلاعات، استعلام، اخذ بهای خدمات و در انتها صدور یک فاکتور تنها بروکراسی لازم برای عبور امن از تنگۀ هرمز است.
🔹
ایران این روند را «ترتیبات ایرانی» نام‌گذاری کرده و از طریق یک فاکتور شیر ۲۰ درصد نفت جهان را به دست گرفته است.
🔹
به گفتۀ این رسانه، حملات این روزهای ایران نه از مسیر موشک بلکه از راه فاکتور پیگیری می‌شود و این ذخایر راهبردی نفت آمریکا است که هزینۀ لفاظی‌های ترامپ را می‌پردازد.
🔹
هزینه‌ای که فقط در یک قلم سبب شده ذخایر آمریکا ۲۵ درصد تخلیه و به کمترین میزان در ۴۳ سال اخیر برسد.
🔸
از روز یکشنبه تاکنون نفت از نزدیکی کانال ۷۰ دلار به مرز ۸۸ دلار رسیده و اقتصادهای غربی و شرقی را زیر فشار برده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/455430" target="_blank">📅 03:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455428">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc9HPTXuLADF7bE36gVUDvJC1Sr5-u5uAgiJliqFQZ4NklgmHtqxQ4w-lEjyT0FquQ7HG27U_pc8Znthm9AR1HPuD8MVZzyw4VrtjNHaXIwifBIr3Pjq3RE9GGWWT2EdLmGCSvflixcd7TGOalVPbQTS6msWB6PrumMcFMWyFCBOznFNb74gC0phae2uddfHp3_qWnprclX7ugAfacJfJgh5RtY_zeRFKAJlVQbiiPsTlhnxKPybedj5vD9CcQ5D4AmmS9-dALFRnXLqX1MhdL2zfXQA9-URuy-oQsOFtYEnFD17n9MB1C6Hmsz7K9oSbTdKBVIPdLNQv0A_-7Z4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات فلسطینی: قربانیان غزه از ۷۵ هزار شهید عبور کرد
🔹
سفیر تشکیلات خودگردان فلسطین در مسکو: شمار شهدای حملات رژیم صهیونیستی به نوار غزه از اکتبر ۲۰۲۳ تاکنون از ۷۵ هزار نفر گذشته است.
🔹
در این حملات وحشیانه که با حمایت غرب و سکوت مجامع بین‌المللی انجام شده، حداقل ۲۵۰ هزار فلسطینی نیز مجروح شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455428" target="_blank">📅 02:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455427">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPI5wgF_3spuNeVwg7HIe0p1gxa85TFpYIV9DHC8KwpGxJGNx5uhyPXjSJLEBWOuFgivXP9zJXINdj634sDJKGVwAAmjE8cKgBrSTPOlX_8b1x9Q-AIemR_SXnWEUEVzAl4rsHeuskO8owDbbxlmNr5maO4ZsCRU98Fdq7llepgYXy0Wz7JIuAnVS3Q6h9q7HDR7Kr3R19ArESbVG3hVODFUfOjI4VMD15ews_zw4LlRQYf0DJ2e8BQAxXAKbaZ6-5DZCaHQDqjWC9zVeMxirJS8c2__q0eykShRoBui8jiBiDhXKwyL9t72mK2ueKFyG04q3WSCrqBC6mb1MwQ_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدۀ هیجان‌انگیز تاج به استقلال
🔹
تاج امشب خبر داد که شاید سرنوشت قهرمان فصل قبل لیگ برتر که ناتمام ماند در جشن برترین‌های لیگ مشخص شود و استقلال کاپ را از آن خودش بکند.
🔹
باشگاه استقلال استدلال کرده چون در زمان توقف لیگ، صدرنشین جدول بوده و با همین جدول، استقلال به‌عنوان تیم اول به آسیا و لیگ نخبگان معرفی شده، بنابراین از نظر آن‌ها منطق و عدالت حکم می‌کند استقلال به‌عنوان قهرمان معرفی شود. سرپرست مدیرعاملی استقلال نیز تأکید کرده که «جام قهرمانی را باید به استقلال بدهند» و این جام را «حق هواداران استقلال» دانسته است.
🔸
وی گفته باشگاه برای این مطالبه، بیش از صد صفحه مستند حقوقی و نمونه‌های بین‌المللی آماده کرده تا نشان دهد در لیگ‌های مشابه، تیم صدرنشین در فصل نیمه‌تمام قهرمان اعلام شده.
اعضای هیئت‌رئیسه فدراسیون این درخواست را رد کرده بودند.
🔹
حالا تاج می‌گوید شاید آنها در مراسم برترین‌های لیگ برتر جام را به استقلال اهدا کنند. اظهارنظری که احتمال زیاد با واکنش منفی تیم‌های دیگر همراه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455427" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455426">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4c62bc0a.mp4?token=sNjQRfAWIxAUnHMNCnLXI_u6Owe_OAo8_FcX11YfhO6vO5Crui1oL0o-QvI28C85ZjFZAO2vJtbrF2N4Xw8JVXat7LoSeURoV3PmqeQCdm1eTzeG0BZNYgBwHfyAsZKpWp46noeMUe88QB3S8merEK9anj6oAndqaEOOv3B7_3IXnpoRQwFa2bdY1wkraTSm1mqjvs_4vGjU-sGNUflisEg4XmAQoWNqLrfpffi9rAF22i5nzWmINiPZuRKo8c6GBjbVmHsc0Xg5XNMzz8lLNSlAB8JWbuwZh1aA0nTqm1SPzLsqBi9Gu1cFwZCh0DA-7RRNL6zq45S5D8V35xHSiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4c62bc0a.mp4?token=sNjQRfAWIxAUnHMNCnLXI_u6Owe_OAo8_FcX11YfhO6vO5Crui1oL0o-QvI28C85ZjFZAO2vJtbrF2N4Xw8JVXat7LoSeURoV3PmqeQCdm1eTzeG0BZNYgBwHfyAsZKpWp46noeMUe88QB3S8merEK9anj6oAndqaEOOv3B7_3IXnpoRQwFa2bdY1wkraTSm1mqjvs_4vGjU-sGNUflisEg4XmAQoWNqLrfpffi9rAF22i5nzWmINiPZuRKo8c6GBjbVmHsc0Xg5XNMzz8lLNSlAB8JWbuwZh1aA0nTqm1SPzLsqBi9Gu1cFwZCh0DA-7RRNL6zq45S5D8V35xHSiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ پهپادی جدید به یک پالایشگاه نفت در لیبی
🔹
شرکت ملی نفت لیبی اعلام کرد که کارخانه ترکیب و بسته‌بندی نفت در پالایشگاه «الزاویه» هدف حملۀ پهپادی مجدد قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/455426" target="_blank">📅 02:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455425">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca8fd7a3a.mp4?token=soKF8Uq2_FoTBzJ6Y7jS_j0uG7hv65Jgl5wdipDmF6SnqZCX1VJzyL18pjJ8a33VJvU_9G3N7gBflWIVsXfqvKtLHMDLCrLkk1_oLxatC2Tl96c0Om8I9qWmQyJqlQFk5cm103_jS_PglcMSUp9Zg0wsUxsiTm0xNOx2bTL_I6a0r6JXQBWIf38H5lcIUpafcrjwtJI0L89-psrzr2uzkGQn86lnt1aoWlwejUq2fBRZTBMrRYe9ncw_r4nG2wTdcLVM7pedcuEUG3_ohA3HxO9NkzOCrp1SESpSnWG3NaZ6txrOHg3aShiPMgDWW-mMG4U5bmZhnGHv83feU8K3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca8fd7a3a.mp4?token=soKF8Uq2_FoTBzJ6Y7jS_j0uG7hv65Jgl5wdipDmF6SnqZCX1VJzyL18pjJ8a33VJvU_9G3N7gBflWIVsXfqvKtLHMDLCrLkk1_oLxatC2Tl96c0Om8I9qWmQyJqlQFk5cm103_jS_PglcMSUp9Zg0wsUxsiTm0xNOx2bTL_I6a0r6JXQBWIf38H5lcIUpafcrjwtJI0L89-psrzr2uzkGQn86lnt1aoWlwejUq2fBRZTBMrRYe9ncw_r4nG2wTdcLVM7pedcuEUG3_ohA3HxO9NkzOCrp1SESpSnWG3NaZ6txrOHg3aShiPMgDWW-mMG4U5bmZhnGHv83feU8K3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان: تا چندروز بعد از بازی با مصر از خواب می‌پریدم فکر می‌کردم صعود کردیم.
@Sportfars</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455425" target="_blank">📅 01:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455424">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شهردار کی‌یف، پایتخت اوکراین از حملۀ موشکی روسیه به این شهر خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455424" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455423">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2069b5638c.mp4?token=p_vwWCMO29xWw5BdAxzNYzDfO8oaBjZva6KXIDE4l9URC5JrrydhX7MbEe3KP7fsXYRyQg7cF5T6dO0YqSttc4BrlNLSvtLU6UR8XrFHfHgpYebIOZcfJWqRMs2gDQgt0CMW_Y4zv-WchoWJ4MGhXLHPXVXGsFd7mqW9e9iEYXnS3M6PK1a9Ie2_JeoE7npv-Q1RNBwlb6f1wrPFVjzkKkCmUyLdyA1Ir03_RukTLqpIh3B0Bmd2Cjkhfu6XDGqgzWMBfAakczIfxXP13wYSLQRPVnBkD1jWaT1WwS1c-Ues09Njbn0WrAysNkPqLRvCU0xhc8OC5etC1KvjUBvV-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2069b5638c.mp4?token=p_vwWCMO29xWw5BdAxzNYzDfO8oaBjZva6KXIDE4l9URC5JrrydhX7MbEe3KP7fsXYRyQg7cF5T6dO0YqSttc4BrlNLSvtLU6UR8XrFHfHgpYebIOZcfJWqRMs2gDQgt0CMW_Y4zv-WchoWJ4MGhXLHPXVXGsFd7mqW9e9iEYXnS3M6PK1a9Ie2_JeoE7npv-Q1RNBwlb6f1wrPFVjzkKkCmUyLdyA1Ir03_RukTLqpIh3B0Bmd2Cjkhfu6XDGqgzWMBfAakczIfxXP13wYSLQRPVnBkD1jWaT1WwS1c-Ues09Njbn0WrAysNkPqLRvCU0xhc8OC5etC1KvjUBvV-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رقم فسخ قرارداد باورنکردنی رضاییان با استقلال
🔹
قرارداد رامین رضاییان با استقلال یک سال پیش از پایان فسخ شد؛ چراکه بند فسخی در آن بوده که در صورت پرداخت یکی از طرفین لغو می‌شده است.
🔹
بختیاری‌زاده، سرمربی استقلال پیش‌تر به رضاییان اولتیماتوم داده بود که زودتر سر تمرینات آبی‌پوشان حاضر شود.
🔹
حالا رامین رضاییان می‌گوید بختیاری‌زاده، سرمربی تیم و مدیریت باشگاه علاقه‌ای به تمدید قرارداد با او نداشته و اصلاً با وی تماس نگرفته‌اند. به‌همین دلیل وی با پرداخت تنها ۱۰۰ میلیون تومان توانسته از این تیم جدا شود.
🔹
به گفتۀ رضاییان مسئولان باشگاه به این دلیل چنین رقم فسخ کمی گذاشته‌اند که فکر می‌کردند بازی او تمام شده و ارزش بند و قرارداد بیش از این را نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455423" target="_blank">📅 01:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455422">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملات توپخانه‌ای مزدوران سعودی به جنوب غرب یمن
🔹
منابع خبری گزارش دادند که مناطقی در شهرستان التعزیه واقع در استان تعز هدف حملات توپخانه‌ای مزدوران سعودی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455422" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455421">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaxmmJlCKQZfsHMv-TYROLH3k-CN-IiLWLSGVvsIoSoF72TXF_axp-UNc6GsLjTccxDIshVj3PG7QWR4YPYFyEmtRJFB2a3adv18IDdvAB6Nk1fKAR2p_y4lraNVtTM2Gpzs5Ise0BTDDssffAytPoqaIBecNZyEnmEXMwWIGbBmBIBHZstru8qp-JHSB0EgK8PjRcUmSNMkLEmBXjqamkFN8v9_hd7nw2YfX_AaLi7rZYOyYrLXIs8xl5j5YpEdMtwPDKTgAs2L9sBt_juQdii6eOagBbHEIUYEEFkdjHwzXoFBP7mEs12yNKwBme3Um_laD9lU6ctxjCJFTCBMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لشکرکشی نفتکش‌های عربستانی به سوی تنگۀ هرمز
🔹
گروهی از نفتکش‌های مرتبط با عربستان از دریای عمان به سمت تنگۀ هرمز روانه‌ شده‌اند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگۀ هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔸
تنها راه بدون نظارت ایران و محور مقاومت برای نفتکش‌های عربستانی حرکت از کانال سوئز، دورزدن آفریقا و گذر از دماغۀ امیدنیک است که طول سفر را ۲۵ روز افزایش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/455421" target="_blank">📅 00:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455420">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699415d3e1.mp4?token=fyOHhWn2Xp8Ez8Icb8tq-7n_1xFjSRJHWYfVDZBGFFw2vPDjAl9OFJegWFpXgDJiB5M-rXB4lS2fBNwfs2OojLyYuuDPz_yZptdYd8QyYD7jCLN4YDwnBShY7wO2m0WDiEwkZpOMLzVR2bRiDkaXohRk1VwKZlJ7buIwGQHnuZDwYlut90z6amdiYjrAWjPXkgOZJ1DwoyY22hn0ITSR9EDNaUzVfol0UdkqbOvswRub95GCWAxfr3TSv9R3zcf6SLyHaeR-jV2VkOGh1gqSSPLx8CmJl8_3eeTW8g-hp9BjAWyw8ZDjkErv9y6hergHDqAIvd8pDQDyIavG9tY_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699415d3e1.mp4?token=fyOHhWn2Xp8Ez8Icb8tq-7n_1xFjSRJHWYfVDZBGFFw2vPDjAl9OFJegWFpXgDJiB5M-rXB4lS2fBNwfs2OojLyYuuDPz_yZptdYd8QyYD7jCLN4YDwnBShY7wO2m0WDiEwkZpOMLzVR2bRiDkaXohRk1VwKZlJ7buIwGQHnuZDwYlut90z6amdiYjrAWjPXkgOZJ1DwoyY22hn0ITSR9EDNaUzVfol0UdkqbOvswRub95GCWAxfr3TSv9R3zcf6SLyHaeR-jV2VkOGh1gqSSPLx8CmJl8_3eeTW8g-hp9BjAWyw8ZDjkErv9y6hergHDqAIvd8pDQDyIavG9tY_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیال‌بافی ترامپ: تنگۀ هرمز باز و در کنترل آمریکا است
🔹
رئیس جمهور آمریکا شامگاه دوشنبه با ادعای اینکه تنگۀ هرمز را به‌صورت کامل از مین‌های آبی پاکسازی کرده‌اند، گفت که ایران اما هنوز می‌تواند مشکل ایجاد کند.
🔹
ترامپ در پاسخ به سوالات خبرنگاران در دفتر کار خود، مدعی شد:‌ «ما یک محاصره بی‌عیب و نقص [علیه ایران] داریم. آنها ورشکسته هستند و پولی ندارند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455420" target="_blank">📅 00:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mblb53ol9Mlx26pc6QQ8BqMRGSgJ-HjIvnY_VqJPVkDcctz3M19Qw0DyfFqGkMc-7Qt0otOrelfJ1kvSMGyoutRuUu4bKdGzsCLzg-6wX8vKHzbBzk-9LLHQFCOxSTmavOBQxNZpAm6EtQ2yGpc_YlQY6QZ3ZfTwtgNYttc5D2l7bVhx69VocBqWsrGdTenYRL7wP_nxEUf4kvLzjzd6brGO4gQsZ91NvJGmhbAt26X6SmaRPNFpJJn2tZ4MMIbkWNi541vpoHykTTT9XQxhyKghjMmzT7OcLkiclZLz3Fzjsw_44sGUujleq676PF4onvvJev8HtA1aKo03rurr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzsqquAMC0oD-OkYKRb8hMCm2jMvK70ARrQ7oZFpHgD-OA-c2WeF2fjfqfE8hhgccZZbDvli2kyoPfJ6w3LXNW1hJ6hh5-M7s55UBAWx149Svo3bUWH9CmG1fIIpCbjBH3yQPExl7bBQHSc92hIyl7DE9A89oXyypzzDe0IGCfZcqIjsP4VfYTYRCpXkPjQVZGqnAGMD2IfplDiPhWaVWa4SDU40yNlUNBZzZVtxf3otwJO7dzVtW5Hs7-8UW8ddw_fDubr3z_2PoBxQpw43ncR9kyYq7W1k5Jbl22VqDbN9fWy7xVljNaa3GYK2WEewhzbgkAdIRzaI_6fzvMatJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtHY8vhECUfhzBDVV2UyooVfyLqhydNIiUw2TMRHOTozudjQQh6WI7EV8E3z8ugtMg1HNzSgmSwgBJpZdRCrQ19_rP-yMn1Er5QWH4EDzsHWSOdsKgy0qITRixnP86TsXXey3nQB3O0NvjS62-A04bN0WMZMhmt4lyd-alz8H_bcSoYM8pSksYxYXT3-pac0cZDDbpf3UP4u6BSDKcwPYsCk3Ua6o1k-vHePSazaFlbD50xyWO3iHLUcM61fAbDgNfCHlL1wsYQOML1Z4nN32USwubzpWvJmEJFOyHBDyvGTOl6FihENVDjEWlXawkiHasiS3kvzgexrN0d4QHeH_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ai4G2rfdi_CB9_UH-Kkuyc-dF9nnzxgQcZ1jIy_6e8oquKEQI4tYE4AjYY3uQvdT1xtkILN1YVkwQ1nn59omLqmdoqr8caeUgXCYERRzzi71IObO6e8VeMQYnntd9AxVIvCCrIxUp08oyoXA1dVdX2O2rr8WpTlGmQCe-vTzKDdJmp-tJxBOHZ18qZegltwb3-Wld5kjnGdnUf1pTNwPX4PffU6sOXJ3p1lCWVX1NXjoSPXuftiXtFXSQ_n5fVnw2zOomGtlNYlIyOJy997MLW9mIRy6dvtH9eaAZgAYbwiA04aQpPupoyp9i98207nc0g9S4mXcErmQuGIuHiLzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1SC3AJlFm0bOsiERLJZ6CWEic12zbkcr9JxEL93Nw_a0YkiUgUnm67zW_o0MEOm-klLUL6tI4XCTDiFYHF3YPztF37XS_zJIQNym73O1CTDlUhvy3Vufgh6JYM8b011SgWGY4NlsiPbv2e83ZjCfsNhf1jYQdNznGPrlg61I-9a_O0opsooiVPIl8mACtEnqgBIF5ZD7EzfNp1tKrO5uMc4jSXCyLjGQlkK0deDjFgJWEhJaoGQJC-SeND0erWDNl4pj_PJMTFcT5MTKK3v9jTlCzpdl8CHmqrJXOrQMdnEoe7TanIiS5SwM_kCRkH8WzMCtSkPYpKzL2H2tbJnYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۰ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455415" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zyn9gjRoLpl7ZcwOEd0etHONZi_skilh1AflTACiSS8KZiQCAhD7Ss0yaDOToV6SLrdsr9XikGim3S6Nvw-wwyWpYoGVHhAIwO7ZPazciGa_Q2rTQdCMTyw5yKmks22VSpv3tz4hUGi4UDmdrD-zoiwKzMI61VLsxJhgVAoDDbt5BzpW8kYrwuC4up9WZh8rNCW9mKrhPDG63tcrIkBzV49Gsk_PXK99hl3iMnxIAzs79sw9OTf2YPKQrPq1X2ylDcbS-As0oEMWP4JvwOvL0iWA3BAAk4l3fz9fNxe6wmRgGMuJ4848y9mJNY64arJFadMzWl5MsK_KAvPs9FnHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJ5FKXTQLX4KHhbA57xYp_a4-gUXAyJRr6XoD7nsuDPw2dGOLMEq7R3o1JPSQ84-27DYFQwa2-5kAkUuKNuUNI42ji1XZAsjc8qi67Ogm-38lZ_Al03jQzQSTdyqhajHG71N8crAZFz04gJSL4YKF9_ZP3_R8pmlCeoe3PWXZv18hE2BNgzq7DU1cXuTVi6ljuWZRSLnPFapWrJiQqaNC5PXh8mUsImbiK9oLyDs_HmOs2Bm6eflgq7iIF2wX7eBUbc7vYCtsCwKl1mBr7-XUkKJ6pwLF0R6by20SmA9hV8yUSiyxM7juNFtNEcmRO6s1CprWlResxfvjpKgIIvvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHq6TDlYzfar4q0ssva25Fo3VfqncdpAVH1lu7I5-DSsbGXAuPxQwhysuT2rWg63LIhbIyLE8G0MOifr7-6cwPv6iZBBLi7yPDImaEdwpwizMPAp30_coCuuOgXxLBr0HRWyopfXIkm5elE8TLE3JGbcnRFj6u2QN1k6dIkoz8kuIVIcSMFvWgRN1oiX5YHss9xwx7hBR1V5Q2UaslduL-QFbnPZFNa8a1PHqfuQG2-GnkFlreg-u_ORELaarqAua5nZzQI_HilrE7lzAD3pFE_4tVLrQ5fp6YIepc16R6X4eu9TAVLREMARDNPjVgiWjNCdwrDTjDuHVaD5WJQ5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVWN8XTUZGm0vX_xpzPUYSSpW3tnOIFZkEIx8v626bscnQ78fbR0Rmxml9xREOUn8ebtEXMIuYpBMdyn7Rlzt7_csCmwtpgCNB3D_pxWbeowlQziORWhvtbl4IC2pnO01gcnCepnPieEEzMBAE3iPxuu065nle7jz5eJz9z5Oqo27yYL3oiEHPeT3DbVqjsbMsqV-FkWUvU_LMM6lgf5ml2iIYYLJjdE4H6Cvj0HG-ldSYLPGIctjJ0YGXnOU2WCPNunmmI_rW44RRKskz1ayifksL_Qneqpk5MpTxhSkz6AcOXAdxMZV1EuEtZUg0MDMMYm7L32AMPOZEPtLtdFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vx1c2SOGWn3g8BfL36OxPb1B9mM5xjmjQ0v75SGUznctuaOK9z1Ucvk2Aino3G01EsejRpbC50x4Iu6xUG_YjNYjOI4FfWErfIBFFbuGk7yljsc1yBJ8Gcp8E5A1sEkxbK8f1f-aib2KrWSwcsazs1rM0r9jpeozJQWSkT4kZbWWjGs7SFjy_pVCNlVlCp_tXBygXLsS89eOyGC-NBnqJLPUBVUW8I4zGdelkbkUeh2xxsMCBoIe3hfiClOJUG0j3mswqvLGiwEigaVm6zqvLHPMwhRRP7zx4Y3SVJQaKDinKzZUmC-ykV04Abtvm_lR7E8MIV7cTJRhnVVJv7BzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shigRJTHPAnLcP6xpqTuXY2zugrqT9Eue9KcVSHJfhO9isDkMtCO_Cc0MhPFGsSmEuynQe5JIq_iBvD3I3wQGgky4yBmQsaDiG0Gw2041IFObrMixtO8fsuGcIdQJx0evAjih5rQq7SJ8EFAl8Lkklv_GfoeuMfdPWCVjYFhtt3fqZPOZi1YSTRk7Uet7J0NjNuYAI-1OvOy_2KT3qgBE9l7CJFszdybO7SlDcubj9xQyeHz5tRZ6L8yq8QyjGZanOXGhsAbdVz7zjU_k07n9DTKMYgS0nkfPqzOBrh2t8wIcGW1xnHGOSmCXA2H-sSstBt_CzX-h_YyMEfCYv1QJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpAipUnTMrW7tM3w1w2YtiLEis0KPHyL7f-ld0i2Wasxs9dGlp4Cn2qJTqLn4L1lG43JRavTD1bCVNOeYcxWnqEVeEe3ydiVlVw1j_zSFPvqynwsLPccholh-7Aj9FCdGVXEZRWwbZPnOqeabPrAjZxEseWJNKhbXYGfIOMyCyB-VByB0Rr4RqH1kkVwlM63vjaD7cT53kz-UuItbF018rjTyzudgK0Olkkjc7f9kF1_TwkWzX6KKuhA7lHDU5uKA_CPx7n1NXteKPucqe_VzzakGWK1cDpso2_lxZtpE5OPNtfMOpyfmyZtl0sEplsbFXDHwc-m_fT8Gnp8M8jPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH6kcQP_Xgo_W9MYIe87inqyXCnzGKdSOc0gl0l94GWjsa2mnGy6GON6Oo8CQ8EOarqbUHy23SMZWZ1dy1smCqzF28-wcO6bIaYuj136Gje6BANE3QuJIDj6OV3cdBCmPevaxwQnrvI2B_EpQIDOrQowJM0EsCsv5ZYKqYjmxSF5ucka_-yDaP2jXP6tjfUvRxiCdEP_K4QjRGNK0duWFbaiVhWahpPph1wu8th3A9X5zvSPdXbewbLxiCq0_4mlKaynJSfwkGvN-sHdn-LC8LtNciLbjLMreP7r64sRTraAyeNs_St2VtkLE7Zp1KcF0eDyJAap8kl-qgpMcajbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBFkmfcPUFZduVz7eP-aC-e5qlrxJdgG9E4S1dnpzU0Cx4YjDA8nr62gCeDnDHyC8O7m90IVj70GBnqyIckZ-_9ynzWJxcVxizsOfhDeYSDlvOQPay7gPpe3ZAFLKmV4XHMnz9K-YOWbgHsjdJIcvNSV8L4IDCjuNipSacq9po9gYapLTeDUf0_-endL-BoqKlrkYAYWJ-GZEqtqhfaFaSpBltNa-IGovXNttZEhKs_BZ7EFcQPQxF11Blip-Va_68O2Mlb3GAs_9BjaH2INexoj_az2op5-HnMft1yLxX5g8FeWkc2wH96dUNJFAh6duM_Qd89kA9f6uYXxlldXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4X3ZnEmC2NH-7yvlDIMp2yOJ4MsKlXs1YWDElrgzKXwcX1bKmnRogNiTHt-GQIIqeGoI685o6xZY6DLeaZltr2DAgchR4NCurYrqpE0D8cq7f9s5kTGWGLUhdFXXdxC6-OKVU2uKqWPlEQBZ5ijcDf5c09R-1_ApRLtOjC1SQkq_G9jbIi7YnE942TlVfOJmh0tX9uHBgAlmxgi-_VHzSgLQRuIfj3wiqzHBfo77iUrNPR3vA23kzuQzUXvvFmx_BOR-eIVaBJMNGWoiDjrTejSxUP0eO-oyeK2ZnhVrTU3A7ws4vovls3kKXw3n9G42vFm0rOwEBg5vwPIvPUvyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455405" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455404">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4136877665.mp4?token=ZyXADOrIrzn7JamP5YmWH6dAe2QgrGmuFhCyyBHTRgdO9lfQSLiEc-wpxPDhLevoaDP1uNu2MGrGFqT9CMQCFV3A2jbziwV0CmLDkx5P83cHVKMZ7_Y_uFfcqaFBFBBKi-3Sprv1Vgxh1_gM43RibZEMEmjI1MY2qoQu1iQNpoCkGbGpIdUWMjHVSjELzXoMUnACKKHc8KK3uiPlPl5uJ-u0ZUNXiy45ozZzXK1Qi3BzskTEqXFS7AC5KTzZK94xwEtc7PF7nz7eTgB65XkdkBiAhhlLi9myYWO83zbHTJdybfuRAEtlGztXEBasjVuMmHK4RKT7a-B8wlBEuDeA-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4136877665.mp4?token=ZyXADOrIrzn7JamP5YmWH6dAe2QgrGmuFhCyyBHTRgdO9lfQSLiEc-wpxPDhLevoaDP1uNu2MGrGFqT9CMQCFV3A2jbziwV0CmLDkx5P83cHVKMZ7_Y_uFfcqaFBFBBKi-3Sprv1Vgxh1_gM43RibZEMEmjI1MY2qoQu1iQNpoCkGbGpIdUWMjHVSjELzXoMUnACKKHc8KK3uiPlPl5uJ-u0ZUNXiy45ozZzXK1Qi3BzskTEqXFS7AC5KTzZK94xwEtc7PF7nz7eTgB65XkdkBiAhhlLi9myYWO83zbHTJdybfuRAEtlGztXEBasjVuMmHK4RKT7a-B8wlBEuDeA-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آغاز تحقیقات از متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده
🔹
سخنگوی پلیس: پس از دستگیری متهمان اصلی پرونده «حمیدرضا رجب‌زاده»، تحقیقات توسط کارآگاهان پلیس آگاهی دربارۀ علت و چگونگی وقوع جنایت در جریان است.
🔹
همچنین متهم زن پرونده که درحال فرار و خروج از کشور…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/455404" target="_blank">📅 00:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455403">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9IbzrbNAJm3YDHhdWHUe7Y3BPbrYO4qn5ymbv18p1JBmY7q5kKQGLiwaNP8qtpIBwuMP8N1xjWbXibN6lf-wYj_Jrm8ShiceF4iz79hP-Tyr0sG-lDu8piUhi90Y834H_gZJbYbC_jrArU-0rWRtjho5RxMiSpHjdsehMRDaFJFYn-hXoatcdyZ_nUUGobID32mqHUrzvgKOoVyzCbZzmukm8OxSwoQNCBXnRQDx6ka7-Yz4OABt3JqntXZjP95vpGMf0BLZ28FC_nooQPhsohIvQQACq0-sXE-cOwnjSI8fFrkAtJDiqvuUNjjn8ARIwsselwQkrIx-26_Ts69hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: جهان آمریکا را به خاطر انسداد تنگۀ هرمز مؤاخذه کند
🔹
وزیر امور خارجه در گفت‌وگوی تلفنی با همتای آلمانی: ناامنی تحمیل شده بر تنگۀ هرمز منحصرا ناشی از تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران است و جهان باید هیأت حاکمۀ آمریکا را به‌خاطر پیامدهای امنیتی و اقتصادی مترتب بر انسداد تنگۀ هرمز مؤاخذه کند.
🔹
امن‌ شدن تنگه هرمز مستلزم توقف اقدامات تجاوزکارانه و مداخلات غیرقانونی آمریکا از جمله محاصرۀ دریایی و دیگر نقض‌های تعهدات آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455403" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455402">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280903eb5d.mp4?token=IuqGMITqxod-1ZeYs72kAyUO9AIbmF0w3-N38lp3bdvX97gCp-J789XJ-7rGA7Hn7vwdXdVCywa5F2kFs2bXrW7EvNTv4V8JxYsr8LUzrAXfqD-l0N71UgfLOQPwzlEx2IfmvjSu1wlvnVYMRRvwuowqnHBMhz1ItUNFzgzeJ7frgZDpsqwBV_Wd0GgePYArJStWtOrs2Qr5hPXTGRkEFpfh82f1U5yTv7HbFE9QPGq7hFl1qM8iawe7dcSkgfjl_IxD99zeGeIjXQXRQDx7StT39xsubMBA6w6iezNtMKTFgqnvkipfFe0FOkuHHNVOE0m80Qtv_xXtQuVkYClK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280903eb5d.mp4?token=IuqGMITqxod-1ZeYs72kAyUO9AIbmF0w3-N38lp3bdvX97gCp-J789XJ-7rGA7Hn7vwdXdVCywa5F2kFs2bXrW7EvNTv4V8JxYsr8LUzrAXfqD-l0N71UgfLOQPwzlEx2IfmvjSu1wlvnVYMRRvwuowqnHBMhz1ItUNFzgzeJ7frgZDpsqwBV_Wd0GgePYArJStWtOrs2Qr5hPXTGRkEFpfh82f1U5yTv7HbFE9QPGq7hFl1qM8iawe7dcSkgfjl_IxD99zeGeIjXQXRQDx7StT39xsubMBA6w6iezNtMKTFgqnvkipfFe0FOkuHHNVOE0m80Qtv_xXtQuVkYClK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهدای میناب در محفل عزای حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455402" target="_blank">📅 23:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455401">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHepa_Q2_gZCL5UhRcceplOq7vETDbwnQkZCcbHm5kTwUG14XS9HgIzNeSp6a2l9nFP5776co0ZezmbRFBqPR7F2jg1s04Bk4J07YI9fWpKXovxvj0OeHQgfdakygHGGPbgdz4ydIstadmohriP5oIcYeQJ65hMDcEgnERx65r_WiaiOPp_1b16199W-wD_K0lmkre2faQWTLz0u3wLCUxqkzCntJP8R3eUb6Mii-FmfvYGNedo26ZpexZkMzZ4bY_GRmWsRuHygzBOaOC4Z5ZupLgFEBZEdrRUldCvaTaQ3ar0Bkh5xmOFdgeiI8subTVZm4Xri0zOVuwBN4BICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادر بر تن متهم؛ احترام به حجاب یا اهانت به چادری‌ها؟
🔹
انتشار تصویر متهم زن در پروندۀ قتل حمیدرضا رجب‌زاده با پوشش چادر، بحث دربارۀ پوشش بازداشت‌شدگان را دوباره بر سر زبان‌ها انداخته است.
🔹
استفاده از چادر توسط متهمان را در گذشته هم در پرونده‌های مختلفی شاهد بوده‌ایم.
🔹
یکی از آن‌ها، دختر قمه‌کش شوشتری بود که با موهای باز مشکی‌رنگ در میان اغتشاشگران قمه می‌چرخاند اما بعد از دستگیری با پوشش چادر رنگی  در صفحۀ تلویزیون حاضر شد.
🔹
یا شبنم نعمت‌زاده دختر وزیر پیشین که مانتویی بود پس‌از محکومیت به فساد مالی، در دادگاه‌ها  طوری چادر به ‌سر کرد که فقط بینی‌اش معلوم بود!
🔹
پلیس به فارس گفته ما الزامی برای چادر سرکردن افراد نداریم اما از آن‌جایی که متهم زن باید حجاب شرعی داشته باشد در این پرونده که متهم پوشش نامناسبی داشت مجبور به استفاده از پوششی شدیم که برای این مواقع پیش‌بینی شده و آن هم چادر بود.
🔹
کارشناسان می‌گویند که باید برای پوشش متهمان زن تدبیری ویژه اندیشید؛ اختصاص چادر برای متهمان بدپوشش، از یک سو بی‌احترامی به زنان محجبه بوده و از سوی دیگر شائبۀ مجرم‌بودن زنان چادری را اشاعه می دهد.
🔹
برخی کارشناسان هم می‌گویند باید پوششی دیگر همچون مانتوی ساده و بلند را در ورودی مقرهای انتظامی و امنیتی قرار داد تا متهمان زن درصورت نامناسب بودن وضعیت از آن استفاده کنند که خرید و اختصاص این نوع پوشش نیازمند تغییر قوانین و تخصیص بودجه ازسوی دولت یا وزارت کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455401" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455400">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
حماسه خون‌خواهی و میدان‌داری کاشمری‌ها در شب ۱۶۳
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455400" target="_blank">📅 23:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455399">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4fd355.mp4?token=CH2pjvxM2qUtjtD0eE3i8cWofwS5rLjX8rfRMxPyvAwC9rCkiVTyughNRApsK5b_2_k5Qwlo47v-MoC5g9HkkUxIAeUzgugcacWU8iv3pwQclKlGzahnVH7ykbuC05G71Mm9Vush8G_vHj8keiZ9486RuiwCqNa6jMS-QnFToSO5yupo4PQQwyoGN5T_uMcCQtKSzWtoXvIkcN5DE3wJmZflef2QlAtku11LnHAV_kU4KMjie_XBBpzVnMFUZam-szLiD6gTStvKiszmPJJ07uXXZxLTZcZ1mSAuBtJlTdL_ikHjbeM6W2lFEv2xnEate3S1NjCmMLAAah3rXHnmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4fd355.mp4?token=CH2pjvxM2qUtjtD0eE3i8cWofwS5rLjX8rfRMxPyvAwC9rCkiVTyughNRApsK5b_2_k5Qwlo47v-MoC5g9HkkUxIAeUzgugcacWU8iv3pwQclKlGzahnVH7ykbuC05G71Mm9Vush8G_vHj8keiZ9486RuiwCqNa6jMS-QnFToSO5yupo4PQQwyoGN5T_uMcCQtKSzWtoXvIkcN5DE3wJmZflef2QlAtku11LnHAV_kU4KMjie_XBBpzVnMFUZam-szLiD6gTStvKiszmPJJ07uXXZxLTZcZ1mSAuBtJlTdL_ikHjbeM6W2lFEv2xnEate3S1NjCmMLAAah3rXHnmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی رهبر شهید بر دستان بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455399" target="_blank">📅 23:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455398">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d79a4d93.mp4?token=EReY_QTf8g9FC0b5gE9rdt0qugnP8YcuRsvRnUBvy9N8nQrS0vHv23U875N48iCz72LdEKrPltfzyFCBZX7hO4HJoNLiVlR0TJ7y_8Iw2AdiS4mU47VqhfkwIuVHGtXp_pkxqv1X-sG0GT59DJ_cqG98ZeseKjg4rzu5zsI_ZvAT0zjUCPwCpz8eNOU6onYrwWyyTEfOrPp0BGbuk4iXPlAgiD7QuwnT-W2UOqH8BEMBiImltqP6o11o739r9IBGRSYKBlVIEFbz30Nv2Ch3uyqwoBQIQwMawMrznEsz-majO0sHrjCpgEK2p9DCMJU0R7d6mlg3IydFsXFCkz_tZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d79a4d93.mp4?token=EReY_QTf8g9FC0b5gE9rdt0qugnP8YcuRsvRnUBvy9N8nQrS0vHv23U875N48iCz72LdEKrPltfzyFCBZX7hO4HJoNLiVlR0TJ7y_8Iw2AdiS4mU47VqhfkwIuVHGtXp_pkxqv1X-sG0GT59DJ_cqG98ZeseKjg4rzu5zsI_ZvAT0zjUCPwCpz8eNOU6onYrwWyyTEfOrPp0BGbuk4iXPlAgiD7QuwnT-W2UOqH8BEMBiImltqP6o11o739r9IBGRSYKBlVIEFbz30Nv2Ch3uyqwoBQIQwMawMrznEsz-majO0sHrjCpgEK2p9DCMJU0R7d6mlg3IydFsXFCkz_tZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع موج ۱۶۳ در چهارمحال‌ و بختیاری با نوای نوحه‌ و سینه زنی همراه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455398" target="_blank">📅 23:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455397">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lplJ6F1x8n57_I0HK1mJtJadSqamTbvoke8Yn-lWmUZTDT42RsNu2iJXOgRht4L4lZy8U56B_ecemvoz96nY_gnur04qO-xY_piFLrtvB5uRQS2KXT4tcjtQ9HDQi0jMvj0BGj4ntSaBsP1JM0UnF5QbNmu6R7LYMD5b862E03cQVjWbSiTV3S-F0PUz6zztWxbPbWN3RXhRNDC5skMNvONFuKTC-ny3CDO2WVseWVzMQ5rgmmXqHP1Kj8gntZQF-CuK4j_Wqa98s5_GWWPNFm91_r1gOVBILJxo_-nQEw2oX8LXfs4hmp_h01oHtWpFuSVkIgme52-sbmJzEPCUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج: قصد داریم قرارداد قلعه‌نویی را برای جام ملت‌ها تمدید کنیم
⚽️
اعضای هیئت‌رئیسه اعتقاد داشتند که باید برای جام ملت‌ها جوانگرایی صورت بگیرید که این نظر خود قلعه‌نویی هم است.
⚽️
پاداش آقای قلعه‌نویی به‌عنوان سرمربی تیم ملی ۷۰ میلیارد تومان بوده است.
⚽️
در فیفادی پیش‌رو ۳ بازی تدارکاتی انجام خواهیم داد؛ بازی با روسیه قطعی شد؛ ۲ تیم اروپایی و یک تیم از آسیا که در جام جهانی هم حضور داشتند حریفان تدارکاتی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455397" target="_blank">📅 23:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455396">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4cf20f78.mp4?token=C1eWvLuRniDee2ii5tRbhlISlDhljWNvsYYUZPLOjDAznryNRgiZZxZOzYZUp0e_8j8-4SpVfki_WxYvpG-iaVkSzJR8KZTyMxWMXjlsGQlr1eSSEFciUsYi6Mar2Z_qLs7DDf9nHeEBlCBk58NemPaBFnmtJNTizoKSVuBnbWO5EyF9AeVfhRlB8WmvQbkDM2vAnq04odSbmpmS4YuoW-JSVC4O8jo_OvbkeYmEMV0ONpuEvPT-1g3rLwQog60Hi_dlZAx1BSdnmCdMOOtgAupwFwPWr1HcIz83XBcog2A6uFrPUrEDTFtwfIfpWOlQU6Z11tevAcy3lLADG5TdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4cf20f78.mp4?token=C1eWvLuRniDee2ii5tRbhlISlDhljWNvsYYUZPLOjDAznryNRgiZZxZOzYZUp0e_8j8-4SpVfki_WxYvpG-iaVkSzJR8KZTyMxWMXjlsGQlr1eSSEFciUsYi6Mar2Z_qLs7DDf9nHeEBlCBk58NemPaBFnmtJNTizoKSVuBnbWO5EyF9AeVfhRlB8WmvQbkDM2vAnq04odSbmpmS4YuoW-JSVC4O8jo_OvbkeYmEMV0ONpuEvPT-1g3rLwQog60Hi_dlZAx1BSdnmCdMOOtgAupwFwPWr1HcIz83XBcog2A6uFrPUrEDTFtwfIfpWOlQU6Z11tevAcy3lLADG5TdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۳ شب پایداری گنابادی ها در حمایت از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455396" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455395">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8836ef1e8e.mp4?token=u0GX4a3GNCeGGq28XXbolKSENuPkHmQ5plFxQcDA_kfRXlUoE_YvweXE5pOTeH450hJBrneaGE9C0o930NnoTvgr8vdbCBI1EAQthxXLD8OmDWQJunpCsuzQlWEx8oCpZJu91sehr9oLhXwdqJOyAY9aG53_fhGriVl5OrBq9rMd_NJ_Nv0u5CQeDpC7huIvfhRs4veyj4Nfq-kJVxwnXYb8lzDyI5lBbZK7TR68za_J93xYwaZbZ1mPONP0CLVAD9yb2oCa54uSh9NWPYnplqnToecceh-LWCd7QpyE6l2Al4tRYwr_n-yytfle6Xqgqj05cqyQXKtyC_neMWWe1U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8836ef1e8e.mp4?token=u0GX4a3GNCeGGq28XXbolKSENuPkHmQ5plFxQcDA_kfRXlUoE_YvweXE5pOTeH450hJBrneaGE9C0o930NnoTvgr8vdbCBI1EAQthxXLD8OmDWQJunpCsuzQlWEx8oCpZJu91sehr9oLhXwdqJOyAY9aG53_fhGriVl5OrBq9rMd_NJ_Nv0u5CQeDpC7huIvfhRs4veyj4Nfq-kJVxwnXYb8lzDyI5lBbZK7TR68za_J93xYwaZbZ1mPONP0CLVAD9yb2oCa54uSh9NWPYnplqnToecceh-LWCd7QpyE6l2Al4tRYwr_n-yytfle6Xqgqj05cqyQXKtyC_neMWWe1U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت گرگانی‌ها با ولایت و انقلاب در ۱۶۳ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455395" target="_blank">📅 23:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455394">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3156abfe8c.mp4?token=qmuNiDvxDn6l5WlOLdf8gpFTDdooR1ZmyQld-49aZbFEuTuMZPTF-lxxBGo34EgCADDXB016WyJ3rPDHXhDSyFQkxf3pYyqZlAQ3TtgEOKhhRXQ996P1Pomg9WAc13B6iqxLNuNP5Q-cFWThhMxlFD8AqxIXKzI2ZIOzAw9-Nla0P8rwtEevQuoB5DZj34WYEuXyyPyNo3NP2u8FOGd1rv4lj0XRHNTnWKWugXIA7pgcu6BeWyHDzYfihLBe6tiyFJCCVxTZVnwRr6ZhEoZ5X0td71oQ2jdV89aUGP6NDUzHZnIsjgd8ODi7nclhxQHlhdJD54ci35V1-Rn0w2rr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3156abfe8c.mp4?token=qmuNiDvxDn6l5WlOLdf8gpFTDdooR1ZmyQld-49aZbFEuTuMZPTF-lxxBGo34EgCADDXB016WyJ3rPDHXhDSyFQkxf3pYyqZlAQ3TtgEOKhhRXQ996P1Pomg9WAc13B6iqxLNuNP5Q-cFWThhMxlFD8AqxIXKzI2ZIOzAw9-Nla0P8rwtEevQuoB5DZj34WYEuXyyPyNo3NP2u8FOGd1rv4lj0XRHNTnWKWugXIA7pgcu6BeWyHDzYfihLBe6tiyFJCCVxTZVnwRr6ZhEoZ5X0td71oQ2jdV89aUGP6NDUzHZnIsjgd8ODi7nclhxQHlhdJD54ci35V1-Rn0w2rr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گردهمایی بزرگ اندیشمندان شیعه و اهل سنت در حرم امام رضا(ع) در آستانه رحلت پیامبر اکرم(ص)
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455394" target="_blank">📅 22:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455393">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آژیر هشدار آزمایشی فردا در جاسک هرمزگان به صدا در می‌آید
🔹
به منظور آمادگی و ارزیابی عملکرد تجهیزات، تست آژیر هشدار توسط نیروهای نظامی از ساعت ۱۰ صبح سه‌شنبه در سطح شهر جاسک انجام می‌شود.
🔹
این اقدام صرفاً یک مانور و تست فنی است و هیچ ارتباطی با وقوع حادثه یا شرایط اضطراری ندارد و شهروندان نگرانی نداشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455393" target="_blank">📅 22:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455392">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c800cb1309.mp4?token=Z1IgtI9tTo3tF5uz3scUVcA3rwj03MlsLtjwcVmp1pfBTIzNc63msbOV4sHc4UgqZOA_RCS9RZqFkCC_AruOrDY7sROwjXiR2pC8lP6_SuSQtXYTVhGu5TNSkdWcfCYRAMA-S0TtgUXqP4kbOgt7d_MHDw-anyf4XD6-r9vbSpvGg5lak3WikqOqIcGPx9Fsl1tqrRSS0KOfZdQD-ak94deANaROq4gq457IVjZMivc-XF2MkO6xV06UxT8coIYAFN4nTyZodP10GOaQE5x540xdM2heQz5y_8xb1DcRwVJYH0OuIdaPF1h3cvQus13CUsSQbdDhnHuKZUlcIvSwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c800cb1309.mp4?token=Z1IgtI9tTo3tF5uz3scUVcA3rwj03MlsLtjwcVmp1pfBTIzNc63msbOV4sHc4UgqZOA_RCS9RZqFkCC_AruOrDY7sROwjXiR2pC8lP6_SuSQtXYTVhGu5TNSkdWcfCYRAMA-S0TtgUXqP4kbOgt7d_MHDw-anyf4XD6-r9vbSpvGg5lak3WikqOqIcGPx9Fsl1tqrRSS0KOfZdQD-ak94deANaROq4gq457IVjZMivc-XF2MkO6xV06UxT8coIYAFN4nTyZodP10GOaQE5x540xdM2heQz5y_8xb1DcRwVJYH0OuIdaPF1h3cvQus13CUsSQbdDhnHuKZUlcIvSwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنوانسیونی که زبانِ رضا پهلوی را دراز کرد
🔹
همزمان با بحث‌ها درباره کنوانسیون رژیم حقوقی دریای خزر و در حالی که دولت مسئولیت نهایی آن را به مجلس واگذار کرده، رضا پهلوی نیز با فرصت‌طلبی خود را مدافع تمامیت ارضی ایران نشان داده است؛ موضعی که با سابقه خاندان پهلوی در حاتم‌بخشی بحرین به عنوان بخشی از خاک ایران و مواضع اخیر جریان سلطنت‌طلب در تضاد است.
🔹
رضا پهلوی که در اواخر اردیبهشت امسال، برای نام بردن از دریای خزر از واژه «بحر خزر» استفاده کرده بود، امروز شهامت پیدا کرده و با اقدامات نمایشی و نوعی ملی‌گرایی قلابی، نام «دریای کاسپین» را به زبان آورده و به خود اجازه می‌دهد تا درباره تمامیت ارضی ایران و پیامدهای حقوقی این کنوانسیون سخن بگوید.
🔹
نکته جالب توجه اما تناقض و رویکرد دوگانه پهلوی‌چی‌ها در قبال منافع ملی و تمامیت ارضی ایران است. این جریان در طول ماه‌های گذشته دائماً ادعا می‌کردند که ایران هیچ حق و حقوقی برای مدیریت تنگه هرمز ندارد.
🔹
به‌عنوان مثال مدیر تیم رسانه‌ای رضا پهلوی و دبیر خبر سابق شبکه سلطنت‌طلب منوتو، بستن یا کنترل تنگه هرمز توسط ایران را ناقض قوانین بین‌المللی دانسته و آن را نفی کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455392" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455391">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108142470c.mp4?token=Mqqg-2Gz8i4j87fIbtpanp6egLibv8ZPkm31QPA1x5hto969bGcP6bU1AnjV9ixvPmKOQx2KE4ALtNWqJQl9CLD1rBwoCiHdvCsTS6T3cghgmC8CxIUoPmpqZ46Pw-aIxxMx_uhvZzCcira6fSmRVE-MuBZHIeVIlMIg97RYtn8LpbgvCCuewkg6kmXJZ5YwAZQJdFMvCQrYDYRJMwDlPrAk6cCr_rxiqkGIU-SvLn0JOYFSv9txUE8xenGWUfCjrAdID-SIddCftulpMJOIfqBkVGroRk1b-tL3t2M18wkiV9GjQ_Su4YPP6Up6YwnpZog7Vor_lpr7Bmg5XevjxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108142470c.mp4?token=Mqqg-2Gz8i4j87fIbtpanp6egLibv8ZPkm31QPA1x5hto969bGcP6bU1AnjV9ixvPmKOQx2KE4ALtNWqJQl9CLD1rBwoCiHdvCsTS6T3cghgmC8CxIUoPmpqZ46Pw-aIxxMx_uhvZzCcira6fSmRVE-MuBZHIeVIlMIg97RYtn8LpbgvCCuewkg6kmXJZ5YwAZQJdFMvCQrYDYRJMwDlPrAk6cCr_rxiqkGIU-SvLn0JOYFSv9txUE8xenGWUfCjrAdID-SIddCftulpMJOIfqBkVGroRk1b-tL3t2M18wkiV9GjQ_Su4YPP6Up6YwnpZog7Vor_lpr7Bmg5XevjxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار تابستانی با رعدوبرق در آسمان مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455391" target="_blank">📅 22:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455390">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bd9832e9.mp4?token=KyWQR0vk9xnbPQJS_Bu9vh1-7aqVdVFHH9OZv574MjeAu5pKCwxS1ni2sjadANZLz2lZnYr1yT2_Fu58TicYCKbNg9Wn9JUI75FzrS44v-qzlbXb7twbM2d-Ky6iggxFnQrtCdHlWbWcNRIlCDlnmu_HZhArVk0nqUf-xpD1Pty1UlKZU2C8gXyVl4V3i3uhRtWYI63hU9lPqzl5x8nDm7nf4oQ99KyiHW08J4e3YA_7x-UvLxvWD7p_cGhsojg33VRHERfDsrCO8ZBcjR5sREjex1y4VPBDCgCeYUKMGOsAM0pKSssfEyFPFTtPU2kXZj2ogohh5XOkvqsj343wdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bd9832e9.mp4?token=KyWQR0vk9xnbPQJS_Bu9vh1-7aqVdVFHH9OZv574MjeAu5pKCwxS1ni2sjadANZLz2lZnYr1yT2_Fu58TicYCKbNg9Wn9JUI75FzrS44v-qzlbXb7twbM2d-Ky6iggxFnQrtCdHlWbWcNRIlCDlnmu_HZhArVk0nqUf-xpD1Pty1UlKZU2C8gXyVl4V3i3uhRtWYI63hU9lPqzl5x8nDm7nf4oQ99KyiHW08J4e3YA_7x-UvLxvWD7p_cGhsojg33VRHERfDsrCO8ZBcjR5sREjex1y4VPBDCgCeYUKMGOsAM0pKSssfEyFPFTtPU2kXZj2ogohh5XOkvqsj343wdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی سپاهان از لباس خود در فصل جدید با الهام از نمادهای ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455390" target="_blank">📅 22:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455389">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs6I-kTfPHR0AliFsOtJDp-Lke8lAmpixlRCO-tQE91c5s_Q1ge7-YqXzTrXA0hJ71AhZHNB44SuQZx-rHd9GGIRtk99wWO5cSUKDG0Timr5klwqA-oNt2FHMIGve9KMhIe9gJZKZ4PxF4uxsw_gZi3sjW_Lln-Y7HKWgimo8_Q7xpogISODOmLde8LAyYDcVfhA8NOsIyFL0OBhZY99wkiRNGVuHfAvNxXOG1y_6vPIy_QvdBbBUoWGEgjUhkzGom_diJFfvgHzvwXaphqEKTGL_W8nL0_yjeFTxkhEbLR3-kt9BKDW7QcSvQl6ddC2zAIAaqypuVlCytdiOHYxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
🔹
اسکات ریتر، نظامی بازنشستۀ آمریکایی: ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455389" target="_blank">📅 22:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455388">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f2acbb8c.mp4?token=fl4-HJtCLHmZTY0Is4oSBUdJMhXQJkwInksHNqbqfh1g97HMlpX7uPjaT_lGnNrbeyWmehTwLJq3l0-uuLVjf0YWxgM6mHfRwEMqhENHRT-swV-TddFrNnhz4sn6bLpzzYc51CRjo4XWmzlYivv8sS0woAyocGj0RB6lBjR71cy0F2tg7BxF2RdX9soQ6ohmCFri-ejIugwPDtMav4hdVXB1125Xf9DRUecNFUQ_3YmiLvFkjPe98W9RaPOlc3RILOZ2vt0bjeZc9mc3s2suOUbqJpI4F6uq-UnsoOy70C39wltbAm-KXziCnFrOVlq22bSoYFBdVvK8WnMZFCppag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f2acbb8c.mp4?token=fl4-HJtCLHmZTY0Is4oSBUdJMhXQJkwInksHNqbqfh1g97HMlpX7uPjaT_lGnNrbeyWmehTwLJq3l0-uuLVjf0YWxgM6mHfRwEMqhENHRT-swV-TddFrNnhz4sn6bLpzzYc51CRjo4XWmzlYivv8sS0woAyocGj0RB6lBjR71cy0F2tg7BxF2RdX9soQ6ohmCFri-ejIugwPDtMav4hdVXB1125Xf9DRUecNFUQ_3YmiLvFkjPe98W9RaPOlc3RILOZ2vt0bjeZc9mc3s2suOUbqJpI4F6uq-UnsoOy70C39wltbAm-KXziCnFrOVlq22bSoYFBdVvK8WnMZFCppag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع انفجار در یک مخزن سوخت در لیبی
🔹
منابع خبری گزارش دادند چندین انفجار در یک مخزن سوخت در پالایشگاه الزاویه در لیبی رخ داده است؛ هنوز علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455388" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaOVLOj5U3W3Kn8IgmzJ4IELMW_iQyeHLiAQR7bSHWR9tf_BzR_Yvbr2DIA7bX05Y0JmeBpBzLIrR2qs3mU3pNXueMXhrlHjq4EXk1QZK4yBab-EhWe6HjL_n4rwWl2CE1c0bJpp4PdK_oPzG734ytIJu-skrF08HdF5Z_HaJRHiDjRMtmhhvbh2r-mk9sTVUBfHtfbpb7Kw0L8xrtH5K_g1WzlRsOmKHqfPNX_qCnhBdnslQlY7GKfyAo99c8CGCbzctQKd-hr_Fhrg3JOi34A-ICQElanh32SfarniN0Pa7NZDE9nuNWUgFrDSh-vkO0UaIe7deWgj-Y2U70afSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بدهی ۲۲ میلیاردی، برق از سر کشتی پراند
🔹
پیگیری فارس از توانیر مشخص کرد، علت قطعی برق مجموعۀ متعلق به فدراسیون کشتی بدهی ۲۲ میلیارد تومانی به صنعت برق بوده.
🔹
البته فدراسیون کشتی گفته این بدهی برای به ورزشگاه آزادی است.
🔹
طبق آنچه وزارت نیرو می‌گوید، هفتۀ…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455387" target="_blank">📅 21:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455386">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIQU2SCBmEjR1AmjhJ7L4NqawwgYtf4JJD2IHo-UfJKC3IEiFat4SWROEV2A14ndO2d1dvxSZHJjf1bDHepTD1uqOAp4X6-W2gk__bOjdwxXb5Pb7PJk1DhqPytyLH1kMeP8G1EY7fQu5LJ8tf1pIdLErexxONTPRoIxWC4XNs8F1-1VuZ4RGPoqEIGCHud2Eyb8NBJ9sBtcrTUSiRIPdF6DdEZIsjBIHxwHaT61ZpwqzD3wac9wGWBi9-5qpAm-LcTbplbtyWL2ZTHD76cOZr0XDKXhM6LXcCDQG-OUxrO3GTI6JtfNiI9esUw7A3-RtU45T7FXtG4Pho_Sy6aF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
🔹
اسکات ریتر، نظامی بازنشستۀ آمریکایی: ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل ایران با کمبود سلاح‌های دورایستا مواجه است.
🔹
آمریکا عملاً در مسیر عقب‌نشینی تدریجی از غرب آسیا قرار گرفته؛ هرچند ترامپ احتمالاً حاضر نخواهد بود این روند را به‌صورت علنی با عنوان «عقب‌نشینی آمریکا» اعلام کند.
🔹
حتی ممکن است برخی دولت‌های منطقه نیز دیگر تمایل چندانی به تداوم همان ترتیبات امنیتی سابق نداشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455386" target="_blank">📅 21:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455385">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f39aca476.mp4?token=pVkuqeK3h6dKMr4-jjJTI8_90HL8LAH-lcPndcyNFSwy3T8TJ1Uk4NomUokuv1aEroBzJeCL8pV2UI-Qv6UZui8dbi-a6X7yoNFUBoU8h9HUHehUppn9272hcrnQOL1Efy8AMCeYI32ogGTFRNlBzf0r220TPynWd11Im2UTw1XJMHWUjMAfsGvtD-nt17kHDitdlTm0K0tPljtbHcSFSTRuvwhSpxHsIOIwnkRvegk4f1Ti8wvhzTrOsjuQnQ23fv4mpqa3va7_KjmiUaF9Csdge4mdJIMDZGsLoloeOx0c83FkIetB9S6V8lvySZoRphjmqNQwOFPakzYvT6U-yE8sxV7VIm668hMz0WM7lQrMSJJiHc4j6SLsEkT5oJwvMqtRkLqqe2ZPGcgwQvkr9_Giym16wav2kRf7YIZ4CJ6PMp-nnYkqCF-fVi2bjivA4mSqBTivGtdfRRwu8j9kqdjSZRDy0QN5xgOBLeBQp_QmvgmOXbyIIHw7fJc1XGUyBKMSuueX0finA0dtrCCY11fVeebFHVueJcHByv47hCRIBkELQTWx8MZUkwzbDZo_Tq-4a4fTn2tU7pa6Su8EHEDE_eTOkNBxUWR_RcsajCn7kiMT5K9IHChhaxwzR7UvIVi2IwD5l2XI6pyhC46PyKCKvxLhg117HPDn16r8Pxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f39aca476.mp4?token=pVkuqeK3h6dKMr4-jjJTI8_90HL8LAH-lcPndcyNFSwy3T8TJ1Uk4NomUokuv1aEroBzJeCL8pV2UI-Qv6UZui8dbi-a6X7yoNFUBoU8h9HUHehUppn9272hcrnQOL1Efy8AMCeYI32ogGTFRNlBzf0r220TPynWd11Im2UTw1XJMHWUjMAfsGvtD-nt17kHDitdlTm0K0tPljtbHcSFSTRuvwhSpxHsIOIwnkRvegk4f1Ti8wvhzTrOsjuQnQ23fv4mpqa3va7_KjmiUaF9Csdge4mdJIMDZGsLoloeOx0c83FkIetB9S6V8lvySZoRphjmqNQwOFPakzYvT6U-yE8sxV7VIm668hMz0WM7lQrMSJJiHc4j6SLsEkT5oJwvMqtRkLqqe2ZPGcgwQvkr9_Giym16wav2kRf7YIZ4CJ6PMp-nnYkqCF-fVi2bjivA4mSqBTivGtdfRRwu8j9kqdjSZRDy0QN5xgOBLeBQp_QmvgmOXbyIIHw7fJc1XGUyBKMSuueX0finA0dtrCCY11fVeebFHVueJcHByv47hCRIBkELQTWx8MZUkwzbDZo_Tq-4a4fTn2tU7pa6Su8EHEDE_eTOkNBxUWR_RcsajCn7kiMT5K9IHChhaxwzR7UvIVi2IwD5l2XI6pyhC46PyKCKvxLhg117HPDn16r8Pxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب دربارۀ  هدیۀ مرحوم فرشچیان: هر وقت این تابلو را نگاه کردم، گریه کردم
🔹
استاد فرشچیان: از امام حسین(ع) حفظ تمامیت ایران از خلیج فارس تا شمال و از شرق تا غرب و سلامتی هموطنانم را می‌خواهم
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455385" target="_blank">📅 21:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455384">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/232f89712b.mp4?token=GUupvkEqAngilMCRlGSd6Dn9u8DWtVdV74oSnS2VlGsp9iq7aG6rqa2_Ru_qRba-GZNpPk4FLdvpvvcgwdYCYanPPLWbbdTMjHIzluIs9YtzTxD2oVyyYygU96bgUg7CKd9zWrKe3rREXeFe5NyOymTDZ2Z941mAgnPRQcVzp8fs9saaWoLcPdyF4wppeCwwK7r2yKExKlQJgIvXBWn_jjxvyyfZrX69Frtz6-p0byDSID1maoG5l1gRg3lJ-oXPwzW8I-Xs7GETAcYh1n6vwQxkt05LsyOQL9Tyg970MBoHujl4obRsOXjVItSS6hXqPtfoOuvWnzdXOz_im4OTD4C8hjTaw_3a9rFBCGOmBXkw3WGx-GzR03oNMYgPc7BtS7bh6tNVtiapgFDv2kEMMjsUxuIhqgZ_MeQ7HP5c56sp41ntZrfFykhd_IruUIIknoVzYYX-mQuCFV3HE_SvmtnMTJPz7KnS3sYXyVQmhtqBkcVVjKOoWOFst2WTWDhJIPNoNEKh5uDopRdRzUm7h0Yev_Fh9tCfb47jjahO17Q8zBHql1AyduR2WgnrMdVlABKwOSxbKOA6tKKbtVv-obst7DR1uLzuUNFWp_5Rk6joya1ILoTNc-7-WygrEHDFNm4oQ1tYTh_Pb-6Qg6Nf6amLnNS50eK8B65dImCAnnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/232f89712b.mp4?token=GUupvkEqAngilMCRlGSd6Dn9u8DWtVdV74oSnS2VlGsp9iq7aG6rqa2_Ru_qRba-GZNpPk4FLdvpvvcgwdYCYanPPLWbbdTMjHIzluIs9YtzTxD2oVyyYygU96bgUg7CKd9zWrKe3rREXeFe5NyOymTDZ2Z941mAgnPRQcVzp8fs9saaWoLcPdyF4wppeCwwK7r2yKExKlQJgIvXBWn_jjxvyyfZrX69Frtz6-p0byDSID1maoG5l1gRg3lJ-oXPwzW8I-Xs7GETAcYh1n6vwQxkt05LsyOQL9Tyg970MBoHujl4obRsOXjVItSS6hXqPtfoOuvWnzdXOz_im4OTD4C8hjTaw_3a9rFBCGOmBXkw3WGx-GzR03oNMYgPc7BtS7bh6tNVtiapgFDv2kEMMjsUxuIhqgZ_MeQ7HP5c56sp41ntZrfFykhd_IruUIIknoVzYYX-mQuCFV3HE_SvmtnMTJPz7KnS3sYXyVQmhtqBkcVVjKOoWOFst2WTWDhJIPNoNEKh5uDopRdRzUm7h0Yev_Fh9tCfb47jjahO17Q8zBHql1AyduR2WgnrMdVlABKwOSxbKOA6tKKbtVv-obst7DR1uLzuUNFWp_5Rk6joya1ILoTNc-7-WygrEHDFNm4oQ1tYTh_Pb-6Qg6Nf6amLnNS50eK8B65dImCAnnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید دههٔ‌ هفتادی که الگوی مدافعان حرم ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455384" target="_blank">📅 21:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455383">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b27a8c503.mp4?token=AkfdEfyNX1u_4mHKg2WfeUo7B5n44WD-FVXXeKfUrkYAml_Szi8Eom5wNHg6TB5dOv1oFl5OZ9ZOOR2usMZf1Xo25X06xko-rn-Yp4Xzj-kRmountzKYqqz5g5Xp0hCnJMydjR5jmA4CxlW6Zo6lRWPijdNbY8J3HyTebtdMWgBC5Ts0u5ferEaBKh20tOnUOVr0LVjjiZ02lmFDZXauIFIwa4OBIIKz_7H1dr4Zra1xIjlxdstNLsiWU0O12oSk7-ZD0MRCgnl75nhjZyKsoCshFxUW08F92gv_K1xN1EWADqiHrQ5e0WLdH5JBWYThiccQWpjVY6uMhC7aJ9_LCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b27a8c503.mp4?token=AkfdEfyNX1u_4mHKg2WfeUo7B5n44WD-FVXXeKfUrkYAml_Szi8Eom5wNHg6TB5dOv1oFl5OZ9ZOOR2usMZf1Xo25X06xko-rn-Yp4Xzj-kRmountzKYqqz5g5Xp0hCnJMydjR5jmA4CxlW6Zo6lRWPijdNbY8J3HyTebtdMWgBC5Ts0u5ferEaBKh20tOnUOVr0LVjjiZ02lmFDZXauIFIwa4OBIIKz_7H1dr4Zra1xIjlxdstNLsiWU0O12oSk7-ZD0MRCgnl75nhjZyKsoCshFxUW08F92gv_K1xN1EWADqiHrQ5e0WLdH5JBWYThiccQWpjVY6uMhC7aJ9_LCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: اگر مردم در عمل ببینند ما صادق و صحیح‌العمل هستیم، تحملشان بیشتر می‌شود؛ حتی اگر مشکلشان حل نشود.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455383" target="_blank">📅 21:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455382">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b060ea1bb5.mp4?token=ZiOT_1vPtuSyLorrPQ5C8IxxSgrEcISTeArp-unzPu3nu3bv6Rihw-jBE7MxTXNRGtyDmU7OuHAslnUp04-Cmm-8eK08DCxAnSwnLuMrFBPnqPKNGegYIdyVav19eK3zXI5IcpaxuAN2W_r-7iQJQRtrOfDsssjLLSmy13r_dEbRLtlDi_O_GWOABObGyxxRu_IzD9At1wFEKmAYZNPGiEy02B6IrLiGxDlMuwRrGFeEjGtKlFy-aT3MnQwe7nJ3d-dpkEtWnANLbJTBQJ4Q899zetV4VQDeJ859VqFG-YZDRcVuccE_sRwwYXspfLMcFr8jhrx-iF9NOQy6FP_WroCzjScfrsUdjQO7EvYlLqPAsNzyeA3-26IkjMnhe78BQ2L8YNxQV8MuYR18BBKFio3nXZ8wDb12fy5EDRdLY2Tj3RMSz0JenzQqJ6raWzyzib5vQs8ruwrMdHLye07aO0tM8ooSHaAWY3EFI7WmVCDI5p-Cc5QMFgqjIGh3o4uUunnZZjxeJPLHWAo5d_AtlaNLw06Ek_luD6yPfBCqJYNf_cHgAEksjUvpJsvwY_F70mMxYPEGSSdGuy0bFqErHSD0pBkKPxryEhO3Rxwz_wrB4dn-unIdczg3mY2HOe0FOoCNJbvirDs7Cp7JS5XZSBNRWdQTRosknf-I1Hoej70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b060ea1bb5.mp4?token=ZiOT_1vPtuSyLorrPQ5C8IxxSgrEcISTeArp-unzPu3nu3bv6Rihw-jBE7MxTXNRGtyDmU7OuHAslnUp04-Cmm-8eK08DCxAnSwnLuMrFBPnqPKNGegYIdyVav19eK3zXI5IcpaxuAN2W_r-7iQJQRtrOfDsssjLLSmy13r_dEbRLtlDi_O_GWOABObGyxxRu_IzD9At1wFEKmAYZNPGiEy02B6IrLiGxDlMuwRrGFeEjGtKlFy-aT3MnQwe7nJ3d-dpkEtWnANLbJTBQJ4Q899zetV4VQDeJ859VqFG-YZDRcVuccE_sRwwYXspfLMcFr8jhrx-iF9NOQy6FP_WroCzjScfrsUdjQO7EvYlLqPAsNzyeA3-26IkjMnhe78BQ2L8YNxQV8MuYR18BBKFio3nXZ8wDb12fy5EDRdLY2Tj3RMSz0JenzQqJ6raWzyzib5vQs8ruwrMdHLye07aO0tM8ooSHaAWY3EFI7WmVCDI5p-Cc5QMFgqjIGh3o4uUunnZZjxeJPLHWAo5d_AtlaNLw06Ek_luD6yPfBCqJYNf_cHgAEksjUvpJsvwY_F70mMxYPEGSSdGuy0bFqErHSD0pBkKPxryEhO3Rxwz_wrB4dn-unIdczg3mY2HOe0FOoCNJbvirDs7Cp7JS5XZSBNRWdQTRosknf-I1Hoej70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی مو‌سفیدان سیاست دور یک میز جمع می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455382" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455381">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b228c55ff.mp4?token=urGQ5WMjz1LLOJ075CKTTt-8WvgkATq3_Jx0pbnpfSSUGnbJxmgE3f3jkCKvfPGqNGISMnD8O0Fv_78B5yKHDuapiSJpXG5_44m-fObj9_5FXBkDigW1jc7xGmS97n5hohknbsljWmzNpYEFJ7ld1zGQsO__dj6FOeczORP0I77sUzvhL4sIYN_Qie-NXXDOS3HRvFej3Sh0gVduuiLxzRgEfDRcmXSE1Lm8CCnPBg3Tf3mtaMcraoIqYIgQAm-m4XkoqTeksyG6W-HafJbhman1vwlIvfgQRn97bWyVvTGv3qXNv98-EDk2_x_DglNFtezBz7t8wFtPAxdpFr9_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b228c55ff.mp4?token=urGQ5WMjz1LLOJ075CKTTt-8WvgkATq3_Jx0pbnpfSSUGnbJxmgE3f3jkCKvfPGqNGISMnD8O0Fv_78B5yKHDuapiSJpXG5_44m-fObj9_5FXBkDigW1jc7xGmS97n5hohknbsljWmzNpYEFJ7ld1zGQsO__dj6FOeczORP0I77sUzvhL4sIYN_Qie-NXXDOS3HRvFej3Sh0gVduuiLxzRgEfDRcmXSE1Lm8CCnPBg3Tf3mtaMcraoIqYIgQAm-m4XkoqTeksyG6W-HafJbhman1vwlIvfgQRn97bWyVvTGv3qXNv98-EDk2_x_DglNFtezBz7t8wFtPAxdpFr9_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: قیام عاشورا سند بنیادین مقاومت در برابر ظلم است
🔹
روز گذشته در آیین افتتاح «محرم و عاشورا در آینه اسناد وزارت امور خارجه» تأکید کردم که قیام حضرت اباعبدالله‌(ع) منشور عدالت‌طلبی و سند بنیادین مقاومت در برابر ظلم است.
🔹
در لایه‌های عمیق‌تر این مستندات، تجلی عزت‌طلبی تمدنی ایران در تقابل با نظام سلطه و قدرت‌های استعماری به چشم می‌خورد.
🔹
به عبارت دیگر این اسناد، تاریخ را از سطح تصمیم‌های رسمی به سطح تجربه انسانی نزدیک می‌کنند.
🔹
اطمینان دارم این نمایشگاه روزنه‌ای برای شناخت عمیق‌تر پیوند تاریخی ایرانیان با مکتب عاشورا و پاسداشت ارزش‌های اسلامی و کرامت انسانی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455381" target="_blank">📅 21:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455380">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZLB3PemLIgU2bSdjDc-8y70jzHPC8BtbH5HcaoVudKPSmbG8S_hEQXQeXEC0VhDNrJVtEhxbhvsLrPbHmR3nbvbyQYQSS5ZmuebCqL45OCVn50lPK-CYuPRsHHejv55rqxX4-0EZp4aMl-6mJSdt3UeiLYnyUu8cYTWliDDY6Lo31mSfDMpKHUZ7d8J4Xfrr6QCHY5YPISs8LIGQR-fljPdpXv5iWSbrnZWgd9bfISGEbPUXhgz-RQ7__1CzJEBog8eQPRd2UbK5xw5apTZbVfk8Okov1xE1ruzL2Y2KYqzEiELsH5pQjyPFaDn3JQBm36_lDqIxkw3jJcwwR1hrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#یادداشت
|
چرا محسن رضایی به شعام رفت؟
🔸
انتصاب محسن رضایی به‌عنوان نماینده رهبر انقلاب در شورای‌عالی امنیت ملی و سپس انتخاب او به‌عنوان دبیر این شورا از سوی رئیس‌جمهور، می‌تواند نشانه‌ای از توجه بیشتر به هماهنگی و تصمیم‌گیری امنیتی در شرایطی باشد که تعریف «امنیت ملی» دیگر به مرزهای میدان نظامی محدود نمی‌شود.
* شعام؛ جایی برای جمع کردن تکه‌های پازل امنیت
🔹
شورای‌عالی امنیت ملی یکی از مهم‌ترین نقاط اتصال بخش‌های مختلف
#حاکمیت
است و مسائل امنیتی کشور را از زوایای دفاعی، سیاسی، دیپلماسی، اقتصاد، اطلاعات و تحولات منطقه‌ای بررسی می‌کند.
🔸
قرار نیست هر دستگاه جداگانه درباره بخشی از امنیت کشور تصمیم بگیرد، بلکه باید میان این بخش‌ها هماهنگی ایجاد شود و تصویر مشترکی از منافع و تهدیدهای ملی شکل بگیرد.
🔹
تجربه جنگ اخیر نشان داد یک بحران امنیتی می‌تواند هم‌زمان ابعاد نظامی، اقتصادی، سیاسی، رسانه‌ای و اجتماعی پیدا کند. از این منظر، شعام صرفاً محل تصمیم‌گیری درباره «جنگ» نیست؛ بلکه باید برای مجموعه‌ای از تهدیدهای
#به‌هم‌پیوسته
، تصمیم‌های هماهنگ و قابل اجرا شکل دهد.
* چرا سرلشکر رضایی؟
🔸
در حکم رهبر انقلاب، «
#تجارب_ارزشمند
» و سابقه رضایی به‌عنوان یکی از «پیشگامان دوره پرافتخار هشت سال دفاع مقدس» برجسته شده است.
🔹
رضایی در سال‌های جنگ تحمیلی ۸ ساله در شرایطی تصمیم‌گیری می‌کرد که اطلاعات ناقص، زمان محدود و هزینه‌ها بسیار بالا بود. این تجربه، علاوه بر سابقه نظامی، تجربه تصمیم‌گیری در شرایط بحرانی و شناخت از منطق تهدید است.
🔸
حضور در فرماندهی سپاه و سپس فعالیت در
#سطوح_عالی
سیاست‌گذاری و مجمع تشخیص مصلحت نظام نیز او را با میدان و ساختار تصمیم‌گیری کلان کشور آشنا کرده است.
🔹
وظیفه دبیر شعام فرماندهی عملیات نظامی نیست، بلکه هماهنگ کردن دستگاه‌ها و تبدیل
#تصمیم‌های_کلان
به فرآیندهای قابل اجراست.
* امنیت امروز، فقط میدان نبرد نیست
🔸
تهدید می‌تواند هم‌زمان از مسیر نظامی، سایبری، اقتصادی، رسانه‌ای و سیاسی وارد شود. عملیات نظامی می‌تواند با جنگ روایت‌ها همراه شود، تحریم اقتصادی بخشی از فشار امنیتی باشد و تحولات منطقه‌ای بر
#معادلات_داخلی
اثر بگذارد.
🔹
در چنین محیطی، مدیر امنیتی باید بتواند میان حوزه‌ها ارتباط برقرار کند. از این زاویه، انتخاب رضایی را می‌توان با تجربه مواجهه با
#بحران‌های_پیچیده
و توان پیوند دادن میدان با سیاست‌گذاری مرتبط دانست.
* ترکیب دو انتصاب
🔸
رهبر انقلاب ابتدا محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند و پس از آن، رئیس‌جمهور او را به‌عنوان
#دبیر_شورا
برگزید.
🔹
نمایندگی رهبر انقلاب جایگاه او را در ساختار شورا مشخص می‌کند و حکم رئیس‌جمهور مسئولیت اجرایی دبیرخانه را به او می‌سپارد. کنار هم قرار گرفتن این دو می‌تواند نشانه‌ای از هم‌جهت شدن سطوح راهبری و اجرایی در مدیریت
#امنیت_ملی
باشد.
* انتخاب برای یک دوره متفاوت
🔸
شرایط امنیتی کشور پیچیده‌تر شده و مرز میان جنگ، سیاست، اقتصاد و رسانه درهم‌تنیده‌تر شده است. چنین شرایطی به تصمیم‌گیری سریع‌تر، هماهنگ‌تر و راهبردی‌تر نیاز دارد.
🔹
از این زاویه، سابقه
#دفاع_مقدس
رضایی، تجربه فرماندهی، حضور طولانی در سطوح عالی مدیریتی و شناخت او از سازوکارهای مختلف تصمیم‌گیری، بیش از آنکه مجموعه‌ای از عناوین در یک کارنامه باشد، مجموعه‌ای از تجربه‌هایی است که می‌تواند برای یک مأموریت مشخص به کار گرفته شود: هماهنگ کردن اجزای مختلف قدرت ملی در برابر تهدیدهایی که دیگر یک‌بعدی نیستند.
1️⃣
تجربه میدانی
2️⃣
نگاه راهبردی
3️⃣
قدرت هماهنگ‌کنندگی
4️⃣
نزدیک شدن سطوح راهبری و اجرا
🔸
انتصاب محسن رضایی در این چارچوب، تلاشی برای متناسب کردن مرکز تصمیم‌گیری امنیت ملی با شرایطی است که در آن، امنیت دیگر یک پرونده جدا از سایر مسائل کشور نیست؛ بلکه حاصل
#هماهنگی
همه آنهاست.
➕
متن کامل را
اینجا بخوانید
.
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455380" target="_blank">📅 21:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455379">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GptZoUte6uwkfj4wGIgEIg86_PjcEut2YLEZjHhjK_tNw0g8tNT8rSz1hT1Onj74Q5m1R8EjvjPrs3Vn7Wv3VYD-6LmuqlUbAKWo1W0GCgCHaMzMYVpVNMsp9vQbh7TDUGxVnEJ1cmFBGNVsG7YZ81ns1pnQ9G4_r4HWCCVjWiMrnNzBih_tWDnk9EqF4u9OZA5JGTR0v7aj2HfrUCOrIalwLsOnTyxgLDS9SEa15XOus9Q7JWYlGjKy27pq2l220P0LskEeRyGaLds1k9fEW3tt3ByTJzgZEUNUQrP6ma0qXBIgj0CiXAKOngo0pqUYj0lnIWTvaSb1SE8DUSIoXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسوایی اخلاقی رئیس فیفا فاش شد
🔹
طبق گزارش یک نشریه انگلیسی، رئیس فیفا در زمان حضور در یوفا برای مدت ۵ سال با یک زن که همکار سابقش بود رابطهٔ غیراخلاقی داشته و از سمتش سوء استفاده کرده است.
🔸
پیش از این اینفانتینو ابتدا به خاطر زد و بند با ترامپ پروندهٔ سنگین اخراجش از سوی یوفا کلید خورده بود.
🔹
حالا افشای رسوایی اخلاقی او در ٣ روز گذشته او را بیش از پیش به در خروج فیفا نزدیک کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455379" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455378">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8756ae1c.mp4?token=S5TTcZhApKni9kYoUo8ufQHW7PRSkAGyl3t_NYBEXYQyMOj2PyM59bg-YViv8cmfdlqaWcyeM8aVkyKAaTktxol52RfQANtTcBmjUVIhXw7rXIdgdtsPvhw2LxLlP1_aQi5pNQsq0Cu4lZNyHoKIhwnWES5XddRdb4hDhdFIEJy4QfzgLm25zIvhcww1sloEBzdd8aZdXuXzNFlEZjt_6IJ9AlR2w8dH9LsokyW67tvp_zwUZxJRUzSeF_69W4aUK-gzaW73M96apMNOqO4yDrK0wgiypc1Al9552GOaVnGQwjHV2IAyVdKY5nXoWYniAWa_z9aYKx3lScTzTyu9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8756ae1c.mp4?token=S5TTcZhApKni9kYoUo8ufQHW7PRSkAGyl3t_NYBEXYQyMOj2PyM59bg-YViv8cmfdlqaWcyeM8aVkyKAaTktxol52RfQANtTcBmjUVIhXw7rXIdgdtsPvhw2LxLlP1_aQi5pNQsq0Cu4lZNyHoKIhwnWES5XddRdb4hDhdFIEJy4QfzgLm25zIvhcww1sloEBzdd8aZdXuXzNFlEZjt_6IJ9AlR2w8dH9LsokyW67tvp_zwUZxJRUzSeF_69W4aUK-gzaW73M96apMNOqO4yDrK0wgiypc1Al9552GOaVnGQwjHV2IAyVdKY5nXoWYniAWa_z9aYKx3lScTzTyu9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ مطالبه رهبر انقلاب از رئیس جدید سازمان بسیج
🔸
تعمیق و گسترش فرهنگ بسیج و مقاومت به منظور تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت آحاد مردم مبعوث شده و اقشار میلیونی جانفدا در راستای ایران قوی و متحد و حفاظت از انقلاب اسلامی
🔸
تقویت شبکه‌ی اطلاعات…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455378" target="_blank">📅 20:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXTkr3H5Sfn6ydswZE11iSaSZ69opPCP8DnARxSYHauGVbF5amKkCFO4rPVe2tJz6OLhVntld9u3vZYsyoomZWy_HRi8NR8-rOlIFAXVqSJmvYC5NH6x5_yupvhvSz3qzcbLEbMttIx1LcCMsOwLNeGxo_o8cWOEzevb-gdTasZ9PQWrw9WD0EadHKl_ZbgcQ5o-NuGPSY3G8WcvFSJ-pOSkB4TbqBaxdtoLo4AxEOuwQpsyn6kvv7rewbH4qf5Lgz0dIngJBPcD3Li9Ni5vl2CoTP2m1vdBN-wt606Uyuain_a90cRvR7s46dKcKNYDv1GyG92Q_VuZjXIJG8jI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیصال ترامپ؛ ایران باید به آمریکا غرامت بدهد
🔹
«دونالد ترامپ» رئیس‌جمهور آمریکا امشب در پیامی در شبکه اجتماعی تروث سوشال نوشت که متوجه شده نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند.
🔹
ترامپ با جالب توصیف کردن خواسته ایران نوشت: «من نیز اکنون درخواست غرامت از ایران دارم،‌ برای تمام افرادی که آنها با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که آنها به خاطر آن مشهور هستند، به قتل رسانده یا به شدت مجروح کرده‌اند».
🔸
البته ترامپ در این پیام هیچ اشاره‌ای نکرد که نظامیان آمریکایی کشته شده در منطقه غرب آسیا و هزاران کیلومتر دورتر از خاک آمریکا، در جریان حمله و اشغالگری آمریکا در عراق، افغانستان و سوریه و توسط هسته‌های مقاومت این کشورها کشته شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/455377" target="_blank">📅 20:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455376">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64259362bf.mp4?token=TKo65kfi8DLoyzTE8HA1s47kUZcvNMFzHFpyfvHxCzR_IDn3sHIPy5wuSEy_Wvl9LqfQWy7GFtckRzGKakQ4zx5LZvvCNVjYgCmNMIMrHros6GvsJs5f2Xl0royKDTM2Sn37zVx0jME3UHbh1mNG5uVusK1Knjab3C74s91KMhSoYqMK4Z7rkyXeN9iMv7rcYQqCG48cKmEdR6R4PccaXe6FNEesBP8ouSuuMWYymX5s0SxAY74OKk2_agnU08nTjXOhAnZMU7EBXaTA4tPBzjY2N67-tkA9_MNsQLOJOb62NHX83nfUilIjpbsCNSLynM-RJLjl1H90onv_W7S5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64259362bf.mp4?token=TKo65kfi8DLoyzTE8HA1s47kUZcvNMFzHFpyfvHxCzR_IDn3sHIPy5wuSEy_Wvl9LqfQWy7GFtckRzGKakQ4zx5LZvvCNVjYgCmNMIMrHros6GvsJs5f2Xl0royKDTM2Sn37zVx0jME3UHbh1mNG5uVusK1Knjab3C74s91KMhSoYqMK4Z7rkyXeN9iMv7rcYQqCG48cKmEdR6R4PccaXe6FNEesBP8ouSuuMWYymX5s0SxAY74OKk2_agnU08nTjXOhAnZMU7EBXaTA4tPBzjY2N67-tkA9_MNsQLOJOb62NHX83nfUilIjpbsCNSLynM-RJLjl1H90onv_W7S5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455376" target="_blank">📅 20:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455375">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsq26edPi5KZyERshTutpv2pBLmsGxwj-q4qpTcOK4UiCgzpaHFoVPUlMNojowVZfB5t0qFNJCrpDc6GqRECTe9Ve-5-NvpdByVc0aSJ4gWY8Qi1HTCqCFJgpgrO8VKINb87Afch--qSTkTwj6TIzEmbVktIHLPxGnDid_rt0kibnmOwfpiztjrjRC5Ctxy7WzVjL2tgxawRWQxxQ9rQ9qjxix5opl1v-4-kUsgenY2Nag-Ja9S4YM-bu4NkX-a2fy8hVTvyQ--zQYV6eaD8H3uZtf_JIM0Xa3QT8lgIuJIHgh1IZ8MlAJEb90lVbAXQPC_-iRycxQTIcGX3WLLYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جدید ستادکل نیروهای مسلح را بیشتر بشناسید
🔹
سرلشکر علی عبداللهی از فرماندهان باسابقه نیروهای مسلح و از چهره‌های شناخته‌شده دوران دفاع مقدس است که بیش از چهار دهه سابقه فعالیت و مسئولیت در حوزه‌های مختلف نظامی، انتظامی، امنیتی و اجرایی دارد.
🔹
او در طول سال‌های خدمت خود مسئولیت‌های مختلفی از جمله فرماندهی لشکر ۱۶ قدس گیلان، جانشینی نیروی هوایی سپاه، معاونت هماهنگ‌کننده و جانشینی فرمانده نیروی انتظامی و سرپرستی فرماندهی انتظامی کشور را برعهده داشته است.
🔹
عبداللهی همچنین سابقه استانداری سمنان و گیلان، معاونت امنیتی وزارت کشور، معاونت آماد، پشتیبانی و تحقیقات صنعتی و معاونت هماهنگ‌کننده ستاد کل نیروهای مسلح را در کارنامه خود دارد.
🔹
جانشینی رئیس ستاد کل نیروهای مسلح و فرماندهی قرارگاه مرکزی حضرت خاتم‌الانبیا(ص) از دیگر مسئولیت‌های وی در سال‌های گذشته بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455375" target="_blank">📅 20:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UugaDZLWhmZYPYY6D_JLTjA_Z-sfEjHXWbJ2J1c85CgwR7fssXhKpWNgeZzN_bjuGYhUZNXyTq6rOsuuxj36Q-789MLQT0HesnSdYeiYvTqlLq551k8Bglra8qyFTJr-1ICWLCzE-BUxpqdlxaH5dKFbWb-tU-BdPiEAqf8v2AkvJ-xFgrXxJlV6LN0YO_JBIZuVYgX8Z5_gy3C10dAi4YBqwMxWbNYPeob8g_7LPSymMDIAgI8jC08_AJ5aLo3tujOrNvLc4fcfnLJal1EF_pXE30eqA3vagjnVwsE-mFU1R7woS7yQZYAzzR7-NjoyumXQYgwk5wof2LYlPq7IHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C96W2XdDDhEoEjEsG4hmUPkX9ocI6xqdwYEWv5HuppqJpZuqOvQcepwrCBKPWCt-ZCdHFR24CjVVoS27GJqEiRyU1HwMCLnTdg8yfVtvW4FaLGLQdT0XKIoZf980ow_RPnbXo0ObM-rnvRl6amp5BEIJqExLsDcRktB2hptrmgSWXYJaELnZogx-2FM_mhArTWwGD6FW-XiSARx8bUydBwDf38kSsREnSdA5QijdwUtAidjKBdV3tQel2SjvAGAqozzo7HZVLRG63-Wi7KvpLI-Gz-KOK_2RvzV68UVxQb0LM8VXTj-ZTWgqMYfCcpre73wuKuTbjazPfVCUzJ0z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8K53b0aRl_24OCed87KMhj6iM_2JW-YWtpIS5JPHli1AfGfBTQIKzPt48u6nnkaAPjrUFUBG4eFVuGwnyfhMIcyXs6TgMXrb5JeHxzVyUgt0gjDgFFtpIQ9Bb-AZQbPPqCmlrYLGy_1kqb47QVFKOBa1lg94D7z9eqS1qmD662JPCmqTRSn4J79sTLct0edMCWTj7IqlnIl_PrxLvCwxBjWfHk3jyFLPlanV2D-hmPAUG3wJBvuWns0t-k3hBw7LoHeL7lUdoWVfDvHmbJHZ1tWRTdefg3djxBP0rWLZICFPmjC9UN23yz_4PcAf7BdUEPB6khhyAXtfspk4I80Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdJwE8HZFNGlfIkBPx5wHgVrfZALcENg_pDpa4cpE3mgD-h3WF1CucJp4rZ7PlNHkd9WSU6GB-YhXZeSGMrLizI5gPgvfsFfHRk3ieVOxiSTpqFBVaEMMLinQGuLyi4EM7ZXrHuWddM5Avp7Cyn9QiYVgk72YBS1jhfTth8AJHGpLoKDHig_byswaUs_cY2W4wSKFCa9XaQaabmkESsWOBzlf5L3kwshCc83M-Sb8daztjkL4hRswY65masXs91gAqfpSSGchXoThW4v_XxuPyGj1QUQJqECi7ZHkQnoA9p5sriuIzk9TAROg4KiSuvC-ZbCo0uLpgyeDnLHkvMM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJTdhgFmMtoP0e20v1MpfTG9ivhNIri8KR9I47CLGC8KouTf7ZhkflZfrRyKoSdPsILPt-gzgniK5Cu76DqWjLEeF3t0G4JPCWkRB_mkkPPpExB_8cctYGpjPXQ_s5CQjKM-OzZtaSqFPlvuMjwnH0In9LcTAvDWPEH1UGjS84q9ZCBM19Rk6l43KuADIyu4jk36pMFpXd_jaOS4s11OyEuifCeWP8ymmRvebJTcJD8FA52Dkg0uo2XNbqK_K0-HYV7LGidvdZcp8erCvseT7kurZShJZ7s2HjQCf69HT_Fyn95QMnJt_b4l87gdBH5_JY5rFY5n_Ul6Ja_5q9PAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Npet8KpwhVjSkiYaK9qqgCH7DCxAKepxwgHWQKUVyuQ78AavIi1UwXCmtnjN83TSi3FvIISVJedWu3DC7jPilGKqQ0LnXNPMXgiGVPEy7Xx1pSfYL9C6dLLgNLZyniTSNOFHbVjurD0Cu3-rD7nNYrUkZakXxI6k4rvqb5PD7AlHgjcmoG7e-t3ypkdOhjYKM-6xAJN1_bVwRYAyzm5qJxvBV-m78eQ2LvVIEHyzXi2_g6OkHhhkKvOMRXxV1K82eShKDDAFKsmI4l3sra0GBZYeOcaZ75J8_9lrTjOlGq_w5QMCrgxlmQQnn0OHg_HKu-W7VQ45eVI9jwaZHjrjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqJlRB5tZE_BljfvBCjPMOkCUMQCcIzXsPuyHWf3bRc8bdei0Qm_FYLQWkXd76pZnqeg8ldf3KaUzXfezt01FxyfpLOlB5mUdlauSEAhWMhSJ1vvvQH4UV32x1OvhCHllr2UiNkUJfDbSqGfpkxXVOfwXuaumaJ7L5PAVVeLh6lJcvhyu8CSNx6Dnd3Hzc_qdjKyCHGWbdlY2I_woGHBE1IP6S3H4FnDNTMmE6cwLm3l6fKO4-56YcZWXw6jj7VMtVrro0qcHfOCYP8w2DEBRf9ZUdlZWkBpot4U-UbiqNqUT6TJebo1h0eYiKOa7y-XUMOulopFJn4IJP9zi9jJvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر مادر همسر سید حسن خمینی
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455368" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=d2O-pbgIMFtp6fGOsjtbWzUrGSWyGfyIUvCBOae8lTe1UiAL3NLl9-ivzOm3DvIf1wqzhDwObBWxfyJ0KtgWAq4UEc7eE6IG9IueR2tq5KOYb9afYsO0NMmv44CPG49IVdbU-XF-tNGWidpiWo3kqrGmYsMZ_4TjX_frj0MksuZZMNCTIjUpNKCchgbed3SL40mJkiLjQnNY72uqxc2BwYlVuygdZyHG-C9R1pBbR9rj4sa7ePUY09pvHjHFOeXcWKlgztyxe3y9q6UoEMHKvmUokJheaP7OKI47ef2yTj2jfWZgXSWKupcMC-1O1skQj6h7h7I-BF5smhbnEQxaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=d2O-pbgIMFtp6fGOsjtbWzUrGSWyGfyIUvCBOae8lTe1UiAL3NLl9-ivzOm3DvIf1wqzhDwObBWxfyJ0KtgWAq4UEc7eE6IG9IueR2tq5KOYb9afYsO0NMmv44CPG49IVdbU-XF-tNGWidpiWo3kqrGmYsMZ_4TjX_frj0MksuZZMNCTIjUpNKCchgbed3SL40mJkiLjQnNY72uqxc2BwYlVuygdZyHG-C9R1pBbR9rj4sa7ePUY09pvHjHFOeXcWKlgztyxe3y9q6UoEMHKvmUokJheaP7OKI47ef2yTj2jfWZgXSWKupcMC-1O1skQj6h7h7I-BF5smhbnEQxaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسر بازنشستۀ آمریکا: ایران معادلات را از هسته‌ای به تنگۀ هرمز تغییر داد
🔹
ویلیام پاتنم: هدف آمریکا همیشه این بود که ایران به سلاح هسته‌ای دست پیدا نکند اما امروز تمام تمرکز آمریکا روی بازکردن تنگۀ هرمز است.
🔹
اقدامات نظامی آمریکا تاکنون نتوانسته به اهداف تعیین‌شده علیه ایران منتهی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455367" target="_blank">📅 19:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP_7ecKDgf1U-rk2Ux3B-Rmf08VE9mTEjuM_69FNPLzwQQsXguD6uJEmWoLwRaGE2rvtGsf3K270t7CsEywUuLPcMmTg6gE5IjTTfCeMU-6WTj6xMulr6r9u7qSm3UkqT4ic6qOys6GoSpe91BQB47Spp5AHmgaiJPYWF2dkqL4cc0m0AYtE0FZeSJnwRoAbFerStR0HZLsJ7etJbRwpup2Gjv2BFEC-av5arQ5DIk3E6S0LNm1vDC1wmIrsq8og4HBZOM5qEWQehK2Tita_YEY52Es8wQzoxi6f6e5CP21q05shargXdzkrdZSt5zbLMkU6LhfnFZ_HVjzFCLRB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید جنبلاط: صلح با اسرائیل غیر ممکن است
🔹
ولید جنبلاط، از رهبران دروزی و رئیس حزب سوسیالیست ترقی‌خواه لبنان، در گفت‌وگو با الجزیره گفت: «ما امروز با نقشه‌ای جدید از مرزهای اسرائیل روبه‌رو هستیم.»
🔹
وی با ابراز نگرانی از حجم انبوه آوارگان جنگی که از جنوب لبنان…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455366" target="_blank">📅 19:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مطالبات فرمانده معظم کل قوا از فرمانده جدید سپاه پاسداران
🔸
ارتقاء مستمر و همه‌جانبه‌ی توانمندی‌ها به منظور بازدارندگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن
🔸
اعتلای فرهنگی در سازمان سپاه و تقویت تقوا، بصیرت و روحیه‌ی انقلابی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455365" target="_blank">📅 19:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbe1U7_xjIKZG5J0kLHNhriufyJjxbLqYREYeeKAFFf-7xD2zgP-1HRwGt_d3hOpF6xYZfLGKQIev8JeU_gHyy5UpKPwlqXTB53YwToIrkx4zWqJZ_KvhBltBo9zKpUss2B-0ElrWjgnKQFvuSke0qzzKibv0KMq8ebmbWtBKBVvdHwrnAX6R5weJreIKq4BduYw5nP_oj1cIij28vGcpoHn2Hcy8d2j_I6ox9VHKkKa4lpugsz2C2nsQPOMkvfgBZMQHl9BRKb2IMQTFZAfuot_yIdfVk8SRqfe_NhQq3RZIl9Wvz_9xwqogHmd2dvPiqPFrk4ZlD3B80UODvV1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب از سرلشکر عبداللهی، رئیس جدید ستادکل نیروهای مسلح چه مطالباتی دارند؟
🔸
ارتقای توانمندی و آمادگی‌های همه‌جانبه و روزآمد دفاعی-امنیتی نیروهای مسلح و بسیج مردمی
🔸
فراهم‌سازی امکان پاسخگویی به‌موقع، انقلابی و مؤثر به هر سطح و نوع از تهدیدات متعارف و…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455364" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۴ مطالبه رهبر انقلاب از رئیس جدید سازمان بسیج
🔸
تعمیق و گسترش فرهنگ بسیج و مقاومت به منظور تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت آحاد مردم مبعوث شده و اقشار میلیونی جانفدا در راستای ایران قوی و متحد و حفاظت از انقلاب اسلامی
🔸
تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن
🔸
تعامل سازنده و مؤثر با دیگر نهادها و سازمان‌های حاکمیتی، دولتی و عمومی و گسترش گروه‌های جهادی، بسیج اقشار و محلات به منظور توسعه‌ی خدمات اجتماعی اثربخش با محوریت مسجد
🔸
ترویج فرهنگ بسیجی به عنوان الگوی مقاومت و پایداری مردمی در سراسر جهان در برابر استکبار صهیونی-آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/455363" target="_blank">📅 19:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuFfPcTFE4oSQYP1iGqKemJFTEwcRiPIPAvoLxkyPXc8mGl53WGPMNWJQm4xrFPKUdRNv0X0i_KYKEQkiiUxPYFQ_L8MKHmXwjtmS1rqQd2p3_HLFkInqN8fqoalmuPJIHmOao409XGhkDBP_sJtQJe78Xz9LzPc16CcAxv3w2BIdasrq8bMmEuuc1_WKUahBRwnhbiPgl83xBbJHxF8ZNq8Ojq_x-d4gmhuQ1EFiHCDvUd2IpEXsEDS_9ulpOQWuc4kK3FuFkqyhtvDyce3NAX14dS-hnRPhI3whJZa822M0zTbXdYefvCi7LqWnQNq-hRofUxZE_gn_5pfIjZDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات فرمانده معظم کل قوا از فرمانده جدید سپاه پاسداران
🔸
ارتقاء مستمر و همه‌جانبه‌ی توانمندی‌ها به منظور بازدارندگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن
🔸
اعتلای فرهنگی در سازمان سپاه و تقویت تقوا، بصیرت و روحیه‌ی انقلابی به عنوان گوهر درونی آحاد پاسداران و فرماندهان
🔸
گسترش مدیریت و فرماندهی برخوردار از بنیه‌ی معنوی و علمی و مهارت‌های نوین در سلسله مراتب سازمانی
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455361" target="_blank">📅 19:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh4m8zFIyT7rwJ9Lg-evFTxd73awYBtJGAHa1AYDzeZP9nWeRaueCHGlmU33YYSGpY6orcdG1bhlZM4sPcLJOiUJqLXACX0A3GGM1HLQ1tDZOhpZDWaPhmW33IzuUSgJIqoBDPzeeysVhm7Ue5-Qhvx0_nkOx0VPJWxjwg4lppEEXlHlryaU1afbUqc1IN6BS8lLSkiO5fwpIlWRSJJWejykLsCUukWwJzXvRyUrgczuhYWp7aivJhx2imCh5-ptOCaW95EXk-sfolp29opaGpcUBz0dsGeR4ke6iMaMkUJ21yRNBiv8wdojTuPwhsAtl2cnCnOavcIbtKoytUorKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455360" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455357">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
تا ساعتی دیگر احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/455357" target="_blank">📅 19:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455356">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر در مرز استان‌های خوزستان، ایلام و لرستان و حوالی حسینیه به وقوع پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455356" target="_blank">📅 18:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0893f142a.mp4?token=MtoQ0-oSpJpHfLZT7aBBlXeBplDbpbjUvqXqg_IfOo6E-BavbmlSztF4gBo6efUC4bArNRfxF3sJRfrfYHqT6dYh2uyaKrErccsnVPProUM5AQfTfWhRvgW1wp9IICoRlub7E-9DxriaJRMTMes8ZGe7o6B744LTU2TluGwArb9jrGOw27xosfZ-cHIdEabFaOkkP47-hS4uo-4IXa4QTAgYhqVMIcIfWg5YV28WA1mHOkP8zmU6Wx4RFUUgjWagKOV-fIFECLesn7hW2Dj1meaT9VOZSElydwyBtKK3Lnf1wDe3rysTsDUrcIxbl1NRHDZ3WPyEnwwOW9yvWStt8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0893f142a.mp4?token=MtoQ0-oSpJpHfLZT7aBBlXeBplDbpbjUvqXqg_IfOo6E-BavbmlSztF4gBo6efUC4bArNRfxF3sJRfrfYHqT6dYh2uyaKrErccsnVPProUM5AQfTfWhRvgW1wp9IICoRlub7E-9DxriaJRMTMes8ZGe7o6B744LTU2TluGwArb9jrGOw27xosfZ-cHIdEabFaOkkP47-hS4uo-4IXa4QTAgYhqVMIcIfWg5YV28WA1mHOkP8zmU6Wx4RFUUgjWagKOV-fIFECLesn7hW2Dj1meaT9VOZSElydwyBtKK3Lnf1wDe3rysTsDUrcIxbl1NRHDZ3WPyEnwwOW9yvWStt8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش نحوهٔ برخورد با سلبریتی‌ها در یک سریال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/455355" target="_blank">📅 18:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPjrNp3WBHPM8isaOU7-CHTsKQ-tyCLSn5AfUwnTLOFyT9dZQBMYvUqpTt0CE7dgvSmmlm9w0tsc2uM19uypAugTWxoArffRNcaIRTtXcwiJghw13iVBGsU36G7bEeVKKKDjBO4SE13UBTOw7sHXBTFRCm7NyU0YxUox1XD_ZBpP7t9M_e-hfak0Q165eVzVa9sUOwe73YnOZ8FyVBkRezGCKetpeUcfCNH9lvpbCtmpVyOL6LesnuHaeIRBASMoO7q8IaEyPYMXeYugQArol5maeEg7uGUj3937OUoZkhPR4fFHE5I5rgKN0SOtScTCY1VIX-vPxgxByZf3_fUYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با توفیق خداوند پالایشگاه آرامکو در جیزان را با استفاده از پهپاد به‌صورت دقیق هدف قرار دادیم.
🔹
این اقدام در پاسخ به نفوذ پهپادهای دشمن سعودی به حریم هوایی استان‌های صعده و حجه صورت گرفت. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455354" target="_blank">📅 18:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FobmflJpS7MCUcGjmdUxAragLY5LLODCgjKuvOMiupBM9BAeHUVm76RXpCiEgDanTPxEgMMgPMJMSWGKFUMMZUFlzyzhWMQmTHnrWQwz_2IRpXprB2AfPJIH5sAoTLe2J7Ad0spxiNZXRRSnwt71XcMkp0rqI9va901Ej8WnAvQ8vhQTzDTrst2GOq__5gdA4FBw2_pY-W0KjKSKPLFkYzc3DCLatBpu1b3rVC-sfK4BUAwybu5b1UP-biNsDBmMaazQoMU0H-Uo0UiCxBd2LShpdmUawp9uVOTxCbmRO9XhpAwuWdJotMWEgmvlR9EXcKtwnL7EKbOPmMznloJwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455352" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8b99ad50.mp4?token=nlRzqPxObW5hekZcoobManlsftad5jzf6v1aW9b5XDXyREh_WX8rNNykfzYrFuarAksMdBA3_36DBc2mEfqUnoKkgqyTx4QolRb1I7sHQ_Z78majXMT4BR3ZEoeq2a3N2G_tSv644sLoL4gnDpvE-8_w454nDbi3-jsRr9rNnWJc2otNsP1DJWU9aZqunojisT_F-jMHCt0zrs3WJVfDcaq9HyKinrCsAtNZ4Bf2p66AZ0I0t0uj1Djxoz3RrTDXd755_IO-1VeZ3u2HVy-llVvaseaX5xbWqFzmh6oHsY_vbJiz7UPoEVS8bUT1Pc91m6qYyzlDXCaxcT6jTkxx2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8b99ad50.mp4?token=nlRzqPxObW5hekZcoobManlsftad5jzf6v1aW9b5XDXyREh_WX8rNNykfzYrFuarAksMdBA3_36DBc2mEfqUnoKkgqyTx4QolRb1I7sHQ_Z78majXMT4BR3ZEoeq2a3N2G_tSv644sLoL4gnDpvE-8_w454nDbi3-jsRr9rNnWJc2otNsP1DJWU9aZqunojisT_F-jMHCt0zrs3WJVfDcaq9HyKinrCsAtNZ4Bf2p66AZ0I0t0uj1Djxoz3RrTDXd755_IO-1VeZ3u2HVy-llVvaseaX5xbWqFzmh6oHsY_vbJiz7UPoEVS8bUT1Pc91m6qYyzlDXCaxcT6jTkxx2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکسی پرنده سریال پایتخت در واقعیت وجود دارد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/455351" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455350">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1921d9c71.mp4?token=ZyZQv9YwMv-Q2D1PSSwDWf3wI0gbewYR55wBAjhRFNlXNtAtT6nNukq_8Xl1bmGnQakawlyiavy-6BjhrkkgGtb9FIfwQvPSJ0PMau4zJ4koHr6OZC3sRAfs98mBKN4XXebhcEg9uIV1iX0Gc7l30AtM2HA-R5HPGaffAdtFsN-hMJH88TQkyHyLHm3IH3z4Ywm5Z9zGzrKEgSfIi5vbhcLwtaLZOKkrjeDW68tjX7_1IbOXCWAFLIKJe877dvI4wl0F2b8ZuwwKH22nKt_szvQVa2-cO_3aCFFt5G-K4DncsSAwmOUus1V8HFmDjNcElaeVy99_ltfGq7JXCU9F5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1921d9c71.mp4?token=ZyZQv9YwMv-Q2D1PSSwDWf3wI0gbewYR55wBAjhRFNlXNtAtT6nNukq_8Xl1bmGnQakawlyiavy-6BjhrkkgGtb9FIfwQvPSJ0PMau4zJ4koHr6OZC3sRAfs98mBKN4XXebhcEg9uIV1iX0Gc7l30AtM2HA-R5HPGaffAdtFsN-hMJH88TQkyHyLHm3IH3z4Ywm5Z9zGzrKEgSfIi5vbhcLwtaLZOKkrjeDW68tjX7_1IbOXCWAFLIKJe877dvI4wl0F2b8ZuwwKH22nKt_szvQVa2-cO_3aCFFt5G-K4DncsSAwmOUus1V8HFmDjNcElaeVy99_ltfGq7JXCU9F5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه سردردهایی خطرناک هستند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455350" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3205d65f27.mp4?token=IynMFTrwKVBd0vZ-flk2qF3w0hbD5KqIDv2hpOxg-yXdPyljdDLsRjAaUU5B1al2BE9wFA-tPRXC1EK27fekqLwX4X82-mHYF4PRu92QAQ5vNqz3O_XXqrbmJ7DimG4d9wBU5P_uCmJF3Se-mgpyTQ0cWjNQ7Y_3aC1G7CGgt23T5oAnBi8L2B0EZUOd81VM9DILaCyojleCQpeNMA7TdjMdP-8114oU-_M1LuFELDOp1o5tQOedifcQrISCME_pFXrnPZR-kKgSKxVu1QU5rSAMlglNkd36LkbYtpgi_ePBlL-l-vZ4YJgNzA4bd8OBq3KNGVB-Z1GoEHZIKKM_bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3205d65f27.mp4?token=IynMFTrwKVBd0vZ-flk2qF3w0hbD5KqIDv2hpOxg-yXdPyljdDLsRjAaUU5B1al2BE9wFA-tPRXC1EK27fekqLwX4X82-mHYF4PRu92QAQ5vNqz3O_XXqrbmJ7DimG4d9wBU5P_uCmJF3Se-mgpyTQ0cWjNQ7Y_3aC1G7CGgt23T5oAnBi8L2B0EZUOd81VM9DILaCyojleCQpeNMA7TdjMdP-8114oU-_M1LuFELDOp1o5tQOedifcQrISCME_pFXrnPZR-kKgSKxVu1QU5rSAMlglNkd36LkbYtpgi_ePBlL-l-vZ4YJgNzA4bd8OBq3KNGVB-Z1GoEHZIKKM_bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین تصاویر ماهواره‌ای از تنگه‌ هرمز
🔹
ترامپ می‌گوید، «تنگه هرمز باز است و ما آن را کنترل می‌کنیم» اما پایش‌های دریایی می‌گوید معدود کشتی‌های عبوری از مسیر ایران تردد می‌کنند.
🔹
داده‌های شرکت رهیابی تردد دریایی مارین نشان می‌دهد عبور از تنگه هرمز به میزان محسوسی کم شده و جریان عبور از مسیر ایران برقرار است؛ پایش‌ ماهواره‌ای این شرکت می‌گوید تردد در تنگه هرمز روز یک‌شنبه نسبت به جمعه ۹ کشتی کم شده است.
🔸
شب گذشته تصاویری از شعله‌های آتش در نزدیکی تنگه هرمز منتشر شد که گفته می‌شد شناوری در منطقه «کمزار» آب‌های عمان در حال سوختن بوده؛ ساعاتی بعد تصاویر نشان داد که یک کشتی که می‌خواسته با اسکورت آمریکا وارد تنگه هرمز شود، هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455349" target="_blank">📅 18:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ef328501.mp4?token=u7vXbL6FnIJEK7Nb-VrTXY76hlj4ngFuPz-LI_o-0n-wWG6VzJxN_6VQ89lKXvKh8Tw5gnb5iAXfYs5qkPP2YcZax2XQzBg7oPu2ydla1WuVnHtZ2l4zHGI0wWXrteDZfaZj7woGkD9SpNGBMMfEO6Nl2GFykFkMdZhszYfy9068rRYjjruRu895V4ZxwEQGVmX1QspGpLtEq4a7gA64xbyjSc_E771vACAOCrijcGqyv6bp9yYquMAMvcmri8gB5Yj3p5pI42QP6cKFGRQ47XMT3xCLsTjEfWA5rkDwa4Fsma9-LoAefRD3wKoweYoihx_B0cih-2aAUlq-Yk26rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ef328501.mp4?token=u7vXbL6FnIJEK7Nb-VrTXY76hlj4ngFuPz-LI_o-0n-wWG6VzJxN_6VQ89lKXvKh8Tw5gnb5iAXfYs5qkPP2YcZax2XQzBg7oPu2ydla1WuVnHtZ2l4zHGI0wWXrteDZfaZj7woGkD9SpNGBMMfEO6Nl2GFykFkMdZhszYfy9068rRYjjruRu895V4ZxwEQGVmX1QspGpLtEq4a7gA64xbyjSc_E771vACAOCrijcGqyv6bp9yYquMAMvcmri8gB5Yj3p5pI42QP6cKFGRQ47XMT3xCLsTjEfWA5rkDwa4Fsma9-LoAefRD3wKoweYoihx_B0cih-2aAUlq-Yk26rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغوش خالی مادر پشت کیک تولد دخترش
🔸
هنا دهقانی قرار بود ۱۰ ساله شود، اما موشک آمریکایی مدرسه و قلب پدر را ویران کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/455348" target="_blank">📅 18:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84326ff6a4.mp4?token=JqiHeRQcEv9GNeqnyFwsUvkUmJmZEyfBHen9ftDoajVnLkwaS_IGo2Nd9eHmYTNC8KbJWpjmxX3GfZfqi_slc1HD2A1bpE9UOzUBxcfAbswKwy0aEGbHG4Tn3w3bcEZptoroy0gKYbx74ccSF8Xo5TV5cMTBKugxoWyNYlrCYD63NuQjWP-eCy3YJZOaoDUOdHMnSm1NJ5WjBWaV1aElG9dDjCPCpSL91B8WGT_LZpyMASBEwcLnLpYh-lw-yYYdzMipmEGEbg4TM7Tj8JzpRSyJRzcR6jetHTyg32NQhasHUcUBHn3jt4ss7TjxtXGASeVjm8VANqngp56Fbso-oRDgOYXLRSsLBennTzo-iGdJF9Ic0aRnxVMBL2rmKF4eyS-5eXufH018AZGl_YKh069EreEzWhwSGFzhUrjf8SPsO-npEodiTaZS2ZSoDLyhA8xWtmUmtJPMxb1XZjk6kmN9Xtz2PtNQIRMXgCnSPba-fhSl_oXEY64fsVU1XnDEdtLMIEm2kCktltBuvvsFVbZxlhnXmFQiVDmRFKdS0K-fvDp5BSz2BrHhu9TAlPPjb1qRzYt0r8hzedbQm_Is4o7YRvJVXT_hdZQBXdEdB5B4HGmhUJFSgcUNqeMyA4LKiwtoBFYYcr8xqrbbkfSWn_rH-CDnphMlk9DBVXULG8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84326ff6a4.mp4?token=JqiHeRQcEv9GNeqnyFwsUvkUmJmZEyfBHen9ftDoajVnLkwaS_IGo2Nd9eHmYTNC8KbJWpjmxX3GfZfqi_slc1HD2A1bpE9UOzUBxcfAbswKwy0aEGbHG4Tn3w3bcEZptoroy0gKYbx74ccSF8Xo5TV5cMTBKugxoWyNYlrCYD63NuQjWP-eCy3YJZOaoDUOdHMnSm1NJ5WjBWaV1aElG9dDjCPCpSL91B8WGT_LZpyMASBEwcLnLpYh-lw-yYYdzMipmEGEbg4TM7Tj8JzpRSyJRzcR6jetHTyg32NQhasHUcUBHn3jt4ss7TjxtXGASeVjm8VANqngp56Fbso-oRDgOYXLRSsLBennTzo-iGdJF9Ic0aRnxVMBL2rmKF4eyS-5eXufH018AZGl_YKh069EreEzWhwSGFzhUrjf8SPsO-npEodiTaZS2ZSoDLyhA8xWtmUmtJPMxb1XZjk6kmN9Xtz2PtNQIRMXgCnSPba-fhSl_oXEY64fsVU1XnDEdtLMIEm2kCktltBuvvsFVbZxlhnXmFQiVDmRFKdS0K-fvDp5BSz2BrHhu9TAlPPjb1qRzYt0r8hzedbQm_Is4o7YRvJVXT_hdZQBXdEdB5B4HGmhUJFSgcUNqeMyA4LKiwtoBFYYcr8xqrbbkfSWn_rH-CDnphMlk9DBVXULG8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهی که شنوا و ناشنوا نمی‌شناسد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455347" target="_blank">📅 17:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حملات پهپادی یمن به مزدوران ریاض در «المخا»
🔹
شبکه سعودی العربیه مدعی شد سامانه‌های پدافندی مزدوران این کشور در المخا در حال مقابله با پهپادهاست، هنوز درباره تلفات احتمالی ناشی از این حملات، خبری منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455346" target="_blank">📅 17:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccc08889a.mp4?token=WrOJtln0d1eZoUuDL_UZi4dzR3cc5HWJYvU97MATACVgVRglKEZZ5W86LWAcyH6B5UNwkwjkL26WckFwMx43U-MV3UrhyrU7E8WzNDOV4lVH6fKwTd1gmu4H3Fshja6bN8PgMeg0DBZtErJ7Gva4vkXIq846qzwSEkoPXFzEmCXfukuZDOrK-viYtpwZzM-tlrxkJUYmM9bb1B4wJFk-f3tpQuhyEvnNKs8PDvPdF3XMnjpUM-reVML-2MTKzrR_8STRh_llSBVwPOed9dFYQ90mvOcaAJIMhd7DmWf_yIDfAaZXx_-fUYf_SPM6XdAAbqzfiEYAO-sz-D1Ndn4UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccc08889a.mp4?token=WrOJtln0d1eZoUuDL_UZi4dzR3cc5HWJYvU97MATACVgVRglKEZZ5W86LWAcyH6B5UNwkwjkL26WckFwMx43U-MV3UrhyrU7E8WzNDOV4lVH6fKwTd1gmu4H3Fshja6bN8PgMeg0DBZtErJ7Gva4vkXIq846qzwSEkoPXFzEmCXfukuZDOrK-viYtpwZzM-tlrxkJUYmM9bb1B4wJFk-f3tpQuhyEvnNKs8PDvPdF3XMnjpUM-reVML-2MTKzrR_8STRh_llSBVwPOed9dFYQ90mvOcaAJIMhd7DmWf_yIDfAaZXx_-fUYf_SPM6XdAAbqzfiEYAO-sz-D1Ndn4UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سودی که از کنوانسیون خزر به جیب اروپا می‌رود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455345" target="_blank">📅 17:30 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
