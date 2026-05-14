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
<img src="https://cdn1.telesco.pe/file/XI5Y2sjaKL13BreaJtNrdGy3ua9KegB8lE54AWIVOmgj33mhRRTDWYsrdYlW4mXq59qNbpIzzKeo4MBL5jS5aKMkJhjeUEHMrYZJyXVe6SKJ1ONIOZ3gmNDs_QLp5pCu9f88lNUG71AJuF6i7TuyR9Bs0CtjOCyvmbeZcg6MHD1HSkEuaComxlUa8Hn7JBeCq5RpXcCp3Frkrej8_aMl3HSw9kWZDgmZREWf7Pz4HkYac-nRPF2LCvJmq25Uo9_TsnlacHPKR-FPnm_74sJ6wpC18ZOTzToudAzKC_OpjlZNLRyQalY9l0P9LYK_oJ60Og_pHLVS1vIV-acjEetkwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 93.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 21:13:13</div>
<hr>

<div class="tg-post" id="msg-2335">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AwLGWLrZGR2M_NvSpE2qZmraGoVOTk4OWVkZPb8fdn5RLNKIc9XptsPi-iIvYXbPs3AxWQf5RkXXDCjqzTeYY61ajtWOXN25hVdG5OxbiT38yReqDdON-d6y04HP-A1_2Mgb8L_-7sNWcuzxC21IWAZJjRZmgpkLJs10BCHhvpyMd9KSSUPyH7jDJm-_cS7gpT5R3Vo6NNN8kdWgZTID5KawkGmVHAnMwB6e5i-dTvhFxYFewm0bXC8_knEx3S0Wj-jXGe49TXRNBs0QmuGECEiP0YAdqtri_xnCFuQHidZ9TYq7yYJXq1tHZWvFq3-BHYcjfkNjjlX6nNS9eV9Uaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش
MITM
در آپدیت جدید از اپ اندروید
#شیروخورشید
گنجونده شده و می‌تونین بدون دردسر ازش استفاده کنین.
برای استفاده بعد از نصب یا بروزرسانی، باید وارد Options، سپس More Options و بخش Connection Protocol شده و CDN Fronting رو انتخاب کنین.
همینطور در قسمت CDN edge IPs اگر IPهای وایت‌لیست شده
Akamai
رو بذارید، سرعت اتصال بهتر میشه.
👉
github.com/shirokhorshid/shirokhorshid-android/releases/latest
💡
t.me/PersianGithubMirror/4954
©
PawnToPromotion, mahdavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/ircfspace/2335" target="_blank">📅 16:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2334">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نحوه اتصال رایگان و نامحدود به اینترنت آزاد با متد ترکیبی MITM + Psiphon
👉
github.com/patterniha/MITM-DomainFronting
©
patterniha, MatinSenPaii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/ircfspace/2334" target="_blank">📅 16:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2333">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">روز هفتاد و ششم از قطع اینترنت.
معاون دفتر پزشکیان گفته "درصورت برگزاری همه‌پرسی، مردم امنیت را به اینترنت ترجیح می‌دهند".
وقتی گفته میشه هدف از قطع سراسری اینترنت و خاموشی دیجیتال مسئله امنیت نیست، دقیقا مطرح شدن همین اراجیفه که به جای نظر مردم به افکار عمومی تحمیل میکنن.
زمان زیادی از کشتار دی‌ماه نگذشته. به جای این چیز خوریا، بهتره یه همه‌پرسی بذارن تا وضعیت مشروعیت جمهوری اسلامی دستشون بیاد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2333" target="_blank">📅 09:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QiW0E4CURtabm8ZUInI5sz0WYqptl0WoEWkUzbxcutG8WFr3wfW20Ul3kT3ctR5E1GdJfHyYWE8Uv-p_Wt_dd-NtXF2lPVt7IwU0n6jUgXo2789eaQu-2uy6WTg-InHVGeBoJavAMOKfarWgfuq05H8YaB-4a4JWbnkugivgt9tz7xx8K1S1BdTXSYVRcrJwcuSpMQ5Q1kthGyYkPZAoV6SHoHa6MxFMUq-C4QfcCFU1_cIjdlES-7C6sm53euRKXvZ5De9ljFRjj2KAjTIfD0TVXOevTFGwf__nWHpqfxwCLziNt58YceAGUkbb6IgxwHTmMSWe6rZwHcEduU0Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون فرهنگی مجلس: امروز پیامرسان‌های داخلی گوی رقابت را از پیامرسان‌های خارجی گرفتند.
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2332" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j1brmuJexlNt1n4kn6UImebsi1c1ariXBohXTbs7GwUE0f-UZFwwr2wpP45bQ8LZ5zMHwuBQ0zdfgG-YPa9OZwLxsQS1p9woPaHjkfx7tVZbZJUVzhRD2ifZxZypMZlvick8VI68pWXsD0UiIyWpPRnULTLfV5U0cvRfKkYYnUREsQwZ6-s86jz9333FBYHZHD7tmSAPv549rvMlCxRBDjnY2vJO-2Kg1d0x_pNVq4ogbLCeEbXP5siesOdMuZqTxjJJN9aH7BmbIDPs_gp2wEYzn7oZz-bMgLbf7M_rdCIQ73S9FWcwIqBCTyQvtzBFifeyQYlyPUqFP_xdrJLhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ روز از قطع اینترنت گذشت؛ همزمان درآمد یک کانال فروش فیلترشکن از ۱ میلیون دلار گذشت!
©
mosi115
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2331" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XZmACDBqm8QmqMInWNku0FtoGh52X0RYOZ6NOcLLMhgrNjC0UrVIP07VjCo1XLuHIW9gLFEPo7ffhv6wQ7GaCC5Rt19YzzFYoaHX7Umze58DlAx75U2WZojrwPRbpeq_y7Ho1ecvA5DoeQ7joB2HRc1Fb5GPJZQ_MxeddlTwodaMPCzNLYil27aosxAnMMIjGlYSLi4xMYh35Yy3gmf_GM5fvfMQcOLmyNFiS7rODMNR3UvhpTVOagtbp8-nsMQIZE9dPwRUxSqqiJYxZa2GuIsO0thK4-x0iY1-hEl9cd0Yd1y8zZuG110SIlx_0Up9VkCt3RythnTlI086o6TY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میاد مرحله‌ی جدیدی از
#اینترنت_طبقاتی
شروع شده؛ دیگه خجالت هم نمیکشن. قدم به قدم دسترسی برخی افراد و کسب و کارها وصل میشه، تا عموم مردم به عصر بدون اینترنت و بدون هوش مصنوعی برگردن.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2330" target="_blank">📅 19:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سی‌ان‌ان در گزارشی نوشته
#اینترنت_طبقاتی
در ایران خشم و نارضایتی عمومی رو شعله‌ور کرده و به نمادی از نابرابری ساختاری در جمهوری اسلامی تبدیل شده ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2329" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قوه قضائیه در یک کشور مردم سالار آنجایی که حقوق مردم با تصمیمات دولت یا نهادهای امنیتی نقض می‌شود واکنش نشان میدهد. در ایران رئیس این قوه نه تنها حق مردم در دسترسی به اینترنت و کسب و کار مردم برایش مهم نبوده، بلکه چندبار شاکی شده چرا اینترنت پرو را سختگیرانه نداده‌اید!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2328" target="_blank">📅 19:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=sJlySgR2eoHvTDKb4wQruLKNNM6edI9KIZTv5nup9Lbs3KhLvJuTjHzH4-MyzXbEe04nTK24JpHxhuHGOyOgvcxLVYg8ZYVCW8dZt8rL2oKbKovCRUn-qxTiqKIO61Sav8PrAstzsXcP-Y8fAkoXJPLGsDwjQVCR1IdCG63hEc-3mIBdnHWEK0p8uPl60TBtfTQxWij4uV2dFF_Gj8M_NhgCnGZvyH7UE7LPdhWzMvvUulrsj-vqgOPylanQ95ywAGA-OrWjWRHq4ScACK3NEp7nRSGydx1c5E8eSw51CHwBvn5BXtD_O1sGAsWrVBAj8ZFgM5DxGKYBN-Q9zTSDjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e9b1e831.mp4?token=sJlySgR2eoHvTDKb4wQruLKNNM6edI9KIZTv5nup9Lbs3KhLvJuTjHzH4-MyzXbEe04nTK24JpHxhuHGOyOgvcxLVYg8ZYVCW8dZt8rL2oKbKovCRUn-qxTiqKIO61Sav8PrAstzsXcP-Y8fAkoXJPLGsDwjQVCR1IdCG63hEc-3mIBdnHWEK0p8uPl60TBtfTQxWij4uV2dFF_Gj8M_NhgCnGZvyH7UE7LPdhWzMvvUulrsj-vqgOPylanQ95ywAGA-OrWjWRHq4ScACK3NEp7nRSGydx1c5E8eSw51CHwBvn5BXtD_O1sGAsWrVBAj8ZFgM5DxGKYBN-Q9zTSDjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هکر بودین و میخواستین بانکهای جمهوری اسلامی رو هک کنین، سرورتون رو کجا میذاشتین؟
علی کیافی‌فر، متخصص امنیت اطلاعات: در جنگ دوازده‌روزه، نوبیتکس، بانک پاسارگاد، بانک سپه و بانک مرکزی از داخل خود ایران هک شدند. مثلاً نوبیتکس توسط یک سرور زامبی واقع در یک مدرسه‌ی علمیه خواهران قم هک شد.
قطع اینترنت امنیت رو کمتر میکنه و نه بیشتر. سیستم‌ها نمی‌تونن آپدیت امنیتی بگیرن، سرتیفیکیت‌ها expire میشن، ابزارهای دفاعی (فایروال، آنتی‌ویروس) از کار می‌افتن و هکرها (داخلی یا خارجی) راحت‌تر کار می‌کنن، چون نظارت و لاگ‌گیری مختل میشه.
©
farhad_mottaghi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2327" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THkhF3yckfGqqv8xYdh1EH-LGe6zhE1RLTIL27RmvcZYblmM0igmnp0SCUx2WUeIPrMZTp3sWcglxdJlQsK7y_n8DGu4JXraAewsasE5mcToUCm_M8BSfUAMM1QfSdgW4NNegj7Bw2HY4yXg8SBIzqXs3qD_-YpOk2XmhFHJWjERKbpUvTd0l2kESGVwgnVeIpP-Gq9aY17vPcNsj_8kzkyPdNL-JuJiY2IazPOJa9PRessQRWpdhBsDvbl7lDSMew4XevJpe1VAo5lmUBhuzjfWaVSWoBNJk0gWQtZk8aWVD9uUjNJOmPbHfQ0ME1Dj54SA8uH0XT5mEA1BwKz3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگهی یک دفتر پیشخوان دولت برای فروش
#اینترنت_پرو
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2326" target="_blank">📅 19:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F5Ppl6wLkK25nGss-Wt_dWJbWmvW9RP94Lu_YMCBbvKPL9JBa8Bh-9SEWMkwIVE9iXzz1LDOj8vCWxzQ57OW7EcYbVSj1hnob0F9vG_aIDuJ0lfzSrViPc_Gl7lqpaNKnbQKbrzsatNDFlRd4Jji3YUtRNT9yAvsYY3X8QNNxlMrkooHgCurUS5cuIEGZnPnxcekPJe6eiVIVYGd1UUACGtunJ52NRhWOaAMzLk7OcinAxhOlhWF52lLIyGgy-KUiCidavP18ou2Csjdp13qyhaE8_crCoihscMyS-U8FVOAzZB_iJGPeXqkIlsBN_ICAcel9EysTHYxR3wg4gfshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا دسترسی آزاد به اینترنت در متن سخنرانی‌های رییس‌جمهور و هیات دولت برقرار شده!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2324" target="_blank">📅 10:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تعداد کاربران اینترنت پرو کمتر از نیم‌میلیون نفر است!
تا امروز یک اپراتور با ارسال بیش از ۴ میلیون پیامک، برای بیش از ۴۵۰ هزار سیمکارت،
#اینترنت_پرو
فعال کرده و اپراتور دیگر با ارسال بیش از ۵۰۰ هزار پیامک، حدود ۴۰ هزار کاربر پرو فعال دارد.
©
aghplt
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2323" target="_blank">📅 08:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HTw3eKHepGTYcSBL2t3sw9Rj3tNQZOU92HZhNTjukpiaFFtKom-VIcdCRPLj_1YFCl5Kxvvlkp7j-Lc1MAmFHBGmwBgeLF5T28MkhipDo8N2DvPuyeP5sd5Lfvkc_qh8pgCAAPfsPgRHyywBG9i5GNEutzcWsXezjwxsi5SSq4gGhiqFVC25swTYeQoMKQMmMgVUXtjuBEl8cQcK_hkGuGqWrJ6BBfOFxDrHrQIAUiNiZJRKrgDWwf8UI4df59btUBqf8rmsiLrc8t35iOl_X2-yuczVQ31QV4laY5-Gm48iUsIWUCQx1yzPbGviv00FSjzmJRgNz0nGx8Ey3Vk0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن مهندسان نفت برای دریافت
#اینترنت_پرو
واجد شرایط شد.
۷۵ روزه اینترنت رو به بهانه امنیت به روی میلیون‌ها ایرانی بستن و هرکی که کار و زندگیش به اینترنت وابسته بود به خاک سیاه نشوندن، تا
#اینترنت_طبقاتی
رو اجرا کنن. مدیونین اگر فکر کنین کیسه دوختن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2322" target="_blank">📅 08:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بدتر از قطعی اینترنت فکر اینه که سالها درس خوندی، دکتر و مهندس و محقق و پژوهشگر شدی، بعد واسه کار علمی دسترسی به اینترنت بین‌الملل نداری؛ اونوقت حمید رسایی با حول و حوش دو کلاس سواد برات تصمیم میگیره تو اینترنت نداشته باشی، تازه خودشم تو ایکس وله!!!
©
NiHa_Mehr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2321" target="_blank">📅 08:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pTOLVOZ9sLESQRqH82lVizMBH9QZCy0xlZlspEq7BzAPyBxqO8xwjPEvfw4CuzdEceo4y7YZz-Tv1QD9Oafi-PCXo8HWOVY_rYDt4RcCzJ__TvTAtUCFqKN_9U28rJinhGr5d75WXcl7eInkc5TAqCmsEq63aZJODxFjLOdAbYsw9bBaQuuPPC6kgLOcCjelkE2HQu478BjL4vcttk8qrtV0aX8hNWWtGPiU-PaAqsR9Jwms31rETL7kR8L7Fm0DpCwi1BR8O3UxLDhQ6g6yaySuU4ZM_6mwk_PFRgyMxurEbPgYPJ8fhy77JC1It9vnb74ccX9lbBrUzTd95Hk2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس قوای سه‌گانه کشور در واقع ۴تان، که یکیشون به نام
#قوه_عاقله
نه توان قانون‌گذاری داره، نه زور اجرای قوانین رو، و نه در جایگاه قضاوته. مهم اینه که قوه عاقله قصه ما با
#اینترنت_طبقاتی
مخالفه و قراره نقش اپوزیسیون داخلی رو در این مضحکه بازی کنه!
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/ircfspace/2320" target="_blank">📅 18:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKO7uATy23vg9csE7pK3XXnpR1zVDpqHgIg1Oi8jUqTgvnf0FSbBq45ZYpaSFiYIkFO0gV5OAEg4SyjWCzvBjMxfPBo6PWglqwACRbKdbS8E-nRwcOT0vCvWA0p8FIQt1I0eFeWuiROzvn3Lb0IdHGqJsTuhUfPMbkymGQrJDEodSRA1evYnZBdtfTR-wrMEqHV6ZPgN28I_3-FkXu67L5E5BBfHJuR4ppYrtjNb4DHAy_yIlfRqMs-96Va9YbVlT1fAp1oYTVvFZ0BGUimdL42xRRw7F6JPItjdekY8m4IznjzpRZ_0X0tLb_ekZjpuuXDRfwgnjU6RkrAIClb_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای
#اینترنت_پرو
به اتحادیه صنف اغذیه‌فروشان و مواد غذایی باز شد و حالا با ارائه پروانه کسب و کارت ملی میتونن از
#اینترنت_طبقاتی
استفاده کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2319" target="_blank">📅 17:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g7XSRVNGgsHWPvs1n0KYbWS8VhX7RpbG5ZpDdi4PcE0IJzB_fi61ZNMF4LmgXRF6lHP6OZ5vZPHyZ75kZ5a25pCFG9iFIHXR3hoetrhelfZMjqKzLHbMM4UFynamwwW5b4MrVqIymP4dkf2-hRd-gulrR1ygwDSiKEfZ50QGAFwEMQuvN2xBdH5t7SrzdirbnTaluCYpTJ7VqRuckvrSZv9ZWi6xZ6yUhJzQOoIluiQPZg9I1L_vSsYen5CD3enM0gWK72UAHGLNYpROhNTC4I398rqfgcseN-4afd0nryMJn9RiwJE7Xrf-KVyT3bG9rs0rLdDTeVYZNm_nct5T8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jCF2EhqlUlh_yo1t6L-CJLKQBJXipwPMOhnTXHkq-avGNszg2vLKLMSh6ovJN0nP6A8PxJLBs3lkYBbULG_QKml-zxQApDgblrHTsKwrm7-D_I4vd8_bxPgXagb6LZ9BVChIsY35sIA6nt5s9_Hzyy6bnkcp8WTS9hr3Ehm2hKPjKyTORKUaJPVeHvpFpGmacRY4IChxA_GzqX1HCIVjYdfuaIi5ghlAW_-QgzB-H_GPgvGV4DAFRPdZI-6mwRxYY9y5xCBJXRi49VGWHrnCp9mzosKbtvOLGaRVQJ0SV95d4oHpcqfwUTfgWxeQvnkbH1Tib5s7yict0GZn1wHVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tc_e3gDAKfO650NG3UwLS7iAlC-FX0kCpkJhTzn73UAqMb9B2AI33t5or7fHRQA1tuVbEfeka032F2ryKInGijKTUFTwUqfY6t3W36sjVTPDsvQcXK4ZSZaevM31xC42mdOyNhn9Qy7zWxC-wUhbG3hINytoDpAdYdjK0TqtvCQNnpquIaiQP76j9dfS6_b-Z1wWnlC98cz_cnzmul5wNT4OZVofoQvM7aR-V-Mu7nJlXyfrz27ATWH6Wk3bP_dpeC36CvnIswB-z_zKu4n3vKyGH8uRfuSqfovUwRbmkwc6QYORyK8VvP_fg41MnTJ2BnGXqM2hCCWofinQ3bbDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BCw6joSow7NM3jApU57mSQDr_RbCd7I68c8-VetV0-wf9aHnHTczbTXoVsG0X8PitlcMm4UBnDGNBlapxvoZ6LiwP3nKUWNaP4n_c1gSOsEtaD_naTnqVKKo5o3rscdE13RT15hVtnPqS6V_Ft8NpXlpP32qmYdFs6qqFcp5GvnvikK1DGo2fuJjBg5ezkx80X0K1Vdt-b1uBvlkZbRJ-u0wsNkIH2cnX2S2aDFBAU2my0ID3EdZaNyY32oT0m9US3sCxHkTQ7x5geobC2B5z7AZRV79-4xSTfc7HPdlkTttSbB-5Pv3XQEOQdY99wQjlwmwcQPVYbsZ2Dp0R1_u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TAnJanLRwSEiSSfxg-1vfc3fuox235EnoW8D7O_oPpvfHzww7u7ohVAE2lsxmtkt7rQRV00KG-oQ9a6FEcdtddVzAEpfodtlfmkhVe1r3U7lStIk7exiBWYP1mg6rBON2wJbyGBUwYDSk476jt9KIQCYTlAHBw5oIFli7VseEX3sJAcdMrZeGMWVxUgS6b_H_XggEfNuHFDbdkwDHXiq8kR62Es8TphOiq-VwbGBu3sabpFacCLYssDXlCp_fEVMLFqH_AaRcaWeodQvb0WpP2NeakQrtwNsLhDmXsdA-nK_cUi6QMhEJeZaArdUd86ao_uyi45ZuTkFTCP1uJeH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MlpFIUDZehWIW9-Mt7yYjDxjCSSuUXzaWOnaLKQhHkhGKqLGpn930eP7e0QY4AyNv2DjtbTDvQ9toNKfGyBOS8NiPdQUcVIdyHxUnmqWU3lNzlwnuKQHqaTTemeZQxDXKBPz3ufH27Xoe0PJWFJkCOeR_fIOT7SyTdQVm76ueBTHChBVY7E8IRWIpBTp73nVBX8BGYANowyckPJi_t2p7hQ19xK8ZkzQ7b-KPzjVGTTOEhsWebBdR__GjqdSe1jz9Zu1He6zizuyGJan2NfzE4vzrfQi-4qEi-Dt6AYUBO5y3Ot5c7LIi8QszQOzv69I_sso0VQyJDzSjTIDj25Jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aFa1ku5N1UoldwzRNQCJzZe1w-fN4AAO7SQ_xrqgo1c5YTv79x5d6XC2bF-pNmUXb7yjhNPXhZZRhejgGafXv-ndvksbF2gf3t9U5iXnfZysQr7q6RMpdztTNq1DFLGiizSEeSsxnzjsY1QGfkJViCczeNELe4BtHKVAo6SXw2m5lV1Z6Xhjj_s_zLaeHdutTCMO39qkO_ru-0evVn4qsFMivP5xI-z5sMrfOaIJc615jzmeHkep1zG3PIXR58QSbz1CqtbJ1Lj9M8oMbVHTHu0RdziyJxbkj5hl2802SMKX_jlZCXKJfuLWs3yQtoNOOY39vEi8iogz0fKQfQaWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODZuAifkJIbCYnP6dRQvlQCgG0Kql4JfQ5Rhx00EuIxMgC54DGEj3ytgmV6BF6AwfKfsRV1xN8zRJl897s7Hegq5PyodAzUOqcd5JiYF4LitnbGPV3P--rZKMD1mXWVG3lXlbbWsjZKuDaiQUpjTI2nT6lgDd-UIqkzKe6BaPnTNFPupZ__fixvSSwK_1AE0PjxGunxtsLrLNCsRKUIzI68285Zx6KXAVPYbO11LEgutPsXGmx9ZlxI2oXBhfOMzt-CIr0fEHeXzmLGBIbWaH_U9KWjXa3nFcHAS15PsSbn8t-9zYLCripbdsJKe1B66GB9gPgim7A0PwMez5p_s_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FjJlKYYT111j0fyL0VTPPvKWaaLt93EYl0pIvJYwQdjOxzahcXU4T31dBsJfT3DbjqYucoEXRdIl_gKgqpnlzJz83aH08be9Nce8A6IEWsjOFu9lM5UIU4sSnnGYbVE_m6chfVmutTe90xQo9jVuxZUEpGVmMww_iKNFk99F00DIhc48PNfV97SRp6wFKbfCUzwXJgAntuzHy8Z7ayZZdgdjIpX2eipzN0uChPmnA4l1MW3w3FjyF2s_NxMRoKDy4rhDLMwn9Hj9W2gWdWt14qNAvdpBg3AeX1Fi9h4RVxLWnd3z3YcEwwpQq57cakTdb0lPGcC2iXXqdT2Gw955cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dH3qKZtXspTn2KRRRCfJ3sebgn_QO4x4UCocGnMg6cCrEP93yyZXGmK5oCPOWiSWp6_leJUQiaK3kzPcebIlgNmWJkY7SmcAwirA-phBS4v9ZQssG09NbveJyFOt4Cc7Tgw-l9TqW590chiq2AexTMZzTIGmCAxb0zLtv2kzc4ZRFKHhCKIHoes_x8Nm3maiV3x6YZrGVwHiZnz9WClvbRcpALOTLQerY6itZdKVyF6LbpV60c5WIKUY6CNfgZxvKOnaEt9Q1YmXteER_oakKdogoX1-_66ECgqc57tOnlDrlbIUHHjF8Jj4r7tpNd1OPNP_Uq-y2onLEb2XQOS-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cHtCL87LESdK0MCu98zBDX22EoEeEEEwLvg9_SbH5jwQMtLc0yLN-gYfxL3cEAcCpqCy2kft0ObkZELbxysf5b16ijj3aj6ejgefAVS7iK3KFODgoh8bP6w6uDOGQtTkoClXH8jIBzYmrPNyv1M9nRwZ6pHMpuuA801i1qrzLXkTTqCkeLkW_5GtYOKGQ-MJFneGBJ30UDJG6p-dh1nZyMpUA6dIIak51ZIFNw42XV0nLKtiHd4qtl6L7Xs77UA3w3GHvXLN_Pin8KTYBton-GsMmLqJCMyUVDtdDZQKuTxaWi2XvyDdANwEadkcbLgIXam5h4c6c8LI_GaAjPvn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lrQfRfziWVGWw_R1THhMgAopZ6I8oEUfw9I21-LnLXY71GNQc1ANy6ZNZ9rsazi3WFBvJzFRSNXDmjmy6Xl62-2Zf6BWPVhfSp-5eZ0_kM1Pkdac_GmvLZRLVVRyDFd1p4RMvQuIUU6fm34GvaiQI--PN4kMKreyO1b2mMUTTrYIS6OLmHMtOxMmNpLbmBngtZxTeo2BR_Lkor7TWCDLf0PaEh3nzRNJ5F4MHhpv7Ca9bLzs5kQt8lq2UofyxULP4fpyxJYZUb4W4uqDOBrt5TxxgQLOSmEskeqEFXIY64iAFfrazd1wbjth33Q0BQmFZf2iHOi01BgQ4gRKEbvT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iYyCTwknVPe-pLqvj8TVMOSeyYu5GtejRwHKsKiWeibLygB8ZTM2KDzna60iOx6KbREmAELuKllwJqjSS7gmoDDz63DRo4AGIuVHjVQ2X4JoZWjaSaM37QLdZv615O8R0Fr0wVaaCgF7VaQUJ1RCdaN3FR4rs-MuyrFi7cTEM5N6hAcHmxCcNeGBgX9cviDaeWmynFE7oMFEs19KQsU5VkuVwGYZjRJIjFNQbQHCm-2HfixxuYQU_COGk0CdEu7V6u7iZz-zzCaiejDWCUCMLsAtZQe25ft81VJMirIJL2a1ipth3gBhjFbSdNq5jcePYtjLLxxMcy9LoUVg3EH4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlZPYXmWy1lPYVKqhV2U7qYB03PiQ31Fzl_x1dZxGT6uTiGhdCtrtdClyOsR1jeahGFjxm_SMkXltrRrrNZiD72jLjzhQmSusPZhxLhZVyh5LJsnsb286iW4rfqsKIL3KqhHSs3oCRRzUYrx7fxo4NMbncau5JGzZi-FZOr-tnQ9ZnBkXkzYNZYY2ySUQ-nL8ZzcX7V6AhR86gpjwrJXWwzteFnjME5SQAKpfntNswK8VsX5JjzZDv9WPG8McJkJ1vMawjSCUVBrPtNocIuol_v9yfP3kF0xXrD_9mimsAS0fl_rQ_avRqFMTr2L5VXFnePMe3DNIQeBs4a_T9RTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZjsI2sHbzR7TwrhLIbNAFZgiNc5dSfSzkXeZsnvTmmyUuaXJmgPmHXU1Ys-9H4c39XaYHyINsZPD0sZwPEUS7pHomN3TFyUJudEmr0rbmsQGb2IDXNTmazbM_LU-WNsWn7BK8p_7zWTsueudjdA5NtoMa-y_oDmKqQstikvua_q64LKJEP9hL2qKT4c5xG8zHyRqR8uTEMrhr7pLxWIl1iFKZN_FYdVE7GJGe9G9zuvGIUdHaxd097-YMi2jEx0qdh9DXKHPDrbooHeu3q9ZhqElKKyq_yyod1lAdE2rN-GOm9uFNSaJHeF6t7iSOAE4UyanLIQLhoBH4x5q6zCX-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kP3ta5_PR7nYQp792bhKCZ4tt6408oNQ5tmn5uGdAaqeryWrvB5pf_ZxAdGBdK2P_VhkaCkzNJl2iIYBT24Gqemj6nu7aO7Skt-nAhl4Eyur-W4kogUS0V58NJDi2XqanvbrBGKvAH_70ZEzIL3JBrHb-rbN0hlDwNQBS7mElUfwudY8azqy83m7e9vC45RzaHH4ePu4w3jps8eY2bSfdWLayyQFf7VRqGYI8S2ajhyut_EWh1vY354ty9SrrVEemj3FJ50j4tSluncIaOM7nQULrmwsgkrIbdxLQbL-JjJ5fTV3cdghrJEd85xYzIYj_dl9XpgI4kbbR7n4viwKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTYznCQgZEejumvTXVCV9YO4ckCMd_9m7FSYNCMXprlfSbLxRTbKXUCVkXwK3Hod2ZrDjEFBksapa1SSWZlsWFefzILnT7_qnVFuRng4rHsFoqz_ecJR6oUY7IkGUgRCEKx_dq-xf-hCLBzCgA44KAhhjCKkPlCN7BL1ioUQ0g-03QGt7UpOmpQXOqcRKXsSC8_lrMZ5ZbuBEjkZQE-DDJE4sEZEiKU7JfGXNJxdAK5UQUFTYKNBOWO7jvt9D4bGnGvrd2vU0ocxfu4yshk_YkKN8rNYL9l3OWjNwaez58bslUfcAyd0GiXSJUdF0FWnVrEqktODpPRbsSf1OfqeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7W1R0aM0r55QNCxqdMJ4hBjclkIndTzzf2EuCKZD8LrAKVjwLxIEn5CiavVlTNNshoJoZ86pOy341YyH6-K9cZdk_VHNb5da7g0SqNPk0XChU1gK_LD2apqTFkwXC-FgtYmmv_zEXFClR9fCv6jGuAPlw0HFc_WP4VMFXhA2q9-j1nv8yWSt2DQ-HnBiqB_4b-04-NbjFHY4_uPykHGkWPZLhZidF_XUMBc-FL5RRe2-ryUTrepXna7KAYSIb7Z9MJs3MzSCai4-piwjg-dqOfN8nfcyiiRg-1zVyOMqQfhOz_M7viuGKynMx3K1CIRtRMAIi7Mf3g8p66lx96Wlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p8A--50RhGIFepVdUVNkxlWpJ4qSeOJeBKIIhiNYtmEm0jjjC3PAb24evXfUuBoHlAVKx-iroqUMkLTlO3Cu3UOKTdJn--ZTP8p9D31ET4wPXf5FxRhUm4XEyFwSkw4kxpiZuRzjzuAxl3QiI5fGXCB3ApnMimX9Fl2QlVXflEA7ZwSyIUnf0n7Ll8cLhQ-mrHdJsq0_ggwEodTSShqwWJ6xCrmDWoy7n-PRXPoSpKJ9Ou2b94Hq8JIFcO_k46VKtHC8hl1WuTdCwWAfg501Huc8XQMkAxq24OCRLt-8JZrmvVHAHyYSNyU1pT-es4svj5TrOZ31IcMQvxczpBdfHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IsEjfrxBZ1O76D-U3tc16sDD08mS7yGDHdCzCFsxJqyj4XKEAhKQ2d6omr5m3qDWdV4N4kESqsD5U2I7ud1AhpN-niFF4G2_oXojTZ9ny3UXeJirCxleQNMVTI7tObbxz38UzpGzDDufvCw6hMPuGbCkbhmMdopTS_F_HVurzPzxUce1E35ZjSHlLt94-4Zz-TbvgAQePZydeD_-KrwAtN8mcN7yiP4bbdH0Ri2ZdWH3mB80kXafCdx-CQl0SM3xZQ015a1_XyPcmBAzwBZYsZKS4q3EV6_1LTMSLslhKwq2c4wuisHHawsdNIMY_0KyynCj5TBNNYAVmu_jV9w6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=Df5fIQueHRx1oAO73ytzL4dbUB48NrcLKKI2e_wSp7HXtK0xe9K8u0RvytaDEqvQ-PwWenqFfELbxH-UPkG23anqHoycWyQK4xIzv4Ay_EtrGafGnxqSwWCQ2VRRNiChMqRBfQ5XbwPE6WfoCaRYp3r5Y7LwpBoNIe67_VgMUPtBUoNMgammrf9cT69psRJIqN52NE4RmCK-L-vB246WK_h1tcSIuIBmD61mpsZoBX4QtfKp6F9JLctwuYa4xznYJOmiAczmoR0a1zOLdUpo1HdE5eMTUpRE4NvnAvUq1WO40tR4lsqMN92LOCj6mzhbuU7rfbMCiGRFHGC5GDAlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=Df5fIQueHRx1oAO73ytzL4dbUB48NrcLKKI2e_wSp7HXtK0xe9K8u0RvytaDEqvQ-PwWenqFfELbxH-UPkG23anqHoycWyQK4xIzv4Ay_EtrGafGnxqSwWCQ2VRRNiChMqRBfQ5XbwPE6WfoCaRYp3r5Y7LwpBoNIe67_VgMUPtBUoNMgammrf9cT69psRJIqN52NE4RmCK-L-vB246WK_h1tcSIuIBmD61mpsZoBX4QtfKp6F9JLctwuYa4xznYJOmiAczmoR0a1zOLdUpo1HdE5eMTUpRE4NvnAvUq1WO40tR4lsqMN92LOCj6mzhbuU7rfbMCiGRFHGC5GDAlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R09ehERXJQ_x48pT5AFZm9XZIylZoN_OlmSIx_eJnhXqoiZGJLNhZE_sV3qrABTZ7DvjkkD0rOVPvd9Gydz-gKnbpwR7RTsmhZuYoE3KSNxYuMUKZLFepNHOvtAHxYnCycaHQRbEE2W12YzVBJriGA8E_JH3kFtrTZ57f4u1sk_kvof6dqBSj9_jUuNypbITGG0haF_mssvmbxBRgimCgbifz2DXSW-61y8K-M3uAdcopa4oEpxDNkJLuo5ujTho2peMaLMDhnHFdiBoPNM59Qu5aYWnvchAoGpyqHlAyegnMV7ppYTWXu3ArTTWgmligT4NuFnDDXn7QM9rKyx4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EABTiS9WI-scNtlgiEYcMGSKG5Bt4TI7-WmjcaDQONritcb6XpuDkkT5G_75RZUEr9_Tn58ocaCHFoegqxcdH5rhX_gMhp5PQ1PdZGsrlhJodiU0diJ8R1z2LUs2xFF8RIPnYJNLac4bFiw9-PBYzxi8t1f3elRFKYT-UpT9Qmja_0ehhQaL4LfFymNYu4mc5AjO6f7bjA5xgc9hgGUA8Y0JssCHgH7ZYYxpucpfqvRoRhKUOF4Z1utjYnXwOD-vEpmc2M5VVjlSPbGtS_5OnP5MABOC_5gs-sAXzSOjfz1V7__arJRpwd-lCPcXIfocMKnF5NEXEhgYP3OK0MM1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M3LTYEguJiYai7qOyuPkDMfkaxOdWPCLzeRw6SgdknVd7Uc9NCsWgPn-l8IaiSIaMCIPPUDCwXEZ8dxMDwjUO35peKq6N5SNw7y60bAGrW4b3huMkrS1eT9eBhBlYz9Xzu_wi3z56Vx21ceGVWUZHgNugFFroDyDNg9dGbjU6QNC9jb3SdCQFXHK2pnjluoJWE3w9T9fVmVc7fP6-XmO7KTAP7pr8MBq4ri59iVg2-bJr96jIaNz8nMKdzb-6oG5npekYpThsWnpza5Cjqchr8edvxzedtYD38EeVrDOzoyM3qjaSoojxRKVPj3h8X7XgVjSRv4jrm1gVKAh1zi4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0mK1HPsC-QQl8tapYcPLdV2NYKFSBTzo5RmJhucTdF-R7w9mdoDfYt1_zGvmyUZ-F_Uuv588PjXD7Og_QF9qdLgxl5BzH7oOnFhpHNMHBxNti8es_EbyC1BXPoNyEc-b_zn_g-N0exy2QeLUcEcP4pPCE5lsWg8pEMS5aCIrbasKRCpJPr3L8Gucmg77LCosHB9XyzzuZ_aCG1Zyixn1NYzjSAjkhMB8KTNY6vsftzI3MKfjrepqZo-ZkE7HBh_U4lM4HiD9RfDMX7J_vYqIbK7oWGNdM1d8j-rChWSrIHdswXhDoEE3hrroaEoO5FOkToSqpV9Tj8kwQXublbcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H4Qujm1TFoFNwQFBemAvx631fYh1csnLbMab7q6k4hsEMMh-MMWxjznlb5PZmD0n4gySFhbCgO7X1HlpP46wdFcnocFUsxE7MgNEJQiQK34Ldn_c5_3dWREV2n_KN2E0aaXCjlAM_Y0lmSmYsjNiMhgguf1-ecAogvUbQCzxf9icuL7aYB3F-RoF-_PwNalsGwucXR9HRg51pA5sJI3TZS4j0MUqixZQQ-JoBCwZEE4mdvp8R6oinznDTFQNYYVwjCt60n7MxLJpqt8XVYLpdJT_VOTAuJUr_HIY1MQI65TlG-FCjER2vrmqoUtXAquaYWizz7ZU9dD99R3-RM1BVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pk79bWtdrmB1FTOHhQ1pGpSUZgJ2RXT5D9155PAIsv_uEuQQbqai-VFh41jsJPZNJi1VbznNpsAauhfbCY4hZybi3-jxW_P6uv97fvOQLphFePoXorFXJ4t2yFyG5DSqIVm6H_W4g5Q8aV7UcdOp02NM2fkuqKJwfgATBSEAeO-FfXCYZYEeS8YgR9XzxvMarADWPB-LUsTMn9v_93p2Y7UilEtH2GQNlBIQDDb7qhNyDl-9Apfb9m0LT3hWM5ugcZRdwi-IM7KDNJ3SkN7_5He8ng_nhw42CUV4pkOqEY-0xV18EetuP9LHrFBA0MSuTsrqBMDg6W26-omUr3I2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XxbDIJc5kRYlAyCk7uMBFqxUAjJwEcJqypx3tK9MDwRVrkPW1-7gG7VihUdtooXAnPZpFHgnayAll3lt08XO5S7yF5-O-XzSolJw_UZc4MOkYtLpEUH1SEvrUhwbJFq9zfNKqFrXfcIeLtPLkgos296tzxxNTJaA6RwpHHNEBnqp3x7n8vzrmBNiFOrhvcRbcmwUgyebY7oSU_6l0yLrgpRbsdgFhZ0iLVN_Ab8Cw97Mr66k9yJjdFNLxV0WdPMgR4Tnl62AKJ8QCH-DgMC7rOuc8skv0Vh473okPJPOYazLi5fPCe7pm8Qkj1mCm8kR8jd4XCnKJnzCYrbe77ua6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jqr1BSrQ42rDe_rU8F8bYutPH5GgdCc1XqpVunN4GsXfk_5YN2Hdd9aUeea6UaUTGRYbp3rFCJzFgvHLZTXfSx4FgPHq-zfLNQCWkrkXjHAiHKZCl0sz-3CifAfmuGb-5EPvI9tvsOfuP5Dkve5OyatvWN0kixZwvSErHIh7mbwDhHe-keeiBXbUApJeUaIjTNykHmhMUZHCRdHQ_-xCWyRrWQKwPb55WEJMQCPTCMYPMZy6NtuPxxQwx0wOVhzAtNqlqngIb0-7bSzEtAOeCYdeNB3Da-d-OsySE9s9a1VZGZE9wzpOUTDuBY7p98vvR_w0N6gikZ2s5rW1pnk23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uAWt8wpZH78HXXxb6L5y2T6pTPKBMkjkVQQ6mAYYLZ7oGmkwqgnSn6VWtPrAB1bISiUU8J9FUe2n3-Ev4sUGjB8hd7o_Ivy88YurmhwQwJhjeBNKmDb-x9Lz1oZf0udcOlXVr84xbWrI9arN5yTV59FLgd4z5d75TB--ez9iRn1xLLCyG6S9jddZjmn_0YqfDr0q6JmLU2bQjmerxnkWdk1Cm06iFoJN8pDIW3YnkkF-aF9PEbq9YsqjDQVznrby0bzEyKMc1eFBUhKBriW06vQPXVBkho8QommthBLo8qP430bui4E-P1qNhr5yDeBHe9t0H-kcnM0wrXWjE2vn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mdgdMV8RlvG7QtkhCzWhqz6KboWUbAeFg10I19Wuq7DCIoEnmnfBvxMUrUfyDAeet3pNDRllire0DBqf-4wgP5gWlipdalPNMnHJoybm7gyDFATVDqbqGLBXMSkyG4u2eGoF8nac-b4shCbCOvsDhysHq_SP_Re_sytzI0beB5RjhKxQpvoh1-Y3uAIAhOOURy5eSk5ZBxj97q4JRIX2MDQOq5HhfZMwNY9R4Hg_7Qg96GEePHtZmc5FvHPJKzYFNRQL68bMYkPOM4vfWv8vqcZFssUtDDRaisVKmkldK5XGU8OYsiZ5gI-IUywA1H-XH0AlA6UfHvSNW5_D0rETfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال تلگرام خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه رایگان و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4128
۱. این برنامه رو برای کانال خودم نوشتم که در لیست بصورت دیفالت وجود داره، ولی هرکی میتونه سایر کانال‌های موردنظرش رو وارد کنه
۲. برای اینکه ریت‌لیمیت نخورین پست‌هارو برای مدت کوتاهی کش میکنه، که با هربار مراجعه یک درخواست به سمت تلگرام ارسال نشه
۳. به وایت‌لیست فعلی اینترنت متکی هست و فیلترشکن نیست. ممکنه روی بعضی از اپراتورها جواب نده، یا خیلی زود از کار بندازنش
۴. برنامه دیتارو از کانال‌های پابلیک میگیره و به هیچ اطلاعات شخصی‌ای واسه تلگرام نیاز نداره
۵. در حال حاضر نسخه ویندوزش رو منتشر کردم، اما اگر بازخوردها مثبت باشه برای مک و لینوکس هم ارائه میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bdADeUqUpLuFKq1XmYkypoULIdsitfAec2r-nZsWrbmgTyiK5q7bMiXV6EtHBwHxNLkUybuW1xVy1_llyEhuXFdDSt85zS5bXTS2gW9OKN9kRB5ehA6Z2hWg1fBxwO_dwTKFcpReoETeaFGLJT-3YeJzcSKDt1SdIchB_9nDb5mx7DEmHJ7Ewz9OKPxgSiaX-eMra4ZhzTiADDtXRKO_8ZX_m8nXgZNEWlCv0yGZWzIOruBKPD0cOYRQ7dUvQOBDIeZDPTI6WnMYPtIqbu_38Vld_59YmzzdQnfYhXZ-o3gSP-2vhHG_OgIB3CMdmpyHw8-At6yB1_kR7YmyJYiVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌بی‌سی در گزارشی گفته که شبکه‌ای مخفی در حال قاچاق تجهیزات اینترنت ماهواره‌ای استارلینک به داخل ایرانه، تا کاربران بتونن محدودیت‌های شدید اینترنت رو دور بزنن.
در این گزارش اومده که افرادی در خارج از کشور این دستگاه‌ها رو تهیه کرده و بصورت پنهانی وارد ایران می‌کنن، تا دسترسی به اینترنت آزاد فراهم بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2265" target="_blank">📅 08:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انجمن فین‌تک در بیانیه خود استدلال کرد که رویکرد ایجاد اینترنت طبقاتی، گره‌ای از مشکلات زیرساختی باز نمی‌کند و در عوض، اعتماد عمومی و پیکره اقتصاد دیجیتال را با آسیبهای جبران‌ناپذیری مواجه خواهد ساخت.
این انجمن از نهادهای تصمیم‌گیر، به ویژه وزارت ارتباطات و شورای عالی فضای مجازی، خواسته که به جای تعریف طرح‌های تبعیض‌آمیز، بر بازگرداندن کیفیت به کل شبکه اینترنت کشور و صیانت از حقوق کاربران تمرکز کنند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2264" target="_blank">📅 08:51 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LoSvhAhKo6YHzlN-mOHxhMwgbEj_KKKIj64T6BKEkpekYYQ2EUjXRHK6_q2_jPcM06tJzofGN0E1KJn0Na1XgSz8QcffeG0FIzD80rvaiJB2dq7_1iHakf--HNHpwe365YwWaes6VPatsq_1823rmjbndbYkoiJuJTHW65v0EXYE9o3topbYV55MJSXPfuntt3HCJUCM5qPXH89OU_MPV1miXYl7YHi-D13rh2YjtoeDqM9fuxUpXKADrHl9hAjtpAjzb_s_43v6ZuIGhxcb0tqH33q2Hlr3-M2E3uhX2kchlbQgM1arm4HlAChMH9vX2Vj3SyC7xF091UHql4VsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌ها نشان می‌دهند که قطع اینترنت در ایران وارد شصت‌وپنجمین روز خود شده؛ این در حالی است که نگرانی‌ها درباره وضعیت حقوق بشر در کشور رو به افزایش است.
از طرف دیگر دسترسی گزینشی و سطح‌بندی‌شده برای عده‌ای خاص برقرار است، اما عموم مردم همچنان از ارتباط با جهان خارج محروم هستند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2263" target="_blank">📅 11:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلومبرگ در گزارشی نوشته که قطع طولانی‌مدت اینترنت در ایران دو پیامد اصلی داشته؛ از یک‌سو توازن قدرت رو به نفع نهادهای امنیتی و نظامی تغییر داده و نقش اونها رو در مدیریت امور کشور پررنگ‌تر کرده، و از سوی دیگه فشار قابل‌توجهی بر اقتصاد و زندگی روزمره مردم وارد کرده. در این شرایط، دسترسی محدود به اینترنت نه‌تنها ارتباطات و جریان اطلاعات رو مختل کرده، بلکه کسب‌وکارهای آنلاین، تجارت و خدمات وابسته به شبکه رو با رکود جدی مواجه کرده.
برآوردها در این گزارش نشون میده زیان اقتصادی این وضعیت فقط به تعطیلی مستقیم کسب‌وکارهای دیجیتال محدود نمیشه؛ اگرچه این بخش به‌تنهایی روزانه ده‌ها میلیون دلار خسارت ایجاد می‌کنه، اما با در نظر گرفتن اثرات گسترده‌تر مثل اختلال در زنجیره تأمین، پرداخت‌ها، تبلیغات و کاهش بهره‌وری، مجموع خسارت‌ها میتونه تا حدود ۸۰ میلیون دلار در روز برسه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2262" target="_blank">📅 08:37 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">روز شصت و چهارم از قطع سراسری اینترنت.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2261" target="_blank">📅 08:35 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کاربران شبکه‌های اجتماعی از جان باختن حسام علاءالدین، شهروند ۴۰ ساله که گفته می‌شود «به‌دلیل داشتن اینترنت ماهواره‌ای استارلینک» بازداشت شده بود، خبر می‌دهند.
بنا بر گزارش‌ها، او که پدر دو دختر بود در اثر شکنجه در بازداشت جان باخته و پیکر بی‌جانش را به خانواده‌اش تحویل داده‌اند.
©
indypersian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2260" target="_blank">📅 19:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نحوه ساخت فیلترشکن شخصی رایگان به کمک گوگل و کلودفلر، از طریق متد MHR-CFW ...
📽
youtu.be/L3lJZrAqqUQ
💡
github.com/denuitt1/mhr-cfw
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2259" target="_blank">📅 19:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2258">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mJ_AmNmNEhq86YO3IdfEotW3OFo3i0ihkFurkf-qAafWKV5UKtD5RqtyLUZxvpxdfd7VCA8X8z2mmMHS4onwKN_57LzaRLAFMA1fQiAmEN2nya6EhXyjINw_CuTMyeNuuWUGxD1kblnCD_XTP1zWvPmETkdBM9AmmsnJHeiPl5D29PItLGOdu8HX0IXIB-z7KsPzTjOj6u1HINR61p1BgkeAcoavQsEhNceIFxujiWcMjf1fRoI6wYPxAICb2waGaGmVuL_QoKqB4Ho7xI9Gmf1XAdmBm-a_nDUcqvkfI3beM_nlsEp11DtRSHu7ZpRrLEamqp4wa4BoeLTiuOeSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز شصت‌وسوم از قطع سراسری اینترنت در ایران، گزارش عملکرد سه‌ماهه اول سال ۲۰۲۶ شرکت Meta Platforms منتشر شد، که بر اساس اون تعداد کاربران فعال روزانه این شرکت به حدود ۳.۵۶ میلیارد نفر رسیده و نسبت به سه‌ماهه قبل حدود ۲۰ میلیون نفر کاهش نشون میده؛ هرچند این شاخص در مقایسه با مدت مشابه سال گذشته همچنان رشد داشته.
متا اعلام کرده این افت فصلی عمدتاً به دلیل اختلالات اینترنت در ایران و همچنین محدودیت دسترسی به واتس‌اپ در روسیه بوده. البته در پی انتشار این گزارش، سهام متا با واکنش منفی بازار مواجه شده و در معاملات حدود ۷ تا ۱۰ درصد کاهش یافته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2258" target="_blank">📅 19:13 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بعد از ۲ ماه قطع سراسری اینترنت و شدت‌گرفتن تعطیلی‌ها و تعدیل نیروها، پایه حقوق وزارت کار بنابر مصوبه شورای عالی کار ۱۶ میلیون و ۶۲۵ هزار تومن تعیین شد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2257" target="_blank">📅 17:39 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2256">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران در
موضع‌گیری
خودش نسبت به اینترنت طبقاتی و حق دسترسی به اینترنت آزاد حرف‌های درستی مطرح کرده، اما خبرنگاران جزو اولین اقشاری بودن که به اینترنت سفید (یکی از
سطوح
بالای اینترنت طبقاتی) دسترسی پیدا کردن!
واسه همین این بیانیه بیشتر شبیه یک موضع‌گیری تشریفاتی به نظر میرسه، تا یک مطالبه جدی و فراگیر. اگر رسانه‌ها واقعاً به این حق عمومی باور دارن، اولین قدم میتونه شفافیت و انتشار فهرست کامل خبرنگارانشون همراه با وضعیت دریافت یا عدم دریافت سیمکارت سفید باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2256" target="_blank">📅 17:33 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2255">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1SPnNwMdZid_pMwGtwWG0bJbSGxrN1bUSxuoN1KBJSO0eY5bqmrydAISdUl5WZY2IUni7fNXj7I3hM9yO29hm2eaE1aFS-9QFtsNleHsiyxhUmhj0Dqn2FwzfczxGHLW4uVTN9NM22gZ2maH4zizL4UrUzafrPAcKdSLD8DMOJYd1Ff1bc0SezSw2P6UjeSo9zdcgInatm_d5Pp_EYedxdB9Ey43lGB0lTrHitJN3iJblG6vvAZqQLvIOziYPg72E2lkDpsX-LEAICS7OWyzt5MK15ZvQQD_cJJZ0ieVJs7qk8pntH2za3xF_UoAqFW6krIlJ_so2ya8D3PvWvfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران استان تهران با صدور بیانیه‌ای تأکید کرد: دسترسی به اینترنت آزاد، باکیفیت و همگانی یک امر تشریفاتی و لوکس نیست، بلکه حق عمومی است و دولت‌ها موظف به تأمین آن برای همه شهروندان هستند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2255" target="_blank">📅 17:27 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2254">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rvHySYRbmAfp1sMZhxQMvnMhHWDdp_u8ir-LuG9MhE3YPK7GfbsBAh5ZajHtG1Kgc3s881DoLrOoPKeGS498nmHiZrnvmq1BfCOlxkmrcN4h5oBm_FUohuF7M7bxN7so7BcOMa_qrhKSW0NvbBcLpF4f0sgF3wUk3JFGK0kpIfuheIf6c7msGtg2ohMA-VLL069vTHGM7pIiZamS9W9F7ExO6MdKxR_S2ytuu3G0NNFkFVYwTcr1SAwl7bwATAVAkhX-A19Mkn0IJWA4qfq9EpoCYarzAbkDykflCywKc1-ouZcgARLqQIn6PmwUfudsw5ovnWMDT9KYSdUJJRG8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایفون در بروزرسانی جدید اپ اندروید Conduit گزینه Personal Pairing رو اضافه کرده، که میشه یک لینک اختصاصی دریافت و با دوستان یا خانواده به اشتراک گذاشت.
این لینک رو باید در داخل اپ سایفون از طریق بخش Pairing URL وارد کرد، تا مستقیما به ایستگاه کاندوئیت کاربر موردنظر متصل بشه.
البته با توجه به قطع سراسری اینترنت، فعلا سایفون بصورت عادی برای کاربران ایرانی قابل استفاده نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2254" target="_blank">📅 17:15 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2253">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bzM8ml9mkT9XSrzmrlReOdhPrl4wMmRvW5Ckk2tY5rYqz2bivrwYRfm6aEnCKk5tMmanfW8G7qw8nWz7B9X23Mxhnk6LkDq3OPGbJM6F9Ye14z9qIoJ9C6N6kgo7p_qbYZzZUTlgoDVt2BRnUTGW_KJSNh9UUJtjpryMvj7YjfvlOPxluAQAaGGDKrrSfuNH9CWuDqbH1xy9kJWiJxPKUG5wkIc2nOIIrXO9j1yVH47zWmGfvmCZd3us9cWkralCoJs7_NzuPi8uvd3xgZazdcv6y_edTfoISr2VntVF5uosHgE2bzr2izve9fR1tsfp5D8C71uDUW8VJ--qZk4Y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه سازمان گزارشگران بدون مرز نشان می‌دهد ایران همچنان یکی از سرکوبگرترین کشورهای جهان برای روزنامه‌نگاران و رسانه‌هاست. جمهوری اسلامی در میان ۱۸۰ کشور، در رتبه ۱۷۷ قرار گرفته است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2253" target="_blank">📅 17:03 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2252">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روز شصت و دوم از قطع سراسری اینترنت در ایران!
میلیاردها تومن پول داره توی زمین VPNها میچرخه که بخش زیادیش میره توی جیب جمهوری اسلامی و حامیانش. شیرینی همین پول‌ها باعث تداوم قطع اینترنت بین‌الملل و تمرکز روی اینترنت طبقاتی شده.
جمهوری اسلامی ده‌ها هزار نفر معترض رو در دی‌ماه قتل‌عام کرد. یادتون باشه بخشی از همین پول‌ها که بابت
#اینترنت_پرو
هزینه می‌کنین، قراره خرج گلوله و سرکوب مردم بشه!
©
Maroon
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2252" target="_blank">📅 08:35 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2251">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DbPo9G3yk_iQMlfFzrC3rxo7nR3o13MrJESDEINN1ZK_l-sdDE4lhnTb8cmgG0JUtJt4fPc5NRVQV6qCf_BPuLSercPVx4dRML3nYvoDughTAkBWesQY0EDu4jII_kfU50YOIfEjVMo2mp4t9Ho6Y6pQNx8lq0mPolfF36oK4dUuVdhjBooqN-DKm6-2KdPUq6JSfMN5_fVivf3VvyTruJrbwfAaVR-MsOd8Lk2v66-5tSvQRffqw4_4vaIIg4trim6au0FC9BXP4myb9WUlW8sLzwEcAbsQHf5MbyxFTdxop5nB3doJuuQufs6akBSNIIuzfxCZdoT6rRjqq6m4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی، یکی از نمایندگان مجلس گفته: رئیس جمهور و وزیر ارتباطات مطرح کردند که ما مخالف اینترنت پرو هستیم؛ پس چه کسی این تصمیم را گرفته؟ رئیس جمهور بورکینافاسو و وزیر ارتباطات افغانستان این تصمیم را گرفته‌اند؟ رئیس شورای عالی امنیت ملی، رئیس‌جمهور است و باید در این زمینه که می‌گوید ما مخالف هستیم پاسخ دهد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2251" target="_blank">📅 18:05 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2250">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V9RWcGtoOMt5_mGegCufoiMogEXWUXxviUEFC8CK_hrUuufd86kgE-K5SSKPBqg48rcho7X8Sc-3LZizISEHey7O36e2LIDw20oVJxN9uIjLZzp_BJgO7EXIG_fHWlmMTgcAK-V8WTV1vl9Kn18qtB-z3Y_FdQvq3eVn8c4Xz0j4yTEF4xXXmjVXApBs8RaW_rKvAJ_2AheP5vnj_TDQN77_qgamye-IPkvV__0B7qdXSepgTAUIfOkWBEFD5ts0jyD4O5L50-UYtJv5ZCCR0v4Z9CGcKy5oLUHiduQk2C2VflFJsmn_9SzKNiagXBc3e3gnedckdApFZCMvUL-YYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت ما را به عصر حجر می‌برد!
انجمن تجارت الکترونیک در بیانیه‌ای اعلام کرده که قطع گسترده و طولانی‌مدت اینترنت در ایران دیگر قابل توجیه با ادعای «امنیت» نیست. این انجمن با اشاره به بیش از ۱۰۰ روز قطعی در یک سال و بیش از ۶۰ روز قطع پیوسته اخیر، تأکید کرده که این سیاست‌ها نه‌تنها امنیت ایجاد نکرده، بلکه اقتصاد دیجیتال را تضعیف و جامعه را با آسیب‌های جدی روبه‌رو کرده است.
در این بیانیه آمده که حتی در دوره‌های قطع کامل اینترنت، حملات سایبری مهمی رخ داده و این موضوع ادعای ضرورت این محدودیت‌ها را زیر سؤال می‌برد. همچنین هشدار داده شده که گسترش «اینترنت طبقاتی» به معنای تبدیل یک حق پایه به امتیازی محدود برای گروهی خاص است و شکاف اجتماعی را عمیق‌تر می‌کند.
به گفته این انجمن، مسئله تنها دسترسی به اینترنت نیست، بلکه حق دسترسی به اطلاعات، ارتباط و حضور در جهان امروز است؛ حقوقی که با ادامه این سیاست‌ها نادیده گرفته می‌شود و هزینه آن را مستقیماً مردم می‌پردازند.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2250" target="_blank">📅 17:46 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2249">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BmwSY5u77IlLzbY7LZxFJg_YX5cx-ay4sn0WEquXCtEMdkDP6uBQ7XZmRIfEolZsTN3B84otwFNK6ri34j3OCHgTYr8D6mlh_aj2tLVL3DhHsTTG2LPMsM2mZxsiNi_BPp23gQaofgonUQstTplHyAD7Mkh5t-jPzm5eL_rHX7l5UFAz8N7s3Geh-knhvjYltlvWePp3llNYXDBok0KwkQkdqdFN3Gzw24sT_vsQfCULDkE0HEBRplVVbzKb8sY0oQ9XA1iSRdZm4g2DFl8hwWEaJMSx7hZqUXvPE0kTm2czyRTUOTUyLucNmtkAXgzQBtmkzNEWMxsxnHKhLK3QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نسخه جدید CFScanner، دامنه‌ها آپدیت شدن و هسته ایکس‌ری به نسخه جدید ارتقا پیدا کرده. یه قابلیت هم اضافه شده که می‌تونی خودت دامنه‌ای که برای Fronting می‌خوای رو انتخاب کنی. همینطور پشتیبانی از Xray توی اسکریپت bash اضافه شده و نسخه Xray تو بخش پایتون بروز شده، تا همه‌چی هماهنگ‌تر و روون‌تر کار کنه.
👉
github.com/MortezaBashsiz/CFScanner/releases
💡
t.me/PersianGithubMirror/3624
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2249" target="_blank">📅 17:28 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2248">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MqgVvGqlw0rXfBwgF_U0Djh4sX5Z4gNF2id42cPNTbG3bCWEFc3DBGmgYrfXjct4Ywn2ZW24Fqh807UDGPPYxpFQwsunekd-ouQpkwgRdcDe-b6RtSFyZkwFk2efvneloaaoWlX3owF5lZQ9S9moJetE_8uFRYrnYCCLzYZqzs0g0hpSbfnf6lgEKNDDHXOnHCVXNqcSDCD-q6Lh5CIUNu7tFifZU1MIg3nikcgzWvR-K8gaLXku9xnHF-DXbJCq0Kr3IWHcZBjpxzUjJvuo_Npu2PEChzFBMJBs8svCm4GPVrV2X6dej6qX5TJVJGjEwFa6ak5ROOhj3ahoiqfksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن علمی روان‌پزشکان ایران اعلام کرد "اینترنت بخشی ضروری از زندگی امروز است و محدودیت یا دسترسی نابرابر به آن افزایش فشار روانی، احساس بی‌عدالتی و کاهش اعتماد عمومی را در پی خواهد داشت".
©
shima23972921
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2248" target="_blank">📅 17:08 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2247">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">روز شصت و یکم از قطع سراسری اینترنت در ایران.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2247" target="_blank">📅 08:48 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcjlhXpvVgAO0omuvjcSSqbZwuRJekLr-jHHshGr8Vl0IvsdOvps335v4M9ZXQIYe-dtMckG5jjx2ZhtiB0DSf4dc2DokcpX5q2cbfPE9wSdPoL6OmCOui6_8jQ0QBJL0cgfRfQQ91Hx9P-FkVm4TTrBdHJp2L_QAqAQPvJUtm7aLIu6ACymX5pW_dd4eZsiflRFONRAnsjJfm9w9tX6i0BRTOUFa0PubSI-BkW0U7OqPGmDXo1i3J_m_Y-3m0YJBDpYltFvcc7z8ruwnGX1UiGvxgaCd3r2ri77qSVlmi-XMGDGusKSoxhlFPCTjZscHuzwhAlXARmbq7nq97aHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به واحدهای قضایی دادگستری نامه زدن که میتونین از
#اینترنت_پرو
برای انجام امور جاری و تخصصی استفاده کنین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2246" target="_blank">📅 08:41 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هیچ‌کس از هزاران فرد دارای معلولیت که از طریق اینستا آنلاین‌شاپ و درآمد داشتن حرف نمی‌زنه. قشری که نه حمایت دولتی دارن، نه جایی تو فضای شهری و نه سهمی از استخدام‌ها‌.
©
Mtherofcatsings
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2245" target="_blank">📅 18:35 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینکه می‌گویند قطعی اینترنت «روزانه ۵۰ میلیون دلار» ضرر دارد، یک مغلطه است؛ این عدد فقط نوک کوه یخِ خسارت‌هاست. ضرر واقعی در نابودی  کسب‌وکارهاست، خصوصاً کسب‌وکارهای کوچک و استارتاپ‌هایی که شکل‌گیری‌شان سال‌ها زمان و هزینه برده. با هر قطعی، بخشی از این اکوسیستم از بین می‌رود.
از آن بدتر، این خسارت متوقف نمی‌شود؛ وقتی درآمد افراد قطع شود، اثرش به کل اقتصاد سرایت می‌کند و یک زنجیره از رکود ایجاد می‌شود. بنابراین مسئله «۵۰ میلیون دلار در روز» نیست؛ واقعیت این است که قطعی اینترنت، در مقیاس میلیاردها دلار به اقتصاد کشور ضربه می‌زند.
©
hiddify_com
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2244" target="_blank">📅 18:33 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رکورد ثبت رزومه در جاب‌ویژن شکست و بیشتر از ۳۱۸ هزار رزومه در یک روز در این پلتفرم ارسال شده. این مسئله نشانه‌ای جدی از تعدیل گسترده در بازار کار و تقاضای انفجاری کاریابی در پی اونه. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2243" target="_blank">📅 18:28 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvjLb-YbVZJN0qdMQzBTW-kgByL6bzC0gcspM0h8CoEk-qwqlE6WXrsa27jaf2luyr9ph07dGQhuZfJ7UXxRxFdMPryKORqItO60F9CQN9fatp9gj35AmHdaLyvQhWMZQIfxw7OTzqiyIbQyBlPasvtq0xB7BSWlx4t1jRlVhc6qT5BaFs-YdLW2uVXdF_BjxaPv8Aop7FCH6peyi6WcZ5Pd7kVgjRtxpsgHZNEHb__QQT3ef_zNOerisNEgi0HZK1FnZDSWWSR7CdZ3ucaZ-wktZWdF23mZkL_QciCxZ1eyxt_L9dYRlTZ0OVOoqV6KkRw49UBcJ1mSF6MhwU-ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی وزیر قطع‌ارتباطات رو از برق بکشه!
۶۰ روزه اینترنت بصورت سراسری قطعه و بازار
#اینترنت_پرو
داغه، مشخص نیست هاشمی در مورد کدوم تلاش حرف میزنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2242" target="_blank">📅 18:22 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zg7ptkL0dMQvx-d1yk2_Oo9_2HTL212dxUK0G5jio8F-y3hpEC0xZHo-_ey5TYrNxWS3N9Qy7Oawymd-Xy-7oPqnCXU-UWrZqLJISTAAKn0nTE_mWNceylmZH84vMaUAbKj9f_vhPG5SDDtYXh7cuZtu9-PsjC2n3iObyAfak6HlkPW7Szc_nMSaC7kp20nWcYJR2xeoE681d-S4bepD5FtEc9v6RfxPdRVtHbnn1YuYljAbOFiJn5cyOdKjClrqH0FQcrq2Bbgoggq6f05SHBqp_KDEWvSoLTGmDI4d5du_QXld3N_Fazkgccqsm9JKlanIGHNTcTCrhMaQaLiJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد روز ۶۰م از قطع سراسری اینترنت در ایران شدیم.
وقتشه اسم وزارت ارتباطات رو به وزارت پست، تلگراف و چاپار (به جز پیجر) تغییر بدن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2241" target="_blank">📅 08:58 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به بهانه‌ی امنیت اینترنت را بستند و حالا گروه گروه پول زور می‌گیرند و باز می‌کنند.
این یک تلاش برای خرد کردن یک ملت به دسته های کوچک است که راحت تر خفه کنند، بیشتر تجسس کنند و مردم را آلوده‌ی بازی کنند تا دیگر حق‌شان را طلب نکنند، وگرنه امتیازات یکی پس از دیگری قطع می‌شوند.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2240" target="_blank">📅 18:12 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌نرسان "بله" خیلی عالیه، پیام که میفرستی باید بعدش اس‌ام‌اس هم بفرستی که بله رو چک کنه؛ چون اصلا چیزی تحت عنوان نوتیفیکیشن نداره‌.
©
aboIfazI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2239" target="_blank">📅 18:08 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O4U0BpIaoSX4raRH7TZ-E55mMigjrrPqJl7GkuZze1Ivbe9NGgI0k9zkoqUoONBi-LNIF4-rHdLErI2wmFb8vCTSsKKyhlkv8nenhs7ntM8U6iU2ZJobu9ynw4VomMrtM4XfdO0HIJbaoL0gMLP9N2fkHgkGofwj72uITUGcZ1Qh35-QS-tsejhlyTwSMjtsLW5pLbc1YFviJy8HW3LZ3bMvX2Si1V2UlbAaNCW1Y9N44W2dXuh7ap9j88Iz7fSggaX_armeeqS5BJiSwYLqszYwSsdtfH-smxoGLXlee6IzhoAmHPoMPpqucrY_RXIFBH0kCsL1-b2n1XX2TWxblQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت
#اینترنت_پرو
در بازار سیاه حدود ۱۰ میلیون هست. مافیای
#اینترنت_طبقاتی
لطف میکنه ۵ عدد اشتراک رو بصورت عمده به قیمت هر عدد ۵ میلیون تومان (یعنی نصف قیمت) عرضه می‌کنه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2238" target="_blank">📅 17:59 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DGUp0XR8kY_JL5R5B97KqFkWF6edSNzFz51gXKKaIG6SZaL0-uJ2lRPtW-1bJrJJIMyYQjaDVyCSJBIxqn3HkWNgZvDH4L9byed8iRY45xaQ1tyw3xqzZUudmRn26oMUDOB_AIEWFY5I8hHLpHwRwuB-87wnIAOwVPZzEKuiWoNflt0Fak9Ben0CP2euwJbVlx6IyoTAiR-0pAZAP1Xb8PBPsfrqcaM9U3WCyOxq5Tqod9EV2Lur_-WnBvkSBeB6Gpot5iJNB3H81zE9pBZVLgq3lH_BT6x_T1fvM29dcVPEOZa7GOVrrcaxI9sGEBi_ogLoRGV2psQu9RA2AryDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت حدود ۲ ماهه اینترنت رو بصورت سراسری قطع کرده تا طرح
#اینترنت_طبقاتی
رو جا بندازه. بعدشم با کیسه دوختن برای مردمی که دنبال حق طبیعیشون هستن، یه بازار سیاه برای فروش آیپی رانتی و
#اینترنت_پرو
راه انداختن.
قبل از اینکه روش تازه‌تری مثل «پرو-پرو» برای خالی‌کردن جیب ملت پیدا کنن، چندین کانال مختلف دارن هماهنگ (حتی توی رنج قیمت) همین اینترنت سفید رو به مردم میفروشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2237" target="_blank">📅 09:17 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در آپدیت جدید theFeed مشکل نمایش بعضی پست‌ها به شکل نظرسنجی برطرف شده، باگ هنگ کردن اپلیکیشن رفع شده و امکان اشتراک کلاینت روی شبکه اضافه شده.
پروژه دفید یه راهکار مبتنی بر DNS برای دسترسی به محتوای کانال‌های تلگرام توی شرایط فیلترینگ شدید اینترنت و مواقعی هست که همه مسیرهای معمول بسته میشن، اما DNS هنوز قابل استفاده می‌مونه. ایده اصلی اینه که بدون نیاز به اتصال مستقیم به تلگرام، بتونی آخرین پیام کانال‌هارو دریافت کنی.
سمت سرور (خارج از ایران) به تلگرام وصل میشه و پیام‌هارو می‌خونه، بعد اونهارو بصورت پاسخ‌های DNS از نوع TXT و به شکل رمزنگاری‌شده در اختیار کلاینت قرار میده. سمت کاربر، کلاینت با تعداد محدودی کوئری DNS میتونه این داده‌ها رو بازیابی کنه. طراحی سیستم طوریه که مصرف کوئری پایین بمونه و در عین حال در برابر محدودیت‌ها و فیلترینگ مقاوم باشه.
برای اینکه ترافیک قابل شناسایی نباشه، از تکنیک‌های مختلف ضد DPI مثل padding تصادفی، تغییر اندازه بلاک‌ها و پخش کردن کوئری‌ها بین resolverهای مختلف استفاده شده. کل ارتباط رمزنگاری‌شده هست و هر درخواست بصورت مستقل پردازش میشه، تا ردگیری سخت‌تر بشه.
کلاینت یه رابط وب داره که امکاناتش فراتر از فقط خوندن پیام‌هاست. امکان جستجو بین پیام‌ها، کپی گرفتن از چند پیام، نمایش لینک‌ها، ریپلای‌ها و تا حدی نظرسنجی‌ها اضافه شده. اگر سمت سرور اجازه داده شده باشه، حتی می‌تونی پیام ارسال کنی یا کانال‌ها رو مدیریت کنی.
یکی از تغییرات مهم نسخه‌های اخیر، اضافه شدن بانک Resolver مشترکه؛ یعنی دیگه هر کانفیگ لیست جدا نداره و همه resolverها یکجا نگهداری و امتیازدهی میشن، برنامه هم بصورت دوره‌ای اونها رو بررسی می‌کنه تا بهترین‌ها استفاده بشن. یه اسکنر داخلی هم داره که می‌تونه رنج‌های IP رو بررسی کنه و resolverهای سالم پیدا کنه.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/3393
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2236" target="_blank">📅 09:01 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6EqaA0pOkH7FhSglk5zhMKjTdRoziKmKLgn97VNfzabs9opktuIRR8fwY1ZOLTCoWMpzkyo9-SOTFXPSG70C6i3CAKZrws-DfiuPI0aW9WD-8Q-wiZZvRDcZxlck4NMGXt254bnEaJTt7KNUc9SlWHWlcD0g1JRJUXgqwlMMbc1Ik5s06Ih5V0ZlpoMl5fG1RnQxqqbJT_TCfCmAGZ4GpHc25jLZbZDvB8RsAlWK5jWAvFtSGKsNkyJrtKRyClcmzZlu22pIpvaD0jxot40CoiOIAmpPBdxzNHKr09aJFQe8FoJPlvMi_4Ov3TsaaGH68tDak50fj2I3Q5-DVbpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Loole یک ابزار مدرن برای مدیریت تانل SOCKS5 در سیستم‌عامل macOS هست، که برای عبور از محدودیت‌های شبکه طراحی شده و با استفاده از Google Drive و روش MasterHttpRelay، یک مسیر ارتباطی پایدار و کمتر قابل‌شناسایی ایجاد می‌کنه.
فرآیند راه‌اندازی بجای درگیری با مراحل پیچیده و زمان‌بر، از طریق یک ویزارد ساده انجام میشه که کاربر رو قدم‌به‌قدم هدایت می‌کنه و حتی بخش‌های حساس مثل تنظیمات Google Cloud رو با راهنمایی دقیق و لینک‌های مستقیم پوشش میده.
👉
github.com/g3ntrix/Loole/releases/latest
💡
t.me/PersianGithubMirror/3455
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2235" target="_blank">📅 08:52 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من تحقیق کردم، چون اینترنت پرو گیگی ۴۰ هزار تومنه، دیگه برا جاسوس نمیصرفه جاسوسی کنه. اینجوری امنیت تامین میشه. ایول.
©
SMoslemi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2234" target="_blank">📅 08:40 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه تشکر هم از بچه‌های سوپر اپلیکیشن روبیکا بکنیم. واقعا ساختن برنامه‌ای که فیلتر نیست، ولی از اونایی که فیلترن ضعیفتر و کندتر کار میکنه کار آسونی نیست.
©
danyydrinkwater
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2233" target="_blank">📅 08:39 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yow394lc0KjlPb71KKZ6qFEK-sQKRM7oW_cLlAHJMtPm5armOIClNAJU5poR9kLe4diys4vzPGK9gROQHAI-sHtrc41lGSFPWkQpjx5-NA2LL5LmraMG1bavu9FZVdRDtM84iuTEnWwGXzFIrXAnyNrh24gRdMgA-E5ZlLamzcHLKCEGyolrliOPV0MEGwlg8en49w68mycfjpu-Dr03yvFzquuNKxp72KcfCT3iTl_SFClFgOMLlS05RdZU1TymrZTCoN0K7eOwDuVp-r7XrxVkYoDffM39DP6rtH-BbcsaflO4fx2-bfXn1iJgpUskw0ivPtZuiHEz1CovyXcmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۹ روز با قطع اینترنت مارو از جهان جدا کردن؛ به اسم امنیت!
بعدش اینترنت رو سهمیه‌بندی کردن و گذاشتن پشت باجه فروش.
اسم این دکان‌بازار امنیته؟ یا رسمی‌کردن نابرابری؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2232" target="_blank">📅 08:36 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZTSgHkVP44gDOMNPdtI60Kg8NdB-ur_NYai9JLGwZFqcd-zC6FXtDip9-H3th5hDRlNRyGoNflc-CKsszIq3gs9fKwJZHou2nlgsFWIILrWbZTUsqzziJth2iMH8Nsuu8XgYyh6D7n9QfTkoaAAwkc71rgCruOT8Ik3IVdnjBBdDslrI7PH7zv6zWnJsKAiBzAet5bsk4UBylJd9Fys-hEAuoli4kaWPU4LskCjab6R3JKnzYK6OCMWXyTO1-ctkp3qp3VafMeNQe8YwBuDrMbNgYOUNFBL415VWLnShFX4FLtkc4x9hvJEctCfWoa5YhxcOvKzwMSZeIX1HJrFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبقات مختلف
#اینترنت_طبقاتی
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2231" target="_blank">📅 19:03 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دولت همچنان بر مخالفت خود با «اینترنت طبقاتی» تأکید می‌کند، اما بررسی‌ها از چند منبع نشان می‌دهد طرحی که امروز با نام اینترنت پرو شناخته می‌شود، نه‌تنها به تصویب نهادهای بالادستی رسیده، بلکه اجرای آن به‌طور مشخص به دستگاه‌های مربوطه از‌جمله به مرکز ملی فضای مجازی سپرده شده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2230" target="_blank">📅 18:28 · 06 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
