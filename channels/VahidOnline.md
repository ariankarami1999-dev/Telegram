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
<img src="https://cdn1.telesco.pe/file/ADVWeaQzLqMwhfqknR6R1oNUBo_X1Bhg0Q_TJk0uk5-s-dPUpzjtGZ9dqgHULaXAltjZAa0H03vxQ1eTix6K_OKp4fgV0YvdKFvzpxft9-o2KNV_gt2eOQxHu9pCOaCxKCI-o3NtnBTzmUTyNvNM6QMcoJapWPmmw9MjKl43_bEen3TF-W65KITI8JKPHJVhhRRJ6HcLwfFGKv-JuOTHk3SO_BkR5lU33VyOOBWzdcZN6QgjwT_qWOBYRAtpTiWpKyymkR2OWqJtbkeunGXLTHlb0fTzbi9cQEEx_CjYXP4zwrimH9OScGq6RhSFhsFjusDUb0Qbbgmw4JhfS_Lx2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pUQ7It0PPRrxo8lxIrR2DuB0VpHL2M2SPFgKYHpf-dJQI3rKzOsUhjbEA6KLB1unNfFGwESnZX8fxmOEC5SEnASgPXjSDappphz7l8Q_H1zz5WsJxaz58A9oWcnUn1S7mkpSjOsfF8gJbRm4ZDaMimU_tyjEDGU-pF8I7qXWqcTdtvACr-Gse_vQ5Q2tAr_lCo_DsSzDNTlBDGa3lhNI1c3E-QiLBVQk0reLJv-Ynx4buL8tn_PS7tDRU9ng_jzGOCLr5a7YsGeOCPB8JLUb_nRyezPlq8OeF8u-gqIyh0dbg7l5CJxtr7aFPW_tbnQlPuZIWRbhG3jl-2kcmItb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از دو منبع آگاه گزارش داد اسرائیل این هفته اطلاعاتی را در اختیار آمریکا قرار داده که نشان می‌دهد جمهوری اسلامی به‌تازگی طرح مشخصی برای ترور دونالد ترامپ تهیه کرده است؛ گزارشی که هم‌زمان با تشدید تنش‌ها میان تهران و واشینگتن منتشر شده است.
به گزارش سی‌ان‌ان، یکی از منابع آگاه گفته است هشدار اسرائیل در هفته جاری به مقام‌های آمریکایی منتقل شده است. منبع دیگری نیز گفته نهادهای اطلاعاتی آمریکا در هفته‌های اخیر به‌طور مداوم اطلاعاتی درباره احتمال تلاش برای ترور ترامپ دریافت کرده بودند، اما اطلاعات ارائه‌شده از سوی اسرائیل جدید بوده و به یک طرح مشخص مربوط می‌شده است.
سی‌ان‌ان نوشت جزئیات این طرح هنوز روشن نیست و همچنین مشخص نشده که آیا دستگاه‌های اطلاعاتی آمریکا نیز به‌طور مستقل این طرح را شناسایی کرده بودند یا تنها از طریق هشدار اسرائیل از آن مطلع شده‌اند.
کاخ سفید در پاسخ به درخواست این شبکه برای اظهار نظر درباره این گزارش، که نخستین بار روزنامه وال‌استریت ژورنال منتشر کرده بود، به اظهارات اخیر دونالد ترامپ اشاره کرد.
ترامپ روز چهارشنبه ۱۷ تیر به خبرنگاران گفت: «آنها می‌خواهند رهبر آمریکا، یعنی من، را از میان بردارند. من در همه فهرست‌های آنها هستم. امروز صبح دیدم که در تک‌تک فهرست‌هایشان قرار دارم. تا اینجا کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد. اینها آدم‌های شرور و بیماری هستند و باید این سرطان را ریشه‌کن کنیم. سرطان را باید از همان ابتدا از بدن خارج کرد.»
سی‌ان‌ان همچنین گزارش داد تنش‌ها میان آمریکا و جمهوری اسلامی در روزهای اخیر، هم‌زمان با فروپاشی آتش‌بس ۶۰ روزه، افزایش یافته و دو طرف تهدیدها و حملات متقابلی را علیه یکدیگر انجام داده‌اند. با این حال، به گفته یک مقام آمریکایی، تلاش‌های دیپلماتیک همچنان پشت پرده ادامه دارد.
به گفته چند مقام آمریکایی، برای انجام حملات احتمالی در شامگاه پنج‌شنبه آماده‌سازی‌هایی انجام شده بود، اما مقام‌های آمریکایی در نهایت ترجیح دادند فعلاً به جای اقدام نظامی، مسیر دیپلماسی را دنبال کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76911" target="_blank">📅 02:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbTHdzegxh7dk8DFvlXCGZ83eA4vv3PpuCPL4rOYTYyeYNDuG-C0uJVmwubDIFMLQW0x8hnEHBNIbK5jO3wrJe_kbj5BBEUd7Eekd8mVsdq4qMh70Bjjf74R60Im7g5_lFv3V2pCfYanu2GgJBXOuaIVrzoj_QszvNJgpEpOnTRLk_zbbluzXuYo2zKkaFUc2L8zVSQnRtsT-qn46qUXZUTD0JW_5XV_L8nAVOYUoYPXSFReFRyxuq_tqZ2PTzu-HzHh-7TBG5a5ibjJ2MMF6RqDmsuGVEFA6bJtqZ7jfK08448wwb3IKrBK0j7WaJfRElxo_lmhW2VsXa_iHgY__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t3bdAjNRZekUQtnqmOnM_cK9AywuXFe5T7vJs8t5XXp3w3pE9aBbdgIKNs5nBbI6IQrPo4VgyXryLF6MSvLnyjTgRToj9KoTpQLNRKnDM3efRskJ59y29-0yoKmPilXI-jM9PpoGkQjBVsVkfJxomL8bvvgVhLLxLMKpRWvACoSA1iSuUxbkisiF1jQbNCZ9lCU7L2nO8krqqwEV_qeFgfld73CAYkxEBhPyBS6JOuMmZEIisqVEq2-LD7M0rJS5QVBUgyIn2OvDEpCZAzvhdz4AjLBpvW7ELsqKvk1MiCUMA4ucCcb2OJ7tybtf-Oz6t6BJSmG7S3IVnMqydp7tEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hfSfM2fK2TtZDl7zKOIb8F3rbVvFKw1rZK9D0-_Qb5kaYmXDvKcUYkVu86_siXEbwyT_TY8SqeCTr6QyJfLR2PUJ0acZGRBixHKcIw5qho4mMYGQWEy0d1IiLJCFKdsGZr60f_pUvj_QC9lqIjFzbuyhL1uXSk_2ygRnrISB2dBuXowJGXGJUHyIum4sY_cmsmZpvzpoh7K3xSoEE56l94IPkDOiHjJu3mr8ArOYLO9HITSmJBAMTQN6N-mVap1J6gKyNPjuXQ0ci1DPpgNv15g_H_kbjUE6A-u6nfkhMIRd_gW_Vin44rgZ7F6KN-hDMch78o8FWwlkM1eJnA3yGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHuudO8BSGKxkcbL-wwMMKqFnFk5Q7CNmOXOPvpT1VoiFiXNQ45EgP7Cc8cTW6kClg5SzZd5uyQHZXRHBXYpdxwuHbQtzD0_NS11-EXTg7ifGc9Krqt9Nxu8aoNNBrnO0V6r4IOg1FJ_S_3cilEU4hWkHscy-9cxMOmRXzXvJx6tiRqppO0PNymtxAlXgHmEM3Q6Wdr4L55HqF04VM5Ei3MfT30SAgym-VYlwlRZjooukEFcl65WbTAiShyPFGJpYFgwTUBgo-epu1QzT9JmPkIFSUwkC4jTMA4wRCrox_V-joYGd-Bsg6Mnli5tBtYAp961Rb81bBEmmqyWNIH41Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری جمهوری اسلامی، ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان در غرب مشهد و کشته شدن دو نفر را تایید کرده است.
ایرنا گزارش کرده که امیرالله شمقدری گفته است این رویداد تروریستی نبوده و انگیزه اصلی وقوع این درگیری در دست بررسی است.
معاون امنیتی استاندار خراسان رضوی به ایرنا گفته است: «براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده‌اند که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم، نفر دوم نیز جان می‌بازد، هر دو نفر با سلاح گرم کشته شده‌اند.»
آقای شمقدری تاکید کرده است که حادثه در منطقه سرافرازان مشهد روی داده است.
او وقوع هر گونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم امام رضا در روز پنجشنبه را تکذیب کرده است.
ایرنا اضافه کرده که بلوار سرافرازان که تیراندازی در آن رخ داده، در غرب مشهد واقع شده است و حدود ۱۷ کیلومتر تا حرم فاصله دارد.
@
VahidHeadline
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evigr6Y-cKEVZ1d9FXeHYZe5ZM_g_HfqnJA8em60nyzzAvV1qGgLzyjVOPHxmYUCiGxoat4EQofcpMOwt26cbNm5ROmQfLMsqb1d6ZQqKShPbD-yO02pzSVN-k6wkFKKTn0UH-N3AOu5hCLXqeqTLkYsVKcMXNm9YEQopN9dBOI0olfHnVvhbiFcY0dsYXWNr92mcxRcMnAGo8_BK6ewLYrPvtsc9LkvEMbz5W25KiCztzZyje_vVulmiL2M0lLiGO47b5ZymVI_QDMFNC4iz4pHNYuxdQBvqUeb5dwvPcNQ0iSWmaptkI2qC8Zps43dD_RWum5N49qIM73cNZi8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
فرماندار کنارک اعلام کرد یک منطقه نظامی متعلق به نیروی دریایی در این شهرستان شامگاه پنجشنبه در دو مرحله هدف حمله قرار گرفته است.
🔸
محمدیونس حقانی به خبرگزاری ایرنا گفت این حمله توسط «جنگنده‌های دشمن» انجام شده و نیروهای امدادی، امنیتی و دستگاه‌های مسئول در حال بررسی ابعاد حادثه هستند.
🔸
ساعاتی پیش از این نیز معاون سیاسی و امنیتی استاندار بوشهر از حمله به یک مقر نظامی در حاشیه شهر بوشهر خبر داده و گفته بود صدای انفجار شنیده‌شده در این شهر ناشی از فعالیت پدافند هوایی بوده است.
🔸
این در حالی است که صداوسیمای جمهوری اسلامی پیش‌تر گزارش‌های مربوط به وقوع انفجار در شهرهای جنوب ایران را رد کرده و اعلام کرده بود «تاکنون هیچ انفجاری در جنوب کشور رخ نداده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWtxgNE22EBhin8Q4Gshycnu9KM0RozuqCnxcBh4rKAvnZfYtulyJ4FzidKbUiW7-gQR22JQrughrHt9Jimh7DPe-r8GHC8WfKhn0Yz-b5Gx-bazm8rryadVtyHJDFYpDMgQQlmtZBltoeOBdmgYPydHyzsI2_faYEAq5d0rQ7R6Q-knYhmvCZ7ZU8z7R7JD5zjjvdUaKwLURnyO2H--Hn8QIQL-wKODoepjZrIHhnTG7nrZoJ13xQlgvTWb4EUD7faZ6VFe37w_EV7EEJYllVB6QHaAD7Z1C9RpSIcYZS3J8aO4XEdCuQAqxcCTEqJ-fK3fnjcFbpZU4wulFn2fpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ایرنا به زبان فارسی سخت تیتری درباره صدای فعالیت پدافند نوشتند، می‌ری توی متن خبر می‌بینی نوشته:
"لحظاتی قبل یک مقر نظامی در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه دشمن آمریکایی- صهیونی قرار گرفت."
irna
به نظر می‌رسه از روی صدای انفجار برخورد پرتابه، مدعی تشخیص کشور پرتاب‌کننده هم شدند.
احسان جهانیان، معاون سیاسی و امنیتی استاندار بوشهر، شامگاه پنج‌شنبه اعلام کرد یک مقر نظامی در حاشیه شهر بوشهر مورد اصابت پرتابه قرار گرفته است.
همزمان صداوسیمای جمهوری اسلامی خبر داد تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iHziPtXQRH4X_Ij7lrqN3LU4p161NtJpcIMZKh3iMBgk4cyLc1k7O5SaWJ_d_GpA7ySXcjDe0T3Q3IGcDIJoT8c3EF442zoRcHKSdnUfEgtLF1KnqP-n0gn3e50K_gjrlHuqMgZnDXATZZCQO6Au2LnAYowBga8_GIRX_jYVcrVPCb0hBPFc3SeEarg1GQ_rgQJCJfxU-ThnYJzFdOZJrmgzZMTZtyljQH5ul-L9itXcYkROqs_d3SP4mrHxzqcQPLpYdefJMGIHz1A7S0gYV5Igr39IuIukjIqL0sUiEkkOevYe4XVt9vShJ_-0Z4Tl5x0u9c7VzaXN-fVtSVIPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
همزمان آتش‌نشانی اهواز اعلام کرد انفجار شامگاه پنج‌شنبه ناشی از «نشت گاز» در یک ساختمان مسکونی در منطقه حصیرآباد بوده است.
@
VahidOOnLine
صدا و سیما بعد از تکذیب آمریکا:
برخلاف برخی خبرهای منتشر شده در  فضای مجازی، تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4okmdtmWnkQXcThbba_8ueqzkD2dQJW4k7THLSwCX6qeqP9pE50hPekZBhzeWcs0q-ambWU9h_uPP753iMch_NOs0xeK-uFhZnHAaqozX2dORuyKmncTE-DA84PT5___nC7ylUcFtpsHj_OVUf8d3nBaxjLwNu073Jdh5QnsNMZK3rb5EQKtyz27Xw-UYVt41JAZ3mHq2sjKuM7jyxTHv6WgztkRtY4Y4LlfufTtEl7lAVW1tms3bhSd1ymgD5hyGIwT3vIESC-mTXby-6CRQ8MDhdB4GIdGnuF4eWjfUV_DhWgzVARNvh0DrQd4KU7a1ZpPxWJgo0exeVWIHQliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qpm9fT_09MyC498mhsU5lMnkO_5l-foN1xirNlYoJiP1MhaHz7_Jt8e9UKznFIvsyZN9FU-8mvUj45RxOJkRP-vMtUXAhe_4fZGjG-_kplT3wfJ5n2NtgUbrg17BpkD9nBMuuRENCvOuJfROKEW3j9CuxAw1k95Pn4xG4jbbVo4SySEiRWV_vxiiX7Dqm03XUadIb7CjfQYS7JZqMGMnhKSS2fGTtdn7u4arvQCHdF-Yoaa7du7GUw4yns6eLCuC8DOaQ8cLoepzdvj_bqHrvR_jgNNxTqjhIviQ5xghTKmHmQy--hqosqtPYOi9DtOm827SJedP63kV3fPS6Bg4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5vnGgTnZbxdVauakF11vE3bsgqqJxSGgppEUQqoCyRVNe-F337h2mYnsncvpBzY7mlx2Dte7c6n8DNZwGykYwjksg_Tyqm9a67iQgdgf3197DSch4GVgzqRkdGb0i4YR3Iw233ITVos-UxSodufldhmSJBIalrOFvJwdYNIOE_XRAASumFZfMoZYf65wdnpvaVuE3T0PV7IPjDvhcy0X2bbvZ3CBcCLdg4Ilj-zMjQYtM1qkURieNrsymP9SfR9Y08O_X8Mnzu670Rx_YgU1Prsx11jaOIqXdgZ7TNXOZ88V6Vfiz4XBapXlZ1X6ftNu9mEQXb65lLAsLuBlwqWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t08IYorK51UDtuk2hcSfTa-ewV2q7SSWY2n1JJ1TF3SYmSGq4Ou3fDvYqBLNDaGGRoNpflWGYyERazymMIgHXMRCzLIFiPrGX6HEEHng2bJgqXKQb4t-v2iPegV_zzmaIEteod17u95ucgM8F71dsbr0OUU1W-5dgTfHJSC_dnheqkZhQooyfm_v_kcmqFHrLcc2P8e0jO3Fl-7q66BpUrFxbFKokESIRvYgfaXVmOsHZPaxMUmxczDzFYO0IenqyiCpOznPM1w6u_fPV-c-GKj8WPl7EBRsDzIHML0YY0Xwu54VJ7U1xWLyeez6p_cux-q6ENsfy_RX92T6Fp8hsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KXwn3FUBLX97oeL8-vG7FnnPki5njBtrI3KkwhEzICyPyW-VOmFSSDoUZlLhxXCkxOlqGwv8gG8U5u_TdvDSjjzvfIXuh2CTSRMfgjdi_oQaYVIL9O9z7Jj7tJv6kRaVOS_5chgNXAtPLk7lQdTRlXk4VRkiacFBIuuP-4wHReKuoC878e0ZodmbwHweIksQWyPp-4cU6J31yNWxfRCIELqpiQ7AzEeOMIwvSi4A8ELANSgdRpPw8l15EG55PoPxfzI_Bd95IKm4JSov1UMrnevDrUtsWxBCFa-9Xpzy4ZyG3mN6EakddorUAqbFO_MCAp7HioDy4VYPPNxE1QES8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک‌تایمز به نقل از فرماندهی مرکزی ایالات متحده (سنتکام)، نیروهای آمریکایی در طول دو روز گذشته بیش از ۱۷۰ هدف نظامی را در امتداد سواحل ایران در نزدیکی تنگه هرمز هدف قرار داده‌اند. این اهداف شامل سامانه‌های پدافند هوایی، انبارهای پهپاد و موشک، قایق‌های تندروی نظامی و زیرساخت‌های لجستیکی بوده است.
سنتکام اعلام کرد که هدف از این عملیات، کاهش توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز بوده است. این روزنامه آمریکایی افزود که تعداد این حملات، حدود ۱۴ برابر تعداد اهدافی است که واشنگتن در آخرین دور تشدید تنش‌ها در ماه ژوئن مورد اصابت قرار داده بود.
@
VahidOOnLine
سپاه پاسداران انقلاب اسلامی روز پنجشنبه ۱۸ تیر اعلام کرد که حملات نظامی ایالات متحده نه‌تنها «پاسخ کوبنده» ایران را در پی خواهد داشت، بلکه ترافیک دریایی حیاتی در تنگه هرمز را نیز با اختلال مواجه می‌کند.
سپاه در بیانیه‌ای اعلام کرد که تردد دریایی به ۵۰ درصد سطح پیش از جنگ بازگشته بود، اما «ماجراجویی و دخالت‌های» واشنگتن در تعیین مسیرهای تردد، عامل اختلالات فعلی است. با این‌وجود سپاه مدعی است که جمهوری اسلامی در تلاش است ظرفیت عبور شناورهایی که مطابق با «ضوابط امنیتی» از سپاه «کسب مجوز» کنند را افزایش دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZhCQkyxRkYxNIxu1aVKjvPsJNvjcqf3g_1r5Q2LjA5KAL9G-xpDsUHPNnshCR55Zd85p8a_qf3YT_HNYeWHjHzkG84D-n-7JSaNPWkv10gjy6WReCk4206rfH2zkfBsAzZYj9LU-HriT4_FB3aI6lgPRL2rcBPmLKeaW8JcM2zVmZx94eOQdnq14pDAf7eyij5y6be-LnaKibWC68kT55epmtlrk7EOjPEd6NRlU6XvYeHEtxV727-1hpcuwr5lzGyKK8F2X31Zn9JWYO3SD3R99YUfdzHjsL7d75L6NQwwliRYtCHwWDys555Iwn2w1VOw-c7xuTSNjeoKGNm_1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MjrpI9vXrXDe7KydljTVz4e1W87SLkx0NRKDN0um2nEy3F4qEgt9FajNbqDpwBS-evkgaC91WcTprUI69kZQUXLHbR0No9_iSdftoLaYfJzZg8myxhxB0sB89e6g1OXXLVHWrcYj-4ErZm4NX3MpQqowJZbxJiuSgJcnS1oi6NT6CIODS6ra0txiM7IGDeTAl86uHN6e_WFBrJdZfjBj87ENXbQ-V-tyERnP3jj1PScyS6ePeMFkcTXBqQ6DNkd-H1JGpw4T2a-7sxLz7BAf9NRNxrT_KlQmKiSkDV1Of1EqWWOoCmw6xJKlR9DaQWSRkKsSn_LQUlYNfdFupJ2gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MyT9XYW_lI7swbvtGZzqjNX4NiAu0tyIPMF3scuKbiEVvwQDosjzew06js_eOhQ2gc3xyd2ukfyVDGVTU3JyAk2bF1MIgX9iKpucwmnGLaAW9Z5DKv9p0xARvvEBtzFsh6Ac7hD8SnD2aycGzsRwcaDVWPNDfrouNM16wXC5MQz29kAypPGzgFfxTZ4J_LVO6fv9EboVHdR0H09t_ZRX8PdUmg-X_MEmWeoaFp3KHdTugqy-M22TkU8t19HYHs2NssjlLfPrvKMtoCTNOJCxg7y4olvoFX80qBKP_E_MYIuhPQ_qsT56TgOf6ciKivqOF2qV7uB3Tn3rzUJjjcwrwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=aNmxWserUvn4ihnjzDfXpo6eM8tTdnW-zBf3j7fvDrBrzaBMXXDJOD0ZT4ill_mvqBmoeEXQwNJHlVNyXVU5bfBDzjaZdY7Sj6pDJzt2nqbhxvfI7T62IglOsxWx5Z_wHMf_6fmj9Orl_MGisHZzYotO-cwoWdo0L6GBq0UT47JlQ2sF11wI9xyR2q91du18Zs_OAMb0wAVVdATIJRtE7wNYSB_4oPdrhay2UtKMBy62i15vvHhiT0sXU4wc4mC9o37W8gbfFKriu4v10ZIHhZSvUtRAL7an5Z_RE0KsovZ32x7DknkAoHu-j308qxsGCkTSZuFPKFtyBnuiGliFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=aNmxWserUvn4ihnjzDfXpo6eM8tTdnW-zBf3j7fvDrBrzaBMXXDJOD0ZT4ill_mvqBmoeEXQwNJHlVNyXVU5bfBDzjaZdY7Sj6pDJzt2nqbhxvfI7T62IglOsxWx5Z_wHMf_6fmj9Orl_MGisHZzYotO-cwoWdo0L6GBq0UT47JlQ2sF11wI9xyR2q91du18Zs_OAMb0wAVVdATIJRtE7wNYSB_4oPdrhay2UtKMBy62i15vvHhiT0sXU4wc4mC9o37W8gbfFKriu4v10ZIHhZSvUtRAL7an5Z_RE0KsovZ32x7DknkAoHu-j308qxsGCkTSZuFPKFtyBnuiGliFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با ادامه درگیری‌های نظامی میان جمهوری اسلامی و ایالات متحده، روز پنج‌شنبه ۱۸ تیر نیز حملات متقابل دو طرف ادامه یافت؛ حملاتی که از جنوب ایران تا عراق، کویت و آسمان اردن را دربر گرفت.
رسانه‌های داخلی ایران از شنیده شدن چندین انفجار در استان بوشهر خبر دادند.
خبرگزاری فارس گزارش داد که صبح پنج‌شنبه مناطقی در استان بوشهر هدف حملات آمریکا قرار گرفته‌اند.
معاون سیاسی استانداری بوشهر نیز به خبرگزاری ایرنا گفت چند نقطه در این استان، از جمله حریم پیرامونی نیروگاه اتمی بوشهر، هدف پرتابه‌های آمریکا قرار گرفته است.
ساعاتی بعد، صداوسیمای جمهوری اسلامی به نقل از منابع محلی از شنیده شدن صدای چند انفجار در شهر چغادک، در نزدیکی بوشهر، خبر داد.
در همین حال، فرماندار عسلویه اعلام کرد بر اثر اصابت دو پرتابه به اسکله صیادی بنود، ۱۰ قایق صیادی دچار آتش‌سوزی شده‌اند. گزارشی درباره تلفات احتمالی این حمله منتشر نشده است.
هم‌زمان، رسانه‌های عراقی از به صدا درآمدن آژیر خطر در پایگاه نظامی «حریر» محل استقرار نیروهای آمریکایی در استان اربیل خبر دادند. همچنین گزارش‌هایی از فعال شدن آژیر‌های هشدار در پایگاه «ویکتوری» آمریکا در بغداد منتشر شده است.
در کویت نیز رسانه‌های محلی از وقوع انفجار در نزدیکی پایگاه هوایی «علی السالم» و منطقه بندری این کشور خبر دادند. وزارت دفاع کویت اعلام کرد در حملات تازه جمهوری اسلامی، دست‌کم یک نفر زخمی شده و وضعیت او پایدار است.
هم‌زمان، سامانه‌های هشدار در اردن از مشاهده چند موشک، پهپاد یا راکت در حریم هوایی این کشور خبر دادند و از شهروندان خواسته شد برای حفظ ایمنی، در پناهگاه‌ها یا داخل ساختمان‌ها بمانند و دستورالعمل‌های مقام‌های محلی را دنبال کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v6bUafNSK1-HSzGpueZWFu33VIFRnqpAM3dbHCWMrNARA2RzzEQ0nhkE3whSTaPdXS-46_FqkGoRpF7HUcoZujj3-ED9ha1zu4j4MH97lH112llJXS1H3Hsj1E0hU1gZoKn49gxvMXiVA0E4yUGYpQRVcozd_lW2O78sw4NRY0t-EGIQazTYyWsfkubDfRBA49ODMbZxQEPBksqgL2JNdAto4bgo5HDdbg4ZGfQR7u0_0PhdAq5lV7dzPf9YhPY-xsBAp-Il1ChVUdXYP6NUIypEeefKa-ZmDcWmVAU54yvNAMClLwcEsjCfTlro2flkacFlu51540YBAokhvaWmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ub2WbUVR9JT_GXUOPjcwqV8qp0rjhvzGfJBCMv-a3aaUee6ISzzTOd7_FldStuDdFj7MV8x4SP_vec3xZNFwigqwmB2MO0meusSA6wR9oIyYmoIyGRXr3x5jvJK4l0XjrTURwghEEioFfTTVjU7fHjbj8MGDO7VJjLjFen9zpn0PbUQG-9uwcKwxdWQ3yKB26Ynn9o6gEc99Delj4NkFPSDlIExj6qZWaj5k73hD8TG5vvrqs9i342Zs1Nixs3tMgh0uqvxtS6de09UsRgX-TiB3ssgr7_VNmAodcatsg_uvD_eQ1fQ1OOMniN5GFfl6ciSVX2W6FGxmSNRev3M70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ucbigtoeNH1Y4sKv717ki3WVqxdFkUCTW7-GJUQSG0ffCshx2dMlSAy0BAUnVaiLMHD9Ld8sCk4tiF89WqvKytCE8bBKvq01U5tIpgyf-jcb30OXP9Jvrpw8Liznia6BT8tXQs2GtuWCZU9jYWeeLFRV6stbwxm6OcHJP8Af107LnG6ENrrecZ4OvpwAgn8SsiRHfZwwEBb9vpqK_gV7j0apddjIMu2581mryGLDFdtYRapcKUoCYqu8FCPDs6H--YTh7P-nqmSANLYXwJawWkwaF_WDPKs0hDJdWnnzI4L_h3mnzpuIx7uyZJOvgg2-49bSQuEC9vkD63UjPtRrOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=FwGU6rnmNdFIa-z7Rfg9l8_2_XNYjpa-MCCfLdH4v_x3aSgRwck-QSBNa7sqq5Pn2fj_rOyEqBuclZkDKP8civh_AjIT-hn2cfzu3PXoHyv88In3-ouPUPWxvcmO3VB0r8j-9qpyc_iLuXRqqbdl725rz2rZYuePZh16bRVyKUzHdw-FoSQS9h-sf0oLkauT_sa4LCITkBVU8ilWY4zHkXPhjWXdys2q5YoF2nnB4tIYeKF8HvC0jJ9QF_x8Ne7RZp08NbA7P1ybOPtb6P4xWaT0LbNCzx1DyvTrYP8EMcDwVqek_IugP3NJOJV0SCTZXaeY85bc08fSAd4D_yXTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=FwGU6rnmNdFIa-z7Rfg9l8_2_XNYjpa-MCCfLdH4v_x3aSgRwck-QSBNa7sqq5Pn2fj_rOyEqBuclZkDKP8civh_AjIT-hn2cfzu3PXoHyv88In3-ouPUPWxvcmO3VB0r8j-9qpyc_iLuXRqqbdl725rz2rZYuePZh16bRVyKUzHdw-FoSQS9h-sf0oLkauT_sa4LCITkBVU8ilWY4zHkXPhjWXdys2q5YoF2nnB4tIYeKF8HvC0jJ9QF_x8Ne7RZp08NbA7P1ybOPtb6P4xWaT0LbNCzx1DyvTrYP8EMcDwVqek_IugP3NJOJV0SCTZXaeY85bc08fSAd4D_yXTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=sBojfcM6MA98HbZ40WBrQLX6bBNjvs8WIapjCrnK8OXOxTfD2rmg0lRJF96PGRsBE5_D8SN3Baw2u-WSZY7siIxFMd8OKsweHV3OmcVPhuqdf1WWuh43KiWN0RTVu1iqP8vCUjgarFK1mmw538Jr0PuWgqhXNSqmTFipbu7JDP17bqK2P3IwyFtLvq2dsmpznOTQOwm8Or8AVua0HNS3fol5ddfGg0RLPs2nGmWkmY9Q9OcykaYD8HUl-pCNMP3m7nbgMNFbNWoevWEylpuEz2m7C04Kea6GojMwdWu44twH2f96FmnLMSraORaJURCGvOjr60Xbh4xf4qbkVgPx5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=sBojfcM6MA98HbZ40WBrQLX6bBNjvs8WIapjCrnK8OXOxTfD2rmg0lRJF96PGRsBE5_D8SN3Baw2u-WSZY7siIxFMd8OKsweHV3OmcVPhuqdf1WWuh43KiWN0RTVu1iqP8vCUjgarFK1mmw538Jr0PuWgqhXNSqmTFipbu7JDP17bqK2P3IwyFtLvq2dsmpznOTQOwm8Or8AVua0HNS3fol5ddfGg0RLPs2nGmWkmY9Q9OcykaYD8HUl-pCNMP3m7nbgMNFbNWoevWEylpuEz2m7C04Kea6GojMwdWu44twH2f96FmnLMSraORaJURCGvOjr60Xbh4xf4qbkVgPx5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Glf707v1mtx-B6eyKdGUD3_cvWsoauO2CyKSMes13IM6VLWkDAOe1Czazbsh01D6k-JtxmTSfrJKrXChbvnfSaj4jnqHIK3AyU0YowAVx3ldu7D2fNWZFFxBO_X2aWiFOw4JCaHjfJwfUTxgY6agNS2sf2JCSHe1E60QALJ7I27oNz3loklV6Dzz08PXiWWFkl_jS2vrbjgM5lb00wXyX0nMoo2LqrB1XB6tMNYu4id1hyU3jKof9xV8SKNzANUCPXrF29xtfmCGhL3vCaEfvWoe-XsRCGyiAGGj-DCLlNpROGA-mh1QhhNXqX9neSgui0VN3q05kF6UTEw7gjuTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cO-n3biXaalRKoqUi3XhyHgaXOHXgWvlJOFQ-gwBna3IyyxEBju90ABMNG8aQsuRGvhczFh-NEJd2F-OcGP8W5dsJDpR3QkvapQcNjUajjY4hKsfZ--4PiiU2S9wyjrDN8QgIT5luOgFlCTKXZjZTl7PalVAa8qsAtWS8jxO8TyEcORx8ujTkFuyfuAN8U1r2PFNs51yXWqTK8NnbxzGlF7N4VfHHtRcLkOE4wBj6TEvfwig3XaEJ0Xdc33Zh053st5uCJsyvuYlEjqzQiU5isjeGStvbH-ZJNUJG6IPdYN4l1qAVFh8XmKhNNfrRa5kmxkRuENK3siI1YejXzW46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=HSXEK1eO4GMy470bNX_G8i2Dpjgnkkycw1cddic1uWoGceNV504A6SpyWY3PM3BgM7_JmR4RRmfpDG34tCUfQlQieVIiXHTS9xpRCpAC-FSx2x3P8wYZwdAGA2h6mN0wsrdhoRgOC2ifKQujq3S1uQq8XPiCjCfsjleM9CDZBxUCaXIefIfJpFmT9CAoo16hC8IhyfhgXsEfk-V9prv7_wjVfGwej-pmLUbZ_IRtzOyHd_JOcvPv9uZOn-bZR_YN3BxkrCzI5eWIoJUyeDAreEJzOrC9VTGZJ3TkpJnIUA6ScM0BDGn5bgzJzVwM0d_nk7Q8uCHIEfuv-plzZ4XWvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=HSXEK1eO4GMy470bNX_G8i2Dpjgnkkycw1cddic1uWoGceNV504A6SpyWY3PM3BgM7_JmR4RRmfpDG34tCUfQlQieVIiXHTS9xpRCpAC-FSx2x3P8wYZwdAGA2h6mN0wsrdhoRgOC2ifKQujq3S1uQq8XPiCjCfsjleM9CDZBxUCaXIefIfJpFmT9CAoo16hC8IhyfhgXsEfk-V9prv7_wjVfGwej-pmLUbZ_IRtzOyHd_JOcvPv9uZOn-bZR_YN3BxkrCzI5eWIoJUyeDAreEJzOrC9VTGZJ3TkpJnIUA6ScM0BDGn5bgzJzVwM0d_nk7Q8uCHIEfuv-plzZ4XWvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=qhqjvtHZ_strD9eMtoB3mLyXy3C2yzJe3tDaqi-V9E_ay4SbCJmeHJzXPmOCX5FG5wNI9C4kBbs8hT2b4-l0V464U8G0gUgI9ZZLgedyGbSqlhKmc2vYpSDmPLctERE1O3e5Aq-uvkprlfduAd_Eb0say99zjL5b0FtycTv4aLEWKjDU1mLcZQUs-lEOXv7KnJ_vd9W93qvhFs3qGMUADjxW8REuuuU8vbZONZQYkQyj-w929MAIplObIApOBB9wIUcWJ5vEY10DN5ZGuB7xITL4iE0KWbXLeD4yZePih_S5uuVoCIPWIM3MQirST8vJh7V6BP7UOfDOKeiLnAbE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=qhqjvtHZ_strD9eMtoB3mLyXy3C2yzJe3tDaqi-V9E_ay4SbCJmeHJzXPmOCX5FG5wNI9C4kBbs8hT2b4-l0V464U8G0gUgI9ZZLgedyGbSqlhKmc2vYpSDmPLctERE1O3e5Aq-uvkprlfduAd_Eb0say99zjL5b0FtycTv4aLEWKjDU1mLcZQUs-lEOXv7KnJ_vd9W93qvhFs3qGMUADjxW8REuuuU8vbZONZQYkQyj-w929MAIplObIApOBB9wIUcWJ5vEY10DN5ZGuB7xITL4iE0KWbXLeD4yZePih_S5uuVoCIPWIM3MQirST8vJh7V6BP7UOfDOKeiLnAbE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YSgTxZuBODoQgL0NFBgJND-ETqC95NB_MV4VNbLLoI70fpryuYgirtEonnOLl2O8TYKJMvxpAax5W3sdMTn9ur27vgwKx8H-DsbXTUWuyji2Zx_d4KcZfWU01IXwktkTs8BoBORESQvYt1-HTu4EuCmL_vzLVFryCLZlsIuEZTCopAhRBlaUIC6Mykmz0imee8XRjond9DlaLGdmrdfrEMQvsVOkHDy8akHOO1jdjVT0JvWjDVExcygZ3zeN8FGI3ywhGzK4LzCs1PUVWo91xFnBZLUsbvOxzMDe6ste_Cy0kiwaEg5XdQdu8oHTsSfhIkg8bW5WSxug96TS2Sg7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=oCSRaFMq8p43vjaeS51jFdRCKdsTFt_rEVSrOITKOmFY5SRhXxV9RXuKLAGgkTYdHQe8b9ZoSVVx0oCal8rFLoP2pyWAkutYkpyPqIkflZRxVbpLzN7jrizCkdhTWNph-nEQTYLoHdCUFjXvlMpSij71lvhBtFLkjCwRAqWrwBvd-RutRYJrD_RZws207k8ABhIUZyieUyLeNCeoSZQ4PghejFCfEMFOhxhUePAoTkAzXnk7ytqDtV9Zgu2k_mC52wmHV2s7CjTHJQhyL8OOBmNflE08tTFVRYIOHU5wSyr_7ZZxcE1uV-MuLohkP1RgyGVhGa9g1O6lhHOy9IdEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=oCSRaFMq8p43vjaeS51jFdRCKdsTFt_rEVSrOITKOmFY5SRhXxV9RXuKLAGgkTYdHQe8b9ZoSVVx0oCal8rFLoP2pyWAkutYkpyPqIkflZRxVbpLzN7jrizCkdhTWNph-nEQTYLoHdCUFjXvlMpSij71lvhBtFLkjCwRAqWrwBvd-RutRYJrD_RZws207k8ABhIUZyieUyLeNCeoSZQ4PghejFCfEMFOhxhUePAoTkAzXnk7ytqDtV9Zgu2k_mC52wmHV2s7CjTHJQhyL8OOBmNflE08tTFVRYIOHU5wSyr_7ZZxcE1uV-MuLohkP1RgyGVhGa9g1O6lhHOy9IdEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrBylk35qBk1iqRMMLpkdQFdtecj60ArseXKHc4trgKkxMvRbYn8nEmTLM3N4wVPVaHI3JVxmx-kkRW3BIrvugh8vrl0GKrhSHzBUikWX-8NkRwoglPrY6LYD96qK5ftshHiGXmgt6cgxuDA70Mk8CLcRAXYWwnyORgtApSa-3yfYbMOC1X3vRfLara21q4NjoKPxi43Rt4-dH1Bs5J85yIfiYRKDYmRnOJXRiR9CHRNf_vxPxR9Y44Y5W_sDQtfhuOExvQXvFQH1TvVPsji1za9Ca6h0AaR-wyesZLEhje_mGIjFwGUZTlzwDxiu3wFkfm4aPFDFCb1Idg3bfSQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=Ft582DgNw1bjf756hQsSk5nRZ2L1iulwLxnRkwZAS4mTugKbT_C82C2_T2fkMYNaZlAgaSqWkcwZkm701J0h5P9N1VfZVP8nso9orW9cLnrl_VvgA967XU8DRISOTrpW--XaYDJH9t9qcBNJVjlNDoxyhYYiLkAAe_KNJ0Y3Rqhz0k1gS3YrVTmGRz3jyp6dxycn180dYCM4nskiTkRnnVIRe19rnKKsVp7WVkOvaeffjRa5EnxrMXShLEJRsXBDSUQu3ClkIV5PZ87phrXNJEvGJpuxRLcKFWve1WMEjWrSMQ0bputIii4-BlWB5G14AU8afGLLCHByVJu3Ee4AZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=Ft582DgNw1bjf756hQsSk5nRZ2L1iulwLxnRkwZAS4mTugKbT_C82C2_T2fkMYNaZlAgaSqWkcwZkm701J0h5P9N1VfZVP8nso9orW9cLnrl_VvgA967XU8DRISOTrpW--XaYDJH9t9qcBNJVjlNDoxyhYYiLkAAe_KNJ0Y3Rqhz0k1gS3YrVTmGRz3jyp6dxycn180dYCM4nskiTkRnnVIRe19rnKKsVp7WVkOvaeffjRa5EnxrMXShLEJRsXBDSUQu3ClkIV5PZ87phrXNJEvGJpuxRLcKFWve1WMEjWrSMQ0bputIii4-BlWB5G14AU8afGLLCHByVJu3Ee4AZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=PyiLNPuQe9u_kAoWNr6JF1lnZDsq0jKn7SNxC1gbdIka6ViyrUcZBKrhxwJPc3EpKffE9ZxpXPeeP4_iVrnpfD9iTOaxPeVmXvLuwJPz0rmrCjE6vqzt34x6aEs-tIdvYOl9feEgPhQyXc_E8Zy_laOmGaRZBshStsTzbYgMAiby9TDFgXqQqEscKLQxfKNkn2Bz-Nhm2AIUbx6gS9Vz5WoCXaPdce4PUoOdDpoTPvokE6lPCHwvwEdsZxYCwaHCI66rgCHz2FUr6zRF6KyqfzDzXKMoGpDRDqeY0I8gbjo0nm-8difBoC_1j6InBnhPlfk0uauR5SscqvUdlLlx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=PyiLNPuQe9u_kAoWNr6JF1lnZDsq0jKn7SNxC1gbdIka6ViyrUcZBKrhxwJPc3EpKffE9ZxpXPeeP4_iVrnpfD9iTOaxPeVmXvLuwJPz0rmrCjE6vqzt34x6aEs-tIdvYOl9feEgPhQyXc_E8Zy_laOmGaRZBshStsTzbYgMAiby9TDFgXqQqEscKLQxfKNkn2Bz-Nhm2AIUbx6gS9Vz5WoCXaPdce4PUoOdDpoTPvokE6lPCHwvwEdsZxYCwaHCI66rgCHz2FUr6zRF6KyqfzDzXKMoGpDRDqeY0I8gbjo0nm-8difBoC_1j6InBnhPlfk0uauR5SscqvUdlLlx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M-GRzs8XLsThAidv_CW6R9lwmOiNalnvJ1fJzu_K9_4AObIWeAxb7uX8NP0gWYl0fA3fllK7vayM081sIQo61_kPQ9Mxm_QUycXELbKrgPPxe9auJ1SbDsRmSgp_E1To5PrXklmKfgxshJa3TWPQXw_4w-cZPIqq0q3DLfxo6XodUCKNRxEhEw7mZRxzw4N28kXsAn5HZ7_x9f6OM299vv13UCeCmhGX6JtRbGSTV1TF6MEASI1PKA6HCv9jiMnF_n8HX_OZWNVu8mWgm-0uWC0lGjsfgjD26m4o3vpmVu8bwFAuZHA0Iyh9M7qoRfl_yhWLH2aGlplImALXv-Ai1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uY_lYthQu4n_sXDsBoBE96DTEsy9cdyLfyZXaRYZUQSz_z41BPUCc116iOfEv2T-doU7fIqU-iqvUcaAj7f6luQVUykxhTJbf7eAYqDUYiwHmO4y8QOLLRzlkjCDY9ztKsTUNtPAqybClJdU5EI2xn4nWlbWZNrNGc5mdcBggEeE-2v8Nzt4afb7KyHj4SxRzkQchGXOtq-8WRasEwrM-hhA2EIKR0nhf_xrmrI0Nie0UDu1MmOyoZA3bOt-LeadLWOCdBPIqfI8pKY8aYmM--pshOawKDITxVX7SbxNCDRVMx6Go1409YIG82hE6mtqNHIQPIPWxO66pDLEU2wGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oOzExKE8UzbIfGVDcbi_gY1-WSP9zhDfBms7YgokvTV34BJ0lx3g8zmyiE3EzTYEzAyCvxRPVXEPlOmymuRR7KixvRUmcmV3YCaLiuX-wbSiiqEQ4X8KDoczm3XZxB9DQvinPiMJXQE6bKsgrrpWJYSJk9H4_QPQjarn1ho8lTFZbJd-Am5R5b_M-qVMkY10jWqNyrj_MJPM0KR7VUdojtHcy-kh0Gq3aK3xSgZFA1Ii_GDM0ZW1jytR4rFVa7UvlBYJ5QHame69tgG1u0V62CmGV9cdM1PnKIb8zZSNA1U2acXstuD3rJ7zZ0mXd15Yle8fTJQTc8ny3OK8WfDnTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=o2Gv53n0JPDaBGG1d_XvRrNTV7zc20STm_3Z7185sR83jL4Oe6wRcp1SFgQmHBBLE0BqcQ_otF6WXLctRbX7ztGA6hmWX5TEvHF7yTJFLfs1EPhkoaLbkGWPHv7XBKIQI540ps9yUsM6PUaIMcciIQjE9LJESzRxdNioPNhHGil7DjUzhqONMHo8-fIZHF6CvcDla0fho2A-bqouLD2Gb-XKCWv7UDaH4SxvKMXGhHS-mPKsftCZnaEOTvMZMOy5HclZ0XLLZOCJPL6iQMjBB-XPiXlxYhTZ65RG1iwhNLJkWUfJNoGKMvUHZJn19HksxZnDaYauo2oatc74KXK0Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=o2Gv53n0JPDaBGG1d_XvRrNTV7zc20STm_3Z7185sR83jL4Oe6wRcp1SFgQmHBBLE0BqcQ_otF6WXLctRbX7ztGA6hmWX5TEvHF7yTJFLfs1EPhkoaLbkGWPHv7XBKIQI540ps9yUsM6PUaIMcciIQjE9LJESzRxdNioPNhHGil7DjUzhqONMHo8-fIZHF6CvcDla0fho2A-bqouLD2Gb-XKCWv7UDaH4SxvKMXGhHS-mPKsftCZnaEOTvMZMOy5HclZ0XLLZOCJPL6iQMjBB-XPiXlxYhTZ65RG1iwhNLJkWUfJNoGKMvUHZJn19HksxZnDaYauo2oatc74KXK0Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkjW2rjfit4FhXVQYEsUkH8KykIwAhJcd4OA1sleg0ESrKMCIRIHeA_8Kvq7igNDJPU2ZPhLIFQ-LtRWswIk2oY8ddoI-_Q0ZZ-uX6BIKI9_Jhbp4ZftPczoKpA7aD9O0pIgK9McV-wCQ4fEvn_p65M6zsFHPDkkXfwOVesS3clKCGqwt2gYJ5u1k7lxl9wQxoK-Dbhmvb71RJtUdU6sPdH9oSsHsiU3qpkw6O3zd8Wz2zqcEIIUPVMlnBVze6vn4Z0Uo1TPGCMpD1qE3izcBcgJxllT7BEoqkV9MNfHt4sN6cf3Hxi_f2kYKEEpdns3tNVhNJUymNHEsd_TLAZMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJfTbd3L0agEcNuCrfzBbGUfYVaI_w7W2t59LdY9CaXOacvwqQEUxSDhVn1z7XY1nHyjQh6TqvtyTLrRGcvKkbYkyW7EHBZ4lTCZ1dpqXOg684G8N0hW7InDffejqHUbcMdcCKu9PuCo2Us6CVDLFW0YEeA-LrMRhJf0frjTbLn6taEbWe1VMPyGTBtf8mM-Nk9iyxKYmqCb7eA9HoGMOSv3VzABkMO91d7cfRuWUbSe2m7nNdp54oDnLjav14wLjX4z9SUat0ppajx-e115FP0s1yHYfulAaP-5KZu_1etgpb5IOld8tahO1VMju0i1MDD6ud6j-VoR2wnN6PPSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=dcJokShqckj2aDedjlfg5S77HUbZzgSc3UoAvvusHoJ7jJnMmiBBKyjboAZ7DTReMKVpxSa2iw2s1gN03qMbqrCw6ULA6cDw24Rze9wNTbJR-M1LYblYN0BJCsamUdXhnc26tafhR7IOkPH5WKlAvWgh9l2nyXqEEGVDg7JwMiL7ES21NZZCl8W_3izHKzjMRQ4wpO3rhb1J1aVj0vsfpDzgaRApTS6XGekpJ-f_g-9vRedHEfyA5hebg72kFNBAS6E_VncngBByZRrjOI2W86Ttt4BEZb9ZGAx0au3dXhFMF0zWAXNtoVrM6wu9eexMg_lwG8mUweXmpPdEkdymoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=dcJokShqckj2aDedjlfg5S77HUbZzgSc3UoAvvusHoJ7jJnMmiBBKyjboAZ7DTReMKVpxSa2iw2s1gN03qMbqrCw6ULA6cDw24Rze9wNTbJR-M1LYblYN0BJCsamUdXhnc26tafhR7IOkPH5WKlAvWgh9l2nyXqEEGVDg7JwMiL7ES21NZZCl8W_3izHKzjMRQ4wpO3rhb1J1aVj0vsfpDzgaRApTS6XGekpJ-f_g-9vRedHEfyA5hebg72kFNBAS6E_VncngBByZRrjOI2W86Ttt4BEZb9ZGAx0au3dXhFMF0zWAXNtoVrM6wu9eexMg_lwG8mUweXmpPdEkdymoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjKRAmLVUrMCL8jaDqfYLD5vL8-_3pEenHl_BDc9a6FRMR3vBtCj4gtivcn56taz3IAvYA5Kho3AQyTDlvDODkG47LjhuAglbjwtaBVQKFTiEjfjUtFO-F3pONg_0XxkF83donGSDFMXp2TeliaA7uKWNqQO5N8AJLjtadaRmk1K6M4AWHp4bSQQS3nPgQHvMd1mPLiyCoHuoWg9ywABc6JJSLXfUp_lS_s9G_EJPZDB7t0AB30bUTMo0EidgcuTpjRWrsAizzlFUy_EQijI-s7tb1xYw7wXf7aD1PkPp1YghHPyVhZUSo1jsPRGYUS7UkQmnjrskaa-ULy5Pnmw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=nVg-qeF322-jtRhKuox0OJx-UH_548TGKsXa3efBSklwSxhBs4azrhY-nANcq6lUmIxdKqMZSB1s3fEFGZ_CPLV1663-gsuKRhysVX3ZmFLhCra4BbclBPWK4bA4PvS-k9_oCVK8cFq1zdO7AhuiglJEemtAvvvjpxHGjq7bWwXWcNwBKdYZKwpMN3QiQP-DhdkRalEGFuoxdr4QxT3LX1ni9BFgmo-IGvEb5s9Q-okP6BrJdWUk1_5FU22y5ivv0Q5tI0wwKRS5Iw6zKbyd5W_ti67ioKxtN64TtBgfRvYpdJ9YEKOllExyO1mNbgPYmJIKzoR6vsmLSMbyCWRsSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=nVg-qeF322-jtRhKuox0OJx-UH_548TGKsXa3efBSklwSxhBs4azrhY-nANcq6lUmIxdKqMZSB1s3fEFGZ_CPLV1663-gsuKRhysVX3ZmFLhCra4BbclBPWK4bA4PvS-k9_oCVK8cFq1zdO7AhuiglJEemtAvvvjpxHGjq7bWwXWcNwBKdYZKwpMN3QiQP-DhdkRalEGFuoxdr4QxT3LX1ni9BFgmo-IGvEb5s9Q-okP6BrJdWUk1_5FU22y5ivv0Q5tI0wwKRS5Iw6zKbyd5W_ti67ioKxtN64TtBgfRvYpdJ9YEKOllExyO1mNbgPYmJIKzoR6vsmLSMbyCWRsSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'همین الان پایگاه نظامی بین چغادک و
#بوشهر
'
پنج‌شنبه ۱۸ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hwMFurlQdc74JM0ApEBgctx0NsUScDx0LjeIUK-u-tbRq-WcupL0rDiQSOa_-92t7h0qyRWAogs3cC80tVc2A1v9ke_pobGOwMlg75MnpepXRObuBDMR0jr2w3Hpu2tkHOVBINUQLCSa2FgDrzcDrUINi5HFMZc5nYaLLZTXEMlZYrB6yOTi8u0oEk-edNe5scwbFuLkh9f0Gxu4arEtZRMOvkzBXcwhGkNtAoQKR9Fgcf9ljvhqJtAZ6CQqw6QKuOq0jQop8R0RNCTQCdnE4LbZp1t4A2xIr5cc1lkw2hBvyuQo7mhFBDMRCl7q-YKc8LKuOBxIOVzA68nGfI80oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NBu2h-JlhE9z00f-p9aYD7dj0o8-OvYJuvwcJMzc292GHI56yr64GcgshXGJ9IYZQZZU6jLxo3wzZi3VfNiko-sXe0bEcn_-gVnWJobFT6Uo_T0RD--gUcMvOq2nMW6Tl5AMl6z5z3G5f8N16Ppl5-gSK2VnkzaKrweJwMkgOrNW-PE_rL9KNouN_CP887nsoM_OexHyvkW5JVJxXoTI6bJWQrM0Ql4AosZVT0Sr-Z9wA4ORkuVVcLH0JhanTQJ39JuFhbOukoG2uUVuh5iPmtbQzg-IBfs6pZmYZ9QJz8mk3cAolbBP_kY_H2r5m6fwlnir03Awp4UYTZdtpvslkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=YFDJat4muyv2jgozyua81rHCpFhxvqpaBUHOo6jy725v2roQSoc7pF9hs-lLvjqbPRZfJPBJDdnzUqM14cjcbnkfqvglsATK6zk52kkZKCSDLZjX8IoliTmHojW5CJ6oWBF2wPBiiibaqrswc8Hra34C5wt0clnDSiB2XKUpx9ZtmUWNPIRCBcmSv1Y8XRf5MD76DTWO6WxkWcBY30zlu0tq-rt2RGD-FDya2o5Mu-llcNpTzBJA7spjHzTB11K5GZtg2gftQ_0uqqyqBzDociDrc9TrwwsJfmUM2ORJI9s2f5nS8HP1luY-752eTqfDZHpLYOKY0SVvlP3CuI-MCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=YFDJat4muyv2jgozyua81rHCpFhxvqpaBUHOo6jy725v2roQSoc7pF9hs-lLvjqbPRZfJPBJDdnzUqM14cjcbnkfqvglsATK6zk52kkZKCSDLZjX8IoliTmHojW5CJ6oWBF2wPBiiibaqrswc8Hra34C5wt0clnDSiB2XKUpx9ZtmUWNPIRCBcmSv1Y8XRf5MD76DTWO6WxkWcBY30zlu0tq-rt2RGD-FDya2o5Mu-llcNpTzBJA7spjHzTB11K5GZtg2gftQ_0uqqyqBzDociDrc9TrwwsJfmUM2ORJI9s2f5nS8HP1luY-752eTqfDZHpLYOKY0SVvlP3CuI-MCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر بالا با شرح
#چابهار
پخش شده‌اند.
در خبری دیگر:
خبرگزاری تسنیم گزارش داده است که جنگنده‌های آمریکایی پایگاه امام علی ندسا در چابهار را بمباران کردند.
تسنیم اضافه کرده که تاکنون صدای حدود ده انفجار در چابهار و کنارک شنیده شده است.
برق قسمتی از شهر چابهار نیز قطع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=GBl0hq7F3izHBcBMHc2ayjfYd3jCgSRszvjaIJ2OkFx4Bg9PTBcoJCr2dM-dm4Mb4JdKRogXLSG-AskQygz92DlwdVP6thGSXw9MDMccs3T0fhrO1a-j_X8g_oGkus6Yul5DllBA--XOflvQ87mBhJv0QZGK0A9lFGUiTK2Lz2eIs6tWpVgetefwKB7rO9rpK8O9Yh8erQa6bK6XT7KFkcVhoGUz7iLDizAoUIo5KJKpLEoEGUhHJP51x9rDYhNTDIoRHX8WrLMj8-WvFC5XpfEk3IdsBH32_TDCiovvnhfFoE9dDS3wVs0qlgTBaxVsFckuBCljBUyUEWQS3dbxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=GBl0hq7F3izHBcBMHc2ayjfYd3jCgSRszvjaIJ2OkFx4Bg9PTBcoJCr2dM-dm4Mb4JdKRogXLSG-AskQygz92DlwdVP6thGSXw9MDMccs3T0fhrO1a-j_X8g_oGkus6Yul5DllBA--XOflvQ87mBhJv0QZGK0A9lFGUiTK2Lz2eIs6tWpVgetefwKB7rO9rpK8O9Yh8erQa6bK6XT7KFkcVhoGUz7iLDizAoUIo5KJKpLEoEGUhHJP51x9rDYhNTDIoRHX8WrLMj8-WvFC5XpfEk3IdsBH32_TDCiovvnhfFoE9dDS3wVs0qlgTBaxVsFckuBCljBUyUEWQS3dbxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#چابهار
، انفجارهای حمله ۲۳:۳۰ چهارشنبه ۱۷ تیر'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PL7KnjGYDuurKyMN6eecuZV0r5NZNeX0l_EiJAh2Eqsk1wl7yHeasLIoVVwRMOT3Z8bxXM90iB40m2gFMGork2zD5jdmYyFKciQsMQT7s0zTnlLPypy0X6YIApeKaQrCitL9RhQDB5o0X6c2OJ6jGMihSb4V7KZRhmZEYbxrRS52UcdjrR3UaSryQxF7-23lD7d8EOQAXjK8vHlwkWlTNJTCX4jRvlqdTl8gZdNUlPE_IoJZ4WV8apkezaYR8BIQ25Yi9eeyL7dSTy34_Z-FnKGRe1dezUybVM201Ji6-0oxTi71SnUz6dVb05coDs6iel6dJ4u1FpZSE5cjTNieLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=mkMDx-iynx_May3Uq_2vDw8dptB5_hZvC0H7kbBARxyu2XmHyF2doBJkvhOVxdeuMoLLsThsXupLMXcG_Cc_HzCVQLgAlF-7z-zVpfHL2qhpExs1rMZDQ_UX3t6GRVgNoNrkGjgNzUin-I35sXfLZ8iJTPgSHlA2jUIXPGgeEfPQQeDhFuN8e6RwpOPEwiHH2QRK5tRVTZd9lqX2uT8m1tWyfdVH2wjP9olNrumAsiNVKhichpsRzv_VaLgFTpNSAqkD2Pg3MUqK41K_LOzTo7LPooK5b1K0wnpm7A1cxP_x7H01PwITWdGmSI9YllnRoO0EavDF68KzaVu4eYxpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=mkMDx-iynx_May3Uq_2vDw8dptB5_hZvC0H7kbBARxyu2XmHyF2doBJkvhOVxdeuMoLLsThsXupLMXcG_Cc_HzCVQLgAlF-7z-zVpfHL2qhpExs1rMZDQ_UX3t6GRVgNoNrkGjgNzUin-I35sXfLZ8iJTPgSHlA2jUIXPGgeEfPQQeDhFuN8e6RwpOPEwiHH2QRK5tRVTZd9lqX2uT8m1tWyfdVH2wjP9olNrumAsiNVKhichpsRzv_VaLgFTpNSAqkD2Pg3MUqK41K_LOzTo7LPooK5b1K0wnpm7A1cxP_x7H01PwITWdGmSI9YllnRoO0EavDF68KzaVu4eYxpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ریاست جمهوری آمریکا درباره درگیری‌های تازه میان ایران و ایالات متحده، با تشبیه تفاهم آتش‌بس میان دو کشور به یک «معامله» گفت:‌ «توافق اولیه‌ای که ما امضا کردیم این بود که اگر آنها از شلیک به کشتی‌ها دست بردارند، محاصره [تنگه هرمز] را لغو خواهیم کرد، اما ۲۴ ساعت پیش چه اتفاقی افتاد؟ آنها شروع به شلیک دوباره به کشتی‌ها کردند.»
آقای ونس با تاکید بر اینکه در صورت ادامه شلیک به کشتی‌ها در تنگه هرمز آمریکا ایران را نابود خواهد کرد گفت: «حالا، رئیس‌جمهور ما گزینه‌های زیادی را در نظر دارد. بدیهی است که من نمی‌توانم بگویم امشب چه اتفاقی خواهد افتاد، اما رئیس‌جمهور خیلی ساده به آنها گفته است، تنگه هرمز باز خواهد شد. این بدان معناست که نفت و گاز به سمت مردم آمریکا جریان خواهد یافت. به همین دلیل است که می‌بینیم قیمت نفت و بنزین شروع به کاهش کرده است.»
او گفت که تاکید ریاست جمهوری آمریکا بر باز ماندن شریان حیاتی مهمی در حمل انرژی جهان است و «این چیزی است که ایرانی‌ها باید بدانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z4qjTtbvSBHhA2coEiLC1FOHP9qu1tDgMioWWorMtfGHYVuA3Jc52V18fgHKX8O3te4oMEBnSbnyvzwhMOsj_IJartqrhe7DuvKJHQwynJdUYWh7R0Hrn-to_pCiZLe5IwvrRngkx0EDdyXx7xRu1uwo9ocAGbGC4BTMjfNcg-7bdyGv0KEbIgTsV7BdOJJmFicaGKlwp6Vii1MDGrhxPWxiwUi4C9NQQTX-WRSpJq7izVD6IOa-0024DcpcU_sbspxqeW1iz7X7VAjiz5o3_puOt30f6GlC3yyZFCNB6m213AHIF8PJaEImG33xXK9Cx0_SqpXZLeCuyvVo0nS9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=bCn4_0dRVN_6jBQT_8_UEox2VSqc10KkQu9iHGOwaIdkhC4nDIzRZ8vyV8gyq51NWPrPht4TI3ve7FYYsTuyJ_FtSN62y31dNrVbeTjkvMjn6jq1SzWVrC3mVlMChJcaEKGNunp-ZCOO03Odi8pH5zsDffD1Yy2zC2bXTxGmom54fsYehpzpMVOUg-LQ1Wk71NrpSH0pCuc9OyBdxTo85AlH0TA8idZfkmiH6xqwaXTlRhiZS8UvFi2uT4MN9Ytf69JSIsSOkP93FhsiyCZmqmJHjyk2R5d3Ch-ODqXGjmq9QPI61Z16jy9fpP8J1Ze1PDV0sYVxeULhUyqkxqSA2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=bCn4_0dRVN_6jBQT_8_UEox2VSqc10KkQu9iHGOwaIdkhC4nDIzRZ8vyV8gyq51NWPrPht4TI3ve7FYYsTuyJ_FtSN62y31dNrVbeTjkvMjn6jq1SzWVrC3mVlMChJcaEKGNunp-ZCOO03Odi8pH5zsDffD1Yy2zC2bXTxGmom54fsYehpzpMVOUg-LQ1Wk71NrpSH0pCuc9OyBdxTo85AlH0TA8idZfkmiH6xqwaXTlRhiZS8UvFi2uT4MN9Ytf69JSIsSOkP93FhsiyCZmqmJHjyk2R5d3Ch-ODqXGjmq9QPI61Z16jy9fpP8J1Ze1PDV0sYVxeULhUyqkxqSA2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'بوشهر، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۴۵'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=tPb57wD8pIOEN4B0sPVaNMx9vT7XwW8sxgk9haYl97WRboOmf8L0OyZO8w15oHaa69bPZqXgpcW6reBsnf2kCTTDQZ9UnCFRUxzAIFkKyyq8NMZG8n6DJaUKbOf7pVqNeaMgvwC3Uj-4hG4Syw7FaLvB0H3B27Sr8jJipsv7BU4r3dSHci6uTrD9mf7bYLHcvB7GrigIWs4EZc22e5klmaX0AJliCMapNVeHb4l5ZIt0Bf0mdFhAU-Z-SHL3UX9YeIZX0llSXDYN4qZU9z1ks-z91nKNrinIvcKy_djxh-UnyQgrmfiOH3ErC1gdGlukJ2UTulcXDL98ZO77PtbSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=tPb57wD8pIOEN4B0sPVaNMx9vT7XwW8sxgk9haYl97WRboOmf8L0OyZO8w15oHaa69bPZqXgpcW6reBsnf2kCTTDQZ9UnCFRUxzAIFkKyyq8NMZG8n6DJaUKbOf7pVqNeaMgvwC3Uj-4hG4Syw7FaLvB0H3B27Sr8jJipsv7BU4r3dSHci6uTrD9mf7bYLHcvB7GrigIWs4EZc22e5klmaX0AJliCMapNVeHb4l5ZIt0Bf0mdFhAU-Z-SHL3UX9YeIZX0llSXDYN4qZU9z1ks-z91nKNrinIvcKy_djxh-UnyQgrmfiOH3ErC1gdGlukJ2UTulcXDL98ZO77PtbSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'چابهار، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۳۰'
لحظاتی پس از حمله آمریکا
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار بندرعباس
باهنر
بد داره میزنه
بندر دوتا صدای انفجار امد
بندرعباس منطقه ۴ انفجار های شدید و پشت سر هم
بندرعباس ۳ تا انفجار پشت هم 23:45
سلام الان ١١:٤٦ دو انقجار با موج بلند در بندرعباس
بمبارون بندرعباس شروع شد وحید جان
ساعت ۲۳:۴۷
اقا وحيد الان بندر عباس صدّا چند انفجار شديد كه پنجره ها لرزيدن
ساعت 11:45
چند صدای انفجار بندرعباس ساعت 23:46
سلام صدای سه چهار تا انفجار شدید بندرعباس اومد
بندرعباس الان چندین صدای انفجار پشت سر هم اومد
سلام
23:47
صدای 6.7 انفجار از دور
قشم
سلام بندرعباس صدای انفجار مهیبی اومد
بندرعباس سه تا انفجار پیاپی و مهیب
صدای بیشتر از ۸ تا انفجار این سمت باهنر و اسکله اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cpZqRbmOC0RkMQSr0QYIJPulMnwIOKQwvapeF7FV1y4jSfvq23HPE9BSs5XFqbdWIbp5b8BIip1O9AfRX0WOSV-zv8C9KBaduKxC6_h0XdzqSRKp5CtIm4v6CVYxPno9QCAcq4uiOmGfjXx5qULyWMW8nDC1TJoN7myDUc_QpArbJ5srcV320Ah65ioUgegkbGsvAY3DCDJMFJ1kGDA4LQBzattGZaZwvH0JXk8ZcAOddWZFzaJIId63-5FdN1gwHDwtRaxw9v_iNAO9uYaEubCiAROzW2eMiDlu7L1nMFe38vfg95qKm6Ze4txtr930BT3KmNzenQ3uCTt_Pz4fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
صدای انفجار چابهار
فکر کنم کنارک بود
چندین صدای وحشتناک  10تا بمب زدن
۵ تا صدای انفجار شدید اومد
چابهار
داداش الان چابهار رو هم زدن
7 و 8 تا صدا اومد
ما تو روستای رمین هستیم برقا رفت و صداش اومد خونه لرزید
سلام کنارک وحشتناک صدای انفجار اومد
چابهار زدن چند تا انفجار شدید
ما کمب هستیم واقعا درهای خونه ما بشدت لرزید
صدای انفجار از زمان جنگ هم بلندتر اومد
دود غلیظی بلند شده که تو شب هم کامل معلومه
از سمتی میاد که پایگاه سپاه اونجاست
البته ممکنه نقطه زنی باشه
الان 3 4 بار دیگه صدا اومد
جدا از اون اولیه
مجدد زدن با جنگنده
فک کنم اسکله سپاه بود چابهار بود صدا نزدیک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QHFb4FpaaSAJoMUvvsBvpQvlEsd-yWMsxGLZfa6binSv8EyhRdnubBbKA0tc9zEAlVE9ro2397VDvKT7hWKOE8jUGYXuMbQhCTfyFEnSd6coiF9hQy4VfMUBcm-Q1KmlpY5xJ_ngdTDZDMtdPYU1hFysRh1U4MGWSNRugl0T81VsX-rVNJ_5jpynIKojZ_JvFeUOfW-O4vmCfUJMtSGyqJElp2mnbYMgsMGidvp64NI7gNLkF-uVUjUTiqQ2p6pe5J1Toh-DjtkGEjAiZzAgrfmAsv571aHF4KUNildDqXTW4ZiGanTwQ6XBAXCajKIk3Mf32Jzw9Q8QZ4CFPGbf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری‌های فارس و مهر شامگاه چهارشنبه ۱۷ تیر گزارش دادند که حوالی ساعت ۱۱:۱۵ شب صدای چند انفجار در بندرعباس و شهرستان سیریک شنیده شده است.
بر اساس این گزارش‌ها، شماری از این انفجارها از سمت دریا و در محدوده ساحل غربی سیریک به گوش رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76847" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">(
⚠️
۴۰ دقیقه، ۸۰ مگابایت)
کل سخنرانی ترامپ در نشست خبری اجلاس ناتو با زیرنویس فارسی ماشین
دونالد ترامپ، رییس‌جمهور آمریکا، با اشاره به رهبران جدید جمهوری اسلامی گفت «ممکن است آن‌ها هم از بین بروند». او هم‌زمان تاکید کرد که درگیری با ایران طولانی نخواهد شد، اما واشینگتن در صورت لزوم به حملات خود ادامه می‌دهد.
ترامپ روز چهارشنبه پس از پایان نشست سران ناتو در آنکارا، در کنفرانس خبری خود از نحوه مدیریت جنگ با ایران دفاع کرد و درباره رهبران جمهوری اسلامی گفت: «آن‌ها رهبرانی داشتند؛ دیگر نیستند. حالا مجموعه دیگری از رهبران را دارند. ممکن است آن‌ها هم از بین بروند.»
او افزود: «ممکن است من هم کشته شوم، چون من هدف شماره یک آن‌ها هستم.»
رییس‌جمهور آمریکا در بخش دیگری از سخنانش با اشاره به تشدید تنش‌ها میان تهران و واشنگتن گفت: «فکر نمی‌کنم جنگ دوباره آغاز شود. آن‌ها چند کشتی را هدف قرار دادند و ما خیلی شدیدتر پاسخ دادیم.»
ترامپ تاکید کرد هرگونه درگیری احتمالی «خیلی سریع» پایان خواهد یافت و افزود: «هر اتفاقی که رخ دهد، خیلی سریع تمام می‌شود و فقط اوضاع را امن‌تر خواهد کرد، از جمله برای نفت. ما به دنبال یک درگیری طولانی‌مدت نیستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76846" target="_blank">📅 22:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOXDNFphzdHrj07GAO_E5aQHoENSsBqL40SGlbhzMEuBNHfX3qG4_5-6g7nyvWF7Bf6PweYgZN_WbDAScsHXfLEBmFkijRur5rko57ajHTBzycyIYJCGNc_DQUMx4opFgqy3wbJVpdvEzhBffY1AmDvzf3mQTGPqEQNSDyLKlNXNchWBssgTk7iuUQpHkCRyMUiBri9DbWeMvPqjYplIPA9FnDhBl1GCHDxzTespHQKeCBPbP_XsipqeGG1ZMo19fs86LCOCjtkawlM82slJno_srQbc9pr9-TM9J-Y1sRFCWmqQmDFNZ7uLHGUF9VcnNvO1XgMzCrZ1tHDglGauAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YDNOtWwDs2jZYNpK2xwCh4XaJ5imakQzL4FI50cZon4Mw0shFEvSClysnulTPtq1lz-rVDsGCVcCQmxG4nHZCxvrCY62DSXMAQaBlWDOa-kpO_jBdcG4IisJkKJqAkuypetyE5PuZzcKTm_NIM8HF6LweCUFQruu7enLXMWI4-Mkc3vkeWki5QkWgfwUh2kk-pUSMS2dtyL5r4j-wkRcsmRGotyQDNH4oD0Xtpw1XFauhMUzukcvsAyZu2HQBu56PEk-JP8XSHrF7p3FBVjPPxt5gcXbxnA7Q34R1lxeJpg9yBlRggKSTh-CR2VWCstBrgK9CR0QD9sp62AiTLfNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=vPp4jZAjw9cmWPvrqpe2Qd_wle2-HMZhi-gKrR5LkhGy8CIhW7QwUIm-kKLYR2Y0MNOBeKcwsWn8LdWiMCBRO9hbuM_opibJmkb34IgiQ1GpHW17yJRz8Ji04oICt_avtu7Uq-albBZXp3ksX5vY8-Nd8D7ksID7pc68Ps7jmYDy-NbplA8PVha4-0UlBhrx2E9eW2rHTXIuqJZkAQ_t6E74xSAAj8gHazLCvOi6lWiI4sQLH-aIRLzTJfUmGB399ZU0jcOkjsVjnQBwnT5EPMeA4uNBHMOlVIqSARr_bF5E60mc8cnpAWJnDLF7Mum2kQbm3cFlUfWG8Dxr-E6X7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=vPp4jZAjw9cmWPvrqpe2Qd_wle2-HMZhi-gKrR5LkhGy8CIhW7QwUIm-kKLYR2Y0MNOBeKcwsWn8LdWiMCBRO9hbuM_opibJmkb34IgiQ1GpHW17yJRz8Ji04oICt_avtu7Uq-albBZXp3ksX5vY8-Nd8D7ksID7pc68Ps7jmYDy-NbplA8PVha4-0UlBhrx2E9eW2rHTXIuqJZkAQ_t6E74xSAAj8gHazLCvOi6lWiI4sQLH-aIRLzTJfUmGB399ZU0jcOkjsVjnQBwnT5EPMeA4uNBHMOlVIqSARr_bF5E60mc8cnpAWJnDLF7Mum2kQbm3cFlUfWG8Dxr-E6X7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری فرانسه، چهارشنبه در حاشیه نشست ناتو در پاسخ به خبرنگاران گفت حملات جمهوری اسلامی به پایگاه‌های آمریکا در خلیج فارس، توافق موقت را نقض کرده و تهران در انجام این حملات اشتباه کرده است.
امانوئل مکرون در عین حال گفت انتظار دارد نشست‌ها در چارچوب آتش‌بس ۶۰ روزه میان آمریکا و جمهوری اسلامی ادامه یابد.
@
VahidOOnLine
فریدریش مرتس، صدراعظم آلمان، نیز در حاشیه این نشست گفت: «ما به دونالد ترامپ گفته‌ایم که باید یک توافق پایدار با ایران حاصل شود، اما این ایران است که مسئول آخرین نقض توافق موقت آتش‌بس است.»
@
VahidOOnLine
دبیرکل ناتو، حملات تازه آمریکا به مواضع جمهوری اسلامی را «کاملاً ضروری» خواند.
مارک روته، پیش از نشست سران ناتو در آنکارا به خبرنگاران گفت وقتی آتش‌بس برقرار است و جمهوری اسلامی «عملاً آن را نقض می‌کند»، واکنش قاطع آمریکا اهمیت حیاتی دارد.
روته روز سه‌شنبه نیز گفته بود هرچند جمهوری اسلامی در حوزه موشکی و هسته‌ای تضعیف شده، ناتو همچنان باید نسبت به تهدیدهای آن هوشیار بماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DRNYO99rbI7GVvLvVldY0DxieqS7xEU0MPmnQf0aJo_DVZBbapJM1wFq1Wz42EY4MNhKnIl-M8EcsoGjLQpMjf_EJiqN7fseNZSN-S_Itna-IPKT3mISt6NdS5Lv2Qnt-m_X9tJ-NzWl6--2QoCcHJGhvSvLqWNpmvamU3DLHPrPgO8RNpJpVV7J0DQVFGGt4L9mI_geD57Aiw_r493SuCmevAKoR5Gwi2R2lZi1Usrr3VVH0QRWM86fdh-m3yP6z1qrKD0SZ466uyaWrTGuMeRIDf9F3am4T3xSihSs2by3-mH3EmV76WWN0A_SoFcofF6gQfK8hK_r9iO1un-qEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Egw3faPLL3RKC4bnjdC5k9lBXDu7TdltMpK1BYmeTVfbv17Ijd-uzmwlsilAjBrBrYAE7QUMggS7JozbvWZN1wRRd06qZR96BOfPpo2QfN8U_0t-CZdMqsM_NEPipEjLINdAWLfqbA3aVMYd9NRH05fUDN5ijwVXs7QbtHUuTnpIfNhJpmcDfQQ0VSMMlsL-LWTtlZ67499YQEF1fxAnA_VD38n1x3XgvHCbreU2yLm0l3xrzeoxHQScnX7ONH7HG_Uwvqm9GYzdlM502MKiVb_9DZhk6eZs_IS1pJ_KyM0aNjw1QLUWPUKmg5G0Ne3PGYZ3lWkjERFRUHWhy6G5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t5lTw36SycYdL-pjV2HtUDsEpAMfDXq9u7wVC6SC-iVdM2orPZ_rnQT_Thw3WL2pBI-BsdAQWHFtF6vb_u1E1rQ7bPxVnbTyjTwt6StonpaDcpxZ6JBPI0hs1TuSW0K1YmWl07F_yRiZrfrYkt7swCundf5bFfSlCLhoCISmuYXS8xpmAT3Ins9CxMqQxDHPG0ppit7wU5d-WIiQKojXfC0dy-DdNrwHeeIxB1AGeRoTCoIVdGE1pzWdZ1AlO_X6swhtU6VrMKjeVONBzFcGdg4mNWNeJDxeLHsguebKdXdZhxvBxch9GO65Ts8bngtCcUfk-0_AE52Mfjubg7CkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YJy4j9PtaWNZObhwcZFczhk7PDP_rf9Krxt0N51Cu0TLAiw-7mrDIuKxxD2WIpUaLBR0T1dGqdUbNvwMv7l3Azwvek1DygT7ShgFYUFKgi1S2SmXjcpsWubOM1hQnHLckmEzo_uI9USsk6uu0QUJ5JUxtUCF2S7Np2edJq3inf7AbOLNqvCgZfhulvW9TLaVyqXg87cQUfj-zt85OSnzpiUrAPGYbm9ZRqLdEiumchPNefO_qcpNE-jM8brEiPqDf7mSgOohXqDjHY-w8JnzCKEaGsEPEEr6TWuckwl6QzxCPVweKQlxU8eiveYNimfXpf0YGmzzBf4DSQc77-tLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SseF7byishuRgKNsbsFZjfZ28YjCXIyI3KS0HPkHWxr5spugL--5N_4i3W2aopiJg7tO4_iLKtPRO0ae80u2Vy35vK2fxvNZbhZnGseFDLTWJHhNVE4X28zpyF4mdsYT0EIYZ8EgI0Dd5_1MrapyMy6VstBOwceWN84DRV0X2bm7DQxc2DKuNVCNKmfjLOUIHcVseIxb3miSA0W6AvbDUxk1MZwSxEHSamWnMveNFJIj4xHaR65Eod6fw0hzMNSj98GsvW5Eml0YYv-Gu3j5W-wCzOFRGs02bLKMWBHCIhPaIQFyuY1JOCK-IkUt9kvHdOMWAj7pGN2XgNi9X0O7Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=v6zqsMkxKUOAQTzGKZ8AkL4C3hxfYLC2_OPfpHrFQLwIvKrl_bbXQXgHH796QmGxoadNWA9aM_SGSllncmi_8svB8N1IYqE7Z-pTvBA4O7eQgvvfIyR1NX87mPAuH2AZMhoUEgRJJv72221LOTTlqnunf7e7aE8NOZ3OYVOExPVCRSwIoxjEy_9UW17p_Ey2nZFMl6UOko_x9M5Vha1s63gjv09R2teYJ0pNB6_IXbtBsPm9IPGaT4EOJ-4ygNmnffdgwiKlg9ZW1iWNmmlrnQAb_DmCGQLRLIOBabtPY2CwgreO73mlsemzf9jOpG6eyxDiiJw68nIgXFYoSFvc6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=v6zqsMkxKUOAQTzGKZ8AkL4C3hxfYLC2_OPfpHrFQLwIvKrl_bbXQXgHH796QmGxoadNWA9aM_SGSllncmi_8svB8N1IYqE7Z-pTvBA4O7eQgvvfIyR1NX87mPAuH2AZMhoUEgRJJv72221LOTTlqnunf7e7aE8NOZ3OYVOExPVCRSwIoxjEy_9UW17p_Ey2nZFMl6UOko_x9M5Vha1s63gjv09R2teYJ0pNB6_IXbtBsPm9IPGaT4EOJ-4ygNmnffdgwiKlg9ZW1iWNmmlrnQAb_DmCGQLRLIOBabtPY2CwgreO73mlsemzf9jOpG6eyxDiiJw68nIgXFYoSFvc6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت ارتش این کشور احتمالا امشب دور تازه‌ای از حملات علیه اهدافی در ایران انجام خواهد داد.
ترامپ پیش از دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با اشاره به حملات جمهوری اسلامی به شناورها در تنگه هرمز گفت: «آن‌ها چند پهپاد و یک موشک به سمت شناورها شلیک کردند، در حالی که این شناورها حق داشتند در تنگه هرمز حضور داشته باشند. به همین دلیل دیشب بسیار سخت به آن‌ها حمله کردیم.»
او افزود: «احتمالا امشب هم بار دیگر حمله بسیار شدیدی انجام خواهیم داد. فقط کمی از قبل به آن‌ها هشدار می‌دهم.اما باید ببینیم در نهایت اوضاع چگونه پیش می‌رود.
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، با تاکید بر نقض مداوم آتش‌بس از سوی جمهوری اسلامی، گفت: «آن‌ها هرگز تحت توافق ما به سلاح هسته‌ای دست نخواهند یافت. اما نمی‌دانم اصلا توافقی در کار خواهد بود یا نه؛ شاید این مسئله را بدون توافق حل کنیم.»
ترامپ گفت جمهوری اسلامی «هر روز» آتش‌بس با آمریکا را نقض می‌کند.
او افزود: «آن‌ها دروغ می‌گویند، تقلب می‌کنند و آدم می‌کشند.»
ترامپ بار دیگر از توافق هسته‌ای دوران ریاست‌جمهوری باراک اوباما انتقاد کرد و آن را «یکی از بدترین فاجعه‌ها» خواند.
او گفت: «توافق ما دیواری در برابر دستیابی به سلاح هسته‌ای است، اما توافق او [باراک اوباما] جاده‌ای به سوی سلاح هسته‌ای بود.»
@
VahidOOnLine
رئیس‌جمهور آمریکا با انتقاد شدید از مقام‌های جمهوری اسلامی آنها را «بیمار» خواند و گفت ما به آنها گفتیم بروید و مراسم تشییع جنازه خود را انجام دهید. آنها به جای آن، دیروز شروع به شلیک موشک به کشتی‌ها کردند.»
دونالد ترامپ که در کنار مارک روته، دبیرکل پیمان آتلانتیک شمالی، ناتو، در آنکارا با خبرنگاران صحبت می‌کرد با اشاره به حملات هوایی شب گذشته اضافه کرد: «ما هم دیشب ضربه سختی به آنها ضربه زدیم، خیلی سخت.»
@
VahidHeadline
ترامپ گفت: «آن‌ها درخواست یک وقفه کردند. می‌خواستند برای مراسم تشییع جنازه خامنه‌ای بروند. من گفتم این فرصت را به آن‌ها بدهید. و آن‌ها دو موشک شلیک کردند. منظورم این است که این دیوانه‌وارترین کار بود.»
رییس‌جمهوری آمریکا افزود: «ما می‌توانستیم آن‌ها را بکشیم؛ بنابراین فکر می‌کنم باید از این زاویه هم به موضوع نگاه کرد.»
او همچنین گفت جمهوری اسلامی درخواست کرده بود که آمریکا آن‌ها را نکشد و افزود: «ما گفتیم قرار نیست شما را بکشیم. هیچ کاری نکردیم. در واقع، ما امنیت آن‌ها را هم تامین کردیم.»
@
VahidOOnLine
ترامپ در جریان نشست خبری در آنکارا، جمهوری اسلامی ایران را به اشتباه جمهوری اسلامی «ژاپن» خواند. او بار دیگر اشاره کرد که در جریان جنگ، جمهوری اسلامی ۱۱۱ موشک به سمت ناوهای هواپیمابر آمریکایی مستقر در منطقه شلیک کرده است. فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از این اعلام کرده بود که این موشک‌ها رهیابی شده یا به هدف نرسیده‌اند.
@
VahidOOnLine
ترامپ گفت که حملات اخیر ایالات متحده به ایران «تاثیر فوق‌العاده‌ای» داشته است. او گفت که در این حملات، سامانه‌های راداری که تهران در حال بازسازی آن‌ها بود، منهدم شده است.
ترامپ هشدار داد که آمریکا می‌تواند تنش‌ها را بیش از پیش افزایش دهد. او گفت: «تاسیسات تولید برق، نیروگاه‌های برق... اگر مجبور شویم، آن‌ها را از کار می‌اندازیم» و افزود: «تاسیسات آب‌شیرین‌کن... اگر لازم باشد آن‌ها را هم هدف قرار می‌دهیم. دلم نمی‌خواهد این کار را انجام دهم.»
او همچنین اظهار داشت که ایالات متحده می‌تواند جزیره خارگ، جزیره‌ای با اهمیت استراتژیک در سواحل ایران را «تصرف» کند و گفت که در آن صورت، ایران «هیچ کاری» نمی‌تواند در برابر آن انجام دهد.
@
VahidOOnLine
ترامپ گفت جمهوری اسلامی «هر روز توافق را نقض می‌کند» و به همین دلیل آمریکا «چاره‌ای جز ادامه حملات» علیه ایران ندارد.
ترامپ با اشاره به توافق آتش‌بس، گفت: «آن‌ها هر روز توافق را نقض می‌کنند. دروغ می‌گویند. تقلب می‌کنند. مردم را می‌کشند.»
رئیس‌جمهوری آمریکا همچنین با انتقاد از دولت‌های پیشین ایالات متحده افزود: «در ۴۷ سال گذشته هیچ رئیس‌جمهوری کاری در برابر آن‌ها انجام نداد.»
@
VahidOOnLine
ترامپ بار دیگر تاکید کرد که ذخیره اورانیوم با غنای بالای ایران، تنها به‌وسیله تجهیزات آمریکایی قابل استخراج است. ترامپ با اشاره به حملات تابستان سال گذشته، یادآوری کرد که این مواد زیر آوار تاسیسات و زیر کوه باقی مانده است.
رئیس‌جمهوری آمریکا، با تاکید بر این‌که نیازی به اعزام نیروی زمینی به ایران نمی‌بیند، گفت: «وقتی که آن‌ها کاملا از بین رفته باشند یا توافقی حاصل شده باشد، برای خارج کردن مواد هسته‌ای می‌رویم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YFYEMFCEbGx8BpgDIx1m7Lu-_9DI67M5faEMWDee0Oq9F8XilOi3LrZKRKyMBDAKD1_J4ykb-mXLuJS0GMT8tkRbpcY6KmtrrjU0tPrY1WJ2VTpdEdk9kJ-w70Y2Y8sHc1U1yWiHG68x6UYlSZAXeQpeE5WM9xYuWVMYzbojUFZlusb-H_4qjd-MPC9qCRJZ45Ssb9vEIBE_6LCDaFH-EwE6mIyK3n3gKNfy0EUcC1_Wg94pJAMpQyfiRlfm8AgvLjmpUxnqXvA1VY015JY3pj1dwaHFKa3DJX5KwZ-aWgPsmI2T4RZz_JAh9DuPWQdanQ206ZbMSFfV5uRvsLAXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل هم‌زمان با گذشت شش ماه از سرکوب خونین اعتراضات سراسری دی‌ماه ۱۴۰۴ در ایران اعلام کرد با توجه به این‌که در ایران «هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد»، دادخواهی قربانیان این سرکوب باید از مسیرهای عدالت کیفری بین‌المللی «به‌عنوان اولویتی فوری و غیرقابل مذاکره» دنبال شود.
دیانا الطحاوی، معاون مدیر منطقه‌ای خاورمیانه و شمال آفریقای عفو بین‌الملل، در بیانیه‌ای که این سازمان روز چهارشنبه ۱۷ تیرمنتشر کرد، گفت: «با گذشت شش ماه از زمانی که نیروهای امنیتی ایران طی دو روز، هزاران زن، مرد و کودک را به‌طور غیرقانونی در سراسر کشور کشتند، ناتوانی جامعه جهانی در برداشتن گام‌های مؤثر برای پیگیری عدالت بین‌المللی غیرقابل توجیه است.»
الطحاوی افزود: «این بی‌عملی به تداوم چرخهٔ سرکوب مرگبار کمک می‌کند؛ چرخه‌ای که در آن بازماندگان و خانواده‌های قربانیان از عدالت محروم می‌شوند و زمینه برای وقوع جنایت‌های بیشتر فراهم می‌شود.»
این مقام عفو بین‌الملل همچنین بار دیگر هشدار داد که تلاش‌های دیپلماتیک برای دستیابی به توافقی میان آمریکا و ایران نباید باعث نادیده گرفتن نقض گستردهٔ حقوق بشر در ایران شود.
به‌گفتۀ الطحاوی، مقام‌های جمهوری اسلامی تاکنون هیچ هزینه‌ای بابت استفادهٔ گسترده و غیرقانونی از نیروی مرگبار علیه معترضان نپرداخته‌اند و همین مصونیت از مجازات، آن‌ها را در تهدید به سرکوب‌های خونین بیشتر جسورتر کرده است.
به‌گفتهٔ سازمان عفو بین‌الملل، «با توجه به این‌که در ایران، به‌دلیل بحران ساختاری مصونیت از مجازات، هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد، باید مسیرهای عدالت کیفری بین‌المللی به‌عنوان اولویتی فوری و غیرقابل مذاکره دنبال شود».
سازمان عفو بین‌الملل در بیانیه‌اش بار دیگر از جامعه جهانی و کشورهای عضو سازمان ملل خواسته است بحران حقوق بشر و مصونیت از مجازات در ایران را در صدر دستور کار خود قرار دهند، از ایجاد یک سازوکار مستقل بین‌المللی برای تحقق عدالت در مورد ایران حمایت کنند و از شورای امنیت سازمان ملل بخواهند وضعیت ایران را به دیوان کیفری بین‌المللی ارجاع دهد.
ماه گذشته، رئیس سازمان عفو بین‌الملل نیز نسبت به تداوم سرکوب داخلی در ایران ابراز نگرانی کرده و هشدار داده بود توافقی که صرفاً به‌طور موقت جنگ را متوقف کند اما حقوق بشر را نادیده بگیرد، خطر آن را دارد که به پوششی برای تداوم مصونیت از مجازات، اشغالگری و سرکوب تبدیل شود.
عفو بین‌الملل می‌گوید توافق ایران و آمریکا، موسوم به «تفاهم‌نامهٔ اسلام‌آباد»، تنها در صورتی می‌تواند به صلحی پایدار منجر شود که حفاظت از حقوق بشر، پاسخگویی عاملان نقض حقوق بین‌الملل، جبران خسارت قربانیان و تضمین عدم تکرار این نقض‌ها نیز در کانون توجه قرار گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BtrUc12bB6e07VKjageg0TfL56klrcqp6ewRwlo7nw46IOxz_DcJ8dMOKY_N1KsyxSebV5B7vVh5JsUnGldg5WbUbM1ds5oJvUKnPHPe9b0s7LPxD6mpws1QLztzsAU9JfsrWnZGlnQkME7jBgxmU0ORWmxFQXshdeltzIeOXR9SmvAuBjp3wiAljumPCgk6Qq9arsinXlGe95D_jiIAPBHN1fTl2Jeh2mcQK7Gr2qstmdSGlEVajzZcE6dV17_nUSvmjXPrbmgknD7oo_7O6dgSjq4V-WRAclaTAcm_VDn0eZI6HNf6eZJLOoedPlzWDu_YllYku1QFGqucc2hWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/shZDE2O_SkUihRDguf1JoHYLqWVOukUaQOgxnuVBri7r03MSkDF0TpDNCYclKDBu3i99EGGIEHCa2bQAC08RdFW2mN_Akpmq5ttZqxsDoPpYZPhHvxFNQzuaGP6ERgtFlPYKNyCathwdESkswTC5n0kmsaJa_Ve6UfKhLpzz0iicNr0IScMeRvu6JZDIRiBEyBlsWBL99NwENMwREFuuGNZabynpdQ5j_cym5TpO75lKW3qzXNlGTSAY0AnUiG4RVdZLyUPraKllJwsUyb3zRKYrBuxl02sF22Pqo_qnhzPTxBgWNoWewGFd8MAvLzlxh86x_5Fk4p7rItRBOWIOxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با اشاره به مراسم دفن علی خامنه‌ای، گفت جمهوری اسلامی به جای حرکت به سمت کاهش تنش، حملات موشکی به شناورها را آغاز کرد و آمریکا نیز در پاسخ، حمله‌ای گسترده علیه جمهوری اسلامی انجام داد.
ترامپ که در دیدار با مارک روته، دبیرکل ناتو، در آنکارا سخن می‌گفت، اظهار داشت: «ما گفتیم بروید مراسم تشییع خود را برگزار کنید، اما آن‌ها به جای آن، دیروز شروع به شلیک موشک به سمت شناورها کردند. به همین دلیل، دیشب بسیار سخت به آن‌ها حمله کردیم.»
رییس‌جمهوری آمریکا همچنین جمهوری اسلامی را «بیمار» توصیف کرد و گفت: «آن‌ها بیمارند. یک مشکلی دارند.»
ترامپ افزود حملات آمریکا «۲۰ برابر شدیدتر» از حملات تلافی‌جویانه ایران بوده است و گفت: «باید سرطان را از بین برد.»
@
VahidOOnLine
مارک روته، دبیرکل ناتو، در نشست خبری مشترک با دونالد ترامپ، رییس‌جمهوری آمریکا، در آنکارا، از حملات شبانه آمریکا به جمهوری اسلامی حمایت کرد و گفت این حملات «کاملا ضروری» بوده است.
روته با اشاره به حملات آمریکا افزود: «این یک پاسخ بسیار قوی بود و من در این موضوع با شما هم‌نظر هستم.»
دبیرکل ناتو همچنین از مواضع کشورهای اروپایی از عملیات نظامی آمریکا علیه جمهوری اسلامی دفاع کرد. او این اظهارات را در واکنش به انتقادهای ترامپ از برخی اعضای ناتو، از جمله بریتانیا و اسپانیا، به دلیل محدود کردن همکاری نظامی با آمریکا مطرح کرد.
روته گفت: «می‌دانم که شما درباره ایران ناامید شده‌اید، اما به نظر من این‌ها مواردی استثنایی هستند.» او افزود: «پنج هزار هواپیما از فرودگاه‌های اروپا در حمایت از عملیات «اپیک فیوری» به پرواز درآمدند و اروپا به سکویی بزرگ برای نمایش و اعمال قدرت آمریکا تبدیل شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=rcyOuhCxAymWVVxgWNgY2YThH_8LfCHXrsJYPECAHAk95j8CS_MZ0UwuqBXwe-fh1kTE5eUezfDIMrCgRKILv5quCdB_Jyay1SHKWvCKlDVs9-wffsZpWiUEcey7skZDVWwiYakR5oA-4Lufal0mjx7PtxYDy1xCsg5dFAyWw3gJjVmP9Cd3Alm-gBhqTYjgZ-UKuQkgyc0TYzd6v-7DCotls1i4-egZvNHgv2YRnZIJqh8E_xFxQ-_VJmqCXe87tyI6gG7vnocAO16jisdjojxpDcxKB2MAPyYinmi3748HLWOZZUV2DlwIhhvq7fwCZvooPRp5zuYOGvrP1v3aBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=rcyOuhCxAymWVVxgWNgY2YThH_8LfCHXrsJYPECAHAk95j8CS_MZ0UwuqBXwe-fh1kTE5eUezfDIMrCgRKILv5quCdB_Jyay1SHKWvCKlDVs9-wffsZpWiUEcey7skZDVWwiYakR5oA-4Lufal0mjx7PtxYDy1xCsg5dFAyWw3gJjVmP9Cd3Alm-gBhqTYjgZ-UKuQkgyc0TYzd6v-7DCotls1i4-egZvNHgv2YRnZIJqh8E_xFxQ-_VJmqCXe87tyI6gG7vnocAO16jisdjojxpDcxKB2MAPyYinmi3748HLWOZZUV2DlwIhhvq7fwCZvooPRp5zuYOGvrP1v3aBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات ج.ا: یک مشت آشغال هستند!
نقل زیرنویس، ترجمه ماشین:
سؤالی دارید؟
ـ آقای رئیس‌جمهور، آیا آتش‌بس تمام شده؟ آیا آتش‌بس پایان یافته؟ آیا تفاهم‌نامه مرده است؟
سؤال بسیار جالبی است.
از نظر من، فکر می‌کنم [تفاهم‌نامه و آتش‌بس] تمام شده. دیگر نمی‌خواهم با آنها سر و کار داشته باشم. آنها تفاله‌اند. می‌دانید تفاله یعنی چه؟ آنها تفاله‌اند. آنها آدم‌های مریضی هستند. رهبرانشان آدم‌های مریضی هستند و آدم‌هایی شرور و خشن‌اند.
دروغگو هستند؛ ما توافق می‌کنیم. و اگر من با او توافق کنم، یعنی توافق داریم. و او بیرون می‌رود، حرف می‌زند. ما توافق می‌کنیم. همه موافقت کرده‌اند: هیچ سلاح هسته‌ای. ما توافق می‌کنیم. آنها بیرون می‌روند و با رسانه‌ها حرف می‌زنند. می‌گویند ما حتی هرگز درباره‌اش حرف نزدیم. یک جای کارشان ایراد دارد. آنها دیوانه‌اند.
آنها دروغگو و متقلب‌اند؛ مریض‌اند. آنها به مردم خودشان آسیب زده‌اند. تا همین حالا ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید وقتی مردم می‌گویند چرا آنها حکومت را سرنگون نکرده‌اند، نمی‌توانند سرنگون کنند، چون مرده‌اند؛ آنها را کشته‌اند. کسی سرنگونشان نمی‌کند.
آنها اسلحه ندارند و طرف مقابل مسلسل دارد و آنها را می‌کشد. رسانه‌ها این را گزارش نکرده‌اند.
اما آنها آدم‌های بدی هستند؛ آدم‌های بدی هستند. و صادقانه بگویم، نمی‌خواهم وقتم را با آنها تلف کنم.
حالا می‌گذارم مذاکره‌کنندگان فوق‌العاده‌مان اگر بخواهند به گفت‌وگو ادامه دهند، اما من چنین چیزی نمی‌بینم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KaifGabUUvSD6KI02hJyRQ3ukIjlfdvjWtsOozuMGOh9nGhddIMuZM9yFMBQ-hm-v_NRxGCHZC5RjiDkE_8-GU3u1aGmRf8jXoY3JGgw0McpFKM4mNWhzKOGB_b5biurHduOklKUXwovgqkT2-wBc1ZFhz5VPqdcoXXVj9p_b6peD8L5xpUmbCDoHkLqi6eiXmDK_XjY5QV1A4iDNNEzRWd4GzMYZ2yRGTRXgrzAE1W5Raz6-qIgEREZfRwPrgh0rMF6i0navmZAPrMoFZ27Nt8DY0xUuWWBfL27H8vT6KgaILEluKwmUyQEQ-D1wdohgR847IOiJRHMlQHNm1Lc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
الان زد بوشهر رو ۱۰:۴۱
سلام وحید جان ساعت ۱۰۴۰ صدای انفجار شدید در بوشهر
سلام وحید همین الان ساعت ۱۰:۴۰ دقیقه صدای دوتا انفجار شدیدی توی بوشهر شنیدیم
سلام وحید الان بوشهر رو زدن فکر کنم پایگاه هوایی بود دوبار صدا اومد
بوشهر پنج تا شش تا صدای انفجار سمت پایگاه هوایی و دریایی ارتش
بوشهرو الان دوباره زدن
بوشهر یه بار حدود ۱۰:۳۰ دوبار زدن یه بار هم حدود ۱۰:۴۰، بار دوم نزدیک‌تر بود
ما پایگاه هوایی بوشهر هستیم
حدود ساعت ۱۰.۴۰   دو تا صدای انفجار اومد
دو سه دقیقه پیش هم دوبار
به نسبت انفجارهای روزهای جنگ معمولی تر بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/meI0Vfa2yvqP0f7WcYF3lcKE35_ovwVyS6xV0YVg3yDCxqUnU7SJ6Yf0_FxAU8XpaL_sAru7bvKfkwDwEglJeCobc4grGelSci8wMOqSiuUAGl4ZPe2cXTBSSSkaW1FApJwkGoZ3ej_d0qbT3TWXiaXJoI2KPP7zLM-6IhVLIzwVgk1NgaiCBx9bEKL5C_yIij4RfrvhlKc8MCkef-n4HoDIuXbabNirmENCxTpmle7QLk2u-KHq-V5cwBTrZO0tokwKKVr4_XvYulESQnd-VrqSFjTAlY6qFNrhEJhHfyqep-4GUPHJ0Hr350iV_q82BDYFCRfChbUHRFqF85Oa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پاسخ دادیم
منابع حکومتی:
پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
🔹
به دنبال حماسه سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقه تاریخ ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقه پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
و ما النصر الا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwLT7OFEotnv_00tvZGwiMMCqjtIqQcqWtyGfB9sxBlISL39y2DMLTN0h6Uo3AV-9oQAQtOuckYMxcg-ehPv8AENA5yroCNsX1BNeBdzKOp8glIdMVU9ljoKJHF3BP3NgJlmlRuc71ZCVev34t4myLlfdPthO4rXSdwN9lYBeyQZW-fN3omVOjE7oLSDUgI89WyEksrB_P55ovsrmyH8WUeeTRNP2lJxdyR387PJzDz5AJotEQl2_9GnComKPFp8wYlf5fNyRPT6AQkv5Lb6_accyuwcXzyRv88JOyxtpNJ7eNh559nOAbFPwj3qBDmCwISDoo0CAsXSWRzUPRNGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شوری اسلامی پس از حمله‌های بامداد چهارشنبه آمریکا به اهدافی در جنوب ایران در واکنش به حمله‌های دو روز گذشته سپاه به سه کشتی در نزدیکی تنگه هرمز در پیامی به زبان انگلیسی در اکس نوشت: کلیدی‌ترین موارد نقض تفاهم‌نامه ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگه هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار حمله‌های اسرائیل به لبنان
او در ادامه این پیام نوشت: «دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید، ما اهل کوتاه آمدن و عقب کشیدن نیستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHKzIS7JcZvEoeowbWaWlaDURBAwQ-kgjLWrPx7gfSk5P0_9qPInPUraGB_wiS9wuEb784omS8dDQ640TK9rmWfE-4566K-IMM5ry1vnXK-2iCgvuosCzuGAxyGMWp0BbFX3yd5K4rSu3hrIMQ58ANJQCAyjGlGK_SQB0xAkaTguz3wvthysxMpVdGFr6tcPQ3c3w6p3zVUOs6dzCGg5zyrsIRhoGm3btGeVMxQmp5QeZGF0zyN2pAt423m8bIqcngw_VL3D3etjamBKMS1QyUW2NIhHZ0EPGH1hRczHmlO5kAMDD1BsGQt8TxpeNJi-PCVAe65WxwyWeCAt7gVCkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت ۶:۲۷ چهار تا موشک داراب شلیک شد وحید
موشک پرانی همین الان داراب فارس
+ کلی چندی پیام مشابه دیگر از داراب و هم‌زمان پیام دریافتی درباره آژیر در بحرین:
Sirens again in Bahrain for the 2nd time just now
آپدیت:
ارتش کویت: پدافند هوایی در حال مقابله با حملات موشکی و پهپادی است
ستاد کل نیروهای مسلح کویت بامداد چهارشنبه اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
در بیانیه ستاد کل ارتش کویت آمده است: «اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات دشمن توسط سامانه‌های پدافند هوایی است.»
ارتش کویت از شهروندان و ساکنان این کشور خواسته است دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76824" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=axFVjYOhlcER1KXSgDQZ591Re1yUUW8mxE4q-cwmqfGR7Q5nBhUeZcYh7hFBMuYzP-u23G-Q9cHfwO4zKXqvsBrLWUCi_FkjYfu_tNYlx4wnidW0Z3fBcB3tmTYlZdBVtHe7t6bPd8EgCWNgbiA5wMxzNjt6KPQyhNF9Ur-mWtQ9IHKvyEKdUdc2lGpPKIcTY6lqIUsGZON4ERcrwQpnompIVv9EHO0lMqF2azog8WkwhGcdpeN6zk-VYTZn4fWB7UxZT90Oqh5PEfNipYxvu-cb020daKIcuGTotzu33-8c8qUqA2bDY5DAibz4vgiP_x-mXqJHPilcgjnUfPjI5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=axFVjYOhlcER1KXSgDQZ591Re1yUUW8mxE4q-cwmqfGR7Q5nBhUeZcYh7hFBMuYzP-u23G-Q9cHfwO4zKXqvsBrLWUCi_FkjYfu_tNYlx4wnidW0Z3fBcB3tmTYlZdBVtHe7t6bPd8EgCWNgbiA5wMxzNjt6KPQyhNF9Ur-mWtQ9IHKvyEKdUdc2lGpPKIcTY6lqIUsGZON4ERcrwQpnompIVv9EHO0lMqF2azog8WkwhGcdpeN6zk-VYTZn4fWB7UxZT90Oqh5PEfNipYxvu-cb020daKIcuGTotzu33-8c8qUqA2bDY5DAibz4vgiP_x-mXqJHPilcgjnUfPjI5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: بیش از ۸۰ هدف نظامی را با مهمات هدایت‌شونده هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده آمریکا (CENTCOM) روز ۷ ژوئیه دور تازه‌ای از حملات تهاجمی علیه ایران را تکمیل کردند و در واکنشی فوری به تازه‌ترین حملات ایران به کشتی‌های تجاری در حال عبور از تنگه هرمز، بیش از ۸۰ هدف را با مهمات هدایت‌شونده دقیق هدف قرار دادند.
نیروهای آمریکا سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های رادار ساحلی، توانمندی‌های موشکی ضدکشتی، و بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را در تنگه و اطراف آن هدف قرار دادند تا توانایی ایران برای ادامه حمله به تجارت بین‌المللی در این گذرگاه تجاری بین‌المللی را تضعیف کنند.
ایران اخیراً به سه کشتی تجاری در حال عبور از تنگه حمله کرده است؛ از جمله M/T Al Rekayyat با پرچم جزایر مارشال، M/T Wedyan با پرچم عربستان سعودی، و M/T Cyprus Prosperity با پرچم لیبریا. این تجاوز بی‌دلیل از سوی نیروهای ایرانی نقضی آشکار و خطرناک از آتش‌بس است و آزادی کشتیرانی را تضعیف می‌کند.
نیروهای سنتکام در موضع آمادگی باقی مانده‌اند و آماده‌اند هر زمان که توافق رعایت یا اجرا نشود، ایران را پاسخگو کنند.
CENTCOM
قرارگاه خاتم‌الانبیا: پاسخ کوبنده می‌دیم
خبرگزاری رسمی جمهوری اسلامی، ایرنا:
قرارگاه خاتم‌الانبیا: نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند
🔹
تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را نخواهیم داد.
🔹
بی‌سابقه‌ترین رویداد و حضور مردمی در تشییع و بدرقه قائد شهید امت اسلامی، شکست خفت باری را بر استکبار جهانی و آمریکای جنایتکار وارد نمود.
🔹
ارتش تروریست آمریکا بدون هیچ گونه پایبندی بر تعهدات خود و در شرایطی که پیکر مطهر رهبر شهید مسلمانان و آزادگان جهان میهمان مسئولان و مردم سلحشور عراق می باشد در تجاوزی آشکار برخی از نقاط جنوب کشور عزیزمان ایران را مورد هدف قرار داد.
🔹
نیروهای مسلح جمهوری اسلامی ایران به تجاوز و اقدام تروریستی آمریکا پاسخ کوبنده‌ای می‌دهند و تحت هیچ شرایطی اجازه دخالت در امور تنگه هرمز و مدیریت آن را به آنها نخواهند داد.
🔹
مجددا اعلام می‌گردد تنها معبر ایمن برای عبور و مرور کشتی‌های تجاری و نفتکش در تنگه هرمز، مسیری است که جمهوری اسلامی ایران آن را تعیین کرده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76823" target="_blank">📅 05:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DzhdO7c85aSTDMZW3rcSJbcUrLrJRCf9q4AhGTLXDJp6Rak6lWmjquamXQBY-h9zNllDjfODdgmmVngatJt2Y7Bg1Mug5QbbU9d1phGAZQYPOMePFRacuRwkzjBKzJr1qtVv2cZxW5UXQnhFmNG0SIE-YJXW6gBFuxGrel8ATwD4DxQ6eEEiJHvOKukzvDx41DcsUy3ryIQgmNRhgCZufxJUrR-TsIjuoU0wvt7L6-Bpe34IT-kcW0pzRwuy_2kkhUf5kmtX0nx48kKCecYWLxRZyJaFbCSEh0T4waJetfXLWqDlIEJ6J-NY8mk0zsEEWqlrtCN4EnhbQQl9a8s1Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mgXD-DEKlbrG6km57vjAq9YABWP6cNSamX3Milp7nAZ0WY_FnAqC4AAjpUU7paH2IFCe3BYHG1t2QCyPgnt0ocu7qT69n9H8ZKkEomWdvFeduz87RC8ADMEYZpetJKJr5cnLpn5YF6k5ODFar8iGXpqJfQjltSZR7DLEiEKTG3sZEoVYnlP3FYvldCrgprDgq5qWKs16hq5W0zxn4RSQo-SW3as0wJYhNX7UP136lhOuk69jETzfvgTE7z4X3PVW-_-pJzXkfwG8GF3ckms7QTmEvXqGTkWl9UbQ0PgjzSCzVkLf1BW6sbw8OoxdX4UeRV5DtnWJ4hfo7nKTJIYg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jbxa7OD4FILOhHifCehi5KhQ9djGcoKtONoAnmjDEPfqsdpZWb1DkZIN_mrv8gay06DhEv0_8e485WU2Gqk4Es0saRZPpEzEVL7GLBvV5euLN-dyt40ZpcxxAfxPL5KAPGWzr1LtBd81qQuP4HtvCsbiW-Fwpvn_95MPdS1z2TkBPeAibfr8TUbr2CRT-Y6lvJCIYLBD2yohhKqPl5Br9AJ5MZbQYvuF8HJ5Hf-YH6mA9kwMmZuBTVNlx-4CrAZ1rqLqFFK39AF-x6a370pVHN3GFo1OJgCCaIUgH3De4BiRY4g_C-_GdmJ73xsn99YUISR1MNHcUCi9PgS8YAF-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ubscRc0OaTcWQLUZ8TqO1Gxz7g6ND0pTQCA3k3aQNtyInaVc23_Igm0ljegtPzoPmXY1THB9fwDTkqUt2GuvZe166qvNqKSlhxuUzumBedRoxYKx0eZWonrRmvQRsdkYYO61JUXsYq1OrbEBnWWeVP9HwA9GVawdcXIQFU-UIA_fyAD2UetTk49sJ_O9BN7Q0-IFwySt8Kw7OOROaAAvcHBmJcNLjaDa2OCXy2a1-2_pFU1zBtaEos2w_WR5-LDUs6lf5Uv8CwNblXB4Y8xPmR1B8p9dFzI3yMdfHtZurZ24JnDIN_QBIX-D2YmeZrGt-mai8jQlZJQpZAhnM_Mu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TYEAXn_m_71oJ6z6kg-hc1bhErmubIJPKE-tb-C1M-ydlsgpQFP17vgoI9ZfW-a-HCI_r79VdmKqI7Fey5P4VwFuvWhicHfL5PYarioPhl0dwHLdl2qQNoiaou90Dbi8FQIXISq8_H5opwI1T8Dzb57tEg954o62C6g1AculKhF0joVpiOcFECn-wf7URP-cPwD_p5PrfKhFM8ToJia7IGuMc04NIa5-nAkj0oTiDP6aMCpTKt0x6J2nPbn_gD22Ej4Vl8QmFXv1pCHelsWzMFY5ZLmaE5bmTt9VtZ8dGrCxTxml2nZJLfrmDpml_2V79trMsaYV8gVroUMV_WRK0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/964f541742.mp4?token=K5T5XyOoZgJxTF1i4dTfqu6WrdtUZqZ-dOkyPahVhvNV5cK0OML4Nghvg9BzkX0cSzVeeOqw4ZeP8Zcnp8p74087tb7Rjszd4vcwiTtpFvh-D9SiFzmImaSxLzNoK8aD_762URQ8ZqTw6G8wY12y3VN0kQ1p5-e6_SKfuZ4MIZmBl8R4aKPSVDz2XZTLAAD6a1muAFYKSiOdXkmewqyoJVLJuI7aUpWa7e86kkzk88t27WjJMHIR7oOsw8RglEAkYGc7mItDB9Ej6ubAh9mnMna3s8AwFNNCctDha4lFAlJYJpuVL5fYVU33M80JwTQl0bm2CjBxIwX1MCwN4k0Jtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/964f541742.mp4?token=K5T5XyOoZgJxTF1i4dTfqu6WrdtUZqZ-dOkyPahVhvNV5cK0OML4Nghvg9BzkX0cSzVeeOqw4ZeP8Zcnp8p74087tb7Rjszd4vcwiTtpFvh-D9SiFzmImaSxLzNoK8aD_762URQ8ZqTw6G8wY12y3VN0kQ1p5-e6_SKfuZ4MIZmBl8R4aKPSVDz2XZTLAAD6a1muAFYKSiOdXkmewqyoJVLJuI7aUpWa7e86kkzk88t27WjJMHIR7oOsw8RglEAkYGc7mItDB9Ej6ubAh9mnMna3s8AwFNNCctDha4lFAlJYJpuVL5fYVU33M80JwTQl0bm2CjBxIwX1MCwN4k0Jtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکان نیوز تصویری از یک انفجار بزرگ در بندرعباس و ویدیویی از انفجار در سیریک، در پی حمله هوایی آمریکا را منتشر کرد.
@
VahidOOnLine
+ تصاویر دیگری که با شرح امشب پخش شده‌اند و من از درستی همه‌شون مطمئن نیستم.
اسکان نیوز گزارش داد که ستون دود از سمت پایگاه هوایی بندرعباس مشاهده شده است.
منابع حکومتی:
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان: دود سیاه در پشت بازار ماهی‌فروشان بندرعباس ناشی از اصابت پرتابه‌های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق‌های صیادی مردمی است.
🔄
آپدیت:
پرس تی‌وی، شبکه خبری انگلیسی جمهوری اسلامی، از شنیده شدن انفجارهای دوباره در جزیره قشم و نیز چندین انفجار در جزیره خارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/76813" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/noXQVIMWO7ENQ8pD4PqBB-lmftvyoZzDe6f6NsKTxsvjmGCbbVR4MYkxiSkynGNUXZ1gfXv641-P82lzfP1x5lW5HLCIhzNBCPFylGKdLiHD1WKv0dz6qCHvFJuHZe8xu7ZlDwXYud3f8fDSaSV0LNjtXf_VmJ2Z4TRTnTgMrcFVhJfADPIKeIMhb60aNQwFolg-_L9qjKIPWizl99Ies19i0w9sGRjk2LO-KpNg-Ylyfnk3O5LxgLSsfiZ27dCZVR8Ez4Hvt3aAh5WCHxuYIHI1aqmZy7h0nqO25M5QqTU2UQoPAn1Wcs7lssVrriySWareKTWEl1UpT4qAlZL6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت اهداف حملات شامل سامانه‌های پدافند هوایی، سامانه‌های پایش ساحلی، موشک‌های زمین‌به‌هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تأسیسات بندری ایران بوده است.
به گفته این مقام، حملات امشب از نظر گستره و قدرت، چهار تا پنج برابر بزرگ‌تر از حملات مشابه آمریکا در هرمز، ۱۰ روز پیش، بوده است.
رسانه‌های دولتی ایران نیز گزارش دادند که صدای چند انفجار در شهرهای بندری بندرعباس و سیریک و همچنین در جزیره قشم شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76812" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S61C0IsIV3-L6KCzCanJq2i4GTTBicfTA3gevRrSOR-a3TPAu7GgQZHL5oeMbS_C9ja0YvEU4R1YXof2ns7T6jcF90NPjC0cCyJe1J4CgPyvd776kLhqF2Lzxg69XZAamm2WMOECHnTetlJ7RlPLvBFNN56zcTocAGXdIeN1EnDE2JVMNMfnjkzfU-Y4UYhVlv86UyCGJM8S-LTIo06PoZxdiNL72jhJ97zHEuw65D5w5J4xMiMO4V8JITtez8DNTZdFmZVYiA8VGknQW9S773-YrhbUq28jcG8scKLf9npoB8zD-nGQkohQVUJqzwtg4eAZmH3KXSkbnukZtFJnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی، در بیانیه‌ای، این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر امریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، شایسته مجوز موقتی که صادر کرده بودیم نیستند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FeOXBi9DkggSTa4Wm6nTBOpRm8pvnRxyp-M_tixYX6tFJD4kcSJkohh_FWjSK2SIrSZbhAvJDOFDPIcMLnw5_CEIPJQR67H6zYoWUIk9ta_kLSZ0q1U245NINdzOdwWWTqdhNGQk10re1DnCEyoQWySWsHFkTHP3kaEddZstggTdONFnmLJA_l_IbW3JsTgWqmNpjeFpkAyBReYP28UERODU-fA5eRaTsR7QuKy3jgDiN8c2NmYTINyFzy7tp_7sQ1mU7UBkmaWtKJfDZ5drNjyvOmwHkGZLzgs33vt1-jTns53ySeJQf2AL2YmZaEwH9jBbgJVXw696FkDgTgjClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
سیریک، صدای چندین انفجار پیاپی.
جزیره هنگام الان صدای چندتا انفجار بزرگ اومد تعدادش ۱۰ تا بیشتر بود
صدای انفجار درگهان (جزیره قشم) میاد ولی صداش کمه انگار دوره به اینجا
سلام وحید جان بندرعباس صدای انفجار
قشم صدای چندین انفجار اومد
نفهمیدیم از کجاست
قبلش صدایی شبیه صدای هواپیما میومد
صدای دو انفجار ۱۲:۳۵ بندرعباس
سلام وحید جان
ساعت ۰۰:۳۲
ما روستای سوزا تو قشم هستیم
اول صدای جنگنده اومد
و بعدم صدای ۵-۶ تا انفجار اومد.
سلام ساعت 12:35 بندرعباس صدای انفجار اومد 4 تا.
سلام کشتی سازی بندرعباس خیلی صدا وحشتناک اومد
سلام بندرعباس ۴ تا صدای انفجار تا الان
آپدیت:
صدا و سیما:
شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد.
فارس:
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔄
آپدیت:
بندرعباس ۴ تا انفجار دیگه
دوباره ۴تا تا الان
شد ۸ تا ۹ تا ۱۰ تا
من مرکز شهرم خیلی بده
سلام وحید جان
ساعت 12.30 صدای 5 انفجار شدید ذوالفقار قشم شیب‌دراز  نزدیک جزیره هنگام
سمت پایگاه هوایی بندرعباس انفجار شدید همین الان
وحید جان سلام همین الان ساعت ۱۲:۴۷ بندرعباس چندین صدای انفجار پشت سر هم اومد لرزید
الان بندر عباس سه چهارتا انفجار بزرگ
درود بندرعباس ۱۲:۴۵ چندین انفجار پشت سر هم
همین الان کلی صدای انفجار اومد بندرعباس 00:48
سلام خوبی، همین الان بندرعباس صدای ۳ تا انفجار قوی اومد ساعت ۰:۴۵
بندرعباس چندین‌تا صدای انفجار پشت سر هم اومد
00/48 قشم پنج شش تا انفجار قوی
00.48 بندرعباس چند صدای انفجار پیاپی
🔄
صدای انفجار پشت سرهم بندرعباس 12:50
هنوز ادامه داره
یک سر دارن میزنن ۰۰:۵۰
مجموعا بالای ۱۵ انفجار
۰۰:۵۰ صدای ۹ انفجار دیگه هم با صدای شدید از سمت پایگاه هوایی داره میاد
بندرعباس ساعت.همین الان چند تا صدای انفجار پشت سرهم اومد۴۸دقیقه بامداد چهارشنبه۱۷تیر
سلام همین الان صدای انفجار پیاپی و نور نارنجی بندرعباس
بندرعباس رو همچنان دارن میزنن
👀
صدای انفجار و پدافند پی در پی بندرعباس همچنان ادامه داره
همین الان بندرعباس
صدای انفجارهای شدید، پنج تا شش انفجار
کشتی سازی بندرعباس، اطراف بستانو رو زدن
سلام صدای انفجار بندرعباس بیشتر سمت اسکله ساعت۱۲:۵۰چهار صدا سمت شرق اینجا صدا نمیاد سمت غرب بندر اینجا صدا میادسمت اسکله
🔄
ساعت 12:57 انفجار دوباره بندرعباس
بندرعباس ۱۲:۵۸ همین الان صدای خیلیییییی شدیدی اومد
خیلی تو شهر بود انگار
اقا وحید بندرعباس یجوری زد شهر لرزید
پیا پی اسکله باهنر داره میزنه پشت سر هم صدا میاد
ساعت 57 : 0 صدای شدید انفجار در بندرعباس
00:58 دو تا سنگین تر زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hstsjzzRyxE3yDjU8F4gFhCjjoa5HnpxKluCmikLxtYc-gQUfOzdtkJq1UPqkjnpLScvLx8terfWYSV-_m7VNHaXpAttj9hqCh_4U9riDDCd8CihDGL6N2Ls5GRii0KPljlWi7syzgLj6_CKWqaKHpUpN1rLr0ZRvd7nUD84AqpbKgMLoZcQAXgTPyPJzRtOT3VqwuPSBTldW1gH_4i3q1KPKHOL0TvKucm7xzYNx7vmZ6UcQhpnaqMe6Kz0HiPyO3NeQXtCToPsBtsCP85bf3YM4zzLeMHTH34KiW9Dlr1PypL4pr35Qj1-AGV0mUV5pPUTcrufyII2oSUtQUZdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا معافیتی را که به‌طور موقت تحریم‌های نفتی علیه ایران را تعلیق کرده بود، لغو کرد و اقدامات جمهوری اسلامی ایران در تنگه هرمز را «کاملاً غیرقابل قبول» خواند.
یک مقام آمریکایی به خبرگزاری فرانسه گفت: «اقدامات ایران در تنگه هرمز برای ایالات متحده کاملا غیرقابل قبول بود و با عواقبی روبه‌رو خواهد شد.»
این مقام آمریکایی گفت تفاهم‌نامه واشنگتن و تهران «کاملا مبتنی بر عملکرد طرف‌ها است» و هشدار داد که ایران تنها در صورتی از مزایا برخوردار خواهد شد که «رفتار مناسبی» نشان دهد.
مجوز معافیت از تحریم‌ها که حدود سه هفته پیش اعلام شده بود، در ابتدا به جمهوری اسلامی ایران اجازه می‌داد به مدت دو ماه نفت خام و محصولات نفتی و پتروشیمی را صادر کند، تحویل مشتریان دهد و درآمد حاصل از آن را به صورت ارزی از راه بانک مرکزی وارد ایران کند.
اقدام آمریکا پس از آن صورت گرفت که بنا بر اعلام ناظران دریایی و دولت قطر و عربستان، در فاصله چند ساعت سه نفتکش، از جمله یک کشتی حمل گاز طبیعی مایع (ال‌ان‌جی) متعلق به قطر، در تنگه هرمز هدف حمله قرار گرفتند.
@
VahidHeadline
وزارت خزانه‌داری آمریکا مجوزی را که ۳۱ خرداد برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران صادر کرده بود، لغو و از روز سه‌شنبه مجوز عمومی جدیدی را جایگزین آن کرد.
وزارت خزانه‌داری آمریکا اعلام کرد مجوز عمومی X به طور کامل لغو شده و مجوز عمومی X1 جایگزین آن شده است.
بر اساس مجوز جدید، شرکت‌ها تا ۲۶ تیرماه فرصت دارند معاملات مجاز بر اساس معافیت ۳۱ خرداد را خاتمه دهند، اما
از ۱۶ تیر خرید جدید یا بارگیری نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران ممنوع است.
اوفک همچنین اعلام کرد هرگونه پرداخت به اشخاص یا نهادهای تحریم‌شده باید به حسابی مسدود و دارای سود در ایالات متحده واریز شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9hA-7ymNWm7q1P1NHvkUgtpe14dcgzhfWZ18Hclw4PMzWJ4NxsjucrjwsLXNJzF06rXDHUA4zrEsZLLZN2o9HDqbYtS5TxriWE0nhFlw5vU_6yWAIuEgsMyXieIMzkY3v5jM5R3wIaRZTPuxtPfrdbbcxPNCUs4mhNCu-Epewy_7aXFbwNjHr3eiXH15xIZT42yvfIApqpTalsAapQSB5ZgIXNVvKsNYounY-zkLZPDQbAkZYVg72RThUSuB8vBjJ8DX-duu5mafXYMECh5hRsdLL8dGmtfNyE74LVnRTxLSsCtKnPQPBzCyJZytfquzXbJKMjd1e3htMzNHIcEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3cNJ4DQitjFcbB8tvocyl_g1qPFjMMED7t7n8E0qCzVchbemmILGsHbbZOOzk5A8JB-EFWC-I2wdpHLnRLRUm8xYYvx-owTjbZ8xsf4GIBAyg2qC3sWs4fsihOc4__Sxxl4prCucjfYz7qgqhumvlxjpYPvIXDj6fASJjDng6GXgCtj9Ya6GAlsCDaZgQCAW5tXgVJnQplZ3ASU0NDZe9TUINIFKPIn_IUE47zlH8ZPl1QTeJ1xvQ-j5rl4JWCaYVChIsGhlrW6rEyW_31C9hJ7jbdHznttoTIJsRHw85kIi7pzlyptA348YYigSTPCHURx4Ud0ydCqF96pKPa_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc9oGB5Rw2_09ZWmqKr-Z1uSq2Hygv5Hfb_x0reOW-l-vNT3g9L7Op6kcYo23mvZFuWWeRuVql6SGYYEdJa09bC2bcsXbEgPHbLF9_y43cHP0AH2PbB_RtcelO7fO6r4k5GRlGp7MzUttMT6JfqyaOHqHWyst1nzQOiLUE0KRPamYLazmqntJtvJh2UEXSwDWR598oHXJtxa-nBHdWcpywvdB_IYQ3DPbb2JyEdZEGT0987guLhFjoxmN8o5_55-EmJs7aRtZUfc9yf3C5CxADxZ-H-InAE99vfcNblAm-L2ZGr_3RJVTre7KBVbm8c1V9lpfvVCIAkI1Ql6K5ivtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rpUgFTCO3oXIray5SIiydsJtGFs4sYm6Gt2Bhqy18rax8PvIkmEf1YwHz1q2O05EX4U6UTBr4kTErGhQdujsAx0U75eE0-HzvHU5b522A_QX0ikDztUohfPwa_i6_H13VsmNG-gsccv7c1SLkCUIV1lHsn9MoPVnyI-9__GT213S15-EKSs4ZcwTAcyHoCCFxBVHPwc0_aC97JwQ-OQ3ZSWU8F3qFbvwUtHtujQaI6gqM_Yf6ntHpj33gJb2VOfuRPnEdigiMPFgvSwziIE9YGhr7r-BXIBsHbpqXgvfFqu8D5NkLy-wC2YVWQhrE_NSdut4V_VJO-tzZyXqxTSGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhWwunuW-FZanS6BvZOXzU6MQwbgp2yv_2yoXmaduT_LGewTkRBwjUN8MbZxIUvyw4v827LBiM3SKTfW3lgGLI4cbtEGbDSqRD99TSuM79L1M3LnG4q3PgyzAF-iMG4cEA8fSNsIj-7qOxICR-6FZS92vIjhUJtIG-_9QY_j6uuG_oSOnQFlP-1FOxC0hS0da9GOeccvciYNRCcpmB1N61JVvYU3haDWjontZx7TNUJmVDMBDmR1wmnFXPAk4jYLPDrbIflaajEbeKqBGCu6pEoPK6shWqID6EsT11nPDWlcl5Pjg4M5K7ZO6Da6A5vzQMR8MljU7PHhRqetwfnAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=HmIEcFMnyrYzJyOqV9O3KSR7yqqfAL96VITlHDTz42MUzOBfea2iJ7xUQS4Gcvc-YY0zM0Qm3-DH7e2J4ifu9Dy1aSg7R0IzW3A9oIv7xAFSZc9yqOm-pSC4cx4bP_Z-u37sO_8WcBHThirlmlEybSSgsNx6v7amZputLXziU9ObfVcoblBK1P0GOseXj4mIcbGoMWu_7jSQegn7SgkzF47l44Miybh_9TkhLmIBAlPhAl0GeAy1ymY6CD4urUWjWgwZm3mEGLo7XHiRNuWnnS7rHEWUBoL1NtZp5VJCbGGkve8-akYy8CrJnBRKM_hv00mVxt-xFtaSva1M1E0ilA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=HmIEcFMnyrYzJyOqV9O3KSR7yqqfAL96VITlHDTz42MUzOBfea2iJ7xUQS4Gcvc-YY0zM0Qm3-DH7e2J4ifu9Dy1aSg7R0IzW3A9oIv7xAFSZc9yqOm-pSC4cx4bP_Z-u37sO_8WcBHThirlmlEybSSgsNx6v7amZputLXziU9ObfVcoblBK1P0GOseXj4mIcbGoMWu_7jSQegn7SgkzF47l44Miybh_9TkhLmIBAlPhAl0GeAy1ymY6CD4urUWjWgwZm3mEGLo7XHiRNuWnnS7rHEWUBoL1NtZp5VJCbGGkve8-akYy8CrJnBRKM_hv00mVxt-xFtaSva1M1E0ilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۱۶ تیرماه در جریان سفر به آنکارا برای شرکت در نشست سالانه ناتو، در کنار رجب طیب اردوغان، رییس‌جمهوری ترکیه، بار دیگر از عملیات نظامی آمریکا و اسراییل علیه جمهوری اسلامی دفاع کرد و گفت این اقدام را نباید «جنگ» نامید، بلکه هدف آن «خلع سلاح هسته‌ای ایران» بود.
ترامپ با اشاره به نقش ترکیه در تحولات خاورمیانه گفت این کشور جمهوری اسلامی را «به‌خوبی می‌شناسد» و همراه با چند کشور دیگر، در تلاش‌ها برای پایان دادن به درگیری‌ها نقش مهمی ایفا کرده است.
او گفت اطمینان دارد رجب طیب اردوغان نیز خواهان دستیابی جمهوری اسلامی به سلاح هسته‌ای نیست.
رییس‌جمهوری آمریکا در ادامه با اشاره به روابط واشینگتن و آنکارا گفت: «این حتی جنگ هم نیست، یک عملیات نظامی است؛ خلع سلاح هسته‌ای ایران است.»
او همچنین با تمجید از توان نظامی ترکیه گفت این کشور می‌توانست وارد درگیری شود، اما چنین تصمیمی نگرفت.
ترامپ در بخش دیگری از سخنانش از عملکرد متحدان اروپایی آمریکا در ناتو انتقاد کرد و گفت از نبود حمایت آنها در جریان درگیری با جمهوری اسلامی «بسیار ناامید» شده است.
او اظهار داشت اگر نشست امسال ناتو در ترکیه برگزار نمی‌شد، شاید اصلا در آن شرکت نمی‌کرد و با اشاره به اردوغان، او را «دوست» و «رهبر بسیار قدرتمند» توصیف کرد.
رییس‌جمهوری آمریکا همچنین گفت ایالات متحده برای دفاع از اروپا در برابر روسیه هزینه‌های هنگفتی پرداخت کرده، اما در مقابل حمایت متقابلی دریافت نکرده است. به گفته او، در جریان تحولات اخیر عمدا واکنش متحدان را زیر نظر داشته تا مشخص شود آیا آنها نیز در مواقع لازم در کنار آمریکا خواهند ایستاد یا خیر.
ترامپ در این زمینه از بریتانیا، فرانسه، آلمان و ایتالیا نام برد و گفت مدت‌هاست این پرسش را مطرح می‌کند که آیا این کشورها نیز در صورت نیاز از آمریکا حمایت خواهند کرد یا نه.
@
VahidHeadline
رئیس‌جمهور آمریکا در عین حال تأکید کرد «ما به هیچ‌کس دیگری نیاز نداریم»، اما این پرسش را مطرح کرد که چرا آمریکا «تریلیون‌ها دلار در ناتو سرمایه‌گذاری کرده» تا از اروپا در برابر روسیه محافظت کند، بدون آن‌که چیزی در مقابل دریافت کند.
ترامپ گفت: «به نوعی داشتم دیگران را آزمایش می‌کردم تا ببینم آیا کنار ما خواهند بود یا نه، چون مدت‌هاست می‌گویم ما به آن‌ها کمک می‌کنیم، اما مطمئن نیستم آن‌ها برای ما چنین کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Bz39czijqQ2m_S7UIelPP7R9-II0NjjopJZ65jtZIELhasYP4kNcZwRdzTFrGP--U3VAsfogtB54CUfrZE_MD0q-IPlkJl9bifPCGGvKSfo805Yta_tXgWKH15gH7XxJsg2gnaCtiBWYf8F9LPyYo-vwScovYOsbal9Ok8JNrTtGM1yuQiiwxe5VVnOgvGnpZk4Rt7nVeZis0YOMqjFFb71GScq92AgfFM4QjwEclpmhIUj2IUlmNADJ73KsgjvFdib3FOhYpNOrmECESsS48ibbwuqT5-yIv56bdmcWUo4fuUUu4e6FtvTE9Xg-X4H7uUdSL9eeW3J3PnNK3UnvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Bz39czijqQ2m_S7UIelPP7R9-II0NjjopJZ65jtZIELhasYP4kNcZwRdzTFrGP--U3VAsfogtB54CUfrZE_MD0q-IPlkJl9bifPCGGvKSfo805Yta_tXgWKH15gH7XxJsg2gnaCtiBWYf8F9LPyYo-vwScovYOsbal9Ok8JNrTtGM1yuQiiwxe5VVnOgvGnpZk4Rt7nVeZis0YOMqjFFb71GScq92AgfFM4QjwEclpmhIUj2IUlmNADJ73KsgjvFdib3FOhYpNOrmECESsS48ibbwuqT5-yIv56bdmcWUo4fuUUu4e6FtvTE9Xg-X4H7uUdSL9eeW3J3PnNK3UnvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهوری ترکیه روز سه‌شنبه ۱۶ تیر، در نشست خبری مشترک با دونالد ترامپ، رئیس‌جمهوری آمریکا به مذاکرات جاری میان تهران و واشنگتن اشاره کرد و گفت که او و دولتش در تلاش‌اند که روابط آمریکا و ایران را به سطحی باثبات برسانند.
اردوغان در این نشست که در حاشیه اجلاس سران ناتو برگزار شد، تاکید کرد که این تلاش‌ها در راستای برقراری صلح جهانی خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76801" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCMmrniAPlKG4UvA2jjJK5k40bgACyVD3WdgmR_lf07jqT8xvqQlTK1WqxM5Mew6h3VKjgo2BmlvKpomvkGS7kstGmipgKlNV7c-C7rk3lsrIKnNwvM3A2iXMQKGVCwm-jkeRxy-ECpvX56NeeFlas66DeOE3lp_pzFDHcxrgmjpJLNsnslBqEAryeo8oQ2DCKs3DgLWEEsglDDAtUl07sozxSKctP9O32DbN7lj8UwQ1HWo-ZLL6lRU3M1j6948kE1-jRpO7HE0IzWPKVd1JkjogKiWMO-27-9OAeeMkMh03aohDa6_qRuCW5Da4S5n1qRAMsNm69g5Z3xUuLDY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است.
خبرگزاری رویترز حمله به آن دو کشتی را تأیید کرده و وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داده بود که سپاه پاسداران دست‌کم دو موشک به سوی آن‌ها شلیک کرده است؛ ادعایی که جمهوری اسلامی تاکنون به آن واکنشی نشان نداده است.
سخنگوی وزارت خارجه قطر روز سه‌شنبه اعلام کرد هدف قرار دادن نفتکش قطری «الرکیات» در نزدیکی تنگه هرمز، حمله‌ای غیرقابل قبول به امنیت کشتیرانی بین‌المللی و تأمین جهانی انرژی است و ایران را مسئول حمله به آن دانست.
هنوز هیچ گروه یا کشوری مسئولیت حملات تازه به نفتکش‌ها در تنگه هرمز را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76800" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=XydJCTdNUywaLibuQN8wyW-A8W9MvAnmS_j4e9Q_4uzgd8aC8M8DtjH6csDr_oBTt--wAyaLgNu4ClFZFiERQdEOFz2IdbsFeI5-zBVf8-0DB9BaHMj040Xg5ieD_eGLLBM15Rbgmf9I0J_NbmJKBAxzXUDgjrqUnOSy9KBcPUMMi3Bwfds1KPhNdPch8bnsqOtbM3EKcSBUXQr8HBRRfaPsAAEIij4VvhpSr2dyLKYnOurutqf2dgBjOhYvG5Hy5kR6JlR-riLqoQ98IrArWMaKFM4hKkx2Y2GJE79zCXkHtDtXs9aCpGoIocsUb6hlSPimet_PMFhGWBR6C5gPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=XydJCTdNUywaLibuQN8wyW-A8W9MvAnmS_j4e9Q_4uzgd8aC8M8DtjH6csDr_oBTt--wAyaLgNu4ClFZFiERQdEOFz2IdbsFeI5-zBVf8-0DB9BaHMj040Xg5ieD_eGLLBM15Rbgmf9I0J_NbmJKBAxzXUDgjrqUnOSy9KBcPUMMi3Bwfds1KPhNdPch8bnsqOtbM3EKcSBUXQr8HBRRfaPsAAEIij4VvhpSr2dyLKYnOurutqf2dgBjOhYvG5Hy5kR6JlR-riLqoQ98IrArWMaKFM4hKkx2Y2GJE79zCXkHtDtXs9aCpGoIocsUb6hlSPimet_PMFhGWBR6C5gPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری که در شبکه‌های اجتماعی منتشر شده گروهی از شرکت‌کنندگان در مراسم تشییع جنازۀ علی خامنه‌ای را نشان می‌دهد که به عباس عراقچی ، وزیر خارجۀ جمهوری اسلامی ایران، حمله کرده و او را «بی‌شرف» خطاب می‌کنند.
گروهی از هواداران نظام جمهوری اسلامی که با مذاکره و توافق با آمریکا مخالف هستند، اعضای تیم مذاکره‌کننده را به «سازشکاری» متهم می‌کنند. روز گذشته نیز تصاویری مشابه از حمله به مسعود پزشکیان در حاشیۀ تشییع جنازۀ علی خامنه‌ای منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76799" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUBgovI3UHIW_NyRA3YLGZKI8zGatQhWEdwdzYPrWrTyjKMPcbBg_yPv1C-Po5tiy2UWn1Yxc0riTU13d3vXYunb6qllyTMt-TMbVtdfxlH7ixpR2kwrQsYsMkIgZvAOZpWouOrGhl3I4csSID07RcWHcQngUDEeJ53rJayNbdThc99SAWpbZ36IlhnXpasbOnoorjg_PlXT5PXyhUWMrHdGXVxTUcu3YqQTrO1ow37sfO2qIn1K_RGu4TEAt3fZWILD3SZ4_P-MQiXUZ9DEWlpsGKmquuGIsHLGaToLbKVqoJ7g0JyWrma2nXngmiHtuR70Ne9R_IpNendfnxl_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با نزدیک شدن زمان انتقال تابوت علی خامنه‌ای به عراق برای اجرای مرحله تازه‌ای از مراسم تشییع رهبر پیشین جمهوری اسلامی، محمدرضا سیستانی، فرزند ارشد علی سیستانی، مرجع عالی‌قدر شیعیان در نجف، به دفتر علی خامنه‌ای اطلاع داده است که پدرش بر تابوت او نماز نخواهد خواند.
در همین حال، جواد شهرستانی، داماد و نماینده علی سیستانی در ایران، نیز در مراسم تشییع و نماز میت علی خامنه‌ای در تهران حضور نداشت.
پیش‌تر محمدکاظم آل‌صادق، سفیر جمهوری اسلامی در عراق، اعلام کرده بود که مراسم استقبال رسمی از پیکر علی خامنه‌ای شامگاه سه‌شنبه در شهر نجف برگزار خواهد شد و آیین تشییع عمومی نیز از ساعت ۶ صبح روز چهارشنبه در شهرهای نجف و کربلا ادامه خواهد یافت.
خودداری علی سیستانی از اقامه نماز میت بر پیکر علی خامنه‌ای در حالی صورت می‌گیرد که جمهوری اسلامی از زمان کشته شدن رهبر دوم خود، مجموعه‌ای از مراسم تشییع و وداع را در چند شهر ایران برنامه‌ریزی کرده و اکنون نیز در تلاش است این آیین را با برگزاری مراسم در شهرهای مذهبی عراق ادامه دهد.
غیبت مهم‌ترین مرجع شیعیان عراق در این بخش از مراسم، یکی از مهم‌ترین حاشیه‌های مرحله عراقی تشییع علی خامنه‌ای به شمار می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76798" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4cRuOlBUTguDW292wbcy6jgW5zT2cAmXC-uI25NtGIdmVYzCkTpxf7jUPYW2feSl8rmy9kIT4gHRdrF89aKzn_0JDfqfr9fAPfCnDxEOa5DJTnX-5qoM1MWRENYkbAi73_srRfG7wX-LKRpKBB9Wjuv67qcfWjn9_377tN2Lcx-2LMeh_WnTtiF7J86i1JO4ASdQF2EQ1ATGkp6m-Z1rQEO5FXVLmKOk8lLVAsYZ4covxFO-7lh8SGCMYE7OBF5YHimQFvG7RBUgP9VDMwIvkA2NZXs5yy8p5jydireKX8KTbiroiyUJfMDSbJRViOLVPm4lpmEnlHoJ4QnH--EcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داد که سپاه پاسداران روز دوشنبه دست‌کم دو موشک به سوی کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است.
بر اساس این گزارش، دو کشتی در پی این حمله آسیب قابل توجهی دیده‌اند، اما هیچ تلفات جانی گزارش نشده است.
حمله گزارش‌شده پس از آن رخ می‌دهد که مهلت توافق یک‌هفته‌ای میان ایالات متحده و ایران برای توقف حملات در تنگه هرمز به پایان رسید.
اکسیوس می‌نویسد که ازسرگیری حملات ایران، تفاهم‌نامه‌ای را که کمتر از سه هفته پیش امضا شده بود، در معرض فروپاشی قرار داده است.
این منبع خبری می‌افزاید که
احتمال می‌رود ایالات متحده در واکنش، اهدافی در ایران را هدف حملات نظامی قرار دهد.
@
VahidHeadline
صداوسیمای جمهوری اسلامی به نقل از «برخی منابع» گزارش داد که «نفتکش الرقایات» متعلق به قطر، قصد داشت «با حمایت نیروی دریایی آمریکا» از مسیر عمانی تنگه هرمز عبور کند، اما «پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.»
این گزارش تلویزیون حکومتی جمهوری اسلامی این‌گونه القا می‌کند که تهران این حمله را انجام داده است. با این حال، جمهوری اسلامی تاکنون به‌طور رسمی مسئولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76797" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObJb03gZHg8SRFcqKRcn4o8W9QiQa8Sc1zaAZrphPSQxZzYvIgdTwOPV0m1QeD09EoAR_MkNFfQeLurQvk7gBKPx1J-WjrsfPeBv3cE4j3Ew1ud2s_jQNpB65l4YvWhiKg3oIhn0z_LcsXq9yJA5By-jWAja3l3tY0hX1alN8Hm8gSMEDoHlRtQC7KOccfy2f9ZwSBo8bdDXsFANkpRHhDV22rTq8GijJp0TmJ1mrKMwJ19B_NdAU-ob-FvaJstdnznY8u8Fau3LW6dEahqzJXF9fbm1XPWOJVG0LQ2Kt0wI6eSRA9PahodISKF_x3n9ZPBURRf7I4EWIPXSCGYzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، بامداد سه‌شنبه ۱۶ تیرماه، اعلام کرد یک نفتکش در حدود ۱۵ کیلومتری شرق لیما (Limah) در سواحل عمان، هنگام حرکت به سمت جنوب، از سمت چپ بدنه هدف یک پرتابه ناشناس قرار گرفت.
به گفته این سازمان، این حادثه باعث آتش‌سوزی در نفتکش شد، اما تاکنون هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد مقام‌های مسئول در حال بررسی این حادثه هستند و به همه شناورها توصیه کرد هنگام عبور از این منطقه با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به این سازمان گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76796" target="_blank">📅 03:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=p2l1_qdfKrg6WV_iXyt8Fp-4jFlD46tiNI93GVrxcgebI7-4zjifJiV06nV_ghvbAW4ul5L2bCoTZKmPQWG4geVWRF00MMkCUrE1LHv1fvbx3AVn3R08LArMZ8khBG7RU5WUaWN-4ctpW1lNJZjq9__okN9Lim02yWvc2x_hEGArRFkBoEFaW0jieRXRx6KZqqq7Yor08q5KUv2hKZkgtP5QTnV8i8QFw5H9vaO2B1jgnM5turmo_d83ef1MP0Qi7npLzFifNukvmkS2TDaTq8bgdt7K5WwZbqMz_16zc79fcmqCm0zyPDidwV8gCzvLALhSnt0-S7ZqXtQQ35HouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=p2l1_qdfKrg6WV_iXyt8Fp-4jFlD46tiNI93GVrxcgebI7-4zjifJiV06nV_ghvbAW4ul5L2bCoTZKmPQWG4geVWRF00MMkCUrE1LHv1fvbx3AVn3R08LArMZ8khBG7RU5WUaWN-4ctpW1lNJZjq9__okN9Lim02yWvc2x_hEGArRFkBoEFaW0jieRXRx6KZqqq7Yor08q5KUv2hKZkgtP5QTnV8i8QFw5H9vaO2B1jgnM5turmo_d83ef1MP0Qi7npLzFifNukvmkS2TDaTq8bgdt7K5WwZbqMz_16zc79fcmqCm0zyPDidwV8gCzvLALhSnt0-S7ZqXtQQ35HouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که از جانی اینفانتینو، رئیس فیفا، خواسته است اخراج فولارین بالوگون، مهاجم تیم ملی آمریکا، را بازبینی کند، زیرا به اعتقاد او خطایی که منجر به کارت قرمز شد، عادلانه نبوده است.
آقای ترامپ در جمع خبرنگاران در دفتر بیضی کاخ سفید گفت: «تنها کاری که کردم این بود که درخواست بازبینی دادم، چون فکر نمی‌کردم آن صحنه خطا باشد.»
او همچنین داوری را که این کارت قرمز را نشان داده بود، «افتضاح» توصیف کرد.
این اقدام بی‌سابقه، روند رسیدگی انضباطی فیفا را در کانون توجه جهانی قرار داده و با واکنش خشمگینانه بلژیک، رقیب آمریکا در دیدار روز دوشنبه برای کسب جواز حضور در مرحله یک‌چهارم نهایی، روبه‌رو شده است.
اتحادیه فوتبال اروپا، یوفا، هم به‌شدت از این تصمیم غیرمنتظره فیفا انتقاد کرده و آن را «بی‌سابقه، غیرقابل درک و توجیه» توصیف کرده است.
@
VahidHeadline
در ادامه واکنش‌های گسترده جهانی به رفع محرومت فولارین بالوگون، مهاجم تیم‌ ملی آمریکا، فدراسیون فوتبال بلژیک روز دوشنبه ۱۵ تیرماه اعلام کرد تصمیم فیفا برای صدور مجوز این بازیکن در رقابت مرحله یک‌هشتم نهایی جام جهانی را به چالش می‌کشد.
فدراسیون فوتبال بلژیک در بیانیه‌ای گفت از روند طی‌شده برای این تصمیم «عمیقا نگران» است و برای دفاع از «اصول بنیادین اخلاق، رقابت عادلانه و منافع فوتبال» به پیگیری این پرونده ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=d1cbfqIMdD0DhkWw2DcSyGdi0BVcOD8qVhPboibUliwI8cX8wFFhEjXtD98oqzmOnpJUBGZHwXES8o18wwmJcRZ07JHmKreTV1dzvG8PSMjhTtCpoLuopqckPRcgyP0gt3mrHodh1Ca5Kz2a-YXBDukZmla70UGUUlhb1nnTU-A7iVNu0ikvKQDKdjouQh7hzNWnMnyN4_8Ne3NYJ4W5cXrhpduXRlJ6MfhJHqxPnHEJq-beH_MnbBa1_oePZvW-U9aSuwQsVguSs-f_jV0So0Gb6nmHNNjH0xQLjzLFk0sF7XlqhbpVZuG_XzX1MoNTwQUK4nabqmZHAPvtaEAqDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=d1cbfqIMdD0DhkWw2DcSyGdi0BVcOD8qVhPboibUliwI8cX8wFFhEjXtD98oqzmOnpJUBGZHwXES8o18wwmJcRZ07JHmKreTV1dzvG8PSMjhTtCpoLuopqckPRcgyP0gt3mrHodh1Ca5Kz2a-YXBDukZmla70UGUUlhb1nnTU-A7iVNu0ikvKQDKdjouQh7hzNWnMnyN4_8Ne3NYJ4W5cXrhpduXRlJ6MfhJHqxPnHEJq-beH_MnbBa1_oePZvW-U9aSuwQsVguSs-f_jV0So0Gb6nmHNNjH0xQLjzLFk0sF7XlqhbpVZuG_XzX1MoNTwQUK4nabqmZHAPvtaEAqDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه بار دیگر گفت: من به دنبال تغییر حکومت در ایران نیستم، هرچند این تغییر حکومت اتفاق افتاده است.
ترامپ افزود: حکومت اول از بین رفت، حکومت دوم از بین رفت. حکومت سوم معقول‌تر است. خواهیم فهمید.
@
VahidHeadline
دونالد ترامپ گفت آمریکا یا با ایران به توافق خواهد رسید یا «کار را تمام خواهد کرد.»
رئیس‌جمهور آمریکا در یک گفت‌وگوی تلویزیونی گفت قیمت نفت با وجود بسته شدن تنگه هرمز چندان بالا نرفت «آنقدر که ما نفت از آنها گرفتیم. مردم اصلا خبر نداشتند و همه اینها فقط در عرض یک ماه و نیم اتفاق افتاد.»
رئیس‌جمهور آمریکا بار دیگر تکرار کرد که کشتی‌های نیروی دریایی و تمام هواپیماهای نیروی هوایی ایران را از بین برده است: «در نهایت فهمیدند که دیگر رادار ندارند، چون سامانه‌های راداریشان نابود شده بود. بنابراین، آخر شب و در تاریکی آنها را هدف قرار دادیم.»
او همچنین گفت: «نیروی دریایی قدرتمند ما بزرگ‌ترین محاصره‌ای را که کسی ندیده اعمال کرد و در طول دو ماه حتی یک کشتی هم نتوانست از محاصره عبور کند. بعد نزدیک شدیم به اینکه شاید بتوانیم به توافقی برسیم پس محاصره را کاهش دادیم. نمی‌دانم، شاید هم به توافق برسیم.»
آقای ترامپ تاکید کرد که «به هر حال پیروز خواهیم شد. یا به توافق می‌رسیم، یا کار را تمام می‌کنیم.»
او گفت تمام کردن کار ایران کار آسانی است: «تمام کردن کار دشوار نخواهد بود. البته من ترجیح می‌دهم توافق شود، چون نمی‌خواهم ۹۱ میلیون نفر تحت تأثیر قرار بگیرند.»
«ما می‌توانیم ظرف یک ساعت پل‌هایشان را ویران کنیم. می‌توانیم شبکه تأمین انرژی را از کار بیندازیم. همه آن نیروگاه‌های بزرگ، زیبا و مدرنی را که ساخته‌اند. آنها پول زیادی داشتند اما حالا دیگر پولی ندارند. ما هیچ پولی به آنها نداده‌ایم اما می‌توانیم برق و نیروگاه‌های تولید برقشان را از کار بیندازیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hepVGaC5S8g5oh62TFwTJ2aegnM-NxN6NBV5LssJp-538vyxSIRPI15zUcrtdh0SiLDSwGRMhmLWpdP4D70yVJAKnXaaVYw-gmrOsKD17fDWmOafUAU9z2wX4DrV5i1bd_uLY4DkXaT1cUo0H82hFDR3PSqhL0svP5MFC4h-wPnAurLBYychX5GMdiU4zaSxBRGt2LV07fc2VX2vvuEJ4g4t4jMGtkLbndLldRYhd3v_xEvr45rhxkKlf8jgOa2A2niq3i3YsYMqMXZkuCqU2kHzaK40LL2icl9ffhby8723j9KW0xHgsaXC-4n_zG3Fq8wX_3sdGfbnHGR2JigcwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=sfs1DNGZmgpEltwQEuMQF_smTCuAYDKXWHkBjTP0nxG2a919DvKCUq8dXN4eagoAEUYNmQuHc5dVsQhOrKEN_ALjPIJdhkIc0uQdOUMrVaXKsFx32oC2St8RhvgIw6ylIicZkBFYYheLiKifqZwRV3tksHKGenqMlz8CtJak_IMcREz3wUKlKGkh8nCUr_YBgWvH6K9xSBJQAY5KgpWnx4xmc3LJ0FampVkxf8-Qi2417OaOmEGFxOjAcCR-nGBdn_2kL7F9Dc2nL8Z3N1rfiAB2KkbKj_QciLXnA6eG6s4bU6pgtQzBX26NFGr3e3C51zUH3UyZCPz-b8MmJXV0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=sfs1DNGZmgpEltwQEuMQF_smTCuAYDKXWHkBjTP0nxG2a919DvKCUq8dXN4eagoAEUYNmQuHc5dVsQhOrKEN_ALjPIJdhkIc0uQdOUMrVaXKsFx32oC2St8RhvgIw6ylIicZkBFYYheLiKifqZwRV3tksHKGenqMlz8CtJak_IMcREz3wUKlKGkh8nCUr_YBgWvH6K9xSBJQAY5KgpWnx4xmc3LJ0FampVkxf8-Qi2417OaOmEGFxOjAcCR-nGBdn_2kL7F9Dc2nL8Z3N1rfiAB2KkbKj_QciLXnA6eG6s4bU6pgtQzBX26NFGr3e3C51zUH3UyZCPz-b8MmJXV0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیمای جمهوری اسلامی روز دوشنبه ۱۵ تیرماه تصاویری از حضور احمد جنتی، دبیر شورای نگهبان در مراسم تشییع پیکر علی خامنه‌ای منتشر کرد.
رسانه‌ها روز دوشنبه همچنین تصویری از محمود احمدی‌نژاد را در مراسم مرگ رهبر سابق جمهوری اسلامی منتشر کردند.
خبرگزاری فرانسه روز دوشنبه گزارش داده بود در حالی که مقام‌های جمهوری اسلامی تلاش کرده‌اند تصویری از وحدت در صفوف حکومت ارائه دهند، تاکنون هیچ‌یک از روسای جمهوری پیشین جمهوری اسلامی، که روابطشان با خامنه‌ای دچار تنش بود، در این مراسم‌ها دیده نشده‌اند.
مراسم تشییع جنازه علی خامنه‌ای پس از دو روز قرار گرفتن پیکر او در مصلای تهران از ساعت شش صبح دوشنبه ۱۵ تیرماه آغاز شد.
روز ۹ اسفندماه ۱۴۰۴، در موج اول حملات اسرائیل به تهران بیت علی خامنه‌ای به‌شدت بمباران شد،‌ به شکلی که تمام ساختمان‌های محوطه بیت با خاک یکسان شده بود و همین احتمال سالم ماندن جسد رهبر سابق جمهوری اسلامی را بسیار کم می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vd-uy-gR0V9xUwGKzIS-jV0dPpUnuCzV4VRNy8kKnwZS6XIdd6HCZA1XGym1bwA7_4Dfbwb_MoAXNTJMlW-wQRfb5GYjRe65vjzVJQx5RQuCYtBCTsz0xTTPRci6owFUZQ0zHmkOrVU1Bki4pzDDSIPX61-h8ZlSJtZDeOmNg4CzrhV6a3r8uKhe7g7KZWWDyTboJwvdIpThfB0_4VxPCb6Z2gp7xy8x2rgSI4r_s0sc_f2w5NZCbTc_KBOK2NW7Hkfv-haMBtvAl68acEUogKQ9dUbPT04raQFXyGbSGlHVR8K1tXZAzWYZtMqiQcXvaFwlMe--ejxCMZNub65AUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/buRZ6PHuoEU0OSGOp-tK8gEcVnTilXbUiVkk6hI15l5eMbWE86TqccJwJz8J0ZcLGkryfCa93MaFKBsDcBFA8RE7PLIhi2l3ByWVwONx8FTiINyndXIKapfm0fBbphu59pyWdhCArxGgkeD0Evi9i0g3o2vOoMGZ_Yo8PsbqpN5RVOP9-DpGnsBhH8Nc3Hddzj8sGK_xEkLWqq0nHuDzk2X2f3yfuw7XRMSX9I6FL3Ip4dNAiDGtkSsn_dx7OCpm-e5OwXGfM2z5h4p2x-XNsEsruB0f7_sx82hSaZZYmgXrlUQKP6O2pGRxA6TjBnLz894QwopxplDQLpsPEaqFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_Rv8344RmWgYmqs6CX3jcixJevzaIBLcqDv_x-ictrpi-mH9tNR2fXLmPCLoGrc6HZpHf3lwc7WlyTtGRwvuGpY7wtRkC-XVAFkZpzsRFCouX4pAx13bC3n6D7PYD9d5r-_Rq_nT883vMauVHoVPhpYv6RTUEKYU2TxIBYi9fUGu27wq8K9U9ECWNeJrFxo88Bykzz0Kf9tElVg6zF6r7T08ZRsdGROKdaSo03AdHeqss1GosyAY7Gu4_AWck9yUcO0hyEe76u61yNNTPxg_H61NdvnBq6g869MUtdB485MzfAYOKACzAtpD7fEaBjLnap3Jq_f61gGyHvPoonyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=hMZCOhywmvOfMly12Yt36FgGMj9nMvWZjghM3oF7b7Dl38wgioBhF_fMmZhZ0SpWRXo8ZWovc1byi_5UbKhcwxVwEFCbIkbW6hAtJ2yoGm-s7YDQYkW2AkktP3vly3tRPF_Fy74nHML0iSUWwCYJsVocfrPdfH8o2yRk0VO2nRiVXfe-ipy6DGlRvp6PJ1th0bvETEFS01QEP1oI2asSun-_fM4BjADIlGDDjsXpHD3bq-5Jpuy2tOoXVTJ9HkKCQSabund2yZqyp4M5TFcOl3j83iYj2Z4BP6RNmsHx-9ApbjicVvRDPWCrT_Y5dZA57Rsgyn2kG-jr49W3955LYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=hMZCOhywmvOfMly12Yt36FgGMj9nMvWZjghM3oF7b7Dl38wgioBhF_fMmZhZ0SpWRXo8ZWovc1byi_5UbKhcwxVwEFCbIkbW6hAtJ2yoGm-s7YDQYkW2AkktP3vly3tRPF_Fy74nHML0iSUWwCYJsVocfrPdfH8o2yRk0VO2nRiVXfe-ipy6DGlRvp6PJ1th0bvETEFS01QEP1oI2asSun-_fM4BjADIlGDDjsXpHD3bq-5Jpuy2tOoXVTJ9HkKCQSabund2yZqyp4M5TFcOl3j83iYj2Z4BP6RNmsHx-9ApbjicVvRDPWCrT_Y5dZA57Rsgyn2kG-jr49W3955LYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb9jpwYRnfp260KDKl6SmdkA0LfjwYaRYY9ay_dmm-viTht0gtfr28H0HUEUcPz8YsM9eah8_0SdyRJ5-Y1Lb16ncrNlnmUUk1a9yDBaHrq_K5ZP3DtD7DrErD1q1nLktXJHOYTurU8IMUkLvbSNPW14xh-ct8hMnC5ot88GDxVpfRkHUE7MewW1GIOFArrQRJNIsS4SCSJl_N8N2qaOOzlfJ9azheSZQ6TadcqrUTl36NpNGlgUNuBSUlSNKFaDN8hBFMfhBN54tZAp1aY8ftQnR1RcnY-ybCZ4pSGN5JSydk10kPvwItvi8DI7Wpa0JpaNfXYDWcL52hKQF1_T9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=LjDs_ImjN3IZ_adP3wZJDLwWWvTNrgYgjv-68ki67_7dT6E-zL98oROMOt3Qf3-1rvrZLVsJF5JQZ1zqy8gNy1mpC2cXzZ24cWIgF7_eh8x18lnGMCw-NTrDGKZ5KYwBhqWZkS5VdZXUY_M4llOLkgWn4IOY9JnEy5Bh6niecR5sJaA8O2FwyRvvzL1TA73aKCdL-tWTrU9hbItELUqiasgz-aOJPtGzDMZYu231hQQTyLOREDppce0VZ3mXbC0e_MQ4Ql6voCKvS98LbR9ygJJAGzXfK4Tc0YCldopq0BhEgOXNcESveCTyKCD8IaMSYLrJLsQ3jyPQfvnaBv-Hsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=LjDs_ImjN3IZ_adP3wZJDLwWWvTNrgYgjv-68ki67_7dT6E-zL98oROMOt3Qf3-1rvrZLVsJF5JQZ1zqy8gNy1mpC2cXzZ24cWIgF7_eh8x18lnGMCw-NTrDGKZ5KYwBhqWZkS5VdZXUY_M4llOLkgWn4IOY9JnEy5Bh6niecR5sJaA8O2FwyRvvzL1TA73aKCdL-tWTrU9hbItELUqiasgz-aOJPtGzDMZYu231hQQTyLOREDppce0VZ3mXbC0e_MQ4Ql6voCKvS98LbR9ygJJAGzXfK4Tc0YCldopq0BhEgOXNcESveCTyKCD8IaMSYLrJLsQ3jyPQfvnaBv-Hsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDkiteHg-uWHSDKE35-Ey-wXyFgy9scItAC8Vqdua3HaMW-cS_8K2XL1LUGSqrnS1I8Gv461vE8DgHQjvUrZApEZhWLGM1iDH2m9CZ5ADq2PaIUDvBIPeMbzK9nbB0n-k-r6ACBNENsPQ4t_ZaV533GkhRl9T7vMRmTdSoUzVCnXFHgGjF_6JxzCU-la8F4Edk-b7a2UwaZFCsZ1_6zlWVQ3ArAeqcc4IrIc62dhYeVgHZvFJnmsJiV0dcdn9lRWSFeb25NndpDVlKYCreSfpxtGWGrGgfkigCuCR5TabrHjf3zfy4YWgHQFC1d0xbR__QZUUzF01dM9eaILhVjJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxUJhwHgfsYMs3UhB9imwxu0lukADqKAZhX625TyxRuh36oAKITYI_dt11hPzcnQeb79BxMxOsEPXYBrKcgjg3ybWlTBFhjhTUuchR9m1TiVJsJxrPmrXXMJ3WYr-ZkA8BFAbmvjjCUgCC42u6n5VzkCNf9l9_L3F7lCbAnl0eKsj7032aDUHYbgn3b8tm-7WJlDN4NAHe29UTqWogmiiSD__9IIofwYsRBg8NXR6vEeKfUTit03Bv2J0mc2A9EQtI_S2999xXX_qz2tTYJhhFTrseqOSAeHjwV43JgIkvM0kNsydn1visUUvAi6R5_qHiWGJl5ZjXQA1aOd1gWcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga3Y-VEDrxBZSM_2ixpbFiSkuxp6rTG5izFh7Bqwl2jArjH4FdnnVziFi3spjJbWstTkN7rozi5ad0vV_nk6gBFa7ICsN0BxkVbGClyOnVIkDYw9tbekxu-K6aKDFjaKq5Qetp2KMbLYptDszgtyRAJvA5MXBLLD_WGQdMUFDPFVAPgVo7DuDNxTkirqe-2_LYKaEPoO6ClD1Vskb4OQmgM4XPXquHnTPhGsF_f8EP3Y9lE5YZlW92LGCA-nWaGsSJECZP9ZpQh5DbifrWz4A3FyTGZCn1GvctzWYTVcUYciLMY8XdYKeOXQYEV6PnHgAAzA7NWm2t154rEBcLjC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرنوش پارسی‌پور، نویسنده، مترجم، تهیه‌کننده و فعال اجتماعی ایرانی، امروز در بیمارستانی در حومه سانفرانسیسکو درگذشت.
خانم پارسی‌پور که از دهه ۷۰ خورشیدی در شمال کالیفرنیا زندگی می‌کرد، از هفته گذشته به علت سکته قلبی در بیمارستان بستری شده بود.
او در سال ۱۳۲۴ در تهران به دنیا آمد و اوایل دهه ۵۰ خورشیدی از دانشکده علوم اجتماعی دانشگاه تهران فارغ‌التحصیل شد. نخستین داستان بلندش، «سگ و زمستان بلند»، را نیز در تهران منتشر کرد.
خانم پارسی‌پور در دهه ۵۰ برای مدتی در تلویزیون ملی ایران کار کرد و سپس برای ادامه تحصیل ایران را ترک کرد، اما در سال ۱۳۵۹ به ایران بازگشت.
او مدت کوتاهی پس از بازگشت به ایران بازداشت شد و چهار سال را در زندان گذراند. پس از آزادی به ترجمه و کتابفروشی پرداخت، اما فشارها ادامه یافت و سرانجام به آمریکا مهاجرت کرد.
خانم پارسی‌پور در سال‌های اقامت در آمریکا نیز چند داستان بلند و ترجمه منتشر کرد.
شناخته‌شده‌ترین آثار او در ایران «طوبا و معنای شب» و در خارج از ایران «زنان بدون مردان» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tWN4O3RrPASGwtptkUM7IL6l4qmNe7Hz1qILl9MjzGC6j-spPGl6gQywoZDhGT-s7eY_X4QU-KIN4pz2LVqsAAuMT6LkqEHi9vUYn1cVYfbAGIexwUOxQY5iz-m7hd9roCYLjzROYgSnxsDG9qCM8sKIsxgaxLCHYCsE_9Y2XCJknCZ6IeRTECFJDyMB8m-WMgUXEIv-9eetbVmhJawJwYfDWQSDaVbuTwWsh3nkzxfKvPvL0erEwq3kgEh91aVOEos4bDYh9tM1mDsctGlvqZ0ucvpp6eF-AFXrbX6AVt9wtptW7uJTEyQ00H2YII77duSvs1sQUpb--hJtTKidaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f6WCz6zhZvxHOoLGaYyL63YJX46XeAsus2I7AWjrkGiT_e_ez7CCx7IfRJ9aWi90Q8gNsKwwNHjjMUgf5pkAz77bsgftEDuk7QdSwAzmA6dQmjd-HdH4_r9hkOR_cE-lBgVPDP9xem4xEd6pdvtz59K5MHvEQ1Z4A23e1GzyEou2fWSjNNALvdhlbiT1Ao8Vs5GZ-Bq07LD3w-bldv9dRiIGQKZEgfilCirRx2xFl5PZ6APTQXVsn_e5G94AjGe6YdP6_x0k1Qo4gz9mJfuQFs5yAspZH8cZV6wpMX3_hRykuBKSQN-wPBnV3V3QIUdPjiyGpMqZdNGev9wLJk4uLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=Keg0e-rZNTAucj3yLOhmcrU0jz1TAmxuZB0qpRUup5A45PmqDK_aup-77KU95SAFagZSgJE34QJ95MxVwpSHL0jW2q6PEN5_JgTsJuomwWWIHK716VR3GwNXjek1Et6zJFm1SJ_UYWzz2QCMiW1M9CW6E6utfQPlG7i5lkBA-q1jyq8K5-aEXX9QfLY6Ikqyn-dPfrnd5GNCnZ3hiCPt0I2V29xd7uWIfd4FbF-RzfRqqVvyuqOV1lQymuKkhNQ-SlvqMd7WV3uX-bO7dCUCjltGZi_GJBc76s-W2sFXiSjsJuB8ytGqMT9J5NDSiGTbx6eFniKoB8NfF-Qp2BYBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=Keg0e-rZNTAucj3yLOhmcrU0jz1TAmxuZB0qpRUup5A45PmqDK_aup-77KU95SAFagZSgJE34QJ95MxVwpSHL0jW2q6PEN5_JgTsJuomwWWIHK716VR3GwNXjek1Et6zJFm1SJ_UYWzz2QCMiW1M9CW6E6utfQPlG7i5lkBA-q1jyq8K5-aEXX9QfLY6Ikqyn-dPfrnd5GNCnZ3hiCPt0I2V29xd7uWIfd4FbF-RzfRqqVvyuqOV1lQymuKkhNQ-SlvqMd7WV3uX-bO7dCUCjltGZi_GJBc76s-W2sFXiSjsJuB8ytGqMT9J5NDSiGTbx6eFniKoB8NfF-Qp2BYBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=Og3M0zoQ-JTwm6ejiPvn8kZPDMAcP031oOg4itfc_SghIaazgBG_3V2CJc2ppL9gPPHm-b4e7A20rM99qqZ3MIaFAu5vNX7pOuekL23349q30wdWvHDCQ2cRseaNKjf00TCewhOPzI24bEvJ7KL9ujJFtJ2RE530gDlYycj60xDHyZHR-zyJvtl5-7YSfGd820CQOAH7LPAw7u8HDNfrzGwjIsKpXHgT-qan2Cyla7miGyOwpg3xUug5gv24HDp2cVSypGCyIBpJVgW_5Z7NGMlSH3-XkqFBkVGd2kWiJloHJMZw025kTkTGeqaryIkZOYoGXmyit-oPHsfhgdWyOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=Og3M0zoQ-JTwm6ejiPvn8kZPDMAcP031oOg4itfc_SghIaazgBG_3V2CJc2ppL9gPPHm-b4e7A20rM99qqZ3MIaFAu5vNX7pOuekL23349q30wdWvHDCQ2cRseaNKjf00TCewhOPzI24bEvJ7KL9ujJFtJ2RE530gDlYycj60xDHyZHR-zyJvtl5-7YSfGd820CQOAH7LPAw7u8HDNfrzGwjIsKpXHgT-qan2Cyla7miGyOwpg3xUug5gv24HDp2cVSypGCyIBpJVgW_5Z7NGMlSH3-XkqFBkVGd2kWiJloHJMZw025kTkTGeqaryIkZOYoGXmyit-oPHsfhgdWyOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 504K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLjtf29Hr-SuZ1uZS3kR2FFSXZlDTRTSmfgVcO_j88Rh9vzGGfYwPhjIkdPcWTUfSlEuPob-NmPT4X7UeNnWLUTOVRQKZ6DgVP6XWVEfshOvebddtgDQ4lfnVUHhFykuBFJl6LExEI3qCyLqNv1WrenlsKA406kT_of3cbfnCSchwctKbR5PkxBOtZ2UE7Z7M2sBqLem5hU-slZguWNoe_NWiTaPeKx-CUIM1bwjxHyI1xjuZSL81rab3eihbtc29Tz9biSZh_RUmUCsLkiJMclEBCRng2kkLnw5vuf0Z0H9qeH3QSkliusRV_Qr2zXyWooIeAEhBTwVsaEuioV_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvIAeUv5yEO53bDCM-_mcjsX2pE3U183kp7Jzi5-2cJf3vaqGceabRyc0IFS_kD2XBkiViKgXylSNkm6xdlL2kxl3-IsOVgco0sDBLHuIm5DGWI9Qo7WFb85B3OFE6gp09ehC7pnQtmJu7BA9LuE0Lp3e-xSUFaEnvKxFE3n5Tc3V4uAEv1SEQ1XkJfPz2s_anlLOsfnKziUkJ4-DJdcXNyO5Z2F4yC7a9uSppEKYV4MdnF5Msa8eYohWrRAcH-qmgkWRucuv1adN-lztHgLP_OeZK3se7Rt4sNPQzLP6TjQLBn__3pTglU9Z9eieN0FAC97vzb_SGlO5Xc5nfycHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arO-Fil-IGsB4o6x0wqUWdgqu8sjT4LLnBq9t8AXYGBqOCBxTiwSd6h_Jp4F_x50xUZen8UUJ-IgADToePSjtlnPiuaBZGmbWIf2hi5ATv6rvPrSeUu0vlyeIBJd2PUdaRGxhaBIVuE22xJ8xjl6RIzglN53Xxiglx1POAp4DO-nwtgrkg2UiDqk2ogof2PBR2TGyadOXw99uVyBdSKrXtk3M0ZjbjrIsqhLe73cWXIFo4eidJbfycr0v5c40sJLZRkFlwUtjHhFD3AZBZhwtggCBjBrrRmrQa6g-3Y_I4wdfvCoan5DgIt5iRXCvG9v9Ms2J_nE9Nez1OD-Bj4yRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPeM0Qp1gRj1bg4_eOERerKeFMQ4qighDfz01epxAp3ryUDnZf0wCo_F-A6YmpdYOErEd_fG6y7o1O58PXcn27jonQFCtYn5EumqGB462s_yxmywtcU1ARro6v0oOqSmemc-4aM7kIrmH98v1OOFzOXHYY1CwMP3cv0k10_mkfNMXRwRHF8L1fvzmGYDpYO82HZK0Q1pJ8O5GVOhTTo0W9VO8B4qZWF5hwna3HpbE0naU5nWzpaQm-CI7JxNKVGNPEltFFj3M5YrOJjit61UdJc3jjlUkXJYaRI8W1gVjkFqtpbssCAMI-m1Rxc_JnCg4_WRp-lTgaoyTRDTwYRAqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YogIs_FoOUvVkIbSE4Lys2qQ_UKTWl95HRAvP93JWf-EZ8ktvcUwOHweGDCETbPdOdBLMfNQyXXquXYa9r5Yn07e8PVKLejbu998zTePQBbd5IPGEjQb-kizWJyo1gKxVcccD30X5fG07XvuZ8NWCvJpHPWgXUS63Ok-cHytaX6JhJ4Wl9Piyh5g7SeQOtIQNsGAnZMOWakY6TspGhvYvd5tTqd5npVSJd6ijLmLmGIB54PUfkGkWmHJYYfBdBePb3yRTr4ec6fLl1T5BCQUGm__eN4xPzha4Ucjj-mBFPvSUD1V49BTY7y63AOZJtQC8WFaVA-xLdETJVxyW1SpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=uvvfQt6IxURfCe1_Py40hH2iB2nJhb9hJBet6ftqQ4nyUqjBKSJZU445BkftHK9zu-lO1dM-SzN0aAH0JukwnmuD7jHyXvgF8YOzSbFfm5XxvWG1q5SttdoVmay8ay_KHKvWtntH2FzmypYRZSb_3sfvbqlwDqSubGjssNDMGGwLSEh6a6698HvuHRAc9nnd5vTK39a2sX6aBz4bCdzwrXfuhvdskPcYwJljxrDhFEOdGNei2D93UCBOab-iW72Iwoi0m69LEtl1UBzR11y4PH7rGXZjBSWCedCcwwAlz3GVE2lPp1PPHWn-HRcxwa-x0jvnkjCQ3-9vLm72_rvuxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=uvvfQt6IxURfCe1_Py40hH2iB2nJhb9hJBet6ftqQ4nyUqjBKSJZU445BkftHK9zu-lO1dM-SzN0aAH0JukwnmuD7jHyXvgF8YOzSbFfm5XxvWG1q5SttdoVmay8ay_KHKvWtntH2FzmypYRZSb_3sfvbqlwDqSubGjssNDMGGwLSEh6a6698HvuHRAc9nnd5vTK39a2sX6aBz4bCdzwrXfuhvdskPcYwJljxrDhFEOdGNei2D93UCBOab-iW72Iwoi0m69LEtl1UBzR11y4PH7rGXZjBSWCedCcwwAlz3GVE2lPp1PPHWn-HRcxwa-x0jvnkjCQ3-9vLm72_rvuxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I-qr4xIuqH-8FE55fpLkEF6_7Y5jkWbX18OG7_6r8sdq0sLTlDxWKF-N7CP1_Kc2zVedEw4-NL5ZlOKayODc9e-6gTon7k_q3-QvG6NCINpj8hOZ_NFf4GqYMBDGst63w490NBfZzl-U6j0QP4ua79_x-xkSP02kkyY3RjkHra0nWRPo1rI7MvHMDlZcuO1aWNqCiVINY4zxU-N5SC35-cENHfpDI5NhII9FNwKROcpsJ89zqva3OAWdg7PwYWM4jMffuWp1I-_En7QZF11nQFwRX8HAbwzMFFRw9YR4VTLSBHcElmu-a2BDFLRoCfAC_UeymmnMKggCy1wfiM0c4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tjLhnxjuTuOT8qJrLbIcaAcm841NYMv45_yB3Ulv_x3H5BD7onxxHSq0Sw0fPb8Q3XpVw5BpTEsJSJnorhILO9r1NjVqt1PWo1tFk_wWGtM8W_7W7Bmkr1j_lVs777s7GcI9DvU3URiciB-b-gQvTshW1nUPKIZxT63YJagj1Fd_UuU3ftueybwH1urOuta23qdN1seYqYkgfWzhvEWgmO8_PybXkEONVcti0rCTzJBR4PRKkEBXhBD6D0hrA6Eo5UV4AXNXHjZ2T2gg-ri-HthanNhvNrwruS0wJoh58OHPmwT3j28yWNj1NRrDuzqx1XW4X2nszOVIMKf2RrqGhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kFF2-Kw-oot2Lr5Heawff-IDNPfRyYY09IRrUp_ewFASREwyPaWnVuwpYfGyrmpQuorl-3ORAlZf9WBNebN_CBjLwnv59_-upeZ1poGP2-oCCRC9j3m3aUsACCUh5vENXqtDeNoOoZnkdD1GSLt8db052NZamtriWUOppbIH6aReK-D8J8GE1r3XUX5wze4yhqD_G8kDy9trku_Y8CCMwU9TNHa9wfVyjauAAalqtEiuLuhmtaVK8ek-aPB-q5O6bVM6AJQaZ6MYJjGqCheNXOgJi1jk7AQ5oGUneyDY0ZqxSwUxHVrgO98GkQndl5ZBPVEzRa4_aAJ55Lq5I-xagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=YDKBIG2MFrB9VDmutn3MekM1gGjEIk8bkUbFuAUnDzhbtXfOj_Xlv0ddgd3iu2CPDvVcl9u0K5K7KQUbx5KajMYcpMLju7OboZ1TpHHHUBj1fkY1lzhgSQSZrga86EEuiLda9qeYazyUKJobCpHuTuuyc4BlpHWfOgQbOoOfWx0SYBZM5VxyoeHdsI_FLByyCHvJtqhslu-Pj_6MeEegcv-Iv7MYsRg3T8vhgNGo2WH5EOnPQR57T1mF4oYMSNP2QYL4JSvSSQZ6dA3bsFxIebSU0mZXdir_KRX0jfVZC8xX7rRmzbjnOL2UWPIU-hhzYPqNftMyZV4Nc4MLmWYaJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=YDKBIG2MFrB9VDmutn3MekM1gGjEIk8bkUbFuAUnDzhbtXfOj_Xlv0ddgd3iu2CPDvVcl9u0K5K7KQUbx5KajMYcpMLju7OboZ1TpHHHUBj1fkY1lzhgSQSZrga86EEuiLda9qeYazyUKJobCpHuTuuyc4BlpHWfOgQbOoOfWx0SYBZM5VxyoeHdsI_FLByyCHvJtqhslu-Pj_6MeEegcv-Iv7MYsRg3T8vhgNGo2WH5EOnPQR57T1mF4oYMSNP2QYL4JSvSSQZ6dA3bsFxIebSU0mZXdir_KRX0jfVZC8xX7rRmzbjnOL2UWPIU-hhzYPqNftMyZV4Nc4MLmWYaJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MbUZaIL-f-PYmXL1_gWJFNwytf1EDofv3z1916oLIhRP26kcwDArAsQEhoeGAgWcGLWN0IMcK3BF-R1YT2g1tnjRrNbPcjsIHoHew6LJsd8hPF-JIblvo4d1ZxiyTSL_M35ITmKO-2T7Tu0P1cba87ADjxvd8VLOOrXQyBPZhBHKlb0U01pt7jzQf3MPpdKiSD2vtBHRUSrDhrSiFbikDPLiR3cuXhWh5ekzZt1IVDEvgB_2RFeEBb4NYx3xQnj10UOq1VyWP7pPxPOW_D_CM1v3xTB1dy5mgUeURcF9ufwrfUn7LdlIPeZ-cxN7O4qNF0fUOcQVd6gy9zS1rGTgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eKKQNHbJvrpm_bf54LZjrEiGrvUcmCg98d6FRjRuMhLaQQ-m8qbGiK_8ACYFC78ScT-4M7u8TtnG-CPks2OqfegxR2zDYYZ9Kj4Q5ZGJVwSxt4sPF1jB-f0oNoLAYVawLShw090v5_ZeBUYO6o4iB8d0zFZINzSxbVbbbpQ8g7pHH6ZSS4z5U6haWGSiWTytS5--ck_jiLvtcx696KJEjFU6e1N94pN7HQlVjsOaTsltQFfwA4Zxk3h49DanpwCd-lMYcpfzeA4GsoBuQwPogmjbCL7xKpw8lU0PqdlmaPcVYfmMzv--DmHKx4ONmLt6P8Rf1g0_8zR4I_oAIXST4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W7YTGAUE-qlehSLYoxV9aTFen1r034JpZdKnG9V6VaemDJ7mOeaQ41g4eAUUkLJb3yVJlwj1A3cvtEJzPOniqDiQmL0PTRXiYpxwECpDbmSQyHebATvnIAMMligYRUHKM3L0qJLvG_x12mk5jP7WbJNjSko2YWYqM7cP7cN6jXzFQ8al0U1VXmNxRgff4U9OA24nQJKFFl3zqqiEnHL64X3Hs9g-A6ptC7rZJOyysI9nxhbx-ET7hIw2AuMX5Bxp56NHBIg7Z-N4lFjItSwiL4fydI5Gxvi2-HGNCeXaz1Q4zxMTC-JmlbO-AU1nFEYsgxV1-oKbymDiz_jcCNoDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C2Pyh2uejgo19sFOKvOt1YoIcvpZDwgkMeFcq32p00nNDj6CBOf9XZgWT7sjdMJiJOHjLHNAo4uevQTPymfwn6NapYxyT-icJLGXHo5X4aav6ev_p4lFguS0BVK3oPahgvY4O3e8TOq2BFG964eaO46k96OREYmCwIgLg0xyep4WSebgdklOVLZ7dolqAZRmChiNLjytzqaDFg-KtJ0dYxAQ-Y6ccgC1DaMhYNZldDTNMjkbVTyED69eq8bbqjGf5_cHfSILuijvj77uGRztadwSd-P0EkAvfVTgDEaP2b4PgNexAictlYUrhA0OrXAebrLjp3VXUpILJqjwy6Kyrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m58ZUivZwLzzaooVuyRsUSoB1-_IGmgAcMZvyndyRUoWBy-KhjCnr-WJkoG_KYhQfbB-Xsh2bb65yM0ea2I_OEzRo5-1YOhrBwFZyE3n78TSO4xO3RqCAfGi-sPmg914CJ4vydSjvwH8a5rQZU51YUZbOZxzR47df4ktErcWgdwjIQaTaA6k4Ovy9EL2l5Yw3x3RL4zV9KvN_omtpDO0c2_hVHphhEvx84-XoWX7uGBHtuUsnWdAaPXWaN_NWHfTr2fSK5BgyI33xOYGC2sAuQsbzQg4TE9EkEmbrSAKyAXcZQyXFoPt6u6TKwNsqm67kuZD_20GT6x0eg0uP5E30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cUEoxpFchxB49EplEvcRRkMFVb7BJzYLN9Dp4yQrzVMiz9ra-2-vaZZjldv7GkW0WW9ESI6KSqPkGkZqzZ9WcLChQrUMQursDiB8QPmus4EHQwWzreVJzv0bxqXUEfOPaMAdmWImFloPQq1Hum7CdFbdOL-7M6JqgrBkGCmizWf6KLTYN8R6aYsdaEW7FKAiyGZEv-lqkrHwBUmuyXzWB4cHc6WQBwjCrL6wXJwphF6RfFEvNwJjhjVsMmJ_QofFQdfyihbzkqmj7YuwMrkWLDhvBdLjmt0cZBIAbtZpD7S2MJtR4JVZzC2zaP-Ot7GATUdh-X4R4__gRTfF4DBDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
