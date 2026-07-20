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
<img src="https://cdn4.telesco.pe/file/KU2x9gC7cdFQxRf6VfrnFb0Qeq4CCntXZpQ00NfSsBA9tWbcID7wZCjw9ocSnocU7VmZkWEh1Uxf23kR2P_A50y_P-4MRML0zDAsUsYFK36EiRd5bjKIq3ycJa2D4ehHP--0H0lFjTVtReNg5KT9TrJ9Upo5Ja7l6LA394GE7dVDGZdVupLk5y02UJxLz4YXIqTuqcb26zwqdG2975RfvPQPUT8LCg1mCJ4fHFxJXJwfQVf-5ywEgqypi3wZW_1g0c7gA7c1HrBXdz7z36y0yxs7DDjXtEvhnXhb3x5tU1oGLcOecP5R3n6GQT7-rOGQNHDKnoSDAyaiwD237M2foQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 199K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 04:30:39</div>
<hr>

<div class="tg-post" id="msg-80863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🥰
فقط گیگی دو هزار تومان
🥰
💵
نامحدود یک ماهه 200 هزار تومن
💵
بدون محدودیت کاربر،مولتی لوکیشن
🤩
مناسب ترید و گیم و یوتیوب و اینستا و..
🔒
ضمانت اتصال تا لحظه آخر
🛫
همراه با ساب لینک نشان دهنده حجم
💿
لوکیشن ها:
🇩🇪
🇹🇷
🇺🇸
🇫🇮
🇳🇱
🇫🇷
🇮🇳
🇦🇪
🇦🇿
🇮🇹
🇵🇱
🇸🇪
🇬🇧
5GIG
▶️
25T 10GIG
▶️
49T…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/80863" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIWOnE8HrWPaDJg8Q5NtNzatdwUWgOP_0KXUdzcJNosDCcCdUuUhai7phLLnvaX99rEuGdLM-Bj7Fig_iTdwIYT7QkqRprwkvw94QKFFUxWFT0Bajfm5mAhx3N4NTtTtsax2LbgfBkgZ_AMHjxh87Y-97QYofEAxBf2SBGnxLQDMZDzQsKlgWVozbxqWH9cCHY7Ro56OEIX0FptPHdkJJt8dUnP__7TsK6ROpdfR_Ro7fDEU0IXaMr5KwRku4JnZSzKgEc0sPKN5AfocBUehqj51poW-2d7fEizCOAws2Ms1YDNlly60sf-fU5_l_XsCnCuThZ21KPFqoCQEZFJa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥰
فقط گیگی دو هزار تومان
🥰
💵
نامحدود یک ماهه 200 هزار تومن
💵
بدون محدودیت کاربر،مولتی لوکیشن
🤩
مناسب ترید و گیم و یوتیوب و اینستا و..
🔒
ضمانت اتصال تا لحظه آخر
🛫
همراه با ساب لینک نشان دهنده حجم
💿
لوکیشن ها:
🇩🇪
🇹🇷
🇺🇸
🇫🇮
🇳🇱
🇫🇷
🇮🇳
🇦🇪
🇦🇿
🇮🇹
🇵🇱
🇸🇪
🇬🇧
5GIG
▶️
25T
10GIG
▶️
49T
50GIG
▶️
195T
100GIG
▶️
345T
😍
با سرعت بالا و پایداری بالا و دارای 10 لوکیشن
🛒
خرید فقط از طریق ربات انجام میشه
⬇️
➡️
@MGVPNNbot
◀️
⭐️
Ch:
@MG_VPNN</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/80862" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umBe_4zQ60ssGLPON2dDwPmi8t6ia8BEQmovQ82kHe0PhH1AjA4QIWzfWysT4jG_Pia6MeP1OCFYw962wr9OS9_0c_fqMzNsmiGLfJdSrFB09e7BZfYYj7rcWLxa7s5aslEMUE--xIOeapkQfxcPAG8ZYMzlNVSRN8KzM7ZKIMXclam10cSa6sK1_e1UWTQPqa_bHJ-J9Yi8MrHpwAf6bwtf5psOQdfrzaEQK_MOLTRS8jyfg8BCT4d2RkPgN2Msmm5fOFH6Wg6_lcmo9As5_Wjf4YOcDiKX-kQ-tLB7lo4yB77Ovi627e6fTPByF5iqpWH-7Ty8bW-rrHiS0JwQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام بار این سفر جذاب و فراموش نشدنی روی دوش تو بود
خسته نباشی مرد
🩵
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/80861" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بسم‌الله
صدای جنگنده غرب کشور</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/80860" target="_blank">📅 02:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حالا که جام تموم شد، رونالدو جان تو کارتو کرده بودی، اون "i'm back" گفتنت برا چی بود آخه مرد مومن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/80859" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ آخر نزاشت تیم ملی اسپانیا یه عکس ملی بگیره تو همه عکسا هست کصکش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/80858" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lf2DcImABFnNKnRA7T1pIjWsie8blA6CyLOheRcLxqC940DNSkdAO8Iuvuozol9RozP95YFogpMYbf248FkOuGT6vkXOb2cWlNEF-Tdxuqi9jbaykS3nDiDZRm_GoYqgC03XEM_WGTDIlbdNLryFuCNuHuJ2HUjQz_W03G3ialIy_jfXyURkBFSg1TyF1Qkwm45Rp9oWAhub87xjbJ2dNr-0hpxJ4A3LjSvyQMSRhPDm1HZF43yc73VaFzI3_ZsNV3FVb-Q5770zAaR4aou7gBukCbriMl-EfbVNDTuJf_GbuXhk39xMESVXTPnLq1xMimeeUCpGCscOJOO0iHMN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر خوشگل و کون بچه بودنت به ایران 2 هفته دیگه مهلت میدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/80857" target="_blank">📅 02:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">علی دایی اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/80856" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب دیگه جام جهانی تموم شد ترامپ زنجنده حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/80855" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بارسا بلد نیست سی ال بزنه چطوری جام جهانیو برد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/80854" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپو یکی‌ بکشه کنار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/funhiphop/80853" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szYvuaZmXFulkyPF2Yur8Eo9xoP9Ma40XC7WFFkkiyCL9S3ZzvhJnZjBARwX9DtcGzKVeKPkk-m9KF7l_nDBAF3gO_c5dHQmWWN4ihLN153pCHL0Y8CxCdFh0mvsBY9w0pGbg0wu6DxICSbKuwVulDCJHuC8394yZZLesoufmeE7HqOFcPwyrJGnX_ko9Epzu3rBuqjm6AUz1s2FRBqw0ymVdTZBnH5Q8R6wfDSs8jcXyrj-Q_PtC3YePPCPqwmh2naCwlclz4q2CCZdcGUTepOE7Md1xNTa6ymi8hmythgwxYMMYhFjDHWfCQSF8_pToZmWv9jbV7owWCHa6ZJSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/80852" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رودری هم به عنوان بهترین بازیکن جام انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/80851" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اونای سیمون هم بهترین گلر جام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/funhiphop/80850" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کوبارسی به عنوان بهترین بازیکن جوان تورنمت انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/80849" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz8QsIwLTF18icYPPinTTah99pyH8n4yxsHIV2Jif3mp5kRCvl4XtewGkUi6nh85bMTVjc9w5Ph0BPCZJ09UtwQH1OKuTw8IJeg4By0tt8bk_Fa4jnoBIVBH_rCDcrMKV1cAO5tBeh9NI_lrL6TWftqUYOZxzjd6FgN_m-WQi_3XuMfI9Jjxr6GBKPXUETpiDykn3n9csklMReloe6--5T5efFxT374AHxI1pcoV6Y3rAOZXmnLEd3LX3whrvUj_KOit2brLntMXTcraoi86jRfrrTKZXezfP-NDBLGB8PcsKhzh9sO53v9nW1S3sETBBSkuvY33DM4y_zrrnHpp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخاری دیگر برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/80848" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd19SVdI57EzAAVGsbMzycrozv9H1KZ9HE7qpMHV9ZebfiBEBgIKNGdca7BoZY97DRsZpBWXaqdGgcR7bM1zEtjTmTtfZQzeoIKKLmUB-uqZlg83hErapP1_MRzBLTyNXVQ0HZQtpEgtjmirOIKqWwgeRHlJtvKh0AgWV2CweRzA1Sz90XbRJrPOYkJYMF_qOt9nEhyBanDJ_Jx26mGWSBWNVmzUXWKjn6ziLVbXaV5mqszHxRKM3E7rQZVfDCHulXWOBfYGZgmEIhJHxWIk8eN_b9KX7L6k87Lo4URHnq2ywv9wL2kUw1dXqcg0FJjxRKRST3M4Lshhgi1iYtcYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/80847" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80846">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/80846" target="_blank">📅 01:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyFj7Sm0-jorZkI_SJasYTH_H031wLrHBvLJ_jncqHZaybcBrTfcPYFfYtLTrzM41c9Eql5qiK2ImWZfLhFTHy71SQw_v1N_EBptoSYJzbl6sLRKQvzlHvIVEVrT1EqgaFGLQNEIpNr7pgyn7XIJigdSSuX0VR4O0okj5ETERD3R0U7MYcuwQTMHNxLPnGpOT-JbtcVbzDi3R8sjNDXqOOCcSzKAen6P94HazU1KEM4dioQEFNEeex9kraHiAQy_YOjWusAXdoyGnEkwR9X_ItLNU4YbML3snbIc8_tKG-96L1FqBEH8Zi8cifCVUZ5pMUVZTIj_dqouVi-wN91oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/meXhywfIUbECGKMewL93uzlzkWzxlpP_3_BgFzdNOQO25ALPU5JA8_sngEY3vsAfVObDar7S1yVkedCTQHwLf97HhsmFIwPyM2agSPD1quT5phGQqkaakZilKCVLu0xSKZJps0l378BxyzAqMo_cc1usSG405hNnbsOJRxf5FfUBfVqI5BI7qQLtEaz5qxupDC26xPxqGmYfsh-wdrf-_7op12zJXLcDwG02iIYDbfL2aERv9lo63KwsOc-nkmk_faJWYs_fxO3vum4l-K5Y5ViLSBsMt-oNbJIeFCx4xwmsV_Bwl6yHZyo7mZQIBiOq_D2XAZUa0o48J16fN3qBGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پارادس چیکار گاوی بنده خدا داشت
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/80843" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خب بارسا فنا حالا وقتشه خیلی سوسکی پرچم آرژانتینو بردارید بجاش اسپانیا بزارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/80842" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسپانیا آورده میگه ببر، صد بار گفتم فقط مصر و کیپ ورد و سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/80841" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw-d04Lp8O-Xieh-x98RylahWIojWsrk8-M8geIH1BT9hU3HVxkBTlv90ueg8xTnxnteQYCNPJguXErtBXGdMA-qzGXwIu1sJoLPFQtHxnlgmBze477PCz6-kfW9MjNh_oih8s4tvrRUOPVrjipPFI-sNjkEwpUrio2lLtVxgaixMaiQt2GQyylsxLJaHff6XArOnLXAcY24HU2wt8EK4WdxgIPTD8wpUmCEBTWuQJD95w8EEW_z5pOs9vGPirjqnIydtpk2Dnx7XNhGEAL3HEAKqaI7qkBM16AofxaqCgMf2Qjep6vh0za4dTev5W3E6TvwbXIgxOH5Zw6sGkfCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟
این دستشو گذاشت جلو دهنش به ما فحش داد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80840" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دریک جان کیرم تو ناموست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/80839" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لامین یه جام جهانی
مسی یه جام جهانی
رونالدو : I'm back
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/80838" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txmTTrWpGOXIwr9dsN9OxwSSJ09B_qbKZMtMbNFlXoWEdtBAUaEgu92m7CpNussxSZ_pevOz7h8SOvkaRzAH63n757X_pc7s8W15smMD8dInFuDsqKZA98snomvn5pxT3SObOdsz0InsMigXOsj502UUq18H96e__q56Zbu1eQJdkaVtZ5bxNomHsKnR9dkPhL3v_8rZbqh5agGOghaL8LnJy6RipT8IcBmi81u7gvHgsJHSKqKendIRV4upf2F5Vxd7YsbmtfyY2hY8F7EaYFNgH8PIzL26tVYJSaJGWMUrEUTVtPTm_rz4tUDJLi_39ScR1bHGBc7BvfE8-5_c-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غروب یک سلطنت همراه شد با طلوع یک سلطنت دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/80836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=uX-cWMMMqWZpVGRiGdT67pBx4atbs3ArvrIAA4VZMcfJiO6n803Q57lhDRdsFAX0dnJy6TxlAdWtKxgiK-urUIQIy5m_SEc9HeNENukCzL3aRTXI-mT74y-X_KPaBaUOY52D5W4MuOlEv3f3CRhxdEzqnnwtNZ6__YXHamR3eTYwR7OReiEE3A9apiaTk4rMsgTcvzF6fG8pLgseLNgENU_uEPjWMS3CzfKoCxYDU_slBLN7rtZw9E4Bqmfex-u3wx-SO4OHsrp8kwlG6qzFfew9dysmgvPJyRFaEne7pbH6s1SRM_UG37BBcEuqx8_lMeP0-edmAxkYH5QEE7Q0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=uX-cWMMMqWZpVGRiGdT67pBx4atbs3ArvrIAA4VZMcfJiO6n803Q57lhDRdsFAX0dnJy6TxlAdWtKxgiK-urUIQIy5m_SEc9HeNENukCzL3aRTXI-mT74y-X_KPaBaUOY52D5W4MuOlEv3f3CRhxdEzqnnwtNZ6__YXHamR3eTYwR7OReiEE3A9apiaTk4rMsgTcvzF6fG8pLgseLNgENU_uEPjWMS3CzfKoCxYDU_slBLN7rtZw9E4Bqmfex-u3wx-SO4OHsrp8kwlG6qzFfew9dysmgvPJyRFaEne7pbH6s1SRM_UG37BBcEuqx8_lMeP0-edmAxkYH5QEE7Q0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/80835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJhFgsGPUJ5OtQhtwARQht0XGao1VIqFesB71jC-Puv3pYj4HOlCsucYxCGL-z8aaTxFS_EfbnuJbGYyC3J2Kgt1wZrwB4WdFFp5cAJalaZKb8TK_RbcVqOTAE8osAmZl4OVLtyA7ZOJBgtKmKL5565TynIz3PjJDanq7kikPDXeZl2HezLlFs1udFgHzVI-TY6ccy3DzInLFo2YjwD1UCvnjtN_9nB3SJZa3w2U0Kd9-AVgjbO1vo_EYptcOxKWP62lme01fIZRfuAxWuAiyOHUwBaA0bR9EmZMmO8eBiZVgYte49tP2r3JQWNCECruc_1BAVZa6sfo6r8M45prbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنا شما بدتر از ایناشو گذروندید اشکال نداره این چیزا
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/80834" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umrQAe1vZfvQfO4HB91GoNBmnrSvjG5P3DHQlKofpulp66dwSlNz_yz0Y-4gaa0JTi77egWmMGna9YkhLY4H4Bfv7-nGRCeOQSJf5Na4DFGaKF6Ic-MSzstDAHjLQF-tjYZcZVmKX2ZnAqlfq7Dfz8fbhDSH3NvSsJSdyaJKWG_Oj2gtEG0-rPfN4An516AvpPElAdmiJ7H5EtUHxLX6Q6jZ_JnfRq_sJk1N5ukqlHv1ESo2C2IHGcWxGmlupW8quE6N7MFShYE-yqn-o9bgdkyfnpzrjqxl-6i0uW5KyU2zxZ85StsLfYIFu2zuHcbP9o8-J7DvDcXFb8qnx32t_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/80833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80832">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اون وسط یکی زد ناموس گاوی رو گایید</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/80832" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80831">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ریدم گاویو کشت پارادس</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/80831" target="_blank">📅 01:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80830">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0ADuK2cpV__myRiHFO956BAcT2TGx9ogTB0HoH3WLxMACUUx5lLKmG0yWPqxn1pADduAtx4pnvMvZXv0-yIa00HY3CGPipBt-INhwEzDkOfP6ZCdfNhikV26SkEksOyLfV1QZCCfX-STJV8PsOPgVEmpKHHyQRBQEEiWjuGLCpspo-jVU7waMAyFLFmnxXDuwditEpqJ4Nur3hTD5jyxIx1USvgWu_4CAYb8hl4wNhB7qFGg00yPnxSDzjygQmhG9aLQYAmEwX-AE_MVvGViv2xcmQxMRwXunPXXWwQYZJHs3UjXqEua1cfEscjprGUGH3DRs3qIswIYCtz3m81Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80830" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80829">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">داداش یامال هم از باخت مسی ناراحته</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/80829" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80828">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مسی چرا اینطوریه، وقتی میبرد گریه میکرد، الان باخته داره میخنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80828" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80827">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اسپانیا قهرمان شه پرتغال میره جدول شانس مجدد که انقد خوشحالن رونالدو فنا؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80827" target="_blank">📅 01:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80825" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80824" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=OnCe2h4iIm1WQh5PZ2absC0NktFs-xDUVYkWWB2v45Z2eYbHJRGbl0ux88H8OFMdGlMmfoc5meZobZupHWEQUAuOAZrKzpysiBXGG_ABvqilkbRCP2DRg3Ycdc3nVrWLgICboZJJLrloMp19RJaUJkI6oxHYCUTyfhyFaHZuQ1p4mhNGDMIEvzODf0-8Ttn3DlP_90dLcWMEh3rCpLV-Bm-fbLrv9VAc-muahJ5Zuw7FyN_C84Ww4uJa3K0Lq-3UZpLGT-Pt7YJeWiVZwvCyabBiFr0P9ukpL6Xrl5IpWk4N_DV02R2_V_aYOnDmMef_NbrBRYA9TjE76qkY3ZUAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=OnCe2h4iIm1WQh5PZ2absC0NktFs-xDUVYkWWB2v45Z2eYbHJRGbl0ux88H8OFMdGlMmfoc5meZobZupHWEQUAuOAZrKzpysiBXGG_ABvqilkbRCP2DRg3Ycdc3nVrWLgICboZJJLrloMp19RJaUJkI6oxHYCUTyfhyFaHZuQ1p4mhNGDMIEvzODf0-8Ttn3DlP_90dLcWMEh3rCpLV-Bm-fbLrv9VAc-muahJ5Zuw7FyN_C84Ww4uJa3K0Lq-3UZpLGT-Pt7YJeWiVZwvCyabBiFr0P9ukpL6Xrl5IpWk4N_DV02R2_V_aYOnDmMef_NbrBRYA9TjE76qkY3ZUAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80819" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الان رونالدو فنا با مسی فنا رفیق میشن بر علیه یامال فنا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80815" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لاپورتا تمدیدش کن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80813" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80811" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بابا یسال گذشته از شروع بازی، چرا تموم نمیشه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80810" target="_blank">📅 01:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80802">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQPnm3DNUvhAphIk15MN6Zty112N6MGEDi9ueOCioR9FDepqgxI1zJmI3fHBE2ry5u3LwazwVOctGMqbAoTM2_AXNenv4slSZJzEHkyN6bEh1u4KtyOpXLpFxKyhbAK-8iVqNB2DSQmqmV90biHhv5VAxaSXBQeJw_gDQY-9THgHFkBrOH88veAOZZmcl9b_06UCAy6VeR2AwFxKkLXWi6ENxubyeCr_A-yuWKpIqzXp3BOSnfMxs56_YCYim-Uf7EeSEU-HPCVmEfiJJ8O4oIxIQ-xXRI8j8TAH12mtzZaUyethYuOEo0OGA3AD2vX_atIIkpG4Vax18r87DaovzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا حضرت سیمئونه و امام مورینیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80802" target="_blank">📅 00:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80801">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این تاکتیک آرژانتین بود ک بازی بره وقت های اضافه
حالا باید ببینیم چه نقشه ای داشتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80801" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80800">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbz0zdIa822iED1AyRx7vG5_5ig3RJ7c3B-hjpIcS7lYmLy9sZxJWcq9WtgXQGrVrWPFGzp5Ck4hwhrZ5KOV86-x8gn3fI2t3bFPzEUHGQGAk4fLpb3-y4DELqHWPxoE2LPYirEY8G3gzrcHge3urfC5dcT2u6Ju3-lTrz1mEQmUqG2GWxEpm4wuRG_iqdZxrN2EMUO_U2QXjowiD0Aiqj3Ahf_OyQ9_QKaquws4LaRv_o0nFD7MI2bP4CP182-1GEA1TByGKERKgdECFqQPkYIBcAqfdrFjF669RCNpjhmRzyzrkbYMa8vhAa2gwe1UCjFS49ZWLrDIdQS0QdeyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یه خطا ساده بود، نباید کارت میداد واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80800" target="_blank">📅 00:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مسی
😂
😂
😂</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80798" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چرا اسکالونی مسی رو نمیاره تو</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80790" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اولمو اژدهاتو صدا کن پارادسو بخوره</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80787" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-yX845oV98S9VZYWZhM20_bEpTOk4DGutqxfxa3L9W_Wr6fA7nWXl2VXId363hyxfADaiGSUg1fgt8LPa_6LdZR_xxrntiNEXbS7VhZW7iUbuySrnHlpC8y0ChaidCmOm-D3YVS-NPfkqN2LWr40n1jN7yC-yqXv8ke4z0P48frDHcTKSWH605sgGYurXoU-bBndZIJvTIawDWEbwTSSOnO2VVBON4wbi2QX2GFkcYEcYBy_vVji55YGPNESPp0BThNTIIC1tnRqkL5DpRX80JArVAWXgiJ5dDCNSkiexGcedODerwoFbtykoypjuIDQKXshLJevvjPwHf71VPAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایت عمو بیژن تو فینال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80784" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80783">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پشمام رونالدو پاس گل داد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80783" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80782">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پشمام رونالدو پاس گل داد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80782" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80781">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نقش فروهر رو سینه اسپید از عمو بیژن بیشتر بود</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80781" target="_blank">📅 23:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80777">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عمو بیژن سیاهی لشکره که
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80777" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیژن ای ایران بخوان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80775" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیمه اول رو بیژن مرتضوی برد
#خلیج_فارس
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80774" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عمو بیژن بیا بنواز بشوره ببره این بازی رو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80773" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فن کدوم تیمید؟
اسپانیا
❤️‍🔥
آرژانتین
❤️
سایر
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80772" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">من فقط منتظر اجرای بیژن و شکیرام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80771" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80769">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تازه دارم میفهمم وقتی یامال تو تیم حریف باشه چقد زجر اوره، بمیرم براتون رئالیا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80769" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80768">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7vTWDJq-iumOstDCA9ekjvhm036BMaeHrOrcnz6jwKEefTckQ2QxXQwSCRtvSwOSiTO8iZgOqsVoqrg1Drn_K5jhVSLhKB79ZtRL2Bz5TjSkYUc0Q3n9C5QqFZTXeVp5llEfYbV3xJg1YSqS8IMSzJ1dG5YYNdvRrVk_r2svLZKSQeEdtrnzBGrN7gArd76z1xMhG2vmDMlIKdTtLOK4qLizITrAywYJz6WV8Vpfbjk_LvpRHIJC3XWixYTMBvvE66Mtn1QOndggRk3XVr3-yxl5UVaK8ypjIlOzA3dyjKC8G0V2DuQC8p9M_rl0VrJKKPDQ4ejd_sgsLgq0xAwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو ببخشید به من گفتن امروز نزارم تکون بخوری</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80768" target="_blank">📅 22:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80766">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj5ow6ALmtG1CFoIN1MRn3smaMBmVnniF4oEq1T3MQEG5zhdWV44XFZdJ8bQSxtnXLu5HW7Z1dB1p2r2B5HuIMXv6X6Ae7SPrZzmbitOlsnLkwQpDDOCCAvahVAyd_HP3eXgJqB_8DtHUytsNpjBpwYeMvhbZugzxUuU7t5H1jBoBNm4gqa7OllmwyUQPo9QUMvplgEIecHoBUoL2RBXqKHVvRpGJVErZ9dGHeAIOyaHl9-1ZfDPDrnZSOCTUsJGAt4OWSHFq9VElq4T5sqftwlbClyQo2qM65ck0pHAa-H309E32VaP1AwMQI6WsNXGNbi3guYwNKONf7uPQZN5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم بروس بافر(گوینده یو اف سی) تیما رو معرفی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80766" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آرژانتینیا هم مثل ایتالیاییا با تمام وجودشون سرود ملی رو میخونن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80764" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هرچقدر میخوام خودمو قانع کنم اسپانیا قهرمان شه برا بارسا خوبه بازم نمیتونم قبول کنم برد اسپانیا رو بخوام</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80762" target="_blank">📅 22:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستان شما نمیتونید کاری کنید کسی که بچگیش مسی یا رونالدو رو دیده و عاشقش شده بفهمه اون یکی بهتر از این یکیه، حالا هی مثل کصخلا فکت و آمار از جام ها و موفقیت های فردی بیارید و روان خودتونو بگایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80761" target="_blank">📅 22:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXBYoNm8TuZdYnGlITsVsm5WfWo9Wtv7uMHia_yFXONrj3dKiIEDmiuY638NCoZlldJ8zWobi3oTxB0IdwIKuVFv9zYWPSmGCBzCXBF98JxjJ4xUdW8_97Ll21HT01C8t1IzctRCwGC8HyHGtrH4MUrX9Ne2ESW_2JRFJRanzFA4kkDkH4O-YbCLjzrnWj-91PFMgr_jG7fV8nKj6ylX72fOyt5Zz3As07s1ddBjTiLgefXkbUVXOHzVAdEMl14ceWcTH9vccfOASoj2N1oAIQPGF1KdXvbCBLmJ33vvnJAISfkQDVsDfUhYMP1jIYYvO_edn4eZv1w47AmwLThrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80760" target="_blank">📅 22:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80758">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSRNf0z4KwzF9oUuiXLKnVNQKze1QW0k4z3yWkpv39whNtmcMVL9hsozEVnA0vR1zK9-wimkZxlsKhjBpAJtP2KqYGU0VKisjavBcMDqcpaczl10IujT6jUt7Nss81C7RH9nWDHPlMGs6DuUO4Zw-z1v_gMKRvs1XVsE6KJPFGk9lrCP4AWo95ErUS_OQ7G6SgbklreYxRHqqNO2MKDYfiGJQx8hbENvclvBnr5x31KzN4PWmZthVj4aJOOOlsN6djRUeZvNCtXXIwfmQhVpCQYOMSfrCaBK2cyt8h_DIHOrnij3D4jAwBS_fHeD3P2T9H899jzt3MScvrLJOJOA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8Gaj26jQqy9GbhfyRZMAxLLkNFOi4paM2XYeWdUvNb23JxJ0rvlQGAehyk7IvPcro8Vvd3QqisDntIVe7fAR3LVWARCtazO9iKQfspUQ6_WdRvhH8BsmeUQHbA6sC91qLRjTZSTReLHgLMvZQd8Zgc9jMY88Exx2yTkSO2tH4qZ65S8FWlvZCtw4bg9Cb_rQ_e9xapBzRFue_UhuXFp_G_5jh2Ws_qsKuuZ3UsyxyAfGdN4tronqNVKiKU_54x1Vjv7FXwdc2A7T3Ks7YzPTTwvmvTIrcCqMEY0PS2VV9NhJV3ZmeZKNnfZ4ObZK9rJjpgYtoSJqwS7fZ7Cjd-Nhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسپید امشب با فروهر رفته تو استیج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80758" target="_blank">📅 21:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xnv5cqjZHsIl5YzRfwMDxxKtQFAhwfem62EU0I9au91FoI5uAtTlbTh_hELcN0oo6rwxvn8n7ZTMAU1-A_RejFYjCPA06mqtP7GLavTNMOaRr8WNHJkpTjEOjfRK66P871p3RtZ7MZBeWYUjqU7sb0n3nUsvrv1HYpcTz6BjfOxIzHdqt9eydlNEz9LAm_debtuR9HchbkRZzESoptFcosLycWrWq2eX0ItEeBvgyWo7UWtAfwY1Kr5vREkyPvmLul2L1SXWa1vZZnWsTr9RdUh45XB_WMh2Lhfgv2VidxYq9puZTcmRaKHLYZdWGFGP1xLFKOfCPxbnXbo3FrZKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjRifUW7Uch6qTDt2jYGNeECml60ZqfSPS1OI4WXoGu_eKyczMyjWBlPE1ibyYEB1rR7O32bPxN8g6bvjb6e_Fm4MbpG59smQ95QqO_rBEo5ooAuy16-P0FOlLDziNXpJe7qWbhxakts_3ValLuxEs-IWicZOFaZla77FcTiTTBuyTKjkgq6v4spK8h9svH8n6ahGFyuvuOJ47Drx8vRQZdhy2kT2WLkXTiaWXXLEUcez269pUhTCCavc6_mBRWeIlclhqDs_mFGW6ig8wXz0eDuoeoRedlCwO9BM-FL-v4QnxmW18hmhD0XibJgCkF4KO3QzNyznvGXKMamO6xgoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنده توپ طلارو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80756" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS_G2JtG6c-5tSY77yKHSZM-VqWOheNE5pCsRfiiVolo8E7nRv5PvMN7x-XplEuqMx3-fMb92cQKha6vtj4tJCKWVVem6xsqReMCM6srQJAtkWO45uSEWmbh1VcZnscdYMidZp_VQpF9QrIRhwtbNDlLRZroQcf4E_UCH70Be-BHuEcd8mapU70jKjdrMgSH3qtB--5D8hLbiOabQo8B0smnyO9MVZInY12GvmgirD76YXd2l5ibNXYu0pzhqH4Yv8sK1PcvWMJrggoaVbYlPeW-U6BC3axlOL3l4Ci_v0TtlmdbAs9HdRBPdqy3khQH1ALvAXd4jCXPBBZZsSXi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
🏆
فینال جام جهانی ۲۰۲۶
🏆
🕔
یکشنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در مرحله نیمه‌نهایی با یک نمایش مقتدرانه، با نتیجه دو بر صفر فرانسه را شکست داد.
- آرژانتین نیز در مرحله نیمه‌نهایی، در دیداری دراماتیک، شکست را با پیروزی ۲ بر ۱ مقابل انگلیس عوض کرد.
- برنده این دیدار، جام جهانی را بالای سر خواهد برد.
- آرژانتین در مسیر رسیدن به فینال نمایش‌های درخشانی ارائه کرده است، اما با توجه به ثبات و قدرت لاروخا، قهرمانی اسپانیا منطقی‌ترین گزینه است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80755" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtYRnyXHwi4v8ZsQEJsCb7J5KTn6tY4cGmj0BEuCjQyswJ9ptsnM_iRf8Bz2O5WDxjhtNgc6wwPRTtFe9qwSFyVXjESRU-Bl6R6xM-aJ8OeQf3OXzl1nmr4HGps6kB-SN4ulxrFxdU6y2HG0j4J0mfFhuEqfbFP81lVQU_pBz1leS5PcJFfYH5dr2lUwK-CXFNJMLyWwYAsmA2iAqe3Hqo_taMyqi9fiXmWQsTvO3Oy6vDVotl-8QcDwPnGl0xeOiuD7A8DF198NljrdB0Y24e7-b73gXGfK5UgHos9uIyHLaGXhUe-RA64MObJ_jQs0eLpa4gYl0IYWymcl1XsHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مامان کریس جنر فوت شده بعد کیم کارداشیان اومده عکس پاهاشون رو گذاشته و میگه مامان بزرگم دوست داشت همه‌ی دنیا بدونن که پوست پاهاش جوون مونده.
پای مامان بزرگه MJ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80754" target="_blank">📅 21:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP9qWN0wD9ZKGLBVRPdYtHdzd1eWbsrVnGPPop9XoQo2eXrK_GsoQI84TMrILSdvg_5FLo7GdRJz24yRfbzrg0FJ5ozpsV2p6tOqBMAxxTrPpbTbf0ZnM4T-fdy_VtVfHxfCqvlI4k9bcg2DzX_k1m3nxYp-QZnQB6U4AYVkWiklEa8M_GgpooSqRCJmxJfYa0h-y4FGpFzogQMS6jZlcH2oAjNw09TLijMEaCJEBflY-41R6zUugx2AqapTu9oHycPCf5JxlcyDodeiPl0a5wPfev2srHW9Wjtsch4nf3-f0mTSyw6hdWMFZI6hm4Cr3zM8OGlfN2Ch6emzF5CNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمت گرم این فینال رو هم برامون در بیار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80753" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-poll">
<h4>📊 کی میبره؟</h4>
<ul>
<li>✓ پرتغال</li>
<li>✓ مکزیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/80751" target="_blank">📅 21:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXkJ2r09Z59BLBwDCJHOgI_eiE2c4F0c-3RbcNl8V1EFiNRPSyLZEueK5NmjnhKocu9nZmUfCY6F_xhiqq71O2iitziRFzh-LXMaH0AqY0vjZr1ZHtMI6Q9Y33egFwjozWIwHbqfYXpEBkg-lw0vznJ72bNCM875WxJ41fT793qiw3QOY6G9WeclMN23cBpC9X8MQu89jHLLHeeTJW1CukJ7k9VGENybrCk11xpBM_RB5aGud3ES5ZCYk4BYqsEHFBwnyL7kzO5nbECMw8qU9ffE1SSHZ9S_14pE_G2WLUFfdurq-z0AbfZjzeC7KdgMOmekF5WYWpFduTxBRo2cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست رونالدینیو
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80750" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره  تا آخرین روز جام نگرانی و استرس داری  ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/80749" target="_blank">📅 21:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره
تا آخرین روز جام نگرانی و استرس داری
ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80748" target="_blank">📅 20:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80746">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">و رسیدیم به آخرین بازی مسی تو جام جهانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80746" target="_blank">📅 20:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80745">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtH8hcGuJbGxtfrqfElNpLT63MEwT8Ze9ChKRZNGbGcdqXiX7b3ul3VE1Mm7fHoTKnkxnf9CqA-ShCumnj6QRIT13luEKU5kiZUhJBi_gCf2nJPsZpSyeO9FyWbly0UEpQWJeTRpN44mZ0Ojz37xBuBFw-2JFDHS9DKqLHuLronPLoG5t7l1FM6Q_V3Ro99uKR-QrkJl_unARxVZpsLl7oq7iOoOoIsTRo6hVPDy3dajA7KhHlR0oID_eCYfql2flJklp1xKXDHDHxML7CpdNIsavJPLSG4qC3pYJMypRp-J8Sa6nYbYU8uGJ5PaBRW-m5fpGYGv-Cur2-0lbLYt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری فران از فناشون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80745" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترکیب دو تیم   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/80744" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80742">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZAOXrzQAj5em_84TlclNJjaRnKE6vdqEnRCe-RYea7er6AwtqFjVc6lZHYL1dR8PGAZ9GGCCRp6R8dKuvBuaUejbpmuv0sIzvwda_XSSvfxsOoaya77Je5Jss82f8j36kU3F-bnt_igcbKlAbI0_4j90vr8VbuPny7hpBaRq96ajAbaj3zK_tRTdpaR6b1FT9J7UX7xxtDZLBR3m4snyVzvDXxzSdaYOMVCDBz_ddEkK4CQnbsGYxqyAMP2OsbSSVfDPE2mNYOHcOrBOV9tw-7BHWW3vmyYBmmRPpWB1dgVpQvdpUfHSHulutjSU_dWEMGW5PuG-_cB_-9zcl395Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkusIygnubGxCaWwEju03pvw9yI58gIBj7VcZfMxpS09ZN8d8OCRvaIQj715lml7tnKpjqeVuX-I3wsTLh7OOl6HcpYkuPCUDJi9h-1AiJBg89ZUI0o9ID-GSdZqP9iIsmcovEuLPiOLTp7u5a_l7kaBwMZ6GS4uy_Gl5KazknBnmeoSspIPxqJ6XEOzh7cu-w_j0bwazYcmAKOtjL_jQQKLn0muCHwYWDeJHSRjHg1W4xDNlBlyPmRIePCVd0McyR8HqbrcTSk5tL_-iBNkHGVIIdXwcybR9JtwaixyutItvaU7bs7URPbr0taqnFu9TQoE5HFOQwIy-TcGfm2t5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/80742" target="_blank">📅 20:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df8VhYncD8WrI1iXUcGdlRAZ2BBVVB_WsNog-LLzF-DBlfAXVe6LnDxHsQtR785HUD0NmM07Mzfr4ALtW3vkK90pT_TucjFADJfAbKGn5hQtn4EJsINHOO9RxNHOfZIopJSXm-quh04mU43KyjlRvzsi8DQKsHuq_cU5EdzG3CFe-Wzyl1zjLWVaUDVveRqxuzPqcmGmtC75IfWeLvK6UCAinKurcIVRGcE_JOfzxPf5418lUnyKJhAXczRLL40lnvuUZI-p1QXInX3I6yy5Caw-436ETWT6ZdG5G6tfG9mqujIwgB3bNBCypVe4Qh2KgMbi4brjIZQ68_hp2HWbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید یکی برا خیابون فینال جام‌جهانی ببره کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80741" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80740">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b6ad923b.mp4?token=Fb7IIBjgHRtSF99jUn7IMRgrARxf0TXD9RXwKdYtXYqYX6eBs7YC0dyrCfdRmLI3IHrljyOm36HApqzsmuldpEPT-rLqLMiBGyUtmlMV1s-lKF-sQgD5bVyFq1oYnniw6A2DFJNR4agdEULdMSnRow5_zjI94XyoAoE-tBC09QngMVqu4ZZtAdlNc8so2KHxf9C6SI0l_H7iIRNBZbpUQSdbdxwF1PYu2krZILlsrpmBwnmRziTu1--OWnRIZvcdVIgcbrQ6gB0fpKrw9fG1GLXUMffDHnGj-FHYiU6N4re5Q4HRi4-KqwqwpTMOoA3l_X0N4i4kwnjXLuyji7nmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b6ad923b.mp4?token=Fb7IIBjgHRtSF99jUn7IMRgrARxf0TXD9RXwKdYtXYqYX6eBs7YC0dyrCfdRmLI3IHrljyOm36HApqzsmuldpEPT-rLqLMiBGyUtmlMV1s-lKF-sQgD5bVyFq1oYnniw6A2DFJNR4agdEULdMSnRow5_zjI94XyoAoE-tBC09QngMVqu4ZZtAdlNc8so2KHxf9C6SI0l_H7iIRNBZbpUQSdbdxwF1PYu2krZILlsrpmBwnmRziTu1--OWnRIZvcdVIgcbrQ6gB0fpKrw9fG1GLXUMffDHnGj-FHYiU6N4re5Q4HRi4-KqwqwpTMOoA3l_X0N4i4kwnjXLuyji7nmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خونه ها امشب
پدر: نگاه به سن یامال بکن
من: نگاه به سن مسی بکن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80740" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80739">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امشب فینال جام جهانیه؟
بازی ساعت چنده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80739" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80738">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسرائیل تو ارتباطات رادیویی جمهوری اسلامی نفوذ کرده و ۱۰۰ دقیقه قبل شلیک موشک ها از هدف همشون خبردار میشه، این موشکی هم امروز تو اردن زدن همینطوری بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80738" target="_blank">📅 19:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80737">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f776ec876.mp4?token=YeqxCLIge4WtoiiAZw0yNdCk29XV6mLxMBehBRxOfZP6-Tqci9wyz7Vrga8hGvB2tSnGEH43Mja52fz-7Lm4pXqdXVBmbsBJqTY6zl20SSiBXK4EMS62CZsuup_AS7g69_gE5Alyo_G6hmva-EgI1gKmR5Zp_lIhOY61zSIgue3d9C8ORTx5tJHsqGKruHenudqcgETQOI5KO99ZqRlH-Kepxg-DmWw0XwnGd7techc7qZE3wsdiAXplguTsrTpk9QYZvgYLaEpKJIQ9V2bm81OE-6s7S2Px324dQnxG5E4u-tUHvlVoBjpLhwK-WscZO06rSVPFnMUM1kHe_gbXlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f776ec876.mp4?token=YeqxCLIge4WtoiiAZw0yNdCk29XV6mLxMBehBRxOfZP6-Tqci9wyz7Vrga8hGvB2tSnGEH43Mja52fz-7Lm4pXqdXVBmbsBJqTY6zl20SSiBXK4EMS62CZsuup_AS7g69_gE5Alyo_G6hmva-EgI1gKmR5Zp_lIhOY61zSIgue3d9C8ORTx5tJHsqGKruHenudqcgETQOI5KO99ZqRlH-Kepxg-DmWw0XwnGd7techc7qZE3wsdiAXplguTsrTpk9QYZvgYLaEpKJIQ9V2bm81OE-6s7S2Px324dQnxG5E4u-tUHvlVoBjpLhwK-WscZO06rSVPFnMUM1kHe_gbXlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این قسمت مصاحبه جدید عراقچی خیلی وایرال شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80737" target="_blank">📅 19:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80736">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه یه نیروگاه برق تو کویتو زده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80736" target="_blank">📅 19:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80734">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80734" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80733">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB1rYcczZLwjHlw-RPOJ9_2MgJzjVrZH26Vf-bgBbh7jWchdifpx70Ap1RpyAWAle8gkAvbaSjJQJVNUXHrbQ3aeaTyWX1z0WbVT1-LLkC0XZaduqP4dRk5VKll0oN03zmLlIw_jR0HG2LiwRluQhNHEbydENtrLqlcj37c5Ld_4On3YNyx8EbPVm5DuN4MwS8BGDE2QHPET7K-PIf6nTX4vlLq4fmFZ6rVIDZrWxipYgPlqE8-o4rfZaiRy54FaYHPbVA2GN-0k4NRm-gPby08r3wFpgwIhXrPeHIlfEdnFp5bQloTS7Se1XzHhpZN4u2vDMK8sh8C6jcWsubTXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80733" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80732">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwb-x399GadiWfmlUgb2ksRCKJtBMXpCNGgcqT6C44RntUlwRYFODOFrkPpkah8zBsjl-SON06QGUPhOqeNFZLi5dkbiFuxJ7tUlx3EqbQ_B8Llb0o3whsr_tzhxS5czGPke9GnYfqEmtU1aQqWdxhN-qMNh-wKiFxPX4YQzHyeN-HpGaUdQFbOgywqDQ27npuWl0-m3_mNQY-2bmZcbo6dtreNUUi5pSrcS83yP2K0XHRtQIzI3E-b81OEtXKwtdklsVeDJKPJA8sZUaNOydfrmoBPj132mrD95bCJKyYpaLeLFr-vOMgyibC4rVINjmU5_-EfLoG1gkiJ2n4r--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا وریا یک اصلاح طلبا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80732" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80731">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خیلی وقته چنلای رپی پست نزدن داریوش ترک‌کرده، حس‌میکنم یه کمبودی تو‌ وجودم دارم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80731" target="_blank">📅 18:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80730">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تنها دکل باقی مونده نرخ ارزون بنزین بود که اونم اینطور که معلومه قراره بگا بره و تا خایه گرون شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80730" target="_blank">📅 17:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80727">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ga9fxx9YYJ3LWO9P-6-mebxbNuwPEv4ug44PawVROKIrOzirS68Us2m-W7e32-hFTKbvQTxHYR93IBBQQ06jp8fBl0OezP96TaoSKlNR2OtXQ1ZNWjUCGZf0hCM56jLCrpY94yyCGrSPV0pRRKxGzCr36mYwpayYg711xPHbIPMgFAE-VOxP2bzSx98tiThFY9gueTZJveYGc72NBOAcgENe6pOCnuf6bqdIr0WrfN_iUibR_jctkl9Y-gY4LVQfzs8pu4JfpyQyUuVqJjdH61mGURsO_JxMAhICGiZWMyRAxqd4MuPAnu5crT27jd-x-4FIOxzbP6LmYt9-ZM-Yow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWExz1FE_kvmrYm_23iBh0YT4d3mlZyjS8-JJ_UKo1ybZWFU-1fYsDVrx2kFl8wJtgK9tffEHi0Q9CUhdHcYlvDHOsmyi-80m3oYIDh4BCfJEomLtGGLGQqINsGrRc8FhCDwwXAFjXWxF8Rz8JZdVHAurrxosCn2q_2UjQi_yESvouXsYghtT8baLkAYSoD1y-iIDvjl-WE9WHBTMaCat8wQlzzoMbn9-YQeXUJqdbRnS1KM_yu7mE1hXP6j1jc403mimAPA60Tvy6oo-Qxzwd7m_Uhi2re6R-WxUFR2cA5zKO7_dVds9P4x2NKIhSaF8yaM0aUtxcxnJvan1C-Vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GAqgpReog9pY3cUuPSDiePCRoNuDEnBmpKOoS0MBrEaK-kyoaxdEiunUrIxtwED56Z5z8zeRrxvigtLh9xlChy9jWqzi71QXY7HWkXBg9bVufOLHthUKKgGv_npJ8dvNcxwqaUakFalTp780UTOX8jUsfHR287vGB848sVccPr4DvB6rv14Vx21XH3mIl97BDUgmtXNCtxADzehuGn4_Lo-4CLMJS_i_aQbFJ5PpwhP0GMbfC6HfA7urDiEubUZ4WDDPnHXlk9PYQWKTYNFdEnbs2T_-JLBCdOE4TP-4Mm81VcSIQ1zgSarPcLSv1BojtHIgJOIAnC3ZaRf9yX7v3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیس ال قلعه‌نویی:
وقتی میام ساعت میندازم و کت‌شلوار می‌پوشم، شما باید بگی به به چه مربی خوش‌تیپی ولی شروع کردید به مسخره کردن!
حتما باید یقه باز بذارم و زنجیر طلا بندازم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80727" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80726">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAvalNetwork - اول نتورک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtXpuWkxlxaNXugGF-Wieq2Llux2iRrQ6sukbuVNUAcD64HcrXxAkU7XfNNiyAHBDkCrCmIYw0ZisehunO_a-mMgdFe8icAF3k0EjPWIdjWLG0U0fM2TM7xgza7qeBR8Wv6WCR1GC526DCYE3C1QmQbQnKwduk1m7xdfcIoWg_a1k61Xz5qB4-Fq4BY72mWgVMemdZzq5JaY3lyZ9JkioQWmVt4nhWHxkXYansHUfhghTa8EHgeb4hz-YtEH1ZEdw990hYoh6F2oJDLEkZtAiE_c0oKZ3KYdkLEUZezuJT01el0c3PiUeYGjcGRfVSGxmu6e_jA9cn9R4ZmWwD6yyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
🤩
فینال جام‌جهانی 2026 رو
رایگان پیش بینی کن و جایزه ببر .!
⚽️
فقط کافیه روی دکمه زیر کلیک کنی، پیش بینیتو راحت ثبت کنی و منتظر بازی باشی.
🔜
زمان بازی: ۲۲:۳۰ دقیقه امشب
کلیک کن روی دکمه زیر و بگو کی میبره!
👇</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80726" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80725">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فرهاد مجیدی اگه سرمربی آرژانتین بود خطاب به امباپه و اولیسه میگفت ما جامو میبریم اونا میتونن توپی که باهاش گل زدن و پاس گل دادنو ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80725" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80724">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5BP00bQkFEObZH_lKRPgGJz5fdClxc9rC-Ai0ZRpANZZMlqXMSoYkCRtNt41nh6Jvv8IF8pQmDN8bKRQ6l_jp0MR_GfVAMSVKF7cYxiOWNKEhEVwJkqeYFhAwuCj6YfW7_msJEnWGqLfwn-G0LG2_1CmPMzPPcuDQr-Y8ZinqLZaUXMtsyND2IMM99mXfye44C3-xSj3Ar8534vYgw6cbK0l2YlHg95psyW0kk6JAht8K5ouQag-ZM6QFFBb7dXZ8P3fQAKOCGAR-FvtO8ee-tukq_2da0DDlU0iWmU0_-HWz67aAbBaQaWI535fPG3oensUQDlImxEuNx4yG7K3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۴  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80724" target="_blank">📅 16:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80723">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">چند تا موشک زدن سمت اردن که یدونه اش بدنه اش افتاده تو اسرائیل و ممکنه سر همین اسرائیل وارد جنگ بشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80723" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80722">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چند تا موشک زدن سمت اردن که یدونه اش بدنه اش افتاده تو اسرائیل و ممکنه سر همین اسرائیل وارد جنگ بشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80722" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80721">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhK-V4pmI3a7cUUEsN-i8OQx3ilvZWRTVwpSoB5kDx5djLJYLUcoF5eXGBb0rNpDhAOS6ZnuV_oiRUW_whw_eHQf187VKz2S6YpvbA927Td0u3I5C-hItGoTm-N_7taj9JPMw-ifZKoTsjbVrLL1Fm7jhd8KXgUtQdykEqmjKJhe1Z6fXu60CQ7pSV185AuUYtzj2YxQ5FHxBEvg_8eJOGZpLjknFCrjs_h0OiJoSoHfwEbn3TMhVh1qQhpB_iGemztAD_jAoq89gsBP-hgouznMmZchMhaJJfqgOIQ3msa6oqY6hZsbL073l3y1dxpUnnuXsVD1fWpXV6nqPz0lYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا یکی دوسال پیش هم همین قیمت بود ولی جلوش بجای تومن نوشته بود ریال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80721" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80720">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biXeEm2xa8vEGQtgkF7TuTt2LKHtshxo06JrHn7t0l0rnmclh7voJ7eoHeFpCGwLBI_iBu2SFM3zmcnDC9iJ3tYpdWZGpC4_A1tMJswMcHrY8qUMc35zCYZHdC4QvAa4l_3TlIHdETxTOXkoJiwMP-bydjWJY5nMMWzgTvOI3vErOvK0uSw-W4XZm8bujmPQ2e6SjZ6_xEntWNVJ9Zx6Azy4V0K2wziUGfXvpauOJVgcSLcBk-8Maf6V9GhS0PlTxPtBPGzkPrXrN189RWViKbUh0tHffERib5hICxr_Crc82-nkVczZUk_7VEkMpPgi4YjWMeuf6wuIAU3-TL34ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی که دیشب باخت ما بودیم نه امباپه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80720" target="_blank">📅 15:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80718">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv5eZ__E6zGECOlkOh-nMXjHOpCoE3R2jA5SDCXIAjxt2JxDdeRFhOsaTH2YTReIs40JQdbdiG6OyVgiAZyryp25fd0N3xNxJpX2ArwABuiBTnHSfYtb0eWyJ1Vuq7YfYNPscuGs7KHEbVpjrBT6Y6ZsyC-VwqVaNn8kxjOYkhiThRLr0dM5P_BOLMhC261_Y8Ik21-3mE1QIHL-ob2lonGFPC85BLRGGYbwbBgs2LTqpa4---27exe-Jvaq0EXKekY26YpOVWe9QoAQ_0myWqMT84Wf_ehwQR_9u75xxTM7BrPrHIaB-gQsrS0B6UL9kGXGVo6zEJ1dJK41pskNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
🏆
فینال جام جهانی ۲۰۲۶
🏆
🕔
یکشنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در مرحله نیمه‌نهایی با یک نمایش مقتدرانه، با نتیجه دو بر صفر فرانسه را شکست داد.
- آرژانتین نیز در مرحله نیمه‌نهایی، در دیداری دراماتیک، شکست را با پیروزی ۲ بر ۱ مقابل انگلیس عوض کرد.
- برنده این دیدار، جام جهانی را بالای سر خواهد برد.
- آرژانتین در مسیر رسیدن به فینال نمایش‌های درخشانی ارائه کرده است، اما با توجه به ثبات و قدرت لاروخا، قهرمانی اسپانیا منطقی‌ترین گزینه است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80718" target="_blank">📅 15:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80716">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امروز صبح گل محمد محمدی جوان افغان بازداشت شده در دی ماه اعدام شد و جانش رو فدای آزادی و آبادی ایران کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80716" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80715">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">امروز صبح گل محمد محمدی جوان افغان بازداشت شده در دی ماه اعدام شد و جانش رو فدای آزادی و آبادی ایران کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80715" target="_blank">📅 14:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80714">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان قضاوت نکنید منظورش کشور کردستانه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80714" target="_blank">📅 14:20 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
