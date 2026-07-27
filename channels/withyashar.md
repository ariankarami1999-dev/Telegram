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
<img src="https://cdn4.telesco.pe/file/sob3OiAxUDMWZdDZx24K8lou3cpg6fCyCoRCxN3lsQCA0jC9htkMz_5uNiuM5VPLYqQ_8inGPgP0F-ZgTbF8Gevfb49FekOTInCHeqH763Z3MN4G2LbQyELYRkZFIEVRmdNl2BuOjyUgI1yR1qAujo4FB51b0_i8lzNfT-HX6CXJcaXjwa-TpZ2o-tce0uTXGgyRYkS2PpNJ-wY5TcTp0vCuNNetCG_ZKsCP5oBpclY18DhLv4DdogFGACtYZNmaFSwKcR3FT7IflWpm4aXRROtOtmZLLTqSwCoALKIRL7mbzroCdQHo1_ROHqnubJDhP-GDPehzdBHUM0zx-_29rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-19797">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست. @WarRoom</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/19797" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19796">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی وزارت خارجه: درخواست مذاکره کردن اصلا با ژن ما همخوانی ندارد
بقایی:ادعای درخواست مذاکره از سمت ایران، صرفا یک خبرسازی است. البته ما درب دیپلماسی را نبسته‌ایم، اما در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/19796" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkMa2tjEuVtwXScgeMEcsccMbonOibuaTJR_9xALs0BubIzCdhrEseWLgUgOsvjAXRqSK8TLgtV-xSup-MU4bTexlvg80vTZPHL12tjZ6yckcXFr88aHm-7II1PuJEQ8pHcUxah7UWmg6X5m8081heViEyKrpzO6712PSDWn8BP8yJ2Yj9-lHDLPpTL60M2lSadqGrdP631X0MRyKb9fAj5MQwvVZDbArlKIt77XKrPk2G7NiOqsZ4fCPBh3HPhXbYp_pFM5-dZuAYOOAUzaYREi15tgnHiM5X1Wlhi2_53QdCMJQHRAj957_nhtaF-R_INLQ_N-Y08PK54PXFL89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از «نیما مرادی» که در حمله اوکراین به کشتی ایرانی کشته شد. کشتی آنا از بندر آستاراخان عازم بندر انزلی بود.
@WarRoom</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/19795" target="_blank">📅 11:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
رئیس‌جمهور روسیه در دیدار با فرماندهان و نظامیان ناوگان دریایی این کشور اعلام کرد که ایران در جریان درگیری نظامی با آمریکا با موفقیت از به‌اصطلاح «ناوگان پشه‌ای» (شناورهای کوچک و تندرو) استفاده کرده و این نیروها عملکردی کاملاً مؤثر از خود نشان داده‌اند
، توسعه چنین نیروهایی برای ناوگان دریایی روسیه نیز ضروری است.
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/19794" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هواپیماهای تهاجمی A-10 Warthog برای عملیات احتمالی علیه ایران در خاورمیانه اعزام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/19793" target="_blank">📅 10:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=ImAfwuVrS2DDQWBU8H8s2S7IM-5RShd91uuZ_INpjlTm1uqc3RRz9eJdE9neGuHXV2e8XuXVlIpABiyaXFUVfx1a20w3ZPOfSr3EYZ7VrZ26c8XxfCLymo7Ai85kNG_LkMGEq0UKAWLcwEduu1O9V50zI9UnDOZZXt3Y4rQqQfC_HcxQ0rrJJ9lq0Keb38c2miBj_vCIqkGGL1Pkmq8s4zTOaZH3Mk-jdXQxvUesxrYiRdhuYrrRbFB3l4YUB2uTljae7UVus_SC4h42E3vTqEdYi9YdRIaF5l1Ma1LSN5yHRJZPQX0krk_4CUo4qCu1sOY3ZGd8NpKkGtq9Q72J4QC7vYm7_z5HkJoSeGU6Mgmc-FqjxqhCRMxv3yHu_AFe-PtYhGwg4_9XNHwnN9DMKNQgEivPqp4JJruVsatTTGVu_xE_B7EyoYTh2NlgR30sw6_vpLytZq7eP74ZFCGsdjuiyU5DQN3zLiSGTXPM9qCBSJZskiokhXjs_LG1nXJgItA-5DMusfOWSeRH5PQHBVvgUpamp2QE850DzWibQdzke9fNmbcPCECQJMMh-lvPW-M7Ld6I_b5qfS5qvgR9TuashTbEDBVPVXWhL8VjhDkNVPKp4p5Uw7sSVKTsihRF177YiRCttt7Xaj4_rGPFRGg-bi_8E6R1P5np3wV_KgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbe6758e6.mp4?token=ImAfwuVrS2DDQWBU8H8s2S7IM-5RShd91uuZ_INpjlTm1uqc3RRz9eJdE9neGuHXV2e8XuXVlIpABiyaXFUVfx1a20w3ZPOfSr3EYZ7VrZ26c8XxfCLymo7Ai85kNG_LkMGEq0UKAWLcwEduu1O9V50zI9UnDOZZXt3Y4rQqQfC_HcxQ0rrJJ9lq0Keb38c2miBj_vCIqkGGL1Pkmq8s4zTOaZH3Mk-jdXQxvUesxrYiRdhuYrrRbFB3l4YUB2uTljae7UVus_SC4h42E3vTqEdYi9YdRIaF5l1Ma1LSN5yHRJZPQX0krk_4CUo4qCu1sOY3ZGd8NpKkGtq9Q72J4QC7vYm7_z5HkJoSeGU6Mgmc-FqjxqhCRMxv3yHu_AFe-PtYhGwg4_9XNHwnN9DMKNQgEivPqp4JJruVsatTTGVu_xE_B7EyoYTh2NlgR30sw6_vpLytZq7eP74ZFCGsdjuiyU5DQN3zLiSGTXPM9qCBSJZskiokhXjs_LG1nXJgItA-5DMusfOWSeRH5PQHBVvgUpamp2QE850DzWibQdzke9fNmbcPCECQJMMh-lvPW-M7Ld6I_b5qfS5qvgR9TuashTbEDBVPVXWhL8VjhDkNVPKp4p5Uw7sSVKTsihRF177YiRCttt7Xaj4_rGPFRGg-bi_8E6R1P5np3wV_KgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتهای زیبای ریچارد نیکسون در مورد شاه و اتفاقات آن روز.
@WarRoom</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/19792" target="_blank">📅 10:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=jFN92xkoMufc7iKU_5i0u8KUI1BvKg78o72mXLfqCJCPVWt55xGLSKS__GvsabE7Iby_9bCIM2lBUtHR0rCXfEIFSpDqWPSeC3vrvWyhoOCL9qJ-UEqCOBi8Avqq5zQ9pgyM_yXv4mEfZxW-R8ItYkUL0SEkxJDwqoQWS5CHs6moC5E1InmxXaXRfSmxVoyAchhHXCaY6SUhNLwc7wKO_752x0zkyl2QLtcMEV3Bnw34nJDY8YNdBceETSwN2lQ9L0IDJt7cITnzUKGhyneJJwneURG8drgEyOp6gtc_2mULG6cqmZMgEt-LI_xzf2s0Qvze1gqKgIKtYFPmqG4aUTEn0l8Z6gmE4nxUo69VoWM1TK2OLh2yUUTeGbK4jZtP7Z4PsiQv1VJK8-GgkxhNMy1cF9NSlbZoKKQSUBhdsfqQRvSxJgKHCUdMhmFHnU6QdUis9masoeGvglU2oZ9ckYErvkmLcwezz5Nt23p76F0iejV646i_U1cxuA1WR6TMm0mz_BSmTgWtTGTFLjA6wPV9Xl-QJ8GkgKXungTLdrJvYzqUffp4Cnu-dZe12u3btZ3eC39PLSeUqCCXr0CClnSYUKUyDUihcGDY8u-m0jXQBS6Bfkg3UbqvFV1JLlaErCSHC5f_JrVMaqX-TrfQizH6mIjRrIigWGZw6cJitc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f90eed59a.mp4?token=jFN92xkoMufc7iKU_5i0u8KUI1BvKg78o72mXLfqCJCPVWt55xGLSKS__GvsabE7Iby_9bCIM2lBUtHR0rCXfEIFSpDqWPSeC3vrvWyhoOCL9qJ-UEqCOBi8Avqq5zQ9pgyM_yXv4mEfZxW-R8ItYkUL0SEkxJDwqoQWS5CHs6moC5E1InmxXaXRfSmxVoyAchhHXCaY6SUhNLwc7wKO_752x0zkyl2QLtcMEV3Bnw34nJDY8YNdBceETSwN2lQ9L0IDJt7cITnzUKGhyneJJwneURG8drgEyOp6gtc_2mULG6cqmZMgEt-LI_xzf2s0Qvze1gqKgIKtYFPmqG4aUTEn0l8Z6gmE4nxUo69VoWM1TK2OLh2yUUTeGbK4jZtP7Z4PsiQv1VJK8-GgkxhNMy1cF9NSlbZoKKQSUBhdsfqQRvSxJgKHCUdMhmFHnU6QdUis9masoeGvglU2oZ9ckYErvkmLcwezz5Nt23p76F0iejV646i_U1cxuA1WR6TMm0mz_BSmTgWtTGTFLjA6wPV9Xl-QJ8GkgKXungTLdrJvYzqUffp4Cnu-dZe12u3btZ3eC39PLSeUqCCXr0CClnSYUKUyDUihcGDY8u-m0jXQBS6Bfkg3UbqvFV1JLlaErCSHC5f_JrVMaqX-TrfQizH6mIjRrIigWGZw6cJitc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دیده نشده از مراسم محمدرضا شاه
@WarRoom</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/19791" target="_blank">📅 10:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏ساعت ۲۵ ایران ‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.» ‏انورسادات با لباس نظامى آمد،  ‏مستقيم به اتاق شاه رفت. ‏دستش را روى قلب شاه گذاشت،  ‏به انگليسی گفت: ‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»…</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/19790" target="_blank">📅 10:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صداوسیما: در ساعات اولیه بامداد امروز، ۶ فروند کشتی متخلف با خاموش نمودن موقعیت‌یاب خود قصد عبور از مسیر جنوب تنگه هرمز را داشتند که یکی از آنها دچار حادثه شده و بقیه تحت مدیریت ایران به خلیج فارس برگردانده شدند
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/19789" target="_blank">📅 10:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار الجزیره: نیروهاى ارتش اسرائیل، به همراه بولدوزرهاى نظامی، وارد شهر عرابه، واقع در نزدیکی جنین، در کرانه باختری شدند
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/19788" target="_blank">📅 09:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پنتاگن : از زمان شروع درگیری‌ها در ۹ اسفند، ۱۸ نظامی ایالات متحده کشته و ۶۲۴ تن زخمی شده‌اند
سی‌ان‌ان ‌: بر اساس اعلام پنتاگون، بیش از ۱۴۰ نظامی آمریکایی جدید به مجروحان جنگ علیه ایران، اضافه شدند
نام چهار سرباز آمریکایی کشته‌ شده در حملات ایران که از پایگاه داده‌های پنتاگون حذف شده بود نیز بازگردانده شد
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/19787" target="_blank">📅 09:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
ساعت ۲۵ ایران
‏ساعت ۹:۱۷ صبح روزِ ۵ مرداد سال ۱۳۵۹ بود كه اين خبر به دنيا مخابره شد: «پادشاه ايران درگذشت.»
‏انورسادات با لباس نظامى آمد،
‏مستقيم به اتاق شاه رفت.
‏دستش را روى قلب شاه گذاشت،
‏به انگليسی گفت:
‏«تو ساعت ٩:١٧ دقيقه مردى، ايران در ساعت ۲۵»
اما ‏آن روز كسی نفهميد معنی ساعت ۲۵ چيست؟
‏او در يک مصاحبه با خبرنگاران خارجى و داخلى ‏گفت: جهان عزادار شد.
‏امروز مردى از ميان ما رفت كه خواهان صلح بود، ‏بعد از او خاورميانه رنگ آرامش و آسايش به خود نخواهد ديد.
‏او فقط پادشاه ايران نبود.
‏پدرِ بزرگى براى منطقه خاورميانه بود و ‏روزهاى سختی را پشت سر گذاشت،
‏او براى دفاع از كشورش در مقابل دنيا ايستاد ، ‏او امروز صبح مُرد اما ايران در ساعت ۲۵ از حركت ايستاد.
‏اين خبر به ايران رسيد، روزنامه كيهان و اطلاعات با خط درشت نوشتند: «شاه مُرد.»‏
‏فرانسوى‌ها ضرب‌المثلى دارند كه حركت روز و شب ۲۴ ساعت است و ساعت ۲۵، ‏ساعت مرگ است.
‏به واقع ساعتِ مرگ محمد رضا شاه پهلوی ساعت ۲۵ ایران بود.
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/19786" target="_blank">📅 09:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش صدای انفجار‌بندر عباس ، ممکنه خنثی سازی باشه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/19785" target="_blank">📅 09:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19784" target="_blank">📅 02:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیغام های زیاد گزارش انفجار در‌ اهواز
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19783" target="_blank">📅 02:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=WLW1LzjNYmUxkoT-19L3aQgxPjA9xe1wxL-9n5o-WtN0DlW-CKKlwZTQrCbSq9gRUfh2sJxKNy9c79BF1YVCsGQEny4w4peI2hwqwzwopRszDyuOX1fS_jDYe6_zE78nDhhzEbnVTZVHF0mt_QA7PNRNTOosSAz2YoFeknfwa2lzBvSMmodfwzX-hw-zRNi8LvPmyaIO1-Njqfuc7RUsFp6YIFgV1tU559fx2HaJ31H75fIGv7AzTSTYRzaDdPD3WnEl8QrIFHGTLmwl0C44lUXTzFWFhmfC6c-26xWSYetZG40Hh9V_C7_n24DiltUNR7AIQ0chV9R6mMAb_2coiqhP-pdFjIon1a5517AHwTIrlFkZ3Jc_zwImvCZO8EKin2fI_6DFrFzYkuD37ZAsW-JwVO3oWC5UADO6sbXO70XrWdez1zAtREr1XkNRkuAWsC8j-BTI0DBIdn1_OtydKMc9oFDb2Z1Rq0kC_AFnLhpifG9_iQRTvweohtpDL5M4x1k5Dj3-gXrQlhxP6Cb8t3OWOqdU92Q4OID9ouMI0O9uN2fzgtyTWHbIdYS3UE2H-cAGJsI1MpxyE_K3J_bpqyCPPKRmvppkEUrTcWw1z_dhDq2e7APnd0B_R9vEo4_vO7pYSWyw4poj1_BJ-32c4wbzOGlK9aKxNHjmPvVijY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6daf7646.mp4?token=WLW1LzjNYmUxkoT-19L3aQgxPjA9xe1wxL-9n5o-WtN0DlW-CKKlwZTQrCbSq9gRUfh2sJxKNy9c79BF1YVCsGQEny4w4peI2hwqwzwopRszDyuOX1fS_jDYe6_zE78nDhhzEbnVTZVHF0mt_QA7PNRNTOosSAz2YoFeknfwa2lzBvSMmodfwzX-hw-zRNi8LvPmyaIO1-Njqfuc7RUsFp6YIFgV1tU559fx2HaJ31H75fIGv7AzTSTYRzaDdPD3WnEl8QrIFHGTLmwl0C44lUXTzFWFhmfC6c-26xWSYetZG40Hh9V_C7_n24DiltUNR7AIQ0chV9R6mMAb_2coiqhP-pdFjIon1a5517AHwTIrlFkZ3Jc_zwImvCZO8EKin2fI_6DFrFzYkuD37ZAsW-JwVO3oWC5UADO6sbXO70XrWdez1zAtREr1XkNRkuAWsC8j-BTI0DBIdn1_OtydKMc9oFDb2Z1Rq0kC_AFnLhpifG9_iQRTvweohtpDL5M4x1k5Dj3-gXrQlhxP6Cb8t3OWOqdU92Q4OID9ouMI0O9uN2fzgtyTWHbIdYS3UE2H-cAGJsI1MpxyE_K3J_bpqyCPPKRmvppkEUrTcWw1z_dhDq2e7APnd0B_R9vEo4_vO7pYSWyw4poj1_BJ-32c4wbzOGlK9aKxNHjmPvVijY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19782" target="_blank">📅 01:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXmvxI0ZJ8t_au-Sd7JAhZpAw1x-D2t6Fd5-GSHvKzQmF73ScU35DFDcKi7JCxNbEq6knhw2f3ESG_tnDthoGMMJrEcBY1KK7Y45pTlRGipqVdnv9erhplMnsxVfA9fs_lD25K8Be7Vo6Twm9qx5LZQ0zYTCg6tWfvKoFYNs1K_RReEmNLO8vNJMluFzVUxWp4cfCEzrcr-0DlqDrMolQ30JIywJr7MYcMoN-4UlTwIbccLK66vSESDT1tFAQpIaeho97Tt3rC6Rr6jVvTNPIq-G79GPe6IMpxLZHKTOgc6Foh_4MTIykIu4-YpoequrjeE0UFnrqUcegeVcnii21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری یک سایت خبری روسی مبنی بر کنترل مافیای لوازم آرایشی توسط حسن روحانی
رسانه‌های روسی در چند ساعت گذشته با انتشار خبری جنجالی از یکی از بزرگ‌ترین پرونده های قاچاق سازمان‌یافته آرایشی-بهداشتی در غرب آسیا پرده برداشتند.  طبق ادعای این سایت، حلقه اصلی این مافیا حسن روحانی؛ دیپلمات‌ سفارت فرانسه و فردی به نام مهدی‌زاده بوده‌ است.   طبق گفته این سایت اخیرا و در طول جنگ ایران و آمریکا دو کشتی محصولات قاچاق آرایشی تولید کره جنوبی، متعلق به وی توسط دستگاه های امنیتی ایران کشف شده است. این در حالی است که چند کشتی تجاری نیز در سال گذشته توسط دستگاه های امنیتی جمهوری اسلامی کشف شده که با دخالت سفارت کره جنوبی و پیگیری وزیرخارجه کره، این موضوع رها شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19781" target="_blank">📅 01:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رسانه های نظامی اوکراینی ادعا کردند: در صورت پاسخ نظامی ایران به اوکراین،ارتش اوکراین حملات پهپادی دور برد به شهر های ایران انجام خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19780" target="_blank">📅 01:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19779">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19779" target="_blank">📅 00:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جولانی: حزب‌الله به مدت 14 سال، رژیم سرکوبگر سابق را در جنگ وحشیانه‌اش علیه مردم سوریه همراهی کرد و باعث آوارگی و کشته شدن تعداد زیادی از افراد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19778" target="_blank">📅 00:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19777" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19776" target="_blank">📅 00:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19775">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ41uWKbYaimEA_qN9dke1czmiopPr1ujKiZUcwTGSDz8hYXejV-PkSIDrcRAF9eL7ENimcEl-PPjQDWF2ojDDpKXi4yXnDSRf2e0BSW2Z2B2wAv6oInpqOli_kgxO5j5I6o2p0NaHRSaemfu1qrozCXum34HQ53s4QS7D_G6bTRkf-suAZN4Jb-M6IqzXIifnEFuSwJJFAAzgqGf44LK6e9U2IkLsGRt8YPWjaCGkEDvF-7WDORXhVz0QXf9QzmGKXWX3nxLsY88E0dw0LuedXyPwvr-w5-U8vNYhuPjcvs0-G929r97k4Cfwjgp89s3oSWzk7eoNgza3KRkFkfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19775" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19774">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5YifZbWb0EOKAlAHgxbmujDPdkANDT3KmGY5WrMcrt9jkFKN14V640YMuZpDRLbzl62zRHJqs6o4XiCW6V5j5zcuEK00V7aY0dtH8M_YFcA06IjBxTShCWakcoDzQIV-JkJeTFj1zR-X475hIiHdgO6bBLbkMpRT7baI27hSH43TJyLJXJNssJfEDHuuJneQIO_E1z7xbpA_buBnJKAyFS67chrH2MsRfgHCLgK07-eZKJme5eY_ANy4fnldQnxwyVGI-sN0XVBaXzIIFg9lNTl7aHlzr471kFu1xh3aP2j7ZU4MgOWL5WR8utIPlOAInstNOlZQ6P5ENhseL2k4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19774" target="_blank">📅 00:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19773">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdioWZrfmvUfgBqh2cIxdSw6BT7OvlXQLL2okBob_GTvxrWqNew0UOPv7jagVtxJCI-3YJc_lY-mdDPc8EbymDgbZXJrefe5m9BboNTKTEjTbVgUyZCpKpctsVHnTFf2wzdybm0AC593TGV4owOWfNaairuRZAvm-7JCb4BSPCBQT4gCAEXcX1NxE-47rPF_m0waE7_8OaZSFby0MQZncQLLPhkZz-_Cy01yBh7F6lOnhpWJW_r__fmRqmPXG6Hs5_uc8MfAocOr8m-PPLGfdqAZudIo_IBH6Vex9IhKZOW-sBgV77_Uc1tC6SLWi_jygftB45ECw4XEVw8zmMWsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : فرشتگان نگهبان جهان
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19773" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19772">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=fplC2v2gjhbS4Aob_OSDyluRHkpMEZBhZDgzXHz9JQobIRmJaZUyoLl8voOX_-McsaNFqqRzArZLoByiMQRu3POizua_NMhcwdCAqGCZKHgFN_VMSuwEGuO2wHv5ZF6_0FkF6GRNUM1e6-HRisepbBzB3EeGBI4M2UnqP1WIznP25z5jlLSzW1VPjCppm5nK2lswA_qh8459jUfnGncL3O-2FdwJIROB09HMXqCM69VAhjAj0lCsOaoxZKRowhQnI2cPwyoKCYytfg8XP3VNLrA6ZdAIBQmeTJkQaRi1UjkoqLlSrQIfW4777dXD3X0IE8AB7JhzuHSe1kR9mJ9WJBUTUNgcOObhWIkDCeKVWHZDo58-DEo-H5uP6dTdWofXcmMhPJjVOi-Lfs5-XcmmLtgl_KIcWQYkSNtzmdFxmRgcnVrZmwH9mrhhnIeezhhLZ19I-_zQA-qZn6LgBDuDMesJ5Ww58JugoDrQ_Uf4oHtNBPXGMvsGP9ek52Y3WxwQZvTzwr_DXPK4QxYJDr7Dy_MY2y9B0lnrWeGV2cJqD7cjh_nO455tFgtMn66ehsxdpf7lJBMj0R0VWFPexOrEDUh1D5e8H1qX7lXwDAt97-cu6YkDTYDlLQLeyHXGn39vyG4Vu4uk11Ka-oNl05OI7URiBbWSz9VbAE-T1oX40bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e1f8494c.mp4?token=fplC2v2gjhbS4Aob_OSDyluRHkpMEZBhZDgzXHz9JQobIRmJaZUyoLl8voOX_-McsaNFqqRzArZLoByiMQRu3POizua_NMhcwdCAqGCZKHgFN_VMSuwEGuO2wHv5ZF6_0FkF6GRNUM1e6-HRisepbBzB3EeGBI4M2UnqP1WIznP25z5jlLSzW1VPjCppm5nK2lswA_qh8459jUfnGncL3O-2FdwJIROB09HMXqCM69VAhjAj0lCsOaoxZKRowhQnI2cPwyoKCYytfg8XP3VNLrA6ZdAIBQmeTJkQaRi1UjkoqLlSrQIfW4777dXD3X0IE8AB7JhzuHSe1kR9mJ9WJBUTUNgcOObhWIkDCeKVWHZDo58-DEo-H5uP6dTdWofXcmMhPJjVOi-Lfs5-XcmmLtgl_KIcWQYkSNtzmdFxmRgcnVrZmwH9mrhhnIeezhhLZ19I-_zQA-qZn6LgBDuDMesJ5Ww58JugoDrQ_Uf4oHtNBPXGMvsGP9ek52Y3WxwQZvTzwr_DXPK4QxYJDr7Dy_MY2y9B0lnrWeGV2cJqD7cjh_nO455tFgtMn66ehsxdpf7lJBMj0R0VWFPexOrEDUh1D5e8H1qX7lXwDAt97-cu6YkDTYDlLQLeyHXGn39vyG4Vu4uk11Ka-oNl05OI7URiBbWSz9VbAE-T1oX40bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش دیگری از‌مستند او قصد داشته در اوایل ماه مارس به فلوریدا سفر کند تا از دونالد ترامپ، رئیس جمهور آمریکا، بخواهد در بمباران حزب الله لبنان به اسرائیل بپیوندد.با این حال، بنیامین نتانیاهو، نخست وزیر اسرائیل، قبل از این سفر، توصیه کرد که درگیری گسترش نیابد و گفت که اسرائیل باید بر ایران متمرکز بماند و هشدار داد که حمله به حزب الله می‌تواند باعث یک جنگ منطقه‌ای گسترده‌تر شود.
نتانیاهو در این تماس تلفنی به گراهام گفت: «ما در حال حاضر بر ایران تمرکز داریم.» گراهام موافقت کرد و پاسخ داد: «این واقعاً توصیه خوبی است.»
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19772" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19771">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=PtkR_TUjQRTv9AXQ2cx2ui6n2-ancLI2RgD31s3VJIUBt6IiPsONr-qNwkWfv0bD1MfyAhsIlDkNh1YAzKbYVPQaEu4FESBGtWPZklnTAR453t5OoHbPP5HjaT9O0Zt5NHGcOEsSZ5nsxlCRNGbG6Zw2FIJjLUnbNadss6OovA6KRoYEkunZvUEntSOeU1OCmI-_66M5LrCFp6mq2rBdetU02wgxIyQdAgIOvmEcMh_szM_nXEIPBuWpyd9bdj8B7PhId9XOl-Rg4kET7Ogsa3tgf5QqjmyveZgNjn-BC-HgG0LHUtBGMC3nQvN3qBebO_eKA4LcdicyV9oOiO3jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de7526ff5.mp4?token=PtkR_TUjQRTv9AXQ2cx2ui6n2-ancLI2RgD31s3VJIUBt6IiPsONr-qNwkWfv0bD1MfyAhsIlDkNh1YAzKbYVPQaEu4FESBGtWPZklnTAR453t5OoHbPP5HjaT9O0Zt5NHGcOEsSZ5nsxlCRNGbG6Zw2FIJjLUnbNadss6OovA6KRoYEkunZvUEntSOeU1OCmI-_66M5LrCFp6mq2rBdetU02wgxIyQdAgIOvmEcMh_szM_nXEIPBuWpyd9bdj8B7PhId9XOl-Rg4kET7Ogsa3tgf5QqjmyveZgNjn-BC-HgG0LHUtBGMC3nQvN3qBebO_eKA4LcdicyV9oOiO3jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر مستند منتشر نشده نشان می‌دهد که سناتور فقید لیندسی گراهام در اوایل ماه مارس پیش‌بینی کرده بود که دولت ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «حرکتی تقریباً برگشت‌ناپذیر» ایجاد خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19771" target="_blank">📅 23:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19770">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وال استریت ژورنال
: ارتش آمریکا یک طرح نظامی تمام عیار برای مدت 2 هفته جنگ همه جانبه با ایران آماده کرده است که هر لحظه پس از دستور ترامپ آغاز خواهد شد.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19770" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19769">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کامنت جدید زیر پست بی بی  : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRKUnvs_mq/?comment_id=18097108343207051
ترجمه : بی‌بی، مردم ایران بسیار دلتنگ شما هستند. لطفاً به هر روشی که صلاح می‌دانید، این بار پس از وحیدی، کاری کنید که روحانیون تندرو نیز یکی‌یکی از این دنیا بروند و ریشه کن شوند . هدف قرار دادن زیرساخت‌ها و سربازان وظیفهٔ عادی، که خودشان نیز قربانی این حکومت هستند، فقط رنج و درد مردم ایران را بیشتر می‌کند.
ما شما را بسیار دوست داریم و از همه تلاش‌ها و زحمات شما صمیمانه سپاسگزاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19769" target="_blank">📅 23:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19768">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کامنت جدید زیر پست ترامپ : فقط همین کامنت رو لایک کنید و کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DbRJwPPBPaP/?comment_id=18108319289002859
ترجمه : لطفاً به‌جای هدف قرار دادن زیرساخت‌ها، که تخریب آن‌ها تنها موجب رنج و سختی بیشتر مردم عادی می‌شود، و همچنین به‌جای سربازان وظیفه که بسیاری از آن‌ها خود قربانی این شرایط هستند، تمرکز خود را بر سران حکومت، به‌ویژه رهبران مذهبی تندرو، قرار دهید.
از تلاش‌های خستگی‌ناپذیر و شبانه‌روزی شما صمیمانه سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19768" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19767">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9edqBxTplmHTe6gVVz7mfxsqGYYWUgOp0VuVbDqPfzn8fIllPCZENtJBkunV5gTgCmXC9mfedczHJEtjbwT4M0v8StmJtjrNFqzqWQDA9yA4gfd2Hk4N_-Hts3yUf8tqxQh_8Y2Ouckslo5nC-7ssp2F13ddKiTsYQN2JX7wAl9n0jZoBzhBUYwto56RCJMYEO5qeC0fs_IrT42mK7iIXeZx0LmfJYbr2X-A3yi_AbIdX1iemIH20_MlqMlhXtWLwVPJ1FrIwW2eWel0rlvSAjxG0OJtwMSNoTlhbYbYZm6W1T8Y2UFOEshp32XkrfN9aUDKAsva2zao3PScIJgew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : الان دیگه نفتکش ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19766">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QctVMC2ol4ZetcXH0wqNcHYWSJsVXlQh46x5Y4y__MHeo1khyTvdAUuziMSSz2S7JIBbXREJNLesabIQhZRD6NJ0shC1cPTT3A6itfbV4RAW_sR1SGXbkCJ6FoLcetpCdYljcFVz0GXLVILLAHhHESFLtFwFs6BPdX0PlNh1OwsKgeNTsucWjkvP5JsAxudnvK38hvCuhqggk5WMC6g9NUij8NEoQjG7vYJRpwr8VGDQ5KNhgtiXwZ8FGuETAtSyMdZERAcAICTKGowRwy1uXOVG4iXvF8BdBDpo36zKQE1fzbVfpvRViQXPokHCKHTfS2VFOwoiW1pgGMAKW8Yt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حمله هوایی به جزیره خارک
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19766" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19765">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced9d7006c.mp4?token=mf-vZUYL4pR4c6tmOtJmFQ-JCCHkQkQFZ-67mMA8GKyzEt5GoJd6n_zFswjvoOTfg6VaKvdA3U_4LfNANdbByMyiZPlVp0spcpy8zw6XEqQUbXNon_D4atFw2i-XgJXAVkQR63wGEdqhKFE6-5sBDh9PT-_Bth1m0nz7VWy4LDtTiMtg4KpECpzzIWLoij_plLWYCvvMdekttImfagHyMf7nsYBvIpZ6W0zqigs2ZEH2xi_khd95dPzIL1V5ffzJiXARxGZIV_Jv11WR7rctqD1ac6O_c9DSr7ObLmDhm2PNZspOMLx4r0CDpmtpUEGlRyZ0gLd8EvA5x-_SbLKsDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced9d7006c.mp4?token=mf-vZUYL4pR4c6tmOtJmFQ-JCCHkQkQFZ-67mMA8GKyzEt5GoJd6n_zFswjvoOTfg6VaKvdA3U_4LfNANdbByMyiZPlVp0spcpy8zw6XEqQUbXNon_D4atFw2i-XgJXAVkQR63wGEdqhKFE6-5sBDh9PT-_Bth1m0nz7VWy4LDtTiMtg4KpECpzzIWLoij_plLWYCvvMdekttImfagHyMf7nsYBvIpZ6W0zqigs2ZEH2xi_khd95dPzIL1V5ffzJiXARxGZIV_Jv11WR7rctqD1ac6O_c9DSr7ObLmDhm2PNZspOMLx4r0CDpmtpUEGlRyZ0gLd8EvA5x-_SbLKsDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏واکنش من به تحلیل‌های احساسی مردم:
💥
«ترامپ از رژیم ترسیده.»
‏
💥
«ترامپ با رژیم ساخته.»
‏
💥
«مهماتشون تموم شده.»
‏
💥
«ترامپ ارباب نتانیاهوعه.»
‏
💥
«همه‌چی از قبل هماهنگ شده بود.»
‏
💥
«اینم یه جنگ نمایشی بود.»
‏
💥
«فلانی با یه مقام امنیتی در ارتباطه.»
‏
💥
«چین آخرش همه رو غافلگیر می‌کنه.»….
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19765" target="_blank">📅 23:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19764">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f4990448.mp4?token=JDw2PVDiXRnzAGCVYBvqgSOGBq_AQvORi9JiUmwSAXEUPRRFSdxy7i7MmKvpiwx-U1Z1FB5jGcrWs3EV3p42VKjlSC0pvaCX75Gmgsr0enJV5HINPNV6CfEmrUwNtt7tpS8xd0SmcX1ADlI5e_Ef0rovKfWazYtYN8GNe0gR9z7zULy29terojrpyOtq2ZsDV74F3HvLLQt03VkCGc86Jtb9kBpETotd9qxTDnTDI5Sozt6ZPfE7IvY6x5A2OVfpnOmvoud6toGt0J_WFzYQENAnBmn45YQiWjCjqLFI-kQ4ZJM8OxEbEGe74ZnK1bRlDP0k6OhRRczTz9Qg1aDx5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f4990448.mp4?token=JDw2PVDiXRnzAGCVYBvqgSOGBq_AQvORi9JiUmwSAXEUPRRFSdxy7i7MmKvpiwx-U1Z1FB5jGcrWs3EV3p42VKjlSC0pvaCX75Gmgsr0enJV5HINPNV6CfEmrUwNtt7tpS8xd0SmcX1ADlI5e_Ef0rovKfWazYtYN8GNe0gR9z7zULy29terojrpyOtq2ZsDV74F3HvLLQt03VkCGc86Jtb9kBpETotd9qxTDnTDI5Sozt6ZPfE7IvY6x5A2OVfpnOmvoud6toGt0J_WFzYQENAnBmn45YQiWjCjqLFI-kQ4ZJM8OxEbEGe74ZnK1bRlDP0k6OhRRczTz9Qg1aDx5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار: آقای رئیس جمهور، امشب کجا را بزنیم؟
ترامپ:
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19764" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19763">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYcl3jBhUh0z3UD3LN4D_BX2-MRKhIb51jMPitlUBEfzCPwYV32mJFRTaHKNOATX_Z0cBb9dfeBF1tXXhcPsUjnlRgEZcKphJFjk-j0xoq4Puxv2czUQTaKFmzw5t56KJmZQW7onfUALZLbuErApUHz1QQBjMMRwOPo97p9x7D6g6hG7ZwWeaW3mhkbWbmZzt9M0Ua0BcEb2qaXdiJeB9EmUWzoLhR7VUBvSw_Ohd-PY06RBklDr4_L5AmLJ2f4v3po3qfjmcT-L2FHs8jcVvswUUmZwaf06KwWDzo2qVGH8trNsoDBY3nM-6n65ILvlpxaAJe2PLORTS7tRRdTw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آگاه : اوکراین را ادب میکنیم
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19763" target="_blank">📅 22:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19761">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkqAgNT9-L8KE94nSl3vsjoMWG-10QWgnoKLIluPl4xBb5SLuCCnORvlKQwTjIUfnzvMblySOL9u68gFiEPetD2PyqJ2SjBr3NVuNiZN4A9rM6djYdnc2UvnGaxfn_aI2H4kYxU0edzI911mYdugQwDgsUqVBP1juuv5yajt1n0DFGMS5qv8T3rHIvLu3pjdYvtdiewkd7uOKMKq3jWbi3frD4rBfDz_kPzPTUZbbDSJFfH9ecdhh21ggDBme_iiTAK4ZY4qdDWBwvQVXRyUge77cmc-53ZR1ifrq5sf3FZuoo2GudIQyV6JysyrHEfCJSi2AFZ9z4Nq_o-lj29AzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فضای به شدت شلوغ و عرفانی حاکم بر منطقه و یک دسته حوری جدید که از اسرائیل به سمت خلیج فارس میآیند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19761" target="_blank">📅 22:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19760">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی: تو عراق به من میگن عباس قهرمان
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19760" target="_blank">📅 21:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19759">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مجتبی خامنه ای: ایران حفظ تمامیّت ارضی لبنان و رفع کامل و بدون قید و شرط تجاوز اسرائیل را به‌عنوان شرط اوّل تفاهم‌نامه‌ی پایان جنگ تحمیلی با امریکا قرار داده
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19759" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19758">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19758" target="_blank">📅 20:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19757">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سی‌بی‌اس
:
بسیاری از آمریکایی ها احساس می کنند که جنگ با ایران به خوبی پیش میره
این احساسات به طول جنگ، ارتباط در مورد آن و تأثیر آن بر اقتصاد مربوط میشه
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19757" target="_blank">📅 20:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19756">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">العربیه:ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است،
هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19756" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19755">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش CNN: عمان پیشنهاد ایجاد یک ائتلاف منطقه‌ای برای ارائه خدمات در تنگه هرمز را داده است، مشابه مدلی که در تنگه مالاکا استفاده می‌شود.
پیشنهاد عمان شامل یک مکانیسم پرداخت داوطلبانه برای خدمات ارائه شده در تنگه هرمز است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19755" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19754">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سی‌بی‌اس:حملات آمریکا به ایران به دلیل سفر مقامات عمانی به تهران در روز جمعه برای انجام مذاکرات، متوقف شد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19754" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19753">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در ابتکاری خوب برای کاستن حاشیه‌ها، شاهزاده رضا پهلوی تمام فالوینگهای اینستاگرام خود را آنفالو و فقط خانواده و پیجهای رسمی را نگهداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19753" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19752">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سفیر ایالات متحده در سازمان ملل متحد به شبکه ان‌بی‌سی گفت: مذاکرات با ایران در سطوح مختلف ادامه دارد، با وجود اختلافات موجود در داخل رژیم ایران
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19752" target="_blank">📅 19:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19751">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=pyD5pMejJXYZ7TMxHS0Cr3NvshFga78vevC8o5yAihPkTYopVJk-yBnD5S7kscwriqPDJIxI5rR4ha37tqt5hkk9JBGRJNzwIDE1_RnfYHetmPPTHW-uGKk8jznhZxqgJZ-nC_mn7BxUHPV_ntGy6FcEZAlU4Hi-hnAW7Tfo20GdEPhUvhBSKhSbDyvq8TZBaMwyVF0TMOqyPclI0jN2dt3D9PlGJV8QfhdCGkhHWUFaeX2SJmzLaDoOSe2rir-aqqTolbnJnReKdZnRUrD44kkREUQl8VWFS5mGRnBMXa7R8bFfGLniLT6S9NxzxvS-R7-BvcAhSiFTrQoh4CMJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90613bbec.mp4?token=pyD5pMejJXYZ7TMxHS0Cr3NvshFga78vevC8o5yAihPkTYopVJk-yBnD5S7kscwriqPDJIxI5rR4ha37tqt5hkk9JBGRJNzwIDE1_RnfYHetmPPTHW-uGKk8jznhZxqgJZ-nC_mn7BxUHPV_ntGy6FcEZAlU4Hi-hnAW7Tfo20GdEPhUvhBSKhSbDyvq8TZBaMwyVF0TMOqyPclI0jN2dt3D9PlGJV8QfhdCGkhHWUFaeX2SJmzLaDoOSe2rir-aqqTolbnJnReKdZnRUrD44kkREUQl8VWFS5mGRnBMXa7R8bFfGLniLT6S9NxzxvS-R7-BvcAhSiFTrQoh4CMJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل:
اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین قاتل، اشتباه وحشتناکی مرتکب خواهد شد.
زیرا پاسخ ما، پاسخ اسرائیل بسیار بسیار قاطع خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19751" target="_blank">📅 18:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19750">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مجری فاکس: در مورد هرگونه اطلاعات جدیدی که ممکن است در مورد برنامه هسته‌ای داشته باشید و قرار است به ترامپ ارائه دهید، چه می‌توانید به ما بگویید؟
نتانیاهو: قرار نیست من اطلاعات جدیدی ارائه دهم؛ فکر می‌کنم خوب است که فرصتی برای نشستن با دوست خوبمان، رئیس جمهور ترامپ، و شنیدن آنچه در ذهن دارد، داشته باشیم، زیرا فکر می‌کنم از بسیاری جهات، این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19750" target="_blank">📅 18:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19749">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بنیامین نتانیاهو در گفت‌وگو با فاکس نیوز: برنامه هسته‌ای ایران باید به هر شکل ممکن پایان یابد؛ چه از طریق توافق و چه بدون توافق.
این جنگ زمانی پایان خواهد یافت که یا نظام ایران سقوط کند، یا آن‌قدر تضعیف شود که به این نتیجه برسد که باید برنامه هسته‌ای خود را متوقف کند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19749" target="_blank">📅 18:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19748">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مطابق گزارش رویترز، به نقل از یک مقام ارشد ایرانی، در تهران، میزان تردید و بدبینی نسبت به تصمیم ایالات متحده برای توقف عملیات نظامی، بیشتر از خوش‌بینی است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19748" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19747">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزارت دفاع اسرائیل اعلام کرده سامانه لیزری پرتو آهنین پس از آزمایش‌های گسترده، در مرحله تحویل/ادغام عملیاتی با ارتش قرار گرفته و به‌عنوان لایه مکمل در کنار گنبد آهنین استفاده می‌شود. این سامانه توانسته در آزمایش‌ها راکت، خمپاره و پهپاد را رهگیری کند و هدفش کاهش شدید هزینه دفاع در برابر تهدیدات ارزان‌قیمت است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19747" target="_blank">📅 17:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19746">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۴ اسرائیل:داماد خامنه‌ای سکوت خود را در مورد انزوای مجتبی شکست
رئیس سابق مجلس ایران فاش کرد که مجتبی خامنه‌ای «به دلایل خاصی» تمام تماس‌های خود را قطع کرده و در بحبوحه سوالات مربوط به غیبت طولانی مدت رهبر جدید از انظار عمومی، تنها با احتیاط گفته است «امیدوارم سالم باشد».
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19746" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19745">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19745" target="_blank">📅 17:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19744">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک منبع بلندپایه به الحدث:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه
«آن را به تعلیق درآورده است»
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19744" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19743">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الکساندر دوبریندت، وزیر کشور آلمان، در بیانیه‌ای در محل حمله به رژه همجنسگرایان برلین گفت: «همه چیز نشان می‌دهد که ما با یک حمله تروریستی اسلامی روبرو هستیم.» این وزیر افزود که مهاجم مظنون به استفاده از قمه است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19743" target="_blank">📅 16:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19742">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شبکه سی‌بی‌اس نیوز به نقل از منابع: مذاکرات بین سلطنت عمان و ایران درباره بازگشایی تنگه هرمز، پیشرفت‌هایی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19742" target="_blank">📅 16:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19741">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19741" target="_blank">📅 16:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19740">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صدا و سیما
:
جمهوری اسلامی بارها هشدار داده است که هرگونه عواقبی که ناشی از انحراف کشتی‌ها از مسیر اعلام‌شده توسط ایران باشد، مسئولیت آن بر عهده‌ی آن کشتی‌ها خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19740" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19739">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری وابسته به رژیم :
سخن از هدف قرار گرفتن سه فروند کشتی تجاری و نفت‌کش در میان است؛ دو فروند در باب‌المندب و یک فروند در تنگه هرمز. ایران در حال بازی با اعصاب ترامپ است و احتمال دارد قیمت نفت در زمان بازگشایی بازار به ۱۱۰ دلار برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19739" target="_blank">📅 15:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک منبع آگاه وابسته به رژیم : کمی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری اسلامی خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19738" target="_blank">📅 15:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19737" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ادعای منبعی عربی به نقل از مقامات آمریکایی و اسرائیلی: نشست ترامپ و نتانیاهو، زمان عملیات مشترک علیه ایران را تعیین خواهد کرد.
مرحله اول این عملیات، بر تاسیسات هسته‌ای متمرکز نخواهد بود و تا 10 روز ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19736" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کریم خان دادستان کل دیوان کیفری بین‌المللی ، که حکم بازداشت نتانیاهو، نخست‌وزیر اسرائیل، و گالانت، وزیر دفاع سابق، را صادر کرده بود، پس از اتهامات سوء رفتار جنسی از سوی یکی از کارمندان سابق، توسط کشورهای عضو با رأی قاطع برکنار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19735" target="_blank">📅 14:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سوأل شما : ترامپ رئیس قوه مجریه است، اما همه چیز را نمی‌تواند شخصاً جابه‌جا کند. معاون رئیس‌جمهور یک جایگاه انتخابی در قانون‌اساسی است که برای تغییر ونس ، پای کنگره و مقررات صریح قانون اساسی وسط می‌آید ؛ تنها راه‌های عملی برای رفتن او، استعفا، مرگ، یا در موارد خاص فرآیندهای قانون اساسی و رأی کنگره است
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19734" target="_blank">📅 14:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نیکزاد، نایب‌رئیس مجلس :اقدام نابخردانه دولت اوکراین درهدف قراردادن کشتی ما بی‌جواب نمی‌مونه
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19733" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سازمان دریایی بریتانیا یک گزارش جدید در جنوب دریای سرخ دریافت کرده است.
گزارش شده که یک نفتکش در نزدیکی خود، برخورد/اصابت موج آب ناشی از یک پرتابه ناشناس را مشاهده کرده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19732" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال ۱۴ : منابع تأیید شده گزارش می‌دهند که جی دی ونس شایعات و نگرانی‌ها در مورد ذخایر مهمات ایالات متحده را دامن زده است. در صورتی که اگر مشکلی بود وزیر جنگ باید این را عنوان کند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19731" target="_blank">📅 14:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گرندپری فرمول یک بحرین به کشور مالزی منتقل شد : دلیل جنگ ایران و آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19730" target="_blank">📅 14:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شورای اتحادیه اروپا پنج قاضی دادگاه‌های انقلاب و یک هکر ایرانی را که می‌گوید در «نقض جدی حقوق بشر» دست داشته‌‌اند در فهرست تحریم‌های خود قرار داد.
«مصطفی نریمانی»، رییس شعبه سوم دادگاه انقلاب کرج؛ «ابوالفضل عامری شهرابی»، قاضی شعبه ۱۱۹۱دادگاه تجدیدنظر کیفری تهران و معاون پیشین دادستان اراک، «مهدی راسخی»، قاضی شعبه سوم دادگاه انقلاب رشت، «محمدرضا عموزاد»، رییس شعبه ۲۸ دادگاه انقلاب تهران و قاضی مشاور شعبه ۱۵، «محمدرضا توکلی»، رییس شعبه اول دادگاه انقلاب اصفهان پنج نامی هستند که به‌دلیل محاکمه اقلیت‌های مذهبی و مخالفان سیاسی توسط شورای اتحادیه اروپا در فهرست تحریم‌ها قرار گرفته‌اند.
اتحادیه اروپا همچنین «نیما صالحی» را به دلیل همکاری گروه هکری «آشیانه» با پلیس فتا و سپاه پاسداران و نقش این گروه در حملات سایبری علیه مخالفان داخلی و نهادهای خارجی و کمک به سرکوب جریان آزاد اطلاعات، تحریم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19729" target="_blank">📅 14:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">العربیه: منابع آگاه گزارش دادند که واشنگتن و تهران پاسخ‌های خود را به پیشنهاد پاکستان و قطر برای از سرگیری مذاکرات ارائه کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19728" target="_blank">📅 14:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❤🦁💚</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr9MnCpwGJS0GamZ4QXeb1h6bKh-MjPtjKjAPh0msD0L_JGu2dJuB2EVtFTLeiGJ-TvRUl-91mCW02VyvrDXueMzTWWf7H7tm0xITEX2JI9O3mkDqLPTW8_rcrdHHPg_dW4Cgszxz0YPThIRQlWLyoaC_UerBCZWNX-xDHJXVvk4819oJIHUavav14JYorCyoId0rA7A5h9BWTQSp1zDw2E3FVIJDYcebI8PpjBBOQcfPsXA_V4CO8S2sxlF9bXJcjkpUMGrtHshEnH706RhKLSYxi41bzOlPX_NLm5FbiPUX04Ih-ZBq-AYcauuLE41t-5RAsEOiWvcTEqg0tgAAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار داداش دیشب سنگ قبر رفیقم طاها نادری رو جاوید نام شهرضا رو شکستن حروم زاده ها دارن سنگ قبر جاوید نام ها رو تو این شهر میشکنن حروم لقمه ها از قبر هم هراس دارن ولی روز انتقام نزدیگه</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19727" target="_blank">📅 14:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کاخ سفید: در مورد ایران هنوز همه گزینه‌ها روی میز است
در پی گزارش رسانه‌های آمریکا که دونالد ترامپ فعلا از تشدید عملیات نظامی علیه ایران منصرف شده است، کاخ سفید تاکید کرد که همچنان «همه گزینه‌ها» در مورد ایران روی میز است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19726" target="_blank">📅 14:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rekU17i8ntB93lsluCZ1xyngz3k_FZeZLhrZWdqwKRyjyMGxZf19PKNFNh1OnIVPxpAlNya2GikcQc_4EWENkxMB_vjOsdSsNQ-4OGxCv62G2FmB0fXR9DJYH_jap7uubBUSP3ts_hWHXDMSVV7LU6PjoEoBktp5f3Wn02Gv4744GaPeSwNhui8FUOAOHlyqpnWqePQrjx8brER6lOFWXGn93kd5dL13y6GXeBfmtptbtqV7R-S8Stc_yRoMqcZDHmIHmgNAcSakOlCQ3mVfLyecYVPDk1OXcss1h4VNMp6_GWa6y22PUFd8TjCJQhmRnk3A0g9yr5D_ocQvj3QYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم. @WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19725" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو:این هفته با ترامپ ملاقات خواهم کرد تا درباره تمام موضوعات، از جمله ایران، گفتگو کنیم.
@WarRoom
🚨
🚨
🚨
🚨
یاشار : آلبوم جدید داره میبره رو کنه
😁</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19724" target="_blank">📅 13:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abDFO2ZYGx3_HNeWylgPomcd1WWi70C1f3La7JmTlkbf4Ng2rZJG_Xvx2seP-TsT9I0Jaek6W1AM8AXTJc2GoZQEDmReeY0YvC1Bmpv1pPyDHwCZaPDCoQsnMuKdA3DHfP2eaDX8CzJqDIazdncIRwEQUj8IzvTHk_vwiT358_KjJGLVO8jkSIiDsPMXkG_TE1l4ndKfmwmp6LGB8ua51R0-XiNzvamVBm6tSRVCz2mOcD6Wl_vfuQgCx_RY1eqnSNngMLNG_eGDg5M5sYAolk2US6icV1rm7q-sLlplW6dqEc0nrPvSpSZopfbx5GKd3mKCIhE3gfEsb1bcCd8DPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن شرتی و غول برره که به مرده ها هم  رحم نمی‌کنند و پریدن توی‌ کادر زیر تابوت اکبر عبدی و بلند میگویند الله اکبر.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19723" target="_blank">📅 13:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4GP9hzgxyCvdM0zyCsbP1FJKBLnce3J4oeP0BxIxdEUKt0Go2MZYz3T65ITwzCDpSduM0ALgdHbySwNzmkJIIP9gMsjKlq8jB8qFzEBsc87Iwpchqfkoslk26Um8ENf479Ez3rLdR9upu1-T2XtylriCgA6hi91RIJGthb87kuPZ4QYNyql3lZgPypow90hw74TiJ9Q2ZifDegbE24Y7VPjPYyT90-FMqC0ZnlHIS-EgJWEGBctVwiYdPMcWZkrFBLE2CuskzytjKfmikZJgzs7tnR_VHYTZCCZXVfocUeUh2zTJivPmy0WsMtm1oF5Loci6TBULTkDwIUL5NoB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از وقوع حادثه‌ای در جنوب دریای سرخ دریافت کرده است. به UKMTO گزارش شده است که یک نفتکش شاهد پرتاب یک پرتابه ناشناخته در نزدیکی کشتی بوده است. گزارش‌ها تأیید می‌کنند که کشتی و خدمه در سلامت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19722" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19721">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هم اکنون هدف قرار گرفتن یک کشتی دیگر در دریای سرخ
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19721" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی ارتش: با توقف حملات آمریکا، عملیات تلفافی‌جویانه را متوقف کردیم
ما برای تمام سناریو ها آمده ایم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19720" target="_blank">📅 12:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویدیو انیمیشن بسیار زیبای تحلیل فرضیه حمله به کوه «کلنگ گزلا»زیر نویس فارسی هم زدم ، از دست ندید
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19719" target="_blank">📅 12:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات سابق و کارشناسان هسته ای گزارش داد، اگر دونالد ترامپ، رئیس جمهور آمریکا حملات آمریکا به ایران را گسترش دهد، واشنگتن می تواند چندین تاسیسات هسته ای باقی مانده را فراتر از کوه کلنگ هدف قرار دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19718" target="_blank">📅 11:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تلگراف: وزیر دفاع انگلستان قصد دارد روابط با دولت ترامپ را بازسازی کرده و همکاری‌های امنیتی را تقویت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19717" target="_blank">📅 11:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یِوگن کورنیتشوک، سفیر اوکراین در اسرائیل، در گفتگو با N12 به حمله به یک کشتی ایرانی در دریای خزر اشاره کرد: "کشتی که در دریای خزر مورد حمله قرار گرفت، قطعات مربوط به پهپادها و موشک‌هایی را حمل می‌کرد که در راه ایران بودند، نه کالاهای غیرنظامی، همانطور که ایران ادعا کرد. این اولین باری نیست که به اهداف نظامی این‌چنینی حمله می‌کنیم، و البته می‌توان انتظار داشت که دوباره به آن‌ها حمله کنیم. از نظر ما، این یک هدف نظامی مشروع است."
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19716" target="_blank">📅 11:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6d-00Lw4XDu_ZQjN79fNAJdydbjzSPZ3QPwnCtIJFCDYwAAmMEOJ8_N4-l4BlS16havnOH3sqCCXVs8kRb3FJZfwjuoahv9gabJHmqj6TGLa-iIzhtTR1DIFtFOoYcE0RrjddzPptqzmgyH7zKSZ_LoGAaYHQSAx2nUVRh9ajBvsSoylpqej0pzQsURU40YuR-YuSLfxyTSI0lXJQISv6-wwlccizopiECBBz3kk046JBp75Q2TiD4oy9pVLrVeVByiMS6qS53guzJGAKz7UH3Ht7gxn4f4DimqGnz9SfXiv0ViA4SbceFDaqfgcLtL2CUVdoHI1IFESfLJn3GJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون حداقل ۱۷ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M و سوخترسان در حال رفت و آمد به خاورمیانه هستند
@WarRoom
دیروز خبر فیکی مبنی بر پایان نقل و انتقالات پل هوایی آمریکا پخش شده بود !</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19715" target="_blank">📅 10:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امروز چهارم مرداد؛ سالروز درگذشت رضاشاه کبیر پدر ایران نوین
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19714" target="_blank">📅 09:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدا و سیما :
‏ سناریوهای احتمالیِ آمریکا در مقابل ایران
سخنگوی ارتش
: یکی از راهبردهای آمریکا خروج از جنگ است البته اگر اسرائیلی‌ها اجازه بدهند.
سناریوی دوم
اینکه تحت فشار اسرائیلی ها عملیات هوایی گسترده انجام دهد. یا انجام عملیات زمینی.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19713" target="_blank">📅 09:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به گزارش سی‌بی‌اس نیوز، مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت‌های مثبتی داشته، هرچند رسیدن به توافق نهایی نیازمند زمان است. همزمان با سفر روز جمعه مقامات عمانی به تهران، آمریکا نیز برای جلوگیری از اختلال در این روند حساس دیپلماتیک، بمباران‌های ۱۳ روزه خود را عمداً متوقف کرد؛ موضوعی که کاخ سفید و سنتکام حاضر به اظهارنظر درباره آن نشدند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19712" target="_blank">📅 09:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شبکه کان اعلام کرد که اسرائیل امروز تمدید وضعیت اضطراری را تا ۱۱ آگوست (۲۰ مرداد) به دلیل اوضاع در ایران و لبنان تصویب کرد. همچنین در مورد سفر نتانیاهو به آمریکا گفت: نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه باترامپ درباره موضوع ایران گفتگو خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19711" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شان پارنل، سخنگوی ارشد پنتاگون در بیانیه‌ای به سی‌ان‌ان گفت: «ارتش آمریکا قدرتمندترین ارتش جهان است و هر آنچه را که برای اجرای عملیات در زمان و مکان مورد نظر رئیس‌جمهور نیاز دارد، در اختیار دارد.»
«ما عملیات‌های موفقیت‌آمیز متعددی را در سراسر فرماندهی‌های رزمی اجرا کرده‌ایم، در حالی که اطمینان حاصل می‌کنیم ارتش ایالات متحده دارای زرادخانه‌ای عمیق از توانمندی‌ها برای محافظت از مردم و منافع ما است.»
@WarRoom
part5 final cnn</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19710" target="_blank">📅 09:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بر اساس گفته چندین منبع‌ به سی ان ان، افراد کمی در حلقه نزدیکان ترامپ یا در داخل پنتاگون بر این باور بودند که گزینه‌های رئیس‌جمهور برای تشدید تنش، نتایج مورد نظر او را به همراه خواهد داشت.
پیش از آغاز جنگ، کین و سایر رهبران نظامی به ترامپ هشدار داده بودند که یک کمپین نظامی طولانی‌مدت می‌تواند بر ذخایر تسلیحاتی آمریکا تأثیر بگذارد(استراحت بین حملات لازمه برای پر کردن ذخایر)
@WarRoom
part4</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19709" target="_blank">📅 09:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به گفته یک منبع آگاه، تا بعدازظهر جمعه، دولت ترامپ هنوز در حال بررسی این موضوع بود که تشدید احتمالی تنش چگونه خواهد بود. این منبع گفت که کشورهای حاشیه خلیج فارس در گفتگوهای اخیر خود با مقامات دولت خواستار خویشتن‌داری شده‌اند، اما اذعان کرده‌اند که ایالات متحده توانمندی‌های منحصربه‌فردی دارد که در صورت تمایل می‌تواند از آن‌ها برای تشدید درگیری استفاده کند.
@WarRoom
part3</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19708" target="_blank">📅 09:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">استیون چونگ، مدیر ارتباطات کاخ سفید، در بیانیه‌ای گفت:
«با توجه به ترکیب تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزات مکرر آن‌ها، عاقلانه است که ایران برای رسیدن به یک توافق مذاکره‌شده تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
@WarRoom
part2</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19707" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک منبع آگاه و یک مقام آمریکایی به سی‌ان‌ان گفتند که جی‌دی ونس، معاون رئیس‌جمهور، و ژنرال دن کین، رئیس ستاد مشترک ارتش، هر دو در جریان نشست روز جمعه در کاخ سفید و در حالی که رئیس‌جمهور دونالد ترامپ در حال بررسی این احتمال بود، نسبت به تشدید جنگ در ایران ابراز نگرانی کردند.
@WarRoom
part1</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19706" target="_blank">📅 09:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ به LCI : توقف موقت حملات به معنای عقب‌نشینی نیست, برای انجام حمله گسترده علیه ایران آمادگی کامل داریم!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19705" target="_blank">📅 09:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارت امور خارجه: گفتگوهای ایران و عمان درباره تنگه هرمز که در تهران برگزار شد، سازنده و مفید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19704" target="_blank">📅 08:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=lPLWA2OqvOWEUADjNzJPiRh-vzc2lWRQYXbCubKzeeGOs8JTuegiGn9TJxLLHXFuaXGMbgbhnruxrlElFzLJOImygcG5uUt3PUxzwUpB4jUxZWEgblBB6X2nuSAYq6P7wp1Oo89yCTanGfXSkWqCK5VMSskPJ5fsN6UrvA9Hh130rM5b3q04MBeZCWnCbMfKaYkk7Wq64Urm9poIpSZLIAPPh91LNi1Io6JGKSYZdKio8gshytk9vqaJdjJWRd-q-lCEK82rdqtkpKjjlzbbzGMSG86UjpFTJm2xZfvZwIgYs7A12ApqEpnANZIRLGDv5fpL7joG71HN5PBGUSeIcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2743288b5.mp4?token=lPLWA2OqvOWEUADjNzJPiRh-vzc2lWRQYXbCubKzeeGOs8JTuegiGn9TJxLLHXFuaXGMbgbhnruxrlElFzLJOImygcG5uUt3PUxzwUpB4jUxZWEgblBB6X2nuSAYq6P7wp1Oo89yCTanGfXSkWqCK5VMSskPJ5fsN6UrvA9Hh130rM5b3q04MBeZCWnCbMfKaYkk7Wq64Urm9poIpSZLIAPPh91LNi1Io6JGKSYZdKio8gshytk9vqaJdjJWRd-q-lCEK82rdqtkpKjjlzbbzGMSG86UjpFTJm2xZfvZwIgYs7A12ApqEpnANZIRLGDv5fpL7joG71HN5PBGUSeIcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصره دریایی ایالات متحده علیه ایران همچنان به طور کامل برقرار است. از ۲۵ ژوئیه، سنتکام ۱۲ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده، ۲ کشتی را که رعایت نکرده بودند، غیرفعال کرده و ۲ کشتی دیگر را برای اطمینان از رعایت کامل محاصره، سوار بر آنها کرده است.
اوایل امروز، نیروهای آمریکایی عملیات تأیید ورود به کشتی M/T Charminar با پرچم کومور را در دریای عرب تکمیل کردند و این نفتکش اکنون به سفر خود ادامه می‌دهد.
نیروهای سنتکام، M/T Lavine با پرچم موزامبیک را در ۲۴ ژوئیه در خلیج عمان غیرفعال کردند، پس از آنکه خدمه چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران در حال حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/19703" target="_blank">📅 03:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک پهپاد در نزدیکی منزل ایتمار بن گویر، وزیر امنیت ملی اسرائیل، سقوط کرده است ، جزئیات در حال بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/19702" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دریای قزوین
😁</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/19701" target="_blank">📅 23:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزارت امور خارجه ایران:
ما محکوم می‌کنیم اقدام دولت اوکراین مبنی بر حمله به یک کشتی تجاری ایرانی در دریای قزوين«خزر»که امروز صبح رخ داد. این حمله منجر به انفجار کشتی و شهادت یکی از ملوانان و زخمی شدن ملوان دیگری شد.
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/19700" target="_blank">📅 23:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۴ : ترامپ دستور توقف تمام حملات به ایران را صادر کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/withyashar/19699" target="_blank">📅 22:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانال 12 : بنیامین نتانیاهو تصمیم دارد در نشستی در کاخ سفید، اطلاعاتی درباره پیشرفت برنامه هسته‌ای ایران را در اختیار ترامپ قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/19698" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زلنسکی : ما دریافتیم که ماهواره‌های روسی به تهران در حمله به مناطق خاورمیانه کمک می‌کنن
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/19697" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
