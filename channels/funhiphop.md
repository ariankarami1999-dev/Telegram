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
<img src="https://cdn4.telesco.pe/file/lNsezOxA2BHXfY6tRgOFhECqXX5ssgKeCQ-EQwdmZv1AtCTmpoEASS4_0m4s7dY8Lo-txw1bSOIgvI9oTcj0j5lFWtD9fjbGmiBzwUBsxCFzqO5mCruOQr9LKjqjU4MK7J_bvEMy49XgLGxsYhlpPY5yl_0FiEN-MR0aABDFVWR2BPr3H4qicfQrCmDiepWsPiyBtPvmNBkmvmGY_7iLZbqhCalV_tXdogu7hF5ls57LG3NxaTPy1T6hJt1soh72eys9kSU-_MfCARxdiNgQFkpZSY4e3gfUz9bDSLBUy54n-dM-upj3ea1--iESkonEEi5ax-8YsHvZGSbuHFbwjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 194K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 14:20:03</div>
<hr>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عجب امتحان بخوانیم و بنویسیم سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/80502" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لطفا فحش های جدید بکار ببرید
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/funhiphop/80501" target="_blank">📅 12:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l27XI5Fhc7BQpG85NQBVSUSSHtFfz_oZqKwMhIHsIfgvdcRtab9UmmxrLaLqD7OLAtXgSwtSBNvrptfsEcVFwD0Z5aGso3g5mQNg0K-MiA5VBVyroqdW6AXCHdS_TZw6jn3ok9Y2dDbWBXHJ1Mcvpy56HCEyj3cSJ709agwFAmBP18yjcWY-IPH1c9pprIstPM1IVw-xwmMsUPAbbEvB5krEWnxYqwkOlaoqvWo8zI9xnokw5NSUP3AoLq-mhmdyr-QcPfVR-Aw1H-hMOjLf7zF7oLePD5rRXaQvGtw_RdSf_AjoQ2ocHVTosUc69CrLZLZbV6XT3Fso28vixPJkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم پول ویناکو ندی بدبختت میکنه خوددانی</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/80500" target="_blank">📅 12:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEwkdeA_yMRkLkVAFFA0fhh2clboeJriasJp4_1nX-cHHczHWu1pVr7wTu2BW83p18NQ-weMbSTFvb1giJe6KkWvpCCf5mDdIEO4g9JY1w4HGwMPVt9jeuQTtv8Uq6fszpKqZTfdaW4vqXpicOKBBDgOyEnz1ZaOtPeQlYxph8vJxK8cFJ6uEwO9bH2o23A4Av32BJCp2icgPPj0ZhUYp0GQbIjD6THIuwyB6wqtm-BclqV5UryOPGyCtNLLbtRb0yCy0pi_L2lNn7sTFECMrE7Rhp_TuJy04JJfKhyElYrTV3-bHtEDgc99A_nLDPmsrjeGXC9N9vEIuZm-1Kq3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ۲۰ درصدی انفجار
💣
⏩
در روزهای دوشنبه تا جمعه، با حداقل ۱۰ میلیون ریال شارژ حساب کاربری در طول روز و ثبت حداقل ۵ میلیون ریال پیش‌بینی ناموفق در بازی انفجار بت فوروارد، در هر روز ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق خود را تا سقف ۱۰۰ میلیون ریال به عنوان بونوس هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BL100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r25
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/80499" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=BZxv5mvW1dmG8QBTxR96CwMt9V0FkRHWs4oA7tc-QGsbA0pT5x1Ef-pb0_LtbCb22OUwit5j6mUL-E9jz0ZttSirD9xdwc0ukf6JNLiMOyjrQigriuZYcEO6uBth4Z9TwtmqOFr1vMcUWWXCeOX1WpE1nVhQODuIFMEFOAWpktaLNq_BKyKRYruVPMtTQpVqYPVAYivYt_GC79WY-2Ypo9LW7DV8dmLhDP4nAlwvlF7F7Nj4JAHdWxp0zljUljoVuZJMd1ipbWH0UX7dcvfFiZ6Rpy4heLphft6vhMBrO-V94lZJSHyOJw75QB1Jl1CxjDGTN1KlfXXE4SEMh-tHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fceed0ed.mp4?token=BZxv5mvW1dmG8QBTxR96CwMt9V0FkRHWs4oA7tc-QGsbA0pT5x1Ef-pb0_LtbCb22OUwit5j6mUL-E9jz0ZttSirD9xdwc0ukf6JNLiMOyjrQigriuZYcEO6uBth4Z9TwtmqOFr1vMcUWWXCeOX1WpE1nVhQODuIFMEFOAWpktaLNq_BKyKRYruVPMtTQpVqYPVAYivYt_GC79WY-2Ypo9LW7DV8dmLhDP4nAlwvlF7F7Nj4JAHdWxp0zljUljoVuZJMd1ipbWH0UX7dcvfFiZ6Rpy4heLphft6vhMBrO-V94lZJSHyOJw75QB1Jl1CxjDGTN1KlfXXE4SEMh-tHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتکشم زدن تازه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/80496" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfpuU0DW8frTTSo4Lr6Bn-Y-2Qsq1baRKn0sNw9vcLIjN6jR6whsLbHN9dkXEQFqyL9X-2dWAS2NkC705xzLa_rcK0Vg9etPT5Kd2AOroTUVDsTQTxe30-g1KjOgFOFkzg0kROefjpE5KMrC1l47vtqG6pm7yIB42ACCICbuYlwUcQPF8bLZapA4JMlAQcUh07YivOAH-2vn7pBZS5G6Ucm7Ov_mK6iIMbjqcL8k0umQIBWT296ukFQt2c7UsKA4Q_m2bqAhmG6jw7jobNXR2A-0oXTC6Bj_DsbAJOqWv_HPtpJuW7O7bRpwHXIJSj_U903WBDaT8siTY9zQ-JEXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بخدا بلینگام بدبخت داشت خطایی که انزو روش انجام داده رو تعریف میکرد، گاییدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/80495" target="_blank">📅 09:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فکر کن خاورمیانه چقدر پیشرفت کرده که دیگه تا خودت صدای انفجار رو نشنوی حال نمیده و هنوز جنگ حساب نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80494" target="_blank">📅 04:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کسی تو سمنان زندگی نمیکنه خبر بده، چجوری متوجه انفجارای اونجا شدید
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80493" target="_blank">📅 04:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80492" target="_blank">📅 04:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس مرکز اطلاع رسانی و روابط عمومی وزارت آموزش و پرورش(صادقی): اگر خدایی نکرده شرایط جنگی در استان های دیگر امشب تداوم داشته باشد ؛ جلسه ای شبانه برگزار خواهیم کرد و تصمیمات جدیدی در مورد تعویق امتحانات نهایی در سایر استان ها خواهیم گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80491" target="_blank">📅 04:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هگست داداش اگه مردی چنتا جنگنده بفرست باز کشور تعقیب گریزی شه
موشک مزه نداره ترس داره لعنتی</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80490" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گویا اراک و زنجانم زدن، موشکا تاماهاک بوده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80489" target="_blank">📅 03:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80488" target="_blank">📅 03:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پارچینو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80487" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/80486" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شاهی علی الحساب یه‌مدت شماره ناشناس جواب نده
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80486" target="_blank">📅 02:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شاهی بعنوان کسی که مارکت شناسه میگم
پول ویناکو ندی بدبختت میکنه خوددانی</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80485" target="_blank">📅 02:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE_ZRL1NjGhoBqaoL51E1BMT5Gmnq7g67cf_YApRwcMsjNmJNRgsV38GcpX--565Qxt_euNradT7Ui3zWP4SpbDFcQ7y6Nguwln9IWo-WEDAEmoLz8n26hJ1HI25GsqIUshZ851zPRlYp6EqnMOhHBWe8pAkALS6dIAQaykBDbOZ-3w7U-hQV5Qf1XRhyZWkqI948wiuAd2H45ogEL76xHaTgfH_ZfgW9dGdOdfxjGKVE5f3_ABssZOtkI8LdlHbkSgTmpjB58YEbVqO4TGLwlY4BWRkdzckhtrQQyesABQjG-UvY6k17EAnHw2q_Nk6oKw6wBhvnHyqgZDntizANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که بیشتر از من فن مسیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80484" target="_blank">📅 02:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8jHPsqOdkxAcRzXuKft9ulNcPGCj2uiyAFNlXu0J1iFZE6BbA4B8rnFlvC-L2eTmzbWhZStPzuEvXEKvPb2LrR8IEfIkBFalH2EEYyWlp0Yq825hzqWkKLrtNS2N67lEwxED_bHbxpCguJLYfIwd3-cT0WkXjD-9X0DS3d8m5I8wQ3CzzIvF8i6fk-V5EyQXwGNVhXsj1GrWTouHTTUTAqEgMC4lelJexyb2shrFC3jGQxvk_r0mXY7utJKuZXHwnT7C4jZe66kvey2bsFOuU2LPLMvztm6_U2snpVd4RLSZY1eNhOZZiCYbxgp6Os5wsZ02ttrcjx-oIToT6TN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان مثلا چرا مجتمع سپاه باید بغل بیمارستان باشه
بعد این فقط یه عکس از چندین عکس دیگه تو اهوازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80482" target="_blank">📅 01:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">متاسفانه گویا امشب حمله به بیمارستان سرطانی کودکان داریم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80480" target="_blank">📅 01:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ننگ بهت ایرانی، گرم فوتبال شدیم ندیدیم چیکار کردن با اهواز</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80479" target="_blank">📅 01:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z008XXkEcBgl1m_AT_vHlp1W6_0OiuWjFKL4e0F2hQElDMtCL4_nURcTp05eZjx5zifrq0bOI4hVNYloPDrqVi2ol-EOkIFk229uvz_t0CLcpd-nlGRNd6TCDLOCHlb_gRcWNuEK821P5TykxOstOQpUbbQaMJkiAVzNxhyGG3uMxYph2y4gtHDqTBcsp5fMyKNvsTpFot7y45IF6TbxGHtp7uWIEQ_oZ42nyhlfRJAJZXKV5Lm-EY_piXG4pVdUvysBTDv7QTq_Difg5-Ta1L9quD18CaUcihBsFz9agQw8uhA9pCoLd5r7cFT7LUDJN3PKUivgoj3as7DLbn2GeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcIqo9bh6PUJQjzT9iTs0YfpAgMlUoNf89qIiuMW59V_4Ra6wWpC4m_ABhyUdXwDPVb6T6ytS-AAfPtIZnBFcEWFvCfakjoEduLtAB9RBt3bxvQVPCYIOFHNejuJcCuB81WT790BF-kCgnl_KGj6toukf6Q2dmZi2jLRrHZJwwhsMAlESjKCK8-mjPRdEtQ_u77uZh0hj9bXS6NlzwO0s2NLXFDpYos60g0h7D6O1D76gkSLrEVqgHlbrw6VAbTNC1GscJXQbC1RBn9MVmmpyjMn71tzkTRPt65U6l-vuTwd7PB-caxbS_WF3mjWLLc-C1jj4DTs7x23UTv2o_I_VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یا عباس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80476" target="_blank">📅 01:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEqwlwjvR9qaCW7DGajd7friNbRV-f-3EQWLxYO8zeM0R_ouXASIIRN3QUwBnsAHnInhe68QTr5N7apHhErx5X_6vceYBENGqQuqFj3JMJGmklWtCPzba1vivOuWsZlsq0VwYXDAuFxEj20N978Iych0DvgcoUA_p-_hXvL84UDwqXlfMie7sHZ0qNr-YCxCnMhujXKMZcDn3ocyQfE_c8Kov0E1i_Mha4Y70VsvliQZAg7XgAYYsnwLbEOS2otrt_h3uIL5rH5uvgTpbG-GNTXfGXLyhO3QSqxL56dywXCeuubEmYsZbhPSLZxKGQrpXn0TT2pM1wkyovwEZqcX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزا جان ببخشید
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80474" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رونالدو فنای عزیز صحبت کوتاهی دارم،
جدای از اینکه جام رو یا یامال میبره بالای سرش یا مسی
باید خدمتتون عرض کنم که مسی اقای گل و پاس گل جام جهانی میشه و توپ طلای بعدی رو بهش میدن.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80473" target="_blank">📅 00:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ساکت شید شبهه علی دایی نواخته
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80472" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromvahid</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlpQkKhE9LGiphJZCNB_zSDyztRbV200z6Mr-KT_HMFXv6GrA6Y0hRHA97QSnYjGDiO2As063cZVMtRsViUv8FFGNPduEyQn86josieyl_1laVvY78iElMddJ1yWYuNl-8bCC6f2pGspoIRLNl6_osQUj9RV89jlVoFxnAIgQxRfv2onc9SnQjZMuEMf48pcvvKVCX_j_mlYqkrEMNalbkHz9sPFHeMA6FfF0NMjDPoiCNpSOLF8jlj7mvP04HGOa-809ZCQFfqechzstVC35u3Y4q4ftugK6krUS3CHXAExLxhitM5C0Aw_lBggkj0BWj0BTc2LysoLCIJ7kZLbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم ی سری جذاب و خوش چهره ، جلوی این گوژپشت اوتیستیک کم اوردن
😔</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80471" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تا ۲۰۱۸ رونالدو رقیب اصلی مسی بود
از ۲۰۱۸ تا ۲۰۲۵ امباپه
از ۲۰۲۶ به اینور هم یامال
تو دیگه کی هستی پروردگار فوتبال
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80470" target="_blank">📅 00:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان بخدا کلیدی ترین بازیکن اسپانیا رودریه، چرا انقدر عکس یامالی که تعداد خطاهایی که برای اسپانیا تو جام جهانی گرفته از گل و پاس گلاش بیشتره رو میزارید رو پوسترا</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80459" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80458">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صداسیما: شدت انفجار ها در اهواز بالاست، در خانه ها بمانید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80458" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سجاد شاهی ویناک گفت پولو ازت بگیریم بدیم بهش واقعیت</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80457" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انگلیس عزیز تو امشب به صورت استثنا فوتبالو از دست آرژانتین نجات بده ما فینال از اسپانیا درخواست میکنیم مجددا فوتبالو از دست شما نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80456" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va99D0AkId4uVsaOKoij8gDqwLkQ7EYWzy6dTHrM4HvqQlC33VElTb0meCqPcnyicQ5hPjsCTuirQzYu26Ee3KO9qKiFqiLowNpWG-0N6Ww2KsD8F0ugZXyqlcBWyk7KBM9quFyvUvUCAQNWtQ_AXSl2BvGOIzyMg3wIVdDJu8qAgaiKypdm9MitlZnkyM3uWFf2B1yZ6DJLKK-3doYYKJVPP6tR6tBmfrZZnUaW1FNhgqwn3zz6iZf0kXjqX42mF_NwIbvNaxbY__itiNsip5OzKUM_RBAgjQmQpWTTolR4QvrgfSo20puRn9XY04Z1RWTpOU7mqpl7czOm4V-zvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام سلطان رو بگیر پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80455" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حالا از دکل کی میخوای بالا بری رئالی
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80454" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کوکوریا دکل بعدیه فک کنم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80453" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80452">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فینال بین بارساییاس محض اطلاع</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80452" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80450">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تموم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80450" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این مصدوم شدن بازیکنای تیمای بزرگ مشکوکه
رونالدو فنا پیگیری کنین بیکار نشینید
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80447" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شاهی ویناک پولو نگرفت بزن برا من</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80446" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">توپ طلا نهمو بیارید بابا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80445" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80444" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وای وای</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80443" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80442" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دومییییییی</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80441" target="_blank">📅 00:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اکثر تیمای بزرگ مصدوم دادن حذف شدن</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80440" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔥
تکل موفق از جود بلینگام</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80439" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUK8WZlIc7fUvuu7HJrMRNjg3CZqPbZC6XStpkybykLbPpRvUd1uRM-wUrQrW0dUzjFrEpkXg8_bgpQhZ0vj3oyqMVNoZmrWpVCeZqcTQ9dfTKCXqbhkbp4ZMJXOGDMXkdCgWXyWWUo9Loxype809X4m0rtD9ZvUIAp08Ak02hkeD9EFEQCMW7rUcx4b1qxXb7E_02Gj-c0zN_NFPWgqr5w-qBZ8SJl0VcNDDntIpcQMAgWUJ3RWPUGdBt2C84hDtvddKExcwZfGrfltUnW7oj2Qa1yKPhbOi4qk4WSfyoJrJav4R6EEk7_vH0sCTYOdFiX-Ad-d4VFotzhRHOTunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مسجد برکت میام برات بمالم</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80438" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80437">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خدایا کیرتم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80437" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80436">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آرژانتین زد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80436" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80435" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیکفورد چربش کن مارتینز اصلی اومد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80434" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مسی باید تو اوج خدافظی میکرد تا اینطوری یه بچه کون توپو از زیر پاش ورنداره بره</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80433" target="_blank">📅 00:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80432">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خدایا امتحانمون نکن</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80432" target="_blank">📅 00:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80431">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">واااای کیر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80431" target="_blank">📅 00:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80430">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چی گرفت کسکش</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80430" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80429">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مسی کیرتو بکن تو بکام کصکش از تیمش برو</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80429" target="_blank">📅 23:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80428">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گوردون برگرد نیوکاسل کصکش</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80428" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80427">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انگلیس زد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80427" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اهواز به طور متعدد و وحشتناک صدای انفجار میاد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80426" target="_blank">📅 23:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این بازی عجیب وایب بازی آرژانتین هلند ۲۰۲۲ رو میده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80425" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نروژ عزیز لطفا تو دیگه امشب فوتبال رو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80424" target="_blank">📅 23:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اهوازو دارن میزنن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80423" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زلاتان ابراهیموویچ:  انگلیس دست خدا رو قبلا دید، امروز پای چپ خدا رو هم میبینه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80422" target="_blank">📅 22:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلاتان ابراهیموویچ:
انگلیس دست خدا رو قبلا دید، امروز پای چپ خدا رو هم میبینه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80421" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80420">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پایگاه‌های آمریکا در اربیل عراق مورد هدف قرار گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80420" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80419">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHeSaM</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFY4Oc3xJIs4YtumEhub3nElU1meNOQ9j05Js21obj6uMKF5ubKESTsNul254ubyfomxmproJwsgY66AXuavqWUqFaYddMLdDJDFunfM0tNYXgGYHsgMSzy7DRLsnbgGrRh-1zXYBRXZf8hnYNFHvoG0a-D9csLeMUBB5Kvre6EmWTqTxZEXP1aaDb6rwpeKGq8lo50FtK3K6PPZfic2nDIfYouD-YmCeZzDZwsbRpZ1SEqR3MY7zb3maYyRnq0MvfQz72girclpOY88LrlkaYROdyODhqRXtQ-0GHx1cyVlTh3SYRf2Rvku6SDuZyYBroFu3M_SGg6-VkRyPMyWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرتون وینه؟</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80419" target="_blank">📅 21:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jzuv2NyqKQaaR30IHKgsurbiBZnfTG-QmP1vjOKp3j2tTrZn8fGYrArHyWylu9Tf1W3Hn56mkyXIbig5MnMKxTe5B1RkSQ22tf9uoyExPhrtl099TBk9-FodrQgSBdhalr-rKWiR4bXLLA9F887EgjqigqQP0Ttb56XSfLt7AE1oFFaT8KCTZbxOoZfV7ZA9apHa7yHySFkDw7sYp51Uj5s7_ptd_g-jRYjb4Hoj3FdDgPnSECah0-grgPdTF-h9Nin4_sq55kvGNzsxhdS1I5VRNVwPGv2QEActRp9Cx2PIOrSIbateWyQrMmrd-bskSHXWM3HJNrOyKmPLlHEQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واا مگه میشه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80418" target="_blank">📅 21:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-FA</strong></div>
<div class="tg-text">واا مگه میشه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80417" target="_blank">📅 21:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80416">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تیم برنده فینال میره برا سوپرجام با پرتغال بازی می‌کنه   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80416" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80415">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تیم برنده فینال میره برا سوپرجام با پرتغال بازی می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80415" target="_blank">📅 21:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK5taCZ5gUm3Lr9SO2Fkl1__l8j1lvX3NKgY7cLkF2K2A0hguBjXMgnOr8Cx_gkT3PYDEkrL9jQEFnszZTRrdmOr8zIwB1N9XXNpN5Kyf0OcruBCPn5_jSslC4VHF4z8PgXv1hZDXtAEYHOOswrsqjEEx1poK9vvNKGVUpQdSVxXhXg6xZMN1Dr_LB1-jZsJJuk_2Zy2Cnnd5mdtkPM9JMDgo-C8XsAtRmgQpSfEqwatQp-ipKGVqG20scVf6WKEKuSsJlfQUWPZgGvmjnxpy1xe0FkB641pV4jNAwjWkq6TxgJOOBYtvvIG8sGICp2RAF2yVfYr7zeSP-MJWKKK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب انگلیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80414" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بیچاره فنای رونالدو اگه امشب آرژانتین ببره ناچارا طرفدار اسپانیایی میشن که پرتغال رو حذف کرده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80413" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdcSGgEWQvvpUJZ3EGzB85Yd4tjGGfvacR0xmPmtqxz0PGaBEOeKyoI7qFLRlLs9pLcplqA4l4ODiBnwMAIifTpX3RopwP_EJGGSLa9hXcIPdIb7uPZiOqCaql4dfyg-z5eRbu-JJcFpjyN7vbIDw7OE4jkgDjfRD43siQDJ1-6Q_NavjdVhwdk0tYsPe6q5ggIuU6mYm3_SvOR8j6EoscYjt-EzRVOrWuvIWIn5fIZNrvzAGaJC1JDSk5qPZuJaDmQ33nShGV9f2XwCPel8g98YjDDfOCxd8ts3stDrMB7WZM6TorhrtnY_dI6JXgP8BYRNWBf6HZEhtw6MJX_fLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب دومین فینالیست جام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80412" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SobaX8t31kNRcqaERLDZPrSs7uoKWPgefXuYAS_4P3U4wirJ-6IcnB3eGqCMOPKC9GnLvnG6hrHqBILY3tAv800vruetRpjW_7tyHCkAlOmxKlpLiprTJVTJk3qV0YtrHPpF0aRH7mV619XhGNOfjYy0GPLzuXoAkz72YvgMvSBcEsOjRm0D5R_ww-1lGzdcEEEmV_LEvzXxde8n1FG57ynB2VhDY3n896WMMyaDVx3mFhVXEF4oemll5q1IVH_OOnWTkLHUPbiZPAsHG3lxncwUkUzB4OkiOWTxMe8-GqT7cvZoBLCh99MQV1nipn7NiHzhuMdsD8mA170yrYqMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ۵۰ بازیکن برتر جام جهانی از نگاه مجله اتلتیک
پ.ن: گشتم نبود، نگردید نیست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80411" target="_blank">📅 20:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80410">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اقا مثکه ویدیو قدیمیه ولی خبر اعتصابات واقعیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80410" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e52b5708d.mp4?token=cuGuSZvbuZmL56DYPIW1zKv_hJ-azdIUPSwjJWL2gStirAbYkpdQ6zUy3MvNpGlx9r9RzTXY7jGW3FVzqxu_-zAZo2XA30s8nY91LXpTaQw4euPJLj3SvHFrD2DBPUduuvZB7yMgH4azSyQ-qH7Xcp8cctq44l-Dq67uY4tCvjM_HzTxIkoCm83CBiqsccJn-jinmsLmzid0fCjndwN9DgNqw3xBM761u1PuwyfK9WE-x2Dd6GNE_ydZTZKnkXgmNpWrchoHrKslZPKRtPdu5U0-QXM6zmKac9x7kuP-2L0fWBj1LDQgZbVxfjU_hNNEq6qycaNpQwS2mz7jV7-hIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e52b5708d.mp4?token=cuGuSZvbuZmL56DYPIW1zKv_hJ-azdIUPSwjJWL2gStirAbYkpdQ6zUy3MvNpGlx9r9RzTXY7jGW3FVzqxu_-zAZo2XA30s8nY91LXpTaQw4euPJLj3SvHFrD2DBPUduuvZB7yMgH4azSyQ-qH7Xcp8cctq44l-Dq67uY4tCvjM_HzTxIkoCm83CBiqsccJn-jinmsLmzid0fCjndwN9DgNqw3xBM761u1PuwyfK9WE-x2Dd6GNE_ydZTZKnkXgmNpWrchoHrKslZPKRtPdu5U0-QXM6zmKac9x7kuP-2L0fWBj1LDQgZbVxfjU_hNNEq6qycaNpQwS2mz7jV7-hIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتصابات در بازار چارسو و علاالدین تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80408" target="_blank">📅 19:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80407">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwLbgtSHgVDZ7Zt11HKG3G0aWdR_cfYtm6m0GoOsJmKpn2dKXQBRa31BKKngMiMjrSGHkX12eaV4TnUhXGAf8jwQingA3ja-VvO7cNY9YGCuB4fBQU4sVDXrr_7Hnk12BrTEqzQg2CCVhmb6gwynCtwK6OXknLSza-_BZUYF4bxNt3wfk_2hfWljbiVF-5sQJoTKM7xTA_G3zNPFR9KaqXHm94yeLchh_P0OQRkuYacj-vF-kVePYHc7RCHxBbtsPpZgV5Z0k5_-DLGv7vKqAWkzY_5rsSHMQx2nGK7zJyUrsiHddCrtPxx0c_PSBeceyaL50DsL-w-v9T6nPMoHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا بخدا
چطوری روتون میشه با زنتون سکس کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80407" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80406">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-HFBQSOmstNa6mxBddfV8ky6nlpm3HtfB7APutWm6lC8csofrjRv_xfAE8tDe5BcVjC91mRl8T7e-iTU5Py9vpuRJcSk3LMzoX9t7CTE99Ul3jnXhtd1vGw1aKVz6-Wx8keTNqPF4-da3XoJhg3kRbf9hkgxHZRCylLFSUoIiCqMfv5BP9s-0zzFtVFWEbAKvKuxUNfrbJuMZmDcEF5E4kbG1A6X9BTe9MJQUZXHQ7JoeNEBVY_sw6hKB30gutGFRzkzZmydV668HbdEWL_SsutTap86oMvqZDbPrjYEDlGO4Yx5POq6Zr_tMC51y9rGm1spU1voa8i6dwCfmXo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g24
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80406" target="_blank">📅 18:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80405">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICBc9ojYjC04GK3jHZdEa6dYhaBaWQJJvgIIBr_L40FBhT9g8j68TDDqGRg8sacAS2hX09K1LADswRREnkUxfoWY-fM1kGzqT6KGYX4dr-YjZUHtDuN5VBsCa-V0afVmQn5D9GqO3v-K2MAE4PtRoOKQCxsQANwy1i7puIIWGDazmrGkBuLavdtPCT8yG3x0Dvom8EPmnYMGskuj5VDYH6mAtBkzHEAPtFUG4nDV_37IEz9-xOGb0tE5UH_HhFqNZb-oitaAtHdRrme1_C7y2t-sFo7ysrhzaOlWeYwY-DlygaLjhI8EFF1UL-Q5YeHwO5JLnh1hno7bkWiW5_Nsfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاخارا بخاطر پسر خوشگله ببندید رو انگلیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80405" target="_blank">📅 18:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80404">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به به به این خبر
عظیمی راد، نماینده مجلس:
به آقای کاظمی دقیقاً ۲۴ ساعت فرصت میدم تا امتحانات نهایی کل استان‌های کشور رو به تعویق بندازه وگرنه برخورد نظارتی شدیدی روش اعمال میکنم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80404" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80403">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کصکشا حداقل برق دکلای اینترنتو قطع نکنید</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80403" target="_blank">📅 17:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80402">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQnyfeEZAK8IE0V9D1Wtvpn4NfiVTEdMe4UEEP56hWJOVR8FXI3o5kehfb_2BNa368kjNVf0EUWRInGqYEs_okv8gNunHmq0RjmSka3DvkyRy7VQRpnaFvvFiXzl-hvWrqFsWZY-1qIbAs621QjOy4jjPNIvhzIwr8Mfag228RY6pV7D2XrecH3NQSq_k9coN9ZrOqP3DRWUiZRF0AGMYb5piaqUzoNR1kARcMx4Dh4Le-gCoFQork8vY5qnNTjTWkG7NFys0hoiPDkXOESrXWn-5nXbcq9NoffmSfhYNkPxlBKf77yNpNuhjFlI7Mb9vQKq0x1E9CJyAlPAmHIubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیک علی تجزیه رو از صدای امریکا زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80402" target="_blank">📅 16:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80401">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPPmKByVtPveaZJc_K10vyu7PlB4t-Ex_gct2bwjjKDBzy7TO5lm5MZQSc5DqSNDs7YdsFFjHVl6cEpqPNXOFrd714Z3fdMFHE839CMiHSYiQAmAo0cKrDDRzrziqCYn3DFwFsy9UupfojCFsOKxskNTFxuPxplc_PArEVR_Bs7ARdv62fhLHnq8bAcItP99XiQqqcSJU3hLcK4aetYtCNOb8PLcWgmr-BNGKXxvrsCsX6UYXZGVVQq1NV3poZRLuqUrsTjdxmqC6oOw7vsMu0zKTtFwEYVE6VGl_mo0DVOp8mgWzrDKqkJUinBE_jsf20hCgIYshGmXAIGPwrvYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چی بود دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80401" target="_blank">📅 16:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام اشک ریلیز شد  Spotify  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80400" target="_blank">📅 16:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqVoDuHnUCEGLm_pJ_XIpksNxev93gePLK0hSg8DIH3Ug8QyWgDAPGXdQb7a1231LojD91d-IBlRR44moNc1I2Ui2MlTP05SKb7trSx91-qnvQJL6FGWO9pkehTZP7HhpaxpoWCtDX4GYJ-HYBvxgMJhd_wUGOH-47QBJ6XsL2lUwrFv0ghPzsNRu8wvsg2C4aJ8DlLKuAzy0czE9D9S_NaTUWTu1CuoBeMnRADtksz05zvsR3iXSz8AqwGaPTeUZwq2iow7_ZevxSJI67oJNvUzO8i6f26to4PJ0Jx6IFkkCq1uVCiUISEebe3RPwPguTxPgb-x5322z_xsMHEW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام
اشک
ریلیز شد
Spotify
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80399" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عجب ترکی دادن لنا و مهیاد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80398" target="_blank">📅 16:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyBvrXiq-QZAa6iDJiCTWAweIHURL8n8h9RXTYjRaUJXqJw-x9EM0Pm2jojKaOQFan06R0tVBgD55fdN4JQpHv3Ai1pZnELB0OMXT9dcWIg7y9d0gN8EfcSMKNTOJ6RFRpLZP9eV2nwkik0vK4IW98nlY_tUjB9lEfLIjjt7Vs7yfCQ5Urdk4kEelBuzHnR4KljwG_RcFhAKtZlfDiDRxtGZ71l0RfPVfZJmbxJUKzhvtKolhymgtQPrejTjuoimQHCNEGl6CyJdRNgMaQCcmC6EsF7zfkz0BOnai6cpVMDv3WyGehTKBw33HIMKdIi4orWnx9gomgxYulSEA5ewSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80397" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جدی مملکت هیچوقت اینقد رو هوا نبوده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80395" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80394" target="_blank">📅 14:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80393" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">که اولیسه و امباپه و دمبله قرار بود کوبارسیو جنده کنن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80392" target="_blank">📅 14:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">زمان جنگ میگفتن نیروگاه بزنن هم ما برق کم نمیاریم، حالا که نیروگاه هم نزدن روزی ۴ ساعت برق نداریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80390" target="_blank">📅 13:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تا کی باید تاوان جنگ طلب بودن چارتا پلشت مثل جلیلی و رسایی و امثالهم رو مردم بی‌گناه بدن؟ دیروز بچه های میناب امروز چارتا سرباز بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80389" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حقیقتا تصور خوبی از این که همزمان با محاصره سیلو گندم میزنن ندارم، خدا رحم کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80388" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">محمد امینی دهاقانی، از معترضین دی ماه، متاسفانه در بامداد امروز اعدام شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80387" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80386" target="_blank">📅 11:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر خزانه داری آمریکا اعلام کرد چند کیف پول دیجیتال مرتبط با بانک مرکزی ایران را تحریم و بیش از ۱۳۰ میلیون دلار فاند و بلاک کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80385" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80384">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPSWBpp4eGZBJtuFU89r69_vLI3MdOSeyDyb8HrI4r7yuQa9hhhlf82oTWRCoQdTNI0z5NJyupDObpCRbCgglIUhWW_56fXNMNVHnUuSrNHsy27CLqwEY1kTJLKbq1HgPLO3HbSKy44ffQ3Z67bQuxztchp0u0lVShNKnYsklSmmP45rTtix4WdJYkFL3yQuluYebkqoZU11xIMZe15DgDEXuqBwxnFOU3FLEKvOcoBng-LIEBZcMX9kZRTrkMqsQ47ytNBgfhuwX4Bl6JqIa4yw2xI4vamGMDjn5AgltMIg-ZAlqq3cc5ziKV16DfL6s-KPBP7bU4f5VxmQFJXpqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تا الان توی مرحله حذفی جام‌جهانی یدونه دریبل هم نخورده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80384" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80383">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPH4NyMbiDjO-8IDDXnDMyuxU8XoZ-JWZpsKkDtvqesrz17gl6CigivmWH9b-8FB0uFSzJBdeZAgKi2fxetYvHzN7fcQgL_UGjX1qkgbNC_511TasQGCqUl7dm6HbtC9-gxMckhreajmfwdR9ReuJPXFq-vDDs_J6G3MOLiv7w3mu7zDLZNNsyABXXEM330eEYLhctsXnum3NKp4iTfEo7nIII0i01JNlXdqR_hRYezRcOkS8X_A1257hlx4KK3RAGeqjYNR-YEm6LU4vld6PfTWepqW7qBiU-M0pLj5uthR0Apg1R6vw58SRSJ97Kw4ZjUAuUz1OAuU4Twhn7EjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید داداش یامال و طرفداراش :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80383" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80382">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pptpSfn4yVynfDdvw6SC9RQnr834UeTtRwWFf1Imxpqys33mE-sADLCC6gcgVVRCpXzhEabkYot5KYzcjZt0m9h7GKaFE8p4H6LBrzHoDV3ZuPR30_p21EA-DF0GwbdvaZnYd6caimifa1reA6JDzTKIHGHYBbHjBLBx4bBam86eRYxo57vW0Ixxw1y3PFoUvTt_zdbJmXnpicaqIZ4bPVMU9Urjgaw5GwpyGRNUUpJ3NpRkGYHgSmqJDbKxiYZSZ2xOiD5xJy9JhHl97WYOC86uDvQwXnyxdV-WXgWqTtmN8u5A0hrPkkV0gMTnlTajvNfdK1abcT2lmmrsMZCN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80382" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80381">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جمهوری اسلامی ایران اعلام کرده زیر ساخت های استارلینک متعلق به شرکت اسپیس ایکس جزو اهداف مشروعش خواهد بود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80381" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80380">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80380" target="_blank">📅 05:05 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
