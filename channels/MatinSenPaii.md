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
<img src="https://cdn1.telesco.pe/file/acn1yKUn9-mWn7q_5SV0YkGza0r2z8nQpN4nTTwBxhl9ULHCwVvtz0XQ3vfBBKX8d4WG-C1DavZSq_d60XOXm3UFZ6-cp9WyB5ef6o4DHxGk_gWLyT4vvPHSGXIAtt6n3ORnoBLDUuQ_UaofCqEMOhYr148yehUj7zGpH6-Ts_wn1Z8AZ7zIAxux4XaMVu9y7EYXU-JO1W5pLDxrgkMz0k7M4-UYSSuYRRkGGI9dFsnIBbJvyx0suElmP103mp-a7MlTZZ_ynIJd8oNVloLzPmEEXOEuez6S4hacARoMFrENuiq8XK4DyNwG2d6H73HXLW1Qbe5trwvVIeNrZftSxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 04:34:08</div>
<hr>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TLtuonlPDbzXKB9VmqG9ucQ_5JZ4s6Wj3tuUpsAKSZqNnhAj0w65o6tB75UMKhYsa0yOPjnqntngB-2ICkEroDxq_M6XHmpNfwTE7m3otHdKDcwVyKNhMBOtXsbbaqQLFK1Gba_hzwvKFtjeYqk-ViASEn3MGULdjvYw-SOSGPRCR6mWFOLqdrd5146lE59Uj-x8aDc8WUeBdcvfJPxFyfKWMCEK_Q136-_oUiwIrV0oh_6CbSziIvNSCrqA9bgm6MHEzr89r3yztvuO_xRbTy0coaMQv8J99ti8Cf1yyd5HeyDR2hrp_anprIl_GE_Fe8Nz5Ht4PXWTiVpo4pMYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHOuikU5M7RdaPdjzHJKXyk5BCWDwFK8E2cFwRcZweKFXq-DBPb4QvQ3Vm-q4y6vVriz6h6j7QXCrsl0QPceGg4WExopk0nYr_ptb-n46JLauwE1GyNnkGV21X0U_jcgmHDW0IRPYzaH5cjch9yElS1t_XDDw_eKFpHtXeR1j3ERmW8wCyLMfBkxc36Hv_lvJX-oqPK0pfTsND-wymW6FHPDbA8GJFFsJ40XEDsR1ZZUKtganehOJjV5cOxGrGSY4bvX-uKdSXjZXSGiIkS1BHcJpU4cdeJ7t7tzsZCu0ZhWZsU5WOehkFVUSjAD7jHdRDyysWmlYjQTb7H2TQgFbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dcHLZNo5_FnbioyqWjh8hbN1CrgW4A9jCroM2tGjTJIi4f3YWQ_ipzIrKTxJwEpj7-6gt4jdR8v4kwLGNuqLrmGVoG3KbcFNyR8f4pTHdmd17bfb5OQN1yevXlqkuN-HkyUNjxCfgvHQM1altXACoGqt1tbNheTD8wpyA-1FS3pSUEopmNaC1L2GmM6XLfIst41Dp7CgAPBuIWFMEuuwjA4al8OCoAInz2ch_nZ6M5NFK_71aT9Ff9wxQ3ISPbzx3WhHP2ll8y76TOkbfNRmx8kVF0yKG-vg6pdKd2BeP7gn02Q7wTBZBWKD8M3X0MnY_24bmY1SINJyMl7BSjFuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cuZTwHtmlBveyGUR10gAen6eDGD9soWo_9qP4MFiWpzrjTg9Cs47Phlmr1y9t6NYQzWhNuHc8rc_4OAhJTOPctytyC-i5xJf1EagoQtZOw-h97fAPgXn8Lf6pp0dKH1bQBa3EZe5RDz8COo_-eyTH1m_32uzHCo86S0oTaf6N34hFu2nu5ag234yx6RuxUBApOOxt0tQdzU082sjXYLxHntvFzJSfLqAGdQzH9SsDsG1yD_6Hk8LT_eaVcuPAqj_-UpnyT5YmfOHqg-9Lg5--IAYwNC3OXQhylzPtVu1kX1yheobBjhNkHrZ8TqeXfvNW5pu618nus74sOmlFp9a0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ0PPOoRyz_2DR1a6RLRJWP3FACzs3TzBp2bhi-IqyyktgCLBYgH_MoADNNJJ-C_HWrxNtPhJ0xi5t-2-WQmihdt-LD9ILKIN2er_Uac03-6lLOzqtUtS2n7agSeNFVgAIA4Md-G1AO9rRsh5Bp0XrFfzfWUJiVeCrRDIxkCburN0OML7Nfee4ZWhVLBsTHyIp6HPzuwguq1-aDqnGAMvgusmAFWUVq7Xv1IKRF6ugXPzqtH-ZmNJZ84E1RXnXGgd8_QI66v-P5OcYggbGvwpAw3b0KcfD_uj1Baku8exCcqmjtTX7n3oFLQvhbxZ5-Rkfx_1kyarC-t1-AhmD1Pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2Oalzj-10cHoEOhwBeuDjvhwK6uGzCBxOQTBkl7Nxr34r3Q3tzJid28CEZP-uoQ3WvfdttZfE-krb9barcsCaaf9XbuGzjou0wIPvkg_mFyVvp5okrsdEwt5t9k4ondAqh3-kHTYKisPeDkk2ADwJnZyKgbfgo7YNiwDDhMEPv2yfwFfBuHsDbh232xJOYnJXpQOpPYdiPbE7hBelIvvl7nvq_WQUmdfpgDm81GMhvw17UYaXg4X3zlBVbPhA8mHugEDjM1Mw8VBEG_9TOlotOonp0CxHjMaPjD1tJUAs_Y9Rf3TZjY0xUDLAlIoiCmUvq-8xqXwQYIkv8mKA-9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CfiaxpbaOWjWYSqVtzctp1vvT3fH9ENxGOZUAf0wl4ij2s-gFHDmA0ntkYutCo46ci2F4ecFfZXWczdVRXH0LHHNV34jgesVqTGB-oUIautrQh5ogtrEAz8ZaFOPM766nHlLcAQFWm1RQd4NlHeV-V5rqPn8KCKWSk7bhXA2Eql-JYwq9G7UN67wjZ6oPcDWiV7mJIrH5GVGWAkX9lssUc31felAFT46tmNVCx89nHh4iNZGEmji-F80vaAzLaVhZFFRcYUAkuZJZ45qjSY13lvJBaNb6FIQmY_JyTyxd8K4Lj3Z6ghGf1KpFvbI3YHioVJlAB6U9KaaQ2X-DMazsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F3gw5OwekYyL1Ud2f1Meu4am66V3k77pKMWmL1RQ-9e0ri1W6HFimRD3XNngUxpsHa73J0vWIIz3UMTRHDBRhdh8YLfV4xXgglMyEuJJK8Z1NnTwjUmHFKkhc2D3UqUqfFnYSKsIzypz9RYWsEDMgku-ooE5MtV0jUmetHoVb0zwReLh23HQ6HpWHJ2QB0XpoXC58ZaiFDGKKTt9ARwgpVH_qCiPurOoSRfNd1eT65C6wt8WD7gHzlCBCLTx4u2F79ek-P3CsnIM-BA1yHWMdpFaUCJRsJa5wXPEt9pHwXKyBl3v3ZOuL12qm1H0obNJEw9F87A-xmCNDluAirsZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s06qr5VH5dOHaPgYuByob-e9MVQRI7_ZfpOPEp0_eUsKlJ6T00Hfx_Hcx96bppVXKfKbCdAksZR_NxELCItYJWq4a4_VeX-2qS4Ue0fo9MjXHNAHDIxr-YLvuT3l7cMa0AQ9cxCB5-mF60d5KVsMcqIG5-_Vu2hQwJvV4OJFpZSXFeYCFjh2QHTBE57aeo9L9CdxEI4M2fjHfGBOESb8cJGUhh8ku4ghEx5uwGL_3GhYIM8CQtJVvsHd_bGphJ3oIDP_PfqJHGYbQk5XaiWWgODnU1eZY6bwGXNV8j2YqMX-rbueoUy6xDw1lFqAz6w0hEzj49CpSfDcAaDXJSQbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hcoL3blCfv3zHeZU3sWEu4uGtwkQfG2_qqJ0VZi3KY_CIyY1vyfvQIIPrJZANlyv2nexTnOoNFYDU_qCUscocKO0y-ogyfUNowt8qMqkxdzM_ZjtxUs-47X9d2mXJFw05dmCk1XxmpaRHKltxV25u9hWXvlAoWGsjyKnDzP_cQqLaNzculY9nDxIEtAkNUL5788vp9CDTbXtrKEPn3x7FBqyu4mJGP2oQ9BkA5_5RLLwW8LkmyV0Yscgh_vnW8-8Qia0c2eFygw_t6ubeJk3mJtwVducik8F5_UyU2dMqeUOLG7Cl1z83fKg50EczrFz4f4414k0ViZkQv0Ga9Nc5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUPfkOUA5F9Q5BNoF2-gQ8RdBrDxXtVXFMmFdzjZ1hbBTDhzwog7mPaBpR_1JLozMqRuyoUx9IRlJg6H_c2DkhCGfeRDiRE24Sc-t_ZV1x9f-G0PBcaVJ1ranDjf3kygWDIbwI9_3mFR0DXfiqhmEBnt4zdJmzQnv9wQ9WhXT92pqOsSPmNDQgRFu5XFpP2Gro1M_l7L_fCrUq4_C_Yb9hB3AOl4zsPTuf_1oL5Yuj6P5CjbTT7Ud-RdqzJKsSrfV0EyM2y_zrsv7UypP0SrP-2NKD5Q9KwqMSudPD2u2vdlYzS2N5C3dmeJPbZKYdyn07HwDqdnLqdygHNCjsO1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBaSL9MK-NxBl4szJ8mCTMbR1SgpUVzMjERoXEfX-u34DMfRPsRiuU2gtqyfDzHH5VzXvKH8O2__VY7GaO_aGUye81cKYjYwRgJqBdDrlgR_e10AyKI0TM4Z0anofNU8uqBjLO8sLlEZX2GLW3Lgt5vP24-AoGQDhtHnf_ZNfDfY8UlyV7lAHCb6_eqPAxRQtmxFPrCycpedhDFh0MpLxLzMbMjInzrOJcTDjIjBjZfm6CVrXtn6VZWN8s_HZEvtIa0XuLZEZEzoG523Sz-v3mRzQuz1SnzeNpddr41YThwOHxOv3rpQs3h7BKL8XojsLG-u-Ev99Gw6g6WMpU50AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KG-SDxbJneJ0a6d_s65NjEdiu6A2zqzIJznHTZ7c4CEYVbKhOUnciZNiTaXcBHv0G_dLbcgVUei7Mw7M3SdfLP9tOVh4pJX85Anxul7uRSbZbe0xvYYZu4X8yeGP0GaXLhRbRIvrckr8GfQDvsogMYU195Z4ykcF9EOhqGdqFfx-LjPw9ewW03r9y7Nn-dFXTzBYQw1bYHRf1DqGq_yplZweernj1qzJNNWl4cLS5OVfrNGV-G5YQx3f0vC-FciibKe-DBz-02w_9gsFwmq-ihkmbR_Yps0p-qYVPdGv_5aew0AEIylb4ibukhg9x_JashjaM8duYT5LpuOaX8zKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8vOtAR-fwwdwfiIUqBr_K1XNPmCMJtwHcoc4hpGuLkHxAW7wGUNjITn7Yg1u0vXbpC6lEJaSDihgDaUmpxHyX-gGjvDftljEEODPpZC44PatGqU59uxPhyDTS5svbsRluoSitkCV-v6CUvRLJG2vHUlKhQopFqEFV2gMM1AJSH89WAZDs1-NXs_HaKCvcrbIrBWZO462jDj-vDVlWutKzDJvgA5jdluG0AXo7WbNunQuhyvyqKo2VOg_9A7bz1ZsUi3WM0mA7jWhA5u_oFXCUw9uD7Oy8C4fFFbMlsevXVmeNb1vOtZf5IYuhBuJxiL5yY1b4io9UZYMEM0cfyOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qEZXK49JxwK0LU56x9xnWx-7vg6Nae1qP6qnlc3epbKNRZU9K1V4fOdzUrLRl9FvOFXJGauqkDwviA2DIyE5nYz2WQJ0tZxI3KEtiQUnGqoMIulVztao2ucMyK2FFyuqwyLZzSxeJF59KJxAUfQo3VvtsI3mECiR7sEY_wP3aCkJyoxIYbEs_L8pIShfmKEo09mTs_Gq185IGF6c1UvPMQgBi6q5d40XgkxyL34sbVb_Z9YF-yv1V-ZgehvJTJnPlckxW0Ix7ogRg0qL-ym38PWvCQ67aDtre-2k0mR7CO-BUoClqgDR0KmSa1QuBvV8yI3gIK5PSStVRd7n0e9J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RWPix8TCNs8-RfDm0GsLCnXF_f5U_mOrr8JwON67cxTIgQ1wfPFh_aOjzFAq9sVnHBDX1TwVxYa6AOpwxFI7vb8RwohBbHon_Dy6E_dVKA5ZJAvBQI0CjhOA_2q5-K5rZQlGh8Tbo8zAE97yJkHMwzTPgphp64AJeQSaFGXAmtpXtJE2mTMp7-0vscYqtEvP4CyGGkcrOqjKZ_NFp5hpr3WDAgyAFuzoHIQaIhVQUmvzKpgPTusPlG6TGYkD3Hu0cZ1P-2TQpGq5vS185me3BzQl4pLDD7-oekuJeHstn3Y_R5S88xgmyjtO2ZwIQWKJwsCsPnNYXnRKvdVXZ3tBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ppCfAcaA35vua9fdnaeE0sCTFFpOGPlmy38ZgzrzNOwYs4l1oTZsQ7ZktHXAPboLaJ4UE10x_n7BtCvUgKXEYEdk65FCiYTA1tiWm0NHI7nKr5ph8JEd5TjSbIT6CPaWftXNLRf7M-dZorU4EvI1LQRCcVxWrkwkDkhajtPMFVuEldo995hOwP_gKZaYRsO3MieQ3GI6HMBAyma6Drodf0eSW8j_4zAKZquDmQDUWZUwAdvMpDhN5Ce4hPBrbGTgiaFbYRxJpH8vT-PmDyZGX53tI8WZMR_l4T8LZozDU1d35C14tl2-ZT8Z--_bdf-VVSaCv8McAlsCVNo6gzu64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ehMoTvvSSTlUi02F91qpH-2RJzMV4gR9m8OeNL-Ir4InW3rZoXXBLISNk1i4F8nTm3g3ztHD_siN2HanizbR0YKz0eoQgBFvRJQcBJ_92GudP3PwyP0iSTaewQdhBTe_g6uoBrRuSMWwX8aN27ne72ERCI6PkuhPD8ZRtWv8i9IHwg11rLZOo5QXSpMwwltD-Tr6kWHAXTH9mkUrdFSYES-dwZgcAm9GuXheH3pye1Bd0dnltFUZ0tt0vkKbDdUKyHiiqEid_rbAkGW5TjFUHcfjDwPPXD8a9c6pT8w-MDWPp0eeaL0RWiYDROOfVSwjOFTMRPjhQtMmsA6LVEebpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=Sp0TEYwSPB5WWDlfha-gSbp-IVbQmALe8yHehldCydLav6w3S9HzvgYlYYJr6wWEPl5sfJ7nJPkvFw5w06ftlz0Zakvz6NDhe7hVghVE6xf3cmPn-nEVzr1ipujzSUnmMwVWgBo2wJAzjuzy_D2NDV_5fhDaf-7qIo25rxpY_lhNCz3ZmPTzr_kuTZva4KIb1sjqnufu6qAsBw1aMrYq1dwANvPdSRP-qfEDq2lfGcVtZHm56lEYmOryagFXgvJP7-Z9ZrMFRyjdJejOnBj90XxW_wsS4F_uRynfTKhfzoGI7Z7C5ICanI4c31vqZyOPamO5bIRNU6L_DPOaQ9rerg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=Sp0TEYwSPB5WWDlfha-gSbp-IVbQmALe8yHehldCydLav6w3S9HzvgYlYYJr6wWEPl5sfJ7nJPkvFw5w06ftlz0Zakvz6NDhe7hVghVE6xf3cmPn-nEVzr1ipujzSUnmMwVWgBo2wJAzjuzy_D2NDV_5fhDaf-7qIo25rxpY_lhNCz3ZmPTzr_kuTZva4KIb1sjqnufu6qAsBw1aMrYq1dwANvPdSRP-qfEDq2lfGcVtZHm56lEYmOryagFXgvJP7-Z9ZrMFRyjdJejOnBj90XxW_wsS4F_uRynfTKhfzoGI7Z7C5ICanI4c31vqZyOPamO5bIRNU6L_DPOaQ9rerg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4754" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in #Turkey is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4753" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNetBlocks</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGk12wwVuIwldeYmkU5pBgBS4KVWyWjdBQtNMYmYqm1dYO1a4xVFP48mx6KisyJm05X2-GvPAnEUAkXBzOqFb1eo9_v15NyVPQKkqKbk7QyIBwge324E6cYYBPmRBbRxJkBZWG36RU4aSRYRhdysbpuWZqRWg8NXr4EZUn8DuwwFRIrrlYNhO6Pj83vlU582H3wp0ecjCHhiVy3t7ldkUhbjF75Bkln4PSzt7uPIJN3j8RsnWQmNRRXX9UqqDLGjoFJ2ndVsFcZjQRkM0WYTZLGMWnkwl_n0e_bqxajAwCw1kvDAB8YbbfJZiecKXp-5Zk45djOl_w3-5CwEqK1D1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
Confirmed: Network data show that major internet provider TurkNet in
#Turkey
is currently experiencing a nation-scale outage, corroborating widespread user complaints; the company says engineers are working to restore service
📉</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4752" target="_blank">📅 14:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=dBffmIZBLT6mHkO9T51Gx1tTvx0bWbnnhngO3ezwxqBzyBrzhAm0-7dr1BjuQAbmX1Qpki9szEOj2DcdNolM5ESAAcCHUBvqNeklvPHIv3hF7c4b7_o3OenreeADF_xqsHDO5dxUN1S3TH7gPBQux7tOy01ZXQf0iUy0zJO41g9ZZGiHFNzDXUtu3jY6-AmBedPw5HA7vKJRmokQVvN0plxl5O09ndQEm8P7v9N5-DiQ-YotbZ_LiY_rVnBZi8xNDqu7vu_AC9HlJnTbSpjVaKVG7NXPTgJeBNNV50b9LqemU-a5-X7_lNOn4VfrOndieTipHYBppAG88cgybh-vJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a9ec28d83.mp4?token=dBffmIZBLT6mHkO9T51Gx1tTvx0bWbnnhngO3ezwxqBzyBrzhAm0-7dr1BjuQAbmX1Qpki9szEOj2DcdNolM5ESAAcCHUBvqNeklvPHIv3hF7c4b7_o3OenreeADF_xqsHDO5dxUN1S3TH7gPBQux7tOy01ZXQf0iUy0zJO41g9ZZGiHFNzDXUtu3jY6-AmBedPw5HA7vKJRmokQVvN0plxl5O09ndQEm8P7v9N5-DiQ-YotbZ_LiY_rVnBZi8xNDqu7vu_AC9HlJnTbSpjVaKVG7NXPTgJeBNNV50b9LqemU-a5-X7_lNOn4VfrOndieTipHYBppAG88cgybh-vJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
آموزش ساخت رایگان، شخصی سریع پروکسی تلگرام کاملا رایگان و بدون نیاز به سرور
https://youtu.be/epG70Xl1xGI
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4751" target="_blank">📅 13:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طبق گزارش Science، استارتاپ‌های لبه‌تکنولوژی مثل OpenAI و Anthropic دیگه مثل گذشته دستاوردهای تحقیقاتی خودشون رو در قالب مقالات علمی منتشر نمی‌کنند. این موضوع که به خاطر رقابت تجاری و نگرانی‌های ایمنی پیش اومده، باعث شده تا روند پیشرفت علم در آکادمی‌ها و به اشتراک‌گذاری دانش توی حوزه AI به شدت کند و محدود بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4750" target="_blank">📅 07:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یادش بخیر، یک زمان اروپایی‌ها فکر می‌کردن مهاجرین غیرقانونی قراره بیان و با گذر زمان در جوامعشون integrate بشن
🥀</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4749" target="_blank">📅 03:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چیز بامزه‌ای شد Mimo 2.5 free + Claude Code و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4748" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=gMuubm4cOvIeuvduO4RHb2cOV8u0FbbJbvM3MRRCPVIH5PljvMDu2IMQn9cfq7V7gkARnx7SxAqIgEw0wYEZRc2OFEbtBvml2nsxU3mndm-GEEUSa1L9s7BXoprAZct0K1kp0QN0C-U2LfUIUepwrLCz7fmwSIz1GZ59AkdQLxm7vBgFYVsc1jDrdMjzJM6CebGgsBMNOuR8s4ROKKUqFTilk2eV5WdUK5Sew-jzTOgimYSm_PRORD5B1HAvlqKu_vLHNcJzHnF1FdZMEV21jffw7fWN3DqjwnJZDTMLcmM_su7Cqehs5MvI9xqp3SvPWI_GZJJaFI09gYtkrxzbhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f09fb91ef.mp4?token=gMuubm4cOvIeuvduO4RHb2cOV8u0FbbJbvM3MRRCPVIH5PljvMDu2IMQn9cfq7V7gkARnx7SxAqIgEw0wYEZRc2OFEbtBvml2nsxU3mndm-GEEUSa1L9s7BXoprAZct0K1kp0QN0C-U2LfUIUepwrLCz7fmwSIz1GZ59AkdQLxm7vBgFYVsc1jDrdMjzJM6CebGgsBMNOuR8s4ROKKUqFTilk2eV5WdUK5Sew-jzTOgimYSm_PRORD5B1HAvlqKu_vLHNcJzHnF1FdZMEV21jffw7fWN3DqjwnJZDTMLcmM_su7Cqehs5MvI9xqp3SvPWI_GZJJaFI09gYtkrxzbhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیز بامزه‌ای شد
Mimo 2.5 free + Claude Code
و مجددا بهم ثابت شد که یه مدل معمولی با harness قوی، از یه مدل قوی با harness معمولی به شدت قدرتمند‌تر ظاهر میشه</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4747" target="_blank">📅 01:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QcYdbE6bCQW4snJiYriTHRr79iZPz0sCapLIzamSRMc7_WRmz-YdtbmctUwBdKqoHcMjm0z5Pa9sG6eLkwtejWZlY8EoXTHkm5LpaeBmxOgq5K6d3YSQrJBfjsrikIGKNRJHK4MzEmwC7aoauzuiTCeWyyJGb9U0DthATC9wZwtsSu1reYtBCOezj-be66OYKDQw3PynXNskPyKFGLqq19xDjKXkfU0GTXPTmaxKoMkiR-f-HghB79pr0r7dnPWvkJc4aR5ZuJNKpmrqT7xAmpMocQF1Aq-lAIBuXMNlhU7QoxkXLNChzHOwQ6gslaEx9RdY-iYY6iFXVPr-jGt2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پلنی نوشت برام که اصلا GOD Tier</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4746" target="_blank">📅 00:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/by2K6VPud_j3zmfIi47V-rfq3QXQuWSIRqUPNeZ1q_TO6LxCMoT3jc7Grs9IWOYLP24HbV-ucC1nhDJmPhx71Xb3zFrDCxrB90WK6hrj9rIE7zgLcBCoFsMrGdNDRhLYfp0iYhEW8dTAPv_hsB1VAXl60VoNhjSTcybLMtLqamespEzH497yBV90xWVqoFPPcznLiCED3Asmea8M9qti7nUaTTvYbs7sWs5_mQyz85kgNc2Fmj0wfq7Wb-YKgVZNURZ8esL5PJur03e9UsC76_FaExuWm7CpykP0SjXEbRa2YtSI5Y9Zg7JQUJeAcbwbMajp6zf0cC5xIqVb0n0Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای گول زدنش به طریق‌های مختلف هم یه کارایی قراره بکنیم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4743" target="_blank">📅 00:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به زودی ویدئو داریم ازش
هم اپ دسکتاپ Claude
هم Claude Code
و هم Claude Code CLI</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4742" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توی opencode همچنان کار میکنه mimo
با با ratelimit سختگیرانه‌تر</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4741" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoFD0fhlscMapNiWitdQwVJDziEsNwIJ8wFaEtWschzQCSPXEOA1QkpSF9XZFhnL-q7NgkANI36KYPz1Y-LMdJC7aHEjZ4zGefW-5NLPi71WqkN9I_wNV2XRY4mBOs9ZbgDl0BIBk2zJLWvFGnkR4SaPsn1QikUWo1ScTfTfHHC0lqk6zyCp5hkC7pBYfHZRHl52t_MZjuWuLjETlUv4DpYrU7CSsikWm5fUWydUPabfLbDz1FtZu4OCerqjQtxOHxaAuwMp2b6Sq0cZKjN1L4xN9pt8mo2MC2Ujrhd75ZZJ1jr1_QCFqJp5w-abII4KC7zxwdVX7jUGiksvyo8zow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون سقوط سهام آنتروپیک
😂
😂
استفاده از mimo چینی در Claude آمریکایی</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4740" target="_blank">📅 00:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4739" target="_blank">📅 15:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/4738" target="_blank">📅 09:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm1XP5RCsHWUkoz8kMoNgpsD-eKP9l6xXMnyJLbMafsBZs3uECG91-AUwGoPJYnlbSckxTRuhR2mjONHwbXWkX2R1JbN-Uxdle6Y0KUoqiv-RzautzHHrE_JLTDTUVuYu_9CDKoLxt8xkSWPAwH0_WvRpojhRsTQTDEfU1d9OZ3piQsmwQjmF6oL_KRSri2aWQvIJ52lC5ctiBnFiAAXU0WFj1c5Qj4lMtFEZAcwc5xcSbwvrrSxTI4qjr37ulkkYTF-dqJGTlL4xuAbVxOKNnhA9OiK6bCXDb8GY6mEVGieZQZIwaOB6aBy81na9x9Qm9VFBTsm6BF2LOuUhvhnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L6zE6y6ZS65OySVpYtqKxm57J7UJJJujqJf2pYIUukfKI098rDsIqnSRXLb1a9GSHTyJ6Rx61624Ow04620byiSMMRZYDGkrX70WtnNghUOyHPiCtEZFrblnS_88gpYQ1ar6dUA4nYuAABYudUh6LCLnCRYBsnObp86XxpeICLCDz0_wXB7iZZLqhC4O-f0tGFeK18VYGcJ1C1fESfCBTTYegF-X6xgyHnlYYhhW7JJmwXKIl6neFd6Yp43BlCKuC7jFAHkFAgSJYWYpf0LoF1qJ-B-znJqi8GdpINxHUJl5brGLdeY8nobywq_aQJU-9lBqfEaKR6RBy56v2JPrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pebqex7UpVqJ5rG72vtlx7dSVhJSSLcfLnyaeEn6aRY9gp269uk-fgFCXTOA3xCq1v2aPCR0DU_1NJvLBzazoaXc1kQ_7FULTWuAlw06J09BNVAQBUJ-MuDajGN5rTz7K5bB9829KaZUFDlAANAlILT-4MNECIyjE1Do5UcUGj0EalWFloI7kYRSu9m7tWW81RpMNvd0-sGp8Da4s7Fg8-qMFdZHa1AyzTOVTQBcMFlsFYVeGJ8DPVjfGHl0yGmYPLybBpuHRk4njqqgufdwQm5-iGnxnpzPQMTqp465-XW02nQhuRMJnK7QDHXde204sgHB8rQ4p7otQtIsWWrTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=RF-e6KSstIIs1mS2ljjTDGWL0YwiJTLkSogbPBjMEG72kDfHhhjRdiwN5mc5ownMOA9x4Jv5M-N3Ud57O1Ab3pNsJQv0XHl-pAU6z9McrDpUbI08p-9TpfPQ6ybL9u8v3y6coa9NACoFOWkqYILBSRU8Wld09ObIFenuQZGO1hknP99YJwG_em8IUBLMdvaFW16QluiSFM9jjeTXpsBF88BUVrMmPnDZkhB4NBBCSycZNBzAZgHwKFpb1cNj6QaJMlIgnvp9jkx3FlpvGnvJ3T5_Wavd0hSaDL1nOBjie8wdACWMRlKPPhpxq44obdiNZdpTJx7k8HjSsIoYf4zr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=RF-e6KSstIIs1mS2ljjTDGWL0YwiJTLkSogbPBjMEG72kDfHhhjRdiwN5mc5ownMOA9x4Jv5M-N3Ud57O1Ab3pNsJQv0XHl-pAU6z9McrDpUbI08p-9TpfPQ6ybL9u8v3y6coa9NACoFOWkqYILBSRU8Wld09ObIFenuQZGO1hknP99YJwG_em8IUBLMdvaFW16QluiSFM9jjeTXpsBF88BUVrMmPnDZkhB4NBBCSycZNBzAZgHwKFpb1cNj6QaJMlIgnvp9jkx3FlpvGnvJ3T5_Wavd0hSaDL1nOBjie8wdACWMRlKPPhpxq44obdiNZdpTJx7k8HjSsIoYf4zr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giOq6Z9E6qIvopVyq_Xe5FxfzwErEcv5zSl5mbnCVB9TbARK_Wvgwsm-B5F8WoK31ttIUyiPRas22h3PjkILNfm0Yxu0ewvi3DhGTzvgIfkM4NqjCpiP6wsjq_rMc1qChut7oYl6Y2FQoM3HdbuuQZbJVO0QRazuaAQcwtYWnK8Jn9uzivJ7Xkagr5CNB_e3BNgJl74oK3ivk1okGPNOuAlnjoxeVa6NhWBCOAAJUxuc6S5CAIkyyCBup_z5LDynfExzEF32pyXGj7UDPOFCx_Li3q7_DtX7D9C2UnTgu3N5DygRVtgyMbxqg3W1dLzCR5OiTndijf3nYYox4i8tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S54ZKOGpSLJG_rGjFyiqkX0ydzehydRdHsqq7pf0lJhm_rsod86mMOSl1fE-zoPmVxO8IYINDnS3X7k6Z9fPtMkC4guUTwUY1gtX1Ri50Slk1s-8fGYW5OWfdklMycAw9rbIS53G2n3N5BqyjuDXil5DIeyAhJT68YkYahkow8VNpkwjLzZigfU9grbSsOnIdbgGFHn8RqKs7nTY5g9OrBx9LgYf6rgMlJy-0qqnpe7FktHC5wSHzoBlNp-s2bTRYDMJkIPMPlPB3zVXy9NiLQCa0GFe-IaRjxBohsXyIiAWHyZ_X9c7LN-7X3qCKgHcUWBypIsNKbT_DL0U6QS11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mh2YmV0QP9MRv8CbTXO4LhyuqaoXWuNTQTnWrXFNZ6aCGpZKOaz9elAwTICqYQxeHwEd2VKXuGxbz2XUs3ueiovF3MPD1o9vcEV_lw90vRq-k3VqqAHKCzjqEMJn3ybJWmkOxgrGX0BbdVBSgvFLPnGkTTLu1IVnRrd1NElHBEFb82nJOY3sz2poKlNB4svYLE-VG4wSXX8xU2mY97VQ530Tn3XoXVdyilN2tveXzhjUYE5WAVRg80l35kT-DSI4W9EeJ35UPsC-NzBA23a2xi7ztDh_d3clgGNUcEOjhB6C2tXeqLKc_b3G9D6btBACw2yb9tT_d8LN2eN5GMrsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LvCUksg-GoLEts-RklBgtLfI8dwTmyDNhI6l7ogOaQfAyNKx6_xc8PcAy9hutH0wCt5a-7hz_2PJjNrb4IIeJr0pCxBrimyHIXNOU7BtZNuG-RS46NePh_6-2uBBkIQDc9Ux9nKmJM8rXN7zfwqfs93UZpmOq7cp5sKJrO3A4Lv-7WuCaYJuwnrTLK2ARcPN-r4HfsYXNplEcJr5dLR7oOzDHMkCIFrASFkAGGcnxTw1BMEGypKBiARPVeu9Xovwb_8KnNu6fEdHLZFNdXkyF56qxQnSBHH-gkvIbujuQ864yMzOmPu0y4RakFkaZ75TCRO4dQqj4VirU4ha17WRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f26ILp4Y-Y37WJ5cLqrZs2rtq3u7tdPd4bZ1sMG9FY5BqwXv0UIcKwS0eADio-ByuQaopKZSyZ7h-vNYD0FgMnM26LOEJAbzAnyqN3-RAZNMOtokmtequYd0MQteb0tH9EG-0_qc51ilKwBRAv99dY_MJ5NQnP0KOR-KW-W268RvzAU80nv9OqMx2mifbMcMy3m62m8jSAjO7iRM42NjDdcKVQacN73Rjs5bzQPGq9ppHySCMPPTAPtlb20u-jDLRos6uTyA6dooVSObh_7BpyQcPQOUGZESGIcr8KZvMPLKC5lsUqBN2koIMrHu_2DfEzYXiRyaFMY2SAgn8XFbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iBBgF3F9KetHIQU1G7UHeZVAMaoE9vLJocQ78qEbzRw00c0IcohPdy0GUZV-zjbIbdOhmoj6L9j5G1yT9-7BGfTWbYt99tDZBbLQuW5s90PKh6573PFVre43Z9LWzsXA8SknhT-gJJZnRLHXHhVf7a8xL3ka5OcsvAKD-QO4kYRwAThIWMBN3RsdmXCTG2Y00k5lRQOrvz5TIgxUdtK12HgzkhlLFMt5SjcLWEw4DXU0-Q3Fsvu6pKttNOAxd7qLu2KW5zUYmzlB64Gds3Kkd1CmWedfhMLwPIC0jheivbBp04RJAc3vqMva2Nnz8nyE0737SbeBJ_VW1lL3QClzRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn333Y1NObZFMda3MvI20mZH9Pi_taA2thHMlJY3K7gfng4Q-TIr6-KClT39jvFr8aiwPAIJ4O8t_i4s_E8KFZGgImADK2boXZOBaKdkal-ho6dANAPp8-RY-kwZASljlmTTw0GuEwXkpdle_O9v6JPtbV3rbtIkK4PXRtS10BRpgIGbMfWMt7P5ZqAySGBsfQP66Dx6upL-6mj_1v44NSHaMsuUUpIxpEc2PwSOyb63KCggSEbEDvv6NG8iMf6lodC-V0gRElSlBu5lWOuKk50wJf-ugfH0O7e6FixgCFIWLMFEDSCjA-su9VXWwwfzVayl7kvse2HYGv2sJdkAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=Bl5Mr3FnEF9sUvYFYoj4i1EzBY8_zw_eGYD5y3bAmyT61xPiYVynQBObwwPJ3FGGN-ielwLInjHi1qKm177xQtrX2Mllsf6Hb8lVBki7kDwuOlmZHyNNJtoxGh97lHIWI-PXqaTM7vLv2F98czFE6eYNBpuzxNvi1KVIL0O6IB7LDdJkcJuevcly_Xn_85ey27cibv6-tR7AecITYrK1ACFYA59gs52fcH-Xt1RbvS8wQtKH2fyoRrggtphoXIPzNFVGio6yesuKVmV-fQ3JdCDFefSh4NBpQw3TKiXccfwOM2YNEvInaAfeTmWTpXiQ1ZW7BmjK0CUQ0sabxCX5vg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=Bl5Mr3FnEF9sUvYFYoj4i1EzBY8_zw_eGYD5y3bAmyT61xPiYVynQBObwwPJ3FGGN-ielwLInjHi1qKm177xQtrX2Mllsf6Hb8lVBki7kDwuOlmZHyNNJtoxGh97lHIWI-PXqaTM7vLv2F98czFE6eYNBpuzxNvi1KVIL0O6IB7LDdJkcJuevcly_Xn_85ey27cibv6-tR7AecITYrK1ACFYA59gs52fcH-Xt1RbvS8wQtKH2fyoRrggtphoXIPzNFVGio6yesuKVmV-fQ3JdCDFefSh4NBpQw3TKiXccfwOM2YNEvInaAfeTmWTpXiQ1ZW7BmjK0CUQ0sabxCX5vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onNuDB5KJ_S3V9Q0zqS1egtyNqGiVO-FN6M90JSBMkKydY4hKzIE3DIGNIl2xksUubaIXQL00886zYssgC-il98IxpgAdvgBJWdU7U2yQaHTj8BCulV8YP0G-9nogeGq0FAuQwhjIKeLjj2-zhUbWwOUrQ0Lx2nnumT3CamxS4n_cWoB2rWnSRhwci0LMjYefpF-vUW0v2fm6BOJM9OLwfWZeuGSMSdCWP_4Iy6WzCiO1CYQWQ6HOzgP8CqI633NM6BPLvYr_yBaWlu45luPq-KJJ7votV4mgJsOvTAS_y5naDLHy7upypapwoAYRYqs-j2Wf4Dt0945_6pctdYfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4707" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HnkllB5KERI55JvZKR6ClTrnGuaUpb9TuG3U0HYvCgIE9FUouVe4wfsXHLeUiT2HYLWRBnYeikV4mDSLBib1snlUKbZtzdWy8cZQfKZffItm6G_Xf2uP6z1gY3AxDlqOk6XzI-tuGjdjqlTz4pobaJpJkAcTlGuMCyePfHsY37simwzDw85hQ-ps37RO9lNzInKCv4HMbtynrYUEXk-5fvg3eSY-23qL5vZVNRhUJw1rUS_C_7p9T_2opdZiNX4dTdirL0vyDxK2fZsFjt8Ro91tEYudkZqiRdfC4muRuSzJZclqPsw3YTw-TNd3WoKFqLWRfokkTAv7E1Nf5lcthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kpu64CwPOtbb5gHxtGKpD_1Jaqf6UPwJZPXZGIMvXhxXPtvDAsmvEulrrvJ81mTSGAH9PBsqfSgRd1rezcQIHrA89MSOYfXttFYTRvtHpgP_EWzizdmKpofFcWx3Lrk-P7Pa9fWviTWZFV6gjYkxpwbt0ozYjwq0E2w9NDmu8R3KYYwW8uKgIQFUvcmaIhVREG3MIGkFcxWuLPBLbDQTSYI-93H6Wc45LGTSb5G_-xcKT0HICERcqB72o7vCLH7tSKLqEKeKs1AonfG8CATPLIGQJqyB-jAOyuP-v_Y6fv7TDomlaIPK1S1RAvqIeMRmNjCRKxiOr1iphnuI2FbEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cwi99Pizt8outwb0Hn4plQ762fWBqBzTnZ8Hv6S0H8nFPdjlzRZtKIqCXfX5WxoB0SF_IBP_I2QGkqWqNuGcfoV9oLjGgArm7qT8P4OcjIrHn0D2vttFoWRo-dR6EQMJFAQOOh3o3nGn_qbu_HYHgengIV-jJk1cacnQA8mGc_1ikOqueZHQ8do-GrSnMe4XfubyrwM5051rWk9AGqiWH_yY9PxFPkiJxFbABReNhn17M7rffD25TSGJb5TY5pKJH6eFmKa_I8f55Anq0iac_uSYFRYH9dib8vKIp2-pAvyyTYZ57UsNPgocnWqAzzVYO180wVC1AI5NEmNKq6Cnng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماژول رایگان و قدرتمند حذف پس‌زمینه‌‌‌ی FeyNoBg
:
تیم شرکت Feyn از مدل جدیدشون به اسم FeyNoBg رونمایی کردن که برای حذف خودکار و فوق‌العاده دقیق بک‌گراند (حتی برای مواردی مثل تار مو در باد یا ویدیوی ضربات ایستگاهی فوتبال) طراحی شده. در کنار خود مدل، کتابخونه پایتونی که باهاش مدل رو آموزش دادن و اجرا می‌کنن به اسم NoBg رو هم به صورت کاملاً اوپن‌سورس روی گیت‌هاب منتشر کردن که می‌تونید همین الان روی هاگینگ‌فیس تستش کنید و از کدهاش استفاده کنید:
سایت اصلی:
https://usefeyn.com/blog/feynobg
مدل روی Hugging Face برای تست:
https://huggingface.co/feyninc/FeyNobg
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/4704" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rcQFmflpqfgeQ6VsEkBF56SwN2dnAQ1FKEWuhVH-m7O8c6PyGzr7jALUsjepgSkTWHQd8tXtwYaVmXpPB5jgDNEXIs71ruYACt_wMoH2AFTFQmF5fd7_APsb5vfKjrbpd3-gyfHP0ebE8VvEjs4hP2Svqrk2jdESEqZcIblLUuldOqatarpXIQY4rl-x381B60FwZlSD66jBopYE5S6n-D0L7ih9TUm_eZlX7zypbf1QvE6Hg3tJmvGjMivUr5g-AgM3UXEKXcGCtg4PCRR7hYUJdcWfmH27Ias-fXmDQAqovX4P3MvG6NcllEiw5LAlEI8LGrH5h8Cj9qDokLCeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالم که هنوز اشخاصی رو مثل سعید عزیز، در کنارمون داریم...
و ناراحتم از اینهمه آزار جنسی و تجاوز و پدوفیلی که توی دنیای واقعی و فضای مجازی میبینم که خیلی‌هاش هم متأسفانه منجر به خودکشی میشه.
ای کاش لااقل نهادی بود که مثل کاری که سعید سوزن‌گر یه تنه داره انجام میده، کامل و به طور رسمی و جدی پشت این قضایا بود. که این عوضیای بی‌صفت، نتونن انقدر راحت توی اینور و اونور با شماره کارتشون فیلم و عکس‌های این چنینی بفروشن
دردم میگیره اینا رو میبینم.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4703" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سالواتوره سن‌فیلیپو، هکر ایتالیایی و خالق Redis، توی مقاله‌ی جدیدش توضیح میده که نبوغ واقعی لینوس توروالدز(خالق لینوکس) فقط توی کدنویسی اولیه کرنل لینوکس نبوده، بلکه بزرگ‌ترین تصمیمش این بوده که خیلی زود کد زدن مستقیم رو کنار گذاشت و روی رهبری، هماهنگی و تعیین اهداف پروژه تمرکز کرد. برخلاف خیلی از مینتینرها که خودشون رو درگیر پیاده‌سازی جزئیات می‌کنن، لینوس فهمید برای مدیریت پروژه‌ای به این بزرگی باید زمانش رو صرف رهبری کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4702" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پشت‌پرده بازار فروش غیررسمی توکن و کلیدهای API هوش مصنوعی
تحقیقات جدید نشون میده چطوری یه شبکه‌ی بزرگ (عمدتا توی چین) برای فروش توکن‌های LLM با تخفیف‌های سنگین شکل گرفته؛ این پروکسی‌ها از طریق سوءاستفاده از اکانت‌های Trial رایگان، ربات‌های پشتیبانی ناامن سایت‌ها و ترکیب کلیدهای API مختلف کار می‌کنن.
که برای به سرقت رفتن اطلاعات مهم استفاده میشن یا Train مدلهای AI چینی.
به زودی بیشتر تحقیق می‌کنم و بهتون میگم
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
اینم لینک مقاله‌اش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4701" target="_blank">📅 03:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خدا لعنت کنه این جاوااسکریپتو با این سینتکسش من ده تا زبان بلد بودم اومدم بکنمش یازده تا جاوا اسکریپت رو هم اضافه کنم بهشون، همشون رو یادم رفت الان فقط جاوااسکریپت بلدم
@Linuxor</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4699" target="_blank">📅 20:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روی اوپن کد هنوز میتونید از nemotron3 انویدیا استفاده کنید</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4698" target="_blank">📅 19:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فعلا میریم nvidia(با اینکه delay زیاد داره) تا ببینم api رایگان امن چی پیدا می‌کنیم باز</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4697" target="_blank">📅 19:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4696">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مهم
راجب Mimo
😭</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4696" target="_blank">📅 19:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4693">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YhWjPKzLl37tug5TYpXqVuERHtOe0pc9u7NJwDq8dZwE4dup9lhbbIrXR4-Nwz5VBfxkd-DJJm8hbJooNMd05fCDs5RMp0colutCAjBwYpC1ac_SUAfKDWpWWDG4mdTY1yoozRUuSFVcfF9T_hy_MiNw6r08krn5j_2jXd2_L_GBFnAIPoeCBp6Xzi4wh3L-M2SZQKX3VMmBWjI0FbYoHbUR2D6z3aX9uhrG8UqarC757aOY35cWi_7wEjVbnlyRYJp6ufc4dsft6LGAhqKFCEfvzs1RenmfZoSJmO4fwkBWPMzx3JPdmF_NQKNy9_FLHnZpxA-qVIj9uV58hRNAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ovb1E5aIkJzf_MTXhrfBsYZrBdfyt3A4rJB6Z3Xl195HlTo2Kj1O3mSWaXwfqSZh1iz45sgZ7sCcaR90NuS240u_rRvzJ9fEE_FDEa_M2XfNEzFi1hOKlEe-rTXGmiQUeWAsJrOySyRE_3tTXAtjGxTEgWtGPx9VZJLZekX5pROqSsqHS_imUVUmcG-0AjvX-CYd2Ei1cN3WDA7DPOcrLOji6EoZm9117XKYRQR1NTrPaE6YV9MgTJ1TjhSVeId5DLCB8n0sCXjGFB3KecGmRGKdg1_RsdiuttQXYUN5kxMqzh2mNu0pMjuySpu6_U1dDJUUKLWuV0RXnERV1alZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOrrSlLLBB3QfkSnqLyW2WlHTSvYehEdG-dsINDgpNbFpPOaMiXWBgxum2Z9tHAXAPU9spsJYwiQ3PuBDVLhsz-Y8JP_njPTPv0mcS8xVGFZmKT7F2kadoJZxH0ulPVFoGPYx0IAillVs1Wjl1miKsW1xgYRrAzCIQ3CcH5VQyVgJGeLhq13oaCFFT0-ASBYtOpRBIiqSO38ZgxbDiac-XXWNItvsDXzd9W4A0Qi0Th01cYoh96ZoHxQIXKs7A8oiPleTidqDiFiReBf2dWZKMjrjjbIhYoeH7Q50vksKiclR7F9RruT3AAknz95Sj1IPvbi-eyhkKqERUiGnF5b2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای این از proxy relay کلودفلر که توی ویدئوهای قبلی یاد داده بودم هم استفاده کنید مشکل برطرف میشه دوستان</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4693" target="_blank">📅 18:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4692" target="_blank">📅 17:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4689" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/G-LdmtH3KrWvBQFDXx8u5ZVthvXYXPPOH8sCp2B-uphZLqccm29lBwRQAaYVm5hnZDv85CEck0fMoWFytzgiNskrv4AzjIaPXiU4zZY2fNo9m0u3xTrvhSCzpAu2SHpcETWzvgbX4_vz2RlvC2J4M50UM_Rrawl7R8p38_QEg3zTvkz58N6ewfEi2jwHNIqopkTrx_cx63_bimHaWkvL6O9BRztURu-Xh1XFlWaxcdNHpkd6JSESlRiebAtI4uwGAOdi-AWixfVuI6oMhJ7uqVCazV8E9yAAFCyO8iJqjP3JoQdktZk72Ud1BUWuxJVKYNMtnaC-ITQwg36vLIswAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش
طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4687" target="_blank">📅 15:19 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
