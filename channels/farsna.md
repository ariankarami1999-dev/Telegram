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
<img src="https://cdn4.telesco.pe/file/n_f7BTl6uWhr2O8BBWoCIqkt-IHiqMJfOlZzQw0hA_SnLhzZQTQ5O6SdmZwghuLe0a3bpf6ejfgZm7Mo_bztLTqKLTAGagGEwtnfTW2GJba57meAilGt3bu_gmTeiFpIRu5W8mXxHUeGf6Zwd0dWYTOWMLWJ5KlCnSif-xiWuGKUVJ3f0cfXiePBA_IqsHjmdmgRpYBtvHHevK_UdpCnaigbfW2oJunKA0D7C_9d52IWqM3AOf84c5Dh_MtWZn2QJhYeRUYwHkUqcqlH2IR18fbdO5R5Ah1xBUWC9STKlJ1l_Hm3KPGPG3xq_I9V28QYQfjc3QazJzrF6QooF956lQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 14:48:29</div>
<hr>

<div class="tg-post" id="msg-458154">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pe4IHhso2zL6vJuSm0kcVcYuder7q7aPJvY6_EE8i6MS4shw4F5jr8gnmRjacsI_C7bLZ9YT80W3_WO8nrviI2MV_icOYebJc2u7ZSkdp3lTqUae-2vFn-G0ncI2NGVLJeEG270ZBa_gkS0FAn8fanbsmGyDExP7DH8kwqEE9cfxQ4tQooaX_dWpgOcrHvXY-7Utr_FxRgxgLiRO_6MEPeXgkL7pjTBd83BAodi_6o-_RVcNjuAchUViMWzkTrTW_nbqQFBiqkHTN7dYcq_op-pQMmpCVP4L39DkyYAPHv5vBnSQVdrXOAm-TDpm25AbzvJMQmKg4AWMzg8GJJANmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ از توهم هرمز به دریاچه کانادایی رسید
🔹
در حالی که توهم روزهای اخیر دونالد ترامپ درباره «آمریکایی» کردن تنگه هرمز خبرساز شده، حالا او در پیامی به سراغ تغییر نام یک دریاچه کانادایی رفته است.
🔹
پیام جدید ترامپ در شرایطی منتشر شده که پس از ناکامی مذاکرات چندین ماهه آمریکا و کانادا، جنگ تعرفه‌ای این دو کشور همسایه عضو ناتو بالا گرفته است.
🔹
او در پیام خود نوشت: «ایالات متحده در حال بررسی جدی تغییر دادن نام دریاچه انتاریو به دریاچه آمریکا است.»
🔹
رئیس‌جمهور آمریکا افزود: «ما انتظار نداریم که دیگر هیچ مراوده تجاری با انتاریو نداشته باشیم. از توجه شما به این موضوع سپاسگزارم.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/458154" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458153">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pubhvdDuefs3DxIA9GWlZVrJHtlwAy1agzUaChBmbxh3EpMWlSKovY5LUOnd9OxZjE7zB8YQSuJxLi6FfaD5abUlVKkaiRZWokvnRu9WUi_XV7FdPnCeBYSKvxACx0YyF9XXadl4OaUbUlVHi6kR70-g9ta87z5QKCuIZQg9riUHwUA5zM-JLlLx7hwCwh8xPuoTIZxJlCY1rvmrMJGGIv2tsvP6gPMT_j6bfqNXfr7dQBkV3I8L9g5z87EnJoD7HpFYx2byjj_bwv8NFDrUg0nv4H1Y30FIaW5hcgCa7L5DVPjiEMCo3ucc-6vOSmz7u_pwb6luAePGHmC4a5Ts0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: هر فشاری که معیشت و امنيت مردم را هدف بگیرد، بخشی از جنگ است
🔹
کسانی که میدان فشار را گسترش می‌دهند بدانند، ما هم برای دفاع از مردم میدان را در چارچوب منافع ملی گسترش خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/458153" target="_blank">📅 14:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458152">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZbBZqSPQETpoXQ7lgCHbq5h04PEhHJ_Xf9jOSC3AFdPCmpzip81jyXJ8u-6cRcJ19S0P-l92GTrfUvxOB32fyre-fr16eo_gOWP6sXiKFbv_3MWrxrmzPstw5GawdEu3w-Hl9pke8BfifVZ2OqWSjTrJWQkXYVp_YRu79bTRAv5qhujp0nkxuu83AbzG4IM5AeqPByw9KLK8mJ_x0hBay63vKODvXwYcD5PrC2ncs5RP9QB61x7BKr5-xYekligbaZ7bOhkhfoff3Q7BwvVtCI1V7F5RzT5Vu1Oovg8Mt8GpAwnefFEuxWk1pIlcv2dmSZjmspUGtEpfhtRpAxT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۶ سلاح غیرمجاز در مرز سیستان‌وبلوچستان
🔹
مرزبانی فراجا: در یک عملیات از قاچاقچیانی که قصد انتقال سلا‌ح‌های غیرمجاز از مرز سیستان‌وبلوچستان به کشور داشتند، ۲۲ کلت کمری، ۴ سلاح شکاری، ۲ نارنجک دستی و ۱۳ خشاب کشف شد.
🔹
قاچاقیان با استفاده از شرایط سخت جغرافیایی فرار کردند، اما تلاش‌ها برای دستگیری آن‌ها ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/458152" target="_blank">📅 14:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458151">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a487029da7.mp4?token=OfVSej94AlqzjyHb7KwXrrMlziunZhvOyT8sm4nETqg9yAG8ZlW2t8BoDOUorwcNtk33WHD_iueGmdi1yD7zXx_szwAz27XqvFEl2nyq-l7y9j4l1cm7M9MceS2kHsU2_WZOXe_wrzRf-gWQvIpw4VsKLKXYUHINHu7iPOwU2TT4dR2Pl9_1Nrbn3o4nRfTyMFpWsvLSzDKOw38yCEMfSTbPXxWhD948R3SXcef9Lmiin4tjZViojRJ0e4EOPJ3SADRpm1Z48459XuVbQDFYqegkYgOIIyMLnZQ6Ugj6cWxW0YuxzV1N2guDb4OGSjzEqC9li9WQq56DaVxycSLpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a487029da7.mp4?token=OfVSej94AlqzjyHb7KwXrrMlziunZhvOyT8sm4nETqg9yAG8ZlW2t8BoDOUorwcNtk33WHD_iueGmdi1yD7zXx_szwAz27XqvFEl2nyq-l7y9j4l1cm7M9MceS2kHsU2_WZOXe_wrzRf-gWQvIpw4VsKLKXYUHINHu7iPOwU2TT4dR2Pl9_1Nrbn3o4nRfTyMFpWsvLSzDKOw38yCEMfSTbPXxWhD948R3SXcef9Lmiin4tjZViojRJ0e4EOPJ3SADRpm1Z48459XuVbQDFYqegkYgOIIyMLnZQ6Ugj6cWxW0YuxzV1N2guDb4OGSjzEqC9li9WQq56DaVxycSLpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای در دیدار با رئیس شورای‌عالی قضایی عراق: همکاری‌های ایران و عراق در همهٔ ابعاد عمیق شده
🔹
رئیس قوه‌قضائیه در دیدار با فائق زیدان گفت: روابط ایران و عراق در بُعد قضایی و حقوقی روابط با تفاهم‌نامه‌ها و موافقتنامه‌هایی که منعقد شده، توسعه پیدا کرده است.…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/458151" target="_blank">📅 13:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458150">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RGNUn5ziVwduB6H7UueOdIk2-VtKAm3CKSrzcw9oncEmxfKzgkyHqTHO42QwIU4k88T1UXCMYAta4MWvkJwkYpC_AshKpO1E0G_5KTfbcuSWxg_5Vqnj5PKrlDSZ7JrYuqasRapS-tJIvVuEojttwVsoZHDHTlDBMt-Yrow1HfcmFqUExVxDnMlMi2WMtN1k0gyiM8_-GcpfRu8BTl2PBOcN1aEC76vWf-EKotrpMXYS8j_kl4oz6DOlIrGjAs2gdq4YQNDBMkkqHzs8bhPsBuo4BMArbRag0Zal4BPSu-Qo3uH5hCq2UaNqe7s3AgT1iiyanEOQh9BcVXrFYVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربانیان جنگ ترامپ با ایران در مزارع آمریکا
🔹
طبق گزارش فایننشال‌تایمز، کشاورزان آمریکا می‌گویند تبعات جنگ با ایران باعث جهش شدید هزینه‌های تولید شده و بحران مالی بی‌سابقه‌ای را برای آنها رقم زده است.
🔹
براساس برآورد فدراسیون مزارع آمریکا، تولیدکنندگان ۹ محصول عمده از جمله ذرت در صورت نبود حمایت‌های دولتی ممکن است امسال حدود ۳۱ میلیارد دلار و سال آینده ۳۲ میلیارد دلار زیان کنند.
🔹
این بحران در آستانهٔ انتخابات کنگره برای دولت ترامپ اهمیت سیاسی ویژه‌ای دارد؛ چراکه کشاورزان از پایگاه‌های مهم رأی‌دهندگان جمهوری‌خواه محسوب می‌شوند و نظرسنجی‌ها نیز از افزایش نارضایتی اقتصادی بخشی از جامعهٔ آمریکا حکایت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/458150" target="_blank">📅 13:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458149">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d8c64f97.mp4?token=ut4_5BlVDuCz7bvXq5JvIBaLxIwRqaVB1jDvYuGJdqD-pEeLQKENh05jdSo9mijytPg-LbyNrkiYWYdQ3J3DlCLnYUvOawqOInENqOcSPhXxyRP7heqF8akqd-E-91fIHjDSdFBd-ElquuferIy3xer-SfnR2aglaFSv9fn9wAXQXW2Dd4f5QU142yU7YrUmyzfAcSerWmuBmdIhOOeayOxGtA3CbQzsgzR48Q4OElgr1LItkDzWqoKdPWcUoSH9WRe_az-UKUsGV_ym0VeppC7SKmqgYHZsejqrS5odkcZUtiPC2bZeAFvyZPWXqMWY4kQZHo0Tptm62RShZ7Tu51q3YjeKx7XcFB7QfK2yX7CNk3CZnE8tmTXmAbSlRmf5lNkP438zD4nTDNTdqtf6ZR3j4kpbPKnPNrf22WdEQV0iVsmwZ5lbNlaUsYWSU_Bl8YIAUSYBQ9hFzIX1-JhDS5DpP4xHdlaWskBbHirXYh1Vkp59MBkua4mBOFd20Y50hjmVcaBa-tKFc389Rap4f1wyMvdYh207Dk89aeS0hftA-7eEiKU-PmWCt9xg2jrKBvt2-DEEw4q9FMPtbAN9Ey6S_aa1L2W5ga69fGTpYN3X_PFirrVnXHNqxZVgGm4ilIub3NgMteuJ-7ylB0j6ZU1dsp3sDkPvWrf-uxbIYa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d8c64f97.mp4?token=ut4_5BlVDuCz7bvXq5JvIBaLxIwRqaVB1jDvYuGJdqD-pEeLQKENh05jdSo9mijytPg-LbyNrkiYWYdQ3J3DlCLnYUvOawqOInENqOcSPhXxyRP7heqF8akqd-E-91fIHjDSdFBd-ElquuferIy3xer-SfnR2aglaFSv9fn9wAXQXW2Dd4f5QU142yU7YrUmyzfAcSerWmuBmdIhOOeayOxGtA3CbQzsgzR48Q4OElgr1LItkDzWqoKdPWcUoSH9WRe_az-UKUsGV_ym0VeppC7SKmqgYHZsejqrS5odkcZUtiPC2bZeAFvyZPWXqMWY4kQZHo0Tptm62RShZ7Tu51q3YjeKx7XcFB7QfK2yX7CNk3CZnE8tmTXmAbSlRmf5lNkP438zD4nTDNTdqtf6ZR3j4kpbPKnPNrf22WdEQV0iVsmwZ5lbNlaUsYWSU_Bl8YIAUSYBQ9hFzIX1-JhDS5DpP4xHdlaWskBbHirXYh1Vkp59MBkua4mBOFd20Y50hjmVcaBa-tKFc389Rap4f1wyMvdYh207Dk89aeS0hftA-7eEiKU-PmWCt9xg2jrKBvt2-DEEw4q9FMPtbAN9Ey6S_aa1L2W5ga69fGTpYN3X_PFirrVnXHNqxZVgGm4ilIub3NgMteuJ-7ylB0j6ZU1dsp3sDkPvWrf-uxbIYa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
ببینید
👇
✅
معیارهای پنج‌گانه انتخاب مدیران در شستا
🔹
محمدرضا سعیدی مدیرعامل شستا ضمن تاکید بر اینکه توسعه اقتصاد در گرو توسعه بنگاه‌های بزرگ است؛ معیارهای پنج‌گانه انتخاب مدیران در شستا را تشریح کرد.
@tappico1381</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/458149" target="_blank">📅 13:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458148">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0UoWdqBGkpvCSStCectjt9lYg04DcpqZzhqWhywWEDEZrHaB3DhaycLfekhTUvTJmA8aYCKP7dOEqndSiVZufnNKZW_yKYnHLD2-sT8MAm6sPwMmdvDcJ7PnbETHbrLqc1k5JDB2MGBOdeAcCaywohP9XwJXnntcZ5rkB9v0IhJAXd620F91z4kDVeiAs4Elwe4VtwjrvUhNNfHiAZC3tyEzIbbeaLLplWc6unurj_xjBdZt96ykst4V7ZZePTPKR2_Jct3B3VhqHIZrHm8asoIQCjuY9jiTnZL_VgHY58nCv_xjvcZGDQkrSR3O8OfPk7MuylSmcKtrHS-l0Ctew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
واگذاری سهام «سیمان تجارت مهریز» در فرابورس
⬅️
نشست خبری معرفی سهام شرکت «گروه صنعتی و معدنی سیمان تجارت مهریز» با نماد «سمهریز»، با حضور مدیران شرکت و خبرنگاران بازار سرمایه در فرابورس ایران برگزار شد. این شرکت در راستای سیاست‌های دولت در زمینه واگذاری بنگاه‌ها، توسعه نقش بازار سرمایه و مولدسازی دارایی‌ها، در فرابورس ایران عرضه خواهد شد.
⬅️
مدیرعامل شرکت با اشاره به ترکیب سهامداران، برنقش کلیدی بانک تجارت به‌عنوان سهامدار عمده تاکید کرد.
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/458148" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458147">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/458147" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQYNj54gp-uEhHrqpEVNFsL0GuKx47TQdn81WzmPpGdLyXkbavu4jcxlIIrHnSDV69yNro9Dysv_G8TingNU_533ylx1teY3_BUUlkgbKl-J1oJliNDQeJPbPsf1oUDhKZINJtU9CpKFLNb_S_3YkUMtmsKdeqMaWPIqq_A425CGWKlDJTRPD_-0kKMbNQ3s16WqzoR26husedYwzAvtAXLgaNvFKty7JntdeQz4H4fdmUy0CvgmtfKSlVhiU1QVmE_u7zlfunm2ZvdOlpTHnLDn3gmfb86YwnvdQy-epOL7Y35WZZcofrGkEvFf05crvdbS91D9CMHbETRRAiGAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای در دیدار با رئیس شورای‌عالی قضایی عراق: همکاری‌های ایران و عراق در همهٔ ابعاد عمیق شده
🔹
رئیس قوه‌قضائیه در دیدار با فائق زیدان گفت: روابط ایران و عراق در بُعد قضایی و حقوقی روابط با تفاهم‌نامه‌ها و موافقتنامه‌هایی که منعقد شده، توسعه پیدا کرده است. ما بر تعمیق هر چه بیشتر این بُعد از روابط تأکید داریم و در این راستا آمادهٔ هرگونه همکاری با دستگاه قضایی عراق هستیم.
🔹
اژه‌ای با اشاره به تفاهم‌نامهٔ تبادل زندانیان بین ایران و عراق گفت: یادداشت‌های تفاهم و توافق قضایی و انتقال و تبادل زندانیان میان ایران و عراق منعقد شده و بر همین اساس، ما بر تقویت موضوع استرداد محکومان ایرانی و عراقی و ایجاد تسهیلات برای خانواده‌های آن‌ها تأکید داریم. پارسال بالغ بر ۱۳۱ محکوم ایرانی از زندان‌های عراق مسترد شدند.
🔹
رئیس شورای‌عالی قضایی عراق هم در‌ این دیدار گفت: حاکمیت و ملت عراق در موضوع تجاوز جنایتکارانهٔ آمریکا و اسرائیل به ایران، با دولت و ملت ایران همبستگی دارد. ما هیچ‌وقت حمایت‌های ایران از عراق چه در سال ۲۰۰۳ و چه در ایام بحران تروریسم را فراموش نمی‌کنیم.
🔹
خون شهدای ایرانی و عراقی در مبارزه با تروریسم در هم آمیخته است و ما اوج این قضیه را در زمان شهادت شهیدان حاج قاسم سلیمانی و ابومهدی المهندس شاهد بودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/458146" target="_blank">📅 13:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458145">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YppLEocn6hwW1I23SDmhu8UGrVbxzTMPvUWTfPESrQmZL4a6-DFZknPuid5zXY51f-rPCCQdeph7dFw20y9Q6ZpLDTDJFz0Bjmy7AfC9Wpg2bO5VD6Rdsah_s22qAiEpukz7ssj5l6oetIrsl2FvVay72KFci_ZJ82D5opB5-CpdAz65t4RQ6Rw4uRXWDUkv8ZD7yFsrjdfp3lqGP5T_wHHNyRu9dFnhPS05f3-0UV87jYlluTdOiCHRV-iKOKZtD85bLs2QGXSV-MHkxbNNdp1TvBPbRWuOTB5Hw6icBbJeq7KwnqYM-ur_CKgw3Ga81C5MTaIMPEH6bvZDSE_sWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گران‌ترین بازیکن لیگ ایران مشخص شد
🔹
سایت ترانسفرمارکت در به‌روزرسانی جدیدش ارزش بازیکنان فصل جدید لیگ برتر ایران را اعلام کرد تا امیرحسین حسین‌زاده، مهاجم ملی‌پوش تراکتور با ۲.۲ میلیون یورو گران‌ترین بازیکن لیگ لقب بگیرد.
📊
پنج بازیکن گران قیمت لیگ برتر ایران:
⬅️
امیرحسین حسین‌زاده(تراکتور): ۲.۲ میلیون یورو
⬅️
اوستون اورونوف(پرسپولیس): ۲ میلیون یورو
⬅️
یاسر آسانی(استقلال): ۱.۸ میلیون یورو
⬅️
علی علیپور(پرسپولیس): ۱.۷ میلیون یورو
⬅️
حسین کنعانی‌زادگان(پرسپولیس): ۱.۶ میلیون یورو
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/458145" target="_blank">📅 13:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8OerPeIM3vECjmPmYeK0gA1lDk7nG2-G3gm8cC-ffxEuTHT5ZCkxeUybAq22xawnRIbPB8TSDG5rCvwuk18EYdJrvwoix7ewR_hO3NeFxv5fn96C5ejvLB2hZw0v-kBN6wq5yXbAaqt8uPa0YYtnxeTnXT9t5Nq7P33yTJ0AECqHaM-2_tzkB9c0RQW1zdk8u7EB7O7YT6gJjuel79-IW-r8jjjareeFQ8BgMsu0naFfcW1aLqxqyBuYs4OkLdPzm9qGcdV1zSY-T5WUodx8aR5be0zuU1MNc_VbkEan7jrJtvtyDViynbvah9N55CsDAmybMWyLBpuIo8i7CjG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: با تحریم‌های غیرقانونی آمریکا مخالفیم
🔹
چین ضمن مخالفت با تحریم‌های یکجانبه واشنگتن علیه ایران که افراد و نهادهای این کشور را هم هدف قرار می‌دهد، تأکید کرد که از حقوق و منافع شرکت‌های چینی حمایت خواهد کرد.
🔹
به گفته سخنگوی سفارت چین در واشنگتن لیو چانگ،…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/458144" target="_blank">📅 13:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
سخنگوی هیئت رئیسۀ مجلس: ادامۀ رسیدگی به گزارش کمیسیون امنیت ملی مبنی بر مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در دستور کار جلسۀ سه‌شنبه صحن علنی مجلس قرار دارد.  @Farsna…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/458143" target="_blank">📅 12:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXavLdFfbk5b52wUr9qQmBldLEJ2LxAZIv2Yrv6fHHlyEozDnrS7Xu0IU5KmaKVAM0MF4obAQbl7t7juSE6OsUwY43nttUS22X6BCZGT0RbvBcgvm0Pj7H5fweZLfWYl97-8SE2LOZA8jn55aWfU4VHn5tLr0F-trUoymaooAphx-Zj4MNewr-DPfpwXVjgyHrZd6tDv51SUTgG1uLnU-WR8whe9sytiH7c8Bp0hQgDUAp-rD5NeXyqo1aMPjuZnYvHCxLMwAmDRkYDMJpL7t9FjFuXlxepK79gqxIdChy1cM9eYqmpf5Jy_6X6FP2tNpzeVLskDc8Rn-2KfXRK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد تاریخی جدید بورس با جهش ۲ درصدی
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۴ هزار واحدی به ۶ میلیون و ۲۲۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/458142" target="_blank">📅 12:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ab6957ba.mp4?token=EKGqPoaCulfwkqD12UzK5nncVgel1bkqbwU0HelLWA342THhz1TIjBi6369YJXZMTUA-q2-SnVuLEna9amDtGS_1vWw_5BMy6ZEcca_dmvA7km2JFnw6zO8aNeodIgCpdMRYQ1K0l0474QaZF_3ydOJdHc5N-eJ0EOv1JjatrYAjLmX410CVKeUfkS8cgY5_eNhcYftuGofH0VUH_pwltdBB81HfdBNhxaoW_TSoNLMdVB07H8ohPFOxnELHxVT19wohOxS5m4dewZMFneiOhkUGPUnRhH7I3LaaARHwg4M1RgBB11IFZzrqTGUK4pMyO-LGrq_YnHB1aylbIV8AUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ab6957ba.mp4?token=EKGqPoaCulfwkqD12UzK5nncVgel1bkqbwU0HelLWA342THhz1TIjBi6369YJXZMTUA-q2-SnVuLEna9amDtGS_1vWw_5BMy6ZEcca_dmvA7km2JFnw6zO8aNeodIgCpdMRYQ1K0l0474QaZF_3ydOJdHc5N-eJ0EOv1JjatrYAjLmX410CVKeUfkS8cgY5_eNhcYftuGofH0VUH_pwltdBB81HfdBNhxaoW_TSoNLMdVB07H8ohPFOxnELHxVT19wohOxS5m4dewZMFneiOhkUGPUnRhH7I3LaaARHwg4M1RgBB11IFZzrqTGUK4pMyO-LGrq_YnHB1aylbIV8AUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: تا ماه آینده از طرح جامع تقویت اقتصاد خانوار در تهران رونمایی می‌کنیم
🔹
این طرح در ۴ سرفصل مراکز آموزشی و پشتیبانی دارد تا کمک کند که اصطلاحاً به‌جای ماهی‌دادن به شهروندان، به آن‌ها ماهی‌گرفتن یاد بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/458141" target="_blank">📅 12:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad6cf14bb.mp4?token=Tpw-qOqF8j1fEKcdYjsnFSZwjDJke5YOIi8e0G8Spp7_VLmaVOU5NKN9hlNvatxW8kpXGRoYzCp34EKn02mM8kc0dyq0Iv9BrbiAsXhnFkvD5Pr-0-kQNJ7aK7xEOBKvDb2Tr_R-lFvJ1BiDigEoi5uh9r1lMUsrbtx4wasby7Mq_mkrOD3Ldm39hYsnK2RrIpD1KwpYo230B15CXZO5y_4t57cG_nSq2XKs39z3BjBERZ8U4LzY6heXoRm88d0ZLvQr6HShXh8_Est2Nl7AjfvWIh5RNuYlLJcVJoYuYWndNWXjDdQHdVjqAM-z6CKai7PIJMMOGC5ckMl_N-ysRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad6cf14bb.mp4?token=Tpw-qOqF8j1fEKcdYjsnFSZwjDJke5YOIi8e0G8Spp7_VLmaVOU5NKN9hlNvatxW8kpXGRoYzCp34EKn02mM8kc0dyq0Iv9BrbiAsXhnFkvD5Pr-0-kQNJ7aK7xEOBKvDb2Tr_R-lFvJ1BiDigEoi5uh9r1lMUsrbtx4wasby7Mq_mkrOD3Ldm39hYsnK2RrIpD1KwpYo230B15CXZO5y_4t57cG_nSq2XKs39z3BjBERZ8U4LzY6heXoRm88d0ZLvQr6HShXh8_Est2Nl7AjfvWIh5RNuYlLJcVJoYuYWndNWXjDdQHdVjqAM-z6CKai7PIJMMOGC5ckMl_N-ysRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: شهرداری کنترل بازار اجارهٔ مسکن تهران را از چنگال سوداگران خارج می‌کند
🔹
۵۱ درصد تهرانی‌ها اجاره‌نشین هستند که بیش از ۶۰ تا ۷۰ درصد درآمدشان را خرج مسکن می‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/458140" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a323b1e08.mp4?token=Fs9-VaoSlUXKZBfa4qg7jxU0XhbsL-59U0KcC1_iE5xwaFOFwHHMlUrqJopt_JIEIOy8FspmwNMLK0cizwAAdwTY9Z0VwCz8c_jqo4StWh67mOJr8Ex0gan6lZ0SzloRMxY75ZRhjrEudyS3_jXHY6dsbKchfXeZHX4EXhoYmIL-M4VKLB_A4momtA1_UoUad6qvl-ItSs1kKNY64lZ_soz9U2-K1j8d7Nrb8WNFiwSv9VMmFaUPQCTimj4o8adZCurBs62Ho6Wo5RoDqMYoLDenDvFL1ub9cPSjW4V7TpOMsV5Bh7SttEJjpfI6mIQeaCXdE-EOo2nvgILcRIyMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a323b1e08.mp4?token=Fs9-VaoSlUXKZBfa4qg7jxU0XhbsL-59U0KcC1_iE5xwaFOFwHHMlUrqJopt_JIEIOy8FspmwNMLK0cizwAAdwTY9Z0VwCz8c_jqo4StWh67mOJr8Ex0gan6lZ0SzloRMxY75ZRhjrEudyS3_jXHY6dsbKchfXeZHX4EXhoYmIL-M4VKLB_A4momtA1_UoUad6qvl-ItSs1kKNY64lZ_soz9U2-K1j8d7Nrb8WNFiwSv9VMmFaUPQCTimj4o8adZCurBs62Ho6Wo5RoDqMYoLDenDvFL1ub9cPSjW4V7TpOMsV5Bh7SttEJjpfI6mIQeaCXdE-EOo2nvgILcRIyMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عرضهٔ مسکن متری تهران از فردا آغاز می‌شود
🔹
درحالی‌که بیش از ۷۰ درصد درآمد خانوارها صرف هزینهٔ مسکن می‌شود. شهرداری برای خانه‌دارکردن مردم، از فردا طرح «خانه‌ریز» را به‌صورت رسمی آغاز می‌کند.
🔹
قیمت خانه‌ریز معادل میانگین قیمت کل آن ملک است و افراد می‌توانند…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/458139" target="_blank">📅 12:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458138">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2af26a6d5.mp4?token=qgvVTAVLdoHDtC_99nSNQ2aC3Tx7VEDutpjqBLUGfm8EV3SaILSWgnr0BPV7mgMFKD61Q7YYO7FiBa5w9OqwN7pst8S4PPDqH585xyjAl0xfhJ5-i7OqTxtwrM-sWxHo1nf8-2YGxPPTRYkqhipYXWH1wOU9CBFibB31rLKx7D2fB0gwcwXwbhsoiHKhmXStGwx2zmwOsfImF4aJN09gpiVw2kfMZSmMa_XqJhALrT04q6Fr4s2TsePOf2QmabVVrAC4RB59l05V5M0NWzrGs_ltGsRffB__zbOBLxavUM1UZ4Tc9BynwAu2Yh5Y-TkavR8MBX9LHEAhdUKqsTjEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2af26a6d5.mp4?token=qgvVTAVLdoHDtC_99nSNQ2aC3Tx7VEDutpjqBLUGfm8EV3SaILSWgnr0BPV7mgMFKD61Q7YYO7FiBa5w9OqwN7pst8S4PPDqH585xyjAl0xfhJ5-i7OqTxtwrM-sWxHo1nf8-2YGxPPTRYkqhipYXWH1wOU9CBFibB31rLKx7D2fB0gwcwXwbhsoiHKhmXStGwx2zmwOsfImF4aJN09gpiVw2kfMZSmMa_XqJhALrT04q6Fr4s2TsePOf2QmabVVrAC4RB59l05V5M0NWzrGs_ltGsRffB__zbOBLxavUM1UZ4Tc9BynwAu2Yh5Y-TkavR8MBX9LHEAhdUKqsTjEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: کالاهای اساسی را برای دهک‌های پایین جامعه با تخفیف ۵۰ درصدی عرضه می‌کنیم
🔹
شهردار تهران: یکی از اقدامات مهمی که شهرداری تهران به‌دنبال عملیاتی‌کردن آن است، ارائهٔ تخفیف ۳۰ تا ۵۰ درصدی در کالاهای اساسی به دهک‌های پایین جامعه است.
🔹
در نخستین گام به‌دنبال…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/458138" target="_blank">📅 12:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458137">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c6340a4f.mp4?token=JMeYRhJixkQvas8vlSpVEP45mCFAaMcTUeerDTLpy5RdD16IVn08bY2vGL4uZuTqOxjQcpj2Euj-voWCf1qsO_gzUvAyocFatg9Bir28PJe4UUvqIwQRPKtsxtbvaStRGMjCayeMNMjnyNlAFsCIptf84Uz-6_sHSO1fP-keSyWzbOAArOUtCvmgRe2ERBTSJjtnVaBzTMl65v9TaUkwsF_95rQsa12CRyCXi7TJp2EUIi2TwsGqBixTUC1yv0Zb_VCnrSb6CWI4m4Nmy6hGiIMzWbMTof_xirqGTWNpZnSkijLwdrDpLF_Pi5SHXItGA31M4PBJtzfdLdK9LWRYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c6340a4f.mp4?token=JMeYRhJixkQvas8vlSpVEP45mCFAaMcTUeerDTLpy5RdD16IVn08bY2vGL4uZuTqOxjQcpj2Euj-voWCf1qsO_gzUvAyocFatg9Bir28PJe4UUvqIwQRPKtsxtbvaStRGMjCayeMNMjnyNlAFsCIptf84Uz-6_sHSO1fP-keSyWzbOAArOUtCvmgRe2ERBTSJjtnVaBzTMl65v9TaUkwsF_95rQsa12CRyCXi7TJp2EUIi2TwsGqBixTUC1yv0Zb_VCnrSb6CWI4m4Nmy6hGiIMzWbMTof_xirqGTWNpZnSkijLwdrDpLF_Pi5SHXItGA31M4PBJtzfdLdK9LWRYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون پزشکیان: رئیس‌جمهور به من گفت «آقای زاکانی یک اتاق فرماندهی برای پایش وضعیت مصرف سوخت تهران درست کند و من حاضرم روزی یک ساعت در این اتاق وضعیت را بررسی کنم». آقای زاکانی صددرصد پای‌کار است.  @Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/458137" target="_blank">📅 12:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458136">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f85e9480.mp4?token=bd7IWFMls6Pi8igvDQ1mlSOXOOXFarQuhjhX5ujHKiea6lepgN-GeIFQMyIduNUZE04srdg4TZnhXtcSfgR7wUmLQpmhdQ73Y0h5-FBKA0kVUZ6YTM086lE18e4Egi0Q7rBnf7DZ_9Jw3whd9VIRD1vRK8UwvP0fi9LBBcuUYM_GbLTo14tuNsVTp-2_eablHx7dPwRahsaHo8-DuUWPzsYh-o82tNCx-0IezwLVsO1tL9dOX2kA45TX2hGjYMlvjllwTa3lthPfrvbnTiCk47pNcC6yZoDevJVxApLeA8gp_97nSo0VPAOASy05BLGVlFEHxr_aoHD8LpVnFn9mPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f85e9480.mp4?token=bd7IWFMls6Pi8igvDQ1mlSOXOOXFarQuhjhX5ujHKiea6lepgN-GeIFQMyIduNUZE04srdg4TZnhXtcSfgR7wUmLQpmhdQ73Y0h5-FBKA0kVUZ6YTM086lE18e4Egi0Q7rBnf7DZ_9Jw3whd9VIRD1vRK8UwvP0fi9LBBcuUYM_GbLTo14tuNsVTp-2_eablHx7dPwRahsaHo8-DuUWPzsYh-o82tNCx-0IezwLVsO1tL9dOX2kA45TX2hGjYMlvjllwTa3lthPfrvbnTiCk47pNcC6yZoDevJVxApLeA8gp_97nSo0VPAOASy05BLGVlFEHxr_aoHD8LpVnFn9mPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقاب اصفهانی: خودروهای غیراستاندارد بخش بزرگی از بنزین کشور را می‌بلعند
🔹
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: بررسی‌های انجام‌شده نشان می‌دهد یکی از عوامل اصلی افزایش مصرف بنزین، پایین‌بودن استاندارد خودروهاست و حدود ۴۰ تا ۵۰ درصد فاصله میان مصرف…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/458136" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458135">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cdc7c07.mp4?token=G_qiUXnRrBNCDiXnPv2h-S3CoXlLCgn1-upoNGDRF-D95yBfPGq7guvwMyQt6hil6JxSs-sqOUjMXiFHaTc9H9C0v_UlbDk8GUDniCJcuf4pRRoAs8A-3ForVdpN9trvYxbPH0pTp7q_NGxJeuTFIsQ2BIRf1wzalREpTjum89022VL24pzN2yRVkuFkQuLYTCqBksZhoC6Ltxyhzk6Zhsl06xE_Ae8xjvn0vhwOV927ijCot739dDym_jbHGRezNUO1-a85ymNcgS_3om47wrLUul8GTKuNIjxC9RPQeV8Oq5-qj8xRbGmg9y0cA-yEqy7q5N4xHvvCJVlyL9eqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cdc7c07.mp4?token=G_qiUXnRrBNCDiXnPv2h-S3CoXlLCgn1-upoNGDRF-D95yBfPGq7guvwMyQt6hil6JxSs-sqOUjMXiFHaTc9H9C0v_UlbDk8GUDniCJcuf4pRRoAs8A-3ForVdpN9trvYxbPH0pTp7q_NGxJeuTFIsQ2BIRf1wzalREpTjum89022VL24pzN2yRVkuFkQuLYTCqBksZhoC6Ltxyhzk6Zhsl06xE_Ae8xjvn0vhwOV927ijCot739dDym_jbHGRezNUO1-a85ymNcgS_3om47wrLUul8GTKuNIjxC9RPQeV8Oq5-qj8xRbGmg9y0cA-yEqy7q5N4xHvvCJVlyL9eqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار فرمانده نیروی زمینی ارتش به تکفیری‌ها و عناصر معاند مستقر در آن‌سوی مرزها
🔹
امیر جهانشاهی: هرگونه تحرک، شرارت و اقدام علیه ایران با پاسخی قاطع و کوبنده مواجه خواهد شد.
🔹
پایش و اشراف اطلاعاتی کامل، طرح‌های عملیات رزم زمینی دشمن را خنثی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/458135" target="_blank">📅 12:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ee52107d.mp4?token=DP6tM-mXv65ltcbChyQT1MOSIpXqD1R_PTFQi_uYUegaHel0TPg_n6SVjjjOx_Njp27EfY5qfWVWZ-F7Uxzla9L8_K8aZaHgyRu7mPZgT7Q0xj9YXQGTEJRi8yDUjUKZ0WtBS4fWSJm1yF4-vRlV0ab5Ath3oPgjy0KkyHLXDXHznvrkGtOGVG6cBk4x0fmJvuFy-qyoXhzr2mbLalCHbLzlzPuSYih0p-gxjm2HsZZmmP4_5dyQwMVEyAE2Ttw2z0C09MsocMkU1Kk_RFuwcGj8i6iTbj2q1ywUxw-6Bjchr8w3lqh-cDioG0VmZeczzEk7ARO07pkyx4bfi71cPiXxJLm8EVOOdN2TMwTJLyb-48VNkUPl_QyV07TywNQ3jX_clQhphyObk2kiLm1SenfsZtZVNDUm5s87LIL-L5A-e6_3uSnRfRBZkanWjiSl_4b1CMMIzIqjXl3CHdPRq10RHbvzN2f1MfAypzRlnMgXCooN7Pf-mEN3W-qyDmqoqWGqYqP00wF3caq3rUUttgtWjPjmBysWesaUVYIRuQ_6mhdPru8gBbByV1h7EdC2YX0hraxbzsOn1r6gdrByBCNe-SfK288NI2GjR-q96o3HBYL7pMW-zD09eIkhsAD1yLqYc_S3bIUU6Q6uss1L3NzOC2quNuWp1vsWDeldy-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ee52107d.mp4?token=DP6tM-mXv65ltcbChyQT1MOSIpXqD1R_PTFQi_uYUegaHel0TPg_n6SVjjjOx_Njp27EfY5qfWVWZ-F7Uxzla9L8_K8aZaHgyRu7mPZgT7Q0xj9YXQGTEJRi8yDUjUKZ0WtBS4fWSJm1yF4-vRlV0ab5Ath3oPgjy0KkyHLXDXHznvrkGtOGVG6cBk4x0fmJvuFy-qyoXhzr2mbLalCHbLzlzPuSYih0p-gxjm2HsZZmmP4_5dyQwMVEyAE2Ttw2z0C09MsocMkU1Kk_RFuwcGj8i6iTbj2q1ywUxw-6Bjchr8w3lqh-cDioG0VmZeczzEk7ARO07pkyx4bfi71cPiXxJLm8EVOOdN2TMwTJLyb-48VNkUPl_QyV07TywNQ3jX_clQhphyObk2kiLm1SenfsZtZVNDUm5s87LIL-L5A-e6_3uSnRfRBZkanWjiSl_4b1CMMIzIqjXl3CHdPRq10RHbvzN2f1MfAypzRlnMgXCooN7Pf-mEN3W-qyDmqoqWGqYqP00wF3caq3rUUttgtWjPjmBysWesaUVYIRuQ_6mhdPru8gBbByV1h7EdC2YX0hraxbzsOn1r6gdrByBCNe-SfK288NI2GjR-q96o3HBYL7pMW-zD09eIkhsAD1yLqYc_S3bIUU6Q6uss1L3NzOC2quNuWp1vsWDeldy-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروسازان چطور بنزین‌ را می‌بلعند  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/458134" target="_blank">📅 12:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458133">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌ دانشگاه شریف: حکم اخراج رضا دالمن، دانشجوی اخراجی برای اجرا به دانشگاه ابلاغ شد
🔹
شورای بدوی حکم اخراج و ۵ سال محرومیت از تحصیل را صادر کرده بود که شورای تجدیدنظر ضمن تأیید اخراج، مدت محرومیت را به ۴ سال کاهش داد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/458133" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458132">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMAuT07vSjuvN5STVKT9ABBtS93M6Lh_RzvstzZ9FbVI1RMw5iHy-TfUXz3ijpqfpaz8r8Wff-ymxwYxIyAj-WfrHLdP0LnPMoa0rLn2lLJnmXRy8WzubPt_nhRdoBWWTfDIh_eKQFJee2hQSbVDr7L0AfYmvw-Ft-pEvlYzR66QmMZEsIaGxCPrTlhsyrPVWNWm6X7xn3inbUtjcTVG5GY8BVrmRb3BZcj3S-xTRT-W_XlQgVaesMIH2wgZfGXJDW6DsCTY7q3YHXyTDQmCGZMqmcaIxWtXvhceVSD6awRnf-2nEd-VM00ZSn7iXqx7wPXUlfZ2GSCM0vU2pIPeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی دسترسی به اسکناس ارز را افزایش می‌دهد
🔹
براساس تصمیم بانک مرکزی، از امروز کلیهٔ اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف ۵ هزار دلار و اشخاص حقیقی نیز با مراجعه به این بانک‌ها تا سقف ۱۰۰۰…</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/458132" target="_blank">📅 11:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458131">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxg7dC4BTtDpluBO_tk3-mHtcGYkh8BwTbPpRmr4GlQVgOiXzFTFH4V0Ua0MMaedTHyrnJnZQGBVJcEOCaA4BXZ44kfLv88FdxdErZaJRkL9VmP6NANbQBvSvSanYpxH9WEWTyjKDf9kk6soA1byk3PTSV0xhA1tdNlEiWxOUjZtcssnuuOzYuMCCrrHc-JWa_4YAu5CQlKVKfUtCZd1J9TWsEpioKuwJ6OFpB-e6aqOkO-eCeoHGhKE0Q53J4v89r5hFYBfpWMaL_-oPg0590z_TS1VSdMQBMpTByWyMck-YJ_qMNUl3hijtxd8_FOaHRgmCPKOWyY-TRTFDrXvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی دسترسی به اسکناس ارز را افزایش می‌دهد
🔹
براساس تصمیم بانک مرکزی، از امروز کلیهٔ اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف ۵ هزار دلار و اشخاص حقیقی نیز با مراجعه به این بانک‌ها تا سقف ۱۰۰۰ دلار با نرخ توافقی اقدام کنند.
عکس: مرضیه نورعلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/458131" target="_blank">📅 11:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458130">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=QuAMLM0dHgK4bycqY3sGg57v6LMduSXhIIkTwYTkxBgwX0DbDBZFGMPINcEGEX4Fc7wXy0FBM1tx8tW3Ar05OJ_ETTBZoukbhjSdAEbraCibSl0qvpzeIAxJ2dTwVfWLP8-AX-E0gdoP7L5F07A9rvbPiqnzayiOKFS4j0CWlAqndNbPzklNa8nB0mgtotA91EHiheKIM1YNAFV3UzaTc-1AcB0EEHA7FrLVFgNR6yADm6gGdi-ZB711XaIf04iiA1bdZcOfkfxL1fixXhMwZz3FYJZjR6s4NITmkLmyuLCjMTdbWlSmGVNQ3rqZgAnqs8bbiOWVWvaqlKLW3Q0vKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=QuAMLM0dHgK4bycqY3sGg57v6LMduSXhIIkTwYTkxBgwX0DbDBZFGMPINcEGEX4Fc7wXy0FBM1tx8tW3Ar05OJ_ETTBZoukbhjSdAEbraCibSl0qvpzeIAxJ2dTwVfWLP8-AX-E0gdoP7L5F07A9rvbPiqnzayiOKFS4j0CWlAqndNbPzklNa8nB0mgtotA91EHiheKIM1YNAFV3UzaTc-1AcB0EEHA7FrLVFgNR6yADm6gGdi-ZB711XaIf04iiA1bdZcOfkfxL1fixXhMwZz3FYJZjR6s4NITmkLmyuLCjMTdbWlSmGVNQ3rqZgAnqs8bbiOWVWvaqlKLW3Q0vKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد نامزد مسلمان سنای آمریکا علیه رسانهٔ نزدیک به ترامپ
🔹
السید: مردم درگیر گرانی بنزین، معیشت، درمان و جنگی که ارتش را نابود می‌کند هستند؛ نه ورزش زنان!
🔹
نامزد دموکرات سنای آمریکا خطاب به ترامپ: تو نمی‌خواهی دربارهٔ قیمت بنزین صحبت کنی؛ نمی‌خواهی دربارهٔ قیمت مواد غذایی صحبت کنی؛ نمی‌خواهی دربارهٔ‌ خدمات درمانی صحبت کنی؛ نمی‌خواهی دربارهٔ این جنگ تجاری احمقانه که اقتصاد را نابود می‌کند صحبت کنی؛ جنگی که در حال نابودکردن ارتش خودمان هم هست.
🔹
مسئلهٔ مردم در میشیگان این است که چطور از پس هزینه بنزین بربیایند؛ مسئله در میشیگان این است که «وقتی بیمار شدم چطور نزد پزشک بروم؟ چطور شغلم را حفظ کنم؟»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/458130" target="_blank">📅 11:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458129">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJEgTS4joszwm2PEHDu4RxKrpwtO6gQVxbfLep6_TG6x5AUC-SUKJi56dXn8CSFDTUf6hgoZRFC2VWgVaAuONWxWnDObBdE60_rzVISIPgsk8IQSd-dJjLadIaJEIdMptXBontO6GVjUh7c0WjP-9acj6Sdtqnbs_iyUgSJsp3h9Bnj7FK54de-PxDmDpnstW_EGMJDaWRLaRk6Rt1VuL4UNUUe4GKieyNe_LES3JeZdBps3Wo21iHQz8v51g-yI78wsj3gmm25md7jWCTe7KqNYj4sRVTW3nW3Z-fdVkHqYVWKnjlqT-THKarqt0Liq2ldjWyIV8EQd-hPFaNSw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر خزانه‌داری آمریکا: امروز شاهد افزایش ناگهانی قیمت نفت بودیم که من واقعاً دلیلش را نمی‌فهمم.
🔸
رئیس‌جمهور آمریکا امروز از تشدید اقدامات اقتصادی علیه ایران سخن گفته بود. @Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/458129" target="_blank">📅 11:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458128">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayl7CF1tAA3qB3BixhGUzeodmYkAK4QJUlwR_J5vILhFBwXzWu6acnPvCu0UT1qj-RjIZBO_XdbWHBFf0M7LuNa5US4x5BxUJMq8ChGCegrdsx0OV7za5Q1BBI2S2N2w1qC_eOT4FYRDZB70cowDayMi_mWTupXHua0lGgLL4ohgjl_VBOrSmXOyxKkq8bOmxxRZbYOK2lcYcSHVS9qljRp_lgp_qfvGLYkCmq1ggDY_TwuSQ5c0UkLnvfraYOeZo8YqUdD8ehjmZrK7OaAuLiHw8zNSEYDMZDe_HmRHr_JH6-_CPWLcWHB_CH7kUkQz54A6owbUHVT8duZgMmnM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه‌آبادی: تلاش کردم ادبیات ترسناک را ایرانی کنم
🔹
حمیدرضا شاه‌آبادی، نویسندۀ «تابوت سرگردان»: ادبیات گوتیک و ادبیات ترسناک گاهی این امکان را فراهم می‌کند که آدم‌ها با ترس‌های درونی خود مواجه شوند، آنها را کشف کنند و به شکل ناخودآگاه با آنها کنار بیایند یا آنها را پس بزنند.
🔹
می‌توانیم بپذیریم که اولین مواجهه‌های مخاطبان نوجوان ایرانی با ادبیات ترسناک از طریق کتاب‌های خارجی صورت گرفته و سایۀ آن را قطعاً می‌بینیم.
🔹
حتی خیلی از نویسندگان ایرانی که داستان ترسناک می‌نویسند، تحت تأثیر کارهای خارجی هستند و همان فضاها را گاهی اوقات تکرار می‌کنند.
🔹
من به سهم خودم تلاش کردم که این‌طور نباشد. سعی کردم جهان داستانی خودم را داشته باشم و فضاسازی‌هایی داشته باشم که یک‌خرده رنگ و بوی ایرانی داشته باشد.
🔹
مثلا در «تابوت سرگردان» ابتدا با مراجعه به «عجایب‌المخلوقات»، مدت‌ها آن را نگاه کردم و دنبال یک کاراکتر ترسناک ایرانی بودم. آخر سر این کاراکتر، «افریت»، را پیدا کردم و انتخاب کردم و آن را پرورش دادم؛ یعنی سعی کردم یک چیز ایرانی باشد و از دل ایران درآمده باشد.
🔹
خیلی معتقد نیستم که داستان ترسناک می‌نویسم؛ از عناصر داستان‌های ترسناک برای بیان قصه‌هایی استفاده می‌کنم که خودم دوست دارم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/458128" target="_blank">📅 11:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krA8VRA69QfG6PPQaIjNj2WPNgTHivK8c8oVAfxpcKuRTfpq8V3-41lGqHRyocIjkM874yLBh3i3CbWh5_yPJTpiuOknL_4WP02QotUXc9-rmvv7T5gEwDllrOKhPP_XhIVH9v9Gd0ziD5ByosWjZfJlk8mJKZUlxDENcMSeZrGVBnicjU9eZ_qV5Q3m7tyoniV5HZCIg9eHK7_Enx2FJ-q9zN09Rwl6O-3FWKD-ZzjZ7sdDcDBQaJoHwSnZHyxdk1MEBr9_rIWPiZWutQA17ffadgGbtY13qSLhSKoO7WquLMVizksq4Ht0u7rQ6mjhNjfunJspO6JrL3a2_pahjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک بارشی پایان تابستان در راه ایران
🔹
بررسی داده‌های امروز هواشناسی نشان می‌دهد پایان تابستان در ایران با الگویی دوگانه همراه است.
🔹
شمال‌غرب و ارتفاعات البرز با افزایش ابر، رگبار پراکنده و احتمال رعدوبرق روبه‌رو هستند" درحالی‌که شرق، جنوب‌شرق و بخش‌هایی از مرکز کشور شاهد وزش باد شدید، گردوخاک و کاهش کیفیت هوا خواهند بود.
🔹
همچنین ارتفاعات سیستان‌وبلوچستان، کرمان، هرمزگان و جنوب فارس به‌دلیل رطوبت دریای عمان و خلیج فارس، مستعد رگبارهای محلی و رعدوبرق هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/458127" target="_blank">📅 10:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXq4J0B4G2AOvoIdARhW3Mfozoa82mFn_ZqY0iOBTIEyV0xbrR6Itoo6RJJ4FWXPOi0gQ1MD3ODzSzxpvF6aa8PTCcxD17gVqiLfympNKg7Y7fuSkwvFqoqU2bcNBSuL2M_QT6l5Cbs626AQaBVZbrMkyUoNCWYbnGh1TVGcBZ0js9ZAF14hElDXzIbe1tO3YvLts9_tJZOHmxJPOTyEx5Gu__feRVyP13Thu8SsOyyijQmumknqKPDkbhGuz-rRQq5jrMJK1hEN0S3-xhJr6AYg_qEy8K_DPqPwJXyJdhb4OwtGian-8krrxHLQU5mKGkUnt0Anjax9qJPD7SAxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایش توان فناورانه کردستان در حضور معاون رئیس‌جمهور
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کردستان و همزمان با هفته دولت، از دستاوردها و توانمندی‌های شرکت‌های دانش‌بنیان، فناور و خلاق استان بازدید کرد.
🔹
در این نمایشگاه، محصولات و دستاوردهایی در حوزه‌های
کشاورزی، تجهیزات آزمایشگاهی، سلامت، خودرو و ماشین‌سازی، فناوری اطلاعات، نفت، نیرو، صنعت و معدن
عرضه شد.
🔹
از جمله محصولات ارائه‌شده می‌توان به
پودر ثعلب، فیکسچر دندانی، دستگاه کشت خون اتوماتیک، سامانه هوشمندسازی گلخانه، کربن فعال، بذر هیبرید توت‌فرنگی، تجهیزات هیدرولیک و آفت‌کش زیستی
اشاره کرد.
🔹
همچنین چند شرکت فناور استان، نیازهای فناورانه خود را در این نمایشگاه مطرح کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/458126" target="_blank">📅 10:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سوم شهریور روز ملی ارس گرامی باد
#منطقه_آزاد_ارس</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/458125" target="_blank">📅 10:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/458124" target="_blank">📅 10:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaBprAFs4X8ZUj1zZxypLZHR_Ps3L9QIHwdvCITmYAcJbSlwLmXNyE9MLCD20L8HRO4Vj16HWd8aR_ctrIwdkaHLaZV9v9vgbCDIEbxoWQ9iSqRcMZlpKLSuydUFzfpY8m_YW4HlSvt_b_6gDG8ZKsnW_8eSlSbsIlhJHmCoIAgNKJPxuLiheahUqYV7JXFVIiyREhLQTT4Scd3d46j-554jb1I_D4zu1cbvyeOq_IMVWIFsya0XKInVDR8-Z1gedE9n2zgUr7HvYfmvZ-g48JRsZTe92szaRN8ZyRguYoFaXThLsnnnjcC0hSp2FdjarqWNMag0B_eSS9wytWXq-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: با تحریم‌های غیرقانونی آمریکا مخالفیم
🔹
چین ضمن مخالفت با تحریم‌های یکجانبه واشنگتن علیه ایران که افراد و نهادهای این کشور را هم هدف قرار می‌دهد، تأکید کرد که از حقوق و منافع شرکت‌های چینی حمایت خواهد کرد.
🔹
به گفته سخنگوی سفارت چین در واشنگتن لیو چانگ، «تحریم‌های یکجانبه غیرقانونی آمریکا هیچ مبنایی در حقوق بین‌الملل ندارد و از مجوز شورای امنیت سازمان ملل برخوردار نیست».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/458123" target="_blank">📅 10:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsT_i6dCJ6aF2TzCTELNHZ4GSGKxcbE0VBxp2m2Ptbe9wYQWd5AttEG1rEP6rBv9zOkOBYxOvMZ2C_-qCXaUYhozjv-3E3NldEOjCdfpCrmo2FADT41i3VkNUXzXBfieg5QteajNdzWMwdSujpjJYaUYN5a9G4nEnEAqBBuynAelmTEgtWuxH2zDAVojKSNIAUeGNI6Uawc3Zk3HUtXKixDFNT9oq-BP5NTF1jZnwIJxnMUIPGJQIfTacKS6Yi6rdMu-qcCLB4KccSTWVMCDmjZMTm6gjpgxeN7eBHifM4-yJTkDZMPZjjcypkOG3QgwP3JktcLbOA8J4Y8NEIZpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
افتتاح نیروگاه‌ خورشیدی ۹۵ مگاواتی در استان تهران
🔹
پزشکیان: انتظار این است در دو سال آینده ۳۰ هزار مگاوات را از طریق انرژی‌های پاک و تجدیدپذیر تولید کنیم.
🔹
با دانشگاهیان و کارشناسان حوزۀ برای کشت گیاهان دارویی در کنار نیروگاه‌های خورشیدی و استفاده از…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/458122" target="_blank">📅 10:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFWYNraFy7NG2JWEsj16sheZetmbchZsYfacAlGZLvNr8Zd3HJAKnfTh8n_TG2xhzlnsu_80flZWOFqQqN6TiLekxyXxGXrNmfGEAqAED2oKrABOTLYvgLYQ1j_SPVAHcbsTCO9k-DPbgk2oVHl7tGwArY292H97uDs567Fooz1fDTbTMCZwRjmzjbsDC2S4lEP9mZ1O8nQpVuUToRRXD0psnmELcGkJfe6c8ozqYnZi4ontUyWEtWHWRZi1gJ5KPQN-NVy2yenjJ8mWD4Mw5pCGkUuXEKBaXk8GmoWZppv3Ddil7eEvE142umS5TIvPGCM9z8_Ts0kNwCW45ySrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwxVn7uCy4-eKGWZ0DHuxL0pjG_gfPJls5THV33eAb51SFuU4yIfWymDQEtrhPp1vV4hD8f0nQCdRZuKgIWkXzGhJJx-STTaeSxkclv_8-rSHopMpIqr-c6WFTotEAl99p5B5BMLeI0a59pqfW7w58OhFcyGW6STR24MIKJynDxP3ekLou4KeAHxIzBKTGBoE2Mmh19MmE2QoD_AJpFXLTFqNCDx-wRogmOpU9bgKM-B8CGP3vi4T_o0uosVm_EwO-_z-L7B9MkcCCAbgYYTbsVj4WBhXfy5yZjzWYjNtRD1PO_CyV_G5z73_Z8dDhZBC7doKQX3_H7k2AJ3xabs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDZpltJynOYUHUMNrtTahXAy8I_gk_jz0h_swlJ1J3dP6G_3ClAU2QRcJAcYAcljkeJBuVyMziCpQ6lK8DQe6Un1njvx7_Vt71enj8jyLuJa4ZzObVfUwjLOcwm_Lwxkzsp8APXWg4D_BRYfqovBUZGXNkKV1yVXEUOpsG-VrPqLX9T80o-Na_YIuZC6ZV8Ba116zzyA8s6M8NNIClwfdQd_tX4WeI_DEUhOMm5gLt4IksfuSwHaEUj9DbMb7m_6AYAAUAZUue101VyKW78Z1ZevdSEYCcxhRiz1zdI7uFMXxK_vsBxD1DSM-DoFcPu5yOAA0Z2Lxjda0eCBcQkvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2vlFVFxNBvXHkPLPupr6uuuXZ1gcQjmT7qaHbxxLuA4cgJseL3JJnNtC0851HV_Y3zk7iA5wUNi0-J9epklA6LA7GnBcYVrqy5eGzbnScST7N9AKIga5yOhibq1GjWZGcQbYKhqYQqxQdAGoyPCEqum5-xdxESCTTbGrqx209cIr4zvxPzDESptuEKOmGL5S_eWnWoYab5MVSVhIRX4Pq4uZznmzRXMWbsK5QejcUsMR-Fh2njdcpssvcW_oF3yz4enm8W8iuOsjYo9SbLOGP8rZxTs_PDWsrIYo3y8TWNtOhoNhg1m5apGFBffMsnAbs8NgOzizRbs3XUAxLDE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBk-48wPrqlcFQs_S1HVfVOlzW_3OXRGY_ePmtSuGXYtS85yWTIAPI48r8CyOIGbk5P4LKOxEMVYd6cu-T2Oe9yxPhUpMsvrJP_Aq2QKhBDsXnQADVQG_HXVfk8nDbdsQnJkAl4ePM0Mpmi0MngLyQ_SDsWCh7S8starCxxwvucQPrlt7kCYg8F3U4u2mnt0hRW9PI_KAQgHHP0KYmw_4O4Zfn9S1kxRFurXrRjxafFcDsaD9-7ggBoCVYr6xMP2opj-1nTi8Ed78CEjWKT3PVkQWDKow4nB9KuK_0Gzz_jbJ5pn3nf9AgDNa7lxYJLfdDMw-i88IB8GopGJ3oty-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-63KSZXK0x6f5MdtBxHxW7sWHMTGqGo18Habsktc9ZVi2F3mLme2mZ1OZHzadyHqoh42jKLmH18O5nMR89r5ZN3Lu0C-Pt1L5217GKeGTY3WauDPsnR7O6u8fthJNPf-nZlJQ831nDK5fPD1b0M4A8jL750ecFV_O_P5poSUgSOZ8YYhxcd0BSLQkevgbmYTjNsA4uJyQyC9s8Gv8qZ0xB-_yCEQP1kzn0wCGGI17oH2LlgHXgBhdhZdg7QtJXDrvePnt6GfTc1IFnKcGpgr3zUzNE4N_zYi1jKMjN7s3jlwQ7yot62WrfYIh0QpJbIquiY-4fZTsZrFrrdg-naWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افتتاح ۶۰۰ مگاوات نیروگاه تجدیدپذیر در کشور
🔹
سازمان انرژی‌های تجدیدپذیر: ۶۰۰ مگاوات نیروگاه تجدیدپذیر در قالب ۱۰۷ پروژه در ۳۱ استان کشور امروز افتتاح می‌شود و ظرفیت نیروگاه‌های تجدیدپذیر کشور تا اوج بار سال آینده به ۱۲ هزار مگاوات می‌رسد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/458116" target="_blank">📅 10:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bab7fd852.mp4?token=RAjPWkLDTz6VDZnbvAAMzz1dH7RcPkgn_W7jRrMZXViT2hlo5Pdrawoxg2f-8E9uONm7WWOjPypT6ThmavMTjVmrOTpLvdH1_36HLatTlcoHyAboObx2TaQfURkexCcq1AkWnq0re_d8FEDPZyR-ADPxUP86nxUxNC5WTSlYLEJRqLaLGgWrdeST3c0-GzBG9rsWzgKE7l2uTfyiZDnAbMHQ_BxkipJo1gV1dXGHpUFzqbdMhISqwP_jE5AoW89mplPFLj1yHBbr3B9MYjbHPq2v4dshZMlHZFiLxyUIr4pAbHJQGRqkjeKJAflZqH07UROAswRVY3gCxJf2mjkRmY5OdjNa6sJLQb3rU5ofadJDti2uWRiJwNs6dYbioyRjh9UfufFj5cIoTnKTnxI-dGPSnDFcQJNsyT4jzS15aO3gAlhGkeyrpZhm4HSgXMcWe-fDbmSOlQpM3TtCRcWAQDerWAM6jcXofpXLm4sIxqRcbYBZka-CTz6F1liF-4Q9emkzaLFtb8Dp_oswl_R5fY11UcquOBQTe_w74Iv_z6gOKlsNB7KmP0HPXvSB-RpGfDXxydJESe9mKOOIXV4bQ8pULSFLp9dB_GQOna0wJdH5ls5I1oMtidPbEdAz_PLqqK10-y7ua9L9zat86VsYVjyUo1Hi7NZvhlF-csrpce0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bab7fd852.mp4?token=RAjPWkLDTz6VDZnbvAAMzz1dH7RcPkgn_W7jRrMZXViT2hlo5Pdrawoxg2f-8E9uONm7WWOjPypT6ThmavMTjVmrOTpLvdH1_36HLatTlcoHyAboObx2TaQfURkexCcq1AkWnq0re_d8FEDPZyR-ADPxUP86nxUxNC5WTSlYLEJRqLaLGgWrdeST3c0-GzBG9rsWzgKE7l2uTfyiZDnAbMHQ_BxkipJo1gV1dXGHpUFzqbdMhISqwP_jE5AoW89mplPFLj1yHBbr3B9MYjbHPq2v4dshZMlHZFiLxyUIr4pAbHJQGRqkjeKJAflZqH07UROAswRVY3gCxJf2mjkRmY5OdjNa6sJLQb3rU5ofadJDti2uWRiJwNs6dYbioyRjh9UfufFj5cIoTnKTnxI-dGPSnDFcQJNsyT4jzS15aO3gAlhGkeyrpZhm4HSgXMcWe-fDbmSOlQpM3TtCRcWAQDerWAM6jcXofpXLm4sIxqRcbYBZka-CTz6F1liF-4Q9emkzaLFtb8Dp_oswl_R5fY11UcquOBQTe_w74Iv_z6gOKlsNB7KmP0HPXvSB-RpGfDXxydJESe9mKOOIXV4bQ8pULSFLp9dB_GQOna0wJdH5ls5I1oMtidPbEdAz_PLqqK10-y7ua9L9zat86VsYVjyUo1Hi7NZvhlF-csrpce0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت، جواب گزافه‌گویی وزیر ترامپ را داد
🔹
صبح امروز وزیر خزانه‌داری آمریکا ایران را به تحریم سنگین تهدید کرد، حالا مدیرعامل شرکت ملی نفت ایران می‌گوید، هر اقدامی که انجام شود، برای آن راهکار پیدا خواهیم کرد و نگرانی نداریم. @Farseconomy -…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/458115" target="_blank">📅 09:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f78e8b1f.mp4?token=Es7fYUxfRtetZshWe3r_b6nLZgC1C2jcfuS2oCHuIVROydQ-32jp8AVIflug8itFyhp8RVhvukjY5VyyBULm3gJwJFZVhCvb09rU3to5Y3VSkS6HwL0lN7ZxNQXKK9dp-r0auO_dvOgg6hImX7orCWi9TDq8P8sas4vtUYqTXJJN2tx54mRMcxcQwLyj1_piPttnNIUxJhJBLGRkA6PQH-IVlxrr5iEXZ2GHVU0cw5Z-7T9kJcAm2KWhUmsBEljwcbhb_eGvCF4C5VbgEVJCbwmfEnwi19cSFuNVfsJpEuDR3-tFMiW7ixZ18obObC_DV3tFsiLu8GSmxpESLFaC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f78e8b1f.mp4?token=Es7fYUxfRtetZshWe3r_b6nLZgC1C2jcfuS2oCHuIVROydQ-32jp8AVIflug8itFyhp8RVhvukjY5VyyBULm3gJwJFZVhCvb09rU3to5Y3VSkS6HwL0lN7ZxNQXKK9dp-r0auO_dvOgg6hImX7orCWi9TDq8P8sas4vtUYqTXJJN2tx54mRMcxcQwLyj1_piPttnNIUxJhJBLGRkA6PQH-IVlxrr5iEXZ2GHVU0cw5Z-7T9kJcAm2KWhUmsBEljwcbhb_eGvCF4C5VbgEVJCbwmfEnwi19cSFuNVfsJpEuDR3-tFMiW7ixZ18obObC_DV3tFsiLu8GSmxpESLFaC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فداکاری یک خانوادهٔ آتش‌نشان آن‌ها را زائر امام رئوف کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/458114" target="_blank">📅 09:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458113">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz3oXd0aCTjs5dsOWR3j9x3siH8L5Sm1q2xmrEUvdBLJPNLnwLJ0-4pe23NzdQgz9J1xko5w8EWDM42KHnx6lU33akH3Kfx14zFuoLzaOWlYUxUF4ZKlZMjCEF8kODmvfVL4aB-hMxhhU7OjTLkBufVzNdJs-XHLEfaFuxpZbRHHTOkGy2J1UvpsGbrS_wgKGtuukB2suh9j1mCrKfRWOGdLXz9odqca5-94DJpo29Ub_71U6sZ9QGk53t6MhNwCyf0HLBuih7NwuHxXspaLN0GACXLpmHzDGQMp8Rfvon7fnGMeiUvrL_7VSpxPAR5sdUrkIPaKOVvaewlnv-JHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح ۶۰۰ مگاوات نیروگاه تجدیدپذیر در کشور
🔹
سازمان انرژی‌های تجدیدپذیر: ۶۰۰ مگاوات نیروگاه تجدیدپذیر در قالب ۱۰۷ پروژه در ۳۱ استان کشور امروز افتتاح می‌شود و ظرفیت نیروگاه‌های تجدیدپذیر کشور تا اوج بار سال آینده به ۱۲ هزار مگاوات می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/458113" target="_blank">📅 09:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af37209889.mp4?token=jSmXCjPvv9xjQDK4Ir0nL_5quYalU4PMfd9jh_HjJ70MEbMH3sNVeM47yd7SEcZEJULKWPBFpgVsKESFFiip7RsuyMiZyw7zzEuGlHsHVmzG8aCVnKosrSMATd4KL5BDqHcmFzDFLn_RtyyJR-238Gkw5Z_HF-QEHaMPxnbVqDS3XOFozHX1tzu6qObmVIDjORnL7Qio85u3Ci_WfieOPp805PmWy-22S941PbfAwU6lX3LmNF2CLTcFqS-Ut_UkH568RlBnKYDmCJjD4D_NphGXomBJC5lfPpueS4txoMZYkZDv_vzo9XMFLiE9rEBiH9uoMBQ1VcBi5CKymCrwApqdsub6bHZhZ--aQqQLBFEJ2NRtjERzZW6v-yCq90u50Ja12LboIc7DNtKxyIf-B2vyfLAAARlM0Rb79U_cxqJ6SPICPKjp2oL9q4wgIbpWiCFcS40WjTHOgE3J6BMC9ZRF0mv_RVCvvy8VmlNCxQHYVl7Sf5Rz5bryPD9fceAx2Arwr-KTmvsQt7BWat5xY7-smERZG34xJJ-DcAOo47QPs028upplsIpWXAKpcS5tPPHLR54pXQ9IjUQejn6dFgEHOEm6hfIxXwSDjvawSyuw5Pm9VhUFiXF6QGg9nYi76zpT6eet5foA8ec-U5IoFZ7lragzLBftETZC_sqXcPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af37209889.mp4?token=jSmXCjPvv9xjQDK4Ir0nL_5quYalU4PMfd9jh_HjJ70MEbMH3sNVeM47yd7SEcZEJULKWPBFpgVsKESFFiip7RsuyMiZyw7zzEuGlHsHVmzG8aCVnKosrSMATd4KL5BDqHcmFzDFLn_RtyyJR-238Gkw5Z_HF-QEHaMPxnbVqDS3XOFozHX1tzu6qObmVIDjORnL7Qio85u3Ci_WfieOPp805PmWy-22S941PbfAwU6lX3LmNF2CLTcFqS-Ut_UkH568RlBnKYDmCJjD4D_NphGXomBJC5lfPpueS4txoMZYkZDv_vzo9XMFLiE9rEBiH9uoMBQ1VcBi5CKymCrwApqdsub6bHZhZ--aQqQLBFEJ2NRtjERzZW6v-yCq90u50Ja12LboIc7DNtKxyIf-B2vyfLAAARlM0Rb79U_cxqJ6SPICPKjp2oL9q4wgIbpWiCFcS40WjTHOgE3J6BMC9ZRF0mv_RVCvvy8VmlNCxQHYVl7Sf5Rz5bryPD9fceAx2Arwr-KTmvsQt7BWat5xY7-smERZG34xJJ-DcAOo47QPs028upplsIpWXAKpcS5tPPHLR54pXQ9IjUQejn6dFgEHOEm6hfIxXwSDjvawSyuw5Pm9VhUFiXF6QGg9nYi76zpT6eet5foA8ec-U5IoFZ7lragzLBftETZC_sqXcPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فروش محمولهٔ نفت آمریکایی به نفع بیماران پروانه‌ای
🔹
رئیس شعبهٔ ۵۵ دادگاه حقوقی بین‌الملل تهران از اختصاص بخشی از اموال توقیف‌شدهٔ آمریکا به بیماران ایرانی خبر داد و گفت: براساس حکم صادرشده، ۷۷۱ بیمار که علیه دولت آمریکا دادخواهی کرده‌اند، در اولویت دریافت…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/458112" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458111">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صدور حکم سارقان سوخت هواپیما در هرمزگان
🔹
رئیس دادگستری هرمزگان: حکم قطعی محکومیت افرادی که با سرقت از خطوط انتقال سوخت هواپیما، اقدام به قاچاق آن می‌کردند، صادر شد.
🔹
۲۲ دی ۱۴۰۳ یک انشعاب ۲ کیلومتری که از طریق آن سوخت هواپیما سرقت و پس از آن قاچاق می‌شد شناسایی و پس از دستگیری متهمین، فرآیند رسیدگی به اتهامات آنها در دستگاه قضایی استان هرمزگان آغاز شد.
🔹
متهم ردیف اول به‌نام یوسف زارعی فرزند محمد، بابت اتهام مباشرت در تخریب عمدی تأسیسات عمومی شبکه فرآورده‌های نفتی موسوم به خط لوله ۱۰ اینچ فرآورده‌های نفتی به ۱۰ سال حبس تعزیری و بابت اتهام مباشرت در قاچاق حرفه‌ای و سازمان‌یافته فرآورده‌های نفتی سوخت ATK به تحمل ۲ سال حبس تعزیری، ۷۴ ضربه شلاق تعزیری، منع اشتغال به حرفه مرتبط به‌مدت ۲ سال و پرداخت ۱۴.۴ میلیارد تومان جزای نقدی محکوم شده است.
🔹
متهم ردیف دوم پرونده مهدی برسم فرزند حسن نیز بابت اتهام معاونت در تخریب عمدی تأسیسات عمومی شبکه فرآورده‌های نفتی موسوم به خط لوله ۱۰ اینچ فرآورده‌های نفتی به پنج سال حبس تعزیری و بابت اتهام معاونت در قاچاق حرفه‌ای و سازمان یافته فرآورده‌های نفتی سوخت ATK، به تحمل ۶ ماه حبس تعزیری، ۷۴ ضربه شلاق تعزیری، منع اشتغال به حرفه مرتبط به‌مدت ۲ سال و پرداخت ۵.۷ میلیارد تومان جزای نقدی محکوم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458111" target="_blank">📅 08:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458110">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تقلای ترامپ برای ازسرگیری مذاکرات با ایران
🔹
شبکه خبری الجزیره به نقل از یک منبع آگاه خبر داد رئیس‌جمهور آمریکا دونالد ترامپ هفته گذشته با فرمانده ارتش پاکستان، عاصم منیر، به صورت تلفنی گفتگو کرده است.
🔸
به گفته این منبع، ترامپ در این تماس، درباره پرونده…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/458110" target="_blank">📅 07:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458109">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzeliqmS2IJEUHoYP84lsBsSKXQhHZTr4qfAMhknEC4G1dBbmKwx9-17ajbWb6d4T31HfuHkIvl7eUBJXXlAswYMxv9TxVFcBAX__BrTDnIGR8e8wtqeduOS-in_K4puOSxFF2kLCi_Ad9PD4tD2r8agtlagxs8TUK7EAA-Zagor53SHDysxQ3yLZpYsnuggR8ubyGFGjpLWM31tMu1Ac9WiCDJo4PPmwzL8EzmU7oaOJo_kS_aT9J7m6gDv_fYfdMa-gXXaJ89aoIbvDBV0k0Qu7lTx_jbPQH6XZEUZSP7A0jmdFP-PyqiCXCALNQzO5_96U-O7UmDzkgJiAOLGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روشن را دیدید، تلویزیون را خاموش کنید
🔹
«آقا پخش می‌کنیما». «بکنید». این دیالوگی است که بین حسن روشن، فوتبالیست پیشین تیم ملی و استقلال و مجری یک برنامۀ یوتیوبی ردوبدل شد. درست بعد از آن که روشن تصویر کارلوس کی‌روش، سرمربی پیشین تیم ملی را دید و فحشی جنسی و کش‌دار داد. او لحظاتی بعد همین را برای ریکاردو ساپینتو، سرمربی استقلال نیز تکرار کرد.
🔹
روشن تنها بازیکن ایرانی است که در تمام تورنمنت‌های مهم فوتبالی برای ایران گلزنی کرده. جام جهانی (۱۹۷۸)، المپیک (۱۹۷۶)، جام ملت‌ها (۱۹۷۶) و بازی‌های آسیایی (۱۹۷۴). او به همراه ایران قهرمانی جام ملت‌ها را هم تجربه کرده و در استقلال هم به قهرمانی رسیده.
🔹
بااین‌حال چیزی که این روزها از روشن در اذهان دنبال‌کنندگان فوتبال مانده، اظهارنظرهای تند، عجیب و غریب و حالا توهین‌آمیزش است. او در این سال‌ها مخالف حضور بازیکنان و مربیان خارجی در ایران بوده. مخالفتی که البته فارغ از درست یا غلط بودنش ایرادی به آن وارد نیست اما روشن حالا پا را فراتر گذاشته و رو به الفاظ رکیک آورده است.
🔹
او با چنین سابقه‌ درخشانی در زمین چمن، بیرون از مستطیل سبز دارد تیشه به میراث خودش می‌زند. وی البته تنها کسی نیست که در این راه قدم می‌زند؛ پیش‌تر خداداد عزیزی، قلیچ و فنونی‌زاده نیز با دُزهای متفاوت با اظهارنظرهای غیرعادی در فضای مجازی خبرساز شده بودند. سؤالی که پیش می‌آید این است که چرا پیشکسوتان به‌جای ارتقای دانش فنی و حضور در پست‌های مدیریتی یا مشاوره‌ای، به کارشناسان حاشیه‌ساز و پرخاشگر تبدیل شده‌اند؟
🔹
سال‌ها ارکان فوتبال از لزوم فرهنگ‌سازی روی سکوهای ورزشگاه‌ها گفته‌اند. اما چه توقعی از نوجوان پرحرارت استادیوم می‌توان داشت وقتی پیشکسوتش چنین ناسزا می‌گوید؟
🔹
برنامه‌های یوتیوبی ثابت کرده‌اند که برای هنجارشکنی، بیشتر از یک تحلیل فنی ارزش قائل‌اند. برای همین است که پس از حرف‌های روشن گل از گل مجری می‌شکفد. او می‌داند همین تکه پربازدیدترین بخش برنامه‌اش خواهد بود.
🔹
حالا دیگر وقتی روشن روی صفحۀ تلویزیون یا برنامۀ اینترنتی ظاهر می‌شود، تنها توصیه‌ای که می‌شود کرد این است که کنترل را بردارید و خاموشش کنید. چون جایی که یک پیشکسوت گل‌زن، به یک فحاش تمام‌عیار تبدیل می‌شود، دیگر ارزش تماشا ندارد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458109" target="_blank">📅 07:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458108">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMIsdrsBc5tPqtSiHNZexVK8rIle_Bu7J3Cf3VEMI-0VGwyuRIg1DvjCAFB0svh38DZIW4nVphuZZEKoORNkpZpTfCxfaOhKLtT5WAXrH_vZoM9ZtaqoDrQQuP_HUAPOfB9N6D71AU-rZG8pWlzQwaqAhbPm3QgIltN0g1TF5_IKw8jr9YBg3UYhZS58L9nILJvEf9CFNBd8JMmAnjj9-Ynd3PKtnTPrQsvzU19ZTPbOZkz58Z8F_6AJwCNIZ6XnEUPE8ZXwMdL9gr2hFecFdfVt92-qdejKBzjVsJBYFz0upGNXfUmGgrIul-dyQPuHJNpbE_IDB3xyaBLtEyAN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقاب اصفهانی امروز به شورای شهر می‌رود
🔹
سخنگوی شورای شهر تهران: در جلسۀ سه‌شنبه، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی به ارائۀ گزارش درخصوص برنامه‌ها و اقدامات انجام‌شده در حوزۀ مدیریت مصرف بهینۀ سوخت در شهر تهران خواهد پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458108" target="_blank">📅 07:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458107">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
سخنگوی هیئت رئیسۀ مجلس: ادامۀ رسیدگی به گزارش کمیسیون امنیت ملی مبنی بر مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در دستور کار جلسۀ سه‌شنبه صحن علنی مجلس قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458107" target="_blank">📅 07:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458106">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آمریکا روادید ۲۰۰ هزار نفر را لغو می‌کند
🔹
طبق اعلامیۀ وزارت خارجۀ آمریکا، واشنگتن قصد دارد ۲۰۰ هزار روادید تجاری و گردشگری که خواستار پناهندگی در این کشور شده‌اند را لغو کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458106" target="_blank">📅 06:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458105">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca58c6482a.mp4?token=JJksclH5zLAlOu4Y--gjAuRIMbRAvfG4Oq1Yb29K6kBvcQDqXxRjEYg139BxbogyCAkdEECUgeQSdeOWQ6KF6V6DK7t1pomV6VD3ygW4d_8NyIq6bkbNNtFDftPh6kViawwoek9yLe4T77BRRklnEZCLn6feVlsmh_DaOYEss652hNE9cx1Eqg_erxC58mL9AL00nNeAMikiAGLorGImyPBO9v36qeg86CceGtfjlOm-j6AtuJhj3WmLWjNnIamPDVjKCDJchR03JH6X0BMoCzOsH1DBFwjaKvjQH1LRA771WJzRfZdZ6UyeuAloAxxG9VvfCzXumpcLg36UYRCsaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca58c6482a.mp4?token=JJksclH5zLAlOu4Y--gjAuRIMbRAvfG4Oq1Yb29K6kBvcQDqXxRjEYg139BxbogyCAkdEECUgeQSdeOWQ6KF6V6DK7t1pomV6VD3ygW4d_8NyIq6bkbNNtFDftPh6kViawwoek9yLe4T77BRRklnEZCLn6feVlsmh_DaOYEss652hNE9cx1Eqg_erxC58mL9AL00nNeAMikiAGLorGImyPBO9v36qeg86CceGtfjlOm-j6AtuJhj3WmLWjNnIamPDVjKCDJchR03JH6X0BMoCzOsH1DBFwjaKvjQH1LRA771WJzRfZdZ6UyeuAloAxxG9VvfCzXumpcLg36UYRCsaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ مجدد اوکراین به یک پالایشگاه نفت در روسیه
🔹
هواپیماهای بدون سرنشین اوکراینی  پالایشگاه نفت شهر «آفیپسکی» در فاصلۀ حدود ۳۰۰ کیلومتری خاک روسیه را هدف قرار دادند.
🔹
این پالایشگاه در حملات قبلی اوکراین نیز هدف قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/458105" target="_blank">📅 06:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458104">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyloew-D0oIGxV8QWTaiswdMPXvD698WqqmVxtffqoqlGkW8dKuCMYV98dD8FT8uITA0eBfhLiy4C6vqYBcJnwrqcOH9nYNUFveKySdPWMSChlcMsm4T8Vz1dqPbswfuBWSUtroex_4cf9qq32t2qMxDOFsKXdUU1OHR7JRLOHhygu2tlac5wgubtmPeiprfGflL5Ohm_ujVQnXXW7ezY-nklnM6Ur3lcy3G-wcSFRUWW0wm2uCGhpHZfgjxLMaOf8UyfFgREzK7AfpvH9ALpbpUK7fxF9qAJIe1fICTLdzDevLV4BnRQsxFtgp-BkSY-d29hi0tY3OUidyc1HvLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌رسانی با سرعت کبوتر
🔹
بعد از سال‌ها رقابت برای سریع‌تر شدن اینترنت و پیام‌رسان‌ها، حالا اپلیکیشن‌هایی ظهور کرده‌اند که دقیقاً خلاف این مسیر حرکت می‌کنند؛ پیام‌ها را عمداً با تأخیر به مقصد می‌رسانند.
🔹
در یکی از این اپ‌ها، پیام با یک کبوتر مجازی ارسال می‌شود و سرعت رسیدنش به فاصله واقعی میان فرستنده و گیرنده بستگی دارد. یعنی هرچه مقصد دورتر باشد، باید بیشتر منتظر بمانید.
🔹
اپلیکیشن دیگری هم از حیوانات مختلف برای ارسال پیام استفاده می‌کند؛ حتی حلزون! هدف، تبدیل انتظار از یک مشکل به بخشی از تجربه پیام‌رسانی است.
🔹
پشت این ایده عجیب، یک هدف جدی‌تر قرار دارد: کاهش فشار ارتباطات فوری، اعلان‌های دائمی و انتظار برای پاسخ سریع. این جریان بخشی از موج «پیام‌رسانی کُند» است؛ جایی که گاهی کندتر بودن، خودش یک قابلیت محسوب می‌شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458104" target="_blank">📅 05:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458103">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86fa6d752a.mp4?token=YXKJamWPmqrCHPQMZ6HBtMGnm0TS-ZzjiFRnV_aF0NNzM2V5Y4G_yu5e99XT5Qoqf1n4syMaMLH5a4y7aTYr6cGWhqBv-lZbpZA6CirISiwAWae6w8vkD_dl_Y4UKc1qwJ1GWLRNgUxbJW89lLWeCF6Ex-Ihq1K7Kl7li6a_BBMo8tmw1xDc55Ekt67Q1pqWKI7ayaomNSXCRZQxXPYMJCYt_T98oEWQHCH7ensKvbom-5Gyr0Q0JUqk5ghyVWGKBTi93XkxqY7pNOqMtuZreVw7gq13rXc3lTD4k9G1C7CyTWlhXx4X8PlnN6t-UTMONmziF0a5LUZ2JC7-6Sqvxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86fa6d752a.mp4?token=YXKJamWPmqrCHPQMZ6HBtMGnm0TS-ZzjiFRnV_aF0NNzM2V5Y4G_yu5e99XT5Qoqf1n4syMaMLH5a4y7aTYr6cGWhqBv-lZbpZA6CirISiwAWae6w8vkD_dl_Y4UKc1qwJ1GWLRNgUxbJW89lLWeCF6Ex-Ihq1K7Kl7li6a_BBMo8tmw1xDc55Ekt67Q1pqWKI7ayaomNSXCRZQxXPYMJCYt_T98oEWQHCH7ensKvbom-5Gyr0Q0JUqk5ghyVWGKBTi93XkxqY7pNOqMtuZreVw7gq13rXc3lTD4k9G1C7CyTWlhXx4X8PlnN6t-UTMONmziF0a5LUZ2JC7-6Sqvxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): کمک کردن به نیازمند را به فردا نینداز
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458103" target="_blank">📅 04:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCPUqEyGooJ4ZxZULgOrdzRnUidbpO_VvxpG5DX8GdOJPbY_Rx-249Fu3HEpUwHI7gKbKR18CIX0OOWs3piFv9rxol-3lbs48hAMLz0qIKCiECVjhpiZZhuHUyeKQDkAqEZnxiFUyudGNyxFGu-aXOOYxJeVAG4Qq3p_yJjWRV1hi03aUalY3ZWWTHJOkiRsqJyTEpuYJk3yMKPdxOi6JwK0Zj6WxHcTJ_tqLpE8U9lLqUiHNae0i5v8Sy5GfqOvnUB2xuo3RScAP1JgnCvBydqPinisgZ8ghfribAJgTWqOkKgmWtFP1h107IpCvhEDmGLtlzVbKnUXu0l3m5N3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7oVcx6ynl0DDe7nZC0zid-9yb7iNIJuf47LkgGfEH6xEebEQJcKyA86Y-vPaHQywNV1ie1fKwDJZFq9KYmb41wa7q4oPSjECWUEvY7B1JXd2auZB-uoip3r5lssGOsAWZ2un-7wENF4yKZEeWT6J8zLGod5w1X0-WZ8LtGe46MjdyxXlxj5vJSFRWlALf2gMpu71v-i4zBVJwy12WLVF7EN8JwNudkDtSEnsZxepfRTaCvQMmNDFh5ByVOQZmrC4LlonHuIAfnSnvIyHmwUZ0bJWfA03XyfaM07cKPgdOvJcPy9cG11-qMXxCWrHryfj4zVo5pCWjzct9ruwFoddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qg2MCQjIdxypLFLV1FFatD4jjDpFt6Dm9_cL4yqsltGM66BeqBBnVa1cSiyDbd1jXZw_GGgd4aT4dMx_2iJTeh8Or9vq7AkYgVBzNRbBHgnXGCMP1sAqPQPziCa6QSkmdfTIjVArYhCv4NOm7lItXNozGt7QvWlXhjeOqoIbKStH6PefEZLEk00s78iC1OCiBSsRj1DbffiyCPiU-B-YjtJy8gsiS738frP0MQ1c0CEVnl1FZmdXXapik7YLou9Y6MO4D3hNdkm4Tft7Xs7LkWgptunCjcVpa6ufeMDkV3dpzHOzfMRfGqngocIjydggi7Wkv8-DM5UDYgjBwrdKKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب‌های پل خواجو
عکس: امین علیجانلو
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/458100" target="_blank">📅 03:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حملات صهیونیست‌ها به جنوب و مرکز نوار غزه
🔹
المیادین: خودروهای نظامی اسرائیل در شرق شهر خان یونس در جنوب نوار غزه آتش گشوده‌اند.
🔹
صهیونیست‌ها به‌سمت چادرهای آوارگان در شرق شهر حمد، واقع در شمال غربی خان یونس، تیراندازی کردند.
🔹
اردوگاه‌های «النصیرات» و «البریج» در مرکز نوار غزه نیز هدف آتش خودروهای زرهی اشغالگران قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/458099" target="_blank">📅 03:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458097">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcvb-k-ozV9AyO0bS5-c8PxE_L3KNUWCgDysPW6JQH5wknRD6AP345I0Vcsu27j1ZU5DH3ULYXB7NSB48Pe_jOzZUaq3eg3I_pXuDRHUB2BrGam7CQ1o8LFtL0igyriJru2zZtNNzrxZHCsVhz3RZRQMoKHuHtpGWTM1H1Zf4EbbRVlVWeavaRb6nDQsdHM5AGPhjRbofpjoKitYTtAevrFsDWajhCoP4mAlcv02bMek8srb33gwZFFvx2DPjf3k8fsbsMUKdeZjgPFxxVYkrQxXbYtcrD9KLIgESAsY6j9aJUxLW0-P2Fe6r3mWsr2gvKm9-TbCTX_qQaVNpBETVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کلوچه‌ از بطری پلاستیکی ساخته می‌شود
🔹
پژوهشگران با کمک مخمرهای مهندسی‌شده، پلاستیک «پی‌ئی‌تی» را به ترکیباتی تبدیل کرده‌اند که می‌توان از آن‌ها برای تولید موادغذایی استفاده کرد.
🔹
این مواد در آزمایشگاه با ترکیباتی مثل فیبر و نشاسته ترکیب و با چاپگر سه‌بعدی به شکل کلوچه درآمده‌اند.
🔹
هدف فعلاً تولید غذای روزمره نیست؛ پژوهشگران به کاربرد این فناوری در محیط‌های کم‌منبع مثل مأموریت‌های طولانی فضایی، زیردریایی‌ها و مناطق بحران‌زده فکر می‌کنند.
🔹
البته هزینۀ فعلی تولید بالاست و این فناوری هنوز در مرحلۀ آزمایشی قرار دارد؛ اما ایدۀ اصلی عجیب است: تبدیل زبالۀ پلاستیکی به بخشی از زنجیرۀ تولید غذا!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/458097" target="_blank">📅 02:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B68u9o__k7hxoORU_HcMt2YmDlh3DJd5XgIMmTP_3QT_RRId6wVhfGKLupEeKbqmLOo630SHYNueHnVSS880LUGoImjFMm_xPhxChuenly7V1fKhO6j2uDAl7K9rD2KlWRqKPSMUFKlUWXBRFh7hbmKqkO4jcoe13KQcmHh3Tcv8-Yp5_pfCFPM4aDK98ofP84E7Xp_ZY2NY13VVUB1180pe7MvCJDoJjgA1O0QNxQ39hnjhmKsMBJeKXcsYQ_4yJlCF0LOaM2OW43Im8OvaIKVb8U91u9X_dpu6Lg6hmIkx5bdROQOmhlM2Rd3HdZt0zSrbPCm8GSkSg44HV1i14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هدف قرارگرفتن یک نفتکش در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در آب‌های ۱۷ کیلومتری منطقۀ «الشیشه» در شمال عمان، مورد اصابت یک پرتابۀ نامشخص قرار گرفته و موتورخانۀ آن از کار افتاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/458096" target="_blank">📅 01:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا تحریم‌هایی را علیه ایران اعمال کرد
🔹
وزارت خارجۀ آمریکا اعلام کرد که تحریم‌هایی علیه «مقامات نظامی و شبکه‌های ایرانی دخیل در تهیۀ سلاح و حملات سایبری» وضع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/458095" target="_blank">📅 01:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458094">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
توپخانۀ اشغالگران، ارتفاعات علی‌الطاهر را برای چندمین بار در روزهای اخیر گلوله‌باران کرد.
🔹
همچنین شهرک المنصوری، حومۀ شهرک‌های میفدون و صربین، و منطقۀ دوحه كفررمان نیز هدف حملات توپخانه‌ای اسرائیل قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/458094" target="_blank">📅 01:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458093">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b225fc7a.mp4?token=RWy_nLyOdqUeL1hz4KVTjvKM__50SFQVyFUoZeoawaNivqrVi6Q1TujjwsdAwTH60WN_Lpels0pkDpor1ls4eBIbeh1RAtbyOCdyv3pAWP_Tj67plzHbpnlQTPGgR5eW6kKMFXYortb51cfHp2BU5nqYDS-ULROVd4Dr4ildPo9ybeUQdJmvomKzr0okwI2hsp6zEWTJAZ1izxLDC1tNKCfIx20t1yK2N2CSMaBC8Z06NTN6t-fa0RxzP0qeLvGfLY9wJfsUK0ZfgIrnCsZ-BMlnPHa30Ikw4y-TlnUj_ZkJ8OIcj97FbrdrYwZAl_UIV-xxz3hnJZxhV-IyfxHJP5DLNA2G_L3UWI4zrYA9LywIq3TWU7Op-A7GDAQ6X0mkJuAquJu-7Prcwp8JplJpOjLLUonlqJEBgpKxVvNLlAR8aBbpdb3Wou3mBSaNvCrUq1_UZf2K8nIKVhTf5cXnuW6-5PipLpUh2CAfCdxHpqSeGxi2WQ-vEC8cpjjBHnI9wUjhv1scajtov_r3sYm9_xl6S_zcJ9eUPNZQZHG1KnxfcWANupbgLwqRc76M4ffZ3i43pW3zbctaekqyes-UJZYoBDfknBlXZg9E-rz5c42ubnTQ9BPiFgZD1CC9jcUCzbx24wU80j7GSogvpxjpaCZkE3d9kW5miMtqKKiMg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b225fc7a.mp4?token=RWy_nLyOdqUeL1hz4KVTjvKM__50SFQVyFUoZeoawaNivqrVi6Q1TujjwsdAwTH60WN_Lpels0pkDpor1ls4eBIbeh1RAtbyOCdyv3pAWP_Tj67plzHbpnlQTPGgR5eW6kKMFXYortb51cfHp2BU5nqYDS-ULROVd4Dr4ildPo9ybeUQdJmvomKzr0okwI2hsp6zEWTJAZ1izxLDC1tNKCfIx20t1yK2N2CSMaBC8Z06NTN6t-fa0RxzP0qeLvGfLY9wJfsUK0ZfgIrnCsZ-BMlnPHa30Ikw4y-TlnUj_ZkJ8OIcj97FbrdrYwZAl_UIV-xxz3hnJZxhV-IyfxHJP5DLNA2G_L3UWI4zrYA9LywIq3TWU7Op-A7GDAQ6X0mkJuAquJu-7Prcwp8JplJpOjLLUonlqJEBgpKxVvNLlAR8aBbpdb3Wou3mBSaNvCrUq1_UZf2K8nIKVhTf5cXnuW6-5PipLpUh2CAfCdxHpqSeGxi2WQ-vEC8cpjjBHnI9wUjhv1scajtov_r3sYm9_xl6S_zcJ9eUPNZQZHG1KnxfcWANupbgLwqRc76M4ffZ3i43pW3zbctaekqyes-UJZYoBDfknBlXZg9E-rz5c42ubnTQ9BPiFgZD1CC9jcUCzbx24wU80j7GSogvpxjpaCZkE3d9kW5miMtqKKiMg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سربازی بیرانوند باز هم به تعویق افتاد؟
🎙
سخنگوی فدراسیون فوتبال: نامه‌ای روز گذشته به سازمان لیگ رسید که در آن قید شده بیرانوند تا ۳۱ شهریور معافیت دارد اما کارت بازی او چنین بحثی را تفکیک می‌کند. آخرین کارتی که برای بیرانوند صادر شده تا این زمان را پوشش می‌دهد.
🎙
بااین‌وجود یک اما هم وجود دارد. اگر استعلام دیگری از مقامات ذی‌صلاح به سازمان لیگ بیاید، آن کارت به‌روزرسانی می‌شود و وی می‌تواند تا زمان جام ملت‌های عربستان و نیم‌فصل در باشگاهش بماند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458093" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcxSWKQHXGNtNbcbPNMsEEq8O2-aANsxuJnaXtrJgoBa35S5BS0oaEP9lE0g27fe0BtYPK6CF613B8bsbsFuw-LTrHCQIHjjOLoGF-eo1ydxenvcQa1jFOmLHFh4kgJnpfry_EdwFELVNAyi04edwTMR7bynZLWrhAQ9XhwKj8WlcuDL590j7zh-W3sD1XyK_CCN0d5zhitfRUrzLN4HiznktNsoWs4SS3e7_wSVEfLj5DO5Wst9YLEzSjXqjhOmbyMVXQ95wu0z-Zsd6VIrGsT6pPx0haIWPE50rCMDCMIETrAXBBh-2gzSL5EdinXAlD0E_SQJp_4DXYu1hs9c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زاکانی: تغییر چندبارۀ رویکرد جنگی آمریکا بهترین اعتراف عملی به شکست پروژه‌های قبلی در جنگ با ملت ایران است
🔹
در زمین نظامی شکست خوردید. در زمین محاصره به اهداف‌تان نرسیدید. در زمین اقتصاد هم بدتر از گذشته شکست خواهید خورد!
🔹
دست و پا نزنید. خروج از این باتلاق امروز کم‌هزینه‌تر از فرداست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/458092" target="_blank">📅 01:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458091">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9287a378d3.mp4?token=v0Z7daxlVR3wC6y0CK1ik6rhN-zS1jX3blwM7Um8TbR8CH5gG6B5roU9p6E6NjZK-Qldv9Jk1xjzevb-GqAELvIf_XZ514sffWHz8-DjgIdSFGbtwsv0bwczdQpctbOUL01mABEqyQzl9ONkVvCZ3k5KkLT0HchkCoCyxRMgWwlBj2vlTwmAlP2Hk13JPWo0D-7_yRqE0rEUy_z00mta0x-Mgh4wt5Z_SsRRjr-GE9XG_l6uYdsJV7LSu-DVX_ftriVrKetjIlyNWzCALvn5VqZib3nLziefM7af5U-miqvLDgi9AwNmrA8YF390qKxITJYqNT30gbnsbpfc_o4RzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9287a378d3.mp4?token=v0Z7daxlVR3wC6y0CK1ik6rhN-zS1jX3blwM7Um8TbR8CH5gG6B5roU9p6E6NjZK-Qldv9Jk1xjzevb-GqAELvIf_XZ514sffWHz8-DjgIdSFGbtwsv0bwczdQpctbOUL01mABEqyQzl9ONkVvCZ3k5KkLT0HchkCoCyxRMgWwlBj2vlTwmAlP2Hk13JPWo0D-7_yRqE0rEUy_z00mta0x-Mgh4wt5Z_SsRRjr-GE9XG_l6uYdsJV7LSu-DVX_ftriVrKetjIlyNWzCALvn5VqZib3nLziefM7af5U-miqvLDgi9AwNmrA8YF390qKxITJYqNT30gbnsbpfc_o4RzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین مرگ‌بر آمریکا در رواق دارالذکر حرم رضوی، و مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/458091" target="_blank">📅 00:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOnMkmdPqM2rJQI2piBviTYXL8VtfrVHQiZWMqGotaOFTA56wdMl9lNfeg_nTPvLlXdXI9AbFhlJYcSXq7FPVG3Cs6bUbJjbnKGcPNDhMUq6X5xamzSlaGx-12yEG1IYcCwWUTsXINihuWChTmlus89yPd5U7EELHqzbNHchTG53ESsZK6ySfJ_AYRcb5BSu0jE36Ow2D-E1VWImeV-QfIhUymcE64COVNjslnxer-eqqJktOhLSCsZQR6ru7Nzkyf93FOh4kIyySDBZZ7rQWGCc5puN95mz-2HxQRsWSysae-a5AkGRdHbBuduLTzimTLWGLWc491qX6gk3i382Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور: مشکل ما مصوبه نیست؛ مسئله اصلی اجرای مصوبات است
🔹
قائم‌پناه در سفر استانی به قم: مشکل ما در بسیاری از موارد قانون و مصوبه نیست، بلکه اجرای مصوبات است. مدیران باید برای تحقق وعده‌های دولت تا حصول نتیجۀ نهایی پیگیری کنند.
🔹
مردم باید ببینند وعده‌هایی که در سفرهای استانی داده شده، در حال تحقق است و پروژه‌ها از مرحلۀ مصوبه عبور کرده و وارد مرحلۀ اجرا شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458090" target="_blank">📅 00:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4PNe2uBCHTzl9P4gEVC18c4o7sBfVXib7e4XLr3zzHRpjKGUQXN43MSoB9xr1mlQXFxBadov6XLQZUzXUkE9yKF_3jXKAeVrBEoYEF5X660UIkgO-nrPNrl7UslIzYWgOvzuwr_4kNodpLu5GhOpA-qn0CMcIB7zBXLeCd8cE_kg54t9Yt_LC6WMf-Win6pNnLfmaS8XqdC4Lg6Xw0UL78Z72OAm4wHwbz14PudqPlkCylD28lTblrSXhAbLGa3x90r8FWNUtynyEGh2Kny4TdgUhLVVbu3gZ2g9_u_bRvnRXdsm3ADNIbX8WYLdtS5vhoyOCMD-CNxa2W_rccB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSzeGLlO-KFXYjw_aCDi6zjCG3PWmOOlu9vW_8nZAmvFEwoCRQiS_MMosOy0JJezdfk02Cq-0KVFYktfKWIzUHEbP24bGyn19Oidh8mqsY6YYid0j8m8_7AHEJyB5xHmfrdzAh_s-wtFlfgBtji5lSP7_oUJJHNaX7xt04HtunBWK1AUGb_2swAoj-UOfD7mNpCm1Kphr8VCmFTD_eYeVf32A_43HD9pPoDYFDu3EI4aq7au3bhOd1RFDU0IIMVX3J4_BNMXKeOflXC8dIeDJrA1X2z0oTX2H8Qcba_Ioe_VLy3tJVyFNU7ECGtxwPYpun3OnHMauVyFtpsDYzDV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voItS6PHqpwPRf0nPU0Xtd-XOHbo18Nj_x9vRYsL4jsZjppYQMN0JVQwYJ_87oaMRJxiVDL7Dx1N3uhCXyhLbzfl8znnD2tH52tMum9bYd7cYfPRKuYQ84UC3U5AF4-DLi0CejUT9Y16dFzmLh1QHi5PK6z1DiKjgDYXog0yNmibmhiK3WJBWQmspDWwvNtWOkEssmi3KmaWYe4hD_-0grt35cy_SKuQ_V_dDTx_s-vt3JBVWvvQ44fsVqFuOIE7CHCylfAz46oDwbpAghDmdT2NnFz0YQk0_zEp9viyk73M5wEjjac0U1I_VFERw-2SmnGGFz-EkVaR06qrjR2i3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKgtGAu8487HRLbOguF_UaPBN24KV-qbUpw6WnOL_YHuqhJg6CUyWeWcjWYXguBDpsK7cxl1PTrTL6lUSEHByWVnta45DEIVg7cCA4qAS89NuCXBAVQqwR5RjusZyT4gWqiY3mEeizCRKV_hhgjyHbOXRU5JFfSanOnek4R-NMkwQL5CVkjgRm3c8FeS7wGgXcKeCCzukkLHmoVB0IdZT0G2drKaYdsour8uf1Q2xK1u_0NWKmzp-bdK1LPpOa1cr0r7c3c3l98C4HR6jmiQmiYDLMKHJhU-59nSKbsA390pKXabfTfsZJtuTxtwgSHt12Xti4JCSGuuh0Gegem9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ag78l1oBzv0Qey5zeQswjsPOE2N1O1JeMPZ4jcEHuoT95YgIWCBzg515v6wP_234m28s4G3jdmaOQyyfg8vTbRLCcyP8KqGkPoOZ0v-ypmva0LowkFBJU9aK3KYAKSPBRXKh4DJ6hY1dvxq_cS7wSAlwMH3JfU4ao5r48Ttp8WleIjT_XX5ZTGA5EB8uAmtGNbGPWcKnJjNO0lCgpydbzK_EvMhaMUDjrKz4z5Bm7RRYGd-Q_zTWISrw4dgO62uALfiSEsmqISRo6OMU9jL7s6oD5hHU7xtNtzM6WPFn-6FxJj4U28c9RejVXeHyAAjCFYWvhkUIQdqBVbhI56cOog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۳ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/458085" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et1_4ca4MLCcklpjky7xZjo7RkqfNSOZ-vXVefZ3XVhuX_a8Hv4Hh0_4Cq-eeyrAGgs2hE1XQ3YbbcxVrKIHlLXXgFQPDnYpyXJFjhQOVht2r6iCjwtUq0KGiAToBPQoC3t8Lb23LoDsFDZ2V79_I4ZvQz7oAXEHvuQOo6xcT0Xl76C_fpsjGSUz0lCaUNxV28oL4W_Yvf9N87HAOZ6P04bI9dlKJrrA5EgxWbizrvZuu_nMwaDsFAnDsS8JIJJhL-2L3r1_KkI6HWFicN2CbIMXmUShNvfrRNQL89KJM6MgZOL8FJOlbGeZFEnBOtSElv9SUGfn6OzDCg2HdFo0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNyFpxzFEICJZ-ybEhWq1NQw4dWTB0E0lGKs-X74GLqXNNVD1D6NU1dzVeyGlR1SN4_BKjOO9GKTp6zk6AffAYgt78ovxsMMjwcgQIO65ophiVW4HLg_yn57jxcj8mz9Ra4lXC5-OjG-7FaSerLG8nj8vRiGNQ3UWT6EoUqTPf_ZcN9_8iKxmmTbXisFet0BePS4B1Ng7ZUmVj519QUpayfzjvA2O4NwvI5EpMaBopMx1ap-M6sRyuaRogMhiMvN_KgEvyiYjTDIhDyAUqrk6JL7zabJjw4AkOZSJsa94wsGXu_NG3MxghVS3RPul6zIBbs7LpHrfe0wEAXLeUvx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5-rem8VT58TVPwHeQBA7rdi1yvQDKC0OkzsWOIi_Yfg2t3zNrzavwlLr8vA4F5RUHyAzr7U6kgcCRfd7g82dvRCkHAXpcB7ZWSv1AeNWOhdVTW59HLWX5-GGTPQufxeGdsHDZHJuj1xvudlvVdMK6LlEOpQ4BA1fBVyfUazFqdjFl__LwN3G77OmzGbz7nTJ4Qjwco-F_kesG4fWzl1vORdRdl0UCfTVkiSzv3rfJ1c53BjO6zTfW4AldtEaMXTYk2kYtZJcVOwUGfty-Zy9WSrHnPyvH91P4Up6RWP-Cu9L10rrR9dkqv75G2qBi64NYOIPrDctMvIwyhl36TSyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-EpRdEgjzN-0E9if0-2seHElSnmU3MwspbDfOZokCh_jeO2oFp2DxolHMCiiitIezYZDAX-unpA256n9nz8SNJMJGSf_Im9TxM73eFuIW391Hh5Wc6qrk8bN3APOPWJFtoDGJ9VoF7yagF0H6RXggdecmSbL65Ujz5IvAwIgK2KaumgcNFKPilajPbbZ9JpChb5IAZDFYlVkumbiEtpNds-nko9FepjULHsru0u6TAGgWP8FfHqUwLnGoPo9VfeH2qc2BcmTcFPHykYI24TCHFoU8CKwPHS-zOK5Zdb8uqLClM7SnR5gixWnVi1xkr8WEjX3uncbOQR31BK_o9ZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgNxvf2ZU2Srgg7m4PlFqvigJofWT9aItLIxagzLNFeAetAMdr2haln1hZaYpaz45i13k4S61aQR3b_JevGIy9fLvrArQxpqAJ0EQu8TsLAg_aYLD4wu2OdE0JIc0TNM_Eb27EvB21NmDHkXLOjC3WycCyWnS1Hi8G1897baqzLpwh0uz2tl4KQK60SRVPDDyLYhY-2q0B6Z86aNGMAQzwtDWBpCdKEmv-fQafte-rKibQsmumsmfiDfGcsbk2bn-z0BeK-VFUocaI0dodYpLBkUeA12pxWLlVAilr_XV9fhacqBdAYUncEyzqcjPJ6RfRTcMeLhLFDT-8nt5b-amw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMAaARXVQdzCKl72ByciSst-Q5xDXSk8d6OGMNMQ1AAV9uZinA1Aa-q1WgYsHv6lwhdc1y4jwOsMwTKOKvUU3O9_F65_6-vubMmSSmZPma6hOldVUx_ftIpWak__IOYLa71ah4mAKTn2dHax1Cp62kv-4_L7dPOWESvKdPfolWsot3f4zUHA7stoYdrXsApJMYlBjzTyMmyCboZimH8dOQGLIXu5WVSSC6g5gj2Z8ivS--YNTwl9neDQlJqVhkw-Le3ECUDWEGzDUd3fljHZow4eLvCeIeEpLd_Bt2f9iYetdVqAm5oHfvlzO9mSnKmbrGozpNwkDQKsDg8_opZRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co9L9BkfZF6ZxE0zgQ_t2RN_voZJSmysro3kQ3_M6kTUiMuDpjmdotxCzVtmypiFlczT_iioRdRHD_yzPwjST14oIManLbkDVmTDKRN28pB_c3ItJwSemKZXQWw6g4Ddw-WUdCrpMy4yF7tEkzaauCgNYyGN5nkeZRznQwpof_kHV587iXM-t7Nbs7YOMVlOD6AL-H1GPFyUsXo5vk71V3Y4C7vUtJa4Al34Pf0JoXoQOHuafh9kwAmLv4sVuwUdiGNJ1-YY8Tmq6eCRM11Bzaah9wKKXGudkl04TON3Oa8xgwfooWwpckIpnBaV3nqqHojtbKXrvBT4r2nOoCUkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTqus2hLuwXPQLS-eZS81gAotpMdNx13HmJPOwSSaCbh5E_grWmwKM6uaGKbp3O3EBS5YsBkfiBOBbY6JlTDjj7s19yFNCH_SwBpMb4bAhk3BF4qDmFpnIt33JZ4Qfu5OoTsxxv8n15cVOWAvhmXmcwb7QdYJ9BGQnNBV0QkyOiRz-d6IZEMVOiyymkeXY3WH6ieOXX2adg_KCUX8DmzTAtfwg_CYO9oiaVDKQ1YO1qaN2_cU3Hr1D4qRCu471xWZTAWc77c4tRK7IyabPgRhEpfpX9MHf_qJX8zdUHAeFNh6WwGT9ZnUbZ3mH1Z7G6piiZ_YDWHRJQY80_OmtGk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhBnOQgAwvL85fQoXT6nrpIREpmfICnGYZbgPsUm3hrh--ed5NRc_FcAipRhPpHItyoQF-WIFL2Nnyb3miRouAw04fEmzHA1V3si5myqaWQweE0d7h2kzO-gF5Jy2f6IIEJQK-VWG7WJuGhyV2iqhamXN3KsE8zKQv8aSSR7yGK99eTHmEfgosCDCuXxHlJ0BGWxqnJOUeh0x03m9yThhG4mFk-4iZ5BqBijsOnzwi_F7RuqLjYQW4dPvKmc-i9DpJ6EoKxnFpwjd3CAR4UR3JOa_KQfd7o3KF2IRoZYH__BjcgLoxAwEvMBSHVAhAdQcuGoLDbWqzOE5aD0NG6HNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE8RiDBoEzt2V94u8wFYPXqMCuKS9Io-4tDkZW4QNgtt69yyIf9e3fN4FF_BUfJB52eqbKX3OsfkKjGRaQg0QCMEwJ0RYam7yTT9q33uZFqLUYGBqlMIj_rThmuo4E8dhD9JslYI0spsksaM_Pd7OASxmXuCevAcnI6xxbTP0LYvmf2j5HVOZqb6cZvbxjPcHpsRgJCPvzmgtcK5ON3cg1kOniv6h6o0aObEEpDQF-Izy0Zrw00RmUqIkDc7M-ErXEnYLK5hklbXaNxiTVUgg3_YX7Qc-q-aFh-wVJpldQy6uB_uPj0Gx9Hb29PkZ0UB-8I3mXsz-kmMHBcGI1Bplg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/458075" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9f37d892.mp4?token=r0ygulF8TJgNvROsI4PmDIB5Mi_rLcnpQZJPshwDKlxkQMqu3oqs7-nbL9IqmqzKwgOEng_fVa4hiVUyBQxtdbKZdvnwqWZo8Lv83tmdBTtn98UXwCzUKCEnjJqEch4OV3ekv6mdJZnMNecdJ_6HeW4c12zset4TLdW7S-pWHNhWYOGVYfydRMppZMbSdff3848rCRSHrf2pHoKiOClRRfpiOMGXil20EFG__Xgt9h_mpWmse7eVywVTW8AVZGrLq-D3cSIurRl7GuH-LrEdXSFZcJUQxy-THhV1ukJe7s5hd2mkV1n5obRId9N6p4sh3pmWYxFfzcGZQ7zgmvfl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9f37d892.mp4?token=r0ygulF8TJgNvROsI4PmDIB5Mi_rLcnpQZJPshwDKlxkQMqu3oqs7-nbL9IqmqzKwgOEng_fVa4hiVUyBQxtdbKZdvnwqWZo8Lv83tmdBTtn98UXwCzUKCEnjJqEch4OV3ekv6mdJZnMNecdJ_6HeW4c12zset4TLdW7S-pWHNhWYOGVYfydRMppZMbSdff3848rCRSHrf2pHoKiOClRRfpiOMGXil20EFG__Xgt9h_mpWmse7eVywVTW8AVZGrLq-D3cSIurRl7GuH-LrEdXSFZcJUQxy-THhV1ukJe7s5hd2mkV1n5obRId9N6p4sh3pmWYxFfzcGZQ7zgmvfl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری از تولد شیرین تا شهادت در کنار پدر  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458059" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0Ra2QYjf5cs7ZoWmID0Jy5QrtokBJ-fItFhVYk5Q5UnajP4tfG5IZGgrdSkuRmO-wgruYSAjtlfS68IE2ZC87rjREBfxTEEmQ4TWYvqIESEtRkiKReia4Wg_33yC7KoqkjcX-sSXVvbca77KnK_9KFq7tod33nlZtBJPnx_gD93bHHIhYiOcEaGVeAWLzE3TRB3E1O2b5WPjUZjJsiu7tTY0_nih8v5c0e-AUushNZbIKLbQEtd5Xb_uYsEFSQgf2wa0tIndAqHjvzOx4_EJ_B2sVhJOIu9L_X21GBOYUNvHSn2XHNfohIyq-iAjs_bL10s7LDyga7yHY7OKM9xeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقيف محمولۀ داروی قاچاق در بندرخمير
🔹
پلیس شهرستان خمیر: در جریان اجرای طرح مقابله با قاچاق کالا و ارز، مأموران انتظامی از یک خودروی سواری هزار قلم داروی غیرمجاز و فاقد مجوز به ارزش ۲ میلیارد ریال کشف کردند.
🔹
در اين رابطه يک نفر دستگير و با تشکیل پروندۀ قضایی جهت سير مراحل قانونی به مراجع قضایی معرفی شدند.
@Frasna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458058" target="_blank">📅 00:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458057">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiX1oqupt7supy0DD1xF6_a4jZmDCMR0B0D7zTbwulwfUU8atxkTaSqCS2AKYsLFuHUTuRBOuwFDWE1U7NYXbjo179LiYdv7hFcYFQo9ekxEqXbPO53Bj-ECyNhnUe2Hcgqzi6vD7I7tR3vibeRjQIPY7JwDIPbqYjI9kEqtSb9cv_pEd6g6WFOMpl2u4tCeHLD2LCRGfTVmM0mn57PAcAKp0WjTqD-ObvYvr3oL57W6NVGmDyeVta5kU0BMbOBOkb9ts1f_OnJ3ilwJDFGY0LDurrtB6-zfzd_wnvgrSeoQGm4GNe0eonkXfUS7dttvqHrv3XZm7eDI8fmnWYReHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شنیده‌شدن؛ خانم‌ها از این اشتباه دوری کنند
🔹
گاهی درد و خستگی واقعی است، اما نوع بیان آن باعث می‌شود به‌جای شنیده‌شدن، فقط احساس گناه ایجاد شود. مظلوم‌نمایی یکی از همین خطاهاست که فرد را در جایگاه قربانی قرار می‌دهد.
🔹
گاهی زن واقعاً خسته و دلخور است، اما به‌جای بیان مستقیم نیازش، جملاتی مثل «همیشه من باید بسوزم و بسازم» یا «هیچ‌کس قدر مرا نمی‌داند» را تکرار می‌کند.
🔹
این شیوه ممکن است در کوتاه‌مدت توجه ایجاد کند، اما در بلندمدت همسر را خسته و دفاعی می‌کند.
🔹
راه بهتر، بیان مستقیم و محترمانه نیازهاست. به‌جای اینکه بگوییم «من بدبختم که هیچ‌کس مرا نمی‌فهمد»، بگوییم: «من این روزها واقعاً تحت فشارم و به همراهی بیشتری از طرف تو نیاز دارم.»
🔹
پیش از گلایه از خودتان بپرسید: «می‌خواهم همسرم دلش برایم بسوزد یا واقعاً بفهمد چه نیازی دارم؟» این دو، نتیجه متفاوتی دارند.
🔹
جملاتی مثل «همیشه من»، «هیچ‌کس مرا» و «من بدبختم که» را به این شکل بیان کنید: «من اکنون احساس ... دارم و به ... نیاز دارم.» قرار نیست دردتان را کوچک کنید؛ قرار است آن را روشن، محترمانه و اثرگذار بیان کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/458057" target="_blank">📅 23:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458056">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb52a1b4f.mp4?token=Zj4iUESzKW-nrZoFQ35vqabcv4LrsGWrSFzEfBorIIPfR0OmcUj5C_Dwf_giNAF_4h2JP2BrcqjJoCFRv2zR1oTx8OFjUEEVdBeRiFCHUwd1dKK9eX6rZIPBPTGXpcmbn2gLUm0hvCE7J7to3MWMw3dHVJqBoMSjWwdNei201MhSikVlpkekSpUUTwA7-AaeXKbOlDWqCZN1PUCvz63m3d6MvNlGVTB6bM67n4mhYTBV68q7bJEPAw8a22KovP3tr5mzfw1qj78KqACXbFQy48OtqFZMd8fOLvQmSaZYPYoOyZ6biMnGIkQQLNI_TNp8GdPv1g4KJnEzDF0SDdWLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb52a1b4f.mp4?token=Zj4iUESzKW-nrZoFQ35vqabcv4LrsGWrSFzEfBorIIPfR0OmcUj5C_Dwf_giNAF_4h2JP2BrcqjJoCFRv2zR1oTx8OFjUEEVdBeRiFCHUwd1dKK9eX6rZIPBPTGXpcmbn2gLUm0hvCE7J7to3MWMw3dHVJqBoMSjWwdNei201MhSikVlpkekSpUUTwA7-AaeXKbOlDWqCZN1PUCvz63m3d6MvNlGVTB6bM67n4mhYTBV68q7bJEPAw8a22KovP3tr5mzfw1qj78KqACXbFQy48OtqFZMd8fOLvQmSaZYPYoOyZ6biMnGIkQQLNI_TNp8GdPv1g4KJnEzDF0SDdWLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: آمریکا از دوران دفاع مقدس هشت‌ساله در آرزوی تسلیم ایران است
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/458056" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458055">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
گناباد در شبی که با عشق و ایثار روشن شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/458055" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458054">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7090408440.mp4?token=r68AVXZOAfvpmTMIplUOGkpb6-W5GZMKywx0wRGCEWwVxBWkvyVxEKfrzBoghLY1JFRdOrPdJcNrcM6MPRMdoKcgHQUeVmTg6Fa6ZM_wLGvi2uSAWp0Oag0Qn3AHfpmtG2FjwYrjQZuZ3V6yqXWKOSINVV0zTEp_P1sONwFh5rxB2DRBsJlX_dKLsQEfeAaP9Q1L4YDqexd52IfazxDnuzXmINfpMrojsOK6mc5v7dCLHpTR-TuF--E9FO43jXLl2Phdhs5l_ziQ3rPAiot5pptKkgGMcDcw8kQZJm9K9VOkrPTPBzH-24stzqwIpwZmJmtSAMcIELZjuCk4jATIJg6Z2ss82r_OFX1lkLVMTV8qisofmrzjw05KUxFBdVn74fzQHUesXqvkO8xlJjP2T_z52Aupzh9DDpmSFq7jssg1BqgTDuzA0ONZ0GmbYzHom1FOZp--ZSrEB8yRJPql-OJ7SdfgrKRMOWMiw8NCtHR0rIbxOR7JFy7plpnqPp5vpwAahWiY-uqglJ-W1TlPIsK83iuktyukSXG7qFz4UGXXddLU0z4iRNfgvVTkyGulh82w0CIlBLtbRCLzehQ7sYYRnVutyogRDctahJ71N_zZBFLOvQ4m07wAu03n_911l1560iPGZZ_ZPyTvckC08C5X_FJsuwz9qXVpK6JuSLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7090408440.mp4?token=r68AVXZOAfvpmTMIplUOGkpb6-W5GZMKywx0wRGCEWwVxBWkvyVxEKfrzBoghLY1JFRdOrPdJcNrcM6MPRMdoKcgHQUeVmTg6Fa6ZM_wLGvi2uSAWp0Oag0Qn3AHfpmtG2FjwYrjQZuZ3V6yqXWKOSINVV0zTEp_P1sONwFh5rxB2DRBsJlX_dKLsQEfeAaP9Q1L4YDqexd52IfazxDnuzXmINfpMrojsOK6mc5v7dCLHpTR-TuF--E9FO43jXLl2Phdhs5l_ziQ3rPAiot5pptKkgGMcDcw8kQZJm9K9VOkrPTPBzH-24stzqwIpwZmJmtSAMcIELZjuCk4jATIJg6Z2ss82r_OFX1lkLVMTV8qisofmrzjw05KUxFBdVn74fzQHUesXqvkO8xlJjP2T_z52Aupzh9DDpmSFq7jssg1BqgTDuzA0ONZ0GmbYzHom1FOZp--ZSrEB8yRJPql-OJ7SdfgrKRMOWMiw8NCtHR0rIbxOR7JFy7plpnqPp5vpwAahWiY-uqglJ-W1TlPIsK83iuktyukSXG7qFz4UGXXddLU0z4iRNfgvVTkyGulh82w0CIlBLtbRCLzehQ7sYYRnVutyogRDctahJ71N_zZBFLOvQ4m07wAu03n_911l1560iPGZZ_ZPyTvckC08C5X_FJsuwz9qXVpK6JuSLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ قایم موشک
🎙
باصدای: سعید باقری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/458054" target="_blank">📅 23:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458053">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c246713.mp4?token=mcjPPEUL6rlhhdMCM3RyBnmL5S347GmCzp_Gq0WNEVSH_8Pt2qvx18tayKAgPU9vjRm6G7GPTgEsULn90jHbnueHWXZWiYGzrXtQ1Bh4kZ1dhoQZYl5YW1uePB0ksG5nCW9vABiUEYV8yVwVLYDrcHT6w54GomTzM4J2vtBJ0uj-6I_2AxE_95ABbuUAM_ux1vzDluGcLq46hWR2cI5g3Ky4ZKTXs5qhHWreFI8ClyD96gDjpQ11PKQK8__V2y8MKVxmDi4Lzip9gTYQBrXnUTuYpr-vj9mXjsyBrTA0Kx0zPn4pBWKCgQbGiILR2aXtK2SQtGzUwuyioZMgKoFoOb0scsKNhyvvppJekFN0rBTYZa-No41WZeyUfwNX63i0z6iAt2FiB5eW2xNyVqqmfauJ-tC8PKqedvRKH_aFD4CVL9Gh4rz8hvtsiD2zjkuM7GpKq-LJ2hIL7TVMcecndFO4ohx-zfdX5qabM3dREakW30V05TNeCGrAizl93sBNJf7O-8X1cXWTwVTldFXAxWsWmLX4wMmDfyYYh0SvH09t3-vznSITTbONZiUd30uR2caEP7UldaIDUi9G4KblS_pMW7XX1DmD6JhtwQDZz70ULiydkaU3MkURnSxpTOpa21aJPPD8p15YrbUC0-nZ6LBR7CQGQkf03j8XO93cDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c246713.mp4?token=mcjPPEUL6rlhhdMCM3RyBnmL5S347GmCzp_Gq0WNEVSH_8Pt2qvx18tayKAgPU9vjRm6G7GPTgEsULn90jHbnueHWXZWiYGzrXtQ1Bh4kZ1dhoQZYl5YW1uePB0ksG5nCW9vABiUEYV8yVwVLYDrcHT6w54GomTzM4J2vtBJ0uj-6I_2AxE_95ABbuUAM_ux1vzDluGcLq46hWR2cI5g3Ky4ZKTXs5qhHWreFI8ClyD96gDjpQ11PKQK8__V2y8MKVxmDi4Lzip9gTYQBrXnUTuYpr-vj9mXjsyBrTA0Kx0zPn4pBWKCgQbGiILR2aXtK2SQtGzUwuyioZMgKoFoOb0scsKNhyvvppJekFN0rBTYZa-No41WZeyUfwNX63i0z6iAt2FiB5eW2xNyVqqmfauJ-tC8PKqedvRKH_aFD4CVL9Gh4rz8hvtsiD2zjkuM7GpKq-LJ2hIL7TVMcecndFO4ohx-zfdX5qabM3dREakW30V05TNeCGrAizl93sBNJf7O-8X1cXWTwVTldFXAxWsWmLX4wMmDfyYYh0SvH09t3-vznSITTbONZiUd30uR2caEP7UldaIDUi9G4KblS_pMW7XX1DmD6JhtwQDZz70ULiydkaU3MkURnSxpTOpa21aJPPD8p15YrbUC0-nZ6LBR7CQGQkf03j8XO93cDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«انتظارات مردم از مجلس انقلابی»؛ صدایی که در شب ۱۷۷ شنیده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/458053" target="_blank">📅 23:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458052">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=OikkUuNPNjjnIfXEbFKQZfywzwHLHksybzRS_oYUhdycUEr9KkiE0R32u3r25zuCj_xiquuLYVUjrvC3SD4uWkN9O4xo-IelH_Jzn7BDmYqe0aqjr3BbNQSW17XvucP2qSwq9Y1jDsFeS5MgQsxwwUJozXtQad6VImVHSaJzTYgfZs-TzJ2EBg9Su4ecSGJxBblIPLny3mLERASQR7pY2imozb6a1BTZTMKMc3KbrBiqUfpWaURPJZKjBefoB0p8yEtY4mUJBmeBQepydWj1Rux1SK8CYgm1VsjsJT_IBdzsa_flTVZzGLjmwYtRthzKdruLki34wcr8UBRL73_AA36RIm3bcvO3M_GIo-QG_oxb470Hfr9PvY6ZzrTtcYkBPcf6r6lWKLmsSDueWoNE-LI0X3UHdzmsgS2SQmZseXateqIZ34qgu1CtlKm_BQACND-ID5iBN_8Zc2wns2FY8fHBK7TA6WlJLyyM8QCtFw9gbk8I8mWAwyD__z-VDoT5cPDS8c7rnsEVqzMxZnpRcbAQ6Xk6iESPgXs5iKr0rfTUnyyIgzuJpLQhs4hzxD_N2LktcsAljnwnkNDZGsbwvTLuc1de4v-1IIwBp06fx2hKtRE2HXJKsCqa0OQnhun6NQ_BS8kZQY4y1nrUDD8l9gr1LbSaBJb63dEKI_VM3FY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=OikkUuNPNjjnIfXEbFKQZfywzwHLHksybzRS_oYUhdycUEr9KkiE0R32u3r25zuCj_xiquuLYVUjrvC3SD4uWkN9O4xo-IelH_Jzn7BDmYqe0aqjr3BbNQSW17XvucP2qSwq9Y1jDsFeS5MgQsxwwUJozXtQad6VImVHSaJzTYgfZs-TzJ2EBg9Su4ecSGJxBblIPLny3mLERASQR7pY2imozb6a1BTZTMKMc3KbrBiqUfpWaURPJZKjBefoB0p8yEtY4mUJBmeBQepydWj1Rux1SK8CYgm1VsjsJT_IBdzsa_flTVZzGLjmwYtRthzKdruLki34wcr8UBRL73_AA36RIm3bcvO3M_GIo-QG_oxb470Hfr9PvY6ZzrTtcYkBPcf6r6lWKLmsSDueWoNE-LI0X3UHdzmsgS2SQmZseXateqIZ34qgu1CtlKm_BQACND-ID5iBN_8Zc2wns2FY8fHBK7TA6WlJLyyM8QCtFw9gbk8I8mWAwyD__z-VDoT5cPDS8c7rnsEVqzMxZnpRcbAQ6Xk6iESPgXs5iKr0rfTUnyyIgzuJpLQhs4hzxD_N2LktcsAljnwnkNDZGsbwvTLuc1de4v-1IIwBp06fx2hKtRE2HXJKsCqa0OQnhun6NQ_BS8kZQY4y1nrUDD8l9gr1LbSaBJb63dEKI_VM3FY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: برنامه‌هایی برای عملیات آفندی اقتصادی علیه دشمن داریم
🔹
دشمن می‌خواهد در اقتصاد علیه ما آفند کند و ما هم باید آفند کنیم.
🔹
امروز هرکسی حتی یک سنت از اوراق قرضۀ آمریکا خریداری می‌کند در خون کودکان شهید ما شریک است. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458052" target="_blank">📅 23:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458051">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_6U14lj2fQFluTulCN0oRlpR29hR3v-XnK50WBqlsZ5momzcLUOGhtQD4apCweRo5onTmIHIZTdB8LZm8mtZ_j2qYiRXAikH6XgZNw1fxIZy9F5y1baDBlFocjDb0_8-b44cCBnWS1pL_p3krwCyn5zPJZSUVYT1PURhMNCthAXeez_pmwHWso7upmczX49a3mcp_Zn-rE9EXEUkX9YAkrUeacqoExKovjYi5AbJemMGOzp83uectJVqcepbHlHLcxogwNbu0oA6soV9UcxcwIi7I9dbC7FibFi-ey4FNdc5sYmKIcrxx2yYUN1JWOd7loVaCPWivlmCG0OGd4_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری موشکی این ناوچه را به سپر دریایی تبدیل می‌کند
🔹
اینترستینگ‌انجینیرینگ: چین یک فروند ناوچهٔ جدید از خانوادهٔ «۰۵۴A» را وارد خدمت نیروی دریایی خود کرده است.
🔹
شناوری حدود ۳۹۰۰ تا ۴۰۰۰ تنی که برای انجام مجموعه‌ای از مأموریت‌های رزمی، از دفاع هوایی و نبرد ضدکشتی گرفته تا مقابله با زیردریایی‌ها، طراحی شده است.
🔹
ورود این ناوچه، بخشی از روند مستمر توسعه و افزایش تعداد شناورهای عملیاتی نیروی دریایی چین محسوب می‌شود.
🔹
کلاس ۰۵۴A که در ردهٔ ناوچه‌های موشک‌انداز قرار می‌گیرد، یکی از پرتعدادترین خانواده‌های شناورهای رزمی چین است.
🔹
یکی از مهم‌ترین ویژگی‌های ۰۵۴A، سامانهٔ پرتاب عمودی موشک آن است؛ این ناوچه به ۳۲ سلول پرتاب عمودی برای موشک‌های پدافند هوایی مجهز شده و از موشک‌های میان‌برد «اچ‌کیو-۱۶» استفاده می‌کند.
🔹
این ترکیب به ناوچه اجازه می‌دهد در برابر تهدیدهای هوایی از خود و سایر شناورهای همراه دفاع کند و بخشی از چتر دفاعی یک گروه دریایی را تشکیل دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458051" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458048">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28636dee93.mp4?token=QVSv1dlhdTlm-k2oK0k75fFUpl-PD4N6Rrp6gaGjoCH5sH0TQ7-8T9TFKqWZUuG7rlpdsV_sBOE3BYDrexxdaczMffl4yYM5bvGTUoPPUe--tFgXDkTCTpKta63MZS3k0Iz8DpeFFdf-UxwtLy8_fGMiLmOXcJCpyIB6ZMn28UtWZ4fo6MzmVF5SBbm0fPv0Rx6hhmygmlanBJhKLtlipqFpz1N2yFOuU4VDA_AgOlaGP6qNm_v6iwzxMjN4bOkYQD-HENd9PWzb2Tt_r8F5hAagFZDJqbA3n5G8DO_KXmnbngegOlPiTlFgIFS121JhcBqJYJd7dcCjnapZ4Hb80w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28636dee93.mp4?token=QVSv1dlhdTlm-k2oK0k75fFUpl-PD4N6Rrp6gaGjoCH5sH0TQ7-8T9TFKqWZUuG7rlpdsV_sBOE3BYDrexxdaczMffl4yYM5bvGTUoPPUe--tFgXDkTCTpKta63MZS3k0Iz8DpeFFdf-UxwtLy8_fGMiLmOXcJCpyIB6ZMn28UtWZ4fo6MzmVF5SBbm0fPv0Rx6hhmygmlanBJhKLtlipqFpz1N2yFOuU4VDA_AgOlaGP6qNm_v6iwzxMjN4bOkYQD-HENd9PWzb2Tt_r8F5hAagFZDJqbA3n5G8DO_KXmnbngegOlPiTlFgIFS121JhcBqJYJd7dcCjnapZ4Hb80w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: با کمک مردم در جنگ اقتصادی هم مثل جنگ نظامی دشمن را شکست می‌دهیم
🔹
مردم همان‌گونه که در حوزۀ صرفه‌جویی پای‌کارآمدند در حوزۀ سرمایه‌گذاری برای بازسازی اقتصاد هم خواهند آمد. @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/458048" target="_blank">📅 23:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458047">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ab451d35.mp4?token=A-pHrEByRiOcHGEf2LL_sNpKUBxwz6Hy4kK4OP5rnBSbxEGrNhxH8hf7j0GA7dImxRyF7RTQflBV2bqtpVIVnxjZq46NNm_Z4dOfM1ggdMdsd-xxY6tAJLMUb7jXMtPLppC0YUo0EDrF-80oCBsH8SHNzJfWgiLLAgiZf9_x9DzEOU6NbxKKJ89o_C9Oa-GNxbbbr-7YcjJUFcdgY9GhTuJo-qKVvs1ZTXzv0yIw9-mfJwigXM-gJ9evLToZNTPTElaM-C3qizopu7KJXdzFlk3vO76bRsT0zE5OHiPZjrNDtN9V1buZV_jnUnkyouFrbd7I5Goyc-jGwqj9gDutAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ab451d35.mp4?token=A-pHrEByRiOcHGEf2LL_sNpKUBxwz6Hy4kK4OP5rnBSbxEGrNhxH8hf7j0GA7dImxRyF7RTQflBV2bqtpVIVnxjZq46NNm_Z4dOfM1ggdMdsd-xxY6tAJLMUb7jXMtPLppC0YUo0EDrF-80oCBsH8SHNzJfWgiLLAgiZf9_x9DzEOU6NbxKKJ89o_C9Oa-GNxbbbr-7YcjJUFcdgY9GhTuJo-qKVvs1ZTXzv0yIw9-mfJwigXM-gJ9evLToZNTPTElaM-C3qizopu7KJXdzFlk3vO76bRsT0zE5OHiPZjrNDtN9V1buZV_jnUnkyouFrbd7I5Goyc-jGwqj9gDutAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: مردم صرفه‌جویی بزرگی را رقم زده‌اند
🔹
اتفاق بزرگی در حوزۀ صرفه‌جویی رخ داده که آمارهای آن به‌زودی منتشر می‌شود؛ باید در این زمینه واقعا قدردان مردم باشیم. @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/458047" target="_blank">📅 23:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458046">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18bd0dbed.mp4?token=Sx2QjNRnit1yPXKr5791wb4XY4twQ3k0uGWEyMgRpH9q5w1P5FU3SvWCxzBCXOGOc3vFFHuH5VmPcTfxlOjm-EZQDl3q5CckFhEeYAGzBw09AUPb2wctXu7SsrqXU4P2Wcc9ceWEG7ts4D5mq1MaCbRSg6n-YeMi-p64sPNzM0m8Xehi3QaDNbWvGEZbWHNsroAykHITbKzj6-XyPxLvRGY_7nW9j1soUJ0D195XhBEgVm28GpJblwnAjdPPQo7YiiFUSvMm7h9uObL4DxaIA1C3yehR8oPJ6b4G7SDjO211CqmKRsdAYUJDoDZVnnB7jshdPYw4WlVJAfJ_-u9KuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18bd0dbed.mp4?token=Sx2QjNRnit1yPXKr5791wb4XY4twQ3k0uGWEyMgRpH9q5w1P5FU3SvWCxzBCXOGOc3vFFHuH5VmPcTfxlOjm-EZQDl3q5CckFhEeYAGzBw09AUPb2wctXu7SsrqXU4P2Wcc9ceWEG7ts4D5mq1MaCbRSg6n-YeMi-p64sPNzM0m8Xehi3QaDNbWvGEZbWHNsroAykHITbKzj6-XyPxLvRGY_7nW9j1soUJ0D195XhBEgVm28GpJblwnAjdPPQo7YiiFUSvMm7h9uObL4DxaIA1C3yehR8oPJ6b4G7SDjO211CqmKRsdAYUJDoDZVnnB7jshdPYw4WlVJAfJ_-u9KuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: مردم می‌توانند با استفاده از اوراق گواهی نفت سود ارزی از نفت آتی کسب کنند  @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/458046" target="_blank">📅 23:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458045">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
به خاطر خدا فکری به حال معیشت و مستمری ناچیز معلولان شدید و خیلی شدید که فاقد شغل و درآمد هستند و توان کار کردن ندارند بکنید. قانون مادۀ ۲۷ معلولان مبنی بر پرداخت مستمری به میزان حداقل دستمزد، سال‌هاست که کامل و درست اجرا نشده. معلولان شدید و خیلی شدید چطور با مستمری ۲ میلیون تومانی در این گرانی و تورم زندگی کنند؟
🔸
رئیس‌جمهور پیگیر حقوق اساتید شده‌اند. ما چه جوری می‌توانیم با ایشان ارتباط بگیریم که کارمندهای قرارداد خرید خدمت اداره کل راه و شهرسازی یک ماه حقوق نگرفته‌اند و معاون توسعه هم تهدید به اخراج کرده است؟ چطور می‌شود پیگیری کرد؟
🔹
چرا هیچ‌کس درباره آنتن‌دهی اپراتورها، مخصوصاً ایرانسل چیزی نمی‌گوید؟ تازگی‌ها می‌بینی یک روز کامل آنتن ایرانسل می‌رود؛ علاوه بر اینترنت، مردم کار و زندگی دارند و منتظر تماس واجب هستند.
🔸
درختان صد و ۲۰۰ ساله در منطقه متروپل بندر انزلی (معروف به باغ زیری) به خاطر تغییر کاربری و بی‌توجهی به منابع طبیعی در حال قطع‌شدن هستند و کسی هم پیگیر آن نیست.
🔹
از صبح تا الان در خیابان کارگر هستم برای تأیید پزشکی اسناد رسمی تأمین اجتماعی. گفتند سیستم قطع است. نزدیک ۳۰۰ نفر کارشان راه نیفتاده. من خودم دارویی دارم که دیگر آزاد به من نمی‌دهند و الان تأیید هم نمی‌شود. امروز باید دارو بگیرم. می‌شود فارس پیگیری کند تا این قطعی سیستم در مراکز دولتی، مخصوصاً کارهای حساس دارو، درست شود؟
🔸
فرزند اوتیسم شدید ۱۸ ساله دارم که در منزل نگهداری می‌کنم. از بهزیستی نه حق پرستاری و نه هزینه لوازم بهداشتی هیچ‌کدام را دریافت نمی‌کنیم. الان که وزارت کار می‌خواهد تعرفه مراکز و حق پرستاری را افزایش دهند، لااقل فکری هم به حال کسانی بکنند که هیچ حق پرستاری نمی‌گیرند و چند سال در نوبت هستند و با هزینه دارو و پوشاک، بچه‌ها را در خانه نگهداری می‌کنند.
🔹
دانشگاه جندی شاپور اهواز هر ماه به بهانه‌های مختلف حقوق نیروهای شرکتی رو با تاخیر پرداخت می‌کنه تا به امروز هم حقوق نگرفتیم.
🔸
سایپا مرداد ۱۴۰۴ فراخوان اسقاط خودرو فرسوده داد و طبق تعهدی که در قرارداد نوشته شده، باید یک ماه بعد ماشین را تحویل می‌داد. الان ۸ ماه گذشته و ما را با خانواده و هزار مشکل دیگر بدون ماشین نگه داشته‌اند. هیچ‌کس هم پاسخگو نیست. خواهشاً شما که خبرنگار هستید پیگیری کنید.
🔹
خبری در خصوص عدم پرداخت حقوق پرسنل شهرداری کوت عبدالله استان خوزستان کار کنید. ما فقط حقوق اردیبهشت را دریافت کرده‌ایم. مگر نیروهای شهرداری انسان نیستند؟ با این شرایط گرانی، جنگ و گرما، پرسنل شهرداری خط مقدم خدمتگزاری هستند. همه ما انقلابی و بچه همین کشوریم؛ چه فرقی با سایر دستگاه‌ها داریم؟ ما سال‌هاست در این مشکل فرو رفته‌ایم و هیچ پاسخی دریافت نکرده‌ایم.
🔸
۲ سال قبل قرار بود سایپا معوقات ما را بدهد، اما هر بار که زنگ می‌زنیم جواب درستی نمی‌دهند. آخرین مرحله که زنگ زدم گفتند بروید شکایت کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/458045" target="_blank">📅 23:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458044">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07642de9.mp4?token=UkXbTgRmjgcdnGBMtZyFqCO26xbJHzwWmVyEenbPvQ6F8dI4IRQsM0BB-hRkLAdc_uiZDjzwbiKNq9VlKYn9TRsF7Vxvxi8j26glWyIrVCJvGIb4MLfN52jj4vmAR6mr507gbL46sTburbgZ-e762wL0m0AfNHU6w4Hk3BOu6KqtisgPHOEiNqbxBz9j0Pk_AdDhT9ZRF2FNnhqhuB3jqsPMoG1rGwkNvqc2-B2ijLSTTwuEz5yDHYQypRttew_8niSM_oR-52F51FRgl7bztX2k1BcIIpzg5L9L4WxcCd0FwrxA3XEPUppsa1uRAEM23sSQC-TxFfqBkGehC4v-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07642de9.mp4?token=UkXbTgRmjgcdnGBMtZyFqCO26xbJHzwWmVyEenbPvQ6F8dI4IRQsM0BB-hRkLAdc_uiZDjzwbiKNq9VlKYn9TRsF7Vxvxi8j26glWyIrVCJvGIb4MLfN52jj4vmAR6mr507gbL46sTburbgZ-e762wL0m0AfNHU6w4Hk3BOu6KqtisgPHOEiNqbxBz9j0Pk_AdDhT9ZRF2FNnhqhuB3jqsPMoG1rGwkNvqc2-B2ijLSTTwuEz5yDHYQypRttew_8niSM_oR-52F51FRgl7bztX2k1BcIIpzg5L9L4WxcCd0FwrxA3XEPUppsa1uRAEM23sSQC-TxFfqBkGehC4v-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: از نیمۀ دوم سال حداقل برای بخشی از دهک‌ها افزایش مبلغ کالابرگ خواهیم داشت  @Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/458044" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458043">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gaj0JsHDbiKTPnbG2iGz8WH6PntJtAzU-Cdl1KKjtrZQWUBIhJYOmRco3A6XQ7P60LFto1fSABYasTcAQnSYge6Zpa96hCP-BwS6N5idybmT76M64v_z7n2GTaZG8Ote1RaKRsKTTb3-NYAh1ighzKL530PfoKyzwUOuDdvVeGyZDdOum_hzv5bNFq4Jghum2inLQ6_UHMvJ0XO1WzqAKQSMbMqmg9tOlXwhYYL7ijreIpItGT8perrNhOhiH8JQdPVuSKuz2RHc3S-ewDthwVRmcVznAf22PmRnD4ukSE_XLE-t5ChlGNF_yaWX_Zf1QPXu7CC3ayB7NCZes5slyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: معیشت معلمان در اولویت کار ما قرار دارد
🔹
کاظمی: معیشت فقط حقوق نیست و ساماندهی نیروی انسانی و پرداخت‌های مختلف نیز بخشی از این موضوع است که اقدامات قابل‌توجهی در این زمینه انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/458043" target="_blank">📅 22:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458042">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRqaQmSPD9HoZ_dFz5ddaAFxLWnJ4DcsvYHEAySYz-IscXJkttGr98ZHnSYsJJKt7zQTNvwAF5g4L5a5lXGzIYH-9GS24n_f5UII1elrSSF5uXOa3Rf47wEqPr9vfKYKBaNZ2X0iO8vgxMxVGLb8grCLFxtxfodHIljmGY1p0VFCK95xBaa46pWAE7HWA4LrHljM59sAcIUgUKFMBx_J4k-u3bek-GODXAX_phy3LvuSQw8ES8e_X9L-9yPURWMGab1MVbMgACrlZ0_NihkybRBUc7Jn5H9znmAKKk7v6JuKEmmcmxBNtTjOK_xMy-TnhM_NjClhpBx-J68L_26J1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح: مدیریت دولت در طول جنگ  تکیه‌گاه رزمندگان در مقابله با دشمنان آمریکایی صهیونیستی بود
🔹
ستادکل نیروهای مسلح و قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): مدیریت دولت در این دورانِ دشوار، در پرتو رهنمودهای حکیمانه و هدایت‌های ارزشمند فرمانده معظم کل قوا حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای (مد ظله العالی)، علی‌رغم تمامی فشارها و تحریم‌های ظالمانه، تکیه‌گاه رزمندگان در مقابله با دشمنان آمریکایی صهیونیستی بود.
🔹
تدبیر و حمایت‌های همه‌جانبه دولت در مدیریت لجستیک و بسیج امکانات کشور برای پشتیبانی از نیروهای مسلح، قدرت بازدارندگی نظام را در برابر دشمنان متجاوز دوچندان کرد و این هم‌افزایی، همان رمز ماندگاری و پیروزی‌های ما در برابر بدخواهان این سرزمین بوده است.
🔹
نیروهای مسلح جمهوری اسلامی ایران، ضمن تجدید میثاق با آرمان‌های شهیدان، اعلام می‌دارد که با تکیه بر توانمندی‌های بومی و دانش نظامی روزآمد، همواره در کنار دولت خدمتگزار برای صیانت از تمامیت ارضی و اقتدار سیاسی کشور ایستاده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/458042" target="_blank">📅 22:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409d0b0c66.mp4?token=RMa56G0vbRz-2qVhInbn7gUbufEnTeAs0uR1HYO_l24stttc59I9yiXddIrW6lAKBxQFaXJnp77GwnzckvAFc1CWAvxMNbWbIMwizdG0lLwNy6__AYJlruNEgmFbChwOtQtTQjC1XUPdYcfoO7V_yqZ0mCm-V80l9jQUAudlho97orVgk65SiukthCu5IICQGkj91QZLm0r0atBfK9pKfU7a1SNExKDGUSuymKqiWEA8qbKKYUI1hIkDWUrHeLNmnbNohHJ5txcw0NdM99AkATrWx6T8zRbm3fL54axpHxy6ZR1Fyyl53cfiRXoj7cMIJHtpiC0D_kPAvLdCOR0DEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409d0b0c66.mp4?token=RMa56G0vbRz-2qVhInbn7gUbufEnTeAs0uR1HYO_l24stttc59I9yiXddIrW6lAKBxQFaXJnp77GwnzckvAFc1CWAvxMNbWbIMwizdG0lLwNy6__AYJlruNEgmFbChwOtQtTQjC1XUPdYcfoO7V_yqZ0mCm-V80l9jQUAudlho97orVgk65SiukthCu5IICQGkj91QZLm0r0atBfK9pKfU7a1SNExKDGUSuymKqiWEA8qbKKYUI1hIkDWUrHeLNmnbNohHJ5txcw0NdM99AkATrWx6T8zRbm3fL54axpHxy6ZR1Fyyl53cfiRXoj7cMIJHtpiC0D_kPAvLdCOR0DEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: نیمی از بودجۀ دولت از طریق مالیات تامین می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/458041" target="_blank">📅 22:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458040">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e285c274b.mp4?token=FO7cOEYun-I5NRaahS9SdkCHFFF6lZXFiOmCCO7GXPjD2W_8IQ6LuoucSmi2vbUm995-53jxD8WX-YVBMT9wh0qchTeVAD7xM_oI-ExYMUVa7ttLtcXJ5ghBunnSo9jG7ed9H7PuYwNC81xv-PMQOXBPcpn57neSGAjHcfHaLEcSZqNJOl7DvKdOuyxn-XqPAE_Lg5_-9AkTFigp_S3-2Pz5H7IVyW07WwY2tx5V8BpRsS_YKUazxw81E3pcHIJ8uaN7pQVNSJ_4qtkYk3mxGoVCr6UQjAG0lPp1b_wZST3lorcuAzhBJHHVBZz67JFVpfuPT_7f3Gfo9tamW2HpeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e285c274b.mp4?token=FO7cOEYun-I5NRaahS9SdkCHFFF6lZXFiOmCCO7GXPjD2W_8IQ6LuoucSmi2vbUm995-53jxD8WX-YVBMT9wh0qchTeVAD7xM_oI-ExYMUVa7ttLtcXJ5ghBunnSo9jG7ed9H7PuYwNC81xv-PMQOXBPcpn57neSGAjHcfHaLEcSZqNJOl7DvKdOuyxn-XqPAE_Lg5_-9AkTFigp_S3-2Pz5H7IVyW07WwY2tx5V8BpRsS_YKUazxw81E3pcHIJ8uaN7pQVNSJ_4qtkYk3mxGoVCr6UQjAG0lPp1b_wZST3lorcuAzhBJHHVBZz67JFVpfuPT_7f3Gfo9tamW2HpeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: افزایش فعلی قیمت ارز ناشی از التهاب در فضای رسانه‌ای است
🔹
تلاش می‌کنیم وضعیت بازار ارز را به حالت عادی بازگردانیم. @Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/458040" target="_blank">📅 22:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458039">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJJW5pBh_tBhn1VB8V6IPhK86IZerhUhYmuAZ99z-_QVKJXfW07YdJDkq-p1F6EhdO2Znx7eriMFRC9VyXn9nDfQpXgh3OHWmTLIztJb8Hj99tFEItXASWFaV-Ih_zkHndlQASQi6VEJ61VHOj8NqUxvWUCxt5L4lqG8hZkk08A3WJtJqrG_Xc5izYRzpAtmx5BoNkwhq4L0OxmDSqboj_vZsrMLcKL9wPyUIWJaikUigvJjj3EZySjCsN-C8Ahu-txYegSRP9eMVvndqfJeFux8J8kWLrWhy9YujZ6iuKyID3E3gtYOGsVoZ3_qTItr3nPKQbmJ118dRByPB574Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار فرماندۀ ارتش پاکستان با رئیس‌جمهور ایران  @Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/458039" target="_blank">📅 22:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458038">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7d7db24e.mp4?token=pFIbsXOjhA7zf03QlBtCPEwNwS3VQ8tNu0atMHfQql9jtOU6D6V7Mpzz15EMzGcCXDyBQogHx6P61CGaEhuGwvificgPErNd_ugJgi6ddaPw4ZVeFcVXSqRO0pCaQCzL7XdEMcEcimS_k1ILEsihn6oN0pYaQcSaTZh5SVrcfa0gcVzlivuBiNtqQiilWvmy3Uc1kYjd2MSQYF3Nuw2BvG7f50b8dQjHgL4Ttm21kJJQTz5ct26cHOpe4Lh5jhi62hys7cZnq9UWQCS4lYhnKlYrzQYS9P2YJb56Jx6H3B8WQLQS9PAFXhSWmzV9RRYYNTpNNXR417n25n_0MXb-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7d7db24e.mp4?token=pFIbsXOjhA7zf03QlBtCPEwNwS3VQ8tNu0atMHfQql9jtOU6D6V7Mpzz15EMzGcCXDyBQogHx6P61CGaEhuGwvificgPErNd_ugJgi6ddaPw4ZVeFcVXSqRO0pCaQCzL7XdEMcEcimS_k1ILEsihn6oN0pYaQcSaTZh5SVrcfa0gcVzlivuBiNtqQiilWvmy3Uc1kYjd2MSQYF3Nuw2BvG7f50b8dQjHgL4Ttm21kJJQTz5ct26cHOpe4Lh5jhi62hys7cZnq9UWQCS4lYhnKlYrzQYS9P2YJb56Jx6H3B8WQLQS9PAFXhSWmzV9RRYYNTpNNXR417n25n_0MXb-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: در میانۀ جنگ اقتصادی خیلی از اطلاعات و تاکتیک‌ها را نمی‌شود بیان کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/458038" target="_blank">📅 22:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458037">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEQBPrzf1ftTCP81cQ3TuPuXLBUMlmmM7gZ6PJcLDwH84sfkCCFWdI2Ra231hN5GAZdyNE3ECjOEDLLjVKB1rEj1Q04_99NKIUH9por5ldoCqL6HgrFTREJAWeg7GHEL69iu99rk50P8P_ysjK_AHcL2rVhsdRW9izxbdx-7vzoO_RVAQcuzYG-o_R-vZAua7yIBp6_vAkobMxJJP8VX1tI7Cu9GCviokEjHQxqkJ6jitRw4nIjPybnR8NHNRHdbsVwLwHgwHOZLNdSM-gmcVQ_YAZP-LpfNhPNt8y1bDpW2yirrvCKAH0kgC0i2_ugrX5fa1swwue-M9dWQoQHmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال در صدر ماند
🔹
پایان هفته سوم لیگ‌برتر ایران
📊
نتایج:
فولاد ۳ - ۰ صنعت نفت
گل‌گهر ۳ - ۰ چادرملو
ذوب‌آهن ۱ - ۱ مس شهربابک
خیبر ۲ - ۳ پیکان
ملوان ۰ - ۱ فجر
تراکتور ۱ - ۰ پرسپولیس
@Sportfars</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/458037" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458036">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ee66b32e.mp4?token=GtZ-zcPjD5EZSn-LjfCmGbZJ2JjGXt9s0p_DMxguPfCTvWw37h0q1uw1iomo9ku8qYIBg2RuuIieB8AKaX4hk5KJZw4pR5fr0hBsF9DnYyDHTa0jACEK52Z1dc3h5eQvYsSSWMWqhO67KTWmWQowwps-NLO5oWkJLwdl9dTBy09W3dxOK5PDM6nU5tBomp85GrvmVDxrQPu1YGKVGJE9FAt5aghU4QTc4-MNxGua1PrFpz6Xkoa_NLZu8PqydUnSgnWzqRm_h3lnA3A8tiDYsZwF5OMil-eYZWc_bwF2bFxi5JfnOLHXVLTuNuuZhRKR3NG3bR1PNYcpjvYw4KM2Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ee66b32e.mp4?token=GtZ-zcPjD5EZSn-LjfCmGbZJ2JjGXt9s0p_DMxguPfCTvWw37h0q1uw1iomo9ku8qYIBg2RuuIieB8AKaX4hk5KJZw4pR5fr0hBsF9DnYyDHTa0jACEK52Z1dc3h5eQvYsSSWMWqhO67KTWmWQowwps-NLO5oWkJLwdl9dTBy09W3dxOK5PDM6nU5tBomp85GrvmVDxrQPu1YGKVGJE9FAt5aghU4QTc4-MNxGua1PrFpz6Xkoa_NLZu8PqydUnSgnWzqRm_h3lnA3A8tiDYsZwF5OMil-eYZWc_bwF2bFxi5JfnOLHXVLTuNuuZhRKR3NG3bR1PNYcpjvYw4KM2Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ وزیر اقتصاد به اسکات بسنت: این‌بار هم شکست می‌خوری
🔹
ما مدت‌ها منتظر این روزها بودیم و می‌دانستیم که آن‌ها چنین برنامه‌هایی دارند.
🔹
دولت کاملاً برای این جنگ اقتصادی آماده است. @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/458036" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458035">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52051e8e8b.mp4?token=ma1ynH2vJvaMw76b5-PCR88_zQWnI2fRa_7N7gPRyi3Qj6yCj7mZ1AUv4j29aOcnyVo5JW03OlafyAnSEG9hVwi8qCblAOzJ6HaG2uOLMr1V79MPM-1VAEo68LgAa_rAv58Aw9fGCG4qjIiWKROsvy78bTuY9o6hFm2EGN4bman0nJkQTuVSFnYabT_wT0Vry4hzSu8ym5croy5o-W6hUf10_L_9JQUVM0laLj5qu0_weas0HDuX5fbZjkEa022QOhkvUgkltSZZtDIeV6fDTfYIgLYLmfTTiJdfdMvReqxy2HExJBZgS5H5CPKx81N3qOUxauKrJZIDgFiiRjn7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52051e8e8b.mp4?token=ma1ynH2vJvaMw76b5-PCR88_zQWnI2fRa_7N7gPRyi3Qj6yCj7mZ1AUv4j29aOcnyVo5JW03OlafyAnSEG9hVwi8qCblAOzJ6HaG2uOLMr1V79MPM-1VAEo68LgAa_rAv58Aw9fGCG4qjIiWKROsvy78bTuY9o6hFm2EGN4bman0nJkQTuVSFnYabT_wT0Vry4hzSu8ym5croy5o-W6hUf10_L_9JQUVM0laLj5qu0_weas0HDuX5fbZjkEa022QOhkvUgkltSZZtDIeV6fDTfYIgLYLmfTTiJdfdMvReqxy2HExJBZgS5H5CPKx81N3qOUxauKrJZIDgFiiRjn7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد
🔹
سرلشکر رضایی: در دیدار با فرمانده ارتش پاکستان: آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/458035" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458034">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5f443076.mp4?token=EqSIAGqLiklksHx9tJli-ILtV22xrM9waKcqI3BDKRRGfRx2WI9cWtW4in-24Na3KaEAuMFpcB2x9gIUV3wHjcbcXhSW29Uskv8T2GUjtkdTXnCSgvhMw0awLuZENgV0Ng_fZk6jVKFXpGdoy3n_q0085oGafIQeu4ycrzzR6iURb-jHj4t0RjRi6VJn2eGfKqKZJTOfNRSxXhk9iyBj5JERD6HLBVIi-m-7VEUof1_ynZhYTVu00eWOceuCICmTQG4DxAm0sh3LiADPQsnX7WflSbXKsMrAR91L59a2R9eRzXTclFNsFh_qqnaaktjBZspjf63_dSv7gyKcVUBF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5f443076.mp4?token=EqSIAGqLiklksHx9tJli-ILtV22xrM9waKcqI3BDKRRGfRx2WI9cWtW4in-24Na3KaEAuMFpcB2x9gIUV3wHjcbcXhSW29Uskv8T2GUjtkdTXnCSgvhMw0awLuZENgV0Ng_fZk6jVKFXpGdoy3n_q0085oGafIQeu4ycrzzR6iURb-jHj4t0RjRi6VJn2eGfKqKZJTOfNRSxXhk9iyBj5JERD6HLBVIi-m-7VEUof1_ynZhYTVu00eWOceuCICmTQG4DxAm0sh3LiADPQsnX7WflSbXKsMrAR91L59a2R9eRzXTclFNsFh_qqnaaktjBZspjf63_dSv7gyKcVUBF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: پس از جنگ از بیکاری ۶۰۰ هزار نفر جلوگیری کردیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/458034" target="_blank">📅 22:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a6cab2e09.mp4?token=FanmKuNcI-nFPWaCNKYjfXKVOk-SvQdIWcrh5WnFPuSiv2i-6Fj32A-I2Goewf4ECdYr5F2nY65oI92fi__L4T2atPVVeMWCMYUjw9yRdOheQmQ7up5wnNgeaNSWN7GmQ6IaMfw-wJPmda9zYeK7unbhmZqLuz_51zwC_rNrml1WMJ5Z-QrfaTnB06Fh2ZJdr7_3h3ap3MJL0oZOH8JIVzBC06Bk0dvM7GdtJm2SE7bzAk2R6qj6bXmxaF_7gp3Wk5QFDi_d2r0K-v82w0ltiTDMSSyh5Y_SkNnj_MikrkPY5-TZs9GiBr8zlZ4n5CH5ogMD-atP5GFaR1Ewa8BFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a6cab2e09.mp4?token=FanmKuNcI-nFPWaCNKYjfXKVOk-SvQdIWcrh5WnFPuSiv2i-6Fj32A-I2Goewf4ECdYr5F2nY65oI92fi__L4T2atPVVeMWCMYUjw9yRdOheQmQ7up5wnNgeaNSWN7GmQ6IaMfw-wJPmda9zYeK7unbhmZqLuz_51zwC_rNrml1WMJ5Z-QrfaTnB06Fh2ZJdr7_3h3ap3MJL0oZOH8JIVzBC06Bk0dvM7GdtJm2SE7bzAk2R6qj6bXmxaF_7gp3Wk5QFDi_d2r0K-v82w0ltiTDMSSyh5Y_SkNnj_MikrkPY5-TZs9GiBr8zlZ4n5CH5ogMD-atP5GFaR1Ewa8BFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: پس از جنگ از بیکاری ۶۰۰ هزار نفر جلوگیری کردیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458033" target="_blank">📅 22:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfbc72996.mp4?token=J89NMhkE37tIddhTz-F2PzLxA7TDtlLLDWHAw39pq2r7sFAgXyFzYLLl63NR0h9jJIwgtqFULunj-GFF_lwg1gxf-w-E6z7RQ9JH_DcpA2demb2uU-6yDLBtBpQx94hJwNst2zvHAf4afwvXxK-9zBZkmJHxu5DfngVSr_04I_5POqj6HgA18SMnL1yF4jQCx5m2FsqTPAyGAeWnBKNm65e5OQIzoqMFJ0pN4KpLGZI8XXPPjKgg2-HljIk1QD9-vqAil2gueYZ3VoZroOi4E_A2dcK9e6OOdITA7qcl4iLH70N0SZ0hZmYwknIXy69uYzuOrkCkuPDWWHWlmd2WMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfbc72996.mp4?token=J89NMhkE37tIddhTz-F2PzLxA7TDtlLLDWHAw39pq2r7sFAgXyFzYLLl63NR0h9jJIwgtqFULunj-GFF_lwg1gxf-w-E6z7RQ9JH_DcpA2demb2uU-6yDLBtBpQx94hJwNst2zvHAf4afwvXxK-9zBZkmJHxu5DfngVSr_04I_5POqj6HgA18SMnL1yF4jQCx5m2FsqTPAyGAeWnBKNm65e5OQIzoqMFJ0pN4KpLGZI8XXPPjKgg2-HljIk1QD9-vqAil2gueYZ3VoZroOi4E_A2dcK9e6OOdITA7qcl4iLH70N0SZ0hZmYwknIXy69uYzuOrkCkuPDWWHWlmd2WMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری از تولد شیرین تا شهادت در کنار پدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458032" target="_blank">📅 22:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458031">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac5db7e37.mp4?token=qq3ZuwN2qE8OX-AGPFRWwWCwgqlbRDfoQG5dIrvztJoYV2cFhnWgjQYsiIDAEKhTTyIiq_eig5nzKXwnF6Y61GC4JMdpYzOEyEADI4ktWkaKXByuq5ca-Zk4wM6RcOxa1Mkk3hJWGaXsiWaSpppKds7-g0MAgHS6VyBkkbmbfF1Gt1x_i0sXQaCYOqyAJsKu7TFbXjJ5uJP2mmqidEDE87Qgu4A66DxL_ArcuMawNcPm0iQ3FcM1S_DTr-xmd5wD9Hvltku4rZ0HkAQpkhFd7Q7VBSvEgzaOTIY2V2r7dhOH-KpfkyP7AojCJnct4knN4dC92r_nwKL7g6DNQBDML2_M-oYFIk1fG2dPjeBlV3u1WH9gBSvM6xlxwcDTb0-_nfuZnvv1TjlpD4DfZayCSSm4h8wi2SF_1DGuamXpTKIJ4h5VoK5Gd28n_Sni6M8dvqG1DQrWVoQyh8kgQUaNTMzZFV0v9RisaSmj6CZ9wwvvYJt_U3Ef-lctvfc9aI6eSCicDqJPSueeGyBHRO9RyH5BokBvb16C_sqIuFr3s1mVLlhW-xCS9Qz04dFDUIUNVwtHLj25Tpa1yevKxudVENfI9a4E411bH2Y7d3TmGPPo_OU1njhemOLyeKk0T0xCjVYV5MpMHDCLolIpcZburuuXroUDsMP95On8LCJ8Bb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac5db7e37.mp4?token=qq3ZuwN2qE8OX-AGPFRWwWCwgqlbRDfoQG5dIrvztJoYV2cFhnWgjQYsiIDAEKhTTyIiq_eig5nzKXwnF6Y61GC4JMdpYzOEyEADI4ktWkaKXByuq5ca-Zk4wM6RcOxa1Mkk3hJWGaXsiWaSpppKds7-g0MAgHS6VyBkkbmbfF1Gt1x_i0sXQaCYOqyAJsKu7TFbXjJ5uJP2mmqidEDE87Qgu4A66DxL_ArcuMawNcPm0iQ3FcM1S_DTr-xmd5wD9Hvltku4rZ0HkAQpkhFd7Q7VBSvEgzaOTIY2V2r7dhOH-KpfkyP7AojCJnct4knN4dC92r_nwKL7g6DNQBDML2_M-oYFIk1fG2dPjeBlV3u1WH9gBSvM6xlxwcDTb0-_nfuZnvv1TjlpD4DfZayCSSm4h8wi2SF_1DGuamXpTKIJ4h5VoK5Gd28n_Sni6M8dvqG1DQrWVoQyh8kgQUaNTMzZFV0v9RisaSmj6CZ9wwvvYJt_U3Ef-lctvfc9aI6eSCicDqJPSueeGyBHRO9RyH5BokBvb16C_sqIuFr3s1mVLlhW-xCS9Qz04dFDUIUNVwtHLj25Tpa1yevKxudVENfI9a4E411bH2Y7d3TmGPPo_OU1njhemOLyeKk0T0xCjVYV5MpMHDCLolIpcZburuuXroUDsMP95On8LCJ8Bb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر دیدنی جشن میلاد پیامبر(ص) در الحدیده یمن
🔸
فردا آغاز هفتۀ وحدت و روز میلاد پیامبر(ص) به روایت اهل‌سنت ‌است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/458031" target="_blank">📅 22:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458030">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c7a7ecd2.mp4?token=lT1aLFAkiIEZqXmkbcDFODU9HVTSyp6BsXY4Q54jtz8kQQSNSQx261K-7KP3kC2aQUxTH_AW6dhoS6KGZsjGQhVDk7Ebegii3HKQ333E8BHQiqI-vc3Ws1VtusZN2GKFx5W5TboDZuPILHr-VYjZOB8ujZR_2ooRx4GpUIpZUOz0FlVXAVpNriheCFxAfqVN7_BCRGHlIpgLfPnFh7wTQaFcA4ZfgvEXe-k8NrkbK77COcA1o6ys1-rDAuHZUxdztIg3aOfIgHG92zITuHh4oddvE4iFm83Qq8_Io17R_73vsuXhScz57PCTFSwE9oIlG0vTriiWzFB5lX3cfuCWVBlIOfdpDQylOU4Vx3RSXrXAS9s5lZQBoSaZ_OvH4Q6GqE0XJYStEEGR2vu9DfKS9WC9swJNeijRZtN6GqQ2U4HL8yKGJKAf8o_G4cMfvqSK8otuxwFJSgeoGhd3bdJ31fazhsqhoB8X-Jk_BHHIqa0E8oHgoyM1P-5_rCbB6A7JtK9Kn7QXcxYCF6lplmc1ZI_FLM53cSKqINZ2fEeD_-AxX1i7GTUyueq-C2zRCrJyKKpojRTxflg10Bu5Ac0d2RVdiL6Coi8VYtRcA51kVnfvIgWsG9T2s0YdPB9AhixwHLKsxDPJWpq-xEcjQdahCZTb9FhnlDjiH-f_si2MUv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c7a7ecd2.mp4?token=lT1aLFAkiIEZqXmkbcDFODU9HVTSyp6BsXY4Q54jtz8kQQSNSQx261K-7KP3kC2aQUxTH_AW6dhoS6KGZsjGQhVDk7Ebegii3HKQ333E8BHQiqI-vc3Ws1VtusZN2GKFx5W5TboDZuPILHr-VYjZOB8ujZR_2ooRx4GpUIpZUOz0FlVXAVpNriheCFxAfqVN7_BCRGHlIpgLfPnFh7wTQaFcA4ZfgvEXe-k8NrkbK77COcA1o6ys1-rDAuHZUxdztIg3aOfIgHG92zITuHh4oddvE4iFm83Qq8_Io17R_73vsuXhScz57PCTFSwE9oIlG0vTriiWzFB5lX3cfuCWVBlIOfdpDQylOU4Vx3RSXrXAS9s5lZQBoSaZ_OvH4Q6GqE0XJYStEEGR2vu9DfKS9WC9swJNeijRZtN6GqQ2U4HL8yKGJKAf8o_G4cMfvqSK8otuxwFJSgeoGhd3bdJ31fazhsqhoB8X-Jk_BHHIqa0E8oHgoyM1P-5_rCbB6A7JtK9Kn7QXcxYCF6lplmc1ZI_FLM53cSKqINZ2fEeD_-AxX1i7GTUyueq-C2zRCrJyKKpojRTxflg10Bu5Ac0d2RVdiL6Coi8VYtRcA51kVnfvIgWsG9T2s0YdPB9AhixwHLKsxDPJWpq-xEcjQdahCZTb9FhnlDjiH-f_si2MUv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌پیروزی لحظه‌آخری تراکتور مقابل پرسپولیس
⚽️
تراکتور ۱ - ۰ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458030" target="_blank">📅 22:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458026">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC0PlvI_4BzUg5g9p4ELd5n0qO_pV1f4HK3M2IHH0Et1IdSPijk7Ijgb4JS1xn9y4ICBTFrcjfb6014cGBkGaGl6esYXbsn1_r1cZm6hYsplPER3VuPCelNaYQe5goK7bGUJ7DgBKnkMGCVOTu13Lej0oY6eEVF1UJXz5Ez-4jQlmr6I9h4qxLsLYllGV7EbwEVEIaP-jJbozYOl8TCwiA1HG3qY2AUbOplZfq7k7Lo7KTNYOmJTvvSBghyxYCrWdsEUXrNWkpvnr9nZgXPIEBeiQTkeN3A7mTQ07fXgnFjbgXq5W2kMRiutIRRxfj1pRVtVDBZskH9vKkxh6usC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdZIjkfTA9FCLOKtUnNcftp03B1nucf3lsZcIhapLlIv3IpuuAZj4FuVDTGwgc7tGPLkSoeX1h_DIH97jOEH21FlD6_m_lP9GfMuldKyb8PXuB5lFfUCt--Lw5TJwDKi7vtwvU0YHrYaLbJhuSFmkNW9Roe3RjU_IXu-P5Ap4pkPdAGN0PpMoYm_WOwxlVBjBNOySgzpWpsGvS6bMZOdG5pn2QElyMeVVM53heF8zMFM4D5IA32Q4XHp2kvmoSqW6Njb5txvZH1Np8IqomQz2DwOBa2L4zAmrPX87ehJ812FsCdTYFNGm4ls8_OoQT5PG-k8voiYgBEKZTqqt387QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxLUMCr-MbD7cWyoQsI6QzRg2iNgt55P9fXqH8jOA5t5BhfJisX2dcbxCqflCsi1eZ9roE9w_vTc05FvwwWgUB-mvOLiBwTMhyD8Y6x7X1LewHSfrCYfrYWwAMIkL4T6kYLQgas5SORGb2WKNiHLAaZkj1VO5vRzwjWn2pU2Qjs3TCWJFJdbQfKoIf8de5ZBiS6kpu4ETVY8_YTC69BXC8C0j-ikn0RAGNRJ7i2Lmx65dMy3HkvTbSOqlRKH3TE1DVDuzpISf35ysj7wVcngNPnu6tSPzdxOPQIsRSVBeTMjnGBHert7rzNkUc94uw3SJhTgrTutoxWuXVLXGhYSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNE0uA8UsjJOjZ0XsltMWYWXAj8zTCDe9T_52wwoxgNZk8KSDLGdZ4y_sJW6ap6PzDfF_jUoulNcVbq5mTKjeIKKxFCtFENy5xcuxBE1J2eud7KUcwSjpzjiDEMBYvcOVtWyTy4beB7dSlwxiSU4-pA9kQnei8l4L3EjlWgrA5Y553eMTbubF77876xX247cQJ4Tlo-Oz2aydlaun75hTQNupbskBK7nd951znq3tm2rNNy2QFKyyC1JaSHzv_ZstiVa4LoOvUe-3o21-zjzgtz1F7MQZfa-JzZhe3zigcqNu9xDUSZpkGDVxHk78nxut4GvMsHrunEBdg_bCFBHZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: به آمریکا بی‌اعتمادیم و باید رفتارش را تغییر دهد
🔹
سرلشکر رضایی: در دیدار با فرمانده ارتش پاکستان: آمریکا باید رفتارش را تغییر دهد و اقدامات عملی درخصوص اجرای شروط تفاهم‌نامه انجام دهد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/458026" target="_blank">📅 21:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458025">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47f59a878.mp4?token=nWTE_8M2qMXQ2bi_aAHRrgD_PQ0AavNV8YlwBRm8MMyoLRh-eqqjqg1v3iuXOELoDhjAztBZEwdqn4_VnKN3PGjyxY3CmprMFe679kt1y7LZNrOLGAh6DwtJI_1mO7lPuc5bsw59XXLXG90KL_wWLBc8Hi17AuTB8fjw0TuC0WJvcIiKgSxVY9xkyTdHvGkSCQ7gKOuL6dfK5M-KdlN0Qlz5KAxDvBHq7bb2rTVnlRkj7pcBTgAtIFPMOh7uBeL2f9lgQGjYFUAFNG0Z_6a4yH4KOF4bcu9HMpS6xP3hWG7BwUZXRQa4bBeuld30YVXR8giwbnY9HswC8OYiYUycRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47f59a878.mp4?token=nWTE_8M2qMXQ2bi_aAHRrgD_PQ0AavNV8YlwBRm8MMyoLRh-eqqjqg1v3iuXOELoDhjAztBZEwdqn4_VnKN3PGjyxY3CmprMFe679kt1y7LZNrOLGAh6DwtJI_1mO7lPuc5bsw59XXLXG90KL_wWLBc8Hi17AuTB8fjw0TuC0WJvcIiKgSxVY9xkyTdHvGkSCQ7gKOuL6dfK5M-KdlN0Qlz5KAxDvBHq7bb2rTVnlRkj7pcBTgAtIFPMOh7uBeL2f9lgQGjYFUAFNG0Z_6a4yH4KOF4bcu9HMpS6xP3hWG7BwUZXRQa4bBeuld30YVXR8giwbnY9HswC8OYiYUycRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سازمان تعزیرات: با هرگونه امتناع از عرضه کالا در فروشگاه‌های اینترنتی، برخورد حداکثری می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/458025" target="_blank">📅 21:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458024">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اداره‌های کردستان فردا زودتر تعطیل می‌شود
🔹
ادارات و دستگاه‌های اجرایی کردستان فردا سه‌شنبه، ۳ شهریور، از ساعت ۱۱ صبح تعطیل می‌شود.
🔹
این تصمیم به مناسبت ۱۲ ربیع‌الاول، میلاد پیامبر اکرم(ص) به روایت اهل‌سنت و آغاز هفته وحدت گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/458024" target="_blank">📅 21:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTJTS11bGKV0xizMoteGzc3Sul3wtwzwS--rf_P5ypi_Tw8IF-FOFZLKMPkz8b8B2pVEqs62j0H8oV_I57Npn0uzoMyb4Bix1XaifnaGxgIgNuWPEbLtBE2gGzKVAV_BjoX6VcCu0VftI9vygoCsyhxSx36s94jBpYOAUO0FEnmFQkF56-RUZuOv7-BXg47iOqnVOCK_BR4OiaqhON0_TpViwvQBOxV5TUX_AXn2VMmmYpOR-OwIO9z7jmydJtpJc2eQ8LIY97qYKLGcB4gR2m38em_K-PMJzsNKdkqmDLBO-TEfMRKwJp-653WbPbzfxoDv7vmd8LWDPexWAG8VaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تحریمی جدید ترامپ؛ تکرار فشار حداکثری با پیوست تبلیغاتی
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا امروز جزئیات طرح ادعایی جدید ایالات متحده برای تحریم‌ها علیه ایران را اعلام کرد.
🔹
اظهارات اسکات بسنت نشان می‌دهد که طرحی که ایالات متحده قصد رونمایی از آن را دارد مشابه همان فشار حداکثری است که در دولت نخست ترامپ اعلام شده بود.
🔹
اسکات بسنت گفت هر کشور یک جدول زمانی مشخص برای متوقف کردن فعالیت‌های خود دارد و اگر کشورها اقدامات لازم را انجام ندهند، ما از طریق اختیارات خود به‌صورت یک‌جانبه دست به اقدام خواهیم زد.
🔹
وی همچنین گفت: وزارت خزانه‌داری ایالات متحده: ما به کشورهایی که قاچاق نفت از ایران را تسهیل می‌کنند و اجازه استفاده از بانک‌های خود را برای منافع رژیم ایران می‌دهند، هشدار داده‌ایم.
🔹
وی تصریح کرد: کشورها برای بستن فعالیت‌هایی که توسط وزارت خزانه‌داری شناسایی شده‌اند، از جمله بستن شعب بانک‌های ایرانی در خارج از کشور، مهلت زمانی خواهند داشت.
🔹
بسنت گفت: هر نهادی که فعالیت‌های پولشویی را به نفع ایران تسهیل کند، بر اساس سیستم مالی مبتنی بر دلار آمریکا از این سیستم کنار گذاشته خواهد شد.
🔹
او همچنین خاطرنشان کرد هیچ‌کس در برابر تحریم‌های ایالات متحده مصون نیست.
🔸
دولت ترامپ بعد از خروج از برجام نیز اعلام کرد که قصد دارد تحریم‌های جدیدی علیه ایران به کار بگیرد. اساس آن تحریم‌ها نیز تحریم ثانویه کشورها و شرکت‌هایی بود که اقدام به معامله با ایران کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/458022" target="_blank">📅 21:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754b64eb06.mp4?token=mcEsjOhfwH8OVxnVWCQU5r28kJF2LJOBXF3GZ5_a6heJEBZCSBhGdTwxPPyYlAsm11C9aNj-A76MiimvHFlsu5Z33CUnIv-WNW-w4P1Y1wUZ7211uzltqNawmdf2V9TGBPcc4hYr6CQX4-nAKCf-uiOEisem8HqDcIIepinf4vPoa_pYjvumrXVirkac25BZevQmUACCKNH91DzwajUHDmVoNdepy8njHqOkLSoufH04uwIjwkc7kyj4l9l9D7GnGPxwwaXQTA9qZbTUq2qKxyviPp9VwCmuA2GTDaj333NuUi_57jRSv7ou8AecIJLz86GmjJ31d0_NNbhMocv1gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754b64eb06.mp4?token=mcEsjOhfwH8OVxnVWCQU5r28kJF2LJOBXF3GZ5_a6heJEBZCSBhGdTwxPPyYlAsm11C9aNj-A76MiimvHFlsu5Z33CUnIv-WNW-w4P1Y1wUZ7211uzltqNawmdf2V9TGBPcc4hYr6CQX4-nAKCf-uiOEisem8HqDcIIepinf4vPoa_pYjvumrXVirkac25BZevQmUACCKNH91DzwajUHDmVoNdepy8njHqOkLSoufH04uwIjwkc7kyj4l9l9D7GnGPxwwaXQTA9qZbTUq2qKxyviPp9VwCmuA2GTDaj333NuUi_57jRSv7ou8AecIJLz86GmjJ31d0_NNbhMocv1gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده جنگ آمریکا شکست خورد؛ نوبت وزیر خزانه‌داری رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/458021" target="_blank">📅 21:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c117fcb8c4.mp4?token=udjS7ENhG9SMpVOQH9L7EAikdYu0KIEneRccAhxb0TxVLFrfO37DyctYIYm8vetZLQ8RAGvD01YkzwRwCMtLQl4hIsuzlWHI1CvaYu_wBiIQpUWVk3h1b1kKkiojPAzOaZevoSXdyDaUmzGrkfjnhFLJ4CzK5vuWha86jElBis-5nOxTRdWPYejc4ShDI2Swf_Ckda0xJYLZHnIJjC78KJ0xn9linx3KxzDDm94NOaK-TaM6Nb6eO94QYOB3xho8c1Nu-PGkzYOsHuvUG-lmQA_t-ETAudVpXdwsGIiLnV9_xAMWjS2fT4Q965FLPFXC1VHaS9b-M_wvTj_peUNu4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c117fcb8c4.mp4?token=udjS7ENhG9SMpVOQH9L7EAikdYu0KIEneRccAhxb0TxVLFrfO37DyctYIYm8vetZLQ8RAGvD01YkzwRwCMtLQl4hIsuzlWHI1CvaYu_wBiIQpUWVk3h1b1kKkiojPAzOaZevoSXdyDaUmzGrkfjnhFLJ4CzK5vuWha86jElBis-5nOxTRdWPYejc4ShDI2Swf_Ckda0xJYLZHnIJjC78KJ0xn9linx3KxzDDm94NOaK-TaM6Nb6eO94QYOB3xho8c1Nu-PGkzYOsHuvUG-lmQA_t-ETAudVpXdwsGIiLnV9_xAMWjS2fT4Q965FLPFXC1VHaS9b-M_wvTj_peUNu4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استانداران و فرمانداران سکان مدیریت را به دست گرفتند
🔸
رویکردی که با عبور از پیچ‌وخم‌های اداری فاصلهٔ تصمیم‌گیری تا اجرا را به حداقل رسانده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/458020" target="_blank">📅 21:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cb723a7e.mp4?token=QYnj_EMMTM2SAhMr22sIQ3KWQ4rxKjNAVCwa0gaiOkXQcZolYv-bcQlrLb4e-IXepEIC3s1a2y728lwYlF-N3jf4M7uF8JIP0Z187dWZi-P94uKs-5bvbPKdBfadC0p1fA9A_dm45E_JzkOyXzJ_dIax7JH_VRZErNn-sQGChghNYLVnQdXlLg1XrHjP82zuSIg7dZgjb3vTu9-1Ft4KIVfftm9nOK38T-1HLfa_GEBwpHifrJt1GOseJvKnrBUex54LRGj7yS690wBcUfjKkOaPU98aCbOBbbpDvrOXXyK1s6hS9SQXLhEWxeF22PcmY4-NayOQiZUw96pdu9aKoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cb723a7e.mp4?token=QYnj_EMMTM2SAhMr22sIQ3KWQ4rxKjNAVCwa0gaiOkXQcZolYv-bcQlrLb4e-IXepEIC3s1a2y728lwYlF-N3jf4M7uF8JIP0Z187dWZi-P94uKs-5bvbPKdBfadC0p1fA9A_dm45E_JzkOyXzJ_dIax7JH_VRZErNn-sQGChghNYLVnQdXlLg1XrHjP82zuSIg7dZgjb3vTu9-1Ft4KIVfftm9nOK38T-1HLfa_GEBwpHifrJt1GOseJvKnrBUex54LRGj7yS690wBcUfjKkOaPU98aCbOBbbpDvrOXXyK1s6hS9SQXLhEWxeF22PcmY4-NayOQiZUw96pdu9aKoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس اتحادیهٔ طلاوجواهر: قیمت‌ها ممکن است هر لحظه افزایش یا کاهش یابد؛ مردم معاملات خود را به زمان ثبات قیمت‌ها موکول کنند تا متضرر نشوند
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/458019" target="_blank">📅 21:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYJqMYnDakxOyLuWzybXUaBvkK-kui6FFaF4Xlwuz3vGJyHNJfKB999PyR8A5ORh9pdW1TmuvAypvIYK8rfhTFdn7NHlDBxM0Y3XfdBdHlWY-xsM76TRANCZEcRKE05CwUgM63517NKMMb4KbmCWNpnQVwxF2YgjlAQ_VYljbe4rlcplnURiDPMhjWvXE5jnDfZlZPPy4LzpbiladJ-7piRgNL62WygPbBdU_F6at_Tg022x8tUanSvqf7dc3K75H76CjmRzXQKLWu8khSnaAkJy2N2jL8GG3Gfmbr8ki8x82qdZuPZTyx1i-nDH-zOnpDhbcfp4zRnMCrvPu7SXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
«راه تاز» برنامه‌ای متفاوت در شبکه سه با روایت دستاوردهای جمهوری اسلامی
🔹
فرهاد جم، سیروس میمنت، علی مسعودی، شهرام قائدی، پژمان بازغی، شهرزاد کمال‌زاده و آرام جعفری در این مسابقه با حضور در پروژه‌های بزرگ کشور، از نزدیک با بخشی از دستاوردها و پیشرفت‌های جدید ایران آشنا می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/458018" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458017">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-text">⭕️
💰
📣
✨
نسیم سرمایه
۳۰۰ میلیون تومان وام قرض‌الحسنه
با کارمزد ۴ درصد
‼️
📅
حداقل مدت میانگین حساب یک ماه و بازپرداخت ۳ تا ۶۰ ماه
🤩
🧮
لینک محاسبه مبلغ وام و اقساط
📱
لینک افتتاح حساب از طریق اپلیکیشن سرمایه
🔷
اطلاعات بیشتر
‼️
وفق ضوابط چنانچه حائز شرایط ­باشید
تا یک میلیارد ریال بدون ضامن،
تسهیلات دریافت نمایید.
#تسهیلات
#تسهیلات_بانکی
📞
با ما در ارتباط باشید: ۴۳۷۳-۰۲۱
#بانک_خوب_سرمایه_است
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/458017" target="_blank">📅 21:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458016">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/458016" target="_blank">📅 21:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458015">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f30fd87.mp4?token=RvtH__5weUwnvLsV9ysNKX8FVTx8_j_j9RJRjPwWl4_rR0zKN5qZ0tlL0aCJP21Vf-fHGDl_2k8LX_qDi9wWkpHhf2IozZDrtQgsovpPv95MERM0BRyMvry8c8XC3DzzWbdDZLv4j7auzyspdY7jwZa91iusIGU6YghBaFzUd6dZ-M6VDrpT8xbQx7cbe6BMERTeuw5bibZrHw4BR1BayGPOFKwYAbsLBhjaZiLDJmpgzdm09WtDydPvkLA07Xr-_gAH1ZFkxB0DU_dxLyWF1ZDVhFlJZ29MvztEUgQxUFESGfwr5hoypkzmA5gulsOkNIE9TxwzMt6Z9hsh5dCpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f30fd87.mp4?token=RvtH__5weUwnvLsV9ysNKX8FVTx8_j_j9RJRjPwWl4_rR0zKN5qZ0tlL0aCJP21Vf-fHGDl_2k8LX_qDi9wWkpHhf2IozZDrtQgsovpPv95MERM0BRyMvry8c8XC3DzzWbdDZLv4j7auzyspdY7jwZa91iusIGU6YghBaFzUd6dZ-M6VDrpT8xbQx7cbe6BMERTeuw5bibZrHw4BR1BayGPOFKwYAbsLBhjaZiLDJmpgzdm09WtDydPvkLA07Xr-_gAH1ZFkxB0DU_dxLyWF1ZDVhFlJZ29MvztEUgQxUFESGfwr5hoypkzmA5gulsOkNIE9TxwzMt6Z9hsh5dCpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات محکومیت دولت آمریکا به پرداخت غرامت با شکایت بیماران پروانه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/458015" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcMumUn4Yf36gWRYlexo9qRI2RzVUEfAJ28NMe1W-8MJ5zSx4KH6chCguiS6a5dej10rBQEFnsF7yClS_UHeFy56n-MhjEsebB96OiECarMIhOLyxQBpFQ5uKkO5oP2McVr5pZTzibJrvAtvw4sm-oVWCviFmRXBBJe7ighWBfebkcjLqi4euQ3aSiws8hjvizb8CSdYfGEft5eJzELidTdh6h6jj7w-jVQ3r0gObNs7nX7HdTTGQ51_nG2_T2jE77vQtLYmo3vFsdVvNjoam3Q85-J3TPnpBZej3rvB2dr9JoIIHpVj3ifKgb9l2gT-kF0HVzxvghoYu-CcLj0Hlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: کسی گُنده‌لافی‌های آمریکایی‌ها را باور نمی‌کند
🔹
شرکای تجاری ایران‌ به ما اعلام کرده‌اند که اظهارات آمریکا را به هیچ جا حساب نمی‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/458010" target="_blank">📅 20:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTXvWQ_-kuWE6IzvMP8CRchSyrO7vXa5M9SknWHuqJoVMpnPLYqLhuLkVq50-IZz-3FK24gIxGIzcDRoHxklTJk_Isn8sq57mQiYmC7n7eN3v4CfhVRzmNUhwWhzRmoXZfiWuBUNLzlEUHXA7vLebd4RCj8Qwl1OKEF3KYKYPH9dHyOnyUxeZULzv_-DidL-v8gb_I5yvehXigckVApOD9UWmTB2W3A0DkOYeVSClOFWq4XtsdxwTW0oBWiw6rk2meNNbX1tq3F5jcjon_pRLL39FhjesTVASrtqRsA14YDE8JsPL9Te62loYYsFytOKkjuf1qJGIRDjBTdP7NFVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ارز، دوباره بیماران کاشت حلزون را در انتظار قطعه گذاشت
🔹
اگرچه عمل کاشت حلزون شنوایی در ۱۶ مرکز دولتی کشور به‌صورت رایگان انجام می‌شود، اما کمبود قطعات یدکی و مشکلات تخصیص ارز، روند درمان و زندگی بیماران را با مشکل مواجه کرده است. از کار افتادن حتی یک قطعه می‌تواند به معنای
قطع شنوایی فرد و بازگشت او به دنیای سکوت
باشد؛ موضوعی که برای کودکانی که به مدرسه و زندگی عادی بازگشته‌اند، تبعات جدی دارد.
🔹
در پی ثبت پویش خانواده‌های بیماران در «
فارس من
»، پیگیری از مسئولان نشان می‌دهد تغییر سیاست‌های ارزی باعث تأخیر در ترخیص قطعات شده و برخی قطعات یدکی نیز
۱۰۰ تا ۲۰۰ میلیون تومان
قیمت دارند و هنوز تحت پوشش بیمه قرار نگرفته‌اند.
🔹
مسئولان تأکید کرده‌اند باید قطعاتی که واقعاً با کمبود مواجه‌اند شناسایی و برای تأمین فوری آن‌ها اقدام شود. جزئیات کامل این پیگیری و پاسخ مسئولان را
اینجا
بخوانید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/458009" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
