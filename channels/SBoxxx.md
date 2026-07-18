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
<img src="https://cdn4.telesco.pe/file/aySSQUtWogR0WKgaBB5F7zD25ZLRZI0DyGeA9LYozjSZsRS_8skvJzqY4NbCnyR6s3dyo4FsNOqkmmkLywtS96KA8Upq-5G7WffySji_LH8xC0YEDVVLfoyCDWQvIGwqdokNPhzumK9LFX74f8fWMCtZaSAr-B8rSYw9FRZJrBz0jXIYGEBJzxFPPQFf1Ygvck3w4Sm8KeDfe0FwOkgw7sbYmdwh0kiprjma8FWBSeavPdKv8Jkf5vVGNPeCQGINaba46b8khDL--9FF-SioTDLUDF0E1kUery8LbxH81a6F66mqm10pvAcGgfpjL-leTvHqobN-N9GpiGnB51lPyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.4K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 22:20:19</div>
<hr>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mK31Ku86h5Pwss19jvRwcEb9ABX9ikkvLoV_33bvJmpQeF8WQBuw02ytF6RxQ2DyxS6bcG0SojlkLMPHpmqPoIsRRJcUz3IRQ76egDzL2Kh88u8ADugd3k2yiQhBIOx-tLrMWy6DXJ3sl3eQIRaR7fQH18B06aXV6hYsL5OuCM0pmSgsdYLS25bvjFZf6W7ObDTxlzNHvt4CuN7GuG5qbk_z0wTMfWOMaPgRWtr1YNJ01JxdpdemqOYmEESYB2QtKcOhnbbh9QdHVEsmyXQCJjPccJ9l51ilvKM6Gum3TkMZeiYUAgDi2eCeC7O-1_CiBFhq505b2UQndW_mcH2KCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید گدبان سفیر اسرائیل در سازمان ملل:
موج آهنین درحال برخواستن است.</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SBoxxx/18949" target="_blank">📅 21:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab73Aa7MNtFUD_sUlKtUj50_VWodQwu9nyChcayZlHDSv2k_KgJORF4On6cHS_rDNXJLLSBPlRxNNes3xaz0Jwy-KeO-fcvuxonLb3tLPDUJ6t1YJDeyD6yVS3d7P_ZP-cDPhh6uSAXZX--zHYVP_N7Fj_W2WdE1bmH-FG5IOG7XfVTCsf2NQES5qOloFGdUbmdu0ECcro_YV1sdgCz2vctjPrGkS9VzxRdmI_wG0b_GL8sgAYD4izT6e-AxmKeBF92__gdrhKtwf11WrK_lhfxmFkP_4_8cNuHpRdyqnvozxqHh14FZoQLm6QjDSG7macsKJ8XN_OND1Em20-EOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است سپاه پاسداران را مانند داعش نابود کنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، در اظهاراتی تازه احتمال اقدام نظامی گسترده علیه سپاه پاسداران انقلاب اسلامی را رد نکرده و گفته است که واشنگتن ممکن است این نهاد را «مانند داعش از بین ببرد». این سخنان در شرایطی مطرح می‌شود که درگیری میان آمریکا و ایران پس از فروپاشی آتش‌بس دوباره شدت گرفته و دو طرف وارد مرحله‌ای از حملات متقابل شده‌اند. (
Time
)
ترامپ در پاسخ به پرسشی درباره اینکه آیا ممکن است سپاه را همانند داعش هدف قرار دهد، گفت که «خواهیم دید چه اتفاقی می‌افتد». او همچنین مدعی شد که ایران بار دیگر خواهان مذاکره شده است، اما همزمان تأکید کرد که واشنگتن حاضر نیست بدون تغییر رفتار تهران، مسیر گفت‌وگو را ادامه دهد.
سپاه پاسداران یکی از مهم‌ترین ستون‌های ساختار قدرت جمهوری اسلامی محسوب می‌شود. این نهاد علاوه بر نقش نظامی، در حوزه‌های امنیت داخلی، برنامه موشکی، فعالیت‌های منطقه‌ای و شبکه نیروهای هم‌پیمان ایران در خاورمیانه نقش گسترده‌ای دارد. آمریکا در سال ۲۰۱۹ سپاه را در فهرست سازمان‌های تروریستی خارجی قرار داد.
مقایسه سپاه با داعش از سوی ترامپ نشان‌دهنده تغییر احتمالی در سطح اهداف جنگی آمریکا است. عملیات علیه داعش عمدتاً با هدف نابودی یک گروه شبه‌نظامی فراملی انجام شد، اما سپاه بخشی از ساختار رسمی حکومت ایران است؛ بنابراین هرگونه تلاش برای «نابودی» آن، می‌تواند به معنای رویارویی مستقیم با یکی از پایه‌های اصلی جمهوری اسلامی و افزایش شدید خطر گسترش جنگ باشد.
اظهارات ترامپ در حالی بیان شده که آمریکا حملات خود علیه اهداف نظامی ایران را افزایش داده و اعلام کرده است که مراکز فرماندهی، سامانه‌های پدافندی، توان موشکی و پهپادی و زیرساخت‌های مرتبط با تهدید علیه کشتیرانی در تنگه هرمز را هدف قرار داده است. ایران نیز در واکنش، حملاتی علیه مواضع آمریکا و متحدانش در منطقه انجام داده است.
از نگاه تحلیلگران، تهدید علیه سپاه نشان می‌دهد که اختلاف میان تهران و واشنگتن دیگر تنها حول موضوعاتی مانند برنامه هسته‌ای یا تحریم‌ها نیست، بلکه به سمت یک رویارویی ساختاری درباره نقش منطقه‌ای ایران و معماری امنیتی خاورمیانه حرکت کرده است.
در صورت عملی شدن چنین رویکردی، آمریکا با یک انتخاب بسیار پرهزینه روبه‌رو خواهد شد: تلاش برای ضربه زدن به مهم‌ترین نهاد نظامی ایران، بدون آنکه تضمینی برای فروپاشی ساختار قدرت تهران یا پایان درگیری وجود داشته باشد.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/18948" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGA3DXtgt4PX3aep6WJGkh1_BDqXZdle-X-jdyIJGqypWIrmI9Aravx3djFFCF0jA5xPOGt6fNQmZw1dFn4_SMlpDpxIBJOhyyC37AYLtil97Btd9NwzQAegETSMM-Xs9koSp41tTD8DEbAEMa1g65O2WWgbI_oQh3ck5Us9c-IqRaIkRBdNAwsLzSvrD3Hr-p1gTJxUl8lX0uXEOdJNnXjtu5s7fimQxNJL8GIID6DMXH7VFiiDCVBD_wfmyVifbl5yz83PdDDfoVsxJaEYr8l8wFhSTqXMnYmTZeJ9f-XkQe5fc8uJumGyx4TLu0RaAV4SoxxnOJAUZBj-_sbkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/18947" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/18946" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT1rMzf3aTnpqB7VoHLpmyZIeOaAmvROFJAdvUQLJzs8FhUGEY5aasQEVyv1helyLWAXaMqAbdP9a-tiZ34k0FZ2OLrf2YeEXOZ7cf1Zg-xZn8wQgafsMtb93jIrT74A6QecyIrvsAbF6hQlwUs_-ZmGIYDlE86bWnw0M4ig8G0EoD-ozfslJNikLnwK6qQ-IJ-jNlWNY18E8Xf9u-1CAVlFah1wk_x7jtLv0MNrq8PJ1VKAHuYDnlYeOp4BnEGSM9Hgo3h5SQ3HmCG8LQTZ-ld0zdWDkRGO3jEHus-wR0MZTai2_oxQYLp_YT_k3CHbGaTj2KYc7ef-3ugjX4v8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/18945" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/18944" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.
در حال حاضر، یک نظامی دیگر مفقود الاثر است.
چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.
سایر افراد که دچار جراحات جزئی شده بودند، به وظایف خود بازگشتند.</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18943" target="_blank">📅 20:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AftHM0yYmFuAf2E-l-hMueNxoiG00u107NEaQ13YeaROvzNGmM3y2UxoKHIaZpWoR4CsIiLXLnF0dUAo7vbb-BBXzsUZNOpjgGYJS4JIMIf5hupn7utlOf_sQIS0OyL0MQZUopEDOX5SgW0MurZQDUHGAGr9YcKxTokCq8VrU01cNr4gfXm6SEpWk91kTiZE-gppzzNcjNdusx6kOmJFDoOFRI7G2V0ZuJUyh9q9UH3din8Sa-Mx0Kos__MOCWrz1JxeR4m-NMx5QuE9lR_HopheGOp8Cet2xn8V_fHZr4pfR_O437PeB1zcftRHUNRJh-X9qhlum_BKguDKTlLPkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام می گوید در حمله سپاه به پایگاه آمریکایی ها در التنف سوریه هیچ تلفاتی وارد نشده است.  اساساً به نظر من حمله به سوریه پیامی تهدیدآمیز به جولانی بود که به حزب الله حمله نکند ولی اینها جدی گرفتند.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/18942" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=f8o2ZK21ZxQb3iBZYjmufzWXr93cl5G7vQSvyXdYPr3z55hIGjdFfUHAHNJqrCRdaexSItRRhywKQVseEZdoptDM3P9tTY1k7ybRcOFfKSfSN8iNESeW5LYUr262Adp5ySk6-P3Rk4YCpIJSi0zrVAcoSTTmv8sgmvmIV1WcgPS-0CFDOWFt8B1bv53gcEkiHtCLtToD9mWx965NgDfJogDFxgO1_eJMvTFLRy99zvW7V_alNZB8SXhrMbFDdsJw0qJO5FtL-r0rs7pX6oBGOdSVMt4rfV6qnmYsN04FPhjHsej8D87iDIRJ7ZnqQKvEpkqq9NgDH7K_e67Q117vmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=f8o2ZK21ZxQb3iBZYjmufzWXr93cl5G7vQSvyXdYPr3z55hIGjdFfUHAHNJqrCRdaexSItRRhywKQVseEZdoptDM3P9tTY1k7ybRcOFfKSfSN8iNESeW5LYUr262Adp5ySk6-P3Rk4YCpIJSi0zrVAcoSTTmv8sgmvmIV1WcgPS-0CFDOWFt8B1bv53gcEkiHtCLtToD9mWx965NgDfJogDFxgO1_eJMvTFLRy99zvW7V_alNZB8SXhrMbFDdsJw0qJO5FtL-r0rs7pX6oBGOdSVMt4rfV6qnmYsN04FPhjHsej8D87iDIRJ7ZnqQKvEpkqq9NgDH7K_e67Q117vmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می شود این ویدیو مربوط به اعزام صدها نیروی ویژه آمریکایی به جبهه های جنگ ایران است.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/18941" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast -- 8.pdf</div>
  <div class="tg-doc-extra">210.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/18940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/18940" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/18939" target="_blank">📅 20:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بلومبرگ :   قیمت بنزین خودروها در ایالات متحده با تشدید رویارویی بین واشنگتن و تهران، بار دیگر به نزدیکی ۴ دلار در هر گالن رسیده است</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18938" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/18937" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انتقاد شدید علی‌اکبر ولایتی مشاور رهبر شهید انقلاب در امور بین الملل از نخست‌وزیر عراق  سفری تأسف بار، بی‌موقع و تخریب کننده مجاهدتهای ملت غیور و مجاهد عراق در تاریخ چند هزار ساله این کشور بزرگ، توسط نخست وزیر جوان و کم تجربه، آقای علی الزیدی.  وی تأکید کرد…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18936" target="_blank">📅 19:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/18935" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت خارجه قطر:
