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
<img src="https://cdn4.telesco.pe/file/RnSxvYIxMrMnRYlG5lT3CvIqtKNb7nq39u0Bd29rvc6aPP58KrEKEQMN67kYbN6uJJkYp_5cvNelkyCWSB3ml1yd7WOpUKb2XMsxjhYmk6-J0xQIdTn5kbyM1ajgRsgCGqCnMVahM1IClNGvfMVeizs9r5SAbvKtkVuVHFCfZ8GTRtbJ2SywlrO8URbHfTgffTyp-REOspL4NrOZtXu2kttHdABMaK-O-upyFY9YWHjIfeEkH4_CG02QYkLwLHvWDh4IxR3duHoLApwOHz1iflyI6cAXWZJGi0cru-Jn8oqmYlKR7Yimz64qirMRXGXL3svDV_XML0iQjNQUpyIiMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 126K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 22:34:12</div>
<hr>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=FyFuacQJ5ESORwV875O6tHJdZHRlBVSQQCUdRh56WCFYPfg4G3HVt2N0Wv0gz1SotCE5jlFLlVMLBoS-8z519O9LQTuK2wp3YNaofe9vLLmWr8hX0tu8JNsbdLd9KMLIOqudR1UL3Z8Dd4-tAC8OQjFkmVIvB1wof0XKg9c-d8yy-qrfyjGTJA19fRz6VlxIsnazOgpfDYQEDDAddAbN9ltBM6pmuYEpAVoQWWFKvdOU6Lvga7DUxjUVf8-MvW6_BBp3Go1VSnr5Q_T5UgiMlS5-ridS9uPOvxaYdSUT61wl8goYqXXYH98HqaH4kRVhRpYTYAIgjB1S-FJCvJL0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=FyFuacQJ5ESORwV875O6tHJdZHRlBVSQQCUdRh56WCFYPfg4G3HVt2N0Wv0gz1SotCE5jlFLlVMLBoS-8z519O9LQTuK2wp3YNaofe9vLLmWr8hX0tu8JNsbdLd9KMLIOqudR1UL3Z8Dd4-tAC8OQjFkmVIvB1wof0XKg9c-d8yy-qrfyjGTJA19fRz6VlxIsnazOgpfDYQEDDAddAbN9ltBM6pmuYEpAVoQWWFKvdOU6Lvga7DUxjUVf8-MvW6_BBp3Go1VSnr5Q_T5UgiMlS5-ridS9uPOvxaYdSUT61wl8goYqXXYH98HqaH4kRVhRpYTYAIgjB1S-FJCvJL0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 997 · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90198">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbyMBvnGKpzg9A-PBQtC4hIIhVbZdBYHoWfBZ8C3He48mUvHRWsRISwZCpW9HMeebT7o9imrsEo6yhr8MJX6ykl9ykV5npWrXS6nlEFl1JPQ7aINWU7sgYvUMvPdto1tl0H4JSJVqJARbK5Ih8oKUKd_n_ahh1I9e_bz4-SsMFPbndoe_oDt_-M8MAIXk7Po9OpavFvBpvbpf6cryPp4uAGn97HjVBx7ITinMWYM7rwEYuZYM9jEyFBIZBvgEyXsMgZRdrdV3mHsYk_9Lj0wg-crmhl1vEmS9WCbUgAgWFZwrDxfuMArrXetJu9hIjXxunU7_vuWY7xRcBZWA_n2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه رولان گاروس
✔️
⏩
با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۵ میلیون ریال بر روی رقابت‌های تنیس آزاد فرانسه (رولان گاروس)،‌ بدون توجه به برد یا باخت، مبلغ ۵٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/RG31
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/Futball180TV/90198" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=UggP1asIgweloB95RX99eh2kNIas4uBvuid55vMe_lY6y0zcqQNFgISqige6DS97FbcS34xaueWUqZKUxaQAJUXqzjgIxAb7O0nvBp6pQblcZFZ1eXuNnHHOtqMNRnmZQ92oblFX4_BjbuZ84jqSdah5gp8QjF5z1ED3uE8pO3Jo9WNWE_gKyXoR1w2K0FbPjm1F_a8FKNzwJQQsZYeApTQmMp4uK7NV1VpTEly_3NSulCL9_8d6w1Grr91utsG5AvBw-dAGMN9KAmrpSC-mwWegsGHhbtI1ep97c5T7Tvd4PSrdNIzucGtShtC4FTfNXya7Jo2J4ASiknLEANgF-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=UggP1asIgweloB95RX99eh2kNIas4uBvuid55vMe_lY6y0zcqQNFgISqige6DS97FbcS34xaueWUqZKUxaQAJUXqzjgIxAb7O0nvBp6pQblcZFZ1eXuNnHHOtqMNRnmZQ92oblFX4_BjbuZ84jqSdah5gp8QjF5z1ED3uE8pO3Jo9WNWE_gKyXoR1w2K0FbPjm1F_a8FKNzwJQQsZYeApTQmMp4uK7NV1VpTEly_3NSulCL9_8d6w1Grr91utsG5AvBw-dAGMN9KAmrpSC-mwWegsGHhbtI1ep97c5T7Tvd4PSrdNIzucGtShtC4FTfNXya7Jo2J4ASiknLEANgF-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90196">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90196" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/Futball180TV/90196" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90195">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koT5RReVaJhMJ_pvlsVGfHjrZeigDEJ4aIuWuD1rqrmZ5e7-IlDsasFgBXHjYzzo9D6ebT-vR9w4PKrSEZHo738hiVyQfxksIS1433ELJCzCazstR892NZ1tA0qDZmOCp9hxsBlz7LFbmpQltIVzIB-TC3DhOXzcS_AcERF2N-dixqHj11Oa7pZOFNve2IGP3HWBxIIrekyEVsmWOjd4bzJyL7q3FDr5ZkRQz1SCjxX5tH26uBtC3SjVV2K6Kg_TJcYhPhusFkX_Z8P4Sf2NgVDjsWOt9utP6uqAApXE1Nd9-FhPMF8cjQFUrm8I_LrRPdSRb_8lJnfuVKpd7bI9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/Futball180TV/90195" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=HoqBc4kLkBSQqaRgvsRchvcQptYwtE3N1A1gZN3raSshsDcVXIH3DUz51312cunLvu_t-7u4pagUJ-rczUmh8YSX-1oKrln2sUSxYNrpoFbuMfLq-wwf1-7SqvuRma4sEMrSgi7D7ITRGpLv1BQO3T0TJcRyX1qF377RTJtJBwHGRsdThGDKJsg8Qkuw5MHXuk48m5u4vQwWMkg4Tma6WkwiXmLyHHo1OAbtR6mBjGR_a1oFzHiRqBEbwpZAsWk_r7xyCXP22RDpCJ2MLEiLPayCBwqt3OTlUpXzwXLtMsf2dvgwuqT6jVyFjVp9UbuGbJ7WePHZOjJvpJD2gIGQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=HoqBc4kLkBSQqaRgvsRchvcQptYwtE3N1A1gZN3raSshsDcVXIH3DUz51312cunLvu_t-7u4pagUJ-rczUmh8YSX-1oKrln2sUSxYNrpoFbuMfLq-wwf1-7SqvuRma4sEMrSgi7D7ITRGpLv1BQO3T0TJcRyX1qF377RTJtJBwHGRsdThGDKJsg8Qkuw5MHXuk48m5u4vQwWMkg4Tma6WkwiXmLyHHo1OAbtR6mBjGR_a1oFzHiRqBEbwpZAsWk_r7xyCXP22RDpCJ2MLEiLPayCBwqt3OTlUpXzwXLtMsf2dvgwuqT6jVyFjVp9UbuGbJ7WePHZOjJvpJD2gIGQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90193">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
آکسیوس: تفاهم‌نامه ایالات متحده و ایران:
🔴
- تمدید آتش‌بس به مدت ۶۰ روز.
🔴
- هیچ عوارضی از سوی ایران بر تنگه هرمز دریافت نخواهد شد.
🔴
- ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد. ایالات متحده محاصره خود را تنها پس از برآورده شدن این خواسته‌ها توسط ایران به پایان خواهد رساند.
🔴
- ایالات متحده برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد.
🔴
- تعهد ایران به اینکه هرگز به دنبال سلاح هسته‌ای نخواهد بود.
🔴
- ایران متعهد می‌شود که در مورد تعلیق کامل برنامه غنی‌سازی اورانیوم و حذف ذخایر اورانیوم غنی‌شده خود مذاکره کند.
🔴
- ایالات متحده متعهد می‌شود که در مورد تدریجی برداشتن تحریم‌ها از ایران و بحث درباره دارایی‌های مسدود شده ایران مذاکره کند.
🔴
- ایالات متحده هیچ نیرویی را از اطراف ایران پس نخواهد کشید. خروج نیروها تنها پس از رسیدن به یک توافق نهایی در پایان ۶۰ روز رخ خواهد داد.
🔴
- جنگ بین حزب‌الله و اسرائیل به پایان می‌رسد – به اسرائیل اجازه داده می‌شود اقدامات پیش‌دستانه‌ای برای جلوگیری از بازسازی سلاح‌های حزب‌الله انجام دهد؛ این شامل حملات هوایی و پهپادی به لبنان خواهد بود. «اگر حزب‌الله رفتار مناسبی داشته باشد، اسرائیل نیز همین‌طور خواهد کرد.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/90193" target="_blank">📅 17:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90192">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el6CyvpFu3Y4T0vzvEKkDpCJaYxzk2sfyD6CPtTFCVSlR19I2eIiJhuSu4zqu76nCHEm9eND8wFMGtPlZShtgl67-zK4t_brM4VCd3VM9lN-VheG39Jn5iSyiHi1t_FF-maJb9lQzHLEMXpiKksGVe2HP60LccSI5FiizVTZS3y8wNkIg1l90AVngcLwZUpVHqInLtcGU8lxlYHcklyHq145eCH2wVdSIXrtRE965W5qa0v--JK0Vd0mSowYfmuWqYyJtoHX4nGBsUMGyTBrLsiimqy0BTguWakn-kwoXuKwR55zP-6Glx1Gcz7HeDYKPoQ35lrkzJTWiE02KhPRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب مشترک داکنز نازون مهاجم استقلال و روماریو اسطوره فوتبال برزیل در پاریس؛ هائیتی و برزیل در یک گروه جام جهانی 2026 حضور دارند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/90192" target="_blank">📅 17:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90191">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOpWv4TN-wF6osE8g2V9KRABHnjMXxa6zsAI2wKcPtWSknf2Q1Bn4L1o864klQ5sTlUIF1asyD9d--v0txKKDbZROjsVk-qSzTk2wJEudZv8kgq1q0PuLvBpU9s1p9GyhDQ9j224D76Oa5_HubENrkb2w5bjNg20Dwtm-O6oaXYRhUa7L5DibYB548qxAF9UpcnSUVZ9lYhGnL9IhTyMdmK0pa34dHp0Z8E3ZPuc3ybIArsr4Ek5DkTCe4LqzY047_ITwfHUtJMOgfnMSUMm8EzRMk2oYiz6hcv0MZuWQ3QlGzUyKob2t79AkXIX9-MkVNaq6LL5dcuKFt064bf4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ: خدانگهدار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/Futball180TV/90191" target="_blank">📅 16:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90190">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67618efab5.mp4?token=oZYTLeYGXCwvex82KZOBjmtcnPXt2QYngGdMNkehmxkJWrxvidNF50_bVfm-bflZ-LJ9zx23phC8JjBplKnj6MVTVZPiogW7UxYN3yX4V7h_SgMl4jANrIvP8Yc80nRsWVvKlrqpEG6vASPOtVySoLJAB0_zzSIW60-Ps5LPaC9x41xYekwbzMxImojGQxQxJ35jvsu-SqhvuhU4ORf5TRN__Q-IxT7HvXBrV7edQDndmc__ZVurih7nSfBREiouoHDk5KSoQz6qzCbUzEbPbsMC3v4JhfFF4I8n9M2goOuF-m0Y32LDUX6UDXQNnMynHb4UihhYNOe0OfKso_ODrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67618efab5.mp4?token=oZYTLeYGXCwvex82KZOBjmtcnPXt2QYngGdMNkehmxkJWrxvidNF50_bVfm-bflZ-LJ9zx23phC8JjBplKnj6MVTVZPiogW7UxYN3yX4V7h_SgMl4jANrIvP8Yc80nRsWVvKlrqpEG6vASPOtVySoLJAB0_zzSIW60-Ps5LPaC9x41xYekwbzMxImojGQxQxJ35jvsu-SqhvuhU4ORf5TRN__Q-IxT7HvXBrV7edQDndmc__ZVurih7nSfBREiouoHDk5KSoQz6qzCbUzEbPbsMC3v4JhfFF4I8n9M2goOuF-m0Y32LDUX6UDXQNnMynHb4UihhYNOe0OfKso_ODrIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر حجازی: دامادم گل زد، تیم ناصر سقوط کرد، دخترم گفت طلاق می گیرم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/90190" target="_blank">📅 13:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90189">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/90189" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90188">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbX48OikWLRMyQjWBAKkt1sqWdrudcOEb1rQRY2QwDkfSeCzU_Pm1JVbcUjYnXFnkTO2bH5b8ZnLe_bbBuLqGUtFbDLmXxGeGbvXfbbrB6dCDY0JkYEGKjG42qYB4u_uks7gTNe35MzCSup1tEdWeVH0PJQshpOUppXXteWdg_y1-DMWI5CFCPCaw92UwCh_CszcDvL_WmKjaKYsOREJR4NLo4unvOBVIy3KsOnFtkbbukxu5u2NxJP0mW0JzvvAFin4DFfHPUt86vXb12KJXnQH9ulN59CUs_jD3MBbO8uw-qqYPRnnT5113qoco3HXRlbTqzQJdU1vLhyePhlZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
قرارداد «PSG: Champions Contract» خودت رو امضا کن و با قهرمانان واقعی یعنی پاری سن ژرمن و 1xBet درآمد کسب کن!
💰
پیش بینی روی PSG — جوایز تو در انتظارت
⚽️
🏅
شما در
Level 1
می‌تونین AirPods Pro، کیت خانگی PSG و جوایز دیگه رو ببرین، و در
Level 3
نینتندو سوییچ 2 یا حتی iPhone 17 Pro Max در انتظارتون هست!
😎
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/90188" target="_blank">📅 13:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90187">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=kBfGDKr1OCwLWoJOKZqsI6hVlttexDrSHdPHKCy0q35LkSko59zE60wNUlr6n-c7t7jh_-gmLdWibgFcKai25lJNEg8iDMPZSc5o-_syWZ_7zuOVdYlpPnnHok7UFovVLnwimUw65A-28wxGXo1a8Wxe5_FYiZdtT6sQ7FDTvVAqmHavc3udJUxeBLHyuzmD2Z6Bd5qE-OmkNxFQay_XEM1ZdRKpMvHYmFjTy66vMaDpXPXNfJd34ZXbL4ij5PSaGkwD11d1Wavg_mGSlnMUsefeCkcC1FrefCwMLC8nWQwFqPZ2gRG2OKWbDfSfb1Zrs9S0ha5DnFDjf-2Bb7NBurVvqGBwtDcNKruarKOTMTmdrIJgW_hq-mptUCdu7NqDG8kcWQuy80O7_NV7SbgNNysxa0gyq7f5ney53Mncy6HkdJh7pWwue4mYAt5VMAmQJara97CG6kn1B57gtTdp49BFXbwuwL1AhHEXoQePt4xRA7_saotv1_WdvCqr8D3TVusIe9na_QkCvVpR5N0qHATobBBAqW3mSM-gwNPdaQh7FWnfPZgf76FDIGXZ2XIAGUCHKw1mCx-ALzmLpk4oWDLYbn3AO5lD1_C6AJRIRXe-5ptaWDhEk619At8UX82hEIk09An5VK4bSnRtotolUt-hu9iyTwzLIoTFOzltvsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fbdde7379.mp4?token=kBfGDKr1OCwLWoJOKZqsI6hVlttexDrSHdPHKCy0q35LkSko59zE60wNUlr6n-c7t7jh_-gmLdWibgFcKai25lJNEg8iDMPZSc5o-_syWZ_7zuOVdYlpPnnHok7UFovVLnwimUw65A-28wxGXo1a8Wxe5_FYiZdtT6sQ7FDTvVAqmHavc3udJUxeBLHyuzmD2Z6Bd5qE-OmkNxFQay_XEM1ZdRKpMvHYmFjTy66vMaDpXPXNfJd34ZXbL4ij5PSaGkwD11d1Wavg_mGSlnMUsefeCkcC1FrefCwMLC8nWQwFqPZ2gRG2OKWbDfSfb1Zrs9S0ha5DnFDjf-2Bb7NBurVvqGBwtDcNKruarKOTMTmdrIJgW_hq-mptUCdu7NqDG8kcWQuy80O7_NV7SbgNNysxa0gyq7f5ney53Mncy6HkdJh7pWwue4mYAt5VMAmQJara97CG6kn1B57gtTdp49BFXbwuwL1AhHEXoQePt4xRA7_saotv1_WdvCqr8D3TVusIe9na_QkCvVpR5N0qHATobBBAqW3mSM-gwNPdaQh7FWnfPZgf76FDIGXZ2XIAGUCHKw1mCx-ALzmLpk4oWDLYbn3AO5lD1_C6AJRIRXe-5ptaWDhEk619At8UX82hEIk09An5VK4bSnRtotolUt-hu9iyTwzLIoTFOzltvsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت همسر ناصر حجازی از روزی که شُهره به همسرش پیشنهاد شام مشترک داد
همسر حجازی: هم خودم را باور داشتم، هم به ناصر مطمئن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/90187" target="_blank">📅 10:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90186">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
روزبه‌چشمی بدلیل مصدومیت از اردوی تیم‌ملی جدا شد و به دبی رفت تا مراحل درمانی خود را طی کند. احتمال خط خوردن این بازیکن از لیست تیم‌ملی برای جام‌جهانی وجود دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/90186" target="_blank">📅 10:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90185">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khk_ZYm2SZUE1RteRw-CAFZRPstVoN-1I2j9Fc7IphGJBdBIb97miklP3Q64oGHbhSzLQ8SrbAF7QDUVatRDFh_xdm0omlyjs1ZPlmkPPz-awLffUFcYjEZmqswYmZiivpRxl8Kb5cxUgsZ3v_MEI2ztzDmW7dTr-9Fn_0rK9q_i2yHThX1BtMTowPXKofPjztC7KPPnPEhJnmKX9iHYJ0NYUhl_zi5RuHvcrgnWqPL1KE5u7cqxxg7pbpBHt9MgdDjFZ59ZXMmiXP7rmMpbNJZoyTh7tksmZ3zB5FVFqbFz_AxG3FaaIMgQRpHXD6OSiJwS5hlDsL-Ux2X1Bduc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس ایران پس از شایعات توافق:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/90185" target="_blank">📅 09:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90184">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=BMmB5UVGPnbMwQAxFC4Dq3fwucLZjvzOwkguQlGRl_qk7jj6_VV8seK0pzH6WzKuG-EPfG03f62W7K85Wh8jNsacFuIBsagq3DJgP9OIImX6uzpjAf_ZJGMW_CUzDBAkDgcdhcrITpDa-hw_dkzER9KOxAxrZKFARjdespb6HWf0mE0Fk5OnQKLD5_Q4lKelYI27zeafLhRRYuCBXHMY_GR1xBSjswzkT-5vN-Md1a99AFZmzWU_h0Cf7EAFed0I_Fkjuf0NnDQr5jenOxaAxuCmTnNKhW_1TE2F-NOanapKdIGDFLv4l60ZAMkfjMB6GdpULy3_fG-vyB5QzI1KwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f849fc0fcc.mp4?token=BMmB5UVGPnbMwQAxFC4Dq3fwucLZjvzOwkguQlGRl_qk7jj6_VV8seK0pzH6WzKuG-EPfG03f62W7K85Wh8jNsacFuIBsagq3DJgP9OIImX6uzpjAf_ZJGMW_CUzDBAkDgcdhcrITpDa-hw_dkzER9KOxAxrZKFARjdespb6HWf0mE0Fk5OnQKLD5_Q4lKelYI27zeafLhRRYuCBXHMY_GR1xBSjswzkT-5vN-Md1a99AFZmzWU_h0Cf7EAFed0I_Fkjuf0NnDQr5jenOxaAxuCmTnNKhW_1TE2F-NOanapKdIGDFLv4l60ZAMkfjMB6GdpULy3_fG-vyB5QzI1KwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظی باشکوه کارواخال از رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/90184" target="_blank">📅 09:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90183">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90183" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90182">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLykryookI5in01stvTwUl4rwztA0ILCnrBfNLOITxXeLc7QTxqAFcxtcCgk2G7uPCOD8E82T_LQvek4CbBKkCD7QAWk86Ax3_KXf5VW-k91BowMKl7M29MsJgbLsen6hgJdCjP8UebrL1utWHoLw5dTNVbmAa4oSEv4coRoJC4aI62EFx9h0Fs5_JuzWWKZos2dMTRAnVynErXDiG0DonNh251GdvKottBEcKdJ1_l-Y5dZZUjeXtRXogn5sm31AcwvIiplwbK2X51agN43QSysx6YS1cNNliMye4ZstmkOA6TJ51Y0ODquHIdszgvBivTdMANcckkEK3exSyPGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90182" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-g7QIEr0uzsfAgR-btOuqQQ3XPOnQ8kxaE1iesIcp1U3dRbRr7_-KCW779uoio1UqG1UOLZw8Dx6unec4TcQUvgU_l6mZfZUzva1iYYBNpWJdGfCDFWe1wqFDJ26oirbyDWUgb2rbGLCaFlg_3KBTNHdXb9Qjdlppmie8Fi6y2etlS7A-YWWPZ-KRPMr33qlYiPE2saEkd4ctGpUC0UlvPocJZDH_JmtdrvZTDLyVfZY7ZoQzdKn-nvLMTmcEt22ienrD88mZEQ_MjqXce3EDAgLYrx5n_di5XEKPOCmOjPV7LmggDGvaKxUNzohm6-zjRFeFWgRq2KyNmRt2cdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T60liMzl6ckWSrUzVpQpbkwl32yxXIBVRDS6SqNmtbyD_B6nCfv4_DkSAeRkMcscaq3O6GKqLyvH6eti70sIoGIGxjsQ3HbAVhPOuEXB2SKbsEOhNnKo4Edr-Sc7vCRYC9JKXm5vt7Wc1o3Artbt_sOaRK2HlUBphEVEu3mJcOq9thUN1JXF-TGyTPA0coszxDbl783QpKhrYD2iJXMM-O_wuocDlTZr_d2p2dEFDn7LgZWg0VJJuWQjh3nnbaaku-LOKS_PV926p5b9sRRCiKI_yVvfpA2yJRBdnn3DIBh-VCJa-m7XivsR0kwZjDpE173lkkc7sh6zHsuFt_lj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDJ016vAOoDsEdmcwrvdoJviRkFyIoEz1B1yxqRK_HMS5BxZjT2RWKnewrrZvFTgZyZybnKYaImSWahqL0MrCUVhUdMNj8Vt1vJeSVe19JPmZW2TBenP6sZPpJjJOGTg6-HHRJ50yXg0FJe9R55-g12gBORM5qZdcwIGoylI_zca9uc8rgDpzP0mkObpiKZIvo-G0oQafb8IY2pX96nDL6WkaStC4Avd8PMgxky4NmjDr4zrLmMjjZvC5bmg3ywBMRg0f2QdjKpy0-mj9783sSe-GSir7KlHdDn_P550Xmtt58RGCRnOhfrSjTbbhvq3EVKOwOdnCbBrwwLlouNM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90178">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XftRP8DmtphCiUzJeEADo-NiaOo2RTVCFQrY1xvRe2mzIolrEpezafq4ZAvDRgT263SwDc6ho7RBT1U-iVclNS0BwXWZhclxXDQSZMA_FrLR06yfJozdJpODrkozKaBoxidoXOihOXB3U9xrOcW3ofUIUjicyWjYHHD2mvWuKqJQtOQt4Cywd-2pM2nQVYflDIBQjQrjQfMrcFLGDCDwjhpsqZWFKBa3eKP5M5qWtwOx3d4fOShQ3eAYOzCkxmXypAvF4hZxZwSz8UKMZKD8GiapqkLiDo_cazMdR-BzCPoBhQ3qM_pbF0KC6JUopo_f_XJ_jBaSBOSoRjOz-31R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تورینو - یوونتوس
🏆
سری آ ایتالیا
⏰
یک‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه المپیک تورین
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
تورینو در ۱۰ دیدار اخیر خود در سری آ، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
✅
یوونتوس در ۱۰ دیدار اخیر خود در سری آ، شش برد و سه تساوی کسب کرده و فقط در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر تورینو در سری آ ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر یوونتوس در سری آ ۱.۷ گل در هر بازی بوده است.
🧠
خروج را از قبل تعریف کنید، نه وسط هیجان.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/90178" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=RElFilN8JOYpM7IEqHGqSWW6yibb55MokJNJ-k6h2DU5taDON1YIsCVdv8ahnZVRoIeGtW62rAIWElhDg-BGMECeT1h_d0VGj0rPGRNMChYCbgwz6LZmWpfWXMITjojdolEw41fr_-YCGPqJwvXsH4pQIKVoOD7t5KukcseG1-CJ1JqTkag5Ynk_jOwU2Q2CChp8cFFTla3TEYpRuSZdLOhMZ9mMdGJLw5ee0Ts2vjAAu86MB0t1QBMNYi3a1XZ-UHFfymqEpSAQ8gdhS7O1tk1xer7tYNpI3WzVGWHJemhIPuodV5ZszcS7m6vD3SVBqQ5IUyYwLpL9kpwlM_dgRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=RElFilN8JOYpM7IEqHGqSWW6yibb55MokJNJ-k6h2DU5taDON1YIsCVdv8ahnZVRoIeGtW62rAIWElhDg-BGMECeT1h_d0VGj0rPGRNMChYCbgwz6LZmWpfWXMITjojdolEw41fr_-YCGPqJwvXsH4pQIKVoOD7t5KukcseG1-CJ1JqTkag5Ynk_jOwU2Q2CChp8cFFTla3TEYpRuSZdLOhMZ9mMdGJLw5ee0Ts2vjAAu86MB0t1QBMNYi3a1XZ-UHFfymqEpSAQ8gdhS7O1tk1xer7tYNpI3WzVGWHJemhIPuodV5ZszcS7m6vD3SVBqQ5IUyYwLpL9kpwlM_dgRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGsPTLsG2_gKkbJWYkkIT5_SGy2VQrHvBsB89Nh24yVf0pdtf5FDn4K6ws_JyTJOycnLuxWnsvm_H2B521RxM46Dg_P7X9tY7Gkgrt3BBbD7a3d35bgadeHdQ5VgrFxLXRPpXAN3h9jX0eK2TkwV-IFgqfsqacAHcn5CLsbR-eE1Lf8WaLPiKH03EzM4nG2BwxjlXIX1YEX1Ivwj_Cx_6xb_cZSTnwlyWOZmFdfhq_rcLp34P0moMBJamSz8gE_mF9dL8W4bj-Ash62Z3EZ5GvuuE6mzVOEpYlj0PN6hTNsZTcjGIz_eDJgcleKUr0p57-Ap2Fyg7xtPNQxgUTE5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=VOhJvtT-gCjOWS0mPXYTk-ZnBb9h5lP16N0yHJQGOCPzFz_FyBTP0JzjveQVobtfebQBxFNd2NcDsR2on2KMIpV7HagXrDpeiXWAyDolhrarSTh54gfOCHCPgiIG5N-xB20V1X6MaiO7ZYla_7asjVsKpnaa2IUl0_RWQIhPHc44iiEfDLEJrM7GQFvSwl8S0kq5ZPa76ozWFqti6LkffIPRWvB2Vkp3IMOEsNIV7bnm2kHOvlSyjsyny7pNEEqOcNfKWHqT4LCKjjzAmbdifGxpJAF8ss6_mdWu16D335h_u7W6onnJJsn7G3CIT7VEEPMk3HzGQpXWM79h6V5TCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=VOhJvtT-gCjOWS0mPXYTk-ZnBb9h5lP16N0yHJQGOCPzFz_FyBTP0JzjveQVobtfebQBxFNd2NcDsR2on2KMIpV7HagXrDpeiXWAyDolhrarSTh54gfOCHCPgiIG5N-xB20V1X6MaiO7ZYla_7asjVsKpnaa2IUl0_RWQIhPHc44iiEfDLEJrM7GQFvSwl8S0kq5ZPa76ozWFqti6LkffIPRWvB2Vkp3IMOEsNIV7bnm2kHOvlSyjsyny7pNEEqOcNfKWHqT4LCKjjzAmbdifGxpJAF8ss6_mdWu16D335h_u7W6onnJJsn7G3CIT7VEEPMk3HzGQpXWM79h6V5TCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90174">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/90174" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90173">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvhE_9_gOf_tpLoRYToVrU68H_6G1-RvvQHHZJZreM6zVBVsthXueCdjSM4xwi56N-JgHID7YTksp13W0gWhC5G8VRtFIGGJA4VLYEmU9CGDHvUjvq-6aYJ8NedoVjnzC85fLpH2auRetTJ38NDDGBImjWmQwrHTQgQ6SxMP4bmJRQkt8OG2wQ0cb6f_n5CeoTw1u59J_rmSnIbv_x_N7DOLqtko73ab7kZ7ILlp0Fsn_cGkk1sEpqHiMn01evWAtdJWan0Dyfqo0B4LEQCX0w_aPCw1IyiYvnzBy0c2zaM7avmPaDzw_GGWNivtzqsxn0bTQ9wL0kQ0tOtgKBL0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/90173" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=JE3qKxZ2aUYGWoV5eYhJ0zaUfvbhxqQJVxRJVc-6Jqr1Z66hzN1c1Pg3TB0Y1tv0ZyRJ2Wx-cd1a_2H3ranT_kJBQNdowgc5zSoua2YwVtoSjQbZxt7QZ9LFq2owvLVMei1c1kYDnmghqNJPEdPsbuZuNMhbDlfmRGI11Y7GJ8lcyE0FTscmVKwm7D5Yxki1H7PSW_nZ7cSY9eLyPDXQY0vEU5NXnrQnk0n3E60WdiDWB8ytuJcARDTXaX8JWtuQL8YHTb_PkbBblmO5WA1F66cQVvLKgOhQPzZQslgaHJb1IWx5kWd1q0DOePFLx6xs2dFJAC_b6PdQ8LOJe_Cgng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=JE3qKxZ2aUYGWoV5eYhJ0zaUfvbhxqQJVxRJVc-6Jqr1Z66hzN1c1Pg3TB0Y1tv0ZyRJ2Wx-cd1a_2H3ranT_kJBQNdowgc5zSoua2YwVtoSjQbZxt7QZ9LFq2owvLVMei1c1kYDnmghqNJPEdPsbuZuNMhbDlfmRGI11Y7GJ8lcyE0FTscmVKwm7D5Yxki1H7PSW_nZ7cSY9eLyPDXQY0vEU5NXnrQnk0n3E60WdiDWB8ytuJcARDTXaX8JWtuQL8YHTb_PkbBblmO5WA1F66cQVvLKgOhQPzZQslgaHJb1IWx5kWd1q0DOePFLx6xs2dFJAC_b6PdQ8LOJe_Cgng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVNDHLkdxKDwtiv95kJogOjx_XhjGKrOZ9qmC4AQ_uGDJzHtVEc8W6sWpFpuPhOXaBM7BraNvsQJ01-7r7Z51DavaQF1pYwLsEVlUBRgmvwX0mXw_eMJGPPuR0KIXOG4tDo3g9rCgTVIMXHdY--NxLH-fs57dC2HEqbeWEJ02wZ6ha3xTx2qIujLYs0bHQqBCD7snKm6LpXfjes0pRcBXNdR5w0aB2ednDc-AB5pyB91VozmkSEUbwEcKfHI8Pb407N-jWUHkZAGvT9zoXEo63L97YFKTazDxgDfHKxVQXuIfYwmWhFmvPD2Zy0xCOgXrhqCrd0O4rWA9n-wKKGw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2FaMe_Ogx-xAkYmimFrP_pVnwDufEyH5fJ8wi3Z-66vZxSJx32e7axHzPAARiGroDJIbzO7nWTcxMfduuJdnwbtN9_t0VljcYOaMoV5UvogNx_0eUKIqGSBn16dBrSt2_FJevtkj2pFrfZNUcO2oLZ2U3CHCWlFgA33BGLSyvRUpW7V8e4pSGbRwhzciQHs_hBM0VVAdxKpBFxvLWVm4-AEQh5JhjjmtzxSRmv-gpvqWSniMlBkaubZTgduQNOh9kC1WgMo_9W7RzPsrBnZZnXM70mX4Uo08WRrVMcBxVAevwX4nJyyZAkFsZ7hkpZcWKZ__fCsrQ3ug4UFYh2lDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=sCF0Y1805yqjRueu0ZdRAoLeyFk3R191Qwy32zHfxOrFm5VHA-Pj00mzR813fWJx3WwZzFCNGstxy3GP6guToRxabCJcUB7qAEowlh6kmaPSHasRvEfU0jvd2coSjCX_yvnleNfzad12zHkMtud0sBm0zu5NLGdC5BcB7tyeHc2aeJwgv-hBkhtooOvvUWP3fAfmdMZaDQEtP2JVVuFwl9nh-ClrCkyymDM2uqgGign6AhNSUjkKV6_XPBQ_xjtUOV9Q0R7QVJCUovLBOBQvskRmW5hCoM-PXFqbTImySnPmaebUZlyJJc17sW9YHw6OQfZCYJRWY2kVlbW75WD38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=sCF0Y1805yqjRueu0ZdRAoLeyFk3R191Qwy32zHfxOrFm5VHA-Pj00mzR813fWJx3WwZzFCNGstxy3GP6guToRxabCJcUB7qAEowlh6kmaPSHasRvEfU0jvd2coSjCX_yvnleNfzad12zHkMtud0sBm0zu5NLGdC5BcB7tyeHc2aeJwgv-hBkhtooOvvUWP3fAfmdMZaDQEtP2JVVuFwl9nh-ClrCkyymDM2uqgGign6AhNSUjkKV6_XPBQ_xjtUOV9Q0R7QVJCUovLBOBQvskRmW5hCoM-PXFqbTImySnPmaebUZlyJJc17sW9YHw6OQfZCYJRWY2kVlbW75WD38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjs63O9wnwcwBgJFmyMJjD57osE7uDuw4TeDyn22ZF6jw-NCp60E_EX2Ztb_ZXQM5SpeaFeV3oHD8RgL1D_SdWwaPyd5_8otSB_y0vTQx7WHZblknLMLL_Tm4nt_rVapJkcIwtEa6rRRl5wIJo49dqPyDTsrfuFjTcWh1VpixbEGnTsFprC-tFphv3yWv4FA3gfcCEpmOb3Cf2A5jOqHSE_ANR_lM6_QXBMgPJ3ntW4MuBNHqJjMCWM2rCqVOLwoblvkk4pxhtIvtdu-j3VBnS35S76OWDc_8zG1xX7bsbKlxQMHLEJkpfm7UzxV27r4vmB6D5O9A9ENhyJd6ScaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_59kBrGINxsf533r09gjh1Xyk32eSqgmrVPWjgzsP2QtvBPg3RjZuf4DdV4B_eIbQQ6aIkIHw0PGiHyV5RPgzWhHeYx7obe4_lVC8fiXiq2d-NZX_UxWyzgxeJHP-gs7_osFAISnEs91LUHTnge1srTlTnYOg7b1b37IA-ib-sg4_RoRfMzdcFtzEe_8Ept9yYBCfl_JhyWiaR6Ek7JHLqUkH2of1e8IABfsShVKU8QtpRBFHw12vye1lGxor0EPjO3rOLZvJ2r2b-QoFWuZJtQm5Gyj-xUNVr2HyzRFsavJqcFmePtMfmW7G4pn4d2a4lkl4Rqh3mlpoVhrHEdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90166" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMu4xsZgvjVnnHQ-qcmJj27glg6PbgXrq0G3roSNLcsyUsilIDbKNOOFTPPGybz_r5cxHwinz5SOpk5IKjomG-ELBenUhAcgUqpkPEwc5eJY0KLJehsovbqOYJPVbVbr3jgzCMnlXoa_DPl6W-8neSbK5CfebKPW2wb5UgwV_43cmDrtPFEUIx9BRkJy5gn94X-fBGSrsjmgM-nq-qb09PSZ3X_Fxw92ZwgyKJffRf4xCenvVFF0w07D9cvH8Che0z2sqx8FBOaiVtmSTrbpeR431ZC0MppADtNuRwkj_FLT02H7XVhuxYsAV00vPY_H5ZacXobSS1BxeR5QeFVe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90165" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=WRZTtU9Gd60aHNQ3X5eDUpSDFXhVhSq4M84ISExcG6BO8_t-GpCs9gbZLOAGC0NlNvdtwqp8FUPnaW8IRJDTUYepiMf4yK0jXfoWM9gUzHFY0tRPe39HGTQQOsmStTAJKMdZiY5GMYYjgfXV6H5bEBZtlQr6T5GHkldqdQgRwEVMs3F49qJygSOObEV2-d0arq8m_wK_zUjo6q-OSbGr0Snbq_ctrmyw7oFhz51R8156xGeM6Wazg4dqc1p3CPwzE42UOMV5rwIxxMNIwoWc-8f_0_RK-3Vi95CX-ZPSyeffJ9ewxBATJocLzyhVLJKCB5XVjZMtBhQ9a6DxIJzi3zQKkjQQvSu7HsQad8bJEO2AkMQMkpwdxjXIKexNnizssRoqlO-xW_3-Wda1CRGaIbELFQRR5PVir-J0PtQT95vv27sc2tCHeAGuKrTr-9UFIt-Xc95pu3ryvB07X1UELCUF454uMBEj9NbIGSpYdoBsJRhA-2mluMf2zRCsqxZHM9DrC0u7-YMI7QjdxkL69KifiVILC5CEikqEhwS91sYDPnFYM3MfHIIv_--4wEKaHLwMHS372M-p3yiBMLEFBkSv0oAKFvThPOnhbge69fcruvfPjXh95XyW3Du--Yw2l-aTFInkdrd6xW8z_0Un1WuzLEHIqzAvINZnuv1nPq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=WRZTtU9Gd60aHNQ3X5eDUpSDFXhVhSq4M84ISExcG6BO8_t-GpCs9gbZLOAGC0NlNvdtwqp8FUPnaW8IRJDTUYepiMf4yK0jXfoWM9gUzHFY0tRPe39HGTQQOsmStTAJKMdZiY5GMYYjgfXV6H5bEBZtlQr6T5GHkldqdQgRwEVMs3F49qJygSOObEV2-d0arq8m_wK_zUjo6q-OSbGr0Snbq_ctrmyw7oFhz51R8156xGeM6Wazg4dqc1p3CPwzE42UOMV5rwIxxMNIwoWc-8f_0_RK-3Vi95CX-ZPSyeffJ9ewxBATJocLzyhVLJKCB5XVjZMtBhQ9a6DxIJzi3zQKkjQQvSu7HsQad8bJEO2AkMQMkpwdxjXIKexNnizssRoqlO-xW_3-Wda1CRGaIbELFQRR5PVir-J0PtQT95vv27sc2tCHeAGuKrTr-9UFIt-Xc95pu3ryvB07X1UELCUF454uMBEj9NbIGSpYdoBsJRhA-2mluMf2zRCsqxZHM9DrC0u7-YMI7QjdxkL69KifiVILC5CEikqEhwS91sYDPnFYM3MfHIIv_--4wEKaHLwMHS372M-p3yiBMLEFBkSv0oAKFvThPOnhbge69fcruvfPjXh95XyW3Du--Yw2l-aTFInkdrd6xW8z_0Un1WuzLEHIqzAvINZnuv1nPq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9JcVdA3nO-YemAa21vbUepbOXAIiMn9x5mnbASOeNw2Vr7AbZ4q7kqcCnM9GTbvhHwBpLIedbvij9p3Kvufe440iZBq-4ITbOFc0WYQDd4s_kZia31HfVz2vucLKPebRkZu1cHMgfvtXqX-lFJqHBMZzZPmxWsbjPjosjFwGqJtORt8_ZEIInvb-IiBrQJon0pzaiHWM6Fp2UWVfbozOmJy8Qq62VG9h8OSEJyMdC3X-l2_u1zSw27wBvFA4DD7paZJ9o4CcVv2514nH20xvp5q1hZ_rggLuj8VKj6R9Y_RrOB4uVpGjihyTC4XkOiMGMjK19yp7AXOHe5XHJBpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90161" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmxd9squKELroL1kbDGnAcfqFDPXE004T51JoktTEki8Lu0WLbVa6WJSjZiECeJyRutZHhUfPYSdeT0l86qUreW8ekMR_A0vWs9jTjqYhv8iY3PkhXkNj8bZhJ1XRGMjJg5hOkFgaXkqfUQ3jvGhHpMLGmwpo2FJiAAgjczq5eXajlowT5uNQsBtCV89xfSpAJMoDtaboCTw77jQv5DtTagJsdWMvscq2m6Cln3qWQDDtaQJtFe51YtIOQl6QqIdPqnz2i0JXK8UkLdIuEGUJJVIng7BB7PGsftMq4_jbUs8rKvjCtGlN7IxS7ROvglFwa6aqbRDcB0ocV1X0hmy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90160" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=II1T9l_JqDedujPoyu6typ4SsI57O3XL4C3DUzyYJpGpYvvy4JFPMO8-exaYqc1MpH2nZYHidFg30Q17UsijWMypyKntVHeCxp7-XKpte-kAYqowlUVQ1IHadQ7cwhM-KIiRUfAMGQhfTdbqtP0h3_0PXwjCe6WdyKcF0Kk4vI3PGrzIHuswxJXkmOApgMIjab4r31qVD9J-yduQ-OUhzH2YmSKqyaxozorADV_0HEuDF23YHNsKgO9e22pTA9VqwcnQRVW-EkLFrOJM3uOsswIGrNpi4-yzCQO048u58cAmMJkCtBMktlmn1FAZ3Or5SagXcY2z3queYOVtxWs1rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=II1T9l_JqDedujPoyu6typ4SsI57O3XL4C3DUzyYJpGpYvvy4JFPMO8-exaYqc1MpH2nZYHidFg30Q17UsijWMypyKntVHeCxp7-XKpte-kAYqowlUVQ1IHadQ7cwhM-KIiRUfAMGQhfTdbqtP0h3_0PXwjCe6WdyKcF0Kk4vI3PGrzIHuswxJXkmOApgMIjab4r31qVD9J-yduQ-OUhzH2YmSKqyaxozorADV_0HEuDF23YHNsKgO9e22pTA9VqwcnQRVW-EkLFrOJM3uOsswIGrNpi4-yzCQO048u58cAmMJkCtBMktlmn1FAZ3Or5SagXcY2z3queYOVtxWs1rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1bstidk2h2-bVHmTVl75ScPc2OTjU15rsr1sakorqrcQqJJdoYRfWkhgmDcOyymJ0sV_69r0SbsEAy0KlXYIFOPGTFRUqKFKJYJBges3R40iJlG7-iBEqhjzHs_WFY7ZgQx0UlgVvIg-yj2BuAMkczxGS-hmbrxVKWQkKEV4v_x8Es_B8tsVb0YEdZCV2KdpI4pjgKGK6Y2vSndvqJE7t0VJeeRLKRM-mNbLlN7RBApMsCakj47N8cy2HVv-UaFN8LNLXxQ9Goz5gPp6a7v-v6Inv1AiRaCeqjjvB3hK5xtpyGF64CTWZ_oi52xL0Es4vS8F-aSD9_TmBUXzKCtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCAwuyoO_wG1CH4EshIb1DtoeB3cjoPEvwdczV0i5DqKUcRwDMhhU1quSlJK3yPxyeVPU-DpyvUr36IILY5BmGWgI7A-CpH0MXXjlduodrtEO4BBqbOu6bjVWqVNS6vPzTSsgDPPJB-ps8Eb4-gsGevw6OTTzYHMzsPRSInjRm4EcrKwDNNBvsDm19es_FoL7ht-kOsniNPhMIyqYsb504aB9QajexEqIphs79BjTqOLMt2vnKFW4N4J0i_WkuanwyeZ1OkA5OvxHySxjbK4ENsrBGxO_BG4AXXIU8vFBU87Bd_fHzv5BcO9WqhZxec-eczyX8UEg2s2a_g7GKGrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید - اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
⏰
شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال در
۱۰
دیدار اخیر خود در لالیگا،
۶
برد و
۲
تساوی ثبت کرده و در
۲
مسابقه شکست خورده است.
✅
اتلتیک بیلبائو در
۱۰
دیدار اخیر خود در لالیگا،
۲
برد و
۱
تساوی ثبت کرده و در
۶
مسابقه شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر رئال مادرید در لالیگا
۲
.۷ گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90157" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCjsstsjXq5vYMOxEwtUdajF3voJHgs2KEWAIyJzevvP5vp80koazaB7J-v2gIZdK7Fi_mSz3ZzRYvt9VTICsz3MNubRy-o_ePPn2ws2Vd0bBmrzb2bRyH--iinNtXB9o1wQm-9qJgSLG9lZXJDLNvyzsj28GQGcmxxChRJruj5jA8E4q99f39BvBHNGfmdnTOfwL_qgcZ-aM_lwZLV5g8katd_79tB-p8xwJnj5phmUBxh7-jVq9GGBUGpCpRun7VsptATTCaFL1A0ppGFFOFeQ1BQkSVbTawwRn-QFNgMMpXKJnFwOYYW_XokFH0bXdE3FjNGE3OXQs4pJm1GFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwsBRbLGu3p10nDokmvb70dpETk9kv7il1LNOvngg4jPwixFy4b4y0WUqwFCtzlx3Pw1BcLoS30gwYhUs7TRlvf5PU9gP7iaW5AxR0XZLeeUmjvONrtq9BZB2CV9iqBYvLNdNuhdZU-doqMo2G5gT1oprywV8aL7HCxAnK40c58GhCc4rtxx-og-FmhG6yWfsCZvuON0CGLQoGhPp3t1e0OYsreVSVc7mXSnEvhfz6Tk_oSeQoQnYLnTvtHRyaGEtFsu_YSa68OmHAj2IrnLC8HjIKBs6_TeQQuI0prY_j800C9NE_yLzkeGj5T_gpjwoKoxREjvHMzvoX6y9ziKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZviqFamzR078RovRb5MWHKI5H4gxNbkqilWvzKTreO0itTGPJVJaI_OFc1ryj_PwyHmht3HCu2060Hgk4fRiEgGBReG4ICoYGjkm-gjR1_fnRWMUXIf0hqreOELIGWnkSpT7d8w6oos3qaaSXHu_g_zz6HvfeaD2zzvQJBlq8QfN7ZqT815nWzsAI8PpuNfW4FIOR_tTg02u_Tbv5VsCHSwTNJh3KrMMIRQIfiG-APNONiZoK8PGksbXRaFF2GC8VZb03R40V80rWI0_4XkkNEZIAqU-0S_A5Paxtg_xUKPP2XeVCQqBZkHWnnjTjyqoxTSbQPVEjWCWsJ8Aefb9CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90153">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90153" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vns2yVFINv8URa5HDn9WYerGwDfoqJ6yxe-oXHIE3CVpmEKSc3ARs-xxfnGULfxpqZewOFbSf5OudouCjSsS4RI67tG-fcXmep4lfgYhKWJjpgTAUSviWBmpA1Zej3wNf_-DyS0rY0cgo0PRe0X1dmc_ONc61dF-9gk6-Gt-nIecZtcT6JttSxEZSImKpeXHkdXQ67gUNGNyT32WXiZNv6GjQ-oYPqEZ4WPh8Jwa9TIsZsIRUw5KKk42qQVUYFDCF_1iTjl__HV2TD6iZDUATPCzB_ZSeYEl66DTgdxiR9pzw-NZKlkXwHTmlGnsXw4tkzezEV-9yDOkULW1x1eImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90152" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9x3UmT9LLg_hpiZwuv-fgWVI7H6b8k9ORAXV7xOERPqpQNxinhvGRcKMVZkNWH95uL1rDzRdAWXPLBQGvSLPah8YFo4QCUC8hQ0Sqqtc1FQjygZEjDtkBvLg4qb6GPeZl29GDWuHm5FNqS_-8iL49MWSvAYtQ-XfLNgRbgeReOyV_BfAFEjgbakOdemI9AB2UoeQwNJSebtm1pvvIUGAUwHVRb5nj5HCZtsTLBeDrxR5VocT4TAh4pbNAkpUi9mQdCLYXV2ThH4CuJhEcwVR_0Jlyjx-zEiXhKSpLfdjdFS273QZojV-FNsCZR9PYS9UEpCMm3CpZXM8u3n81-Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/Futball180TV/90149" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU9G2DijnUVbhYTDiGLIY_z5X_2acwggReaGjfJSgW5JYi4F78S72TtRu-W9VgRuAxxBCRSQdxl-xEeQbdQY9KkmPWqhGbUFgEFK91vIaKtXFa8UOXo4YzLZvih1NSXNelEyeKyMSY5DNXxwEcEV7l5HAIwFAH4z5K1z-AaJhkBkGmUOWmmzx3D8iWD3t3xwPwHv_Jy7f3jzwqi0ik9aifmnvyeAYsOhCln7ebr8DJdQoKdtxC4Sc9RfbockTe1tMHt58DK5VZVbi9GBTWp1aQb6YltwnqG1s450WYsw1rKFha9WiV5_mLoYohMcUhRxlsHQX-XWmnfLRH5KOlBVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgx70xemB0VlfDK5Mdss3--DR5tZRsXfn1PjrIgDDwO82Lp4livVF5q2-GNGm8L1lao-H1i_hA3ksyyQXi3joOEGtayTYcDBa2UsOw9_UJ2BsFHsO20OZ9jSsP7hYIrLAHrWdhN1LfqsbFCK2hyR7L0V9jFVLJWThYVAOfe-_WH_dutDoEUYXC-OAD7G8Ec1cApbLRndW1hhdaOtlnwBf0pfs0Pb6warAEgdor0nr9YRA8IojIXJgpEVffTrKvFEMhekE1JV0FJ4KKHNZCyHWZ9oBkbM8LFlTZeuSxO4p_T3xtwG14BCAMYPq4i9MPCcD5iewz_mGOTYQpnx1DVlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5e1bBhrofU8bhRbUOkqm1DvD6lXOrZzUCkWQmn8F58_ljfEUnmxhkRjDS81O5qzUXjfeh7IfKefpk_UM61d-onSJ4RxWBejR1_uQaHSu-Kl8dz617D0DBQxoRz7p2gvpCBWXwKEQU-3Yy7O8DN6o-DoXE5vLJ4-d4JRpvcxW91M2Xi8F7259TzF3szjFLfHWnoqZ7_tlA78e-qT3OIax-xOEGqMadFi4B8b4x_bAAOzSlr5v0V9kz2MxbG4Yv18bkkTs2KVL-Aowqo7ln-3GhUN7AMKHsF_v6yJJt7CQ4DsCJ-t_V2UN5g1riaGPvSKk9UfdDRzUlNVVtj5HYsOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90144" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSEKIqFXUXPwps6xBToOfBA04198mZdiU8Jh1A27_T9ywBt72nZ0VW0gTNgsW5KdjCysm1W9P3IhcYeZ6QbKXxwrvzJNr9zMaKn7swFE8UDhWNRbcy7xqvFanpSNXj9BJpgD6yhjHAp6IQ_EPKUuKWlb1_r8VO-JzzxOTFaNTpZKNldouYR4sd7HESs40_pr7_2ppAP5zw5TV5rbsVG46C9eBwzrix54vBBHVx-PHBjmc3_jAG1IASC-s9k6PiQVmvglLLYcoN5_q1zZHbTCogVCSntHdYSj_sQdPJyDYthX-qnsjTLLluaFGNfBdCUZD-WF35F0t6jJ0dTSoj3Cuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90143" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEMbA2PrrOEPVi5B7j4fkZoTVuOuCrHipPorL1QiXgmpZB2Q-dmNkjyz7DPGmL3dTcpsatNtCIVOsUIHFTlns_B9ghBuuekpwNsEne34jZxD7XMq3QdK_ElhAtBzyTzfNOYbreMqTM4YLnHZu-STNRcydO_E0jeMuy_S6F8pGtQo2tazJBeIL1obfDTfStt1dZzGOfTXKmuk_qAx-JNE9TN0L6-JB-GF_-Pj9JLdlMXCBsyUJn9zPVbk-3rwVTeeHW9xPUPglPnN3fetqJpqNEQqw3oJ2uU5tirYNnDEEMhUNQgIrHHF4h453Gk-nJbzrRx9HuPJu7p9lLfVT7GbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7xy-8k-kYi6AOLGuUkPeAlGlvcwXU3O6HuL_t3gh_QOFkL0ZyL1h3wRt7AJzZ9ABmTtkipi9OXYtQchxeRNj5NE1nM4Na0zS_rRJC3-yGY-jomlVf-m_qgtRZYf5JdJ9G3HV0bbmpfZTnDoXTVQXZqRXAlb05Y-iHKyH9iV-GlAKSR59fmPY8iavHeYKNA95EuQDHIm7SRTzg9SWvvbZ22G6WmErO2b2ekgvvyyDGhuVnI65EBaVi2Fo1ZBh14VyCEoMmJv2T0X9iSfdw-60anq3TWo3mb_tmQXMa8Rllb36efP9U4qrAhHVMXMy4x2unseFYmgYLKIApwBiGDErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVWC2LYv4WrMiT9WCzO-jwHuv52DhyX4rf5IijtDZfPInjni0Td8n3xTy0TIGq-FDV58zU3-TMo94F_oiVaSLcnv5DO5YBGZ0FG91Psj4eoDJK42U56fxMdPioYj7MnkFjLBTrbZmFBcU96LmU_WTNBZ8brfipUZ5c1Cvdm9R5lgAWKBGCZDOHW0NYyAnFrPBkTGqBy_d3CKvqlpVEf0pcZq4bqQ6rF5LP1X2kKtQW7Od1IQ1htqAbyEriAJYsX2yKwImUqYt6H8DVB2qtLA0fT4Z94c6-XZZYvE9d1ZCLOgZ2QlsqNokK-rbuSHgHdJdizexqoZ68PkAGy9WlNYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/invLDKFLc2lyXtDKi2l7SDt-l0mx2cuXbPOuFLtrY2sJ5o2fdeP64rdlBv6WqrGWBTyRpHxQJIXBSv4pP1vyni84qhlBdsD4nIgBlChqBvMlr4MzGBbecBI8TVs4Q_qY66fz6e1Mqws4FlMbN3m-pZSbsTFODAJwbSUziFZ0uSL8q3uLjLzIOrI1bvMvX4M-WAno-BSTg6e32xLQzmrfyL2PaqB_riczzQpCq9nh63S1X5h0RAYramHQw01ROwLJi51xa-UZhZGz_1IERvtXrBt-bhxm_OQ_rnL6CIUzl6NNrqZz3to_YchmUnv7lMKMK-95_HUlKoKWzaVBPP_Qwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90133" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/90133" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RexAEivHmAmmiFCiVG_ombRTxU_qIG4ZQG9Nfx20cfxCpnUeBdGCHPGX74Ufw0U0v3hzX0izFfXcjrqsjDcZgSocj2G_fIAYVeDfO8mCVebejbpbINMH-d127k7oDjSPMW22wk91jHDwdYZ77EJPruHYPGPR9H_Njy9Uyr8dA1ZdfuwjgxV-mbIX-I7SdKw2TL2Yi7BexsU5EfRI7PKwwWMLXvm8psm7yqUPKm9-cnq_kVDTNGqP2qttHPwgFOrphAwN0uy-IFHecqs77-vUpAw3hYyHU6Bwir8VyjsIguzBSo4_FA0EVNnDrjN2-RAr2V47l4ewaaaW-s8oM20NeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90132" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuYlAVUW5tl-oykRdgho5CYte2Enmoa3JSeruKQK_G0zZC6QuO3vytDClvnTDKbQFOnCbGUKgdnoEp2Hr0JmhgZjXUmjdItZa_H-6OdslG6_CnwTTKa0qi8Uzl4s5ggFSzecz1oGXTcFCrUYvMKDiWfsFpXHBcwcI4knNv8MJyFk6BJD04l1KGI4MFgwDy_4OjyVXWzPNF86GL24Ul4UlHgFQoal-jFS2nskfH7SZ2Mvu0_bED541g5IqTLaPVOhFfsDATL9fjKO5vfZShMhXJ68-L2pH2JaMdxK9EtjFH9QDQstd-G0uyzGrySrTW7CzeqcfRzoX7XlbLX8M_nUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90131" target="_blank">📅 01:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=cGdZLZsa_liPT89UpeccES1Uq4dyFGWqlqcLRubSt_ju_rXdqeXgHJKuHG0WMYWeE0XRTyysROrhYz77PSolyf5axygBhO2xpjZHq6FWPwkh9jimm2qUqJ7LwiKskXw8_JQbkvfa_t5ED2PKuV7IgovpC4OFocO5i6_Hbt8vx9IlzJ9Qiko7w-CIiOORMS-QcJtX1GW0OjRUD2IsRL-ayWaVDVll3GY_vrmM5D2jPFEoqh14SAFbZAn6bVTbpbhKTn-KqkWLqbuoRQXXjQVyXjEUOyGArTu7vebe4vSabBOnVsFNz3FEXlBeKnfj37KlbyJSTPyZ2_IgbtjnhjXcaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=cGdZLZsa_liPT89UpeccES1Uq4dyFGWqlqcLRubSt_ju_rXdqeXgHJKuHG0WMYWeE0XRTyysROrhYz77PSolyf5axygBhO2xpjZHq6FWPwkh9jimm2qUqJ7LwiKskXw8_JQbkvfa_t5ED2PKuV7IgovpC4OFocO5i6_Hbt8vx9IlzJ9Qiko7w-CIiOORMS-QcJtX1GW0OjRUD2IsRL-ayWaVDVll3GY_vrmM5D2jPFEoqh14SAFbZAn6bVTbpbhKTn-KqkWLqbuoRQXXjQVyXjEUOyGArTu7vebe4vSabBOnVsFNz3FEXlBeKnfj37KlbyJSTPyZ2_IgbtjnhjXcaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHGIRisgHw1TCaX9F6EBSOVcMLhCVzEhzFYPOH4tXR8OUZNbJbvVVPP_MDWdfkFtXQMgFmLHqnvi0FyY902eAXzY9ZgdjufkE5NyHb9THk3nny9I7j8WeP07mQdxGhiQQElzLSrvhovLUGUdN7gtARsP0hfd6W4MODjoYePb_54StSHmuvCIV9zF0nmillEYvmuYbpwaGDOMBwpxsiB4YkjkfhGNxX3w3QZCxVFt4vze0RYVeqowVgysEz8XUCTX0eBhqOkZnH_WXkqA0MwkWXk-GWTXkz0ilJHxTlD6QGW01--zBHcZAyo7p0eqGOlMyMUhdfALU4tCnxR0YW7gFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdad6VVshyb-sPgPKezl33YNcT5BYyX30_fk92D34MHd_v69C2K-YKr9yhq0gh66PHCWyjZDetk_EVWhrb_DosubtKeAODxNuKo7xU_-X3ONuITBaf8_G6kg0Z0ne9Ury-_QcrPl2mKtGqBbJtUF7oQ0epm-lIiXuYpmeFiKGjkP-Lz_cxVFcbL0yJgZgF_wOCDwwo8utqg7m1LzLwwMBFrB-QNrS9BtYRu0jUh5_vWEEvVT03fENCqWFYLlu8vWDIfXqFWcjeSoclZKIOrxlAUHSU1JXEA5VqecRIZgCORO4A1bU0NYucOkpfSDKhVfax0YHx4NSxxX43WfWfx9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdJG6U7RyIE4rXdtR6OlPnXI6SXBom3LQ0-aiIqiY2-LjhoHx19mUaKt6P6gqUsiTGQLi2gn_l6-yDqGpy9WXc4jMq7dG0YRY0sboiAqiGEk3E2dgcszvovtZuE35xQ2SVK51lAqbhLk6K_rSXaau28XGGdatrpZVul6AZaMvVoavOXhUF2m8jJtJJcEuAtL_2uJBKTUotU9TiBBHWvouaGSlPo5wjDSfQ1XL4g-iVYFWGqYlO82uZzlzHqgHdEjT1RKyIsDhRsKdHOGBMaF9iCxdf1lMK8DcCAIp5GsZWcBPq6mI19a8ML6HaIC_M4AMsQb-29It_KDkViWew3L0zb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdJG6U7RyIE4rXdtR6OlPnXI6SXBom3LQ0-aiIqiY2-LjhoHx19mUaKt6P6gqUsiTGQLi2gn_l6-yDqGpy9WXc4jMq7dG0YRY0sboiAqiGEk3E2dgcszvovtZuE35xQ2SVK51lAqbhLk6K_rSXaau28XGGdatrpZVul6AZaMvVoavOXhUF2m8jJtJJcEuAtL_2uJBKTUotU9TiBBHWvouaGSlPo5wjDSfQ1XL4g-iVYFWGqYlO82uZzlzHqgHdEjT1RKyIsDhRsKdHOGBMaF9iCxdf1lMK8DcCAIp5GsZWcBPq6mI19a8ML6HaIC_M4AMsQb-29It_KDkViWew3L0zb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=JrMUdc0lXMBVHTXt2zwK13Wjs0Ydkn3mETAZxgQWzH4Y_ZXrpbnUtqxMfsYjqnc7VR3VdiyhSJZyrPInoiXY1vuPRGxJnMY4AsbPVbIlczxEypQla0OByGZjIYGa-yQuN4Eatx-jQKhNVGOAyGyBlJet5nOuETcArmbIiIOwMzY_4ndbeA4qZdnofxMjRG5S2hUs8dLJKuvoXSLqXSQvElC_JDqwmJsAyMAWpaolj3ze3ioY3ajxo0Zck_5f0LDMSJjFfcpIYGzsqfwVHtBHqf6nl620A9FhXeCV2PPGEu__bCq6rI-8MZCQk_0VDXIbEGJdQwDeva_jaVYZ0Y52Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=JrMUdc0lXMBVHTXt2zwK13Wjs0Ydkn3mETAZxgQWzH4Y_ZXrpbnUtqxMfsYjqnc7VR3VdiyhSJZyrPInoiXY1vuPRGxJnMY4AsbPVbIlczxEypQla0OByGZjIYGa-yQuN4Eatx-jQKhNVGOAyGyBlJet5nOuETcArmbIiIOwMzY_4ndbeA4qZdnofxMjRG5S2hUs8dLJKuvoXSLqXSQvElC_JDqwmJsAyMAWpaolj3ze3ioY3ajxo0Zck_5f0LDMSJjFfcpIYGzsqfwVHtBHqf6nl620A9FhXeCV2PPGEu__bCq6rI-8MZCQk_0VDXIbEGJdQwDeva_jaVYZ0Y52Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS_RhiV1eqvx0HownTZny3udmIqax7iGwVIImZURXvDdNYnZ6tDzboXuQb8553zUfgwjSF4IvAVutmZvcKkK03eYYrBGIhqbOxqgDZw7qMBEt7vhw-5uT7h5lBbEXBoSJtduUsVCnGsglM-HDbhRVFom6FULFkluayMXgjK9mQgd3hQRw1c6yJukyd26w_Km2Lmm8ZjW0x5JGrAVW42hq52ZHMuk6tUrunLG4a-Gx6DWT-0xJgkhJVi3pCvaMZjCrlF05JwnYtWtgwR_hw9V5aUjZeN26urWnVcHRAgo4KpX-RdEVzY-DlAhuSBHhmPjmu6OK2dKrbCdKcCGFoqDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRSas3syCT3BQ_33xxnRJKh7xaUAgkGEsowJYLwIeAy0wbFDYPlUzHpxiKfewUv6ATL_gH153_pdh6UYSpiGQE5QN-MBgkRS6aDVLO6JIJFapGVgc24NY3VDYwS7XxcggXY8DTbAVDxgymEjLUnOyfs2k3Wn_yMYT8NuuhiToh-TuNAbFVHgi8Hw-505FesTte5-VCUDlC9j26UVsodprp6RBVbOsWr33cxD2vMwXiq_T_fzqDFAiXthB3zEFb4fd9Q3N9rKgx2bhQB0PsWH5xBTT-YYYxygwSfDRWmXlC0gwTyrrTA_NfuB75fv8JXdF_0u07Xjqfe4T68IFw1IYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90123" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/90123" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz1iR47ammyAIUzBa83tXgVBmfrm43d6A-lrPoTLcS0KRRr_6Lk6v24hznsC157Z1iV2uI2Vw_IkKTCVDB2pfLXNMd8WTQyp8nXTffe3UQryggw02iuZxj9UrkWr-ZMuJQRBA-1d52mERaSXtHZaiyXg1a3-psanDupVCoeGFzWN8wJEghT78gKRGBKItnJw77JgL9y0Azat-ydBGCHd2lgvHhNS8mbWi1VYjmWygY1ykOB69uwNWTV98sYH8-fdn6wzsM00UR_zW9-cEADMHVzRs1VyQMHSxprJNWONtDTVOyflqaPqAFVcLcAKTMWa3rKXxvwrtQskpfIeqUiZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/90122" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCjQIjmRmEDMvw5pcTkFBH3pVEiJaySRVfHnuO2KlHUkRZ7AgfewoGCIymizdHBkW2pYW4LdO5WQtxfR5lEZUObJS6xgfAgwpGEXXzhcUJDvDcE_SNRqbLZxvf7Ja0JpQ_2XcmL21tzFRtqZG112THbd7EUiBy2J2vgPku-q9KVnbzSi-R_UefrW3mWnTmdLpmOJGEunCVv2K8AGLNA4i5gtYGUl5IExexAFGEekj9XtjiVVyIzgCHjNJUrJvvoaZVpPIO9d0H7f7ZBSOi2QBjPrunnAxkR9Zba-MFKZc_sdt6-9IGCAwcmtrj8VJpBZDB3qiFJpwyQTUaiwcucLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQwipfHkrAyRrWOtBLMD0iRxYIrFMdcFa2_u38wEvz7kHnqoU3tvHmLTO10EqoJQ60XJslPsD2uP_jm6lGezZctdEVbWO1jw7HudYa1gju-06qMmlInUspfnRhS9BqO10hyha1fHeLlCN2W5qvFZcg4vi9j0uAQfTnNxP5ZsuXPY0CdUQ7dDLzn9SEM0qIEuQ_aobh2xeIR3VKmZVMn8u3FjNrUoYeuE4_vbeebYL0uJz9oM6FB0Kd8wocbjOTbfN6_42Q37j76K-8Rj4URvygDe155qHl4f8ESaT8Pi8LCwpn8SHfi3ArrXbNkU9bAtdGydy_6CkukU9z1FSg5Iqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7p61bpGNQrLO8KRJGE0SMveG-TP6zaVrrczmcg01aR5jHY_a7MH_JbsIZb8ksmHPEFPjDH99ZEv2l0AE9x2GBInqdnhSP4ZYZD08uRwHKqliVUMPHuvm7_4OagAex4-__MZ_ObIPdY30ybZoXgP6Zp34o2xdxTfoy9YYZkr79w5lwR-k-4a83QoZCiR2k36SEz_yhQqD94OzgXO55bMbOTslHORMt1kvQZ7VnBi56z5AcBSVL-5J0TrDQgSBz5SmMuosFQH0hllYHpEQxo8Neq6S3lneom9-3LG6IyfQO4hYe987L29UM3olC5FmJuVCZmF3_9O8PHXaPtjpCVyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCDvd1qSIolrR1HqYq2v_uOHkShtSPM7-gCEUu12U1QtyowfNnIkeK_x_Mfz-nnHwLTLnB99EyrU6wP2_KiKe5v5lcpsZdePCL27LyHj7319lfvM3zStL4gJWi6IgKWIXPF4Vz8eXZmzub6Tk0VNO_o1KJxC7lcoMcZLD4zCbrLmkpGGOLrGjg4Fu3dkLn6bfAEjlhD-k_ZKzZD2RTthaq4y5NfyCiIr7Xmb7Re_W1IT1zjSEbI6vfGLUcMr9rYj2ChQytJYl-at6vm3rnK7LvXYRB83-4AShJY5OCgd7c2WNq0AgH5rNdCeATEkfXwLC8-OIWIR6zu50cvvSaLdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaDkGXjAn_MZtmb9FJ_H4NIBozWC9NvbW2r1QeijseS1FBL_gxQyEmrt9sydr4Uvyc9p-fYcy_eVm_XNXVoQxU8yn14rYojQvwY4-YUmQJC7_F4fTpGfal4fZ18BSq-Vc5XayYokiefcnCTrAQF_xdo10vd-th-fDyU-gK0W5OWUY6VzzYJsSg4nZLEMPLcvm3-0wLJBQoWogbFje9qhjn-lSnQWqE95Qf_h3-3y_Bsb43riD3e5MwxOFH8JlVdRMa5hhWkbfy1E38fNFdTfKxwQCM9KbfQaWAXQfip_Lb5-_yRqUlgrXQ3wU_hN7xnFsgKwS73uNRz1pbpG1O-C7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkn7N5BKcuw91b55_DvZry59ml2_xjvsxffcumjhf_cyf5hHXSzxtMsgrnHNpTxERWup5Q85cBHLhq9y2OwbqM4eHk1PWB2e56xN8Hk8kwlDzyp5ye6HBYl3K1bjTswg396UUh2r3RaGROmVx4SWhPrFs-ZoiPrmYJL_hP-lSYbMP6ZrWaAQVmI7dwIyI_wSu0iGXbBk1Bc6w1dfyRSn7Ze7IrOTk_ROYGU3cFgQAXFytv8KmqKVTqNwSgT13HDwvVCTBdsgZjcMi8N9YDCmK34tR_iSsWcrm2fcuRdBC0_SgBKvLwQ6UGr8LY3j6SCqKqiBTCVbvdv4xCtN6R1RdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4sVkZniYOQVyHA9Ip45mouedGk4UGpZSneVvZ9_LGhTCtT11zd5oKTeyUHncVLQsg_twNUGUrpL1VRyVDTgEC6oJ74A0I2ZdxU0XdoJBuU0ZPLpqCAdIrdyC8NCvUHLAoDI5cxePboQ3690CbsKPWKPi_T8GXULg34bxpJHYYykNwXu6AscPbSXbHFzauYwdZ1poQwe0PYaWzPZxPcSyocD_I1p2BsUC2Bi5eOIgtD4wFi91yBc-H5hEG6oqik2Helo5ZEeFjdM1Ty6lg8VMBpBrEuLsMf6UDs8Gae87E6lqNlpXyujZfPEL1q_m4HfXYZ8brLNkhxKqpo6m4p0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwp4KcxizSu9byNeTZBzEusU52Bg9hc1UJxQVRUX8z5WhhyLjaIWRsabTs9Uhk71vymV7XScY7hQ4wJUdfKxTPo8EgEIg_avvkpoqIA6sVwD81VyLyXDdGjTF_SKG6DYC7dpNNF0NsV-mn-qP0okM_zRPAKmx4bf446_JfpqWaiUVVTQTbnjJJndCywD5HcTYfEQIF_Y9CLfttBQkpIHEsShu0cR2ID8QSfqu8ol7tpxLRDQlky9qtWn-YIdyTFox4rc1U2dyqpAoefc2N47HLPj9oHmVVrkcQJQfS_3g4oJvXMcXoxXRH5Va36Yk3-U4bsX_EB03Y-C7qSKl6Y_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=J07AHRl2HWT_IDoiV6PkC8ozJtq-h6icKNxTK3sTI1AuBwbLwF_TT4ANPryasoNeyRkgEMfsEZ67YYFl9ICYe6QMfGLV7dgh1MF8pVkgghTIr1sH7pJMyu4_xCyNq1XWULsp1e69HMdBhkXOmg4GU-F-z9AW8CC6zIojSVpD-HVWLXTuF7cfFvV32u0ZCxRed2oliRy9VD1Mgluh7gzvJBtKQZ9MBBgNZ_dSGDZW7RSCLCFbMDAGC1asNV1V4GAPkxkn9Y2KhgI-tR3qrvxWiRUhXA5ZOmG9fnvLR7OsWM8YjSxW06DzuLa8XBjY4wmGaV2fPyhW5kBzm_h_JDLATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=J07AHRl2HWT_IDoiV6PkC8ozJtq-h6icKNxTK3sTI1AuBwbLwF_TT4ANPryasoNeyRkgEMfsEZ67YYFl9ICYe6QMfGLV7dgh1MF8pVkgghTIr1sH7pJMyu4_xCyNq1XWULsp1e69HMdBhkXOmg4GU-F-z9AW8CC6zIojSVpD-HVWLXTuF7cfFvV32u0ZCxRed2oliRy9VD1Mgluh7gzvJBtKQZ9MBBgNZ_dSGDZW7RSCLCFbMDAGC1asNV1V4GAPkxkn9Y2KhgI-tR3qrvxWiRUhXA5ZOmG9fnvLR7OsWM8YjSxW06DzuLa8XBjY4wmGaV2fPyhW5kBzm_h_JDLATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=eG3oW02RgPT0g2UKN12Xk3R3b9kmaenXVuvxSlcq8lKVS4RduZpJBfjya94X4GnSMwWAKdkEwC7K5cKfS3Fg4G9yWYsC2V-VnI6mr7U3-nbI2RsSN1q2crozePQXEb-4tFPrmeQ1Kzgr9h_OmcS6UwFoQWl5pfFraGRAFUF1Znjf0K0Q-Nwk7218tEFOoQYrZFFYlQj7GT5uMiKQboxnQWGT6WZO5Dvk7QJ1Kjuagz55xqmlZK4gWw7NtmjviDTvqXmIR2Wn-aNj36H58NaaB7BtyegjxPNadPWqaxSkgFM9zP9rwzXR7dTIGVMWh_hO3LSvwSB4F5YEfvF_iqd4zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=eG3oW02RgPT0g2UKN12Xk3R3b9kmaenXVuvxSlcq8lKVS4RduZpJBfjya94X4GnSMwWAKdkEwC7K5cKfS3Fg4G9yWYsC2V-VnI6mr7U3-nbI2RsSN1q2crozePQXEb-4tFPrmeQ1Kzgr9h_OmcS6UwFoQWl5pfFraGRAFUF1Znjf0K0Q-Nwk7218tEFOoQYrZFFYlQj7GT5uMiKQboxnQWGT6WZO5Dvk7QJ1Kjuagz55xqmlZK4gWw7NtmjviDTvqXmIR2Wn-aNj36H58NaaB7BtyegjxPNadPWqaxSkgFM9zP9rwzXR7dTIGVMWh_hO3LSvwSB4F5YEfvF_iqd4zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=LdGy88k_fliBeHVxawoM-F_OM2_qlZN4ojHzG8v9ycDlWs96iip2Izp7-PVpEBlkitHoNS0PsqKXLrUa5ZCKaYAp0UJ01AS_VAYLuvaHpmPRGCsf-PcEqpLMoomTc6IOrlPhfsC084Xd6bwUZL-CIC-lmaGyPXr_0YOfar5A1sWwGQmc_JSiHLPfmOBsocYBGn2qI91F8Hq0WR2oZG6IbreMoMq8lJ4nCcmP7u1wxerAROdqHdkIy5DlZBzhrI_xIewdp471XK8xkMIhiIaDloCWqfQ19sHtuefhiqzNA5KB5UMAfwP7vVfPwqBmvz2yRQA27Evh6j8n88cVhXDtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=LdGy88k_fliBeHVxawoM-F_OM2_qlZN4ojHzG8v9ycDlWs96iip2Izp7-PVpEBlkitHoNS0PsqKXLrUa5ZCKaYAp0UJ01AS_VAYLuvaHpmPRGCsf-PcEqpLMoomTc6IOrlPhfsC084Xd6bwUZL-CIC-lmaGyPXr_0YOfar5A1sWwGQmc_JSiHLPfmOBsocYBGn2qI91F8Hq0WR2oZG6IbreMoMq8lJ4nCcmP7u1wxerAROdqHdkIy5DlZBzhrI_xIewdp471XK8xkMIhiIaDloCWqfQ19sHtuefhiqzNA5KB5UMAfwP7vVfPwqBmvz2yRQA27Evh6j8n88cVhXDtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e690AFiMJcwMBj9RtN9qFJQqGnXlGQSc1__gvelT4ow_34L_i1FOOOeq_4eWcN4Xb5Lml_bt6Nf4CL3lMcf36fCOclpUXZ5jstdhjavrHJxBN5_Fu5XD6r7b0kyCG0DoRXsCBn9IAO0D7fwWKqZQLtRo1FipOMzenfeT40bLoYh3nu6jd6Rg_Lp8V1vuH7UgPRs-oHZgE9WghujneBugVb0Yc94WOnxyoppKg4A6rKKjI-GbtY9-57vMh3p-qKhel7FgfCJ2B1i50ZeS5yf5ntmAmwGkVrxSGfHbnQjYGVxZ3ekAfZGSSEhHZcN_8prsL4GiYqoaoDfgtgYg5-ehzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quJ9QUzjEU8xF4sEYGld6cV3UkR5VvYQsB-VjkptGgAMabB3riGjDdl2Eov3Vv_swnSiGxnAg3ySn3l_vKAMxsXpN7dJN1Uw3mepaAvABohk35VitwJMC-ck-YEDZ12OLjzTsyRLngmkyNGao2d2ZbOAUAOpOkiTfdLnBTFwZ_7vjLI3f0x0ESzuWqmaMDWozP6NIiMfLC5Wtu-At799QkKiGRD8OGvpwuqh3dl1pn6T122oYgxnAShBa3LnmMcy8PJvmLmOYSFZYIbQiltUo2MlaZhKW4Wvgbu7vUZ-2dMiZtvXr8n1_9nX1ur0b6q41NItiMlxZiLD6tEs5jV4Sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=iUfSmiRQ0Q5vd6biSfIIwPHgjFnt6aKhyySM83YrZ_eRw_M3_PYnmplCetXjA6Qw3HAoJaYz1dA_dvCHam9ETBYpFkgzKDOZOHHgyL0cMoT0jFeyIFb8gf4JilnZXQaZMoxlOh1_1R38R-DUpdsHFYs7Db-vWc1FaBfln-jp8Kq3IpQoLyR0jjzZIejsRPaprNwEDGd7HyFY4DDdkJRHpDtuOO1UYb5INMORTjo7X542TgaSakfzr5TgYxIk3hHQZdvpJxe2gUmXQP8tslGb53rX-f7cMkLAzzjvASX7GTP5OC7XII9Vj3gsSXKacVUJ633SoR24N7PuOa2ra8SQJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=iUfSmiRQ0Q5vd6biSfIIwPHgjFnt6aKhyySM83YrZ_eRw_M3_PYnmplCetXjA6Qw3HAoJaYz1dA_dvCHam9ETBYpFkgzKDOZOHHgyL0cMoT0jFeyIFb8gf4JilnZXQaZMoxlOh1_1R38R-DUpdsHFYs7Db-vWc1FaBfln-jp8Kq3IpQoLyR0jjzZIejsRPaprNwEDGd7HyFY4DDdkJRHpDtuOO1UYb5INMORTjo7X542TgaSakfzr5TgYxIk3hHQZdvpJxe2gUmXQP8tslGb53rX-f7cMkLAzzjvASX7GTP5OC7XII9Vj3gsSXKacVUJ633SoR24N7PuOa2ra8SQJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1xkfvnJvlxSPUVazmSKpia7WLnSL9-f4uorM1rnFji9hknTmoPzacaOLDKE6WdsbdgL-M0HpynhY806JeU89uN11NJ1vjKN9MD3oa3wNWNut2lYz3r2XYRkI8LD2nHID0FbtdzjtAN5SWf92PGHPAtdPxE4VexV9-xBtX5MrlppRRTZ70IcDjlCc5LslL3HCjb-mv07eYBDqn6c3Vwvjdua2KEG3Tardqe3P6_4dMW4Mpl0FcE2jAd0fniuIrM6MsANCOsi31Z7fmNwytEr39_G-yCzAFMwbZ2wdTiQIeAgzvuvolwAdukn2QRCj4wWu0Dddxm5XqVl2ON_vrKBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=I6qvs0zc1U4p6K-nXoPY6T1666Xr5gu_Zof_fQDXiwZDREpdrQdDFInH-lMu139HRleQm0Z2dJg8sCV6WFJwqSRB1KXtGb7tawrq3ieF_2xO0cxdZ1DZ2D7NZqEfFfDRPuCRPeJKUmOYfn9F1v_1Th6VaZTKkDMFGCb79RCZeuw-4EW8nMgYhqL02mT02xLRhLm0I6a-PPi9n40XQg_3PlMutFBpyl_gGsjGpRQLMjZgqNKqV-rI1LMDGUJ5dV8xLxr3e3zohiaL0f7R_-fhWmNAgvhXhiXhPfus6IpFHu98Y12PDkg1K1Tl-g90IR0zicphHPetQkI4Qw0AzurYrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=I6qvs0zc1U4p6K-nXoPY6T1666Xr5gu_Zof_fQDXiwZDREpdrQdDFInH-lMu139HRleQm0Z2dJg8sCV6WFJwqSRB1KXtGb7tawrq3ieF_2xO0cxdZ1DZ2D7NZqEfFfDRPuCRPeJKUmOYfn9F1v_1Th6VaZTKkDMFGCb79RCZeuw-4EW8nMgYhqL02mT02xLRhLm0I6a-PPi9n40XQg_3PlMutFBpyl_gGsjGpRQLMjZgqNKqV-rI1LMDGUJ5dV8xLxr3e3zohiaL0f7R_-fhWmNAgvhXhiXhPfus6IpFHu98Y12PDkg1K1Tl-g90IR0zicphHPetQkI4Qw0AzurYrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=fxu96bp6YO15WhToxBdmz0tekNSNsopJ-gm6_Zr2XH1i0HCPJdupfwJkPasn1dj-d2t4YMtwqfUF6FqyAdJeDOgWhNLLPHnYtSdG_riTb_lOw4MLMHnctVv5MCEjpv35SnW0XCl-NTeErwkfo8UnoPq7ClBi2ek9bWugbhXM0byCHEvFjnFHadyuFHDyjf-qeKA41gZ6Q0mgVR3Ely2jVcTnwqqjUocyZ75_xPI9Hy7ubFz0azV26lqaM9dzGeO72TqOOEkTtPNof_583xgzaB4T1mLo7RI-9BtVZYx77TWtATS90v6T0H6o5ze_kGRXfle-GEZPuKtI1MkivauyAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=fxu96bp6YO15WhToxBdmz0tekNSNsopJ-gm6_Zr2XH1i0HCPJdupfwJkPasn1dj-d2t4YMtwqfUF6FqyAdJeDOgWhNLLPHnYtSdG_riTb_lOw4MLMHnctVv5MCEjpv35SnW0XCl-NTeErwkfo8UnoPq7ClBi2ek9bWugbhXM0byCHEvFjnFHadyuFHDyjf-qeKA41gZ6Q0mgVR3Ely2jVcTnwqqjUocyZ75_xPI9Hy7ubFz0azV26lqaM9dzGeO72TqOOEkTtPNof_583xgzaB4T1mLo7RI-9BtVZYx77TWtATS90v6T0H6o5ze_kGRXfle-GEZPuKtI1MkivauyAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
