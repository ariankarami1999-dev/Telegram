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
<img src="https://cdn4.telesco.pe/file/Sh_oQ_zrKPH5aEEo_UHIkHmH4ohkX1KR4MgYFCYvn9QlX2PzCYPFnD-d4MYSKlo7ZtpWkjqFnbK54kWzJIGARLUdef5dkc1zBOhNl-1dEi9SWtogSSxxpDYbUrnn_C6Y8qwMG1d8Auofk5yJawccRL29wVE0zGv9qyC3_6hfWBgaMkoH-TGadSadhCVWHiuwJhAKuAvFMVkxs5xqfkF2lM9AyiK7QN1fnOKY3mGG0LKITp9gKq5FOG4btqrwhRpDC0VE9keN-QkilQ351WFaKDAtQ2F1Ern5snhIU0Tz6Apv9bacXS3OP73D_kK9wt_GhAKpqTR0z4Xwl0QBu69vvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 333K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIPnEhYv6wPYzlyleIXGlbFfGVgRiBuNU1R43W1l_R0MYgEQB-2LltZalrOJ5FrPfYbL-GrjPzNPIwRlbSqrrKfOSpTiHfQUys9HvRuKy90JgZZdsBhd_-Qfg9KpwZyWIMu1iQeQY_lwi_rZ94JW4VIcTmQwYhHPiwQ6JfxeIr1MHq48bJ9nDVP46ROVFKYThKZLGCd5tera60Q3Iiic-1RMyYM1X3cda_Eirb4WILL_4NzuVrSh_wuykJs9muAhRhqVd6vRGpUpyLhAzRn5S6dCcNWSzcsl94miTItgszAlFINdcreoLuJ-g6hE9SeAPecsD5Xlg7sPtIIbD2HjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlX5Wf-q4bWnaQiTQaiHHEGYOx4fef8wkkJqSOlEGttdn8ffAh1gMaLtlGEdRU_bprThW60R-PDKD2_b5ISa26-CO75P_NFhxQl05ndre3d6GCWZX_eGcAg9g1NpGNt-pqM8fbrdxZ8P2_RAaJdroMMgsxjWLgFqcNkNMkof9Vx07JPdJRl_dh11JEF6GjXQg97-HISXjClyA7gyMeaY-MDnZ38M76nWQuNpz5mU0JwF5AdAoEoSqv-gNGhGnA8bDOo8YNU8hJm5VXUwwcfAWCwLZiFKINSYy1dybOrIx-XpYIau-PsU8gSEq7KFA-jVfqe6vtob6rdnOCaaReLleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خبرگزاری های رژیم :
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌ کشی و با پارچه پوشیده شده است.
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ ازاین‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد.
@withyashar
یاشار : امام رضا هم جواب کرد
😂</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=m0nrO3qxzHL_jMUGjvOvZMIFAOp_0ndmq5zD4OvhNULxXMICNZjxJzqJNcCM0v3lJWXw1ZwwmtxPM0IsIqRxAb7y-JOsY0_4eOQYMwOGuC2NKecMPBzwlE8Y6aTI5XVHet_e2XMOYgdWUnFz-V2KEJGxOw0vD4RbaL9tP-t4EnFRlhsUucU8DcbEzTnIzZaK3KSnIBDCszFXtLto9qnc_95OW4znHQecXO1INrH4ZEx1JLuzwC6qDAN2qKD5NIPU1flYrd2Y5ZKc0YvFgmWweyfmETy0rbm3pvFbJ2D2pwMT6YQ_g6_ED8XyLf5RR9ndxJSDSycmE9YbtMqCnA80kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=m0nrO3qxzHL_jMUGjvOvZMIFAOp_0ndmq5zD4OvhNULxXMICNZjxJzqJNcCM0v3lJWXw1ZwwmtxPM0IsIqRxAb7y-JOsY0_4eOQYMwOGuC2NKecMPBzwlE8Y6aTI5XVHet_e2XMOYgdWUnFz-V2KEJGxOw0vD4RbaL9tP-t4EnFRlhsUucU8DcbEzTnIzZaK3KSnIBDCszFXtLto9qnc_95OW4znHQecXO1INrH4ZEx1JLuzwC6qDAN2qKD5NIPU1flYrd2Y5ZKc0YvFgmWweyfmETy0rbm3pvFbJ2D2pwMT6YQ_g6_ED8XyLf5RR9ndxJSDSycmE9YbtMqCnA80kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUE7J5vGNMoNgUuQZJdPFopx4cNTfSBXLt335BtwLhjrjw9ui9ZBeItsxKiFNRmZy6f70yzvx6WLFbfa4gAdFa_RZoqAoracPq-aVGDipqKM-xZo0Yl5nSMsUBiByq8Az7dvspBq9tHtTjc-ehkREK9SgfmxbITd-Y7FY4__GlSIZlSZPcCgehX8PPNSsVpkLlq_KA9OCPd4-oGRcCMckdYlsmoAdGOGt_RdgIrP0naV_OpVkAs59X-hOqou-5GIyMQspnN0LtLyc-9OSEHMS14F1Ww0MZG1vJFwk1PBdBsX5WVkS4kSuCcFVRXZ9erFHpSy1sQ59AcThDBXJWqJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shoNSEWJI5dwcaK9uxhdv3B0Jv9CRjlw_yXuqI1TvZg4SgXZIIO7RU92OSEka5WY4IDWD_wK3adem6YRLenZh2EW6Q0zvG8-R51fOD63u5ntKH7ehHGEosDtgM9MZQAHnwq7lFPApOfhcJg8vr9ODlkrkii7IioqmfXSUpBlN5UCF-lEgz_0DY8FFSLy1BVRymqZDhyxuBD_5OTBBu40OLmTyGmBw0qE0yhH-hnWdO7SUXTxtt-zJiA0jDTmsEHShYLOyz8R2ADXy2C21ZA4PectFy_naa-8e8q2ynqzXp82XPM73xI_SkEokjFX4U6dWWiC0HE8N6PXQEECx9DLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0q-hZcTcWkr8ykfj78naAn6KI6ZRqw3rPNArtWgw-iRboZSK9E_4PWGoEQn_AsSBv-PmWDOYFGB2vJ1_dMOSfSfSCmA-iPI7E6fZalS-KdPoeKO89_E77oN61qMye9r3cwmkOzOCU5mzLJo8RSiui82Yl3gd3lVmqscHXK7Cgy1JJE_02mZsn7kLBbY67xK5ZmVzTAWQEtoyujY4_1xKeCBezMmJpfKbmApwGy95xL1ZHHC2jvNXiUaD15BL3XphHGASrOm8qQ9Cwt3y_qY6PAhkS1HdegvljFG_hHQY5C4cbqVCQ6i_BobSlGIKzp4pLgjBirS20i1ez7HJqah2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=VDYr500ziZN-VECMbsg_2mvzbLzTyJuxYRcB5UYgy5fCnwXA6t4AC38bY1bbRqbuZohXUD0Dm4RDLhv40giYyuvCbh3uzTVeLQF-qdox6Qw1nTitbogb23Um6hrPMdc31R2uPlmVViR9zoni3VjrEBRzEbfxpuIwB1i4JiaxlNaULsuohMNtcvrUOBrhWn2kpjr1r9_xCYtf5z7R5mdxKUEGCA9ShZ94bG5kY04Er3_rsW22SLcQ3YZaZtPacSk0Fd4DqtQzSm71BJvSAVHyW77tFS_eVsIHuZUNAOVEOk2LEZ1V6wBxpXkcZB6LMsHW1-I1TinsM-PLP_xwEfiMqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=VDYr500ziZN-VECMbsg_2mvzbLzTyJuxYRcB5UYgy5fCnwXA6t4AC38bY1bbRqbuZohXUD0Dm4RDLhv40giYyuvCbh3uzTVeLQF-qdox6Qw1nTitbogb23Um6hrPMdc31R2uPlmVViR9zoni3VjrEBRzEbfxpuIwB1i4JiaxlNaULsuohMNtcvrUOBrhWn2kpjr1r9_xCYtf5z7R5mdxKUEGCA9ShZ94bG5kY04Er3_rsW22SLcQ3YZaZtPacSk0Fd4DqtQzSm71BJvSAVHyW77tFS_eVsIHuZUNAOVEOk2LEZ1V6wBxpXkcZB6LMsHW1-I1TinsM-PLP_xwEfiMqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unJKlWMunXBfv7fwbZaKFofgrpjOGxMR93KY50yHW8VeSeACtRTWGw2kCd2sjto4d6Bl27fpJ55c78sZGbUkXT33FI1HiGaGZAeaHFWyS9ho7T_8wB5G2vgAQyUJYb8FgKTwLuGXcWGfQQQ4Esi5GaiH6XGbpiYu0cDnybPJve3B0V1xgfToke6vjlv1jVwXYYZvDCmRQquYdvIrJStKqUIPFIq_MbrVPUjrl-pLW0TORlx42gxYIz4s44z9qigxWmqTOkm9qMxiJOuYl5-_BOAP1dpSlETvZuJTQhHdN0PxHJRx2SF2QngsG2HXLvYHkw2LBKepAzznTVPqrCZJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGZy5au2zooT0tRirK4ROQyyMkRhcGk_XcAsgBVOKVeD8AyxHyGD-l56uovYXtq7wOAeZ9QVAyPhU66HV7pKDYP3qh_zD1r1kSw-m8ScVBbIrTzY3_co14EM-xhyyuIhbfwxrdZBKLy96BAXbLO-N8AvXyNW88QL6AalZvmIfvahUpfAQmmR1TYScTEao9aFkz6_-mcmFTcFRuviwpNsYU1MXgaxp_iE-cqcGvExNfREQR0yZuGc5WAkTOVtEJ_ulYYGQJei716ndKtRDDqNDL9paIh_RfcZu0CujYHhdSYqhU-D84Pb6PI-zBRuxlzXS24OVE4RSRg-UiztNOVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kofg781dy87e2f2PyH1b1qUP_NgNA0R-Fn1L0KAPsT9Fq_lEVGj3gyTxHJEF_frv0PtaKPSDcNIiCllq7NCGUeNCRMxiaVStgrYpvt_eS-tnFNnANVCMl66-uYibjtgb8USLUHjMCYHtG9RfyQHj4nhH42ti4XNm5bmNKqdDRmbUOMaLpF3-cnJ4vttWEa3QaI3L86LBmbEZwDzr7-hh1gtL47ketWFvHe4yOe6x0bzZHYOoOxCSHFUXYYVLncPiUZWD6pmOialYgPC8bSiBS34UASbGCbs3_Hec_sqBc1SNT4y3oi6-Rpe4jhKtizCbDvzmjutMZjGDiMprgCorGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=Oi9mTfr3g4Qj6tEeGRoAS2U19s6DRo6IBSIGEbbq-VDMVWjN0UGm0udgprU2P12CDWgxf72fXaSTypE77_8ytEm4X6CNY-y55lWL_CHVQw4paqTbP3gRQu0Ri7cnsPpAXrly5N5ZEvQt7MkoFyQYhDggHpVAC_QRBkeOp3adrs-QYyajnkP8BRXo-YRzRa-9yzUG-U98a2l7N7CLRPA5GqQ2Cwi0gkJoeukAPpxxA-anAHz5NOPSsEEuvUn2vlBr98d7nj5NIVelZR3NQrl0jadX99VmEtD5ShX4CsCcJuFWdxlYC8rH6Z4iXaPSworwd3X6FRr_69wKXMPLHf__lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=Oi9mTfr3g4Qj6tEeGRoAS2U19s6DRo6IBSIGEbbq-VDMVWjN0UGm0udgprU2P12CDWgxf72fXaSTypE77_8ytEm4X6CNY-y55lWL_CHVQw4paqTbP3gRQu0Ri7cnsPpAXrly5N5ZEvQt7MkoFyQYhDggHpVAC_QRBkeOp3adrs-QYyajnkP8BRXo-YRzRa-9yzUG-U98a2l7N7CLRPA5GqQ2Cwi0gkJoeukAPpxxA-anAHz5NOPSsEEuvUn2vlBr98d7nj5NIVelZR3NQrl0jadX99VmEtD5ShX4CsCcJuFWdxlYC8rH6Z4iXaPSworwd3X6FRr_69wKXMPLHf__lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16229" target="_blank">📅 23:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سی‌ان‌ان: آمریکا و کشورهای خلیج فارس نهادها و مقامات مالی حزب‌الله رو تحریم کردن.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16228" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmwATtYKBhcgab1QGdeZhDqkwDPgwR_rSTaHeMvezex_fOkxcBazpp8SUVZGn0Q57khydObZ6f9lkjUIpan9UnR6zGzSXBKyJtZNty1hfUquwFJSMtB52V3tLtIh6LPg22UVMVRzUFo7C8zQuaL9ZaFjz-jjMmgrkqJ_UiWUy5XXUsQCQjg6y-s4Vs8IOknv2-irwWiKWENtVqRoWoK8ujB1ocImChU8h6rpVRdnC_aeLbilCvdDc0LUNFG2avRiKvu5EWoQjSOnb9aW590VB2b_t_8RhB-2tUH555ELabk_dns4AcvLXWhdBqgcPkTUDvl9Mk_ximsIIpbsTFnmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تابوت های آماده شده برای خامنه ای و خانواده اش
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16227" target="_blank">📅 22:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔸
فرمانده سپاه تهران : خودروی حمل اجزای خامنه ای به شکل ضریح حرم امام رضا طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16226" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در تروث : مایلم به رئیس جمهور شی و کشور بزرگ چین به خاطر پیروزی بزرگشان در قانون شهروندی از طریق تولد تبریک بگویم!
@withyashar
یاشار: ترامپ در آغاز دوره جدیدش فرمان اجرایی‌ای امضا کرد که می‌خواست اعطای خودکار شهروندی به بعضی نوزادان متولد آمریکا را محدود کند(پدر خودش با همین قانون آمریکایی شد چون پدر بزرگش آلمانی بود)، اما دادگاه‌های فدرال دوباره آن را متوقف کردند الانم  عصبی شده داره به چین تبریک میگه
😂</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16225" target="_blank">📅 21:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو در خط مقدم جنوب لبنان:
«حزب الله زمانی قوی‌ترین ستون محور منطقه‌ای ایران بود، با تقریباً ۱۵۰ هزار راکت و موشک که به سمت اسرائیل نشانه رفته بود. امروز، تنها حدود ۸ درصد باقی مانده است. اگر تهدیدی برای امنیت یا سربازان خود شناسایی کردید، فوراً اقدام کنید. منتظر نمانید.»
پیام ما به ایران و حزب الله ساده است: شما اینجا جایی ندارید. آینده لبنان باید توسط لبنان و اسرائیل تعیین شود، نه توسط تهران یا نیروهای نیابتی آن. هدف ما امنیت و رفاه پایدار برای هر دو طرف مرز است.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16224" target="_blank">📅 21:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر خزانه داری آمریکا : فقط چین نفت ایران را خرید
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16223" target="_blank">📅 20:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد @withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16222" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رژیم چنج ؟! محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16221" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=IkUky0-7wP7QqbU5f2rD5h7KUf2aNTUK8J93Itht3TLGdAucNEsATF0ZqUW8We0_-OoWgc3-oveRJdj3zRPdLjHrotlqZCRJev8ilw-4EvqVAoUYaqjCqc3LStKCWh8XpDC73QomdOJRxCl1RFK8VWWHeveFS7qdMglNlrb9YFuVyHTN_-8P8n3mhy5FWJzWdWeXvdMARr-WqDD5mL4VBR-l7K4KXHUji5q79KZGXiZsHmLxbXQNX-9J5SPbRm6_IhdVnSKTSyBaoBmggjfTJ0rexJgCMJ4JXMYy6cpaqE-pCNzu9qG7l4rmAomHbhoKWGmwd6-8nqhQYnitdEdYfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=IkUky0-7wP7QqbU5f2rD5h7KUf2aNTUK8J93Itht3TLGdAucNEsATF0ZqUW8We0_-OoWgc3-oveRJdj3zRPdLjHrotlqZCRJev8ilw-4EvqVAoUYaqjCqc3LStKCWh8XpDC73QomdOJRxCl1RFK8VWWHeveFS7qdMglNlrb9YFuVyHTN_-8P8n3mhy5FWJzWdWeXvdMARr-WqDD5mL4VBR-l7K4KXHUji5q79KZGXiZsHmLxbXQNX-9J5SPbRm6_IhdVnSKTSyBaoBmggjfTJ0rexJgCMJ4JXMYy6cpaqE-pCNzu9qG7l4rmAomHbhoKWGmwd6-8nqhQYnitdEdYfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل از رهبران حماس مرگ مجتبی خامنه ای را لو داد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16220" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خالد مشعل از رهبران حماس: مجتبی خامنه ای کشته شده
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16217" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نتانیاهو: اسرائیل و لبنان دو کشور دارای حاکمیت هستند و حزب‌الله باید از بین برود.
هدف از مناطق امنیتی در جنوب لبنان دور ساختن خطر از شمال اسرائیل است. ظرف هفته‌های اخیر 9000 عضو مسلح حزب‌الله حذف شدند.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16216" target="_blank">📅 19:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Si7DrojQPEuoaPz5a2quI4rAFbiVehHC-0-uugeSqk3RL0EpMTCcEfJ_6a6cSR0NJ0_EkAwVWsKd8tBMrDxDQKYMv6-46N5lcTg0CQcqB12ySdxxNkz6EU9LJcHeLiiY436wyRwFvItAYVaY7GXZ89KlUG-wAOingUbw3wVyTimY2Vk0qNv-eGCcPekPVKSQ8BX-g-BpWuR3Q8T3aiHoqTI5LzNJ0Z62VV6sI18gi_JhSJHRDSgr_li2yigBbLZebCHn-FpGRL6mCpMcTNj6uUL__ibVpQMC35o9J9fIOGiR3H1wOuqi3TLehriz4B2WvJGDm7Ln4TX5KiQXvY4Y2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: اولین آیفون تاشوی اپل هم معرفی می‌شود
iPhone ULTRA
اپل احتمالاً در ۸ سپتامبر ۲۰۲۶ از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و نخستین آیفون تاشوی خود رونمایی خواهد کرد. به گفته مارک گورمن از بلومبرگ، این تاریخ محتمل‌ترین زمان برگزاری رویداد معرفی محصولات جدید اپل است و در صورت تغییر، مراسم ممکن است یک روز بعد برگزار شود.
آیفون تاشوی اپل، که به‌طور غیررسمی
«آیفون اولترا» نامیده می‌شود، گران‌ترین گوشی تاریخ این شرکت باشد.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16215" target="_blank">📅 18:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juxL82F2PwSsihusWR09e-o-0LESDXfhLDmZn2-3DQR5dVgCCVrypsp--EMilS4ggzB2nezA9HSc2Y4b3xC0GDx7T8SxcP7i3QD0kWHNmGCziMSBkcCs0IHv2SDNRR52qCba3HFllogK2jpmgczCC6kT86vfBTQtqGt1RHgPaET25-f_Z4l450r9KbE6tGqTS8quTQAW4aNfbqF7pv6zwhIdlzWRcFtHce6kR4rw-vzV3bpJtbTnw2Bc5Nr_X9KPjp1-tbWp_uFgVTJYM9hekbjzu_03x_464j3BuWG0rCAAsCTVO1NjEGU3gwcB93PBQii1dez9jEc94GsayY5z2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
@withyashar
یاشار : منظورش مردان تغییر جنسیت داده هست</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16214" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxYggi4jUS371pEa85U8BqYJEI400TUnno3GVVCOF2jxuEOk3aEraVB54eLk8DAbXnoqTPYsJi6invErol2yaCwgL_3KT42qGiiACUI9aGQV_GeP5OADgbdEM2INAEsOexizABYp1wxTkYl3yBU6TkS9UYHJ8KUG989loSFysPUWbqO0SXYf3a4kHUCuXwDbeF3_IUAqcMN47aeU3dqjbPyQVNP28tm1NVtP6kFDNLquvf_EXgDUgCUb6DGbDMnpuzsNYLEfLO1AU_MvDNFX2VJUmcGJibEul-LH7q8VY4Xi2ATfTwyl06Qg0191Knn8iEUzMM3t86DosE_C8AWh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16213" target="_blank">📅 18:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رسانه‌های عبری : «پلیس و سرویس امنیت عمومی اسرائیل (شین بت) یک شهروند آمریکایی را به ظن جاسوسی برای ایران دستگیر کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16212" target="_blank">📅 18:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لقب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16211" target="_blank">📅 17:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وای نت عبری : یک هواپیمای مسافربری شرکت هواپیمایی الکترا ایرویز که با نام تجاری لات به سمت اسرائیل در حرکت بود، پس از آنکه دو جت جنگنده نیروی هوایی به سمت آن شلیک کردند، در هوا چرخید. طبق گزارش‌ها، خلبان دکمه‌ای را فشار داده که هشدار ربودن هواپیما را می‌داد. این هواپیما از ورشو پرواز کرد و در آسمان ترکیه نسبت به ربودن هواپیما هشدار داد. پس از آن، بر فراز قبرس پرواز کرد و پس از عدم دریافت اجازه فرود در قبرس، برگشت و مسیر خود را تغییر داد. مقامات ارشد صنعت هوانوردی این حادثه را بسیار غیرمعمول و خطرناک می‌دانند و تحقیقات فوری در این زمینه آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16210" target="_blank">📅 17:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آتاانتیک : اسناد منتشرشده نشان می‌دهد با وجود هشدار قبلی ترامپ درباره عدم استفاده از سیگنال پس از یک افشای جنجالی، مقام‌های ارشد دولت او همچنان از این پیام‌رسان برای هماهنگی‌های حساس استفاده کرده‌اند. طبق اسناد FOIA، دست‌کم ۱۳ گروه گفت‌وگوی سیگنال در نیمه اول ۲۰۲۵ فعال بوده که یکی از آن‌ها با عنوان «Iran/Ukraine Planning» به بحث درباره ایران و اوکراین اختصاص داشته است.
این گروه‌ها با حضور مقام‌های سطح بالا مانند مارکو روبیو (وزیر خارجه)، پیت هگزث (وزیر دفاع) و دن کین (رئیس ستاد مشترک) اداره می‌شدند و برخی چت‌ها دارای حذف خودکار پیام‌ها (۸ ساعت تا یک هفته) بودند؛ موضوعی که نگرانی‌هایی درباره نقض قانون نگهداری اسناد فدرال ایجاد کرده است.
در حالی که کاخ سفید استفاده محدود از سیگنال روی گوشی‌های دولتی را تأیید کرده، این اپ برای تبادل اطلاعات طبقه‌بندی‌شده مجاز نیست. با این حال، وجود چنین گروه‌هایی به‌ویژه درباره ایران نشان می‌دهد این پرونده همچنان در بالاترین سطوح تصمیم‌گیری آمریکا به‌طور فعال در حال بررسی و هماهنگی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16209" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTnW2EZgxuVUqyGCqaWHpY8lRsovm3fgrV58KwRD2E8c1Yer2mkVyYb2Mi572aUeZQoTMgH7lyNcbpZUSzIWGhMtQUOTZpxnGnQdUhtvXhWjZIiiD-GeRmnFH7iRHHkvx9kZEcB_vO95tXa_SbQVT0q9ziBIy4Zd0NSeE1oXvq-WqrLkjQWc-NCoeWgAqV17D80VO_Oqm214KJsS2-i1BWrXdV8CiLwVSl2gmrFQD14peRyPYvNxwjTFyrOIK5d4G-ecFkyQF0mJyodEezD-Y8Bm4eGvyJISj1Y-eapdgSaxohyV2yEdN5fKmzsSqBTCL_y-81p1wbCQwSO9Qwr-N04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1345ea8bef.mp4?token=oQLFuYN_8V-yKEDE7e0uGfqlAINFzWGG8DZaiDpAHx4mQB1wm_AlAZYHcDi2jrDgmVBd1BD4S3JH0yzN70X4UvFeSBAGZSAPHNfOuiAST1V9BjzY03lw1XaeIXEtW1FwfJXPfwlNB12_KJ01biIcDrTL-Gc0HtrC6cQHoEs_Y6ejy5w_6vscGirGepJAYSmdadVX8da3nv-oqiWix3czuStfDXyx1NdeG2zBQr67clD9rQT16FdSRdSt58UmiiEszpgQaFaQ587k81_7tTlCk0pxMLiFSvxeKXq3XJegoQpbU40MO_gNI__SmQXkNjPx3XSJjguWg4JCOZHNUixyTnW2EZgxuVUqyGCqaWHpY8lRsovm3fgrV58KwRD2E8c1Yer2mkVyYb2Mi572aUeZQoTMgH7lyNcbpZUSzIWGhMtQUOTZpxnGnQdUhtvXhWjZIiiD-GeRmnFH7iRHHkvx9kZEcB_vO95tXa_SbQVT0q9ziBIy4Zd0NSeE1oXvq-WqrLkjQWc-NCoeWgAqV17D80VO_Oqm214KJsS2-i1BWrXdV8CiLwVSl2gmrFQD14peRyPYvNxwjTFyrOIK5d4G-ecFkyQF0mJyodEezD-Y8Bm4eGvyJISj1Y-eapdgSaxohyV2yEdN5fKmzsSqBTCL_y-81p1wbCQwSO9Qwr-N04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت دفاع اسرائیل و شرکت رافائل در بیانیه‌ای اعلام کردند با توجه به تجربیات دو جنگ اخیر با ایران، سامانه‌های پدافندی گنبد آهنین و پرتوی آهنین را برای مقابله بهتر با پهپاد‌ها،راکت‌ها و موشک‌های کروز ارتقا داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16208" target="_blank">📅 17:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">روزنامه لبنانی المدن گزارش داد:
توافق‌نامه امضاشده میان اسرائیل و لبنان در پایان هفته گذشته به
قطع روابط دیپلماتیک ایران و دولت لبنان منجر شد‌ و عباس عراقچی در پی امضای این توافق‌نامه، سفرش به بیروت را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16207" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اتاق جنگ با یاشار : بعد از خبر تشکیل نشدن جلسه جمهوری اسلامی و آمریکا تتر شد ۱۷۲،۵۰۰+ و بیتکوین به زیر ۶۰،۰۰۰$ و همکنون ۵۸،۵۰۰- اومد و نفت برنت +۷۴$ شد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16206" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الحدث: منابع می‌گویند ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/16205" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ستاد مراسم دفن خامنه‌ای: مردم برای نزدیک شدن به جنازه علی خامنه‌ای اصرار نکنن.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16204" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:  فردا در دوحه با قطری‌ها «دارایی‌های مسدود شده» مذاکره خواهیم کرد. @withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16203" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsQViawrwquNmCmbgHKWp3iVINJQSkCNG9yIWLNZB7xQ9tv7kdkj-6YjgQy-jIw0Rbqfng437K2F2uaLqqn_kuTUhSKrsK_rMiwu_KlAnK6SL3XAncB7CEvqY5Vd1kVRtNf02hD-ZZoV0-PayLyJ10__goqLFxAUAb4XknPi8EjeCjiA1jCjqMiVoyK4vlklJVXCtweCd5uuO5QAQqbVEpO4ILUR-uRuximfckhR5TVlVGy88fbOnslo8HvTPLBUcnU7JNsijozMuV4oys7v2D1fw5yninOhK2nnNiE2jafZ0HJB1Nr8NHZcaVZd0DW4QB_lhjn2fjIlVqN2i8Zx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی :
کیپ‌ورد آرژانتین رو حذف میکنه
،
من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16202" target="_blank">📅 15:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی وزارت خارجه:  آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند. @withyashar
😂</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16201" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@withyashar
😂</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16200" target="_blank">📅 15:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FntClDTI_2qjvUOdKR2WgWBUFQR4x-W9tTDQ3_c96RcqTxBd7y4s-3eHsYwozi73d9fd1vnab1579tmvljz8AxR2fd0OCzXocp72vscgvr43tC7ayrB9PtNdipZqoj-Bg7NG1lJcl1xuUIw0pPiq0U0SJ2rRGx8cewmZV0zyaWWiZkmv7Fl9HGamX10lGmqZgal3LR3-di7EklkmYdcK4C8sIu2MahB1HmbrOVPB-r8MNZuAI6LKrSm0JOGWCCNGBIJS8mqa8BkwvXQH_0RqlK9gW3ijAjlhfXQ58Tt7Zs1biemrFF8lU__2-pjBO_LWARLuW63BB9W-Fn55LMhnIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر وایرال شده از تعزیه محرم
قیافه بعل یه جوریه که داره میگه خب عاشورا من چه کاره‌ بودم
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16199" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دبیر ستاد تشییع جنازه خامنه‌ای :
مجتبی بخاطر تهدیدات دشمن نمیتونه تو نماز میت پدرش شرکت بکنه و باید مخفی بمونه
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16198" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند  @withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16197" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر : هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16196" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWMverKVOEG9emXRR-xTb0t3AYIeE2IS_C_tG--4uti1hdTjtpS1dLtF-dK882vi-tPBWUXfEr1osBIEvnNnnfNanFDf4wK8zlYrJdQ1I0o-VJatLgAi1qxKqNQlS1Uv8sieIvxykdAB5qWc2KG7pz-qZ1qtcLhrwekUSNsoP9BwyXXqQh4EqDbdr3OwamImKybvLZxeW-Rs0_TCj_i4GwHmKHa6J1c1DPcQITKK9FLSdJKP2_pIQ3qLv-f3r3VuMW8VC5hDuiag0NZCA1LZQiLPdUvq0Moh4Sf0OcpHdCi6DeT_DXA6JU0yy2VbIhBURBd6U5yo5Mf8nA3QSr6ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی آمریکا موشک ضدکشتی LRASM را با بمب‌افکن پنهانکار B-2 عملیاتی کرده و در رزمایش Valiant Shield 2026 با آن یک شناور آبی‌خاکی بازنشسته را غرق کرده است.
در حالی که B-1B از قبل این موشک را حمل می‌کرد، تلاش برای افزودن آن به B-52 و P-8 ادامه دارد، اما B-2 فعلاً تنها پلتفرم برد بلند پنهانکار برای شلیک آن محسوب می‌شود.
ترکیب برد بلند LRASM با پنهانکاری و سنسورهای B-2، توان حمله دقیق و دورایستا را افزایش داده و تهدیدی جدی‌تر برای ناوگان‌های دریایی، به‌ویژه در اقیانوس آرام، ایجاد می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16195" target="_blank">📅 12:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر امنیت داخلی آمریکا:
پس از حذف ایران از جام جهانی رقصیدم
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16194" target="_blank">📅 12:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک منبع آگاه غربی:
ممکن است اسرائیل ابتدا در هفته های آینده وارد جنگ با جمهوری اسلامی شود سپس ایالات متحده آمریکا به اسرائیل ملحق خواهد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16193" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد که مارکو روبیو، وزیر امور خارجه ایالات متحده، توانسته است دونالد ترامپ را متقاعد کند که اسرائیل باید حضور خود در لبنان را حفظ کرده و علیه ایران اقدام نظامی انجام دهد.
در همین حال، جی‌دی ونس، معاون رئیس‌جمهور، ناچار به عقب‌نشینی از موضع خود شد و در نهایت اعلام کرد که از توافقی که با محوریت اسرائیل شکل گرفته حمایت می‌کند، نه از ابتکار عمل ایالات متحده.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16192" target="_blank">📅 11:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXlLBTY3grk5gAsopiNcDqsGW8s1AkieBBz2u9m9nIY_aDdBHGbe2uC5jsiTtSzxgU_Wsq4N7HkJYtF2BCY-hK0ilcIhedXHEbhq-bKuCIvcUvdt5YhOYEZQXL920XFq5Rzpo5hz9ms9JHTuItRixCmDGcV4tnkiWks46Nxmcd6Hczk7qkDlVYHwIGG-_A-PprB4vYuKECiL_9PNCU_GN6hblnn9PqE1eXFavZZSi6_WXox85V5Ec199gge4UbwHFL8bOmOjQ8_vtfOLvd5i3vHEzHO_ercc65TKIU5d5x-wcoa_LVBc6WkqyEetgdYBI_fnS8N2vBKwAFbhXuSi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ثبت شده از محمد اکبرزاده قبل از تصادف و مرگش
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16191" target="_blank">📅 11:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0rzhesJAuUNYohWY0uICi1_1OHDBCkZWH5p3DjLq7xfSrfVBJmi00f_tOBQtXzt4jknhm2HAxGJx8aMfy6ESzthEz7W_NYK3whcYwjfBZYsplUA0SDt2dhkT0DzAratUwkFq63DyF9gTJuDUGTu5bVp9X7eac0Zszh0r45Mo8ryAmFPrpsHf22nK7gsiD3PnYX6_fyQO87dbwx62-phDPcRx5UGx32-yP5t9HEp40ZUMt4aLg7DWpfmGy-ticAd9bCwVo9bMeYgVD9tvu5-GBVw0patewAAoOrmJW9mdYwRdpmExHeUNa0qzvm_Vg02trmjDQUjJhBKdRr7KiEFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان انفجار مهیب و برخواستن دود از سمت فرودگاه شیراز
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16190" target="_blank">📅 11:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسرائیل در حال آماده شدن برای شروع مجدد جنگ تمام‌عیار علیه ایران
بر اساس اطلاعات موجود، اسرائیل در حال آماده‌سازی یک کمپین مستقل برای آغاز دوباره جنگ تمام‌عیار علیه ایران است. این تحرکات نشان می‌دهد تل‌آویو مسیر جداگانه‌ای از آمریکا در پیش گرفته و انتظار می‌رود در آینده بسیار نزدیک وارد فاز عملیاتی جدیدی شود.
در همین حال، فعالیت موساد در داخل ایران به‌طور محسوسی افزایش یافته و شتاب ناگهانی این تحرکات، از تسریع آماده‌سازی‌ها هم‌زمان با عملیات مستقل اسرائیل حکایت دارد. هم‌زمان، انتظار می‌رود در روزهای آینده موارد بیشتری از انفجارهای مرموز، آتش‌سوزی‌های صنعتی و حوادث مشکوک در داخل ایران رخ دهد؛ رخدادهایی که با الگوهای تاریخی خرابکاری و عملیات پنهانی موساد هم‌خوانی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16189" target="_blank">📅 11:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد !
۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه
یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا نزدیکی سریلانکا به نمایش می‌گذارند
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16188" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=JPW_GwG2yNvqPykOWpY6d_1vT6OpqazNr2MKf0jQ6AMRNQvLTPfRDa-mBYmq0WHzlVjfo9kn9tEcpeeWhmfL4wu_7vRVamJk989P9G2PXBDro5qwVatAHFGb8qYwCe6QYkFYu12j1OKmAlDxX4Dh-U3KYeSTpISJBAEGs9iBTC_FOuNMa2AeHjugeUAvuuXFb1DBETh9qY-2PrdA8knHO05Wc3hnoPUb7d7v84Dgh0_yv9dTwNtqpVGhIk0uvS40Q-wZAsJYLmdbGMxF-TSe9KC6rgHh12SmgsqvtZz22jPYYjhedCPc3T8YWswIn8NEFfmPKlEC1oUXtJaUeL7PVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=JPW_GwG2yNvqPykOWpY6d_1vT6OpqazNr2MKf0jQ6AMRNQvLTPfRDa-mBYmq0WHzlVjfo9kn9tEcpeeWhmfL4wu_7vRVamJk989P9G2PXBDro5qwVatAHFGb8qYwCe6QYkFYu12j1OKmAlDxX4Dh-U3KYeSTpISJBAEGs9iBTC_FOuNMa2AeHjugeUAvuuXFb1DBETh9qY-2PrdA8knHO05Wc3hnoPUb7d7v84Dgh0_yv9dTwNtqpVGhIk0uvS40Q-wZAsJYLmdbGMxF-TSe9KC6rgHh12SmgsqvtZz22jPYYjhedCPc3T8YWswIn8NEFfmPKlEC1oUXtJaUeL7PVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنبریان سخنران صداوسیما: اگر ترامپ را قصاص نکنیم رهبر فعلی باید بدون شک تا ابد در مخفیگاه باشد
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16186" target="_blank">📅 10:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAE1xyKwLZJUK5thDyXyti0tiFD31DQnDjlhcZSFnUsBnSsM51ZppGBAf8gc5-mzGz9Eom4Qm_GpLWJE9i8KpHiQxmsrpy426mu85U2crUrSyA2fW_gQUP1IIzTQRw1JKJoEaEIHO_b7_3gXXUZoV08qhoW7Epu_c2Sz1GmKHURNVqyoxS5GGVy9pKYpUefYGoYeZr02DJGfVpydQAC4OXOusxbyBKEzw26MhNPerskSMYB1Nb4TYLkaC2Tzh1Qf4tQv7aEXN1mbgqeT_uJMgjS6nR0lxMYMwB-RDmwmjv5zLJj1eadIbPEa6SWbSqdFxkQ7rpz20BcjOefpaMadRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو نیروی سپاه پاوه ترور شدند
روابط عمومی سپاه استان کرمانشاه:
طی اقدامی، افرادی با تیراندازی درب منزل در شامگاه دوشنبه هشتم تیرماه، «برهان کریسانی» و «خالد خالدی‌نیا» دو تن از نیروهای بومی ما را هدف قرار دادند
در‌این عملیات خالد خالدی نیا بهمراه خواهر و خواهر زاده‌اش کشته شد﻿
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16185" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسناد محرمانه هک شده مادربرد و تراشه جدید آیفون ۱۸ پرو مکس فاش شدند.
بیش از ۶۳۰ گیگابایت اطلاعات از جزئیات کلیدی آیفون ۱۸ پرو و آیفون ۱۸ پرو مکس اپل به سرقت و فاش شد.
رویترز : فایل‌های حساس شامل فهرست قطعات و تأمین‌کنندگان، و حتی عکس‌هایی از مدل‌های در دست‌توسعه آیفون 18 پرو از طریق نشت داده در شرکت هندی Tata Electronics توسط هکر ها روی دارک‌وب منتشر شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16184" target="_blank">📅 10:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حزب‌الله:
قمار سر توافق ننگین بی‌نتیجه است
حسن عزالدین، عضو ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان:
صهیونیست‌ها مکان‌هایی را در به اصطلاح
مناطق آزمایشی
گنجانده‌اند که اصلاً جای پایی در آنجا ندارند مانند شهرک فرون.
دولت لبنان اساساً خودش را فروخته
و به دنبال فروش قدرت لبنان است.
پرونده لبنان همچنان در اولویت ایران قرار دارد
و جمهوری اسلامی ایران این پرونده را به هیچ طرف دیگری واگذار نخواهد کرد. معادله‌ای که تهران ایجاد کرده همچنان پابرجاست و ادامه می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16183" target="_blank">📅 09:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شروع حذف‌های هدفمند؟
دریادار دوم محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، متولد ۱۳۵۰ بود و در زمان سانحه رانندگی و درگذشت(دیروز)،حدود  ۵۵ سال داشت. او تازه سه هفته پیش، در روز دوشنبه ۱۸ خرداد ۱۴۰۵ معادل ۷ ژوئن ۲۰۲۶، در فهرست تحریم‌های اتحادیه اروپا قرار گرفته بود!
وی در ماه‌های اخیر در سخن‌رانی‌ها و مواضع مرتبط با امنیت خلیج فارس و نظارت بر حضور نیروهای خارجی فعال بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16182" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیوان عالی آمریکا امروز سه پرونده سرنوشت‌ساز برای دولت ترامپ را تعیین تکلیف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16181" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peHKa2Y6QkP0_FV7khSfntJ36JnGBzjoXa-MrDLE40L4M4rR07mPX6VKXnMtt7pTT-BWqcgSvAQD1_ygPjGFz1SsQdofwxswZBqAUktmRcSMSMSsKFgIZweVWiDJmVWGw7lDAyO0Ao8NnKY68qp3ZnngyaOUeFOz78crblMTP27jfziXkPqGrrUZt2vApnLE0MAS69biWcWS4vBxrQnIlAS8puy4-vKwc4ghr2KE7Sty7zs9VBjVpgOOeRa7_O8YPEqdUx_IB1y7u2rQnNSiCEgFRsBLkEH4C4JP4MJg7RY6_AUUihp2G1wIg9X2VtQZwFrilXW71Yp0jVXMsNMG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید روزنامه همشهری :  انتقام قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16180" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روبیو: احتمال شکست مذاکرات با ایران وجود دارد
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/16179" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به شرکت‌های نفتی: «قیمت‌ها را کاهش دهید - وگرنه مشکلات بزرگی پیش خواهد آمد!»
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16178" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd9p5oOXIdp-OD3V9tsDl0bT9-ZX7lYDNkhzXOxa09sjfUzvnyckz4FgXqUt4bxlGVr_zS7-X0K7Tuuv8STb0NiCv7e9i9v9L5MAGog_DD2T8NH90X5oyhUC8TwF0AhqnuSOgBygP1oT_hJwFBjN_RVTPzQLv6VA-m5hWUMpe4OHDjldnZzANS2pbyXnNnvC8jjRXMidm8Tq-_nTP0wAttZknRoHotvIm1h2LfdGF7EwUWzV-j291Weyi257ov8bcHkq90lMUoC0EGRo3Pt7v4M7TrbyImX1mP4UNt3esqNiyRxZaLtt-NAjZjP2vKWUpOyrrhpw2rl_wktGt4pIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار هدفمند در موناکو فرانسه
۳ اکراینی نفر زخمی شدند که حال دو نفر از آنها وخیم است.
پلیس در جستجوی مظنون فراری پس از انفجار «هدفمند» در موناکو است که شامل یک وسیله انفجاری جاسازی شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16177" target="_blank">📅 08:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله مسلحانه به ایست بازرسی پاوه در کرمانشاه باعث کشته شدن 3 سپاهی شده که یکی از این افراد نقش مهمی در قتل عام مردم در سال 401 داشت که به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16176" target="_blank">📅 08:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو : اگر از غزه خارج میشدیم، خامنه‌ای، نصرالله و اسد الان در قدرت بودن.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16175" target="_blank">📅 00:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZeoRC14YGUsNeFgTYTPO0_g_G78xiGbp2bNCd6GLgaR3drwg8XAtpRcX2JR-B4B6QWngF6iu6S7zREMRTGw5w3sHr5BTC0A_3hKYPmIxMMnhZa069NLQV46MPsekgscSfu5dJRPbDCe0AUVL1hSj-eKg2IxMMeJnAJlliSMYuAq70joErEgiSnn-c9eMxAG-XV0w1-TdIl5lbpFVKnzPwHzGJA_t_lmAEDEu5HoefISWmKX5TMTmcO1902T_ZUtwCJ6VaEQ5YcqIc276jKIhmPYofEnIq8yTJi8mL7VhfT4lfrirjP8-1fZudaDdlwjT-P_I554Azf6D0Epq3PUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سنگین اسرائیل به مواضع حماس در خان یونس
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16174" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k02V0cPfNH4Mpw6--rjeEZSI5fhml-Wr00-vugZKYdJAGQWlGvoHZKCoA-nUg1I96-H3N0q_Acqj-b6xL2IMKxKopBbgk9IdI1wBfCagbM7t2G5d-l1D-zNrT2XbXUVDGxm8sF52rWzE4_k0uW8u3fpMwU6_IXl_NMCnK8XSYNDm_F6GLNAROHQedeSTf21-ck3IZ4tSxwqN4U3zH8eO8PLHmsmyir_jypUoZUk-9BwoFRWw3zHPNwzIXdKIQ2McyZj2FBtF2-bcgm_pUykHpAxPlCLd6QgUfzvcyfNr1BmFXBXE5LVsw04IbOnosrkTJdQCcALXMDZYEIml94UkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید باور نکنید ولی؛
امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال
۱ میلیون دلار
پاداش طلب کرده بود و فدراسیون پرداخت کرده
۱میلیون دلار هم بازیکنا و سایر اعضا دریافت کردن
اول یک میلیون دلار (۱۷۰ میلیارد تومن) رو گرفت بعد نشست رو نیمکت.
نتیجه: حذف در مرحله گروهی در آسان ترین گروه.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16173" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر دفاع اسرائیل:آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده رخ دهد و ارتش اسرائیل آماده عملیات و هدف قرار دادن اهداف در ایران در صورت شلیک موشک‌های بالستیک در پاسخ به نقض‌ها در لبنان هستند،اسرائیل در حالت هشدار قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16172" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">موافقت عمان با اخذ هزینه خدمات دریایی
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16171" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=HbT775FxTWta2g8BWLP0eCJBGpCMgPQUoaHK2VuBHp6780o66hKk71iEDhdfJOkr-4zljjU6oHMFf1FfdgHudwhAFySX5ok8-l8G8C6RZkNpbxYjOPoGzirbzGTr2PkhcRzs6tm1UrtR9WzAiq4_DfNftH_ahNFNZkrGWTZHyQ2ApsCXjXGZQPxevwAuSz92WrXt3rG6qVOmwHJL-hzISirMMLv-1JK4u01kg8z6FoNCFCXTku9ysN16V29fHkhzkLMLGxJ7h-hhRwfQxeCOKwPJv_bxBYXcqozKXUI93mpifePAsukU4_BcjDx_8Oe1rkaAa99X0hk7APXVwdBaFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=HbT775FxTWta2g8BWLP0eCJBGpCMgPQUoaHK2VuBHp6780o66hKk71iEDhdfJOkr-4zljjU6oHMFf1FfdgHudwhAFySX5ok8-l8G8C6RZkNpbxYjOPoGzirbzGTr2PkhcRzs6tm1UrtR9WzAiq4_DfNftH_ahNFNZkrGWTZHyQ2ApsCXjXGZQPxevwAuSz92WrXt3rG6qVOmwHJL-hzISirMMLv-1JK4u01kg8z6FoNCFCXTku9ysN16V29fHkhzkLMLGxJ7h-hhRwfQxeCOKwPJv_bxBYXcqozKXUI93mpifePAsukU4_BcjDx_8Oe1rkaAa99X0hk7APXVwdBaFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ مورد کمونیست:
آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
این حتی باورکردنی نیست
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16170" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6615611a73.mp4?token=N2VNwwIpNA8glRvz1n4Nm9I0YaPPj4Hro0u6PyFxTRdVyxaFfkUEXjx4Fd6hc9EOkfRIYBw3ldqhCNeg1jmXbKAi-Hb436n1tPD8PNjQcXe7UzW3NBCUiW-etZUeEYKAev2Yh8cRKI35hPKS0aBl985acbQtL9VPHxRXB8-pGnx4JPobyIJmOt1qNrRJXPkTH08b2zOnbWO7KLLMhkKatZ_S6r9HUthdqscPdqI4Shcx0EWd2Dx7kmuONBe8djk01Kfy2XT78ExttYP7udNnCmCnHjaVtDZzqyLQTpQPU6suLR7_xLq__LaCaarVQAN0SOqJuKfekMdva-CIk2zUuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6615611a73.mp4?token=N2VNwwIpNA8glRvz1n4Nm9I0YaPPj4Hro0u6PyFxTRdVyxaFfkUEXjx4Fd6hc9EOkfRIYBw3ldqhCNeg1jmXbKAi-Hb436n1tPD8PNjQcXe7UzW3NBCUiW-etZUeEYKAev2Yh8cRKI35hPKS0aBl985acbQtL9VPHxRXB8-pGnx4JPobyIJmOt1qNrRJXPkTH08b2zOnbWO7KLLMhkKatZ_S6r9HUthdqscPdqI4Shcx0EWd2Dx7kmuONBe8djk01Kfy2XT78ExttYP7udNnCmCnHjaVtDZzqyLQTpQPU6suLR7_xLq__LaCaarVQAN0SOqJuKfekMdva-CIk2zUuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما از نظر نظامی در حال پیروزی هستیم. به نظر من، تقریباً از نظر نظامی پیروز شده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16169" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=P6O8oFrFn7pcOYcvig6MlTfkAHdmus0HxEYyJWaRIioXKI7b7qn2inMwQ6zODzm4mEMxboF0Cq0z5cbfd_nurXYJbmXVK41hwNyo_WBRKjAUHJgZva3Y0bdD0MEFDL8kh3i8dmfGVEiqQyNRFYeH-X_7S1BL8M8Vk_d6ukiw-FtbQA3LxMiEe-n_PeWqZuBtkZ0kK_dls8PYKdnO2Z_oFaCXE6eWe9_oQUGtzk5fBHHESqH2wnFXQBtvDEBFI4VsVfPkwQim15UqZ9nIYmiPRURMBwl8dGdK2RK6JcLfGy87DtHO3GHIAESl1e6wNyX5rQCMKmAJCODg-TFWXFJCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=P6O8oFrFn7pcOYcvig6MlTfkAHdmus0HxEYyJWaRIioXKI7b7qn2inMwQ6zODzm4mEMxboF0Cq0z5cbfd_nurXYJbmXVK41hwNyo_WBRKjAUHJgZva3Y0bdD0MEFDL8kh3i8dmfGVEiqQyNRFYeH-X_7S1BL8M8Vk_d6ukiw-FtbQA3LxMiEe-n_PeWqZuBtkZ0kK_dls8PYKdnO2Z_oFaCXE6eWe9_oQUGtzk5fBHHESqH2wnFXQBtvDEBFI4VsVfPkwQim15UqZ9nIYmiPRURMBwl8dGdK2RK6JcLfGy87DtHO3GHIAESl1e6wNyX5rQCMKmAJCODg-TFWXFJCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نشست دوحه شاید مهم باشد، شاید هم نه؛ خواهیم دید
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16168" target="_blank">📅 23:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال ۱۲ اسرائیل : وزیر دفاع اسرائیل، کاتز، دستورالعملی از ارتش اسرائیل بر آماده‌سازی «عملیات آبی و سفید» برای یک کمپین احتمالی علیه جمهوری اسلامی اعلام کرد و تأیید کرد که اسرائیل تا زمانی که «خلع سلاح سازمان‌های تروریستی» انجام نشود، مناطق امنیتی در غزه، لبنان و سوریه را ترک نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/16167" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برخواستن جنگنده از مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/16166" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=F1tIYeFgfER5oYmMP02_IEZI_4vK5IBwXK4nrL5wvFwe9jHcimR0iKS3w3Z9w0CtC7V6Qz6-WqxOthlZ2XR9LJx6sI7OvwsH7t-BhWeuRKPbQdFkPitbQhIkhQ9keyFVguy9FKstpN6VMN9n7ijLPsI9xXgmw4HBkGUMQTtx9Ho7NwtVZ-NHpluxYV9qb8I-to_1E9OQWTPtq5ZBNTNPQS6AMDxWsaLja-3efhyjSLa6WKwQ7gXv8cdWDu9oRyOevPyPkXk3jNhAdnTXUSsVKoc0XLoOo1vi6bbfKPMtLjuJ0-RXJQkxD4VyDfQaUd3_clZLmHZUg5zQv0PPXa0EX4xpXM8a6yxw6cG-XxuAIjKzZlrcoPyW0dCMt5KPkaZboXLCPXGcemKSSjwdJMM8nVdj00BlbcqifuqrVmehKK09ev-yL5qnk6ObIzP28hfQykgNmfUHIosZl3PFNz0lt69QQMTg38ThjT1pfuBgQcVj8klGVgb01WTRqep8Yk0O80omJ-lhV4FjsopTxCFz7I2VyolJGo6dYdo9rIM3Qc9msEIFffmlU38NNLjxxfy1HarlzVH1NaHVvKu29H-PEXkLmuem84S_q6daOtfAtTxv5iA3k1KsfReCrXOBIvuyZJLIOkrF4wDtneDK0AJSZ6CdRUtwZhGitx-ek6J7W6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=F1tIYeFgfER5oYmMP02_IEZI_4vK5IBwXK4nrL5wvFwe9jHcimR0iKS3w3Z9w0CtC7V6Qz6-WqxOthlZ2XR9LJx6sI7OvwsH7t-BhWeuRKPbQdFkPitbQhIkhQ9keyFVguy9FKstpN6VMN9n7ijLPsI9xXgmw4HBkGUMQTtx9Ho7NwtVZ-NHpluxYV9qb8I-to_1E9OQWTPtq5ZBNTNPQS6AMDxWsaLja-3efhyjSLa6WKwQ7gXv8cdWDu9oRyOevPyPkXk3jNhAdnTXUSsVKoc0XLoOo1vi6bbfKPMtLjuJ0-RXJQkxD4VyDfQaUd3_clZLmHZUg5zQv0PPXa0EX4xpXM8a6yxw6cG-XxuAIjKzZlrcoPyW0dCMt5KPkaZboXLCPXGcemKSSjwdJMM8nVdj00BlbcqifuqrVmehKK09ev-yL5qnk6ObIzP28hfQykgNmfUHIosZl3PFNz0lt69QQMTg38ThjT1pfuBgQcVj8klGVgb01WTRqep8Yk0O80omJ-lhV4FjsopTxCFz7I2VyolJGo6dYdo9rIM3Qc9msEIFffmlU38NNLjxxfy1HarlzVH1NaHVvKu29H-PEXkLmuem84S_q6daOtfAtTxv5iA3k1KsfReCrXOBIvuyZJLIOkrF4wDtneDK0AJSZ6CdRUtwZhGitx-ek6J7W6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیم
ا
: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/16165" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16164" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1RsyUTppcDMlw94qNcyh1wU4hppUYXTnjkkxGQT8Nr1xLWBZzDcCH7BaGb2GrcNc8_qRrR77aQT_UByY43CEGap9SprI4tpFm_K5ImW7ARv0DlrEKL__Ct2-MI4ru8L1iWdg9t08qQ6HcZIeh86bNEy8fXKYckKAbh9WCcAyD8ayUX1mqQHytrvPJhlhOY7h3Fz-ktxGoVCw1ciTI2_RE4gLzGQIXKIGRmm8Yov5K5oc3pJgGmdQAXFAqRYUiWlc6_8gZbNIK9YASwqwC5TaYXXwuOBv5S--YpOD2VOv9BgmHUMU63PluNrnchNWpbiFOwxCaPz7hf_QMyVvetCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون پیام هشدار سفر از طرف سفارت/کنسولگری چین
🚨
🚨
🚨
🚨
«وزارت امور خارجه چین و سفارت چین در ایران به هم‌وطنان چینی توصیه می‌کنند که در
حال حاضر از سفر به اصفهان ، قم ، مرکزی ، بوشهر و مناطق دیگر خودداری کنند
. لطفاً وضعیت امنیتی محلی را با دقت دنبال کنید، از مناطق با تنش و درگیری بالا دوری کنید، سطح هوشیاری را افزایش دهید و تدابیر امنیتی را تقویت کنید.
رعایت قوانین محلی، خودداری از حمل مشروبات الکلی، گوشت خوک و سایر اقلام ممنوعه در هنگام ورود، و پرهیز از عکس‌برداری در مکان‌هایی غیر از نقاط مجاز ضروری است. اگر امکان استفاده از کارت بانکی، کارت اعتباری یا چک مسافرتی ندارید، از پیش برای آن برنامه‌ریزی کنید. برای اطلاعات بیشتر، اپلیکیشن “China Consular Affairs” را دانلود کنید.
شماره اضطراری در ایران: 110
شماره امداد: 115
خط اضطراری جهانی وزارت امور خارجه چین برای حفاظت کنسولی و خدمات: +86-10-12308 / 65612308
شماره کنسولگری سفارت ایران: +98-9122176035
شماره کنسولگری سفارت ابوظبی: +98-9914240393
اداره فرهنگ و گردشگری چین در بخش گردشگری نیز توصیه می‌کند: “سه رعایت، سه نه” یعنی امنیت را آموزش بدهید، ادب را رعایت کنید، به بهداشت توجه کنید؛ سر و صدا نکنید، بی‌نظمی ایجاد نکنید، و قوانین را نقض نکنید.»
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16163" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16162" target="_blank">📅 20:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">معاون وزیر امور خارجه:
ایران به تنهایی عملیات پاکسازی مین‌ها از تنگه هرمز را طبق یادداشت تفاهم بر عهده خواهد داشت.
هیچ کشوری در پاکسازی مین‌های تنگه هرمز با ما مشارکت نخواهد کرد و از نظر اصولی اجازه این کار را نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16161" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک مقام آمریکایی: ما به ایران به‌روشنی توضیح دادیم که تنها در صورت تحقق پیشرفت در پرونده هسته‌ای، دارایی‌های مسدودشده این کشور آزاد خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16160" target="_blank">📅 20:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه با فرمول پس زدن خاک از اجزای خامنه‌ای وضعیت رو نگاه کنیم ، با توجه به اتفاقاتی که داره می‌افته، این فرضیه درمیاد که یه درگیری دوباره پیش میاد تا این تشییع انجام نشه ! و اینا مثل فوتبال در دقیقه ۹۵ ضایع بشن ! و هی زجر بکشن…
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16159" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سفارت ایران در قطر : قصد مذاکره با آمریکا را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16158" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68787096d3.mp4?token=vdo2DNAtqVqCvEHN-ojZe57rxKS-vbdtJD02GQmoEBObybWVi3ywMeY74jP5FCAO89aMWpAeSmjJ0Jh78_zN4Jm_cWkng-6BJGBNU8aKKNTOPiKvslM_qbxn_CRd7vAVlQuKmW2Jb5u3lZ4Ha_fPfmVGLKopD-ryQOOCK4Y5sHAwtJxe2l2y9_RFvwgvKA2TyqbS-1pyeooEfrpAO2dEO6GCC3uVEZ64OGebokJPHv_tjernO3_i0R47pcXFhfRgcPXoOeGLY11CWD4FsIccd59qbFRA8XVT8vflxyVU3dDegLNyGonm6G_h_8x2AfU70BXsbHzefCE7soaEphg5wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68787096d3.mp4?token=vdo2DNAtqVqCvEHN-ojZe57rxKS-vbdtJD02GQmoEBObybWVi3ywMeY74jP5FCAO89aMWpAeSmjJ0Jh78_zN4Jm_cWkng-6BJGBNU8aKKNTOPiKvslM_qbxn_CRd7vAVlQuKmW2Jb5u3lZ4Ha_fPfmVGLKopD-ryQOOCK4Y5sHAwtJxe2l2y9_RFvwgvKA2TyqbS-1pyeooEfrpAO2dEO6GCC3uVEZ64OGebokJPHv_tjernO3_i0R47pcXFhfRgcPXoOeGLY11CWD4FsIccd59qbFRA8XVT8vflxyVU3dDegLNyGonm6G_h_8x2AfU70BXsbHzefCE7soaEphg5wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در جریان سفری مداوم به خاورمیانه، دریاسالار برد کوپر، فرمانده سنتکام، با رهبران ارشد غیرنظامی و نظامی در اسرائیل و لبنان گفتگو کرد. کوپر و کارکنانش در لبنان با رئیس جمهور جوزف عون و فرمانده نیروهای مسلح لبنان، ژنرال رودولف هیکل، دیدار کردند. این رهبران در مورد مسیر پیش رو برای اجرای یک توافق‌نامه تاریخی که روز جمعه در واشنگتن دی سی امضا شد، گفتگو کردند.
سنتکام : بیش از ۵۰ هزار نفر از نیروهای نظامی آمریکایی در حال حاضر در سراسر منطقه در حال فعالیت هستند و هوشیار و آماده باقی مانده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16157" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16155">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزیر جنگ اسرائیل: ما در حال آماده شدن برای نبرد جدیدی با ایران هستیم که هر لحظه ممکن است رخ دهد و ما از لبنان عقب‌نشینی نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16155" target="_blank">📅 18:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16154">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔸
قطر فعالیت‌های دریایی خود را تا اطلاع ثانوی متوقف کرد
وزارت راه و ترابری قطر با صدور اطلاعیه‌ای اعلام کرد به‌منظور حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور به‌طور موقت متوقف می‌شود.
این وزارتخانه از تمامی مالکان و استفاده‌کنندگان وسایل دریایی خواست موقتاً از حرکت در دریا خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/16154" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16153">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
آمریکا و ایران پس از چند روز درگیری و تبادل آتش در نزدیکی تنگه هرمز، فعلا از تشدید تنش خودداری خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16153" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16152" target="_blank">📅 17:47 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
