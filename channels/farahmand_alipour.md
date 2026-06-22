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
<img src="https://cdn4.telesco.pe/file/LT3hMl2R7w7y6l6yPsDugVDXYOPjJa9G8Gk1FUKJ6Nhmgy4ULMkJzuEgGDC5EzO1keP65ohgHtQj1ODY-zI8fuwkN_N_CocBgfYYOKHSTgsDr5G_cT56Lx8CnlTUV9PyV0F4YLp2UK-z8E7UC-pVNqBD1E4ioe0GQo8wSI_eIT4guiIFX4ZC26Tf27e-si2Z_lsPJfNi2Z3LglHm9P85Yray1HaAvbuuuIMXFFXyEnC4aRXaZJtqxxXCljUaARVfDK2pmNa8qkTD-oHB8XLyGMESDan5GUPQJN0LPwAx0tz6yjOKHyQ97lKNkWW1aEfu-8w6LlZjz-HyCJGCYdi-Kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRMGjR_kUKZw5WQQVNdhkE4kdvWUBddcFTmeYacXXlQY5hLqYnaBWif_KFM1dBbAmJXangMEGrmuH0jKXm-L5YLqY_pyEzvV7RgRupCB1xG20vZHBkYlf9YQnC5AfztEsWAsHxh85dvMRgNb9FXN3yzBhdOf6g_2rVsBXPXQRaoaw6tnm3AnSE9v_OEgS29MfBMjmxOBHbs9MpuDLw8gsx-TU-ehGE6tIiI1hEmNvQhujfaXe_EObGgQr3cfEZn2VytHEuTG_qB60fULSpHbcfLMPI3Nl9k6wN2V1O-x2Lj7Inl8girEmUQB5YRDGTAqc6fSEC31NJlvy7j1ZndjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIinY0MFaAW6k6z2K3hUb0170UpuB2heigF5UcSdeuS91zQJ5vy1GubbRec2t-dvqz_jKK4Qm4tmjSs9x6x6lzsJIhnTw8Fk_bHjWJPhNH4x4Oi5LjugAiWnjCj2SHyr3k0ah2QYyhWysAica4RerzIkeP1l4rw5sar9hEWnjCkP3iElB38-lorz5xlaRsyyrbyC131O0D9I6NY_cmVtCmkX-WQkSaqlYsu1o1xo8gitEj9A6LaTEebeMXX3VBWgyiqTcZzLAZHa-Dzbdsxp6pBmECf5f6qAwfewWsKdnbkq5t6fZ4chpgkHzVyAFfMyQKcsgoT5JIcFDZDN6N5IsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRJPVLvahshFW0k6cQc419bTwku_x39NwS7WiGVBNSSnpozd2yn0VvhVte2Ipg5wmBqco4gJeOGfE-f4L5G__XrTrnkVyWM6l2TLPCbR0eeFdv7xfC_N5klzYXoiz-MKlq2o-LjwAzVdZQ8qYnggblArunLF3tfF2WgZxFBdlFRv98BiJq6OJcmmZ31tetKHDtOneBa7qaAKf-BCJLDftAtP2XUHlpaEwvvKJHeUoENbfJLQr43BTg_TqW8eMeSUOd96x-Qu2jriqLOO6r6AmA7-OsdfndoHCqgWJBEJP5xq5ydWICBI52ltCgNnmo5Jw9efDx8nuEk628Coj91SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIYhK15Sh0cGS91laW-EHNkwXJ1erUyknj2kwnWuYQEnWK8Ra6bD5C4JWBbpZhG6G5N92AdhONmky-ExHQAM3nDvLeU8cw_j4hg1GONC33pEVwyjHIWvcs0MjRtCBDTNItnTnei590jAQeTHI-B2qtDZ_TansdeD7FCTBMCcpXn0dHHvJCMPitgdUJPxBw7uFC-6gI7IEzgcWXIUsWEe7uAXnfUL7HrnZ0QTGY8W8ORvusgJ6onnHxRNH-VjziZgQ6xdGuaQvnn4Yl-1dbw7ysf89H_hXckK3KW4jd-72JbVem_0rYPxGiyugZp6kuN4M0Ci_RZWhTesaXemaAebPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kk6UzVHiJ5a-wdt0SySHcSrQ8Y-4lxQVZTO6H2iQzaRkCpqU-5HA65T3835alxbJElUi4teeWwwuGK--Uaj-E9VTOP_3YcZWEVx1Zb8ugOZ01F4MUCqjLb5ZSgcGH823Pj7GN_aQS_4_6MZ6wKoymD_gRN-Lz6DcdJkbBoTPNfpbeRpA30GGt5fGqzAHyLQiakSlhzVQWVk_y7sBwpe5c5zAkXKZ-9F471rtEgj-oMnS0fPeHQyH0TzCT1wcyemKXXq5yeL0mzki0WjVLkBsBUc7ZPpUZM6fSWI22_grsYvtYQYWnrrthHcwJp37YPKhnRVsVLTdjpx3K6JOKSkw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3Qj3kf-JJzINr17Bd4aFUCxfE4RNS74s08-2sj1vTt1Y68KO7rkOl8bv5Nzr6Dxpy-VSDZqbC-OgtuwHMXozZsPT7b3O-1gIW4parsuZEEjsYqAx6nrAQFNYpoyX19IC4psoqsnlqurvaZxOF7YRdd63iLoPo0N1BY6lFHScmTesRFSIgicaurVD0fJufELkf32dI5wuk03y_Ezw88HG90GhfPHercRsaInDzNgSuDYEF6VanyYR31UU74SA2PqN4sRfq9kzt07ZSWG-01uj_UEuq4NE5e-toJ1_WHK5g0cxBxflg3z5WOik3uG6GNQoRzm9ZLe02dTJzDPSgM0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgSKtERFlk7GeVHmOibaVa04Ek_gRAxDA09ET419nXzjgZnndD1_lSPx5vI7X0iA1bkJGuPSXaaBDoRMbh2bGf89RenuHNDrBXrYeu3whlkmTpYTXCls9Cs-2NyKW6P_2ijn2BFI3QCQ7XEREsy0WVKHR2lIVdLZviMzo5tGiIRyV5QHpjvMaupkOTwKai5wLr2Qi5zuA66CKfj9Oz2J2i2fRAKuNOjnHT6BPD6kA2b_45gaauXjUXBFF0jtSnOQyUwo0AgQUie6K4EExUKLEh79O6p3K83gsooTPwv1VDQ2fX5jPQmmbouBLU9jssIYCrGiPYFH14j3DSFiLNlXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBdeWNzf9v2czF2d-w4ILsENvZZaBY7oYT7T3MW_SMR-9JwcyjEJfHkUQh801LPyYGwrbOs1oSwAzKxmR5OJZdnUbp21v8rMaOV5_XH-JE2zpG-okI297oV1HBmQp6Nyav32Ts8LRUsXD3b3QN_w2nRTbRYSUUT_uyrfhAz4lXK9aSz2OdpjJcYYROp1ffwmO8kIe31DNn6Y9xaVDmbulXfBV942xlTxfhe7NhPVxyFEfxG1lZBsRj0AuuBXUN3Keex-qz1MruXuVHthv9HEC7-DbCkKAMOg57jVMRIbx2Gjlwn-JI6OWqYoGnQDzjoVWqezF3qjWNzoDPc0mcM_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=lDMnEdWbs3c0oCu3qJj0Ri4zry2IpEYAPONWLmiOn6aaljy8GGCgH6ysrralDxt0RZhj7uwV8_Mw2ZgylnEbvetl8mxO3m_8fSY5q6472QijcH7KOrHjmy6aRJt6SzibGsVjjCC9B1Tc6MaloSW9oiKFTLcP4-GLMnSRjZnYNIReoclccIzckaWassZlDNJ0ZZeBoN-0H-g5slm1DzVoc-rV3ELvSvI5a1aKOY0bUhgd6s2iPUh5dc5qeiLH_MwFEwnInl5qS1eqjqan7eOJbXmsm9ArKAKJmo9hnxk8efSs7zs4pAeLeKY3soHzY7DYP8di8ZepK9W4Ni3rgTvTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=lDMnEdWbs3c0oCu3qJj0Ri4zry2IpEYAPONWLmiOn6aaljy8GGCgH6ysrralDxt0RZhj7uwV8_Mw2ZgylnEbvetl8mxO3m_8fSY5q6472QijcH7KOrHjmy6aRJt6SzibGsVjjCC9B1Tc6MaloSW9oiKFTLcP4-GLMnSRjZnYNIReoclccIzckaWassZlDNJ0ZZeBoN-0H-g5slm1DzVoc-rV3ELvSvI5a1aKOY0bUhgd6s2iPUh5dc5qeiLH_MwFEwnInl5qS1eqjqan7eOJbXmsm9ArKAKJmo9hnxk8efSs7zs4pAeLeKY3soHzY7DYP8di8ZepK9W4Ni3rgTvTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgq5-bj90lOJ3EZOrEqyh25aVxF6nFKyIg7DJh9WYa3gNmh3eBkTa6jhQrq3mXJOHJMkx9st-q0sfnPwC0MigaeGEcMI6zj4Tz53rCOASxLXSCdFpK9KRUo9m6Ux-71fWfSGe34nvy5ZAXATURUiScrGPXFX54TA5_q3D4sEL6EjR3-1CnjB2HCAVx07zqfVQaajNFHXXNB-wjYuztOAokw-V0XswRrNCxkdJN1tpwZKmtsDzwbmoYjrJskysJtDcCrC-thGD8d2_wpzQDBalA2CHK-NZjpBM48wA-5uacfNbdcTeMYfnBRumXpNSSrdvg3sIeNlwUYndp3mmQSWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OOB1Dn50w4GsobTpwCHE_bV0u3Xn6-UGNBEFLqHotj5Lyeps9OiP__nJaHlb4hjhwnphRcdHonRXdL6R9weeHE-sjjRSjjGb8oEKRBysdUf5Uvrlo6T5wGBLy6Q394hyKgfq2ta9TqcakqrXPTrQsgxDnRxy6xDZ-v6jB9_JYaHd0NPnpueUs0vx_s2Q6cNjv680_oWY0ya8wm0mlVv-fP6PUhTAwWnMiYGJJqmF3b2mQn0k_ObgBdNAV2Pc0g3QdF4SF_z2rgZ3VS7qEeNIlJvbyvUFAptc99zv9X_owPCWoKYd5HqSQ_9sUpqobFSGFDZx354gWG2teC8V6nBfew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OOB1Dn50w4GsobTpwCHE_bV0u3Xn6-UGNBEFLqHotj5Lyeps9OiP__nJaHlb4hjhwnphRcdHonRXdL6R9weeHE-sjjRSjjGb8oEKRBysdUf5Uvrlo6T5wGBLy6Q394hyKgfq2ta9TqcakqrXPTrQsgxDnRxy6xDZ-v6jB9_JYaHd0NPnpueUs0vx_s2Q6cNjv680_oWY0ya8wm0mlVv-fP6PUhTAwWnMiYGJJqmF3b2mQn0k_ObgBdNAV2Pc0g3QdF4SF_z2rgZ3VS7qEeNIlJvbyvUFAptc99zv9X_owPCWoKYd5HqSQ_9sUpqobFSGFDZx354gWG2teC8V6nBfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=N55dWWRotSbpoEjWX6mYCd2gSjmSSqBdAt3kDW-XyjPyQfgSoJERTouzuwnLO0gDZigppBzalz3hcbyDYCHmdb9mu09X0BSq8rmwUZGw7EwZoCBEzsWGAQAamBBrexQnxjPI2xtT1Xa-By5Ju7h56sGFJQG9ifUMPhP4LcG0v-tSeTha5rZVyyImh_BVCe7dLE3vdtgDBENEPf3EN3GUmtLrWKAgaPAlUvAgChqH_PqScVSltq6As84gMxqdX188KhL0aYw7RPVuQ_Uj7nDTlYFBi43wtdyeEwrak-k8mIY-kEyfQyxnp1CGZzecD8w2O2BFcL-fUfCy9_1yzWrD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=N55dWWRotSbpoEjWX6mYCd2gSjmSSqBdAt3kDW-XyjPyQfgSoJERTouzuwnLO0gDZigppBzalz3hcbyDYCHmdb9mu09X0BSq8rmwUZGw7EwZoCBEzsWGAQAamBBrexQnxjPI2xtT1Xa-By5Ju7h56sGFJQG9ifUMPhP4LcG0v-tSeTha5rZVyyImh_BVCe7dLE3vdtgDBENEPf3EN3GUmtLrWKAgaPAlUvAgChqH_PqScVSltq6As84gMxqdX188KhL0aYw7RPVuQ_Uj7nDTlYFBi43wtdyeEwrak-k8mIY-kEyfQyxnp1CGZzecD8w2O2BFcL-fUfCy9_1yzWrD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14DqUyzcDLMh8ROn6n-yBOv8MaR1Se43nWVZ8FhzWfOtRLwGP8APzHGIazEDHKlqOY-flR4SbKb9l8gJ9EE-756Y9135rGhYPtvvOjgW3lhYUr1lxieB0pZaSCpojDX6SAUr2lKV_MW2zEO2VS6MD0B3weX9LzBq0iTFHmW3WblJa-kviI2tciKRisr4mEd8kTbvztC9_M6RDgh99nXZnR0olbwkw0E3VOTl0bsqTO4BPdWRsBN5EeS2TvuYM2snjUIv6OvJDjzNWeTcJvFyA1_sDDtOFExCH_njdde27USsc1BgPECfXm4PIBixP2h7z1_hGOkBCScSTozgPYZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC99gtbzcJb84DccOJHAd8-PQxoRqmSPgfDs5EJA8q120r7um-4wWw6XbKSt7nrXe229lUGUoXDhk8B1HClTLIjIceVA_uJ5ZHqswOOcY7fQouR5MWJRKl5lB_V0CjzIHB-VC4G6nsWxlkMCWQLhJAKYCym-YdQXhDrzUSAoqTZ6fXmHOhxMRZVdzhBuB6SLxiPmpr60CvkJvpig9_FZt2Vbp5bNx4i8pSc9fPs8letu0oQSSeBUucgSQwfIpFr32LHIWfnAuKhIcUMnrkJBrsIpeLoYM5iGjMqSGmMmK1fQgF5Lhv1MgiwNlwGwtJRNgsIygdhxd9GEtqKbMl6UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqXhaaeBJNs51WQkXYw712PY-vmwcPgnOwkedSH0Su1ogLDKUxUtTbsQQIdZD8ayGQlDeY_MJpQ1e2tOXfNSzoofgoTjk0fLtllxMNWD7Ls0uThEwK59McWlu8aeshUJCz6NKk-Pmg3J_hQr6sjNE7i8jzTbb-tMjZNK3UFWWXv3k5E-1PGRjp6Q50NPH_EEczsqXH_ZEUR9L6JIDbOQzVGV1ygwmugaMSDK4d02o9bphHwxTGC1DsOLikD4PMazjWfVDWPJ_gYOWKeg-nmgxnM0eWRP3eW38xQoq9BGBaCdgSfPtOTNqH_B9DPa8Dp1XER2ihASo10ZbK857T68YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imJi3SisCkzsdXYRkyrN8_4GwewyNuGEO0eWG6hIs6JZIjZFxba2BBuQLdIzU5cgR_VfQb4OBW14XfHFzAUoh9ns_PEG7bJWA638tkJWOqvSz22ssFNvVs2WkGqiI3tqK8s56WxjAIQqGcw8pPUxcUK53uOA_gfYT8f3Eokk60XA9XJmvCY_yK3NQ_z5haoQ-zQhHqvtz8vymxio-gLCgmSTQcnLXlB8ugozVBP81r3mfcQaXZTd-Q3l8HZthI7wfa00T0RKwlFcDE_sPLXT93oFocZ2GatkK-wZQgeiNogky7D8X83IVHgdryo3eb35gOJaILj3D5_W-o87U9AKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxAMfYkVw-JuBGIdR9Pa5ti3ncdVUXyli432qYzJ7XFhCA1yC85On5qCovAJXfVC9LWgssJSGOK7ijXJvENGjP9Td6CPNsGfeymmzhKADZOmzPHJxyDDRK3mNAN0_UNFJQ9MnpWH-EvP37mkScS4OkhEyhpIryUMQgSB92CtgKMAPFFChBvbZ9U9cvrsT1Emxg5C4nOA-KguNKMtZLmdYLh5_KxW1htZwQA2lMNQ_ymSrefvHq8rniPNY0WZoTRaV3bEGN7MWX6f5jvWmTPsi-DksototeM4tvkMZ__emDnkH8Qg5Af9b7Lx6oeMNXUUXrx2YNUBJzzQ4r26RSgZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=elmce35eScg40ZY192wI8S-vBVRvAs0Hwvm6QuW-2VRHth1Z8NS2SVt3IihYQCnSkn4XHmAjsJYpCPUnH50z-y8StXBrB3qkNWfH5IHMJk_bQA91ToUPCaVUy17ocXoRDtVXVJse7VmaSWsYWcKBaLkYZsBY1kMzaC2kdHFEpMZ3ytv3A1UW2gxITV0VYyn3fKqqRFXOAJg-xG0l9vLqDjSqjGxhZ1WUcLrTNv4X_mYQnA_d2z2YLXmYtseXvD_DNUzpxfyXiNqku0ecYwriEcTaTg8wEwXFDp9AJjW6We-xnwRQeeUgHNDj1B8gIpg6x28dym6EM5m4gBXZ9UdQjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=elmce35eScg40ZY192wI8S-vBVRvAs0Hwvm6QuW-2VRHth1Z8NS2SVt3IihYQCnSkn4XHmAjsJYpCPUnH50z-y8StXBrB3qkNWfH5IHMJk_bQA91ToUPCaVUy17ocXoRDtVXVJse7VmaSWsYWcKBaLkYZsBY1kMzaC2kdHFEpMZ3ytv3A1UW2gxITV0VYyn3fKqqRFXOAJg-xG0l9vLqDjSqjGxhZ1WUcLrTNv4X_mYQnA_d2z2YLXmYtseXvD_DNUzpxfyXiNqku0ecYwriEcTaTg8wEwXFDp9AJjW6We-xnwRQeeUgHNDj1B8gIpg6x28dym6EM5m4gBXZ9UdQjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=LjoX-pZe4iSUpWsio-VhXa2lo3sYhYWVdswIAdMthZWGDfHnerhfUyBbs7kyF5YaeDDlx0brj9CQTcE9ozuMK4OXAw-wE7G-CyZfu1poxXZYYa695dOe9IwiHdy71Enqs9ZTy8TUfJenAntA1q_9KWgNYSRDNvQuvJxAEgTV7xAIIWwJ5ofGKcFXHuFgZXQklx0bcGL9K7jSBmlXepA3t7mJb9Nnyz3FhSji2Ba3GNv2RmtSAdl9PfFSp5r3DPg4ee9uEueY8cZfV9CY7Nv4HZ6fX-w0tVbMWHGXBKDfExhuDZyYyrTU_G4vniEtZ_mczkv_ZdFyRaeJvtLmpMLKzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=LjoX-pZe4iSUpWsio-VhXa2lo3sYhYWVdswIAdMthZWGDfHnerhfUyBbs7kyF5YaeDDlx0brj9CQTcE9ozuMK4OXAw-wE7G-CyZfu1poxXZYYa695dOe9IwiHdy71Enqs9ZTy8TUfJenAntA1q_9KWgNYSRDNvQuvJxAEgTV7xAIIWwJ5ofGKcFXHuFgZXQklx0bcGL9K7jSBmlXepA3t7mJb9Nnyz3FhSji2Ba3GNv2RmtSAdl9PfFSp5r3DPg4ee9uEueY8cZfV9CY7Nv4HZ6fX-w0tVbMWHGXBKDfExhuDZyYyrTU_G4vniEtZ_mczkv_ZdFyRaeJvtLmpMLKzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=r-HS5C05NfxlZZRJx5aitffp2WeRwuhZvvZYO_aAU2kR5H9wjbjJQlQutjRlHubwsztayiTyKn-97-73-LGzPTEgH9h9Rn2uziqS7AMX5WWlFftW12p7IJtSk77CtJNguAo8sa4KEenPCU7tk_j3N-z8fZfTwxN_jW4amFCavLOVErQyhDZmBd0RucxvNR2UI26ODSE9_lxi-llC5V_tCfCyr7wkBFTO-qExc9aD_aVoVjAkPNu7lajrG3dEzMCxmd9nfmyPCyfoC8fsYGLxmxlW3_4JGK8BTD-N3AdNmxYe2p9OocQCnzV7s3bQBdpboo-biL8jb5koCRUfy3eCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=r-HS5C05NfxlZZRJx5aitffp2WeRwuhZvvZYO_aAU2kR5H9wjbjJQlQutjRlHubwsztayiTyKn-97-73-LGzPTEgH9h9Rn2uziqS7AMX5WWlFftW12p7IJtSk77CtJNguAo8sa4KEenPCU7tk_j3N-z8fZfTwxN_jW4amFCavLOVErQyhDZmBd0RucxvNR2UI26ODSE9_lxi-llC5V_tCfCyr7wkBFTO-qExc9aD_aVoVjAkPNu7lajrG3dEzMCxmd9nfmyPCyfoC8fsYGLxmxlW3_4JGK8BTD-N3AdNmxYe2p9OocQCnzV7s3bQBdpboo-biL8jb5koCRUfy3eCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=erpaBMWv4j5XCdXS5VA86_ZzNRM8qrc0rM7CwiUWxhmqXJTY55xTSGlZBH0ndJP50Qo6ooEInkKrQc891d_-XUBs6MEYK5E-_0oFkPL1aL1t5JPPcn6WEzzUcjg9jYpMC05P11Nu6BmyRc2SYfaJU3FUKK9fsGqQTTHmsJiXU-D8XKlQY-6OHM5sCNfv93ZkqFgpyM4Qhv29PinQQkjZ58sDtymi5-xAERwayTLP26a422zZzHZHax4Bp06B7G9SWDBcUMiwqFkqa5ZQPPIxwGfvpXysFQ6d_hNcZpUyz5mwjT71ZWb5Nhvmhko2RtirEv2WR4xHOIOZ73jhWr5C6QbKI2U8qdUSVYfvPVvSmuFaTMd8BuVUaaAa-z0KQOIFO4fWcD-qaCAEsk8nVUapWfSB62X7TG80i_zSNrp8fDoGww3PG9UnCeUM031X-yGVmGav1zt-MHAEynAyCr6KbAgnOCjvASxzbU6Cw1tJhr9OKTQ725ezWNLHN_n7OhdIEtZF8V-HVvjOovix8rXF1-Ru2urPirXcwZxy4AyZSYslWpBQidZkSZIdeT1y4uzPReaGiJvzPv6bPkWP0XPLFS2Pmi1CHJw4vxnYaSTMYs13q7Yb6n_s-Gd9usSwvy8BvkZYana0e7FWMdSqBjbiRnDG2pdlmOg_2ANn3_FlYfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=erpaBMWv4j5XCdXS5VA86_ZzNRM8qrc0rM7CwiUWxhmqXJTY55xTSGlZBH0ndJP50Qo6ooEInkKrQc891d_-XUBs6MEYK5E-_0oFkPL1aL1t5JPPcn6WEzzUcjg9jYpMC05P11Nu6BmyRc2SYfaJU3FUKK9fsGqQTTHmsJiXU-D8XKlQY-6OHM5sCNfv93ZkqFgpyM4Qhv29PinQQkjZ58sDtymi5-xAERwayTLP26a422zZzHZHax4Bp06B7G9SWDBcUMiwqFkqa5ZQPPIxwGfvpXysFQ6d_hNcZpUyz5mwjT71ZWb5Nhvmhko2RtirEv2WR4xHOIOZ73jhWr5C6QbKI2U8qdUSVYfvPVvSmuFaTMd8BuVUaaAa-z0KQOIFO4fWcD-qaCAEsk8nVUapWfSB62X7TG80i_zSNrp8fDoGww3PG9UnCeUM031X-yGVmGav1zt-MHAEynAyCr6KbAgnOCjvASxzbU6Cw1tJhr9OKTQ725ezWNLHN_n7OhdIEtZF8V-HVvjOovix8rXF1-Ru2urPirXcwZxy4AyZSYslWpBQidZkSZIdeT1y4uzPReaGiJvzPv6bPkWP0XPLFS2Pmi1CHJw4vxnYaSTMYs13q7Yb6n_s-Gd9usSwvy8BvkZYana0e7FWMdSqBjbiRnDG2pdlmOg_2ANn3_FlYfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=FE3hvurlYUk9s_Wi737Y5rYq0XJSyC64KqVypzEkVb_pj33SlmOb26m7t2Ctv-l42ygN8q05J-pkg5Q1MoURy_wyV0UCds6MQSZhNvrIgVXbOVu7bAbEZeeJEK0NN4CefaD9KraDxel5WD_M4RNjzlms8d8_Sj61Yx5CSfXV7Lp-BZEqGS8U6dR4kQyuucLx4QppPfJ-cY3V4LE2CDJEsgm6igK908kpgHFXHQrizXGqNSU7t7jOzW3sDJ0bXwdz_Y1spGKnppEIJus84y4BYrSMyRHeon_2SS-tQW8LE1VzbfUA82-g9CgPRLJz6XIsT5Uot7yUbL05eX7p4vY-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=FE3hvurlYUk9s_Wi737Y5rYq0XJSyC64KqVypzEkVb_pj33SlmOb26m7t2Ctv-l42ygN8q05J-pkg5Q1MoURy_wyV0UCds6MQSZhNvrIgVXbOVu7bAbEZeeJEK0NN4CefaD9KraDxel5WD_M4RNjzlms8d8_Sj61Yx5CSfXV7Lp-BZEqGS8U6dR4kQyuucLx4QppPfJ-cY3V4LE2CDJEsgm6igK908kpgHFXHQrizXGqNSU7t7jOzW3sDJ0bXwdz_Y1spGKnppEIJus84y4BYrSMyRHeon_2SS-tQW8LE1VzbfUA82-g9CgPRLJz6XIsT5Uot7yUbL05eX7p4vY-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=sGkw28ZMU0wrW_xOCfTkQ5KXAiGEb6p1IUYe33BQRqEnf-tY3BXLbxDY4FQkm-q6ZVZqaEUza_zvNLeWvPIX2ID-zYv10gFlMF7UJHmd3DhEbWXA9607R1lCbOZWm1QH2mj7_Ii2-cz5IIEkhBpvsWa9PxJc4c-bq_-9dVdETT1Usyx8wyrJDZD0PzMiYIqw04zyMB8OeZl-Ndy1uoqTVhaLnWvRITfyD0RKhMbMDbi8sHlpOZXimyONqpUCMJqLEL7_1AzbVyg2GUEMdbYqY3m3DFXUGwG3aalJgsdxM1BAJo4g_nERgughCIc3Lw-4ScLUFGEiXhSze8XkhJZG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=sGkw28ZMU0wrW_xOCfTkQ5KXAiGEb6p1IUYe33BQRqEnf-tY3BXLbxDY4FQkm-q6ZVZqaEUza_zvNLeWvPIX2ID-zYv10gFlMF7UJHmd3DhEbWXA9607R1lCbOZWm1QH2mj7_Ii2-cz5IIEkhBpvsWa9PxJc4c-bq_-9dVdETT1Usyx8wyrJDZD0PzMiYIqw04zyMB8OeZl-Ndy1uoqTVhaLnWvRITfyD0RKhMbMDbi8sHlpOZXimyONqpUCMJqLEL7_1AzbVyg2GUEMdbYqY3m3DFXUGwG3aalJgsdxM1BAJo4g_nERgughCIc3Lw-4ScLUFGEiXhSze8XkhJZG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6C2FRx8b9LEO1dpikftoMdVJT8HzCSJL3sAdWewCEIR_lJK1yIyiJDaNh3xCjWyDxe0Lpf8v9sG40IkE405G5QG2VGF_zejTbqDik-zCQwp1ZwCOQmjTpIZ_6T5aI8KQuzOfZ5JUOkXZ_GTVzdPcI1Rc-wPQVyaXIvZSlkwk6N4dlSwPNPQ3hLHOseP_kZ9f9U4sPYlsL7SVqt2EoYx6wPpg21orE4E1gvGZ9o_ygn0fskje1ficOjWh27LKqMmj58yoeAQxjzIKY9SC64vnh-QebzftVZXTAkcdtH5Ij0-lp757tYYBqimbBrA_CG6hmORqJbZRx5rRu5FJ8FLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=k1i0gCWBz8TUDPeako8jhHv0dWuBzSjWxnnmHtcYxBeuRFVw3vyYSQUVkDmCvOf8nUlo_vWVBKJYX0eBuMfHiQf1u9uIg-rYUJjD7zfjFCxv2LmsGYrSURuTnvnlQXlZ7jwUJpZ6Ou660_wZyQIBMd7DcMSTQEs0RJKhzbJPapjUt40lDsAMGX0ILzeJmGEDsLACDZp5U2Mc4nKV0oPCrcmYShHHNvOirJ9k5T2JLczIj3e2CJtN7UxND0Z3JNW6XaNl9QrOMKlihAs0FJP7Ow4iGSlgWi0c62MXN6yorNL7DtUYiiDQKpEQwBfziIF_w5ZUL_b_hPFWhcH4eWnFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=k1i0gCWBz8TUDPeako8jhHv0dWuBzSjWxnnmHtcYxBeuRFVw3vyYSQUVkDmCvOf8nUlo_vWVBKJYX0eBuMfHiQf1u9uIg-rYUJjD7zfjFCxv2LmsGYrSURuTnvnlQXlZ7jwUJpZ6Ou660_wZyQIBMd7DcMSTQEs0RJKhzbJPapjUt40lDsAMGX0ILzeJmGEDsLACDZp5U2Mc4nKV0oPCrcmYShHHNvOirJ9k5T2JLczIj3e2CJtN7UxND0Z3JNW6XaNl9QrOMKlihAs0FJP7Ow4iGSlgWi0c62MXN6yorNL7DtUYiiDQKpEQwBfziIF_w5ZUL_b_hPFWhcH4eWnFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIVqs5uqoqKAPFsujfLJCpjdVHmmu3FzpAMzouGvHH04eyWz9MDbj7soDfy6_B-oYdZR3pcjn433i8BRrJB3r3_sdoVyz0rIw_15EQMssYQ4be0jdm0sAF9fpyI_drNeTE703miDXoFnqce16pAGqzw-7px8QNECmPlXj9F19rc7QHPgf1xYmLiKVHPODCKwf9cLHs_y7ylHBbWdUAr1bwSMJV66CLW0EEh8AOgP6QcDiV3UDrtNGSSfwA8b4fD23ko69yMlb6REitETix8DCyppizdjg9fo4RdYNU31XjY3wjOSr9JHvKyC9u-60dvOonwDl7c52oHdVk465AOZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExVraZRCnlyYtYIakbhDcqIFp608FZRABbhs4JHUXvvWkvfIeczeE9e4Ffm5WUBXDPuq3SEUE_gv-dFwUIH4f8eylrg2I16vfM5JsUwwRQhnhZHjutrEEkfTtLLBJ2ojmRd-clASBU5_KNAADyHBgX5Lx6XOLfqdPEBMNJFqD5tl02YI0Tz784fgDx40yHhwuF_geUpcy1DJxgZlLmd5nVx7tWmwQyXX-UnJM1GRWN_OVPGDh-kA6Uj-yBXtIIEsB1v5bhUqAzhJzcBPfBaALLH3v3oIIv0NKdT9LlPPqma8J8lpnLg3-JqGVYLLdmDci1yDtbG1dRGilyA6E9o8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=VQ9a774OwWUIHDTh3E4GJCfDAjieEMXJvSCBln9HkD43_UBH246Slm6LgCykoar9RZaMq4U9-3ZfrI6jrINA6SOCU5z57uId85q0GQ7yOHmS0QmCaIFhZghTtpxIpDJmneI7qef8uMQxx9nT92fDvKZ1VYnFzgKEIMxhtLQ9le-rhPihAgJ5tLOeXry0avyWgDbdVYsjwzo2RWuaxlzcvwDjI2j8law2atrZuVdrsBj1oHZMyETYUqt8KwHQfGyZB--5rIgvt8891ZfcFUKm6GzaIyTwqjnmuAovuIccM2LepDtkvRK4xfvn2gChU9-AGogW3TVuqp2jNkDVpLnfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=VQ9a774OwWUIHDTh3E4GJCfDAjieEMXJvSCBln9HkD43_UBH246Slm6LgCykoar9RZaMq4U9-3ZfrI6jrINA6SOCU5z57uId85q0GQ7yOHmS0QmCaIFhZghTtpxIpDJmneI7qef8uMQxx9nT92fDvKZ1VYnFzgKEIMxhtLQ9le-rhPihAgJ5tLOeXry0avyWgDbdVYsjwzo2RWuaxlzcvwDjI2j8law2atrZuVdrsBj1oHZMyETYUqt8KwHQfGyZB--5rIgvt8891ZfcFUKm6GzaIyTwqjnmuAovuIccM2LepDtkvRK4xfvn2gChU9-AGogW3TVuqp2jNkDVpLnfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=qt1Q9mXSYGLlOBXrHC1T8tQUdCQILtHx1fau046gJ7hDIy1-GOwnK6Xbc-KymJqGPnoik01qAFje0k7nkAl-BV9g9SjP7LVTqV3E57LpEL9Qd-F9Eqz8lOMJ5NLvfXXKSCFX18ApOPg_ZCDfF3qgpNXhWYe0VVLZ36dvvQtbTcqXVHDKuMAeT_XJG2aESnYWRwcYyiOc_PB9UCMu9_KnZQ0QbMSmf2tCGsgQD6ivg0GpNLfWywSraKjEuCqN-0XJUbTxCtAPGBD1o2jAQTiaLL7Ci4GXPzZxOQ8vNFGOcJW2n1FxZboXsCguaqMrn2HZskDhfiZRB0Y3qOgy3sqK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=qt1Q9mXSYGLlOBXrHC1T8tQUdCQILtHx1fau046gJ7hDIy1-GOwnK6Xbc-KymJqGPnoik01qAFje0k7nkAl-BV9g9SjP7LVTqV3E57LpEL9Qd-F9Eqz8lOMJ5NLvfXXKSCFX18ApOPg_ZCDfF3qgpNXhWYe0VVLZ36dvvQtbTcqXVHDKuMAeT_XJG2aESnYWRwcYyiOc_PB9UCMu9_KnZQ0QbMSmf2tCGsgQD6ivg0GpNLfWywSraKjEuCqN-0XJUbTxCtAPGBD1o2jAQTiaLL7Ci4GXPzZxOQ8vNFGOcJW2n1FxZboXsCguaqMrn2HZskDhfiZRB0Y3qOgy3sqK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=lY78s6WGOFtZ0Ea8G5_tlfZ49SWAd2Y2BrbfyWoKcELVWA6u-jlLPhbb_VAalY7LBh9Fi2nufJzf3ROB88mXZOUpB0JQrr72myz6hJkoUooYH0EbF97-UxTiB1ZvCaIoOtyS0i_1sqd6-TlNHCTtBUDjehca6KpxBwW9S_daV_iI-fZV_Vh4h4WXR4STXOtk273MRYnJu-o6kbktBG9oVX7PjrLgGdZtSWh4PHTrG7865_tgWRLlkrSudD3t9RbM4W3lmrFk0YaGlhsrFcFu-1SA3LhNw2j1OUvGYn3PqW1eHQwtxfNb5mZU20M6N0ClPECzV9JHZNJ09ql4Ud-etg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=lY78s6WGOFtZ0Ea8G5_tlfZ49SWAd2Y2BrbfyWoKcELVWA6u-jlLPhbb_VAalY7LBh9Fi2nufJzf3ROB88mXZOUpB0JQrr72myz6hJkoUooYH0EbF97-UxTiB1ZvCaIoOtyS0i_1sqd6-TlNHCTtBUDjehca6KpxBwW9S_daV_iI-fZV_Vh4h4WXR4STXOtk273MRYnJu-o6kbktBG9oVX7PjrLgGdZtSWh4PHTrG7865_tgWRLlkrSudD3t9RbM4W3lmrFk0YaGlhsrFcFu-1SA3LhNw2j1OUvGYn3PqW1eHQwtxfNb5mZU20M6N0ClPECzV9JHZNJ09ql4Ud-etg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaEN3p_WVV3bzz2mTf5MWBGDRCEE3J4yYTHjpNx8QdsypSaA1y9kOgNim35fs1XWguAfTPcZDbZyK2-B1iG27ABJlER-tEb__-ZmnCd2H2xYcHtGUZp1GUNQBEBmObbTmG_Neu1Q6ES2e06iHbjOKVOQNcsc0NBvwNhwafOlLD6c5JIKLS9vxqHkmwxs1Rl61YPqhrNoF_6v_iXb8DdUou1JK3lU-tMh3afD7zGsuVc1MCPfzzzHCgMT5cEBbDY7ppo7CG3Z63gQoRYLgZoQ0leHw_QJ7k36vjUpNhMkzx8et7CBAQD8PWGCisGdciQMke9fUQNA8R8psy1tJJwggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=q5PQU2WOaibg6cRh7Nx1RV2lfk54p3nS7LdUwSm53-lAOPNHTorvc-rXLIuvoKwQU3tZgfYWCk8bXu0So6jkAbqfAXkn2W4agqPFP_mw8WqOXML4N9kY8MTnEMIZFwJU2R0DtG21gY_DwLSLVFqn0eBqamwLRTd43GtOcaW5h-veZZTAMCa7bPxWi74ImNtG1j_ANuQutNTd4cofFPRWRJtFERDZrQB-61mZp5LgFgGeSBQSJQ0DwnLGsfu7ZvDs2RErCH6hscV8NNkce4It1yreF1AflZCjYFEVl4MAWgxMOzVBcHN6n9IGR8_bFeXL6VJ6uJzHKHzJYbGMPuJFpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=q5PQU2WOaibg6cRh7Nx1RV2lfk54p3nS7LdUwSm53-lAOPNHTorvc-rXLIuvoKwQU3tZgfYWCk8bXu0So6jkAbqfAXkn2W4agqPFP_mw8WqOXML4N9kY8MTnEMIZFwJU2R0DtG21gY_DwLSLVFqn0eBqamwLRTd43GtOcaW5h-veZZTAMCa7bPxWi74ImNtG1j_ANuQutNTd4cofFPRWRJtFERDZrQB-61mZp5LgFgGeSBQSJQ0DwnLGsfu7ZvDs2RErCH6hscV8NNkce4It1yreF1AflZCjYFEVl4MAWgxMOzVBcHN6n9IGR8_bFeXL6VJ6uJzHKHzJYbGMPuJFpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ny10HEPGCrK1Hq9OiMxg4UK9D2zErLto_t4Vo0RPFIRpyEduYQiU3Hx5qNJD_-spPJB_DNYUAWu-JORy7oHVj1Rffl5D0PVMQ6AIndcFg1hpOXmJ34iKlwq5t9-TJjqPDNtLfS-5IsgzwBu7-CywFH9nScz_mMGj0MQEZNjJpexGPZQkihF61KepczyVFWWASsS_xK0JwcNvJbYLTh_gL8rLaOZT5-6UedIWz-o5qYXjlsmis3vybdypGHZZ7iXVqKOCzyWxX7S36jZsoSQZUypwNcN7_LFjRHB1kOELpU2SF2tAMXBr2PcAAd5Le6_dP3-vInHBPDy0VotGszY1Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ny10HEPGCrK1Hq9OiMxg4UK9D2zErLto_t4Vo0RPFIRpyEduYQiU3Hx5qNJD_-spPJB_DNYUAWu-JORy7oHVj1Rffl5D0PVMQ6AIndcFg1hpOXmJ34iKlwq5t9-TJjqPDNtLfS-5IsgzwBu7-CywFH9nScz_mMGj0MQEZNjJpexGPZQkihF61KepczyVFWWASsS_xK0JwcNvJbYLTh_gL8rLaOZT5-6UedIWz-o5qYXjlsmis3vybdypGHZZ7iXVqKOCzyWxX7S36jZsoSQZUypwNcN7_LFjRHB1kOELpU2SF2tAMXBr2PcAAd5Le6_dP3-vInHBPDy0VotGszY1Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ZgGCem3ftsBLyEHR97fzOP1iiAA16ZujkXXBB7CnAuLcdWqlIH9xT35HNVDxpYWKqQaDnySqodDhYz5GqWkTjhNkbDFQcHEUS6LfTBGva0wC1u_yZSG1dK-_rtbK_ZcSU1SdDh8rGZ1QvKOkTT8a9vh8CVV1u5wJ2eisYZSAC-OH6_3bJuds4fkXBjzSuBSpMPuDlvzavZSEfEU9XB0s7rXZ-WA0s7sP1e2RrsHQ2CJj0cp9Cm30V-wthZf_BXqesC2metF0aXXKHEJoF6dw23tdV_rb8JeTmkQyl-hhy-dDKDUMtjZmkHko88DBcLeQRfkSs5QdYW1hsp9eqCBvOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=ZgGCem3ftsBLyEHR97fzOP1iiAA16ZujkXXBB7CnAuLcdWqlIH9xT35HNVDxpYWKqQaDnySqodDhYz5GqWkTjhNkbDFQcHEUS6LfTBGva0wC1u_yZSG1dK-_rtbK_ZcSU1SdDh8rGZ1QvKOkTT8a9vh8CVV1u5wJ2eisYZSAC-OH6_3bJuds4fkXBjzSuBSpMPuDlvzavZSEfEU9XB0s7rXZ-WA0s7sP1e2RrsHQ2CJj0cp9Cm30V-wthZf_BXqesC2metF0aXXKHEJoF6dw23tdV_rb8JeTmkQyl-hhy-dDKDUMtjZmkHko88DBcLeQRfkSs5QdYW1hsp9eqCBvOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP9orfF-zKZ0I1JptXOaadk_Xpb7aucbbmwrf_SyJMabySM9mBks-ivHqfCl9pU-QkTz5GEU7MsS8K34NsDfzvNtaXxAV8SP97Mu9sBTleSo_libc6_KZCpsPRN5mIjeuffxNEknIyp5-42lh_fn8Y6VuCV61nr14c_WRcTebxrwDEgNBVsxjlZ9niYZ6EaVnnus3zP_PrPKzg_ktXLDmkmwLyYmaPS4ZY_bW8_Z9FJoE8LMU2tlJ5aRRwqJRcUWFVt9pR0iU-ljf0kBHBev5PCWpzthndSgnDaI0Mik-wAVlW6mkmWxdx13QJL2Z0CxHqUe4t2uRbL5a6vrDVwYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=HkNDvnyzih8zvTXrSK3gZVz-pwgBDriPuQL86VoSDODOqwsO_nVtfRbIvcVbcrkkxbIzYAMDDrVuiYL6vzHunIpqPUM5fArm41_P4t8_pBAFtnk1NCzKaqDbWonbDE81_gyb-QW98JRWjpzpgrj_Y0nD4ZgkrY3bJ3K8b5C6EnY0sgT-enFXmoMV6ax9ZZKu9iWJSnSubudlMB-p6jhoZmGH_imFiyDsJdLQClMTTAUywhJKzLd4ZxuRWLtYahzd_vwB9mQIot63trYirPDTvIet3PBVwTc3bd_IRQ8UBnFZdiJSKaPR0SZ1UIcvmdN_PG1xto5XtUXgYgdG5-HHCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=HkNDvnyzih8zvTXrSK3gZVz-pwgBDriPuQL86VoSDODOqwsO_nVtfRbIvcVbcrkkxbIzYAMDDrVuiYL6vzHunIpqPUM5fArm41_P4t8_pBAFtnk1NCzKaqDbWonbDE81_gyb-QW98JRWjpzpgrj_Y0nD4ZgkrY3bJ3K8b5C6EnY0sgT-enFXmoMV6ax9ZZKu9iWJSnSubudlMB-p6jhoZmGH_imFiyDsJdLQClMTTAUywhJKzLd4ZxuRWLtYahzd_vwB9mQIot63trYirPDTvIet3PBVwTc3bd_IRQ8UBnFZdiJSKaPR0SZ1UIcvmdN_PG1xto5XtUXgYgdG5-HHCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwduqALueRgep_Y9uRjoiaT0g01ld58sV6EnHIDU9at2l2BmGz2yK814huwMZ9YFsPv4u9mKobcvLDMMiKtn9o5ehvYTgA52iPxkDJky2ryk_FEpTF6W4VrcTGf4sVFAy44VKMURw8Oet8kDXUpagntK4_hSfAG9-ygYKKhz9y6vbm3jvIQQIA0kl97ZYKpMSWjhP7pjUMxfU_Bb1SOfMGzVZNILP36AFjThwYDP7sB4p6AFwvXAb3snEnIpq_nUKBh5rPf5c5dzj4MnXDr_gC8rKozoppzkC4ollpQmr5Sp3SE2f_9OEwfvmScaJ6gWCWB1D-QBTcZfTIJL13IanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=KBMrLfc6OxI_lC1E9PycuVzC9ZhlFvBi8CIvQXqugoX-Ltlq9CugK-Qi9g-owRN-GOxuR5PzIcX403JWGD6ddulEvRpeHIDfD1xLvWFezG-lfulHxzOjbyY2ZXcy51ELmuINI3xvKxRGfPY9suEZcliyq9VTFfIVEvCAIm3BIwxPq3Iwn-XXrzI0wd8r5JS1rBubJ6eRIdRY_x-8UUrc01-hDyQmbX5-npwiCgcc1dNX5nxCCAMu5XwUw88CGSmufSaYNJV53Tzsa4w2r4_HGEsvjIXaFMg0Y21XhgbseB80vl6tzGwyY-xRb00Tr5a60wEtILr0RDGhhfd6XiEUEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=KBMrLfc6OxI_lC1E9PycuVzC9ZhlFvBi8CIvQXqugoX-Ltlq9CugK-Qi9g-owRN-GOxuR5PzIcX403JWGD6ddulEvRpeHIDfD1xLvWFezG-lfulHxzOjbyY2ZXcy51ELmuINI3xvKxRGfPY9suEZcliyq9VTFfIVEvCAIm3BIwxPq3Iwn-XXrzI0wd8r5JS1rBubJ6eRIdRY_x-8UUrc01-hDyQmbX5-npwiCgcc1dNX5nxCCAMu5XwUw88CGSmufSaYNJV53Tzsa4w2r4_HGEsvjIXaFMg0Y21XhgbseB80vl6tzGwyY-xRb00Tr5a60wEtILr0RDGhhfd6XiEUEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LsBPIAAT9s_1PkGoqq-FqT7-FsY4t6Ael3KdAvHkwkTL7k7-xS25N00ZCPz6EkVg_SPRRIICATBrPJctPffbnVzVjIzhUyjcyN37o6IG_xVH3phfMQs5pEhFx9OqG9UhxdIr_7Xo2_pucrpK1pqpfuq6JolesITldNs2UNUqH28DtHLSwTYwnyfiEfAz5ONm07zOckSnhIsT0iJFSm0s3WW6PfArk36A6btoN6Bs9O9GhfU1dNusTFa1PcFcyAKshu66q5OtXsw5-TRVKx09wxH4OO2Sa_7UGwqC-gNVFKWdso1i7wbYdnHhaKIS-aJZ_expreuMx7xrLfGq4oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=bbTo_3eMGtCRsL-I3a5zMChh74FYhottzVQPoW7hCXdKeFUvBNZd9Awt_LC77bKo1LQ18ltkAE94iBc-dE6a-Myhvq0HTs6ymNsADuHWip8g5rbO4ndB8PGPizu1tzHFpAYiJCwmYGtfpbWROW6D9BoklIOUSIhtSNW_uya5itgk2wJmoqbs7jh-s_1JH2-c_N2_2tpe9i4R5nhmwMMBByEH9WF7dIZkg7lAZFiOIYS1XCSvIU3oU63dlDBmCaTHU2jwNpIbEn_wAWW6sS97NOZ29a-GIWB5mQ7RZZMWVEGamzYJFAu23Y9G1VmT4YWKIhVdn8w41_FtD2BW1R2wcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=bbTo_3eMGtCRsL-I3a5zMChh74FYhottzVQPoW7hCXdKeFUvBNZd9Awt_LC77bKo1LQ18ltkAE94iBc-dE6a-Myhvq0HTs6ymNsADuHWip8g5rbO4ndB8PGPizu1tzHFpAYiJCwmYGtfpbWROW6D9BoklIOUSIhtSNW_uya5itgk2wJmoqbs7jh-s_1JH2-c_N2_2tpe9i4R5nhmwMMBByEH9WF7dIZkg7lAZFiOIYS1XCSvIU3oU63dlDBmCaTHU2jwNpIbEn_wAWW6sS97NOZ29a-GIWB5mQ7RZZMWVEGamzYJFAu23Y9G1VmT4YWKIhVdn8w41_FtD2BW1R2wcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqonQc9nQVdMCu76y8iuX9HZ7Y7vMPBqg3UMDQnXtCQ1vPMO_fmy1xseRS5au0E0lBmKhdpDwbFxl8S8kxxNUFZjhneknUqKnp_XqV6tnEILa1GbqXVIehEvaj6Q8c3H6kN3325T6FxQNBWxkcwm_rglPa6EB-HLRanr8etH_cVWzrBJ5yG6_7YDxYwao5yOn9gEvjxYSL7gmaoaeornwplscRzi3w4HLUc07nrnvukBLR9ANnk5vznAZHRVvwyo_WvLHkKW9wFLKUSTJHrf0QH8Sw1bawMHFeKCnk6BIs8RXJSHPwVC3_XjOiCrY3BMEYpDseBJ5gjgMgwOX1VVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9l9q9FYPA6Tk86n0-s8UZ005o_rNjZ5T_syivXFp9D7LS3qbGO5iS3sgadn_67bd4gnD7fZtlMOI1SSdPz-44O9Ih5iAsMrBgYowHf5qnEEO7tkgggyCweaqRRTyL5CdFRAJ5fLvHoJT37jqONFHoD4uVcZyPkZd0gh8IkFliYXoHeBWvGA50sbncOb_q1BPcsdyKMSHAkbTomM44lqkYcqEOdEBkx_j8Gd6Zs9qfz6MsqRKn_8RSkW0_iPhhBBjNQrG0pVAewsiNcAHjH-C_tx2fGBLOdIc7NAxITpX2JbOTgoS5Nj21lEpk8lkfA3gTAs984c1u2NNchzc9xSsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=OHY0kmF7bvq63zYTxzA7u3Co6f-sxRN6dYrDBIaIZnIWwCpnt0vNfiX8V36Hi6UoSL60_fDYYMMdbUunesKJv2oDMKBCq4-X028sv2937dwONNkIopihZh25dKp4fB2_g971x8fKlVaPA3MazE0iO1666zZzSSHQnw4mI5CmJBAbNfLQOCfrSu-K8c4qtzZqDA3HzoJ6n1-MmVASmIdYJEkdcnuJ6_8MiTDYnOOZWfzNjRuLXNayftQESDhTekERKtWCz_k1CrBTBqvuQA8Hm9PYuCG65iUhsVJGoftKF96ljxv8jMblE0UyJBmkb6yDN8agPKB7QgVkY-hW9oDAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=OHY0kmF7bvq63zYTxzA7u3Co6f-sxRN6dYrDBIaIZnIWwCpnt0vNfiX8V36Hi6UoSL60_fDYYMMdbUunesKJv2oDMKBCq4-X028sv2937dwONNkIopihZh25dKp4fB2_g971x8fKlVaPA3MazE0iO1666zZzSSHQnw4mI5CmJBAbNfLQOCfrSu-K8c4qtzZqDA3HzoJ6n1-MmVASmIdYJEkdcnuJ6_8MiTDYnOOZWfzNjRuLXNayftQESDhTekERKtWCz_k1CrBTBqvuQA8Hm9PYuCG65iUhsVJGoftKF96ljxv8jMblE0UyJBmkb6yDN8agPKB7QgVkY-hW9oDAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_DiZNTOq95aM_OceNTV6UEPbDT1GXA6jXPih3nDenIC1dVho2V3Ty-0xEV5eJLG17slNJ9g3UkZG5yRj6ZJAxNzRoCXh3D54KfPvg2R9LcGxoB7ZyIEtpPB0pDuzbvE6hfP96cgBmfSXg7e8f9pzxO17xngmGwyblNY3Z67uGvlH4ZKHIzQ2HW8nF1LaXBtS3eZZPec0xYDZGHIaPGUDQZMoVYpBzHYmQPguODpcixJHNFzcwCuRW4krQRlw5aiIeCDfM9AqJR0LRu8pwTKNdccCcY9btJtHlc2qgHNEv-N1gnP4G7xdhQttKUUOtZMkDZAMyfph8gwh7bglDUJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlskpCJAniLmwS9FOp9wRBjCtnap3pMsQfWo9U4MxHBXO9tt7nAr97qGm7CdEfQL8O3rugzyQVjWgQk4KmXBYPMKyxpJavkoOoVlfTK5Ss90DPDRKI_1J6UMTDnCT7DB9OIlnvZtVJsNGKLM6wJiImmOTi1ZTjAVPPrUoT6zY0TFzwOTYIoJKZYubXmbdCJrB9abGIsSGysC4R0QCNIxg6-3lmi59Uxy3S1-ywvGWdEu2Ux-Cjkz8Zafie5DH5lTraepRluYVn9R6tke_23pdMw3rfcQprKR86aJ_JS4aA2OTrWAFaQBY1Nh7KiuQ0nhKJG1-NI-ze6F8UZFPcotAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQF5c7MdWRLLeudC7ZGb-l1H3cnNM-bqgTj0mev18zmanJiUJHMTuapaYRD6YguviMxTMd8EuoICT4sdb5sqLf2-E-JQr1wUQKg8WTAOqyeArAXBVV_OJCqStk8m1HbYq3Pas_wKyxVQ3nCZ6ja8euV4N3-iuMn7Dm3pyJHGNgI7pgoIz8WRg97smjx5e2M2rlgu-nWmRscSySz-P57Tuc6_wAFmFC_l5NhB7Ghff5JVk0rL6kYDfxMdYdMCSCu5J6qr7uW2kejCKK1OgIq7HmtY6UUy_8MxENk2pb-IFpttMQnGMBSBFEqRCHfz89ggt349gNyn4mEGt3NmO-Q3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr2bdPf2myrgttaA3xucuSmDKzD3gb2ggDot4TDee4xCc52sm0oDwC2iZJBizuZbuSHETgr4nz4NYrVAw1HVJ-DZrG6OUcQfqoOaAULxsozyPZ77iRmcnOsctM7q4LoSbH7YwEf_y6pWJu2ajXTk8WLCGAk7Zaql2PvKsr255z7mjBCVaxxfroYcaaNFB1d1VM5XRh-tvA6fXiaGAtBK4wWTyDouyzbphovm-Q07cueUa1N86DUFbuGLDe5G_7HiqsmyRPkqlH58-7a8phsBCvdFcBlnez99M5lt-2O0UclgPVegu3pwKc5b7EMsn1et1Q9n-rCwtT79H_M29tg0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlNwiInRzSlcMrn3sjgW6s9GWqXO2ZKZ-oxJ0bTlM-VAC2F_B5l_YO5IuAZO-Phigiy4wN9EowJOqX2-bi9SpE7RfJsHAuBTBsXtI1QSCWCMzeDpRbYlC4Fi-I2TIzrvfdoN7bWDgP0SJTcznYUdY2fmGUDjszi86kbdtnfAzAFDw1tJH1_6TD8vDGGpXy0EoWsN_2U85dUW32I9fk4nBfF-QHc4yqUgDuQSDkDOwy1IRBYU1CpEdBy4g_lqlTKfZ4nkVgbbj35fQ4eb9uQJlT8IXah99EInTMlGPm7Kas4r1RPhJjG4-moA10gHtvSo2C3L87Ueb4YUGc8-8-NIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=dLevGAThcslnx9jVJGBqJvpoH4G0NdnvtQZHNwXHT474W77O5ITG2NN-HOARh-YI3hXyX9ld8iaigN5QP8EN5HLjAo6jREZaBESNDLxcU6JMJ7TwZv9GU5rJovJ3VSVcqijwzGJwfhWxzv4fm9Y8YRQwp30dfX6JubEFXk-cTVE9a65NxnQGWCHDmMQmRj0QzjlbeSNQHt16_mnakwWo9MCurPEa6XR8Ki08CBzweXUKCVpSnIYJUOFVEAJygulAWZcDmK7N_kGclsxGP4YTP_9lH_KPusSeNc0IVYDu5WSeOJ0XYiQHwryJfpZvynMrCT5Yc9rHtmcFRLuLpmzFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=dLevGAThcslnx9jVJGBqJvpoH4G0NdnvtQZHNwXHT474W77O5ITG2NN-HOARh-YI3hXyX9ld8iaigN5QP8EN5HLjAo6jREZaBESNDLxcU6JMJ7TwZv9GU5rJovJ3VSVcqijwzGJwfhWxzv4fm9Y8YRQwp30dfX6JubEFXk-cTVE9a65NxnQGWCHDmMQmRj0QzjlbeSNQHt16_mnakwWo9MCurPEa6XR8Ki08CBzweXUKCVpSnIYJUOFVEAJygulAWZcDmK7N_kGclsxGP4YTP_9lH_KPusSeNc0IVYDu5WSeOJ0XYiQHwryJfpZvynMrCT5Yc9rHtmcFRLuLpmzFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=pC0sgjUR6_hJBblFtG-1xUSngHRhfLPKp_XQJ17LeETDlXYCNvw3armXsXGHhZ14ysgVxH39YPskpPKFhGLBO_AX2rVM7DEkga6WZuwBwEXZoj87ItTjV7kAvQnNDnC6MxccYVt2NM8XIlsggy5-C0W_DmUnmYMECzrPQ4sLoqSB9PbQTIeknGuZOulUUndZk7g_Oq35gEB52fZb8diDdeIKBTjwYDF3taq2bGK95iDogFeqTuS2SwygLy84thuUg0l5VLIuXnHGU4qaRF_Gl1pkOKW7v_dTU5XuGmBvSDcw38GWj8yia_YA4FlF48PVyRVpPVnjA83oGguRRcW6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=pC0sgjUR6_hJBblFtG-1xUSngHRhfLPKp_XQJ17LeETDlXYCNvw3armXsXGHhZ14ysgVxH39YPskpPKFhGLBO_AX2rVM7DEkga6WZuwBwEXZoj87ItTjV7kAvQnNDnC6MxccYVt2NM8XIlsggy5-C0W_DmUnmYMECzrPQ4sLoqSB9PbQTIeknGuZOulUUndZk7g_Oq35gEB52fZb8diDdeIKBTjwYDF3taq2bGK95iDogFeqTuS2SwygLy84thuUg0l5VLIuXnHGU4qaRF_Gl1pkOKW7v_dTU5XuGmBvSDcw38GWj8yia_YA4FlF48PVyRVpPVnjA83oGguRRcW6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=k2xSfgT2BBXDqVdNxjcR0BPDbyaw9hZ_oT7iKAcWYz8INSGDUxoMPGaqhpfi5hZApKBob9bgK8ICEfdPcvESM3B8wjnijzyqnn-m73qFXrQTrAPvCGpnoseeNtP2nl-KM3K4AxoTYiqK72xTndqsE8nNUs8HUJIb_jhDrAnbyT9S61KMFuq6SopGj8VbbdHNU08dZaTqyhomfP8gZMIKg2kdKgWwww_6raujdxu0U6ofvBLqXwnzqLXTtqSXJAxPsMEhV9getHEHrS4MC28wI7jKhnlv-OUe-ZvpzMRjn3FL7u7NPAidolO0ovKscBwxMSTYXJPiYeYHvAwkKRzy-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=k2xSfgT2BBXDqVdNxjcR0BPDbyaw9hZ_oT7iKAcWYz8INSGDUxoMPGaqhpfi5hZApKBob9bgK8ICEfdPcvESM3B8wjnijzyqnn-m73qFXrQTrAPvCGpnoseeNtP2nl-KM3K4AxoTYiqK72xTndqsE8nNUs8HUJIb_jhDrAnbyT9S61KMFuq6SopGj8VbbdHNU08dZaTqyhomfP8gZMIKg2kdKgWwww_6raujdxu0U6ofvBLqXwnzqLXTtqSXJAxPsMEhV9getHEHrS4MC28wI7jKhnlv-OUe-ZvpzMRjn3FL7u7NPAidolO0ovKscBwxMSTYXJPiYeYHvAwkKRzy-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=HE8kPXG9Ooh2Hho9foHTUb4EGdF7kTt8bcF3u9g7MAk_1syWvJF57zf1gxdSLzmQUMO4fFsUBzLtpGIdUX3o-X_gh7-tHHo8D6M9YJtcPYHZ6Tb2FTHe3h45oxs15AkAq_f9yyTeziCxTLs2jKp_LVvsHz78adsV-584H3u6k4-VFjjcloSXMNAXZ8fFzMQRD8q5yHpZdWOVhN1B8DEL9bS9K91WpcwlYpX_FJ5w8ShZUN-prc4OX-VJJ2Bf1VooHVH8KkUvgv_m0nYz_0cWWhsdyioZEtaU1OjdeSDwAew0Qdnp4Y_sR-rnjhxIRCLYjdIymVFaIjYPgzi_cEhAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=HE8kPXG9Ooh2Hho9foHTUb4EGdF7kTt8bcF3u9g7MAk_1syWvJF57zf1gxdSLzmQUMO4fFsUBzLtpGIdUX3o-X_gh7-tHHo8D6M9YJtcPYHZ6Tb2FTHe3h45oxs15AkAq_f9yyTeziCxTLs2jKp_LVvsHz78adsV-584H3u6k4-VFjjcloSXMNAXZ8fFzMQRD8q5yHpZdWOVhN1B8DEL9bS9K91WpcwlYpX_FJ5w8ShZUN-prc4OX-VJJ2Bf1VooHVH8KkUvgv_m0nYz_0cWWhsdyioZEtaU1OjdeSDwAew0Qdnp4Y_sR-rnjhxIRCLYjdIymVFaIjYPgzi_cEhAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jafZGe1at3u4GqTBJB_kSyts9sKoVTyYM3Pt_8ksMmPEF19pyEWWHrl2ggD-HByykILi6ZXxl7HX9e6yuO3TORMpnVWXRkR4t-Pu603xOE3mfI2_rNZyvpARP1DUFeG_PeU5_6vmTNgMFWu8PPM9LZ2OylDQXkSpg-Ts-TRrN3nZ8RAxjNHa0Iy4NPud_WJgpqmytOeVcCT0U9TXNDH4jT-N9ZWteBYr6tF-l1FwmLZMETrHoxJtyw-2VfB_vaOaAq2cCQ899YlLjFLvZJg_-ypcqPJz_aPKanE-3V3qDT7sAuP7F3MjFbioU5p_mFbPvJipdrrsGJC5__UuLW4akw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsSFlizNo5SXL4rSz1qZuqFZo4XWPVO7Dcy-ofcWV3Op0HJtw9_umw-revfv3MoCoiLNT0TdmZz2JlKSP10DYUu6v-gq5S2-7gduQR--giJ7NvWlxPEsIHQV3uZc8hBSGcwsuUr0SyzoxvMMUC53cmZcaDfV_BPWwRBqcU8SbjfNP2nidxuyK7DJAa1gmI-ntabNupGMSbpvpW5iScJdQCNcVgpR25XIrGIp5LCUdKDZLdc5j2FN3jTuoPvr-XwgUvk9dHHKpWnO93RkOWnh9yxEpIEN2YfgfEjyq_Gs2Q0MeBM2FstbL6nDIt23v47d1729O5N3uAMlXDilnhS-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Y2fy3BO8TeqrvQi3MftzFyVTnpn10FtXM2rUhH6ntrAR-l-WzW7UBDOvMcv4W43i5GhtXY6Yi7DNrw9IuzjvOxnJa0avE9OpLjEAUtG31aghseMmO52l1ZwVu5NHy5rZZ9oNg43Lb9WO5QsDP4pJZK93bd2YloTvxRGPkowdDU9BbzakxWXDHFd84ecsYiRYz39y0NKg5Wdy9-ZpnAXQDiHqT0wZpF3hlpw9UYBKt0hGxdWl3R5AyxnE66GD5Oq5qCDP93A3KHgDaBztydkmJUrdKft6--8ODlPhe8d5vm-qXLFhaeP1AdzW1DrrpCMSJEHeL3IibgHYogNFpMOoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Y2fy3BO8TeqrvQi3MftzFyVTnpn10FtXM2rUhH6ntrAR-l-WzW7UBDOvMcv4W43i5GhtXY6Yi7DNrw9IuzjvOxnJa0avE9OpLjEAUtG31aghseMmO52l1ZwVu5NHy5rZZ9oNg43Lb9WO5QsDP4pJZK93bd2YloTvxRGPkowdDU9BbzakxWXDHFd84ecsYiRYz39y0NKg5Wdy9-ZpnAXQDiHqT0wZpF3hlpw9UYBKt0hGxdWl3R5AyxnE66GD5Oq5qCDP93A3KHgDaBztydkmJUrdKft6--8ODlPhe8d5vm-qXLFhaeP1AdzW1DrrpCMSJEHeL3IibgHYogNFpMOoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyZ8jHWnyH2Ep9Gx_0mbVI9YZnfvMk0aHbAZSfKiVWzFCRb3yLHZ3kEdjrRzGlo0xsAW0lqNTN8gZluh3wOrkjmodRaEIeTiVbxnIyWJ7MpIQqAzDVkfisq9A-lkvlHfqQLO62Mv4Ks-RcdyEKJSpP00sVCv5ZPSBe30nJwI9N6km0ie34EoQ9TxuR9hAm2OUbbbU8XV9zGBPMQUqnngLdMyHP171qCijuJKqxhkM6OqkbMh_enfqMAXCBOFMdCcp5wpXBDRJ38njN9h5iu98wm28AO11i4w5Z-hZc2dhFsyCN2T7BVsnZJFRi1OgjIA-iaLlHW5NOdSPvjHZyHvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eS0MZ9QOIdMkSpc_FoPQgzrinq0exCGYVWiryoDacWJPcqZL-pQk8qBgt36NpJEM2BZ3f7wPbjYqWGkZWu2qQHrN_99v3UVL9BSOvG3BvqSJszZPl7xmXIXfoQ97ohPWbbcxs8ldhhWR1rywq4gmMKwutgUzuKGVVXPiuZaSEvd_gtiNwqt7SC0c3MgLgQdPqyp_TKNQ7Xk94xBf_mo2oBqnMQ5DIx7g5W-JwRS7MRTrDF5pwF4DRNCKqOnFdhya7EkAES_Kw5O26xAcMVGSDVJJ4enggsE0TFXHSTk1fe0hybj69fWD66c5zxuR9OeF1ek0RQkU8AG2jZCEs0auFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=eS0MZ9QOIdMkSpc_FoPQgzrinq0exCGYVWiryoDacWJPcqZL-pQk8qBgt36NpJEM2BZ3f7wPbjYqWGkZWu2qQHrN_99v3UVL9BSOvG3BvqSJszZPl7xmXIXfoQ97ohPWbbcxs8ldhhWR1rywq4gmMKwutgUzuKGVVXPiuZaSEvd_gtiNwqt7SC0c3MgLgQdPqyp_TKNQ7Xk94xBf_mo2oBqnMQ5DIx7g5W-JwRS7MRTrDF5pwF4DRNCKqOnFdhya7EkAES_Kw5O26xAcMVGSDVJJ4enggsE0TFXHSTk1fe0hybj69fWD66c5zxuR9OeF1ek0RQkU8AG2jZCEs0auFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXSZAa4nCSqT2oKyMItSKmnGfdg1oI9sT0606aLFvQPBKNjszzfInMXWkAg9JjqRdaIuzDanIppOSFbgAUq2Iv8r2lCO3oooEl3IBtdhipfbllB3lvLMmwWAFhifDHf-iNW3_Oarpf0UzVRehrZKULPLx01MbnqJ7SRurv8rsYcRTU_18WSM-HCN3WZ1mJZPXSPEfNqZVUr3cbvnxvJiUrpaIz2mwOOMseXAClMibBi5L8V_-wFEo8vic-OFe2vdcAQynumXuW49adUCYZvKVFGY08LN4g2yi-nFZXKoXGGm8bCgmKIqDhUb8qy8fd-qBjFO63PpmdCUZIjXI_5Gcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSDDLTV3cDa6U5GPRng8Jfw9aLQK44I484IOyDFK3EUG6k_I1UHkvHaDsfAu49eqAw8hJS-5gQT7tPI4UZOuMV6lx1kiRm1kNxJTmqxj2x9XDuu1fQ6PcQnNZrC9i2vnjEv4TwLZKFwgHMB_4JHNAMlusc0_Xv3uuUIfd7c-p3aoqA6_2x4P-PVyrRMothryj8NpLHGfE0qJ0PtSxm4eFc5Xc7KnD_NGEqVPlwoKhEBHZyQhdLXdsMIrkekhyiYScflPcK_MKfhDLCBHMRFdrOSFbJfbLUDYYcp1eOif-nzfFocVLWUdKteY4yvIBKiUR7uv4X32aVZL4l2Ag6gb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=jonyBvqM-s7jlCYmlowYztYauMict9VvgCanGOiQBXbswpESHGrOnc1rxLy4wPwUYj2TzCTK1ZU6SpQIuHe18fEZ__n2cHIl-KHA7mhFXMMsPNg3_rFzEG9n3Ofn6i_yQSTBzvVgIgLiFEQAFZWNdyJYGO9vfwtdKogIpD3itDEnTumdQln6n2voSUnebR-zffxJoWYJDnGWWRGNfIUaA9od2xGqw9zjSigY2XOBwCAtcjpLt1-7lFwlZL4UENeEVRZD-Zh0jQnZa39N0ugJ-UN5dn869y4Z2UtMXU-MCf_6dxMveV-mmt1vJyoJZnwcK-pSLkP4NI3-Okh3Gmtlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=jonyBvqM-s7jlCYmlowYztYauMict9VvgCanGOiQBXbswpESHGrOnc1rxLy4wPwUYj2TzCTK1ZU6SpQIuHe18fEZ__n2cHIl-KHA7mhFXMMsPNg3_rFzEG9n3Ofn6i_yQSTBzvVgIgLiFEQAFZWNdyJYGO9vfwtdKogIpD3itDEnTumdQln6n2voSUnebR-zffxJoWYJDnGWWRGNfIUaA9od2xGqw9zjSigY2XOBwCAtcjpLt1-7lFwlZL4UENeEVRZD-Zh0jQnZa39N0ugJ-UN5dn869y4Z2UtMXU-MCf_6dxMveV-mmt1vJyoJZnwcK-pSLkP4NI3-Okh3Gmtlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=GjqgCpmWl2PMyTerH8wWJyEG3YhvFQmzwQI9fULvCKoy7PLThmFIovDDkRyKOILHjv3mSQz5Npzwht-j0hFHIxwJd4OeOkvvf1LxxigARrCBpegEJWdYy2oL38u7gAa25BV2OstgXhfuiXONVdtrqMG-62tNmcVJVWVKLSvf4kWLEz-dEMgQXJkG72nzE5w2iVic_9sceez8f_PdJZfzzIG9oeSthM7aNxmDXgLPkfxXS_RaguTrG3LiV_KIV1FN1CyX_DV4uHIM__4H7MK1V7pcU82xrmXR-HTnNpN99DS0upWh4k-6lgBlHIHqe8DiWME0wiOG2dnkjajc09b83g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=GjqgCpmWl2PMyTerH8wWJyEG3YhvFQmzwQI9fULvCKoy7PLThmFIovDDkRyKOILHjv3mSQz5Npzwht-j0hFHIxwJd4OeOkvvf1LxxigARrCBpegEJWdYy2oL38u7gAa25BV2OstgXhfuiXONVdtrqMG-62tNmcVJVWVKLSvf4kWLEz-dEMgQXJkG72nzE5w2iVic_9sceez8f_PdJZfzzIG9oeSthM7aNxmDXgLPkfxXS_RaguTrG3LiV_KIV1FN1CyX_DV4uHIM__4H7MK1V7pcU82xrmXR-HTnNpN99DS0upWh4k-6lgBlHIHqe8DiWME0wiOG2dnkjajc09b83g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amX1YaxQoLYJr7XKkShVu58AZIvb9FGl9cVQVGCjITtJZH-5GVd2oY36Cp58L6P7U-4Cp7_Kf_BPNNBZK9F54mQFk-XAJA47cYsxXn9rY_8MYB4awZwrtl9iidihoT9J0_F5q-otIu2AL9eEeMBwcszuXOyawW6CANW9Q3ayNDYBjoZ-gYk1fN2sRi7PZu1vuZNMAUaQwolxm5_JBdgzWb9Jsqsg9OffQzdm__qlUPISPiHCwqvTTFiFpi2EqFovCGFbgKb5ImOuj3IxWvsl3ypJb1s0wat87xnX9Xp-5o63oIVwfaQBxQV60kPntYgTV_E5EnDodlvWJVwjSg6woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1Y1ZjGC5-2q4E_aOfvHAnVczHfvzCa0OPAc-hFnL6x3ZsvxkdpXMXIarMvyc5CBw8fNReJaBesXScTqHSE2MDyeAXGddt1tVM6m_7CwHyZ-9S_fmJvlqsHOHKlIHXRlu83fqKtfqscyBuYtYtXZw9wkmDw4QuoBU9HCvjyKScPCMRRgfsFTMlcFDfnfz3slcI5HZxx_ruhyHk3aF68ZEKY1UtCLVG5t8bJY1yAxMvIy1Y9wltfAfkHwP6xh0TWNG7rRWO2dqAjsgAFsjRkX2GTaA1tSVFJAflZkfVQyxGTHH-KssesIPdT6rulophqfIuD5IxAwhg_96AUKdHqQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpiYXLtI0IEienKthCnkt_q0d62hLxsGTUvPdTvuJJCP6s9VGKfT3N2X8SEkAW4bQdbbGvXgrDqnuKUV3YMi3A_Omocan5wIlHv2xIlqfb5mWtUysVcve31I-cGYEf909QykObXo4um-61wnudjdj1YK4nCg42JlDKT6bRTg73KcMV4nvS44cqt_J-fJXMxiOMHdr7mFMR8xs5Sqiu-eM4Uu9VQCoAh5O3jzTNnR6m3B-z7hM3ZObx8SPmXe3zXSU9TojylDLMIroySuEdAeGzykbges4hcPJe08zhWS0Wmx-WyI2sQr43_lFniDSIAX-7a9_Mm-QZpEdhlYD2x3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=T42EmHk6D8CBnr-gD_d0i4Au92siYbONvTMJATaShsoGPY91xloOlgahkFveawfUJuwRBuF7-vLUxOS264RCvVCyxiKyvlN9Ktb4vivqe22wWBHrwWoudwC3V8YvIKKaTkqeDmfMaEof2dYhUZ0A7LBhHsm0u-hd19g612ZuVdhAO5UEkB3Ey-rDM_53LbxoBdqwuWi59835LYYXbk4y9KAztsLYmzdrIZIaEcWjYTtM73Ap1Z6tpEnFV3bjhpr7ncd9D2ZuPCLCm2qpbr85cW4H-8ENFCpBoQTRVL2rTCoq9IxExyB9RyFbrxNgWCHbtlVWowgkSKHcJwzsmT8WIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=T42EmHk6D8CBnr-gD_d0i4Au92siYbONvTMJATaShsoGPY91xloOlgahkFveawfUJuwRBuF7-vLUxOS264RCvVCyxiKyvlN9Ktb4vivqe22wWBHrwWoudwC3V8YvIKKaTkqeDmfMaEof2dYhUZ0A7LBhHsm0u-hd19g612ZuVdhAO5UEkB3Ey-rDM_53LbxoBdqwuWi59835LYYXbk4y9KAztsLYmzdrIZIaEcWjYTtM73Ap1Z6tpEnFV3bjhpr7ncd9D2ZuPCLCm2qpbr85cW4H-8ENFCpBoQTRVL2rTCoq9IxExyB9RyFbrxNgWCHbtlVWowgkSKHcJwzsmT8WIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZWWDYlJ9r0682dKSFr3RwHqnfkaWm-VksJbYzL9dEcjg8iBWRTLm0Zp9yFF3oZiXVtbzpZR8tth_YXN58vKpH_EVP5EQTAB3puPw4jMmatZmI1L9RMRB0Vs5ZXNdMdMwSVePt_nbioEOVBq8a643ak14PDHkvjqBlClnnDrOA0sa9_Cz5hhDT8E0ERDqBX-3Na2fyqp5DEeKivV709gkNs7VeyRdf9QlrlmmkHmkYqgH3G8dYxxFcQ1v5CBSoFNy4jAtMu20KWg8H84jQYZ2sApXyKp_kopkilDWOr8AafdgPlKHBwRpVutgtGwL1IQrsrsXMDB8lOJm6DS3-qgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2C8twYvWwlbA7JL0y3X4btO-9CbEl8XpP3j9rdxNNCbHAoUve_a9b7D3bn8ZKdk-3N3Spr33JKQrCoI_JJ22DoexHUe1NHKWu8xl-_P0MPq-aK8hLkY2zRe2Dytc06i-63uQIe3yuYTMIfkJ_ALk6CSeA0SW0DHAKJR6Sy5hHsa8mI5NC8wyTApggzs_GFKLqzaNMvRlUpjbrPeulQitgixnrXj2sgvvqW18pa5UV8ORNOaAb8lWl1uG6EEB86EkY6Q4ynfXAKx5kH-Pj2U1l-DTJeWqW7rLYWQAVS0id1pJZkU27Ak8ut_huBAkOez59SjtJwIQYivZt2cVdHoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ROjerMG7ocF-nun4BIBHSNsToxuSH6lmlQd4G1srZZnhacHcDhE9lGAm41EfdYTP6tV3X7O3W_X0zu8Boy6OjwFwPTbjcWZigLj-lTfiAkJtcl55d-Qj-hemvNemILjN1fC8z744YNh5RY-CI75Npfc9TnZL3NKwqk4ZDpj6tRAZBMs8_fuS5tuivvwMfcgAID3XNonF_KiFI3GKMNI5rNs7Ly5idFMhrJr4DURxqGM7P02C1QUpNOzmW9Oxw0_lU3tppGPi5uf9NUlq1mim_omIIijcnCQGvsjNePMAlaF7qjkXOXDWwFZhA50XwCjWf9_J4d-049U6I45xoXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_cjvWLx23ktdgYXSI7qEiQLHPjBSeFbOAMrGGRVJAYPKKl2xBOq9vWBJNVUqA0e0Iypw8wuybbY9VdLwgRNvZpMmR9fBCvlDW5Yet5LuL32rFQYTu9rk_jsP1Fj_0eZ38VjwWmRH1lBNnspNHfTqh6tmgi9ao4JcJxJDJXB487T5e-51J6cK5zGxJNdmxvXH6MQBc_fLgugFgK3FWSb0Vm9e-0XurA5ppZw62ucfmeF6iMS3e6ydgSmI4wIbJyn0FQlje_ARFRC4PujRG61Fmy1evmsXlVtqsO-KiWo0fpChDmcl_JcZOJvAq0abIejNtXWkdfzYgEwtBDPpznQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=TeNr-3-FFrKcY9tXRJPtvhYH2KVZu2HLPPq6Nudgq8QIa2YuWKiyX7cb-is6avKnK7HVHltQNovkJdvU8j6DS7mhqC4_iWfOjBAOv7Qj71s4vgp7FEiHrKu4jwOvL8Ye0_CqIR2aB94Ot8WaBdaqxJdQC37gtiEmh61I-bus7epKIarN93_AIt7EARbRh1O1m3dlRhwPO9YbzUyXnr81vTHaR77POfP7bFXMUMBrnIe_u62yMudoX680Djpn5d2wEWHj84oDfNLHgy0-pQCX0tgbJ3GbmTh1JksWNDT_6mx6HDPmt0OUd0_MgsmhOuSOzmfZJ6VUGO4pMb_0RFeBng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=TeNr-3-FFrKcY9tXRJPtvhYH2KVZu2HLPPq6Nudgq8QIa2YuWKiyX7cb-is6avKnK7HVHltQNovkJdvU8j6DS7mhqC4_iWfOjBAOv7Qj71s4vgp7FEiHrKu4jwOvL8Ye0_CqIR2aB94Ot8WaBdaqxJdQC37gtiEmh61I-bus7epKIarN93_AIt7EARbRh1O1m3dlRhwPO9YbzUyXnr81vTHaR77POfP7bFXMUMBrnIe_u62yMudoX680Djpn5d2wEWHj84oDfNLHgy0-pQCX0tgbJ3GbmTh1JksWNDT_6mx6HDPmt0OUd0_MgsmhOuSOzmfZJ6VUGO4pMb_0RFeBng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJPXr9PF6lbmtDfCvTKP-ChzEyq7ipuCWzOL3yY9PrdbOyBPU--6qMLW0O6EMpTKgitgcYIAS_5ALojgwfPrKeGNHoB-BMw-rgPYy8-4ocsBfKTSnNlkKvHlZrzS18_P0NLw3kJpTOEh9cQy_-ZETZQgqzuIMcwWJbrFgySgF4ccq_-Km1q6vcinc24V6yiSGnqv2PuflVlP2ibUXKSbAbXAV-0tQEqo-Y5QjjoyoV5i9dp4O3EKT3cLGqzh2YGS9oTq81zcE-bmfXaFpWbGwgU2fCRiPvQzjDJ0jchZJrkiv5llUQYJ1TwXLFjztskyYs68wxxsMKrtN2UsifpHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=XBGGtCFycYL0tG1ndZ-FV_ZqnM0Xqg1DWKybGM92niYkeBUyhq9hypigQIB5KJOiSkgMsxRj_IGWTIoIwZlU52Lsz9vhBWPqsAMAAyBUDTNocW6jb9CbcBS2Va729MQtD9ol5Igy1cZv-PFOxNHg4-kvU1MOehsI5ASWThHM7L8fJQtfE6nifNOfoCATgU4Ei50WGJYHEs6RmuSLBHsXGJFFTbCZtFZvTsXxvC65Iy2kctedybFQmaghncfvq4C25agEbEu7ZxqqtTHuecyfNGzjYgj7VoJ0gZ7yiJ-wLb1xnV2EczPTPq_xyxUXomMV_TahcaLQAqzqX5O98j5ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=XBGGtCFycYL0tG1ndZ-FV_ZqnM0Xqg1DWKybGM92niYkeBUyhq9hypigQIB5KJOiSkgMsxRj_IGWTIoIwZlU52Lsz9vhBWPqsAMAAyBUDTNocW6jb9CbcBS2Va729MQtD9ol5Igy1cZv-PFOxNHg4-kvU1MOehsI5ASWThHM7L8fJQtfE6nifNOfoCATgU4Ei50WGJYHEs6RmuSLBHsXGJFFTbCZtFZvTsXxvC65Iy2kctedybFQmaghncfvq4C25agEbEu7ZxqqtTHuecyfNGzjYgj7VoJ0gZ7yiJ-wLb1xnV2EczPTPq_xyxUXomMV_TahcaLQAqzqX5O98j5ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=FeBtsmBVS6XMZcGg0_gu5Axp9QzxJ158cZ0nP_Y6bMbMzo6EzcE1ECTzHYl9nX6O0xXtz4ybczitdIFQPMaMJsgeJafPjqc-z4S7ZiKItnOUhu0BAI_S3rymeWfi8GPJ6BQbeoN5bX3bI8ugGkUge70fAnrfOj-PcWOy3Qe4WN3fSnkTJW5MAj9xLz3KiX8gCtnSNpIctgTQ8X6STFxJWSbl7YrDS5ozqX8nhkOISuEK1UavnwdK3M-O5tkZm_FXmVwXL9505Nl4ps6iFRyuiWDMrpSRIr4stv_e4H0N2Fas16XWt2vyF36EWS-59GSKkDsVKjq1T1dQCHm1e_pmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=FeBtsmBVS6XMZcGg0_gu5Axp9QzxJ158cZ0nP_Y6bMbMzo6EzcE1ECTzHYl9nX6O0xXtz4ybczitdIFQPMaMJsgeJafPjqc-z4S7ZiKItnOUhu0BAI_S3rymeWfi8GPJ6BQbeoN5bX3bI8ugGkUge70fAnrfOj-PcWOy3Qe4WN3fSnkTJW5MAj9xLz3KiX8gCtnSNpIctgTQ8X6STFxJWSbl7YrDS5ozqX8nhkOISuEK1UavnwdK3M-O5tkZm_FXmVwXL9505Nl4ps6iFRyuiWDMrpSRIr4stv_e4H0N2Fas16XWt2vyF36EWS-59GSKkDsVKjq1T1dQCHm1e_pmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUwy9yI-jd879smatIMKIzxTTZPzLKZowIGxQal7_hBi_T97j2VQRp8GTRKG2pD8tDiBedl50t_qWO6ap0gBtXuT_47gzUTRQikVMwlpqfw2LRMygAdDWelBf5We6sOtROxx-qrGDtXupTwIOiY3vhQkqPbaMLF_K6wj_3pNmdCie2fsnQy_prITNcXfaZ6RhJGXaNWqeSTuX94AX8Y0ExB3eyJ2uHt4U2Jb3MgotJVdEk381XJyHSjflqD9RzPn5JDayODGxp1PJrRxFOQtziLODlbU36YsaEJjBmO4lyDYrDqOYf-o7lAJHGaHjdu5m-9LRsgyJbK79FT0AWgckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=qgGQyBWy8nCyv7bguTREdeAPX6iDpJgQo_j3illghNSOc-EYi6FiPtAavKKsm5PCYb3okstuC6sJWFIlA1H7M66CG3OdSwZNjgzy6bjhEfpo2w3flh0zCcdfo3gqBR7xU6IQQrUJ84Xdz3d9B5smheeBJELmUxVKBtEaVKn8NABGZhbeLQzFxQ3oH8Sb0X5XdMQp2siFxzLalfAgFsRJrFLFTqiHTatw9O1xk49MkdxxUVRtD905fNGotAyo6qYnIR1a67R27SnChRUIZyQOUJl7mzbgBz_3svRT0ijn_QRvA6ZW8F65Ps2g4BPHGMpuTC-gV_hfVTa8tvA-jLSTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=qgGQyBWy8nCyv7bguTREdeAPX6iDpJgQo_j3illghNSOc-EYi6FiPtAavKKsm5PCYb3okstuC6sJWFIlA1H7M66CG3OdSwZNjgzy6bjhEfpo2w3flh0zCcdfo3gqBR7xU6IQQrUJ84Xdz3d9B5smheeBJELmUxVKBtEaVKn8NABGZhbeLQzFxQ3oH8Sb0X5XdMQp2siFxzLalfAgFsRJrFLFTqiHTatw9O1xk49MkdxxUVRtD905fNGotAyo6qYnIR1a67R27SnChRUIZyQOUJl7mzbgBz_3svRT0ijn_QRvA6ZW8F65Ps2g4BPHGMpuTC-gV_hfVTa8tvA-jLSTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Twk1OAICpD_cnlzDyuaPjbx1P31xD7lU6tBvfaa53MZNTwwXJ9Fa3eqDeJllo9bpy_hPCNE3y2R9FwgxtT3IhOO0YGTsEabFES8DK0wfCuuYYjKjsKqALYlgfaXfJgD2Im3iljg8VT4xYDntRQF0-xgYZvPHJqT1rSymzfWy5qGrCcusBTZhazw0UL98NlMI6RDHmeEB3j52vMIasmFjpZ1ttEYXrBatL5jWfjkc-C-wMHz-KZWFjsmxcxknc8OnTje9n0GotZ7d0DZnCjQwsy1ZXnyXuKsiriTtJp2w9Zu3yibq-lqsOE6IMyyy0VLQOXgk2aCPeMZHoLZ8xMcbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Twk1OAICpD_cnlzDyuaPjbx1P31xD7lU6tBvfaa53MZNTwwXJ9Fa3eqDeJllo9bpy_hPCNE3y2R9FwgxtT3IhOO0YGTsEabFES8DK0wfCuuYYjKjsKqALYlgfaXfJgD2Im3iljg8VT4xYDntRQF0-xgYZvPHJqT1rSymzfWy5qGrCcusBTZhazw0UL98NlMI6RDHmeEB3j52vMIasmFjpZ1ttEYXrBatL5jWfjkc-C-wMHz-KZWFjsmxcxknc8OnTje9n0GotZ7d0DZnCjQwsy1ZXnyXuKsiriTtJp2w9Zu3yibq-lqsOE6IMyyy0VLQOXgk2aCPeMZHoLZ8xMcbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMAA30NalXQljWKX1BR-i0MsFzEJ2UMCwTvzS1wAlVSp99vfGNdaLMUMPsFfUyC828WS5GgFxr4OX8YixClyjHwcw4Blgu-RDseDnBbHpubVIE3ZTNH_rq6rEkniFLjGtcESWBhwzFr54XPk4SbwqyrWeO9rBkqj3ih_fHS9AYoqv0dJhzZ6PQ5QZw9atCjCT58ZG0x-4x4SCkmBGkwxWb9ZTlGryZ2_2XRfp2ICrTyl89SvxWWDaRc5s5eqWN8E6W663ejlw4GMfX8eiNv5SItp6j83QQwJlR8b7K68VRH9fET3NM0iwnW3nHsY3NatHhGplxKvjheF3_8Vuo4Lzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
