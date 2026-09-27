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
<img src="https://cdn4.telesco.pe/file/EEYd5NW1G8miKwObW-FhR-PWt4cD3XvgYjEsGP3akvV8E28A39xM9wcSEhdLfIOVdbAZXj-lhTEwLIO7kW7fbqISQOVxUqtnDpfFNaFYrC6TsKGSTo_ropdtclJ0732rH7OqztYCs-7qB1974zdgHUHMe32Xep5rUHGOAFmp50ldMEiX8xvG5jwqLFurKYCZBbNJyTqcNd0UrE4f_0UIq8TYCKDlEP-Mio8Gq5ioCKmbIvO8kwSKbDhFRPYbQdYqCFEzKcFqyEPaioJ5nRFMw2Q_mHyrdvSwGPvGtRK3XHBNpJq1MNzmEDS7x1iUZqi3-mhBQ4GRzOlyF5EfTJjn6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:  ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس  نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در…</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/21243" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:
ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در آن غرق شد؟ آیا آمریکا در منطقه و در تنگه هرمز در نبرد با ملتی که خدایی فکر می‌کند و توحیدی فکر می‌کند غرق نخواهد شد؟ دیپلماسی با قدرت امکان‌پذیر است و ما باید حرفمان را از قدرت و اقتدار و جایگاه قدرت اقتدار بزنیم.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/21242" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باز هم تاکید میکنم خواهرمیانه جای مبتدی ها نیست :
حکم ۱۰ ماه زندان حمید رسایی اجرا می‌شود</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/21241" target="_blank">📅 12:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7n_VT9iISkua7NBm6q_RybfqY5Su7MBqNlpzLTEVQyLS_BXBbZS4e4ockPkjTf1grVA9WTADybIZ75gzG78Dsp5MRKThas4-Zy78MkGPwWRypsetzVhzCQUgesk7Ckui1LwVfO-rN9vZ6fx-Xt51KhAUm4mCsWeABiOrC0u_RZ3h5fiGXPrg12WoOfA5EpFv7vzIfUhF8Aevwx_UGHG-OCk2jGJSdwHVVZCK7ILP2IAI1Fm3jDDwBLQZj_zok7Prp47MAexVyd_PfZFNf8flALx-IVq2TKEWJlk4nQfzNak--apkXXkPufDCzte0fHqvXv94RiffbnniRt4bwZc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهرمیانه برای مبتدی ها نیست!</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/21240" target="_blank">📅 12:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک نفر دایرکت داده خب استاد ما که به قله رسیده و سرش نشسته ایم، حالا اگر پنبه نایاب شد بیاییم خود قله را آغشته به روغن بنفشه کنیم!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/21237" target="_blank">📅 09:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترسم این است که پنبه هم نایاب شود؛ آن وقت با چی روغن بنفشه را داخل آنجایمان قرار بدهیم؟!  اصلاً آدم یک جوری می شود!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21236" target="_blank">📅 09:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شیوه درست استفاده از روغن بنفشه</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/21235" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=PGUW7fnOWkYEhUDBdBwuNeuAYGQseE1k4X15ZJpvq-GEKaxMA3wQWznlwWa_zP1AZ8UL9e5--i7fjCovkVi1G6cOpvBRZhnncOmSF0WY0-i1YaiGAOCimqHDBVmqygeRNJ0hsFHSR7U79txe_I99SAahmuL4ujFKvHgGHjGHTXDeAd1mQXRIlQAYxEH15z7aj_-LfxkXFYvrRndUYZ7-xRxKrkespOCj1fHaC52vWobF32xaJR2uR3NE8UVuZZ85AiIXEE9GJDa9qZp2kCj3gUBOXlS73mTmMvGXuROgm3lpiAthhaOG0VLwInre_QYMMEVlmpnd8nzYouElQdf-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=PGUW7fnOWkYEhUDBdBwuNeuAYGQseE1k4X15ZJpvq-GEKaxMA3wQWznlwWa_zP1AZ8UL9e5--i7fjCovkVi1G6cOpvBRZhnncOmSF0WY0-i1YaiGAOCimqHDBVmqygeRNJ0hsFHSR7U79txe_I99SAahmuL4ujFKvHgGHjGHTXDeAd1mQXRIlQAYxEH15z7aj_-LfxkXFYvrRndUYZ7-xRxKrkespOCj1fHaC52vWobF32xaJR2uR3NE8UVuZZ85AiIXEE9GJDa9qZp2kCj3gUBOXlS73mTmMvGXuROgm3lpiAthhaOG0VLwInre_QYMMEVlmpnd8nzYouElQdf-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.  در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21234" target="_blank">📅 08:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZR2R3BXR9ojj7XnTPt5RCpzIwHIVbUfi5wtfUzDN3med5MoW7bOrymHaQhh7zbpVmYHZ4AXQUTv8uTjUkLI2Nq4mVZyNOgRTtdaLqFUyQFZAginAwjZyyln67mqDUnMrEPZFQN_lMeFugH5qx5Y7MLIJCfXYv2zCgHulendpfDVge6mqHQADigMxN-bkVm1TBhnsiBvFTjm2AQwJxpp0z2BacQFGxLM9KHHjfLTX4JARdtolVqhIrdd55OCxs3qop-HgAR8NMt0UffgrvrrDMAVyT5W0V-Ije0oOL0V-1HU3bNU9dimAoRKbawha5c_j8UU_wcFBpYmElEohIQTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.
در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/21233" target="_blank">📅 08:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بوی محاصره زمینی می آید…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21232" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حملات موشکی گسترده سپاه در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/21231" target="_blank">📅 07:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FL3KT-dWbnkz-jIjsBwL2vVnVbhNv-vnJyVxc-GwtnutvK1vVQNdpizB7qGuI2goYaW6uRuTvk22vV5Z8-ECf5C6t9khoQKdn3D4SnBdyLBmPWBShpB_CZGz-st9GWerwj09QqA6wlc12Fj9aXioJQfHrjpbTb31gfOO9qcTgvGmntx_98kEeVp3yXqmBz0ThVvlHO_rmFyFAdd2qoYiWuFExJfYosMznxM3kcykGU7tgmFTu2Yg06y26dy0ou1DMSRkABIqSdFxkgK30A_uQlFWd98l3i8NhCPesQmRB-0YHxLLtVl68jaSZGakg4sQG3eXwBfai9wIKsMU0I4uJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه
فرودگاه نجف عراق که اجازه پرواز به هواپیماهای ایرانی رو نمیده ،
توسط جمهوری اسلامی ساخته شده
😄
شب خوش!
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/21230" target="_blank">📅 01:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">واشنگتن و پکن؛ پیام مشترک درباره ایران و تنگه هرمز
در یکی از قابل‌توجه‌ترین بخش‌های دیدار اخیر دونالد ترامپ و شی جین‌پینگ، موضوع ایران نیز در گفت‌وگوهای دو رهبر مطرح شد؛ موضوعی که می‌تواند برای تهران و به‌ویژه آینده تنگه هرمز اهمیت ژئوپلیتیکی قابل‌توجهی داشته باشد.
بر اساس فکت‌شیت منتشرشده از سوی کاخ سفید، ترامپ و شی درباره نگرانی‌های جهانی از جمله ایران گفت‌وگو کردند و بر دو اصل تأکید داشتند: ایران نباید به سلاح هسته‌ای دست پیدا کند و هیچ کشور یا نهادی نباید برای عبور از آبراه‌های بین‌المللی عوارض تعیین کند.
اگرچه در متن جدید نام «تنگه هرمز» به‌طور مستقیم ذکر نشده، اما این بند در شرایط کنونی به‌وضوح با مناقشه هرمز ارتباط پیدا می‌کند. اهمیت موضوع زمانی بیشتر می‌شود که بدانیم در مواضع قبلی واشنگتن و پکن، مسئله بازگشایی هرمز و مخالفت با دریافت عوارض برای عبور کشتی‌ها صراحتاً مطرح شده بود.
از منظر تهران، نکته مهم صرفاً محتوای این دو موضع نیست؛ بلکه هم‌زمانی مواضع واشنگتن و پکن اهمیت بیشتری دارد. چین بزرگ‌ترین خریدار نفت ایران و یکی از مهم‌ترین شرکای اقتصادی تهران است و در بسیاری از پرونده‌های ژئوپلیتیکی در برابر فشارهای آمریکا موضع متفاوتی داشته است. بنابراین هم‌صدایی آمریکا و چین درباره اصول مرتبط با هرمز می‌تواند فضای مانور دیپلماتیک ایران را محدودتر کند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21229" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21228">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibXgYLbR22wuxeU4Hrp7KyPAHl_Ew9MK49VNHQMLniPyotPmn58O8_9jNSbuia_MxN-IZ9bViMLK0WQAKQzaKFagCEQmMN5dtsgKOSMR-bCz7yf2bXg64z58VMmAYK8_6SdkCnfUDU5Pk1xKzgN-9fJn4sVdJ-LzhjV6H88aqBdufJizyme4AHTCSS41c9ACKeuHYkWBSmEkQmDSTPm7znCOUdax2_AvjnCGhRFs_XOSECe8TLYRmSKdrj4UtlRo0D8xSHZwPCX0oz65bIAxMk2ZonXakPK4QmKIe6xjB7C4KE8O9znaWREGEVylVsXfMB6_xTiRlRwXSSgpJyoaaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عملیات انتقال کشتی‌به‌کشتی (STS) در دریای عمان نسبت به سطح ماه فوریه، ده برابر شده است.
تولیدکنندگان نفت را بارگیری کرده و با عبور از تنگه هرمز از طریق مسیری جایگزین که امنیت آن توسط ارتش آمریکا در نزدیکی سواحل عمان تأمین می‌شود، محموله‌ها را برای تحویل به خریداران نهایی به کشتی‌های بزرگ‌تر منتقل می‌کنند.</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21228" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شورای عالی امنیت ملی:  «ادعاهایی مبنی بر اینکه ایران به محدودیت‌های اخیر هوایی با اقدام نظامی پاسخ خواهد داد، نادرست است.  مذاکرات با کشورهای ذی‌ربط برای لغو ممنوعیت‌های غیرقانونی پرواز به‌طور فعال در جریان است.  در صورت لزوم، اقدامات متقابل غیرنظامی برای…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21227" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:  پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس  اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21226" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پسری ۹ ساله ارمنی‌تبار مسیحی در اورشلیم، پس از آنکه به دلیل دوچرخه‌سواری و استفاده از هدفون در روز عید یوم کیپور مورد اعتراض قرار گرفت، توسط شهرک نشینان یهودی با اسپری فلفل مورد حمله قرار گرفت.
تصاویری که از
کانال ۱۳
اسرائیل پخش شد، نشان می‌داد که این کودک که نامش ویلیام است، پس از این حمله در حال دریافت درمان پزشکی از سوی تکنسین‌های اورژانس در یک آمبولانس است. این درگیری در نزدیکی شهر قدیم رخ داد، زمانی که ویلیام در حال دوچرخه‌سواری و گوش دادن به موسیقی بود.
گزارش‌ها حاکی است که مهاجمان از پسر خواستند هدفون خود را در بیاورد. پس از آنکه او این کار را انجام داد و به زبان انگلیسی صحبت کرد، فریاد زدند: «انگلیسی نه، یهودی‌ها» و سپس مستقیماً اسپری فلفل را به سمت او پاشیدند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21225" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر امور خارجه آذربایجان، بایراموف:
اگرچه دهه‌ها درگیری با ارمنستان تراژدی عظیمی بر مردم ما تحمیل کرد و زخم‌های عمیقی بر سرزمین ما باقی گذاشت، آذربایجان انتخاب کرده است که به آینده نگاه کند و صفحه دشمنی را ورق بزند.
ما صلح را به ارمنستان پیشنهاد دادیم که کاملاً مطابق با هنجارها و اصول حقوق بین‌الملل و مبتنی بر شناخت متقابل و احترام به حاکمیت و یکپارچگی قلمرو یکدیگر است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21224" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!  از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21223" target="_blank">📅 14:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpyziqwKEyLPUo4jywjpiCGfFEW_c73g3VQcYAswcC2flpMpfI0iXygUk1AYGIZorhl4J_JjM97b-sdlD_xzqKN9TvdGeC-I-DDASSrSzdSJbUcvRg2ypJupZLcOZCycQmPlBBvpHmHvLcp7kw_HjamLGaZDusxiPL-ynVO7FaH-YaIOnOFRe4TW9wqOe5Z2CQI3rlmiqTQr9i0bNOI2AbF4nmP8934IMjThKhtBikEOgoChq3r9IisuNz5DCfGKWwcD_LSo6reGTvQ_fsz7MfA6CDE8klnCLRVVpVcrMjdxhy4FV6uSIEqaok3e7At4uiDBpUlCDGw8bgdkpe2rOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21222" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDFbf33OHIKhrMKqKT34qAo1TDRTZxhDhS3CqTAKaTDVK4ti_ZYfCqr3NScOjn92Av73QRlCokIcEvsEEEgr62R6rvGsP0fwUbEDDesj3qwK-_CMIKrO4RCC2yO2bTRZKb3_xjOKQnGs8MlL5En1ZYSt5HjmgSm0L5-xpxUMH1OMYTkEIsBMH56lYax5b1sVsvdAx8Efl1_UL8XObLYx0dkHyzyVvw8KAPxK5HWKJ8Y-IuYi2IIXI-oTfTjrtVLFvjgBCpYrmFZIauj1NExKmIaTi29g-aP9zu-HPF58CbyQJIwPc_eVfEEOzB3tiDrgk9iKQfIvW4v0QO4u6EirzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشاره دوباره ترامپ به تنگه هرمز به عنوان تنگه ترامپ !</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21221" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.  طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21220" target="_blank">📅 08:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=J5-P1RMjl_P4Wxvb-c9oFhLBCZiwJLvQCj76g8h1fmV8nFsuWNXS0n3VHOqKXG4lyXhymTIuwaFzC0w4ANEmCP781KvVEVkYI5La3Dy2WIM3N_pQVzBRqPhhoDbqmYsBBhUOPn6pKZlBoaOswlRdoGl0JPka0-ER7maRGj-bMHweCoL3kDPoRygX_Sjy6brxIVsbaxdzV8TKBTJdunjZ7kfRv86lcoyhRo6LyvZ2K8GXL37-1uSeJe9gmaNulsX_SLUYflCBtQJ_IR4WaK57XW0OogkGG6RjxfDux_zrKNyZTDFbq4X9-w87sKF157-fRnVT2a26KnB7kGsmMU4OHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=J5-P1RMjl_P4Wxvb-c9oFhLBCZiwJLvQCj76g8h1fmV8nFsuWNXS0n3VHOqKXG4lyXhymTIuwaFzC0w4ANEmCP781KvVEVkYI5La3Dy2WIM3N_pQVzBRqPhhoDbqmYsBBhUOPn6pKZlBoaOswlRdoGl0JPka0-ER7maRGj-bMHweCoL3kDPoRygX_Sjy6brxIVsbaxdzV8TKBTJdunjZ7kfRv86lcoyhRo6LyvZ2K8GXL37-1uSeJe9gmaNulsX_SLUYflCBtQJ_IR4WaK57XW0OogkGG6RjxfDux_zrKNyZTDFbq4X9-w87sKF157-fRnVT2a26KnB7kGsmMU4OHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21219" target="_blank">📅 08:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.
طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات هسته‌ای در ازای رفع محاصره بنادر ایران توسط ایالات متحده و کاهش فشارهای اقتصادی بر تهران، از سر گرفته شود.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21218" target="_blank">📅 07:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=BHjAQpBO4U9jzFerbAFpRHl6hSi-SRdRgm4Ym4ws3CkPT2ka93J7NgwytOUajt0cfBAFDqxnbqaTVCwixxtCLslB_nHUUs2TrP7B--0eJG-3wgipxDLRwHHJNrngBfc6afg0yQ4CGPd5GIsHQN6sb18uDLrSCvOl8o5FVKInJNhNtzeMOi-hdiFeaWFXvQg7xwyoGD0f2nRsNQvEff6sq8MdslsSP_umBw3mhj8brcGEitgJemAB9k_dAUIy3JNSJ0sy09WaS9wU8my-8kARvN0N1We9nDLxB86OCJcWkM_0k7NHcUEsNrn6sRWuacsw5hi0J526vRm0l6mpyDWPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=BHjAQpBO4U9jzFerbAFpRHl6hSi-SRdRgm4Ym4ws3CkPT2ka93J7NgwytOUajt0cfBAFDqxnbqaTVCwixxtCLslB_nHUUs2TrP7B--0eJG-3wgipxDLRwHHJNrngBfc6afg0yQ4CGPd5GIsHQN6sb18uDLrSCvOl8o5FVKInJNhNtzeMOi-hdiFeaWFXvQg7xwyoGD0f2nRsNQvEff6sq8MdslsSP_umBw3mhj8brcGEitgJemAB9k_dAUIy3JNSJ0sy09WaS9wU8my-8kARvN0N1We9nDLxB86OCJcWkM_0k7NHcUEsNrn6sRWuacsw5hi0J526vRm0l6mpyDWPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGz565h_Juc719HjMe_iGHc7kyoLkiyZGXuQjJiSgqwmVc5ngzj1MP7cFoMSOrch6SB3OyHyg8KkvE7wr8zaZtvnjoy4PfdO_RWi0kSMIQUuq8InmUhupAinsnQBb10wzcojLJbvwPMlaBzpohk23cW3O4axLxGPVv0XveyQ8Ax-x7M7alPrL8DuN_d88ckHL8j8nGssm0lD-MlytXeofIEijuXPOhQB3d0kqoOn8DPQXDe-7OEWSsS7SoOzF6tHdD03ysf327KLyzph3wg_zF9e6QY2jXDx2molTmRdkoK0DnWWCk4XnADfnX6vpc_O0fcl5NNVOaG5GJMmaXUBiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من شخصاً هیچ وقت به نزدیک بودن توافق ایران و آمریکا توجه نمی کنم ولی اعتقاد دارم نزدیکی ایران و آمریکا نزدیک است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21208" target="_blank">📅 23:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21207" target="_blank">📅 22:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzmT582MTFhAIUKn5_v25RYGgkvpPX62PtHVWfS-Ki0w4OLacOdYMXZgTAHfN49lvIa_I4DGN9tYhP6veoBO8oYoH0Oc9OEU_Wvl3ecm2EsGbIOKBZgXKhAuX2kALAGRFtd66aw6TrBxaeNumnWbpiVGDJQ7guCM0pvKoFq2WwUZ264_i2u1hvB1n4ZTm_CSadLYkNR4PxkhPpToMvuux-aokqSMOoYkcXSC80XOqVRJkiNRpTgN0OwHQPKfGxeSnplJrauh04ClBG33nYI6kv4Fz09k_PFzKMYQwHEPCh2_-4FRd2ysZnVfhElVbaOT9EapfrT1Xm5ofYPRfszeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21206" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مرندی ذوالاکتاف:
هیچ پیشرفتی در مذاکرات غیرمستقیم با رژیم ترامپ حاصل نشده است. منطقه به سوی تشدید تنش پیش می‌رود، چرا که دیکتاتوری‌های حوزه خلیج فارس که در جنگ علیه ایران همدست بوده‌اند، به توطئه ترامپ و بسنت علیه ملت ایران می‌پیوندند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21205" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLEfdA3jNVJDy1xuSR_oHjiTxSq9OqXae4XqdE0RtTmYAdcBahIEeyJ14k_vmZyO5mgNalb7v61iDBf3S02tBneml_vEorgE9zV9nB04t-3D3zlQ39gUZLAkWwrqRqZRNUNTAeUBaPY6st7UarVPFJxlJxwgruINobSSCOGSqOd0rZDllYrgZbgP_w1cnAsPicD13jXopaE7INqIbkmKRtB5RtMCTt28a4T5ID0imc2EYGxgVVPB83LLguBmLlF09es5ioqD6eCsxejiFCyCNSO8_W_kPzS2PWq748JNbR0ToWtoXXJvNSEbOTdZsIktcKWmziQ4Vjw30zHea3octw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21204" target="_blank">📅 22:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzApDgQFHrujSJOt6IBnWQYlJCoIooA-ERDw1qXgV_4nWaN8xKV8-ShZCnWF2BeGI3UpW_QaGpc-0HQeDvIcFQZTGxnend88MV6dAwZBPuj8XxseBi7HfSWGaA8KLQDp3dRr31eV8efZd8ma9PQ3OSIL9rah2cj4uIgS38e0FxLG75jwVsebMuz9eyORS4skGda12QeKi2X72vBs65cSJsvlviO02gXacBZIBtPmyEQyUzHtp0La1nqOSJkGwrmiivWcSMs2HNTjimzEJqZkj61pmvrbifUjrH9uNsRx3AHgWrzMI-GjZquCPisPE8a6j7ABzpuWNOQXKjZABdxdGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!
از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21203" target="_blank">📅 21:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Ali SharifAzadeh – انتخابات اسرائیل</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21202" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ
:
در نوامبر در چین دوباره با شی ملاقات خواهیم کرد</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21201" target="_blank">📅 20:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21200" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏ قائم‌پناه:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگر به پایگاه‌ آمریکا در کشور شما حمله نکنیم بلکه به خود کاخ سفید موشک بزنیم.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21199" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سفیر آمریکا در چین:
پکن در پی هشدار ترامپ، بخشی از حمایت‌ها از تهران را متوقف کرده است</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21198" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">میانگین 200 پیپ</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21197" target="_blank">📅 18:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21196" target="_blank">📅 16:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رئیس اسبق سیا:   امکان تصرف خارک برای آمریکا وجود ندارد</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21195" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21194" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
عربستان سعودی ارسال نفت به اروپا را لغو کرد!</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21193" target="_blank">📅 16:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21192" target="_blank">📅 16:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21191" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21190" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21189" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:
پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21188" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21187" target="_blank">📅 14:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خاتمی، امام جمعه تهران:
کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21186" target="_blank">📅 14:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5tz33-R6gBrD7C-wM7E-TzZoNkx_Xb7UKF3J7yPo0WcXCq08ebcvRPYX324IMVk4DjnAdcOR0pg_jDFosyQNWlXdxMD_TyfLBSJvnQQqtI8Tzj5RoztePYhUqIPuWOLXpebMf_fmqb51U0BAY94llZuyRnkQn9OJHO41lG8HnEiCAKOTnG4FUgR5QCB99slR0uoFjwgfKuRqutZ3E1ZVpQBK-NU9yNV4DCjVtPXJOtc0RI85z2pOzqZJDZs6O3VA8LyecBzzeMvBrpbMqxCzFRP7ekG1qsNdHpHw8Dj46y0TuXGSt763lnvdLiya44Hnk17OgGbCIXJFzGHf9hinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.
در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21185" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYv0bvJPA-AqVMq6JuqfO_Jl5yeAYHL4aLZAPi3UlJ5EjsulMpC6EMGd_KKjXL0xJOhsuLyVO_5Pby7SgAo6wNi6WxLlx2Y9o_3MwGN2GB3vFsdvluS73wE3a2syWRIS1KPs_7FG6RKm4Zrbl-z6HyIdwW-LjogryUciZ3Z2UyQLFK6WVT0RW4GjtdpUG92Q5vqI4Lymtmg1xJfrSfsPI0PkonGkD4FFuKyCY4MdN0rudkS1HkP3ZPoAqUr3Le8WxXlIU91hPJmG1v5oZi4--Q_Vqf1r1AWSxCceUGfvtMHde_Dn_OAiII919BNbmxHRYyXaxj9ETiYfSZwyfwTo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و هر بالایی فرصت فروش است.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21184" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پاکستان، ترکیه و عربستان سعودی در پی افزایش حملات حوثی‌ها به خاک عربستان، یک جلسه اضطراری رؤسای ستاد مشترک را بر اساس پیمان دفاعی مشترک مکه تشکیل می‌دهند.
این جلسه اولین گام در سطح فعال‌سازی تحت این پیمان است که مقرر می‌دارد هرگونه حمله به یکی از اعضا، حمله به هر سه کشور تلقی می‌شود.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21183" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کلمبیا تمام روابط دیپلماتیک خودش با ایران را قطع کرد
دلایل اجازه ندادن به بازرس ها آژانس  بستن تنگه هرمز رعایت نکردن حقوق بشر و .... بود
یکی از دلایل جالبش رابطه ایران با گروه های مواد مخدر  بود</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/21182" target="_blank">📅 01:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نتانیاهو:
«آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.
به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.
استعمار؟ لطفاً دست بردارید».</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21180" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=q3dpepLSXdCR-Qyx3voTDMJkSvCF8XzmlFnBbtMgCH-nmoWXhQcRJRSVPBW0U99FSvWg-cu_oYvLzqculIV-q4YS8jRhboIL_C1mh7H3ekP1Q0r6H976ZGWTkEw_xasfJvyg-IxbrKMtfqFBiBCmE1LXLxnm_8Q2aNAYo1yLaZsM3VhLsi9fJTAQCzzbV3c6O3yJf4G8cwGrdxNWTsRI6EhiEr86tq7rKq1Ql5R5Ft8VCGeY3kfzNRIU429JGj1lq0JMML5ZrdtEglJ5OdzoVIeWvSGXlSnv9Bl-ver0VE5uaarHm0gnsEbOKMkQVxshM-5b5NMv4YP-UFtxOnjjmxPDiVyJT0IU_LWmBkIiD-YHmxQNfFHkNwf2pGaI5iOZYRZ0pDxxYMbCBc7CYwu_IBxNpCF-QISOIfZrw6WOqlq8us8TCLknKrcG6oWz79XnwnP1vie7EU-dBDbYlnU-C4-ehYcLeFJC8Gf_qZXkiry9vmXYUPyKg6oknOAFwnQ0McUE3zYEvzD_BRNHnX3st3MHhzLI-0ZccsrASVdB-m_bQnrpvx3pzrKWKzL8X6DN0_hFRhxYKZldSryPL-QwnJb05eOBdz0yx96nqRc9cde4lWofD9006jIKPwXUMxbj1ZBf2nX9-p3Enw1f1f2wLW9AT971n650PbL-0F87zDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=q3dpepLSXdCR-Qyx3voTDMJkSvCF8XzmlFnBbtMgCH-nmoWXhQcRJRSVPBW0U99FSvWg-cu_oYvLzqculIV-q4YS8jRhboIL_C1mh7H3ekP1Q0r6H976ZGWTkEw_xasfJvyg-IxbrKMtfqFBiBCmE1LXLxnm_8Q2aNAYo1yLaZsM3VhLsi9fJTAQCzzbV3c6O3yJf4G8cwGrdxNWTsRI6EhiEr86tq7rKq1Ql5R5Ft8VCGeY3kfzNRIU429JGj1lq0JMML5ZrdtEglJ5OdzoVIeWvSGXlSnv9Bl-ver0VE5uaarHm0gnsEbOKMkQVxshM-5b5NMv4YP-UFtxOnjjmxPDiVyJT0IU_LWmBkIiD-YHmxQNfFHkNwf2pGaI5iOZYRZ0pDxxYMbCBc7CYwu_IBxNpCF-QISOIfZrw6WOqlq8us8TCLknKrcG6oWz79XnwnP1vie7EU-dBDbYlnU-C4-ehYcLeFJC8Gf_qZXkiry9vmXYUPyKg6oknOAFwnQ0McUE3zYEvzD_BRNHnX3st3MHhzLI-0ZccsrASVdB-m_bQnrpvx3pzrKWKzL8X6DN0_hFRhxYKZldSryPL-QwnJb05eOBdz0yx96nqRc9cde4lWofD9006jIKPwXUMxbj1ZBf2nX9-p3Enw1f1f2wLW9AT971n650PbL-0F87zDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک موزیک ویدیوی Erotic از اتحاد عربستان و فاکستان ببینید شب جمعه ای دلتان باز شود!</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21179" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21178">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز:   آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21178" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رویترز:
آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/21177" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسرائیل می‌گوید حملات جدید علیه ایران «مسئله‌ای زمان» است و تأسیسات هسته‌ای ممکن است مجدداً هدف قرار گیرند.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21176" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTSBFDEqUQvgPlTQYh0i2tpsmKXc8US5zF2aDYJLXPHNl35zmUudmYFirQsPqbhaKfm7Z-5N6hgr7GLACwA_dczFuq0RSVqw1zsPcf8shci6iyUfUF3wD91mttBsw3myZZALMbJQLjlaeuJFlZOxEDLKtYkPeTBQXiUbIav1OMaclnBASLYwO1xwoTEbJIroHv8JDs8og-7uMHYJ4HKplcMx0F6pjQdFrSXT2Pnai2-7WdisBPXFXrnJZXbGpHva_e243fWyRHIxZmox4Hu0n0P3Y2kUqAiLV--rTi2rMuMiRB4M9Ei5QmtgSLy6U78UeBGomIuapH0U-lFD3TCnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.  علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21170" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
مصادره ۶ میلیون بشکه نفت ایران توسط آمریکا
تانکر ترکرز مدعی شد:
نزدیک به شش میلیون بشکه نفت خام ایران (به ارزش تقریبی ۶۰۰ میلیون دلار) که توقیف شده، بی‌سروصدا در حال عبور از اقیانوس اطلس به سمت ایالات متحده آمریکا است.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21169" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=JkuClazc8trocH92HgFSwRG6ADm6IAomeKq9LrIM-T_GDa8F4Y5V4qlNfiK8nVkvDsBDoInUWOJB7dsOvDJx0lgyoey1SZ92JO_KqRvWEJ3o-1T5nHFTyzkck1mGFtN3giE-Q0mgs3gvvsQdVs61BITLuy8shwmiRlSxH385aou6YCueyOg5a6mR9t3IJxXKAHBfJBOBXmXYTd0nIF4Yti90dPuUR7D8FJTnIhk866x2EkvP422vzvciwzYs2zfJvUAD0UQx55iKn8dDs56Cd2WluTmL3rTyCgYyQLs-Xs4CFC-OKvhwmsv_-O-hUwTtHuD1ok1iiiM9ETqBEvoasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=JkuClazc8trocH92HgFSwRG6ADm6IAomeKq9LrIM-T_GDa8F4Y5V4qlNfiK8nVkvDsBDoInUWOJB7dsOvDJx0lgyoey1SZ92JO_KqRvWEJ3o-1T5nHFTyzkck1mGFtN3giE-Q0mgs3gvvsQdVs61BITLuy8shwmiRlSxH385aou6YCueyOg5a6mR9t3IJxXKAHBfJBOBXmXYTd0nIF4Yti90dPuUR7D8FJTnIhk866x2EkvP422vzvciwzYs2zfJvUAD0UQx55iKn8dDs56Cd2WluTmL3rTyCgYyQLs-Xs4CFC-OKvhwmsv_-O-hUwTtHuD1ok1iiiM9ETqBEvoasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opvv9zgzpwW5Xmb9FEXHgjk-B0UQrcpruOZDU8t-s79UA5QX46gpt5E1ytR35PhUZtrfzAaKNxC3_GuueOrADg6xUntMY8BSJI67nUbqlv7i5qdmCgbwOQRLV8biCDhzmYwW6cTywNzJYyBuoHXWMCQEc0LqdxZ9jqUYQv6kDoKa5gFaW9GzMRtARkEbgHAT9j5KO5yjuazcTH7b159Z2jf-sv77xk2tcqgeeDu3s9TAdezo3xdYbjSFRpNRttPvYTDBczHLuIJ_kvVfYjQ-67cdIPxC4C2_vIoNeoS1SrKizaH0DYEr_wYLmRI1aah6NhIgHkksP4RfX-Syp3IWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbCVNODDNyLh_zwttWGMiTNsatL9KYoRIow4-Z8h3kEDBpCHATSqHhuhxGg8fmjqViFzsIbZGMisnUgp3kTuw_crqbiK0qKbBdcEkW_afhDF1euK-0QdYOGYJKKyuHYgrOeRFyD5JKuZMoO5R7nVuRmyQ84T7O4vuN06_qjYCIQZJA-niuZ5V3HNZlef4rPUQgeERfr5bhYav2WqKKuVWSqoxRR-jEf23xij1M3u0I8_Db-SeRLi6YLw9xYp6BwTQHW2iwxNgW3JrXEv0AAcySYvjp1iHt_H08LEGGHbi6gCZiFi4o73LeWH7ktLl0dlv35rYrTH9THQECmDiFoH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmUbQXkM1kIzgky3FOUjO7skmjgZOvVDsbN5khi89J_klHNxcabzCBhUXYmGjh4_Dzx1UwtHShT8D93hQhLP1JKh2bjYylt8eFS86laZ1bW2GYZFG9VymS4GBDrKHeO2oqngyawCrLTvhKTB-0GzGWNmZii2HVep92pM6x2xLx3NQQgJl1c7t9HIFVJOabTjwF-veXdkMlAWI5k37LwEz-CFS5BPfGQISCbQKL-s6PZmcCBBjvSb3irfgsWnyfEeXxCVI4dy7Y2nY9W2ZAIkECL6gW8aLfDYUv1DAcIq0XaDuxJ_BYvQpcRskD1zIlRdFBRg69dqmPpcdbgYgAf0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dv-UUwJyU64hHAB7tuF5IXitqZeug3zHmTRxyAlnvfG3b9zPorK0X0WuRiAzwWubhWkI6ZQYgwFDDQgH0OYIMKK8-ooANCrMcJdKyERaLjxxWX5djdQQJd65t74oqk6Pw7tuj5YT7Q6lgi8q6uBEgTTMfa_cvh9HBvStv1gxQnhlouEMjo-NyT9DLKDyRfHASAh1BTcQ1nsS2OSxeE4K8ZpsNTchj1qdeV6zoXt7V_58tW6strYppjqWl6iZwxlBE3SqtZOHDJcYwHLzXKx3PYviBcXYyh74zWxwLkn6G7jdALKrw_1M_POo7gFxBk6l6cJ9mJ1vgsF_vMj57R9YxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS4xeNmi2RaPKD0PzFAp5eqZb4DoaF4taWL9g8mapmpU0AWgoBXzqGa3xCcEbsSCtig9UdZnemplQgbi9jDy1VxzvESQLuMoIdU_WPv3xhxRRw9Pflz0g4mB1QJ03B2C_vw1uWledE5s9w7UwRkvzB2ik3kU6jSPobHyLGYj72d0Pb7TXwbSXTcAStYsP9q_yIX5j5gI4gGjZl79QDk7FUQP1ZlFA3anVExYJS4rLmxx5y9AaJCqfl9ibHYN8nJ2gPQ7kvvJ0pe1c40M7hzJUFMK6Fd8vWmgJx-sXD7T51tBPiJldBjNf4I5v4P_87n0b_wCBsR0HPY4MuEtMzmnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
