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
<img src="https://cdn4.telesco.pe/file/bXE99KnaAax1XQ3dJzgiAkhDuK9vUAE_3zWLfoStzh4nSF9emjLD0lMtP3Bt4UKNdKS0M2Oi5ah1BLVQf8u5R5CwdERR0PWyMVD_FXC5v3Rpl8fa_BYctOYthNSH6-Ogfaajuz9HgQW7PblEd8YmVNzK355gMJTY36aT0yEYp6IPWTD4tB-OpKTdeN3jupcxChLBqFq_lXdqSKP8mHPZ1fh0bGFi0TdgxsrAcY8cIpyV9t0EyJth5-aeBEWaR0-dMW6451FqCG-kJ38dm5oKa5M27r59T46BE-E-timW31gGUtpkXNxTuJzmIR_u7be__bS6-hl8mCia1BIVR4GlqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک نفر دایرکت داده خب استاد ما که به قله رسیده و سرش نشسته ایم، حالا اگر پنبه نایاب شد بیاییم خود قله را آغشته به روغن بنفشه کنیم!</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/21237" target="_blank">📅 09:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترسم این است که پنبه هم نایاب شود؛ آن وقت با چی روغن بنفشه را داخل آنجایمان قرار بدهیم؟!  اصلاً آدم یک جوری می شود!</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/21236" target="_blank">📅 09:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شیوه درست استفاده از روغن بنفشه</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/21235" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=PGUW7fnOWkYEhUDBdBwuNeuAYGQseE1k4X15ZJpvq-GEKaxMA3wQWznlwWa_zP1AZ8UL9e5--i7fjCovkVi1G6cOpvBRZhnncOmSF0WY0-i1YaiGAOCimqHDBVmqygeRNJ0hsFHSR7U79txe_I99SAahmuL4ujFKvHgGHjGHTXDeAd1mQXRIlQAYxEH15z7aj_-LfxkXFYvrRndUYZ7-xRxKrkespOCj1fHaC52vWobF32xaJR2uR3NE8UVuZZ85AiIXEE9GJDa9qZp2kCj3gUBOXlS73mTmMvGXuROgm3lpiAthhaOG0VLwInre_QYMMEVlmpnd8nzYouElQdf-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=PGUW7fnOWkYEhUDBdBwuNeuAYGQseE1k4X15ZJpvq-GEKaxMA3wQWznlwWa_zP1AZ8UL9e5--i7fjCovkVi1G6cOpvBRZhnncOmSF0WY0-i1YaiGAOCimqHDBVmqygeRNJ0hsFHSR7U79txe_I99SAahmuL4ujFKvHgGHjGHTXDeAd1mQXRIlQAYxEH15z7aj_-LfxkXFYvrRndUYZ7-xRxKrkespOCj1fHaC52vWobF32xaJR2uR3NE8UVuZZ85AiIXEE9GJDa9qZp2kCj3gUBOXlS73mTmMvGXuROgm3lpiAthhaOG0VLwInre_QYMMEVlmpnd8nzYouElQdf-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.  در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/21234" target="_blank">📅 08:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZR2R3BXR9ojj7XnTPt5RCpzIwHIVbUfi5wtfUzDN3med5MoW7bOrymHaQhh7zbpVmYHZ4AXQUTv8uTjUkLI2Nq4mVZyNOgRTtdaLqFUyQFZAginAwjZyyln67mqDUnMrEPZFQN_lMeFugH5qx5Y7MLIJCfXYv2zCgHulendpfDVge6mqHQADigMxN-bkVm1TBhnsiBvFTjm2AQwJxpp0z2BacQFGxLM9KHHjfLTX4JARdtolVqhIrdd55OCxs3qop-HgAR8NMt0UffgrvrrDMAVyT5W0V-Ije0oOL0V-1HU3bNU9dimAoRKbawha5c_j8UU_wcFBpYmElEohIQTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.
در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/21233" target="_blank">📅 08:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بوی محاصره زمینی می آید…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/21232" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حملات موشکی گسترده سپاه در تنگه هرمز</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/21231" target="_blank">📅 07:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FL3KT-dWbnkz-jIjsBwL2vVnVbhNv-vnJyVxc-GwtnutvK1vVQNdpizB7qGuI2goYaW6uRuTvk22vV5Z8-ECf5C6t9khoQKdn3D4SnBdyLBmPWBShpB_CZGz-st9GWerwj09QqA6wlc12Fj9aXioJQfHrjpbTb31gfOO9qcTgvGmntx_98kEeVp3yXqmBz0ThVvlHO_rmFyFAdd2qoYiWuFExJfYosMznxM3kcykGU7tgmFTu2Yg06y26dy0ou1DMSRkABIqSdFxkgK30A_uQlFWd98l3i8NhCPesQmRB-0YHxLLtVl68jaSZGakg4sQG3eXwBfai9wIKsMU0I4uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه
فرودگاه نجف عراق که اجازه پرواز به هواپیماهای ایرانی رو نمیده ،
توسط جمهوری اسلامی ساخته شده
😄
شب خوش!
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/21230" target="_blank">📅 01:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">واشنگتن و پکن؛ پیام مشترک درباره ایران و تنگه هرمز
در یکی از قابل‌توجه‌ترین بخش‌های دیدار اخیر دونالد ترامپ و شی جین‌پینگ، موضوع ایران نیز در گفت‌وگوهای دو رهبر مطرح شد؛ موضوعی که می‌تواند برای تهران و به‌ویژه آینده تنگه هرمز اهمیت ژئوپلیتیکی قابل‌توجهی داشته باشد.
بر اساس فکت‌شیت منتشرشده از سوی کاخ سفید، ترامپ و شی درباره نگرانی‌های جهانی از جمله ایران گفت‌وگو کردند و بر دو اصل تأکید داشتند: ایران نباید به سلاح هسته‌ای دست پیدا کند و هیچ کشور یا نهادی نباید برای عبور از آبراه‌های بین‌المللی عوارض تعیین کند.
اگرچه در متن جدید نام «تنگه هرمز» به‌طور مستقیم ذکر نشده، اما این بند در شرایط کنونی به‌وضوح با مناقشه هرمز ارتباط پیدا می‌کند. اهمیت موضوع زمانی بیشتر می‌شود که بدانیم در مواضع قبلی واشنگتن و پکن، مسئله بازگشایی هرمز و مخالفت با دریافت عوارض برای عبور کشتی‌ها صراحتاً مطرح شده بود.
از منظر تهران، نکته مهم صرفاً محتوای این دو موضع نیست؛ بلکه هم‌زمانی مواضع واشنگتن و پکن اهمیت بیشتری دارد. چین بزرگ‌ترین خریدار نفت ایران و یکی از مهم‌ترین شرکای اقتصادی تهران است و در بسیاری از پرونده‌های ژئوپلیتیکی در برابر فشارهای آمریکا موضع متفاوتی داشته است. بنابراین هم‌صدایی آمریکا و چین درباره اصول مرتبط با هرمز می‌تواند فضای مانور دیپلماتیک ایران را محدودتر کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21229" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21228">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibXgYLbR22wuxeU4Hrp7KyPAHl_Ew9MK49VNHQMLniPyotPmn58O8_9jNSbuia_MxN-IZ9bViMLK0WQAKQzaKFagCEQmMN5dtsgKOSMR-bCz7yf2bXg64z58VMmAYK8_6SdkCnfUDU5Pk1xKzgN-9fJn4sVdJ-LzhjV6H88aqBdufJizyme4AHTCSS41c9ACKeuHYkWBSmEkQmDSTPm7znCOUdax2_AvjnCGhRFs_XOSECe8TLYRmSKdrj4UtlRo0D8xSHZwPCX0oz65bIAxMk2ZonXakPK4QmKIe6xjB7C4KE8O9znaWREGEVylVsXfMB6_xTiRlRwXSSgpJyoaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عملیات انتقال کشتی‌به‌کشتی (STS) در دریای عمان نسبت به سطح ماه فوریه، ده برابر شده است.
تولیدکنندگان نفت را بارگیری کرده و با عبور از تنگه هرمز از طریق مسیری جایگزین که امنیت آن توسط ارتش آمریکا در نزدیکی سواحل عمان تأمین می‌شود، محموله‌ها را برای تحویل به خریداران نهایی به کشتی‌های بزرگ‌تر منتقل می‌کنند.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21228" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شورای عالی امنیت ملی:  «ادعاهایی مبنی بر اینکه ایران به محدودیت‌های اخیر هوایی با اقدام نظامی پاسخ خواهد داد، نادرست است.  مذاکرات با کشورهای ذی‌ربط برای لغو ممنوعیت‌های غیرقانونی پرواز به‌طور فعال در جریان است.  در صورت لزوم، اقدامات متقابل غیرنظامی برای…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21227" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:  پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس  اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21226" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پسری ۹ ساله ارمنی‌تبار مسیحی در اورشلیم، پس از آنکه به دلیل دوچرخه‌سواری و استفاده از هدفون در روز عید یوم کیپور مورد اعتراض قرار گرفت، توسط شهرک نشینان یهودی با اسپری فلفل مورد حمله قرار گرفت.
تصاویری که از
کانال ۱۳
اسرائیل پخش شد، نشان می‌داد که این کودک که نامش ویلیام است، پس از این حمله در حال دریافت درمان پزشکی از سوی تکنسین‌های اورژانس در یک آمبولانس است. این درگیری در نزدیکی شهر قدیم رخ داد، زمانی که ویلیام در حال دوچرخه‌سواری و گوش دادن به موسیقی بود.
گزارش‌ها حاکی است که مهاجمان از پسر خواستند هدفون خود را در بیاورد. پس از آنکه او این کار را انجام داد و به زبان انگلیسی صحبت کرد، فریاد زدند: «انگلیسی نه، یهودی‌ها» و سپس مستقیماً اسپری فلفل را به سمت او پاشیدند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21225" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر امور خارجه آذربایجان، بایراموف:
اگرچه دهه‌ها درگیری با ارمنستان تراژدی عظیمی بر مردم ما تحمیل کرد و زخم‌های عمیقی بر سرزمین ما باقی گذاشت، آذربایجان انتخاب کرده است که به آینده نگاه کند و صفحه دشمنی را ورق بزند.
ما صلح را به ارمنستان پیشنهاد دادیم که کاملاً مطابق با هنجارها و اصول حقوق بین‌الملل و مبتنی بر شناخت متقابل و احترام به حاکمیت و یکپارچگی قلمرو یکدیگر است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21224" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!  از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21223" target="_blank">📅 14:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COw8VH-arwr6GsG9Vx-tPH0SGJTRJXODTdm9LEWdcFumbu4Hb_EYgehxyVg8S3nYGL2AcWD8DenV8pUnU_weOnAADQkvz-elbWewCIcxohBkzfBgSBqcFMX7D4NZP_tVwHMiC7kT4HywKpM-fYNbrBPIIACW2UW1XBBI0rKzia2n_fYVzgc_QvecEFad362yZE94CcaKXQ0Yw_LzyLD0iaMINe_GBae0iH8ZPAikPTgGqJTQADEyTIhDEEGmh2R1433Ejlqdqhou7e-l4x69PlE2BMty2fEk2IkYJ2dcxcbN9rHiSINsumY3gWwcs3cQDaRIJ7NVOGTv8x4t4cuD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21222" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKKkNyo29P_xa0A1FkvdYLNQ7DxBdbecysYzYFeIYqhym2DhSQmUkonWoNeYeFMac6CwJECBBHw-KEGTiLB8wZ8Fu0PRMIk7KGrclrFGWMGUO-aNHJyiNB8CCZHTKIhYhmXPFxkMp8uF74UdmfSCvmZug0RzMBGOl4e8h8HxmERxLyBsX7-jh0Q0RpI0t2Dj8WjDJF_pNS6uDkMFIVVsOCCD9IgHzKf4iXab4xl4Fl5N4Dn4QjqAj2RPYUcU7RwfBCQW7LvJdzjVvGj1cvS9GuLpliB9ie0tWP3WIHaZQwaacekKdTkC2JB-jP_mULMADxsowb_FbwdPbBAGxcpsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشاره دوباره ترامپ به تنگه هرمز به عنوان تنگه ترامپ !</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21221" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.  طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21220" target="_blank">📅 08:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=OGNK-JDrH-sIcQJbnHsmp0eVKgNlEPhHALWFfBjSCWQDTWlDfHSPDVUAs8k8pcWpMuovakiPf9hvlzoOq7i9KjRC9KxpM4stDZr7RIZ5Gr94VxcsDQYsn2Cw_R-TaqVM1umrdqs8SUbZYowQQYekPatK-ia5nE1AXU545pYl5G7I21XLpzLFDA8kz-kBy8vUWU5zb4jNgGGCjRf_kBwZIBNGxyCRVNOIbSd4pWGvNp3Km9516D3ieWzUpuBvtCsXA3DNwXq0AqAfW7MU-JB7HwDPIkPCeDDgScZV8hpIneBkgtzgWXUosEtapf1DLSYpyywsPe7m9DUyAkpQM5GniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=OGNK-JDrH-sIcQJbnHsmp0eVKgNlEPhHALWFfBjSCWQDTWlDfHSPDVUAs8k8pcWpMuovakiPf9hvlzoOq7i9KjRC9KxpM4stDZr7RIZ5Gr94VxcsDQYsn2Cw_R-TaqVM1umrdqs8SUbZYowQQYekPatK-ia5nE1AXU545pYl5G7I21XLpzLFDA8kz-kBy8vUWU5zb4jNgGGCjRf_kBwZIBNGxyCRVNOIbSd4pWGvNp3Km9516D3ieWzUpuBvtCsXA3DNwXq0AqAfW7MU-JB7HwDPIkPCeDDgScZV8hpIneBkgtzgWXUosEtapf1DLSYpyywsPe7m9DUyAkpQM5GniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21219" target="_blank">📅 08:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.
طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات هسته‌ای در ازای رفع محاصره بنادر ایران توسط ایالات متحده و کاهش فشارهای اقتصادی بر تهران، از سر گرفته شود.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21218" target="_blank">📅 07:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=ZsInA64IBL4Ybp8omE63RLfU0ZkqUaVms7oAgIhSZY4gJ0b6saObzL2K8XertmWZj9eo82gJXj5bu6gsto8nLROabAfpE9OV_klY_DbvzmhrJOSWhH4kxuOgjsxKjJ6I9JT_6mP6ZFPW0trGLmTzx2Fad9LGFNhsz3EJcY_gkU3bW8l0sFjJncpwVPsACZTmqJLynibUAcd2prKsu-maerC_wA21sJ2h_BfRkNnrCEh2fva3FcAkavP7sjIJCnmrr24PJloXo1-vvcg0ugvyW1CikG2LDu7V7YgHFfIpCOnojaaCCyBckwoooxVbRScCAc5hnDc5JtSZDnqJ8a5CQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=ZsInA64IBL4Ybp8omE63RLfU0ZkqUaVms7oAgIhSZY4gJ0b6saObzL2K8XertmWZj9eo82gJXj5bu6gsto8nLROabAfpE9OV_klY_DbvzmhrJOSWhH4kxuOgjsxKjJ6I9JT_6mP6ZFPW0trGLmTzx2Fad9LGFNhsz3EJcY_gkU3bW8l0sFjJncpwVPsACZTmqJLynibUAcd2prKsu-maerC_wA21sJ2h_BfRkNnrCEh2fva3FcAkavP7sjIJCnmrr24PJloXo1-vvcg0ugvyW1CikG2LDu7V7YgHFfIpCOnojaaCCyBckwoooxVbRScCAc5hnDc5JtSZDnqJ8a5CQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS-mi-KTujBgS-QOCFi8DBNznCjpjAmCnNbILMNx_SaIrh7TtCqrUwFCFLMSRmpf3op4MUrnz1j-5f_8rMCzP-TowJMvIBCKpNxNeErejyG6EW70ari96ipnCdTWG1Zil0MsoiJxaObosLAJjRgCxxzC8VkGXzFBnjhgKczfUC85uYoUuHuYAxAEMm1YyYwi4lUGbXfv5x8-lZH9XNcawW9OHaeijKVjmxiuLITvus1w7EqBRlXvxlZZvaxPXEMmE8c5bfRpprOP2PwB922pg0dBheHcHcxzeDZvpzJMxTmG2Ee1YqJQZ7kDtUYjzpvjRawMEoPGNMFKE2bVy0iXeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من شخصاً هیچ وقت به نزدیک بودن توافق ایران و آمریکا توجه نمی کنم ولی اعتقاد دارم نزدیکی ایران و آمریکا نزدیک است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21208" target="_blank">📅 23:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/21207" target="_blank">📅 22:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2-2sPFpknwXO8eyRItOsytan0L9qCogtI-sS-L6MgmzICdHI0HrJkqJxD1py6taoGiaGOWuJbXFTBQOulgn4sO8jTI5VbMrJn17YsPtZ4b7SgGEWC5W_CsjeqoEsVI2_vGyl7_dmY_6-b5N9vPTzqEmEDuCWnMs5vvUMZg3ghH87cP02cc8hjRe7FljhEj3okWRe8fe-6vLuETFtuideg9Fd2zO2kF9eH8GbMCfNBJD0TM2XKVTaeo86kT6BF0-ezMV6U-ujMmWmRAwmlrEn-Zc3c9-rKxyy4Xx3buHve32pZTqqYALxiP8BI7DUQ9BvZLON2iS1JryJP5uOJSTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21206" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مرندی ذوالاکتاف:
هیچ پیشرفتی در مذاکرات غیرمستقیم با رژیم ترامپ حاصل نشده است. منطقه به سوی تشدید تنش پیش می‌رود، چرا که دیکتاتوری‌های حوزه خلیج فارس که در جنگ علیه ایران همدست بوده‌اند، به توطئه ترامپ و بسنت علیه ملت ایران می‌پیوندند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21205" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPPn7KbEXbloiadYDeBSEvYjQKkvQWkQjOE17tM4usW3bCFDj5hWOlaEfThSoHhlEAKOA04Qj7kG8czb8Q4NuVUgaJC0qfaei61xyXA8K-j1RjcoviXcl_W71Y-GKMuGhP0lnf74rjv5DETG_xqKeA8Vz0nBhVpm_7XiboADcb2AYOg3rM5R4kLeibU89VN5NoSC6_NTWO8fhW5YEP9V5wg2VQ8Am6hiqB2ujhWYYf6d41ocR6RBVl3KNuAdS0J5ZgSVDSlnev-_3p_sHoWg_TG2NNeBw6GeYmKydPbDOiCoKCUZVq8oTIJlbmypyTSFGMDp_epoK2Fv_wGMvPS-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21204" target="_blank">📅 22:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thjdfk5QBBxRzdnKS9pxfylMN3FlgqYumr_ZyQx5CrL8ZyVywsTzwVXHUMcMvqoTPX38QecxKcy0shB46cUBkVOs1x1eqnJ5vPczI-OnAbSIiA0g2SL38q0V-fUMWpYVMpeol1U53DVwgrxxFMkG553BCCa03Mpmch0F5ygG7Vk5YlVNbgVVOBeyyLw3DRmom_-Yd3-3JpwHBx04RefGjM0oFlSuPcKefIsTWciIYLknJLQSk0lQa5dpE3E1FbVPZlMVu9ruAg1vAIqJpvZiIeYUlzPwtBYRmVZnS8X2bUzMmfXhQ1jLres1ycohXkO4BOF6BdcvE2U7Jsw_XCmOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!
از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21203" target="_blank">📅 21:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Ali SharifAzadeh – انتخابات اسرائیل</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/21202" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ
:
در نوامبر در چین دوباره با شی ملاقات خواهیم کرد</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21201" target="_blank">📅 20:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21200" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏ قائم‌پناه:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگر به پایگاه‌ آمریکا در کشور شما حمله نکنیم بلکه به خود کاخ سفید موشک بزنیم.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21199" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سفیر آمریکا در چین:
پکن در پی هشدار ترامپ، بخشی از حمایت‌ها از تهران را متوقف کرده است</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21198" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">میانگین 200 پیپ</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21197" target="_blank">📅 18:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21196" target="_blank">📅 16:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رئیس اسبق سیا:   امکان تصرف خارک برای آمریکا وجود ندارد</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21195" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21194" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
عربستان سعودی ارسال نفت به اروپا را لغو کرد!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21193" target="_blank">📅 16:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21192" target="_blank">📅 16:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21191" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21190" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21189" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:
پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21188" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21187" target="_blank">📅 14:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خاتمی، امام جمعه تهران:
کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21186" target="_blank">📅 14:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GULhlGXsi-OYKvKFYcM_gphMRsE2OQs88is_csPGk3Kgs-O8JUgs65ZdXnWR1t3R_YEk1GUG9vSV5M6_xjmY9Nt-vUp_mIFR_SR4Oli-GrxJ8Cy2csTsWZrxMGcGcTLT-TG7fnZzpVq9dU-UjKssyB1s_YpuppLvZ2axmAmvt1WfzWoJ62GEyu7i5sOd1n9tKJAqs-G1K1ftiALD2IiatdA9HWvfpWHBtnV0jMsOh11LBxAE4FgC1JU9eqqBQkNoBvhlETmOqe_QgYAzJI6NbYoF_1gXg1fVjeJaRh-OQV4MiDEr7LSUK50PDJXvG5vufIV2VNe2yai47j5inchfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.
در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21185" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RjsGu9KvYjA-K8CMnXFI14MEjRIyrHza64tygJVMq0maY9uW6QaoMc58vXYv8yw27BWe-qzWIaPKwC1wt7Bl1WWfDL2uM4WYbWHbKplr_NsC5US5FLjG1JZH6g85TUuuF2YS1EzRknEpQH1rn-tL7r2_hQzRCVJ90WU_7E9bepUhsr10OIzr-1VS4l1NtJ8ivKemmEJvwH3_wM9A9SFMdikoeYzR3unaLXDIQ9hbOcRK_Jhvlc9RLt2pPtyNqJrlyJsQEIrhXSxjGKlbvUTu31wX7E4_Y_JnKSsykcvnA7ukagBIRK3_QbOfgp4Q4Y7BmQqTNyKXEEzbsQPGWiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و هر بالایی فرصت فروش است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21184" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پاکستان، ترکیه و عربستان سعودی در پی افزایش حملات حوثی‌ها به خاک عربستان، یک جلسه اضطراری رؤسای ستاد مشترک را بر اساس پیمان دفاعی مشترک مکه تشکیل می‌دهند.
این جلسه اولین گام در سطح فعال‌سازی تحت این پیمان است که مقرر می‌دارد هرگونه حمله به یکی از اعضا، حمله به هر سه کشور تلقی می‌شود.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21183" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کلمبیا تمام روابط دیپلماتیک خودش با ایران را قطع کرد
دلایل اجازه ندادن به بازرس ها آژانس  بستن تنگه هرمز رعایت نکردن حقوق بشر و .... بود
یکی از دلایل جالبش رابطه ایران با گروه های مواد مخدر  بود</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21182" target="_blank">📅 01:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو:
«آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.
به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.
استعمار؟ لطفاً دست بردارید».</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21180" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=jLHhshoOFs3YXLZNzr-Ond38ZYhLs1fLAge5GvU_eOyMl7BA0emlJI4VD5ezD1_X6-03dPYrtL-qhTB_niCqhkAEg2kJ4cuOzm51baYS51zxEB13w2rFSsVhOcj-Rbx1wxEcIZtjnfS4JiSgWgzny_BapiFPeRAYJlrfmkIgD1KebJp2uo3kg1fC-Rzzl5qdlvWJg-MrvFYbREjppbvhvkKmccHptO7VwZUQ4KyBRH4ReisgRoyKf2KPV8expeozAlwp2fuCc_MDK2CmE43ZiO5n9l0zZ85yDcE4PNB-BGHYuS4cwpSbNsaJgYsEUPrm7X02HcY3mTDE3lBKGC83-aVL4WZy6ytKV4vd1lLCLE-stexixvnwoQdkFQBy3v1Nt3pd3KNbe6fWnYfZS4PZtdaUEbyMEtqRU6kR3yOaUXBjEbX1o6XWZyY6IvQkojBOu6jAOtbbFNmU2D4qUQYaPLYsVoV0AG8oRRGaJyTqwikHUgQP4KeEhpGiQCGzu9-SN2wyr2D7DccIpg8dFF-EBUT_Qbwm_OFhomkZ5PigNrq1glEjZt-j9jiXtOLqXPGja7cGFc4Vq1w9OJWZP3csM02uuBvyn25HcxAGPfCtPYJ8BNK6sdRs49aQfnPPROqRX0feDAGSPkoTlWu-WWt5-ElLYvXgdYVUgcxQ91eeEik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=jLHhshoOFs3YXLZNzr-Ond38ZYhLs1fLAge5GvU_eOyMl7BA0emlJI4VD5ezD1_X6-03dPYrtL-qhTB_niCqhkAEg2kJ4cuOzm51baYS51zxEB13w2rFSsVhOcj-Rbx1wxEcIZtjnfS4JiSgWgzny_BapiFPeRAYJlrfmkIgD1KebJp2uo3kg1fC-Rzzl5qdlvWJg-MrvFYbREjppbvhvkKmccHptO7VwZUQ4KyBRH4ReisgRoyKf2KPV8expeozAlwp2fuCc_MDK2CmE43ZiO5n9l0zZ85yDcE4PNB-BGHYuS4cwpSbNsaJgYsEUPrm7X02HcY3mTDE3lBKGC83-aVL4WZy6ytKV4vd1lLCLE-stexixvnwoQdkFQBy3v1Nt3pd3KNbe6fWnYfZS4PZtdaUEbyMEtqRU6kR3yOaUXBjEbX1o6XWZyY6IvQkojBOu6jAOtbbFNmU2D4qUQYaPLYsVoV0AG8oRRGaJyTqwikHUgQP4KeEhpGiQCGzu9-SN2wyr2D7DccIpg8dFF-EBUT_Qbwm_OFhomkZ5PigNrq1glEjZt-j9jiXtOLqXPGja7cGFc4Vq1w9OJWZP3csM02uuBvyn25HcxAGPfCtPYJ8BNK6sdRs49aQfnPPROqRX0feDAGSPkoTlWu-WWt5-ElLYvXgdYVUgcxQ91eeEik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک موزیک ویدیوی Erotic از اتحاد عربستان و فاکستان ببینید شب جمعه ای دلتان باز شود!</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21179" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز:   آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21178" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رویترز:
آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21177" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اسرائیل می‌گوید حملات جدید علیه ایران «مسئله‌ای زمان» است و تأسیسات هسته‌ای ممکن است مجدداً هدف قرار گیرند.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21176" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udyODfrCp1Z20KGFgNL0a_CQPn1KDE8iys3MegSIXQkwqTEL81HF2cLGwimUr5quVyNMKl4UDhPE1PaAcs0yQOfj7U-dGgOYf3hMm0Z4G2PMWvGbEYNEEq5obzrjg27zqc7FXB_xQy5VNw-3oCu6ZK9O585cQ_nIGMCUo5Jd3101nk6R1au6rO0vtQTpU0uq8BKtxcsfb4nWfdUvrTL2ZAs7c0kL2gcvMR7NQiKzwnQQ46Kd4UCZjFY_admeqWPCh0H2ww1YbkN9Vs07G69bInuKtGMDP9leHUUqWkvCqbmA-NKwX8HfoLV1hTmhegiUFqGqU4ECdoNc-E3iSjXY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.  علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21170" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
مصادره ۶ میلیون بشکه نفت ایران توسط آمریکا
تانکر ترکرز مدعی شد:
نزدیک به شش میلیون بشکه نفت خام ایران (به ارزش تقریبی ۶۰۰ میلیون دلار) که توقیف شده، بی‌سروصدا در حال عبور از اقیانوس اطلس به سمت ایالات متحده آمریکا است.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21169" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=EyG_y1xo4dWRml_vT_9JvFYcFBtLtorWPD1ispFdY5evxVRNhEQcGo4Rjh9_OE4A4MehkNiahfYGpOVmalchspr1jwuQvUvJx9UhcxJGzC8rtm8xnZ1M16P7hbrVMM58MfRXFxEji0lvb9cQqMk-KjQeJNf7uo6GCD_2l4CTMiwmXVIuZisywUXAfLoBhvdhWKNC3zcluZ5gUUR2IQ0chJIl1x3TVJC2LkJ8PcD-_zLs1fODLj0vEPw2p-ABxAHxfGIE6iNBlsHyyMtK3KRTXuDyXngv0PKSoUnroelVao65meKYJ0EpjJlAoi-n_EanVFTBgfNETk_BoWvoaA2jdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=EyG_y1xo4dWRml_vT_9JvFYcFBtLtorWPD1ispFdY5evxVRNhEQcGo4Rjh9_OE4A4MehkNiahfYGpOVmalchspr1jwuQvUvJx9UhcxJGzC8rtm8xnZ1M16P7hbrVMM58MfRXFxEji0lvb9cQqMk-KjQeJNf7uo6GCD_2l4CTMiwmXVIuZisywUXAfLoBhvdhWKNC3zcluZ5gUUR2IQ0chJIl1x3TVJC2LkJ8PcD-_zLs1fODLj0vEPw2p-ABxAHxfGIE6iNBlsHyyMtK3KRTXuDyXngv0PKSoUnroelVao65meKYJ0EpjJlAoi-n_EanVFTBgfNETk_BoWvoaA2jdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRho7ShDYZnfDo8f3sS7kwWOOv1h4aS0U6w9NH6utZ2htY039emUlFCMb6y-eDU2NwBo4PKu-1qgzPelOkwXL5FQU6v4k8UI8clUJsmi8o9PMrRggv1ySHYWYdq97z_XotR-UF9CGP6I-QgaEepzr8_me0UKw4vvbvUIHwQYqxgsdhAvCpMx3Y6PONrYltiDWqLrFiq65b7VMiXWnCEj4c06muOxYYDpVTMxviWsMhbZEZvtxaed5k9iHHIEL24IIwycBaZAVbmRthGtwFWhIO6DUiXTiKCjsGUtsKEaT-1Mk4X7WnqbYrwjXggKTHcuVX64uyAt7hY2Tud9LXabhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBrLABf_LBF1cbHZgk375mG4k20G46mJPb0y-7ka9Vlq7fySLkkTVM7klTWai6L36RxU_156YKKBgtDqsRcVb21Y-K4Jt_AT9sfSjfCqFktqJzSllUsTK79Kp7df-qqHIuj4aIanGxRxTaPK5O_a0eM0qqwslY-XBuWWnz_RTnURkcnbfNQyvH5gewU-RE-z8sR4Y1xux-59lv_kYdd5fH8TN9us-UwZTXGagPTf_ckvxvoMt9foVXVZrhqtwYqKRNK7LxhqrUTw9D1b3DWB8uHSrJLyKHmU71t6tgEi46QD_pnwNzqxJ9H1N08fGnWSG1eIXU-rVDQYdeRNxo_-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4DscAxTah53OJvW-EkztBvmV8M4manfxy17irtYri1ArJ9rQouv5EDFJxgMNa9-VjnClpIqiQjGzvMuBeDZ4kZVWdDP8CrIky-QOBG5C6EVZnpF8VXGpSp1aaEHNFWAnS4NoAViQb-HQ0YzFSGg5jTluGScmETmAn2uKdocyMY-9nU0gAzk02bM5yNHFI-q8vHCLF4T_YvpE0EO1tcQdpmWHLe1rIkPsZmDo9DznQGqTCUSpa4KZhYYSZ0I_Ug8o3plfe3JiMmfrf1GI82zT7abSxKnhfwQSDZm4NL7py8SlCLS7IaTEBsIdGPzklhA4n-e5xAYDDwGS-MOKUjZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uddg5MaC3k2FPFWBHSG2RtwvFxx2DLwux7l866a7cay_WIxqwcOcaWMRgIVdEqGQ99adFM233Ts4t5LZwUtE9UT5ZrinxDa8AqlSHdFF2JanZO8Z2rVA-4hL4eHCR3vtZb_EosQSbAde_s-HmXBkh5KJDCuHMJ-MH8OoNTqTbqPXlRaNmrqx4EAhkX48Huiuqzm3N7oraBJlvNx0jhSVMXREKSpigqw5yuJO18_8ild-e68FNnIxb6XCcRkWWeqJYV7gFnABzUKVGDYSbpT4-G38wpl8nQcvUQc2gOwGoZAccwsRcqKY0XsI6AnxASgPnQit8O0_-ECAUYkAZAg3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJSa2qV-VjAaKGqx1a8XVge9nxdmGBiRU5IdxxxsDTu-YHx_kgsAenhNnaZQ78bzJYvUqBTrTFgfh0R9TkvvdXwOtY_vNHtgVAJOvMzfigI0iQe5NPtOzIy_ZTn-JZ4D5EQNBvsnFmnPoemUM6R9-cGqf-S6hjf_UiVNTwZYo-eXj4lGq3m2qlTL4LhsNb2mvXJV1MFunwnCxPe-KMI34M_tHnkkeuFjqfaRO_nYbyILTPZoDAKeNORK73yOjJrSGTRDMJZDdaOSA4LPRxtigmSF1976b5CqYEJHMtk-3jvyPOM5lLAOYMhkUFfS7bTa443c3wATTsP6AaZ6dQiQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21142" target="_blank">📅 16:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21141" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwG11m-6iWlN1JE4GecAJDVtqAuh3D3o0-rEfXbv-MGaZh1t42te1merKUKBkvymWwzSfDkQRlG2iYXrPbkNuOlOIOmcRXVjEmlt5k9ZODCxAFncIRXxg0CxKbeEEGAOUX0BuWnYgGawEMUlx1drFnffITSMX471-tnGvNCUkrMHZVzytM_buIMXDUBRZizx9l25JtrA1v9lwUu76K3VLS74k860icg9GefP6NsL4hJri6oCTkPaa36fWvcr6TANcELTYo2P_2CZZ1geSrn8Yhu0_mQivvXSMczw6EW2RU3nISQNcroPDMYnZjV4bfeBm5032Np_PkWm5zzrBla8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باربی های وطنی به مقر سازمان ملل متحد وارد شدند!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21140" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21139" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
