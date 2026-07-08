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
<img src="https://cdn4.telesco.pe/file/BCbA99rckAyKz2GUIxK4n71XL3x2mQYFDupAxHeCekMjFIzYziLS5kITo4WSQrRd0aSKY_Y3kr4i-InYzeFCNN-x_mer4qJ1d4_UpcGREWErMNA5-fvghmWC2oKvX0eB0VCeaG7SckV7N_tVi67TvDKaxfXxORHQwpy6E0WxHGdAYSbguh7NKXoLzt5gSXRQHJzHsX0MWAZ-__vEc0Q1JKOlJ9Lg5fBy8NtJnh8KLA8ZltSWHp1NCeWcZ_osCe_dVe4roiB6xSngN7piXZqAXiuU6rs__ILQvjJ8ShjJhcADycnDKp7A2b7pxmy5Ryy63B1jUTXG25h8cq285G7v7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 344K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 13:38:29</div>
<hr>

<div class="tg-post" id="msg-16855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: من از بی بی خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است او به خاطر من به جنگ نپیوست. @withyashar</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/withyashar/16855" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کلاس های تابستانی دانشگاه ازاد مجازی شد
@withyashar</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/withyashar/16854" target="_blank">📅 13:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تابوت خامنه ای به حرم حضرت علی وارد شد
@withyashar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/16853" target="_blank">📅 13:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آموزش پرورش : امتحان نهایی حتی در شرایط جنگی هم برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/withyashar/16852" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی‌ان‌ان به نقل از آژانس ایمنی هوانوردی اروپا:
شرکت‌های هواپیمایی باید از پرواز بر فراز حریم هوایی ایران، عراق و لبنان به دلیل تنش‌ها خودداری کنن
.
@withyashar</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/16851" target="_blank">📅 13:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: اگر ایرانی ها سلاح هسته ای داشتند استفاده می کردند
@withyashar</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/withyashar/16850" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">والا نیوز عبری : ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ
@withyashar</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/16849" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ : یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.
@withyashar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/16848" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ : آن‌ها دیروز شروع کردند به شلیک بمب، در واقع موشک، به سمت کشتی‌ها؛ عربستان سعودی، کویت و چند کشور دیگر. و آن‌ها نمی‌دانند... من فکر نمی‌کنم آن‌ها بدانند چه غلطی دارند می‌کنند، اما آن‌ها آدم‌های بدی هستند، آدم‌های خیلی بد.
اما این‌ها افرادی شرور و بیمار هستند و ما باید سرطان آن‌ها را ریشه‌کن کنیم، سرطان آن‌ها را؛ و می‌دانید با سرطان چه کار می‌کنند؟ باید سرطان را زود قطع کرد و برداشت. و این احساس من است.
@withyashar</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/withyashar/16847" target="_blank">📅 13:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ سیگنال حمله (سلیمانی) را داد آن‌ها همه‌جا می‌روند و مردم را می‌کشند؛ آن‌ها هزاران هزار تن از سربازان ما را کشته‌اند، آن‌ها صدها هزار انسان بی‌گناه را کشته‌اند. آن‌ها سلیمانیِ بمب‌های کنار جاده‌ای را داشتند؛ من در دوره اول (ریاست‌جمهوری‌ام) کار او را…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/16846" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb46c094c1.mp4?token=PdlP53JucdKoaDVxDaV3LhMsUISzaG-Ag7BoTsU2dKkKPy39S8OtEYzxTmSb8_K4_UNTVGjRlhhmgLkKPg6jWgojqNZZ9eYqKVK7CfQAEGjHQiRhhliKsfayeBdsHeKzHekP3GOwvxjrrovmGxthxiUGsXoOX-TuvWVvUyup_kxpfNFJj45EULAujm7CI-NbMdZ4VrPAihz47CUECCAZt0PLBZtWbyUMhAyzY62vxQAT5wX7WkCyhG8R4G-__1WHwP6rOnAsuL5sRCKsQ4ZJOdaTl539PY_N7eucUip8FwkEmNEP7yW4QTtyt6GStdvNx-qJEWiASWTWTmmRdptu1iUrYuM7zQufix9Ar6DQrZBsrhQe1X7_q5EGKFXhCDwgw5q5hY93ZdF0yg0zzRja_Pv3r88WvVLVPQjlcK4iiK9Sj3SWmcGMTfGtNw7a8G9hSiKRIEC4MXwhO89y_UhFlvl7_3aoW_5kJhEaisPE3-GaOe3hETRUNlIOpvaQljWvWRteDhXzvGbjoG1aSrqfmkzaB3f6cNRokPLGcKIUWDPxYvQh_yl5Ua36qyLWOG3mqXyvw3CDYSPGKn9eaeOGxqGx7xugU6t47uQhst3-DryZR_sxa9irPhe5_iFU3A8XGvIlTuffACvrDqvpMWYqjupuSL1rYumIikfLERJWAlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb46c094c1.mp4?token=PdlP53JucdKoaDVxDaV3LhMsUISzaG-Ag7BoTsU2dKkKPy39S8OtEYzxTmSb8_K4_UNTVGjRlhhmgLkKPg6jWgojqNZZ9eYqKVK7CfQAEGjHQiRhhliKsfayeBdsHeKzHekP3GOwvxjrrovmGxthxiUGsXoOX-TuvWVvUyup_kxpfNFJj45EULAujm7CI-NbMdZ4VrPAihz47CUECCAZt0PLBZtWbyUMhAyzY62vxQAT5wX7WkCyhG8R4G-__1WHwP6rOnAsuL5sRCKsQ4ZJOdaTl539PY_N7eucUip8FwkEmNEP7yW4QTtyt6GStdvNx-qJEWiASWTWTmmRdptu1iUrYuM7zQufix9Ar6DQrZBsrhQe1X7_q5EGKFXhCDwgw5q5hY93ZdF0yg0zzRja_Pv3r88WvVLVPQjlcK4iiK9Sj3SWmcGMTfGtNw7a8G9hSiKRIEC4MXwhO89y_UhFlvl7_3aoW_5kJhEaisPE3-GaOe3hETRUNlIOpvaQljWvWRteDhXzvGbjoG1aSrqfmkzaB3f6cNRokPLGcKIUWDPxYvQh_yl5Ua36qyLWOG3mqXyvw3CDYSPGKn9eaeOGxqGx7xugU6t47uQhst3-DryZR_sxa9irPhe5_iFU3A8XGvIlTuffACvrDqvpMWYqjupuSL1rYumIikfLERJWAlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سیگنال حمله (سلیمانی) را داد
آن‌ها همه‌جا می‌روند و مردم را می‌کشند؛ آن‌ها هزاران هزار تن از سربازان ما را کشته‌اند، آن‌ها صدها هزار انسان بی‌گناه را کشته‌اند. آن‌ها سلیمانیِ بمب‌های کنار جاده‌ای را داشتند؛ من در دوره اول (ریاست‌جمهوری‌ام) کار او را ساختم، و این کار بزرگی بود چون فکر می‌کنم اگر او هنوز دوروبرشان بود، آن‌ها احتمالاً خیلی قوی‌تر می‌بودند؛ چون او آدم بدی بود اما یک... او یک نابغه شرور بود، اما یک آدم بد، و او پدر بمب کنار جاده‌ای بود. بمب کنار جاده‌ای بمبی است که وقتی با وسیله نقلیه کوچک خود در حال رانندگی هستید منفجر می‌شود؛ منفجر می‌شود و دیگر پا، دست و صورتی برایتان باقی نمی‌ماند. و آن‌ها هزاران هزار نفر را کشته‌اند، حتی ناوشکن یو‌اس‌اس کول (USS Cole) هم کار آن‌ها بود، اگر آن فاجعه را به یاد داشته باشید.
@withyashar</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/16845" target="_blank">📅 13:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کویت از مورد اصابت قرار گرفتن دو موشک بالستیک و ۱۳ پهپاد در سپیده‌دم خبر داد. @withyashar</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/16844" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اتاق جنگ با یاشار  : امشب ردبول میزنیم
😁
💥
⚔️</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/16843" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اردوغان: ما برای یک عملیات احتمالی پاکسازی مین در تنگه هرمز آماده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/16842" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سنتکام : دیشب ما دور تازه‌ای از حملات تهاجمی علیه ایران را به پایان رساندیم که طی آن با استفاده از مهمات دقیق، بیش از ۸۰ هدف مورد اصابت قرار گرفت. نیروهای آمریکایی سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های راداری ساحلی، توانمندی‌های…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/16841" target="_blank">📅 12:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تتر از ۱۸۰،۰۰۰ تومان عبور کرد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/16840" target="_blank">📅 12:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">@withyashar
تحلیل روز</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/16839" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=NH2xBpATYsobvbsYaRK3y4kb2OTkIsBJ_Rs3L3EziUHPAokU8jpk7SIbStttNP5y0FieeH9bCgbpcivYk3aPdCPyqJMlA93wO-HQnzsg9UPWuta0Ix3Io562MNL1EE4vOzm7R_zcg2HTTubD0vIqiJIZhotnKf7XZWnXbc4PA3Ls2OUxiIUEj7cJl4bDt1JA81aRZaVJ0vOlxYIaq136M6BxEte6Y06ZBYrTVe331r7N48VvNxW_O36EBSlc_GP9R-MntbJykCrGVsdOv9ce8JAOL5bjaAtNEzgxzK7gW6sHm9lwQNZeH6Ef5o9vZf5PLspHW2czyz7D_awDnKeWig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=NH2xBpATYsobvbsYaRK3y4kb2OTkIsBJ_Rs3L3EziUHPAokU8jpk7SIbStttNP5y0FieeH9bCgbpcivYk3aPdCPyqJMlA93wO-HQnzsg9UPWuta0Ix3Io562MNL1EE4vOzm7R_zcg2HTTubD0vIqiJIZhotnKf7XZWnXbc4PA3Ls2OUxiIUEj7cJl4bDt1JA81aRZaVJ0vOlxYIaq136M6BxEte6Y06ZBYrTVe331r7N48VvNxW_O36EBSlc_GP9R-MntbJykCrGVsdOv9ce8JAOL5bjaAtNEzgxzK7gW6sHm9lwQNZeH6Ef5o9vZf5PLspHW2czyz7D_awDnKeWig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/16838" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: من از بی بی خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است او به خاطر من به جنگ نپیوست.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/16837" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دبیرکل ناتو
در مورد نقش اروپا در جنگ ۴۰ روزه
: ۵ هزاربار‌ پرواز برای حمایت از عملیات نظامی علیه ایران از مبدا اروپا انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/16836" target="_blank">📅 12:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کویت از مورد اصابت قرار گرفتن دو موشک بالستیک و ۱۳ پهپاد در سپیده‌دم خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/16835" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جروزالم پست: وزیر جنگ آمریکا، به دنبال حملات علیه ایران، سفر خود به اسرائیل را لغو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/16834" target="_blank">📅 12:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a5af1369.mp4?token=oUos5jxUOrXpDN0AGht9vVTWVKHSawCYoHraEg17DloPRJxUzBYHCEAL__T_0LEB2ytn-BJnYKEWmlZNsIcosjcr6WzmOu0grA4gk5DoKlUHV5XWV-HfhTSMHh_WrBFQ12tnRoTmzRG0lSVcGgN8L7oIez4VlDp0zr132eJwPAo63icEU30yF_9mDo5J5mSdzNruJML2BnLbZKO9p1-ry64uQEXg7AXifhJgeCdGExD5wX-y6wVeIVYz3FBGHBdyBUModW_ksUzeQPvpve0Cb7FzQIQB-2zYGsdQ_3X9xuXhc0dZ-wfQAY5OMj2pDkz0guGXKIw6EwzGmN-4n9_CBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a5af1369.mp4?token=oUos5jxUOrXpDN0AGht9vVTWVKHSawCYoHraEg17DloPRJxUzBYHCEAL__T_0LEB2ytn-BJnYKEWmlZNsIcosjcr6WzmOu0grA4gk5DoKlUHV5XWV-HfhTSMHh_WrBFQ12tnRoTmzRG0lSVcGgN8L7oIez4VlDp0zr132eJwPAo63icEU30yF_9mDo5J5mSdzNruJML2BnLbZKO9p1-ry64uQEXg7AXifhJgeCdGExD5wX-y6wVeIVYz3FBGHBdyBUModW_ksUzeQPvpve0Cb7FzQIQB-2zYGsdQ_3X9xuXhc0dZ-wfQAY5OMj2pDkz0guGXKIw6EwzGmN-4n9_CBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونا توی اعتراضات دی ماه ۵۴ هزار نفر از مردم بی گناه رو کشتن‌.
مردم دست خالی بودن و اونا با مسلسل بهشون شلیک میکردن.
از نظر من مذاکرات و توافق با ایران تموم شد.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16833" target="_blank">📅 12:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با باشار :کاملا مشخصه ناتو و ترامپ برای حمله به ایران به توافق رسیدند ، و کار تمام است !!!
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/16832" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14e22ad6d.mp4?token=aq4un4ZBngaiu-FhgyN7Yhrq1V98OFCEhockbI4mYOHwTMa_G2M81XV1DxLVvvGEYoK8Rq1sCP89ieaFXUE1pP8sbuxKacitXHNUT4xwlI5E8CVrXBPlST1tyvnr3C_2KgtckNheVg9-q2rvlQzuong9Tx-qB3T40YU2fNklEKDy1NthImt3d5TWhyx3FyFRuVLHIykiejLUbv_15hoceELJKyKBppM3xqXRu-dGYi-RrUuFfH7XxFXdwm0Wc4x7a4poXXf2SmEBy6QKnPH8R3BC9Mv8VnrxCDcM8KZd_eVAv7IMZKmHyBsoq4yFubEgQKQ7bkVzkBQaTBhreJ2G1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14e22ad6d.mp4?token=aq4un4ZBngaiu-FhgyN7Yhrq1V98OFCEhockbI4mYOHwTMa_G2M81XV1DxLVvvGEYoK8Rq1sCP89ieaFXUE1pP8sbuxKacitXHNUT4xwlI5E8CVrXBPlST1tyvnr3C_2KgtckNheVg9-q2rvlQzuong9Tx-qB3T40YU2fNklEKDy1NthImt3d5TWhyx3FyFRuVLHIykiejLUbv_15hoceELJKyKBppM3xqXRu-dGYi-RrUuFfH7XxFXdwm0Wc4x7a4poXXf2SmEBy6QKnPH8R3BC9Mv8VnrxCDcM8KZd_eVAv7IMZKmHyBsoq4yFubEgQKQ7bkVzkBQaTBhreJ2G1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: مقام‌های ایران بی‌کفایت هستند؛ اگر کاربلد بودند، ۴۷ سال پیش توافق می‌کردند/وی در ادامه با استفاده از ادبیاتی تهدیدآمیز گفت: «باید سرطان را زود از ریشه درآورد. نظر من این است.»
در پایان این اظهارات جنجالی، ترامپ به صراحت اعلام کرد که مسیر دیپلماسی با ایران پایان یافته است: «به نظر من، یادداشت تفاهم با ایران دیگر مُرده است.»
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16831" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: دیگر نمی‌خواهم با ایرانی ها مذاکره کنم @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/16830" target="_blank">📅 12:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: دیگر نمی‌خواهم با ایرانی ها مذاکره کنم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/16829" target="_blank">📅 12:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: بعضیا می‌پرسن چرا مردم ایران حکومت رو سرنگون نمی‌کنن؟ خب معلومه، چون خیلی‌هاشون کشته شدند @withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16828" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا:
مبدا هرگونه پشتیبانی از ارتش متجاوز آمریکا برای تجاوز  به حاکمیت و سرزمین ایران اسلامی، هدف مشروع نیروهای مسلح خواهد بود.
@withyashar
اتاق جنگ با یاشار : مبدا هر پشتیبانی از جمهوری اسلامی هم برای ما مردم هدف مشروع است !</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16827" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16826">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: بعضیا می‌پرسن چرا مردم ایران حکومت رو سرنگون نمی‌کنن؟ خب معلومه، چون خیلی‌هاشون کشته شدند
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16826" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: مقامات جمهوری اسلامی آشغال هستن , هیچکس آن قاتل‌ها را دوست ندارد
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما اصلاً درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/16825" target="_blank">📅 11:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار : لطفا از درس و امتحان غافل نشید انقدر در‌این مورد دایرکت ندید و دنبال در رفتن نباشید ! فک کنین ۱۸-۱۹ دی هست برای خودتون بجنگید و درستون رو بخونید ! اگه برگزار شد شما آماده هستید اکه نشد شما علمتون بیشتر شده و برای بعدی آماده هستید! اگه منتظر حمله بزرگین نه فعلا نمیشه ! پس یه تکون بده درستم بخون ! مخصوصا زبانتو خوب کن کلی پول در‌ میاری ! دیگه دایرکت امتحان و درس نخوندن نبینما‌!!!!!!</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/16824" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ : سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/16823" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ : اسپانیا یک هدف از دست رفته و شریک بدی در ناتو است. من روابط تجاری خود را با آنها قطع خواهم کرد و به دیدارشان نخواهم رفت.
ما نیازی به رابطه تجاری با اسپانیا نداریم
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/16822" target="_blank">📅 11:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش بومی از اسکله صیادی شهر کوهستک شهرستان سیریک : به گفته تعدادی از ماهی‌گیران حاضر در محل، این اسکله پیش از حمله آمریکا تخلیه شده بود و هنگام اصابت‌ها کسی در آنجا حضور نداشت.
گزارش ها نشان میدهد چند سیاد ترکش خوردند و زخمی شدند
‌
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/16821" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو به نیوز مکس: خطر ایران همچنان پابرجا است و تهران همچنان قادر به بازسازی برنامه هسته‌ای خود است
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/16820" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست یابد؛ آنها دیوانه هستند و هزاران نفر را کشته‌اند.
ما وقت زیادی را با ایران تلف کردیم و باید کار خودمان را انجام دهیم
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/16819" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: ایران سران آمریکا از جمله من را مورد هدف قرار دادند
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/16818" target="_blank">📅 11:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دونالد ترامپ: شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی هستند. ایران به کشتی‌ها موشک شلیک کرد، و به همین دلیل، ایالات متحده واکنش نشان داد
فکر نمی‌کنم ایران بداند که چه کاری در حال انجام است
ایرانی‌ها هزاران نفر را کشته‌اند و آن‌ها یک گروه جنایتکار هستند
آنها دیوانه‌اند
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/16817" target="_blank">📅 11:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روابط عمومی سپاه : پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی در منطقه صورت گرفت
(پیشتر سنتکام گفته بود ۸۰ هدف رو زدیم پس‌اینام ۵ تا گزاشتن روش کردن ۸۵ بگن ما بیشتر زدیم ، دقیقا همینه ها !!!)
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/16816" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7690f1e966.mp4?token=qaYwIzYqEMK1vZAHR5D7Vj7jHKQ_n6dRe8KxNGVKw9GhVcKztCjkm9U2cUjbjUgE8nufcyzpvPCeCTimgOmGLtlCtgLUt8ZZDDqUGudpViQh33QeAI2m65AEJuBnwi3YOBO7yP7uuSF3h7qOYJCfTS3pFbl6Lf_eoNUMgoywt1jnjdqr7bhmXQdUZi6q381nlNIR5CH2uQY2BWrCIFBpdp8n9iA3Gv0AZfj5KDt3a_foQw1qWcf6qI6c13tqBHU2n9HZ-ibly2gn5gJHkatcJ2oZVG6pg7xeOc_TNWB13l_ROAU1HfY0j1-pEotXZSV00MDabhlCqHoKevt2PRWZ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7690f1e966.mp4?token=qaYwIzYqEMK1vZAHR5D7Vj7jHKQ_n6dRe8KxNGVKw9GhVcKztCjkm9U2cUjbjUgE8nufcyzpvPCeCTimgOmGLtlCtgLUt8ZZDDqUGudpViQh33QeAI2m65AEJuBnwi3YOBO7yP7uuSF3h7qOYJCfTS3pFbl6Lf_eoNUMgoywt1jnjdqr7bhmXQdUZi6q381nlNIR5CH2uQY2BWrCIFBpdp8n9iA3Gv0AZfj5KDt3a_foQw1qWcf6qI6c13tqBHU2n9HZ-ibly2gn5gJHkatcJ2oZVG6pg7xeOc_TNWB13l_ROAU1HfY0j1-pEotXZSV00MDabhlCqHoKevt2PRWZ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود در بوشهر  دقایقی قبل
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/16815" target="_blank">📅 11:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جاسم البدیوی، دبیرکل شورای همکاری خلیج فارس، اعلام کرد حملات ایران به کویت و بحرین در ادامه رویکرد تهران برای تضعیف تلاش‌ها در مسیر حل‌وفصل بحران جاری انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/16814" target="_blank">📅 11:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">داریم به این لحظه نزدیک میشیم. گفتم از الان داشته باشین، سیو کنین، چون اون موقع ممکنه اینترنتتون قطع باشه و نفهمین چی شده. @withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/16813" target="_blank">📅 11:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارسالی : نیرو دریایی و پایگاه هوایی رو زدن پشت خونمون تو بوشهر
عکس دارم ولی لوکیشن خونمون مشخصه توش
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/16812" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فارس  : ۲ مقر نظامی در بوشهر مورد حمله دشمن قرار گرفت معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند. @withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/16811" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فارس  : ۲ مقر نظامی در بوشهر مورد حمله دشمن قرار گرفت
معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/16810" target="_blank">📅 10:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بوشهر سمت باند فرودگاه رو زدن
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16809" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دو ‌انفجار دیگر بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16808" target="_blank">📅 10:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16807">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش انفجار بوشهر الان
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16807" target="_blank">📅 10:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16806">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQbaZTFNwwswBkFbH1QKIn5NRY-Kt3IyP90pvtmGagRt-wkN72IyA89tlYxgT3eWmT-XYos78KJDEOqG0U3offrfh5ymhkaGclW2mPdj78dp6UebuG1UzfIPD03CtrZHybhTM6qqDj5U10EbeYLUuAOUnBlJnh5NEuCEYZFuz3gl01Mfy22jcKjTeBr-4mk5N3FcwedcD9oPreQyuOKIj-K-t3PAOpZivbOJyYZAPr5A2JAgOLNYRiz29QJMfjPe-0Y56lLKYoJcXIK4n_eXW1BvFJWtRBB18ESokwAfTBgBSSAwkgdyheXzdRWReBbvYSiq9dJQChfzWtkjpzdRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه درباره حملات آمریکا و نقض يادداشت تفاهم
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16806" target="_blank">📅 10:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16805">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تلویزیون بحرین: همکنون سامانه‌های پدافند هوایی بحرین، اهداف ایرانی را در آسمان این کشور شناسایی و منهدم کردند.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16805" target="_blank">📅 10:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16804">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086c3e88a0.mp4?token=LrIx6fFto6JzXvg6UzYnoupqTF5i16BOWzVuaHfX9TkwfWXaj-OJ7gqwkZq1pKVrCpt-6Gm0ClV3YoY90j5PfJVXMswKKyyY_8JQFBFlx6ebRiCeWkWlcIOolYilgZyDLAoVT29qGvXgCzFTzUEBS_f9Dn832Syq9guqLSrrzsVJhWzNuR5Wv_9hag3Atp5-xiwX8Izz2owx6c3P5YrS3ZJxxsEQs2TLxhAq5LHzdG6eDy6RP1Ko4WN_Po51h-WpePeuHSS-0L0DMUM0Sv782yrJ1ArQyd_zTHAtHBmxtDmIgUNIlUU9HGQNHVWLQ-0SH2O_l1axcpDYjgDpLhD_PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086c3e88a0.mp4?token=LrIx6fFto6JzXvg6UzYnoupqTF5i16BOWzVuaHfX9TkwfWXaj-OJ7gqwkZq1pKVrCpt-6Gm0ClV3YoY90j5PfJVXMswKKyyY_8JQFBFlx6ebRiCeWkWlcIOolYilgZyDLAoVT29qGvXgCzFTzUEBS_f9Dn832Syq9guqLSrrzsVJhWzNuR5Wv_9hag3Atp5-xiwX8Izz2owx6c3P5YrS3ZJxxsEQs2TLxhAq5LHzdG6eDy6RP1Ko4WN_Po51h-WpePeuHSS-0L0DMUM0Sv782yrJ1ArQyd_zTHAtHBmxtDmIgUNIlUU9HGQNHVWLQ-0SH2O_l1axcpDYjgDpLhD_PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : دیشب ما دور تازه‌ای از حملات تهاجمی علیه ایران را به پایان رساندیم که طی آن با استفاده از مهمات دقیق، بیش از ۸۰ هدف مورد اصابت قرار گرفت.
نیروهای آمریکایی سامانه‌های پدافند هوایی ایران، شبکه‌های فرماندهی و کنترل، سایت‌های راداری ساحلی، توانمندی‌های موشکی ضدکشتی و همچنین بیش از ۶۰ فروند شناور کوچک متعلق به سپاه را در داخل و اطراف تنگه هدف قرار دادند تا توانایی ایران برای ادامه حمله به تجارت بین‌المللی در این گذرگاه حیاتی را تضعیف کنند.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16804" target="_blank">📅 10:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16803">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آلارم حمله موشکی در بحرین فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16803" target="_blank">📅 05:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16802">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منابع خبری از شنیده شدن صدای انفجار در بحرین خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16802" target="_blank">📅 05:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16801">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8524de4243.mp4?token=ilA-RliLRa6eXZWDKnbGMUBXsVGtBJ_bTifLkbG1toPV-nm5eBv46cxdfMks3ZFxsK3kaJ47rTKQn3WbsWuMvN5DyvldcCbRdZGiiDU-gA-4_pdv7GdEGkIvWjdHLjxLDT7lkKhkChiB46UWmJoXv8fof9JzzaRlkhEvETge2pysWXgGa1R4bUuG-qv6Xhj_Z3BLdvffBzyuTqt9Q25J5z89Z5kz7bQQL61obEl7AZJC5-YnmPG-yddf1LkRe47XpFER7veTuHV2kN6toV2CU99ZAm7x2IX6k5Lp_P7zzdhIOqSsVydGwB863sxpQYFoOjPRp6aysgcjXYCy5SEe_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8524de4243.mp4?token=ilA-RliLRa6eXZWDKnbGMUBXsVGtBJ_bTifLkbG1toPV-nm5eBv46cxdfMks3ZFxsK3kaJ47rTKQn3WbsWuMvN5DyvldcCbRdZGiiDU-gA-4_pdv7GdEGkIvWjdHLjxLDT7lkKhkChiB46UWmJoXv8fof9JzzaRlkhEvETge2pysWXgGa1R4bUuG-qv6Xhj_Z3BLdvffBzyuTqt9Q25J5z89Z5kz7bQQL61obEl7AZJC5-YnmPG-yddf1LkRe47XpFER7veTuHV2kN6toV2CU99ZAm7x2IX6k5Lp_P7zzdhIOqSsVydGwB863sxpQYFoOjPRp6aysgcjXYCy5SEe_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله به اسکله ی صیادی بندرکوهستک
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16801" target="_blank">📅 04:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16800">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ffa8fddf.mp4?token=qSxSzo5soAD1Rjga20VW8sn9rNPsE-X4fcJw8sHDnlskp4tqml-pT9kGUjq4QJAKrTPhNNlJdUEk8AFPgK8x9FPUzKiknEkn_uO1NmUHVAGACV-lvkciq8NBVYQRhA9UibzmBJFby9uVUe8d5bI2ZL-LYOt5aUX6FlLmh3Vx5kdNOeXkF4H12xtz91hwlKqnXQ9GQzqCT6V_LihbLYpuJQWFbGDObDCYKeA00Lg6QcteMCXDJ3QrriJ7kySP9fdnHPakRrQH8Pnriu5nB8aNelSTcwVlPP-ZK5cE1lUHU4avZIJL_RsreUpd9_4Q81h4C97DTxUu8ENdIf3O851R5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ffa8fddf.mp4?token=qSxSzo5soAD1Rjga20VW8sn9rNPsE-X4fcJw8sHDnlskp4tqml-pT9kGUjq4QJAKrTPhNNlJdUEk8AFPgK8x9FPUzKiknEkn_uO1NmUHVAGACV-lvkciq8NBVYQRhA9UibzmBJFby9uVUe8d5bI2ZL-LYOt5aUX6FlLmh3Vx5kdNOeXkF4H12xtz91hwlKqnXQ9GQzqCT6V_LihbLYpuJQWFbGDObDCYKeA00Lg6QcteMCXDJ3QrriJ7kySP9fdnHPakRrQH8Pnriu5nB8aNelSTcwVlPP-ZK5cE1lUHU4avZIJL_RsreUpd9_4Q81h4C97DTxUu8ENdIf3O851R5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک بالستیک الان بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16800" target="_blank">📅 04:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16799">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3d8e2a2.mp4?token=BfB0Bk5fXAs-UOcFDjhgcl7NeWf6OMfOA4QF26mAjwnULKzSR3GFg7OMJTscVJO8CE8K7j-rdllD79ZClwR_eopis-o1wdft8-TZHoJ7pJ-8Z04ATF8oMWp5_lAu5ygeRu-8Xjete2UmpZpBxCL0sln3793U5QUkRRoG4vwZMTjdtZarnsDqprPu3DPeD_zSLvLlcaeJGUvFuIss_HKmRDtWD-A8xEznBFqR37dAPsFSnD29sjVwTjplfPwRCO-9jAc4GP82c57ML9KrfCU3FR0azgdVDnrQBfJ2njVV4XZaTr00G1EH-Pg4xTReCl9lRAK1XpgF2oM4ijjHuNGvbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3d8e2a2.mp4?token=BfB0Bk5fXAs-UOcFDjhgcl7NeWf6OMfOA4QF26mAjwnULKzSR3GFg7OMJTscVJO8CE8K7j-rdllD79ZClwR_eopis-o1wdft8-TZHoJ7pJ-8Z04ATF8oMWp5_lAu5ygeRu-8Xjete2UmpZpBxCL0sln3793U5QUkRRoG4vwZMTjdtZarnsDqprPu3DPeD_zSLvLlcaeJGUvFuIss_HKmRDtWD-A8xEznBFqR37dAPsFSnD29sjVwTjplfPwRCO-9jAc4GP82c57ML9KrfCU3FR0azgdVDnrQBfJ2njVV4XZaTr00G1EH-Pg4xTReCl9lRAK1XpgF2oM4ijjHuNGvbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شلیک موشک از خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16799" target="_blank">📅 04:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16798">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴄᴀʟʟ ᴍᴇ Kasra 🎙</strong></div>
<div class="tg-text">بندر امام رفتم سیگار بکشم زدن
😂
😂
😂</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16798" target="_blank">📅 04:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16797">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هم اکنون پرتاب موشک بالستیک از تبریز
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16797" target="_blank">📅 04:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16796">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عبور جنگنده‌ها از آسمان شهر بوشهر همین الان
@withyashat</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16796" target="_blank">📅 04:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16795">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خوزستان بندر امام همین الان زدن
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16795" target="_blank">📅 04:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16794">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eb15d06f.mp4?token=JoPHyxllhp55te31jC13BMt3Qn2ng30n5WzPYDjeItZfeJM_ttMcoHgYNYldx7ifFwgwi6D10-Kapl5DBkq_hYGZNWxF91ApKRowoa6IbXKHVtqCpwyR_YPA66Yh1F_FDNtq6nD-4_vB8_RMRn3yTuxkoAl3sUQ5PM12aGs-cxron4ovG8LLYoOOTUN8cagOwj20rEqvLL7Ea36kL287BuDDi0tOn4_6ZtfvpJEnGBx2AmKahRp15D8dUG342RI3v7x9l4zGRYApqacGYNLomuxNhOrOZXu5ExRLvM324tGy-tl-PWfbMAme-et4GepqhGXuooQ5hnJ7TdxGkhRoeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eb15d06f.mp4?token=JoPHyxllhp55te31jC13BMt3Qn2ng30n5WzPYDjeItZfeJM_ttMcoHgYNYldx7ifFwgwi6D10-Kapl5DBkq_hYGZNWxF91ApKRowoa6IbXKHVtqCpwyR_YPA66Yh1F_FDNtq6nD-4_vB8_RMRn3yTuxkoAl3sUQ5PM12aGs-cxron4ovG8LLYoOOTUN8cagOwj20rEqvLL7Ea36kL287BuDDi0tOn4_6ZtfvpJEnGBx2AmKahRp15D8dUG342RI3v7x9l4zGRYApqacGYNLomuxNhOrOZXu5ExRLvM324tGy-tl-PWfbMAme-et4GepqhGXuooQ5hnJ7TdxGkhRoeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوهستک سیریک الان زخمی هم داشته
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16794" target="_blank">📅 04:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16793">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3052fe68.mp4?token=Qf1Pr83j_xoiSQcBpsfNMxTbAj_p5jy4aXhwMB8IyIROXXaOIOX_JHTh05HGMR-85jtU-7QmOdZ-yRYkSgPZRAVO8j8Mg2hTyrTXcXmw59l9Ko1N3w9HZAX8as9fxapvyfpB54D8fFRLx9GiYuS6s7IjP6r75E_G21oa-HOATSN4O9IKceQgYOrJPBrXNImCUwT17EsJt-XV6Eu2Xfl21PM2IAbBJq8_Cv9ObPdbH0FPtw1vprLH5f8_zEiQmMSb1xnOiicA36BDJU5kLflrZxNPq7K_mJg00mzHe1bVJnqs5bjJ7tdOXX_KGl8rlVY6c2wAjxTumk_LEzT50xVP3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3052fe68.mp4?token=Qf1Pr83j_xoiSQcBpsfNMxTbAj_p5jy4aXhwMB8IyIROXXaOIOX_JHTh05HGMR-85jtU-7QmOdZ-yRYkSgPZRAVO8j8Mg2hTyrTXcXmw59l9Ko1N3w9HZAX8as9fxapvyfpB54D8fFRLx9GiYuS6s7IjP6r75E_G21oa-HOATSN4O9IKceQgYOrJPBrXNImCUwT17EsJt-XV6Eu2Xfl21PM2IAbBJq8_Cv9ObPdbH0FPtw1vprLH5f8_zEiQmMSb1xnOiicA36BDJU5kLflrZxNPq7K_mJg00mzHe1bVJnqs5bjJ7tdOXX_KGl8rlVY6c2wAjxTumk_LEzT50xVP3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله کوهستک ، سیریک الان
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16793" target="_blank">📅 04:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16792">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD5elMlr5dR_9rpqLqWnjCIYLzOBd4yqtNWsjR_cvNV9OgxQamwdDbQMaBGCzcsE_lnenzX3hTUhKkR6oz7bVtV_RAYRI0LvRKYErGG9wzqiorOzyO8AUeADcG6clNlS5X0FFNDcxz1jgKlxUmUC4WEMQiogphGqiBr880BX5JK1VUVQnVxLoRaL5WHyRAI8QYnsDrx5eDiVLWqJV6sswTjNX82JKhbukICxNc4-unv9jIgodOjX8--14zWK0hzjCSFjtn0tHmbZkyEF_2JcvvItXrNbY-pV0BE5n6AgnuGzz9hzCcoHiDxYpo81MxyXzn4hdRyH7PQ0jCrPbS1OWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله کوهستک
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16792" target="_blank">📅 04:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16791">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گویا از بندر عباس پهپاد گازی ‌ول دادن ، صدای پهپاد شاهد شنیده میشه @withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16791" target="_blank">📅 04:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16790">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شلیک موشک از سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16790" target="_blank">📅 04:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16789">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسمیت، خبرنگار ارشد نیویورک تایمز :
یه مقام نظامی آمریکا گفته؛ حملات هوایی علیه ایران فعلاً ادامه داره و قراره تا یه مدتی ادامه پیدا کنه، تمرکز حملات هم روی چندین هدف نظامی ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16789" target="_blank">📅 04:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16788">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گویا از بندر عباس پهپاد گازی ‌ول دادن ، صدای پهپاد شاهد شنیده میشه
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16788" target="_blank">📅 04:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16787">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسکله کوهستک و پایگاه موشکی کرپان زدن در‌غرب سیریک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16787" target="_blank">📅 04:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16786">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شلیک موشک از سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16786" target="_blank">📅 03:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16785">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قشم و زدن باز الان
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16785" target="_blank">📅 03:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16784">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دو انفجار در خورموج بوشهر شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16784" target="_blank">📅 03:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16783">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پزشکیان بعد از شنیدن خبر حمله، سریع شال و کلاه کرد و فلنگ رو بست تا مجبور نشه با اتوبوس برگرده تهران. هواپیمای مراج وی هم اکنون وارد حریم هوایی ایران شد. @withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16783" target="_blank">📅 03:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16782">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بوشهر انفجار سمت بندر دیر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16782" target="_blank">📅 03:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16781">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش صدای انفجار بلندی از سمت خارگ ارسالی از بندر گناوه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16781" target="_blank">📅 03:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16780">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجار در قشم
@withyashat
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16780" target="_blank">📅 03:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16779">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">موج جدید حملات آمریکا شروع شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16779" target="_blank">📅 03:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16778">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش انفجار بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16778" target="_blank">📅 03:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16777">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">من دارم توهم میزنم یا بازم صدا میاد؟</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16777" target="_blank">📅 03:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16776">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommojijen</strong></div>
<div class="tg-text">من دارم توهم میزنم یا بازم صدا میاد؟</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16776" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16775">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سه تا انفجار دیگه بندرعباس
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16775" target="_blank">📅 03:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVOOndL0GVFG46KGdiwi3-5ilHGUsRbWQQoTeBRZglA2iK-q4ml2oZP3mTXLteRbLgz00raUx8Ib1jxB3csMmKjHD5BWx1fUNw4At_DL1m84euxB9Oqydn-guoru50XvdamTBKec13YTXo-2ATqPspeh4bu-DRi0Pbj9xqSPEpxkoWCBZUcuUiaQzHkCIJ6QGX5-cr01cO8UYQEe-K1O51TIVDRapw3hlmq5HfefHJ5v9BNeN7NypAK4zSC7-Yr3qAj7pnyTzPzChfhNNuGMrsyNYsZuZDp-Ax3Se2F0c8pWXptbLG4vBcPAGdaNg5qMEp_XQRjMbJl_K4_NrZYVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه انفجار بندر شهید حقانی @withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16774" target="_blank">📅 03:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیکلاس کریستوف ستون‌نویس نیویورک‌تایمز: به نظر می‌رسد جنگ ترامپ با ایران دوباره در حال ازسرگیری است
علاوه بر حملات هوایی، آمریکا لغو تحریم‌های نفتی علیه ایران را نیز پس گرفته است. این موضوع صرفاً یک نوسان یا اتفاق گذرا نیست، اما دست‌کم برای من هنوز مشخص نیست که آیا ما به سمت یک جنگ تمام‌عیار بازمی‌گردیم یا وارد سایه‌ای تیره‌تر از منطقه خاکستریِ میان جنگ و صلح خواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16773" target="_blank">📅 03:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">لحظه سقوط هواپیما باری پاکستان @withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16772" target="_blank">📅 03:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed44ca638.mp4?token=i09U_FIV-2zOa9AI0XyxKZGCFBOtX8d_wDmIEToBHZ2Lg649NSDciFkHl6DjSdPAfx36Wf5DFGkC49CPhDJ5QC37tjO16MmWpNTT_9ln06P2zQHWH93ZVI7UfapnXStsbEnNyC1175kLw40tagpkz9dO3bztZ9JP1I4z6gKjH5LMA9KDptooy7J-_p3Om7RgEDegjd4FwvcAwihuRSdVb1FHquTWoaTICyvoDtotbZ52VKPVQTzEliOEZC2CS3rRQ_PD8-aMMGYPvceoK0ajOSsyDek1pH8XRnBPSZZZc2dtKojIW0BMDWBYRL3cY-6CmnCkdPqyFzZVPkNLRTjn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed44ca638.mp4?token=i09U_FIV-2zOa9AI0XyxKZGCFBOtX8d_wDmIEToBHZ2Lg649NSDciFkHl6DjSdPAfx36Wf5DFGkC49CPhDJ5QC37tjO16MmWpNTT_9ln06P2zQHWH93ZVI7UfapnXStsbEnNyC1175kLw40tagpkz9dO3bztZ9JP1I4z6gKjH5LMA9KDptooy7J-_p3Om7RgEDegjd4FwvcAwihuRSdVb1FHquTWoaTICyvoDtotbZ52VKPVQTzEliOEZC2CS3rRQ_PD8-aMMGYPvceoK0ajOSsyDek1pH8XRnBPSZZZc2dtKojIW0BMDWBYRL3cY-6CmnCkdPqyFzZVPkNLRTjn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این این این تحلیل ممباقر‌ الان میچسبه
@withyashar
🤣
✌🏾</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16770" target="_blank">📅 03:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
طی ساعات آتی احتمال شعله‌ور شون جنگ بزرگ وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16769" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16768" target="_blank">📅 02:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سی‌ان‌ان: وزیر جنگ آمریکا روز چهارشنبه به اسرائیل سفر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16767" target="_blank">📅 02:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMf78tnfnByV_QB4n5oL4ediMntVuds8LjmqKjp7Xt-t_dRJonFM_IMTsv5rVLTNS6Ik4fcz8eOmHbdp6VxOwxIrDX4C9R7JTRnoSOdTbp4GG9nr9ZwsrJdbpOSJNDYdHR2gcF5nmJo9crITEgmbErjDmOy4u2tq9x3f17ogOnH6AGuzVxob39p9EGLvUtGAbI32Jb_mfWWfoWArGsBhdbL4uZ5L3vYAdNH8qe2MqFzW2w3ZOdh0D-nIK4SYJNGui7qEkSpVqkmvh1tGMfFkIkpOxx8CEcwCE4f42BmPyhFY8De3bXer5CiyfcVF6bLiqyf1GPzzGR6RMRq5HAKMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این صحنه هم باید تو تاریخ ثبت بشه ! کالکشن تمام هواپیما های آمریکا یکجا
🤣
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16766" target="_blank">📅 02:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiSOakPv4IOVXo9_wmLoEDIpn3m4bZE0-axdEfxkr8SvHH4K--siNpvYamX18JWSoRh0qge_xYrd3LhE2fnPJl0gKVaQ-0IolagAmkwJAeb-QmdFHf-VJnTSGJL-sLybULZCd2HDihdV13-A3DftwvLo83ghUlD9qykP56jSVQVyMcKA0BwvDBEKDzcxSiY_27BbwWnm4nqQGZhTi7zkHdi5qfXgt8JLU0WnObvkHKvhCcqxlRM43qSkwlzhKp9zhAHiEKb5xrO7vuVsOBQlVXzr7q5zrxMo2fjHzdT4Y_3xGEWbq3ymDk7_mIAKhaYIwERmOsTickrB5FvZwRZYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان بعد از شنیدن خبر حمله، سریع شال و کلاه کرد و فلنگ رو بست تا مجبور نشه با اتوبوس برگرده تهران. هواپیمای مراج وی هم اکنون وارد حریم هوایی ایران شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16765" target="_blank">📅 02:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتاق جنگ با یاشار : ایران و آمریکا رفتن فینال لیگ خلیج فارس برای تصاحب تنگه طلایی
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16764" target="_blank">📅 02:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قشم ، حاوی الفاظ رکیک
🔞
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16763" target="_blank">📅 02:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینترنتها به شدت ضعیف شده و ممکنه قطع بشه. حتما اگر پیج اینستاگرام رو فالو ندارید، فالو کنید و چنل تلگرام هم داشته باشید تا من رو گم نکنید به دوستاتونم بگین این تنها کمک شماست
🙌🏾
🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16762" target="_blank">📅 02:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-v3g-7S25NkQVpANUpBkYSFIcASJK8yhWZhzluRSGuGc-PMgjtDSLN40Ey5hlSNSns2chaUbiwQRstfWesJG7ZzfVeeS_-iLnmVwozbi63J_xWuRAgL95XZ0YlT50obhQp0r0nMuHbJJhGUpe6usTMdhfZpwWfQR0M1-M0JX6h-s8ufaLvkIQ0oUbAi--QanNbI4Lx-25DOCeXcmacNm0xhvTfY5ljGebfwIaPYl_lhvXGw8bughzRGxsvu16AvRMIUJBlTAIyEf4Woemk1FBp32XhqC_xJwIEDP-PbZwpxcBui7ows9UmOyfu0lKb5-q1kLRvwPTLN3rQlaOm88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دو انفجار دیگر در بندرعباس شنیده شد @withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16761" target="_blank">📅 02:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هم اکنون دو انفجار دیگر در بندرعباس شنیده شد
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16760" target="_blank">📅 02:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسرائیل قشنگ داره لبنان رو می‌کوبه تا جمهوری اسلامی جواب بده، اونم بیاد ملحق شه
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16759" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوباره از اصفهان جنگنده بلند شد
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16758" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الان وقت مسخره بازی نیست !</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16757" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری‌ های رژیم : چیزی‌نیست بازار ماهی فروش ها و چنتا کشتی ماهیگیری رو زدن
@withyashar
😳
🤣</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16756" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منابع غربی : حضور ترامپ در ترکیه خطری نخواهد داشت زیرا آنها متقابلا میدانند مراسم تشییع  خامنه‌ای به حاشیه و اختلال کشیده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16755" target="_blank">📅 02:10 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
