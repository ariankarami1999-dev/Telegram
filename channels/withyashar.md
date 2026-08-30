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
<img src="https://cdn4.telesco.pe/file/QH-zbGjjcljjsEvscO7RIcOD2BEuiev61JdkBIC55Rju-gozCDcJSxmzyxJ1k6PEKJYN50WcW-T0PVFpyZgByBfjQFTDFUdJyfDV97SMHVloOVx_xrYbLuzM6SgisUMQlUq-bKtEQJ5qlPLV3M4ciGO2ofTSdxqVzbWcNXuSdNAza36UIwC1dpFEb4IEzqN6AYmp6afnsli3w64G72UcNzXQQxgYUCe-hmoHBfKRuNR4NCDtDG09aSnqE_clHIBPO2ocoW8iTbwZfEewD1XIeqfJIdP6nKm8BJajOqSa5p7RjGz4pXt2gxzova-k3MtVAexrlnztXlFd3onkPXVumQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 440K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-21759">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ابراهیم عزیزی رئیس کمیسیون امنیت ملی:یک بار دیگر اراده ما را آزمایش کنید و بهای سنگین تری بپردازید، انتقام در راه است؛ فقط بدوید!‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/21759" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21758">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام آمریکایی: برای نخستین بار در یک ماه گذشته، حملاتی را علیه ایران انجام دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/21758" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21757">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۲ اسرائیل در خبری فوری اعلام کرد ارتش آماده هر سناریویی است و یک بانک اهداف گسترده دارد
@WarRoom</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/withyashar/21757" target="_blank">📅 00:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21756">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فرودگاه مهرآباد تا اطلاع ثانوی تعطیل شد
@WarRoom</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/withyashar/21756" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21755">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ab68fe7d.mp4?token=aQcgozu-1VADUqPFUbImKaPQZ1hZzul8SgoIQWxdCABll49JNnxxwHDkHT7yG-RmsqaF3pidEYCRTShShldSDpasU8XVqr94hCMAvlzqazMQzcmzZO-3aEmezChJDMr6jfWCujEiFvZZVo9PxDRBdOilJDDeEgrR_TDLGGlD--TDW44HHNADpr5IaGx1snKixR4LVeSx11Ip294dhdgBLunWhu193MVJRBcEt6NNDr1hcnODlPuBT87qWzHPiw66etCGuOw9ssyk8Xl0rhz8Jy9Qw3J0IxjTj5XJTNLdrBCyQpcsQi49PB7HNu3S304w9P_uPY4SjQo3WYWbbE5Yv4FG6X7iNVLsAgaistdOJnLxF6fVz9ppmyBGRxWHxyQbV2jN7kfarvtrn1Z6aGq5QojDv2f3tYT2xAvMYQ5_bv44H7jrXw_eKuzZaHZoMRsk1kl1HePTJbetWpwtu4wEmH0ZqgvfaY8-DYaWdC2TPSesBxL4Hd3Tc5SVQo0Wv2oQgBaFA1wntigPoPLUwK5M0kbE5trCs0pBDFdnlg2aYJKf8W-4UtqBXrHHPObYlmSvYFob0-PAh0MQolQPate0HWUHISwvmGUKhrm8ms2LpoN0dK7dYb2-nJ0lbhYCI1EB_y_O8H-08I-YhPuzuSEGDGG2MtaFbYdfkKe_C53htmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ab68fe7d.mp4?token=aQcgozu-1VADUqPFUbImKaPQZ1hZzul8SgoIQWxdCABll49JNnxxwHDkHT7yG-RmsqaF3pidEYCRTShShldSDpasU8XVqr94hCMAvlzqazMQzcmzZO-3aEmezChJDMr6jfWCujEiFvZZVo9PxDRBdOilJDDeEgrR_TDLGGlD--TDW44HHNADpr5IaGx1snKixR4LVeSx11Ip294dhdgBLunWhu193MVJRBcEt6NNDr1hcnODlPuBT87qWzHPiw66etCGuOw9ssyk8Xl0rhz8Jy9Qw3J0IxjTj5XJTNLdrBCyQpcsQi49PB7HNu3S304w9P_uPY4SjQo3WYWbbE5Yv4FG6X7iNVLsAgaistdOJnLxF6fVz9ppmyBGRxWHxyQbV2jN7kfarvtrn1Z6aGq5QojDv2f3tYT2xAvMYQ5_bv44H7jrXw_eKuzZaHZoMRsk1kl1HePTJbetWpwtu4wEmH0ZqgvfaY8-DYaWdC2TPSesBxL4Hd3Tc5SVQo0Wv2oQgBaFA1wntigPoPLUwK5M0kbE5trCs0pBDFdnlg2aYJKf8W-4UtqBXrHHPObYlmSvYFob0-PAh0MQolQPate0HWUHISwvmGUKhrm8ms2LpoN0dK7dYb2-nJ0lbhYCI1EB_y_O8H-08I-YhPuzuSEGDGG2MtaFbYdfkKe_C53htmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من رژیم ایران رو نابود میکنم، اینو بهتون قول میدم و مطمئنم این کار شدنیه.اونا خیلی ضعیف تر از قبل شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/21755" target="_blank">📅 00:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21754">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/21754" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21753">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار من تو مسیر بندرعباس میناب بودم  از کنار دیوار خیاط دانشگاه هرمزگان موشک بلند شد
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/21753" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21752">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سی‌ان‌ان: دور جدید حملات نظامی امریکا به ایران شروع شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/21752" target="_blank">📅 00:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش صدای انفجار جدید از لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/21751" target="_blank">📅 00:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رسانه های عبری : جالب خواهد بود ببینیم رژیم ایران چگونه به حمله آمریکا واکنش نشان خواهند داد، زیرا عدم واکنش به این حادثه می تواند نشانه حقارت باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/21750" target="_blank">📅 00:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال ۱۳ عبری: اسرائیل به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی هزاران کورد را به اسرائیل برده و آموزش داده بوده است. ولی سه روز پس از آغاز جنگ ۴۰ روزه، پیامی از آمریکا به اسرائیل می‌رسد که طرح اجرا نشود. @WarRoom</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/21749" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21748">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بیانیه سپاه : دشمن در هر دو عرصه اقتصادی و نظامی، تبعات این محاسبه غلط را خواهد پرداخت
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/21748" target="_blank">📅 00:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21747">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۳ عبری: اسرائیل به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی هزاران کورد را به اسرائیل برده و آموزش داده بوده است. ولی سه روز پس از آغاز جنگ ۴۰ روزه، پیامی از آمریکا به اسرائیل می‌رسد که طرح اجرا نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/21747" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21746">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سنتکام:ایران میخواست یه سری مین رو توی تنگه هرمز بفرسته که ماهم جواب کارشو دادیم.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/21746" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21745">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/21745" target="_blank">📅 23:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21744">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آکسیوس : دستکم ۷۰ تن سپاهی کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/21744" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21743">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسرائیل جنوب لبنان رو داره برای فصل کاشت آماده میکنه و شخم میزنه
😂
🔥
@WarRoom</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/21743" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21742">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آکسیوس:ارتش آمریکا در خاورمیانه به حالت آماده باش درآمده است و برای پاسخ ایران آماده شده است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/21742" target="_blank">📅 23:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21741">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/21741" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21740">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ادعای آکسیوس : ایران در حال آماده‌سازی برای پرتاب راکت‌های حامل مین‌های دریایی به داخل تنگه هرمز بود
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/21740" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21739">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادعای رسانه های رژیم :
حمله ای که آمریکا انجام داد با پهپاد بوده که از اردن بلند شدن، حداقل چندین پهپاد MQ9 از پایگاه موفق سلطی امروز به سمت منطقه تنگه هرمز آمدند.
فرماندهی سنتکام اکنون در آنجا می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/21739" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21738">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تسنیم: برخی گزارش‌های اولیه غیررسمی حاکیست که بر اثر جنایت دشمن آمریکایی تاکنون ۲ نفر به شهادت رسیده و ۲ نفر نیز مجروح شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/21738" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21737">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سید محمد مرندی: رژیم ترامپ مرتکب یک اشتباه بزرگ شد.
@WarRoom
😂
🔥</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/21737" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21736">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش شنیده شدن چندین انفجار در جزیره لارک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/21736" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری های تروریستی رژیم ، فارس و تسنیم این حمله را تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/21734" target="_blank">📅 23:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش های منتشر شده از کشته و زخمی شدن تعدادی از افراد سپاه در پی حمله نظامی آمریکا به جزیره لارک.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/21733" target="_blank">📅 23:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21732">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/21732" target="_blank">📅 23:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21731">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به گزارش دیدبانهای اتاق جنگ :
۳ انفجار در ابتدا حدود ۸:۴۵ دقیقه شب و ۳ انفجار بعد از ۱۵ دقیقه ۹:۰۰ شب تهران در لارک اتفاق افتاد تهران
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/21731" target="_blank">📅 22:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21728">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/21728" target="_blank">📅 22:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21727">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه های عرزشی : درحال حاضر قایق‌های تندروی سپاه در تنگه هرمز،از چراغ‌های جستجو برای خواندن نام کشتی‌ها از روی بدنه آن‌ها در شب استفاده می‌کنند و سپس با استفاده از رادیو، با نام کشتی‌ها تماس می‌گیرند تا به آن‌ها هشدار دهند که تحت نظر سیستم قرار دارند و از آن‌ها می‌خواهند که از عبور خود منصرف شوند،درغیر این صورت با آن‌ها برخورد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/21727" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21726">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارشاتی‌از‌ لارک هست ولی شب میلاد هم هست و عرزشی ها فشفشه بازی میکنن
😂
@WarRoom</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/21726" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21725">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وقوع حادثه دریایی برای یک کشتی متعلق به بحرین @WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/21725" target="_blank">📅 22:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21724">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5076i5YycexYsxkr9e0UUXzVsttck-hLyTBVSAX0m34eWZQBUrgrhnJGUINKsFFEMYP7HIPW-sKZVuHVVTHUdHliAPuiB0hGxNQr11Yvp7ub6uvrNlXrNS7fSJTEI0kdXY70cODqNnRgEDyo0TNNStbICQ84aMwXxCn7Hleq8uvsAEEzGuafQNatbR5b-wvqo0YwOt7D7APiOFjKvSu7H-bgykJew8K0Non1AJSakmiiSmtz3kCBeqU9hlovukEAAyzQVcTglHQIXQKKaJizrLYPTo0CDYSXuc1eDZabbucx-qHVhLQinjcWCTPzEYtxEtUZWv2G7WPFA8hvyaVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگال کانال ۱۲ اسرائیل : مقامات ارشد رژیم ایران به دلیل وخامت اوضاع اقتصادی در کشور و ترس از بازگشت اعتراضات، در حال بررسی فرار هستند
مارک لوین به ترامپ ؛ اگر درست باشد، آقای رئیس‌جمهور، الان بهترین زمان است که مخالفان و نیروهای مقاومت ایران را مسلح کنید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21724" target="_blank">📅 22:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21723">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وقوع حادثه دریایی برای یک کشتی متعلق به بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21723" target="_blank">📅 21:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21722">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شبکه I24NEWS:کشتی های جنگی ترکیه به طرز خطرناکی در دریای مدیترانه به کشتی های نیروی دریایی ارتش اسرائیل نزدیک شدند که باعث هشدار و سطح آماده باش رزمی در نیروی دریایی اسرائیل شده
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/21722" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21721">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">از تنگه صدا میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21721" target="_blank">📅 21:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21720">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش شنیده شدن چندین انفجار در جزیره لارک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21720" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21719">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyGJ_9Vr0og6DqKtH4-inLAgvC7wryzJS9rMjrLI6KudpeeSjbnn05mTSjPYZoDw6ro464MTSDe2pjVyD0RLoWe5KWgUjGpte3FroxzTPfHgJOQ2KIjgdP3pJWvEk2wjPlZ5gNjXEpaFnzhzvTnssyvhuqlW5U3SJV4w9zJ-d6kZTBVjNKRrspmDe_gQ4YwmsWloj8OqP6elCtxkMC-AkftBWgXXdeiZ9yqi9qc_5qikktJl4GTZHscTfyGn7IGQOUjdWa8qbOmgub4xZEBFeZybgXf0axxJ-p2-zS919Y7fcNMKGzFlu6Qe9hCDHv5-UI1rZNNgnG47p3fXsn5XKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی با تأخیر زمانی از حادثه‌ای در ۱۲ مایل دریایی شمال خصب، عمان دریافت کرده است.
یک نفتکش هنگام عبور از تنگه هرمز توسط یک پرتابه ناشناخته مورد اصابت قرار گرفته است.
این پرتاب دقیقاً رأس سه ساعت پیش از طرف دیدهبان‌های اتاق جنگ گزارش شده بود ولی من از ترس حرف مردم به علت این‌که ساعت، ساعت معمول حمله نبود گزارش نکردم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21719" target="_blank">📅 20:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21718">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3d0d56a.mp4?token=XxDYUxjOJNDua9RtWmuwLV-seUc6pmRWHr9hvRV1rycryXvDweEDk2wsp37Gz1D7zbbtojlv1gTSJu341S1dwSYb6TGG0LZScRkbyejieM6lxil_ntHu0AC140P936vFaP2AsLqp8E0no4WE_dYpj06y_sJ8-eCLaDTa40F_90s71wGlfJk-y5ixSy0PV4qNz1o0cuOSeCH1O341pA6KW0RgaEuaafFclFdZQObnZ2VPjv25IDJXyetcRd1rcjm3Y8vyNauPTj05AygS-g-MDReXNdLW2CbT6gszRfUaR0H4LzJorKnLZm4uVYnSdv2WCR26_Wiuq3D-_Nqfak8qAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3d0d56a.mp4?token=XxDYUxjOJNDua9RtWmuwLV-seUc6pmRWHr9hvRV1rycryXvDweEDk2wsp37Gz1D7zbbtojlv1gTSJu341S1dwSYb6TGG0LZScRkbyejieM6lxil_ntHu0AC140P936vFaP2AsLqp8E0no4WE_dYpj06y_sJ8-eCLaDTa40F_90s71wGlfJk-y5ixSy0PV4qNz1o0cuOSeCH1O341pA6KW0RgaEuaafFclFdZQObnZ2VPjv25IDJXyetcRd1rcjm3Y8vyNauPTj05AygS-g-MDReXNdLW2CbT6gszRfUaR0H4LzJorKnLZm4uVYnSdv2WCR26_Wiuq3D-_Nqfak8qAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعزام بسیجیا با قایق‌ماهیگیری، برای مقابله با ناو‌های آمریکایی؛
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21718" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21717">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK1hRbVn0ZiCFDQb1YlwaH5tdRY2FqBfkoY4wuZm4QrBUKVz5xgvm-2C79_tMVMKPcNk1RPI6bWvOpYEfTF0Sd6T_vNstXKddu2d-FcddXOpqawNK8yEuxSUwbY3zY_s1r5Bn_EtjwONTsR2UUbs8zNtU_1mASHt2Se5F5v3ubjFkFkkFtIVFdTMdmSML5CDdvb_aWZQz3rJgK2qunSQDqFPN77fZtmfFH096WqiBqpxwkdWTEcrxSU864VnM6KURT6reh8BCcqfFhZZbtCC7ieGAMTzJgkln3Snh29vOHGnkyvs977bp6rP3aI72T0pKHxVrqlCSBdkW4fiFf_FRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرنده «CMV-22B Osprey» مستقر در ناو هواپیمابر، کد اضطراری ۷۷۰۰ را بر فراز خلیج عدن ارسال کرده و در حال حرکت به سمت صلاله در سلطنت عمان است
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/21717" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21715">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy1pkXLSDPzePhnWMLlMnCaZWjZKPlW663t4Jz4VvTKDfF3f-TrT49xgtApAydVdOw7OlWFbVzExTreLpSH2ST6M5o-k1XHs-IxqZuKKf7UqnDnXVqc7HIj-5lnCp4-RIv9JM9TNO_VqHgRDwPCpgq3Gc34tqsNGt2-1oSZU1nz3MFIBnI5-aq7rJ7KhME1fuFaElYpnLd1ywYJLVu_o56cz8KoshxiZ04AXRnMjLwMpOOod1uB3P40fDgwqF5Pkwvi12N28g_9mUc2mmpFwjxHyQQwsCy11tY6PmcYbW_V9uQyDJYapdgey5VyDMIxATOD2Wuhcw3FEGPFYyDvZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91FBSu0a9UCFvzjcMUyTtURnsppXnSaEoqGuiJFggMZ4xQsnj6Qf4TwWq5QxkXttDMfzLZ-cZ7skIX2Xoooo6XsCg-QAmi8wvLKDxrzx530P9C8KypOOzjB0jh_puFHHrAcZ_0W-SHHovypbF25kMWI0ClnddjjqS7DNWqm5sdEJEi_BjejZEzRsxO_h7g8_R8oyUEkf2sLsKRcTG1j6fRbe-TdU1WnwplXADfjB_acGXt-pz6WSLDzBko2xI04nt4wQvqkO7jgOf18Mi225bw1Phx0025Wpa9mkYNNnkDtcLYSRabWvWZacHPNI2LQS0fS11mPD97aKRJWgPtODw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیکلاس مادورو از زندان:
«این عکس‌ها را به‌عنوان هدیه‌ای کوچک برای همه نوه‌هایم، چه پسر و چه دختر، و برای همه مردم شریف و بزرگواری که ما را دوست دارند، می‌فرستم.می‌خواهم بدانید که ما استوار ایستاده‌ایم؛ با قلب‌هایی سرشار از عشق شما. عشقی که به ما می‌رسد و به دعا، کنش و تلاش همیشگی، همبستگی و حمایت واقعی تبدیل می‌شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21715" target="_blank">📅 17:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21714">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن» آمریکا، بامداد یکشنبه ۳۰ اوت، پس از بیش از ۲۵۰ روز حضور بی‌وقفه در دریا و پایان مأموریت طولانی خود در خاورمیانه، از آب‌های نزدیک سنگاپور عبور کرد و در مسیر بازگشت به آمریکا قرار گرفت. خبرنگاران در جزیره باتام اندونزی، این ناو را کمی پس از ساعت یک بامداد به وقت محلی در حال عبور از تنگه سنگاپور مشاهده کردند. این ناو در جریان مأموریت خود در خاورمیانه از عملیات نظامی آمریکا پشتیبانی کرده و یکی از طولانی‌ترین دوره‌های استقرار ناوهای هواپیمابر آمریکایی در سال‌های اخیر را پشت سر گذاشته است. آبراهام لینکلن قرار است پیش از بازگشت به پایگاه خود در آمریکا، برای استراحت و بازیابی خدمه در تایلند توقف کند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21714" target="_blank">📅 15:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21713" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
👺</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21712" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الجزیره: آمریکا فعلاً از تحریم چین بابت خرید نفت ایران اجتناب می‌کند به گفته یک مقام سابق امنیت ملی آمریکا، تحریم چین همچنان به‌عنوان گزینه ذخیره ترامپ باقی مانده و تواشنگتن امیدوار است مجبور به استفاده از آن نشود
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21711" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21710">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پرونده جدید : مأموران ایرانی، کودکان زیرسن قانونی 15 و 17 ساله را در شمال اسرائیل، از طریق اینترنت اغفال ، جذب کرده و با پرداخت مبالغی به صورت جداگانه، آن‌ها را برای عکس‌برداری از مکان‌های استراتژیک و نقاشی کردن نوشته‌های گرافیتی استخدام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21710" target="_blank">📅 14:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21709">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر انرژی اسرائیل : اسرائیل دوباره به ایران حمله خواهد کرد حتی اگر آمریکا توافقی امضا کند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21709" target="_blank">📅 13:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21708">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏آزاده اخلاقی، همسر محسن نامجو می‌گوید نامجو ۶ روز پیش «به بهانه پرینت چند کاغذ در سر کوچه» با یک صندل از خانه خارج شد و ناگهان با چمدانی که از همسرش ربود، از ایران سر درآورد. اخلاقی همچنین افشا کرد که نامجو حتی پاسپورت جمهوری اسلامی را نداشته و با واسطه‌گری…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21708" target="_blank">📅 13:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21707">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز : بانک مصر در حال بررسی پیشنهاد وزارت خزانه‌داری آمریکا برای قطع ارتباط شعب امارات از بانکداری واسطه‌ای دلاری به دلیل تراکنش‌های ادعایی مرتبط با ایران است. بانک مرکزی امارات بازرسی ویژه و فوری از این شعب آغاز کرده است. بانک مصر اعلام کرد عملیات در امارات عادی است و اقدام آمریکا هنوز پیشنهادی بوده و تنها به شعبه امارات محدود می‌شود، نه عملیات در مصر یا سایر نقاط.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21707" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21706">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLqU4UF2jyxCHm9b_CUbD_ADoBfZQMfsEGsUQ7WbjsrMEPZMsWZAI9oaDT-VhnMgVxGKwd59UQxtzQpD7k6nnwKzJxoZ9Vl1dsM_UtlHgGM821nnGsLw4_p9sZewv6Zzh668tuKuu10dyIDTZ5dNt3rSpfWAOM8KImUlq8BxnQsJ61srQXVI7lBu4lSQ8irDNsYTERvJJQuGL-dT96GU0i5JVYhuH3AwT5TH3DodKjF2zlFIEgvZL7IdOkzBU98_xDa69JSvI7MoVY0tBkSO-Q7PW7BtoIdmMgcKaqi1DeM1TCpfgg9b_V5FGwSsBF5bzby4gL7JsoCBrnOmK_yqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق، انتقال محموله‌های نفتی خود را از طریق عملیات انتقال از یک کشتی به کشتی دیگر (ship to ship) در خارج از تنگه هرمز، آغاز کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21706" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21705">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آکسیوس به نقل از گزارش سنتکام میگه جمهوری اسلامی یه مشت آشغال ریخته بود (۲۰۰ شئ شکل مین) تو تنگه میگفتن مین‌گذاری کردیم ولی کلا ۱۱ تا مین انداختن تو آب، که ازون ۱۱ تا ۵ تاش درست انجام شده بوده
.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21705" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqQL4LIn9lW4qb_F84B6RFSbdqr1199qk7iMX8DLhz2vKTRVrkvH2GYi37_fpRCJsV1SiZF-u_dWAs4wYoSI9eTmI7dbdv-JfhMa_k5hHq-hM5BO1npbicUPzqk0UjG7Pel_kA-AzVmkz3BglHQR9ru8J8vFuOR40DFCn-zkgmh57igtaOuxbVrMFsgwgykdyzmSQQsDDQutnsio-lMz-q67Arn1TCC5XuGAbUqAbibTKSa1U8IO9ttiRfvFTZF5aQBs6fxtLc3wit0jtjLWkuH03to-pYGgzcGIbTzNJoSK5shr2k-0HPqIjt9g2NC6-28bW3jCxFysTTbxOfpcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند جنگنده F-16C/D گارد ملی هوایی اوهایو
از بال ۱۸۰ شکاری و اسکادران ۱۱۲ شکاری در مسیر خاورمیانه هستند. این جنگنده‌ها با کال‌ساین‌های
TABOR11 تا TABOR16 و TABOR21 تا TABOR25 و TABOR17
ابتدا به پایگاه لاژس در آزور پرتغال می‌روند و سپس راهی خاورمیانه می‌شوند. در این عملیات، هواپیمای سوخت‌رسان
GOLD10 (AE066E / 62-3569)
پس از سوخت‌رسانی به جنگنده‌های TABOR11 تا TABOR16 و
GOLD12 (AE44FF / 23-46116)
در حال بازگشت به پایگاه گارد ملی هوایی بنگور است. همچنین
GOLD22 (AE0479 / 58-0061)
برای ادامه سوخت‌رسانی به جنگنده‌ها در حال حرکت است و
GOLD25 (AE5FAC / 19-46065)
نیز در این مأموریت حضور دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21704" target="_blank">📅 09:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21703">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از منابع: مدیر سازمان اطلاعات مرکزی آمریکا (سیا) پیشنهادی را به مسکو ارائه کرده است مبنی بر برگزاری یک اجلاس که در آن ترامپ، پوتین و زلنسکی حضور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21703" target="_blank">📅 03:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21702">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">@WarRoom
جعبه شیرنی ۲</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21702" target="_blank">📅 02:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21701">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشایان</strong></div>
<div class="tg-text">سلام یاشار جان. این یه پیام دلیه که برات می‌نویسم زیاد ربطی به ماجراهای روزمره نداره. خوشحالم که پیدات کردم اینارو بهت بگم چون بنظرم خیلی بیشتر ازینا حقته بدونی. من ۳۰ سالمه. ۸ سالم بود که تو دبستان شهید باهنر تجریش با رفیقام قفل وبسایتت بودیم. تو زمانی که آخوند نمی‌ذاشت بچه های ایران نفس بکشن یاشار رپفا یه تنه آرتیستای جدید و سبک جدید حمایت می‌کرد و میاورد بالا و من چون اینترنت خونمون دایل آپ بود می‌رفتم پاساژ البرز تجریش، یه مغازه بود مسعود موزیک که سی دی پستای جدید وبسایتتو برامون میزد و اون زمان رپ برای ما انگار تمام آزادی و چیزی بود که نداشتیم. و امروز برام اصن عجیبه که حتی پزشو نمیدی و زیاد به روی خودت نمیاری که اگه تو نبودی اصن چیزی به نام رپ فارس با اون دوره تاریخیش که هیچوقت دیگه اونطوری نشد به وجود نمیومد. الان شاید نسل جدید باورشون نشه اما ما یادمون نمیره تو کی بودی و چیکار کردی. تو فری استایل همه رپرا یه پسر عینکی لاغر بود که کم کم همه فهمیدن این یاشار رپفاعه. خوشحالم که الان از طریق این کانال از حالت باخبرم. به امید یه روز که تو ایرانمون، توی یه ایونت که کتاب خاطراتت از رشد موسیقی زیرزمینی ایرانو نوشتی و برا علاقه مندا امضا می‌کنی بیام و کتابتو بخرم و امضاتم بگیرم. عشقی داداش.</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21701" target="_blank">📅 02:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">@WarRoom
جعبه شیرنی</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21700" target="_blank">📅 02:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromalireza</strong></div>
<div class="tg-text">سلام یاشار جان عشقی
امروز دو تا مشتری اومدن (من صندوق دار یه مغازه شیرین عسلم تو پایین شهر) دو تا مشتری اومدن زرتشتی بودن و اصالتا یزدی واقعا خیلی آدمای با شخصیت و خوش رو خوشتیپ خوش صحبت با فرهنگ بالا با اصالت و واقعا زیبا بودن اصا انرژی مثبت فراوان اصلا خیلی حالم خوب شد و انرژی گرفتم
ولی در روز چند رأس عرزشی میان مغازه واقعا آدمای کثیف بی شخصیت بی ذات پرو و طلبکار بد رو کثافت و کثیف بد تیپ بد چهره شبیه خوک میمونن و شپشو ان آدم حالش بهم میخوره و واقعا اعصاب خورد کنه وجود شون حروم زاده های بی مغز قاتل
واقعا بی صبرانه منتظر روزیم که از دست این شیعه ها و عرزشیا خلاص شیم و مردم با اصالت مونو ببینیم و کلی کیف کنیم</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21699" target="_blank">📅 02:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21698">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتاق جنگ با یاشار :
P-8 Poseidon
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21698" target="_blank">📅 01:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتاق جنگ با یاشار : تنگه دعوا شده
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21697" target="_blank">📅 01:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
چندین کزارش از شنیده شدن صدای انفجار از تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21696" target="_blank">📅 01:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21695">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21695" target="_blank">📅 01:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21694">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">@WarRoom
hamshahri javan</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21694" target="_blank">📅 00:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21693">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21693" target="_blank">📅 00:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21692">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏آزاده اخلاقی، همسر محسن نامجو می‌گوید نامجو ۶ روز پیش «به بهانه پرینت چند کاغذ در سر کوچه» با یک صندل از خانه خارج شد و ناگهان با چمدانی که از همسرش ربود، از ایران سر درآورد. اخلاقی همچنین افشا کرد که نامجو حتی پاسپورت جمهوری اسلامی را نداشته و با واسطه‌گری بهمن بابازاده، خبرنگار امنیتی که ۶ ماه با نامجو در تماس بود، مجوز حکومتی برای بازگشت به ایران را دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21692" target="_blank">📅 00:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21691">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm4pwHKYZDky9K_GNCqaTsOvrIzyl0xVlYyU5_0JpXjdtpEQKls3WsuXKd28q_U51tEaTx9K4wr6aIxd2fRANhR7FV2b0OzD0qK5mMQttn_KH4fvpVjMojT2uQGNnQaoRgczRLNPm02rrI7U9NJoliJu9pf8FIiELaaJhiLLTEUIf3IRXGLkVwKZVSBeUe3hZduO5RuRuJMO-m-56gdn-cQGEhXwpygs5L7atJ_Ta7ZiNlBdU73p215k3gNSRGEy6mnSZagGtuPYNVFPFNgKy3aqcZP0HOkUE-3-vRbr1kuRszlciCVJm2zbTJwyN6vDDJ-cU9bzamh5I0AwygQmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کارگاهی محدوده بزرگراه آزادگان انفجار رخ داد ؛ یک کارگر جان باخت ,در این حادثه یک کارگر 21 ساله جان خود را از دست داد و یک مرد 30 ساله نیز مصدوم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21691" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21690">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtwpIl8ARXGH6zxD7Rf46zslrkEhMKTR5tBN8PUUj2wZ2pNOQ0Kn3EZmyGFWC5ivoB18dBm3N6H6KWucZEw9HEtGnlNHqWdC1fPQ3d3cMedOgZNms_C4DpfG-rsuHsYsbi05_HZ86iNP2-PQ1mfnylZ7Denr3qpfsU8FOQicasLjlB_0vj2q15iRO2U8hog6BixoJHEIR6JJbz88C6DxIf8V86BcoW_axR9oRsu58EiYPJg6fJRH8ddNZ7UNwP-AwYIQ_YHZWhXvtr-R5jS8x14nvZgu5kMVkvvEjyMUfATUm-sY_A7FqxLecxgpbDpSm3ORbicmGDDywKS8Id_ZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل
: فرمانده یگان نخبه و یک
تک‌تیرانداز حماس در غزه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21690" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21689">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پدافند جنوب غرب تهران فعال شد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21689" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21688">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کاظم دست کج غریب‌آبادی:
تلاش قطر و پاکستان این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر.
ایران آمادگی خود را از طریق تفاهم با عمان درباره تنگه هرمز مشخص کرده، اما اجرای تعهدات بر عهده آمریکا است.اما آمریکا تعهدات خود را متوقف کرده
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21688" target="_blank">📅 22:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21687">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس: ابتکار بستن تنگه هرمز از سوی فرمانده نیروی دریایی سپاه مطرح شد
دو مقام اسرائیلی به باراک راوید گفتند با اینکه طرح بستن تنگه هرمز توسط سیاست مداران ایرانی درحال بررسی بود، تنگسیری بدون گرفتن اجازه کل تنگه هرمز را مین گذاری کرده بود
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21687" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21686">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بانک مرکزی امارات متحده عربی با تأکید بر لزوم رعایت قوانین توسط تمامی شعب «بانک مصر»، از آغاز تفتيش و بازرسی فوری این بانک در رابطه با مبارزه با پول‌شویی خبر داد و اعلام کرد که اقدامات احتمالی بعدی را بررسی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21686" target="_blank">📅 21:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21685">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مارک لوین : قطر یک رژیم سلطنتی و اسلام‌گرای شیطانی و نامشروع است
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21685" target="_blank">📅 20:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21684">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=b4IEUGgrJmVsYcdHvTH-KdHzI9St99qMVtIOq19pGahCPJl_YtJ_U0cPDXrVhmpvSzGQ0DQjoX-vs3ogO1bKGRtQrqTbvDroBVfaE28k00ostm9FRwrg7hJYAuIaCB-1BxsjqY6tUVHQCC_hHr1qS7i6Lwt5RqT68d4LrQdaWZ5Rs8VWTGXYtRy0TTfCKpYY3Jh7UYiAX-rJZ8jMRp0eJ3ilo5gzn3TdIk0lN5E373HP057rKBuPnCPseLsn1-9JdUMEBFehfuzjOzZuUDJgPUnxX46tldDYB4FFuJ-0zgwtB9g1wbD6xkR2SYqiu-GAvsaabjihuGGQysLwM6Fu0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a3d293ea.mp4?token=b4IEUGgrJmVsYcdHvTH-KdHzI9St99qMVtIOq19pGahCPJl_YtJ_U0cPDXrVhmpvSzGQ0DQjoX-vs3ogO1bKGRtQrqTbvDroBVfaE28k00ostm9FRwrg7hJYAuIaCB-1BxsjqY6tUVHQCC_hHr1qS7i6Lwt5RqT68d4LrQdaWZ5Rs8VWTGXYtRy0TTfCKpYY3Jh7UYiAX-rJZ8jMRp0eJ3ilo5gzn3TdIk0lN5E373HP057rKBuPnCPseLsn1-9JdUMEBFehfuzjOzZuUDJgPUnxX46tldDYB4FFuJ-0zgwtB9g1wbD6xkR2SYqiu-GAvsaabjihuGGQysLwM6Fu0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث : دریاچه آمریکا توسط اردک‌های دونالد محافظت می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21684" target="_blank">📅 18:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21683">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ‌ در تروث : «سی‌ان‌ان (CNN، شبکه خبری آمریکایی) در یک مارپیچ مرگ قرار دارد و MS NOW (شبکه خبری آمریکایی که به‌تازگی نامش از MSNBC تغییر کرده و ترامپ با کنایه آن را “MSDNC” می‌نامد) هم همین وضعیت را دارد؛ واقعاً تقریباً هیچ‌کس هیچ‌کدام از این دو شبکه را تماشا نمی‌کند! بهترین فرد در سی‌ان‌ان، هری انتن (Harry Enten، تحلیلگر و نظرسنج سیاسی CNN) است، چون حاضر شد نشان دهد که دونالد جی. ترامپ (رئیس‌جمهور آمریکا) شش برابر محبوب‌تر از آبراهام لینکلن (رئیس‌جمهور شانزدهم آمریکا)، جرج واشنگتن (نخستین رئیس‌جمهور آمریکا) یا هر رئیس‌جمهور دیگری است. او اعتبار دارد؛ اخراجش نکنید! سی‌ان‌ان را می‌توان با مدیریت و مجریان جدید دوباره احیا کرد، اما MS NOW را نمی‌توان! چون یک برند بزرگ را هرگز نمی‌توان واقعاً نابود کرد!»
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21683" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21682">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مرکز اطلاع‌رسانی فراجا : الف.ل، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد. بدهی این فرد به شبکه بانکی کشور، ۳۰۰ میلیون یورو معادل بیش از ۷۰ هزار میلیارد تومان است. این فرد تاکنون از اجرای تعهدات خود امتناع کرده و متواری بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21682" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21681">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1l4TepI1xgzdwIDbbLZr0tDkN6V_mcox8OOYG64eHQsL6fnFCk8rIw62kihk3EQhA8ZsieW1iRxpWwS7umOhb5GVJOldS9SSOtWeqHgI7K_0uX-MXZwsSN-Up79dC3uJT6i3wljL9GSziDK-o6MAhrNdnX8Rkvka6pTzTR453VJCuDlcuF060JARIOdOHUv1GiSMISrd18xdoyeyTnGhN2Kg42RscjDL3_Mb64ku5wM2hRbnnWZKkeR1sZHy6dt7dRJLF24k9RTH0AlS-12BQVchOcE727zKIHlV_THhgJ0LuSAdyvtemdQwhZkqNUT-kSKGDApdMMsR1GVnotPdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت کارکنان ناو لاوان به کشور پس از 7 ماه
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21681" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرنگار وال استریت ژورنال:
هیچ چیز به اندازه احتمال ادامه حمل و نقل دریایی هدایت‌شده توسط آمریکا از طریق تنگه هرمز، به اهرم فشار رژیم آسیب نمی‌رساند. اگر این امر ادامه یابد، اوضاع را تغییر خواهد داد. اگر چنین شود، اوضاع بسیار بد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21680" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvoTz-uL-8yAd033PFto8lqIXSQFNflU_da8Bwto20T6llKYNAC5I9k8di2GHzCNvaMm84GDfP6ZLFP5FPBz1PNr6xNKbrp2iSX0pwB3to9JVHXNO0kaVS5lqlicQE021A4Wc8L5pmR1sVvaIeak0D2oRXrIVQH7WF4L3-r58Bvsn-tVkMKLvs5sCAJxSCIo6XyUtE4n9hZPsoBIeQ63NRT48FfliK2bDE6Oj_zonT0ysmFRLYT-ed4GNlbRf0Y-IZmFXbc5dW2n0FdAvXSlFfudTAlT4aCo10-KhWZuLjdYRUvUn7YTVhohFfmDKMI4wkJhyxpGPXLWqj_xHevpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره‌ای از بقایای ناوچه‌های جماران، نقدی، بایندر و چند شناور دیگر
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21679" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اتاق جنگ با یاشار : شکاف و درگیری در  بدنه حاکمیت
؛ تنها ساعاتی پس از آنکه مجتبی خامنه‌ای در پیام خود به مناسبت هفته دولت تأکید کرد بیان ضعف‌ها و کاستی‌های کشور در شرایط جنگ می‌تواند به دشمن روحیه بدهد و به انسجام جامعه آسیب بزند، مسعود پزشکیان در گفت‌وگوی تلویزیونی تصویری کاملاً متفاوت از وضعیت اقتصادی ارائه کرد و گفت: «پول و درآمد نداریم» و دولت با کمبود منابع مالی و ارزی روبه‌روست و مشکلات کشور بیشتر شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21678" target="_blank">📅 15:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رویترز: جنگ و تشدید تحریم‌های آمریکا فشار سنگینی بر اقتصاد ایران وارد کرده است.
مقام‌های ایرانی برای نخستین‌بار در این گزارش به ابعاد قابل‌توجه فشار اقتصادی اذعان کرده‌اند؛ مسعود پزشکیان می‌گوید تجارت خارجی ایران به دلیل تحریم‌ها و محاصره دریایی آمریکا حدود
۳۵ درصد کاهش یافته
و تورم سالانه نیز به
۶۶ درصد
رسیده است. مجتبی خامنه‌ای هم از دولت خواسته برای مقابله با تورم، بیکاری، افزایش قیمت‌ها و مشکلات بازار اقدام جدی انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21677" target="_blank">📅 14:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tquUf0EdfEUdPpZ-Cbt7SCpD3koaY0lkjEuLrrgUG1rSNGeoK1UDXqFmtZScDl_CYMTb4Jorqz6BoU9cjPhfTCzlwc0_QSXv1qyg_d11UXR6jaPjBIyyKCFryXnQJfscAYQA6vMA-PQKWOj6D7K39wC6mTy79EKBftrMRGp-IKO_3Wu-shoE0qKhZrgO58T6ifJzGKOkj1yM1j1YnI057Yw9bjBqqs4KHvXL9GAEYYFA_vk1stGri29JWCRaEy9X3XZWCETpWa_NwRxM9spmiH2zLRg73TGK_EJWavyqc8HRFnoocH2ELCWTntE2FimBR4xSd5OXQnrmnTksUpxrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب، یک تانکر نفتی به نام "ELLIE" تلاش کرد تا از تنگه هرمز عبور کند و از مسیر جنوبی استفاده کرد که توسط ایالات متحده پشتیبانی می‌شد، اما این تلاش ناموفق بود و تانکر به عقب بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21676" target="_blank">📅 13:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری هاآرتص در تحلیل‌ خود درباره وضعیت ایران، با اشاره به تضعیف موقعیت جمهوری اسلامی، افزایش فشارهای داخلی و خارجی و نگرانی‌های فزاینده در میان مقام‌های حکومت، ارزیابی کرده است که احتمال به خطر افتادن بقای جمهوری اسلامی نسبت به گذشته جدی‌تر شده است
@WarRo</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21675" target="_blank">📅 13:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مؤسسه نیروی دریایی آمریکا USNI : گزارش داده است که ناو هواپیمابر تئودور روزولت CVN71 و ناوگروه رزمی آن در هفته‌های آینده از سن‌دیگو حرکت کرده و برای استقراری بیش از هفت‌ماهه در خاورمیانه آماده می‌شوند. فرمانده ناو نیز خدمه را برای مأموریتی حدود هشت‌ماهه آماده…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21674" target="_blank">📅 13:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نرخ دلار ۲۰۷،۰۰۰ تومان(سقف تاریخی)
دلار کف بازار ۲۱۰ هزار تومان(سقف تاریخی)
تتر ۲۰۴،۰۰۰ تومان
بیتکوین ۷۷،۶۳۷ $
انس جهانی طلا ۴،۴۵۳ $(آخرین قیمت)
نفت برنت  ۸۸،۱۰$(آخرین قیمت)
@WarRoom
۱ ظهر تهران</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21673" target="_blank">📅 13:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الجزیره : ترامپ ترامپ می‌خواهد سایه جنگ ایران را از انتخابات کنگره دور کند به افکار عمومی داخل آمریکا و بازارهای جهانی اطمینان دهد که منابع انرژی دوباره با قیمت‌های قابل‌قبول در دسترس خواهند بود و ایران دیگر این سلاح مهم، یعنی تنگه هرمز، را در اختیار ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21672" target="_blank">📅 12:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">استیون میلر، مشاور کاخ سفید:
تنگه هرمز برای ایالات متحده باز و برای ایران بسته است!
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21671" target="_blank">📅 12:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرمانده مرزبانی فراجا از کشف ۳۸ قبضه سلاح جنگی با اشراف اطلاعاتی مرزبانان در غرب کشور در مرزهای استان کردستان خبر داد.در این عملیات، ۳۸ قبضه سلاح جنگی شامل ۲۰ قبضه کلاش و ۱۸ قبضه کلت به همراه ۳۹ عدد خشاب و یک هزار و ۳۵۰ عدد فشنگ جنگی و یک دستگاه بیسیم کشف و ضبط شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21670" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک توافق تاریخی نفتی دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21669" target="_blank">📅 11:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ در‌تروث مدعی شده آمریکا با ونزوئلا به یک
توافق تاریخی نفتی
دست یافته که بر اساس آن، بخش خصوصی با حمایت دولت آمریکا
کنترل اکثریت بیش از ۶۵ میلیارد بشکه ذخایر اثبات‌شده نفت ونزوئلا
را به دست می‌گیرد؛ به گفته او، این قرارداد بدون هزینه برای مالیات‌دهندگان آمریکایی، ذخایر نفت آمریکا را بیش از دو برابر کرده و در آینده باعث افزایش عرضه نفت و کاهش قیمت بنزین در آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21668" target="_blank">📅 11:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از منابع آگاه گزارش داد دولت
ترامپ
به میانجی‌های مذاکرات ایران اعلام کرده است که
هیچ علاقه‌ای به بازگشت به چارچوب تفاهم اولیه‌ای که در ژوئن با ایران شکل گرفته بود ندارد
.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21667" target="_blank">📅 10:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21666">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد واشنگتن با سرعت در حال انتقال مقادیر زیادی مهمات، موشک‌های رهگیر و تجهیزات نظامی به خاورمیانه است تا توان نیروهای آمریکایی و متحدانش برای مقابله با تهدیدهای احتمالی ایران تقویت شود. این انتقال شامل سامانه‌های دفاع هوایی و موشکی، از جمله رهگیرهای پاتریوت و تاد، از نقاط مختلف جهان به منطقه است. مقام‌های آمریکایی می‌گویند این اقدامات بخشی از تلاش واشنگتن برای تقویت حضور نظامی و حفظ آمادگی دفاعی در برابر هرگونه اقدام احتمالی ایران است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21666" target="_blank">📅 10:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیروی دریایی سپاه انقلاب اسلامی: رویکرد ما در مورد تنگه هرمز تا زمانی که اقدامات آمریکا متوقف شود و این کشور به تعهدات خود عمل کند، ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21665" target="_blank">📅 02:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bchOD0cMFgWlJ403qWzNIieCmTEVPJGL1pBB_K8D7WaqO1_pQusSL1_ubQvmM0_jzDIz-rzbyTMHBsOe-S5ZQZRYK2ri7rDEj9nYExrA7TX1aDLQJB2XVQLxJg2LW4vN24TzYe5Jrsi6GlPrSM0gVPgcpsx3-4RQchqxY7F8NHEm8Zn6tu1xxcGafnyUkhDGjsY5nGYA02zcoAcMJasBE8eRy_UgPF38oh6O3WRToWaHmjq86M8vUFSiXFHzJmHQrUjfl-Tn4uRr7dGi2XzrBr3rZ8gejsZB1W3-jY0Lf8FY0Mz7jJzwgJfw5V_TOUFXiDnd2sKu5xx-YRHsz8R3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهند که یک عملیات لایروبی مخفی برای ایجاد یک مسیر دریایی جدید در سمت عمان از تنگه هرمز در حال انجام است.
این مسیر دریایی حدوداً 1600 فوت عرض و عمق طبیعی آن تقریباً 93 فوت است، که نیازمند لایروبی محدود برای عبور تانکرهای نفتی بزرگ است.
آمریکایی‌ها می‌گویند که کشتی‌هایی که از این مسیر عبور می‌کنند، به دلیل جزیره مسندم و انحنای زمین، خارج از دید ایران باقی می‌مانند!
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21664" target="_blank">📅 00:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتاق جنگ با یاشار :  امشب مارگاریتا زدم
😁
ببینیم چی‌میشه … بیداریم
⚔️</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21663" target="_blank">📅 23:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18d571649.mp4?token=ZDBteUZipVCvxFGQcFrdOkg-oCT_tvopNMyVJLYdleQyJD3Mz6LvYQQfrympvdFGY50mBu0QttvMsdafH7fIS_PNiVG5lRW0h-hV4B9nIX2ebxIcK2a8Rmv-RVjo_G-2Q3KX1pzDTJwuhG_3QYA1Wt6TQDmnc-4PmJjbnRhFtW_9EJ5vaNNYlgDHVSrMciBbIZaLAEG7jME9iGiyU3nyJs_ASwHB-2bnBs2lo81UQmL-YdOJeLnMaBZhQeU6BQU02uBnkRGHvCPKNc2yE3avyfol4RlxnW41bqVMxLSSPUyo5COVxNkMsjZJZfGsV7FrOXF5nX4HOUJqX2q_WVpVug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18d571649.mp4?token=ZDBteUZipVCvxFGQcFrdOkg-oCT_tvopNMyVJLYdleQyJD3Mz6LvYQQfrympvdFGY50mBu0QttvMsdafH7fIS_PNiVG5lRW0h-hV4B9nIX2ebxIcK2a8Rmv-RVjo_G-2Q3KX1pzDTJwuhG_3QYA1Wt6TQDmnc-4PmJjbnRhFtW_9EJ5vaNNYlgDHVSrMciBbIZaLAEG7jME9iGiyU3nyJs_ASwHB-2bnBs2lo81UQmL-YdOJeLnMaBZhQeU6BQU02uBnkRGHvCPKNc2yE3avyfol4RlxnW41bqVMxLSSPUyo5COVxNkMsjZJZfGsV7FrOXF5nX4HOUJqX2q_WVpVug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اونایی که میگن تحریم تاثیر نداره عقلندارن
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21662" target="_blank">📅 23:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9bx312oNWcG8HRIsmjbbCVf3kiU1QCvA7qqQvbUvdgl7NQcqWxeO6PI_FfmiydlAoiH2DAJkf04mZPq9WN4-0Wo9rptK3BfRWghvPwxmDYqbUCdnNjw-ao3M6x3U0H4SLLjMZ_EuQcA9ng3DsdNXYvgNx2_Zh0oANhxwjYgVfJcFmGyIrcckfExabkkQDiiUMjf2zHTWE1ULs_urU74m8vdqsfzTKrnVTNiSHfOcm1H4wN3gS2HnM2qghyvlQDEiF9LLLqWGumt2TcysrGqoeQHSRhqBmqNMn_SYnsGTr8FYchyu5UeOCcE1CLmqkIOS_9JJRwampvJ0oyCr_ejwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق: سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21661" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیدبان اتاق جنگ : مخفیگاه دقیق:
سه تا موشک/پهپاد ساعت نزدیکای ۲۲ از نزدیک مدرسه پرتاب شد یه تونل دارن فقط چند صد متر با خونه ها و مدرسه فاصله داره یه جاده اسفالت فرعی هست رد میشه  صد یا دویست متر بیشتر با محل پرتاب اینا فاصله نداره..سیریک-بمانی
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21660" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مسعود پزشکیان هم اکنون اعلام کرد نرخ سوم بنزین، از ۵ هزار تومان به ۱۰ هزار تومان افزایش پیدا می‌کند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21659" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیدبان اتاق جنگ : سه تا پهباد بودن یکی افتاد نزدیک ساحل
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21658" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t73aESrukbZY28RN_0vkNpIoHhd_caHRc4-lPDN4n2dxtXxuExl-lxzwPRUOs0MPBaaCE9BCsaxFQCIEAL-XmdgvPDXalrEpQ-xjLQH7rU6SUAqCkoHdjojs8FQnFql3c37FydgWzEaNl0vHj1JOHPIQkMM8VsmankCI2_ctInhR1lFrZdfCazS1GZbbCSsF_SS4S-uLTlsZ4_h4XiHhfpBjpPdDNrJFXVZR3BUIrnG8TuLE0OKqPLq4oXk7i4y3MG7uPJL1m5ti1LYnUPI_WZiw1EUsateF_orjFDvs5_D6cpFbtUwHvKqQufS3IgDphmhPApWoOLqW4_c8FoRXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در تنگه هرمز در آتش میسوزد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21657" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21656">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش ۳ پرتاب از سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21656" target="_blank">📅 22:10 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
