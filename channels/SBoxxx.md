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
<img src="https://cdn4.telesco.pe/file/vYWFBSVUQR-9ocyZRl6YzwP3kWh2Ew5AklnCZlAfJn1fB0OVpbDyZ-2KKglFZ8xJ6Bul2Ua-grkpp6_MU9GD4MesW40q8Gl0ymgUGtqPx7HS0xJv-LvO7yC-_WRbtdi5me45eefXzOdlIqrmLeEbC_2Ddz6Cxe4_iA7WUWdSpOx1L7x2alnDyTDui2RjjgUYqgodBE-ESrz-UxoBPCOYwUDVfxKIQKxCyeRiUmrSMOZFTGyBE3dDIaYmkNCIv1jVyfFP5t0DfY3rJBX6E-lfRPwOXJN2UCGcxSrwI-tKKPptfQxng5XRKKA8Y7JnQ0X2yFy7jHSKf_SyjYnkBYX-FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 17:32:06</div>
<hr>

<div class="tg-post" id="msg-18594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/SBoxxx/18594" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTqQ-rWk_cEh_2oy1EwHgqI0PVusZsxxxwl3UuOuxwZpEzuqGCj_dgn5vqxdxKR22P0KKvVEoxEjWGwI2NpW5PjAtqvH-SjbpzPeMt5jW7qzJ3DAUDlV-AgVDz5Bz-tA7riatkbOv3cafp2pXOocC4Ctqf6fbrske5SNsdKB_DnpsxhOgInN_51BlfCXbbBzIyZfd831Sc6oAoi3t2tf71uzgLstiIi8aObrgfSnFjLz3eru6jitzsJFoQLQqbO-029kKRDhvhVXV9mibWW7IxRTRbjcRzy46pxBCuhVg0_OUwBOLC94s7xGmnHVz8ssmsgA5r_eOGdGeFkpSIP7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/SBoxxx/18593" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان یک آبراه بین‌المللی باقی می‌ماند. نیروهای ایالات متحده مستقر و آماده هستند تا اطمینان حاصل کنند که این وضعیت حفظ شود.</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/SBoxxx/18592" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">توانیر: کاهش ظرفیت شبکه برق به دلیل آسیب‌های گسترده‌ در جنگ
‌
مدیرعامل شرکت توانیر:
حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SBoxxx/18591" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq8q-opFQjAF8pE2Iy-uQKhzeX1Zp6Pqmz4AOqA5QNDh66S-uzzkYVwp8TWrpgX4DdtEmvqvmvDW5EBA5hx_40bff0PRth-nwT6XpZ87MCWxEjMn3OsB7klYzRATZ1R2dkNc4HYkElcE7bpyMQFXCmDOfEOgAg3nbR6eWUXvh0dGX-puSU_P-_EiBzAXreT5kqdrjgdF1I77i09Vrgb2y8C-z0emkRUl5tGVU6DrhxEvoPA1VI0FUa1AvSGz-Pz_FQ624ofM0OjNbmOk3gbl4-zHHYUDxLTzV8hOL50zDJxCqKo4w7KJMLG-f_FkzAIed2V-ufL1nRsHZ5oqn2xzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان:   ما از ایران درخواست می کنیم به ارزش های اخلاقی و فرهنگی که دو کشور را به هم وصل می کنند، احترام بگذارند</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/18590" target="_blank">📅 16:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/18589" target="_blank">📅 16:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/18588" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/18587" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تنها راه نابودی اسراییل این است که با آنها رابطه سیاسی برقرار کنیم و بعد عباس آقا را بگذاریم سفیر دایمی مان در اورشلیم !</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/18586" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/18585" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/18584" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک شهروند هندی پس از حمله ایران به یک کشتی تجاری در نزدیکی سواحل عمان گم شده است.</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/18583" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من که قانع شدم.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/18582" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عزت‌الله ضرغامی:   علت مرگ لیندسی گراهام دیدن تشییع جنازه میلیونی  امام خامنه‌ای بوده.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/18581" target="_blank">📅 15:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/18580" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قول میدهم هر ۱۸ نفری که گم شده اند هندی بوده اند</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/18579" target="_blank">📅 15:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">طبق گزارش‌های دولت منطقه‌ای که به رسانه (SCMP) استناد شده است، دو خلبان نظامی چینی، از جمله یک فرمانده تاکتیکی ارشد، ماه گذشته در حین تمرین‌های پروازی خط مقدم کشته شدند.
پکن که به ندرت تلفات نظامی را به‌طور عمومی افشا می‌کند، علت مرگ این دو خلبان را اعلام نکرده است و هنوز مشخص نیست که آیا این دو خلبان در یک حادثه کشته شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/18578" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=vjSvjmbc7ke8qrXgJShzOn3_LENlW5FNmWt8cpsgDk31PBLEfuhxBtm9ENqZYzsXN3ZrgvS0NQvyWI0z17tdBEDr4qN86Nk28wCFjVensMPeJbdhHSua0Imm-uEN61KkmKHavIN9p2SYeu-CBqCnvN52llDIpnBbXAzGktYaNkk2Wk43RgNY1ubqHA0M40MxoYqoGUH6bKzDH6cYmwB2J0YW7Jsmpd8Q0A46Jss8ePE3H6vx6nO9RyHhbA4OfMyAbfCkenSPl4kGmmyYYHj-FIV7R0lrdWnk1s6wJGcAzC1FRXzFnHsZo9tRDX4RJ1c2buuYR8F82XTtPpYZR6Iqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=vjSvjmbc7ke8qrXgJShzOn3_LENlW5FNmWt8cpsgDk31PBLEfuhxBtm9ENqZYzsXN3ZrgvS0NQvyWI0z17tdBEDr4qN86Nk28wCFjVensMPeJbdhHSua0Imm-uEN61KkmKHavIN9p2SYeu-CBqCnvN52llDIpnBbXAzGktYaNkk2Wk43RgNY1ubqHA0M40MxoYqoGUH6bKzDH6cYmwB2J0YW7Jsmpd8Q0A46Jss8ePE3H6vx6nO9RyHhbA4OfMyAbfCkenSPl4kGmmyYYHj-FIV7R0lrdWnk1s6wJGcAzC1FRXzFnHsZo9tRDX4RJ1c2buuYR8F82XTtPpYZR6Iqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر جام جهانی در ایران برگزار می شد!</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18577" target="_blank">📅 14:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg9r_mlHvNFwnAIEO2xQGv_3e8U9zaGrqIpWWAD00Ygum3yzXF_m-qDby3xUoOV-NfuJ5mrqgV4sl5_K5O_R4tW-ERwDQ8SNvWPx-viIr661ciuoPg80EkrJpJx9qiFmIsjZ08ClnhglPukDdK5AcSDI3fxwWhGYgvjlp0NKygaosegSgOfKSbtgWl3_gtiSnk-xDzmPpaouUmACXxwXH91mGwFHoeaKQHyKMlENkjBR5b7VbjXJMjtEGzd32OriuBDcQZ8jsxxkUkJRTKPw_8ofRBU_N-QVNFaB0GZScKjTDZ-K_H1X9f20MUV-h4wLBMI6JomDCAGgxMI3397otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18576" target="_blank">📅 13:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/18575" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو ممکن است برای شرکت در مراسم خاکسپاری سناتور گراهام به ایالات متحده سفر کند، جایی که احتمال دارد با ترامپ دیدار کند.
منبع: i24</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/18573" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.
مسمومیت با پولونیوم-۲۱۰
(در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب مغز استخوان، ریزش مو و در نهایت نارسایی چند اندام شود. این روند می‌تواند طولانی و بسیار رنج‌آور باشد.
مسمومیت با عوامل عصبی مانند نوویچوک
معمولاً بسیار سریع‌تر پیشرفت می‌کند. علائم می‌تواند شامل انقباض شدید عضلات، ترشحات فراوان، تنگی نفس، تشنج و اختلال هوشیاری باشد. بدون درمان فوری، وضعیت می‌تواند در مدت کوتاهی بحرانی شود. فرد لزوماً مدت طولانی هوشیار نمی‌ماند و ممکن است به سرعت دچار کاهش سطح هوشیاری شود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18572" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پسکوف سخنگوی کاخ کرملین هشدار داد که در صورت تهدید موجودیت دولت روسیه، از سلاح‌های هسته‌ای استفاده خواهد شد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18571" target="_blank">📅 11:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حملات ایران به کشورهای جنوب خلیج فارس ادامه دارد.
امارات هم هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18570" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18569" target="_blank">📅 11:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080aef9062.mp4?token=qM5oS-Y7YAFnJObZ_rBG-5AADN3w4LIL5_oM8VrZKyh1VfbSzo_9bMNMVjXRAuzXzGeU27Rg0T3XBoKa6mJt7bWrZCP4J_2ENkt2P_Sf0Hsf0EV_7k0gFuWU7HQeEte77DO1Pu4J3Ca1_wsnYwjcvRCHfJniwLaGNC2sx1UradtXGOqAdDuJn4QS5oAQVW89-7vFkcY9W6UND3Xa25fzwubQIeaquYFmiIkAQnqhNKkSxKhbpoy3rT-4qsYJNkrSXqXGrRuwZH0LbiBqHHCFoS6YnSqGm8Bh1rypmS9SZ8HdKA4deFP1iOh42mm7v4wMTnqLQo0BDRQGuxLKXLFVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080aef9062.mp4?token=qM5oS-Y7YAFnJObZ_rBG-5AADN3w4LIL5_oM8VrZKyh1VfbSzo_9bMNMVjXRAuzXzGeU27Rg0T3XBoKa6mJt7bWrZCP4J_2ENkt2P_Sf0Hsf0EV_7k0gFuWU7HQeEte77DO1Pu4J3Ca1_wsnYwjcvRCHfJniwLaGNC2sx1UradtXGOqAdDuJn4QS5oAQVW89-7vFkcY9W6UND3Xa25fzwubQIeaquYFmiIkAQnqhNKkSxKhbpoy3rT-4qsYJNkrSXqXGrRuwZH0LbiBqHHCFoS6YnSqGm8Bh1rypmS9SZ8HdKA4deFP1iOh42mm7v4wMTnqLQo0BDRQGuxLKXLFVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/18568" target="_blank">📅 11:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
سناتور لیندزی گراهام، یکی از بزرگترین افراد و سناتورانی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود. به شدت دلتنگ لیندزی خواهیم شد!!! جزئیات و مراسم به دنبال خواهد آمد. بسیار غم‌انگیز! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18567" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایران بزرگترین حمله خود را از زمان آتش‌بس در سراسر خلیج فارس آغاز کرد و موشک‌های بالستیک و پهپادها را به سمت دارایی‌های نظامی ایالات متحده و تأسیسات لجستیکی شلیک کرد.
اهداف گزارش‌شده شامل پایگاه هوایی العودید (قطر)، پایگاه هوایی پرنس حسن (اردن)، ستاد ناوگان پنجم ایالات متحده (بحرین)، پایگاه هوایی الظفره (امارات متحده عربی)، سایت‌های نظامی ایالات متحده در کویت و مرکز لجستیک نیروی دریایی ایالات متحده در بندر دقم (عمان) بود که ادعاهای اضافی مبنی بر حمله به کشتی‌ها در تنگه هرمز نیز مطرح شده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18566" target="_blank">📅 09:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18565">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">لیندزی گراهام، سناتور جمهوریخواه آمریکا، درگذشت!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18565" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akXOJYbgFnT-4QL6_FdtEVflFIClw5V-_4UG2goF7pmAl6_QdfQ6DeBfOhYZQBuD0BUbWOxyI4x4I3n0CaoaAKNbnDElzLWmc6dNP2ZPLXUrRyzzyxzbwIfRblfbKB07RgaK4AKw9RAvTJ_gJGZUJo9fZ5Gj2nQGUGu6FedU9Dr7ZETEwiAastnsekuklZ0wU-z99xPIgZBbbz9iAKPAPCZ6-X174EsCDBKP0dEUEKwKUM4MiEu9vDbvle_6Py0xZzFFpmae0PJgTejTP9f8dtic2QxBKRW65n4EgzXxABk2hjLMvt3qWJXuRbQXWI2pDzYtW0dZIFoFo6lVca-B7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
شب خوش</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18564" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNftcse7aDMY70V-sEQ6pzZc6V0kMFkVYx9rXIQM5CSsr7uJhJ2UfkLlwIidiauuvxzDwNDU3vx0tvnWGcbjYhKHW7pB7Dj-cEnoJS5gUp1kTS9uRRwf4WUQPrJ-3_lWwJ76HW_1YcDkdB-iPCmgugB38q5JY1LjBT8Cr3FBuRF9IDqkqSgvEFJP7J0gEhPJmLFRCM2c7h5jlNco8pULarSt0cUeWUsugisWVqeXHvrLMYeEORNUEzsLaKSgeytk0qm9oZCVI0diXaYpb2_LTs6zbCuKlNx_vnWZqcJXLV3LdXYQeaOIirdcjBOg497nye3TA41ja3htEDs6fBIh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدیم ما به اینها میگفتیم موشک ولی باز هر جور صلاح است</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18563" target="_blank">📅 04:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پرتاب راکت های هیمارس از خاک کویت و بحرین به سمت ایران</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18562" target="_blank">📅 04:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله سپاه به یک کشتی دیگر‌ در هرمز</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18561" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">برنامه مان اینطوری است:
نیمه شب: کل کل خداداد و جمشید خیابانی
پاسی از نیمه شب: حمله اصحاب شمال به جنوب کشور خصوصا به دکل سیریک
صبح: گزارش اژدهای بندر از نظم ایرانی در تنگه هرمز
اندکی بعد از صبح: حمله موشکی پهپادی سپاه به اربیل و بحرین و کویت
اذان ظهر: پاره شدن گوش ملت در پاکدشت به دلیل امحای مهمات عمل نکرده
ظهر: مثبت بسته شدن بورص به امید نتیجه دادن اکل میت
بعد از ظهر: قطع برق
عصر: ترامپ از خواب بیدار شده و می‌گوید ۱۰۰۰ موشک میخواهد در ما بکند
سرشب:سفر عراقچی به عمان یا قطر یا پاکستان
وسط شب: توییت های محمدسامثینگ درباره مهندسی مالی بعد چهارم سقوط بازار بورس آمریکا
آخر شب: هالند!</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/18558" target="_blank">📅 03:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">باور کنید اگر انتقام را به دکل سیریک بسپاریم زودتر جواب می‌دهد.
یک تنه دارد انبارهای سلاح آمریکا را خالی می‌کند!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18557" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فوری | خبرگزاری فارس: دو انفجار در مناطق ساحلی سیریک، میناب و بندرعباس در جنوب ایران رخ داد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18556" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18555" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18554" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر جنگ آمریکا:
ایران انتخاب اشتباهی کرد و اکنون هزینه‌اش را می‌پردازد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18553" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کارشناس رسمی ارشد ایالات متحده:
از میان اهداف مورد اصابت، رادارهای نظارتی هوایی، تأسیسات ذخیره‌سازی موشک و پهپاد، سایت‌های پرتاب موشک و پهپاد، رادارهای نظارتی دریایی و پرتابگرهای موشک‌های سطح به هوا هستند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18552" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش‌ها حاکی است بحرین و کویت در حملات موشکی ایالات متحده علیه ایران دخیل هستند</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18551" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18550" target="_blank">📅 03:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of Hormuz. A civilian crew member is missing and the vessel is unable to continue the journey due to an onboard fire and significant engineroom damage.
Iran was provided yet another opportunity to demonstrate adherence to the Memorandum of Understanding after being held accountable for earlier attacks on commercial vessels but has again failed.
In response, the United States is imposing a heavy cost by continuing to degrade Iran’s ability to attack civilian mariners and commercial ships freely transiting the strait. The strikes are being carried out at the direction of the Commander in Chief.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/18549" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فوری | مشاور سخنگوی وزارت امور خارجه ایران به الجزیره:
تأکید می‌کنیم که حملات اخیر آمریکا بدون پاسخ نخواهد ماند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/18548" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بندرعباس، بوشهر، عسلویه!</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/18547" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18546" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18545" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/18544" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امیدوارم کار به خوردن گوشت ناحیه خاصی از الاغ زنده نرسد.
سبحان الله!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/18543" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18542" target="_blank">📅 02:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18541" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
به ارتش اسرائیل توسط نخست‌وزیر و من دستور داده شده است که برای یک عملیات نظامی مستقل اسرائیلی علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18540" target="_blank">📅 02:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18539" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:  افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.  آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.  امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18538" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmvWnXkN6QUgIq9jfT3wmJSbuNMb1NAfUBabPQd1201x0KYyQM1xil_11OBes6zElXsD07VIYYwS83jFdvWGmPsVjDujh3Np592r_5Um8OXyRA25oNw-6JqQqHQV5eE6Btv_Ohh7Gf1Y-NdV4bgiMuKU1EXZJcj9xA9my5eA508RB_ais0dxGY23ABCeltkexATuh1qmEifRaBpMhPiXzbl-7sjxsHI8Idb-Jjrv7Ru0b8Vk1no0vmebYyTfNXA_h5zVv3OLFLKA0uCTtbhT1avHX1kzp69R5wz2MVU3Sy_b8s5tbI7emubYQs-3zjFcN-4SNUG4UUj-Mpf4VByeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.
آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.
امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار و کمونیستی، آمریکا را در بر بگیرد!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18537" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCHEozur162Itjizd1mZP4SncqRFTMFW4Hr6OmkCzg4_v5Apvd6AlHP4A9psccIcedIpUDUe7mGq4uO9F0aO2t7YqCeSIT2gTzl9_dM5O5A_jNpZKwtm9dJyJsMF-yayRyi7s2zVyc6heB05MKZP1hp7KsZGN9vlqhEOQp0H5j8w1MuTH6bsM7VrtE1L6DsmKQToqQZo4RD911l05CT0bSp6_o2Oqdq6yoBucXKZk2e_cyPwLXihSIQdMPeZ4yk8JplSlwoj-FstBm4ywsusYNju4im91ECGKOqMzAunCQ64a6CxqUNuRW9-isI5kOgrj3p8cl6UDJ8UFGBiqvz0yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا من منیراً له لامنیراً له!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18536" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18535" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18534" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18533" target="_blank">📅 00:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">برخی گزارش‌های غیر رسمی از فعال شدن پدافند هوایی در اصفهان خبر می‌دهند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18532" target="_blank">📅 00:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رئیس پیشین سازمان صدا و سیما:
انتقام از ترامپ به زودی انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18531" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18529" target="_blank">📅 23:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79f85bd8d.mp4?token=NcRXQoVi3wK1O9I51RxkUajX4b4X54_fQkErcny4NylgfTP5lvtnatagYLNwWcj-8o5E_pvlDA2V7LLSBY3_Zft6hxq3fGOV-Z7lke2SxEcdkJf6giqXbktW3EJuZdsWROjiISvpMISzPEJ1TAhhtp5jIuAQYZWLBWARW-PDxOQlDw4orjw2mPp2wGIZlbKjsltBJO3xTyyufIxZ1WTuJXPTJpqkySMSBsty4mlxX9lCRnC3wQh09JalNn43tAozGM2PPTCRigNm8oemiJlvmWW7ITVRvhaxFgdK7ZVNuCC8IYL_J5XVb5y2bbD0rYkjH5amdlpKzlCnk53ZPYtFB4QNuoGwmvopKQfCNt4Ic6BarE-V8L-2NcJbx_XXbGUWszrOvW9U-LW2fFRH-x7hfEI-4Yyg_WNwwjFj355ITL6f7wM9wb1OU45g0goHMjGYVfKmJ5OxUipuGKUdVMZq4xbbGE7zqVwe8KO5S4K1HyG213U93OMCTbComktb33PBhdohf0KbDpjTGI4AaI1jFgXnzEzNFhpf2SiOBzqPEG9tcI3xwzawsnBAznXCXlBXzaDU_vUkTzFBxC95IuyVnNGHF2vAwPV1If62wOmnNH2-QfOKTdcjmOWh8pSoxb5Ba15M2IYaPVYoduhtjIjCMAH0ft6oD6vXeTonqNQX1i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79f85bd8d.mp4?token=NcRXQoVi3wK1O9I51RxkUajX4b4X54_fQkErcny4NylgfTP5lvtnatagYLNwWcj-8o5E_pvlDA2V7LLSBY3_Zft6hxq3fGOV-Z7lke2SxEcdkJf6giqXbktW3EJuZdsWROjiISvpMISzPEJ1TAhhtp5jIuAQYZWLBWARW-PDxOQlDw4orjw2mPp2wGIZlbKjsltBJO3xTyyufIxZ1WTuJXPTJpqkySMSBsty4mlxX9lCRnC3wQh09JalNn43tAozGM2PPTCRigNm8oemiJlvmWW7ITVRvhaxFgdK7ZVNuCC8IYL_J5XVb5y2bbD0rYkjH5amdlpKzlCnk53ZPYtFB4QNuoGwmvopKQfCNt4Ic6BarE-V8L-2NcJbx_XXbGUWszrOvW9U-LW2fFRH-x7hfEI-4Yyg_WNwwjFj355ITL6f7wM9wb1OU45g0goHMjGYVfKmJ5OxUipuGKUdVMZq4xbbGE7zqVwe8KO5S4K1HyG213U93OMCTbComktb33PBhdohf0KbDpjTGI4AaI1jFgXnzEzNFhpf2SiOBzqPEG9tcI3xwzawsnBAznXCXlBXzaDU_vUkTzFBxC95IuyVnNGHF2vAwPV1If62wOmnNH2-QfOKTdcjmOWh8pSoxb5Ba15M2IYaPVYoduhtjIjCMAH0ft6oD6vXeTonqNQX1i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:
مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18528" target="_blank">📅 23:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاظم خان همه آن خودکارهایی که از این اسکلها بلند کردی حلال ت!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18527" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری CNN:  پیشنهاد عمان شامل یک مسیر جنوبی از آب‌های عمان با عبور آزاد عادی، و یک مسیر شمالی از آب‌های ایران که نیازمند تأیید قبلی ایران اما بدون عوارض عبور است.  این پیشنهاد همچنان در حال مذاکره است، و مقامات ایرانی و عمانی در مسقط درباره آن بحث کردند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18526" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرگزاری CNN:
پیشنهاد عمان شامل یک مسیر جنوبی از آب‌های عمان با عبور آزاد عادی، و یک مسیر شمالی از آب‌های ایران که نیازمند تأیید قبلی ایران اما بدون عوارض عبور است.
این پیشنهاد همچنان در حال مذاکره است، و مقامات ایرانی و عمانی در مسقط درباره آن بحث کردند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18525" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18524">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i98F5QTwq43d4O7fnMdCf3y9lpGkTfGxYtbV_lmq2f4CxCHIIDCxpdHmwI5cN2ARDwXhhM4L9pXWIBPOi6x8O0zLWVMh1EcdBEXAimFTu8LUQh4DaxOJZXmda8LtHsHMmg739yIgWZt2TpCudxGmTDPt-E7vHSiZyBG26oLB5vw8m_0GIws4zFYCsEKj608-78I3u4hLu-hbVJP-yxJDhaOrXZnags-2deAGtjIx0JQswgFWOogo8F2v3fgHK8obzDYsEEP5OXu9IgvFB-TjTtR_E5iH3ym36sTGahqCpkqGTwzQpTLiIjLsJzDsdahXRn8DJmaq7bvaKQPzP-r7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل داستان سر این است که ایران می گوید مسیر آبی رنگ که تحت کنترل عمان و تحت حمایت نظامی آمریکا است ناامن است و باید از مسیر زرد که در آبهای ایران است کشتی ها عبور کنند و پول عوارض بدهند اما آمریکایی ها می گویند این یک تنگه و آبراه بین المللی است و کسی حق انسداد…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/18524" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18523">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiN0QSFEQjnMje1VsLBN2talNMMAxeuECzUPuWi0pVXw0hBYqXs6mN36p3_dG2qU9siVj7iab5b7VGew6aQwk9bCDcjDT13oJvH6RqaLvRwR55u0jRxWA0Lzd1D9pQkyemcdGDtzBJOPiewqnRuYgY25Wxivkdu2j_6-7zAZAGD032cuMO1eRdbCRj_3hTMIBXkLYvG4awEtMAKOjnTCT0YYq1GJ5nBrn8Stk4DqBlyqHFyZJgVxDX7Gvt5rdeCPJQ8JfArYnqVzCFa-WWQ5Di5Ylm1SpH-oi37XOqw5n0y14aDfcKWsZFayoKTRl2mc8wpqh3J0Vg-OUrkEKfGZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار مهیب در منطقه مستونگ، در بلوچستان پاکستان، گزارش شده است. این انفجارها به حدی قوی بودند که امواج شوک آن‌ها در سراسر شهر احساس شد.  وضعیت همچنان در حال تحول است. جزئیات بیشتری در انتظار دریافت هستند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18523" target="_blank">📅 19:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18522">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">— مقامات آمریکایی به خبرگزاری آسوشییتدپرس گفتند:
«ترامپ به مذاکره‌کنندگان آمریکایی زمان محدودی برای رسیدن به توافق با ایران داده است».</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18522" target="_blank">📅 19:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18521">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 5  جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18521" target="_blank">📅 19:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18520">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">باز شروع شد...</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18520" target="_blank">📅 18:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18519">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IptbjVl2X0YRzEfv1bQMgwYNt4u1eddloUArRGCEiwaogdwQCFnue7IaV8rFL2BvENlOgKSESAUH-HxVbXK8tfHlN-ZgwivbHiX_4aeafdGdYu5DgcHxaZp8jcXNUhV-ymZ-jGpxYhbr_5SaNhNFYj3cYvXCUnboT7K5ELajpY5Hjxm6eBgl1OLB_z5dzXpO6biU1F_-_kXEMc4v_nOT1Is-Vyo-oRijhRB88jk1TQZpwAafY7e3hCq6JJHCsagMpF0DPRYkkgiIuymE6vJCg4PVNyKME6awwpwqPq_bIb9vFJKp9L2N4t_XljKWS12DlDyuapeHTzr1mG5R4NPoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار لیست ترور اهداف اسرائیلی از سوی شبکه افق!</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18519" target="_blank">📅 18:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18518">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18518" target="_blank">📅 18:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18517">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsgdC01PGzKjAMc5hp7oa_xIULwPyM-xyKpyZC6RFSiDTWASgxC3dRvmt4M1GGVGw_ciw_7Z71eAeHUjTXEfACDSit5fg8sKoJ7Edn9n58aKkQKpCP0qUd3HAX3QXlqtrU2HNnlStsgQ_8urf9IqPV5bNxg3gldSJmxkwOtsNFhkDLh-tGjO_gcQjn8xIAqxEf_ImEan-P0l3v4lYsoPwk9MkGKhGl1yLSQAFf-z0vOhxuiNWTkvq29UiIyRJruQn45H3J9IeQvyCOKfInUMTE6FxNjTGusqw6X9pzR2X5ldjHkt3Nks8m8hlUoazMrcKNzWZh09ypPR54wgeO8MpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به ایران ۲۴ ساعت مهلت داده تا به صورت عمومی متعهد شود که حملات به کشتی‌ها را متوقف کند و تنگه هرمز را باز نگه دارد.  واشینگتن هشدار داد که عدم رعایت این درخواست منجر به "پیامدهای جدی" خواهد شد و افزود که اگر دیپلماسی شکست بخورد، برنامه‌های اضطراری از…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18517" target="_blank">📅 18:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18516">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۳ اسرائیل: برآوردهای اسرائیل نشان می‌دهد که ایالات متحده و ایران در حال بازگشت به مسیر دیپلماتیک هستند</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18516" target="_blank">📅 17:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18515">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رهبر ایران، آیت‌الله مجتبی خامنه‌ای:
به شهید بزرگوارمان عرض می‌کنم:
ما عهد می‌کنیم که انتقام خون پاک شما و خون تمامی شهیدان این دو جنگ را از جنایتکاران و خبیثانی که این اعمال را مرتکب شده‌اند، خواهیم گرفت.
این انتقام، خواست ملت ماست و قطعاً به انجام خواهد رسید.
این جنایتکاران، که نام و نشانشان برای همگان مشخص است، با آرزوی دروغین مرگ مسالمت‌آمیز در بستر خود، به گورستان خواهند رفت.
آنها باید بدانند که این موضوع، به حضور من یا هر مقام دیگری بستگی ندارد.
خواه ما اینجا باشیم یا نباشیم، این کار انجام خواهد شد و به زودی، افرادی از میان مردمان آزادی‌خواه در سراسر جهان، هر کدام سهمی از این مأموریت الهی را به انجام خواهند رساند.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/18515" target="_blank">📅 14:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18514" target="_blank">📅 11:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18513" target="_blank">📅 11:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فرماندار پاکدشت: صدای انفجارهای دقایقی پیش در شرق استان تهران مربوط به عملیات کنترل شده امحای مواد منفجره بوده است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18512" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18511" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18510" target="_blank">📅 09:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گفته می‌شود کارخانه فولکس‌واگن در اوسنابروک با خطر تعطیلی مواجه است و صدها شغل در خطر قرار دارند. دلیل این امر این است که صندوق ثروت ملی قطر یک قرارداد بین فولکس‌واگن و شرکت اسلحه‌سازی اسرائیلی رافائل را مسدود کرده است که برای تولید قطعات برای سیستم دفاع موشکی گنبد آهنی پیش‌بینی شده است.
صندوق ثروت حاکمیتی قطر سومین سهامدار بزرگ فولکس‌واگن است و انتظار می‌رود از حق وتوی خود بر سر معامله با رافائل استفاده کند.
بر اساس گزارش، قطر همچنین تلاش‌های گروه کشتیرانی آلمانی هاپاگ-لویرد برای تصاحب شرکت کشتیرانی اسرائیلی زیم را مسدود کرده است. صندوق ثروت حاکمیتی قطر حدود ۱۲.۳ درصد از سهام هاپاگ-لویرد و ۱۰.۴ درصد از سهام فولکس‌واگن را در اختیار دارد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18509" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صداوسیما :
ایران برای ادامه مذاکرات آمادگی ندارد، زیرا ایالات متحده به توافقات حاصل شده با اسلام‌آباد پایبند نبوده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18508" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:  "۱۰۰۰ موشک قفل و آماده شلیک به سمت ایران نشانه‌گیری شده‌اند و هزاران موشک دیگر بلافاصله پس از آن‌ها خواهند آمد در صورتی که دولت ایران بر تهدید خود که در بسیاری از نقاط جهان اعلام کرده است، برای ترور یا تلاش برای ترور رئیس‌جمهور فعلی ایالات متحده آمریکا،…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18507" target="_blank">📅 08:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18506" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آکسیوس— «ما انتظار داریم ایرانی‌ها بگویند که هر کانالی در تنگه باز خواهد بود و عوارضی دریافت نمی‌شود»، یک مقام آمریکایی گفت.
یک مقام دوم آمریکایی گفت که اگر ایران امتناع کند، «پیامدهای شدید» وجود خواهد داشت. «اگر این موضع آن‌ها [فردا] نباشد، روز خوبی برای آن‌ها نخواهد بود»</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18505" target="_blank">📅 08:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شرکت اسرائیلی رافائل در حال مذاکره با شرکت‌های دفاعی هندی برای تولید مشترک موشک‌های رهگیر تامیر برای سامانه دفاع هوایی گنبد آهنین در هند است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18504" target="_blank">📅 01:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه کم لوبیا زیاد خورده بودیم بادی خارج شد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18503" target="_blank">📅 01:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مسئولان ارشد آمریکایی می‌گویند که ایران به آن‌ها گفته است حملات به کشتی‌ها از «بخشی خطاپذیر از سیستم خودشان» سرچشمه گرفته است.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18502" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آمریکا به ایران ۲۴ ساعت مهلت داده تا به صورت عمومی متعهد شود که حملات به کشتی‌ها را متوقف کند و تنگه هرمز را باز نگه دارد.
واشینگتن هشدار داد که عدم رعایت این درخواست منجر به "پیامدهای جدی" خواهد شد و افزود که اگر دیپلماسی شکست بخورد، برنامه‌های اضطراری از قبل در حال اجرا هستند.
منبع: باراک رافید</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/18501" target="_blank">📅 00:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه مقاومت اسلامی عراق در رابطه با ضرب العجل دولت برای تسلیم سلاح مقاومت   سلاح ما که زینت‌بخش بازوان مردان ما در میدان‌هاست، هرگز ابزار چانه‌زنی نبوده، بلکه مرام و پیمانی بر گردن ما و امانتی از جانب امام منتظر، صاحب الزمان (عج) و نایب محبوبش است و با آن…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18500" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18499" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTG6Du8uadLJSOQK45eXX1vkMKkVjaQW6xS8lCaFVCpfdZJCrtXtIeQ6SKVifbutWDwzalwIop86ISXHT7FgKbHdHg0esu2HEgTt1ZcytAwqxNfOsnkvdmrZQ2m9u60ib5b08SVHefe8Oxz7Pr0_dazctXtr5KS_jPgmNIst6kRxWtu62TdSp5C8P42HDLI9eMDJc4OHW-9cT_0DJsvKFTZAQZo_FiZ6oKN_Ljt0sVN44sD01ZdYwwgRpYTqmoc5ruJ0nE-F9OARVfu8FQSQphHDlXFWHVJ-S-LGGYQXxiZvg_W56qmQtsS90OCvHCq_Zdhk18McxYu36AvHFzsbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا:
امروز، پس از از سرگیری حملات ایران به کشتیرانی بین‌المللی در تنگه هرمز، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC) یک تسهیل‌کننده مالی ایرانی را که عملاً اختلاس‌های کلان را در رژیم ایران نهادینه کرده و ثروت‌های عمومی را به خارج از کشور منتقل کرده است، تحریم کرد.
این اداره همچنین امروز همچنین صرافی‌های کلیدی ایرانی را که سالانه میلیاردها دلار را از طرف بانک‌های تحریم‌شده ایرانی جابجا می‌کنند، هدف قرار داد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18498" target="_blank">📅 00:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18497" target="_blank">📅 00:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شورای رهبری یمن:  «پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.  ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18496" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شورای رهبری یمن:
«پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.
ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران می‌خواهیم که از یمن به عنوان میدان نبرد برای منازعات منطقه‌ای استفاده نکند.
دولت و نیروهای مسلح، اقدامات سیاسی و نظامی را برای جلوگیری از هرگونه تلاش برای نقض حاکمیت یمن، انجام خواهند داد.»</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18495" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صدای انفجارهایی در کرج!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18494" target="_blank">📅 21:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر دفاع روانی اسراییل:  امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.  اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.  ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18493" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdmOy7WEOS_DS1K0SpfuljBdWcx_03qPAoI7s1F_hqPbynpU_A9MKJre3NnN2zP_8Abz_SsShWsiFDWw2KjQHb3UjqLQuo-QRFcvqj4EiFZx3FMDRCWC51YGmQEw8sfQekLMZdTNbhL_ZvVuOFkYlnbt49m2J68O5eZWv-4frGEK3b8A4Q-mbJeISHo_tCz1rMBPnhHYe_FbGTYY_OLHhkD0tPfL45wo7CtGhDNEs2YFdDahqLPLWJ-nySczqox_s3fMb33kgwLT6M8f6_sFcqkMUP1seAZK92B5FHG1ShPx7L-Q6llotIQZJizVOwmRwU8p84DpFHy4PC_9ZqRPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع روانی اسراییل:
امروز در مراسم اختتامیه دوره آموزشی "کنافیم 192" شرکت کردم.
اینها فارغ‌التحصیلان دوره خلبانی هستند که رهبری اسکادران‌های هوایی بعدی را به سمت تهران بر عهده خواهند گرفت.
ارتش اسرائیل آماده است تا عملیات را از سر بگیرد، برتری هوایی را دوباره به دست آورد و برای بار سوم به ایران حمله کند.
احساس می‌کنم خلبانان جوان در آینده نزدیک مشکلی در کسب ساعات پرواز نخواهند داشت.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18492" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجار در پالایشگاه نفت پلدختر در استان لرستان</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18491" target="_blank">📅 19:41 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