«ما مجدداً تأکید می‌کنیم که هدف قرار دادن نیروگاه‌های برق و تأسیسات شیرین‌سازی آب در کویت از تمام خطوط قرمز عبور می‌کند».</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/18934" target="_blank">📅 17:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/18933" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/18932" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV3loRHioADLexKJfsc2PHUbk91O7Oq4EdUnTKvrKb8O6DX_wk8_rYJ3OqLM2j43qvwXShtW3cXpCg2baIcgY938N9Q0yexn_GIxQT3DTA4Dc6c8PfoutPncTMkNUfB2XGHZfIoFFHYZ9VekWPzHHZGV3g_eTl8HGR2_96QVsHaVfjhTmpr88GhIZaGKMcMBfBWbwl1Rd-4HFMj3riCH78tsc_nf7KwrRwjyhyme-ImW7Hso1cO3bntuxm9a7eCK4s0I9NqAYlzs1YCE3hHYgGo3lf2UXqBxrlXb05hYyfxb4klqWJi8aRofGU0NWPfwTz4BHjbmR0YUsyeex2tOgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟
قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.
در بحران ۲۰۲۶ نیز با وجود کاهش نسبی قیمت نفت پس از آتش‌بس، ماندگاری قیمت بالای بنزین فشار سیاسی بر ترامپ را حفظ کرد و به عاملی مهم در کاهش نرخ تأیید او تبدیل شد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/18931" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا در مواجهه با ایران کلأ دو راه برایش مانده: بمب اتم یا حمله زیرساختی نابودکننده</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18930" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejFnr1orrVn0B01EnUkrTPgQwz0OZVUNHQCDdb4BL_o8x0ieyyshHpNVjuyikINooxVwYBs4yRsmvzmtryGu4H2le7TSOs97j3L-igBKnb1TnGsU9DIs6Y9mQJjugJKqWiTbz2bdQqTqC1GOPIAqdZ6mHBP8c_srxkafhDej1DkWNg3RSV-iCWhypMSK0DPk3g2Zi4CrYAevcq6Lt3Hma3lq4DunMcsGck-jTd5US5YK3lroda6V8WCwDjHBI2IFhSlfRvPSg7HWk59I0MrT1KZ-9q7gWd8fydj2YKJLEK5AMdd1996XN0eVeMMrkgEbK2fLkGwvE-Q122-s6CpPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف مورد اصابت گرفته در منطقه از سوی سپاه</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18929" target="_blank">📅 16:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18928">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">موشک‌های بالستیک ایرانی آکادمی امنیت کویت را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18928" target="_blank">📅 16:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18927" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18926">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=bxkSkB1k8GBT0iHccYyvtZTkicCNgeP3TGoSRetCr9NlWjo2O971a_xAjkHoVZLA1xQ2DuXhzkqEvevtyeXYPGubgERyXWdWcL7TpLFiYXTXlTXWw4Nhof_kxVQyeKy8zC-mvsqhbMW2Sl8LGNZd2NJBCkp9EgJIyFTDIXr1Oe1hd7nV7SfwwC_ttFvVe0y696svR31CMnXUE66AK65bQ3C93yoeZdtZO_FMJ8KjY9_eLJ071f5ZkB83bbxtxgJGeIpMLUeXlm-F4BNSbnBHovXMN3TlytS5Z1Vb1ZbQP_7j-voc3odSMmcdMOVDkjjtnvRD4T6nSmMtNpobowhffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=bxkSkB1k8GBT0iHccYyvtZTkicCNgeP3TGoSRetCr9NlWjo2O971a_xAjkHoVZLA1xQ2DuXhzkqEvevtyeXYPGubgERyXWdWcL7TpLFiYXTXlTXWw4Nhof_kxVQyeKy8zC-mvsqhbMW2Sl8LGNZd2NJBCkp9EgJIyFTDIXr1Oe1hd7nV7SfwwC_ttFvVe0y696svR31CMnXUE66AK65bQ3C93yoeZdtZO_FMJ8KjY9_eLJ071f5ZkB83bbxtxgJGeIpMLUeXlm-F4BNSbnBHovXMN3TlytS5Z1Vb1ZbQP_7j-voc3odSMmcdMOVDkjjtnvRD4T6nSmMtNpobowhffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18926" target="_blank">📅 11:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18925">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک مقام آمریکایی گفت که ایران یک موشک بالستیک به سمت یک پایگاه نظامی آمریکا در عربستان سعودی شلیک کرد.
این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه اخیر است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18925" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18924">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چین در این 4 سال مانند یک زالو، شیره جان روسیه را مکید و اکنون به دنبال زامبی کردن روسیه است.  ادعاهای ارضی چینی ها هم بعید نیست دوباره ضد روسیه مطرح بشود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18924" target="_blank">📅 11:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxKnHg5KNNU8dXxYvFjnlA-wjMs2nfzhmirZWOrhKmUmE22EjqZl8KVEQRxHZfV1X0Z6ExWbFJPtQiGpASc0af0Y5Qw7D1Tihj8fBuNXgJo_ZGPYsyXmAiELBhQfD3N3DrLxtPBOWVMWcuJurkBu6qLJ_wMlVZhwHpjh4GxUWuR6_RsMpXuc6JOa2TKIvykZs60kgOB3apYVK8fJwKzFSso6YqnmGTA-eEiP0CYdMXPV1pX5-Wa9Impq2XISjkw9sEJKxy3BzNUtPMZeGJ5Ngw9aKo3roMfBgGzxldc5d6gcjfXrQbQskxPRJPLoxnaaFPx1tYrA9XtuQl9Webf99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه زمانی تراکم حملات ایران به کویت از 3 ژوئن تا کنون</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18923" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پرس تی وی: نیروی دریایی سپاه پاسداران انقلاب اسلامی، حملات هوایی و موشکی را علیه اسکله پشتیبانی سوختی نیروی دریایی آمریکا در بندر الاحمدی کویت و همچنین انبوهی از هواپیماهای نظامی دشمن در پایگاه هوایی شیخ عیسی بحرین انجام داد.
این نیرو همچنین، مرکز داده‌های اطلاعاتی باتلکو متعلق به دشمن در بحرین را هدف قرار داد و یک مرکز ارتباطی و سیگنال دهی آمریکایی را در کویت منهدم کرد، در حالی که کنترل کامل تنگه هرمز را حفظ کرده است.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18922" target="_blank">📅 09:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">استانداری هرمزگان:
پل محور رفت سه راه‌میناب به‌سمت
رودان
بعد از دو راهی سرزه مورد حمله دشمن واقع شده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18921" target="_blank">📅 09:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سبحان الله!
شب خوش!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18920" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به نظر می‌رسد بانو وضعیت پدافند کویت را توصیف می‌کند!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18919" target="_blank">📅 01:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18917">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:  Oh, the night is my world City light painted girl  In the day, nothing matters It's the nighttime that flatters  In the night, no control Through the wall something's breaking…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/18917" target="_blank">📅 01:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:
Oh, the night is my world
City light painted girl
In the day, nothing matters
It's the nighttime that flatters
In the night, no control
Through the wall something's breaking
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never comes
A safe night (You take my self, you take my self control)
I'm living in the forest of a dream (You take my self, you take my self control)
I know the night is not as it would seem (You take my self, you take my self control)
I must believe in something, so I'll make myself believe it (You take my self, you take my self control)
This night will never go</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18916" target="_blank">📅 01:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18915" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18915" target="_blank">📅 01:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18914">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18914" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18913">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ایران اعلام کرد که یک پهپاد MQ-9 ریپر متعلق به ایالات متحده را در نزدیکی بوشهر سرنگون کرده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18913" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از کرامات شیخ ما یکی این است
شیره را خورد و گفت شیرین است</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18912" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سرلشکر رضایی:
هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18911" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.  ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18910" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.
ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18909" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تسنیم حمله به یزد و لار را که فرمانداران شان تکذیب کرده بودند تایید کرد!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18908" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجزیره : وقوع ۵ انفجار در شهر یزد، در مرکز کشور.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18907" target="_blank">📅 00:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18906" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مهر:
موشک‌های آمریکا به مناطق شهر اهواز برخورد کردند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18905" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چی بود امضا کردند اینها؟!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18904" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Memorandum of Misunderstanding!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18903" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اخبار تاییدنشده از حمله موشکی به یزد!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18902" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18901" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18900" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه پاسداران:
اگر آمریکا به پل‌ها و زیرساخت‌ها حمله کند، ما دارایی‌های صنعتی و فناوری اطلاعات شرکت‌های آمریکایی را که در منطقه حضور دارند، نابود خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18899" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حملات ایالات متحده به لار، استان فارس، ایران.
گزارش‌ها حاکی از آن است که این حملات با انفجارهای ثانویه همراه بوده‌اند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18898" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رونن کوهن، رئیس هیئت مشورتی کمیته وزارتی اسرائیل در امور شین بت:
«پس از ترور رهبر ایران، یک سوء قصد علیه یکی از اعضای خانواده نخست وزیر نتانیاهو انجام شد که در آخرین لحظه  خنثی شد.»</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18897" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!
ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18896" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18895" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIKLWWYhrDn1qSlw-KXxjGelSv8X75OVPeYYOv6wGfjxjKV2GjQDs_29EBPH94iZF1tJA1l6vovaWdgK7RyIMIjJgwQG1h01Km3hm_HLUpVpBGG7ru42GguARan6rsXXT1aPzFLYgQ_ypckljxIrEkCMY1YRyKnmq5leEYabPZclITaljxf7W41OIZzJEwTZslUvhxzsv6pLKHb5Bkiu30WEVd_M-Il1tDM7MJZa-lBT4ynxKKs6Asc2P-wvv2r2w71Zew94F1p0Lk1v4xdkcSX_jx7ME3gjFgTQFLuW8sYXZqQQwbjOal2B9fvP2gqIVfXevxoK6tNHvIApDFQAzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18894" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">داده فروشی به سبک ترامپ!  شرکت رسانه‌ای خانواده ترامپ، Trump Media & Technology Group (TMTG)، قصد دارد سرویس جدیدی با نام Truth API راه‌اندازی کند که به مؤسسات مالی، صندوق‌های سرمایه‌گذاری و شرکت‌های معاملاتی امکان می‌دهد پست‌های منتشرشده در شبکه اجتماعی Truth…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18893" target="_blank">📅 21:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تحقیقات CFTC درباره اپراتور تله‌پرامپتر ترامپ به اتهام استفاده از اطلاعات محرمانه  گابریل پرز (Gabriel Perez)، اپراتور تله‌پرامپتر که مسئول کنترل متن سخنرانی‌ها و هماهنگی نمایش آن برای دونالد ترامپ است، تحت تحقیق کمیسیون معاملات آتی کالاهای آمریکا (CFTC) قرار…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/18892" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7b70ZmpbQTmW89XEhje0GICf8ASp2jhZlBeW3JXYC1vms9s0zEDrdWgELKhYUfouZ8eR6P89jNr0qPpRxjeJwlBSOTDreiFQrBAdHEm7Jk4_IK_7wJYXAGwT5_HONeibbScEq70DgSv8k-Q5mYwHBxSwLq_9B14LE-SMHrQq074aG1y74l85o2S82MYh-xYTygrq0Ada9OapArrncOS1JmeRdW1Ja8cfHMd5Y_FFVWFbQVXAhUMUUZKKUjmUrWusaCzvIf3f_4F5ufWz5ntua3WTEtcyRQTtkMiEp18uhIGJEInaAcldkg5qRgy2VFYbIq7bygJ_tNxI75ZQvpCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PpZig6JiCGwC5uurPfczVoCsIcWTLqAweSN1udA4Z00TtJZ2WSAaF0NaCCDOgN7jy-nzDc_9kQwvL4bL76JuK65a7ZjKZHH4sQQBu8a1JeAPQ2J2qo8yTC0wlHfGUzhpepT683eW3ISQJHv0gKxI5akMFSd2NVmVDg2lnHfEou_SHGhmj8NkrxENAgwktNamMcE7vhJ1x-sik3WOzZaror35jJYyuVJpONAfTVCnFUC773qjAubPZqqxyIGuYqkusjYcbknReL6XrgDy8FSsWFwPxE8iGn4-cJePkBxwGrDzaaMXQmhVBmGJ-DtfGqQhDh1DDNfamkvFGPy6b7xdpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همبستگی عجیبی میان شمار اعضای کانال با قیمت دلار به ریال وجود دارد!
شاید چون اینجا هیچ گاه خوش بینی متوهمانه برای مذاکرات به خواننده تزریق نشده است.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18890" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18889">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دولت ترامپ به اسرائیل اطلاع داده است که قصد دارد ده‌ها فروند هواپیمای تانکر سوخت‌رسان آمریکایی دیگر را به این منطقه اعزام کند، در حالی که  ترامپ در حال بررسی گسترش عملیات نظامی علیه ایران است.
اگرچه ترامپ هنوز تصمیم نهایی را نگرفته است، مقامات می‌گویند که احتمال افزایش تنش‌ها در روزهای آینده وجود دارد.
— Axios</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18889" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18888">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHjc_wf3BbAbV2rPWnpKn3Zbm_C6CewihxxpPy-MZgrlZR9r5CkHxn5G8i4g9t_aA6jimBUwsD1SaKSZTC6N18zLe1p-Ra2ijDOHdvTuY5_BbPJ97v2579oSeoidYKZTayd8VBwlk7xrp5zQ4sYM1TCJdO2RJehasH2jrcGVoTqdMw6iBblhG9h8Unj6wpZOH4wilou4zm2X4IcNd6p5mTR9GAKvF-pMMbYAss3vNozY8-i-PdBTDuybPLZrQRxuAC5k6UjiypFd8hzi0UPY5VbIe_LV0Sn8BX1EapUw2SOWcJzeB3gD4eG-kTdg1I-B5TFMXQ6EG01KBbwF5pebNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم شاخص #GRI به درستی پویه های ژئوپولیتیک را تشخیص داد.  #GRI</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18888" target="_blank">📅 19:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18887">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQZXq4Mm5xNKff-YPDfsl5I4jTlPOSYAPCT3Wz9F9yzdr8PllO65t9wzy9VeZ_idJrLpm1ubzT8olWBtuGrwx1-0WhM8ocfy3Es41W_hinc6RDYytQUmHnlaeGd7hXi6rz0qpZFYWFEjtCuijwF0l-2BNEkUoeNYKfh4bozzI4s7dYVTAxwEMWYLM4JM1E1ENuMp9avFotRemLkbAlrUH-DHLz2k__PPr-8yfdjlNUVBKEOhE3-ThHYZJZoLjnfijUHEShk5SFprt1FowQ8aH2Uk9xKJsl9CtjCwCMHAWTfLTMbCMXRaoSXCgAVcJ9h5QrK9xVlSN2gxbzfCBdTFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.  پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18887" target="_blank">📅 19:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18886">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlyuEQ1pA7o3XmCjQTOLUq5ypm4PTGffdshGV8R3JGQmTxyw-h7g2BrevCOuG_Db5e0nGTxPC2mAUylpDnzP2GIsTe9xHQbGUwYRjM-sG76f9nKUK4cfdjUPPN8dAgYGmoLG4PnDAfvDSvqZkfqDgQY3H2Vs9QnPaRcqaKCHWLlOhdFj2U7Cx4RVRfbSbdtB_kZERTaxHqNIcHmPNFfYsoNFkvdx_AdUYAgmNdO1U-YowHIoKH_nQQ7TMED3m2Ua2IQI38CdGz_MdOOojzCg4ITueqPfrHczG7sH7DVR_RxvKqs_JuVJ7OBIEwfo-_khL3gqguSOKaSo_cC-_8XoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18886" target="_blank">📅 17:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18885">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پاکستان و کویت در مراحل اولیه گفتگوهایی برای گسترش همکاری‌های دفاعی خود هستند
به گزارش‌ها، کویت به دنبال یک توافق امنیتی به سبک عربستان سعودی است که می‌تواند شامل حضور نیروهای پاکستانی، هواپیماهای جنگنده، پهپادها، سامانه‌های پدافند هوایی و سایر حمایت‌های نظامی باشد و در مقابل افزایش همکاری و سرمایه‌گذاری در حوزه انرژی را به پاکستان پیشنهاد می دهد.
با این حال، مقامات پاکستانی اعلام کرده‌اند که استقرار نیروهای رزمی در حال حاضر مورد بررسی قرار نمی‌گیرد و تأکید می‌کنند که این گفتگوها هنوز در مراحل اولیه خود قرار دارند.
منبع: رویترز
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18885" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNLtdlMCsJL_bbibFkcUTzhsSOKiFqZ6oXJ6tPBkBQFy-q5bF9HTCy9tEMtY8RDmQJyr8-Cs7T_w5IJZold52IH4TV7-uypFDFkQ_eZQlLCa6Kwr1I6ceN9aIcAWUQhMatXsanI9eLi_1Xax1rkc2vdun_wjY5G8ngnXRZotwHPBcxZWd_ZDvEiVFovS_YLdVIaQvLKywOxn6RydwsX7ESVQSLX8mF3C4mtPajIUK5zWvp9mpIqQ7-oY0Ekv6kSH40o4V2HMM6IlpqhlS8VcC9vBHPmSj4iZlTOAfhk8rMnkTy2oKcIJ98lbOpweH_NofkZNg8FQtgz9SvEQps6ExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی همسرت رو میخوای طلاق بدی اما مهریه ش هم سنگینه!</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SBoxxx/18884" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نایب رئیس آرژانتین انگلیس را «دزدان دریایی غاصب» و «تجاوز‌گران» نامید و پیش از نیمه‌نهایی جام جهانی به مناقشه جزایر فالکلند اشاره کرد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18883" target="_blank">📅 16:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18882" target="_blank">📅 15:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">علی مطهری:   یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18881" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">علی مطهری:
یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18880" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzWxnYjaGfpyDV0n3CsY7ZLPAeqZSEFG7Br9DojE-emwyB2G7_SbWQvoqDv7p-hfuxPHPabkOPbhMi-FkUUTJod68qBOZiualkC2akxqdrv5Zihmv8_jCkolXoCyxLVO-xXY5qe92bg60asoOnyx-JIVwrJkhq7_CaZdFMD9WQ-XNDnwFtCegeJFCIDtb1a20SBTIEqD8J8mNtAtEbT5_uSs0r03jLIAAJr60pTbODLjX3MSzITV-ufCVa-Ez1oQPYgCqI_VzktbBz-M4w_ZON5y4zhyZz1YBYxG7MB2YzAte7GoyI7Ns40HftjJbnkysYotexPTUFDodPx4Cde7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18879" target="_blank">📅 14:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18878">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18878" target="_blank">📅 14:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5HRmpiQWCDaaN3ZkkcIwiETIvFo4LYNyF4dDwG5tSb3rTCTkF2jbOz-SGq_62AmtSRyiQStQu-h3qozcg8MeQBZNdjxGswDPm7kS46gRHSm1vGhNC5NYCIT4p-kFQr-waTkTjMW68BSgtUlncbpzb7iznq6T-GKv5TZXwxMHcqKeroPCMETc9hWzPHm1nCcox0lUP_qrA4jbilqpsLb6mQ1OpMyVGm0rtm8BLuHQcpaLGnR0CaHLqxWkktHOdUxRChfprsqdsgAgAIIvKELSVDc8o3hsncpChzbJbi7V4WneubVzBqr1oV56zjEn8bIsok-vbjrUTi4GF1SaJOm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.   مسمومیت با پولونیوم-۲۱۰ (در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18877" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjBkT87LmgowUUZNoO0yhYaGNQnVETmfk-IwuKQtu_YUYlVTvEk4XJNxngAFcJuH2vV-7063JFjPQDqstihxaSLglrM-M2Q9_I-L3VeuCHJSqkzM55k5t8mtNNBMrLjyJqBN4VtdXRnP7vCJG-NMOpDmLmonzeapfWLIDVlqrzfZx9xxT0OsNLbLEpen6hlymK-Ps_sZo_0uMBamrWgMt09mMByscyk54n-d8ONzHdSA03bxhSDctUT-K8UsrWOSVHpMbIJoLQQB7VVA3cpRXbHph-TKQXKbsdrVzvUijVeiI-4e3BCPw0N96al7se8A95JSLRll-ctdMs6ltupMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توفان احضاریه‌ دموکرات‌ها؛ تلاش نمایندگان کنگره آمریکا برای واکاوی معاملات ترامپ و حلقه نزدیکانش  لینک  #بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18876" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الازرق</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18875" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
انهدام چند فروند سوخت‌رسان و جنگندۀ آمریکایی با موشک بالستیک و پهپادهای متعدد
در موج۱۴ عملیات نصر۲
🔹
سپاه پاسداران: مردم شریف اردن؛ مردمان نجیب سرزمین قدمگاه انبیا الهی، ای مردمی که بیش از همه‌ی مردم جهان با فلسطین قرابت دارید و با دردهای مظلومان غزه و کرانه از همه آشناترید، بعد از حمله سال گذشته ما به پایگاه العدید قطر، ارتش کودک‌کش آمریکا برای دور کردن مرکز فرماندهی خود از حجم بالای آتش رزمندگان اسلام، مرکز فرماندهی نیروهای آمریکا در منطقه (سنتکام) را از قطر به الازرق در خاک شما منتقل کرد و از آن موقع تاکنون مرکز فرماندهی شرارت علیه مردم فلسطین و سایر کشورهای اسلامی در خاک شما و دردسترس شماست.
🔹
علاوه بر سنتکام پایگاه هوایی و دهها فروند سوخت‌رسان، اف۳۵، اف۱۵، و اف۱۶ آمریکایی در خاک شما مستقر هستند و از آنجا به مردم مظلوم فلسطین، ایران و لبنان حمله هوایی می‌کنند.
🔹
شب گذشته ارتش کودک‌کش آمریکا بازهم شرارت کرد و از پایگاه‌های خود در اردن برای ارتکاب جنایت جنگی بزرگ و زدن اهداف غیر نظامی از جمله چند پل، محلات مسکونی و یک مرکز پمپاژ آب در بندرعباس در جنوب ایران استفاده کرد.
🔹
در پاسخ به این شرارت، رزمندگان اسلام در موج ۱۴ عملیات نصر ۲ با رمز مبارک یا صاحب‌الزمان(عج) ادرکنی جنگنده‌ها و سوخت‌رسان‌های آمریکایی مستقر در اردن را در دو مرحله حمله با چندین فروند موشک بالستیک و پهپادهای متعدد مورد هدف قرار دادند که منجر به انهدام چند فروند سوخت‌رسان و جنگنده آمریکایی و آسیب جدی به تعداد بیشتری از آنها شد.
🔹
اینک نوبت شما مردم شریف و ارتش غیور و با شرف اردن است که به تکلیف الهی خود عمل کنند و با ضربه به منافع آمریکایی متجاوز و ضداسلام، لکۀ ننگ آمریکاییهای اشغالگر را از دامان اردن عزیز پاک کنید.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18874" target="_blank">📅 13:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18873" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18872" target="_blank">📅 13:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18871" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو  لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.  این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18870" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTx48hpXRbLf14gElUNuj4arNcWj2EYDZHS5sUtI3ilGSXwebTL3BE8jBfsZyXwcO21CWACiCuubyT0H94thFzdmDPrURWH4Qcih7gm2zGtOB4irkCio7JxcpX9d0U14dSstesIkEokrfcA-jlv4CkLwiFyyg-qDmjX2cWmKDC7dzzaMCSjqBlMLZ6Z1jq_-Heg3_GyT9r5Ff1lvJwHnUuoBxI1OZvFIZlRfxBMCjF35207lI68bgw44673_IRj3t0dy-Mci_JiWK3xVUccyJjpGutiI86DMBVkJYZMDWmDTmdOhcvH-ankERWf-LiS2evweBrXwTH0PQVn9bT-hvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو
لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.
این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18869" target="_blank">📅 11:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MUt3UOzDRhwI3yUJ3U8QrXSVXTr3WuORq-UmVJVukwYeULUxa_9voqRylKdHrCsBGpKAJ6taj7DV6rn8E_RZwwarX-pl7oPOksFiz-H5K7y_h_C7QSvBitscXkQM75DlX8nkxudo1nhazB7scRHwMO1ypRZSnhxRZHj13svGFpoUfJR4d40mBRWcyJ_WvQoLeAuw9QSuwBoFyjSL_41SCcOR4FE58E93t4KO9vJEw3rJyuu7gRTh6HAc9gXikE_txigKO4iMf16XYpVjwjShrx5o7_S0BTzmjOF-hLyg3EUvmf1T0fSnfF8DsMk3nzAZxZS4x25-SFdJy0fn-squuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ـ
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18868" target="_blank">📅 11:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1rA-SBDlpGt3L8avkOFdfJm-zlqvNCJKdoQcetbSl04bL1LRyvDs_J81jdRFYomUpWjQAvUzbYlXFVoOjC-6asCEMmnTXC4dMf8_XKiutCq74kd3YMW4B32xycyzY56DkEMD1XRC5JIioygAqvu5XsuNXTMSHVVOIZ-XWVSUmwI13j65ngIqY3_LcAfF_4HmhHzZJs_3CC6oHZCo0YsCJagkaJY7x1GaJSm4SxnP-Dtq0j5A6j0QILwrRJPD6SpGZI_XMyailWmXIrG7KZTDtsyY0ZqaowJP_S5Wv1m3CpHbi5A-x_01iHdmYP7QzA1lRhZqcBRfYXnZvX8ZTbptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نمودار نسبت بورس به سکه که دست به دست می شود و از آن عملکرد بهتر بورس نسبت به طلا در سالهای آتی نتیجه گرفته می شود تنها در صورتی محقق خواهدشد که :
— سازش اساسی — چندین بار بهتر و فراتر از برجام — داشته باشیم
— تغییر حاکمیت سیاسی در ایران روی بدهد و آن هم بدون جنگ داخلی و تجزیه
به جز این دو صورت هیچ تضمینی نیست که این بار هم محدوده حمایتی مشخص شده حتماً جواب بدهد.
تحلیل تکنیکال روی Ratio Charts هیچ تفاوتی با تحلیل تکنیکال روی نمودارهای سنتی ندارد و ممکن است همین رنج اساساً به پایین بشکند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18867" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLTsviHSta2LsIotIqAng75-C67xZ6jzjn8ro2-KhZFavlxFgzU_d7JijWqAqpFS6nNoSAvlhe8Lyvr8v9ihrgSyyYbKgdOZKYsXBNAR8Rm0HH4RL_gDrnP2nfFjpqq0eiw2cviyPNBIF6ZZq_gxgvPomRLC3d2N8PqZKfs7Lp2oGGb9LpwGiGKfhKBsGbQH4hxsUWPF54q-xbjciTisd4tyCIZyRezZb59ibAuHYOPWCZl5VONJa3J8BI9KkgTbfZzQ26bbpdJERPvTzVXRFGJjr49TcTtsatlxqGDvx-6paaUE2gc_z_Ik3wmXurBL3qC5enRa2l-Hhn6kM9Rd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18866" target="_blank">📅 11:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6-uQ1yKbTf9SKnbfUnMb8nUckkuT6ypL36oytaQgoRkdwLCCsTQrfvqRnPkH2bfBC7ETmRWRdaKGDgsVBGmsTyaLQBM4M-VkkSvEHKN7nNDCpWgHzGoHlSbOygcJcFTtzXPa6KVmk5hN1Mhfd6WLF-ywbZ6NCo4byvG5PP5_Yn-EDg2PkPBfyHuHVbaoipSUHbV-h-lEC96dYSQOoaqVduAiNlO57z_KVg1XR1kxVSnFjGaGQ69v-vbL22twE76ZT0W1G0BkzYi5rzuwWiPaAr1_2rQUnzadNyplw0diK04xei4XNSSlTbeRnUFuqOpbrQleok4SL95tm7mAEe7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.
پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18865" target="_blank">📅 10:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18864">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18864" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 8
جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18864" target="_blank">📅 10:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18863">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مرکز UKMTO:
گزارش دریافت شده حاکی از برخورد یک تانکر با یک پرتابه نامشخص در روز پنجشنبه، در فاصله ۱۹ نریلی (حدود ۳۵ کیلومتر) شرق شهر خصب کشور عمان است. گزارش‌ها حاکی از آسیب جزئی به ساختار تانکر در نزدیکی عمان است.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18863" target="_blank">📅 10:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18862">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سپاه پاسداران: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم شد
در ادامه عملیات مقابله به مثل رزمندگان اسلام، سحرگاه امروز نیروی دریایی سپاه در موج ۱۳ عملیات نصر ۲ با رمز مبارک یا اباعبدالله الحسین (ع) و تقدیم به تمامی مردم‌خونگرم استان‌های خوزستان، بوشهر، هرمزگان و سیستان و بلوچستان، رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان را هدف قرار داده و منهدم کردند.
عملیات مقابله به مثل با قاطعیت ادامه دارد، همان‌گونه که بعثت جانانه شما مردم؛ و تنگه هرمز هم به فضل الهی کماکان در قبضه قدرت دریادلان نیروی دریایی سپاه است</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18862" target="_blank">📅 10:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18861">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anxGMNkMVr9_Su4iIrEbAyr-mVQ7oGT8gEEdYB2Qbs1NJ67j66hik_7dP6p8IUf3K81U28_PmRiLx3S8HU7fGyTz3sBR2TiqgYxeJnRgHSJClnQxmAWye4Bi2E1vmeLsd0GvhjatdBrUVrZUvKXllszO3KoCpGCgQK9Fh8737b8A1UOSfpsUHlLJreN__deAeXg88ubZXSYTh6YrVVs1RjmQ90S2ujVSIWMC-0_Weu-3z4WWK8qIKjTl9vmX44mKzxomOyFLVD4LD2zKgkKjesAN7xU6j8u1-RAhc9DoasVr3HMZM83unaiYpjC6M9LCkfcykzKk7X6nCCHWsqpZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج کنترل دریایی چابهار</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/18861" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18860">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18860" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18859">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تلویزیون ایران:
قطع برق در فرودگاه ایرانشهر واقع در استان سیستان و بلوچستان، در پی حمله آمریکا، اما هیچ تلفات جانی گزارش نشده است.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18859" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18858">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_4KI0___prk4TA8xGZfSRa1XbxukKuY3BHAUKqnoGoImsBfnKTH5Q3AkEfrfUh7IB3uNUZhJ-QWF2kpGYXXlLdaYEko4ZoLPA1lKkpL-y3VJeR4hzXXFutgg9VPAO07S3yR6RrPoulS2ulO5fFfAD7kG4Z9YKlsz-W0X7ZKj2dbZPjeIe2c3wCXi4f3oev2NuWqtvMlQkzVRNWPOEfIinCM0qHxjRD0Paupig4Rx488cjs2Tps_FE-yrEaLJ91MUXcStZYCOm-7NemhmR4fFBBT1wqyPXeMEhO7fYKmDUm-JgJx3fdIKpS3UXyT8A4h_vkgUxgWrAJWN2O9QC-X_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا ایران مستقیماً یک سامانه موشکی زمین به زمین آمریکایی را در کویت هدف قرار داده است.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/18858" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18857">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به‌روزرسانی ۱۶ جولای  سنتکام: یک کشتی «از کار انداخته شد» و کشتی دیگری «برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران» توقیف شد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18857" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18856">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18856" target="_blank">📅 01:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18855">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!  هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18855" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18854">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه های اسرائیلی:
پرواز جنگنده‌های اسرائیلی به سمت مقصدی نامعلوم.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18854" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18853">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش حمله به کویت، که احتمالاً توسط گروه‌های عراقی وابسته به ایران انجام شده است.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18853" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18852">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Business Insider:
اسرائیل از حملات موشکی ایران آموخت که به رهگیرهای بسیار بیشتری نیاز دارد؛ رئیس برنامه دفاع موشکی: «این یک مسابقه است»
حملات موشکی ایران، اسرائیل را به این نتیجه رسانده است که برای جنگ‌های آینده به تعداد بسیار بیشتری موشک رهگیر نسبت به برآوردهای قبلی نیاز دارد.
«موشه پاتل» (Moshe Patel)، رئیس سازمان دفاع موشکی اسرائیل، در گفت‌وگو با
Business Insider
گفت که تجربه نبردهای اخیر نشان داده است تولید رهگیرها باید با سرعت بسیار بیشتری انجام شود، زیرا «این یک مسابقه است»؛ مسابقه‌ای میان توان تولید رهگیرهای دفاعی و توان دشمن برای تولید و انباشت موشک‌های تهاجمی.
به گفته او، سامانه دفاع موشکی
Arrow
(پیکان)، که لایه اصلی دفاع اسرائیل در برابر موشک‌های بالستیک است، در جریان حملات ایران عملکرد موفقی داشته و طی عملیات‌های سال‌های ۲۰۲۴، ۲۰۲۵ و همچنین جنگ طولانی‌تر سال ۲۰۲۶، صدها موشک بالستیک را رهگیری کرده است.
پاتل گفت نرخ موفقیت این سامانه همچنان بیش از ۹۰ درصد بوده، اما حجم حملات و تغییر تاکتیک‌های دشمن نشان داده است که موجودی رهگیرها باید بسیار بیشتر از برآوردهای گذشته باشد. به گفته او، حتی اگر سامانه عملکرد بسیار خوبی داشته باشد، در یک جنگ طولانی، مصرف رهگیرها به سرعت افزایش می‌یابد.
وی افزود که اسرائیل اکنون علاوه بر افزایش تولید رهگیرهای فعلی، توسعه نسل‌های جدید این سامانه را نیز با سرعت بیشتری دنبال می‌کند. رهگیر
Arrow 4
به مراحل پایانی توسعه نزدیک شده و
Arrow 5
نیز در دست طراحی است. هر دو سامانه قرار است با بهره‌گیری از فناوری‌های جدید، از جمله هوش مصنوعی، توان مقابله با تهدیدات آینده را افزایش دهند.
پاتل تأکید کرد که اسرائیل تمامی داده‌های به‌دست‌آمده از رهگیری‌های واقعی را به دقت تحلیل می‌کند تا سامانه‌های دفاع موشکی خود را بهبود دهد. او گفت هر درگیری واقعی، اطلاعات ارزشمندی در اختیار مهندسان قرار می‌دهد که در آزمایش‌های عادی قابل دستیابی نیست.
این مقام اسرائیلی همچنین به فشار فزاینده بر زنجیره تأمین جهانی سامانه‌های دفاع هوایی اشاره کرد و گفت افزایش تقاضا برای موشک‌های رهگیر، از جمله سامانه آمریکایی
Patriot
، نشان می‌دهد بسیاری از کشورها به دنبال تقویت دفاع موشکی خود هستند و تولیدکنندگان باید ظرفیت تولید را افزایش دهند.
او در پایان گفت درس اصلی جنگ‌های اخیر این است که داشتن یک سامانه دفاعی پیشرفته به تنهایی کافی نیست؛ کشورها باید ذخایر بسیار بزرگی از موشک‌های رهگیر نیز در اختیار داشته باشند تا بتوانند در صورت وقوع یک نبرد طولانی، به دفاع مؤثر ادامه دهند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/18852" target="_blank">📅 00:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارهای شدید در سیریک</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18851" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آقایان این همه می گفتند پایگاه های آمریکا در منطقه را در هم کوبیدیم!
هیچ تاثیری در کاهش توان آفندی آمریکایی ها نداشته. هر شب دارند بدتر می زنند و اینها هر شب برای سر ترامپ جایزه می گذارند!</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/18850" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نماینده کنگره آمریکا از «تغییر رژیم» در ایران گفت
نماینده کنگره آمریکا تیم بورچت خواستار روی کار آمدن فردی در ایران شد که به گفته او با آمریکا تعامل کند.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18849" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمله آمریکا به تانکرهای سوخت در بندر عباس</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/18848" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
