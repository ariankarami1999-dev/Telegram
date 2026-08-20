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
<img src="https://cdn4.telesco.pe/file/fwq46h0VeHrL8_x_y1DI0ieVKXolWkSxLm1xsdHYQc4D49juBmat-ANbNyjnVjy-l9RRx1dNASKiwvPfa7fLKUKNx3QSvhsnuUvLt_jU12X8OICyKal2bt296UlyqhEKika-GqWZ8VP-c9JzZ-Lcb420nV9tf-AEm_dLRjguCs08phwr2vK68L4hOaOVyU85J-YkuBW0VDy-dKHyFDJqV_UUeqjmyrt2NVVfN3hWc8ZnOvU0235aUAVp_Jq5JWJC6gPPEptq-oBA_OMAfsu6cjskybgwipLPvQqgm2sO92bWhnopjfTVnWdZrb8eoTKJfZMbqbBBQYc4JigPo9O7lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو با محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.94K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 19:26:16</div>
<hr>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/mohsentavoosiseo/911" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/mohsentavoosiseo/910" target="_blank">📅 14:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/mohsentavoosiseo/909" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 846 · <a href="https://t.me/mohsentavoosiseo/908" target="_blank">📅 13:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خطاب به همه کسانی که خیلی حرفه ای و باهوش هستند.
خطاب به کسانی که از اینکه یک سری بی سواد یا کم سواد حرف اشتباه میزنن، ناراحتن.
خطاب به همه با سواد ها!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/mohsentavoosiseo/907" target="_blank">📅 13:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه اشتباه بزرگ کسانی که تازه مهاجرت کردند یا تازه درگیر پروژه های غیر فارسی شدند یا حتی مدت زیادی گذشته اصلا،
❗️
اینه که فکر میکنن جهان یا بین الملل یا "خارج"! یا کشورهای دیگه، همونی هست که ازش تجربه دارند و همه چیو با عینک خودشون میببنن.
❗️
❗️
حتی استناد میکنن که فلان همکار یا مدیر خارجی هم اصلا اعتقادش همینه.
❗️
❗️
❗️
در حالی که همون همکار خارجی هم اشتباه میکنه. اون هم فقط نگاه خودشو داره میگه و تجربیات خودشو.
✅️
در همه جای جهان(غیر از هند و پاکستان و اندونزی و روسیه و...)، لینک بیلدینگ و پست مهمان مشابه رپورتاژ، بوده و هست و خواهد بود.
✅️
مدل پیدا کردن و صحبت با رسانه ها در کمپین های روابط عمومی PR، یعنی کاملا کلاه سفید، بوده و هست و خواهد بود.
✅️
مدل اینکه کلا کمپین اف پیج یا PR و کلاه سفیدم ران نشه و فقط تبلیغ بنری یا گوگل ادز یا کلا کمپین های تبلیغاتی فقط ران بشه هم هست که سئوشون فقط تکنیکال و سئو داخلی و کیورد ریسرچ و ساخت صفحه میشه(اونم محدود).
✅️
✅️
همه اینا هست. فقط شرکت با شرکت، فرق داره. سایت با سایت فرق داره‌. هرچقدر بزرگ تر باشن شرکت ها، مدلاشون به مدل آخر نزدیک تر میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/mohsentavoosiseo/906" target="_blank">📅 22:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).  دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست.…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/mohsentavoosiseo/905" target="_blank">📅 20:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سوال:   دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش  اولین سایت که ترب هستش  ولی اگه ترب رو حساب نکنیم میشه سایت سوم طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته  ولی کلیک ۵ تا!! راه حل برای کلیک گرفتن چیه؟ عنوان  و متا هم از دو رقیب دیگه…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/mohsentavoosiseo/903" target="_blank">📅 20:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-902">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوال:
دوستان من یه دسته بندی رو آوردم بالا و رتبه ۴ صفحه ی یک هستش
اولین سایت که ترب هستش
ولی اگه ترب رو حساب نکنیم میشه سایت سوم
طبق سرچ کنسول توی بازه ۲۸ روز ، ۱۲۹ سرچ داشته
ولی کلیک ۵ تا!!
راه حل برای کلیک گرفتن چیه؟
عنوان  و متا هم از دو رقیب دیگه خیلی بهتر هستش.
چون روی کلمه ی اصلی اومده بالا
پاسخ در ویس:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/mohsentavoosiseo/902" target="_blank">📅 19:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سوال:   من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟  پاسخ: https://t.me/mohsentavoosiseo/511 این ویس و ویس پایین  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/mohsentavoosiseo/901" target="_blank">📅 13:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-900">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سوال:
من از وقتی هاست سایتم رو برم روی Geo Dns میهن وب هاست یه مشکلی پیدا کردم. کلمات کلیدی تو سرچ کنسول رتبه دارن ولی وقتی خودم دستی سرچ میکنم نیستن. اکثر ساتیتام اینجوری شدن. این طبیعیه؟
پاسخ:
https://t.me/mohsentavoosiseo/511
این ویس و ویس پایین
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/mohsentavoosiseo/900" target="_blank">📅 13:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).  دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست.…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/mohsentavoosiseo/899" target="_blank">📅 10:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/mohsentavoosiseo/898" target="_blank">📅 11:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/mohsentavoosiseo/897" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تولید محتوا با کلاد
استاندارد سازمان رو برای کلاد تعریف کردن
هوش مصنوعی، چت کردن و چهار تا فایل اتچ کردن و اسکرین شات فرستادن و چهار تا پرامپت خوب دادن نیست! اینا خیلی مقدماتیه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/mohsentavoosiseo/896" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/846
بن میشیم نمیتونیم کلاد بگیریم!
Ban
#بن
#ban
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/mohsentavoosiseo/895" target="_blank">📅 15:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/mohsentavoosiseo/894" target="_blank">📅 15:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تفاوت کلاد تو چیه دقیقا؟ نسبت به بقیه AI ها؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/mohsentavoosiseo/893" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=vuccFlP9gkkBxUnwULYgpFTTAUxcuUmqn9hY-0hTju3lZWYt0ZJmA4Duqh5VkkL1_WCghb3W5exaDTEHQCw2zPgfj_4Su2KRkO8FhM5NWKl7U2xUxvRXIUxmLuTX-E-cS8g4JD_Sg8-S1VQewDszB1Xfsl3qrk4mY91ZhTMbp4FkQpI8lm2HAlnjpXH19KGGMeBRhEhH_y77d5s3BcK1nI20TlUhHNYFTpiIFd95Mc-ECaXtlLHlrraLNCaAMGl8GrTxBKq82zZDTJsD6wLHoFpOnpYD4s8au1s5LpiK7qXOP081fn1jHJ75REWiIcHTI-KIbd5iCERPoGr5Janqp1d1QrtEjOhOlgi--2yHfzK-MVyFZJc9o_hNPtjUFvbojlIuRr9vuxHnijqKbkSWGdrSVnHHZeoKzgP6ik5LlvR8mBhRnOUS7zacmv_hXNW_0hhVjbJKQu5lIsZW0M6R82hdXYqH_cPb2RpatFE7iqp3vUTr581OSneN3OM8MSECuR_vpkEXEMJD69wJwYqr4JxXYBDztXxl7Xi-N8DWSsNo-VzZ3XCVlp3gEg8vnpTHO9C4U7efAGWFpDLDTrBTvnuXut5pKtOqWfrSIwtd7j_HCkOXjQDL7co4L8sq6V9gBDGFuHM_YAc6BEp8Uing9KOJYaJCCP3vYy70-YUR1gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67db1cde60.mp4?token=vuccFlP9gkkBxUnwULYgpFTTAUxcuUmqn9hY-0hTju3lZWYt0ZJmA4Duqh5VkkL1_WCghb3W5exaDTEHQCw2zPgfj_4Su2KRkO8FhM5NWKl7U2xUxvRXIUxmLuTX-E-cS8g4JD_Sg8-S1VQewDszB1Xfsl3qrk4mY91ZhTMbp4FkQpI8lm2HAlnjpXH19KGGMeBRhEhH_y77d5s3BcK1nI20TlUhHNYFTpiIFd95Mc-ECaXtlLHlrraLNCaAMGl8GrTxBKq82zZDTJsD6wLHoFpOnpYD4s8au1s5LpiK7qXOP081fn1jHJ75REWiIcHTI-KIbd5iCERPoGr5Janqp1d1QrtEjOhOlgi--2yHfzK-MVyFZJc9o_hNPtjUFvbojlIuRr9vuxHnijqKbkSWGdrSVnHHZeoKzgP6ik5LlvR8mBhRnOUS7zacmv_hXNW_0hhVjbJKQu5lIsZW0M6R82hdXYqH_cPb2RpatFE7iqp3vUTr581OSneN3OM8MSECuR_vpkEXEMJD69wJwYqr4JxXYBDztXxl7Xi-N8DWSsNo-VzZ3XCVlp3gEg8vnpTHO9C4U7efAGWFpDLDTrBTvnuXut5pKtOqWfrSIwtd7j_HCkOXjQDL7co4L8sq6V9gBDGFuHM_YAc6BEp8Uing9KOJYaJCCP3vYy70-YUR1gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این همون ویدیو بالاست برای کسانی که اینستا ندارند(کار خوبی می کنند برای تمرکزشون)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/mohsentavoosiseo/892" target="_blank">📅 14:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سوال یکی از بچه های گروه دوره:
میشه بهم نظرتون رو بگید که چقدر تفاوت هست بین جمنای با اشتراک گوگل پرو و کلاد ؟
چرا کلاد انقدر محبوب شده و اقلای طاووسی هم دارن تاکید میکنن روش؟
تفاوت سطحش با جمنای در چی هست ؟
خصوصا برای تولید محتوا تجربه دارید جفتش رو مقایسه کنیم؟
البته چون اپدیت جدید در حال ضبطه این سوال پیش اومده براشون
😎
. پاسخ:
https://www.instagram.com/reel/DcBLYe_MLHx/
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/mohsentavoosiseo/891" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پاسخ سوالات پر تکراری که درباره دو پست بالا پرسیده شد:
❓
آیا ما که قبلا دوره رو خریدیم دریافت می کنیم این اپدیت رو؟
بله! فکر کردید من شرکت های خودروسازی داخلی هستم؟ حالا که بازی قشنگ شده جدا شیم؟ شما همراهان قدیمی رو تنها بذارم؟ هوای شما رو که بیشتر باید داشته باشم! پشتیبانی هم دو نفره شده از دو نفر قوی. قدیمی های سال اول خبر ندارند پشتیبانی تلگرامی دارند. جایی دیدید بیفته دنبالتون بگه این ویژگی اضافه شده بیا دریافتش کن. قبلا پولش رو دادی. من میگم! الانم گفتم
😎
❓
این اپدیت چه زمانی منتشر میشه؟
شما تا پایان 2026 روش حساب کنید. خودم نمیدونم. در حال ضبطم. دوسه ماه طول میکشه حداقل. همین ماه البته فصل اولش میاد که البته سبک هست فصل اولش.
❓
من تهیه کردم ولی اون دوره بین المللی، توش خالی هست هیچی نیست!
بالاتر گفتم، اون رو تا اخر 2026 حساب کنید کامل بشه. کم کم میاد در حال ضبطم. اصلا هم نمیتونم عجله کنم. شما اون یکی رو ببینید. دوره سئو جامع. سوالات بعدی هم بخونید!
❓
به درد سایت فارسی هم میخوره؟
بله. ولی مثال های من به همه زبان هاست و کلا مبتنی بر زبان یاد نمی گیرید. مبتنی بر وردپرس هم یاد نمیگیرید. اما هر زبانی و هر CMS و برای وردپرس هم یاد می گیرید.
❓
برای چه سطحی هست؟
از صفر تا خیلی حرفه ای ها. همه. ولی کسی که تا حالا پشت کامپیوتر نبوده یا در حد لاگین کردن تو سایت ها بلد نیست یا تا حالا تو زندگیش فایل word باز نکرده یا بلد نیست وی پی ان استفاده کنه، نه ها!
❓
باید صبر کنیم اپدیت جدید بیاد؟
نه! ببینید دوره فعلی رو. دوره جامع فعلی که دسترسی دارید، کامل و به روز هست. اگر خیلی بی حوصله هستید از فصل "تحقیق کلمات کلیدی و صفحه بندی در عصر هوش مصنوعی" شروع کنید. همش مهم هست و موثر و به روز و کاربردی.
❓
میشه فقط آپدیت AI سئو بین المللی رو جداگونه بگیریم؟
کلا یکی هست! صفر تا صد هست. هوش مصنوعی جدا نیست. بین المللی هم جدا نیست. قیمت دوره هم بسیار پایین هست بخاطر جنگ. کلا امکان بخش خاصی رو جدا خریدن وجود نداره. یا همه یا هیچ هست.
❓
سرفصل های این اپدیت جدید که تصویر یک دوره جدید گذاشته بودید چی هست؟ تو صفحه دوره فعلی سر فصل های این اپدیت هست؟
اون عملا میشه محتوای فصل سئو بین المللی همین دوره جامع، که صفر تا صد سئو به هر زبانی و کاملا آمیخته با هوش مصنوعی(Claude) هست.
توی صفحه فعلی دوره، این سرفصل ها نیست. اما اگر بخرید، این ها هم دریافت خواهید کرد:
موضوعاتی که در آپدیت، پوشش داده میشه این هاست ولی دقیقا عنوان سرفصل ها این نیست. به دلایل متعددی، فقط کسی که دسترسی داره، عنوان ها و سرفصل ها رو دقیق میبینه بعد از انتشار:
🟢
مباحث کار با هوش مصنوعی، OKF, Skill، اسناد AI، Memory، MCP, Connectors.
🟢
انواع SERP در گوگل در در زبان ها و کشور های مختلف
🟢
کسب رتبه در Google Shop (Merchant)
استاندارد سازی پروژه ها با هوش مصنوعی
آنبوردینگ انسان و Agent
🟢
کسب رتبه در کشور خاص، زبان خاص، یا جمعی از کشور ها و زبان ها یا به صورت کلی کسب رتبه و افزایش شانس نمایش و پیشنهاد توسط AI به صورت بین المللی (مثل
booking.com
)
🟢
ساخت پلاگین لینک داخلی خودکار با کلاد برای وردپرس با وایب کدینگ.
🟢
ساخت دسته جمعی صفحات سایت با AI
🟢
تحقیق بازار شامل Intent, Keyword و محدوده سوالاتی که از AI پرسیده می شود.
🟢
ساخت صفحات (تارگتینگ، کلاسترینگ به روش محسن طاوسی. نه اینکه هرکاری اکثریت کردند شما هم بکنید و فرصت ها بسوزند!)
🟢
سئو تکنیکال برای گوگل، بینگ و AI ها.
🟢
بهینه سازی داخلی سایت.
🟢
تولید محتوا با AI
🟢
کسب لینک از کشور ها و زبان های مختلف
کل بحث Off-Page
🟢
هرس صفحات و بهبود نرخ خزش
🟢
چند زبانه کردن سایت از نظر SEO
🟢
گزارش نویسی به هر زبانی
با تمام سرفصل های بالا، AI آمیخته شده است. کلا همشون با AI هست. بیشتر کلاد (اختصاصی از خود کلاد) و تا حدی هم Gemini
جهت خرید، به
@mohsentavoosisupport
پیام بدید. من نیستم پشت این اکانت. بچه ها هستند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/mohsentavoosiseo/890" target="_blank">📅 18:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
قیمت دوره، قرار بود سال 1405 بشه 18 تومن. بخاطر دو تا جنگ و دی ماه، با مبلغ پایین تر در دسترس شد و از 1 شهریور(هفته دیگه)، مشه حدود 6. و سپس هر ماه یا هر سه ماه، افزایش قیمت داره. و طبق معمول، تخفیف دوره ای و مناسبتی هم نداره و هر ماه یا هر 3 ماه، افزایش تدریجی داره.
کاهش قیمت بخاطر جنگ بود و هست. کسی که پارسال 12 تومن میداد، امسال 5 تومن رو سخت تر از اون 12 تومن پارسال میده. درامدش فرقی نکرده و هزینه هاش هم سه برابر شده!
✅
به نقل از خود شرکت کنندگان دوره میگم که در هایتلایت اینستاگرامم هم گذاشتم:
اگر اهل یادگیری سئو یا نمایش یا فروش بیشتر در AI ها هستید یا میخواید اپلای کنید یا پروژه بگیرید، یا کسب و کار خودتون در داخل یا خارج رو به هر زبانی، گسترس بدید، اگر دوره رو ندارید یا نگیرید، احتمال پشیمونی و حسرت که چرا زودتر نگرفتید بالاست. به نقل از خود بچه ها.
❕
اما در عین حال، تضمین نمی کنم. هیچ تعهد و در باغ سبزی هم نشون نمیدم. صرفا هر آنچه دارم رو در دوره آموزش میدم که هر کس با من جلو بیاد، قوی، حرفه ای، بازای و تجاری و بین المللی و با زیرساخت درست بالا بیاد و آبکی نباشه آموزشش و
احتمالا
به چرخه عوض کردن دوره های مختلفش پایان بده.
🟢
قبلش تحقیقات خودتون رو انجام بدید. اگر ذره ای شک داشتید، تهیه نکنید. پولی که با شک پرداخت می کنید برای من جذاب نیست.
و در نظر بگیرید، برای کسب و کار خودتون، خرج نقدی میخواد. فکر نکنید فقط یادگیری هست. پول هم باید خرج کنید. مگر اینکه بخواید استخدام بشید یا پروژه بگیرید.
خرید در:
@mohsentavoosisupport</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/mohsentavoosiseo/889" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-888">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcnnBmkTp8l3NufK6WcSZRKRBvunynUk7q5wbnaByqx1WH40953cxhF2eEZl1FtRsP2pfXXdhFVBI0kuseEizpSDdWcdCmusClWTSn75oPRWjtV-9OJwehMkOwleESVncm2IDE2nusGRMaPJjBpn11oIC30k_cgQutcnpnsyQEcUCiVlwmA8tqqmCbdTclJOrbVqHBBv28RbL-zem1Hh_7hXZJBe1GOMfSC4nTZtCcp8EOQrs_82p0c54PyIbzQ1DBZcuuj_9Z4kfYDTG0-7WR_AP94Vk0unwk5NU9QPuOaNzTQvTyQBQcYtwFtHq8KCsuJUva6af-fdboNcMYX1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسانی که جدیدا دوره رو میخرند، دو تا دوره دریافت می کنند(قدیمی ها نگران نشید تا آخر بخونید).
دوره جدید، برای راحتی ذهن شما جداگونه قرارداده شده و دوره صفر تا صد SEO و AEO برای همه زبان ها و همه کشور هاست! و کاملا آمیخته با AI که ابزار اصلیمون Claude هست. کلاد اختصاصی در محیط خود کلاد. نه این Opus که هوش مصنوعی های ایرانی و خارجی، میفروشند.
البته بگم من مثال هندی پاکستانی نمیزنم. ولی از شرق آسیا یعنی ژاپن، تا قاره آمریکا رو پوشش میدم. آلمانی، ژاپنی، ترکی استانبولی، روسی، فرانسوی، اسپانیایی داریم. فارسی و انگلیسی هم که سرجاش.
این آپدیت احتمالا تا آخر مهر کامل میشه و برای قدیمی ها در فصل سئو بین المللی قرار میگیره. و برای جدید ها، در این یکی دوره
هم
قرار میگیره.
خرید در:
@mohsentavoosisupport
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/888" target="_blank">📅 14:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کلاد، برای هر متخصص SEO و هر متخصص دیگه ای ضروری هست و یک هزینه جاری هست. شما میگید من غذا نمیخورم؟ سوار وسیله نقلیه نمیشم؟ اجاره خونه یا پول قبض نمیدم؟
کلاد هم بهش اضافه کنید. بایدیه. اونم اختصاصی. نه اشتراکی. اصلا با محدودیتی که کلاد رو اکانت هاش داره اشتراکی معنا نداره. با این همه قابلیت، فقط چت نیست! باید اختصاصی بگیرید.
اپدیت دوره که تو همین مرداد یک فصلش میاد، کلا با Claude هست. کوبیدم از اول ساختم. نه فقط ایرانی و فارسی. نه فقط حتی انگلیسی! هرچند Base همون قبلی ها هست که الان هم تو دوره هست. فقط یک ابزار قدرتمند بهمون اضافه شده.
به زودی سورپرایز خواهید شد!
😎
پی نوشت:
(کلاد تلفظ انگلیسیش کلاد هست)، ریشه اسمش فرانسوی هست که میشه کلود. شرکت آنتروپیک هم آمریکایی هست.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/mohsentavoosiseo/886" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/mohsentavoosiseo/885" target="_blank">📅 20:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یکی از
شاخص های سواد از نظر یونسکو
، توانایی یادگیری زدایی(unlearning) و یادگیری مجدد و توانایی استفاده کاربردی از دانش خود است.
خیلی از آموزش هایی که ما میبینیم فقط احساس یادگیری میده و چیز کاربردی یاد نمیده.
نه باعث افزایش درامد میشه. نه اپلای و کسب موقعیت شغلی بهتر، نه پروژه گرفتن و نه حتی نتایج و راحتی بیشتر و بهتر و کم خرج تر برای بهبود رتبه گوگل و شانس پیشنهاد شدن در AI!
خب الان فایدش چی شد؟ درک بیشتر تا یه حدی معنی داره. ارزش داره بری اتحاد، مشتق، انتگرال، اعداد مختلط، سری فوریه رو یاد بگیری که بعد بهتر بتونی مثلا معماری ساختمون انجام بدی؟ یا کد بزنی؟
اگه اعداد مختلط نون شد اومد سر سفره، یا ماشینتو عوض کردی یا خونتو یا دارایی هات رو یا زندگیت با کیفیت تر شد، قطعا مسیرت درسته.
حالا به جای این ریاضیات، هرچیزی بذار. از الگوریتم های گوگل تا مستندات و نحوه کارکرد مدل Fable کلاد تا... .
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/mohsentavoosiseo/884" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بازگشت قیمت(افزایش) دوره از 1 آبان یا زودتر. اگر قسطی دادید قسط رو تا پایان مهر کامل کنید یا اگر دوستی دارید که میخواسته تهیه کنید بهش اطلاع بدید.  با اومدن اپدیت بزرگ دوره(SEO و GEO بین المللی با AI) قیمت، تغییر خواهد کرد. چه اول آبان 1405 چه زودتر.  طبق…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/mohsentavoosiseo/883" target="_blank">📅 20:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
این پست حاوی ایده درامد دلاری و افشاگری پشت پرده هست. دست به دست پخش کنید که در جریان قرار بگیرید پشت پرده چه خبره یا خودتون ازش استفاده کنید:
این نظر سنجی که روش ریپلای زدم رو یادتونه؟
نتیجش این شد که من ورود نمیکنم بهش. ولی شما ورود کنید! در ادامه میگم چرا من ورود نمیکنم.
اینجا بهتون میگم ممکنه برای بعضی ها به صرفه باشه خودتون کاسبیشو راه بندازید:
(توجه: لینک ها درست هستن. با آی پی ایران نرید. من لینک غلط نمیذارم! راهشو پیدا کنید و باز کنید لینک هارو)
https://www.trendyol.com/google/gemini-pro-18-ay-kisisel-mail-e-davet-p-1098587629
این جمینای رو میده240 لیر 18 ماهه. یعنی حدود 1 میلیون تومن. یعنی اگه ویزامستر کارت داشته باشی میخری. اصلا نداشته باشی هم میخری. میدی برات میخرن.
حالا اگه خواستی کاسبی راه بندازی این میشه یکی از منابعت که ازش بخری و بیای بفروشی.
یا برای کلاد بری 150 تا Seat بخری هر کدوم میشه 20 دلار. از ریجن نیجریه میتونی تا 16 دلار و یک کم کمتر بگیری. حالا ریجن نیجریه رو باید با اپل آیدی نیجریه ای بگیری. برای هر 150 تا اکانت که میفروشی(max seats) باید یه اپل ای دی جدا داشته باشی. برای اپل آی دی جدا هم باید از نامبرلند یا هرجا شماره مجازی نیجریه بگیری. ریسک های از دست دادن اکانت اپل و شمارت هم در نظر بگیر.
بعد باید بشینی مدیریت کنی اکانت هایی که میدی رو. و اکانت هایی که تمدید نمی کنن رو. چون از کارتت سر ماه کم میشه مگر اینکه لغو کنی.
من خودم حدود ده تا دونه، یک مدت کوتاه اکانت chatgpt فروختم و خیلی ها هم دوباره پیام دادن که باز هم میخوان. یادتونه؟ چرا متوقف کردم؟ از کجا خریدم خودم؟ از اینجا:
https://www.trendyol.com/openai/chatgpt-plus-aboneligi-kendi-mailinize-davet-ile-tanimlanir-p-947506812
اون موقع میداد 100 لیر و دعوت نامه ای بود! بعد ناگهان تمام سایت های ترکیه، ناموجود کردند! همه با هم! الان میده 600 لیر. یعنی 13 دلار حدودا. باز زیر قیمته.
از اینجا هم میخریدم:
https://www.epinline.com/chatgpt-plusgpt-5dall-e-vip-1-ay-p-26417-m-1
این الان یک ماهه میده 350 لیر. میشه حدود 7.8 دلار.
آیا برای من صرف داره از اینجا بخرم 8 دلار بفروشم 18 دلار اصلا؟ کمتر از 20 دلار خود chatgpt؟ بله ارزش داره!
یعنی رو هر اکانتی که میفروشی حتی دو دلار کمتر از سایت اصلیش، باز بین 5 تا 12 دلار سود میکنی. گاهی هم ممکنه سودت در حد 2 دلار باشه.
این جمینای یک ساله رو میده 150 لیر. یعنی 3 دلار!
https://www.epinline.com/gemini-google-pro-12-ay-mail-adresinize-davet--p-27078-m-1
هزینه جاری خرید اکانت ها، مدیریت، پشتیبانی، تبلیغات و اینکه اطمینان کنن ازت بخرن هم در نظر بگیر.
من بخش اعتماد کاربر و اطلاع رسانیش رو داشتم. با بخش مدیریت و توسعه پذیریش به نسبت دردسر مدیریتش تا رسیدن به سود ماهی 2.3 هزار دلار به صورت غیر فعال(بدون درگیری خودم) اکی نبودم. اگه یه روزی بفروشم، همینه روش کار. حداقل پایه اش اینه. فعلا اصلا ظرفیت ندارم برای پروژه جدید باز کردن تو زندگیم.
و خیلی ساده با گذر زمان همه این پست رو یادشون رفته. من یه پست میذارم میگم اکانت میفروشم. خوبی تلگرام و اینستاگرام همینه که با گذر زمان کسی برنمیگرده پست های قبلی رو بخونه
😅
😎
شاید هم همین الان یکی از بات های فروش این اکانت ها مال منه! از کجا معلوم؟ خدا میدونه
😶
حالا به شما گفتم! قطعا برای خیلی ها به صرفه هست برن تو کارش!
هم سایت بزن هم ربات تلگرام. خیلی راحت با کلاد بنویس ربات رو با وایب کدینگ(همین الان بات احراز هویت و ارتباط با پشتیبان های دوره من، همینطوری نوشته شده توسط خودم با کلاد).
بعد هم پول بده تبلیغ کن جا بنداز پشتیبانی خوب هم بده. این بخش از خود تامین، سخت تر هست. اول فروش. دوم فروش. سوم فروش. بعدا محصول. قطعا باید بها بپرداخت برای اینکه بشناسن محصول شما رو و اعتماد کنن. خیلی بیشتر از بهای خرید و تهیه و تامین خود محصول.
رفع مسئولیت: من فقط تجربه خرید خودم از این سایت ها و دانسته های خودم رو گفتم. هر قدمی برمیدارید خودتون مسئولید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/mohsentavoosiseo/882" target="_blank">📅 14:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSFpsrhR2pGjr-Unwr_YdRvYKNZkaNQJ4LnBW5bFq93TT7iCu010kAYcbt4Q8I9nWIH9-elizewgxbKG6Cw0EY4i0SV_1et4MuX8BK9Q8PX8tbBABe6aIiG9jIOnR7D5fPRmrxj_KNOqgdaMsUIV4HOGU1szf7oeig7vxhVvLYXTIP4mY5M2SBZyoI_04XhPF2RR7VUcX77uaEyX23af_ywqeiEkJA5ISVbVc0hgLKyMYquRMv8NGOjxJGXGWSfWl1PX3VYdRl96W2Qr8xlTcHw-zBAbPW3qPPaOpna6SukY3ZWmUcMFb4p_hM4Sh-Brt4UAQCseTZEVzx0iFg5FGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یکی از ساده ترین هنرکاری های کلاد هست! از منوی رفلکت، بهتون عملکرد خودتونو میگه و واقعا بازخورد های جذابی میده! در اپدیت پیش روی دوره، تمام کسانی که دوره رو دارند، سئو بین المللی با کلاد رو به خشن ترین حالت ممکن یاد می گیرند
😎
.
به من گفته:
ایراد هایی که از skill ها و عملکردشون میگیری، به خاطر دستورات خودت وسط کار هست و یادت میره که خودت خرابش کردی!
😅
یا گفته فلان جا حرف من رو بدون سند رد کردی و هنوز میگه تو اشتباه کردی!
بعد میگم کلاد خداست میگید نه! بازم میرید از فلان جی پی تی، ایرانیش رو میخرید؟ خیلی فرق داره! اختصاصی بگیرید. کانکتور و اسکیل و داکیومنت و کوورک و... تو اختصاصی هست فقط.
mohsentavoosi.com/1
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/mohsentavoosiseo/881" target="_blank">📅 15:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بازگشت قیمت(افزایش) دوره از 1 آبان یا زودتر.
اگر قسطی دادید قسط رو تا پایان مهر کامل کنید یا اگر دوستی دارید که میخواسته تهیه کنید بهش اطلاع بدید.
با اومدن اپدیت بزرگ دوره(SEO و GEO بین المللی با AI) قیمت، تغییر خواهد کرد. چه اول آبان 1405 چه زودتر.
طبق معمول هرکس زودتر ما بپیونده، نفع بیشتری میبره. برعکس جاهای دیگه که همیشه یک کمپین تخفیفی میذارن. ما سال به سال افزایش قیمت داریم. امسال هم شرایط راحت تری بخاطر سه قطعی و دو جنگ بود. روال به صورت کلی و دراز مدت، همیشه افزایشی و بدون کمپین فروش و تخفیف مناسبتی و دوره ای هست.
کسانی که از قبل از اپدیت دوره رو دارند، بدیهی هست که اپدیت رو دریافت می کنند به صورت رایگان.
پیام به:
@mohsentavoosisupport
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/mohsentavoosiseo/880" target="_blank">📅 11:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mloFn8unyH9Vz9lE-lu6TQ8DdSqob4Elgaiq318duE9Bv99LTzV3WCaN_X8J1A-ji0y-NNmg0x199SBmbTqLocQvILko9ntSnCtwLp1h3NEBWCDeDndN7wY5I6LBOprW-muKIbzNkoPi-Xv0Sn5e_25CPgs0o4YAiVQeCMq-omkZlUl-0WBipmdjLsJAq4AUGRzmgydJdjQoku7Tg-7ssCouxW2l_E2Ima6AwYiWiZaF-J9lZ0OzVJLn9k9E1n-fHi6JZbJlhMGpDcXKu8fXQq0GvPCxmcppKC4HQagi57so1VFT78upVEqF2KkPQwy_ufc03dXjH7LrR9jHt3JfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓️
از کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
با چی ایجنت بسازیم؟
کلاد
❓️
از ایجنت کدوم هوش مصنوعی استفاده کنیم؟
کلاد
❓️
از کدوم مدل ها LLM ها استفاده کنیم؟
همه مدل های کلاد. Haiko. Fable. Sonnet. Opus.
❓️
از کدوم AI های اشتراکی یا api داخلی غیر فیلتر استفاده کنیم؟
هیچ کدوم. فقط کلاد اختصاصی.
❓️
برای کد نویسی از چه AI استفاده کنیم؟
Claude Code
❓️
برای مدیریت تسک هامون و انجامشون چطور؟
Claude Cowork
❓️
برای تولید محتوا؟
کلاد
❓️
برای مردن؟
کلاد
❓️
برای...... انقدر سوال نپرس. پاسخ:
کلاد.
❓️
جایگزین کلاد چیه؟
سوال گستاخانه ای بود.
❓️
از سایت های ایرانی کلاد اوپوس گرفتم. خوبه؟
پناه بر کلاد
😭
❓️
چیکار کنم دیگه هی نگی کلاد؟
از کلاد بپرس.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/mohsentavoosiseo/879" target="_blank">📅 20:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.  @mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/mohsentavoosiseo/877" target="_blank">📅 13:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp2_-RB50UrIfFXKaEMCvzsLlaqLUOCH9KKl2d8lyjWcUUbku4VG2F7jg6wiYp2Sawp7OwxF2MayLrLVfyQy5PNGrRSs4SnnGCX_wn1vdJv0f6GBXiCipqMKgH0dM5bXWUwZStBFByjUPmmw1dfl5CQSBnNr0SKAqurRzsNEiLqT_LKjhIWgQKs0a9-XJyMcYlaY2hFGD0baMTmGibw3wEseEWV2M75ZaZb0a4m70aQ03lyTlTgcJWsb4oiVoTF8Dy3Mc9GMl-6j0vmIJTANlIWKTqpqfIfDfpSX90d1umI6_34g5qrEjoyRhWjhKS8U3mRaANNoGcK13eyXJiqfYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی مهم و جالب درباره گزارش نویسی و عملکرد و نقد کار خود، در ویس پایین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/mohsentavoosiseo/875" target="_blank">📅 13:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v232vkdN3Lz__dr9TR3uH-IwKe2TMcv2Sz4ChoOsMcs5jKr4YEtY0M2DBUpXGlFw706Tjskg2gJlcU3C9oRJ4TlIWGJjazPOmADYK9I27BquL08YeKYWfqnZc4ZomPDOEg4yx1x7LSdv7HzhwwVjdEYbVjpnxpDG4f6JxjSgVk9z7gvLwiE7_EuAtQE5D79Njuhzt0A4Ty6wzxXGCKzQATtac0l9UGVil6quzbHaINt4QIU4jvCtfExFa7JRENowpPoHfABrUb7aKcegUMBwN8Q5EhxhW1PGLvXf_EmYKMhQHeXGdxu_TuWm0hfp_04MaqzvLvwYpDDZcOCmDg7Fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vz1_j61GGMp78Gz1QDMs26hXmwy2LVsJqJ3KuqOov1TsCcd-1TmMLTxGi_9hyvtG1FAduKbYeKOxfAB-Zr9rD3R8P9ADm9NDTnwUZwE1U7Jaj9DjRrygqT6nrWukxxWUdeEfXb8wNfCV3l-4PGvreX2riGRRuDQJQihbv2X-ZD3oJreoX66UBckBAVe8k39SoifGihKMVX5g5_Na8DUgfjirzmw6iwgl8StjSZfYbh95L7BafsxNpJZEmnNmccD8f2f_eORyq0akE9cXeNWDDjeNEfD8HGgVe6s74mD5J5s7L99ZUs7tXJLQLyUeQJ_zSn2uzyM-I022pU2zhe29Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصویر چهارستونه(گرونتر) برای ابزار keyword tool هست و تصویر سه ستونه(ارزون تر) برای ابزار Mangools که ایرانی ها به KWFinder میشناسنش.
شما خودتون رو بذارید جای سایتی که ابزار اشتراکی میفروشه.
منگولز، روزی 500 تا سرچ میده. هر منگولز رو به 20 نفر بده، میشه روزی 25 تا برای هر نفر. نفری 2 دلار میشه هزینه خودش. کلا 40 دلار برای 20 نفر میده. میتونه تو پکیج کلیش بگنجونه.
حالا اگه کیورد تول 390 دلاری رو بده، 200 تا در روز داره کلا. به 20 نفر بده هر نفر ماهی 10 تا سرچ داره(بجای 25 تا) و نفری 20 دلار میفته براش. یعنی با دلار نرخ امروز نفری 4 میلیون تومن فقط یه دونه اشتراکیش! فکر کن حالا بخود بیاره تو پکیج هایی که حداکثر یک یا یک و نیم میلیون تومنه!
به من بگو دقیقا چطوری باید این کارو انجام بده؟ در یک صورتی میتونه! اینکه یا جمع کنه بره یا خیریه باز کنه به همه از جیب خودش ابزار اشتراکی بده.
این رو برای مخاطبین خودم پرمیوم هستند نگفتم. چون شما همه چیز رو با دید تجاری پخته نگاه می کنید و نمیگید اااا چرا گرون شد چرا نیست. میفهمید پشت قضیه چطور هست.
برای کسانی گفتم که دید تجاری قوی ندارند.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/mohsentavoosiseo/873" target="_blank">📅 12:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تیم پشتیبانی رفع اشکال دوره تغییر کرده، دیگه یک نفر نیست و روز های تعطیل آخر هفته هم پوشش داده شده. مگر تعطیلات خیلی بزرگ یا استثناها.
که سرعت پاسخگویی بالاتر بره.
نه تیکتی هست نه لزوما تایپی. نه وبینار هست که بخواد ساعت خاصی برگزار شه و آزادی زمانی شما گرفته بشه یا مجبور باشید تو روزها یا ساعت های خاصی آنلاین بشید. چت تلگرام هست. بهترین حالت ممکن.
البته قبلا هم چت تلگرام بود!
خیلی از شرکت کنندگان دوره، خبر ندارن و کلا از چیزی که دارند استفاده نمی کنند.
من که مشکلی ندارم استفاده نکنید
😎
. سر بچه ها خلوت تر میشه راحت تر هستند
😎
. ولی استفاده کنید کنتور نمیندازه! نمیگیم چرا زیاد سوال میپرسی! نمیگیم چرا هر چی توضیح میدی ما نمیفهمیم! برعکس کمک می کنیم سوال رو درست بتونید بپرسید. خیلی راحت هم اگر خارج از سئو باشه یا بلد نباشیم، میگیم نمیدونیم!
"نمیدونم" گفتن تو فرهنگ ما (تیم محسن طاوسی) تابو نیست. برعکس، کسی که همه چیز رو میدونه، احتمالا کلا چیزی نمیدونه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/mohsentavoosiseo/872" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سوال یکی از بچه های دوره در گروه دوره:
من سئوکار یه مجموعه هستم
قرار هست یه سایت دیگه هم بالا بیاریم و کارفرما میگن که کل محصولات همه چی رو یه صفحه باشه(  صفحه اصلی)  و تمامی فیلترها مثلا ارزان ترین گران ترین و تمامی محصولات بیاد صفحه اصلی.
و صفحه تک محصولات و درگاه و تمام
و ن لندینگ ن کتگوری هیچی هیچی
همه چی داخل صفحه اصلی
و من هرچی توضیح  میدم که این اصلا منطقی نیست از لحاظuxدرست نیست از لحاظ سئو چالشی دارید نمیشه کار کرد از همه لحاظ مشکل داره اما اصرار دارن که همین باشه.
حوزه سئویی هم حوزه خیلی سختی هست
چه پیشنهادی دارید؟؟
پاسخ:
اگه یکی اصرار کنه من ماشین با چرخ چهارگوش میخوام شما چون مکانیک یا خودروسازی باید بگی باشه؟ ولشکن کلا. نمیشه. اون کارفرما دید و اطلاعات حداقلی نداره. ولی شما که دارید.
نکته برای سوال کننده:
شما یو ایکس رو ولکن. چالش داره از نظر سئو درست نیست! کلا نمیشه. چالش یه چیز کوچکتر و معمولا قابل حله. نه یه زیرساخت مهم اصلی که بخواد وجود نداشته باشه.
و قطعا شما قاطع نگفتی نمیشه. داری چونه میزنی. اونم میخواد چونه بزنه. تخصصشو نداره که. از مدل سوال که نوشته شده "چالش داره سئوش" مشخص هست خود سوال کننده محکم نگفته نمیشه. خودشم شک داره. بدیهیه که کارفرما که دل خجسته ای داره بنده خدا و اطلاعات نداره چونه میزنه و اصرار میکنه که بشه. من ایرادی تو کارفرما با توجه به سوال(بخش چالش) نمیبینم. اون حق داره بخواد. شما حق نداری ببری رو اصرار و چالش و موضع غیر محکم. پاسخ انجام یک چیز چالش دار و با فشار نیست!
پاسخ یک "نه" و "کلا نمیشه" صد درصدی بزرگ و قاطع هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/mohsentavoosiseo/871" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درباره کمپین تبلیغات محیطی ا.......پ
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/mohsentavoosiseo/870" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/mohsentavoosiseo/869" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">https://t.me/mohsentavoosiseo/737
صفر تا صد مشکلات ایندکس شدن صفحات سایت.
❗️
دست و پا نزن برای به زور ایندکس کردن.
✅️
7 چیزی که باید چک کنید. تمام پاسخ های من به این موضوع
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/mohsentavoosiseo/868" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستانی که ایران نیستند،
با توجه به اینکه اپدیت پیش روی دوره، بسیار تمرکزش سئو بین المللی و چند زبانه و مبتنی بر هوش مصنوعی هست،
و اسپات پلیر هم دوباره از وایت لیست خارج شده و از خارج دوباره در دسترس نیست و دیتا سنتر ها دوباره محدودیت هایی برای دسترسی از خارج به داخل اعمال کردند،
اگر نیاز به وی پی ان ایران دارید به دایرکت همین کانال(آیکون پیام یا کلید message) پیام بدید تا وی پی ان ایران براتون بفرستم. وی پی انی که خودم استفاده می کنم (میخرم).</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/mohsentavoosiseo/867" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چرت تر از دو جمله زیر نمیشناسم تو زندگیم:
❌️
درخت پربارتر افتاده تر است.
❌️
هرجا خبری هست ادعایی نیست.
بولشیت کامل. Absolutely nonsense.
مغز اصلا نباید دنبال این باشه که کی متواضعه کی پرباره. هر قسمتی که برامون سودمنده بصورت متغیر و داینامیک و قسمت شده، بر میداریم و استفاده می کنیم.
❗️
نمونه انسان ها و شرکت های سوپرموفق و پر ادعا و متکبر و غیر متواضع:
✅️
استیو جابز. هم بنیانگذار اپل و مخترع صفحه نمایش لمسی و اسکرولی که همین الان گوشی ها دارند و کلی چیز دیگه.
اخلاق گند مرحوم به گوش همه رسیده.
✅️
تراویس کالانیک، هم بنیانگذار اوبر که بخاطر اخلاق گندش از شرکت خودش به عنوان مدیرعاملی اخراج شد. همچنان ثروتمند و صاحب شرکت Atoms هست که ربات تولید میکنه.
✅️
هنری فورد! شرکت بی نظیر خودرو Ford
✅️
ارسطو اوناسیس، غول کشتیرانی یونانی قرن گذشته.
✅️
لاری الیسون. هم بنیانگذار اوراکل.
✅️
پابلو اسکوبار. قاچاقچی و تولید کننده معروف کوکائین مدیین کلمبیا(مدلین که همه میگن غلطه. ل نیست. ی هست. Medellín) سی چهل سال پیش. راستی خلافکارای موفق چی؟ ادعا باید داشته باشن یا باید متواضع باشن؟
هزاران مثال می تونید در طول تاریخ پیدا کنید. کلا من با گره زدن اخلاق و کسب و کار یا موفقیت، مشکل دارم.
قطعا مرتبط و موثرند روی هم. قطعا اخلاق و انسانیت مهمه. کسب پول از راه سالم و بدون دروغ و فریب و دزدی و... مهمه. آسیب نزدن به کره زمین، طبیعت، آدم ها، همدیگه و حیوون ها مهمه و ضروریه. قطعا مهربونی با حیوانات نشانه ای از تمدن و انسانیت هست و بدرفتاری باهاشون نشانه عقب ماندگی و بربریت.
ولی خیلی گوگولی و کودکانست اون دو جمله بولشیت اول این پست درباره تواضع و ادعا.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/mohsentavoosiseo/866" target="_blank">📅 13:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/mohsentavoosiseo/864" target="_blank">📅 12:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فیچر و امکانات و قابلیت: ۱۰ درصد
فروش و به سود رسیدن: ۹۰ درصد
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/mohsentavoosiseo/863" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حالا با توجه به دو پست بالا، الان سئو مرده با هوش مصنوعی؟
چرا سرچ کنسول جمع نمیکنه پس؟ چرا فیچر وریفای کردن پیج اینستا و...هم اضافه کرده؟ اون تیم به این بزرگی دنبال چی هست برای سئویی که مرده؟ ( اون تیم، عملا تیم پر هزینه توسعه سرچ کنسول هست برای وب مستر ها که زمین بازی و دون پاشی برای محصول اصلی یعنی گوگل ادز هست).
گوگل ادز چرا نمیمیره؟ چرا رشد هم داره فروش ادز؟ مگه جستجوی کلمه ای نمرده؟ چرا هنوز آدم ها و شرکت های زیادی در سراسر جهان، کمپین های بزرگ گوگل ادز با جستجوی کلمات کلیدی اجرا میکنند؟
الان این تحلیلی که داشتیم چه ربطی به هوش مصنوعی داشت؟
چرا این سئو بجای اینکه بمیره هی قدرتمند تر و مهم تر میشه؟
هوش مصنوعی فقط تسهیل گر و سرعت بخش و بالا برنده دقت ماست برای اجرا و پیاده سازی. برای تحقیق. برای تحلیل. قبلا چرتکه بود تو فروشگاه ها. الان کارتخوان متصل به صفحه نمایش دوطرفه و لمسی هست. حتی تو خیلی از فروشگاه ها که صندوق های فول اتوماتیک هست، باز یک مسئول و یک اپراتور تنظیم و تعمیر و راهنما داره.
شما اون اوپراتور هستید که خیلی بیشتر از یک اپراتور پشت صندوق، باید حرفه ای باشید و اصول رو بلد باشید بدون وابستگی به ابزار. بدون وابستگی به CMS و وردپرس بودن یا نبود و کد سایت و زبان پروژه!
حالا شما باید کلاد رو کانفیگ کنید که خروجی خوب بده. دیتا رو درست بخونه. یه مستر(استاد و حرفه ای) باید بالاسر هوش مصنوعی باشه تو سئو.
و اون Master شمایید. کسی که به هوش مصنوعی وقتی چیزی میگه، هوش مصنوعی میگه آهان اره و ادامش میده.
اون مغز متفکر که هوش مصنوعی از رود دستش باید ادامه بده، شمایید. پس باید کامل سئو رو بلد باشید. سنتی ولی عمیق بلد باشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/mohsentavoosiseo/861" target="_blank">📅 17:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این عکس، نمودار حدود 8 ماه گذشته یکی از پروژه های انگلیسی هست. هیچ فیلتری جز زمان هم ست نشده.  تاریخ 5 فوریه زمان شروع همکاری بوده.  به نظرتون بد شده اوضاعش یا خوب شده؟ اگه میخواید بگید نمودار پوزیشن بدتر شده پس بده که متاسفانه تحلیلتون غلطه و کل سئو رو درست…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/mohsentavoosiseo/860" target="_blank">📅 17:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjVsvJYch2ndnKvoNfGkfgHOaLF_VoqUHKfHwbZ27R01fRroC02S8RYjDS9OZyFwYo-darG7jdLPxf3QTdXDVJ6zzL6L66s4ETS7PzLBFZQRe_cr9pbohD2rOUAuknWm3TPFaBNUdP29JGgDu8VA1zGXzXeYv0G6M8vUVOC7pIOyvt-aY5x4zB-346j-MVtUk8ujnd1T9oot9W5kFHPbut7JoBy_3QWQVeMT0dQOar9GWP6rO2QzO1ZaOhOSWrMhrzxuJ8XrEmDWNOkKkD-aJ3zFl9qZDeybUKY0eCwORKCCAssu02WRc9BFnGE7Uz36LbjQnmp5FKGL1h5iW6hSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس، نمودار حدود 8 ماه گذشته یکی از پروژه های انگلیسی هست. هیچ فیلتری جز زمان هم ست نشده.
تاریخ 5 فوریه زمان شروع همکاری بوده.
به نظرتون بد شده اوضاعش یا خوب شده؟
اگه میخواید بگید نمودار پوزیشن بدتر شده پس بده که متاسفانه تحلیلتون غلطه و کل سئو رو درست یاد نگرفتید. (
اینجا
توضیح دادم چرا).
اگر میخواید بگید کلیک ها کمتر شده در کل، پس بدتر شده، مثل پوزیشن اونقدر تحلیلتون اشتباه نیست. ولی باز هم کافی نیست. لزوما بدتر نشده.
اتفاقی که افتاده اینه که کلی صفحه با کیورد های اشتباه، حذف شدند. کلی صفحه که مانع رتبه گرفتن بقیه صفحات میشدند ریدایرکت و ادغام شدند(اصلاح تارگتینگ) و کلی صفحه بیخود که فقط باجت رو مصرف می کردند حذف شدند.
این یعنی کلیک هایی که الان نزدیک شده به کلیک زمان شروع این پروژه، نرخ تبدیل بالاتری دارند و کارفرما کاملا تفاوت تماس و مشتری از سایت رو متوجه میشه و مستقیما تاثیر مثبت مالی داره.
سوالم رو دوباره میپرسم. حالا به نظرتون وضعیت سایت بهتر شده یا بدتر؟
😎
سئو رو عمیق و درست یاد بگیریم و با دید تجاری. نه با بلغور ترجمه. نه سطحی. نه غیر کاربردی. نه با لفظ بازی بی کاربرد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/mohsentavoosiseo/859" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-858">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فلسفه زندگی من
روتین
نون کردن
پرداخت بهای غیر زمانی و غیر مالی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/mohsentavoosiseo/858" target="_blank">📅 14:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ادامه پست قبلی:  مغزتون رو درگیر واژه ها نکنید. تو بحث پیچیده و علمی و خاص و واژه سازی حرف زدن، من پروردگار پیچیده سازی هستم! میتونم یه کاری کنم از این به بعد پست های من رو ببینید بگید ااااااااا وای چقدر این آدم خفن و با سواده. ولی کاربرد نداره و بیشتر کسانی…</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/mohsentavoosiseo/857" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-855">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادامه پست قبلی:
مغزتون رو درگیر واژه ها نکنید. تو بحث پیچیده و علمی و خاص و واژه سازی حرف زدن، من پروردگار پیچیده سازی هستم! میتونم یه کاری کنم از این به بعد پست های من رو ببینید بگید ااااااااا وای چقدر این آدم خفن و با سواده. ولی کاربرد نداره و بیشتر کسانی گول میخورن که تجربه کمتری دارند.
مهمه که انتقال مفهوم و آموزش دادن، ساده باشه، کاربردی باشه و یه نونی بده دستت یا تنور نونواییت رو داغتر کنه. وگرنه آدم ها بعد از مدتی دیدن آموزش هات، میفهمن که با واژه ها، کارشون باتو پیش نمیره.
الان همین پیلار کلاستر که من تو دوره دو فصل دربارش حرف زدم با عنوان Keyword Targeting on Pages،
شاخص داره، ل
ینک داخلی ازش در میاد،
عنوان ها ازش در میان،
نرخ تبدیل ازش در میاد،
رقابت و سرچ والیوم ازش در میاد،
اولویت بندی ازش درمیاد،
انتیتی ها خودبخود اجرا میشن،
ویژگی ها و صفت ها و کاربرد ها ازش در میان،
نالج گراف تا حد مورد نیاز و نه بیشتر، خودبخود تکمیل میشه
و به طور پیشفرض اصلا نقشه موضوعی یا Topical Map استخراج میشه.
و در نهایت منجر به رشد اعتبار موضوعی یا Topical Authority میشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/mohsentavoosiseo/855" target="_blank">📅 14:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-854">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جمله زیر رو یکی از بچه ها در گروه شرکت کنندگان دوره به نقل از دیگری نوشت که نظرم رو در ادامه، زیرش مینویسم.
به نظر من کیورد ریسرچ به شکل سنتی خیلی وقته منسوخ شده.
اگر هنوز فرآیند سئو رو با پیدا کردن کیورد و ساختن لیست کلمات شروع می‌کنید، بهتره رویکرد رو تغییر بدید و وارد مسیرهای جدید بشید:
به جای کیورد ریسرچ، EAV Research
به جای پیدا کردن کلمه، Entity Research
به جای تمرکز روی سرچ‌ولوم، Topic Research
به جای پیلار کلاستر،  Topical Map
به جای تولید محتوا برای کلیک و ایمپرشن ، تکمیل Knowledge Graph سایت
امروز باید ببینید :
موجودیت اصلی کسب‌وکار شما چیست
چه Attribute هایی دارد
چه Entity هایی به آن مرتبط هستند
چه ارتباطی بین آن‌ها باید ساخته شود.
سئو دیگر فقط گرفتن رتبه برای Query نیست؛ ساختن یک مدل معنایی کامل از یک حوزه است که گوگل بتواند تخصص و اعتبار سایت را در آن درک کند.
این حرف، بسیار دهن پر کن و جذاب هست. اما در دنیای اجرا و عمل، برمیگرده به همون چیزهای قبل. وقتی شما به شکل سنتی کیورد ریسرچ میکنی بیشتر از 80 درصد موارد بالا، خودبخود انجام شده است.
یکی از جملات من در دوره که تو آموزش رایگان هم درباره تحقیق کلمات کلیدی در
این لینک
گفتم، اینه که تحقیق کلمات کلیدی، بر اساس صفت، برند و کاربرد باید انجام بشه. دقت کنید: صفت، برند و کاربرد.
همچنین آموزش دادم که چطور خارج از اون کیورد هم کلمه در بیاریم. مثلا برای دسته لوازم جانبی موبایل، "قاب موبایل" که توش "لوازم جانبی" نداره.
پس عملا شما با کیورد ریسرچی که من گفتم یا  خودتون به هر شکلی یاد گرفتید و اینطوری انجام میدید، بیشتر از 80 درصد جملات جذاب نقل قول شده بالا رو دارید اجرا میکنید.
حالا در این شرایط،
EAV Research و Entity Research و Topic Research و چه Attribute هایی دارد و چه Entity هایی به آن مرتبط هستند و  چه ارتباطی بین آن‌ها باید ساخته شود
خودبخود انجام شده. احتمالا نویسنده خودش روش هاش خیلی بیش از حد قدیمی بوده.
این جمله هم کلا اشتباهه:
به جای تولید محتوا برای کلیک و ایمپرشن ، تکمیل Knowledge Graph سایت.
چون اصلا نباید اینکار رو کنید به خصوص در این عصر هوش مصنوعی که AI Overview میاد از رقیب های  همین دیتا رو کامل تر از تو برمیداره و جستجوی عبارت های informational رفته سمت هوش مصنوعی.
گذشت زمانی که باید کامل راجع به یک چیزی حرف بزنی تا رتبه بگیری. واقعیت از اول هم اینطوری نبود اصلا!
یعنی برای اینکه تو "بروکر فارکس" بیای بالا لازم نیست عین همون الفبای قبلی رو درباره ترید مثل "اسپرد چیست" مثل "تحلیل تکنیکال و فاندامنتال" و... که تکرار مکررات هست بیای بنویسی دربارش.
قرار نیست برای اینکه تو کلمه "طراحی سایت" بیای بالا راجع به همه طراحی های سایت ها حرف بزنی. اصلا به این سادگی ها نیست. حرف بزن. بعد که صفحه 5 گیر کردی و رقیبت با Off-Page و ترافیک قوی و بدون هیچ نالج گراف کاملی در سایتش اومد بالا، بیا باهم صحبت کنیم اون موقع.
این جمله کلا از اساس غلطه و نویسنده حتی نمی دونه "موجودیت" یعنی چی.
موجودیت اصلی کسب‌وکار شما چیست.
یه برنامه نویس بهتر متوجه میشه entity یا موجودیت یعنی چی.
کسب و کار که موجودیت نمیشه! مجموعه ای از موجودیت های متصل به هم میشه یک کسب و کار. اگه بخوایم از نگاه اسکیما بهش موجودیت بدیم، میشه یه local business یا person یا organization. کسب و کار محلی، شخص یا سازمان. همین! الان این حس خفن بودن میده؟ واااااااای من موجودیت کسب و کارم رو دراوردم! سلطان خود پیش فرض افزونه های سئو وردپرس اینو برات میندازن اصلا. نیازی به زحمتت نبود!
اگرم منظور خود موجودیت غیر اسکیمایی هست که یک کسب و کار، یه دونه موجودیت نیست که! جمله غلطه!
انتیتی یا موجودیت یعنی یک چیز! واقعا چیز! یک thing. که جدا و قابل تشخیصه. و اسم داره، هویت داره، ویژگی داره و ارتباط با سایر موجودیت ها. الان محسن طاوسی یک موجودیت هست. اسم داره. مکان داره ویژگی داره. و تمام ویژگی های موجودیت "انسان" رو به ارث میبره.
الان حس می کنی سئو رو خیلی خفن تر بلدی؟ نه فقط مغز بیچارت رو پر از دیتای بی کاربرد کردی که تو رو از پول دور میکنه ولی احساس کاذب خفن بودن بهت میده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/mohsentavoosiseo/854" target="_blank">📅 14:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نظر من درباره ابزار های تحقیق کلمات کلیدی:
🔴
موافق اصرار بر اینکه کیورد تول خوبه منگولز خوب نیست(KWFinder) نیستم. این صرفا یه احساس هست. واقعا منگولز یه چیز دیگست. اگر مبلغ اورجینال اختصاصیشو حساب کنیم، از کیورتول ارزون تر هم هست. خیلی هم کامل تره. سرچ با دامنه هم داره. و کلی امکانات دیگه.
🟢
فقط برای کیورد های فارسی، همون سئو سیگنالز کافیه مگر اینکه دوست داشته باشید ابزار جهانی بخرید. یعنی صرفا با سئو سیگنال چیزی از دست نمیدید برای کیورد های فارسی. اتفاقا استخراج کلمات با وارد کردن دامنه هم داره. قوی هم هست تو فارسی ها.
عدد های سرچ والیوم(تعداد جستجوی کلمات در ماه) هم خیلی روش حساب نکنید. همه ابزار ها دقیق نیستند. کلا نمیشه دقیق فهمید. حدودی هم نمیشه فهمید. ولی نسبت رو میشه فهمید. همون کافیه. رو هر عددی که ابزار ها میدن حساب کنید. اما برنامه ریزی مالی روش نکنید.
🟢
ابزار خارجی ارزون تری که اشتراکیشم راحت تر در دسترس هست، سمراش هست. Semrush جستجو با دامنه هم داره. یعنی استخراج کلمات با وارد کردن دامنه. و گپ رقبا. اما خیلی ضعیف تر از منگولز و کیورد تول هست.
🟢
برای گپ، نیازی نیست خود اون ابزاره گپ داشته باشه. من تو آموزش زیر به صورت کاملا رایگان و با گوگل شیت یا اکسل، استخراج کیورد گپ رو آموزش دادم. کافیه با ابزار ها بر اساس دامنه، استخراج کنید. بعد رقیباتون رو طبق آموزشی که گفتم قرار بدید تو شیت. خودتونم کیورد های سایت خودتونو قرار بدید تو شیت.
و خود این فایل شیت که دادم(کپی بگیرید ازش)، گپ رو میده:
https://mohsentavoosi.com/video/keyword-gap-excel/
اینم لینک کامل آموزش و مستنداتش و گوگل شیتش(تقاضای دسترسی ندید. read only هست). به جاش کپی کنید ازش از منوی File، و برای خودتون مستقل داشته باشید و هر بلایی خواستید سرش بیارید.
اگر آموزش میدید یا به کسی کمک میکنید، منشن من و منبع(اینجا) رو فراموش نکنید. من کپی کننده خارجی ها نیستم که بگید خودشوم از خارجیا برداشته و این حرفا.
❕
پی نوشت 1:
کیورد گپ یعنی رقباتون رو چه کیورد هایی رتبه یا ایمپرشن کلیک دارند و شما ندارید. شکاف کلمات کلیدی. قسمت خالی کلمات کلیدی و ضعف شما نسبت به رقباتون.
❗️
پی نوشت 2:
کامنت های زیادی زیر پستی که گذاشتم اومده که لینک گوگل شیت کجاست؟ در حالی که تو متن پست گذاشتم تو ویدیو هم کلامی و تصویری گفتم لینک رو. بخونید کامل صفحه رو.
‼️
پی نوشت 3:
ترخدا مغزتونو با استوری و پست دیدن اینستا و یوتیوب نابود نکنید. مغز خیلی ها بدو بدو شده یه صفحه رو نمیتونن یک بار بشینن کامل بخونن. پنج هزار بار درباره محتوایی که میبینن سوال تو ذهنشون ایجاد میشه چون یک بار نمیتونن ببینن و تمرکز کنن. خیلی اوضاع تمرکز ذهن ها خرابه.
‼️
پی نوشت 4:
بخدا من هم ADHD دارم یا ژنتیکی یا از محیط و عادت. ولی کنترلش کردم. من هم درون گرام یا حداقل درون گرایی قوی دارم. ولی توجیه نمیکنم(میون پرانتز، توجیه رو توجیح ننویسید)  که چون از درون انرژی میگیرم، پس ارتباطات بلد نباشم یا خجالت بکشم، و بگم من خجالت و بلد نبودنم اشکال نداره چون درون گرام!
درونگرا باید بتونه جلوی پنج هزار نفر سخنرانی کنه حتی با تپق ولی بدون خجالت و بتونه احساساتشو در جمع بیان کنه. اگر نمیتونه ربطی به درون گرایی نداره. به خدا قسم نداره. اگر آتئیستی به خاک استیفن هاوکینگ و داروین قسم که بی مهارتیه. شرم الکیه. جای رشد داره.
درون گرا فقط از درون خودش بیشتر از بیرون انرژی دریافت میکنه. شارژش تو تنهاییه. همین! چه ربطی به خجالتی بودن و بی مهارت بودن تو ارتباطات داره؟!
یه ای دی اچ دی در سطحی که تو جامعست(نه بچه هایی که از سنین کم اختلال یادگیری دارند)، هم میتونه یاد بگیره تمرکز کنه. بدون قرص. یه بار هم که شده مسئولیت خودمونو گردن بگیریم. تو این عصر هوش مصنوعی میخواید همچنان بدو بدو همه چیو ببینید؟ چجوری میخواید AI Agent تربیت کنید پس؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/852" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a9cb06f1.mp4?token=Qkgv30cvzbA4SXNx6lLtS6EcLN_Q2azM1Azzz0WeVtMF2xGjUOMgrkyE2qrmPwTUPk_BDQoCdr96hJHVvDXj97atlxjfAq7DN1xylsPZwb1XRPRTxJs15l_KYgLDDySBoxdCMYi7eMU5a5s-2xKOPMTPs-NcyrQplW4RxevsjhgR8d2GWdaV-rJFhy6icWxXRCwFZaap7pVBm2ajKEzekJSByLSXb06GyM4XZYvstU0W0VTOwtg_e8VbTGm4ge9lvEXCMNWnYS9xdHsSkhA-ZTF0eJq8rxkE3ekE6b6gaaSMQuTIaWNJkxNHgJC1JrieDgsB4YHRN0uitYwpRBkeeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a9cb06f1.mp4?token=Qkgv30cvzbA4SXNx6lLtS6EcLN_Q2azM1Azzz0WeVtMF2xGjUOMgrkyE2qrmPwTUPk_BDQoCdr96hJHVvDXj97atlxjfAq7DN1xylsPZwb1XRPRTxJs15l_KYgLDDySBoxdCMYi7eMU5a5s-2xKOPMTPs-NcyrQplW4RxevsjhgR8d2GWdaV-rJFhy6icWxXRCwFZaap7pVBm2ajKEzekJSByLSXb06GyM4XZYvstU0W0VTOwtg_e8VbTGm4ge9lvEXCMNWnYS9xdHsSkhA-ZTF0eJq8rxkE3ekE6b6gaaSMQuTIaWNJkxNHgJC1JrieDgsB4YHRN0uitYwpRBkeeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
تو جشنواره تریبون، رتبه‌ات رو برگردون
🍀
تا ۸۰٪ تخفیف خرید رپورتاژ
🌼
تا ۶۰٪ تخفیف خرید بک‌لینک
🌿
۲٪ کش بک روی هر سبد خرید
🌼
رپورتاژ رایگان و امکان پرداخت قسطی
🍒
فقط تا ۳ مرداد
🍊
همین الان وارد جشنواره تریبون شو و رتبه‌ات رو برگردون
اطلاعات بیشتر در:
⬇️
tribn.ir/Vrfz6P
tribn.ir/Vrfz6P
ℹ️
این پست، تبلیغ هست. Ad
ℹ️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/mohsentavoosiseo/851" target="_blank">📅 16:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان اینجا کسی هست تو عنوان نویسی رپورتاژ قوی باشه ؟
چه جالب مگه عنوان نویسی شاخه جدایی داره خوب هر کی مقاله رو بنویسه عنوانم در میاره دیگه! مگه اینجوری نیست!؟
Are you kidding? Realy?
واقعا بعد از دیدن دوره و این همه ویدیو و سرفصل، سوال دوم بالا سواله؟
😭
😭
یعنی تولید کننده محتوا اطلاعات داره از سرچ والیوم و ابزار کیورد ریسرچ و میانگین موضوع کیورد و سایت شما و سایت رسانه رپورتاژ که این همه تو دوره ویدیو داره؟
طبیعیه که ادم ها دوره رو کامل نبینن. ولی بهتر نیست سوال شه که ااااا راجع بهش تو دوره هست؟ کدوم فصل ها کدوم ویدیو ها؟
تو این عصر هوش مصنوعی همه رو از AI میپرسی یا از دانشگاه یوتیوب! پس قطعا من باید ارزش افزوده دیگه ای داشته باشم. وگرنه که این همه مدرس. این همه آموزش رایگان. این همه منبع.
اگر دوره من رو دارید، ببینیدش! استفاده کنید ازش. دریاییه که تو محتواش غرق میشید. ولی موج سوار تو دریای طوفانی بیرون میاید.
THANKS FOR YOUR ATTENTION TO THIS MATTER. PRESIDENT MT.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/mohsentavoosiseo/848" target="_blank">📅 00:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/mohsentavoosiseo/847" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/mohsentavoosiseo/846" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.   با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.   پس من ورود…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/mohsentavoosiseo/844" target="_blank">📅 12:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوستانی که اکانت کلاد خریدند و تجربه موفق دارند و بن نشده لطفا تو دایرکت همین کانال اعلام کنید.
با توجه به نظر سنجی بالا من نمیبینم توی خودم که ماهانه به ۱۰۰۰ نفر بفروشم. نهایت میشه ۱۰۰ نفر با کلی دردسر. میشه حداکثر ماهی ۲۰۰ دلار با کلی مکافات.
پس من ورود نمی کنم به اینکار. و میخوام شما بگید از کجا میگیرید که عمومی بذارم بقیه هم برن بگیرن. کلاد بدون دردسر و بدون محدودیت.
از یک سرویس عمومی که همه بتونن. نه دوست و آشنا و کارت خارجی خودتون.
بگید که منم به بقیه بگم. تو دایرکت کانال بفرستید.
اگر ا......ت بوده فقط اگه بعد از اون بن شدن های دسته جمعیش بوده باشه بگید.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/mohsentavoosiseo/843" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/mohsentavoosiseo/842" target="_blank">📅 15:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/mohsentavoosiseo/841" target="_blank">📅 15:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ربطی به سوال بالا نداره. کلی هست.
با کلاس و بی کلاس در تعریف من.
پرداخت به هرچیزی جز خود‌ عیب جویی از هرکسی جز خود. مطابق مطالب زرد و سطحی.
#تروما
#آسیب
#سمی
#طرحواره
#تله
#عیب
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/mohsentavoosiseo/840" target="_blank">📅 15:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/839" target="_blank">📅 14:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-838">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/mohsentavoosiseo/838" target="_blank">📅 14:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پاسخ سوال بالا، قسمت ششم
در تجارت، تواضع اشتباه هست.منت گذاشتن بسیار مهم و جایز هست. ترکیب تضادها در کار.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/837" target="_blank">📅 14:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاسخ سوال بالا، قسمت پنجم
انتقال پیام پنهان ضعف
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/mohsentavoosiseo/836" target="_blank">📅 14:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پاسخ سوال بالا، قسمت چهارم
هم خدا هم خرما. در نظر گرفتن استاندارد تخفیفی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/mohsentavoosiseo/835" target="_blank">📅 14:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/mohsentavoosiseo/834" target="_blank">📅 14:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/mohsentavoosiseo/833" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/mohsentavoosiseo/831" target="_blank">📅 13:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxQ5mXZwI4TCc1UYhDlSIcchfDzpX9ZZnhq4np7KOPeryodA__S8tLjXwRf_ARV7G7Oedi4OJ2rsH6DacMJJGXvUhoDCd9BP5TK_yp78_W_gIJBiNUdfNECszt4ianRRX13YtV-Q2Q9xIQQy3M0pDg3U_Ybj34IidkB86bre-AzywaMo5xWBfXbhx-ZkhzpASUZIK1m49mNw-TLxrhzBNF2kntKaYAEDRxagbBis6hQx847xKiWPgZ740beZTx3FGogndRyvIVnxY1qa7PMtUM92JshOWIJLHzxoxJytHZ6rMR8NyGJjaYY3HLpomcRgjrf1i0OOPN-YrqZLHL8Tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/mohsentavoosiseo/830" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان اموزشی پادکستی سراغ دارید برای این مهارتی که وقتی سر پول گرفتن فضا سنگین میشه بتونی هندل کنی ! کلا تعارف نکنی یا با ادب بتونی پولتو بگیری بدون اینکه وارد تعارف های بیش از حد بشی یا وارد فضای سنگین بشی و طرف با قدرت کلامش بواسطه تجریش ازت امتیاز نگیره ( مثلا تخفیف بگیره یا نگه داره فردا پس فردا نکنه) ؟
حس‌میکنم این بازاریا وقتی دادن پولتو یک روز هم بیشتر طول میدن احساس برنده بودن میکنن . اینو چطوری بهش غلبه میکنین
مثلا طرف قفل میکنه تخفیف بده
یا همشو نمیدم نصف میدم نصف یوقت دیگ
وقتی سفت میگیری کلا ناراحت میشن و کار نمیگیره وقتی هم که راه میای باید داستان داشته باشی
نه که ندن ولی پولو از ارزش میندازن یبار
جواب سوال بالا در ادامه.(یه پادکست ضبط کردم. طولانی شد ویس ها).
#پروژه
#پروژه_گرفتن
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/mohsentavoosiseo/829" target="_blank">📅 13:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه کلاس زبان عمومی باید برای کلمه "People" قرار بدیم. اینجوری فایده نداره. خوب نیست دیگه انقدر آدم بی سواد باشه در عصر هوش مصنوعی که مترجم در لحظه و رایگان در دسترس هست.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/mohsentavoosiseo/828" target="_blank">📅 12:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پاسخ سوال بالا
https://t.me/mohsentavoosiseo/826
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/mohsentavoosiseo/827" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-826">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سوال از پشتیبان دوره(سانسور شده):
من دسترسی کامل به دوره دارم و دارم رو سایتم کار می کنم.
کارفرما اومده بهم میگه که یه محصولی به نام x یا خرید x ما تقریبا از سه ماه پیش اومدیم روی رتبه یک و محصولی بوده که تقریبا فقط ما داشتیم.
الان رقیبمون هم این محصول رو موجود کرده. در صورتی که دو سه روزه محصول رو تو سایت گذاشته و اومده لینک دو. اما ما خیلی طول کشید تا بیایم لینک یک.
من جواب لحظه ای که به کارفرما دادم این بود که شما سرمایه گذاری درستی روی سایتت نکردی الان سایتت از نظر UX و پرفورمنس و اعتبار و off page  صفره و مسلمه که سایتی با این اعتبار سریع میاد لینک دو و بعد ما.
الان کارفرما میگه با من با عدد حرف بزن و منطقی بهم بگو که دقیق چیکا کنم که تا چند روز اینده این سایت نیاد جای من که رتبه یک هستم رو بگیره.
پاسخ در voice پیش رو:
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/mohsentavoosiseo/826" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/mohsentavoosiseo/825" target="_blank">📅 22:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر لینک پستش رو میذارم. ولی حرفم خود تصویر نیست.  بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/mohsentavoosiseo/824" target="_blank">📅 22:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-823">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 این تصاویر رو می بینید کامل؟</h4>
<ul>
<li>✓ نه فقط کلی نگاه میکنم ببینم راجع به چیه.</li>
<li>✓ کلا حوصله ندارم ببینم اینارو</li>
<li>✓ کامل میبینم. دونه دونه فرایند ها و تصاویر و عناوین و متن هاشو.</li>
</ul>
</div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر لینک پستش رو میذارم. ولی حرفم خود تصویر نیست.  بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/823" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHV-CPdZzNCy-ccGFCSeApxjh58LLkEyY-52i2sGYC54R3u7qvFJto3qPvHEnVtm1qLN69gD-rh3KXWFdmaktPDpTwqhYr9L3_a9Qvag6qzSXv2xjWMV9dH14Fh96j4YJ5JcIGQjki5wFq7wG98mcrTkWj7yFJTe0yWEW2McTqhsjPMX1jPWSI0LfN_wAlB7TrwzAfrHMdLmJGogX-7I3HcKKaCtxnnsV8Z6I8DIzUBxRVoiwL_2LcwgXTkD3wZ9riumIieTJWHw5WzgOffCnENRENZAnQhLTjrgX__0tatlvGKm9rDUh2FvI1E-0Up1jzB805U-NcDxk6Eke4yYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر احترام به حقوق تولید کننده تصویر
لینک پستش
رو میذارم. ولی حرفم خود تصویر نیست.
بعد از نظر سنجی پایین، چیز دیگه ای میخوام بگم.</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/mohsentavoosiseo/822" target="_blank">📅 18:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگر از داخل ایران وصل میشید، کشور رو یک کشور در نظر بگیرید و هربار یه کشور نشه. جوری نشه که انگار طی الارض دارید صبح آلمانید یک ساعت بعد آمریکا یک ساعت بعد ترکیه. (بیاید فرض کنیم پیاده از مرز سوئیس نمیرید آلمان و بین مرزهای شنگن در حالی که کلاد رو باز می کنید).</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/mohsentavoosiseo/819" target="_blank">📅 18:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کاهش احتمال مسدود شدن اکانت Claude
بجز اکانت گوگلی که باهاش تو کلاد لاگین میشید و بجز کارتی که باهاش پرداخت میشه،
اگر از داخل ایران وصل میشید، کشور رو یک کشور در نظر بگیرید و هربار یه کشور نشه. جوری نشه که انگار طی الارض دارید صبح آلمانید یک ساعت بعد آمریکا یک ساعت بعد ترکیه. (بیاید فرض کنیم پیاده از مرز سوئیس نمیرید آلمان و بین مرزهای شنگن در حالی که کلاد رو باز می کنید).
و چک کنید وی پی ان رو با یک سایت تحریم(بدون شکن) مثل
https://developers.google.com/search/docs
که 403 نده. اگه سایت های فیلتر براتون باز میشه ولی 403 میده این ها، یعنی به راحتی وی پی انتون قابل تشخیص هست که از ایران وصل میشید.
همچنین توی  incognito یا private mode مرورگر، وارد سایت
https://whatismyipaddress.com/
بشید و ببینید کدوم کشور هست آی پیتون.
من چون ایران نیستم خودم دست به تست نشدم. ولی همونطور که قبلا گفته بودم، کشور وی پی ان، با کارت پرداخت کننده اون حساب، باید بخونه. معمولا خرید مستر کارت مجازی همون کشور، راه امن تری هست. ولی روی کلاد تجربه ندارم که با این کار هم باز میبنده یانه.
چون اغلب آدم ها حوصله ندارن وی پی ان و مسترکارت مجازی رو خودشون بخرن بزنن. میدن یکی پرداخت کنه. همین خودش باعث دردسر میشه.
به شرطی که سایت پرداخت کننده هم، اون کارت مجازی رو قبول کنه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/mohsentavoosiseo/818" target="_blank">📅 18:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تفاوت کلاد در چت بات(پایین ترین سطح استفاده از کلاد):  متأسفانه لینکی که دادی به خاطر AJAX فیلتر می‌شن و محتوای واقعی سوال‌ها رو نمی‌تونم ببینم سیستم فیلتر کردن با JavaScript کار می‌کنه که من بهش دسترسی ندارم.  اشاره به همون بحث همیشگی SSR در سئو(https://…</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/mohsentavoosiseo/817" target="_blank">📅 14:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تفاوت کلاد در چت بات(پایین ترین سطح استفاده از کلاد):
متأسفانه لینکی که دادی به خاطر AJAX فیلتر می‌شن و محتوای واقعی سوال‌ها رو نمی‌تونم ببینم سیستم فیلتر کردن با JavaScript کار می‌کنه که من بهش دسترسی ندارم.
اشاره به همون بحث همیشگی SSR در سئو(
https://t.me/mohsentavoosiseo/267
) که گفتم فاز لبه تکنولوژی برداشتن بر ضد پول و به ضرر خودمون هست.
هوش مصنوعی های دیگه نمیفهمن به خاطر جاوااسکریپتی لود شدن با Query string نشون نمیده. این عین انسان میفهمه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/mohsentavoosiseo/816" target="_blank">📅 14:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مباحث امنیتی(امنیت ایالات متحده)</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/mohsentavoosiseo/813" target="_blank">📅 14:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صحبت خارج از موضوع کلاد:
چون خیلی شکایت میشنوم میگم. وگرنه جالب نیست بگم. چون اون ها هم بهرحال از دوستان من هستند. میگم که شاید تغییری ایجاد شه.
از ل............ت برای احترام اول به اعصاب بعد به پولتون توصیه نمیکنم خریدی انجام بدید. آدم های خوبی هستند. اما چون همه چیز دست مدیران فنی هست و ذهنشون همه چیو فنی میبینه و با ذهن تکنیکال غیر تجاری میخوان مشکلات رو حل کنن و تصمیم گیری کنند،
در مدیریت فرایند سفارش ها به مشکلات زیادی میخورن و بعد میان موردی دونه دونه حل میکنن.
افتادند توی لوپ و حلقه بهینه سازی(بازم فنی) که دیگه یک بار برای همیشه درستش کنند. چند ساله. اما گاهی باید ورود کرد دستی کار رو جمع کرد. باید هزینه کرد. بیخیال سود بیشتر شد و به روش غیر فنی، فعلا شرایط رو درست کرد.
بماند که در تشخیص فنی اینکه مشکل کجاست هم اشتباه میکنند. چون فقط از یک زاویه دارن به مشکل نگاه می کنند.
همون چیزی که همیشه میگم مغز صرفا دولوپری و غیر تجاری،
1- یا ایده هاش شکست میخوره،
2- یا نمیتونه بفروشه اصلا و جمع میکنه
3- یا نارضایتی از محصول یا خدماتش ایجاد میشه که نمیتونه حلش کنه(این ها سومی هستند و حداقل تو یک و دو گیر نکردند).
این نکته برای خود اون کسب و کار و کسانی که دریچه دریافتشون بازه، میلیون دلاری ارزش داره. باید میلیارد ها تومن یا صد ها هزار دلار از دست بدن تا این بازخورد رو از زبون یه مشاور که ایراد کسب و کارشون رو میگه بشنون.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/mohsentavoosiseo/812" target="_blank">📅 14:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
❗️
🟢
درباره معلق شدن اکانت های کلاد
موجی که راه افتاد ظاهرا همه کسانی که از سایت ا.........ت خریده بودند suspend شدند. اما از گزارش هایی از ساسپند شدن غیر از ا.......ت هم هست.
برای ما نشده. لاگین از ایران هم داریم با وی پی ان. و لاگین های ما از چند کشور هست. ولی هربار کشورش عوض نمیشه.
پرداخت هم از یکی از کشور های ثابت اتحادیه اروپاست با کارت شخصی. با کارت زراعت بانک، ایش بانک و وکیف بانک ترکیه و ورود از ترکیه هم مشکلی نداشته.
مکالمه ما هم فارسی هست اکثرا. ربطی به زبان شما نداره. حساسیت اصلیش روی پرداخت کننده هست و هویت پرداخت کننده.
چون بحث احراز هویت سنی و مباحث امنیتی(امنیت ایالات متحده) توش لحاظ میشه.
اکثر ادم ها هم استفاده های سنگین ندارند. حتی از skill و connector ها که پایه ترین و ابتدایی ترین قابلیت کلاد هست استفاده نمیکنن. فعالیتی که توسعه کد سنگین تو گیت هاب به صورت انلاین و مواردی که میتونه منجر به استفاده عمومی بشه رو بهش حساس تر هست.
اما خودشون میدونن دقیقا رو چی حساسن. تو متن خودش هم نوشته موارد خاص و این خاص رو تعریف نکرده.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/mohsentavoosiseo/811" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کسانی که گزینه "خوشحال" رو زدند که از جایی با قیمت خیلی کمتر به صورت اختصاصی میخرند،
ممنون میشم دایرکت پیام بدید(آیکون یا کلید message همین کانال) و من رو هم از این نون سهیم کنید
😒
. زشته کارتون که مخفی نگهش داشتید
😏</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/mohsentavoosiseo/810" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-poll">
<h4>📊 اگر من ابزار های اختصاصی(نه اشتراکی) هوش مصنوعی رو به قیمت دلاری اصلش ارائه بدم با حداکثر 10 درصد بالاتر، هر ماه حتما تهیه می کنید از من؟</h4>
<ul>
<li>✓ صد در صد بله</li>
<li>✓ 10 درصد بالاتر نه. معادل دقیق قیمت دلاریش باشه صد در صد</li>
<li>✓ نه. فقط اگه یک کم ارزون تر از معادل دلاریش در بیاد میگیرم. وگرنه نمی گیرم.</li>
<li>✓ من از بعضی AI ها رو از جایی میخرم که خیلی کمتر از قیمت دلاریش در میاد. اختصاصی هم هست و خوشحالم.</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/mohsentavoosiseo/809" target="_blank">📅 15:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درباره این ویس و اون سوال، اون سه راهکار (ادز و کانال های غیر کیوردی، کیورد ریسرچ عمیق تر و out of the box و تغییر استراتژی محتوایی)، اگه همچنان شکست بخوره، جواب نده یا نصرفه یا توان هزینه کردن نباشه،  دیگه باید بوسید گذاشت کنار دیگه. سود ما تسلیم شدن به موقع…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/mohsentavoosiseo/808" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/mohsentavoosiseo/807" target="_blank">📅 00:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/mohsentavoosiseo/805" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">https://www.instagram.com/reel/DaNzmW8MtPF/</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/mohsentavoosiseo/804" target="_blank">📅 20:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">https://www.instagram.com/reel/DaNzmW8MtPF/</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/mohsentavoosiseo/803" target="_blank">📅 20:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">من احساس میکنم آموزشی که جناب طاووسی میدن برای این مدل بیزینس ها مثل سایت ما یه آپدیت نیاز داره که نیاز هست برای سایتایی که کم محصول هستن و محصولاتشون قابل تفکیک و توسعه به صفحات مختلف نیست چیکار باید بکنن؟</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/mohsentavoosiseo/802" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سوال یکی از دانشجویان دوره از پشتیبان دوره:  من یک سایت در زمینه فروش پلاگین های وردپرسی دارم. کلا نزدیک 13-14 تا محصول بیشتر روی سایتم نیست مشکل من اینه که توی مثال ما یک لندینگ بیشتر نمیتونیم بسازیم اونم برای خود محصوله.سایر صفحات میشه ویژگی های محصولمون...که…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/mohsentavoosiseo/801" target="_blank">📅 19:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوال یکی از دانشجویان دوره از پشتیبان دوره:
من یک سایت در زمینه فروش پلاگین های وردپرسی دارم. کلا نزدیک 13-14 تا محصول بیشتر روی سایتم نیست
مشکل من اینه که توی مثال ما یک لندینگ بیشتر نمیتونیم بسازیم اونم برای خود محصوله.سایر صفحات میشه ویژگی های محصولمون...که نمیتونیم اینجا صفحه لیستینگ بسازیم و مجبوریم بلاگ ایجاد کنیم.
اگه بخوام مثال بزنم مثلا پلاگین woocommerce gift داریم که براش یه لندینگ ساختیم و یکی از ویژگی های این پلاگین BOGO deal هستش..خب ما اینجا نمیتونیم یه صفحه لیستینگ بسازیم که در مورد BOGO deal باشه و فقط یه پلاگین توش باشه..نمیتونیمم یه لندینگ جدا برای BOGO بزنیم که اونجا پلاگین رو معرفی کنیم. مجبوریم یه بلاگ بزنیم که در مورد BOGO حرف بزنیم و نتیجه این میشه که کسی که توی حوزه ما یه پلاگین مخصوص فقط برای BOGO deal زده باشه میاد بالاتر از پلاگین ما قرار میگیره و ما هم توی برنامه مون نیست که بیایم این ویژگی رو از دل پلاگینمون در بیاریم و یه پلاگین جداش بکنیم. در نتیجه توی نتایج در صفحات عقب تر دیده میشیم.
یا مثال دیگه یکی از ویژگی های پلاگین ما Buy X Get Y هست که این کلمه خیلی سرچ میشه. ما نمیتونیم اینو جدا کنیم از پلاگین و یه پلاگین یا محصول جدا بدیم ولی رقبا اومدن یه پلاگین نوشتن فقط buy x get y انجام میده و اون الان بالاتر از ماست توی نتایج در حالی که این یه ویژگی خیلی کوچیک از پلاگین بزرگ ماست.
وقتی هم بلاگ مینویسیم برای این ویژگی توی بلاگ مجبوریم اینفورمیشنال صحبت کنیم و از روش های مختلف غیر از پلاگین خودمون هم حرف بزنیم که بتونیم با رقبایی که فقط بلاگ وردپرسی هستن رقابت کنیم. در نتیجه نرخ تبدیلمون خیلی کم میشه.
من احساس میکنم آموزشی که جناب طاووسی میدن برای این مدل بیزینس ها مثل سایت ما یه آپدیت نیاز داره که نیاز هست برای سایتایی که کم محصول هستن و محصولاتشون قابل تفکیک و توسعه به صفحات مختلف نیست چیکار باید بکنن؟</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/mohsentavoosiseo/800" target="_blank">📅 19:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سوال زیر رو 99 درصد آدم ها متوجه نمیشن. ولی تو جواب، ساده توضیح دادم سوال، چی هست.
مخاطبشم اکثر آدم ها نیستند. اما نکته های توی جواب، از نظر باز شدن ذهن، به درد همه میخوره.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/mohsentavoosiseo/799" target="_blank">📅 19:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انقدر که رو وایب کدینگ مانور میدن تعجب میکنم. البته درک میکنم. بازارگرمی خوبیه برای اینکه کسی که خبر نداره بگه wowwww برم ببینم چیه.
vibe coding - وایب کدینگ
یعنی به هوش مصنوعی بگی چی میخواد برات کدش رو بزنه. همین! یعنی هوش مصنوعی به عنوان نوکر کد زن تو باشه. یعنی nokar coding یا vibe nokaring
😏
حالا میتونی روی پرامپت خوب زدن مانور بدی که اون دیگه ربطی به وایب کدینگ نداره. برای کار با هر هوش مصنوعی هست به صورت کلی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/mohsentavoosiseo/798" target="_blank">📅 17:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگر فروش اکانت کلاد، جمینای و سایر هوش مصنوعی ها رو دارید، و همینطور ابزار های SEO،  من به عنوان Reseller شما و شما هم تامین کننده اصلی، میتونیم همکاری داشته باشیم.
فقط با کد تخفیف و این چیزا کار در نمیاد.
ممکنه کد تخفیف بزنن سری دوم نزنن. و ممکنه یک ابزار بخره کاربر از طریق من، ولی بعد سری دوم بیاد ابزار دیگه ای با همون اکانت بخره. لینک affiliate خالی هم فایده نداره. مگر اینکه کوکی خوبی براش تعریف بشه.
اگر یک ساز و کار عادلانه و قابل track خوبی وجود داشته باشه، میشه همکاری کرد. تقاضای زیادی سمت من میاد. به خاطر سود بسیار کم و تامین پردردسرش، من نمیخوام خودم ورود کنم به کسب و کارش کلا که کلا خودم بزنم. در حد ریسلر فقط میخوام درگیر شم.
کلا به خاطر track نامناسب یا عدم اعتماد کافی یا ثبات نداشتن آدم ها یا کسب و کار هاشون، تا حالا همکاری جدی reseller نداشتم.
اگر فکر می کنید میتونیم همکاری داشته باشیم به دایرکت همین کانال، پیام بدید.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/mohsentavoosiseo/797" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوال:
من 20 میلیون تومن پول توی بورس دارم. بفروشم سایت بزنم؟ سئو هم بلدم.
پاسخ:
سئو با 20 تومن در نمیاد. میشه 120 دلار! میشه 5200 لیر.
شما هیچ کسب و کاری رو با 100 دلار نمی تونید به سود برسونید. پول میخواد. با هر استراتژی ای حساب کنید(کیورد های کم رقابت)، باز هم با صد دلار به فکر راه اندازی کسب و کار نباشید.
در بدترین حالت، کم رقابت ترین حالت، حوزه خیلی خیلی خاص یا محدود شده به چند مورد خاص که سوداوری خوبی داره(بعد از تحقیق مفصل کلمات کلیدی)، مثلا در حد کیودری مثل "خرید فلان ماده اولیه" که اون مواد اولیه برای کارخونه های خاصه و شما هم مثلا آشناش رو برای تامینش دارید، رقابتش صفر یا نزدیک به صفره و خلوته ولی سرچ کننده ها مشتری هستند و پرداخت خوب دارند و نرخ تبدیلش بالاسات،(چون مثلا کم هست کلا)
در این صورت، با ماهی 200 دلار(نه یک بار 200 دلار)، میشه امیدوار بود بعد از 6 ماه شروع کنه به درامدزایی. در خیلی شرایط استثنایی، 3 ماه. شایدم اگه کیورد خاص پرسودی باشه مثل مثالی که زدم و هیچ کس هم کار نمیکنه و جنسشم جوریه که شما میتونید تامین کنید راحت، شاید خیلی استثنایی بشه با همون یک بار 200 دلار. بشرطی که از قبل بدونید. نه اینکه تازه بخواید شروع کنید تحقیق کردن.
روش دیگه ای بلدید؟ میگی نه! رفیق من فلان کرد و فلان؟ حله. من بلد نیستم. از رفیقتون بپرسید. نه بلدم نه آموزشش رو میدم.
شما اکانت 20 دلاری کلاد نیاز دارید حداقل. دستی هم انجام بدید موقع Off-Page نیاز دارید به هزینه کردن. خیلی چیز ها هم هزینه پنهان هست که به چشم نمیاد. مثل زمانتون که داره میره و از کار و زندگی مفتید. ماهی 40 میلیون تومن از دست میدید که سال دیگه تازه شروع کنه به درامدزایی.
سئو پول میخواد. رایگان نیست. ابزار هاش هم رایگان گیر بیارید، موقع Off-Page، پول میخواد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/mohsentavoosiseo/796" target="_blank">📅 14:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مشکل ما با کسانی هست که سوال نمی پرسند از پشتیبانی و خجالت می کشند!
آپدیت مفصل سئو بین المللی بیاد که خیلی فشردست اون موقع هم میخواید سوال نکنید؟(دانشجویان دوره).
کی دیدید التماس کنه بیا از پشتیبانی استفاده کن! 60 هزار تا سوال بپرس! هرروز! هر ساعت! ما طبق زمان بندی خودمون جواب میدیم. ولی شما که میتونید بپرسید!
آگر تو دوره باشه و مشخصه که ندیدید، ارجاع میدیم به ویدیو دوره، بهر حال یه کمکی می کنیم در حد تعهدی که مکتوب دادیم(نوشته شده موقع خرید). ولی از سمت شما واقعا نباید مراعات و شرم وجود داشته باشه!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/mohsentavoosiseo/795" target="_blank">📅 12:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چالش رایج دیگه ما!
آدم ها خجالت میشکن. فکر میکنن کنتور میندازه یا سهمیه ایه سوال پرسیدن! (پشتیبانی دوره رو میگم. نه دایرکت خودم).
مهارت سوال کردن، مهارت طرح سوال وقتی که جواب، دقیق به جواب ما نیست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/mohsentavoosiseo/794" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
