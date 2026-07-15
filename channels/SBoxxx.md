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
<img src="https://cdn4.telesco.pe/file/nxOSqF6MzDnUKIhKnHivr2272bdGx28iIT8wj0212QsFFG5ynhpYVWTyLba7WcZFMOcJn6LBkcyq2jSBgyHDKH8p0YH65oyUUNQtVHZw7CrV5VNhIzphEM05AqEPHlHooxIJZAnHU2N6QBts9wCqiBaEIm77UsLl2oWu0IM5y5vf8tLZw0QwFbDMcBeH3Kaj2MxbBxABA8N_neN0URIp1bsZIwk0VJs6CzbeJcmYUk9wWuCyPkvm0GymA2na0HFI038eKB2vaOCPhW-rI6tst9JwIoNvP4l82OMUgtv52nYv5k4jGuZf1t5iDZ-VU-S-OC2pDksYDGz3FVHJErWqxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.3K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 22:26:50</div>
<hr>

<div class="tg-post" id="msg-18795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله ایران به اربیل</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SBoxxx/18795" target="_blank">📅 22:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قبلاً هم گفته ام که پیش‌زمینه سخنان دونالد ترامپ درباره «تهدید کمونیسم» را باید بیش از آنکه در واقعیت سیاسی امروز آمریکا جست‌وجو کرد، در ادبیات سیاسی محافظه‌کاران این کشور و تلاش او برای پیوند زدن خود با میراث رونالد ریگان دید. از منظر علوم سیاسی، کمونیسم…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/18794" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/18793" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم  باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم  محمدباقر قالیباف در بیاینه تبینی خطاب به مردم عزیز ایران:   این روزها که دوباره آتش…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/18792" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قالیباف:
باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
محمدباقر قالیباف در بیاینه تبینی خطاب
به مردم عزیز ایران:
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد.
لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/18791" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXDKCq6H0HNtMD2SbwsYZ4Nk5nCmaP_fwRWRS5RW219-5IqXCKbOmbsKPVIALYY5UTERxcNxniy9tNL41XQXmiLI6UErqcB2_Ih8IGbaSijifjq3NmSRtapqMttPcLc6291KsODxq-pkTNastuckvdI1h-O4AdQnAdihLj-lHQpNhmqkQc6LFs81ENcrrRjwuTg7tNd4wMZJMCt2k_pOWmQXojwTHRKnzPO89MpHARQw7wRhvbxcrROdU3RfdvdFVDzYGBpGvawghJ_cHbC1cO_FwLlwfswNEnrXKHcf0OUQxqxeZuG8v1wLhslFdrC7r2TUR7Q8jdsbfVyY7OY4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/18790" target="_blank">📅 20:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به گزارش یک مقام ایرانی ناشناس، ایران یک پیام خصوصی به جِی. دی. ونس، معاون رئیس‌جمهور، ارسال کرد و در آن، جارد کوشنر و استیو ویتکوف را به سوءاستفاده از اطلاعات محرمانه حاصل از مذاکرات بین آمریکا و ایران برای کسب منافع مالی و انتشار اطلاعات متهم کرد.
دولت ترامپ به صراحت این ادعا را رد کرد و این اتهامات را نادرست خواند.
منبع: Drop Site News</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/18789" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gladUh9lHJxF3ZKF71rpKSfKk7J-C2fFjsKOR0wRZv7eXdXSJqR3FZQuBhLE8sUWW5JKFY1miPJnZDss1QBZeStSFHnqvZhufFYI_NDousR-VSWmqaItbWg1FrhJx5fataG4n83ORb_93DxRhIVWs6tplOri4EFN9OZJk8iKfnM-X5yZs5MselHKzQewKY1aVPmznj2Dpj3U_fjE6Q6JRCcw-xDVT4iqivzSQ5HGkNJotuPJzQcE5uuUpjU_ZqifE0BXSyKYrXFt6_O66fsbrzQqRVp5QM4QLYWXzvjIKakFteQkrAny7UqfqQp2Sv2LCKVdh_yp1DquANKDpllMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:   چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/18788" target="_blank">📅 20:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18787">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUVxRe7lLSDJrs7Q84FneAgfaeQUUrCKl8SZRqQWXEBIYIZcfXmKXAQupydxG2P07N7a7QJrjI4e2P6gRln4vO1JkA47w28jhalDgdanGco_NTmbKBQ0FZzAesxnvhxu98w2nBBNiGVEVbW8fDXxLnrNE0I68iuVEjVM0eOYzR4UoS1RvKW9npYHTOT9GLlbLoTbwEffAMeMZ4VXHVhoPCjUqnR-SQo2wS1mu7PF9f4-RB6iv4P6otCN6WkLLQvP7nMmJrtsCaP_yL5ikWzN0XUH6eOtbsXIQFyR35Snld78yctJfIUNJeGhCWXWIWBRQM5L5g0ElmJ6F7ffhgUWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/18787" target="_blank">📅 20:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حمله به کویت</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/18785" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک تبعه ترکیه مبتلا به اسکیزوفرنی در مرکز شهر درسدن تصادف کرد، اما هیچ‌کس را نکشت یا مجروح نکرد. پلیس آلمان به سمت او شلیک کرد و او اکنون در بازداشت به سر می‌برد.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/18784" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/18783" target="_blank">📅 19:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">و از این جالب تر این است که نسل کشی یهودیان توسط نازیها در جنگ جهانی دوم به کلی الهام گرفته از نسل کشی ارمنی‌ها در جنگ جهانی اول توسط ترکان عثمانی بود.  اسناد بسیاری در این حوزه وجود دارد.  حالا نوه آن خونریزهای نسل کش آمده از خطر نسل کشی می‌گوید!</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/18782" target="_blank">📅 19:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران:
نیروهای مسلح جمهوری اسلامی ایران نشان داده‌اند که هرگونه تجاوز به خاک ایران، قطعاً با پاسخ متقابل مواجه خواهد شد.
در حال حاضر، برنامه‌ای برای مذاکره نداریم و تمرکز ما بر دفاع است.
موافقت‌نامه همکاری، مجموعه‌ای از تعهدات متقابل است و در صورت نقض این تعهدات توسط طرف دیگر، ما نیز از اجرای تعهدات خود خودداری خواهیم کرد.
این یک اصل است و در آینده نیز از همین مسیر پیروی خواهد شد.
منبع: تسنیم</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/18781" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/18780" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتانیاهو روز یکشنبه به ایالات متحده سفر خواهد کرد و روز دوشنبه با ترامپ دیدار خواهد داشت..
روزنامه "هایوم" اسرائیل
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/18779" target="_blank">📅 18:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار: آیا رئیس‌جمهور الشرع (جولانی) برای شما تعهداتی در مورد کمک به حزب‌الله در لبنان داد؟  ترامپ: بله، او این کار را کرد.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/18778" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.  تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/18777" target="_blank">📅 18:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzvI4-Y4lwzUGYNkdq-t-2hiEQiS7-5oUvYd_k2o2EToQtf98KAhM7c20zIjKb7krLuWSb9A35sIi1L9ww0LZnCgAWZi-WY0rrS1CwXzBvjdx8BD6NFKdetRodrgOYdD2kh5SZQTK3n0gUWubjB9IDDu-TieJCoAOwBa6S2Vz7sEg1FWUsW8VtpJpo5uIxSE2vbBgThltt3YMXVLGyT8YHbw0SjUA7FqcD0EQAaYc806Z1_7DIpFXNNLtFw5PTYq-bFIlzv-ep2wyTyLyaJHgAQ1zRfR-TsXPV__y8gXXm6vtjRAtvfgzvYd9vuRmrPX5TQve5jBp2siKiQb6HX59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل مدعی شد ترامپ و مقامات ارشد آمریکایی طرح عملیات گسترده‌ای در تهران و شهرهای بزرگ ایران را بررسی کردند و تصمیم بر گسترش آتش دارند.
تا پیش از این عملیات های نظامی محدود به اهدافی در جنوب ایران بود.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/18776" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/18775" target="_blank">📅 17:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18774" target="_blank">📅 17:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ولایتمدار، عضو کمیسیون امنیت ملی:
به‌زودی دولایه از مسئولان آمریکا و اسرائیل را قصاص می‌کنیم
مردم نیز خود را برای تحمل شرایط سخت آماده کنند</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/18773" target="_blank">📅 17:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKEvu868P17te8DZZgBO3t9D2Uv7-alKzxrVJk8PDAXKN6gS6J_qnFZ0uU95YBP7GoHgFmb29eu0-m6oBdkPaTxls3UTtC3bHKjjsiEpK6c4f9Xl93DYpP2SzCCJwDfNIhtiu_3CI2Ia1VbK6QaCw8Q8QorGRcgQJunmvRObaWydUZsp4nm7aHrrUNgSRUJr7duwgyp5Fsyaamm_pQOmXAA2YXUBJO2eAUZ872r7Jv4m0cc67-HUS8BWyQL9UMlNkI3gL0aNZ8UJfC3utNtVpBOV5vnIkbsJdLcF2YMYBLQK3UcO3oiteZewcvgE2LkgcMUT0vgC5i3XRwdmP7vf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX5cxNbTUuFLHlb_TF48TnBKds21koYK-v8eMl1YTds8rn3rjB71GRdNLswceDjDIWO6qJxhA6vOmoJeIBASJODUUucOea0W5jBYqh7SPRLd7feynWRxXZ5aPfI3sTsCoQYX1ESu-jFXlWlQDEtdQBnXCDhpnWlbngKD6okSVn1ap6tRLFgB_05vGYTblg8VFSLsbLYlx8MtaDJ_vcnhh-jbvc4p-qQxLccQza8vJ_Uxf72ohZLyB973gSfMKaOFSv28Ro_ocnGrq1CD5qvcH2lrNQ1485-F_Kid8GMR0LkjwS440G6sQGMWwT_TgjPKrlfwarrmq5cqlpsfExBg1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک نشست امروز با نیما  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/18771" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIptvv7yifLH_y-NftoNnS83-e65MVqW2NM9UteEWpWOgn0hE7c_kVdKZnyaj4KG4MiQKWCPbVPMFEXDxE0a-Fi_gAbgvjzFMdxDVuwD4Tql798-NHTu-dFYs-2BXAqd412iL_gtK_H1Zn9bt4XVl231Bo3v9EhaG-J-sq5AGuP7PuFk93N-DRERzckwYPYrz7cGh0cg4n2mOMzMeNVfqQYMTjD41oVEb6lJmesXEpYImffqHo2vudieU7JSJMV1fji1DUYLN8N9W5bl9FPrcyxCmEa2OUJpU3uzYao55N7ENbN3vwpZFZv77NtRobrwdTWQ-B58Qsy1gR8iWic85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک
نشست امروز با نیما
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/18770" target="_blank">📅 15:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg2sOrtNienOxSmv2zm3sO1_EsiBi4SAJD8KmeHiHVw_sbLOte3Ggt02u1SYcYeX7rVHFDOHhflE3wPruf5av31MgHuMbbL723eypaortRJb0WHF_JVK54I6bmDyuJj7JYOZU0aHlyLQ5AjHyIVcNIZVpwQtUb7QDV1QUmyvvqsJo9HzL4qu1psmErHDK6OWyWeVA9RBm0PgHExOCLilf_mR9A157YVJye0dEhqN-D_3NTLeH23__k1RDCKNaZKTDKzbzE83dmVo0IJoHLMrE5qMJRsRqEe54GSYUMnZlEeH7_B8alfIzxx9w6HMWRtoUvaLzDSlgw_oKy5af8llAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خریدهای تسلیحاتی اشتباه ارمنستان — بخش ۱  این تحلیل توسط یک کارشناس نظامی روس نوشته شده و لزوما همه اش مورد تایید من نیست.  گفتن اینکه وضعیت استراتژیک ارمنستان نامطمئن است، دست کم گرفتن مشکل بزرگی است که ارمنستان با آن درگیر است. این کشور کوچک عملاً توسط دشمنان…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18769" target="_blank">📅 14:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجار در شیراز !</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18768" target="_blank">📅 13:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=HxvCSyJRws5Wnlc2yKcxgbVGSzj66PoCUAX6f2tke5IE3xEjiej3lnMoAxYuHEm3mLZ7RycZfvziBwBXAv8N_kaBMxEiQSzUHIRjMYD_eh6St8ysnyu7MVSGWC54kJrMw9Y3pCRYgUvNPW2t-2mpm2rbkQmXuG74sw0aG0vN1fOeHHwlGEqrlbjMFbSSD2CeZPNXfKEckPGS-fUdmifQt1XrIVpufiSqc2-pjRH2mDh2h2Fnf9ulkQwkrjnO6_0-nhW8WoWvzYMxIbVKEIaRFbqj24hvMAUA387TwcgpduNiL7swyfwY4ETN6JEqxaO7dzhR12zNoP54YgIZaajQYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c67f12a39a.mp4?token=HxvCSyJRws5Wnlc2yKcxgbVGSzj66PoCUAX6f2tke5IE3xEjiej3lnMoAxYuHEm3mLZ7RycZfvziBwBXAv8N_kaBMxEiQSzUHIRjMYD_eh6St8ysnyu7MVSGWC54kJrMw9Y3pCRYgUvNPW2t-2mpm2rbkQmXuG74sw0aG0vN1fOeHHwlGEqrlbjMFbSSD2CeZPNXfKEckPGS-fUdmifQt1XrIVpufiSqc2-pjRH2mDh2h2Fnf9ulkQwkrjnO6_0-nhW8WoWvzYMxIbVKEIaRFbqj24hvMAUA387TwcgpduNiL7swyfwY4ETN6JEqxaO7dzhR12zNoP54YgIZaajQYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18767" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منوچهر متکی:  باید برویم پایگاه های آمریکایی ها در منطقه را تصرف کنیم و بعدش صد نفر از سربازان شان را اسیر کنیم بیاوریم ایران!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18766" target="_blank">📅 13:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18765" target="_blank">📅 13:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aex-UDhtemjlqwA6JBodgiOdt-b-uDnjGqtjjK9J6R37RV0CZT9jbL07TcEyRqejZrFFa_LWHYmRmE72qQEaLat6svLBqOXiFWf4JGuVkN86RgYe41bVGlyIUxhz13sjqHy2ABOWMNZBBgcKxUZa4dQyC54n-nYadyiA3EAxCLG1lsakZc3CL3SnerkYuWg_HLvVBiNCF_RcjceVPMeBFeGhgrgADx28wLWquc_mBsDuCdNq580B-lr2puCDI2dmQSrEQkG_oKjL7lS07sA1Vky57BpXI6ShQH44yuD_YV9xw31Hi8wo17ROwOKVsDaq-owKnpji3gBp3RMUD9HXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.  وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18764" target="_blank">📅 13:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک جنجال شدید در بالکان به وجود آمده. پس از آنکه وزیر صربستانی، سِنیژانا پاونوویچ، گفت که اگر جای اسلوبودان میلوشوویچ بود، پاکسازی قومی در کوزوو را انجام می‌داد.
وزیر امور اداری و خودگردانی محلی، در یک مصاحبه تلویزیونی روز دوشنبه (شبکه تلویزیونی کوریر)، گفت:
"اگر جای اسلوبودان میلوشوویچ بودم، در سال ۱۹۹۸، پاکسازی قومی را در کوزوو انجام می‌دادم. این سخت‌ترین بیانیه‌ای است که تا به حال بیان کرده‌ام."
وزیر کشور کوزوو، ژلال سوهلا، دیروز گفت:
"من تصمیمی را امضا کرده‌ام که بر اساس آن، سِنیژانا پاونوویچ، شخص ناخوشایند اعلام شده است. ورود او به کوزوو و عبور از خاک جمهوری کوزوو به طور دائم ممنوع خواهد بود."
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18763" target="_blank">📅 12:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دقیقاً چه مدل آمادگی مدنظر هست لطفاً قید بفرمایید.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/18762" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محمدجواد لاریجانی:  مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18761" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محمدجواد لاریجانی:
مردم خودشان را برای یه جنگ سه چهار ساله آماده بکنند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18760" target="_blank">📅 12:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntYDpLnoRuT9oWhEVl63pLNa0ZLE5zBODXGLhkCFcKddP70HqsI_NAxLFpOioEEGB3nbmPh0be5OCijthu5VDK0I464Fbtz6HC_T4jzF6WKX3UWqEtqyxsnNZSFpHuCTgQQ8E1-tis1xaUQKX8Zq-8H-gIg5l4Mebh9scnSSFgV1ALBdbZIo9_DDEQzfmXseqpwcAqLWV-JY3lF0Hqr-ZyVYySYfb_f76UUcPh7Svav1XacJqEKyw-ZyC7oCwd8CdEJ2Ie2e3mNQcFMYwGyj_QZVUU58DFCvUwv8lumXGPBPXfLkdV9pgfpcBxGHM5k7V4P8AAAIxpyBf9Bn2Phb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و تا زمان انتشار گزارش PPI بعید است حرکت صعودی خاصی در طلا و دیگر دارایی های روبروی دلار داشته باشیم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18759" target="_blank">📅 11:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔔
#دلار
تهران =
187,000
#تتر
(تومان) = 186,340</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18758" target="_blank">📅 11:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ:
ما امشب به شدت به آن‌ها ضربه خواهیم زد، فردا شب به شدت به آن‌ها ضربه خواهیم زد، و شب بعد نیز به شدت به آن‌ها ضربه خواهیم زد.
و سپس، هفته آینده اوضاع برای آن‌ها واقعاً بد می‌شود زیرا هفته آینده نوبت نیروگاه‌ها و پل‌ها می‌رسد.
ما تمام نیروگاه‌ها و پل‌های آن‌ها را از کار می‌اندازیم.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18757" target="_blank">📅 02:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزارت امور خارجه آمریکا: وظایف مرزی و گمرکی درمسیر TRIPP  تحت کنترل ارمنستان باقی خواهد ماند.   وزارت امور خارجه ایالات متحده در مورد مقررات اتحادیه اقتصادی اوراسیا در مسیر TRIPP اعلام کرد، تمام وظایف امنیتی مرزی و گمرکی تحت کنترل ارمنستان باقی خواهد ماند.…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18756" target="_blank">📅 00:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ارمنستان به اظهارات ترکیه درباره « کریدور زنگزور» واکنش نشان داد و گفت کریدور بنام زنگزور وجود ندارد  وزیر مدیریت سرزمینی و زیرساخت‌های ارمنستان داوید هوداتیان در مصاحبه با «آرمن‌پرس» به اظهارات اخیر وزیر حمل‌ونقل و زیرساخت‌های ترکیه درباره اینکه به اصطلاح…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18755" target="_blank">📅 00:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18754">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فارس:
چندین انفجار در بمپور و چابهار شنیده شد، علت نامشخص است</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18754" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18753">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدیده‌بان سرمایه</strong></div>
<div class="tg-text">⚠️
۲ مجمع، ۲ شرکت، ۱ آدرس، ۱ سهامدار عمده: آقای زنوزی
📍
آدرس مجمع
#خبنیان
استان آذربایجان شرقی، شهر اسکو، دهستان شورکات جنوبی، روستای سرین‌دیزج، خیابان آزادی، جاده
تبریز - جزیره اسلامی
، پلاک ۰
📍
آدرس مجمع
#درپاد
استان آذربایجان شرقی، شهر اسکو، دهستان شورکات جنوبی، روستای سرین‌دیزج، خیابان آزادی، جاده
تبریز - جزیره اسلامی
، پلاک ۰
این دیگر «محل برگزاری مجمع» نیست؛ این یعنی بردن مجمع به جایی که هرچه کمتر دیده شود، بهتر.
🏛
شرکت بورسی قرار نیست مجمع عمومی را در نقطه‌ای برگزار کند که سهامدار برای رسیدن به آن، از شهر رد شود، به دهستان برسد و آخر سر در روستا دنبال حق مالکیتش بگردد. مجمع عمومی، عمومی است؛ نه جلسه خصوصی سهامدار عمده، نه مراسمی دور از دسترس برای خلوت کردن سالن.
🚧
وقتی آدرس مجمع از شهر عبور می‌کند و به دهستان و روستا می‌رسد، دیگر سخت است کسی باور کند هدف، تسهیل حضور سهامدار بوده. این مدل انتخاب محل، بیشتر از آنکه احترام به حق حضور باشد، شبیه مهندسی غیبت است؛ یعنی مجمع را می‌بری جایی که کمتر کسی برسد، کمتر کسی سؤال بپرسد و کمتر کسی مزاحم تصمیمات از پیش چیده‌شده شود.
📅
آن هم در تاریخ
۳۱ تیر
؛ درست در اوج فصل مجامع. یعنی هم‌زمانیِ شلوغ، آدرسِ دور، و برای
#خبنیان
حتی نبودِ صورت‌های مالی حسابرسی‌شده روی کدال. یعنی محدودسازی سهامدار، هم از مسیر جغرافیا، هم از مسیر اطلاعات.
📉
این دیگر فقط بی‌نظمی نیست؛ بی‌اعتنایی صریح به حق نظارت سهامدار است. سهامدار را هم به نقطه‌ای پرت می‌فرستند که رسیدن به آن سخت باشد، هم گزارش را در مهلت قانونی روی کدال نمی‌گذارند.
🔁
وقتی در
#درپاد
و
#خبنیان
الگو یکی است، آدرس یکی است، مدل رفتار یکی است و سهامدار عمده هم به یک منشأ مشخص یعنی آقای زنوزی برمی‌گردد، دیگر نمی‌شود این شباهت‌ها را تصادفی دید. این بیشتر شبیه یک الگوی حکمرانی است: استفاده از بورس برای پول و اعتبارش، بدون پذیرش شفافیت، پاسخگویی و دسترسی‌پذیری.
⛔
اگر قرار است سهامدار برای حضور در مجمع، هم با آدرس بجنگد، هم با نبود گزارش حسابرسی‌شده، دیگر اسم این را نباید «برگزاری مجمع» گذاشت؛ اسم درستش بی‌اثر کردن حق مالکیت سهامدار است.
🆔
@FinancialmketAnalysis</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18753" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18752">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محاصره آمریکا بر ایران دوباره به صورت رسمی آغاز شد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18752" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18751">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه پاسداران :
اگر آمریکا به «اقدامات شرورانه» خود ادامه دهد، «یک قطره» نفت یا گاز از منطقه خارج نخواهد شد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18751" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18749" target="_blank">📅 22:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttFI_h734DOw5R-YQUzIYQtQXJsnVEhVS0lvTKLyVuu-SJPMPvWn91WxAqQENDJhW2Qy5RYGuHDrkVTB5uKpAuTVm9ocgl3y2nJ8OlvgAwPP_NARESkKN-z0EpNgYJ5FFwtDoPA98dVB_WT8VO5XOmodJMO2GgOSA2suIsrhqcT4o-6pA5NB30oLrXA5ODoSq3XKd0NJQKCXqz22TKnONDBtPajH2Z8Cqjoq2v2Xyt9kf8cJYpWy4bnDu2reijYM6nDCkLjJBdNxlORHWhNEsjLDGp0v3CVl-h_KwtqJHpClO8HtlhsMIalMwDw2CJu0TOcU5Bg5T1XENwtWpTs-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید مرندی:
برای چند هفته دولت ترامپ در حال تدارک حملات هوایی گسترده و تهاجم زمینی به ایران با حمایت چندین کشور عربی است و  ایران بی‌سروصدا خود را برای یک رویارویی بزرگ آماده کرده است.
در صورت آغاز چنین عملیاتی، آن حکومت های عرب خلیج فارس دوام نخواهند آورد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18748" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!  این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18747" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک مقام آمریکایی تأیید کرد که نیروهای آمریکایی در حال حاضر در ایران حملات هوایی انجام می‌دهند.
شبکه ABC|</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18746" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18745">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پایگاه شیخ عیسی و ناوگان پنجم آمریکا در بحرین در معرض حملات موشکی شدید قرار گرفته‌اند
خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18745" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18744">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ به نتانیاهو دستور داد نیروهای خود را از سوریه و لبنان خارج کند - آکسیوس</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18744" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18743">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=vFN2zhdq0WK-HUP1GLZKlC4SKn2_JaImK151L_oRZyGHbfo-egPICOcEpP1kz1hqR-AO-7uf3-id17vI7hG5BpzCkf5bzmut2IEd9ltlkJggia-Qywv6HJz5iF6vlWShy4jGbZsDpO4ZpuQsYhi5HXxPn1nVHUdbOHFJ-gdsOvhnTLVqDLK0sHtR-yZz998UALr2xQaOW0GuYmBPN5ZM_mxnF9TwDuWZVWXfnHWrDTkEHSxj2tlpmgIJyMX8CnI46EoO3xo8FAG627lZ_06NqJ3avenctsn3245f_cFQg2Njm9_OT_W2eqO2muG1nne3hhe1Sbnj5OoqR9RF48TYbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52c0b59bc.mp4?token=vFN2zhdq0WK-HUP1GLZKlC4SKn2_JaImK151L_oRZyGHbfo-egPICOcEpP1kz1hqR-AO-7uf3-id17vI7hG5BpzCkf5bzmut2IEd9ltlkJggia-Qywv6HJz5iF6vlWShy4jGbZsDpO4ZpuQsYhi5HXxPn1nVHUdbOHFJ-gdsOvhnTLVqDLK0sHtR-yZz998UALr2xQaOW0GuYmBPN5ZM_mxnF9TwDuWZVWXfnHWrDTkEHSxj2tlpmgIJyMX8CnI46EoO3xo8FAG627lZ_06NqJ3avenctsn3245f_cFQg2Njm9_OT_W2eqO2muG1nne3hhe1Sbnj5OoqR9RF48TYbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشک ایرانی پر از منور بر فراز بحرین!
این منورها پدافند موشکی را فریب می‌دهند تا با شلیک های پیاپی، ذخایر موشکی شان دچار فرسایش بشود.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18743" target="_blank">📅 21:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18742">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599f22b724.mp4?token=iGzlqjD0dDPb2UA2g2nkv90DlZjvSLgO8V45L9Y_SF7U6aACdP8GC6xTWS6ofZg1HQ0G88JiAuA7ndBp_vilVPLkZJ1Zv9Fd5MTqZjZxGFlo-uMfkh8Ywiij-8cDfeENKE6frKwCupAM_YAuNA1G6OUEIpw-vQV7LknMNAZNp9xo2JeLgC5aOZDCxfA_AQoUKwKUOHuwo3A5VfQ3C3d6uJkgqQU0Ry6hzDJ_BasYiw7f5PhrPIAWHo6X5zC5QW1D8D-4fBWgUthL2keaSYo_Pd6V3m43FrqlhVrbJ7AiK-fvzVbq09JLELNB8fzD85cOpy6RKnKlm1tZlchVhOEc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599f22b724.mp4?token=iGzlqjD0dDPb2UA2g2nkv90DlZjvSLgO8V45L9Y_SF7U6aACdP8GC6xTWS6ofZg1HQ0G88JiAuA7ndBp_vilVPLkZJ1Zv9Fd5MTqZjZxGFlo-uMfkh8Ywiij-8cDfeENKE6frKwCupAM_YAuNA1G6OUEIpw-vQV7LknMNAZNp9xo2JeLgC5aOZDCxfA_AQoUKwKUOHuwo3A5VfQ3C3d6uJkgqQU0Ry6hzDJ_BasYiw7f5PhrPIAWHo6X5zC5QW1D8D-4fBWgUthL2keaSYo_Pd6V3m43FrqlhVrbJ7AiK-fvzVbq09JLELNB8fzD85cOpy6RKnKlm1tZlchVhOEc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دیگر چه کوفتی است در شیراز ؟!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18742" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18741">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به نظر می‌رسد حشدالشعبی هم …</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18741" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18740">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
به نظر من، و این ممکن است برایتان عجیب باشد، اما خاورمیانه در حال متحد شدن است.
ما در حال از بین بردن زورگوی خاورمیانه هستیم.
ایران، زورگوی خاورمیانه بود. آنها به عراق زور می‌گفتند. آنها به هر کشوری زور می‌گفتند. در سراسر خاورمیانه، ترس وجود داشت.
دیگر هیچ ترسی وجود ندارد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18740" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18739">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مهر نیوز با استناد به منابع خبری گزارش می‌دهد که رژیم اسرائیل حملات خود به جنوب لبنان را ادامه داده و آتش‌بس را نقض کرده است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18739" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18738">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18738" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18737">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18737" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18736">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=jIt_oMHWTBsL2nQ7kgwcuEWyrPaFI4GrYK-xB3QNxiYwAt8jVQmflDc1jpz9npaWXvWYR8h4stOtGAlYlJ1HYxQQCD-SlzDfsyydSnJha1-Nh7KXz1oob_4zcyIr-raZvhaQRG30bUusPbF1jINmALWEuWBvf2DSqo2uvC8SuBx1rhKfgbQJiVwklctsyn1a5wHUQDIyZ062MPRZ8fkE6Su5YGstLwptyYZcmsJuS1Jc0PCOD8QKkijwjJ2U1-N5XiVi9vSUsSleMNqATP0OB2bIJQNr8MxgvMYJUl_F05aZuCNEBUZNIuKAZNBPkq5ISPQg7_Z5OqtuTt7E4ST4fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8fda31b18.mp4?token=jIt_oMHWTBsL2nQ7kgwcuEWyrPaFI4GrYK-xB3QNxiYwAt8jVQmflDc1jpz9npaWXvWYR8h4stOtGAlYlJ1HYxQQCD-SlzDfsyydSnJha1-Nh7KXz1oob_4zcyIr-raZvhaQRG30bUusPbF1jINmALWEuWBvf2DSqo2uvC8SuBx1rhKfgbQJiVwklctsyn1a5wHUQDIyZ062MPRZ8fkE6Su5YGstLwptyYZcmsJuS1Jc0PCOD8QKkijwjJ2U1-N5XiVi9vSUsSleMNqATP0OB2bIJQNr8MxgvMYJUl_F05aZuCNEBUZNIuKAZNBPkq5ISPQg7_Z5OqtuTt7E4ST4fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:
او جوان و خوش‌تیپ است.
من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18736" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18735">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18735" target="_blank">📅 19:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18734">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به گزارش‌ها، حداقل چهار موشک بالستیک ایرانی شب گذشته پایگاه هوایی پادشاه فیصل در اردن را هدف قرار دادند.
گزارشهای تصویری نشان می‌دهند که سامانه‌های پدافند هوایی نتوانستند این موشک‌ها را رهگیری کنند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18734" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارهای شدید در جنوب ایران و شمال کویت!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18733" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:  نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.  ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18732" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18731">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJgPcRnGn_-8O9MKEEifaubLCrgW4Isawv5BFdUC1hLI0nywdPWdJVv1gT9H-bCN-KL7ZIuG4cV3d9GcsNiynOLCFoagUh83C6RIOHOAtiS7GEB-v8ahJi1kRgB9SXX_n75VLqiiQPIXCkvN5HLSh454l9p6t4hCKy60v2nDvoAgmomnh3Y2p92s8Sili9epk7LzEdPwAENrViwa81_CKEd0HYea2L1EQ0qvhDuv0EvKfzytCPcoBe6SkEsBA_LBDvUm8v-ZVsPCxequGvsfhMz-khzSNl_7zq3MlUu-ZUaLa002eAOLF9qgwXUnGp9o-xXMLB3BkauLF1-P15LRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18731" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18730">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هدف قرار گرفتن یک تانکر نفتی که پرچم لیبریا را به اهتزاز درآورده و متعلق به امارات است.  3 نفر از خدمه کشتی در میان مفقودین هستند</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18730" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18729">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هدف قرار گرفتن یک تانکر نفتی که پرچم لیبریا را به اهتزاز درآورده و متعلق به امارات است.
3 نفر از خدمه کشتی در میان مفقودین هستند</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18729" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18728">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:
نفت مانند گذشته بی‌سابقه‌ای در جریان است. تنگه هرمز به روی همه کشتی‌ها به جز ایران باز است - به دلیل رهبری دروغگو، خشن و بدخواه آنها که آنها را در مسیر نابودی کامل قرار می‌دهد.
ما محاصره کامل خواهیم داشت، اما فقط کشتی‌هایی که به بنادر ایران می‌آیند و برمی‌گردند، یا هر چیزی را که مربوط به محموله‌های ایرانی است، حمل می‌کنند.
من تصمیم گرفته‌ام هزینه بازپرداخت ۲۰ درصدی ایالات متحده را با معاملات تجاری و سرمایه‌گذاری که کشورهای مختلف خلیج فارس در ایالات متحده انجام خواهند داد، جایگزین کنم. این سرمایه‌گذاری‌ها عظیم خواهند بود.
روزهایی که ایران صدها هزار نفر را می‌کشت، به پایان رسیده است و از همه مهمتر، ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18728" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18727">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!  به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.  روسیه هم متوجه…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18727" target="_blank">📅 15:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18726">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6ux2eIgZRsdYIGcO1jmf5EP7I_14Y9x8XESdY49NZLNNZ_ng0R4zv7UNWceOG7qm8YtxZXHHT--z5aMR22P_S6zv_xHrfwp02yd9qgsZU3yvQPVszsrWCUy4-BMFYD5Wrqx0IYiwxq4hWD-mmc6o6eRyPJN7cM_FjWlDIWWbszfBZZDpX0KG6QXDeD3_BdJqv2iBc9c-yD45niol73XkQ7odVxVLPq_BTxVMQ_9qJmFwLYtbrKk_qc8PAOeIsrPXIs2Dr785DSfLqJvvKK8rcvFTw3d7qwcHxFXHkYj0ZVvmAPvAorMz4yOPBIUyBNHmOldOGKTCqH2oyT5gWejFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!
به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.
روسیه هم متوجه تلاش‌های جاسوسی فزاینده چین در میان مقامات دولتی رده میانی شده است، اما مسکو تمایلی به مطرح کردن این موضوع با پکن ندارد، زیرا از آسیب رساندن به این رابطه می‌ترسد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18726" target="_blank">📅 15:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18725">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شهادت ۳ نفر در شهرستان حاجی‌آباد بندرعباس
🔹
بر اساس پیگیری‌های خبرنگار تسنیم از استانداری هرمزگان، حمله به مناطق غیرنظامی در غرب بندرعباس و شهرستان حاجی‌آباد تأیید شد.
🔹
در روستای سیدجوذر به یک ساختمان محیط زیست حمله شده که ۳ نفر به شهادت رسیدند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18725" target="_blank">📅 14:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18724">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhb7njBY1sJFBiNv-vLXiVtZtZ1RkzUdmWZ3LphuKFrD0ZOxl_fRlSUTMdlk_DyBbI35T5bMP_WjPS9sKCxfD0vZDRbyZPcne2IWLMA6sWrVoNorJggOIaCfJjLscIXgKHCg3nK5s9hSKfvVZ57mc9dDoGiKoOrXukHmYLlAVtPHAnGPXgqTe_VA4JAFRpoUtWa6wq4WIMvH2x_UKVUotdjlFn6dwItwkPw2WGLbs6PkG3Gj5-LD1z2bwnrHpD6PDIo399sEkN-1IR8jWKERbhy0zOFpQrZkNVoO7LyQHi6nqIpzVjJ_dnnpVb8N19Lmmt8Ay0F0bVS3naixAwYU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی که دیشب به ترامپ توصیه کرده بود برود نگهبان قبر لیندسی گراهام بشود، همان دیشب از هیات رییسه کمیسیون امنیت ملی مجلس کنار گذاشته شد!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18724" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18723">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18723" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های دولتی ایران، حملات هوایی آمریکا به چهار نقطه در شهر بوشهر، ایران، انجام شد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18722" target="_blank">📅 14:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ضربه قایقهای انتحاری آمریکا به تاسیسات صنایع دریایی مواردی را آشکار کرد. ارتفاع قایق نهایت 2.5-3m باشد که رادارها سطحی توام با کلاتر دریایی کمی دیرتر قایق را میگیرند اما  باز هم چندین کیلومتر فرصت دارند (رادارهای پر ارتفاع؟).از آن سو ج.ا مدیریت شبکه محور روی عبور قایقهای خودی ندارد، میتواند با آنها اشتباه بگیرد.
نظارت آمریکاییها با پهپاد از آسمان، گشتیهای سپاه را هم تحت رصد دارد که با یک عملیات شبکه محور از میان چند جزیره ایرانی به خوبی عبور کرده و خود را به سادگی به بطن صنایع دریایی رسانده است. در موقعیت شبهای بحرانی احتمالا گشتی ها سپاه و نظارت انسانی ساحلی هم کاهش می‌یابد، زیرا ریسک عملیاتی بالایی با توجه به تسلط هوایی آمریکاییها وجود دارد. در کل شکست عملیاتی جدی بود و رخنه‌های بزرگی را آشکار کرد.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18721" target="_blank">📅 13:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">توییت سازمان اطلاعات سپاه!  به تاریخ ها دقت کنید؛ مشخصاً راهبرد سپاه این است که این تاریخ های حساس برای آمریکایی ها خالی از جنگ نباشد.  از همین تقویمی که در پست ریپلای شده قرار دادم استفاده شده است.  11 ژوئن = تاریخ آغاز جام جهانی 3 نوامبر = انتخابات مجالس…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18720" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18719">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18719" target="_blank">📅 13:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9B6eWDOVtgpjgMKUvtTL2znsS6Hgki_Hts5fQVUgX2LS2eNk8gNoPhIADP8pOcY77DVZocUo6goBYSHYYfjU6eZ9h2H5Cc-hNxaEzHb15RmPvNjFB4f1XnDifA56eKoc6oEaFO80s64iB6WmoSSWCy7ZJgcfB0fOkxdoWnWUkRKb6Vnyz6BRWxJd2xu37wZ95qFrS4LHbg7dCD9y5L4rBcrADsIHFiW56F8uUGQndEIb6heyVSQPxVUDZokdLj26sABqGfjqWHx4pJdy2esA7_pOqSByRxEGSluJS1yn4YRYHP5ZMON_WDFbBUE3wXi91LOWnCDlh_BHPZSkDELDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی قرار دارد.
با توجه به انتشار خبر کلیدی تورم، اساساً این ساعات برای معامله مناسب نیست.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18718" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 7
سه شنبه 14 جولای 2026</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18717" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18716">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18716" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک نفر دایرکت داده خدا لعنتشان کند؛ دیشب ‌پیک اول را زده بودم برق رفت همه جا تاریک شد فکر کردم کور شده ام!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18715" target="_blank">📅 10:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18714" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18713" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18712">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزارت دفاع امارات:
در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18712" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18711">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارشگر: شما ماه‌هاست که ایران را بمباران می‌کنید. آیا این وضعیت عادی جدید است؟
ترامپ: ما ۱۹ سال در ویتنام بودیم در حالی که فقط ۴ ماه است که ما اینجا هستیم.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18711" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18710">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادعای وزارت دفاع امارات:
دو نفتکش اماراتی در مسیر جنوبی تنگه هرمز با دو فروند موشک کروز ایرانی هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18710" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18709">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قطعی برق در دمای 40 درجه به نظرم خیلی زیبنده ابرقدرت 4 دنیا نیست ولی خب.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/18709" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18708">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">راه قدس از بحرین می گذرد!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18708" target="_blank">📅 01:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18707">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجار در بحرین!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18707" target="_blank">📅 01:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18706">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تلویزیون ایران: دو انفجار در جزیره کیش، در جنوب کشور، رخ داد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18706" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18705">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:  محمد Something آنجا وجود دارد که نیاز به بیل دارد.  بیل‌ها به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18705" target="_blank">📅 00:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18704">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ادعای ترامپ:
عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18704" target="_blank">📅 00:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18703">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز جمعه ۱۰ ژوئیه به طور رسمی کنگره را از ازسرگیری عملیات نظامی علیه ایران مطلع کرد و تعهدات خود را طبق قانون اختیارات جنگی انجام داد.
این اطلاع‌رسانی پس از ازسرگیری حملات آمریکا به اهداف نظامی ایران و بازگشت محاصره دریایی این کشور صورت می‌گیرد که در واکنش به حملات مداوم ایران به کشتیرانی تجاری در تنگه هرمز و علیه منافع و شرکای منطقه‌ای آمریکا انجام شده است.
طبق قانون اختیارات جنگی ۱۹۷۳، رئیس‌جمهور موظف است ظرف ۴۸ ساعت از ورود نیروهای مسلح آمریکا به درگیری یا شرایط قریب‌الوقوع، کنگره را مطلع کند.
این اطلاع‌رسانی به خودی خود مجوز اقدام نظامی نیست، اما الزامات گزارش‌دهی این قانون را برآورده می‌کند و کنگره نقش نظارتی خود را حفظ می‌کند</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18703" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18702">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ درباره ایران:
حفظ تفاهم نامه نوعی آزمون بود.
آن‌ها به این آزمون احترام نگذاشتند.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18702" target="_blank">📅 00:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18701">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آسمان کلیر، پرواز چند جنگنده خودی در اطراف تهران!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18701" target="_blank">📅 23:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18700">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_7MToYvrNiWN0jYISDMM8hJzRPgV5VtiSCRsCUwqShxRatsEXaC1R1ejPg_78N1hGCa-AoafrfQg7Sl-U0KoDoGoZqFeo7m2ksXEj1UpuUe2aU51fzelxFgf7yPtv_k043q-YqumHFWraNU6U8TBBHn6XK5zzF7_I_WT9Bp9lFLzR9gDQdPju4Ywxo28AXDF214HoqJJtg4UlRYUyDRjdk8OJ1U5OeUhVa3n3Afmz5HulGcPAsDXnp747IHKpFM-anfosowk3MuXA5quQC9UxJRjiggOtu7ZiT3eWQiABB0aMdN8AiExXKHQMV1cyIwrSPNQT39RrPg2Iq54b1HFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان کلیر، پرواز چند جنگنده خودی در اطراف تهران!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18700" target="_blank">📅 23:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یحیی سریع سخنگوی نیروهای مسلح یمن:
در پاسخ به تجاوز جنایتکارانه سعودی، نیروهای مسلح یمن با تعدادی موشک بالستیک و پهپاد، عملیات نظامی را با هدف قرار دادن فرودگاه بین‌المللی ابها انجام دادند
به همه شرکت‌های هواپیمایی در مورد پرواز از طریق حریم هوایی عربستان سعودی هشدار می‌دهیم و از آنها می‌خواهیم تا زمان لغو محاصره فرودگاه بین‌المللی صنعا، هشدارهای ما را جدی بگیرند.
ما از جمهوری اسلامی ایران به خاطر کمک‌هایش به جمهوری یمن در لغو محاصره ناعادلانه فرودگاه بین‌المللی صنعا و تسهیل پروازهای بشردوستانه به و از فرودگاه، صمیمانه تشکر می‌کنیم
.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18699" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18698">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18698" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش‌های ایران از موج انفجارها در چندین مکان در جنوب
منابع ایرانی از وقوع سری انفجارها در چندین مکان در بخش جنوبی کشور گزارش می‌دهند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18697" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ارتش آمریکا اعلام کرد که از ساعت ۲۰:۰۰ به وقت گرینویچ فردا، محاصره دریایی تمام بنادر ایران را آغاز خواهد کرد
.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18696" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیویورک تایمز: ترامپ رسماً کنگره را از سرگیری جنگ علیه ایران مطلع کرد</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/18695" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عقل ندارند. خب الان کله زرد می‌گوید من ۲۰ درصد میگیرم ده درصدش یعنی ۲ درصدش را میدهم به شما!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18694" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عباس آقا عراقچی:  رئیس‌جمهور ایالات متحده کاملاً حق دارد. هر کس که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تضمین کند، باید برای این خدمت عوارض دریافت کند.  ایران همیشه نگهبان تنگه بوده و تا ابد نیز باقی خواهد ماند.  ۲۰٪ البته خیلی زیاد است. ما منصف…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18693" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
