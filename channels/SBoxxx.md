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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 20:18:59</div>
<hr>

<div class="tg-post" id="msg-18609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ادامه پرتاب موشک از ایران</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SBoxxx/18609" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyxiSN8R6dHV0UA0IpsiODgn508QEZF9-jd4-UsfS45oHI_QN5wTW9IvxjbycNUQKBnivLID77f8pKp_R4wix15X34X00oqewxEwi9goMfddtuRUCa8pxFTw6NFvBgxcrTxjfzVWJuV_Y97tzDE6ZM1NB8Q_6wE2dlhmb6enKa3sFyh-yiXcLWoXvahymz2_Oct4qtknOEu27iug4Khx6KX6JMY7Nak-zJhKVaH9ol8FLC2EXWTmLHfXzT7oP9h5XUBM_mAtfhB4R1TyUIMKCM54A1REzkoxgLcIzQsbcIBqyYOvNk2fzQ5RXFpp6VPlPIXVWmp5Zzl_QEGKYVBC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی این حرامزاده هم دیشب سقط شد
مردی که قطر‌ را به مرکز ترویج تروریسم اخوانی تبدیل کرد و از حامیان اصلی حماس و القاعده‌ در سوریه هم بود.</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/18608" target="_blank">📅 19:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">منابع عربی از کشته و زخمی شدن چندین سرباز امریکایی در پی حملات سپاه به مواضع آمریکا در کویت خبر  می دهند!</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/18607" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دود غلیظ پس از برخورد موشک های ایران به جایی در کویت</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/18606" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/18605" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/18604" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUTTGL7NPIkGZF2US2_o6PADqWcEG2eNmnBieRItoe6cBXpV4Nj_UgdrL0WJgBLfL75aD4huLO60sD7b2huh9EC4HJaPaUIGIBilz886IcWw0QIGYav9KUNNxFovPRnXRd-MWRDnA9CIG9kCbLvQEcTOSOeWYIgL_Lpg9dHMxLUDzCLO3Dn910Dm3wpK8ijCq1wPydjua0WhdHQvKgTuV9cSqB2PlG2gTV1Atpj8P6-ML8nTe_y2lc2QMGZXTMa0nBjoPsX2vCjCGEu77tAEn6u-blFBogndDZNtsGpEbU6iE0QoNEUhf-BUQieBY6DZ5jILqKyu7fIaDiXWoSHw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/18603" target="_blank">📅 19:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/18602" target="_blank">📅 19:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18601">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لابد دیده ایم آزادی قدس از دست یهود سخت است گفته ایم کویت و بحرین را از دست خود عربها آزاد کنیم.
به نظر من که ساده تر و بهتر است.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/18601" target="_blank">📅 19:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.
همین</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/18600" target="_blank">📅 19:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX3Sh8E7mpZ09poyQ5nQLD1mEGF6-KOCpatEUwYf7_20MmHJVTDp09PETDpzp4j3Wm-wfcBAwPB-CwykNYxqe3PoV5RurByR1TWGbYCvN18NNRTbyUijIsD05cUITpavF8QN5CBDTqoy2Ju45YclksodyY6fk4CymyTRqwu6oajayqBm-rcHBU8ETT4bN8iD3vCnMaM-2bfBRQzLiYhzpRJrdIoOKRHhMMOJ_tYlRixomy_sCNremJwYZOQ8sL6SRIJ0tA9faH_tgCnCENrqBxCXPahZBoy0KzDJd5_cgXalJVlnmVuCCbg1SDCd1-eWPPUDPmlTrpWZ4BctFDD3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/18599" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارهای جدید در کویت!</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/18598" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ :  آنها (ایرانی ها) دیروز با توافقی موافقت کردند که از نظر ما کاملاً ایده‌ آل بود،دیگر هیچ برنامه هسته‌ ایی در کار نبود و از همه‌ چیز دست کشیدند  اما پس از آن، اتاق مذاکره را ترک کردند و کمتر از یک ساعت بعد، یک پهپاد به سمت یک کشتی شلیک کردند</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/18597" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرنگار: تنگه هرمز باز است یا بسته؟  ترامپ: «تنگه هرمز باز است و من نمی‌خواهم در مورد آن صحبت کنم چون می‌خواهم به یاد لیندسی گراهام باشم.  قبل از تماس تلفنی به شما گفتم.»</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/18596" target="_blank">📅 17:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/18595" target="_blank">📅 17:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">واکنش کنایه‌آمیز مرندی به مرگ گراهام:   حیف شد؛ کاش قبل‌از رفتن به جهنم قیمت فردای نفت را می‌دید!</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18594" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTqQ-rWk_cEh_2oy1EwHgqI0PVusZsxxxwl3UuOuxwZpEzuqGCj_dgn5vqxdxKR22P0KKvVEoxEjWGwI2NpW5PjAtqvH-SjbpzPeMt5jW7qzJ3DAUDlV-AgVDz5Bz-tA7riatkbOv3cafp2pXOocC4Ctqf6fbrske5SNsdKB_DnpsxhOgInN_51BlfCXbbBzIyZfd831Sc6oAoi3t2tf71uzgLstiIi8aObrgfSnFjLz3eru6jitzsJFoQLQqbO-029kKRDhvhVXV9mibWW7IxRTRbjcRzy46pxBCuhVg0_OUwBOLC94s7xGmnHVz8ssmsgA5r_eOGdGeFkpSIP7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18593" target="_blank">📅 17:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه‌های دولتی اعلام کرد که کشتی‌های خارجی ممکن نیست بدون شناسایی، ردیابی و پایش توسط نیروهای ایرانی از تنگه هرمز عبور کنند.
✅
واقعیت: ایران بر تنگه هرمز تسلط ندارد. این تنگه همچنان یک آبراه بین‌المللی باقی می‌ماند. نیروهای ایالات متحده مستقر و آماده هستند تا اطمینان حاصل کنند که این وضعیت حفظ شود.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/18592" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">توانیر: کاهش ظرفیت شبکه برق به دلیل آسیب‌های گسترده‌ در جنگ
‌
مدیرعامل شرکت توانیر:
حدود ۴۲۰۰ مگاوات از توان شبکه برق کشور کاهش یافته و بیش از ۲ هزار نقطه از شبکه دچار آسیب شده‌اند.
با وجود فشار مضاعف گرمای تابستان بر شبکه، عبور کم‌چالش از روزهای پیش‌رو در گرو همراهی مردم است.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/18591" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq8q-opFQjAF8pE2Iy-uQKhzeX1Zp6Pqmz4AOqA5QNDh66S-uzzkYVwp8TWrpgX4DdtEmvqvmvDW5EBA5hx_40bff0PRth-nwT6XpZ87MCWxEjMn3OsB7klYzRATZ1R2dkNc4HYkElcE7bpyMQFXCmDOfEOgAg3nbR6eWUXvh0dGX-puSU_P-_EiBzAXreT5kqdrjgdF1I77i09Vrgb2y8C-z0emkRUl5tGVU6DrhxEvoPA1VI0FUa1AvSGz-Pz_FQ624ofM0OjNbmOk3gbl4-zHHYUDxLTzV8hOL50zDJxCqKo4w7KJMLG-f_FkzAIed2V-ufL1nRsHZ5oqn2xzDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان:   ما از ایران درخواست می کنیم به ارزش های اخلاقی و فرهنگی که دو کشور را به هم وصل می کنند، احترام بگذارند</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/18590" target="_blank">📅 16:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18589" target="_blank">📅 16:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عمان سفیر ایران در مسقط را احضار و یادداشت اعتراضی در مورد حمله ایران به این کشور را به او تحویل داده است.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18588" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18587">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/18587" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18586">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنها راه نابودی اسراییل این است که با آنها رابطه سیاسی برقرار کنیم و بعد عباس آقا را بگذاریم سفیر دایمی مان در اورشلیم !</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18586" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیروز عباس سعداکبر عراقچی عمان بود امروز سپاه عمان را زد
🤣
🤣</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18585" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یعنی وسط کویر لوت هم یک قایق کاغذی کاردستی پنج سانت و ده سانت چپه بشود چند هندی گم می شوند!</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18584" target="_blank">📅 15:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک شهروند هندی پس از حمله ایران به یک کشتی تجاری در نزدیکی سواحل عمان گم شده است.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18583" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18582">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">من که قانع شدم.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18582" target="_blank">📅 15:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18581">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عزت‌الله ضرغامی:   علت مرگ لیندسی گراهام دیدن تشییع جنازه میلیونی  امام خامنه‌ای بوده.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/18581" target="_blank">📅 15:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18580">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18580" target="_blank">📅 15:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18579">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قول میدهم هر ۱۸ نفری که گم شده اند هندی بوده اند</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/18579" target="_blank">📅 15:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18578">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">طبق گزارش‌های دولت منطقه‌ای که به رسانه (SCMP) استناد شده است، دو خلبان نظامی چینی، از جمله یک فرمانده تاکتیکی ارشد، ماه گذشته در حین تمرین‌های پروازی خط مقدم کشته شدند.
پکن که به ندرت تلفات نظامی را به‌طور عمومی افشا می‌کند، علت مرگ این دو خلبان را اعلام نکرده است و هنوز مشخص نیست که آیا این دو خلبان در یک حادثه کشته شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/18578" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18577">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=NKUROosPNHgH2dOacCUfQPAlT1VPpJ26Hm97KV9oTSIJ3PK0pF463Acwa955Lmw0HPmTgpVm1V5g7ItG3EsmEeZnzE6xnzo56hK-KgxU4MMcE8D8e-kRs0G5AoPpl7iYnRyFLsTV4oafOhb3AzL_iT_a0DPMTBkofSg_aEHPq-TEvLrrpqjhoOQ-Ulg6jvtSYNSDLBLWuKWFwaSARrjWNahOxVc7IuR3loMDLBP_HPpNNXvm6riyZOf-UmTLwN6q1ZnyKAsFMWV_-SwpNMujPcQ7TUydm713evh0Lo8pZZ2QT6JOG8zVEnoUwdKO2_yWQH7VWQMLKLUHCMczopWKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479291fcd2.mp4?token=NKUROosPNHgH2dOacCUfQPAlT1VPpJ26Hm97KV9oTSIJ3PK0pF463Acwa955Lmw0HPmTgpVm1V5g7ItG3EsmEeZnzE6xnzo56hK-KgxU4MMcE8D8e-kRs0G5AoPpl7iYnRyFLsTV4oafOhb3AzL_iT_a0DPMTBkofSg_aEHPq-TEvLrrpqjhoOQ-Ulg6jvtSYNSDLBLWuKWFwaSARrjWNahOxVc7IuR3loMDLBP_HPpNNXvm6riyZOf-UmTLwN6q1ZnyKAsFMWV_-SwpNMujPcQ7TUydm713evh0Lo8pZZ2QT6JOG8zVEnoUwdKO2_yWQH7VWQMLKLUHCMczopWKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر جام جهانی در ایران برگزار می شد!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18577" target="_blank">📅 14:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18576">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPmh6qP-1RZQUmVlF-ED2G9X9uXlhLfbkrbeqHSk8y7Fa52NifKqI3UVOhWRWF8vvSH7TxAi3cC4mO5pFFOhPQgAVuCXgHusaruaKcBEwGDUn68rgNiAd0Lp5v3Pf-wC0pELaeuMFKlHTs5l9rwcdE9ejabDEk4CnZ3b1TqQtIrCq0u_HQOvNt_hRhrd5I_woHYeMcDvShNa-U-bkrvu1SN8MOyyh85GtMkKOgHM-of-sFII980JXbe92WVs6-ofwlvO0FTbSZjnoS68__9MAcqJF6vt52azp2ucsapgzCMJt7gQ76VlrT-Yhda5StIllXIvbhmLC1-VRLxZ_so_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18576" target="_blank">📅 13:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18575">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18575" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18573">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو ممکن است برای شرکت در مراسم خاکسپاری سناتور گراهام به ایالات متحده سفر کند، جایی که احتمال دارد با ترامپ دیدار کند.
منبع: i24</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18573" target="_blank">📅 13:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18572">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.
مسمومیت با پولونیوم-۲۱۰
(در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب مغز استخوان، ریزش مو و در نهایت نارسایی چند اندام شود. این روند می‌تواند طولانی و بسیار رنج‌آور باشد.
مسمومیت با عوامل عصبی مانند نوویچوک
معمولاً بسیار سریع‌تر پیشرفت می‌کند. علائم می‌تواند شامل انقباض شدید عضلات، ترشحات فراوان، تنگی نفس، تشنج و اختلال هوشیاری باشد. بدون درمان فوری، وضعیت می‌تواند در مدت کوتاهی بحرانی شود. فرد لزوماً مدت طولانی هوشیار نمی‌ماند و ممکن است به سرعت دچار کاهش سطح هوشیاری شود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18572" target="_blank">📅 11:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18571">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پسکوف سخنگوی کاخ کرملین هشدار داد که در صورت تهدید موجودیت دولت روسیه، از سلاح‌های هسته‌ای استفاده خواهد شد.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/18571" target="_blank">📅 11:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18570">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حملات ایران به کشورهای جنوب خلیج فارس ادامه دارد.
امارات هم هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18570" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18569">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18569" target="_blank">📅 11:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080aef9062.mp4?token=GorN9bSIxrqp7spIKtLHvJxkC2A21PihHGQ955Y-WGrkbHhNZ1i4b1pKbS_4iSWOu0VPb5tPTCqzsU6pYynLb8lnLHqh2iK_gzki8aI7oaJB0nJK5G6a6nhO4ZbpjwAxL-5bgOBt9TC_nCufJWHHxNLGNtsvhpAqfXY73dr7gJAYCbLIXBXFEZNkhwbf1nDYlpKhi6EzAP7DH0zwnlusLKOSDS4nhDDCttdN7ENtVNhl7V3nV1zTHMdJrbjaEXX2d56Yu2hkwGaKTOW7Gzfx3mcfteNZmhTAdTlNQzg4NIVXlau5rqcFphDORPUe-1uQihhySsPjIqt09JgvzoHKiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080aef9062.mp4?token=GorN9bSIxrqp7spIKtLHvJxkC2A21PihHGQ955Y-WGrkbHhNZ1i4b1pKbS_4iSWOu0VPb5tPTCqzsU6pYynLb8lnLHqh2iK_gzki8aI7oaJB0nJK5G6a6nhO4ZbpjwAxL-5bgOBt9TC_nCufJWHHxNLGNtsvhpAqfXY73dr7gJAYCbLIXBXFEZNkhwbf1nDYlpKhi6EzAP7DH0zwnlusLKOSDS4nhDDCttdN7ENtVNhl7V3nV1zTHMdJrbjaEXX2d56Yu2hkwGaKTOW7Gzfx3mcfteNZmhTAdTlNQzg4NIVXlau5rqcFphDORPUe-1uQihhySsPjIqt09JgvzoHKiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نحوه عجیب اعلام خبر فوت لیندسی گراهام  توسط گوینده شبکه خبر :
🔹
«به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✍🏻
CAPITANO
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18568" target="_blank">📅 11:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:
سناتور لیندزی گراهام، یکی از بزرگترین افراد و سناتورانی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود. به شدت دلتنگ لیندزی خواهیم شد!!! جزئیات و مراسم به دنبال خواهد آمد. بسیار غم‌انگیز! رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18567" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ایران بزرگترین حمله خود را از زمان آتش‌بس در سراسر خلیج فارس آغاز کرد و موشک‌های بالستیک و پهپادها را به سمت دارایی‌های نظامی ایالات متحده و تأسیسات لجستیکی شلیک کرد.
اهداف گزارش‌شده شامل پایگاه هوایی العودید (قطر)، پایگاه هوایی پرنس حسن (اردن)، ستاد ناوگان پنجم ایالات متحده (بحرین)، پایگاه هوایی الظفره (امارات متحده عربی)، سایت‌های نظامی ایالات متحده در کویت و مرکز لجستیک نیروی دریایی ایالات متحده در بندر دقم (عمان) بود که ادعاهای اضافی مبنی بر حمله به کشتی‌ها در تنگه هرمز نیز مطرح شده است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18566" target="_blank">📅 09:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18565">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لیندزی گراهام، سناتور جمهوریخواه آمریکا، درگذشت!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18565" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vin-7TXLg2bVqBRnbfcwZOi5FPMJtn4GHHcTKI2YHiXbhXytS6xrDGqMRzMrJWghFRwZf0SG4tavgWogqnOAYa0M_5iW2vSRgiD-h_4SyIiGwk5twhw8Nv_mVjPi2GVTLPLRAoeoPdaQEXG_R1HBNszE5snRb5vf-5fjs2nGBBoybMn1yQ6-o8YkBK4yOTziiJeddEjKo3bYM475KW7gue4tE7V3ANigm0lEU12p5rRB2zjrTbBDhwEHxO_SlQhVE0EEndkGQ4YsnWWYBuYm3SlrQy1qsxsmTiacb5poMDfw8efigsXj72T3eKIAJZoMZpI1Rw-jVsomT2zD41av-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعییی
شب خوش</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18564" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM8JnLWsg8jhG7DhWtvv7Fh-jXloPwytmNw1RMIJHklln7_uEgcYDh6XVxsbnGjP7IlUax5h1_rubGoY-N0umzOwqYH55fiL8MpCeBmPubP3yy5Ehay-Ro6AJpVallu49TL1u0SBIEeAdPbOsHye31jwOdNHoCZC53R2mybemRkj2M8ttvwFpyUN1pkGCeO0sK0hUY-j90nsYBlHQBnGUniR56CYu3qCYit6OAuwmcnuykhFBGz8i8qHTIQqMi7MPjwTlQBa1sgv2YIrnf3ilc0ukNClLbTNZAQoXiCSffjtMsvru0IU83bPhNx_Y72cUDNZnLNmV7_yA0z5xNcupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدیم ما به اینها میگفتیم موشک ولی باز هر جور صلاح است</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18563" target="_blank">📅 04:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرتاب راکت های هیمارس از خاک کویت و بحرین به سمت ایران</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18562" target="_blank">📅 04:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حمله سپاه به یک کشتی دیگر‌ در هرمز</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18561" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/18558" target="_blank">📅 03:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">باور کنید اگر انتقام را به دکل سیریک بسپاریم زودتر جواب می‌دهد.
یک تنه دارد انبارهای سلاح آمریکا را خالی می‌کند!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18557" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فوری | خبرگزاری فارس: دو انفجار در مناطق ساحلی سیریک، میناب و بندرعباس در جنوب ایران رخ داد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18556" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18555" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هواپیماهای روی تهران متعلق به نیروی هوایی جمهوری اسلامی ایران هستند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18554" target="_blank">📅 03:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر جنگ آمریکا:
ایران انتخاب اشتباهی کرد و اکنون هزینه‌اش را می‌پردازد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18553" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کارشناس رسمی ارشد ایالات متحده:
از میان اهداف مورد اصابت، رادارهای نظارتی هوایی، تأسیسات ذخیره‌سازی موشک و پهپاد، سایت‌های پرتاب موشک و پهپاد، رادارهای نظارتی دریایی و پرتابگرهای موشک‌های سطح به هوا هستند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18552" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش‌ها حاکی است بحرین و کویت در حملات موشکی ایالات متحده علیه ایران دخیل هستند</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18551" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18550" target="_blank">📅 03:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At 7:15 p.m. ET today, U.S. Central Command forces began launching the third round of strikes this week against Iran after Islamic Revolutionary Guard Corps forces blatantly attacked M/V GFS Galaxy, a Cyprus-flagged container ship transiting the Strait of Hormuz. A civilian crew member is missing and the vessel is unable to continue the journey due to an onboard fire and significant engineroom damage.
Iran was provided yet another opportunity to demonstrate adherence to the Memorandum of Understanding after being held accountable for earlier attacks on commercial vessels but has again failed.
In response, the United States is imposing a heavy cost by continuing to degrade Iran’s ability to attack civilian mariners and commercial ships freely transiting the strait. The strikes are being carried out at the direction of the Commander in Chief.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/18549" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فوری | مشاور سخنگوی وزارت امور خارجه ایران به الجزیره:
تأکید می‌کنیم که حملات اخیر آمریکا بدون پاسخ نخواهد ماند.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/18548" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بندرعباس، بوشهر، عسلویه!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/18547" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/18546" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18545" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18544" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امیدوارم کار به خوردن گوشت ناحیه خاصی از الاغ زنده نرسد.
سبحان الله!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18543" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به نظر می‌رسد برنامه خوردن گوشت الاغ مرده کنکله</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18542" target="_blank">📅 02:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبر فوری: نیروی دریایی سپاه می‌گوید یک کشتی را که دستورات ناوبری را در تنگه هرمز نادیده گرفت با شلیک هشدار متوقف کرده است  . گفته می‌شود تنگه تا اطلاع ثانوی برای تمام ترافیک بسته است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18541" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:
به ارتش اسرائیل توسط نخست‌وزیر و من دستور داده شده است که برای یک عملیات نظامی مستقل اسرائیلی علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18540" target="_blank">📅 02:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18539" target="_blank">📅 01:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:  افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.  آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.  امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18538" target="_blank">📅 00:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM82ClajhhWoIdB57aRW3u5eor_Fxylo-DYhesRxOV9FSqFY19mzJdaDUWeS_NZXihJjUmy8ca9YpaZ3aXClXG3Rt8UAhJHPbPcS3nhQlININfQYnQzUHc58Xon8DZXbKTb8E1G1ZUeE6MzY5OPwEKn3skY0BCrb2fbIIuxTNZRmOKQ70IskDMa97CAqo1EV6nvgXGkwZUeqdrg-esx5qa70_qqu5OqxHkBdff9MS4itAcV_P4qB-lYOgIPBWoTQlq23YBcOZnPnRntA8SQ4C4r6cFOUQdFMs8_jxQzJm2Q1LazkwwgKz4wzaVfUKG6Dmt7TdmsTTgHA0axETuf5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
افراد افراطی و پوچ‌گرا که اغلب به آن‌ها "دموکرات‌ها" گفته می‌شود، کنترل حزب خود را از دست داده‌اند.
آن‌ها توسط افرادی پرحرف و نامناسب رهبری می‌شوند که کاملاً از مسیر خود منحرف شده‌اند.
امیدوارم آن‌ها مقاومت کنند و اجازه ندهند این ایدئولوژی بیمار و کمونیستی، آمریکا را در بر بگیرد!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18537" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtXGDpuxnj8XCxHaJgtjOHRLo0XkhieXMBWfgKjPE1wUkuGUkQbjoeH-8O0dlzK82K9EmIDOiHGnDveHygSnbpzcvup5MGX6wECTGUDYXDNH3LIKP03ZtH9X7jmH0b3cZZAW0Ok7YISM1uAr7V0Ot6xkSnqkfDhwnWhAH_gjc59li1py3eG3gCxNmxVCNJgOk9y12kF6Kh_7mWMUHKS-k1Dr-aeODn6ORpZ5DV16benRBukPGRrw26bf257xQ3sDPFibsrraaTeXv5RcfMGisNVQ6ey6LjcdS-X6t5p18yXKoJhYrtTlreMuISPQ_N0WO8hB48kv_p_goDGsGWutig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا من منیراً له لامنیراً له!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18536" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مکن ای صبح طلوع....</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18535" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18534" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18533" target="_blank">📅 00:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برخی گزارش‌های غیر رسمی از فعال شدن پدافند هوایی در اصفهان خبر می‌دهند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18532" target="_blank">📅 00:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس پیشین سازمان صدا و سیما:
انتقام از ترامپ به زودی انجام خواهد شد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18531" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18529" target="_blank">📅 23:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79f85bd8d.mp4?token=cC0iHdpoaaasyuWFCWr4PZG1b-uJujOOt-EcjzYHv2KBrwCI6nYaiDZDK8vOEhGJ4sUymB2tbErcQTz_Qke2mjLFY6nZGV8nA8XT89vKpvvT24hBhTljMvszU97-QNbPCl-uLx3zrXMLcyknFVYxjyv9JQzWcu8hrIPLFXyFcvCT_ffHO565adk5dU2vqgc27k-tmLOJF50TCttqn8YnQbGLEotcQNvK6uXA6wFwWk0pDbveC1jm_3ObhxYoj9fvDTF2DCBCfgaIB-AKfkhDnwfqMSMzglPGbZXEF6L2nNHCGVjQpwRwbuxHJ7oy6P0Zr3WKjje-Qltu8p5iciGzWYGynaRAERu7oMEOQN3ttbHzVPVLoNXlY88p6OfmE4uoOpVQIbwo6jUgogVU2Uu56ueX2fPus9cexCN48ZBPxkDwmTTbe945GKBnv3m8GF1T-sardouUFyBSuLft1M9OhBDpeqq8TvIJGHSAdHknUrz0sGSFgBGMGZ0CmvczXrTky6_-JbRfNyTXAi2lbo2eezoEn2NoxfZoKWxhQwZxOVEO8Y9WPYrGVRQTqUjIuiLXRdA_Gcqt8bQ2xlw3PD48acenxSxrga7XMJ2p5Hg49NcR-JSmM1W-pAKOlu60JAXNGSApeJSrhuxFtMQcquy_d-x0AfZtzvnIRhuLNCtuPFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79f85bd8d.mp4?token=cC0iHdpoaaasyuWFCWr4PZG1b-uJujOOt-EcjzYHv2KBrwCI6nYaiDZDK8vOEhGJ4sUymB2tbErcQTz_Qke2mjLFY6nZGV8nA8XT89vKpvvT24hBhTljMvszU97-QNbPCl-uLx3zrXMLcyknFVYxjyv9JQzWcu8hrIPLFXyFcvCT_ffHO565adk5dU2vqgc27k-tmLOJF50TCttqn8YnQbGLEotcQNvK6uXA6wFwWk0pDbveC1jm_3ObhxYoj9fvDTF2DCBCfgaIB-AKfkhDnwfqMSMzglPGbZXEF6L2nNHCGVjQpwRwbuxHJ7oy6P0Zr3WKjje-Qltu8p5iciGzWYGynaRAERu7oMEOQN3ttbHzVPVLoNXlY88p6OfmE4uoOpVQIbwo6jUgogVU2Uu56ueX2fPus9cexCN48ZBPxkDwmTTbe945GKBnv3m8GF1T-sardouUFyBSuLft1M9OhBDpeqq8TvIJGHSAdHknUrz0sGSFgBGMGZ0CmvczXrTky6_-JbRfNyTXAi2lbo2eezoEn2NoxfZoKWxhQwZxOVEO8Y9WPYrGVRQTqUjIuiLXRdA_Gcqt8bQ2xlw3PD48acenxSxrga7XMJ2p5Hg49NcR-JSmM1W-pAKOlu60JAXNGSApeJSrhuxFtMQcquy_d-x0AfZtzvnIRhuLNCtuPFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:
مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18528" target="_blank">📅 23:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کاظم خان همه آن خودکارهایی که از این اسکلها بلند کردی حلال ت!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18527" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری CNN:  پیشنهاد عمان شامل یک مسیر جنوبی از آب‌های عمان با عبور آزاد عادی، و یک مسیر شمالی از آب‌های ایران که نیازمند تأیید قبلی ایران اما بدون عوارض عبور است.  این پیشنهاد همچنان در حال مذاکره است، و مقامات ایرانی و عمانی در مسقط درباره آن بحث کردند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18526" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری CNN:
پیشنهاد عمان شامل یک مسیر جنوبی از آب‌های عمان با عبور آزاد عادی، و یک مسیر شمالی از آب‌های ایران که نیازمند تأیید قبلی ایران اما بدون عوارض عبور است.
این پیشنهاد همچنان در حال مذاکره است، و مقامات ایرانی و عمانی در مسقط درباره آن بحث کردند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18525" target="_blank">📅 23:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18524">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKQh5f9-OGyzySiyEN8VBIHW9fsmbqvoVhmZRgbGCgG8mxCgvffojGGrbdr5xD8KTnL2isWjlCcbrtLiGV4Z_O1-PA3ktQIf64h33TZGb-Z25dRbumABpQowESLS7glNQLLFsuMoLf9KJNPMIeAD1yNxQEYfdlvMm6ZChCTjnUs4p_dTdQ895rQv5EM9Lv8ug2a8IlBVRZqwLzfUpTmdaFoZ4dREqHzegzw4z7mbXwqFZxA_UVz1iosaIRSylIiKO0eagd1JZL2sa7qMH788cASAgJ6-CgqPcdmXoy6gMdRX6HE78Nu-UdhaGcE2_lcVt5cKNZttLCV4Xiknt6SBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل داستان سر این است که ایران می گوید مسیر آبی رنگ که تحت کنترل عمان و تحت حمایت نظامی آمریکا است ناامن است و باید از مسیر زرد که در آبهای ایران است کشتی ها عبور کنند و پول عوارض بدهند اما آمریکایی ها می گویند این یک تنگه و آبراه بین المللی است و کسی حق انسداد…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/18524" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHNY_6xjK9h20CYsLuLUUAZ44JkcrnREyHIBc5ipjTgG5w-3PjtZ9LeZQUDmR4izl_RyqGbS-29U-ite4LoRFZoA4sxzXF4v3qeO8aeUv45iJ_dgxG7dIM0lxRABcD8v9XizlXPGbXMMKwURBPPM7M1EHIwf_qIquBqILF7D5PAkjUpWTkE5LVnPvztyG5rPXu2E7mGe15vea-46Vj0wC6nz5Sn7rqDORFarcYHbJ_5-r4gZbJ_f7qtx2nYaTefBbzXMuPxKxv8Ghzk0aSwqQZfnO1Fxgrcftd3H4Y99CkvrxLcew_HTf_y5idMi27NX0JMaRDPSmGK6LC2rBwwmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار مهیب در منطقه مستونگ، در بلوچستان پاکستان، گزارش شده است. این انفجارها به حدی قوی بودند که امواج شوک آن‌ها در سراسر شهر احساس شد.  وضعیت همچنان در حال تحول است. جزئیات بیشتری در انتظار دریافت هستند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18523" target="_blank">📅 19:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">— مقامات آمریکایی به خبرگزاری آسوشییتدپرس گفتند:
«ترامپ به مذاکره‌کنندگان آمریکایی زمان محدودی برای رسیدن به توافق با ایران داده است».</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18522" target="_blank">📅 19:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 5  جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18521" target="_blank">📅 19:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">باز شروع شد...</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18520" target="_blank">📅 18:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18519">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W812Wqcr8zg1ipxyK3ZSJ_p4TDw9Au4xtD2__F1qhF5fGV82fiAd78q6o9_xnvxylax3-8aG7GiLbDayeYFJ-Jtz__vbOhO7bXXC48WpFyqDcFkj8Q7mGd06CSp8r4cPMpUxH9wAeA-ZsFYbvo2oBkBYDB-41_lcxn9kZKWi8EQsFdAUMwPTFudLcYQnfZg_8NRsY3UTn5-uApsuoja0P2oPJZgqRqC07A2VC7-Dewprgg5ihRTJKV54-88_QlCpqbLehYMDgcwF1s22soZYNUM7N8qPl3F2sDgIKknts44uuq-Gx5GT_WX-o8KYgcRItGCF-OV3lULx5Pw25vBAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار لیست ترور اهداف اسرائیلی از سوی شبکه افق!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/18519" target="_blank">📅 18:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18518">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">به 24 ساعت هم نرسید!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18518" target="_blank">📅 18:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2Q-8Hg9f69LDTG1TOdMasMmsonyFDDKej3FLs6J8JUiIny9Ak2nZ_0eFiw_0PcRb9k3aOteV_xqYDeF5XnyuVrbvgJONSJZA_KFOnQTwp9ZbM6CPGmYKH56MUkp90MeiEi-uaejWwD9Cs3SoZJx7B4OkIU7iYzfRtxw8H0tuPcmkHVUTJkj30J5pRe7urPIwmvcZhqeaUMrrLqfyXUwxnIedLbKQyn9EVIHCg8UZADcPlHDe4YYHBHhA1H-Gj6ZpeNN75ijCAMmj1H5NQEDyiVvIUprWvXn1O3SYclA71iCNENIJJ2Fg0MttKJKj_QwOFkdQD8pf0N3CrcfxFdf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به ایران ۲۴ ساعت مهلت داده تا به صورت عمومی متعهد شود که حملات به کشتی‌ها را متوقف کند و تنگه هرمز را باز نگه دارد.  واشینگتن هشدار داد که عدم رعایت این درخواست منجر به "پیامدهای جدی" خواهد شد و افزود که اگر دیپلماسی شکست بخورد، برنامه‌های اضطراری از…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18517" target="_blank">📅 18:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۳ اسرائیل: برآوردهای اسرائیل نشان می‌دهد که ایالات متحده و ایران در حال بازگشت به مسیر دیپلماتیک هستند</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18516" target="_blank">📅 17:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رهبر ایران، آیت‌الله مجتبی خامنه‌ای:
به شهید بزرگوارمان عرض می‌کنم:
ما عهد می‌کنیم که انتقام خون پاک شما و خون تمامی شهیدان این دو جنگ را از جنایتکاران و خبیثانی که این اعمال را مرتکب شده‌اند، خواهیم گرفت.
این انتقام، خواست ملت ماست و قطعاً به انجام خواهد رسید.
این جنایتکاران، که نام و نشانشان برای همگان مشخص است، با آرزوی دروغین مرگ مسالمت‌آمیز در بستر خود، به گورستان خواهند رفت.
آنها باید بدانند که این موضوع، به حضور من یا هر مقام دیگری بستگی ندارد.
خواه ما اینجا باشیم یا نباشیم، این کار انجام خواهد شد و به زودی، افرادی از میان مردمان آزادی‌خواه در سراسر جهان، هر کدام سهمی از این مأموریت الهی را به انجام خواهند رساند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/18515" target="_blank">📅 14:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18514" target="_blank">📅 11:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقامات ارشد آمریکایی اعلام کرده‌اند که چشم‌انداز دستیابی به توافق هسته‌ای با ایران رو به کاهش است، که این موضوع نگرانی‌هایی را در مورد این مسئله ایجاد می‌کند که آیا دیپلماسی می‌تواند از برنامه هسته‌ای تهران جلوگیری کند یا خیر.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18513" target="_blank">📅 11:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فرماندار پاکدشت: صدای انفجارهای دقایقی پیش در شرق استان تهران مربوط به عملیات کنترل شده امحای مواد منفجره بوده است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18512" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18511" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انتشار اخبار تاییدنشده از انفجار و آتش سوزی در پاکدشت و پارچین</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18510" target="_blank">📅 09:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گفته می‌شود کارخانه فولکس‌واگن در اوسنابروک با خطر تعطیلی مواجه است و صدها شغل در خطر قرار دارند. دلیل این امر این است که صندوق ثروت ملی قطر یک قرارداد بین فولکس‌واگن و شرکت اسلحه‌سازی اسرائیلی رافائل را مسدود کرده است که برای تولید قطعات برای سیستم دفاع موشکی گنبد آهنی پیش‌بینی شده است.
صندوق ثروت حاکمیتی قطر سومین سهامدار بزرگ فولکس‌واگن است و انتظار می‌رود از حق وتوی خود بر سر معامله با رافائل استفاده کند.
بر اساس گزارش، قطر همچنین تلاش‌های گروه کشتیرانی آلمانی هاپاگ-لویرد برای تصاحب شرکت کشتیرانی اسرائیلی زیم را مسدود کرده است. صندوق ثروت حاکمیتی قطر حدود ۱۲.۳ درصد از سهام هاپاگ-لویرد و ۱۰.۴ درصد از سهام فولکس‌واگن را در اختیار دارد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18509" target="_blank">📅 09:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صداوسیما :
ایران برای ادامه مذاکرات آمادگی ندارد، زیرا ایالات متحده به توافقات حاصل شده با اسلام‌آباد پایبند نبوده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18508" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:  "۱۰۰۰ موشک قفل و آماده شلیک به سمت ایران نشانه‌گیری شده‌اند و هزاران موشک دیگر بلافاصله پس از آن‌ها خواهند آمد در صورتی که دولت ایران بر تهدید خود که در بسیاری از نقاط جهان اعلام کرده است، برای ترور یا تلاش برای ترور رئیس‌جمهور فعلی ایالات متحده آمریکا،…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18507" target="_blank">📅 08:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18506" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
