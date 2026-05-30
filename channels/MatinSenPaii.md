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
<img src="https://cdn1.telesco.pe/file/DVl6JgTUMrFCax2-z4Eij6PNo8sjbYz51XNXn63PcGQNzESOKt_Pq4ejZjZ9FMo3qIDcJ1m_FI4QwpG0h8h7nRmKjiecHfAkP-c-wWeRqYl7sCHQ0yeQrKuDfV9tEvzCz-bKoUVPmmcytcM8p8G3WPkBKTmqzAkgNtxeS94Ai5rn3rnr1NfGAtdwSU36Y3_7a9JCwRO8tlmSDSaq90cn9E8jpNCvSyYIJMyB1wDpeG9ovNnzX8M1D7MlZIoSU29fR9AbIw69GPOnFsiLb7OB1cy21cJ5U60dMR7kz5eN4Ut8dndwVEqYVuWfEvK1iKMcTcl1k2YFzIz59r_gY5XfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 18:20:33</div>
<hr>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN6oF-xDiVJA7REBMznUELxpHxlscLxOnQDsQBaViiK_t7_qLGJW0VlT9i7TqAQCd1j2F74diss8hB05UTjkRMA5ysDelZnQFR-EruCXf7l9WPU0dRbnQVXYkwbXt8xToZStSed2j_0G0swuQlri5F4dWBHgCfUL5GrqCIaklR-BP6K9BjTAiXHFGF6MrbHGJWdZ9hN2RgveC6ZhVCgdyKSpYtkKWDUuGIikwv7YsTabQ1k1e6DtY-0v6_ziu81npU7T1xkDMEUNrlJa02OPtTbZNYW_NTkxpo_N_MaPiYsiY8Wiabg4D7kCZOH4-LvrzNX4pEQaWimMF99_G3apVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این تبلیغ مزخرف رو اگر این زیر می‌بینید ریپورتش کنید
😑</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/3593" target="_blank">📅 17:07 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏دوستان می‌دونستید که این روشن/خاموش شدن Wifi ویندوزتون باگ نیست؟! به‌خاطر فیلترینگ شدید فایروال‌های ایرانه
🤦🏻‍♀️
دلیل و راه‌حلش:
تست اتصال مایکروسافت (NCSI) که فیچر ویندوز ۱۰ به بعده بلاک می‌شه؛ به زبان ساده، به‌خاطر فیلترینگ، ویندوز فکر می‌کنه اینترنت قطع شده و برای همین هی وای‌فای رو خاموش/روشن می‌کنه تا اتصال برقرار شه.
راه غیرفعال کردنش:
۱. همزمان کلید Windows + R رو فشار بده (کلید ویندوز همون لوگو ویندوز روی کیبورد)
۲. توی کادر Run که باز شد، بنویس regedit و اینتر رو بزن.
۳. برو این مسیر:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
۴. روی EnableActiveProbing دابل‌کلیک و بعدش Value رو ۰ کن.
۵. سیستم رو ری‌استارت کن و تمام.
دیگه این فیچر غیرفعال می‌شه و VPNتون قطع نمی‌شه :(
البته تا وقتی که غیرفعاله حتی اگه اینترنت قطع باشه، همیشه «Connected» نشون می‌ده.
✍️
گیک‌زهرا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dXjNLG-Hh9IvX7oQ4wLoIOkl5fRIPxXWnY5PJUNeE7mxl3K_9WgyNxUIjsMnqE0xQVsUZvAWdwH7c0rZhKOuuZOgNoJQfQ9Ct2WbPOG2jOwpChKxFOS-2lj_86GhdKVlhSHSZkmfTsMpzVwGwtXjTQPMQ-MkNXO4I_6MSc2-M8ANZhMmM-2O-Kml9yMYEB4HVwtED-jdfm8gZO46ha4UvJe5UICLbObijj8vsEOVvrJKP9Tf3YwehqtiqxsdboKX5OhBopFSzvNcu2bhSQc72bMSPlWqgwuhBrDmrKmne25uRpfHQM5WuynAmWktAIhPxKh_X5uhuXAGCBL_n52nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TDG1m0xo58pPpv1LCEs2GaeACUh16HbOgyYVz57pT8MH0Fa8wTuVTufs358RJhC-Z3n0XqCeh8UCcadoygk03viGFLXnLRGwtr0I-i_bGKG2PMfQCOfUsmQ5OWi314BMTFXN7bYA4HSogFvwtWt3FLZHidrk1b5X1iDUQCz2qNBBUowtmXu56AmlTz2OXsdgfS86w4sdNTAm1_oJhVGzualYQ4BGdg9R48lxhLl9h_3BIZIOgnF5eOGCAYFiR_auW2E21Q29vZQisnxHy0QRJNhgv2cS5R5FSMneTumDRKitJ0t3oxaUNeM2kxXce71ZutC2Szlag71ZDN99BXi2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XxDv362M8VOLRvOnwGrRERGbCVlpQOGfMzF3VNvsVCI2QV9EZqB0d4liQanFrylbFeY7SScNZ3zEf65-M1uiyy1qAdQb7nShZAV7_t2Ld8uYNzg7ND5cEZTMW7RZuDIQHl88h-x2-M0gTRi7EssQnx9AX7wL8oK8bue94uIeqkvCdtrbBrpV7capJD8HEif4xNz2dUGvFVWU4TcySHASRV3r0EphPdugbx6EKQ5cgmbnkKhHvtBg8LoFJUD_kYfXsVo6rmBxDDRnQHaWqPuCEZQ67tjtrb2nPwSeU8gkLoEuv7PVWRVZTv22AR_1bxay-gyjxCNt_LmFgcshxm1LBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nIhSPKcO4TEJ7evWOC0Hj637wSsrRU5wORquYA2UoibFkNlPXsJ87q9lEDlaDjnKKHdeeWWM7lOnJT15LgjFZg_kuCXQjoYZkyORaaeGaCUWIxId3g_D5eG6eTGFed0IEw_ZoDyqotH9sCYunvq7y1oGMLn0AN2SztGCeblrCQShx0y6m8irB6gup6hD2o8_EJbmzaujgeRkMrRh78WoUQ3ZejkYLCoEqkMGzM2yjRQkNe3vv5tnjOXryfWJweDwWSMSeyRxk3Kb5XawAt3JXIK7Lqihq9KsMqe4nooLdR00o3yMz7hzLkv7mK4VHBpRVOKIFT7Z4J8uPx97_OWKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XbfOkhMDqHaSS-sSkTAgk3MLDPHN_ZuVHl8lREp5H7ydT2Do90pvfRT5mEuXGBdeDzWQMpd_FJuaqmSVxQlYDuZ4n4LvtNziHyNdxFoRatAP_SbjOhPUy8guL5l-CR2NwXYlNYbU2595UBQeaklXkqTvniKxzJoF-RTHrmfYDHtW6kH8mkFvu5ydDQn52N6T4FDUGJ0QO3A0NFySeEiqVeBJnoGo-GjVHle-v49cX0GTDLjfcLjWpTEL_bNYsQyB8uBHMJ0W3Vg3OpMugYfTFF4n_CuuPb8ICc2cqVPAONnfSVUa2K33Wel_GrznZPHF2_442b_S9550uv3xPa0ggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUS5efErPhZ8WlDG_d2MKj8X-lE5iJ4eRYvYC7MIk0cxoTPyx6HQfNGTd32CscBuzsOfjCnrn_71L7E3W8jixRjQ7yDu8SmxPiqIHIbdQIBxx6a-_W8v6qnZgXjoTNqLQuWOXQZsIUAR6BfgxFEzzSQ9bwi04liC-eHUN6iun3QFnm0H9G17oxZBQ9ZkC3x2Tn-Yl8QkCIH0du4Vd8yHFNB3hC5OWc8ftaY7eQ0sWl2SeseHtz-1KHR35yPuaeTpkhG_m9iDPPgLqfgpDKpPUKQ-ucfK8AXrG-TcP-9OmqgVFmvRE6aRlm2I8sAaCMQRwwXS2pP5yuoGBSmdpiC9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZNVidUXRKINyuQzGVo0XgACQ-m0tmG5A-HUcgHC2SQAC663MH7e6WVlE1EEh876Y-Fd5cAzTlw4DyAkvSGHbkWhIttXM-c2A-F_wLEFM2dKOHZ23EK6Eu597vC7AYm_H9JSXkOEOiMDREkNiPJ30xNNz_NuSfPH4GCIpG2WBfpIZ7ZpywGUHi1iHhNEqXXyuXaXAv2upzRiKqUgsPxLjv0ypiawHlON_ux_Er5Tju1CfCsrWUVPxdk6drzDOvfRHA1E7Fab2vRuDYuXGGb0Fzx_J484bh7CDsIa_h6d9k-WsXFgUSaEpyIj-CKbPOMxfmAmBbW7AkgsZxtBTtQyK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KR1AmAibixKhXXEPSdBGrrBAtJb7Js3OsTkALkoRZrMlMTwyuff6pKtu2T5Kjar4wlcu_VeB48Bwp85dAcQiLmyCQfcg2iTivafqIf4zm-W1QMSn6-oDUMcgUd1gNrKPqQIq0--JRqPWhCVdgyPvduE9cDkyT4iD9y0yiMoy1jXJWGF6WiNTadEYYikVcgZzJBTpwyyYCLn3YhtddHS9n2jSDLsbEGzBsmySEKn6R7dBILW2qlWJYtQB0yzlyd9FEaaAzyn8bNNFpvfurGu3rgyTvncjRi5s2B2RenwVBbluEofBKf4qMSvUimDOCKSjzGWsO44Sbuh8STUSMTKYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lIN_FDxgqub9GBuRhuXb_OUqQ5riyU6z9V0lp4AMA5uWuM0gWbECWjbWg5fbBlHnV1MWIenXG8x5aFlmdLHZWZWkZYWcp6QwCbUqABwzgyv0ErK8TE7guxcco901lfXX4QjCOo4Sf0ugvLgujhzvxzKhwwxo8UppKFX484gT_KDvgCHxqLVDoDXCm_VJrXewKaLesl4YpGQwszvK-w0r93lwNy6ibGkx6_Y-nW2k1qvMERisrlTtTocArhvC5SPpJGLh-akCcgL4M7Wzkt0M5eT_MNtlGyYSwyZaT3F-1rAHCH-nopM4IehOWW10FuIXJx8ai731LORPyAPLnpevow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DBzTK0S0hkzqWY0tHm3d9CWPFpX2PciMF-YaZNS_bbZVy6aJhzODy8pQspPdt9mx2miNnVbOHvA-buNzzbCf0iSS7lOaKCjEwnkLKunYcb9EUuzE5otMDRtr3oi1WTRmpsEOZNRYasGHdaIeIAwQf27EigtMrY08tpKT51gd_VCvb1ypN_Llgu8X4csqjOzdUtS-I6tSSdQnlWohfoSXxlDhjR4m2afCRXJngFTzNMcfx4GaGcNdT7N_fD2JbQpYvmoJBeskXZCyQuPHQWoR9_VD8yThFPHibXeINHccfFN4MRBYcjydwqIrNhIkz0Nn3wyAwhp4Cp4BMjccWxhWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L3hxFSRWzp8w9IdKsetNbVRXPr5E8hB7biYdAE_0D6PqBcITcqV0fzYn6vlHG2jeKdnHbkSUIcMnzVjq2l63UA-aGKD-0J-BeyPHinjMtqWljj_vc0Qyy4zyYQ1IQhBaakGJikCaeVbPEDcJ8QwkM-pDA_iPYkmc1yoiYXoZLVIDuArLdjVfsXw4k6MWx0H7mSsx-TaOOwfm7FrMh0pY7fBtNpxxWUQMcG1KO8LF8sUhOqz90PK6uKwuZiBNmdtMvmVUSbBmnKJ7ENWtDceg7Dh4Rk43vKpupIVIgxCEYfpUeqEIXBABk7zMLrsBE49XL4vMn4c7FU5ewGbQCSlV1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TQ7IiLFD9FUrFV7S24wayOVQ9Q2G3CgI3_DRi6lBg2tHly7l0Uo2Z66vBb0OhyI-D0srCmXm-nhwSnAD2QLroFsHBqlkoV5FKUWs8dwDdRS238UeRwZPzHBh29U0MnpPQwDrzOt1_SyxTEMscjCbvNM1dXSZ7g5P35l9E0n7dzd4ajetkHShlMyG57CpamLmQdz_50sFGxCXLzIoGNzXv4ZjnRi8ppWOIBdh4gTkIvCWWByAhCyfrpmvVM0F5jXINFAznxTDLLOTkWiU96L0xqNQ33_tdW7Uh1VUnPuWSYxsQ6iKzgNN8N4W2ExzVBoLwHgRLT2U_YNtmAjKtW2hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tZMaXkLzGSelhFExrwYxxLNFo2bAz2iAam-YPJO-yGpXQLGLCQqyZmSR5xh77KMeqz9TgneV8MEENFFSM7r-7ieKxbDQ0pi0s-UHytE8mp3vMO4iC7Toj-sh5VSpuIUHCjBIvdAe2hL4lX7yTO-uGnsP7VzVF1_tJK-_nr8hEpOxUJf47XdWMnEkD5eD0vxKjDuq-X8EeKMQkk52qwTuqY4A_15oT626D72i8ZOQOdFeb_1IKsXIaVaIphl7M3kVwFmcNHBuE5mU9oUhmepZxTDlI2FvM_SJo7q3vzk3RCK_hwzGjARSAGBtpGVv-HO2iZxbJyUiE8S8xJ4LoUQliA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاری که خودم کردم:
1- صد هزارتا زدم بره برای اسکن با ورژن جدید سنپای‌اسکنر. با 200 تا worker کلا 10 دقیقه طول کشید
2- برای من 4 تا آیپی پیدا کرد
3- آیپی‌ها رو با این پروژه‌:
https://t.me/MatinSenPaii/3554
بازنویسی کردم روی کانفیگ پنل BPB(هرچند خودش داره اما این شکلی راحتتره)
(صفر تا صد ساخت BPB رایگان)
4- کپی پیست به v2rayN و ادامه ماجرا
سرعت آپلودا هم اوکی شده الان راحت اندازه دانلودم میگیرم</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I8fJ5dNp7j1RxPGU5XtofbWoiQ27w1WCjZ-T3eWzoxEEf2s4Zd-Mzw7jDga8HnILBeZJ22qhZC70d6zb9HKYkKptUqkUzPqRYrvxLgFSdRMy04Tc98jTRFfZlKDR8xooOX8BHIrZjAZ047F7ovR6hOer2Cg4KDSDNk1nwrYK-pCz5R83_s3xNb-cA9H5oOl3mXOGnEHn2xKW52_3d3cGsHiLwGPU0crcRNrtGt2IlREUHJkCH1HiXrdtap9HQ6Y1gy9GVj686K-Ti4lImEP2G4DzVtxSEUOUDkKincOb1xdbkoMmsskYlLgP8VnnH-JTdGcojKZg7yp6_zyqMH6UxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S0PktGkBt2baFzWHm_C3kfpXZRKQffH-nq93uGSXZkxoVj1Jdiln3ThqFMdl0yqZKyOu6qv3DL1LTICBVc-sjpby6Ct7tvscIoUh9vjSvqJ6Fpek0QLNgbbTkSwPjyAxyfKjzgmEU-LiXpmES7eW9mSGy8gfmuxKPSCzMmW0kTRypUczdV6nelVkA0jI_5snCuh300LgPBI0L2VxHnCYShmGY6DB0XcNVs-zA_R0dstotZtxlIP0y0isyeQX6Y2YfCbxB_7qE9nAux9e_SNqepj5vTRb9RB1dZm2hARaGJkHKOggqVKrSQpBmKnvmXcrMIGOb3xcpXDjOFNbIFr7OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWrrRvhTNVd7krVm_GePSxTsQC6jtKBLvVzkTO17eyOLGlT9GZg6IJGpmPdKWSmhXWlxSX7C5ARHR_d3U9nbg0ksvALCIfgh5uvwMTBwMBlppQv5wwYn1eNKwKoPgXAuQ_0hU5bpYYPRSKb2Th58deR7qWsOc3_ieBT1lGZfRppFl4wArfw_b8z3oL0iK8Tjim5yRsdwzrmmSwb_sayWnbXd9gcmOc2TPKuUQ3Vs6Qm-U45E0LNKwPuayz7y2oK0PL6diLM24mdYYu4ujB5Ei92fuICkvF7-UCNawJfl9y6cmpqOQIjOmLZSr96hAYqXpwEgOMX44QiCNOpn7d5akA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTuYu0HsPqbK9LOCzTnEG6WDhshE0a3tpcJ-pbFY4llnWJ4B_huqtvFWBqE-rQUF7bq8k9TG73n81b84e-LkY7BKwku94bIrd6P6HeQQF0U7chGjyXWM6rhhT9cSHYwF_8iq69vNI05I7m8Abt5-Rv6EyGX-uVUxHKgiSBGOSQ_q-Pw7RDhAQdK_vToGyo-4ky-aCUztjALKzES1EQQTFpzndLOX6hoK1apVDdl1toRrGwuYdTU4UpkUoH-1zj8pq3j9zjiLHaaWoUJrp7_oNdRs9KEeVD4YuWNNILnmQqDu43Vv61ZcGSQtO-6EB0wuaPTTMagloTD8x4XzKLpI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ae_zn6zMVhYKnKR-kymEuoEnQP6__2lm6jtVeHimXlebnE-NAJTSiNu4xLRWJwrP2mGeeNUqkREjhMDRjjyoL-eEmc6ZNvbxhmbFyFj6G_mCOtauZks0ur8sE79S90w22JBRwjR-623YWqv3oB-z8cV2rrJdwp0V6bvMXyNMXCm_yKkHWZVX8uhq9Qe2BvT5A1ic7YYzPlQ6rcK_IHEJKV3fom0gpIvq1_tnzKnr1dIw7CbZgu-WNysCgsGWj_8rok_OlD10qs6DXT9oNXLh2rFZMYRfWERH_yURdkSDVCNCZT0d76NqWwtrL5LLPXMtNmWl4swJav-7l4B91NMUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjU0AIKvsjm4-CqMu3fHqjB9clDCbw2TT_Pj6Ae-OmLuQGiQXOHYwRIdVZ3YwCkLWMtcRggAPERKmMDGj4F1XtfFH-WnaVX99FS7syGbHImm5bmB5zZFDCYokmPRx7RM6fv3YdWE7Yt3FqHnGbBUdrfoSxoiXDBYcDQrciQnmMm_A7LtWHVu5tKXRIktToDvsg0k5iYcUBrj6INJ0fZzFhlxibxpiSsC3zvQkfyjtfx5fLlanCl6iqSxUQgnWlHVDTlrGzfqJuHhynqGnQ6OH4tGKNv409pAmFJHQNj2tLGsMEGZhb3zQ0kC9kGzHfkU3Qnj2XLXYRZ2VqNvrOQ9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eau8-VA12Rqmh9OfbCLJvap2N9N6Zf35Tgmpo6T3taL-wGuZxWq-ETCvWyElmJBWLOYsF8g0O8PqVxgfLme94LKHssfITLWaepjjoYuY1Y4dQ9QTjkv8rQVfXUFMRu6CDsm6ih1KMZiwnl0TnlJrtfoziqOwHJCh3e1TQwDTJZsG_u9Tv3GCmzxqtJyaPgrl6RJLh5RX5lo3gIWqnkjONg5BzuYYfTTtlVU1hkO2DbPTY_WQu_i_yYW1r9poRP5cQRJ-QPC2WNCSKBpSXk9sazd7R1wISItp4l1b96M3oyMH-cVBnaVfplkyZ6Ek229URQsqyxZoshsKit69HNl9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای نسخه‌ها:
🪟
ویندوز (Windows)
senpaiscanner-windows-amd64.exe
مناسب برای:
سیستم‌های ویندوزی ۶۴ بیتی (بیشتر لپ‌تاپ‌ها و کامپیوترهای امروزی با پردازنده‌های Intel یا AMD).
senpaiscanner-windows-336.exe
(یا همان
windows-386.exe
)
مناسب برای:
سیستم‌های ویندوزی قدیمی ۳۲ بیتی.
🍏
مک‌بوک / اپل (macOS / Darwin)
senpaiscanner-darwin-arm64
مناسب برای:
مک‌بوک‌ها و آی‌مک‌های جدید با تراشه‌های اختصاصی اپل (
M1, M2, M3
و جدیدتر).
senpaiscanner-darwin-amd64
مناسب برای:
مک‌بوک‌ها و کامپیوترهای قدیمی‌تر اپل که پردازنده
Intel
دارند.
🐧
لینوکس (Linux)
senpaiscanner-linux-amd64
مناسب برای:
توزیع‌های لینوکس ۶۴ بیتی روی کامپیوترها و سرورهای استاندارد (Intel/AMD).
senpaiscanner-linux-arm64
مناسب برای:
مینی‌کامپیوترها (مثل رزبری پای ۴ و ۵)، سرورهای ابری ARM، یا لینوکس‌های نصب‌شده روی مک‌های M1/M2.
senpaiscanner-linux-386
مناسب برای:
سیستم‌ها یا سرورهای بسیار قدیمی لینوکس با ساختار ۳۲ بیتی.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YmYw4VLoMd0Qzq9WcSiG3H-sP_QR6VkTZTegxqDjeIQXKJrpZbsgR8FFrlLMcH9S2PRnd-zTfmJhJCP4pcuplE-foiFj73OpEdM1-SYF2YXhDJ99LT_U76yLOrkVYPiz-cRHapnHlek848BqqFq4VuYUYN75bqADO-cCbToB6-E_5JvHx_EXz2WGWLV5pNd_JVWezcVWQME7WCgV49gyPLm5aNJKLdjSJfYOr3-PPsUYPeIFv99KS4q-nVvlTSQIz_wwB-WRHVH9CizuPRCxFghgv_Q2JbKehZ9qUjRYMmq2Nd4x92-7jQ-4XFuU2o4fXOYozRCzxXcRyJQZn78oSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rL9b1Sx5JZLsNRY2yOqqIQrhaotLrJrT0knk-x-0r1ZOQlG-UGZtachpbH6HkbWVSYSA7qoRRO4Fwj9p6XQ8mtGmPTbqGVzXtbInSQXSgWJImlDttBER_ORhtsgmdrgHKzHQqYLy8AQyPSsGyEmQLAupaLvqe_2RWx-NNZ_JF99kuWYf75xUizh-mYqZahtsz4eD1aDEodyW3TuWoggRN3uzVmuJCg_tL5-QVY8QSnfC7WkV66YKVvShy57pl_NWsI-3cKBOv8YdCo2i4-wz63IXkoau8bcSjPcgQOlZdxpmOsi5vYksjxZAaXj7Wyv8BOt1q7klS3hN5tyVIHEcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/heZNun6dDFiVfJXaUOFoinkAFyV7gZNOTV89RwPDgjD1tHqTSHutAi4LapHMXgAFaeO9eHX4AYDu-LmkRSx3fNJy_sZhjMKxztGSSQI-4yMYYTh-AOu5jM6OsipLKoGx29wivWluN7zxWbyfVYcqWzWTUneyJkPICLZEN8Sw7eNvtsLFrNvosY3WMfy3ObfKWy0eKh4YcjclNVa9hFXJ-boGiT-4P_u-CnZN7BKeE1tcGfaeFBu-HKdQ-nxdbgeono5LQDxMJQoJf-33BNNYbg8XCU_ASeqQkX3kbcL_HkWGHmDh0iXDDWgSdjeYDlGSbHxsOIIEm7A78rp989D-mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZROjPJlnMtcccWu2iChLKg2vSEih9603_eqsIUsqix84RZ2pWqK-WljvcUTt6P4gRACUbZMJ0o-HxxnRfsqP7JKmoStBVg2rsmAWMeEH3F20r1i40U2Pcz_CCV9ifSQ8cPG3Ri9qQYebtnMFSQExwRHthdIG9DQpeGOpeX6BYzmPfaPR3KusmugwKaoVQ-Oqf9YVkByUJgqdT5i80p4DqeIaaWmNjExZG5xS-2tE7Xte45CpTv5iymxM9RD1REYbY0QdbaipePGUFt9Q1ftGKGgFYvWXZhF9sjurI1cCjKrM8pvR-ICN25i0YJJ8zVdHRfq4aQ6OBBLbcRoV6pfpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jzq-NQ8mKu-o7MKmx2NyzciC-_pVFvDNK5iEwltRTNKZ_8VWec0EqqGei-Q0IyBj7F6egRHQXiORj8N4m4EPPxL1GoviaDjg0aYjYCfoYnBSnDc3yZ9cmH-cmJR7fdntLIXWULljXgIEm1y-vmsG9E6WU6I0e40ZwhO6OHFdfF-qa-dGN_IqxCCZJPj_btIlIAXHTWfUE0_liXHk4hAUh-H9zWBBjYgtiidjh6aNSNIceAWn9UJI0LjQ_lEjGEZnDPLlUpvGnVi-GVSQm0E4DaUMaOQ8Bw703OsF7nxXWC85CKwNIclqFiCZ1YJP49dWXhD4v3Q2T_MSFyuKb30CPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آیپی تمیز مخابرات
69.84.182.49</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3520" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3515" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3515" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a5dUlclCX0CNrG9IO0cLUGPn88k27U3LnBszMwY6VVZvbSQZeQ13jhrsKM-O4prlV3liFwByGcwlt4u97LXfTTvW0vi9H7UdXxVbZ4hgcvYUXMLsal3rKql5nldmm0cxP64CsOxYCvOZN8qGMfyagTKUHRULTiFMCTxPP2Xg-vRlWSTEJgWfjruppcLX9pJyMo6qX6wgnXsSV491em50FlY53Um9_ZY0Xvco7hqlL_ccTJ8Dq6ieUJgxbjujGwv943q1ZoVAM6NOd9J7gaRMErHiUZzwcZlf9v_QjRwuhQvAF-_TGn5cDpgOg3jiypwtAHXr1u6PUXheYHEN-CB1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hPsAc3pNYHme2P7ae5973XeAuAOpF_yL7ORbPJetQI9VBddsqPdE5bfDYBpJghOvShyu-bQjR9yG5BbvPJNizsWUDJKwwjRW79wOe1BIHzpTBs_41uN4CB9UYOCBF6v9sWBsZKHf4aWQBvviWgRgHWx0XdMWXn-3rplzoSl8spLw_D823EcxuxUQx10TpY6uTqx5MbPaMsgPb6MRf3GiD_X2kT2hJyxLFLEP4daeqNiZ5sOwzZScjPH5IWhV-5hk3xiJ-ztdsQHIt_CxUCU7-zlb27dHstYdpsegSj5uzaY39NrECq5oPecQ5x5p_UQkXcy6CPQnZqGomrtQuzpYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aO94P1mEmKqZ_8_XDa5pWm4cPXrX31vAQTJoT-D3zYsbXSwWxuxyH9s_vVG46njiw-biJoQJ9jCVnAq-WOnZlFF_8HdAbZ5p42SscDYUhrsSt0bq2rPOTWp2BVNCuVHgXNJBspJuHmCv7QIQca-LwCluU3BsrQ7ysEVbDgVeh4OQZD2jWZwIHHKwbx7UTvA71PfG4mh6uxuYJ9i7ZFPnaE6uvNiG_DG4cXCaQJ2joPGlHYyZx8JYZkFSbgMvJo8YRSDXGENa714mSUpaTD9_z8zNK3HvUfwUKbpHXm-JgkEWEkIVdDayDy8MgULy8lNv58BvSiM3ttllNR1H3W4Rpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H1rqeqX_fPFMiW_cns8bYJ9JUQONJvgwjGGeGCGmJEaSM92As_Fszd6b1vVnZdOec4uvAeyZlucieGMmrqbNbROyerXlRt5fnxxs6N30LNP5nGAE9CdlmRmqyZ1A1X_jb-wVcEsdQrEg8Ib--K2cJagS7fiA079nR7j8HKvpYS7Beo4rtOSTnnUbW7Hg-l4eJSKmNnDHxYP_slOHHWriV9AqTWeBgiq3ZhVmZ-EhZG7OfGPPYpztll2iHzgjZaOu2U2fspw_QMaySEWB7RfzdRlLrBpG3aLe_rDZsnkf9DA4jRzjqvcnOeJPlerBYmmfBlCqwT2y7TbcpPHS1KBJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OXvVxG55JZGeXsJ7eeAn_fFOWVBEh4ELemxWvysZ4diJ0AdNqG0Dc2gaA5UnoEOdaf0vZTuoBudLFL3OXKaYDlaueBucbwrnpdgCAjYmfZH508yWPnnLbLnU4hKSsuvDIcP4NjtvPkV-o5CsCV2l83TUnoU4DPAQnaSiDrKY2OiXwCNO5kML1eVyRr7Ys4Kj1JJqBJWEXWIQyDFiQ5sPtGC929hRM8RrbWXdX2TzXoLSfGSQmySYF2A85SGcMi_SPZg0Apis_3WWrjFAPPvI3R2Xuvm2KJ_kx84nRZARrkQwYcGQticmR-OfLRo0ZCT1b1CYBXkpgZxC2zOuBLoDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JH1a69jms-p8QVOI0wKMwP9fqlKmEgScjd-4qLFUt1SM_IoRQ2usUCWZnrC3mFqfxb-vd-c4jqhYdajVpDANRuQf_dZxuDwdK0_06NzCgEDbEnPx2DrIHCq_1Jbr4YqRp_CAsZA_WyOPL_7les-hqBc7CQ9FoI3V8KEeZsl7D6UJ0Sq1ZUvSFTvIJN_nSw8RXkneu4xUbogMz4E9anicH_TXdVvBoz7DzwcjhBM1ZWyQzEK1Hgqo0Sn2IYR-FtVB0hB-8cBnmS-EloCl04l1eqcaBhJESAlF2l5-oHJd_ApMpZsr2k8ZN--I14zVU3kYovxZPgEf6kuelcm_bmfjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qIxBX4Yw1oiFznPEhd6s2N9qfSFKu5lj25bBdSkJDj6R5WxadRyESA8pLw2R8XFj0SwpeFa-N0QhO-bH85dSuDzvgFPtLuCB7LKFfbBUv-hUIa63OoFJ6ThDlyzqOMRspl29enucg-aC_fJz6kWiZpaARpeEfMshHPpbyqMtBegtuNUa-S3OFxN0trV4HukRT3LGcio48d4zZrx7WA5UqOKdncQLQXKqxHamN9yYQcSsz2kwhz1sy_2-5bTmvJeLLoZLkGdfOVScMjPFUJiOKhx1-a5gHSZzFSZbPJVBNJzPR-bMs3P6TPGSPt9kEJTbv8_wBUeOItKSGAv2rIuNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bNuJlG71S8KAn0gVfg5ndspfZC_DbTtqcUA05ykURqZyfCZb71T5vMrJOir2Q9vrY0thgS3nkr_SMT3H0F85rk0x5No13tLzUna_VKJCnLU5MdBLSculWFx4vikFmNI19p1Of9U2cVDMGuM_KosUwEu1bXopVK2vj1bvo_FIfpg5YMBTk6X7Xm-7T-pLpVd7jkR376SUHxxQDEdJ6qMF35ZOUSHHyRNtq0DJPBTiAll0lj1uE77BM7gcWDB8Q6hVGNkyhRvGRvWATTEraRSFPS_Ui592tw6NtWpTUMI2I0HcLI1SuFOV2xW_0Abqu-uphx7SDEUKBpxX-efo8s8awQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o5UHluKS3Ywb9DwCQnUyJeg6LY7MuBfFkvPReIx7jaMAqwIXrQ_OwULcYnmYOTko2PspXtg1QeRz8c2mlu-HwIPDazRN3GY2bYvmx0q2VAycwGP5OOczrig3h4WNhkpTjdyBRAhdYQalMaGrv0P6lQ-d3hslTWvwqFcMOW65bnJx7rjMwgVov-15JA0l-zvbC7tEJQeJHDpclTbbTJN97jlVB-5AI_ME_bBi7TjhvcK9DZLhIGvm3vLyJR8MEHNXq3EAOHfZdikUaezAWwG1RYxw4ebfjsU89wEAKWii5wLOu5M8r9R_H_Us1HPyhBMixQ4Cz4kwGXzGe8O_XymsSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش قدم به قدم اتصال به کانفیگ های بات
نکته
از آپدیت آخر  V2rayNG استفاده کنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3506" target="_blank">📅 15:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCgAnbdHyXh2O--3IFsmW5hetnFibQwLggWIMbo0rmrqdF69P4PTWOGs2QQf1dvGHb83B7ypiLskWGLitw1J1TlhROK5Vn6WtkfwRAGmTcKnhtQ7CCun2SXuZvqQE_eJaLoPlYFoy-ztBOfJHCZ16bk9_MQxpBokCAyRCJD1MpmEkJ--OlLUA-Dg6F2k9hh-Pn9gKGS9F_ErBT6WZBkI1xd93s6gqAoLrUa21rV9j4JIiO8B0a6vkzWNaLSfNX_zO6qcYzUsS5qR0gbZKtx3IL3xu81hnBXAF5Tz2slCT9rrxSZ0PDaWi0f3cfrAyBMrULCIZ-VHIY9nlNMlt-LEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3505" target="_blank">📅 15:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان ربات تحت بار و فشار زیادیه. کمی صبر کنید پدرام داره روش کار می‌کنه یه کم دیگه مجدد واستون قرار میدم</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3504" target="_blank">📅 14:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yii2QEnmEl8TVFy-n5g-zS7Ulkh9Phs3dOsz8mvfiEdlnd1FGEmYRr0MibKmsGmYaZSPZ8DZwYDAqihlOhryMAB8MrIcLF-_RcqvSxxAZRLzynw4taefM_MU7yFVPZNYXeUaqyFyLfdIuSpaV1MDrvf2kJVMdbuifwzYEO9c2yb6mA8JesB6bmWvSE0uTmvkPAu8PXXY65FjaJJiuSlfSaXGhxD5lpUEQsg3VfsJWhYlj66yC3mUfYNLi__dnqGDZmCDBwSO9CWght-pcVq5VrDDiqi6jQ8XDTc0_a96-nJB-MjXHRZTXkRZyErKWdmoDE4jYRGlO19qZnjTKqudIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شما رو نمیدونم ولی این اینترنتی که الان دسترسی دارم بهش، هرچی هست بجز اینترنت.
در آستانه‌ی ۳ ماه قطعی، اختلال و نابودیِ کار و زندگی مردم، اینترنتی را «برگرداندند» که طبق مصوبه خودشان باید به وضعیت قبل از ۱۸ دی برمی‌گشت؛ یعنی دقیقاً همان دوره‌ای که فیلترینگِ گسترده، مسدودسازی IP و دامنه‌ها و قطع دسترسی به پروتکل‌هایی مثل IPv6 ،UDP و QUIC در شدیدترین حالت ممکن بود.
دنیا در این ۳ ماه جلو رفت، اما شما ما را ۶ ماه نسبت به جهان عقب‌تر بردید.
۳ ماه از عمر، جان، سرمایه، فرصت و اعتماد مردم گرفته شد؛ بدون حتی یک عذرخواهی. و حالا همان اینترنت ناقص، محدود و ازکارافتاده را دوباره تحویل داده‌اید و اسمش را «بازگشایی» گذاشته‌اید.
اینترنت واقعی یعنی دسترسی آزاد و پایدار به تمام پروتکل‌ها؛ نه نسخه‌ای دستکاری‌شده که فقط اسم اینترنت را یدک می‌کشد.
روی «طرح تبعیض آمیز اینترنت طبقاتی پرو» همه این پروتکل‌ها در دسترس بود؛ یعنی وقتی پول بیشتری می‌گرفتید، ناگهان همه‌چیز ممکن می‌شد. سؤال ساده است:
مگر امروز مردم پول اینترنت نمی‌دهند؟
دسترسی کامل به اینترنت، لطف و منت نیست؛ حداقلِ وظیفه‌ شماست.
هرکسی این توییت را می‌بیند اگر اینترنت واقعی می‌خواهد، باید فریاد کند که این وضعیت عادی‌سازی نشود. مسئول مستقیم این وضعیت، شخص مسعود پزشکیان و ستار هاشمی هستند و باید بابت این سطح از سرکوب دیجیتال و اینترنت ناقص مورد سؤال و بازخواست قرار بگیرند.
خبرنگارها، رسانه‌ها و فعالان حوزه فناوری هم باید بپرسند:
این چه اینترنتی است که به مردم تحویل داده‌اید؟
✍️
iSegar0 || سگارو</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/MatinSenPaii/3502" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3501">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">همه میگن سایفون افسانه‌ست و مال پیرمرداست و هیچوقت کانکت نشده و...
برای من WindScribe این شکلیه. حتی قبل از دی ماه هم یه بار واسم کانکت نشد
😂</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3501" target="_blank">📅 12:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3500">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خنده دار ترین اتفاق امروز این بود که دیدم کلی کانال که تا سه روز پیش گیگی ۳۰۰-۴۰۰ میفروختن، شروع کردن کانفیگ رایگان بذارن
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/MatinSenPaii/3500" target="_blank">📅 11:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3499">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
apple.com : 17.253.144.10</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/MatinSenPaii/3499" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3498">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni: certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/MatinSenPaii/3498" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3497">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6YREkLhuDemZ-6OaEpKbVNE6ciqf-aw2Ef6NnBKKvV1QnkdQrfMvAFJWCLhTmWB4AY13i55gjwRlCxk42fvIY7URujdrTnz73Ep0PD2iQwYzTxgAzO7muWHB2kJY0SSuCKe23geR5Y4mh4qf0adZkfhU95kbf9C4XFT6KBrzarJsd8IkNOyLQox7rPmzKQnR1rybq4W5el9b83sV19GXuhsQtQ2QhzQoujVC0FXYXL681OTGgtOXCEieEeTLLSZKEbJM3AFk_ZnazB9QpRpOZSfp6K7Cyc9UKuLWwzEnaKx7Pya87o6x4ladyYN_zfCCvtaEtOEP1bR8W8-t3zAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
invizible pro
🍷
با این روش و sni های زیر میتونید توی برخی اپراتور ها متصل شید رفقا
✅
sni:
certum.pl, neshan.org, subkade.ir, gifpey.info, shaadbin.ir, uupload.ir, letsencrypt.org, gerdoo.me, nairobi.saymyname.website, actualities.google.com, myf2mi.top, chatgpt.com, bazion.ir, 8.6.112.0.sslip.io, abadis.ir, ikac.ir, ebooksworld.ir, iranicard.ir, gameq.ir, melovaz.ir, sourceforge.net, google.com, scholar.google.com, libra-books.com, uploadboy.com, soft98.ir, daneshpaz.top, berlin.saymyname.website, epicgames.com, uploadina.com, sarzamindownload.com, asiatech.ir, shecan.ir, par30games.net, 3fa.ir, taaghche.com, downloadly.ir, oldtowns.top, cafebazaar.ir, Shaparak.ir, uploadkon.ir, news.google.com, varzesh3.com, hooshang.ai, downloadha.comfilimo.com, gitlab.com, search.bertina.ir, mail.google.com, chat.boofai.com, support.google.com, search.google.com, vercel.com, farsroid.com, bosgame.ir, 2.188.21.46.sslip.io, divar.ir, okta.com, snap.ir, nic.ir, flzios.ir, digikala.com, fastdic.com, cdnjs.com, 162.159.152.4.sslip.io, hooshyar.golrang.ai, openai.com, aparat.com, download.ir, yasdl.com, pastehub.ir, downloadha.com, iranmatlab.ir, bitpin.ir, Python.org, my.files.ir, post.ir, picofile.com, namnak.com, gov.ir, dl2.sermoviedown.pwmyf2mi.top, nixfile.com, pirategames.ir, balad.ir, supermario.corp.google.com, faraazin.ir, vgdl.ir, aharvesal.ir, chat.smartbytes.ir, cdn77.com, behmelody.in, cup.theazizi.ir, alibaba.ir, zarebin.ir, patoghu.com, subzone.ir, navaar.ir, zoomit.ir, rio.ggusers.com, linklick.ir, gold-team.org, dlfox.com, centos.org, fidibo.com, tamin.ir, guardnet.ir, atlassian.com, 2059.ir, site.google.com, sheets.google.com, react.dev, irimo.ir, m.ulni.ir, 2.188.21.130.sslip.io, f2me.top, myket.ir, dls2.iran-gamecenter-host.com, Telewebion.com, airport.ir, ubuntu.com, email.google.com, radio.9craft.ir, torob.com, vercel.app, rubika.ir, dic.b-amooz.com, mizanonline.ir, 87.107.110.155.sslip.io, chess.com, gapgpt.app, ninisite.com
لینک دانلود اپ
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3497" target="_blank">📅 10:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3496">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شاتل و همراه اول هم شروع کردن به رفع فیلترینگ بالاخره(لااقل منطقه‌ی ما)
الان با شاتل با کانفیگای رایگان هیدیفای پیام میدم</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3496" target="_blank">📅 10:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">این ساب تیم مهسا داخل هایدیفای هم رو بیشتر نتا اوکیه پینگ بگیرید یسری سرعت بهتریم دارن
https://raw.githubusercontent.com/hiddify/hiddify-app/refs/heads/main/test.configs/mahsa
داخل خود هایدیفای هم + بزنید داخل نسخه جدید گزینه free روشن کنید هستش</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3495" target="_blank">📅 09:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3494">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اینها هنوز کار می‌کنن دوستان. برای من اوکین</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/3494" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3493" target="_blank">📅 09:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3492">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHTXTj1GwNHH4ocqiYlz8w3z-M81vujoAwLXRB0UOMX_G2mcxV2qZcmDYYguNDkECfddiLA7susSrfIg_S0ISmx4j8pl_PHlq_fjlMqR5M9CYm8DjhyrvrpWs-M5RUVQQ6hpUOeN-PVMDtl3t6fskgSIPFMoNuDWNLwmKcLrFFz4zwPUe2928_6AZXfeqWy0rAgZJ2BpC4C8ko9eyzAAqOBo0rWfJ1HIw-0VSXYIOdtr0uQqz9Yp7mUzEAKF3h0pWJk5QLLxhUUur3byoyZe8Gl05jhMfXGZwlY9BvuO9w1XzPyKsc9FM5k2rd3aU93CqDvtl85pkLGLjy3h1h3dwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت اینجا توضیح داده شده:
https://t.me/MatinSenPaii/3467
اگر یادتون باشه دی ماه هم همین بودش. یک هفته‌ای طول کشید تا همه چیز یه کم نرمال‌تر بشه(هیچوقت به قبل از دی بر نگشت) و الآن هم متاسفانه احتمالا همون روند هستش</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/MatinSenPaii/3492" target="_blank">📅 02:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3491">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مورد داشتیم از چنل WhiteDNS و بقیه‌ی کانال‌ها، سرور اسلیپ‌نت برمیداشت می‌دزدید می‌ذاشت کانالش از ملت پول دونیت هم میگرفت. یک شارلاتان‌هایی لو رفتن سر این ربات که فقط خدا می‌دونه
دوران عجیبی بود خلاصه</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/MatinSenPaii/3491" target="_blank">📅 01:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3490">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">1- هرکسی میتونه با دی‌کامپایل کردن کدهای اپ npv منطق هش پسوورد و... اش رو در بیاره و فیلترچی خیلی وقته که این ابزار رو در اختیار داره. 2- آیپی پشت کانفیگ‌ها رو به راحتی میشه با وایرشارک فهمید نیازی به این جنگولک بازیا هم نیست. 3- آیپی‌های کلودفلر ای که باز…</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/MatinSenPaii/3490" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3489">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">با این ربات می‌تونید قفل کانفیگای NPVT رو بشکونین و لینک Vless معمولی دریافت کنید. حتی اگر رمز داشته باشه:
@DickiriptorBot</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/MatinSenPaii/3489" target="_blank">📅 01:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3488">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">طرف با کانال دو میلیونی برداشته کانفیگ worker گذاشته توی npv و اکسپورت گرفته گذاشته چنلش نوشته کانفیگ موشکی وصل:/</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/MatinSenPaii/3488" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3487">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فایل Json جدید برای Spoof: {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "172.67.139.236",   "CONNECT_PORT": 443,   "FAKE_SNI": "security.vercel.com" } برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/MatinSenPaii/3487" target="_blank">📅 01:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hiddify-Android-arm64.apk</div>
  <div class="tg-doc-extra">113.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3483" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/MatinSenPaii/3483" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=fmi5te4YkqJSpD9k2e1JyXbocUbuM1ESW-pqcwvMT2ABYZ8npEoDTl0ctqSdRVSFPR3qeX6MNcLakPeIQUH5JGZzhmgVMzRXJfMAqsrezGTPn9-bz1nk9lOPGwrXJa9-szLvPgNiTlCZ4Av37qiS9KA2TeM8FTdG5DG_0WaSL4v-5UK7YuCV1knC9QnxIEcVq98B9QBjvbSLsAE-_OuiZPvhkTCGWiIvy94CmBNRRSZ9JOcGCL3WD5M5BH68mlkNrwZn3-G42JIsvUKev6YpebkVoxjFqGAnsG0D6dBAMpbsrOIiRrxQbj1nZpkuG6KZPF0SNwNBKyKxktDgoSkXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ebb21ad73.mp4?token=fmi5te4YkqJSpD9k2e1JyXbocUbuM1ESW-pqcwvMT2ABYZ8npEoDTl0ctqSdRVSFPR3qeX6MNcLakPeIQUH5JGZzhmgVMzRXJfMAqsrezGTPn9-bz1nk9lOPGwrXJa9-szLvPgNiTlCZ4Av37qiS9KA2TeM8FTdG5DG_0WaSL4v-5UK7YuCV1knC9QnxIEcVq98B9QBjvbSLsAE-_OuiZPvhkTCGWiIvy94CmBNRRSZ9JOcGCL3WD5M5BH68mlkNrwZn3-G42JIsvUKev6YpebkVoxjFqGAnsG0D6dBAMpbsrOIiRrxQbj1nZpkuG6KZPF0SNwNBKyKxktDgoSkXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با اپلیکیشن Hiddify (اندروید، ios، ویندوز، مک و لینوکس)
در صورتی که کانفیگ‌های CDN روی اینترنتتون کمی نفس بکشه می‌تونید به رایگان با کانفیگ‌های مجانی هیدیفای وصل بشید. چون مدام عوض میکنه کانفیگ رو، به شخصه تجربه‌ی بهتری از خود MahsaNG تجربه میکنید
لینک ریپو برای دانلود:
https://github.com/hiddify/hiddify-app/releases
فایل‌های اندروید و ویندوز:
https://t.me/MatinSenPaii/3483
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/MatinSenPaii/3482" target="_blank">📅 23:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رفقا، Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w?si=yd2q8LmmyvZ_VfsQ
و Paqet تانل:
https://youtu.be/nwpLOANv7VY?si=OMOXPs7XTV9uqk_M
رو چک کنید که آموزش داده بودم قبلا. رسپینا شنیدم تانل تونستن بزنن بچه‌ها، اما مستقیم هم شنیدم چندین اپراتور. به توضیحات ویدئو دقت کنید Paqet مستقیم با اینترنت سیمکارت(CGNAT) امکان‌پذیر نیست</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3481" target="_blank">📅 21:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">متد SNI همچنان فعاله دوستان. کانفیگ‌هایی هم که گذاشته بودم(
https://t.me/MatinSenPaii/3183
) همچنان کار میکنه ۱۵-۲۰ تاش</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/MatinSenPaii/3480" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/MatinSenPaii/3479" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xh90kiW_UJ8tBot04cgRjZOqi7zVHMnALsPvWescrPE1-zY97n-eI8vlAmvZRcHSm_WUNByHAMwA_x2XTzyoWIaBeWgoK4ZxelsHpAk5cea1gi-btsSClT2WYFaUl2crwm_DvQ5bhxJCu-OIwGJpoTl4tAA-oEucIhadQTXOrnxOs4svqLSpLe68iTmegE1FJ_TprlxX8y56iK95KGM-BcjXWw7d-M4b_5yJejCVpSxKk4i3bYoXiZ9OdzSWDCJf0zJcK7h4Sq5bpusNYR86HmWHH2r-QTSIcAH72MxFolYQ4RnAQRcK1NPNKfr9CVdf-ZINGIZx8NMsN5uFLCp1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت اینترنتی که واسه مردم وصل کردن
خط قرمزا اختلاله !!!!
✍️
SamAlpha_</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/MatinSenPaii/3478" target="_blank">📅 18:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BpJkmm1AiLkJiszu947OttZUw33KYgWLDcZD76iDncYVH-fssSBXO67W3MtQA--vCJcbDdnX6QfXvvVrcR1lFtSyADC33iP9id_UudvvLa8SnaCp1fF2AHEgc2EfK8-P1Oz3Q2rXBpsBCp52VJhC_uT1yAGlte8oWYWZYkZtIuIh1hv_M6_9c6qAIGvtckl2tWn-dwSZyEFTpINlhsV4PJRL5knspC2Wg0SJWenC0ukF98iwIwuiRvNEzt-YkIoRShopwngm73wCI46rsEcTOO2S1CEgujxVMjmxgoUQVyOcURCNe8XraMe1EVzzw_2zwGiL5UhrCZzfl0CMA_zzCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AvjRWubifP0ZxB55N_dtCJp8DKVpbNq8ezOdE9g6SRGp90ap_o9zIJ7kMN6C63wVfr5mfSLgjrFHLbExt1ZK1gNLeWfNt55EME5koGww3yum-1L5z-CDeueYA1_TStSKu-DGOqyLjgFp8uFNuulv5B36fBzCKeIGtahWNyC4F4m8KsRnFa3fidbEY-35hDLfRaobUVdhNc_84aqQ4OLoySQpvx2RK6NWX9X1YLpWx7LmGeWFvjIa8rYCJK7m5OX0rdGWLVuEdDcSa7uIJI1_P_iRyBr82sxI76noGdh7sZ7zg9z-NVhJJefQDzt26z9J_ufsjG8rTZY2VEd7pAvQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FJ1Xq3rv5qeZjvOlOt15H3p2FCrXcp49m998VxWvxJcojr96-BGWFZCV3mwe5EJy-hCQQU3D1LXHYXflEF-XoN6ep85wWYDDuf_EKmhjXIDMB1LfZaTJR0EY5TAq4Cx6mHZrlo0YmVMhndb-Tm2IndiBz-RyhnYxcsGzHQM2PhgU2B3n7V6gC1DOR6a-cPszoGlH8btKw_rDImhK6UCAMnxpDNnHGB2NEB3kP9_FMNTK57zPrttHDyoFbzcgCcXuuT0wMEQtgBjDUzb3lsvkiqBIM2EG18Surj2ZfZ1zuS-GAUkYsqiyt2RFgV-8LdrppntWSSr9sUZeJfOztWGSeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pOl-FIG0Y2eHG3_hqv-PSTBOdJaX1z2u6VhRVhDAUjBTR2tqFumdeiwpWPI75Botf1kIbla9ukiQ42RzSJImH4vekOmQBPZxDqYu2P8rKcpBu9CAxRGxYbhkNRBoSb0qb33dq1I0jAu8wgUKiCM-4B00RZNMqiQdEPCigbLwcKxUbGMbN5ZtHvfevA7RpMwqLJr_RnjT2rM5deXNApq04e2x0SQ4Br2VM3R3W7qTC_MN4E7nnEz1u2NIQLRxQTJOcz7PnO4PI8zfSkjAMPcrJM5vePFRkRPgwidTnifCcL_PUmkEhAGXxg3800f3U1VsXYex95IQ0Jr1LtyULd5-Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیر و خورشید برای من این شکلی شده که وصل میشه اما هیچی کانکت نمیشه</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/MatinSenPaii/3474" target="_blank">📅 17:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فایل Json جدید برای Spoof:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "172.67.139.236",
"CONNECT_PORT": 443,
"FAKE_SNI": "security.vercel.com"
}
برای من روی مخابرات اوکیه</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/MatinSenPaii/3473" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3472">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آموزش ساخت کانفیگ BPB شخصی:
https://t.me/MatinSenPaii/3443
آموزش  Sni-Spoof هم این:
https://t.me/MatinSenPaii/3186</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/MatinSenPaii/3472" target="_blank">📅 16:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3471">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NSuYAZLodHOUlALUX8NvSSxzaDNejsHL2fC44af7tcCOi6uCe_5z8l7KyJkgqiCoIpc5iHyJ4s6M0wOLmXJUvinUAicULvLdnRcMFpWgnsn88FvB5tqTW8EvmR9iBL2DDo8D6YzIci2Hb1CLdwY4mj2jl1o0opWgjZGEzSmX8YztrHRv-9AwUyLytWjC6DURqP-aC_c7ONXxkBHu--SzaScvREti_N3S56-QFbb0bbE7Me7r5ZTWumlX24vVt2N_phOMAIyKmmHL0ppRu4TdQm36ctVmsfsa74_c3acPHeGxALkQ34nV_5IbTf_sEPDEZ94Uc4Jq_YTl7PGNC5pg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/MatinSenPaii/3471" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3470">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OBForWyfunUgGNEVqxzypoAKsmzmkNB4w-d-0kTENzI-d8DHAkGT7w4zviyj81_UAZCw_VFkKtRQK5vMoj4yHc-SWKVuYAttQ3mmonsmuJYVRr4kg11CUixihbwoCfOKucbt6ImKWo9Q8UWRYaDTes_Ww57a9kBDzFrs1G7PltFuWr2_CeJIJzF12XbK5PFoY29B--oQWkar8RTe8_Vfc8lDyCLR6miF2bGgEGde1sr1nFe_GXOgefQIwDphEl5qRMBu91zlrO6vYORj-WLBdyhHFrp1uDVae4B_5ZfPRIveNXTk1sUCkQ4MovPd700eG4qvlrQMln0V0r5ISvDIjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سرعت آپلود روی CDN و Worker Cloudflare</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/MatinSenPaii/3470" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3469">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTIpA2tgJBWdYEhr8ymdO8rdwwEr7ViAEp5QTPWyP7JgoHEVq8Bsn_vMpfCHT28pjZL1Cbq5ELuMmHiABPW6t3dvmO4-L4HZ6udi9N8_54ax87ZzmTbkU0Lk8iC7CZ7SGzH7uEz8rDsAbazKPvpXZGNNLOOh8cuJLvbWCFsqEFqm2alVX6bVBPRzDDc-regRpcMVGYfNxn5SYawpntCmR_CajGwbs41Uqqs-4mWIeZW6-zqErHTbdI7SPxdP67rQg_UBoYsMr-mfKpUZ2098r3TngkY2TtWxSqjdrN0ScszdvqaRhAuSYnYoHH3OAhr6aqvrOK0-SFfvOaRzSIqshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اهداف من اینه که آموزش‌هایی بذارم طی چندوقت آینده، (هرچند قبلا هم گذاشتم) که شما رو بی‌نیاز کنه از خرید هرگونه کانفیگ. و هرشخص بتونه برای خودش و خانواده‌اش به راحتی فیلترشکن شخصی راه بندازه. منتها اگر فعلا نیاز دارید به لوکیشن و یا سرعت و... ، می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/MatinSenPaii/3469" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3468">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بزرگترین نجات‌دهنده‌ی ما، WhiteDNS و MasterDNS هستش که از واجباته برای خودتون ستاپ کنید! توی کل این 80 روز می‌شد باهاش وصل شد. آموزشش رو هم ضبط کردم طولانیه اما حوصله کنید و ببینید:
youtu.be/6Pm7kNQb3mo
‎</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/MatinSenPaii/3468" target="_blank">📅 10:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3467">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💭
چرا زمانی که اینترنت را قطع می‌کنند، درجا این کار را انجام می‌دهند اما وقتی نوبت به باز کردن می‌رسند، انقدر قطره‌چکانی این کار انجام می‌شود؟
1-
جنبه فنی
(دلیل اصلی تفاوت سرعت قطع و وصل):
🌐
ایران اینترنت را از طریق چند gateway بین‌المللی محدود (عمدتاً تحت کنترل شرکت ارتباطات زیرساخت - TCI و ASهای اصلی مثل AS49666) به جهان متصل می‌کند. این ساختار متمرکز است:
"قطع کردن آسان است"!
کافی است BGP announcements (اعلام مسیرهای روتینگ) را withdraw کنند، یا ترافیک را در gatewayها بلاک کنند، یا IPv6/IPv4 را محدود کنند.
با دستور مرکزی، همه‌ی ISPها (مخابرات، ایرانسل و ...) در چند دقیقه یا چند ساعت، آفلاین می‌شوند. مثل کلید kill switch.
وصل کردن سخت و زمان‌بر است:
وقتی همه چیز را قطع می‌کنند، فیلترینگ، routing tables، DNSها، و سیستم‌های DPI (Deep Packet Inspection) و SNI filtering در لایه‌های مختلف (gateway، ISPها، IXP) به هم می‌ریزد.
برای برگرداندن، باید تدریجی تست کنند:
اول routing را باز کنند، سپس DNS resolution را درست کنند، بعد فیلترینگ را لایه به لایه اعمال کنند تا "نشتی" (leak) اینترنت آزاد رخ ندهد.
هر تغییری ممکن است باعث باز شدن ناخواسته سایت‌ها/اپ‌ها شود، پس مرحله به مرحله روی ISPهای مختلف و مناطق تست می‌کنند. این کار ساعت‌ها تا روزها طول می‌کشد.
در قطعی(و سپس وصلی)‌های اخیر (مثل جنگ دوازده روزه یا دی‌ماه) هم دقیقاً همین الگو دیده شده.
2-
جنبه سیاسی-امنیتی
:
💬
قطع: تصمیم سریع از شورای عالی امنیت ملی یا نهادهای امنیتی گرفته می‌شود (برای کنترل اعتراضات، جلوگیری از هماهنگی یا جاسوسی سایبری و هر مزخرف دیگه‌ای).
وصل: نیاز به هماهنگی بین نهادهای مختلف (وزارت ارتباطات، سپاه/اطلاعات، شورای فضای مجازی) دارد. گاهی اختلاف میان این نهادها در بازگشایی یا نوع آن، باعث تأخیر می‌شود. آن‌ها نمی‌خواهند ناگهان همه چیز باز شود چون کنترل را از دست می‌دهند. پس "تدریجی و با احتیاط" اینترنت را باز می‌کنند تا فیلترینگ جدید را تثبیت کنند.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/MatinSenPaii/3467" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3466">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">کانفیگای توی
لینک سابسکریپشن
رو چک کنین. کار میکنن براتون احتمالا.</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/MatinSenPaii/3466" target="_blank">📅 01:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3465">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/MatinSenPaii/3465" target="_blank">📅 23:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3464">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">حقی که نصف و نیمه بهمون داده بودن و با فیلتر رو ازمون کامل گرفتن، بعد ۸۰ روز هم پسش دادن، به همون حالت نصف و نیمه.
شرمنده اگه یک درصد هم باعث خوشحالی من نشده این وصل شدنه. هیچی تغییر نکرده.</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/MatinSenPaii/3464" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3463">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سرعت آپلود شما هم پشت worker و کلا کلودفلر پایینه بچه‌ها؟</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/MatinSenPaii/3463" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3462">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚡
cfray v1.1
یه ابزار تک‌فایلی پایتونی که همه چیز رو برای مدیریت کانفیگ‌های VLESS و V2ray پشت Cloudflare یکجا جمع کرده.</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/MatinSenPaii/3462" target="_blank">📅 21:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3461">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینترنت برگشت، و خوشحالم که توی این مدت تونستم کنارتون باشم و توی اتصالتون به اینترنت آزاد راهنماییتون کنم
❤️
همونطور که همیشه گفتم، زحمت اصلی رو برنامه‌نویس‌های عزیز کشیدن. افرادی از جمله پترنیها با sni spoof، امین محمودی با MHR و MasterDNS، aleskxyz با پروژه‌های خفنش، iampedi و تیم خوبمون با اپ WhiteDNS، سارتو با پروژه TheFeed، سم، مارک، Samim با پروژه شیر و خورشید، و همینطور بچه‌های کامیونیتی زیرزمینی Vasl، عزیزی، امیرپارسا، ریتالین، GuardNet و... که اسم‌هاشون بی‌شماره.
می‌خوام بدونید که خیلی از افراد پشت من بودن تا بتونم آموزش‌ها رو به دستتون برسونم. و اسم خیلی‌هاشون رو نمی‌تونم ببرم. از اون عزیزی که به من صد گیگ کانفیگ داد گرفته، تا بچه‌هایی که قبل از آموزش‌ها باهاشون مشورت می‌کردم تا اشتباهی نداشته باشم و همه‌چیز بی‌نقص باشه.
همینطور از افرادی که به من دونیت کردن و من تونستم کیبورد و موس بگیرم که وضعیت بدنیم بیشتر از این اذیتم نکنه، و راحتتر بتونم تایم بیشتری رو پشت سیستم باشم.
صمیمانه از همه‌تون ممنونم
❤️
ما همه بدون چشم‌داشت کار کردیم. و هیچ منتی سر شما نیست و شما هیچ چیزی به ما مدیون نیستید.
و ما کسایی هستیم که امثال سگارو، یوسف قبادی، IRCF، وحید فرید، یـ‌بـ‌خـ و... رو دیدیم و قدم برداشتیم توی این مسیر.
هفته‌هایی بود که چند روز پشت سر هم نمی‌خوابیدیم، با درد مچ دست و کمر و چشم و تونل کارپال و وضعیت جسمانی افتضاح خیلی‌هامون ادامه دادیم؛
فقط و فقط چون به آزادی باور داشتیم.
زنده باد ایران</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/MatinSenPaii/3461" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3460">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/MatinSenPaii/3460" target="_blank">📅 20:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3459">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه
مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/MatinSenPaii/3459" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستانی که همراه اول و شاتل و زیتل دارن، حالا حالاها باید بشینن تا وصل بشن</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/MatinSenPaii/3458" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin Mahmoudi</strong></div>
<div class="tg-text">نقطه قشنگ ماجرا خارج شدن این موضوعات حتی از ایران بود، این افتخارش رو هممون بدست آوردیم، هرکسی به نحوی کمک کرد.
یکی روی توسعه کمک کرد.
یکی با ساخت ویدیو کمک کرد.
یکی با توییت زدن و معرفی توی کانالش.
یکی با استار دادن.
دوستان برای پروژه ها نرم افزار اندروید ساختن و ....
همه باهم کنار هم باعث شدیم پروژه ها خفن بشن.
همه با هم کاری کردیم که پروژه مثلا MasterDnsVPN، چندین روز بهترین پروژه زبان GO توی گیت هاب باشه.
همه با هم کاری کردیم همین پروژه 2 روز توی ترند گیت هاب باشه و اینا همشون خیلی خفنه.
توی پروژه ی MasterHttpRelayVPN، هم همه باز همین کمک هارو کردن و موفقیت های خوبی بدست آوردن.
همه با هم این کار رو کردیم، کار یک نفر نیست.
این مدت جدا از بد بودن و سختی ها، همه با هم افتخاراتی رو بدست آوردیم ...
که همه با هم باید به هم خسته نباشید بگیم
❤️
درکل همگی خسته نباشید.
امیدوارم این روز ها دیگه تکرار نشه ....
همگی عشقید و خسته نباشید، دم همگی هم گرم
❤️</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/MatinSenPaii/3457" target="_blank">📅 17:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/MatinSenPaii/3456" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=Q8f-ylgC63xKSDSQJi3ugFnDfOGSLWSkWVMTQOvejjzjQd5izUXU6tNzFlTuZZEWaBdtSJ7SoeLlWzLI-qz8XOXn5bLPucRiGLWPr3MaZalN0tKiOfBbNl5u9Hokyy7devKe8cPFqPiAHnSAMChxxruluUkkewmf3Ow32InkxOnHaif931xvVFIv6oVO8N2JTvoCLdVdPu0V1cIhEDH0iU5hVn_z6tZovPGoaPKbXCY-zPaVlthpsHxTGMAbEWqmFzxNVP2Zh2GpRV0Kgdo-dHftzGKHLoJBDDdso90JGe9y_m7UjcTt0sMYyNpu0NujEaa5mnUWI24ssvPsAdNfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=Q8f-ylgC63xKSDSQJi3ugFnDfOGSLWSkWVMTQOvejjzjQd5izUXU6tNzFlTuZZEWaBdtSJ7SoeLlWzLI-qz8XOXn5bLPucRiGLWPr3MaZalN0tKiOfBbNl5u9Hokyy7devKe8cPFqPiAHnSAMChxxruluUkkewmf3Ow32InkxOnHaif931xvVFIv6oVO8N2JTvoCLdVdPu0V1cIhEDH0iU5hVn_z6tZovPGoaPKbXCY-zPaVlthpsHxTGMAbEWqmFzxNVP2Zh2GpRV0Kgdo-dHftzGKHLoJBDDdso90JGe9y_m7UjcTt0sMYyNpu0NujEaa5mnUWI24ssvPsAdNfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/MatinSenPaii/3455" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نت خونگی اوکیه
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%202</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/MatinSenPaii/3454" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قربون دستت حالا که دستور دادی اینترنت باز شه
یه دستور هم بده اونایی که کارشون رو از دست دادن برگردن سرکارشون
یه دستور بده اونایی که زندگیشون از هم پاشید برگردن سر خونه زندگیشون
یه دستور بده اونایی که سر اجاره خونه خونشون رو تخلیه کردن برگردن خونشون
اینترنت شاید برای شما یه دکمه روشن و خاموش باشه، ولی برای خیلیا نیست واینترنت زندگیشونه که با دکمه خاموش و روشن به حالت قبلی برنمی‌گرده.
✍️
Reza Jafari</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/MatinSenPaii/3453" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🍷
بازگشت همه به سوی سایفون + v2ray هست چند تا جدید که گفته بودم میزارم استفاده کنید ip جدیدا رو
✅
141.193.213.11
104.18.38.202</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/MatinSenPaii/3452" target="_blank">📅 16:27 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
