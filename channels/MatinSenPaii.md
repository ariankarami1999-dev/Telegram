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
<img src="https://cdn1.telesco.pe/file/DYlWFR5xiahOVxN7gIJODwRMnfhd3VqNbP_f_Yypx05V77Woo3dgcEOoDKVjg6R4XIEKbS3AAkoPzY8RdND69Nno-MuCetZ2kOKLRsef1U8Ip5MZT_eSR1GcMClC4zp495jtZl2fzKNtqXIQ-2BlJSp4-igga6V3gEwr0ezvpNglnG7JkDWr3w2ieuPTpekzWiUJ7WeOiRTAkdKXgi5c0C9CSTcpm83p29MCnIUt8Ml6Gfa-bo1jAFNxfpB6eLQPwHe4n43GXWTddS5N4_KqmCda3WbD46Gk8SoRqV5TNiTIeMeD2IHJrOD0pRy1hGjnGnSjL9MKSy_--GHDNplLtg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 02:17:14</div>
<hr>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OZqsIXAGwVRJd7uxVth6PBrdHd23pgWkMsb6MG7zarN-WCdH2NNBIWwXxxPH_3dpGdBj3RXimgJB_TJ-PcY2D4qvB8JDkABZ2IdXYqBhM_8XCM-riZlfQef53Scj_qiLpSyIuskg_elN3K5PFs3Y2WSqVSBVOklQHvxrLQ3lwEFRw915aJNBzA6VFmT0Hk8EMRYA2jVg80dE551rwBsurRsRSCYkf_z105P2-uUBHSzXp2m9OaQxFsivW3Y4ol9tnVeqzb72QZlG_d7uz-0cklQvdqK3NRzXpoRTCIR4oAIzN1j-1tkLH0ic6JEZGnLHokm9tZFBrM-gA1VZJvRp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EeTN13Z8iIsZfX0Wsr-4hfKD1nnCtPAyS8auLEfPleQgCdoXgdhcS3_1qV2sg9wIdU4Y001l0ugmzfrLUCzy-1FEXPeG5AKNQi-kOvldBDFEoTIteNeM41LTv-DYLVy1vOQnUKoRU9C1Rm9c0qlZgKh8MEK-KOddOOrWceFt1GnC0tXcF2aSZRpss7b7tZvYjNYiGy0g_NmYGc-Rn_tMeXpnr0d6L4J6MhhB46_Xl0-SRaD8sZsod4abpploWG5U1tOnJufaJmbdtAxynbPU0gzIvcf95JgeOY7p5I9qzmxfurUNpB-5w7MnmisCE_BdG8wczCmJwuDdzPNLMTJfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PuzvbKU16cmxiL7GrjizDINjWzrDQxhbD08r-flKS6uha3DHWv_Ecp-VMN9fiJQPpAQcXOqTWC5gyII_I8_tqLYatNOtLYucagRTbm0lbBfN96eAmw_Lt3q5jIHF-7d2jmqM1VkB34M4-D2ul7AHfK0UNvOBEHjyHlPguv8CaC_BfFBA_2_srEH6NZQYTqdTfcV0mpqEyRr1PV6SeJVkZO-QtD3yvFnL4z3XSH_uyMO6C0hcUOLwzicE-RU6uZ0jjHKeHRatonRZE70IeuY4kfNGGxGSIzrPjwdKG5UKSq-mNwYjMym6KqBtC8-lrZ820psxEZdNx5goY84NZpVReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg2DoSN-HHcu1D-Pd7MmcgMbgQE6J9l0RI3XnXHIBtqNMIZKc6FsG4VQFRVEpDjsbKOlIqBc6L8VFqmoG8o01QSWCBPQWCv5UWb6-Q7GAVF5GjkR35j5lB38c7WonHDK-0WDKQ5UnLWt1oTyyaLjvZYkg7guDVjybP7_wzV4v9F2hzfmS5Sq8cp8qMJHDCJu6SNeUKTnh7d8Fdp1ItTL_KsKuq0dPxvMLUNt23OjpyndYr2ikFoSFgFuhoB9M3hzNY7K3pOlh2fus9JsjHm9xvLJ0lz-e2KrqKLv2MBNqyQwPJ2t2jlmtb_p2doEQJKO_4p5ukbdLrVyh4Mqi2ebfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tPaY5uz5tsLxlyZ3gK1rtnsH-6iJXQIm4GsMl0rFz7pXioeYtBW3Wu742A0wpWSpgc2Du9gesKAS9o228q55ra2S3vT4coWc5ZoEcevWXowP4qIp203JU_P92YI0SL2sj3NXF44GyZAYqAt9Tx9yhxK5RMTozox1KsbLRM8KXj2k61evKFehn6uH0j6rkr9NyJa7CPIZ7Z9kFuo1WXdOC8wnX783-z8goj83qbWxOmte-bRR1Unp4JK98508dPtjO_wZZ-V8BCeI7yJhoeQlD9YMtyu9BqVl3vomB9ck_JFG2PiumQ5A4VwCkaPUcUmgVw6IiFRlpeLuX46JZuBPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UgNtUP7MRa3APbKTrh8zXr3VC5EJYaZ4n4ulTwsvJlYLAQgb8n1ye0R81JvYjr1i_SBfPt28ghJSfUFx_NUKj35DiYyfHMTwKKu1QKiQlR9VCPxH4VNeRhGlX5EyXAv7-CfDALEuOi_g-Ov863PHqgBAEMt6Kk2Eql1X8oCujanIHYIrzzxOLIKcsq1N4kiYyYvA_7KEI5-cq1cLBPPFShluUnNPKtKaRj5sDYgpGsSmPPTeaArAZNPcyfNDjEUOM2B_Cs9-bIXCpqBkU5Z3EZZ2m_fWNAX1MEs_Febo23eDFXi2yMTA0NM-HGlrG7fMzzqACZALX_i7Ygaz9Vev4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IeOIbswOX-K1w5FRziQXxbEUv4xArFI3qeWqXkoRZJ_N5-sl_U11cnfyMbG8LwqHuYmBe1nyGJXpk84c8_Lgn32pA0sg1jp_Mc5KQErFUNSrgpuhtkvKwbFNN0BRfLVcyktjX3WtZUh1Kfkkt9NNLr2tS0TKAIVTEjPk0fPiAkdm0l93LnKSNg5Zu4DwNB8E_MmD40Fikthy6qyfKjEOa5XxyJR9DCYjmPLQbiWIFQBTbR-KDCcSIWdV6Gyek2IKG6S5AfB3hR3uxZKrvLS4aG0kgZvgov8W9D56GNpHAMZOfSPZxttOWKxshSrymSQ9pAM9HE9ihQWJTb8Pj3tvkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NP_YWDQs58hVHHKCVVBWk2c-QZC9q-zSXljCYygiaCFUzmirBzKxP2g8q8HlhRtL_GqLqLAcct8oXT1wDcl4yH3hG_Ukcb0h2MkJcXiuo4D6dRzFQamIAcDxqDXxAfUrHevCanzfgTJQgDfXM6YCuHv0zAyI2DGIT0VTKFR8vQE0znxt4IBmMPLWikZ_eOqwYmuBbB6ZpPyVe6R8uZpm4VjdCvHJ1V2OujfsMyOhrRwydOAHZWqCzLSW39n3TzrNYYOlmP6y51sUfqP9l8sLiK5US4FpdOu4V5MQj4aUC2DqQTP3Bt4uWK5I9mbSBas5pnF02Scwkc_snrWLGaljRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_0y3VoObKaTkGgzCPvY1DZV9AtFpdkdXhBGlFP1EOaXLjeFT1AkeD-50WlhdQXjc0j-Ej5OGVgf9bQ_oQKUtrSLWjKrl9yGUc3dKSGcv0CPNS8b27UWEzreaHGOXviyKlss-1f2q0KY2FLsWOAZABnY9VJg549_UGB9JPfx19EUcpV1FZ43hJCy2xkmQdvi89QdwOAS1pCEQNDwT-lqLJTSPMvTAW6m7He0RCRdwQtjEfaVDTCQCZSvQv0pJTMugOqk8zD_FwXHJ0BqZWDlCUF94HaFNf1tA5hcF5ghGNFlNc7VyyiWRFp1CFQW6TfF8lhdjRDmd4ftuQxHuZxqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ry_YIBig5LBO-fcOPOPyBaCak9R8txNXPvo2YH9HVYlc_VURgMDjws98nt_qR2w6WTWlflAynFFckXqo0P5X5TKU7FXEXv5OekL1XckA-f8GExQ7va83IerS6mZUlf7l6Oe8MlEXYFaeNflMm6uSxlM_6d89PvN36flwtPDePQBuo9PUBKkBNceLi8D5tO7RK97EZKj5mAGJvjM_gnZs9sjSplZOozHzy_X-6kHtpCfjw1rngIcYdO3FPJ3P5peBlFkeiaRFnsmTsAXcrXLX5ah00gW7y4N5wvIPqMJ07nzvBKVMpnr4Uh7i_cvpNn9kd1yDMepEyMzkeqkbs--6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AkaUpXBbLD6r1XM6VieCurfvVbw1wZ_W8w_kdcUSPOmjLmHIg4paeExrDcdQp1zJM2enpjngjJGNn0c4hyi2Nvk5b03Ttt-p05jndGCXt2OWtx-Kj4ecGN9YmayRnTxwPc-WQzL8LbEPsp85nYil6F_lf5B8867zwXvjl_xn1rlIYuaG-q-Y8-bW4JX-22J8aHfJlj37j6YcZECEyw7o_WxNLn4r95zpwLgD9ZSemd0bxJgPZlo0AKuX8e0lUDCnxTVIYr2NQTuS1xTZwniQJBt6zW_rTWBYmk_Ml3blrqb9HEbT-0wtg__Rov0O77NBO7OAnjTBiKdIrXz2qPSi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/B2VrrwpxyiymwdTsK1lOTx0gpqsjzTvSAB_JzI2q_cjn7aOBDktBMVyd1nG40X1J5WdRBvz0KyktDTciQAE9g6Ljsj3lKGHl7a7WQq8WwplGkdTIA75GxOMG1cugx8dFbxI4urOEee7hnzVAZRMKmKBsyL1qCk5oWv4ffGo3ZF7OYaEUsBYweLXZBVy_LK5m22ic9IuuVcQk8MT5R110qhwEhyavjWg_JVwoI1rGtfAah3AWPNEKe-pFWoOGNzhnwsXjv4NzcQGZ3BDu0ZDY1VAYeVMb_hwDvyrYPQSQ4irL5W7qOi8Cshx4tQ4FuRty2lilehV--c4UkebvzZLTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UwlmLrXKKw7EgY1hC4iUJSCNGr0yUWU6YYP2kez-9jDFAkocolBre2HULZzLMWa_31TYvv8eD37rrGylXZJxMj4dHcIasp2ZX1GSK7VzGAhzyhKujlZ7fftD_wktpSVh_DnTECAq35XntoWZw7Y7ZkG9ot_7-g1UeAVqkBc5bu-90IfuGXqHkvUfQ4ELjTZKjq_fM3dGGbuFhErfWC4pTOLA_hZkIo78aCJSFpsbEeXw2hjP1k6QqU4QNV9GhNzSIYwaoPnr4Hai9gZx9c8mLQbqzC-Uo5Rhv89g0yvzaP7nRze033yrMcGylsMaXGpyaXhA1Lg6FBbCxgl7omZRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CKO4Mer1q_twtHk4WItMc9y8M7D0WeqJwdRnfRWsIu0FzgK-9ksLvH_VaNumQIXKTRwDayGkTg6ZUPEFttk61oLnHxFRFm2LaN9Js3g-swQH0VxsKlz2BMOzmT4sJgs--k4OQBbpM9iPRr4cAF_T7EnnTD5rSUCuiJ7Y7S1Zk6pvdkwBXhbuedM_-4wz4by2UymEUmWlZmGlv5f0FHCyEbqTfvWeWbgVxrUg5UQBpI-tV5ayCyr7zysKS0Ly98cjpvJvhF-Q_RPrQnZ1NoRY6-PnyXVL_RqgraPRSM740UaYjYMo_l9WKBb7XfdjwA9hdOI-Oxzo4hbMCeZhSwL9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLZx0DTOotjIH9RXXeiS8H-7w6pk0BWx7eWUZq-Sob3pFCl8-GbXBg03vuRmDAB6LpQzqnX9fArlamwLrVGJwNza1cEZqaLdZ9mV2rTxm2qPgrrqqs7W4kWVjlgpnBRu3e2NeXsh3OCcQVnriYHmfXv7ySCI3eNFPjJPeahxZLS-0SCT7zM6yfLTI9C3LmjG-BB1ZZ5ruUFfRDVfSv-mkFotvYTW94jIyzt836B1OpiWFaXZfboWWJjG9Br9ieI7Hgr2rwHBaBIcJlRipAtiHg1dH-6RRGYfqBsaoP9u2RgloccizHiNOrZL1FdJitQBzCkaBMk0Q9jujZALZmcHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=KNd0AMQpv7-_nubVZx8sjANaNJnVFP-Xinsn8roYIz4JEp1S8Zm1L-RYWNIMer35qH1zpq1FjiD2iOM5VqvPPOO8kEsKEDBuT8B_kt1zcVFmyUlhKV_BDtvUVVlU--kSz5hhdTomdTLtIFkO8hZv-QrS1W-60prFD9MEOgtFvL4vScfhS1Pr1RvuQ51kkMpEDUk6wxX1ahb8BeT4OiftWAyNfjI8jFsfCVBHsfdoLEwWMSUtViixIO3Ye7PBvVzNrKcaGdAgF-xzCKaP9lCy3qDSRIu9EyQF1NzuKak9rkYks83uSTwzR6WUYOCWF971Nardhd5n0tTQ_D2FwmA0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=KNd0AMQpv7-_nubVZx8sjANaNJnVFP-Xinsn8roYIz4JEp1S8Zm1L-RYWNIMer35qH1zpq1FjiD2iOM5VqvPPOO8kEsKEDBuT8B_kt1zcVFmyUlhKV_BDtvUVVlU--kSz5hhdTomdTLtIFkO8hZv-QrS1W-60prFD9MEOgtFvL4vScfhS1Pr1RvuQ51kkMpEDUk6wxX1ahb8BeT4OiftWAyNfjI8jFsfCVBHsfdoLEwWMSUtViixIO3Ye7PBvVzNrKcaGdAgF-xzCKaP9lCy3qDSRIu9EyQF1NzuKak9rkYks83uSTwzR6WUYOCWF971Nardhd5n0tTQ_D2FwmA0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuumCEWYEwKZRPQCcIOjUwgEGbWa89Qrn6p2nC13TbmTQzLbfngWrN-DaswBRsovjhuoMLgbWsmcZNiJ5vmcftflQlFbQQ3xaYT0WRw0ERltJLdEAiXjZyHCcCZ5cdSpc5kF7bILKCi5brVSUUU6aszMM9WdrQexefVqTcHNq3LTRKLE2DcJ-5qMxkkpLqOnx8sS6wKk2gur_ZJnAydQm-V_xbrFuRkysl_IMDsZ0U28989L_5gMghCw_hsuZOTpn2P-izs926vVmqr09D7JQYom01qZ93SD6oJc2Wv-g0l0TXsJXfm8CkvHxy5IjA2JLy2fOc1ZJCcvhELAuIlcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T51LTfAO3MH3QYXZtMQi0QKDdelSCwViRPuSLXZLftC8B_KAPwI2zmUY3XtQHwWS8j273wCTQZ9NERp8ER2-wT-GiIvPxpLAcDWipZ5QuPgEY5j3hXvGwa4iEi_yspYBlle9aCia7s4-EiH2ikbgDiYqIsSyXS6RTpaibHjcM9P1TrI5nWcKjg1No1VxINw9G2-KoNFGy0_gtNrzFGXJjgDiLQVEZrOzyl-0WZrq-GPszO6gtn6XpLd7WIKQlXS2r0LyN49fvZ3IYNOWXO97wFYJ0Z_5SS9QQsHVY29-bOjjO0wc_sj__eeSe2EY5bVgtWD0tBjokRnF5Ot51dlmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JW79iGXFLq1Vdz9wYF9bciljq6HVpr_ybA7FNQRermeNcTMgZOT_cruIfkl1GuUtbsBvqMUaocoieUlsG_1XOzWfB78KocGEiPnEhlVt4PozjbIQn0RBUmvWZbgvWiqyXhtWJ8rcJBdLu-Bk9P4GG-2Ogs8jvvAcs-d4IochuD4mzisFhoFZIyPi3DaKE1qLlgWzoqV7OzZozsFLesCaXSPPx6Bmews3WO1uICmWSM-J_bpw8j3Teq4o3SgOHyjpc82FOhr_TBrRSf7xrjye5erya5634ssXfdJGaYunXgPNqDBjVynJlJByaxxXLTTzZKwWb1RvNzeArLci_39qNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PPfb_QCm_7jkDqk-EFg811KyyZkGeJtgrrUH7Qn4-XZ9A9WcvpwqNK4U-_sJAMD1syxIvUVG2YxWd1K1gbrQotkH88zAYW66dKSp24_l4nh7gHkKtt831yJcs9IbkMaIXZIQLmbrCRzge937tis3qw0xHDwqIt3Z_6lS3OLNd3fHlfp6vqcMVJo_ZXTs9E5INEwyYW7u1Ga_tPAivWozE2gAaRvY2Ub3qTi1V1scOa4P4ixdInyEKa1iU_9Bvgn6x9zMnqLNTt842iTI5YHtAIGZ0Zyradv6l3BesZDvep1YXMGIwNavYfMEoKJb10P2DQijXGSZJurl1zsQjxFAwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a6ZbDfkk8t9XPyWHuS2Hy14Xd0dGNwAg97Z2YcV9PFXeFFmmK-J9N0SyVtLQC8ncjFgCBBOhu8ATp6lgI4tGBKDcU7iUgYt7PtoKZT-trhfG4oASLGoWHdIRiNFOr8OOw1gUdNloTJrdfvXg9f1y-1pPwB62eY39An5yyleRvLwnvbvzRlhirNlxy7Rz2SWgAeItlQV6EFy2xcn-u8foF7dfgW1HWDJfZ5xy4JaFPS-sOHUsBNj9BTPHMw3tx2j9w9GANjNyi2tU6cN881T94OrqHEGPUhYiCImvF80Qg7J8MoL8lM7aQMNE1tDvCJ2_YQA3jFR_Gd_Q2jxAQFhF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SvyOWiIruIs9OpghedVU5MGQJLmnsmxONmSjdH6WQCg4QttHPi50Wd3AzhWTbJbu2O1AIqX-9pOlhJZGkG6ZLNzbXPa-eezL1CRl876jrMmSRqgtIRZYsjIDaakqGQv2BLQyeJO1Qdo8FMlFJzwQIz0pISivulx5WyOmBRIZi0V1pUZBJGa2VIEOjrpItrgmucfmNBiyxQdGhTidfz_fZnfd8OecOk3u0WePPStYRF36NLM2Me-BCeh-YBfY00bKJ-egwbGF1pZ8Vx53-VISuoV6PecvHX_WlJvUAW3g1cOTzyvq1dSpdc_vNQeLiMc9nJ3HbkuzzUE61nYsfpofHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aAoKD3RWM_VXgDdYH7rAjP09s9NHMtPqo1_7iSWACxOKq8xgtzfD70HkMBoyIbB8rplz8JolL07KNc7feZmomrTKlb2dO-7ZIR56S6WYUNDxyqLV2nJQtFZx8JeH0JRC1w4guHNUoy_qKz8G73Ndn7-KjXXwtKL5kylvxB7DiCzLvYlPTTpfzTgwUeaGUDM-1wCY_YUUF8JocwHGH3cU4pZUrl1A7n7C9-OotDBTBB5Zg577djnBLa5TsSFkzCbP6G6T_fyrSycygz0K8-f5k6J-FxlixlQ3EkSbfllN7-UkLLCrrqyTqHErlQaaY7TV36bACa5ZjbI7iw92oaO8gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kX5sv9eC-BO16MgrCI_1YEkiDbCsbAoIjBwKKmacyvXYfZYuYjOkWh2Gs7NOgEpzUUtFlnnQ4xqjFdABsU92sqHuLDocVhCEWrvkbg3QOibrb25miJaKlQNvjSEePd_1eJcTrlRwSp0JK1fPN6Rv8OoU1jmEluVQt7ZidpIwnBzuK9R0GOW6uA5U1V4w8N0Zp9rtwRaFM03Yil50U4aR4HWcVuSI40TPDFZzJaBQOJVdN6TcEDjOnsCuYxtjV1PqjA9-cCbIgb8J5EnXsa5kjtjQNJzGoOUvW-225iPhWs8O7_Hp85aA37i-uW4JVU4TouQD1L-9wo7sMWkLAgC9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyZwGzWLW9S4PU8rnVoP3Vv-XfcZllSHNQvEb5F12ALwD5t1sVLfrHGLboCSCEVmrJVctVjZXlb1_WVyo2E-NGguE_EPU_uiIBaeB1IbVo2ooqzSh5xwai8MPZlphfcZgmhtbL3r0nMJnHRc0PiyU5j_9wC97IOj6ZsIxNBQmweTYy75CdEUhY0Cd1d3Y3Nd5BU26WUOtlBhRhEjPMq05LUp0HrERxUV-iBXlwnNhNzSZIkAFcDzCD66M76o04PWUbSwannmhEBeptyrUlM5_1rn3FZrN2mNg1JwFTxY4mEg4geD0N3Fecutz-0L5adCYVP6ImtvvXPo1m0EKhWFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzcuYTid7b4hfruSqzA6pnG-AxmdCgfpAxwUgWJsyKJpEGg2VdTRibebjS-1EP_AQ-pfqiSpnUVS4F0XeKKWxKhZwR-qLtvXbWFgZJDfMqvHBNWYZWI54SPrbsvwQ8HpUBkjegEAicrY9TONSJ7V91PYIyx-e5u7i-DmclONAyjPyXTgdJSMQDU1mUz7Mk7GBEFjUnvIlW5baFkWtfVYjGv4A_CWgJMgrzk6MQfn0K-h2StrbAAGu5Ym54kMh_AnXw1ISe5mfsOpAC8vOJTIM-qP52L1TJ64AKKypB5q2Z9AGmphU_sIIDw4edVsd-1hA33UQB4aRSVnKCPU8YCeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omDJISLm1d_MM3MeH4_Ng0Daw86j6BZV5hk2omsPTKGPGmTnWflwAP4TkRJd6N7oEcAcxHMPAcp-Q-MxEFPRhjqkNtZo-RZpWY_aZFgoq3AWRh9f8qqYgkd3ng1u9vdtTsjOvVGxaowkQX1F1CkaHAPI6NYbAp7mtMhLfSayUiTDqTjBfsONc5WUJLzif6VDh9jRCIHpe785Pcs7KkISj83Wobpoh_4aSiv1FCQxHlufIe27viGRjyXZCsc2qVWMVfeZ6vlbny_oX7Uv4EZKCfXHfT4iyFwL5eJnLndg9E_lWUfcWvGX4eX7jvTJjm6mug_fHSoeR624nG2hHKp33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvA1B-JYYd3hxV--ok2eLX9nKK3K4F1iDVWhUuxFgZbYsEjBnRQxFjxx5bBfgeZPf-kV2rPTy5cpOAGDjERsyuAXwaQ3fH8XdnZEDz_L6EQ__y7qxCrYDKD2-qmJKQfYJ9YOFMFt4BBpaz_Ou70PU4eyUZ74ueK2tqdXSX1MAYdkWXc9iUw_4F67So8D4MHBzZ4QIUTYk-3io2CVt1nXmW1GfxThPej_H5yakuqlpxFnW6BncrKIsuU2C4RaGdvf0F66K3DHoAM97sYv5P0R6G10kludS0StJ-6rIPBp-yzEmmZs21Ea_0P_BwoOtG7ySqY9e5qjU1Cq_D8Sz34EPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KwT72yKVkm2xNmlguwKz0onAtbMG7CrOYVznsRlkrz1qtO6Gk7vOh8xHZKSKm4pm5-xMKCoy23PH9EMPSyzDkM52iqsjXCdIEzDH99cKXiTCqcGzNwfJCPsW7_HR6im5Yqk2WbJuXx7FQBs3U-5ibaKHvgDcOS8cg3FaG_pdcXJpL1KTzwF-I8rzHXOQ0jB0QMTDD19HI7Wlz0NZGk8-lBMKd4SaAScKCdBmOYxTgShNJVTvWexYFrY1gG3LDkU-7QMhOKC_ITBt-tTAYbZbyYMAlceRyVev653SdKLzZC4iNEu_tgTzfBOQ3QMGTNQ5Dt6nMc1SbPrvfPmiPO46DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blNax6TdhWZlzYUgIh0Drw4eAh-DduLRYszlEblxZPEqyBdjuGzw03-dqK4_nFTvYKoU7DfYMVp6fhNOGUXL5C1r5pEWX4lXh-tXiusdfXpb5wR660Lbta0hne-NIvaETHniW47yPrjkiY40VdwKnTxZp9RvfD-qEAYKouWzDzA-vc4wGu6G9O01Na8r4OM-7ZBH7UPUNU2zA0ZFe5xNYKR8U2amuGoTlic-8mM0kTtTLhYZHExPu7tipeqtuLpUqXbYQWvuQwVHo2vX7qRiPjjpFykfTZjLydGF8NvDrr7nMhj2V6d8aTnCI07afvv5_p5M2o3eKJ-3Xb_We5Pntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMMl0FegIVwACpgSGWcjOKuH-CYH8jHvJgZOi2uytC-K7RHXFzByAtfam5fQDqP-KqdJ2AZHcs94IB8WciHg9TDLxzXjpF_piHbhIQzEq9RtKH41H-LSATpkVlx4W6S2JiT0sn-Gq4xHd4sleyfzs9xuf4N9MsGLqk-Iqma-nlLUDZ1glX5MGrlONJB_oY-CoBozoq29QEfZdo7w7dfKZAcy2ozZ1hEBbdjnJu6depLCLTfWyBjlTdTa1_yWoUrfhUGok3-Vr0wwjeLRoiTro4bEMCzRdDGaCBlERc0kBJGwVbBZo_ARjb-nyM1uyWbCAt--5rDuATqqpHZntJSugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SjEH2X2-C_Z36sadduQnAyeNaW6Y5fWB-_mLgrnJznDbwklPKoRLBbii8H9iFPwrvqfdmDQ_mxosrR48kf0uNMK8xm6RC-hz7A17dvqR9KnJcM7zIoVjYU4rLfXbASpNdrhFOS865NF7E9xOF4cJIj_ji_tToS50WsNyBrId7wClu-EhNTycS68OZZOA0mpit7_UZCjR72prfoR0rJmUUnJWwHryUheZAtSdy1fwkqIcusBtDMA3WsF4lQt5m19_UuaUbVn_bspBp7C6V5Yf06YbBPQ7YtHa7RQ4VvZkiGtJ83J10SenPFDIZeU1zfvW7Fx_ElXuugQIWG4cLfP2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DJugLJiIgWTIPTWdWIXkJq8Zg3I9gnogPIr6fUB4u-eETzM5YfVanN2Fczs0tFrXC9OuifW2Xka8KXpqcUaX1_W0oXqXUvpN40j2btDBZsZBGhbe31HqqqXX8w0bt95UVTBgz2doReU-R8RDuYTJ_vHXCImN3mxqC0TNULRp0ZnwCuc9kYNQVctPxbsLtjdJeJh-cF6iLyEBD31DBbTaario0YYhEVv9KDuME0l7sYH97d9HAGuwstYWwTaQ8pRqPGvJWWEs5VBsLjp9nCUkVvAACW7u6FYkwF0MEj7hz2hRj5y24aA_vdj-0BtLhEIrFekdzwDgZ0k3EjVTHyQlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TQoxOKw0_032qVKfVflG6eGDwBSqhzJzFggU6WzIRXImm-zXdD8HyuEp4saqX_zf2eT2BEcS8I29MyvTyQgi1V_3vok93wt3NXU6icd63ZBXfktzlC-pTAdDbXLtkNlz3j07ryVXLsHiopb8CjUYrnXnwfGUu8-f7LQQm7VPTGVGGj4IBz5aHnY5ZzuNOok5ULDf_K_nt8Ib9dTAb_2M5vEwbpl2f_sR9KM1NBcNxZTp2Tb1TidyDr-z_uwilngE8DKNz24ryKOmDQ28Zf43WkgP1xK4O2eVnEDA7tbQVcqa5twuoqPYsz_voTbQdonae3DJjq_oD1c2UQol5v9KHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NMZp_8SleRNF0l6HNVIyW64Twe8saoqkG4fZSKGJ93dZm4g3InnNAzcXQm_0jPN3csaG9MAftKtJpLCufjHB-tNvtbToC91G2ufx7y7LS_GHTfzlGi7rTVn6g076UeQCsBMgQBtRkDQ8uWrDdfCzRliectqTrT-bqVKS0Y5v3_7qVBQkQcgN8Le4VP0rwp61R9eyZwVI_XNbgc4tT08iPza0Oav2gta2LXANuBwmFBJ5ib2uM88Tu7Z756DllBoVPp3hZMrI7rZBYQtccX3ZfmW7eGsumfTbaBy0XhX37azuvFX1Anxca4TJl9ZJZ3cHBNhq4c1OJPcU13diu63UMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E_d6XtGPzUaYaE1zOKtej_hregGaFp2shiAuWU17RW6qlz_BZW4S8VXJAIgq0Nxr99Eqx8qE9wUGvN4jRtMEUDNrV9-BlJ-7MXTG8ao245xMyXfSmqfAAX7ZnxxzHPuV6k1kLxEQqZWTf6rDfCYGYf-H3temfr1JJMKWPDTQbtXOw-p3ziIUQDZAMdNhC4_FPkIIC0FnGgQIkAaFl8lpf9e5QL3f4sgCl4mh0LW3McN2l0vPAQuFeqDqOnSHTmMAFOr33ctq7yyOHPGGo3u2zoY2XDlipgIAvH2nP3jb191MHrL01zjvy-ckACEwseT3N201WnLF7A2831SFZ3ekPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kh9dLRiwY4qKNEuXP6shkS--u77QTRf-n0euaLz05KOR7wn79xVQU16Eep2NBhs5smHuGT3j3dOrytpkG0rqGwezXCQy9YUDKgaHYRrVzkQ0u_cOtieI5ZmbVbtPlPPv9KUvKJXMrCeoVh6AC-kN2Bf8LMPTJUUJPo6iRO9YPFQhAn8Rd2ejJHshp39lgtdnw_Yb6sMs7k-PJN-RZatvDSo6GcgB1gskwzyUv5elfxFbcinLH1DoyzvNZbhysviaZoj_RCCT0yYX05MEi3Aj8yMyKVQtOdSmVMYca41r58wtnbAoWxXYkH3M-lfWqeTHo0rpWk9dBoyo8dQknRjzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qm5FJ6Wxnv3vJQhDbZfozJLLj8u8c2LrWbOLOaLKF3Yz2C2Rirx_r1oQK9ZclclIjcdnQ56Mib79y_2B6SpnA8xAx86_Q_UGV5JjDDH58LSRWa3wJeKEqEjbNvMCK3YRwLX_PrmFJH9KZ1jlmdp7jmna2Nwm3-FCodo14hQfZyYaP-E5P6z8--ixvuyvHAsf5UOEBUugog1a6W0Hg4KCqxiwAk7nK1qMS-39QVSehMhUK1iKrnvMHDKA4Cgh_Dr8jjSIuQ5kdIuBh9gkY9Upo-VPHKn9CcmdxPo4soAYStKYJP8BLI-DGrYLnPm5X9D1VTTkbYxZJtCmqoupuYGdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0ggOqByOkUYJnDaO1VYapssJqhxt5ijyHw4M7d7h5BSzWWRhNSG0TSC8q_YLCh3ekwylcAVixAvfaVCU3cqnt063R-gglNaTPzdEtbibfUDxhrNgd4CXCPlRGBNdHwyKRj37ujiUnxq01LZdlGB177AjtEAjuI3SYzwGRbaQGdyM1pr0rqaTdhpGzbthzh4cXNO0I__BRXxxj05ArVnursEha_aT1wQtzGgHiHABKIlvlF4H4m5PVzUeT_JK1xxF-hitX6zuEda4gSYzk5RlvquKMLTLhKH0SujSrGkAxGKGigfCE07qIKLQak5yxsDC03oU0_Rvve41M_UyvQ3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJQuabflvu8n4Vm_5xsIt8H75EgLOjvcQmQ98sEUCgB4a1OJgrrmkIJxKr40F5KHtuqSx33GolyinrAc2hIjyrVfnYo5N5ZPHjhM5i7XP_HazEBjPbiiMgR33WD_8Xqx7wg1b1j13mH6CtVQ4g1ZRbrrG-NYIh97mXWdfTNptIZ2w07nJAOzPLw8jBGDvn7ci840KoLqmB8j-GZeqMU32frxy9Qja7mSwETojCl6smVbJKPHqQER4ThFKKsKnCjK2wOUuoZgN-5F4QsZz3y5NLIwc_7niVLje3z6yQY81GPU8OWkaw8lwIq-h8J19Uw0CZL3Jo_Ey4AjozpsH4XO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fz0LhQpVj6Z7R-eb_J9dF2YCbbwpFqeZdVQ_BUZwVBNbZ34_P6iX-nNZB9JBzTzM95RdvGb3KUB5n1xvoNQvr9-16MuvM7b7xYKBAnxxl6V3sGsaFe3xqUwUIUn3oDZuiVNJAp_CB6gvq-vHy9TbBGJJL-ykOgYz_bvYGczuVAmZ1Wx6o60YbiPi3v0bh4JFomKim6mBpEb0difO79J8X4j_a1Kxo0rHBEyDjVSlpQOE6zhxWthsu92WHRaMbwWTuH1pSGPXFBzg9e3kYnOnCgF15GiZfTFif1ZHP01-B7QtbFILzM-bnnd8ZH71doo3iUH5a9Wria2EdNaJAl69-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fexIvqrD9zTxwvzeJs_7XuNfW3k3f_erecce5ucIFEeJIIFVNd04uzhUhyY-Q9ZkIu9834AngSN6E0gKWP4XA3wq238OqWU1DhRaKqKCK9oK7yhCWZSNdCNi2_PxOvdkEkB-5AOVGO9394pndArfDBeOusTJNy8PV7zsrUy5mwcLVIvhH70hrOsLZubg-tZ0gbRkeoX1bh_gbGHO5qaXeK4ggIwEJ0oY8c-TCyOhSzyl4mfNzwxPT3X5nKP8XDThec18GCeFPJ4Tr37aCeqWL3RhQiIrFhyWQGYFu1s1SWwdW5zehixkDTar6F1BZrzDY6O2BWXQabuObTJ2ahQ35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/awmLRgdWQlZqgBH3xLbIs38bHYd7qkzjJGoadprzQE8SO0CSr7EaXgzAzx9OGYTPKyauV54OrauIQUmMXHzryh1dlhKhMhFcEzEvTcCj4HvPU9BzyjhihXh1NwE0iaoLAVHUudOzq8IiqLyGPPnleb23FGJVAEU4m1eWxsBTvYnjnwuKrlY8MD5fWS7-a9FmIKFQ3G54E4ucClfka2G5VD6mgBSfSS8sljhAIbDwSF1v18fEG8cSKEwuGXmkmKWUo9mBxZYwQG2S_CzitLwXGfVGapsQTRu9O9aBa2_Tw32f-PNUks-Vqno2ib2gJyFgIWPzc3f3J4dVi4Gx6ilxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uww6lx8DURNYCuslVw3L7tGoItzTqH-xuhuafPumr6LHnn1FhEhDrsrV4uiqWVGEZHFcQqAovLJnsqbZv4rOoGVFU1LFKSOecRxd5WW08kIribq4vFTNzzSWHZ26mRvcqUUZWi_CyxK7XO3MucemSG_WRwew2DeBkZ4svnwFki1_TOqKl-F0F1YRaH6bCITPvPIFwFZ4VRsnN0Q0z1ObsIgVfrAaLpGxo0js6S52GRCY1jx7wvlOvlIRu9Ag5O8KogeL8vYqkusLixN0P30AZMgdXg71GxEqfDbu5I08T18W3BdijdYlQxDBUfCLoaXB6OAZNn5jd4IroFIuLQB3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORsbHocxqT7AbDQva-6XQu56-E7BV310UMPg7bQ9xthaYzTyvJcXlfUS-d0rgLz9SKAK8HATvtv5EVdr1eGMwmEv3m376ZUSDDwoS-tVX-D98jwltr0WXdNdmFGJQbntouilwZO6Jrza3TcSVLujO1wua0nxPz3mcdi-O6XgUE7thsF-wk5PoowdYhasWRiZPpiOFstAKw530usQ9HU_l1pYc3Zhw3fGZx4-4g5cVhWWKYCs2hO3ipKq6fSU9DXcDgVUPBosVy96hLT08PCLLdKnuzkuC0JEn9ZgJuT9mamGzKXU_WsMcUbH7hlRFt80aXHag0vb1H6EJMXqOKBgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان، یه توضیح مهم درباره پروژه X4G که توی ویدیوی بالا معرفی کردیم:
بعد از انتشار ویدیو متوجه شدیم که به نظر می‌رسه بخش قابل توجهی از پروژه X4G از پروژه RVG گرفته شده، بدون اینکه اعتبار مناسبی به سازنده اصلی داده شده باشه.
🔗
پروژه اصلی
(لطفا برای حمایت استار بدید)
https://github.com/arvin341az-glitch/RVG
✍️
برای اینکه از سمت WhiteDNS حق و اعتبار سازنده اصلی تا جای ممکن رعایت بشه، این کارها رو انجام می‌دیم:
- اسم RVG رو به عنوان ویدیو اضافه می‌کنیم.
- توضیح مربوط به این موضوع رو در کامنت‌های ویدیو پین می‌کنیم.
- لینک گیت‌هاب داخل توضیحات ویدیو رو به ریپوی اصلی RVG تغییر می‌دیم.
این جور اتفاق‌ها متأسفانه توی دنیای Open Source پیش میاد. ما قبل از ساخت ویدیو با هیچ‌کدوم از توسعه‌دهنده‌های این پروژه‌ها در ارتباط نبودیم و طبیعتاً تشخیص اینکه یک پروژه از پروژه دیگه کپی شده، همیشه از قبل ممکن نیست.
ممنون از دوستانی که این موضوع رو به ما اطلاع دادن.
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4883" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=qe1qleGsK7qNyNidp0GX6Oa_ICl9jBHGmAwk8CUrCC6mPuibIkcrJduCU_2rO5NW25KomDQOWavCwyMIGBASdjp-w-a1jK829-wtSxtbpCC4qqUKenxMig_d64o7xZupqWllVjtCkMT-3-xyNK5eVwySBCFRE-2nCzC8S8A_CbrJwHUze4FdDZPMscp5_nm7V70ktv-siWGImf-3HM7WW9I1PMc8zCVAL0ZZzljqRoZ61McRLbd-Hz_GpvHqSusDhpeZv4KO9kIK-ZDOXVH80Il8D3qdLov0d83yem8yN2twvPIZvW1rGcZ6WlbMg-EqPzUkU9CozYp7q5SUeXivvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3382773d8.mp4?token=qe1qleGsK7qNyNidp0GX6Oa_ICl9jBHGmAwk8CUrCC6mPuibIkcrJduCU_2rO5NW25KomDQOWavCwyMIGBASdjp-w-a1jK829-wtSxtbpCC4qqUKenxMig_d64o7xZupqWllVjtCkMT-3-xyNK5eVwySBCFRE-2nCzC8S8A_CbrJwHUze4FdDZPMscp5_nm7V70ktv-siWGImf-3HM7WW9I1PMc8zCVAL0ZZzljqRoZ61McRLbd-Hz_GpvHqSusDhpeZv4KO9kIK-ZDOXVH80Il8D3qdLov0d83yem8yN2twvPIZvW1rGcZ6WlbMg-EqPzUkU9CozYp7q5SUeXivvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش ساخت فیلترشکن رایگان X4G + پنل شخصی
این پنل تقریبا شبیه به سرویس BPB هستش اما روی بستر سرویس Railway اجرا میشه و سرعت و امنیت بسیار خوبی داره.
🔗
تماشا در یوتیوب
https://youtu.be/8G7xioYZqPQ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4882" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست قابلیت های هر پیام رسانی رو داره:  - چت های شخصی و ایجاد گروه ها - تنظیمات پیشرفته پنل کاربری - پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ  نصبش ساده ست و با یک کامند انجام…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4881" target="_blank">📅 13:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZethRise</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1uNxIkMQ-0JvdssN1GQ2Vhb7GqIrRN5uM-kNgdutiSkgMtjzJvC218vIdBss6cWFN9yTxN6eFt4fstlAsMueQpk-OsYSu9nt63ljyboSbuqsiWHb4AnMPa0AN0Rp_iWqtrUWjlCMYfaqpiCMmrK_XVa8Ru_ZQ8CjCxCxP2gzFDC9dLENAba3U5D5lmcdXg_yfsyYNpx6Xp4g8GjR69YddcUR12q0HY-0_4tsDZlx01-PTRz9DL499Wtu46eX9WD2dArXE0sW1_Y0ALllw8jf5jnRY_6rRhUvIS9mtSsH_D4Kg0LmgWcwilODH4GtC_EIJRTIEeX92yEP6yMjdWh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلفل چت یک پیامرسان متن باز سلف هاست هست که روی سرورهای قوی تا ضعیف قابل اجراست
قابلیت های هر پیام رسانی رو داره:
- چت های شخصی و ایجاد گروه ها
- تنظیمات پیشرفته پنل کاربری
- پنل ادمین با دسترسی و کنترل تمام قابلیت های اپ
نصبش ساده ست و با یک کامند انجام میشه:
curl -sL https://git.diastom.xyz/ZethRise/FelFelChat/-/raw/master/install.sh | bash
و سپس با کامند
felfel
در ترمینال سرور میتونید اون رو مدیریت کنید!
درحال حاضر فلفل چت ممکنه مشکلاتی در UI داشته باشه و همچنین در backend چون نسخه اولشه (v1.0) پس اگر به مشکلی برخوردید توی ریپازیتوری issue باز کنید!
👩‍💻
Git Self-Hosted Repo
📱
X Profile
🚀
Developed By
Zeth</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4880" target="_blank">📅 13:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دو تا از دوستای خوبم امروز همراهم اومدن و اذیتشون کردم و کلی تجهیزات گرفتیم
🥰
🥰
به زودی خبرهای خوبی در راهه</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4879" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔵
WhiteVPN Desktop — نسخه ۱.۰.۱۴
🔧
رفع اشکال آیکون نوار وظیفه (taskbar)
در نسخه‌های اخیر، منوی راست‌کلیک روی آیکون کار نمی‌کرد و امکان بستن برنامه از آنجا وجود نداشت — تنها راه، Task Manager بود.
مشکل از حلقه‌ای بود که پیام‌های آیکون را می‌خواند و روی رشتهٔ (thread) اشتباهی اجرا می‌شد.
اگر نسخهٔ ۱.۰.۱۲ یا ۱.۰.۱۳ را نصب کرده‌اید، این به‌روزرسانی را حتما داشته باشید
📥
دانلود:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.14
@whitedns</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4878" target="_blank">📅 08:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(Dᵢₐₙₐ🍓)</strong></div>
<div class="tg-text">📚
آموزش اسکن Resolver و استفاده در WhiteDNS (cottendns)
اگه دنبال یه Resolver مناسب و پایدار برای راه‌اندازی WhiteDNS هستی، توی این آموزش قدم‌به‌قدم نحوه اسکن و پیدا کردن IPهای مناسب با Clean IP Finder و استفاده از اون‌ها در CottonDNS رو توضیح دادیم.
⚡️
🔍
کاربردها:
• اسکن و پیدا کردن ریزالور های مناسب
• بررسی پایداری و سرعت Resolverها
• استفاده در WhiteDNS
• بهبود کیفیت و پایداری اتصال
📥
دانلود ابزارها:
🔹
Clean IP Finder v1.3.6
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.6
🔹
WhiteDNS v1.6.0
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚡️
ابزارها رو دانلود کن و طبق آموزش پیش برو.
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4877" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
