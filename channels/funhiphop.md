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
<img src="https://cdn4.telesco.pe/file/gPcOaKS6DkoCkJO8nm6LnzbLNEjstiCgwbdF_LexKG6jt1sbvgKz-JcFe1Btegq7YNVEWxKki57-29DzwaKcGEk6zmH7G840f7it-CuQrgS0ITaFV7zwZfwqDs8NzagVw7BiYLquMgqlJQuifE7c7_pX7Ywl0kGcuVJ0EWCA7RZzjrJwug327-XeRFqZ1r2x3GI6K8dL8vESdysf4miQ1zgob1o00ScjCHsPMHX_X1XblonL-SLy_-KkHz63OLTZ6R7CIKp3uI6mu9DGrNtZCoJZF4rp76BoR9fJzwu9TqpQO_IXn7Sz0vpvwESTKJG9Q2IbYNN3ZmQ9vu36fJ8EyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 183K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 22:37:13</div>
<hr>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانادا پاره شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/funhiphop/79380" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مراکش با امید گل ۰.۰۹ جلوعه</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/funhiphop/79379" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه گل فوق العاده زد مراکش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/79378" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvIdJfLV0xYrAQkIZFmmLgtSfE4xLwGEe2uO4NHqp8pnNyiXjPDFBDOr-UY0zxB7Gt1dvkXdpHwoZVVLnsWHOqrk6wDcG-gkSzV9olpJzFvCYEGjN_QPQ-4FoZxy08QzljNIs2YhOdHKcZhkIX6Bg9Dcv_V9GNiE0FD16L6j3p9LXGlc137ZURTesZQbLse2DC8gy6A6zN61cy6KkJUnpNaTL8KsEy0fK4oBwVfKNAyRK45Sfnv84GqOFdca-JTwR2ZYaSil-lk6dKQ6c0xL9OSE_NWo1T55hD8nZWaU0-CUDoZV5Ml5Cd8cY7yYlZCzr8di81r22V_rpEQCzts0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امثال توماج عادت دارند دستی که برای کمک به سمتشون دراز شده رو گاز بگیرند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/79377" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkW42VDPMMPW4hfOMDQIpcodmYmBP1ENOMohdL-Lw0F_6EIBTvP1PsytTxI5MY7NvSDlH4z2WmeFd9xYrFTB8alBWcXNjzwqMzfyzkxedv0wpQ5tiNLrdp5e9DxAwnwvqbXDFmhiFXUOTsRSsyPr-hbhewDd8m8-7o25n_VTJUMlXYRutl0aqJllyxNku1Cf2zWto54Ae3EuJ92ObN0tAYH0p-gZ8TbX43Y1rCIBV01Y1Y9HP6YZqClrjNwaUtfWtnM7E1bPH_PDV7eiAhINoN_TYvlM71Ft7U1AKAP2Ifp9iZWeWYbzgTBxTk-McWCqL1tzrAn9cm39YA3p1Dy1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/funhiphop/79376" target="_blank">📅 20:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rwAlK5R3G4qdfM0VzlJl8lZePc48qqfIKt4JciI9l8qG0-NEzlWcwoyEiuE-RVMWNGWCY_cqvHa2-bUsUrvPTXpXVC8R7T1h3qCEc9KnshGRhzxlWdTPgac0E3t1qOKIz6l5j-hgPFVYMvmQa4auJBQUFgXYIbB48iOGtwbFAvP5eFWw_HX-w94tbo42KOnHw9mIKQ_8xlrCvb24fKPjMwQTwfsKS4kR5XaawVEZHb3n6AqKOXFfzMMPEO5TI8AiVwwF0XiwDk0Wkq4fjpTP9Ic0609Mz6h83uesh5kxw_3sA3KjbcuBrJUUjq5icGut8EYOM8UsZXMK3Qr1EbqWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
⭕️
سرور "تانل شده" با بالاترین کیفیت!
تخفیفای ویژمون رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 2,500 تومان!
😈
( مهلت خرید تا پایان امشب! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/79374" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ5qt4tWu0YkwBeBqIXVo89TEtu7LHuGB6gNAqT3mxpmva-pH9-IccT3gYW9lBKaJH8PcnwkCNwLUiouFME0aFF6_EA17YQGMUDcuaGszBaz-FF7PbatYoQgRR9YuvivxXmNypQNlVSC8WG-5Cp6Q2F1PkAtpL6703Or0x5WOgIJ4Tr2QFuNFdyFmk7LEaYL063LN0nhgfAQYvR-tqBFRJxD8ITx_Hq2os4bqFFl86h4QgURj4VsyTxcHO-p-Wxs3zhPN5YbYaaTtTenD0xBecUShK-AJKvswyX4BYOZZTHD_eWpCp9UEziCl5xrqXbJckvGCbMH8YbqGclFl17rPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متین بامرام.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/79373" target="_blank">📅 19:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWK5yFnEtcEdkXWesDDA3FHiKefsL75ATXz8PlyH3mMwtElmN1CDTx3ZnZ4Yd9SdoRGP1OX2hsaZfvGs8MA62ZQG5MfmhLb6z4GuFu78T0bRcK84ZnBg-39aMI89ZRliKr9pZQonmT74MMNz5eITXZsOBZYCexi_STV5I3imFxIqn_R6S5RclMsPiPRdo8zdVkH_XvfMYXWOwprMwXLHCXnJQuFOnSw67J7vzpbK-tV_f-kyJKyszcjOYMYB2uMLRRJSA106CpqMqLlrh-sttG8ZzN4ENjpom3wcWMGeTVNRjzLwL-pzVcT29Pdh6UWUUlgQ6O6ga4DMn7BnUSSLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید رضا پهلوی:
به نمایندگان خارجی حاضر در تهران که برای سوگواری بر سر دیکتاتور درگذشته ایران، علی خامنه‌ای، گرد هم آمده‌اید: ایران در حال سوگواری برای او نیست.
ایران برای بیش از ۴۰ هزار پسر و دختر که در تاریخ‌های ۸ و ۹ ژانویه توسط خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به قتل رسیدند، در سوگ است.
این رژیم، مقادیر هنگفتی از ثروت مردم ایران را صرف برگزاری این نمایش تبلیغاتی می‌کند، در حالی که هیچ یک از رهبران دموکرات در آن حضور نداشتند.
آنچه امروز می‌بینید، ملتی نیست که برای حاکم خود در غم و اندوه است. این ملتی است که پر از خشم عادلانه‌ای است، و این خشم و شجاعت قهرمانانه، بقایای این رژیم جنایتکار را سرنگون خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/79372" target="_blank">📅 18:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79371">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byt2dWB1BlZv3gADq-0Z52cPgQexddKf_IT8Kq3_ACeMYa7jWUVQSaukSRYGBt8bJsCYBJ-XF5uxTV_0_9JKNpTM0u8CLXCqU1qYnZmRSxDBu-GSfx9-Rc8CIsX2gyav37Oh02BYQt8GTKMm3uo8gAFbCBx4N401q7hGHTuOwP9ImOEGWWmyO5bqtJmo3qNOuaTGmvQv-DOc0qjUJ6HHu9rZtN48cnqD1TEu98XudF6melrcydbmdqxEO9NdVZOpTWqEUQt2YMejQ8N4QRl562vlWgPHvwSD0bbNwKRukrV0JuB8FS7trqt8Lw6uqTTrzAi9XiacgX4_YSYNNeznsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاراگوئه
🇵🇾
-
🇫🇷
فرانسه
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه فیلادلفیا (لینکولن فایننشال فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- پاراگوئه در مرحله قبل شگفتی‌ساز شد و آلمان قدرتمند را در ضربات پنالتی شکست داد.
- فرانسه در دور قبل در یک دیدار راحت با نتیجه سه بر صفر سوئد را شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی کانادا و مراکش برود.
- با توجه به دیدارهای اخیر و آمادگی فرانسه، برد فرانسه و گلزنی امباپه می‌توانند گزینه‌های مناسبی باشند.
🧠
با پول قرضی یا ضروری هرگز بازی نکنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/79371" target="_blank">📅 18:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1wyNvqu5hpBiSokxk6Rfdk8DRZIzKYMcFkPVcJaSI0BYLE8_0znbXnIReITyBwepzutFGR5zYH4IqjNg6fmjgWYdRTm2nCPgoBIge-3ZBUywCPNJm_7W2YVJnTEqWaE4E9CGFJRVk54PQxxVa_l_ybYoRTlS7_gmsII7akT3-U2qRe7jRYg5QUnqirXCWdkbtEJIArD2Ges1wz88zfm5eywm4CmSSIqWspKnT2mEiAPzzbaUk7mGVbXTptfvYE0qMnQMZ47gD-AcZ6ykS_nb7KBQtkW5dQsoXapyM22sLasFPgcQzjt-MCiYvhICK20YXA1az0gxsVhgwrGWjdeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی اونقدرا که جَو می‌دن باهوش و فهمیده نیست واقعا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/79369" target="_blank">📅 18:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الان تو مراسم یهو یه پرده بزرگ و ضخیم اومد جلوی تابوت حضرت آقا، ما شروع به اعتراض کردیم که این چه وضعشه چرا تابوت رو از ما پنهان می‌کنید؟
💔
💔
💔
که مجری برامون توضیح داد به دلیل تابش آفتاب و وضعیت خیلی خاص پیکر حضرت آقا، مجبوریم فقط چند دقیقه تابوت رو به نمایش بذاریم و دوباره شب ساعت ۸ پرده‌ها کنار می‌رن تا دوباره بتونید جلوه‌ی نورانی این تابوت‌ها رو ببینید.
ما هم نگرانیمون برطرف شد و آروم شدیم:)))
🫠
🫠
🫠
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/79368" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">العربیه الحدث:
دور جدید مذاکرات ایران و آمریکا ۲۰ تیر (یک روز بعد از تدفین رهبر شهیدمان
💔
) بین ویتکاف و کوشنر و باقرشاه و پروفسور عراقچی برگزار خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/79367" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم  می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/79366" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=gzCq6gHRuSTDIA2dal1gNB9FEdaEWFR9mQrIm6ti2oxqas-Xq9y5mRhKaA4ycFiQTMVqkI922wzYSNWK6izfymWRXYIA8CZOME1TybNJl5takQY6dRNDm6xER5ObWXfDTNWebBmH8c-EnlIgl8KrJpzv69ix0sLCDNpiD6lWEsSC0FqUqFJ8oysD--K-x8e5LVzNFqLsaPinbOvP_IS5oqSqdbASVGUpNWKO4e8oWgWqb1ND91-r7OHmnkOarD-Q8uge2IRknMIEUH-NdEq9s6MyiDWzfXSR6xqHPiU71xJant-yUtetMa9_gCOxFh2_TsF4Ti1zM6gSoNUt0uihXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=gzCq6gHRuSTDIA2dal1gNB9FEdaEWFR9mQrIm6ti2oxqas-Xq9y5mRhKaA4ycFiQTMVqkI922wzYSNWK6izfymWRXYIA8CZOME1TybNJl5takQY6dRNDm6xER5ObWXfDTNWebBmH8c-EnlIgl8KrJpzv69ix0sLCDNpiD6lWEsSC0FqUqFJ8oysD--K-x8e5LVzNFqLsaPinbOvP_IS5oqSqdbASVGUpNWKO4e8oWgWqb1ND91-r7OHmnkOarD-Q8uge2IRknMIEUH-NdEq9s6MyiDWzfXSR6xqHPiU71xJant-yUtetMa9_gCOxFh2_TsF4Ti1zM6gSoNUt0uihXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم
می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79365" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79364" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UccoIXgh9J2g6WIEvMKsOfoOgISRVh-qq_T85N0KBpa1qq8hEYILAC0cnxVDD02fyhZ1zTge1DlzylF7ZFL-cm0dPKavXE0zoGzYfz4BPRpe37Thrjqo1IMDmxoxXHLLCOQrHID_jaDf8Osglwo3MxHgj7kA91x3Kd1SDuMhM9610-sVS2Z_TUm7Jl00hsMu9Ph4HHG_J65CtEXnfQpgYsmv8wpKY0oaQ4N_xKI54n1vYsjDqHD1jNGzBykMCvvBRqEUx8D8DAlbus5dPNcwOXBUtRTxa4lwzTLxNgN3OJvSnrGe5Qy0sTxyV_LI_N2swmgzsTKZZpBitXirVaHOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو جنگ ۴۰ روزه سپاه در ازای هر یدونه موشکی که به اسرائیل می‌زد رندوم ۱۲ تا موشک و پهپاد می‌زد تو کردستان عراق.
بعد الان رئیس اقلیم کردستان برا تشییع اومده ایران و چنین شاهکاری رو خلق کرده.
من هر چی بخوام بگم فحش می‌خورم برا همین صرفا به این بسنده می‌کنم که ببینید ترامپ عجب نابغه‌ی درجه یکیه که به اینا کاملا اعتماد کرد اون همه تجهیزات رو راحت داد دستشون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79363" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIKDhx8XbEyrsLMNU9Ve2ecHxSIm0U4eNVjFaqtjDIBkRMTREZnsceNFQQCDQeCtWn5X84Yqyj_0EOzbx6upPFb72vqVzpbEWObhZJP9tgH6rqESBX0yXniDR1lcoXbGGsnRnngelJAQBm6AzMCDUMQKNAsZkgRP6UK7bJuYFz0x-_HGMNjHaoHWM9cD-QrF5Oim4U3VJl1xetLzl72zDjCYQvyMxA01wYbpb1TTRg43Ai7CoYJIrwRf8iOvCJJzwuchlTxCyjZ197hM7nBdvOHf9tY-Bw_8Oy0rE5aoAQpwiQmikD37BIPyKz-AdfcI-0t1nygviag-Jk2WggIkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تسلیت به پدیده به کون ها
دریک رو صعود مراکش بت زده، کپشن زده که میخواد از نحس بودنش به نفع کانادا استفاده کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79362" target="_blank">📅 15:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۱۴۱۱ هم دکی پول ویناکو پس میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79361" target="_blank">📅 14:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWDgXyyqgqtGPKQnX656Fbr5YDP1aRfV2SplTnXkZhXZLVoX61d40Xii8SJzA6uSYJ4S6MzBsBIy1U7Dw0qg4KmkKF6pL3hn9w8cCKz5AwPdUDUHf_lPXGdFGIgqjeaGH4dBxf2YjqNurtiHGISKyG-T7rMe9w41L4kf7v6zWZA4MnL9Mu-z37VUUpxIkpNbM9AwE4Ob7IgPBiOyqYxk0aZtpuAmBIBFea5zAtV58kECJ4yBJVJXJr7NW5gEZHHsmQFPblg4xZIdNWALm3j2J9BwZB1Q4MptzCmNOwjrdfsM2K8Z9gdlg9WiWkJJXmbmyrvZ5TiaaG7_DZEFP7Mbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره، سال ۱۴۱۰ هم امام زمان ظهور میکنه رضا پهلوی حکومتو تحویل امام زمان میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79360" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYW6kaCyczqmMATJDeVP76znaM_3vJM4OrSVUxPte2bB-jxe6mhcSfeMsJZhhjjZVh_Tp3hqNBqhHaWZT3ObpsVF47d0G73C8-ch0x_6W1wM4D0nfcacO1FBsNKQvA1B7GKLVLONJZFQbVBCFaTqjP9KNLFAhLIgyWfjHCCwLTxLOzF5ucqZY8au8kL7yzMUDaCvouc1kPf0BzjVQRpgpiwj9GD1M9XHV1lHmfZYeyqeNE3pCsY8-tfD-KuafpmrQUFZMLLMuGL_K-ldKNiyPyjHKOtsm8B7t0su6DYL4ZT986NT9B9M6Ya3fJ29DEp_pKvaIiW6GhN54oBulMw2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلش نمی‌زد فکرم هزار جا میرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79359" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توماج صالحی از امثال شهبازی هم بیناموس تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79357" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MX67iXLzxN7agTE_nIOYPX7-GtKHj2mHURL3GNMjTU3mkbmf5XzRTFbFhtkY-T7sg__jNCFgq4pq9Yp2vAfkyqaoYponGlXraQ6PS5VyOazbjTYx6jwGnW6d1raale_C7MXgI2K9W1YiFK4yFQqvWgDQbx1RYgCppgHOKMklPaB2Xb8SdW4OEDm8PF09-BbCYKPeLr5AoBlFv3GLqqnPlSHGsg2ZSd86-_o30PRqWvo-sTDiWZJ2jFYDMrwjjvDdXWNeoWBjE1C4iAPFidWOWM1epAi-REMKb6CN9x04oDC-ZTgGwuqkXkszktxWSrlo1DRoj1fnfJbePBZwZbxPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6qFvg7u9lzxp6JQeRUu6wnyh6K5ZCmXNyO_F_nR3xIR8YwCrpZccnsw9ffOuEljaVjzunlorskByBvuc-8boeVfpw_qns2n0y6te37R1YxjiqJhYqxUfSxdwpPW00ksFhs3sOmKbPo8mfmgKL4u_N-xZ5PM6ih-3wjRtxTiVh0jUs2ZBWbw8Ljr9SusHI87QrI2KLA0Cb9oA87nTliqPzbo6wvYDS2j6bJkTBtqlxPgbbLs75N-xd-4PzQKjMFYbfCVPKDE4P6c-S_dPlp0dtBZMQ6fLe-SGaTkfy0LxRcBcOAbuQW4g--Ge52c5ODzTvG02RO6Fk4kCHnVUUncUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو ژاپن کاملا قانونیه که خودخواسته کاملا ناپدید بشید و یه سری کمپانی وجود داره که بهتون کمک می‌کنه که هر نشونه‌ای که از خودتون و زندگی قبلیتون رو‌ پاک کنید و با هویت جدید زندگی کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79355" target="_blank">📅 12:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79354" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79353" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79350">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مسی چندسال جوون تر بود چه رقابتی میشد رقابت امباپه و مسی</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79350" target="_blank">📅 12:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ما نخواییم کشورمون ۴ فصل باشه کیو باید ببینیم
پختیم بابا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79349" target="_blank">📅 12:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کی قراره قبول کنید از وقتی تیما ایتالیایی افت کردن کیر رفت تو فوتبال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79348" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEJjoCAQfzBYfu8ldg3cTsEbWxD9yC6Ij2USZ1a92G9jglVie_Kc2L4FIipuYgOwcV69lx9cz1tfLl5qp_SryAbNBGbBJhpWYg6dRy4F_zB78dSnrjOY75dJ1yr3ovy-bGjmXy_PQe6y414Mul5spT4zxdfO0wAJwQRDsHebN9a1w3tC6EoD_xc8KopzDXMZJIvHHw8gBRT8so9U3XNfDFRYsKnha0y5sls6_8doBK46TPkD6IxWLJdnLq_iBgJzcPNfBOpVZLxRjxNkw0r9Xjw_QIUHaHUicHrtk1fzfjK39AKV_wsiGEtgVA0Vcvk_cx3Bi9DSjHEuPdlrxnVyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب بازی مصر و استرالیا خیلی عجیب بود، یهو استرالیا برا پنالتی گلرشو تعویض کرد، گفتم دیگه هیچی سوپرایزم نمیکنه که چشمم خورد به بازیکنا مصر که داشتن قبل پنالتی هایلایت بازیا رئالو میدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79347" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79346">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj24RH7xXPK2EzUlQEZhSEJggDgceufriLA_7iOnNcI6A66rzVqvzGOrnx0Sas9ctDMwd7f8x2s4qkqxCZdRJ6qicFM8uRcjDnfrEzk7xJNeytq-nIDm9jaScKvxlUoW0AmHV09KhF5X0-tpfgnt54MM9gF7rjS1NykvzNOWFU7r11RIozlUiah_hQe-L833WfPLVIIuFpJK52uiIyhrvGwBYsHc1C5Ity1tD3AugnrmkGEmVqkLxS0P71dkfNmMnf4FisS14nKPbM-Chj5QkZVz0HNVGsaKC1sTixnPaY1obnNTxoVvvmOw4Ro3TBgyvhiePb9FB4S2_gYrqKlbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاراگوئه
🇵🇾
-
🇫🇷
فرانسه
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه فیلادلفیا (لینکولن فایننشال فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- پاراگوئه در مرحله قبل شگفتی‌ساز شد و آلمان قدرتمند را در ضربات پنالتی شکست داد.
- فرانسه در دور قبل در یک دیدار راحت با نتیجه سه بر صفر سوئد را شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی کانادا و مراکش برود.
- با توجه به دیدارهای اخیر و آمادگی فرانسه، برد فرانسه و گلزنی امباپه می‌توانند گزینه‌های مناسبی باشند.
🧠
با پول قرضی یا ضروری هرگز بازی نکنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79346" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al69tOeFAlqmYub83ydxK63Fi3KoflwXVsniLDM8TxCSh5yzfi-vWry_PRFQbBYODizn2VSNCEnOsYjkLimRtjcOgOmnWhj1P3qA6o7FGO1jVy4m36HQp4z3vY_GTiK97VrdPtBN1fr5qmAk0iTcL3y8OTGgQOY6P8uGB5XzaLxzziprniDQBwpKIHpKg0PN0vi4uyYlJJFzuOUG8bs5FwqMzjPTj4XQjSqi07CFwPPRr8ADXHieaTNDKocFG4-s-JWTYD8ZWOeP5g9w___nsMg4ZPWZeznsLVqDbn25pjPPXCQw39tCAK5rA22qg3wx_oVNXmzmSPjBM3nAVTpyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببین حرامز
هم آرژانتین برد و صعود کرد، هم مسی گل زد و هم تیم کشورت یعنی غنا باخت و حذف شد و این یعنی به فاصله چند ساعت سه تا کیر خیلی گنده خوردی.
به نظرم الان وقتشه بری صورتت رو بشوری و یه عنوان آخرین جادوت سعی کنی یه وردی چیزی بخونی که مردم جایی تو خیابون دیدنت فقط یه دور به قیافه‌ت بخندن و دیگه دلقک بازیات و کیر شدنات یادشون نباشه که یه دور دیگه به اونا هم بخندن.
موفق باشی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79344" target="_blank">📅 08:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af167dceef.mp4?token=jNPRgmv7KsBtKyNtlqZGQH76esB7uP55BDhdBWnBI9tIHccH8WTYb35_H2hp_9cP4J4zinZHB6h6b9YV-S-6tnYDvI-pwQuzz4QNFCfNStnPVy8Gfqvd7DOnVp2CDUo1KMZV_C70Xcl5kCvtRNsBo6-RlvDqElPVj6IBjybsu2Z8JERFA4vvBrvWwjRfa81VewlicvsnHEuF1Ubv5sv9I4311HSn66ClCUeUE_6Ecg5RcKA_-MHq2Vja6MPlPe_a_tzFHdKF_iwKa2pjRbe9-VzkcJ7JW_jUpLAGNtW2-Fbwf71IrEvPpvgJjHfscbPml4qw9HfLdnRxlPMdrXfY8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af167dceef.mp4?token=jNPRgmv7KsBtKyNtlqZGQH76esB7uP55BDhdBWnBI9tIHccH8WTYb35_H2hp_9cP4J4zinZHB6h6b9YV-S-6tnYDvI-pwQuzz4QNFCfNStnPVy8Gfqvd7DOnVp2CDUo1KMZV_C70Xcl5kCvtRNsBo6-RlvDqElPVj6IBjybsu2Z8JERFA4vvBrvWwjRfa81VewlicvsnHEuF1Ubv5sv9I4311HSn66ClCUeUE_6Ecg5RcKA_-MHq2Vja6MPlPe_a_tzFHdKF_iwKa2pjRbe9-VzkcJ7JW_jUpLAGNtW2-Fbwf71IrEvPpvgJjHfscbPml4qw9HfLdnRxlPMdrXfY8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 2
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79343" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پروردگار بی همتای فوتبال، حضرت لیونل مسی بهترین بازیکن زمین شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79342" target="_blank">📅 04:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171cc02113.mp4?token=B7SCsjc5hnuz0x4WV6IQa-sXYNfkBCwU2nBS6R87O0orNwVzrBC-efGvyg5VhojnIWnDAcXEIC2t1ilw-Ln82cARR0XMxp3Ue9GGO_yYTzq4sruDwp10Nj2nNg5Z9EE3TdZ57QKO96aL5DKlBXH_OkQ8TvgiXhR8DisB8bJT40yR9EOHexdwfGm3qwX-X1w8_HXLQSV4acuCWSKFwYJXKLdRVklA6GKS4QEIeilSwZIkm7Z4e7f617V-6ooe11x9sFL___bqBnhzkzQnJ6qAHYXiWvfubI2ZBy5DrX0bhUVnQXJbFiU3VKJG6ofr86c46mEO2a0E640ECTvLMCDzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171cc02113.mp4?token=B7SCsjc5hnuz0x4WV6IQa-sXYNfkBCwU2nBS6R87O0orNwVzrBC-efGvyg5VhojnIWnDAcXEIC2t1ilw-Ln82cARR0XMxp3Ue9GGO_yYTzq4sruDwp10Nj2nNg5Z9EE3TdZ57QKO96aL5DKlBXH_OkQ8TvgiXhR8DisB8bJT40yR9EOHexdwfGm3qwX-X1w8_HXLQSV4acuCWSKFwYJXKLdRVklA6GKS4QEIeilSwZIkm7Z4e7f617V-6ooe11x9sFL___bqBnhzkzQnJ6qAHYXiWvfubI2ZBy5DrX0bhUVnQXJbFiU3VKJG6ofr86c46mEO2a0E640ECTvLMCDzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جادگر کصکش من الان اینو چیکار کنم؟
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79341" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تمام ارژانتین صعود کرد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79340" target="_blank">📅 04:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جادوگر بیناموس چیشد پس</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79330" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79329">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گللل سوم هم میزنه آرژانتین
و پاس گل توسط پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79329" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79326">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سیمئونه لاشی از تو تماشاگرا بلند شو بیا بشین رو نیمکت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79326" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایفانتینو کونی کجایی پس، داریم حذف میشیم کصکش</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79325" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این جام جهانی خیلی شبیه ۲۰۱۸ عه
عملا یک مدعی وجود داره همونم فرانسس
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79324" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیمه اول با درخشش پروردگار فوتبال جهان به پایان رسید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79313" target="_blank">📅 02:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاش‌ میتونستم از عمر خودم کم کنم و به عمر فوتبالی حضرت لیونل مسی اضافه کنم
ولی افسوس که نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79312" target="_blank">📅 02:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله اکبر ازین عظمتی که پروردگار بی بدیل فوتبال جهان داره
ترجیح میدم برم وضو بگیرم تا بیشتر از دیدن بازی لیونل مسی ثواب کنم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79311" target="_blank">📅 02:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فرید بیا بمال</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79310" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شاهد حرکات بیرانوندی از گلر کیپ ورد هستیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79309" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خداوند و نویسنده تاریخ فوتبال نزدیک بود بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79308" target="_blank">📅 01:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79307">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79307" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79306">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79306" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79305">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بازی جذاب قهرمان بر حق و تنها تیم بدون باخت جام جهانی با آرژانتین شروع شد.
به امید درخشش جادوگر غنایی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79305" target="_blank">📅 01:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پادشاه باقر امروز یه جوری تو مراسم خامنه‌ای گریه کرد و خودشو زد که انگار این منم که قاتل حضرت آقا هر شب از طریق واسطه پاکستانی بهم پیام می‌ده ?slm chi tanete
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79304" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توماج صالحی رپر خوب مملکتمون تو رتبه بندی جهانی مادرجنده ها قرار گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79303" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">استرالیا با حذف مصر رفت به یک هشتم جام جهانی، حریفش برنده بازی ایران ایتالیاست که فردا ساعت سه و نیم صبح مشخص میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79301" target="_blank">📅 00:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارشگر مادرجنده اسپویل نکن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79298" target="_blank">📅 00:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIJJMp7517npimoQux8aUsvONYNSzbpvW7HAPAByyH9W1EFxtLHRt-2DNBcN__QJccl6OI--q5_8Xz-Ynv0fLuXhEd3bu2oorXrfBE4bL-VJQLfZvrtSdqoU2hcKiIkzb00GYafAxaztGgBSHEdtkLeMgF62x3GL-3FdyZqWsYNhmsFbBxMfjCN5dApcpXBuAJV4aJXCFqAKoHwpXGALqQU2xIip7RSsS90HqclyS26vlta2irOA_JqqVphNpPpBvF7dNIfzdmcviTpFCDjwcMecrFXtLy7UwYpwyqVIAwbwOIENXfLSZqvHLiZdjvKwVyxs7MmKBlIp4-MlYBg3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عجیب اسرائیل به فارسی درمورد مراسم تشییع:
بسیاری از افراد (ما) هم می‌آیند، نه برای سوگواری، بلکه برای اینکه مطمئن شوند او واقعاً فوت کرده است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79296" target="_blank">📅 23:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTO0idbCMmdRZhgjPVdOwMLcORYTW4ycdUK-a5PVKQnhKRv7IbRR3OYoMkMZVS83iWAY0biPHy2E4PkSP4C7LKm1hjTe_rMt0wx2ib4iHOyab9nU38j_JxdO-62cfb_VMfb-CYP5Pwlc2eTvJwtf3V85QQFDZfyH0UNehMDQmoQVIFfdsyhGGPCankjbrWLbfL2DSpaBIcfiOutkNCLk4J4vue5AmoURQnuIAWzXMk_twhOgTyAWzQTFVRRtsEukGU9WGilElU6IpyXJIybMR8Wg0bbHSz7C9NiRYbYlKKXl6mcjM_n-HAsaJfseOd__xDAqzVhAvrYyxwpJvQZ2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه قالیباف:
ترامپ که کشورش ۴۰ و خورده‌ای میلیون نفر گرسنه و نیازمند کمک غذایی داره حق نداره به ما بگه گرسنه و برامون دل بسوزونه.
پولای بلوکه شده هم مال خودمونه هر جور دلمون بخواد خرج می‌کنیم، آمریکایی‌ها بهتره به فکر آمار سوء تغذیه و گرسنگی تو کشور خودشون باشن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79295" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79294" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79293" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تنها کشوری هستیم که توش
هم مرد ستیز هست
هم زن ستیز هست
هم به پسر تجاوز میشه
هم به دختر تجاوز میشه
هم به خر تجاوز میشه
هم ترنسا رو کتک میزنن هم ترنسا رو میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79292" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTOnDeyGKn2pWir2AWV29yLaUGu_KIQZ8N7e07dSu3A3mcCR8VdkPrt6YWFx7I0ae59v6fFzi9YxT5jwpSt4nsfmjwfvqd8euFH7phNbtjeTS1L6rfXsQJPqtJ7ShF8FMCDV1TfclhiBNh2EsyMGeaUhY15_LdLYlmPN4hNe_1ucF7JnZ8LfI8nRoZqYKna1hmQcXruXWtenWjiOiAZ-oGjnxerZ_AS3tiXUzR2ZhsaPOLFTMRB0BNcyFQR97uYsT3G-EHXuVdGBmJA7tdwNeBJOe7eCFa6rrJFg8vVkxDzXpo5DRShSGdy9qfVlxdxAv0CEQmkDC7RhEGivyswqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جادوگر غنایی چرا یه جادو نمینویسه یه دکتر زیبایی بیاد صورتشو عمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79291" target="_blank">📅 21:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvzUZmMw_xq_jYsyxg_7DLA0akKwEw1YF44hV-vjRqzUwqlVbvCOm3fiGbXX0245MtKrLHu6osJ_qcY-GbVnyTa2Uo_PfIJiNr8k3cUUjPiFkuRUOsK_d0qm-5NL7Xl0t2-u4yADxCrYeC3jM2bC8pfa-NnlZVpmzRTjhoEN_kUM_FN6o8g0ZkK6QhQumi9qfVueyTaMKsO4G8GKDUfhrBSKiWPPfNLTvGrcP3Jh4X7aNoRmupHVVl7Nk5aTjIfosNvtI1Mkvp5HbLhlcJK56PxpilzdzfAHeVpn51d_86nuyYewarn2QCvkUYCEGIBtp6gcHHsKxyZwSvIUBLBHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کی رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79290" target="_blank">📅 21:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چندتا سریال تاریخی بگید ببینم بلدید</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79289" target="_blank">📅 21:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79288" target="_blank">📅 20:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyjcx4uwDiQ0HIAQfzAX0Xu3uG1-sPWjyjT4Frb8sxcZz6ZAroy3im-NXNFP8RGMbSohrlUcvfSz2ckzNwCBW2qfnFhrCA_p0qMp8zNhkFtNF560VJXruqEEXlD_toLSfJz8FXOoVPdR5EPp2oo1DCh4W53P5y2xQodk6-2B6NBwOBiUvCtra76-v05_IfzbA86MTKVpbHdYBQvBNc7Gqwp-W_yu5X3qgV-dk4nbLA72LJ4Bz4EUuGfK0_wyxOMRbq2TgCcrIToj2LIn2X_dvKykQw4ORIrblOiOaz7bL-HjebysrLNuCTI9MLpW4M3j5DeemAVrPZDjQIlG8NWOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه عباس یه خوارتو گاییدم عجیبی دیده میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79287" target="_blank">📅 20:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یکی از عجیب ترین چیزایی که تو ترکیه دیدم این بود که تو کلاس دانشگاه نشسته بودیم یهو یکی از دخترا با دستش نماد گرگ رو نشون داد و کل ترکا شروع کردن به زوزه کشیدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79286" target="_blank">📅 20:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIGce12v20WC_-13EMj9iz0wzlyc6FMF7Qq-kYbYWnAop2eZDm60wFDudtJBYmPoRrjmyNrldLlA5DWrV9cyF6_ZgzVPBPgPhtdPt1atIkFEqh-RQo-TnsFmfnwMhUl45Yk7gezN7nxrm2Nng9HUa47g8ipAuhBSFvd_AYp85CRNNjIrtfF4uO61Z2Mo6k-46PlEOPHa1FbUEsZzSpBlG9uFcpzxoPOzPnEq3B1lulKfqF1nq6t_0BovIzww_g6IzrsZYV0ai8KCUsZYZ0oh0uVNDkdNibknViY7R4HHEj1ppaU292A2UihldvCkklRLrVIqJtRu-Qr5mlORiMn4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ژنرال مرحله بعدی با چه تیمی بازی داره؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79285" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-J3Qppni8GbRxdLC5vra-BPM1qxz9cdLO1xQvQj0iUAzZl4vVs_xLdVWLUGleVvT_z8OUhRvNACmMpwPeQ5xVTEBtx3h6SfKp2DUr5sfylTGGuVYvbBWTFOZPIOzrX9CH84WXcSH7pfRaazUznQS27V6D8vOYGOMkO_eWjlamaMUQC89dFA5eNEhoCNL5MOjtbUxRZVP48Y7i_4wkscSJqarCijupN-JmMxa5tdncY5dlOVp2EJsDp3H2obeF0CFvIDjGAyZqjI1HvMP7NQQemuOBGZNA16C6UtRyAbYbM8qj9T5rJlkiqicM9yOT3ghjFvHhbKXNHFmPS6e7UaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79283" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq_Kp-K8BZvn3kMjJncOLErYZwevP9Xnr7vp8v7KXX2myXc711UPYhL0sWOd6edTV_zq14wDgFLNxxgkpcnZU6UHcH5hWbNAMULZhk-ln0Wv-wlTnL4654_ER7yno1kW0O8kmaxyePKen6IDyBIy0bZ-uNeMArl1-OsTSkueWwe31BqYUIwl31JzvmujvTV4pMJhu_VYASmVRns-cJl3FVDsZnoiC0Vtk8FhaxbvXmboiHzPdMtiV4aWR0WMXxBY5PdtMKZpkYDMbQTCwUIcH2dHrsmcxy_qIKNfGdhio2l1ZNdbS8PAyuAyI6nWhKroGrUTKhFUConY1MHHJmLBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهر حیدری و ارام طلاق گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79282" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjS6DmF6Py-u2y_6jwA3bxwQsOIO9SSgdvMjfGTOQLnRTAg8IttWYvECFEvZdh4IiQeTbkjdpU7R5u86ECEjAt6j4d1OevhgYu_d61Lmj0YTfflDXGd2YdEjybO6_2JQtG5tkGFNVsO0AWTEgLoRjoux5XeqCXY-7o1kMmqQnDJEG30hAf8rNO6N8C2uaZr5PpCdygmexRAdtpHBijd3Yzy0r2lpjxqkF5QxPebSxtccOWyYRK_RIkakB0MKYSOBLAoAcFqhYivdgIS_QuERFeaPz80ows-K0yJvlcUUwOEym2M3-IA5PgBro0SMVq1WkcqVxVn_C_VmDOatHzGEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه پاشون لیز میخورد میفتادن چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79280" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xgd3L7c5IaYjTlxQhV5QbkKNm8t8Wk6beBQPh3eOAfAA-eZSiZEtNPfkseKWsEgLDu7bA2U8-Rsxm-fw8v0D75vzSbZoHkJdMIMCFt6sTMXt0reoCPxlZFKgK0D1nZwn3vZ5H50IBdEHi5AUezCABtKuh22PNlVqd1e5jRbH0pApVC25_RYq4Vt6zEFhC1iU3Q2Pr5V_nuEEDwn8Gg57EFsUrJx1Od0MeH4Ncv-VPRjJfUJ6qW3t56P_-cvkTSBE8rbwQZxMVdjZnxjdbXWSl8L0fyIQKePJCwxNyjiDxGUFrQpga5l39NvidAlDXESFnybc07ZO-UvDZrc0XQnACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79279" target="_blank">📅 16:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=Ges1c39ZlFoLSOwKB5a898N9BJ9f5hcZm3nahx0Xm4El663XOfCLEh94iEpDKzw5SdZb4BH4C9KJkJliV2k1LbrUkF6qzxT5xxjFWE-YjyU-WcwDvbX_D3IV-Vw--Mwz9zD_OqlnXms6G7XtuHJ8p2e3JwbzB5SWOHIyjwOQ09RbOJLbmKpidH3JZXpa4Q-DhPHNEZV_UdceP44mLZ-B-Ac7qVJW_Mj8bd7S25EhVNN8SItgBNNFhxs5kaFNPGxEFnw03JCDJzI0U0evSjEVm8djgOBuxHafJ4TWjYuWwPWQSUyOQCHBv74ziYrg3c_lu3oKkcjW_I87DDBk-K_-RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=Ges1c39ZlFoLSOwKB5a898N9BJ9f5hcZm3nahx0Xm4El663XOfCLEh94iEpDKzw5SdZb4BH4C9KJkJliV2k1LbrUkF6qzxT5xxjFWE-YjyU-WcwDvbX_D3IV-Vw--Mwz9zD_OqlnXms6G7XtuHJ8p2e3JwbzB5SWOHIyjwOQ09RbOJLbmKpidH3JZXpa4Q-DhPHNEZV_UdceP44mLZ-B-Ac7qVJW_Mj8bd7S25EhVNN8SItgBNNFhxs5kaFNPGxEFnw03JCDJzI0U0evSjEVm8djgOBuxHafJ4TWjYuWwPWQSUyOQCHBv74ziYrg3c_lu3oKkcjW_I87DDBk-K_-RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کنم دکی پولو زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79278" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینستاگرام مادرجنده من علاقه ای به خداداد افغانی و خیابانی ندارم، دست از سرم بردار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79277" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsXJncqWx_5uq99HaXb98qGsU9xargMMl-v8TePMUSWdQyvi8E0e4FP4ITq4CadIMC1w_jtCV3hvmdbOf_RJOR4zOVi6LcQwAd6Oh4fPx62XJJz66tvkFlkemReo-xnwOHf_whElr2oxd2ZT204ybQuhs7LflxvQyL0mmVWZ8nlNwwXn92avGFeR75eKdHcXKN9AcDOKEi4m4f9dpxJSFtO2tmw6L3n4_XXZBm1x8BDg93Vq_BvtWKMTMH_NGN8r6oIs3uEh9kIn4S8GkAII1z_ibgnxelBJ64zl-uRZLc7mASpQS7KjLK7pbhR4Lk-MZ5IJUc0E0Jw1c4p_ipdsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا تمام مقامات نظامی و سیاسی امروز تو مراسم بودن به جز اسی کوهن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79276" target="_blank">📅 15:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کاش یه مقدار از پولای بلوکه شده رو اهدا کنیم اروپا کولر بخرن باهاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79275" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیروز میثاقی اسنایدرو دعوت کرده بود، بعد میگفت آره ما سه تا مساوی اوردیم شایسته حذف شدیم، اسنایدر گفت خب کصخل وقتی حذف شدی چه فرقی داره سه تا باخت بیاری یا سه تا مساوی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79274" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ungc7janJkKSeBdIsAfAYqpU-3LioWxTlNpL6p1wrX7v93PGnFA9scKEBwoCzkFPa_et4mmnu1RYHd8AW4l8M3w2EW310u47nOijkn4L4d4RIeZLlhStB8qvn42CUH_AP1XuyNdnyK-y_4CxJFD3mul0O4_H2OY6Rih9v_80a1xJCyYqVoG3dNS-XEdLPqH-pnsYUcPnPLZTIXAVIzMoM18mTjata-d3agrNceNrLn-h_I-uxB0C9fI3-cX8cxWjiId6DJ4PuXBn5BrihA2OMQeOfRg-SRwguRFLuk0wPDzjKUAchBru6x0zjmN9utIXJUAqkDbj_r8iw7CPXcCGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سروش سروش ببین چی پیدا کردم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79273" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">درار از جیبت بیبی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79272" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY48ZOw8sOxJ-bCSxH7lnSJd2bWeHhp5FSGvxTpNgGaamy6zGVoZl4eZKNo4H4gHXKIjdITcKxCElauTb0GV9Wg8v8ndV17tCQdhwMo2XHERWPtbeuc4RnWhIOQGuwjda03crbMexSbs9ubrDmxLB7q0BSjNs1kRVcHexxJZRxvFw3rkKh--nNTA6oc3EAraKAX0T2cDcJWGLevYrhqmF3CFpsMooTgLfQDLONoEUbKW5g8thD7RDL1XDQQKjRdwLJiGUtK0Pc2B7M8FMxPbJ_sCsEqrkWepDt6UJHsaqauArxjW_haIZ7oHJrWQ8LS_t8oy17eNKgAZ20FX0sX4lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی اسرائیل  در گفتگو با i24news:
هر زمانی بخوایم کسی را حذف کنیم اینکار را میکنیم. هرکسی الان در ج.ا زنده است یعنی هنوز زمان کشته شدنش فرا نرسیده‌.
همه مقامات ج.ا در دسترس ما هستند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79271" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5PmOpx7KfE7bp90Y5XGmNolsJq2zbgddHRJ9V60YBgCaLkaZBuctFdNLdJT4aKbzVhc5QUXz3ykBTFU2Yb_rUtZ0147YgibawUp4KtRebXwQvTufi8j6tnKQjKoUOpavcjJ73CeXZEczslD0bmrqUqu4ui8sTUIYrPsWFzwT8QRlRAuMsNoMLrZ8GIcPQUDodzyrb54R9Zxdbd2lVjVOfpIsANsbQXQlYTjL1uuyBdxB_SGwBmk_hH-KmyraqeHBWrAb-SVUnwvPByU7bcoOaH-8Kfkt3Phzo2Ylyn-QYApHdyLcF9VypU8uhZahS60SXng3Q-Rooz42M3SS1l7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">که گفتی شاه ساندکلادی؟
😂
😂
😂
😂
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79270" target="_blank">📅 12:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79268">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB1xZbfoXU2mMfEtmqJz6wJhTQ50dzAyGMz5cZhIXzHvk_c_GacmjJdBz3e8PtuKIsFqyRVBphTlr-M0vGiTzrR4ca8Jzxt7m6o6b7RTAjkezimGWQ92jFuGLQOsLfa_Vh3pbUvdij1y5h1gXUHlPrtF_rvTurdoiiZEZ9e0URtKCiSD0oQQnKhs6chmYn_ZR4FhDx9yJTsk16dT1XD7lbpyMCP3YCz8IsDzjf04XqSei6Orc6v35XZsbxa6ZxcXGRw7aVBKMRbtyaB3GD865piuwTfUJA8H-UVocISCgNeSMmCRdWaTfPihzNOhazpT24UIopFZsuqKOvsFoU9rAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این بگه همین که نشستن مذاکره میکنن یکی از اهداف آمریکا از جنگ بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79268" target="_blank">📅 11:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79267">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یه پرامپت خفن میخوام تولید کنم که توش کون نیما بزارم با آهنگ ترویس اسکات، فقط برای ساختش به خود نیما و یه دوربین نیاز دارم</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79267" target="_blank">📅 11:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79266">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4PRdgX3zxow-8WSrIV4KNgpZIPAsZZTdhgp49izQv2aZa_8eA0yDplbYNoZ9q-3zjq0Et3OtMYs8ze2sntQDCEjA2DRWK6ctb0WKHXrdzTmjZuVZIqS60gBgz5ckr7Das6hfREJf8NprL_jE2Qv6lnoym8gsPFWWT9cKZHpLuNqZYu7OiMssfWSffNg1ZB0DN3piipsQv_1uEaO94h1VDTSIa-qW6aODKKLIE6k2N2UkCDaZGDiLo2F23M2j7Qoh2OiLWYFmHcHDOf2OxnNVSa4wL_PauYQ6MRc7SqD5i3hJAxSYVSPrmwKnnexI8b3Bi8LWTr8KU6Zzp5QS16PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت خفن اوردم براتون که تجاوز پنگوئن به سیاوش قمیشی با آهنگ دلخواه شما
(به جای **** اسم آهنگ دلخواهتون رو بذارید.)
A medium shot, front-facing photo of a middle-aged bald man with glasses wearing a plain black t-shirt. He is bending forward slightly, his face contorted in a realistic expression of intense pain, anger, and physical distress. Clinging tightly directly onto his back is a full-sized King Penguin that appears to be straining hard. Both the man and the penguin are staring directly into the camera lens. Photorealistic style, studio lighting, isolated against a solid, put **** Cover's music as background.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79266" target="_blank">📅 11:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShPlDMSY2vRv-dxSoEhmW6kPrvBXqWAGa0SQKrncmGhXpVfyFWDFsq0IB--471kGhggSX2eVLc71QlmFc0g2mS4rnjQwUoscR5SkOvQ7fqmO2qUF5BCPvZRx_ywA1vfcBeQackrscp-zx-DgSXhzVF_REBbQLJeOn9jvUVgrRciQnt_tn5RYQhbY2gQ8SpvrAzcpNtDVlyPcCV5GNK1_fBBXiW9HKptK-Sb4HzGWQ-jV9gE-RmstLy1NCbtBHsC9uQUdNfzQO2NZ1p3Ohap7FuOrUrAB5ak7Ph9BFkuLwGrpj4EPz5nE5tcmP6lJkPq5EjR74OXEXH1VX2BKIxmKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4CpaxDRvlHNZr9SfdgH1gebVX4i3TdxkUT8E4N4oNB00MA6QkeoCsnGChZkjiFeEPrOdEJ1fxW6KnfH_GpyjU-uu1BWb4RmuXpEhbWo21jIRYfz7_dFC0uMi9excxgyu4LDouJmdInNVbqiRTVR4dy0U5u2ZG5XVieI4oRn_ilMZCSa-L6e6Rw3bq_33K5PFwRDIlqjDWomNMHCBAMLvERjHCFZsN-bXycF4xIknNBU1_yM_4v9jBAKABr58bSfTBLQpREY9u16vGBUZ1d75ZEVVgApg802yrTTVp1A2PS8Y3cXdDVmnxQmuv5JIdF5zOSUWKjkLjleHno7FpnAFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پشششماااممم من از الان طرفدار تیم قبرستون اسپانیا و یامالم دلیلشم به خودم مربوطه
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79263" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79262" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زنوزی: تمام مردم ترکیه قبل این که فن تیمای خودشون باشن فن تراکنورن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79261" target="_blank">📅 10:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e68880fd.mp4?token=WnuOZ5sgYGHiFEg7ApVErdhINJyk_o3VqQrHLpCUaYDHt6t-Ya-g61uNuceSiRMqOSZft-Fn9FM8K0nU8GJA06wJtWFZ3gY-Bmsx5U8mrO-hLAGIfKhdcuFccrLHPlnG-OuaD1_K5hEUGOcDbdZ3GMNJgvvp5_Rui1vUUUTl6O5Gfn6z2WTc46CtdYH49d03cQ5BHCM7VtR35E22XoUsZDbEyTdrecXxSqJc5OzgLzgF2t2s6pFZEhR83crhjy9eB5ygM1liIbgb5FGGqSGTuto7vvxUXjLvVxTK2K0D0WO2czk65goEY4PQH7FtIgLPTnnPj1iu9u4hSd3pp26uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e68880fd.mp4?token=WnuOZ5sgYGHiFEg7ApVErdhINJyk_o3VqQrHLpCUaYDHt6t-Ya-g61uNuceSiRMqOSZft-Fn9FM8K0nU8GJA06wJtWFZ3gY-Bmsx5U8mrO-hLAGIfKhdcuFccrLHPlnG-OuaD1_K5hEUGOcDbdZ3GMNJgvvp5_Rui1vUUUTl6O5Gfn6z2WTc46CtdYH49d03cQ5BHCM7VtR35E22XoUsZDbEyTdrecXxSqJc5OzgLzgF2t2s6pFZEhR83crhjy9eB5ygM1liIbgb5FGGqSGTuto7vvxUXjLvVxTK2K0D0WO2czk65goEY4PQH7FtIgLPTnnPj1iu9u4hSd3pp26uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79260" target="_blank">📅 08:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پسر خوب فیفا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79259" target="_blank">📅 04:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79258" target="_blank">📅 02:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79257" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رونالدو بعد از جام جهانی از تیم ملی پرتغال خداحافظی میکنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79256" target="_blank">📅 01:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امشب یکی از تلخ ترین شب های فوتبالی برای رئالیاست
۱: یا شاهد گریه مودریچ و خداحافظی احتمالیش از فوتبال هستند
۲: یا شاهد گریه رونالدو و برآورده نشدن رویای قهرمانی جام جهانی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79255" target="_blank">📅 01:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79254" target="_blank">📅 01:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79252">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXJ3A524eEpZTEmizkjDw9NWa2lNKbXLxAo7Vga6O-FZk3FjSxnQvh_C9TagJEnEaML8DWkXw_o5hrPe2-_GXRWEBjUFhNZuOyqEAzUWkE81n2xfntdN2DLsxDNqN5ZoS3ksUJpxgkguygHTCNrAMIvzGBhpo1aq1Ch0_e2Qls7TrRaUnBQTmvMDvADok0a_WKvEGXkJXYipcCH4jRjbwmR8RYfCD5KQwleWuHH1Gf--iO9YP8iX91fIoxHrFMckKv5-fnZgazlhNlTl8C7bojIDUFSwTRl7DsN7eWcV1wqePvh2s-8q_9MYRvNe9aaNboCXOm3FQLIoFyP5kU7rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگرد سیجله دیگه، زیاد سخت نگیرید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79252" target="_blank">📅 00:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79251">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مطمئنم یامال کرجیه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79251" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79250">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCAQoC6TE8OmKtMeyj8an6j-BGM7TnNWn3l62g6qmAyzOClHgYljBmPhXBtb0HXVxEvkNxMoL1QajC_XE5xR3KXXPQcp_rP_bP_6BOzPQ5UEVb9tlsBIFrhy_Qvm6hfvIWqZbY_Mj90DzaFFuJ67P6MLli2yDl6GM_UePO3YVUHLv_JJdOhTmnQLPUuBWSukGYfB4cdJIvKPnrOM8SCzCXyaU7wbMuoVlmp8CUrbjoBSbAaRo0kv8fppi6QEHbp9EzfMIpQIelUOxJqvFyDXxFgjXzcKGRBK0Ap7EIgwhRM7cd8CV3akgDymMmBKvPZMNStndkSqgBvvwA6GFvEn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و مشخص کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79250" target="_blank">📅 22:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNxBs32hHdcTbWUWSJruKfz97fDYsvOQ6jrF16Z_i84Md7XbCo2u5gfKFykVuGzvXbzT4UPgpiGnjhAo4AEyusF0ui5Thw0lyva8it2IjGT0RF3W2gS19XZeVd8YHVivK5mYKq9EtpWir3b1QK9LUioY8lH6iAob0oKzSMlLEZen3p6xF910A715II9Zcl2hISkClfHG6m9549Vbh_dkHOuWSrkutMKcZfEhRzKjaydMznfC6D7AitJ2U1jujlTVxemVvg1xLdPi2gaNUVui6gzAXIE9ILUul5GrUDbJUtiPPIIddqDhX713GaZm5UzfN9zsdqub--ajjqYDLVES3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام “به زندگی اعتبار نی۲” ریلیز شد.
Youtube
Downloed
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79248" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSNHKMxtqSi1YaU6YG5uVNf_fKxrVw-Ov81PprKKirD-7lgDMslfNtlXhb9w7ZwYG5-v9XD9WNlWIl7wACiDvR7W74zFIG5fWmC5h0TZJVb-hRFYkr6VmUfrKD_HKTu2ZTDAq-rWHru6_M6Um72wzfr8umhnA8qOVm0Tym4SLQ332vSS0cWcvRif1yVGl9zLT4nRceI8ooKcpi8bhA3eImwdiNO3tjUb37ZU6kyJ8sdwZpvz6yD_OcG_H-5D4TOrKbafaCYhojlFtTb9ywoJJR0RANrWbEk8TZmedGCqUH5_rCEb_Cs0BCcEOEIFTyysmNKVqUFIYqqR7jwF3-i1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیوم جان قلب خیلی بزرگی داری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79247" target="_blank">📅 21:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT49MXYRhlWZXHYkrjS5B-HVREnTGfcHp8Zc7CxiYBpADrb3Eq4cBlgWmp9x1bJP_62lmWxt028NI8ZEQCcfIDEMpm7zWtrWULfXOS59aCicvXe3G0QN0x-1NQm-Xloe8JgcI7uNdWKQhoLSwrViPAZif31MtW6G8QFdgXjMTdIYMc5zPlTyxa2PTdoDNmG8-AXCjWqarciIMqkGD8MViSfH5FNybLbJCdSRvy7qGdIIBTgeSJBbx1LgNqQBX_Pa2_Me0fnQQvcUP4BrsLRCPl_7T-kvCD56-KcyAsFqC5RTlI8UkkZKRkFUPJB12qpXLvrNge19tM_Q1JfdeQd0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
با Legovpn وصل بمون، همیشه و همه‌جا
✅
سرعت بی‌نظیر برای استریم و گیم
✅
لوکیشن‌های متنوع از سراسر دنیا
✅
قیمت‌هایی که نمی‌تونی رد کنی
✅
پشتیبانی ۲۴ ساعته، ۷ روز هفته
✅
کشبک ۱۰٪ روی هر خرید
🤑
کافیگت رو بگیر، دنیا مال توئه
🌍
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79246" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">لومر؛ خبرنگار نزدیک به ترامپ:
مراسم تشییع خامنه ای پر از هدف برای تروره. مراسمو بمباران کنید تموم شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79245" target="_blank">📅 20:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آفریقاییا یجوری تو جام جهانی با دل و جون بازی میکنن انگار به برنده غذا میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79244" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه خبری اومده که خروج از کشور واس کسایی که پویش جان فدا ثبت نام کردن ممنوع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79243" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvDCgbzvcmtriRrc_GmFxEc07wOeWrk1ODFMbhbA5I5dAG6d_DEbD-PAbworffxwe3qSWC-omQSkeKWHrjgZaw5s9cVyEou4ehGP-SVbAU0bO3fP8H2iknEYi7CprVNDQNl0hWxqARAOVyOwhj6YKjnmFgcAh6-MyaUe6TsfWCYDf3UzjOBlb7zu6F3EjzDMEs3d3Rm8mQiOq4mbYyf_kPxgehUJLlgX6jddnfwiMpjLbcOU9Qi76GX3yh6xjN9FGnrJSDHXrVDfi1ZXrF-MryrQb4ZBT5HX1874IQlx9nTT34O91O27x6ykoceEPYJH55r84H3WIsxCNZ0Jwu2-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی سه هوش مصنوعی واس مرحله حذفی جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79242" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
