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
<img src="https://cdn4.telesco.pe/file/QMG8LJBZNzAHxu-odr1Wh9vtowLgAVmEdLF5Std5b6KpTAqDYx0f3W4FvEK-XR6tpI4eXgkk0GeShH3JKmVwCVzeejE1r4IOzh4q9GHAHvXd3TgR8_RGU7gwyM4CBhjQmqDt614TMgEcHU_g9XW_2661nI1VHIPX55RUwDgegMhZ585-JRI-G2uqogmTD4VkQRx7SfonqBWPeZ2GYGhjolBEh4o3FHteHjyMPOp3yM_UINNYjbW1HiT6RXgzaB5prhVpY9NcDl3WH8f0CcCyeN1OgfZIamWriv2K5-8LYSDR166NozTmEuLBCEZz5mQFej_jxlQk--kDIj_FBv7PLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-146480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
شروط جدید ایران برای توقف جنگ اعلام شد
🔴
سخنگوی سپاه: اگر دشمن خواهان پایان این وضعیت است، باید:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/146480" target="_blank">📅 14:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/146479" target="_blank">📅 14:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یعنی هر لحظه ممکنه پای پاکستان و‌ ترکیه هم به جنگ باز بشه
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/146478" target="_blank">📅 14:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پزشکیان: قدردانی از همراهی مردم در اجرای طرح بنزین
🔴
طرح «یک روز در هفته بدون خودرو» از سوی دستگاه‌های دولتی اجرایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/146477" target="_blank">📅 14:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش ها از صدای چند انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/146476" target="_blank">📅 14:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی‌ان‌ان: تحلیل تصاویر ماهواره‌ای شبکه CNN نشان می‌دهد که ساخت‌وساز در سایت هسته‌ای «کوه کلنگ» (Pickaxe Mountain) در نزدیکی نطنز، که در عمق زمین قرار دارد، افزایش چشمگیری داشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/146475" target="_blank">📅 14:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان: ما مذاکره با اسرائیل را به خاطر منافع لبنان و نه برای خشنود کردن هیچ کس در خارج از کشور انتخاب کردیم
🔴
درخواست من برای پایان دادن به خصومت‌ها با اسرائیل به معنای پایان دادن به جنگ‌هایی است که قابل تحمل نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/146474" target="_blank">📅 14:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مدیرعامل فرودگاه بین المللی تهران: هیچ یک از پروازهای خارجی لغو نشده است/ هیچ کشوری مکاتبه‌ای برای اعمال محدودیت‌ها نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146473" target="_blank">📅 14:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی سپاه: هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/146472" target="_blank">📅 14:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سنتکام: هیچ ناو آمریکایی هدف قرار نگرفت؛ ۱۰ تانکر ایرانی را نابود کردیم
🔴
فرماندهی مرکزی آمریکا مدعی شده هیچ‌یک از ناوهای جنگی این کشور مورد اصابت قرار نگرفته و تلاش‌های سپاه برای حمله به آنها ناموفق بوده است.
🔴
سنتکام همچنین ادعا کرده نیروهای آمریکایی طی هفته گذشته ۱۰ تانکر ایرانی را نابود کرده‌اند.
🔴
به گفته این فرماندهی، این تانکرها بخشی از یک «شبکه پنهان» چندمیلیارددلاری بوده‌اند که برای تأمین مالی سپاه پاسداران فعالیت می‌کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/146471" target="_blank">📅 14:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVQmIs4HRm92dcs2N7HEgNrIPVQaXbC6Q6iN9ir73gIuGx4wyK4mH-XClZNOhXxmR6y1F8xKE2E_OS6nF1XYA_SSTZTQ4GevC5qbtwP2i9toxgUbFqYS-bpyU_9tyy-mbiZuLmHjMrqd2MTCYDsylhG1ClyOa6DYbd8foLpn6Feq9I6r8hCcBAabnKgcpm-QMlk4fAYHLN0F0LKIq6PwQ_2Qr2rvx3AiW4YU3Ah0W6e4Nh0RNFuhYdLjfSNg2cuvuBoDBBcsy9ZeQEJgCaK0ZCF7kUHctuWfGJrMBJUAH2AOxCIKVp03ZSBR08TaNEDTjwVaT_rbAhzCIJ5bvLhaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: یک کشتی با پرچم پاناما در آب‌های سرزمینی عراق توسط یک پهپاد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/146470" target="_blank">📅 14:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الجزیره از متن پیش‌نویس قطعنامه آمریکا و اروپا
:
در پیش‌نویس قطعنامه‌ای مشترک از سوی آمریکا و کشورهای اروپایی که الجزیره به آن دست یافته است، تأکید شده که ایران همچنان به تعهدات خود در ارتباط با پرونده هسته‌ای‌اش پایبند نیست و از این وضعیت «عمیقاً ابراز نگرانی» شده است.
🔴
در این پیش‌نویس تأکید شده است که نبود اطلاعات درباره مواد هسته‌ای و اجازه ندادن به دسترسی به تأسیسات ایران، دو مسئله‌ای هستند که نیازمند رسیدگی فوری‌اند.
🔴
این متن بار دیگر از تهران می‌خواهد عدم پایبندی خود به توافق پادمان‌ها را در سریع‌ترین زمان ممکن برطرف کند.
🔴
این پیش‌نویس از ایران می‌خواهد به‌صورت جدی و بدون پیش‌شرط وارد مذاکراتی شود که هدف آن ایجاد اعتماد در جامعه بین‌المللی است و بر حمایت از دستیابی به یک راه‌حل دیپلماتیک برای چالش‌های ناشی از برنامه هسته‌ای ایران تأکید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146469" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: حملات حوثی‌ها علیه عربستان سعودی ممکن است منجر به فعال شدن پیمان دفاع مشترک شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146467" target="_blank">📅 14:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: تلاش‌های میانجی‌گری میان ایران و آمریکا ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146466" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
آکسیوس: تصمیم کاخ سفید برای مخالفت نکردن با تلاش بریتانیا در مورد تحریم شهرک‌نشینان اسرائیلی، نشانه‌ای از نارضایتی واشنگتن از سیاست‌های دولت نتانیاهو در کرانه باختری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146465" target="_blank">📅 13:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دلار به 232,000 تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/146464" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=ObRyfDMe0BprhD6EbLLgPBrDvvuRFO_FjABeqLkAilinlaW6ZmYJapbbA49D-XwzP1yg_VX3VgFFJJtRc6q2V552oDbtr4Il-tb-2MSW0zVi1bxb3XtRjSvt9fLh9Pttdfc3mOiud-BJy1gvLsC8u_Gx329ZNsw4lhMxRr7AhpESpU3ao_L7i9EVhxe0h9LlAqZ13DjijgzbIvKbdP1mLpPcTsUr1mU3H1mmOx6NQnPy0e69MxBltJnQXar14RaU8FoovM_f-AZmWCa4X4vAiYo4_a7odPm5F_o_R-Nc4yjul1tA0X8NxfIKKd7zKnWmqOm25qcJz-_6v2qsumEFtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=ObRyfDMe0BprhD6EbLLgPBrDvvuRFO_FjABeqLkAilinlaW6ZmYJapbbA49D-XwzP1yg_VX3VgFFJJtRc6q2V552oDbtr4Il-tb-2MSW0zVi1bxb3XtRjSvt9fLh9Pttdfc3mOiud-BJy1gvLsC8u_Gx329ZNsw4lhMxRr7AhpESpU3ao_L7i9EVhxe0h9LlAqZ13DjijgzbIvKbdP1mLpPcTsUr1mU3H1mmOx6NQnPy0e69MxBltJnQXar14RaU8FoovM_f-AZmWCa4X4vAiYo4_a7odPm5F_o_R-Nc4yjul1tA0X8NxfIKKd7zKnWmqOm25qcJz-_6v2qsumEFtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شرکت پخش فرآورده‌های نفتی
:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را برداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146463" target="_blank">📅 13:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: ما حملات مجدد ایران به اردن را محکوم می‌کنیم و آن را نقض حاکمیت ملی و نقض قوانین بین‌المللی می‌دانیم.
🔴
ادامه حملات ایران، تشدید تنش‌ها را تشدید می‌کند و تلاش‌ها برای مهار تنش‌ها را پیچیده‌تر کرده و تلاش‌های دیپلماتیک را تضعیف می‌کند.
🔴
ما بر لزوم پرهیز از هرگونه اقدامی که تنش‌ها را تشدید می‌کند، تأکید داریم و خواستار بازگشت جدی به روند مذاکرات و پایبندی به دستاوردهای حاصل شده هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/146462" target="_blank">📅 13:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رئیس اتاق اصناف: گرانی کالاها صرفا به دلیل قیمت تمام شده تولید خود آن‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/146461" target="_blank">📅 13:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
عوستاد خوش‌چشم تحلیلگر صداسیما:
تو پاییز یه جنگ شدید، اما کوتاه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146460" target="_blank">📅 13:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L13zpol1xRj67vcbjyYMyjfhgiwZLNzKCyeuCs_wLxKb0bExcWdfxxEaiezkyh6ZROk8Nf1KVPYGEMGUeaiqaBcOT-SXEK2qH0zlTVrI4uZWt5NH6uvy9oWaWz6uwAGs9tF0lMkm-T41UY6cCAjC6Un6NYZ7TavnoEHESyaFvuE3kRM2wdzZ631kGxaknEonCHmVJe_7qaE-Y08EXhivfHlL5eMdgZ2-BMPiQ2O-HrfSn4Y2DPNPum5KjubR_lctXeYhA8xWbwXpNrgpKvWrxs_fOd33dP-HYJoibl2FI3EfJ2tvh0BOYjDoaoXw5xijtMN3UWwA82ew-hsX3GISfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی در شمال غربی بندر رشید در امارات متحده عربی مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146459" target="_blank">📅 13:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت و گو با الجزیره : موشک‌هایی که ایران به سمت اردن شلیک کرد، هیچ تلفاتی در میان نیروهای آمریکایی برجای نگذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146458" target="_blank">📅 12:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دلار و طلا منفجر شد
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/AlirezaMehrabi_ir
https://t.me/AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146457" target="_blank">📅 12:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شعار دیشب در تجمعات : اصلا دلار بشه ۱ میلیون، نمیریم از خیابون
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146456" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5eec3b402.mp4?token=Nyi4zQ9dM8-wXJarM5VtPvyZJdkyo9cuYuaGNig6RS1uWDA4ZevM1_--6E9Mrds-_f1AeMmeHsIfZMOGbwahmluxK9vjrv41xRLJGD1vsLd9tCG7_Yqzt_Oxcp0tIxET5xRdHWtxwNV3NxOHkHzzwHyZR07DLg_zPuyeq7nNPlPkzULwygysJcb4O9PQf6Jj0H6UkqTM3b19N0ZsKwWdY3AezgcKI7_z0Il5EL_0AriNVf0NzAPsLVgB6zhXjl_MxvsyDEBZwE_O1ggay9xgCidHuWWsxWLFDFAi-hoz-Rz10msD4jyGTwWDydwPvzf30GxUv9cuvmLumw6It0HxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5eec3b402.mp4?token=Nyi4zQ9dM8-wXJarM5VtPvyZJdkyo9cuYuaGNig6RS1uWDA4ZevM1_--6E9Mrds-_f1AeMmeHsIfZMOGbwahmluxK9vjrv41xRLJGD1vsLd9tCG7_Yqzt_Oxcp0tIxET5xRdHWtxwNV3NxOHkHzzwHyZR07DLg_zPuyeq7nNPlPkzULwygysJcb4O9PQf6Jj0H6UkqTM3b19N0ZsKwWdY3AezgcKI7_z0Il5EL_0AriNVf0NzAPsLVgB6zhXjl_MxvsyDEBZwE_O1ggay9xgCidHuWWsxWLFDFAi-hoz-Rz10msD4jyGTwWDydwPvzf30GxUv9cuvmLumw6It0HxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادتونه ابوطالب گفته بود: «دلتون برای دلار 78 هزار تومنی تنگ میشه»؟
🔴
امروز دلار به 3 برابر 78 هزار تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/146455" target="_blank">📅 12:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602dc700b.mp4?token=hoyS9cKV_EdhhC0il0EH9CbsFqZMDw7uP3jEc2CnNlMIn11tz4r52I7s46O1uuAML3xlozZSEWIDoLxLDdOlgL4DP3MvvveR8cEZUARqltdaCLJP4NlP9iQLLc6W94NDvaqT-rMN_6XtCC7RkaaM-GwyOrsxa3_XX_bonjkstGfkNSIh70ump5xkco5yX2Jjp7Un9ZA8K8nhHvqb0ggUUwIWLMg0lAimzCOiyibBERXXEuRiU4F2m6r1omOXvlO31iPxDc-u0UiHqw2hZpzE0AjF3D2U22msfSxM9-r41PZ2qW33qPot-xuHaKbM_AirWqAj04UzrdzKS6tYnJr4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602dc700b.mp4?token=hoyS9cKV_EdhhC0il0EH9CbsFqZMDw7uP3jEc2CnNlMIn11tz4r52I7s46O1uuAML3xlozZSEWIDoLxLDdOlgL4DP3MvvveR8cEZUARqltdaCLJP4NlP9iQLLc6W94NDvaqT-rMN_6XtCC7RkaaM-GwyOrsxa3_XX_bonjkstGfkNSIh70ump5xkco5yX2Jjp7Un9ZA8K8nhHvqb0ggUUwIWLMg0lAimzCOiyibBERXXEuRiU4F2m6r1omOXvlO31iPxDc-u0UiHqw2hZpzE0AjF3D2U22msfSxM9-r41PZ2qW33qPot-xuHaKbM_AirWqAj04UzrdzKS6tYnJr4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انفجار در شمال ادلب سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/146454" target="_blank">📅 12:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رسانه های سوری گزارش دادند انفجاری با منبع نامشخص در شهر سرمدا واقع در شمال ادلب به وقوع پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/146453" target="_blank">📅 12:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / سازمان دریایی بریتانیا: چندین کشتی در شمال خلیج فارس و دریای عمان، در پی هدف قرار گرفتن با آتش، دچار اختلال و توقف فعالیت شده‌اند
🔴
هیچ تأییدی درباره وقوع تلفات جانی یا خسارت زیست‌محیطی در پی هدف قرار گرفتن کشتی‌ها در خلیج فارس وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146452" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری/گزارش ها از حمله پهپادی ایران به یک نفتکش در سواحل دبی، امارات.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146451" target="_blank">📅 12:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
در آستانه جنگ جهانی سوم هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146450" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijsWlpqsKBw3kr06yBE_Q2VjfGScisdscbgbOnYK1fgh1ZZ6Md4huLKlp-ww3Im8scrVmFO24MaEMJVs5yxAJ_xR8Bz-2COI36CGnthmG5W19ZaTw91sPRsbztBm376WJqxVqFqdhnL5Yjn0bkKmNEpujNrbk14TACEnB1bHGgmQ1lIaHjbveovUhwTavcP9yERYG1El179xxPhJs1BjGhmJmlcboXMpgfxJeDCUz8o74Zt3QkmHC_hbWEkJYmeSUzaQaHRHT-UbTZLzkZErvaWizM7LPtmsFguEHfO_ZfwniQf1514oNR_nqJihn-DFIN8hu8W-GrJKq45auNiZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایوان هوبینگر، مسئول بخش همسویی در شرکت آنتروپیک، می‌گوید که "احتمال بیش از ۱۰ درصد" وجود دارد که هوش مصنوعی در ده سال آینده "تمام انسان‌ها را نابود کند"
🔴
هوبینگر گفت که شرکت آنتروپیک "تمام تلاش خود را می‌کند"، اما اذعان کرد که این شرکت هنوز برنامه‌ای برای حل مشکل همسویی هوش مصنوعی فوق‌العاده ندارد و "هنوز به وضوح در مسیر" دستیابی به این هدف نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146449" target="_blank">📅 12:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=to5-MWeZfe1xMBTPACcnfnk29ZupgXnS6ZlQQS-KwIX2o4AftIcQOfArn87tbh7bHoxDIPqegIcWUGg64uAH_GsZ7k8oJ3d-SA4ybGr1DMlmLKzCtBHK-Mh3gjt_ldb964RTFz_NHLM7NaV-L8pHbtDemMEgG4scbkJjE9v5mzOnwWMEqcbJss9RzkheD0TK4puZClk3pR0ACy7E4wvjT-4g2vM30hNxHHACqECDbtOHrx4C-gxXP6Z24vvp2MxpeUpx-5-doQPAv1ICjJP-BANb_oppdAX8hxAQk7rjGFggPr-8YRXg4ilLRqRm-Cyoa0haJyxgLuqMjFkMdVTm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=to5-MWeZfe1xMBTPACcnfnk29ZupgXnS6ZlQQS-KwIX2o4AftIcQOfArn87tbh7bHoxDIPqegIcWUGg64uAH_GsZ7k8oJ3d-SA4ybGr1DMlmLKzCtBHK-Mh3gjt_ldb964RTFz_NHLM7NaV-L8pHbtDemMEgG4scbkJjE9v5mzOnwWMEqcbJss9RzkheD0TK4puZClk3pR0ACy7E4wvjT-4g2vM30hNxHHACqECDbtOHrx4C-gxXP6Z24vvp2MxpeUpx-5-doQPAv1ICjJP-BANb_oppdAX8hxAQk7rjGFggPr-8YRXg4ilLRqRm-Cyoa0haJyxgLuqMjFkMdVTm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار 230هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146448" target="_blank">📅 12:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQAdESPQqO2lVLETHYtt8Vvq89fPg66Faf312xe6FWgu-7YOBxwSL4BZ1mEeIeRkaSzDw137ZhketGu2lCBPXiJiE-jxMA97UYwdzcmY4_OKqHCNM9IvKp6eWnNSRLrpKnmT-aqdcylqNKYJVUroWJ7ngTfJ08qWDbLNTPLgLwBvjGFUUPvALUD6kae6iVkTFKYAiDCJPF9q2T64ON7krD5tnyJSMPgIAT0-AWkU4BxV35gv_NRWQW5zLjU8eoSws5CWmV7wJaaddiqNxCOGm5IhtP3i8TV8nTNRQcjQJH9vfy3lOJbBwuHLcalnpwwktxOeil_zF0jKCXsPsj9cRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای تانکر سعودی از پایگاه هوایی فهد در طائف به سمت یمن پرواز می‌کنند تا به جنگنده‌هایی که یمن را بمباران می‌کنند، سوخت‌رسانی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/146447" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
طبق اعلام خبرگزاری ریانووستی، بر اساس داده‌های وزارت جنگ آمریکا، شمار مجروحان این کشور از ابتدای جنگ با ایران به ۸۲۰ نفر افزایش یافته و شمار کشته‌شدگان نیز بدون تغییر، ۱۸ نفر اعلام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/146446" target="_blank">📅 11:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دیروز بهتون گفتم ارزش ذاتی طلا 24 میلیونه
‼️
الان با این قیمت‌ها هنوز تقریبا 300 تومن زیر ارزش ذاتیشه
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/146445" target="_blank">📅 11:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
قیمت هرگرم طلا 18 عیار به 24,000,000 تومان رسید ...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146444" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146441">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrE_zQ3f7-iopSZznNBhQjx3ne_W2gslbye7HIQOh7SOiqZ8VyZrmzSiKeaLNvrR7V8lfeJAKFmiMMEJ5EHI6c5c-I6ntCaGkWX5Rsoa_UMWYyL8MDsZ7HMOJLRfH7glrQeud6WV43MmMdCTx15OGJrgoClfMHIUBRmLZ-YLPESe0qS2yRhLnwqvyQouqpHiVnoKlwDS2v7BRtkszcw6Eud2siVmT7LThNGsl8WtzWSiRYJ8u-fqdnlPTe1voV_uhE7ux4ypwULHPGKyeNu9W9SCsJu_KZhPpYDy29ZZsYdCiUa3r0Thaz36HPsqZuD4U1phCPx-uCwm1t4LsAbRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c690ff7b.mp4?token=GifWJ6gi6w5MZ34V6VRCNB2cjP64YeEj72PfDoFYJhziiv5YMhxfTghbJr2N2DZ-zRiL4XeiAduVTHGxjD5iEM845C_-KE1kFZ9cGOH_k_Sl7EDPBoKdnmWBmPlypwk5W47utofISA3eGJOUYZvQpDqidhxxpuSNFrAVQ31DaWllPXjz4zvV88pZPueFQpN0XOvtJVsRzJ7gIDoGojLvkMeYE3JFlB06piKQqivx1x7kEGK079pCujbbukWWt_f3198rBCUXdv-b5_8gmDX72DwQpkebAGASOHD0SZ3P1ADdbHgqvJh1gZZzP3D4VtpJv4WXrSovkYkie8uHbFgWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c690ff7b.mp4?token=GifWJ6gi6w5MZ34V6VRCNB2cjP64YeEj72PfDoFYJhziiv5YMhxfTghbJr2N2DZ-zRiL4XeiAduVTHGxjD5iEM845C_-KE1kFZ9cGOH_k_Sl7EDPBoKdnmWBmPlypwk5W47utofISA3eGJOUYZvQpDqidhxxpuSNFrAVQ31DaWllPXjz4zvV88pZPueFQpN0XOvtJVsRzJ7gIDoGojLvkMeYE3JFlB06piKQqivx1x7kEGK079pCujbbukWWt_f3198rBCUXdv-b5_8gmDX72DwQpkebAGASOHD0SZ3P1ADdbHgqvJh1gZZzP3D4VtpJv4WXrSovkYkie8uHbFgWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به یک پایانه نفتی در نووروسییسک، واقع در منطقه کراسنودار روسیه، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146441" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye7C-lPqm-tptRy_xAYW8zG2Y1-SvB_mE0bYfhw85AO-136JQ_ka1LONYw_oX9vD7fQT-6RIgBx6jAe8as94FGrSCBYKxFxQVUFRYbVgJmcTKRFW0sjTQBUTXGfyaVuA9cUl2ov51O3IdRzgNrS2c98gH8Wqi603Xm4IGnRqlNkSRucohA2iNuVoV56jJdt92aW1aTmEEeJ-AWqQ9NAACEbWDTK0BaUzh0Mio5Caotm35jOrDEOT-2UueQdnHQf_OaQU_4A_efcXc07A75Kbd6tEA8zkG6WGSidmg8166HnR96uFT_ItB-mSi24dlRU-rZAatGgH7Yzmqwm8aGFRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEy7IcxkjHYwROgEb6ddCDkEUfWuLphKxgAVW5djnhoCJZp_oIlRHOO_v1BLG1DMTwIn_D-cP9xYhbQsFSAsTx88hROgQQFWR4Cl5U0Wr9P9Bbq4T4JjglYnoEyEvtQOvhzU6Gvs8Nh4G4mkqzwgpAtAt5AlR1IqY6LHrwdCvFrCaY-B0CF_NQDvd_L-scvMgW_zX0g5zGs_yJY1fcDA5ZKU-lFvkGabTRwES2LsYA2zeuzoq5Ymsqp-r1zOAYhlvYB4DgKY0-wjAubg5aD9X3tYGDyq-wQTQte1cr-1iyubXUkg1_BSF2_cEcogK_VaktT19mp-rCYZUttMFHtzyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اولین گوشی تاشو اپل با نام آیفون Duo و قیمت ۲ هزار دلار معرفی می‌شود
🔴
جدیدترین گزارش حاکی از معرفی موبایل تاشوی اپل با نام آیفون Duo به‌جای آیفون اولترا است و مدل پایه آن با ۲۵۶ گیگابایت حافظه داخلی، حدود ۲ هزار دلار قیمت خواهد داشت. قیمت این گوشی با حافظه ۲ ترابایتی نیز می‌تواند به حدود ۳ هزار دلار برسد.
🔴
همچنین برخلاف شایعه‌ای که پیش‌تر از عدم پشتیبانی از قلم اپل در آیفون دوئو خبر داده بود، گفته شده این قابلیت در گوشی تاشوی اپل وجود خواهد داشت. شرکت تولیدکننده قاب گوشی Dbrand نیز تصاویری از طراحی این گوشی تاشو را منتشر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146439" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146438">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d1aa66745.mp4?token=ktwlewQGSRgsDQLdUt6IfpcQWnpwsymjd6mOpK4CQaiEcJdDuT8n4PYMaQ4IsaZ_1XxC4NpCG1I-UWSu5LN6CCs-O-IY-edcl1HD-0QLkV9-vtpK7echkqxXGOt47X9CUIjl1ql1Tuy1c4XODgXSA5f7BuQzDmzg2W3j8HxpZxnreJwqeFN4c27tfMZUKIlz-zwo_7LNEjtdJSU7Z_lGxS9ORfDjCsQGTHt6MaGBBG0-Un3V0lFmHyXDPdTq3ofAAGMdLA48KAMSIAEuNKJB89FDlKFochyXzYL-Sn_KmwdghJlyz7poYCeLP4gvrA5acrt2cqlYHreRYX1g5XFUj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d1aa66745.mp4?token=ktwlewQGSRgsDQLdUt6IfpcQWnpwsymjd6mOpK4CQaiEcJdDuT8n4PYMaQ4IsaZ_1XxC4NpCG1I-UWSu5LN6CCs-O-IY-edcl1HD-0QLkV9-vtpK7echkqxXGOt47X9CUIjl1ql1Tuy1c4XODgXSA5f7BuQzDmzg2W3j8HxpZxnreJwqeFN4c27tfMZUKIlz-zwo_7LNEjtdJSU7Z_lGxS9ORfDjCsQGTHt6MaGBBG0-Un3V0lFmHyXDPdTq3ofAAGMdLA48KAMSIAEuNKJB89FDlKFochyXzYL-Sn_KmwdghJlyz7poYCeLP4gvrA5acrt2cqlYHreRYX1g5XFUj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارش شدید باران در مناطق مختلف ژاپن در روز‌های سه‌شنبه ۱۷ و چهارشنبه ۱۸ شهریورماه باعث جاری شدن سیل و آب‌گرفتگی خیابان‌ها شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146438" target="_blank">📅 11:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neDoKLsFF2i08q9ArGuoz3Usj-6H6ztpHZ4KxpMCtb85jjRMdndrvWw0usxWreoNvGsluNL5wtCJNQAYoVdhZa1W1MBVHvzwHfcZstGoZilPvGUaVNbm0fiCfqdKX00lr1g4_Et15PvtykAWDwdqB7NBiGKVdBkl3ZaZ6xwCvOxseBv0LlXDGxcT-xmrghKNPAwBx5As33IA-Ec_mlSP0fTi-R58DuDvj2-pPLUXWKT4VVgGswSOaNlcoGRhq8HDnAkTPiNpin9dGGAsSNcyzSvC3XtzNdUhRzTWPeLgRssvnJKQH9ahyyV2yPToGZwVuS2KLar8I-b3sjnunoGG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kq7eZLs0Q74ba36lmcTt6fSGOWRig4RSwB-uLzvldnPCEzX-2XhmesRd2Ho7Ni9VF8W6HQX5iR5fg7E2Em58O0L32JTqXHrr4Tw2WwUsIZpJTse5jqIMAGoaRBK7j0wyP7qmz06ZBPXlE7MpCoJk_Q4jgkwTqj5muNRrDSN7qM70NGE9jjldRMwIE5Q_T9vii69Yf0D7ZKeM06Lfk-bVZH4oZq0mKlngyH_09oKFiZVCUCN3ssNOaf-48_KGAgF6qQ4Sp6hDxJzsFuyUPieDm66CYZ_TPMRY4nc4FdEmbGmXbWUNB_mZBkJYj5lGl4P4DvPNhwt2Dlk_33gJELTVew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شلیک موشک از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146436" target="_blank">📅 11:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146435" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc7szHqAU0oNkyv1OiPeGpsNToOOQKiFqgXI4A_vVknlfRqZhg221A8-QIRpA4Rw9a911WQMM9PDycEQEDIE0ZNY8xthOegXqxdjHJiL85Popt06eGWsu9T85wos8dk0JYbcaVvrTrTeYeF4EzjEsYNU3OYE13Ts8vNmUtCFHb-w5ucIg1t9KESty2rjEJXS1q_IT1IHMcNQyOg-M9zZpeBaKZutyA9-E8zQu95rlShQ8bI45h60tZBEqy7c6UL2qxaND51BTX2jV5GT4LJ7X_9KZEtiw1ZhUBtVaak1q1UJ5DQePOgn9iKOpGG07Lim3wCIbMXBxGLZyI-MZwRNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی فعال رسانه نوشت:
‏در پرونده فساد فوتبال⁩، برای تعدادی از مدیران ارشد و چهره‌های فدراسیون فوتبال به اتهام اختلاس⁩ کیفرخواست صادر شده است
🔴
مهدی تاج⁩
‏
🔴
محمدمهدی نبی
‏
🔴
احسان اصولی‌صفا
‏
🔴
تهمورث حیدری
‏
🔴
خداداد افشاریان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146434" target="_blank">📅 11:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
احتمال شنیده شدن انفجار کنترل شده در جنوب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146433" target="_blank">📅 11:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7GZku5eRErGFfyOqzm8Nt77KucoEuahKdsiVRCZ-zVTCtVXDbpQMWUqoEe1Yxsl_ecIOoP2OiwCN4k-vQSkRhap8PA_krbn8Fj3wWwm_YoKXU-8deN0aZTRMU-RP_dBSpZNWHrHcEMv41eMLKXSu4BUrqe4vzIM8f7T8Eg4etj5cesZAujmQWgNwau1c7N5l3n3Ifhqahd31CYTZnEvQFGq_9Ra9PBbse2RiZU3jPJi92jw8ltZ-MtxVaN-FQjidabj3Yb7HH1uU5gOVLB270fCbZADqROYq6GD7qkRwBcfrpBri8Vk-835ZHWkkyPL2swn2oWG-1MU7MjMfJ63hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر جالب و ترسناک از رعد و برق در رشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146432" target="_blank">📅 11:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyOhcO5tSGJFceZzymErORpM1x38wcIK28ExE-6XF4F5XIywrsr0QSn3qR1J_pLETTltkeOzy-iYVc7qthW9r1sIM56dMFd9K3ahPOE5oOl5N9kdo2ZviD13JvKFlqGShtNnJldOI9WQ8fJ2UF-vve5aQ-4AkYyKGxT2NzZ6yL6D1A1GPQLqNAswuzQ0ovWVSD9_kma7IQsrpNHQvboSGeMWGmdqAnZmMS8SnCjE_3gwwefuj4KHUaYkkFvQ_fycctg-bdsfrLFTZZAsAiZTqdxfBN43uNjlXmbDy1OJzLq8KXRh7FIxmeOy9CipO9oPqCsBb6KJUjHAd1UjilKqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759ddd2cc9.mp4?token=i2R36NqztuttylvOydTq075weoLsEeaYVUsF2E-KcPRDto4ULNHKd9IklBs8ECLXQYWDCxuPOt-Dlzz5S_lK4ccOpU4WSYTngtdkWHARfQpbUlIw87OjN8NqmIY-_c9ZcXIgo0r4avfuz94SzLFLdQyQe88sY_l52ShyxAjSndmwEmUZOUIGzDhTZWh40CXm0rrNyU-CoFSGLYbV2Td_HuMMeSFYZQivEt0FxZvK3sWT0-wXUGx4zENeE_P2xOXN6e3dNQybz0UhpfDILNmM7YBy_3pyY4fjYIRNQ_ASn6W5JpNV0Sh7BxhdqGzOsfHerhjbeISjar64IxkTvQE5Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759ddd2cc9.mp4?token=i2R36NqztuttylvOydTq075weoLsEeaYVUsF2E-KcPRDto4ULNHKd9IklBs8ECLXQYWDCxuPOt-Dlzz5S_lK4ccOpU4WSYTngtdkWHARfQpbUlIw87OjN8NqmIY-_c9ZcXIgo0r4avfuz94SzLFLdQyQe88sY_l52ShyxAjSndmwEmUZOUIGzDhTZWh40CXm0rrNyU-CoFSGLYbV2Td_HuMMeSFYZQivEt0FxZvK3sWT0-wXUGx4zENeE_P2xOXN6e3dNQybz0UhpfDILNmM7YBy_3pyY4fjYIRNQ_ASn6W5JpNV0Sh7BxhdqGzOsfHerhjbeISjar64IxkTvQE5Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رنگ‌های آیفون ۱۸
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146430" target="_blank">📅 11:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX-0v1IrGGFacKx5BrZaQUStUVONfIP0BpFrsFXXyVhaQLVwS2_O8L98cg91vjWa2qX_drdibxDm8t9MKpgb-DT4fEbijBVCsUmRRyOCh3-CbIfNIBLFji9XoFKYpHb65dSTbSVHH-Jf8c1MWVrs3etkTL8-_zh9lG0QQCgOjriCff0fLKQm6bi7NqPuxfZ6yxSD-xJ9T2OnCSjTL0DsPdxmKf9KUQtV3uWzPnYMPvSzuH48HsMboBT1K52ykvUwNsztCMub3pwZYPqACy8KQVaqPUYJxFtGGsh_eVAfkR73LvQV18F-vfh2xh-sKhnkQWGvA3p6CuW7IlmKlYrn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت برای اولین بار از ماه ژوئیه به 100 دلار به ازای هر بشکه رسیده است، این افزایش قیمت در پی تنش‌های اخیر بین ایالات متحده و ایران رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146427" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37c9e54d8.mp4?token=Ycq-rNf-yyVi5vqO_IRRANCPNJ-Bl3tf7AirDcCrKYCumOHZLvGEz0bpTA2ma_i2v3lRZ_wFjU-0GKFhFf9BrqAKDHetI18fNvyNRIaVaXTmHoklzTX4SKh6p8vSPsd95mtcma2RoOnIuD8P8a_u9G0ZVZJvpyXRl2oyjJWeQD3pxZ0VJ1F6xQoJ_vzRlF5PmanfSuy_RBiGNxmdfm2h4DTRnFA5o45CeKmUEpQ-sP9wkcuDuTxyyOZMiWZGpslDFr-wd0coxo_t4gCOszwQJPdM3Nr3IfdCvzIoavPJoKZ4-KqE0r4iZv8srZiG_VWSkGs_Y5tky3vnuS0eYBYjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37c9e54d8.mp4?token=Ycq-rNf-yyVi5vqO_IRRANCPNJ-Bl3tf7AirDcCrKYCumOHZLvGEz0bpTA2ma_i2v3lRZ_wFjU-0GKFhFf9BrqAKDHetI18fNvyNRIaVaXTmHoklzTX4SKh6p8vSPsd95mtcma2RoOnIuD8P8a_u9G0ZVZJvpyXRl2oyjJWeQD3pxZ0VJ1F6xQoJ_vzRlF5PmanfSuy_RBiGNxmdfm2h4DTRnFA5o45CeKmUEpQ-sP9wkcuDuTxyyOZMiWZGpslDFr-wd0coxo_t4gCOszwQJPdM3Nr3IfdCvzIoavPJoKZ4-KqE0r4iZv8srZiG_VWSkGs_Y5tky3vnuS0eYBYjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تذکر صریح معاون دفتر پزشکیان به مجریان صدا سیما: شما همه چیز می‌دانید! تجویز نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146426" target="_blank">📅 10:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lva0I60uYP72IDh866QvK2jtT43d5lES71Fiiu1gOEA3IJjH9Ed_cBV16rUoU7zdRgJsumQ3_XQYMKXxRFIB0Vh6yOe8njU8f4PyuhEJE82it4NUj6dn8ztEfuEsqMHKaynIQB-D_lxsmvQ3aWWHc-8geZcPEwKHxUba5gMIuiKX7__7HYt1wxSyWtMNLdV33_C1c0xntw-VBCThTbmXfPALszm9IcjmqGnlvLMK4-ItV54-x2hYBE4B8ssebGqpMhGhQbagj8kWSopoKkgnfz4b0PP0rpyyrb_XFx5Dn54V4Mkr4aYZOZgGtM2kBBMmEBwHTiFllaMLoBAuQgVOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس سازمان فناوری اطلاعات به کارت زرد مجلس به وزیر: دفاع از حقوق مردم اگر هزینه داشته باشد، افتخار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146425" target="_blank">📅 10:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اسرائیل در اعتراض به تحریمهای جدید بریتانیا علیه شهرک نشینان به کنسولگری بریتانیا در شرق اورشلیم اطلاع داده است که باید ظرف ۳۰ روز تعطیل و تخلیه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146424" target="_blank">📅 10:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / گزارش‌ها حاکی از آن است که یک نفتکش در نزدیکی سواحل دبی، امارات متحده عربی، در حمله پهپادی ایران هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146423" target="_blank">📅 10:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مقام آمریکایی به نیویورک پست:
در صورت ادامه شلیک‌های جمهوری اسلامی تمام ناوگان نفتکش جمهوری اسلامی  را هدف قرار خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146422" target="_blank">📅 10:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2dd7afa6.mp4?token=WAfUVVcfLwu0TxQ_lYMx1t3WcpGXcU2UMYg3aAboJQlcCYzVRwOmeZNXYL7OO_3Nnt0OiLcqB2LKfcWGPUz0-WCG1sUZCHXgvaanW4xAu5ckM5fQv93pH3-fZ1Urn5Cb7yGl_6emuA4P5COSvWOWIR8ganguofh2m9u2DldV8_jqIBxF6EWLXqcyi3mVG-LWaSDNBeEcLX6q-8hb8SS9wExdnrtB-stmWvPVCPpOKkcHo5GimIk-5wQ5Qo30N40BRAD0pSYd2hlbDeekA_DM8HezVABF2TkikKAFLzi_xfD8Cw5UfRtmpn1p3TETe5uOGet9UCsEOEB_NCrSKX4zcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2dd7afa6.mp4?token=WAfUVVcfLwu0TxQ_lYMx1t3WcpGXcU2UMYg3aAboJQlcCYzVRwOmeZNXYL7OO_3Nnt0OiLcqB2LKfcWGPUz0-WCG1sUZCHXgvaanW4xAu5ckM5fQv93pH3-fZ1Urn5Cb7yGl_6emuA4P5COSvWOWIR8ganguofh2m9u2DldV8_jqIBxF6EWLXqcyi3mVG-LWaSDNBeEcLX6q-8hb8SS9wExdnrtB-stmWvPVCPpOKkcHo5GimIk-5wQ5Qo30N40BRAD0pSYd2hlbDeekA_DM8HezVABF2TkikKAFLzi_xfD8Cw5UfRtmpn1p3TETe5uOGet9UCsEOEB_NCrSKX4zcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از انفجار ایجادشده توسط اسرائیل در شهرک المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146421" target="_blank">📅 10:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCOewTifWpSL5Yw5ECsQ5TOKf-A8SUy4RscO-AVVWBgLTl61GZZhsdPiTvG9dfW-I4ovgWGkj_BKHknCM7XffIStqnFSFPW0BrJIBj0D-cNFp0q4dqfT9q2OIJE8rwjUw8H_cTka2ldEx4P3opYJI8KtzFJHSpS6Zc8XvFTY58p6PopgnhDht2uIdG-G1gBc24Og1EatNGIXE804x_LaIUGhUqW7CFdL8xCwdWpKNRx5ZJ_23R75Oc_rTCd8uGBkV0S8Wd67BoAfuJ0ZsS_v9m4rUFTffwM4VjsWvDVP9qVpRs_tvunxUKbdF_Ih-oqeV0zchYFBUB8F9aufPgfJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران با دلار ۲۳۰تومنی تو مترو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146420" target="_blank">📅 10:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پادشاه آفرود ایران شده 1/300 میلیارد تومن
‼️
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146419" target="_blank">📅 10:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
آخوند ، طائب: آقای ترامپ اگه میگی مارو شکست دادی، پس با کی داری میجنگی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146418" target="_blank">📅 10:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هشدارها در خمیس مشیط، جنوب‌غرب عربستان سعودی، فعال شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146417" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
آیدیش:
@khabar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146416" target="_blank">📅 10:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5KNhbaNWq0LGTfyhmBLYN0_yAnaiwZvetuDX1bzx_T9vk47Bf0oaA1EdAW-VgiaGNjy3aIrA0lniyVVL3-Dsgz6XXBuO3nbqBqOoQMDpb26hx0qMx-JDsFVMQiU9n_4urCTEKMtRlqSHMiLaAQA-5STqsjAdG3QmG3Ud1IYC-DB4NxAOfEHcDLUeQ-CwVpASpJn5OSMvDaiJ4EqjghGUKLoEgNn8pSFJ3UncxGsmJ9T3bmu_yfya9KYBG-Vqvh9hUf0eIdAwIV087mc4HGCwjdp9oc1qKug241skhyRyUv7qUKvmGYo8wEwLhU_JW72i3QP3-RMM-W--Idfvdg-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد حشمت الله فلاحت پیشه از هدف قرار گرفتن نفتکش‌ها: ثروت‌ های ملی به آتش کشیده میشود، باید به ایران سوزی پایان داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146415" target="_blank">📅 10:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=fcKWLMZ32LYsPFobZi3-wP8i4t4mpowwupwoAgBh0BWGHARw1_z-XKNw8HEvbulE3oxZPaET-wrt8CJayjyVRylCehOHWzdoJON1Rx_yfYGgr2G4doHvWtoS0fWTGHz-aDDz8QY_T9EBNOMXi_Oa4LQB9efx4KEcKtG6-47of_zvl-HtqUM1djmWaeefASXzc1mcgCIRCMW53cus-fVzT93OOb-1ctwap_mrVhz1ZmiBOD5qYE9hf_yy0UJV0aj-QJUEzS9TxSspE45XIL2CVf6X4i-hnwtatXe4bd_-ujbOQl-veKF9PPS1VpTSi3C47PuG9WsjcCUMe4joznxNqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43f6f01e8.mp4?token=fcKWLMZ32LYsPFobZi3-wP8i4t4mpowwupwoAgBh0BWGHARw1_z-XKNw8HEvbulE3oxZPaET-wrt8CJayjyVRylCehOHWzdoJON1Rx_yfYGgr2G4doHvWtoS0fWTGHz-aDDz8QY_T9EBNOMXi_Oa4LQB9efx4KEcKtG6-47of_zvl-HtqUM1djmWaeefASXzc1mcgCIRCMW53cus-fVzT93OOb-1ctwap_mrVhz1ZmiBOD5qYE9hf_yy0UJV0aj-QJUEzS9TxSspE45XIL2CVf6X4i-hnwtatXe4bd_-ujbOQl-veKF9PPS1VpTSi3C47PuG9WsjcCUMe4joznxNqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترمینال نفتی روسیه در دریای سیاه هدف قرار گرفت
🔴
پهپادهای اوکراینی دیشب به یک ترمینال نفتی در شهر «نووروسیسک» که یکی از بزرگ‌ترین بنادر روسیه در دریای سیاه است، حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146414" target="_blank">📅 10:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
اسرائیل در اعتراض به تحریمهای جدید بریتانیا علیه شهرک نشینان به کنسولگری بریتانیا در شرق اورشلیم اطلاع داده است که باید ظرف ۳۰ روز تعطیل و تخلیه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146413" target="_blank">📅 10:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDyDX8SX6aI1FiJiMK4cKxU7gNKYubhVmkFXInnRMc8ykEZ3LLQ0umhHbUOfr7JL71FGUpeUvsTy5rFwQFqFUoq5smraoZFyyd4hHJYoPdxgyVTCjwF83rPSZh2zqjvyn3luFS8CE3JSQHpcNuDVefK_FuwUdqoRdrLdaXBdo_aV_yytx2syVH9FFmCr2Vo0OFtO4CrtkRBEr8z39J0nKDRCzuaydnrKSzba8on-s-VDPZgaq8DHAV8SW1olAoMpaFnNI35TwEP1-UWWqZD15sHDc2ftfjT5W-pB8ZvfGQG7bvJL1UUGiGLmGQT04TMxC8hZpa3UXQLXNXVIgGZOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل شرکت ارتباطات زیرساخت ایران: قطعی فیبر ساعت ۰:۵۵ برطرف شد و شبکه پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146412" target="_blank">📅 09:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZkyT5TFuGHbXYou1j8IUc1lU79GxMX2PRk_Bv-YkQRWx79oeGDOKN_fXeYGoMKFvDUnJy32H6t7qRNugDAODEZIb-RPpbhkjpjk2W6vjgBwp6yOOZ7wHfKatJvDiIGXyogjdfovec1L_hLl1eZUH4edfyOh1iIYQ7Mw0kjyG8YwIIH4Thsjx71Mn2Xihdb7Ce4FgVppt1GUYileT6pOtzSesQocMqr_WYxHaHBB8J2jrqHiUKLolIaFDjZHEL8SXOKePQZkgA_aI2cX_OUjSBjLlPkABmm0N3TNqm7OLM8XZ-kM5_U9epITWVLWKKFySJ7a9Ls1dmtOEIisH086Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMadHFWF_pYGqVxyEpL2RBh_mB8il1R15CUgZVj1mz77sRrg5BWyZ86kCu6XY9JDc_fr3R0BD1nCR00vncB0SJG9z4ykdW1h8azh71CBXchNzE7X80bgZl7RPy4gQrtdsyAGbfm3vbVXqHFA7mzp0_szf-o_2XxwCI5FQK2JHsxOmtzblExNN57SIR0YhfX4iORRedZeN9g4ARNZc24-5VBLWxAes1WKAptnpLXuffDCHyNj8TS4fKdHi7ofAFtaMFLbUsz8aJ6eF1XUGRcEo_0jITXRF2KsLcF8Q6WEkXpTZ7eHeddZCilGA1MJkWHdoxzvYDkfJf1kK4dkNCEohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Txtj9xmzXB6vR3UpoIKEdgspSnCgv8DJxTFZypKolNJeMPXDLG69sZg-7GnuJsmZN7Bzv87YP0b2lD20WBOuTFuFil1_7oClK_UEdplvrcsc8wSnPSmvrJycVsH1YiocvAB4WChQOt-kbfy5rfZEvE3Y7dHzZNFV-L1ngTFZJSjrdAEMUaJnnWF2W1jYqdpPMLc1TaxACTcQhBTiT8_SKBnzXUQlx1Xkc82HmKR2oOjvbf5NjnDEfkejj8dngi5deYNWCtvbA0YZ4bH8cp0erCp1jsaFawqlOTN0wRvgMPGlVjQVo7yqQSF7XRccxbRGFgBYxuRT6KpuQ57XOtMiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آسانسور غول‌پیکر چین؛ کشتی ۳ هزار تنی را ۱۱۳ متر بالا می‌برد
🔴
سازه‌ی بالابر سد Three Gorges Dam در چین کشتی‌ها را تا ارتفاع ۱۱۳ متر جابه‌جا می‌کند.
🔴
این سیستم عظیم با وزن ۱۵٬۵۰۰ تن، زمان عبور شناورها را به ۴۰ دقیقه کاهش می‌دهد. استفاده از ۲۵۶ کابل فولادی دقت این مهندسی را به دو سانتیمتر می‌رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146409" target="_blank">📅 09:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146408">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: در واکنش به حمله به ناوهای جنگی ایالات متحده، به حملات علیه نفتکش‌های ایرانی ادامه خواهیم داد
🔴
هر بار ایران به کشتی‌های جنگی ما حمله کند، یک نفتکش را از دست خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146408" target="_blank">📅 09:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64f3accac.mp4?token=DLRgoJsRnaX5Oq48K7fwQMceCGQv9M2dmPAYOIaGndI6ZYZbA1jldy4XPzOal8RRcRqwwVaFAm9uXWEhtYAhPXrl3uHetfUL2mJFC_kB7qVSIo1VB4d4jMYLs55cLcMcKuyF2nLoL8z6yFPsXhw6BCKCpG18lM3yhD9L97_dOYnH-3xqbpxGFB3LhM7PKG3HbF2oUnO3p5ypf0NVMd4PYNQ2A2LPYnlwd-AuqlZ1L6IslbMJIDM8b2vHoCjnGYf548AKnIDnx99aSDtvh2Ji_s8i9kaz27k622zakFjem-GmeqVe0sO9OvwYueJEJcpy-saPUKeNxpfVWq5pDu7J1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64f3accac.mp4?token=DLRgoJsRnaX5Oq48K7fwQMceCGQv9M2dmPAYOIaGndI6ZYZbA1jldy4XPzOal8RRcRqwwVaFAm9uXWEhtYAhPXrl3uHetfUL2mJFC_kB7qVSIo1VB4d4jMYLs55cLcMcKuyF2nLoL8z6yFPsXhw6BCKCpG18lM3yhD9L97_dOYnH-3xqbpxGFB3LhM7PKG3HbF2oUnO3p5ypf0NVMd4PYNQ2A2LPYnlwd-AuqlZ1L6IslbMJIDM8b2vHoCjnGYf548AKnIDnx99aSDtvh2Ji_s8i9kaz27k622zakFjem-GmeqVe0sO9OvwYueJEJcpy-saPUKeNxpfVWq5pDu7J1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
34 میلیون تومان وجه رایج مملکت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146407" target="_blank">📅 09:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سپاه: ناوشکن‌های رزمی DDG-119 و DDG-53 آمریکا مورد حمله قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/146406" target="_blank">📅 09:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU9l4KgDOFqLaoYaG0chxZ2TtTwx2TAi_LV8iFp316HonfGrZktffzjjB4QxKT3wYdX06Dnq6S8NLdED9cRMZIunRAEMrhSlg6miV1N8yigsz5R4ypsepyRs8kDxLW137pkHBAPgJpcaLzww0Mb24kOlW0zAzBex44N0c-SF8kVghHPgEuJ61GrYdiG4rQYAq8tkSh7IiABG6t7x_XKrJzzVN6uSwekaISZiAHxVGI7NPBKLlazE5m2nkXE9oH0yTOXVQumAS1cDQsqIR12bUJ15I1S7JUySDiUDU7CSMQjs9lQXOVCXGX3aja8NsqcxvPgZ_46EjPw9tLjx4u2neQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: دولت ترامپ با اقدام تحت رهبری بریتانیا برای تحریم شهرک‌نشینان اسرائیلی و نهادهای دخیل در گسترش شهرک‌سازی در کرانه باختری مخالفت نکرده است.
🔴
به گفته مقام‌های آمریکایی و دیپلمات‌های غربی، اندی برنهام، نخست‌وزیر بریتانیا، پیش از اعلام این تصمیم، ترامپ را در جریان گذاشت؛ اما ترامپ مخالفتی نکرد و از لندن نخواست مسیر خود را تغییر دهد.
🔴
مقام‌های آمریکایی همچنین به بریتانیا گفته‌اند که درباره سیاست اسرائیل در کرانه باختری نگرانی‌های مشترکی دارند، هرچند با خود تحریم‌ها موافق نیستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146405" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
عبور ۶ کشتی حامل کالا از تنگه هرمز در روز سه‌شنبه
🔴
داده‌های شرکت کپلر نشان می‌دهد که روز سه‌شنبه ۶ کشتی حامل کالا از تنگه هرمز عبور کرده‌اند؛ موضوعی که نشان‌دهنده کاهش این میزان نسبت به میانگین روزهای گذشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146404" target="_blank">📅 09:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
آتش‌گرفتن یک کشتی در قطر
🔴
قطر از وقوع آتش‌سوزی در یک کشتی در بندر «الوکره» و مهار آن خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/146403" target="_blank">📅 09:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
منابع یمنی: جنگنده‌های سعودی ۳۲ حمله هوایی به استان‌های مأرب، الجوف، تعز و الحدیده انجام داده‌اند
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/146402" target="_blank">📅 09:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dee846013.mp4?token=pTkTrRXe2m27G1wsJNceVXk6ErN6bVSZKhES4TlpnEVGyzLjRIYnlKrwrq3eqUMAxYdGJsbdY18S7AkT0OzHGU8Dw4kgcxN-tubyVd92A0EUYu0jaCsBc2PjtXwJ0SK6ZEyBIT5A1VTPfUxyEBneOePYj8vwfN4-b8doBPjggaFaJNt0qP4wtF7AxP1FoK3hnPcMoXj9eLvQvY_uEksZ5UjGoXMccNz2UPMlU567kggoOJplSYFYLNT_J-mg5zGSznNr-fBQwOQaD07njen1efbOaBcQBrbAu51hEWIVz2e_WyYFC4waLB1aNl3xmPHX9u6EfVCrNW88c_tUrfCgNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dee846013.mp4?token=pTkTrRXe2m27G1wsJNceVXk6ErN6bVSZKhES4TlpnEVGyzLjRIYnlKrwrq3eqUMAxYdGJsbdY18S7AkT0OzHGU8Dw4kgcxN-tubyVd92A0EUYu0jaCsBc2PjtXwJ0SK6ZEyBIT5A1VTPfUxyEBneOePYj8vwfN4-b8doBPjggaFaJNt0qP4wtF7AxP1FoK3hnPcMoXj9eLvQvY_uEksZ5UjGoXMccNz2UPMlU567kggoOJplSYFYLNT_J-mg5zGSznNr-fBQwOQaD07njen1efbOaBcQBrbAu51hEWIVz2e_WyYFC4waLB1aNl3xmPHX9u6EfVCrNW88c_tUrfCgNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل کوثری: ستاد کل نیروهای مسلح، سپاه و ارتش از سال‌ها قبل برای ایجاد آمادگی لازم، برنامه‌ریزی‌های دقیق و بلندمدتی انجام داده بودند تا در شرایط حساس بتوانند پاسخ مناسبی به تهدیدات بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/146401" target="_blank">📅 08:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146400">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سی‌ان‌ان: عربستان در تلاش است تا کشورهای دیگر را علیه یمن وارد جنگ کند
🔴
پادشاهی سعودی پس از حمله بزرگ ارتش یمن به خاک این کشور در حال برنامه‌ریزی برای پاسخ به آنها در یمن است و متحدان خود را از برنامه‌های خود مطلع کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/146400" target="_blank">📅 08:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bede8db302.mp4?token=b8cAMvW54lg5V3YD0YqBaXg5_P4tB9GUqwJh2QQhO1WgH6OuEiExNchqnuQN9_jgoB7yd1BqIlKYk7ztl1LDt6grghsYGd1wo_BhftFtjVW7XoLH8TJq2MUHvfT8oDhvzyaX5tHeDszbkycSuXNoeTgE06GQ7JAa9kiogsTXAZmIl41DUg-EcDE3ndjrcsGjiHjNXUqIOR73mz4Rg5sLX5babF4uvvsRU-SEnGBMvL5Syvt0wN0FphTbkR_Z49oKAI8Byv73n_0pIuPd-nzu8EaZAYlkE79adHezQrQxTjxTBP7qV5p3z0gxu3BSkBg3efoSYM2LJxwC1vM9KuBaSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bede8db302.mp4?token=b8cAMvW54lg5V3YD0YqBaXg5_P4tB9GUqwJh2QQhO1WgH6OuEiExNchqnuQN9_jgoB7yd1BqIlKYk7ztl1LDt6grghsYGd1wo_BhftFtjVW7XoLH8TJq2MUHvfT8oDhvzyaX5tHeDszbkycSuXNoeTgE06GQ7JAa9kiogsTXAZmIl41DUg-EcDE3ndjrcsGjiHjNXUqIOR73mz4Rg5sLX5babF4uvvsRU-SEnGBMvL5Syvt0wN0FphTbkR_Z49oKAI8Byv73n_0pIuPd-nzu8EaZAYlkE79adHezQrQxTjxTBP7qV5p3z0gxu3BSkBg3efoSYM2LJxwC1vM9KuBaSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه شلیک بیش از 100 موشک پاتریوت، سیستم دفاع هوایی آمریکایی، در اردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/146399" target="_blank">📅 08:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وال استریت ژورنال: حملات اخیر ایران علیه تجهیزات نیروی دریایی آمریکا نگران‌کننده است
🔴
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/146398" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146397">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6c355c1f2.mp4?token=u8Cd_8rKrdXw1xifDDdPj-oUj-GrLmrjV6FSMbTouR2QIq1XFMDl2Ekeza0ePkZzvvpOclscOQiZafGKyu0vQ1xXox-89nSCdzHMTCAia16ozv-fUlWQijv98KV3xK_a0cYCTPL9b-yiFbusunOapHhwaYhHJeMGhspD2h66Odd4lseanGfJKueOVv8WBdMowF3mon6ZXNFyQV5I9lWvseYjothxoizAXb3odmaVJwfvhNHOOdsWXUuOdQy8EprtGqdL6hIq4RlZJ13jUij9fclgJTl8Sxs3AEvJN_xDnInSNSDieoMxlAnLkaGpHk09brFPfJkdCw9sb_EcwR0S3p971SYmgz08YvwKDXEF3JL8HrDN96A23DvEC0uebeoI6Jt_r6_GxVn78c6zyZhmAAc5MUlOC-DXEdbLL8sy7q9XyrNJhpO9aF2jjZLm1tXcVGPtDg9A4-EfJm2WOPjIECfda2Q3CCcCw6D6KN7MbiAgJakvUZx5W1wfI8BLijUuCixZxK7rbnF0nfwhiRNQ2E9SAcsFLkFJs396fnAnfQKsWQ3vFOmVr9cSj4EN99sJPQSoQPiIaA4K3r0sDgy0jJ28Zs-nJRsWMQwzFg6-M0HvejTL2zgTHSWwJy-RWW20mK2T6AUz6QoUl81uPkXOGU-BiJ20j8sPrRe0VtF2bLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6c355c1f2.mp4?token=u8Cd_8rKrdXw1xifDDdPj-oUj-GrLmrjV6FSMbTouR2QIq1XFMDl2Ekeza0ePkZzvvpOclscOQiZafGKyu0vQ1xXox-89nSCdzHMTCAia16ozv-fUlWQijv98KV3xK_a0cYCTPL9b-yiFbusunOapHhwaYhHJeMGhspD2h66Odd4lseanGfJKueOVv8WBdMowF3mon6ZXNFyQV5I9lWvseYjothxoizAXb3odmaVJwfvhNHOOdsWXUuOdQy8EprtGqdL6hIq4RlZJ13jUij9fclgJTl8Sxs3AEvJN_xDnInSNSDieoMxlAnLkaGpHk09brFPfJkdCw9sb_EcwR0S3p971SYmgz08YvwKDXEF3JL8HrDN96A23DvEC0uebeoI6Jt_r6_GxVn78c6zyZhmAAc5MUlOC-DXEdbLL8sy7q9XyrNJhpO9aF2jjZLm1tXcVGPtDg9A4-EfJm2WOPjIECfda2Q3CCcCw6D6KN7MbiAgJakvUZx5W1wfI8BLijUuCixZxK7rbnF0nfwhiRNQ2E9SAcsFLkFJs396fnAnfQKsWQ3vFOmVr9cSj4EN99sJPQSoQPiIaA4K3r0sDgy0jJ28Zs-nJRsWMQwzFg6-M0HvejTL2zgTHSWwJy-RWW20mK2T6AUz6QoUl81uPkXOGU-BiJ20j8sPrRe0VtF2bLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی اردنی‌ها از دیدن موشک‌های
سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/146397" target="_blank">📅 08:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146396">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
👈
سپاه: بامداد امروز آشیانه تعمیر و آماده‌سازی و محل استقرار جنگنده‌های f-15، f-35 و f-16 آمریکایی هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/146396" target="_blank">📅 07:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146395">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
هم اکنون وضعیت آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/146395" target="_blank">📅 07:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/146394" target="_blank">📅 02:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146393">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4468d01fd4.mp4?token=KSuSqW9aMXi0HgbJJzecm-5oxsMC92Yb4NWvqsmPiDyP3lpPE6Fbg0e2XhWNqbWoK__ylmxVPfzpsX68Mn1UJKOMRxc1lR1FtEAvhwRsPc_fDEVIcjmxNf43IIBxo2KU0kNYsSnx-y-RzWPHNGJNX9z5t9RMHEG_gGyn3wDN4gOI76Iitg0cdvHH6FtIUViv9eDzo8jMiKO4-9AW1XEPiFSGIkYsNmL6Pxt9w1MwWWwTlKutS_lkdogFPc-EWjlBvc9o_NMe37tWj3mIlJAZAjgbBIqIJK_Icw4pw8VtgmtFRC3T7tiCCtus5zHkW6LZSfky5rGKHH47zkeq6xrLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4468d01fd4.mp4?token=KSuSqW9aMXi0HgbJJzecm-5oxsMC92Yb4NWvqsmPiDyP3lpPE6Fbg0e2XhWNqbWoK__ylmxVPfzpsX68Mn1UJKOMRxc1lR1FtEAvhwRsPc_fDEVIcjmxNf43IIBxo2KU0kNYsSnx-y-RzWPHNGJNX9z5t9RMHEG_gGyn3wDN4gOI76Iitg0cdvHH6FtIUViv9eDzo8jMiKO4-9AW1XEPiFSGIkYsNmL6Pxt9w1MwWWwTlKutS_lkdogFPc-EWjlBvc9o_NMe37tWj3mIlJAZAjgbBIqIJK_Icw4pw8VtgmtFRC3T7tiCCtus5zHkW6LZSfky5rGKHH47zkeq6xrLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه ویدیو حملات به اردن رو منتشر کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/146393" target="_blank">📅 02:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146392">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
‌سازمان دریایی بریتانیا: ما گزارشی درباره یک حادثه از یک کشتی تجاری در تنگه هرمز دریافت کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/146392" target="_blank">📅 02:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146391">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
آیدیش:
@khabar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/146391" target="_blank">📅 02:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146390">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: ایران از این نفتکش ها به عنوان بخشی از یک شبکه مخفی چند میلیارد دلاری برای تامین مالی سپاه پاسداران و عوامل ایرانی در منطقه استفاده می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/146390" target="_blank">📅 01:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ویدیویی که سنتکام از حمله به نفتکش ها منتشر کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/146389" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: پس از اینکه سپاه پاسداران انقلاب اسلامی ظرف دو روز دو بار یک کشتی جنگی آمریکایی را با موشک‌های بالستیک هدف قرار داد، 5 نفتکش ایرانی را منهدم کردیم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/146388" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146386">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c99f81fed2.mp4?token=N6x7bjg7nBvfNp3QdloHSVqRT_IXbFZh5kiG4mUAHls5sv_jlL2ud7HV27Ty7bBArdUKHj6u72cxxNCFAVP4mi7u5wU17qE2fD0WhFg-nBaULn4N78_5NU5OOf1pak_St3C17naDZ9P4om9oE483uikU9SsyDs-cyjM6ubUyFVVBx1ITyNn9bx260RlUkZL4Wji_Pv0virUi5H4Couel0OirpeD9VvbOHEk4oSdsZDA_CJY9rWW1-13_6is_06W06Gz7I0cmFtRBB7K10x3jI8ikH-r0DryDkj-qwT639QV7c64tEUNn6iafwcOC_P1e_tT412t59cEmNZo7P1xgbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c99f81fed2.mp4?token=N6x7bjg7nBvfNp3QdloHSVqRT_IXbFZh5kiG4mUAHls5sv_jlL2ud7HV27Ty7bBArdUKHj6u72cxxNCFAVP4mi7u5wU17qE2fD0WhFg-nBaULn4N78_5NU5OOf1pak_St3C17naDZ9P4om9oE483uikU9SsyDs-cyjM6ubUyFVVBx1ITyNn9bx260RlUkZL4Wji_Pv0virUi5H4Couel0OirpeD9VvbOHEk4oSdsZDA_CJY9rWW1-13_6is_06W06Gz7I0cmFtRBB7K10x3jI8ikH-r0DryDkj-qwT639QV7c64tEUNn6iafwcOC_P1e_tT412t59cEmNZo7P1xgbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از شلیک موشک‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/146386" target="_blank">📅 01:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146385">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
منابع ایتایی: در پی حملات ایران به اردن حدود ۵۰۰سرباز آمریکایی کشته و زخمی شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/146385" target="_blank">📅 01:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146384">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یه موشک هم رفته تو سوریه که رهگیری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/146384" target="_blank">📅 01:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146383">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گویا یه موشک هم رفته خورده بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/146383" target="_blank">📅 01:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش‌های اولیه حاکی از آن است که یک نفتکش ایرانی دیگر با نام «DERYA» هدف حمله نیروهای آمریکایی قرار گرفته است.
🔴
این گزارش‌ها به‌تازگی منتشر شده‌اند و هنوز مشخص نیست این حمله پیش از آغاز حمله تلافی‌جویانه ایران انجام شده یا پس از آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/146382" target="_blank">📅 01:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هرکی موافقه به اسرائیل حمله بشه و انتقام‌گرفته بشه لایک کنه
😂</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/146381" target="_blank">📅 01:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فووووووووری</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/146380" target="_blank">📅 01:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فووووووووری</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/146379" target="_blank">📅 01:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هم اکنون وضعیت آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/146378" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری/پایگاه‌های هوایی «موفق السلطی» در منطقه الازرق و «شاهزاده حسن» اهداف حملات موشکی ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/146377" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/سپاه با موشک خوشه‌ای حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/146376" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFin4SLNJG-LxQVL43nv-AZYLSuy4P-TdXWwI0hOE_GkE5fksyQIpXzOuoOTYxnX4CPv7qzQVuEn_laVgH7EWVR6LLx1NQ10S1d45ak2y1xNTKLMnP9aA6N5qlw8l1JXyzs1MLRguvEzCbKaKc9yapRnb5D9vgcGKak_9OOBww8mA-sG0HK-iU-KuRIddDlWO-ljChES6Y8YlwgQaScNWKcW6BkcGGJoauI-VmAjEIfswYSrWtrR3GngH_09xNXfNM0O6VV-SOjB6o4yD53cn4kjxa_DZQnS4Y8h_zncyQ2b_gEZ1Kihvh2bM0PF5NoC0ggR8he3LxHB7JSRBAi5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هم اکنون آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/146375" target="_blank">📅 01:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146374">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سپاه گفته خدمه‌های نفت‌کش‌هایی که تو اسکله های بحرین و کویت هستن تخلیه کنن؛ چون ما میزنیم
‼️
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/146374" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/حدود 15موشک شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/146372" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146371">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/حملات به اردن هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/146371" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146370">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/از ۱۲شهر ایران موشک شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/146370" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146369">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/شلیک موشک از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/146369" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
