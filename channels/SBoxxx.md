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
<img src="https://cdn4.telesco.pe/file/KJ34VsenenYiXm5M8hcfGZmdzvsQ6IDpMya_LnCReZpdk2rwLnXdwN2zppWKYuVcpy0HbwRjkZKS8BZgpQk1PwcJwY_NRbYcV1HC3ffj2tbuV313hxnF6HQS7RxWpJHWIhizFbbwJfmGUMytAKFo3XfUUo7LVJjAv4AgZ7ialwZSzISiThanyFrhOilcojwk1yP58T5wxqC2AyLQ4D9NKaPMSOlLg5-MlY6rYSPqrBblBWDwdPN3eCgVCalXsiI6wke7Eki9XUPiR1ygMDmYnm95Y3FapoJvRoSglWH0OjtG9SUr_WMCDM4xaL2DotBV3_1I1nfV0SRbEl1hoLSPEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 05:23:27</div>
<hr>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akXOJYbgFnT-4QL6_FdtEVflFIClw5V-_4UG2goF7pmAl6_QdfQ6DeBfOhYZQBuD0BUbWOxyI4x4I3n0CaoaAKNbnDElzLWmc6dNP2ZPLXUrRyzzyxzbwIfRblfbKB07RgaK4AKw9RAvTJ_gJGZUJo9fZ5Gj2nQGUGu6FedU9Dr7ZETEwiAastnsekuklZ0wU-z99xPIgZBbbz9iAKPAPCZ6-X174EsCDBKP0dEUEKwKUM4MiEu9vDbvle_6Py0xZzFFpmae0PJgTejTP9f8dtic2QxBKRW65n4EgzXxABk2hjLMvt3qWJXuRbQXWI2pDzYtW0dZIFoFo6lVca-B7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
شب خوش</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/SBoxxx/18564" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNftcse7aDMY70V-sEQ6pzZc6V0kMFkVYx9rXIQM5CSsr7uJhJ2UfkLlwIidiauuvxzDwNDU3vx0tvnWGcbjYhKHW7pB7Dj-cEnoJS5gUp1kTS9uRRwf4WUQPrJ-3_lWwJ76HW_1YcDkdB-iPCmgugB38q5JY1LjBT8Cr3FBuRF9IDqkqSgvEFJP7J0gEhPJmLFRCM2c7h5jlNco8pULarSt0cUeWUsugisWVqeXHvrLMYeEORNUEzsLaKSgeytk0qm9oZCVI0diXaYpb2_LTs6zbCuKlNx_vnWZqcJXLV3LdXYQeaOIirdcjBOg497nye3TA41ja3htEDs6fBIh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدیم ما به اینها میگفتیم موشک ولی باز هر جور صلاح است</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/SBoxxx/18563" target="_blank">📅 04:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پرتاب راکت های هیمارس از خاک کویت و بحرین به سمت ایران</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/SBoxxx/18562" target="_blank">📅 04:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله سپاه به یک کشتی دیگر‌ در هرمز</div>
<div class="tg-footer">👁️ 796 · <a href="https://t.me/SBoxxx/18561" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برنامه مان اینطوری است:
نیمه شب: کل کل خداداد و جمشید خیابانی
پاسی از نیمه شب: حمله اصحاب شمال به جنوب کشور خصوصا به دکل سیریک
صبح: گزارش اژدهای بندر از نظم ایرانی در تنگه هرمز
اندکی بعد از صبح: حمله موشکی پهپادی سپاه به اربیل و بحرین و کویت
اذان ظهر: پاره شدن گوش ملت در پاکدشت به دلیل امحای مهمات عمل نکرده
ظهر: مثبت بسته شدن بورص به امید نتیجه دادن اکل میت
بعد از ظهر: قطع برق
عصر: ترامپ از خواب بیدار شده و می‌گوید ۱۰۰۰ موشک میخواهد در ما بکند
سرشب:سفر عراقچی به عمان یا قطر یا پاکستان
وسط شب: توییت های محمدسامثینگ درباره مهندسی مالی بعد چهارم سقوط بازار بورس آمریکا
آخر شب: هالند!</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/SBoxxx/18558" target="_blank">📅 03:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باور کنید اگر انتقام را به دکل سیریک بسپاریم زودتر جواب می‌دهد.
یک تنه دارد انبارهای سلاح آمریکا را خالی می‌کند!</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/SBoxxx/18557" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فوری | خبرگزاری فارس: دو انفجار در مناطق ساحلی سیریک، میناب و بندرعباس در جنوب ایران رخ داد.</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SBoxxx/18556" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SBoxxx/18555" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/18554" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر جنگ آمریکا:
ایران انتخاب اشتباهی کرد و اکنون هزینه‌اش را می‌پردازد.</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SBoxxx/18553" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کارشناس رسمی ارشد ایالات متحده:
از میان اهداف مورد اصابت، رادارهای نظارتی هوایی، تأسیسات ذخیره‌سازی موشک و پهپاد، سایت‌های پرتاب موشک و پهپاد، رادارهای نظارتی دریایی و پرتابگرهای موشک‌های سطح به هوا هستند.</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SBoxxx/18552" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش‌ها حاکی است بحرین و کویت در حملات موشکی ایالات متحده علیه ایران دخیل هستند</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SBoxxx/18551" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SBoxxx/18550" target="_blank">📅 03:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of Hormuz. A civilian crew member is missing and the vessel is unable to continue the journey due to an onboard fire and significant engineroom damage.
Iran was provided yet another opportunity to demonstrate adherence to the Memorandum of Understanding after being held accountable for earlier attacks on commercial vessels but has again failed.
In response, the United States is imposing a heavy cost by continuing to degrade Iran’s ability to attack civilian mariners and commercial ships freely transiting the strait. The strikes are being carried out at the direction of the Commander in Chief.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/18549" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فوری | مشاور سخنگوی وزارت امور خارجه ایران به الجزیره:
تأکید می‌کنیم که حملات اخیر آمریکا بدون پاسخ نخواهد ماند.</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SBoxxx/18548" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بندرعباس، بوشهر، عسلویه!</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SBoxxx/18547" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SBoxxx/18546" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/18545" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SBoxxx/18544" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امیدوارم کار به خوردن گوشت ناحیه خاصی از الاغ زنده نرسد.
سبحان الله!</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/18543" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SBoxxx/18542" target="_blank">📅 02:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/18541" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
به ارتش اسرائیل توسط نخست‌وزیر و من دستور داده شده است که برای یک عملیات نظامی مستقل اسرائیلی علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SBoxxx/18540" target="_blank">📅 02:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/18539" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:  افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.  آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.  امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/18538" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8wDfJjhP-PIgzGmh5_TPuNEmxkor6-BFfbqQtchs0zZz844_POqSk-Jkx2sDPyeb5_yY14iZ33F1EWXAnofnCkrYooJmtTVtb1nPf9_3AWL_vSmLjq0J47dELZe4XYlyUNCvdDW4rq5tdENtxX51kAsSTSXL7YFC9S_NwbVRCJPzSsdwP9XUpUrBOfXFbaqO38qIMCLkTsvtiDixTouyRgpV21LCgECfS0dn_LW50ZDlDHxP0a3ShMOATfCiDAvOV7TxfRfCti407UyEE8XQizGnxOHqcmiLhADqhibTlxvyx3jKozf91XQym5jRJ2_IWbvCQPt8IQ91COF63yyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.
آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.
امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار و کمونیستی، آمریکا را در بر بگیرد!</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/18537" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntl1Hi5B45YL7l7ByKN5edzloD3Cf8_2kEP4mF-ki1PTMhhp5eGxJOnqyyc6U7dLJ2b6rRARQmIRubKiSTD3hh_RgVEWAhPEpij0mqkmoiPUze_efBuDdtqlNgQu1uLYE508mIDK9FDc5roZWZZH6O4Ep2CdumeD_Sa5FhozCP1-NqsavAgd_JkUzw45-itYXvRcNXwWrTp6C8RxGkJieASwexdyqyU14WXELZc1VzXjoWLT3UamwmgIcw65hIcZKa4UXFJpPMhcWZBfYwr9OtMoW-2GmkLk32MMgbsuuELtwM3YxjKI7Xhz3KUTDTVjel5JhIqMoWvhRGA4S5z4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا من منیراً له لامنیراً له!</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/18536" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/18535" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/18534" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18533" target="_blank">📅 00:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برخی گزارش‌های غیر رسمی از فعال شدن پدافند هوایی در اصفهان خبر می‌دهند.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/18532" target="_blank">📅 00:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رئیس پیشین سازمان صدا و سیما:
انتقام از ترامپ به زودی انجام خواهد شد.</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/18531" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/18529" target="_blank">📅 23:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79f85bd8d.mp4?token=NcRXQoVi3wK1O9I51RxkUajX4b4X54_fQkErcny4NylgfTP5lvtnatagYLNwWcj-8o5E_pvlDA2V7LLSBY3_Zft6hxq3fGOV-Z7lke2SxEcdkJf6giqXbktW3EJuZdsWROjiISvpMISzPEJ1TAhhtp5jIuAQYZWLBWARW-PDxOQlDw4orjw2mPp2wGIZlbKjsltBJO3xTyyufIxZ1WTuJXPTJpqkySMSBsty4mlxX9lCRnC3wQh09JalNn43tAozGM2PPTCRigNm8oemiJlvmWW7ITVRvhaxFgdK7ZVNuCC8IYL_J5XVb5y2bbD0rYkjH5amdlpKzlCnk53ZPYtFBxMtvocyeiO8d9765e1dRc8HAZBWZs6v2n9ywvH6j_a9urgf31d3qO9W10ycayRPHY17YV6rbSXI46SqtSTShezFlFNvDeBjYMHSLCQzDOzAkh0bHopm4t69QRoO7ftIafrMWe_Z0tbkVL4-gRxVA0gTlnj0Jp0_pe1iB4EIBheJzDQ-_yeHrD0etJP2srQ_e_VOtLQI3L4wQiew65LS9FjCF-D7dZ2hphCbKdMmkKqApnybF9scqS0JPoSIqROPGkb4sPJkqP2plKkfsjTnnQGrqsiNoCktRCro_00dsAePuIV8MD2Tg8-qisumfmVvfSYS4rZogrKg3rE5mL64FvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79f85bd8d.mp4?token=NcRXQoVi3wK1O9I51RxkUajX4b4X54_fQkErcny4NylgfTP5lvtnatagYLNwWcj-8o5E_pvlDA2V7LLSBY3_Zft6hxq3fGOV-Z7lke2SxEcdkJf6giqXbktW3EJuZdsWROjiISvpMISzPEJ1TAhhtp5jIuAQYZWLBWARW-PDxOQlDw4orjw2mPp2wGIZlbKjsltBJO3xTyyufIxZ1WTuJXPTJpqkySMSBsty4mlxX9lCRnC3wQh09JalNn43tAozGM2PPTCRigNm8oemiJlvmWW7ITVRvhaxFgdK7ZVNuCC8IYL_J5XVb5y2bbD0rYkjH5amdlpKzlCnk53ZPYtFBxMtvocyeiO8d9765e1dRc8HAZBWZs6v2n9ywvH6j_a9urgf31d3qO9W10ycayRPHY17YV6rbSXI46SqtSTShezFlFNvDeBjYMHSLCQzDOzAkh0bHopm4t69QRoO7ftIafrMWe_Z0tbkVL4-gRxVA0gTlnj0Jp0_pe1iB4EIBheJzDQ-_yeHrD0etJP2srQ_e_VOtLQI3L4wQiew65LS9FjCF-D7dZ2hphCbKdMmkKqApnybF9scqS0JPoSIqROPGkb4sPJkqP2plKkfsjTnnQGrqsiNoCktRCro_00dsAePuIV8MD2Tg8-qisumfmVvfSYS4rZogrKg3rE5mL64FvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:
مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/18528" target="_blank">📅 23:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کاظم خان همه آن خودکارهایی که از این اسکلها بلند کردی حلال ت!</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18527" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری CNN:  پیشنهاد عمان شامل یک مسیر جنوبی از آب‌های عمان با عبور آزاد عادی، و یک مسیر شمالی از آب‌های ایران که نیازمند تأیید قبلی ایران اما بدون عوارض عبور است.  این پیشنهاد همچنان در حال مذاکره است، و مقامات ایرانی و عمانی در مسقط درباره آن بحث کردند.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18526" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری CNN:
پیشنهاد عمان شامل یک مسیر جنوبی از آب‌های عمان با عبور آزاد عادی، و یک مسیر شمالی از آب‌های ایران که نیازمند تأیید قبلی ایران اما بدون عوارض عبور است.
این پیشنهاد همچنان در حال مذاکره است، و مقامات ایرانی و عمانی در مسقط درباره آن بحث کردند.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/18525" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18524">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1h9crWeU3HE4CYpIlMZYNLobsJQOrZZ2RtMc1Sa1hWgPXZB6Myp0qjAcl67nJ6zHc6plNzpEfxJFzbMjGM1ONDuTMtcbNMEpcOHti8o_q-_j-yrYoQQrbwi3tDtJajEwtJ36GPWITAmzJjFOhcuLcG6Xw2KBniT--1yGT7oj0tzBaskXTBy2nyGYv4kWln6YCD3MGMMMHvFs1kgbwwmxD5lHe1lkToq9SLNL4emXOAKn6LO0SP6IwZkl-pr-UqPGnO7JUywXQarEYcm_pcrcPRhbv7q5c47n2zmEGkoMTwDE2kJwUu8Th6iTnsYgm-T2IvylwqE1HQYeiE3oik3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل داستان سر این است که ایران می گوید مسیر آبی رنگ که تحت کنترل عمان و تحت حمایت نظامی آمریکا است ناامن است و باید از مسیر زرد که در آبهای ایران است کشتی ها عبور کنند و پول عوارض بدهند اما آمریکایی ها می گویند این یک تنگه و آبراه بین المللی است و کسی حق انسداد…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18524" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1sfrZeOyL9oGIgF_PqkrmnRv2znXMrlXSvf5y4Z_1pYPd0bOxVXBcTe6XAej4wnOkq1u-CzA1iUeWocQy-G9PbokEKdQYauxZq_6Jk3Z9qjnhvVo4lLC3eiGbor8nGNoGgT59BVNmQ2RKW6BpVQul_lZBssPkqi4Gsg578it7vmJS3ALgFv--o2_ykKFM4T42IYls5OL1yrQsClF9IgRRI9hSzlFAq-futyr4vMVwL-HZmiXryjBvYrz1y2L2iFYzr6DdOZAp2fX7UjcJ6aVwUp-EdpYZrf1hufbXTqNAdf0_-0CL5P5pjp1jpIsHPfFtwhK6bmnWGVnitGgW07hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار مهیب در منطقه مستونگ، در بلوچستان پاکستان، گزارش شده است. این انفجارها به حدی قوی بودند که امواج شوک آن‌ها در سراسر شهر احساس شد.  وضعیت همچنان در حال تحول است. جزئیات بیشتری در انتظار دریافت هستند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18523" target="_blank">📅 19:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">— مقامات آمریکایی به خبرگزاری آسوشییتدپرس گفتند:
«ترامپ به مذاکره‌کنندگان آمریکایی زمان محدودی برای رسیدن به توافق با ایران داده است».</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18522" target="_blank">📅 19:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 5  جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18521" target="_blank">📅 19:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18520">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">باز شروع شد...</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18520" target="_blank">📅 18:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbe_7iA8H3K7A_VNHOS-FlQVIGImf0h01JVqjd9oaZda1dmN6WHBspNY7PmNHOFeZ0PsSyR3EMoXG6M-RDOXHXM3FiLB0NMRIZjsepS2OagiSBrfybPxa0FvSZz5LX5VjMI27xMeKZ4AF2OYmk_br-tx8K4HISuUZVaW6eWV5kPq-q-_XVlS8aQIyje8bLS6Ry-f3UeVbo-SgblnIkpjosXbxa3Xmqt7vMAH5PIboeG6Z69WqyeXb60_jlUR_Oq4GMPTBjaf79FOgC2FUPbsr7QTOBThsWvyXTdJhI_9XjeMXD3c88apRZQUWKBq5bf3rbst0ggDkxmgf8jpXCbIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار لیست ترور اهداف اسرائیلی از سوی شبکه افق!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18519" target="_blank">📅 18:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18518" target="_blank">📅 18:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDdQjz-J7otlLjHzvQJqAhGEPub5TGOwLc_QDPzUAVGjEX_2iFiHyulAiDSANhNZar0krDKn76Uccv-ttk2gcukJDnNsngsyzlmWLHtIAReoEtJbms8fcojjrDa-2OnCIgE664bvwBoVbabfZlgqHUu7hH79W1MrNvv-xQY8jKKAp69PNHsNDY1mee5Jt6WDRKCLQ4dlVdSIso_MU2xDP-pyuMr4hitdryQAns6YF8E4lXPngHcyR8_nMHcg5OJi_RtVX7hdjsm8a2PX9PcIbQTlqbefW3ch2GMA8AK_PavWZSLgCqyIoOaKuT4n-ghCr6_Eoh04U9wsM0PxSbZbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به ایران ۲۴ ساعت مهلت داده تا به صورت عمومی متعهد شود که حملات به کشتی‌ها را متوقف کند و تنگه هرمز را باز نگه دارد.  واشینگتن هشدار داد که عدم رعایت این درخواست منجر به "پیامدهای جدی" خواهد شد و افزود که اگر دیپلماسی شکست بخورد، برنامه‌های اضطراری از…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18517" target="_blank">📅 18:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18516">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۳ اسرائیل: برآوردهای اسرائیل نشان می‌دهد که ایالات متحده و ایران در حال بازگشت به مسیر دیپلماتیک هستند</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18516" target="_blank">📅 17:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18515">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رهبر ایران، آیت‌الله مجتبی خامنه‌ای:
به شهید بزرگوارمان عرض می‌کنم:
ما عهد می‌کنیم که انتقام خون پاک شما و خون تمامی شهیدان این دو جنگ را از جنایتکاران و خبیثانی که این اعمال را مرتکب شده‌اند، خواهیم گرفت.
این انتقام، خواست ملت ماست و قطعاً به انجام خواهد رسید.
این جنایتکاران، که نام و نشانشان برای همگان مشخص است، با آرزوی دروغین مرگ مسالمت‌آمیز در بستر خود، به گورستان خواهند رفت.
آنها باید بدانند که این موضوع، به حضور من یا هر مقام دیگری بستگی ندارد.
خواه ما اینجا باشیم یا نباشیم، این کار انجام خواهد شد و به زودی، افرادی از میان مردمان آزادی‌خواه در سراسر جهان، هر کدام سهمی از این مأموریت الهی را به انجام خواهند رساند.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18515" target="_blank">📅 14:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18514" target="_blank">📅 11:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18513" target="_blank">📅 11:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرماندار پاکدشت: صدای انفجارهای دقایقی پیش در شرق استان تهران مربوط به عملیات کنترل شده امحای مواد منفجره بوده است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18512" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18511" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18510" target="_blank">📅 09:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گفته می‌شود کارخانه فولکس‌واگن در اوسنابروک با خطر تعطیلی مواجه است و صدها شغل در خطر قرار دارند. دلیل این امر این است که صندوق ثروت ملی قطر یک قرارداد بین فولکس‌واگن و شرکت اسلحه‌سازی اسرائیلی رافائل را مسدود کرده است که برای تولید قطعات برای سیستم دفاع موشکی گنبد آهنی پیش‌بینی شده است.
صندوق ثروت حاکمیتی قطر سومین سهامدار بزرگ فولکس‌واگن است و انتظار می‌رود از حق وتوی خود بر سر معامله با رافائل استفاده کند.
بر اساس گزارش، قطر همچنین تلاش‌های گروه کشتیرانی آلمانی هاپاگ-لویرد برای تصاحب شرکت کشتیرانی اسرائیلی زیم را مسدود کرده است. صندوق ثروت حاکمیتی قطر حدود ۱۲.۳ درصد از سهام هاپاگ-لویرد و ۱۰.۴ درصد از سهام فولکس‌واگن را در اختیار دارد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18509" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">صداوسیما :
ایران برای ادامه مذاکرات آمادگی ندارد، زیرا ایالات متحده به توافقات حاصل شده با اسلام‌آباد پایبند نبوده است.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18508" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:  "۱۰۰۰ موشک قفل و آماده شلیک به سمت ایران نشانه‌گیری شده‌اند و هزاران موشک دیگر بلافاصله پس از آن‌ها خواهند آمد در صورتی که دولت ایران بر تهدید خود که در بسیاری از نقاط جهان اعلام کرده است، برای ترور یا تلاش برای ترور رئیس‌جمهور فعلی ایالات متحده آمریکا،…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18507" target="_blank">📅 08:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18506" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آکسیوس— «ما انتظار داریم ایرانی‌ها بگویند که هر کانالی در تنگه باز خواهد بود و عوارضی دریافت نمی‌شود»، یک مقام آمریکایی گفت.
یک مقام دوم آمریکایی گفت که اگر ایران امتناع کند، «پیامدهای شدید» وجود خواهد داشت. «اگر این موضع آن‌ها [فردا] نباشد، روز خوبی برای آن‌ها نخواهد بود»</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18505" target="_blank">📅 08:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شرکت اسرائیلی رافائل در حال مذاکره با شرکت‌های دفاعی هندی برای تولید مشترک موشک‌های رهگیر تامیر برای سامانه دفاع هوایی گنبد آهنین در هند است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18504" target="_blank">📅 01:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یه کم لوبیا زیاد خورده بودیم بادی خارج شد</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18503" target="_blank">📅 01:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مسئولان ارشد آمریکایی می‌گویند که ایران به آن‌ها گفته است حملات به کشتی‌ها از «بخشی خطاپذیر از سیستم خودشان» سرچشمه گرفته است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/18502" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمریکا به ایران ۲۴ ساعت مهلت داده تا به صورت عمومی متعهد شود که حملات به کشتی‌ها را متوقف کند و تنگه هرمز را باز نگه دارد.
واشینگتن هشدار داد که عدم رعایت این درخواست منجر به "پیامدهای جدی" خواهد شد و افزود که اگر دیپلماسی شکست بخورد، برنامه‌های اضطراری از قبل در حال اجرا هستند.
منبع: باراک رافید</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18501" target="_blank">📅 00:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیانیه مقاومت اسلامی عراق در رابطه با ضرب العجل دولت برای تسلیم سلاح مقاومت   سلاح ما که زینت‌بخش بازوان مردان ما در میدان‌هاست، هرگز ابزار چانه‌زنی نبوده، بلکه مرام و پیمانی بر گردن ما و امانتی از جانب امام منتظر، صاحب الزمان (عج) و نایب محبوبش است و با آن…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18500" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18499" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMqK-XGosvJHa8I9xqxO2-3twYBVS1Q3ALgTAcF2nn5TbRWQk3GDuzhZp7yEn0nh7DCIv3MbQwu0Hc0ijfV3A31NtOf-YCyzVMNwkXuwbBaRTKRpxJgKJr6NfTUFMhLLoBwPKr_IRtmh7VM9w8uUncaD2TcP2GBi48CTDKJYtf03-zDvTknkf87tlZxGV7glSv4s6-ZVDNch16VjvX-3gtrNimkpNmrXQRvIGn5NMBKbGeWjEIHLKxJQrm-0mNDt5BbHvzztSqnojXoVC3owIXR8DpzVvhij3Lbxj17VLj5d2lEP_pdsBV71RcjIsM9qnlcqvu4lcnh9DwwaSkkq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا:
امروز، پس از از سرگیری حملات ایران به کشتیرانی بین‌المللی در تنگه هرمز، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC) یک تسهیل‌کننده مالی ایرانی را که عملاً اختلاس‌های کلان را در رژیم ایران نهادینه کرده و ثروت‌های عمومی را به خارج از کشور منتقل کرده است، تحریم کرد.
این اداره همچنین امروز همچنین صرافی‌های کلیدی ایرانی را که سالانه میلیاردها دلار را از طرف بانک‌های تحریم‌شده ایرانی جابجا می‌کنند، هدف قرار داد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18498" target="_blank">📅 00:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18497" target="_blank">📅 00:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شورای رهبری یمن:  «پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.  ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18496" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شورای رهبری یمن:
«پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.
ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران می‌خواهیم که از یمن به عنوان میدان نبرد برای منازعات منطقه‌ای استفاده نکند.
دولت و نیروهای مسلح، اقدامات سیاسی و نظامی را برای جلوگیری از هرگونه تلاش برای نقض حاکمیت یمن، انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18495" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صدای انفجارهایی در کرج!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18494" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر دفاع روانی اسراییل:  امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.  اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.  ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18493" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1djrFM68ApJVdBzmp7PJdpCMPfoHp-IHjoAUaYD4Jzfy2hzlkONUYkJ3cmPIw30iDkf24s9vuX8jqfUfqtdfZ039SJHw0yx8r_2R_mykNtlshh9a2IPaKYTr_C_3Two5ESXjGVbbpnacH2rsl5dsFynyWuiUr2Tm-zfsjW85kE79cTJqL_m_mTO8VkE8n8xW--LhLr9n-q_vuP3N5oIsRUxdybq_ooZe5yY7e3xkbdaN8L6Q0t8ur2-c-JlgKQrE4VBNRakbfir6NzTIm6gjZTXIxJ3i0BkCSD1uXewPiri8C9HuHiwx8ctfa_KC0Pxg1ys-menSgj3tjYGaSOTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع روانی اسراییل:
امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.
اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.
ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی را دوباره به دست آورد و برای بار سوم به ایران حمله کند.
احساس می‌کنم خلبانان جوان در آینده نزدیک مشکلی در کسب ساعات پرواز نخواهند داشت.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18492" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار در پالایشگاه نفت پلدختر در استان لرستان</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18491" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک به درستی پیش بینی کرد که یک اصلاح نزولی در طلا و دیگر دارایی های ریسکی داریم که پایدار و شدید نیست.  اکنون هم سطح شاخص کاهش یافته و رشد بیشتر طلا را متصور هستیم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18490" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B21VACPvq-HlbhDFXt6nNsIr12DnarqO-5AB_19By91FzpYeqet6yvQ0vnCycoJMtoSe-Ye2bq05kfKmwiowcw-Hmx4kZrYcNe4_wa86mMB15-dq_VDziCdAdO_X2hSXJMB8ZhjdJFq5O7T9wBcdVzbSR3qf0iEXpS1M-Q-K0Ml1NLLqzefGiVlIIpvAWccYiNK64ncr7jvYcOtnnsbk-G3sPxDLowEq5ld3DHTfC5UUvGR1enP15oHUtZANSBQCQkIpc0r7DB8oInHODeaQwzHlrBH_UlcW79iI-ro6zxsfxWwu7dCaG_6NbR7ZEQpLjnA36UqAR-FkqGeM9whyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18489" target="_blank">📅 18:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iupPyAbk-9Wc4LLZOAKmc7OUzAeij39aouQ5PdtabCOmUoumwAwbP_N04DFMfP4i8yD3ZSbVNOofDGvMbpsaybpD4AF5Brc8CwmOab8W8wyj6y6GAAc6gW5rnJ3-RAQMu-jvS5EX3WgLhp38FHKKlBYj0GaP6N6xlxzrzt9gUgD1BNtEZPvEKZ1LT8ztBxmIttPyCo0c45b5yJlFXIxqEekXUmD59iXLm23Vfme3Ow_HHEWNom0oxv-UyhlEkjoQRWuyu5Key-16rfCf_jgdN24dcZNDKB801WM3Dk08kXqig7IIMC102Bxep4lHyjDEBgeO28kYkFYc1VRaa2PGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18488" target="_blank">📅 18:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsD1q-QAlncA-T_hbWvKrA0nkzA1vnqAAWikVDSYNdcWLFeaM93lzB76jtg6R9SZRq9LyWUwDR98qAnGRDrdt9QTvsO2w0MtOXqkEXrmEcX38-R9KZH6SqetE7SzMroHfkQW7NGY0l42rru-ikBRsH4ce2z19poHX5NYhtmXVl6EfMQjcK6epuU6gFkmKajUs8ZhcydQRGm9PRHxO-yQHZgwDcs386wnZDiQ1L6vtk81a6Awr2SNWCVkER6wk7jACchDC5nfPGJcaPC7apBFoaXfJDkeoKuDK8_wGamKnZypswl3Z2J0BwapPKZpocO2UCuJMwfla4TbYMDQ_sUxaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18487" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بعد از اینکه ترامپ گفت آتش‌بس با ایران به پایان رسیده است، گزارش شده که دو ناو هواپیمابر آمریکایی به طور غیرعادی در نزدیکی ایران و در محدوده برد موشک های ایران دیده شده‌اند.
این موضوع می‌تواند نشانه‌ای از آماده‌سازی برای تجدید فشار یا اعمال محاصره در تنگه هرمز باشد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18486" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ :  در صورت موفقیت ایران در ترور من، دستورالعمل‌هایی برای اقدام صادر کرده‌ام</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18485" target="_blank">📅 18:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وال‌استریت ژورنال:   بر اساس اطلاعاتی که اسراییل ارائه کرده، ایران طرح جدیدی برای ترور ترامپ طراحی کرده است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18484" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRGfcBnru1wAPZsRdOtMxjmReg8IrJVCCR7JHxSsNXuE4a9An_pA8S1uSntJqSEoMMfmJIMWJhz9_ZD7doBUjpB4uBxej8G5TMLmHiz-uNaKcwUZBtAWRcJHM0eZ0kdcR0dZNF46u0o0_6EF4ge_VWb7nd2TF6DcT078eEe42eQA6RPru42YYnMUqIspbWO7M6X87lVYHq8MeXWwekmzhD-3rxZemSksrrpcHkDJ9VkxQsrkTH5myM68VdUwfdiPp9CXmY-tPfVjDXiRQfLTcwsJBN2jyJqrSsA2_33XDSpBu-TyRmWSSvReOfP2O7d49HMxyCnS9kQhP-Cvqak_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18482" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک هیئت قطری با هدف نجات مذاکرات بین ایالات متحده و ایران به تهران آمده است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18481" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فقط میخواست ما را ضایع کند که گفتیم فقط شبها برنامه بود در آن فیلم</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18480" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18479" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صدای انفجار در کنارک !</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18478" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خوب خاطرم هست در دوره دبیرستان یکی از بچه ها یک فیلم ویدیویی آورد که رویش نوشته بود «جدول تناوبی عناصر» و دقیقا داستانش مثل همین مذاکرات ما با آمریکا بود
روزها صحبت می‌کردند و شبها با هم حکم بازی می کردند. حکم تفخیذ.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18477" target="_blank">📅 18:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18476" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsRuTVz99BYcIK3e_yk8B-UrsrQ99tYmqxlCdxgcni7ucE3pYvFhgah-eiT42Ue6etQJC1MQlqY5Q9u8Y3kMmbwVOwTslmsa4Kh1_XZ94yC3-g4UuqScKXSM4vRm09e7guZC5jSlIPUXnTPW-9oUylk0pTUEzk7hYrJoFWPHs7JcrBNfI68OXc-61StnUA6Ec-4XBd2ByvLyx6IHpcyB-lx7cB27ExEku30ljVNaUQWBhs1JyU1eQfFwuq4J59o_49mYakHeK5PI4O0CVVMEim0hTkCuJrr9Dw0nebYtek828lKPsNT-NL9S3Ovw5xv9cJrfUp8H1YNxayL7Qiq39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می گوید جمهوری اسلامی از آنها درخواست ادامه مذاکرات کرده اما آتش بس تمام شده است!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18475" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ادعای بابک زنجانی در خصوص خرابکاری در راه آهن آق قلا</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18474" target="_blank">📅 14:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyYO1yUAJLpmUlXSvhE0koVi_PcsvrnnV8Ry7ba-347ZWCOl2e1zQ72FMWLGaYuWY8jBZp8wXWg174yzDT3yQxDEb4pUHMQW736pbV9z0Wpiejs7DUuQvBXMWcQLRBAZA0-xYhFpXJnzjTkQm8UlxWu0ee9Mxvfi3zX5-4R4Ze1guxf3XWzm5mGArguI-b8FvgRoliS_CFCHE7F586oD0HWcWR7dXKyAkCjbP2cgqAlJqDncEL_3qVQNLUk3ldDAazGgGuUE4sKHohlx_jqAXOCVxwtS8BaaEgF3vp9IpHRadcYJrosccBz9m13sHLNe6MSZzhaj9_4C35UA2HrVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای بابک زنجانی در خصوص خرابکاری در راه آهن آق قلا</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18473" target="_blank">📅 14:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 5  جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18472" target="_blank">📅 14:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18471" target="_blank">📅 13:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAl84O4Lbhnt0ROHqGgk2KYT24HyssU0vMwKYYqFhgfp72KvFaJX0FRtJWR0pXp7DeFDrRX7G0TIt4mkK2DIuzLCjBOkVim2-7WGyCBlBq_1XD4YW2-vH_BVRVb6rHv3mShSgRJnf0-Wflmx58c4Yrmv40RuyQ8SFo7x2xuo6yhdkN5eO-NzqJd0Q9FY8qhl_7sPRXC7YExSDrr1AB9G-3pmTp_lXGGKJOD3Qo5cH-lG5InRqUdvf42jMfsjT48OEe6NcLcqRv5bEcpJY24lucisaXIh0lQNyavM4TBLSJiYjNwZD4mL7zCVElp-bfZIHB0V12O46hRqjrJ52-YmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18470" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الشرق الاوسط: حماس جلسات رهبری خود را از قطر به ترکیه منتقل می‌کند.
در ماه‌های اخیر، این گروه بخش قابل توجهی از فعالیت‌های سیاسی خود را به ترکیه منتقل کرده است، در حالی که قطر سال‌ها به عنوان مرکز اصلی فعالیت‌های سیاسی آن عمل می‌کرد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18469" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMRqpbIjeMPbgRy9HvAGewMqdwjvaniAkeEzHtff7dGAI5ZIZwSRwrZr7TacMpSfsqNRJ_X43QZOfCfwr_3f-JcEh5hFJqHWmBO6hlkCWCxlULSdl0vkEXdPj2uXMDH4MbingrIUaOP-aISV6LEba4_EWN8R-bld-yWUESvuRl5f4GQevB5llU5r40M3zzFkrV05HeohXOgTKWCL9HGYyHHj37Y5_1pDo7uBqM0MsMDi2bOk_Zw0pG_eUk5NpAOG4JdHvrciP37KbPInzWppRegJhzcm9r_6tFxvQ611aeQbEnqTr5Sf4FOJgsPcJ9DdlbgkHiKxaMVXOl6Hkya1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18468" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 5
جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18467" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک مقام آمریکایی به شبکه CNN گفت که ایالات متحده و ایران در حال انجام مذاکرات غیررسمی برای کاهش تنش‌ها هستند، این در حالی است که پس از یک سری حملات متقابل، این مذاکرات در جریان است.
ایالات متحده در حال حمله و سپس توقف است، به این امید که از تشدید بیشتر اوضاع جلوگیری کند و به دیپلماسی فرصت عمل دهد. در عین حال، واشنگتن برای انجام حملات بیشتر امشب، در صورت لزوم، آماده‌سازی‌ها را انجام می‌دهد.
بر اساس گزارش Axios، دونالد ترامپ "به شدت به دنبال راهی برای خروج از جنگی است که آمریکایی‌ها از آن حمایت نمی‌کنند."
پاکستان و قطر نیز در تلاش هستند تا هر دو طرف را به میز مذاکره بازگردانند. میانجی‌ها معتقدند که حملات اخیر ایران در تنگه هرمز، توسط جناح‌هایی در داخل رهبری ایران صورت گرفته است که با توافق‌نامه همکاری مخالفت دارند و در تلاش برای تضعیف آن هستند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18466" target="_blank">📅 11:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18465">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkCJR7spRVyL5yreq5VI_3_WulcZZbrJegwxlcQUPLsYkhDXuM3-p04PTb39dLyq7JtAUdG4faiHXC6dF1vCF4bEkFqtsd-VzcNlla3NvGyHJjdDEyp79eIO2cEK0l4F_dfHseKdaBenJIWNsdT_hlut45t5yBO35SUfkU0p1R5_Sf_sQfBG1a0LDhKeTUbzTurEaiKPQHZpg5x7Ozh2bvQCDO8IYTT751dVlxuNKun55L6nminPuvaS3YfimrG_9OJs3XfdEukmCPMPjcqgC6jHWdCXSmK1b-fEbGoSAa9oLsX0qUvYSZCoCtGV3WZ1lfGgWz8H6HYsgTFVXMvbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18465" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE8Hl7GE_OgO3G6kYp5jHcvbwi5I1tp4F_4ZPem9AsVgiafBBSzJLCxP8jIaXo2HkVNPs8Na4m7la4TBVA0n5GvzkK0xL9W4_7d6pEnsh8LBHvmz_JDWxvSnvWyr-fmZQnZyiqTkdBYgJh6xWsmwj-RnG-1Zmm5sllqAz7ixwCcsCR2BS7Ys0vAOgEvbJ7MedWPVXvGnXNhus89d4fYrqDG9eCzD_hfh3StTdYbn1aGqLrDg9kKxVlmAg7uMXaySEHeOygkEXBibzmVwx4fO3klI1PuG5RRbMI7hO09EaOxaIncQ3g2UJSJXY_obsSzBCJiG6G38SHX5oroKYP6ThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگ-۲۹ همراه؛ جنگنده‌ای واقعی اما با محدودیت‌های مهم
انتشار تصاویر اسکورت هواپیمای حامل پیکر رهبر پیشین ایران توسط یک فروند میگ-۲۹، موجی از بحث‌ها را در فضای مجازی به راه انداخته است. برخی کاربران مدعی شده‌اند که این هواپیما در واقع یک
میگ-۲۹UB
، یعنی نسخه آموزشی دو سرنشینه، بوده و به همین دلیل از رادار بی‌بهره است. بررسی مشخصات فنی نشان می‌دهد که این ادعا تا حد زیادی صحیح است، اما نتیجه‌گیری برخی مبنی بر اینکه این هواپیما «جنگنده واقعی نیست» نادرست و اغراق‌آمیز است.
نسخه MiG-29UB برای آموزش خلبانان طراحی شده و به دلیل نصب کابین دوم، رادار اصلی N019 از دماغه آن حذف شده است. در نتیجه، این هواپیما توانایی کشف و درگیری فراتر از میدان دید (BVR) را مانند نسخه‌های تک‌سرنشینه ندارد و نمی‌تواند از موشک‌های هدایت راداری به همان شکل بهره ببرد. این موضوع، توان رزمی آن را در نبردهای هوایی مدرن کاهش می‌دهد.
با این حال، حذف رادار به معنای از دست رفتن کامل قابلیت رزمی نیست. میگ-۲۹UB همچنان از دو موتور قدرتمند RD-33، عملکرد پروازی مشابه نسخه استاندارد، توپ داخلی و امکان حمل برخی تسلیحات، به‌ویژه موشک‌های کوتاه‌برد حرارتی مانند R-73، برخوردار است. بنابراین این هواپیما همچنان قادر به انجام مأموریت‌های رهگیری دیداری، گشت هوایی، آموزش رزمی و اسکورت تشریفاتی است.
در مأموریتی مانند همراهی هواپیمای حامل پیکر یک مقام بلندپایه، هدف اصلی معمولاً نمایش اقتدار، احترام نظامی و ایجاد جلوه‌ای نمادین است، نه مقابله با یک تهدید هوایی پیچیده. از این رو، استفاده از یک فروند MiG-29UB برای چنین مأموریتی امری غیرعادی محسوب نمی‌شود.
در مجموع، اگرچه میگ-۲۹UB فاقد رادار است و از نظر توان رزمی با نسخه‌های عملیاتی میگ-۲۹ برابری نمی‌کند، اما همچنان یک هواپیمای جنگنده با قابلیت‌های قابل توجه است و نمی‌توان آن را صرفاً یک «هواپیمای آموزشی» فاقد ارزش رزمی دانست.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18464" target="_blank">📅 11:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوزاندن ترامپ لگویی خندان دیشب در مشهد!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18463" target="_blank">📅 11:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKITBbyBaJRJEs4vUL9K6f3M5EcHX3HuQKMHIsCtBOA_3BR8xveciXiHG_yQviBkZJNL2PumYlqpy-35jTjp7S8LhKVUCtx18MZxhGbcDrMiOhus7uycgq7RdfmUaow1Civc65JOsnhLRh-O9988wAA6c4qsZGHd1-Hws4l-POlX2sV95VSZ18-u4-PDdgp5_L6bJiCcwZgeW7OpSBuSxQkxNWdBg-QpGlTmaNAMrzjx7lodnXORYZCDiDD0-Udy476lydeKPglIW5ozkjCHdHhImHWpskK3YHSjsM8NbFo-adQBI81fJfzXsocHXYjsFKFWj7f_rH3r_igt-uienQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbXodqFrrEGZOdIma0funbCbNFRrUO4ts3_6-pB56UpqI6GBThEoVLgjqpN4OVwALAyJos8dMEKI5vpxt0l4ef-gCEFL8BaIazRUXQ6nGNoS7dNBTIpPYZ2ld6W09noae5Ylt8PgRreaCjkzjnoNFPFoBfEqc9OyMIz59tv2t5kqd6dPgOm9qxB_psGRQJrL1PtANrulApaW3lMCSnVAru3fzBynsHxuEVvi4EUC_yMBHfCgFRWHAXPAOcsy1H3JjpqQ-4daiMN5GYZ3dbdck0rWXTdS4bvZCmfynA1ntT1Yhk7tdKXH5BXdFzmHpynpmuvJGOH4dYkqCYgE-B0kiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه فکر می کنم به نظرم چهره آقای نجاتی در عکس سه نفره هم هست!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18461" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18460" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
