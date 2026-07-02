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
<img src="https://cdn4.telesco.pe/file/YI0GtSt8hTVbTAqnttD0ozQm4pszOccuYQS7N5l55qH5Px_ViJ04Kn5PvRar7_yLyWxoWPM-Mm2pcaZ-dJXiicUEct6eh0D8_jzHi2NJzBs7Ss9QATfHfdbXStRwaC5XPLaOmvToElmZMI3WHPyXGxWmJtxAjiKp3XVawBmRVcRFCUbboR3akn0YKTpFH1j1VqUqUSewsPwLACHUi23iRMI-04tuxwwQdzzW3QWOzPzQyAMoSuNyyq6ufeeB8rdWFqvS2-g-U-UIJgUEyv3uZBCJQ5dqS8428KLi6UsuP5sM0rl0aAB-GFxoUmLLOoj7qsy3LyS8wWDje21pTCWDrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-131437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
زلنسکی از آمریکا مجوز تولید موشک پاتریوت خواست
🔴
در پی حملۀ شبانه سنگین روسیه به کی‌یف و مناطق اطراف آن، رئیس‌جمهور اوکراین از آمریکا خواست به اوکراین برای تولید موشک‌های سامانه پدافند هوایی پاتریوت مجوز دهد.
🔴
روسیه و اوکراین دیشب هم به حملات دوربرد علیه اهدافی که فاصله زیادی از خطوط مقدم جنگ دارند، ادامه دادند که تلفاتی در هر دو کشور داشت.
🔴
ستاد کل نیروهای مسلح اوکراین اعلام کرد که در حملات شبانه روسیه ۱۳ نفر کشته شدند. در مقابل، مقام‌های روسیه از کشته شدن چهار نفر در حملات پهپادی اوکراین خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/131437" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131436">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d606e626.mp4?token=ps_Xore-vwgKqhhzN2TmOeHxlYvb7Mv5FRj2Pi51WoOheG8-nIa60npRsmxRfCCUKy2mVOq6N_hR58762EZBkaan3ddvwhizW7a5x2cPqr3O_vKfSGRe0rlhSTI3e98dhcCa8vDHktHTCeCYXAyrKl0AUHJDkVpFxrOMZVk2geajl79aTflDpWuAe29BhaPYM9ROBNnseWNpZh6h_aavc4ulZWrcuQmDR_lJC-SFDgbfP42JRntn2CWoPlLza5NPI_9rPZxc8WOXn9y5_w2GDgQK28aarfiifumR4Lm-_H1iUgYhGBAAHoy6dSo5eZoKfCmDTTvCIqWqrb0opCO_IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d606e626.mp4?token=ps_Xore-vwgKqhhzN2TmOeHxlYvb7Mv5FRj2Pi51WoOheG8-nIa60npRsmxRfCCUKy2mVOq6N_hR58762EZBkaan3ddvwhizW7a5x2cPqr3O_vKfSGRe0rlhSTI3e98dhcCa8vDHktHTCeCYXAyrKl0AUHJDkVpFxrOMZVk2geajl79aTflDpWuAe29BhaPYM9ROBNnseWNpZh6h_aavc4ulZWrcuQmDR_lJC-SFDgbfP42JRntn2CWoPlLza5NPI_9rPZxc8WOXn9y5_w2GDgQK28aarfiifumR4Lm-_H1iUgYhGBAAHoy6dSo5eZoKfCmDTTvCIqWqrb0opCO_IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بزودی در تهران، مشهد و قم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/131436" target="_blank">📅 15:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4392bc1c10.mp4?token=Tg655rhCVI-UToPFS2mED1ClFaRxyIpJe64sM6gn2bZ33P5JyUULRpVILPEuFN26tNaQO45B-J6BhsQTo8fyo36zT4APInJg1jStYP7_yoJEOHdqj9_UMay-YSKcQqqaA4vNxJPY5KtWLyYRAWDXOfFZLrA61CbAayQZYDlh9JW3IH-k_wBo12QWtKmrojOlOVVQIhflBfnXA0n-ijlMqCUSAbcL_LhsvuIGU2n4eo5kCck93nH4EFrU_fJ0SoiCr3RKQuyB1J--XH-sbmCaPhgM6T8Ht-NfXeeryawHsTVUqw-53Mgvmz9eY7XCofpuFcmK4D7KwhAokJZIkxC4BRefFYyRgxAWbqmC832XimnLpdEyfQth8MZRpHpTNf_-ydByxM_n9YdAOM8Sk4fDKoZO1-7DmlDAI3hMVNRu2kujRnGAB5l4hxSOv4AGVBAYZWoamCQGtQ8vuOnyHkTv0aT44WlfE96fzhAW_RnlRO4D7yZeAFvchr2Brt-v32kVAjrUleNBc1lrOD4Dd5kd6UK1OY07mwrwlznxaZKcXjzbIXvItR6NK0s9XYHaRN6jTJ-TrjlSbPmv946arHpW1nkU6QrnzDydlsrIsqZRIUlD3pgmMjiHfEQV0O4hUB-I0_6RNmX8LB0R8GLF1ge9vws0_ZviAeAek3DU3TeUfVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4392bc1c10.mp4?token=Tg655rhCVI-UToPFS2mED1ClFaRxyIpJe64sM6gn2bZ33P5JyUULRpVILPEuFN26tNaQO45B-J6BhsQTo8fyo36zT4APInJg1jStYP7_yoJEOHdqj9_UMay-YSKcQqqaA4vNxJPY5KtWLyYRAWDXOfFZLrA61CbAayQZYDlh9JW3IH-k_wBo12QWtKmrojOlOVVQIhflBfnXA0n-ijlMqCUSAbcL_LhsvuIGU2n4eo5kCck93nH4EFrU_fJ0SoiCr3RKQuyB1J--XH-sbmCaPhgM6T8Ht-NfXeeryawHsTVUqw-53Mgvmz9eY7XCofpuFcmK4D7KwhAokJZIkxC4BRefFYyRgxAWbqmC832XimnLpdEyfQth8MZRpHpTNf_-ydByxM_n9YdAOM8Sk4fDKoZO1-7DmlDAI3hMVNRu2kujRnGAB5l4hxSOv4AGVBAYZWoamCQGtQ8vuOnyHkTv0aT44WlfE96fzhAW_RnlRO4D7yZeAFvchr2Brt-v32kVAjrUleNBc1lrOD4Dd5kd6UK1OY07mwrwlznxaZKcXjzbIXvItR6NK0s9XYHaRN6jTJ-TrjlSbPmv946arHpW1nkU6QrnzDydlsrIsqZRIUlD3pgmMjiHfEQV0O4hUB-I0_6RNmX8LB0R8GLF1ge9vws0_ZviAeAek3DU3TeUfVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر ایالات متحده آمریکا دولت لبنان را تحت فشار قرار دهد تا دخالت سوریه در خلع سلاح حزب‌الله را بپذیرد، آیا شما با آن موافقت می‌کنید؟
🔴
نواف سلام، نخست‌وزیر لبنان: نه، نه، نه او و نه من به این سؤال پاسخ نخواهیم داد. من معتقدم که رئیس‌جمهور احمد الشراع قبلاً به این سؤال و بیشتر از آن پاسخ داده است.
🔴
از طرف وزیر اسعد الشیبانی، چیزی برای افزودن به آنچه رئیس‌جمهور احمد الشراع گفته است وجود ندارد و من هم چیزی برای افزودن ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/131435" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131434">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پاکستان: دیشب طالبان بهمون حمله پهپادی کرد ولی همه رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/131434" target="_blank">📅 15:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131433">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcwiCJQ3XmW6ozv3CH7OyDLgWmQf29ewHJcyONqmwyGc1bTYY9xAy3rHLVjvN6ILlaWFhnn45FUL0N5DNjcwwYKM1c0W3UA9fQRuFsOUJVx69229Q3r8nl0itVS1nPr6WI0pTU3K5tc8ydxbogGJgXtVKEN0taOR5_EhxjGkdXmzWw-5rUW4bvypDVrRkJcGNdjFAq4GTsO5ojHAJT-A-nG-AQlckUXPqPS3Fh8CpZ1W8UbuBI7o3CXNtarR0VZ5aRtzUefjxQEgaRkwkKksAfqIS8Ce4eN1Yq94EH-DFmyiktO9xqKD1EKuJGzi9ex37bHB8vxhrf1Xm8o4Bw-asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان درخواست ترامپ برای وفاداری بی‌قید و شرط به ناتو را رد کرده است، و وزیر دفاع بوریس پیستوريوس در مصاحبه‌ای با اشپیگل تأکید کرده است که این اتحاد بر اساس اجماع ساخته شده است نه اطاعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131433" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131432">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سفارت روسیه در سوئد اعلام کرد که دوباره با پهپادهایی که یکی از آنها حامل یک بمب ساختگی بود، مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/131432" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131431">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg7K3Wj8HDNSRiRLV_myEeAaL-f2tVqslUaWlHxkdnVYQgTp4G9j7niLAKK9Lm6B24SietE4755O42cfmOsd7z4GfznZfnWAVX9YCJyIC5ne4CEjYkOb5epyFPhNP1Eh_Yzlh-Fr4XgJRa8DHhZxHl0TFSByBoDV74ijglVzmJJ8vtHsJ1ugF17yz2NLzO_8gjN3CnkAyqdKwUMtToRykuMdb_YhnlPbb2HETQtxdPuFW6o-EVzD54N7m3hotZRTsozrz8wgkTdBDYbdZe-FWxdBi-IIgfN8DqqLtDxlyo3PP1HmfXLgFor3D81Sga6K-IqKaFgG7doDkHw9yKNi1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشته های گرمایی در اروپا از 2129 نفر گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/131431" target="_blank">📅 15:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131430">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نیویورک‌تایمز: جنگ ایران چگونه به دلخوری شدید ترامپ و بن سلمان منجر شد؟
🔴
ترامپ هر چه کرد، ولیعهد سعودی نظرش را تغییر نداد
🔴
از لحظه‌ای که ایران تنگه را بست، کل روانشناسی اعراب خلیج‌ فارس تغییر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/131430" target="_blank">📅 14:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131429">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8uR1pBGEder_nMvXzB6KTQpiK3b8xe97Cr0NjqTZz5t8J_KnYKr9GUpzaQPagvDoHW4nGtPOnCho9Nea7gbvboqROvWkBhC9GAH1vWqORnmOqbUwSrs4_oSCO2AL2Ku_3JhWFKs1zlrbgCB01Lah6XE2r27PogKRzlAD3mJaY6X93lSlA1jPMpNkhzo5FpZlPT4axdptDW2aDif-JVBJb_KRAtvvrf0qRRiXhuTyQgdidiMn6LpjPvbZMCruNYl8nKnK7HaO2O4Tuc_tV2trjkd6YV-VG2BZr5QlzZEwbmspVX0BfzQxAq4AHhwhPRS0dO6Tp10ZJKrWcqIZ5MiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد لبنان، عامر بیسات، می‌گوید خسارات ناشی از جنگ از سال ۲۰۲۴ ممکن است بیش از ۱۶ میلیارد دلار باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/131429" target="_blank">📅 14:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131428">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH7YCkMLR1KZlUOn0wXFCSFozrnl80oZ7tG-YC4OmefDVszZ655rSu5Q8pbEJC-Lse2O4XT5DAIp-z3WR6cG182EXKqAIuAre9HRlG5UbyLPT9oltD65tyVJHBRTUVTtyo-WTOEKJDnuUJJIbz9RCZ6bJrewMcP5gQnI47Gf_wT6WAzI4eyMjFBfMk8cZaPOvoSZ0MYr4AiGKOL7Ojd1GCeTA8BNTZIk7juS9YFN87jgxR8ae16aGf9FX_Rz2sALKdDNT0lSw7x1dvgrZA2cvB2JYKTxLxBfZ-IO1JX1uu0_93AncDTjry23XNPNbRyIvAofabX50AdER79tLnHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش شده است که نیروهای روسیه یک هلیکوپتر تهاجمی Ka-52 را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/131428" target="_blank">📅 14:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131427">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
الحدث مدعی شد: دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک براگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/131427" target="_blank">📅 14:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131426">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سخنگوی ارتش : مذاکره، جنگ در سنگری دیگر است
🔴
دست بر روی ماشه، چشم به روی دشمن و گوش به فرمان فرمانده معظم کل قوا هستیم و هر لحظه اراده کنند، وارد جنگ با دشمنان خواهیم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/alonews/131426" target="_blank">📅 14:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131425">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گزارش جروزالم‌پست، پس از وارد شدن خسارت‌هایی در جریان جنگ ایران، سنتکام در حال بررسی انتقال پایگاه‌های آمریکا از منطقه خلیج فارس به صحرای نقب در اسرائیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131425" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131424">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c4dfc3f2bb.mp4?token=tOS52m3PLEpHj9RCfAP34sR8lSczxzPv5z-jRcDHmha79Mkv3HF7Mp5Q3MotIg9F7jN8emfaON_cxVmgd9q9c0TpH_ZMIT6kwTyzmWyJweyxJvXnx9P_wfRHJHtjYYVma4tQz8vqQ6fXM28sWrNOr2pcESlLtI_gUEbhbkTnNmrVv3jyZDR-hbZBy8dAqaILoQs8pzkiptYFJ7Nsawq1TCrvvxCr9G1mH-KVCdk-dqplXl1N_wd1GGfBiG_gRO2WqSt3fFvzaEs-XVyIYcmWf90EcJSoY3A1ShIkSenhwOi_XsFxKF0-e-fqBGFcU7GsVAuLCWF_lhqE4yY0sDuDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c4dfc3f2bb.mp4?token=tOS52m3PLEpHj9RCfAP34sR8lSczxzPv5z-jRcDHmha79Mkv3HF7Mp5Q3MotIg9F7jN8emfaON_cxVmgd9q9c0TpH_ZMIT6kwTyzmWyJweyxJvXnx9P_wfRHJHtjYYVma4tQz8vqQ6fXM28sWrNOr2pcESlLtI_gUEbhbkTnNmrVv3jyZDR-hbZBy8dAqaILoQs8pzkiptYFJ7Nsawq1TCrvvxCr9G1mH-KVCdk-dqplXl1N_wd1GGfBiG_gRO2WqSt3fFvzaEs-XVyIYcmWf90EcJSoY3A1ShIkSenhwOi_XsFxKF0-e-fqBGFcU7GsVAuLCWF_lhqE4yY0sDuDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار تلفات زلزله ونزوئلا به ۲۲۹۵ کشته و ۱۱۲۶۷ زخمی رسیده است و نزدیک به ۵۰ هزار نفر هنوز ۹ روز پس از وقوع اولین زلزله مفقود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131424" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131423">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری / العربیه: دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131423" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131422">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
استاندار تهران: اینترنت قطع نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131422" target="_blank">📅 13:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131421">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ادعای شین‌بت اسرائیل : یه شهروند تاجیکستانی رو به بخاطر جاسوسی برای ایران، دستگیر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131421" target="_blank">📅 13:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131420">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
استاندار تهران: اینترنت قطع نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131420" target="_blank">📅 13:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131419">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd28bd491.mp4?token=OBnOfBZsWuYD5dxCMPMEgK59kUig9Lp8dzUG7JsJkBIkH1zq85QVRHaSD_fimOq61kqd7H2QlF0IS7zj771Ks34hemchobAzc2VqhmKiwT4rYs4YcxJNl_SvfjGjaoI6zRIa2PfVDfst_nbuKXwNf6L678QLd30JSpnviieX8scDRZR8cnr71BIR5ynuGFUM_RV90Mt2sVkWdY6LvXfioLpQTgkN9TpMQZIrz5AGVs6QjmSuAxMzETB3dQU27ojc4keLtBCt24hemmYksrNZmeVRGeBaJoKJpPeYt4yNcnACkcSKO9jaBk1SMw4yXjjqqLgi1340hdqaljKYySQmZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd28bd491.mp4?token=OBnOfBZsWuYD5dxCMPMEgK59kUig9Lp8dzUG7JsJkBIkH1zq85QVRHaSD_fimOq61kqd7H2QlF0IS7zj771Ks34hemchobAzc2VqhmKiwT4rYs4YcxJNl_SvfjGjaoI6zRIa2PfVDfst_nbuKXwNf6L678QLd30JSpnviieX8scDRZR8cnr71BIR5ynuGFUM_RV90Mt2sVkWdY6LvXfioLpQTgkN9TpMQZIrz5AGVs6QjmSuAxMzETB3dQU27ojc4keLtBCt24hemmYksrNZmeVRGeBaJoKJpPeYt4yNcnACkcSKO9jaBk1SMw4yXjjqqLgi1340hdqaljKYySQmZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از وقوع آتش سوزی در یکی از محله‌های نجف
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131419" target="_blank">📅 13:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال ...
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131418" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7644c63d7d.mp4?token=S1zEctqrbYpKym34DMs6KvDZSQOb96WA9sdWx8t1uGqSrHrwkYq6yJ1a0fMZ_gPvPY0rgnsGaYZldpj_nTfd4QKpksj1_3R5HAMKPp-pTM0oWyN9SKbx5nS9anMI_Xk0opX_RcYRP7V5wFlC6j1s_ybeVIBRpQVb8w1GboyS7Yl2__LulFOyKjChEQJRRIkD-FCQyyV_Ws1b747Sj96lu8lbaa-PgD8GVmYloPGBLtrW_ApmhGVildApwlAMCRLim3JkcEhFm6BY8yduT3e_l25HY-LXI2gXxFcinYkVRjSKE93UdF--wtKASyaytlHDXas9zrdcUTBnR4QtljPrrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7644c63d7d.mp4?token=S1zEctqrbYpKym34DMs6KvDZSQOb96WA9sdWx8t1uGqSrHrwkYq6yJ1a0fMZ_gPvPY0rgnsGaYZldpj_nTfd4QKpksj1_3R5HAMKPp-pTM0oWyN9SKbx5nS9anMI_Xk0opX_RcYRP7V5wFlC6j1s_ybeVIBRpQVb8w1GboyS7Yl2__LulFOyKjChEQJRRIkD-FCQyyV_Ws1b747Sj96lu8lbaa-PgD8GVmYloPGBLtrW_ApmhGVildApwlAMCRLim3JkcEhFm6BY8yduT3e_l25HY-LXI2gXxFcinYkVRjSKE93UdF--wtKASyaytlHDXas9zrdcUTBnR4QtljPrrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گذاشتن جایزه ۱۰۰ کیلو طلا برای کشتن ترامپ و نتانیاهو
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131417" target="_blank">📅 13:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
دلار هم اکنون 176,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131416" target="_blank">📅 13:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c41d4e2cd.mp4?token=KZMj15YyejJLXn7fMOeUnP5EWMjhLVOiKlR2IiitUct7qe3KTB3Bfp0h6rX03CxUPQMibjs7-YI-0ncsxbZoOh_Hai130Qs3BFNkblU3W91UQCrRUORmOpYNB-vAXaowlZ1oR8gy50PXZApkdlsfJNit4FZBa25ETCSha-GV7-IVwRM8gGSbLiGjXEZ8st-_GmSlYD6cAWQ9hQQVPiPvPEOimhZZbClaIlZytJSscuJvPLwXUklM-Oc2jAD7m86cFQ3onafy4IfcsNRBIjJEA7yC-FVfT02VzOmF9piN-FGiaGcx-1i-bAOK5dzcZSwGGGrAVpZc-PZBXdildAZ5V1s4JtVFcXz-XwtByqI6l5CWQpG7N_XfYg288hTbiRMP233lz8Q62Cd8aBHWbor0fWc3zm-LgDXaa64iBswePGZT7wY7lZUGRCQZDEvROfzHwKqpve9VGToJ6bZHXQDlN0VIU5iCrH_yfDJSqRteVYvb34mRFlXJSI3ZNSIslaZ0lriZw5bt8JEw6HjnWQ3Uj6H4e-AJKs88PpGmcyP1B7hJ6HiMKIcuPsyz8u0o6SNhveip7G0vXIgu8IWTxyPM6chMsqIRvxVmeuJEiCVqzAC8NL5OceId9jmEqO7dXzAnyG3jhKU7kuvWTgV12hRi286D9xSEkFYeMDaRdYj4shc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c41d4e2cd.mp4?token=KZMj15YyejJLXn7fMOeUnP5EWMjhLVOiKlR2IiitUct7qe3KTB3Bfp0h6rX03CxUPQMibjs7-YI-0ncsxbZoOh_Hai130Qs3BFNkblU3W91UQCrRUORmOpYNB-vAXaowlZ1oR8gy50PXZApkdlsfJNit4FZBa25ETCSha-GV7-IVwRM8gGSbLiGjXEZ8st-_GmSlYD6cAWQ9hQQVPiPvPEOimhZZbClaIlZytJSscuJvPLwXUklM-Oc2jAD7m86cFQ3onafy4IfcsNRBIjJEA7yC-FVfT02VzOmF9piN-FGiaGcx-1i-bAOK5dzcZSwGGGrAVpZc-PZBXdildAZ5V1s4JtVFcXz-XwtByqI6l5CWQpG7N_XfYg288hTbiRMP233lz8Q62Cd8aBHWbor0fWc3zm-LgDXaa64iBswePGZT7wY7lZUGRCQZDEvROfzHwKqpve9VGToJ6bZHXQDlN0VIU5iCrH_yfDJSqRteVYvb34mRFlXJSI3ZNSIslaZ0lriZw5bt8JEw6HjnWQ3Uj6H4e-AJKs88PpGmcyP1B7hJ6HiMKIcuPsyz8u0o6SNhveip7G0vXIgu8IWTxyPM6chMsqIRvxVmeuJEiCVqzAC8NL5OceId9jmEqO7dXzAnyG3jhKU7kuvWTgV12hRi286D9xSEkFYeMDaRdYj4shc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غضنفری نماینده مجلس : یک کودتا علیه رهبر مجتبی خامنه ای در جریان هست
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131415" target="_blank">📅 12:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شاخص کیفی هوای اصفهان با رسیدن به عدد ۵۰۰، در وضعیت «خطرناک» قرار گرفت
🔴
برخی مناطق این کلان‌شهر، در وضعیت «بنفش» و «بسیار ناسالم» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131414" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بلومبرگ:جمهوری اسلامی کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
🔴
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131413" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131412" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiGRzAHiWE6QRsRHRp8G9vimR2b7yOjonx8nY5anUk7oG9w3hNYBQhHxo-s1qRrBbVUW12jyt86br0-fXlPPEQTQ6_j2PItuVCvvwKoa5IxgoGxX0FxlWBlQ3PMFuKH_Z4CQojKqgw5vlCYJBQmc6zoQ0ERA6uGV-jiEnwlcJGPcSaA_4qFKPnKLcJpPhXDcyIidsRnwTzae1VSDe7NsGIacXipnNBfS-p-F6A8fIfnzzpUCMhjYG6XYgO1EFQvXf52JBluVE3je4ByQLFybnDM_OWO-6FqBdMZ5d2Nhz3TnXnTGShRlJ4uCm8dNJUF-ajJnm7s0DfBtOMbYLu_66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دکل ارتباطی در سیریک که آمریکا در جریان اتفاقات هفته پیش سه مرتبه بهش حمله کرده بود، امروز دوباره سرپا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131411" target="_blank">📅 12:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رئیس مجلس ونزوئلا: در پی افزایش شمار قربانیان زلزله که تاکنون دست‌کم دو هزار و ۲۹۵ کشته و ۱۱ هزار و ۲۶۷ زخمی بر جای گذاشته است، هفت روز عزای عمومی اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131410" target="_blank">📅 12:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
الحدث به نقل از منبع آگاه از مذاکرات دوحه: آمریکا به ایران گفته که پیشرفت در پرونده دارایی‌های مسدود شده، منوط به پایبندی کامل تهران به یادداشت تفاهم است و تغییر در وضعیت تنگه هرمز، نقض تفاهمات تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131409" target="_blank">📅 12:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رئیس اتحادیه کشوری کسب‌وکارهای مجازی: امکان صدور مجوز فروش آنلاین مصنوعات طلا در درگاه ملی مجوزها فراهم شده است و متقاضیان طی روزهای اخیر می‌توانند درخواست خود را ثبت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131408" target="_blank">📅 12:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم الانبیا: حضور جنگنده‌های آمریکا بر فراز تنگه هرمز امنیت منطقه را به خطر خواهد انداخت
🔴
استمرار حضور جنگنده‌های آمریکا، اعم از با سرنشین و بدون سرنشین، بر فراز تنگه هرمز، موجبات ناامنی این آبراه گردیده و امنیت منطقه را به خطر خواهد انداخت.
🔴
ایران در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن، دریغ نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131407" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8ff9a7ef.mp4?token=tw4zY5y5ZUdjdnK04w7tpnMQKjUTDOfBq6T1Sth87MyPWbLcfFcCp7wuD4i3SK4Sva9zfvmvY4tjRHlMbFWVxUEEYawYOyWV_5m5i_v7RnFdDPPDCMzHz-LcFyNsPyWZHrfnjfJnAC_ZP1GGfs14jG3EbH_TGxZBgnp8FJVk3-QjHnls7zGEATpzqPbFR9EhU-agKn8FPbmPGnkzPogTjj6_1H0F47cVrS6DYLThl-CTacxSvaIMDm6rMOSq_51rFBLJ2dwsdNg8uU18DzXQ_tc_MOr3pi2KF9QI0OM2mymnOP45Gd1coKlJGprTGpBqQvI7XEfQvZ1Gwy9G2SeoYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8ff9a7ef.mp4?token=tw4zY5y5ZUdjdnK04w7tpnMQKjUTDOfBq6T1Sth87MyPWbLcfFcCp7wuD4i3SK4Sva9zfvmvY4tjRHlMbFWVxUEEYawYOyWV_5m5i_v7RnFdDPPDCMzHz-LcFyNsPyWZHrfnjfJnAC_ZP1GGfs14jG3EbH_TGxZBgnp8FJVk3-QjHnls7zGEATpzqPbFR9EhU-agKn8FPbmPGnkzPogTjj6_1H0F47cVrS6DYLThl-CTacxSvaIMDm6rMOSq_51rFBLJ2dwsdNg8uU18DzXQ_tc_MOr3pi2KF9QI0OM2mymnOP45Gd1coKlJGprTGpBqQvI7XEfQvZ1Gwy9G2SeoYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز F-35 های آمریکایی برفراز ورزشگاه لیوایز کالیفرنیا قبل‌ از شروع بازیشون مقابل بوسنی هرزگوین
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131406" target="_blank">📅 12:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d4fc7f4a.mp4?token=iW5JpdzvV9btOMOQ9wROvw0V1zxdZ4M5KYwq2l50zhuJy4pdbxgmB1ILxP165bRRO-_XBiR8o9SBWloBn1Ipx4tinL-U0jJcWeXrmV5xE3vPTqamgGu8RHEVZ4YGaflHnEnGJscPemjhUWRiAdSdhd0-zDxbUk7XTfD1l-Am0CFlXxczdW-RcycCCw7qj8g7Li-zc6TEK5UdlF2ANmvD1VfjZaAvRNiBSnCq3SwVgqjuXc1tEPYoh-3A6f9J4Aagb-DM6lY6-74VJrl0RMegtvjQNPIvO8vZekUiJOBqQGadoFtj2sJkGokyJu3TQNmscWqMK567sdQClYwT7BFsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d4fc7f4a.mp4?token=iW5JpdzvV9btOMOQ9wROvw0V1zxdZ4M5KYwq2l50zhuJy4pdbxgmB1ILxP165bRRO-_XBiR8o9SBWloBn1Ipx4tinL-U0jJcWeXrmV5xE3vPTqamgGu8RHEVZ4YGaflHnEnGJscPemjhUWRiAdSdhd0-zDxbUk7XTfD1l-Am0CFlXxczdW-RcycCCw7qj8g7Li-zc6TEK5UdlF2ANmvD1VfjZaAvRNiBSnCq3SwVgqjuXc1tEPYoh-3A6f9J4Aagb-DM6lY6-74VJrl0RMegtvjQNPIvO8vZekUiJOBqQGadoFtj2sJkGokyJu3TQNmscWqMK567sdQClYwT7BFsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قائم‌پناه، معاون پزشکیان: اگر قرار باشد نظر رهبری هر آنچه که می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد، دیگر مجلس و شعام معنا ندارد.
🔴
رهبر نظر می‌دهد و نظرش کارشناسی می‌ شود؛ دوباره بر میگردد یا می پذیرند یا نمی پذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131405" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b5f1dc8.mp4?token=A13bc789g6IzEN7QRPIZnPfE22JuaCuJWhFdvp3OdgBJRN6XSw49SYTdDJxpiwwgsyLXNFI09Whm5k4WKhvn_ZKbJAucEj9OkbY6A_YJ2JGw6jBE22vX22bY_8cmptWxfHTO-QcXWakySOi_m9RlZa6QzTJY1WZa3IJZT9pB6N8H9jF6RHql_K6DKduf00MPUNWSVvDGVaA0NdBwtk6H2Z32BfPX8SCSwOTLto4wfvSBKkBZVYBqqKtv7i1Oysrbqrd04Rv2dk3OvtjCtzqDpbUDhY1bSWFrvAS0Dv_ieQfuVAlRB7zp635AbWS8gMejklCG25Ob-m09pxhFcP0y0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b5f1dc8.mp4?token=A13bc789g6IzEN7QRPIZnPfE22JuaCuJWhFdvp3OdgBJRN6XSw49SYTdDJxpiwwgsyLXNFI09Whm5k4WKhvn_ZKbJAucEj9OkbY6A_YJ2JGw6jBE22vX22bY_8cmptWxfHTO-QcXWakySOi_m9RlZa6QzTJY1WZa3IJZT9pB6N8H9jF6RHql_K6DKduf00MPUNWSVvDGVaA0NdBwtk6H2Z32BfPX8SCSwOTLto4wfvSBKkBZVYBqqKtv7i1Oysrbqrd04Rv2dk3OvtjCtzqDpbUDhY1bSWFrvAS0Dv_ieQfuVAlRB7zp635AbWS8gMejklCG25Ob-m09pxhFcP0y0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی جالب در تجمعات شبانه
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131404" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خنده لیونل مسی از بازرسی بدنی او توسط آمریکایی‌ها روی باند فرودگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131403" target="_blank">📅 11:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
الجزیره: حمله روسیه با موشک‌های بالستیک و پهپاد به کی‌یف و دیگر مناطق اوکراین
🔴
۱۳ نفر کشته و ۵۶ تن دیگر زخمی شدند
🔴
مسکو: تأسیسات نظامی و انرژی و فرودگاه‌های نظامی در چندین منطقه را هدف قرار دادیم
🔴
زلنسکی: پوتین مدت‌ها است که خود را برای این حمله گسترده آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131402" target="_blank">📅 11:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143916ad31.mp4?token=lyKUcrIPdqOscxlbVKIKlOlftokXCJKIegBT2eWPJcF7HpC3MZ5LhuGdz12WdgteuusBuA1T4-a_tbxS4uuT9dtlUMO09bLFZBZsmjWyvrhgVn9FlXN90fYdi-K5Kwse6UCGplPP6QrOKElUF2WvQbcvbZY4Roh_SDuVp0bIyK1yo6msMPyqT94qzoNKiaUELtVO6-BwfPUJVQnW9DfSBJnK0J5scdapd4wGDbhiZ9ohhBDYS2WJ6Fw0dU0LMQxOehXEDqLUldeONvlsUOzAwq5GsUAIF3wEj74efYCAiM_XnMofhKekiobU3DlHzOowrVCwoxdMqFSF7VpNiRrwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143916ad31.mp4?token=lyKUcrIPdqOscxlbVKIKlOlftokXCJKIegBT2eWPJcF7HpC3MZ5LhuGdz12WdgteuusBuA1T4-a_tbxS4uuT9dtlUMO09bLFZBZsmjWyvrhgVn9FlXN90fYdi-K5Kwse6UCGplPP6QrOKElUF2WvQbcvbZY4Roh_SDuVp0bIyK1yo6msMPyqT94qzoNKiaUELtVO6-BwfPUJVQnW9DfSBJnK0J5scdapd4wGDbhiZ9ohhBDYS2WJ6Fw0dU0LMQxOehXEDqLUldeONvlsUOzAwq5GsUAIF3wEj74efYCAiM_XnMofhKekiobU3DlHzOowrVCwoxdMqFSF7VpNiRrwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روضه یک مداح نریمانی برای جنوب لبنان: ۱۱هزار خونه صاف شده؛ آقایان چرا نمیزنید زیر میز مذاکره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/131401" target="_blank">📅 11:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-c7PyPd_IZLx_wqIwytSWyac9l-8EP-hMsX-FalBRaN9Ype-pUzy4RttMH5pDjF69JatDB8z0O1hpfbca1zHWIObAb1-zuWijaow58qnlIjOpdb7gTHtCggbMbltUSDm04wEtiYrxs3nDuNcJHrWlizizO_ItLMIs-6099R6GYUTWCefXXFP-xXsbqi-v2HcqGAvJwPckBdTc6ktudi_7kA7QXkwAyqmDu9xhF4CtyJUl28zaMfbjTP6mlIpXHGVht7ScNed2otNMwohDYNKMA77CfLX0_DWCBUrHnG2H9QC1ErFv_yq_adXZENnbfR3iX87UDKBiXlw2XqeBA6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبور تتر از ۱۷۷ هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131400" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_r7IsEl2iHHDBF7ESFa04gUBOZQQ2bUr9pE4sizZ2gw4KwRccLGipHl5lNNPbsjLZc0C9znGByU1Hf2wJD5W-GvwHVY38py-9ElzRbb1V0ucoOedhjJE_je6YfwVGFZwn0DQB24MWvVv5KBc4BMsfw2slkkESSNdsC0KWsKa7BzFdtZ31wpXcXA3nloZxGcKQ5lFFX4VBIHrhF1724o6F0Oys9WEXrQbdwsnbot8Lo_wu4Zq66Fbb0uT4IA2U7zqQyG1ArijGtkG7iM-O350womt_Tg-g4ZjMQLlgrkQDhcb2_R639gWb3ybhLxC6tgVwR0c3C7OSGEExd-ilTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
🔴
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
🔴
طبق اعلام اسلام‌آباد، زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/131399" target="_blank">📅 11:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131398">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQSScnDmzD0U9Bl3O7YyobI9QN9JxlyI5Gko82JgMyGzEPtpgbgDDyckaMIvY6FcjrnO-DvLCOhDwr84DNLbXY_gcNLAjuR-IoLGmketm9LLDbgf5otY0uHPDatEUQ0Akb3Dfd3aMMoleCdSpmnrStmbDX4sNOutSu8_QoRemLmlShBRTPNKRpA1BzVaPaLklaMkiCioPy8zmoMT2NWvwMJofNvX_okLJHgyFXpu60oHBXE2b9dY_zQcJy6f6OFJdFR1ReHFlak-T22jOQMFVb8C5RxxFlfNmwdYqK7jYACwhOnMBTptCe-LTWr6MKsEaeCSbINwKglewB0pEVJzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر عجیب ایسنا درباره مذاکرات دیروز در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131398" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131397">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ایران و مصر رکورددار شد
🔴
طبق اعلام فیفا دیدار ایران و مصر، پربیننده‌ترین مسابقه جام جهانی با ۱۰۷.۴ میلیون بیننده بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131397" target="_blank">📅 11:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131396">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
منبعی بلندپایه به العربیه: توافق شده است که امکان استفاده از بخشی از دارایی‌های مسدودشده ایران فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131396" target="_blank">📅 11:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131395">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / توی تجمعات شبانه، برای کشتن ترامپ و نتانیاهو، صد کیلو جایزه تعیین شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131395" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عراقچی : هر تهدیدی علیه مردم یا رهبری ایران، با یه پاسخ فوری و خیلی قوی روبه‌رو می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/131394" target="_blank">📅 10:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سقوط قیمت نفت برنت به کانال ۷۰ دلار
🔴
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131393" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: مذاکرات آمریکا و ایران پس از تشییع جنازه رهبر سابق ایران ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131392" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131391">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce007c4843.mp4?token=URR9fD-KCCilgeHEhP0yA5V9J41hJSc5M9seCYJ5V5tyOnN4V-6CcJueqz6GcV7t9yhyh9BjFagrT5iL8NUPVkXvQER5Vp5fudpCMXwTmZsNAa50l82QiefR0A56LGQijjgB7PmxYI79ZfV5EMLS8sRxRbtOg2lhvsT8JxSR6q60CpuvOIcqM3Gt6HFtGl0zWwjy2w7a2snfFb9XgwuzLai6rIw9XCV8VHCWfx-BXeddv9_qm6ZypUW2ekO-hjv0YD8g_IYWx-bawhTgR3YvzU20S8AsIu-_t436XA1cqX7ir3rupX_9rHOfREZEBCW5BxQPe-6uT2FTs6Nje4mNqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce007c4843.mp4?token=URR9fD-KCCilgeHEhP0yA5V9J41hJSc5M9seCYJ5V5tyOnN4V-6CcJueqz6GcV7t9yhyh9BjFagrT5iL8NUPVkXvQER5Vp5fudpCMXwTmZsNAa50l82QiefR0A56LGQijjgB7PmxYI79ZfV5EMLS8sRxRbtOg2lhvsT8JxSR6q60CpuvOIcqM3Gt6HFtGl0zWwjy2w7a2snfFb9XgwuzLai6rIw9XCV8VHCWfx-BXeddv9_qm6ZypUW2ekO-hjv0YD8g_IYWx-bawhTgR3YvzU20S8AsIu-_t436XA1cqX7ir3rupX_9rHOfREZEBCW5BxQPe-6uT2FTs6Nje4mNqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه پیشین آمریکا: نباید انتظار داشته باشیم که ایران به شرایط تفاهم‌نامه پایبند باشد، زیرا جمهوری اسلامی هرگز به وعده‌های خود عمل نمی‌کند. آنها فکر می‌کنند اهرم فشاری برای مقابله با ایالات متحده دارند؛ بر عهده ماست که خلاف آن را ثابت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131391" target="_blank">📅 10:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131390">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کی‌یف ایندپندنت: حداقل ۱۱ کشته و ده‌ها زخمی، پس از حمله روسیه  به کیف . روسیه یکی از بزرگ‌ترین حملات ترکیبی موشکی و پهپادی خود را در طول شب به کی‌یف و دیگر شهرهای اوکراین انجام داد.
🔴
این حمله به ساختمان‌های مسکونی، یک هتل در مرکز کی‌یف و زیرساخت‌های غیرنظامی آسیب رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131390" target="_blank">📅 10:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131389">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رئیس سازمان وظیفه عمومی فراجا: مشمولان دارای سه فرزند و بیشتر تا پایان سال ۱۴۰۷ فرصت دارند از معافیت سربازی بهره‌مند شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131389" target="_blank">📅 09:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131388">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آمریکا: در پی فرود اضطراری یک فروند بالگرد «ام اچ-۶۰ اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه تن دیگر زخمی شدند
🔴
تحقیقات درباره چگونگی وقوع این اتفاق ادامه دارد
🔴
هیچ دلیلی در دست نیست که نشان دهد این حادثه، ناشی از اقدام خصمانه بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131388" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
واژگونی قایق گردشگری در پاکستان با ۷ کشته و یک مفقودی
🔴
پلیس پاکستان اعلام کرد که روز گذشته (چهارشنبه)، پس از واژگونی یک قایق گردشگری در ایالت «خیبر پختونخوا» در این کشور، هفت نفر جان باختند و یک نفر دیگر نیز مفقود شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131387" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔴
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131386" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
انتقام روسیه از حملات کی‌یف
🔴
روسیا الیوم با اشاره به حملات روسیه به اوکراین اعلام کرد: حملات شبانه روسیه به کی‌یف یکی از شدیدترین عملیات‌های اخیر مسکو بوده و در واکنش به حملات کی‌یف علیه زیرساخت‌های غیرنظامی روسیه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131385" target="_blank">📅 09:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
🔴
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131384" target="_blank">📅 09:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeVTa6l2K-TQxLZtxVZIf33FV-lQEpeY1wmaIt9fUsTIWQnmz2sI4vUJIvIcGjPr-_8gL3uKJ3iqsL6gIjUdM-tPVGj_nlJ7L2fxBrH7ZcZZ3VSg7mFaZNWh7bFd8pHrsFqAHD92TJrc7muTvGRawDHHfQ3RVk4NBlg5k4z3RVu9jqD2JiGWxvKjSuCMzEzATlY-QEsVU4DwlJIR_UFJUSahuJ_tZfSwwWBNJngUfvU4wypB6gVavXVDWhBePVUAW7JfYfPmSeSeaHeEmq1Ezk7xD8Yc6ExJ_IFmNCrFLNzQtB9poLhBMWOtAByTIcGp2GYZ6IIdIiMXXCxVgp2GcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی خطاب به قالیباف: هوچی‌گری هم حدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131383" target="_blank">📅 09:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131382">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: ایران از زمان لغو محاصره دریایی توسط آمریکا در ۲ هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است.
🔴
‌تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131382" target="_blank">📅 09:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197e89311.mp4?token=Cnw15RSRjUP8AIAX7sGlTmOKq-Elv59sPa0KG_Tj2PfnTE-TBDQ8L8miku2WxlRNyd_DRXK1SKAydIYJTqfyVhi4Wawk9qPVL9CDEjX1SsboY9Pj416zmH07_JrbYW9F87CpeXxdhVOoLxyfjAKJmZihnFPspNfYIYvPeH0Ppcsdvuk-LT5Ai2eb8oqCkqPwAuRg0hBa2fPTOIh7oN6zeBQ0Wg0nubQwMI6mHNfxmpsKyB-jZD1jURbMnM89d9OoxczN0LhXpy0TAPVJ0k2d6q134-qWWuwBeTZlE5FuxpA1dUm-Dy2YdaemlGON75ZPrtT0nfjBiiZ1v1sG0X77Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197e89311.mp4?token=Cnw15RSRjUP8AIAX7sGlTmOKq-Elv59sPa0KG_Tj2PfnTE-TBDQ8L8miku2WxlRNyd_DRXK1SKAydIYJTqfyVhi4Wawk9qPVL9CDEjX1SsboY9Pj416zmH07_JrbYW9F87CpeXxdhVOoLxyfjAKJmZihnFPspNfYIYvPeH0Ppcsdvuk-LT5Ai2eb8oqCkqPwAuRg0hBa2fPTOIh7oN6zeBQ0Wg0nubQwMI6mHNfxmpsKyB-jZD1jURbMnM89d9OoxczN0LhXpy0TAPVJ0k2d6q134-qWWuwBeTZlE5FuxpA1dUm-Dy2YdaemlGON75ZPrtT0nfjBiiZ1v1sG0X77Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراینی‌ها پیش از حمله گسترده موشکی و پهپادی ترکیبی روسیه، در متروی زیرزمینی کی‌یف پناه گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131380" target="_blank">📅 08:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رسانه‌های محلی فلسطین گزارش دادند : قایق‌های جنگی اسرائیل به سوی سواحل «خان‌یونس» در جنوب نوار غزه تیراندازی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131379" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131378">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از دستیاران نخست‌وزیر عراق مدعی شد: ایالات متحده انتقال دلار به عراق را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131378" target="_blank">📅 08:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131377">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سازمان امنیت دولتی یمن در سازمان ملل: حوثی‌ها با حمایت ایران بیش از ۱۸۰ حمله به کشتی‌ها انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131377" target="_blank">📅 08:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131376">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lObHzGpiZY8s-Do_SUFGeU1EgjHPIsrobJrqrYxUvizIoKIyZlkXfDWsoXvhyhmacW6BFxaApbsuKsM7z-HFL0iOKoVf9LGF5JowJ4KIJDATQTUPbzFWX5KrxOj-_0xExavg4YUd3GLagjaNyT1-nskwAkDPPD716J2kZHBWJIhiIboNQlARX0n0Iw1bPeSoBFo9vCOrZq6O9nbvJut2l3JWA_QL5BHDq0K19gIKmOGBTdA5n2_NBFYl2GEbwDVTVbNIz4Zv0SL02chlpclQ6CaJIubAVjabSlFt3jg8awidMdKEPLXveutPkJ57w912C4ylVoMkVLvY5bpKUQv01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: تنگه هرمز زیر فرمان ایران تعریف می‌شود نه سنتکام
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131376" target="_blank">📅 08:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131375">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الجزیره: ایران پس از مذاکرات دوحه، کانال ارتباطی برای نظارت بر تفاهم‌نامه با آمریکا ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131375" target="_blank">📅 08:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131374">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یک منبع ارشد به العربیه: به ایران اجازه داده خواهد شد تا محصولات کشاورزی آمریکایی را با بخشی از پول‌های مسدود شده‌اش خریداری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131374" target="_blank">📅 08:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131373">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بخشایش اردستانی،نماینده مجلس: تجمعات شبانه باید فورا جمع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131373" target="_blank">📅 02:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131372">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_ZbgHv2lHsMpyX3vlm5JpROd0m9EVg7Gs1weVg6Ion3yv25rhU75HVE8PCZeafK2rGN9PbzJHoB2OyWrcXS_9z6tgUn6v4myI1Hja7eQfAxr4tL3ucIimW7RdkfcDEG50ME9Oop2ljnhj4E-Vjk3NdxsHEuYu7PhrCR6eF5AQiwJ0xzSLpKSt6GYnd9Uiv4JYJYJ6WjZ0MUaTZAhMJ0IA-eZD64W9J4LstRy14VTiYb96Pev-WyoXBXjAMtY25q_7hKtKucs0CKODBXfLmahXZoYNES1APDQfhHhKjOBxciuclpLcPOVd5_lzh4HSmLRgAutIbOVEeGE2A4tRF9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش ایالات متحده آمریکا اعلام کرد که در پی فرود اضطراری یک فروند بالگرد از نوع «ام اچ-60 اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه نظامی دیگر خدمه این بالگرد نیز زخمی شده اند که وضعیت جسمانی آن ها پایدار گزارش شده است.
خبرگزاری «رویترز» به نقل از ارتش آمریکا همچنین تاکید کرد که هیچ دلیلی در دست نیست که نشان دهد این حادثه ناشی از اقدام خصمانه بوده است.
در بیانیه ناوگان پنجم نیروی دریایی آمریکا آمده است: «شناورهای نیروی دریایی هم اکنون در حال انجام عملیات جست وجو در منطقه برای یافتن یکی دیگر از اعضای خدمه پروازی هستند که همچنان مفقود است. همچنین تحقیقات درباره چگونگی وقوع این حادثه ادامه دارد.»
در این بیانیه همچنین آمده است که این بالگرد در منطقه بر روی ناو هواپیمابر «یواس اس جورج اچ. دبلیو. بوش» مستقر و به مأموریت اعزام شده بود.
فرود اضطراری بالگردها روی آب می تواند حتی برای خلبانان با تجربه نیز بسیار خطرناک باشد؛ زیرا بالگردهایی که بخش فوقانی آن ها سنگین تر است، هنگام برخورد با آب معمولاً به واژگون شدن متمایل می شوند و ممکن است به حالت وارونه در آب قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/131372" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131371">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
حادثه امنیتی در ناو هواپیمابر جورج اچ دبلیو بوش در نزدیکی ایران و دریای عرب.
🔴
نیروهای نیروی دریایی آمریکا در جستجوی یک عضو خدمه مفقود شده از هلیکوپتری هستند که از ناو هواپیمابر جورج بوش برخاسته و در دریای عرب به صورت اضطراری فرود آمده است.
🔴
سه نفر از چهار عضو خدمه هلیکوپتر با موفقیت نجات یافته‌اند و در عرشه ناو هواپیمابر در حال بهبودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131371" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131370">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzSsbHmXGVBdL-OuwLdzyCiWCLGXVKnVjUWNGg_pflJktJMXS88y1YEU93ShR_nSdVS_GRBOcGn5sY8YvPky5gZy34VTtqvtJiscr55TQJpHBuY1cQvTO9nVRzCttuYyeLbzyumJlBFI0LfUCWiNMmhwOcHiVX1OifAZWdUwCMdXi8s-jbpWoyKBq95kjXG44zBnMHB80lPNRcSXHX3pXd0JSyuykiyUujmdhfDdP-YvvExQ2kflver3JaLgiFa7fN8oxwLDsW-3UNDnv2_DApA7JrU6OKQbeivVYA-GwCDTEtZZjUdlKB-OrsSIO9Lk9Kz6Pcc8LeGhBCwZRGv63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: برای مراسم‌ تشییع، همه مردم بیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/131370" target="_blank">📅 02:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131369">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">کشور ایران از بیخ فاسده
میترسن یکیو برکنار کنن اونیکیارو لو بده
پس نتیجه میگیرن داخل ی سفره بشینن و بدزدنو بخورن
فوتبال هم اینطور شده</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/131369" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131368">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر ورزش عربستان سعودی پس از حذف تیم ملی این کشور از جام جهانی، رئیس فدراسیون و چند مدیر ورزشی این کشور را عزل کرد، همچنین سرمربی تیم هم اخراج شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131368" target="_blank">📅 01:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131367">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/131367" target="_blank">📅 01:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131366">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNa8KJLqqdhX8e9YthOr4hSBlvckbrdOJTMcXn6r5Ax5DZeDAIX2BdrmV0S4vyop8-9-Bwjm6ujBl4MMUepNLyLNOKkJag_M_SKlaIpy-DFMYek4Gm9Ihtt9DINhpeP2bZti9zlctB2FCuts6w0kPcKyoBzJ6Q79c8IMnG-kWLqhgqHwFpOQPK8SHIuqvqIHkRK4EtsXAAXuyCvIHpuvEYxJ6t7N8LxQExskoSbtnJAQcGhf4ZZbR61FaH7euGEHJot-QfSYN8Due6LoVItebehrg8kVQas8H9szuvjYPATbYtxLrfmqGXnVx5czCJNaFgGBIsyjPXNjbqC0SFSv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به تاج و اعضای فدراسیون که رفتن به جام جهانی مجموعا بیش از 50میلیارد تومان حق ماموریت داده شده
🔴
فک کن بری جام جهانی و بهترین هتل مفت بخوری و تیمت هم برینه و ۵۰میلیارد هم بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131366" target="_blank">📅 01:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131365">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/131365" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131364">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcSFXAPE8UT77n0AtXhsk-13zFsblEDWRAYRDnZSMYUbpA95Z_VAnJT6aIbQY0yKTr4WhpuVqRq5NC3jnD1KYc515mm-skD6MIeJnNNBUOAlFdsLl315A3Fqg1ZSNg5Mrhh-mmcPJqWq4CjdCjSPQOLouUP3HM0LJbFOpXBbry95sIc4OsaXQCxx00HV6CW50XvezY3D0nEsaaSXfyQEHwMimAiDksviBLavddhw8fzTrAC8UKhYnLGJLne4MNqYu2jlmDWGSDYuzyhv9ZE1gkvhR7JJQLCLyN0Cm0VXAA8_u4EoQuGs0VqU-g4x2eYd3y-RizYlXqQDPKTQmF2n4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/131364" target="_blank">📅 01:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131363">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🎙
فردوسی پور:
نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن!
@AloSport</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/131363" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131362">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3740efe365.mp4?token=XGIj8f6KZHi-2iZMD8KEdUUZF29Tu5nf-mfFme1CSicbW1-_2KD9jDY2KeLiQpappgKMJFl79vGzpva_0SeUE_nPEIx92TizdAUPLyCL_xJo5Hxzt9QVpQ43ZLA4LFsnvzbsNIueIXlDvE7Buroh9152tjNii5LDr5tOD32DfiaPuSUJRMpWJfg9ZqiTWpOMEW-Cs6Eui3U8AWgjM7GTgic1c4Ym566O58lKKJrN8M4rswDMwtM8pmH-fAviYHsNElHcdqKmMoKnEB8zUv21c7mnqPW6TQ1dsvnXGx6ICKlMCaOlQpy0iJm1vnuFkn5EYnwqD0fXPbMHVNw-crAypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3740efe365.mp4?token=XGIj8f6KZHi-2iZMD8KEdUUZF29Tu5nf-mfFme1CSicbW1-_2KD9jDY2KeLiQpappgKMJFl79vGzpva_0SeUE_nPEIx92TizdAUPLyCL_xJo5Hxzt9QVpQ43ZLA4LFsnvzbsNIueIXlDvE7Buroh9152tjNii5LDr5tOD32DfiaPuSUJRMpWJfg9ZqiTWpOMEW-Cs6Eui3U8AWgjM7GTgic1c4Ym566O58lKKJrN8M4rswDMwtM8pmH-fAviYHsNElHcdqKmMoKnEB8zUv21c7mnqPW6TQ1dsvnXGx6ICKlMCaOlQpy0iJm1vnuFkn5EYnwqD0fXPbMHVNw-crAypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صداوسیما جوری داره از قلعه‌نویی تعریف میکنه که خود قلعه‌ هم تعجب کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/131362" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131361">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=B6TBRZqNNHPimOASl5XAAhcR4GKYedap5rb4wEDUEnyoKl_KXYOUO5fdmO7UIrQnzn7Sbxsu9p8hkQ7p_ScFPDjPhOnKgWP6LDdAD7A5G_4wXldN8JoR9ntfLtemoTlf9bgvo0sseYNgI3-f899P-RcimrbpRx3U2utWVWpLJldAX-rB4eBNvfMzXC3RhK1EalC7eCHgh_LG2JXYi2g5Xra41hvnnrrs54OdLD3rJLwHeOfROGn5H4SfXku1o83KAyzpFEl1s6bFNkAbG0DCiHl-NiLZ5sxRjDrXjYLR_uPhybdvrHxUBfq32kZNLgY5tpHyeNeIUqFzsyDBuUeUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=B6TBRZqNNHPimOASl5XAAhcR4GKYedap5rb4wEDUEnyoKl_KXYOUO5fdmO7UIrQnzn7Sbxsu9p8hkQ7p_ScFPDjPhOnKgWP6LDdAD7A5G_4wXldN8JoR9ntfLtemoTlf9bgvo0sseYNgI3-f899P-RcimrbpRx3U2utWVWpLJldAX-rB4eBNvfMzXC3RhK1EalC7eCHgh_LG2JXYi2g5Xra41hvnnrrs54OdLD3rJLwHeOfROGn5H4SfXku1o83KAyzpFEl1s6bFNkAbG0DCiHl-NiLZ5sxRjDrXjYLR_uPhybdvrHxUBfq32kZNLgY5tpHyeNeIUqFzsyDBuUeUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
@AloSport</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/131361" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131360">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v91o6J1JCug_4NqJmmllwK3rOFDem4F1uMoh_t-ajIrJw_mpNCKb2_WBzIBiu7kdW1lQPWXnvIDy8mkS48G2NHP0y5ko5Br9cwP957-5BNQtz-q4WtWdb1_Tz6s8-EQf9rO1HTbNCfBqfFqz31ADqawtFhckbIULjDVcYThh641zET02yi7vRVsPB9VCpIDtcdiXK3ORTGRO1T0OLbpGXgujSlbC4hjUmiiw7BE-QLZ2CIwJlhnel5QqAfUPHQ7iBILrGmxOqaWHDbpJBZQsN7MZcdMQ7uqwPBJfNTHpVacODyi996BbAh0J3F4KcKULAMJ8TlM_zzb52nH7sUgQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع رسانه‌ای گزارش دادند: مقر احزاب تجزیه‌طلب در منطقة «ديكلة» واقع در شمال عراق هدف دو حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/131360" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی به سمت اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/131359" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131358">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ:  در مورد کوبا، پس از دهه‌ها و دهه‌ها، به سمت ما می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131358" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131357">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386c345efc.mp4?token=cT95tthDFhXP6ibOcu9xj0FGDoVyAnxBiydgnytc9mJ8QpeHBTHLTQmijx0cdJS-0C2_G3J4sKUyD63kkhteBAPYAZVwl0IK6Bpi3nnO6b0m3oP3YiVlxg3Ux1EeuBnPzkCiuoKsYMCR5maAF-69gYlTtIbnCNuJkBFr1P5_uikPWHcJIcrMLyOJaXL363AJTyT4z2x2d2nNS1rRD1AvQSvk6R5_vn22sbIrJ5ALpwwoNFMaWdFvwEhfJceVGHtzUmKPu0of9xaUi1HWqQh-JspB5NBETInecI59VRLTbVBvS8nFZcXm7ArEaxTBt0a7wHFOfGhEW90t9bVc9QcNIwepD57o1Rn_m0LhMFV5opBa6Sa6LIjgy6bUHXsN9sD4NDXUbzW51QecuNyojUQ7haaiXchu2zgQsbaXKF423qO4dp8xp3q-Rtc0607i3j0qcjAWSQ8TzHdVzWmRFdDZuoJjDfSzw3wdM0KVK-eRuA6hoaWSbBNQ5RmQ0JdZoZRBqrXUptxRRf0y5ciNQ3YC0GAettNzr0PSOG0vLvT05LL8SdrkOjxBom-g8uw33xnP1jMx7FsZ-MWRrBNy3F-rzQgd-EVVgU9Cegbw0SPW6i1GGJ-N4D085PxwMokQfaqElOYL3swXGxgLC29Ar1faRKceJzJicxjFJgFaYlP729Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386c345efc.mp4?token=cT95tthDFhXP6ibOcu9xj0FGDoVyAnxBiydgnytc9mJ8QpeHBTHLTQmijx0cdJS-0C2_G3J4sKUyD63kkhteBAPYAZVwl0IK6Bpi3nnO6b0m3oP3YiVlxg3Ux1EeuBnPzkCiuoKsYMCR5maAF-69gYlTtIbnCNuJkBFr1P5_uikPWHcJIcrMLyOJaXL363AJTyT4z2x2d2nNS1rRD1AvQSvk6R5_vn22sbIrJ5ALpwwoNFMaWdFvwEhfJceVGHtzUmKPu0of9xaUi1HWqQh-JspB5NBETInecI59VRLTbVBvS8nFZcXm7ArEaxTBt0a7wHFOfGhEW90t9bVc9QcNIwepD57o1Rn_m0LhMFV5opBa6Sa6LIjgy6bUHXsN9sD4NDXUbzW51QecuNyojUQ7haaiXchu2zgQsbaXKF423qO4dp8xp3q-Rtc0607i3j0qcjAWSQ8TzHdVzWmRFdDZuoJjDfSzw3wdM0KVK-eRuA6hoaWSbBNQ5RmQ0JdZoZRBqrXUptxRRf0y5ciNQ3YC0GAettNzr0PSOG0vLvT05LL8SdrkOjxBom-g8uw33xnP1jMx7FsZ-MWRrBNy3F-rzQgd-EVVgU9Cegbw0SPW6i1GGJ-N4D085PxwMokQfaqElOYL3swXGxgLC29Ar1faRKceJzJicxjFJgFaYlP729Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مدال افتخار
:
من پسران زیبایم را می‌بینم. فکر می‌کنم می‌خواهم یکی را به خودم و یکی را به آن‌ها بدهم و یک سه‌نفره خواهیم داشت.
🔴
من به آن‌ها مدال افتخار کنگره را برای چیزی می‌دهم... برای نبوغ آن‌ها در شکار.
🔴
و من یکی را برای پذیرش «روسیه روسیه روسیه» یا چیزی شبیه به آن دریافت خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/131357" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131356">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها با تعداد بی‌سابقه‌ای که تا به حال کسی ندیده است از تنگه هرمز خارج می‌شوند، ما در حال ثبت آمارهای بی‌سابقه هستیم و قیمت نفت در حال کاهش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131356" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131355">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=C6JcNOWusHCN1UqpkkvVgw9OM4BFkw8zDs99ZkHzUiItxEYnq2ZY0O9rHiz7c9vPL7qnX3FDi0HUy7o7bM9yQh1Zs_2pp9YrIoR4HWLWFw2TyipknycGK9jwG9UmZ_61HTupqCBZ1vpAXV1GbyM7a7s5AkVzWOTjztNSv28dm8HXYo4_NBO3ygSi7BEdiTvFYMQvrLlsywaEYgkrkWyFRLJn8fbZOXElzLnzLGtljNaugy3jOCjuSilyR1CmCk_WZvDo7CIwI3xHjPiwhb3kJzI6K7q7eB77-HzscTzCtgaDD3aLkTy3_WwO1nlwouiHomiujTTY-tkqJ9tRUljw3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=C6JcNOWusHCN1UqpkkvVgw9OM4BFkw8zDs99ZkHzUiItxEYnq2ZY0O9rHiz7c9vPL7qnX3FDi0HUy7o7bM9yQh1Zs_2pp9YrIoR4HWLWFw2TyipknycGK9jwG9UmZ_61HTupqCBZ1vpAXV1GbyM7a7s5AkVzWOTjztNSv28dm8HXYo4_NBO3ygSi7BEdiTvFYMQvrLlsywaEYgkrkWyFRLJn8fbZOXElzLnzLGtljNaugy3jOCjuSilyR1CmCk_WZvDo7CIwI3xHjPiwhb3kJzI6K7q7eB77-HzscTzCtgaDD3aLkTy3_WwO1nlwouiHomiujTTY-tkqJ9tRUljw3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : کنترل کامل. ما کنترل کامل همه چیز را داریم.
🔴
این فقط آغاز دوران طلایی آمریکا است.
🔴
بهترین‌ها هنوز در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/131355" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131354">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=nlViZtUqYIzSbiwANi32cTUZ2Pm0uT7V3IfB1Y5yCqr5xoQMP_Zy_wJ_t907iT9SOsq-_oQIGvCSCVMEhZ6p1WG-G8jufoSfR4o_wszK1F7eCCcR6b0ASOX7C2JrsWOfnZAIwJfBvGkZkHdsyKt26WEJ6CBdukHRMYxaLOoDx-BqNC4aae1lN2JiE-BL1FJtVtKf12GOhb02vApxEAw40fXj24d4J_tByTUryZeRgxyK_c-amAq-m1rmxObNv970KW18BsJRKPXhU8ye4EVzbU-FSKxMSrRiBwYYRQm4TlT74D7z_-bY05uqpuZQr9Us7BfiPHvGFwLLD6bwM2jyFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=nlViZtUqYIzSbiwANi32cTUZ2Pm0uT7V3IfB1Y5yCqr5xoQMP_Zy_wJ_t907iT9SOsq-_oQIGvCSCVMEhZ6p1WG-G8jufoSfR4o_wszK1F7eCCcR6b0ASOX7C2JrsWOfnZAIwJfBvGkZkHdsyKt26WEJ6CBdukHRMYxaLOoDx-BqNC4aae1lN2JiE-BL1FJtVtKf12GOhb02vApxEAw40fXj24d4J_tByTUryZeRgxyK_c-amAq-m1rmxObNv970KW18BsJRKPXhU8ye4EVzbU-FSKxMSrRiBwYYRQm4TlT74D7z_-bY05uqpuZQr9Us7BfiPHvGFwLLD6bwM2jyFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما بزرگ‌ترین زیردریایی‌های جهان را می‌سازیم.
🔴
ما در زمینه زیردریایی‌ها و دیگر موارد ۱۵ سال جلوتر هستیم
🔴
ما دوباره با کشتی‌ها شروع خواهیم کرد. قبلاً روزی یک کشتی می‌ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/131354" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131353">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
اکسیوس: آمریکا تلاش دارد ایران را از دریافت عوارض از تنگه هرمز منصرف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/131353" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131352">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=DRYq-S8xqGeLROFj3QO4h7BO4wYHAHbumtJ2nryld_v9PhhAZ2hiLJNZTvKE3vZqo6Jv5WXwyQzqZiigf_sNarKlUkMVEv7_yY2Ndx1S8_D-S3q34EJp0J98IAAqMUT46GQ8aJuxy7dKXPluoXkEBslJn-mVDWChPUROMg-P6eiHKr3RyfIJY_JpehxIGFiC4TjestMInxJUfLCKLhol7tLnWI4r178WC7M3L_y2GdEnK5tnYWb_kWFGMBpWl37K7Rx3NeMS4kgW-tx-GMxcOu3G2_6pO90XEZgN3TxJDZHdAEJNV6xFWVrey1Fnk1NYc_2mXNQWdGlvO8ZutQBpgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=DRYq-S8xqGeLROFj3QO4h7BO4wYHAHbumtJ2nryld_v9PhhAZ2hiLJNZTvKE3vZqo6Jv5WXwyQzqZiigf_sNarKlUkMVEv7_yY2Ndx1S8_D-S3q34EJp0J98IAAqMUT46GQ8aJuxy7dKXPluoXkEBslJn-mVDWChPUROMg-P6eiHKr3RyfIJY_JpehxIGFiC4TjestMInxJUfLCKLhol7tLnWI4r178WC7M3L_y2GdEnK5tnYWb_kWFGMBpWl37K7Rx3NeMS4kgW-tx-GMxcOu3G2_6pO90XEZgN3TxJDZHdAEJNV6xFWVrey1Fnk1NYc_2mXNQWdGlvO8ZutQBpgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اسپانیایی‌ها — اعضای ناتو اما نه اعضای خیلی خوبی از ناتو.
🔴
آن‌ها به خوبی رفتار نمی‌کنند، اما یاد خواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/131352" target="_blank">📅 23:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131351">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
جی دی ونس: در حال حاضر، مذاکرات به خوبی پیش می‌رود
🔴
کسانی که به دولت به‌خاطر مذاکره حمله می‌کنند، همان افرادی هستند که ما را تشویق می‌کردند چند بمب دیگر هم روی جاهایی مثل افغانستان بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131351" target="_blank">📅 23:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131350">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ
:
عربستان سعودی و دیگران در حال نگاه کردن به چین و سایر کشورها برای محافظت از آن‌ها در طول دوره مدیریت بایدن بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/131350" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131349">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=dGV1H40oeykvzx90YgOihdX625lsiTA11IKOBKKyJHZM3ZH-hDxBipsJ_-COEBhlX6EZ9TYFIkE3Vw34O7Jdgc6aVUwzirVH8m3Y11iadUYd_cx1uZNcjTIfsuvePXdZcnR_eNCTL1fGElmPUlxIyH8P3ddOeSL87rxgmBKTweyB5RTg83wEvSokFA4fUJxeVQSodIFhNjIevEGRc4xTZNejH0HURJQV5MeBL3swPKIAMojty4skvGj7oAUHSQvbvSTdX50L5aSZzDKDzWUoa40HYplahq6zbjE815hb-fpE_BkwKJtTnWztlgCEl8GHwVCP-tUcIH36Sj21nUvf_Su1UCwWSDih0cEZXSXx7sUzr3lMUsoenS29sY6QYMSyJ5OIFQqc84x_xUmXN0s4JavjtAPKKrnsJfUqzQfQBOufVVHSSlcjj6RMIat_iji7XfmCA_fvRFF2pPawbWUD9dbTWO1pUbCctbtNLhJYA4-jv9z2xaOCQ3TxgvibLfLat45CYyP7gBsuoUrYYUGFWtvUs71VhdTBCqibCjNt-YbEEh4D4I-zCJuGbp39v3a7qQn-c1ravFnWkA8WXLvZW9q-wki2I_BJPiyCPntg86E_CYx1Y6ULq7kEyDV4vGSGiX8dTmi6PyAyvNcs6s5gTtn6yP4Rm-X2MiYA3sbYjOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=dGV1H40oeykvzx90YgOihdX625lsiTA11IKOBKKyJHZM3ZH-hDxBipsJ_-COEBhlX6EZ9TYFIkE3Vw34O7Jdgc6aVUwzirVH8m3Y11iadUYd_cx1uZNcjTIfsuvePXdZcnR_eNCTL1fGElmPUlxIyH8P3ddOeSL87rxgmBKTweyB5RTg83wEvSokFA4fUJxeVQSodIFhNjIevEGRc4xTZNejH0HURJQV5MeBL3swPKIAMojty4skvGj7oAUHSQvbvSTdX50L5aSZzDKDzWUoa40HYplahq6zbjE815hb-fpE_BkwKJtTnWztlgCEl8GHwVCP-tUcIH36Sj21nUvf_Su1UCwWSDih0cEZXSXx7sUzr3lMUsoenS29sY6QYMSyJ5OIFQqc84x_xUmXN0s4JavjtAPKKrnsJfUqzQfQBOufVVHSSlcjj6RMIat_iji7XfmCA_fvRFF2pPawbWUD9dbTWO1pUbCctbtNLhJYA4-jv9z2xaOCQ3TxgvibLfLat45CYyP7gBsuoUrYYUGFWtvUs71VhdTBCqibCjNt-YbEEh4D4I-zCJuGbp39v3a7qQn-c1ravFnWkA8WXLvZW9q-wki2I_BJPiyCPntg86E_CYx1Y6ULq7kEyDV4vGSGiX8dTmi6PyAyvNcs6s5gTtn6yP4Rm-X2MiYA3sbYjOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما اجازه نمی‌دهیم کمونیست‌ها راهمان را ببندند.
🔴
آن مردم، کاری که انجام می‌دهند، واقعاً احمقانه است. آن‌ها واقعاً احمق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131349" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131348">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=EX9bl2eBRnfYIDny4bgOUScnet6CQJc6U8-ltxffIGhTOUemXVWnvR44U0tIi08vByHUWUgB8qHOh9kELDcq2qVYjV9ThTxRaRZ6-MyG0IAEeiBmlTo897R3ulR-EGo6h8N7bFNbnRlAJ5dqmiocQKZQIsKrEKbzpMr9fFErLskCUe7IxbjBh9x5843snZXaLl5mlDulPjnlxWUz95XTorCPsitr7tKzfyXi0L3UIELNzmkf44wGuaDbuSLOyCOZ5BdQ3GmakRB76nujRHjRqBAgH9Yr7mEyktmLIDsMnhn_y_RzHvrrY_SOE8o81Jz15mHUTbo8f0oWZxV1nsRQrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=EX9bl2eBRnfYIDny4bgOUScnet6CQJc6U8-ltxffIGhTOUemXVWnvR44U0tIi08vByHUWUgB8qHOh9kELDcq2qVYjV9ThTxRaRZ6-MyG0IAEeiBmlTo897R3ulR-EGo6h8N7bFNbnRlAJ5dqmiocQKZQIsKrEKbzpMr9fFErLskCUe7IxbjBh9x5843snZXaLl5mlDulPjnlxWUz95XTorCPsitr7tKzfyXi0L3UIELNzmkf44wGuaDbuSLOyCOZ5BdQ3GmakRB76nujRHjRqBAgH9Yr7mEyktmLIDsMnhn_y_RzHvrrY_SOE8o81Jz15mHUTbo8f0oWZxV1nsRQrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
در 4 جولای، دمای هوا تقریباً 107 درجه خواهد بود.
🔴
و من می روم، و یک سخنرانی واقعا طولانی دارم فقط برای اینکه نشان دهم که می توانم هر کاری انجام دهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/131348" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131347">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=qEid1CRqwoAXPNoNn_N66bgGjIxuKd85ybwZGMpIUF89fz88fZUVaC_3-1V30Br55LHGo_nleVROyJGJHUk_ejWKZHCBFsffMGe3QyqQfWwrSPejmbsZTVOLzVXWgfnpGyA4_lCVxRrvAu6JTVM734R-JDpFEsEpmZIQAZkouHpwbJyHsvUSRpRGHHeMKvuUINKpGRonK7q7sQ2ym8JMcaGV62dRjuZ-vWFXEfMpj-zxuzn7OMPHWlwK-jO_BVF8GdgfAl7-PHhN7lEKT24THKoYnr5-LiNs-kt-Hx0A1W8hh1lNEB9OR0PdhTD6-MweOMI-1UqXFP9_j0C0s-NdmiKyh086oy7UwP87Pla8CVfsY_ENrqUoJ-bFOu239wde1tJaUTE8W9kFXUgigNArmdksrbgW1wlERm2zlm7NFvUP7enD0VGAznVf0Vn1-21TCgBOFMLnqs--COyPMOUaGfPPYtEmJPW7NEgYnY7PgFSkSwERJ51DzlGykSohlx9KMKWyHp2bLRm6hCLP4tSr0Id6ddL5Hn0cEcCjbJznM8QPk-Wto9hE_5uqWe77gdzf3kPbRacLlUv4U2pojIhoUzyFb9CpfUQnVqgul8ut8qAC0f8KuZVZbl-7D0qIGkTLxeXU026XEd9i0U3BtAKB874Z4ih9RZH1POHpd8GP5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=qEid1CRqwoAXPNoNn_N66bgGjIxuKd85ybwZGMpIUF89fz88fZUVaC_3-1V30Br55LHGo_nleVROyJGJHUk_ejWKZHCBFsffMGe3QyqQfWwrSPejmbsZTVOLzVXWgfnpGyA4_lCVxRrvAu6JTVM734R-JDpFEsEpmZIQAZkouHpwbJyHsvUSRpRGHHeMKvuUINKpGRonK7q7sQ2ym8JMcaGV62dRjuZ-vWFXEfMpj-zxuzn7OMPHWlwK-jO_BVF8GdgfAl7-PHhN7lEKT24THKoYnr5-LiNs-kt-Hx0A1W8hh1lNEB9OR0PdhTD6-MweOMI-1UqXFP9_j0C0s-NdmiKyh086oy7UwP87Pla8CVfsY_ENrqUoJ-bFOu239wde1tJaUTE8W9kFXUgigNArmdksrbgW1wlERm2zlm7NFvUP7enD0VGAznVf0Vn1-21TCgBOFMLnqs--COyPMOUaGfPPYtEmJPW7NEgYnY7PgFSkSwERJ51DzlGykSohlx9KMKWyHp2bLRm6hCLP4tSr0Id6ddL5Hn0cEcCjbJznM8QPk-Wto9hE_5uqWe77gdzf3kPbRacLlUv4U2pojIhoUzyFb9CpfUQnVqgul8ut8qAC0f8KuZVZbl-7D0qIGkTLxeXU026XEd9i0U3BtAKB874Z4ih9RZH1POHpd8GP5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
🔴
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/131347" target="_blank">📅 23:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131346">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: اخبار جعلی اخیراً نسبت به من بسیار مهربان بوده‌اند.
🔴
وقتی شما همان کاری را انجام می‌دهید که ما انجام می‌دهیم، آن‌ها باید مهربان باشند، حدس می‌زنم.
🔴
من حتی با تئودور روزولت صحبت کردم.
گفت: «نظر شما درباره کانال پاناما چیست؟ آیا آن را بزرگترین دستاورد خود می‌دانید و در مورد این واقعیت که دموکرات‌ها کانال پاناما را به قیمت ۱ دلار به پاناما دادند، چه حسی دارید؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/131346" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131345">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/131345" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=SPAi5NU0wm2dSktW3Kqwm3BmLlbcVjBpDRrNAoUHV3PxSbDTuqnVVN316JvO2-W8VxffGDrhieRRok_pilXPYfrjbUHdKLAbgqY48ejE_0eeu1FTJ8smT9Ypr-mh6IWTQ98QqEnAZEE454SjmncMzu6ymNPZ3Zxe09UZppIjk3uQuVae5cn_k3lvpGg4semOJBPGvoq-KS__9l1yE5zY7llIwf_QFKuTEC39M5txF-VTZopQa56uh2poBo2KcXW907wQUs1FWySPSPPf0qB75LM8mzqKvxGW--_iwfsRRtiJFPQtm0h2FzFyFWvzAtwabwAUIrKoFcUIi8jDqWs7lGs1dF-BEOcsCSPC6Yf95Y9-dhrXaNh1N_tf5NfuOJzakjUsZc3NTP8q7W_gAZ2gHswVJYiykm4pi3m16ms_9KBlnxgJMEnqNfE6LYY6ebe-QHIsjgg6C1vIdEPGb4b68--Ckjw9ZWyjEgSC1UZSHZSdDn3Ww4XL0BfmZ3vyUdk-eapjvcs00mWx4WALEbt0bWzA58keoeMTC6FTq0fsxBrEani8e3eFZNeIxhrxZixjzjlWT8oxRiLhAsWQHxUF51qrhhwOErZkJlzXNK_PhspurvVivrAlI_PB-T7SBS0jMj2zBtL-__Ziu4ncQYv5s3vLqRtJgOfgHDPXmZMSzds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=SPAi5NU0wm2dSktW3Kqwm3BmLlbcVjBpDRrNAoUHV3PxSbDTuqnVVN316JvO2-W8VxffGDrhieRRok_pilXPYfrjbUHdKLAbgqY48ejE_0eeu1FTJ8smT9Ypr-mh6IWTQ98QqEnAZEE454SjmncMzu6ymNPZ3Zxe09UZppIjk3uQuVae5cn_k3lvpGg4semOJBPGvoq-KS__9l1yE5zY7llIwf_QFKuTEC39M5txF-VTZopQa56uh2poBo2KcXW907wQUs1FWySPSPPf0qB75LM8mzqKvxGW--_iwfsRRtiJFPQtm0h2FzFyFWvzAtwabwAUIrKoFcUIi8jDqWs7lGs1dF-BEOcsCSPC6Yf95Y9-dhrXaNh1N_tf5NfuOJzakjUsZc3NTP8q7W_gAZ2gHswVJYiykm4pi3m16ms_9KBlnxgJMEnqNfE6LYY6ebe-QHIsjgg6C1vIdEPGb4b68--Ckjw9ZWyjEgSC1UZSHZSdDn3Ww4XL0BfmZ3vyUdk-eapjvcs00mWx4WALEbt0bWzA58keoeMTC6FTq0fsxBrEani8e3eFZNeIxhrxZixjzjlWT8oxRiLhAsWQHxUF51qrhhwOErZkJlzXNK_PhspurvVivrAlI_PB-T7SBS0jMj2zBtL-__Ziu4ncQYv5s3vLqRtJgOfgHDPXmZMSzds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره داگ برگام، وزیر داخله:
فکر می‌کردم بسیار تأثیرگذار باشد. راستش را بخواهید، فکر می‌کردم همسرش کاترین حتی تأثیرگذارتر باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/131344" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131343">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641158562d.mp4?token=hBzsfYbCCpb-noSnTob0eNk8cQrfCTPGsplgMUep5_aepOlH35X_GfrTGIlymej8B16NC3u9-7V3IVqY9yG5c3nCIzCR3Fsri32ymnmQBhbOL1na8Gk2CoHyBpWvvzv2Vg0EQ7NyCZlYZkkkslkwoby_vwq0zGKaPMW62gJ2T_QKbFAaIacRM6oZR0NqINnu7iSv42EJXKx_Tq-msCxYfMpVZzqEu9d2OJwGPyKrUl8p5u-CktJgPQnZA5NkiNeNy7hHafMBDAQwtQy7JfeTHPvHT1saxjzvy5SjH4chkWqBzv2Brwf_E-o3oxL3T9_Ec8-RCzwTKtH-ns4-NvuUgYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641158562d.mp4?token=hBzsfYbCCpb-noSnTob0eNk8cQrfCTPGsplgMUep5_aepOlH35X_GfrTGIlymej8B16NC3u9-7V3IVqY9yG5c3nCIzCR3Fsri32ymnmQBhbOL1na8Gk2CoHyBpWvvzv2Vg0EQ7NyCZlYZkkkslkwoby_vwq0zGKaPMW62gJ2T_QKbFAaIacRM6oZR0NqINnu7iSv42EJXKx_Tq-msCxYfMpVZzqEu9d2OJwGPyKrUl8p5u-CktJgPQnZA5NkiNeNy7hHafMBDAQwtQy7JfeTHPvHT1saxjzvy5SjH4chkWqBzv2Brwf_E-o3oxL3T9_Ec8-RCzwTKtH-ns4-NvuUgYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من دو تله‌پرامپتر (دستگاه نمایش متن سخنرانی) دارم که کار نمی‌کنند، و اینجا ایستاده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/131343" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قالیباف علنا به تندروها گفت خفه بشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131342" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید.
🔴
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/131341" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Kf4H8M9ZkD0MKgkU5D6EwMHEgU-iZKMK0p4N1IF-9CDKf1fanPdIwcdmzgvjTgy4VV5nLXYQd6aaGJH-HD1vAippIVsAvzFIhTCK_zf3ppbFIHMm3ZMZtuAul80xGBPU-yHv-CTud2s3Zc6X_-_7rCUnajPMqIIcQf2T5yDeEqC1BhsMgo7u1iqqTHMQggAmWA2T-A-QHQI722yYBkYeD7UrLbfENOKODERZs9uL5tKB27ehAIdi8Ve4epRtnzeF4e89y17eXVjhSKtcDHd_QuvcybOo4De5y2F9LDeWXFReLb1J9wLs7U22oz73wG-IWugo_0-kQEERDP2u7kekPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Kf4H8M9ZkD0MKgkU5D6EwMHEgU-iZKMK0p4N1IF-9CDKf1fanPdIwcdmzgvjTgy4VV5nLXYQd6aaGJH-HD1vAippIVsAvzFIhTCK_zf3ppbFIHMm3ZMZtuAul80xGBPU-yHv-CTud2s3Zc6X_-_7rCUnajPMqIIcQf2T5yDeEqC1BhsMgo7u1iqqTHMQggAmWA2T-A-QHQI722yYBkYeD7UrLbfENOKODERZs9uL5tKB27ehAIdi8Ve4epRtnzeF4e89y17eXVjhSKtcDHd_QuvcybOo4De5y2F9LDeWXFReLb1J9wLs7U22oz73wG-IWugo_0-kQEERDP2u7kekPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «باید به شما بگویم این پرواز افتتاحیه‌ی هواپیمایی به نام ایر فورس وان پس از ۳۷ سال بود. این یک هواپیمای عالی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/131340" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قالیباف: ما خودمان در مجلس قانون تصویب کردیم؛ شورای عالی امنیت ملی هم مصوبه دارد. بر اساس این قانون، به هیچ عنوان به سایت‌هایی که بمباران شده و آسیب دیده‌اند، دسترسی داده نمی‌شود. این قانون است.
🔴
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای عالی امنیت ملی تعیین کرده، نمی‌دهیم. طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔴
در حال حاضر، آن‌ها فقط در دو مورد حق دسترسی دارند؛ یکی نیروگاه بوشهر و دیگری راکتور تهران. دسترسی‌ها فقط در همین حد بوده است و ما نسبت آن متعهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131339" target="_blank">📅 23:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔴
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/131338" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قالیباف : می‌خوام تو سفر به چین
روابط تهران و پکن رو قوی‌تر کنیم و به سطح یه شراکت راهبردی برسونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131337" target="_blank">📅 23:08 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
