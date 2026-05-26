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
<img src="https://cdn4.telesco.pe/file/et1gtQISz72pKtT7VhEx2934eZkRn91129GfMv2PgI5nqiVUuPrWA1vp5n-uu7PJrASxwUQKgH8oV9ldQDqNtXqP-DQSVrZU7b1bJ1mkQIwe0fNe7upV5qv32V2UGDA9b3Y5JdhKxDyMpMHkhaNPRDF3GvK3qEeA4mLUoZxQakgKlafnumaEQQMV6wM6Ttoq87S5F5Qy39-u4Jb0CcTn-zyAGBnWogeSBJVS3ypXi2EAhU0qttw04iHHPXGoNaAKNuLtEsMcMhkx5s2wxg-yYp_9ycnnlbmO7QgbkY_BOGnbw4XkAV7sq7w3dfc7Ctl5L_60jd9-jSwKbJCmk5wYJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.7K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-8518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این پروکسی های تلگرام هم داشته باشید فعلا با مخابرات و برخی اینترنت های خانگی متصلن:
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
ممکنه منطقه ای باشه، بهتره تست کنید.
💥
@RUSSIAPROXYY
🇷🇺
📌
آیدی فروشگاهمون
👇🏻
💥
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 707 · <a href="https://t.me/IranProxyV2/8518" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎁
بفرستید واسه دوستاتون
❤️
vless://27d6de57-240b-400e-a036-192608ae0459@mbv.followern.ir:443?encryption=none&security=tls&sni=tino.protag.ir&fp=chrome&insecure=0&allowInsecure=0&type=ws&host=tino.protag.ir&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
متصله رو وایفاها، قلب بزنید ببینیم چندنفرید، برا دوستاتون بفرستید که وصل نیستن تک خوری نکنیدا
😶
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/IranProxyV2/8517" target="_blank">📅 17:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درنظر داشته باشین که فعلا درحال حاضر تنها وایفاها وصل شدن مث مخابرات و آسیاتک، شاتل و... اونم بصورت منطقه ای، مشخص نیست اینم اختلال باشه یا اپدیت فایروال باشه، پس صبور کنید تا همچی مشخص بشع، فعلا اپراتور های همراه مث ایرانسل، همراه اول و رایتل و... وصل نشدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/IranProxyV2/8516" target="_blank">📅 17:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
پروکسی متصله، رو وایفا و مخابرات منطقه ای دوستان عزیز، اگه وصل نشد تو منطقتون ذخیره کنید داشته باشینش، صبور باشید شایدم اپدیت فایروال مشخص نیست هیچی
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/IranProxyV2/8515" target="_blank">📅 16:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8514">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو وایفا و مخابرات وصله
😁
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/IranProxyV2/8514" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8512">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مجدد بستن پهنای باندو
😐</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/IranProxyV2/8512" target="_blank">📅 15:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw4zm-b4g0Wl_qRXesjxPJPujrIOrppewb52pD5iQOehx8jssOxtBRAV3qJx3y1Z72M21RLFQhqzMancYS4B17yvnTwqS3IXT_HvLyUN4DJZnpL8_OsBe2zhOBPxbQbpcVn0tHu8mwNZKNFTAcRICm35-5Vn4THkSvkDIrv5HYw3sP57U9iWmsD3zSHmi0JJzHc87gtaQSjdmeOUWGXhupDt35ec32OylnfzMJ5vDM_yUNvTBAL_RKTcdCtQLKq01kcJJq2Yfh2yMtoY5p_5mIFI9KT2DM7NJY1hM5zSE8XRKDSqgVSQX_1fFen1HMhoMQ-W2Cxf-RSfGN5OtJbDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8503" target="_blank">📅 14:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روح و روانمون بگا رفت، از بس حرفای چرت و پرت تحویلمون دادن، رسما دارن مردم خر فرض میکنن و پاسکاریمون میکنن، من یکی که دیگه مخم نمیکشه حرفای اینارو باور کنم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/IranProxyV2/8502" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlC-FsutHciY6Tccm5c4D7rFVHPHQhmC0UWW8SGh4Z7k2FMnehih95GUb45zjK6jnkUXno7G4B_OA-8Fe6Mvt0Nr_X984jyZ3AmDLuVIGUCynEF_rVssFjIuitDXnl0bgqIeiYkRvHC9wv5RkSw0K2QoHCGsD2u2odXfomlR23fL0NLs5tGHeqJc-i9Xoyrsmey847glGjbyV5VJCkLlVJVwEv0nO4IDPUC3lLCMP7jqj_4eqsGzlwhkQtCTsF7VGrK37TNJcrqapx0RY5YDiAm97CXPBALCnq0nMCutLoGfdipm2qmwRGKjX-sd-hU2qjhGakaQYxsrlnyjc2dd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا حتی ذره ای تکنولوژی سردرنمیارن با اون کلشون
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/IranProxyV2/8501" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/IranProxyV2/8500" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئیس جمهور کشور اگه تا آخر هفته اینترنتارو باز کرد که کرد اگه نتونست بنظرم استعفا بده بهتره چون نه اونوریا حسابش میکنن که ترورش کنن حتی نه اینوریا حسابش میکنن
اونور دنیا رئیس جمهور یه کشور ناو میفرسته یه دنیارو بگا داده بعد اینجا رئیس جمهورش اینترنتم نمیتونه وصل کنه
جدی اگه نتونستین وصل کنید خودت و کل کابینت بنظرم استعفا بدید یه موز بزارید رو صندلی بجای خودتون حداقل فایده اش اینه موزه پتاسیم داره ولی شما همونم ندارید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/IranProxyV2/8499" target="_blank">📅 14:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8498">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فارس: چندین نماینده مجلس که عضو جبهه پایداری و تندرو هستند درمورد مصوبه شورای فضای مجازی شکایت کردند و دیوان اداری دستور داد اجرای بازگشایی اینترنت متوقف شه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8498" target="_blank">📅 13:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان داداش نقش تو چیه دقیقا تو کشور</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/IranProxyV2/8497" target="_blank">📅 13:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGsFeKUWzAdpW5MjH6U1PdEsVzrWEHdGLEuvYoa2FfFnaKnv1lN0t2qb6qDESbtKE-dhQ_GRAsra-eZgk6OxvBUIsFgFod2LtOV1F1oBdPvuKxnbFjKSYF-_6YTsbRdmlbzEYlukRyD6IylP7305m1GppT6IMxNSM3Ce1HYHajreelG_aZ99K8pvd52SiDgod_irCQqL1AqSNl3b0TaaT1wPXXkXttgEGF0IDowwbbVrq-ummvqRxwbGrHaCsRJPokRMgqm3b4DzRmf68DyHV5fSvaLuHOHZ3_YTIeTgCEaiRbfAPLXm52TGl838DnioHiwI3vD5Yl_hp6sJpbdDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارسی هم این موضوع موقت تاخیر در بازگشایی رو تایید کرد، درکل میگن که فعلا تاخیر خورده اینکه باز بشه یا نه
😬
وقتی مملکت بیوفته دست سپاه همین میشه دیگه، هیچکس دیگه هیچ کاره ای نیست
🥲
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/IranProxyV2/8496" target="_blank">📅 13:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی…</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/IranProxyV2/8495" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در پی شکایاتی از مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»؛ دیوان عدالت اداری دستور موقت توقف اجرای مصوبه را صادر کرد
😐
🔹
مصوبات و تصمیمات ستاد تا زمان رسیدگی نهایی به شکایت، قابل ترتیب اثر نیست
🔹
دیوان عدالت اداری اعلام کرد، در پی طرح شکایاتی با خواسته ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» مصوب ۱۴۰۵/۲/۲۲ رئیس‌جمهور، هیأت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت مطروحه صادر کرد.
حرومزاده ها یعنی چی، هی پاسکاریمون میکنید، بخدا خسته شدم دیگه
😐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/IranProxyV2/8494" target="_blank">📅 13:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re_vrZPouE1b7LVU7SeKI-hALNydTwiHeTZWDMJXG62_k7Y4lCmyKaquWFa3lXvqlZexvuEZIUheD9tJjtsdUSrTyu6C5chdniwM9T_f-_SrXj5njULuCSkTe7CvpNrYiLD_FY-KqidPOBg5Ae1OcvC0CN9bHw8d7Jn9Rff1OL1NxFoUw5pRZldLRf0DOiyPpLEx4Mm77Zza8XFoJq9J5NDZh147dDMXwwg1GY_5G-4dmj0thtS4oiI5iVSBwMlUTs7tqCea4DCw19GSjzMWanvjUf0VKLexyvEp3d6DrATxuhyZiIc-eMl-R8HIEELRkDxHmN5ocog11I3bBsSX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=130T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/IranProxyV2/8493" target="_blank">📅 12:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8491">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚠️
اطلاعیه، درصورتی که نت بین الملل بازگشایی شد، مجموعه روسیه پروکسی تصمیمی گرفته که به همه دوستانی که از مجموعه ما خرید داشتند به ازای هر 1 گیگی که خریداری کردین، 3 گیگ بصورت خودکار به کانفیگ هاتون اضافه خواهد کرد، پس حتما لینک ساب هاتون یا سروراتون رو یه جایی ذخیره کنید داشته باشید حتما
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/IranProxyV2/8491" target="_blank">📅 12:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8490">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان درصورت باز شدن و در دسترس گرفتن نت بین المللی و برگشتن نت به حالت عادی، حواستون به چنل باشه سرورای عمومی و رایگان براتون میزاریم حتما برای دسترسی راحتتر
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8490" target="_blank">📅 12:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8489">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده  منبع:سایت رسمی نت بلاکس  @RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8489" target="_blank">📅 11:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8488">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLKAQlEjgzQ_y_7mc18pq0PrstSgmyBB-TADyKkwFd9Bx3Wif1GKxVS-ihxIGvB953_gWJnNzSRenR-jJxttZrqVmgmJ2tbEqPHQpTR1XvNXdDE7CwcuhAGlFyDjIuOlPaIxMQpT4shlBEXJZd47ImLLWptFJvbsqA4iuW-bg1icnOa3ODRVnGEpKOiWxFUssPKlNHpKm53ZErdIT35ELgByflUvAclRbc5wbN-PhXbqPmG5Li6xLQnRsZi--aT1s9totzA5qj74H8QtE4B_3pdW_1jicIh2WKvxm6QJSPOFxirqO3UAJQoW-Q5SVJ8P9vweVBewshDqhC_S_zSG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت نت بلاکس هنوز هیچ دسترسی باز نشده، این چرت و پرتا که چنلا میزارن رو باور نکنید میگن نت بلاکس گفته باز شده
منبع:سایت رسمی نت بلاکس
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/IranProxyV2/8488" target="_blank">📅 11:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8487">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادرس
mail.google.com
باز شده ولی
gmail.com
باز نیست ، اینطوری قراره نت باز بشه؟
😐
اینکه وایت لیستو دارن ادامه میدن اسمش نت باز کردن نیست عجبا
😐
!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/IranProxyV2/8487" target="_blank">📅 11:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8486">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8486" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8485">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0rgwf-gQ_9lqDGbZ1ybmV8gQc7o8O4966Xz1AjaHBh21bLyNL8VoRpNBQ3Aizp24SgmGaytD-4J7NrBGDQgVzNlXPyd5MYP8vIhwrG-1oIxL1ycbB2JsHZQwJXkMkfxz2MrMPq3xTfRGtNy0BfHYXsnixpnTS6ACbs400urEONuCQtJHvSeZksK65ldcbFQURPLdSPlf_SnqGu-azSADTFmY6Def8N5sXnfxBdnsKZArxWsxrWX3l6i6hlYD-hb444SqKJ5N0AY-wvafZf1pWXoTtOXd0xp5hRDqtJqQ3DvXqS0uGS_EBRDB4c47-xAcjG_7ad6bts2-qMeysDfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8485" target="_blank">📅 10:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8484">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
trojan://humanity@193.151.132.136:40443?path=%2Fassignment&security=tls&insecure=1&host=www.ignitelimit.com&type=ws&allowInsecure=1&sni=www.ignitelimit.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8484" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8483">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8483" target="_blank">📅 10:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8482">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مذاکرات طوری داره پیش میره که احتمال اینکه ایران اورانیوم غنی شده آمریکا رو بگیره بیشتره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/8482" target="_blank">📅 10:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-R7cTfi2GpiBnKbaFoTGMlOxJCCv2O50pCGowmwiQ5FSGl244AH8MZCt9fVyh41vRrRGFCASjRPtIwMRLrhikE1E5Krqf2fOPowStjg4_VX1BmnmpgEK0-dgB6HAR99Ys__PvFdTmOTZNUGkYVvlC_H_s6VvxMWep3m3ShKziYkRPOPSXSiOSKCIeLVHAfasXnML0P_SdVFt4dibkwu36PVZsd6KNBNViFbte9Vj3VynpE_KAUe8Yhvs-NjKFC-yIXQYqM6PtVZIX60pBk89qs96zMb6tIRHk4yWbC1Iz6x4C2r_Pxv3pId_Fm0FLBtek_RwsXHfsmgYYfHgpAdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZinE_ML-Ipj9l-em-JnjSjo7DIzqsxz-5Z346SA-3ftnjQxa4jpyEUt-lCd10Xo9oTy-yPHxfjVlcn9YL6dntzIkgQr-hk77sG7xBQSPWPKFTby7Gh8Y0N0qEnHod8wYfQrSdsi-A0fUooQCUXmksWQPhzOCEtEbeMOu6vVLfzwZcQJJmolSXNEAp5gSh76pEHbYTNtyX9aN-50nAa5nkt_ay-AVZ0PmRuYKzXrji1f4iVCLF9Oz5arOji_TgjLHnNgcGvnMauZEsHUpD_eAjj2ZoSTn2EmUABC5LgZWplMN80o_Cv4QDsvzVJuLmq_Xb_2haULaL-mFwElFpXXRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBvKNil9oe_mGRBmdueImNSiSIGg2ISzncOADGuivZIf0qRicfMwylSuQKF9K0sCQisr3XmMWtgm_-QGKilFFS_DwwX1oy5V9cyU0G_YJbjD64Jtlu8DtN5r-QS-1g4DRCxdQ3upSNF7YGEQhBuFdmTKMkboGTd6cmUFd70MB9xxWzGKlJ1tHd4lJIE8XuxBVsMwVyMZtFEIe3oYbOdNCkYFaeDoXjGImehv9UXVt9dEet8Rua3KUQZ3-DBwqMAihzDc4EWmnCj_zF_jQ42a1NBcElCJ5EkBpk9322U1L7wkJZeE7VtzZ5xbaCbvJOccV5dA1WMhiGmPUhWTl_TKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vISCZ9GXfMM7_JSkeI99JSO67eMFuyGm0Oi6xyghXNVYePvGXwPhIdc5qWhfpICY27oO3OsqtLS_Y1t96F1Vqpe_aWM1bB1DpzP0xD2cPNtV-qNcIjQoCAyFgLP81WRW3F4g-eAj5msSEC5-teK1wq_hmFj0derie-0v2zXochjSWGPvhCle1abNHkJpU-Bh4uOaAM3BZAS7oJ_KTMjYgfFAnD_tnxvCQx55QXlO0zyWIvsaUwYceeSgHksr-qXEhNEsL7xS9WOBUA6BX-PqFU89AX3v45XEh88zSntVf12XLMmm9xPgghDOeWy8HdhBERrzaHI4hbrPsPlkWbKQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
طبق تلاش و زحمات تیم russia proxy بر پایه اصول صدور ترافیک خالصی بدون پکت لاست
⬅️
آپتایم ۱٠٠ درصدی با سرعت +89 مگابیت و قیمت بسیار پایین
گیگی ۱۵٠
⚠️
🔡
براتون پخت و پز کردم، ۳ روزه نخوابیدم، سرورارو بهینه کردم با بالاترین سرعت و بهترین پینگ از الان میتونید باهاش حتی گیمم بزنید، اختلالات به طور کامل برطرف شد و هیچ قطعی نخواهیم داشت
❤️
🍸
➡️
@RUSSIAPROXYY_Bot
⚡️
آیدی ربات جهت ثبت سفارش
⬆️</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNusKlZc7drqjkY41KjBR1E_EE4y0eSUyhHyMRW-lnhVS1iNoJzYgrnSI14ZReIls0MLX0aY0UXp6faoEHfajZrdGcV7OYTpLmJ5oIltjI5GpIINWC5jIJiEgo4_-DWAz2auZYBqyZ9bawIUOToFVB3SlK4t5k8TD1E_HxAPUgV0KGEUIZ9hI6OG1GqI4rUnW-pr5LX4fwKIYjA_ftEOtWFnB3gz5An40ycUijM0R0NQmbrO_1ZBadfXzGHY2zhRDUqK5K6ZPps4KTbEEwPTFrEpivOtM7fQ0I_Mkk4izvLB3AyEMNdalm_k3xbXTILF2KJjeeiXgQj9dtysyQXYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaACeyh5pt5Cn5tN19d9eUjfM5aDC9rJloUTj1W2wa-AqNBGJyNbC0fd0O_kTVXkw171c6y2MkTE9qFxcOftSh-d7WBujGoABEwHcopm6DDD4jBKx5XsnpNmvA4t7L-gv572UXvIwScJZmUN2nNwMnFu-vShId_DUGtl4CxfoaNZ4-zrXaYr1SZL4mEAXB1kLEOzcsG5_UxQ6gNc2XhzYs31QAhG-hUAeiW9VDOy6uZ44DLG8gqcG9hfH0L4SoejtIkp1W4L9BWUFsiGD_kFJFZVCFDKFOVR2GECBUHTBENpCltZNAA9R9RHNb6l0UReZRI6u2jh2sTeISgYMtdpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0NUtabxrn6ieT04iovYrnL-7t5l6h8z8lK_47vNVRslL0oNUVotWNqPTZtjH5eCjJ4UPrC1NXjyQ6K907VxanQDK_cKbRaEmOtdsXWn4xEJ9mz0id1gDO5hg69e1A93pQtThgKgVe1AK1bOCA-WGfBLhfIwLFyEzgT_MsORI3TmOp40yEtVqBgssAfDtgg8A6enURAu0NvsVWkYBGlTRkZHBdxPWXGerwqieODS6AgoatX6bX1_a7ToXv6ty155Ll5oy90DPpIl4jbnSBgo5lNt4xXU-gXm550cQenyler-VF5BqF2c50jhClHWkfp0E583r2DOhwr6HoghlcHCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbfPdO6W-l3r4GgG4d31LoYm5bZoI0EqC1rYIYLmZfe4uCrmlGa9BKZmZ6v5J6jKTPZRMLz08qlqwYXcDF3bBMbYxxLKpfgmOKVtNaigVZYHJMGFX5YKiO8iABqQ6ZNw6wunTKKpc-ZWeHyOt2ec_H7iX_WWRxy95ocTV4YC1adBX4SA6PO0Z-j8C_Pd3BOw-y8re3LV7a1menFkJf1TvpHM6F_THy0Zs2Gq3VPQcMiBgEkGhiDdqmW2CGsFI9mF8XFbQSo6_WuLnoDXRpUbgwScuXJ9XYa_d1W0_J_lv6wOonBNOh9JomXFbpoDcpmIbmaw6vvyQrUitsOzO8rh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihaAyFgvktHCLTr37IALpxnudWALyUkrQF-wSqEfCPWoAGURBivgOex3GmWPZbhBJHATTOFV_xDkn90Aw7sjIkVJSyTnPDuFtHQknChlrLfhF2YdDu6DzIH7NgRxgJvHDxjf3V2cYxZXLlIJm8lLsiOF7QcczOEZV8ZaoTP8iA7JWryuWclL0yXw2xWBj50-g7aoZIJaR0PfgK660AgJYJooyzIKZbajUv_oSnTA_eBRrN-U8ldBy56dhyhx6VYNDH-odYlmgYpm8WdskAs549bBEI9zliGwhIAizlX3O9Fylf3HWID_R3jXTcUtBUMKYZZfpgll_SwdggVGtsJjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1UPPQ7dq-PyllvYwwpCaR0mYdR7SRz4QUfliZMEJcKIXV-GEpLBqt0-_RRR5-posUbeet72Iih3c5N4rIOn3Ynjn1MB8-6kmhLMvLUkjBQD9GHLz65N0yNBLGzb1fQSpJlf0IJnPE7x4o9gMHegsO0ffKi_VG_5SvMO1qYswW_kKSTli2x5pPLB7aT-8Ug_ZM6vO_usIxG09d_rkylRpVO3Yuawna19nDq9Ds1xBA1XlabluAqCl2CQbro0E2lddISUmlheR3aO-eePNyXvdQLhg_dQvJ306upwQXAqfkDxWkzoFAJdtFkY86Ax2mcKQJwne7xNR7PFXALBp8eSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3rm-EOLGkn7XEKKDzViiiY7Jt4FCv7Ra82qWaNaxT4UMtClUHrTsWwyP2QyQb2M-_gyudLKSajWyXPRIbeN5UPnnSDQC4faPy3Aw9wxIzRH7bQrvURZYy5DF_gZkzm6TRjMthWImrRs6p_0uiP7Eepd-WvtUokRUmYjp9r7ktFQ7jsv47Ju72KLzsVOc2ex9IminIgA60ZNh_AnoH9HzWKW6WK5oUhq1m4InYZlTmRW8KUhMnaevOE_PADdeIKzlPz8ceqByZ4o9F7DipWDSvwCkEI17jhA8LdtbZJCJq_rudui-A7iLpymqoEM17yDkwkcF6Dbn5Da5qT0tVJAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJmjz4elOedmn_66tFTD5e6wdqRzh2OeVlCdz1XCdPAeCVaPotkJ0HjYiFcR7mARJn7HPaqgOp49GUte4LIP0loohyiBbV1-AX-M5WtzunB4TzOipll3evgqlw_QvA2DerHBySFfh_dFtdxrpFZIkIN_qeGnMukuhNikrjA1_6Qfi6UBSIjzxinkzzGfGsjFgpNy8v3RT59hwh_Mqf0GYcIeaGo_iIbaa0SPN5G76jTW12ZF1lp6oNQEtjRZ0S2v8KD0PHWzRNbKc8-fLckODqa1zz5Wzeso1QcgC0NvgOHvDMUWiHZEZKm3FZT6LS4r3I8tkHTGfXDlD96cetZtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=DuqeDy5h1xn6WZI8PuYIQ9F1Gk0tFQkUwCFM8P7d1gDvNF4OtTA1Ylq7d0HwyvZJLd9AS9oruOT6Xo3_zqInrIUWSq55IyniM5fd9MmHmSHWYHBxP-c-9LXnAE6wWrnREHpSFFfqC5ldZAiX7MIdgAsEy1yz_SqgPhHTNm6QPT5_H_Pb4JVlp_I3QER77DYC9jvkARsYTx8Gp05i0f9-I98BzMCHyHORyJvU9hgHWo3MHdFO21u8bf_oR9ic0kIMAU1UbiDE7r6SGVv8B_oo5l0kxYqY9eMQinUOFaOG8aAO2HvcBxIyavtcvK-7TKSKihAKuagSPtOayB2U3fophmQZsiAGROEiqiN8ouPZEJv_xUNbvXW2U7VxzCpp9Nxmpncq7HO5Lp1ISVfTJEoRBVvAAlrAerOJv1jcTKj4JpmSoT4oOdSTID3PH_Q4KztgA0a7z8cVuUwZJ_4JgLkG7rcAr2LYK2fh6y6x5EQIL6QPJc7IcQzqUm8EUkG7jhwJh_Ts4ptb1mDUPoLYKkHiOwuuOpWadFhp-Fs67bA8lKCvPGX4PtLi6yqp-7xoQl2q6SEbEDFghCgpZlSfnHvbWnG0Bvw8Rpo5ORLMWqqmGSvZ2ND0WxTU1LrwX5hQhKF0j5C1WME3ObCFcKLvDHn3RHP-4DUPWVGMi1baTcTP4x4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=DuqeDy5h1xn6WZI8PuYIQ9F1Gk0tFQkUwCFM8P7d1gDvNF4OtTA1Ylq7d0HwyvZJLd9AS9oruOT6Xo3_zqInrIUWSq55IyniM5fd9MmHmSHWYHBxP-c-9LXnAE6wWrnREHpSFFfqC5ldZAiX7MIdgAsEy1yz_SqgPhHTNm6QPT5_H_Pb4JVlp_I3QER77DYC9jvkARsYTx8Gp05i0f9-I98BzMCHyHORyJvU9hgHWo3MHdFO21u8bf_oR9ic0kIMAU1UbiDE7r6SGVv8B_oo5l0kxYqY9eMQinUOFaOG8aAO2HvcBxIyavtcvK-7TKSKihAKuagSPtOayB2U3fophmQZsiAGROEiqiN8ouPZEJv_xUNbvXW2U7VxzCpp9Nxmpncq7HO5Lp1ISVfTJEoRBVvAAlrAerOJv1jcTKj4JpmSoT4oOdSTID3PH_Q4KztgA0a7z8cVuUwZJ_4JgLkG7rcAr2LYK2fh6y6x5EQIL6QPJc7IcQzqUm8EUkG7jhwJh_Ts4ptb1mDUPoLYKkHiOwuuOpWadFhp-Fs67bA8lKCvPGX4PtLi6yqp-7xoQl2q6SEbEDFghCgpZlSfnHvbWnG0Bvw8Rpo5ORLMWqqmGSvZ2ND0WxTU1LrwX5hQhKF0j5C1WME3ObCFcKLvDHn3RHP-4DUPWVGMi1baTcTP4x4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puYKSWOj93KZSXVz6BwSYgRzJVET3QtV9H4kwepLxMS_V-RQx9pgrQ6jbfEEAqhkjH4CXOAHlqWcJhR8-KjQyddStAnc2aHv9VnZKKyN-mvZjT5aUfurermOZhc9gT7wOrlL_I4tpKHz5acMPblygYR-wXWIABTOH1VV6RFIqkOevTIB_Qa9QJP2c5MLA9HRlPzVdzPIDLT2THc-OVuEmIWifdku7EyzZ6vt8xd0o9ZFJauTBAGo1fhggu3FB4GDGO29ikprGKE7pcR_2wokNFygI1_jUFWWxK8xKK4gZMk3cFgYXkEYKWhkYUfE0pYzxU0pWBLd_wB6Il7enqZcdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMO0EMjv3R50tMnmwpa_kYbtoH9X4FDBGOATAJak_iX8NQltn9Djwjqz2d6XwTXCiZ0agNwc1F5KflKFi7NbGh_AhpyYhxEVQsITd9eN3Evxu3vY2l23PdxP27_K5ovXHUucWkEfjEY9plALXh37Wm26BdCZ-Cey1j8cjooD99jde4p5PZj6C8tFW6Yp9uYKoTIb2gV8iCQyyzXl4hK8M1uqgNJc02aBN2A9E692pMKZKWlsJQYiWq6TdIIwlUpS00iEj3EXhprSNHQET22nAiIfadZYvryX3D0TFI80l5MrQVl6FHYxs11Ghr9qJaCeCi2hja7oE26umcueHc2wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-EGQNKDbluYeDNJDpKeP7qAB-ikIkv1783H8CEKqmfbAehrkNA1ksyx9VC-AFUNvEe64uY_4_1gHJZLYxcM4wDLOJa9WFlLSrodHYM7to8WTgYV5Da2alxFtJWDyYKls4EpeHwyr68IyRuvJ25LpDEmn3m3jV2jIpbh863L-IOwdFIoG4qvxyv5WgOpYQ-5eCbLEQZDgfZwKyZzUcmOB_D1SMMGoVaW0DwuVyJAg3ovBuNYIFYILIf-usMBjZgmaUZM9BJ1lVxfrJ4G2knsS4vEkbezYyIwoE0ULUUPmmAePKLi1J6kD4I-ZzNV1hQ5XxK7uwOgakviLF6llBhbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=VHPoBBsWZ6iCXefRwmoGDHfQP5dYHCcEZwlQvzJFjWHGshA049Lg2ds_ftR0Y0ocP3SPcLJJTx-Rlr16c8mK8OvCbYDiqLNQwH2GMO37D5ZwwFJ_o8F9AMQXkJtZfbRT9wJtYxNMAfKsPulEehvemOhssNHpkA1ZjBkSjAESLiFre0WfELm3HAUofqmM4vQ6kg3Egdnl3z3C8aNfMR0ul4dT5N0OhS4y8Z2GC05wiw4Vhj2zQlWKQM_4qs6E7OT2P6cxESFyMsRlTh0YiF4aV-uLCPKSJwvb-dZoVPnFEEFxO_pEcLIM5iMOyvSVGly-RpIO2bmKzelM-MPOA0w6UR35i-jDTrP8w2mMvjNzdwgX8bX9kP_GsNNz7u7DoMoCuZgBehW75zIBsqh0LD6nYR5yZ6VmHBJMwcu4f3kikT7LLof0r401RNcIAys8smaEewAQrISHZs956KJL4geTJOkSGoaUcwkxDN_p22IxVHG4WsoSCBRykvbh2H46HVBQTrhatLdW8eCE7YpgDwS1Gyq97KrWq1Lld0bsvzzNtoiFtINfKsISZUlwn3CXicIiFABhcATEnbwvJV8zwBY5PyNLLDMQR9KxWNJhdr_nvv5uUinLyC_BWk6CP5WN0IwH9SldrF1FW-n3BrQYRDyYAUBqifrUQ81rHXJqc_74M9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=VHPoBBsWZ6iCXefRwmoGDHfQP5dYHCcEZwlQvzJFjWHGshA049Lg2ds_ftR0Y0ocP3SPcLJJTx-Rlr16c8mK8OvCbYDiqLNQwH2GMO37D5ZwwFJ_o8F9AMQXkJtZfbRT9wJtYxNMAfKsPulEehvemOhssNHpkA1ZjBkSjAESLiFre0WfELm3HAUofqmM4vQ6kg3Egdnl3z3C8aNfMR0ul4dT5N0OhS4y8Z2GC05wiw4Vhj2zQlWKQM_4qs6E7OT2P6cxESFyMsRlTh0YiF4aV-uLCPKSJwvb-dZoVPnFEEFxO_pEcLIM5iMOyvSVGly-RpIO2bmKzelM-MPOA0w6UR35i-jDTrP8w2mMvjNzdwgX8bX9kP_GsNNz7u7DoMoCuZgBehW75zIBsqh0LD6nYR5yZ6VmHBJMwcu4f3kikT7LLof0r401RNcIAys8smaEewAQrISHZs956KJL4geTJOkSGoaUcwkxDN_p22IxVHG4WsoSCBRykvbh2H46HVBQTrhatLdW8eCE7YpgDwS1Gyq97KrWq1Lld0bsvzzNtoiFtINfKsISZUlwn3CXicIiFABhcATEnbwvJV8zwBY5PyNLLDMQR9KxWNJhdr_nvv5uUinLyC_BWk6CP5WN0IwH9SldrF1FW-n3BrQYRDyYAUBqifrUQ81rHXJqc_74M9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=YG3jIN7gG6w5iZTPrI0FUpT1q8eDRW6CPA8wnYFBmHyKJkzUXtTwB2MM4MRM7_6YGC9BysP82zs7BPZK6RI9IXLFRACBZw-xnzAlBP2tUlRubgtZgB99mq5DkaB9UdEGwWliX3LSVuheClGUhYqivOhLQKlc5TkZkNZGi9UTk60LSoHcT6Ng2XISrwsmgmWYvPuXxmdnFG71y1V9haVWix276KWnE9EbpAgU_QRL4YcDOTujdBfPy2cIjpslwrO6plT_kKbG11rrds8ml2xbhxp7aYVQ-UHa6gLzhtCbiS4s7cejw4yJOZkQr9Ko500qt3cvwaDVi_iLEDUg3OHHJYsDp0XiVJziWEwame7JDGoTaOJdUAoQrURLfT3kpm3MDiQT8WsSpd__mak7sCzaBOTkkNmVmOmEPefTiZuK01B8wLJwt-oiuD2mEcoayLmyt5_2-H1T2lv3xXzh-lNVrAudN4c_nm9xjCZdex4qgJwps8GvUg7CF3y2SkuX7b211fZNQ1U0TS0ZLZ9Ng6ZJbLIMIfHY5s1FLl-9xhiwpHbJLpyC54oh4Pd-qyaipfA-MkmDcbe5HmUeAYbsbskqVfaP23oOcukrTO0a6LKkpQezuCYrm9-gmp6F4TFnWcXk81TV4ail3t6MEkMkgEsmF4dvJcT5oo5k5An1jlJ88FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=YG3jIN7gG6w5iZTPrI0FUpT1q8eDRW6CPA8wnYFBmHyKJkzUXtTwB2MM4MRM7_6YGC9BysP82zs7BPZK6RI9IXLFRACBZw-xnzAlBP2tUlRubgtZgB99mq5DkaB9UdEGwWliX3LSVuheClGUhYqivOhLQKlc5TkZkNZGi9UTk60LSoHcT6Ng2XISrwsmgmWYvPuXxmdnFG71y1V9haVWix276KWnE9EbpAgU_QRL4YcDOTujdBfPy2cIjpslwrO6plT_kKbG11rrds8ml2xbhxp7aYVQ-UHa6gLzhtCbiS4s7cejw4yJOZkQr9Ko500qt3cvwaDVi_iLEDUg3OHHJYsDp0XiVJziWEwame7JDGoTaOJdUAoQrURLfT3kpm3MDiQT8WsSpd__mak7sCzaBOTkkNmVmOmEPefTiZuK01B8wLJwt-oiuD2mEcoayLmyt5_2-H1T2lv3xXzh-lNVrAudN4c_nm9xjCZdex4qgJwps8GvUg7CF3y2SkuX7b211fZNQ1U0TS0ZLZ9Ng6ZJbLIMIfHY5s1FLl-9xhiwpHbJLpyC54oh4Pd-qyaipfA-MkmDcbe5HmUeAYbsbskqVfaP23oOcukrTO0a6LKkpQezuCYrm9-gmp6F4TFnWcXk81TV4ail3t6MEkMkgEsmF4dvJcT5oo5k5An1jlJ88FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT48WaDUzOaoPs4BYf3dYALT6wTtKfSHXIR7SdiU6_nx7OiCGDwkNoZUXjdQrB8J_cPjIyoSC_S-H5_RVmI92t3QgZBfD8RqDAOY4gzqocdC7NIJren68b9ULj4Px3sFmXtr9xqeHtGpZaEZ4KSo-TsU9Adb7GMna9HgpqEpLYvCJSH8BNmIm2rXtojhOpHoHgIgIVhhaEBghhxqIfr6En0ymL0CMVyKE8H-Pr1VSDVBRkiRzsX0GkCmaBZkfisJfCAzWRkZmrceY2r2w9ZEPNU_UC6LGnMC6TdXYbyVXZEyW1L4-e1NQfgoL7krYPNEUVRs9CNDO62j14bGEcAiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=uyC5pNSFJskRuVc0Qkd37R8xGfZXOsXi9UscbMni0og7DUErOttp7Qcn3-yMYLj-oWueSg5zJJ5NPrPNO1XVBMphQHtxqJgkBXb7kx3zcSnCXPwVsjKf-kh3u-WyxDj7utIcs7EhWxOwD6jEY37JCoIKFKpsCgcvgsrFenRVBVdXIQlv3Fa3SQlGwlyppiNszkr--U9SRJb-XTs9fKKy2tIwXFT7gUWbJzEWnOUVljwdCR6HmppNGltKaLkW1Fg6nvXy3HRPUzGP-BmR7yrO_4woyWq6gFqSDFnLlH51ALS5_wzxEa47z9mS1jt9nBOayGCydsOCVsQO4VebG2P7mYaDzeBy_iXNZvVFeMyfZ9QZ7ADp2GrPrKASUbw7XkmyGw6sWlp2DTYxVnoCau_O2Pv5OiLoYn0ebn4Kn0E0u-ejmVQQAiaUYXZPan3MtE1eEkIcHHeZUkEOhqIoV5v-fPWK1kN_-JYslGwM15l9I1WHH4CkLFUwMBlJ1iPWX0L-d-8DTnVD1rE3tYqKPqktYX6GZEQD7scFW909_lT4c-geRApWrHqw5soW8Q00vCSSODthi7SZFVVczTi04mWoagtwBcz1Jqk8LFqUKmK2K987bEoujtYfQ8o1fpLVbbIDtGPK-m8llO5d9h_SdAo9_3FRIyvWMka0RM1bcDLCyww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=uyC5pNSFJskRuVc0Qkd37R8xGfZXOsXi9UscbMni0og7DUErOttp7Qcn3-yMYLj-oWueSg5zJJ5NPrPNO1XVBMphQHtxqJgkBXb7kx3zcSnCXPwVsjKf-kh3u-WyxDj7utIcs7EhWxOwD6jEY37JCoIKFKpsCgcvgsrFenRVBVdXIQlv3Fa3SQlGwlyppiNszkr--U9SRJb-XTs9fKKy2tIwXFT7gUWbJzEWnOUVljwdCR6HmppNGltKaLkW1Fg6nvXy3HRPUzGP-BmR7yrO_4woyWq6gFqSDFnLlH51ALS5_wzxEa47z9mS1jt9nBOayGCydsOCVsQO4VebG2P7mYaDzeBy_iXNZvVFeMyfZ9QZ7ADp2GrPrKASUbw7XkmyGw6sWlp2DTYxVnoCau_O2Pv5OiLoYn0ebn4Kn0E0u-ejmVQQAiaUYXZPan3MtE1eEkIcHHeZUkEOhqIoV5v-fPWK1kN_-JYslGwM15l9I1WHH4CkLFUwMBlJ1iPWX0L-d-8DTnVD1rE3tYqKPqktYX6GZEQD7scFW909_lT4c-geRApWrHqw5soW8Q00vCSSODthi7SZFVVczTi04mWoagtwBcz1Jqk8LFqUKmK2K987bEoujtYfQ8o1fpLVbbIDtGPK-m8llO5d9h_SdAo9_3FRIyvWMka0RM1bcDLCyww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA6pLf06k6_tkCEiCszXen11Vd4t5RVj2csDgqDtToWVvo1OEuQehGhcm2b0lWdpdLcRGoW6KJqab8X3yXH554HwdbTKarAFzg0cie_aePg4wIQ-tSp6DFI49Y_8cXFaO6U3ZMJfMmOonEdTIR6D7GGsGvl5NDMMAb45fVZJTytCOekueSvJkadEQPACTVlc6zqdpBIOnW3EW7_1vyIVWrz5xJmrBeImJ0CPiNzM2TiyupEz6cpVrx8zZMm2qKZJvYc5ugQCKno4FN7WAsHay5AZL5UnYzBSRXNfIFypaqWEX9CKQ7ILMva6T1TZjxPH734kC027KLELj3ts9DmZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUuVLVPq-YNObWOd26qHBPWQ_7eTbjjhoc8diCk9SXPP58oEZDuAYAM56fqBpcg5ACUuARk02q3DhnVmQR5ViRGgV-EsVFH-ex1cN8hGpR66Cy8loKQT0S7pDEa300_ullYbS1TvZAWzeuzDQXzlsuQCVy1mNL0g3uMLaGBxwm99ONHg0FUIuCNZqa9VulQYVE7slnCQSbawvqaHBGVLn3Xy_VZ6z5siyDcpqLwXywura97BCvXbiMSt8XM-fG3H25IZU9gVE42C5wrFr0iZIg-uK5coDX70fNJGnPO7c60AeE-Yxe4-Ei3UsiLJWujjfp4maWixau2cYgHNoPAsOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=tlcN2k-SwW-Y64TQXdSZ3baLhglRw6VK6GCMblbzBsjZGjRz_D4zNJiwGm3FaS4zpYwbaio-G5rc-DaRnlReg3zTJuUoVR5a2mQi_8iJAIXvbodUXg5XYVg0Cn1vxN4kmEIA1hxETFf77lBIRG7uu40OetD8RZ-iddL74sQMCFHUt-_Mkwm8wk0S6Lnr22nvB-t1xdfEI9mtoimbfNGRGFCHKdcdhxn1uI4plq3GVLP8Bd-tMssfQ3Y0X9FBBeTJ7geld_A1iiO772CfjSn5DIo1T_yDCoKyc5vMXS8Ez_Muu-qb_BminPNaeTnzejA8QdK_5R68slJ6gRQylaB5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=tlcN2k-SwW-Y64TQXdSZ3baLhglRw6VK6GCMblbzBsjZGjRz_D4zNJiwGm3FaS4zpYwbaio-G5rc-DaRnlReg3zTJuUoVR5a2mQi_8iJAIXvbodUXg5XYVg0Cn1vxN4kmEIA1hxETFf77lBIRG7uu40OetD8RZ-iddL74sQMCFHUt-_Mkwm8wk0S6Lnr22nvB-t1xdfEI9mtoimbfNGRGFCHKdcdhxn1uI4plq3GVLP8Bd-tMssfQ3Y0X9FBBeTJ7geld_A1iiO772CfjSn5DIo1T_yDCoKyc5vMXS8Ez_Muu-qb_BminPNaeTnzejA8QdK_5R68slJ6gRQylaB5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIhtJ54EKefm-j1v5V9Z_LPPHk9eMC1vuOjulPejNy4fQs70i5c0VYnVvpT3ju0XFatpv6M8mKc0ElQmA2GCorJux2w_jgMYhosYRLQYkio8Xo7Rr7q7ul7p4C-e0CJtrD0lk93a0PIRxM3H6qoMv4_-ZP_IqYrAJvksrBGG-IKGadi2062n_FYAFYviMOUWiXkar-Kk8POF04YmBDL7Q9H9XF_NH4baQC8dXvOgcp2Uekp35Uh77OKlYtlS1fyWaAVKlCqI93kDK7Xa_NCR0vubT2B1RPYM3_nnZO7F8eD2EosRy1eXGxTa3z6Ld_xZ8H4UW7sAG-CCUh08PlG7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMKlNrNOlTbVHB3ycASP0jdsNUTHc0ntF6k_ekCdaoLd7QzbU8AOSdybpXXhgExwP8d8nUmNoAEk_e6fOWG6o8wq-TPH9DLLvECHkbejPwDdZjj_Rx5OCVv0GmLGwiSOdjrPDOMcga1md2CvfSjFzkk1R4CKATKoFG80JHp6-UliGBiCacEHiB9yQy98FPfrbI0nsBNpFECkhNvgYHi_-UJC-zEn1Ge8ygncCh-DuDvImYysRDHiqzfRbs9RWrqverceZxda3O4zsgWE6e2uzBFheuD3GOl1A4H0ufhduqZmWjItPRHjXXnP9JRwbmTWJCw0dsi_c-JjAKIi8OOhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaHV1hnqUkmh2Jn61gcIil7NMYOOZLaErrmi_4NgdzcFSsjN2RQ8UUXDczHFzAJS1NhiwmybL1CGiuLBrFCCGznYTksbPQn6qUJ1PL9pEwZzwP3QuSdL24svQoXq8y-n5UoO8DpyWzVdKeYof3TQ4gIjIV5QZbUfQJvPMUvtZ4elHLxi4wz2aTKSzCJ5IAeXSUgYzOgXW4jpgCbFjl7JUiwuQP77RdCdoo4f0U_7zRwohmvgbtykOfetyFxvIejpAwtKoQLQQTpbRD33kB_xsrEjmAb9raAW387F-o82OMQKPGK6ze5wSdd_NLiaEwhc6AMKbc16Sopctm-ngyl6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=TO64NQC93xu2vD-IHJR4HBulqzmi0qEckiiNYWF0LHsVRX2J5vHzs8XrcjfOL2sZOpFB1cKlYxmAAISwhPvtlNptUf8opbb6mjX6D0Ba6jsg-umXXWdTmswLwA7lzI6rL5p9ACD5mdtRIBjCfNmnj3INVAjaEjZpFJrYzt1wzpmIr0qUCvyFHJKNx__qbnBYHUH_OpUrwvQux13-FKgEeq1HRTox6ozQe41Vw26NjNkdOvt6w1g1RHWYUAeArBGqzDl_sRqI0ayvL2C0BmXGfA5HrcRnpwy4dbXSTa5Tu4bUAidiblcBEOl9ur3UPnNdQPHCMJWkkz1XGXy93-5Oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=TO64NQC93xu2vD-IHJR4HBulqzmi0qEckiiNYWF0LHsVRX2J5vHzs8XrcjfOL2sZOpFB1cKlYxmAAISwhPvtlNptUf8opbb6mjX6D0Ba6jsg-umXXWdTmswLwA7lzI6rL5p9ACD5mdtRIBjCfNmnj3INVAjaEjZpFJrYzt1wzpmIr0qUCvyFHJKNx__qbnBYHUH_OpUrwvQux13-FKgEeq1HRTox6ozQe41Vw26NjNkdOvt6w1g1RHWYUAeArBGqzDl_sRqI0ayvL2C0BmXGfA5HrcRnpwy4dbXSTa5Tu4bUAidiblcBEOl9ur3UPnNdQPHCMJWkkz1XGXy93-5Oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Otq0lVRUZ3xAjU95J1cVAimWszMvuuQ5V_hW5ykkD3_S48JTldSsu-MfkWWyvAxE6q-RDCIY82yaO1hvAPadoPFyf8igqZ7_nCrQ97Td6TBkAjaI2Xa_fW7uKfXomXT9-hKIEH-d14WaXh4mS-ATKHXp331FSH6uIESrFQDHMDU6-OZ7AGVBXc8tt4WAxGM6mQE5GwocIOixB6e-PWxEj_LOr7CEJcDw_rdMfmz9kKsN7sr7IS9me5apJZymUyfved_H9N1Ig5-z6QztlMNhs5I_5-ybBade9mVqzDsl5kHALjO5zWb6X0_Lu2gpXJxzS2p_cVMB_8pDQfGZwnNnB7f3P57w0-5mFuZSfFs5rjonPYj9ogI_S2VPtQBc1kHnxVG40Ko0yKDdH5QXyhZY4CvOkIghLTxRPQrqlUM9F3jvrqgqydKgPHuActk_hUooBqjZGeaU7tptrBUHNfnqqpAFv2UWsoXW8nwI5Gg8oOStuqPB29b3wkvNMdFeSy9QTjNX-V_7pt4t-q-YXfjKcUreu3-M75mxoshveFDumokPr6bZ2ON3IoAZsAKu7v611ty8wPSphFyxg2GjSYqv5xVYPHDaBtIm7bciCEg32cyiG9jqdWK6RZTwifjtkHFzO28ExKa-jxEUqrXU3Nj_7-cH3jaSeFKg4rYlMX-mBI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=Otq0lVRUZ3xAjU95J1cVAimWszMvuuQ5V_hW5ykkD3_S48JTldSsu-MfkWWyvAxE6q-RDCIY82yaO1hvAPadoPFyf8igqZ7_nCrQ97Td6TBkAjaI2Xa_fW7uKfXomXT9-hKIEH-d14WaXh4mS-ATKHXp331FSH6uIESrFQDHMDU6-OZ7AGVBXc8tt4WAxGM6mQE5GwocIOixB6e-PWxEj_LOr7CEJcDw_rdMfmz9kKsN7sr7IS9me5apJZymUyfved_H9N1Ig5-z6QztlMNhs5I_5-ybBade9mVqzDsl5kHALjO5zWb6X0_Lu2gpXJxzS2p_cVMB_8pDQfGZwnNnB7f3P57w0-5mFuZSfFs5rjonPYj9ogI_S2VPtQBc1kHnxVG40Ko0yKDdH5QXyhZY4CvOkIghLTxRPQrqlUM9F3jvrqgqydKgPHuActk_hUooBqjZGeaU7tptrBUHNfnqqpAFv2UWsoXW8nwI5Gg8oOStuqPB29b3wkvNMdFeSy9QTjNX-V_7pt4t-q-YXfjKcUreu3-M75mxoshveFDumokPr6bZ2ON3IoAZsAKu7v611ty8wPSphFyxg2GjSYqv5xVYPHDaBtIm7bciCEg32cyiG9jqdWK6RZTwifjtkHFzO28ExKa-jxEUqrXU3Nj_7-cH3jaSeFKg4rYlMX-mBI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
