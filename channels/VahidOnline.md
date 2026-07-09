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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 02:17:25</div>
<hr>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbTHdzegxh7dk8DFvlXCGZ83eA4vv3PpuCPL4rOYTYyeYNDuG-C0uJVmwubDIFMLQW0x8hnEHBNIbK5jO3wrJe_kbj5BBEUd7Eekd8mVsdq4qMh70Bjjf74R60Im7g5_lFv3V2pCfYanu2GgJBXOuaIVrzoj_QszvNJgpEpOnTRLk_zbbluzXuYo2zKkaFUc2L8zVSQnRtsT-qn46qUXZUTD0JW_5XV_L8nAVOYUoYPXSFReFRyxuq_tqZ2PTzu-HzHh-7TBG5a5ibjJ2MMF6RqDmsuGVEFA6bJtqZ7jfK08448wwb3IKrBK0j7WaJfRElxo_lmhW2VsXa_iHgY__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t3bdAjNRZekUQtnqmOnM_cK9AywuXFe5T7vJs8t5XXp3w3pE9aBbdgIKNs5nBbI6IQrPo4VgyXryLF6MSvLnyjTgRToj9KoTpQLNRKnDM3efRskJ59y29-0yoKmPilXI-jM9PpoGkQjBVsVkfJxomL8bvvgVhLLxLMKpRWvACoSA1iSuUxbkisiF1jQbNCZ9lCU7L2nO8krqqwEV_qeFgfld73CAYkxEBhPyBS6JOuMmZEIisqVEq2-LD7M0rJS5QVBUgyIn2OvDEpCZAzvhdz4AjLBpvW7ELsqKvk1MiCUMA4ucCcb2OJ7tybtf-Oz6t6BJSmG7S3IVnMqydp7tEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hfSfM2fK2TtZDl7zKOIb8F3rbVvFKw1rZK9D0-_Qb5kaYmXDvKcUYkVu86_siXEbwyT_TY8SqeCTr6QyJfLR2PUJ0acZGRBixHKcIw5qho4mMYGQWEy0d1IiLJCFKdsGZr60f_pUvj_QC9lqIjFzbuyhL1uXSk_2ygRnrISB2dBuXowJGXGJUHyIum4sY_cmsmZpvzpoh7K3xSoEE56l94IPkDOiHjJu3mr8ArOYLO9HITSmJBAMTQN6N-mVap1J6gKyNPjuXQ0ci1DPpgNv15g_H_kbjUE6A-u6nfkhMIRd_gW_Vin44rgZ7F6KN-hDMch78o8FWwlkM1eJnA3yGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHuudO8BSGKxkcbL-wwMMKqFnFk5Q7CNmOXOPvpT1VoiFiXNQ45EgP7Cc8cTW6kClg5SzZd5uyQHZXRHBXYpdxwuHbQtzD0_NS11-EXTg7ifGc9Krqt9Nxu8aoNNBrnO0V6r4IOg1FJ_S_3cilEU4hWkHscy-9cxMOmRXzXvJx6tiRqppO0PNymtxAlXgHmEM3Q6Wdr4L55HqF04VM5Ei3MfT30SAgym-VYlwlRZjooukEFcl65WbTAiShyPFGJpYFgwTUBgo-epu1QzT9JmPkIFSUwkC4jTMA4wRCrox_V-joYGd-Bsg6Mnli5tBtYAp961Rb81bBEmmqyWNIH41Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های داخلی ایران بامداد جمعه ۱۹ تیرماه و در حالی که مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی آخرین مراحل را طی می‌کند، از تیراندازی مرگباردر مشهد خبر دادند.
به گزارش خبرگزاری ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان مشهد و قتل ۲ نفر را تایید کرد
براساس این گزارش امیرالله شمقدری، با وجود تایید این خبر «از ارائه جزییات بیشتر در این باره خودداری و تاکید کرد: هنوز علت حادثه و هویت کشته شدگان مشخص نیست.»
دقایقی پیش، کانال تلگرامی صابرین نیوز نزدیک به سپاه پاسداران نوشت: «بر اساس اطلاعات واصله، این تیراندازی در بلوار فکوری رخ داده است. دو فرد ناشناس با لباس نظامی و با استفاده از اسلحه کمری، شماری از بسیجیان را مورد هدف قرار دادند که طی این اقدام تروریستی، یکی از بسیجیان در صحنه و دیگری در بیمارستان به شهادت رسید.»
خبرگزاری دیده‌بان ایران، نزدیک به اصلاح‌طلبان با اعلام این خبر نوشت: «مهاجمین که با لباس نظامی به سمت نیروهای سپاه تیراندازی کردند، اکنون متواری هستند.»
@
VahidOOnLine
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
در خبری دیگر به نقل از منابع حکومتی:
شمقدری ، معاون امنیتی انتظامی استاندار خراسان رضوی:
🔹
این حادثه حوالی ساعت ۲۲ پنجشنبه شب در منطقه سرافرازان رخ داده و حادثه تروریستی نبوده و انگیزه وقوع این درگیری در دست بررسی است.
🔹
براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم نفر دوم نیز جان می‌بازد. هر دو نفر با سلاح گرم کشته شده‌اند.
🔹
این حادثه در منطقه سرافرازان مشهد روی داده و وقوع هرگونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم رضوی تکذیب می‌شود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4okmdtmWnkQXcThbba_8ueqzkD2dQJW4k7THLSwCX6qeqP9pE50hPekZBhzeWcs0q-ambWU9h_uPP753iMch_NOs0xeK-uFhZnHAaqozX2dORuyKmncTE-DA84PT5___nC7ylUcFtpsHj_OVUf8d3nBaxjLwNu073Jdh5QnsNMZK3rb5EQKtyz27Xw-UYVt41JAZ3mHq2sjKuM7jyxTHv6WgztkRtY4Y4LlfufTtEl7lAVW1tms3bhSd1ymgD5hyGIwT3vIESC-mTXby-6CRQ8MDhdB4GIdGnuF4eWjfUV_DhWgzVARNvh0DrQd4KU7a1ZpPxWJgo0exeVWIHQliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qpm9fT_09MyC498mhsU5lMnkO_5l-foN1xirNlYoJiP1MhaHz7_Jt8e9UKznFIvsyZN9FU-8mvUj45RxOJkRP-vMtUXAhe_4fZGjG-_kplT3wfJ5n2NtgUbrg17BpkD9nBMuuRENCvOuJfROKEW3j9CuxAw1k95Pn4xG4jbbVo4SySEiRWV_vxiiX7Dqm03XUadIb7CjfQYS7JZqMGMnhKSS2fGTtdn7u4arvQCHdF-Yoaa7du7GUw4yns6eLCuC8DOaQ8cLoepzdvj_bqHrvR_jgNNxTqjhIviQ5xghTKmHmQy--hqosqtPYOi9DtOm827SJedP63kV3fPS6Bg4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5vnGgTnZbxdVauakF11vE3bsgqqJxSGgppEUQqoCyRVNe-F337h2mYnsncvpBzY7mlx2Dte7c6n8DNZwGykYwjksg_Tyqm9a67iQgdgf3197DSch4GVgzqRkdGb0i4YR3Iw233ITVos-UxSodufldhmSJBIalrOFvJwdYNIOE_XRAASumFZfMoZYf65wdnpvaVuE3T0PV7IPjDvhcy0X2bbvZ3CBcCLdg4Ilj-zMjQYtM1qkURieNrsymP9SfR9Y08O_X8Mnzu670Rx_YgU1Prsx11jaOIqXdgZ7TNXOZ88V6Vfiz4XBapXlZ1X6ftNu9mEQXb65lLAsLuBlwqWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v6bUafNSK1-HSzGpueZWFu33VIFRnqpAM3dbHCWMrNARA2RzzEQ0nhkE3whSTaPdXS-46_FqkGoRpF7HUcoZujj3-ED9ha1zu4j4MH97lH112llJXS1H3Hsj1E0hU1gZoKn49gxvMXiVA0E4yUGYpQRVcozd_lW2O78sw4NRY0t-EGIQazTYyWsfkubDfRBA49ODMbZxQEPBksqgL2JNdAto4bgo5HDdbg4ZGfQR7u0_0PhdAq5lV7dzPf9YhPY-xsBAp-Il1ChVUdXYP6NUIypEeefKa-ZmDcWmVAU54yvNAMClLwcEsjCfTlro2flkacFlu51540YBAokhvaWmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYSfGBJ9o7c0ApeunYf4B5QXwv2cIFXEVEvOto5R_-y8bSkw3cBHhR4joOZvpqxTVN0NVRsImtAxh6eMckEHsGlIofikerq24xqRJ2LzUilUFFH0vVpVnn5hjKL9d-hItm8GSAQY_gflVanlTcHfOz2dY-tR3Ft-TEjaYbQBbzCKQzV6aNo5lrUTgFWUBcxximTRUCiDZVzDB_0G-c9hoxMlb_h5aE3KIojL-P9GK0u8FsggqjikXt8m7KCB11fXXL-IHP5lxXolw_O0VYow2qCh__2kEWAoFonw4bINE5-l41puQ1Dz5oDxT5eT3qSfSW4OpQy1TnV1YYTRvRQP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P-tnpFu8iitbY6fJYF7n464fc_wZMl9fYvh5ItC7v-hVPH8dra463B79DerKziC7jKFyQRhGE5EKg-tYKz7bKc7T9V_77cH4xMB1Lop_5-r-PVtK9bED7VN9___8W4YTYHVj8tufD9vjARX-Zymk_JgmFoN4mEJSxc5hgdaqM6NrI74623gBBELS4ngOhI_iMnrToxsq0_o2L0wOUkASFk98cdkEnrgGeqMvUcIw69ffqh4fDi0UD3TIEh2NXNS2ebGlQ3KuL0tHM9wqRCfNnjRbt-MN-PfG4VySpEVskddB9pssWzDIkuzrv0EMfNlXlCirbQiOGPjqawaXfXILPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=E3BjfR1r6I5aZz4iKEeCoSaxpmtEg_VGwL3sAKHpbbWkQHixK_oUV1mFNJIiwLRgsr1jkDFwyy90bsehr9EucKjKb3uoMOIbesEZFSSsmWXkllJhQusP5f-jcJJhtiAwsTGl8ArqOeombvEn13zu4DofiRLzQHenelT3BPFe3wNUfiZ-WygDXXLnkw17W9-JiLnLaJrtm9FZQsRSLJdHunvRRXyM27dgTMDFoTfsF57gFEitj4eX6xQgBPtExStX8i8HPO1F1zwKkfEMUMs8M5Mj00eQZuB1ZAqiRPuTvHXFD08kkAeedI8ocfOHVukAfVBzqpk05N6s6dVP1FmVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=E3BjfR1r6I5aZz4iKEeCoSaxpmtEg_VGwL3sAKHpbbWkQHixK_oUV1mFNJIiwLRgsr1jkDFwyy90bsehr9EucKjKb3uoMOIbesEZFSSsmWXkllJhQusP5f-jcJJhtiAwsTGl8ArqOeombvEn13zu4DofiRLzQHenelT3BPFe3wNUfiZ-WygDXXLnkw17W9-JiLnLaJrtm9FZQsRSLJdHunvRRXyM27dgTMDFoTfsF57gFEitj4eX6xQgBPtExStX8i8HPO1F1zwKkfEMUMs8M5Mj00eQZuB1ZAqiRPuTvHXFD08kkAeedI8ocfOHVukAfVBzqpk05N6s6dVP1FmVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=kX-ns3h5A4AGkTA26wF5HRgNsaex9wPRcdbx3PGGGqUTH7TAb4cT36PZND-9N1WveG3roTch8_RHeRTaXH1bNLKf2Wvds_LysNTayAqlB8pWJZGJjM2c4Md_i-XrrQewZ51Oqeq6O9S_t3ToA6DWZcGSkpkxrGrbdRvQdebWPFslxaz4eMkr040UY5axutJ_Xr0DTyEtYl2p3nb14qii3pz1iLIMAIvV4ULTWmbynmris4BSnMKkewKHUOtKt53UNk0lJ23NE_gwgf4mvQVjG81m2OYPQHZ2q6NKgLMNzBJQuLE3iySW7dSZybN2lGOy_11R2lG1rp44UpMyiZs8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=kX-ns3h5A4AGkTA26wF5HRgNsaex9wPRcdbx3PGGGqUTH7TAb4cT36PZND-9N1WveG3roTch8_RHeRTaXH1bNLKf2Wvds_LysNTayAqlB8pWJZGJjM2c4Md_i-XrrQewZ51Oqeq6O9S_t3ToA6DWZcGSkpkxrGrbdRvQdebWPFslxaz4eMkr040UY5axutJ_Xr0DTyEtYl2p3nb14qii3pz1iLIMAIvV4ULTWmbynmris4BSnMKkewKHUOtKt53UNk0lJ23NE_gwgf4mvQVjG81m2OYPQHZ2q6NKgLMNzBJQuLE3iySW7dSZybN2lGOy_11R2lG1rp44UpMyiZs8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRzpc8hvuOHqq0NSMw-GAhpZtm9fkIMDK1ZNxUHW2rv8kTv68H0PnQzpwyzuGkzBy1ByIvcQWsPfzOJ6ZC0bT2UDTLpFvSFKf9ab0BueZGiuWjKj5RQF-pYqe4wVrPdfMQck_nrW1BAQMu50lVCHpt5PXctAqGIdO8luYuKDCCbVjV2MVi8IF1P8RUeTnFbty7zj0kbCHs97xIlSW4f-17UHyNJV13FsivvW9XcalwTUITIJSrAQ_1ZUFSw8548OJXQXq9UnrT8mzS4B23osATo2zZs456GE-R4P1uAQsfsQjUMrYibWFdGny6huN99IV--qDjgppgjAlzQAndf22A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlLxWQg96JhzS4BShKT9MJ8BVlKRD8JAWWOxILBailWywfc4oDRgYtS3e9SOvQy70H6SW747qgIvDk61Aq9-Xm3eMlmKJ63HITj0YWeutRKzfrlmGE_lzQDDrIaM1CFjKucPFLFZVFZXZTbXeYOvii2V5J-FbQbDWZHvxzujVkEpQkNyTWMBlT_b4LDPDttBRj4p_PwJnZupAiX0A4-jcrNiH7jO1L5aCe-DP6NzY6jQ4UsgwX2tea2N003tJ6Wgpp4byWHFiHI9gfm5rGCITIgjBTc7Ngcb850zaLIn7dueuHG68PSKuvQm5chlPMSdvp9EIdZHYUYx20sv6MsS5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=l45WfZGzaBpccESTPSVgty3zc3GkgG-PqKvvZ_u7LmEAn9G6SVBxM3PEk6Ux-Era35ral3-Brj3Yks_YYVjyJf5nQIj7veGCePYzCUDzTr78rhe_bhIHr7pYqESCUH3UcDSbDuvkVnveXooUBmL3ygtJv2kYPN0vgcWVBok7EC-EeLJEJd_i2WM1YYMtZpE6xfSTV8IjPyNZrzAL9kw5I3YPsvnrTkDps_LUWxWuIa7coKPyaJl89cEK1NTJb9DzdzWeXJz2F9PywIeMoafo6SpJfyZd2IKjEJF--0fy9dqNNDjj6hZ2H8MOXHJLDdjUHp_zcPDYxXyv6HQ3Wsg2gw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=l45WfZGzaBpccESTPSVgty3zc3GkgG-PqKvvZ_u7LmEAn9G6SVBxM3PEk6Ux-Era35ral3-Brj3Yks_YYVjyJf5nQIj7veGCePYzCUDzTr78rhe_bhIHr7pYqESCUH3UcDSbDuvkVnveXooUBmL3ygtJv2kYPN0vgcWVBok7EC-EeLJEJd_i2WM1YYMtZpE6xfSTV8IjPyNZrzAL9kw5I3YPsvnrTkDps_LUWxWuIa7coKPyaJl89cEK1NTJb9DzdzWeXJz2F9PywIeMoafo6SpJfyZd2IKjEJF--0fy9dqNNDjj6hZ2H8MOXHJLDdjUHp_zcPDYxXyv6HQ3Wsg2gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=Eu-bYrrSiS3IfjVbAz-YoWuj_SRfG_8oVo-_Gfc8BV1pjGOuWIjPflRDesfrWHnIJh7YvyKzi7fAiYNNSCK-J9DITXrXRqFBtzFK4S6tGk4mEb3P18EMI8Z485VEzurze0IPnoY1jnjOhBuVSXNn4iaRAf8_JxhqBl5Kux-dPzkvO3uU4371xkqvFCR_bNy09aYDdQa0_uuDgXp2gAM9iUxM_eg4vC0M3BGnML3VmTJA8XugUwAlKJgIbp644476gbmcK6f_oVvJsBLZZEjlqGIKsd3WvzOqVyljBcOGi6MrERHGuzn5Cgb57bT0Nrg5AWsordcbk51XDH091rWMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=Eu-bYrrSiS3IfjVbAz-YoWuj_SRfG_8oVo-_Gfc8BV1pjGOuWIjPflRDesfrWHnIJh7YvyKzi7fAiYNNSCK-J9DITXrXRqFBtzFK4S6tGk4mEb3P18EMI8Z485VEzurze0IPnoY1jnjOhBuVSXNn4iaRAf8_JxhqBl5Kux-dPzkvO3uU4371xkqvFCR_bNy09aYDdQa0_uuDgXp2gAM9iUxM_eg4vC0M3BGnML3VmTJA8XugUwAlKJgIbp644476gbmcK6f_oVvJsBLZZEjlqGIKsd3WvzOqVyljBcOGi6MrERHGuzn5Cgb57bT0Nrg5AWsordcbk51XDH091rWMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oY4uUbiOwG-3-ZyBVfQ-YQNy7v2Q3hTPC8rgQHuDLBhqeIVo1IBAo9gx_cCnGFTpIZssju17OR6u0AOpHnUeoW_C1OsGLLcQUtH6oaZyk_rPOtB-OZzqdYyuaqgu-KcgAp_wVcU7ibfWmdmlAEUKiRsRkGPe9NTC-Pj0e5JbV_FlRFYBxEapXM6GkoeSpBaGWK09a6XkLVbL0miI-VZqiBdM7ggYb400gGz98rRy8zHKexJ22bKr_A9kut4emvzJQcdAUy4UwNWMj0ilWEdRpz8AWLBaRwcY81teW47h5RmJK9b16Fvsc36NWSI1Fw-Ioo3mFHbVU6IwXTLkQ_kHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=eZDlkWyUPEQO8qbd1v9wqZyf8A8hcOT18TtzITcv4h7Y7xwttRxYldY5BXoPNXBhD2UJ6-R5ooH6w16wjHjLcsKwxJxsgQARV-A0OLm4VfxPNzeH0vUctch4gto30_rX26in76Bm9LA2x7YI1Kv7S6X7wVpkwLUr0-2ljopba4mIlXjXug9VilcBQFMUkS2BuA_FxgSpuBoeX3Qv1XzB5O12jKs_uqYXa6KIZbnv5UzjbqC9asQKuVTIj1oaKF9dhsRZoxI711hxhzr1ZT5Goiou0x2TXfBbVjeyBVoqWEpWaNVBxx1kt43gsVFmocbk9oMmS2J-hAkgZlfYXJm-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=eZDlkWyUPEQO8qbd1v9wqZyf8A8hcOT18TtzITcv4h7Y7xwttRxYldY5BXoPNXBhD2UJ6-R5ooH6w16wjHjLcsKwxJxsgQARV-A0OLm4VfxPNzeH0vUctch4gto30_rX26in76Bm9LA2x7YI1Kv7S6X7wVpkwLUr0-2ljopba4mIlXjXug9VilcBQFMUkS2BuA_FxgSpuBoeX3Qv1XzB5O12jKs_uqYXa6KIZbnv5UzjbqC9asQKuVTIj1oaKF9dhsRZoxI711hxhzr1ZT5Goiou0x2TXfBbVjeyBVoqWEpWaNVBxx1kt43gsVFmocbk9oMmS2J-hAkgZlfYXJm-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wg4DL_lzaSE91tvJxBfq4oC1u4Pq9SHXIMNVPU5a4Gf54EUqm2Aox89HFzi41WpsDokpYnRgn5YmFg1Gm-F7ExncD6qwMS6tzIobFYpiHEda3bwwzhHH_9OgzdveLQ1XwFEaAXNIyHGU2anivriB4NorxbCxhOHZVyIwNuPvKX7lnqe1uL3IHVSwt7jbaVIzCyTezWEKiIMIDe-Yp4BxJTU4NXdT6sgFkmEqvLzOv-jppJEHg9THhn5WxVlvx8ms7D-7yBv-kJQSpZarK8HEbdKHV474pnGEAFX6P9HGljnF75UC88euOfHfNmlsgz-cn236JSdukbRudxoFjeK2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=MQVR5jrPo5ZJfDUDA2Omtd5jU9COfcDphyLliSXNmhNxpy8V6fmBeg1XCI3gDglmsfcBwGp9u3S4KYuaB2rmMJC6fFG3ijYv2vPObpsTuL0wnv2G6CRXnl8tCwVGJOjPN6KtUvwzq8QjmLz7mQ_8uWSiQsSiOYZuSXINnB3Sp2V2d7DQeeVxXmfw3iUYuOb0zbRJmZHQIKMn8mp4PvNJVezBQFqcS1ut6XJEA5GdmUBhbUAimJ90b7j4akAZOxGSK43NdDXaTzbJBew5OJysDJxbUmMnD3StNiqRvEHmYl8zWxzwLU8Nrjho1cIpPuhQPTI1sK6VGP_exABpfsHQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=MQVR5jrPo5ZJfDUDA2Omtd5jU9COfcDphyLliSXNmhNxpy8V6fmBeg1XCI3gDglmsfcBwGp9u3S4KYuaB2rmMJC6fFG3ijYv2vPObpsTuL0wnv2G6CRXnl8tCwVGJOjPN6KtUvwzq8QjmLz7mQ_8uWSiQsSiOYZuSXINnB3Sp2V2d7DQeeVxXmfw3iUYuOb0zbRJmZHQIKMn8mp4PvNJVezBQFqcS1ut6XJEA5GdmUBhbUAimJ90b7j4akAZOxGSK43NdDXaTzbJBew5OJysDJxbUmMnD3StNiqRvEHmYl8zWxzwLU8Nrjho1cIpPuhQPTI1sK6VGP_exABpfsHQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=RKQIiIQybmdU0iRyiXvV1YmDS2-qEIyoJcqB2LLO7HN1bPUjIqt1g-GaWJrm_31JzMtyKDC5ctDKGvtitwCF8NACBqLgw8_QBMQBSXZyP-jNfFEzO_23wt_HmZGSB_hezCvIGy0Z_m6Dtr0Waanp-Sgqx4347oCDpPLyFTTl01XkBtbUShavzo8OF1F2aypUOTyqMCUW7e9tfRnT70VIoRjz7Nk40ryhn0F325l2GlCTsYkL0LgL1_3KJq5cTl6kIFElCwnRyxrrurj_g-_IimrnG3sVOTWdZk4fjKM4oJq0KOaJ9OU4ee_5yxOJBWZsCEz7K1XhHopmG7mWPjYD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=RKQIiIQybmdU0iRyiXvV1YmDS2-qEIyoJcqB2LLO7HN1bPUjIqt1g-GaWJrm_31JzMtyKDC5ctDKGvtitwCF8NACBqLgw8_QBMQBSXZyP-jNfFEzO_23wt_HmZGSB_hezCvIGy0Z_m6Dtr0Waanp-Sgqx4347oCDpPLyFTTl01XkBtbUShavzo8OF1F2aypUOTyqMCUW7e9tfRnT70VIoRjz7Nk40ryhn0F325l2GlCTsYkL0LgL1_3KJq5cTl6kIFElCwnRyxrrurj_g-_IimrnG3sVOTWdZk4fjKM4oJq0KOaJ9OU4ee_5yxOJBWZsCEz7K1XhHopmG7mWPjYD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i_4tDcU_kXtTCKHui1wlRvmtRKXZ-POPmy1Ge9nVJgoUPexaNFQHmKlkjWVYuShzk9G4-Kr5Dmmi9JryuV_BQ5JA4x41sdLdJAiTOgc1qRSCuA9C6S1RGjqADINlyACH7D1xvmvxoQV40XkHPkC_v9H5hlQq7vtcdpEPfgQ3eDFHoWda4TOQh9dPAYNDEbeQ5znRBnMC8dnG078CYZRdLaTktnaFnbrC10ExIiAtUdQmUOfh8IWBZpQtkSltqrgKmXakTy_aNye17PWRo7J5muAqhNZg14bPamcAzAHThW4h8j7JheTITVHVT6AOVwhOjLIccHjSjMrlfCmZEuYP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5qOw7NdufL6KmwTJ8F3X9R_lP7YpMlOcTxATqqzwXIGwxeySvDieLtcib3tYhJ-PyYKDi6Ectiq_iZx1pBEdib05KT1iJGKjR5oEFr1YdOoJIe6AT-IRaAu782pxW8iGfuXdk0g9yktsXhzsDqW6CUl7an-mnwka4XVKHf2HRxWo46W0Da7dPngP5ClwGJcbTTyu9o1LRDVI5EVUJbxN7I5Fjs_zY1zE7PtItvSmrkWT8-L4a0KxRNhmD--QhAVLXwtzCewIU3S5mXbZlDpts3E0xBJAeYBnyYXL2lLPKxnP3DWUQxINoAzC1uPKjfaSaZbxBpKFuCKjLG_5pmEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pyo1QG8H79abIaJhYDj1kPvGQNpPhM0nvU6GJDdBFOYQgWev3r-Y0Zu5O2dOoQuOFUjFWAju134GQQbBbvURcE1SqAtIJW2xcqlAhU1F06GOP5x7elIV7hjRrQfQZSFYqjiZ3h0bPxAbDOkH4lJy_qN5oDXdur5GQeVhPW4ns91LsDShmGxRQHepGb4FmN2h8kFDF7vl1Ib2KHdtTe-3wLJXILZU0wohnjMRsTsaCRVn8O4h0VXGG5nY7mmhuMzPfR1J2TG1BUXCl3sQDCe9emdUBELwsMEgIJ8KxvpWLOc7coqJRY1pW70cQekL6Wd0aTwvvYrSdsr9p5Otg4PMrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=FGwaN8feMLOs6TA_E2U-CGhAfcZoXekRI6UG5PXmFH7Js4-BpedyzYeU08eRIRgKKE0rLw5Vi_dvJ3qi3g5nra99tkUKALYDoIkdidDz_jmR4ZAdPuNS5FJ_gt-Ka2YrCY4ph4tl6HD-317hRx0vUvRoH93D-5Hoz5wSP5mtEZIjm6l8slxvRrklh4PKuJogqcboC5HVUGk-xgpZN9k_elzHACgMataVxWuDlRSOQRi1H2JMfps1qG4_kpl8iybsR5cZGdwl30UrDO2YWMaxhbawqpLJ8BxiBBF-GugZMzHIL9SPh62iLHeXqAzSXfohJddnZoxXs2ucySNTOJjvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=FGwaN8feMLOs6TA_E2U-CGhAfcZoXekRI6UG5PXmFH7Js4-BpedyzYeU08eRIRgKKE0rLw5Vi_dvJ3qi3g5nra99tkUKALYDoIkdidDz_jmR4ZAdPuNS5FJ_gt-Ka2YrCY4ph4tl6HD-317hRx0vUvRoH93D-5Hoz5wSP5mtEZIjm6l8slxvRrklh4PKuJogqcboC5HVUGk-xgpZN9k_elzHACgMataVxWuDlRSOQRi1H2JMfps1qG4_kpl8iybsR5cZGdwl30UrDO2YWMaxhbawqpLJ8BxiBBF-GugZMzHIL9SPh62iLHeXqAzSXfohJddnZoxXs2ucySNTOJjvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EOPgPidcnZSNpasRvM-XorYK5klLBtF6mNihQ-0MNsvwxtCSd5wk3KauJq9VudW-lhmrplxz6mMIty4_GVgmBI5BxypqoxSGvQQnRscl9kPDA_JFEcm8lum3J8EBzJnFmigdy-OTA-Qq0Lg_LRSQYit8TKq37XsPOCFi9fRNp_p4DmhpzuGv-eoluWwQ829Sf3cDB9DjqOsiJkaEcW9jtI4w1wgXCE6LTDxzzRZWBe5sMfyJhEwSNQuKpEANwn8p42YiN7svnUqWnszGc4CPmITga76t-EeuA_6Pi6CvV06xaIKd66A9ZNj9HgzAawwqvK2kp176EIG14TQQOY57gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjKRAmLVUrMCL8jaDqfYLD5vL8-_3pEenHl_BDc9a6FRMR3vBtCj4gtivcn56taz3IAvYA5Kho3AQyTDlvDODkG47LjhuAglbjwtaBVQKFTiEjfjUtFO-F3pONg_0XxkF83donGSDFMXp2TeliaA7uKWNqQO5N8AJLjtadaRmk1K6M4AWHp4bSQQS3nPgQHvMd1mPLiyCoHuoWg9ywABc6JJSLXfUp_lS_s9G_EJPZDB7t0AB30bUTMo0EidgcuTpjRWrsAizzlFUy_EQijI-s7tb1xYw7wXf7aD1PkPp1YghHPyVhZUSo1jsPRGYUS7UkQmnjrskaa-ULy5Pnmw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cpZqRbmOC0RkMQSr0QYIJPulMnwIOKQwvapeF7FV1y4jSfvq23HPE9BSs5XFqbdWIbp5b8BIip1O9AfRX0WOSV-zv8C9KBaduKxC6_h0XdzqSRKp5CtIm4v6CVYxPno9QCAcq4uiOmGfjXx5qULyWMW8nDC1TJoN7myDUc_QpArbJ5srcV320Ah65ioUgegkbGsvAY3DCDJMFJ1kGDA4LQBzattGZaZwvH0JXk8ZcAOddWZFzaJIId63-5FdN1gwHDwtRaxw9v_iNAO9uYaEubCiAROzW2eMiDlu7L1nMFe38vfg95qKm6Ze4txtr930BT3KmNzenQ3uCTt_Pz4fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QHFb4FpaaSAJoMUvvsBvpQvlEsd-yWMsxGLZfa6binSv8EyhRdnubBbKA0tc9zEAlVE9ro2397VDvKT7hWKOE8jUGYXuMbQhCTfyFEnSd6coiF9hQy4VfMUBcm-Q1KmlpY5xJ_ngdTDZDMtdPYU1hFysRh1U4MGWSNRugl0T81VsX-rVNJ_5jpynIKojZ_JvFeUOfW-O4vmCfUJMtSGyqJElp2mnbYMgsMGidvp64NI7gNLkF-uVUjUTiqQ2p6pe5J1Toh-DjtkGEjAiZzAgrfmAsv571aHF4KUNildDqXTW4ZiGanTwQ6XBAXCajKIk3Mf32Jzw9Q8QZ4CFPGbf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری‌های فارس و مهر شامگاه چهارشنبه ۱۷ تیر گزارش دادند که حوالی ساعت ۱۱:۱۵ شب صدای چند انفجار در بندرعباس و شهرستان سیریک شنیده شده است.
بر اساس این گزارش‌ها، شماری از این انفجارها از سمت دریا و در محدوده ساحل غربی سیریک به گوش رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76847" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76846" target="_blank">📅 22:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOXDNFphzdHrj07GAO_E5aQHoENSsBqL40SGlbhzMEuBNHfX3qG4_5-6g7nyvWF7Bf6PweYgZN_WbDAScsHXfLEBmFkijRur5rko57ajHTBzycyIYJCGNc_DQUMx4opFgqy3wbJVpdvEzhBffY1AmDvzf3mQTGPqEQNSDyLKlNXNchWBssgTk7iuUQpHkCRyMUiBri9DbWeMvPqjYplIPA9FnDhBl1GCHDxzTespHQKeCBPbP_XsipqeGG1ZMo19fs86LCOCjtkawlM82slJno_srQbc9pr9-TM9J-Y1sRFCWmqQmDFNZ7uLHGUF9VcnNvO1XgMzCrZ1tHDglGauAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tAqe5a2aQ4Cm_d4aX1CIjxNygcbPwb1_o1yVns3llkOpH7rcBXSRcN0aD89fneX3hjwEtaWGCFlRPWBWyuM_D691Ah0pup61pXLlgbbccvL25EZZ-GbLn_vzxCqQq6zt3C3OzRZMBgE59XKmkdFxkfxb4sTEVl6HGx9flpSlbYgCQ2FnjJtKOnvJnmbETgtM6643kMVMDi1Ti2jZnKngYxUCBni9M8N122m6YyHanUtAGQXtmSrNH2GARzXmXw7eEo_S4GtrWUoGRf5sN9s4cL_y1vxBRR2a7N5GEmcKRBp_g4bKJE_V9BlV6Rfgk9H85pZsXh3JLCk0H_dFhcAUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U3_3zTj5WTIH72hGrH9WGiEnauzPVVH0HPYADXA2zQP6Hmx8x0tc2qqVp9FMdAUc8Rjka-xwQGD097ObLYj7VV1LwY2Wkiup8SpaLGZCBeKwiJQpzwyGvSY7W1mwwYxVOTLZdtduND5qNxMvcyhwr_t2gMvJYxGZooNEBQOHCkjRPCVemHcmFzt2qi7-_FlLOeVazuycBfG9vH-2DZaMRJvFn1VwEeW-zm5mbc5QQ-DMP-LG3qm-1E2FOiRd0HIn7QC6IWbVUWrhckaeDrVYhYXKQ9mr8WzAR-jZW9jjetf7h_Yxt6LPkTkGlIGK7p3bBwqNm-d4R3p6xxOOABCSnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=gTp9cQT-aqFfJ20EeN0oovQSTDhlp-f-osXAUUPjHmGiIDN0NAN5bzXpjj6lgPBH115JHQalwNvdiEXqVc5Fp8YJ-2tLnqXT1wmGb8DtuhmHS71yIjKC0OrTB-lbqeppWj0mQIVxbdbhYhhCdihohEUP7uUeXeon3v-Td0taUMbO2ViA-7erJyF7Qli_gYP8SmXIvsJgN9cLnqZdymZoeUGW-29liW3EKR_0VSl8rmzjAaumw6QRw5tptO1WHh9H5X12FTR4AePfPwK7dpDCKfti2JGRCUnWBDIGy9GBepJPPByLPYgQtnlkbYhk2Lw-NMOVBnecw73q2sSfXb8dzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=gTp9cQT-aqFfJ20EeN0oovQSTDhlp-f-osXAUUPjHmGiIDN0NAN5bzXpjj6lgPBH115JHQalwNvdiEXqVc5Fp8YJ-2tLnqXT1wmGb8DtuhmHS71yIjKC0OrTB-lbqeppWj0mQIVxbdbhYhhCdihohEUP7uUeXeon3v-Td0taUMbO2ViA-7erJyF7Qli_gYP8SmXIvsJgN9cLnqZdymZoeUGW-29liW3EKR_0VSl8rmzjAaumw6QRw5tptO1WHh9H5X12FTR4AePfPwK7dpDCKfti2JGRCUnWBDIGy9GBepJPPByLPYgQtnlkbYhk2Lw-NMOVBnecw73q2sSfXb8dzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fR8qJYi4e-JTo-0A-CqgmGW-tTnGSSBHgwsmUqUDPO1Q2JcoBCl_QxRw1_dIAdFBH3Q52fC1-qEiy9ZEJXA245uNGAhqGDoyZUJ29dO5LxQQ6jI8hoJXJr3fWxTFfY-optz2hU8wr1PkncmUMNwAwNDa_sKySkZpk3RvT-5k7seMPEASvt6Oq4RPhHhKi9ShaIAwlCpv42jTAbZxkNENZWkX5ViAun5cYO2i2g9xeXH9Hdw6ArDWdfarzI4IXNmhQKusvKxRRvuQZvtgLCkjK_7A7kl5RZaxbI_3jwShl7acumI6BCZnc45_4p1VVhiDChcspafHYneF8SxzZME7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NN2TOovgKJgVUDpyERebE-nZsFK3-xh2yLzkMFkQvwydFL_kQrNokVVwxaCdyW0e_eXsplRTK3IXkjXWWBvjYuqrqDbE0qZcf61hIevtp7NZYZ3-oH-9WseeCEd9xpRf1Z0xwN-r-tdAYPMpIlKgMWFvQr2zKki2LQHsBxI6sIhfm74srIWWVZXynpm_7oOgw3xUwvrwp5ZNvPQMjfUOkXbTeycr0OZIywE4PzbW3PFDH3Fs0ZiP1U_76NY8oFnm3lLxi3qYNgTfSVVnqIvCCXTHR2UdN5Az4NwFgggfIfKWiyEImqgDSomuik2Q0HFVYH1iGwuIIkELZfzv4HhDMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0y4tR-DEOB_td-DXBFVOKb0JylbGfo9xw5R3z12Y5QtIEUgw8I-QEQitruGWDSqNlprDfhKuqodDne1AlYxZ6U09g9Ncol7K4KXSmH-MxmhZ_mYN9lwr-G0K49QPDKnnvh00m--bIw3W0zz1GI8WsEGCTPoEqsva8uXXiHH5bpfQtoV86KmnRIPZf2YrYMglIuOy39hGy9KIT_XfJ7h2ibfTFIVD2UnVxTbNRkqNkUsPturi_lOVAekk_cFtpK520rW3jRjGK26cwu5MJbVN4j0K79ZoQpffVJKgIiP2aff2s6esTeWIMmQ3Yo5JHTIQg1c71rhTVF6kHG20rIInw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIKpnCk308VoBhyGZ9iWdZFxlTGylzFzxMVTlOtjt9g_Is2Yy9BXpbOLNRk4-XJHboC_Az5pYe5YfOojsEkegtsdKRJenm2BWChYYuYc2MHb7cSwqBLxqOJeSH9p-CSE55gHoWxdDZJ2tgkW80LTgP58qX_5fZFsV9AP82ZHTBmtZMRXpAKQYkRXMERbKN-iFw0uttNkqhrKkbiLKycJqoJMcOTBus-ttacfDOP9SGCg6mjmQxI82ssULMx5TrfpBXtj30IM25HFFUknXxm2v4OXa2TyeAeQDFyOSRAQFJFDFZqW6mqmYWAJnY7l87HNxZqL0HoCOnAE4nfL5Akzyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76824" target="_blank">📅 06:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=D8S_UCxctT-mZqdz_P06eoURmphk8rFxsjXR5-DT23k12jM7OJn4WjCk6tMbxM-YbFXC2ultd8UDuRqyNHdW3d65Xk1C9EGzqVq_HfEMcuQ3OvaVjGHbhBg1kKIxmxZdoKEC1v2gLKLS1adY7w7NjPrldpUJ5c8YwgLJrHKhDVepQuAKRTGhLyoa1-y-TxIxs6oBWqq5yMQsRvLB_M_sYhZOL94gJ6QMViORD6Y4OkFc_HaV8Z_P3t-HCQUfQZu4AeuI2xzkDj_EQ_-WE_6VMqAtP7QB0d6rJZXUGYio14yKXMgO2vjsrSmhE8eZKBaJqGuCZlioWyRuupPvi09l0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e118ef7ca5.mp4?token=D8S_UCxctT-mZqdz_P06eoURmphk8rFxsjXR5-DT23k12jM7OJn4WjCk6tMbxM-YbFXC2ultd8UDuRqyNHdW3d65Xk1C9EGzqVq_HfEMcuQ3OvaVjGHbhBg1kKIxmxZdoKEC1v2gLKLS1adY7w7NjPrldpUJ5c8YwgLJrHKhDVepQuAKRTGhLyoa1-y-TxIxs6oBWqq5yMQsRvLB_M_sYhZOL94gJ6QMViORD6Y4OkFc_HaV8Z_P3t-HCQUfQZu4AeuI2xzkDj_EQ_-WE_6VMqAtP7QB0d6rJZXUGYio14yKXMgO2vjsrSmhE8eZKBaJqGuCZlioWyRuupPvi09l0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76823" target="_blank">📅 05:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DzhdO7c85aSTDMZW3rcSJbcUrLrJRCf9q4AhGTLXDJp6Rak6lWmjquamXQBY-h9zNllDjfODdgmmVngatJt2Y7Bg1Mug5QbbU9d1phGAZQYPOMePFRacuRwkzjBKzJr1qtVv2cZxW5UXQnhFmNG0SIE-YJXW6gBFuxGrel8ATwD4DxQ6eEEiJHvOKukzvDx41DcsUy3ryIQgmNRhgCZufxJUrR-TsIjuoU0wvt7L6-Bpe34IT-kcW0pzRwuy_2kkhUf5kmtX0nx48kKCecYWLxRZyJaFbCSEh0T4waJetfXLWqDlIEJ6J-NY8mk0zsEEWqlrtCN4EnhbQQl9a8s1Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ea6wutDnjFlLaebFv1FIdc9CcUcp7UCQD3qxsNoez-PN2igNx_63QX5X9A-w9Vjz5ptVkgEmWEIFRHuetUega0U5Yrxvakf00ju8iGtvRkXQUOJnvw1Ka6LU0dsnAZ3tWKWOG5QCzx-oUqJ9p2qLcy2eLCp-Nr12GY1IAOi-PkwNvcn1jHoISTWEA9h6j8PM0-8cwPKIjOI7Bjgei642VDhAICUeRBjCqqTR-rYHKoGpG1YeAFh4Nx7M62Ph0o_bzWdqiLS9pnBYeRMghw4H8XffMXv-pObPXJAwRrNGbdYkDd5BJIanY7aWEczNFauItMg1SdRXw8Eo39_Py1XG1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76813" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/noXQVIMWO7ENQ8pD4PqBB-lmftvyoZzDe6f6NsKTxsvjmGCbbVR4MYkxiSkynGNUXZ1gfXv641-P82lzfP1x5lW5HLCIhzNBCPFylGKdLiHD1WKv0dz6qCHvFJuHZe8xu7ZlDwXYud3f8fDSaSV0LNjtXf_VmJ2Z4TRTnTgMrcFVhJfADPIKeIMhb60aNQwFolg-_L9qjKIPWizl99Ies19i0w9sGRjk2LO-KpNg-Ylyfnk3O5LxgLSsfiZ27dCZVR8Ez4Hvt3aAh5WCHxuYIHI1aqmZy7h0nqO25M5QqTU2UQoPAn1Wcs7lssVrriySWareKTWEl1UpT4qAlZL6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت اهداف حملات شامل سامانه‌های پدافند هوایی، سامانه‌های پایش ساحلی، موشک‌های زمین‌به‌هوا، پایگاه‌های موشک‌های کروز ضدکشتی، محل‌های پرتاب پهپاد و تأسیسات بندری ایران بوده است.
به گفته این مقام، حملات امشب از نظر گستره و قدرت، چهار تا پنج برابر بزرگ‌تر از حملات مشابه آمریکا در هرمز، ۱۰ روز پیش، بوده است.
رسانه‌های دولتی ایران نیز گزارش دادند که صدای چند انفجار در شهرهای بندری بندرعباس و سیریک و همچنین در جزیره قشم شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76812" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S61C0IsIV3-L6KCzCanJq2i4GTTBicfTA3gevRrSOR-a3TPAu7GgQZHL5oeMbS_C9ja0YvEU4R1YXof2ns7T6jcF90NPjC0cCyJe1J4CgPyvd776kLhqF2Lzxg69XZAamm2WMOECHnTetlJ7RlPLvBFNN56zcTocAGXdIeN1EnDE2JVMNMfnjkzfU-Y4UYhVlv86UyCGJM8S-LTIo06PoZxdiNL72jhJ97zHEuw65D5w5J4xMiMO4V8JITtez8DNTZdFmZVYiA8VGknQW9S773-YrhbUq28jcG8scKLf9npoB8zD-nGQkohQVUJqzwtg4eAZmH3KXSkbnukZtFJnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی، در بیانیه‌ای، این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر امریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، شایسته مجوز موقتی که صادر کرده بودیم نیستند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FeOXBi9DkggSTa4Wm6nTBOpRm8pvnRxyp-M_tixYX6tFJD4kcSJkohh_FWjSK2SIrSZbhAvJDOFDPIcMLnw5_CEIPJQR67H6zYoWUIk9ta_kLSZ0q1U245NINdzOdwWWTqdhNGQk10re1DnCEyoQWySWsHFkTHP3kaEddZstggTdONFnmLJA_l_IbW3JsTgWqmNpjeFpkAyBReYP28UERODU-fA5eRaTsR7QuKy3jgDiN8c2NmYTINyFzy7tp_7sQ1mU7UBkmaWtKJfDZ5drNjyvOmwHkGZLzgs33vt1-jTns53ySeJQf2AL2YmZaEwH9jBbgJVXw696FkDgTgjClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j_MwMp-KTnDhDPhCABggT_3XMvwDcN4m-WAglhuMdlLG3B2ASU-XOonlBrZxav-NgGUZhpGGIi2w-1XSNrxGpMSXdIS6-1Ol91l0jBesrf4I_rOXcahhkYWFM2NTQYApXxbDaSvn6yUIa7Yy6AIuAQCS9u4JUt3c9GK1-qtZ-Wjuu4A8vr8kKwkAuUbNuW8QbjBe4gmxnlr4q8M2ZUNzpUZsDE37vDYG2ct0imrJQ7qMy2wuQTD5LZmg7ZImuLvWVPrXBu8fVNUUsZBpH3sLOxRE8lIWZlvwoHlaka5upeXld-q6gPLC1roQEwXAikX-HwOCXOwdVzajMlRhvm5Lpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kP5U5qMRKFz5ZurEp7jINgFRGQpLxkji9Q3RsIgOBh8-yAAojdDqwH5Sxa46_HNInSv0jvDeNj-dew-qmghqZJfqgzdPDOM4T6AHXSaCD0tVIvdzLz5DikezjzBPYlWYGPrMD1DzV8rqshZ0BTRu4ap4mRNoesJhT7xavz4Dbzho9R35AY4l8qXDLfRaZtGdFxM1EcFxdTmCenis3c9dpH5yQsNfyZztCd1nb017Yr9P23LOgaDeV_r_mWDuDG06yDMubrR4cmVau4N4Yi73d1MJ98liind4GR_DiYgbZ9c0QTO9Hur3459TRcfC1WuyEQjRueAfP-E7lX-kjsX15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGvxTJB9QkTwdSnnLRCFsfpKdNauYVd65ua-YZdKnaiHWhtapzRUAhk5-hLzlGk-N8HCsdKMHTJATd8gxmH4pEMmPtrppq58GZUfkV1yC2McGln1WPphwAv0WezBK859IXgTUKFdy7_Tbmt51H4m7vrzX7Qx2h4yqszePG00zg9662i-ylyhOU8VbwZ49m6SnpZ3hApIyev9gSQqW7FjpqF53FbIs1P94i83jaO2ij26i3f9on925tFBpYX0BxK9JXf8zcFzGwaOkrLN2EGlmUP_TxpMkET_04FSquswmXd9JS2DRlL66tr0XUWAPc4Vjuy4ybd3QqQ0u60W5lTRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmVc70jSOYML6Yf5DA9dTFQPiQy_K4CvMCbMS0cxrssL40iBiJtmk43V76FIENDrhIE2pcJ6Xd43y40QPtzuOQMO_gFhsd9wV4_Xk1M_UbbA4ANBorU0-43CuCowgV4HIdgX-UyauP-WrBz7-DjkMwPdECrN99DEyY_CbInS65N9QEIlWVTyaZKmXRm1SWHCtJfy2yaKt3EVwm0rc2EO88Y_EUh6Ol6uGB1kDEwXJQKR8GM_VRAENlpUAFb9X6WpFMAz-rAoKszUg19LAbHeVOw7t0xeiq2TB1yt__8-0Dq7dCFTGGRE9TYRf29nSWcowPAVz-6VxEqzl6L4waTJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCa8D2P9hGYHYsZqjYCYHE_5AVgTZ27kBmjf7P-_g3ijMG7WRuP0Zm3q7dvAbrup7-d9YYRPnyuOCQdO7XivTGZwoknG3lLW2Xe8RqGbvBqyOfrGoVnbS-9nw9hxUJ_nAzEO0nhuauQ7X0B0pX19xS_WUR-6SOwb0weXyk6DIx9w6WSpqdth3TPKMWcXf9MgYZ10E-0fqVvwHPAUf45hBBtn_e8zpipu4onW65Niyhbfq1Yl_3f-PqzEgvCN_bHd0mPie-6JPWxFcqSpJxwReZ0-GZN3PJuPj8xq9gUO5CELC6gRChnHuNf2H0d3hMhhx6f7LoQ9me1NEar8N4EFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrRBMrBly0per4lZ95hII7yvRElAH_icH1BCzDJiCRodaoSnThb_95ehbwWPQIP2e24SWNJ0Oxin-spbshM8omvf4CMSnl1K1SMBzEpal3jIMXGeho3lu5gx6CfeZ_TL67eXe5BYeVWJ8kCRp9V1-5BTKmXBrLH1HnjnrZvTXD8j9O9di9qbKVbg7QuXPhrDjapL4v7IfHuiruZZIpKkbEcdmeNZnqzTDB2vOf3e3yaRzba7m36VrXy1EBqwND01Z4KgLzpJXRKXYhfjlCUFyKat72VN-sgPzFAzuvyDysVA0iON3mM7Oc1dG8EIXATHKr1XBxZa-evi4oGc6FAF1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Ykr6ngb0_aUYWUNHjC-LDAlNDJVfk62Orxspnv4Rf5jBc2bGiZ-hPWl42uN-1CJ1m4PgxCkYN6BAlaGWs4PdtgOOkCswL9_Su6snmJT1hBpSt-qGnrdIeN4u7WSRcY4_99GnAZt2yonFkF_xset_PpqR4P1cL9tMuCAMTrIwqskWcrRPOscpo5dAoR1RXplFEOLJlo2XkHyWMFGY3YyCY4P0Kt9XOVPUK26vaCVWjT5hWX-nGX5Q18QyoAF-O3Llsh0Lk6qFObp_6Mpq_rYX2bWSSkz-XzDwfv478BY87MstUrbLNGi7kuRStIx_Be_MRNfnaw6NRTiGsnyWg4-s_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=Ykr6ngb0_aUYWUNHjC-LDAlNDJVfk62Orxspnv4Rf5jBc2bGiZ-hPWl42uN-1CJ1m4PgxCkYN6BAlaGWs4PdtgOOkCswL9_Su6snmJT1hBpSt-qGnrdIeN4u7WSRcY4_99GnAZt2yonFkF_xset_PpqR4P1cL9tMuCAMTrIwqskWcrRPOscpo5dAoR1RXplFEOLJlo2XkHyWMFGY3YyCY4P0Kt9XOVPUK26vaCVWjT5hWX-nGX5Q18QyoAF-O3Llsh0Lk6qFObp_6Mpq_rYX2bWSSkz-XzDwfv478BY87MstUrbLNGi7kuRStIx_Be_MRNfnaw6NRTiGsnyWg4-s_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهوری ترکیه روز سه‌شنبه ۱۶ تیر، در نشست خبری مشترک با دونالد ترامپ، رئیس‌جمهوری آمریکا به مذاکرات جاری میان تهران و واشنگتن اشاره کرد و گفت که او و دولتش در تلاش‌اند که روابط آمریکا و ایران را به سطحی باثبات برسانند.
اردوغان در این نشست که در حاشیه اجلاس سران ناتو برگزار شد، تاکید کرد که این تلاش‌ها در راستای برقراری صلح جهانی خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76801" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekS9iPJ0krJl0vGG1PrUX7wROyok1rOLH7kjMHqAhg7h4ZxGSn2_HXnGfDiCTnaXQSnHaqlGpVpDuOOJexh6L5cp39qayNzbV5ZPfE8-NYhZxnalmnsabfZhRqQpcyCRDTEnzWKPX_lKh2lrk7OQ98V3ijMqTH2PoYwy-DHX8rs1TaFYXb0te4r4QPb8G6R-mIRMwRdLzW97JMxN6qCwy3wPv67_2pB67W06107kog8VpDgcqjGuyiwDCB0PJiJWwdohJEyo0to3e7M1fG_DoFiSGyznbEfN6Rq2OCP_T9T_vGYbeb9sq3o9a2-0P9nI67cBAfbUT8oh6tld2FZSdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76800" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=fSpTWIhR4jMFiT-0VHIlzOWT3cnd0UTcbg5l0mW2IqdgPxHHvd4dMI9IAoTl8afYpwJ3i7fyniKMtB3AEZqb05S4QgxZ3XrwetgeTIkoKCHeDN6n2jhgKsceuxcSh07zVH_WBob9J1ZWOqkSYDjRwI7sSGo3CqdChrBpjlqIaH43Vo6NAdgUIBFtDNN6P_F50eHC5e3z9eBNm-z5jZL8AO3QxjG48GLAN1wKBL_eo1vyAx5zxACRNb6e4Zo4w28euly6S42WMX6UqlL7QCrVp3u2bS6-n38uEa4KsqWD59N6P067iH5HAUw04NQKeg6ka57U8GtrImCNAVIEbkzDXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=fSpTWIhR4jMFiT-0VHIlzOWT3cnd0UTcbg5l0mW2IqdgPxHHvd4dMI9IAoTl8afYpwJ3i7fyniKMtB3AEZqb05S4QgxZ3XrwetgeTIkoKCHeDN6n2jhgKsceuxcSh07zVH_WBob9J1ZWOqkSYDjRwI7sSGo3CqdChrBpjlqIaH43Vo6NAdgUIBFtDNN6P_F50eHC5e3z9eBNm-z5jZL8AO3QxjG48GLAN1wKBL_eo1vyAx5zxACRNb6e4Zo4w28euly6S42WMX6UqlL7QCrVp3u2bS6-n38uEa4KsqWD59N6P067iH5HAUw04NQKeg6ka57U8GtrImCNAVIEbkzDXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری که در شبکه‌های اجتماعی منتشر شده گروهی از شرکت‌کنندگان در مراسم تشییع جنازۀ علی خامنه‌ای را نشان می‌دهد که به عباس عراقچی ، وزیر خارجۀ جمهوری اسلامی ایران، حمله کرده و او را «بی‌شرف» خطاب می‌کنند.
گروهی از هواداران نظام جمهوری اسلامی که با مذاکره و توافق با آمریکا مخالف هستند، اعضای تیم مذاکره‌کننده را به «سازشکاری» متهم می‌کنند. روز گذشته نیز تصاویری مشابه از حمله به مسعود پزشکیان در حاشیۀ تشییع جنازۀ علی خامنه‌ای منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76799" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76798" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQJmDuj3rnxmFAuFtFx4UY-WJo4v358HVNCpvBGl6w-4g0AF-EuHObCBclnbqe1OuFXiJV2tP9lHnYrQ2LGHOLL--SQ0tEokcEadZWHknlTfnBt2YdKYjYVO7FrU9fKhLO6hUOZAPbvw-HDIJOO_eIRMfTht1r5Ll5vF-80L9GNlmZNvndzzdUsFegKdZy7mQr2_ncKsVBSHGlOz1UiY7CPGBkzlV77Q_8KU5QM7ufoyRlG6VwjYcBgidoTnkQVifsZ7fsFTV1N-IXNGTFXwu00UG1gWzswmKG2zxcssCoqXTPgqw5W5FBhAGC2wRL_Oj-ZoNWVP9XzAgMIn5XnefQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76797" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyqwpU4Ah72cpGDufG_Cl6r6PWuZ2He5So8K4SWZYttVyqO7oQRS6-_SmgzGhWMcBmJwx4yFYkSbkJl5Av6FmHO7sFJAwzaNVX8rXm18UMBrNDer-UDtTzbMns8eaem0TCGGRX6Mm9EB_Oh6X_DUU32sSzfgd9VcUc1r1rLGIm3RpeHu2GXeluHNlvEgrt0ayzyf5-JNPttKxfbcNIarKRl1QO0PZKTyyllLyef5Y-T--yI70ydu48rSgeILMN4uBTVZ3ZKm28mvd07IVLpgMtqtzZGIZbSEqkYQuCarS-P3rMLsSrJGdu5AMOEtkUMBww4wXAvp6EWlyO23ifue-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، بامداد سه‌شنبه ۱۶ تیرماه، اعلام کرد یک نفتکش در حدود ۱۵ کیلومتری شرق لیما (Limah) در سواحل عمان، هنگام حرکت به سمت جنوب، از سمت چپ بدنه هدف یک پرتابه ناشناس قرار گرفت.
به گفته این سازمان، این حادثه باعث آتش‌سوزی در نفتکش شد، اما تاکنون هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد مقام‌های مسئول در حال بررسی این حادثه هستند و به همه شناورها توصیه کرد هنگام عبور از این منطقه با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به این سازمان گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76796" target="_blank">📅 03:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=dDwv77k1iTGY9nPJ2WhtsoRJdxJQxTdL3U7i6yMzPMhmhk2XYrWL6c8kWt7QwpLhHWuHNFKWS_p_X5kcgiQrOMxWLyT95IINfsdWiAKFlh7hrjUjKkUOxN_9u59TcHU1XGrJSms2dMNkARHQXEH4GbrNhCRHDnbJNsUXL1ojwDwrhSDtecX1URkiyiH_74Prlbpbpmqd3ssAlEoTMPaBpuInG8xKfvhjig7-zuG_IMi1s9leJMnjRWXcq7k54jhtu17ydPTBotZBkfG2PgZ9sUU73IIx9-U9nOdilE0ic4S6EgEBbCeu43Z2NcoJfEhF7KayH0z8FaqFh9HEGTGN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=dDwv77k1iTGY9nPJ2WhtsoRJdxJQxTdL3U7i6yMzPMhmhk2XYrWL6c8kWt7QwpLhHWuHNFKWS_p_X5kcgiQrOMxWLyT95IINfsdWiAKFlh7hrjUjKkUOxN_9u59TcHU1XGrJSms2dMNkARHQXEH4GbrNhCRHDnbJNsUXL1ojwDwrhSDtecX1URkiyiH_74Prlbpbpmqd3ssAlEoTMPaBpuInG8xKfvhjig7-zuG_IMi1s9leJMnjRWXcq7k54jhtu17ydPTBotZBkfG2PgZ9sUU73IIx9-U9nOdilE0ic4S6EgEBbCeu43Z2NcoJfEhF7KayH0z8FaqFh9HEGTGN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=Yp0O_LMsDTInJo0zD8PNtQn7OJwvsG_lJPNFl2axy8PCNqJI6pzaWim3pYvQ2ObFwqtqqLlrR7sDrejeon6E9PQwXIvlewxhlTPqmAIc_UjqYKUldQuM0F9p4h38SOEJ30goHmfrc20fNoQ2DRlhdUFhhpgunBfk3uLXgR1CP1ErgX1SlGLoIAf8B6pFroJYUDm0pn8V987bwHo8L0v4OTrdab2E156LYI3eFzAL_VmmM3CvtE_B2eliATTSF5FjWx0yba1RnMJ-fiUF3-_ZkKUUsSMMfFxQ6G69zihYl-8txRUq6ClRc_l3kcEW1R593Fz9ywTChb3yLix_v1LVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=Yp0O_LMsDTInJo0zD8PNtQn7OJwvsG_lJPNFl2axy8PCNqJI6pzaWim3pYvQ2ObFwqtqqLlrR7sDrejeon6E9PQwXIvlewxhlTPqmAIc_UjqYKUldQuM0F9p4h38SOEJ30goHmfrc20fNoQ2DRlhdUFhhpgunBfk3uLXgR1CP1ErgX1SlGLoIAf8B6pFroJYUDm0pn8V987bwHo8L0v4OTrdab2E156LYI3eFzAL_VmmM3CvtE_B2eliATTSF5FjWx0yba1RnMJ-fiUF3-_ZkKUUsSMMfFxQ6G69zihYl-8txRUq6ClRc_l3kcEW1R593Fz9ywTChb3yLix_v1LVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tu4dADYGQsFWpIwo3WS1-FRJQ5Nq_t1favLhtGHTl_ZRZ4MKPnIs1hN4X8rUSSnpFFG9cykCesWOs1QVwsLCUb1gRYvje_7t2oHg8TIOAHJmqW2I3bMFo7ynmJxkiqDsBXNaaEkyPDZcl6dpoUg5vZbmonvwaGv7GzyHVfl_qVqB6VC5xmhF2kKamu_C9XK1oFWr0mpxGt8RP6a6ryQ9Wqtg0CdAaInPCTQiycT7-a7jAa_h0mb3qc-7AvDEeEFjpy_PlzLbek6DMLiOL9vI07CcY6d1Gay1rYcF6MNTeXItDZd3chrDCmHWcolweWihZNBR5YpVrd2yEAA-uaNqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=If024OB54dLTRcJpzvgCoW3eKsJKt34zgVZ8NbDr0vKQc4teyYwika2uzmRh5JIC-FlSpKVrHizQyEjbgtLEx6uAqQVG5fxVoQL9C7jfFTxmRcJ95tyLSKezBZr-rJ1qidIr65HI2JHOEVOX7gXr8mU6t-B_Im9KdF74sJKcCqO9I3KoU7072hTBFJ_Z_ew8FenBbqdbNcUYyC5cbIuBFe-Z-NlMAAFRUDCCRnNWtWmKFOp-BGoFqZYpKpSgL3RvEFGkLmnmG4Wy0dBaWxLw8RhCVEotAW3t4dfJnBRDbFxLanqi3a8YA-ZbXX4QrV7IaWu0r2JjblJK-5_XUTgyng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=If024OB54dLTRcJpzvgCoW3eKsJKt34zgVZ8NbDr0vKQc4teyYwika2uzmRh5JIC-FlSpKVrHizQyEjbgtLEx6uAqQVG5fxVoQL9C7jfFTxmRcJ95tyLSKezBZr-rJ1qidIr65HI2JHOEVOX7gXr8mU6t-B_Im9KdF74sJKcCqO9I3KoU7072hTBFJ_Z_ew8FenBbqdbNcUYyC5cbIuBFe-Z-NlMAAFRUDCCRnNWtWmKFOp-BGoFqZYpKpSgL3RvEFGkLmnmG4Wy0dBaWxLw8RhCVEotAW3t4dfJnBRDbFxLanqi3a8YA-ZbXX4QrV7IaWu0r2JjblJK-5_XUTgyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uyzpko8j-99AbMGovsxXF-WRvC00LJ9JwKkE8PBiF2CPUz8P8DYYfJBmWtdSnxwexG52O8PMqWLHwig2RjPdbkDgcqLulVyrDWXysMff1uKPNYqblLT6s1vpcB0j4m0TsTfqa9wzL3Q3lHNDfh9P8BSn9IVA8n9w5Cszz575iSlyJE9xNpaeDtIWmD5HAObCZ9HCZD_RCNXh9HHLM4bo13h1GN7NRIVSpdZ2YDWbi1hhVSwy_0b9T-U6Atu2Y8ZaNjFI4QylcFT1IY59-YZ_vzcWCKCIWC5ts3KPH7EXSHJ09GFg5QkFvfk7g3s7NMyDvFfGLbQDpvKMEQkqjrmu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RY6MqxX-8e-7oyCLiHdfbApwxS698CFAzYKwQpUyYF4GoyABBLq--ryaDjYnQ8XMsCoLirn0FS40VBAjZOygvGeAa1zfEov1Me7jT1el-R4_SIunY6EMpVFLCU8qE6NEp7Bts9QKWqhfGD2-k_YKGMH2_vrwYXIgTcL9eHTggpyKyFiAhq5sdbPboxkN8t8K2AmK40F9jIm64j-4bvQTOvDy6w7r7xYw1XgQPaWZ3K6jBJ-MGZbGE7tibNlQwVIq9HkHi2N7pWElOQb23qebyhEc68DZ6pI5bYKE3vjbIJVkp0_l4ScVG6Mhv1jFuhyz2kmD1bSEmgw86Q5IxvxHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mg6x0yRr4SJlupnAQs7j7M5hUuCZv7uX_BTVKiClb8ghd-AcajNeGBBEmSrLC-t6bjq5GY4pRQZx1NUYf2G_UJu5eUmKv_DMQr5LdTfmsHPOznpS_iIrF0mOoHhHeRN1VJEM8MUpicY4Ld--HpdrEF1IjH2UY9lyhZ7B5Cef_1HW_9qxlGz2AOoPLYkjs9rIjpPNoMiE02vdDSKIgOfrknCHQJjhyYjF0IdJZoqUM3sOxJ6qOHDDfEknyDdRxt3RWDybeHYs4VYgSZetxeCgrO3RHusTjVIMLt3nj_6UOy8X-cefsfqtuW7WHbBQlSGkkqHKZmjSRURAvlMZKVbUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=Bh4TcNiVJDy0JN2hIsRRU5CnmGd2HnRXlVogPVl_pIQpoJa7U-MsOaS0BtlYe3CNdKirNfLhaACTJxmK71zTBo1P_HOB5xQbKFUAwAN0KM39n4GoDDW_D1BLH-Exascanda9_fH5HMepA4Iqp6MrscBec8u_eCmsg5F4rlmFthVacjQCOzCZmGcEhddj0BEvYmyjJ4naAu-BkF9qmIN5ukfYTl7ks2eI02Yq-pICTG5pdK97IFP5Q9X_Hqp-lkoFQwusW7fJmbVkDgOk0ht6o16bqQLdT9F5ugmIm0BDD5YY6eDkOIRaB0IHUu60tRFOu99OPGK6tDI5jfLHzvw3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=Bh4TcNiVJDy0JN2hIsRRU5CnmGd2HnRXlVogPVl_pIQpoJa7U-MsOaS0BtlYe3CNdKirNfLhaACTJxmK71zTBo1P_HOB5xQbKFUAwAN0KM39n4GoDDW_D1BLH-Exascanda9_fH5HMepA4Iqp6MrscBec8u_eCmsg5F4rlmFthVacjQCOzCZmGcEhddj0BEvYmyjJ4naAu-BkF9qmIN5ukfYTl7ks2eI02Yq-pICTG5pdK97IFP5Q9X_Hqp-lkoFQwusW7fJmbVkDgOk0ht6o16bqQLdT9F5ugmIm0BDD5YY6eDkOIRaB0IHUu60tRFOu99OPGK6tDI5jfLHzvw3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX0JrE52_3-MxWk9XtIFNZBqpZb4JJXqDFPwa91uDxRe4qIEgJUXoWXXq4AUFobecvb4DS8qq6ZMEnHgZa6HFmar_QwoEr7FswuqXhAZK5RfSV-lnCHVJXIzbyzHavBrVmO0Duk2LWqGAaRuZiXNeFCAIc3Po0p32cTDhP3uLUgIrLeyXxCNxKDKCLhDN0N5rvmDfBIfyGNtu2NeQQpyX8HB2ELWbYKlntOe8ur3I8SvZ7A1Iqp5cI25sjUt724yUdAI0YNfUzLpxPfAUFz1iFd7UE__7TAVWkl7Rq-mRPxP2pV2zyTnMQ-YAsxkb_TDwMPQfs5WjgxzqTzgCZOpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=eEtnJHhDW5W4SB4pH14nEkNTU2wi35a2ZHvjM2TVaryNLCqM2reMwCB9ShF4884fpJxCLlOJ3JGPlt2IGS4LF_nKDDAj-93sTCG7veBxbhmwRfob0BnZWgRY2sfvhihpDzRcmPuX1g-8xYroEE7KcYWzPOg9kJhtqLu8duxEK7pZZX9zsSD1JLqfDrKkf4dUA1WODYUGHE95kWaQJINr4OgeF4XYxn_PlkGEhBbFeUpXgBS3Ce6ScBz6WH-2502r1qRYlfJ1v7fjZnNIHx_95-QH8lywxWobrgyed_TNjUmwywcuOhjMgz-0C1dUtNh7ww4lu9GpRMX2V1QZFLRLXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=eEtnJHhDW5W4SB4pH14nEkNTU2wi35a2ZHvjM2TVaryNLCqM2reMwCB9ShF4884fpJxCLlOJ3JGPlt2IGS4LF_nKDDAj-93sTCG7veBxbhmwRfob0BnZWgRY2sfvhihpDzRcmPuX1g-8xYroEE7KcYWzPOg9kJhtqLu8duxEK7pZZX9zsSD1JLqfDrKkf4dUA1WODYUGHE95kWaQJINr4OgeF4XYxn_PlkGEhBbFeUpXgBS3Ce6ScBz6WH-2502r1qRYlfJ1v7fjZnNIHx_95-QH8lywxWobrgyed_TNjUmwywcuOhjMgz-0C1dUtNh7ww4lu9GpRMX2V1QZFLRLXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjdhWyHIZ1dYBiZFOfZpf_Mj14ODRlsAF0CTNlUZPSf7-N3I8FWNbEvkp40xZXTbFMSY28nlb4yKBWj0bqdLt79KjHnFqp2WEAoNG4Fd2MqbVhHbcIKXyskR7fPK_ie3A-o6FIAiYtYhJFvzwqbAldIN5y99HUtzqxonhqbhqhScSuTFBQ2tjrt7NpsLtY8XsL7bZPnSwsizOkjt93UToFw5UvajL10Hs6Q2Ly2luJnotIrZiAarHoRKoPif1T4n5SVItGQDVmou_zeHzu9RriucbP4upIf169XnXgAqlrmFtmLVECv9SmMZA0dALCpYSQhesLoNIearEFa5ZzgMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoSwXNHR5rq8GMD1ViyyGs8sxnnTHFLpiecPcFHeDGZu4GL44s13euD3qj_l9BiutL58Mei6RDb2um2Jf6_qcKsQqDoZSRqUJ6rl2i76dNrJoqASQekXwJIO3xEWA8SepDOwjqq5g4Im9OV2MaAsL4NduPlTbOwGChMtSjOmGCR_FyVXvY1k8-wqJKxJVCdiwNarsf4rhBdzhWpBz2Zq2WkExrtjhvTD93xIRTk5LWw-JvIxf1jgrMYGLRgU5f39GOa2TwUEaWhkYIk4GROAuQ2P8UdfSKinVdurReQDaIqvQKnO-RnxDhn3BGhTlmfheOSiaysjM1bDtVEMUXDxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etHCqefh2BmIwIYPHsBrTC5l3ESSVY2oJrnMj6KyHJTtDO4hu1UA6Yx6S9TgkGxDdSWUjilIjjkHRo0Zk2h1j1PXBjv451N6dR5J3TZJWua2SInWKn3lynsbNBfgKRkbOhqJJXxgNJ8zLsTKX9PhyAQxG4Ly7UuLomHAphlQfhFBKR_HYEieOM-Vh-DKe2ZXLZ5DqOgd3cwOGG_xj33NP66eKtLtUa2JoSJ2W-w29JqTmf0hzQxsDWcuJ8TbIsRZ8MOiVvku5EvFgg5ptEJrtlL_9dS_a02Xln37ZBn8sB8KI-6fCYJz6xNDD5zRKYKbN-Bx1xG-nFQJrJK3YYbN6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DfVIifFKgTmxDcMgG9rNNf-35XFRYeAVcN8ZJFxvz6ACHeHfJdDmqrT6yz5ssDJ4rPOu_IiugoiYbSFyONaJRbV_IGobDef4Ekc_SbBYc8wgWySVOYXOEa9xsiv1UJZKL2emS-PpIiFunj1o86YJzPmg6kTlj0YbzoFsxyL7bYurDXWuL686gMHNb6RLNwbe-0xLv8Gh8PKc80xlXXWdENgssb0z0c5f1qK3AD9JZ7EYGzQd-Cn5C2z9o0iAofVdt8s8l7qau6USY9JFmzaicUT4CHLbW-J8cNZkjfck_77eIsBYALJh-j1AXUzVrmedF-LroKb6sf56BOaypDubkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/htq8YzP9rOvOxqJNvytDCTQsMISh6leo4Uw7oX3Bqll5E_YMlG2u7siT6pXLLvMgQ0UKLVFE8ozxRZZ1s_lhCkkMw9RuZ8Orihsd13GDe3Hj8MVmT7RkvPeUY6ioeLiH7zcEN87FRGdgil4-4stefeEc-ETpUQLdgxU_MHMXueUCBmqt5KKRo4uvpimTzeC0oKCEURwpWnE5ZveTQdgqIF6z5TDlsWJU3WXfVMg920TpFWCrWsjgO0mpS-zxZYSQfO8zvmbL1jQmZShSCQvPy6rFMERlZVDyDZO_OWzu9YjdVAz4-1st7zuyh6QB5a7rox2Xsce_G0yjvp1TNb1aKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=K-CNHg6DxkbNbo6O01RBdfBhIyBKrnnqnLvhLMRAWR9XTFHaIWnXSY4H765gZGnfZjYBSmlNPjYRaXAC_4Z1Rk7hIy8IPvsdxhizxeMjPnW5ma7g-KE60pqgnsQlaNsr05KGvtoSJgJIrffCnWRd9xP9pxGMqTpOnYc9ujNwEygzzLfX7owp-zl8QZdwzMeNdRKpmYh_yB-G3lkg7OKYPUYDVIlt_KHT3YFvtJtHntAZsX1MMEF8P3MrgMEwk1EyClJMww8t9U8p66aCCqZEJzW5A-Iudbmpmq3clBtERrCHWlKOV7c_dy5sMKjkCQJaidMsZ1hAqqS54JzKjtKMGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=K-CNHg6DxkbNbo6O01RBdfBhIyBKrnnqnLvhLMRAWR9XTFHaIWnXSY4H765gZGnfZjYBSmlNPjYRaXAC_4Z1Rk7hIy8IPvsdxhizxeMjPnW5ma7g-KE60pqgnsQlaNsr05KGvtoSJgJIrffCnWRd9xP9pxGMqTpOnYc9ujNwEygzzLfX7owp-zl8QZdwzMeNdRKpmYh_yB-G3lkg7OKYPUYDVIlt_KHT3YFvtJtHntAZsX1MMEF8P3MrgMEwk1EyClJMww8t9U8p66aCCqZEJzW5A-Iudbmpmq3clBtERrCHWlKOV7c_dy5sMKjkCQJaidMsZ1hAqqS54JzKjtKMGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=hKe2PuCLKxfpJBZJTOztPqx5bVvTPcFjYkC3XVu6BtPHFbbhtJJ25qGrJLEPA9Cstn7v-EjnthvQlg72lt610uT2zYtbpTb3wBqX7Lr1alaRgu1-IWVJsYV9YNWJ5br2wao_WmEJPS2SzzIdd9As1yNpcswinMOIb52bpUxGVm2k3QVUzt_P_8a7xTI-RO0od6Dm7h1LVYQO8z7s-Er3278_u70qhTW16y0SFq-7LUFFtE_UxbGyRApUZRAGYlQLobqg6ac90Dcsk6XebzBFJl5wUILaHVhISYjpIqJbwbB7LsWqYw0XY6jHiszFM9WtfHlq0nJmzYbEJRYLrJN8pA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=hKe2PuCLKxfpJBZJTOztPqx5bVvTPcFjYkC3XVu6BtPHFbbhtJJ25qGrJLEPA9Cstn7v-EjnthvQlg72lt610uT2zYtbpTb3wBqX7Lr1alaRgu1-IWVJsYV9YNWJ5br2wao_WmEJPS2SzzIdd9As1yNpcswinMOIb52bpUxGVm2k3QVUzt_P_8a7xTI-RO0od6Dm7h1LVYQO8z7s-Er3278_u70qhTW16y0SFq-7LUFFtE_UxbGyRApUZRAGYlQLobqg6ac90Dcsk6XebzBFJl5wUILaHVhISYjpIqJbwbB7LsWqYw0XY6jHiszFM9WtfHlq0nJmzYbEJRYLrJN8pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 503K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSdXziK-kgHhqd7H9nY92zYt-9TyKmU9UXntLlCSCLmIToOSt0j32TRg5hmKFNPIESc4wTRWiI2CUdXQtl0mYLjU9sYcAuMveukZxhIDI9Zbjml9HWEingVM27_AaQuFUpbFN2ulWYY9QQfoOKYfZ81a31vk5Tk6t1z4VBPrGMRHozE13l6wYINKuM154EIsadxIb81EByuQBmoQ2__Ro0oXiyPENeVlqbUks41QQn1HMtiPCB75As8XBgIrNSkPcsfMtgfWDiCzzTeoen3u4f2gf5IdM3KFlq4fz_RLf3OTkdKiD0gGiC9FJqVjobYmeBHVAwbW7ZtuBWp16Evc6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Q6fOtli3XijB3_kTsu9QX3IRnG9WKC3-od1E6-M-O9ofteoDJzVMvk9643IoKAe8VVB1oiztnDOWLs80IEYgUTqDjOS-kW7GEqdaa_XXno-t5duNsWvCqb2XsYVzJIRo2f-9q9I_kbtX81y5vDS9pvqdI-Ogw9C_6AHawlxrODTL8bgL9IqoSbeUtT2UT46e82L_59AUxACO-CC7EZbZ0cSQBfD49fJghLfTJoxeM94d077kvNSYs7eNACk5oXMRVengw5l2Fe6E9j5RkH0AdoKfnNKWlBh1WFzrfhYmjuUQyj6wP8ydeS4I7DaeHNF5zwqK7BTow57AIHZrDXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 437K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NaDh_5ShumakLAh2cm6vsH_nNJQ6qi4njXFpeGiXN6PSZay9kNLVSU0ygpdzxxnoOl2a5TUrshr_yzksPLBhyx_x7zocxZHl8W09Gcfc-js9zE3v4xgLlbzTXpJdeyhfF6kk0Wa0PGBSwOlj5Y0J1m1gOSILABjtkzGLLV9gIg-qCDXvpftMQDQMDwZxhbt6CF3HOj4tyjZHjky84w_xaZjieFFSMFvcpkQNziNpUFT-T9CzXzQdwisbaysM4FpeEpeRZoWs9VAzSo7MbFk3v94AZlXg0evKS4-Iqx5Q-8D_gC13mFwJxuCALDpcUKDuFT911IvvdxLe3F3SegOZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IBPAT48evwHf90a33V5z7dnJST3m93rbEaTmvTWoUSWj5xDDrieMz8pb3cr3d3ctDiV5986Nnghds9_7W3FPTpIKAGRXesqrdmPBVZj1qHx8FJ3_OUHMydgzkQpE6k-7Sj8IL3Vl3uUzESh0vZxgKTXQ7y-nB0Zmmks96JmcGFDgBXlq5Y2jlCyzvOYbvLexBnxCwNf_2un68xMTsaBitMjj7UtKSvV05nBM7adkMyTgoozf6qY4N7kd15GoW6vHOFSUP4gi94-PqKzX17UkxTlchOaEVdqW2rB3F99QnfCIRCxp93G0UO-XgyuGtEGXnq4fiJdyQFTZk5g_RhBtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u3nfih3YkL5QZN7Mf3E22jXYSSi3iFNY5RdKzy3NCSsIR7J8TKIIYef1hkZ1F74s1qDL66QBoKTRwdGVbBYnIJsJlZDyNDXKg_pwYZ7qj11GZshiM9Sjw6Y4-HdrFUsUUx3x3Jq3WCsbw29tiVhyUEpKbPgyRH7QG2EVGC8B6twkXXtm_XCc2JrmS0L_E06P_-ZB0n0-33PjcYvCqrjxkHM0vrUEjHJoe_JNFOn854fKNm_s1H5-PzrN1lYYi4qRJmCasPYrDh6Y6DqJC67eLa7BNscBj_FJn-O29wLlhaDREoa2V44GDr-qDNLeDd2fFhaRc0uLS6B9sN4Pw6W5UA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=fR1MXVd0RvrCgR5v0rCBiG1gzf4Shcb8W2FjBW6wQ9TyR2u8TjvaOKNT211AShgTWICxbNic1_860sjfR8C71wPq8d5HLDUUxp-X11kjzG1OFhVfktV9T7s6daSahbZYBgLiA7In5stfBAi6xlGJvUcRvAKrWEvFNBKi8DBJxvFAtGG-Dw6uPNkEPZaUoF7RJBz-O98PmjgI7f_WPJnwTUZBwa3FtQRg_X3SwtUjKhRbtjDRAwSmgeYa_MHEQmZM1GVLapCYkVjGeV7DIzuUZZj4QKRABpgm5eumOEfVxP8rtecTyTJh7b3UyX97Lv1QlcZeB7v0kkF0O_pOB3d8Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=fR1MXVd0RvrCgR5v0rCBiG1gzf4Shcb8W2FjBW6wQ9TyR2u8TjvaOKNT211AShgTWICxbNic1_860sjfR8C71wPq8d5HLDUUxp-X11kjzG1OFhVfktV9T7s6daSahbZYBgLiA7In5stfBAi6xlGJvUcRvAKrWEvFNBKi8DBJxvFAtGG-Dw6uPNkEPZaUoF7RJBz-O98PmjgI7f_WPJnwTUZBwa3FtQRg_X3SwtUjKhRbtjDRAwSmgeYa_MHEQmZM1GVLapCYkVjGeV7DIzuUZZj4QKRABpgm5eumOEfVxP8rtecTyTJh7b3UyX97Lv1QlcZeB7v0kkF0O_pOB3d8Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gluyEkfIwPCiN5AXg1czHoi015xAogQZSLQ5HG8AQrW67tzVYbbhhmiQOeD-DdQRaj0F6CWO5GXcXrP1xSxH82A7iVZy1BrE67ja-dqEa5m7Btw9UlVUcDNVhtcGd-HseQAOJdV7weU6TD5TbMX4JIlsy0BW9XzTVF0pjntppusqXt7PUYCvngdmjZ8V9jAyNloCjfMqwGZsvFoR9AhgotbGcqBGChwB6fbammmKpHU-uI2oQEX0juyK_NZN39_ZIwwFU00eWn6egVGOECjGEp3KqdaruyIWWrfvTRvJ_-YpIOq38_UvLE3K0fMUe0_rKKzNDOtU4xpPelkvoCWgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yzzuu5ABC_FyufJkLp1xfI6B-hkasjF6lJVs_bpceloqRNCXhF-NOUTgOlvrYVZhHuYjtggsWg7gbRpiT_KRL5D6g9kfz299-9scYsJIhOihSLH8-aC9Jl57nx-JKx2_c1RI7n9SfuPE-_DniqA4NIlpqUaVZ_2XsOAQpsqzNCm5xhkLTv0YtNORfGs_F-S7F9e5fiVV4wC-8vcKO6k5hH-KeBlgAQP2ldOTr0GYtThuegcbAOqqfZqUo7AstCta20nUs96P5ghOsLmZphhNJoiQ3ePaGKM567IqU-DLCqkREHlPzo90bTIu8jUwaIbQBIl-aJtOMROuXeyAxu6ooA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qo1UxQ5lN1bD_ibq79QObebJh8oulKhx7dbzAVPKo1eEIoKFzIgf719NUGo-B9Jtf3Ais4ayw1inzoluVxgCmNFJWNbEmVQNW1RfjWzTOmBZo3-TETPeGmzpRtQ54lHIIcg-oPEC3x5eRPsWeO2KrdZG3HKCFgr7rvv8JeKNIET-yTmB7M988HJ3IwaZtZ3Vup8FLLPlmMwQuY6_qTY4bKTKOh5uqXNjily9lk733jmt2gnrDXvwjlB1JZwjpNHhpVvuMEyP9xITRZBGc_70N5B3ShgRIMcH6Mv0VxzoVrPne1LJ9oZfq7bRqgzWgIyapZCZfFam_6pWDshHQlRebQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=T33jl0Hb8OJ1v9BFjtl-esl4EFLisBDnnQW-U_S3-g4pmOmjYhbXRFu4Ek8qmCjq21VivXqJGglJzj8wEN0gG0or_HhlgUR0p1IaP4y7xgjRX_8UhmvNPTWmGY9jqJKG8srO9xWlqKx0Pz3hdQujjUr6FihlSI-hOo4VTQ5wACDuz1gxb2Kla3DwvSbLRkSTm4SLXlR1oMRi-smbgDkxvK6La5NZ_7y7hTs1FrK27oUeuLyppYCIJ3-I-3nGFCTnP6ZL7e_gZVjpE0RFQi7Vc7wN_hj7_VNlwyJ7sWIIbcTBvcrS6I_beQM3-zt040kAX54BLEOdxAhvb4zYy7Hyog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=T33jl0Hb8OJ1v9BFjtl-esl4EFLisBDnnQW-U_S3-g4pmOmjYhbXRFu4Ek8qmCjq21VivXqJGglJzj8wEN0gG0or_HhlgUR0p1IaP4y7xgjRX_8UhmvNPTWmGY9jqJKG8srO9xWlqKx0Pz3hdQujjUr6FihlSI-hOo4VTQ5wACDuz1gxb2Kla3DwvSbLRkSTm4SLXlR1oMRi-smbgDkxvK6La5NZ_7y7hTs1FrK27oUeuLyppYCIJ3-I-3nGFCTnP6ZL7e_gZVjpE0RFQi7Vc7wN_hj7_VNlwyJ7sWIIbcTBvcrS6I_beQM3-zt040kAX54BLEOdxAhvb4zYy7Hyog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Oeo8XJavF8Yzq9vF_mZqAkKfMD_WSn1vA2O2EaDcy7nbYQYQ2WZyZ9WT0MB3j-Frm7uU98z3VxG2UTkwnKg-iRuolDX14YVfnONaxIMT2uZ-ZiLjgkvqZj0KIIiPn1ng054LT3JQgovOBxvPjUKtkEG6cUCd-7ZwzorJd8ky3oOM1lrbaHJLuxOs3tZbFBY54Bn-c03_qdG8aW6uac6SmjXlUYPIp-dc0d0EMOLkXPYn8NjW0WS8FW9a19rm_8Acn1pFph7KGrozIYfzpE3UAa80L1oT2vzF3POXb0FwzxADXkRqcuIk7LydzjyyneS9NHiZnAnp6TpHl5fMRJM-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hktlMob93dsJxfLGKA8GYnCX4dUtGqZzX6VAhlXlx2J3Qc4AqDwihhIx1evmNnKDOssmvGT0UHfSK334MZJ7j0VDiFGYb1a36e6ZlYfGwUA_3KS00Ea8MxJvu1aNELhhtMJhYy8-Lw6_tSjR-igwRmL94gKERez-zzNNGxqPSxrlTp5t1kFUVhFQQyzyN_a_a8w3j65YbnUy0kWSjwA2fpIcUNNdh-RC8uRtW_5dOfKJxbz3VeiVwUHhrrTykXISrRLZzh5b9CoGfUeVfZXDcAFfEaKVRa4ON0jLpywBgtxpA59nIGOqrVN2aAjB-KEKzRbsjHH_QoQYJcIiDEsr5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qEpe4LmxEWV_F5i_xbDsHeRPcRu-8Rt5bCggjLp3dEUdEeBgCk0ABjjVPFbTsfQvraSAp-TrfVipxfQxfOgJYCJzD5IThAZRpbENdDp1LtlBPsnZ8QIMAxoTBigpdpUKqyjXphb2Ctm-eo88TZg4p6mc0hVtC-obOuRp0qlI0N5qnmKnu42X6TdlYt5uGryUYr0dHlNQt7F4DsUvkTW7kHjqqM44jz6RTkGhUi4jan3lGxhn-qHHTKsE002iHRXmzYeTEBKRAK1dJ4_5NMxjgNLUs8RctDhClGZT2ZWa9y5zfu5cF-_MgYaVsRvUnb3gyqVa-Iim726GWaDtsDsv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tHSn053fMG97pfaB0nUUa2TTtwxpe43nt2d9cr6Z_mygiTZTZKRRUBsECcwWOzkOL-X296EotYa2RmfDxavRCVTRRG_DKjbrNczLvWWfALXSaDMvxquo6Ok3dC7wzRijxf_CbEEK96q7prI4UoMXJNV2ryWsCLi1Pyg6X7jd1hL9uRfCIgpLezaUUTcW2xCVzg4X6X3l774aMqOmfZQon0xAG1pgwB5E-tINXdiwCdAQT6xzZSYRyf0gFRh_fLQN_bwSI9NsgalLP2bv7s4k7gP07HkSbZrWwquPVzuDgUpC1dq1gqv7txpD4rhST1fGliTjFafPByJAkqBlm2vSrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQunURc8dEwjQ3o1Fd7iEmnNP4JmxXpa-V3THOA40T87QNg8M8tCC7g6GX-PqTAmXMl-C19L5PDXR75GBEBfAwsh1ep2SLisEY9IebyMs2MpWiSovQFPd6cQw8Uv1RotJaYJSBniFBqz4eFoLe8xZpAU2m3dG6AR_S_4yCHW1jN7jrxVVfYAbHmpaDcPKsyKox03ZvB1_-nwwKUyYmaRBlo9rDJVemO5iyHtQos_IddF2fVrE3U1DGcaHKMBr0VQxMGsEblxBwntBuCVN4eL5HjER19_WsK8V_JrFrq3U6fXF_FW6L7gOzle4iAFt3iHYRkbL6meoSHqlm5EtznlWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrJXNJyJ8GeevdaUb8XS5FO2JfKYz5aVmHNhfMmkvTMluiH9Lja_B-M05_VycuGNeLfpAoN3Fho8SWuL7hHn9fMUs96i60UAIbZ7R0hE2MPdHYJTt31qGQklijRg1kQw-aFSvoQfoaB0cvVarEomGvaChS3Ou_RZluiLrslhxS__foGnuhSYkP3YAFYTThuV55IudCuGjjX3-afPrUnM6SkQfgCnJoCClHCODfkEOyRjHdZc8X9xZnH2yP-nfRp2TNuqrpSuivdpTGKu7EhU6AatezLOVx2e0TN1kwFJWziYACmNHdDrZOHxH0Z2_DhmRTQ-dwlmHDwHgaPV5RxJ2w.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=adgeSoSFokRyBKO4svZeKsegEfEE5Ydc1k0MO6wUZl03TqBupxIyMqotlMvsKPEYIOqujz48UNVNhegbU6L5JCA95T3kxpgGlOe_TTebV7vGn8IuWK7AxjMtwpNEGsmFFq8IVH7VeL86OelYsQBggYzR_cLeg-IIKGCqbIBWHtfHFMNIleWJSkYPj6e18_g5lTvypmsQU1XpubSRJzuPZwBL37-tVY4i5Ss453uDn4xC9bYMsC4-ZEDYPr_L-Ar6M1mTcMxOA0_1beyFhrwg0qryhoPcTJjAm-7Wsq9rO3Z0JrXP-7nzM3SlAIChuq_kLHKp8Pp2l8qCkwNRPeY8pw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=adgeSoSFokRyBKO4svZeKsegEfEE5Ydc1k0MO6wUZl03TqBupxIyMqotlMvsKPEYIOqujz48UNVNhegbU6L5JCA95T3kxpgGlOe_TTebV7vGn8IuWK7AxjMtwpNEGsmFFq8IVH7VeL86OelYsQBggYzR_cLeg-IIKGCqbIBWHtfHFMNIleWJSkYPj6e18_g5lTvypmsQU1XpubSRJzuPZwBL37-tVY4i5Ss453uDn4xC9bYMsC4-ZEDYPr_L-Ar6M1mTcMxOA0_1beyFhrwg0qryhoPcTJjAm-7Wsq9rO3Z0JrXP-7nzM3SlAIChuq_kLHKp8Pp2l8qCkwNRPeY8pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
