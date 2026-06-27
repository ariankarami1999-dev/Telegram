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
<img src="https://cdn4.telesco.pe/file/VrBFWjSZbQjpGI-RwGZ3wZ8ONwVzniD9FjofM5M4RgAWAiF3Wpo3uJhOkKs5Hgwvlio9mZLO-yS7ya62T-XTzWczpeKGg3n8nNCB4hRqA_ABka4eZ7Q3_gjANNpehDnXAa_SCvtY1wXtFVeUVDHl_qRotquHBbtLGXlCL5Ofnjp4rjfosSxgVkb3y1wIa-WEZZ29wIUHp0SVi6Dzxx9kqG3uf-MNKMUpKOMHhWt6A98XD0tCM668mIV5eBv0NVk235ruDSvmV48OY6Alc88tFORcGabjDRgCgYaFGPEwHK7sJVmr7ivoHyvu2RjSn83pW6UxaOIotbgg9btlYJsmRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 06:13:10</div>
<hr>

<div class="tg-post" id="msg-15907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144f492601.mp4?token=F7nRc4c6WO981_hbclCOKk6NzfTpIjE5zYox9tCjbNIAWDvHcIEz1ccLsXCLJqg8LO5joxoPEmCBSpTV2MDrXJAyr4F8510U33IWKSuGqwsLvXq0THAuFPBU-TAMOZZ06iBrEbeiHZBLESQ-G_8nLXhwP2W4T8bskbbAfiPeBSJdIZjat0req1SUft127RrP1dShWE3HbBvZUibwQeDCLk2cEahkuek_3Nj1whRpvyxXscyvQcdIGmmXuA1fwsYH8dGxnTt2Ny5KiQQPihxpcNDjih1Qz1lCvxrW-3v50M9nw6Y1pBHTz9pBaOC1YWN2ykFO3uXgxq-mlQraPMvSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144f492601.mp4?token=F7nRc4c6WO981_hbclCOKk6NzfTpIjE5zYox9tCjbNIAWDvHcIEz1ccLsXCLJqg8LO5joxoPEmCBSpTV2MDrXJAyr4F8510U33IWKSuGqwsLvXq0THAuFPBU-TAMOZZ06iBrEbeiHZBLESQ-G_8nLXhwP2W4T8bskbbAfiPeBSJdIZjat0req1SUft127RrP1dShWE3HbBvZUibwQeDCLk2cEahkuek_3Nj1whRpvyxXscyvQcdIGmmXuA1fwsYH8dGxnTt2Ny5KiQQPihxpcNDjih1Qz1lCvxrW-3v50M9nw6Y1pBHTz9pBaOC1YWN2ykFO3uXgxq-mlQraPMvSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری تن به تن نیروی های لبنانی و طرفداران حزب‌الله
@withyashar
یاشار:درک به ما چه ولی ، روزهای جالبی در انتظار لبنان است... من خبر لبنان بدم میاد</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/15907" target="_blank">📅 01:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15906">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سپاه پاسداران: «ما تأکید می‌کنیم که این حملات بی‌پاسخ نخواهد ماند و پاسخی سریع و قاطع در زمان و مکانی که ما انتخاب می‌کنیم، داده خواهد شد.» @withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/15906" target="_blank">📅 01:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه :نگارن نباشید  ما با پیک موتوری میبریم براشون ، قااااررررر قاااااررررررر
😂
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/15905" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مردم : کجا ما تازه برنج خیس کرده بودیم @withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/15904" target="_blank">📅 01:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی ان ان: حملات ارتش آمریکا به ایران پایان یافت. @withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/15903" target="_blank">📅 01:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک مقام آمریکایی به «نیویورک تایمز»: حمله به ایران، ازسرگیری عملیات جنگی گسترده، نیست.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/15902" target="_blank">📅 01:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سی ان ان: حملات ارتش آمریکا به ایران پایان یافت.
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/15901" target="_blank">📅 01:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بیانیه سنتکام :  امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/15900" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن @withyashar
🚨</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/15899" target="_blank">📅 01:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZrf0Jy8-cZ37vFP-GwlNxI42E1WojBuuys2H-pr62Q6HvhLGQoD2s0Ke6sHiONHt2W-W3KPBMPS-ZDaiaNAi2YmGi5JjnPLzIvnIGocalFZycA34G311oTx3dGR8QwXI071vm9WuoKkEjvD1FhYXx_KtU7e_X1keb0oh-H3rWcMpyTUeDn9Zf3O5qe975-qcPqTA7soQvFdHBAkGx_J8dqx-3JA530gx9mVSDcTsWtiQtWIr5yJBuI3ROm5uPogXXEG_GgKTbDoMk9npJ1K8D0VK3JAPbXb64zPjDUhE44YnQO5oVkGXE9bueOK0QAXSorSnYqXfR9qY09hEfBVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ششم تیرماه، روز جشن نیلوفر، (نیلوپر) روز دختر در ایران باستانه
@withyashar
یاشار: این روز رو صمیمانه به تمام دختران سرزمینم تبریک میگم، مخصوصاً خواهران عزیزم در اتاق جنگ که واقعاً من را حمایت کردند. مرسی</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/15898" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/15897" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا به یک مکان در مسن قشم بخش شهاب جزیره قشم حمله موشکی کرد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/15896" target="_blank">📅 00:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن @withyashar
🚨</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15895" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به ایست بازرسی بانه سقز حمله شد و ۲ نفر کشته و ۵ نفر زخمی شدن
@withyashar
🚨</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15894" target="_blank">📅 00:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اعتراضات طرفداران حزب الله به   امضا صلح با اسرائیل‌
درگیری شدید و ارتش لبنان به سمت معترضان در جاده فرودگاه بیروت گاز اشک‌آور پرتاب می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/15893" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدای انفجار و جنگنده در مراغه
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15892" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه پاسداران: «ما تأکید می‌کنیم که این حملات بی‌پاسخ نخواهد ماند و پاسخی سریع و قاطع در زمان و مکانی که ما انتخاب می‌کنیم، داده خواهد شد.»
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15891" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صدا و سیما:ساعت ۲۳:۱۵ امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.یک منبع آگاه نظامی علت این انفجارها را برخورد یک فروند موشک در محدوده اسکله طاهرویی سیریک اعلام کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش، چندین تیر هشدار از شهرستان سیریک به سمت شناورهای متخلف در تنگه هرمز شلیک شد.همچنین گزارش‌ها حاکی از شلیک دو موشک هشدار دهنده چند ساعت پیش از اطراف کارپان به سمت تنگه هرمز است.
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15890" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مقام آمریکایی به فاکس نیوز: حملات همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15889" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY2ebmp2VXiYMYbWYf9C_65UO0TlxBLAWIImNLeEbRBl6gjdXfbvclWrn7DdXjo3G3IKwpjkuNwYiQskLM79Ta54CIELzQmu-roOLbE9fdU0u08lB1-eMAGZoq6q7V4hk_INdN7TWa0XZPlYw11qXrhoA-iFFSChlqwf2mG7C2Zj9mDQ7cgwVKI7BByNp7yb_8FX6ZhHWUhGJSfTKfk3opeVng93j46jWrcQmFyLrrHi3k_y-H08In18rKm2NARPf9fkuCPX1xgoaAuFpani38VJZvhMpS072pMyu4lRGVCuKnkHBtgfOt5d2HD3MoaJiwBHXReBqaXESqSv9R4pFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام :
امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.
سنتکام این حمله را نقض آشکار آتش بس و تهدیدی برای آزادی ناوبری خواند.
نیروهای ایالات متحده به هماهنگی عبور امن برای کشتی های تجاری ادامه می دهند و می گویند که برای اطمینان از رعایت کامل توافق، هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15888" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15887">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرنگار آکسیوس : یک مقام آمریکایی به من گفت که ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15887" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15886">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار : همین فرمون بیداریم تا بازی رژیم با مصر …
💥
زارتان زورتانه گویا</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/15886" target="_blank">📅 00:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15885">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منابع آگاه : سپاه قصد دارد اهدافی در منطقه را در پاسخ به حمله آمریکا مورد هدف قرار دهد
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15885" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15884">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سنتکام: به دستور دونالد ترامپ عملیات محدود ما در ایران آغاز شد در جواب شکست آتش بس توسط جمهوری اسلامی @withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15884" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15883">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اتاق جنگ با شما : سه انفجار فوق سنگین همین الان سیریک  احتمالا اسکله سپاه سیریک یا اسکله طاهرویی(چون تو یه خطن از این زاویه نمیشه تشخیص داد کدومه  احتمال ۹۰ درصد جواب اون پهپاد های ج ا رو دادن @withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15883" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15882">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام: به دستور دونالد ترامپ عملیات محدود ما در ایران آغاز شد در جواب شکست آتش بس توسط جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15882" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15881">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: من از شلیک دیروز ایران به یک کشتی در تنگه هرمز خوشم نیامد/ آنها نباید این کار را می‌کردند و به زودی پاسخ ما را خواهید دید
خبرنگار: آیا همچنان معتقدید آتش‌بس برقرار است؟
ترامپ: از این خوشم نیامد که آن‌ها دیروز چهار موشک به سمت یک کشتی شلیک کردند. ما سه تا از آن‌ها را ساقط کردیم. آن کشتی متعلق به متحدانمان نبود، اما به هر حال یک کشتی بود؛ یک کشتی بسیار گران‌قیمت. کشتی سالم ماند، اما کمی آسیب دید. آن‌ها نباید چنین کاری بکنند. بنابراین، خواهید فهمید.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15881" target="_blank">📅 23:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15880">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرنگار به ترامپ : شما گفتید ایران آتش‌بس را نقض کرده است. آیا آنها با عواقبی روبرو خواهند شد؟
ترامپ: خواهید فهمید.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/15880" target="_blank">📅 23:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15879">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارشهای شما به اتاق جنگ : سیریک سپاه سرخور طاهرویی رو زد
گزارش ها نظر بر ‌این هست که پهپاد ها هم امروز از همین مکان شلیک شده بود
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/15879" target="_blank">📅 23:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15878">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/15878" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15877">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15877" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15876">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db6vvXvyI00KTHHmHfy5nybrn0n7KyBDzuEneqEQnXKfVg3LT-oPJvoRVAOPB0mFkIQ65TNWpb9YhcqUhM8qD35A6ROac29dI0-Lpry87uJK6qIFfLiHjmced8Ij-rLKDO8yqX2L8s-1BHIxPOjc62dkM-Dwbj3-FQc2gWAjI-l-tKwvRrw6iuDwLjQ6B1jPu0BH343dQHebsR9s4uRFxAlexjGUKSOJGw04sddKnuXVBdu3eibtQriC9vALyiwTxyP85J5vftB8X-LYHnFTKvkzeGAXirf0R7EWVy6Ha8Qn_mhbLJ6tDTd2vQ5H7e_VBJ-MU5NmxlwJQvJbuC7-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با شما : سه انفجار فوق سنگین همین الان سیریک
احتمالا اسکله سپاه سیریک یا اسکله طاهرویی(چون تو یه خطن از این زاویه نمیشه تشخیص داد کدومه
احتمال ۹۰ درصد جواب اون پهپاد های ج ا رو دادن
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15876" target="_blank">📅 23:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15875">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15875" target="_blank">📅 23:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15874">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هشدار روسیه به سئول درباره تحریکات نظامی با آمریکا علیه کره شمالی
وزارت خارجه روسیه تأکید کرد: اقدامات نظامی کره جنوبی و آمریکا در نزدیکی مرز کره شمالی موجب تشدید تنش‌ می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15874" target="_blank">📅 23:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15873">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2d413441.mp4?token=KEygERooQ8gnxfKJwjFBweYrqV1OUiS5zjsK8WLnAlTSojXHCSytAmz4za1s98v2q-7yFFK3mdYd03Cp_Jh7nyaQbb9LOQEnEG67gaciK7wG0ob5nS8O_AjJJWlN3YGV3AorD_TXyd6s9VSAst6pDqdtTVesHSv-v7Fv-srWzWvldXsFapACtw7QOt7TqGaO7RwFZqx-XLpaYsyTKLkEeKXLz3A75KBFNKGPfQWuj6x9nM_VkwtQds9T-lCVudW0bLtViuKPpjTGn1oqCa1D0JYAIQX9UGsRRStUbdQKTm5Hw5Olg6sw6gOgxhOwl_DKG3IPJFMdrNd6XgKWHumV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2d413441.mp4?token=KEygERooQ8gnxfKJwjFBweYrqV1OUiS5zjsK8WLnAlTSojXHCSytAmz4za1s98v2q-7yFFK3mdYd03Cp_Jh7nyaQbb9LOQEnEG67gaciK7wG0ob5nS8O_AjJJWlN3YGV3AorD_TXyd6s9VSAst6pDqdtTVesHSv-v7Fv-srWzWvldXsFapACtw7QOt7TqGaO7RwFZqx-XLpaYsyTKLkEeKXLz3A75KBFNKGPfQWuj6x9nM_VkwtQds9T-lCVudW0bLtViuKPpjTGn1oqCa1D0JYAIQX9UGsRRStUbdQKTm5Hw5Olg6sw6gOgxhOwl_DKG3IPJFMdrNd6XgKWHumV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است.
من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
او یک ژنرال درخشان بود. او مردی بسیار بیمار از نظر روانی بود.
کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که در خاورمیانه رخ داد. مردم گفته‌اند که بزرگترین اتفاقی است که در ۱۰۰ سال گذشته رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15873" target="_blank">📅 22:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15872">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ: اخبار جعلی گفتند ایران امروز بسیار قوی‌تر از ۴ ماه پیش است.
آنها برای رسیدن به توافق لحظه‌شماری می‌کنند.
آنها چیزهای زیادی به ما می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/15872" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15871">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=CfhL9wIfC9oPXcxy_HUVvQrKOwP-UohWuuJgj0amhOqsLQ7wI-qQCT8k7G0t_Pt6S1fhJ8gFQe5NTUp90cR1ONEhrht5XC_7EDS6XRtLdBvD2H3M2bWJpWm1r_cJj5dnpNx8PJ2m8gFojI7MFRTS4YHs2CC_UtW8M5ye4O9EZ18xelDo4jVivo0o9ohvlXVFauI6F9nMDPKWN9GuPopxYE3TBPosMz7GIHfhP9H-8W_L50pyGjzyF-2Yfr1xxqgQFP7X_AiPUQCzjeQpAlNT9MWKRZOypasK3m9OoiPkXZUTRfrKgQRvjTjE2vUAdCm60PQVg-ZEWPtvMRVyJklMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514bc17e72.mp4?token=CfhL9wIfC9oPXcxy_HUVvQrKOwP-UohWuuJgj0amhOqsLQ7wI-qQCT8k7G0t_Pt6S1fhJ8gFQe5NTUp90cR1ONEhrht5XC_7EDS6XRtLdBvD2H3M2bWJpWm1r_cJj5dnpNx8PJ2m8gFojI7MFRTS4YHs2CC_UtW8M5ye4O9EZ18xelDo4jVivo0o9ohvlXVFauI6F9nMDPKWN9GuPopxYE3TBPosMz7GIHfhP9H-8W_L50pyGjzyF-2Yfr1xxqgQFP7X_AiPUQCzjeQpAlNT9MWKRZOypasK3m9OoiPkXZUTRfrKgQRvjTjE2vUAdCm60PQVg-ZEWPtvMRVyJklMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: دیگر هیچ‌کس نمی‌خواهد رهبر ایران باشد.
آنها پرسیدند: «چه کسی دوست دارد رئیس جمهور شود؟» و همه گفتند: «نه، متشکرم.»
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/15871" target="_blank">📅 21:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15870">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=EQS_e-zfz9HFt6xySQue0vuOA6TI-IK_1-N6-uI8iVK2BBrQPgUNsG6QRlVaLSIg5bmRLf5z4maafBsPnWK_FLISfCFGzpCeeGOBMBs62YaU61sIid0JOcywc9IDk63l_oH4lBA9BWHrO-YTZSj6CM7JBP8K25l-DrJDvlsoXLCSFtMutjVnbjW0hCI29HZcih8OOwh9xLPIIBNlFd7KSwbNda9M_S_e8Gpb-VTjsUsk5-WK_v0URsRMAXIGd2wQbSqjEsQGglPMJoheoHTqCzE5ISYFsEkSyENYuayHBiAIBWGyfMBZZbmmzK7ywBfddpAvR-wgB3IzGeYNry6HFU5Kyrf3y8WTSiZJAgoApVivxlXEHd_N79ST7AUP1n2HqFyOLU_Vc2STR3CHI00j2ilWLhbhNT7BQ8oTiAr47LRNiLE0PT6BDS0rlu9sAi-5uIufPuSkBeCbWLxyXGJfP82PBEGJBRqitSKOndL4ExWOdKg7ln3dGKlkNwjalGhndzEH3MFzPGsviXnoD7m4LS3Cx_OHEiiI4UqqBbjop7VfEjtYdldTcUSpPP-R_XDu_HkuzOc7Ml1vEYL0TEL2QkqurPWdKxQtyWIPmmTGzDqXMGFjXs1gxoPVFigufhVjRrCrVq_NXv_S7n3x61vEls4ZCPNsGh9jcWPpZW-3G58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44d4d0504.mp4?token=EQS_e-zfz9HFt6xySQue0vuOA6TI-IK_1-N6-uI8iVK2BBrQPgUNsG6QRlVaLSIg5bmRLf5z4maafBsPnWK_FLISfCFGzpCeeGOBMBs62YaU61sIid0JOcywc9IDk63l_oH4lBA9BWHrO-YTZSj6CM7JBP8K25l-DrJDvlsoXLCSFtMutjVnbjW0hCI29HZcih8OOwh9xLPIIBNlFd7KSwbNda9M_S_e8Gpb-VTjsUsk5-WK_v0URsRMAXIGd2wQbSqjEsQGglPMJoheoHTqCzE5ISYFsEkSyENYuayHBiAIBWGyfMBZZbmmzK7ywBfddpAvR-wgB3IzGeYNry6HFU5Kyrf3y8WTSiZJAgoApVivxlXEHd_N79ST7AUP1n2HqFyOLU_Vc2STR3CHI00j2ilWLhbhNT7BQ8oTiAr47LRNiLE0PT6BDS0rlu9sAi-5uIufPuSkBeCbWLxyXGJfP82PBEGJBRqitSKOndL4ExWOdKg7ln3dGKlkNwjalGhndzEH3MFzPGsviXnoD7m4LS3Cx_OHEiiI4UqqBbjop7VfEjtYdldTcUSpPP-R_XDu_HkuzOc7Ml1vEYL0TEL2QkqurPWdKxQtyWIPmmTGzDqXMGFjXs1gxoPVFigufhVjRrCrVq_NXv_S7n3x61vEls4ZCPNsGh9jcWPpZW-3G58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم
«کمونیسم همه‌چیز را نابود می‌کند، اما بسیار آسان است. راستش را بخواهید، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
من اجاره را رایگان می‌کردم. خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی که خانه می‌خواهد، نگران نباشد. فقط خانه‌ای را که می‌خواهید انتخاب کنید. همه غذای رایگان می‌گیرند. از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی خواهند داد. در سال اول، شما محبوب‌ترین فرد هستید.»
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15870" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15869">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=j6p1F6r3k9zOXNfhOGue2ScQp0OO-fR4c7lvjByxXL7hfL-XironVhVTrmeFrbV8tHZPvc4o7VbyzEeeb41vtJmK9JKe93XN3h-W2wYkjPmeaCnxKyISsqDQu4r_4fCFEasHvcZ48X81B9-isY9OA-3tVCuS_jHOlJZOJ3y14Z_OP0TbZhfAkKch0Vdgwg4bMqf7ajHOwC6nugma2OzoDSsJ2uydglZtg2ectY31TBPXKkQqiGsOf8cg0_9-KVUKWommsHSdBPtSaTNmK5yVdRpkhyidilVcvoyATrkFNeTkXnOWQyZPy6bkhk4HwFX9Ezd8yzAaNUwERjwTPhRImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8d4b334.mp4?token=j6p1F6r3k9zOXNfhOGue2ScQp0OO-fR4c7lvjByxXL7hfL-XironVhVTrmeFrbV8tHZPvc4o7VbyzEeeb41vtJmK9JKe93XN3h-W2wYkjPmeaCnxKyISsqDQu4r_4fCFEasHvcZ48X81B9-isY9OA-3tVCuS_jHOlJZOJ3y14Z_OP0TbZhfAkKch0Vdgwg4bMqf7ajHOwC6nugma2OzoDSsJ2uydglZtg2ectY31TBPXKkQqiGsOf8cg0_9-KVUKWommsHSdBPtSaTNmK5yVdRpkhyidilVcvoyATrkFNeTkXnOWQyZPy6bkhk4HwFX9Ezd8yzAaNUwERjwTPhRImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
دین درحال رونق گرفتن است
«دین دوباره رونق گرفته است. دین واقعاً در حال اوج گرفتن است. اگر دین یک سهم بورسی بود، همهٔ ما بسیار ثروتمند می‌شدیم.»
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/15869" target="_blank">📅 21:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15868">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل در چارچوب توافق تفاهم با لبنان، تا زمان خلع سلاح حزب‌الله در مرزهای خط زرد باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/15868" target="_blank">📅 21:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15867">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6nEZYZC21Sewau_eiTS_srltduImOlisHNaCak7JxLtAPTOgxiviFDpH25CuQc5dShMsTKHYKoCAUCJDNsd6SByJkYlf1mVw6Up3XDWphd7Yb3hTTIMSrp78trEtI3gdfiYu-4iXiE6vYnTXX66Q0rGoORSHiOtE9nRMce17uSdcduhT5IYKKKkmSkTMUXpaIJkdJkH12o4WG6bje5KY_c_RbBVVFFWStgoete5kTYMRFnRmc1eJAry7nTKCbCS2oHoZEUdrjoowvdWaFKs5tg8LWv5Y-R-nIzyNofcHzQCaTtmHYZIQvmPozhrSxO4ZldbgFziLj7VnQSg4VLjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : اتش سوزی نزدیک فرودگاه امام لعنت الله
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/15867" target="_blank">📅 21:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15866">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">افزایش شمار قربانیان دو زلزله‌ ونزوئلا به حدود 600 جان‌باخته و هزاران زخمی و مفقود
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/15866" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.  این ادعا هنوز از سوی حزب‌الله تأیید نشده است. @withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/15865" target="_blank">📅 20:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد @withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/15864" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15863">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار آکسیوس از امضای توافق بین اسرائیل و لبنان خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/15863" target="_blank">📅 20:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15862">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سپاه : ادعای مقامات آمریکایی درباره برقرار کردن خط ارتباط مستقیم با ایران در مورد تنگه هرمز، کاملا ساختگی و دروغ است.
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/15862" target="_blank">📅 20:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15861">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ارتش اسرائیل: نیروهای ما در حال تحمیل یک واقعیت امنیتی جدید هستند که به حضور حزب الله در این منطقه استراتژیک پایان خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/15861" target="_blank">📅 20:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15860">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/15860" target="_blank">📅 19:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ در‌ تروث: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌ها در تنگه هرمز شلیک کرد. یکی از آنها به طور محکم به عرشه بالایی یک کشتی بزرگ و گران‌قیمت بارگیری برخورد کرد. خسارت وارد شد، اما کشتی به مسیر خود ادامه داد. ما سه پهپاد دیگر را سرنگون کردیم. بدیهی…</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15859" target="_blank">📅 19:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15858">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQF9RyXXRBFz0Cg6P_NrkxzvliDTScRZjOz-uxW87lm56Zpi4m47R2UEF9boBy3V_WyF1jfwZDN-ntiuOJOxsccwAB8Zc6kIw6TzRVmr0gQPesKvhwWRitgxDJJ61k1qKqrGMPAHcBAnWgziA8jQL3DK49CMzLaW4BjgTH-KHTUp-1bJWwIlmnBHpGAaaIn9M366mITjtHSutPk6Ulr-DsTYCTd0xkV21sFvQ5TJSsqoxKbj0s1OHNfHJ21NunaKAPNShtMbmV8eTNAMEjw7GhSpEtgqcqnz-ylABFn-9MaawekopIl7svPHYcH1s7RDTvLu30NJyfYj9yMID3tpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌ها در تنگه هرمز شلیک کرد.
یکی از آنها به طور محکم به عرشه بالایی یک کشتی بزرگ و گران‌قیمت بارگیری برخورد کرد. خسارت وارد شد، اما کشتی به مسیر خود ادامه داد.
ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15858" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ارتش اسرائیل مدعی تصرف بلندی علی الطاهر شد
ارتش اسرائیل : تپه علی الطاهر در جنوب لبنان فتح شد و نظامیان ما کنترل این نقطه را به دست گرفته‌اند.
این ادعا هنوز از سوی حزب‌الله تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15857" target="_blank">📅 19:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه: عمان به اروپایی‌ها اعلام کرده است که دیگر راهی برای بازگشت وضعیت تنگه هرمز به دوران پیش از جنگ وجود ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15856" target="_blank">📅 18:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15855">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دولت امارات: در حال رسیدگی به یک مشکل فنی در سامانه هشدار زودهنگام هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15855" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15854">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyyaiPJBhgelwq4AI4AvHcqNCFlKuoMwMA2meSvUvC3NXKp4ozB4W9J6xFo7oFjjpC0wtrS8wsGKoHWAOv5uf5ryrAmWzjV_IjZhzvFykljTzyE0lyCMxGxXdKk_hg4YkbMhmQMZ7S2EiYUAIb_slS09bwlE6r4CvBvZ1JaUZODp6DUMFNRHQUuu3dnkY8SdmvGHKPoNCkxkFW89BBFmeylTswE4ah2PUYm-8O0Ia9tsQ4NjdrrvOl1WGGxACmY2XxKMhGLHyj8QbAXzKU5ndNRmCylzBF6CzgUDoQ28ogvIHOeWGKylcpJvHcuoLQm2pAhsb10nOnO5C_ORXz0fBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سیاتل همجنسگرایان دارن از الان گرم میکنن آماده بازی ایران و‌ مصر بشن
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15854" target="_blank">📅 18:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15853">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جان بولتون، مشاور سابق امنیت ملی آمریکا، در پرونده نگهداری غیرقانونی اسناد طبقه‌بندی‌شده متهم بود که بخشی از یادداشت‌ها و اطلاعات محرمانه دولت را خارج از سیستم رسمی و در محیط شخصی نگه داشته و در برخی موارد برای امور شخصی استفاده کرده است. او برای جلوگیری از دادگاه طولانی، یک اتهام سوءمدیریت اسناد محرمانه را پذیرفت و با دادستان‌ها به توافق رسید. طبق این توافق، به جای زندان، حدود ۲ تا ۲.۲۵ میلیون دلار جریمه پرداخت کرده و پرونده با توافق قضایی بسته شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/15853" target="_blank">📅 18:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15852">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت: فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است، به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،…</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15852" target="_blank">📅 18:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15851">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : بررسی وضعیت پروازها
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15851" target="_blank">📅 17:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15850">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی به سرکنسولگری ایران منتقل شدند
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/15850" target="_blank">📅 17:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15849">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امارات : لطفاً هشدار قبلی را نادیده بگیرید.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15849" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15848">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وضعیت عادی شد
بر اساس الگوهای پیشین، در مواردی که در امارات آژیر هشدار فعال شده و سپس به‌سرعت وضعیت «عادی» اعلام می‌شود، معمولاً این شرایط با رخدادهایی مرتبط بوده که در نزدیکی سواحل یا مسیرهای دریایی و در اثر حمله یا حادثه برای یک شناور رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/15848" target="_blank">📅 16:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15847">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احتمالاً پهپادهایی که از جنوب ایران به سمت کشتی‌ها در تنگه هرمز پرتاب شده‌اند.
گاهی اگر مسیر پرواز مشابه باشد، باعث فعال شدن هشدارها در امارات می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/15847" target="_blank">📅 16:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15846">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15846" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15845">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هشدار موشکی در امارات</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15845" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15844">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15844" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15843">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت:
فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است،
به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،
هیچ چیزی ما را متوقف نخواهد کرد،
نیروهای ما آماده‌اند تا وارد جنگ شوند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15843" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15842">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6I_6Fgr01rXVmljbwClDSRBEbXBfkWZAvgcJYMNWc7MONybSisNPIq0NnGrDIPedQ7t984yWYsKChptE7Khy0aFkm4ZSr-iA4bjAWucgWyYc3F0w1iisV3cYOgSoHRld2eVUm0dUe09zYp-FA4cED3lUqoGXpQm7OE4iLL2aFCklDsSe4m0hpSfGCUe6JotgQT-2Dq-LGIn36-4X3bpbnuzpN_so-X6Mxc9zUvjzNKL-7WvjxDloY0Jq2A_x4QjC4qTXZNu8qUkgBDVR0XEq3hKo45MY0Pu7QJPPXDNlqhJuwQpBmNO--J55HD05h4ooGx9avqTS-04tVVaMczMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت اعزامی به انبارهای گندم ترامپامون
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15842" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15841">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/15841" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15840">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b7f6c830.mp4?token=fkAZEVM8qhltO47yaDqGAQKU6sQsUxwVUSYgoVKo8bTKwkjzXN5kku7i4uEkap4CH5GyGzH7uJFiNa4qpJKk3qMVvhzAoBaDbW2tWLOOOSCuarM_thG3TSCnTCcXaroqeCnkGWTWF7XcMslZiib7o36wvNowZp8eyvrBny6Z_9l-Jlw1Iw6lbCthspSnej2YeNnWGW6JMG4mjbDXoLLYOYOI5BBu6OyU4MxZve5UV30H9C89nlVckWlIdWlAnzj2xqt6enycIbymA8R_6yvxrKUwBDNgJ4i6RLvFtdPo2O7neWei6NZOKHXGSON6RHJn1BwH1Dr2CMzi2WBqUVLqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b7f6c830.mp4?token=fkAZEVM8qhltO47yaDqGAQKU6sQsUxwVUSYgoVKo8bTKwkjzXN5kku7i4uEkap4CH5GyGzH7uJFiNa4qpJKk3qMVvhzAoBaDbW2tWLOOOSCuarM_thG3TSCnTCcXaroqeCnkGWTWF7XcMslZiib7o36wvNowZp8eyvrBny6Z_9l-Jlw1Iw6lbCthspSnej2YeNnWGW6JMG4mjbDXoLLYOYOI5BBu6OyU4MxZve5UV30H9C89nlVckWlIdWlAnzj2xqt6enycIbymA8R_6yvxrKUwBDNgJ4i6RLvFtdPo2O7neWei6NZOKHXGSON6RHJn1BwH1Dr2CMzi2WBqUVLqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل برگه‌هایی را بر فراز شهر المنصوری در جنوب لبنان انداخت و از ساکنان خواست تخلیه کنند، که این اولین دستور تخلیه از زمان آتش‌بس است.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15840" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15839">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش اسرائیل برای شهر منصوری در‌جنوب لبنان هشدار تخلیه صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15839" target="_blank">📅 15:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15838">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدا و سیما : سه نفتکش خارجی که قصد عبور غیرقانونی از تنگه هرمز را داشتند، پس از هشدار سپاه پاسداران به بنادر خود بازگشتند.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15838" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15837">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPjEJgVe_6p_9OfyfcZaBqgyHWaHxM_EShTHWoX8NBXVKJP4FhEClMGA1HxiCQRMgKP33UQhZDUIxV0ZWGUMvkH8gN6TRos6JzOI55v3S3JTmNyPU7irg7BbUFvN9y7n_iFSYR4OfqznT84_lPabzqexdGqt6oXUbuNgXndgtHGTfTUT6kBcMuf7vAFfsCLTtHrQ535oGnrGQhHiElOwg0-k26fT3qVwEJeUxOT9ISpIDwjlY3N7X8YnS8PLotA52nD9ef2GEtjs9Jp_Pc9bWPxz-Sz3a2wJD7Dra6T2w_EXXou4c6y0eG0W7Jpex_zazl6TTCGAYAlHHrM8wiyMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارداد 35 میلیاردی پنتاگون برای خرید موشک‌های رهگیر سامانه پدافندی تاد
وزارت جنگ آمریکا قرارداد بزرگی به ارزش 35 میلیارد دلار با شرکت لاکهید مارتین امضا کرده تا تولید موشک‌های رهگیر پیشرفته THAAD را به‌طور قابل توجهی افزایش دهد.
بر اساس اعلام پنتاگون، این قرارداد 7 ساله قرار است تولید سالانه موشک‌های THAAD را از 96 فروند به حدود 400 فروند افزایش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15837" target="_blank">📅 14:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15836">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برادر زاده اسماعیل هنیه در حمله به نوار غزه کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15836" target="_blank">📅 14:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15835">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15835" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15834">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBwa2uTW7OFqiFzWvWMpnteqXi35Ax6BtGIYys_GujBJTjL76roM0wXR1R4wqyebn9gnUu38Kwvv2OZnpCnJUlncYUNKJaH3msgFQ1ofsyRV6BsVQeVgYrgzv8gHsjqV-6BECU9MAN6A7gM6wqnHbnPVLdS78BCuyFO6iXFlOzawajdAvNVKTA6XKdzuJz6Pbj8lpltd8ximynLu5_VHX0FgDNiRQPi7IeVtAaXgk6sTRRdNmWlBin4FOhJ_UmHETs626QaScqmPVscURCr10fj_OshWUDngee3EEWqlX9h3wIMOlPbRGBx9t5v9-3fZrg9wkGv8dJ_dp7pLP-sAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما با کپی‌برداری از اینترنشنال اومده کنار پخش تلوزیون، عکس کشته شده‌های لبنان رو گذاشته.
@withyashar
۱۸ مدل هم اتاق جنگ کپی‌کردن‌
🤣
کلا کپی‌ هم بلد نیستن</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15834" target="_blank">📅 14:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15833">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d351d6.mp4?token=AQ8sT8sune4g6U9PKJRIaMiT4oxlKG2ZOqNAj-3y7TVu_vQURfj0gqgAA8tRTG8EiaW6UcVBDtRtEe6G83QNQVpwiCKCx6B1PKVqX4e-hPWMp3Zg6J_UG94e_5S19uh4QWWP1q91Bh25Ki9rRxc69L_RJhaPneWIz_Jc2vKVTcBfqZETj_Vk1wjcx_ND0ChzvGzAL01CtK5541rCv7lyZXOAQ3qBCnpg5JES_9UNqyijoAyu3EFBMcqa2cCqFCBwJUyQMxetZgOqbnnKt3YLe8ICCcexC83kq9dB45hdrKt-FRYowd8vj5C3rE7bZtPQCLCvqMeTTSsuBza95ZlK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d351d6.mp4?token=AQ8sT8sune4g6U9PKJRIaMiT4oxlKG2ZOqNAj-3y7TVu_vQURfj0gqgAA8tRTG8EiaW6UcVBDtRtEe6G83QNQVpwiCKCx6B1PKVqX4e-hPWMp3Zg6J_UG94e_5S19uh4QWWP1q91Bh25Ki9rRxc69L_RJhaPneWIz_Jc2vKVTcBfqZETj_Vk1wjcx_ND0ChzvGzAL01CtK5541rCv7lyZXOAQ3qBCnpg5JES_9UNqyijoAyu3EFBMcqa2cCqFCBwJUyQMxetZgOqbnnKt3YLe8ICCcexC83kq9dB45hdrKt-FRYowd8vj5C3rE7bZtPQCLCvqMeTTSsuBza95ZlK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درود یاشارجان
اینجا بندرعباس جایی که تنگسیری تبدیل به کتلت شد , عرازشه شب شام‌غریبان اومدن شمع روشن کردن
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15833" target="_blank">📅 13:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15832">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dc4232c0.mp4?token=iyBid9VzAymSpIzq8Z0gf3evta3l-bnMD-Oe-f-lPKllvvQh5C2SsGghfwXBXVdrzofvsKceYjpe2IsP0ZRUUcY6UAcx-gYQIYqT3nGn7c3iPNs9moH70yMOxESuJ0v0CvEFvOPw8k3eDh79AG-hkG7q65rEwMmDXSBxj6a5PHk8R_KA7jYwla-K5CV7U_e0-I-N8ZSv7g6jgdxFNNCTenUUEMJrxnpiBgzXUgx7wlCipgXRlCGFIsUOsMYX1dyu9wk91FhVEx1jmEEUCOXsRij9U8X_5WpE1-14lN1o-CM_LHRXGTMQPrvIkiJmYM40v1CcgGSMzFQxwj7PgHL2UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dc4232c0.mp4?token=iyBid9VzAymSpIzq8Z0gf3evta3l-bnMD-Oe-f-lPKllvvQh5C2SsGghfwXBXVdrzofvsKceYjpe2IsP0ZRUUcY6UAcx-gYQIYqT3nGn7c3iPNs9moH70yMOxESuJ0v0CvEFvOPw8k3eDh79AG-hkG7q65rEwMmDXSBxj6a5PHk8R_KA7jYwla-K5CV7U_e0-I-N8ZSv7g6jgdxFNNCTenUUEMJrxnpiBgzXUgx7wlCipgXRlCGFIsUOsMYX1dyu9wk91FhVEx1jmEEUCOXsRij9U8X_5WpE1-14lN1o-CM_LHRXGTMQPrvIkiJmYM40v1CcgGSMzFQxwj7PgHL2UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز خوراکی خودش را معرفی نکرده بود که حلوا است یا
💩
. بدم می‌آد ازتون. گشنه‌ها. خجالت می‌کشه آدم اینو استوری کنه. می‌گن سهام برند طلا و جواهرات ونکلیف آرپلز ۵۰٪ ریخت، بعد این ویدیو.
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15832" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15831">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15831" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15830">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/15830" target="_blank">📅 13:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15829">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست (Boost) در کانال‌های تلگرام به‌صورت مستقیم هیچ درآمدی برای مالک کانال ایجاد نمی‌کند و قابل فروش هم نیست. بوست‌ها را کاربران دارای Telegram Premium به کانال می‌دهند تا قابلیت‌هایی مثل استوری کانال، ایموجی‌ها و ری‌اکشن‌های سفارشی و همچنین ارتقای سطح (Level up) کانال فعال شود؛ یعنی بوست بیشتر یک سیستم امتیازدهی و فعال‌سازی امکانات است و نه پول. بنابراین مالک کانال هیچ مبلغی دریافت نمی‌کند و بوست‌ها تبدیل به پول نمی‌شوند، قابل برداشت نیستند. در جمع‌بندی، بوست فقط برای افزایش امکانات و اعتبار کانال است، نه برای درآمد یا فروش</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15829" target="_blank">📅 13:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15828">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c8cc82c5.mp4?token=a40XPE0gNFir3CpmOgvUIftKI2rQXwi4NmrxsUgUplkmrrbb4KmCrC0fJMhWKveKlCBQUrlzVyQxel8brFtE2MAFCpvWC3h14A39QbmyplmtCN3CXpC1nCAbiAup3T_kbJ8Ot4bnUwPpdu7sZh1ewfOlCqogFx9gb6kPHpYVnssvFmEliY7cR7bms39wfZ5xIJnn4tmcXFoUCr4F87IEp7o7AwYDYdws15C8UK36SyNvo7Xz80YaMRdJRnh1quHD_FebcCRbsDDeCYy-VXkeX8MruTt6V4p9IBELZsGXPhqhIp3jrsmmMSsbxRp5tFW5QzLWEGgpIW48egxdjXQtMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c8cc82c5.mp4?token=a40XPE0gNFir3CpmOgvUIftKI2rQXwi4NmrxsUgUplkmrrbb4KmCrC0fJMhWKveKlCBQUrlzVyQxel8brFtE2MAFCpvWC3h14A39QbmyplmtCN3CXpC1nCAbiAup3T_kbJ8Ot4bnUwPpdu7sZh1ewfOlCqogFx9gb6kPHpYVnssvFmEliY7cR7bms39wfZ5xIJnn4tmcXFoUCr4F87IEp7o7AwYDYdws15C8UK36SyNvo7Xz80YaMRdJRnh1quHD_FebcCRbsDDeCYy-VXkeX8MruTt6V4p9IBELZsGXPhqhIp3jrsmmMSsbxRp5tFW5QzLWEGgpIW48egxdjXQtMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش بسیار از مشاهده شدن دود حجیم در تهران
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15828" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15827">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بازداشت یک هکر رژیم در مونته‌نگرو با درخواست اف‌بی‌آی
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
اداره پلیس مونته‌نگرو  امروز در بیانیه‌ای مدعی شد این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15827" target="_blank">📅 12:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15826">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تسنیم:دیشب یک گروه مسلح در نزدیکی مسجد جامع شهر سراوان تیراندازی کردند و از محل متواری شدن
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/15826" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15825">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۷.۸ ریشتر سواحل جنوبی جزیره میندانائو در فیلیپین را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15825" target="_blank">📅 11:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15824">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش اسرائیل در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل اسرائیل نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15824" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15823">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نادرشاه افشار در مبارزه با هوتکی‌ها بود تا اصفهان را از اشغال آنان بیرون آورد، در یکی از روزهای نبرد چشمش به پیرمردی افتاد که با وجود سن بسیار زیاد، شمشیر به دست گرفته بود و با چنان قدرت و مهارتی می‌جنگید که گویی جوانی نیرومند است. گفته می‌شود چندین تن از جنگجویان افغان به دست او کشته شدند و همین موضوع باعث شگفتی نادر شد.
بعد از پیروزی و آزادی اصفهان نادر دستور داد پیرمرد را نزد او بیاورند. وقتی او را آوردند، نادر با تعجب به قامت خمیده و چهره سالخورده‌اش نگاه کرد و گفت: «تو با این سن و سال چنین دلاورانه می‌جنگی و این همه نیرو داری؛ پس چرا وقتی افغان‌ها به ایران حمله کردند، اصفهان را گرفتند، مردم را کشتند و کشور را به این روز انداختند، تو کجا بودی؟ چرا آن زمان نجنگیدی تا کار به اینجا نکشد؟»
پیرمرد بدون آنکه هراسی به خود راه دهد، سرش را بلند کرد و با آرامش پاسخ داد: «
من آن روز هم بودم؛ این تو بودی که نبودی.»
می‌گویند نادر با شنیدن این پاسخ لحظه‌ای سکوت کرد، سر به زیر انداخت و دیگر سخنی نگفت؛ زیرا دریافت منظور پیرمرد این نبود که مردم ایران ناتوان یا ترسو بودند، بلکه می‌خواست بگوید مردم آماده دفاع از سرزمین خود بودند، اما فرمانده‌ای نداشتند که آنان را گرد هم آورد و رهبری کند. با آمدن نادر، همان مردم پراکنده به نیرویی منسجم تبدیل شدند و توانستند اشغالگران را از ایران بیرون برانند
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15823" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15822">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gdzp6moY9auo9LWa4tJ8gfx-3_KxlWYuKwHORnpTNYUAEq27U8xVL8k99Li_QmyB4ai_ZnXLfysEpBuIo5j1FiPiJlKXlDB2AKMivEVNPCP4sTmgWke-9IR-otvz0SiT7mvUONLi0g_GngJCrxOKFfTWZ0mR72qbny0ccfHrrsBrWEYodaYQ0Y_AbFna1TTxYcArYkAjjdTyP3HIr9zxoty5hk82IGbbX_KA29iN8WkdiSx1iuOhGeJPMnoruzB_L5mEH7oxcTkQm9SaVBpAX9faOfZaSvc_6e213AfOPRdLG9uwYrC7AtgBth8wltnxANNdbOjdxBjft15IZRe0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15822" target="_blank">📅 10:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15821">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سیدمحمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس : چرا برای هفته بعد قرار مذاکره گذاشتید؟
مسئولان محترم مذاکرات: مگر نگفتید بندهای ۱،۴،۵،۱۰،۱۱ پیش‌شرط ادامه‌ی مذاکرات است و تا عملی نشود، مذاکرات متوقف می‌شود.
این بندها کامل اجرایی و عملی نشده است.  چرا برای هفته‌ی آینده قرار مذاکراتی گذاشتید؟
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/15821" target="_blank">📅 09:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15820">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آخرین آمار رسمی، حاکی از کشته شدن دست‌کم ۲۳۵ نفر در پی دو زمین‌لرزه شدید در این کشور است. وزارت بهداشت ونزوئلا همچنین از زخمی شدن بیش از چهار هزار شهروند این کشور در دو زمین‌لرزه به بزرگای ۷.۲ و ۷.۵ که شامگاه چهارشنبه رخ دادند، خبر داده است.
سازمان زمین‌شناسی آمریکا هشدار داده است که شمار قربانیان به احتمال زیاد به هزاران نفر خواهد رسید و احتمال زیادی وجود دارد که آمار کشته‌ها از ۱۰ هزار نفر فراتر رود.
@withyashar</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15820" target="_blank">📅 09:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15819">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بیانیهٔ تیم ملی نسبت به احتمال تبلیغات همجنس‌‌بازی در بازی مقابل مصر
فیفا به هر دو تیم شرکت‌کننده اطمینان داده است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این موضوع در داخل ورزشگاه یا به‌عنوان بخشی از برنامه رسمی مسابقه برگزار نخواهد شد.
موضع ایران این است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این پروژه نباید در داخل ورزشگاه یا به عنوان بخشی از فضای مسابقه برگزار شود.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15819" target="_blank">📅 08:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15818">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تحقیقات وال استریت ژورنال نشان می‌دهد: خسارات وارده به پایگاه نیروی دریایی ایالات متحده در بحرین در جریان حملات ایران از اواخر فوریه تا ژوئن بسیار بیشتر از آن چیزی است که گزارش شده است. طبق تحقیقات، ستاد ناوگان پنجم، تأسیسات ارتباطات ماهواره‌ای، انبارها و ساختمان‌های مسکونی آسیب دیده‌اند , که برخی از آنها دیگر قابل استفاده نیستند. تحقیقات هزینه بازسازی را حدود ۴۰۰ میلیون دلار تخمین زده است، اما انتظار می‌رود هزینه کل بسیار بیشتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/15818" target="_blank">📅 08:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15817">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: ما یک بازار جدید داریم که به آن کشور دوست‌داشتنی ایران می‌گویند. جای زیبایی است، آیا کسی دوست دارد به آنجا برود؟ آنها در تامین غذا مشکل دارند و ما قرار است مقداری از پولشان را بگیریم و آن را خرج کنیم و گندم، سویا و ذرت زیادی بخریم و این روند به زودی آغاز خواهد شد. این کار بزرگ خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15817" target="_blank">📅 07:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15816">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=J4gNO44fUlbXzPkU0JaYFp0I26shG3Iv4vgdVJl5rTnbPbJS0ggw9CI1onVqkc5PqzNvUQBUOJJmvqFC1hpy_OvQYin6y5xAo9AdsjhT1FzeRSKbVwliNETy5B9XvLJcaxR53H13oSLe0tfUQDBALk46btqUh9BqMWM-y8cJotNGA3PDBpVXCAQFTsEirDbu-1MKcjdxNQJHPzRLPQ-B8sBwk0owRPIj4N_GRPafuz4y3SM_9lvNluTnDn4us5cvyENgttSIbEmzWZfhEYcA55XjeRszQqcv0fGpyEcEh-dqtXPQZYliSEhLpAPAiRXzDa-R7tdtFc_hkUEJJRENdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=J4gNO44fUlbXzPkU0JaYFp0I26shG3Iv4vgdVJl5rTnbPbJS0ggw9CI1onVqkc5PqzNvUQBUOJJmvqFC1hpy_OvQYin6y5xAo9AdsjhT1FzeRSKbVwliNETy5B9XvLJcaxR53H13oSLe0tfUQDBALk46btqUh9BqMWM-y8cJotNGA3PDBpVXCAQFTsEirDbu-1MKcjdxNQJHPzRLPQ-B8sBwk0owRPIj4N_GRPafuz4y3SM_9lvNluTnDn4us5cvyENgttSIbEmzWZfhEYcA55XjeRszQqcv0fGpyEcEh-dqtXPQZYliSEhLpAPAiRXzDa-R7tdtFc_hkUEJJRENdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسی
🧕🏻
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15816" target="_blank">📅 00:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15815">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبکه المنار : توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/15815" target="_blank">📅 23:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15814">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جنگنده های اسرائیل بر فراز جنوب لبنان به پرواز درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15814" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15813">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/15813" target="_blank">📅 22:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15812">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسرائیل و لبنان، عقب‌نشینی نیروهای اسرائیلی از جنوب لبنان را تکذیب کردند
یک مقام ارشد ارتش اسرائیل گفت که این کشور از منطقه حائل عقب‌نشینی نخواهد کرد. یک مقام نظامی لبنان نیز گفت که تحولات میدانی روزهای اخیر «خلاف عقب‌نشینی را نشان می‌دهد.»
ارتش اسرائیل هم در بیانیه‌ای اعلام کرد که تغییری در محل استقرار نیروهایش در جنوب لبنان ایجاد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/15812" target="_blank">📅 22:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هشدار نهاد مدیریت آبراهه خلیج فارس(PGSA) در‌مورد تبعات
تردد شناورها خارج از مسیر اعلام شده ایران
نهاد مدیریت آبراهه خلیج فارس‏ در پاسخ به استعلام‌های مکرر اعلام میکند:
هرگونه تردد از مسیرهای خارج از چارچوب تعیین‌شده PGSA، مشمول تضمین عبور ایمن نبوده و از پوشش بیمه و مسئولیت‌های مرتبط برخوردار نخواهد بود.
تبعات ناشی از تردد از مسیرهای غیرمجاز، برعهده مالک، بهره‌بردار و فرمانده شناور خواهدبود.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/15811" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15810">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq57-7fOlhigKSRl9-0XkTsel5Ly9ttPN6-KVDUVQPsOb4F9XzSP8RAqX13rtuSLlQJsdRYDr-Bao_e1dmTy3liovr0f0SoJiYEeUVrmbh1k9gchAXrNnmGSXrvTa5o5epIwm4OQ6v4ua_HiZWQIC8MdS7qpgbtByTsDMAFD4oIULYWh7zFcvFJiAVmAKCVknx3JkDuPOZtfgWFt5jr7jt10vQ_WdCkuI2FMrrLoSkXcB9TONfup-DI80BmCZDVq6WLJPCCd55L3N2dM0dQIq-vdgrYTGSYH-ivlNJ6j2ZLBjuqwby77ZugKMiWLS-ULga_KZxW3OEx-Et2IxCgwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتشسوزی منطقه ویژه بوشهر الان
دوران جنگ دوبار زده بودن اینجارو
@withyashar
🚨</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/15810" target="_blank">📅 22:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ورود نیروهای اسرائیل به خاک سوریه
یک گشتی نظامی ارتش اسرائیل با عبور از خط مرزی، به حومه غربی شهرک «الرفید» در ریف جنوبی قنیطره حمله کردند.
نیروهای اسرائیل در جریان این حمله، تعدادی را بازداشت و آن‌ها را مورد بازجویی قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/15809" target="_blank">📅 21:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15808" target="_blank">📅 21:40 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
