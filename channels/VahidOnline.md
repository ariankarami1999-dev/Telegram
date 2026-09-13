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
<img src="https://cdn1.telesco.pe/file/RMeRclCbMqv-rSLM8J0LSOO1hKKfof_pdAGWRLZ8nO_65aiIPRNzzgDC2djjahhELRDOmrP0SUT1e5t03_sjhLYpYgNElRpPDStF7SGMEEkJcXt3CNLxZkA_ghdqSukLQ02QudTmUT28IWdpeOnXlfgujX-pljTCiwyKpO8HLd6-lm_dUoHqhi_uNvSZuUuXBWXCr8TsUZUJOux6oalnGenzvB30Sl3Q4vKVs8VedTQT4P0ebH5l1PCvf8tfbMzgvB1nCIVdMUf30PTo1epQvAV_RrZniApsAAf6ea5iLOTyEpvv-dljQ5VRr1Y3TmPmFFio3TW-40eBRy97rHfKCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kgj3WpGSW5UXqnrHXFdoM8vujH-UlYzHDb3bYLP2mWRZLTgn3YwdMZsCZgHjs60_3kAYxp36U4fPUDJ-ZBIo8CXRoTPQysZlgx9R69MGwIiK2ficc_QDoU-wzXhSzJoNBGRagV0hMlLqKWVUe1cH5zn5Xookg-ukGGCG9K7bxx9bw2rUaRH_huuMAqRmycoQ2TWPHrz8SQY4WCyN7WF5ljH7hg22EV2r8_FVednk8cBavlXm0UuvBcJuOLbCQEfukavcKCsuctNVV6FEhoo-fyu9ZtB47qtsiqzLyJuCNcqDzcE6D9hSU5XVWcXzHHjEcnn1yj9E0C3lc1cLFQIrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nPZiAFrLOB7Qfzxf80LAUc0kSi8QlLJsOiDXKuf_Kqjrlr_ify4XLMjKzqgXCMDiMR29gb-yA-BAi3o65vKcyPPLWlG3DQxVIAGHGzRyuCI1zU-eB_aj794vDojAWZI1uNdsYciN4XR6adBMWEGziN8JaCXk3XhP1rHCWvEFUk0I242E2y12w-vfGF_WOJAr7eWaanHFNkZPUwGYsrYHIKsv6sWVXhrZ2aGzT-bCHkQ3zOHEbqX_Ucip34YHFr1ilKNeQQcmTh6xmkqPTU7kWfeGek_8stqS4OAfjWB7PpqBI-0Yn7jOTT8SluvAu8FSHi4DvkTJydhINvSjJyXtNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز شنبه، با صدور یک هشدار امنیتی، از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر داد.
این نهاد نظارتی دریایی اعلام کرد: «گزارشی مبنی بر وقوع یک حادثه در محدوده تنگه هرمز دریافت شده است. یک کشتی هنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.»
@
VahidOOnLine
امیر تیموری، فرماندار شهرستان قشم، اعلام کرد یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب‌دراز جزیره قشم هدف قرار گرفته است.
به گفته فرماندار قشم، در این حادثه یک نفر کشته و سه نفر دیگر مجروح شده‌اند.
تیموری عامل این حمله را آمریکا اعلام کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/VahidOnline/78352" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n6D7JRvrK_1DBzrydHYSX-RJAGtoAwG5b-7yFnMISzLty1Jjbl6pishSCl0Uj2MDnkrprKQpON2yQS4-laR4vrM2SIRGphbJWI7svgw37KDz-FD5TkDrsHQ5udVJectNgGs3HCoOPfuCwV1DL4ERUr2Iaq3SA-33i1F3viVVP6N7VAEjKQTFe5eXiumI60c_j7K5AswlDQKvxzkll80lZkgX8CryTh3smMn9g_HjNWauP5X2RM1x0uqXm6_0Ijeu1o9PrbKDwvfMq4WPy8Mm59yYkvPZ46qh_J4NDyY-IxzznSFpJr5xyWEcNwI5jgZ6cbcN70XUAcl7ppL97voU14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbff18bf8.mp4?token=n6D7JRvrK_1DBzrydHYSX-RJAGtoAwG5b-7yFnMISzLty1Jjbl6pishSCl0Uj2MDnkrprKQpON2yQS4-laR4vrM2SIRGphbJWI7svgw37KDz-FD5TkDrsHQ5udVJectNgGs3HCoOPfuCwV1DL4ERUr2Iaq3SA-33i1F3viVVP6N7VAEjKQTFe5eXiumI60c_j7K5AswlDQKvxzkll80lZkgX8CryTh3smMn9g_HjNWauP5X2RM1x0uqXm6_0Ijeu1o9PrbKDwvfMq4WPy8Mm59yYkvPZ46qh_J4NDyY-IxzznSFpJr5xyWEcNwI5jgZ6cbcN70XUAcl7ppL97voU14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تور اجبارى اتاق شلاق براى "عبرت" متهمان
یکی از شهروندان با ارسال ویدیویی که مخفیانه از اتاق اجرای احکام شلاق ثبت کرده، مشاهدات و تجربه مستقیم خود را با بنیاد عبدالرحمن برومند در میان گذاشته است؛ روایتی که به‌زودی در قالب یک شهادت‌نامه تفصیلی منتشر خواهد شد.
او درباره انگیزه خود از انتشار این ویدیو پس از چند سال می‌گوید:
«آنچه در جریان بازداشت و صدور این حکم بر من گذشت، در برابر حجم بی‌پایان ظلم و بی‌عدالتی شاید اهمیتی نداشته باشد؛ آنچه برای من اهمیت دارد، تاباندن نور بر گوشه‌ای از این سازوکار مخوف است تا همگان ببینند مردم ایران برای داشتن یک زندگی معمولی با چه مجازات‌های تحقیرآمیزی روبرو می‌شوند.»
@
IranRights
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/VahidOnline/78351" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=blMZ6AmQY_--1s9btZr1-Fe-ZT05pyKaOOrNkmvs_JeXSqfdR4tYYi7nR6-ukKeuvqGYWQZAuKcwWyz4DeX9dKfxLDHZRk0CU6H5jmFI3HX4d1ysYRMdPSOs9kSgbtG4-GUcJkk6k5rG_adfmvhdLK3SYA91vafskXewe3mwruDJSt3VmJaAQSPs0XRDY7L1NRK-Czdytq1uVgi3gAyU9fhbMbMnymBppeUpM_xfRYErpXJ_IFFqj2kBpMRa3yd74oSPW3M9kZ47vt7tsLK-Z2n5wjHriLuv3VDDdrKXp0lZlFr9Yw4-IlRN1RAbyqyi10zDP3iIKH0JjJMEz3MRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9047a957c6.mp4?token=blMZ6AmQY_--1s9btZr1-Fe-ZT05pyKaOOrNkmvs_JeXSqfdR4tYYi7nR6-ukKeuvqGYWQZAuKcwWyz4DeX9dKfxLDHZRk0CU6H5jmFI3HX4d1ysYRMdPSOs9kSgbtG4-GUcJkk6k5rG_adfmvhdLK3SYA91vafskXewe3mwruDJSt3VmJaAQSPs0XRDY7L1NRK-Czdytq1uVgi3gAyU9fhbMbMnymBppeUpM_xfRYErpXJ_IFFqj2kBpMRa3yd74oSPW3M9kZ47vt7tsLK-Z2n5wjHriLuv3VDDdrKXp0lZlFr9Yw4-IlRN1RAbyqyi10zDP3iIKH0JjJMEz3MRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهوری آمریکا در جریان دیدار با مایکل مارتین، نخست‌وزیر ایرلند، در دوبلین بر اعمال کنترل مقتدرانه و یک «محاصره دریایی باورنکردنی» بر تنگه هرمز تاکید کرد و گفت این اقدامات مانع از جهش شدید بهای جهانی نفت شده است.
دونالد ترامپ همچنین گفت نیروهای سنتکام به‌طور میانگین روزانه ۲۵ شناور و قایق را متوقف و توقیف می‌کنند؛ اقداماتی که به گفته او بیشتر آن‌ها در تاریکی شب و در جریان گشت‌های شبانه انجام می‌گیرد.
این در حالی است فرماندهی مرکزی آمریکا، سنتکام،
امروز
اعلام کرد طی ۶۰ روز گذشته و از زمان ازسرگیری «محاصره دیوار فولادی» ایران، مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78350" target="_blank">📅 23:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utz_4L9d_xGllKNk6xhgBX4uWdP9ogMGHRdp9bJInf1f2fxP5LLHmCFRxmvVEzxzNYvp15x0gWJPv_z0GHYA2gGEBsncM1W6SL2z5BklTcPWU2lLaKC3qVksLPi_3q_KD3x_TQ-8Wkuv13mCXrxJ_3sat0FALMuE6BdX1iB7VUtuH8ZS_JrIlcC4AYjH7tN_RoTTxu0CGcoy_FP5KrUkTxmEN0E3_7sGALi-3b5uHaLZivDwqIqJ53L6hYdczuS1KFHQW06YyvqyNWi_PpzrN5mi3l0rYn2CNGl83zodIYqqdUgQwIpSWjLzTkHJlVWhgVnBWfW2kq49hYGMEluj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی یک دستگاه اتوبوس حامل کارگران مجتمع مس سرچشمه، در صبح شنبه ۲۱ شهریور، یک کشته و ۳۸ مصدوم برجا گذاشت.
سید محسن مرتضوی، رییس مرکز فوریت‌های پزشکی رفسنجان، با تایید این خبر گفت ۳۸ مصدوم این حادثه برای دریافت خدمات درمانی به بیمارستان منتقل شده‌اند. به گفته او، بررسی‌های اولیه نشان می‌دهد ورود یک دستگاه ون به مسیر حرکت اتوبوس باعث انحراف و سپس واژگونی آن شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78349" target="_blank">📅 21:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOilBWpWDX1zAW8HdDDrcMU0bAMfbF2gGYtWtm_mULMplJIIfcrL8UBdtcvvTg6cVU3Ob0PQxKNFqFgCquoBaaZ0xVKBsB--Ra-93k1-CpksYgzEdd-f26E0s8mkSP9uigr2TlnNHJIdKDwKA3qOy-1mKN6EYryKB2d_UFe7IzB_JdrGLcudFzWW_nak-EV-mgnVDZAZqpceJKWFpQpFkJ13XgHc-x_bFRssEj6SXPEQS24sRkWrWxp7bGGwvM98ov42eO_8NQWR-wlJVpbHPNhdE7prWp1KxsqmEy9k92kixTVYgmAHTq5rba0CDKjnAzn_aOp3Bf2CKSZdlM47hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع امنیتی عراق به خبرگزاری فرانسه گفتند نیروهای امنیتی این کشور سکوهای پرتاب پهپاد را منطقه دورافتاده الطیب در استان میسان در جنوب عراق و در نزدیکی مرز با ایران کشف کرده‌اند.
همزمان خبرگزاری رویترز به نقل از دو منبع نظامی در عراق اعلام کرد این منطقه مرزی پس از کشف سکوهای پرتاب پهپاد بسته شده است.
کشف این سکوها پس از حمله به خط لوله نفت عربستان سعودی انجام شده است؛ حمله‌ای که ریاض و بغداد گفته‌اند از خاک عراق انجام شده است. بغداد روز شنبه گذرگاه‌های مرزی شلمچه و چذابه را نیز بسته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78348" target="_blank">📅 21:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgpWSjLkfz7qVSgZc_jfKsd1__Ji34Y6bo7bKnXMePBiYHmsx9TvjCjEVe9-KzPe_w-j9jD77MBraRA2ExBi9Z8B8mnVVQDMK9n-l5NLdTF_TTVINYnp0bVOeQNTxqI73ccbIk_Rr6MT4RnVBoelaNZUPVNrnkNPh1t3elEpK_WP7McOuR6mF2u5Go0nAmorASXTVy3__NSGmlnUzyeSjEJDZ4Wa3czyDXSNJt8ntf6uoPqWgavyrSLm_fS7afOfKrZuqud7_rNIRlLwetCo1r0KnKBWAsZyXI4rBkFqsAy0N65908hT3Q_9XZSIvYf7ljpoOU2YxxyFKLpv_FH1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، به نقل از یک منبع آگاه گزارش داد تفاهم نهایی جمهوری اسلامی و عمان درباره مسیرهای جدید کشتیرانی، به معنای بازگشایی تنگه هرمز نیست و باز شدن این تنگه به اجرای هفت شرط تهران از سوی آمریکا بستگی دارد.
این منبع گفت تهران و مسقط پس از گفت‌وگوهای فنی و دیپلماتیک، در اوایل شهریور درباره جزییات مسیرهای جدید ورود به خلیج فارس و خروج از آن به توافق نهایی رسیدند و قرار است این تفاهم به‌زودی با حضور وزیران خارجه کشورهای منطقه اعلام شود.
بر اساس این گزارش، تفاهم تنها میان جمهوری اسلامی و عمان است و کشورهای دیگر، از جمله عراق و کشورهای ساحلی خلیج فارس، برای اطلاع از جزییات مسیرها و ترتیبات تردد در نشست حضور خواهند داشت.
مهر نوشت مسیر ورود به خلیج فارس به‌طور کامل و بخشی از مسیر خروج از آن در آب‌های سرزمینی ایران قرار خواهد داشت و تردد در این مسیرها بر اساس ترتیبات تعیین‌شده از سوی جمهوری اسلامی انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/78347" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=jNF4mvde8BTHp6Vzw3BqwBiFlZ_8T9gDj5HIgpSxLx2mUb6sGw_-6I4_2beqteTDs1khIPTrfk5nHoT31R7ErR2Hp6viN_bKFe8ND7COzUHi86BTH5yHmNlhqpA47Mbx2ox9U8SfQlRY_H7cv-szT13nEzJioUVbzdmgb5tXZD_mTpfAyUTExw0d53Z04-kbfXUT8IkuzrpWpaEDA9EBIUXDn_QaaXWie_v2KD8IgYhylBioWizjEU3p2zzWRIfsmWUBKdV2Keyii7GIW7iJMk-GQ7z7OVTy91tZp1rl2C46CkSmgqDjuB64sTbvzUTdoLPiUMcSkwTs4XH7QAIMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c0eda53bf.mp4?token=jNF4mvde8BTHp6Vzw3BqwBiFlZ_8T9gDj5HIgpSxLx2mUb6sGw_-6I4_2beqteTDs1khIPTrfk5nHoT31R7ErR2Hp6viN_bKFe8ND7COzUHi86BTH5yHmNlhqpA47Mbx2ox9U8SfQlRY_H7cv-szT13nEzJioUVbzdmgb5tXZD_mTpfAyUTExw0d53Z04-kbfXUT8IkuzrpWpaEDA9EBIUXDn_QaaXWie_v2KD8IgYhylBioWizjEU3p2zzWRIfsmWUBKdV2Keyii7GIW7iJMk-GQ7z7OVTy91tZp1rl2C46CkSmgqDjuB64sTbvzUTdoLPiUMcSkwTs4XH7QAIMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، روز شنبه ۲۱ شهریور ماه گفت اطلاعات تهران نشان می‌دهد حمله موشکی آمریکا به لامرد از خاک یکی از کشورهای حاشیه جنوبی خلیج فارس نیز انجام شده است.
اسماعیل بقایی در گفتگو با رسانه‌های دولتی ایران گفت این موضوع نشان می‌دهد آمریکا «برخلاف همه قواعد و اصول حقوق بین‌الملل» از خاک و حاکمیت ملی کشورهای دیگر برای حمله به ایران استفاده کرده است.
او تاکید کرد ایرانیان این موضوع را پیگیری خواهند کرد.
بقایی همچنین گفت برخی کشورهای همسایه، برخلاف «اصل حسن همجواری»، اجازه داده‌اند از قلمرو آنها برای حمله به ایران و «ارتکاب جنایت جنگی علیه مردم» استفاده شود.
در نهم اسفند ۱۴۰۴، یک سالن ورزشی در لامرد فارس، مورد حمله دو موشک قرار گرفت که منجر به کشته شدن حداقل ۲۱ نفر، از جمله ۴ کودک، و زخمی شدن ۱۰۰ نفر شد. این حمله اندکی پس از حمله هوایی به مدرسه شجره طیبه میناب رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78346" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abkLNDnawJVPDu-XKn6H6EdRjgHBlDoIcwKb6Q9Ca8w7VO-V6pOtxlpQN_O3bBuAqnYHZtCPYWdwlIQv7T1rGsyq_2As3nVpfQRaXh7t3f8GpC8Er5cAQ25lVNOmIgjt458VVLgqsb7XTkhDE92j6eripHfNg_a3hNbZ5b5PQhrqv6KaZMzfsniKByWjhr8SS8DqMLJDPFEnSQXqHu7BxcHMTgPtTGzy4_A6-Wv4n3RAXeYvP5e5Eqs-ybawRq99rO8njetvw1_jE0sPCClyMPnauFt2zKS8Rav-FUa0YNaWebKkO9uUVYqnQKd4MxYbJVw2jvbaR1PQi1X9F15ZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت احتمالاً جمهوری اسلامی مسئول حمله هوایی به عربستان سعودی بوده که به تعطیلی خط لوله شرق به غرب انجامید.
او روز شنبه در دوبلین و در پاسخ به پرسش خبرنگاران درباره مسئولیت ایران گفت: «فکر می‌کنم مسئول‌اند، احتمالاً خودشان‌اند.»
ترامپ افزود با محمد بن سلمان، ولیعهد عربستان، گفت‌وگو کرده و او را «دوست خوب» خواند.
رئیس‌جمهوری آمریکا همچنین گفت حوثی‌های همسو با جمهوری اسلامی با دولت او تماس گرفته‌اند و اعلام کرده‌اند نمی‌خواهند آمریکا مستقیماً وارد درگیری شود.
او گفت: «آنها به‌مراتب ترجیح می‌دهند ما درگیر نباشیم و بیشتر شناورها را عبور می‌دهند. فقط یک کشور هست که از آن راضی نیستند و ترتیبش را می‌دهیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78345" target="_blank">📅 15:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=qVkgYOjkPxUqBcHSaLfMK-6UyIitv1lF3dq7CcbHRGjZHHtqo27a0lHfRlIJ-Q0jVLViALMLGtTw0szTH7ZwA9blTRmpA-5aq-mWaC8p6aL_cq9vMYOMSWISphZvtmLufFQqQFBl4RqsfwKMLEYDbY5HHXUH4G7zwDf5gagUSxDsN-5ojaIP-kPN_zNBJNODorjyGkPX-Y7uJQ0d74auWAy5tvtZqUYgQIUGbyT9QkSLD7nxrE8bx0edupUPDtACwidU2eft6pUsljR8sZgqdMVKOhQmLiv81qgCvB4jbNAq8NdCuGc5RcX3e-teDvluczkfdC5l74Tjixw9aLpqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/243b69b1d1.mp4?token=qVkgYOjkPxUqBcHSaLfMK-6UyIitv1lF3dq7CcbHRGjZHHtqo27a0lHfRlIJ-Q0jVLViALMLGtTw0szTH7ZwA9blTRmpA-5aq-mWaC8p6aL_cq9vMYOMSWISphZvtmLufFQqQFBl4RqsfwKMLEYDbY5HHXUH4G7zwDf5gagUSxDsN-5ojaIP-kPN_zNBJNODorjyGkPX-Y7uJQ0d74auWAy5tvtZqUYgQIUGbyT9QkSLD7nxrE8bx0edupUPDtACwidU2eft6pUsljR8sZgqdMVKOhQmLiv81qgCvB4jbNAq8NdCuGc5RcX3e-teDvluczkfdC5l74Tjixw9aLpqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشرشده در رسانه‌های اجتماعی نشان‌دهنده ازدحام در خروجی مرز بازرگان است.
برخی گزارش‌ها دلیل اختلال در تردد از این گذرگاه مرزی را «محدودیت‌های ظرفیت پذیرش در سمت ترکیه» عنوان می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78344" target="_blank">📅 15:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtWQS4ovRZPuY8K9b3sbdTM18pG32EUNbewvaAz5LhKFIZSXP2FRjSBlDnZb5KrKaoFQpbYIJ09PBj7mM3ZRpxXVMBsobNA-GGpm8MV5m9KjGz1OVFdNm8fZ_YN2V2SLH0E609Bcs6Q1UvvGlMuws8XjhOcFdwIuoJ7QmxMQ0b7NmwvfVqbQKzxUQiEShf-20_fUdpVZG3Cy7DOrxYieqQ-0B4z-2-bukqmPo-vPsJnUOkuJ6bSiu0ZXA65eCHtyZEE-yd8DufF0Kya_3XVDOXzBZAj7ovUnTT12PM5wXErKbRI2af9blAGi1_30C0RZlOcUNmE6KI7Ot1rzPC9n-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون استاندار خوزستان اعلام کرد مرز چذابه نیز همچون شلمچه از بامداد امروز با اعلام مقام‌های عراق تا اطلاع ثانوی بسته شد. بنابر اعلام ولی‌الله حیاتی، هیچ تردد کالا و مسافری از این مرزها انجام نمی‌شود.
ساعتی پیش رویترز بع نقل از دو منبع امنیتی نوشت عراق پس از تازه‌ترین حملات پهپادی صورت‌گرفته به عربستان سعودی، دستور بستن گذرگاه مرزی شلمچه بین عراق و ایران را به عنوان یک اقدام احتیاطی صادر کرد.
مرز چذابه در استان میسان عراق قرار دارد و دفتر نخست‌وزیری عراق بامداد شنبه فرمانده عملیاتش را برکنار کرد. این برکناری پس از آن انجام شد که تحقیقات تأیید کرد آخرین حملات پهپادی به عربستان سعودی از خاک عراق انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78343" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/euNj5LbUW8NS8vYnhlZPe0KsiB0NPOEmn4Gl65RqNnSGM1VZktKiTK7dtO-Beg_vOvv2N6CGLZSkKP_kwgYCWoE6gS2709Fntb0RnAj0Aedokbl6_qOJ7ty9j-aHjGPNpLoxsBqqAmatucKWqltDMC1-_gg-zEJaha81BjpmE71uKe9sCMlqQS3cZZwLiynZtw_6uhj-TVqsHmrzHMZZ4czHpLk2NJd1wo9Gt5bJMwotE9OxdKgnCkVuvaTfBSaejW60J6eq8xiviu59omLCVPHbmitlxH8C5EqLBoYLu4WYOA_ENANLedJHVKMgE-tsKmi70v9Fe4daQQScTQExlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NEY5lAuXcpwQ08GgxIs5_dLgxaHjK8Y3Nsc8vcoVEBC75s3DazGUkODzunWF9rsf7mdHI76un5fB336hQKTmdlSADh6Oz2UwMXm7uT3m-OhNjcvuz6ybZepU3RP3zfLX4Wzjj00Yr4xXNd_DLWJ21UQdFwRWwkLq2JZ7FugzZxDdwKDTy2o0ZJJRZ-MSZ3J4kGs-05Y2Nm0w0ArAxtJkui07KPbKoPDD8vYKkcewm3gROCCLwI3zz43BOFdOyhKas_BqZ6HC2ns5aTI77TGaQqeZAtRT7jW8YtZ2K06Z_WHNKZTF3NqXsDv5WWotfo6yEKcCXjIRm1iFCl485ujZwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درگیری میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح در منطقه «بخشان» سراوان، پس از بیش از هفت ساعت همچنان ادامه دارد. «شیوار نیوز» از حمله به نیروهای حکومتی از دو محور، شکسته‌شدن بخشی از حلقه محاصره و خروج شماری از افراد مسلح از محدوده درگیری خبر داده است.
این درگیری حدود ساعت چهار بامداد شنبه ۲۱ شهریور ۱۴۰۵ و پس از محاصره یک خانه مسکونی آغاز شد. شبکه اسناد حقوق بشر بلوچستان پیش‌تر از استقرار گسترده نیروهای نظامی و امنیتی و استفاده از سلاح‌های سبک و سنگین در این منطقه خبر داده بود.
براساس اطلاعات منتشر شده از سوی شیوار نیوز، نیروهای نظامی و امنیتی پس از آغاز درگیری، محدوده حضور افراد مسلح را محاصره و مسیرهای منتهی به محل را مسدود کردند. بااین‌حال، در ادامه افرادی از خارج محدوده محاصره، نیروهای حکومتی را از دو محور هدف قرار دادند.
@
VahidHeadline
قرارگاه قدس نیروی زمینی سپاه پاسداران اعلام کرد در جریان درگیری با افراد مسلح در شهرستان سراوان در استان سیستان و بلوچستان، سه نفر از نیروهای سپاه کشته شده‌اند.
بر اساس اطلاعیه این قرارگاه، این سه نفر با عنوان «پاسداران گمنام امام زمان» معرفی شده‌اند.
قرارگاه قدس همچنین اعلام کرد که تا پیش از ظهر روز شنبه، چهار نفر از افراد مسلح ناشناس نیز در جریان این درگیری کشته شده‌اند.
این اطلاعیه جزئیات بیشتری درباره هویت افراد مسلح، گروه یا سازمان وابسته به آنها، محل دقیق درگیری و چگونگی آغاز درگیری منتشر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78341" target="_blank">📅 15:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/StBL0RXYBedEv45qAm42h7txGsF_Gtw9SUzPrnhRVYNcd7hnhdfY_hAZyH9GrgDXugWWHzTpbXhqvWUv2DY_jZdivSGIOE1B6-Ob_H_H0_6UCozMf407WwgVFg6Rhwy-vUZ8W3wf1uVsSCZf4L1MLhn9tmV4BKwHbwWmZhK7b2RM0tgrltGZlxi9jDN-WL_uz-DLuXSIAIEZDNXoqa8IF9FH19L_3rG3D8QMKzDtBMnQOrNhER9PdbelUGuR7_Iq0tvi2qpfa6FVoV-UEDr2m9KQmJrbYUyDLHrOrLKd_ciooBxc5wskKzh7MKjRP5Xn0Qk6sXWINMo5yArpI3XuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سودا ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، که از ۹ فروردین در بازداشت به سر می‌برد، به اعدام محکوم شده است.
بر اساس این اطلاعات، شعبه سوم دادگاه انقلاب بندرعباس به ریاست قاضی خواجه‌حسنی، سودا ابراهیمی شمس‌آبادی را با اتهام‌هایی از جمله «توهین به رهبری»، «فعالیت رسانه‌ای و تبلیغی برخلاف امنیت ملی»، «اقدام اطلاعاتی و امنیتی به نفع دولت‌های متخاصم» و «عکسبرداری و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور» به اعدام محکوم کرده است.
دادگاه همچنین او را به دو تا پنج سال حبس، محرومیت از برخی خدمات دولتی و مصادره اموال محکوم کرده است.
حکم اعدام سودا ابراهیمی شمس‌آبادی روز اول شهریور به وکیل او ابلاغ شده است.
بر اساس اطلاعات رسیده، ابراهیمی شمس‌آبادی در جریان دوران بازداشت، به مدت ۲۰ روز در سلول انفرادی نگهداری شده و در دوران بازجویی تحت فشار شدید قرار داشته است. خانواده او در این مدت از محل نگهداری و وضعیتش اطلاعی نداشتند.
قاضی خواجه‌حسنی که این حکم را صادر کرده پیشتر در سال ۱۴۰۲ از سوی مقام‌های قوه قضاییه در زمینه‌هایی از جمله صدور بیشترین احکام و جدیت در انجام کار مورد تقدیر به عنوان قاضی نمونه قرار گرفته بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78340" target="_blank">📅 15:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DYYG_kHGBtlC-0vI5ppflqPvmRFdIsP7M1xNsK8eLFIPTeMtUwaj97qmRWEnRXUVBVuTCDwBVFTS9yZrpUtXA31fxy5M-sE-5b_COubb8yrQd8bNOuUzGEqHograEV2NbuKQ950rDxqrIvDJVjrjprpVCKHcOiMoPZti9G9HOtr3CTfUt4-jni701hJj193kPA9mCvtK5W5NUJn-BwHP94_S899jEPoLCF9xdBfCIIa8jcVtMjkHnKk7MDGCM1Pv3JIX0RKuQ9xyP_cYzphMTuDVFKnStAvNxFYeDbmBx8s9DRx0dLksqETT5AdBpioADu4ohhHNQDlaaFjtrn8cVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xp-nRumxB2Sl6Kxliz7m32gzZeVULXK_r86AEDzHNk5oRg2vog-ukuY1xkpu7nu16dvSswFUflHerv-YHJRUvwVcDpqBobLECY8--DngI1r4QRjKz0hMSQSwZlzP8QLkZaeikvcz6Yf7H82A4U5TREjIZ7Sw0KBMvUbNP183sIAfeO8mk2uOFqvc1S_rqPsVg5hPFMDAUTtgEK17xtUiMq45Gu1aU7MExP_ZZezy_mwyt6oLxhlsg1rYBmCSZFS0VI6ri6LEopyfuIC2eghDtHrCadbOqHXHPo24CnSWzbsww1HSCNTPIfjR5GPrUUlXQCeGgRnVa0sl3ZeQLJfU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aQ9TyFF2vTlaYoY5KMvPL7ecRWTRcQyR_uwQa23z7cb2Gzixknocv2Id7SbcowwXGxY5eLpooauS1fAi1V7Z-rJsa4V2GyrTq9C3qF22Suy5I7X-NA89eRWERKoJLD73g7ZimcfSA0Q9pQpCzv68_UYGV1Sp3X_-6JRmLMdpMPCRLDjqflfn2q-GUykDyRnKyfYy-erGEBiPBvbApXNzTM5Hh4cy5nXURJx4rU6m1W8kjKb-LcTAreHiq3EqyhRDd5kE3bG8JD-bFRQGbYCxzaQfUDbI0CTZa_vK14FQ8psoaX3fDOM1KbfYtLD8M1McB51U05GBaTXcKTSLAHT4LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت انرژی عربستان سعودی روز جمعه ۲۰ شهریور با انتشار بیانیه‌ای اعلام کرد که خط لوله انتقال نفت «شرق-غرب» (واقع در مناطق ریاض و مدینه) صبح پنجشنبه هدف چندین حمله قرار گرفته است.
در این بیانیه آمده است که به دنبال این حملات، عملیات انتقال نفت در خط لوله مذکور به صورت احتیاطی متوقف شد.
این رویداد همچنین منجر به مصدومیت تعدادی از افراد شد که خدمات درمانی و مراقبت‌های پزشکی لازم به آن‌ها ارائه گردید.
@
VahidOOnLine
وزارت خارجه عربستان سعودی اعلام کرد خط لوله نفتی شرق به غرب این کشور با پهپادهایی که از عراق پرتاب شده بودند، هدف حمله قرار گرفت.
وزارت خارجه عربستان سعودی افزود بنا به درخواست نخست‌وزیر عراق، در این مرحله تصمیم گرفته است اقدام تلافی‌جویانه انجام ندهد.
@
VahidOOnLine
خبرگزاری رویترز گزارش کرده که بغداد دستور تعطیلی گذرگاه مرزی شلمچه میان عراق و ایران را صادر کرده است.
دو منبع امنیتی عراقی به این خبرگزاری اعلام کردند که عراق این گذرگاه را به عنوان اقدامی احتیاطی و در پی حمله پهپادی از مبدأ عراق به خط لوله نفت شرق-غرب عربستان سعودی، بسته است.
گذرگاه مرزی شلمچه یکی از مسیرهای زمینی اصلی میان ایران و عراق است.
براساس گزارش‌ها پهپاد شلیک شده به عربستان از استان میسان عراق شلیک شده است. این استان در قسمت جنوب شرقی عراق و هم مرز با ایران است که مرکز اداری آن شهر عماره است.
@
VahidHeadline
رویترز نوشت: به گفته این دو منبع، عملیاتی گسترده برای تعقیب و پیگرد عاملان این حمله به عربستان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78337" target="_blank">📅 05:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78336" target="_blank">📅 22:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0oTDSpkMmo6o6uSp1u1rx7xQrM0WOTvtC_uSGu4YjOjHLmVZG2bJStL75J2Yjwe9qiE0KWzRu9pNlwGzAS0mgQXQud8xQ14cIEioJbFjprpLNgRNIxYkbWGdjEEi-txnzYeAVLtj-MfkyZENVYv2kGrVS83qus2MnLfRSH9j7UBSV3nC1ewZSmo7vsKgmG95AopYITiPEEqQFHvm4Bq5v5pWKi_v0WAEj3LAazKqE5hQo3KAM0XViJhnylegZP1bqjeN3jL5pkqPIj2whr8llRiM7--yt0-S9uYBdtyQncYwbvHgXSgKGr5HzpoOBcRiyLGkI7I1TftLbRbUcDR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس دولت چهاردهم جمهوری اسلامی که به هند سفر کرده است روز جمعه ۲۰شهریور۱۴۰۵ در پایتخت این کشور اذعان کرد که فشارهای آمریکا بر ایران به مرحله «دشوار و خطرناک» رسیده است.
او با اشاره به این که جهان امروز در یکی از «پیچیده‌ترین مقاطع خود» است، خواستار «همکاری عملیاتی» کشورهای عضو بریکس شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78335" target="_blank">📅 20:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=K9j8hR2hh67TGBgLaK4NFUsEda4bmbma83nKmzqSNKZaXeAHSvSLX6d22qBtNWEYVRtPw-kb_wZXao08YgAPigGWizgS4PS37wHk0Jan3WNHahlD0jKBEJldvZMdfwX-k2KoHNdsxV49UdJ-o-Y5PwFbd282EsvHm5Npf8opykXYXQBryI19FCJp1JShAYKmeltwccjqO0C97dfvT8G6TfGKHNLTDeEEesQLyJ2X6bhw-cpB2H3BxCyUEm_MAEJLI0wIqdIPH1CvFPsw3Rwrt0qv85P3JgSFA2qtWZSsnojtVD9P7nk92qbTAZN-KX-TJ9_nt375AQcYcXr0ln7HYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cf80dbb.mp4?token=K9j8hR2hh67TGBgLaK4NFUsEda4bmbma83nKmzqSNKZaXeAHSvSLX6d22qBtNWEYVRtPw-kb_wZXao08YgAPigGWizgS4PS37wHk0Jan3WNHahlD0jKBEJldvZMdfwX-k2KoHNdsxV49UdJ-o-Y5PwFbd282EsvHm5Npf8opykXYXQBryI19FCJp1JShAYKmeltwccjqO0C97dfvT8G6TfGKHNLTDeEEesQLyJ2X6bhw-cpB2H3BxCyUEm_MAEJLI0wIqdIPH1CvFPsw3Rwrt0qv85P3JgSFA2qtWZSsnojtVD9P7nk92qbTAZN-KX-TJ9_nt375AQcYcXr0ln7HYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرمحمد شاه‌کرمی با انتشار ویدیویی در صفحه اینستاگرام خود، از حضورش در مکانی خبر داد که به گفته او، برادرش آخرین لحظات حضورش در آنجا را پیش از بازداشت سپری کرده بود.
او در توضیح این ویدیو نوشت: «۱۸ شهریور، برگشتم به همان خیابانی که آخرین نگاه‌های برادرم آنجا بود؛ تا صدایش را از همان‌جا دوباره بلند کنم. این‌بار ایستادم برای صدا زدن نام امیرمحمد شاه‌کرمی.»
در این ویدیو، خواهر امیرمحمد با در دست داشتن تصویری از برادرش، نام او را در همان خیابان فریاد می‌زند.
امیرمحمد شاه‌کرمی، نوجوان ۱۴ ساله، در ۱۸ دی‌ماه در شهر قدس بازداشت شد و پیکر او حدود ۶۰ روز بعد به خانواده‌اش تحویل داده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78334" target="_blank">📅 17:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957af9390d.mp4?token=sr7_RroRq7InjBb3z6xY54CBFPRKPUns6D49I6B8EVADfhrv8nqa-hHn6ZXhdN3bt9UjJH9pC8lphdHM0qcyPrBqOdWHYc-8ArHC4yK0if-RNHkVrIwQQIut9V071sH5u3Q3wS_LIzTcTTQscdU_huq4ILYnnG7-R48QcM_KYiKksk0QuE_4MVT3vYl_waDzC14IZ1adyDQib_fC5oR3BUA_zdode8yAYnBPAb8nNNQ-g5sSp0hT05G3mi76BlrUakCCJju-8aBpEmee-O4lR0twXT6dW_KctTKioAhgGgJKqTmHejQZvIWuV6c6KEPvopaJDTUfxKG5koLkIGlwrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957af9390d.mp4?token=sr7_RroRq7InjBb3z6xY54CBFPRKPUns6D49I6B8EVADfhrv8nqa-hHn6ZXhdN3bt9UjJH9pC8lphdHM0qcyPrBqOdWHYc-8ArHC4yK0if-RNHkVrIwQQIut9V071sH5u3Q3wS_LIzTcTTQscdU_huq4ILYnnG7-R48QcM_KYiKksk0QuE_4MVT3vYl_waDzC14IZ1adyDQib_fC5oR3BUA_zdode8yAYnBPAb8nNNQ-g5sSp0hT05G3mi76BlrUakCCJju-8aBpEmee-O4lR0twXT6dW_KctTKioAhgGgJKqTmHejQZvIWuV6c6KEPvopaJDTUfxKG5koLkIGlwrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تسلیحات کشف‌شده در علی الطاهر را ایران برای حزب‌الله فرستاده بود
نخست‌وزیر اسرائیل روز جمعه ۲۰ شهریور اعلام کرد نیروهای اسرائیلی در جریان عملیات در ارتفاعات علی الطاهر در جنوب لبنان، مقادیر زیادی تسلیحات را از زیرساخت‌های حزب‌الله خارج کرده‌اند.
بنیامین نتانیاهو با اشاره به تسلیحات کشف‌شده گفت: «مقادیر بسیار زیادی سلاح از آنجا خارج کردیم که سال‌ها توسط ایران سازماندهی و تامین مالی شده بود.»
ارتش اسرائیل پیشتر با انتشار ویدیویی اعلام کرده بود، نیروهایش پس از به دست گرفتن کنترل عملیاتی ارتفاعات علی الطاهر، زیرساخت‌های زیرزمینی و روی زمین را منهدم کرده‌اند. به گفته ارتش اسرائیل، این شبکه بیش از دو کیلومتر امتداد داشت و شامل ده‌ها راکت، موشک و پهپاد و همچنین موشک‌های ضدتانک، مین و مواد منفجره بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78333" target="_blank">📅 17:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4B9OV8Xge6mTU_mGgIgFlnRXu3RcaMoosdMtzwmDKKa8I9Egzp8u4uAr2_w2ps8tP233xEdrz654DxUyLog-aSVd4wLgKppkktgixZc0TNCxNDQBJaB6ssULGiqe4ihP3ISBg8B78-tWqp0-_PlQeYW3l3LLqkgcY_FANQajVEL_Rz7CkUbh6_uepQzpWsEM-iS8JUpOcagLEi4oCwwvINJeaHTiW_XPXK96WErAEe933kzmW5R6dPmVvUNemBDk6vtq0Db7CQ0vbX9ayzxCXRGr_Ytn2lj0XzHVDRiwV4jSqSbRB6EnzKXcyQovEbAEBj0M8K_K13zHNoWrF4i5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گزارش‌های رسانه‌ای مبنی بر آسیب‌دیدن هواپیماهای آمریکایی در جریان حملات موشکی اخیر جمهوری اسلامی به اردن را رد کرد.
او پنج‌شنبه ۱۹ شهریور در مصاحبه با شبکه نیوزنیشن، در پاسخ به سؤالی درباره این گزارش‌ها، گفت: «نه. هیچ خسارتی وارد نشده است. هیچ اتفاقی نیفتاده است.»
کمی قبل از اظهارات ترامپ، شبکه خبری فاکس به نقل از یک مقام ارشد آمریکایی نوشته بود که موشک‌های بالستیک ایرانی در جریان حمله گسترده موشکی سه‌شنبه، ۱۷ شهریور، به هواپیماهای جنگی آمریکا مستقر در اردن، آسیب زده‌اند.
فاکس‌نیوز این خبر را به گزارش جنیفر گریفین، خبرنگار ارشد خود منتشر کرده است.
شبکۀ خبری سی‌بی‌اِس برای نخستین‌بار این موضوع را منتشر کرده بود که در جریان حملات موشکی ایران به پایگاه نیروهای آمریکایی در اردن، «چندین هواپیمای نظامی ایالات متحده، آسیب دیده‌اند».
ارتش اردن روز چهارشنبه ۱۸ شهریورماه با صدور بیانیه‌ای گفته بود که ایران در طول شب قبل، ۲۰ موشک بالستیک به سمت اردن شلیک کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78332" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTgds8V3Lp16HZtg08w5QRsW-wzXDXJBEQKpnbp3_i4ZBaTDDPQQCj3c_aSaHSa4MpgzMPHfGS1RY84_Z7xlp94YOhU0KRNjxjYuOdYuJUXb1tXOyC_GOIdbeo5BkWjib_jJbKNCp6APGsjZ06fK9by-lqDeAuxEi1UjQbfyeJ4eL29dsQCsF6HAbL9_H2GADE-FEgDnrs93kCgzH_ODouOIjJUbwzPIyp0TEULJ7fYaVsT6mgj_IMCFe4mUVqENl7tb8H6xL3GKj8L83pAHpPND4l7AFoZ1e4Ct1td6OAG3f4T4hPQAP2-u-kjGNeg_CIdmDKcvkKmQordyb4clwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت آمریکایی «آنتروپیک» اعلام کرده است که سه عملیات مرتبط با حکومت ایران را شناسایی و مختل کرده که در آن‌ها از مدل هوش مصنوعی «کلود» برای تولید و انتشار محتوای تبلیغاتی، طراحی سامانه‌های نظارتی و تهیه اطلاعات مرتبط با هدف‌گیری نیروهای دریایی آمریکا استفاده شده است.
این شرکت روز پنج‌شنبه ۱۹ شهریور در تازه‌ترین گزارش اطلاعات تهدید خود، مجموعه‌ای از موارد سوءاستفاده از مدل‌های هوش مصنوعی آنتروپیک را تشریح کرد. این گزارش فعالیت‌های شناسایی‌شده و مختل‌شده از دسامبر ۲۰۲۵ تا اوت ۲۰۲۶ را پوشش می‌دهد و علاوه بر ایران، مواردی مرتبط با چین، روسیه و کشورهای دیگر را نیز بررسی کرده است.
بر اساس این گزارش، آنتروپیک حساب‌هایی را شناسایی و مسدود کرده که از «کلود» برای اجرای عملیات نفوذ با هدف تاثیرگذاری بر افکار عمومی استفاده می‌کردند. سه مورد از این عملیات به عوامل همسو با حکومت جمهوری اسلامی مرتبط بوده است.
آنتروپیک می‌گوید هر یک از این عملیات از سوی فرد یا مجموعه‌ای انجام شده که یا مستقیما در یک نهاد تبلیغاتی حکومتی ایران فعالیت داشته یا به نمایندگی از چنین نهادی کار می‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78331" target="_blank">📅 17:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnlH5CEZ6mto-Fm0NeNJTB7608_OD-zvYLxx7F5QxWD49mcPyZzHxMWVpD_LqjuIez-MgVyb7yxSlbIBGAuci1JYNVmf2U1AB1b7xuSiZqaEtF_gCfG6jSi5Of0Rk5ad3xEZNsexE4tsXBHJwzVIsbY1UIhW1kA5O34x61bFBy8MXdNOBlI_JhQ4vgZ2GbodL1Zc8qJrbhwdZS2CEW7giTdpx7v8vBCbOrd4rgEln1c0_06QPDwmS4UXAgPOmr1mHg32eR4XXDcCJf1x11y7hb_O56g8rtJWYnbROfNN_76EiHKbzisau4CB_pIhprISnVLxhQOgu-3ZliwqM7ikAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت مخابرات ایران با انتشار اطلاعیه‌ای در سامانه کدال (سامانه اطلاعات جامع شرکت‌های پذیرفته شده فهرست شده در بورس) اعلام کرد هزینه مکالمه تلفن ثابت با تلفن‌های همراه از روز جمعه ۲۰ شهریور ۴۵ درصد افزایش می‌یابد.
به گزارش انتخاب، بر اساس این اطلاعیه، سقف هزینه مکالمه تلفن ثابت با تلفن همراه از ۶۲۵ ریال به ۹۰۶ ریال افزایش یافته است. این تغییر در پی ابلاغ دستورالعمل افزایش هزینه تماس تلفن ثابت با تلفن همراه، تماس میان تلفن‌های همراه و پیامک اعمال می‌شود.
شرکت مخابرات ایران اعلام کرد میزان دقیق تاثیر این افزایش بر درآمد شرکت هنوز مشخص نیست و آثار مالی آن در گزارش‌های دوره‌ای منتشر خواهد شد.
این شرکت در خردادماه نیز هزینه ثابت ماهانه تلفن ثابت را ۴۵ درصد افزایش داده بود. هزینه ثابت ماهانه مشترکان خانگی در تهران و کلان‌شهرها به ۴۳ هزار و ۵۰۰ تومان، در مراکز استان‌ها به ۳۲ هزار و ۶۲۵ تومان و در سایر شهرها به ۲۴ هزار و ۶۵۰ تومان رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78330" target="_blank">📅 17:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=RQn60JosDPvQ2VaSmNttsEhQZKhGDUxvjekr8FEDqlazqWMtJKJX3g3gShl_2W6zZr0HPEM0qbTwBDXcGgrIDM2sDb6Hei-RJjNMqckMJDqUf95lGrnvTwlij2GkU54Lg53GkRbTsOMn0AHiep-UgyAANYZFud5ms5pUF7Go97pR2xEEPLRFymJWXFSVfbIXGmej58FrMWZApFsYDWxxD6fRM8XuskqONHA1vGzkx5r7ZvJtILc5NTbOtUUv6EIIfhe-raYQdapSa-_qcM_cJLQnx623vVFdN__8nPTWCuDeXRScX-g12B4_MSS7pvvln4I_9w0LSwlVn2BELnA-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb8399ab74.mp4?token=RQn60JosDPvQ2VaSmNttsEhQZKhGDUxvjekr8FEDqlazqWMtJKJX3g3gShl_2W6zZr0HPEM0qbTwBDXcGgrIDM2sDb6Hei-RJjNMqckMJDqUf95lGrnvTwlij2GkU54Lg53GkRbTsOMn0AHiep-UgyAANYZFud5ms5pUF7Go97pR2xEEPLRFymJWXFSVfbIXGmej58FrMWZApFsYDWxxD6fRM8XuskqONHA1vGzkx5r7ZvJtILc5NTbOtUUv6EIIfhe-raYQdapSa-_qcM_cJLQnx623vVFdN__8nPTWCuDeXRScX-g12B4_MSS7pvvln4I_9w0LSwlVn2BELnA-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.  بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی…</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78329" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78328" target="_blank">📅 07:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmgT6e-MmDzvTwAi_6S5IOqdJo9K5eAMYlN1u4VFh2jtZyUidnDt_-k2QHm18GR-41MNrZc-mLKeS5F7o5ICjxo0FpsS9ikNBnhnGGiX_hIMC5Kx6fUbhxds8PKrbRCjfPvHm3Tc3kdRwqy77g2tnwLboApkzovFiD-9gkd9qyzIw-LT9-qSj6sPWpNMN5H5vdzTvGykfLkkIi0Ti0L5mTeed6b7jwJNGVwS3Y4zaOTFOJDphhh3S8KkZAVKpj-EDMgC6n4cGnYjhr1H9S3FhVyRuvW5v90lcLOH6NKM7Zkx57W_UfJZ4mJhUhqZk7cKEJqtS2Whs3utjB2h_iVojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا در دومین شب گردهمایی انتخاباتی میان‌دوره‌ای جمهوری‌خواهان که در دالاس در حال برگزاری است، بار دیگر، تنگه هرمز را «تنگه ترامپ» خواند و گفت «ما تنگه ترامپ را کنترل می‌کنیم». رئیس‌جمهوری آمریکا بار دیگر تاکید کرد که هرگز نمی‌توانیم به ایران اجازه دهیم سلاح هسته ای داشته باشد و نخواهد داشت. او گفت که ایران در حال عقب‌نشینی از همه جا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78327" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wih43peQInaaFxyGAQD0g5L2Y3WnqFo3vHZk-xQ1qD218i5ud-CLR3FMc1K9lbUmfoK9-xBLZ5bmKJudDjWEyB7MNsbynwIVuRzpLbFIgPqXQ4-uOiUOKqFqeYAIGjbgUZ0xSqQmrsl9zZA5VsVnJDKGTrEbmEM_GBsmmBwLa1FEaAxY73l8pslUqZByBrtcP9srQQ-10RZRPeCVLEIMFwia6DE1iQFdak--1N4YEju2RNgewaOecCovwUCPsNYjRXyl76bmHCA9CKbTw-zUEgOBlJuIHlOozPQbzusg-Ra0xjpnu9PUFDS721QJN7j7vvzQAQ68KpfhZJ3ddoIVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانگ کائو، سرپرست وزارت نیروی دریایی آمریکا، به اپک تایمز گفت نیروهای جمهوری اسلامی خسارت گسترده‌ای به پایگاه پشتیبانی نیروی دریایی آمریکا در بحرین، محل استقرار ناوگان پنجم این کشور، وارد کرده‌اند.
کائو در توضیح استقرار اخیر ناو هواپیمابر یواس‌اس آبراهام لینکلن و الزامات لجستیکی عملیات طولانی‌مدت گفت خسارت واردشده به پایگاه بحرین بر امکان پشتیبانی از این ناو تاثیر گذاشته است.
او گفت: «خدمه این ناو جایی برای پهلو گرفتن نداشتند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78326" target="_blank">📅 07:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2pLbIok3hGp9vRU_-H0ZXOxG1VlCzKzZL8yR9iFea9Ynzvair-BNJ057U2cFQo8Gdj-pv8ym-YqW0uxy_gZePDTpxoLEDimPghcLbEVx1yLqDec8_362cZzg9oybU9F1FX3ifoyilqegOoWStDdc_P6CFNkhfDpRJS78nY5iN4IQnTrOh74qWpdp8KkuCJ1kcWMGxPN91JPK7awYomvwXzSDkgV1ueh_oezS-lPjwb7GFM8Q3EFnoapbXZ7mugEsjIFUYl0uvLOpiZBZ---BzR16tHqDgyV_eqYB54MDVFAWtONfpDgtobPkDT1PO6W-b1Uq2pcG09W_GJ06sf61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت پنج‌شنبه ۱۹ شهریور هم‌زمان با تشدید درگیری‌ها در منطقه و افزایش نگرانی‌ها درباره اختلال در عرضه انرژی، بیش از شش درصد جهش کرد و نفت برنت به ۱۰۷ دلار و ۶۳ سنت در هر بشکه رسید. نفت خام وست تگزاس اینترمدیت نیز از مرز ۱۰۰ دلار عبور کرد.
بر اساس داده‌های اویل‌پرایس، قیمت نفت موربان با بیش از پنج درصد افزایش به ۱۲۲ دلار و ۴۸ سنت رسید و سبد نفتی اوپک نیز با بیش از چهار درصد افزایش، ۱۱۲ دلار و ۲۵ سنت قیمت‌گذاری شد.
افزایش قیمت‌ها پس از حملات به نفتکش‌ها در خلیج فارس و دریای عمان و پیشروی حوثی‌ها در سواحل دریای سرخ رخ داد. رویترز گزارش داد تصرف بندر مخا و پیشروی حوثی‌ها به سوی جزایر حنیش، نگرانی‌ها درباره امنیت تنگه باب‌المندب و مسیر صادرات نفت عربستان سعودی را افزایش داده است.
هم‌زمان، تردد کشتی‌ها از تنگه هرمز به‌شدت کاهش یافته و داده‌های اولیه نشان می‌دهد ۱۸ شهریور تنها هفت کشتی از این آبراه عبور کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78325" target="_blank">📅 03:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=mh09_ASmzLu0bVXG4xcw7hn-8lVlHgYGx8sRKtLfcZmwFgC8Bpbh0_fmf40E1QGAfDu4tD5OaFeY9Ds_vTCgwUCdZipIOYSnIQwKSV7hgZ7N-2M-mRbw7zlQHFV1ZHJcOOCMcsaj0YUzU9y_VPBN7Vjskl3r9-YfBhzJOBXk9ydKcuXXoPkGP2WceRZ-0YnSkT8Bfh_2bPnQqLFbF_AYg1JIzPkpEqfPDA1Qrkehg1PvuFpHuc5iXrK8yb8HEziQNB-x-fXxZDUNGqnR--YfELZIl0zNFnSMecya3n0U2YRZ8BkqPoEKfmEl1dglb3iy5F8GaqjjOqri9vJIvBw--A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09d9c8c443.mp4?token=mh09_ASmzLu0bVXG4xcw7hn-8lVlHgYGx8sRKtLfcZmwFgC8Bpbh0_fmf40E1QGAfDu4tD5OaFeY9Ds_vTCgwUCdZipIOYSnIQwKSV7hgZ7N-2M-mRbw7zlQHFV1ZHJcOOCMcsaj0YUzU9y_VPBN7Vjskl3r9-YfBhzJOBXk9ydKcuXXoPkGP2WceRZ-0YnSkT8Bfh_2bPnQqLFbF_AYg1JIzPkpEqfPDA1Qrkehg1PvuFpHuc5iXrK8yb8HEziQNB-x-fXxZDUNGqnR--YfELZIl0zNFnSMecya3n0U2YRZ8BkqPoEKfmEl1dglb3iy5F8GaqjjOqri9vJIvBw--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار ویدیویی در شبکه اجتماعی ایکس نوشت
:
امشب بزرگ‌ترین پایگاه ایران در خارج از ایران، یعنی تونل‌های علی‌الطاهر در لبنان را نابود کردیم. در حال تکمیل مأموریت هستیم. سال نو مبارک!
پیش‌تر ارتش اسرائیل اعلام کرد شبکه تونلی حزب‌الله در ارتفاعات علی‌الطاهر را با استفاده از بیش از هزار و ۱۰۰ تن مواد منفجره تخریب کرده است.
به گفته ارتش، در این تونل‌ها که طول آن‌ها بیش از دو کیلومتر اعلام شده، ده‌ها موشک، راکت، پهپاد، سلاح‌های سبک، موشک‌های ضدزره، صدها مین و مقادیر زیادی مواد منفجره کشف شده است.
بر اساس اعلام ارتش اسرائیل، با انهدام این سایت، عملیات تخریب شبکه‌ای متشکل از هشت تونل به طول مجموع ۵٫۴ کیلومتر در منطقه علی‌الطاهر و قلعه شقیف تکمیل شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78324" target="_blank">📅 01:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rAZqmjmXSk3GtkI3OY-K2VgeNuqbdKinF9Ct4YiB1CcJws9kZtpIFePREKmEVoAGKLkRNbm2NlPE0ax_IXoSFA3J89SayDrdo9P-NZAMRUEBUAVBvFp9ZvNYI_qUwSmef58utcoR5NlAlRnwDQYOJEU58mE21208K7akRcknWm9GPakSPt5P7nrk9VadQeWYYM0TfGYjVObMNkDRUZHV1XuvjnNQBy1dnoydB_WJ_Whp0MthGenZkIF0F8SiosZWhyM1fNxsoH8KtwNa1UHJTZ1IESWhf9jrbcmmXK8fxZbLWfRxf11rGLkUv70EsrmOZBBmCxGecOY9KJWpBxvn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا، یوکی‌ام‌تی‌او، عصر پنج‌شنبه به وقت واشنگتن از برخورد چند «پرتابه» به دو شناور در نزدیکی سواحل عمان خبر داد.
بر اساس این گزارش، این برخوردها در فاصله چهار مایل دریایی غرب شهر خصب، در استان مسندم عمان، روی داده است.
طبق این گزارش، کاپیتان یک شناور اعلام کرد که شاهد آن بود که چهار پرتابه نامشخص به دو شناور نامشخص اصابت کردند.
در پی این اصابت‌ها، یکی از شناورها دچار آتش‌سوزی شد و از وضعیت شناور دوم اطلاعی در دست نیست.
مقامات عمانی در حال بررسی این واقعه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78323" target="_blank">📅 01:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=dRcUWxg8Id_nQF8tpqXyDzCffWlUV5TIO5ylYSxTur7EQlay77Diumvzj0xeyVVZYmxLQ9rOOZpHROsOuV7iREJi5XQc_utvxOXt99_cUhGdB3qb9KheqptKd2BGnswuh_U7mzO0SD-En5w72X6zh9IM2dF3aTMGETVQu9eWfZyGSUj3TJL05rKDwFS-GouHsh3jmz1cw9zQ9_MF_BQA8_VNPNQn4mD-6dmxD0ALo7xWKjHtMulkUu3aGQdUHJDrCOjBhTT314FA9LhPtHQHS7Iavkd1ML7JmBlznY17Dg9AVf-TcJJMOIZpSmNo2E1jveVCVytHpLy_fMvNoUikEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c378ed4e1d.mp4?token=dRcUWxg8Id_nQF8tpqXyDzCffWlUV5TIO5ylYSxTur7EQlay77Diumvzj0xeyVVZYmxLQ9rOOZpHROsOuV7iREJi5XQc_utvxOXt99_cUhGdB3qb9KheqptKd2BGnswuh_U7mzO0SD-En5w72X6zh9IM2dF3aTMGETVQu9eWfZyGSUj3TJL05rKDwFS-GouHsh3jmz1cw9zQ9_MF_BQA8_VNPNQn4mD-6dmxD0ALo7xWKjHtMulkUu3aGQdUHJDrCOjBhTT314FA9LhPtHQHS7Iavkd1ML7JmBlznY17Dg9AVf-TcJJMOIZpSmNo2E1jveVCVytHpLy_fMvNoUikEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز پنجشنبه ۱۹ شهریورماه تصاویری منتشر کرد که به گفته این نیرو، هدف قرار دادن یک شناور بدون‌سرنشین آمریکایی در ورودی تنگه هرمز را نشان می‌دهد. سپاه اعلام کرد این شناور با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون» بوده است.
علی عظمایی، فرمانده نیروی دریایی سپاه پاسداران، گفت این شناور بدون‌سرنشین «جاسوسی» متعلق به ارتش آمریکا در تنگه هرمز مورد اصابت قرار گرفته است. او همچنین گفت: «تنگه هرمز مسدود و تحت اشراف اطلاعاتی و کنترل هوشمند ماست و هرگونه تحرک خصمانه مورد هدف قرار می‌گیرد.»
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد ارتش آمریکا طی روزهای گذشته شناورهای بدون‌سرنشین خود را به تنگه هرمز اعزام کرده است. مقام‌های آمریکایی تاکنون درباره این گزارش اظهارنظری نکرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78322" target="_blank">📅 22:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlrimZlQ4df_8nkErEQB5C-h9e_tyN1xjMcKjru4k2PsZYTG5bLFnavE60ntTB-Nps864PIyfKGPvo1zUUNxKOx6nTgukKuAuYPnF3dsyjDXONALpgBo9WzK2b4ppA2ycptpm21Fe3t9BKVxNcf8OzQxLOf0MXgkEsQqS3ObaUl0fyhtnPIHuX_ZnSRLdKqjBOAPNVHnqx3TES8UXjtX-tWKUZkRXZQ-Nuhey2bP2o25M6hbkxtnx4j7jZ9jQej4zyFkvoa_qTTTHTC0T_5ViMREQnb8GX-xxC9lPMUW8M24_4sJs46JxAjPm3UluV9Um9FQxB2BFx4279kZsc_phg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، روز پنجشنبه ۱۹ شهریور در گفتگو با بلومبرگ اعلام کرد این سازمان بر اساس تصاویر ماهواره‌ای، شاهد تحرکات ساخت‌وساز در سایت بسیار مستحکم «کوه کلنگ‌گزلا» (Pickaxe Mountain) در جنوب مجتمع اصلی غنی‌سازی ایران بوده است.
گروسی با اشاره به اینکه بازرسان آژانس هنوز موفق به بازرسی از داخل این تونل‌های عمیق نشده‌اند، گفت: «نشانه زنده از تحرکات در اطراف این سایت ساخت‌وساز وجود دارد، اما اطلاعات دقیقی از فعالیت‌های درون آن در دست نیست.» او یادآور شد که ایران پیش‌تر قصد خود را برای انتقال تجهیزات به زیر کوه جهت «مصون‌سازی در برابر حملات» اعلام کرده بود.
این اظهارات در پی ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل مطرح می‌شود. بر اساس گزارش‌ها، آژانس از ژوئن ۲۰۲۵ و پس از حملات نظامی آمریکا و اسرائیل به تاسیسات هسته‌ای ایران، امکان راستی‌آزمایی وضعیت ذخایر اورانیوم با غنای بالا را نداشته است.
دونالد ترامپ، رئیس‌جمهوری آمریکا، بار دیگر با اشاره به این سایت زیرزمینی، نسبت به هرگونه اقدام ایران هشدار داد و در یک تجمع انتخاباتی گفت: «ما متوجه فعالیت‌های مختصری در کوه کلنگ شده‌ایم. به ایران توصیه می‌کنم دست از پا خطا نکند، چرا که مجبور خواهیم شد ضربه بسیار سختی به آن‌ها وارد کنیم.»
از سوی دیگر، سی‌ان‌ان روز گذشته به نقل از منابع خود گزارش داد که ایالات متحده در حال توسعه سلاحی با نفوذ بیشتر با قابلیت تخریب اهدافی در زمین‌های سخت مانند کوه کلنگ‌گزلا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78321" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idWT9KRBSzFKzlDJ6lTyel9TgtRR6-dBQrNFWXxhBhQJHPPFtAI0ZCjl40GSEKbK4vYuN3VlhWFvSJdQZx0NGgZV1PPK58cjNu-oFG7kYKDz-LKfFLAVszWLE9JbScN9VHKF8EXUaaHp-PtMEjBJsabfQZOTdRhevqr0HQYJDpjW7vt30DtqBK-JFXXrrW-XZ1JYRmUjQcElh3JEbIOSG_DyBURQdIi1CpG1dOaZalv8Ju_gxHpsZc02gpdTrTBDpYwqnRaRG8r2hWynFBpIHc0S8JTPfwagLgH06dqlE1af8tmBPjV90PKaGcPt-S80FcBXoX3e2PN5qzxUzSirOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه قبل ماموران امنیتی به منزل خانواده «کیاوش میرقاسمی» از کشته‌شدگان اعتراضات دی‌ماه۱۴۰۴ یورش برده و «سمانه عصاران» مادر او را بازداشت کردند.
به‌‌دنبال تشدید فشارها بر خانواده میرقاسمی حالا صفحه اینستاگرامی مادر او از دسترس خارج و کنترل آن به اجبار به دست نهادهای امنیتی افتاده است.
تمامی پست‌های پیشین این صفحه حذف شده و تنها یک پست به دستور مقامات قضایی در این صفحه قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78320" target="_blank">📅 18:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78319">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf1MHA-pAdeArul0_rHjQL36YAZhqSHteVT8lPZ9Mzb_Dj8a1Gyq0PmMzalm9X9QrT_BArYmVtm8dVgB-Wtn939fT8XBdvDf-m2xOqgUJ5gZeuEgw0FngOgTMejVJ7Ys0F-6czO6wCip42r_q27D6qk0rDUvO1zvm8fTYiPQVxgwW3XPVvEV-MUmwVt5PxT23Ua_8jcTrNnZzoCjyv1l21Twt7WstBbXHCcqVoNvAuz6ibg4eQDzQlnG2Y-UGeXbItqcVuUxo_Rvk4KkPb_NwFMQm8b9dFfy6NU-zUw-8qiaL_jKywid8Uw76gq-LKvis2kiP_6H1YaBbDOucV7C5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس بریتانیا دو نفر را به ظن ارتکاب جرائم مرتبط با ایران و نقض قانون امنیت ملی بریتانیا بازداشت کرد.
این دو فرد در لندن پایتخت بریتانیا و در جریان تحقیقات مربوط به فعالیت‌های مرتبط با ایران بازداشت شده‌اند.
پلیس متروپولیتن لندن با صدور بیانیه‌ای تأکید کرد که این تحقیقات، با هیچ‌یک از حوادث ماه‌های اخیر که در اماکن و ساختمان‌های مربوط به یهودیان و جامعۀ ایرانیان مقیم بریتانیا رخ داده بود، ارتباطی ندارد.
هنوز جزئیات بیشتری از هویت افراد بازداشتی یا ماهیت اتهام‌های منسوب به آنها منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78319" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_vc_K0CcrrRGmsldJ_sqfYR1NFVVQE881iljicGGsii9zIx8Lrv42mZN8y0OASi3CuLkNnB1XsjPtISp1IyMFc8mBXBTsa967eueoTMLDSE0Cj_GOfqf9E12udC_cdMjxuNNzwiT_un0tsJZixW76a-Hn9TetczDdX71LocTvMucEIUGtXY_8_EDmVghWxNBZzPFQCjlUGXUwNduQczuxIymRTyeWE9-pX7EeOHr0UP1wvjy2nh-K_7JiI5xGC4wsVsuQ5tqD7_pqAewOp_QYw8ZsBes921sWlBCAAEs4DCoXIbWL-nUWssK9PxjCDNQAtcdRp3UyJeRsvEvdj9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CpK3A7mBYg1WqO6c7unTcEf56hldMkPvsp6ZXdu5t2TaXcn-LiAtarAOo09__thA9X0XYxx6czwckx0BO6bUy4pTZ7wfNO-D61XKHt-afH3VypmDM8db9NE3QgBv4UMW9KCkQeVMEoqvY3OTxaivwsev5CQW1a4Opfoq0eYGc1FR6vdP5xA50qHO2Sod1sVVt0oWDlbK8IICk1TUkW2sps8pq3tkOiubUDNxNbYmxaZdkp-ZaCbQPLxyCPJ6mt_0W6lEvgzv3OMfms89RdAg-RfUkr1NUb61j2ZVwcjhL44ktbjDLhcgaT8uHT9FEW1ZMxnSzq6oSo8HaWJeGACwxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اکانتش در توییتر:
MaryamAzimih
مریم عظیمی، مهندس ایرانی اپل، که پیش‌تر از بازداشت و انتقال خود با چشم‌بند در خودروی نیروهای اطلاعاتی جمهوری اسلامی در مشهد و تصور مرگ قریب‌الوقوع نوشته بود، در مراسم جهانی رونمایی اپل، یکی از فناوری‌های جدید دوربین آیفون ۱۸ پرو و پرومکس را معرفی کرد.
عظیمی در ویدیوی از پیش ضبط‌شده اپل به‌عنوان مهندس کیفیت تصویر معرفی شد.
او در بخش مربوط به دوربین آیفون ۱۸ پرو، قابلیتی به نام «تصویر مرجع اپل» را ارائه کرد.
اپل دوربین این مدل را پیشرفته‌ترین دوربین خود تا امروز توصیف کرده است.
حضور عظیمی از دو جهت در میان ایرانیان مورد توجه قرار گرفت: نقش او در توسعه فناوری تصویربرداری در یکی از بزرگ‌ترین شرکت‌های جهان و مخالفت علنی‌اش با جمهوری اسلامی، از جمله روایت شخصی او از دوران بازداشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78317" target="_blank">📅 17:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ORjMKVw1C1IrJln3ic8NX5ZVa735Z-cdZGEw8GxoghM6H8lF9vpBRVgQ_Wj0VNPolqf8eKu-6gJKlxkESlsvB0guR06aSY20xUY3t7mU_SkoKd5eozNiUW_W7x_hyGKrYhteL-0u86R8b1nZ1HrFWTyzAXNQVRdp91FCsV5pJfI72Aki8EkGhKx9cKAhuYI8eiAPP_kZEOm7HjRjPO7DgUuBeto5rGQXQJIu0ScpYxLFZyePE2B36-enoFaVCrOWoM__U1-fGIbFyuaN2TxEL00T_kWzMpAqX2HKEKC-BY5RHqUZaW-v5Xd7D6MY9iruU7yx6eGewTIYvMjjXmJzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fyXN8Fl1Aa9JCWGBBjDKjcZko517Qcy4O72QvGooHWBVmQODuBiK5hnYwaCNaIxSb-J61QVbrhrtxdpsJCbXthgE11jT6CuHT91OU6naqae4ib-9OXKbjJgaRE4KD2tVToJK3a9CcZvwF6bWgRu3087VxcTlPuuN19zZPnvtvXu4wuqImqH01ghb8eKg58y6cP8xHRcsqSBsWf8zTdXog5OOL7N-2-FGZUEL4PzjVTa9LlNEE8Umzn0Lf2nfXrGXVJM2piR6A-UcNMr94O-_Of7ZokYE7FgeHuXmLOuwHOK1m3xdOr_UjndSHAFnnTiBD64JwkVLTl1YCslKo9u9cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78315" target="_blank">📅 16:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bxd3NPVfWhwhfAyH6L9UPCyDIzKt06YujaFLBZJWGAgBKa6SjumGTWrNDjQ5tWg2sEYGbanLXemfRUCMoi-Y3D0XvtISKLV8BnJL6eB5RTKPykdH-6r_n_2PtR8saD9bYEhJUda5J87wHGS4MaGXGE9OoyfNnusOuB56CmAfm6WEsoHEQZQ_GafHwHNPxV_17WtoL5rHTiMS0Ac3u_ZYoQPaTXlDSTnrpZCMCgfFEKjmhoICsT60K-TWQ01ms6BpixrTAzVRW0QpZjLoPXS4N0a311F0UijMoRRjDSPdKeR8H4I3cNkt22B9xgBpzb9zNas8h1LJJj69fWt3euYoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند افزایش روزانه قیمت ارز در بازار تهران روز پنجشنبه ۱۹ شهریور (۱۰ سپتامبر) ادامه یافت و بهای دلار به ۲۳۵ هزار و ۷۰۰ تومان رسید.
dw_persian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78314" target="_blank">📅 16:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0ZFI3f-dDuenQCnSz1TiSDrO-x2ZpAFFuCyD46CjA9kaJPpOMK20hqoiMZJzNVwmiZo7OUYwZ-1kiX9egnAYXExDq-u7Q5Y3c6gmsf1wSqG--YNPggpa8EF7_rywmfLf2M_Q24-v6j8C47dZbALvMDo8hEnqIiCOGb6E_Ce3UzBRTuM5nyRpolxO5ZlTTi2NGKa7PUcrmGU8JovhOXJz0wEB_RJgGGc5HC27ymrwvnoP0kX4M-2F1zDvkXxEGBTDuM2HgMSGeLwr3xheZ3ySW2jdVex3hVKagzZIfIPdCzWPlVELHHSUArpF6VZxwRqksKUJ_65nQMf7oHLXt8dzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌ها در خاورمیانه، قیمت نفت شاخص برنت روز پنج‌شنبه از ۱۰۲ دلار عبور کرد که نسبت به روز گذشته حدود یک درصد و نسبت به ابتدای ماه حدود ۸ درصد رشد نشان می‌دهد.
طبق برآورد اداره اطلاعات انرژی آمریکا، ماه گذشته تولید روزانه نفت ایران به خاطر اعمال مجدد محاصره دریایی آمریکا ۸۰۰ هزار بشکه نسبت به ماه ژوئیه افت کرده، اما هم‌زمان تشدید حملات جمهوری اسلامی به کشتی‌ها در تنگه هرمز و آغاز حملات حوثی‌ها در دریای سرخ و باب‌المندب به نفتکش‌های عربستان نیز باعث شده متوسط تولید روزانه نفت کشورهای عرب منطقه در ماه گذشته ۹۴۰ هزار بشکه نسبت به ماه ژوئیه کاهش یابد.
مجموع تولید نفت ایران و کشورهای عرب منطقه در ماه گذشته ۶.۷ میلیون بشکه کمتر از دوران پیش از جنگ خاورمیانه بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78313" target="_blank">📅 16:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5TbcJgqD5DfC89xtBvon376_etQoi2gX0k_JpqYGn2o0GdLYpEQFT04W_bkjYCMC9dnkma6TtwL3vfnmzfnExy7pYrtbcyBX_8-lGepgapSaRHlC41U9QefDhQa0ip2_tX2_pT_TuVHv9hAcJhe5BMfWmKiLFVJ4Yb13iOIdYgddlF7lEngjT7pn7u-cQpBVinPUPpa_0IZbCPQDTE5287h2uUdLCqoqHak9UUXScWwhdGTNbbJtjuyFFd6nbMSu3uEgq47pZbGeuXtYFULXS63JJ9h3pYZMDnCbp3pGm7wG3wQzYpw_i6Tjho7iW4ejX_53AbM7c-i5xg8FIEj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد ایرانی و سه فرد مطلع می‌گوید حکومت ایران با استفاده از سازوکاری شبیه تهاتر و با دور زدن تحریم‌ها، در حال وارد کردن میلیاردها دلار کالا از جمله تجهیزات نظامی از چین است.
در این گزارش که روز پنجشنبه ۱۹ شهریور منتشر شد، منابعی که نام‌شان اعلام نشده گفته‌اند بر اساس این سازوکار تجاری مخفی، نفت ایران در ازای اعتبار برای واردات از چین در سال‌های اخیر، یک شریان حیاتی مالی برای تهران همزمان با افزایش فشارهای اقتصادی و نظامی ایالات متحده فراهم کرده است.
آن‌ها گفته‌اند که این سازوکار همچنین به چین، بزرگ‌ترین واردکنندهٔ نفت خام جهان، کمک کرده است تا به نفت تخفیف‌دار ایران دسترسی داشته باشد.
به نوشتهٔ رویترز و به نقل از منابع طرف گفت‌وگو با آن، ایران از این سازوکار برای خرید دارو، وسایل نقلیه و تجهیزات ارتباطی از چین نیز استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78312" target="_blank">📅 16:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=gB4Gp13SUCmNUyEXhNUgHCg_y1ecq0pOY7Y79wqRarnG7Vq0snPX1y4vkseWszDF4788KAC1SUnw9LJPnQzDcTNsZdNEeF1y02Nhn9ywcMVjrj0k2nGVwTEHVIWacmfejJ1c0-gpQlZXfaodvpm1vlMfm-dq3hTaDoGayfVX_xRuK6KAA_tIEb8-P0EOgtUGdtZfL6x6PiaK89qhJVXzCOJoO63VE3b7-NVjO0kY8XtJ7o3E3_Kb1o6fndV9zcYcTDQYCzm1XecCiodsq0dFgpMIQTF_kQTh5VWTP_FGWc_me2Ma2Tl5xkj5nxEPnwWjitbp1WCkLIglH_9p4tbgYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2c630a3b3.mp4?token=gB4Gp13SUCmNUyEXhNUgHCg_y1ecq0pOY7Y79wqRarnG7Vq0snPX1y4vkseWszDF4788KAC1SUnw9LJPnQzDcTNsZdNEeF1y02Nhn9ywcMVjrj0k2nGVwTEHVIWacmfejJ1c0-gpQlZXfaodvpm1vlMfm-dq3hTaDoGayfVX_xRuK6KAA_tIEb8-P0EOgtUGdtZfL6x6PiaK89qhJVXzCOJoO63VE3b7-NVjO0kY8XtJ7o3E3_Kb1o6fndV9zcYcTDQYCzm1XecCiodsq0dFgpMIQTF_kQTh5VWTP_FGWc_me2Ma2Tl5xkj5nxEPnwWjitbp1WCkLIglH_9p4tbgYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب «کاروانسرای روس‌ها» در سبزوار:
quotes
خانه واجد ارزش تاریخی «تومانیان» معروف به «پادگان روس‌ها» در سبزوار روز چهارشنبه در روز روشن با لودر تخریب شد و اعتراض گسترده فعالان میراث فرهنگی را به همراه داشت.
تصاویر منتشر شده در شبکه‌های اجتماعی نشان می‌دهد که یک دستگاه لودر روز چهارشنبه ۱۸ شهریور بخشی از یک بنای تاریخی معروف به «پادگان روس‌ها» در سبزوار را تخریب کرده است.
«پادگان روس‌ها» یا خانه «تومانیان» در سبزوار با وجود آنکه در فهرست آثار ملی ثبت نشده بود اما از سوی میراث فرهنگی به عنوان یک بنای واجد ارزش تاریخی اعلام شده بود.
معماری این بنا متعلق به دوره پهلوی اول بوده و در زمان اشغال ایران توسط روس‌ها، ارتش روسیه مدتی در این بنا مستقر شده و به همین دلیل به «پادگان روس‌ها» مشهور شده است.
مجتبی کاویان، مدیرکل میراث فرهنگی و مدیر پایگاه بافت تاریخی سبزوار در گفت‌وگو با صدای میراث گفت: این اثر بدون هماهنگی و بدون مجوز میراث فرهنگی تخریب شده و اعلام جرم علیه تخریب کنندگان این اثر واجد ارزش تاریخی قطعی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78311" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LqfmFdK1PZxi1T7PRxkliv0iMK9Y5xPg7Tl0pNK4U950zsWkQMNxM3A9RWc2JK4J9eVepMhgQlv4MnuCHi70tcWKB39Z-9QOQlWFvZgdP4g0nhGxo_SPkRUXdxM2wpsRCph73_UVpisff9vs3ufeKTd-uZ3Tu2XRYsBsZKyqbQWzc-nm2zM0nifQAZs_Gqn8-dSCj20BmLTvntH6nba1l9fgwtAQid80l3mXXZiG0lHGM331kl3GIVi7ya-npbWLhvgbYXugPN3b4X9XW6fqBm3MyIDwG01Rt3u1JAyY1xKvkQ2DwZbYwlp9bz7kMYsw-V2pYlOGj47PWpla94iLtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t9yJQNACdtBwnL8xbcYoect2v0un_Cv_q1k3yhvxT8uEo11PLulMJfiItieHT8z3OrWARXcwilqAEsFvZaqNpnejMr1tdftit9d32d7hcMUXW9LyLTL24wjuC2sogPi4-RIWBlW8ujp3Kj-NdU0dxCmJTdB7ZAa_LRbTPEYG4Qp2TT059wkDRZtkJ1VZzCUqmFmzOhrv2ObOfEktoR49TFbGTwp-YNCtC_z_xPmhWw1F86cHKCD4pCWzCN2p18O0J4EgaQTDJO2ri3dbs6JkpvvfSFFPOz89IOjxPzeWvQtYBQky0AHpYTiPvZh48aiu-OXL5_y2nAzQERFGHjIAQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ از مشاهده «تحرکاتی» در کوه کلنگ‌گزلا خبر داد و به جمهوری اسلامی ایران هشدار داد: «توصیه می‌کنم ایران زرنگ‌بازی درنیاورد، زیرا مجبور خواهیم شد بسیار سخت به آن حمله کنیم.»
ترامپ در ادامه از حاضران پرسید آیا ایران باید سلاح هسته‌ای داشته باشد و پس از پاسخ منفی جمعیت گفت دولت‌های پیشین دهه‌ها تلاش کرده‌اند جمهوری اسلامی را از دستیابی به سلاح هسته‌ای منصرف کنند، اما به گفته او، مقام‌های جمهوری اسلامی ایران «زبان گفتگو را نمی‌فهمند.آن‌ها فقط یک چیز را می‌فهمند و اکنون به مقدار زیادی از همان نصیبشان می‌شود».
@
VahidOOnLine
رییس‌جمهوری آمریکا، در گردهمایی جمهوری‌خواهان در دالاس گفت جنگ با جمهوری اسلامی مدت کوتاهی پس از انتخابات میان‌دوره‌ای سوم نوامبر پایان خواهد یافت و تهران خواهان توافق با دموکرات‌ها است.
ترامپ برجام را «یکی از بدترین توافق‌ها» خواند و گفت جمهوری اسلامی در مسیر دستیابی به سلاح هسته‌ای قرار داشت.
او افزود: «اگر من برجام را لغو نکرده بودم و اگر با بمب‌افکن‌های زیبای بی-۲ آنها را هدف قرار نداده بودیم، اکنون سلاح هسته‌ای داشتند.»
ترامپ گفت در آن صورت مجبور بود با رهبر جمهوری اسلامی تماس بگیرد و بگوید: «جناب رهبر، حالتان چطور است قربان؟ کاری هست که بتوانیم برایتان انجام دهیم؟»
ترامپ در ادامه تاکید کرد: «ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. موضوع بسیار ساده است. نمی‌توانیم اجازه دهیم آنها سلاح هسته‌ای داشته باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78309" target="_blank">📅 06:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78308" target="_blank">📅 06:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78307" target="_blank">📅 06:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78306" target="_blank">📅 06:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان ساعت ۰۰:۲۵ قشم صدای انفجار اومد
قشم صدای انفجار اومد
وحید قشم بد زدن تمام خونه لرزید
#قشم
00:24 نوزدهم شهریور
صدای انفجار و لرزش
قشم صدای شدید
شیشه ها لرزید
موج انفجار شدید همین الان قشم 00:25
وحید قشم یه صدایی اومد
شیشه ها لرزید
صدای یک انفجار بندرعباس
وحید جان انفجار شدید ساعت 12:25 قشم
سلام صدای وحشتناک باعث لرزش شیشه خونه شد
سلام قشمو بد زد کل ساختمون لرزید
همین الان نزدیک قشم صدا انفجار اومد.
خونه لرزید.
صدای انفجار به بندرعباس رسید لب ساحل نمیدونم کجا زدن
درود به آقا وحید شبت بخیر ساعت 0:25 انفجار سنگین از سمت دریا نمیدونم قشم بود یا جای دیگه ولی بندرعباس به شدت حس شد
قشم لرزید
موجش قوی بود
شدید بود خیلی
توی دریا بود انگار
سلام داداش وحید .صدای انفجار مهیب در قشم شنیدیم
خیلی مهیب بود ..
۰۰:۲۶ بندرعباس انفجار رخ داد
فقط صدا نبود
در و پنجرها هم تکون خوردن
صداش انقدر جدید بود ما داریم میگردیم میگیم لابد اسانسور ساختمونمون ول شده
🤦‍♀️
صدای انفجار در خونه لرزيد قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78305" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/692967643d.mp4?token=vCmsNEBgaU1cCLTzkUaHrI0w3R2TCOdU2tmz99vgy-fSBZh7k3m2FSOWSjvY8G67dj_LPm14qvY5ze6OMgsNoTADrX9nzD3PMPgx1Ctr5eT3FVCBavL3Kt2eQ3LHu8nSu2ojQb7p2-AoFUMQVZoVqVZk7cMQgXWt5LZvYpVwoOwYiJt6yB82bFZQP6NwWHNZMY91augLqcLl3y6vRMt47va2eUkMs1iKcEJgqXVhC0RRPC849SyzfJRWX37_iDx35h-6ALeQzQ-A9emE7mlZqQy9rW-BXqt1tdrX3_hi8VJKHMu-IdYIVl2esduHQeu5Nftn3CQG04eGN6BwENwClw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/692967643d.mp4?token=vCmsNEBgaU1cCLTzkUaHrI0w3R2TCOdU2tmz99vgy-fSBZh7k3m2FSOWSjvY8G67dj_LPm14qvY5ze6OMgsNoTADrX9nzD3PMPgx1Ctr5eT3FVCBavL3Kt2eQ3LHu8nSu2ojQb7p2-AoFUMQVZoVqVZk7cMQgXWt5LZvYpVwoOwYiJt6yB82bFZQP6NwWHNZMY91augLqcLl3y6vRMt47va2eUkMs1iKcEJgqXVhC0RRPC849SyzfJRWX37_iDx35h-6ALeQzQ-A9emE7mlZqQy9rW-BXqt1tdrX3_hi8VJKHMu-IdYIVl2esduHQeu5Nftn3CQG04eGN6BwENwClw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز چهارشنبه ۱۸ شهریور گفت که از دید او جنگ با ایران «بلافاصله» بعد از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت.
دونالد ترامپ پیش از عزیمت به سمت شهر دالاس برای شرکت در اجلاس حزب جمهوری‌خواه به خبرنگاران گفت: «فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام خواهد شد. چون آن‌ها (ایران) دیگر نمی‌توانند دوام بیاورند».
ترامپ درباره وضعیت ایران افزود: «آن‌ها مستأصل هستند و تلاش می‌کنند بر انتخابات تأثیر بگذارند».
ترامپ در پاسخ به پرسشی درباره حملات گسترده طرفین در اطراف تنگهٔ هرمز گفت: «حملات توسط ما انجام شد. ما ۹ نفتکش آن‌ها را زدیم. قرار است حملات بیشتری انجام شود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78304" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/739c863db9.mp4?token=NP1Vccf_yO208P9d6BRcSeNUSJWZeLF7LFg2BXHQNAW22QEDmNgUusZU8IKGXZ93GW-0h2gEeRm_5D7_C7B0wHR2IXvlk35QGtnGQjHrt_3SgsFsayYLhMgM6dE1uhSB_qcrcwbLcCqGyu2mloIY4cMvXpZsehstqwbPD8gnCq-yyx2DhSBKx5x2u1xBJ2DuWiqjjqWGSyPhagS07RxzYSKJjZMgviUG-_uYYgHBWAIXGFeXXLnmHDC1-Q5yzPlGKXuYBkNmt4npyX7mVhhYs9zWSLEDrxfeSKxLnz_VTEBzT1-OZRUv_nFHepikbQ-8WznNH9gMMzd5r4O7bo7cfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/739c863db9.mp4?token=NP1Vccf_yO208P9d6BRcSeNUSJWZeLF7LFg2BXHQNAW22QEDmNgUusZU8IKGXZ93GW-0h2gEeRm_5D7_C7B0wHR2IXvlk35QGtnGQjHrt_3SgsFsayYLhMgM6dE1uhSB_qcrcwbLcCqGyu2mloIY4cMvXpZsehstqwbPD8gnCq-yyx2DhSBKx5x2u1xBJ2DuWiqjjqWGSyPhagS07RxzYSKJjZMgviUG-_uYYgHBWAIXGFeXXLnmHDC1-Q5yzPlGKXuYBkNmt4npyX7mVhhYs9zWSLEDrxfeSKxLnz_VTEBzT1-OZRUv_nFHepikbQ-8WznNH9gMMzd5r4O7bo7cfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامعلی حداد عادل می‌گوید حکومت فعلا نمی‌تواند «به علت شرایط جنگ آن‌طور که باید وارد جبهه حجاب» شود.
این عضو شورای عالی انقلاب فرهنگی و مجمع تشخیص مصلحت نظام در ادامه می‌گوید شرایط کنونی کشور از نظر حجاب «بسیار سخت‌تر از سال ۶۰ است که شروع به کار کرده بودیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78303" target="_blank">📅 21:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fpUkA9T5uSy0APdZBYthiaGq5_dZkzLi65EkYq9Wcc6B6ZBHm2ufrCWMTpzroFyIz7zoI8BocZ-LI6u3d95UaUcONgXkYwCRnNVDjYy8W92_kj-354rqgwb85b6xm9dNlEfPiVVXuVjJin1HLMqglMc2DMjF1aCcXS04cJqUTB_5GojQ03d1HxEzvB5u0Cn3ZHPOszcqk2YvnGcucudd7YsFAHNBxXXZrVbtFvEkZLX_aKZa30eV6ABKi2NvlG5htXEIgJMgBVvp4XZUGAColiFVAdRL2aAcCn4vFHjKm4cHj7s6x2z0bcTB5DmQRsU0sbs8P-RgNcH-WXDysnG0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز روز چهارشنبه ۱۸ شهریور به نقل از منابع دیپلماتیک گزارش داد که شورای حکام آژانس بین‌المللی انرژی اتمی با صدور قطعنامه‌ای، پرونده ایران را به دلیل نقض تعهدات منع اشاعه هسته‌ای، پس از ۲۰ سال به شورای امنیت سازمان ملل متحد ارجاع داده است.
این قطعنامه جدید در پی قطعنامه پیشین شورای حکام در ۱۲ ژوئن سال گذشته صادر شد؛ فهرستی از موارد «پایبند نبودن» ایران به تعهداتش که درست یک روز پیش از آغاز حملات هوایی اسرائیل و متعاقبا ایالات متحده به تاسیسات هسته‌ای ایران تصویب شده بود.
بر اساس قوانین و الزامات حقوقی، گزارش رسمی این نقض تعهدات به شورای امنیت سازمان ملل، مستلزم تصویب دومین قطعنامه از سوی این شورای ۳۵ عضوی بود که اکنون به سرانجام رسیده است. این اقدام می‌تواند مسیر را برای بازگشت تحریم‌های بین‌المللی و افزایش فشارهای دیپلماتیک بر تهران هموارتر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78302" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vpSWhWDRoInw1yLtA0VaeQ7TQb3a28B1RraGD-8zbuOkKeuZSa34qCfr4q7TblgPpqSrVMpamxwM_xpfplGl3-O49D8MN5Rls3nDBwnNNy5OB69M_3W3LXWmZiQe77oOLIMXXDj6qUEWaZuDx6lcxJ2jdlHDp3aWjy5Z5Vohx0wQE2F6uG7FVWD-bmo-WiP68-Q5wx_U4itKw0iHhhBu_xVPBInxO2q4KDkZHgitgENYFk8XVQiKwFz4R2BAyd34X5fWIBR57yB_7gUwwKHjDt6fGIIfRj3CuZIE0EZSk_yjeUKvzoENol9gVDTzPBWvSHY1T4P8nZc3ieEiyakwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'شناور آمریکایی در تنگه هرمز، سمت جزیره سلامه خصب عمان، چهارشنبه ۱۸ شهریور'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78301" target="_blank">📅 19:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=bqjHWJLz3P4FH69p8j620XiVC4HtwybIv9fSslbxYzuZDpreqpMbyTLnhlLhae7MZAv-znQeDYpQ_KaGsiZ-j1B4ENG_GztBeF5a11yW7p6Zi_XNkTaJo6WxsjZYICxJe0wltlckmgONamXOBw2N9qqhw1ZmJzw-NQcz-h5V-CU11v3QeZOLceqxLwKcOXpUU7VH9chcBz-2qD-xIBHqy7OZw7UmcpJgAOONI1QcQMchUvssqG6XpWbXttbhfMQCFjZ46ZaHWNQFlLJyTJsuGfZ7Va3VwjRZ1ktGn9e75TAZX_c-a0xVhqOwqspGJGp_70lfaca70AB0XrbwU3bQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c510746f.mp4?token=bqjHWJLz3P4FH69p8j620XiVC4HtwybIv9fSslbxYzuZDpreqpMbyTLnhlLhae7MZAv-znQeDYpQ_KaGsiZ-j1B4ENG_GztBeF5a11yW7p6Zi_XNkTaJo6WxsjZYICxJe0wltlckmgONamXOBw2N9qqhw1ZmJzw-NQcz-h5V-CU11v3QeZOLceqxLwKcOXpUU7VH9chcBz-2qD-xIBHqy7OZw7UmcpJgAOONI1QcQMchUvssqG6XpWbXttbhfMQCFjZ46ZaHWNQFlLJyTJsuGfZ7Va3VwjRZ1ktGn9e75TAZX_c-a0xVhqOwqspGJGp_70lfaca70AB0XrbwU3bQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با حضور در قله جبل‌الشیخ (حرمون) و اشاره به تسلط بر مناطق مرزی سوریه و لبنان، هدف اصلی کارزارهای نظامی جاری این کشور در منطقه را شکست و سرنگونی رژیم ایران عنوان کرد.
نتانیاهو در پیامی ویدیویی، به حضور نیروهای نظامی اسرائیل در مناطق مرزی سوریه و لبنان اشاره کرد و گفت: ما اجازه نخواهیم داد هیچ گروه تروریستی در مرزهای ما مستقر شود. این یکی از دستاوردهای عظیم ماست، اما کار اصلی هنوز باقی مانده است.
نخست‌وزیر اسرائیل با ابراز اطمینان از دستیابی به این هدف افزود: کار اصلی ما شکست دادن و تضعیف کامل رژیم ایران است. ما بسیار به این هدف نزدیک هستیم و می‌دانیم که کل این محور سرانجام سقوط خواهد کرد و ما این کار را انجام خواهیم داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78300" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNdHto83yMDMdfZb-nxV0ub18VEM0D1QpLd9fsskGvNw5bfRTttjErLv6nCV59h1LhmVlO0dTpsCrDJq3HTuYYPr6TESvFefUydFbf2WEJVc8pp3TWk0LhFegnDw4211oX9_aj-awmDZe48Z93s_rKVBSTqDWGLzGo0F0VQsrdkz0njr2-3fuzjGT9dZowzFUZcUhvUj9z1u5j5_d9cbFd68RO9NIaAbdbQlRhqOjqSHCKK5bMfiroqJZ7fwHuYR0ladfGYQuyzX0bqTLpCdHhH_PWB7lWGGSiiZgoazEIfzYvH7A7095J0XLdb8GxQnapV6m6857q0GjROfwk2QSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه پاسداران برای پایان وضعیت کنونی و بازگشایی تنگه هرمز از آمریکا خواست جنگ و تهدیدها را متوقف کند، اسرائیل از لبنان عقب‌نشینی کند، محاصره یمن پایان یابد، ۲۴ میلیارد دلار از دارایی‌های مسدودشده ایران آزاد شود و مداخله در برنامه‌های هسته‌ای و موشکی جمهوری اسلامی متوقف شود.
حسین محبی، سخنگوی سپاه پاسداران، روز چهارشنبه ۱۸ شهریورماه گفت اگر آمریکا خواهان پایان وضعیت کنونی است، باید ضمن «توقف کامل جنگ» از تهدید دوباره دست بکشد.
محبی در بخش دیگری از سخنانش تهدید کرد که در صورت ادامه حملات، پاسخ سپاه گسترده‌تر خواهد بود و گفت: «اگر دشمن دو یا سه هدف ما را بزند، ما با ۲۰ هدف پاسخ محکم می‌دهیم.» او همچنین گفت جنگ کنونی برای نخستین‌بار «آسیب‌های راهبردی» را مستقیما به آمریکا منتقل کرده است.
این اظهارات در حالی مطرح شد که با تداوم محاصره دریایی ایران، صادرات نفت از طریق تنگه هرمز متوقف شده و فشار تحریم‌های مضاعف دولت ترامپ، باعث تورم کم‌سابقه در ایران و رسیدن قیمت دلار به ۲۳۳هزار تومان شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78299" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sedVoCfOMTOMCxVUHXgJlc430zoneApc1qbmww_cXdtzROd5h9ot0MWzvYoUW1icHAZzNEEgemaKY8cyI2u7E3OJybTNYb7JHuiYuvnp3Ff05PUtKngYBYKpvUMOwsbxUNSlqZZ5HcxUHMESPpIKfIHu3awLN43bP2GOq9vpEmy1M8ErOAzAWuW382aNF8Vr_UA6Y18le6j1oVB-6oGwZb6cBRQk7XmjliVD8-wdb6jkwYPumr_20PrD8p-6KkQbYWUzpriiEM5h0lT-KRunFQV_aprk5RIL4CGLriMA7BPEnyDT5sa38OB9h2iZ1W90ZQYX6YWAwTthX1Y8UvMBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۱۸ شهریور ۱۴۰۵ رکورد تازه‌ای ثبت کرد و نرخ دلار آمریکا از ۲۳۲ هزار تومان گذشت.
برخی وب‌سایت‌های اعلام قیمت ارز نرخ دلار را در معاملات ظهر چهارشنبه تا ۲۳۵ هزار و ۵۰۰ تومان نیز گزارش کردند.
هم‌زمان قیمت یورو از ۲۷۱ هزار تومان و پوند بریتانیا از ۳۱۵ هزار تومان فراتر رفت. این افزایش‌ها در حالی ادامه دارد که ریال طی دو هفته گذشته بیش از ۱۵ درصد ارزش خود را در برابر دلار از دست داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78298" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErgK5hsaXbTCszb3hqnR-IT4jigjxKRFJCzZECTanDGywQz1RvIFueNhv6hWSjRFB-ZzdwGgARK6mwjN1pqriSGKdKOQ-g5wIVnRXIyW-nBh7NF1cR5D7gE9F1UJ1PWHdMZUcG2mY_dSdbMc9HGJF1ZWbTQHcEKIgWcn3e5x060A0axj6y6ZUGgiOMSixDI-ImYwghtGVi5BKXny1Y8H2aEatXSHkS4fYV94desVNwWuGZZj_tbOB35teMH74DDPexAicDPlVOEoZi3nS1rXdI3AgfARAgPN_x6QRBO2PT9nROiwjXRR3bMvYIutCJzNzAYGwtv9Y6pQnPm33Ru2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت خام برنت برای نخستین بار از دوم مرداد به ۱۰۰ دلار در هر بشکه رسید و بار دیگر وارد محدوده سه‌رقمی شد.
افزایش قیمت نفت و ارز در شرایطی رخ داده است که درگیری‌ها در خلیج فارس و منطقه ادامه دارد. شامگاه سه‌شنبه ۱۷ شهریور، آمریکا اعلام کرد پس از حملات موشکی ناموفق جمهوری اسلامی به دو ناو جنگی این کشور در خلیج فارس، پنج نفتکش مرتبط با سپاه پاسداران را منهدم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78297" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aMAcgNyNSjdSx3BiWZHHcaXFAaGTbr0kLUe7InIsmKQ5MatBdefwVfvBAI0YFovf4WNR5AEIRw0QlGaGhOlekXn3CcAwrZdhFac7KTnUNfiZOPKmVc5oP_ZVuiEIKKXgFlVvBMFBVMP-7KLP2ESpUc2tMu63zWhy-kMrGL0nDcGNBsIbNW4UXpKVP4vFHHullXZRUMF4vr2Pu69l-F0RMHxC--A0fTvP2jw2Ap3oOruV28MFUMrwNZo7jeXEZ6Wr2oNaU2_z5eo68obvrw6eEZTY0tTNzUm9dr8awADmoNjoAo37qg3Bd-ZJdd1YLSYx87CvUIu3-UjBOdvcTGHNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cGDO-sZ6oedbPih255dG91L8GiEvhbPd6vcqJrYIrqs_UgI-HpXJ5ZGp0ERBapawkJjEgbiPQikGHQqatyhoLYP9Hx7CYkLCFjDc4hCQDIBOxmy78IAuUEFAUoy_wfhRQKpTvNPu6-zdGLSpe6rH4IRN9suOJL48WxIqMrglXtBUEoovKq3ynrewek7TKVAJZBNDsTXHpLrtsbuaIx5o8hmQsOh866f-5cT5exv-Q8exxawrjdBMFv0hdHkdBe1ttaWCTG7ovQHMhW9ja33HBtBvcRYm6CHSQpnU2MSqW_0QUgZNjJkoWWuQMuQqeuYr4GKHSJ9nJnMKaBXX1PG7TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا (UKMTO) ظهر چهارشنبه ۱۸  شهریورماه از وقوع حادثه برای یک نفتکش در ۲۴ مایلی بندر راشد امارات متحده عربی خبر داد.
براساس این گزارش، «کاپیتان یک نفتکش گزارش داده است کشتی‌ای را مشاهده کرده که در حالت لنگراندازی کج شده است، که احتمالا نشان‌دهنده ورود آب به داخل آن پس از حمله با یک پرتابه نامشخص است.»
@
VahidOOnLine
مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در ۲۸ مایل دریایی جنوب شرقی بندر فاو عراق با یک پرتابه ناشناس هدف قرار گرفته است.
بر اساس این گزارش، ناخدای نفتکش برخورد پرتابه با شناور را گزارش کرده است.
خدمه نفتکش در سلامت هستند و تاکنون هیچ پیامد زیست‌محیطی ناشی از این حمله گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78295" target="_blank">📅 16:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IIxtwtp8F30Mc3FBTOyttLYvZFnjAi_nNNo1lg1tGid4D1mL-Go7CS8M0aGLSW2vyUQlwSwFOpluGg74E_6UE6i3zZ9p2iihq0TnChMxBgYgNyv-wHtG9t_EDjD91y4zw1pz_KO317h3xKlGjPMidnSH9JfhF2lkMWUFBS-xroOIaVmyKioVDrQiq5Ls0ha7VgLcky60pyZM58Q50o48lUiEmnEoixiDJiHHXUwp1BQPHG5b-RxF2ES-eLlcmiKIf9RiYFrCXAyCnZwq4EpKnY_9vzekuqLaEr7fQFQaJc1Q9rjLHtnObISNTg0Gsl4kNvl8r2dOEMVrVEnb60HViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
🚫
ادعا:
نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که دو ناوشکن نیروی دریایی آمریکا را که در خاورمیانه در حال عملیات بودند، هدف قرار داده‌اند.
این ادعا کاملاً دروغ است.
✅
واقعیت:
هیچ ناو جنگی نیروی دریایی آمریکا هدف قرار نگرفته است؛ تمام حملات مورد تلاش سپاه پاسداران شکست خورده‌اند.
در همین حال، نیروهای آمریکایی تنها طی هفته گذشته موفق شده‌اند ۱۰ نفتکش ایرانی را منهدم کنند.
این شناورها بخشی از یک شبکه سایه چندمیلیارددلاری بودند که منابع مالی سپاه پاسداران را تأمین می‌کند و ایران قادر به دفاع از آن‌ها نیست.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78294" target="_blank">📅 16:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ql5P_Cd-Hm5AaF57bug-A7UVSEl1HINCPt2Ae-UP1BftKQJq3Lc1AeBY9bDOfde2MVlV2ucDsSjeYFtv9IvHB3546lEu3UeI7syRrSZe0qysh-MAzPEpHPKz9OfGPJx-KXZq7MxQ-oLGCWJFojfiaf6_YgXGZRmYlOW2vwaDnQPwdKZlguZSnNAb96L1wQTc1k6fG1Gn6W6rtmkHCFVs_VOWIFMrfZSsMAGc-4XAT-4LioA0v684PKYfIa7H3oGx83XjbgG2fUPJh1Ht-T-HtLfknk3IWjfVjUeK1Ft5kPnbgZ46tg7IM4g7qEJILISKAyxF1MUdnbdBicpsyPtUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ماموستا محمد نزهتی»، روحانی اهل سنت و امام جماعت منطقه چیانه در شهرستان پیرانشهر، در یک حمله مسلحانه کشته شد.
سپاه پاسداران او را از روحانیون همکار با بسیج معرفی کرده و مسئولیت کشته‌شدن نزهتی را متوجه آنچه «گروهک‌های تجزیه‌طلب کردی» و «صهیونیستی-آمریکایی» خوانده، کرده است.
براساس این بیانیه، نزهتی سابقه «همکاری طولانی» با «بسیج اساتید، طلاب و روحانیون» داشته است.
سپاه همچنین فعالیت‌های او را در راستای حمایت از جمهوری اسلامی و آنچه «وحدت شیعه و سنی» خوانده، توصیف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78293" target="_blank">📅 16:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=fJ8cUYvDiTFCTF44gdT3GONIHX7RPBgusIRA8X5joseCerdHWU94agB4YQxp_PZ3rFimXkms_MRguU5yK4g09SlSkluifZGvIyw8_weXsXM8g9cM-GpeGyF0prk4OpLCXAx3XtJQB8fPeY_iBptJ-GrhcdpRbtgn3NhNLfnc1G1ltrASGwU4VUk5wdHz6wsDZbOUAnvNY176ULAIgdc_1zlAOUJhi0m7cpD2myM-gi0HUsPZpLhB_lOPjBg8J9dve0YOx700TG8kEjl8-rWbVsSsbW1EtN0QFB3pbLG135As6_x-UNe0nV_7D35LmCmcT-nHoUjRSTuD_w1MkUxFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f95a9d62.mp4?token=fJ8cUYvDiTFCTF44gdT3GONIHX7RPBgusIRA8X5joseCerdHWU94agB4YQxp_PZ3rFimXkms_MRguU5yK4g09SlSkluifZGvIyw8_weXsXM8g9cM-GpeGyF0prk4OpLCXAx3XtJQB8fPeY_iBptJ-GrhcdpRbtgn3NhNLfnc1G1ltrASGwU4VUk5wdHz6wsDZbOUAnvNY176ULAIgdc_1zlAOUJhi0m7cpD2myM-gi0HUsPZpLhB_lOPjBg8J9dve0YOx700TG8kEjl8-rWbVsSsbW1EtN0QFB3pbLG135As6_x-UNe0nV_7D35LmCmcT-nHoUjRSTuD_w1MkUxFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مادر یسنا (فروغ) اسکندری در سوگ دخترش
یسنا اسکندری، وکیل دادگستری و نقاش، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در منطقه آریاشهر تهران هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78292" target="_blank">📅 16:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78291">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qnbhj8dix9cjCYrv_hsk7cia9BMC192TzGQWxyqWI-I8f2OlOCyK7IlUkKhO8ovkRvszQ_r6Luzq4pv4rJQ63LN4hUdloQFyMcUGEeYrty4lvkH7CjIK4Im8ce-JtvCcGKuOjM7WjiiC--9cEGI2_4fNB1P3M1XHs5s5N1hT0cjsDQ-z-HVBu3V1-U_p7S4nJs4VlgkVYf41Y5OUgzKRpT89Rc_DoMo1E07nPkOkPNnvQukGlU0nlG3hiyYDWrMgYrHTB8ukQ0fO9TTHEbCia06bWTcnbTlQZV8R4fzQB9SO9JKS4KZLZBydORyU17z0W0RKs7MkoCruz-mLVP4Wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران: دو شناور و هشت نفتکش را هدف قرار دادیم
سپاه پاسداران که در طول چند ساعت گذشته با انتشار چند اطلاعیه از حملات موشکی خود به مواضع آمریکا در اردن و بحرین خبر داده بود، در آخرین اطلاعیه مدعی شده است که در واکنش به حمله آمریکا به ۵ نفتکش ایران نیروی دریایی سپاه به «دو فروند شناور آمریکایی و هشت نفتکش» حمله کرده و «خسارت های زیادی» به آنها وارد کرده است.
در این اطلاعیه که بامداد چهارشنبه ۱۸ شهریور منتشر شده همچنین ادعا شده است که «۱۰ فروند کشتی متخلف که به گفته نیروی دریایی سپاه، قصد عبور از «منطقه ممنوعه و ناایمن تنگه هرمز» را داشتند حمله شده است.
این گزارش‌ها هنوز از سوی منابع مستقل تایید نشده است.
با این حال، سنتکام در اطلاعیه نیمه شب سه‌شنبه خود هدف قرار دادن ۵ نفتکش ایران را در واکنش به حمله به رزم‌ناوهای خود دانسته و گفته بود این ناوهای جنگی خسارت ندیده و در حال ادامه ماموریت‌های خود هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78291" target="_blank">📅 08:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=fdqwwEcvPpZsGUifxaKeRwTEJO-3uMzs-XnXS-2RVdzsN2MCxKApueXbVfQHSgoe8ShZoIX9ppdPszOIHp9_Qpq8z6Esa_NPPI8-afv3Iaf4hAcUjX-9JwE7ItFz6sQaeeXJe8lVyozHOeO66viYckGMEKcgL0txZEEkUXf7ykGdXhvg0C184mxOjRmrvlxKQVNomu199jIq2iBkapxpSrh0IkMnpPEBvdxydjStDbwIMYmtHgk7GsFRoTzxWaOqiTOUkp2EEFGfLG4YyvtAB4ercHnC9Q234gMBhRBNI-rMXjgYoedvAAE5aFxeeivwDq9G256nwVS0V0HAIUQDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e8057645e.mp4?token=fdqwwEcvPpZsGUifxaKeRwTEJO-3uMzs-XnXS-2RVdzsN2MCxKApueXbVfQHSgoe8ShZoIX9ppdPszOIHp9_Qpq8z6Esa_NPPI8-afv3Iaf4hAcUjX-9JwE7ItFz6sQaeeXJe8lVyozHOeO66viYckGMEKcgL0txZEEkUXf7ykGdXhvg0C184mxOjRmrvlxKQVNomu199jIq2iBkapxpSrh0IkMnpPEBvdxydjStDbwIMYmtHgk7GsFRoTzxWaOqiTOUkp2EEFGfLG4YyvtAB4ercHnC9Q234gMBhRBNI-rMXjgYoedvAAE5aFxeeivwDq9G256nwVS0V0HAIUQDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) با انتشار ویدیویی نوشت: نفتکش ریسکو روز سه‌شنبه، پس از آن‌که در واکنش به تلاش‌های سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی آمریکا توسط نیروهای سنتکام منهدم شد، در خلیج عمان غرق شد.
@
VahidOOnLine
M/T Riesco sinks in the Gulf of Oman, Sept. 8, after being destroyed by CENTCOM forces in response to attempted IRGC attacks on a U.S. Navy warship.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78290" target="_blank">📅 05:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 4.19 دقیقه صبح بندرکنگان الان صدای انفجار اومد
در و پنجره ها شدید لرزید
سلام صدای انفجار نزدیکای بندر دیر
صدای انفجار شدید.بندر دیر.
ساعت ۴/۲۰ بامداد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78289" target="_blank">📅 04:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/beWf_wI_RrKoZPe_KoDK4EJa-Hs1fai__ls2aQxnkzmYMe7Vqz3siq_mjnHP8wGP7aVFnvvUkHYILvGgkqAEzjy8-t2uWyYLN5APmQ_MIhlj7aVlhm4HdhR_Gb997qupBhVOoGDbgNiy1fZw69cPLzBoqhhCLuFLG0X0iJSgSagGYJcnF8WWLG6ctLI5vcg2d9TgcC26Ihk_54ZrslUSBHVo3SJtwHUWUBwog04fGMm4_gG5TPoqUpQbIDfJfgxabK4_ai8bFRQFMMtuiJZ_DwFO_hZHDnD6yfals2jGtilVmqyMQH06y02tOmZtOiWgiw2hOCxhSl81hLzKaXak_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای خطاب به «مردم مبعوث شده ایران اسلامی» اعلام کرد که با رمز «حیدر کرار» به پایگاه الازرق اردن حمله کرده است.
در این بیانیه آمده که به محل استقرار جنگنده‌ها حمله شده است.
پیش‌تر اسکای‌نیوز از رهگیری موشک‌ها در آسمان اردن خبر داده بود.
تلویزیون دولتی سوریه نیز گزارش داد که پدافند هوایی سوریه برخی موشک‌ها را که از ایران شلیک شده بودند بر فراز شهر مرزی اربد در اردن رهگیری کرده است.
برخی رسانه‌ها در ایران از جمله همشهری نیز گفته‌اند که سپاه با «موشک‌های خوشه‌ای» به اردن حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78288" target="_blank">📅 02:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=Z9BQaJ37n3Qfaa22pnfycv0gZhfw81sjIZzf7FFj2C5Pmf-wQqoXxM8Vc81sAmHtNaIAlo4NHuZtWelJhOtzx-7m4uUOOQj3hM4NC9ay-ZR55cOga664ldVnsY6TosWiBuCz7hmVunLjWtzDG_6tbWH-_0iJaA8Gvdlo2J1-q0VQNkeuaD-0IjZtFtdYbRziqJHok4SOlZQbuk52AYOYaLLnpYScnHP3tQ6DJ44830abggogG-AZCDYnK1b0YeWx6_b7gQ2b8Zt5BfuVX8UpLec1bHciJYDtBfX9vJHAIpzOlj2qmW22CiQQIe_w7RgOXAFydfAbNu2rjsZjWKFhAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d875f49ad.mp4?token=Z9BQaJ37n3Qfaa22pnfycv0gZhfw81sjIZzf7FFj2C5Pmf-wQqoXxM8Vc81sAmHtNaIAlo4NHuZtWelJhOtzx-7m4uUOOQj3hM4NC9ay-ZR55cOga664ldVnsY6TosWiBuCz7hmVunLjWtzDG_6tbWH-_0iJaA8Gvdlo2J1-q0VQNkeuaD-0IjZtFtdYbRziqJHok4SOlZQbuk52AYOYaLLnpYScnHP3tQ6DJ44830abggogG-AZCDYnK1b0YeWx6_b7gQ2b8Zt5BfuVX8UpLec1bHciJYDtBfX9vJHAIpzOlj2qmW22CiQQIe_w7RgOXAFydfAbNu2rjsZjWKFhAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین
خبرنگار:
آقای وزیر، بخش زیادی از توجه افکار عمومی آمریکا معطوف به آخرین تحولات در ایران است. می‌توانید درباره حملات آمریکا به نفتکش‌های ایرانی صحبت کنید و توضیح دهید که این رفت‌وبرگشت اقدامات در ۲۴ ساعت گذشته چگونه بوده است؟
مارکو روبیو:
بله، این رفت‌وبرگشت کاملاً روشن است: ایران همچنان تلاش می‌کند کشتی‌های نیروی دریایی آمریکا را هدف قرار دهد و هر بار که این کار را انجام دهند یا تلاش کنند انجامش دهند، نفتکش از دست خواهند داد. فکر می‌کنم امروز هم دوباره شاهد این موضوع خواهید بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78287" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b638672d55.mp4?token=K_wz3d0z5VvYyWC58T98fzT5Cx7Y8E5Ri-d4reVvs-JyyHHTZnhojygUwrQAJxNzy_HOUQ3-nfburWwSpWAHTbouZFrJziV_FLLgJNEZg--W2pRKHdm8xpC8YIhiRuH-kezfdJtRf-V_Dj0btsCQCAJz8xf1HCSj9Qs4tRWuHawt_Dat6bbIsLvS_Zmac5hEu0pQ-wyDdg1szS-nlD7Fllx0mNZZDrfKyecQK-by0206w-bc2qCImZeih_JuXwbVqlw0c0k2wfkTcAOjodZd3BXGNLZFa1GaSwBnFwq1YWu5niRXKVWnuxHlAO0WbvuBXtdfhgkeNlXm9ebhiGH4og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b638672d55.mp4?token=K_wz3d0z5VvYyWC58T98fzT5Cx7Y8E5Ri-d4reVvs-JyyHHTZnhojygUwrQAJxNzy_HOUQ3-nfburWwSpWAHTbouZFrJziV_FLLgJNEZg--W2pRKHdm8xpC8YIhiRuH-kezfdJtRf-V_Dj0btsCQCAJz8xf1HCSj9Qs4tRWuHawt_Dat6bbIsLvS_Zmac5hEu0pQ-wyDdg1szS-nlD7Fllx0mNZZDrfKyecQK-by0206w-bc2qCImZeih_JuXwbVqlw0c0k2wfkTcAOjodZd3BXGNLZFa1GaSwBnFwq1YWu5niRXKVWnuxHlAO0WbvuBXtdfhgkeNlXm9ebhiGH4og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: "
آمریکا ۵ نفتکش سپاه پاسداران را پس از هدف قرار گرفتن یک ناو جنگی دیگر آمریکایی توسط ایران منهدم کرد"
"U.S. Destroys 5 IRGC Tankers After Iran Targets Another American Warship"
ترجمه ماشین:
تمپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) روز ۸ سپتامبر پنج نفتکش حامل نفت خام ایران را منهدم کردند؛
این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی (IRGC) طی دو روز گذشته، دو بار یک ناو جنگی نیروی دریایی آمریکا را با موشک‌های بالستیک هدف قرار داد.
ناو جنگی آمریکا با موفقیت از حملات ایران اجتناب کرد و به گشت‌زنی در آب‌های منطقه ادامه داد. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
در پاسخ به تازه‌ترین حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران
M/T Kaviz، M/T Charminar، M/T Horizon 1 و M/T Riesco
را در
دریای عمان
و همچنین نفتکش
M/T Derya
را در نزدیکی
جزیره خارک
منهدم کرد. نیروهای آمریکایی پیش از حمله به کشتی‌ها و از کار انداختن آن‌ها، به خدمه دستور دادند کشتی‌ها را ترک کنند.
ایران از این نفتکش‌ها به‌عنوان بخشی از یک شبکه چندمیلیارددلاری پنهانی استفاده کرده که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ وسیله‌ای برای دفاع از این شناورها ندارد.
در ۵ سپتامبر نیز نیروهای سنتکام سه نفتکش حامل نفت خام ایران را پس از آن منهدم کردند که سپاه پاسداران تلاش کرد به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌شونده آمریکا حمله کند. تمامی تلاش‌های سپاه پاسداران برای حمله به ناوهای جنگی نیروی دریایی آمریکا ناکام مانده است.
centcom
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78286" target="_blank">📅 01:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=pseYGrD3n_u2C6RWogKITvJq-4QSpZZN7vjyOx2HuvKiAtjgYXkcDmL4iqkWmAg9hixQ0l2ditH7AJvRt0UGvsRTOJRjFov0bKIM8MgYryMJgJst2OeVhg8K7ZMBhHBIyDLQDioxjpIlQIZyOv40RNpWvbZ_YpZRH1z4T87aJH7eT7Q5UTYSZ6F0PHZlLiUlNbH1Ofp9xSX-eo5yljZrzDGsGT2smj-gP9mCWB5ql65C1gkTxsoJuKedJydGYFg1PFU2-Gp2TvmhKIbuRDgVMrADJemTI_xVwFm3278hkpkThilWOWtCEBrW4nbejV5Jk28rBcFuQsfE5rUf4DFSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc7356e9f5.mp4?token=pseYGrD3n_u2C6RWogKITvJq-4QSpZZN7vjyOx2HuvKiAtjgYXkcDmL4iqkWmAg9hixQ0l2ditH7AJvRt0UGvsRTOJRjFov0bKIM8MgYryMJgJst2OeVhg8K7ZMBhHBIyDLQDioxjpIlQIZyOv40RNpWvbZ_YpZRH1z4T87aJH7eT7Q5UTYSZ6F0PHZlLiUlNbH1Ofp9xSX-eo5yljZrzDGsGT2smj-gP9mCWB5ql65C1gkTxsoJuKedJydGYFg1PFU2-Gp2TvmhKIbuRDgVMrADJemTI_xVwFm3278hkpkThilWOWtCEBrW4nbejV5Jk28rBcFuQsfE5rUf4DFSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا بر ده‌ها پیام‌های دریافتی از صفهان، یزد، خرم‌آباد، خمین و شهرهای دیگر چندین موشک پرتاب شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78285" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UAZnKNw6QBxgKcua6-Xjfw_s2OjXVlNcRrNMBncE_zXKJN1ENZ2CRshq8YsJS1isfUOjHrpoW2WDAReUmo8GYck91za1GgPOXfDasAq1AIgHYoeiDEV_C3YKU6JtWD7bRXW6Rv8yBdc5rqESarL4ou6kq2WwvZsavpq6ebOnZ7-uWv1hS91Xo6N2VdrSS6YaXFJzjRtkiBLxzaWbD_8YsQGHhXjz4ZhM4jP-vGLzdu0fnfVXuZ1JqrV_s3A7haiFzTAgEAjliQM4zwV5VM_g0QRrMXYA9VBWTOGt0S21JRt2CKgrHpXjGEXgMkWzwPcCp1hbKym8mikikN8YQJwE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی گزارش‌ها از حمله ارتش آمریکا به اهدافی در جاسک و اطراف جزیره خارک، رسانه‌های حکومتی در ایران تائید کردند که یک نفتکش دیگر نیز در اطراف جاسک هدف قرار گرفت و خدمه آن با قایق نجات در حال انتقال به مناطق ساحلی هستند.
پیشتر رسانه‌های حکومتی در ایران گفته بودند یک نفتکش در اطراف خارک هدف قرار گرفت.
رسانه‌های اسرائيلی و آمریکایی به نقل از مقامات آمریکایی گزارش داده بودند که علاوه بر اهداف دیگر، چند نفتکش ایرانی نیز هدف نیروهای آمریکایی قرار گرفته‌‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78284" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ib-ih0cM-RNcDTVFlVp-dSJPECAUnSpeI4Zy0VxqLqro62Rc2wiXFHGUJokr2oOUI3JoSHYaF32v7lrK0Q1Il12a6DY5vEX6sImVW9NZ_1mmdB6OSIGSvCmAglhoJ2vAoQWsPh4HPB3xtqo_fvpI_IjzaMupN9e-6N_2FU178E1CaGs2xOZCoKdU8kys2puLcOquotxaOs_wcVeB6tR_Lnkg-ud2E4rLBSVeqBbn7wxPKsVRCvAo8T0lEsoz4qTlS7vhttUMvI4OkyMEyV_S90fcDF7UtxGRHmm0G8LIqOLplM1lSegeAOfyVbiTo1tkFeOoja7icw3p3jImDkntVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سپاه به خدمه نفت‌کش‌ها در کویت و بحرین: شناورهای خود را ترک کنید
سپاه پاسداران انقلاب اسلامی هشدار داد که نفتکش‌های مستقر در لنگرگاه‌ها و اسکله‌های بحرین و کویت را هدف قرار خواهد داد.
در این بیانیه که در رسانه‌های جمهوری اسلامی بازتاب یافت، اشاره شده که آمریکا به «چند نفتکش ایرانی» حمله کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78283" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WVasJWOVDEe4Rd5h5vu2XBTXBFcbgyoHUaVafnjKScHi4FXjv51zdqebY_-M3uQJYgcVmvjgql5JMNUrSSI26dTHDQRWw4SjYJaOE47-lInzSMURpRr2Fup1QWFY13vO5TWMK7jRbp7Z4wqqr_xNfbu07VerLv7Rtr05LxXIC-MrSkk5X_zzoX-Nag0FA4RMQ6l2RuJFnYVn0GKMRBH1keA8UVqBCRcuOyFtTMtVVggDw_Emzep53k9xr3ZNA6aXx0i7D0dcMjtRHgAK63_6dBY_QWhWQ2_4xrstTMu2hX26_yUKpeRafgIFpyALwLeHQvEKQEbw3QUiWxsfFHNXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز: ارتش آمریکا نفتکش‌های ایرانی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است
شبکه فاکس‌نیوز شامگاه سه‌شنبه ۱۷ شهریور به نقل از مقام‌های ارشد آمریکایی گزارش داد ارتش آمریکا اهدافی را در نزدیکی جزیره خارک و جاسک هدف قرار داده است که شامل نفتکش‌های ایرانی می‌شوند.
فاکس‌نیوز به نقل از این مقام‌ها گزارش داد، این حملات بخشی از تلاش گسترده‌تر آمریکا برای افزایش فشار اقتصادی بر ایران است.
مقام‌های ارشد آمریکایی افزودند این راهبرد شامل غرق کردن و از کار انداختن نفتکش‌های حامل نفت خام ایران می‌شود.
@
VahidOnLive
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، گزارش داد که یک نفتکش کوچک ایرانی در فاصله ۴ مایلی جزیره خارک، هدف حمله موشکی ارتش آمریکا قرار گرفت.
تسنیم نوشت که این نفتکش در محدوده لنگرگاه جزیره خارک مورد اصابت پرتابه نیروهای آمریکایی قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78282" target="_blank">📅 22:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-bH2GjXru-w4oLOf1bWt7TPFgGcDgH0LKajfDYVoxQN84MrOyDuaKNdVWCSiGuzDqOEiTQeKMnZGr4Nvhcm4Zzz_QA6UgoE6LBc7ZcF3wTSN192csGvBhrweUN-NsLpBHhDtw_M4d0J1F3RMWYILigDa_TSYuEekUAZgvWuxS7KKqVBWD73YLoq5n80f0rF5AHGy746gX1j3e3Fw9nRC5E7_pzUf1pXRPjPgsizJOYODTZyKXGcACWBxO8hbcS9uoKub8ONBJEbI_hMnlHTDfrb0VdyLPPa26vW6FWbTEImvJF_F6_b-7txubAN_YhpXTqTD14wHnP-cLIasHpkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، روز سه‌شنبه ۱۷ شهریور اعلام کرد ارتش آمریکا به سه نفتکش ایرانی اخطار تخلیه داده و آن‌ها را به هدف قرار دادن تهدید کرده است.
عبداللهی هشدار داد هرگونه حمله به نفتکش‌های ایران با واکنش نیروهای مسلح جمهوری اسلامی ایران همراه خواهد شد و پایگاه‌ها و منافع آمریکا در منطقه هدف قرار خواهند گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78281" target="_blank">📅 22:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">"صدای انفجار از حوالی ساحل جاسک"
خبرگزاری فارس وابسته به سپاه پاسداران:
حوالی ساعت ۲۱:۴۵ امشب، صدای انفجار در شهرستان جاسک شنیده شد.
منابع محلی می‌گویند صدا از سمت دریا و نزدیکی منطقه سنگ سیاه به گوش رسیده و انفجار در دو مرحله و با فاصله کوتاه رخ داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78280" target="_blank">📅 22:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isXmUMNTItvR2DyrDca7qC3CSXCeT_m2PI-VP3l82mPyHEMu3wrb_spJUCljkwbXiX6kkBgQwzFw_sOTQkiOIvM6w4BnENZ7PIGBrmqu3rljype8kmzTbzYzz_jl46h1YASifKwYewg9bm16nDQkYy0u1jT9QOhrwID9MJW7QJs-7b-aJgxKB60-a0tKonL6FQC3tzZRKjGLNAW810gfzQFXze-Lym0UsfekRSDSfE4-yGkGf5hCcq_8nGOwMm0Mbag0hPoFZThaBcjGNIF_rTMR922Rx08Pvaw7ZCbeXP-mVDXK5Tf3B4hbMKOLTyuYngRs1Zkr2QwoRqTzHnDD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی روز سه‌شنبه ۱۷ شهریور به رویترز گفت یک شناور بدون سرنشین زیرسطحی نظامی آمریکا در خاورمیانه، هنگام پایش آب‌های منطقه در حمایت از جنگ علیه ایران، دچار نقص فنی شده است.
این اظهارنظر ساعاتی بعد از آن منتشر شده که سپاه پاسداران انقلاب اسلامی از «شکار» و به «غنیمت گرفتن» یک شناور زیرسطحی آمریکایی در تنگه هرمز خبر داد.
مقام آمریکایی که به شرط ناشناس ماندن صحبت می‌کرد، گفت این شناور معیوب از «مدل قدیمی‌تر» بوده و هیچ‌گونه تجهیزات سونار یا رادار طبقه‌بندی‌شده حمل نمی‌کرد.
او افزود این شناور بیش از یک روز پیش دچار نقص فنی شده است اما به سرنوشت آن و یا کنترل نیروهای نظامی ایران بر آن اشاره نکرد.
در بیانیه نیروی دریایی سپاه پاسداران ادعا شده که «یکی از مدرن‌ترین زیر دریایی‌های هوشمند و بدون سرنشین» ارتش آمریکا در بامداد روز سه‌شنبه به دام افتاده است.
پیش از این گزارش‌هایی درباره مین‌روبی آب‌های تنگه هرمز توسط ارتش آمریکا با استفاده از تجهیزاتی مانند شناورهای زیر آبی بدون سرنشین منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78279" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcB5F3di7MdFc6NRy-IdSl7rlWKUrkZt5jm8J5HTtX8W-SKEUZ-ALT0_mrJG9Ge-3L13FwRNTTmr5kZRY5kyG2jUFg8CBbo02M8Olm6yI9wq5wBgJYx5Uvt7n7w5EvbBuJ0QaFvqSt_gHH5mhUj1oJnpmjJ69grRHEEMNDec-FM4O_QW-OKwKCmV9bw5WfK6QytwQ3uhPt_Nr6fuSpwfboNrDGUnpeXABX8sh-CVBJ_uw-4qmqn60r4YX6ECi3lwWarI1-EkRBHB3ju8Dv9TrEY1wltgBI2lQNAlun4NNRKeldSgTJjj5j9QsDg9z5-1p19LCRfdwyfeN15yec-aiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای دولتی یمن روز سه‌شنبه ۱۷ شهریور خبر دادند یکی از فرماندهان ارشد حوثی‌ها را در جریان یک درگیری در استان تعز به اسارت گرفته‌اند.
منابع نظامی، این فرماندۀ حوثی را ابوعلی الاجنی، رئیس سازمان اطلاعات و شناسایی انصارالله، معرفی کرده‌اند که در یک درگیری سنگین در تعز در جنوب غربی یمن به اسارت درآمده است.
این چهرۀ مهم حوثی‌ها، که با وجود جایگاه نظامی‌اش در کادر رهبری حوثی‌ها جا ندارد، به همراه ۹ تن دیگر بازداشت شده است.
درگیری‌های سنگین در تعز از پنجشنبۀ گذشته در جریان بوده و تلفات زیادی به جا گذاشته است.
در همین حال مارکو روبیو وزیر خارجۀ آمریکا هم با اشاره به نقش نیابتی حوثی‌ها در قبال جمهوری اسلامی، گفت معتقد است که «دست ایران پشت بسیاری از حملات حوثی‌ها به عربستان سعودی مخفی است».
وزیر خارجۀ آمریکا با تأکید بر روابط دفاعی کشورش با عربستان سعودی، گفت واشینگتن تحولات یمن را از نزدیک زیر نظر دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78278" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6gsKcEpUT-id4A85F1Hsx5rQaD2JMFDmpCRZ0IOzlYe2ETFGUVIH00CpSDLHfvpFuu212aWQUdAmK-MH46nOmZbB4eQlb0XwJUmC9kkjybFOnuKXKNrW7E0UUBwZGQWrbq-7kY4m0hX5yz7a4Dtn7JaW5n4ch7JeG1ifsHDTTTy3XvDHt3cpHwYPIkyb_cM34GHX2NdyU416apyLcUmdqNcqC4BDf8CPyQcw8Vt0233H4sTRmcmIIp0W8vN1tfMvsqtahbcrsdK-jyXPT_I07Bgnzqs1oTYFK_mAiagdKYjFXFplqeod6oYTUzCVy9ARztb5xNPl7vnHnqYrX6xFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h2lmaOl15K4XYx31ElJcY-jXGdk_7EfvM70Ht-98RbdKBb7P8Z4OW-LNf276qX7-yvlVjEFXihRb6M_oqwMykr19way5KX6JrthgNa6tf7ZfGB6g1LbTkKFyQf-SLugvD0Vz9FN56J3nI3EAmJPwd05ejKe2vTDfv6iRtzmnctWtsu-ViUpBlTwMC-h0Q75yfhDmT2L0saW-naHxpA8cvO3L6T45M2Qbsj3zKjGKZ5kJlyDgtWTkKOmBnGkcLpfNCl4VyxxIzfU9Z6sO7oOho0iy3xVnozCu_nRkjOikUmCvZbKpPMIwN0hH0VwLh5LjUQGbkK7aId4LrPyH8k947A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hi6TISmBU0R8AeXhoXrEEkaAjr-3ZFn25Yb8UPq9aawEyxsJV1Q6w9jpfQ0aLYsGU8jwC1b-M-7Fj7ZFHBfiAze-O8qjB3teR6lMfC-Z-VwWBlVyYFwqUx-z_5U-hHi0xv48mxcBSFnwJKD5AmVxpeMipGiN5FArEBGDlB7DHL6hgQz897KCv4wJWhENaNqyLdfv_aeo8ooHqNUyz7eGZjOy5KnxdvucMvpG6QtQYDrEN5x7gqt1G5f_6_g0T7j5EKFuhNlMwTrj0zPGRqcVhCcJAULa0aEt-lh9WKGLkmkk_iUHQ5MwUtozla98Yrbpg7MMYiZGcQh5BwqUEBM5oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx46EP0tUuJrZd7nfFgws3rhwJ88QYDRSMjK0RVG_BogwzMuCNxWf8Ho8vFt-xGO0fNcL_Sg-fqycIqh_2mcgOaqzg1NzWreKLoJQTa-Dy4HkxEnU9JkKbRumP0-gjMvsXRvm6PmwERasqnN5twXo8UL8c77c4M05IaF1vhqE0HAYQw-pmjyQuyK-nsYnX3USHxtroMc4kxmRoXe332TUEqj66kUsndjf3EGW0LmiMB1PRZBnPvRQrjZLF6-exSh4z_B93DIL8NFCRsYtFGLm1WRgRbnRYuykK1k7M0LmB0BmehffoCnKwblxvf12vluiRUZPKDrM4Q7v07dskhDkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kEKGp7_yWbc310R9KGpSrThe7JCWxOLnNJ9nAACy4AETZwU1MACJ4LBBJP1OZuAAeusSZMEvIScs23YpBkAF95zmoY3nuj6E-1WNm_NhsSWxzzcQzYVphpwes5DWm2Ccd9RwoBJ9twPkOiyTRPBGGb1qrQtFFLmubmFxXop8vvK1DiJVDt2OBsNiUB7sde6i0yRCz01bx726OIhn7792Rtuxhh18_aFvpCw_R_KCVgE1U5QKqxt0Pd_SzhHDuYEuq5oY6k44P4BpVJnK4i9JHApc9JbTlE7fI5LFWC52UdnOFELWFUK9XLRKwqwUg7iFdO4fPNZdmC4CL8txsxWaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eqD0oddaMm0uLpObDSpM7xyeZPxG0AAZYUfm7Xol9_kprWM-tJ-KlWgIKCdHi5rR1rYdRn7lJlAzC57vQFAb5ipsDrlhZIedTu2AegzglKysF_XEigbtNRoyMgP3dYsOMhNsb6QP-vsBvMG1wYQ5vgksq9mhCcrCSzt2sTBM7V7GxGfhnTLBvIo2Y5jObisJ8RlxBGMSxf5hzPIxjlgoUJJEajumpbfekU_dn73MX72TMebTAiAw59ltEWkZKVEMm5Opg4nl3Hu6dTp_JB4VSUUmxKTQ7b98vp3XTxNWBr5_2fLxjpYdUDn3v0AiLlUCsDwGYBNhoXIDZ6oCRtxSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GnWYg3FSC-ZPJTAgrOvSx2mWr1nnQH9xc_kM4XfCLeiBxvRl2DnKeIFao_zj9eB9ZbusKrdRlFjbODoau7R4_mkqa7c4SSGP43lGIpMZDeqfsK97zcTD7Di35q3qhblWZZO9-7e302oBWlgXJl2QLYukndN6w6fmOaB8GpYCARSzojgDtGhktTKqo3BPKoGKFxxQB3cw4zplokTrHYA20Gg28pQQ0OmqtMSTyr5mQCOiAVDwGSiqfxntBdEsM87xc0OLR-TcEDiJXR8_2uDa_Z_BjsgywmIvLUQqAENRX-vgr4eLqFsPphPdhWErtw_6j089FS8HpXJBRID_kKPlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hw4-7owFkyxuZxfezXIVoX2bw7FMGPhBro9gdJ8zysZRe8EG6iFm582-6p8at5nt-7V0DgoTGLKJrTWmFnn9GG_3GaQ1YjOB0tptkzqJBrWdQtR_v8VdhVQq2VPmSIWRoVDns2mW6-yOi1xsxTe2RSWZILyg19NbCrQY3CV28xBQWHbW97HxJyBv7BltJjVPTRwNFjVWw11ZSzLWNfX6ISA4XmL9hK7am1fUTXJPuXEZWyDX7nyOvZ4SgR-i4fI98_bgDLXie-MVbs_AxUzWSel7yhEe0gIvvX0hAmETqFNDD7jfQy1ToymQkCsq0eJdtrFDTk82eLXrYrWgp-2xrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ehrv7pxWdNJHCB0YuOyp2t96YcrhSzeN8wciZGT0_-Llc9Qqnr0aHQ1aBPUPDa_7O1L1dISaOy8cnZaoi8hK0HbsD0mDsxtYr6pYatBwbz9bgqBhnljpZrD5o_PM2nwfIxkwDGEZkeTFbTbuNSfjhp7t40TgiK-bh3psnxJYOWVgPkyrI4QwZlFF6q6ufaU77fGpJCT8Pmy5qEKJtBffTf2mOf3cAD118tZkk6jw_ub0jdTzH2LsVLqd1RdkR_PJRGttASo3ii1jHANlkDw_5CLytqYOJUMX-4iBpSRQ11calltrBzpKfNUPJQS3f9Ft22GnqVLYUpRYBUTCaiTXUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=i4bL4S34GoN2MAGdkfVN6WDjAsI6dDaINJArMgM0PuP4yvzrBWtzFt63qsaVD-9Ws0-7EDOS15FNImXyIKvpU26GauocwbS5Sy4bJ2-XENWxxwEcXyJA4IQdBZjBydW3wHAa8OKY4p03GiZ9azIqiK1B5K1HKsAhCJ9NZuW4OGPAhrjv_uKaUXnbHCHRt7RiD1S-p6_FwxJSZcbUme2ne-t6-paAE7ZnYG-k6J99Gq_WrQJKUucooW6BEC35tgB8X7qGs2vdBoXpUrKJySqWxyt_pA_EByE55yo9umeIEQ8Rlg3ClwLFTvtKguaxwv_snWPusb2BiYRCW09DXE5QRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=i4bL4S34GoN2MAGdkfVN6WDjAsI6dDaINJArMgM0PuP4yvzrBWtzFt63qsaVD-9Ws0-7EDOS15FNImXyIKvpU26GauocwbS5Sy4bJ2-XENWxxwEcXyJA4IQdBZjBydW3wHAa8OKY4p03GiZ9azIqiK1B5K1HKsAhCJ9NZuW4OGPAhrjv_uKaUXnbHCHRt7RiD1S-p6_FwxJSZcbUme2ne-t6-paAE7ZnYG-k6J99Gq_WrQJKUucooW6BEC35tgB8X7qGs2vdBoXpUrKJySqWxyt_pA_EByE55yo9umeIEQ8Rlg3ClwLFTvtKguaxwv_snWPusb2BiYRCW09DXE5QRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjpSViQG5C4TdLZ3uEZRFvimgYf_Ia3pVukECGhmdFIfYCidSfWy8Xe8JxfVVIk4ssvmYTSxKwdNYyEVhzzkCMbSI7VLvKNp5arGsNNp7aewDXmS0jnokBFbayYhZdlGIamsUKEIKr5qddE9Oyfy01HkiFFAyo2-5VI8kyUDtzCEyL-XRdbO17Ow5722S5I_FLCcbudmRqxHQQKbX6TOk_QQGOBDeRR2VJDy0bcCCtymGVlhoQQuSrqq4KpcISYu8m1ZXJ189ATIP4T29MoFdEX2INPnGrSNj3JsPQwVa2SlMe5pQ3ezBAszHR_TIgvt0wv7RF7NQWwd27MoJK32yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlXS_xILt_OEcbe9ePVu7NBr9l7pscAGIaN2dP8ooqGrDESq1EgPX0roc3O0KGhoNUo9mINrGqr_lMeu9IMGhET9wiJtWWMoAu9QdBeL-g5Si3Od7Vm1LtG5FT-JpAKUV7QZNgbCEGcJ2lYosbO4zaKRvFGcIR6OXRzRBL5sYVhx1wn7iv5YYvEdjuZOWyqtg07StiXUmQgXH8png-x-IyhmxhJKcAYryQEGSYgINNM55Df1ym_LSha_7QVrLuZZkRHfgo20UvqbS9-iYLQdQEPir5KcW7mSRufeyRWU-9EnFuf-NXJ94CTjz_papJq88bgbZ-EBtUS1uDzOGzIRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=caDCYg3_74rnFbz6GQeuKU9iYaEnrNcy523XED4T0EwsIJJktzJiN1U7FMpMOq-tCC2WNSGVQLHUwGz_hbrLUpkOtMi7zBakMnavXT6X-HMcJ7MfcSturjggZw1IYjP5J5rxjJfieFEspudrvHrHYYPjIN88HFo7NJka0Oei5yYFnfeeEZ7c0HPqUNsBjn4rbSA3kJho3SYwrUhGDX_pBGmYqRnWeWOI9vtn-wYlIHpEgJ3I_KiJ7In_wSKPlfa0M6_UPWvIgP7YtBYefwRw8nUbLM4Fv9902EV3jdOVTIMuRphJ_mbUfs7QKDj9x6nHvpyurbA02JBxCF4ZFnQ8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=caDCYg3_74rnFbz6GQeuKU9iYaEnrNcy523XED4T0EwsIJJktzJiN1U7FMpMOq-tCC2WNSGVQLHUwGz_hbrLUpkOtMi7zBakMnavXT6X-HMcJ7MfcSturjggZw1IYjP5J5rxjJfieFEspudrvHrHYYPjIN88HFo7NJka0Oei5yYFnfeeEZ7c0HPqUNsBjn4rbSA3kJho3SYwrUhGDX_pBGmYqRnWeWOI9vtn-wYlIHpEgJ3I_KiJ7In_wSKPlfa0M6_UPWvIgP7YtBYefwRw8nUbLM4Fv9902EV3jdOVTIMuRphJ_mbUfs7QKDj9x6nHvpyurbA02JBxCF4ZFnQ8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u72V3SvJWnW-5m6dEFuh6L1JgeZYz3EeqNNqqXVExpEdajSyOV05ismt1fgwQE_7vlVA7j0aRzFTfWXJeJj7hECfkfaVztGLcOU0H2y9bvlizI0cLtiLDmIY8IB9SqAPNEVhS9Oa4al_JkOhVOBVwFjZaO33WyQWWN5scSDOEqctxWwqOTfiwZZnrgJy7lSJ2BxTdA78R3xG2IH9Om1z4OulPBsxS0ZMT3yBQ8ehG9up0FfpJuGPSneXEI4NR5ZqlrnSkmA3wFJz1a4emo-tgMkFIIA_Le0W-GFICFwoEMGFaQ8Mj_dXBLjjvOZzUAZpVe3P4fZLgrQz6EVpiiHx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_zocYdfqcvnnDpfc1Basm_YGHEdE3vUu5iEZplUCrk3151iwFaFq8IE9Fc3tBZJqWC3_-sm1vjBzy8_cKPONWoL06mU0ps4QQRXwzhzalpUf2r_0zIwD4m6ZJrxp_-zgd3glZkDLJ0XS1joCONCjMFxO87GBCHz4BBsIKhw_dKcxUbkCtCTWMkP209r8MOAOVbMhNI14zYnLqEByVNugCy6jpNeud2sJYtVIpJw7HnUHptVE2jpOu2RIOiuMucuFTQQZ4I2Gck-P3R_--LUharExHUSJOd1_sitrtQ27ABqH0iBmKMHb5fL5VVd4Fg1GB644Es5rBujUIM3LAzwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lo4LBECPnAcEqIwUBL3aUoqTA1IDPiLNV733LsvwDb3BTX79-hTAJ0-N9m0hphst94gf4-O4mO8KZ9IfCzUJITuvIiywMvXYlROBB4ZjkxJMlE20vSCLTard1p6JxDjLi356GFacW0w0Z6G0CUnKRINtWYeKYUn_unR9JgCuxRJspo3pk97FZU2EtzTdnSMUyz09xrWTuXELVz3HaD9wG9lSOGSMZ1bKHw42MePB7gB40Wus8HKNEzM7511iJ4vlewb1hWDuMk2N-dgCVZBVSBLTx25M7QOxjgXcVEWI4oWDuv3AudHGcOb5r-zKAC_JRCNWsFJ6LJ9AmS-MqF_bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cep1xJk9S-MGJqT5BNvcSWoutsV0g32-tGXsqMVTRtKobYBXCbfJ3xt1Ddi7gQyOf08omDW694vEj-QReMSuSQksPK0j5YSV3ALDTl3n7mS7_pe9HtQfCuQwWFHPluJPC7FAUsx4SdhRLXwktd6KMBW8QjeRUA0VIIoWg6YbyJCwG9zkqsx6QG-OYKSWoARiWon_mul0oexDXtBMrfdQjqU1FSas0UsvuW3yG0PNkcHDRMes6xpvRjDWENW2NLsx-EGVzcVjtrzi9acoxmylVg1Zr2CnFtOWSWHZW4lgeSpYNcqzNjGzWJHGGxR6Mdv0Zfm5z-lN7gZO4EaO1MY2KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=awRgKTBw9mvZ4uVTbkOArUYt_rnexbA52dqUBfk072YsCLRuubGqZ77A678kUOabnmyNh6IHyvNW8ZxT0SgnVcZa80PrLnmmWduMalY0ZesHsc1ZIEnhr8s7NIGeR2rqLV6Hatke49UQl1VhYHdBnO4DvHlL2bu1NfOLtJPZKRWoP94XCmEe1wF9R1ReUCPWx8Dyuh1A8Ydl-VhSHfXTyExktRgEtKO6VlSSG-DAA5y60peLR6h6rEBxugGR-PEVCsluPZ97u4m_rOCH8LLN0phzXepjideVxLdBOoMijVpzBhzDYAJYjrx1Ho5bS20P5iJUcDQ1twa3Ux--iWhSwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=awRgKTBw9mvZ4uVTbkOArUYt_rnexbA52dqUBfk072YsCLRuubGqZ77A678kUOabnmyNh6IHyvNW8ZxT0SgnVcZa80PrLnmmWduMalY0ZesHsc1ZIEnhr8s7NIGeR2rqLV6Hatke49UQl1VhYHdBnO4DvHlL2bu1NfOLtJPZKRWoP94XCmEe1wF9R1ReUCPWx8Dyuh1A8Ydl-VhSHfXTyExktRgEtKO6VlSSG-DAA5y60peLR6h6rEBxugGR-PEVCsluPZ97u4m_rOCH8LLN0phzXepjideVxLdBOoMijVpzBhzDYAJYjrx1Ho5bS20P5iJUcDQ1twa3Ux--iWhSwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iM7XndUVdiYsIn5SiI_SHRToIOehGacAI4C3gffSiaI3q9fX0s9KGmTRVRND7p-VvjVM2rn0r9Z2WbK73cB7XSguOry8DqQxqkOiVsRSZgOC-_iXch-tgtoaJTIFwQOLitY0rmhSHYHhL6TNDNjhX_WOJ7aNk6dJN76B__4ucdCEPEZ3sTKLa7AHUKV9gk126L55MFyt5MQ24evM2AJK-yc7P8unu6fgLBv-EnZwIps9LGPATBIKjrcSDDEZmpkMHsqVzAi7IIkGxRhcKjhcpczPzgRm-ZlQSKGA5ZXULc957s582mpjqm8UyjxEeq25O3KH3ZkpQzugkFzzEaREmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=GxnET7hZAi_35kYHcQ32xPolmfG_DKe4Ru5X353Q9DR6qLmw9VXaQTYEkiShlt_Mdc_m6Oir1YQodI-YNN3NW47UDr-jIp2Fa6kw2MvFMm_KRiv7-zcrBMKOeaRdwJeN1TmXm6cJoPwLztD6DKEz5MmbB5tbGVIBrKaZBvhw_FDUK6gljze9pVkTBoUlPz7C6u4ta4PBTmachhQKYXNXu1umZz-hME5E2yi3h-afRZKxv7LrAbFuyFpFCbkv5-PISlviZKG19jsqTUdT0bvUGJfa1gWHddQX6HzQ1f4rY4GbdRPeYnManWJUSU1MvZr1RHk4DVPOCJuMDDhx-ur8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=GxnET7hZAi_35kYHcQ32xPolmfG_DKe4Ru5X353Q9DR6qLmw9VXaQTYEkiShlt_Mdc_m6Oir1YQodI-YNN3NW47UDr-jIp2Fa6kw2MvFMm_KRiv7-zcrBMKOeaRdwJeN1TmXm6cJoPwLztD6DKEz5MmbB5tbGVIBrKaZBvhw_FDUK6gljze9pVkTBoUlPz7C6u4ta4PBTmachhQKYXNXu1umZz-hME5E2yi3h-afRZKxv7LrAbFuyFpFCbkv5-PISlviZKG19jsqTUdT0bvUGJfa1gWHddQX6HzQ1f4rY4GbdRPeYnManWJUSU1MvZr1RHk4DVPOCJuMDDhx-ur8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRkO8aphiu2M8tAhnuG_Fw0DncSs3g_JR3Cy0tYVfJIDiA9Z_0wDb73GlOjv38YOUYyqPty1RLiwmziTFdnMTYBjRXDO7SZFEQaSOevZSbMJANI5fOmRssWy3fubnTTa3LJaaH5szg5YG_k2V51mHjXUpkBWrqbsYOQSjlzUfEPHPbSkFVwr6V39J8o-agqV8gZCybHjRM18H68NPNQ7ZnpLPsiaL6J9QkDP3ntkly1IvBkibGBp8VnKCUxaeba9neh2JnO8GRH7fmy1hhwKqZrHg_GR80A2gw1s57aLoLQhvjWbHc_1No-mVhpFZZ1jVJNIoLRtEr3ryDDp7IkEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ha2bEs7asELY4cCRStBn2898C7C-t5lXv82WDnQa6ngzQDt21l_iysT1jhglUrkFAk3Usu07w8r_wPNX1JMNW0294mWeaJ7eBVn0UUCcPd6el-hkBqYhNIaXMhSRNpiL6fRwSB3VZt6AjolW8ommGXVEYkpYFb6BLKcAXOWUZRe_x-MWppkd9Gsgkr7jPp8TTYG4gIo6Wd4GDMQH19GoTT-QpL7ouqnaUpDT3q30vX2k1iVDtaBDZEC6ftzhaI9SkCu_5COCuzDjlqYs0oy5dg4w2lO8jccdvW8b9awkjOSz2xsZA7QWllC1dftLFmt2tGQ3S1BBPeHOyCXJVgB8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QB34RHTufhAgcRczZUOSSnwu3Snb9JoknUcCyzlW3xI3DoLbH7OflyYztno5RQ3CZglQ9rcAq4z6W8u93LSur0grF7QY6s4Nllr8QkblOvdhoU_v2xPTyOQZ2WFpcqn7aU-m-e_Ye08aqwq8FTItmdk0IZe3ua50cQ7hpJnDZ4BwxCDBUbcL838_m0RzVMXxBXujp-bQvoEOpau6B44-kDDQ0SWCVz24xQy5XV8OKVu0R8xgG8YcJfF12tBiLwRfwbyEf5UkFOT50sFbrCK_PGe6npAk_FCXbKfLHgbnw4xLnK4wq3tjJexySIQjXSaWvE0UFKipFzM462QFhoXGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bndwg_Fwqam7_ocfHlW8msjuzVXsfJn70Kw8fvaJIXroZqqIkfop3Spl5Jl_yVoVhwFISaZhS2nkn5NFpAKB4KhiU_T8IkCS2MZOH1nNOIg0MG3ItZPR-mAN9T2YBt-xM9qBgFvHVqTZrjcq7C0KpOkCdlYmfABpKlGlHoge0wh_j6Ar0kTjj4kcFu34eipb1NjZMF0UgSxRmme0u58Ub2h96bA5jdUBahJgYQOjKoMxlScNthMj4dVdcM6wd06KIj3APbzWnAA8uTEOl0GgE7G65kzlrqQv4WGRuv9QJh437gl2SNksAH5fwxeuILIPCbt-FqghUipOUR1CDippoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UacNecu7Jd1pHp_yAg0aLmxyzg83WVzl2C7jiS1dEPkkBf82FnuSh83BQV3jCxbG1KWol7G0T3BPnUwHAuXVUAzHDHt_JbNqdu6LILdCLmTU_ndLNORhxDsJ7_JECbxxoULbECVzY5FGsbaZ4jFIOniNnYcZJQTfxzg0jujdIIunwO9lwxeZ1usiieqGyAXhZk02zQ2xDgdMGu6LG7DobuU5_nKenrQox5XqTjk_v20Ra3-dMxP6zc7IZVs5zhkrwCnSwEcHQvpUsQB6s99s6k2OsOl_VDWDFln8TR9S-bfIy9iyZvj6PTJlWF5snKYXRH9qzyDxu0by-fjotr2Lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZcs3p1Gb7ZtPXgfkn2Wj6IT1nxLhQmcqvNJbgikqMGu2d559mHrF0FcONol6Bp9Q4SEonGXz9iMx3MIVh1YedKrJb3n-akOYs7iJ9RZ918SCPSm9Ex3hPt_TJVfrZjp09G_Rvv6MCaFGSEcyAMiUrSM3mYpbchqMKH4XhxMUdCzs9AzeJaIYG5iVZhJAqsKHh33es_Hj68znNDEDAHqXsZefwmtP48Zjbonx7ut4ARNOrMchOZf6KSxDApvF4EjggjsxuqjXi_GOnrJdo88zocgyiF5sx9y9et9kUZUZuPZyVtswliGO1hyJwVEM6i2STiYbbGAHf-JST-c0RGu_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">BadAngel66636
آرمین تیموری راد ۱۹ ساله
پدرش: امید تیموری راد ۴۷ ساله
عموش: امیر تیموری راد ۴۲ ساله
نوشته بودند ۱۸ دی در فردیس کرج به دست ماموران سرکوبگر حکومت کشته شدند.
روی مزارشون نوشته شده ۱۹ دی
و نوشته بودند:
به جز این سه نفر، همسر امید تیموری‌راد و مادر آرمین هم در پی اصابت گلولەهای جنگی، بە شدت مجروح شدە است:
@VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFi0oDb8FmUbZlFeORo5jIJAygtc2ZnEG8BBwbC_XOGM4NtwPQfGhspJdWrDda9GtSPjkrrmZusfcZTTcaUzI5yult5bfSLAHSdI1rKqjP5e-fZaxVDOpTnKq5zDB3yLXMiqrAvRWUpyQybyVJU_qYJAryN4z1UwJn1DmXWtyRXwRB_0Ce9FaWxRyCQHAR1GXrujdNlpOhLLGmDsRXQcPDEy0XgmjMfmjgsM4mpUFFaWUJUr1duAQgg-cezOZxCqjflRiZN4JbQK3ErMkU4dHIFEuXFd6lEpsSQm_w7xeG9xHxfXq59WJ0eNJH3gqFScr1H2NeXjlmnaBygU_f7GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=GjuyhBJlMq2pijF16QNerBC247BySvZCr43R954qPPhqfVEzXoDnjGAbosY0igbOel34mYJPlzmg9t45Hwqt-kCkznKNH7ZjulHSEe3qhdY5GPq17JCl9cMgDxrTbnR_0hn9_zqOG7fDsiSZYhJN6OIhccas2QFFEz3gZvX0hSmA6KX3R2Ylggjchd1Sh9L6iOfcXrUsWYNjvSIABeQKctrJGUdj9O8ULmtfoOoplO7fDEfZVaEgq8B6atKktdBvswwh_Kl6YfBsTvxbwKn1UKIXbYikRc3TrOKRqZWN2oP_QN6CosYbpkpJC338iH4YVArDemu0u3G1sdfzIxPKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=GjuyhBJlMq2pijF16QNerBC247BySvZCr43R954qPPhqfVEzXoDnjGAbosY0igbOel34mYJPlzmg9t45Hwqt-kCkznKNH7ZjulHSEe3qhdY5GPq17JCl9cMgDxrTbnR_0hn9_zqOG7fDsiSZYhJN6OIhccas2QFFEz3gZvX0hSmA6KX3R2Ylggjchd1Sh9L6iOfcXrUsWYNjvSIABeQKctrJGUdj9O8ULmtfoOoplO7fDEfZVaEgq8B6atKktdBvswwh_Kl6YfBsTvxbwKn1UKIXbYikRc3TrOKRqZWN2oP_QN6CosYbpkpJC338iH4YVArDemu0u3G1sdfzIxPKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YZB_Ew-VgFP6tt4VV_eKOGw_UJEBsKsN380c5JOFo6wy7HT8kMmEO79G-tyttYYirKEr2aNo61i3FBgDt9VK1GM1QQu_8TGt4MNVa-U8sxOwIRbNMQJzwLhJuxlzJNBFnDsuC1PvZJnIy2vlmlTj-C88uPFpL-4-Bar_t8ca3vTyAozOa18SrDHuB4XJF_lV_gfkis13d1suWG7Pxdj2iB_IixLeItXTyAJhgm23jgtxFOu6VRL0V06zp5bRuWKtJ-FLTOV-vX-V60QW3EMfV0sGejtrDi21t-TC5InTVQvGabPP6ftLU4aGZHgT9gaVwEFEHwgQ-CrSwTA52yGkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKP9z-isXEoWU3aHC2ddKyl6Uewf_hzgBIlFxTbyfW4HjkijtuzMbfjLUjOGw5lQopHQVQ0DGqzd6L9_M76lODQvY2EtkXOn4xhe-b0jbReKrJAfJ5yWPLdyUIY7CxilTyw61T9puSJInwLRWVHkziaUA8Uqp-TN6QnO05_qcz9_l6XDW804Y-ErVmPuqU6_H65CawpqiWgkAz_V0cZnZGL8Hgr9uY4fpv1mC9w8-Fos03iCt_RFs_PK6opbv40KT86HxSgPDDydktW_qxrLPAjjClj7FbQTJU_CnBEouARDiZBkhx53T94mRkR5JkhwLhfFJ9a6LtB7zNyHbs5Fhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم نیروی دریایی سپاه پاسداران انقلاب اسلامی روز شنبه در بیانیه‌ای اعلام کرد که سه نفتکش را که از «مسیرهای غیرمجاز در تنگه هرمز عبور می‌کردند، و همچنین سه شناور دیگر آمریکایی را در مناطق دیگر هدف قرار داده است.»
نیروی دریایی سپاه در این بیانیه به هدف قرار گرفتن سه نفتکش ایرانی توسط نیروهای آمریکایی در صبح امروز اشاره کرده و گفته است که این حملات خساراتی به‌بار آورده است.
@
VahidHeadline
علی محمدی، معاون سیاسی نیروی دریایی سپاه، روز شنبه در گفتگو با خبرگزاری فارس، گفت: «در ۱۰ روز منتهی به هشتم شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.»
او گفت:‌ «حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل اراده نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=LkN5hgx397DqUKGxhvYtSmyMDCmqLNpaBwe4b2keAdwmUeJIe20DojoXgOJq7HUm81HNCl5PUBkYhV1oYiDxCijbA-z2G9Cp2DehsxiS3-gYymMGCeAykG7UhjX0YskRYiFYDvB7OHjnZD3KKEZvkho3TxthvDrXN8eJuBpmFAFQIoui-V8p67qaccKOMX1gnTwiZxNI__P6JoaYSqLe5TCrah19Iq3572EscuUHd6ucNkpTO2HWvGIHV2daxPHeiRPPvXnvwW7mh8m9YKDfgzobq531vlyLVeVZtQ3uJYPOattx-1mcQjWvOAD7km1MvGhNCa57FQtq80-cOJ6Edg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=LkN5hgx397DqUKGxhvYtSmyMDCmqLNpaBwe4b2keAdwmUeJIe20DojoXgOJq7HUm81HNCl5PUBkYhV1oYiDxCijbA-z2G9Cp2DehsxiS3-gYymMGCeAykG7UhjX0YskRYiFYDvB7OHjnZD3KKEZvkho3TxthvDrXN8eJuBpmFAFQIoui-V8p67qaccKOMX1gnTwiZxNI__P6JoaYSqLe5TCrah19Iq3572EscuUHd6ucNkpTO2HWvGIHV2daxPHeiRPPvXnvwW7mh8m9YKDfgzobq531vlyLVeVZtQ3uJYPOattx-1mcQjWvOAD7km1MvGhNCa57FQtq80-cOJ6Edg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E32ek-vTPZkuABhfpfZxNZVmSSpi68v5qyPNSNvhaC6XWhHq4jX2hdjyWZUSAgsnnhmaTivxoT1tfaBpXH_9Oq554GM4xocgK7W2ZPad9SPSnnnZvm3Zsl6K8CFGwfTNebBwyAkDzldG72gPJpyYZBUXBhcWcRgppp-IK0Eh0oOXFKIRmuWQx1HxQ2kcBrUQD5drojFlCftB1o-Opayw43X3yoi-kwV8_V6SB7ZB-vHY-bhBDTnwta4lA-6yTLyCbhfbpDnVJ7qYa4nAZIZl5ti2y2HNEXY3S4hLMTUPLd2WeSoBpqKWQDW6CpzkgUOpTO2phPlWlTAO4wantmivhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9owg3YR0G-N9QSyY7Y8FubtUB2cJoYxAIBfdDw09n52v8k2SNkj1Tl-VTO5LLq0FWrq_ak16Mj4qKMBAcoDxcv3FTiF4IW048Sp4MIpR_3B_NomtwsmitofvaWeNOlqPYYNlGLl71oPrgrSjRdVuIXVDxw_gYhuvKZHDMc8-yWJbGagT96r1saXIGIMcPK2qoaANAgiKIJryN3Jz6cLcW0kVjcw54wiV1q-P-IzpM5iox9eYUDYLvfXvrxeU9Nx8mQvCrKD8NEWLxnU0nMePbgZo-bcwB7Z1X1ddGx-OQcS1za9s4hR-QLlJcq6zAvfROWTyE8ggN3rjqhNTURo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9m-br2Vklyq_JqRO89oZDtry_VW5jZ5W0SPLGxWURD_Z-KXzjoRa_KkHLEa9J9VfrVvBJHpsBRLwf9q51HL7IUFmegEUaA0DmWCO7buG9qTS1r3Jd90asOLJU0UAzyYd5HUUUSLBQXYUGWt41Mp4KIrYC8IEVza1w_E4LncnxgJZvdGmR_Ix8VqUt9IbtqLego1Y_NeSVqtN1LryxH048bHgNnwBE2rD2aYpph9W0AhBuaY6pk040WXY3ZHK98_jo_ZLy9spT9XQvjPZ9YrCW9ocwsii3ZGwlZfIaWzF00NHAX2WrrB_J0jqd18zsZdUryN3QNOmzep_1tOkEXTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❇️
مادر دو معترض جان‌باخته، در لاهیجان بازداشت
🔹
مادر دو جانباخته اعتراضات ایران نزهت میرراضی، معروف به «مامان نزهت»، مادر علی و عماد شوش، دو تن از جان‌باختگان اعتراضات سراسری ایران، روز جمعه ۱۳ شهریور در لاهیجان بازداشت و به مکانی نامعلوم منتقل شده است.
🔹
نیروهای امنیتی نزهت میرراضی را در حالی بازداشت کردند که تاکنون اطلاعاتی درباره نهاد بازداشت‌کننده، محل نگهداری و اتهامات احتمالی مطرح‌شده علیه او منتشر نشده است.
🔹
بازداشت این مادر دادخواه یک روز پس از آن روی داد که او با انتشار ویدئویی به پیشواز زادروز یکی از دو فرزند کشته‌شده‌اش، عماد شوش، رفته بود. خانم میرراضی همزمان با افزایش فشارهای امنیتی در استان گیلان و جلوگیری نیروهای اطلاعاتی و انتظامی از برگزاری مراسم زادروز هومن صباغ بر سر مزار او در لاهیجان صورت گرفته است.
🔹
نزهت میرراضی در دو دوره از اعتراضات سراسری ایران دو فرزند خود را از دست داده است.علی شوش، شاعر، بازیگر تئاتر و نوازنده اهل لاهیجان، در جریان اعتراضات سراسری «زن، زندگی، آزادی» در سال ۱۴۰۱ جان باخت. هه‌نگاو می‌گوید او در جریان اعتراضات در اصفهان به دست نیروهای حکومتی کشته شد.
🔹
عماد شوش، برادر علی، نیز از اعضای فعال خانواده‌های دادخواه بود و بر اساس گزارش‌ها، در جریان اعتراضات سال ۱۴۰۱ سابقه بازداشت داشت.
🔹
عماد شوش روز ۱۸ دی ۱۴۰۴ در جریان اعتراضات در لاهیجان بر اثر شلیک مستقیم نیروهای حکومتی و اصابت چهار گلوله جان باخت.
🔹
در هفته‌ی گذشته نیز جعفر پناهی به دیدار مادر این خانواده رفته بود.
@MahmoudianMehdi</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=YM0LSdHDO_UYdSF2Mp365NMLJNGh0C1Js5hduLgO7Y_fmDzF7zWtKVerkWPoBlpikK5fPpsX-WJYNb_zqYE53U5ivTo0dVOW_SGd_nx8ZkBmYSwD-qqdLtRpXM0Btnhs2RzTsOKWnBdYTqF-24SvkexsXrOJjAtq3u_Ggnf1f7Vm1o1iOu4rxysgmiSfNdHGeN8BOM8rrSDBCiMjCjhpY98SIwrtyM2WCFjtnMd3pcWghK1wT3voesSe51Ub8-bZq7H_j06xnI2_bGLmEKErlP385DthlHtutEuMRrdUet_4FndMSpgyh8nGZkCsJPXoAiLW7uND3k2_19ITaOehEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=YM0LSdHDO_UYdSF2Mp365NMLJNGh0C1Js5hduLgO7Y_fmDzF7zWtKVerkWPoBlpikK5fPpsX-WJYNb_zqYE53U5ivTo0dVOW_SGd_nx8ZkBmYSwD-qqdLtRpXM0Btnhs2RzTsOKWnBdYTqF-24SvkexsXrOJjAtq3u_Ggnf1f7Vm1o1iOu4rxysgmiSfNdHGeN8BOM8rrSDBCiMjCjhpY98SIwrtyM2WCFjtnMd3pcWghK1wT3voesSe51Ub8-bZq7H_j06xnI2_bGLmEKErlP385DthlHtutEuMRrdUet_4FndMSpgyh8nGZkCsJPXoAiLW7uND3k2_19ITaOehEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت سنتکام:
'
سنتکام پس از هدف قرار گرفتن ۲ ناو جنگی نیروی دریایی آمریکا توسط ایران، ۳ نفتکش سپاه پاسداران را منهدم کرد
'
ترجمه ماشین:
تامپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) روز ۵ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی موشک‌های بالستیک به سوی دو ناو جنگی نیروی دریایی آمریکا در حال گشت‌زنی در آب‌های منطقه شلیک کرد، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
یک ناو هواپیمابر آمریکا و یک ناوشکن مجهز به موشک‌های هدایت‌شونده با موفقیت از چندین حمله بدون تحریک قبلی ایران گریختند. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
پس از حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران،
M/T Downy
در نزدیکی ساحل جزیره خارک و
M/T Stark 1
در نزدیکی جاسک را به‌طور دائمی از کار انداخت. نیروهای آمریکایی همچنین نفتکش خالی
M/T Kylo
(که با نام «Noxen» نیز شناخته می‌شود) را در دریای عمان به‌طور کامل منهدم کردند؛ این شناور پس از آنکه به خدمه دستور داده شد کشتی را ترک کنند، در چندین نقطه حیاتی هدف قرار گرفت تا غیرقابل استفاده شود.
این سه نفتکش ایرانی بخشی از یک شبکه سایه چندمیلیارددلاری هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ ابزاری برای دفاع از آن‌ها ندارد.
دریاسالار برد کوپر، فرمانده سنتکام، گفت: «پیام به سپاه پاسداران روشن باشد: اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه کشتی شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و در معرض آسیب ایران را نابود خواهیم کرد.»
CENTCOM
دقایقی بعد در پستی دیگر:
«پیام به سپاه پاسداران باید روشن باشد: اگر به دو فروند از کشتی‌های ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه فروند از کشتی‌های شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و آسیب‌پذیر ایران را نابود خواهیم کرد.» — دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
پیت هگست وزیر جنگ آمریکا:
ساده است: اگر ایران به کشتی‌های آمریکا شلیک کند، ما نفتکش‌هایش را نابود خواهیم کرد (و غرقشان خواهیم کرد). تنها کاری که باید بکنند این است که شلیک به @‌USNavy را متوقف کنند.
ناوگان نفتکش‌های ایران بی‌دفاع است — ایران نه نیروی دریایی دارد و نه نیروی هوایی. هواپیماها، کشتی‌ها و زیردریایی‌های ما می‌توانند همه آن‌ها را، در حوزه‌های @‌CENTCOM و @‌USPACOM، هدف قرار دهند.
PeteHegseth
خبرگزاری صداوسیمای جمهوری اسلامی گزارش کرده که خدمه دو نفتکشی که امروز از سوی آمریکا مورد حمله قرار گرفته بودند «با قایق‌های نجات به ساحل منتقل شدند.»
براساس این خبر یکی از این نفتکش‌ها «خالی و دومی حامل محموله نفت» بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TPWsmLoZCGU_ApeczY-fcK0ZbdWqClWtLXtOUkr_LhIkjJrHF2BIZCipgDeMwPUKnlzFploStsrdy26zawV9G4FE9ySo-ATcOeNmqF3AZRv8aNVBkNwf5r6Qar6Nonpzbrt1dWD-de1HsyPYgcO1bSlKiDB0dvKC-iPTOF9jUA3IhKMb4fclADeUiBNyb469pf-F-NeHFIWqV-7SwD5TmcpYqF82E4lmp0jDI-CvbykbDUvMXcfb8tWTvEQkRrMi7H8aCPBgXM3VSkIu0n6lJtsatNSbTFXgnmObIu_pwUokDkW19VlwV2psmBGaynzPOZmxv_aCJVbxCw_QS6RwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز شنبه ۱۴ شهریور با جهشی دیگر به ۲۲۸ هزار تومان رسید و بهای یورو نیز از ۲۶۳ هزار تومان عبور کرد.
وب‌سایت‌هایی که نرخ غیررسمی ارز در ایران را به نمایش می‌گذارند، همچنین بهای پوند انگلیس را ۳۰۷ هزار و درهم امارات را بیش از ۶۲ هزار تومان اعلام کرده‌اند.
این افزایش مجدد تنها یک روز بعد از آن رخ داده که عبدالناصر همتی، رئیس‌کل بانک مرکزی ایران، کمبود جدی ارز برای واردات را رد کرد و کاهش شدید پول ملی ایران را ناشی از افزایش تقاضای «احتیاطی، سفته‌بازانه و خروج سرمایه» دانست.
قیمت دلار در ابتدای شهریور از مرز ۲۰۰ هزار تومان عبور کرد و طی دو هفته گذشته به شکل مداوم افزایش یافته است.
این در حالی است که همتی هفته پیش گفته بود ایران «به‌اندازهٔ کافی» ارز در اختیار دارد و بانک مرکزی در صورت نیاز آمادهٔ تزریق تا دو میلیارد دلار به بازار است، اما این اظهارات مانع ادامهٔ افزایش نرخ ارز نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78240" target="_blank">📅 17:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uNi6_zhQ3rMQFCDSx3daC0bVpTWW33qk3CvdSF534b7ZXffVffwwBaVu69gPv1d1XJFIMvcLjPkkcx-NAf-Nsy8F7Yw5z1Ha9cxOnsDHi4oPDzp4A6lkzOW94jyUplGpvNusDZv6bc26szIPjCRgKCmAvY6n_OOWdMY3719ub6tae4c6ZwiZiqEmZI9VzCTS8Cs9kHo7jgNc3cHQ8L2c_xUQGchvIXmhskoowEec2N3Ot6RHZ63QNc2wphizHocv5mPS8yDSQ3P_t7BRcjZNdsCqk1K8HiTYgtQh_4DjdzycJPS6e9WfsoqA6kBL5GfC_tNJtMJ6gzfoVikqoFbxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده روز جمعه ۱۳ شهریور از موافقت با فروش پنج میلیارد دلار بمب، کیت‌های هدایت و دیگر تجهیزات نظامی به عربستان سعودی خبر داد.
این وزارتخانه اعلام کرد این فروش، توان دفاع هوایی عربستان را برای مقابله با تهدیدهای کنونی و آینده منطقه‌ای تقویت و هماهنگی تجهیزات این کشور با سامانه‌های نیروهای آمریکایی و دیگر شرکای واشینگتن در خلیج فارس را بیشتر می‌کند.
عربستان سعودی از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران بارها هدف حملات موشکی و پهپادی نیروهای ایرانی و حوثی‌های مورد حمایت تهران در یمن قرار گرفته است.
وزارت خارجه آمریکا کنگره را از این معامله مطلع کرده است؛ این فروش برای نهایی شدن همچنان به تأیید قانون‌گذاران آمریکایی نیاز دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78239" target="_blank">📅 17:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19446f537f.mp4?token=EUWFMOTwdgcvuj0ahS_ZzORBFK7SyKEGGOiSF785Z8eyPyYJ1zeQ2H0k8bffRZ2PuA8aooX_Zhb6T9-rPOJ3Q95qAjLDshJhzbEtDJdjLFZYNw3CN00GNz-fS726vRWCPIRyyXOR3FS6wuPn1vNiyDfRBjTbiVtra9JyhXmWv98s7_Hh9r6aFSnz19Smmv7aKm-i_uSgIeTLZO17FBLN_WLUNxTD6qHU8SwxhXKG4LtzTLi2cumOq9sB8mcdU2t294qMZoX-qZ_AwNQMyQFohXliu-yKZ5VeMBNVSFpORpa9WhY27jCHruzeIDqmRIpwYZDCgYkaMHyWnaUHLS1D4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19446f537f.mp4?token=EUWFMOTwdgcvuj0ahS_ZzORBFK7SyKEGGOiSF785Z8eyPyYJ1zeQ2H0k8bffRZ2PuA8aooX_Zhb6T9-rPOJ3Q95qAjLDshJhzbEtDJdjLFZYNw3CN00GNz-fS726vRWCPIRyyXOR3FS6wuPn1vNiyDfRBjTbiVtra9JyhXmWv98s7_Hh9r6aFSnz19Smmv7aKm-i_uSgIeTLZO17FBLN_WLUNxTD6qHU8SwxhXKG4LtzTLi2cumOq9sB8mcdU2t294qMZoX-qZ_AwNQMyQFohXliu-yKZ5VeMBNVSFpORpa9WhY27jCHruzeIDqmRIpwYZDCgYkaMHyWnaUHLS1D4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های ایران از شنیده شدن صدای چند انفجار در نزدیکی جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و هدف قرار گرفتن یک نفتکش کوچک ایرانی خبر داده‌اند.
خبرگزاری تسنیم گزارش داد این نفتکش صبح شنبه ۱۴ شهریور در شش مایلی جزیره خارک و در محدوده لنگرگاه، «هدف قرار گرفته است.»
تسنیم می‌گوید این هدف‌گیری «با چهار پرتابه نیروهای آمریکایی» انجام شده است.
به گفته منابع محلی، این حادثه تلفات جانی نداشته و کارکنان در حال تخلیه نفتکش هستند. وب‌سایت عصر ایران نیز اصابت چهار پرتابه به این شناور را گزارش کرده است.
خبرگزاری فارس پیشتر اعلام کرده بود که صدای انفجارها از محدوده خلیج فارس شنیده شده، اما نشانه‌ای از دود مشاهده نشده و منشأ صداها مشخص نیست.
نورنیوز نیز به نقل از منابع محلی، گزارش «حمله موشکی آمریکا به یک نفتکش ایرانی» را منتشر کرد، اما آن را تأییدنشده خواند.
خبرگزاری دانشجو هم ویدیویی را منتشر کرده که می‌گوید مربوط به این نفتکش هدف قرار گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78238" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=P5gyozT3YXBzh1yfFbVRNH1wuxamURzpvouSGzAP7Qld65QoQKg_Lp8ErhidCX8NWnzhGFN0bblFON0uDpATzIQ8Rl-Bi4dja-uP5DpwUTdzbtEPAcAMviM69YHjL21Aeney6OnRzJvm2pp22Z19jIY1wUx8YC0mwJyw8FeeRuSN35hnL5YsTtHA12NC_tX8P5bSyoXxEDg_m-ZwXIjSGvx-HYTUko_XFisg8wTafbDmpuMWA5562OFFuICAKXwGGdwazzFWx4BnEk5F8t12FDBe6TKUiabwqz15HJIfTVzzy96dN4hi7n6baNEil-p3rRWwuwg4UFefBR1VL-EqzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=P5gyozT3YXBzh1yfFbVRNH1wuxamURzpvouSGzAP7Qld65QoQKg_Lp8ErhidCX8NWnzhGFN0bblFON0uDpATzIQ8Rl-Bi4dja-uP5DpwUTdzbtEPAcAMviM69YHjL21Aeney6OnRzJvm2pp22Z19jIY1wUx8YC0mwJyw8FeeRuSN35hnL5YsTtHA12NC_tX8P5bSyoXxEDg_m-ZwXIjSGvx-HYTUko_XFisg8wTafbDmpuMWA5562OFFuICAKXwGGdwazzFWx4BnEk5F8t12FDBe6TKUiabwqz15HJIfTVzzy96dN4hi7n6baNEil-p3rRWwuwg4UFefBR1VL-EqzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتین خواجوی‌نیا، دانش‌آموز ۱۶ ساله رشته کامپیوتر، شامگاه ۱۸دی۱۴۰۴ در جریان اعتراضات مقابل فرمانداری شهر قدس، قلعه حسن‌خان، با شلیک گلوله جنگی کشته شد.
مادر آرتین ویدیویی از جمع‌آوری کفش‌های فرزندش منتشر کرده است؛ کفش‌هایی از دوره‌های مختلف زندگی او که حالا به یادگار مانده‌اند.
مادر این نوجوان کشته شده، نوشته است: «از اولین تا آخرین قدم‌های تو را مرور می‌کنم پسر قهرمانم. از لحظه‌به‌لحظه بزرگ شدنت حالا فقط خاطراتی برای من مانده که هر ثانیه از مقابل چشمانم می‌گذرد.»
«از آن نوزاد زیبا با آن لباس زرد در آغوشم تا آن مرد بلند قامتی که باید برای دیدنش سرم را بالا می‌بردم، تو همیشه یادگار مادر شدن من خواهی ماند.»
او فرزندش را «قهرمان جاودانه من» خطاب کرده و نوشته است: «هر لحظه و هر جا یادت جاوید و راهت پرنور.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78237" target="_blank">📅 17:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hm1S58BRZ_Sjx254OqGDMP0PadtAcyIayAAknBeBsK-V-r0SrthfN4tRQrRDgX4wIxrIThh9FqYQbMBSCAiUuhiPuywDiypaV0Gc7CciaL8ymiYKZ3CxSHMVkbq6ft3CXpDmjvpaFnCXU3cTbViK1E35RP2Fzs6ikBECOBhviNPioyiOffB_KY2KzYr1SNpwJ_KJF1Zixrm2tqkw-lWxXeRk0HKwDvfkVYpuwtwD-vRJE4a9NhkKPsUEMAAm4ni2r0H28Yl-up6aEV-W2zp7RYKlRipqLosgwyZomKgy14C53-aCsWMx7gitWL_-2NEfD-yQg3r6KYw80qQ3rPTr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PhDoBtxgpiNO03lh9w1e09iCJSIkq-JMKtSuDD6sc-KpFPSifTvp87EfLT_BhTZHCYtRWvwRTUkeYN_qd789KAQq-htnF09z7ie6-EwMITcoiaUEJ_POsjVE1bG1chEUJplfRhTp5V9x0nBOV4eJJou72uxdFkJDWdSWgNE5qM5venJB6OSr4VYzNtZCzzQ4P2e4nwKQ6j4lFt77fWyXJ-JPAjXuzSYYXPtvALg-LAoR2iuJJhcJybB5MutWabqxUXkEh5fFIAq6uiwuZHZJzwkX8_aUoxnMcy70YL06b00hbEYJoBp8nOb-8P21e8J2OKHrD-EEHiI0zEn3x4L63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
