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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 359K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 02:17:25</div>
<hr>

<div class="tg-post" id="msg-17231">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/withyashar/17231" target="_blank">📅 02:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17230">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وال‌استریت ژورنال: اسرائیل اخیراً اطلاعات جدیدی را با ایالات متحده به اشتراک گذاشت که به گفته این کشور، نشان‌دهنده یک طرح جدید سپاه برای ترور رئیس‌جمهور ترامپ است.
ترامپ روز چهارشنبه، در سخنرانی خود در اجلاس ناتو در آنکارا، ترکیه، به تهدیدهای ایران علیه جان خود اشاره کرد و گفت: «آنها می‌خواهند رهبر آمریکا—من—را از بین ببرند... من در تمام لیست‌های آنها هستم.
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/17230" target="_blank">📅 01:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17229">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حکومت رمال ها  ، بت لگویی ترامپ را آتش زد !
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/17229" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17228">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">باقیمانده خامنه ای دفن شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/17228" target="_blank">📅 01:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17227">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnOzVf5fzuxkEreKA2Kd98JkxclDCulnCWApFu6_44oG-MbmnRHBW8KgpfyzrPv51G-lnAgB8I4B3O_vOkJQeEFq-uzeVK2EAZHBA3XU0gepPOm2XisRruZQmLLehQSnsR12uG_SwEzLvef2FrAEKN0_y_LXnFW3K46WQH25xuM1_Ps3-ewyKwhaxf6utbx3wdzK21Bcm1wAzFy7aI699xUMi0id_yS9AjaPdX5ijW7WBny_K26Vu5Ji9rIftsclQJ4gCpbo6aMqRiR21QQUMz0ga2nJkj8krY3FsUf0U2TYefiq1CfXb8lCp5UvYcgK86IezG-asD4kknQVw-qqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب اتاق جنگ
⚠️
این عکس هم هوش مصنوعی است !
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/17227" target="_blank">📅 01:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17226">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حقیقت یاب اتاق جنگ
⚠️
این عکس هوش مصنوعی است !
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/17226" target="_blank">📅 01:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بیانیه جدید سنتکام:
ادعا: رسانه‌های دولتی ایران مدعی هستند که عبور و مرور از تنگه هرمز فقط از مسیرهایی مجاز است که ایران تعیین کرده است.
واقعیت: ایران کنترل تنگه هرمز را در اختیار ندارد. از اوایل ماه مه، نیروهای ایالات متحده به عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از این گذرگاه حیاتی تجارت بین‌المللی کمک کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/17224" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17223">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EaISfVcBgH8L0T5Etxe3rTDt-2EnxTD_468amIid34wfWES2af5A2t0BB3LVzqgTHmXr_R3ik8sf_0IRA1D91VVtGcpDcMYhDPOV5oyqMAvWaTcisSsIKTxx9RSIqK91FWNssDIHwC_oFASyi9ZNCjC6B4rrPCiprkyBNEmjYxi0O_FOCm6FWcSp6L9APfYjBBqO7UaDIneZOrX1mCbozDWWHxMz7-k39r2EvsQ4H-BFYmEuFsKhx941Ffv0E_X1FMxqm-2l5PyBnUp64ypVg4r9PHHcgbA3Lyi_7hlRvTqSmDGTqiEnxh5wFxm7s_JnfTKrNeyoYd9UTNqjQNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای آواکس به همراه ۱۰ سوخترسان  ، فقط نشونه اینه که منتظر تایید نهایی هستند… یک جرقه
💥
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/17223" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17222">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اومدن گلگی کنم گیفت و استار نمیاد دیدم نه بعضی ها هستن که روحیه بدم بهم هنوز
🙌🏾
دمتون گرم حواسم هست بهتون روز آزادی پیغام میدم تک تکتون جمع میشیم
😭
❤️‍🩹
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/17222" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17221">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شرحه واقعه از یک شاهد بیار‌ عرزشی :
شهیدان علوی و هنرور به ضارب مشکوک میشوند که او هم با لباس بسیجی بوده و قصد انجام یک ترور را داشته است، بعد از نزدیک شدن به تروریست دست به اسلحه می‌برد و به سمت شهدا شلیک می‌کند و به سرعت از محل متواری میشود
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/17221" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به گزارش رسانه های‌ رژیم:
بر اساس اطلاعات، دو فرد ناشناس با لباس نظامی‌و با استفاده از اسلحه کمری، شماری از بسیجیان را مورد هدف قرار دادند که طی این اقدام، یکی از بسیجیان در صحنه و دیگری در بیمارستان به هلاکت رسید
ضاربین متواری هستند تلاش نیروهای امنیتی برای شناسایی و دستگیری عوامل این اقدام ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17219" target="_blank">📅 00:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارشها ۸-۱۰ نفر در‌ تیر اندازی های مشهد کشته شدند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17218" target="_blank">📅 00:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17216" target="_blank">📅 00:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیدبان اتاق جنگ : من دور حرمم نیرو های بسیج و سپاهی دارن خیابونارو ول میکنن میرن با موتور سرعتشونم زیاده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17215" target="_blank">📅 00:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مشهد - ایست‌بازرسی منطقه سرفرازان  توسط افراد ناشناس به رگبار بسته شد
یک درگیری مسلحانه در اطراف حرم امام رضا.... و دومی افرادی که امشب به ایست بازرسی مشهد حمله کردن لباس نظامی به تن داشتند و بعد از زدن نیروهای امنیتی فرار کردن.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17214" target="_blank">📅 00:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlP1ZugjZkpbQYxOKpgrPaurEvG4n6Stzmem0wVIXEZaXIk9vP_HEPepYJ4aCOrn8JXqTNSLBGDBYmp3bbRNGQ5ncQkYahihTt2-M2CIV8qeqyO7YttjpoxCv2qBg6FWFO_X1yuzIdOCwQwnzyhCbJBHzdostCBI101D2PvzQ4GzkoTwfgJctZExwPmp-jOmEt4QCGAzk_uMNigpuheDxC8qZkFFMmPCMyIFEP3boB_BajIuxyRuL7a3k5qIVTEdaBBvp_kvsIhbGy7JYgyPr1a5Z7GR644C0GaX6mhzCE5jKMLVHLnHik0w0YLtuYFKYiOkcdp-Ad3vH8belQsqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17213" target="_blank">📅 00:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF-aiD3qdxjzNS0GdY6iU2KwCjsM0AAueM3Enex4Qvbxg9HIZ5--2UW3sdehCivbHw41Ah3mVGLtS74q4DWQ5UKDCRfwdOEJLs_aIylxKjtKDugQLRpgtu28oWDFnRpYrXfQZlDbwqn9PVqVIA9GBIecUSOnCJpoG1Tl0vmZCXw7eHOrpmQeI5nyYBreY0Lt6TrGUUnf2mKvEFhjCgny_Uj1UPNpTyGU2q6n-8wUmICTddVxYMocBEeZbcD7bczcxuU0lTLkKbQj3T8mV4j-vEpqUr-Z7jpflCxDAZ6X55zRSVWS69AVweJH11WtOqtPP9nzlGuXtH9tQJrMIfOM4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری در ‌مشهد از حجازی از چهره های مخوف علی خامنه ای در کنار ممباقر ، بیگلی بیگلی هم او پشته
@withyashar
🤣</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17212" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارشاتی از حمله به یک ایست بازرسی در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17211" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسانه های عربی: یک فرد مسلح به سمت اعضای سپاه پاسداران آتش گشود.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17210" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آی۲۴ عبری:  عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند -خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17209" target="_blank">📅 00:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر عمور خارجه ترکیه
فیدان: با آقای عراقچی صحبت کردم و ایشان نیز با من موافق بودند که آتش‌بس هنوز به پایان نرسیده است
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17208" target="_blank">📅 00:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSadeq</strong></div>
<div class="tg-text">پهپاد هم داره میچرخه توی آسمون
مشهد</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17207" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17206">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommaryam</strong></div>
<div class="tg-text">از وکیل اباد هم شنیده شد</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17206" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17205">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐦𝐢𝐫𝐬𝐚𝐥𝐚𝐫</strong></div>
<div class="tg-text">یاشار منم مشهدم، صدای تیراندازی از سمت میدون پارک‌ملت میومد</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17205" target="_blank">📅 00:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17204">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش تایید نشده ((تیر اندازی در مشهد))
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17204" target="_blank">📅 23:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17203">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرماندار شهر کنارک : یک پایگاه نظامی متعلق به نیروی دریایی، در دو مرحله مورد حملات هوایی دشمن قرار گرفت. @withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17203" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17202">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb4117500.mp4?token=tKEJz-y-g4_LUt3fsG-zM-zpXhkyDPEnr0y0ZNDYNVECRbmOmnhrvgLpTqWatzC0IWby8Dh-Y82zK5b29kTLNCAIlA_pPVBLNxKTUHtGWvZjXZSM3YvP0W0wnuW73KonQbiGzBkRWxxG3MMnJWecLI6V9HWfXUdKo4WFP4K9SkhQDhBH_7rK-sBnxifA9mPoNYMNIyzFgU6n4Esb26Qzl6i_ekFzwhKBUuh3Pe2KgnBOKeXIcG36SoisTnXIPPl7m8KtsbYhFNE0uXAUElL0csPJEBupstCmJziMfSx8fSMJ70JKbBUHfX7tvDcV_RFrzlz_LcDVV5eRpgRypwNtmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb4117500.mp4?token=tKEJz-y-g4_LUt3fsG-zM-zpXhkyDPEnr0y0ZNDYNVECRbmOmnhrvgLpTqWatzC0IWby8Dh-Y82zK5b29kTLNCAIlA_pPVBLNxKTUHtGWvZjXZSM3YvP0W0wnuW73KonQbiGzBkRWxxG3MMnJWecLI6V9HWfXUdKo4WFP4K9SkhQDhBH_7rK-sBnxifA9mPoNYMNIyzFgU6n4Esb26Qzl6i_ekFzwhKBUuh3Pe2KgnBOKeXIcG36SoisTnXIPPl7m8KtsbYhFNE0uXAUElL0csPJEBupstCmJziMfSx8fSMJ70JKbBUHfX7tvDcV_RFrzlz_LcDVV5eRpgRypwNtmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مراسم تشییع جنازه امشب یکی داشت علیه مذاکره کننده ها شعار میداد که یهو یک نفر که احتمال زیاد نیرو امنیتی بود ، جلوی دهن طرف گرفت
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17202" target="_blank">📅 23:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17201">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرماندار شهر کنارک : یک پایگاه نظامی متعلق به نیروی دریایی، در دو مرحله مورد حملات هوایی دشمن قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17201" target="_blank">📅 23:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17200">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل : نتانیاهو و ترامپ گفتگو کردند ، رئیس‌جمهور آمریکا از تحولات آمریکا در خلیج فارس اطلاع داد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17200" target="_blank">📅 23:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17199">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ به اتاق جنگ گفت به عشق ماکرون و عینک قشنگش امشب اول فوتبال رو میبینیم و بعد خواهیم دید چه خواهد شد ، کلی اسپانسر داره جام جهانی پول دادن پول متوجه هستی ؟!صداشون در میاد ، ممد چی چی هم سر معدن داره مته میزنه بگو ول کنه بازی رو ببینه
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17199" target="_blank">📅 23:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17198">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه عراقی تندرو شیعه : از دوستان خبرگزاری تسنیم خواهش می‌کنیم ما رو دنبال کنن و برای انتشار خبرها عجله نکنن. همون‌طور که قبلاً هم گفتیم، این حمله از خاک کویت انجام شده و با
پشتیبانی اطلاعاتی پایگاه آمریکایی الظهران در عربستان صورت گرفته.
@withyashar
یاشار : تسنیم رو دیس کرده و
ولی هر چی‌گفته آخرش رسیده به حرف‌ من
😂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17198" target="_blank">📅 23:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17197">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfsTz8xNR9tWMBxepsX6K16halkBisuD9FsJjx-t0A1aettmKs6Rr07leUvmQHkC-sMNqjjKGXT1Kj1h9x1Wmwlbp5tKt0Fnv941ZTjMULSLmAUTsQDx31Avv2XY1Od7jeZrg-izlAH4LYReGuwaUKftOFX7zniThjARayvEGCr7RAfJNV72copdwr0mpLTcbWtIF-yUgOE0_gLrAION6WB0b4RBoaoggx2Xgc1OtDGPGgMqakmE7wUXnXU5YhUKIiyNhKE1KYekLcdtcWqoopGgIyyNyEx-4IQblvw0PE-MkbdEEor18tNK1_pN7efati631M5KSzWVvcNQlt2hlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رؤیت اتش سوزی در بندر عسلویه توسط ماهواره
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17197" target="_blank">📅 23:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17196">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjgQZqfw1n0gkBi7t7z0VpULtcV1poxP72cihfaq4adDH0OQOL76baKqw0i8btAkT0MUvJBtNryrJRC_sd6DsymanN1WIk7InqqWHrWX9VEqPPPlQL_g-FHHDZVyE-cqV0N5mOvhhDnoJcMsye-TpjiftUpx7MDiXZDr2pFh6CacH2unu5pscRd9g9jygXcDm8tyeFV0zXLGukcE-u_ssXuFDfkdb5RA6NZiEt4ddusMrEP9ZxmlLRL5RViA5jKgqeAyBnUnRf066kuDJdqu9cSzVhhnhBiMj1c63K_gzRYhHb-ssmarJmxucB7NOZHVVISqaK7Tar4YF4Z06VNKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیروز کریمی رفت جم تیوی
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17196" target="_blank">📅 23:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17195">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24e89d01f.mp4?token=ITV5KWmKb-eVElFUvHAUDgZou1zP06OJ7eCgRwJ1_Ehej9804FcadAEcuM8IYuPHEBicOOewlz0RG7jrdGrn0WwJTkdJiSPuiqNVkn2GeVRZXZ_qG9280CTcgxtxpbmOYdYXPWycLDjIfwX1kfkIuMcGk7VQXjRAZvYXVDSGBGbsP3Y_e5D1A2wRwdmq91CMzipA1j_2R6TNnevXerCUpfsdn-OseExcslw6wH-MqPG-85Jc2LiGgOWgqovhSvM-Jqge8LluQ1f4xAHgvy0YoN8cwmWQ3UEaXZEFpoSZaobC-jj-GhQ6-ARQaObtyAayHxUnECFtXZyXoawmHmWO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24e89d01f.mp4?token=ITV5KWmKb-eVElFUvHAUDgZou1zP06OJ7eCgRwJ1_Ehej9804FcadAEcuM8IYuPHEBicOOewlz0RG7jrdGrn0WwJTkdJiSPuiqNVkn2GeVRZXZ_qG9280CTcgxtxpbmOYdYXPWycLDjIfwX1kfkIuMcGk7VQXjRAZvYXVDSGBGbsP3Y_e5D1A2wRwdmq91CMzipA1j_2R6TNnevXerCUpfsdn-OseExcslw6wH-MqPG-85Jc2LiGgOWgqovhSvM-Jqge8LluQ1f4xAHgvy0YoN8cwmWQ3UEaXZEFpoSZaobC-jj-GhQ6-ARQaObtyAayHxUnECFtXZyXoawmHmWO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چغادک بوشهر بعد از حمله
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17195" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17194">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش کانال ۱۴:
سپاه پاسداران استراتژی خود را در برابر ترامپ تغییر
داده و با تشدید تنش‌ها در تنگه هرمز، گارد انقلابی از رویارویی نظامی به یک کمپین رسانه‌ای علیه ترامپ و افکار عمومی آمریکایی در آستانه انتخابات میانی روی آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17194" target="_blank">📅 23:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17193">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار بوشهر:
صدای انفجار شنیده شده لحظاتی پیش در شهر بوشهر متاثر از واکنش به موقع پدافند هوایی است.
واکنش به موقع پدافند هوایی مانع از اقدام عملی تجاوز هوایی پهپادهای آمریکا شد.
همچنین لحظاتی قبل یک مقر نظامی‌در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه  آمریکایی- اسرائیلی قرار گرفت.
تاکنون گزارشی از تلفات انسانی متاثر از این اقدام دشمن دریافت نشده است‌
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17193" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17192">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری شین اسرائیل :
ترور هدفمندی که در اهواز رخ داد، علیرضا خدادادی، مشاور قراردادهای استانی سپاه ولی‌عصر در اهواز بود.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17192" target="_blank">📅 22:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17191">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۱ عبری: کشورهای خلیج فارس (احتمالاً کویت و بحرین) یک عملیات مشترک نظامی محدود علیه ایران انجام داده‌اند.
بر اساس گزارش‌های شاهدان عینی، پرتاب موشک از خاک کویت مشاهده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17191" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17190">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صداوسیما
: امشب به بندرعباس، قشم، سیریک و جاسک حمله نشده و ما تکذیب میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17190" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17189">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sggZ3EkOzzY5dt07Rq_gHAqh7e3qLI6HP1Mq6VgTgga1YwtqRFyZkCMrsKltfMHcxLJZPgZZgix1qIptxNgYdfE6oh_rVY60T_EsAEGD2ITLCPcp_vwMoW-J3rnsweVRE4SQlTXM2ggFRBSJ_9v_g47QRZWdfrgIXfNz-KB_xTFjAEoxIsoH5jy4ToIqp2mTCikukSCbJhESTIkiRqvy51JnHabUUU87uMzR-RWXQmzGvc6dLqp4viCIpbYY-NgZwcuhjRcrSYQ3SvFc7Mv1TD1rRhTssiK1_J_g60VZU-oJ955UKaA6Xcx3KrguXvqcZwa682D36OqHKsPXPP31Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه ایران، عراقچی، تهران را به مقصد نامعلومی ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17189" target="_blank">📅 22:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تحلیلگران رژیم
: احتمالا حملات امشب کار کویت و بحرین است
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17188" target="_blank">📅 22:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17187">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">العربیه: ارتش ایالات متحده مسئول حملات اخیر در ایران نیست
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17187" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتاق جنگ با یاشار : میپرسین بگم که ، نظر من اینه که هر کی هم بزنه بدون همکاری اطلعاتی و زیرساخت جنگی امریکا و اسرائیل و کسب اجازه امکان نداره بزنه… پس در نتیجه چه سوألیه
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17186" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کارشناسان تلگرام : گویا حملات از سمت کویت بوده
@withyashar
😁
🤒</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17185" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d6bd72f1.mp4?token=Ib6o9t3DginCevxYp3wJoDGgaaMeKec3faVgSEasp9lLMSCyZGT7GMdQ00ATpYTnSJAdBckvwOt0OZ5ysi4cYjNzBHchdCcnxL0GflpS7hVl4w0pYpky7eR1s5HQ38KCSO5EdA_navGCC-AcgB_YHiSKOxhCG_2zeKAXrJ5LXS3lqXNP4hMMGFxqxOHfT53_epG6KCrGoF9RdHj2qQ4u0MRkWLQPO91MlElcMGPSXGXsB-mWwS98o6xqnBZeZ0ALtr0UfgS-rHQMH-NCMKupco90b0h1GP5p_iv2z9TI9lVmTppO1QvqIiM3pJIML1Z0eSC2q6y8oWBnDNaySfIX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d6bd72f1.mp4?token=Ib6o9t3DginCevxYp3wJoDGgaaMeKec3faVgSEasp9lLMSCyZGT7GMdQ00ATpYTnSJAdBckvwOt0OZ5ysi4cYjNzBHchdCcnxL0GflpS7hVl4w0pYpky7eR1s5HQ38KCSO5EdA_navGCC-AcgB_YHiSKOxhCG_2zeKAXrJ5LXS3lqXNP4hMMGFxqxOHfT53_epG6KCrGoF9RdHj2qQ4u0MRkWLQPO91MlElcMGPSXGXsB-mWwS98o6xqnBZeZ0ALtr0UfgS-rHQMH-NCMKupco90b0h1GP5p_iv2z9TI9lVmTppO1QvqIiM3pJIML1Z0eSC2q6y8oWBnDNaySfIX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده لگو غول‌آسای ترامپ در مشهد/ هنوز مشخص نیست این مجسمه با چه هدفی ساخته شده است
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17184" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اکسیوس: یک مقام ارشد آمریکایی ادعا کرده است که ارتش ایالات متحده در ساعات اخیر حمله‌ای را در ایران انجام نداده است!
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17183" target="_blank">📅 22:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17182">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آتش‌نشانی اهواز : انفجار ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز است @withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17182" target="_blank">📅 22:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17181">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در‌کیش‌فقط صدای جنگنده شنیده میشود ولی هیچ خبری‌ نیست</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17181" target="_blank">📅 22:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17180">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من هیچ گزارشی از قشم ، کیش و ابوموسی ندارم. نمی‌دونم چرا همه جا دارن این خبر رو میزنن. حتما اشتباهه.</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17180" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار ‌جدید بندر عباس @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17179" target="_blank">📅 22:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17178">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدای انفجار‌ جدید اهواززز
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17178" target="_blank">📅 22:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17177">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شنیده شدن صدای ۲ انفجار در بوشهر و چغادک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17177" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17176">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش انفجار ‌جدید بندر عباس
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17176" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17175">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHTxA6co9uk_zry5mTVcetGfNf0BGO2g54RjBx8ZPLlymtV_ywlUAstAIxtqoJ8QOhMkQwLVN99G1TJwEPcQt1PJUeehNXhoKcskjGGiQ4qL6HiFdUGWFmhQTcrZIkOOUxF35vcPA__FYjPNBHdB6M3ixefmOa5qYngA8pGmDDXJZI1iEBm0k2Cb_lAL6-nk2xxl6i7imcoD0KgH2y0vqZdwpk34AvuU50qnIisF92XGHnCTeAwJW6qPfXabg1EoMpFe5KXl2Rwheg-1MsIWG3ctONwabVpIOAhwQGvvFyN6xbA7At_N50LmA24BZHkquZOpF5CdWRcD6JFAGK7BIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر بزرگه داره نماز میت رو اقامه میکنه
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17175" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17174">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش انفجار‌ در اسکله چابهار
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17174" target="_blank">📅 21:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17173">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مهر : شنیده شدن سه انفجار در کنارک
دقایق قبل سه انفجار  در کنارک شنیده شد.
از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17173" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17172">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM M</strong></div>
<div class="tg-text">یاشار من بچه اهوازم ، اونجایی که خبر دادی زده ( حصیر آباد ) دو سه تا دکل مخابراتی هست که روی کوهه ، احتمالا اونارو زده</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17172" target="_blank">📅 21:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17171">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آتش‌نشانی اهواز : انفجار ناشی از نشت گاز شهری در یک ساختمان مسکونی دوطبقه در منطقه حصیرآباد اهواز است
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17171" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17170">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اهواز ارسالی :ماشین اتشنشانی و آمبولانس زیاد داره توی شهر میره به یک سمت ولی نمیدونم کجا میرن
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17170" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17169">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش تایید نشده انفجار در اهواز
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17169" target="_blank">📅 21:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17168">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28fdd7b746.mp4?token=gC7nM-8k_ajSQ9BHOdOa8Kz38fVQFGRcs3p4fwGVDQlqZAiaefnDBVsjZxIvtNWeSdkbUO5fluQHGS7JXTeWkNGplEpB-hpcszXW1tWTRJtjNpw2wSy5oLucl4Uy85IuS7aTvAjIDRCyH2R4sK_dY3GLJ0fvD8tzpchLiKErXQ87q7p0y10T5eO9gafSYsePqtfhlLTkk5ioO6n6Xgrt0re7Vlbxe719GsxFONST1Vgc0D0E66MIIeS7f5Xbd1HAczw7zHuJzmO4O0O7EbkKLhZy6vXUu7SYz_1AzGyVx9AnCCFJFBf1q8t2jP_3k30MXQE-_ZgpRD3eyay3T4dQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28fdd7b746.mp4?token=gC7nM-8k_ajSQ9BHOdOa8Kz38fVQFGRcs3p4fwGVDQlqZAiaefnDBVsjZxIvtNWeSdkbUO5fluQHGS7JXTeWkNGplEpB-hpcszXW1tWTRJtjNpw2wSy5oLucl4Uy85IuS7aTvAjIDRCyH2R4sK_dY3GLJ0fvD8tzpchLiKErXQ87q7p0y10T5eO9gafSYsePqtfhlLTkk5ioO6n6Xgrt0re7Vlbxe719GsxFONST1Vgc0D0E66MIIeS7f5Xbd1HAczw7zHuJzmO4O0O7EbkKLhZy6vXUu7SYz_1AzGyVx9AnCCFJFBf1q8t2jP_3k30MXQE-_ZgpRD3eyay3T4dQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشیاء ناشناسی در آسمان جنوب عراق مشاهده شدند که به سمت ایران در حرکت هستند، اما ماهیت آنها و اینکه آیا موشک بودند یا پهپاد یا دیگر، هنوز تأیید نمیتوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17168" target="_blank">📅 21:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17167">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فعالیت پدافند  چابهار
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/17167" target="_blank">📅 21:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17166">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from♱ ᴀᴍɪʀ︎ ♱</strong></div>
<div class="tg-text">آ‌واکس
❌
یاشار
✅</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17166" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17165">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تو نوار ساحلی میرم میام هرچی نفر اول بگم</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/17165" target="_blank">📅 21:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17164">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۞۩ ¥𝕒z∂𝓐Ｎ۩ ②①:②⑧</strong></div>
<div class="tg-text">تو نوار ساحلی میرم میام هرچی نفر اول بگم</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17164" target="_blank">📅 21:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پدافند بوشهر درگیر شد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17163" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دو سوخت رسان از رامون و بن گوریون به سمت تنگه هرمز به پرواز در آمدن
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17162" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtbTiFWp6MGVzvJTF7BnSc3-AmyX41ZSCW-f-6yCS_Ebs2Exyv7XJ1ny6Xd_wS3lZWLVffcYn-2nNrWhqOM0eEWUVkJ42_Gydq7d1v74_I3DdL_DoVxi9iNjNFwwhsB-wQKijjaMKilxjNeUwd4BlRpClJPrrjYqaJS9D_RbH23fTZZGL0NluN23TkZx1QnnTtnMhlEjwBYbo1XbNwLyJck3WPnKwSHupv0F8fc4rWH8nC-mFFi0B7w5Nb74uoY2a8ypfJX3KIatyaQKg-wDY0FaMJRl_zMDHf_85B5kRge2WfkmdDReA7JXy_G-HTYECCMntU_BEjlUdEA1TYa10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پدافند سلمان حاجی آباد هرمزگان زدن
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17161" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش انفجار چابهار
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17160" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
شروع شد</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17159" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتاق جنگ با یاشار : کاهش 5 درصدی نفت جهانی  با وجود درگیری سنگین نشاندهنده بی تاثیر بودن حملات ایران و استراتژی درست آمریکا میباشد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17158" target="_blank">📅 21:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به گزارش شبکه کان، مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17157" target="_blank">📅 20:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA_fVsG-moBfkYqzYBW1X7jGOsh2V2LMiWoUrCNlfNMD61CYtPLaubY6bbCRrZ_f-lLSZtaf4-X_ifgr2nB8oGVKR97Qs0greJimvXlhLKoMcvjzanjytrwT5dMll2iCpAdKke3T6d40tXorZx6Uu0XUzA4E6rG-6aMLiQudG_EcsnQBIU-BUnMsxZa-jFzzWc2oyRtMK6Olnvy0qijf8VA1mdVaGWvGYhcpz4YjWAgnQVLfkyUfUwUySmk8ilq7XgYc59wJxr-BL9cGmSBA1zuR6o1JUOAqlkbnPdzUzjtBS7Wa8lHMevkoorCMRKNGTkTzQA612C9DHU-NjP1FfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داره شلوغ میشه …
🚨
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17156" target="_blank">📅 20:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلام  امشب هم ردبول بزنیم؟</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17155" target="_blank">📅 20:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFarjam061</strong></div>
<div class="tg-text">سلام
امشب هم ردبول بزنیم؟</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17154" target="_blank">📅 20:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ارسالی : حمله آمریکا به اسكله صيادي بنود در بوشهر خدا راشكر خسارت جاني نداشت ولي خسارت مالي حدود ١٢قايق صيادي دوستان اتيش گرفت @withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/17153" target="_blank">📅 20:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231716a55f.mp4?token=thsw_LwL0ertzRjKSRghvmh-9sQBmgxe4WK824XgN-4ImIUNKMzFjrIsF9oUykUl9n3LmYkZz9UWUeVv7x-tceg4aZro-FnL6373ySQ961LLycQO7e16wBKs1LoLjuWBeZH-pYNEN7oF7x2XGz6svW_TFjhKxqCIWvSN-eb96vp2h5-K-Gf0xzVUrsAnNIo47pwFBnhRm-uW8duSP8wZeqe4z5iL--wf-9teTO5jIY-ax1-GHDQ2aTBHQ43Ht32UMB5LymNKh7VgdNQG1K8plmznivcRCLVpZd3xeYwFl4sUjT262Q3Zkcag4n82nChqNysPAkDBOVAU31olW9gn1CaYJu69K4dcr1PGDLWHJ04-blG_-UtGwwGw8V__5TXe0TAhT7d-Et8fmOBmtBLK2h4QGKybE5kPpEDomiQPh11MvXtA1DaJLwVbxyz5Ihu-asPZLg6LUkG7jdSA19IZYEhVUWtHniDir5WlZIPLQSDPzn6ChfVFNYOGg7mT0PZblwkRLvqiTDzVO1jZdtmAGp-vL2FzYjAepI5zV2h2aYYTE6l0EeFvlQt3hlsC-li1f3cjpFAdyyrmWYtNG-p_UKbDLSGBIi3AY_VER2lzlew-scDPomuznPD1LP59Z7kWI8Dmgx8ifTGQx3HMe5GtHmPYH62sk_d8PX37YI63PKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231716a55f.mp4?token=thsw_LwL0ertzRjKSRghvmh-9sQBmgxe4WK824XgN-4ImIUNKMzFjrIsF9oUykUl9n3LmYkZz9UWUeVv7x-tceg4aZro-FnL6373ySQ961LLycQO7e16wBKs1LoLjuWBeZH-pYNEN7oF7x2XGz6svW_TFjhKxqCIWvSN-eb96vp2h5-K-Gf0xzVUrsAnNIo47pwFBnhRm-uW8duSP8wZeqe4z5iL--wf-9teTO5jIY-ax1-GHDQ2aTBHQ43Ht32UMB5LymNKh7VgdNQG1K8plmznivcRCLVpZd3xeYwFl4sUjT262Q3Zkcag4n82nChqNysPAkDBOVAU31olW9gn1CaYJu69K4dcr1PGDLWHJ04-blG_-UtGwwGw8V__5TXe0TAhT7d-Et8fmOBmtBLK2h4QGKybE5kPpEDomiQPh11MvXtA1DaJLwVbxyz5Ihu-asPZLg6LUkG7jdSA19IZYEhVUWtHniDir5WlZIPLQSDPzn6ChfVFNYOGg7mT0PZblwkRLvqiTDzVO1jZdtmAGp-vL2FzYjAepI5zV2h2aYYTE6l0EeFvlQt3hlsC-li1f3cjpFAdyyrmWYtNG-p_UKbDLSGBIi3AY_VER2lzlew-scDPomuznPD1LP59Z7kWI8Dmgx8ifTGQx3HMe5GtHmPYH62sk_d8PX37YI63PKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سناتور
جیم بنکس: جمهوری اسلامی در صورت ادامه نقض توافق با «جهنم» قدرت نظامی آمریکا روبه‌رو می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/17152" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrBz4lEkKeI1AXpKOQOUbzSknv6JvDjoR85nqafem1VMDNVJOlIGTxNqDUeoYKrjTCzFnDjX9CM1toAlfhA9gp0yBy3g4NbsdEys9CyfweosNrXCm7hMjx0pSx8WwjD4NcKC7hv4NbLPORYaAN2wNy4HeggyU4t4sBIidkYn8vqWz30feTfWIPgO3UiQOWKQ6kdkZncUDPIHIlqV7Tr9Ql4lFEd7zFt72ZT39hcmTFGRGqDiPONqUAacqWj4Wazk7oUrY9BxwpuLTnjUXdXSszOLNgYr1Gm7FzkGwk3VRGJ_TAD3jxI5DQhKCPzcnbPzNcQgljktkuX2xW5ecf9SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حازم قاسم سخنگوی حماس در غزه ترور شد
وضعیت کنونی وی وخیم اعلام شد
ه
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17151" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الجزیره: سپاه پاسداران ایران یک مرکز فرماندهی آمریکا در غرب آسیا را امروز هدف قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/17150" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فوری | شبکه خبری ABC به نقل از یک مسئول آمریکایی: ما از دیشب تا همین لحظه ، ده‌ها موشک و پهپاد ایرانی را رهگیری کرده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17149" target="_blank">📅 20:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مدیرعامل راه‌آهن: با تلاش مهندسان شرکت راه‌آهن در کمتر از ۱۳ ساعت پس از حمله دشمن آمریکایی به خط راه‌آهن مشهد؛ یکی از خطوط بازسازی شد و به چرخه خدمات‌دهی بازگشت.
خط دوم نیز تا ساعاتی دیگر بازسازی خواهد شد.
هم‌اکنون تردد قطارها در خط بازسازی شده از سر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17148" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منابع : پس از پایان رسمی مراسم تشییع (آیت الله) خامنه‌ای، احتمال دارد که سپاه پاسداران (IRGC) بار دیگر فعالیت‌های خود را تشدید کند.
مراسم تشییع امشب به پایان میرسد و خامنه ای در حرم امام رضا در مشهد به خاک سپرده میشود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17147" target="_blank">📅 19:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da60dd210.mp4?token=MFR5qcVn7G-jEBrTOphXyAtFqNw8vuA7QPWhkNejQ9NpX5y5eIc_uYmkWm8Dv0d7eNpfc1G0GvxCbcLLDuSeSGwXu1CLk5qnyfdmbmv4OKMYd6qLyjI6UxZIYLThz27Va9dpur1-0wCouYl4rxdMyEjvFQroUIFHVnPKmv9XwZqb-fUD5nwR23NgJU8wiZ3gToe3yUYlpOvwLsonld-3-rmejbSXd3HXLmtTLioULz-qcql15683zm-PkFnjBUaGZC4nPLN31lK44Is0mLkvmrmCKp_k4CNXDmzy_TjMKlfbL5XwyrfJwvzCL-Q2O3zrWP36BrkK7Bg5qZkoUxj_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da60dd210.mp4?token=MFR5qcVn7G-jEBrTOphXyAtFqNw8vuA7QPWhkNejQ9NpX5y5eIc_uYmkWm8Dv0d7eNpfc1G0GvxCbcLLDuSeSGwXu1CLk5qnyfdmbmv4OKMYd6qLyjI6UxZIYLThz27Va9dpur1-0wCouYl4rxdMyEjvFQroUIFHVnPKmv9XwZqb-fUD5nwR23NgJU8wiZ3gToe3yUYlpOvwLsonld-3-rmejbSXd3HXLmtTLioULz-qcql15683zm-PkFnjBUaGZC4nPLN31lK44Is0mLkvmrmCKp_k4CNXDmzy_TjMKlfbL5XwyrfJwvzCL-Q2O3zrWP36BrkK7Bg5qZkoUxj_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمه از نزدیک آتش سوزی شدید زنجان
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17146" target="_blank">📅 19:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شورای همکاری خلیج فارس
: حملات ایران به کشتیرانی در تنگه هرمز، امنیت انرژی و تجارت جهانی را تهدید می‌کند
ما از شورای امنیت می‌خواهیم که موضع قاطعی برای تضمین آزادی دریانوردی در تنگه هرمز اتخاذ کند.ما ایران را مسئول این حملات می‌دانیم و از آن می‌خواهیم که فوراً و بدون قید و شرط تمام اقدامات خصمانه خود را متوقف کند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17145" target="_blank">📅 19:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5fspNLHD_XkjPkdg587O4bwBOScf_1b5yiBT_s2WYWJPGXLFGLnWdJXkE2YbBot00_zFR_6zoK5tgU4Vh7wHoYkZ4bUE6d63jJjTwE_FD_YROz_Y6D_30qTzzVVCLYsPDsiomMkhBTevAE8Pz8pNz_TnDjdbrju1qTTfxqY9jG8sm2V1z9OqcJKTCrW35_9ezyCVqAgSpJQWkohP_YfFutFSKc5gOpPwLbtUVKMB2P7lwCJM6Jt5cyfja46EX6Oc3cwSPHtUECIK9cV_arFrBb8qxfM-jzSI7JgOSTL7kmgt3zBl8jYI9GdNbxnO9ZKPiJrPXQy7u3zwZJkRkK97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنجان الان از زاویه های بیشتر ( دم بچه های زنجان گرم
😁
🫱🏼‍🫲🏽
)
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17144" target="_blank">📅 19:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qedZUm23QzxTJ0ivYRg82gygp-ESKz4m3l34iPbg1lzPn9mTg9BxZ6OvBTiIKGWqZGg82BubWHAINIIJd0kBcgg5HLPtw1zNW7P0Tonhk29QnKojKLsY9VIuIHOUvghunY-HlPq5srNu-kY45sG8PD4GBes3ENAMUpAcbTYnVdGIJ1IXqPyQgFp3RLHU7oIhrdrmAMKqbqXniutZZXYh7gqtmuN2niRpHB6uyzXSVu94_ac8TC0UJ432h8oCyR36qtFCj0ygcZYSvUdV-ACkUJ9OYJjNqve_i6tFHcW6O_r_UEorPnerASV8Wn3i5Z-egqJhSU4tJv8VQaDZjtdvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwjDdByhTQ460VsAsLQycxMvLThsv_fPPxuwjcuqR9oLwLn_tyJPupYwbaT5BDrhrQKUdLJLkyFj5Tw7D_Gh3zN4MJ_mfwcqvTXgrV8MnZO96wOvDgDiA-nMOreqbIcfd70zywt1Q8aqhz4MqxDuMOvlgo-2yTABTeykTcGzvxtye_v902FgWnaVW6MeenFiVic0xThJbiWua9Pj8NHQrwX1FsPjP_mwQzr4rv3Kpkh4xRd7WrswPHkWbvJFIlgrUVGaRQuyNmhcOmL3UJMlMleTh3YW1Ui_oOdtP2oC6SSzUFGbURULMqlzjAnNo4rtoQCKPOz9fKIEILhawMbIBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجار‌ در شهرک صنعتی زنجان (تایید شد)
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17142" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار‌ شهرک صنعتی زنجان
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17141" target="_blank">📅 19:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نخست‌وزیر نتانیاهو خطاب به خلبانان جدید نیروی هوایی در مراسم تحویل نشان‌ها: "جنگ هنوز به پایان نرسیده است، چالش‌های جدیدی در حال ظهور هستند." وزیر امنیت اسرائیل، یوزی یعکوو، در این مراسم گفت: "ارتش دفاعی اسرائیل آماده است تا عملیات را از سر بگیرد و به صورت…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/17140" target="_blank">📅 18:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نخست‌وزیر نتانیاهو خطاب به خلبانان جدید نیروی هوایی در مراسم تحویل نشان‌ها: "جنگ هنوز به پایان نرسیده است، چالش‌های جدیدی در حال ظهور هستند."
وزیر امنیت اسرائیل، یوزی یعکوو، در این مراسم گفت: "
ارتش دفاعی اسرائیل آماده است تا عملیات را از سر بگیرد و به صورت مستقیم به ایران حمله کند - حتی برای بار سوم.
"
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17139" target="_blank">📅 18:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976290cc1c.mp4?token=TF2CsYx6tFLPTdhxeYGZHxZ9CdZja8_6YSXlxeU5ssIJtTCEjY5pO9ETNOzzx7foZmQ_wWO3OmLRnaGwwGGHXdnBkan3k88KkFuHdGC1-lPPOo_TFNTy-SXdRzAv3_xYp6jBthdTB9-dORBPzdY34KYiCPKRmdcyXmlTlqsLR2EscxLH6Ouw19o1DrtNYzyyhaUI35OU8ChNgG15P_R8gszNlu21bUFeHK6ebr9bxHZ72akr705GXp2LxpUUg7qLvLxkvtOsLfjoiPFtRoMlHIs1HTYRss5A6SdVVBiOHj-LvAeCvQ9YplmO0RmtyUoFOM1XM3c8hQTYv1uf-lH8eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976290cc1c.mp4?token=TF2CsYx6tFLPTdhxeYGZHxZ9CdZja8_6YSXlxeU5ssIJtTCEjY5pO9ETNOzzx7foZmQ_wWO3OmLRnaGwwGGHXdnBkan3k88KkFuHdGC1-lPPOo_TFNTy-SXdRzAv3_xYp6jBthdTB9-dORBPzdY34KYiCPKRmdcyXmlTlqsLR2EscxLH6Ouw19o1DrtNYzyyhaUI35OU8ChNgG15P_R8gszNlu21bUFeHK6ebr9bxHZ72akr705GXp2LxpUUg7qLvLxkvtOsLfjoiPFtRoMlHIs1HTYRss5A6SdVVBiOHj-LvAeCvQ9YplmO0RmtyUoFOM1XM3c8hQTYv1uf-lH8eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه زیبای قبل و بعد بیت رهبری برای درک بهتر شما
💥
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17138" target="_blank">📅 18:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=o-bIz3K7uQr7aLvUoVnRqPZPvStT1-vCrJ4XtcqWWIbQ4qkDTF1gnsdLVSdsINclkEsfYoXGzgqg7hNuW8XJYEsMIMps8EBN17p0tzHDforXvyre47MbZcjK1VGOnMulwY552tuPOdbkFyevuJgHnBksLqCgufwKhs1B2AD6EHmlL8L2qFQ_4noIce7PhgUdynId6Urkjm0S52dWhYi-KENNIlJ7mrNEYGPZGal-KtjNJnu4tw-COuzsSlHcys1EiDMg-J_2j9n_wFiPzNZnW0ESwHphHAJYk8Xbb2dBzsSgl3p-nLFjM-AgiXnXOD9NLqRlTZEE-op0fUnS9YiaAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cac8f1356.mp4?token=o-bIz3K7uQr7aLvUoVnRqPZPvStT1-vCrJ4XtcqWWIbQ4qkDTF1gnsdLVSdsINclkEsfYoXGzgqg7hNuW8XJYEsMIMps8EBN17p0tzHDforXvyre47MbZcjK1VGOnMulwY552tuPOdbkFyevuJgHnBksLqCgufwKhs1B2AD6EHmlL8L2qFQ_4noIce7PhgUdynId6Urkjm0S52dWhYi-KENNIlJ7mrNEYGPZGal-KtjNJnu4tw-COuzsSlHcys1EiDMg-J_2j9n_wFiPzNZnW0ESwHphHAJYk8Xbb2dBzsSgl3p-nLFjM-AgiXnXOD9NLqRlTZEE-op0fUnS9YiaAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : حمله آمریکا به اسكله صيادي بنود در بوشهر خدا راشكر خسارت جاني نداشت ولي خسارت مالي حدود ١٢قايق صيادي دوستان اتيش گرفت
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17137" target="_blank">📅 18:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آلن ایر، مذاکره کننده سابق آمریکا در برجام: فعلاً احتمالاً در چرخه بی‌پایان «حملات و سپس کاهش تنش» گرفتار شده‌ایم ! دلیل اصلی این وضعیت، اختلاف بر سر تعریف «باز بودن تنگه هرمز» است.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17136" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ارتش اسرائیل (IDF) اعلام کرد که اخیراً دو تونل دیگر متعلق به حزب‌الله در شهر مجدال زون در جنوب لبنان تخریب شده است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17135" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت امور خارجه ایران: عراقچی، در گفت‌وگوهای تلفنی جداگانه‌ای با همتایان خود از عمان و ترکیه، درباره تحولات در تنگه هرمز گفتگو کرد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17134" target="_blank">📅 17:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntBEVJ9qPAWhnQi1u9xjVADFD28mBZXdZjk4S7uU7KWxsQgkeQvJtTdgYhoee1yy7Knc7BLxRvjtqKnwNCXZOnYu1RZV2VGk1cW2NISXfTJm9JwrF6DCEwwcrSZXAcSiPZD1aMqt63sAtORR65ugKdXXSVfdFSXVh-gCdGgqiBYG5J4tD1jMOeNFY8p0TDjSnh7uuY7AHLo0xiH8NtWRLfJVFtnB3usXgp0WqmnkJyLeBT3n9U0Isa1-j6szQdw47rtmfk6WhhfKVb3MnMfNdS0-qsYXn70U4gEeFTAzEPEk9R7Nr4evCkpQb4ykk4tS7Kv-QToHd7XVf3UYFuWHNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر نادری که صبح امروز توسط یک دیده‌بان در شهر اصفهان، مرکز ایران، گرفته شده، جت‌های جنگنده F-35A Lightning II نیروی هوایی ایالات متحده یا گارد ملی هوایی را نشان می‌دهد که بر فراز این شهر پرواز می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17133" target="_blank">📅 17:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۳ پا : مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17132" target="_blank">📅 17:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17131">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیویورک تایمز به نقل از فرماندهی مرکزی آمریکا (سنتکام): طی دو روز گذشته، بیش از ۱۷۰ هدف نظامی ایران را در جریان حملات هوایی مورد هدف قرار داده‌ایم
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17131" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17130">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=kikiZfNoyG8Xy1ud2q1tFAW7mDYPAX2VEGf75vxEcmYtjQ_8DWuX9L-lZObZuId0z0guJ5ILWscw4x3-QHea46BrcYJiXibXfh9H5x_W34As06_waafsUdIWXshmF9gFCt6SrtQh16k5pQom3eq_SLpi8Ot_z2HHaEY-D5EZhXf2AQxOaBswY_4dR21q1GmvaAl57cFPJWtle_EXTb9hPKo6TM8aE2JMCpH9nw4G9WG7iyMHFAOc2FGQ6Ur0WsHv8oO1icovTeqXMsB5mhiIfW-Y6LLwhq1For_ukojBXB-aVscZKwS9o3HFdFeOUrX6P7hEGMKqHDJbPrNn4BbOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75c9892.mp4?token=kikiZfNoyG8Xy1ud2q1tFAW7mDYPAX2VEGf75vxEcmYtjQ_8DWuX9L-lZObZuId0z0guJ5ILWscw4x3-QHea46BrcYJiXibXfh9H5x_W34As06_waafsUdIWXshmF9gFCt6SrtQh16k5pQom3eq_SLpi8Ot_z2HHaEY-D5EZhXf2AQxOaBswY_4dR21q1GmvaAl57cFPJWtle_EXTb9hPKo6TM8aE2JMCpH9nw4G9WG7iyMHFAOc2FGQ6Ur0WsHv8oO1icovTeqXMsB5mhiIfW-Y6LLwhq1For_ukojBXB-aVscZKwS9o3HFdFeOUrX6P7hEGMKqHDJbPrNn4BbOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">l
نتانیاهو : حمله به ایران مانند برداشتن سرطان از بدن شماست.اگر سرطان را از بین نبرید، خواهید مرد.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17130" target="_blank">📅 16:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17129">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNwECMCcEa1t7cL_KEqo_rFZDEUhx3IDk5eKrY9-9iISqy5IiAKnZrGVvNlb6ras1rr8oDIcg6yzvMAIBi7y1NJ2zfiHYvlDg0pfBZ_V5amXE0UagP4qrb9leOB69SbukQBj-m8vPPT18P3kN7g7JNjIauXE5_XuBUERkCUgQsX6IkZggn64rKfjxfMbDUrEOvYyBdZlb-Gr7bAyc4ez_8yxfUMhJevC4vrx-gyA97nI35UiuMlGZH466Jl_tqOkQKqY7iGqi3-F2_1UKudQKmTNjp1Jj0tybE7xb7AffOxC2z5hRIvjQ9qAq9qilMl2fxww7TJv_W9hdHt6viJLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پهپاد شناسایی آمریکا در آسمان زاهدان سيستان و بلوچستان
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17129" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fd028548.mp4?token=MksD-kw4XMRouOzpbIry_C9QMYMRf7z6rptrl3gYsF9T52Y8_D-rqGH7E8LuKz_UbM-kPDJ6S5M8JeLFWbRHKifu7pNG-LcREknkWKZ9u5NhpL4IgTYwufutk1W9B7JrQwC4OXCsewjUmHCIB6oAqqfW8pAxHuiTszBGehWdWTjRaosV2u5rc3dcIpAPQkLL1U7PRVTg8PJ1PzdohL57pmR4-bmKtcq0mKmZiB_Yddxo2f1cXM41DfNpeswUUdKVL2s60uoPTV1eAGNWsbCH-2QZ0DrGaSuEzrk9xRSChTDsvRg5GvZ3z4FtnmgVRW4kEOmGWTc_OvgNA85rYak1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fd028548.mp4?token=MksD-kw4XMRouOzpbIry_C9QMYMRf7z6rptrl3gYsF9T52Y8_D-rqGH7E8LuKz_UbM-kPDJ6S5M8JeLFWbRHKifu7pNG-LcREknkWKZ9u5NhpL4IgTYwufutk1W9B7JrQwC4OXCsewjUmHCIB6oAqqfW8pAxHuiTszBGehWdWTjRaosV2u5rc3dcIpAPQkLL1U7PRVTg8PJ1PzdohL57pmR4-bmKtcq0mKmZiB_Yddxo2f1cXM41DfNpeswUUdKVL2s60uoPTV1eAGNWsbCH-2QZ0DrGaSuEzrk9xRSChTDsvRg5GvZ3z4FtnmgVRW4kEOmGWTc_OvgNA85rYak1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج اسکله گمرک تجاری بندر چابهار @withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17127" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
