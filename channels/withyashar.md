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
<img src="https://cdn4.telesco.pe/file/XEPx3HeecqAQ_V7GpJs6yHCUO5awMV3VnjdAmJPAP8r-7xFT1PY8uZpXj-PRXM6luH5xsWcJjbx5VbnVyorpEuxOfIvVhqO0kMn-36PLab4aD51J10PVdUECAvneSpsKNCZM7FeRwx3rW7Btg0R5lIZCqXR2vmPnwS0Vo0zjI6HG6Nq0Gn3QkSFCOQv6d6fxXoXw_hN-tgqM3Col7eldz8Bsr0hkT2WOU8jdCqh8I2R3axJvirZRsRLvVnslLAZ9_sZSwLTX2sfZSdG4WzPiwxdsJnCP5JdBGOg8rFpo-as7YIepG66xiEp6S0EPpOhiIRpxqyb7QVZMr_Q8KGjYvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 389K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 07:57:58</div>
<hr>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: ما دوربینی در نیروی فضایی داریم که می‌تواند نشان‌های اسم ایرانیان روی سینه‌شان، احتمالاً محمد، را از فضا بخوانند.
@WarRoom</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/18138" target="_blank">📅 02:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ
: آنها هنوز مقداری قدرت دارند، اما خیلی زیاد نیست. و میزان تضعیف سلاح‌هایشان فوق‌العاده بوده است. هیچ‌کس فکر نمی‌کرد که این کار را بتوان اینقدر سریع انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/18137" target="_blank">📅 02:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f817c2d295.mp4?token=t2RYQAjy9qLwVtLBPofF22DT4hgaf4y1NQhKTHbcyKAi-CS4luSRLx10dTbizyax7r820ODYXXlryQPNu5383fTzEgunvG55Oz7lJtZVkZjb8TttDz5oXgWeXnMoY9LHrDHG6yWQN7AvNVilcYW6i6p0UFVyLj-zgioSweliiMVwx1eS0bwGMZwmpyJDWVf6-nyuxg0RHNOOqkYB1F7XlE6_QAni6U-T1WMN2QpIDQ9yMFyWNoDqn1f87n-e-LmjW2UiGs2zviyjYIZUa5Ox_6eVhyRasN-8YaLDOZmxA_e1z5E1kLXfZH6sMGlm5P-c7troX35N5ohh1mon8w4KvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f817c2d295.mp4?token=t2RYQAjy9qLwVtLBPofF22DT4hgaf4y1NQhKTHbcyKAi-CS4luSRLx10dTbizyax7r820ODYXXlryQPNu5383fTzEgunvG55Oz7lJtZVkZjb8TttDz5oXgWeXnMoY9LHrDHG6yWQN7AvNVilcYW6i6p0UFVyLj-zgioSweliiMVwx1eS0bwGMZwmpyJDWVf6-nyuxg0RHNOOqkYB1F7XlE6_QAni6U-T1WMN2QpIDQ9yMFyWNoDqn1f87n-e-LmjW2UiGs2zviyjYIZUa5Ox_6eVhyRasN-8YaLDOZmxA_e1z5E1kLXfZH6sMGlm5P-c7troX35N5ohh1mon8w4KvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/18136" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پرتاب موشک از‌ حومه تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/18135" target="_blank">📅 02:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c274513f5f.mp4?token=ObZwI-6Wvv3nO5naZvMVyfIf8OEgyJilY04HDohZ1xszKAcahX0anF66puKZRKELW9kjYHIS7KuDJODaRfFo8snwkjWT2K3Cyh-6F0eWLqk3YlKSNeFleKVApIVkpxp7K_m30zlDXZRNoXD70yxXlDQY7CSr9lbwpXnOAsXAMDoBYD70uQc6ZyTQYpv2Jk5du82QjmDR-46tt8IlBWRHpxZ0FLN1mPO2w1mAOAUizy24DSpzn2heirtvwib_-RDVU6bJsRNouhUD1Bp7crVXQNIB78I2mlOrVVF6SVYTv95_1wlrgb5twkNragK5FmcOg6QNreh1vZOSJVR8-zAo-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c274513f5f.mp4?token=ObZwI-6Wvv3nO5naZvMVyfIf8OEgyJilY04HDohZ1xszKAcahX0anF66puKZRKELW9kjYHIS7KuDJODaRfFo8snwkjWT2K3Cyh-6F0eWLqk3YlKSNeFleKVApIVkpxp7K_m30zlDXZRNoXD70yxXlDQY7CSr9lbwpXnOAsXAMDoBYD70uQc6ZyTQYpv2Jk5du82QjmDR-46tt8IlBWRHpxZ0FLN1mPO2w1mAOAUizy24DSpzn2heirtvwib_-RDVU6bJsRNouhUD1Bp7crVXQNIB78I2mlOrVVF6SVYTv95_1wlrgb5twkNragK5FmcOg6QNreh1vZOSJVR8-zAo-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران
:
‌اگر به تنگه هرمز نگاه کنید، پیدا کردن جایی که آنها چیزی دارند برای ما سخت است. باید جلویش را بگیریم.
ما باید آن را باز نگه داریم. من قصد داشتم هزینه ای دریافت کنم، اما در عوض آنها ترجیح می دهند پول زیادی را در ایالات متحده خرج کنند، که صراحتاً بهتر است، زیرا من ایده هزینه را دوست ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/18134" target="_blank">📅 02:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ
: مذاکره؟ نمیدونم شاید بخوام شایدم نه؛ ولی اینبار رحمی نمیکنم همه چیزشون رو بمباران میکنم
نمایندگان من همین یه ساعت پیش با ایرانی ها گفت گو داشتن
بهتره تسلیم بشن، چون چیزی براشون باقی نمیمونه
آنها دیوانه هستند ولی ما دیوانه‌تر و قویتر هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/18133" target="_blank">📅 02:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم اکنون حمله موشکی به کویت
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/18132" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مجری فاکس: همچنان قصد دارید جزیره خارک رو تصرف کنید؟
ترامپ: نمیتونم اینو به شما بگم، چون اگر بگم، کار احمقانه‌ای خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/18131" target="_blank">📅 01:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار در‌ بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/18130" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مجری فاکس
:
آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@WarRoom</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/18129" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Bitcoin 65000$
Tether 184.000 T
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/18128" target="_blank">📅 01:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به گفته فردی آگاه حملات آمریکایی امشب به پایگاه‌های ایرانی در منطقه شهر اهواز متمرکز شده است که این منطقه عمیق‌تر در داخل ایران قرار دارد، برخلاف سواحل تنگه هرمز که بیشتر اهداف مورد حمله آمریکا در روزهای اخیر در آنجا قرار داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/18127" target="_blank">📅 01:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مجری فاکس: آیا جنگ با ایران از سر گرفته شده است؟
ترامپ: خب، فکر می‌کنم شما می‌توانید آن را به هر شکلی که می‌خواهید تعریف کنید، اما قطعاً ما آن‌ها را به شدت شکست می‌دهیم. باید آن‌ها را شکست داد.
مجری فاکس: آیا می‌توان به اهداف خود فقط از طریق یک عملیات هوایی دست یافت، یا اینکه این امر مستلزم یک عملیات زمینی است؟
ترامپ: من فکر می‌کنم که اهداف در حال حاضر محقق شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/18126" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ به فاکس نیوز: اگر ایرانی‌ها برای مذاکره جدی به
وین
نروند، هفته آینده به نیروگاه‌ها و پل‌ها حمله خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/18125" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18124">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ به فاکس نیوز: امشب، فردا و پس فردا، ایران را با قدرت مورد هدف قرار خواهیم داد و در مرحله نهایی، تاسیسات انرژی و پل‌ها را هدف قرار خواهیم داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/18124" target="_blank">📅 01:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18123">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ : حملات به ایران تا زمانی که من بگم ادامه داره.
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/18123" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18122">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیت هگثت: اگر نیاز باشد حملات به تهران نیز می‌رسد
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/18122" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18121">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش از حمله موشکی سپاه به تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/18121" target="_blank">📅 01:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ارتش جمهوری اسلامی :
در مرحله هفتم عملیات «صاعقه» با پهپادهای انهدامی پایگاه الازرق اردن را هدف قرار داده و محل استقرار جنگنده‌های F/A-18، ساختمان اسکان و یک سوله تجهیزات ارتش آمریکا را مورد هدف قرار دادیم.
در این بیانیه همچنین آمده است که از زمان آغاز درگیری‌های اخیر، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه‌ها و مراکز نظامی آمریکا در منطقه انجام شده و این عملیات تا «رسیدن به پیروزی نهایی» ادامه خواهد داشت
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18118" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کرج ؟؟!؟؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/18117" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18116" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18115">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کرج ؟؟!؟؟؟؟؟؟؟؟</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18115" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18114">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار در جزیره هنگام
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18114" target="_blank">📅 00:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91267f7421.mp4?token=i5eaGoSJEk5nI9thQ8A3ilVor-7wPYRAVvrdkD6stb-keosOzqDx8HoaDY1VLbdzjzEFc1Ox08JuKIPDjOekmuq5zBMbCCaCwHM5ve6ZZsI0WYXBgbkZaznHewEUsh_meNE32D-LJxlxAtWeoFSKwH2oFAqTxGrek5KTqxkCeRfYMv6ruGtmaRwr_NaRcBOvtpAxFZ8G2RtRPF9tqcG5WyaAwOcf8Qe5xtjkPL9VXeD79u213CYk-86KXC1mZxyv6JiUH8E56DYSTlTQxylx9lyVyuio5KuZxcjxffmtgqmfQfzCbLAwjL1h4tRYoYXzmF2Wn5JOy8c9P-S4DPTG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91267f7421.mp4?token=i5eaGoSJEk5nI9thQ8A3ilVor-7wPYRAVvrdkD6stb-keosOzqDx8HoaDY1VLbdzjzEFc1Ox08JuKIPDjOekmuq5zBMbCCaCwHM5ve6ZZsI0WYXBgbkZaznHewEUsh_meNE32D-LJxlxAtWeoFSKwH2oFAqTxGrek5KTqxkCeRfYMv6ruGtmaRwr_NaRcBOvtpAxFZ8G2RtRPF9tqcG5WyaAwOcf8Qe5xtjkPL9VXeD79u213CYk-86KXC1mZxyv6JiUH8E56DYSTlTQxylx9lyVyuio5KuZxcjxffmtgqmfQfzCbLAwjL1h4tRYoYXzmF2Wn5JOy8c9P-S4DPTG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار پیاپی ،دریابانی سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18113" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مهر:بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18112" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امشب ری اکشن ام پایینه جریان چیه
🤒</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18111" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مهر : جزیره قشم مورد اصابت پرتابه دشمن قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18110" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صداوسیما: دقایقی قبل، صدای چند انفجار در شهرستان بمپور در جنوب سیستان و بلوچستان شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18109" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اسپانیا هیولای جام جهانی را کشت صعود به فینال جام جهانی پس از 16 سال
فرانسه
0️⃣
-
2️⃣
اسپانیا
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18108" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرماندار سیریک، مهلت ۱۲ روزه برای تخلیه کامل لنج‌های تجاری را ابلاغ کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18107" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18106">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شیراز صدای زیاد جنگنده رو مخ همه رفته و ترس ایجاد کرده
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18106" target="_blank">📅 00:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار :امشب آمریکایی ها فک کنم قهوشون تموم شده بود پادگان ، بی حالن…
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18105" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار قشممممم</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18104" target="_blank">📅 00:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دو انفجارررر بندعباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18103" target="_blank">📅 00:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3QK4jqkYfIRqDEQc4pcXkzT6mJO0rfbf5y8Mbv-fbkSUH7kUULKI27NDKuPp-Zgpp9uRfnu62ifySld91_wPlD3ayefFEeLqHyRtzzwZEJVpayJLlLV5n4NTyy49YCGBd552Xc12S_oxQTcgBujMk2-fMoftC3XODXqQVzAuVZu9odpwuM9hgoxwR_fdknwOhhQwzMeu3uwPzg7UDJu00E9nR2Eq4xekCoK96iXNrMehO9KihjzWJbSjNPMuBcyDLAaIBMSrM8c21bxWqwtuctHKputfSeTTQaowBEaGurN4yWx2uTY4EhBViULOoQcEljyX5ZPSzZDZW6HoFZIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه داری:
رژیم ایران با فریب زنده می ماند و شبکه شمخانی یکی از سودآورترین موتورهای آن است.
وزارت خزانه داری زیرساخت های مالی را که به رژیم اجازه می دهد تهدیدات خود را به امنیت ملی ایالات متحده و حمل و نقل جهانی ادامه دهد ، تعطیل می کند.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18102" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حملات امشب در شب سوم تا کنون به این شهرها انجام شده است
💥
بهبهان
💥
بوشهر
💥
سیریک
💥
بندرعباس
💥
اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18101" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمد مرندی: ترامپ برای هفته‌ها مخفیانه در حال برنامه‌ریزی حملات هوایی گسترده و تهاجم زمینی با حمایت دولت‌های عربی بود
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18100" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUBoqamSmz6v3XXco5-53oKQU7OSkN-70ud8_26oP-V7cSKb-wWAnYjN1H-bREHFKrPpyrgYuUiOsAOmPejc-LuCnuOtgPnGd-sgz7-9zbzAx_kPSpXuf9OCrq-Wt3le3z2E_KWmeJfapfxuIHslrw17r2n9bVc3zPtHTfRAweMuKv1LS6HvVeV6yZPdIQdhHB8WFxjtolFYaq0OM3Fbxc0qivLzgmsItENvy2H23MUoDgGqHE18wRDsIDtMbhDMRvmSFGHEewT4n4ovaehVHTVd2m-TPJTSvT0HTi7l2O0MQ0sOso7ywFcx055MlNFj7IZF2DdIcAl2qqfdSvKniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق اعلام سنتکام، محاصره از همین لحظه باید شروع شده باشد.
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18099" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18098" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در ساعت ۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET) امروز (۲۲:۳۰ به وقت تهران)، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) دور تازه‌ای از حملات علیه ایران را آغاز کردند تا به تضعیف بیشتر توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز مورد استفاده…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18097" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یاشار بهبهان بازم صدای انفجار اومد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18096" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اهواز همینجور میزنه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18095" target="_blank">📅 23:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بندر عباس جدیددددد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18094" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18093">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سه انفجار سریع و رعد آسا به نوع پله ای سمت صنایع بسیار دهشتناک
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18093" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18092">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آی‌۲۴نیوز: مقامات اسرائیلی معتقدند که ایالات متحده در حال افزایش آمادگی‌ها برای یک درگیری تمام‌عیار احتمالی با ایران است، با منابعی که با واشنگتن در تماس هستند و برنامه‌ریزی گسترده‌ای برای بازگشت به درگیری‌های با شدت بالا را توصیف می‌کنند که ممکن است در عرض چند هفته رخ دهد.
یک منبع اسرائیلی گفت: «یک جنگ وجود خواهد داشت. تنها سوال این است که چه زمانی.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18092" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اهواز رگباری میزنهههههه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18091" target="_blank">📅 23:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18090">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پدافند بوشهر درگیر شد
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18090" target="_blank">📅 23:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDd0G1fXJ5t-8Jmmzogd2hdseSaHyu3d_-U41Qu6XEmKx8tdd5rDcp65MWAE84tlTqvFDKSB6uOyMUfGgOQGDcfQO9tTlNYHq4vRC4-_XUQl2BsFOf0NU_FhnhlKhZshgUH7TmXuX5_h7G9T4cfahryVgtozk3yhJiuEAp52rzeEVGOBI6dAjQw6H8pwhf8EQTydndRhupw4iFgNfBtgCdKfuGOmZsLR46E69lDztPVh3umCPTsaHyqgrb2_NPV0hFMEhQp1Wd4aPaCkIi8XMEW7EpxvYBHRhh3ejcGz9snhyfko2ZcOzFU2p56GIiS6Y_oOc_WGbGlFxoyc4e8BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین عکس ارسالی شب سوم حمله : سمت شهرک پیامبراعظم بندرعباس
از لحظه ای که علام کردی تا الان
۱۰ تا انفجارو رد کرده
لعنتی معلوم نیست چیه پشت اون تپه
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18089" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سیریک رگباری‌ میزنه با صدا فوتبال میکس شده
🥲
قوی باشید</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18088" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فیلم و عکس هم بدیدددد</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18087" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجاررر سیریک
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18086" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۳-۵ انفجار جدید بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18085" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اهواز چند انفجار جدید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18084" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSsNV3NJc_pjeUxideiN1h7SnsyYVKCXPaZfF-gRBvowYO7F68fiHqpi_CZev8jK1X7qhxpHtGZCx1WxRKydNY0WPWGBrF-167JkuTnb3L9rhg3icXjswO5Q85qwIpWN9pmOS7mMVdeMUgUBBHy22esjot2AXHcSNj4sJ_HWj4dkH4ceCfaJr64ru2LofQzdN4RxVCXBywdUDX5sLvbxO63XYSMCDY62kEkkpT8xJqp0y83N1WhQw8rSweY3KW4X9pPVYHhQb-DMXIICeHRL_JjlPoB1IMdM4Ix0Gyp3LgLKl8t3t9cXO0_GEDJ4DxvHXJsjb8CT3F-4LESSkNuAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ساعت
۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۲:۳۰ به وقت تهران)
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) دور تازه‌ای از حملات علیه ایران را آغاز کردند تا به تضعیف بیشتر توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز مورد استفاده قرار می‌گیرد، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری
محاصره دریایی
بنادر و مناطق ساحلی ایران آماده می‌کنند.
قرار است این محاصره دریایی از ساعت
۴:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
(۲۳:۳۰ به وقت تهران)
به اجرا گذاشته شود
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18083" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام:
دور جدیدی از حملات هوایی علیه ایران را آغاز کرده‌ایم.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18082" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارتش کویت: یک شناور متعلق به نیروی دریایی کویت امشب مورد هدف ایران قرار گرفت که در نتیجه، چهار نفر از نیروهای مسلح مجروح شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18081" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شمارش معکوس و لحظه‌شماری رسانه‌ها برای آغاز محاصره دریایی امریکا علیه جمهوری اسلامی ایران:
55 دقیقه تا از سرگیری محاصره دریایی آمریکا بر تنگه هرمز
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18080" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۴ انفجار بندرررر ر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18079" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لشکر 192 اهوازو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18078" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18077" target="_blank">📅 22:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۵ انفجار اهواز
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18076" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18075" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجار در کیانشهر اهواز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18074" target="_blank">📅 22:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وای نت : فرودگاه‌ بن‌گوریون به حدی از سوخت‌رسان پر شده که ممکن است باعث لغو یا اختلال هزاران بلیت هواپیمای غیرنظامی شود! @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18073" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۲ انفجار دمشق
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18072" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش های بسیار از‌ درگیری پدافند شهر اسلام آباد غرب در استان کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18070" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه های رژیم : دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18069" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFP3HwDOZWWNUTUq0NkJBEfOdaLGeDjxKnYhjh4KnTcrOKmhdjVX03dthtgL7MlI2jhuuB0NjmBy9gnPx_sXB5NSGeu4A756O_rdPZJpBNU9n_uQhyl-cYLeTuI4PoHJ1DmECNfyXZdYwEO95OHw9ax8D9xG_wVOo3QPsn3XW_4IVuf4ACOlV8URSBF0R-cmzLo_7XaWe668s7fy6NCHVFaA2nUeL3plnP89diktGzH5wyEpZBMCjsJ7ejFnzH8oO7krgkG61Q0pCSV00YseiFxIUoNpp8lYpYsmhRmYI651roek77L82_Vyot7MHg7k-3nYiXM23QkYbQfhYE-JMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار در‌
تاریخ
!!!
یه کبوتر جای درستی میرینه
@WarRoom
🚨
🚨
🚨
🚨
😂</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18068" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آموزش‌وپرورش : دانش آموزا به هیچ وجه نگران نباشند ،حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن ، با خیال آسوده امتحانتونو بدید.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18067" target="_blank">📅 21:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کابینه امنیتی-سیاسی فردا ساعت ۲۰:۰۰ تشکیل جلسه خواهد داد. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18066" target="_blank">📅 21:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی‌ان‌ان : حداقل ۲۲ کشتی تجاری در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18065" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437c5a5907.mp4?token=KYIzVZWVyG2eDXIJKvuLZMw5oC6tcx8JbSclJAhLEsIjHyAkLdi0V8BX9rsXS1Ymy_H_rcaOrGEAvEC0eEAIDgSWMEwOYcIXRssRuGevs7OzTFh33wWTC8yl7Hgl9mLnhGD0Km6WHQfXq4yOMeaBwQYt9iA-gp7Hpy_4SmQ5K7hyXSFqAckUOMX3ihi_l07ZjNRz7TpbFI-ezlGIZjTVUjPg27PSwqhHqJ440gyVhVQJCY2wQ7L1bkwos6vA-4BopnVEpMxAnngdnFnc2B-sbtSV43pF0d14OX9CASaION2L2F-cCMgAoumhuBNPC5zOBfMPFs9SCYs19lkCXhtaXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437c5a5907.mp4?token=KYIzVZWVyG2eDXIJKvuLZMw5oC6tcx8JbSclJAhLEsIjHyAkLdi0V8BX9rsXS1Ymy_H_rcaOrGEAvEC0eEAIDgSWMEwOYcIXRssRuGevs7OzTFh33wWTC8yl7Hgl9mLnhGD0Km6WHQfXq4yOMeaBwQYt9iA-gp7Hpy_4SmQ5K7hyXSFqAckUOMX3ihi_l07ZjNRz7TpbFI-ezlGIZjTVUjPg27PSwqhHqJ440gyVhVQJCY2wQ7L1bkwos6vA-4BopnVEpMxAnngdnFnc2B-sbtSV43pF0d14OX9CASaION2L2F-cCMgAoumhuBNPC5zOBfMPFs9SCYs19lkCXhtaXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لانچر مشهد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18064" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فوری | شبکه ABC به نقل از یک مسئول آمریکایی: نیروهای آمریکایی در حال حاضر هم حملات هوایی را در ايران انجام می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18063" target="_blank">📅 21:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فوری | شبکه خبری ABC به نقل از یک مسئول آمریکایی: حملات آمریکا به ايران همچنان از چند ساعت پیش ادامه دارد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
یاشار : بابا من میگم میزنند! بعضی نمیفهمند !</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18062" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد.
@WarRoom
🥲</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18061" target="_blank">📅 21:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">موج جدید حملات موشکی ، از لارک موشک بلند شد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18060" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پایگاه هوایی شیخ عیسی و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین، هدف حملات موشکی و پهپادی قرار گرفته است.
@WarRoom
یاشار : هدف با اصابت فرق ‌داره</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18059" target="_blank">📅 21:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملات موشکی و پهپادی خصمانه جمهوری اسلامی علیه بحرین و اردن از سر گرفته شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18058" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxFUMo6Ed7E4LOJuRN50Ll6_O3NHAK7xBXOeowQZpZCPmqUk7EfRlSFasg-UTHgzbEWAJfYS1MhcmC6ArXxri3csy4iRNm5Ibx83iSAL5xysHmRD2Xpp0t-DYFFyu8_Q6imvUwNYLE-ViFFPasEYQyNkO69V-8lkh4p-uza6nX9ZXfPPiLWD2rGlmPUqyTgzE9D6ggCkniP9qESb8fe-t8ExeDPYoHuTCL5pRuN2yP0YXoHSh8jEjMDnbsFHTiivD4w2elPdeWqbeWqRActBbBLBfoGxQTjsy6Rkepa_jl9VV6vdVx9AeJ7en8KxGptx-TWexM4gO147YtfeOlT3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون آسمان بحرین ، جمهوری اسلامی از موشک های خوشه‌ای استفاده کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18057" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شلیک موشک بسمت بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18056" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50324115f7.mp4?token=XNG4hwf7hP1NWDsOlFUioVUE_ib56lhqAVS_yAVuUaZhNDDQLjc-eGp9aK7Tvlv1mjUmxzePPGebDIwbulT7JAuCfhJBa8mpn5xYSeDuegjpSO48y3xeguq5GP-xBT1qNpOtmf5jrZaVHR3CShPeC5g5PA5_uRt4l2lFK011pk7o2iWeTe4-SkK054kY33Gpo3SRoBfOlJbVQuW-zYASd-eAFKVfzP2c9k3wuZvZftu9DEWxa87KcktOCC-b4k6YrImEnQxCdtM-BkljXDhbm8BJaq3CLF3xI_Ch2HUTaxqDhZ8zTWTOrp5kZc8R_rJIjODkHv6SU454P3UHKuljVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50324115f7.mp4?token=XNG4hwf7hP1NWDsOlFUioVUE_ib56lhqAVS_yAVuUaZhNDDQLjc-eGp9aK7Tvlv1mjUmxzePPGebDIwbulT7JAuCfhJBa8mpn5xYSeDuegjpSO48y3xeguq5GP-xBT1qNpOtmf5jrZaVHR3CShPeC5g5PA5_uRt4l2lFK011pk7o2iWeTe4-SkK054kY33Gpo3SRoBfOlJbVQuW-zYASd-eAFKVfzP2c9k3wuZvZftu9DEWxa87KcktOCC-b4k6YrImEnQxCdtM-BkljXDhbm8BJaq3CLF3xI_Ch2HUTaxqDhZ8zTWTOrp5kZc8R_rJIjODkHv6SU454P3UHKuljVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای نت : فرودگاه‌ بن‌گوریون به حدی از سوخت‌رسان پر شده که ممکن است باعث لغو یا اختلال هزاران بلیت هواپیمای غیرنظامی شود!
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18055" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارشهای متعدد از مشاهده ستون دود(احتمالا آتش‌سوزی) خ دماوند.میدان امام حسین تهران @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18054" target="_blank">📅 20:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8fc831a4f.mp4?token=Tel07LjmmnvsX78PrmaioB-CRStGTef5Jtwj8veOHATw7TXNnfWlKMGWWSprvJmrOmZF0OtZG3rKRzcadjU4RM_PusjCywQhWM45CI0L2pVWJ6o5lkFuqZgOY6sVTReHmqsJVt0uowc4J0iXzUC0ICft-RDz1ITR2XciSHiHtMbiRc2X9pOMTEHgSwq0CUaqbDdQMaNtKeSn0O2wbspxAYwligbwbkkwywAWm8sryHDHNGhIaY545KW3dNgsuDSIgs2MXZMaeqR-jr5-6xHABQQ_vKx_No8OlMj8kxlMcoRGYrR9PGPdiXnwSo5R0TezsOssj9qbi5x2-0mSxbx-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8fc831a4f.mp4?token=Tel07LjmmnvsX78PrmaioB-CRStGTef5Jtwj8veOHATw7TXNnfWlKMGWWSprvJmrOmZF0OtZG3rKRzcadjU4RM_PusjCywQhWM45CI0L2pVWJ6o5lkFuqZgOY6sVTReHmqsJVt0uowc4J0iXzUC0ICft-RDz1ITR2XciSHiHtMbiRc2X9pOMTEHgSwq0CUaqbDdQMaNtKeSn0O2wbspxAYwligbwbkkwywAWm8sryHDHNGhIaY545KW3dNgsuDSIgs2MXZMaeqR-jr5-6xHABQQ_vKx_No8OlMj8kxlMcoRGYrR9PGPdiXnwSo5R0TezsOssj9qbi5x2-0mSxbx-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ایران ما فراوان سپهدار است
⚔️
@WarRoom
🇮🇷</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18053" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش شلیک موشک/صدای انفجار از  تبریز و شیراز
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18052" target="_blank">📅 20:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارتش اسرائیل: ۴ تروریست حماس در شمال نوار غزه به هلاکت رسیدند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18051" target="_blank">📅 20:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_LYdNIi0E-9f-0BS9Ewc37tU7iE2mJRQfYD96_w6tiPOGZ3EfCMas7T3rS1nzfxlFMNTAM-ka7GBiMS2r9aD1v4t_1qNWwuCdONiYQHXqgwnALqmY3-GW3dJkrtBcu7jCtyd6mI6aBpPiR23CNMn4vWJ8PZp1A_YGwvi7SL4yiik68Q0zc_isgq-BVxxVtah8EKBR_vKgBf5qYTGcaV8wWkUnTqm4QelP2BCtfNJXGHuIiL92K0kurXhDtC8wyxxOi3Sg0tZa2h4l6CfPFusD4ioour9WkYIh0-EySUcTom5WaB1XPv-XDQRcMjRCGyRdkTca8LOBEl5iP9boK-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانری مک‌مستر، فرماندار کارولینای جنوبی، اعلام کرد با قبول درخواست ترامپ ، دارلین گراهام نوردون، خواهر لیندسی گراهام، تا پایان دوره تصدی او در ماه ژانویه، جایگزین او خواهد بود.  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18050" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حزب الله عراق: در صورت جنگ علیه ایران، مشارکت نیروهای مقاومت فوری خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18049" target="_blank">📅 20:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammadreza</strong></div>
<div class="tg-text">سلام آقا یاشار.
خداوکیلی تا آخر هفته تهران رو نزنه من یکی خونم رو میبرم بندرعباس ...
داره حسودیم میشه به بندری ها.
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18048" target="_blank">📅 20:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای انفجار سنگین بوشهر
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18047" target="_blank">📅 20:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ماهشهر صدای ۲ انفجار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18046" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرنگار: آیا لایحه تحریم‌های روسیه را امضا می‌کنید؟
ترامپ: لیندزی آن را بسیار شدیداً می‌خواست. آن‌ها دوست دارند ایران و حزب‌الله را به آن اضافه کنند. این به افتخار لیندزی است.
شانس خوبی وجود دارد که انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18045" target="_blank">📅 20:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدای انفجار/شلیک در قشم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18044" target="_blank">📅 19:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تنگه دعوا شدددد
🚨
🚨
🚨
وقوع جنگ تمام عیار در تنگه هرمز،
سپاه هم از حمله موشکی به دو نفتکش دیگر در تنگه هرمز خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18043" target="_blank">📅 19:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb5168e57.mp4?token=h9mkSkPAmQ7JS2sdsctZhw2E7H3EKSuThKClFjW6IFypvE7dxCDojlv3OqfUODnFVyyoIhKL6Q4WF16N4yeCc4ZbOM25i5gOAtDHiWVJlnBWUe0lxr8fIRcHqddiURu6P9Ot_UVZpJmhw7blpcLuJQvCmbPOlTEUwG4DGo0wuEq3ffyPBmtt5qo84-uQ16ByQln6A2KcCON8AUMmU-MAbGxhOvu8D6XZmR1KRsFQVGbf9Yabtj6bo-vfufh-L1ZW9zCEnOqXOXNqNtBTfvrRySv0BABU7KLwdYgg8lpu98JJt2-5W1AC9sYmTzBxtA7LNQc6caCv5NsKO-gRDffCCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb5168e57.mp4?token=h9mkSkPAmQ7JS2sdsctZhw2E7H3EKSuThKClFjW6IFypvE7dxCDojlv3OqfUODnFVyyoIhKL6Q4WF16N4yeCc4ZbOM25i5gOAtDHiWVJlnBWUe0lxr8fIRcHqddiURu6P9Ot_UVZpJmhw7blpcLuJQvCmbPOlTEUwG4DGo0wuEq3ffyPBmtt5qo84-uQ16ByQln6A2KcCON8AUMmU-MAbGxhOvu8D6XZmR1KRsFQVGbf9Yabtj6bo-vfufh-L1ZW9zCEnOqXOXNqNtBTfvrRySv0BABU7KLwdYgg8lpu98JJt2-5W1AC9sYmTzBxtA7LNQc6caCv5NsKO-gRDffCCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونا اول شلیک کردن و این اشتباه بزرگی بود، چون از همون موقع ما حسابی داریم بهشون ضربه می‌زنیم.»
«سلیمانی کنترل کامل ایران رو در دست داشت.»
«رهبران ایران از سلیمانی می‌ترسیدن.»
«من اون رو کشتم.»
«کشورهای عربی به من گفتن: "ترجیح می‌دیم توی آمریکا سرمایه‌گذاری کنیم تا اینکه بابت عبور از تنگه عوارض پرداخت کنیم." و من هم از این موضوع خوشم اومد، چون نباید هیچ کشوری بتونه برای تنگه عوارض بگیره.»
«در مقابل این سرمایه‌گذاری، کشورهای حاشیه خلیج فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری می‌کنن و به نظرم این معامله خیلی بهتره
@WarRoom
یاشار : بازم سیگنال سلیمانی داد حمله امشب حتمی است
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18042" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: از لغو محاصره دریایی یا اعطای معافیت‌های تحریمی به ایران پشیمان نیستم؛ من به آنها فرصت دادم تا به توافق برسند
@warroom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18041" target="_blank">📅 19:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">موج جدید حملات موشکی ایران به کویت
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18040" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb6044c25.mp4?token=jlJAg6VwE_a7YZzloLqAfQGPHhDxAhgIw63U8MFc2ywrC9-OqTSSBltdeqyfpODYq_8dmf_ODtchmp5Wt-obTExiu0Y20PodSKmYSxCj4_iXt3-HJRazm3xMt2qJtsuVPuYd_3QhF4r8oee5gPVILq4JUVW2j4udNqU-alAJ4_9SnCK2piwjA7s55gJwu8HhknWTiyPu4k5Kah0s5xACu_EtMOtQBunvueaY6MsjDhNYc7k9BHnUuTIW3blMRmgScEnSJapKHZaputkjwJTf5K9xmox3pK5QDD_uW3XvFZ8wx45LcdfWDH9UYZyeG2AeYcKm7rkKaK5RyDuIwwUU4zHSeiShnYhckYcuQt1kGzqTHDMh7c0qKZr_0O2_1BmEunCw8luNdXBO9cz-p2_IDwW-NNiPlql7r061j9JBVP0wFFk-QRpMQX8VqPur0fZfkLNyJhoI9pFBcCby-GjhsFggOuOTyElxBZ13ZOdo2MFA1MwuT66_USZNlAFopwMElmMuVcl6xkl887VavUc-nghuZJa5noQcfRD8Bf8BL8nD3JWeVDTy_XWz8B9hdvYt8VkUXbO4Ti86BrZLsLt74pZvz934M1vp-VvX304BWMQaawgd0fzhQrKu438qyrPEj91gFCmP-MyoisO4xCxow7rz4oqEvnaVwE-hi0cMSX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb6044c25.mp4?token=jlJAg6VwE_a7YZzloLqAfQGPHhDxAhgIw63U8MFc2ywrC9-OqTSSBltdeqyfpODYq_8dmf_ODtchmp5Wt-obTExiu0Y20PodSKmYSxCj4_iXt3-HJRazm3xMt2qJtsuVPuYd_3QhF4r8oee5gPVILq4JUVW2j4udNqU-alAJ4_9SnCK2piwjA7s55gJwu8HhknWTiyPu4k5Kah0s5xACu_EtMOtQBunvueaY6MsjDhNYc7k9BHnUuTIW3blMRmgScEnSJapKHZaputkjwJTf5K9xmox3pK5QDD_uW3XvFZ8wx45LcdfWDH9UYZyeG2AeYcKm7rkKaK5RyDuIwwUU4zHSeiShnYhckYcuQt1kGzqTHDMh7c0qKZr_0O2_1BmEunCw8luNdXBO9cz-p2_IDwW-NNiPlql7r061j9JBVP0wFFk-QRpMQX8VqPur0fZfkLNyJhoI9pFBcCby-GjhsFggOuOTyElxBZ13ZOdo2MFA1MwuT66_USZNlAFopwMElmMuVcl6xkl887VavUc-nghuZJa5noQcfRD8Bf8BL8nD3JWeVDTy_XWz8B9hdvYt8VkUXbO4Ti86BrZLsLt74pZvz934M1vp-VvX304BWMQaawgd0fzhQrKu438qyrPEj91gFCmP-MyoisO4xCxow7rz4oqEvnaVwE-hi0cMSX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره فوت سناتور لیندسی گراهام: امیدوار بودم که او بیشتر به سلامتی خود اهمیت می‌داد.
اما آنچه اتفاق افتاده، در واقع چیزی است که تشخیص آن بسیار دشوار است
من فکر نمی‌کنم در این ماجرا چیز شیطانی وجود داشته باشد. می‌دانم که نظریه‌های توطئه زیادی وجود دارد.
به نظر من، اگر اف‌بی‌آی در حال بررسی علت فوت او باشد، وقت خود را تلف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18039" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اندیمشک و دزفول رو ززززززدن @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/18038" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: فکر نمی‌کنم به حضور نظامی در عراق نیاز داشته باشیم
ایران باری بر دوش عراق است زیرا قلدر کشورهای خاورمیانه است.
شرکت‌های نفتی در سطوح بی‌سابقه‌ای وارد عراق خواهند شد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18037" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ : قدرت نظامی ایران فقط یه بخش خیلی کوچیک از چیزی شده که چهار ماه پیش بود پس عراق دیگه مشکل ایران رو نخواهد داشت @WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18036" target="_blank">📅 19:41 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
